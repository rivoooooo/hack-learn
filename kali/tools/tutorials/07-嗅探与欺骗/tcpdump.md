# tcpdump（命令行抓包）

> **一句话**：在终端里抓取并打印网络流量，几乎无处不在、几乎无依赖，是服务器上抓包落盘的首选工具。
> **分类**：嗅探与欺骗 ｜ **Kali 包**：`tcpdump` ｜ **官方文档**：<https://www.tcpdump.org/>

## 1. 它解决什么问题

[tcpdump](../07-嗅探与欺骗/tcpdump.md) 和 Wireshark 的关系，用一句话概括：

> **tcpdump 负责「抓」，Wireshark 负责「看」。**

| 场景 | 为什么用 tcpdump |
| --- | --- |
| 服务器上没有图形界面 | tcpdump 是纯 CLI |
| 服务器上不能装大依赖 | tcpdump 几乎只依赖 `libpcap` |
| 需要长时间后台抓包 | tcpdump 有成熟的环形缓冲（`-C` + `-W`） |
| 需要把抓包做成流水线 | tcpdump 的 BPF 过滤在**内核里执行**，效率极高 |
| 只想快速看一眼流量 | 一行命令，结果直接打在屏幕上 |
| 需要做远程抓包 | `ssh server tcpdump -w - \| wireshark -k -i -` |

**它不擅长什么**：逐层协议解剖、流跟踪、图形化统计。这些交给 Wireshark。

**与 Wireshark 的定位对比**：

| | tcpdump | Wireshark / tshark |
| --- | --- | --- |
| 依赖 | 极小（libpcap + libssl） | 大（数千 dissector + GUI 库） |
| 部署成本 | 几乎所有 Linux 都有 | 需要安装 |
| 输出 | 一行摘要 / pcap 文件 | 完整协议树 |
| 过滤 | **只有 BPF（内核级）** | BPF + 显示过滤器 |
| 分析能力 | 弱 | ⭐ 极强 |
| 长期抓包 | ⭐ **环形缓冲很成熟** | dumpcap 也行 |

**正确的工作流**：**tcpdump 在服务器上抓 → 下载到本地用 Wireshark 分析**。

## 2. 工作原理

### 2.1 为什么 tcpdump 很快 —— BPF 在内核里执行

这是 tcpdump 最核心的机制：

```
[1] 用户态：你写一个过滤表达式   "tcp port 80 and host 10.0.0.1"
        ↓
[2] libpcap 把它编译成 BPF 字节码（一种虚拟机指令）
        ↓
[3] 把 BPF 程序 attach 到内核的 socket（AF_PACKET）
        ↓
[4] 内核收到每个包时，先跑 BPF 程序
        ← 不匹配的包在内核里就丢弃，不复制到用户态
        ↓
[5] 只有匹配的包才被复制到 tcpdump 的用户态缓冲区
        ↓
[6] tcpdump 打印或写文件
```

**为什么这个设计重要**：

| 好处 | 说明 |
| --- | --- |
| **CPU 开销低** | 不匹配的包在内核里就丢了，不消耗用户态 CPU |
| **内存占用低** | 用户态缓冲区里只有匹配的包 |
| **高流量下不会崩** | 这是 tcpdump 能在服务器上跑的根本原因 |

**对照**：如果不用 BPF，10 Gbps 链路上的所有包都要复制到用户态 → CPU 打满、内存爆掉。

**这也是为什么「BPF 过滤器」和「显示过滤器」的语法完全不同**——前者是编译成虚拟机指令的，后者是 Wireshark 自己的表达式引擎。

### 2.2 抓包数据流

```
[网卡] → [内核网络栈]
              ↓
        [PF_PACKET socket]
              ↓ ← 就在这里，BPF 过滤发生
        [BPF 程序]
              ↓
        [内核环形缓冲区]  ← ⭐ 这里会丢包！
              ↓
        [用户态缓冲区]
              ↓
        [tcpdump 输出]
```

**丢包发生在哪**：**内核环形缓冲区**。

| 参数 | 作用 |
| --- | --- |
| `-B <size>` | 设置内核缓冲区大小（**单位是 KiB**，libpcap 1.10+） |
| `-s <snaplen>` | 每包只抓前 N 字节（减少数据量） |
| `-p` | 不进混杂模式（只收自己的包，减少数据量） |
| **BPF 过滤器** | ⭐ 最有效的减量手段 |

**判断有没有丢包** —— tcpdump 退出时会打印：

```
1234 packets captured
1234 packets received by filter
0 packets dropped by kernel        ← ⭐ 这行是 0 才是正常的
```

**`dropped by kernel` 非 0 = 丢包了**。解决顺序：

```
1. 加 BPF 过滤器（最有效）
2. 减小 -s（只抓头部）
3. 调大 -B
4. 关掉 -p？不，是「加上 -p」（不进混杂模式，减少数据）
5. 换更快的存储/更小的输出
```

### 2.3 混杂模式（promiscuous mode）

| 模式 | 收到什么 |
| --- | --- |
| **非混杂（默认在交换网络下）** | 只收到：发给自己的单播 + 广播 + 组播 |
| **混杂模式** | 网卡接收**线路上经过的所有帧**（不按目的 MAC 过滤） |

**关键事实**：**在交换网络中，混杂模式也看不到别人之间的单播流量**——因为交换机根本不会把那些帧发到你的端口。

```
[HUB 网络]     混杂模式 = 能看到所有人的流量 ✅
[交换网络]     混杂模式 = 只能看到广播/组播 + 发给你的 ✅
              看别人之间的流量 ❌（需要端口镜像或 ARP 投毒）
[Wi-Fi 开放]   能看到同 BSSID 的所有帧
[Wi-Fi WPA2]   能看到所有帧，但数据帧加密
```

**如何关闭混杂模式**：`-p`。**什么时候用**：

- 你只想看自己的流量（减少数据量、减少混淆）；
- **你不想让网卡进入混杂模式**（某些监控系统会对此告警）。

### 2.4 时间戳精度

| 参数 | 精度 |
| --- | --- |
| 默认 | 微秒（microsecond） |
| `--micro` | 微秒 |
| `--nano` | **纳秒**（需要网卡/内核支持） |
| `--time-stamp-precision <precision>` | 显式指定 |

**什么时候需要纳秒**：高频交易分析、极精确的时序分析。**日常抓包微秒足够。**

**`-j <type>`** 指定时间戳类型（这取决于平台，Linux 上常见的是 `host`——由内核在收到包时打时间戳；`adapter`——由网卡硬件打时间戳，更精确）。

### 2.5 文件轮转（长时抓包的关键）

tcpdump 的文件轮转有两个参数配合：

| 参数 | 作用 |
| --- | --- |
| `-C <file_size>` | 每个文件超过 N **百万字节（MB）** 就切新文件 |
| `-W <filecount>` | 最多保留 N 个文件，**循环覆盖** |
| `-G <seconds>` | 每 N 秒切一个新文件（用于按时间切分） |
| `-z <command>` | 每个文件轮转后执行该命令（**注意：会以 root 执行，有安全风险**） |
| `-Z <user>` | 运行 tcpdump 的用户（决定文件属主） |

**经典的长时抓包命令**：

```bash
tcpdump -i eth0 -w /var/capture/ring.pcap -C 100 -W 20
```

**含义**：每个文件最大 100 MB，最多保留 20 个 = **最多占用 2 GB 磁盘**，写满后从第一个开始覆盖。

**⭐ 这解决了「抓包把磁盘写满导致生产事故」这个经典问题。**

**关于 `-z` 的安全警告**：

```
-z postrotate-command
```

**这个命令是 tcpdump 以什么权限执行？** —— 以 tcpdump 的权限（通常是 root，因为抓包需要特权）。所以：

> **不要用 `-z` 执行不受信任的命令。** 如果 tcpdump 以 root 运行，`-z` 里的命令也是 root 权限。这是一个真实的提权风险面。

如果需要轮转后处理，更安全的做法是：

```bash
# 让 tcpdump 以低权限用户写文件，然后由外部脚本处理
tcpdump -i eth0 -w /tmp/cap.pcap -C 100 -W 20 -Z nobody
# 外部脚本监控 /tmp/cap.pcap* 并处理
```

## 3. 安装与快速上手

```bash
sudo apt install tcpdump
tcpdump -h
```

