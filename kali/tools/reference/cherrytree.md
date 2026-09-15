# cherrytree

> Hierarchical note taking application CherryTree is a hierarchical note taking application, featuring rich text, syntax highlighting, images handling, hyperlinks, import/export with support for multiple formats, support for multiple languag…

> **功能分类**：通用工具 ｜ **Kali 包**：`cherrytree` ｜ **官方文档**：<https://www.kali.org/tools/cherrytree/>

## 1. 安装

```bash
sudo apt update
sudo apt install cherrytree
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.2.0 |
| 架构 | any |
| 可执行命令 | `cherrytree` |
| 依赖 | `desktop-file-utils`、`libatkmm-1.6-1v5`、`libc6`、`libcairo2`、`libcairomm-1.0-1v5`、`libcurl4t64`、`libfmt10`、`libfribidi0`、`libgcc-s1`、`libglib2.0-0t64`、`libglibmm-2.4-1t64`、`libgspell-1-3` 等 |
| 安装体积 | 11.00 MB |
| 官网 | <https://www.giuspen.net/cherrytree/> |
| 源码仓库 | <https://salsa.debian.org/debian/cherrytree> |
| 包追踪 | <https://pkg.kali.org/pkg/cherrytree> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Screenshots
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

官方给出的调用示例：`man cherrytree`

```text
root@kali:~# man cherrytree
CHERRYTREE(1)               General Commands Manual               CHERRYTREE(1)
NAME
     cherrytree - a hierarchical note taking application
SYNOPSIS
     cherrytree  [-V]  [-N]  [filepath  [-n  nodename]  [-a anchorname] [-x ex-
     port_to_html_dir] [-t export_to_txt_dir] [-p export_to_pdf_path] [-P pass-
     word] [-w] [-s]]
DESCRIPTION
     cherrytree is a hierarchical note taking application, featuring rich text,
     syntax highlighting, images handling, hyperlinks, import/export with  sup-
     port for multiple formats, support for multiple languages, and more.
AUTHOR
     cherrytree  was written by Giuseppe Penone <
[email protected]
> and Evgenii
     Gurianov <https://github.com/txe>.
     This manual page was written by  Vincent  Cheng  <
[email protected]
>,
     for the Debian project (and may be used by others).
cherrytree 0.99.49               September 2022                   CHERRYTREE(1)
Learn more with
OffSec
Want to learn more about cherrytree? get access to in-depth training and hands-on labs:
PEN-200: 5.1.4. Report Writing for Penetration Testers: Choosing the Right Note-Taking Tool
PEN-200 course
Updated on: 2026-May-25
 Edit this page
btscanner
chntpw
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cherrytree`，再执行 `cherrytree --version` 2>/dev/null || `cherrytree -V`
- [ ] **2.** **读官方帮助** —— `cherrytree -h`，需要细节时 `man cherrytree`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `cherrytree -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cherrytree/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[cherrytree](../../tools/tutorials/11-社会工程与报告/cherrytree.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cherrytree/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cherrytree/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
