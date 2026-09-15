# Wireshark / tshark（网络协议分析）

> **一句话**：把抓到的数据包逐层解码并可视化，是分析网络问题的显微镜；`tshark` 是它的命令行版本，用于脚本化与远程分析。
> **分类**：嗅探与欺骗 ｜ **Kali 包**：`wireshark`（GUI）、`tshark`（命令行）、`wireshark-common`（dumpcap/editcap/mergecap 等）｜ **官方文档**：<https://www.wireshark.org/>

## 1. 它解决什么问题

[tcpdump](../07-嗅探与欺骗/tcpdump.md) 能在终端里列出包，但它给你的是「一行摘要」。当你需要回答这些问题的时，就需要 Wireshark：

| 问题 | Wireshark 的能力 |
| --- | --- |
| 这个 TCP 连接为什么慢？ | 逐包看时间戳、序列号、重传、窗口变化；`Statistics → TCP Stream Graphs` |
| 这个 HTTP 请求的完整内容是什么？ | **Follow → TCP Stream**，直接看到解出来的明文 |
| TLS 握手为什么失败？ | 看 ClientHello/ServerHello/Alert 的每一个扩展字段 |
| 这个包里的某个字节是什么意思？ | 点开协议树，每一层字段都有名字和值 |
| 我要找含有某个字符串的包 | `Ctrl+F` 搜包内容 |
| 我要统计异常行为 | 显示过滤器 + 统计功能 + 导出 |

**两者的分工**：

| | tcpdump | Wireshark |
| --- | --- | --- |
| 界面 | 终端一行摘要 | GUI 协议树 |
| 部署 | 任何服务器（无图形界面也能跑） | 需要图形环境 |
| 用途 | **采集**：在服务器上快速抓包落盘 | **分析**：把 pcap 打开逐层解剖 |
| 过滤器 | BPF（捕获过滤，语法紧凑） | BPF（捕获）+ **显示过滤器（更强大）** |

**正确的工作流**：

```
[服务器无图形] tcpdump -w 抓包  →  scp 下载  →  [本地] Wireshark 打开分析
[本地有图形]  Wireshark / dumpcap 直接抓

[脚本化]      tshark 提取字段 → awk/jq 统计
```

**`tshark` 为什么重要**：它是 Wireshark 的命令行版，**拥有几乎相同的协议解析引擎和显示过滤器语法**。这意味着：

- 你学的显示过滤器语法在两边通用；
- 可以在服务器上、在自动化脚本里用同样的过滤逻辑；
- `airodump-ng` / `wifite` 等工具内部就用 `tshark` 做解析。

## 2. 工作原理

### 2.1 协议解析（dissection）—— Wireshark 的核心

Wireshark 内置**数千个协议解析器（dissector）**。处理一个包的过程：

```
[1] 读取 pcap 文件：拿到 帧字节 + 链路层类型（Ethernet? 802.11? Linux cooked?）
        ↓
[2] 按链路层类型选第一个 dissector（如 ethernet）
        ↓
[3] 解析出 Ethernet 头：src MAC, dst MAC, EtherType
        ↓
[4] 按 EtherType（0x0800 = IPv4）调用 ip dissector
        ↓
[5] 解析 IP 头：src/dst IP, protocol, TTL, flags, 分片信息
        ↓
[6] 按 protocol（6 = TCP）调用 tcp dissector
        ↓
[7] 解析 TCP 头：端口, 序列号, flags, 窗口 => 再按端口找应用层 dissector
        ↓
[8] 应用层：http / tls / dns / smb ...
        ↓
[9] 重组的应用层数据（HTTP body、TLS 明文）由上层 dissector 处理
```

**这解释了几件事**：

| 现象 | 原因 |
| --- | --- |
| 「显示为 TCP 但看不到内容」 | 应用层是加密的（TLS），或者用了非标准端口而没有 dissector |
| 「显示为 `[Malformed Packet]`」 | dissector 解析失败（可能是加密、可能是构造的畸形包、也可能是 dissector 的 bug） |
| 「显示为 `Data (1234 bytes)`」 | 没有匹配的应用层 dissector，只给了原始字节 |
| 端口不是标准的但内容能解析 | Wireshark 有**启发式 dissector**（如 HTTP 在非 80 端口也能识别） |
| 需要手工指定 | `Decode As...`（右键→ Decode As）或 `-d` 参数强制指定 dissector |

### 2.2 捕获过滤器 vs 显示过滤器

**这是 Wireshark 初学者最容易混淆的一点**。

| | 捕获过滤器（Capture Filter） | 显示过滤器（Display Filter） |
| --- | --- | --- |
| 什么时候生效 | **抓包时**（丢弃不匹配的包，不写入文件） | **显示时**（包已经在文件里，只是不显示） |
| 语法 | **BPF**（Berkeley Packet Filter），与 [tcpdump](../07-嗅探与欺骗/tcpdump.md) 相同 | Wireshark 自有语法 |
| 性能影响 | **减少磁盘与内存占用**（只存匹配的） | 不影响文件大小 |
| 能否改 | **不能**——没抓到的包永远丢了 | **随时改** |
| 写法示例 | `tcp port 80` | `tcp.port == 80` |
| 注意 | 语法错误会直接导致抓包失败 | 语法错误只是过滤器变红 |

**关键建议**：

> **不要用捕获过滤器过度限制。** 如果只是为了「在界面上看得清楚」，用**显示过滤器**。
> 捕获过滤器一旦丢包，**无法恢复**——很多调查都是因为「当初过滤太窄」而失败的。
> 只在两种情况下用捕获过滤器：① 高流量环境磁盘/内存吃不消；② 抓包时间极长。

**两者语法的对照**：

| 需求 | 捕获过滤器（BPF） | 显示过滤器 |
| --- | --- | --- |
| 主机 | `host 192.168.1.1` | `ip.addr == 192.168.1.1` |
| 源主机 | `src host 192.168.1.1` | `ip.src == 192.168.1.1` |
| 端口 | `port 80` | `tcp.port == 80` |
| 源端口 | `src port 443` | `tcp.srcport == 443` |
| 端口范围 | `portrange 1-1024` | `tcp.port >= 1 && tcp.port <= 1024` |
| 协议 | `tcp` / `udp` / `icmp` | `tcp` / `udp` / `icmp` |
| 网络 | `net 192.168.1.0/24` | `ip.addr == 192.168.1.0/24` |
| **排除** | `not port 22` | `!tcp.port == 22` |
| **逻辑** | `and` / `or` / `not` | `&&` / `\|\|` / `!` |
| 字节匹配（捕获） | `tcp[13] & 2 == 2`（SYN 包） | — |
| 字段匹配（显示） | — | `tcp.flags.syn == 1` |
| 字符串 | — | `http.request.uri contains "login"` |

**一个重要的实践**：**两者不能混用**。把 `tcp.port == 80` 填进捕获过滤器会报错——那是显示过滤器的语法。

### 2.3 流跟踪（Follow Stream）

Wireshark 能**把同一连接的所有包重组成连续的字节流**。这是分析应用层协议最有效的方法：

```
右键某个包 → Follow → TCP Stream / HTTP Stream / UDP Stream / TLS Stream
```

| 模式 | 效果 |
| --- | --- |
| **TCP Stream** | 双向的原始字节（客户端→服务器用一种颜色，反向另一种） |
| **HTTP Stream** | 只显示应用层 HTTP 数据（去掉 TCP 头） |
| **TLS Stream** | 如果有解密密钥，显示明文；否则显示加密数据 |
| **UDP Stream** | 类似 TCP 但基于 UDP |

**它做了什么**：根据 TCP 序列号**把乱序、重传、分段的包重组成原始字节流**。这是理解「TCP 是字节流协议」的最佳方式——**你在屏幕上看到的就是应用层实际收到的东西**。

### 2.4 解密能力

Wireshark 能解密多种加密流量（**前提是你有密钥**）：

| 协议 | 解密所需 | 配置路径 |
| --- | --- | --- |
| **WPA/WPA2** | PSK 或 PMK | `Preferences → Protocols → IEEE 802.11 → Decryption keys` |
| **WPA3** | ⚠️ 一般不支持 | — |
| **TLS / HTTPS** | 私钥（RSA）或 **SSLKEYLOGFILE** | `Preferences → Protocols → TLS → (Pre)-Master-Secret log filename` |
| **Kerberos** | keytab 文件 | `-K <keytab>` |
| **IPsec** | SA 信息 | `Preferences → Protocols → ESP` |
| **SNMPv3** | 认证/加密密钥 | `Preferences → Protocols → SNMP` |
| **802.11（WEP）** | WEP 密钥 | 同 WPA |

**SSLKEYLOGFILE 是现代最实用的 TLS 解密方式**：

