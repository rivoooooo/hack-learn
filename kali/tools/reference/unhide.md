# unhide

> Forensic tool to find hidden processes and ports Unhide is a forensic tool to find processes and TCP/UDP ports hidden by rootkits, Linux kernel modules or by other techniques. It includes two utilities: unhide and unhide-tcp. unhide detect…

> **功能分类**：数字取证 ｜ **Kali 包**：`unhide` ｜ **官方文档**：<https://www.kali.org/tools/unhide/>

## 1. 安装

```bash
sudo apt update
sudo apt install unhide
```

| 项目 | 内容 |
|------|------|
| 版本 | 20240510 |
| 架构 | any |
| 可执行命令 | `unhide`、`unhide-linux`、`unhide-posix`、`unhide-tcp`、`unhide_rb`、`unhide-gui` |
| 依赖 | `iproute2`、`libc6`、`lsof`、`procps`、`psmisc` |
| 安装体积 | 172 KB |
| 官网 | <https://www.unhide-forensics.info> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/unhide> |
| 包追踪 | <https://pkg.kali.org/pkg/unhide> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
unhide -h          # 查看用法
man unhide         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 6 个可执行命令，下面是官方页面内嵌的帮助原文。

### `unhide`

官方给出的调用示例：`unhide -h`

```text
root@kali:~# unhide -h
Unhide 20240509
Copyright © 2010-2024 Yago Jesus & Patrick Gouin
License GPLv3+ : GNU GPL version 3 or later
http://www.unhide-forensics.info
NOTE : This version of unhide is for systems using Linux >= 2.6
Usage: unhide [options] test_list
Option :
   -V          Show version and exit
   -v          verbose
   -h          display this help
   -m          more checks (available only with procfs, checkopendir & checkchdir commands)
   -r          use alternate sysinfo test in meta-test
   -f          log result into unhide-linux.log file
   -o          same as '-f'
   -d          do a double check in brute test
   -u          inhibit stdout buffering of subprocesses (needs stdbuf command)
Test_list :
   Test_list is one or more of the following
   Standard tests :
      brute
      proc
      procall
      procfs
      quick
      reverse
      sys
   Elementary tests :
      checkbrute
      checkchdir
      checkgetaffinity
      checkgetparam
      checkgetpgid
      checkgetprio
      checkRRgetinterval
      checkgetsched
      checkgetsid
      checkkill
      checknoprocps
      checkopendir
      checkproc
      checkquick
      checkreaddir
      checkreverse
      checksysinfo
      checksysinfo2
      checksysinfo3
```

### `unhide-linux`

官方给出的调用示例：`unhide-linux -h`

```text
root@kali:~# unhide-linux -h
Unhide 20240509
Copyright © 2010-2024 Yago Jesus & Patrick Gouin
License GPLv3+ : GNU GPL version 3 or later
http://www.unhide-forensics.info
NOTE : This version of unhide is for systems using Linux >= 2.6
Usage: unhide-linux [options] test_list
Option :
   -V          Show version and exit
   -v          verbose
   -h          display this help
   -m          more checks (available only with procfs, checkopendir & checkchdir commands)
   -r          use alternate sysinfo test in meta-test
   -f          log result into unhide-linux.log file
   -o          same as '-f'
   -d          do a double check in brute test
   -u          inhibit stdout buffering of subprocesses (needs stdbuf command)
Test_list :
   Test_list is one or more of the following
   Standard tests :
      brute
      proc
      procall
      procfs
      quick
      reverse
      sys
   Elementary tests :
      checkbrute
      checkchdir
      checkgetaffinity
      checkgetparam
      checkgetpgid
      checkgetprio
      checkRRgetinterval
      checkgetsched
      checkgetsid
      checkkill
      checknoprocps
      checkopendir
      checkproc
      checkquick
      checkreaddir
      checkreverse
      checksysinfo
      checksysinfo2
      checksysinfo3
```

### `unhide-posix`

官方给出的调用示例：`unhide-posix -h`

```text
root@kali:~# unhide-posix -h
Unhide-posix 20240509
Copyright © 2013-2024 Yago Jesus & Patrick Gouin
License GPLv3+ : GNU GPL version 3 or later
http://www.unhide-forensics.info
NOTE : This is legacy version of unhide, it is intended
       for systems using Linux < 2.6 or other UNIX systems
usage: unhide-posix proc | sys
```

