# recon-ng

> Web Reconnaissance framework written in Python Recon-ng is a full-featured Web Reconnaissance framework written in Python. Complete with independent modules, database interaction, built in convenience functions, interactive help, and comma…

> **功能分类**：信息搜集 ｜ **Kali 包**：`recon-ng` ｜ **官方文档**：<https://www.kali.org/tools/recon-ng/>

## 1. 安装

```bash
sudo apt update
sudo apt install recon-ng
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.1.2 |
| 架构 | all |
| 可执行命令 | `recon-ng`、`recon-cli`、`recon-web` |
| 依赖 | `libjs-jquery`、`libjs-skeleton`、`node-normalize.css`、`python3`、`python3-dicttoxml`、`python3-dnspython`、`python3-flasgger`、`python3-flask`、`python3-flask-restful`、`python3-lxml`、`python3-mechanize`、`python3-redis` 等 |
| 安装体积 | 271 KB |
| 官网 | <https://github.com/lanmaster53/recon-ng> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/recon-ng> |
| 包追踪 | <https://pkg.kali.org/pkg/recon-ng> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Search for results on xssed.com (use recon/domains-vulnerabilities/xssed) for the target domain (set SOURCE cisco.com):
root@kali:~# recon-ng

    _/_/_/    _/_/_/_/    _/_/_/    _/_/_/    _/      _/            _/      _/    _/_/_/
   _/    _/  _/        _/        _/      _/  _/_/    _/            _/_/    _/  _/
  _/_/_/    _/_/_/    _/        _/      _/  _/  _/  _/  _/_/_/_/  _/  _/  _/  _/  _/_/_/
 _/    _/  _/        _/        _/      _/  _/    _/_/            _/    _/_/  _/      _/
_/    _/  _/_/_/_/    _/_/_/    _/_/_/    _/      _/            _/      _/    _/_/_/


                                          /\
                                         / \\ /\
        Sponsored by...           /\  /\/  \\V  \/\
                                 / \\/ // \\\\\ \\ \/\
                                // // BLACK HILLS \/ \\
                               www.blackhillsinfosec.com

                      [recon-ng v4.9.4, Tim Tomes (@LaNMaSteR53)]

[76] Recon modules
[8]  Reporting modules
[2]  Import modules
[2]  Exploitation modules
[2]  Discovery modules

[recon-ng][default] > use recon/domains-vulnerabilities/xssed
[recon-ng][default][xssed] > set SOURCE cisco.com
SOURCE => cisco.com
[recon-ng][default][xssed] > run

---------
CISCO.COM
---------
[*] Category: Redirect
[*] Example: http://www.cisco.com/survey/exit.html?http://xssed.com/
[*] Host: www.cisco.com
[*] Reference: http://xssed.com/mirror/76478/
[*] Status: unfixed
[*] --------------------------------------------------
[*] Category: XSS
[*] Example: http://developer.cisco.com/web/webdialer/wikidocs?p_p_id=1_WAR_wikinavigationportlet_INSTANCE_veD7&p<br>_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&p_r_p_185834411_no<br>deId=803209&p_r_p_185834411_title=%22%3E%3Ch1%3ECross-Site%20Scripting%20@matiaslonigro%3C/h1%3E%3Cs<br>cript%3Ealert%28/xss/%29%3C/script%3E
[*] Host: developer.cisco.com
[*] Reference: http://xssed.com/mirror/76294/
[*] Status: unfixed
[...]
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `recon-ng`

```text
root@kali:~# recon-ng
    _/_/_/    _/_/_/_/    _/_/_/    _/_/_/    _/      _/            _/      _/    _/_/_/
   _/    _/  _/        _/        _/      _/  _/_/    _/            _/_/    _/  _/
  _/_/_/    _/_/_/    _/        _/      _/  _/  _/  _/  _/_/_/_/  _/  _/  _/  _/  _/_/_/
 _/    _/  _/        _/        _/      _/  _/    _/_/            _/    _/_/  _/      _/
_/    _/  _/_/_/_/    _/_/_/    _/_/_/    _/      _/            _/      _/    _/_/_/
                                          /\
                                         / \\ /\
        Sponsored by...           /\  /\/  \\V  \/\
                                 / \\/ // \\\\\ \\ \/\
                                // // BLACK HILLS \/ \\
                               www.blackhillsinfosec.com
                      [recon-ng v4.9.4, Tim Tomes (@LaNMaSteR53)]
