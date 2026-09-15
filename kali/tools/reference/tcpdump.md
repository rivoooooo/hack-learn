# tcpdump

> Command-line network traffic analyzer This program allows you to dump the traffic on a network. tcpdump is able to examine IPv4, ICMPv4, IPv6, ICMPv6, UDP, TCP, SNMP, AFS BGP, RIP, PIM, DVMRP, IGMP, SMB, OSPF, NFS and many other packet typ…

> **功能分类**：信息搜集 ｜ **Kali 包**：`tcpdump` ｜ **官方文档**：<https://www.kali.org/tools/tcpdump/>

## 1. 安装

```bash
sudo apt update
sudo apt install tcpdump
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.99.6 |
| 架构 | any |
| 可执行命令 | `tcpdump` |
| 依赖 | `libc6`、`libpcap0.8t64`、`libssl3t64` |
| 安装体积 | 1.31 MB |
| 官网 | <https://www.tcpdump.org/> |
| 源码仓库 | <https://salsa.debian.org/debian/tcpdump> |
| 包追踪 | <https://pkg.kali.org/pkg/tcpdump> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
tcpdump -h          # 查看用法
man tcpdump         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tcpdump`

> 官方示例调用：`tcpdump -h`

```text
root@kali:~# tcpdump -h
tcpdump version 4.99.6
libpcap version 1.10.6 (64-bit time_t, with TPACKET_V3)
OpenSSL 3.6.3 9 Jun 2026
64-bit build, 64-bit time_t
Usage: tcpdump [-AbdDefghHIJKlLnNOpqStuUvxX#] [ -B size ] [ -c count ] [--count]
		[ -C file_size ] [ -E algo:secret ] [ -F file ] [ -G seconds ]
		[ -i interface ] [ --immediate-mode ] [ -j tstamptype ]
		[ -M secret ] [ --number ] [ --print ] [ -Q in|out|inout ]
		[ -r file ] [ -s snaplen ] [ -T type ] [ --version ]
		[ -V file ] [ -w file ] [ -W filecount ] [ -y datalinktype ]
		[ --time-stamp-precision precision ] [ --micro ] [ --nano ]
		[ -z postrotate-command ] [ -Z user ] [ expression ]
Learn more with
OffSec
Want to learn more about tcpdump? get access to in-depth training and hands-on labs:
PEN-200: 18.2.2. Linux Privilege Escalation: Inspecting Service Footprints
PEN-200: 20. Tunneling Through Deep Packet Inspection
Digital Forensics Foundations: 6.2.2. Network Forensics: Tcpdump and Wireshark
IT Generalist Common Tools: 1.4. Wireshark Essentials: Remote Packet Capture
Network Penetration Testing Essentials: 6.5.2. Networking Fundamentals: Tcpdump
PEN-200 course
Updated on: 2026-Aug-25
 Edit this page
syft
tcpreplay
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install tcpdump`，再执行 `tcpdump --version` 2>/dev/null || `tcpdump -V`
- [ ] **2.** **读官方帮助** —— `tcpdump -h`，需要细节时 `man tcpdump`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: tcpdump [-AbdDefghHIJKlLnNOpqStuUvxX#] [ -B size ] [ -c count ] [--count]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/tcpdump/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[tcpdump](../../tools/tutorials/07-嗅探与欺骗/tcpdump.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/tcpdump/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/tcpdump/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
