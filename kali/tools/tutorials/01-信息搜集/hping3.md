# hping3（自定义 TCP/IP 数据包构造与发送）

> **一句话**：像 ping 一样发"任意" TCP/IP 包——自己决定协议、标志位、TTL、载荷、分片，用来看目标怎么回应。
> **分类**：信息搜集 ｜ **Kali 包**：`hping3` ｜ **官方文档**：<http://www.hping.org/>

## 1. 它解决什么问题

普通扫描器（[nmap](nmap.md)、[masscan](masscan.md)）已经帮你在"发包策略"上做了决定。但有些问题必须自己控制每一个字段才能回答：

- 这个防火墙到底是**丢包**还是**回 RST**？（换个标志位就看出来了）
- 路径 MTU 是多少？（`--dontfrag` + 不同包大小）
- 目标的**TCP 序列号**是否可预测？（`--seqnum`，老式 IP ID 隐蔽扫描的前提）
- 目标在不在？但它**禁 ICMP、也不监听任何端口**？（发 TCP NULL 到 0 端口，看谁回 RST）
- 这条路第 5 跳的 RTT 稳定吗？（`--traceroute --ttl 5 --tr-keep-ttl`）

hping3 就是那个"手工构造数据包"的工具。

| 工具 | 定位 |
|------|------|
| **hping3** | 任意字段、单包级控制，教学/排障/规避研究 |
| [nmap](nmap.md) | 自动化扫描策略 + 服务识别，日常主力 |
| [masscan](masscan.md) | 只追求速度的大规模扫描 |
| `scapy` | 编程式构造（更灵活但要写代码） |

> **hping3 的默认行为很特别**：默认协议是 TCP，发到目标的**端口 0**，窗口大小 64，**一个标志位都不设**。这种"TCP NULL 包到端口 0"有很好的概率**不被日志记录**，是最经典的 "hide ping"。

## 2. 工作原理

```text
   hping3 -S -p 80 -c 3 192.168.56.101
        │
        │ ① 构造 IP 头：可以自定义 TTL / IP ID / TOS / 分片
        │ ② 构造 TCP 头：源端口递增（用于匹配回包）、自定义标志位/窗口/序列号
        │ ③ 附加数据：-d 指定长度，-E 从文件读，-e 加签名
        ▼
   ┌──────────────────────────────────────────────────────┐
   │  raw socket 直接发出（libpcap 或 Linux sock_packet）  │
   └──────────────────────┬───────────────────────────────┘
                          │
   ┌──────────────────────┴───────────────────────────────┐
   │  libpcap 抓回包，按"目标端口 - 源端口基准"匹配请求     │
   │  打印：len / ip / flags / ttl / id / win / rtt       │
   └──────────────────────┬───────────────────────────────┘
                          │
   收包格式（-V 会多打印 tos/iplen/ack/sum/urp）
   len=46 ip=192.168.1.1 flags=RA DF seq=0 ttl=255 id=0 win=0 rtt=0.4 ms
```

关键机制：

- **源端口递增匹配回包**：hping3 从随机基准源端口开始，每发一个包就 +1；收到回包时用 `回包的目标端口 - 基准源端口` 算出这是第几个请求的回复。`-k/--keep` 可以保持源端口不变。
- **标志位组合**：`-S` SYN、`-A` ACK、`-F` FIN、`-R` RST、`-P` PUSH、`-U` URG、`-X` Xmas、`-Y` Ymas。可以叠加（如 FIN+SYN 用于某些规避技巧）。
- **扫描模式 `-8`**：把逐包发送包装成"端口扫描算法"，是双进程+共享内存设计。注意扫描模式下**大多数 hping 选项仍然生效**（比如要用 SYN 扫描就得显式加 `-S`）。
- **文件传输模式**：`-E` 读文件内容做载荷，`--sign` 打标记，`--safe` 在丢失时重传，接收端用 `--listen` 收。这是 hping3 的"隐藏技能"。
- **`--flood`**：不关心回包，全速发包。**这是 DoS 能力，只能在明确授权的实验环境使用。**

## 3. 安装与快速上手

