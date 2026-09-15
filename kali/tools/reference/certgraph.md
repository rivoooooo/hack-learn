# certgraph

> Tool to crawl the graph of certificate Alternate Names This package contains a tool to crawl the graph of certificate Alternate Names. CertGraph crawls SSL certificates creating a directed graph where each domain is a node and the certific…

> **功能分类**：通用工具 ｜ **Kali 包**：`certgraph` ｜ **官方文档**：<https://www.kali.org/tools/certgraph/>

## 1. 安装

```bash
sudo apt update
sudo apt install certgraph
```

| 项目 | 内容 |
|------|------|
| 版本 | 20180911 |
| 架构 | any |
| 可执行命令 | `certgraph` |
| 依赖 | `libc6` |
| 安装体积 | 6.37 MB |
| 官网 | <https://github.com/lanrat/certgraph> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/certgraph> |
| 包追踪 | <https://pkg.kali.org/pkg/certgraph> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
certgraph -h          # 查看用法
man certgraph         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `certgraph`

官方给出的调用示例：`certgraph -h`

```text
root@kali:~# certgraph -h
Usage of certgraph: [OPTION]... HOST...
	https://github.com/lanrat/certgraph
OPTIONS:
  -cdn
    	include certificates from CDNs
  -ct-expired
    	include expired certificates in certificate transparency search
  -ct-subdomains
    	include sub-domains in certificate transparency search
  -depth uint
    	maximum BFS depth to go (default 5)
  -details
    	print details about the domains crawled
  -dns
    	check for DNS records to determine if domain is registered
  -driver string
    	driver to use [crtsh, google, http, smtp] (default "http")
  -json
    	print the graph as json, can be used for graph in web UI
  -parallel uint
    	number of certificates to retrieve in parallel (default 10)
  -sanscap int
    	maximum number of uniq TLD+1 domains in certificate to include, 0 has no limit (default 80)
  -save string
    	save certs to folder in PEM format
  -timeout uint
    	tcp timeout in seconds (default 10)
  -tldplus1
    	for every domain found, add tldPlus1 of the domain's parent
  -updatepsl
    	Update the default Public Suffix List
  -verbose
    	verbose logging
  -version
    	print version and exit
Updated on: 2025-Dec-09
 Edit this page
cabextract
certi
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install certgraph`，再执行 `certgraph --version` 2>/dev/null || `certgraph -V`
- [ ] **2.** **读官方帮助** —— `certgraph -h`，需要细节时 `man certgraph`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage of certgraph: [OPTION]... HOST...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/certgraph/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/certgraph/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/certgraph/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
