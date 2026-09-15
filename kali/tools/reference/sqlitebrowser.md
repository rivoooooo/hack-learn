# sqlitebrowser

> GUI editor for SQLite databases SQLite Database Browser is a visual tool used to create, design and edit database files compatible with SQLite. Its interface is based on QT, and is meant to be used for users and developers that want to cre…

> **功能分类**：Web 应用 ｜ **Kali 包**：`sqlitebrowser` ｜ **官方文档**：<https://www.kali.org/tools/sqlitebrowser/>

## 1. 安装

```bash
sudo apt update
sudo apt install sqlitebrowser
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.13.1 |
| 架构 | any |
| 可执行命令 | `sqlitebrowser` |
| 依赖 | `libc6`、`libgcc-s1`、`libqcustomplot2.1`、`libqscintilla2-qt5-15`、`libqt5core5t64` |
| 安装体积 | 5.55 MB |
| 官网 | <https://sqlitebrowser.org/> |
| 源码仓库 | <https://salsa.debian.org/sqlitebrowser-team/sqlitebrowser> |
| 包追踪 | <https://pkg.kali.org/pkg/sqlitebrowser> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sqlitebrowser -h          # 查看用法
man sqlitebrowser         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

官方给出的调用示例：`man sqlitebrowser`

```text
root@kali:~# man sqlitebrowser
SQLITEBROWSER(1)            General Commands Manual            SQLITEBROWSER(1)
NAME
     sqlitebrowser - light GUI editor for SQLite databases
SYNOPSIS
     sqlitebrowser [file]
DESCRIPTION
     SQLite  Database  Browser is a visual tool used to create, design and edit
     database files compatible with SQLite. It is meant to be  used  for  users
     and developers that want to create databases, edit and search data using a
     familiar spreadsheet-like interface, without the need to learn complicated
     SQL commands.
SEE ALSO
     SQLitebrowser's home page: http://sqlitebrowser.sourceforge.net/.
AUTHOR
     sqlitebrowser  was  developed  originally by Mauricio Piacentini from Tab-
     uleiro Producoes. Icons were contributed by  Raquel  Ravanini,  also  from
     Tabuleiro.  Jens  Miltner contributed the code to support SQLite 3.x data-
     bases for the 1.2 release.
     In the spirit of the original SQLite source files,  the  authors  disclaim
     copyright  to this source code. It may be used as the basis for other pro-
     grams, public domain, open source or commercial. Do whatever you want with
     it.
     This manual page was written  by  Francois  Fevotte  <francois.fevotte@en-
     sta.org>, for the Debian project (but may be used by others).
     Permission  is granted to copy, distribute and/or modify this document un-
     der the terms of the GNU General Public License, Version 2  or  any  later
     version published by the Free Software Foundation.
     On Debian systems, the complete text of the GNU General Public License can
     be found in /usr/share/common-licenses/GPL.
                                August  4, 2007                SQLITEBROWSER(1)
Updated on: 2026-May-25
 Edit this page
spiderfoot
swaks
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sqlitebrowser`，再执行 `sqlitebrowser --version` 2>/dev/null || `sqlitebrowser -V`
- [ ] **2.** **读官方帮助** —— `sqlitebrowser -h`，需要细节时 `man sqlitebrowser`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sqlitebrowser -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sqlitebrowser/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sqlitebrowser/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sqlitebrowser/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
