# minicom

> Menu-driven serial communication program Minicom is a text-mode serial communications program modelled on the MS-DOS program Telix. It drives modems and serial consoles through a full-screen, menu-driven interface and emulates ANSI and VT1…

> **功能分类**：硬件攻击 ｜ **Kali 包**：`minicom` ｜ **官方文档**：<https://www.kali.org/tools/minicom/>

## 1. 安装

```bash
sudo apt update
sudo apt install minicom
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.11.1 |
| 架构 | any |
| 可执行命令 | `minicom`、`ascii-xfr`、`runscript`、`xminicom` |
| 依赖 | `libc6`、`libtinfo6`、`ascii-xfr` |
| 安装体积 | 1.10 MB |
| 官网 | <https://salsa.debian.org/minicom-team/minicom> |
| 包追踪 | <https://pkg.kali.org/pkg/minicom> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
minicom -h          # 查看用法
man minicom         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ascii-xfr`

官方给出的调用示例：`ascii-xfr -h`

```text
root@kali:~# ascii-xfr -h
ascii-xfr: invalid option -- 'h'
Usage: ascii-xfr -s|-r [-dvn] [-l linedelay] [-c character delay] filename
       -s:  send
       -r:  receive
       -e:  send the End Of File character (default is not to)
       -d:  set End Of File character to Control-D (instead of Control-Z)
       -v:  verbose (statistics on stderr output)
       -n:  do not translate CRLF <--> LF
       Delays are in milliseconds.
```

### `minicom`

官方给出的调用示例：`minicom -h`

```text
root@kali:~# minicom -h
Usage: minicom [OPTION]... [configuration]
A terminal program for Linux and other unix-like systems.
  -b, --baudrate         : set baudrate (ignore the value from config)
  -D, --device           : set device name (ignore the value from config)
  -s, --setup            : enter setup mode
  -o, --noinit           : do not initialize modem & lockfiles at startup
  -m, --metakey          : use meta or alt key for commands
  -M, --metakey8         : use 8bit meta key for commands
  -l, --ansi             : literal; assume screen uses non IBM-PC character set
  -L, --iso              : don't assume screen uses ISO8859
  -w, --wrap             : Linewrap on
  -H, --displayhex       : display output in hex
  -z, --statline         : try to use terminal's status line
  -7, --7bit             : force 7bit mode
  -8, --8bit             : force 8bit mode
  -c, --color=on/off     : ANSI style color usage on or off
  -a, --attrib=on/off    : use reverse or highlight attributes on or off
  -t, --term=TERM        : override TERM environment variable
  -S, --script=SCRIPT    : run SCRIPT at startup
  -d, --dial=ENTRY       : dial ENTRY from the dialing directory
  -p, --ptty=TTYP        : connect to pseudo terminal
  -C, --capturefile=FILE : start capturing to FILE
  --capturefile-buffer-mode=MODE : set buffering mode of capture file
  -F, --statlinefmt      : format of status line
  -R, --remotecharset    : character set of communication partner
  -v, --version          : output version information and exit
  -h, --help             : show help
  configuration          : configuration file to use
These options can also be specified in the MINICOM environment variable.
This variable is currently unset.
The configuration directory for the access file and the configurations
is compiled to /etc/minicom.
Report bugs to <
[email protected]
>.
```

### `man`

官方给出的调用示例：`man runscript`

