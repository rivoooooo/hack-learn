# seclists

> Collection of multiple types of security lists SecLists is a collection of multiple types of lists used during security assessments. List types include usernames, passwords, URLs, sensitive data grep strings, fuzzing payloads, and many mor…

> **功能分类**：口令攻击 ｜ **Kali 包**：`seclists` ｜ **官方文档**：<https://www.kali.org/tools/seclists/>

## 1. 安装

```bash
sudo apt update
sudo apt install seclists
```

| 项目 | 内容 |
|------|------|
| 版本 | 2025.3 |
| 架构 | all |
| 可执行命令 | `seclists` |
| 依赖 | `kali-defaults` |
| 安装体积 | 1.80 GB |
| 官网 | <https://github.com/danielmiessler/SecLists> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/seclists> |
| 包追踪 | <https://pkg.kali.org/pkg/seclists> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
root@kali:~# ls -lh /usr/share/seclists/
total 40K
drwxr-xr-x  6 root root 4.0K Mar 23 09:56 Discovery
drwxr-xr-x  3 root root 4.0K Mar 23 09:56 Fuzzing
drwxr-xr-x  2 root root 4.0K Mar 23 09:56 IOCs
drwxr-xr-x  2 root root 4.0K Mar 23 09:56 Miscellaneous
drwxr-xr-x 11 root root 4.0K Mar 23 09:56 Passwords
drwxr-xr-x  2 root root 4.0K Mar 23 09:56 Pattern-Matching
drwxr-xr-x  7 root root 4.0K Mar 23 09:56 Payloads
-rwxr-xr-x  1 root root 3.5K Mar  7 16:02 README.md
drwxr-xr-x  4 root root 4.0K Mar 23 09:56 Usernames
drwxr-xr-x  7 root root 4.0K Mar 23 09:56 Web-Shells
root@kali:~#
root@kali:~# tree -d /usr/share/seclists/
/usr/share/seclists/
├── Discovery
│   ├── DNS
│   ├── Infrastructure
│   ├── SNMP
│   └── Web-Content
│       ├── CMS
│       ├── SVNDigger
│       │   ├── cat
│       │   │   ├── Conf
│       │   │   ├── Database
│       │   │   ├── Language
│       │   │   └── Project
│       │   └── context
│       ├── URLs
│       └── Web-Services
├── Fuzzing
│   └── Polyglots
├── IOCs
├── Miscellaneous
├── Passwords
│   ├── Common-Credentials
│   ├── Cracked-Hashes
│   ├── Default-Credentials
│   ├── Honeypot-Captures
│   ├── Leaked-Databases
│   ├── Malware
│   ├── Permutations
│   ├── Software
│   └── WiFi-WPA
├── Pattern-Matching
├── Payloads
│   ├── Anti-Virus
│   ├── File-Names
│   ├── Images
│   ├── PHPInfo
│   └── Zip-Bombs
├── Usernames
│   ├── Honeypot-Captures
│   └── Names
└── Web-Shells
    ├── FuzzDB
    ├── JSP
    ├── laudanum-0.8
    │   ├── asp
    │   ├── aspx
    │   ├── cfm
    │   ├── jsp
    │   │   └── warfiles
    │   │       ├── META-INF
    │   │       └── WEB-INF
    │   └── php
    ├── PHP
    └── WordPress

53 directories
root@kali:~#
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ls`

> 官方示例调用：`ls -lh /usr/share/seclists/`

```text
root@kali:~# ls -lh /usr/share/seclists/
total 40K
drwxr-xr-x  6 root root 4.0K Mar 23 09:56 Discovery
drwxr-xr-x  3 root root 4.0K Mar 23 09:56 Fuzzing
drwxr-xr-x  2 root root 4.0K Mar 23 09:56 IOCs
drwxr-xr-x  2 root root 4.0K Mar 23 09:56 Miscellaneous
drwxr-xr-x 11 root root 4.0K Mar 23 09:56 Passwords
drwxr-xr-x  2 root root 4.0K Mar 23 09:56 Pattern-Matching
drwxr-xr-x  7 root root 4.0K Mar 23 09:56 Payloads
-rwxr-xr-x  1 root root 3.5K Mar  7 16:02 README.md
drwxr-xr-x  4 root root 4.0K Mar 23 09:56 Usernames
drwxr-xr-x  7 root root 4.0K Mar 23 09:56 Web-Shells
```

### ``

```text
root@kali:~#
```

### `tree`

> 官方示例调用：`tree -d /usr/share/seclists/`

```text
root@kali:~# tree -d /usr/share/seclists/
/usr/share/seclists/
├── Discovery
│   ├── DNS
│   ├── Infrastructure
│   ├── SNMP
│   └── Web-Content
│       ├── CMS
│       ├── SVNDigger
│       │   ├── cat
│       │   │   ├── Conf
│       │   │   ├── Database
│       │   │   ├── Language
│       │   │   └── Project
│       │   └── context
│       ├── URLs
│       └── Web-Services
├── Fuzzing
│   └── Polyglots
├── IOCs
├── Miscellaneous
├── Passwords
│   ├── Common-Credentials
│   ├── Cracked-Hashes
│   ├── Default-Credentials
│   ├── Honeypot-Captures
│   ├── Leaked-Databases
│   ├── Malware
│   ├── Permutations
│   ├── Software
│   └── WiFi-WPA
├── Pattern-Matching
├── Payloads
│   ├── Anti-Virus
│   ├── File-Names
│   ├── Images
│   ├── PHPInfo
│   └── Zip-Bombs
├── Usernames
│   ├── Honeypot-Captures
│   └── Names
└── Web-Shells
    ├── FuzzDB
    ├── JSP
    ├── laudanum-0.8
    │   ├── asp
    │   ├── aspx
    │   ├── cfm
    │   ├── jsp
    │   │   └── warfiles
    │   │       ├── META-INF
    │   │       └── WEB-INF
    │   └── php
    ├── PHP
    └── WordPress
53 directories
```

### ``

```text
root@kali:~#
```

### `seclists`

> 官方示例调用：`seclists -h`

```text
root@kali:~# seclists -h
> seclists ~ Collection of multiple types of security lists
/usr/share/seclists
|-- Discovery
|-- Fuzzing
|-- Miscellaneous
|-- Passwords
|-- Pattern-Matching
|-- Payloads
|-- Usernames
`-- Web-Shells
Learn more with
OffSec
Want to learn more about seclists? get access to in-depth training and hands-on labs:
WEB-200: 2.3.1. Web Application Enumeration Methodology: Common Wordlists
PEN-200: 6.4.1. Information Gathering: DNS Enumeration
PEN-200 course
WEB-200 course
Updated on: 2026-Mar-02
 Edit this page
scapy
sendemail
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install seclists`，再执行 `seclists --version` 2>/dev/null || `seclists -V`
- [ ] **2.** **读官方帮助** —— `seclists -h`，需要细节时 `man seclists`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `seclists -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/seclists/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/persistence.md`](../../tools/by-attack/persistence.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/seclists/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/seclists/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
