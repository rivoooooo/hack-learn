# slowhttptest

> Application layer Denial of Service attacks simulation tool SlowHTTPTest is a highly configurable tool that simulates some application layer Denial of Service attacks. It implements most common low-bandwidth application layer Denial of Ser…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`slowhttptest` ｜ **官方文档**：<https://www.kali.org/tools/slowhttptest/>

## 1. 安装

```bash
sudo apt update
sudo apt install slowhttptest
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.9.0 |
| 架构 | any |
| 可执行命令 | `slowhttptest` |
| 依赖 | `libc6`、`libgcc-s1`、`libssl3t64`、`libstdc++6` |
| 安装体积 | 89 KB |
| 官网 | <https://github.com/shekyan/slowhttptest> |
| 源码仓库 | <https://salsa.debian.org/debian/slowhttptest> |
| 包追踪 | <https://pkg.kali.org/pkg/slowhttptest> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Use 1000 connections (-c 1000) with the Slowloris mode (-H), and generate statistics (-g> with the output file name (-o slowhttp). Use 10 seconds to wait for data (-i 10), 200 connections (-r 200) with GET requests (-t GET) against the target URL (-u http://192.168.1.202/index.php) with a maximum of length of 24 bytes (-x 24) and a 3 second time out (-p 3):
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `slowhttptest`

> 官方示例调用：`slowhttptest -c 1000 -H -g -o slowhttp -i 10 -r 200 -t GET -u http://192.168.1.202/index.php -x 24 -p 3`

```text
root@kali:~# slowhttptest -c 1000 -H -g -o slowhttp -i 10 -r 200 -t GET -u http://192.168.1.202/index.php -x 24 -p 3
Sat May 17 10:45:26 2014:
Sat May 17 10:45:26 2014:
    slowhttptest version 1.6
 - https://code.google.com/p/slowhttptest/ -
test type:                        SLOW HEADERS
number of connections:            1000
URL:                              http://192.168.1.202/index.php
verb:                             GET
Content-Length header value:      4096
follow up data max size:          52
interval between follow up data:  10 seconds
connections per seconds:          200
probe connection timeout:         3 seconds
test duration:                    240 seconds
using proxy:                      no proxy
Sat May 17 10:45:26 2014:
slow HTTP test status on 0th second:
initializing:        0
pending:             1
connected:           0
error:               0
closed:              0
service available:   YES
```

### `slowhttptest -h`

> 官方示例调用：`slowhttptest -h`

```text
root@kali:~# slowhttptest -h
slowhttptest, a tool to test for slow HTTP DoS vulnerabilities - version 1.9.0
Usage: slowhttptest [options ...]
Test modes:
  -H               slow headers a.k.a. Slowloris (default)
  -B               slow body a.k.a R-U-Dead-Yet
  -R               range attack a.k.a Apache killer
  -X               slow read a.k.a Slow Read
Reporting options:
  -g               generate statistics with socket state changes (off)
  -o file_prefix   save statistics output in file.html and file.csv (-g required)
  -v level         verbosity level 0-4: Fatal, Info, Error, Warning, Debug
General options:
  -c connections   target number of connections (50)
  -i seconds       interval between followup data in seconds (10)
  -l seconds       target test length in seconds (240)
  -r rate          connections per seconds (50)
  -s bytes         value of Content-Length header if needed (4096)
  -t verb          verb to use in request, default to GET for
                   slow headers and response and to POST for slow body
  -u URL           absolute URL of target (http://localhost/)
  -x bytes         max length of each randomized name/value pair of
                   followup data per tick, e.g. -x 2 generates
                   X-xx: xx for header or &xx=xx for body, where x
                   is random character (32)
  -f content-type  value of Content-type header (application/x-www-form-urlencoded)
  -m accept        value of Accept header (text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5)
Probe/Proxy options:
  -d host:port     all traffic directed through HTTP proxy at host:port (off)
  -e host:port     probe traffic directed through HTTP proxy at host:port (off)
  -p seconds       timeout to wait for HTTP response on probe connection,
                   after which server is considered inaccessible (5)
  -j cookies       value of Cookie header (ex.: -j "user_id=1001; timeout=9000")
Range attack specific options:
  -a start        left boundary of range in range header (5)
  -b bytes        limit for range header right boundary values (2000)
Slow read specific options:
  -k num          number of times to repeat same request in the connection. Use to
                  multiply response size if server supports persistent connections (1)
  -n seconds      interval between read operations from recv buffer in seconds (1)
  -w bytes        start of the range advertised window size would be picked from (1)
  -y bytes        end of the range advertised window size would be picked from (512)
  -z bytes        bytes to slow read from receive buffer with single read() call (5)
Updated on: 2025-Dec-09
 Edit this page
slimtoolkit
smbmap
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install slowhttptest`，再执行 `slowhttptest --version` 2>/dev/null || `slowhttptest -V`
- [ ] **2.** **读官方帮助** —— `slowhttptest -h`，需要细节时 `man slowhttptest`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: slowhttptest [options ...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/slowhttptest/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/impact.md`](../../tools/by-attack/impact.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/slowhttptest/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/slowhttptest/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
