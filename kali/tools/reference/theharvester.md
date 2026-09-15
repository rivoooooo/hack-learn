# theharvester

> Tool for gathering e-mail accounts and subdomain names from public sources The package contains a tool for gathering subdomain names, e-mail addresses, virtual hosts, open ports/ banners, and employee names from different public sources (s…

> **功能分类**：信息搜集 ｜ **Kali 包**：`theharvester` ｜ **官方文档**：<https://www.kali.org/tools/theharvester/>

## 1. 安装

```bash
sudo apt update
sudo apt install theharvester
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.11.1 |
| 架构 | all |
| 可执行命令 | `theharvester` |
| 依赖 | `kali-defaults`、`python3`、`python3-aiodns`、`python3-aiofiles`、`python3-aiohttp`、`python3-aiohttp-socks`、`python3-aiomultiprocess`、`python3-aiosqlite`、`python3-bs4`、`python3-censys`、`python3-certifi`、`python3-dateutil` 等 |
| 安装体积 | 2.26 MB |
| 官网 | <https://github.com/laramies/theHarvester> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/theharvester> |
| 包追踪 | <https://pkg.kali.org/pkg/theharvester> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

````text
Usage Example
Search from email addresses from a domain (-d kali.org), limiting the results to 500 (-l 500), using DuckDuckGo (-b duckduckgo):
root@kali:~# theHarvester -d kali.org -l 500 -b duckduckgo
*******************************************************************
*  _   _                                            _             *
* | |_| |__   ___    /\  /\__ _ _ ____   _____  ___| |_ ___ _ __  *
* | __|  _ \ / _ \  / /_/ / _` | '__\ \ / / _ \/ __| __/ _ \ '__| *
* | |_| | | |  __/ / __  / (_| | |   \ V /  __/\__ \ ||  __/ |    *
*  \__|_| |_|\___| \/ /_/ \__,_|_|    \_/ \___||___/\__\___|_|    *
*                                                                 *
* theHarvester 4.4.3                                              *
* Coded by Christian Martorella                                   *
* Edge-Security Research                                          *
* cmartorella@edge-security.com                                   *
*                                                                 *
*******************************************************************

[*] Target: kali.org

[*] Searching Duckduckgo.

[*] No IPs found.

[*] No emails found.

[*] Hosts found: 14
---------------------
[...]

```console
````

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `theHarvester`

官方给出的调用示例：`theHarvester -d kali.org -l 500 -b duckduckgo`

````text
root@kali:~# theHarvester -d kali.org -l 500 -b duckduckgo
*******************************************************************
*  _   _                                            _             *
* | |_| |__   ___    /\  /\__ _ _ ____   _____  ___| |_ ___ _ __  *
* | __|  _ \ / _ \  / /_/ / _` | '__\ \ / / _ \/ __| __/ _ \ '__| *
* | |_| | | |  __/ / __  / (_| | |   \ V /  __/\__ \ ||  __/ |    *
*  \__|_| |_|\___| \/ /_/ \__,_|_|    \_/ \___||___/\__\___|_|    *
*                                                                 *
* theHarvester 4.4.3                                              *
* Coded by Christian Martorella                                   *
* Edge-Security Research                                          *
*
[email protected]
                                   *
*                                                                 *
*******************************************************************
[*] Target: kali.org
[*] Searching Duckduckgo.
[*] No IPs found.
[*] No emails found.
[*] Hosts found: 14
---------------------
[...]
```console
````

### `restfulHarvest`

官方给出的调用示例：`restfulHarvest -h`

```text
root@kali:~# restfulHarvest -h
usage: restfulHarvest [-h] [-H HOST] [-p PORT] [-l LOG_LEVEL] [-r]
                      [--rate-limit RATE_LIMIT]
options:
  -h, --help            show this help message and exit
  -H, --host HOST       IP address to listen on default is 127.0.0.1
  -p, --port PORT       Port to bind the web server to, default is 5000
  -l, --log-level LOG_LEVEL
                        Set logging level, default is info but
                        [critical|error|warning|info|debug|trace] can be set
  -r, --reload          Enable automatic reload used during development of the
                        api
  --rate-limit RATE_LIMIT
                        Set API rate limit (e.g., "10/minute", "100/hour"),
                        default is 5/minute
theHarvester
```

### `theHarvester（示例）`

官方给出的调用示例：`theHarvester -h`

```text
root@kali:~# theHarvester -h
Read proxies.yaml from /etc/theHarvester/proxies.yaml
*******************************************************************
*  _   _                                            _             *
* | |_| |__   ___    /\  /\__ _ _ ____   _____  ___| |_ ___ _ __  *
* | __|  _ \ / _ \  / /_/ / _` | '__\ \ / / _ \/ __| __/ _ \ '__| *
* | |_| | | |  __/ / __  / (_| | |   \ V /  __/\__ \ ||  __/ |    *
*  \__|_| |_|\___| \/ /_/ \__,_|_|    \_/ \___||___/\__\___|_|    *
*                                                                 *
* theHarvester 4.11.1                                             *
* Coded by Christian Martorella                                   *
* Edge-Security Research                                          *
*
[email protected]
                                   *
*                                                                 *
*******************************************************************
usage: theHarvester [-h] -d DOMAIN [-l LIMIT] [-S START] [-p] [-s]
                    [--screenshot SCREENSHOT] [-e DNS_SERVER] [-t]
                    [-r [DNS_RESOLVE]] [-n] [-c] [-f FILENAME] [-w WORDLIST]
                    [-a] [-q] [-b SOURCE]
theHarvester is used to gather open source intelligence (OSINT) on a company
or domain.
options:
  -h, --help            show this help message and exit
  -d, --domain DOMAIN   Company name or domain to search.
  -l, --limit LIMIT     Limit the number of search results, default=500.
  -S, --start START     Start with result number X, default=0.
  -p, --proxies         Use proxies for requests, enter proxies in
                        proxies.yaml.
  -s, --shodan          Use Shodan to query discovered hosts.
  --screenshot SCREENSHOT
                        Take screenshots of resolved domains specify output
                        directory: --screenshot output_directory
  -e, --dns-server DNS_SERVER
                        DNS server to use for lookup.
  -t, --take-over       Check for takeovers.
  -r, --dns-resolve [DNS_RESOLVE]
                        Perform DNS resolution on subdomains with a resolver
                        list or passed in resolvers, default False.
  -n, --dns-lookup      Enable DNS server lookup, default False.
  -c, --dns-brute       Perform a DNS brute force on the domain.
  -f, --filename FILENAME
                        Save the results to an XML and JSON file.
  -w, --wordlist WORDLIST
                        Specify a wordlist for API endpoint scanning.
  -a, --api-scan        Scan for API endpoints.
  -q, --quiet           Suppress missing API key warnings and reading the api-
                        keys file.
  -b, --source SOURCE   baidu, bevigil, bitbucket, brave, bufferoverun,
                        builtwith, censys, certspotter, chaos, commoncrawl,
                        criminalip, crtsh, dehashed, dnsdumpster, duckduckgo,
                        dymo, fofa, fullhunt, github-code, gitlab,
                        hackertarget, haveibeenpwned, hudsonrock, hunter,
                        hunterhow, intelx, leakix, leaklookup, mojeek, netlas,
                        onyphe, otx, pentesttools, projectdiscovery, rapiddns,
                        robtex, rocketreach, securityscorecard,
                        securityTrails, sherlockeye, shodan, shodanInternetDB,
                        subdomaincenter, subdomainfinderc99, thc, threatcrowd,
                        tomba, urlscan, venacus, virustotal, waybackarchive,
                        whoisxml, windvane, yahoo, zoomeye
```

### `theharvester`

官方给出的调用示例：`theharvester -h`

```text
root@kali:~# theharvester -h
┏━(Message from Kali developers)
┃
┃ The command theharvester is deprecated. Please use theHarvester instead.
┃
┗━
Learn more with
OffSec
Want to learn more about theharvester? get access to in-depth training and hands-on labs:
PEN-200: 12.1.1. Client-side Attacks: Information Gathering
MITRE ATT&CK - Resource Development (TA0042): 2.1.2. Client-side Attacks: Client Fingerprinting
SEC-100: 19.1.2. Information Gathering and Enumeration: Client Fingerprinting
PEN-200 course
SEC-100 course
Updated on: 2026-Aug-25
 Edit this page
tftp-hpa
tlssled
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install theharvester`，再执行 `theharvester --version` 2>/dev/null || `theharvester -V`
- [ ] **2.** **读官方帮助** —— `theharvester -h`，需要细节时 `man theharvester`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `theharvester -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/theharvester/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[theharvester](../../tools/tutorials/01-信息搜集/theharvester.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/theharvester/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/theharvester/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
