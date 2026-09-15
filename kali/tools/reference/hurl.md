# hurl

> Hexadecimal & URL encoder + decoder This package contains a hexadecimal & URL (en/de)coder.

> **功能分类**：通用工具 ｜ **Kali 包**：`hurl` ｜ **官方文档**：<https://www.kali.org/tools/hurl/>

## 1. 安装

```bash
sudo apt update
sudo apt install hurl
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.1 |
| 架构 | all |
| 可执行命令 | `hurl` |
| 依赖 | `libcgi-pm-perl`、`perl` |
| 安装体积 | 187 KB |
| 官网 | <https://github.com/fnord0/hURL> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/hurl> |
| 包追踪 | <https://pkg.kali.org/pkg/hurl> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
hurl -h          # 查看用法
man hurl         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hURL`

官方给出的调用示例：`hURL -b "S2FsaSBMaW51eAo="`

```text
root@kali:~# hURL -b "S2FsaSBMaW51eAo="
Original string       :: S2FsaSBMaW51eAo=
base64 DEcoded string :: Kali Linux
```

### `hURL（示例）`

官方给出的调用示例：`hURL -h`

```text
root@kali:~# hURL -h
.::[ hURL - hexadecimal & URL (en/de)coder ]::.
v2.1 @COPYLEFT  ->  fnord0 <at> riseup <dot> net
  USAGE: /usr/bin/hURL [ -flag|--flag ] [ -f <file1>,<file2> ] [ string ]
  COMMAND LINE ARGUMENTS
   -M|--menu	=> Menu-driven GUI		 ;  /usr/bin/hURL -M
   -U|--URL	=> URL encode			 ;  /usr/bin/hURL -U "hello world"
   -u|--url	=> uRL decode			 ;  /usr/bin/hURL -u "hello%20world"
   -D|--DURL	=> Double URL encode		 ;  /usr/bin/hURL -D "hello world"
   -d|--durl	=> double URL decode		 ;  /usr/bin/hURL -d "hello%2520world"
   -B|--BASE64	=> Base64 encode		 ;  /usr/bin/hURL -B "hello world"
   -b|--base64	=> base64 decode		 ;  /usr/bin/hURL -b "aGVsbG8gd29ybGQ="
   -H|--HTML	=> HTML encode			 ;  /usr/bin/hURL -H "<hello world>"
   -h|--html	=> hTML decode			 ;  /usr/bin/hURL -h "&lt;hello world&gt;"
   -X|--HEX	=> ascii ->  heX		 ;  /usr/bin/hURL -X "hello world"
	--esc   :: output in escaped string	    ; "\x00\x01\x02\x03 ..."
	--pair  :: output in hexpair format	    ; 00010203 ...
   -x|--hex	=> hex   ->  ascii		 ;  /usr/bin/hURL -x "68656c6c6f20776f726c64"
   -I|--INT	=> Int   ->  hex		 ;  /usr/bin/hURL -I "10"
   -i|--int	=> hex   ->  int		 ;  /usr/bin/hURL -i "0xa"
   -n|--nint	=> -int  ->  hex		 ;  /usr/bin/hURL -n -- -77
   -N|--NHEX	=> -hex  ->  iNt		 ;  /usr/bin/hURL -N 0xffffffb3
   -T|--INTB	=> inT   ->  bin		 ;  /usr/bin/hURL -T 30
   -t|--bint	=> bin   ->  int		 ;  /usr/bin/hURL -t 1010
   -F|--FLOATH	=> Float ->  hex		 ;  /usr/bin/hURL -F 3.33
   -l|--hfloat	=> hex   ->  float		 ;  /usr/bin/hURL -l 0x40551ed8
   -o|--octh	=> octal ->  hex		 ;  /usr/bin/hURL -o 35
   -O|--HOCT	=> hex   ->  Octal		 ;  /usr/bin/hURL -O 0x12
   -0|--binh	=> bin   ->  hex		 ;  /usr/bin/hURL -0 1100011
   -1|--hexb	=> hex   ->  bin		 ;  /usr/bin/hURL -1 0x63
   -2|--SHA1	=> SHA1 checksum		 ;  /usr/bin/hURL -2 "hello world"
   -3|--SHA224	=> SHA224 checksum		 ;  /usr/bin/hURL -3 "hello world"
   -4|--SHA256	=> SHA256 checksum		 ;  /usr/bin/hURL -4 "hello world"
   -5|--SHA384	=> SHA384 checksum		 ;  /usr/bin/hURL -5 "hello world"
   -6|--SHA512	=> SHA512 checksum		 ;  /usr/bin/hURL -6 "hello world"
   -7|--ROT13	=> ROT13 encode			 ;  /usr/bin/hURL -7 "hello world"
   -8|--rot13	=> ROT13 decode			 ;  /usr/bin/hURL -8 "uryyb jbeyq"
   -9|--stack	=> push string 2 stack (corelan) ;  /usr/bin/hURL -9 "hello world"
	--esc   :: output in escaped string	    ; "\x00\x01\x02\x03 ..."
	--pair  :: output in hexpair format	    ; 00010203 ...
	--ansiC :: output in C format		    ; 0x00, 0x01, 0x02, 0x03 ...
   -m|--md5	=> md5 digest			 ;  /usr/bin/hURL -m "hello world"
   -e|--net	=> int -> hex (net-byte order)   ;  /usr/bin/hURL -e 4444
   -E|--NET	=> hex (nEt-byte order) ->  int  ;  /usr/bin/hURL -E 5c11
   -w|--wbin	=> hex [file] -> binary [file]	 ;  /usr/bin/hURL -w -f <INfile> <OUTfile>
   -r|--rbin	=> binary [file] -> hex (corelan);  /usr/bin/hURL -r -f /tmp/msgbox.bin
	--esc   :: output in escaped string	    ; "\x00\x01\x02\x03 ..."
	--pair  :: output in hexpair format	    ; 00010203 ...
	--ansiC :: output in C format		    ; 0x00, 0x01, 0x02, 0x03 ...
   --color|--nocolor	=> enable/disable colored output [default is ENABLED]
   --corelan		=> display corelan reference
   --help		=> displays help
   --man		=> displays extended help with examples
   --version		=> displays version information
   -s				=> suppress (display result only)
   -f|--file <file1>,<file2>	=> use file(s) as input
   [string]			=> string as input
Updated on: 2025-Dec-09
 Edit this page
httprobe
hyperion
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install hurl`，再执行 `hurl --version` 2>/dev/null || `hurl -V`
- [ ] **2.** **读官方帮助** —— `hurl -h`，需要细节时 `man hurl`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `hurl -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hurl/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hurl/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hurl/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
