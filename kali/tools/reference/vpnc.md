# vpnc

> Cisco-compatible VPN client vpnc is a VPN client compatible with cisco3000 VPN Concentrator (also known as Cisco’s EasyVPN equipment). vpnc runs entirely in userspace and does not require kernel modules except for the tun driver to communi…

> **功能分类**：通用工具 ｜ **Kali 包**：`vpnc` ｜ **官方文档**：<https://www.kali.org/tools/vpnc/>

## 1. 安装

```bash
sudo apt update
sudo apt install vpnc
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.5.3 |
| 架构 | any |
| 可执行命令 | `vpnc`、`cisco-decrypt`、`pcf2vpnc`、`vpnc-connect`、`vpnc-disconnect` |
| 依赖 | `libc6`、`libgcrypt20`、`libgnutls30t64`、`perl`、`vpnc-scripts`、`cisco-decrypt` |
| 安装体积 | 238 KB |
| 官网 | <https://github.com/streambinder/vpnc> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/vpnc> |
| 包追踪 | <https://pkg.kali.org/pkg/vpnc> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
vpnc -h          # 查看用法
man vpnc         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 5 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cisco-decrypt`

> 官方示例调用：`cisco-decrypt -h`

```text
root@kali:~# cisco-decrypt -h
Usage: cisco-decrypt DEADBEEF...012345678 424242...7261
    Print decoded result to stdout
```

### `man`

> 官方示例调用：`man pcf2vpnc`

```text
root@kali:~# man pcf2vpnc
PCF2VPNC(1)                           vpnc                          PCF2VPNC(1)
NAME
     pcf2vpnc - converts VPN-config files from pcf to vpnc-format
SYNOPSIS
     pcf2vpnc <pcf file> [vpnc file]
DESCRIPTION
     This  script  accompanies vpnc. It attempts to convert *.pcf-configuration
     files  often  spread  with  proprietary  (read  Cisco)  VPN-clients   into
     vpnc-configuration files, usually named *.conf.
     If  [vpnc file] is not specified, the result will be printed to STDOUT. If
     specified, it will be written to that file. Please make sure that  it  has
     appropriate permissions as it may contain sensitive data!
AUTHOR
     pcf2vpnc  was  originally  written  by  Stefan  Tomanek.  Updates and this
     man-page were made by Wolfram Sang (ninja(at)the-dreams.de).
     Permission is granted to copy, distribute and/or modify this document  un-
     der  the terms of the GNU General Public License, Version 2 any later ver-
     sion published by the Free Software Foundation.
     On Debian systems, the complete text of the GNU General Public License can
     be found in /usr/share/common-licenses/GPL.
SEE ALSO
     vpnc(8) cisco-decrypt(8)
pcf2vpnc                           June 2007                        PCF2VPNC(1)
```

### `vpnc`

> 官方示例调用：`vpnc --help`

```text
root@kali:~# vpnc --help
Usage: vpnc [--version] [--print-config] [--help] [--long-help] [options] [config files]
Options:
  --gateway <ip/hostname>
      IP/name of your IPSec gateway
  conf-variable: IPSec gateway<ip/hostname>
  --id <ASCII string>
      your group name
  conf-variable: IPSec ID<ASCII string>
  --secret <ASCII string>
      your group password (cleartext)
  conf-variable: IPSec secret<ASCII string>
  --username <ASCII string>
      your username
  conf-variable: Xauth username<ASCII string>
  --password <ASCII string>
      your password (cleartext)
  conf-variable: Xauth password<ASCII string>
Use --long-help to see all options
Report bugs at https://github.com/streambinder/vpnc.git
```

### `vpnc-connect`

> 官方示例调用：`vpnc-connect --help`

```text
root@kali:~# vpnc-connect --help
Usage: vpnc-connect [--version] [--print-config] [--help] [--long-help] [options] [config files]
Options:
  --gateway <ip/hostname>
      IP/name of your IPSec gateway
  conf-variable: IPSec gateway<ip/hostname>
  --id <ASCII string>
      your group name
  conf-variable: IPSec ID<ASCII string>
  --secret <ASCII string>
      your group password (cleartext)
  conf-variable: IPSec secret<ASCII string>
  --username <ASCII string>
      your username
  conf-variable: Xauth username<ASCII string>
  --password <ASCII string>
      your password (cleartext)
  conf-variable: Xauth password<ASCII string>
Use --long-help to see all options
Report bugs at https://github.com/streambinder/vpnc.git
```

### `vpnc-disconnect`

> 官方示例调用：`vpnc-disconnect -h`

```text
root@kali:~# vpnc-disconnect -h
Usage: /usr/sbin/vpnc-disconnect
Updated on: 2026-Aug-25
 Edit this page
vopono
wapiti
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install vpnc`，再执行 `vpnc --version` 2>/dev/null || `vpnc -V`
- [ ] **2.** **读官方帮助** —— `vpnc -h`，需要细节时 `man vpnc`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: cisco-decrypt DEADBEEF...012345678 424242...7261`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/vpnc/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/vpnc/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/vpnc/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
