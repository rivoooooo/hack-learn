# maryam

> OWASP Maryam is a modular/optional open source framework bas This package contains the OWASP Maryam, a modular/optional open source framework based on OSINT and data gathering. Maryam is written in Python programming language and it’s desi…

> **功能分类**：识别与指纹 ｜ **Kali 包**：`maryam` ｜ **官方文档**：<https://www.kali.org/tools/maryam/>

## 1. 安装

```bash
sudo apt update
sudo apt install maryam
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.5.3 |
| 架构 | all |
| 可执行命令 | `maryam` |
| 依赖 | `python3`、`python3-bs4`、`python3-cloudscraper`、`python3-dask`、`python3-flask`、`python3-gensim`、`python3-lxml`、`python3-matplotlib`、`python3-numpy`、`python3-pandas`、`python3-plotly`、`python3-requests` 等 |
| 安装体积 | 976 KB |
| 官网 | <https://github.com/saeeddhqan/Maryam> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/maryam> |
| 包追踪 | <https://pkg.kali.org/pkg/maryam> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
maryam -h          # 查看用法
man maryam         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `maryam`

官方给出的调用示例：`maryam -h`

```text
root@kali:~# maryam -h
usage: maryam [-h] [-e execute] [-s start] [-v]
maryam -h
optional arguments:
	  -h, --help   show this help message and exit
	  -e execute   execute a command and exit
	  -s start     run a command without exit
	  -v           show version and exit
Updated on: 2025-Dec-09
 Edit this page
macchanger
maskprocessor
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install maryam`，再执行 `maryam --version` 2>/dev/null || `maryam -V`
- [ ] **2.** **读官方帮助** —— `maryam -h`，需要细节时 `man maryam`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `maryam -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/maryam/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/maryam/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/maryam/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
