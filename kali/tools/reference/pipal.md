# pipal

> Statistical analysis on password dumps All this tool does is to give you the stats and the information to help you analyse the passwords. The real work is done by you in interpreting the results.

> **功能分类**：口令攻击 ｜ **Kali 包**：`pipal` ｜ **官方文档**：<https://www.kali.org/tools/pipal/>

## 1. 安装

```bash
sudo apt update
sudo apt install pipal
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.4.0 |
| 架构 | all |
| 可执行命令 | `pipal` |
| 依赖 | `ruby`、`ruby-json`、`ruby-levenshtein` |
| 安装体积 | 243 KB |
| 官网 | <https://www.digininja.org/projects/pipal.php> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/pipal> |
| 包追踪 | <https://pkg.kali.org/pkg/pipal> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Analyze and display the top 5 passwords (-t 5), using the given file as input (/usr/share/wordlists/nmap.lst):
root@kali:~# pipal -t 5 /usr/share/wordlists/nmap.lst
Generating stats, hit CTRL-C to finish early and dump stats on words already processed.
Please wait...
Processing:    100% |ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo| Time: 00:00:04


Total entries = 5085
Total unique entries = 5076

Top 5 passwords
#!comment:  *                                                                         * = 10 (0.2%)
cabrera = 1 (0.02%)
#!comment:  * The Nmap Security Scanner is (C) 1996-2010 Insecure.Com LLC. Nmap is    * = 1 (0.02%)
#!comment:  * also a registered trademark of Insecure.Com LLC.  This program is free  * = 1 (0.02%)
#!comment:  * software; you may redistribute and/or modify it under the terms of the  * = 1 (0.02%)

Top 5 base words
love = 26 (0.51%)
angel = 22 (0.43%)
password = 18 (0.35%)
soccer = 18 (0.35%)
princess = 13 (0.26%)

Password length (length ordered)
3 = 1 (0.02%)
4 = 11 (0.22%)
5 = 434 (8.53%)
6 = 1863 (36.64%)
7 = 1219 (23.97%)
8 = 865 (17.01%)
9 = 387 (7.61%)
10 = 156 (3.07%)
11 = 41 (0.81%)
12 = 13 (0.26%)
13 = 7 (0.14%)
14 = 1 (0.02%)
15 = 1 (0.02%)
16 = 1 (0.02%)
17 = 1 (0.02%)
87 = 83 (1.63%)
88 = 1 (0.02%)
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pipal`

> 官方示例调用：`pipal -t 5 /usr/share/wordlists/nmap.lst`

```text
root@kali:~# pipal -t 5 /usr/share/wordlists/nmap.lst
Generating stats, hit CTRL-C to finish early and dump stats on words already processed.
Please wait...
Processing:    100% |ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo| Time: 00:00:04
Total entries = 5085
Total unique entries = 5076
Top 5 passwords
#!comment:  *                                                                         * = 10 (0.2%)
cabrera = 1 (0.02%)
#!comment:  * The Nmap Security Scanner is (C) 1996-2010 Insecure.Com LLC. Nmap is    * = 1 (0.02%)
#!comment:  * also a registered trademark of Insecure.Com LLC.  This program is free  * = 1 (0.02%)
#!comment:  * software; you may redistribute and/or modify it under the terms of the  * = 1 (0.02%)
Top 5 base words
love = 26 (0.51%)
angel = 22 (0.43%)
password = 18 (0.35%)
soccer = 18 (0.35%)
princess = 13 (0.26%)
Password length (length ordered)
3 = 1 (0.02%)
4 = 11 (0.22%)
5 = 434 (8.53%)
6 = 1863 (36.64%)
7 = 1219 (23.97%)
8 = 865 (17.01%)
9 = 387 (7.61%)
10 = 156 (3.07%)
11 = 41 (0.81%)
12 = 13 (0.26%)
13 = 7 (0.14%)
14 = 1 (0.02%)
15 = 1 (0.02%)
16 = 1 (0.02%)
17 = 1 (0.02%)
87 = 83 (1.63%)
88 = 1 (0.02%)
```

### `pipal -h`

> 官方示例调用：`pipal -h`

```text
root@kali:~# pipal -h
pipal 3.4.0 Robin Wood (
[email protected]
) (http://digi.ninja)
Usage: pipal [OPTION] ... FILENAME
	--help, -h, -?: show help
	--top, -t X: show the top X results (default 10)
	--output, -o <filename>: output to file
	--gkey <Google Maps API key>: to allow zip code lookups (optional)
	--list-checkers: Show the available checkers and which are enabled
	--verbose, -v: Verbose
	FILENAME: The file to count
Updated on: 2025-Dec-09
 Edit this page
phpsploit
pixiewps
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install pipal`，再执行 `pipal --version` 2>/dev/null || `pipal -V`
- [ ] **2.** **读官方帮助** —— `pipal -h`，需要细节时 `man pipal`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: pipal [OPTION] ... FILENAME`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/pipal/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/pipal/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/pipal/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