**权限配置（最佳实践）**：

```bash
# 方式一：用 sudo（最直接）
sudo tcpdump -i eth0 -c 10

# 方式二：给二进制 capability（避免每次 sudo）
sudo setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump
getcap /usr/sbin/tcpdump
# /usr/sbin/tcpdump cap_net_admin,cap_net_raw=eip

# 方式三：加入组（部分发行版有）
```

**⚠️ 关于方式二**：给 `tcpdump` 加 `cap_net_raw` 意味着**任何用户都能抓包**。在多用户系统上这可能是安全问题。**个人 Kali 虚拟机里没问题；生产服务器上要谨慎。**

**最短工作流**：

```bash
# 1) 看有哪些接口
sudo tcpdump -D

# 2) 抓 10 个包
sudo tcpdump -i eth0 -c 10

# 3) 抓包落盘
sudo tcpdump -i eth0 -w /tmp/capture.pcap

# 4) 读回来分析
tcpdump -r /tmp/capture.pcap -c 20
wireshark /tmp/capture.pcap
```

## 4. 核心参数详解

### 4.1 输出格式控制

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-n` | **不解析主机名**（显示 IP） | ⭐ **强烈建议总是加**——DNS 反向解析会拖慢并产生额外流量 |
| `-nn` | 不解析主机名**也不解析端口名**（显示 80 而不是 http） | ⭐ 脚本化时用 |
| `-N` | 不打印主机名的域名部分 | 罕见 |
| `-f` | 不解析外网地址 | — |
| `-t` | **不打印时间戳** | 输出更紧凑 |
| `-tt` | 打印**未格式化的 Unix 时间戳** | 脚本处理时用 |
| `-ttt` | 打印**相对上一包的间隔** | ⭐ **看时序最有用的格式** |
| `-tttt` | 打印完整日期时间 | 日志化时用 |
| `-ttttt` | 相对第一包的时间 | — |
| `-q` | 简洁输出（少打协议信息） | — |
| `-v` | 详细输出（TTL、校验和、选项） | `-vv` / `-vvv` 更详细 |
| `-e` | **打印链路层头**（含 MAC 地址） | ⭐ 看 MAC 必须加 |
| `-x` | 打印包的**十六进制**（不含链路层头） | — |
| `-xx` | 打印包的十六进制**含链路层头** | — |
| `-X` | 打印十六进制 **+ ASCII**（不含链路层头） | ⭐ 看内容用 |
| `-XX` | 十六进制 + ASCII，**含链路层头** | — |
| `-A` | **只打印 ASCII**（不含链路层头） | ⭐ **看明文内容最方便** |
| `-l` | **行缓冲**（配合管道时必需） | ⭐ 管道给别的程序时必加 |
| `-E <algo:secret>` | 用 IPsec ESP 密钥解密 | 需要密钥 |
| `-M <secret>` | 用 TCP-MD5 密钥校验 | — |
| `-S` | 打印绝对序列号（而非相对） | 分析 TCP 时用 |
| `-u` | 打印未解码的 NFS 句柄 | — |
| `-#` / `--number` | 打印包编号 | — |
| `--print` | 即使 `-w` 也打印到屏幕 | — |

**`-A` 与 `-X` 的区别**：

| | `-A` | `-X` |
| --- | --- | --- |
| 输出 | 纯 ASCII | 十六进制 + ASCII |
| 适合 | **看 HTTP/FTP 明文** | 看二进制内容 |

**`-l` 为什么必需**：默认 tcpdump 会缓冲输出（提高效率）。**管道给 `grep`/`awk` 时，不 `-l` 就会「攒够一批才输出」**，看起来像卡住了。

```bash
# 正确：实时管道
sudo tcpdump -i eth0 -l -A | grep -i 'user-agent'

# 也可以这样（效果类似）
sudo tcpdump -i eth0 -U -A | grep -i 'user-agent'
```

（`-U` 是 `--immediate-mode`，让包一到就交给上层，进一步减少延迟。）

### 4.2 抓包控制

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-i <interface>` | 指定接口 | ⭐ `any` 表示所有接口 |
| `-D` | 列出所有接口 | 不确定名字时用 |
| `-c <count>` | 抓 N 个包后退出 | ⭐ 定量抓包 |
| `-s <snaplen>` | 每包截取前 N 字节 | `-s 96` 只看头部；`-s 0` 抓完整包 |
| `-B <size>` | 内核缓冲区大小（KiB） | ⭐ 高流量时调大防丢包 |
| `-p` / `--no-promiscuous-mode` | 不进混杂模式 | 只关心自己流量时用 |
| `--immediate-mode` / `-U` | 包一到就交给上层（不等待攒批） | 低延迟场景 |
| `-Q <in\|out\|inout>` | 只抓入向/出向/双向 | 排查单向问题时用 |
| `-y <datalinktype>` | 指定链路层类型 | 少见 |
| `-T <type>` | 强制按某种类型解析 | 较少用 |
| `-K` / `--dont-verify-checksums` | 不校验 IP/TCP/UDP 校验和 | 卸载校验和导致的误报时用 |
| `-L` | 列出接口支持的链路层类型 | — |
| `-I` | 进监听模式（无线） | — |
| `-J` | 列出支持的时间戳类型 | — |
| `-j <type>` | 指定时间戳类型 | `-J` 查看可用值 |
| `--time-stamp-precision <p>` | 时间戳精度 | — |
| `--micro` / `--nano` | 微秒 / 纳秒 | — |
| `-g` / `-h` / `-H` / `-d` / `-S` / `-O` | 平台相关/少见 | 见 `man tcpdump` |

**`-s 0` 的含义**：在 libpcap 1.0+ 里，`-s 0` 表示**抓完整包**（不截断）。这是默认行为，但显式写出来更清晰。

### 4.3 文件与轮转

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-w <file>` | **写入 pcap 文件**（不打印到屏幕） | ⭐ 主用途 |
| `-r <file>` | 从 pcap 文件读取 | ⭐ 离线分析 |
| `-C <size>` | 每个文件最大 N **MB**，超过就切 | 配 `-W` 做环形缓冲 |
| `-W <count>` | 保留 N 个文件后循环覆盖 | ⭐ 配 `-C` |
| `-G <seconds>` | 每 N 秒切一个新文件 | 按时间切分 |
| `-z <command>` | 每次轮转后执行命令 | ⚠️ **以 tcpdump 权限执行，注意安全** |
| `-Z <user>` | 指定运行用户（决定文件属主） | ⭐ 生产环境建议用 |
| `-F <file>` | **从文件读取过滤表达式** | 表达式很长时用 |
| `-V <file>` | 从文件读文件名列表（用于 `-r` 或 `-w` 的多文件） | 少见 |

**三条实用的命令**：

```bash
# ① 最长的安全抓包（限大小、环形覆盖）
sudo tcpdump -i eth0 -w /var/capture/ring.pcap -C 100 -W 20

# ② 按时间切分（每 1 小时一个文件）
sudo tcpdump -i eth0 -w /var/capture/hourly-%Y%m%d%H.pcap -G 3600

# ③ 限时抓包
sudo timeout 60 tcpdump -i eth0 -w /tmp/60s.pcap
```

**`-G` 的文件名格式**：`-w` 里的 `%Y%m%d%H` 等会被 `strftime` 替换——**这是 `-G` 的必需用法**。

### 4.4 其他

| 参数 | 作用 |
| --- | --- |
| `-Z <user>` | 以指定用户身份运行（丢特权） |
| `--version` | 版本 |
| `-h` / `--help` | 帮助 |

## 4.5 BPF 过滤表达式（**tcpdump 的精髓**）

**这是 tcpdump 最该掌握的部分。** 表达式由 **原语（primitive）** 和 **逻辑运算符** 组成。

### 逻辑运算符

| 运算符 | 写法 | 优先级 |
| --- | --- | --- |
| 与 | `and` 或 `&&` | 最高 |
| 或 | `or` 或 `\|\|` | 中 |
| 非 | `not` 或 `!` | 最高（单目） |

**用括号明确优先级**——`&&` 比 `\|\|` 优先级高，但**不要依赖记忆**：

```bash
# 想要：TCP 且（目标端口 80 或 443）
# ❌ 错误写法（等价于 (tcp && port 80) || port 443）
tcp && port 80 || port 443
# ✅ 正确
tcp && \( port 80 or port 443 \)
```

