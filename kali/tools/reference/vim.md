# vim

> Vi IMproved - enhanced vi editor Vim is an almost compatible version of the UNIX editor Vi. Many new features have been added: multi level undo, syntax highlighting, command line history, on-line help, filename completion, block operations…

> **功能分类**：通用工具 ｜ **Kali 包**：`vim` ｜ **官方文档**：<https://www.kali.org/tools/vim/>

## 1. 安装

```bash
sudo apt update
sudo apt install vim
```

| 项目 | 内容 |
|------|------|
| 版本 | 9.2.0858 |
| 架构 | any |
| 可执行命令 | `vim`、`vim.basic`、`vim-common`、`helpztags`、`vim-doc`、`vim-gtk3`、`vim.gtk3`、`vim-gui-common`、`gvimtutor`、`vim-motif`、`vim.motif`、`vim-nox`、`vim.nox`、`vim-runtime`、`vimtutor`、`vim-tiny`、`vim.tiny`、`xxd` |
| 依赖 | `libacl1`、`libc6`、`libgpm2`、`libselinux1`、`libsodium26`、`libtinfo6`、`vim-common`、`vim-runtime`、`vim.basic` |
| 安装体积 | 4.06 MB |
| 官网 | <https://www.vim.org/> |
| 源码仓库 | <https://salsa.debian.org/vim-team/vim> |
| 包追踪 | <https://pkg.kali.org/pkg/vim> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
vim -h          # 查看用法
man vim         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 18 个可执行命令，下面是官方页面内嵌的帮助原文。

### `vim.basic`

官方给出的调用示例：`vim.basic -h`

```text
root@kali:~# vim.basic -h
VIM - Vi IMproved 9.2 (2026 Feb 14, compiled Jul 27 2026 10:11:18)
Usage: vim [arguments] [file ..]       edit specified file(s)
   or: vim [arguments] -               read text from stdin
   or: vim [arguments] -t tag          edit file where tag is defined
   or: vim [arguments] -q [errorfile]  edit file with first error
Arguments:
   --			Only file names after this
   -v			Vi mode (like "vi")
   -e			Ex mode (like "ex")
   -E			Improved Ex mode
   -s			Silent (batch) mode (only for "ex")
   -d			Diff mode (like "vimdiff")
   -y			Easy mode (like "evim", modeless)
   -R			Readonly mode (like "view")
   -Z			Restricted mode (like "rvim")
   -m			Modifications (writing files) not allowed
   -M			Modifications in text not allowed
   -b			Binary mode
   -l			Lisp mode
   -C			Compatible with Vi: 'compatible'
   -N			Not fully Vi compatible: 'nocompatible'
   -V[N][fname]		Be verbose [level N] [log messages to fname]
   -D			Debugging mode
   -n			No swap file, use memory only
   -r			List swap files and exit
   -r (with file name)	Recover crashed session
   -L			Same as -r
   -A			Start in Arabic mode
   -H			Start in Hebrew mode
   -T <terminal>	Set terminal type to <terminal>
   --not-a-term		Skip warning for input/output not being a terminal
   --ttyfail		Exit if input or output is not a terminal
   -u <vimrc>		Use <vimrc> instead of any .vimrc
   --noplugin		Don't load plugin scripts
   -p[N]		Open N tab pages (default: one for each file)
   -o[N]		Open N windows (default: one for each file)
   -O[N]		Like -o but split vertically
   +			Start at end of file
   +<lnum>		Start at line <lnum>
   --cmd <command>	Execute <command> before loading any vimrc file
   -c <command>		Execute <command> after loading the first file
   -S <session>		Source file <session> after loading the first file
   -s <scriptin>	Read Normal mode commands from file <scriptin>
   -w <scriptout>	Append all typed commands to file <scriptout>
   -W <scriptout>	Write all typed commands to file <scriptout>
   -x			Edit encrypted files
   --remote <files>	Edit <files> in a Vim server if possible
   --remote-silent <files>  Same, don't complain if there is no server
   --remote-wait <files>  As --remote but wait for files to have been edited
   --remote-wait-silent <files>  Same, don't complain if there is no server
   --remote-tab[-wait][-silent] <files>  As --remote but use tab page per file
   --remote-send <keys>	Send <keys> to a Vim server and exit
   --remote-expr <expr>	Evaluate <expr> in a Vim server and print result
   --serverlist		List available Vim server names and exit
   --servername <name>	Send to/become the Vim server <name>
   --startuptime <file>	Write startup timing messages to <file>
   --log <file>		Start logging to <file> early
   -i <viminfo>		Use <viminfo> instead of .viminfo
   --clean		'nocompatible', Vim defaults, no plugins, no viminfo
   -h  or  --help	Print Help (this message) and exit
   --version		Print version information and exit
```

