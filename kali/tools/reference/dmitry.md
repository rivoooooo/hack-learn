# dmitry

> Deepmagic Information Gathering Tool DMitry is a UNIX/(GNU)Linux command line application written in C. DMitry can find possible subdomains, email addresses, uptime information, perform tcp port scan, whois lookups, and more.

> **功能分类**：信息搜集 ｜ **Kali 包**：`dmitry` ｜ **官方文档**：<https://www.kali.org/tools/dmitry/>

## 1. 安装

```bash
sudo apt update
sudo apt install dmitry
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3a |
| 架构 | any |
| 可执行命令 | `dmitry` |
| 依赖 | `libc6` |
| 安装体积 | 50 KB |
| 官网 | <https://mor-pah.net/software/dmitry-deepmagic-information-gathering-tool/> |
| 源码仓库 | <https://salsa.debian.org/debian/dmitry> |
| 包追踪 | <https://pkg.kali.org/pkg/dmitry> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Run a domain whois lookup (w), an IP whois lookup (i), retrieve Netcraft info (n), search for subdomains (s), search for email addresses (e), do a TCP port scan (p), and save the output to example.txt (o) for the domain example.com:
root@kali:~# dmitry -winsepo example.txt example.com
Deepmagic Information Gathering Tool
"There be some deep magic going on"

Writing output to 'example.txt'

HostIP:93.184.216.119
HostName:example.com

Gathered Inet-whois information for 93.184.216.119
---------------------------------
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dmitry`

官方给出的调用示例：`dmitry -winsepo example.txt example.com`

```text
root@kali:~# dmitry -winsepo example.txt example.com
Deepmagic Information Gathering Tool
"There be some deep magic going on"
Writing output to 'example.txt'
HostIP:93.184.216.119
HostName:example.com
Gathered Inet-whois information for 93.184.216.119
---------------------------------
```

### `dmitry（示例）`

官方给出的调用示例：`dmitry -h`

```text
root@kali:~# dmitry -h
Deepmagic Information Gathering Tool
"There be some deep magic going on"
Usage: dmitry [-winsepfb] [-t 0-9] [-o %host.txt] host
  -o	 Save output to %host.txt or to file specified by -o file
  -i	 Perform a whois lookup on the IP address of a host
  -w	 Perform a whois lookup on the domain name of a host
  -n	 Retrieve Netcraft.com information on a host
  -s	 Perform a search for possible subdomains
  -e	 Perform a search for possible email addresses
  -p	 Perform a TCP port scan on a host
* -f	 Perform a TCP port scan on a host showing output reporting filtered ports
* -b	 Read in the banner received from the scanned port
* -t 0-9 Set the TTL in seconds when scanning a TCP port ( Default 2 )
*Requires the -p flagged to be passed
Learn more with
OffSec
Want to learn more about dmitry? get access to in-depth training and hands-on labs:
Security Operations Essentials: 11.2.1. Enterprise Network Architecture: Learn how Open-Source Intelligence Helps Identify the Enterprise Footprint
Updated on: 2025-Dec-09
 Edit this page
dirsearch
dns2tcp
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dmitry`，再执行 `dmitry --version` 2>/dev/null || `dmitry -V`
- [ ] **2.** **读官方帮助** —— `dmitry -h`，需要细节时 `man dmitry`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: dmitry [-winsepfb] [-t 0-9] [-o %host.txt] host`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dmitry/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dmitry/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dmitry/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