```bash
sudo apt install hping3
sudo hping3 -h | head -40
sudo hping3 -v          # 显示版本与所用数据链路层接口
```

最小可用命令：

```bash
# 1) 用 TCP 做存活探测（穿透禁 ICMP 的主机）
sudo hping3 -S -p 80 -c 3 192.168.56.101

# 2) 对网段做端口扫描（SYN）
sudo hping3 -S -8 1-1024 192.168.56.101

# 3) traceroute（默认走 TCP 到 80 端口）
sudo hping3 --traceroute -S -p 80 192.168.56.101
```

## 4. 核心参数详解

### 基础选项

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-h, --help` | 帮助（可管道给 less） | — |
| `-v, --version` | 版本与数据链路层接口（sock_packet / libpcap） | 权限问题排查 |
| `-c, --count <n>` | 发 n 个包后停止（等 `COUNTREACHED_TIMEOUT` 秒） | **不加会被无限发送，务必注意** |
| `-i, --interval <s\|uX>` | 发包间隔：`-i 1` = 1 秒；`-i u1000` = 1000 微秒 | 默认 1 秒 |
| `--fast` | = `-i u10000`（每秒 10 包） | 快速演示 |
| `--faster` | = `-i u1` | 极快 |
| `--flood` | 全速发送且不处理回包 | **DoS 能力，仅授权实验环境** |
| `-n, --numeric` | 只输出数字，不做反解 | 提速 |
| `-q, --quiet` | 只显示启动与结束摘要 | 脚本化 |
| `-I, --interface <name>` | 指定网卡（支持前缀匹配，如 `-I et`） | 多网卡/`--rand-dest` 时必用 |
| `-V, --verbose` | 详细输出（多打印 tos/iplen/ack/sum/urp） | 分析回包 |
| `-D, --debug` | 调试模式 | 排查接口/链路层问题 |
| `-z, --bind` / `-Z, --unbind` | 把 Ctrl+Z 绑定/解绑为 TTL 增减 | 交互调整 TTL |
| `--beep` | 收到匹配包时响铃 | 演示 |

### 协议选择

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| （默认） | TCP | 默认发到端口 0，无标志位（hide ping） |
| `-0, --rawip` | RAW IP 模式，配合 `-H/--ipproto` 指定 IP 协议号 | 协议层实验 |
| `-1, --icmp` | ICMP 模式（默认 echo request） | 传统 ping |
| `-2, --udp` | UDP 模式（默认到端口 0） | UDP 探测 |
| `-8, --scan <ports>` | 扫描模式：`1,2,3` / `1-1000` / `all` / `known`，前缀 `!` 取反 | 如 `-8 1-1024,!known` |
| `-9, --listen <sig>` | 监听模式：等待含 `<sig>` 的包并打印其后的内容 | 文件传输的接收端 |

### IP 层选项

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-a, --spoof <host>` | 伪造源 IP（**回包会回到伪地址，你看不到**） | 仅授权环境；需配合嗅探 |
| `--rand-source` | 随机源地址 | 压力测试/状态表测试，**攻击性操作** |
| `--rand-dest` | 随机目的地址（需形如 `10.0.0.x`） | 需配 `-I` |
| `-t, --ttl <n>` | 设置 TTL | 配 `--traceroute` |
| `-N, --id <n>` | 设置 IP ID（默认随机） | 分析目标 ID 生成规律 |
| `-H, --ipproto <n>` | RAW IP 模式下的 IP 协议号 | 配 `-0` |
| `-W, --winid` | 按 Win2k 之前的字节序显示 ID | 老系统 |
| `-r, --rel` | 显示 ID 增量而非 ID 值 | 分析 ID 可预测性 |
| `-f, --frag` | 分片发包（默认"虚拟 MTU" 16 字节） | 分片重组测试、绕过弱过滤 |
| `-x, --morefrag` | 设置 more fragments 标志 | 触发重组超时 |
| `-y, --dontfrag` | 设置 DF 标志 | **路径 MTU 发现** |
| `-g, --fragoff <n>` | 设置分片偏移 | — |
| `-m, --mtu <n>` | 设置虚拟 MTU（配 `-f`） | — |
| `-o, --tos <hex>` | 设置 TOS（`--tos help` 看取值） | QoS 实验 |
| `-G, --rroute` | 记录路由（IP 选项，非 ICMP），并显示返回包的路由缓冲 | 许多主机忽略该选项 |

