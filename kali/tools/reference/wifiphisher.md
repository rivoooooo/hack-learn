# wifiphisher

> Automated phishing attacks against Wi-Fi networks This package contains a security tool that mounts automated phishing attacks against Wi-Fi networks in order to obtain secret passphrases or other credentials. It is a social engineering at…

> **功能分类**：通用工具 ｜ **Kali 包**：`wifiphisher` ｜ **官方文档**：<https://www.kali.org/tools/wifiphisher/>

## 1. 安装

```bash
sudo apt update
sudo apt install wifiphisher
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.4 |
| 架构 | all |
| 可执行命令 | `wifiphisher` |
| 依赖 | `cowpatty`、`dnsmasq-base`、`hostapd`、`iptables`、`net-tools`、`python3`、`python3-pbkdf2`、`python3-pyric`、`python3-roguehostapd`、`python3-scapy`、`python3-six`、`python3-tornado` |
| 安装体积 | 7.89 MB |
| 官网 | <https://github.com/sophron/wifiphisher> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/wifiphisher> |
| 包追踪 | <https://pkg.kali.org/pkg/wifiphisher> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
wifiphisher -h          # 查看用法
man wifiphisher         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wifiphisher`

> 官方示例调用：`wifiphisher -nJ -e "Free Wi-Fi" -T firmware-upgrade`

```text
root@kali:~# wifiphisher -nJ -e "Free Wi-Fi" -T firmware-upgrade
[*] Starting Wifiphisher 1.1GIT at 2017-02-22 13:52
[+] Selecting wlan0 interface for creating the rogue Access Point
[*] Cleared leases, started DHCP, set up iptables
[+] Selecting Firmware Upgrade Page template
[*] Starting the fake access point...
Jamming devices:
DHCP Leases:
1487839973 c0:cc:f8:06:53:93 10.0.0.93 Victims-iPhone 11:c0:cc:38:66:a3:b3
HTTP requests:
[*] GET 10.0.0.93
[*] GET 10.0.0.93
[*] GET 10.0.0.93
[*] POST 10.0.0.93 wfphshr-wpa-password=s3cr3tp4s5
[*] GET 10.0.0.93
[*] GET 10.0.0.93
[*] GET 10.0.0.93
```

### `wifiphisher -h`

> 官方示例调用：`wifiphisher -h`

