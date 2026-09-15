# masscan（互联网级高速端口扫描）

> **一句话**：用异步无状态发包的方式，在几分钟内扫完一个 B 段甚至整个互联网的指定端口。
> **分类**：信息搜集 ｜ **Kali 包**：`masscan` ｜ **官方文档**：<https://github.com/robertdavidgraham/masscan>

## 1. 它解决什么问题

nmap 很强，但它是**有状态**的：每发一个包都要在内存里记录"我在等这个包的回包"。扫 `/16` 网段的全端口意味着 65 536 × 65 536 ≈ 43 亿次探测，nmap 的内存和连接表会被撑爆。

masscan 换了个思路：**不记录状态**。它只负责"疯狂发包"，收到回包就打印一条结果。代价是它不能像 nmap 那样做精细的服务识别和脚本扫描。

| 工具 | 并发模型 | 速度量级 | 精度 |
|------|---------|---------|------|
| **masscan** | 无状态异步发包（类似 ZMap/scanrand） | 万~百万包/秒 | 只能判断端口开/关，`--banners` 可抓少量 banner |
| [nmap](nmap.md) | 有状态，动态调整重传与并行度 | 千包/秒量级 | 服务版本、OS、脚本结论 |
| [fping](../02-漏洞分析/fping.md) | ICMP 并行 | 主机存活级别 | 只判断存活 |

**典型分工**：masscan 出"活口清单" → nmap 做精扫。

## 2. 工作原理

```text
        masscan（单进程）                       目标（成千上万）
   ┌────────────────────────────────┐
   │ 1. 把「IP × 端口」展开成一个序列  │
   │    索引 0 .. N-1                │
   │ 2. 一个线程按序列疯狂发 SYN      │ ──────►  SYN 到 1.2.3.4:80
   │    （无需等待、无需记录状态）    │ ──────►  SYN 到 1.2.3.5:80
   │                                │ ──────►  SYN 到 1.2.3.6:80  ...
   │ 3. 另一个线程用 libpcap 抓回包   │ ◄──────  SYN/ACK（=开放）
   │    收到 SYN/ACK 就打印一行       │ ◄──────  RST（=关闭，默认不打印）
   └────────────────────────────────┘
                  │
                  └─► 结果写入 stdout / XML / JSON / 二进制
```

关键点：

1. **发送与接收分离**——发送线程只管往外喷包，接收线程用 `pcap` 旁路抓包，互不阻塞。
2. **顺序是"随机"的**——`--seed` 控制随机序列，这也是为什么它能用 `--shards 1/3` 把一次扫描拆到三台机器上。
3. **收到 RST 时，本机内核会先回一个 RST**，导致 masscan 自己的 `--banners` 抓不到 banner。解决办法是设 `--adapter-port` 并用 iptables 把该端口 DROP 掉（见第 8 节）。
4. **不丢包是不可能的**——无状态意味着没有重传确认机制，高速率下会漏掉一部分开放端口（`--retries` 会盲重发）。

## 3. 安装与快速上手

```bash
sudo apt install masscan
masscan --help | head -30
masscan --iflist          # 先看有哪些网卡
```

最小可用命令：

```bash
# 1) 扫单个 C 段最常用的 100 个端口
sudo masscan 192.168.56.0/24 -p80,443,22,21,445,3389 --rate 1000

# 2) 扫私有网段全端口，只输出开放结果
sudo masscan 192.168.56.0/24 -p1-65535 --rate 5000 --open-only

# 3) 结果写成 list 格式，方便后续处理
sudo masscan 192.168.56.0/24 -p1-65535 --rate 5000 -oL masscan_ports.txt
```

> ⚠️ masscan 的设计目标就是"全社会都能看见你在扫"。**未经书面授权扫描任何不属于你的 IP 段，可能违反法律，也会让你被 ISP 停号。** 练习只用 Host-Only 内网或 `scanme.nmap.org`（且务必 `--rate 100` 以下）。