```bash
# 启动浏览器前设置环境变量
export SSLKEYLOGFILE=/tmp/sslkeys.log
firefox     # 或 chromium

# 浏览器会把本次会话的 TLS 会话密钥写入该文件
# 在 Wireshark 里配置：
# Preferences → Protocols → TLS → (Pre)-Master-Secret log filename = /tmp/sslkeys.log
```

**它的原理**：TLS 1.3 用临时密钥（(EC)DHE），**服务器私钥无法解密**。但**客户端自己知道会话密钥**，所以让它把密钥导出到文件。**这只能解密你自己的客户端发起的流量**——这也说明了为什么 TLS 1.3 的前向保密（PFS）让被动监听变得无用。

### 2.5 硬件与权限

| 平台 | 抓包机制 |
| --- | --- |
| Linux | **libpcap**（默认）。`dumpcap` 需要 `CAP_NET_RAW` + `CAP_NET_ADMIN` |
| Windows | **Npcap**（需单独安装） |
| macOS | libpcap（需 BPF 权限） |

**Kali 上的权限配置**：

```bash
# 安装时会询问「非 root 用户能否抓包」——选 Yes
sudo dpkg-reconfigure wireshark-common

# 把用户加入 wireshark 组
sudo usermod -aG wireshark $USER
newgrp wireshark     # 或重新登录

# 验证
groups | grep wireshark
```

**为什么不用 root 跑 Wireshark**：Wireshark 有**数千个 dissector**，历史上出现过大量因畸形包导致的**解析器漏洞**。以 root 打开一个恶意构造的 pcap 意味着**把 root 权限交给攻击者**。

**正确的权限模型**：

```
wireshark（GUI，普通用户）
    ↓ 通过管道通信
dumpcap（需要 CAP_NET_RAW/CAP_NET_ADMIN，或 setuid）
    ↓
内核 nPcap/libpcap
```

**Wireshark 只负责解析，不直接抓包**——这限制了攻击面。

## 3. 安装与快速上手

```bash
# GUI
sudo apt install wireshark

# 命令行
sudo apt install tshark

# 通用工具（dumpcap/editcap/mergecap/capinfos/...）
sudo apt install wireshark-common
```

**权限配置（重要）**：

```bash
sudo dpkg-reconfigure wireshark-common    # 选 Yes，允许非 root 抓包
sudo usermod -aG wireshark $USER
newgrp wireshark
```

**快速上手（GUI）**：

```bash
# 1) 查看可用接口
sudo wireshark -D
# 或直接在 GUI 里看起始页的接口列表

# 2) 抓包
sudo wireshark -i eth0 -k        # -k 表示立即开始抓
# 或者打开 Wireshark → 双击接口

# 3) 打开已有文件
wireshark capture.pcap
```

**快速上手（tshark）**：

```bash
# 抓包
sudo tshark -i eth0 -f "tcp port 80" -c 20

# 从文件读并过滤
tshark -r capture.pcap -Y "http.request" -V | head -60

# 提取字段
tshark -r capture.pcap -Y "dns" -T fields -e ip.src -e dns.qry.name
```

## 4. 核心参数详解

### 4.1 捕获相关（GUI 与 tshark 通用）

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-i <interface>` | 指定接口（名字或编号） | ⭐ 最常用 |
| `-D` / `--list-interfaces` | 列出所有可用接口 | 不确定接口名时先跑这个 |
| `-f <capture filter>` | **BPF 捕获过滤器** | 谨慎使用（丢包不可恢复） |
| `-s <snaplen>` | 每包截取长度（默认 65535 / 全部） | 只关心头部时用 `-s 96` 大幅减小文件 |
| `-p` / `--no-promiscuous-mode` | 不进入混杂模式 | 只想看发给自己的包时 |
| `-I` / `--monitor-mode` | **监听模式**（无线网卡） | 802.11 抓包时用 |
| `-B <buffer size>` | 内核缓冲区大小（MiB） | **高流量环境调大防丢包** |
| `-y <link type>` | 链路层类型 | 少见 |
| `--time-stamp-type <type>` | 时间戳类型 | 高精度需求时 |
| `-L` / `--list-data-link-types` | 列出接口支持的链路类型 | 排查 802.11 抓包失败 |
| `--list-time-stamp-types` | 列出时间戳类型 | — |

### 4.2 捕获控制

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-k` | **立即开始抓包**（不弹对话框） | ⭐ 命令行启动 GUI 时用 |
| `-c <count>` | 收到 N 个包后停止 | ⭐ 定量抓包，避免忘记停 |
| `-a <condition>` | 自动停止条件 | ⭐ **强烈推荐**。`-a duration:60`（60 秒）、`-a filesize:10240`（10 MB）、`-a files:10`、`-a packets:10000` |
| `-b <condition>` | **环形缓冲**（ring buffer） | ⭐ **长期抓包的必备**：`-b filesize:10240 -b files:20` = 20 个 10MB 文件循环覆盖 |
| `-S` | 抓到新包时更新显示（GUI） | — |
| `-l` | 配合 `-S` 自动滚动 | — |
| `--update-interval <ms>` | 刷新间隔（毫秒） | 慢速终端调大 |

**`-b` 环形缓冲是长期抓包的正确姿势**：

```bash
# 循环保留 20 个 100MB 文件（最多 2GB 磁盘占用）
tshark -i eth0 -b filesize:102400 -b files:20 -w /var/capture/ring.pcapng
```

**它解决了「抓包把磁盘写满」这个经典事故**。

### 4.3 输入与处理

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-r <infile>` | 读取 pcap 文件 | ⭐ 分析时用；`-` 表示 stdin |
| `-R <read filter>` | 读取过滤器（需配 `-2`） | 罕见（用 `-Y` 更常见） |
| `-2` | **两遍分析**（two-pass） | 需要 `-R` 或需要完整重组（如 HTTP 对象导出）时用 |
| `-Y <display filter>` | **显示过滤器** | ⭐⭐ **最常用** |
| `-n` | 禁用所有名称解析 | ⭐ 抓包时提高性能；分析时反而想要解析 |
| `-N <flags>` | 名称解析开关（`m` MAC, `t` 传输层, `n` 网络, `d` DNS, `s` 端口, `N` 不解析, `v` VLAN, `g` 地理） | `-N mnt` 是保守的常用组合 |
| `-d <layer>==<selector>,<proto>` | **强制指定 dissector** | 非标准端口时用 |
| `--enable-protocol` / `--disable-protocol` / `--only-protocols` / `--disable-all-protocols` | 协议开关 | 提高性能或排除干扰 |
| `--enable-heuristic` / `--disable-heuristic` | 启发式解析开关 | — |
| `-H <hosts file>` | 指定 hosts 文件 | 名称解析 |

### 4.4 输出格式（tshark 的核心）

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-w <outfile>` | **写出 pcap 文件**（不打印到屏幕） | ⭐ 抓包落盘；`.gz` 自动 gzip |
| `-V` | **显示完整的协议树**（每个字段逐行） | ⭐ 需要看细节时用 |
| `-O <protocols>` | 只显示指定协议的详细树 | 输出更简洁 |
| `-P` / `--print` | 即使 `-w` 也打印摘要 | — |
| `-x` | **十六进制 + ASCII 转储** | 看原始字节 |
| `--hexdump <opt>` | hexdump 选项（`all`/`frames`/`ascii`/`delimit`/`noascii`/`time`/`notime`/`help`） | — |
| `-T <format>` | **输出格式**：`text`/`tabs`/`fields`/`json`/`jsonraw`/`pdml`/`psml`/`ps`/`ek` | ⭐ `fields` 与 `json` 最常用 |
| `-e <field>` | 输出指定字段（配 `-T fields`） | ⭐ 脚本化的关键 |
| `-E <opt>=<val>` | fields 选项：`header=`（表头）、`separator=`（分隔符）、`occurrence=`（同一字段多个值取第几个）、`aggregator=`（聚合符）、`quote=` | — |
| `-j <filter>` | 对协议树做过滤（只显示匹配的子树） | 罕见 |
| `-J <filter>` | 类似 `-j` 但影响输出 | 罕见 |
| `-S <separator>` | 摘要行分隔符 | — |
| `-q` | 安静模式（不打印包，只打印统计） | ⭐ 配合 `-z` |
| `-Q` | 更安静 | — |
| `-g` | 输出文件组可读权限 | — |
| `-W <n>` | 保存额外信息（如 `n` = 文件名注释） | — |
| `-t (a\|ad\|adoy\|d\|dd\|e\|r\|u\|ud\|udoy)` | 时间戳格式 | `-t ad` = 绝对日期时间；`-t r` = 相对首包 |
| `-u s\|hms` | 秒的显示格式 | — |
| `-l` | 每收到一个包就 flush（**配管道时必需**） | 实时处理时用 |
| `-F <filetype>` | 输出文件类型（默认 pcapng） | — |
| `--compress <type>` | 压缩输出 | — |

