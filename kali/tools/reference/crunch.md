# crunch

> Tool for creating wordlist Crunch is a wordlist generator where you can specify a standard character set or any set of characters to be used in generating the wordlists. The wordlists are created through combination and permutation of a se…

> **功能分类**：口令攻击 ｜ **Kali 包**：`crunch` ｜ **官方文档**：<https://www.kali.org/tools/crunch/>

## 1. 安装

```bash
sudo apt update
sudo apt install crunch
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.6 |
| 架构 | any |
| 可执行命令 | `crunch` |
| 依赖 | `libc6` |
| 安装体积 | 84 KB |
| 官网 | <http://sourceforge.net/projects/crunch-wordlist/> |
| 源码仓库 | <https://salsa.debian.org/debian/crunch> |
| 包追踪 | <https://pkg.kali.org/pkg/crunch> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Generate a dictionary file containing words with a minimum and maximum length of 6 (6 6) using the given characters (0123456789abcdef), saving the output to a file (-o 6chars.txt):
root@kali:~# crunch 6 6 0123456789abcdef -o 6chars.txt
Crunch will now generate the following amount of data: 117440512 bytes
112 MB
0 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 16777216
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `crunch`

> 官方示例调用：`crunch 6 6 0123456789abcdef -o 6chars.txt`

```text
root@kali:~# crunch 6 6 0123456789abcdef -o 6chars.txt
Crunch will now generate the following amount of data: 117440512 bytes
112 MB
0 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 16777216
```

### `crunch -h`

> 官方示例调用：`crunch -h`

```text
root@kali:~# crunch -h
crunch version 3.6
Crunch can create a wordlist based on criteria you specify.  The output from crunch can be sent to the screen, file, or to another program.
Usage: crunch <min> <max> [options]
where min and max are numbers
Please refer to the man page for instructions and examples on how to use crunch.
Learn more with
OffSec
Want to learn more about crunch? get access to in-depth training and hands-on labs:
PEN-210: 7.2.4. Cracking Authentication Hashes: Using Aircrack-ng with Crunch
PEN-200: 18.2.1. Linux Privilege Escalation: Inspecting User Trails
PEN-210 course
PEN-200 course
Updated on: 2025-Dec-09
 Edit this page
crowbar
cryptcat
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install crunch`，再执行 `crunch --version` 2>/dev/null || `crunch -V`
- [ ] **2.** **读官方帮助** —— `crunch -h`，需要细节时 `man crunch`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: crunch <min> <max> [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/crunch/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[crunch](../../tools/tutorials/04-口令攻击/crunch.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/crunch/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/crunch/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
