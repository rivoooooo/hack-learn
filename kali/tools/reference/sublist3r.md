# sublist3r

> Fast subdomains enumeration tool for penetration testers This package contains a Python security tool designed to enumerate subdomains of websites using OSINT. It helps penetration testers and bug hunters collect and gather subdomains for …

> **功能分类**：通用工具 ｜ **Kali 包**：`sublist3r` ｜ **官方文档**：<https://www.kali.org/tools/sublist3r/>

## 1. 安装

```bash
sudo apt update
sudo apt install sublist3r
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1 |
| 架构 | all |
| 可执行命令 | `sublist3r` |
| 依赖 | `python3` |
| 安装体积 | 1.85 MB |
| 官网 | <https://github.com/aboul3la/Sublist3r> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/sublist3r> |
| 包追踪 | <https://pkg.kali.org/pkg/sublist3r> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
Search for subdomains of kali.org (-d kali.org) using the Bing search engine (-e bing) with 3 threads (-t 3).
root@kali:~# sublist3r -d kali.org -t 3 -e bing

                 ____        _     _ _     _   _____
                / ___| _   _| |__ | (_)___| |_|___ / _ __
                \___ \| | | | '_ \| | / __| __| |_ \| '__|
                 ___) | |_| | |_) | | \__ \ |_ ___) | |
                |____/ \__,_|_.__/|_|_|___/\__|____/|_|

                # Coded By Ahmed Aboul-Ela - @aboul3la

[-] Enumerating subdomains now for kali.org
[-] Searching now in Bing..
[-] Total Unique Subdomains Found: 19
www.kali.org
archive-3.kali.org
archive-4.kali.org
archive-5.kali.org
bugs.kali.org
cdimage.kali.org
docs.kali.org
ar.docs.kali.org
he.docs.kali.org
id.docs.kali.org
tr.docs.kali.org
forums.kali.org
git.kali.org
http.kali.org
images.kali.org
pkg.kali.org
repo.kali.org
security.kali.org
tools.kali.org
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sublist3r`

> 官方示例调用：`sublist3r -d kali.org -t 3 -e bing`

```text
root@kali:~# sublist3r -d kali.org -t 3 -e bing
                 ____        _     _ _     _   _____
                / ___| _   _| |__ | (_)___| |_|___ / _ __
                \___ \| | | | '_ \| | / __| __| |_ \| '__|
                 ___) | |_| | |_) | | \__ \ |_ ___) | |
                |____/ \__,_|_.__/|_|_|___/\__|____/|_|
                # Coded By Ahmed Aboul-Ela - @aboul3la
[-] Enumerating subdomains now for kali.org
[-] Searching now in Bing..
[-] Total Unique Subdomains Found: 19
www.kali.org
archive-3.kali.org
archive-4.kali.org
archive-5.kali.org
bugs.kali.org
cdimage.kali.org
docs.kali.org
ar.docs.kali.org
he.docs.kali.org
id.docs.kali.org
tr.docs.kali.org
forums.kali.org
git.kali.org
http.kali.org
images.kali.org
pkg.kali.org
repo.kali.org
security.kali.org
tools.kali.org
```

### `sublist3r -h`

> 官方示例调用：`sublist3r -h`

```text
root@kali:~# sublist3r -h
usage: sublist3r [-h] -d DOMAIN [-b [BRUTEFORCE]] [-p PORTS] [-v [VERBOSE]]
                 [-t THREADS] [-e ENGINES] [-o OUTPUT] [-n]
OPTIONS:
  -h, --help            show this help message and exit
  -d, --domain DOMAIN   Domain name to enumerate it's subdomains
  -b, --bruteforce [BRUTEFORCE]
                        Enable the subbrute bruteforce module
  -p, --ports PORTS     Scan the found subdomains against specified tcp ports
  -v, --verbose [VERBOSE]
                        Enable Verbosity and display results in realtime
  -t, --threads THREADS
                        Number of threads to use for subbrute bruteforce
  -e, --engines ENGINES
                        Specify a comma-separated list of search engines
  -o, --output OUTPUT   Save the results to text file
  -n, --no-color        Output without color
Example: python3 /usr/bin/sublist3r -d google.com
Updated on: 2026-Mar-02
 Edit this page
ssdeep
thc-pptp-bruter
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sublist3r`，再执行 `sublist3r --version` 2>/dev/null || `sublist3r -V`
- [ ] **2.** **读官方帮助** —— `sublist3r -h`，需要细节时 `man sublist3r`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sublist3r -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sublist3r/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sublist3r/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sublist3r/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
