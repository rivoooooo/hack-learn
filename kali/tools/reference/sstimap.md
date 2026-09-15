# sstimap

> Automatic SSTI detection tool with interactive interface SSTImap is a penetration testing software that can check websites for Code Injection and Server-Side Template Injection vulnerabilities and exploit them, giving access to the operati…

> **功能分类**：通用工具 ｜ **Kali 包**：`sstimap` ｜ **官方文档**：<https://www.kali.org/tools/sstimap/>

## 1. 安装

```bash
sudo apt update
sudo apt install sstimap
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.4 |
| 架构 | all |
| 可执行命令 | `sstimap` |
| 依赖 | `python3`、`python3-html5lib`、`python3-mechanize`、`python3-requests`、`python3-urllib3` |
| 安装体积 | 454 KB |
| 官网 | <https://github.com/vladko312/SSTImap> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sstimap> |
| 包追踪 | <https://pkg.kali.org/pkg/sstimap> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sstimap -h          # 查看用法
man sstimap         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sstimap`

> 官方示例调用：`sstimap -h`

```text
root@kali:~# sstimap -h
usage: sstimap.py [-h] [-V] [--module MODULE] [--config CONFIG] [--no-color]
                  [-u URL] [-i] [--load-urls LOAD_URLS]
                  [--load-forms LOAD_FORMS] [--load-vuln LOAD_VULN]
                  [--save-vuln SAVE_VULN] [-M MARKER] [-P INJECTION_POINTS]
                  [-d DATA] [--data-type DATA_TYPE] [--data-params KEY=VALUE]
                  [-H HEADER] [-C COOKIE] [-m METHOD] [-a USER_AGENT] [-A]
                  [--delay DELAY] [-p PROXY] [--verify-ssl] [--log-response]
                  [-c CRAWL_DEPTH] [-f] [--empty-forms]
                  [--crawl-exclude CRAWL_EXCLUDE]
                  [--crawl-domains CRAWL_DOMAINS] [--save-urls SAVE_URLS]
                  [--save-forms SAVE_FORMS] [-l LEVEL] [-L LEVEL CLEVEL]
                  [-e ENGINE] [-r TECHNIQUE] [--bool-ok BOOLEAN_REGEX_OK]
                  [--bool-err BOOLEAN_REGEX_ERR] [--bool-match BOOLEAN_MATCH]
                  [--bool-match-min BOOLEAN_MATCH_MIN]
                  [--bool-fuzzy STABLE ERROR] [--bool-samples COUNT MIN MAX]
                  [--blind-delay TIME_BASED_BLIND_DELAY]
                  [--verify-blind-delay TIME_BASED_VERIFY_BLIND_DELAY]
                  [--legacy] [--generic] [--run] [-t] [-T TPL_CODE] [-x]
                  [-X EVAL_CODE] [-s] [-S OS_CMD] [-B PORT] [-R HOST PORT]
                  [--remote-shell REMOTE_SHELL] [-F] [-U LOCAL REMOTE]
                  [-D REMOTE LOCAL]
SSTImap is an automatic SSTI detection and exploitation tool with
predetermined and interactive modes.
options:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  --module MODULE       Provide information about the module ('list' to show
                        all modules)
  --config CONFIG       Use custom config file or directory
  --no-color            Disable color in output
target:
  At least one of these options has to be provided to define target(s)
  -u, --url URL         Target URL (e.g. 'https://example.com/?name=test')
  -i, --interactive     Run SSTImap in interactive mode
  --load-urls LOAD_URLS
                        File or directory to load URLs from (use '-' for
                        STDIN)
  --load-forms LOAD_FORMS
                        File or directory to load forms from (use '-' for
                        STDIN)
  --load-vuln LOAD_VULN
                        File or directory to load vulnerability from (use '-'
                        for STDIN)
  --save-vuln SAVE_VULN
                        File or directory to save detected vulnerability to
request:
  These options can specify how to connect to the target URL and add
  possible attack vectors
  -M, --marker MARKER   Use string as injection marker (default '*')
  -P, --injection-points INJECTION_POINTS
                        Injection points to test without markers: Q(uery)
                        B(ody) H(eaders) C(ookies). Default: QBHC
  -d, --data DATA       Request body data param to send (e.g. 'param=value')
                        [Stackable]
  --data-type DATA_TYPE
                        Request body data type (default 'auto')
  --data-params KEY=VALUE
                        Module params for plugins and request body data types
  -H, --header HEADER   Header to send (e.g. 'Header: Value') [Stackable]
  -C, --cookie COOKIE   Cookie to send (e.g. 'Field=Value') [Stackable]
  -m, --method METHOD   HTTP method to use (default 'GET')
  -a, --user-agent USER_AGENT
                        User-Agent header value to use
  -A, --random-user-agent
                        Random User-Agent header value from a list of desktop
                        browsers on every request
  --delay DELAY         Delay between requests (Default/0: no delay)
  -p, --proxy PROXY     Use a proxy to connect to the target URL
  --verify-ssl          Verify SSL certificates (not verified by default)
  --log-response        Include HTTP responses into ~/.sstimap/sstimap.log
crawler:
  These options can specify how to detect URLs and forms on the target
  website.
  -c, --crawl CRAWL_DEPTH
                        Depth to crawl (default/0: don't crawl)
  -f, --forms           Scan page(s) for forms
  --empty-forms         Treat pages without params as GET forms
  --crawl-exclude CRAWL_EXCLUDE
                        RegEx in URLs to not crawl
  --crawl-domains CRAWL_DOMAINS
                        Crawl other domains: Y(es) / S(ubdomains) / N(o).
                        Default: S
  --save-urls SAVE_URLS
                        File or directory to save crawled URLs to
  --save-forms SAVE_FORMS
                        File or directory to save crawled forms to
detection:
  These options can be used to customize the detection phase.
  -l, --level LEVEL     Level of escaping to perform (1-5, Default: 1)
  -L, --force-level LEVEL CLEVEL
                        Force a LEVEL and CLEVEL to test
  -e, --engine ENGINE   Comma-separated list of template engines to test:
                        [language:[variant:]][category/]engine,... For all,
                        use '*'
  -r, --technique TECHNIQUE
                        Techniques: R(endered) E(rror-based) B(oolean error-
                        based blind) T(ime-based blind). Default: REBT
  --bool-ok BOOLEAN_REGEX_OK
                        RegEx to match when boolean error-based blind payload
                        evaluates correctly
  --bool-err BOOLEAN_REGEX_ERR
                        RegEx to match when boolean error-based blind payload
                        causes an error
  --bool-match BOOLEAN_MATCH
                        Comma-separated list of matching params or 'all'.
                        Default: code,header_count,cookie_count,byte_len,body_
                        len,body_words,body_lines,encoding,redirects,time,url,
                        content_type,server
  --bool-match-min BOOLEAN_MATCH_MIN
                        Minimum amount of usable params for matching. Default:
                        7
  --bool-fuzzy STABLE ERROR
                        Allow small deviations in some of the matching
                        parameters. Default: 0.05 0.1
  --bool-samples COUNT MIN MAX
                        Amount of tests to profile the page and payload sizes.
                        Default: 10 1 7
  --blind-delay TIME_BASED_BLIND_DELAY
                        Delay to detect time-based blind injection (Default: 4
                        seconds)
  --verify-blind-delay TIME_BASED_VERIFY_BLIND_DELAY
                        Delay to verify and exploit time-based blind injection
                        (Default: 30 seconds)
  --legacy              Include old payloads, that no longer work with newer
                        versions of the engines
  --generic             Try dedicated payloads for generic engines, detecting
                        more context.
  --run                 Run detection at the start of SSTImap in interactive
                        mode.
payload:
  These options can be used to get access to the template engine, filesystem
  or OS shell after an attack.
  -t, --tpl-shell       Prompt for an interactive shell on the template engine
  -T, --tpl-code TPL_CODE
                        Inject code in the template engine
  -x, --eval-shell      Prompt for an interactive shell on the template engine
                        base language
  -X, --eval-code EVAL_CODE
                        Evaluate code in the template engine base language
  -s, --os-shell        Prompt for an interactive operating system shell
  -S, --os-cmd OS_CMD   Execute an operating system command
  -B, --bind-shell PORT
                        Spawn a system shell on a TCP PORT of the target and
                        connect to it
  -R, --reverse-shell HOST PORT
                        Run a system shell and back-connect to local HOST PORT
  --remote-shell REMOTE_SHELL
                        Expected system shell on the target (default
                        '/bin/sh')
  -F, --force-overwrite
                        Force file overwrite when uploading
  -U, --upload LOCAL REMOTE
                        Upload LOCAL to REMOTE files
  -D, --download REMOTE LOCAL
                        Download REMOTE to LOCAL files
Updated on: 2026-Aug-25
 Edit this page
sslyze
starkiller
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sstimap`，再执行 `sstimap --version` 2>/dev/null || `sstimap -V`
- [ ] **2.** **读官方帮助** —— `sstimap -h`，需要细节时 `man sstimap`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sstimap -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sstimap/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sstimap/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sstimap/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