**⚠️ 括号必须转义**（因为 shell 也用括号）：

```bash
sudo tcpdump -i eth0 'tcp and (port 80 or port 443)'     # ✅ 单引号最省事
sudo tcpdump -i eth0 tcp and \( port 80 or port 443 \)   # ✅ 转义
```

### 主机相关

| 表达式 | 含义 |
| --- | --- |
| `host 192.168.1.1` | 源或目的是该主机 |
| `src host 192.168.1.1` | 源 |
| `dst host 192.168.1.1` | 目的 |
| `ether host aa:bb:cc:dd:ee:ff` | MAC 地址（**需配 `-e` 看 MAC**） |
| `ether src aa:bb:cc:dd:ee:ff` | 源 MAC |
| `ether dst aa:bb:cc:dd:ee:ff` | 目的 MAC |
| `net 192.168.1.0/24` | 网段（CIDR） |
| `net 192.168.1` | 等价于 `192.168.1.0/24`（也可 `192.168.1.0 mask 255.255.255.0`） |
| `src net 10.0.0.0/8` | 源网段 |
| `host foo.example.com` | 主机名（**会触发 DNS 解析**，建议用 IP） |

### 端口相关

| 表达式 | 含义 |
| --- | --- |
| `port 80` | 源或目的是 80 |
| `src port 1024` | 源端口 |
| `dst port 443` | 目的端口 |
| `portrange 1-1024` | 端口范围 |
| `port 80 or port 443 or port 8080` | 多个端口 |

**注意**：`port 53` 会同时匹配 TCP 和 UDP 的 53。要限定协议：

```bash
udp port 53        # 只用 UDP 的 DNS
tcp port 53        # DNS over TCP（大响应/区域传送）
```

### 协议相关

| 表达式 | 含义 |
| --- | --- |
| `tcp` / `udp` / `icmp` / `arp` | 协议 |
| `ip` / `ip6` | IP 版本 |
| `ether` | 以太网 |
| `icmp6` | ICMPv6 |
| `ip proto 47` | IP 协议号 47（GRE） |
| `ip6 proto 58` | ICMPv6 |
| `tcp port 80` | 组合 |
| `udp portrange 67-68` | DHCP |

**常见协议号**：

| 号 | 协议 |
| --- | --- |
| 1 | ICMP |
| 6 | TCP |
| 17 | UDP |
| 47 | GRE |
| 50 | ESP（IPsec） |
| 51 | AH（IPsec） |
| 58 | ICMPv6 |
| 89 | OSPF |

### 字节匹配（最强的功能）

语法：

```
proto [ offset : size ] op value
```

| 部分 | 含义 |
| --- | --- |
| `proto` | 协议（`ip`/`tcp`/`udp`/`icmp`/`ether`） |
| `offset` | 从该协议头开始的字节偏移 |
| `size` | 取几字节（默认 1） |
| `op` | `=`, `!=`, `<`, `>`, `<=`, `>=`, `&`, `|` |
| `value` | 值 |

**经典例子**：

| 表达式 | 含义 |
| --- | --- |
| `tcp[13] & 2 != 0` | **TCP SYN 标志置位**（三次握手的第一个包） |
| `tcp[13] & 2 = 2 and tcp[13] & 16 = 0` | **纯 SYN**（SYN 置位且 ACK 未置位） |
| `tcp[13] & 4 != 0` | RST 置位 |
| `tcp[13] & 1 != 0` | FIN 置位 |
| `tcp[13] = 24` | PSH+ACK（数据包） |
| `ip[8] < 10` | TTL < 10（可疑） |
| `ip[6:2] & 0x1fff != 0` | 分片包（非首片） |
| `icmp[0] = 8` | ICMP Echo Request（ping） |
| `icmp[0] = 0` | ICMP Echo Reply |
| `tcp[0:2] > 1024` | TCP 源端口 > 1024 |
| `udp[8:4] = 0x00000000` | UDP 载荷前 4 字节为 0 |

**TCP flags 位图（`tcp[13]`）**：

```
 bit:  7   6   5   4   3   2   1   0
      CWR ECE URG ACK PSH RST SYN FIN
mask: 128 64  32  16  8   4   2   1
```

| 想要的 | 表达式 |
| --- | --- |
| SYN | `tcp[13] & 2 != 0` |
| SYN+ACK | `tcp[13] & 18 = 18` |
| RST | `tcp[13] & 4 != 0` |
| FIN | `tcp[13] & 1 != 0` |
| PSH | `tcp[13] & 8 != 0` |

**⭐ `tcp[13] & 2 != 0` 是 tcpdump 里最常用的字节匹配**——用来只抓连接建立的包。

**8 位对齐警告**：`tcp[13]` 是对的（TCP 头从 0 算，flags 在第 13 字节）。但要注意：

> **涉及多字节取值的字节匹配，offset 必须是相应大小的整数倍**，否则 BPF 编译会失败。例如 `ip[12:4]`（4 字节）要求偏移 12（是 4 的倍数）✅，`ip[13:4]` ❌。

### 常用过滤表达式速查表

| 需求 | 表达式 |
| --- | --- |
| 只看 HTTP | `tcp port 80` |
| 只看 HTTPS | `tcp port 443` |
| 只看 DNS | `udp port 53` |
| 只看 DNS（含 DoT） | `port 53 or port 853` |
| 只看 DHCP | `udp portrange 67-68` |
| 只看 ARP | `arp` |
| 只看 ICMP | `icmp` |
| 排除 SSH 和本地噪声 | `not port 22 and not arp and not (host 224.0.0.0/4)` |
| 只看某主机的非 SSH 流量 | `host 192.168.1.10 and not port 22` |
| 只看 TCP SYN | `tcp[13] & 2 != 0` |
| 只看 RST（连接被拒） | `tcp[13] & 4 != 0` |
| 只看 HTTP GET/POST | `tcp port 80 and tcp[((tcp[12] & 0xf0) >> 2):4] = 0x47455420`（GET） |
| 只看某网段到某网段 | `net 10.0.0.0/24 and net 172.16.0.0/16` |
| 只看大包 | `greater 1000` |
| 只看小包 | `less 100` |
| 只看广播 | `ether broadcast` 或 `ip broadcast` |
| 只看组播 | `ether multicast` |
| 只看 VLAN | `vlan` |
| 只看分片 | `ip[6:2] & 0x1fff != 0` |
| 排除自己管理连接的噪声 | `not port 22 and not port 3389` |

**关于「只看 HTTP GET」那个表达式**：`((tcp[12] & 0xf0) >> 2)` 计算 TCP 头的实际长度（考虑 options），然后取载荷前 4 字节与 `"GET "` 比较。**这体现了 BPF 表达式的表达能力**——但**可读性很差，日常用「`tcp port 80` 然后交给 Wireshark」更实际**。

**验证表达式是否正确**：

```bash
# -d 打印编译后的 BPF 字节码，可以验证语法
sudo tcpdump -i eth0 -d 'tcp port 80 and host 10.0.0.1'
```

**这是排查「为什么过滤表达式没生效」的最好方法**——语法错误在这里会立刻暴露。

## 5. 实战演练

**环境声明**：以下所有抓包操作**只在你自己的设备、你自己的网络、或你已获得书面授权的环境中执行**。**在未授权的网络上抓包属于违法行为**（见文末法律章节）。

### 场景 1：第一次抓包

**步骤 1：确认接口**

```bash
sudo tcpdump -D
```

**预期输出**

```
1.eth0 [Up, Running, Connected]
2.any (Pseudo-device that captures on all interfaces) [Up, Running]
3.lo [Up, Running, Loopback]
4.wlan0 [Up, Running, Wireless]
5.nflog (Linux netfilter log (NFLOG) interface)
6.nfqueue (Linux netfilter queue (NFQUEUE) interface)
7.bluetooth0 (Bluetooth adapter number 0)
```

**`any` 的注意事项**：它抓所有接口，但链路层类型是 `Linux cooked`（`SLL`），**看不到以太网头**（MAC 地址）。需要看 MAC 时用具体接口。

**步骤 2：抓 10 个包**

```bash
sudo tcpdump -i eth0 -c 10 -nn
```

**预期输出**

