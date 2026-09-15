# rarcrack

> Password cracker for rar archives This program uses a brute force algorithm to guess your encrypted compressed file’s password. This program can crack zip, 7z, and rar file passwords.

> **功能分类**：口令攻击 ｜ **Kali 包**：`rarcrack` ｜ **官方文档**：<https://www.kali.org/tools/rarcrack/>

## 1. 安装

```bash
sudo apt update
sudo apt install rarcrack
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.2 |
| 架构 | any |
| 可执行命令 | `rarcrack` |
| 依赖 | `libc6`、`libxml2-16` |
| 安装体积 | 56 KB |
| 官网 | <http://rarcrack.sourceforge.net/> |
| 源码仓库 | <https://salsa.debian.org/salvage-team/rarcrack> |
| 包追踪 | <https://pkg.kali.org/pkg/rarcrack> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
rarcrack -h          # 查看用法
man rarcrack         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rarcrack`

官方给出的调用示例：`rarcrack --help`

```text
root@kali:~# rarcrack --help
RarCrack! 0.2 by David Zoltan Kedves (
[email protected]
)
Usage:   rarcrack encrypted_archive.ext [--threads NUM] [--type rar|zip|7z]
Options: --help: show this screen.
         --type: you can specify the archive program, this needed when
                 the program couldn't detect the proper file type
         --threads: you can specify how many threads
                    will be run (default: 1)
Info:    This program supports only RAR, ZIP and 7Z encrypted archives.
         RarCrack! usually detects the archive type.
Updated on: 2025-Dec-09
 Edit this page
qsslcaudit
raven
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install rarcrack`，再执行 `rarcrack --version` 2>/dev/null || `rarcrack -V`
- [ ] **2.** **读官方帮助** —— `rarcrack -h`，需要细节时 `man rarcrack`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:   rarcrack encrypted_archive.ext [--threads NUM] [--type rar|zip|7z]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rarcrack/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rarcrack/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rarcrack/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
