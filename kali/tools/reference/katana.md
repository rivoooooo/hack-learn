# katana

> Next-generation crawling and spidering framework. A next-generation crawling and spidering framework Fast And fully configurable web crawling Standard and Headless mode JavaScript parsing / crawling Customizable automatic form filling

> **功能分类**：通用工具 ｜ **Kali 包**：`katana` ｜ **官方文档**：<https://www.kali.org/tools/katana/>

## 1. 安装

```bash
sudo apt update
sudo apt install katana
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.7.0 |
| 架构 | any |
| 可执行命令 | `katana` |
| 依赖 | `libc6` |
| 安装体积 | 64.20 MB |
| 官网 | <https://github.com/projectdiscovery/katana> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/katana> |
| 包追踪 | <https://pkg.kali.org/pkg/katana> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
katana -h          # 查看用法
man katana         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `katana`

> 官方示例调用：`katana -h`

```text
root@kali:~# katana -h
Katana is a fast crawler focused on execution in automation pipelines offering both headless and non-headless crawling.
Usage:
  katana [flags]
Flags:
INPUT:
   -u, -list string[]     target url / list to crawl
   -resume string         resume scan using resume.cfg
   -e, -exclude string[]  exclude host matching specified filter ('cdn', 'private-ips', cidr, ip, regex)
CONFIGURATION:
   -r, -resolvers string[]              list of custom resolver (file or comma separated)
   -d, -depth int                       maximum depth to crawl (default 3)
   -jc, -js-crawl                       enable endpoint parsing / crawling in javascript file
   -jsl, -jsluice                       enable jsluice parsing in javascript file (memory intensive)
   -ct, -crawl-duration value           maximum duration to crawl the target for (s, m, h, d) (default s)
   -kf, -known-files value              enable crawling of known files (all,robotstxt,sitemapxml), a minimum depth of 3 is required to ensure all known files are properly crawled.
   -mrs, -max-response-size int         maximum response size to read (default 4194304)
   -timeout int                         time to wait for request in seconds (default 10)
   -time-stable int                     time to wait until the page is stable in seconds (default 1)
   -aff, -automatic-form-fill           enable automatic form filling (experimental)
   -fx, -form-extraction                extract form, input, textarea & select elements in jsonl output
   -retry int                           number of times to retry the request (default 1)
   -proxy string                        http/socks5 proxy to use
   -td, -tech-detect                    enable technology detection
   -H, -headers string[]                custom header/cookie to include in all http request in header:value format (file)
   -config string                       path to the katana configuration file
   -fc, -form-config string             path to custom form configuration file
   -flc, -field-config string           path to custom field configuration file
   -s, -strategy string                 Visit strategy (depth-first, breadth-first) (default "depth-first")
   -iqp, -ignore-query-params           Ignore crawling same path with different query-param values
   -fsu, -filter-similar                filter crawling of similar looking URLs (e.g., /users/123 and /users/456)
   -fst, -filter-similar-threshold int  number of distinct values before a path position is treated as parameter (default 10) (default 10)
   -tlsi, -tls-impersonate              enable experimental client hello (ja3) tls randomization
   -dr, -disable-redirects              disable following redirects (default false)
   -pc, -path-climb                     enable path climb (auto crawl parent paths)
   -kb, -knowledge-base                 enable knowledge base classification
   -kb-secrets                          enable secrets extractor in the knowledge base
   -kb-validate-secrets                 validate detected secrets against their provider (sends live API calls)
   -kb-endpoints                        enable endpoints extractor (classifies REST/GraphQL/SOAP/XHR requests)
   -mdp, -max-domain-pages int          maximum number of pages to crawl per domain (default unlimited)
DEBUG:
   -health-check, -hc        run diagnostic check up
   -elog, -error-log string  file to write sent requests error log
   -pprof-server             enable pprof server
HEADLESS:
   -hl, -headless                         enable headless crawling (experimental)
   -hh, -hybrid                           enable headless hybrid crawling (experimental)
   -sc, -system-chrome                    use local installed chrome browser instead of katana installed
   -sb, -show-browser                     show the browser on the screen with headless mode
   -ho, -headless-options string[]        start headless chrome with additional options
   -nos, -no-sandbox                      start headless chrome in --no-sandbox mode
   -cdd, -chrome-data-dir string          path to store chrome browser data
   -scp, -system-chrome-path string       use specified chrome browser for headless crawling
   -noi, -no-incognito                    start headless chrome without incognito mode
   -cwu, -chrome-ws-url string            use chrome browser instance launched elsewhere with the debugger listening at this URL
   -xhr, -xhr-extraction                  extract xhr request url,method in jsonl output
   -mfc, -max-failure-count int           maximum number of consecutive action failures before stopping (default 10)
   -ed, -enable-diagnostics               enable diagnostics
   -pls, -page-load-strategy string       page load strategy (heuristic, load, domcontentloaded, networkidle, none) (default "heuristic")
   -dwt, -dom-wait-time int               time in seconds to wait after page load when using domcontentloaded strategy (default 5)
   -csp, -captcha-solver-provider string  captcha solver provider (e.g. capsolver)
   -csk, -captcha-solver-key string       captcha solver provider api key
   -al, -auto-login string                automatic login with username:password (headless only)
