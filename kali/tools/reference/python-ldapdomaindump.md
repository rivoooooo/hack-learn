# python-ldapdomaindump

> Active Directory information dumper via LDAP (Python 3) This package contains an Active Directory information dumper via LDAP. In an Active Directory domain, a lot of interesting information can be retrieved via LDAP by any authenticated u…

> **功能分类**：信息搜集 ｜ **Kali 包**：`python-ldapdomaindump` ｜ **官方文档**：<https://www.kali.org/tools/python-ldapdomaindump/>

## 1. 安装

```bash
sudo apt update
sudo apt install python3-ldapdomaindump
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.9.4 |
| 架构 | all |
| 可执行命令 | `python3-ldapdomaindump`、`ldapdomaindump`、`ldd2bloodhound`、`ldd2pretty` |
| 依赖 | `python3`、`python3-dnspython`、`python3-ldap3`、`ldapdomaindump` |
| 安装体积 | 84 KB |
| 官网 | <https://github.com/dirkjanm/ldapdomaindump> |
| 源码仓库 | <https://salsa.debian.org/python-team/packages/python-ldapdomaindump> |
| 包追踪 | <https://pkg.kali.org/pkg/python-ldapdomaindump> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
python3-ldapdomaindump -h          # 查看用法
man python3-ldapdomaindump         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ldapdomaindump`

官方给出的调用示例：`ldapdomaindump -h`

```text
root@kali:~# ldapdomaindump -h
usage: ldapdomaindump [-h] [-u USERNAME] [-p PASSWORD] [-at {NTLM,SIMPLE}]
                      [-o DIRECTORY] [--no-html] [--no-json] [--no-grep]
                      [--grouped-json] [-d DELIMITER] [-r] [-n DNS_SERVER]
                      [-m]
                      HOSTNAME
Domain information dumper via LDAP. Dumps users/computers/groups and
OS/membership information to HTML/JSON/greppable output.
Required options:
  HOSTNAME              Hostname/ip or ldap://host:port connection string to
                        connect to (use ldaps:// to use SSL)
Main options:
  -h, --help            show this help message and exit
  -u, --user USERNAME   DOMAIN\username for authentication, leave empty for
                        anonymous authentication
  -p, --password PASSWORD
                        Password or LM:NTLM hash, will prompt if not specified
  -at, --authtype {NTLM,SIMPLE}
                        Authentication type (NTLM or SIMPLE, default: NTLM)
Output options:
  -o, --outdir DIRECTORY
                        Directory in which the dump will be saved (default:
                        current)
  --no-html             Disable HTML output
  --no-json             Disable JSON output
  --no-grep             Disable Greppable output
  --grouped-json        Also write json files for grouped files (default:
                        disabled)
  -d, --delimiter DELIMITER
                        Field delimiter for greppable output (default: tab)
Misc options:
  -r, --resolve         Resolve computer hostnames (might take a while and
                        cause high traffic on large networks)
  -n, --dns-server DNS_SERVER
                        Use custom DNS resolver instead of system DNS (try a
                        domain controller IP)
  -m, --minimal         Only query minimal set of attributes to limit memmory
                        usage
```

### `ldd2bloodhound`

官方给出的调用示例：`ldd2bloodhound -h`

```text
root@kali:~# ldd2bloodhound -h
usage: ldd2bloodhound [-h] [-d] FILENAME [FILENAME ...]
LDAPDomainDump to BloodHound CSV converter utility. Supports
users/computers/trusts conversion.
positional arguments:
  FILENAME     The ldapdomaindump json files to load. Required files:
               domain_users.json and domain_groups.json
options:
  -h, --help   show this help message and exit
  -d, --debug  Enable debug logger
```

### `ldd2pretty`

官方给出的调用示例：`ldd2pretty -h`

```text
root@kali:~# ldd2pretty -h
usage: ldd2pretty [-h] [-d DIRECTORY]
LDAPDomainDump to pretty output like enum4linux.
options:
  -h, --help            show this help message and exit
  -d, --directory DIRECTORY
                        The ldapdomaindump directory where the json files are
                        saved. Required files: domain_users.json,
                        domain_groups.json and domain_policy.json
Updated on: 2025-Dec-09
 Edit this page
pwncat
qsslcaudit
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install python3-ldapdomaindump`，再执行 `python3-ldapdomaindump --version` 2>/dev/null || `python3-ldapdomaindump -V`
- [ ] **2.** **读官方帮助** —— `python3-ldapdomaindump -h`，需要细节时 `man python3-ldapdomaindump`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `python3-ldapdomaindump -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/python-ldapdomaindump/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/python-ldapdomaindump/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/python-ldapdomaindump/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
