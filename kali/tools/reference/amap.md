# amap

> Next-generation scanning tool for pentesters AMAP stands for Application MAPper. It is a next-generation scanning tool for pentesters. It attempts to identify applications even if they are running on a different port than normal. It also i…

> **功能分类**：通用工具 ｜ **Kali 包**：`amap` ｜ **官方文档**：<https://www.kali.org/tools/amap/>

## 1. 安装

```bash
sudo apt update
sudo apt install amap
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.4 |
| 架构 | any |
| 可执行命令 | `amap`、`amap6`、`amapcrap` |
| 依赖 | `libc6`、`libssl3t64` |
| 安装体积 | 282 KB |
| 官网 | <https://www.thc.org> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/amap> |
| 包追踪 | <https://pkg.kali.org/pkg/amap> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan port 80 on 192.168.1.15. Display the received banners (b), do not display closed ports (q), and use verbose output (v):
root@kali:~# amap -bqv 192.168.1.15 80
Using trigger file /etc/amap/appdefs.trig ... loaded 30 triggers
Using response file /etc/amap/appdefs.resp ... loaded 346 responses
Using trigger file /etc/amap/appdefs.rpc ... loaded 450 triggers

amap v5.4 (www.thc.org/thc-amap) started at 2014-05-13 19:07:16 - APPLICATION MAPPING mode

Total amount of tasks to perform in plain connect mode: 23
Protocol on 192.168.1.15:80/tcp (by trigger ssl) matches http - banner: \n\n501 Method Not Implemented\n\n
<h1>Method Not Implemented</h1>
\n

to /index.html not supported.
\n

\n

<hr />

\n

<address>Apache/2.2.22 (Debian) Server at 12
Protocol on 192.168.1.15:80/tcp (by trigger ssl) matches http-apache-2 - banner: \n\n501 Method Not Implemented\n\n</address>
<h1>Method Not Implemented</h1>
\n

to /index.html not supported.
\n

\n

<hr />

\n

<address>Apache/2.2.22 (Debian) Server at 12
Waiting for timeout on 19 connections ...</address>amap v5.4 finished at 2014-05-13 19:07:22
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `amap`

官方给出的调用示例：`amap -bqv 192.168.1.15 80`

```text
root@kali:~# amap -bqv 192.168.1.15 80
Using trigger file /etc/amap/appdefs.trig ... loaded 30 triggers
Using response file /etc/amap/appdefs.resp ... loaded 346 responses
Using trigger file /etc/amap/appdefs.rpc ... loaded 450 triggers
amap v5.4 (www.thc.org/thc-amap) started at 2014-05-13 19:07:16 - APPLICATION MAPPING mode
Total amount of tasks to perform in plain connect mode: 23
Protocol on 192.168.1.15:80/tcp (by trigger ssl) matches http - banner: \n\n501 Method Not Implemented\n\n
<h1>Method Not Implemented</h1>
\n
to /index.html not supported.
\n
\n
<hr />
\n
<address>Apache/2.2.22 (Debian) Server at 12
Protocol on 192.168.1.15:80/tcp (by trigger ssl) matches http-apache-2 - banner: \n\n501 Method Not Implemented\n\n</address>
<h1>Method Not Implemented</h1>
\n
to /index.html not supported.
\n
\n
<hr />
\n
<address>Apache/2.2.22 (Debian) Server at 12
Waiting for timeout on 19 connections ...</address>amap v5.4 finished at 2014-05-13 19:07:22
```

### `amap（示例）`

官方给出的调用示例：`amap -h`

```text
root@kali:~# amap -h
amap v5.4 (c) 2011 by van Hauser <
[email protected]
> www.thc.org/thc-amap
Syntax: amap [-A|-B|-P|-W] [-1buSRHUdqv] [[-m] -o <file>] [-D <file>] [-t/-T sec] [-c cons] [-C retries] [-p proto] [-i <file>] [target port [port] ...]
Modes:
  -A         Map applications: send triggers and analyse responses (default)
  -B         Just grab banners, do not send triggers
  -P         No banner or application stuff - be a (full connect) port scanner
Options:
  -1         Only send triggers to a port until 1st identification. Speeeeed!
  -6         Use IPv6 instead of IPv4
  -b         Print ascii banner of responses
  -i FILE    Nmap machine readable outputfile to read ports from
  -u         Ports specified on commandline are UDP (default is TCP)
  -R / -S    Do NOT identify RPC / SSL services
  -H         Do NOT send application triggers marked as potentially harmful
  -U         Do NOT dump unrecognised responses (better for scripting)
  -d         Dump all responses
  -v         Verbose mode, use twice (or more!) for debug (not recommended :-)
  -q         Do not report closed ports, and do not print them as unidentified
  -o FILE [-m] Write output to file FILE, -m creates machine readable output
  -c CONS    Amount of parallel connections to make (default 32, max 256)
  -C RETRIES Number of reconnects on connect timeouts (see -T) (default 3)
  -T SEC     Connect timeout on connection attempts in seconds (default 5)
  -t SEC     Response wait timeout in seconds (default 5)
  -p PROTO   Only send triggers for this protocol (e.g. ftp)
  TARGET PORT   The target address and port(s) to scan (additional to -i)
