# regripper

> Perform forensic analysis of registry hives Regripper’s CLI tool can be used to surgically extract, translate, and display information (both data and metadata) from Registry-formatted files via plugins in the form of Perl-scripts. It allow…

> **功能分类**：数字取证 ｜ **Kali 包**：`regripper` ｜ **官方文档**：<https://www.kali.org/tools/regripper/>

## 1. 安装

```bash
sudo apt update
sudo apt install regripper
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.0~git20260527.ec96dd4 |
| 架构 | all |
| 可执行命令 | `regripper` |
| 依赖 | `libparse-win32registry-perl`、`perl` |
| 安装体积 | 1.11 MB |
| 官网 | <https://github.com/keydet89/RegRipper3.0> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/regripper> |
| 包追踪 | <https://pkg.kali.org/pkg/regripper> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Screenshots
regripper
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `regripper`

官方给出的调用示例：`regripper -h`

```text
root@kali:~# regripper -h
Rip v.3.0 - CLI RegRipper tool
Rip [-r Reg hive file] [-f profile] [-p plugin] [options]
Parse Windows Registry files, using either a single module, or a profile.
NOTE: This tool does NOT automatically process Registry transaction logs! The tool
does check to see if the hive is dirty, but does not automatically process the
transaction logs.  If you need to incorporate transaction logs, please consider
using yarp + registryFlush.py, or rla.exe from Eric Zimmerman.
  -r [hive] .........Registry hive file to parse
  -d ................Check to see if the hive is dirty
  -g ................Guess the hive file type
  -a ................Automatically run hive-specific plugins
  -aT ...............Automatically run hive-specific TLN plugins
  -f [profile].......use the profile
  -p [plugin]........use the plugin
  -l ................list all plugins
  -c ................Output plugin list in CSV format (use with -l)
  -s systemname......system name (TLN support)
  -u username........User name (TLN support)
  -uP ...............Update default profiles
  -h.................Help (print this information)
Ex: C:\>rip -r c:\case\system -f system
    C:\>rip -r c:\case\ntuser.dat -p userassist
    C:\>rip -r c:\case\ntuser.dat -a
    C:\>rip -l -c
All output goes to STDOUT; use redirection (ie, > or >>) to output to a file.
copyright 2020 Quantum Analytics Research, LLC
Updated on: 2026-Aug-25
 Edit this page
recordmydesktop
requests
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install regripper`，再执行 `regripper --version` 2>/dev/null || `regripper -V`
- [ ] **2.** **读官方帮助** —— `regripper -h`，需要细节时 `man regripper`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `regripper -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/regripper/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/regripper/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/regripper/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