```
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
14:30:01.123456 IP 192.168.1.10.54321 > 93.184.216.34.443: Flags [S], seq 123456789, win 64240, options [mss 1460,sackOK,TS val 12345 ecr 0,nop,wscale 7], length 0
14:30:01.138765 IP 93.184.216.34.443 > 192.168.1.10.54321: Flags [S.], seq 987654321, ack 123456790, win 65535, options [mss 1460,sackOK,TS val 98765 ecr 12345,nop,wscale 8], length 0
14:30:01.138890 IP 192.168.1.10.54321 > 93.184.216.34.443: Flags [.], ack 1, win 501, options [nop,nop,TS val 12346 ecr 98765], length 0
14:30:01.139012 IP 192.168.1.10.54321 > 93.184.216.34.443: Flags [P.], seq 1:518, ack 1, win 501, options [nop,nop,TS val 12347 ecr 98765], length 517
...
10 packets captured
10 packets received by filter
0 packets dropped by kernel          ← ⭐ 没有丢包
```

**逐字段解读**：

| 字段 | 含义 |
| --- | --- |
| `14:30:01.123456` | 时间戳（默认微秒精度） |
| `IP` | 网络层协议 |
| `192.168.1.10.54321` | 源 `IP.端口` |
| `>` | 方向 |
| `93.184.216.34.443` | 目的 `IP.端口` |
| `Flags [S]` | ⭐ **TCP 标志**：`S`=SYN，`S.`=SYN+ACK，`.`=ACK，`P.`=PSH+ACK，`F.`=FIN+ACK，`R`=RST |
| `seq 123456789` | 序列号 |
| `ack 1` | 确认号（相对值） |
| `win 64240` | 接收窗口 |
| `options [...]` | TCP 选项（MSS、SACK、时间戳、窗口缩放） |
| `length 0` | **TCP 载荷长度**（0 = 没有应用数据） |

**⭐ 你可以在前三个包里直接看出 TCP 三次握手**：

```
[S]    ← 客户端请求连接（SYN）
[S.]   ← 服务器同意（SYN+ACK）
[.]    ← 客户端确认（ACK）→ 连接建立
```

**底部的三行统计**：

| 行 | 含义 |
| --- | --- |
| `N packets captured` | tcpdump 自己处理的包数 |
| `N packets received by filter` | 被 BPF 过滤器放行的包数 |
| **`N packets dropped by kernel`** | ⭐ **内核缓冲区丢弃的包数——必须是 0** |

### 场景 2：BPF 过滤实战

**练习 1：只看 DNS**

```bash
sudo tcpdump -i eth0 -nn 'udp port 53' -c 10
```

**预期输出**

```
14:31:02.123456 IP 192.168.1.10.41234 > 192.168.1.1.53: 12345+ A? example.com. (29)
14:31:02.125678 IP 192.168.1.1.53 > 192.168.1.10.41234: 12345 1/0/0 A 93.184.216.34 (45)
```

**解读**：

| 部分 | 含义 |
| --- | --- |
| `12345+` | 查询 ID + `+`（期望递归） |
| `A?` | 查询类型 A，`?` 表示查询 |
| `example.com.` | 查询的域名 |
| `1/0/0` | 回答数/权威数/附加数 |
| `A 93.184.216.34` | A 记录与 IP |

**⭐ 这条命令就是「DNS 审计」的最小形态**——你能看到本机查询了哪些域名。

**练习 2：只看 HTTP 请求的明文内容**

```bash
sudo tcpdump -i eth0 -nn -A -s 0 'tcp port 80' -c 5
```

**`-A` 让内容以 ASCII 打印**，你会看到：

```
14:32:15.123456 IP 192.168.1.10.54322 > 93.184.216.34.80: Flags [P.], seq 1:120, ack 1, win 501, length 119
E..{@.@...
...
GET /index.html HTTP/1.1
Host: example.com
User-Agent: curl/7.88.1
Accept: */*

14:32:15.234567 IP 93.184.216.34.80 > 192.168.1.10.54322: Flags [P.], seq 1:500, ack 120, win 65535, length 499
E..o...
...
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256
...
```

**⭐ 这就是「明文 HTTP 一无所有」的直观展示**——请求行、Host、User-Agent 全都看得见。

**练习 3：只看 TCP SYN（连接建立）**

```bash
sudo tcpdump -i eth0 -nn 'tcp[13] & 2 != 0' -c 10
```

**输出**：

```
14:33:01.111111 IP 192.168.1.10.54400 > 93.184.216.34.443: Flags [S], seq 123, win 64240, length 0
14:33:01.222222 IP 192.168.1.10.54401 > 1.1.1.1.53: Flags [S], seq 456, win 64240, length 0
```

**⭐ 这是「连接审计」的形态**——你能看到这台机器**尝试连接**了哪些地址和端口，**不需要等连接成功**。

**练习 4：找连接被拒绝的情况**

```bash
sudo tcpdump -i eth0 -nn 'tcp[13] & 4 != 0' -c 10
```

**输出**：

```
14:34:01.111111 IP 192.168.1.1.80 > 192.168.1.10.54402: Flags [R.], seq 0, ack 1, win 0, length 0
```

**`Flags [R.]` = RST**：连接被重置。**发 RST 的一侧就是「拒绝方」**——可能是防火墙、服务没监听、或应用主动断开。

**练习 5：排除噪声，只看实质流量**

```bash
sudo tcpdump -i eth0 -nn -c 20 \
  'not arp and not port 22 and not udp port 53 and not icmp'
```

**⭐ 实际使用时「排除法」比「包含法」更常用**——因为广播、ARP、DNS、SSH（你自己的管理连接）都是噪声。

**练习 6：验证过滤表达式**

```bash
sudo tcpdump -i eth0 -d 'tcp port 80 and host 10.0.0.1'
```

**预期输出**（BPF 字节码）

```
(000) ldh      [12]
(001) jeq      #0x800           jt 2	jf 5
(002) ldb      [23]
(003) jeq      #0x6             jt 4	jf 5
(004) ldh      [20]
...
```

**⭐ 如果是语法错误，这里会直接报错**——这是排查过滤器问题的第一招。

### 场景 3：抓包落盘 + 事后分析（标准工作流）

**步骤 1：在「服务器」上抓包**

```bash
# 模拟服务器场景：抓 60 秒，限制文件大小
sudo timeout 60 tcpdump -i eth0 -w /tmp/server-capture.pcap \
  -s 0 -B 4096 -nn
```

| 参数 | 作用 |
| --- | --- |
| `timeout 60` | 60 秒后自动停止（避免忘记） |
| `-w` | 写文件 |
| `-s 0` | 抓完整包（不截断） |
| `-B 4096` | 4 MB 内核缓冲区（防丢包） |
| `-nn` | 不做名称解析（更快） |

**步骤 2：看文件信息**

```bash
capinfos -A /tmp/server-capture.pcap | head -12
```

**预期输出**

```
File type:           Wireshark/tcpdump/... - pcap
Number of packets:   12345
File size:           8.9 MB
Data size:           8.7 MB
Capture duration:    60.012345 seconds
First packet time:   2026-09-15 14:35:00.123456
Last packet time:    2026-09-15 14:36:00.135801
Data byte rate:      145 kBps
Data packet rate:    205.67 packets/sec
```

**⭐ 先看文件信息是分析任何 pcap 的第一步**——决定用什么方法分析。

**步骤 3：用 tcpdump 离线查看**

```bash
# 只看 HTTP 请求
tcpdump -r /tmp/server-capture.pcap -nn -A 'tcp port 80' | head -40

# 只看前 20 个包
tcpdump -r /tmp/server-capture.pcap -nn -c 20

# 用过滤表达式筛选（离线过滤同样高效）
tcpdump -r /tmp/server-capture.pcap -nn 'tcp[13] & 4 != 0'
```

**步骤 4：交给 Wireshark 深度分析**

```bash
wireshark /tmp/server-capture.pcap
# 或
tshark -r /tmp/server-capture.pcap -Y "http.request" -T fields -e http.host -e http.request.uri
```

**⭐ 这就是完整的工作流**：**tcpdump 采集 → 文件传输 → Wireshark 分析**。

### 场景 4：长时间后台抓包（生产环境的正确做法）

**需求**：在服务器上挂一个抓包任务，跑几天，但不能把磁盘写满。

