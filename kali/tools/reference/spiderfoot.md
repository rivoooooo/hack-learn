# spiderfoot

> OSINT collection and reconnaissance tool This package contains an open source intelligence (OSINT) automation tool. Its goal is to automate the process of gathering intelligence about a given target, which may be an IP address, domain name…

> **功能分类**：识别与指纹 ｜ **Kali 包**：`spiderfoot` ｜ **官方文档**：<https://www.kali.org/tools/spiderfoot/>

## 1. 安装

```bash
sudo apt update
sudo apt install spiderfoot
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.0 |
| 架构 | all |
| 可执行命令 | `spiderfoot`、`spiderfoot-cli` |
| 依赖 | `python3`、`python3-adblockparser`、`python3-bs4`、`python3-cherrypy-cors`、`python3-cherrypy3`、`python3-cryptography`、`python3-dnspython`、`python3-docx`、`python3-exifread`、`python3-gexf`、`python3-ipwhois`、`python3-lxml` 等 |
| 安装体积 | 13.73 MB |
| 官网 | <https://www.spiderfoot.net> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/spiderfoot> |
| 包追踪 | <https://pkg.kali.org/pkg/spiderfoot> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
spiderfoot -h          # 查看用法
man spiderfoot         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `spiderfoot`

官方给出的调用示例：`spiderfoot -h`

```text
root@kali:~# spiderfoot -h
usage: sf.py [-h] [-d] [-l IP:port] [-m mod1,mod2,...] [-M] [-C scanID]
             [-s TARGET] [-t type1,type2,...]
             [-u {all,footprint,investigate,passive}] [-T] [-o {tab,csv,json}]
             [-H] [-n] [-r] [-S LENGTH] [-D DELIMITER] [-f]
             [-F type1,type2,...] [-x] [-q] [-V] [-max-threads MAX_THREADS]
SpiderFoot 4.0.0: Open Source Intelligence Automation.
options:
  -h, --help            show this help message and exit
  -d, --debug           Enable debug output.
  -l IP:port            IP and port to listen on.
  -m mod1,mod2,...      Modules to enable.
  -M, --modules         List available modules.
  -C, --correlate scanID
                        Run correlation rules against a scan ID.
  -s TARGET             Target for the scan.
  -t type1,type2,...    Event types to collect (modules selected
                        automatically).
  -u {all,footprint,investigate,passive}
                        Select modules automatically by use case
  -T, --types           List available event types.
  -o {tab,csv,json}     Output format. Tab is default.
  -H                    Don't print field headers, just data.
  -n                    Strip newlines from data.
  -r                    Include the source data field in tab/csv output.
  -S LENGTH             Maximum data length to display. By default, all data
                        is shown.
  -D DELIMITER          Delimiter to use for CSV output. Default is ,.
  -f                    Filter out other event types that weren't requested
                        with -t.
  -F type1,type2,...    Show only a set of event types, comma-separated.
  -x                    STRICT MODE. Will only enable modules that can
                        directly consume your target, and if -t was specified
                        only those events will be consumed by modules. This
                        overrides -t and -m options.
  -q                    Disable logging. This will also hide errors!
  -V, --version         Display the version of SpiderFoot and exit.
  -max-threads MAX_THREADS
                        Max number of modules to run concurrently.
```

### `spiderfoot-cli`

官方给出的调用示例：`spiderfoot-cli -h`

```text
root@kali:~# spiderfoot-cli -h
usage: sfcli.py [-h] [-d] [-s URL] [-u USER] [-p PASS] [-P PASSFILE] [-e FILE]
                [-l FILE] [-n] [-o FILE] [-i] [-q] [-k] [-b]
SpiderFoot: Open Source Intelligence Automation.
options:
  -h, --help   show this help message and exit
  -d, --debug  Enable debug output.
  -s URL       Connect to SpiderFoot server on URL. By default, a connection
               to http://127.0.0.1:5001 will be attempted.
  -u USER      Username to authenticate to SpiderFoot server.
  -p PASS      Password to authenticate to SpiderFoot server. Consider using
               -P PASSFILE instead so that your password isn't visible in your
               shell history or in process lists!
  -P PASSFILE  File containing password to authenticate to SpiderFoot server.
               Ensure permissions on the file are set appropriately!
  -e FILE      Execute commands from FILE.
  -l FILE      Log command history to FILE. By default, history is stored to
               ~/.spiderfoot_history unless disabled with -n.
  -n           Disable history logging.
  -o FILE      Spool commands and output to FILE.
  -i           Allow insecure server connections when using SSL
  -q           Silent output, only errors reported.
  -k           Turn off color-coded output.
  -b, -v       Print the banner w/ version and exit.
Learn more with
OffSec
Want to learn more about spiderfoot? get access to in-depth training and hands-on labs:
SEC-100: 19.2.4. Information Gathering and Enumeration: Automating Information Gathering
SEC-100 course
Updated on: 2026-May-25
 Edit this page
sparrow-wifi
sqlitebrowser
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install spiderfoot`，再执行 `spiderfoot --version` 2>/dev/null || `spiderfoot -V`
- [ ] **2.** **读官方帮助** —— `spiderfoot -h`，需要细节时 `man spiderfoot`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `spiderfoot -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/spiderfoot/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[spiderfoot](../../tools/tutorials/01-信息搜集/spiderfoot.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/spiderfoot/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/spiderfoot/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
