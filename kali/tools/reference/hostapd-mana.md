# hostapd-mana

> Featureful rogue access point This package contains a eatureful rogue access point first presented at Defcon 22.

> **功能分类**：通用工具 ｜ **Kali 包**：`hostapd-mana` ｜ **官方文档**：<https://www.kali.org/tools/hostapd-mana/>

## 1. 安装

```bash
sudo apt update
sudo apt install hostapd-mana
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.6.5 |
| 架构 | any |
| 可执行命令 | `hostapd-mana`、`hostapd-mana_cli` |
| 依赖 | `libc6`、`libnl-3-200`、`libnl-genl-3-200`、`libssl3t64`、`openssl`、`ssl-cert` |
| 安装体积 | 1.29 MB |
| 官网 | <https://github.com/sensepost/hostapd-mana> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/hostapd-mana> |
| 包追踪 | <https://pkg.kali.org/pkg/hostapd-mana> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
hostapd-mana -h          # 查看用法
man hostapd-mana         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hostapd-mana`

官方给出的调用示例：`hostapd-mana --help`

```text
root@kali:~# hostapd-mana --help
hostapd-mana: invalid option -- '-'
hostapd-mana v2.6
User space daemon for IEEE 802.11 AP management,
IEEE 802.1X/WPA/WPA2/EAP/RADIUS Authenticator
Copyright (c) 2002-2016, Jouni Malinen <
[email protected]
> and contributors
--------------------------------------------------
MANA https://github.com/sensepost/hostapd-mana
By @singe (
[email protected]
)
Original MANA EAP by Ian (
[email protected]
)
Original karma patches by Robin Wood -
[email protected]
Original EAP patches by Brad Antoniewicz @brad_anton
Sycophant by Michael Kruger @_cablethief
usage: hostapd [-hdBKtv] [-P <PID file>] [-e <entropy file>] \
         [-g <global ctrl_iface>] [-G <group>]\
         [-i <comma-separated list of interface names>]\
         <configuration file(s)>
options:
   -h   show this usage
   -d   show more debug messages (-dd for even more)
   -B   run daemon in the background
   -e   entropy file
   -g   global control interface path
   -G   group for control interfaces
   -P   PID file
   -K   include key data in debug messages
   -i   list of interface names to use
   -S   start all the interfaces synchronously
   -t   include timestamps in some debug messages
   -v   show hostapd version
```

### `hostapd-mana_cli`

官方给出的调用示例：`hostapd-mana_cli -h`

```text
root@kali:~# hostapd-mana_cli -h
hostapd_cli v2.6
Copyright (c) 2004-2016, Jouni Malinen <
[email protected]
> and contributors
usage: hostapd_cli [-p<path>] [-i<ifname>] [-hvB] [-a<path>] \
                   [-P<pid file>] [-G<ping interval>] [command..]
Options:
   -h           help (show this usage text)
   -v           shown version information
   -p<path>     path to find control sockets (default: /var/run/hostapd-mana)
   -s<dir_path> dir path to open client sockets (default: /var/run/hostapd-mana)
   -a<file>     run in daemon mode executing the action file based on events
                from hostapd
   -B           run a daemon in the background
   -i<ifname>   Interface to listen on (default: first interface found in the
                socket path)
commands:
  ping = pings hostapd
  mib = get MIB variables (dot1x, dot11, radius)
  sta <addr> = get MIB variables for one station
  all_sta = get MIB variables for all stations
  new_sta <addr> = add a new station
  deauthenticate <addr> = deauthenticate a station
  disassociate <addr> = disassociate a station
  signature <addr> = get taxonomy signature for a station
  sa_query <addr> = send SA Query to a station
  get_config = show current configuration
  help = show this usage help
  interface [ifname] = show interfaces/select interface
  level <debug level> = change debug level
  license = show full hostapd_cli license
  quit = exit hostapd_cli
  mana_change_ssid = change the default SSID for when mana is off
  mana_get_ssid = get the default SSID for when mana is off
  mana_get_state = get whether mana is enabled or not
  mana_disable = disable mana
  mana_enable = enable mana
  mana_loud_off = disable mana's loud mode
  mana_loud_on = enable mana's loud mode
  mana_loud_state = check mana's loud mode
  mana_macacl_off = disable MAC ACLs at management frame level
  mana_macacl_on = enable MAC ACLs at management frame level
  mana_macacl_state = check mana's MAC ACL mode
  mana_wpe_off = disable mana's wpe mode
  mana_wpe_on = enable mana's wpe mode
  mana_wpe_state = check mana's wpe mode
  mana_eapsuccess_off = disable mana's eapsuccess mode
  mana_eapsuccess_on = enable mana's eapsuccess mode
  mana_eapsuccess_state = check mana's eapsuccess mode
  mana_eaptls_off = disable mana's eaptls mode
  mana_eaptls_on = enable mana's eaptls mode
  mana_eaptls_state = check mana's eaptls mode
  sycophant_get_state = get whether sycophant is enabled or not
  sycophant_disable = disable sycophant
  sycophant_enable = enable sycophant
Learn more with
OffSec
Want to learn more about hostapd-mana? get access to in-depth training and hands-on labs:
PEN-210: 9.3.1. Rogue Access Points: Building the hostapd-mana Configuration
PEN-210: 11. Attacking WPA Enterprise
PEN-210 course
Updated on: 2025-Dec-09
 Edit this page
horst
hostapd-wpe
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install hostapd-mana`，再执行 `hostapd-mana --version` 2>/dev/null || `hostapd-mana -V`
- [ ] **2.** **读官方帮助** —— `hostapd-mana -h`，需要细节时 `man hostapd-mana`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `hostapd-mana -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hostapd-mana/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hostapd-mana/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hostapd-mana/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
