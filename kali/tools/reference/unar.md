# unar

> Unarchiver for a variety of file formats The Unarchiver is an archive unpacker program with support for the popular zip, RAR, 7z, tar, gzip, bzip2, LZMA, XZ, CAB, MSI, NSIS, EXE, ISO, BIN, and split file formats, as well as the old Stuffit…

> **功能分类**：数字取证 ｜ **Kali 包**：`unar` ｜ **官方文档**：<https://www.kali.org/tools/unar/>

## 1. 安装

```bash
sudo apt update
sudo apt install unar
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.10.8 |
| 架构 | any |
| 可执行命令 | `unar`、`lsar` |
| 依赖 | `gnustep-base-runtime`、`libbz2-1.0`、`libc6`、`libgcc-s1`、`libgnustep-base1.31`、`libicu78`、`libobjc4`、`libstdc++6`、`libwavpack1`、`zlib1g`、`lsar` |
| 安装体积 | 5.85 MB |
| 官网 | <https://theunarchiver.com/command-line> |
| 源码仓库 | <https://salsa.debian.org/gnustep-team/unar> |
| 包追踪 | <https://pkg.kali.org/pkg/unar> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
unar -h          # 查看用法
man unar         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `lsar`

> 官方示例调用：`lsar -h`

```text
root@kali:~# lsar -h
lsar v1.10.8, a tool for listing the contents of archive files.
Usage: lsar [options] archive [files ...]
Available options:
-long (-l)                           Print more information about each file in
                                     the archive.
-verylong (-L)                       Print all available information about each
                                     file in the archive.
-test (-t)                           Test the integrity of the files in the
                                     archive, if possible.
-password (-p) <string>              The password to use for decrypting
                                     protected archives.
-encoding (-e) <encoding name>       The encoding to use for filenames in the
                                     archive, when it is not known. If not
                                     specified, the program attempts to
                                     auto-detect the encoding used. Use "help"
                                     or "list" as the argument to give a listing
                                     of all supported encodings.
-password-encoding (-E) <name>       The encoding to use for the password for
                                     the archive, when it is not known. If not
                                     specified, then either the encoding given
                                     by the -encoding option or the
                                     auto-detected encoding is used.
-print-encoding (-pe)                Print the auto-detected encoding and the
                                     confidence factor after the file list
-indexes (-i)                        Instead of specifying the files to list as
                                     filenames or wildcard patterns, specify
                                     them as indexes.
-json (-j)                           Print the listing in JSON format.
-json-skip-solid-information (-jss)  Do not print solid object information in
                                     the JSON output.Can be helpful for solid
                                     archives with a lot of files.
-json-ascii (-ja)                    Print the listing in JSON format, encoded
                                     as pure ASCII text.
-no-recursion (-nr)                  Do not attempt to list archives contained
                                     in other archives. For instance, when
                                     unpacking a .tar.gz file, only list the .gz
                                     file and not its contents.
-help (-h)                           Display this information.
-version (-v)                        Print version and exit.
```

### `unar`

> 官方示例调用：`unar -h`

```text
root@kali:~# unar -h
unar v1.10.8, a tool for extracting the contents of archive files.
Usage: unar [options] archive [files ...]
Available options:
-output-directory (-o) <string>    The directory to write the contents of the
                                   archive to. Defaults to the current
                                   directory. If set to a single dash (-), no
                                   files will be created, and all data will be
                                   output to stdout.
-force-overwrite (-f)              Always overwrite files when a file to be
                                   unpacked already exists on disk. By default,
                                   the program asks the user if possible,
                                   otherwise skips the file.
-force-rename (-r)                 Always rename files when a file to be
                                   unpacked already exists on disk.
-force-skip (-s)                   Always skip files when a file to be unpacked
                                   already exists on disk.
-force-directory (-d)              Always create a containing directory for the
                                   contents of the unpacked archive. By default,
                                   a directory is created if there is more than
                                   one top-level file or folder.
-no-directory (-D)                 Never create a containing directory for the
                                   contents of the unpacked archive.
-password (-p) <string>            The password to use for decrypting protected
                                   archives.
-encoding (-e) <encoding name>     The encoding to use for filenames in the
                                   archive, when it is not known. If not
                                   specified, the program attempts to
                                   auto-detect the encoding used. Use "help" or
                                   "list" as the argument to give a listing of
                                   all supported encodings.
-password-encoding (-E) <name>     The encoding to use for the password for the
                                   archive, when it is not known. If not
                                   specified, then either the encoding given by
                                   the -encoding option or the auto-detected
                                   encoding is used.
-indexes (-i)                      Instead of specifying the files to unpack as
                                   filenames or wildcard patterns, specify them
                                   as indexes, as output by lsar.
-no-recursion (-nr)                Do not attempt to extract archives contained
                                   in other archives. For instance, when
                                   unpacking a .tar.gz file, only unpack the .gz
                                   file and not its contents.
-copy-time (-t)                    Copy the file modification time from the
                                   archive file to the containing directory, if
                                   one is created.
-forks (-k) <visible|hidden|skip>  How to handle Mac OS resource forks.
                                   "visible" creates AppleDouble files with the
                                   extension ".rsrc", "hidden" creates
                                   AppleDouble files with the prefix "._", and
                                   "skip" discards all resource forks. Defaults
                                   to "visible".
-quiet (-q)                        Run in quiet mode.
-version (-v)                      Print version and exit.
-help (-h)                         Display this information.
Updated on: 2026-Aug-25
 Edit this page
uhd
unblob
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install unar`，再执行 `unar --version` 2>/dev/null || `unar -V`
- [ ] **2.** **读官方帮助** —— `unar -h`，需要细节时 `man unar`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: lsar [options] archive [files ...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/unar/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/unar/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/unar/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
