# wifipumpkin3

> Powerful framework for rogue access point attack This package contains a powerful framework for rogue access point attack, written in Python, that allow and offer to security researchers, red teamers and reverse engineers to mount a wirele…

> **功能分类**：通用工具 ｜ **Kali 包**：`wifipumpkin3` ｜ **官方文档**：<https://www.kali.org/tools/wifipumpkin3/>

## 1. 安装

```bash
sudo apt update
sudo apt install wifipumpkin3
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1.7 |
| 架构 | all |
| 可执行命令 | `wifipumpkin3`、`captiveflask`、`evilqr3`、`phishkin3`、`sslstrip3`、`wp3` |
| 依赖 | `hostapd`、`iptables`、`iw`、`net-tools`、`python3`、`python3-aiofiles`、`python3-bs4`、`python3-dhcplib`、`python3-dnslib`、`python3-dnspython`、`python3-flask`、`python3-flask-restful` 等 |
| 安装体积 | 29.24 MB |
| 官网 | <https://github.com/P0cL4bs/wifipumpkin3> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/wifipumpkin3> |
| 包追踪 | <https://pkg.kali.org/pkg/wifipumpkin3> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
wifipumpkin3 -h          # 查看用法
man wifipumpkin3         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 6 个可执行命令，下面是官方页面内嵌的帮助原文。

### `captiveflask`

官方给出的调用示例：`captiveflask -h`

```text
root@kali:~# captiveflask -h
[*] CaptiveFlask v1.0.2 - subtool from wifipumpkin3
usage: captiveflask [-h] [-t TEMPLATE] [-s STATIC] [-r REDIRECT] [-p PORT]
                    [-rU REDIRECT_URL] [-f FORCE_REDIRECT] [-v VERSION]
CaptiveFlask - Server to create captive portal with flask doc:
https://github.com/mh4x0f/captiveportals
options:
  -h, --help            show this help message and exit
  -t, --tamplate TEMPLATE
                        path the theme login captive portal
  -s, --static STATIC   path of the static files from webpage
  -r, --redirect REDIRECT
                        IpAddress from gataway captive portal
  -p, --port PORT       The port for captive portal
  -rU, --redirect-url REDIRECT_URL
                        Url for redirect after user insert the credentials on
                        captive portal
  -f, --force-login_successful-template FORCE_REDIRECT
                        force redirect to login_successful.html template
  -v, --version VERSION
                        show version the tool
```

### `evilqr3`

官方给出的调用示例：`evilqr3 -h`

```text
root@kali:~# evilqr3 -h
[*] EvilQR3 v0.0.1 - subtool from wifipumpkin3
usage: evilqr3 [-h] -t TEMPLATE -s STATIC [-p PORT] [-rU REDIRECT_URL]
               -sa SERVER_ADDRESS -mu MATCH_USERAGENT -tp TOKEN_API [-d DEBUG]
               [-v VERSION]
EvilQR3 -
options:
  -h, --help            show this help message and exit
  -t, --tamplate TEMPLATE
                        path the theme login captive portal
  -s, --static STATIC   path of the static files from webpage
  -p, --port PORT       The port for captive portal
  -rU, --redirect-url REDIRECT_URL
                        Url for redirect after user insert the credentials on
                        captive portal
  -sa, --server-address SERVER_ADDRESS
                        IpAddress from gataway captive portal
  -mu, --match-useragent MATCH_USERAGENT
                        IpAddress from gataway captive portal
  -tp, --token-api TOKEN_API
                        The token API for make request with security
  -d, --debug DEBUG     Enable debug mode
  -v, --version VERSION
                        show version the tool
```

### `phishkin3`

官方给出的调用示例：`phishkin3 -h`

```text
root@kali:~# phishkin3 -h
[*] phishkin3 v1.0.2 - subtool from wifipumpkin3
usage: phishkin3 [-h] [-r REDIRECT] [-p PORT] [-cU CLOUD_URL]
                 [-rU REDIRECT_URL] [-v VERSION]
phishkin3 - Server to create captive portal with external phishing page doc:
options:
  -h, --help            show this help message and exit
  -r, --redirect REDIRECT
                        IpAddress from gataway captive portal
  -p, --port PORT       The port for captive portal
  -cU, --cloud-url-phishing CLOUD_URL
                        cloud url phishing domain page
  -rU, --redirect-url REDIRECT_URL
                        Url for redirect after user insert the credentials on
                        phishing page
  -v, --version VERSION
                        show version the tool
