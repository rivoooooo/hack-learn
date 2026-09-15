# websploit

> Web exploitation framework WebSploit is an open source project which is used to scan and analysis remote system in order to find various type of vulnerabilites. This tool is very powerful and supports multiple vulnerabilities.

> **功能分类**：通用工具 ｜ **Kali 包**：`websploit` ｜ **官方文档**：<https://www.kali.org/tools/websploit/>

## 1. 安装

```bash
sudo apt update
sudo apt install websploit
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.0.4 |
| 架构 | all |
| 可执行命令 | `websploit` |
| 依赖 | `python3`、`python3-requests`、`python3-scapy` |
| 安装体积 | 76 KB |
| 官网 | <https://sourceforge.net/projects/websploit/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/websploit> |
| 包追踪 | <https://pkg.kali.org/pkg/websploit> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# websploit
WARNING: No route found for IPv6 destination :: (no default route?)

     __          __  _               _       _ _
     \ \        / / | |             | |     (_) |
      \ \  /\  / /__| |__  ___ _ __ | | ___  _| |_
       \ \/  \/ / _ \ '_ \/ __| '_ \| |/ _ \| | __|
        \  /\  /  __/ |_) \__ \ |_) | | (_) | | |_
         \/  \/ \___|_.__/|___/ .__/|_|\___/|_|\__|
                              | |
                              |_|

        --=[WebSploit FrameWork
    +---**---==[Version :2.0.5 BETA
    +---**---==[Codename :We're Not Crying Wolf
    +---**---==[Available Modules : 19
        --=[Update Date : [r2.0.5-000 2.3.2014]



wsf > use web/dir_scanner
wsf:Dir_Scanner > set TARGET http://192.168.1.202
TARGET =>  192.168.1.202
wsf:Dir_Scanner > run
[*] Your Target : 192.168.1.202
[*]Loading Path List ... Please Wait ...
[index] ... [400 Bad Request]
[images] ... [400 Bad Request]
[download] ... [400 Bad Request]
[2006] ... [400 Bad Request]
[news] ... [400 Bad Request]
[crack] ... [400 Bad Request]
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `websploit`

```text
root@kali:~# websploit
WARNING: No route found for IPv6 destination :: (no default route?)
     __          __  _               _       _ _
     \ \        / / | |             | |     (_) |
      \ \  /\  / /__| |__  ___ _ __ | | ___  _| |_
       \ \/  \/ / _ \ '_ \/ __| '_ \| |/ _ \| | __|
        \  /\  /  __/ |_) \__ \ |_) | | (_) | | |_
         \/  \/ \___|_.__/|___/ .__/|_|\___/|_|\__|
                              | |
                              |_|
        --=[WebSploit FrameWork
    +---**---==[Version :2.0.5 BETA
    +---**---==[Codename :We're Not Crying Wolf
    +---**---==[Available Modules : 19
        --=[Update Date : [r2.0.5-000 2.3.2014]
wsf > use web/dir_scanner
wsf:Dir_Scanner > set TARGET http://192.168.1.202
TARGET =>  192.168.1.202
wsf:Dir_Scanner > run
[*] Your Target : 192.168.1.202
[*]Loading Path List ... Please Wait ...
[index] ... [400 Bad Request]
[images] ... [400 Bad Request]
[download] ... [400 Bad Request]
[2006] ... [400 Bad Request]
[news] ... [400 Bad Request]
[crack] ... [400 Bad Request]
```

### `man`

> 官方示例调用：`man websploit`

```text
root@kali:~# man websploit
WEBSPLOIT(1)                General Commands Manual                WEBSPLOIT(1)
NAME
     websploit - Advanced MITM Framework
SYNOPSIS
     websploit
DESCRIPTION
     Websploit  is  an  automatic vulnerability assessment, web scanner and ex-
     ploiter tool. It is python command line tool that is composed  on  modular
     structure  pretty  similar  to  Metasploit. There are currently 7 modules.
     The command line does not accept any options. User just get  into  console
     typing "websploit" as root and the prompt will change to this: wsf >
OPTIONS
     wsf > help
            Shows  all  command  you can type in the websploit console. Some of
            them are only aplicable when using a certain module.
     wsf > show
            Show Modules of Current Database
     wsf > use <module_name>
            Select Module For Use
     wsf > options
            Show Current Options Of Selected Module
     wsf > set <module_option>
            Once you had seen the options of the selected module, you  may  use
            this command to define its desired value.
     wsf > back
            Exit current module
     wsf > update
            Disabled  on  Debian  systems in order to avoid conflicts with apt-
            get.
     wsf > about
            Shows info about the author.
EXAMPLES
     Here is a simple example on how to use scan_wifi module in order to hunt
     existing wifi networks.
     $wsf > scan_wifi > execute
     SSID              BSSID               CHANNEL   SIGNAL   BARS   SECURITY
     EDTSTAR_2350      1C-B0-44-38-98-49   11        89              WPA2
     JAZZTWE_aJpE      00-4A-77-4D-C4-CC   1         69       _      WPA1 WPA2
     RadioPatioA1985   74-9D-79-2A-47-60   11        57       _      WPA2
     MIWIFI_dsTp       EC-BE-ED-39-1A-D2   1         44       __     WPA2
     DabaduNet4434     78-84-B4-51-44-35   8         44       __     WPA2
     MyHomenet821      74-7D-79-52-2A-00   1         37       __     WPA2
                                                                   WEBSPLOIT(1)
Updated on: 2026-May-25
 Edit this page
wafw00f
whatmask
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install websploit`，再执行 `websploit --version` 2>/dev/null || `websploit -V`
- [ ] **2.** **读官方帮助** —— `websploit -h`，需要细节时 `man websploit`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `websploit -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/websploit/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/websploit/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/websploit/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
