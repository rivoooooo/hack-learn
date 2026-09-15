# wig-ng

> Utility for Wi-Fi device fingerprinting This package contains WIG (Wi-Fi Information Gathering), a utility for Wi-Fi device fingerprinting. Supported protocols and standards: Apple Wireless Direct Link (AWDL) Cisco Client Extension (CCX)

> **功能分类**：通用工具 ｜ **Kali 包**：`wig-ng` ｜ **官方文档**：<https://www.kali.org/tools/wig-ng/>

## 1. 安装

```bash
sudo apt update
sudo apt install wig-ng
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.1 |
| 架构 | all |
| 可执行命令 | `wig-ng`、`wig-ng.py` |
| 依赖 | `python3`、`python3-impacket`、`python3-pcapy`、`python3-setproctitle` |
| 安装体积 | 334 KB |
| 官网 | <https://github.com/6e726d/wig-ng> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/wig-ng> |
| 包追踪 | <https://pkg.kali.org/pkg/wig-ng> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
wig-ng -h          # 查看用法
man wig-ng         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wig-ng`

官方给出的调用示例：`wig-ng -h`

```text
root@kali:~# wig-ng -h
usage: wig-ng.py [-h] [-v] [-c count] [-a] (-i network interface |
                 -r pcap file | -R pcap directory)
options:
  -h, --help            show this help message and exit
  -v, --verbose         Output verbosity (incremental).
  -c, --concurrent count
                        Number of PCAP capture files to process
                        simultaneously.
  -a, --active          Some modules can perform frame injection, this is
                        define by setting the active mode.
  -i, --interface network interface
                        IEEE 802.11 network interface on monitor mode.
  -r pcap file          PCAP capture file with IEEE 802.11 network traffic.
  -R pcap directory     Directory with PCAP capture files.
```

### `wig-ng.py`

官方给出的调用示例：`wig-ng.py -h`

```text
root@kali:~# wig-ng.py -h
usage: wig-ng.py [-h] [-v] [-c count] [-a] (-i network interface |
                 -r pcap file | -R pcap directory)
options:
  -h, --help            show this help message and exit
  -v, --verbose         Output verbosity (incremental).
  -c, --concurrent count
                        Number of PCAP capture files to process
                        simultaneously.
  -a, --active          Some modules can perform frame injection, this is
                        define by setting the active mode.
  -i, --interface network interface
                        IEEE 802.11 network interface on monitor mode.
  -r pcap file          PCAP capture file with IEEE 802.11 network traffic.
  -R pcap directory     Directory with PCAP capture files.
Updated on: 2025-Dec-09
 Edit this page
wifipumpkin3
windows-privesc-check
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install wig-ng`，再执行 `wig-ng --version` 2>/dev/null || `wig-ng -V`
- [ ] **2.** **读官方帮助** —— `wig-ng -h`，需要细节时 `man wig-ng`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `wig-ng -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wig-ng/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wig-ng/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wig-ng/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