amap is a tool to identify application protocols on target ports.
Usage hint: Options "-bqv" are recommended, add "-1" for fast/rush checks.
```

### `amap（示例）`

官方给出的调用示例：`amap -h`

```text
root@kali:~# amap -h
amap v5.4 (c) 2011 by van Hauser <
[email protected]
> www.thc.org/thc-amap
Syntax: amap [-A|-B|-P|-W] [-1buSRHUdqv] [[-m] -o <file>] [-D <file>] [-t/-T sec] [-c cons] [-C retries] [-p proto] [-i <file>] [target port [port] ...]
Modes:
  -A         Map applications: send triggers and analyse responses (default)
  -B         Just grab banners, do not send triggers
  -P         No banner or application stuff - be a (full connect) port scanner
Options:
  -1         Only send triggers to a port until 1st identification. Speeeeed!
  -6         Use IPv6 instead of IPv4
  -b         Print ascii banner of responses
  -i FILE    Nmap machine readable outputfile to read ports from
  -u         Ports specified on commandline are UDP (default is TCP)
  -R / -S    Do NOT identify RPC / SSL services
  -H         Do NOT send application triggers marked as potentially harmful
  -U         Do NOT dump unrecognised responses (better for scripting)
  -d         Dump all responses
  -v         Verbose mode, use twice (or more!) for debug (not recommended :-)
  -q         Do not report closed ports, and do not print them as unidentified
  -o FILE [-m] Write output to file FILE, -m creates machine readable output
  -c CONS    Amount of parallel connections to make (default 32, max 256)
  -C RETRIES Number of reconnects on connect timeouts (see -T) (default 3)
  -T SEC     Connect timeout on connection attempts in seconds (default 5)
  -t SEC     Response wait timeout in seconds (default 5)
  -p PROTO   Only send triggers for this protocol (e.g. ftp)
  TARGET PORT   The target address and port(s) to scan (additional to -i)
amap is a tool to identify application protocols on target ports.
Usage hint: Options "-bqv" are recommended, add "-1" for fast/rush checks.
```

### `amap6`

官方给出的调用示例：`amap6 -h`

```text
root@kali:~# amap6 -h
amap v5.4 (c) 2011 by van Hauser <
[email protected]
> www.thc.org/thc-amap
Syntax: amap6 [-A|-B|-P|-W] [-1buSRHUdqv] [[-m] -o <file>] [-D <file>] [-t/-T sec] [-c cons] [-C retries] [-p proto] [-i <file>] [target port [port] ...]
Modes:
  -A         Map applications: send triggers and analyse responses (default)
  -B         Just grab banners, do not send triggers
  -P         No banner or application stuff - be a (full connect) port scanner
Options:
  -1         Only send triggers to a port until 1st identification. Speeeeed!
  -4         Use IPv4 instead of IPv6
  -b         Print ascii banner of responses
  -i FILE    Nmap machine readable outputfile to read ports from
  -u         Ports specified on commandline are UDP (default is TCP)
  -R / -S    Do NOT identify RPC / SSL services
  -H         Do NOT send application triggers marked as potentially harmful
  -U         Do NOT dump unrecognised responses (better for scripting)
  -d         Dump all responses
  -v         Verbose mode, use twice (or more!) for debug (not recommended :-)
  -q         Do not report closed ports, and do not print them as unidentified
  -o FILE [-m] Write output to file FILE, -m creates machine readable output
  -c CONS    Amount of parallel connections to make (default 32, max 256)
  -C RETRIES Number of reconnects on connect timeouts (see -T) (default 3)
  -T SEC     Connect timeout on connection attempts in seconds (default 5)
  -t SEC     Response wait timeout in seconds (default 5)
  -p PROTO   Only send triggers for this protocol (e.g. ftp)
  TARGET PORT   The target address and port(s) to scan (additional to -i)
amap is a tool to identify application protocols on target ports.
Usage hint: Options "-bqv" are recommended, add "-1" for fast/rush checks.
```

### `amapcrap`

官方给出的调用示例：`amapcrap -h`

```text
root@kali:~# amapcrap -h
amapcrap v5.4 (c) 2011 by van Hauser/THC <
[email protected]
>
Syntax: amapcrap [-S] [-u] [-m 0ab] [-M min,max] [-n connects] [-N delay] [-w delay] [-e] [-v] TARGET PORT
Options:
    -S           use SSL after TCP connect (not usuable with -u)
    -u           use UDP protocol (default: TCP) (not usable with -c)
    -n connects  maximum number of connects (default: unlimited)
    -N delay     delay between connects in ms (default: 0)
    -w delay     delay before closing the port (default: 250)
    -e           do NOT stop when a response was made by the server
    -v           verbose mode
    -m 0ab       send as random crap:0-nullbytes, a-letters+spaces, b-binary
    -M min,max   minimum and maximum length of random crap
    TARGET PORT  target (ip or dns) and port to send random crap
This tool sends random data to a silent port to illicit a response, which can
then be used within amap for future detection. It outputs proper amap
appdefs definitions. Note: by default all modes are activated (0:10%, a:40%,
b:50%). Mode 'a' always sends one line with letters and spaces which end with
\r\n. Visit our homepage at http://www.thc.org
Updated on: 2026-Mar-02
 Edit this page
sqldict
bed
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install amap`，再执行 `amap --version` 2>/dev/null || `amap -V`
- [ ] **2.** **读官方帮助** —— `amap -h`，需要细节时 `man amap`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage hint: Options "-bqv" are recommended, add "-1" for fast/rush checks.`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/amap/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/amap/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/amap/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
