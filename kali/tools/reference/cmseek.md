# cmseek

> CMS Detection and Exploitation suite This package contains a CMS Detection and Exploitation suite. It scans WordPress, Joomla, Drupal and over 180 other CMSs. A content management system (CMS) manages the creation and modification of digit…

> **功能分类**：通用工具 ｜ **Kali 包**：`cmseek` ｜ **官方文档**：<https://www.kali.org/tools/cmseek/>

## 1. 安装

```bash
sudo apt update
sudo apt install cmseek
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1.3 |
| 架构 | all |
| 可执行命令 | `cmseek` |
| 依赖 | `python3`、`python3-requests` |
| 安装体积 | 400 KB |
| 官网 | <https://github.com/Tuhinshubhra/CMSeeK> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/cmseek> |
| 包追踪 | <https://pkg.kali.org/pkg/cmseek> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
cmseek -h          # 查看用法
man cmseek         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cmseek`

官方给出的调用示例：`cmseek -h`

```text
root@kali:~# cmseek -h
CMSeeK Version 1.1.3
Github: https://github.com/Tuhinshubhra/CMSeeK
Coded By: @r3dhax0r
USAGE:
       python3 cmseek.py (for guided scanning) OR
       python3 cmseek.py [OPTIONS] <Target Specification>
SPECIFING TARGET:
      -u URL, --url URL            Target Url
      -l LIST, --list LIST         Path of the file containing list of sites
                                   for multi-site scan (comma separated)
MANIPULATING SCAN:
      -i cms, --ignore--cms cms    Specify which CMS IDs to skip in order to
                                   avoid flase positive. separated by comma ","
      --strict-cms cms             Checks target against a list of provided
                                   CMS IDs. separated by comma ","
      --skip-scanned               Skips target if it's CMS was previously detected.
      --light-scan                 Skips Deep Scan. Does CMS and version detection only.
      -o, --only-cms               Only detect CMS, ignore deep scan and version detection.
RE-DIRECT:
      --follow-redirect            Follows all/any redirect(s)
      --no-redirect                Skips all redirects and tests the input target(s)
USER AGENT:
      -r, --random-agent           Use a random user agent
      --googlebot                  Use Google bot user agent
      --user-agent USER_AGENT      Specify a custom user agent
OUTPUT:
      -v, --verbose                Increase output verbosity
VERSION:
      --version                    Show CMSeeK version and exit
HELP & MISCELLANEOUS:
      -h, --help                   Show this help message and exit
      --clear-result               Delete all the scan result
      --batch                      Never ask you to press enter after every site in a list is scanned
EXAMPLE USAGE:
      python3 cmseek.py -u example.com                           # Scan example.com
      python3 cmseek.py -l /home/user/target.txt                 # Scan the sites specified in target.txt (comma separated)
      python3 cmseek.py -u example.com --user-agent Mozilla 5.0  # Scan example.com using custom user-Agent Mozilla is 5.0 used here
      python3 cmseek.py -u example.com --random-agent            # Scan example.com using a random user-Agent
      python3 cmseek.py -v -u example.com                        # enabling verbose output while scanning example.com
 CMSeeK says ~ vale
Updated on: 2026-Aug-25
 Edit this page
cloud-enum
cosign
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cmseek`，再执行 `cmseek --version` 2>/dev/null || `cmseek -V`
- [ ] **2.** **读官方帮助** —— `cmseek -h`，需要细节时 `man cmseek`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `cmseek -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cmseek/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cmseek/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cmseek/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
