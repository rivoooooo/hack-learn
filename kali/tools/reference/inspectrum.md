# inspectrum

> Tool for visualising captured radio signals inspectrum is a tool for analysing captured signals, primarily from software-defined radio receivers. inspectrum supports the following file types: *.sigmf-meta, *.sigmf-data - Signal Metadata Fo…

> **功能分类**：无线攻击 ｜ **Kali 包**：`inspectrum` ｜ **官方文档**：<https://www.kali.org/tools/inspectrum/>

## 1. 安装

```bash
sudo apt update
sudo apt install inspectrum
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.4.0 |
| 架构 | any |
| 可执行命令 | `inspectrum` |
| 依赖 | `libc6`、`libfftw3-single3`、`libgcc-s1`、`libliquid1`、`libqt5core5t64` |
| 安装体积 | 276 KB |
| 官网 | <https://github.com/miek/inspectrum> |
| 源码仓库 | <https://salsa.debian.org/debian-hamradio-team/inspectrum> |
| 包追踪 | <https://pkg.kali.org/pkg/inspectrum> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
inspectrum -h          # 查看用法
man inspectrum         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man inspectrum`

```text
root@kali:~# man inspectrum
INSPECTRUM(1)                    User Commands                    INSPECTRUM(1)
NAME
     inspectrum - tool for visualising captured radio signals
DESCRIPTION
     inspectrum  is a tool for analysing captured signals, primarily from soft-
     ware-defined radio receivers.
OPTIONS
     -r rate
     Sample rate in Hz.
      file
     Currently inspectrum can only read files with interleaved (complex) 32-bit
     floats, such as those produced by GNURadio or osmocom_fft.
FEATURES
     Spectrogram with zoom/pan
     Large (multi-gigabyte) file support
CONTACT
     #inspectrum on freenode IRC
SEE ALSO
     osmocom-fft(1)
INSPECTRUM                          Oct 2015                      INSPECTRUM(1)
Updated on: 2026-Aug-25
 Edit this page
inetsim
intrace
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install inspectrum`，再执行 `inspectrum --version` 2>/dev/null || `inspectrum -V`
- [ ] **2.** **读官方帮助** —— `inspectrum -h`，需要细节时 `man inspectrum`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `inspectrum -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/inspectrum/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/inspectrum/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/inspectrum/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
