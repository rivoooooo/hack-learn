# goofile

> Command line filetype search Use this tool to search for a specific file type in a given domain.

> **功能分类**：通用工具 ｜ **Kali 包**：`goofile` ｜ **官方文档**：<https://www.kali.org/tools/goofile/>

## 1. 安装

```bash
sudo apt update
sudo apt install goofile
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6 |
| 架构 | all |
| 可执行命令 | `goofile` |
| 依赖 | `python3`、`python3-requests` |
| 安装体积 | 37 KB |
| 官网 | <https://github.com/sosukeinu/goofile> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/goofile> |
| 包追踪 | <https://pkg.kali.org/pkg/goofile> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Search for files from a domain (-d kali.org) of the PDF filetype (-f pdf):
root@kali:~# goofile -d kali.org -f pdf

-------------------------------------
|Goofile v1.5                       |
|Coded by Thomas (G13) Richards     |
|www.g13net.com                     |
|code.google.com/p/goofile          |
-------------------------------------


Searching in kali.org for pdf
========================================

Files found:
====================

docs.kali.org/pdf/kali-book-fr.pdf
docs.kali.org/pdf/kali-book-es.pdf
docs.kali.org/pdf/kali-book-id.pdf
docs.kali.org/pdf/kali-book-de.pdf
docs.kali.org/pdf/kali-book-it.pdf
docs.kali.org/pdf/kali-book-ar.pdf
docs.kali.org/pdf/kali-book-ja.pdf
docs.kali.org/pdf/kali-book-nl.pdf
docs.kali.org/pdf/kali-book-ru.pdf
docs.kali.org/pdf/kali-book-en.pdf
docs.kali.org/pdf/kali-book-pt-br.pdf
docs.kali.org/pdf/kali-book-zh-hans.pdf
docs.kali.org/pdf/kali-book-sw.pdf
docs.kali.org/pdf/articles/kali-linux-live-usb-install-en.pdf
====================
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `goofile`

> 官方示例调用：`goofile -d kali.org -f pdf`

```text
root@kali:~# goofile -d kali.org -f pdf
-------------------------------------
|Goofile v1.5                       |
|Coded by Thomas (G13) Richards     |
|www.g13net.com                     |
|code.google.com/p/goofile          |
-------------------------------------
Searching in kali.org for pdf
========================================
Files found:
====================
docs.kali.org/pdf/kali-book-fr.pdf
docs.kali.org/pdf/kali-book-es.pdf
docs.kali.org/pdf/kali-book-id.pdf
docs.kali.org/pdf/kali-book-de.pdf
docs.kali.org/pdf/kali-book-it.pdf
docs.kali.org/pdf/kali-book-ar.pdf
docs.kali.org/pdf/kali-book-ja.pdf
docs.kali.org/pdf/kali-book-nl.pdf
docs.kali.org/pdf/kali-book-ru.pdf
docs.kali.org/pdf/kali-book-en.pdf
docs.kali.org/pdf/kali-book-pt-br.pdf
docs.kali.org/pdf/kali-book-zh-hans.pdf
docs.kali.org/pdf/kali-book-sw.pdf
docs.kali.org/pdf/articles/kali-linux-live-usb-install-en.pdf
====================
```

### `goofile -h`

> 官方示例调用：`goofile -h`

```text
root@kali:~# goofile -h
usage: goofile [-h] [-d DOMAIN] [-f FILETYPE] [-k KEY] [-e ENGINE] [-q QUERY]
               [--logging LOGGING]
options:
  -h, --help            show this help message and exit
  -d, --domain DOMAIN   the domain to search - optional (ie. kali.org
  -f, --filetype FILETYPE
                        the filetype to search for - required (ie. pdf)
  -k, --key KEY         Google Custom Search Engine API key - optional
  -e, --engine ENGINE   Google Custom Search Engine ID - optional
  -q, --query QUERY     Only search for files with keyword - optional
  --logging LOGGING     Set the logging verbosity to something other than
                        "INFO" - optional
Updated on: 2025-Dec-09
 Edit this page
golang-github-binject-go-donut
google-nexus-tools
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install goofile`，再执行 `goofile --version` 2>/dev/null || `goofile -V`
- [ ] **2.** **读官方帮助** —— `goofile -h`，需要细节时 `man goofile`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `goofile -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/goofile/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/goofile/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/goofile/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