### `man`

官方给出的调用示例：`man helpztags`

```text
root@kali:~# man helpztags
HELPZTAGS(1)                     User Commands                     HELPZTAGS(1)
NAME
     helpztags - generate the help tags file for directory
SYNOPSIS
     helpztags DIRS...
DESCRIPTION
     helpztags scans given directories for *.txt and *.txt.gz files.  Each file
     is scanned for tags used in vim help files. For each directory proper tags
     file is generated.
     There should be at least one directory given. In other case program exits
     with error.
AUTHORS
     Written by Jakub Turski and Artur R. Czechowski based on idea contained in
     vim sources for its :helptags command.
REPORTING BUGS
     Please use a Debian reportbug command or procedure described at
     http://bugs.debian.org/.
SEE ALSO
     Read :help helptags in vim for detailed information about helptags.
vim 9.2                           August 2010                      HELPZTAGS(1)
```

### `vim.gtk3`

官方给出的调用示例：`vim.gtk3 -h`

```text
root@kali:~# vim.gtk3 -h
VIM - Vi IMproved 9.2 (2026 Feb 14, compiled Jul 27 2026 10:11:18)
Usage: vim [arguments] [file ..]       edit specified file(s)
   or: vim [arguments] -               read text from stdin
   or: vim [arguments] -t tag          edit file where tag is defined
   or: vim [arguments] -q [errorfile]  edit file with first error
Arguments:
   --			Only file names after this
   -g			Run using GUI (like "gvim")
   -f  or  --nofork	Foreground: Don't fork when starting GUI
   -v			Vi mode (like "vi")
   -e			Ex mode (like "ex")
   -E			Improved Ex mode
   -s			Silent (batch) mode (only for "ex")
   -d			Diff mode (like "vimdiff")
   -y			Easy mode (like "evim", modeless)
   -R			Readonly mode (like "view")
   -Z			Restricted mode (like "rvim")
   -m			Modifications (writing files) not allowed
   -M			Modifications in text not allowed
   -b			Binary mode
   -l			Lisp mode
   -C			Compatible with Vi: 'compatible'
   -N			Not fully Vi compatible: 'nocompatible'
   -V[N][fname]		Be verbose [level N] [log messages to fname]
   -D			Debugging mode
   -n			No swap file, use memory only
   -r			List swap files and exit
   -r (with file name)	Recover crashed session
   -L			Same as -r
   -A			Start in Arabic mode
   -H			Start in Hebrew mode
   -T <terminal>	Set terminal type to <terminal>
   --not-a-term		Skip warning for input/output not being a terminal
   --gui-dialog-file {fname}  For testing: write dialog text
   --ttyfail		Exit if input or output is not a terminal
   -u <vimrc>		Use <vimrc> instead of any .vimrc
   -U <gvimrc>		Use <gvimrc> instead of any .gvimrc
   --noplugin		Don't load plugin scripts
   -p[N]		Open N tab pages (default: one for each file)
   -o[N]		Open N windows (default: one for each file)
   -O[N]		Like -o but split vertically
   +			Start at end of file
   +<lnum>		Start at line <lnum>
   --cmd <command>	Execute <command> before loading any vimrc file
   -c <command>		Execute <command> after loading the first file
   -S <session>		Source file <session> after loading the first file
   -s <scriptin>	Read Normal mode commands from file <scriptin>
   -w <scriptout>	Append all typed commands to file <scriptout>
   -W <scriptout>	Write all typed commands to file <scriptout>
   -x			Edit encrypted files
   -X			Do not connect to X server
   -Y			Do not connect to Wayland compositor
   --clientserver <socket|x11|mswin> Backend for clientserver communication
   --remote <files>	Edit <files> in a Vim server if possible
   --remote-silent <files>  Same, don't complain if there is no server
   --remote-wait <files>  As --remote but wait for files to have been edited
   --remote-wait-silent <files>  Same, don't complain if there is no server
   --remote-tab[-wait][-silent] <files>  As --remote but use tab page per file
   --remote-send <keys>	Send <keys> to a Vim server and exit
   --remote-expr <expr>	Evaluate <expr> in a Vim server and print result
   --serverlist		List available Vim server names and exit
   --servername <name>	Send to/become the Vim server <name>
   --startuptime <file>	Write startup timing messages to <file>
   --log <file>		Start logging to <file> early
   -i <viminfo>		Use <viminfo> instead of .viminfo
   --clean		'nocompatible', Vim defaults, no plugins, no viminfo
   -h  or  --help	Print Help (this message) and exit
   --version		Print version information and exit
Arguments recognised by gvim (GTK+ version):
   -background <color>	Use <color> for the background (also: -bg)
   -foreground <color>	Use <color> for normal text (also: -fg)
   -font <font>		Use <font> for normal text (also: -fn)
   -geometry <geom>	Use <geom> for initial geometry (also: -geom)
   -iconic		Start Vim iconified
   -reverse		Use reverse video (also: -rv)
   -display <display>	Run Vim on <display> (also: --display)
   --role <role>	Set a unique role to identify the main window
   --socketid <xid>	Open Vim inside another GTK widget
   --echo-wid		Make gvim echo the Window ID on stdout
```

