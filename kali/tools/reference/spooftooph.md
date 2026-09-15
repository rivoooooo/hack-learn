# spooftooph

> Automates spoofing or cloning Bluetooth devices Spooftooph is designed to automate spoofing or cloning Bluetooth device Name, Class, and Address. Cloning this information effectively allows Bluetooth device to hide in plain site. Bluetooth…

> **功能分类**：无线攻击 ｜ **Kali 包**：`spooftooph` ｜ **官方文档**：<https://www.kali.org/tools/spooftooph/>

## 1. 安装

```bash
sudo apt update
sudo apt install spooftooph
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.5.2 |
| 架构 | any |
| 可执行命令 | `spooftooph` |
| 依赖 | `bluez`、`libbluetooth3`、`libc6`、`libncurses6`、`libtinfo6` |
| 安装体积 | 74 KB |
| 官网 | <http://www.hackfromacave.com/projects/spooftooph.html> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/spooftooph> |
| 包追踪 | <https://pkg.kali.org/pkg/spooftooph> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Use the Bluetooth interface (-i hci1) to spoof itself as the given address (-a 00803789EE76):
root@kali:~# spooftooph -i hci1 -a 00803789EE76
Manufacturer:   Broadcom Corporation (15)
Device address: 00:19:0E:0E:EA:4B
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `spooftooph`

官方给出的调用示例：`spooftooph -i hci1 -a 00803789EE76`

```text
root@kali:~# spooftooph -i hci1 -a 00803789EE76
Manufacturer:   Broadcom Corporation (15)
Device address: 00:19:0E:0E:EA:4B
```

### `spooftooph（示例）`

官方给出的调用示例：`spooftooph -h`

```text
root@kali:~# spooftooph -h
spooftooph v0.5.2 by JP Dunning (.ronin)
<www.hackfromacave.com>
(c) 2009-2012 Shadow Cave LLC.
NAME
	spooftooph
SYNOPSIS
	spooftooph -i dev [-mstu] [-nac]|[-R]|[-r file] [-w file]
DESCRIPTION
	-a <address>	: Specify new BD_ADDR
	-b <num_lines>	: Number of Bluetooth profiles to display per page
	-B 		: Disable banner for smaller screens (like phones)
	-c <class>	: Specify new CLASS
	-h		: Help
	-i <dev>	: Specify interface
	-m		: Specify multiple interfaces during selection
	-n <name>	: Specify new NAME
	-r <file>	: Read in CSV logfile
	-R		: Assign random NAME, CLASS, and ADDR
	-s		: Scan for devices in local area
	-t <time>	: Time interval to clone device in range
	-u		: USB delay.  Interactive delay for reinitializing interface
	-w <file>	: Write to CSV logfile
			  (Useful in Virtualized environment when USB must be passed through.)
Updated on: 2025-Dec-09
 Edit this page
snmpcheck
spray
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install spooftooph`，再执行 `spooftooph --version` 2>/dev/null || `spooftooph -V`
- [ ] **2.** **读官方帮助** —— `spooftooph -h`，需要细节时 `man spooftooph`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `spooftooph -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/spooftooph/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/spooftooph/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/spooftooph/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
