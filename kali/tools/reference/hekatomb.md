# hekatomb

> Extract and decrypt all credentials from all domain computers Hekatomb is a Python script that connects to an LDAP directory to retrieve all computers and users’ information. From there, it will download all DPAPI blobs of all users from a…

> **功能分类**：通用工具 ｜ **Kali 包**：`hekatomb` ｜ **官方文档**：<https://www.kali.org/tools/hekatomb/>

## 1. 安装

```bash
sudo apt update
sudo apt install hekatomb
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.5.14 |
| 架构 | all |
| 可执行命令 | `hekatomb` |
| 依赖 | `python3`、`python3-chardet`、`python3-dnspython`、`python3-impacket`、`python3-ldap3`、`python3-pycryptodome` |
| 安装体积 | 63 KB |
| 官网 | <https://github.com/ProcessusT/HEKATOMB> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/hekatomb> |
| 包追踪 | <https://pkg.kali.org/pkg/hekatomb> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
hekatomb -h          # 查看用法
man hekatomb         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hekatomb`

官方给出的调用示例：`hekatomb -h`

```text
root@kali:~# hekatomb -h
██░ ██ ▓█████  ██ ▄█▀▄▄▄     ▄▄▄█████▓ ▒█████   ███▄ ▄███▓ ▄▄▄▄
▓██░ ██▒▓█   ▀  ██▄█▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄
▒██▀▀██░▒███   ▓███▄░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░▒██▒ ▄██
░▓█ ░██ ▒▓█  ▄ ▓██ █▄░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██    ▒██ ▒██░█▀
░▓█▒░██▓░▒████▒▒██▒ █▄▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓
 ▒ ░░▒░▒░░ ▒░ ░▒ ▒▒ ▓▒▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒
 ▒ ░▒░ ░ ░ ░  ░░ ░▒ ▒░ ▒   ▒▒ ░   ░      ░ ▒ ▒░ ░  ░      ░▒░▒   ░
 ░  ░░ ░   ░   ░ ░░ ░  ░   ▒    ░      ░ ░ ░ ▒  ░      ░    ░    ░
 ░  ░  ░   ░  ░░  ░        ░  ░            ░ ░         ░    ░
   Because Domain Admin rights are not enough.
		Hack them all.
	         @Processus
	            v1.5
**************************************************
usage: hekatomb [-h] [-hashes LMHASH:NTHASH] [-pvk PVK] [-dns DNS]
                [-port [port]] [-smb2] [-just-user JUST_USER]
                [-just-computer JUST_COMPUTER] [-md5] [-csv] [-debug]
                [-debugmax]
                target
Script used to automate domain computers and users extraction from LDAP and
extraction of domain controller private key through RPC to collect and decrypt
all users' DPAPI secrets saved in Windows credential manager.
positional arguments:
  target                [[domain/]username[:password]@]<targetName or address
                        of DC>
options:
  -h, --help            show this help message and exit
authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
authentication:
  -pvk PVK              Domain backup keys file
  -dns DNS              DNS server IP address to resolve computers hostname
  -port [port]          Port to connect to SMB Server
  -smb2                 Force the use of SMBv2 protocol
  -just-user JUST_USER  Test only specified username
  -just-computer JUST_COMPUTER
                        Test only specified computer
  -md5                  Print md5 hash instead of clear passwords
verbosity:
  -csv                  Export results to CSV file
  -debug                Turn DEBUG output ON
  -debugmax             Turn DEBUG output TO MAAAAXXXX
Updated on: 2025-Dec-09
 Edit this page
hashrat
hexinject
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install hekatomb`，再执行 `hekatomb --version` 2>/dev/null || `hekatomb -V`
- [ ] **2.** **读官方帮助** —— `hekatomb -h`，需要细节时 `man hekatomb`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `hekatomb -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hekatomb/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hekatomb/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hekatomb/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
