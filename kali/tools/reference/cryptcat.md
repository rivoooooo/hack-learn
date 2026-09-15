# cryptcat

> Lightweight version netcat extended with twofish encryption Cryptcat is a simple Unix utility which reads and writes data across network connections, using TCP or UDP protocol while encrypting the data being transmitted. It is designed to …

> **功能分类**：通用工具 ｜ **Kali 包**：`cryptcat` ｜ **官方文档**：<https://www.kali.org/tools/cryptcat/>

## 1. 安装

```bash
sudo apt update
sudo apt install cryptcat
```

| 项目 | 内容 |
|------|------|
| 版本 | 20031202 |
| 架构 | any |
| 可执行命令 | `cryptcat` |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6` |
| 安装体积 | 80 KB |
| 官网 | <http://farm9.com/content/Free_Tools/cryptcat_linux2.tar> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/cryptcat> |
| 包追踪 | <https://pkg.kali.org/pkg/cryptcat> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
On the server, listen for a connection (-l) on port 4444 (-p 4444) and don’t do name resolution (-n). Redirect all data to a file (> dataxfer). On the client, connect to the remote IP address (192.168.1.202) on port 4444 (4444) and pipe in the data to be transferred (< /tmp/juicyinfo):
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cryptcat`

官方给出的调用示例：`cryptcat -l -p 4444 -n > dataxfer`

```text
root@kali:~# cryptcat -l -p 4444 -n > dataxfer
```

### `cryptcat（示例）`

官方给出的调用示例：`cryptcat 192.168.1.202 4444 < /tmp/juicyinfo`

```text
root@kali:~# cryptcat 192.168.1.202 4444 < /tmp/juicyinfo
```

### `cryptcat（示例）`

官方给出的调用示例：`cryptcat -h`

```text
root@kali:~# cryptcat -h
[v1.10]
connect to somewhere:	nc [-options] hostname port[s] [ports] ...
listen for inbound:	nc -l -p port [-options] [hostname] [port]
options:
	-g gateway		source-routing hop point[s], up to 8
	-G num			source-routing pointer: 4, 8, 12, ...
	-h			this cruft
	-i secs			delay interval for lines sent, ports scanned
	-l			listen mode, for inbound connects
	-n			numeric-only IP addresses, no DNS
	-o file			hex dump of traffic
	-p port			local port number
	-r			randomize local and remote ports
	-s addr			local source address
	-u			UDP mode
	-v			verbose [use twice to be more verbose]
	-w secs			timeout for connects and final net reads
	-z			zero-I/O mode [used for scanning]
port numbers can be individual or ranges: lo-hi [inclusive]
Updated on: 2025-Dec-09
 Edit this page
crunch
cryptsetup-nuke-password
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cryptcat`，再执行 `cryptcat --version` 2>/dev/null || `cryptcat -V`
- [ ] **2.** **读官方帮助** —— `cryptcat -h`，需要细节时 `man cryptcat`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `cryptcat -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cryptcat/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cryptcat/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cryptcat/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
