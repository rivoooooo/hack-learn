# lynis

> Security auditing tool for Unix based systems Lynis is an auditing tool for hardening GNU/Linux and Unix based systems. It scans the system configuration and creates an overview of system information and security issues usable by professio…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`lynis` ｜ **官方文档**：<https://www.kali.org/tools/lynis/>

## 1. 安装

```bash
sudo apt update
sudo apt install lynis
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.1.6 |
| 架构 | all |
| 可执行命令 | `lynis` |
| 依赖 | `e2fsprogs` |
| 安装体积 | 1.68 MB |
| 官网 | <https://cisofy.com/lynis/> |
| 源码仓库 | <https://salsa.debian.org/debian/lynis> |
| 包追踪 | <https://pkg.kali.org/pkg/lynis> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan the system in quiet mode (-Q) and output in cronjob format (–cronjob):
root@kali:~# lynis -Q --cronjob

[ Lynis 2.6.2 ]

################################################################################
  Lynis comes with ABSOLUTELY NO WARRANTY. This is free software, and you are
  welcome to redistribute it under the terms of the GNU General Public License.
  See the LICENSE file for details about using this software.

  2007-2018, CISOfy - https://cisofy.com/lynis/
  Enterprise support available (compliance, plugins, interface and tools)
################################################################################


[+] Initializing program
------------------------------------
- Detecting OS...  [ DONE ]
- Checking profiles... [ DONE ]

  ---------------------------------------------------
  Program version:           2.6.2
  Operating system:          Linux
  Operating system name:     Debian
  Operating system version:  kali-rolling
  Kernel version:            4.18.0
  Hardware platform:         x86_64
  Hostname:                  kali
  ---------------------------------------------------
  Profiles:                  /etc/lynis/default.prf
  Log file:                  /var/log/lynis.log
  Report file:               /var/log/lynis-report.dat
  Report version:            1.0
  Plugin directory:          /etc/lynis/plugins
  ---------------------------------------------------
  Auditor:                   [Not Specified]
  Language:                  en
  Test category:             all
  Test group:                all
  ---------------------------------------------------
[...]
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `lynis`

> 官方示例调用：`lynis -Q --cronjob`

```text
root@kali:~# lynis -Q --cronjob
[ Lynis 2.6.2 ]
################################################################################
  Lynis comes with ABSOLUTELY NO WARRANTY. This is free software, and you are
  welcome to redistribute it under the terms of the GNU General Public License.
  See the LICENSE file for details about using this software.
  2007-2018, CISOfy - https://cisofy.com/lynis/
  Enterprise support available (compliance, plugins, interface and tools)
################################################################################
[+] Initializing program
------------------------------------
- Detecting OS...  [ DONE ]
- Checking profiles... [ DONE ]
  ---------------------------------------------------
  Program version:           2.6.2
  Operating system:          Linux
  Operating system name:     Debian
  Operating system version:  kali-rolling
  Kernel version:            4.18.0
  Hardware platform:         x86_64
  Hostname:                  kali
  ---------------------------------------------------
  Profiles:                  /etc/lynis/default.prf
  Log file:                  /var/log/lynis.log
  Report file:               /var/log/lynis-report.dat
  Report version:            1.0
  Plugin directory:          /etc/lynis/plugins
  ---------------------------------------------------
  Auditor:                   [Not Specified]
  Language:                  en
  Test category:             all
  Test group:                all
  ---------------------------------------------------
[...]
```

### `lynis -h`

> 官方示例调用：`lynis -h`

```text
root@kali:~# lynis -h
[ Lynis 3.1.6 ]
################################################################################
  Lynis comes with ABSOLUTELY NO WARRANTY. This is free software, and you are
  welcome to redistribute it under the terms of the GNU General Public License.
  See the LICENSE file for details about using this software.
  2007-2025, CISOfy - https://cisofy.com/lynis/
  Enterprise support available (compliance, plugins, interface and tools)
################################################################################
[+] Initializing program
------------------------------------
  Usage: lynis command [options]
  Command:
    audit
        audit system                  : Perform local security scan
        audit system remote <host>    : Remote security scan
        audit dockerfile <file>       : Analyze Dockerfile
    show
        show                          : Show all commands
        show version                  : Show Lynis version
        show help                     : Show help
    update
        update info                   : Show update details
  Options:
    Alternative system audit modes
    --forensics                       : Perform forensics on a running or mounted system
    --pentest                         : Non-privileged, show points of interest for pentesting
    Layout options
    --no-colors                       : Don't use colors in output
    --quiet (-q)                      : No output
    --reverse-colors                  : Optimize color display for light backgrounds
    --reverse-colours                 : Optimize colour display for light backgrounds
    Misc options
    --debug                           : Debug logging to screen
    --no-log                          : Don't create a log file
    --profile <profile>               : Scan the system with the given profile file
    --view-manpage (--man)            : View man page
    --verbose                         : Show more details on screen
    --version (-V)                    : Display version number and quit
    --wait                            : Wait between a set of tests
    --slow-warning <seconds>  : Threshold for slow test warning in seconds (default 10)
    Enterprise options
    --plugindir <path>                : Define path of available plugins
    --upload                          : Upload data to central node
    More options available. Run '/usr/sbin/lynis show options', or use the man page.
Updated on: 2025-Dec-09
 Edit this page
llm-tools-nmap
macchanger
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install lynis`，再执行 `lynis --version` 2>/dev/null || `lynis -V`
- [ ] **2.** **读官方帮助** —— `lynis -h`，需要细节时 `man lynis`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: lynis command [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/lynis/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[lynis](../../tools/tutorials/02-漏洞分析/lynis.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/privilege-escalation.md`](../../tools/by-attack/privilege-escalation.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/lynis/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/lynis/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
