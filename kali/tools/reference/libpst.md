# libpst

> Library for reading Microsoft Outlook PST files (development files) Library for accessing data from Microsoft Outlook PST files. This package include the files needed for developing with libpst, including the headers, static library and do…

> **功能分类**：数字取证 ｜ **Kali 包**：`libpst` ｜ **官方文档**：<https://www.kali.org/tools/libpst/>

## 1. 安装

```bash
sudo apt update
sudo apt install libpst-dev
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.6.76 |
| 架构 | any |
| 可执行命令 | `libpst-dev`、`libpst4t64`、`pst-utils`、`lspst`、`nick2ldif`、`pst2dii`、`pst2ldif`、`readpst` |
| 依赖 | `libpst4t64`、`libpst4t64` |
| 安装体积 | 2.58 MB |
| 官网 | <https://www.five-ten-sg.com/libpst/> |
| 源码仓库 | <https://salsa.debian.org/debian/libpst> |
| 包追踪 | <https://pkg.kali.org/pkg/libpst> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libpst-dev -h          # 查看用法
man libpst-dev         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 8 个可执行命令，下面是官方页面内嵌的帮助原文。

### `lspst`

官方给出的调用示例：`lspst -h`

```text
root@kali:~# lspst -h
lspst / LibPST v0.6.76
Little Endian implementation being used.
Usage: lspst [OPTIONS] {PST FILENAME}
OPTIONS:
	-d <filename> 	- Debug to file. This is a binary log. Use readlog to print it
	-l	- Print the date, CC and BCC fields of emails too (by default only the From and Subject)
	-f <date_format> 	- Select the date format in ctime format (by default "%F %T")
	-h	- Help. This screen
	-V	- Version. Display program version
```

### `pst2dii`

官方给出的调用示例：`pst2dii -h`

```text
root@kali:~# pst2dii -h
pst2dii v0.6.76
Little Endian implementation being used.
Usage: pst2dii -f ttf-font-file [OPTIONS] {PST FILENAME}
	-f ttf-font-file  	- Set the font file
OPTIONS:
	-B bates-prefix   	- Set the bates prefix string
	-O dii-output-file	- Set the dii load file output filename
	-V                	- Version. Display program version
	-b bates-number   	- Set the starting bates sequence number
	-c bates-color    	- Specify the color of the bates stamps as 6 digit hex
	-d filename       	- Debug to file.
	-h                	- Help. This screen
	-o dirname        	- Output directory to write files to.
```

### `pst2ldif`

官方给出的调用示例：`pst2ldif -h`

```text
root@kali:~# pst2ldif -h
pst2ldif v0.6.76
Little Endian implementation being used.
Usage: pst2ldif [OPTIONS] {PST FILENAME}
OPTIONS:
	-V	- Version. Display program version
	-b ldapbase	- set the LDAP base value
	-c class	- set the class of the LDAP objects (may contain more than one)
	-d <filename>	- Debug to file.
	-h	- Help. This screen
	-l line	- extra line to insert in the LDIF file for each contact
	-o	- use old schema, default is new schema
```

### `readpst`

官方给出的调用示例：`readpst -h`

```text
root@kali:~# readpst -h
ReadPST / LibPST v0.6.76
Little Endian implementation being used.
Usage: readpst [OPTIONS] {PST FILENAME}
OPTIONS:
	-V	- Version. Display program version
	-C charset	- character set for items with an unspecified character set
	-D	- Include deleted items in output
	-L <level> 	- Set debug level; 1=debug,2=info,3=warn.
	-M	- Write emails in the MH (rfc822) format
	-S	- Separate. Write emails in the separate format
	-a <attachment-extension-list>	- Discard any attachment without an extension on the list
	-b	- Don't save RTF-Body attachments
	-c[v|l]	- Set the Contact output mode. -cv = VCard, -cl = EMail list
	-d <filename> 	- Debug to file.
	-e	- As with -M, but include extensions on output files
	-h	- Help. This screen
	-j <integer>	- Number of parallel jobs to run
	-k	- KMail. Output in kmail format
	-m	- As with -e, but write .msg files also
	-o <dirname>	- Output directory to write files to. CWD is changed *after* opening pst file
	-q	- Quiet. Only print error messages
	-r	- Recursive. Output in a recursive format
	-t[eajc]	- Set the output type list. e = email, a = attachment, j = journal, c = contact
	-u	- Thunderbird mode. Write two extra .size and .type files
	-w	- Overwrite any output mbox files
	-8	- Output bodies in UTF-8, rather than original encoding, if UTF-8 version is available
Only one of -M -S -e -k -m -r should be specified
Updated on: 2025-Dec-09
 Edit this page
libfindrtp
libsmali-java
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install libpst-dev`，再执行 `libpst-dev --version` 2>/dev/null || `libpst-dev -V`
- [ ] **2.** **读官方帮助** —— `libpst-dev -h`，需要细节时 `man libpst-dev`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: lspst [OPTIONS] {PST FILENAME}`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/libpst/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/libpst/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/libpst/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