## 4. 核心参数详解

### 目标与端口

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `192.168.0.1` | 单个 IP | — |
| `10.0.0.1-10.0.0.100` | 地址范围 | 精确控制范围 |
| `0.0.0.0/0` | CIDR；多个用空格或逗号分隔 | 大规模扫描前务必配 `--excludefile` |
| `--range <ip/range>` | 与位置参数等价 | 写在配置文件里更清晰 |
| `-p 80,20-25` | 端口列表 / 范围 | 最常用形式 |
| `-p U:161,U:1024-1100` | 指定 UDP 端口（前缀 `U:`） | SNMP/NTP 探测 |
| `--exclude 10.0.0.1/32` | 排除地址 | 保护网关等关键设备 |
| `--excludefile f.txt` | 从文件排除 | 大型扫描的"安全阀" |

### 速率与准确性

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `--rate 1000` | 每秒发包数（默认仅 100） | 内网 1000~5000 稳妥；不要一上来就百万 |
| `--retries 2` | 每个探测盲重发次数（间隔 1 秒） | 高速率下提高命中率，代价是更"吵" |
| `--wait 10` | 发完后等待收包秒数（默认 10） | 跨公网扫描可加大到 30 |
| `--ttl 255` | 发包 TTL（默认 255） | 一般不用改 |
| `--seed time` | 随机序列种子 | 需要可复现的扫描顺序时固定一个整数 |
| `--shards 1/3` | 把扫描切成 3 份，本机执行第 1 份 | 多机分布式扫描 |
| `--resume-index` / `--resume-count` | 手动分片 | 脚本调度大任务时用 |

### 网卡与源地址

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-e eth0` | 指定发送网卡 | 多网卡机器必加 |
| `--adapter-ip 192.168.1.101` | 指定源 IP（可给范围，长度须为 2 的幂） | 官方推荐的运行方式，避免内核 RST 干扰 |
| `--adapter-port 61234` | 指定源端口（范围长度须为 2 的幂） | 配合 iptables DROP 才能抓 banner |
| `--adapter-mac` / `--router-mac` | 手工指定 MAC | 特殊网络环境下用 |
| `--iflist` | 列出可用网卡后退出 | 排错第一步 |

### 抓取与输出

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `--banners` | 抓取有限协议的 banner（HTTP/HTML title 等） | 需要先处理内核 RST 问题 |
| `--http-user-agent <UA>` | 自定义 HTTP UA | 配合 `--banners` |
| `--open-only` | 只报告开放端口 | **强烈建议默认加上** |
| `-oL out.txt` | 简单列表格式 | 后续 `awk`/`grep` 最方便 |
| `-oX out.xml` | XML | 可导入 Metasploit |
| `-oJ out.json` | JSON | 程序化处理 |
| `-oB out.bin` | 二进制（体积小） | 用 `--readscan` 转成其他格式 |
| `-oG out.gnmap` | grepable | 兼容老脚本 |
| `--output-format` + `--output-filename` | 等价写法 | 配置文件中更好读 |
| `--readscan out.bin -oX out.xml` | 读取二进制结果并转换 | 结果复用 |
| `--packet-trace` | 打印收发摘要 | 只在低速率下调试点用，高速率会刷屏 |
| `--pcap out.pcap` | 保存收到的包 | 事后用 Wireshark 复盘 |

### 配置与续跑

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-c masscan.conf` | 读配置文件 | 复杂扫描落盘成文件更可靠 |
| `--echo` | 不执行，只把当前配置 dump 出来 | 生成配置模板 |
| `--resume paused.conf` | 从 Ctrl-C 保存的状态继续 | 长时间扫描必备 |
| `--offline` | 不真发包，只做基准测试 | 评估发包能力 |

## 5. 实战演练

**环境**：VirtualBox Host-Only 网络 `192.168.56.0/24`；攻击机 Kali（`192.168.56.10`）；靶机 Metasploitable2（`192.168.56.101`）；靶机 DVWA 容器（`192.168.56.102`）。全部为本地自建环境。

