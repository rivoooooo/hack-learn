# dhcpig

> DHCP exhaustion script using scapy network library DHCPig initiates an advanced DHCP exhaustion attack. It will consume all IPs on the LAN, stop new users from obtaining IPs, release any IPs in use, then for good measure send gratuitous AR…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`dhcpig` ｜ **官方文档**：<https://www.kali.org/tools/dhcpig/>

## 1. 安装

```bash
sudo apt update
sudo apt install dhcpig
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6 |
| 架构 | all |
| 可执行命令 | `dhcpig` |
| 依赖 | `python3`、`python3-scapy` |
| 安装体积 | 85 KB |
| 官网 | <https://github.com/kamorin/DHCPig> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/dhcpig> |
| 包追踪 | <https://pkg.kali.org/pkg/dhcpig> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Exhaust all of the available DHCP addresses using the eth0 interface (eth0):
root@kali:~# pig.py eth0
WARNING: No route found for IPv6 destination :: (no default route?)

Sending DHCPDISCOVER on eth0
waiting for first DHCP Server response on eth0
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pig.py`

> 官方示例调用：`pig.py eth0`

```text
root@kali:~# pig.py eth0
WARNING: No route found for IPv6 destination :: (no default route?)
Sending DHCPDISCOVER on eth0
waiting for first DHCP Server response on eth0
```

### `dhcpig`

> 官方示例调用：`dhcpig -h`

```text
root@kali:~# dhcpig -h
enhanced DHCP exhaustion attack.
Doc:
    http://github.com/kamorin/DHCPig
Usage:
    pig.py [-h -v -6 -1 -s -f -t -a -i -o -l -x -y -z -g -r -n -c ] <interface>
Options:
    -h, --help                     <-- you are here :)
    -v, --verbosity                ...  0 ... no         (3)
                                        1 ... minimal
                                       10 ... default
                                       99 ... debug
    -6, --ipv6                     ... DHCPv6 (off, DHCPv4 by default)
    -1, --v6-rapid-commit          ... enable RapidCommit (2way ip assignment instead of 4way) (off)
    -s, --client-src               ... a list of client macs 00:11:22:33:44:55,00:11:22:33:44:56 (Default: <random>)
    -O, --request-options          ... option-codes to request e.g. 21,22,23 or 12,14-19,23 (Default: 0-80)
    -f, --fuzz                     ... randomly fuzz packets (off)
    -t, --threads                  ... number of sending threads (1)
    -a, --show-arp                 ... detect/print arp who_has (off)
    -i, --show-icmp                ... detect/print icmps requests (off)
    -o, --show-options             ... print lease infos (off)
    -l, --show-lease-confirm       ... detect/print dhcp replies (off)
    -g, --neighbors-attack-garp    ... knock off network segment using gratious arps (off)
    -r, --neighbors-attack-release ... release all neighbor ips (off)
    -n, --neighbors-scan-arp       ... arp neighbor scan (off)
    -x, --timeout-threads          ... thread spawn timer (0.4)
    -y, --timeout-dos              ... DOS timeout (8) (wait time to mass grat.arp)
    -z, --timeout-dhcprequest      ... dhcp request timeout (2)
    -c, --color                    ... enable color output (off)
Updated on: 2026-May-25
 Edit this page
dfvfs
dirb
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dhcpig`，再执行 `dhcpig --version` 2>/dev/null || `dhcpig -V`
- [ ] **2.** **读官方帮助** —— `dhcpig -h`，需要细节时 `man dhcpig`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dhcpig/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/impact.md`](../../tools/by-attack/impact.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dhcpig/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dhcpig/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