### 4.5 统计（`-z`）—— 非常实用

`-z` 的输出需要配合 `-q`（不看包详情）使用：

| `-z` 参数 | 作用 |
| --- | --- |
| `-z io,phs` | **协议层级统计**（各级协议的包数） |
| `-z io,stat,<interval>` | **流量统计**（按时间间隔的字节/包数） |
| `-z conv,tcp` | **TCP 会话列表**（每对 IP:端口 的包数/字节） |
| `-z conv,ip` / `-z conv,udp` / `-z conv,eth` | 其他会话统计 |
| `-z endpoints,ip` | IP 端点统计 |
| `-z http,tree` | HTTP 请求统计 |
| `-z http_req,tree` | HTTP 请求方法/URI 分布 |
| `-z dns,tree` | DNS 统计 |
| `-z expert` | **专家信息统计**（重传、乱序、异常等） |
| `-z follow,tcp,ascii,<stream#>`, | 跟踪某个 TCP 流（ASCII 显示） |
| `-z follow,tcp,hex,<stream#>`, | 跟踪 TCP 流（十六进制） |
| `-z io,stat,0,tcp.analysis.retransmission` | 重传统计 |
| `-z phs` | 同 `io,phs` |

**最常用的组合**：

```bash
tshark -r capture.pcap -q -z io,phs            # 协议分布
tshark -r capture.pcap -q -z conv,tcp          # 会话列表（找异常通信）
tshark -r capture.pcap -q -z expert            # 找问题（重传/乱序/异常）
```

### 4.6 其他实用参数

| 参数 | 作用 |
| --- | --- |
| `--export-objects <protocol>,<dir>` | **导出对象**（HTTP 文件、SMB 文件、TFTP、DICOM 等） |
| `--export-tls-session-keys <file>` | 导出 TLS 会话密钥 |
| `--color` | 彩色输出 |
| `-G [report]` | 输出各种报告（`protocols`、`fields`、`defaultprefs`、`currentprefs`） |
| `-o <name>:<value>` | 覆盖某个首选项 |
| `-K <keytab>` | Kerberos 解密用的 keytab |
| `--temp-dir <dir>` | 临时目录 |
| `-C <profile>` | 配置 profile |
| `-h` / `--help` | 帮助 |
| `-v` / `--version` | 版本 |

**`--export-objects` 极其有用**：

```bash
# 把 HTTP 传输的所有文件导出到 out/ 目录
tshark -r capture.pcap --export-objects http,./out/

ls -lh out/
```

**这是从 pcap 里「捞出文件」的标准方法**——附件、图片、下载的文件都在里面。

### 4.7 常用显示过滤器速查

**按协议**：

```
http                      # 只看 HTTP
tls 或 ssl                # 只看 TLS
dns                       # 只看 DNS
arp
icmp
smb 或 smb2               # SMB（Windows 文件共享）
ldap / kerberos
ftp / ftp-data
ssh / tcp.port == 22
telnet                    # 明文！能直接看到内容
```

**按地址/端口**：

```
ip.addr == 192.168.1.10
ip.src == 192.168.1.10 && ip.dst == 8.8.8.8
tcp.port == 443
tcp.port == 80 || tcp.port == 443
udp.port >= 1 && udp.port <= 1024
eth.addr == aa:bb:cc:dd:ee:ff
```

**TCP 标志位**：

```
tcp.flags.syn == 1 && tcp.flags.ack == 0     # SYN 包（连接发起）
tcp.flags.reset == 1                          # RST（连接重置）
tcp.flags.fin == 1                            # FIN
tcp.analysis.retransmission                   # ⭐ 重传（🔴 网络问题信号）
tcp.analysis.duplicate_ack                    # 重复 ACK
tcp.analysis.zero_window                     # 零窗口（接收方处理不过来）
```

**HTTP**：

```
http.request                                  # 请求
http.response                                 # 响应
http.request.method == "POST"
http.request.uri contains "login"
http.response.code >= 400
http.host contains "example"
http.user_agent contains "curl"
http.cookie contains "session"
http contains "password"                      # ⭐ 全文搜索
```

**DNS**：

```
dns.qry.name contains "example"
dns.flags.rcode != 0                          # 非 NOERROR（查询失败）
dns.qry.type == 1                             # A 记录
dns.qry.type == 16                            # TXT 记录（常用于数据外传！）
dns.qry.type == 255                           # ANY
```

**TLS**：

```
tls.handshake.type == 1                       # ClientHello
tls.handshake.type == 2                       # ServerHello
tls.handshake.type == 11                      # Certificate
tls.record.content_type == 23                 # Application Data（加密内容）
tls.handshake.extensions_server_name          # ⭐ SNI（明文域名，即使 TLS 1.3）
```

**⚠️ SNI 是个重要的隐私点**：TLS 的 SNI 扩展是**明文**的，所以即使流量加密，**你访问的域名依然可见**（除非用 ECH）。这是为什么「TLS 不等于隐私」的一个经典例子。

**802.11 / 无线**：

```
wlan.fc.type_subtype == 0x08                  # Beacon
wlan.fc.type_subtype == 0x0c                  # ⭐ Deauthentication
wlan.fc.type_subtype == 0x0a                  # Disassociation
wlan.fc.type_subtype == 0x04                  # Probe Request
wlan.fc.type_subtype == 0x00                  # Association Request
eapol                                         # WPA 握手
wlan.ssid contains "lab"
wlan.bssid == aa:bb:cc:dd:ee:ff
```

**字符串搜索**：

```
frame contains "password"
tcp contains "GET /"
udp contains "example"
frame matches "(?i)admin"                     # 正则（(?i) = 忽略大小写）
```

**比较与集合**：

```
ip.ttl < 10                                   # TTL 异常小
frame.len > 1400                              # 大包
tcp.len == 0                                  # 纯 ACK
!(arp || dns || icmp)                         # 排除噪声协议
ip.addr == 10.0.0.0/8                         # CIDR
tcp.port in {80, 443, 8080}                   # 集合
```

### 4.8 配套命令行工具

| 工具 | 作用 | 关键参数 |
| --- | --- | --- |
| **`dumpcap`** | **纯抓包**（Wireshark 的抓包引擎） | `-i`、`-f`、`-w`、`-b`、`-a`、`-c`、`-D`、`-s`、`-p`、`-I`、`-B` |
| **`editcap`** | 编辑/转换 pcap | `-r`（保留选定）、`-A`/`-B`（时间范围）、`-d`（去重）、`-s`（截断）、`-c`（每文件包数）、`-i`（每秒一文件）、`-F`（输出格式）、`-T`（封装类型） |
| **`mergecap`** | 合并多个 pcap | `-a`（串联而非合并）、`-w`、`-s`、`-F`、`-I`（IDB 合并模式） |
| **`capinfos`** | 打印 pcap 元信息 | `-c`（包数）、`-s`（大小）、`-u`（时长）、`-a`/`-e`（首末包时间）、`-y`（字节/秒）、`-H`（哈希）、`-A`（全部信息） |
| **`text2pcap`** | 从 ASCII hex dump 生成 pcap | `-o`（偏移格式）、`-l`（链路类型）、`-4`/`-6`（加 IP 头）、`-T`（加 TCP 头）、`-u`（加 UDP 头） |
| **`reordercap`** | 按时间戳重排 | `-n`（已有序则不写输出） |
| **`rawshark`** | 分析原始 pcap 数据 | `-r`、`-F`（字段）、`-Y`、`-S` |
| **`captype`** | 打印 pcap 文件类型 | — |
| **`tcpdump`** | 见 [tcpdump](../07-嗅探与欺骗/tcpdump.md) | — |

**`capinfos` 是分析任何 pcap 的第一步**：

```bash
capinfos -A capture.pcap
```

**输出**：文件类型、封装类型、包数、文件大小、总包长度、时间范围、时长、平均速率、包大小分布、SHA256 哈希。

**先跑 `capinfos` 能回答**：这个文件有多大？涵盖多长时间？流量速率如何？——**决定后续怎么分析**。

## 5. 实战演练

**环境声明**：以下所有抓包操作**只在你自己的网络、你自己的设备上执行**。**抓别人的流量是违法的**（见文末法律章节）。场景 2~5 全部基于**本地回环/自建靶机/已有抓包文件**，不涉及他人流量。

### 场景 1：确认环境与权限（第一步）

**步骤 1：检查接口**

```bash
sudo wireshark -D
# 或
tshark -D
```

**预期输出**

