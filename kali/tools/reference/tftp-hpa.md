# tftp-hpa

> HPA’s tftp client Trivial File Transfer Protocol (TFTP) is a file transfer protocol, mainly to serve boot images over the network to other machines (PXE). tftp-hpa is an enhanced version of the BSD TFTP client and server. It possesses a nu…

> **功能分类**：通用工具 ｜ **Kali 包**：`tftp-hpa` ｜ **官方文档**：<https://www.kali.org/tools/tftp-hpa/>

## 1. 安装

```bash
sudo apt update
sudo apt install tftp-hpa
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.4 |
| 架构 | any |
| 可执行命令 | `tftp-hpa`、`tftp`、`tftpd-hpa`、`in.tftpd` |
| 依赖 | `libc6`、`tftp` |
| 安装体积 | 58 KB |
| 官网 | <https://git.kernel.org/pub/scm/network/tftp/tftp-hpa.git/> |
| 源码仓库 | <https://salsa.debian.org/debian/tftp-hpa> |
| 包追踪 | <https://pkg.kali.org/pkg/tftp-hpa> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
tftp-hpa -h          # 查看用法
man tftp-hpa         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tftp`

官方给出的调用示例：`tftp -h`

```text
root@kali:~# tftp -h
Usage: tftp [-4][-6][-v][-l][-m mode] [host [port]] [-c command]
```

### `in.tftpd`

官方给出的调用示例：`in.tftpd -h`

```text
root@kali:~# in.tftpd -h
Usage: tftpd [options] [directory]
 [options] may be:
  -t, --tftpd-timeout <value>: number of second of inactivity before exiting
  -r, --retry-timeout <value>: time to wait a reply before retransmition
  -m, --maxthread <value>    : number of concurrent thread allowed
  -v, --verbose [value]      : increase or set the level of output messages
  --trace                    : log all sent and received packets
  --no-timeout               : disable 'timeout' from RFC2349
  --no-tsize                 : disable 'tsize' from RFC2349
  --no-blksize               : disable 'blksize' from RFC2348
  --no-windowsize            : disable 'windowsize' from RFC7440
  --no-multicast             : disable 'multicast' from RFC2090
  --logfile <file>           : logfile to log logs to ;-) (use - for stdout)
  --pidfile <file>           : write PID to this file
  --listen-local             : force listen on local network address
  --daemon                   : run atftpd standalone (no inetd)
  --no-fork                  : run as a daemon, don't fork
  --prevent-sas              : prevent Sorcerer's Apprentice Syndrome
  --user <user[.group]>      : default is nobody
  --group <group>            : default is nogroup
  --port <port>              : port on which atftp listen
  --bind-address <IP>        : local address atftpd listen to
  --mcast-ttl                : ttl to used for multicast
  --mcast-addr <address list>: list/range of IP address to use
  --mcast-port <port range>  : ports to use for multicast transfer
  --pcre <file>              : use this file for pattern replacement
  --pcre-test <file>         : just test pattern file, not starting server
  --mtftp <file>             : mtftp configuration file
  --mtftp-port <port>        : port mtftp will listen
  --no-source-port-checking  : violate RFC, see man page
  --mcast-switch-client      : switch client on first timeout, see man page
  -V, --version              : print version information
  -h, --help                 : print this help
 [directory] must be a world readable/writable directories.
 By default /tftpboot is assumed.
Learn more with
OffSec
Want to learn more about tftp-hpa? get access to in-depth training and hands-on labs:
Network Penetration Testing Essentials: 19.1.3. File Transfers: Installing and Configuring TFTP
Network Penetration Testing Essentials: 19.2.5. File Transfers: TFTP
Updated on: 2026-Aug-25
 Edit this page
testssl.sh
theharvester
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install tftp-hpa`，再执行 `tftp-hpa --version` 2>/dev/null || `tftp-hpa -V`
- [ ] **2.** **读官方帮助** —— `tftp-hpa -h`，需要细节时 `man tftp-hpa`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: tftp [-4][-6][-v][-l][-m mode] [host [port]] [-c command]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/tftp-hpa/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/tftp-hpa/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/tftp-hpa/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
