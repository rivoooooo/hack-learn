# cabextract

> Microsoft Cabinet file unpacker Cabextract is a program which unpacks cabinet (.cab) files, which are a form of archive Microsoft uses to distribute their software and things like Windows Font Packs.

> **功能分类**：数字取证 ｜ **Kali 包**：`cabextract` ｜ **官方文档**：<https://www.kali.org/tools/cabextract/>

## 1. 安装

```bash
sudo apt update
sudo apt install cabextract
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.11 |
| 架构 | any |
| 可执行命令 | `cabextract` |
| 依赖 | `libc6`、`libmspack0t64` |
| 安装体积 | 83 KB |
| 包追踪 | <https://pkg.kali.org/pkg/cabextract> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
cabextract -h          # 查看用法
man cabextract         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cabextract`

官方给出的调用示例：`cabextract -h`

```text
root@kali:~# cabextract -h
Usage: cabextract [options] [-d dir] <cabinet file(s)>
This will extract all files from a cabinet or executable cabinet.
For multi-part cabinets, only specify the first file in the set.
Options:
  -v   --version       print version / list cabinet
  -h   --help          show this help page
  -l   --list          list contents of cabinet
  -t   --test          test cabinet integrity
  -q   --quiet         only print errors and warnings
  -L   --lowercase     make filenames lowercase
  -f   --fix           salvage as much as possible from corrupted cabinets
  -i   --interactive   prompt whether to overwrite existing files
  -n   --no-overwrite  don't overwrite (skip) existing files
  -k   --keep-symlinks follow symlinked files/dirs when extracting
  -p   --pipe          pipe extracted files to stdout
  -s   --single        restrict search to cabs on the command line
  -F   --filter        extract only files that match the given pattern
  -e   --encoding      assume non-UTF8 filenames have the given encoding
  -d   --directory     extract all files to the given directory
cabextract 1.11 (C) 2000-2023 Stuart Caie <
[email protected]
>
This is free software with ABSOLUTELY NO WARRANTY.
Updated on: 2025-Dec-09
 Edit this page
bully
certgraph
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cabextract`，再执行 `cabextract --version` 2>/dev/null || `cabextract -V`
- [ ] **2.** **读官方帮助** —— `cabextract -h`，需要细节时 `man cabextract`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: cabextract [options] [-d dir] <cabinet file(s)>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cabextract/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cabextract/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cabextract/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
