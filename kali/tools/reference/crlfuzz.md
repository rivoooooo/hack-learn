# crlfuzz

> Fast tool to scan CRLF vulnerability written in Go CRLFuzz is a tool to scan for CRLF vulnerabilities in a fast way using Go

> **功能分类**：通用工具 ｜ **Kali 包**：`crlfuzz` ｜ **官方文档**：<https://www.kali.org/tools/crlfuzz/>

## 1. 安装

```bash
sudo apt update
sudo apt install crlfuzz
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.4.1 |
| 架构 | any |
| 可执行命令 | `crlfuzz` |
| 依赖 | `libc6` |
| 安装体积 | 5.48 MB |
| 官网 | <https://github.com/dwisiswant0/crlfuzz> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/crlfuzz> |
| 包追踪 | <https://pkg.kali.org/pkg/crlfuzz> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
crlfuzz -h          # 查看用法
man crlfuzz         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `crlfuzz`

> 官方示例调用：`crlfuzz -h`

```text
root@kali:~# crlfuzz -h
   _____ _____ __    _____
  |     | __  |  |  |   __|_ _ ___ ___
  |   --|    -|  |__|   __| | |- _|- _|
  |_____|__|__|_____|__|  |___|___|___|
      v1.4.0 - @dwisiswant0
[WRN] Use with caution. You are responsible for your actions
[WRN] Developers assume no liability and are not responsible for any misuse or damage.
Usage:
  [buffers] | crlfuzz [options]
  crlfuzz [options]
Options:
  -u, --url <URL>           Define single URL to fuzz
  -l, --list <FILE>         Fuzz URLs within file
  -X, --method <METHOD>     Specify request method to use (default: GET)
  -o, --output <FILE>       File to save results
  -d, --data <DATA>         Define request data
  -H, --header <HEADER>     Pass custom header to target
  -x, --proxy <URL>         Use proxy to fuzz
  -c, --concurrent <i>      Set the concurrency level (default: 20)
  -s, --silent              Silent mode
  -v, --verbose             Verbose mode
  -V, --version             Show current CRLFuzz version
  -h, --help                Display its help
Updated on: 2025-Dec-09
 Edit this page
creddump7
crowbar
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install crlfuzz`，再执行 `crlfuzz --version` 2>/dev/null || `crlfuzz -V`
- [ ] **2.** **读官方帮助** —— `crlfuzz -h`，需要细节时 `man crlfuzz`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/crlfuzz/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/crlfuzz/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/crlfuzz/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
