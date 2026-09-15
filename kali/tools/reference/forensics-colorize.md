# forensics-colorize

> Show differences between files using color graphics forensics-colorize is a set of tools to visually compare large files, as filesystem images, creating graphics of them. It is intuitive because the produced graphics provide a quick and pe…

> **功能分类**：数字取证 ｜ **Kali 包**：`forensics-colorize` ｜ **官方文档**：<https://www.kali.org/tools/forensics-colorize/>

## 1. 安装

```bash
sudo apt update
sudo apt install forensics-colorize
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1 |
| 架构 | any |
| 可执行命令 | `forensics-colorize`、`colorize`、`filecompare` |
| 依赖 | `libc6`、`colorize` |
| 安装体积 | 2.05 MB |
| 官网 | <https://github.com/jessek/colorize> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/forensics-colorize> |
| 包追踪 | <https://pkg.kali.org/pkg/forensics-colorize> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
forensics-colorize -h          # 查看用法
man forensics-colorize         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `colorize`

官方给出的调用示例：`colorize -h`

```text
root@kali:~# colorize -h
colorize by Jesse Kornblum version 1.1
$ colorize [-h|-V] [-w <num>] [-ovd] FILES
-d  - Change direction data flows, defaults to down or right
-o  - Change image orientation, defaults to vertical
-v  - Verbose mode
-w  - Set output image width, defaults to 100
-V  - Display version number and exit
-h  - Display this help message and exit
```

### `filecompare`

官方给出的调用示例：`filecompare -h`

```text
root@kali:~# filecompare -h
filecompare version 1.1 by Jesse Kornblum
Usage: filecompare [-b size[bkmgpe]] [-Vh] FILE1 FILE2
-b  Set block size with optional suffix b,k,m,g,p, or e
    Note that the program will output at least one complete block
    Make sure you have enough disk space!
-t  Use transitional colors instead of default red or green
-V  Display version number and exit
-h  Display this help message
Updated on: 2025-Dec-09
 Edit this page
forensic-artifacts
fping
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install forensics-colorize`，再执行 `forensics-colorize --version` 2>/dev/null || `forensics-colorize -V`
- [ ] **2.** **读官方帮助** —— `forensics-colorize -h`，需要细节时 `man forensics-colorize`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: filecompare [-b size[bkmgpe]] [-Vh] FILE1 FILE2`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/forensics-colorize/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/forensics-colorize/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/forensics-colorize/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
