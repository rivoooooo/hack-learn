# netmask

> Helps determine network masks This is a tiny program handy if you work with firewalls or routers occasionally (possibly using this as a helper for shell scripts). It can determine the smallest set of network masks to specify a range of hos…

> **功能分类**：信息搜集 ｜ **Kali 包**：`netmask` ｜ **官方文档**：<https://www.kali.org/tools/netmask/>

## 1. 安装

```bash
sudo apt update
sudo apt install netmask
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.5.0 |
| 架构 | any |
| 可执行命令 | `netmask` |
| 依赖 | `libc6` |
| 安装体积 | 74 KB |
| 官网 | <https://github.com/tlby/netmask> |
| 源码仓库 | <https://salsa.debian.org/debian/netmask> |
| 包追踪 | <https://pkg.kali.org/pkg/netmask> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
netmask -h          # 查看用法
man netmask         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `netmask`

官方给出的调用示例：`netmask -h`

```text
root@kali:~# netmask -h
This is netmask, an address netmask generation utility
Usage: netmask spec [spec ...]
  -h, --help			Print a summary of the options
  -v, --version			Print the version number
  -d, --debug			Print status/progress information
  -s, --standard		Output address/netmask pairs
  -c, --cidr			Output CIDR format address lists
  -i, --cisco			Output Cisco style address lists
  -r, --range			Output ip address ranges
  -x, --hex			Output address/netmask pairs in hex
  -o, --octal			Output address/netmask pairs in octal
  -b, --binary			Output address/netmask pairs in binary
  -n, --nodns			Disable DNS lookups for addresses
  -f, --files			Treat arguments as input files
Definitions:
  a spec can be any of:
    address
    address:address
    address:+address
    address/mask
  an address can be any of:
    N		decimal number
    0N		octal number
    0xN		hex number
    N.N.N.N	dotted quad
    hostname	dns domain name
  a mask is the number of bits set to one from the left
Updated on: 2025-Dec-09
 Edit this page
netdiscover
netsed
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install netmask`，再执行 `netmask --version` 2>/dev/null || `netmask -V`
- [ ] **2.** **读官方帮助** —— `netmask -h`，需要细节时 `man netmask`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: netmask spec [spec ...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/netmask/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/netmask/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/netmask/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
