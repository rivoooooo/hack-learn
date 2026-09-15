# gqrx-sdr

> Software defined radio receiver Gqrx works with hardware supported by gr-osmosdr, including Funcube Dongle, RTL-SDR, Airspy, HackRF, BladeRF, RFSpace, USRP and SoapySDR. Gqrx can operate as an AM/FM/SSB receiver with audio output or as an …

> **功能分类**：无线攻击 ｜ **Kali 包**：`gqrx-sdr` ｜ **官方文档**：<https://www.kali.org/tools/gqrx-sdr/>

## 1. 安装

```bash
sudo apt update
sudo apt install gqrx-sdr
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.17.7 |
| 架构 | any |
| 可执行命令 | `gqrx-sdr`、`gqrx` |
| 依赖 | `libc6`、`libgcc-s1`、`libgnuradio-analog3.10.12`、`libgnuradio-blocks3.10.12`、`libgnuradio-digital3.10.12`、`libgnuradio-fft3.10.12`、`libgnuradio-filter3.10.12`、`libgnuradio-network3.10.12`、`libgnuradio-osmosdr0.2.0t64`、`libgnuradio-pmt3.10.12`、`libgnuradio-runtime3.10.12`、`libpulse0` 等 |
| 安装体积 | 2.08 MB |
| 官网 | <https://gqrx.dk/> |
| 源码仓库 | <https://salsa.debian.org/bottoms/pkg-gqrx-sdr> |
| 包追踪 | <https://pkg.kali.org/pkg/gqrx-sdr> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gqrx-sdr -h          # 查看用法
man gqrx-sdr         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man gqrx`

```text
root@kali:~# man gqrx
GQRX(1)                          User Commands                          GQRX(1)
NAME
     gqrx - Software Defined Radio GUI application
DESCRIPTION
     Gqrx  is a software defined radio (SDR) receiver implemented using GNU Ra-
     dio and the Qt GUI toolkit. It works with  hardware  supported  by  gr-os-
     mosdr,  including  Funcube  Dongle,  RTL-SDR, Airspy, HackRF, BladeRF, RF-
     Space, USRP and SoapySDR.
     Gqrx can operate as an AM/FM/SSB receiver with audio output or as an  FFT-
     only  instrument. There are also various hooks for interacting with exter-
     nal applications using network sockets.
     It is strongly recommended to run the volk_profile utility before  running
     gqrx.  This  will  detect  and enable processor-specific optimisations and
     will in many cases give a significant performance boost.
     The first time you start gqrx it will open a device configuration  dialog.
     Supported  devices that are connected to the computer are discovered auto-
     matically and you can select any of them in the drop-down list.
     If you don't see your device listed in the drop-down list it could be  be-
     cause:
     *      The driver has not been included in a binary distribution
     *      The udev rule has not been properly configured
     *      Linux kernel driver is blocking access to the device
     You  can  test  your device using device specific tools, such as rtl_test,
     airspy_rx, hackrf_transfer, qthid, etc.
     Gqrx supports multiple configurations and sessions if you have several de-
     vices or if you want to use the same  device  under  different  configura-
     tions.  You  can load a configuration from the GUI or using the -c command
     line argument.
OPTIONS
     -h, --help
            Display the help page
     -s, --style style
            Use the given style (fusion, windows)
     -l, --list
            List existing configurations
     -c, --conf file
            Start with a specific configuration file
     -e, --edit
            Edit the configuration file before using it
     -r, --reset
            Reset the configuration file
SEE ALSO
     https://gqrx.dk/
gqrx 2.17.7                       May 27, 2025                          GQRX(1)
Updated on: 2026-May-25
 Edit this page
gparted
gr-osmosdr
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install gqrx-sdr`，再执行 `gqrx-sdr --version` 2>/dev/null || `gqrx-sdr -V`
- [ ] **2.** **读官方帮助** —— `gqrx-sdr -h`，需要细节时 `man gqrx-sdr`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `gqrx-sdr -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gqrx-sdr/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gqrx-sdr/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gqrx-sdr/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
