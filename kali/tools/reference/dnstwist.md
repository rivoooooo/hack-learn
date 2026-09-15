# dnstwist

> Domain name permutation engine dnstwist generates a list of similarly looking domain names for a given domain name and performs DNS queries for them (A, AAAA, NS and MX). For MX records it checks whether there is an active mail server whic…

> **功能分类**：通用工具 ｜ **Kali 包**：`dnstwist` ｜ **官方文档**：<https://www.kali.org/tools/dnstwist/>

## 1. 安装

```bash
sudo apt update
sudo apt install dnstwist
```

| 项目 | 内容 |
|------|------|
| 版本 | 0~20250130 |
| 架构 | all |
| 可执行命令 | `dnstwist` |
| 依赖 | `python3` |
| 安装体积 | 489 KB |
| 官网 | <https://github.com/elceef/dnstwist> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/dnstwist> |
| 包追踪 | <https://pkg.kali.org/pkg/dnstwist> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
dnstwist -h          # 查看用法
man dnstwist         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dnstwist`

官方给出的调用示例：`dnstwist -h`

```text
root@kali:~# dnstwist -h
dnstwist 20250130 by <
[email protected]
>
usage: /usr/bin/dnstwist [OPTION]... DOMAIN
Domain name permutation engine for detecting homograph phishing attacks,
typosquatting, fraud and brand impersonation.
positional arguments:
  domain                 Domain name or URL to scan
options:
  -a, --all              Print all DNS records instead of the first ones
  -b, --banners          Determine HTTP and SMTP service banners
  -d, --dictionary FILE  Generate more domains using dictionary FILE
  -f, --format FORMAT    Output format: cli, csv, json, list (default: cli)
  --fuzzers LIST         Use only selected fuzzing algorithms (separated with
                         commas)
  -g, --geoip            Lookup for GeoIP location
  --lsh [LSH]            Evaluate web page similarity with LSH algorithm:
                         ssdeep, tlsh (default: ssdeep)
  --lsh-url URL          Override URL to fetch the original web page from
  -m, --mxcheck          Check if MX host can be used to intercept emails
  -o, --output FILE      Save output to FILE
  -r, --registered       Show only registered domain names
  -u, --unregistered     Show only unregistered domain names
  -p, --phash            Render web pages and evaluate visual similarity
  --phash-url URL        Override URL to render the original web page from
  --screenshots DIR      Save web page screenshots into DIR
  -t, --threads NUM      Start specified NUM of threads (default: 10)
  -w, --whois            Lookup WHOIS database for creation date and registrar
  --tld FILE             Swap TLD for the original domain from FILE
  --nameservers LIST     DNS or DoH servers to query (separated with commas)
  --useragent STRING     Set User-Agent STRING (default: Mozilla/5.0 (linux
                         64-bit) dnstwist/20250130)
Updated on: 2025-Dec-09
 Edit this page
dnsgen
doona
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dnstwist`，再执行 `dnstwist --version` 2>/dev/null || `dnstwist -V`
- [ ] **2.** **读官方帮助** —— `dnstwist -h`，需要细节时 `man dnstwist`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `dnstwist -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dnstwist/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dnstwist/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dnstwist/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
