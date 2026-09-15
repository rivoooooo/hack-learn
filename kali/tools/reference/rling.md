# rling

> Better rli This package is similar to the rli utility found in hashcat-utils, but much, much faster. rli compares a single file against another file(s) and removes all duplicates.

> **功能分类**：通用工具 ｜ **Kali 包**：`rling` ｜ **官方文档**：<https://www.kali.org/tools/rling/>

## 1. 安装

```bash
sudo apt update
sudo apt install rling
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.84 |
| 架构 | any |
| 可执行命令 | `rling`、`dedupe`、`getpass`、`rehex`、`splitlen` |
| 依赖 | `libc6`、`libjudydebian1`、`zlib1g`、`dedupe`、`getpass` |
| 安装体积 | 166 KB |
| 官网 | <https://github.com/Cynosureprime/rling> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/rling> |
| 包追踪 | <https://pkg.kali.org/pkg/rling> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
rling -h          # 查看用法
man rling         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 5 个可执行命令，下面是官方页面内嵌的帮助原文。

### `getpass`

官方给出的调用示例：`getpass -h`

```text
root@kali:~# getpass -h
getpass Version 1.10 2023/09/02 05:27:23 dlr Exp dlr $
extract passwords from result files
	-c [colspec]	Set extraction to N-, N-M, or -M like cut
	-d [val]	Set delimiter to character, decimal value, or 0x-style hex value
	-f [field]	Set extraction to field number. Starts at 1
	-n		Disable extension exclusion entirely (equivalent to -x /dev/null)
	-t		Disable extension expansion (file.txt -> file.txt.[hashtype], etc.)
	-x [file]	Read excluded extension list from file, replacing default
	-h		This help
	-S exp		Sets $HEX[] conversion for char or range
	-U exp		Resets $HEX[] conversion for char or range
			Specify a character like a,b,c, or a range like a-f,
			0x61-0x66 or as decimal values line 0-32.
Default excluded extensions:
	.txt .orig .test .csalt.txt .fixme .new
```

### `rling`

官方给出的调用示例：`rling --help`

```text
root@kali:~# rling --help
rling: unrecognized option '--help'
rling version: 1.84 2026/07/03 05:52:30 dlr Exp dlr $
rling - remove matching lines from a file
rling input output [remfil1 remfile2 ...]
	-i		Ignore any error/missing files on remove list
	-d		Removes duplicate lines from input (on by default)
	-D file		Write duplicates to file
	-n		Do not remove duplicate lines from input
	-c		Output lines common to input and remove files
	-s		Sort output. Default is input order.
			This will make the -b and -f options substantially faster
	-t number	Number of threads to use
	-p prime	Force size of hash table
	-b		Use binary search vs hash (slower, but less memory)
	-2		Use rli2 mode - all files must be sorted. Low mem usage.
	-f		Use files instead of memory (slower, but small memory)
	-l [len]		Limit all matching to a specific length.
	-M memsize	Maximum memory to use for -f mode
	-T path		Directory to store temp files in
	-q [cahwl]	Do frequency analysis on input
			a - all output, c - count, l - length, w - word,
			s - running statistics, h - append histogram
			Additional files will be matched against input files
	-h		This help
	stdin and stdout can be used in the place of any filename
Total runtime 0.0002 seconds
```

### `splitlen`

官方给出的调用示例：`splitlen -h`

```text
root@kali:~# splitlen -h
splitlen Version 1.10 2020/09/01 21:51:47 dlr Exp dlr $
splitlen -o filename file [..file]
	-u		Remove $HEX[] encoding from input
	-o filename	Output to filename, modified with lengths
			The char # will be replaced with _length in filename
			If no # is in filename, _len will len appended to name
	-c char		Use char as place to insert number in -o file
	-s		Sorts by length into a single output file.
	-M size		Sets the final buffer size for -s option
	-S exp		Sets $HEX[] conversion for char or range
	-U exp		Resets $HEX[] conversion for char or range
			Specify a character like a,b,c, or a range like a-f,
			0x61-0x66 or as decimal values line 0-32.
Updated on: 2026-Aug-25
 Edit this page
rizin-cutter
rz-ghidra
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install rling`，再执行 `rling --version` 2>/dev/null || `rling -V`
- [ ] **2.** **读官方帮助** —— `rling -h`，需要细节时 `man rling`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `rling -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rling/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rling/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rling/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
