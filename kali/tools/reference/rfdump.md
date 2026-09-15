# rfdump

> Tool to decode RFID tag data RFDump is a tool to decode RFID tags and show their meta information: tag ID, tag type, manufacturer etc. The user data memory of a tag can be displayed and modified using either a hex or an ASCII editor. In ad…

> **功能分类**：无线攻击 ｜ **Kali 包**：`rfdump` ｜ **官方文档**：<https://www.kali.org/tools/rfdump/>

## 1. 安装

```bash
sudo apt update
sudo apt install rfdump
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6 |
| 架构 | any |
| 可执行命令 | `rfdump` |
| 依赖 | `libc6`、`libexpat1`、`libglib2.0-0t64`、`libgtk-3-0t64` |
| 安装体积 | 251 KB |
| 官网 | <http://www.rfdump.org/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/rfdump> |
| 包追踪 | <https://pkg.kali.org/pkg/rfdump> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
rfdump -h          # 查看用法
man rfdump         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

官方给出的调用示例：`man rfdump`

```text
root@kali:~# man rfdump
RFDUMP(1)                   General Commands Manual                   RFDUMP(1)
NAME
     rfdump -- Tool to detect RFID-Tags and show their meta information
SYNOPSIS
     rfdump [-p /dev/ttyS?]  [--setupreader]  [file.xml]
DESCRIPTION
     This manual page documents briefly the rfdump command.
     This manual page was written for the Debian distribution because the orig-
     inal program does not have a manual page.
     rfdump  is a tool to detect RFID-Tags and show their meta information: Tag
     ID, Tag Type, manufacturer etc. The User-Data of a tag  can  be  displayed
     and modified using either a Hex or an ASCII editor. In addition, the inte-
     grated  cookie  feature demonstrates how easy it is for a company to abuse
     RFID technology to spy on their customers.   rfdump  works  with  the  ACG
     Multi-Tag Reader or similar card reader hardware.
OPTIONS
     -h           --help
               Show summary of options.
     -p        specify port to use
     --setupreader
               setup the card reader
FILES
     ~/.config/rfdump.ini
               rfdump configuration file
FURTHER DOCUMENTATION
     Further documentation can be found under /usr/share/doc/rfdump.
AUTHOR
     This manual page was written by Meike Reichle <
[email protected]
> for
     the  Debian  system (but may be used by others).  Permission is granted to
     copy, distribute and/or modify this document under the terms  of  the  GNU
     General  Public License, Version 2 any later version published by the Free
     Software Foundation.
     On Debian systems, the complete text of the GNU General Public License can
     be found in /usr/share/common-licenses/GPL.
                                                                      RFDUMP(1)
Updated on: 2026-May-25
 Edit this page
rfcat
rkhunter
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install rfdump`，再执行 `rfdump --version` 2>/dev/null || `rfdump -V`
- [ ] **2.** **读官方帮助** —— `rfdump -h`，需要细节时 `man rfdump`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `rfdump -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rfdump/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rfdump/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rfdump/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
