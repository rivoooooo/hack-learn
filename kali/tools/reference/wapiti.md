# wapiti

> Web application vulnerability scanner Wapiti allows you to audit the security of your web applications. It performs “black-box” scans, i.e. it does not study the source code of the application but will scan the web pages of the deployed we…

> **功能分类**：信息搜集 ｜ **Kali 包**：`wapiti` ｜ **官方文档**：<https://www.kali.org/tools/wapiti/>

## 1. 安装

```bash
sudo apt update
sudo apt install wapiti
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.2.10 |
| 架构 | all |
| 可执行命令 | `wapiti`、`wapiti-getcookie` |
| 依赖 | `mitmproxy`、`python3`、`python3-aiosqlite`、`python3-browser-cookie3`、`python3-bs4`、`python3-dnspython`、`python3-httpcore`、`python3-httpx`、`python3-httpx-ntlm`、`python3-mako`、`python3-packaging`、`python3-playwright` 等 |
| 安装体积 | 3.26 MB |
| 官网 | <https://wapiti.sourceforge.net/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/wapiti> |
| 包追踪 | <https://pkg.kali.org/pkg/wapiti> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
wapiti -h          # 查看用法
man wapiti         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wapiti`

官方给出的调用示例：`wapiti -h`

```text
root@kali:~# wapiti -h
 ██╗    ██╗ █████╗ ██████╗ ██╗████████╗██╗██████╗
 ██║    ██║██╔══██╗██╔══██╗██║╚══██╔══╝██║╚════██╗
 ██║ █╗ ██║███████║██████╔╝██║   ██║   ██║ █████╔╝
 ██║███╗██║██╔══██║██╔═══╝ ██║   ██║   ██║ ╚═══██╗
 ╚███╔███╔╝██║  ██║██║     ██║   ██║   ██║██████╔╝
  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝   ╚═╝╚═════╝
usage: wapiti [-h] (-u URL | --list-modules | --update) [--swagger URI]
              [--data data] [--scope {url,page,folder,subdomain,domain,punk}]
              [-m MODULES_LIST] [-l LEVEL] [-p PROXY_URL] [--tor]
              [--mitm-port PORT] [--headless {no,hidden,visible}]
              [--wait TIME] [-a CREDENTIALS] [--auth-user USERNAME]
              [--auth-password PASSWORD] [--auth-method {basic,digest,ntlm}]
              [--form-cred CREDENTIALS] [--form-user USERNAME]
              [--form-password PASSWORD] [--form-url URL] [--form-data DATA]
              [--form-enctype DATA] [--form-script FILENAME] [-c COOKIE_FILE]
              [-sf SIDE_FILE] [-C COOKIE_VALUE] [--drop-set-cookie]
              [--skip-crawl] [--resume-crawl] [--flush-attacks]
              [--flush-session] [--store-session PATH] [--store-config PATH]
              [-s URL] [-x URL] [-r PARAMETER] [--skip PARAMETER] [-d DEPTH]
              [--max-links-per-page MAX] [--max-files-per-dir MAX]
              [--max-scan-time SECONDS] [--max-attack-time SECONDS]
              [--max-parameters MAX] [-S FORCE] [--tasks tasks]
              [--external-endpoint EXTERNAL_ENDPOINT_URL]
              [--internal-endpoint INTERNAL_ENDPOINT_URL]
              [--endpoint ENDPOINT_URL] [--dns-endpoint DNS_ENDPOINT_DOMAIN]
              [-t SECONDS] [-H HEADER] [-A AGENT] [--verify-ssl {0,1}]
              [--color] [-v LEVEL] [--log OUTPUT_PATH] [-f FORMAT]
              [-o OUTPUT_PATH] [-dr DETAILED_REPORT_LEVEL] [--no-bugreport]
              [--version] [--cms CMS_LIST] [--wapp-url WAPP_URL]
              [--wapp-dir WAPP_DIR]
Wapiti 3.2.10: Web application vulnerability scanner
options:
  -h, --help            show this help message and exit
  -u, --url URL         The base URL used to define the scan scope (default
                        scope is folder)
  --swagger URI         Swagger file URI (path or URL) to target API endpoints
  --data data           Urlencoded data to send with the base URL if it is a
                        POST request
  --scope {url,page,folder,subdomain,domain,punk}
                        Set scan scope
  -m, --module MODULES_LIST
                        List of modules to load
  --list-modules        List Wapiti attack modules and exit
  -l, --level LEVEL     Set attack level
  -p, --proxy PROXY_URL
                        Set the HTTP(S) proxy to use. Supported: http(s) and
                        socks proxies
  --tor                 Use Tor listener (127.0.0.1:9050)
  --mitm-port PORT      Instead of crawling, launch an intercepting proxy on
                        the given port
  --headless {no,hidden,visible}
                        Use a Firefox headless crawler for browsing (slower)
  --wait TIME           Wait the specified amount of seconds before analyzing
                        a webpage (headless mode only)
  -a, --auth-cred CREDENTIALS
                        (DEPRECATED) Set HTTP authentication credentials
  --auth-user USERNAME  Set HTTP authentication username credentials
  --auth-password PASSWORD
                        Set HTTP authentication password credentials
  --auth-method {basic,digest,ntlm}
                        Set the HTTP authentication method to use
  --form-cred CREDENTIALS
                        (DEPRECATED) Set login form credentials
  --form-user USERNAME  Set login form credentials
  --form-password PASSWORD
                        Set password form credentials
  --form-url URL        Set login form URL
  --form-data DATA      Set login form POST data
  --form-enctype DATA   Set enctype to use to POST form data to form URL
  --form-script FILENAME
                        Use a custom Python authentication plugin
  -c, --cookie COOKIE_FILE
                        Set a JSON cookie file to use. You can also pass
                        'firefox' or 'chrome' to load cookies from your
                        browser.
  -sf, --side-file SIDE_FILE
                        Use a .side file generated using Selenium IDE to
                        perform an authenticated scan.
  -C, --cookie-value COOKIE_VALUE
                        Set a cookie to use for every request for
                        authenticated scan. You can put multiple cookies
                        separated by semicolons as a value
  --drop-set-cookie     Ignore Set-Cookie header from HTTP responses
  --skip-crawl          Don't resume the scanning process, attack URLs scanned
                        during a previous session
  --resume-crawl        Resume the scanning process (if stopped) even if some
                        attacks were previously performed
  --flush-attacks       Flush attack history and vulnerabilities for the
                        current session
  --flush-session       Flush everything that was previously found for this
                        target (crawled URLs, vulns, etc)
  --store-session PATH  Directory where to store attack history and session
                        data.
  --store-config PATH   Directory where to store configuration databases.
  -s, --start URL       Adds a url to start scan with
  -x, --exclude URL     Adds a url to exclude from the scan
  -r, --remove PARAMETER
                        Remove this parameter from urls
  --skip PARAMETER      Skip attacking given parameter(s)
  -d, --depth DEPTH     Set how deep the scanner should explore the website
  --max-links-per-page MAX
                        Set how many (in-scope) links the scanner should
                        extract for each page
  --max-files-per-dir MAX
                        Set how many pages the scanner should explore per
                        directory
  --max-scan-time SECONDS
                        Set how many seconds you want the scan to last (floats
                        accepted)
  --max-attack-time SECONDS
                        Set how many seconds you want each attack module to
                        last (floats accepted)
  --max-parameters MAX  URLs and forms having more than MAX input parameters
                        will be erased before attack.
  -S, --scan-force FORCE
                        Easy way to reduce the number of scanned and attacked
                        URLs. Possible values: paranoid, sneaky, polite,
                        normal, aggressive, insane
  --tasks tasks         Number of concurrent tasks to use for the exploration
                        (crawling) of the target.
  --external-endpoint EXTERNAL_ENDPOINT_URL
                        Url serving as endpoint for target
  --internal-endpoint INTERNAL_ENDPOINT_URL
                        Url serving as endpoint for attacker
  --endpoint ENDPOINT_URL
                        Url serving as endpoint for both attacker and target
  --dns-endpoint DNS_ENDPOINT_DOMAIN
                        Domain serving as DNS endpoint for Log4Shell attack
  -t, --timeout SECONDS
                        Set timeout for requests
  -H, --header HEADER   Set a custom header to use for every requests
  -A, --user-agent AGENT
                        Set a custom user-agent to use for every requests
  --verify-ssl {0,1}    Set SSL check (default is no check)
  --color               Colorize output
  -v, --verbose LEVEL   Set verbosity level (0: quiet, 1: normal, 2: verbose)
  --log OUTPUT_PATH     Output log file
  -f, --format FORMAT   Set output format. Supported: csv, html, json, md,
                        txt, xml. Default is html.
  -o, --output OUTPUT_PATH
                        Output file or folder
  -dr, --detailed-report DETAILED_REPORT_LEVEL
                        level 1 : include only the HTTP requests, level 2 :
                        include HTTP requests and responses
  --no-bugreport        Don't send automatic bug report when an attack module
                        fails
  --update              Update Wapiti attack modules and exit
  --version             Show program's version number and exit
  --cms CMS_LIST        Choose the CMS to scan. Possible choices : drupal,
                        joomla, prestashop, spip, wp
  --wapp-url WAPP_URL   Provide a custom URL for updating Wappalyzer Database
  --wapp-dir WAPP_DIR   Provide a custom directory path for updating
                        Wappalyzer Database
```

