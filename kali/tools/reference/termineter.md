# termineter

> Smart meter testing framework This package contains a Python framework which provides a platform for the security testing of smart meters. It implements the C1218 and C1219 protocols for communication over an optical interface. Currently s…

> **功能分类**：漏洞利用 ｜ **Kali 包**：`termineter` ｜ **官方文档**：<https://www.kali.org/tools/termineter/>

## 1. 安装

```bash
sudo apt update
sudo apt install termineter
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0.6 |
| 架构 | all |
| 可执行命令 | `termineter` |
| 依赖 | `python3`、`python3-crcelk`、`python3-pluginbase`、`python3-pyasn1`、`python3-serial`、`python3-smoke-zephyr`、`python3-tabulate`、`python3-termcolor` |
| 安装体积 | 343 KB |
| 官网 | <https://github.com/rsmusllp/termineter> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/termineter> |
| 包追踪 | <https://pkg.kali.org/pkg/termineter> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# termineter

   ______              _          __
  /_  __/__ ______ _  (_)__  ___ / /____ ____
   / / / -_) __/  ' \/ / _ \/ -_) __/ -_) __/
  /_/  \__/_/ /_/_/_/_/_//_/\__/\__/\__/_/

  <[ termineter                     v1.0.4
  <[ model:                         T-1000
  <[ loaded modules:                    17

termineter > show modules

Modules
=======

  Name                    Description
  ----------------------  ------------------------------------------------
  brute_force_login       Brute Force Credentials
  diff_tables             Check C12.19 Tables For Differences
  dump_tables             Write Readable C12.19 Tables To A CSV File
  enum_tables             Enumerate Readable C12.19 Tables From The Device
  enum_user_ids           Enumerate Valid User IDs From The Device
  get_identification      Read And Parse The Identification Information
  get_info                Get Basic Meter Information By Reading Tables
  get_local_display_info  Get Information From The Local Display Tables
  get_log_info            Get Information About The Meter's Logs
  get_modem_info          Get Information About The Integrated Modem
  get_security_info       Get Information About The Meter's Access Control
  read_table              Read Data From A C12.19 Table
  remote_reset            Initiate A Reset Procedure
  run_procedure           Initiate A Custom Procedure
  set_meter_id            Set The Meter's I.D.
  set_meter_mode          Change the Meter's Operating Mode
  write_table             Write Data To A C12.19 Table

termineter >
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `termineter`

```text
root@kali:~# termineter
   ______              _          __
  /_  __/__ ______ _  (_)__  ___ / /____ ____
   / / / -_) __/  ' \/ / _ \/ -_) __/ -_) __/
  /_/  \__/_/ /_/_/_/_/_//_/\__/\__/\__/_/
  <[ termineter                     v1.0.4
  <[ model:                         T-1000
  <[ loaded modules:                    17
termineter > show modules
Modules
=======
  Name                    Description
  ----------------------  ------------------------------------------------
  brute_force_login       Brute Force Credentials
  diff_tables             Check C12.19 Tables For Differences
  dump_tables             Write Readable C12.19 Tables To A CSV File
  enum_tables             Enumerate Readable C12.19 Tables From The Device
  enum_user_ids           Enumerate Valid User IDs From The Device
  get_identification      Read And Parse The Identification Information
  get_info                Get Basic Meter Information By Reading Tables
  get_local_display_info  Get Information From The Local Display Tables
  get_log_info            Get Information About The Meter's Logs
  get_modem_info          Get Information About The Integrated Modem
  get_security_info       Get Information About The Meter's Access Control
  read_table              Read Data From A C12.19 Table
  remote_reset            Initiate A Reset Procedure
  run_procedure           Initiate A Custom Procedure
  set_meter_id            Set The Meter's I.D.
  set_meter_mode          Change the Meter's Operating Mode
  write_table             Write Data To A C12.19 Table
termineter >
```

### `termineter（示例）`

官方给出的调用示例：`termineter -h`

```text
root@kali:~# termineter -h
usage: termineter [-h] [-v] [-L {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                  [-r RESOURCE_FILE]
Termineter: Python Smart Meter Testing Framework
options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -L, --log {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        set the logging level
  -r, --rc-file RESOURCE_FILE
                        execute a resource file
Updated on: 2025-Dec-09
 Edit this page
teamsploit
terraform
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install termineter`，再执行 `termineter --version` 2>/dev/null || `termineter -V`
- [ ] **2.** **读官方帮助** —— `termineter -h`，需要细节时 `man termineter`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `termineter -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/termineter/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/termineter/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/termineter/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
