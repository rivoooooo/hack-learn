# dos2unix

> Convert text file line endings between CRLF and LF This package contains utilities dos2unix, unix2dos, mac2unix, unix2mac to convert the line endings of text files between UNIX (LF), DOS (CRLF) and Mac (CR) formats. Text files under Window…

> **功能分类**：通用工具 ｜ **Kali 包**：`dos2unix` ｜ **官方文档**：<https://www.kali.org/tools/dos2unix/>

## 1. 安装

```bash
sudo apt update
sudo apt install dos2unix
```

| 项目 | 内容 |
|------|------|
| 版本 | 7.5.4 |
| 架构 | any |
| 可执行命令 | `dos2unix`、`mac2unix`、`unix2dos`、`unix2mac` |
| 依赖 | `libc6` |
| 安装体积 | 1.54 MB |
| 官网 | <https://waterlan.home.xs4all.nl/dos2unix.html> |
| 源码仓库 | <https://salsa.debian.org/debian/dos2unix> |
| 包追踪 | <https://pkg.kali.org/pkg/dos2unix> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# unix2dos -n unix.txt dos.txt
unix2dos: converting file unix.txt to file dos.txt in DOS format ...

unix2mac Usage Example
root@kali:~# unix2mac -n unix.txt mac.txt
unix2mac: converting file unix.txt to file mac.txt in Mac format ...

dos2unix Usage Example
root@kali:~# dos2unix -n dos.txt unix2.txt
dos2unix: converting file dos.txt to file unix2.txt in Unix format ...

mac2unix Usage Example
root@kali:~# mac2unix -n mac.txt unix3.txt
mac2unix: converting file mac.txt to file unix3.txt in Unix format ...
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `unix2dos`

> 官方示例调用：`unix2dos -n unix.txt dos.txt`

```text
root@kali:~# unix2dos -n unix.txt dos.txt
unix2dos: converting file unix.txt to file dos.txt in DOS format ...
unix2mac Usage Example
```

### `unix2mac`

> 官方示例调用：`unix2mac -n unix.txt mac.txt`

```text
root@kali:~# unix2mac -n unix.txt mac.txt
unix2mac: converting file unix.txt to file mac.txt in Mac format ...
dos2unix Usage Example
```

### `dos2unix`

> 官方示例调用：`dos2unix -n dos.txt unix2.txt`

```text
root@kali:~# dos2unix -n dos.txt unix2.txt
dos2unix: converting file dos.txt to file unix2.txt in Unix format ...
mac2unix Usage Example
```

### `mac2unix`

> 官方示例调用：`mac2unix -n mac.txt unix3.txt`

```text
root@kali:~# mac2unix -n mac.txt unix3.txt
mac2unix: converting file mac.txt to file unix3.txt in Unix format ...
```

### `dos2unix -h`

> 官方示例调用：`dos2unix -h`

```text
root@kali:~# dos2unix -h
Usage: dos2unix [options] [file ...] [-n infile outfile ...]
 --allow-chown         allow file ownership change
 -ascii                default conversion mode
 -iso                  conversion between DOS and ISO-8859-1 character set
   -1252               use Windows code page 1252 (Western European)
   -437                use DOS code page 437 (US) (default)
   -850                use DOS code page 850 (Western European)
   -860                use DOS code page 860 (Portuguese)
   -863                use DOS code page 863 (French Canadian)
   -865                use DOS code page 865 (Nordic)
 -7                    convert 8 bit characters to 7 bit space
 -b, --keep-bom        keep Byte Order Mark
 -c, --convmode        conversion mode
   convmode            ascii, 7bit, iso, mac, default to ascii
 -e, --add-eol         add a line break to the last line if there isn't one
 -f, --force           force conversion of binary files
 -h, --help            display this help text
 -i, --info[=FLAGS]    display file information
   file ...            files to analyze
 -k, --keepdate        keep output file date
 -L, --license         display software license
 -l, --newline         add additional newline
 -m, --add-bom         add Byte Order Mark (default UTF-8)
 -n, --newfile         write to new file
   infile              original file in new-file mode
   outfile             output file in new-file mode
 --no-allow-chown      don't allow file ownership change (default)
 --no-add-eol          don't add a line break to the last line if there isn't one (default)
 -O, --to-stdout       write to standard output
 -o, --oldfile         write to old file (default)
   file ...            files to convert in old-file mode
 -q, --quiet           quiet mode, suppress all warnings
 -r, --remove-bom      remove Byte Order Mark (default)
 -s, --safe            skip binary files (default)
 -u,  --keep-utf16     keep UTF-16 encoding
 -ul, --assume-utf16le assume that the input format is UTF-16LE
 -ub, --assume-utf16be assume that the input format is UTF-16BE
 -v,  --verbose        verbose operation
 -F, --follow-symlink  follow symbolic links and convert the targets
 -R, --replace-symlink replace symbolic links with converted files
                         (original target files remain unchanged)
 -S, --skip-symlink    keep symbolic links and targets unchanged (default)
 -V, --version         display version number
```

