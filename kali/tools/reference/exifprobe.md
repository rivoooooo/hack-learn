# exifprobe

> Read metadata from digital pictures Exifprobe reads image files produced by digital cameras (including several so-called “raw” file formats) and reports the structure of the files and the auxiliary data and metadata contained within them. …

> **功能分类**：数字取证 ｜ **Kali 包**：`exifprobe` ｜ **官方文档**：<https://www.kali.org/tools/exifprobe/>

## 1. 安装

```bash
sudo apt update
sudo apt install exifprobe
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.0.1 |
| 架构 | any |
| 可执行命令 | `exifprobe`、`exifgrep` |
| 依赖 | `libc6`、`exifgrep` |
| 安装体积 | 506 KB |
| 官网 | <https://github.com/hfiguiere/exifprobe> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/exifprobe> |
| 包追踪 | <https://pkg.kali.org/pkg/exifprobe> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
exifprobe -h          # 查看用法
man exifprobe         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `exifgrep`

官方给出的调用示例：`exifgrep -h`

```text
root@kali:~# exifgrep -h
Usage: exifgrep [-var|-export] [-num] [-r] [-t] [-n] [-c] [egrep-options] egrep-pattern [NOT egrep-pattern] imagefilename[s]
```

### `exifprobe`

官方给出的调用示例：`exifprobe -h`

```text
root@kali:~# exifprobe -h
Usage:
exifprobe [options] filenames(s)
	-h - print this help message
	-V - print program version and copyright
	-R - Report mode: only tagnames and decimal values, indented, inline
	-S - Structure mode: everything, offset values not inline (default)
	-L - List mode: list all tags and values (only); no structure
	-Z - Zero (turn off) all output flags
	-a - toggle print addresses in hex and decimal
	-D - toggle print enabled addresses, tag numbers and values in decimal only
	-X - toggle print enabled addresses, tag numbers and values in hex only
	-I - toggle indent (after address -> before -> none)
	-i - toggle "inline" print of IFD values
	-n - toggle printing of filename at start of each output line
	-c - toggle use of color to highlight certain sections
	-u - print all 16 bits of unicode data
	-p[items] - toggle print identifiers for:
		s - sections
		g - segments
		e - IFD entries
		a - expand known entries in APP0...APPN segents
		m - print MakerNote scheme detection info
		M - debug MakerNote scheme detection info
		l - long tagnames (default in List mode)
	-e[items] - toggle print IFD entry items:
		t - tagname
		n - tag number in decimal
		N - tag number in hex
		T - entry type
		v - value in decimal
		V - value in hex
		o - file offset to value in decimal
		O - file offset to value in hex
		r - relative (unadjusted) offset in decimal
		R - print "raw" values where expansion of values is needed
		a - print ascii strings until null, rather than by length
		A - print ALL elements of multiple-value tags
	-M[len|a] - hex/ascii dump 'len' (or all) bytes of unknown MakerNotes
	-A[len|a] - hex/ascii dump 'len' (or all) bytes of unknown APPn segments
	-U[len|a] - hex/ascii dump 'len' (or all) bytes of UNDEFINED data of unknown format
	-B[len|a] - hex/ascii dump 'len' (or all) bytes of binary images or invalid JPEG data
	-N[num]   - force noteversion 'num' for MakerNote interpretation
	-m[name]  - force use of maker 'name' to select MakerNote interpretation routines
	-l[model] - force use of 'model' to select MakerNote interpretation routines
	-O[offset]       - start processing at 'offset' in file
	-C[make]+[model] - print makes matching 'make', models matching 'model' (substrings)
	Program: 'exifprobe' version 2.1.0
	Compiled: no date
	Copyright (C) 2005 Duane H. Hesser, (C) 2011-2015 Hubert Figuiere
		(open source; see LICENSE.EXIFPROBE)
Updated on: 2026-Jun-17
 Edit this page
dislocker
ferret-sidejack
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install exifprobe`，再执行 `exifprobe --version` 2>/dev/null || `exifprobe -V`
- [ ] **2.** **读官方帮助** —— `exifprobe -h`，需要细节时 `man exifprobe`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: exifgrep [-var|-export] [-num] [-r] [-t] [-n] [-c] [egrep-options] egrep-pattern [NOT egrep-pattern] imagefilename[s]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/exifprobe/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/exifprobe/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/exifprobe/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