```
1. eth0
2. any
3. lo (Loopback)
4. wlan0
5. nflog
6. nfqueue
...
```

**`any` 接口**：抓所有接口的流量（Linux 特有）。注意它的链路层类型是 `Linux cooked`，某些解析会受限。

**步骤 2：检查权限配置**

```bash
groups | grep wireshark
# 如果为空，说明没加入组
```

**如果为空**：

```bash
sudo dpkg-reconfigure wireshark-common      # 选 Yes
sudo usermod -aG wireshark $USER
newgrp wireshark
```

**步骤 3：验证非 root 能抓包**

```bash
tshark -i lo -c 3
```

如果不报权限错误，说明配置成功。**这是最佳实践**——不要用 root 跑 Wireshark。

### 场景 2：抓第一次包（在自己机器上）

**用 GUI**：

```bash
sudo wireshark
# 或（加入 wireshark 组后）
wireshark
```

1. 起始页会列出接口，**每个接口后面有迷你流量图**；
2. 点接口名旁的蓝色鲨鱼鳍图标开始抓包；
3. 产生一些流量（例如在浏览器打开一个页面）；
4. 点红色方块停止。

**用 tshark（推荐用于精确控制）**：

```bash
# 抓 20 个包，不做名称解析（更快）
sudo tshark -i eth0 -c 20 -n
```

**预期输出**

```
    1 0.000000000 192.168.1.10 → 192.168.1.1  DNS 74 Standard query 0x1234 A example.com
    2 0.002134000  192.168.1.1 → 192.168.1.10 DNS 90 Standard query response 0x1234 A example.com A 93.184.216.34
    3 0.002456000 192.168.1.10 → 93.184.216.34 TCP 74 54321 → 443 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM
    4 0.015234000 93.184.216.34 → 192.168.1.10 TCP 74 443 → 54321 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460
    5 0.015345000 192.168.1.10 → 93.184.216.34 TCP 66 54321 → 443 [ACK] Seq=1 Ack=1 Win=131328 Len=0
    6 0.015678000 192.168.1.10 → 93.184.216.34 TLSv1.2 583 Client Hello
    ...
```

**逐列解读**：

| 列 | 含义 |
| --- | --- |
| 序号 | 包编号 |
| 时间 | 相对首包的时间（秒，微秒精度） |
| 源 IP | — |
| 目的 IP | — |
| 协议 | 最高层协议名（DNS/TCP/TLS/HTTP/…） |
| 长度 | 帧长度（字节） |
| 信息 | 协议摘要（**最有价值的一列**） |

**你能直接看出 TCP 三次握手**：

```
[SYN] → [SYN, ACK] → [ACK]      ← 三次握手完成，连接建立
[FIN, ACK] ... [ACK]            ← 四次挥手中
```

### 场景 3：显示过滤器实战（核心技能）

**⚠️ 重要区分**：
- `-f` = **捕获过滤器**（BPF 语法，抓包时生效，`tcp port 80`）
- `-Y` = **显示过滤器**（Wireshark 语法，显示时生效，`tcp.port == 80`）

**在 GUI 里**：顶部过滤器栏输入显示过滤器，回车。**语法错误时背景变红**。

**在 tshark 里**：

```bash
tshark -r capture.pcap -Y "tcp.port == 80"
```

**练习 1：找出所有 DNS 查询**

```bash
tshark -r capture.pcap -Y "dns.flags.response == 0" \
  -T fields -e frame.number -e ip.src -e dns.qry.name
```

**预期输出**

```
1	192.168.1.10	example.com
15	192.168.1.10	cdn.example.com
42	192.168.1.10	api.third-party.com
```

**⭐ 这就是「DNS 审计」的基本形态**——你能看到一台机器访问了哪些域名。

**练习 2：找出所有 TCP 重传（网络问题信号）**

```bash
tshark -r capture.pcap -Y "tcp.analysis.retransmission" \
  -T fields -e frame.number -e ip.src -e ip.dst -e tcp.port
```

**解读**：重传意味着「发出去的包没被确认」——常见原因：

| 原因 | 说明 |
| --- | --- |
| 链路拥塞 | 最常见的 |
| 丢包 | 物理层/无线信号问题 |
| 接收方缓冲区满 | 看 `tcp.analysis.zero_window` |
| 路径 MTU 问题 | 大包丢失、小包正常 |

**练习 3：找出所有 HTTP 请求的 URI**

```bash
tshark -r capture.pcap -Y "http.request" \
  -T fields -e ip.src -e http.request.method -e http.host -e http.request.uri
```

**练习 4：只看某一台主机的所有流量**

```bash
tshark -r capture.pcap -Y "ip.addr == 192.168.1.10" -c 50
```

**练习 5：排除噪声**

```bash
# 排除 ARP、DNS、ICMP，只看实质通信
tshark -r capture.pcap -Y "!(arp || dns || icmp)"
```

### 场景 4：Follow TCP Stream（理解应用层协议）

**这是 Wireshark 最有价值的功能之一。**

**步骤 1：先找到感兴趣的流**

```bash
tshark -r capture.pcap -q -z conv,tcp
```

**预期输出**

```
================================================================================
TCP Conversations
Filter:<No Filter>
                                               |       <-      | |       ->      | |     Total     |    Relative    |   Duration   |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |      Start     |              |
192.168.1.10:54321        <-> 93.184.216.34:443      42      5678      38      12345      80     18023     0.002456000        1.2345
192.168.1.10:54322        <-> 192.168.1.5:445        12      1200       9       900      21      2100     0.500000000        0.3000
```

**⭐ 这是「会话概览」**——一眼看出谁和谁通信、传了多少数据。**找异常通信（例如内网主机向外部 IP 传大量数据）就从这里开始。**

**步骤 2：在 GUI 里跟踪流**

1. 点击任何一个属于该连接的包；
2. 右键 → **Follow → TCP Stream**；
3. 弹出一个窗口，显示**完整的双向字节流**。

**你会看到**：

```
GET /login HTTP/1.1
Host: example.local
User-Agent: curl/7.88.1
Accept: */*

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...
```

**⭐ 这就是应用层实际交换的内容**——Wireshark 帮你做了 TCP 重组（处理乱序、重传、分段）。

**步骤 3：在 tshark 里做同样的事**

```bash
# 先用 conv,tcp 找到流编号，然后在 GUI 里看；或直接跟踪第 0 号流
tshark -r capture.pcap -q -z follow,tcp,ascii,0
```

**⚠️ 前提**：**流量必须未加密**。如果看到的是乱码，说明是 TLS。

### 场景 5：从 pcap 里捞文件（--export-objects）

**这是应急响应的常用操作**——从流量里还原出传输的文件。

```bash
mkdir -p /tmp/exported
tshark -r capture.pcap --export-objects http,/tmp/exported/
ls -lh /tmp/exported/
```

**预期输出**

```
-rw-r--r-- 1 user user  45K ...  index.html
-rw-r--r-- 1 user user 120K ...  logo.png
-rw-r--r-- 1 user user 2.3M ...  document.pdf
-rw-r--r-- 1 user user  890 ...  (empty)
```

**支持的协议**：`http`、`smb`、`smb2`、`tftp`、`imf`（邮件）、`dicom`、`ftp-data` 等。

**注意**：

- `(empty)` 通常是 304 未修改的响应（没有 body）；
- 文件名由 Wireshark 从 HTTP 头里提取；
- **只有未加密的流量能导出**（HTTPS 需要先解密）。

**这是应急响应中「找出嫌疑人下载了什么文件」的标准步骤。**

### 场景 6：解密 TLS（仅限自己的流量）

**这是完全合法的用法**——解密**你自己发起**的流量。

**步骤 1：设置 SSLKEYLOGFILE**

```bash
export SSLKEYLOGFILE=/tmp/sslkeys.log
rm -f /tmp/sslkeys.log

# 启动浏览器
firefox
# 或
chromium
```

**步骤 2：同时抓包**

```bash
sudo tshark -i lo -f "tcp port 443" -w /tmp/tls.pcap -a duration:30
# 或者抓所有接口
sudo tshark -i any -w /tmp/tls.pcap -a duration:30
```

**步骤 3：在浏览器里访问一个 HTTPS 站点**（触发 TLS 握手）

**步骤 4：确认密钥文件已生成**

```bash
ls -lh /tmp/sslkeys.log
head -2 /tmp/sslkeys.log
# CLIENT_RANDOM 1234abcd... 5678efgh...
```

**步骤 5：在 Wireshark 里配置解密**

1. `Edit → Preferences → Protocols → TLS`
2. `(Pre)-Master-Secret log filename` 填 `/tmp/sslkeys.log`
3. 确定

**步骤 6：重新打开 pcap，看到明文**

