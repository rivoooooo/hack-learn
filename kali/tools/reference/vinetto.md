# vinetto

> Forensics tool to examine Thumbs.db files vinetto is a console program to extract thumbnail pictures and their metadata from Thumbs.db files, that are generated under Microsoft Windows. vinetto can help *nix-based forensics investigators t…

> **功能分类**：数字取证 ｜ **Kali 包**：`vinetto` ｜ **官方文档**：<https://www.kali.org/tools/vinetto/>

## 1. 安装

```bash
sudo apt update
sudo apt install vinetto
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.9.15 |
| 架构 | any |
| 可执行命令 | `vinetto` |
| 依赖 | `python3`、`python3-pil` |
| 安装体积 | 234 KB |
| 官网 | <https://github.com/AtesComp/Vinetto> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/vinetto> |
| 包追踪 | <https://pkg.kali.org/pkg/vinetto> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
vinetto -h          # 查看用法
man vinetto         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `vinetto`

官方给出的调用示例：`vinetto -h`

```text
root@kali:~# vinetto -h
Vinetto: Version 0.9.15
usage: vinetto [-h] [-e EDBFILE] [-H] [-m [{f,d,r,a}]] [--md5] [--nomd5]
               [-o DIR] [-q] [-s] [-U] [-v] [--version]
               [infile]
Vinetto.py - The Thumbnail File Parser
positional arguments:
  infile                depending on operating mode (see mode option), either a location
                        to a thumbnail file ("Thumb.db" or similar) or a directory
options:
  -h, -?, --help        show this help message and exit, use -v for more details
  -e, --edb EDBFILE     examine EDBFILE (Extensible Storage Engine Database) for
                        original thumbnail filenames
                        NOTE: -e without an INFILE explores EDBFILE extracted data
                        NOTE: Automatic mode will attempt to use ESEDB without -e
  -H, --htmlrep         write html report to DIR (requires option -o)
  -m, --mode [{f,d,r,a}]
                        operating mode: "f", "d", "r", or "a"
                          where "f" indicates single file processing (default)
                                "d" indicates directory processing
                                "r" indicates recursive directory processing from a
                                      starting directory
                                "a" indicates automatic processing using well known
                                      directories starting from a base directory
  --md5                 force the MD5 hash value calculation for an input file
                        Normally, the MD5 is calculated when a file is less than
                        0.5 GiB in size
                        NOTE: --nomd5 overrides --md5
  --nomd5               skip the MD5 hash value calculation for an input file
  -o, --outdir DIR      write thumbnails to DIR
                        NOTE: -o requires INFILE
  -q, --quiet           quiet output: Errors only
                        NOTE: -v overrides -q
  -s, --symlinks        create symlink from the the image realname to the numbered name
                        in DIR/.thumbs (requires option -o)
                        NOTE: A Catalog containing the realname must exist for this
                              option to produce results OR a Windows.edb must be given
                              (-e) to find and extract possible file names
  -U, --utf8            use utf8 encodings
  -v, --verbose         verbose output, each use increments output level: 0 (Standard)
                        1 (Verbose), 2 (Enhanced), 3 (Full)
  --version             show program's version number and exit
--- Vinetto.py 0.9.15 ---
Based on the original Vinetto by Michel Roukine
Author: Keven L. Ates
Vinetto.py is open source software
  See: https://github.com/AtesComp/Vinetto
For more detailed help notes, use -v
Updated on: 2026-May-25
 Edit this page
unhide.rb
wafw00f
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install vinetto`，再执行 `vinetto --version` 2>/dev/null || `vinetto -V`
- [ ] **2.** **读官方帮助** —— `vinetto -h`，需要细节时 `man vinetto`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `vinetto -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/vinetto/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/vinetto/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/vinetto/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
