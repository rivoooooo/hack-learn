# whois

> Intelligent WHOIS client This package provides a commandline client for the WHOIS (RFC 3912) protocol, which queries online servers for information such as contact details for domains and IP address assignments. It can intelligently select…

> **功能分类**：识别与指纹 ｜ **Kali 包**：`whois` ｜ **官方文档**：<https://www.kali.org/tools/whois/>

## 1. 安装

```bash
sudo apt update
sudo apt install whois
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.6.6 |
| 架构 | any |
| 可执行命令 | `whois`、`mkpasswd` |
| 依赖 | `libc6`、`libcrypt1`、`libidn2-0`、`mkpasswd` |
| 安装体积 | 384 KB |
| 源码仓库 | <https://salsa.debian.org/md/whois> |
| 包追踪 | <https://pkg.kali.org/pkg/whois> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
whois -h          # 查看用法
man whois         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `mkpasswd`

> 官方示例调用：`mkpasswd -h`

```text
root@kali:~# mkpasswd -h
Usage: mkpasswd [OPTIONS]... [PASSWORD [SALT]]
Crypts the PASSWORD using crypt(3).
      -m, --method=TYPE     select method TYPE
      -5                    like --method=md5crypt
      -S, --salt=SALT       use the specified SALT
      -R, --rounds=NUMBER   use the specified NUMBER of rounds
      -P, --password-fd=NUM read the password from file descriptor NUM
                            instead of /dev/tty
      -s, --stdin           like --password-fd=0
      -h, --help            display this help and exit
      -V, --version         output version information and exit
If PASSWORD is missing then it is asked interactively.
If no SALT is specified, a random one is generated.
If TYPE is 'help', available methods are printed.
Report bugs to <
[email protected]
>.
```

### `whois`

> 官方示例调用：`whois --help`

```text
root@kali:~# whois --help
Usage: whois [OPTION]... OBJECT...
-h HOST, --host HOST   connect to server HOST
-p PORT, --port PORT   connect to PORT
-I                     query whois.iana.org and follow its referral
-H                     hide legal disclaimers
      --verbose        explain what is being done
      --no-recursion   disable recursion from registry to registrar servers
      --help           display this help and exit
      --version        output version information and exit
These flags are supported by whois.ripe.net and some RIPE-like servers:
-l                     find the one level less specific match
-L                     find all levels less specific matches
-m                     find all one level more specific matches
-M                     find all levels of more specific matches
-c                     find the smallest match containing a mnt-irt attribute
-x                     exact match
-b                     return brief IP address ranges with abuse contact
-B                     turn off object filtering (show email addresses)
-G                     turn off grouping of associated objects
-d                     return DNS reverse delegation objects too
-i ATTR[,ATTR]...      do an inverse look-up for specified ATTRibutes
-T TYPE[,TYPE]...      only look for objects of TYPE
-K                     only primary keys are returned
-r                     turn off recursive look-ups for contact information
-R                     force to show local copy of the domain object even
                       if it contains referral
-a                     also search all the mirrored databases
-s SOURCE[,SOURCE]...  search the database mirrored from SOURCE
-g SOURCE:FIRST-LAST   find updates from SOURCE from serial FIRST to LAST
-t TYPE                request template for object of TYPE
-v TYPE                request verbose template for object of TYPE
-q [version|sources|types]  query specified server info
Learn more with
OffSec
Want to learn more about whois? get access to in-depth training and hands-on labs:
PEN-200: 6.2.1. Information Gathering: Whois Enumeration
PEN-200 course
Updated on: 2026-Mar-02
 Edit this page
truecrack
wifite
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install whois`，再执行 `whois --version` 2>/dev/null || `whois -V`
- [ ] **2.** **读官方帮助** —— `whois -h`，需要细节时 `man whois`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: mkpasswd [OPTIONS]... [PASSWORD [SALT]]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/whois/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/whois/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/whois/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
