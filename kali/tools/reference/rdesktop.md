# rdesktop

> RDP client for Windows NT/2000 Terminal Server and Windows Servers rdesktop is an open source client for Windows NT/2000 Terminal Server and Windows Server 2003/2008. Capable of natively speaking its Remote Desktop Protocol (RDP) in order …

> **功能分类**：信息搜集 ｜ **Kali 包**：`rdesktop` ｜ **官方文档**：<https://www.kali.org/tools/rdesktop/>

## 1. 安装

```bash
sudo apt update
sudo apt install rdesktop
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.9.0 |
| 架构 | any |
| 可执行命令 | `rdesktop` |
| 依赖 | `libasound2t64`、`libc6`、`libgmp10`、`libgnutls30t64`、`libgssapi-krb5-2`、`libhogweed6t64`、`libnettle8t64`、`libpcsclite1`、`libtasn1-6`、`libx11-6`、`libxcursor1`、`libxrandr2` |
| 安装体积 | 692 KB |
| 官网 | <https://www.rdesktop.org/> |
| 源码仓库 | <https://salsa.debian.org/debian/rdesktop> |
| 包追踪 | <https://pkg.kali.org/pkg/rdesktop> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
rdesktop -h          # 查看用法
man rdesktop         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rdesktop`

官方给出的调用示例：`rdesktop --help`

```text
root@kali:~# rdesktop --help
rdesktop: invalid option -- '-'
rdesktop: A Remote Desktop Protocol client.
Version 1.9.0. Copyright (C) 1999-2016 Matthew Chapman et al.
See http://www.rdesktop.org/ for more information.
Usage: rdesktop [options] server[:port]
   -u: user name
   -d: domain
   -s: shell / seamless application to start remotely
   -c: working directory
   -p: password (- to prompt)
   -n: client hostname
   -k: keyboard layout on server (en-us, de, sv, etc.)
   -g: desktop geometry (WxH[@DPI][+X[+Y]])
   -i: enables smartcard authentication, password is used as pin
   -f: full-screen mode
   -b: force bitmap updates
   -L: local codepage
   -A: path to SeamlessRDP shell, this enables SeamlessRDP mode
   -V: tls version (1.0, 1.1, 1.2, defaults to negotiation)
   -B: use BackingStore of X-server (if available)
   -e: disable encryption (French TS)
   -E: disable encryption from client to server
   -m: do not send motion events
   -M: use local mouse cursor
   -C: use private colour map
   -D: hide window manager decorations
   -K: keep window manager key bindings
   -S: caption button size (single application mode)
   -T: window title
   -t: disable use of remote ctrl
   -N: enable numlock synchronization
   -X: embed into another window with a given id.
   -a: connection colour depth
   -z: enable rdp compression
   -x: RDP5 experience (m[odem 28.8], b[roadband], l[an] or hex nr.)
   -P: use persistent bitmap caching
   -r: enable specified device redirection (this flag can be repeated)
         '-r comport:COM1=/dev/ttyS0': enable serial redirection of /dev/ttyS0 to COM1
             or      COM1=/dev/ttyS0,COM2=/dev/ttyS1
         '-r disk:floppy=/mnt/floppy': enable redirection of /mnt/floppy to 'floppy' share
             or   'floppy=/mnt/floppy,cdrom=/mnt/cdrom'
         '-r clientname=<client name>': Set the client name displayed
             for redirected disks
         '-r lptport:LPT1=/dev/lp0': enable parallel redirection of /dev/lp0 to LPT1
             or      LPT1=/dev/lp0,LPT2=/dev/lp1
         '-r printer:mydeskjet': enable printer redirection
             or      mydeskjet="HP LaserJet IIIP" to enter server driver as well
         '-r sound:[local[:driver[:device]]|off|remote]': enable sound redirection
                     remote would leave sound on server
                     available drivers for 'local':
                     alsa:	ALSA output driver, default device: default
         '-r clipboard:[off|PRIMARYCLIPBOARD|CLIPBOARD]': enable clipboard
                      redirection.
                      'PRIMARYCLIPBOARD' looks at both PRIMARY and CLIPBOARD
                      when sending data to server.
                      'CLIPBOARD' looks at only CLIPBOARD.
         '-r scard[:"Scard Name"="Alias Name[;Vendor Name]"[,...]]
          example: -r scard:"eToken PRO 00 00"="AKS ifdh 0"
                   "eToken PRO 00 00" -> Device in GNU/Linux and UNIX environment
                   "AKS ifdh 0"       -> Device shown in Windows environment
          example: -r scard:"eToken PRO 00 00"="AKS ifdh 0;AKS"
                   "eToken PRO 00 00" -> Device in GNU/Linux and UNIX environment
                   "AKS ifdh 0"       -> Device shown in Microsoft Windows environment
                   "AKS"              -> Device vendor name
   -0: attach to console
   -4: use RDP version 4
   -5: use RDP version 5 (default)
   -o: name=value: Adds an additional option to rdesktop.
           sc-csp-name        Specifies the Crypto Service Provider name which
                              is used to authenticate the user by smartcard
           sc-container-name  Specifies the container name, this is usually the username
           sc-reader-name     Smartcard reader name to use
           sc-card-name       Specifies the card name of the smartcard to use
   -v: enable verbose logging
Updated on: 2026-Jun-17
 Edit this page
pspy
reaver
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install rdesktop`，再执行 `rdesktop --version` 2>/dev/null || `rdesktop -V`
- [ ] **2.** **读官方帮助** —— `rdesktop -h`，需要细节时 `man rdesktop`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: rdesktop [options] server[:port]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rdesktop/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/lateral-movement.md`](../../tools/by-attack/lateral-movement.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rdesktop/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rdesktop/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
