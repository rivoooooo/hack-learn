# blueranger

> Simple Bash script to locate Bluetooth devices BlueRanger is a simple Bash script which uses Link Quality to locate Bluetooth device radios. It sends l2cap (Bluetooth) pings to create a connection between Bluetooth interfaces, since most d…

> **功能分类**：无线攻击 ｜ **Kali 包**：`blueranger` ｜ **官方文档**：<https://www.kali.org/tools/blueranger/>

## 1. 安装

```bash
sudo apt update
sudo apt install blueranger
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.1 |
| 架构 | any |
| 可执行命令 | `blueranger` |
| 依赖 | `bluez` |
| 安装体积 | 13 KB |
| 官网 | <http://www.hackfromacave.com/projects/blueranger.html> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/blueranger> |
| 包追踪 | <https://pkg.kali.org/pkg/blueranger> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Use the Bluetooth interface (hci1) to scan for the specified remote address (20:C9:D0:43:4B:D8):
root@kali:~# blueranger hci1 20:C9:D0:43:4B:D8

Starting ...

Close with 2 X Crtl+C


      (((B(l(u(e(R)a)n)g)e)r)))

By JP Dunning (.ronin)
www.hackfromacave.com

Locating: ares (20:C9:D0:43:4B:D8)
Ping Count: 1

Proximity Change    Link Quality
----------------    ------------
FOUND           255/255

Range
------------------------------------
|*
------------------------------------
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `blueranger`

官方给出的调用示例：`blueranger hci1 20:C9:D0:43:4B:D8`

```text
root@kali:~# blueranger hci1 20:C9:D0:43:4B:D8
Starting ...
Close with 2 X Crtl+C
      (((B(l(u(e(R)a)n)g)e)r)))
By JP Dunning (.ronin)
www.hackfromacave.com
Locating: ares (20:C9:D0:43:4B:D8)
Ping Count: 1
Proximity Change    Link Quality
----------------    ------------
FOUND           255/255
Range
------------------------------------
|*
------------------------------------
```

### `blueranger（示例）`

官方给出的调用示例：`blueranger -h`

```text
root@kali:~# blueranger -h
BlueRanger 1.0 by JP Dunning (.ronin)
<www.hackfromacave.com>
(c) 2009-2012 Shadow Cave LLC.
NAME
	blueranger
SYNOPSIS
        /usr/bin/blueranger <hciX> <bdaddr>
DESCRIPTION
	<hciX>         Local interface
	<bdaddr>       Remote Device Address
Updated on: 2026-Mar-02
 Edit this page
bettercap
bruteforce-salted-openssl
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install blueranger`，再执行 `blueranger --version` 2>/dev/null || `blueranger -V`
- [ ] **2.** **读官方帮助** —— `blueranger -h`，需要细节时 `man blueranger`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `blueranger -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/blueranger/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/blueranger/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/blueranger/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
