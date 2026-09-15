# waybackpy

> Access Wayback Machine’s API using Python waybackpy is a Python package and a CLI tool that interfaces with the Wayback Machine’s APIs. Internet Archive’s Wayback Machine has 3 useful public APIs. SavePageNow API (also known as Save API) C…

> **功能分类**：通用工具 ｜ **Kali 包**：`waybackpy` ｜ **官方文档**：<https://www.kali.org/tools/waybackpy/>

## 1. 安装

```bash
sudo apt update
sudo apt install waybackpy
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.0.6 |
| 架构 | all |
| 可执行命令 | `waybackpy` |
| 依赖 | `python3`、`python3-click`、`python3-requests`、`python3-urllib3` |
| 安装体积 | 96 KB |
| 官网 | <https://github.com/akamhy/waybackpy> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/waybackpy> |
| 包追踪 | <https://pkg.kali.org/pkg/waybackpy> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
waybackpy -h          # 查看用法
man waybackpy         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `waybackpy`

官方给出的调用示例：`waybackpy --help`

```text
root@kali:~# waybackpy --help
Usage: waybackpy [OPTIONS]
                       _                _
                      | |              | |
  __      ____ _ _   _| |__   __ _  ___| | ___ __  _   _
  \ \ /\ / / _` | | | | '_ \ / _` |/ __| |/ / '_ \| | | |
   \ V  V / (_| | |_| | |_) | (_| | (__|   <| |_) | |_| |
    \_/\_/ \__,_|\__, |_.__/ \__,_|\___|_|\_\ .__/ \__, |
                  __/ |                     | |     __/ |
                 |___/                      |_|    |___/
  Python package & CLI tool that interfaces the Wayback Machine APIs
  Repository: https://github.com/akamhy/waybackpy
  Documentation: https://github.com/akamhy/waybackpy/wiki/CLI-docs
  waybackpy - CLI usage(Demo video): https://asciinema.org/a/469890
  Released under the MIT License. Use the flag --license for license.
Options:
  -u, --url TEXT                  URL on which Wayback machine operations are
                                  to be performed.
  -ua, --user-agent, --user_agent TEXT
                                  User agent, default value is 'waybackpy
                                  3.0.6 -
                                  https://github.com/akamhy/waybackpy'.
  -v, --version                   waybackpy version.
  -l, --show-license, --show_license, --license
                                  Show license of Waybackpy.
  -n, -au, --newest, --archive_url, --archive-url
                                  Retrieve the newest archive of URL.
  -o, --oldest                    Retrieve the oldest archive of URL.
  -N, --near                      Archive close to a specified time.
  -Y, --year INTEGER RANGE        Year in integer.  [1994<=x<=9999]
  -M, --month INTEGER RANGE       Month in integer.  [1<=x<=12]
  -D, --day INTEGER RANGE         Day in integer.  [1<=x<=31]
  -H, --hour INTEGER RANGE        Hour in integer.  [0<=x<=24]
  -MIN, --minute INTEGER RANGE    Minute in integer.  [0<=x<=60]
  -s, --save                      Save the specified URL's webpage and print
                                  the archive URL.
  -h, --headers                   Headers data of the SavePageNow API.
  -ku, --known-urls, --known_urls
                                  List known URLs. Uses CDX API.
  -sub, --subdomain               Use with '--known_urls' to include known
                                  URLs for subdomains.
  -f, --file                      Use with '--known_urls' to save the URLs in
                                  file at current directory.
  --cdx                           Flag for using CDX API.
  -st, --start-timestamp, --start_timestamp, --from TEXT
                                  Start timestamp for CDX API in
                                  yyyyMMddhhmmss format.
  -et, --end-timestamp, --end_timestamp, --to TEXT
                                  End timestamp for CDX API in yyyyMMddhhmmss
                                  format.
  -C, --closest TEXT              Archive that are closest the timestamp
                                  passed as arguments to this parameter.
  -f, --cdx-filter, --cdx_filter, --filter TEXT
                                  Filter on a specific field or all the CDX
                                  fields.
  -mt, --match-type, --match_type TEXT
                                  The default behavior is to return matches
                                  for an exact URL. However, the CDX server
                                  can also return results matching a certain
                                  prefix, a certain host, or all sub-hosts by
                                  using the match_type
  -st, --sort TEXT                Choose one from default, closest or reverse.
                                  It returns sorted CDX entries in the
                                  response.
  -up, --use-pagination, --use_pagination
                                  Use the pagination API of the CDX server
                                  instead of the default one.
  -gz, --gzip TEXT                To disable gzip compression pass false as
                                  argument to this parameter. The default
                                  behavior is gzip compression enabled.
  -c, --collapse TEXT             Filtering or 'collapse' results based on a
                                  field, or a substring of a field.
  -l, --limit TEXT                Number of maximum record that CDX API is
                                  asked to return per API call, default value
                                  is 25000 records.
  -cp, --cdx-print, --cdx_print TEXT
                                  Print only certain fields of the CDX API
                                  response, if this parameter is not used then
                                  the plain text response of the CDX API will
                                  be printed.
  --help                          Show this message and exit.
Updated on: 2026-Aug-25
 Edit this page
wapiti
webscarab
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install waybackpy`，再执行 `waybackpy --version` 2>/dev/null || `waybackpy -V`
- [ ] **2.** **读官方帮助** —— `waybackpy -h`，需要细节时 `man waybackpy`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: waybackpy [OPTIONS]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/waybackpy/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/waybackpy/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/waybackpy/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
