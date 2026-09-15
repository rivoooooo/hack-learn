# xsrfprobe

> Prime Cross Site Request Forgery Audit and Exploitation Toolkit XSRFProbe is an advanced Cross Site Request Forgery (CSRF/XSRF) Audit and Exploitation Toolkit. Equipped with a powerful crawling engine and numerous systematic checks, it is …

> **功能分类**：通用工具 ｜ **Kali 包**：`xsrfprobe` ｜ **官方文档**：<https://www.kali.org/tools/xsrfprobe/>

## 1. 安装

```bash
sudo apt update
sudo apt install xsrfprobe
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.0.0 |
| 架构 | all |
| 可执行命令 | `xsrfprobe` |
| 依赖 | `python3`、`python3-bs4`、`python3-pydantic`、`python3-rapidfuzz`、`python3-requests`、`python3-selenium` |
| 安装体积 | 271 KB |
| 官网 | <https://github.com/0xInfection/XSRFProbe> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/xsrfprobe> |
| 包追踪 | <https://pkg.kali.org/pkg/xsrfprobe> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
xsrfprobe -h          # 查看用法
man xsrfprobe         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `xsrfprobe`

官方给出的调用示例：`xsrfprobe -h`

```text
root@kali:~# xsrfprobe -h
                        ________                    ______
    ____  __________________  __/_______________________  /______
    __  |/_/_  ___/_  ___/_  /_ ___  __ \_  ___/  __ \_  __ \  _ \
    __>  < _(__  )_  /   _  __/ __  /_/ /  /   / /_/ /  /_/ /  __/
    /_/|_| /____/ /_/    /_/    _  .___//_/    \____//_.___/\___/
                                /_/
                                    ~  0xInfection | v3.0.0
usage: xsrfprobe -u <url> <args>
Required Arguments:
  -u, --url URL         Main URL to test
Optional Arguments:
  -c, --cookie COOKIE   Cookie value to be requested with each successive
                        request. If there are multiple cookies, separate them
                        with commas. For example: `-c PHPSESSID=i837c5n83u4,
                        _gid=jdhfbuysf`.
  -o, --output OUTPUT   Output directory where files to be stored. Default is
                        the output/ folder where all files generated will be
                        stored.
  -d, --delay DELAY     Time delay between requests in seconds. Default is
                        zero.
  -q, --quiet           Set the DEBUG mode to quiet. Report only when
                        vulnerabilities are found. Minimal output will be
                        printed on screen.
  -H, --headers HEADERS
                        Comma separated list of custom headers you'd want to
                        use. For example: ``--headers "Accept=text/php,
                        X-Requested-With=XHR"``.
  -v, --verbose         Increase the verbosity of the output (e.g., -vv is
                        more than -v).
  -t, --timeout TIMEOUT
                        HTTP request timeout value in seconds. The entered
                        value may be either in floating point decimal or an
                        integer. Example: ``--timeout 10.0``
  -E, --exclude EXCLUDE
                        Comma-separated paths / file containing paths
                        (separated by newlines) to exclude when crawling and
                        scanning.
  --user-agent USER_AGENT
                        Custom user-agent to be used. Only one user-agent can
                        be specified.
  --max-chars MAXCHARS  Maximum allowed character length for the custom token
                        value to be generated. For example: `--max-chars 5`.
                        Default value is 6.
  --crawl               Crawl the whole site and simultaneously test all
                        discovered endpoints for CSRF.
  --max-urls MAX_URLS   Maximum number of URLs to crawl (with --crawl). 0
                        means unlimited. Default: 200.
  --max-depth MAX_DEPTH
                        Maximum link depth to crawl from the seed URL (with
                        --crawl). 0 means unlimited. Default: 5.
  --crawl-timeout CRAWL_TIMEOUT
                        Wall-clock time budget for crawling in seconds (with
                        --crawl). 0 means unlimited. Default: 0.
  --no-analysis         Skip the Post-Scan Analysis of Tokens which were
                        gathered during requests
  --skip-poc            Skip the PoC Form Generation of POST-Based Cross Site
                        Request Forgeries.
  --no-verify           Do not verify SSL certificates with requests.
  --debug               Print out requests and responses while making
                        requests.
  --random-agent        Use random user-agents for making requests.
  --version             Display the version of XSRFProbe and exit.
  --json                Output the results into a JSON file.
  --force-header-tests  Run Referer/Origin header tests even when an anti-CSRF
                        token is confirmed enforced. Research/opt-in only:
                        bypass requests still carry a valid token, so results
                        on token-protected endpoints are false positives.
Browser Integration:
  --browser             Enable headless Firefox browser for SameSite and
                        browser-dependent tests.
  --auto-validate-poc   Auto-validate generated PoC files in headless browser
                        (requires --browser).
  --geckodriver-path GECKODRIVER_PATH
                        Path to geckodriver binary. Default: assumes
                        geckodriver is in PATH.
  --browser-timeout BROWSER_TIMEOUT
                        Page load timeout for headless browser in seconds.
                        Default: 30.
  --enum-subdomains     Enable subdomain enumeration via crt.sh for
                        SameSite=Strict sibling domain bypass tests.
  --no-form-submit      Do not submit forms during scanning. Only perform
                        passive token detection.
Updated on: 2026-Aug-25
 Edit this page
xplico
yara
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install xsrfprobe`，再执行 `xsrfprobe --version` 2>/dev/null || `xsrfprobe -V`
- [ ] **2.** **读官方帮助** —— `xsrfprobe -h`，需要细节时 `man xsrfprobe`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `xsrfprobe -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/xsrfprobe/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/xsrfprobe/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/xsrfprobe/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