```
现在原本显示 "Application Data" 的包会变成 HTTP/2 请求和响应
Follow → HTTP/2 Stream 就能看到明文
```

**命令行等价**：

```bash
tshark -r /tmp/tls.pcap \
  -o tls.keylog_file:/tmp/sslkeys.log \
  -Y "http2" -c 10
```

**⭐ 这个练习的教学价值极大**：

| 学到的 | 说明 |
| --- | --- |
| **TLS 1.3 的前向保密** | 即使拿到服务器私钥也解不开——**只能靠客户端导出密钥** |
| **被动监听对 TLS 1.3 无效** | 这正是为什么现代网络安全依赖 TLS |
| **中间人攻击为什么需要证书信任** | 攻击者必须让客户端信任他的证书，否则 SSLKEYLOGFILE 这条路走不通 |
| **SNI 是明文的** | 即使不解密，你也能看到访问的域名（`tls.handshake.extensions_server_name`） |

**验证 SNI 明文可见**（不解密也能看）：

```bash
tshark -r /tmp/tls.pcap -Y "tls.handshake.type == 1" \
  -T fields -e ip.dst -e tls.handshake.extensions_server_name
```

**输出**：

```
93.184.216.34	example.com
142.250.72.14	www.google.com
```

**⭐ 这就是「TLS 不等于隐私」的最好例证**——域名是暴露的。ECH（Encrypted Client Hello）就是为了解决这个问题。

### 场景 7：tshark 脚本化分析（自动化）

**把 tshark 的输出接给 awk/jq 做统计**。

**统计每个 IP 的流量占比**：

```bash
tshark -r capture.pcap -T fields -e ip.src -e frame.len \
  | awk '{bytes[$1]+=$2} END {for (ip in bytes) print bytes[ip], ip}' \
  | sort -rn | head -10
```

**统计 DNS 查询的 Top 域名**：

```bash
tshark -r capture.pcap -Y "dns.flags.response == 0" \
  -T fields -e dns.qry.name \
  | sort | uniq -c | sort -rn | head -20
```

**统计 TCP 重传最多的主机**：

```bash
tshark -r capture.pcap -Y "tcp.analysis.retransmission" \
  -T fields -e ip.src | sort | uniq -c | sort -rn | head
```

**把结果输出为 JSON（接自动化）**：

```bash
tshark -r capture.pcap -Y "http.request" -T json \
  -e ip.src -e http.host -e http.request.uri | \
  python3 -c "
import json, sys
data = json.load(sys.stdin)
for pkt in data:
    layers = pkt['_source']['layers']
    print(layers.get('ip.src'), layers.get('http.host'), layers.get('http.request.uri'))
"
```

**⭐ 这是「用 tshark 做安全分析」的核心形态**：把「看包」变成「**可量化的统计**」。

**一个实用的「异常 DNS 检测」脚本**：

```bash
#!/usr/bin/env bash
# 说明：从 pcap 中找出可疑 DNS 行为。仅分析你自己抓取的流量。
set -euo pipefail
PCAP="$1"

echo "=== 超长域名（可能的 DNS 隧道/数据外传）==="
tshark -r "$PCAP" -Y "dns.flags.response == 0" \
  -T fields -e ip.src -e dns.qry.name \
  | awk 'length($2) > 50 {print}'

echo "=== TXT 记录查询（常用于数据外传）==="
tshark -r "$PCAP" -Y "dns.qry.type == 16" \
  -T fields -e ip.src -e dns.qry.name

echo "=== DNS 查询失败率高（可能的 DGA 域名）==="
tshark -r "$PCAP" -Y "dns.flags.rcode == 3" \
  -T fields -e ip.src -e dns.qry.name | head -20
```

### 场景 8：用 editcap / mergecap 处理抓包文件

**场景**：抓包文件太大，只想看某个时间段。

```bash
# 1) 先看文件信息
capinfos -A capture.pcap
```

**预期输出（节选）**

```
File type:           Wireshark/co... pcapng
Number of packets:   1,234,567
File size:           892 MB
Data size:           875 MB
Capture duration:    3600.123 seconds
First packet time:   2026-09-15 10:00:00.123456
Last packet time:    2026-09-15 11:00:00.246912
Data byte rate:      243 kBps
Data packet rate:    342 pps
SHA256:              ...
```

```bash
# 2) 只保留 10:30 到 10:35 的部分
editcap -A "2026-09-15 10:30:00" -B "2026-09-15 10:35:00" \
  capture.pcap attack-window.pcap

ls -lh attack-window.pcap
```

```bash
# 3) 只保留特定的包（第 100-200，以及第 500 号）
editcap -r capture.pcap selected.pcap 100-200 500
```

```bash
# 4) 去掉重复包
editcap -d capture.pcap dedup.pcap
```

```bash
# 5) 按包数切分成多个小文件
editcap -c 100000 capture.pcap split.pcap
ls split_*
```

```bash
# 6) 合并多个抓包文件
mergecap -w merged.pcap part1.pcap part2.pcap part3.pcap
# 按时间顺序合并（默认行为，会排序）
```

```bash
# 7) 转换格式（pcapng → pcap）
editcap -F pcap capture.pcapng capture.pcap
```

**这些工具在处理 GB 级抓包时非常必要**——Wireshark 打开超大文件会很卡，先用 editcap 切片再分析。

### 场景 9：分析无线抓包（与 05 目录衔接）

**如果你有 [airodump-ng](../05-无线攻击/airodump-ng.md) 抓的 pcap**：

```bash
# 1) 看文件信息
capinfos -A /tmp/cap-01.cap

# 2) 找出所有 AP
tshark -r /tmp/cap-01.cap -Y "wlan.fc.type_subtype == 0x08" \
  -T fields -e wlan.bssid -e wlan.ssid | sort -u

# 3) 找 WPA 握手（EAPOL）
tshark -r /tmp/cap-01.cap -Y "eapol" -V | head -80

# 4) ⭐ 检测 deauth 帧（WIDS 分析的核心）
tshark -r /tmp/cap-01.cap -Y "wlan.fc.type_subtype == 0x0c" \
  -T fields -e wlan.sa -e wlan.da -e wlan.fixed.reason_code \
  | sort | uniq -c | sort -rn | head -20
```

**第 4 条的输出直接告诉你**：

| 输出 | 含义 |
| --- | --- |
| 第 1 列计数很高 | 大量 deauth |
| `wlan.sa` 集中在一个 MAC | **这个 MAC 就是攻击者**（伪造的源地址） |
| `wlan.fixed.reason_code` 全是 7 | ⭐ **自动化工具的特征**（[aireplay-ng](../05-无线攻击/aireplay-ng.md) 默认 code 7） |

**⭐ 这就是「从抓包文件里找出无线攻击证据」的标准方法**——不需要任何注入，完全被动分析。

**解密密文（如果知道 PSK）**：

```
Preferences → Protocols → IEEE 802.11
  → Decryption keys → 添加 wpa-pwd（格式：password:SSID）
```

**或用 `airdecap-ng`（[aircrack-ng](../05-无线攻击/aircrack-ng.md) 套件）**：

```bash
airdecap-ng -p labpassword123 -e lab-test -b AA:BB:CC:DD:EE:FF /tmp/cap-01.cap
wireshark /tmp/cap-01-dec.cap
```

## 6. 输出解读

### tshark 默认摘要行

```
    6 0.015678000 192.168.1.10 → 93.184.216.34 TLSv1.2 583 Client Hello
    ↑      ↑          ↑              ↑           ↑     ↑      ↑
  包号   时间戳     源地址          目的地址     协议  长度   摘要
```

| 列 | 含义 | 关注点 |
| --- | --- | --- |
| 包号 | 帧编号 | 引用某包时用（如 `frame.number == 6`） |
| 时间戳 | 相对首包（默认）或绝对（`-t ad`） | 看时序、算延迟 |
| 源/目的 | IP 或 MAC | — |
| 协议 | 最高层 dissector 名 | 判断这是什么流量 |
| 长度 | 字节数 | 大包可能有问题 |
| 摘要 | 协议细节 | ⭐ **最有用的一列** |

### GUI 界面的三个窗格

| 窗格 | 内容 | 用途 |
| --- | --- | --- |
| **上层：包列表** | 所有包一行一条 | 概览、筛选、排序 |
| **中层：协议树** | 当前包的逐层展开（每层可展开到字段） | ⭐ **理解协议的入口**：点开任意字段，底部会高亮对应的字节 |
| **下层：字节视图** | 原始十六进制 + ASCII | 对照字段与原始字节 |

**⭐ 中层与下层的联动是 Wireshark 的学习神器**：点击协议树里的任意字段，下面的字节视图会**高亮对应的字节**。这让「协议格式」从抽象的图变成看得见的东西。