### 场景 1：C 段常见端口快速普查

```bash
sudo masscan 192.168.56.0/24 -p21,22,23,25,80,110,139,143,443,445,\
3306,3389,5900,8080 --rate 1000 --open-only -oL scan_common.txt
```

预期输出片段：

```text
#masscan
open tcp 22 192.168.56.101 1757952000
open tcp 80 192.168.56.101 1757952000
open tcp 445 192.168.56.101 1757952000
open tcp 3306 192.168.56.101 1757952000
open tcp 8080 192.168.56.102 1757952000
```

解读：每行格式是 `open tcp <端口> <IP> <时间戳>`。这一步只回答"哪些 IP 的哪些端口可能开着"，不做任何版本判断。

### 场景 2：全端口扫描 + 清单交给 nmap

```bash
# 第一步：masscan 全端口
sudo masscan 192.168.56.0/24 -p1-65535 --rate 5000 --open-only -oL scan_full.txt

# 第二步：提取唯一 IP
awk '{print $4}' scan_full.txt | sort -u > live_hosts.txt
wc -l live_hosts.txt

# 第三步：nmap 精扫（只扫 masscan 报出来的端口）
awk '{print $3}' scan_full.txt | sort -un | paste -sd, > ports.txt
sudo nmap -sV -sC -Pn -iL live_hosts.txt -p "$(cat ports.txt)" -oA fine_scan
```

解读：`-p1-65535` 对 /24 就是约 1677 万次探测，5000 包/秒下大约 1 小时；同一任务用 nmap 会慢得多。把 masscan 的端口列表回灌给 nmap，既快又准。

### 场景 3：抓取 HTTP banner（含内核 RST 干扰的完整处理）

```bash
# 1) 屏蔽内核对本机源端口的响应，避免 masscan 自己发的包被 RST 打断
sudo iptables -A INPUT -p tcp --dport 61234 -j DROP

# 2) 用同一个端口作为源端口做扫描，并开启 banner 抓取
sudo masscan 192.168.56.0/24 -p80,8080 --banners \
     --adapter-port 61234 --rate 500 --open-only

# 3) 记得清理规则
sudo iptables -D INPUT -p tcp --dport 61234 -j DROP
```

预期输出片段：

```text
Discovered open port 80/tcp on 192.168.56.101
Banner on port 80/tcp on 192.168.56.101: [http] HTTP/1.1 200 OK
Server: Apache/2.2.8 (Ubuntu)
[title] Metasploitable2 - Linux
```

解读：masscan 支持 banner 的协议很少（主要是 HTTP、部分 FTP/SMTP），能把 `Server` 头和 `<title>` 带出来已经足够做初步判断。

### 场景 4：配置持久化 + 断点续跑

```bash
# 生成配置模板
sudo masscan 192.168.56.0/24 -p1-65535 --rate 2000 --echo > my.conf
head -5 my.conf

# 断开后 Ctrl-C 会生成 paused.conf，用它续跑
sudo masscan --resume paused.conf
```

解读：`--echo` 会把等价配置打印出来，改一改就是可复用的任务文件；Ctrl-C 不是丢失进度，而是把状态存进 `paused.conf`。

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `open tcp 80 1.2.3.4 <ts>` | 该端口收到了 SYN/ACK | 记入清单，交给 nmap `-sV` |
| `open udp 161 ...` | UDP 有响应（少见） | 用 `snmpwalk` 或 nmap `-sU` 复核 |
| `Banner on port ...` | 抓到的协议 banner | 提取 `Server` / `title` 做指纹 |
| 端口没出现在结果里 | 关闭 **或** 被过滤 **或** 回包丢了 | 提高 `--rate` 降低丢包不现实，应降速 + `--retries` 复扫 |
| `rate:` 实时行 | 当前发包速率 | 与 `--rate` 对比，判断是否达到预期 |

