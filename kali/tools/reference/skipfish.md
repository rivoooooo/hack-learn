# skipfish

> Fully automated, active web application security reconnaissance tool Skipfish is an active web application security reconnaissance tool. It prepares an interactive sitemap for the targeted site by carrying out a recursive crawl and diction…

> **功能分类**：Web 应用 ｜ **Kali 包**：`skipfish` ｜ **官方文档**：<https://www.kali.org/tools/skipfish/>

## 1. 安装

```bash
sudo apt update
sudo apt install skipfish
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.10b |
| 架构 | any |
| 可执行命令 | `skipfish` |
| 依赖 | `libc6`、`libidn12`、`libpcre3`、`libssl3t64`、`zlib1g` |
| 安装体积 | 563 KB |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/skipfish> |
| 包追踪 | <https://pkg.kali.org/pkg/skipfish> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Using the given directory for output (-o 202), scan the web application URL (http://192.168.1.202/wordpress):
root@kali:~# skipfish -o 202 http://192.168.1.202/wordpress

skipfish version 2.10b by lcamtuf@google.com

  - 192.168.1.202 -

Scan statistics:

      Scan time : 0:00:05.849
  HTTP requests : 2841 (485.6/s), 1601 kB in, 563 kB out (370.2 kB/s)
    Compression : 802 kB in, 1255 kB out (22.0% gain)
    HTTP faults : 0 net errors, 0 proto errors, 0 retried, 0 drops
 TCP handshakes : 46 total (61.8 req/conn)
     TCP faults : 0 failures, 0 timeouts, 16 purged
 External links : 512 skipped
   Reqs pending : 0

Database statistics:

         Pivots : 13 total, 12 done (92.31%)
    In progress : 0 pending, 0 init, 0 attacks, 1 dict
  Missing nodes : 0 spotted
     Node types : 1 serv, 4 dir, 6 file, 0 pinfo, 0 unkn, 2 par, 0 val
   Issues found : 10 info, 0 warn, 0 low, 8 medium, 0 high impact
      Dict size : 20 words (20 new), 1 extensions, 202 candidates
     Signatures : 77 total

[+] Copying static resources...
[+] Sorting and annotating crawl nodes: 13
[+] Looking for duplicate entries: 13
[+] Counting unique nodes: 11
[+] Saving pivot data for third-party tools...
[+] Writing scan description...
[+] Writing crawl tree: 13
[+] Generating summary views...
[+] Report saved to '202/index.html' [0x7054c49d].
[+] This was a great day for science!
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `skipfish`

官方给出的调用示例：`skipfish -o 202 http://192.168.1.202/wordpress`

```text
root@kali:~# skipfish -o 202 http://192.168.1.202/wordpress
skipfish version 2.10b by
[email protected]
  - 192.168.1.202 -
Scan statistics:
      Scan time : 0:00:05.849
  HTTP requests : 2841 (485.6/s), 1601 kB in, 563 kB out (370.2 kB/s)
    Compression : 802 kB in, 1255 kB out (22.0% gain)
    HTTP faults : 0 net errors, 0 proto errors, 0 retried, 0 drops
 TCP handshakes : 46 total (61.8 req/conn)
     TCP faults : 0 failures, 0 timeouts, 16 purged
 External links : 512 skipped
   Reqs pending : 0
Database statistics:
         Pivots : 13 total, 12 done (92.31%)
    In progress : 0 pending, 0 init, 0 attacks, 1 dict
  Missing nodes : 0 spotted
     Node types : 1 serv, 4 dir, 6 file, 0 pinfo, 0 unkn, 2 par, 0 val
   Issues found : 10 info, 0 warn, 0 low, 8 medium, 0 high impact
      Dict size : 20 words (20 new), 1 extensions, 202 candidates
     Signatures : 77 total
[+] Copying static resources...
[+] Sorting and annotating crawl nodes: 13
[+] Looking for duplicate entries: 13
[+] Counting unique nodes: 11
[+] Saving pivot data for third-party tools...
[+] Writing scan description...
[+] Writing crawl tree: 13
[+] Generating summary views...
[+] Report saved to '202/index.html' [0x7054c49d].
[+] This was a great day for science!
```

