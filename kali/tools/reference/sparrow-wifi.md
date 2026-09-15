# sparrow-wifi

> Graphical Wi-Fi Analyzer for Linux This package contains a graphical Wi-Fi analyzer for Linux. It provides a more comprehensive GUI-based replacement for tools like inSSIDer and linssid that runs specifically on Linux. In its most comprehe…

> **功能分类**：通用工具 ｜ **Kali 包**：`sparrow-wifi` ｜ **官方文档**：<https://www.kali.org/tools/sparrow-wifi/>

## 1. 安装

```bash
sudo apt update
sudo apt install sparrow-wifi
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.0 |
| 架构 | all |
| 可执行命令 | `sparrow-wifi`、`sparrowwifiagent` |
| 依赖 | `gpsd`、`gpsd-clients`、`python3`、`python3-dateutil`、`python3-dronekit`、`python3-gps3`、`python3-manuf`、`python3-matplotlib`、`python3-numpy`、`python3-pyqt5.qsci`、`python3-pyqt5.qtchart`、`python3-requests` 等 |
| 安装体积 | 1.94 MB |
| 官网 | <https://github.com/ghostop14/sparrow-wifi> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sparrow-wifi> |
| 包追踪 | <https://pkg.kali.org/pkg/sparrow-wifi> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sparrow-wifi -h          # 查看用法
man sparrow-wifi         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sparrowwifiagent`

官方给出的调用示例：`sparrowwifiagent -h`

```text
root@kali:~# sparrowwifiagent -h
usage: sparrowwifiagent.py [-h] [--port PORT] [--allowedips ALLOWEDIPS]
                           [--staticcoord STATICCOORD]
                           [--mavlinkgps MAVLINKGPS] [--sendannounce]
                           [--userpileds] [--recordinterface RECORDINTERFACE]
                           [--ignorecfg] [--cfgfile CFGFILE] [--allowcors]
                           [--delaystart DELAYSTART] [--debughttp]
Sparrow-wifi agent
options:
  -h, --help            show this help message and exit
  --port PORT           Port for HTTP server to listen on. Default is 8020.
  --allowedips ALLOWEDIPS
                        IP addresses allowed to connect to this agent. Default
                        is any. This can be a comma-separated list for
                        multiple IP addresses
  --staticcoord STATICCOORD
                        Use user-defined lat,long,altitude(m) rather than GPS.
                        Ex: 40.1,-75.3,150
  --mavlinkgps MAVLINKGPS
                        Use Mavlink (drone) for GPS. Options are: '3dr' for a
                        Solo, 'sitl' for local simulator, or full connection
                        string ('udp/tcp:<ip>:<port>' such as:
                        'udp:10.1.1.10:14550')
  --sendannounce        Send a UDP broadcast packet on the specified port to
                        announce presence
  --userpileds          Use RPi LEDs to signal state. Red=GPS
                        [off=None,blinking=Unsynchronized,solid=synchronized],
                        Green=Agent Running [On=Running, blinking=servicing
                        HTTP request]
  --recordinterface RECORDINTERFACE
                        Automatically start recording locally with the given
                        wireless interface (headless mode) in a recordings
                        directory
  --ignorecfg           Don't load any config files (useful for overriding
                        and/or testing)
  --cfgfile CFGFILE     Use the specified config file rather than the default
                        sparrowwifiagent.cfg file
  --allowcors           Allow Cross Domain Resource Sharing
  --delaystart DELAYSTART
                        Wait <delaystart> seconds before initializing
  --debughttp           Print each URL request
Updated on: 2026-May-25
 Edit this page
snowdrop
spiderfoot
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sparrow-wifi`，再执行 `sparrow-wifi --version` 2>/dev/null || `sparrow-wifi -V`
- [ ] **2.** **读官方帮助** —— `sparrow-wifi -h`，需要细节时 `man sparrow-wifi`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sparrow-wifi -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sparrow-wifi/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sparrow-wifi/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sparrow-wifi/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
