# nbtscan

> Scan networks searching for NetBIOS information NBTscan is a program for scanning IP networks for NetBIOS name information. It sends NetBIOS status query to each address in supplied range and lists received information in human readable fo…

> **功能分类**：信息搜集 ｜ **Kali 包**：`nbtscan` ｜ **官方文档**：<https://www.kali.org/tools/nbtscan/>

## 1. 安装

```bash
sudo apt update
sudo apt install nbtscan
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.7.2 |
| 架构 | any |
| 可执行命令 | `nbtscan` |
| 依赖 | `libc6` |
| 安装体积 | 57 KB |
| 官网 | <https://github.com/resurrecting-open-source-projects/nbtscan> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/nbtscan> |
| 包追踪 | <https://pkg.kali.org/pkg/nbtscan> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
nbtscan -h          # 查看用法
man nbtscan         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `nbtscan`

官方给出的调用示例：`nbtscan --help`

```text
root@kali:~# nbtscan --help
NBTscan version 1.7.2.
This is a free software and it comes with absolutely no warranty.
You can use, distribute and modify it under terms of GNU GPL 2+.
Usage:
nbtscan [-v] [-d] [-e] [-l] [-t timeout] [-b bandwidth] [-r] [-q] [-s separator] [-m retransmits] (-f filename)|(<scan_range>)
	-v		verbose output. Print all names received
			from each host
	-d		dump packets. Print whole packet contents.
	-e		Format output in /etc/hosts format.
	-l		Format output in lmhosts format.
			Cannot be used with -v, -s or -h options.
	-t timeout	wait timeout milliseconds for response.
			Default 1000.
	-b bandwidth	Output throttling. Slow down output
			so that it uses no more that bandwidth bps.
			Useful on slow links, so that ougoing queries
			don't get dropped.
	-r		use local port 137 for scans. Win95 boxes
			respond to this only.
			You need to be root to use this option on Unix.
	-q		Suppress banners and error messages,
	-s separator	Script-friendly output. Don't print
			column and record headers, separate fields with separator.
	-h		Print human-readable names for services.
			Can only be used with -v option.
	-m retransmits	Number of retransmits. Default 0.
	-f filename	Take IP addresses to scan from file filename.
			-f - makes nbtscan take IP addresses from stdin.
	<scan_range>	what to scan. Can either be single IP
			like 192.168.1.1 or
			range of addresses in one of two forms:
			xxx.xxx.xxx.xxx/xx or xxx.xxx.xxx.xxx-xxx.
Examples:
	nbtscan -r 192.168.1.0/24
		Scans the whole C-class network.
	nbtscan 192.168.1.25-137
		Scans a range from 192.168.1.25 to 192.168.1.137
	nbtscan -v -s : 192.168.1.0/24
		Scans C-class network. Prints results in script-friendly
		format using colon as field separator.
		Produces output like that:
		192.168.0.1:NT_SERVER:00U
		192.168.0.1:MY_DOMAIN:00G
		192.168.0.1:ADMINISTRATOR:03U
		192.168.0.2:OTHER_BOX:00U
		...
	nbtscan -f iplist
		Scans IP addresses specified in file iplist.
Learn more with
OffSec
Want to learn more about nbtscan? get access to in-depth training and hands-on labs:
PEN-200: 6.4.4. Information Gathering: SMB Enumeration
PEN-200 course
Updated on: 2025-Dec-09
 Edit this page
nasty
nbtscan-unixwiz
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install nbtscan`，再执行 `nbtscan --version` 2>/dev/null || `nbtscan -V`
- [ ] **2.** **读官方帮助** —— `nbtscan -h`，需要细节时 `man nbtscan`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/nbtscan/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[nbtscan](../../tools/tutorials/01-信息搜集/nbtscan.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/nbtscan/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/nbtscan/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
