# hak5-wifi-coconut

> Userspace driver for the Hak5 Wi-Fi Coconut Userspace drive for USB Wi-Fi NICs and the Hak5 Wi-Fi Coconut

> **功能分类**：通用工具 ｜ **Kali 包**：`hak5-wifi-coconut` ｜ **官方文档**：<https://www.kali.org/tools/hak5-wifi-coconut/>

## 1. 安装

```bash
sudo apt update
sudo apt install hak5-wifi-coconut
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1.0 |
| 架构 | any |
| 可执行命令 | `hak5-wifi-coconut`、`wifi_coconut` |
| 依赖 | `firmware-mediatek`、`libc6`、`libusb-1.0-0`、`wifi_coconut` |
| 安装体积 | 176 KB |
| 官网 | <https://hak5.org> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/hak5-wifi-coconut> |
| 包追踪 | <https://pkg.kali.org/pkg/hak5-wifi-coconut> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
hak5-wifi-coconut -h          # 查看用法
man hak5-wifi-coconut         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wifi_coconut`

> 官方示例调用：`wifi_coconut -h`

```text
root@kali:~# wifi_coconut -h
Wi-Fi Coconut
Usage: wifi_coconut [options]
By default, the wifi_coconut tool opens in interactive mode.
Universal options:
 --disable-leds        Go fully dark; don't enable any LEDs
 --invert-leds         Normally a Wi-Fi Coconut enables all the LEDs
                       and blinks during traffic; Invert only lights
                       when there is traffic.
 --disable-blinking    Disable blinking the LEDs on traffic
Non-interactive modes:
 --no-display          Don't display channel UI while logging
 --wait                Wait for a coconut to be found
 --pcap=[fname]        Log packets to a pcap file.  If file is '-',
                       a pcap file will be echoed to stdout so that it can
                       be piped to other tools. --wait-for-coconut    Wait for a coconut to be connected and identified
 --list-coconuts       List Wi-Fi Coconut devices and exit
 --coconut-device=X    If you have multiple Wi-Fi Coconuts, specify
                       which one to use
 --enable-partial      Enable a Wi-Fi Coconut even if not all the
                       radios have been identified.
 --plain-dot11         Log plain 802.11 packets instead of radiotap
                       formatted packets with signal and channel
 --quiet               Disable most output
Updated on: 2025-Dec-09
 Edit this page
h8mail
hakrawler
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install hak5-wifi-coconut`，再执行 `hak5-wifi-coconut --version` 2>/dev/null || `hak5-wifi-coconut -V`
- [ ] **2.** **读官方帮助** —— `hak5-wifi-coconut -h`，需要细节时 `man hak5-wifi-coconut`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: wifi_coconut [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hak5-wifi-coconut/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hak5-wifi-coconut/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hak5-wifi-coconut/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
