# changeme

> Default credential scanner This package contains a default credential scanner. Commercial vulnerability scanners miss common default credentials. Getting default credentials added to commercial scanners is often difficult and slow. changem…

> **功能分类**：通用工具 ｜ **Kali 包**：`changeme` ｜ **官方文档**：<https://www.kali.org/tools/changeme/>

## 1. 安装

```bash
sudo apt update
sudo apt install changeme
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.2.3 |
| 架构 | all |
| 可执行命令 | `changeme` |
| 依赖 | `python3`、`python3-cerberus`、`python3-jinja2`、`python3-libnmap`、`python3-logutils`、`python3-lxml`、`python3-memcache`、`python3-netaddr`、`python3-paramiko`、`python3-psycopg2`、`python3-pymongo`、`python3-pyodbc` 等 |
| 安装体积 | 314 KB |
| 官网 | <https://github.com/ztgrace/changeme> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/changeme> |
| 包追踪 | <https://pkg.kali.org/pkg/changeme> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
changeme -h          # 查看用法
man changeme         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `changeme`

官方给出的调用示例：`changeme -h`

```text
root@kali:~# changeme -h
 #####################################################
#       _                                             #
#   ___| |__   __ _ _ __   __ _  ___ _ __ ___   ___   #
#  / __| '_ \ / _` | '_ \ / _` |/ _ \ '_ ` _ \ / _ \\  #
# | (__| | | | (_| | | | | (_| |  __/ | | | | |  __/  #
#  \___|_| |_|\__,_|_| |_|\__, |\___|_| |_| |_|\___|  #
#                         |___/                       #
#  v1.2.3                                             #
#  Default Credential Scanner by @ztgrace             #
 #####################################################
usage: changeme.py [-h] [--all] [--category CATEGORY] [--contributors]
                   [--debug] [--delay DELAY] [--dump] [--dryrun]
                   [--fingerprint] [--fresh] [--log LOG] [--mkcred]
                   [--name NAME] [--noversion] [--proxy PROXY]
                   [--output OUTPUT] [--oa] [--protocols PROTOCOLS]
                   [--portoverride] [--redishost REDISHOST]
                   [--redisport REDISPORT] [--resume]
                   [--shodan_query SHODAN_QUERY] [--shodan_key SHODAN_KEY]
                   [--ssl] [--threads THREADS] [--timeout TIMEOUT]
                   [--useragent USERAGENT] [--validate] [--verbose]
                   target
Default credential scanner v1.2.3
positional arguments:
  target                Target to scan. Can be IP, subnet, hostname, nmap xml
                        file, text file or proto://host:port
options:
  -h, --help            show this help message and exit
  --all, -a             Scan for all protocols
  --category, -c CATEGORY
                        Category of default creds to scan for
  --contributors        Display cred file contributors
  --debug, -d           Debug output
  --delay, -dl DELAY    Specify a delay in milliseconds to avoid 429 status
                        codes default=500
  --dump                Print all of the loaded credentials
  --dryrun              Print urls to be scan, but don't scan them
  --fingerprint, -f     Fingerprint targets, but don't check creds
  --fresh               Flush any previous scans and start fresh
  --log, -l LOG         Write logs to logfile
  --mkcred              Make cred file
  --name, -n NAME       Narrow testing to the supplied credential name
  --noversion           Don't perform a version check
  --proxy, -p PROXY     HTTP(S) Proxy
  --output, -o OUTPUT   Name of result file. File extension determines type
                        (csv, html, json).
  --oa                  Output results files in csv, html and json formats
  --protocols PROTOCOLS
                        Comma separated list of protocols to test:
                        http,ssh,ssh_key. Defaults to http.
  --portoverride        Scan all protocols on all specified ports
  --redishost REDISHOST
                        Redis server
  --redisport REDISPORT
                        Redis server
  --resume, -r          Resume previous scan
  --shodan_query, -q SHODAN_QUERY
                        Shodan query
  --shodan_key, -k SHODAN_KEY
                        Shodan API key
  --ssl                 Force cred to SSL and fall back to non-SSL if an
                        SSLError occurs
  --threads, -t THREADS
                        Number of threads, default=10
  --timeout TIMEOUT     Timeout in seconds for a request, default=10
  --useragent, -ua USERAGENT
                        User agent string to use
  --validate            Validate creds files
  --verbose, -v         Verbose output
Updated on: 2025-Dec-09
 Edit this page
cewl
chirp
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install changeme`，再执行 `changeme --version` 2>/dev/null || `changeme -V`
- [ ] **2.** **读官方帮助** —— `changeme -h`，需要细节时 `man changeme`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `changeme -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/changeme/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/changeme/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/changeme/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
