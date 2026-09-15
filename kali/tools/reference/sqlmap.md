# sqlmap

> Automatic SQL injection tool sqlmap goal is to detect and take advantage of SQL injection vulnerabilities in web applications. Once it detects one or more SQL injections on the target host, the user can choose among a variety of options to…

> **功能分类**：信息搜集 ｜ **Kali 包**：`sqlmap` ｜ **官方文档**：<https://www.kali.org/tools/sqlmap/>

## 1. 安装

```bash
sudo apt update
sudo apt install sqlmap
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.10.8 |
| 架构 | all |
| 可执行命令 | `sqlmap`、`sqlmapapi` |
| 依赖 | `python3`、`python3-magic` |
| 安装体积 | 12.69 MB |
| 官网 | <https://sqlmap.org/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/sqlmap> |
| 包追踪 | <https://pkg.kali.org/pkg/sqlmap> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sqlmap -h          # 查看用法
man sqlmap         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sqlmap`

> 官方示例调用：`sqlmap -u "http://192.168.1.250/?p=1&forumaction=search" --dbs`

```text
root@kali:~# sqlmap -u "http://192.168.1.250/?p=1&forumaction=search" --dbs
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.2.11#stable}
|_ -| . ["]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org
[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program
[*] starting at 13:37:00
[13:37:00] [INFO] testing connection to the target URL
```

### `sqlmap -h`

> 官方示例调用：`sqlmap -h`

```text
root@kali:~# sqlmap -h
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.10.8#stable}
|_ -| . ["]     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org
Usage: python3 sqlmap [options]
Options:
  -h, --help            Show basic help message and exit
  -hh                   Show advanced help message and exit
  --version             Show program's version number and exit
  -v VERBOSE            Verbosity level: 0-6 (default 1)
  Target:
    At least one of these options has to be provided to define the
    target(s)
    -u URL, --url=URL   Target URL (e.g. "http://www.site.com/vuln.php?id=1")
    -g GOOGLEDORK       Process Google dork results as target URLs
  Request:
    These options can be used to specify how to connect to the target URL
    --data=DATA         Data string to be sent through POST (e.g. "id=1")
    --cookie=COOKIE     HTTP Cookie header value (e.g. "PHPSESSID=a8d127e..")
    --random-agent      Use randomly selected HTTP User-Agent header value
    --proxy=PROXY       Use a proxy to connect to the target URL
    --tor               Use Tor anonymity network
    --check-tor         Check to see if Tor is used properly
  Injection:
    These options can be used to specify which parameters to test for,
    provide custom injection payloads and optional tampering scripts
    -p TESTPARAMETER    Testable parameter(s)
    --dbms=DBMS         Force back-end DBMS to provided value
  Detection:
    These options can be used to customize the detection phase
    --level=LEVEL       Level of tests to perform (1-5, default 1)
    --risk=RISK         Risk of tests to perform (1-3, default 1)
  Techniques:
    These options can be used to tweak testing of specific SQL injection
    techniques
    --technique=TECH..  SQL injection techniques to use (default "BEUSTQ")
  Enumeration:
    These options can be used to enumerate the back-end database
    management system information, structure and data contained in the
    tables
    -a, --all           Retrieve everything
    -b, --banner        Retrieve DBMS banner
    --current-user      Retrieve DBMS current user
    --current-db        Retrieve DBMS current database
    --passwords         Enumerate DBMS users password hashes
    --dbs               Enumerate DBMS databases
    --tables            Enumerate DBMS database tables
    --columns           Enumerate DBMS database table columns
    --schema            Enumerate DBMS schema
    --dump              Dump DBMS database table entries
    --dump-all          Dump entries of all DBMS database tables
    -D DB               DBMS database to enumerate
    -T TBL              DBMS database table(s) to enumerate
    -C COL              DBMS database table column(s) to enumerate
  Operating system access:
    These options can be used to access the back-end database management
    system underlying operating system
    --os-shell          Prompt for an interactive operating system shell
    --os-pwn            Prompt for an OOB shell, Meterpreter or VNC
  General:
    These options can be used to set some general working parameters
    --batch             Never ask for user input, use the default behavior
    --flush-session     Flush session files for current target
  Miscellaneous:
    These options do not fit into any other category
    --wizard            Simple wizard interface for beginner users
[!] to see full list of options run with '-hh'
```

### `sqlmapapi`

> 官方示例调用：`sqlmapapi -h`

```text
root@kali:~# sqlmapapi -h
Usage: sqlmapapi [options]
Options:
  -h, --help            show this help message and exit
  -s, --server          Run as a REST API server
  -c, --client          Run as a REST API client
  -H HOST, --host=HOST  Host of the REST API server (default "127.0.0.1")
  -p PORT, --port=PORT  Port of the REST API server (default 8775)
  --adapter=ADAPTER     Server (bottle) adapter to use (default "wsgiref")
  --database=DATABASE   Set IPC database filepath (optional)
  --username=USERNAME   Basic authentication username
  --password=PASSWORD   Basic authentication password
Learn more with
OffSec
Want to learn more about sqlmap? get access to in-depth training and hands-on labs:
WEB-200: 8.4.1. SQL Injection: SQLMap
PEN-200: 10.3.2. SQL Injection Attacks: Automating the Attack
WEB-200 course
PEN-200 course
Updated on: 2026-Aug-25
 Edit this page
sprayhound
sqlninja
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sqlmap`，再执行 `sqlmap --version` 2>/dev/null || `sqlmap -V`
- [ ] **2.** **读官方帮助** —— `sqlmap -h`，需要细节时 `man sqlmap`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: python3 sqlmap [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sqlmap/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[sqlmap](../../tools/tutorials/03-Web应用/sqlmap.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/initial-access.md`](../../tools/by-attack/initial-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sqlmap/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sqlmap/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
