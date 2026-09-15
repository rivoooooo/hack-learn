# inspy

> LinkedIn enumeration tool This package contains a Python based LinkedIn enumeration tool. You will need an API key from HunterIO.

> **功能分类**：通用工具 ｜ **Kali 包**：`inspy` ｜ **官方文档**：<https://www.kali.org/tools/inspy/>

## 1. 安装

```bash
sudo apt update
sudo apt install inspy
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.0.0 |
| 架构 | all |
| 可执行命令 | `inspy` |
| 依赖 | `python3`、`python3-bs4`、`python3-requests` |
| 安装体积 | 45 KB |
| 官网 | <https://github.com/gojhonny/InSpy> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/inspy> |
| 包追踪 | <https://pkg.kali.org/pkg/inspy> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
Search LinkedIn for google employees (–empspy) with the provided wordlist of job titles (/usr/share/inspy/wordlists/title-list-large.txt).
root@kali:~# inspy --empspy /usr/share/inspy/wordlists/title-list-large.txt google

Search for technologies (–techspy) in use at the target company (cisco) using the provided list of terms (/usr/share/inspy/wordlists/tech-list-small.txt).
root@kali:~# inspy --techspy /usr/share/inspy/wordlists/tech-list-small.txt cisco
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `inspy`

官方给出的调用示例：`inspy --empspy /usr/share/inspy/wordlists/title-list-large.txt google`

```text
root@kali:~# inspy --empspy /usr/share/inspy/wordlists/title-list-large.txt google
Search for technologies (
–techspy
) in use at the target company (
cisco
) using the provided list of terms (
/usr/share/inspy/wordlists/tech-list-small.txt
).
```

### `inspy（示例）`

官方给出的调用示例：`inspy --techspy /usr/share/inspy/wordlists/tech-list-small.txt cisco`

```text
root@kali:~# inspy --techspy /usr/share/inspy/wordlists/tech-list-small.txt cisco
```

### `inspy（示例）`

官方给出的调用示例：`inspy -h`

```text
root@kali:~# inspy -h
usage: inspy [-h] [--domain DOMAIN] [--email EMAIL] [--titles [file]]
             [--html file] [--csv file] [--json file] [--xml file]
             company
InSpy - A LinkedIn enumeration tool by Jonathan Broche (@LeapSecurity),
version 3.0.0
positional arguments:
  company          Company name to use for tasks.
options:
  -h, --help       show this help message and exit
  --domain DOMAIN  Company domain to use for searching.
  --email EMAIL    Email format to create email addresses with. [Accepted
                   Formats:
[email protected]
,
[email protected]
,
[email protected]
,
[email protected]
,
[email protected]
,
[email protected]
,
[email protected]
,
[email protected]
]
  --titles [file]  Discover employees by title and/or department. Titles and
                   departments are imported from a new line delimited file.
                   [Default: title-list-small.txt]
Output Options:
  --html file      Print results in HTML file.
  --csv file       Print results in CSV format.
  --json file      Print results in JSON.
  --xml file       Print results in XML.
Updated on: 2025-Dec-09
 Edit this page
ike-scan
irpas
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install inspy`，再执行 `inspy --version` 2>/dev/null || `inspy -V`
- [ ] **2.** **读官方帮助** —— `inspy -h`，需要细节时 `man inspy`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `inspy -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/inspy/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/inspy/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/inspy/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
