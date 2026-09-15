# hashdeep

> Recursively compute hashsums or piecewise hashings hashdeep is a set of tools to compute MD5, SHA1, SHA256, tiger and whirlpool hashsums of arbitrary number of files recursively. The main hashdeep features are: It can compare those hashsum…

> **功能分类**：数字取证 ｜ **Kali 包**：`hashdeep` ｜ **官方文档**：<https://www.kali.org/tools/hashdeep/>

## 1. 安装

```bash
sudo apt update
sudo apt install hashdeep
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.4 |
| 架构 | any |
| 可执行命令 | `hashdeep`、`md5deep`、`sha1deep`、`sha256deep`、`tigerdeep`、`whirlpooldeep` |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6` |
| 安装体积 | 1.57 MB |
| 官网 | <https://md5deep.sourceforge.net> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/hashdeep> |
| 包追踪 | <https://pkg.kali.org/pkg/hashdeep> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
hashdeep -h          # 查看用法
man hashdeep         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 6 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hashdeep`

官方给出的调用示例：`hashdeep -h`

```text
root@kali:~# hashdeep -h
hashdeep version 4.4 by Jesse Kornblum and Simson Garfinkel.
$ hashdeep [OPTION]... [FILES]...
-c <alg1,[alg2]> - Compute hashes only. Defaults are MD5 and SHA-256
                   legal values: md5,sha1,sha256,tiger,whirlpool,
