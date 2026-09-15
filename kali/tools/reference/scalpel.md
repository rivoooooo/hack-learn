# scalpel

> Fast filesystem-independent file recovery scalpel is a fast file carver that reads a database of header and footer definitions and extracts matching files from a set of image files or raw device files. scalpel is filesystem-independent and…

> **功能分类**：数字取证 ｜ **Kali 包**：`scalpel` ｜ **官方文档**：<https://www.kali.org/tools/scalpel/>

## 1. 安装

```bash
sudo apt update
sudo apt install scalpel
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.60 |
| 架构 | any |
| 可执行命令 | `scalpel` |
| 依赖 | `libc6` |
| 安装体积 | 89 KB |
| 官网 | <https://github.com/nolaforensix/scalpel-1.60> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/scalpel> |
| 包追踪 | <https://pkg.kali.org/pkg/scalpel> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
scalpel -h          # 查看用法
man scalpel         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `scalpel`

> 官方示例调用：`scalpel -h`

```text
root@kali:~# scalpel -h
Scalpel version 1.60
Written by Golden G. Richard III, based on Foremost 0.69.
Carves files from a disk image based on file headers and footers.
Usage: scalpel [-b] [-c <config file>] [-d] [-h|V] [-i <file>]
                 [-m blocksize] [-n] [-o <outputdir>] [-O num] [-q clustersize]
                 [-r] [-s num] [-t <blockmap file>] [-u] [-v]
                 <imgfile> [<imgfile>] ...
-b  Carve files even if defined footers aren't discovered within
    maximum carve size for file type [foremost 0.69 compat mode].
-c  Choose configuration file.
-d  Generate header/footer database; will bypass certain optimizations
    and discover all footers, so performance suffers.  Doesn't affect
    the set of files carved.  **EXPERIMENTAL**
-h  Print this help message and exit.
-i  Read names of disk images from specified file.
-m  Generate/update carve coverage blockmap file.  The first 32bit
    unsigned int in the file identifies the block size. Thereafter
    each 32bit unsigned int entry in the blockmap file corresponds
    to one block in the image file.  Each entry counts how many
    carved files contain this block. Requires more memory and
    disk.  **EXPERIMENTAL**
-n  Don't add extensions to extracted files.
-o  Set output directory for carved files.
-O  Don't organize carved files by type. Default is to organize carved files
    into subdirectories.
-p  Perform image file preview; audit log indicates which files
    would have been carved, but no files are actually carved.
-q  Carve only when header is cluster-aligned.
-r  Find only first of overlapping headers/footers [foremost 0.69 compat mode].
-s  Skip n bytes in each disk image before carving.
-t  Set directory for coverage blockmap.  **EXPERIMENTAL**
-u  Use carve coverage blockmap when carving.  Carve only sections
    of the image whose entries in the blockmap are 0.  These areas
    are treated as contiguous regions.  **EXPERIMENTAL**
-V  Print copyright information and exit.
-v  Verbose mode.
Updated on: 2025-Dec-09
 Edit this page
samdump2
scrounge-ntfs
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install scalpel`，再执行 `scalpel --version` 2>/dev/null || `scalpel -V`
- [ ] **2.** **读官方帮助** —— `scalpel -h`，需要细节时 `man scalpel`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: scalpel [-b] [-c <config file>] [-d] [-h|V] [-i <file>]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/scalpel/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[scalpel](../../tools/tutorials/09-数字取证/scalpel.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/scalpel/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/scalpel/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
