# p0f

> Passive OS fingerprinting tool p0f performs passive OS detection based on SYN packets. Unlike nmap and queso, p0f does recognition without sending any data. Additionally, it is able to determine the distance to the remote host, and can be …

> **功能分类**：信息搜集 ｜ **Kali 包**：`p0f` ｜ **官方文档**：<https://www.kali.org/tools/p0f/>

## 1. 安装

```bash
sudo apt update
sudo apt install p0f
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.09b |
| 架构 | any |
| 可执行命令 | `p0f` |
| 依赖 | `libc6`、`libpcap0.8t64` |
| 安装体积 | 218 KB |
| 官网 | <https://lcamtuf.coredump.cx/p0f3/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/p0f> |
| 包追踪 | <https://pkg.kali.org/pkg/p0f> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Use interface eth0 (-i eth0) in promiscuous mode (-p), saving the results to a file (-o /tmp/p0f.log):
root@kali:~# p0f -i eth0 -p -o /tmp/p0f.log
-- p0f 3.09b by Michal Zalewski <lcamtuf@coredump.cx> ---

[+] Closed 1 file descriptor.
[+] Loaded 322 signatures from '/etc/p0f/p0f.fp'.
[+] Intercepting traffic on interface 'eth0'.
[+] Default packet filtering configured [+VLAN].
[+] Log file '/tmp/p0f.log' opened for writing.
[+] Entered main event loop.

.-[ 192.168.1.15/35834 -> 173.246.39.185/873 (syn) ]-
|
| client   = 192.168.1.15/35834
| os       = Linux 3.11 and newer
| dist     = 0
| params   = none
| raw_sig  = 4:64+0:0:1460:mss*20,7:mss,sok,ts,nop,ws:df,id+:0
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `p0f`

官方给出的调用示例：`p0f -i eth0 -p -o /tmp/p0f.log`

```text
root@kali:~# p0f -i eth0 -p -o /tmp/p0f.log
-- p0f 3.09b by Michal Zalewski <
[email protected]
> ---
[+] Closed 1 file descriptor.
[+] Loaded 322 signatures from '/etc/p0f/p0f.fp'.
[+] Intercepting traffic on interface 'eth0'.
[+] Default packet filtering configured [+VLAN].
[+] Log file '/tmp/p0f.log' opened for writing.
[+] Entered main event loop.
.-[ 192.168.1.15/35834 -> 173.246.39.185/873 (syn) ]-
|
| client   = 192.168.1.15/35834
| os       = Linux 3.11 and newer
| dist     = 0
| params   = none
| raw_sig  = 4:64+0:0:1460:mss*20,7:mss,sok,ts,nop,ws:df,id+:0
```

### `p0f（示例）`

官方给出的调用示例：`p0f -h`

```text
root@kali:~# p0f -h
p0f: invalid option -- 'h'
Usage: p0f [ ...options... ] [ 'filter rule' ]
Network interface options:
  -i iface  - listen on the specified network interface
  -r file   - read offline pcap data from a given file
  -p        - put the listening interface in promiscuous mode
  -L        - list all available interfaces
Operating mode and output settings:
  -f file   - read fingerprint database from 'file' (/etc/p0f/p0f.fp)
  -o file   - write information to the specified log file
  -s name   - answer to API queries at a named unix socket
  -u user   - switch to the specified unprivileged account and chroot
  -d        - fork into background (requires -o or -s)
Performance-related options:
  -S limit  - limit number of parallel API connections (20)
  -t c,h    - set connection / host cache age limits (30s,120m)
  -m c,h    - cap the number of active connections / hosts (1000,10000)
Optional filter expressions (man tcpdump) can be specified in the command
line to prevent p0f from looking at incidental network traffic.
Problems? You can reach the author at <
[email protected]
>.
Updated on: 2025-Dec-09
 Edit this page
owl
pack2
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install p0f`，再执行 `p0f --version` 2>/dev/null || `p0f -V`
- [ ] **2.** **读官方帮助** —— `p0f -h`，需要细节时 `man p0f`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: p0f [ ...options... ] [ 'filter rule' ]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/p0f/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/p0f/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/p0f/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
