# wifite

> Python script to automate wireless auditing using aircrack-ng tools Wifite is a tool to audit WEP or WPA encrypted wireless networks. It uses aircrack-ng, pyrit, reaver, tshark tools to perform the audit. This tool is customizable to be au…

> **功能分类**：无线攻击 ｜ **Kali 包**：`wifite` ｜ **官方文档**：<https://www.kali.org/tools/wifite/>

## 1. 安装

```bash
sudo apt update
sudo apt install wifite
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.8.2 |
| 架构 | all |
| 可执行命令 | `wifite` |
| 依赖 | `aircrack-ng`、`ieee-data`、`net-tools`、`python3`、`python3-chardet`、`reaver`、`tshark` |
| 安装体积 | 8.01 MB |
| 官网 | <https://github.com/kimocoder/wifite2> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/wifite> |
| 包追踪 | <https://pkg.kali.org/pkg/wifite> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Attack access points with over 50 dB of power (-pow 50) using the WPS attack (-wps):
root@kali:~# wifite -pow 50 -wps

  .;'                     `;,
 .;'  ,;'             `;,  `;,   WiFite v2 (r85)
.;'  ,;'  ,;'     `;,  `;,  `;,
::   ::   :   ( )   :   ::   ::  automated wireless auditor
':.  ':.  ':. /_\ ,:'  ,:'  ,:'
 ':.  ':.    /___\    ,:'  ,:'   designed for Linux
  ':.       /_____\      ,:'
           /       \

 [+] targeting WPS-enabled networks

 [+] scanning for wireless devices...
 [+] enabling monitor mode on wlan0... done
 [+] initializing scan (mon0), updates at 5 sec intervals, CTRL+C when ready.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wifite`

官方给出的调用示例：`wifite -pow 50 -wps`

```text
root@kali:~# wifite -pow 50 -wps
  .;'                     `;,
 .;'  ,;'             `;,  `;,   WiFite v2 (r85)
.;'  ,;'  ,;'     `;,  `;,  `;,
::   ::   :   ( )   :   ::   ::  automated wireless auditor
':.  ':.  ':. /_\ ,:'  ,:'  ,:'
 ':.  ':.    /___\    ,:'  ,:'   designed for Linux
  ':.       /_____\      ,:'
           /       \
 [+] targeting WPS-enabled networks
 [+] scanning for wireless devices...
 [+] enabling monitor mode on wlan0... done
 [+] initializing scan (mon0), updates at 5 sec intervals, CTRL+C when ready.
```

### `wifite（示例）`

官方给出的调用示例：`wifite -h`

```text
root@kali:~# wifite -h
   .               .
 .´  ·  .     .  ·  `.  wifite2 2.8.1
 :  :  :  (¯)  :  :  :  a wireless auditor by derv82
 `.  ·  ` /¯\ ´  ·  .´  maintained by kimocoder
   `     /¯¯¯\     ´    https://github.com/kimocoder/wifite2
options:
  -h, --help                    show this help message and exit
SETTINGS:
  -v, --verbose                 Shows more options (-h -v). Prints commands and outputs. (default: quiet)
  -i [interface]                Wireless interface to use, e.g. wlan0mon (default: ask)
  -c [channel]                  Wireless channel to scan e.g. 1,3-6 (default: all 2Ghz channels)
  -inf, --infinite              Enable infinite attack mode. Modify scanning time with -p (default: off)
  -mac, --random-mac            Randomize wireless card MAC address (default: off)
  -p [scan_time]                Pillage: Attack all targets after scan_time (seconds)
  --kill                        Kill processes that conflict with Airmon/Airodump (default: off)
  -pow, --power [min_power]     Attacks any targets with at least min_power signal strength
  --skip-crack                  Skip cracking captured handshakes/pmkid (default: off)
  -first, --first [attack_max]  Attacks the first attack_max targets
  -ic, --ignore-cracked         Hides previously-cracked targets. (default: off)
  --clients-only                Only show targets that have associated clients (default: off)
  --nodeauths                   Passive mode: Never deauthenticates clients (default: deauth targets)
  --daemon                      Puts device back in managed mode after quitting (default: off)
WEP:
  --wep                         Show only WEP-encrypted networks
  --require-fakeauth            Fails attacks if fake-auth fails (default: off)
  --keep-ivs                    Retain .IVS files and reuse when cracking (default: off)
WPA:
  --wpa                         Show only WPA/WPA2-encrypted networks (may include WPS)
  --wpa3                        Show only WPA3-encrypted networks (SAE/OWE)
  --owe                         Show only OWE-encrypted networks (Enhanced Open)
  --new-hs                      Captures new handshakes, ignores existing handshakes in hs (default: off)
  --dict [file]                 File containing passwords for cracking (default: /usr/share/dict/wordlist-probable.txt)
WPS:
  --wps                         Show only WPS-enabled networks
  --wps-only                    Only use WPS PIN & Pixie-Dust attacks (default: off)
  --bully                       Use bully program for WPS PIN & Pixie-Dust attacks (default: reaver)
  --reaver                      Use reaver program for WPS PIN & Pixie-Dust attacks (default: reaver)
  --ignore-locks                Do not stop WPS PIN attack if AP becomes locked (default: stop)
PMKID:
  --pmkid                       Only use PMKID capture, avoids other WPS & WPA attacks (default: off)
  --no-pmkid                    Don't use PMKID capture (default: off)
  --pmkid-timeout [sec]         Time to wait for PMKID capture (default: 300 seconds)
COMMANDS:
  --cracked                     Print previously-cracked access points
  --ignored                     Print ignored access points
  --check [file]                Check a .cap file (or all hs/*.cap files) for WPA handshakes
  --crack                       Show commands to crack a captured handshake
  --update-db                   Update the local MAC address prefix database from IEEE registries
Learn more with
OffSec
Want to learn more about wifite? get access to in-depth training and hands-on labs:
PEN-210: 6.2.4. Aircrack-ng Essentials: Airodump-ng Output Files
PEN-210 course
Updated on: 2026-Mar-02
 Edit this page
whois
witnessme
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install wifite`，再执行 `wifite --version` 2>/dev/null || `wifite -V`
- [ ] **2.** **读官方帮助** —— `wifite -h`，需要细节时 `man wifite`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `wifite -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wifite/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[wifite](../../tools/tutorials/05-无线攻击/wifite.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wifite/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wifite/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
