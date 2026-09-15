# mdk4

> Wireless attack tool for IEEE 802.11 networks This package contains a proof-of-concept tool to exploit common IEEE 802.11 protocol weaknesses. MDK4 is a new version of MDK3. MDK4 is a Wi-Fi testing tool from E7mer of 360PegasusTeam, ASPj o…

> **功能分类**：无线攻击 ｜ **Kali 包**：`mdk4` ｜ **官方文档**：<https://www.kali.org/tools/mdk4/>

## 1. 安装

```bash
sudo apt update
sudo apt install mdk4
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.2 |
| 架构 | any |
| 可执行命令 | `mdk4` |
| 依赖 | `aircrack-ng`、`libc6`、`libnl-3-200`、`libnl-genl-3-200`、`libpcap0.8t64` |
| 安装体积 | 236 KB |
| 官网 | <https://github.com/aircrack-ng/mdk4> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/mdk4> |
| 包追踪 | <https://pkg.kali.org/pkg/mdk4> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
mdk4 -h          # 查看用法
man mdk4         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `mdk4`

官方给出的调用示例：`mdk4 -h`

```text
root@kali:~# mdk4 -h
MDK4 4.2 - "Awesome! Supports Proof-of-concept of WiFi protocol implementation vulnerability testing"
by E7mer, thanks to the author of MDK3 and aircrack-ng community.
MDK4 is a proof-of-concept tool to exploit common IEEE 802.11 protocol weaknesses.
IMPORTANT: It is your responsibility to make sure you have permission from the
network owner before running MDK4 against it.
This code is licenced under the GPLv3 or later
MDK4 USAGE:
mdk4 <interface> <attack_mode> [attack_options]
mdk4 <interface in> <interface out> <attack_mode> [attack_options]
Try mdk4 --fullhelp for all attack options
Try mdk4 --help <attack_mode> for info about one attack only
###### This version supports IDS Evasion (Ghosting) ######
# Just append  --ghost <period>,<max_rate>,<min_txpower> #
# after your attack mode identifier to enable ghosting!  #
# <period>      : How often (in ms) to switch rate/power #
# <max_rate>    : Maximum Bitrate to use in MBit         #
# <min_txpower> : Minimum TX power in dBm to use         #
# NOTE: Does not fully work with every driver, YMMV...   #
##########################################################
#### This version supports IDS Evasion  (Fragmenting) ####
# Just append  --frag <min_frags>,<max_frags>,<percent>  #
# after your attack mode identifier to fragment all      #
# outgoing packets, possibly avoiding lots of IDS!       #
# <min_frags> : Minimum fragments to split packets into  #
# <max_frags> : Maximum amount of fragments to create    #
# <percent>   : Percantage of packets to fragment        #
# NOTE: May not fully work with every driver, YMMV...    #
# HINT: Set max_frags to 0 to enable standard compliance #
##########################################################
Loaded 10 attack modules
ATTACK MODE b: Beacon Flooding
  Sends beacon frames to show fake APs at clients.
  This can sometimes crash network scanners and even drivers!
ATTACK MODE a: Authentication Denial-Of-Service
  Sends authentication frames to all APs found in range.
  Too many clients can freeze or reset several APs.
ATTACK MODE p: SSID Probing and Bruteforcing
  Probes APs and checks for answer, useful for checking if SSID has
  been correctly decloaked and if AP is in your sending range.
  Bruteforcing of hidden SSIDs with or without a wordlist is also available.
ATTACK MODE d: Deauthentication and Disassociation
  Sends deauthentication and disassociation packets to stations
  based on data traffic to disconnect all clients from an AP.
ATTACK MODE m: Michael Countermeasures Exploitation
  Sends random packets or re-injects duplicates on another QoS queue
  to provoke Michael Countermeasures on TKIP APs.
  AP will then shutdown for a whole minute, making this an effective DoS.
ATTACK MODE e: EAPOL Start and Logoff Packet Injection
  Floods an AP with EAPOL Start frames to keep it busy with fake sessions
  and thus disables it to handle any legitimate clients.
  Or logs off clients by injecting fake EAPOL Logoff messages.
ATTACK MODE s: Attacks for IEEE 802.11s mesh networks
  Various attacks on link management and routing in mesh networks.
  Flood neighbors and routes, create black holes and divert traffic!
ATTACK MODE w: WIDS Confusion
  Confuse/Abuse Intrusion Detection and Prevention Systems by
  cross-connecting clients to multiple WDS nodes or fake rogue APs.
ATTACK MODE f: Packet Fuzzer
  A simple packet fuzzer with multiple packet sources
  and a nice set of modifiers. Be careful!
ATTACK MODE x: Proof-of-concept of WiFi protocol implementation vulnerability testing
  Proof-of-concept of WiFi protocol implementation vulnerability,
  to test whether the device has wifi vulnerabilities.
  It may cause the wifi connection to be disconnected or the target device to crash.
Updated on: 2025-Dec-09
 Edit this page
mdk3
medusa
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install mdk4`，再执行 `mdk4 --version` 2>/dev/null || `mdk4 -V`
- [ ] **2.** **读官方帮助** —— `mdk4 -h`，需要细节时 `man mdk4`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `mdk4 -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/mdk4/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/mdk4/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/mdk4/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
