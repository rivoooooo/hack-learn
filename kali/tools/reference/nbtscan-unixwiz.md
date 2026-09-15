# nbtscan-unixwiz

> Scanner for open NETBIOS nameservers This package contains a command-line tool that scans for open NETBIOS nameservers on a local or remote TCP/IP network, and this is a first step in finding of open shares. It is based on the functionalit…

> **功能分类**：通用工具 ｜ **Kali 包**：`nbtscan-unixwiz` ｜ **官方文档**：<https://www.kali.org/tools/nbtscan-unixwiz/>

## 1. 安装

```bash
sudo apt update
sudo apt install nbtscan-unixwiz
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0.35 |
| 架构 | any |
| 可执行命令 | `nbtscan-unixwiz` |
| 依赖 | `libc6` |
| 安装体积 | 53 KB |
| 官网 | <http://unixwiz.net/tools/nbtscan.html> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/nbtscan-unixwiz> |
| 包追踪 | <https://pkg.kali.org/pkg/nbtscan-unixwiz> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
Scan a range of IP addresses (192.168.0.100-110) without doing inverse name lookups (-n):
root@kali:~# nbtscan-unixwiz -n 192.168.0.100-110
192.168.0.105   WORKGROUP\RETROPIE              SHARING
*timeout (normal end of scan)

Scan a single IP address (192.168.0.38) and show Full NBT resource record responses (-f):
root@kali:~# nbtscan-unixwiz -f 192.168.0.38
192.168.0.38    WORKGROUP\DOOKOSSEL             SHARING
  DOOKOSSEL      <00> UNIQUE Workstation Service
  DOOKOSSEL      <03> UNIQUE Messenger Service<3>
  DOOKOSSEL      <20> UNIQUE File Server Service
  ..__MSBROWSE__.<01> GROUP  Master Browser
  WORKGROUP      <00> GROUP  Domain Name
  WORKGROUP      <1d> UNIQUE Master Browser
  WORKGROUP      <1e> GROUP  Browser Service Elections
  00:00:00:00:00:00   ETHER
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `nbtscan-unixwiz`

> 官方示例调用：`nbtscan-unixwiz -n 192.168.0.100-110`

```text
root@kali:~# nbtscan-unixwiz -n 192.168.0.100-110
192.168.0.105   WORKGROUP\RETROPIE              SHARING
*timeout (normal end of scan)
Scan a single IP address (
192.168.0.38
) and show Full NBT resource record responses (
-f
):
```

### `nbtscan-unixwiz -f 192.168.0.38`

> 官方示例调用：`nbtscan-unixwiz -f 192.168.0.38`

```text
root@kali:~# nbtscan-unixwiz -f 192.168.0.38
192.168.0.38    WORKGROUP\DOOKOSSEL             SHARING
  DOOKOSSEL      <00> UNIQUE Workstation Service
  DOOKOSSEL      <03> UNIQUE Messenger Service<3>
  DOOKOSSEL      <20> UNIQUE File Server Service
  ..__MSBROWSE__.<01> GROUP  Master Browser
  WORKGROUP      <00> GROUP  Domain Name
  WORKGROUP      <1d> UNIQUE Master Browser
  WORKGROUP      <1e> GROUP  Browser Service Elections
  00:00:00:00:00:00   ETHER
```

### `nbtscan-unixwiz -h`

> 官方示例调用：`nbtscan-unixwiz -h`

```text
root@kali:~# nbtscan-unixwiz -h
nbtscan-unixwiz: invalid option -- 'h'
nbtscan 1.0.35 - 2008-04-08 - http://www.unixwiz.net/tools/
usage: nbtscan-unixwiz [options] target [targets...]
   Targets are lists of IP addresses, DNS names, or address
   ranges. Ranges can be in /nbits notation ("192.168.12.0/24")
   or with a range in the last octet ("192.168.12.64-97")
   -V        show Version information
   -f        show Full NBT resource record responses (recommended)
   -H        generate HTTP headers
   -v        turn on more Verbose debugging
   -n        No looking up inverse names of IP addresses responding
   -p <n>    bind to UDP Port <n> (default=0)
   -m        include MAC address in response (implied by '-f')
   -T <n>    Timeout the no-responses in <n> seconds (default=2 secs)
   -w <n>    Wait <n> msecs after each write (default=10 ms)
   -t <n>    Try each address <n> tries (default=1)
   -P        generate results in perl hashref format
Updated on: 2025-Dec-09
 Edit this page
nbtscan
ncat-w32
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install nbtscan-unixwiz`，再执行 `nbtscan-unixwiz --version` 2>/dev/null || `nbtscan-unixwiz -V`
- [ ] **2.** **读官方帮助** —— `nbtscan-unixwiz -h`，需要细节时 `man nbtscan-unixwiz`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `nbtscan-unixwiz -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/nbtscan-unixwiz/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[nbtscan](../../tools/tutorials/01-信息搜集/nbtscan.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/nbtscan-unixwiz/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/nbtscan-unixwiz/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
