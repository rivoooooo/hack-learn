# humble

> HTTP Headers Analyzer This package contains an humble, and fast, security-oriented HTTP headers analyzer.

> **功能分类**：通用工具 ｜ **Kali 包**：`humble` ｜ **官方文档**：<https://www.kali.org/tools/humble/>

## 1. 安装

```bash
sudo apt update
sudo apt install humble
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.64 |
| 架构 | all |
| 可执行命令 | `humble` |
| 依赖 | `publicsuffix`、`python3`、`python3-colorama`、`python3-defusedcsv`、`python3-fpdf`、`python3-requests`、`python3-tldextract`、`python3-xlsxwriter` |
| 安装体积 | 470 KB |
| 官网 | <https://github.com/rfc-st/humble> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/humble> |
| 包追踪 | <https://pkg.kali.org/pkg/humble> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
humble -h          # 查看用法
man humble         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `humble`

> 官方示例调用：`humble -h`

```text
root@kali:~# humble -h
usage: humble.py [-h] [-a] [-b] [-c] [-cicd [GRADE]] [-df] [-e [TESTSSL_PATH]]
                 [-f [FINGERPRINT_TERM]] [-g] [-grd] [-H REQUEST_HEADER]
                 [-if INPUT_FILE] [-l {es}] [-lic]
                 [-o {all,csv,html,json,pdf,txt,xlsx,xml}] [-of OUTPUT_FILE]
                 [-op OUTPUT_PATH] [-p PROXY] [-r] [-s [SKIP_HEADERS ...]]
                 [-u URL] [-ua USER_AGENT] [-v]
'humble' (HTTP Headers Analyzer) | https://github.com/rfc-st/humble | v.2026-07-31
options:
  -h, --help                               show this help message and exit
  -a                                       Print statistics of the performed
                                           analysis; if the '-u' parameter is
                                           omitted they will be global
  -b                                       Print overall findings; if omitted
                                           detailed ones will be printed
  -c                                       Checks URL response HTTP headers
                                           for compliance with OWASP 'Secure
                                           Headers Project' best practices
  -cicd [GRADE]                            Print analysis for CI/CD
                                           processing; optionally, set the
                                           minimum required GRADE (E, D, C, B,
                                           A, A+)
  -df                                      Do not follow redirects; if omitted
                                           the last redirection will be the
                                           one analyzed
  -e [TESTSSL_PATH]                        Print only TLS/SSL checks; requires
                                           the PATH of testssl
                                           (https://testssl.sh/)
  -f [FINGERPRINT_TERM]                    Print fingerprint statistics; if
                                           'FINGERPRINT_TERM' (E.g., 'Google')
                                           is omitted the top 20 results will
                                           be printed
  -g                                       Print guidelines for enabling
                                           security HTTP response headers on
                                           popular frameworks, servers and
                                           services
  -grd                                     Print the checks to grade an
                                           analysis, along with advice for
                                           improvement
  -H REQUEST_HEADER                        Adds REQUEST_HEADER to the request;
                                           must be in double quotes and can be
                                           used multiple times, e.g. -H "Host:
                                           example.com"
  -if INPUT_FILE                           Analyzes 'INPUT_FILE': curl's '--
                                           dump-header' file or HTTP Archive
                                           (HAR) file
  -l {es}                                  Defines the language for displaying
                                           analysis, errors and messages; if
                                           omitted, will be printed in English
  -lic                                     Print the license for 'humble',
                                           along with permissions, limitations
                                           and conditions
  -o {all,csv,html,json,pdf,txt,xlsx,xml}  Export the analysis to the
                                           specified formats (separated by
                                           spaces); 'all' will export to all
                                           formats
  -of OUTPUT_FILE                          Exports analysis to 'OUTPUT_FILE';
                                           if omitted the default filename of
                                           the parameter '-o' will be used
  -op OUTPUT_PATH                          Exports analysis to 'OUTPUT_PATH';
                                           must be absolute. If omitted the
                                           PATH of 'humble.py' will be used
  -p PROXY                                 Use a proxy for the analysis. E.g.,
                                           'http://127.0.0.1:8080'. If no port
                                           is specified '8080' will be used
  -r                                       Print HTTP response headers and a
                                           detailed analysis; '-b' parameter
                                           will take priority
  -s [SKIP_HEADERS ...]                    Skips 'deprecated/insecure' and
                                           'missing' checks for the indicated
                                           'SKIP_HEADERS' (separated by
                                           spaces)
  -u URL                                   Scheme, host and port to analyze.
                                           E.g., https://google.com or
                                           https://google.com:443
  -ua USER_AGENT                           User-Agent ID from
                                           'additional/user_agents.txt' file
                                           to use. '0' will print all and '1'
                                           is the default
  -v, --version                            Checks for updates at
                                           https://github.com/rfc-st/humble
examples:
  -u URL -a                            Print statistics of the analysis performed against the URL
  -u URL -b                            Analyzes the URL and prints overall findings
  -u URL -b -o csv                     Analyzes the URL and exports overall findings to CSV format
  -u URL -cicd A                       Analyzes the URL and prints CI/CD results, warning if they do not reach an 'A' grade
  -u URL -l es                         Analyzes the URL and prints (in Spanish) detailed findings
  -u URL -o pdf                        Analyzes the URL and exports detailed findings to PDF format
  -u URL -o html -of test              Analyzes the URL and exports detailed findings to HTML format and 'test' filename
  -u URL -o html json                  Analyzes the URL and exports detailed findings to HTML and JSON formats
  -u URL -o pdf -op D:/Tests           Analyzes the URL and exports detailed findings to PDF format and 'D:/Tests' path
  -u URL -p http://127.0.0.1:8080      Analyzes the URL using 'http://127.0.0.1:8080' as the proxy
  -u URL -r                            Analyzes the URL and prints detailed findings along with HTTP response headers
  -u URL -s ETag NEL                   Analyzes the URL and skips 'deprecated/insecure' and 'missing' checks for 'ETag' and 'NEL' headers
  -u URL -ua 4                         Analyzes the URL using the fourth User-Agent of 'additional/user_agents.txt' file
  -a -l es                             Print statistics (in Spanish) of the analysis performed against all URLs
  -f Google                            Print HTTP fingerprint headers related to the term 'Google'
want to contribute?:
  How to                               https://github.com/rfc-st/humble/blob/master/CONTRIBUTING.md
  Acknowledgements                     https://github.com/rfc-st/humble/#acknowledgements
  References and unit tests            https://humble.readthedocs.io
Updated on: 2026-Aug-25
 Edit this page
hubble
i2c-tools
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install humble`，再执行 `humble --version` 2>/dev/null || `humble -V`
- [ ] **2.** **读官方帮助** —— `humble -h`，需要细节时 `man humble`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `humble -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/humble/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/humble/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/humble/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
