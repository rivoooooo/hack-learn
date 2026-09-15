# httprint

> Web server fingerprinting tool httprint is a web server fingerprinting tool. It relies on web server characteristics to accurately identify web servers, despite the fact that they may have been obfuscated by changing the server banner stri…

> **功能分类**：Web 应用 ｜ **Kali 包**：`httprint` ｜ **官方文档**：<https://www.kali.org/tools/httprint/>

## 1. 安装

```bash
sudo apt update
sudo apt install httprint
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.301 |
| 架构 | i386 |
| 可执行命令 | `httprint` |
| 安装体积 | 1.45 MB |
| 官网 | <https://www.net-square.com/httprint.html> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/httprint> |
| 包追踪 | <https://pkg.kali.org/pkg/httprint> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
httprint -h          # 查看用法
man httprint         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `httprint`

官方给出的调用示例：`httprint -h`

```text
root@kali:~# httprint -h
httprint v0.301 (beta) - web server fingerprinting tool
(c) 2003-2005 net-square solutions pvt. ltd. - see readme.txt
http://net-square.com/httprint/
[email protected]
Usage:
httprint {-h <host> | -i <input file> | -x <nmap xml file>} -s <signatures> [... options]
-h <host>            host can be either an IP address, a symbolic name,
                     an IP range or a URL.
-i <input text file> file containing list of hosts as described above
                     in text format.
-x <nmap xml file>   Nmap -oX option generated xml file as input file.
                     Ports which can be considered as http ports are taken
                     from the nmapportlist.txt file.
-s <signatures>      file containing http fingerprint signatures.
Options:
-o <output file>     output in html format.
-oc <output file>    output in csv format.
-ox <output file>    output in xml format.
-noautossl           Disable automatic detection of SSL.
-tp <ping timeout>   Ping timeout in milliseconds.
                     Default is 4000 ms. Maximum 30000 ms.
-ct <1-100>          Default is 75. Do not change.
-ua <User Agent>     Default is Mozilla/4.0 (compatible; MSIE 5.01;
                     Windows NT 5.0.
-t <timeout>         Connection/read timeout in milliseconds.
                     Default is 10000 ms. Maximum 100000 ms.
-r <retry>           Number of retries. Default is 3. Maximum 30.
-P0                  Turn ICMP ping off.
-nr                  No redirection. Do not automatically follow 301,
                     302 responses. Enabled by default.
-th <threads>        Number of threads. Default is 8. Maximum 64.
-?                   Displays this message.
Examples:
httprint -h www1.example.com -s signatures.txt
httprint -h https://www2.example.com/ -s signatures.txt
httprint -h http://www3.example.com:8080/ -s signatures.txt
httprint -h www1.example.com -s signatures.txt -noautossl
httprint -h 10.0.1.1-10.0.1.254 -s signatures.txt -o 10_0_1_x.html
httprint -x nmap.xml -s signatures.txt -oc report.csv
httprint -x nmap.xml -s signatures.txt -ox report.xml
httprint -i input.txt -s signatures.txt -o output.html -th 16
Updated on: 2025-Dec-09
 Edit this page
htshells
httprobe
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install httprint`，再执行 `httprint --version` 2>/dev/null || `httprint -V`
- [ ] **2.** **读官方帮助** —— `httprint -h`，需要细节时 `man httprint`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/httprint/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/httprint/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/httprint/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
