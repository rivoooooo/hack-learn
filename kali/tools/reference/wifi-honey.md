# wifi-honey

> Wi-Fi honeypot In the case of WPA/WPA2, by running airodump-ng along side this you also end up capturing the first two packets of the four way handshake and so can attempt to crack the key with either aircrack-ng or coWPAtty. What this scr…

> **功能分类**：无线攻击 ｜ **Kali 包**：`wifi-honey` ｜ **官方文档**：<https://www.kali.org/tools/wifi-honey/>

## 1. 安装

```bash
sudo apt update
sudo apt install wifi-honey
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0 |
| 架构 | all |
| 可执行命令 | `wifi-honey` |
| 依赖 | `aircrack-ng`、`screen` |
| 安装体积 | 16 KB |
| 官网 | <https://www.digininja.org/projects/wifi_honey.php> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/wifi-honey> |
| 包追踪 | <https://pkg.kali.org/pkg/wifi-honey> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Broadcast the given ESSID (FreeWiFi) on channel 6 (6) using the wireless interface (wlan0):
root@kali:~# wifi-honey FreeWiFi 6 wlan0
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wifi-honey`

> 官方示例调用：`wifi-honey FreeWiFi 6 wlan0`

```text
root@kali:~# wifi-honey FreeWiFi 6 wlan0
```

### `wifi-honey --help`

> 官方示例调用：`wifi-honey --help`

```text
root@kali:~# wifi-honey --help
Found 1 processes that could cause trouble.
Kill them using 'airmon-ng check kill' before putting
the card in monitor mode, they will interfere by changing channels
and sometimes putting the interface back in managed mode
    PID Name
    587 NetworkManager
Requested device "wlan0" does not exist.
Run /usr/sbin/airmon-ng without any arguments to see available interfaces
Found 1 processes that could cause trouble.
Kill them using 'airmon-ng check kill' before putting
the card in monitor mode, they will interfere by changing channels
and sometimes putting the interface back in managed mode
    PID Name
    587 NetworkManager
Requested device "wlan0" does not exist.
Run /usr/sbin/airmon-ng without any arguments to see available interfaces
Found 1 processes that could cause trouble.
Kill them using 'airmon-ng check kill' before putting
the card in monitor mode, they will interfere by changing channels
and sometimes putting the interface back in managed mode
    PID Name
    587 NetworkManager
Requested device "wlan0" does not exist.
Run /usr/sbin/airmon-ng without any arguments to see available interfaces
Found 1 processes that could cause trouble.
Kill them using 'airmon-ng check kill' before putting
the card in monitor mode, they will interfere by changing channels
and sometimes putting the interface back in managed mode
    PID Name
    587 NetworkManager
Requested device "wlan0" does not exist.
Run /usr/sbin/airmon-ng without any arguments to see available interfaces
Found 1 processes that could cause trouble.
Kill them using 'airmon-ng check kill' before putting
the card in monitor mode, they will interfere by changing channels
and sometimes putting the interface back in managed mode
    PID Name
    587 NetworkManager
Requested device "wlan0" does not exist.
Run /usr/sbin/airmon-ng without any arguments to see available interfaces
Updated on: 2026-Aug-25
 Edit this page
what-is-python
windows-binaries
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install wifi-honey`，再执行 `wifi-honey --version` 2>/dev/null || `wifi-honey -V`
- [ ] **2.** **读官方帮助** —— `wifi-honey -h`，需要细节时 `man wifi-honey`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `wifi-honey -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wifi-honey/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wifi-honey/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wifi-honey/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
