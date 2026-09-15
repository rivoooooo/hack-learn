# braa

> Mass SNMP scanner Braa is a mass snmp scanner. The intended usage of such a tool is of course making SNMP queries - but unlike snmpget or snmpwalk from net-snmp, it is able to query dozens or hundreds of hosts simultaneously, and in a sing…

> **功能分类**：信息搜集 ｜ **Kali 包**：`braa` ｜ **官方文档**：<https://www.kali.org/tools/braa/>

## 1. 安装

```bash
sudo apt update
sudo apt install braa
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.90.1 |
| 架构 | any |
| 可执行命令 | `braa` |
| 依赖 | `libc6` |
| 安装体积 | 66 KB |
| 官网 | <https://github.com/mteg/braa> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/braa> |
| 包追踪 | <https://pkg.kali.org/pkg/braa> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Walk the SNMP tree on 192.168.1.215 using the community string of public, querying all OIDs under .1.3.6:
root@kali:~# braa public@192.168.1.215:.1.3.6.*
192.168.1.215:122ms:.1.3.6.1.2.1.1.1.0:Linux redhat.biz.local 2.4.20-8 #1 Thu Mar 13 17:54:28 EST 2003 i686
192.168.1.215:143ms:.1.3.6.1.2.1.1.2.0:.1.3.6.1.4.1.8072.3.2.10
192.168.1.215:122ms:.1.3.6.1.2.1.1.3.0:4051218219
192.168.1.215:122ms:.1.3.6.1.2.1.1.4.0:Root <root@localhost> (configure /etc/snmp/snmp.local.conf)
192.168.1.215:143ms:.1.3.6.1.2.1.1.5.0:redhat.biz.local
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `braa`

```text
root@kali:~# braa
[email protected]
:.1.3.6.*
192.168.1.215:122ms:.1.3.6.1.2.1.1.1.0:Linux redhat.biz.local 2.4.20-8 #1 Thu Mar 13 17:54:28 EST 2003 i686
192.168.1.215:143ms:.1.3.6.1.2.1.1.2.0:.1.3.6.1.4.1.8072.3.2.10
192.168.1.215:122ms:.1.3.6.1.2.1.1.3.0:4051218219
192.168.1.215:122ms:.1.3.6.1.2.1.1.4.0:Root <root@localhost> (configure /etc/snmp/snmp.local.conf)
192.168.1.215:143ms:.1.3.6.1.2.1.1.5.0:redhat.biz.local
```

### `braa（示例）`

官方给出的调用示例：`braa -h`

```text
root@kali:~# braa -h
braa 0.90.1 - (c) by Mateusz 'mteg' Golicz and contributors, 2003 - 2015, 2024
usage: braa [options] [query1] [query2] ...
  -h        Show this help.
  -2        Claim to be a SNMP2C agent.
  -b <n>    Use GETBULK requests for walks.
  -v        Show short summary after doing all queries.
  -x        Hexdump octet-strings
  -t <s>    Wait <s> seconds for responses.
  -d <s>    Wait <s> microseconds after sending each packet.
  -w <s>    Wait <s> microseconds after sending a group of query packets.
  -p <s>    Wait <s> milliseconds between subsequent passes.
  -f <file> Load queries from file <file> (one by line).
  -a <time> Quit after <time> seconds, independent on what happens.
  -r <rc>   Retry count (default: 3).
Query format:
  GET:   [community@]iprange[:port]:oid[/id]
  WALK:  [community@]iprange[:port]:oid.*[/id]
  SET:   [community@]iprange[:port]:oid=value[/id]
Examples:
[email protected]
:161:.1.3.6.*
         10.253.101.1-10.253.101.255:.1.3.6.1.2.1.1.4.0=sme
         10.253.101.1:.1.3.6.1.2.1.1.1.0/description
It is also possible to specify multiple queries at once:
         10.253.101.1-10.253.101.255:.1.3.6.1.2.1.1.4.0=sme,.1.3.6.*
         (Will set .1.3.6.1.2.1.1.4.0 to 'me' and do a walk starting from .1.3.6)
Values for SET queries have to be prepended with a character specifying the value type:
  i      is INTEGER
  a      is IPADDRESS
  s      is OCTET STRING
  o      is OBJECT IDENTIFIER
If the type specifier is missing, the value type is auto-detected
Updated on: 2026-Aug-25
 Edit this page
bluez
bulk-extractor
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install braa`，再执行 `braa --version` 2>/dev/null || `braa -V`
- [ ] **2.** **读官方帮助** —— `braa -h`，需要细节时 `man braa`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `braa -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/braa/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/braa/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/braa/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