### 状态栏与颜色

| 元素 | 含义 |
| --- | --- |
| 底部左侧 `Packets: 1234 · Displayed: 56 (4.5%)` | 总包数 vs 显示（被过滤器筛掉的） |
| **黑色背景包** | ⚠️ **解析异常**（`[Malformed Packet]`） |
| **红色背景包** | 🔴 **错误**（校验和错误、连接重置等） |
| **深灰色行** | TCP 重传、乱序等分析标记 |
| **浅黄色行** | 常见的应用层协议（HTTP/NetBIOS/DCERPC） |
| **浅绿色行** | 其他 TCP 流量 |
| **浅蓝色行** | UDP 流量 |

**这些颜色是「默认配色规则」**，可在 `View → Coloring Rules` 里查看与修改。

### 判断成功 / 关键信号

| 你要找的 | 过滤器 | 说明 |
| --- | --- | --- |
| TCP 连接是否建立 | `tcp.flags.syn==1 && tcp.flags.ack==0` 后是否有 `flags.ack==1 && flags.syn==1` | 三次握手 |
| 连接是否被重置 | `tcp.flags.reset == 1` | 🔴 被 RST（防火墙？服务异常？） |
| 是否有丢包 | `tcp.analysis.retransmission` / `tcp.analysis.zero_window` | 网络问题 |
| HTTP 是否成功 | `http.response.code >= 400` | 4xx/5xx |
| DNS 是否异常 | `dns.flags.rcode != 0` | NXDOMAIN 等 |
| 是否有明文凭据 | `http contains "password"` / `ftp` / `telnet` | ⚠️ 安全问题 |
| TLS 是否正常 | `tls.alert_message` | TLS 告警 |
| 无线是否有 deauth 攻击 | `wlan.fc.type_subtype == 0x0c` | WIDS |

**下一步**：

| 发现 | 动作 |
| --- | --- |
| 重传率高 | 用 `Statistics → TCP Stream Graphs → Time Sequence` 看细节；排查链路/MTU |
| 有 RST | 看是哪个方向发的，判断是防火墙还是服务问题 |
| 明文凭据 | **立刻上报为安全问题**；检查为什么没用 HTTPS |
| 异常外部通信 | 提取 IP/域名，做威胁情报查询 |
| deauth 洪泛 | 见 [kismet](../05-无线攻击/kismet.md) 的 WIDS 章节 |

## 7. 与其他工具配合

```text
┌──── 采集层（在服务器上，无图形）────┐
│ tcpdump -w cap.pcap                 │
│ dumpcap -i eth0 -b filesize:100000 -b files:20 -w ring.pcapng │
└──────────────┬──────────────────────┘
               │ scp / 共享存储
               ↓
┌──── 预处理层 ────────────────────┐
│ capinfos（看文件信息）            │
│ editcap -A/-B（切时间窗）         │
│ editcap -d（去重）                │
│ mergecap（合并多个文件）           │
└──────────────┬───────────────────┘
               ↓
┌──── 分析层 ──────────────────────┐
│ wireshark（GUI 逐层解剖）         │
│ tshark -T fields（脚本化统计）     │
│ tshark --export-objects（捞文件）  │
│ tshark -z conv,tcp（会话概览）     │
└──────────────┬───────────────────┘
               ↓
┌──── 结论层 ──────────────────────┐
│ 报告 / 告警 / 后续调查             │
└──────────────────────────────────┘
```

| 组合 | 说明 |
| --- | --- |
| **[tcpdump](tcpdump.md) → Wireshark** | ⭐ **最经典的组合**。服务器上用 tcpdump 抓（轻量、无依赖），下载到本地用 Wireshark 分析 |
| **[dumpcap](wireshark.md) → Wireshark** | 同机时用 dumpcap（比 tcpdump 更懂 pcapng 和 Wireshark 生态） |
| **Wireshark → [hashcat](../04-口令攻击/hashcat.md)** | 从流量里提取哈希（如 NTLM 挑战响应）→ `hashcat -m 5600` 离线破解 |
| **[responder](responder.md) → Wireshark** | responder 抓到的哈希可以用 Wireshark 从 pcap 里验证（看 SMB/NTLMSSP 报文） |
| **[ettercap](ettercap.md) → Wireshark** | ettercap 抓的 pcap 用 Wireshark 深度分析（ettercap 自己的界面分析能力有限） |
| **[mitmproxy](mitmproxy.md) ↔ Wireshark** | mitmproxy 看 HTTP/HTTPS 的应用层；Wireshark 看 TCP/TLS 层。**互补** |
| **[airodump-ng](../05-无线攻击/airodump-ng.md) → Wireshark** | ⭐ 无线抓包用 Wireshark 分析 EAPOL 与 deauth |
| **[kismet](../05-无线攻击/kismet.md) → Wireshark** | `kismetdb_to_pcap` 导出特定时间窗 → Wireshark 深度分析 |
| **[bettercap](../05-无线攻击/bettercap.md) → Wireshark** | `net.sniff.output` 写的 pcap → Wireshark |
| **[macchanger](macchanger.md)** | 改 MAC 后抓包，验证流量中的 MAC 是否真的变了 |

**一条完整的取证链路**：

```bash
# 1) 服务器上抓包（环形缓冲，不会撑爆磁盘）
ssh server 'sudo dumpcap -i eth0 -b filesize:102400 -b files:20 -w /tmp/ring.pcapng -a duration:3600'

# 2) 下载
scp server:/tmp/ring_00001_*.pcapng ./ 2>/dev/null || scp server:/tmp/ring*.pcapng ./

# 3) 看文件信息，决定怎么切
capinfos -A ring*.pcapng

# 4) 切出可疑时间窗
mergecap -w merged.pcapng ring*.pcapng
editcap -A "2026-09-15 14:00:00" -B "2026-09-15 14:30:00" merged.pcapng window.pcapng

# 5) 会话概览，找异常
tshark -r window.pcapng -q -z conv,tcp | head -30

# 6) 捞出文件
mkdir -p out && tshark -r window.pcapng --export-objects http,./out/

# 7) 逐层分析
wireshark window.pcapng
```

## 8. 常见坑与排错

### 8.1 权限与接口

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `Permission denied` / 看不到任何接口 | 用户不在 `wireshark` 组 | `sudo dpkg-reconfigure wireshark-common` 选 Yes；`sudo usermod -aG wireshark $USER`；重登录 |
| `There are no interfaces on which a capture can be done` | 权限，或缺 `libpcap` | 检查 `groups`；`sudo apt install wireshark-common` |
| `dumpcap: command not found` | 未安装 `wireshark-common` | `sudo apt install wireshark-common` |
| 用 root 跑 GUI 出警告 | 故意设计 | **不要用 root**；修好组权限 |
| Windows 上抓不到包 | 缺 Npcap | 安装 Npcap（安装 Wireshark 时勾选） |

### 8.2 抓包相关

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| **抓包时大量丢包**（`Packets dropped: N`） | 内核缓冲区太小 / CPU 跟不上 | ⭐ 调大 `-B`（如 `-B 128`）；减小 `-s` 截断；用捕获过滤器缩小范围 |
| 磁盘被写满 | 没设限制 | ⭐ **用环形缓冲** `-b filesize:102400 -b files:20`；用 `-a duration:` 限时 |
| 过滤器报语法错但不知道哪错 | 混用了捕获/显示过滤器语法 | 见 2.2 节的对照表 |
| **捕获过滤器写错导致抓不到任何包** | BPF 语法错误时可能静默失败 | 先用 `tcpdump -d "表达式"` 验证（会打印编译后的 BPF 代码） |
| 只有单向流量 | 交换网络 + 未做端口镜像 | 见 8.4 节 |
| 抓不到本机生成的流量 | 抓的是物理接口 | 抓 `lo`（回环）或 `any` |

### 8.3 分析相关

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `[Malformed Packet]` | dissector 解析失败 | 尝试 `Decode As`（右键）；可能是加密或畸形包 |
| 端口非标准，内容显示为 `Data` | 没有匹配的 dissector | `Decode As` 手工指定，或 `-d tcp.port==8080,http` |
| 看不到 HTTP 内容 | TLS 加密 | 要么解密（场景 6），要么用 [mitmproxy](mitmproxy.md) |
| Follow Stream 看到乱码 | 加密流量 | 同上 |
| 大文件打开极慢 | Wireshark 要解析所有包 | ⭐ 先 `editcap` 切分；或抓包时就用捕获过滤器 |
| 显示过滤器写不出想要的效果 | 不知道字段名 | ⭐ **在 GUI 里点开协议树，看字段名**；或用 `tshark -G fields \| grep keyword` |
| 找不到某个协议的字段名 | — | `tshark -G fields \| grep -i dns`；或 `tshark -G protocols \| grep -i http` |
| TLS 解密不生效 | 密钥文件格式不对/路径错，或用了 TLS 1.3 且没抓 ClientHello | 确认 `SSLKEYLOGFILE` 在**浏览器启动前**设置；确认 pcap 里有 ClientHello |
| `--export-objects` 什么都没导出 | 流量加密，或不支持的协议 | 先解密；或检查协议拼写 |

