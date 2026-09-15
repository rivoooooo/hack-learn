# bloodhound-ce-python

> Python based ingestor for BloodHound CE This package contains a Python based ingestor for BloodHound CE, based on Impacket. This tool is only compatible with BloodHound CE. For legacy Bloodhound (<= 4.3.1) use bloodhound-python package.

> **功能分类**：通用工具 ｜ **Kali 包**：`bloodhound-ce-python` ｜ **官方文档**：<https://www.kali.org/tools/bloodhound-ce-python/>

## 1. 安装

```bash
sudo apt update
sudo apt install bloodhound-ce-python
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.9.1 |
| 架构 | all |
| 可执行命令 | `bloodhound-ce-python` |
| 依赖 | `python3`、`python3-dnspython`、`python3-impacket`、`python3-ldap3`、`python3-pyasn1` |
| 安装体积 | 357 KB |
| 官网 | <https://github.com/dirkjanm/BloodHound.py/tree/bloodhound-ce> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/bloodhound-ce-python> |
| 包追踪 | <https://pkg.kali.org/pkg/bloodhound-ce-python> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
bloodhound-ce-python -h          # 查看用法
man bloodhound-ce-python         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `bloodhound-ce-python`

> 官方示例调用：`bloodhound-ce-python -h`

```text
root@kali:~# bloodhound-ce-python -h
usage: bloodhound-ce-python [-h] [-c COLLECTIONMETHOD] [-d DOMAIN] [-v]
                            [-u USERNAME] [-p PASSWORD] [-k] [--hashes HASHES]
                            [-no-pass] [-aesKey hex key]
                            [--auth-method {auto,ntlm,kerberos}]
                            [-ns NAMESERVER] [--dns-tcp]
                            [--dns-timeout DNS_TIMEOUT] [-dc HOST] [-gc HOST]
                            [-w WORKERS] [--exclude-dcs] [--disable-pooling]
                            [--disable-autogc] [--zip]
                            [--computerfile COMPUTERFILE]
                            [--cachefile CACHEFILE] [--ldap-channel-binding]
                            [--use-ldaps] [-op PREFIX_NAME]
Python based ingestor for BloodHound Community Edition
For help or reporting issues, visit https://github.com/dirkjanm/BloodHound.py
options:
  -h, --help            show this help message and exit
  -c, --collectionmethod COLLECTIONMETHOD
                        Which information to collect. Supported: Group,
                        LocalAdmin, Session, Trusts, Default (all previous),
                        DCOnly (no computer connections), DCOM, RDP,PSRemote,
                        LoggedOn, Container, ObjectProps, ACL, All (all except
                        LoggedOn). You can specify more than one by separating
                        them with a comma. (default: Default)
  -d, --domain DOMAIN   Domain to query.
  -v                    Enable verbose output
authentication options:
  Specify one or more authentication options.
  By default Kerberos authentication is used and NTLM is used as fallback.
  Kerberos tickets are automatically requested if a password or hashes are specified.
  -u, --username USERNAME
                        Username. Format: username[@domain]; If the domain is
                        unspecified, the current domain is used.
  -p, --password PASSWORD
                        Password
  -k, --kerberos        Use kerberos ccache file
  --hashes HASHES       LM:NLTM hashes
  -no-pass              don't ask for password (useful for -k)
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
  --auth-method {auto,ntlm,kerberos}
                        Authentication methods. Force Kerberos or NTLM only or
                        use auto for Kerberos with NTLM fallback
collection options:
  -ns, --nameserver NAMESERVER
                        Alternative name server to use for queries
  --dns-tcp             Use TCP instead of UDP for DNS queries
  --dns-timeout DNS_TIMEOUT
                        DNS query timeout in seconds (default: 3)
  -dc, --domain-controller HOST
                        Override which DC to query (hostname)
  -gc, --global-catalog HOST
                        Override which GC to query (hostname)
  -w, --workers WORKERS
                        Number of workers for computer enumeration (default:
                        10)
  --exclude-dcs         Skip DCs during computer enumeration
  --disable-pooling     Don't use subprocesses for ACL parsing (only for
                        debugging purposes)
  --disable-autogc      Don't automatically select a Global Catalog (use only
                        if it gives errors)
  --zip                 Compress the JSON output files into a zip archive
  --computerfile COMPUTERFILE
                        File containing computer FQDNs to use as allowlist for
                        any computer based methods
  --cachefile CACHEFILE
                        Cache file (experimental)
  --ldap-channel-binding
                        Use LDAP Channel Binding (will force ldaps protocol to
                        be used)
  --use-ldaps           Use LDAP over TLS on port 636 by default
  -op, --outputprefix PREFIX_NAME
                        String to prepend to output file names
Updated on: 2025-Dec-09
 Edit this page
bing-ip2hosts
bloodhound.py
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install bloodhound-ce-python`，再执行 `bloodhound-ce-python --version` 2>/dev/null || `bloodhound-ce-python -V`
- [ ] **2.** **读官方帮助** —— `bloodhound-ce-python -h`，需要细节时 `man bloodhound-ce-python`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `bloodhound-ce-python -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/bloodhound-ce-python/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[bloodhound](../../tools/tutorials/08-后渗透/bloodhound.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/bloodhound-ce-python/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/bloodhound-ce-python/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
