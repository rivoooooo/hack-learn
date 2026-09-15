# joomscan

> OWASP Joomla Vulnerability Scanner Project This package contains JoomScan, short for [Joom]la Vulnerability [Scan]ner. It’s a project in perl programming language to detect Joomla CMS vulnerabilities and analysis them.

> **功能分类**：Web 应用 ｜ **Kali 包**：`joomscan` ｜ **官方文档**：<https://www.kali.org/tools/joomscan/>

## 1. 安装

```bash
sudo apt update
sudo apt install joomscan
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0.7 |
| 架构 | all |
| 可执行命令 | `joomscan` |
| 依赖 | `liblwp-protocol-https-perl`、`libregexp-common-perl`、`libwww-perl`、`perl` |
| 安装体积 | 274 KB |
| 官网 | <https://www.owasp.org/index.php/Category:OWASP_Joomla_Vulnerability_Scanner_Project> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/joomscan> |
| 包追踪 | <https://pkg.kali.org/pkg/joomscan> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan the Joomla installation at the given URL (-u http://192.168.1.202/joomla) for vulnerabilities:
root@kali:~# joomscan -u http://localhost/
    ____  _____  _____  __  __  ___   ___    __    _  _
   (_  _)(  _  )(  _  )(  \/  )/ __) / __)  /__\  ( \( )
  .-_)(   )(_)(  )(_)(  )    ( \__ \( (__  /(__)\  )  (
  \____) (_____)(_____)(_/\/\_)(___/ \___)(__)(__)(_)\_)
      (1337.today)

    --=[OWASP JoomScan
    +---++---==[Version : 0.0.5
    +---++---==[Update Date : [2018/03/13]
    +---++---==[Authors : Mohammad Reza Espargham , Ali Razmjoo
    --=[Code name : KLOT
    @OWASP_JoomScan , @rezesp , @Ali_Razmjo0 , @OWASP

Processing http://localhost/ ...



[+] Detecting Joomla Version
[++] Joomla 3.8.6

[+] Core Joomla Vulnerability
[++] Target Joomla core is not vulnerable

[+] Checking Directory Listing
[++] directory has directory listing :
http://localhost/administrator/components
http://localhost/administrator/modules
http://localhost/administrator/templates
http://localhost/images/banners


[+] Checking apache info/status files
[++] Interesting file is found
http://localhost/server-status

[+] admin finder
[++] Admin page : http://localhost/administrator/

[+] Checking robots.txt existing
[++] robots.txt is found
path : http://localhost/robots.txt

Interesting path found from robots.txt
http://localhost/joomla/administrator/
http://localhost/administrator/
http://localhost/bin/
http://localhost/cache/
http://localhost/cli/
http://localhost/components/
http://localhost/includes/
http://localhost/installation/
http://localhost/language/
http://localhost/layouts/
http://localhost/libraries/
http://localhost/logs/
http://localhost/modules/
http://localhost/plugins/
http://localhost/tmp/


[+] Finding common backup files name
[++] Backup files are not found

[+] Finding common log files name
[++] error log is not found

[+] Checking sensitive config.php.x file
[++] Readable config files are not found


Your Report : reports/localhost/
root@kali:~#
root@kali:~# ls /usr/share/joomscan/reports/localhost/
localhost_report_2018-3-19_at_8.37.58.html  localhost_report_2018-3-19_at_8.37.58.txt
root@kali:~#
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `joomscan`

> 官方示例调用：`joomscan -u http://localhost/`