### `mac2unix -h`

> 官方示例调用：`mac2unix -h`

```text
root@kali:~# mac2unix -h
Usage: mac2unix [options] [file ...] [-n infile outfile ...]
 --allow-chown         allow file ownership change
 -ascii                default conversion mode
 -iso                  conversion between DOS and ISO-8859-1 character set
   -1252               use Windows code page 1252 (Western European)
   -437                use DOS code page 437 (US) (default)
   -850                use DOS code page 850 (Western European)
   -860                use DOS code page 860 (Portuguese)
   -863                use DOS code page 863 (French Canadian)
   -865                use DOS code page 865 (Nordic)
 -7                    convert 8 bit characters to 7 bit space
 -b, --keep-bom        keep Byte Order Mark
 -c, --convmode        conversion mode
   convmode            ascii, 7bit, iso, mac, default to ascii
 -e, --add-eol         add a line break to the last line if there isn't one
 -f, --force           force conversion of binary files
 -h, --help            display this help text
 -i, --info[=FLAGS]    display file information
   file ...            files to analyze
 -k, --keepdate        keep output file date
 -L, --license         display software license
 -l, --newline         add additional newline
 -m, --add-bom         add Byte Order Mark (default UTF-8)
 -n, --newfile         write to new file
   infile              original file in new-file mode
   outfile             output file in new-file mode
 --no-allow-chown      don't allow file ownership change (default)
 --no-add-eol          don't add a line break to the last line if there isn't one (default)
 -O, --to-stdout       write to standard output
 -o, --oldfile         write to old file (default)
   file ...            files to convert in old-file mode
 -q, --quiet           quiet mode, suppress all warnings
 -r, --remove-bom      remove Byte Order Mark (default)
 -s, --safe            skip binary files (default)
 -u,  --keep-utf16     keep UTF-16 encoding
 -ul, --assume-utf16le assume that the input format is UTF-16LE
 -ub, --assume-utf16be assume that the input format is UTF-16BE
 -v,  --verbose        verbose operation
 -F, --follow-symlink  follow symbolic links and convert the targets
 -R, --replace-symlink replace symbolic links with converted files
                         (original target files remain unchanged)
 -S, --skip-symlink    keep symbolic links and targets unchanged (default)
 -V, --version         display version number
```

### `unix2dos -h`

> 官方示例调用：`unix2dos -h`

