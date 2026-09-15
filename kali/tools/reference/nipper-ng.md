# nipper-ng

> Device security configuration review tool Nipper-ng is the next generation of nippper, and will always remain free and open source. This software will be used to make observations about the security configurations of many different device …

> **功能分类**：识别与指纹 ｜ **Kali 包**：`nipper-ng` ｜ **官方文档**：<https://www.kali.org/tools/nipper-ng/>

## 1. 安装

```bash
sudo apt update
sudo apt install nipper-ng
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.11.10 |
| 架构 | any |
| 可执行命令 | `nipper-ng`、`nipper` |
| 依赖 | `libc6`、`nipper` |
| 安装体积 | 777 KB |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/nipper-ng> |
| 包追踪 | <https://pkg.kali.org/pkg/nipper-ng> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
nipper-ng -h          # 查看用法
man nipper-ng         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `nipper`

官方给出的调用示例：`nipper --help`

```text
root@kali:~# nipper --help
                     _                           ____
               _ __ (_)_ __  _ __   ___ _ __    / ->/|
              | '_ \| | '_ \| '_ \ / _ \ '__|  /<-_/ |
              | | | | | |_) | |_) |  __/ |     |   | /
              |_| |_|_| .__/| .__/ \___|_|     |___|/
                      |_|   |_|
                           Version 0.11.10
                     http://nipper.titania.co.uk
             Copyright (C) 2006-2008 Ian Ventura-Whiting
Nipper is a  Network Infrastructure  Configuration Parser.  Nipper takes
a network infrastructure  device configuration,  processes the  file and
details security-related  issues with detailed  recommendations.  Nipper
was previous known as CiscoParse.
By default, input is retrieved from stdin and is output (in HTML format)
to stdout.
Command:
    nipper [Options]
General Options:
    --input=<file>
    Specifies a  device configuration  file to  process.  For CheckPoint
    Firewall-1 configurations, the input should be the conf directory.
    --output=<file> | --report=<file>
    Specified an output file for the report.
    --csv=<file>
    Want to output the network filtering configuration to a CSV file?.
    --version
    Displays the program version.
Example:
    The  example   below  will   process  a   Cisco   IOS-based   router
    configuration file called ios.conf  and output  the report to a file
    called report.html.
    nipper --ios-router --input=ios.conf --output=report.html
For additional help:
    --help[=<topic>]
    Show  the  online help  or show  the  additional  help on  the topic
    specified.  The help  topics  are;  GENERAL,  DEVICES,  DEVICES-ADV,
    SNMP,  REPORT, REPORT-ADV,  REPORT-SECT, REPORT-HTML,  REPORT-LATEX,
    AUDIT-ACL, AUDIT-PASS, AUDIT-ADV or CONFIG-FILE.
Updated on: 2026-Mar-02
 Edit this page
multimon-ng
openssh-ssh1
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install nipper-ng`，再执行 `nipper-ng --version` 2>/dev/null || `nipper-ng -V`
- [ ] **2.** **读官方帮助** —— `nipper-ng -h`，需要细节时 `man nipper-ng`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `nipper-ng -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/nipper-ng/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/nipper-ng/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/nipper-ng/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
