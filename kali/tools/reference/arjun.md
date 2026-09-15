# arjun

> HTTP parameter discovery suite This package can find query parameters for URL endpoints. Web applications use parameters (or queries) to accept user input, take the following example into consideration. http://api.example.com/v1/userinfo?i…

> **功能分类**：通用工具 ｜ **Kali 包**：`arjun` ｜ **官方文档**：<https://www.kali.org/tools/arjun/>

## 1. 安装

```bash
sudo apt update
sudo apt install arjun
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.2.7 |
| 架构 | all |
| 可执行命令 | `arjun` |
| 依赖 | `python3`、`python3-dicttoxml`、`python3-ratelimit`、`python3-requests` |
| 安装体积 | 348 KB |
| 官网 | <https://github.com/s0md3v/Arjun> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/arjun> |
| 包追踪 | <https://pkg.kali.org/pkg/arjun> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
arjun -h          # 查看用法
man arjun         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `arjun`

> 官方示例调用：`arjun -h`

```text
root@kali:~# arjun -h
usage: arjun [-h] [-u URL] [-o JSON_FILE] [-oT TEXT_FILE] [-oB [BURP_PROXY]]
             [-d DELAY] [-t THREADS] [-w WORDLIST] [-m METHOD]
             [-i [IMPORT_FILE]] [-T TIMEOUT] [-c CHUNKS] [-q]
             [--rate-limit RATE_LIMIT] [--headers [HEADERS]]
             [--passive [PASSIVE]] [--stable] [--include INCLUDE]
             [--disable-redirects] [--casing CASING]
options:
  -h, --help            show this help message and exit
  -u URL                Target URL
  -o, -oJ JSON_FILE     Path for json output file.
  -oT TEXT_FILE         Path for text output file.
  -oB [BURP_PROXY]      Output to Burp Suite Proxy. Default is 127.0.0.1:8080.
  -d DELAY              Delay between requests in seconds. (default: 0)
  -t THREADS            Number of concurrent threads. (default: 5)
  -w WORDLIST           Wordlist file path. (default: {arjundir}/db/large.txt)
  -m METHOD             Request method to use: GET/POST/XML/JSON. (default:
                        GET)
  -i [IMPORT_FILE]      Import target URLs from file.
  -T TIMEOUT            HTTP request timeout in seconds. (default: 15)
  -c CHUNKS             Chunk size. The number of parameters to be sent at
                        once
  -q                    Quiet mode. No output.
  --rate-limit RATE_LIMIT
                        Max number of requests to be sent out per second
                        (default: 9999)
  --headers [HEADERS]   Add headers. Separate multiple headers with a new
                        line.
  --passive [PASSIVE]   Collect parameter names from passive sources like
                        wayback, commoncrawl and otx.
  --stable              Prefer stability over speed.
  --include INCLUDE     Include this data in every request.
  --disable-redirects   disable redirects
  --casing CASING       casing style for params e.g. like_this, likeThis,
                        likethis
Updated on: 2026-Jun-17
 Edit this page
xsstrike
autorecon
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install arjun`，再执行 `arjun --version` 2>/dev/null || `arjun -V`
- [ ] **2.** **读官方帮助** —— `arjun -h`，需要细节时 `man arjun`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `arjun -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/arjun/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/arjun/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/arjun/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
