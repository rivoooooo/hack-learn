# payloadsallthethings

> Collection of useful payloads and bypasses A list of useful payloads and bypasses for Web Application Security and Pentest/CTF.

> **功能分类**：通用工具 ｜ **Kali 包**：`payloadsallthethings` ｜ **官方文档**：<https://www.kali.org/tools/payloadsallthethings/>

## 1. 安装

```bash
sudo apt update
sudo apt install payloadsallthethings
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.1 |
| 架构 | any |
| 可执行命令 | `payloadsallthethings` |
| 依赖 | `kali-defaults` |
| 安装体积 | 7.52 MB |
| 官网 | <https://github.com/swisskyrepo/PayloadsAllTheThings> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/payloadsallthethings> |
| 包追踪 | <https://pkg.kali.org/pkg/payloadsallthethings> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
payloadsallthethings -h          # 查看用法
man payloadsallthethings         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `payloadsallthethings`

官方给出的调用示例：`payloadsallthethings -h`

```text
root@kali:~# payloadsallthethings -h
> payloadsallthethings ~ Collection of useful payloads and bypasses
/usr/share/payloadsallthethings
|-- AWS\ Amazon\ Bucket\ S3
|-- CRLF\ Injection
|-- CSRF\ Injection
|-- CSV\ Injection
|-- CVE\ Exploits
|-- Command\ Injection
|-- Directory\ Traversal
|-- File\ Inclusion
|-- GraphQL\ Injection
|-- Insecure\ Deserialization
|-- Insecure\ Direct\ Object\ References
|-- Insecure\ Management\ Interface
|-- Insecure\ Source\ Code\ Management
|-- JSON\ Web\ Token
|-- LDAP\ Injection
|-- LaTeX\ Injection
|-- Methodology\ and\ Resources
|-- NoSQL\ Injection
|-- OAuth
|-- Open\ Redirect
|-- SAML\ Injection
|-- SQL\ Injection
|-- Server\ Side\ Request\ Forgery
|-- Server\ Side\ Template\ Injection
|-- Type\ Juggling
|-- Upload\ Insecure\ Files
|-- Web\ Cache\ Deception
|-- Web\ Sockets
|-- XPATH\ Injection
|-- XSS\ Injection
|-- XXE\ Injection
`-- _template_vuln
Learn more with
OffSec
Want to learn more about payloadsallthethings? get access to in-depth training and hands-on labs:
WEB-200: 2.3.1. Web Application Enumeration Methodology: Common Wordlists
WEB-200 course
Updated on: 2025-Dec-09
 Edit this page
passing-the-hash
pdfcrack
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install payloadsallthethings`，再执行 `payloadsallthethings --version` 2>/dev/null || `payloadsallthethings -V`
- [ ] **2.** **读官方帮助** —— `payloadsallthethings -h`，需要细节时 `man payloadsallthethings`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `payloadsallthethings -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/payloadsallthethings/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/payloadsallthethings/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/payloadsallthethings/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