### `gvimtutor`

官方给出的调用示例：`gvimtutor -h`

```text
root@kali:~# gvimtutor -h
==USAGE=========================================================================================
vimtutor [[-(-l)anguage] ISO639] [-(-c)hapter NUMBER] [-(-g)ui] | [-(-h)elp] | [--list]
	where:
		ISO639 (default=en) is a 2 or 3 character language code
		NUMBER (default=1) is a chapter number (1 or 2)
	examples:
		vimtutor -l es -c 2 -g
		vimtutor --language de --chapter 2
		vimtutor fr
More information at 'man vimtutor'
================================================================================================
```

### `vim.motif`

官方给出的调用示例：`vim.motif -h`

```text
root@kali:~# vim.motif -h
VIM - Vi IMproved 9.2 (2026 Feb 14, compiled Jul 27 2026 10:11:18)
Usage: vim [arguments] [file ..]       edit specified file(s)
   or: vim [arguments] -               read text from stdin
   or: vim [arguments] -t tag          edit file where tag is defined
   or: vim [arguments] -q [errorfile]  edit file with first error
Arguments:
   --			Only file names after this
   -g			Run using GUI (like "gvim")
   -f  or  --nofork	Foreground: Don't fork when starting GUI
   -v			Vi mode (like "vi")
   -e			Ex mode (like "ex")
   -E			Improved Ex mode
   -s			Silent (batch) mode (only for "ex")
   -d			Diff mode (like "vimdiff")
   -y			Easy mode (like "evim", modeless)
   -R			Readonly mode (like "view")
   -Z			Restricted mode (like "rvim")
   -m			Modifications (writing files) not allowed
   -M			Modifications in text not allowed
   -b			Binary mode
   -l			Lisp mode
   -C			Compatible with Vi: 'compatible'
   -N			Not fully Vi compatible: 'nocompatible'
   -V[N][fname]		Be verbose [level N] [log messages to fname]
   -D			Debugging mode
   -n			No swap file, use memory only
   -r			List swap files and exit
   -r (with file name)	Recover crashed session
   -L			Same as -r
   -A			Start in Arabic mode
   -H			Start in Hebrew mode
   -T <terminal>	Set terminal type to <terminal>
   --not-a-term		Skip warning for input/output not being a terminal
   --gui-dialog-file {fname}  For testing: write dialog text
   --ttyfail		Exit if input or output is not a terminal
   -u <vimrc>		Use <vimrc> instead of any .vimrc
   -U <gvimrc>		Use <gvimrc> instead of any .gvimrc
   --noplugin		Don't load plugin scripts
   -p[N]		Open N tab pages (default: one for each file)
   -o[N]		Open N windows (default: one for each file)
   -O[N]		Like -o but split vertically
   +			Start at end of file
   +<lnum>		Start at line <lnum>
   --cmd <command>	Execute <command> before loading any vimrc file
   -c <command>		Execute <command> after loading the first file
   -S <session>		Source file <session> after loading the first file
   -s <scriptin>	Read Normal mode commands from file <scriptin>
   -w <scriptout>	Append all typed commands to file <scriptout>
   -W <scriptout>	Write all typed commands to file <scriptout>
   -x			Edit encrypted files
   -display <display>	Connect Vim to this particular X-server
   -X			Do not connect to X server
   -Y			Do not connect to Wayland compositor
   --clientserver <socket|x11|mswin> Backend for clientserver communication
   --remote <files>	Edit <files> in a Vim server if possible
   --remote-silent <files>  Same, don't complain if there is no server
   --remote-wait <files>  As --remote but wait for files to have been edited
   --remote-wait-silent <files>  Same, don't complain if there is no server
   --remote-tab[-wait][-silent] <files>  As --remote but use tab page per file
   --remote-send <keys>	Send <keys> to a Vim server and exit
   --remote-expr <expr>	Evaluate <expr> in a Vim server and print result
   --serverlist		List available Vim server names and exit
   --servername <name>	Send to/become the Vim server <name>
   --startuptime <file>	Write startup timing messages to <file>
   --log <file>		Start logging to <file> early
   -i <viminfo>		Use <viminfo> instead of .viminfo
   --clean		'nocompatible', Vim defaults, no plugins, no viminfo
   -h  or  --help	Print Help (this message) and exit
   --version		Print version information and exit
Arguments recognised by gvim (Motif version):
   -display <display>	Run Vim on <display>
   -iconic		Start Vim iconified
   -background <color>	Use <color> for the background (also: -bg)
   -foreground <color>	Use <color> for normal text (also: -fg)
   -font <font>		Use <font> for normal text (also: -fn)
   -boldfont <font>	Use <font> for bold text
   -italicfont <font>	Use <font> for italic text
   -geometry <geom>	Use <geom> for initial geometry (also: -geom)
   -borderwidth <width>	Use a border width of <width> (also: -bw)
   -scrollbarwidth <width>  Use a scrollbar width of <width> (also: -sw)
   -reverse		Use reverse video (also: -rv)
   +reverse		Don't use reverse video (also: +rv)
   -xrm <resource>	Set the specified resource
```

