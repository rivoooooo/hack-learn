# wafw00f

> Identify and fingerprint Web Application Firewall products This package identifies and fingerprints Web Application Firewall (WAF) products using the following logic: Sends a normal HTTP request and analyses the response; this identifies a

> **功能分类**：信息搜集 ｜ **Kali 包**：`wafw00f` ｜ **官方文档**：<https://www.kali.org/tools/wafw00f/>

## 1. 安装

```bash
sudo apt update
sudo apt install wafw00f
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.4.2 |
| 架构 | all |
| 可执行命令 | `wafw00f` |
| 依赖 | `python3`、`python3-requests` |
| 安装体积 | 265 KB |
| 官网 | <https://github.com/EnableSecurity/wafw00f> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/wafw00f> |
| 包追踪 | <https://pkg.kali.org/pkg/wafw00f> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
wafw00f -h          # 查看用法
man wafw00f         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wafw00f`

官方给出的调用示例：`wafw00f -h`

```text
root@kali:~# wafw00f -h
Usage: wafw00f url1 [url2 [url3 ... ]]
example: wafw00f http://www.victim.org/
Options:
  -h, --help            show this help message and exit
  -v, --verbose         Enable verbosity, multiple -v options increase
                        verbosity
  -a, --findall         Find all WAFs which match the signatures, do not stop
                        testing on the first one
  -r, --noredirect      Do not follow redirections given by 3xx responses
  -t TEST, --test=TEST  Test for one specific WAF (use --list to get names,
                        quote names with spaces e.g. "AireeCDN (Airee)")
  -o OUTPUT, --output=OUTPUT
                        Write output to csv, json or text file depending on
                        file extension. For stdout, specify - as filename.
  -f FORMAT, --format=FORMAT
                        Force output format to csv, json or text.
  -i INPUT, --input-file=INPUT
                        Read targets from a file. Input format can be csv,
                        json or text. For csv and json, a `url` column name or
                        element is required.
  -l, --list            List all WAFs that WAFW00F is able to detect
  -p PROXY, --proxy=PROXY
                        Use an HTTP proxy to perform requests, examples:
                        http://hostname:8080, socks5://hostname:1080,
                        http://user:pass@hostname:8080
  -V, --version         Print out the current version of WafW00f and exit.
  -H HEADERS, --headers=HEADERS
                        Pass custom headers via a text file to overwrite the
                        default header set.
  -T TIMEOUT, --timeout=TIMEOUT
                        Set the timeout for the requests.
  --no-colors           Disable ANSI colors in output.
Updated on: 2026-May-25
 Edit this page
vinetto
websploit
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install wafw00f`，再执行 `wafw00f --version` 2>/dev/null || `wafw00f -V`
- [ ] **2.** **读官方帮助** —— `wafw00f -h`，需要细节时 `man wafw00f`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: wafw00f url1 [url2 [url3 ... ]]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wafw00f/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[wafw00f](../../tools/tutorials/03-Web应用/wafw00f.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wafw00f/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wafw00f/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
