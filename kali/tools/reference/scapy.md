# scapy

> Interactive packet manipulation tool root@kali:~# scapy -h Usage: scapy.py [-c new_startup_file] [-p new_prestart_file] [-C] [-P] [-H] Args: -H: header-less start -C: do not read startup file

> **功能分类**：信息搜集 ｜ **Kali 包**：`scapy` ｜ **官方文档**：<https://www.kali.org/tools/scapy/>

## 1. 安装

```bash
sudo apt update
sudo apt install scapy
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.7.0 |
| 架构 | all |
| 可执行命令 | `python3-scapy`、`scapy`、`scapy3` |
| 官网 | <https://scapy.net/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/scapy> |
| 包追踪 | <https://pkg.kali.org/pkg/scapy> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
python3-scapy -h          # 查看用法
man python3-scapy         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `scapy`

官方给出的调用示例：`scapy -h`

```text
root@kali:~# scapy -h
Usage: scapy.py [-c new_startup_file] [-p new_prestart_file] [-C] [-P] [-H]
Args:
	-H: header-less start
	-C: do not read startup file
	-P: do not read pre-startup file
```

### `scapy3`

官方给出的调用示例：`scapy3 -h`

```text
root@kali:~# scapy3 -h
Usage: scapy.py [-c new_startup_file] [-p new_prestart_file] [-C] [-P] [-H]
Args:
	-H: header-less start
	-C: do not read startup file
	-P: do not read pre-startup file
Learn more with
OffSec
Want to learn more about scapy? get access to in-depth training and hands-on labs:
Network Penetration Testing Essentials: 13.7. Network Scripting: Capturing and Sending Packets with Scapy
Scripting for System Administrators Skill Path: 3.7. Network Scripting: Capturing and Sending Packets with Scapy
Scripting and Programming Skill Path: 2.7. Network Scripting: Capturing and Sending Packets with Scapy
Updated on: 2026-Mar-02
 Edit this page
sbd
seclists
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install scapy`，再执行 `python3-scapy --version` 2>/dev/null || `python3-scapy -V`
- [ ] **2.** **读官方帮助** —— `python3-scapy -h`，需要细节时 `man python3-scapy`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: scapy.py [-c new_startup_file] [-p new_prestart_file] [-C] [-P] [-H]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/scapy/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[scapy](../../tools/tutorials/07-嗅探与欺骗/scapy.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/scapy/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/scapy/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