[76] Recon modules
[8]  Reporting modules
[2]  Import modules
[2]  Exploitation modules
[2]  Discovery modules
[recon-ng][default] > use recon/domains-vulnerabilities/xssed
[recon-ng][default][xssed] > set SOURCE cisco.com
SOURCE => cisco.com
[recon-ng][default][xssed] > run
---------
CISCO.COM
---------
[*] Category: Redirect
[*] Example: http://www.cisco.com/survey/exit.html?http://xssed.com/
[*] Host: www.cisco.com
[*] Reference: http://xssed.com/mirror/76478/
[*] Status: unfixed
[*] --------------------------------------------------
[*] Category: XSS
[*] Example: http://developer.cisco.com/web/webdialer/wikidocs?p_p_id=1_WAR_wikinavigationportlet_INSTANCE_veD7&p<br>_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&p_r_p_185834411_no<br>deId=803209&p_r_p_185834411_title=%22%3E%3Ch1%3ECross-Site%20Scripting%20@matiaslonigro%3C/h1%3E%3Cs<br>cript%3Ealert%28/xss/%29%3C/script%3E
[*] Host: developer.cisco.com
[*] Reference: http://xssed.com/mirror/76294/
[*] Status: unfixed
[...]
```

### `recon-cli`

> 官方示例调用：`recon-cli -h`

```text
root@kali:~# recon-cli -h
usage: recon-cli [-h] [-w workspace] [-C command] [-c command] [-G]
                 [-g name=value] [-M] [-m module] [-O] [-o name=value] [-x]
                 [--no-version] [--no-analytics] [--no-marketplace]
                 [--stealth] [--version] [--analytics]
recon-cli - Tim Tomes (@lanmaster53)
options:
  -h, --help        show this help message and exit
  -w workspace      load/create a workspace
  -C command        runs a command at the global context
  -c command        runs a command at the module context (pre-run)
  -G                show available global options
  -g name=value     set a global option (can be used more than once)
  -M                show modules
  -m module         specify the module
  -O                show available module options
  -o name=value     set a module option (can be used more than once)
  -x                run the module
  --no-version      disable version check. Already disabled by default in
                    Debian
  --no-analytics    disable analytics reporting. Already disabled by default
                    in Debian
  --no-marketplace  disable remote module management
  --stealth         disable all passive requests (--no-*)
  --version         displays the current version
  --analytics       enable analytics reporting. Send analytics to google
```

### `recon-ng -h`

> 官方示例调用：`recon-ng -h`

```text
root@kali:~# recon-ng -h
usage: recon-ng [-h] [-w workspace] [-r filename] [--no-version]
                [--no-analytics] [--no-marketplace] [--stealth] [--accessible]
                [--version]
recon-ng - Tim Tomes (@lanmaster53)
options:
  -h, --help        show this help message and exit
  -w workspace      load/create a workspace
  -r filename       load commands from a resource file
  --no-version      disable version check. Already disabled by default in
                    Debian
  --no-analytics    disable analytics reporting. Already disabled by default
                    in Debian
  --no-marketplace  disable remote module management
  --stealth         disable all passive requests (--no-*)
  --accessible      Use accessible outputs when available
  --version         displays the current version
```

### `recon-web`

> 官方示例调用：`recon-web -h`

```text
root@kali:~# recon-web -h
*************************************************************************
 * Welcome to Recon-web, the analytics and reporting engine for Recon-ng!
 * This is a web-based user interface. Open the URL below in your browser to begin.
 * Recon-web includes the Recon-API, which can be accessed via the `/api/` URL.
*************************************************************************
[*] Marketplace disabled.
[*] Version check disabled.
 * Workspace initialized: default
usage: recon-web [-h] [--host HOST] [--port PORT]
options:
  -h, --help   show this help message and exit
  --host HOST  IP address to listen on
  --port PORT  port to bind the web server to
Updated on: 2025-Dec-09
 Edit this page
rcracki-mt
reconspider
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install recon-ng`，再执行 `recon-ng --version` 2>/dev/null || `recon-ng -V`
- [ ] **2.** **读官方帮助** —— `recon-ng -h`，需要细节时 `man recon-ng`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `recon-ng -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/recon-ng/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[recon-ng](../../tools/tutorials/01-信息搜集/recon-ng.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/recon-ng/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/recon-ng/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