### `vim.nox`

官方给出的调用示例：`vim.nox -h`

```text
root@kali:~# vim.nox -h
VIM - Vi IMproved 9.2 (2026 Feb 14, compiled Jul 27 2026 10:11:18)
Usage: vim [arguments] [file ..]       edit specified file(s)
   or: vim [arguments] -               read text from stdin
   or: vim [arguments] -t tag          edit file where tag is defined
   or: vim [arguments] -q [errorfile]  edit file with first error
Arguments:
   --			Only file names after this
   -v			Vi mode (like "vi")
   -e			Ex mode (like "ex")
   -E			Improved Ex mode
   -s			Silent (batch) mode (only for "ex")
   -d			Diff mode (like "vimdiff")
   -y			Easy mode (like "evim", modeless)
   -R			Readonly mode (like "view")
   -Z			Restricted mode (like "rvim")
   -m			Modifications (writing files) not allowed
   -M			Modifications in text not allowed
   -b			Binary mode
   -l			Lisp mode
   -C			Compatible with Vi: 'compatible'
   -N			Not fully Vi compatible: 'nocompatible'
   -V[N][fname]		Be verbose [level N] [log messages to fname]
   -D			Debugging mode
   -n			No swap file, use memory only
   -r			List swap files and exit
   -r (with file name)	Recover crashed session
   -L			Same as -r
   -A			Start in Arabic mode
   -H			Start in Hebrew mode
   -T <terminal>	Set terminal type to <terminal>
   --not-a-term		Skip warning for input/output not being a terminal
   --ttyfail		Exit if input or output is not a terminal
   -u <vimrc>		Use <vimrc> instead of any .vimrc
   --noplugin		Don't load plugin scripts
   -p[N]		Open N tab pages (default: one for each file)
   -o[N]		Open N windows (default: one for each file)
   -O[N]		Like -o but split vertically
   +			Start at end of file
   +<lnum>		Start at line <lnum>
   --cmd <command>	Execute <command> before loading any vimrc file
   -c <command>		Execute <command> after loading the first file
   -S <session>		Source file <session> after loading the first file
   -s <scriptin>	Read Normal mode commands from file <scriptin>
   -w <scriptout>	Append all typed commands to file <scriptout>
   -W <scriptout>	Write all typed commands to file <scriptout>
   -x			Edit encrypted files
   --remote <files>	Edit <files> in a Vim server if possible
   --remote-silent <files>  Same, don't complain if there is no server
   --remote-wait <files>  As --remote but wait for files to have been edited
   --remote-wait-silent <files>  Same, don't complain if there is no server
   --remote-tab[-wait][-silent] <files>  As --remote but use tab page per file
   --remote-send <keys>	Send <keys> to a Vim server and exit
   --remote-expr <expr>	Evaluate <expr> in a Vim server and print result
   --serverlist		List available Vim server names and exit
   --servername <name>	Send to/become the Vim server <name>
   --startuptime <file>	Write startup timing messages to <file>
   --log <file>		Start logging to <file> early
   -i <viminfo>		Use <viminfo> instead of .viminfo
   --clean		'nocompatible', Vim defaults, no plugins, no viminfo
   -h  or  --help	Print Help (this message) and exit
   --version		Print version information and exit
```

### `vimtutor`

官方给出的调用示例：`vimtutor -h`

