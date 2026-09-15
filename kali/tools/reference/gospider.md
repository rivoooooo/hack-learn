# gospider

> Fast web spider written in Go This package contains a Fast web spider written in Go. The features are: - Fast web crawling - Brute force and parse sitemap.xml - Parse robots.txt - Generate and verify link from JavaScript files

> **功能分类**：通用工具 ｜ **Kali 包**：`gospider` ｜ **官方文档**：<https://www.kali.org/tools/gospider/>

## 1. 安装

```bash
sudo apt update
sudo apt install gospider
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1.6 |
| 架构 | any |
| 可执行命令 | `gospider` |
| 依赖 | `libc6` |
| 安装体积 | 14.67 MB |
| 官网 | <https://github.com/jaeles-project/gospider> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/gospider> |
| 包追踪 | <https://pkg.kali.org/pkg/gospider> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gospider -h          # 查看用法
man gospider         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `gospider`

官方给出的调用示例：`gospider -h`

```text
root@kali:~# gospider -h
Fast web spider written in Go - v1.1.6 by @thebl4ckturtle & @j3ssiejjj
Usage:
  gospider [flags]
Flags:
  -s, --site string               Site to crawl
  -S, --sites string              Site list to crawl
  -p, --proxy string              Proxy (Ex: http://127.0.0.1:8080)
  -o, --output string             Output folder
  -u, --user-agent string         User Agent to use
                                  	web: random web user-agent
                                  	mobi: random mobile user-agent
                                  	or you can set your special user-agent (default "web")
      --cookie string             Cookie to use (testA=a; testB=b)
  -H, --header stringArray        Header to use (Use multiple flag to set multiple header)
      --burp string               Load headers and cookie from burp raw http request
      --blacklist string          Blacklist URL Regex
      --whitelist string          Whitelist URL Regex
      --whitelist-domain string   Whitelist Domain
  -L, --filter-length string      Turn on length filter
  -t, --threads int               Number of threads (Run sites in parallel) (default 1)
  -c, --concurrent int            The number of the maximum allowed concurrent requests of the matching domains (default 5)
  -d, --depth int                 MaxDepth limits the recursion depth of visited URLs. (Set it to 0 for infinite recursion) (default 1)
  -k, --delay int                 Delay is the duration to wait before creating a new request to the matching domains (second)
  -K, --random-delay int          RandomDelay is the extra randomized duration to wait added to Delay before creating a new request (second)
  -m, --timeout int               Request timeout (second) (default 10)
  -B, --base                      Disable all and only use HTML content
      --js                        Enable linkfinder in javascript file (default true)
      --sitemap                   Try to crawl sitemap.xml
      --robots                    Try to crawl robots.txt (default true)
  -a, --other-source              Find URLs from 3rd party (Archive.org, CommonCrawl.org, VirusTotal.com, AlienVault.com)
  -w, --include-subs              Include subdomains crawled from 3rd party. Default is main domain
  -r, --include-other-source      Also include other-source's urls (still crawl and request)
      --subs                      Include subdomains
      --debug                     Turn on debug mode
      --json                      Enable JSON output
  -v, --verbose                   Turn on verbose
  -q, --quiet                     Suppress all the output and only show URL
      --no-redirect               Disable redirect
      --version                   Check version
  -l, --length                    Turn on length
  -R, --raw                       Enable raw output
  -h, --help                      help for gospider
Updated on: 2026-Aug-25
 Edit this page
goshs
gr-air-modes
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install gospider`，再执行 `gospider --version` 2>/dev/null || `gospider -V`
- [ ] **2.** **读官方帮助** —— `gospider -h`，需要细节时 `man gospider`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gospider/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gospider/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gospider/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