```bash
# 创建目录（归 nobody 所有，降低风险）
sudo mkdir -p /var/capture
sudo chown nobody:nogroup /var/capture

# 启动环形缓冲抓包
sudo tcpdump -i eth0 \
  -w /var/capture/ring.pcap \
  -C 100 \
  -W 20 \
  -s 96 \
  -B 8192 \
  -Z nobody \
  -nn \
  -f 'not port 22 and not arp and not udp port 53'
```

| 参数 | 作用 | 为什么 |
| --- | --- | --- |
| `-C 100` | 每文件 100 MB | 便于传输和分析 |
| `-W 20` | 保留 20 个 | **最多 2 GB 磁盘** ⭐ |
| `-s 96` | 只抓前 96 字节 | **只保留头部**（IP+TCP 头约 54-74 字节）→ 数据量大幅减少 |
| `-B 8192` | 8 MB 内核缓冲 | 高流量下防丢包 |
| `-Z nobody` | 以 nobody 运行 | ⭐ **降权限**（防 tcpdump 漏洞被利用） |
| `-nn` | 不解析 | 提高性能 |
| `-f '...'` | 排除 SSH/ARP/DNS | **减少噪声和体积** |

**生成的文件的轮转规律**：

```
/var/capture/ring.pcap0    ← 最早的
/var/capture/ring.pcap1
...
/var/capture/ring.pcap19   ← 最新的（还没写满时是当前文件）
```

**从环形缓冲里取出数据**：

```bash
# 按时间顺序合并
mergecap -w /tmp/all.pcap /var/capture/ring.pcap*

# 或者只取某个时间窗
editcap -A "2026-09-15 14:00:00" -B "2026-09-15 14:30:00" /tmp/all.pcap /tmp/window.pcap
```

**⭐ 这套配置是「生产环境安全抓包」的标准形态**：

| 风险 | 缓解 |
| --- | --- |
| 磁盘写满 | `-C` + `-W` 限制总量 |
| 敏感数据落盘 | `-s 96` 只留头部（**不落应用层内容**） |
| 权限过大 | `-Z nobody` 降权 |
| 抓包任务被遗忘 | 加监控/用 systemd timer 限时 |

**⚠️ 关于 `-s 96` 的取舍**：

| | `-s 96` | `-s 0`（完整） |
| --- | --- | --- |
| 文件大小 | 小（约 1/10 或更少） | 大 |
| 能看到 | IP/TCP 头、TCP 标志、端口、窗口 | ⭐ **应用层内容** |
| 适合 | **长期流量统计、连接审计** | 协议分析、内容取证 |
| 不适合 | 看 HTTP 内容 | 长期运行（磁盘会爆） |

**推荐**：长期监控用 `-s 96`（或 `-s 128` 以包含常见选项），需要内容分析时再临时完整抓包。

### 场景 5：实时监控与管道（-l 的重要性）

**需求**：实时看哪些 IP 在通信。

```bash
# ❌ 这样会「卡住」（输出被缓冲）
sudo tcpdump -i eth0 -nn 'tcp' | grep -v '127.0.0.1'

# ✅ 加上 -l（行缓冲）
sudo tcpdump -i eth0 -nn -l 'tcp' | grep -v '127.0.0.1'
```

**`-l` 与 `-U` 的区别**：

| 参数 | 作用 |
| --- | --- |
| `-l` | **行缓冲**——每行就输出（对管道友好） |
| `-U` / `--immediate-mode` | 包一到就交给上层（不等待攒批）——**进一步降低延迟** |

**实践**：**管道时加 `-l`；需要最低延迟时再加 `-U`**。

**几个实用的实时管道**：

```bash
# ① 实时统计每个源 IP 的包数
sudo tcpdump -i eth0 -nn -l 'tcp' | \
  awk '{split($3,a,"."); ip=substr($3,1,length($3)-length(a[length(a)])-1); print ip}' | \
  sort | uniq -c | sort -rn | head

# ② 实时提取 DNS 查询的域名
sudo tcpdump -i eth0 -nn -l 'udp port 53' | \
  grep -oP 'A\? \K[^ ]+' | \
  while read d; do echo "$d"; done

# ③ 实时提取 HTTP Host
sudo tcpdump -i eth0 -nn -l -A 'tcp port 80' | \
  grep -oP 'Host: \K\S+'

# ④ 实时告警：出现 RST 就打印
sudo tcpdump -i eth0 -nn -l 'tcp[13] & 4 != 0' | \
  awk '{print strftime("%H:%M:%S"), $0}'
```

**⭐ 「tcpdump + 管道」是运维和安全监控里最常见的模式**——它把抓包变成了一个**流式数据源**。

### 场景 6：检测异常（安全分析）

**练习 1：找出所有向外部的新连接（SYN 包）**

```bash
sudo tcpdump -i eth0 -nn -l 'tcp[13] & 2 != 0 and not net 192.168.1.0/24'
```

**解读**：`tcp[13] & 2 != 0` 是 SYN，`not net 192.168.1.0/24` 排除内网。**输出就是「内网主机尝试连接的外部地址」**。

**练习 2：找出拒绝连接（可能有人在扫端口）**

```bash
sudo tcpdump -i eth0 -nn -l 'tcp[13] & 4 != 0' | \
  awk '{print $3, $5}'
```

**解读**：大量 RST 通常是端口扫描的副产品（扫到未开放的端口）。

**练习 3：找出 TTL 异常小的包（可能是路由异常）**

```bash
sudo tcpdump -i eth0 -nn -v 'ip[8] < 10'
```

**练习 4：找出分片包（可能的分片攻击/绕过）**

```bash
sudo tcpdump -i eth0 -nn 'ip[6:2] & 0x1fff != 0'
```

**练习 5：把统计做成一行**

```bash
sudo tcpdump -i eth0 -nn -c 1000 'tcp' -w /tmp/sample.pcap
tcpdump -r /tmp/sample.pcap -nn 'tcp[13] & 2 != 0' | wc -l
# ↑ 这一千个包里有几个是连接建立
```

**⭐ 这些「异常检测」的核心思路是**：**先用 tcpdump 把「我关心的包」筛出来，再用 awk/sort/uniq 做统计。** 复杂分析再交给 Wireshark。

## 6. 输出解读

### 标准输出行

```
14:30:01.123456 IP 192.168.1.10.54321 > 93.184.216.34.443: Flags [S], seq 123456789, win 64240, options [mss 1460,sackOK,TS val 12345 ecr 0,nop,wscale 7], length 0
```

| 部分 | 含义 |
| --- | --- |
| `14:30:01.123456` | 时间戳（默认微秒） |
| `IP` | 网络层（`IP`=IPv4，`IP6`=IPv6，`ARP`，`ICMP` 等） |
| `192.168.1.10.54321` | 源 IP.端口 |
| `>` | 方向（`>` 单向，`<` 也可出现） |
| `93.184.216.34.443` | 目的 IP.端口 |
| `Flags [S]` | TCP 标志 |
| `seq` / `ack` | 序列号 / 确认号 |
| `win` | 接收窗口 |
| `options [...]` | TCP 选项 |
| `length 0` | TCP 载荷长度 |

### TCP 标志速查

| 显示 | 含义 |
| --- | --- |
| `[S]` | SYN |
| `[S.]` | SYN + ACK |
| `[.]` | ACK（且没有其他标志） |
| `[P.]` | PSH + ACK（**通常带数据**） |
| `[F.]` | FIN + ACK（关闭） |
| `[R]` / `[R.]` | RST（重置） |
| `[FP.]` | FIN + PSH + ACK |
| `[U.]` | URG + ACK |

**⭐ 最重要的判读**：

| 你看到 | 说明 |
| --- | --- |
| `[S]` 后紧跟 `[S.]` 再紧跟 `[.]` | ✅ **三次握手成功** |
| 只有 `[S]` 没有 `[S.]` | ❌ 目的不可达/被防火墙丢弃（超时） |
| `[S]` 后紧跟 `[R.]` | ❌ 目的拒绝（端口未开放或有防火墙 REJECT） |
| 看到 `[R.]` 且 ack=1 | 连接被主动重置 |
| `[F.]` 序列 | 正常关闭 |

### TCP 选项字段

| 选项 | 含义 |
| --- | --- |
| `mss 1460` | 最大报文段长度 |
| `sackOK` / `sack 1 {...}` | 选择性确认 |
| `TS val 12345 ecr 0` | 时间戳（val=自己的，ecr=回显对方的） |
| `wscale 7` | 窗口缩放因子（实际窗口 = win << wscale） |
| `nop` | 填充（无操作） |

