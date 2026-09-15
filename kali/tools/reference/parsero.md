# parsero

> Robots.txt audit tool Parsero is a free script written in Python which reads the Robots.txt file of a web server and looks at the Disallow entries. The Disallow entries tell the search engines what directories or files hosted on a web serv…

> **功能分类**：通用工具 ｜ **Kali 包**：`parsero` ｜ **官方文档**：<https://www.kali.org/tools/parsero/>

## 1. 安装

```bash
sudo apt update
sudo apt install parsero
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.81~git20140929 |
| 架构 | all |
| 可执行命令 | `parsero` |
| 依赖 | `python3`、`python3-bs4`、`python3-urllib3` |
| 安装体积 | 20 KB |
| 官网 | <https://github.com/behindthefirewalls/Parsero> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/parsero> |
| 包追踪 | <https://pkg.kali.org/pkg/parsero> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Search for results from a website (-u www.bing.com) using Bing indexed Disallows (-sb):
root@kali:~# parsero -u www.bing.com -sb

____
| _ \ __ _ _ __ ___ ___ _ __ ___
| |_) / _` | '__/ __|/ _ \ '__/ _ \
| __/ (_| | | \__ \ __/ | | (_) |
|_| \__,_|_| |___/\___|_| \___/

Starting Parsero v0.75 (https://github.com/behindthefirewalls/Parsero) at 06/09/14 12:48:25
Parsero scan report for www.bing.com
http://www.bing.com/travel/secure 301 Moved Permanently
http://www.bing.com/travel/flight/flightSearchAction 301 Moved Permanently
http://www.bing.com/travel/css 301 Moved Permanently
http://www.bing.com/results 404 Not Found
http://www.bing.com/spbasic 404 Not Found
http://www.bing.com/entities/search 302 Found
http://www.bing.com/translator/? 200 OK
http://www.bing.com/Proxy.ashx 404 Not Found
http://www.bing.com/images/search? 200 OK
http://www.bing.com/travel/hotel/hotelSearch 301 Moved Permanently
http://www.bing.com/static/ 404 Not Found
http://www.bing.com/offers/proxy/dealsserver/api/log 405 Method Not Allowed
http://www.bing.com/shenghuo 301 Moved Permanently
http://www.bing.com/widget/render 200 OK
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `parsero`

> 官方示例调用：`parsero -u www.bing.com -sb`

```text
root@kali:~# parsero -u www.bing.com -sb
____
| _ \ __ _ _ __ ___ ___ _ __ ___
| |_) / _` | '__/ __|/ _ \ '__/ _ \
| __/ (_| | | \__ \ __/ | | (_) |
|_| \__,_|_| |___/\___|_| \___/
Starting Parsero v0.75 (https://github.com/behindthefirewalls/Parsero) at 06/09/14 12:48:25
Parsero scan report for www.bing.com
http://www.bing.com/travel/secure 301 Moved Permanently
http://www.bing.com/travel/flight/flightSearchAction 301 Moved Permanently
http://www.bing.com/travel/css 301 Moved Permanently
http://www.bing.com/results 404 Not Found
http://www.bing.com/spbasic 404 Not Found
http://www.bing.com/entities/search 302 Found
http://www.bing.com/translator/? 200 OK
http://www.bing.com/Proxy.ashx 404 Not Found
http://www.bing.com/images/search? 200 OK
http://www.bing.com/travel/hotel/hotelSearch 301 Moved Permanently
http://www.bing.com/static/ 404 Not Found
http://www.bing.com/offers/proxy/dealsserver/api/log 405 Method Not Allowed
http://www.bing.com/shenghuo 301 Moved Permanently
http://www.bing.com/widget/render 200 OK
```

### `parsero -h`

> 官方示例调用：`parsero -h`

```text
root@kali:~# parsero -h
usage: parsero [-h] [-u URL] [-o] [-sb] [-f FILE]
options:
  -h, --help  show this help message and exit
  -u URL      Type the URL which will be analyzed
  -o          Show only the "HTTP 200" status code
  -sb         Search in Bing indexed Disallows
  -f FILE     Scan a list of domains from a list
Updated on: 2025-Dec-09
 Edit this page
paros
pasco
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install parsero`，再执行 `parsero --version` 2>/dev/null || `parsero -V`
- [ ] **2.** **读官方帮助** —— `parsero -h`，需要细节时 `man parsero`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `parsero -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/parsero/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/parsero/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/parsero/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
