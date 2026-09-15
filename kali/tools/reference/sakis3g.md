# sakis3g

> Tool for establishing 3G connections Sakis3G is a tweaked shell script which is supposed to work out-of-the-box for establishing a 3G connection with any combination of modem or operator. It automagically setups your USB or Bluetooth™ mode…

> **功能分类**：无线攻击 ｜ **Kali 包**：`sakis3g` ｜ **官方文档**：<https://www.kali.org/tools/sakis3g/>

## 1. 安装

```bash
sudo apt update
sudo apt install sakis3g
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.2.0e |
| 架构 | any |
| 可执行命令 | `sakis3g` |
| 依赖 | `bzip2`、`libusb-1.0-0` |
| 安装体积 | 537 KB |
| 官网 | <http://www.sakis3g.org> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sakis3g> |
| 包追踪 | <https://pkg.kali.org/pkg/sakis3g> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sakis3g -h          # 查看用法
man sakis3g         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sakis3g`

官方给出的调用示例：`sakis3g --interactive "connect"`

```text
root@kali:~# sakis3g --interactive "connect"
```

### `sakis3g（示例）`

官方给出的调用示例：`sakis3g --help`

```text
root@kali:~# sakis3g --help
Sakis 3G All-in-one script - Version 0.2.0e
(c) Sakis Dimopoulos 2009, 2010 under GNU GPL v2
Usage:
      sakis3g [actors] [switches] [variables]
Sakis3G is a shell script which is supposed to work out-of-the-box for
establishing a 3G connection with any combination of modem or operator.
NOTE: This script requires root priviledges to properly work. If not executed
from root, it will try to acquire them.
Common actors are:
connect       - Attempts to establish 3G connection.
disconnect    - Stops all active PPP connections.
toggle        - Attempts to establish 3G connection. If already connected, it
disconnects instead.
reconnect     - Attempts to establish 3G connection. If already connected, it
first disconnects and then attempts.
start         - Same as connect. Provided for use as init.d script.
stop          - Same as disconnect. Provided for use as init.d script.
reload        - Same as reconnect. Provided for use as init.d script.
force-reload  - Same as reload. Provided for use as init.d script.
restart       - Same as reload. Provided for use as init.d script.
desktop       - Creates desktop shortcut for this script.
status        - Prints connection status and exits. Exit code is 0 if
connected, or 6 if not connected.
help          - Prints this screen and exits.
man           - Displays man page.
NOTE: For more information, you should consult man page or official Sakis3G
wiki, available at:
  http://wiki.sakis3g.org/
Updated on: 2025-Dec-09
 Edit this page
s3scanner
samdump2
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sakis3g`，再执行 `sakis3g --version` 2>/dev/null || `sakis3g -V`
- [ ] **2.** **读官方帮助** —— `sakis3g -h`，需要细节时 `man sakis3g`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sakis3g/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sakis3g/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sakis3g/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
