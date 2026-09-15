# subfinder

> Subdomain discovery tool This package contains a subdomain discovery tool that discovers valid subdomains for websites by using passive online sources. It has a simple modular architecture and is optimized for speed. subfinder is built for…

> **功能分类**：通用工具 ｜ **Kali 包**：`subfinder` ｜ **官方文档**：<https://www.kali.org/tools/subfinder/>

## 1. 安装

```bash
sudo apt update
sudo apt install subfinder
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.16.0 |
| 架构 | any |
| 可执行命令 | `subfinder` |
| 依赖 | `libc6` |
| 安装体积 | 28.46 MB |
| 官网 | <https://github.com/projectdiscovery/subfinder> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/subfinder> |
| 包追踪 | <https://pkg.kali.org/pkg/subfinder> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
subfinder -h          # 查看用法
man subfinder         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `subfinder`

官方给出的调用示例：`subfinder -h`

```text
root@kali:~# subfinder -h
Subfinder is a subdomain discovery tool that discovers subdomains for websites by using passive online sources.
Usage:
  subfinder [flags]
Flags:
INPUT:
   -d, -domain string[]  domains to find subdomains for
   -dL, -list string     file containing list of domains for subdomain discovery
SOURCE:
   -s, -sources string[]           specific sources to use for discovery (-s crtsh,github). Use -ls to display all available sources.
   -recursive                      use only sources that can handle subdomains recursively rather than both recursive and non-recursive sources
   -all                            use all sources for enumeration (slow)
   -es, -exclude-sources string[]  sources to exclude from enumeration (-es alienvault,zoomeyeapi)
FILTER:
   -m, -match string[]   subdomain or list of subdomain to match (file or comma separated)
   -f, -filter string[]   subdomain or list of subdomain to filter (file or comma separated)
RATE-LIMIT:
   -rl, -rate-limit int      maximum number of http requests to send per second (global)
   -rls, -rate-limits value  maximum number of http requests to send per second for providers in key=value format (-rls hackertarget=10/m) (default ["github=30/m", "fullhunt=60/m", "pugrecon=10/s", "robtex=18446744073709551615/ms", "securitytrails=1/s", "shodan=1/s", "virustotal=4/m", "hackertarget=2/s", "waybackarchive=15/m", "whoisxmlapi=50/s", "securitytrails=2/s", "sitedossier=8/m", "netlas=1/s", "github=83/m", "hudsonrock=5/s", "urlscan=1/s"])
   -t int                    number of concurrent goroutines for resolving (-active only) (default 10)
UPDATE:
   -up, -update                 update subfinder to latest version
   -duc, -disable-update-check  disable automatic subfinder update check
OUTPUT:
   -o, -output string       file to write output to
   -oJ, -json               write output in JSONL(ines) format
   -oD, -output-dir string  directory to write output (-dL only)
   -cs, -collect-sources    include all sources in the output (-json only)
   -oI, -ip                 include host IP in output (-active only)
CONFIGURATION:
   -config string                flag config file (default "/root/.config/subfinder/config.yaml")
   -pc, -provider-config string  provider config file (default "/root/.config/subfinder/provider-config.yaml")
   -r string[]                   comma separated list of resolvers to use
   -rL, -rlist string            file containing list of resolvers to use
   -nW, -active                  display active subdomains only
   -proxy string                 http proxy to use with subfinder
   -ei, -exclude-ip              exclude IPs from the list of domains
   -mr, -max-results int         limit the number of results per source (0 = unlimited; honored by paginating sources)
DEBUG:
   -silent             show only subdomains in output
   -version            show version of subfinder
   -v                  show verbose output
   -nc, -no-color      disable color in output
   -ls, -list-sources  list all available sources (-oJ for JSON)
   -stats              report source statistics
OPTIMIZATION:
   -timeout int                   seconds to wait before timing out (default 30)
   -max-time int                  minutes to wait for enumeration results (default 10)
   -rsr, -response-size-read int  max response body size to read in bytes from passive sources (0 = unlimited)
Updated on: 2026-Aug-25
 Edit this page
stunnel
subversion
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install subfinder`，再执行 `subfinder --version` 2>/dev/null || `subfinder -V`
- [ ] **2.** **读官方帮助** —— `subfinder -h`，需要细节时 `man subfinder`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/subfinder/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/subfinder/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/subfinder/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
