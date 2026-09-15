# ptunnel

> Tunnel TCP connections over ICMP packets ptunnel is an application that allows you to reliably tunnel TCP connections to a remote host using ICMP echo request and reply packets, commonly known as ping requests and replies. It acts as a pro…

> **功能分类**：后渗透 ｜ **Kali 包**：`ptunnel` ｜ **官方文档**：<https://www.kali.org/tools/ptunnel/>

## 1. 安装

```bash
sudo apt update
sudo apt install ptunnel
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.72 |
| 架构 | any |
| 可执行命令 | `ptunnel` |
| 依赖 | `libc6`、`libpcap0.8t64`、`libselinux1`、`lsb-base` |
| 安装体积 | 133 KB |
| 官网 | <http://www.mit.edu/afs.new/sipb/user/golem/tmp/ptunnel-0.61.orig/web/> |
| 源码仓库 | <https://salsa.debian.org/alteholz/ptunnel> |
| 包追踪 | <https://pkg.kali.org/pkg/ptunnel> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ptunnel -h          # 查看用法
man ptunnel         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ptunnel`

> 官方示例调用：`ptunnel -h`

```text
root@kali:~# ptunnel -h
ptunnel v 0.72.
Usage:   ptunnel -p <addr> -lp <port> -da <dest_addr> -dp <dest_port> [-m max_tunnels] [-v verbosity] [-f logfile]
         ptunnel [-m max_threads] [-v verbosity] [-c <device>]
     -p: Set address of peer running packet forwarder. This causes
         ptunnel to operate in forwarding mode - the absence of this
         option causes ptunnel to operate in proxy mode.
    -lp: Set TCP listening port (only used when operating in forward mode)
    -da: Set remote proxy destination address if client
         Restrict to only this destination address if server
    -dp: Set remote proxy destionation port if client
         Restrict to only this destination port if server
     -m: Set maximum number of concurrent tunnels
     -v: Verbosity level (-1 to 4, where -1 is no output, and 4 is all output)
     -c: Enable libpcap on the given device.
     -f: Specify a file to log to, rather than printing to standard out.
     -s: Client only. Enables continuous output of statistics (packet loss, etc.)
-daemon: Run in background, the PID will be written in the file supplied as argument
-syslog: Output debug to syslog instead of standard out.
   -udp: Toggle use of UDP instead of ICMP. Proxy will listen on port 53 (must be root).
Security features:  [-x password] [-u] [-setuid user] [-setgid group] [-chroot dir]
     -x: Set password (must be same on client and proxy)
     -u: Run proxy in unprivileged mode. This causes the proxy to forward
         packets using standard echo requests, instead of crafting custom echo replies.
         Unprivileged mode will only work on some systems, and is in general less reliable
         than running in privileged mode.
         Please consider combining the following three options instead:
-setuid: When started in privileged mode, drop down to user's rights as soon as possible
-setgid: When started in privileged mode, drop down to group's rights as soon as possible
-chroot: When started in privileged mode, restrict file access to the specified directory
-setcon: Set SELinux context when all there is left to do are network I/O operations
         To combine with -chroot you will have to `mount --bind /proc /chrootdir/proc`
Starting the proxy (needs to run as root):
 [root #] ptunnel
Starting a client (also needs root):
 [root #] ptunnel -p proxy.pingtunnel.com -lp 8000 -da login.domain.com -dp 22 -c eth0
And then using the tunnel to ssh to login.domain.com:
 [user $] ssh -p 8000 localhost
And that's it. Enjoy your tunnel!
Updated on: 2025-Dec-09
 Edit this page
pskracker
pwnat
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ptunnel`，再执行 `ptunnel --version` 2>/dev/null || `ptunnel -V`
- [ ] **2.** **读官方帮助** —— `ptunnel -h`，需要细节时 `man ptunnel`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:   ptunnel -p <addr> -lp <port> -da <dest_addr> -dp <dest_port> [-m max_tunnels] [-v verbosity] [-f logfile]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ptunnel/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ptunnel/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ptunnel/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
