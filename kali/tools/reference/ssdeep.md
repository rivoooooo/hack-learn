# ssdeep

> Recursive piecewise hashing tool ssdeep is a tool for recursive computing and matching of Context Triggered Piecewise Hashing (aka Fuzzy Hashing). Fuzzy hashing is a method for comparing similar but not identical files. This tool can be us…

> **功能分类**：数字取证 ｜ **Kali 包**：`ssdeep` ｜ **官方文档**：<https://www.kali.org/tools/ssdeep/>

## 1. 安装

```bash
sudo apt update
sudo apt install ssdeep
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.14.1 |
| 架构 | any |
| 可执行命令 | `libfuzzy-dev`、`libfuzzy2`、`ssdeep` |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6` |
| 安装体积 | 83 KB |
| 官网 | <https://github.com/ssdeep-project/ssdeep> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/ssdeep> |
| 包追踪 | <https://pkg.kali.org/pkg/ssdeep> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libfuzzy-dev -h          # 查看用法
man libfuzzy-dev         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ssdeep`

官方给出的调用示例：`ssdeep -h`

```text
root@kali:~# ssdeep -h
ssdeep version 2.14.1 by Jesse Kornblum and the ssdeep Project
For copyright information, see man page or README.TXT.
Usage: ssdeep [-m file] [-k file] [-dpgvrsblcxa] [-t val] [-h|-V] [FILES]
-m - Match FILES against known hashes in file
-k - Match signatures in FILES against signatures in file
-d - Directory mode, compare all files in a directory
-p - Pretty matching mode. Similar to -d but includes all matches
-g - Cluster matches together
-v - Verbose mode. Displays filename as its being processed
-r - Recursive mode
-s - Silent mode; all errors are suppressed
-b - Uses only the bare name of files; all path information omitted
-l - Uses relative paths for filenames
-c - Prints output in CSV format
-x - Compare FILES as signature files
-a - Display all matches, regardless of score
-t - Only displays matches above the given threshold
-h - Display this help message
-V - Display version number and exit
Updated on: 2026-Mar-02
 Edit this page
snmpenum
sublist3r
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ssdeep`，再执行 `libfuzzy-dev --version` 2>/dev/null || `libfuzzy-dev -V`
- [ ] **2.** **读官方帮助** —— `libfuzzy-dev -h`，需要细节时 `man libfuzzy-dev`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ssdeep [-m file] [-k file] [-dpgvrsblcxa] [-t val] [-h|-V] [FILES]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ssdeep/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ssdeep/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ssdeep/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