```text
root@kali:~# man runscript
RUNSCRIPT(1)                General Commands Manual                RUNSCRIPT(1)
NAME
     runscript - script interpreter for minicom
SYNOPSIS
     runscript scriptname [logfile [homedir]]
DESCRIPTION
     runscript  is  a  simple script interpreter that can be called from within
     the minicom communications program to automate tasks like logging in to  a
     Unix system or your favorite BBS.
INVOCATION
     The program expects a script name and optionally a filename and the user's
     home directory as arguments, and it expects that it's input and output are
     connected  to the "remote end", the system you are connecting to. All mes-
     sages from runscript meant for the local screen are directed to the stderr
     output. All this is automatically taken care of if you run it  from  mini-
     com.   The logfile and home directory parameters are only used to tell the
     log command the name of the logfile and where to write it. If the  homedir
     is  omitted,  runscript  uses the directory found in the $HOME environment
     variable. If also the logfile name is omitted, the log  commands  are  ig-
     nored.
KEYWORDS
     Runscript recognizes the following commands:
          expect   send     goto     gosub    return   !<   !
          exit     print    set      inc      dec      if   timeout
          verbose  sleep    break    call     log
OVERVIEW OF KEYWORDS
     send <string>
          <string>  is  sent  to the modem. It is followed by a '\r'.  <string>
          can be:
            - regular text, e.g. 'send hello'
            - text enclosed in quotes, e.g. 'send "hello world"'
          Within <string> the following sequences are recognized:
              \n - newline
              \r - carriage return
              \a - bell
              \b - backspace
              \c - don't send the default '\r'.
              \f - formfeed
              \^ - the ^ character
              \o - send character o (o is an octal number)
          Control characters can be used in the string with the ^ prefix (^A to
          ^Z, ^[, ^ ^], ^^ and ^_). If you need to send the  ^  character,  you
          must prefix it with the \ escape character.
          Octal  characters  are  either four-digit or delimited by a non-digit
          character, e.g. the null character may be sent with \0000  and  'send
          1234' is equivalent to 'send \0061234'.
          Also $(environment_variable) can be used, for example $(TERM).  Mini-
          com  passes  three  special environment variables: $(LOGIN), which is
          the username, $(PASS), which is  the  password,  as  defined  in  the
          proper  entry  of  the dialing directory, and $(TERMLIN) which is the
          number of actual terminal lines on your screen  (that  is,  the  sta-
          tusline excluded).
     print <string>
          Prints <string> to the local screen. Default followed by '\r\n'.  See
          the description of 'send' above.
     label:
          Declares a label (with the name 'label') to use with goto or gosub.
     goto <label>
          Jump to another place in the program.
     gosub <label>
          Jumps to another place in the program. When the statement 'return' is
          encountered,  control  returns to the statement after the gosub.  Go-
          sub's can be nested.
     return
          Return from a gosub.
     ! <command>
          Runs a shell for you in which 'command' is executed. On  return,  the
          variable  '$?'  is set to the exit status of this command, so you can
          subsequently test it using 'if'.
     !< <command>
          Runs a shell for you in which 'command' is executed. The stdout  out-
          put  of  the  command execution will be sent to the modem. On return,
          the variable '$?' is set to the exit status of this command,  so  you
          can subsequently test it using 'if'.
     exit [value]
          Exit from "runscript" with an optional exit status. (default 1)
     set <variable> <value>
          Sets  the  value  of <variable> (which is a single letter a-z) to the
          value <value>. If <variable> does not  exist,  it  will  be  created.
          <value> can be a integer value or another variable.
     inc <variable>
          Increments the value of <variable> by one.
     dec <variable>
          Decrements the value of <variable> by one.
     if <value> <operator> <value> <statement>
          Conditional  execution  of <statement>. <operator> can be <, >, != or
          =.  Eg, 'if a > 3 goto exitlabel'.
     timeout <value>
          Sets the global timeout. By default, 'runscript' will exit after  120
          seconds. This can be changed with this command. Warning: this command
          acts  differently  within  an 'expect' statement, but more about that
          later.
     verbose <on|off>
          By default, this is 'on'. That means that anything that is being read
          from the modem by 'runscript', gets echoed to the screen.  This is so
          that you can see what 'runscript' is doing.
     sleep <value>
          Suspend execution for <value> seconds.
     expect
            expect {
              pattern  [statement]
              pattern  [statement]
              [timeout <value> [statement] ]
              ....
            }
          The most important command of all. Expect keeps reading from the  in-
          put  until it reads a pattern that matches one of the specified ones.
          If expect encounters an optional statement  after  that  pattern,  it
          will  execute  it.  Otherwise the default is to just break out of the
          expect. 'pattern' is a string, just as in 'send' (see  above).   Nor-
          mally,  expect will timeout in 60 seconds and just exit, but this can
          be changed with the timeout command.
     break
          Break out of an 'expect' statement. This is normally only  useful  as
          argument to 'timeout' within an expect, because the default action of
          timeout is to exit immediately.
     call <scriptname>
          Transfers  control to another script file. When that script file fin-
          ishes without errors, the original script will continue.
     log <text>
          Write text to the logfile.
NOTES
     If you want to make your script to exit minicom (for example when you  use
     minicom  to  dial up your ISP, and then start a PPP or SLIP session from a
     script), try the command "! killall -9 minicom" as the  last  script  com-
     mand.  The  -9  option should prevent minicom from hanging up the line and
     resetting the modem before exiting.
     Well, I don't think this is enough information to make you an  experienced
     'programmer'  in  'runscript', but together with the examples it shouldn't
     be too hard to write some useful script files. Things will  be  easier  if
     you  have  experience  with BASIC.  The minicom source code comes together
     with two example scripts, scriptdemo and unixlogin.  Especially  the  last
     one is a good base to build on for your own scripts.
SEE ALSO
     minicom(1)
BUGS
     Runscript should be built in to minicom.
AUTHOR
     Miquel   van   Smoorenburg,   <
[email protected]
>   Jukka   Lahtinen,
     <
[email protected]
>
```

### `man（示例）`

官方给出的调用示例：`man xminicom`

```text
root@kali:~# man xminicom
XMINICOM(1)                    Linux Users Manual                   XMINICOM(1)
NAME
     xminicom - friendly serial communication program
SYNOPSIS
     xminicom minicom-options
DESCRIPTION
     Xminicom is a script wrapper around minicom.  It tries to find a color ca-
     pable  xterm  or  rxvt  on  your system, and then runs minicom with the -c
     (color) flag in a terminal session.
OPTIONS
     See minicom (1).
AUTHOR
     Miquel van Smoorenburg,
[email protected]
SEE ALSO
     minicom(1)
                               September 14, 1998                   XMINICOM(1)
Updated on: 2026-Aug-25
 Edit this page
metasploit-framework
mitmproxy
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install minicom`，再执行 `minicom --version` 2>/dev/null || `minicom -V`
- [ ] **2.** **读官方帮助** —— `minicom -h`，需要细节时 `man minicom`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ascii-xfr -s|-r [-dvn] [-l linedelay] [-c character delay] filename`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/minicom/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/minicom/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/minicom/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
