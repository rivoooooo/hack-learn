# wpprobe

> Fast WordPress plugin enumeration tool A fast WordPress plugin scanner that detects installed plugins via REST API enumeration and maps them to known vulnerabilities. Over 3000 plugins detectable without brute-force, thousands more with it.

> **功能分类**：通用工具 ｜ **Kali 包**：`wpprobe` ｜ **官方文档**：<https://www.kali.org/tools/wpprobe/>

## 1. 安装

```bash
sudo apt update
sudo apt install wpprobe
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.12.11 |
| 架构 | any |
| 可执行命令 | `wpprobe` |
| 依赖 | `libc6` |
| 安装体积 | 14.43 MB |
| 官网 | <https://github.com/Chocapikk/wpprobe> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/wpprobe> |
| 包追踪 | <https://pkg.kali.org/pkg/wpprobe> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
wpprobe -h          # 查看用法
man wpprobe         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wpprobe`

官方给出的调用示例：`wpprobe -h`

```text
root@kali:~# wpprobe -h
 __    __  ___  ___           _
/ / /\ \ \/ _ \/ _ \_ __ ___ | |__   ___
\ \/  \/ / /_)/ /_)/ '__/ _ \| '_ \ / _ \
 \  /\  / ___/ ___/| | | (_) | |_) |  __/
  \/  \/\/   \/    |_|  \___/|_.__/ \___|
                                            dev [kali]
Stealthy WordPress Plugin Scanner - By @Chocapikk
08:31:32 [WARNING] Vulnerability database not found. Run: wpprobe update-db
WPProbe is a high-speed WordPress plugin scanner that detects installed plugins and checks for known vulnerabilities using the Wordfence database.
Usage:
  wpprobe [command]
Available Commands:
  completion  Generate the autocompletion script for the specified shell
  help        Help about any command
  list        Show how many CVEs wpprobe can detect, split by severity
  scan        Scan a WordPress site for installed plugins and vulnerabilities
  search      Search vulnerabilities by various filters
  uninstall   Uninstalls WPProbe and removes all related files and the binary
  update      Update WPProbe to the latest version
  update-db   Update vulnerability databases
Flags:
  -h, --help      help for wpprobe
  -v, --version   version for wpprobe
Use "wpprobe [command] --help" for more information about a command.
Updated on: 2026-Aug-25
 Edit this page
winregfs
wpscan
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install wpprobe`，再执行 `wpprobe --version` 2>/dev/null || `wpprobe -V`
- [ ] **2.** **读官方帮助** —— `wpprobe -h`，需要细节时 `man wpprobe`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wpprobe/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wpprobe/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wpprobe/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