### `unhide-tcp`

官方给出的调用示例：`unhide-tcp -h`

```text
root@kali:~# unhide-tcp -h
Unhide-tcp 20240509
Copyright © 2010-2024 Yago Jesus & Patrick Gouin
License GPLv3+ : GNU GPL version 3 or later
http://www.unhide-forensics.info
Usage: unhide-tcp [options]
Options :
   -V          Show version and exit
   -v          verbose
   -h          display this help
   -f          show fuser output for hidden ports
   -l          show lsof output for hidden ports
   -o          log result into unhide-tcp.log file
   -s          use very quick version for server with lot of opened ports
   -n          use netstat instead of ss
```

### `man`

官方给出的调用示例：`man unhide_rb`

```text
root@kali:~# man unhide_rb
UNHIDE(8)                   System Manager's Manual                   UNHIDE(8)
NAME
     unhide -- forensic tool to find hidden processes
SYNOPSIS
     unhide [OPTIONS] TEST_LIST
     unhide-posix proc | sys
DESCRIPTION
     unhide is a forensic tool to find processes hidden by rootkits, Linux ker-
     nel modules or by other techniques.  It detects hidden processes using six
     techniques.
OPTIONS
     Options are only available for unhide-linux not for unhide-posix.
     -d     Do a double check in brute test to avoid false positive.
     -f     Write a log file (unhide-linux.log) in the current directory.
     -h     Display help
     -m     Do  more checks. As of 2012-03-17 version, this option has only ef-
            fect for the procfs, procall, checkopendir and checkchdir tests.
            Implies -v
     -r     Use alternate version of sysinfo check in standard tests
     -V     Show version and exit
     -v     Be verbose, display warning  message  (default  :  don't  display).
            This option may be repeated more than once.
     -u     Do  unbuffered  write  to stdout.  This option could be useful when
            unhide is spawned by another process (e.g. it's used by unhideGui).
     -H     Provide a slightly human frienlier output.  This option adds ending
            messages to tests and indicates when no hidden process is found.
TEST_LIST
     The checks to do consist of one or more of the following tests.
     The standard tests are the aggregation of one or more elementary test(s).
     Standard tests :
     The brute technique consists of bruteforcing the all process IDs.
     This technique is only available with version unhide-linux.
     The proc technique consists of comparing /proc with the output of /bin/ps.
     The procall technique combinates proc and procfs tests.
     This technique is only available with version unhide-linux.
     The procfs technique  consists  of  comparing  information  gathered  from
     /bin/ps with information gathered by walking in the procfs.
     With -m option, this test makes more checks, see checkchdir test.
     This technique is only available with version unhide-linux.
     The  quick  technique  combines  the  proc, procfs and sys techniques in a
     quick way. It's about 20 times faster but may give more false positives.
     This technique is only available with version unhide-linux.
     The reverse technique consists of verifying that all threads  seen  by  ps
     are also seen in procfs and by system calls. It is intended to verify that
     a  rootkit has not killed a security tool (IDS or other) and make ps show-
     ing a fake process instead.
     This technique is only available with version unhide-linux.
     The sys technique consists of comparing information gathered from  /bin/ps
     with information gathered from system calls.
     Elementary tests :
     The checkbrute technique consists of bruteforcing the all process IDs.
     This technique is only available with version unhide-linux.
     The  checkchdir  technique consists of comparing information gathered from
     /bin/ps with information gathered by making chdir() in the procfs.
     With the -m option, it also verify that the thread appears in its  "leader
     process" threads list.
     This technique is only available with version unhide-linux.
     The  checkgetaffinity technique consists of comparing information gathered
     from /bin/ps with the result of call  to  the  sched_getaffinity()  system
     function.
     This technique is only available with version unhide-linux.
     The  checkgetparam  technique  consists  of comparing information gathered
     from /bin/ps with the result of call to the sched_getparam() system  func-
     tion.
     This technique is only available with version unhide-linux.
     The checkgetpgid technique consists of comparing information gathered from
     /bin/ps with the result of call to the getpgid() system function.
     This technique is only available with version unhide-linux.
     The checkgetprio technique consists of comparing information gathered from
     /bin/ps with the result of call to the getpriority() system function.
     This technique is only available with version unhide-linux.
     The  checkRRgetinterval  technique consists of comparing information gath-
     ered from /bin/ps with the result of call to  the  sched_rr_get_interval()
     system function.
     This technique is only available with version unhide-linux.
     The  checkgetsched  technique  consists  of comparing information gathered
     from /bin/ps with the result of call to  the  sched_getscheduler()  system
     function.
     This technique is only available with version unhide-linux.
     The  checkgetsid technique consists of comparing information gathered from
     /bin/ps with the result of call to the getsid() system function.
     This technique is only available with version unhide-linux.
     The checkkill technique consists of comparing  information  gathered  from
     /bin/ps with the result of call to the kill() system function.
     Note : no process is really killed by this test.
     This technique is only available with version unhide-linux.
     The  checknoprocps  technique consists of comparing the result of the call
     to each of the system functions. No comparison is done  against  /proc  or
     the output of ps.
     This technique is only available with version unhide-linux.
     The checkopendir technique consists of comparing information gathered from
     /bin/ps with information gathered by making opendir() in the procfs.
     This technique is only available with version unhide-linux.
     The  checkproc  technique  consists  of comparing /proc with the output of
     /bin/ps.
     This technique is only available with version unhide-linux.
     The checkquick technique combines the proc, procfs and sys techniques in a
     quick way. It's about 20 times faster but may give more false positives.
     This technique is only available with version unhide-linux.
     The checkreaddir technique consists of comparing information gathered from
     /bin/ps with  information  gathered  by  making  readdir()  in  /proc  and
     /proc/pid/task.
     This technique is only available with version unhide-linux.
     The  checkreverse technique consists of verifying that all threads seen by
     ps are also seen in procfs and by system calls. It is intended  to  verify
     that  a  rootkit has not killed a security tool (IDS or other) and make ps
     showing a fake process instead.
     This technique is only available with version unhide-linux.
     The checksysinfo technique consists of comparing  the  number  of  process
     seen by /bin/ps with information obtained from sysinfo() system call.
     This technique is only available with version unhide-linux.
     The  checksysinfo2 technique is an alternate version of checksysinfo test.
     It might (or not) work better on kernel patched for RT, preempt or latency
     and with kernel that don't use the standard scheduler.
     It's also invoked by standard tests when using the -r option
     This technique is only available with version unhide-linux.
   Exit status:
     0      if OK,
     1      if a hidden or fake thread is found.
EXAMPLES
     Quicker test:
            unhide quick
     Quick test:
            unhide quick reverse
     Standard test:
            unhide sys proc
     Deeper test:
            unhide -m -d sys procall brute reverse
BUGS
     Report unhide bugs on the bug tracker on  GitHub  (https://github.com/YJe-
     sus/Unhide/issues)
     With  recent versions of Linux kernel (> 2.6.33), the sysinfo test may re-
     port false positives.  It may be due to optimization in the scheduler, the
     use of cgroup or even the use of systemd.  The use of the PREEMPT-RT patch
     amplifies the occurrence of the problem.  This is currently under investi-
     gation.
SEE ALSO
     unhide-tcp (8).
AUTHOR
     This manual page was written by Francois Marier (
[email protected]
)  and
     Patrick Gouin (
[email protected]
).
     Permission  is granted to copy, distribute and/or modify this document un-
     der the terms of the GNU General Public License, Version 3  or  any  later
     version published by the Free Software Foundation.
LICENSE
     License   GPLv3+:   GNU   GPL   version  3  or  later  <http://gnu.org/li-
     censes/gpl.html>.
     This is free software: you are free to change and redistribute it.   There
     is NO WARRANTY, to the extent permitted by law.
Administration commands             May 2024                          UNHIDE(8)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install unhide`，再执行 `unhide --version` 2>/dev/null || `unhide -V`
- [ ] **2.** **读官方帮助** —— `unhide -h`，需要细节时 `man unhide`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: unhide [options] test_list`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/unhide/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/unhide/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/unhide/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
