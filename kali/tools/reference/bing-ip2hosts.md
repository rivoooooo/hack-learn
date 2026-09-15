# bing-ip2hosts

> Enumerate hostnames for an IP using bing.com This package contains a Bing.com web scraper that discovers hostnames by IP address. Bing is the flagship Microsoft search engine formerly known as MSN Search and Live Search. It provides a feat…

> **功能分类**：通用工具 ｜ **Kali 包**：`bing-ip2hosts` ｜ **官方文档**：<https://www.kali.org/tools/bing-ip2hosts/>

## 1. 安装

```bash
sudo apt update
sudo apt install bing-ip2hosts
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0.5 |
| 架构 | all |
| 可执行命令 | `bing-ip2hosts` |
| 依赖 | `bind9-dnsutils`、`wget` |
| 安装体积 | 29 KB |
| 官网 | <https://www.morningstarsecurity.com/research/bing-ip2hosts> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/bing-ip2hosts> |
| 包追踪 | <https://pkg.kali.org/pkg/bing-ip2hosts> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
root@kali:~# bing-ip2hosts -p microsoft.com
[ 65.55.58.201 | Scraping 1 | Found 0 | / ]
http://microsoft.com
http://research.microsoft.com
http://www.answers.microsoft.com
http://www.microsoft.com
http://www.msdn.microsoft.com

root@kali:~# bing-ip2hosts -p 173.194.33.80
[ 173.194.33.80 | Scraping 60-69 of 73 | Found 41 | | ]| / ]
http://asia.google.com
http://desktop.google.com
http://ejabat.google.com
http://google.netscape.com
http://partner-client.google.com
http://picasa.google.com
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `bing-ip2hosts`

官方给出的调用示例：`bing-ip2hosts -p microsoft.com`

```text
root@kali:~# bing-ip2hosts -p microsoft.com
[ 65.55.58.201 | Scraping 1 | Found 0 | / ]
http://microsoft.com
http://research.microsoft.com
http://www.answers.microsoft.com
http://www.microsoft.com
http://www.msdn.microsoft.com
```

### `bing-ip2hosts（示例）`

官方给出的调用示例：`bing-ip2hosts -p 173.194.33.80`

```text
root@kali:~# bing-ip2hosts -p 173.194.33.80
[ 173.194.33.80 | Scraping 60-69 of 73 | Found 41 | | ]| / ]
http://asia.google.com
http://desktop.google.com
http://ejabat.google.com
http://google.netscape.com
http://partner-client.google.com
http://picasa.google.com
```

### `bing-ip2hosts（示例）`

官方给出的调用示例：`bing-ip2hosts -h`

`````text
root@kali:~# bing-ip2hosts -h
  m,                   .,recon:,        ,,
  #####               ]##""^^"%##m    %##b
  ####b               ]##      `##b
  ####b               ]##       ##    i##    @#b,######m       ,######m ##b
  ####b 1mw,          ]##MMM####      i##    ]###`    %##     ###`    `@##
  ####b  1#####Nw,    ]##``    @#b    i##    ]##       ###   ###       j##
  ####i   %########[  ]##       @##   i##    ]##       ###   ##g       j##
  ####n      2#####[  ]##      @##    i##    ]##       ###   @##       {##
  ####g  ,#########b  ]##   ,,e###    j##    ]##       ###    7##m,,,s#M##
  #############M^     'WWWWWW%b^       ii    'nn       nn*      `1337` g##
  ##########"                                                          G##
    "%##"                                                     @#Gmmem###G
  ,i                ,s2e,     ##                                  ````
   `               "`   %#    ##                             T#
  ]#   ]#,#M5@#p         #b   #H#H%@#     s#M5O#o   ,#MSSM  W@##W=  s#SSW
  ]#   j#p    ^#p      ,#M    ##    @#   ##'   'O#  S#,      ]#     #b
  ]#   j#      #M    ,#M      ##    @#   #o     O#    "SXm   ]#      ^"@#
  ]#   j##,  ,##   ,#2        ##    @#   7#.   .#O  ,   ]#   ]#Q       ,#s
  ]#   j######'    #######x   ##    @#    s#####o    ####^    #Tt    ####^
       j#
       j#          bing-ip2hosts (1.0.5) by Andrew Horton @urbanadventurer
       j#          https://morningstarsecurity.com/research/bing-ip2hosts
                   https://github.com/urbanadventurer/bing-ip2hosts
bing-ip2hosts is a Bing.com web scraper that discovers websites by IP address.
Use for OSINT and discovering attack-surface of penetration test targets.
Usage: /usr/bin/bing-ip2hosts [OPTIONS] IP|hostname
OPTIONS are:
-o FILE	Output hostnames to FILE.
-i FILE	Input list of IP addresses or hostnames from FILE.
-n NUM	Stop after NUM scraped pages return no new results (Default: 5).
-l	Select the language for use in the setlang parameter (Default: en-us).
-m	Select the market for use in the setmkt parameter (Default is unset).
-u	Only display hostnames. Default is to include URL prefixes.
-c	CSV output. Outputs the IP and hostname on each line, separated by a comma.
-q	Quiet. Disable output except for final results.
-t DIR	Use this directory instead of /tmp.
-V	Display the version number of bing-ip2hosts and exit.
Updated on: 2025-Dec-09
 Edit this page
bettercap-ui
bloodhound-ce-python
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
`````

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install bing-ip2hosts`，再执行 `bing-ip2hosts --version` 2>/dev/null || `bing-ip2hosts -V`
- [ ] **2.** **读官方帮助** —— `bing-ip2hosts -h`，需要细节时 `man bing-ip2hosts`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: /usr/bin/bing-ip2hosts [OPTIONS] IP|hostname`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/bing-ip2hosts/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/bing-ip2hosts/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/bing-ip2hosts/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
