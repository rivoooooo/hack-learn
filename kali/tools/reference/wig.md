# wig

> WebApp Information Gatherer This package contains a web application information gathering tool, which can identify numerous Content Management Systems and other administrative applications. The application fingerprinting is based on checks…

> **功能分类**：通用工具 ｜ **Kali 包**：`wig` ｜ **官方文档**：<https://www.kali.org/tools/wig/>

## 1. 安装

```bash
sudo apt update
sudo apt install wig
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.6 |
| 架构 | all |
| 可执行命令 | `wig` |
| 依赖 | `python3` |
| 安装体积 | 6.36 MB |
| 官网 | <https://github.com/jekyc/wig> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/wig> |
| 包追踪 | <https://pkg.kali.org/pkg/wig> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
wig -h          # 查看用法
man wig         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wig`

官方给出的调用示例：`wig -h`

```text
root@kali:~# wig -h
usage: wig [-h] [-l INPUT_FILE] [-q] [-n STOP_AFTER] [-a] [-m] [-u] [-d]
           [-t THREADS] [--no_cache_load] [--no_cache_save] [-N] [--verbosity]
           [--proxy PROXY] [-w OUTPUT_FILE]
           [url]
WebApp Information Gatherer
positional arguments:
  url              The url to scan e.g. http://example.com
options:
  -h, --help       show this help message and exit
  -l INPUT_FILE    File with urls, one per line.
  -q               Set wig to not prompt for user input during run
  -n STOP_AFTER    Stop after this amount of CMSs have been detected. Default:
                   1
  -a               Do not stop after the first CMS is detected
  -m               Try harder to find a match without making more requests
  -u               User-agent to use in the requests
  -d               Disable the search for subdomains
  -t THREADS       Number of threads to use
  --no_cache_load  Do not load cached responses
  --no_cache_save  Do not save the cache for later use
  -N               Shortcut for --no_cache_load and --no_cache_save
  --verbosity, -v  Increase verbosity. Use multiple times for more info
  --proxy PROXY    Tunnel through a proxy (format: localhost:8080)
  -w OUTPUT_FILE   File to dump results into (JSON)
Updated on: 2026-May-25
 Edit this page
whatweb
wordlists
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install wig`，再执行 `wig --version` 2>/dev/null || `wig -V`
- [ ] **2.** **读官方帮助** —— `wig -h`，需要细节时 `man wig`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `wig -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wig/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wig/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wig/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
