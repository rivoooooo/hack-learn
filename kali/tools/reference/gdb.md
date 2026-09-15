# gdb

> GNU Debugger GDB is a source-level debugger, capable of breaking programs at any specific line, displaying variable values, and determining where errors occurred. Currently, gdb supports C, C++, D, Objective-C, Fortran, Java, OpenCL C, Pas…

> **功能分类**：数字取证 ｜ **Kali 包**：`gdb` ｜ **官方文档**：<https://www.kali.org/tools/gdb/>

## 1. 安装

```bash
sudo apt update
sudo apt install gdb
```

| 项目 | 内容 |
|------|------|
| 版本 | 17.2 |
| 架构 | any |
| 可执行命令 | `gdb`、`gcore`、`gdb-add-index`、`gdbtui`、`gstack`、`gdb-minimal`、`gdb-multiarch`、`gdb-source`、`gdbserver` |
| 依赖 | `libc6`、`libdebuginfod1t64`、`libexpat1`、`libgcc-s1`、`libgmp10`、`libipt2`、`liblzma5`、`libmpfr6`、`libncursesw6`、`libpython3.14`、`libreadline8t64`、`libsource-highlight4t64` 等 |
| 安装体积 | 12.16 MB |
| 官网 | <https://www.gnu.org/s/gdb/> |
| 源码仓库 | <https://salsa.debian.org/gdb-team/gdb> |
| 包追踪 | <https://pkg.kali.org/pkg/gdb> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gdb -h          # 查看用法
man gdb         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 9 个可执行命令，下面是官方页面内嵌的帮助原文。

### `gcore`

> 官方示例调用：`gcore -h`

```text
root@kali:~# gcore -h
Usage: /usr/bin/gcore [-h|--help] [-v|--version]
                      [-a] [-o prefix] [-d data-directory]
                      pid1 [pid2...pidN]
Create a core file of a running program using GDB.
  -h, --help         Print this message then exit.
  -v, --version      Print version information then exit.
  -a                 Dump all memory mappings.
  -o prefix          Use 'prefix.pid' as the core file name.
                       The default prefix is 'core'.
  -d dir             Pass '--data-directory dir' as an argument
                       to GDB.
```

### `gdb`

> 官方示例调用：`gdb -h`

```text
root@kali:~# gdb -h
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
```

### `gdb-add-index`

> 官方示例调用：`gdb-add-index -h`

```text
root@kali:~# gdb-add-index -h
Usage: gdb-add-index [-h|--help] [-v|--version] [--dwarf-5] FILENAME
Add a .gdb_index section to FILENAME to facilitate faster debug
information loading by GDB.
  -h, --help         Print this message then exit.
  -v, --version      Print version information then exit.
  --dwarf-5          Add the DWARF-5 style .debug_names section
                       instead of .gdb_index.
```

### `gdbtui`

> 官方示例调用：`gdbtui -h`

```text
root@kali:~# gdbtui -h
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
```

### `gstack`

> 官方示例调用：`gstack -h`

```text
root@kali:~# gstack -h
Usage: /usr/bin/gstack [-h|--help] [-v|--version] PID
Print a stack trace of a running program
  -h, --help         Print this message then exit.
  -v, --version      Print version information then exit.
```

### `gdb-multiarch`

> 官方示例调用：`gdb-multiarch -h`

```text
root@kali:~# gdb-multiarch -h
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
```

### `gdbserver`

> 官方示例调用：`gdbserver --help`

```text
root@kali:~# gdbserver --help
Usage:	gdbserver [OPTIONS] COMM PROG [ARGS ...]
	gdbserver [OPTIONS] --attach COMM PID
	gdbserver [OPTIONS] --multi COMM
COMM may either be a tty device (for serial debugging),
HOST:PORT to listen for a TCP connection, or '-' or 'stdio' to use
stdin/stdout of gdbserver.
PROG is the executable program.  ARGS are arguments passed to inferior.
PID is the process ID to attach to, when --attach is specified.
Operating modes:
  --attach              Attach to running process PID.
  --multi               Start server without a specific program, and
                        only quit when explicitly commanded.
  --once                Exit after the first connection has closed.
  --help                Print this message and then exit.
  --version             Display version information and exit.
Other options:
  --wrapper WRAPPER --  Run WRAPPER to start new programs.
  --disable-randomization
                        Run PROG with address space randomization disabled.
  --no-disable-randomization
                        Don't disable address space randomization when
                        starting PROG.
  --startup-with-shell
                        Start PROG using a shell.  I.e., execs a shell that
                        then execs PROG.  (default)
  --no-startup-with-shell
                        Exec PROG directly instead of using a shell.
                        Disables argument globbing and variable substitution
                        on UNIX-like systems.
Debug options:
  --debug[=OPT1,OPT2,...]
                        Enable debugging output.
                          Options:
                            all, threads, event-loop, remote
                          With no options, 'threads' is assumed.
                          Prefix an option with '-' to disable
                          debugging of that component.
  --debug-format=OPT1[,OPT2,...]
                        Specify extra content in debugging output.
                          Options:
                            all
                            none
                            timestamp
  --disable-packet=OPT1[,OPT2,...]
                        Disable support for RSP packets or features.
                          Options:
                            vCont, vConts, T, Tthread, qC, qfThreadInfo and
                            threads (disable all threading packets).
For more information, consult the GDB manual (available as on-line
info or a printed manual).
Report bugs to "<http://www.gnu.org/software/gdb/bugs/>".
Learn more with
OffSec
Want to learn more about gdb? get access to in-depth training and hands-on labs:
Low Level Programming - x86 Skill Path
Low Level Programming - ARM Skill Path
Updated on: 2026-Aug-25
 Edit this page
ftester
gef
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install gdb`，再执行 `gdb --version` 2>/dev/null || `gdb -V`
- [ ] **2.** **读官方帮助** —— `gdb -h`，需要细节时 `man gdb`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: /usr/bin/gcore [-h|--help] [-v|--version]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gdb/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[gdb](../../tools/tutorials/10-逆向工程/gdb.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gdb/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gdb/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
