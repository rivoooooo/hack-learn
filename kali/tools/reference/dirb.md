# dirb

> URL bruteforcing tool DIRB is a Web Content Scanner. It looks for existing (and/or hidden) Web Objects. It basically works by launching a dictionary based attack against a web server and analyzing the responses. DIRB comes with a set of pr…

> **功能分类**：Web 应用 ｜ **Kali 包**：`dirb` ｜ **官方文档**：<https://www.kali.org/tools/dirb/>

## 1. 安装

```bash
sudo apt update
sudo apt install dirb
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.22 |
| 架构 | any |
| 可执行命令 | `dirb`、`dirb-gendict`、`html2dic` |
| 依赖 | `libc6`、`libcurl4t64` |
| 安装体积 | 1.44 MB |
| 官网 | <https://dirb.sourceforge.net/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/dirb> |
| 包追踪 | <https://pkg.kali.org/pkg/dirb> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan the web server (http://192.168.1.224/) for directories using a dictionary file (/usr/share/wordlists/dirb/common.txt):
root@kali:~# dirb http://192.168.1.224/ /usr/share/wordlists/dirb/common.txt

-----------------
DIRB v2.21
By The Dark Raver
-----------------

START_TIME: Fri May 16 13:41:45 2014
URL_BASE: http://192.168.1.224/
WORDLIST_FILES: /usr/share/wordlists/dirb/common.txt

-----------------

GENERATED WORDS: 4592

---- Scanning URL: http://192.168.1.224/ ----
==> DIRECTORY: http://192.168.1.224/.svn/
+ http://192.168.1.224/.svn/entries (CODE:200|SIZE:2726)
+ http://192.168.1.224/cgi-bin/ (CODE:403|SIZE:1122)
==> DIRECTORY: http://192.168.1.224/config/
==> DIRECTORY: http://192.168.1.224/docs/
==> DIRECTORY: http://192.168.1.224/external/
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dirb`

> 官方示例调用：`dirb http://192.168.1.224/ /usr/share/wordlists/dirb/common.txt`

```text
root@kali:~# dirb http://192.168.1.224/ /usr/share/wordlists/dirb/common.txt
-----------------
DIRB v2.21
By The Dark Raver
-----------------
START_TIME: Fri May 16 13:41:45 2014
URL_BASE: http://192.168.1.224/
WORDLIST_FILES: /usr/share/wordlists/dirb/common.txt
-----------------
GENERATED WORDS: 4592
---- Scanning URL: http://192.168.1.224/ ----
==> DIRECTORY: http://192.168.1.224/.svn/
+ http://192.168.1.224/.svn/entries (CODE:200|SIZE:2726)
+ http://192.168.1.224/cgi-bin/ (CODE:403|SIZE:1122)
==> DIRECTORY: http://192.168.1.224/config/
==> DIRECTORY: http://192.168.1.224/docs/
==> DIRECTORY: http://192.168.1.224/external/
```

### `man`

> 官方示例调用：`man dirb`

```text
root@kali:~# man dirb
DIRB(1)                     General Commands Manual                     DIRB(1)
NAME
     dirb - Web Content Scanner
SYNOPSIS
     dirb <url_base> <url_base> [<wordlist_file(s)>] [options]
DESCRIPTION
     DIRB  IS  a Web Content Scanner. It looks for existing (and/or hidden) Web
     Objects. It basically  works  by  launching  a  dictionary  basesd  attack
     against a web server and analizing the response.
OPTIONS
     -a <agent_string>
            Specify your custom USER_AGENT.  (Default is: "Mozilla/4.0 (compat-
            ible; MSIE 6.0; Windows NT 5.1)")
     -b     Don't squash or merge sequences of /../ or /./ in the given URL.
     -c <cookie_string>
            Set a cookie for the HTTP request.
     -E <certificate>
            Use the specified client certificate file.
     -f     Fine tunning of NOT_FOUND (404) detection.
     -H <header_string>
            Add a custom header to the HTTP request.
     -i     Use case-insensitive Search.
     -l     Print "Location" header when found.
     -N <nf_code>
            Ignore responses with this HTTP code.
     -o <output_file>
            Save output to disk.
     -p <proxy[:port]>
            Use this proxy. (Default port is 1080)
     -P <proxy_username:proxy_password>
            Proxy Authentication.
     -r     Don't Search Recursively.
     -R     Interactive Recursion.  (Ask in which directories you want to scan)
     -S     Silent Mode. Don't show tested words. (For dumb terminals)
     -t     Don't force an ending '/' on URLs.
     -u <username:password>
            Username and password to use.
     -v     Show Also Not Existent Pages.
     -w     Don't Stop on WARNING messages.
     -x <extensions_file>
            Amplify search with the extensions on this file.
     -X <extensions>
            Amplify search with this extensions.
     -z <milisecs>
            Amplify search with this extensions.
SEE ALSO
     brain(x)
The Dark Raver                     27/01/2009                           DIRB(1)
```

### `dirb-gendict`

> 官方示例调用：`dirb-gendict -h`

```text
root@kali:~# dirb-gendict -h
Usage: dirb-gendict -type pattern
  type: -n numeric [0-9]
        -c character [a-z]
        -C uppercase character [A-Z]
        -h hexa [0-f]
        -a alfanumeric [0-9a-z]
        -s case sensitive alfanumeric [0-9a-zA-Z]
  pattern: Must be an ascii string in which every 'X' character wildcard
           will be replaced with the incremental value.
Example: dirb-gendict -n thisword_X
  thisword_0
  thisword_1
  [...]
  thisword_9
```

### `man html2dic`

> 官方示例调用：`man html2dic`

```text
root@kali:~# man html2dic
HTML2DIC(1)                 General Commands Manual                 HTML2DIC(1)
NAME
     html2dic - Dump word dictionary from html input file
SYNOPSIS
     html2dic <file>
DESCRIPTION
     html2dic  extract  all words from an HTML page, generating a dictionary of
     all word found, one word per line.  Output is printed on stdout.
SEE ALSO
     dirb(1),dirb-gendict(1)
Philippe Thierry                   15/06/2017                       HTML2DIC(1)
Learn more with
OffSec
Want to learn more about dirb? get access to in-depth training and hands-on labs:
WEB-200: 2.2.5. Web Application Enumeration Methodology: Automated HTTP Endpoint Discovery
WEB-200 course
PEN-200 course
Updated on: 2026-May-25
 Edit this page
dhcpig
dnsmap
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dirb`，再执行 `dirb --version` 2>/dev/null || `dirb -V`
- [ ] **2.** **读官方帮助** —— `dirb -h`，需要细节时 `man dirb`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: dirb-gendict -type pattern`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dirb/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[dirb](../../tools/tutorials/03-Web应用/dirb.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dirb/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dirb/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
