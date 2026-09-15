# 0trace

> Traceroute tool that can run within an existing TCP connection The package is traceroute tool that can be run within an existing, open TCP connection, therefore bypassing some types of stateful packet filters with ease.

> **功能分类**：信息搜集 ｜ **Kali 包**：`0trace` ｜ **官方文档**：<https://www.kali.org/tools/0trace/>

## 1. 安装

```bash
sudo apt update
sudo apt install 0trace
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.01 |
| 架构 | any |
| 可执行命令 | `0trace`、`0trace.sh`、`sendprobe`、`usleep` |
| 依赖 | `libc6`、`tcpdump`、`0trace.sh` |
| 安装体积 | 43 KB |
| 官网 | <https://lcamtuf.coredump.cx> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/0trace> |
| 包追踪 | <https://pkg.kali.org/pkg/0trace> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
0trace -h          # 查看用法
man 0trace         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `0trace.sh`

> 官方示例调用：`0trace.sh -h`

```text
root@kali:~# 0trace.sh -h
Usage: /usr/bin/0trace.sh iface target_ip [ target_port ]
```

### `sendprobe`

> 官方示例调用：`sendprobe -h`

```text
root@kali:~# sendprobe -h
Usage: sendprobe src_ip dst_ip sport dport seq ack
```

### `man`

> 官方示例调用：`man usleep`

```text
root@kali:~# man usleep
usleep(3)                   Library Functions Manual                  usleep(3)
NAME
     usleep - suspend execution for microsecond intervals
LIBRARY
     Standard C library (libc, -lc)
SYNOPSIS
     #include <unistd.h>
     int usleep(useconds_t usec);
 Feature Test Macro Requirements for glibc (see feature_test_macros(7)):
     usleep():
         Since glibc 2.12:
             (_XOPEN_SOURCE >= 500) && ! (_POSIX_C_SOURCE >= 200809L)
                 || /* glibc >= 2.19: */ _DEFAULT_SOURCE
                 || /* glibc <= 2.19: */ _BSD_SOURCE
         Before glibc 2.12:
             _BSD_SOURCE || _XOPEN_SOURCE >= 500
DESCRIPTION
     The  usleep()  function  suspends  execution of the calling thread for (at
     least) usec microseconds.  The sleep may be  lengthened  slightly  by  any
     system  activity or by the time spent processing the call or by the granu-
     larity of system timers.
RETURN VALUE
     The usleep() function returns 0 on success.  On  error,  -1  is  returned,
     with errno set to indicate the error.
ERRORS
     EINTR  Interrupted by a signal; see signal(7).
     EINVAL
            usec  is  greater than or equal to 1000000.  (On systems where that
            is considered an error.)
ATTRIBUTES
     For an explanation of the terms used in this section, see attributes(7).
     +----------------------------------------------+---------------+---------+
     | Interface                                    | Attribute     | Value   |
     +----------------------------------------------+---------------+---------+
     | usleep()                                     | Thread safety | MT-Safe |
     +----------------------------------------------+---------------+---------+
STANDARDS
     None.
HISTORY
     4.3BSD,  POSIX.1-2001.   POSIX.1-2001  declares  it  obsolete,  suggesting
     nanosleep(2) instead.  Removed in POSIX.1-2008.
     On  the  original  BSD  implementation, and before glibc 2.2.2, the return
     type of this function is void.  The POSIX version returns int, and this is
     also the prototype used since glibc 2.2.2.
     Only the EINVAL error return is documented by SUSv2 and POSIX.1-2001.
CAVEATS
     The interaction of this function with the SIGALRM signal, and  with  other
     timer  functions  such  as alarm(2), sleep(3), nanosleep(2), setitimer(2),
     timer_create(2), timer_delete(2),  timer_getoverrun(2),  timer_gettime(2),
     timer_settime(2), ualarm(3) is unspecified.
SEE ALSO
     alarm(2),  getitimer(2),  nanosleep(2), select(2), setitimer(2), sleep(3),
     ualarm(3), useconds_t(3type), time(7)
Linux man-pages 6.18               2026-02-08                         usleep(3)
Updated on: 2026-May-25
 Edit this page
wireshark
above
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install 0trace`，再执行 `0trace --version` 2>/dev/null || `0trace -V`
- [ ] **2.** **读官方帮助** —— `0trace -h`，需要细节时 `man 0trace`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: /usr/bin/0trace.sh iface target_ip [ target_port ]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/0trace/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/0trace/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/0trace/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
