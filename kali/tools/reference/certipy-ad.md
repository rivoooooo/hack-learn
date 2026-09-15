# certipy-ad

> Tool for attacking AD Certificate Services Offensive tool for enumerating and abusing Active Directory Certificate Services (AD CS).

> **功能分类**：Top 10 常用 ｜ **Kali 包**：`certipy-ad` ｜ **官方文档**：<https://www.kali.org/tools/certipy-ad/>

## 1. 安装

```bash
sudo apt update
sudo apt install certipy-ad
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.1.0 |
| 架构 | all |
| 可执行命令 | `certipy-ad` |
| 依赖 | `python3`、`python3-argcomplete`、`python3-asn1crypto`、`python3-bs4`、`python3-cryptography`、`python3-dnspython`、`python3-httpx`、`python3-impacket`、`python3-ldap3`、`python3-openssl`、`python3-pyasn1`、`python3-pycryptodome` 等 |
| 安装体积 | 746 KB |
| 官网 | <https://github.com/ly4k/Certipy> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/certipy-ad> |
| 包追踪 | <https://pkg.kali.org/pkg/certipy-ad> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
certipy-ad -h          # 查看用法
man certipy-ad         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `certipy-ad`

官方给出的调用示例：`certipy-ad -h`

```text
root@kali:~# certipy-ad -h
usage: certipy-ad [-v] [-h]
                  {account,auth,ca,cert,find,parse,forge,relay,req,shadow,template} ...
Active Directory Certificate Services enumeration and abuse
positional arguments:
  {account,auth,ca,cert,find,parse,forge,relay,req,shadow,template}
                        Action
    account             Manage user and machine accounts
    auth                Authenticate using certificates
    ca                  Manage CA and certificates
    cert                Manage certificates and private keys
    find                Enumerate AD CS
    parse               Offline enumerate AD CS based on registry data
    forge               Create Golden Certificates or self-signed certificates
    relay               NTLM Relay to AD CS HTTP Endpoints
    req                 Request certificates
    shadow              Abuse Shadow Credentials for account takeover
    template            Manage certificate templates
options:
  -v, --version         Show Certipy's version number and exit
  -h, --help            Show this help message and exit
Learn more with
OffSec
Want to learn more about certipy-ad? get access to in-depth training and hands-on labs:
PEN-300: 22.2.2. Attacking Active Directory Certificate Services: NTLM Relay to ADCS HTTP Endpoints
PEN-300 course
Updated on: 2026-Aug-25
 Edit this page
ccrypt
chainsaw
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install certipy-ad`，再执行 `certipy-ad --version` 2>/dev/null || `certipy-ad -V`
- [ ] **2.** **读官方帮助** —— `certipy-ad -h`，需要细节时 `man certipy-ad`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `certipy-ad -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/certipy-ad/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/certipy-ad/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/certipy-ad/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