### ICMP 选项

| 参数 | 作用 |
|------|------|
| `-C, --icmptype <n>` | ICMP 类型（隐含 `-1`） |
| `-K, --icmpcode <n>` | ICMP 代码（隐含 `-1`） |
| `--icmp-ipver` / `--icmp-iphlen` / `--icmp-iplen` / `--icmp-ipid` / `--icmp-ipproto` | 设置 ICMP 数据里内嵌 IP 头的各字段 |
| `--icmp-cksum <n>` | 设置 ICMP 校验和 |
| `--icmp-ts` | = `--icmptype 13`（时间戳请求） |
| `--icmp-addr` | = `--icmptype 17`（地址掩码请求） |

### TCP / UDP 选项

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-s, --baseport <n>` | 基准源端口（默认随机），每包递增 | 需要固定源端口时配 `-k` |
| `-p, --destport <n>` | 目的端口（默认 0）；`+n` 每收到回复递增，`++n` 每发包递增 | 常用 |
| `--keep` | 源端口保持不变 | — |
| `-w, --win <n>` | TCP 窗口大小（默认 64） | OS 指纹参考 |
| `-O, --tcpoff <n>` | 伪造 TCP 数据偏移 | 规避研究 |
| `-M, --tcpseq <n>` | 设置 TCP 序列号 | — |
| `-L, --tcpack <n>` | 设置 TCP ACK 号 | — |
| `-Q, --seqnum` | 收集目标生成的序列号，**用于判断是否可预测** | 老式 IP ID 隐蔽扫描的前提 |
| `-b, --badcksum` | 发送错误的 TCP/UDP 校验和 | 校验和校验实验 |
| `--tcp-mss <n>` | 启用 TCP MSS 选项 | — |
| `--tcp-timestamp` | 启用 TCP 时间戳选项，并尝试推测时间戳更新频率与系统运行时间 | OS 指纹 |
| `-F/-S/-R/-P/-A/-U` | FIN / SYN / RST / PUSH / ACK / URG 标志位 | 可叠加 |
| `-X, --xmas` | Xmas 标志（FPU 组合） | 规避技巧 |
| `-Y, --ymas` | Ymas 标志 | 规避技巧 |

### 数据与传输

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-d, --data <size>` | 设置载荷大小（总长 = 协议头 + size） | 路径 MTU 测试 |
| `-E, --file <file>` | 用文件内容作载荷 | 文件传输 |
| `-e, --sign <sig>` | 用 `<sig>` 填充载荷开头 | 传输标记 |
| `-j, --dump` | 十六进制转储收到的包 | 协议学习 |
| `-J, --print` | 打印收到的包里的可打印字符 | 提取传输内容 |
| `-B, --safe` | 安全协议模式：丢包重传 | 文件传输 |
| `-u, --end` | 文件传输到 EOF 时通知对方并阻止继续接收 | 文件传输 |

### Traceroute 与脚本

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-T, --traceroute` | traceroute 模式（隐含 `--bind` 和 `--ttl 1`，可用 `-t` 覆盖） | 支持 TCP/UDP/ICMP 下的 traceroute |
| `--tr-keep-ttl` | 固定 TTL，只监控某一跳 | 观察第 5 跳的变化 |
| `--tr-stop` | 收到第一个非 ICMP time-exceeded 就退出（更接近 traceroute 行为） | — |
| `--tr-no-rtt` | 不显示 RTT | 减少输出 |
| `--tcpexitcode` | 用最后收到的 TCP 标志位作为程序退出码 | **脚本判断端口开放与否**（SYN/ACK 还是 RST） |

## 5. 实战演练

**环境**：本地实验网络。Metasploitable2 `192.168.56.101`（开放 21/22/80/445…），DVWA `192.168.56.102:8080`，攻击机 Kali `192.168.56.10`。

### 场景 1：穿透禁 ICMP 的主机做存活探测

```bash
sudo hping3 -S -p 80 -c 3 192.168.56.101
```

预期输出片段：

```text
HPING 192.168.56.101 (eth1 192.168.56.101): S set, 40 headers + 0 data bytes
len=46 ip=192.168.56.101 ttl=64 DF id=0 sport=80 flags=SA seq=0 win=5840 rtt=1.4 ms
len=46 ip=192.168.56.101 ttl=64 DF id=0 sport=80 flags=SA seq=1 win=5840 rtt=0.9 ms
len=46 ip=192.168.56.101 ttl=64 DF id=0 sport=80 flags=SA seq=2 win=5840 rtt=0.8 ms

