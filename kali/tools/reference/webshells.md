# webshells

> Collection of webshells A collection of webshells for ASP, ASPX, CFM, JSP, Perl, and PHP servers.

> **功能分类**：Web 应用 ｜ **Kali 包**：`webshells` ｜ **官方文档**：<https://www.kali.org/tools/webshells/>

## 1. 安装

```bash
sudo apt update
sudo apt install webshells
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1 |
| 架构 | all |
| 可执行命令 | `webshells` |
| 依赖 | `kali-defaults` |
| 安装体积 | 71 KB |
| 官网 | <https://www.kali.org> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/webshells> |
| 包追踪 | <https://pkg.kali.org/pkg/webshells> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
root@kali:~# tree /usr/share/webshells/
/usr/share/webshells/
├── asp
│   ├── cmd-asp-5.1.asp
│   └── cmdasp.asp
├── aspx
│   └── cmdasp.aspx
├── cfm
│   └── cfexec.cfm
├── jsp
│   ├── cmdjsp.jsp
│   └── jsp-reverse.jsp
├── perl
│   ├── perlcmd.cgi
│   └── perl-reverse-shell.pl
└── php
    ├── findsock.c
    ├── php-backdoor.php
    ├── php-findsock-shell.php
    ├── php-reverse-shell.php
    ├── qsd-php-backdoor.php
    └── simple-backdoor.php

6 directories, 14 files
root@kali:~#
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tree`

> 官方示例调用：`tree /usr/share/webshells/`

```text
root@kali:~# tree /usr/share/webshells/
/usr/share/webshells/
├── asp
│   ├── cmd-asp-5.1.asp
│   └── cmdasp.asp
├── aspx
│   └── cmdasp.aspx
├── cfm
│   └── cfexec.cfm
├── jsp
│   ├── cmdjsp.jsp
│   └── jsp-reverse.jsp
├── perl
│   ├── perlcmd.cgi
│   └── perl-reverse-shell.pl
└── php
    ├── findsock.c
    ├── php-backdoor.php
    ├── php-findsock-shell.php
    ├── php-reverse-shell.php
    ├── qsd-php-backdoor.php
    └── simple-backdoor.php
6 directories, 14 files
```

### ``

```text
root@kali:~#
```

### `webshells`

> 官方示例调用：`webshells -h`

```text
root@kali:~# webshells -h
> webshells ~ Collection of webshells
/usr/share/webshells
|-- asp
|-- aspx
|-- cfm
|-- jsp
|-- laudanum -> /usr/share/laudanum
|-- perl
|-- php
`-- seclists -> /usr/share/seclists/Web-Shells
Learn more with
OffSec
Want to learn more about webshells? get access to in-depth training and hands-on labs:
PEN-200: 9. Common Web Application Attacks
WEB-200: 2.4.4. Web Application Enumeration Methodology: Web Shells
PEN-200 course
WEB-200 course
Updated on: 2025-Dec-09
 Edit this page
webacoo
weevely
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install webshells`，再执行 `webshells --version` 2>/dev/null || `webshells -V`
- [ ] **2.** **读官方帮助** —— `webshells -h`，需要细节时 `man webshells`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `webshells -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/webshells/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/persistence.md`](../../tools/by-attack/persistence.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/webshells/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/webshells/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
