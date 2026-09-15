# hakrawler

> Web crawler designed for easy, quick discovery of endpoints and assets Fast golang web crawler for gathering URLs and JavaSript file locations. This is basically a simple implementation of the awesome Gocolly library.

> **功能分类**：Web 应用 ｜ **Kali 包**：`hakrawler` ｜ **官方文档**：<https://www.kali.org/tools/hakrawler/>

## 1. 安装

```bash
sudo apt update
sudo apt install hakrawler
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.1 |
| 架构 | any |
| 可执行命令 | `hakrawler` |
| 依赖 | `libc6` |
| 安装体积 | 9.37 MB |
| 官网 | <https://github.com/hakluke/hakrawler> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/hakrawler> |
| 包追踪 | <https://pkg.kali.org/pkg/hakrawler> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
hakrawler -h          # 查看用法
man hakrawler         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hakrawler`

官方给出的调用示例：`hakrawler --help`

```text
root@kali:~# hakrawler --help
Usage of hakrawler:
  -d int
    	Depth to crawl. (default 2)
  -h string
    	Custom headers separated by two semi-colons. E.g. -h "Cookie: foo=bar;;Referer: http://example.com/"
  -insecure
    	Disable TLS verification.
  -json
    	Output as JSON.
  -proxy string
    	Proxy URL. E.g. -proxy http://127.0.0.1:8080
  -s	Show the source of URL based on where it was found. E.g. href, form, script, etc.
  -size int
    	Page size limit, in KB. (default -1)
  -subs
    	Include subdomains for crawling.
  -t int
    	Number of threads to utilise. (default 8)
  -timeout int
    	Maximum time to crawl each URL from stdin, in seconds. (default -1)
  -u	Show only unique urls.
Learn more with
OffSec
Want to learn more about hakrawler? get access to in-depth training and hands-on labs:
WEB-200: 2.2.5. Web Application Enumeration Methodology: Automated HTTP Endpoint Discovery
WEB-200 course
Updated on: 2025-Dec-09
 Edit this page
hak5-wifi-coconut
hamster-sidejack
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install hakrawler`，再执行 `hakrawler --version` 2>/dev/null || `hakrawler -V`
- [ ] **2.** **读官方帮助** —— `hakrawler -h`，需要细节时 `man hakrawler`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage of hakrawler:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hakrawler/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hakrawler/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hakrawler/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