--- 192.168.56.101 hping statistic ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.8/1.0/1.4 ms
```

解读：
- `flags=SA` = SYN+ACK，端口 80 **开放**。
- `ttl=64` 是很强的 OS 线索（Linux 默认 64）。
- `win=5840` 也是指纹特征之一。
- 如果目标是 `flags=RA`（RST+ACK），说明端口**关闭但主机在线**——这同样证明了存活。
- 如果**完全没有回包**，说明被丢包（filtered），而不是主机不在。

### 场景 2：用 `-8` 扫描模式做端口扫描

```bash
sudo hping3 -S -8 20-30,80,443,3306 192.168.56.101
```

预期输出片段：

```text
Scanning 192.168.56.101 (192.168.56.101), port 20-30,80,443,3306
8 ports to scan, use -V to see all the replies
+----+-----------+---------+---+-----+-----+-----+
|port| serv name |  flags  |ttl| id  | win | len |
+----+-----------+---------+---+-----+-----+-----+
   21 ftp         .S..A...   64     0  5840    46
   22 ssh         .S..A...   64     0  5840    46
   23 telnet      .R..A...   64     0     0    46
   25 smtp        .S..A...   64     0  5840    46
   80 http        .S..A...   64     0  5840    46
  443 https       .R..A...   64     0     0    46
 3306 mysql       .S..A...   64     0  5840    46
All 8 ports scanned but not all are open and ports 20-30 are closed
```

解读：
- `flags` 列：`.S..A...` = SYN/ACK → **开放**；`.R..A...` = RST/ACK → **关闭**。
- `23 telnet` 和 `443 https` 回 RST 说明关闭，而 21/22/25/80/3306 开放。
- **注意**：这是"看起来像 nmap"的模式，但 hping 会额外给出 **IP ID、TTL、WIN** 等原始字段——这些对 OS 指纹很有价值。提示行也专门提醒了这一点。

### 场景 3：防火墙行为分析（丢包 vs 拒绝）

```bash
# 对比三种标志位打到同一个端口
echo "=== SYN ==="   && sudo hping3 -S -p 80 -c 2 192.168.56.101
echo "=== ACK ==="   && sudo hping3 -A -p 80 -c 2 192.168.56.101
echo "=== NULL ==="  && sudo hping3 -p 80 -c 2 192.168.56.101
```

预期输出解读：

| 发出的包 | 有回包 | 无回包 |
|---------|--------|--------|
| SYN | 端口开放（SYN/ACK）或关闭（RST/ACK） | **被丢包**（stateful 过滤） |
| ACK | 到达了目标（RST） | **被无状态规则丢弃**（很多防火墙只放行已建立连接） |
| NULL（无标志） | 端口关闭时多数 OS 回 RST（RFC 793） | 被过滤 |

判断口诀：**"SYN 无响应 = 有防火墙；SYN 有响应而 ACK 无响应 = 有状态检测"**。这就是 hping3 在防火墙规则审计上的价值。

### 场景 4：TCP 版 traceroute + 路径 MTU 发现

```bash
# 用 TCP 80 做 traceroute（穿透丢 ICMP 的网络）
sudo hping3 --traceroute -S -p 80 -t 1 192.168.56.101   # 先看第 1 跳

# 全路径
sudo hping3 --traceroute -S -p 80 8.8.8.8