-p <size> - piecewise mode. Files are broken into blocks for hashing
-r        - recursive mode. All subdirectories are traversed
-d        - output in DFXML (Digital Forensics XML)
-k <file> - add a file of known hashes
-a        - audit mode. Validates FILES against known hashes. Requires -k
-m        - matching mode. Requires -k
-x        - negative matching mode. Requires -k
-w        - in -m mode, displays which known file was matched
-M and -X act like -m and -x, but display hashes of matching files
-e        - compute estimated time remaining for each file
-s        - silent mode. Suppress all error messages
-b        - prints only the bare name of files; all path information is omitted
-l        - print relative paths for filenames
-i/-I     - only process files smaller than the given threshold
-o        - only process certain types of files. See README/manpage
-v        - verbose mode. Use again to be more verbose
-d        - output in DFXML; -W FILE - write to FILE.
-j <num>  - use num threads (default 6)
```

### `md5deep`

官方给出的调用示例：`md5deep -h`

```text
root@kali:~# md5deep -h
md5deep version 4.4 by Jesse Kornblum and Simson Garfinkel.
$ md5deep [OPTION]... [FILES]...
See the man page or README.txt file or use -hh for the full list of options
-p <size> - piecewise mode. Files are broken into blocks for hashing
-r        - recursive mode. All subdirectories are traversed
-e        - show estimated time remaining for each file
-s        - silent mode. Suppress all error messages
-z        - display file size before hash
-m <file> - enables matching mode. See README/man page
-x <file> - enables negative matching mode. See README/man page
-M and -X are the same as -m and -x but also print hashes of each file
-w        - displays which known file generated a match
-n        - displays known hashes that did not match any input files
-a and -A add a single hash to the positive or negative matching set
-b        - prints only the bare name of files; all path information is omitted
-l        - print relative paths for filenames
-t        - print GMT timestamp (ctime)
-i/I <size> - only process files smaller/larger than SIZE
-v        - display version number and exit
-d        - output in DFXML; -u - Escape Unicode; -W FILE - write to FILE.
-j <num>  - use num threads (default 6)
-Z - triage mode;   -h - help;   -hh - full help
```

### `sha1deep`

官方给出的调用示例：`sha1deep -h`

```text
root@kali:~# sha1deep -h
sha1deep version 4.4 by Jesse Kornblum and Simson Garfinkel.
$ sha1deep [OPTION]... [FILES]...
See the man page or README.txt file or use -hh for the full list of options
-p <size> - piecewise mode. Files are broken into blocks for hashing
-r        - recursive mode. All subdirectories are traversed
-e        - show estimated time remaining for each file
-s        - silent mode. Suppress all error messages
-z        - display file size before hash
-m <file> - enables matching mode. See README/man page
-x <file> - enables negative matching mode. See README/man page
-M and -X are the same as -m and -x but also print hashes of each file
-w        - displays which known file generated a match
-n        - displays known hashes that did not match any input files
-a and -A add a single hash to the positive or negative matching set
-b        - prints only the bare name of files; all path information is omitted
-l        - print relative paths for filenames
-t        - print GMT timestamp (ctime)
-i/I <size> - only process files smaller/larger than SIZE
-v        - display version number and exit
-d        - output in DFXML; -u - Escape Unicode; -W FILE - write to FILE.
-j <num>  - use num threads (default 6)
-Z - triage mode;   -h - help;   -hh - full help
```

### `sha256deep`

官方给出的调用示例：`sha256deep -h`

```text
root@kali:~# sha256deep -h
sha256deep version 4.4 by Jesse Kornblum and Simson Garfinkel.
$ sha256deep [OPTION]... [FILES]...
See the man page or README.txt file or use -hh for the full list of options
-p <size> - piecewise mode. Files are broken into blocks for hashing
-r        - recursive mode. All subdirectories are traversed
-e        - show estimated time remaining for each file
-s        - silent mode. Suppress all error messages
-z        - display file size before hash
-m <file> - enables matching mode. See README/man page
-x <file> - enables negative matching mode. See README/man page
-M and -X are the same as -m and -x but also print hashes of each file
-w        - displays which known file generated a match
-n        - displays known hashes that did not match any input files
-a and -A add a single hash to the positive or negative matching set
-b        - prints only the bare name of files; all path information is omitted
-l        - print relative paths for filenames
-t        - print GMT timestamp (ctime)
-i/I <size> - only process files smaller/larger than SIZE
-v        - display version number and exit
-d        - output in DFXML; -u - Escape Unicode; -W FILE - write to FILE.
-j <num>  - use num threads (default 6)
-Z - triage mode;   -h - help;   -hh - full help
```

### `tigerdeep`

官方给出的调用示例：`tigerdeep -h`

```text
root@kali:~# tigerdeep -h
tigerdeep version 4.4 by Jesse Kornblum and Simson Garfinkel.
$ tigerdeep [OPTION]... [FILES]...
See the man page or README.txt file or use -hh for the full list of options
-p <size> - piecewise mode. Files are broken into blocks for hashing
-r        - recursive mode. All subdirectories are traversed
-e        - show estimated time remaining for each file
-s        - silent mode. Suppress all error messages
-z        - display file size before hash
-m <file> - enables matching mode. See README/man page
-x <file> - enables negative matching mode. See README/man page
-M and -X are the same as -m and -x but also print hashes of each file
-w        - displays which known file generated a match
-n        - displays known hashes that did not match any input files
-a and -A add a single hash to the positive or negative matching set
-b        - prints only the bare name of files; all path information is omitted
-l        - print relative paths for filenames
-t        - print GMT timestamp (ctime)
-i/I <size> - only process files smaller/larger than SIZE
-v        - display version number and exit
-d        - output in DFXML; -u - Escape Unicode; -W FILE - write to FILE.
-j <num>  - use num threads (default 6)
-Z - triage mode;   -h - help;   -hh - full help
```

### `whirlpooldeep`

官方给出的调用示例：`whirlpooldeep -h`

```text
root@kali:~# whirlpooldeep -h
whirlpooldeep version 4.4 by Jesse Kornblum and Simson Garfinkel.
$ whirlpooldeep [OPTION]... [FILES]...
See the man page or README.txt file or use -hh for the full list of options
-p <size> - piecewise mode. Files are broken into blocks for hashing
-r        - recursive mode. All subdirectories are traversed
-e        - show estimated time remaining for each file
-s        - silent mode. Suppress all error messages
-z        - display file size before hash
-m <file> - enables matching mode. See README/man page
-x <file> - enables negative matching mode. See README/man page
-M and -X are the same as -m and -x but also print hashes of each file
-w        - displays which known file generated a match
-n        - displays known hashes that did not match any input files
-a and -A add a single hash to the positive or negative matching set
-b        - prints only the bare name of files; all path information is omitted
-l        - print relative paths for filenames
-t        - print GMT timestamp (ctime)
-i/I <size> - only process files smaller/larger than SIZE
-v        - display version number and exit
-d        - output in DFXML; -u - Escape Unicode; -W FILE - write to FILE.
-j <num>  - use num threads (default 6)
-Z - triage mode;   -h - help;   -hh - full help
Updated on: 2025-Dec-09
 Edit this page
hash-identifier
hashid
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install hashdeep`，再执行 `hashdeep --version` 2>/dev/null || `hashdeep -V`
- [ ] **2.** **读官方帮助** —— `hashdeep -h`，需要细节时 `man hashdeep`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `hashdeep -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hashdeep/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[tiger](../../tools/tutorials/02-漏洞分析/tiger.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hashdeep/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hashdeep/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