```

### `sslstrip3`

官方给出的调用示例：`sslstrip3 -h`

```text
root@kali:~# sslstrip3 -h
sslstrip 0.9 by Moxie Marlinspike (mh4x0f)
Fork: https://github.com/mh4x0f/sslstrip3
Usage: sslstrip <options>
Options:
-w <filename>, --write=<filename> Specify file to log to (optional).
-p , --post                       Log only SSL POSTs. (default)
-s , --ssl                        Log all SSL traffic to and from server.
-a , --all                        Log all SSL and HTTP traffic to and from server.
-l <port>, --listen=<port>        Port to listen on (default 10000).
-f , --favicon                    Substitute a lock favicon on secure requests.
-k , --killsessions               Kill sessions in progress.
-t <config>, --tamper <config>    Enable response tampering with settings from <config>.
-i , --inject                     Inject code into HTML pages using a text file.
-h                                print(this help message.
```

### `wifipumpkin3`

官方给出的调用示例：`wifipumpkin3 -h`

```text
root@kali:~# wifipumpkin3 -h
usage: wifipumpkin3 [-h] [-i INTERFACE] [-iNet INTERFACE_NET] [-s SESSION]
                    [-p PULP] [-x XPULP] [-m WIRELESS_MODE] [--no-colors]
                    [--rest] [--restport RESTPORT] [--username USERNAME]
                    [--password PASSWORD] [-iNM IG_NETWORKMANAGER]
                    [-rNM RM_NETWORKMANAGER] [-v]
wifipumpkin3 - Powerful framework for rogue access point attack. See:
https://wifipumpkin3.github.io/docs/getting-started#usage
options:
  -h, --help            show this help message and exit
  -i INTERFACE          set interface for create AP
  -iNet INTERFACE_NET   set interface for share internet to AP
  -s SESSION            set session for continue attack
  -p, --pulp PULP       interactive sessions can be scripted with .pulp file
  -x, --xpulp XPULP     interactive sessions can be string with ";" as the
                        separator
  -m, --wireless-mode WIRELESS_MODE
                        set wireless mode settings
  --no-colors           disable terminal colors and effects.
  --rest                Run the Wp3 RESTful API.
  --restport RESTPORT   Port to run the Wp3 RESTful API on. default is 1337
  --username USERNAME   Start the RESTful API with the specified username
                        instead of pulling from wp3.db
  --password PASSWORD   Start the RESTful API with the specified password
                        instead of pulling from wp3.db
  -iNM, --ignore-from-networkmanager IG_NETWORKMANAGER
                        set interface for ignore from Network-Manager
  -rNM, --remove-from-networkmanager RM_NETWORKMANAGER
                        remove interface from Network-Manager
  -v, --version         show program's version number and exit
```

### `wp3`

官方给出的调用示例：`wp3 -h`

```text
root@kali:~# wp3 -h
usage: wp3 [-h] [-i INTERFACE] [-iNet INTERFACE_NET] [-s SESSION] [-p PULP]
           [-x XPULP] [-m WIRELESS_MODE] [--no-colors] [--rest]
           [--restport RESTPORT] [--username USERNAME] [--password PASSWORD]
           [-iNM IG_NETWORKMANAGER] [-rNM RM_NETWORKMANAGER] [-v]
wifipumpkin3 - Powerful framework for rogue access point attack. See:
https://wifipumpkin3.github.io/docs/getting-started#usage
options:
  -h, --help            show this help message and exit
  -i INTERFACE          set interface for create AP
  -iNet INTERFACE_NET   set interface for share internet to AP
  -s SESSION            set session for continue attack
  -p, --pulp PULP       interactive sessions can be scripted with .pulp file
  -x, --xpulp XPULP     interactive sessions can be string with ";" as the
                        separator
  -m, --wireless-mode WIRELESS_MODE
                        set wireless mode settings
  --no-colors           disable terminal colors and effects.
  --rest                Run the Wp3 RESTful API.
  --restport RESTPORT   Port to run the Wp3 RESTful API on. default is 1337
  --username USERNAME   Start the RESTful API with the specified username
                        instead of pulling from wp3.db
  --password PASSWORD   Start the RESTful API with the specified password
                        instead of pulling from wp3.db
  -iNM, --ignore-from-networkmanager IG_NETWORKMANAGER
                        set interface for ignore from Network-Manager
  -rNM, --remove-from-networkmanager RM_NETWORKMANAGER
                        remove interface from Network-Manager
  -v, --version         show program's version number and exit
Updated on: 2025-Dec-09
 Edit this page
wgetpaste
wig-ng
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install wifipumpkin3`，再执行 `wifipumpkin3 --version` 2>/dev/null || `wifipumpkin3 -V`
- [ ] **2.** **读官方帮助** —— `wifipumpkin3 -h`，需要细节时 `man wifipumpkin3`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sslstrip <options>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wifipumpkin3/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/collection.md`](../../tools/by-attack/collection.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wifipumpkin3/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wifipumpkin3/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
