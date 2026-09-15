# pocsuite3

> Open-sourced remote vulnerability testing framework Pocsuite3 is an open-sourced remote vulnerability testing and proof-of-concept development framework developed by the Knownsec 404 Team. It comes with a powerful proof-of-concept engine, …

> **功能分类**：通用工具 ｜ **Kali 包**：`pocsuite3` ｜ **官方文档**：<https://www.kali.org/tools/pocsuite3/>

## 1. 安装

```bash
sudo apt update
sudo apt install pocsuite3
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.1.0 |
| 架构 | all |
| 可执行命令 | `pocsuite3`、`poc-console`、`pocsuite` |
| 依赖 | `binutils`、`nasm`、`python3`、`python3-chardet`、`python3-colorama`、`python3-colorlog`、`python3-dacite`、`python3-docker`、`python3-fake-factory`、`python3-lxml`、`python3-openssl`、`python3-packaging` 等 |
| 安装体积 | 943 KB |
| 官网 | <https://pocsuite.org> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/pocsuite3> |
| 包追踪 | <https://pkg.kali.org/pkg/pocsuite3> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
pocsuite3 -h          # 查看用法
man pocsuite3         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man poc-console`

```text
root@kali:~# man poc-console
POC-CONSOLE(1)              General Commands Manual              POC-CONSOLE(1)
NAME
     poc-console - console mode of pocsuite3.
Legal Disclaimer
     poc-console is part of pocsuite3. Usage of pocsuite3 for attacking targets
     without  prior mutual consent is illegal.  pocsuite3 is for security test-
     ing purposes only.
SYNOPSIS
     poc-console
DESCRIPTION
     poc-console is the console mode  of  pocsuite3.   pocsuite3  is  an  open-
     sourced  remote  vulnerability  testing  and  proof-of-concept development
     framework developed by the Knownsec 404 Team. It  comes  with  a  powerful
     proof-of-concept  engine,  many nice features for the ultimate penetration
     testers and security researchers.
OPTIONS
     poc-console do not have command line options. To see a list  of  available
     commands, enter help at the console prompt.
SEE ALSO
     The full documentation for pocsuite3 is maintained at:
     https://pocsuite.org
VERSION
     This manual page documents pocsuite3 version 2.0.5
AUTHOR
     (c) 2014-present by Knownsec 404 Team
     <
[email protected]
>
     This program is free software; you may redistribute and/or modify it under
     the terms of the GNU General Public License as published by the Free Soft-
     ware  Foundation;  Version  2  with  the clarifications and exceptions de-
     scribed below. This guarantees your right to use, modify, and redistribute
     this software under certain conditions. If you  wish  to  embed  pocsuite3
     technology  into  proprietary software, we sell alternative licenses (con-
     tact
[email protected]
).
     Manual page started by 13ph03nix <
[email protected]
>
Manual page for poc-console         Nov 2022                     POC-CONSOLE(1)
```

### `pocsuite`

> 官方示例调用：`pocsuite -h`