### 末尾统计行

```
10 packets captured
10 packets received by filter
0 packets dropped by kernel
```

| 行 | 含义 | 判读 |
| --- | --- | --- |
| `packets captured` | tcpdump 处理的 |
| `packets received by filter` | **BPF 放行的** | `captured` 与 `received` 不一致 = 有些包在用户态被丢 |
| **`packets dropped by kernel`** | ⭐ **内核缓冲区丢的** | **必须为 0**！非 0 说明要加 BPF 过滤器 / 调大 `-B` / 减小 `-s` |

**丢包了怎么办（按有效性排序）**：

```text
1. 收紧 BPF 过滤器（在内核里就丢弃 → 最有效）
2. 减小 -s（只抓头部）
3. 调大 -B（更大的内核缓冲）
4. 加上 -p（不进混杂模式 → 减少数据量）
5. 排除高频噪声（ARP、DNS、你自己的 SSH）
6. 换更快的磁盘 / 写到 tmpfs
```

### 判断成功 / 关键信号

| 目标 | 命令 | 成功信号 |
| --- | --- | --- |
| 确认连通性 | `tcpdump -nn 'host X' -c 5` | 看到双向的包 |
| 确认连接建立 | `tcpdump -nn 'tcp[13] & 2 != 0'` | 有 `[S]` 和 `[S.]` |
| 确认端口未开放 | `tcpdump -nn 'tcp[13] & 4 != 0'` | 有 `[R.]` |
| 没有丢包 | 看末尾统计 | `0 packets dropped by kernel` |
| 抓到内容 | `tcpdump -nn -A 'port 80'` | 看到 HTTP 明文 |

**下一步**：

| 发现 | 动作 |
| --- | --- |
| 丢包 | 按上面的顺序优化 |
| 有 RST | 确认是哪一侧发的，查防火墙/服务状态 |
| 只有单向流量 | 检查 `-Q`、接口选择、路由/非对称路由 |
| 需要深度分析 | `wireshark capture.pcap` |
| 需要统计 | `tshark -r capture.pcap -q -z conv,tcp`（见 [wireshark](wireshark.md)） |

## 7. 与其他工具配合

```text
┌──── 采集层 ─────────────────────────────────────┐
│ tcpdump（服务器上，轻量、无图形依赖）             │
│   -C/-W 环形缓冲（长时抓包不掉盘）               │
│   -s 96 只抓头（长期监控）                      │
│   -z 轮转后处理（注意权限）                      │
└─────────────────┬───────────────────────────────┘
                  │ scp / 共享存储 / ssh 管道
                  ↓
┌──── 预处理层 ───────────────────────────────────┐
│ capinfos（文件信息）                             │
│ editcap（切时间窗、去重、截断）                   │
│ mergecap（合并）                                │
└─────────────────┬───────────────────────────────┘
                  ↓
┌──── 分析层 ─────────────────────────────────────┐
│ wireshark（GUI 逐层解剖）                        │
│ tshark（脚本化、-T fields、-z 统计）             │
└─────────────────┬───────────────────────────────┘
                  ↓
┌──── 结论层 ─────────────────────────────────────┐
│ 报告 / 告警 / 后续调查                          │
└─────────────────────────────────────────────────┘
```

| 组合 | 说明 |
| --- | --- |
| **tcpdump → [Wireshark](wireshark.md)** | ⭐ **最经典**。服务器抓，本地看 |
| **tcpdump \| ssh → Wireshark** | ⭐ **实时远程分析**（见下） |
| **tcpdump → `awk`/`sort`/`uniq`** | 快速统计（不需要 Wireshark 时） |
| **tcpdump → [hashcat](../04-口令攻击/hashcat.md)** | 从流量里提取哈希（如 NTLM 挑战响应）→ 离线破解 |
| **tcpdump → [ettercap](ettercap.md) / [bettercap](../05-无线攻击/bettercap.md)** | 这些工具也会写 pcap，用 tcpdump 快速查看内容 |
| **tcpdump → [responder](responder.md)** | responder 抓的哈希可在 tcpdump/Wireshark 里验证 |
| **[macchanger](macchanger.md) → tcpdump** | 改 MAC 后用 `tcpdump -e` 验证流量里的 MAC 是否真的变了 |
| **[airodump-ng](../05-无线攻击/airodump-ng.md)** | 无线抓包（802.11）用 airodump-ng，有线用 tcpdump |

**⭐ 实时远程分析（很实用）**：

```bash
# 在本地 Kali 上运行：
ssh user@server 'sudo tcpdump -i eth0 -U -s 0 -w - not port 22' | wireshark -k -i -

# 解释：
#   -U            → 立即模式（低延迟）
#   -w -          → 写到 stdout
#   管道          → 通过 SSH 传到本地
#   wireshark -k  → 立即开始抓（从 stdin 读）
#   -i -          → 从 stdin 读
#   not port 22   → 排除 SSH（否则会抓到自己看自己）
```

**这是「服务器上抓包、本地看分析」的最佳实践**——不需要落盘，不需要传输文件。

**⚠️ 注意**：`not port 22` 很重要，否则 SSH 流量自己会形成回声，越抓越多。

**用 tcpdump 验证 macchanger**：

```bash
# 1) 改 MAC
sudo ip link set eth0 down
sudo macchanger -r eth0
sudo ip link set eth0 up

# 2) 用 tcpdump 看 MAC（必须加 -e）
sudo tcpdump -i eth0 -e -nn -c 5
```

**输出**：

```
14:40:01.123456 08:00:27:aa:bb:cc > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 42: ...
                 ↑ 新 MAC
```

## 8. 常见坑与排错

### 8.1 权限与接口

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `You don't have permission to capture on that device` | 无抓包权限 | `sudo`；或 `setcap cap_net_raw,cap_net_admin=eip $(which tcpdump)` |
| `tcpdump: eth0: No such device exists` | 接口名不对 | `tcpdump -D` 看接口列表 |
| `tcpdump: syntax error` | BPF 表达式语法错 | ⭐ 用 `tcpdump -d '表达式'` 验证；检查括号转义 |
| `tcpdump: no suitable device found` | 指定了不存在的接口 | 同上 |
| 在 `any` 接口上看不到 MAC | `any` 用 `Linux cooked` 链路类型，没有以太网头 | 用具体接口（`eth0`）并加 `-e` |

### 8.2 输出与管道

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| **管道给 grep 时「卡住」不输出** | 输出被缓冲 | ⭐ **加 `-l`**（或 `-U`） |
| 看不到主机名，只有 IP | 默认行为或加了 `-n` | 去掉 `-n`（**但注意 DNS 反解会拖慢**） |
| 看不到端口名 | 加了 `-nn` | 用 `-n` 而不是 `-nn` |
| 时间戳不好读 | 默认格式 | `-tttt`（完整日期）、`-ttt`（相对间隔） |
| 想看看内容但都是乱码 | 没有 `-A`/`-X` | 加 `-A`（ASCII）或 `-X`（hex+ASCII） |
| `-A` 看不到内容 | 流量是加密的（HTTPS） | 无法解密；用 [mitmproxy](mitmproxy.md) 或 Wireshark + 密钥 |
| 输出太长看不清 | 没过滤 | 加 BPF 过滤器 + `-c` |

### 8.3 丢包

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| **`packets dropped by kernel` 非 0** | 内核缓冲不够 / 处理跟不上 | ⭐ **加 BPF 过滤器**（最有效）→ 减小 `-s` → 调大 `-B` → 加 `-p` |
| 高流量下丢包严重 | 万兆/高 PPS 环境 | tcpdump 单进程可能不够；用 `dumpcap`（多线程更优）或专用采集卡 |
| 写到慢速磁盘导致丢包 | I/O 瓶颈 | 写到 tmpfs 或 SSD；减小 `-s` |

**一个诊断丢包的实际过程**：

```bash
# 1) 先不加过滤，看丢包
sudo tcpdump -i eth0 -c 10000 -w /dev/null
# 如果显示 N packets dropped → 有丢包

# 2) 加 BPF 过滤
sudo tcpdump -i eth0 -c 10000 'tcp and not port 22' -w /dev/null
# 再看丢包

# 3) 还丢 → 减小 snaplen
sudo tcpdump -i eth0 -c 10000 -s 96 'tcp and not port 22' -w /dev/null

# 4) 还丢 → 调大缓冲区
sudo tcpdump -i eth0 -B 32768 -c 10000 -s 96 'tcp and not port 22' -w /dev/null
```

