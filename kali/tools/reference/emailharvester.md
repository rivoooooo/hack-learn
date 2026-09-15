# emailharvester

> Email addresses harvester This package contains EmailHarvester, a tool to retrieve Domain email addresses from Search Engines. Features: Retrieve Domain email addresses from popular Search engines (Google, Bing, Yahoo, ASK, Baidu, Dogpile,…

> **功能分类**：通用工具 ｜ **Kali 包**：`emailharvester` ｜ **官方文档**：<https://www.kali.org/tools/emailharvester/>

## 1. 安装

```bash
sudo apt update
sudo apt install emailharvester
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3.2 |
| 架构 | all |
| 可执行命令 | `emailharvester` |
| 依赖 | `python3`、`python3-colorama`、`python3-requests`、`python3-termcolor`、`python3-validators` |
| 安装体积 | 70 KB |
| 官网 | <https://github.com/maldevel/EmailHarvester> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/emailharvester> |
| 包追踪 | <https://pkg.kali.org/pkg/emailharvester> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
emailharvester -h          # 查看用法
man emailharvester         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `emailharvester`

官方给出的调用示例：`emailharvester -h`

```text
root@kali:~# emailharvester -h
usage: EmailHarvester.py [-h] [-d DOMAIN] [-s FILE] [-e ENGINE] [-l LIMIT]
                         [-u USER-AGENT] [-x PROXY] [--noprint]
                         [-r EXCLUDED_PLUGINS] [-p]
 _____                   _  _   _   _                                _
|  ___|                 (_)| | | | | |                              | |
| |__  _ __ ___    __ _  _ | | | |_| |  __ _  _ __ __   __ ___  ___ | |_  ___  _ __
|  __|| '_ ` _ \  / _` || || | |  _  | / _` || '__|\ \ / // _ \/ __|| __|/ _ \| '__|
| |___| | | | | || (_| || || | | | | || (_| || |    \ V /|  __/\__ \| |_|  __/| |
\____/|_| |_| |_| \__,_||_||_| \_| |_/ \__,_||_|     \_/  \___||___/ \__|\___||_|
    A tool to retrieve Domain email addresses from Search Engines | @maldevel
                                Version: 1.3.2
options:
  -h, --help            show this help message and exit
  -d, --domain DOMAIN   Domain to search.
  -s, --save FILE       Save the results into a TXT and XML file (both).
  -e, --engine ENGINE   Select search engine plugin(eg. '-e google').
  -l, --limit LIMIT     Limit the number of results.
  -u, --user-agent USER-AGENT
                        Set the User-Agent request header.
  -x, --proxy PROXY     Setup proxy server (eg. '-x http://127.0.0.1:8080')
  --noprint             EmailHarvester will print discovered emails to terminal. It is possible to tell EmailHarvester not to print results to terminal with this option.
  -r, --exclude EXCLUDED_PLUGINS
                        Plugins to exclude when you choose 'all' for search engine (eg. '-r google,twitter')
  -p, --list-plugins    List all available plugins.
Updated on: 2026-Mar-02
 Edit this page
donut-shellcode
enum4linux-ng
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install emailharvester`，再执行 `emailharvester --version` 2>/dev/null || `emailharvester -V`
- [ ] **2.** **读官方帮助** —— `emailharvester -h`，需要细节时 `man emailharvester`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `emailharvester -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/emailharvester/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/emailharvester/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/emailharvester/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
