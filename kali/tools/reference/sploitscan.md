# sploitscan

> Search for CVE information SploitScan is an efficient and easy-to-use command-line tool designed to consult CVE (Common Vulnerabilities and Exposures). Extremely important for professionals, as it allows them to implement measures that pre…

> **功能分类**：通用工具 ｜ **Kali 包**：`sploitscan` ｜ **官方文档**：<https://www.kali.org/tools/sploitscan/>

## 1. 安装

```bash
sudo apt update
sudo apt install sploitscan
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.14.3 |
| 架构 | all |
| 可执行命令 | `sploitscan` |
| 依赖 | `python3`、`python3-git`、`python3-jinja2`、`python3-openai`、`python3-requests`、`python3-tabulate`、`python3-tqdm` |
| 安装体积 | 268 KB |
| 官网 | <https://github.com/xaitax/SploitScan> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/sploitscan> |
| 包追踪 | <https://pkg.kali.org/pkg/sploitscan> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sploitscan -h          # 查看用法
man sploitscan         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sploitscan`

官方给出的调用示例：`sploitscan -h`

```text
root@kali:~# sploitscan -h
███████╗██████╗ ██╗      ██████╗ ██╗████████╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║
███████╗██████╔╝██║     ██║   ██║██║   ██║   ███████╗██║     ███████║██╔██╗ ██║
╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   ╚════██║██║     ██╔══██║██║╚██╗██║
███████║██║     ███████╗╚██████╔╝██║   ██║   ███████║╚██████╗██║  ██║██║ ╚████║
╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
v0.14.3 / Alexander Hagenah / @xaitax /
[email protected]
usage: sploitscan [-h] [-e {json,csv,html}]
                  [-t {nessus,nexpose,openvas,docker}]
                  [--ai {openai,google,grok,deepseek}]
                  [-k KEYWORDS [KEYWORDS ...]] [-local] [-f] [-m METHODS]
                  [-i IMPORT_FILE] [--input-dir INPUT_DIR] [-c CONFIG] [-d]
                  [cve_ids ...]
SploitScan: Retrieve and display vulnerability and exploit data for specified
CVE ID(s).
positional arguments:
  cve_ids               Enter one or more CVE IDs (e.g., CVE-YYYY-NNNNN). This
                        is optional if an import file is provided via -i.
options:
  -h, --help            show this help message and exit
  -e, --export {json,csv,html}
                        Export the results in the specified format ('json',
                        'csv', or 'html').
  -t, --type {nessus,nexpose,openvas,docker}
                        Specify the type of the import file ('nessus',
                        'nexpose', 'openvas', or 'docker').
  --ai {openai,google,grok,deepseek}
                        Select the AI provider for risk assessment (e.g.,
                        'openai', 'google', 'grok', or 'deepseek').
  -k, --keywords KEYWORDS [KEYWORDS ...]
                        Search for CVEs related to specific keywords (e.g.,
                        product name).
  -local, --local-database
                        Download the cvelistV5 repository into the local
                        directory. Use the local database over online research
                        if available.
  -f, --fast-mode       Enable fast mode: only display basic CVE information
                        without fetching additional exploits or data.
  -m, --methods METHODS
                        Specify which methods to run, separated by commas
                        (e.g., 'cisa,epss,hackerone,ai,prio,references').
  -i, --import-file IMPORT_FILE
                        Path to an import file. When provided, positional CVE
                        IDs can be omitted. The file should be a plain text
                        list with one CVE per line.
  --input-dir INPUT_DIR
                        Path to a directory containing vulnerability reports
                        to scan for CVE IDs.
  -c, --config CONFIG   Path to a custom configuration file.
  -d, --debug           Enable debug output.
Updated on: 2026-Aug-25
 Edit this page
socat
sprayhound
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sploitscan`，再执行 `sploitscan --version` 2>/dev/null || `sploitscan -V`
- [ ] **2.** **读官方帮助** —— `sploitscan -h`，需要细节时 `man sploitscan`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sploitscan -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sploitscan/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sploitscan/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sploitscan/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