```text
root@kali:~# vimtutor -h
==USAGE=========================================================================================
vimtutor [[-(-l)anguage] ISO639] [-(-c)hapter NUMBER] [-(-g)ui] | [-(-h)elp] | [--list]
	where:
		ISO639 (default=en) is a 2 or 3 character language code
		NUMBER (default=1) is a chapter number (1 or 2)
	examples:
		vimtutor -l es -c 2 -g
		vimtutor --language de --chapter 2
		vimtutor fr
More information at 'man vimtutor'
================================================================================================
```

### `vim.tiny`

官方给出的调用示例：`vim.tiny -h`

```text
root@kali:~# vim.tiny -h
VIM - Vi IMproved 9.2 (2026 Feb 14, compiled Jul 27 2026 10:11:18)
Usage: vim [arguments] [file ..]       edit specified file(s)
   or: vim [arguments] -               read text from stdin
   or: vim [arguments] -t tag          edit file where tag is defined
Arguments:
   --			Only file names after this
   -v			Vi mode (like "vi")
   -e			Ex mode (like "ex")
   -E			Improved Ex mode
   -s			Silent (batch) mode (only for "ex")
   -y			Easy mode (like "evim", modeless)
   -R			Readonly mode (like "view")
   -Z			Restricted mode (like "rvim")
   -m			Modifications (writing files) not allowed
   -M			Modifications in text not allowed
   -b			Binary mode
   -l			Lisp mode
   -C			Compatible with Vi: 'compatible'
   -N			Not fully Vi compatible: 'nocompatible'
   -V[N][fname]		Be verbose [level N] [log messages to fname]
   -n			No swap file, use memory only
   -r			List swap files and exit
   -r (with file name)	Recover crashed session
   -L			Same as -r
   -T <terminal>	Set terminal type to <terminal>
   --not-a-term		Skip warning for input/output not being a terminal
   --ttyfail		Exit if input or output is not a terminal
   -u <vimrc>		Use <vimrc> instead of any .vimrc
   --noplugin		Don't load plugin scripts
   -p[N]		Open N tab pages (default: one for each file)
   -o[N]		Open N windows (default: one for each file)
   -O[N]		Like -o but split vertically
   +			Start at end of file
   +<lnum>		Start at line <lnum>
   --cmd <command>	Execute <command> before loading any vimrc file
   -c <command>		Execute <command> after loading the first file
   -S <session>		Source file <session> after loading the first file
   -s <scriptin>	Read Normal mode commands from file <scriptin>
   -w <scriptout>	Append all typed commands to file <scriptout>
   -W <scriptout>	Write all typed commands to file <scriptout>
   --clean		'nocompatible', Vim defaults, no plugins, no viminfo
   -h  or  --help	Print Help (this message) and exit
   --version		Print version information and exit
```

### `xxd`

官方给出的调用示例：`xxd -h`

```text
root@kali:~# xxd -h
Usage:
       xxd [options] [infile [outfile]]
    or
       xxd -r [-s [-]offset] [-c cols] [-ps] [infile [outfile]]
Options:
    -a          toggle autoskip: A single '*' replaces nul-lines. Default off.
    -b          binary digit dump (incompatible with -ps). Default hex.
    -C          capitalize variable names in C include file style (-i).
    -c cols     format <cols> octets per line. Default 16 (-i: 12, -ps: 30).
    -E          show characters in EBCDIC. Default ASCII.
    -e          little-endian dump (incompatible with -ps,-i,-r).
    -g bytes    number of octets per group in normal output. Default 2 (-e: 4).
    -h          print this summary.
    -i          output in C include file style.
    -t          append terminating zero to C include output (-i).
    -l len      stop after <len> octets.
    -n name     set the variable name used in C include output (-i).
    -o off      add <off> to the displayed file position.
    -ps         output in postscript plain hexdump style.
    -r          reverse operation: convert (or patch) hexdump into binary.
    -r -s off   revert with <off> added to file positions found in hexdump.
    -d          show offset in decimal instead of hex.
    -s [+][-]seek  start at <seek> bytes abs. (or +: rel.) infile offset.
    -u          use upper case hex letters.
    -R when     colorize the output; <when> can be 'always', 'auto' or 'never'. Default: 'auto'.
    -v          show version: "xxd 2026-06-16 by Juergen Weigert et al.".
Updated on: 2026-Aug-25
 Edit this page
veil
vopono
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install vim`，再执行 `vim --version` 2>/dev/null || `vim -V`
- [ ] **2.** **读官方帮助** —— `vim -h`，需要细节时 `man vim`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: vim [arguments] [file ..]       edit specified file(s)`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/vim/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/vim/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/vim/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
