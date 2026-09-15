# iaxflood

> VoIP flooder tool A UDP Inter-Asterisk_eXchange (i.e. IAX) packet was captured from an IAX channel between two Asterisk IP PBX’s. The content of that packet is the source of the payload for the attack embodied by this tool. While the IAX p…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`iaxflood` ｜ **官方文档**：<https://www.kali.org/tools/iaxflood/>

## 1. 安装

```bash
sudo apt update
sudo apt install iaxflood
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.1 |
| 架构 | any |
| 可执行命令 | `iaxflood` |
| 依赖 | `libc6` |
| 安装体积 | 25 KB |
| 官网 | <http://www.hackingexposedvoip.com/sec_tools.html> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/iaxflood> |
| 包追踪 | <https://pkg.kali.org/pkg/iaxflood> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Flood the VoIP server from the source (192.168.1.202) to the destination (192.168.1.1) by sending 500 packets (500):
root@kali:~# iaxflood 192.168.1.202 192.168.1.1 500
Will flood port 4569 from port 4569 500 times
We have IP_HDRINCL
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `iaxflood`

官方给出的调用示例：`iaxflood 192.168.1.202 192.168.1.1 500`

```text
root@kali:~# iaxflood 192.168.1.202 192.168.1.1 500
Will flood port 4569 from port 4569 500 times
We have IP_HDRINCL
```

### `iaxflood（示例）`

官方给出的调用示例：`iaxflood -h`

```text
root@kali:~# iaxflood -h
usage: iaxflood sourcename destinationname numpackets
Updated on: 2026-Mar-02
 Edit this page
hb-honeypot
imhex
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install iaxflood`，再执行 `iaxflood --version` 2>/dev/null || `iaxflood -V`
- [ ] **2.** **读官方帮助** —— `iaxflood -h`，需要细节时 `man iaxflood`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `iaxflood -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/iaxflood/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/impact.md`](../../tools/by-attack/impact.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/iaxflood/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/iaxflood/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
