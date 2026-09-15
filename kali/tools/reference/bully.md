# bully

> Implementation of the WPS brute force attack, written in C Bully is a new implementation of the WPS brute force attack, written in C. It is conceptually identical to other programs, in that it exploits the (now well known) design flaw in t…

> **功能分类**：无线攻击 ｜ **Kali 包**：`bully` ｜ **官方文档**：<https://www.kali.org/tools/bully/>

## 1. 安装

```bash
sudo apt update
sudo apt install bully
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.4.00 |
| 架构 | any |
| 可执行命令 | `bully` |
| 依赖 | `aircrack-ng`、`libc6`、`liblua5.3-0`、`libpcap0.8t64`、`pixiewps` |
| 安装体积 | 175 KB |
| 官网 | <https://github.com/kimocoder/bully> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/bully> |
| 包追踪 | <https://pkg.kali.org/pkg/bully> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Attack the wireless ESSID (-e 6F36E6) through the monitor mode interface (wlan0mon):
root@kali:~# bully -e 6F36E6 wlan0mon
[!] Bully v1.0-22 - WPS vulnerability assessment utility
[X] Unknown frequency '-113135872' reported by interface 'mon0'
[!] Using '00:1f:33:f3:51:13' for the source MAC address
[+] Datalink type set to '127', radiotap headers present
[+] Scanning for beacon from '6F36E6' on channel 'unknown'
[+] Got beacon for '6F36E6' (9c:d3:6d:b8:ff:56)
[+] Switching interface 'mon0' to channel '8'
[!] Beacon information element indicates WPS is locked
[!] Creating new randomized pin file '/root/.bully/pins'
[+] Index of starting pin number is '0000000'
[+] Last State = 'NoAssoc'   Next pin '54744431'
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `bully`

> 官方示例调用：`bully -e 6F36E6 wlan0mon`

```text
root@kali:~# bully -e 6F36E6 wlan0mon
[!] Bully v1.0-22 - WPS vulnerability assessment utility
[X] Unknown frequency '-113135872' reported by interface 'mon0'
[!] Using '00:1f:33:f3:51:13' for the source MAC address
[+] Datalink type set to '127', radiotap headers present
[+] Scanning for beacon from '6F36E6' on channel 'unknown'
[+] Got beacon for '6F36E6' (9c:d3:6d:b8:ff:56)
[+] Switching interface 'mon0' to channel '8'
[!] Beacon information element indicates WPS is locked
[!] Creating new randomized pin file '/root/.bully/pins'
[+] Index of starting pin number is '0000000'
[+] Last State = 'NoAssoc'   Next pin '54744431'
```

### `bully -h`

> 官方示例调用：`bully -h`

```text
root@kali:~# bully -h
  bully v1.4
  the fork that actually works!
  maintained by kimocoder - https://twitter.com/kimocoder
  usage: bully <options> interface
  Required arguments:
      interface      : Wireless interface in monitor mode (root required)
      -b, --bssid macaddr    : MAC address of the target access point
   Or
      -e, --essid string     : Extended SSID for the access point
  Optional arguments:
      -c, --channel N[,N...] : Channel number of AP, or list to hop [b/g]
      -i, --index N          : Starting pin index (7 or 8 digits)  [Auto]
      -l, --lockwait N       : Seconds to wait if the AP locks WPS   [43]
      -o, --outfile file     : Output file for messages          [stdout]
      -p, --pin N            : Starting pin number (7 or 8 digits) [Auto]
      -s, --source macaddr   : Source (hardware) MAC address      [Probe]
      -u, --lua              : Lua script file
      -v, --verbosity N      : Verbosity level 1-4, 1 is quietest     [3]
      -w, --workdir path     : Location of pin/session files  [~/.bully/]
      -5, --5ghz             : Hop on 5GHz a/n default channel list  [No]
      -B, --bruteforce       : Bruteforce the WPS pin checksum digit [No]
      -F, --force            : Force continue in spite of warnings   [No]
      -S, --sequential       : Sequential pins (do not randomize)    [No]
      -T, --test             : Test mode (do not inject any packets) [No]
  Advanced arguments:
      -d, --pixiewps         : Attempt to use pixiewps               [No]
      -a, --acktime N        : Deprecated/ignored                  [Auto]
      -r, --retries N        : Resend packets N times when not acked  [2]
      -m, --m13time N        : Deprecated/ignored                  [Auto]
      -t, --timeout N        : Deprecated/ignored                  [Auto]
      -1, --pin1delay M,N    : Delay M seconds every Nth nack at M5 [0,1]
      -2, --pin2delay M,N    : Delay M seconds every Nth nack at M7 [5,1]
      -A, --noacks           : Disable ACK check for sent packets    [No]
      -C, --nocheck          : Skip CRC/FCS validation (performance) [No]
      -D, --detectlock       : Detect WPS lockouts unreported by AP  [No]
      -E, --eapfail          : EAP Failure terminate every exchange  [No]
      -L, --lockignore       : Ignore WPS locks reported by the AP   [No]
      -M, --m57nack          : M5/M7 timeouts treated as WSC_NACK's  [No]
      -N, --nofcs            : Packets don't contain the FCS field [Auto]
      -P, --probe            : Use probe request for nonbeaconing AP [No]
      -Q, --wpsinfo          : Use probe request to gather WPS info  [No]
      -R, --radiotap         : Assume radiotap headers are present [Auto]
      -W, --windows7         : Masquerade as a Windows 7 registrar   [No]
      -Z, --suppress         : Suppress packet throttling algorithm  [No]
      -V, --version          : Print version info and exit
      -h, --help             : Display this help information
Learn more with
OffSec
Want to learn more about bully? get access to in-depth training and hands-on labs:
PEN-210: 8.3. Attacking WPS Networks: WPS Attack
PEN-210 course
Updated on: 2025-Dec-09
 Edit this page
brutespray
cabextract
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install bully`，再执行 `bully --version` 2>/dev/null || `bully -V`
- [ ] **2.** **读官方帮助** —— `bully -h`，需要细节时 `man bully`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `bully -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/bully/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/bully/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/bully/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