```text
root@kali:~# joomscan -u http://localhost/
    ____  _____  _____  __  __  ___   ___    __    _  _
   (_  _)(  _  )(  _  )(  \/  )/ __) / __)  /__\  ( \( )
  .-_)(   )(_)(  )(_)(  )    ( \__ \( (__  /(__)\  )  (
  \____) (_____)(_____)(_/\/\_)(___/ \___)(__)(__)(_)\_)
      (1337.today)
    --=[OWASP JoomScan
    +---++---==[Version : 0.0.5
    +---++---==[Update Date : [2018/03/13]
    +---++---==[Authors : Mohammad Reza Espargham , Ali Razmjoo
    --=[Code name : KLOT
    @OWASP_JoomScan , @rezesp , @Ali_Razmjo0 , @OWASP
Processing http://localhost/ ...
[+] Detecting Joomla Version
[++] Joomla 3.8.6
[+] Core Joomla Vulnerability
[++] Target Joomla core is not vulnerable
[+] Checking Directory Listing
[++] directory has directory listing :
http://localhost/administrator/components
http://localhost/administrator/modules
http://localhost/administrator/templates
http://localhost/images/banners
[+] Checking apache info/status files
[++] Interesting file is found
http://localhost/server-status
[+] admin finder
[++] Admin page : http://localhost/administrator/
[+] Checking robots.txt existing
[++] robots.txt is found
path : http://localhost/robots.txt
Interesting path found from robots.txt
http://localhost/joomla/administrator/
http://localhost/administrator/
http://localhost/bin/
http://localhost/cache/
http://localhost/cli/
http://localhost/components/
http://localhost/includes/
http://localhost/installation/
http://localhost/language/
http://localhost/layouts/
http://localhost/libraries/
http://localhost/logs/
http://localhost/modules/
http://localhost/plugins/
http://localhost/tmp/
[+] Finding common backup files name
[++] Backup files are not found
[+] Finding common log files name
[++] error log is not found
[+] Checking sensitive config.php.x file
[++] Readable config files are not found
Your Report : reports/localhost/
```

### ``

```text
root@kali:~#
```

### `ls`

> 官方示例调用：`ls /usr/share/joomscan/reports/localhost/`

```text
root@kali:~# ls /usr/share/joomscan/reports/localhost/
localhost_report_2018-3-19_at_8.37.58.html  localhost_report_2018-3-19_at_8.37.58.txt
```

### ``

```text
root@kali:~#
```

### `joomscan -h`

> 官方示例调用：`joomscan -h`

```text
root@kali:~# joomscan -h
    ____  _____  _____  __  __  ___   ___    __    _  _
   (_  _)(  _  )(  _  )(  \/  )/ __) / __)  /__\  ( \( )
  .-_)(   )(_)(  )(_)(  )    ( \__ \( (__  /(__)\  )  (
  \____) (_____)(_____)(_/\/\_)(___/ \___)(__)(__)(_)\_)
			(1337.today)
    --=[OWASP JoomScan
    +---++---==[Version : 0.0.7
    +---++---==[Update Date : [2018/09/23]
    +---++---==[Authors : Mohammad Reza Espargham , Ali Razmjoo
    --=[Code name : Self Challenge
    @OWASP_JoomScan , @rezesp , @Ali_Razmjo0 , @OWASP
Help :
Usage:	joomscan [options]
--url | -u <URL>                |   The Joomla URL/domain to scan.
--enumerate-components | -ec    |   Try to enumerate components.
--cookie <String>               |   Set cookie.
--user-agent | -a <User-Agent>  |   Use the specified User-Agent.
--random-agent | -r             |   Use a random User-Agent.
--timeout <Time-Out>            |   Set timeout.
--proxy=PROXY                   |   Use a proxy to connect to the target URL
           Proxy example: --proxy http://127.0.0.1:8080
                                  https://127.0.0.1:443
                                  socks://127.0.0.1:414
--about                         |   About Author
--help | -h                     |   This help screen.
--version                       |   Output the current version and exit.
Learn more with
OffSec
Want to learn more about joomscan? get access to in-depth training and hands-on labs:
Introduction to Vulnerability Tracking: 2.4. Scanning for Web Vulnerabilities
Updated on: 2025-Dec-09
 Edit this page
johnny
kali-autopilot
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install joomscan`，再执行 `joomscan --version` 2>/dev/null || `joomscan -V`
- [ ] **2.** **读官方帮助** —— `joomscan -h`，需要细节时 `man joomscan`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:	joomscan [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/joomscan/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/joomscan/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/joomscan/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
