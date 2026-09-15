# tcpflow

> TCP flow recorder tcpflow is a program that captures data transmitted as part of TCP connections (flows), and stores the data in a way that is convenient for protocol analysis or debugging. A program like ’tcpdump’ shows a summary of packe…

> **功能分类**：嗅探与欺骗 ｜ **Kali 包**：`tcpflow` ｜ **官方文档**：<https://www.kali.org/tools/tcpflow/>

## 1. 安装

```bash
sudo apt update
sudo apt install tcpflow
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6.1 |
| 架构 | any |
| 可执行命令 | `tcpflow`、`tcpflow-nox` |
| 依赖 | `libc6`、`libcairo2`、`libgcc-s1`、`libhttp-parser2.9`、`libpcap0.8t64`、`libssl3t64`、`libstdc++6`、`zlib1g` |
| 安装体积 | 819 KB |
| 官网 | <https://github.com/simsong/tcpflow> |
| 源码仓库 | <https://salsa.debian.org/debian/tcpflow> |
| 包追踪 | <https://pkg.kali.org/pkg/tcpflow> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
tcpflow -h          # 查看用法
man tcpflow         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tcpflow`

> 官方示例调用：`tcpflow -h`

```text
root@kali:~# tcpflow -h
TCPFLOW version 1.6.1
usage: tcpflow [-aBcCDhIpsvVZ] [-b max_bytes] [-d debug_level]
     [-[eE] scanner] [-f max_fds] [-F[ctTXMkmg]] [-h|--help] [-i iface]
     [-l files...] [-L semlock] [-m min_bytes] [-o outdir] [-r file] [-R file]
     [-S name=value] [-T template] [-U|--relinquish-privileges user] [-v|--verbose]
     [-w file] [-x scanner] [-X xmlfile] [-z|--chroot dir] [expression]
   -a: do ALL post-processing.
   -b max_bytes: max number of bytes per flow to save
   -d debug_level: debug level; default is 1
   -f: maximum number of file descriptors to use
   -h: print this help message (-hh for more help)
   -H: print detailed information about each scanner
   -i: network interface on which to listen
   -I: write for each flow another file *.findx to provide byte-indexed timestamps
   -g: output each flow in alternating colors (note change!)
   -l: treat non-flag arguments as input files rather than a pcap expression
   -L  semlock - specifies that writes are locked using a named semaphore
   -p: don't use promiscuous mode
   -q: quiet mode - do not print warnings
   -r file      : read packets from tcpdump pcap file (may be repeated)
   -R file      : read packets from tcpdump pcap file TO FINISH CONNECTIONS
   -v           : verbose operation equivalent to -d 10
   -V           : print version number and exit
   -w  file     : write packets not processed to file
   -o  outdir   : specify output directory (default '.')
   -X  filename : DFXML output to filename
   -m  bytes    : specifies skip that starts a new stream (default 16777216).
   -F{p} : filename prefix/suffix (-hh for options)
   -T{t} : filename template (-hh for options; default %A.%a-%B.%b%V%v%C%c)
   -Z       do not decompress gzip-compressed HTTP transactions
   -K: output|keep pcap flow structure.
Security:
   -U user  relinquish privleges and become user (if running as root)
   -z dir   chroot to dir (requires that -U be used).
Control of Scanners:
   -E scanner   - turn off all scanners except scanner
   -S name=value  Set a configuration parameter (-hh for info)
Console output options:
   -B: binary output, even with -c or -C (normally -c or -C turn it off)
   -c: console print only (don't create files)
   -C: console print only, but without the display of source/dest header
   -0: don't print newlines after packets when printing to console
   -s: strip non-printable characters (change to '.')
   -J: output json format.
   -D: output in hex (useful to combine with -c or -C)
expression: tcpdump-like filtering expression
See the man page for additional information.
```

### `tcpflow -h`

> 官方示例调用：`tcpflow -h`

