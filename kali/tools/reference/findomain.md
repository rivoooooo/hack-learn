# findomain

> Fastest and most complete solution for domain recognition Findomain is fastest and most complete solution for domain recognition. It supports screenshoting, port scanning, HTTP checks, data imports from other tools, subdomain monitoring, a…

> **功能分类**：通用工具 ｜ **Kali 包**：`findomain` ｜ **官方文档**：<https://www.kali.org/tools/findomain/>

## 1. 安装

```bash
sudo apt update
sudo apt install findomain
```

| 项目 | 内容 |
|------|------|
| 版本 | 10.0.1 |
| 架构 | amd64 |
| 可执行命令 | `findomain` |
| 依赖 | `chromium`、`libc6`、`libgcc-s1`、`postgresql` |
| 安装体积 | 18.61 MB |
| 官网 | <https://github.com/Findomain/Findomain> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/findomain> |
| 包追踪 | <https://pkg.kali.org/pkg/findomain> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
findomain -h          # 查看用法
man findomain         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `findomain`

官方给出的调用示例：`findomain -h`

```text
root@kali:~# findomain -h
The fastest and cross-platform subdomain enumerator, do not waste your time.
Usage: findomain [OPTIONS]
Options:
  -t, --target <TARGET>
          Target host
  -r, --resolved
          Show/write only resolved subdomains
  -i, --ip
          Show/write the ip address of resolved subdomains
  -f, --file <FILES>
          Use a list of subdomains writen in a file as input
  -o, --output
          Write to an automatically generated output file. The name of the output file is generated using the format: target.txt. If you want a custom output file name, use the -u/--unique-output option
  -u, --unique-output <UNIQUE_OUTPUT>
          Write all the results for a target or a list of targets to a specified filename
  -m, --monitoring-flag
          Activate Findomain monitoring mode
      --postgres-user <POSTGRES_USER>
          Postgresql username
      --postgres-password <POSTGRES_PASSWORD>
          Postgresql password
      --postgres-host <POSTGRES_HOST>
          Postgresql host
      --postgres-port <POSTGRES_PORT>
          Postgresql port
      --postgres-database <POSTGRES_DATABASE>
          Postgresql database
  -q, --quiet
          Remove informative messages but show fatal errors or subdomains not found message
      --query-database
          Query the findomain database to search subdomains that have already been discovered
      --import-subdomains <IMPORT_SUBDOMAINS>
          Import subdomains from one or multiple files. Subdomains need to be one per line in the file to import
      --enable-dot
          Enable DNS over TLS for resolving subdomains IPs
      --ipv6-only
          Perform a IPv6 lookup only
      --threads <THREADS>
          Number of threads to use for lightweight tasks such as IP discovery and HTTP checks. Deprecated option, use --lighweight-threads instead. This would be removed in the future
      --lightweight-threads <LIGHTWEIGHT_THREADS>
          Number of threads to use for lightweight tasks such as IP discovery and HTTP checks. Default is 50
      --screenshots-threads <SCREENSHOTS_THREADS>
          Number of threads to use to use for taking screenshots. Default is 10
      --parallel-ip-ports-scan <PARALLEL_IP_PORTS_SCAN>
          Number of IPs that will be port-scanned at the same time. Default is 10
      --tcp-connect-threads <TCP_CONNECT_THREADS>
          Number of threads to use for TCP connections - It's the equivalent of Nmap's --min-rate. Default is 500
      --resolvers <CUSTOM_RESOLVERS>
          Path to a file (or files) containing a list of DNS IP address. If no specified then Google, Cloudflare and Quad9 DNS servers are used
      --aempty
          Send alert to webhooks still when no new subdomains have been found
  -x, --as-resolver
          Use Findomain as resolver for a list of domains in a file
  -w, --wordlist <WORDLISTS>
          Wordlist file to use in the bruteforce process. Using it option automatically enables bruteforce mode
      --no-wildcards
          Disable wilcard detection when resolving subdomains
      --filter <STRING_FILTER>
          Filter subdomains containing specifics strings
      --exclude <STRING_EXCLUDE>
          Exclude subdomains containing specifics strings
      --exclude-sources <EXCLUDE_SOURCES>
          Exclude sources from searching subdomains in [possible values: certspotter, crtsh, sublist3r, facebook, spyse, threatcrowd, virustotalapikey, anubis, urlscan, securitytrails, threatminer, c99, bufferover_free, bufferover_paid]
      --http-status
          Check the HTTP status of subdomains
  -c, --config <CONFIG_FILE>
          Use a configuration file. The default configuration file is findomain and the format can be toml, json, hjson, ini or yml
      --rate-limit <RATE_LIMIT>
          Set the rate limit in seconds for each target during enumeration
      --pscan
          Enable port scanner
      --iport <INITIAL_PORT>
          Initial port to scan. Default 0
      --lport <LAST_PORT>
          Last port to scan. Default 1000
  -v, --verbose
          Enable verbose mode (useful to debug problems)
      --mtimeout
          Allow Findomain to insert data in the database when the webhook returns a timeout error
      --no-monitor
          Disable monitoring mode while saving data to database
  -s, --screenshots <SCREENSHOTS_PATH>
          Path to save the screenshots of the HTTP(S) website for subdomains with active ones
      --sandbox
          Enable Chrome/Chromium sandbox. It is disabled by default because a big number of users run the tool using the root user by default. Make sure you are not running the program as root user before using this option
  -j, --jobname <JOBNAME>
          Use an database identifier for jobs. It is useful when you want to relate different targets into a same job name. To extract the data by job name identifier, use the query-jobname option
      --query-jobname
          Extract all the subdomains from the database where the job name is the specified using the jobname option
      --http-timeout <HTTP_TIMEOUT>
          Value in seconds for the HTTP Status check of subdomains. Default 5
      --tcp-connect-timeout <TCP_CONNECT_TIMEOUT>
          Value in milliseconds to wait for the TCP connection (ip:port) in the ports scanning function. Default 2000
      --stdin
          Read from stdin instead of files or aguments
      --ua <USER_AGENTS_FILE>
          Path to file containing user agents strings
      --randomize
          Enable randomization when reading targets from files
      --no-resolve
          Disable pre-screenshotting jobs (http check and ip discover) when used as resolver to take screenshots
      --external-subdomains
          Get external subdomains with amass and subfinder
      --validate
          Validate all the subdomains from the specified file
      --resolver-timeout <RESOLVER_TIMEOUT>
          Timeout in seconds for the resolver. Default 1
      --http-retries <HTTP_RETRIES>
          Number of retries for the HTTP Status check of subdomains. Default 1
      --double-dns-check
          Enable double DNS check. This means that the subdomains that report an IP address are checked again using a list of trustable resolvers to avoid false-positives. Only applies when using custom resolvers
  -n, --no-discover
          Prevent findomain from searching subdomains itself. Useful when you are importing subdomains from other tools
      --max-http-redirects <MAX_HTTP_REDIRECTS>
          Maximum number of HTTP redirects to follow. Default 0
      --reset-database
          Reset the database. It will delete all the data from the database
  -h, --help
          Print help
  -V, --version
          Print version
Updated on: 2025-Dec-09
 Edit this page
fiked
firewalk
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install findomain`，再执行 `findomain --version` 2>/dev/null || `findomain -V`
- [ ] **2.** **读官方帮助** —— `findomain -h`，需要细节时 `man findomain`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: findomain [OPTIONS]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/findomain/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/findomain/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/findomain/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
