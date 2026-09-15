# openocd

> Open on-chip JTAG/SWD debug solution for embedded target devices OpenOCD aims to provide debugging, in-system programming and boundary-scan testing for embedded target devices. The debugger uses an IEEE 1149-1 compliant JTAG TAP bus master…

> **功能分类**：硬件攻击 ｜ **Kali 包**：`openocd` ｜ **官方文档**：<https://www.kali.org/tools/openocd/>

## 1. 安装

```bash
sudo apt update
sudo apt install openocd
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.12.0 |
| 架构 | any |
| 可执行命令 | `openocd` |
| 依赖 | `libc6`、`libcapstone5`、`libftdi1-2`、`libhidapi-hidraw0`、`libjaylink0`、`libjim0.84`、`libusb-1.0-0` |
| 安装体积 | 8.97 MB |
| 官网 | <http://openocd.sourceforge.net/> |
| 源码仓库 | <https://salsa.debian.org/electronics-team/openocd> |
| 包追踪 | <https://pkg.kali.org/pkg/openocd> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
openocd -h          # 查看用法
man openocd         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `openocd`

官方给出的调用示例：`openocd -h`

```text
root@kali:~# openocd -h
Open On-Chip Debugger 0.12.0
Licensed under GNU GPL v2
For bug reports, read
	http://openocd.org/doc/doxygen/bugs.html
Open On-Chip Debugger
Licensed under GNU GPL v2
--help       | -h	display this help
--version    | -v	display OpenOCD version
--file       | -f	use configuration file <name>
--search     | -s	dir to search for config files and scripts
--debug      | -d	set debug level to 3
             | -d<n>	set debug level to <level>
--log_output | -l	redirect log output to file <name>
--command    | -c	run <command>
Updated on: 2026-Aug-25
 Edit this page
oletools
openssh
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install openocd`，再执行 `openocd --version` 2>/dev/null || `openocd -V`
- [ ] **2.** **读官方帮助** —— `openocd -h`，需要细节时 `man openocd`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `openocd -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/openocd/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/openocd/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/openocd/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