```text
root@kali:~# tcpflow -h
TCPFLOW version 1.6.1
usage: tcpflow [-aBcCDhIpsvVZ] [-b max_bytes] [-d debug_level]
     [-[eE] scanner] [-f max_fds] [-F[ctTXMkmg]] [-h|--help] [-i iface]
     [-l files...] [-L semlock] [-m min_bytes] [-o outdir] [-r file] [-R file]
     [-S name=value] [-T template] [-U|--relinquish-privileges user] [-v|--verbose]
     [-w file] [-x scanner] [-X xmlfile] [-z|--chroot dir] [expression]
   -a: do ALL post-processing.
   -b max_bytes: max number of bytes per flow to save
   -d debug_level: debug level; default is 1
   -f: maximum number of file descriptors to use
   -h: print this help message (-hh for more help)
   -H: print detailed information about each scanner
   -i: network interface on which to listen
   -I: write for each flow another file *.findx to provide byte-indexed timestamps
   -g: output each flow in alternating colors (note change!)
   -l: treat non-flag arguments as input files rather than a pcap expression
   -L  semlock - specifies that writes are locked using a named semaphore
   -p: don't use promiscuous mode
   -q: quiet mode - do not print warnings
   -r file      : read packets from tcpdump pcap file (may be repeated)
   -R file      : read packets from tcpdump pcap file TO FINISH CONNECTIONS
   -v           : verbose operation equivalent to -d 10
   -V           : print version number and exit
   -w  file     : write packets not processed to file
   -o  outdir   : specify output directory (default '.')
   -X  filename : DFXML output to filename
   -m  bytes    : specifies skip that starts a new stream (default 16777216).
   -F{p} : filename prefix/suffix (-hh for options)
   -T{t} : filename template (-hh for options; default %A.%a-%B.%b%V%v%C%c)
   -Z       do not decompress gzip-compressed HTTP transactions
   -K: output|keep pcap flow structure.
Security:
   -U user  relinquish privleges and become user (if running as root)
   -z dir   chroot to dir (requires that -U be used).
Control of Scanners:
   -E scanner   - turn off all scanners except scanner
   -S name=value  Set a configuration parameter (-hh for info)
Console output options:
   -B: binary output, even with -c or -C (normally -c or -C turn it off)
   -c: console print only (don't create files)
   -C: console print only, but without the display of source/dest header
   -0: don't print newlines after packets when printing to console
   -s: strip non-printable characters (change to '.')
   -J: output json format.
   -D: output in hex (useful to combine with -c or -C)
expression: tcpdump-like filtering expression
See the man page for additional information.
```

### `tcpflow -h`

> 官方示例调用：`tcpflow -h`

```text
root@kali:~# tcpflow -h
TCPFLOW version 1.6.1
usage: tcpflow [-aBcCDhIpsvVZ] [-b max_bytes] [-d debug_level]
     [-[eE] scanner] [-f max_fds] [-F[ctTXMkmg]] [-h|--help] [-i iface]
     [-l files...] [-L semlock] [-m min_bytes] [-o outdir] [-r file] [-R file]
     [-S name=value] [-T template] [-U|--relinquish-privileges user] [-v|--verbose]
     [-w file] [-x scanner] [-X xmlfile] [-z|--chroot dir] [expression]
   -a: do ALL post-processing.
   -b max_bytes: max number of bytes per flow to save
   -d debug_level: debug level; default is 1
   -f: maximum number of file descriptors to use
   -h: print this help message (-hh for more help)
   -H: print detailed information about each scanner
   -i: network interface on which to listen
   -I: write for each flow another file *.findx to provide byte-indexed timestamps
   -g: output each flow in alternating colors (note change!)
   -l: treat non-flag arguments as input files rather than a pcap expression
   -L  semlock - specifies that writes are locked using a named semaphore
   -p: don't use promiscuous mode
   -q: quiet mode - do not print warnings
   -r file      : read packets from tcpdump pcap file (may be repeated)
   -R file      : read packets from tcpdump pcap file TO FINISH CONNECTIONS
   -v           : verbose operation equivalent to -d 10
   -V           : print version number and exit
   -w  file     : write packets not processed to file
   -o  outdir   : specify output directory (default '.')
   -X  filename : DFXML output to filename
   -m  bytes    : specifies skip that starts a new stream (default 16777216).
   -F{p} : filename prefix/suffix (-hh for options)
   -T{t} : filename template (-hh for options; default %A.%a-%B.%b%V%v%C%c)
   -Z       do not decompress gzip-compressed HTTP transactions
   -K: output|keep pcap flow structure.
Security:
   -U user  relinquish privleges and become user (if running as root)
   -z dir   chroot to dir (requires that -U be used).
Control of Scanners:
   -E scanner   - turn off all scanners except scanner
   -S name=value  Set a configuration parameter (-hh for info)
Console output options:
   -B: binary output, even with -c or -C (normally -c or -C turn it off)
   -c: console print only (don't create files)
   -C: console print only, but without the display of source/dest header
   -0: don't print newlines after packets when printing to console
   -s: strip non-printable characters (change to '.')
   -J: output json format.
   -D: output in hex (useful to combine with -c or -C)
expression: tcpdump-like filtering expression
See the man page for additional information.
Updated on: 2025-Dec-09
 Edit this page
t50
tcpick
LIGHT
DARK
Links
Home
Download / Get Kali
Blog
OS Documentation
Tool Documentation
System Status
Archived Releases
Partnerships
Platforms
ARM (SBC)
NetHunter (Mobile)
Amazon AWS
Docker
Linode
Microsoft Azure
Microsoft Store (WSL)
Vagrant
Development
Bug Tracker
Continuous Integration
Network Mirror
Package Tracker
GitLab
Community
Discord
Support Forum
PeerTube
Follow Us
Bluesky
Facebook
Instagram
Mastodon
Substack
X
Newsletter
RSS
Policies
Cookie Policy
Privacy Policy
Trademark Policy
© OffSec Services Limited 2026. All rights reserved.
Kali Linux is part of OffSec's Community Projects
Learn more about OffSec's free, open-source penetration testing tools for cybersecurity professionals
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install tcpflow`，再执行 `tcpflow --version` 2>/dev/null || `tcpflow -V`
- [ ] **2.** **读官方帮助** —— `tcpflow -h`，需要细节时 `man tcpflow`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `tcpflow -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/tcpflow/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/tcpflow/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/tcpflow/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
