# dnsx

> Perform multiple dns queries This package contains a fast and multi-purpose DNS toolkit allow to run multiple probes using retryabledns library, that allows you to perform multiple DNS queries of your choice with a list of user supplied re…

> **功能分类**：通用工具 ｜ **Kali 包**：`dnsx` ｜ **官方文档**：<https://www.kali.org/tools/dnsx/>

## 1. 安装

```bash
sudo apt update
sudo apt install dnsx
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3.1 |
| 架构 | any |
| 可执行命令 | `dnsx` |
| 依赖 | `libc6` |
| 安装体积 | 27.80 MB |
| 官网 | <https://github.com/projectdiscovery/dnsx> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/dnsx> |
| 包追踪 | <https://pkg.kali.org/pkg/dnsx> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
dnsx -h          # 查看用法
man dnsx         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dnsx`

官方给出的调用示例：`dnsx -h`

```text
root@kali:~# dnsx -h
dnsx is a fast and multi-purpose DNS toolkit allow to run multiple probes using retryabledns library.
Usage:
  dnsx [flags]
Flags:
INPUT:
   -l, -list string      list of sub(domains)/hosts to resolve (file or comma separated or stdin)
   -d, -domain string    list of domain to bruteforce (file or comma separated or stdin)
   -w, -wordlist string  list of words to bruteforce (file or comma separated or stdin)
QUERY:
   -a                       query A record (default)
   -aaaa                    query AAAA record
   -cname                   query CNAME record
   -ns                      query NS record
   -txt                     query TXT record
   -srv                     query SRV record
   -ptr                     query PTR record
   -mx                      query MX record
   -soa                     query SOA record
   -any                     query ANY record
   -axfr                    query AXFR
   -caa                     query CAA record
   -all, -recon             query all the dns records (a,aaaa,cname,ns,txt,srv,ptr,mx,soa,axfr,caa)
   -e, -exclude-type value  dns query type to exclude (a,aaaa,cname,ns,txt,srv,ptr,mx,soa,axfr,caa) (default none)
FILTER:
   -re, -resp                          display dns response
   -ro, -resp-only                     display dns response only
   -rc, -rcode string                  filter result by dns status code (eg. -rcode noerror,servfail,refused)
   -rtf, -response-type-filter string  return entries with no records for the specified query types (e.g., a, cname)
PROBE:
   -cdn  display cdn name
   -asn  display host asn information
RATE-LIMIT:
   -t, -threads int      number of concurrent threads to use (default 100)
   -rl, -rate-limit int  number of dns request/second to make (disabled as default) (default -1)
UPDATE:
   -up, -update                 update dnsx to latest version
   -duc, -disable-update-check  disable automatic dnsx update check
OUTPUT:
   -o, -output string            file to write output
   -j, -json                     write output in JSONL(ines) format
   -omit-raw, -or                omit raw dns response from jsonl output
   -ot, -output-template string  custom output template (e.g. -ot '{{host}} {{a}}')
DEBUG:
   -hc, -health-check  run diagnostic check up
   -silent             display only results in the output
   -v, -verbose        display verbose output
   -raw, -debug        display raw dns response
   -stats              display stats of the running scan
   -version            display version of dnsx
   -nc, -no-color      disable color in output
OPTIMIZATION:
   -retry int                number of dns attempts to make (must be at least 1) (default 2)
   -hf, -hostsfile           use system host file
   -trace                    perform dns tracing
   -trace-max-recursion int  Max recursion for dns trace (default 255)
   -resume                   resume existing scan
   -stream                   stream mode (wordlist, wildcard, stats and stop/resume will be disabled)
   -timeout value            maximum time to wait for a DNS query to complete (default 3s)
CONFIGURATIONS:
   -auth                         configure ProjectDiscovery Cloud Platform (PDCP) api key (default true)
   -r, -resolver string          list of resolvers to use (file or comma separated)
   -wt, -wildcard-threshold int  wildcard filter threshold (default 5)
   -auto-wildcard                automatically detect wildcard domains for filtering
   -wd, -wildcard-domain string  domain name for manual wildcard filtering (mutually exclusive with -auto-wildcard; other flags will be ignored - json output recommended)
   -proxy string                 proxy to use (eg socks5://127.0.0.1:8080)
Updated on: 2026-Aug-25
 Edit this page
dnswalk
dradis
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dnsx`，再执行 `dnsx --version` 2>/dev/null || `dnsx -V`
- [ ] **2.** **读官方帮助** —— `dnsx -h`，需要细节时 `man dnsx`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dnsx/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dnsx/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dnsx/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