### `skipfish（示例）`

官方给出的调用示例：`skipfish -h`

```text
root@kali:~# skipfish -h
skipfish web application scanner - version 2.10b
Usage: skipfish [ options ... ] -W wordlist -o output_dir start_url [ start_url2 ... ]
Authentication and access options:
  -A user:pass      - use specified HTTP authentication credentials
  -F host=IP        - pretend that 'host' resolves to 'IP'
  -C name=val       - append a custom cookie to all requests
  -H name=val       - append a custom HTTP header to all requests
  -b (i|f|p)        - use headers consistent with MSIE / Firefox / iPhone
  -N                - do not accept any new cookies
  --auth-form url   - form authentication URL
  --auth-user user  - form authentication user
  --auth-pass pass  - form authentication password
  --auth-verify-url -  URL for in-session detection
Crawl scope options:
  -d max_depth     - maximum crawl tree depth (16)
  -c max_child     - maximum children to index per node (512)
  -x max_desc      - maximum descendants to index per branch (8192)
  -r r_limit       - max total number of requests to send (100000000)
  -p crawl%        - node and link crawl probability (100%)
  -q hex           - repeat probabilistic scan with given seed
  -I string        - only follow URLs matching 'string'
  -X string        - exclude URLs matching 'string'
  -K string        - do not fuzz parameters named 'string'
  -D domain        - crawl cross-site links to another domain
  -B domain        - trust, but do not crawl, another domain
  -Z               - do not descend into 5xx locations
  -O               - do not submit any forms
  -P               - do not parse HTML, etc, to find new links
Reporting options:
  -o dir          - write output to specified directory (required)
  -M              - log warnings about mixed content / non-SSL passwords
  -E              - log all HTTP/1.0 / HTTP/1.1 caching intent mismatches
  -U              - log all external URLs and e-mails seen
  -Q              - completely suppress duplicate nodes in reports
  -u              - be quiet, disable realtime progress stats
  -v              - enable runtime logging (to stderr)
Dictionary management options:
  -W wordlist     - use a specified read-write wordlist (required)
  -S wordlist     - load a supplemental read-only wordlist
  -L              - do not auto-learn new keywords for the site
  -Y              - do not fuzz extensions in directory brute-force
  -R age          - purge words hit more than 'age' scans ago
  -T name=val     - add new form auto-fill rule
  -G max_guess    - maximum number of keyword guesses to keep (256)
  -z sigfile      - load signatures from this file
Performance settings:
  -g max_conn     - max simultaneous TCP connections, global (40)
  -m host_conn    - max simultaneous connections, per target IP (10)
  -f max_fail     - max number of consecutive HTTP errors (100)
  -t req_tmout    - total request response timeout (20 s)
  -w rw_tmout     - individual network I/O timeout (10 s)
  -i idle_tmout   - timeout on idle HTTP connections (10 s)
  -s s_limit      - response size limit (400000 B)
  -e              - do not keep binary responses for reporting
Other settings:
  -l max_req      - max requests per second (0.000000)
  -k duration     - stop scanning after the given duration h:m:s
  --config file   - load the specified configuration file
Send comments and complaints to <
[email protected]
>.
Learn more with
OffSec
Want to learn more about skipfish? get access to in-depth training and hands-on labs:
Introduction to Vulnerability Tracking: 2.4. Scanning for Web Vulnerabilities
Updated on: 2026-Mar-02
 Edit this page
siparmyknife
snmpenum
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install skipfish`，再执行 `skipfish --version` 2>/dev/null || `skipfish -V`
- [ ] **2.** **读官方帮助** —— `skipfish -h`，需要细节时 `man skipfish`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: skipfish [ options ... ] -W wordlist -o output_dir start_url [ start_url2 ... ]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/skipfish/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/skipfish/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/skipfish/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
