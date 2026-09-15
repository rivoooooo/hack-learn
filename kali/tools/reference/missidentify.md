# missidentify

> Find win32 applications Miss Identify (missidentify) is a program to find MS Windows type win32 applications. By default, it displays the filename of any executable that does not have an extension, as exe, dll, com, sys, cpl, hxs, hxi, olb…

> **功能分类**：数字取证 ｜ **Kali 包**：`missidentify` ｜ **官方文档**：<https://www.kali.org/tools/missidentify/>

## 1. 安装

```bash
sudo apt update
sudo apt install missidentify
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0 |
| 架构 | any |
| 可执行命令 | `missidentify` |
| 依赖 | `libc6` |
| 安装体积 | 47 KB |
| 官网 | <https://missidentify.sf.net> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/missidentify> |
| 包追踪 | <https://pkg.kali.org/pkg/missidentify> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
missidentify -h          # 查看用法
man missidentify         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `missidentify`

官方给出的调用示例：`missidentify -h`

```text
root@kali:~# missidentify -h
missidentify version 1.0 by Jesse Kornblum
Usage: missidentify [-Vh] [-rablv] [-s|-S len] [FILES]
-r  Recursive mode. All subdirectories are traversed
-q  Silent mode. No error messages are displayed
-a  Display all executable files regardless of extension
-b  Bare filename. No path information displayed
-l  Relative paths in filenames
-v  Verbose mode. Displays the filename for every 10th file processed
-s|-S Display strings
-V  Display version number and exit
-h  Display this help message
Updated on: 2026-Jun-17
 Edit this page
linkedin2username
myrescue
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install missidentify`，再执行 `missidentify --version` 2>/dev/null || `missidentify -V`
- [ ] **2.** **读官方帮助** —— `missidentify -h`，需要细节时 `man missidentify`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: missidentify [-Vh] [-rablv] [-s|-S len] [FILES]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/missidentify/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/missidentify/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/missidentify/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
