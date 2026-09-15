# voiphopper

> Runs a VLAN hop security test VoIP Hopper is a GPLv3 licensed security tool, written in C that rapidly runs a VLAN Hop security test. VoIP Hopper is a VoIP infrastructure security testing tool but also a tool that can be used to test the (…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`voiphopper` ｜ **官方文档**：<https://www.kali.org/tools/voiphopper/>

## 1. 安装

```bash
sudo apt update
sudo apt install voiphopper
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.04 |
| 架构 | any |
| 可执行命令 | `voiphopper` |
| 依赖 | `libc6`、`libpcap0.8t64` |
| 安装体积 | 130 KB |
| 官网 | <https://sourceforge.net/projects/voiphopper> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/voiphopper> |
| 包追踪 | <https://pkg.kali.org/pkg/voiphopper> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# voiphopper -i eth0 -z
VoIP Hopper assessment mode ~ Select 'q' to quit and 'h' for help menu.
Main Sniffer:  capturing packets on eth0
a
Analyzing ARP packets on default interface: eth0
New host #1 learned on eth0: (MAC): 78:ca:39:fe:0b:4c   (IP): 192.168.1.229
New host #2 learned on eth0: (MAC): 60:6b:bd:5a:b6:6c   (IP): 192.168.1.213
New host #3 learned on eth0: (MAC): 40:6c:8f:1b:cb:90   (IP): 192.168.1.232
a
Disabling analysis of ARP packets on default interface:  eth0
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `voiphopper`

官方给出的调用示例：`voiphopper -i eth0 -z`

```text
root@kali:~# voiphopper -i eth0 -z
VoIP Hopper assessment mode ~ Select 'q' to quit and 'h' for help menu.
Main Sniffer:  capturing packets on eth0
a
Analyzing ARP packets on default interface: eth0
New host #1 learned on eth0: (MAC): 78:ca:39:fe:0b:4c   (IP): 192.168.1.229
New host #2 learned on eth0: (MAC): 60:6b:bd:5a:b6:6c   (IP): 192.168.1.213
New host #3 learned on eth0: (MAC): 40:6c:8f:1b:cb:90   (IP): 192.168.1.232
a
Disabling analysis of ARP packets on default interface:  eth0
```

### `voiphopper（示例）`

官方给出的调用示例：`voiphopper -h`

```text
root@kali:~# voiphopper -h
VoIP Hopper Extended Usage:
Miscellaneous Options:
	-l (list available interfaces for CDP sniffing, then exit)
	Example:  voiphopper -l
	-m (Spoof the MAC Address, then exit)
	Example:  voiphopper -i eth0 -m 00:07:0E:EA:50:86
	-d (Delete the VLAN Interface, then exit)
	Example:  voiphopper -d eth0.200
	-V (Print the VoIP Hopper version, then exit)
	Example:  voiphopper -V
MAC Address Spoofing Options (used with -a, -v, or -c options):
	-m (Spoof the MAC Address of existing interface, and new Interface)
	-D -m (Spoof the MAC Address of only new Voice Interface)
	Example:  voiphopper -i eth0 -m 00:07:0E:EA:50:86
	Example:  voiphopper -i eth0 -D -m 00:07:0E:EA:50:86
CDP Sniff Mode (-c 0)
	Example:  voiphopper -i eth0 -c 0
CDP Spoof Mode (-c 1):
	-E <string> (Device ID)
	-P <string> (Port ID)
	-C <string> (Capabilities)
	-L <string> (Platform)
	-S <string> (Software)
	-U <string> (Duplex)
Example Usage for SIP Firmware Phone:
voiphopper -i eth0 -c 1 -E 'SIP00070EEA5086' -P 'Port 1' -C Host -L 'Cisco IP Phone 7940' -S 'P003-08-8-00' -U 1
Example Usage for SCCP Firmware Phone:
voiphopper -i eth0 -c 1 -E 'SEP0070EEA5086' -P 'Port 1' -C Host -L 'Cisco IP Phone 7940' -S 'P00308000700' -U 1
Example Usage for Phone with MAC Spoofing:
voiphopper -i eth0 -m 00:07:0E:EA:50:86 -c 1 -E 'SEP00070EEA5086' -P 'Port 1' -C Host -L 'Cisco IP Phone 7940' -S 'P003-08-8-00' -U 1
Avaya DHCP Option Mode (-a):
	Example:  voiphopper -i eth0 -a
	Example:  voiphopper -i eth0 -a -m 00:07:0E:EA:50:86
VLAN Hop Mode (-v VLAN ID):
	Example:  voiphopper -i eth0 -v 200
	Example:  voiphopper -i eth0 -v 200 -D -m 00:07:0E:EA:50:86
Alcatel VLAN Discovery (-t 0|1|2):
	Example:  voiphopper -i eth0 -t 0
	Example:  voiphopper -i eth0 -t 1
	Example:  voiphopper -i eth0 -t 0 -m 00:80:9f:ad:42:42
	Example:  voiphopper -i eth0 -t 1 -m 00:80:9f:ad:42:42
	Example:  voiphopper -i eth0 -t 2 -v 800
	Example:  voiphopper -i eth0 -t 2 -v 800 -m 00:80:9f:ad:42:42
Updated on: 2025-Dec-09
 Edit this page
vlan
watobo
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install voiphopper`，再执行 `voiphopper --version` 2>/dev/null || `voiphopper -V`
- [ ] **2.** **读官方帮助** —— `voiphopper -h`，需要细节时 `man voiphopper`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `voiphopper -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/voiphopper/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/voiphopper/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/voiphopper/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
