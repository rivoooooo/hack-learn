# sprayhound

> Password spraying tool and Bloodhound integration SprayHound is a Python library to safely password spray in Active Directory, which sets pwned users as owned in Bloodhound and detects paths to Domain Admins.

> **功能分类**：通用工具 ｜ **Kali 包**：`sprayhound` ｜ **官方文档**：<https://www.kali.org/tools/sprayhound/>

## 1. 安装

```bash
sudo apt update
sudo apt install sprayhound
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0~git20260614.4a31205 |
| 架构 | all |
| 可执行命令 | `sprayhound` |
| 依赖 | `python3`、`python3-ldap3`、`python3-neo4j`、`python3-pkg-resources` |
| 安装体积 | 69 KB |
| 官网 | <https://github.com/Hackndo/sprayhound> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sprayhound> |
| 包追踪 | <https://pkg.kali.org/pkg/sprayhound> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sprayhound -h          # 查看用法
man sprayhound         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sprayhound`

> 官方示例调用：`sprayhound -h`

```text
root@kali:~# sprayhound -h
usage: sprayhound [-h] [-u USERNAME] [-U USERFILE] [-p PASSWORD | --lower |
                  --upper] [-t THRESHOLD] [-dc DOMAIN_CONTROLLER] [-d DOMAIN]
                  [-lP LDAP_PORT] [-lu LDAP_USER] [-lp LDAP_PASS] [-lssl]
                  [-lpage LDAP_PAGE_SIZE] [-nh NEO4J_HOST] [-nP NEO4J_PORT]
                  [-nu NEO4J_USER] [-np NEO4J_PASS] [--unsafe] [--force]
                  [--nocolor] [-v]
sprayhound v0.0.4 - Password spraying
options:
  -h, --help            show this help message and exit
  --unsafe              Enable login tries on almost locked out accounts
  --force               Do not prompt for user confirmation
  --nocolor             Do not use color for output
  -v                    Verbosity level (-v or -vv)
credentials:
  -u, --username USERNAME
                        Username
  -U, --userfile USERFILE
                        File containing username list
  -p, --password PASSWORD
                        Password
  --lower               User as pass with lowercase password
  --upper               User as pass with uppercase password
  -t, --threshold THRESHOLD
                        Number of password left allowed before locked out
ldap:
  -dc, --domain-controller DOMAIN_CONTROLLER
                        Domain controller
  -d, --domain DOMAIN   Domain FQDN
  -lP, --ldap-port LDAP_PORT
                        LDAP Port
  -lu, --ldap-user LDAP_USER
                        LDAP User
  -lp, --ldap-pass LDAP_PASS
                        LDAP Password
  -lssl, --ldap-ssl     LDAP over TLS (ldaps)
  -lpage, --ldap-page-size LDAP_PAGE_SIZE
                        LDAP Paging size (Default: 200)
neo4j:
  -nh, --neo4j-host NEO4J_HOST
                        Neo4J Host (Default: 127.0.0.1)
  -nP, --neo4j-port NEO4J_PORT
                        Neo4J Port (Default: 7687)
  -nu, --neo4j-user NEO4J_USER
                        Neo4J user (Default: neo4j)
  -np, --neo4j-pass NEO4J_PASS
                        Neo4J password (Default: neo4j)
example:
    sprayhound -d adsec.local -p Winter202
    sprayhound -U userlist.txt -d adsec.local
Updated on: 2026-Aug-25
 Edit this page
sploitscan
sqlmap
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sprayhound`，再执行 `sprayhound --version` 2>/dev/null || `sprayhound -V`
- [ ] **2.** **读官方帮助** —— `sprayhound -h`，需要细节时 `man sprayhound`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sprayhound -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sprayhound/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sprayhound/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sprayhound/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
