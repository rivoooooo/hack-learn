# unrar-nonfree

> Extract files from rar archives root@kali:~# man unrar-nonfree UNRAR(1) RAR archiver UNRAR(1) NAME unrar - extract files from rar archives SYNOPSIS

> **功能分类**：数字取证 ｜ **Kali 包**：`unrar-nonfree` ｜ **官方文档**：<https://www.kali.org/tools/unrar-nonfree/>

## 1. 安装

```bash
sudo apt update
sudo apt install unrar-nonfree
```

| 项目 | 内容 |
|------|------|
| 版本 | 7.2.7 |
| 架构 | any |
| 可执行命令 | `libunrar-dev`、`libunrar-headers`、`libunrar5t64`、`unrar`、`unrar-nonfree` |
| 官网 | <https://www.rarlab.com/> |
| 源码仓库 | <https://github.com/debian-calibre/unrar-nonfree> |
| 包追踪 | <https://pkg.kali.org/pkg/unrar-nonfree> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libunrar-dev -h          # 查看用法
man libunrar-dev         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 5 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man unrar-nonfree`

```text
root@kali:~# man unrar-nonfree
UNRAR(1)                          RAR archiver                         UNRAR(1)
NAME
     unrar - extract files from rar archives
SYNOPSIS
     unrar command [-switch ...] archive [file ...] [@listfiles ...] [path ...]
     [path_to_extract/]
DESCRIPTION
     This manual page documents briefly the unrar command.
     This manual page was written for the Debian GNU/Linux distribution because
     the original program does not have a manual page.
     Commands and options described here are as of unrar 7.11.
     unrar is a program for extracting .rar archives.
USAGE
     archive
            Archive  file  name  in  RAR or other supported format.  If archive
            file uses RAR multiple volume format,  specify  only  first  volume
            file name as archive file name.
     file ...
            File  path name to extract.  You can specify more path names at one
            time.
     @listfiles ...
            If argument starts with "@", unrar uses listfile as file path  list
            file.   This  list  file  includes  file  path list to extract from
            archive file.  You can use 2 or more list files at one time.
            File list uses one line for one file path.  And blank line  is  ig-
            nored.
            This  file is used to extract many file path names in one time that
            your shell can't accept.
     path_to_extract
            If last argument is ended with "/", unrar uses  path_to_extract  as
            file extraction target path.
COMMANDS
     After  the  program  name  comes a command and then optional switches with
     dashes before them.  A summary of commands is included below.  For a  com-
     plete description, run unrar without options.
     e      Extract files to current directory.
     l[t[a],b]
            List archive content [technical[all], bare].
     p      Print file to stdout.
     t      Test archive files.
     v[t[a],b]
            Verbosely list archive [technical[all], bare].
     x      Extract files with full path.
OPTIONS
     NOTE: Every switch must be separated by a whitespace.  You cannot put them
     together.
     --     Stop switches scanning.
     -@[+]  Disable [enable] file lists.
     -ad[1,2]
            Alternate destination path.
     -ag[format]
            Generate archive name using the current date.
     -ai    Ignore file attributes.
     -ap<path>
            Set path inside archive.
     -c-    Disable comments show.
     -cfg-  Disable read configuration.
     -cl    Convert names to lower case.
     -cu    Convert names to upper case.
     -dh    Open shared files.
     -ep    Exclude paths from names.
     -ep3   Expand paths to full name.
     -ep4<path>
            Exclude the path prefix from names.
     -f     Freshen files.
     -id[c,d,n,p,q]
            Display or disable messages.
     -ierr  Send all messages to stderr.
     -inul  Disable all messages.
     -kb    Keep broken extracted files.
     -me[par]
            Set encryption parameters.
     -n<file>
            Additionally filter included files.
     -n@    Read additional filter masks from stdin.
     -n@<list>
            Read additional filter masks from list file.
     -o+    Overwrite existing files.
     -o-    Do not overwrite existing files.
     -ol[a,-]
            Process symbolic links as the link [absolute paths, skip].
     -om[-|1][=lst]
            Propagate Mark of the Web.
     -op<path>
            Set the output path for extracted files.
     -or    Rename files automatically.
     -ow    Save or restore file owner and group.
     -p[password]
            Set password.
     -p-    Do not query password.
     -r     Recurse subdirectories.
     -sc<chr>[obj]
            Specify the character set.
     -si[name]
            Read data from standard input (stdin).
     -sl<size>
            Process files with size less than specified.
     -sm<size>
            Process files with size more than specified.
     -ta[mcao]<d>
            Process files modified after <d> YYYYMMDDHHMMSS date.
     -tb[mcao]<d>
            Process files modified before <d> YYYYMMDDHHMMSS date.
     -tn[mcao]<t>
            Process files newer than <t> time.
     -to[mcao]<t>
            Process files older than <t> time.
     -ts[m,c,a,p]
            Save or restore time (modification, creation, access, preserve).
     -u     Update files.
     -v     List all volumes.
     -ver[n]
            File version control.
     -vp    Pause before each volume.
     -x<file>
            Exclude specified file.
     -x@<list>
            Exclude files in specified list file.
     -x@    Read file names to exclude from stdin.
     -y     Assume Yes on all queries.
FILES
     $HOME/.rarrc
     /etc/.rarrc
     /etc/rar/.rarrc
     /usr/lib/.rarrc
     /usr/local/lib/.rarrc
     /usr/local/etc/.rarrc
            UnRAR (and RAR) configuration file.
     Syntax: (switches for all commands)
            switches=<any RAR switches separated by spaces>
     Syntax: (switches for specific command)
            switches_<command>=<any RAR switches separated by spaces>
     Example:
            switches=-m5 -s
            switches_a=-m5 -s
            switches_x=-o+
SEE ALSO
     rar(1)
AUTHORS
     This  manual  page was written by Petr Cech <
[email protected]
> according to
     "unrar" for the Debian GNU/Linux system (but may be used by others).
                                   2021-11-03                          UNRAR(1)
Updated on: 2026-Aug-25
 Edit this page
unix-privesc-check
urlcrazy
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install unrar-nonfree`，再执行 `libunrar-dev --version` 2>/dev/null || `libunrar-dev -V`
- [ ] **2.** **读官方帮助** —— `libunrar-dev -h`，需要细节时 `man libunrar-dev`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `libunrar-dev -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/unrar-nonfree/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/unrar-nonfree/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/unrar-nonfree/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
