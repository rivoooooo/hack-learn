# inviteflood

> SIP/SDP INVITE message flooding over UDP/IP A tool to perform SIP/SDP INVITE message flooding over UDP/IP. It was tested on a Linux Red Hat Fedora Core 4 platform (Pentium IV, 2.5 GHz), but it is expected this tool will successfully build …

> **功能分类**：漏洞分析 ｜ **Kali 包**：`inviteflood` ｜ **官方文档**：<https://www.kali.org/tools/inviteflood/>

## 1. 安装

```bash
sudo apt update
sudo apt install inviteflood
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.0 |
| 架构 | any |
| 可执行命令 | `inviteflood` |
| 依赖 | `libc6`、`libnet9` |
| 安装体积 | 33 KB |
| 官网 | <http://www.hackingvoip.com/sec_tools.html> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/inviteflood> |
| 包追踪 | <https://pkg.kali.org/pkg/inviteflood> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Using the eth0 interface (eth0) and the provided user (5000), flood the target domain (example.local) and flood target (192.168.1.5) using 100 packets (100):
root@kali:~# inviteflood eth0 5000 example.local 192.168.1.5 100

inviteflood - Version 2.0
              June 09, 2006

source IPv4 addr:port   = 192.168.1.202:9
dest   IPv4 addr:port   = 192.168.1.5:5060
targeted UA             = 5000@192.168.1.1

Flooding destination with 100 packets
sent: 100
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `inviteflood`

> 官方示例调用：`inviteflood eth0 5000 example.local 192.168.1.5 100`

```text
root@kali:~# inviteflood eth0 5000 example.local 192.168.1.5 100
inviteflood - Version 2.0
              June 09, 2006
source IPv4 addr:port   = 192.168.1.202:9
dest   IPv4 addr:port   = 192.168.1.5:5060
targeted UA             =
[email protected]
Flooding destination with 100 packets
sent: 100
```

### `inviteflood -h`

> 官方示例调用：`inviteflood -h`

```text
root@kali:~# inviteflood -h
inviteflood - Version 2.0
              June 09, 2006
 Usage:
 Mandatory -
	interface (e.g. eth0)
	target user (e.g. "" or john.doe or 5000 or "1+210-555-1212")
	target domain (e.g. enterprise.com or an IPv4 address)
	IPv4 addr of flood target (ddd.ddd.ddd.ddd)
	flood stage (i.e. number of packets)
 Optional -
	-a flood tool "From:" alias (e.g. jane.doe)
	-i IPv4 source IP address [default is IP address of interface]
	-S srcPort  (0 - 65535) [default is well-known discard port 9]
	-D destPort (0 - 65535) [default is well-known SIP port 5060]
	-l lineString line used by SNOM [default is blank]
	-s sleep time btwn INVITE msgs (usec)
	-h help - print this usage
	-v verbose output mode
Updated on: 2026-Mar-02
 Edit this page
impacket
jsp-file-browser
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install inviteflood`，再执行 `inviteflood --version` 2>/dev/null || `inviteflood -V`
- [ ] **2.** **读官方帮助** —— `inviteflood -h`，需要细节时 `man inviteflood`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/inviteflood/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/impact.md`](../../tools/by-attack/impact.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/inviteflood/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/inviteflood/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
