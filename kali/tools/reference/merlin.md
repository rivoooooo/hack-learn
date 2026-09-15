# merlin

> Command & Control server & agent (metapackage) This package contains a cross-platform post-exploitation HTTP/2 Command & Control server and agent written in golang as well as an identification tool.

> **功能分类**：通用工具 ｜ **Kali 包**：`merlin` ｜ **官方文档**：<https://www.kali.org/tools/merlin/>

## 1. 安装

```bash
sudo apt update
sudo apt install merlin
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.1.4 |
| 架构 | any |
| 可执行命令 | `golang-github-ne0nd0g-merlin-dev`、`merlin`、`merlin-server`、`merlinserver` |
| 依赖 | `merlin-agent`、`merlin-server`、`merlin-server` |
| 安装体积 | 23 KB |
| 官网 | <https://github.com/Ne0nd0g/merlin> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/merlin> |
| 包追踪 | <https://pkg.kali.org/pkg/merlin> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
golang-github-ne0nd0g-merlin-dev -h          # 查看用法
man golang-github-ne0nd0g-merlin-dev         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `merlinserver`

官方给出的调用示例：`merlinserver -h`

```text
root@kali:~# merlinserver -h
Usage of ./merlin:
  -addr string
    	The address to listen on for client connections (default "127.0.0.1:50051")
  -debug
    	Enable debug logging
  -extra
    	Enable extra debug logging
  -password string
    	the password to for CLI RPC clients to connect to this server (default "merlin")
  -secure
    	Require client TLS certificate verification
  -tlsCA string
    	TLS Certificate Authority file path to verify client certificates
  -tlsCert string
    	TLS certificate file path
  -tlsKey string
    	TLS private key file path
  -trace
    	Enable trace logging
  -version
    	Print the version number and exit
Updated on: 2025-Dec-09
 Edit this page
memdump
metagoofil
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install merlin`，再执行 `golang-github-ne0nd0g-merlin-dev --version` 2>/dev/null || `golang-github-ne0nd0g-merlin-dev -V`
- [ ] **2.** **读官方帮助** —— `golang-github-ne0nd0g-merlin-dev -h`，需要细节时 `man golang-github-ne0nd0g-merlin-dev`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage of ./merlin:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/merlin/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/merlin/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/merlin/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