```text
root@kali:~# wifiphisher -h
usage: wifiphisher [-h] [-i INTERFACE] [-eI EXTENSIONSINTERFACE]
                   [-aI APINTERFACE] [-iI INTERNETINTERFACE]
                   [-pI PROTECTINTERFACE [PROTECTINTERFACE ...]]
                   [-mI MITMINTERFACE] [-iAM MAC_AP_INTERFACE]
                   [-iEM MAC_EXTENSIONS_INTERFACE] [-iNM] [-kN] [-nE] [-nD]
                   [-dC DEAUTH_CHANNELS [DEAUTH_CHANNELS ...]] [-e ESSID]
                   [-dE DEAUTH_ESSID] [-p PHISHINGSCENARIO] [-pK PRESHAREDKEY]
                   [-hC HANDSHAKE_CAPTURE] [-qS] [-lC] [-lE LURE10_EXPLOIT]
                   [--logging] [-dK] [-lP LOGPATH] [-cP CREDENTIAL_LOG_PATH]
                   [--payload-path PAYLOAD_PATH] [-cM] [-wP]
                   [-wAI WPSPBC_ASSOC_INTERFACE] [-kB] [-fH]
                   [-pPD PHISHING_PAGES_DIRECTORY]
                   [--dnsmasq-conf DNSMASQ_CONF] [-pE PHISHING_ESSID]
options:
  -h, --help            show this help message and exit
  -i, --interface INTERFACE
                        Manually choose an interface that supports both AP and
                        monitor modes for spawning the rogue AP as well as
                        mounting additional Wi-Fi attacks from Extensions
                        (i.e. deauth). Example: -i wlan1
  -eI, --extensionsinterface EXTENSIONSINTERFACE
                        Manually choose an interface that supports monitor
                        mode for deauthenticating the victims. Example: -eI
                        wlan1
  -aI, --apinterface APINTERFACE
                        Manually choose an interface that supports AP mode for
                        spawning the rogue AP. Example: -aI wlan0
  -iI, --internetinterface INTERNETINTERFACE
                        Choose an interface that is connected on the
                        InternetExample: -iI ppp0
  -pI, --protectinterface PROTECTINTERFACE [PROTECTINTERFACE ...]
                        Specify the interface(s) that will have their
                        connection protected (i.e. NetworkManager will be
                        prevented from controlling them). Example: -pI wlan1
                        wlan2
  -mI, --mitminterface MITMINTERFACE
                        Choose an interface that is connected on the Internet
                        in order to perform a MITM attack. All other
                        interfaces will be protected.Example: -mI wlan1
  -iAM, --mac-ap-interface MAC_AP_INTERFACE
                        Specify the MAC address of the AP interface
  -iEM, --mac-extensions-interface MAC_EXTENSIONS_INTERFACE
                        Specify the MAC address of the extensions interface
  -iNM, --no-mac-randomization
                        Do not change any MAC address
  -kN, --keepnetworkmanager
                        Do not kill NetworkManager
  -nE, --noextensions   Do not load any extensions.
  -nD, --nodeauth       Skip the deauthentication phase.
  -dC, --deauth-channels DEAUTH_CHANNELS [DEAUTH_CHANNELS ...]
                        Channels to deauth. Example: --deauth-channels 1,3,7
  -e, --essid ESSID     Enter the ESSID of the rogue Access Point. This option
                        will skip Access Point selection phase. Example:
                        --essid 'Free WiFi'
  -dE, --deauth-essid DEAUTH_ESSID
                        Deauth all the BSSIDs in the WLAN with that ESSID.
  -p, --phishingscenario PHISHINGSCENARIO
                        Choose the phishing scenario to run.This option will
                        skip the scenario selection phase. Example: -p
                        firmware_upgrade
  -pK, --presharedkey PRESHAREDKEY
                        Add WPA/WPA2 protection on the rogue Access Point.
                        Example: -pK s3cr3tp4ssw0rd
  -hC, --handshake-capture HANDSHAKE_CAPTURE
                        Capture of the WPA/WPA2 handshakes for verifying
                        passphrase. Requires cowpatty. Example : -hC
                        capture.pcap
  -qS, --quitonsuccess  Stop the script after successfully retrieving one pair
                        of credentials
  -lC, --lure10-capture
                        Capture the BSSIDs of the APs that are discovered
                        during AP selection phase. This option is part of
                        Lure10 attack.
  -lE, --lure10-exploit LURE10_EXPLOIT
                        Fool the Windows Location Service of nearby Windows
                        users to believe it is within an area that was
                        previously captured with --lure10-capture. Part of the
                        Lure10 attack.
  --logging             Log activity to file
  -dK, --disable-karma  Disables KARMA attack
  -lP, --logpath LOGPATH
                        Determine the full path of the logfile.
  -cP, --credential-log-path CREDENTIAL_LOG_PATH
                        Determine the full path of the file that will store
                        any captured credentials
  --payload-path PAYLOAD_PATH
                        Payload path for scenarios serving a payload
  -cM, --channel-monitor
                        Monitor if target access point changes the channel.
  -wP, --wps-pbc        Monitor if the button on a WPS-PBC Registrar is
                        pressed.
  -wAI, --wpspbc-assoc-interface WPSPBC_ASSOC_INTERFACE
                        The WLAN interface used for associating to the WPS
                        AccessPoint.
  -kB, --known-beacons  Broadcast a number of beacon frames advertising
                        popular WLANs
  -fH, --force-hostapd  Force the usage of hostapd installed in the system
  -pPD, --phishing-pages-directory PHISHING_PAGES_DIRECTORY
                        Search for phishing pages in this location
  --dnsmasq-conf DNSMASQ_CONF
                        Determine the full path of a custom dnmasq.conf file
  -pE, --phishing-essid PHISHING_ESSID
                        Determine the ESSID you want to use for the phishing
                        page
Updated on: 2026-Jun-17
 Edit this page
vwifi-dkms
wireshark
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install wifiphisher`，再执行 `wifiphisher --version` 2>/dev/null || `wifiphisher -V`
- [ ] **2.** **读官方帮助** —— `wifiphisher -h`，需要细节时 `man wifiphisher`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `wifiphisher -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wifiphisher/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wifiphisher/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wifiphisher/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