# 只监控第 5 跳
sudo hping3 --traceroute --ttl 5 --tr-keep-ttl -S -p 80 8.8.8.8
```

预期输出片段：

```text
HPING 8.8.8.8 (eth1 8.8.8.8): S set, 40 headers + 0 data bytes
hop=1 IP=192.168.1.1 rtt=1.1 ms
hop=2 IP=10.0.0.1 rtt=5.2 ms
hop=3 IP=172.16.1.1 rtt=9.8 ms
...
```

路径 MTU 发现：

```bash
# 带 DF 位，逐步加大包，直到不再收到响应（说明超过路径 MTU）
for s in 1400 1450 1472 1473 1500; do
  echo "--- data size $s ---"
  sudo hping3 -S -p 80 -y -d $s -c 1 8.8.8.8 2>&1 | tail -2
done
```

解读：`-y`（DF）配合递增的 `-d`，能找出路径上最小的 MTU。这对诊断"大包发不出去、小包正常"这类诡异问题极其有用。

## 6. 输出解读

标准 TCP 输出格式：

```text
len=46 ip=192.168.1.1 flags=RA DF seq=0 ttl=255 id=0 win=0 rtt=0.4 ms
```

| 字段 | 含义 | 情报价值 |
|------|------|----------|
| `len` | 从数据链路层捕获的数据字节数（不含链路层头） | 异常值可能说明填充/隧道 |
| `ip` | 源 IP（回包方） | — |
| `flags` | TCP 标志：`R`=RESET `S`=SYN `A`=ACK `F`=FIN `P`=PUSH `U`=URGENT `X`=非标 0x40 `Y`=非标 0x80 | `SA`=开放，`RA`=关闭 |
| `DF` | IP 头设置了 Don't Fragment | OS/路径信息 |
| `seq` | 由源端口推算的序号（ICMP 用序列字段） | 定位是第几个请求 |
| `id` | IP ID | **老式 OS 指纹与隐蔽扫描的关键** |
| `win` | TCP 窗口大小 | OS 指纹（Linux 5840、Windows 8192/64240…） |
| `rtt` | 往返时间（毫秒） | 网络质量、判断是否同一设备 |

加 `-V` 时会额外打印：`tos`（TOS 字段）、`iplen`、`ack`（ACK 号）、`sum`（校验和）、`urp`（紧急指针）。

**判断要点**：

- **有回包 = 主机在线**，无论内容是 SA 还是 RA。这就是 hping3 比 ping 可靠的存活判断方式。
- **`--seqnum` 输出里第二列（增量）恒定 = 序列号可预测**：这是老式 TCP 序列号预测攻击（以及 IP ID 隐蔽扫描）的前提。现代系统通常已随机化。
- **`--tcpexitcode` 让脚本判断端口状态**：

```bash
if sudo hping3 -S -p 22 -c 1 --tcpexitcode 192.168.56.101 >/dev/null 2>&1; then
  echo "端口 22 开放"
else
  echo "端口 22 关闭或被过滤"
fi
```

## 7. 与其他工具配合

```bash
# 1) hping3 存活探测（穿透禁 ping）-> nmap 精扫
sudo hping3 -S -p 80 -c 1 --tcpexitcode 192.168.56.101 >/dev/null 2>&1 && echo alive
sudo nmap -sV -iL alive_hosts.txt --open -oA hping_then_nmap

# 2) hping3 --seqnum -> 判断序列号可预测性（分析用途）
sudo hping3 -Q --seqnum -p 139 -S -i u1 -c 20 192.168.56.101

# 3) hping3 文件传输（实验室演示"在受限网络里搬文件"）
#    接收端（192.168.56.102）：
sudo hping3 192.168.56.10 --listen signature --safe --icmp
#    发送端（192.168.56.10）：
sudo hping3 192.168.56.102 --icmp -d 100 --sign signature --safe --file /etc/hostname

