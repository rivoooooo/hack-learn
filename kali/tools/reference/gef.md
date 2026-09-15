# gef

> Modern experience for GDB with advanced debugging capabilities GEF is a set of commands for x86/64, ARM, MIPS, PowerPC and SPARC to assist exploit developers and reverse-engineers when using old school GDB. It provides additional features …

> **功能分类**：通用工具 ｜ **Kali 包**：`gef` ｜ **官方文档**：<https://www.kali.org/tools/gef/>

## 1. 安装

```bash
sudo apt update
sudo apt install gef
```

| 项目 | 内容 |
|------|------|
| 版本 | 2026.01 |
| 架构 | all |
| 可执行命令 | `gef` |
| 依赖 | `gdb` |
| 安装体积 | 436 KB |
| 官网 | <https://github.com/hugsy/gef> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/gef> |
| 包追踪 | <https://pkg.kali.org/pkg/gef> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gef -h          # 查看用法
man gef         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `gef`

> 官方示例调用：`gef -h`

```text
root@kali:~# gef -h
This is the GNU debugger.  Usage:
    gdb [options] [executable-file [core-file or process-id]]
    gdb [options] --args executable-file [inferior-arguments ...]
Selection of debuggee and its files:
  --args             Arguments after executable-file are passed to inferior.
  --core=COREFILE    Analyze the core dump COREFILE.
  --exec=EXECFILE    Use EXECFILE as the executable.
  --pid=PID          Attach to running process PID.
  --directory=DIR    Search for source files in DIR.
  --se=FILE          Use FILE as symbol file and executable file.
  --symbols=SYMFILE  Read symbols from SYMFILE.
  --readnow          Fully read symbol files on first access.
  --readnever        Do not read symbol files.
  --write            Set writing into executable and core files.
Initial commands and command files:
  --command=FILE, -x Execute GDB commands from FILE.
  --init-command=FILE, -ix
		     Like -x but execute commands before loading inferior.
  --eval-command=COMMAND, -ex
		     Execute a single GDB command.
		     May be used multiple times and in conjunction
		     with --command.
  --init-eval-command=COMMAND, -iex
		     Like -ex but before loading inferior.
  --nh               Do not read ~/.gdbinit.
  --nx               Do not read any .gdbinit files in any directory.
Output and user interface control:
  --fullname         Output information used by emacs-GDB interface.
  --interpreter=INTERP
		     Select a specific interpreter / user interface.
  --tty=TTY          Use TTY for input/output by the program being debugged.
  -w                 Use the GUI interface.
  --nw               Do not use the GUI interface.
  --tui              Use a terminal user interface.
  -q, --quiet, --silent
		     Do not print version number on startup.
Operating modes:
  --batch            Exit after processing options.
  --batch-silent     Like --batch, but suppress all gdb stdout output.
  --return-child-result
		     GDB exit code will be the child's exit code.
  --configuration    Print details about GDB configuration and then exit.
  --help             Print this message and then exit.
  --version          Print version information and then exit.
Remote debugging options:
  -b BAUDRATE        Set serial port baud rate used for remote debugging.
  -l TIMEOUT         Set timeout in seconds for remote debugging.
Other options:
  --cd=DIR           Change current directory to DIR.
  --data-directory=DIR, -D
		     Set GDB's data-directory to DIR.
At startup, GDB reads the following early init files and executes their
commands:
   None found.
At startup, GDB reads the following init files and executes their commands:
   * system-wide init files: /etc/gdb/gdbinit
For more information, type "help" from within GDB, or consult the
GDB manual (available as on-line info or a printed manual).
Report bugs to <https://www.gnu.org/software/gdb/bugs/>.
You can ask GDB-related questions on the GDB users mailing list
(
[email protected]
) or on GDB's IRC channel (#gdb on Libera.Chat).
Updated on: 2026-Aug-25
 Edit this page
gdb
gemini-cli
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install gef`，再执行 `gef --version` 2>/dev/null || `gef -V`
- [ ] **2.** **读官方帮助** —— `gef -h`，需要细节时 `man gef`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `gef -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gef/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gef/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gef/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
