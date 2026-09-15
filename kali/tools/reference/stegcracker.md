# stegcracker

> Steganography brute-force tool StegCracker is steganography brute-force utility to uncover hidden data inside files.

> **功能分类**：通用工具 ｜ **Kali 包**：`stegcracker` ｜ **官方文档**：<https://www.kali.org/tools/stegcracker/>

## 1. 安装

```bash
sudo apt update
sudo apt install stegcracker
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.1.0 |
| 架构 | all |
| 可执行命令 | `stegcracker` |
| 依赖 | `python3`、`steghide` |
| 安装体积 | 50 KB |
| 官网 | <https://github.com/Paradoxis/StegCracker> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/stegcracker> |
| 包追踪 | <https://pkg.kali.org/pkg/stegcracker> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
stegcracker -h          # 查看用法
man stegcracker         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `stegcracker`

> 官方示例调用：`stegcracker -h`

```text
root@kali:~# stegcracker -h
usage: stegcracker <file> [<wordlist>]
Steganography brute-force utility to uncover hidden data inside files
positional arguments:
  file
       Input file you think contains hidden information and wish to crack.
       Note: Stegcracker only accepts the following file types: jpg, jpeg,
       bmp, wav, au
  wordlist
       Wordlist containing the one or more passwords (one password per line).
       If no password list is supplied, this will default to the rockyou.txt
       wordlist on Kali Linux.
options:
  -h, --help
       Show this help message and exit
  -o, --output OUTPUT
       Output file location, this will be the file the data will be written to
       on a successful cracked password. If no output location is specified,
       the default location will be the same filename with ".out" appended to
       the name.
  -t, --threads THREADS
       Number of concurrent threads used to crack passwords with, increasing
       this number might lead to better performance. Default: 16
  -c, --chunk-size CHUNK_SIZE
       Number of passwords loaded into memory per thread cycle. After each
       password of the chunk has been depleted a status update will be printed
       to the console with the attempted password. Default: 64
  -q, --quiet, --stfu
       Runs the program in "quiet mode", meaning no status updates or other
       output besides the cracked password will be echoed to the terminal. By
       default, all logging / error messages are printed to stderr (making
       piping to other processes easier).
  -v, --version
       Print the current version number and exit.
  -V, --verbose
       Runs the program in "verbose mode", this will print additional
       debugging information (include this output when submitting bug
       reports). Cannot be used in conjunction with the "--quiet" argument.
Updated on: 2025-Dec-09
 Edit this page
statsprocessor
stegosuite
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install stegcracker`，再执行 `stegcracker --version` 2>/dev/null || `stegcracker -V`
- [ ] **2.** **读官方帮助** —— `stegcracker -h`，需要细节时 `man stegcracker`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `stegcracker -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/stegcracker/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/stegcracker/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/stegcracker/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
