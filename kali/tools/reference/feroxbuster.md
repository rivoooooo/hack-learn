# feroxbuster

> Fast, simple, recursive content discovery tool written in Rust feroxbuster is a tool designed to perform Forced Browsing. Forced browsing is an attack where the aim is to enumerate and access resources that are not referenced by the web ap…

> **功能分类**：信息搜集 ｜ **Kali 包**：`feroxbuster` ｜ **官方文档**：<https://www.kali.org/tools/feroxbuster/>

## 1. 安装

```bash
sudo apt update
sudo apt install feroxbuster
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.13.1 |
| 架构 | any |
| 可执行命令 | `feroxbuster` |
| 依赖 | `fonts-noto-color-emoji`、`libc6`、`libgcc-s1` |
| 安装体积 | 12.27 MB |
| 官网 | <https://github.com/epi052/feroxbuster> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/feroxbuster> |
| 包追踪 | <https://pkg.kali.org/pkg/feroxbuster> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
feroxbuster -h          # 查看用法
man feroxbuster         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `feroxbuster`

官方给出的调用示例：`feroxbuster --help`

```text
root@kali:~# feroxbuster --help
A fast, simple, recursive content discovery tool.
Usage: feroxbuster [OPTIONS]
Options:
  -h, --help
          Print help (see a summary with '-h')
  -V, --version
          Print version
Target selection:
  -u, --url <URL>
          The target URL (required, unless [--stdin || --resume-from ||
          --request-file] used)
      --stdin
          Read url(s) from STDIN
      --resume-from <STATE_FILE>
          State file from which to resume a partially complete scan (ex.
          --resume-from ferox-1606586780.state)
      --request-file <REQUEST_FILE>
          Raw HTTP request file to use as a template for all requests
Composite settings:
      --burp
          Set --proxy to http://127.0.0.1:8080 and set --insecure to true
      --burp-replay
          Set --replay-proxy to http://127.0.0.1:8080 and set --insecure to true
      --data-urlencoded <DATA>
          Set -H 'Content-Type: application/x-www-form-urlencoded', --data to
          <data-urlencoded> (supports @file) and -m to POST
      --data-json <DATA>
          Set -H 'Content-Type: application/json', --data to <data-json>
          (supports @file) and -m to POST
      --smart
          Set --auto-tune, --collect-words, and --collect-backups to true
      --thorough
          Use the same settings as --smart and set --collect-extensions and
          --scan-dir-listings to true
