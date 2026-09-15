# reaver

> Brute force attack tool against Wi-Fi Protected Setup PIN number Reaver performs a brute force attack against an access point’s Wi-Fi Protected Setup pin number. Once the WPS pin is found, the WPA PSK can be recovered and alternately the A…

> **功能分类**：无线攻击 ｜ **Kali 包**：`reaver` ｜ **官方文档**：<https://www.kali.org/tools/reaver/>

## 1. 安装

```bash
sudo apt update
sudo apt install reaver
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6.6 |
| 架构 | any |
| 可执行命令 | `reaver`、`wash` |
| 依赖 | `libc6`、`libpcap0.8t64` |
| 安装体积 | 851 KB |
| 官网 | <https://github.com/t6x/reaver-wps-fork-t6x> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/reaver> |
| 包追踪 | <https://pkg.kali.org/pkg/reaver> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan for networks using the monitor mode interface (-i wlan0mon) on channel 6 (-c 6), while ignoring frame checksum errors (-C):
root@kali:~# wash -i wlan0mon -c 6 -C
BSSID               Ch  dBm  WPS  Lck  Vendor    ESSID
--------------------------------------------------------------------------------
E0:3F:49:6A:57:78    6  -73  1.0  No   Unknown   ASUS

reaver Usage Example
Use the monitor mode interface (-i mon0) to attack the access point (-b E0:3F:49:6A:57:78), displaying verbose output (-v):
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wash`

官方给出的调用示例：`wash -i wlan0mon -c 6 -C`

```text
root@kali:~# wash -i wlan0mon -c 6 -C
BSSID               Ch  dBm  WPS  Lck  Vendor    ESSID
--------------------------------------------------------------------------------
E0:3F:49:6A:57:78    6  -73  1.0  No   Unknown   ASUS
reaver Usage Example
Use the monitor mode interface (
-i mon0
) to attack the access point (
-b E0:3F:49:6A:57:78
), displaying verbose output (
-v
):
```

### `reaver`

官方给出的调用示例：`reaver -i wlan0mon -b E0:3F:49:6A:57:78 -v`

```text
root@kali:~# reaver -i wlan0mon -b E0:3F:49:6A:57:78 -v
Reaver v1.6.5 WiFi Protected Setup Attack Tool
Copyright (c) 2011, Tactical Network Solutions, Craig Heffner <
[email protected]
>
[+] Waiting for beacon from E0:3F:49:6A:57:78
[+] Associated with E0:3F:49:6A:57:78 (ESSID: ASUS)
[+] Trying pin 12345670
```

### `reaver（示例）`

官方给出的调用示例：`reaver -h`

```text
root@kali:~# reaver -h
Reaver v1.6.6 WiFi Protected Setup Attack Tool
Copyright (c) 2011, Tactical Network Solutions, Craig Heffner <
[email protected]
>
Required Arguments:
	-i, --interface=<wlan>          Name of the monitor-mode interface to use
	-b, --bssid=<mac>               BSSID of the target AP
Optional Arguments:
	-m, --mac=<mac>                 MAC of the host system
	-e, --essid=<ssid>              ESSID of the target AP
	-c, --channel=<channel>         Set the 802.11 channel for the interface (implies -f)
	-s, --session=<file>            Restore a previous session file
	-C, --exec=<command>            Execute the supplied command upon successful pin recovery
	-f, --fixed                     Disable channel hopping
	-5, --5ghz                      Use 5GHz 802.11 channels
	-v, --verbose                   Display non-critical warnings (-vv or -vvv for more)
	-q, --quiet                     Only display critical messages
	-h, --help                      Show help
Advanced Options:
	-p, --pin=<wps pin>             Use the specified pin (may be arbitrary string or 4/8 digit WPS pin)
	-d, --delay=<seconds>           Set the delay between pin attempts [1]
	-l, --lock-delay=<seconds>      Set the time to wait if the AP locks WPS pin attempts [60]
	-g, --max-attempts=<num>        Quit after num pin attempts
	-x, --fail-wait=<seconds>       Set the time to sleep after 10 unexpected failures [0]
	-r, --recurring-delay=<x:y>     Sleep for y seconds every x pin attempts
	-t, --timeout=<seconds>         Set the receive timeout period [10]
	-T, --m57-timeout=<seconds>     Set the M5/M7 timeout period [0.40]
	-A, --no-associate              Do not associate with the AP (association must be done by another application)
	-N, --no-nacks                  Do not send NACK messages when out of order packets are received
	-S, --dh-small                  Use small DH keys to improve crack speed
	-L, --ignore-locks              Ignore locked state reported by the target AP
	-E, --eap-terminate             Terminate each WPS session with an EAP FAIL packet
	-J, --timeout-is-nack           Treat timeout as NACK (DIR-300/320)
	-F, --ignore-fcs                Ignore frame checksum errors
	-w, --win7                      Mimic a Windows 7 registrar [False]
	-K, --pixie-dust                Run pixiedust attack
	-Z                              Run pixiedust attack
	-O, --output-file=<filename>    Write packets of interest into pcap file
Example:
	reaver -i wlan0mon -b 00:90:4C:C1:AC:21 -vv
```

### `wash（示例）`

官方给出的调用示例：`wash -h`

```text
root@kali:~# wash -h
Wash v1.6.6 WiFi Protected Setup Scan Tool
Copyright (c) 2011, Tactical Network Solutions, Craig Heffner
Required Arguments:
	-i, --interface=<iface>              Interface to capture packets on
	-f, --file [FILE1 FILE2 FILE3 ...]   Read packets from capture files
Optional Arguments:
	-c, --channel=<num>                  Channel to listen on [auto]
	-n, --probes=<num>                   Maximum number of probes to send to each AP in scan mode [15]
	-O, --output-file=<filename>         Write packets of interest into pcap file
	-F, --ignore-fcs                     Ignore frame checksum errors
	-2, --2ghz                           Use 2.4GHz 802.11 channels
	-5, --5ghz                           Use 5GHz 802.11 channels
	-s, --scan                           Use scan mode
	-u, --survey                         Use survey mode [default]
	-a, --all                            Show all APs, even those without WPS
	-j, --json                           print extended WPS info as json
	-U, --utf8                           Show UTF8 ESSID (does not sanitize ESSID, dangerous)
	-p, --progress                       Show percentage of crack progress
	-h, --help                           Show help
Example:
	wash -i wlan0mon
Learn more with
OffSec
Want to learn more about reaver? get access to in-depth training and hands-on labs:
PEN-210: 8.3. Attacking WPS Networks: WPS Attack
PEN-210 course
Updated on: 2026-Jun-17
 Edit this page
rdesktop
shell-gpt
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install reaver`，再执行 `reaver --version` 2>/dev/null || `reaver -V`
- [ ] **2.** **读官方帮助** —— `reaver -h`，需要细节时 `man reaver`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `reaver -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/reaver/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[reaver](../../tools/tutorials/05-无线攻击/reaver.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/reaver/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/reaver/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
