# above

> Network security sniffer for finding vulnerabilities in the network This package contains a network security sniffer for finding vulnerabilities in the network, designed for pentesters and security professionals. It is based entirely on ne…

> **功能分类**：嗅探与欺骗 ｜ **Kali 包**：`above` ｜ **官方文档**：<https://www.kali.org/tools/above/>

## 1. 安装

```bash
sudo apt update
sudo apt install above
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.8.1 |
| 架构 | all |
| 可执行命令 | `above` |
| 依赖 | `python3`、`python3-colorama`、`python3-scapy` |
| 安装体积 | 1.42 MB |
| 官网 | <https://github.com/caster0x00/Above> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/above> |
| 包追踪 | <https://pkg.kali.org/pkg/above> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
above -h          # 查看用法
man above         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `above`

> 官方示例调用：`above -h`

```text
root@kali:~# above -h
        ___    __
       /   |  / /_  ____ _   _____
      / /| | / __ \/ __ \ | / / _ \
     / ___ |/ /_/ / /_/ / |/ /  __/
    /_/  |_/_.___/\____/|___/\___/
    Above: Network Security Sniffer
    Developer: Mahama Bazarov (Caster)
    Contact:
[email protected]
    Version: 2.8.1
    Codename: Rubens Barrichello
    Documentation & Usage: https://github.com/caster0x00/Above
usage: above [-h] [--interface INTERFACE] [--timer TIMER] [--output OUTPUT]
             [--input INPUT] [--passive-arp] [--search-vlan]
options:
  -h, --help            show this help message and exit
  --interface INTERFACE
                        Interface for traffic listening
  --timer TIMER         Time in seconds to capture packets, default: not set
  --output OUTPUT       File name where the traffic will be recorded, default:
                        not set
  --input INPUT         File name of the traffic dump
  --passive-arp         Passive ARP (Host Discovery)
  --search-vlan         VLAN Search
Updated on: 2026-May-25
 Edit this page
0trace
adaptixc2
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install above`，再执行 `above --version` 2>/dev/null || `above -V`
- [ ] **2.** **读官方帮助** —— `above -h`，需要细节时 `man above`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `above -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/above/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/above/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/above/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
