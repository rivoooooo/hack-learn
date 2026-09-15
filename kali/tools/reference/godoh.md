# godoh

> DNS-over-HTTPS Command & Control Proof of Concept This package contains a proof of concept Command and Control framework, written in Golang, that uses DNS-over-HTTPS as a transport medium. Currently supported providers include Google, Clou…

> **功能分类**：通用工具 ｜ **Kali 包**：`godoh` ｜ **官方文档**：<https://www.kali.org/tools/godoh/>

## 1. 安装

```bash
sudo apt update
sudo apt install godoh
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6 |
| 架构 | any |
| 可执行命令 | `godoh` |
| 依赖 | `libc6` |
| 安装体积 | 7.42 MB |
| 官网 | <https://github.com/sensepost/goDoH> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/godoh> |
| 包追踪 | <https://pkg.kali.org/pkg/godoh> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
godoh -h          # 查看用法
man godoh         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `godoh`

官方给出的调用示例：`godoh -h`

```text
root@kali:~# godoh -h
A DNS (over-HTTPS) C2
    Version:
	By @leonjza from @sensepost
Usage:
  godoh [flags]
  godoh [command]
Available Commands:
  agent       Connect as an Agent to the DoH C2
  c2          Starts the godoh C2 server
  completion  Generate the autocompletion script for the specified shell
  help        Help about any command
  receive     Receive a file via DoH
  send        Send a file via DoH
  test        Test DNS communications
Flags:
  -d, --domain string          DNS Domain to use. (ie: example.com)
  -h, --help                   help for godoh
  -p, --provider string        Preferred DNS provider to use. [possible: googlefront, google, cloudflare, quad9, raw] (default "google")
  -K, --validate-certificate   Validate DoH provider SSL certificates
Use "godoh [command] --help" for more information about a command.
Updated on: 2025-Dec-09
 Edit this page
getsploit
golang-github-binject-go-donut
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install godoh`，再执行 `godoh --version` 2>/dev/null || `godoh -V`
- [ ] **2.** **读官方帮助** —— `godoh -h`，需要细节时 `man godoh`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/godoh/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/godoh/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/godoh/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
