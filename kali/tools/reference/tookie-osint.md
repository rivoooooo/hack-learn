# tookie-osint

> OSINT information gathering tool for finding social media accounts Tookie-osint has a simple-to-use UI and is really straightforward. The main idea of Tookie-osint is to discover usernames that are requested from an input. Tookie-osint is …

> **功能分类**：通用工具 ｜ **Kali 包**：`tookie-osint` ｜ **官方文档**：<https://www.kali.org/tools/tookie-osint/>

## 1. 安装

```bash
sudo apt update
sudo apt install tookie-osint
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.1fix |
| 架构 | all |
| 可执行命令 | `tookie-osint` |
| 依赖 | `chromium-driver`、`python3`、`python3-colorama`、`python3-requests`、`python3-selenium`、`python3-webdriver-manager` |
| 安装体积 | 1.12 MB |
| 官网 | <https://github.com/Alfredredbird/tookie-osint> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/tookie-osint> |
| 包追踪 | <https://pkg.kali.org/pkg/tookie-osint> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
tookie-osint -h          # 查看用法
man tookie-osint         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tookie-osint`

> 官方示例调用：`tookie-osint -h`

```text
root@kali:~# tookie-osint -h
usage: tookie-osint [-h] (-u USER | -U USERFILE) [-t THREADS] [-d] [-sk]
                    [-p PROXY] [-W] [-o {txt,csv,json}] [-D DELAY] [-a] [-H]
Username OSINT scanner
options:
  -h, --help            show this help message and exit
  -u, --user USER       Username to scan
  -U, --userfile USERFILE
                        File path to username file
  -t, --threads THREADS
                        Threads. Defualt is 2
  -d, --debug           Allows debugging options
  -sk, --skipheaders    skips using random user agents
  -p, --proxy PROXY     proxy
  -W, --webscraper      Toggles uses the webscraper
  -o, --output {txt,csv,json}
                        Output format (txt, csv, json)
  -D, --delay DELAY     Delay webscraper should wait for the page to load
  -a, --all             Show all results (positive and negative)
  -H, --harvest         Webscrape data from the sites
Examples:
  Basic scan (default txt output):
    tookie-osint -u alfred
  JSON output with 10 threads:
    tookie-osint -u alfred -o json -t 10
  Scan usernames from a file:
    tookie-osint -U users.txt -o csv
  Use proxy and show all results:
    tookie-osint -u alfred -p http://127.0.0.1:8080 -a
  Skip random headers:
    tookie-osint -u alfred --skipheaders
  Use webscraper:
    tookie-osint -u alfred -W -H
  Use a user file list
    tookie-osint -U users.txt -t 20
Updated on: 2026-Jun-17
 Edit this page
tailscale
udptunnel
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install tookie-osint`，再执行 `tookie-osint --version` 2>/dev/null || `tookie-osint -V`
- [ ] **2.** **读官方帮助** —— `tookie-osint -h`，需要细节时 `man tookie-osint`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `tookie-osint -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/tookie-osint/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/tookie-osint/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/tookie-osint/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
