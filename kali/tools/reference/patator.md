# patator

> Multi-purpose brute-forcer Patator is a multi-purpose brute-forcer, with a modular design and a flexible usage. Currently it supports the following modules: ftp_login : Brute-force FTP ssh_login : Brute-force SSH

> **功能分类**：Web 应用 ｜ **Kali 包**：`patator` ｜ **官方文档**：<https://www.kali.org/tools/patator/>

## 1. 安装

```bash
sudo apt update
sudo apt install patator
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1.0 |
| 架构 | all |
| 可执行命令 | `patator` |
| 依赖 | `default-jre`、`ldap-utils`、`python3`、`python3-ajpy`、`python3-dnspython`、`python3-impacket`、`python3-ipy`、`python3-mysqldb`、`python3-paramiko`、`python3-psycopg2`、`python3-pycryptodome`、`python3-pycurl` 等 |
| 安装体积 | 183 KB |
| 官网 | <https://github.com/lanjelot/patator> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/patator> |
| 包追踪 | <https://pkg.kali.org/pkg/patator> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Do a MySQL brute force attack (mysql_login) with the root user (user=root) and passwords contained in a file (password=FILE0 0=/root/passes.txt) against the given host (host=127.0.0.1), ignoring the specified string (-x ignore:fgrep=’Access denied for user’):
root@kali:~# patator mysql_login user=root password=FILE0 0=/root/passes.txt host=127.0.0.1 -x ignore:fgrep='Access denied for user'
12:30:36 patator    INFO - Starting Patator v0.5 (http://code.google.com/p/patator/) at 2014-05-19 12:30 EDT
12:30:36 patator    INFO -
12:30:36 patator    INFO - code  size | candidate                          |   num | mesg
12:30:36 patator    INFO - ----------------------------------------------------------------------
12:30:37 patator    INFO - 0     16   | toor                               |  4493 | 5.5.37-0+wheezy1
12:30:37 patator    INFO - Hits/Done/Skip/Fail/Size: 1/4493/0/0/4493, Avg: 3582 r/s, Time: 0h 0m 1s
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `patator`

> 官方示例调用：`patator mysql_login user=root password=FILE0 0=/root/passes.txt host=127.0.0.1 -x ignore:fgrep='Access denied for user'`

```text
root@kali:~# patator mysql_login user=root password=FILE0 0=/root/passes.txt host=127.0.0.1 -x ignore:fgrep='Access denied for user'
12:30:36 patator    INFO - Starting Patator v0.5 (http://code.google.com/p/patator/) at 2014-05-19 12:30 EDT
12:30:36 patator    INFO -
12:30:36 patator    INFO - code  size | candidate                          |   num | mesg
12:30:36 patator    INFO - ----------------------------------------------------------------------
12:30:37 patator    INFO - 0     16   | toor                               |  4493 | 5.5.37-0+wheezy1
12:30:37 patator    INFO - Hits/Done/Skip/Fail/Size: 1/4493/0/0/4493, Avg: 3582 r/s, Time: 0h 0m 1s
```

### `patator -h`

> 官方示例调用：`patator -h`

```text
root@kali:~# patator -h
Patator 1.1.0 (https://github.com/lanjelot/patator) with Python-3.14.6
Usage: patator module --help
Available modules:
  + ftp_login     : Brute-force FTP
  + ssh_login     : Brute-force SSH
  + telnet_login  : Brute-force Telnet
  + smtp_login    : Brute-force SMTP
  + smtp_vrfy     : Enumerate valid users using SMTP VRFY
  + smtp_rcpt     : Enumerate valid users using SMTP RCPT TO
  + finger_lookup : Enumerate valid users using Finger
  + http_fuzz     : Brute-force HTTP
  + rdp_gateway   : Brute-force RDP Gateway
  + ajp_fuzz      : Brute-force AJP
  + pop_login     : Brute-force POP3
  + pop_passd     : Brute-force poppassd (http://netwinsite.com/poppassd/)
  + imap_login    : Brute-force IMAP4
  + ldap_login    : Brute-force LDAP
  + dcom_login    : Brute-force DCOM
  + smb_login     : Brute-force SMB
  + smb_lookupsid : Brute-force SMB SID-lookup
  + rlogin_login  : Brute-force rlogin
  + vmauthd_login : Brute-force VMware Authentication Daemon
  + mssql_login   : Brute-force MSSQL
  + oracle_login  : Brute-force Oracle
  + mysql_login   : Brute-force MySQL
  + mysql_query   : Brute-force MySQL queries
  + rdp_login     : Brute-force RDP (NLA)
  + pgsql_login   : Brute-force PostgreSQL
  + vnc_login     : Brute-force VNC
  + dns_forward   : Forward DNS lookup
  + dns_reverse   : Reverse DNS lookup
  + snmp_login    : Brute-force SNMP v1/2/3
  + ike_enum      : Enumerate IKE transforms
  + unzip_pass    : Brute-force the password of encrypted ZIP files
  + keystore_pass : Brute-force the password of Java keystore files
  + sqlcipher_pass : Brute-force the password of SQLCipher-encrypted databases
  + umbraco_crack : Crack Umbraco HMAC-SHA1 password hashes
  + tcp_fuzz      : Fuzz TCP services
  + dummy_test    : Testing module
Updated on: 2026-Aug-25
 Edit this page
padbuster
pdf-parser
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install patator`，再执行 `patator --version` 2>/dev/null || `patator -V`
- [ ] **2.** **读官方帮助** —— `patator -h`，需要细节时 `man patator`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: patator module --help`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/patator/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[patator](../../tools/tutorials/04-口令攻击/patator.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/patator/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/patator/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
