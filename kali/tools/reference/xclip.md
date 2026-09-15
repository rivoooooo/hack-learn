# xclip

> Command line interface to X selections xclip is a command line utility that is designed to run on any system with an X11 implementation. It provides an interface to X selections (“the clipboard”) from the command line. It can read data fro…

> **功能分类**：通用工具 ｜ **Kali 包**：`xclip` ｜ **官方文档**：<https://www.kali.org/tools/xclip/>

## 1. 安装

```bash
sudo apt update
sudo apt install xclip
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.13 |
| 架构 | any |
| 可执行命令 | `xclip`、`xclip-copyfile`、`xclip-cutfile`、`xclip-pastefile` |
| 依赖 | `libc6`、`libx11-6`、`libxmu6` |
| 安装体积 | 62 KB |
| 官网 | <https://github.com/astrand/xclip> |
| 源码仓库 | <https://salsa.debian.org/debian/xclip> |
| 包追踪 | <https://pkg.kali.org/pkg/xclip> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
xclip -h          # 查看用法
man xclip         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `xclip`

> 官方示例调用：`xclip -h`

```text
root@kali:~# xclip -h
Usage: xclip [OPTION] [FILE]...
Access an X server selection for reading or writing.
  -i, -in          read text into X selection from standard input or files
                   (default)
  -o, -out         prints the selection to standard out (generally for
                   piping to a file or program)
  -l, -loops       number of selection requests to wait for before exiting
  -d, -display     X display to connect to (eg localhost:0")
  -h, -help        usage information
      -selection   selection to access ("primary", "secondary", "clipboard" or "buffer-cut")
      -noutf8      don't treat text as utf-8, use old unicode
      -target      use the given target atom
      -rmlastnl    remove the last newline character if present
      -version     version information
      -silent      errors only, run in background (default)
      -quiet       run in foreground, show what's happening
      -verbose     running commentary
Report bugs to <
[email protected]
>
```

### `xclip-copyfile`

> 官方示例调用：`xclip-copyfile --help`

```text
root@kali:~# xclip-copyfile --help
tar: Usage\: dirname [OPTION] NAME...\nOutput each NAME with its last non-slash component and trailing slashes\nremoved; if NAME contains no /'s, output '.' (meaning the current directory).\n\n  \033]8;;https\://www.gnu.org/software/coreutils/manual/coreutils.html#dirname-z\033\\\033[1m-z, --zero\033[0m\033]8;;\033\\\n         end each output line with NUL, not newline\n      \033]8;;https\://www.gnu.org/software/coreutils/dirname#dirname--help\033\\\033[1m--help\033[0m\033]8;;\033\\\n         display this help and exit\n      \033]8;;https\://www.gnu.org/software/coreutils/dirname#dirname--version\033\\\033[1m--version\033[0m\033]8;;\033\\\n         output version information and exit\n\nExamples\:\n  dirname /usr/bin/          -> "/usr"\n  dirname dir1/str dir2/str  -> "dir1" followed by "dir2"\n  dirname stdio.h            -> "."\n\nReport bugs to\:
[email protected]
\nGNU coreutils home page\: <https\://www.gnu.org/software/coreutils/>\nGeneral help using GNU software\: <https\://www.gnu.org/gethelp/>\nReport any translation bugs to <https\://translationproject.org/team/>\nFull documentation <https\://www.gnu.org/software/coreutils/dirname>\nor available locally via\: info '(coreutils) dirname invocation': Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
```

### `xclip-cutfile`

> 官方示例调用：`xclip-cutfile --help`

```text
root@kali:~# xclip-cutfile --help
tar: Usage\: dirname [OPTION] NAME...\nOutput each NAME with its last non-slash component and trailing slashes\nremoved; if NAME contains no /'s, output '.' (meaning the current directory).\n\n  \033]8;;https\://www.gnu.org/software/coreutils/manual/coreutils.html#dirname-z\033\\\033[1m-z, --zero\033[0m\033]8;;\033\\\n         end each output line with NUL, not newline\n      \033]8;;https\://www.gnu.org/software/coreutils/dirname#dirname--help\033\\\033[1m--help\033[0m\033]8;;\033\\\n         display this help and exit\n      \033]8;;https\://www.gnu.org/software/coreutils/dirname#dirname--version\033\\\033[1m--version\033[0m\033]8;;\033\\\n         output version information and exit\n\nExamples\:\n  dirname /usr/bin/          -> "/usr"\n  dirname dir1/str dir2/str  -> "dir1" followed by "dir2"\n  dirname stdio.h            -> "."\n\nReport bugs to\:
[email protected]
\nGNU coreutils home page\: <https\://www.gnu.org/software/coreutils/>\nGeneral help using GNU software\: <https\://www.gnu.org/gethelp/>\nReport any translation bugs to <https\://translationproject.org/team/>\nFull documentation <https\://www.gnu.org/software/coreutils/dirname>\nor available locally via\: info '(coreutils) dirname invocation': Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
```

### `xclip-pastefile`

> 官方示例调用：`xclip-pastefile -h`

```text
root@kali:~# xclip-pastefile -h
Usage: /usr/bin/xclip-pastefile
Updated on: 2026-May-25
 Edit this page
wordlists
zim
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install xclip`，再执行 `xclip --version` 2>/dev/null || `xclip -V`
- [ ] **2.** **读官方帮助** —— `xclip -h`，需要细节时 `man xclip`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: xclip [OPTION] [FILE]...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/xclip/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/xclip/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/xclip/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
