# dsniff

> Various tools to sniff network traffic for cleartext insecurities This package contains several tools to listen to and create network traffic: arpspoof - Send out unrequested (and possibly forged) arp replies. dnsspoof - forge replies to a…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`dsniff` ｜ **官方文档**：<https://www.kali.org/tools/dsniff/>

## 1. 安装

```bash
sudo apt update
sudo apt install dsniff
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.5a2 |
| 架构 | any |
| 可执行命令 | `dsniff`、`arpspoof`、`dnsspoof`、`filesnarf`、`macof`、`mailsnarf`、`msgsnarf`、`sshmitm`、`sshow`、`tcpkill`、`tcpnice`、`urlsnarf`、`webmitm`、`webspy` |
| 依赖 | `libc6`、`libnet9`、`libnids1.21t64`、`libpcap0.8t64`、`libssl3t64`、`libtirpc3t64`、`libx11-6`、`libxmu6`、`openssl`、`arpspoof` |
| 安装体积 | 582 KB |
| 官网 | <https://github.com/hackerschoice/dsniff> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/dsniff> |
| 包追踪 | <https://pkg.kali.org/pkg/dsniff> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
dsniff -h          # 查看用法
man dsniff         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 14 个可执行命令，下面是官方页面内嵌的帮助原文。

### `arpspoof`

> 官方示例调用：`arpspoof --help`

```text
root@kali:~# arpspoof --help
arpspoof: invalid option -- '-'
Version: 2.5a2
Usage: arpspoof [-i interface] [-c own|host|both] [-t target] [-r] host
```

### `dnsspoof`

> 官方示例调用：`dnsspoof --help`

```text
root@kali:~# dnsspoof --help
dnsspoof: invalid option -- '-'
Version: 2.5a2
Usage: dnsspoof [-i interface] [-f hostsfile] [expression]
```

### `dsniff`

> 官方示例调用：`dsniff --help`

```text
root@kali:~# dsniff --help
dsniff: invalid option -- '-'
Version: 2.5a2
Usage: dsniff [-cdamDNPCv] [-i interface | -p pcapfile] [-s snaplen]
              [-f services] [-t trigger[,...]]
              [pcap filter]
 -c         Half-duplex TCP stream assembly
 -a         Show duplicates
 -v         Verbose. Show banners
 -d         Enable debugging mode
 -D         Disable DPI. Only decode known ports.
 -m         Force DPI also on known ports (e.g. ignore /etc/services).
            For example, -m will detect SSH on port 443 (https).
 -C         Force color output even if not a TTY (disable color: dsniff|cat)
 -N         Resolve IP addresses to hostname
 -P         Enable promisc mode
 -t <...>   Force a decoding method for a specific port/protocol.
            Example: Decode IMAP on port 8143: -t 8143/tcp=imap
 -i <link>  Specify the interface to listen on
 -p <file>  Read from pcap file
 -s <len>   Analyze at most the first snaplen of each TCP connection [default: 1024]
 Example:
   dsniff -i eth0 -C >log.txt
```

### `filesnarf`

> 官方示例调用：`filesnarf --help`

```text
root@kali:~# filesnarf --help
filesnarf: invalid option -- '-'
Version: 2.5a2
Usage: filesnarf [-i interface | -p pcapfile] [[-v] pattern [expression]]
```

### `macof`

> 官方示例调用：`macof --help`

```text
root@kali:~# macof --help
macof: invalid option -- '-'
Version: 2.5a2
Usage: macof [-s src] [-d dst] [-e tha] [-x sport] [-y dport]
             [-i interface] [-n times]
```

### `mailsnarf`

> 官方示例调用：`mailsnarf --help`

```text
root@kali:~# mailsnarf --help
mailsnarf: invalid option -- '-'
Version: 2.5a2
Usage: mailsnarf [-i interface | -p pcapfile] [[-v] pattern [expression]]
```

### `msgsnarf`

> 官方示例调用：`msgsnarf --help`

```text
root@kali:~# msgsnarf --help
msgsnarf: invalid option -- '-'
Version: 2.5a2
Usage: msgsnarf [-i interface | -p pcapfile] [[-v] pattern [expression]]
```

### `sshmitm`

> 官方示例调用：`sshmitm --help`

```text
root@kali:~# sshmitm --help
sshmitm: invalid option -- '-'
Version: 2.5a2
Usage: sshmitm [-d] [-I] [-p port] host [port]
```

### `sshow`

> 官方示例调用：`sshow --help`

```text
root@kali:~# sshow --help
sshow: invalid option -- '-'
Usage: sshow [-d] [-i interface | -p pcapfile]
```

### `tcpkill`

> 官方示例调用：`tcpkill --help`

```text
root@kali:~# tcpkill --help
tcpkill: invalid option -- '-'
Version: 2.5a2
Usage: tcpkill [-i interface] [-1..9] expression
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install dsniff`，再执行 `dsniff --version` 2>/dev/null || `dsniff -V`
- [ ] **2.** **读官方帮助** —— `dsniff -h`，需要细节时 `man dsniff`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: arpspoof [-i interface] [-c own|host|both] [-t target] [-r] host`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dsniff/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dsniff/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dsniff/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
