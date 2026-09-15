# axel

> Light command line download accelerator Axel tries to accelerate the downloading process by using multiple connections for one file, similar to DownThemAll and other famous programs. It can also use multiple mirrors for one download. Using…

> **功能分类**：通用工具 ｜ **Kali 包**：`axel` ｜ **官方文档**：<https://www.kali.org/tools/axel/>

## 1. 安装

```bash
sudo apt update
sudo apt install axel
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.17.14 |
| 架构 | any |
| 可执行命令 | `axel` |
| 依赖 | `libc6`、`libssl3t64` |
| 安装体积 | 223 KB |
| 官网 | <https://github.com/axel-download-accelerator/axel> |
| 源码仓库 | <https://salsa.debian.org/debian/axel> |
| 包追踪 | <https://pkg.kali.org/pkg/axel> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
axel -h          # 查看用法
man axel         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `axel`

> 官方示例调用：`axel -h`

```text
root@kali:~# axel -h
Axel 2.17.14 (linux-gnu)
Usage: axel [options] url1 [url2] [url...]
--max-speed=x		-s x	Specify maximum speed (bytes per second)
--num-connections=x	-n x	Specify maximum number of connections
--max-redirect=x		Specify maximum number of redirections
--output=f		-o f	Specify local output file
--search[=n]		-S[n]	Search for mirrors and download from n servers
--ipv4			-4	Use the IPv4 protocol
--ipv6			-6	Use the IPv6 protocol
--header=x		-H x	Add HTTP header string
--user-agent=x		-U x	Set user agent
--no-proxy		-N	Just don't use any proxy server
--insecure		-k	Don't verify the SSL certificate
--no-clobber		-c	Skip download if file already exists
--quiet			-q	Leave stdout alone
--verbose		-v	More status information
--alternate		-a	Alternate progress indicator
--percentage		-p	Print simple percentages instead of progress bar (0-100)
--help			-h	This information
--timeout=x		-T x	Set I/O and connection timeout
--version		-V	Version information
Visit https://github.com/axel-download-accelerator/axel/issues to report bugs
Updated on: 2026-Aug-25
 Edit this page
atftp
azurehound
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install axel`，再执行 `axel --version` 2>/dev/null || `axel -V`
- [ ] **2.** **读官方帮助** —— `axel -h`，需要细节时 `man axel`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: axel [options] url1 [url2] [url...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/axel/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/axel/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/axel/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
