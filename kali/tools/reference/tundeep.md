# tundeep

> Layer 2 VPN/injection tool The tool resides [almost] entirely in user space on the victim aside from the pcap requirement.

> **功能分类**：通用工具 ｜ **Kali 包**：`tundeep` ｜ **官方文档**：<https://www.kali.org/tools/tundeep/>

## 1. 安装

```bash
sudo apt update
sudo apt install tundeep
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1~git20190802 |
| 架构 | any |
| 可执行命令 | `tundeep` |
| 依赖 | `libc6`、`libpcap0.8t64`、`zlib1g` |
| 安装体积 | 49 KB |
| 官网 | <https://www.adampalmer.me/iodigitalsec/tundeep/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/tundeep> |
| 包追踪 | <https://pkg.kali.org/pkg/tundeep> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
tundeep -h          # 查看用法
man tundeep         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tundeep`

> 官方示例调用：`tundeep -h`

```text
root@kali:~# tundeep -h
tundeep: option requires an argument -- 'h'
Option -h error.
*** tundeep v1.0_20170728 by Adam Palmer <
[email protected]
> ***
Usage: tundeep <-i iface|[-t|-T] tapiface> <-h ip> <-p port> [-6] [-C] <-c|-s> [-x tapip] [-y tapmask] [-u tapmac] [-b bpf] [-d udp mode] [-e udp remote] [-K]
-6 IPv6 mode
-C compress mode
-K disable checksum
-a print all pcap devs
-b "bpf"
-i interface to bind to
-h IP to bind to/connect to
-p port to bind to/connect to
-c client mode
-s server mode
-d udp mode
-e udp peer
-t tap interface
-T ipv6 tap interface
-u tap mac
-x if -t mode, set iface ip, if -T mode, set iface ipv6 ip
-y if -t mode, set iface mask, if -T mode, set iface ipv6 prefixlen
--------------------
Updated on: 2025-Dec-09
 Edit this page
trivy
uhd-images
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install tundeep`，再执行 `tundeep --version` 2>/dev/null || `tundeep -V`
- [ ] **2.** **读官方帮助** —— `tundeep -h`，需要细节时 `man tundeep`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: tundeep <-i iface|[-t|-T] tapiface> <-h ip> <-p port> [-6] [-C] <-c|-s> [-x tapip] [-y tapmask] [-u tapmac] [-b bpf] [-d udp mode] [-e udp remote] [-K]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/tundeep/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/tundeep/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/tundeep/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
