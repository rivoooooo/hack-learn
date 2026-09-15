# sprayingtoolkit

> Scripts to make password spraying attacks against Lync/S4B, OWA & O365 A set of Python scripts/utilities that tries to make password spraying attacks against Lync/S4B & OWA a lot quicker, less painful and more efficient.

> **功能分类**：通用工具 ｜ **Kali 包**：`sprayingtoolkit` ｜ **官方文档**：<https://www.kali.org/tools/sprayingtoolkit/>

## 1. 安装

```bash
sudo apt update
sudo apt install sprayingtoolkit
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0~git20201009.68f295d |
| 架构 | all |
| 可执行命令 | `sprayingtoolkit`、`atomizer`、`spindrift` |
| 依赖 | `kali-defaults`、`mitmproxy`、`python3`、`python3-boto3`、`python3-docopt`、`python3-imapclient`、`python3-lxml`、`python3-requests`、`python3-requests-ntlm`、`python3-termcolor`、`python3-urllib3`、`atomizer` |
| 安装体积 | 79 KB |
| 官网 | <https://github.com/byt3bl33d3r/SprayingToolkit> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sprayingtoolkit> |
| 包追踪 | <https://pkg.kali.org/pkg/sprayingtoolkit> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sprayingtoolkit -h          # 查看用法
man sprayingtoolkit         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `atomizer`

官方给出的调用示例：`atomizer -h`

```text
root@kali:~# atomizer -h
Usage:
    atomizer (lync|owa|imap) <target> <password> <userfile> [--targetPort PORT] [--threads THREADS] [--debug]
    atomizer (lync|owa|imap) <target> <passwordfile> <userfile> --interval <TIME> [--gchat <URL>] [--slack <URL>] [--targetPort PORT][--threads THREADS] [--debug]
    atomizer (lync|owa|imap) <target> --csvfile CSVFILE [--user-row-name NAME] [--pass-row-name NAME] [--targetPort PORT] [--threads THREADS] [--debug]
    atomizer (lync|owa|imap) <target> --user-as-pass USERFILE [--targetPort PORT] [--threads THREADS] [--debug]
    atomizer (lync|owa|imap) <target> --recon [--debug]
    atomizer -h | --help
    atomizer -v | --version
Arguments:
    target         target domain or url
    password       password to spray
    userfile       file containing usernames (one per line)
    passwordfile   file containing passwords (one per line)
Options:
    -h, --help               show this screen
    -v, --version            show version
    -c, --csvfile CSVFILE    csv file containing usernames and passwords
    -i, --interval TIME      spray at the specified interval [format: "H:M:S"]
    -t, --threads THREADS    number of concurrent threads to use [default: 3]
    -d, --debug              enable debug output
    -p, --targetPort PORT    target port of the IMAP server (IMAP only) [default: 993]
    --recon                  only collect info, don't password spray
    --gchat URL              gchat webhook url for notification
    --slack URL              slack webhook url for notification
    --user-row-name NAME     username row title in CSV file [default: Email Address]
    --pass-row-name NAME     password row title in CSV file [default: Password]
    --user-as-pass USERFILE  use the usernames in the specified file as the password (one per line)
```

### `spindrift`

官方给出的调用示例：`spindrift -h`

```text
root@kali:~# spindrift -h
Usage:
    spindrift [<file>] [--target TARGET | --domain DOMAIN] [--format FORMAT]
Arguments:
    file    file containing names, can also read from stdin
Options:
    --target TARGET   optional domain or url to retrieve the internal domain name from OWA
    --domain DOMAIN   manually specify the domain to append to each username
    --format FORMAT   username format [default: {f}{last}]
```

### `sprayingtoolkit`

官方给出的调用示例：`sprayingtoolkit -h`

```text
root@kali:~# sprayingtoolkit -h
> sprayingtoolkit ~ Scripts to make password spraying attacks against Lync/S4B, OWA & O365
/usr/share/sprayingtoolkit
|-- aerosol.py
|-- atomizer.py
|-- core
|-- spindrift.py
`-- vaporizer.py
Updated on: 2025-Dec-09
 Edit this page
spray
spraykatz
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sprayingtoolkit`，再执行 `sprayingtoolkit --version` 2>/dev/null || `sprayingtoolkit -V`
- [ ] **2.** **读官方帮助** —— `sprayingtoolkit -h`，需要细节时 `man sprayingtoolkit`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sprayingtoolkit/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sprayingtoolkit/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sprayingtoolkit/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
