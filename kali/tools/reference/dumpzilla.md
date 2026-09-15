# dumpzilla

> Mozilla browser forensic tool Dumpzilla application is developed in Python 3.x and has as purpose extract all forensic interesting information of Firefox, Iceweasel and Seamonkey browsers to be analyzed. Due to its Python 3.x development, …

> **功能分类**：数字取证 ｜ **Kali 包**：`dumpzilla` ｜ **官方文档**：<https://www.kali.org/tools/dumpzilla/>

## 1. 安装

```bash
sudo apt update
sudo apt install dumpzilla
```

| 项目 | 内容 |
|------|------|
| 版本 | 20210311 |
| 架构 | all |
| 可执行命令 | `dumpzilla` |
| 依赖 | `libnss3`、`python3`、`python3-lz4`、`python3-magic-ahupp` |
| 安装体积 | 136 KB |
| 官网 | <http://www.dumpzilla.org/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/dumpzilla> |
| 包追踪 | <https://pkg.kali.org/pkg/dumpzilla> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Analyze the Mozilla profile folder (/root/.mozilla/firefox/k780shir.default/) and dump everything except the DOM data (–All):
root@kali:~# dumpzilla '/root/.mozilla/firefox/k780shir.default/' --All

====================================================================================================
Cookies              [SHA256 hash: 18d35b51ec9865ea3dd21e9bc69dc3d286d4e20373bbb0b350a0e41c8bf2da42]
====================================================================================================


Domain: google.com
Host: .google.com
Name: PREF
Value: ID=ddcc3d04cf65b33f:TM=1400253352:LM=1400253352:S=LrFq_HXVbaconjt0l
Path: /
Expiry: 2016-05-15 11:15:52
Last acess: 2014-05-16 11:15:52
Creation Time: 2014-05-16 11:15:52
Secure: No
HttpOnly: No


Domain: kali.org
Host: .kali.org
Name: __utma
Value: 24402336.1888242215.144BAC0N56.1400253356.14322255.1
Path: /
Expiry: 2016-05-15 11:15:55
Last acess: 2014-05-16 11:15:55
Creation Time: 2014-05-16 11:15:55
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dumpzilla`

官方给出的调用示例：`dumpzilla '/root/.mozilla/firefox/k780shir.default/' --All`

```text
root@kali:~# dumpzilla '/root/.mozilla/firefox/k780shir.default/' --All
====================================================================================================
Cookies              [SHA256 hash: 18d35b51ec9865ea3dd21e9bc69dc3d286d4e20373bbb0b350a0e41c8bf2da42]
====================================================================================================
Domain: google.com
Host: .google.com
Name: PREF
Value: ID=ddcc3d04cf65b33f:TM=1400253352:LM=1400253352:S=LrFq_HXVbaconjt0l
Path: /
Expiry: 2016-05-15 11:15:52
Last acess: 2014-05-16 11:15:52
Creation Time: 2014-05-16 11:15:52
Secure: No
HttpOnly: No
Domain: kali.org
Host: .kali.org
Name: __utma
Value: 24402336.1888242215.144BAC0N56.1400253356.14322255.1
Path: /
Expiry: 2016-05-15 11:15:55
Last acess: 2014-05-16 11:15:55
Creation Time: 2014-05-16 11:15:55
```

### `dumpzilla（示例）`

官方给出的调用示例：`dumpzilla -h`

```text
root@kali:~# dumpzilla -h
usage: python dumpzilla.py PROFILE_DIR [OPTIONS]
Options:
 --Addons
 --Search
 --Bookmarks [-bm_create_range <start> <end>][-bm_last_range <start> <end>]
 --Certoverride
 --Cookies [-showdom] [-domain <string>] [-name <string>] [-hostcookie <string>] [-access <date>] [-create <date>]
           [-secure <0|1>] [-httponly <0|1>] [-last_range <start> <end>] [-create_range <start> <end>]
 --Downloads [-range <start> <end>]
 --Export <directory> (export data as json)
 --Forms [-value <string>] [-forms_range <start> <end>]
 --Help (shows this help message and exit)
 --History [-url <string>] [-title <string>] [-date <date>] [-history_range <start> <end>] [-frequency]
 --Keypinning [-entry_type <HPKP|HSTS>]
 --OfflineCache [-cache_range <start> <end> -extract <directory>]
 --Preferences
 --Passwords
 --Permissions [-host <string>] [-modif <date>] [-modif_range <start> <end>]
 --RegExp (use Regular Expresions for string type filters instead of Wildcards)
 --Session
 --Summary (no data extraction, only summary report)
 --Thumbnails [-extract_thumb <directory>]
 --Verbosity (DEBUG|INFO|WARNING|ERROR|CRITICAL)
 --Watch [-text <string>] (shows in daemon mode the URLs and text form in real time; Unix only)
Wildcards (without RegExp option):
 '%'  Any string of any length (including zero length)
 '_'  Single character
 '\'  Escape character
Regular Expresions: https://docs.python.org/3/library/re.html
Date syntax:
 YYYY-MM-DD hh:mi:ss (wildcards allowed)
Profile location:
 WinXP profile -> 'C:\Documents and Settings\%USERNAME%\Application Data\Mozilla\Firefox\Profiles\xxxx.default'
 Win7 profile  -> 'C:\Users\%USERNAME%\AppData\Roaming\Mozilla\Firefox\Profiles\xxxx.default'
 MacOS profile -> '/Users/$USER/Library/Application\ Support/Firefox/Profiles/xxxx.default'
 Unix profile  -> '/home/$USER/.mozilla/firefox/xxxx.default'
dumpzilla: error: ambiguous option: -h could match -hostcookie, -httponly, -host, -history_range
Updated on: 2025-Dec-09
 Edit this page
dumpsterdiver
dwarf2json
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dumpzilla`，再执行 `dumpzilla --version` 2>/dev/null || `dumpzilla -V`
- [ ] **2.** **读官方帮助** —— `dumpzilla -h`，需要细节时 `man dumpzilla`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `dumpzilla -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dumpzilla/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dumpzilla/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dumpzilla/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
