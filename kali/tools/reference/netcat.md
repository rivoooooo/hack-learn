# netcat

> TCP/IP swiss army knife A simple Unix utility which reads and writes data across network connections using TCP or UDP protocol. It is designed to be a reliable “back-end” tool that can be used directly or easily driven by other programs an…

> **功能分类**：信息搜集 ｜ **Kali 包**：`netcat` ｜ **官方文档**：<https://www.kali.org/tools/netcat/>

## 1. 安装

```bash
sudo apt update
sudo apt install netcat-traditional
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.10 |
| 架构 | any |
| 可执行命令 | `netcat-traditional`、`nc.traditional` |
| 依赖 | `libc6`、`nc.traditional` |
| 安装体积 | 139 KB |
| 官网 | <http://www.stearns.org/nc/> |
| 源码仓库 | <https://salsa.debian.org/debian/netcat> |
| 包追踪 | <https://pkg.kali.org/pkg/netcat> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
netcat-traditional -h          # 查看用法
man netcat-traditional         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `nc.traditional`

> 官方示例调用：`nc.traditional -h`

```text
root@kali:~# nc.traditional -h
[v1.10-50.1]
connect to somewhere:	nc [-options] hostname port[s] [ports] ...
listen for inbound:	nc -l -p port [-options] [hostname] [port]
options:
	-c shell commands	as `-e'; use /bin/sh to exec [dangerous!!]
	-e filename		program to exec after connect [dangerous!!]
	-b			allow broadcasts
	-g gateway		source-routing hop point[s], up to 8
	-G num			source-routing pointer: 4, 8, 12, ...
	-h			this cruft
	-i secs			delay interval for lines sent, ports scanned
        -k                      set keepalive option on socket
	-l			listen mode, for inbound connects
	-n			numeric-only IP addresses, no DNS
	-o file			hex dump of traffic
	-p port			local port number
	-r			randomize local and remote ports
	-q secs			quit after EOF on stdin and delay of secs
	-s addr			local source address
	-T tos			set Type Of Service
	-t			answer TELNET negotiation
	-u			UDP mode
	-v			verbose [use twice to be more verbose]
	-w secs			timeout for connects and final net reads
	-C			Send CRLF as line-ending
	-z			zero-I/O mode [used for scanning]
port numbers can be individual or ranges: lo-hi [inclusive];
hyphens in port names must be backslash escaped (e.g. 'ftp\-data').
Learn more with
OffSec
Want to learn more about netcat? get access to in-depth training and hands-on labs:
PEN-200: 6.4.2. Information Gathering: TCP/UDP Port Scanning Theory
Network Penetration Testing Essentials: 19.2.2. File Transfers: Netcat
Network Penetration Testing Essentials: 10.6. Linux Networking and Services I: Netcat (nc)
Security Operations Essentials: 8.6. Linux Networking and Services I: Netcat (nc)
Network Penetration Testing Essentials: 14.2.1. Working with Shells
Network Penetration Testing Essentials: 14.2.1. Working with Shells: Netcat Shells
PEN-200 course
Updated on: 2025-Dec-09
 Edit this page
netbase
netdiscover
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install netcat-traditional`，再执行 `netcat-traditional --version` 2>/dev/null || `netcat-traditional -V`
- [ ] **2.** **读官方帮助** —— `netcat-traditional -h`，需要细节时 `man netcat-traditional`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `netcat-traditional -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/netcat/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[netcat](../../tools/tutorials/06-漏洞利用/netcat.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/netcat/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/netcat/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
