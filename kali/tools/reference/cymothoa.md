# cymothoa

> Stealth backdooring tool Cymothoa is a stealth backdooring tool, that inject backdoor’s shellcode into an existing process. The tool uses the ptrace library (available on nearly all * nix), to manipulate processes and infect them.

> **功能分类**：后渗透 ｜ **Kali 包**：`cymothoa` ｜ **官方文档**：<https://www.kali.org/tools/cymothoa/>

## 1. 安装

```bash
sudo apt update
sudo apt install cymothoa
```

| 项目 | 内容 |
|------|------|
| 版本 | 1 |
| 架构 | i386 |
| 可执行命令 | `cymothoa`、`bgrep`、`udp_server` |
| 依赖 | `libc6`、`bgrep` |
| 安装体积 | 90 KB |
| 官网 | <https://cymothoa.sourceforge.net/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/cymothoa> |
| 包追踪 | <https://pkg.kali.org/pkg/cymothoa> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
bgrep – Binary grep
root@kali:~# bgrep
bgrep version: 0.2
usage: bgrep <hex> [<path> [...]]

udp_server – UDP server for Cymothoa
root@kali:~# udp_server
usage: udp_server port
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `udp_server`

```text
root@kali:~# udp_server
usage: udp_server port
">
 [
 [...]]
udp_server – UDP server for Cymothoa
```

### `udp_server`

```text
root@kali:~# udp_server
usage: udp_server port
">
 [
 [...]]
udp_server – UDP server for Cymothoa
```

### `udp_server`

```text
root@kali:~# udp_server
usage: udp_server port
">
 [
 [...]]
udp_server – UDP server for Cymothoa
```

### `udp_server`

```text
root@kali:~# udp_server
usage: udp_server port
">
Join Free CTF
Get Kali
Blog
Documentation
Documentation Pages
Tools Documentation
Frequently Asked Questions
Known Issues
Community
Community Support
Forums
Discord
Join Newsletter
Mirror Location
Get Involved
Courses
Developers
Git Repositories
Packages
Auto Package Test
Bug Tracker
Kali NetHunter Stats
About
Kali Linux Overview
Press Pack
Wallpapers
Kali Swag Store
Meet The Kali Team
Partnerships
Contact Us
```

### `bgrep`

```text
root@kali:~# bgrep
bgrep version: 0.2
usage: bgrep <hex> [<path> [...]]
udp_server – UDP server for Cymothoa
```

### `udp_server`

```text
root@kali:~# udp_server
usage: udp_server port
```

### `cymothoa`

> 官方示例调用：`cymothoa -h`

```text
root@kali:~# cymothoa -h
                              _
                          _  | |
  ____ _   _ ____   ___ _| |_| |__   ___  _____
 / ___) | | |    \ / _ (_   _)  _ \ / _ \(____ |
( (___| |_| | | | | |_| || |_| | | | |_| / ___ |
 \____)\__  |_|_|_|\___/  \__)_| |_|\___/\_____|
      (____/
Ver.1 (beta) - Runtime shellcode injection, for stealthy backdoors...
By codwizard (
[email protected]
) and crossbower (
[email protected]
)
from ES-Malaria by ElectronicSouls (http://www.0x4553.org).
Usage:
	cymothoa -p <pid> -s <shellcode_number> [options]
Main options:
	-p	process pid
	-s	shellcode number
	-l	memory region name for shellcode injection (default /lib/ld)
	  	search for "r-xp" permissions, see /proc/pid/maps...
	-m	memory region name for persistent memory (default /lib/ld)
	  	search for "rw-p" permissions, see /proc/pid/maps...
	-h	print this help screen
	-S	list available shellcodes
Injection options (overwrite payload flags):
	-f	fork parent process
	-F	don't fork parent process
	-b	create payload thread (probably you need also -F)
	-B	don't create payload thread
	-w	pass persistent memory address
	-W	don't pass persistent memory address
	-a	use alarm scheduler
	-A	don't use alarm scheduler
	-t	use setitimer scheduler
	-T	don't use setitimer scheduler
Payload arguments:
	-j	set timer (seconds)
	-k	set timer (microseconds)
	-x	set the IP
	-y	set the port number
	-r	set the port number 2
	-z	set the username (4 bytes)
	-o	set the password (8 bytes)
	-c	set the script code (ex: "#!/bin/sh\nls; exit 0")
	  	escape codes will not be interpreted...
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install cymothoa`，再执行 `cymothoa --version` 2>/dev/null || `cymothoa -V`
- [ ] **2.** **读官方帮助** —— `cymothoa -h`，需要细节时 `man cymothoa`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cymothoa/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/persistence.md`](../../tools/by-attack/persistence.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cymothoa/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cymothoa/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