```text
root@kali:~# unix2dos -h
Usage: unix2dos [options] [file ...] [-n infile outfile ...]
 --allow-chown         allow file ownership change
 -ascii                default conversion mode
 -iso                  conversion between DOS and ISO-8859-1 character set
   -1252               use Windows code page 1252 (Western European)
   -437                use DOS code page 437 (US) (default)
   -850                use DOS code page 850 (Western European)
   -860                use DOS code page 860 (Portuguese)
   -863                use DOS code page 863 (French Canadian)
   -865                use DOS code page 865 (Nordic)
 -7                    convert 8 bit characters to 7 bit space
 -b, --keep-bom        keep Byte Order Mark (default)
 -c, --convmode        conversion mode
   convmode            ascii, 7bit, iso, mac, default to ascii
 -e, --add-eol         add a line break to the last line if there isn't one
 -f, --force           force conversion of binary files
 -h, --help            display this help text
 -i, --info[=FLAGS]    display file information
   file ...            files to analyze
 -k, --keepdate        keep output file date
 -L, --license         display software license
 -l, --newline         add additional newline
 -m, --add-bom         add Byte Order Mark (default UTF-8)
 -n, --newfile         write to new file
   infile              original file in new-file mode
   outfile             output file in new-file mode
 --no-allow-chown      don't allow file ownership change (default)
 --no-add-eol          don't add a line break to the last line if there isn't one (default)
 -O, --to-stdout       write to standard output
 -o, --oldfile         write to old file (default)
   file ...            files to convert in old-file mode
 -q, --quiet           quiet mode, suppress all warnings
 -r, --remove-bom      remove Byte Order Mark
 -s, --safe            skip binary files (default)
 -u,  --keep-utf16     keep UTF-16 encoding
 -ul, --assume-utf16le assume that the input format is UTF-16LE
 -ub, --assume-utf16be assume that the input format is UTF-16BE
 -v,  --verbose        verbose operation
 -F, --follow-symlink  follow symbolic links and convert the targets
 -R, --replace-symlink replace symbolic links with converted files
                         (original target files remain unchanged)
 -S, --skip-symlink    keep symbolic links and targets unchanged (default)
 -V, --version         display version number
```

### `unix2mac -h`

> 官方示例调用：`unix2mac -h`

```text
root@kali:~# unix2mac -h
Usage: unix2mac [options] [file ...] [-n infile outfile ...]
 --allow-chown         allow file ownership change
 -ascii                default conversion mode
 -iso                  conversion between DOS and ISO-8859-1 character set
   -1252               use Windows code page 1252 (Western European)
   -437                use DOS code page 437 (US) (default)
   -850                use DOS code page 850 (Western European)
   -860                use DOS code page 860 (Portuguese)
   -863                use DOS code page 863 (French Canadian)
   -865                use DOS code page 865 (Nordic)
 -7                    convert 8 bit characters to 7 bit space
 -b, --keep-bom        keep Byte Order Mark (default)
 -c, --convmode        conversion mode
   convmode            ascii, 7bit, iso, mac, default to ascii
 -e, --add-eol         add a line break to the last line if there isn't one
 -f, --force           force conversion of binary files
 -h, --help            display this help text
 -i, --info[=FLAGS]    display file information
   file ...            files to analyze
 -k, --keepdate        keep output file date
 -L, --license         display software license
 -l, --newline         add additional newline
 -m, --add-bom         add Byte Order Mark (default UTF-8)
 -n, --newfile         write to new file
   infile              original file in new-file mode
   outfile             output file in new-file mode
 --no-allow-chown      don't allow file ownership change (default)
 --no-add-eol          don't add a line break to the last line if there isn't one (default)
 -O, --to-stdout       write to standard output
 -o, --oldfile         write to old file (default)
   file ...            files to convert in old-file mode
 -q, --quiet           quiet mode, suppress all warnings
 -r, --remove-bom      remove Byte Order Mark
 -s, --safe            skip binary files (default)
 -u,  --keep-utf16     keep UTF-16 encoding
 -ul, --assume-utf16le assume that the input format is UTF-16LE
 -ub, --assume-utf16be assume that the input format is UTF-16BE
 -v,  --verbose        verbose operation
 -F, --follow-symlink  follow symbolic links and convert the targets
 -R, --replace-symlink replace symbolic links with converted files
                         (original target files remain unchanged)
 -S, --skip-symlink    keep symbolic links and targets unchanged (default)
 -V, --version         display version number
Updated on: 2026-Mar-13
 Edit this page
darkstat
fierce
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dos2unix`，再执行 `dos2unix --version` 2>/dev/null || `dos2unix -V`
- [ ] **2.** **读官方帮助** —— `dos2unix -h`，需要细节时 `man dos2unix`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: dos2unix [options] [file ...] [-n infile outfile ...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dos2unix/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dos2unix/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dos2unix/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
