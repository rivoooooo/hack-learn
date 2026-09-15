# ncurses-hexedit

> Edit files/disks in hex, ASCII and EBCDIC Hexedit is a file editor which allows editing and viewing a file in hexadecimal, along with its ASCII or EBCDIC text equivalent. Standard editing features include insert, delete, search (text or by…

> **功能分类**：通用工具 ｜ **Kali 包**：`ncurses-hexedit` ｜ **官方文档**：<https://www.kali.org/tools/ncurses-hexedit/>

## 1. 安装

```bash
sudo apt update
sudo apt install ncurses-hexedit
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.9.7 |
| 架构 | any |
| 可执行命令 | `ncurses-hexedit`、`hexeditor` |
| 依赖 | `libc6`、`libncurses6`、`libtinfo6`、`hexeditor` |
| 安装体积 | 130 KB |
| 官网 | <http://www.rogoyski.com/adam/programs/hexedit/> |
| 源码仓库 | <https://salsa.debian.org/debian/ncurses-hexedit> |
| 包追踪 | <https://pkg.kali.org/pkg/ncurses-hexedit> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ncurses-hexedit -h          # 查看用法
man ncurses-hexedit         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hexeditor`

> 官方示例调用：`hexeditor -h`

```text
root@kali:~# hexeditor -h
[N]Curses Hexedit 0.9.7 by Adam Rogoyski <
[email protected]
>
Copyright (C) 1998, 1999 Adam Rogoyski
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.
Usage: hexeditor [options] [file]
Options:
  -h, --help              Print this message and exit.
  -8, --highbit           Print high order 8-bit text.
  -a, --alltext           Print all text characters.
  -b, --buffer            Buffer the entire file in memory.
                            Much faster and enables insert/delete.
  -d, --disk              Edit a fixed disk, i.e. /dev/hda (Read-only)
  -f, --force             Force editing of disk.
                            Needed to write to disks.
  -n, --nocolor           Force Gray scale, no colors.
  -q, --quiet             Quiet Mode, No annoying beeping
  -r, --readonly          Do no modifying of the file.
  -v, --version           Print the version number and exit.
Updated on: 2025-Dec-09
 Edit this page
ncrack
net-tools
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ncurses-hexedit`，再执行 `ncurses-hexedit --version` 2>/dev/null || `ncurses-hexedit -V`
- [ ] **2.** **读官方帮助** —— `ncurses-hexedit -h`，需要细节时 `man ncurses-hexedit`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: hexeditor [options] [file]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ncurses-hexedit/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ncurses-hexedit/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ncurses-hexedit/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