### 8.4 抓不到想要的流量

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| 只看到自己的流量 | **交换网络**（正常行为） | 需要端口镜像（见下）；**不要用 ARP 投毒除非自有/授权网络** |
| 看不到本机的回环流量 | 抓的是物理接口 | 抓 `lo` 或 `any` |
| 看不到某个网段的流量 | 路由/接口选择 | 确认接口；`ip route` 看路由 |
| 只能看到一个方向 | 非对称路由 | `-Q inout`；或在两端都抓（比较） |
| 抓不到 VLAN 标记的包 | 网卡/驱动剥离了 VLAN 头 | 检查网卡 offload 设置：`sudo ethtool -K eth0 rxvlan off` |
| 校验和显示错误 | **网卡校验和卸载（offload）** | ⭐ **正常现象**——出方向的包校验和由网卡计算，tcpdump 在计算前就抓到了。加 `-K` 不校验 |

**⭐ 校验和错误是新手最常见的困惑**：

```
tcpdump: bad udp cksum 0x1234 -> 0x5678!
```

**原因**：**网卡校验和卸载**（checksum offload）。内核把「计算校验和」这件事交给网卡做，所以 tcpdump 在**校验和算出来之前**就抓到了包，看到的自然是不完整的校验和。

**这不是攻击，也不是丢包**——只是抓包位置的问题。用 `-K`（`--dont-verify-checksums`）关掉校验。

**交换网络下看到别人流量的合法方法**：

| 方法 | 说明 | 前提 |
| --- | --- | --- |
| **端口镜像（SPAN）** | 交换机把某端口流量复制给你 | ⭐ **企业标配**，需要交换机管理权限 |
| **网络分光器（TAP）** | 硬件串接 | 需要硬件 |
| **集线器** | 古老的 Hub 广播所有帧 | 已淘汰 |
| **虚拟机虚拟交换机** | VirtualBox/VMware 的混杂模式 | ⭐ **实验环境的最佳选择** |
| ARP 投毒 | 见 [ettercap](ettercap.md) / [bettercap](../05-无线攻击/bettercap.md) | ⚠️ **仅在自有/授权网络** |

**虚拟机里的配置**：

```
VirtualBox：设置 → 网络 → 高级 → 混杂模式 → 「允许全部」
VMware：网络适配器 → 桥接/仅主机 → 勾选混杂模式
```

**⭐ 很多人在虚拟机里抓不到包就是因为没开混杂模式。**

### 8.5 长时抓包相关

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| 磁盘被写满 | 没设大小限制 | ⭐ `-C` + `-W` 环形缓冲；`-s 96` 只抓头 |
| 文件太大无法分析 | 单文件 GB 级 | `-C 100` 切成小文件；或事后 `editcap -c 100000` |
| 抓包任务被遗忘在后台 | 无管理 | 用 systemd timer 限时；加监控告警 |
| `-z` 执行了危险命令 | ⚠️ **以 tcpdump 的权限（常是 root）执行** | ⭐ **不要用 `-z` 跑不受信任的命令**；用外部脚本处理 |
| 文件属主是 root | 默认行为 | `-Z nobody` 指定用户 |

## 9. 防御视角（蓝队）

tcpdump 是**防守方最基础的流量可见性工具**——几乎所有网络监控方案的最底层都是「抓包 → 分析」。

### 9.1 部署位置（决定你能看到什么）

| 位置 | 能看到 | 用途 |
| --- | --- | --- |
| **边界（出口）** | 内外网之间的所有流量 | ⭐ 检测数据外传、C2 通信 |
| **核心交换机（SPAN）** | 内网横向流量 | ⭐ 检测横向移动 |
| **关键服务器（本机）** | 该服务器的所有流量 | 检测针对该服务器的攻击 |
| **DMZ** | 面向公网的服务流量 | 检测外部攻击 |
| **终端（本机）** | 该终端的流量 | 端点取证 |

**⚠️ 关键限制**：tcpdump 只能看到**经过它所在位置**的流量。**在交换网络中，本机抓包只能看到本机流量**——想看到全网的流量必须有 **SPAN/TAP**。

### 9.2 检测清单（可直接落地的过滤表达式）

**① 检测明文凭据协议**

```bash
# 这些协议本身就不该在现代网络中出现
sudo tcpdump -i eth0 -nn -l -A \
  '(tcp port 23 or tcp port 21 or tcp port 110 or tcp port 143)'
```

| 端口 | 协议 | 风险 |
| --- | --- | --- |
| 23 | Telnet | ⚠️ **口令明文** |
| 21 | FTP | ⚠️ **口令明文** |
| 110 | POP3 | ⚠️ 口令明文 |
| 143 | IMAP | ⚠️ 口令明文 |
| 25/587 | SMTP | 内容明文 |
| 161/162 | SNMP v1/v2c | community string 明文 |
| 389 | LDAP | 凭据明文（应改用 636 LDAPS） |

**⭐ 看到这些端口的流量就是配置风险**——直接上报。

**② 检测数据外传**

```bash
# 找出向外部的大流量连接
sudo tcpdump -i eth0 -nn -l \
  'tcp[13] & 2 != 0 and not net 10.0.0.0/8 and not net 192.168.0.0/16 and not net 172.16.0.0/12'
```

**看什么**：

| 信号 | 含义 |
| --- | --- |
| 内网主机连接**陌生公网 IP** | 可能的 C2 |
| 固定间隔的小包 | ⚠️ **C2 心跳** |
| 大量出方向数据（用 `-Q out`） | 数据外传 |

```bash
# 只看出方向（数据外传方向）
sudo tcpdump -i eth0 -nn -l -Q out 'not net 10.0.0.0/8'
```

**③ 检测 DNS 隧道**

```bash
sudo tcpdump -i eth0 -nn -l -s 0 'udp port 53' -A | \
  grep -oP 'A\? \K[^ ]{40,}'
```

**`{40,}` 表示长度 ≥ 40 的域名** —— **超长域名是 DNS 隧道的典型特征**。

```bash
# 检测大量 TXT 查询（TXT 能承载更多数据）
sudo tcpdump -i eth0 -nn -l 'udp port 53' -A | grep -i 'TXT'
```

**④ 检测端口扫描**

```bash
# 统计每个源 IP 的 SYN 包数（短时间内大量 SYN = 扫描）
sudo tcpdump -i eth0 -nn -l -c 100000 'tcp[13] & 2 != 0' | \
  awk '{print $3}' | cut -d. -f1-4 | sort | uniq -c | sort -rn | head -20
```

**⑤ 检测横向移动（SMB/RDP/WinRM）**

```bash
# SMB
sudo tcpdump -i eth0 -nn -l 'tcp port 445'
# RDP
sudo tcpdump -i eth0 -nn -l 'tcp port 3389'
# WinRM
sudo tcpdump -i eth0 -nn -l 'tcp port 5985 or tcp port 5986'
```

**看什么**：**一台内网主机短时间内连接多台主机的这些端口** = 横向移动的强信号。

**⑥ 检测 ARP 投毒**

```bash
# 统计「声称自己是网关」的 MAC 数量（正常应为 1）
sudo tcpdump -i eth0 -nn -e -l 'arp.opcode == 2' -A | \
  grep -oP 'Request who-has \K\S+' 
```

**⭐ 更直接的检测方式**：

```bash
# 观察所有 ARP 响应里的 (IP, MAC) 对，找「同一 IP 对应多个 MAC」
sudo tcpdump -i eth0 -nn -e 'arp.opcode == 2' \
  | awk '{print $NF, $(NF-2)}' | sort -u
```

**输出**：

```
192.168.1.1 aa:bb:cc:dd:ee:ff     ← 正常的网关 MAC
192.168.1.1 08:00:27:aa:bb:cc     ← ⚠️ 第二个 MAC！ARP 投毒的铁证
```

**也可以用 `arpwatch` 这个专门的工具**：

```bash
sudo apt install arpwatch
sudo arpwatch -i eth0
# 它会在 ARP 表变化时自动记录并（可选）发邮件告警
```

### 9.3 一个可落地的「流量巡检」脚本

