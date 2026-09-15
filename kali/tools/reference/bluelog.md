# bluelog

> Bluetooth scanner and logger Bluelog is a Bluetooth scanner designed to tell you how many discoverable devices there are in an area as quickly as possible. It is intended to be used as a site survey tool, identifying the number of possible…

> **功能分类**：无线攻击 ｜ **Kali 包**：`bluelog` ｜ **官方文档**：<https://www.kali.org/tools/bluelog/>

## 1. 安装

```bash
sudo apt update
sudo apt install bluelog
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1.2 |
| 架构 | any |
| 可执行命令 | `bluelog` |
| 依赖 | `bluez`、`ieee-data`、`libbluetooth-dev`、`libbluetooth3`、`libc6` |
| 安装体积 | 198 KB |
| 官网 | <http://www.digifail.com/software/bluelog.shtml> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/bluelog> |
| 包追踪 | <https://pkg.kali.org/pkg/bluelog> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# bluelog
Bluelog (v1.1.2) by MS3FGX
---------------------------
Autodetecting device...OK
Opening output file: bluelog-2014-05-15-1651.log...OK
Writing PID file: /tmp/bluelog.pid...OK
Scan started at [05/15/14 16:51:46] on 00:19:0E:0E:EA:4B.
Hit Ctrl+C to end scan.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `bluelog`

```text
root@kali:~# bluelog
Bluelog (v1.1.2) by MS3FGX
---------------------------
Autodetecting device...OK
Opening output file: bluelog-2014-05-15-1651.log...OK
Writing PID file: /tmp/bluelog.pid...OK
Scan started at [05/15/14 16:51:46] on 00:19:0E:0E:EA:4B.
Hit Ctrl+C to end scan.
```

### `bluelog -h`

> 官方示例调用：`bluelog -h`

```text
root@kali:~# bluelog -h
Bluelog (v1.1.2) by Tom Nardi "MS3FGX" (
[email protected]
)
----------------------------------------------------------------
Bluelog is a Bluetooth site survey tool, designed to tell you how
many discoverable devices there are in an area as quickly as possible.
As the name implies, its primary function is to log discovered devices
to file rather than to be used interactively. Bluelog could run on a
system unattended for long periods of time to collect data.
Bluelog also includes a mode called "Bluelog Live" which creates a
webpage of the results that you can serve up with your HTTP daemon of
choice. See the "README.LIVE" file for details.
For more information, see: www.digifail.com
Basic Options:
	-i <interface>     Sets scanning device, default is "hci0"
	-o <filename>      Sets output filename, default is "devices.log"
	-v                 Verbose, prints discovered devices to the terminal
	-q                 Quiet, turns off nonessential terminal outout
	-d                 Enables daemon mode, Bluelog will run in background
	-k                 Kill an already running Bluelog process
	-l                 Start "Bluelog Live", default is disabled
Logging Options:
	-n                 Write device names to log, default is disabled
	-m                 Write device manufacturer to log, default is disabled
	-c                 Write device class to log, default is disabled
	-f                 Use "friendly" device class, default is disabled
	-t                 Write timestamps to log, default is disabled
	-x                 Obfuscate discovered MACs, default is disabled
	-e                 Encode discovered MACs with CRC32, default disabled
	-b                 Enable BlueProPro log format, see README
Advanced Options:
	-r <retries>       Name resolution retries, default is 3
	-a <minutes>       Amnesia, Bluelog will forget device after given time
	-w <seconds>       Scanning window in seconds, see README
	-s                 Syslog only mode, no log file. Default is disabled
Updated on: 2025-Dec-09
 Edit this page
bloodhound.py
bopscrk
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install bluelog`，再执行 `bluelog --version` 2>/dev/null || `bluelog -V`
- [ ] **2.** **读官方帮助** —— `bluelog -h`，需要细节时 `man bluelog`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `bluelog -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/bluelog/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/bluelog/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/bluelog/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
