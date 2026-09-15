# gpart

> Guess PC disk partition table, find lost partitions Gpart is a tool which tries to guess the primary partition table of a PC-type disk in case the primary partition table in sector 0 is damaged, incorrect or deleted. It is also good at fin…

> **功能分类**：数字取证 ｜ **Kali 包**：`gpart` ｜ **官方文档**：<https://www.kali.org/tools/gpart/>

## 1. 安装

```bash
sudo apt update
sudo apt install gpart
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.3 |
| 架构 | any |
| 可执行命令 | `gpart` |
| 依赖 | `libc6` |
| 安装体积 | 76 KB |
| 官网 | <https://github.com/baruch/gpart> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/gpart> |
| 包追踪 | <https://pkg.kali.org/pkg/gpart> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gpart -h          # 查看用法
man gpart         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `gpart`

官方给出的调用示例：`gpart --help`

```text
root@kali:~# gpart --help
gpart: invalid option -- '-'
Usage: gpart [options] device
Options: [-b <backup MBR>][-C c,h,s][-c][-d][-E][-e][-f][-g][-h][-i]
         [-K <last sector>][-k <# of sectors>][-L][-l <log file>]
         [-n <increment>][-q][-s <sector-size>]
         [-V][-v][-W <device>][-w <module-name,weight>]
gpart v0.2.3-dev (c) 1999-2001 Michail Brzitwa <
[email protected]
>.
Guess PC-type hard disk partitions.
Options:
 -b  Save a backup of the original MBR to specified file.
 -C  Set c/h/s to be used in the scan.
 -c  Check/compare mode.
 -d  Do not start the guessing loop.
 -E  Do not try to identify extended partition tables.
 -e  Do not skip disk read errors.
 -f  Full scan.
 -g  Do not try to get the disk geometry.
 -h  Show this help.
 -i  Run interactively (ask for confirmation).
 -K  Scan only up to given sector.
 -k  Skip sectors before scan.
 -L  List available modules and their weights, then exit.
 -l  Logfile name.
 -n  Scan increment: number or 's' sector, 'h' head, 'c' cylinder.
 -q  Run quiet (however log file is written if specified).
 -s  Sector size to use (disable sector size probing).
 -V  Show version.
 -v  Verbose mode. Can be given more than once.
 -W  Write guessed primary partition table to given device or file.
 -w  Weight factor of module.
Updated on: 2025-Dec-09
 Edit this page
gowitness
gtkhash
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install gpart`，再执行 `gpart --version` 2>/dev/null || `gpart -V`
- [ ] **2.** **读官方帮助** —— `gpart -h`，需要细节时 `man gpart`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: gpart [options] device`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gpart/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gpart/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gpart/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