**排错神器：查字段名**

```bash
# 找所有 DNS 相关字段
tshark -G fields | grep -i "dns\." | head -30

# 找所有协议
tshark -G protocols | grep -i http

# 查看某个显示过滤器的编译结果（验证语法）
tshark -r capture.pcap -Y "http.request" -c 1
```

### 8.4 抓不到别人流量的经典问题

**这是最常见的「Wireshark 不工作」原因**。

| 网络类型 | 你能看到 |
| --- | --- |
| **集线器（Hub）** | 所有人的流量（因为 Hub 广播所有帧） |
| **交换机（Switch）** | **只有你自己的流量 + 广播/组播** |
| Wi-Fi（开放/无加密） | 同 BSSID 的所有流量（无线是共享介质） |
| Wi-Fi（WPA2 加密） | 所有帧，但数据帧是加密的（需要密钥解密） |

**在交换网络中「看到别人流量」的合法方法**：

| 方法 | 说明 | 前提 |
| --- | --- | --- |
| **端口镜像（SPAN）** | 交换机把某个端口的流量复制到你的端口 | ⭐ **企业环境的标准做法**，需要交换机管理权限 |
| **网络分光器（TAP）** | 物理设备串接在链路中 | 需要采购硬件 |
| **ARP 投毒** | 见 [ettercap](ettercap.md) / [bettercap](../05-无线攻击/bettercap.md) | ⚠️ **只在你自己的网络上用** |

**⚠️ 强烈建议**：**在你自己的实验网络中，用端口镜像/虚拟交换机（如 VirtualBox 的 host-only + promiscuous 模式）**。ARP 投毒是「必要时的最后手段」，且**只在自有/授权网络上**才可以。

**虚拟机里的注意事项**：

```
VirtualBox：网络设置 → 高级 → 混杂模式 → 「允许全部」
VMware：网络适配器 → 仅主机模式 + 混杂模式
```

**很多人在虚拟机里抓不到包，就是因为混杂模式没开。**

## 9. 防御视角（蓝队）

Wireshark 是**双向工具**——攻击者用它分析窃取的流量，防守方用它做取证与检测。这一节讲**防守视角的用法**。

### 9.1 检测明文协议（最常见的配置风险）

```bash
# 找出所有明文凭据传输（这些协议本身就不该出现）
tshark -r capture.pcap -q -z io,phs | grep -E 'telnet|ftp|http|pop|imap|smtp|snmp'
```

**风险清单**：

| 协议 | 风险 | 应替换为 |
| --- | --- | --- |
| **Telnet** | 口令明文 | SSH |
| **FTP** | 口令明文 | SFTP / FTPS |
| **HTTP Basic** | 口令 base64（≈明文） | HTTPS |
| **POP3 / IMAP（非 TLS）** | 口令明文 | POP3S / IMAPS |
| **SMTP（非 TLS）** | 凭据 + 内容明文 | SMTPS / STARTTLS |
| **SNMP v1/v2c** | community string 明文 | SNMPv3 |
| **LDAP（非 TLS）** | 凭据明文 | LDAPS |
| **VNC（无加密）** | 会话可嗅探 | VNC over SSH/TLS |

**检测脚本**：

```bash
#!/usr/bin/env bash
# 说明：扫描 pcap 中的明文协议使用。仅分析你抓取的流量。
set -euo pipefail
PCAP="$1"

echo "=== 明文协议使用情况 ==="
for proto in telnet ftp-data ftp http pop imap smtp; do
  n=$(tshark -r "$PCAP" -Y "$proto" -T fields -e frame.number 2>/dev/null | wc -l)
  [ "$n" -gt 0 ] && echo "⚠️  $proto: $n 个包"
done

echo
echo "=== 疑似明文凭据 ==="
tshark -r "$PCAP" -Y 'http contains "password" || ftp contains "PASS" || telnet' \
  -T fields -e frame.number -e ip.src -e ip.dst 2>/dev/null | head -20
```

### 9.2 检测可疑外联与数据外传

```bash
# 1) 会话概览（找异常的大流量或非预期连接）
tshark -r capture.pcap -q -z conv,ip | head -40
```

**看什么**：

| 信号 | 含义 |
| --- | --- |
| 内网主机向**陌生公网 IP 传大量数据** | 可能的数据外传 |
| 固定间隔的小包（beacon） | ⚠️ **C2 心跳**的典型特征 |
| 大量连接失败（RST） | 端口扫描或 C2 探测 |

```bash
# 2) DNS 异常（C2 常用 DNS 隧道）
tshark -r capture.pcap -Y "dns.flags.response == 0" \
  -T fields -e ip.src -e dns.qry.name | \
  awk '{if (length($2) > 40) print "⚠️ 超长域名:", $0}'
```

**DNS 隧道特征**：

| 特征 | 说明 |
| --- | --- |
| 域名极长（> 40 字符） | 把数据编码进子域名 |
| 大量 TXT 查询 | TXT 记录能承载更多数据 |
| 同一父域的随机子域 | `<random>.attacker.com` |
| 高比例 NXDOMAIN | DGA（域名生成算法） |

```bash
# 3) TLS SNI 分析（不解密也能看访问了哪些域名）
tshark -r capture.pcap -Y "tls.handshake.type == 1" \
  -T fields -e ip.dst -e tls.handshake.extensions_server_name | sort -u
```

**⭐ 这是最实用的检测手段之一**——**即使全站 HTTPS，你也能看到访问的域名**（除非对端用 ECH）。

```bash
# 4) 固定间隔心跳检测（C2 特征）
tshark -r capture.pcap -Y "ip.dst == 203.0.113.5" \
  -T fields -e frame.time_relative -e frame.len
```

**如果时间间隔高度规律（如每 30.0 秒一次），且包很小 → 很可能是 C2 心跳。**

### 9.3 检测横向移动

```bash
# 1) SMB 流量（Windows 横向移动的主要途径）
tshark -r capture.pcap -q -z io,phs | grep -i smb

# 2) 找出 SMB 的连接与共享访问
tshark -r capture.pcap -Y "smb2.cmd == 3" \
  -T fields -e ip.src -e ip.dst -e smb2.filename | head -20

# 3) Kerberos 异常（Kerberoasting / AS-REP Roasting）
tshark -r capture.pcap -Y "kerberos.msg_type == 30" \
  -T fields -e ip.src -e ip.dst -e kerberos.SNameString
```

**横向移动的关键特征**：

| 特征 | 过滤器 | 含义 |
| --- | --- | --- |
| 一台主机短时间内连接**很多** 445 端口 | `tcp.port == 445` + 统计 | 可能的 SMB 扫描 |
| 大量 **Kerberos TGS 请求**（etype 23） | `kerberos.msg_type == 30` | ⭐ **Kerberoasting** |
| 大量 **AS-REP** | `kerberos.msg_type == 11` | AS-REP Roasting |
| **NTLM 认证到多个主机** | `ntlmssp` | 凭据传递 |
| RDP 连接（3389） | `tcp.port == 3389` | 远程桌面 |

**⭐ 这几条是「检测域内横向移动」的核心。**

### 9.4 检测 ARP 投毒（与 [ettercap](ettercap.md) / [bettercap](../05-无线攻击/bettercap.md) 对抗）

**ARP 投毒的流量特征**：

| 特征 | 过滤器/命令 | 说明 |
| --- | --- | --- |
| **同一 MAC 声明多个 IP** | `arp.opcode == 2` | 攻击者用同一 MAC 应答多个 IP |
| **网关 IP 的 MAC 突然改变** | `arp.src.proto_ipv4 == 192.168.1.1` | 看谁在声明自己是网关 |
| **ARP 响应频率异常高** | 统计 ARP 包速率 | 正常网络 ARP 很少；投毒会持续发送 |

**检测命令**：

```bash
# 找出所有声称自己是网关的 MAC（正常应该只有一个）
tshark -r capture.pcap -Y 'arp.opcode == 2 && arp.src.proto_ipv4 == 192.168.1.1' \
  -T fields -e eth.src | sort | uniq -c | sort -rn
```

**预期输出（正常）**

```
   42 aa:bb:cc:dd:ee:ff       ← 只有一个 MAC
```

**预期输出（被投毒）**