SCOPE:
   -cs, -crawl-scope string[]       in scope url regex to be followed by crawler
   -cos, -crawl-out-scope string[]  out of scope url regex to be excluded by crawler
   -fs, -field-scope string         pre-defined scope field (dn,rdn,fqdn) or custom regex (e.g., '(company-staging.io|company.com)') (default "rdn")
   -ns, -no-scope                   disables host based default scope
   -do, -display-out-scope          display external endpoint from scoped crawling
FILTER:
   -mr, -match-regex string[]                     regex or list of regex to match on output url (cli, file)
   -fr, -filter-regex string[]                    regex or list of regex to filter on output url (cli, file)
   -f, -field string                              field to display in output (url,path,fqdn,rdn,rurl,qurl,qpath,file,ufile,key,value,kv,dir,udir) (Deprecated: use -output-template instead)
   -sf, -store-field string                       field to store in per-host output (url,path,fqdn,rdn,rurl,qurl,qpath,file,ufile,key,value,kv,dir,udir)
   -em, -extension-match string[]                 match output for given extension (eg, -em php,html,js,none)
   -ef, -extension-filter string[]                filter output for given extension (eg, -ef png,css)
   -ndef, -no-default-ext-filter                  remove default extensions from the filter list
   -mdc, -match-condition string                  match response with dsl based condition
   -fdc, -filter-condition string                 filter response with dsl based condition
   -duf, -disable-unique-filter                   disable duplicate content filtering
   -pcs, -page-content-similar                    enable page content similarity filtering (after exact content dedup)
   -sdd, -similarity-deduplication                alias for -pcs (page content similarity)
   -pcsm, -page-content-similar-mode string       similarity mode: simhash, tfidf, or bm25 (default "simhash")
   -pcsd, -page-content-similar-distance int      simhash max hamming distance (default 3) (default 3)
   -pcst, -page-content-similar-threshold string  tfidf/bm25 min score 0-1 (default 0.85) (default "0.85")
   -pcsn, -page-content-similar-budget int        pages to fully process per similarity cluster (default 1) (default 1)
   -fpt, -filter-page-type string[]               filter response with page type (e.g. error,captcha,parked)
RATE-LIMIT:
   -c, -concurrency int                number of concurrent fetchers to use (default 10)
   -p, -parallelism int                number of concurrent inputs to process (default 10)
   -rd, -delay int                     request delay between each request in seconds
   -rl, -rate-limit int                maximum requests to send per second (default 150)
   -rlm, -rate-limit-minute int        maximum number of requests to send per minute
   -hrl, -host-rate-limit int          maximum requests to send per second per host
   -hrlm, -host-rate-limit-minute int  maximum number of requests to send per minute per host
UPDATE:
   -up, -update                 update katana to latest version
   -duc, -disable-update-check  disable automatic katana update check
OUTPUT:
   -o, -output string                     file to write output to
   -ot, -output-template string           custom output template
   -sr, -store-response                   store http requests/responses
   -srd, -store-response-dir string       store http requests/responses to custom directory
   -ncb, -no-clobber                      do not overwrite output file
   -sfd, -store-field-dir string          store per-host field to custom directory
   -or, -omit-raw                         omit raw requests/responses from jsonl output
   -ob, -omit-body                        omit response body from jsonl output
   -lof, -list-output-fields              list of fields to output in jsonl format
   -eof, -exclude-output-fields string[]  exclude fields from jsonl output
   -j, -jsonl                             write output in jsonl format
   -nc, -no-color                         disable output content coloring (ANSI escape codes)
   -silent                                display output only
   -v, -verbose                           display verbose output
   -debug                                 display debug output
   -version                               display project version
Updated on: 2026-Sep-03
 Edit this page
ciphey
rustscan
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install katana`，再执行 `katana --version` 2>/dev/null || `katana -V`
- [ ] **2.** **读官方帮助** —— `katana -h`，需要细节时 `man katana`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/katana/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/katana/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/katana/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
