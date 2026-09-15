# siege

> HTTP regression testing and benchmarking utility Siege is an regression test and benchmark utility. It can stress test a single URL with a user defined number of simulated users, or it can read many URLs into memory and stress them simulta…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`siege` ｜ **官方文档**：<https://www.kali.org/tools/siege/>

## 1. 安装

```bash
sudo apt update
sudo apt install siege
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.1.7 |
| 架构 | any |
| 可执行命令 | `siege`、`bombardment`、`siege.config`、`siege2csv` |
| 依赖 | `libc6`、`libssl3t64`、`zlib1g`、`bombardment` |
| 安装体积 | 284 KB |
| 官网 | <https://www.joedog.org/JoeDog/Siege> |
| 源码仓库 | <https://salsa.debian.org/debian/siege> |
| 包追踪 | <https://pkg.kali.org/pkg/siege> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
siege -h          # 查看用法
man siege         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `bombardment`

> 官方示例调用：`bombardment --help`

```text
root@kali:~# bombardment --help
usage:
bombardment [urlfile] [inital # of clients] [inc value] [# of inc] [delay]
```

### `siege`

> 官方示例调用：`siege -h`

```text
root@kali:~# siege -h
Usage: siege [options]
       siege [options] URL
       siege -g URL
Options:
  -V, --version             VERSION, prints the version number.
  -h, --help                HELP, prints this section.
  -C, --config              CONFIGURATION, show the current config.
  -v, --verbose             VERBOSE, prints notification to screen.
  -q, --quiet               QUIET turns verbose off and suppresses output.
  -g, --get                 GET, pull down HTTP headers and display the
                            transaction. Great for application debugging.
  -p, --print               PRINT, like GET only it prints the entire page.
  -c, --concurrent=NUM      CONCURRENT users, default is 10
  -r, --reps=NUM            REPS, number of times to run the test.
  -t, --time=NUMm           TIMED testing where "m" is modifier S, M, or H
                            ex: --time=1H, one hour test.
  -d, --delay=NUM           Time DELAY, random delay before each request
  -b, --benchmark           BENCHMARK: no delays between requests.
  -i, --internet            INTERNET user simulation, hits URLs randomly.
  -f, --file=FILE           FILE, select a specific URLS FILE.
  -R, --rc=FILE             RC, specify an siegerc file
  -l, --log[=FILE]          LOG to FILE. If FILE is not specified, the
                            default is used: /var/log/siege.log
  -m, --mark="text"         MARK, mark the log file with a string.
                            between .001 and NUM. (NOT COUNTED IN STATS)
  -H, --header="text"       Add a header to request (can be many)
  -A, --user-agent="text"   Sets User-Agent in request
  -T, --content-type="text" Sets Content-Type in request
  -j, --json-output         JSON OUTPUT, print final stats to stdout as JSON
      --no-parser           NO PARSER, turn off the HTML page parser
      --no-follow           NO FOLLOW, do not follow HTTP redirects
Copyright (C) 2024 by Jeffrey Fulmer, et al.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.
```

### `siege.config`

> 官方示例调用：`siege.config -h`

```text
root@kali:~# siege.config -h
```

### `man`

> 官方示例调用：`man siege2csv`

```text
root@kali:~# man siege2csv
BOMBARDMENT(1)                     siege2csv                     BOMBARDMENT(1)
NAME
     bombardment - Run siege with an ever-increasing number of users
   SYNOPSIS
     bombardment  [urlfile]  [clients] [increment] [trials] [delay] bombardment
     urls.txt 5 10 20 1
DESCRIPTION
     bombardment is part of the siege distribution. It calls siege with an ini-
     tial number of clients. When that run finishes, it immediately calls siege
     again with that number of clients plus the increment.  It  does  this  the
     number of times specified in the fourth argument.
OPTIONS
     urlfile
         The name of the file containing one or more URLs for siege to test.
     clients
         The initial number of clients to be used on the first run.
     increment
         The number of clients to add to each ensuing run.
     trials
         The number of times to run siege.
     delay
         The is the amount of time, in seconds, that each client will wait
         between requests.  The siege default is overridden by bombardment
SEE ALSO
     siege(1), siege2csv(1)
AUTHOR
     Written by Peter Hutnick, et al.
JoeDog                             2024-11-14                    BOMBARDMENT(1)
Updated on: 2026-May-25
 Edit this page
rsakeyfind
sipsak
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install siege`，再执行 `siege --version` 2>/dev/null || `siege -V`
- [ ] **2.** **读官方帮助** —— `siege -h`，需要细节时 `man siege`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: siege [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/siege/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/impact.md`](../../tools/by-attack/impact.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/siege/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/siege/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
