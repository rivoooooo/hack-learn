# firewalk

> Active reconnaissance network security tool Firewalk is an active reconnaissance network security tool that attempts to determine what layer 4 protocols a given IP forwarding device will pass. It works by sending out TCP or UDP packets wit…

> **功能分类**：信息搜集 ｜ **Kali 包**：`firewalk` ｜ **官方文档**：<https://www.kali.org/tools/firewalk/>

## 1. 安装

```bash
sudo apt update
sudo apt install firewalk
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.0 |
| 架构 | any |
| 可执行命令 | `firewalk` |
| 依赖 | `libc6`、`libdumbnet1`、`libnet9`、`libpcap0.8t64` |
| 安装体积 | 51 KB |
| 官网 | <http://packetfactory.openwall.net/projects/firewalk/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/firewalk> |
| 包追踪 | <https://pkg.kali.org/pkg/firewalk> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan ports 8079-8081 (-S8079-8081) through the eth0 interface (-i eth0), do not resolve hostnames (-n), use TCP (-pTCP) via the gateway (192.168.1.1) against the target IP (192.168.0.1):
root@kali:~# firewalk -S8079-8081  -i eth0 -n -pTCP 192.168.1.1 192.168.0.1
Firewalk 5.0 [gateway ACL scanner]
Firewalk state initialization completed successfully.
TCP-based scan.
Ramping phase source port: 53, destination port: 33434
Hotfoot through 192.168.1.1 using 192.168.0.1 as a metric.
Ramping Phase:
 1 (TTL  1): expired [192.168.1.1]
Binding host reached.
Scan bound at 2 hops.
Scanning Phase:
port 8079: *no response*
port 8080: A! open (port not listen) [192.168.0.1]
port 8081: *no response*

Scan completed successfully.

Total packets sent:                4
Total packet errors:               0
Total packets caught               2
Total packets caught of interest   2
Total ports scanned                3
Total ports open:                  1
Total ports unknown:               0
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `firewalk`

官方给出的调用示例：`firewalk -S8079-8081  -i eth0 -n -pTCP 192.168.1.1 192.168.0.1`

```text
root@kali:~# firewalk -S8079-8081  -i eth0 -n -pTCP 192.168.1.1 192.168.0.1
Firewalk 5.0 [gateway ACL scanner]
Firewalk state initialization completed successfully.
TCP-based scan.
Ramping phase source port: 53, destination port: 33434
Hotfoot through 192.168.1.1 using 192.168.0.1 as a metric.
Ramping Phase:
 1 (TTL  1): expired [192.168.1.1]
Binding host reached.
Scan bound at 2 hops.
Scanning Phase:
port 8079: *no response*
port 8080: A! open (port not listen) [192.168.0.1]
port 8081: *no response*
Scan completed successfully.
Total packets sent:                4
Total packet errors:               0
Total packets caught               2
Total packets caught of interest   2
Total ports scanned                3
Total ports open:                  1
Total ports unknown:               0
```

### `firewalk（示例）`

官方给出的调用示例：`firewalk --help`

```text
root@kali:~# firewalk --help
firewalk: invalid option -- '-'
Usage : firewalk [options] target_gateway metric
		   [-d 0 - 65535] destination port to use (ramping phase)
		   [-h] program help
		   [-i device] interface
		   [-n] do not resolve IP addresses into hostnames
		   [-p TCP | UDP] firewalk protocol
		   [-r] strict RFC adherence
		   [-S x - y, z] port range to scan
		   [-s 0 - 65535] source port
		   [-T 1 - 1000] packet read timeout in ms
		   [-t 1 - 25] IP time to live
		   [-v] program version
		   [-x 1 - 8] expire vector
Updated on: 2025-Dec-09
 Edit this page
findomain
firmware-mod-kit
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install firewalk`，再执行 `firewalk --version` 2>/dev/null || `firewalk -V`
- [ ] **2.** **读官方帮助** —— `firewalk -h`，需要细节时 `man firewalk`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage : firewalk [options] target_gateway metric`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/firewalk/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/firewalk/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/firewalk/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
