# crack

> Password guessing program (crypt() variant) Crack is program designed to quickly locate vulnerabilities in Unix (or other) password files by scanning the contents of a password file, looking for users who have misguidedly chosen a weak log…

> **功能分类**：通用工具 ｜ **Kali 包**：`crack` ｜ **官方文档**：<https://www.kali.org/tools/crack/>

## 1. 安装

```bash
sudo apt update
sudo apt install crack
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.0a |
| 架构 | any |
| 可执行命令 | `crack` |
| 依赖 | `crack-common`、`libc6`、`libcrypt1` |
| 安装体积 | 153 KB |
| 官网 | <https://alecmuffett.com/alecm/software/crack/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/crack> |
| 包追踪 | <https://pkg.kali.org/pkg/crack> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
crack -h          # 查看用法
man crack         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `Crack`

官方给出的调用示例：`Crack -h`

```text
root@kali:~# Crack -h
Crack: unrecognised argument -h
Usage: Crack [options] [bindir] [[-fmt format] files]...
Crack
Programs to break password files
```

### `Crack（示例）`

官方给出的调用示例：`Crack -h`

```text
root@kali:~# Crack -h
Crack: unrecognised argument -h
Usage: Crack [options] [bindir] [[-fmt format] files]...
Crack-Reporter
Programs to break password files
```

### `Crack-Reporter`

官方给出的调用示例：`Crack-Reporter -h`

```text
root@kali:~# Crack-Reporter -h
---- passwords cracked as of Mon Sep 14 05:24:49 EDT 2026 ----
---- errors and warnings ----
---- done ----
Crack-Reporter
Programs to break password files
```

### `Crack-Reporter（示例）`

官方给出的调用示例：`Crack-Reporter -h`

```text
root@kali:~# Crack-Reporter -h
---- passwords cracked as of Mon Sep 14 05:24:50 EDT 2026 ----
---- errors and warnings ----
---- done ----
crack-common
Password guessing program (common files of all variants)
Crack is program designed to quickly locate vulnerabilities
in Unix (or other) password files by scanning the contents
of a password file, looking for users who have misguidedly
chosen a weak login password.
This package provides the common files for the crypt() and
MD5 versions.
```

### `Crack（示例）`

官方给出的调用示例：`Crack -h`

```text
root@kali:~# Crack -h
Crack: unrecognised argument -h
Usage: Crack [options] [bindir] [[-fmt format] files]...
Crack-Reporter
Programs to break password files
```

### `Crack-Reporter（示例）`

官方给出的调用示例：`Crack-Reporter -h`

```text
root@kali:~# Crack-Reporter -h
---- passwords cracked as of Mon Sep 14 05:24:56 EDT 2026 ----
---- errors and warnings ----
---- done ----
Updated on: 2026-Aug-25
 Edit this page
cosign
crackmapexec
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install crack`，再执行 `crack --version` 2>/dev/null || `crack -V`
- [ ] **2.** **读官方帮助** —— `crack -h`，需要细节时 `man crack`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: Crack [options] [bindir] [[-fmt format] files]...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/crack/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[crackmapexec](../../tools/tutorials/08-后渗透/crackmapexec.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/crack/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/crack/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
