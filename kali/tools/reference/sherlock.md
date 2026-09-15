# sherlock

> Find usernames across social networks Sherlock relies on the site’s designers providing a unique URL for a registered username. To determine if a username is available, Sherlock queries that URL, and uses to response to understand if there…

> **功能分类**：通用工具 ｜ **Kali 包**：`sherlock` ｜ **官方文档**：<https://www.kali.org/tools/sherlock/>

## 1. 安装

```bash
sudo apt update
sudo apt install sherlock
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.16.0 |
| 架构 | all |
| 可执行命令 | `sherlock` |
| 依赖 | `python3`、`python3-certifi`、`python3-colorama`、`python3-openpyxl`、`python3-pandas`、`python3-requests`、`python3-requests-futures`、`python3-socks`、`python3-stem` |
| 安装体积 | 187 KB |
| 官网 | <https://github.com/sherlock-project/sherlock> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/sherlock> |
| 包追踪 | <https://pkg.kali.org/pkg/sherlock> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sherlock -h          # 查看用法
man sherlock         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sherlock`

官方给出的调用示例：`sherlock -h`

```text
root@kali:~# sherlock -h
usage: sherlock [-h] [--version] [--verbose] [--folderoutput FOLDEROUTPUT]
                [--output OUTPUT] [--tor] [--unique-tor] [--csv] [--xlsx]
                [--site SITE_NAME] [--proxy PROXY_URL] [--dump-response]
                [--json JSON_FILE] [--timeout TIMEOUT] [--print-all]
                [--print-found] [--no-color] [--browse] [--local] [--remote]
                [--nsfw] [--no-txt] [--ignore-exclusions]
                USERNAMES [USERNAMES ...]
Sherlock: Find Usernames Across Social Networks (Version 0.16.0)
positional arguments:
  USERNAMES             One or more usernames to check with social networks.
                        Check similar usernames using {?} (replace to '_',
                        '-', '.').
options:
  -h, --help            show this help message and exit
  --version             Display version information and dependencies.
  --verbose, -v, -d, --debug
                        Display extra debugging information and metrics.
  --folderoutput, -fo FOLDEROUTPUT
                        If using multiple usernames, the output of the results
                        will be saved to this folder.
  --output, -o OUTPUT   If using single username, the output of the result
                        will be saved to this file.
  --tor, -t             Make requests over Tor; increases runtime; requires
                        Tor to be installed and in system path.
  --unique-tor, -u      Make requests over Tor with new Tor circuit after each
                        request; increases runtime; requires Tor to be
                        installed and in system path.
  --csv                 Create Comma-Separated Values (CSV) File.
  --xlsx                Create the standard file for the modern Microsoft
                        Excel spreadsheet (xlsx).
  --site SITE_NAME      Limit analysis to just the listed sites. Add multiple
                        options to specify more than one site.
  --proxy, -p PROXY_URL
                        Make requests over a proxy. e.g.
                        socks5://127.0.0.1:1080
  --dump-response       Dump the HTTP response to stdout for targeted
                        debugging.
  --json, -j JSON_FILE  Load data from a JSON file or an online, valid, JSON
                        file. Upstream PR numbers also accepted.
  --timeout TIMEOUT     Time (in seconds) to wait for response to requests
                        (Default: 60)
  --print-all           Output sites where the username was not found.
  --print-found         Output sites where the username was found (also if
                        exported as file).
  --no-color            Don't color terminal output
  --browse, -b          Browse to all results on default browser.
  --local, -l           Use the local data.json file.
  --remote              Fetch data.json from GitHub instead of the local file.
  --nsfw                Include checking of NSFW sites from default list.
  --no-txt              Disable creation of a txt file
  --ignore-exclusions   Ignore upstream exclusions (may return more false
                        positives)
Learn more with
OffSec
Want to learn more about sherlock? get access to in-depth training and hands-on labs:
SEC-100: 19.1.2. Information Gathering and Enumeration: Manual Snooping
SEC-100 course
Updated on: 2026-Aug-25
 Edit this page
shellfire
sidguesser
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sherlock`，再执行 `sherlock --version` 2>/dev/null || `sherlock -V`
- [ ] **2.** **读官方帮助** —— `sherlock -h`，需要细节时 `man sherlock`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sherlock -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sherlock/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sherlock/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sherlock/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
