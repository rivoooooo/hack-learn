# ferret-sidejack

> Monitors data and extracts interesting data This tool extracts interesting bits from network traffic. One use is to feed the “hamster” tool. Another use is to dump the output intoa text file, then use indexers and grep programs to analyze …

> **功能分类**：Web 应用 ｜ **Kali 包**：`ferret-sidejack` ｜ **官方文档**：<https://www.kali.org/tools/ferret-sidejack/>

## 1. 安装

```bash
sudo apt update
sudo apt install ferret-sidejack
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.0.1 |
| 架构 | any |
| 可执行命令 | `ferret-sidejack` |
| 依赖 | `libc6`、`libgcc-s1`、`libpcap-dev`、`libstdc++6` |
| 安装体积 | 379 KB |
| 官网 | <https://github.com/robertdavidgraham/ferret> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ferret-sidejack> |
| 包追踪 | <https://pkg.kali.org/pkg/ferret-sidejack> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ferret-sidejack -h          # 查看用法
man ferret-sidejack         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ferret-sidejack`

官方给出的调用示例：`ferret-sidejack -h`

```text
root@kali:~# ferret-sidejack -h
-- FERRET 3.0.1 - 2007-2012 (c) Errata Security
-- build = Sep 29 2024 02:38:07 (64-bits)
-- libpcap version 1.10.6 (64-bit time_t, with TPACKET_V3)
options:
 -i <adapter>    Sniffs the wire(less) attached to that network adapter.
                 Must have libpcap or winpcap installed to work.
 -r <files>      Read files in off-line mode. Can use wildcards, such as
                 using "ferret -r *.pcap". Doesn't need libpcap to work.
 -c <file>       Reads in more advanced parameters from a file.
Updated on: 2026-Jun-17
 Edit this page
exifprobe
finalrecon
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ferret-sidejack`，再执行 `ferret-sidejack --version` 2>/dev/null || `ferret-sidejack -V`
- [ ] **2.** **读官方帮助** —— `ferret-sidejack -h`，需要细节时 `man ferret-sidejack`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `ferret-sidejack -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ferret-sidejack/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/collection.md`](../../tools/by-attack/collection.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ferret-sidejack/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ferret-sidejack/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
