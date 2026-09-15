# kalibrate-rtl

> Calculate local oscillator frequency offset using GSM base stations Kalibrate, or kal, can scan for GSM base stations in a given frequency band and can use those GSM base stations to calculate the local oscillator frequency offset.

> **功能分类**：无线攻击 ｜ **Kali 包**：`kalibrate-rtl` ｜ **官方文档**：<https://www.kali.org/tools/kalibrate-rtl/>

## 1. 安装

```bash
sudo apt update
sudo apt install kalibrate-rtl
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.4.1 |
| 架构 | any |
| 可执行命令 | `kalibrate-rtl`、`kal` |
| 依赖 | `libc6`、`libfftw3-double3`、`libgcc-s1`、`librtlsdr0`、`libstdc++6`、`rtl-sdr`、`kal` |
| 安装体积 | 62 KB |
| 官网 | <https://github.com/steve-m/kalibrate-rtl> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/kalibrate-rtl> |
| 包追踪 | <https://pkg.kali.org/pkg/kalibrate-rtl> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan for GSM base stations in the GSM-850 band (-s GSM850), then use channel 128 (-c 128) to get the frequency offset:
root@kali:~# kal -s GSM850
Found 1 device(s):
  0:  ezcap USB 2.0 DVB-T/DAB/FM dongle

Using device 0: ezcap USB 2.0 DVB-T/DAB/FM dongle
Found Rafael Micro R820T tuner
Exact sample rate is: 270833.002142 Hz
kal: Scanning for GSM-850 base stations.
GSM-850:
    chan: 128 (869.2MHz - 3.988kHz) power: 486634.32
    chan: 143 (872.2MHz - 3.760kHz) power: 56331.63

root@kali:~# kal -c 128
Found 1 device(s):
  0:  ezcap USB 2.0 DVB-T/DAB/FM dongle

Using device 0: ezcap USB 2.0 DVB-T/DAB/FM dongle
Found Rafael Micro R820T tuner
Exact sample rate is: 270833.002142 Hz
kal: Calculating clock frequency offset.
Using GSM-850 channel 128 (869.2MHz)
average     [min, max]  (range, stddev)
- 4.093kHz      [-4102, -4083]  (20, 5.314593)
overruns: 0
not found: 0
average absolute error: 4.709 ppm
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `kal`

> 官方示例调用：`kal -s GSM850`

```text
root@kali:~# kal -s GSM850
Found 1 device(s):
  0:  ezcap USB 2.0 DVB-T/DAB/FM dongle
Using device 0: ezcap USB 2.0 DVB-T/DAB/FM dongle
Found Rafael Micro R820T tuner
Exact sample rate is: 270833.002142 Hz
kal: Scanning for GSM-850 base stations.
GSM-850:
    chan: 128 (869.2MHz - 3.988kHz) power: 486634.32
    chan: 143 (872.2MHz - 3.760kHz) power: 56331.63
```

### `kal -c 128`

> 官方示例调用：`kal -c 128`

```text
root@kali:~# kal -c 128
Found 1 device(s):
  0:  ezcap USB 2.0 DVB-T/DAB/FM dongle
Using device 0: ezcap USB 2.0 DVB-T/DAB/FM dongle
Found Rafael Micro R820T tuner
Exact sample rate is: 270833.002142 Hz
kal: Calculating clock frequency offset.
Using GSM-850 channel 128 (869.2MHz)
average     [min, max]  (range, stddev)
- 4.093kHz      [-4102, -4083]  (20, 5.314593)
overruns: 0
not found: 0
average absolute error: 4.709 ppm
```

### `kal -h`

> 官方示例调用：`kal -h`

```text
root@kali:~# kal -h
kalibrate v0.4.1-rtl, Copyright (c) 2010, Joshua Lackey
modified for use with rtl-sdr devices, Copyright (c) 2012, Steve Markgraf
Usage:
	GSM Base Station Scan:
		kal <-s band indicator> [options]
	Clock Offset Calculation:
		kal <-f frequency | -c channel> [options]
Where options are:
	-s	band to scan (GSM850, GSM-R, GSM900, EGSM, DCS, PCS)
	-f	frequency of nearby GSM base station
	-c	channel of nearby GSM base station
	-b	band indicator (GSM850, GSM-R, GSM900, EGSM, DCS, PCS)
	-g	gain in dB
	-d	rtl-sdr device index
	-e	initial frequency error in ppm
	-E	manual frequency offset in hz
	-v	verbose
	-D	enable debug messages
	-h	help
Updated on: 2025-Dec-09
 Edit this page
kali-community-wallpapers
kismet
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install kalibrate-rtl`，再执行 `kalibrate-rtl --version` 2>/dev/null || `kalibrate-rtl -V`
- [ ] **2.** **读官方帮助** —— `kalibrate-rtl -h`，需要细节时 `man kalibrate-rtl`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/kalibrate-rtl/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/kalibrate-rtl/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/kalibrate-rtl/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
