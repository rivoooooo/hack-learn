# netdiscover

> Active/passive network address scanner using ARP requests Netdiscover is an active/passive address reconnaissance tool, mainly developed for those wireless networks without dhcp server, when you are wardriving. It can be also used on hub/s…

> **功能分类**：信息搜集 ｜ **Kali 包**：`netdiscover` ｜ **官方文档**：<https://www.kali.org/tools/netdiscover/>

## 1. 安装

```bash
sudo apt update
sudo apt install netdiscover
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.21 |
| 架构 | any |
| 可执行命令 | `netdiscover` |
| 依赖 | `libc6`、`libpcap0.8t64` |
| 安装体积 | 3.08 MB |
| 官网 | <https://github.com/netdiscover-scanner/netdiscover> |
| 源码仓库 | <https://salsa.debian.org/debian/netdiscover> |
| 包追踪 | <https://pkg.kali.org/pkg/netdiscover> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
netdiscover -h          # 查看用法
man netdiscover         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `netdiscover`

官方给出的调用示例：`netdiscover --help`

```text
root@kali:~# netdiscover --help
Netdiscover 0.21 [Active/passive ARP reconnaissance tool]
Written by: Jaime Penalba <
[email protected]
>
Usage: netdiscover [-i device] [-r range | -l file | -p] [-m file] [-F filter] [-s time] [-c count] [-n node] [-dfPLNS]
  -i device: your network device
  -r range: scan a given range instead of auto scan. 192.168.6.0/24,/16,/8
  -l file: scan the list of ranges contained into the given file
  -p passive mode: do not send anything, only sniff
  -m file: scan a list of known MACs and host names
  -F filter: customize pcap filter expression (default: "arp")
  -s time: time to sleep between each ARP request (milliseconds)
  -c count: number of times to send each ARP request (for nets with packet loss)
  -n node: last source IP octet used for scanning (from 2 to 253)
  -d ignore home config files for autoscan and fast mode
  -R assume user is root or has the required capabilities without running any checks
  -f enable fastmode scan, saves a lot of time, recommended for auto
  -P print results in a format suitable for parsing by another program and stop after active scan
  -L similar to -P but continue listening after the active scan is completed
  -N Do not print header. Only valid when -P or -L is enabled.
  -S enable sleep time suppression between each request (hardcore mode)
If -r, -l or -p are not enabled, netdiscover will scan for common LAN addresses.
Updated on: 2025-Dec-09
 Edit this page
netcat
netmask
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install netdiscover`，再执行 `netdiscover --version` 2>/dev/null || `netdiscover -V`
- [ ] **2.** **读官方帮助** —— `netdiscover -h`，需要细节时 `man netdiscover`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: netdiscover [-i device] [-r range | -l file | -p] [-m file] [-F filter] [-s time] [-c count] [-n node] [-dfPLNS]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/netdiscover/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[netdiscover](../../tools/tutorials/01-信息搜集/netdiscover.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/netdiscover/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/netdiscover/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
