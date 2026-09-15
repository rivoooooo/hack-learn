# dnsenum

> Tool to enumerate domain DNS information Dnsenum is a multithreaded perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks. The main purpose of Dnsenum is to gather as much information as possible abo…

> **功能分类**：信息搜集 ｜ **Kali 包**：`dnsenum` ｜ **官方文档**：<https://www.kali.org/tools/dnsenum/>

## 1. 安装

```bash
sudo apt update
sudo apt install dnsenum
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3.2 |
| 架构 | all |
| 可执行命令 | `dnsenum` |
| 依赖 | `libhtml-parser-perl`、`libnet-dns-perl`、`libnet-ip-perl`、`libnet-netmask-perl`、`libnet-whois-ip-perl`、`libstring-random-perl`、`libwww-mechanize-perl`、`libxml-writer-perl`、`perl` |
| 安装体积 | 87 KB |
| 官网 | <https://github.com/SparrowOchon/dnsenum2> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/dnsenum> |
| 包追踪 | <https://pkg.kali.org/pkg/dnsenum> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Don’t do a reverse lookup (–noreverse) and save the output to a file (-o mydomain.xml) for the domain example.com:
root@kali:~# dnsenum --noreverse -o mydomain.xml example.com
dnsenum VERSION:1.2.4

-----   example.com   -----


Host's addresses:
__________________

example.com.                             392      IN    A        93.184.216.119


Name Servers:
______________

b.iana-servers.net.                      122      IN    A        199.43.133.53
a.iana-servers.net.                      122      IN    A        199.43.132.53


Mail (MX) Servers:
___________________
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dnsenum`

官方给出的调用示例：`dnsenum --noreverse -o mydomain.xml example.com`

```text
root@kali:~# dnsenum --noreverse -o mydomain.xml example.com
dnsenum VERSION:1.2.4
-----   example.com   -----
Host's addresses:
__________________
example.com.                             392      IN    A        93.184.216.119
Name Servers:
______________
b.iana-servers.net.                      122      IN    A        199.43.133.53
a.iana-servers.net.                      122      IN    A        199.43.132.53
Mail (MX) Servers:
___________________
```

### `dnsenum（示例）`

官方给出的调用示例：`dnsenum -h`

```text
root@kali:~# dnsenum -h
dnsenum VERSION:1.3.1
Usage: dnsenum [Options] <domain>
[Options]:
Note: If no -f tag supplied will default to /usr/share/dnsenum/dns.txt or
the dns.txt file in the same directory as dnsenum
GENERAL OPTIONS:
  --dnsserver 	<server>
			Use this DNS server for A, NS and MX queries.
  --enum		Shortcut option equivalent to --threads 5 -s 15 -w.
  -h, --help		Print this help message.
  --noreverse		Skip the reverse lookup operations.
  --nocolor		Disable ANSIColor output.
  --private		Show and save private ips at the end of the file domain_ips.txt.
  --subfile <file>	Write all valid subdomains to this file.
  -t, --timeout <value>	The tcp and udp timeout values in seconds (default: 10s).
  --threads <value>	The number of threads that will perform different queries.
  -v, --verbose		Be verbose: show all the progress and all the error messages.
GOOGLE SCRAPING OPTIONS:
  -p, --pages <value>	The number of google search pages to process when scraping names,
			the default is 5 pages, the -s switch must be specified.
  -s, --scrap <value>	The maximum number of subdomains that will be scraped from Google (default 15).
BRUTE FORCE OPTIONS:
  -f, --file <file>	Read subdomains from this file to perform brute force. (Takes priority over default dns.txt)
  -u, --update	<a|g|r|z>
			Update the file specified with the -f switch with valid subdomains.
	a (all)		Update using all results.
	g		Update using only google scraping results.
	r		Update using only reverse lookup results.
	z		Update using only zonetransfer results.
  -r, --recursion	Recursion on subdomains, brute force all discovered subdomains that have an NS record.
WHOIS NETRANGE OPTIONS:
  -d, --delay <value>	The maximum value of seconds to wait between whois queries, the value is defined randomly, default: 3s.
  -w, --whois		Perform the whois queries on c class network ranges.
			 **Warning**: this can generate very large netranges and it will take lot of time to perform reverse lookups.
REVERSE LOOKUP OPTIONS:
  -e, --exclude	<regexp>
			Exclude PTR records that match the regexp expression from reverse lookup results, useful on invalid hostnames.
OUTPUT OPTIONS:
  -o --output <file>	Output in XML format. Can be imported in MagicTree (www.gremwell.com)
Learn more with
OffSec
Want to learn more about dnsenum? get access to in-depth training and hands-on labs:
PEN-200: 6.4.1. Information Gathering: DNS Enumeration
PEN-200: 25.2.2. Enumerating AWS Cloud Infrastructure: Domain and Subdomain Reconnaissance
PEN-200 course
Updated on: 2025-Dec-09
 Edit this page
dnschef
dnsgen
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dnsenum`，再执行 `dnsenum --version` 2>/dev/null || `dnsenum -V`
- [ ] **2.** **读官方帮助** —— `dnsenum -h`，需要细节时 `man dnsenum`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: dnsenum [Options] <domain>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dnsenum/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[dnsenum](../../tools/tutorials/01-信息搜集/dnsenum.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dnsenum/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dnsenum/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
