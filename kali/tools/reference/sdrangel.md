# sdrangel

> Qt-based SDR front-end for various devices SDR front-end supporting many hardware and software receivers/transmitter, including: RTL-SDR, BladeRF, HackRF and others. It uses Qt framework and OpenGL for graphical rendering, works on many op…

> **功能分类**：通用工具 ｜ **Kali 包**：`sdrangel` ｜ **官方文档**：<https://www.kali.org/tools/sdrangel/>

## 1. 安装

```bash
sudo apt update
sudo apt install sdrangel
```

| 项目 | 内容 |
|------|------|
| 版本 | 7.27.2 |
| 架构 | any |
| 可执行命令 | `sdrangel`、`sdrangelbench`、`sdrangelsrv` |
| 依赖 | `libairspy0`、`libairspyhf1`、`libavcodec62`、`libavformat62`、`libavutil60`、`libbladerf2`、`libc6`、`libcodec2-1.2`、`libfftw3-single3`、`libflac14`、`libgcc-s1`、`libhackrf0` 等 |
| 安装体积 | 109.88 MB |
| 官网 | <https://www.sdrangel.org/> |
| 源码仓库 | <https://salsa.debian.org/debian-hamradio-team/sdrangel> |
| 包追踪 | <https://pkg.kali.org/pkg/sdrangel> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sdrangel -h          # 查看用法
man sdrangel         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

官方给出的调用示例：`man sdrangel`

```text
root@kali:~# man sdrangel
SDRANGEL(1)                         SDRANGEL                        SDRANGEL(1)
NAME
     SDRangel - SDR and signal analyzer frontend (GUI)
SYNOPSIS
     sdrangel [options]
DESCRIPTION
     Software Defined Radio application
OPTIONS
     -h, --help
            Displays help on commandline options.
     --help-all
            Displays help, including generic Qt options.
     -v, --version
            Displays version information.
     -a, --api-address <address>
            Web API server address.
     -p, --api-port <port>
            Web API server port.
     -w, --fftwf-wisdom <file>
            FFTW Wisdom file.
     --scratch
            Start from scratch (no current config).
     --soapy
            Activate Soapy SDR support.
     --remote-tcp
            Start Remote TCP Sink
     --remote-tcp-address <address>
            Remote TCP Sink interface IP address (Default any).
     --remote-tcp-port <port>
            Remote TCP Sink port (Default 1234).
     --remote-tcp-hwtype <hwtype>
            Remote  TCP  Sink  device hardware type (Optional. E.g. RTLSDR/SDR-
            playV3/AirspyHF).
     --remote-tcp-serial <serial>
            Remote TCP Sink device serial (Optional).
     --list-devices
            List available physical devices.
     --start
            Start all devices and features.
SDRangel                                                            SDRANGEL(1)
```

### `sdrangelbench`

官方给出的调用示例：`sdrangelbench -h`

```text
root@kali:~# sdrangelbench -h
Usage: sdrangelbench [options]
Software Defined Radio application benchmarks
Options:
  -h, --help                  Displays help on commandline options.
  --help-all                  Displays help, including generic Qt options.
  -v, --version               Displays version information.
  -t, --test <test>           Test type: decimateii, decimatefi, decimateff,
                              decimateif, decimateinfii, decimatesupii, ambe,
                              golay2312, ft8, ft4, ft8protocols, callsign,
                              fftrrcfilter, firrrcfilter, meshtastic.
  -n, --nb-samples <samples>  Number of sample to deal with.
  -r, --repeat <repetition>   Number of repetitions.
  -l, --log2-factor <log2>    Log2 factor for rate conversion.
  -f, --file <file>           File to be used for the test.
  -a, --args <args>           Custom arguments string to be used for the test.
```

### `sdrangelsrv`

官方给出的调用示例：`sdrangelsrv -h`

```text
root@kali:~# sdrangelsrv -h
Usage: sdrangelsrv [options]
Software Defined Radio application
Options:
  -h, --help                      Displays help on commandline options.
  --help-all                      Displays help, including generic Qt options.
  -v, --version                   Displays version information.
  -a, --api-address <address>     Web API server address.
  -p, --api-port <port>           Web API server port.
  -w, --fftwf-wisdom <file>       FFTW Wisdom file.
  --scratch                       Start from scratch (no current config).
  --soapy                         Activate Soapy SDR support.
  --remote-tcp                    Start Remote TCP Sink
  --remote-tcp-address <address>  Remote TCP Sink interface IP address (Default
                                  any).
  --remote-tcp-port <port>        Remote TCP Sink port (Default 1234).
  --remote-tcp-hwtype <hwtype>    Remote TCP Sink device hardware type
                                  (Optional. E.g. RTLSDR/SDRplayV3/AirspyHF).
  --remote-tcp-serial <serial>    Remote TCP Sink device serial (Optional).
  --list-devices                  List available physical devices.
  --start                         Start all devices and features
Updated on: 2026-Aug-25
 Edit this page
screen
set
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sdrangel`，再执行 `sdrangel --version` 2>/dev/null || `sdrangel -V`
- [ ] **2.** **读官方帮助** —— `sdrangel -h`，需要细节时 `man sdrangel`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sdrangelbench [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sdrangel/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sdrangel/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sdrangel/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