### `wapiti-getcookie`

官方给出的调用示例：`wapiti-getcookie -h`

```text
root@kali:~# wapiti-getcookie -h
usage: wapiti-getcookie [-h] -u URL -c COOKIE [-p PROXY] [--tor]
                        [-a CREDENTIALS] [--auth-user USERNAME]
                        [--auth-password PASSWORD]
                        [--auth-method {basic,digest,ntlm}] [--form-data DATA]
                        [--form-enctype DATA] [--headless {no,hidden,visible}]
                        [-A AGENT] [-H HEADER]
Wapiti-getcookie: An utility to grab cookies from a webpage
options:
  -h, --help            show this help message and exit
  -u, --url URL         First page to fetch for cookies
  -c, --cookie COOKIE   Cookie file in Wapiti JSON format where cookies will
                        be stored
  -p, --proxy PROXY     Address of the proxy server to use
  --tor                 Use Tor listener (127.0.0.1:9050)
  -a, --auth-cred CREDENTIALS
                        (DEPRECATED) Set HTTP authentication credentials
  --auth-user USERNAME  Set HTTP authentication credentials
  --auth-password PASSWORD
                        Set HTTP authentication credentials
  --auth-method {basic,digest,ntlm}
                        Set the authentication type to use
  --form-data DATA      Set login form POST data
  --form-enctype DATA   Set enctype to use to POST form data to form URL
  --headless {no,hidden,visible}
                        Use a Firefox headless crawler for browsing (slower)
  -A, --user-agent AGENT
                        Set a custom user-agent to use for every requests
  -H, --header HEADER   Set a custom header to use for every requests
Updated on: 2026-Aug-25
 Edit this page
vpnc
waybackpy
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install wapiti`，再执行 `wapiti --version` 2>/dev/null || `wapiti -V`
- [ ] **2.** **读官方帮助** —— `wapiti -h`，需要细节时 `man wapiti`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `wapiti -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wapiti/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wapiti/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wapiti/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