```bash
#!/usr/bin/env bash
# 说明：实时流量巡检。仅在你拥有/被授权监控的网络上运行。
set -euo pipefail
IFACE="${1:-eth0}"
SECS="${2:-60}"

PCAP="/tmp/tcpdump-audit-$$.pcap"
echo "[*] 采集 ${SECS} 秒流量于 $IFACE ..."
sudo timeout "$SECS" tcpdump -i "$IFACE" -nn -s 96 -B 4096 -w "$PCAP" 2>/dev/null || true

echo
echo "===== 1) 文件概况 ====="
capinfos -A "$PCAP" 2>/dev/null | grep -E 'Number of packets|Capture duration|Data byte rate'

echo
echo "===== 2) 丢包情况 ====="
sudo tcpdump -r "$PCAP" -nn -c 1 >/dev/null 2>&1 || true
echo "（若采集时有丢包，tcpdump 会打印 'packets dropped by kernel'）"

echo
echo "===== 3) 明文协议（应为 0）====="
for p in 23 21 110 143 389; do
  n=$(tcpdump -r "$PCAP" -nn "tcp port $p" 2>/dev/null | wc -l)
  printf "  port %-5s %s 个包\n" "$p" "$n"
done

echo
echo "===== 4) Top 10 目的地址 ====="
tcpdump -r "$PCAP" -nn 'tcp' 2>/dev/null | \
  awk '{print $5}' | sed 's/\.[0-9]*$//' | sort | uniq -c | sort -rn | head -10

echo
echo "===== 5) 外部新连接（SYN）====="
tcpdump -r "$PCAP" -nn 'tcp[13] & 2 != 0' 2>/dev/null | \
  awk '{print $5}' | sort -u | head -20

echo
echo "===== 6) 连接被拒（RST）计数 ====="
tcpdump -r "$PCAP" -nn 'tcp[13] & 4 != 0' 2>/dev/null | wc -l

echo
echo "[*] pcap 保存于 $PCAP（分析完请删除）"
```

**⭐ 把这个脚本挂到 cron 上**（例如每小时跑一次），就能得到一份**持续的流量基线**。

### 9.4 与 Wireshark 的防守分工

| 任务 | 用谁 | 原因 |
| --- | --- | --- |
| **持续采集** | ⭐ tcpdump | 轻量、低依赖、环形缓冲成熟 |
| **快速筛查** | ⭐ tcpdump + awk | 不需要 GUI，能在服务器上直接跑 |
| **深度分析** | ⭐ Wireshark | 协议树、Follow Stream、统计功能 |
| **批量字段提取** | tshark | `-T fields` 是脚本化的最佳接口 |
| **文件切片/合并** | editcap / mergecap | 处理 GB 级抓包 |

见 [wireshark](wireshark.md) 第 9 节有更多分析细节。

### 9.5 一个重要的提醒：抓包本身的合规性

**tcpdump 抓到的 pcap 里包含明文凭据、个人通信内容、业务数据。**

| 风险 | 缓解 |
| --- | --- |
| pcap 泄露 | 加密存储、严格访问控制、限期删除 |
| 含个人数据 | 按《个人信息保护法》要求处理（目的限制、最小必要） |
| **未授权抓包** | ⭐ **最根本的风险**——见文末法律章节 |
| 长期抓包无审批 | 建立**抓包审批流程**（谁、为什么、抓什么、保留多久） |

**企业环境中抓包的合规要点**：

```text
1. 有明确的书面授权（监控范围、目的、时间窗）
2. 有告知机制（员工手册 / 隐私政策中说明公司网络可能被监控）
3. 最小化原则（只抓必要的，-s 96 只抓头）
4. 数据分类与保留策略（抓包文件属敏感数据）
5. 访问审计（谁看过这些 pcap）
6. 限期删除
```

## 10. 参考

- 官方站点：<https://www.tcpdump.org/>
- 官方手册（含完整 BPF 语法）：<https://www.tcpdump.org/manpages/tcpdump.1.html>
- **pcap-filter 语法**：<https://www.tcpdump.org/manpages/pcap-filter.7.html>
- libpcap：<https://www.tcpdump.org/manpages/pcap.3pcap.html>
- Kali 工具页：<https://www.kali.org/tools/tcpdump/>
- 本机手册：`man tcpdump`、`man pcap-filter`（**BPF 语法的权威文档**）
- 本机帮助：`tcpdump -h`
- 验证过滤表达式：`sudo tcpdump -d '表达式'`（打印 BPF 字节码）
- 相关本目录：[wireshark](wireshark.md)（含 tshark）、[ettercap](ettercap.md)、[responder](responder.md)、[mitmproxy](mitmproxy.md)、[macchanger](macchanger.md)
- 相关其他目录：[hashcat](../04-口令攻击/hashcat.md)、[airodump-ng](../05-无线攻击/airodump-ng.md)、[kismet](../05-无线攻击/kismet.md)、[bettercap](../05-无线攻击/bettercap.md)

## ⚠️ 法律与伦理

**抓包就是「截获通信」**。tcpdump 本身只是一个工具，但**对非授权的网络或设备抓包即构成违法**。

**核心原则**：

> **「我只是抓包看看，没有攻击」不是合法性依据。**
> **截获他人通信本身即违法**——不需要破解、不需要利用、不需要造成损害。

**特别需要注意的误区**：

| 误区 | 事实 |
| --- | --- |
| 「交换网络抓不到别人的包，所以安全」 | 但可以用 **SPAN/ARP 投毒**做到——那就变成了主动行为 |
| 「我是运维，有权抓公司的包」 | ❌ 除非公司**书面授权**你做监控，否则同事的流量不是你能抓的 |
| 「我在自己的机器上抓，只抓自己的流量」 | ✅ **这个是可以的**——但要用 BPF 过滤器限定在自己的流量上 |
| 「Wi-Fi 是共享介质，收到不算偷」 | ❌ 无线电波可及 ≠ 有权接收 |
| 「只是学习，不用于任何目的」 | ❌ 在多数司法辖区，学习目的**不构成**抗辩 |

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条 | 非法侵入计算机信息系统；**非法获取计算机信息系统数据** |
| 《刑法》 | 第二百八十六条 | 破坏计算机信息系统 |
| 《刑法》 | 第二百五十三条之一 | **侵犯公民个人信息罪** |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《个人信息保护法》 | 相关条款 | 处理个人信息需有合法性基础（目的限制、最小必要、告知同意） |
| 《数据安全法》 | 相关条款 | 数据处理活动的合规要求 |
| 《治安管理处罚法》 | 相关条款 | 偷窥、偷拍、窃听他人隐私 |

**本教程仅适用于**：

- ✅ **你自己的设备与你自己的网络**（你自己的流量，抓多少都行）
- ✅ 你自己搭建的隔离实验环境（host-only 虚拟网络、隔离 VLAN）
- ✅ **你自己的组织内**，且你**被正式书面授权**做流量监控（安全团队职责）
- ✅ 有**书面授权**的渗透测试与合规审计（明确授权网段、时间窗、目的）
- ✅ 公开的示例 pcap 文件

**严禁**：

- ❌ 抓取任何非自有、非授权网络的流量
- ❌ 用 SPAN / ARP 投毒 / 混杂模式获取未授权的流量
- ❌ 对同事、家人、邻居、顾客的设备抓包
- ❌ 保留、分析、分享他人流量的 pcap
- ❌ 从抓包中提取他人凭据后用于任何目的（即使是「验证一下」）
- ❌ 把抓包数据上传到任何第三方平台

**推荐的学习路径（完全合法）**：

```text
✅ 抓你自己的流量
   tcpdump -i lo -w /tmp/mine.pcap
   → 能学到：BPF 语法、TCP 标志、丢包诊断、管道使用

✅ 抓你自己的实验网络（host-only 虚拟网络）
   → 能学到：完整的抓包与分析流程

✅ 分析公开的示例 pcap（Wireshark 官方示例）
   → 能学到：各种协议的实际形态

✅ 用 -s 96 只抓头部（长期监控时）
   → 既减少数据量，也减少敏感数据落盘
```

**这四条路径覆盖了 100% 的知识点，而且完全合法。**

**最后一句**：tcpdump 是**运维和防守方最基础的可见性工具**。请用它来**保护自己的网络**，而不是窥视别人的通信。
