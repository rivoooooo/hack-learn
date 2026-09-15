# wordlistraider

> Tool to prepare existing wordlists This package contains a Python tool for preparing existing wordlists. It returns a selection of words that matches the passed conditions in an existing list. As an example you have a GB big wordlist and y…

> **功能分类**：通用工具 ｜ **Kali 包**：`wordlistraider` ｜ **官方文档**：<https://www.kali.org/tools/wordlistraider/>

## 1. 安装

```bash
sudo apt update
sudo apt install wordlistraider
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0~git20200927 |
| 架构 | all |
| 可执行命令 | `wordlistraider` |
| 依赖 | `figlet`、`python3`、`python3-colorama`、`python3-more-termcolor`、`python3-pyfiglet` |
| 安装体积 | 30 KB |
| 官网 | <https://github.com/GregorBiswanger/WordlistRaider> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/wordlistraider> |
| 包追踪 | <https://pkg.kali.org/pkg/wordlistraider> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
wordlistraider -h          # 查看用法
man wordlistraider         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wordlistraider`

官方给出的调用示例：`wordlistraider -h`

```text
root@kali:~# wordlistraider -h
__        __            _ _ _     _   ____       _     _           _
\ \      / /__  _ __ __| | (_)___| |_|  _ \ __ _(_) __| | ___ _ __| |
 \ \ /\ / / _ \| '__/ _` | | / __| __| |_) / _` | |/ _` |/ _ \ '__| |
  \ V  V / (_) | | | (_| | | \__ \ |_|  _ < (_| | | (_| |  __/ |  |_|
   \_/\_/ \___/|_|  \__,_|_|_|___/\__|_| \_\__,_|_|\__,_|\___|_|  (_)
Coded by Gregor Biswanger, Jürgen Gutsch & Community - Version 1.0
usage: wordlistraider [-h] -w path to source file -t path to the target file
                      [--min MIN] [--max MAX] [-n NUMBERS]
                      [-s SPECIALCHARACTERS]
Returns a selection of words that matches the passed conditions in an existing
list.
options:
  -h, --help            show this help message and exit
  -w, --wordlist path to source file
                        the wordlist to raid
  -t, --target path to the target file
                        the target wordlist
  --min, --minlength MIN
                        minimum length of password (default: 8)
  --max, --maxlength MAX
                        maximum length of password
  -n, --numbers NUMBERS
                        password must include numbers (default: false)
  -s, --specialcharacters SPECIALCHARACTERS
                        includes passwords with special characters (default:
                        false)
Updated on: 2025-Dec-09
 Edit this page
windows-privesc-check
wotmate
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install wordlistraider`，再执行 `wordlistraider --version` 2>/dev/null || `wordlistraider -V`
- [ ] **2.** **读官方帮助** —— `wordlistraider -h`，需要细节时 `man wordlistraider`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `wordlistraider -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wordlistraider/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wordlistraider/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wordlistraider/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
