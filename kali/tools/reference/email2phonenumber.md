# email2phonenumber

> OSINT tool to obtain a target’s phone number by having their email address This package contains an OSINT tool that allows you to obtain a target’s phone number just by having their email address. This tool helps automate discovering someo…

> **功能分类**：通用工具 ｜ **Kali 包**：`email2phonenumber` ｜ **官方文档**：<https://www.kali.org/tools/email2phonenumber/>

## 1. 安装

```bash
sudo apt update
sudo apt install email2phonenumber
```

| 项目 | 内容 |
|------|------|
| 版本 | 0~git20220216 |
| 架构 | all |
| 可执行命令 | `email2phonenumber` |
| 依赖 | `python3`、`python3-bs4`、`python3-certifi`、`python3-chardet`、`python3-idna`、`python3-requests`、`python3-soupsieve`、`python3-urllib3` |
| 安装体积 | 72 KB |
| 官网 | <https://github.com/martinvigo/email2phonenumber> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/email2phonenumber> |
| 包追踪 | <https://pkg.kali.org/pkg/email2phonenumber> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
email2phonenumber -h          # 查看用法
man email2phonenumber         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `email2phonenumber`

官方给出的调用示例：`email2phonenumber -h`

```text
root@kali:~# email2phonenumber -h
usage: email2phonenumber.py [-h] {scrape,generate,bruteforce} ...
An OSINT tool to find phone numbers associated to email addresses
positional arguments:
  {scrape,generate,bruteforce}
                        commands
    scrape              scrape online services for phone number digits
    generate            generate all valid phone numbers based on NANPA's
                        public records
    bruteforce          bruteforce using online services to find the phone
                        number
options:
  -h, --help            show this help message and exit
Updated on: 2025-Dec-09
 Edit this page
eapmd5pass
enum4linux
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install email2phonenumber`，再执行 `email2phonenumber --version` 2>/dev/null || `email2phonenumber -V`
- [ ] **2.** **读官方帮助** —— `email2phonenumber -h`，需要细节时 `man email2phonenumber`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `email2phonenumber -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/email2phonenumber/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/email2phonenumber/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/email2phonenumber/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
