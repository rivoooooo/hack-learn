# intrace

> Traceroute-like application piggybacking on existing TCP connections InTrace is a traceroute-like application that enables users to enumerate IP hops exploiting existing TCP connections, both initiated from local network (local system) or …

> **功能分类**：信息搜集 ｜ **Kali 包**：`intrace` ｜ **官方文档**：<https://www.kali.org/tools/intrace/>

## 1. 安装

```bash
sudo apt update
sudo apt install intrace
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6 |
| 架构 | any |
| 可执行命令 | `intrace` |
| 依赖 | `libc6` |
| 安装体积 | 52 KB |
| 官网 | <https://github.com/robertswiecki/intrace> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/intrace> |
| 包追踪 | <https://pkg.kali.org/pkg/intrace> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Run a trace to the target host (-h www.example.com) using port 80 (-p 80) with a packet size of 4 bytes (-s 4):
root@kali:~# intrace -h www.example.com -p 80 -s 4
InTrace 1.5 -- R: 93.184.216.119/80 (80) L: 192.168.1.130/51654
Payload Size: 4 bytes, Seq: 0x0d6dbb02, Ack: 0x8605bff0
Status: Packets sent #8

  #  [src addr]         [icmp src addr]    [pkt type]
 1.  [192.168.1.1    ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 2.  [192.168.0.1    ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 3.  [  ---          ]  [  ---          ]  [NO REPLY]
 4.  [64.59.184.185  ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 5.  [66.163.70.25   ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 6.  [66.163.64.150  ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 7.  [66.163.75.117  ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 8.  [206.223.119.59 ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `intrace`

官方给出的调用示例：`intrace -h www.example.com -p 80 -s 4`

```text
root@kali:~# intrace -h www.example.com -p 80 -s 4
InTrace 1.5 -- R: 93.184.216.119/80 (80) L: 192.168.1.130/51654
Payload Size: 4 bytes, Seq: 0x0d6dbb02, Ack: 0x8605bff0
Status: Packets sent #8
  #  [src addr]         [icmp src addr]    [pkt type]
 1.  [192.168.1.1    ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 2.  [192.168.0.1    ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 3.  [  ---          ]  [  ---          ]  [NO REPLY]
 4.  [64.59.184.185  ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 5.  [66.163.70.25   ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 6.  [66.163.64.150  ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 7.  [66.163.75.117  ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 8.  [206.223.119.59 ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
```

### `intrace（示例）`

官方给出的调用示例：`intrace -h`

```text
root@kali:~# intrace -h
InTrace, version 1.6 (C)2007-2016 Robert Swiecki <
[email protected]
>
2026/09/14 06:06:09.550367 <INFO> Usage: intrace <-h hostname> [-p <port>] [-d <debuglevel>] [-s <payloadsize>] [-4] [-6]
Updated on: 2026-Aug-25
 Edit this page
inspectrum
isr-evilgrade
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install intrace`，再执行 `intrace --version` 2>/dev/null || `intrace -V`
- [ ] **2.** **读官方帮助** —— `intrace -h`，需要细节时 `man intrace`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `intrace -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/intrace/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/intrace/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/intrace/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