```text
root@kali:~# pocsuite -h
,------.                        ,--. ,--.       ,----.   {2.1.0-c3c615a}
|  .--. ',---. ,---.,---.,--.,--`--,-'  '-.,---.'.-.  |
|  '--' | .-. | .--(  .-'|  ||  ,--'-.  .-| .-. : .' <
|  | --'' '-' \ `--.-'  `'  ''  |  | |  | \   --/'-'  |
`--'     `---' `---`----' `----'`--' `--'  `----`----'   https://pocsuite.org
usage: pocsuite [options]
options:
  -h, --help            show this help message and exit
  --version             Show program's version number and exit
  --update              Update Pocsuite3
  -n, --new             Create a PoC template
  -v {0,1,2,3,4,5,6}    Verbosity level: 0-6 (default 1)
Target:
  At least one of these options has to be provided to define the target(s)
  -u, --url URL [URL ...]
                        Target URL/CIDR (e.g.
                        "http://www.site.com/vuln.php?id=1")
  -f, --file URL_FILE   Scan multiple targets given in a textual file (one per
                        line)
  -p, --ports PORTS     add additional port to each target ([proto:]port, e.g.
                        8080,https:10000)
  -s                    Skip target's port, only use additional port
  -r POC [POC ...]      Load PoC file from local or remote from seebug website
  -k POC_KEYWORD        Filter PoC by keyword, e.g. ecshop
  -c CONFIGFILE         Load options from a configuration INI file
  -l                    Show all PoC file from local
Mode:
  Pocsuite running mode options
  --verify              Run poc with verify mode
  --attack              Run poc with attack mode
  --shell               Run poc with shell mode
Request:
  Network request options
  --cookie COOKIE       HTTP Cookie header value
  --host HOST           HTTP Host header value
  --referer REFERER     HTTP Referer header value
  --user-agent AGENT    HTTP User-Agent header value (default random)
  --proxy PROXY         Use a proxy to connect to the target URL
                        (protocol://host:port)
  --proxy-cred PROXY_CRED
                        Proxy authentication credentials (name:password)
  --timeout TIMEOUT     Seconds to wait before timeout connection (default 10)
  --retry RETRY         Time out retrials times (default 0)
  --delay DELAY         Delay between two request of one thread
  --headers HEADERS     Extra headers (e.g. "key1: value1\nkey2: value2")
  --http-debug HTTP_DEBUG
                        HTTP debug level (default 0)
  --session-reuse       Enable requests session reuse
  --session-reuse-num REQUESTS_SESSION_REUSE_NUM
                        Requests session reuse number
Account:
  Account options
  --ceye-token CEYE_TOKEN
                        CEye token
  --oob-server OOB_SERVER
                        Interactsh server to use (default "interact.sh")
  --oob-token OOB_TOKEN
                        Authentication token to connect protected interactsh
                        server
  --seebug-token SEEBUG_TOKEN
                        Seebug token
  --zoomeye-token ZOOMEYE_TOKEN
                        ZoomEye token
  --shodan-token SHODAN_TOKEN
                        Shodan token
  --fofa-user FOFA_USER
                        Fofa user
  --fofa-token FOFA_TOKEN
                        Fofa token
  --quake-token QUAKE_TOKEN
                        Quake token
  --hunter-token HUNTER_TOKEN
                        Hunter token
  --censys-uid CENSYS_UID
                        Censys uid
  --censys-secret CENSYS_SECRET
                        Censys secret
Modules:
  Modules options
  --dork DORK           Zoomeye dork used for search
  --dork-zoomeye DORK_ZOOMEYE
                        Zoomeye dork used for search
  --dork-shodan DORK_SHODAN
                        Shodan dork used for search
  --dork-fofa DORK_FOFA
                        Fofa dork used for search
  --dork-quake DORK_QUAKE
                        Quake dork used for search
  --dork-hunter DORK_HUNTER
                        Hunter dork used for search
  --dork-censys DORK_CENSYS
                        Censys dork used for search
  --max-page MAX_PAGE   Max page used in search API
  --page-size PAGE_SIZE
                        Page size used in search API
  --search-type SEARCH_TYPE
                        search type used in search API, v4,v6 and web
  --vul-keyword VUL_KEYWORD
                        Seebug keyword used for search
  --ssv-id SSVID        Seebug SSVID number for target PoC
  --lhost CONNECT_BACK_HOST
                        Connect back host for target PoC in shell mode
  --lport CONNECT_BACK_PORT
                        Connect back port for target PoC in shell mode
  --tls                 Enable TLS listener in shell mode
  --comparison          Compare popular web search engines
  --dork-b64            Whether dork is in base64 format
Optimization:
  Optimization options
  -o, --output OUTPUT_PATH
                        Output file to write (JSON Lines format)
  --plugins PLUGINS     Load plugins to execute
  --pocs-path POCS_PATH
                        User defined poc scripts path
  --threads THREADS     Max number of concurrent network requests (default
                        150)
  --batch BATCH         Automatically choose defaut choice without asking
  --requires            Check install_requires
  --quiet               Activate quiet mode, working without logger
  --ppt                 Hiden sensitive information when published to the
                        network
  --pcap                use scapy capture flow
  --rule                export suricata rules, default export reqeust and
                        response
  --rule-req            only export request rule
  --rule-filename RULE_FILENAME
                        Specify the name of the export rule file
  --no-check            Disable URL protocol correction and honeypot check
Docker Environment:
  Docker Environment options
  --docker-start        Run the docker for PoC
  --docker-port DOCKER_PORT
                        Publish a container's port(s) to the host
  --docker-volume DOCKER_VOLUME
                        Bind mount a volume
  --docker-env DOCKER_ENV
                        Set environment variables
  --docker-only         Only run docker environment
Web Hook:
  Web Hook Options
  --dingtalk-token DINGTALK_TOKEN
                        Dingtalk access token
  --dingtalk-secret DINGTALK_SECRET
                        Dingtalk secret
  --wx-work-key WX_WORK_KEY
                        Weixin Work key
Poc options:
  definition options for PoC
  --options             Show all definition options
[*] shutting down at 07:28:25
Updated on: 2026-Aug-25
 Edit this page
php-defaults
powershell-empire
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install pocsuite3`，再执行 `pocsuite3 --version` 2>/dev/null || `pocsuite3 -V`
- [ ] **2.** **读官方帮助** —— `pocsuite3 -h`，需要细节时 `man pocsuite3`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `pocsuite3 -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/pocsuite3/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/pocsuite3/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/pocsuite3/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