# 4) hping3 -> Wireshark 抓包复盘
sudo hping3 -S -p 80 -c 3 192.168.56.101 &
sudo tcpdump -i eth1 -w hping.pcap host 192.168.56.101
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `[open_sockraw] socket(): Operation not permitted` | 需要 raw socket 权限 | `sudo` 运行 |
| 命令跑不完，一直刷屏 | **没加 `-c`**，默认无限发送 | 永远加上 `-c <n>`；Ctrl-C 中断 |
| `-a` 伪源 IP 后完全看不到回包 | 回包被发到伪地址了 | 这是预期行为；需要在能收到该地址流量的位置嗅探 |
| `--rand-dest` 报错或发错网卡 | 无法自动判断出口 | 必须加 `-I <iface>` |
| 全是不回包，但目标明明在线 | 防火墙丢弃该标志位/端口 | 换标志位组合（SYN→ACK→NULL）；换端口 |
| 输出里 `sport=` 和预期端口不一致 | 源端口是随机基准并递增 | 用 `-s` 固定基准源端口，配 `--keep` 更稳 |
| `--flood` 把实验网络打瘫 | 该模式全速发包 | 只在隔离的授权环境使用；随时 Ctrl-C |
| traceroute 只到第一跳就停 | 中间设备不回 ICMP time-exceeded | 换协议（UDP/TCP）重试；`--tr-stop` 会让它提前退出，注意区别 |
| `-8` 扫描很慢 | 双进程设计且未优化 + 默认间隔 | 配 `-i u1000` 提速；大规模扫描还是用 [nmap](nmap.md)/[masscan](masscan.md) |
| 交互式 Ctrl+Z 不生效 | 被 `--unbind` 解绑了 | 用 `-z` 重新绑定 |
| 虚拟机里收不到自己的包 | 桥接/Host-Only 网络配置不同 | 确认网卡与网络模式；用 `-I` 指定 |

## 9. 防御视角（蓝队）

- **hping3 的能力大致分两类**，防守策略也不同：
  - **无害探测**：存活探测、TCP traceroute、路径 MTU 发现。这些在流量上和正常 TCP 连接差别不大，**只能靠行为和频率识别**。
  - **攻击性用法**：`--flood`（DoS）、`--rand-source`（状态表耗尽）、`-a` 伪源 IP（欺骗）。这些有明显的流量特征。
- **检测特征**：
  - **TCP NULL / FIN / Xmas 扫描**：正常的 TCP 连接不会以"无标志位"或"仅 FIN"开头。Suricata/Snort 对这类非法标志组合有现成规则。
  - **端口 0**：hping3 默认发往端口 0，**真实业务流量永远不会访问端口 0**。这是极好的检测点。
  - **非常规 TTL / 固定间隔**：hping3 默认每 1 秒一个包，节奏机械。
  - **`--flood`**：单源极高 PPS，NetFlow/流量监控一眼可见。
  - **`--rand-source`**：同一时间海量不同源 IP 访问同一目标 → 状态表耗尽攻击的典型特征。
- **缓解**：
  - 边界设备丢弃**目标端口为 0** 的包（顺带也丢源端口 0）。
  - 对**非法 TCP 标志组合**（NULL/FIN-only/Xmas）直接丢弃并记录。
  - **SYN flood 防护**：SYN cookies、连接速率限制、`net.ipv4.tcp_syncookies=1`。
  - **反欺骗**：入口过滤（BCP38/uRPF）阻止伪造源 IP 到达目标网络——这能直接废掉 `-a` 和 `--rand-source` 的很多用法。
- **蓝队注意**：hping3 也是**很好的教学与自测工具**。用它对你自己的防火墙发各种标志位组合，然后检查规则是否按预期动作——这是验证防火墙策略最直接的办法。

## 10. 参考

- 项目主页：<http://www.hping.org/>
- HPING3-HOWTO（隐蔽扫描、文件传输等进阶用法）：<http://www.hping.org/hping3.html>
- Kali 工具页：<https://www.kali.org/tools/hping3/>
- man page：`man hping3`（含完整字段含义与输出格式说明）
- 用法核实：本教程参数取自 `hping3 3.a2.ds2` 的 man page

---

**相关教程**：[nmap](nmap.md) ｜ [masscan](masscan.md) ｜ [arp-scan](arp-scan.md) ｜ [netdiscover](netdiscover.md) ｜ [fping](../02-漏洞分析/fping.md)
