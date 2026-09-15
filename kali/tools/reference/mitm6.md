# mitm6

> Pwning IPv4 via IPv6 mitm6 is a pentesting tool that exploits the default configuration of Windows to take over the default DNS server. It does this by replying to DHCPv6 messages, providing victims with a link-local IPv6 address and setti…

> **功能分类**：通用工具 ｜ **Kali 包**：`mitm6` ｜ **官方文档**：<https://www.kali.org/tools/mitm6/>

## 1. 安装

```bash
sudo apt update
sudo apt install mitm6
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.3.0 |
| 架构 | all |
| 可执行命令 | `mitm6` |
| 依赖 | `python3`、`python3-netifaces`、`python3-scapy`、`python3-twisted` |
| 安装体积 | 40 KB |
| 官网 | <https://github.com/dirkjanm/mitm6> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/mitm6> |
| 包追踪 | <https://pkg.kali.org/pkg/mitm6> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
mitm6 -h          # 查看用法
man mitm6         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `mitm6`

> 官方示例调用：`mitm6 -h`

```text
root@kali:~# mitm6 -h
usage: mitm6 [-h] [-i INTERFACE] [-l LOCALDOMAIN] [-4 ADDRESS] [-6 ADDRESS]
             [-m ADDRESS] [-a] [-r TARGET] [-v] [--debug] [-d DOMAIN]
             [-b DOMAIN] [-hw DOMAIN] [-hb DOMAIN] [--ignore-nofqdn]
mitm6 - pwning IPv4 via IPv6
For help or reporting issues, visit https://github.com/dirkjanm/mitm6
options:
  -h, --help            show this help message and exit
  -i, --interface INTERFACE
                        Interface to use (default: autodetect)
  -l, --localdomain LOCALDOMAIN
                        Domain name to use as DNS search domain (default: use
                        first DNS domain)
  -4, --ipv4 ADDRESS    IPv4 address to send packets from (default:
                        autodetect)
  -6, --ipv6 ADDRESS    IPv6 link-local address to send packets from (default:
                        autodetect)
  -m, --mac ADDRESS     Custom mac address - probably breaks stuff (default:
                        mac of selected interface)
  -a, --no-ra           Do not advertise ourselves (useful for networks which
                        detect rogue Router Advertisements)
  -r, --relay TARGET    Authentication relay target, will be used as fake DNS
                        server hostname to trigger Kerberos auth
  -v, --verbose         Show verbose information
  --debug               Show debug information
Filtering options:
  -d, --domain DOMAIN   Domain name to filter DNS queries on (Allowlist
                        principle, multiple can be specified.)
  -b, --blocklist, --blacklist DOMAIN
                        Domain name to filter DNS queries on (Blocklist
                        principle, multiple can be specified.)
  -hw, -ha, --host-allowlist, --host-whitelist DOMAIN
                        Hostname (FQDN) to filter DHCPv6 queries on (Allowlist
                        principle, multiple can be specified.)
  -hb, --host-blocklist, --host-blacklist DOMAIN
                        Hostname (FQDN) to filter DHCPv6 queries on (Blocklist
                        principle, multiple can be specified.)
  --ignore-nofqdn       Ignore DHCPv6 queries that do not contain the Fully
                        Qualified Domain Name (FQDN) option.
Updated on: 2026-Jun-19
 Edit this page
goldeneye
phishery
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install mitm6`，再执行 `mitm6 --version` 2>/dev/null || `mitm6 -V`
- [ ] **2.** **读官方帮助** —— `mitm6 -h`，需要细节时 `man mitm6`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `mitm6 -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/mitm6/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/collection.md`](../../tools/by-attack/collection.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/mitm6/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/mitm6/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
