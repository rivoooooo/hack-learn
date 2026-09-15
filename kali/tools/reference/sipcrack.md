# sipcrack

> SIP login dumper/cracker The tools contained in this package offer support for pcap files, wordlists and many more to extract all needed information and bruteforce the passwords for the sniffed accounts. sipdump - Dump SIP digest authentic…

> **功能分类**：口令攻击 ｜ **Kali 包**：`sipcrack` ｜ **官方文档**：<https://www.kali.org/tools/sipcrack/>

## 1. 安装

```bash
sudo apt update
sudo apt install sipcrack
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.2 |
| 架构 | any |
| 可执行命令 | `sipcrack`、`sipdump` |
| 依赖 | `libc6`、`libpcap0.8t64`、`libssl3t64` |
| 安装体积 | 72 KB |
| 官网 | <http://www.remote-exploit.org/codes_sipcrack.html> |
| 源码仓库 | <https://salsa.debian.org/debian/sipcrack> |
| 包追踪 | <https://pkg.kali.org/pkg/sipcrack> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sipcrack -h          # 查看用法
man sipcrack         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sipcrack`

官方给出的调用示例：`sipcrack -h`

```text
root@kali:~# sipcrack -h
SIPcrack 0.2
----------------------------------------
Usage: sipcrack [OPTIONS] [ -s | -w <wordlist> ] <dump file>
       <dump file>   = file containing logins sniffed by SIPdump
       Options:
       -s            = use stdin for passwords
       -w wordlist   = file containing all passwords to try
       -p num        = print cracking process every n passwords (for -w)
                       (ATTENTION: slows down heavily)
* Invalid arguments
```

### `sipdump`

官方给出的调用示例：`sipdump -h`

```text
root@kali:~# sipdump -h
SIPdump 0.2
---------------------------------------
Usage: sipdump [OPTIONS] <dump file>
       <dump file>    = file where captured logins will be written to
       Options:
       -i <interface> = interface to listen on
       -p <file>      = use pcap data file
       -m             = enter login data manually
       -f "<filter>"  = set libpcap filter
* Invalid arguments
Updated on: 2025-Dec-09
 Edit this page
shellnoob
sipp
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sipcrack`，再执行 `sipcrack --version` 2>/dev/null || `sipcrack -V`
- [ ] **2.** **读官方帮助** —— `sipcrack -h`，需要细节时 `man sipcrack`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sipcrack [OPTIONS] [ -s | -w <wordlist> ] <dump file>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sipcrack/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sipcrack/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sipcrack/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