```
   38 aa:bb:cc:dd:ee:ff
   35 08:00:27:aa:bb:cc       ← ⚠️ 出现第二个 MAC！这就是攻击者
```

**⭐ 这个命令是检测 ARP 投毒最直接的方法**——**一个 IP 出现两个 MAC 就是铁证**。

```bash
# ARP 包的时间分布（投毒会持续、高频）
tshark -r capture.pcap -Y "arp" -T fields -e frame.time_relative | head -30
```

### 9.5 检测无线攻击（WIDS）

见 [kismet](../05-无线攻击/kismet.md) 第 9 节，以及本文件的场景 9。

```bash
# 从无线抓包里找 deauth 攻击
tshark -r capture.pcap -Y "wlan.fc.type_subtype == 0x0c" \
  -T fields -e wlan.sa -e wlan.da -e wlan.fixed.reason_code \
  | sort | uniq -c | sort -rn | head -20
```

**判读**：

| 信号 | 含义 |
| --- | --- |
| 计数很大 | 大量 deauth |
| `wlan.sa` 集中 | 攻击者的 MAC |
| `reason_code` 全是 7 | 自动化工具的特征 |

### 9.6 一份可落地的「流量巡检」清单

```bash
#!/usr/bin/env bash
# 说明：对抓包文件做基础安全巡检。仅分析你抓取的流量。
set -euo pipefail
PCAP="${1:?用法: $0 <pcap>}"

echo "========== 1) 文件信息 =========="
capinfos -A "$PCAP" | head -12

echo
echo "========== 2) 协议分布 =========="
tshark -r "$PCAP" -q -z io,phs 2>/dev/null | head -30

echo
echo "========== 3) 明文协议（应为 0）=========="
for p in telnet ftp http pop imap; do
  n=$(tshark -r "$PCAP" -Y "$p" -T fields -e frame.number 2>/dev/null | wc -l)
  printf "%-8s %s\n" "$p" "$n"
done

echo
echo "========== 4) 会话 Top 10 =========="
tshark -r "$PCAP" -q -z conv,ip 2>/dev/null | head -16

echo
echo "========== 5) TCP 重传统计 =========="
tshark -r "$PCAP" -Y "tcp.analysis.retransmission" \
  -T fields -e ip.src 2>/dev/null | sort | uniq -c | sort -rn | head -5

echo
echo "========== 6) DNS 异常 =========="
echo "-- 超长域名 (>40 字符) --"
tshark -r "$PCAP" -Y "dns.flags.response == 0" -T fields -e dns.qry.name 2>/dev/null \
  | awk 'length($0) > 40' | sort -u | head -10
echo "-- NXDOMAIN 计数 --"
tshark -r "$PCAP" -Y "dns.flags.rcode == 3" -T fields -e frame.number 2>/dev/null | wc -l

echo
echo "========== 7) TLS SNI 域名 =========="
tshark -r "$PCAP" -Y "tls.handshake.type == 1" \
  -T fields -e tls.handshake.extensions_server_name 2>/dev/null | sort -u | head -20

echo
echo "========== 8) ARP 网关 MAC 数（应为 1）=========="
tshark -r "$PCAP" -Y 'arp.opcode == 2' -T fields -e arp.src.proto_ipv4 -e eth.src 2>/dev/null \
  | awk '{print $1}' | sort | uniq -c | sort -rn | head -10
```

**把这个脚本挂到定期任务上，对关键位置的镜像流量做巡检**——这是最实用的「流量层安全监控」。

### 9.7 一个重要提醒

**Wireshark 抓到的 pcap 里常常包含明文凭据和敏感内容。**

| 风险 | 缓解 |
| --- | --- |
| pcap 被泄露 | 加密存储；严格的访问控制；限期删除 |
| pcap 里含个人数据 | 按《个人信息保护法》要求处理 |
| 未授权抓包 | ⭐ **这是最根本的风险——见文末法律章节** |
| 用 root 打开恶意 pcap | 用非特权用户；保持 Wireshark 更新（dissector 漏洞历史上很多） |

**最后一点尤其重要**：

> Wireshark 的 dissector 是一大堆 C 代码，历史上出现过**大量**解析漏洞。
> **不要用 root 打开来源不明的 pcap。** 也不要给 Wireshark 超过必要范围的权限。

## 10. 参考

- 官方站点：<https://www.wireshark.org/>
- 官方文档：<https://www.wireshark.org/docs/>
- **显示过滤器参考**：<https://www.wireshark.org/docs/dfref/>
- tshark 手册：<https://www.wireshark.org/docs/man-pages/tshark.html>
- dumpcap 手册：<https://www.wireshark.org/docs/man-pages/dumpcap.html>
- 示例抓包：<https://wiki.wireshark.org/SampleCaptures>
- Kali 工具页：<https://www.kali.org/tools/wireshark/>
- 本机手册：`man wireshark`、`man tshark`、`man dumpcap`、`man editcap`、`man mergecap`、`man capinfos`
- 本机帮助：`tshark -h`、`dumpcap -h`、`capinfos -h`
- 查字段名：`tshark -G fields | grep <关键字>`
- 查协议名：`tshark -G protocols | grep <关键字>`
- 相关本目录：[tcpdump](tcpdump.md)、[ettercap](ettercap.md)、[responder](responder.md)、[mitmproxy](mitmproxy.md)、[macchanger](macchanger.md)
- 相关其他目录：[hashcat](../04-口令攻击/hashcat.md)、[airodump-ng](../05-无线攻击/airodump-ng.md)、[kismet](../05-无线攻击/kismet.md)、[bettercap](../05-无线攻击/bettercap.md)

## ⚠️ 法律与伦理

**抓包（嗅探）是「截获通信」的行为**，在几乎所有司法辖区都受到严格规制。

**核心原则**：

> 「我只是抓包看看，没有攻击」**不是合法性依据**。
> **截获他人通信本身即违法**——不需要破解、不需要利用。

**特别提醒「交换网络」的误区**：

| 常见误解 | 事实 |
| --- | --- |
| 「交换网络抓不到别人的包，所以没关系」 | 但你可以用端口镜像/ARP 投毒**做到**，那就是**主动攻击** |
| 「Wi-Fi 是共享介质，能收到就算我的」 | ❌ **无线电波可及 ≠ 你有权接收** |
| 「我只是在自己家里抓」 | 你家的网卡也会收到邻居的帧——**物理位置不构成授权** |
| 「公司网络是我的工作环境」 | ❌ 除非有**书面授权**，否则同事的流量不是你能抓的 |

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条 | 非法侵入计算机信息系统；**非法获取计算机信息系统数据** |
| 《刑法》 | 第二百八十六条 | 破坏计算机信息系统 |
| 《刑法》 | 第二百五十三条之一 | **侵犯公民个人信息罪** |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《个人信息保护法》 | 相关条款 | 处理个人信息需有合法性基础 |
| 《数据安全法》 | 相关条款 | 数据处理活动的合规要求 |

**本教程仅适用于**：

- ✅ **你自己的设备与你自己的网络**（你自己的流量，你想怎么抓都行）
- ✅ 你自己搭建的隔离实验环境（host-only 虚拟网络、隔离 VLAN）
- ✅ 有**书面授权**的渗透测试与合规审计（明确授权抓包的网段、时间窗、目的）
- ✅ **你自己企业的网络**，且你**被正式授权**做监控（如安全运营团队的流量分析职责）
- ✅ 公开的示例 pcap 文件（用于学习）

**严禁**：

- ❌ 抓取任何非自有、非授权网络的流量
- ❌ 对同事、家人、邻居的设备抓包
- ❌ 用端口镜像/ARP 投毒获取未授权的流量
- ❌ 保留、分析、分享他人流量的 pcap
- ❌ 从抓包中提取他人凭据后用于任何目的
- ❌ 用 root 打开来源不明的 pcap（这既是安全问题，也可能是攻击者的陷阱）

**推荐的学习路径（完全合法）**：

```text
✅ 抓你自己的流量（你自己的设备，你自己的网络）
   → 能学到：协议结构、显示过滤器、Follow Stream、TLS 解密（自己的密钥）
✅ 分析 Wireshark 官方示例抓包（https://wiki.wireshark.org/SampleCaptures）
   → 能学到：各种协议的实战解析
✅ 在 host-only 虚拟网络里，用你自己的 Kali + 靶机做实验
   → 能学到：完整的安全分析流程
✅ 抓你自己的无线网络（配合 05 目录）
   → 能学到：802.11 分析、EAPOL、deauth 检测
```

**这四条路径覆盖了 100% 的知识点，而且完全合法。**

**最后一句**：Wireshark 是**防御者的显微镜**。请用它来**看清自己的网络**，而不是窥视别人的。