Proxy settings:
  -p, --proxy <PROXY>
          Proxy to use for requests (ex: http(s)://host:port,
          socks5(h)://host:port)
  -P, --replay-proxy <REPLAY_PROXY>
          Send only unfiltered requests through a Replay Proxy, instead of all
          requests
  -R, --replay-codes <REPLAY_CODE>...
          Status Codes to send through a Replay Proxy when found (default:
          --status-codes value)
Request settings:
  -a, --user-agent <USER_AGENT>
          Sets the User-Agent (default: feroxbuster/2.13.1)
  -A, --random-agent
          Use a random User-Agent
  -x, --extensions <FILE_EXTENSION>...
          File extension(s) to search for (ex: -x php -x pdf js); reads values
          (newline-separated) from file if input starts with an @ (ex: @ext.txt)
  -m, --methods <HTTP_METHODS>...
          Which HTTP request method(s) should be sent (default: GET)
      --data <DATA>
          Request's Body; can read data from a file if input starts with an @
          (ex: @post.bin)
  -H, --headers <HEADER>...
          Specify HTTP headers to be used in each request (ex: -H Header:val -H
          'stuff: things')
  -b, --cookies <COOKIE>...
          Specify HTTP cookies to be used in each request (ex: -b stuff=things)
  -Q, --query <QUERY>...
          Request's URL query parameters (ex: -Q token=stuff -Q secret=key)
  -f, --add-slash
          Append / to each request's URL
      --protocol <PROTOCOL>
          Specify the protocol to use when targeting via --request-file or --url
          with domain only (default: https)
Request filters:
      --dont-scan <URL>...
          URL(s) or Regex Pattern(s) to exclude from recursion/scans
      --scope <URL>...
          Additional domains/URLs to consider in-scope for scanning (in addition
          to current domain)
Response filters:
  -S, --filter-size <SIZE>...
          Filter out messages of a particular size (ex: -S 5120 -S 4927,1970)
  -X, --filter-regex <REGEX>...
          Filter out messages via regular expression matching on the response's
          body/headers (ex: -X '^ignore me$')
  -W, --filter-words <WORDS>...
          Filter out messages of a particular word count (ex: -W 312 -W 91,82)
  -N, --filter-lines <LINES>...
          Filter out messages of a particular line count (ex: -N 20 -N 31,30)
  -C, --filter-status <STATUS_CODE>...
          Filter out status codes (deny list) (ex: -C 200 -C 401)
      --filter-similar-to <UNWANTED_PAGE>...
          Filter out pages that are similar to the given page (ex.
          --filter-similar-to http://site.xyz/soft404)
  -s, --status-codes <STATUS_CODE>...
          Status Codes to include (allow list) (default: All Status Codes)
      --unique
          Only show unique responses
Client settings:
  -T, --timeout <SECONDS>
          Number of seconds before a client's request times out (default: 7)
  -r, --redirects
          Allow client to follow redirects
  -k, --insecure
          Disables TLS certificate validation in the client
      --server-certs <PEM|DER>...
          Add custom root certificate(s) for servers with unknown certificates
      --client-cert <PEM>
          Add a PEM encoded certificate for mutual authentication (mTLS)
      --client-key <PEM>
          Add a PEM encoded private key for mutual authentication (mTLS)
Scan settings:
  -t, --threads <THREADS>
          Number of concurrent threads (default: 50)
  -n, --no-recursion
          Do not scan recursively
  -d, --depth <RECURSION_DEPTH>
          Maximum recursion depth, a depth of 0 is infinite recursion (default:
          4)
      --force-recursion
          Force recursion attempts on all 'found' endpoints (still respects
          recursion depth)
      --dont-extract-links
          Don't extract links from response body (html, javascript, etc...)
  -L, --scan-limit <SCAN_LIMIT>
          Limit total number of concurrent scans (default: 0, i.e. no limit)
      --parallel <PARALLEL_SCANS>
          Run parallel feroxbuster instances (one child process per url passed
          via stdin)
      --rate-limit <RATE_LIMIT>
          Limit number of requests per second (per directory) (default: 0, i.e.
          no limit)
      --response-size-limit <BYTES>
          Limit size of response body to read in bytes (default: 4MB)
      --time-limit <TIME_SPEC>
          Limit total run time of all scans (ex: --time-limit 10m)
  -w, --wordlist <FILE>
          Path or URL of the wordlist
      --auto-tune
          Automatically lower scan rate when an excessive amount of errors are
          encountered
      --auto-bail
          Automatically stop scanning when an excessive amount of errors are
          encountered
  -D, --dont-filter
          Don't auto-filter wildcard responses
      --scan-dir-listings
          Force scans to recurse into directory listings
Dynamic collection settings:
  -E, --collect-extensions
          Automatically discover extensions and add them to --extensions (unless
          they're in --dont-collect)
  -B, --collect-backups [<collect_backups>...]
          Automatically request likely backup extensions for "found" urls
          (default: ~, .bak, .bak2, .old, .1)
  -g, --collect-words
          Automatically discover important words from within responses and add
          them to the wordlist
  -I, --dont-collect <FILE_EXTENSION>...
          File extension(s) to Ignore while collecting extensions (only used
          with --collect-extensions)
Output settings:
  -v, --verbosity...
          Increase verbosity level (use -vv or more for greater effect.
          [CAUTION] 4 -v's is probably too much)
      --silent
          Only print URLs (or JSON w/ --json) + turn off logging (good for
          piping a list of urls to other commands)
  -q, --quiet
          Hide progress bars and banner (good for tmux windows w/ notifications)
      --json
          Emit JSON logs to --output and --debug-log instead of normal text
  -o, --output <FILE>
          Output file to write results to (use w/ --json for JSON entries)
      --debug-log <FILE>
          Output file to write log entries (use w/ --json for JSON entries)
      --no-state
          Disable state output file (*.state)
      --limit-bars <NUM_BARS_TO_SHOW>
          Number of directory scan bars to show at any given time (default: no
          limit)
Update settings:
  -U, --update
          Update feroxbuster to the latest version
NOTE:
    Options that take multiple values are very flexible.  Consider the following
    ways of specifying
    extensions:
        feroxbuster -u http://127.1 -x pdf -x js,html -x php txt json,docx
    The command above adds .pdf, .js, .html, .php, .txt, .json, and .docx to
    each url
    All of the methods above (multiple flags, space separated, comma separated,
    etc...) are valid
    and interchangeable.  The same goes for urls, headers, status codes,
    queries, and size filters.
EXAMPLES:
    Multiple headers:
        feroxbuster -u http://127.1 -H Accept:application/json "Authorization:
        Bearer {token}"
    IPv6, non-recursive scan with INFO-level logging enabled:
        feroxbuster -u http://[::1] --no-recursion -vv
    Read urls from STDIN; pipe only resulting urls out to another tool
        cat targets | feroxbuster --stdin --silent -s 200 301 302 --redirects -x
        js | fff -s 200 -o js-files
    Proxy traffic through Burp
        feroxbuster -u http://127.1 --burp
    Proxy traffic through a SOCKS proxy
        feroxbuster -u http://127.1 --proxy socks5://127.0.0.1:9050
    Pass auth token via query parameter
        feroxbuster -u http://127.1 --query token=0123456789ABCDEF
    Ludicrous speed... go!
        feroxbuster -u http://127.1 --threads 200
    Limit to a total of 60 active requests at any given time (threads * scan
    limit)
        feroxbuster -u http://127.1 --threads 30 --scan-limit 2
    Send all 200/302 responses to a proxy (only proxy requests/responses you
    care about)
        feroxbuster -u http://127.1 --replay-proxy http://localhost:8080
        --replay-codes 200 302 --insecure
    Abort or reduce scan speed to individual directory scans when too many
    errors have occurred
        feroxbuster -u http://127.1 --auto-bail
        feroxbuster -u http://127.1 --auto-tune
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install feroxbuster`，再执行 `feroxbuster --version` 2>/dev/null || `feroxbuster -V`
- [ ] **2.** **读官方帮助** —— `feroxbuster -h`，需要细节时 `man feroxbuster`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: feroxbuster [OPTIONS]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/feroxbuster/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/feroxbuster/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/feroxbuster/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
