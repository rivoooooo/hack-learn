# horst

> Highly Optimized Radio Scanning Tool horst is a small, lightweight IEEE802.11 WLAN analyzer with a text interface. Its basic function is similar to tcpdump, Wireshark or Kismet, but it’s much smaller and shows different, aggregated informa…

> **功能分类**：通用工具 ｜ **Kali 包**：`horst` ｜ **官方文档**：<https://www.kali.org/tools/horst/>

## 1. 安装

```bash
sudo apt update
sudo apt install horst
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.1 |
| 架构 | any |
| 可执行命令 | `horst` |
| 依赖 | `libc6`、`libncurses6`、`libnl-3-200`、`libnl-genl-3-200`、`libtinfo6` |
| 安装体积 | 155 KB |
| 官网 | <https://github.com/br101/horst> |
| 源码仓库 | <https://salsa.debian.org/debian/horst> |
| 包追踪 | <https://pkg.kali.org/pkg/horst> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
horst -h          # 查看用法
man horst         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `horst`

> 官方示例调用：`horst -h`

```text
root@kali:~# horst -h
Usage: horst [options]
General Options: Description (default value)
  -v		show version
  -h		Help
  -q		Quiet, no output
  -D		Show lots of debug output, no UI
  -a		Always add virtual monitor interface
  -c <file>	Config file (/etc/horst.conf)
  -C <chan>	Set initial channel
  -i <intf>	Interface name (wlan0)
  -t <sec>	Node timeout in seconds (60)
  -d <ms>	Display update interval in ms (100)
  -V view	Display view: history|essid|statistics|spectrum
  -b <bytes>	Receive buffer size in bytes (not set)
  -M[filename]	MAC address to host name mapping (/tmp/dhcp.leases)
Feature Options:
  -s		(Poor mans) Spectrum analyzer mode
  -u		Upper channel limit
  -N		Allow network connection, server mode (off)
  -n <IP>	Connect to server with <IP>, client mode (off)
  -p <port>	Port number of server (4444)
  -o <filename>	Write packet info into 'filename'
  -X[filename]	Allow control socket on 'filename' (/tmp/horst)
  -x <command>	Send control command
Filter Options:
 Filters are generally 'positive' or 'inclusive' which means you define
 what you want to see, and everything else is getting filtered out.
 If a filter is not set it is inactive and nothing is filtered.
 Most filter options can be specified multiple times and will be combined
  -e <MAC>	Source MAC addresses (xx:xx:xx:xx:xx:xx), up to 9 times
  -f <PKT_NAME>	Filter packet types, multiple
  -m <MODE>	Operating mode: AP|STA|ADH|PRB|WDS|UNKNOWN, multiple
  -B <MAC>	BSSID (xx:xx:xx:xx:xx:xx), only one
Updated on: 2025-Dec-09
 Edit this page
hexwalk
hostapd-mana
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install horst`，再执行 `horst --version` 2>/dev/null || `horst -V`
- [ ] **2.** **读官方帮助** —— `horst -h`，需要细节时 `man horst`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: horst [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/horst/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/horst/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/horst/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
