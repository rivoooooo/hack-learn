# xsstrike

> Most advanced XSS scanner XSStrike is a Cross Site Scripting detection suite equipped with four hand written parsers, an intelligent payload generator, a powerful fuzzing engine and an incredibly fast crawler.

> **功能分类**：通用工具 ｜ **Kali 包**：`xsstrike` ｜ **官方文档**：<https://www.kali.org/tools/xsstrike/>

## 1. 安装

```bash
sudo apt update
sudo apt install xsstrike
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.1.6 |
| 架构 | any |
| 可执行命令 | `xsstrike` |
| 依赖 | `python3`、`python3-fuzzywuzzy`、`python3-requests`、`python3-tld` |
| 安装体积 | 179 KB |
| 官网 | <https://github.com/s0md3v/XSStrike> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/xsstrike> |
| 包追踪 | <https://pkg.kali.org/pkg/xsstrike> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
xsstrike -h          # 查看用法
man xsstrike         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `xsstrike`

> 官方示例调用：`xsstrike -h`

```text
root@kali:~# xsstrike -h
	XSStrike v3.1.5
usage: xsstrike.py [-h] [-u TARGET] [--data PARAMDATA] [-e ENCODE] [--fuzzer]
                   [--update] [--timeout TIMEOUT] [--proxy] [--crawl] [--json]
                   [--path] [--seeds ARGS_SEEDS] [-f ARGS_FILE] [-l LEVEL]
                   [--headers [ADD_HEADERS]] [-t THREADCOUNT] [-d DELAY]
                   [--skip] [--skip-dom] [--blind]
                   [--console-log-level {DEBUG,INFO,RUN,GOOD,WARNING,ERROR,CRITICAL,VULN}]
                   [--file-log-level {DEBUG,INFO,RUN,GOOD,WARNING,ERROR,CRITICAL,VULN}]
                   [--log-file LOG_FILE]
options:
  -h, --help            show this help message and exit
  -u, --url TARGET      url
  --data PARAMDATA      post data
  -e, --encode ENCODE   encode payloads
  --fuzzer              fuzzer
  --update              update
  --timeout TIMEOUT     timeout
  --proxy               use prox(y|ies)
  --crawl               crawl
  --json                treat post data as json
  --path                inject payloads in the path
  --seeds ARGS_SEEDS    load crawling seeds from a file
  -f, --file ARGS_FILE  load payloads from a file
  -l, --level LEVEL     level of crawling
  --headers [ADD_HEADERS]
                        add headers
  -t, --threads THREADCOUNT
                        number of threads
  -d, --delay DELAY     delay between requests
  --skip                don't ask to continue
  --skip-dom            skip dom checking
  --blind               inject blind XSS payload while crawling
  --console-log-level {DEBUG,INFO,RUN,GOOD,WARNING,ERROR,CRITICAL,VULN}
                        Console logging level
  --file-log-level {DEBUG,INFO,RUN,GOOD,WARNING,ERROR,CRITICAL,VULN}
                        File logging level
  --log-file LOG_FILE   Name of the file to log
Updated on: 2026-Jun-19
 Edit this page
phishery
arjun
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install xsstrike`，再执行 `xsstrike --version` 2>/dev/null || `xsstrike -V`
- [ ] **2.** **读官方帮助** —— `xsstrike -h`，需要细节时 `man xsstrike`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `xsstrike -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/xsstrike/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/xsstrike/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/xsstrike/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