masscan **不能**告诉你"端口是 closed 还是 filtered"，也不能给出服务版本。所有需要"确切结论"的场景都要回到 nmap。

## 7. 与其他工具配合

```bash
# masscan -> nmap
sudo masscan 10.0.0.0/24 -p1-65535 --rate 3000 -oL m.txt
awk '{print $4}' m.txt | sort -u > hosts.txt
sudo nmap -sV -sC -Pn -iL hosts.txt --open -oA fine

# masscan -> Metasploit（先转 XML）
sudo masscan 10.0.0.0/24 -p1-65535 --rate 3000 -oX m.xml --open-only
msfconsole -q -x 'db_import /tmp/m.xml; services'

# masscan -> 直接给后续爆破工具供目标
awk '/80|443|8080/{print "http://"$4":"$3}' m.txt > urls.txt
# 再交给 gobuster / ffuf / nikto
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `FAIL: failed to load pcap` / 权限错误 | 未用 root 或缺少 libpcap | `sudo` 运行；`sudo apt install libpcap0.8` |
| 扫本地网段时结果全丢、或巨大延迟（几十秒起步） | 从**本机扫描本机所在网段**时，内核会替你回 RST，且 ARP 解析拖慢 | 用 `--adapter-ip` 指定一个**未被使用**的 IP；或换一台机器扫描 |
| 扫公网时明显很慢、每个结果都延迟 10 秒 | Linux 在发第一个包前要先 ARP 解析网关 | 加 `--router-mac <网关MAC>`，跳过 ARP |
| `--banners` 抓不到内容 | 内核 RST 抢先中断连接 | iptables DROP 源端口 + `--adapter-port` 用同一端口 |
| 高速率下明明开放的端口没报出来 | 无状态扫描丢包 | 降 `--rate`，加 `--retries 2`，或扫两遍取并集 |
| 被目标网络封禁 / 收到 abuse 投诉 | 速率过高或扫描了未授权范围 | 事先书面授权；与对方 IT/ISP 沟通；把投诉方加入 `--excludefile` |
| `-p1-65535` 直接跑了 20 万次扫描 | 参数写成了 `-p1-65535` 但目标是 `/0` 之类 | 先 `--echo` 确认展开范围，再执行 |
| 结果文件被覆盖 | 默认覆盖同名文件 | 加 `--append-output` 或换文件名 |

## 9. 防御视角（蓝队）

- **检测特征**：masscan 的流量非常"不像人"——同一源 IP 在极短时间内对大量**不同端口/不同主机**发 SYN，且**从不完成三次握手**。Suricata 的 `threshold`/`detection_filter` 规则很容易抓到。
- **速率识别**：即使 masscan 用 `--rate 100` 伪装，也会呈现"固定间隔、均匀分布"的非自然节奏；而正常用户流量是突发+长连接的。
- **缓解**：
  - 默认拒绝入站，只放行必要端口。
  - 上网关/边界设备做 per-source SYN 速率限制（如 `iptables -m limit`、厂商设备的 DoS 防护）。
  - 对内网资产做**端口收敛**：不必要的端口不开，扫描结果自然"干净"。
  - 部署蜜罐端口：任何对蜜罐端口的连接都几乎可确定为扫描行为。
- **注意**：masscan 可以伪造源 IP（`--adapter-ip`），所以"按源 IP 封禁"可能误伤或被绕过；应结合 TTL、TCP 指纹等做综合判断。

## 10. 参考

- 官方仓库（含 README 与用例）：<https://github.com/robertdavidgraham/masscan>
- 原始论文与设计说明：<https://github.com/robertdavidgraham/masscan/blob/master/doc/design.md>
- man page：`man masscan`

---

**相关教程**：[nmap](nmap.md) ｜ [fping](../02-漏洞分析/fping.md) ｜ [netdiscover](netdiscover.md) ｜ [arp-scan](arp-scan.md)
