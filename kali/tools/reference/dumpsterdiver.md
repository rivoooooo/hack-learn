# dumpsterdiver

> Tool to analyze big volumes of data in search of hardcoded secrets This package contains a tool, which can analyze big volumes of data in search of hardcoded secrets like keys (e.g. AWS Access Key, Azure Share Key or SSH keys) or passwords…

> **功能分类**：通用工具 ｜ **Kali 包**：`dumpsterdiver` ｜ **官方文档**：<https://www.kali.org/tools/dumpsterdiver/>

## 1. 安装

```bash
sudo apt update
sudo apt install dumpsterdiver
```

| 项目 | 内容 |
|------|------|
| 版本 | 0~git20210628.058087e |
| 架构 | all |
| 可执行命令 | `dumpsterdiver` |
| 依赖 | `python3`、`python3-colorama`、`python3-passwordmeter`、`python3-termcolor`、`python3-yaml` |
| 安装体积 | 44 KB |
| 官网 | <https://github.com/securing/DumpsterDiver> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/dumpsterdiver> |
| 包追踪 | <https://pkg.kali.org/pkg/dumpsterdiver> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
dumpsterdiver -h          # 查看用法
man dumpsterdiver         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `DumpsterDiver`

> 官方示例调用：`DumpsterDiver -h`

```text
root@kali:~# DumpsterDiver -h
       ___                          __             ___   _
      / _ \ __ __ __ _   ___   ___ / /_ ___  ____ / _ \ (_)_  __ ___  ____
     / // // // //  ' \ / _ \ (_-</ __// -_)/ __// // // /| |/ // -_)/ __/
    /____/ \_,_//_/_/_// .__//___/\__/ \__//_/  /____//_/ |___/ \__//_/
                      /_/
                                                       #Coded by @Rzepsky
usage: DumpsterDiver.py [-h] -p LOCAL_PATH [-r] [-a] [-s] [-o OUTFILE]
                        [--min-key MIN_KEY] [--max-key MAX_KEY]
                        [--entropy ENTROPY] [--min-pass MIN_PASS]
                        [--max-pass MAX_PASS]
                        [--pass-complex {1,2,3,4,5,6,7,8,9}]
                        [--exclude-files EXCLUDE_FILES [EXCLUDE_FILES ...]]
                        [--bad-expressions BAD_EXPRESSIONS [BAD_EXPRESSIONS ...]]
options:
  -h, --help            show this help message and exit
BASIC USAGE:
  -p LOCAL_PATH         path to the folder containing files to be analyzed
  -r, --remove          when this flag is set, then files which don't contain
                        any secret will be removed.
  -a, --advance         when this flag is set, then all files will be
                        additionally analyzed using rules specified in
                        '~/.dumpsterdiver/rules.yaml' file.
  -s, --secret          when this flag is set, then all files will be
                        additionally analyzed in search of hardcoded
                        passwords.
  -o OUTFILE            output file in JSON format.
CONFIGURATION:
  --min-key MIN_KEY     specifies the minimum key length to be analyzed
                        (default is 20).
  --max-key MAX_KEY     specifies the maximum key length to be analyzed
                        (default is 80).
  --entropy ENTROPY     specifies the edge of high entropy (default is 4.3).
  --min-pass MIN_PASS   specifies the minimum password length to be analyzed
                        (default is 8). Requires adding '-s' flag to the
                        syntax.
  --max-pass MAX_PASS   specifies the maximum password length to be analyzed
                        (default is 12). Requires adding '-s' flag to the
                        syntax.
  --pass-complex {1,2,3,4,5,6,7,8,9}
                        specifies the edge of password complexity between 1
                        (trivial passwords) to 9 (very complex passwords)
                        (default is 8). Requires adding '-s' flag to the
                        syntax.
  --exclude-files EXCLUDE_FILES [EXCLUDE_FILES ...]
                        specifies file names or extensions which shouldn't be
                        analyzed. File extension should contain '.' character
                        (e.g. '.pdf'). Multiple file names and extensions
                        should be separated by space.
  --bad-expressions BAD_EXPRESSIONS [BAD_EXPRESSIONS ...]
                        specifies bad expressions - if the DumpsterDiver find
                        such expression in a file, then this file won't be
                        analyzed. Multiple bad expressions should be separated
                        by space.
Updated on: 2025-Dec-09
 Edit this page
dufflebag
dumpzilla
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dumpsterdiver`，再执行 `dumpsterdiver --version` 2>/dev/null || `dumpsterdiver -V`
- [ ] **2.** **读官方帮助** —— `dumpsterdiver -h`，需要细节时 `man dumpsterdiver`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `dumpsterdiver -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dumpsterdiver/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dumpsterdiver/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dumpsterdiver/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
