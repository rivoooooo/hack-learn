# command-not-found

> Suggest installation of packages in interactive bash sessions This package will install a handler for command_not_found that looks up programs not currently installed but available from the repositories.

> **功能分类**：通用工具 ｜ **Kali 包**：`command-not-found` ｜ **官方文档**：<https://www.kali.org/tools/command-not-found/>

## 1. 安装

```bash
sudo apt update
sudo apt install command-not-found
```

| 项目 | 内容 |
|------|------|
| 版本 | 23.04.0 |
| 架构 | all |
| 可执行命令 | `command-not-found`、`update-command-not-found` |
| 依赖 | `apt-file`、`lsb-release`、`python3`、`python3-apt` |
| 安装体积 | 524 KB |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/command-not-found> |
| 包追踪 | <https://pkg.kali.org/pkg/command-not-found> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
command-not-found -h          # 查看用法
man command-not-found         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `command-not-found`

官方给出的调用示例：`command-not-found -h`

```text
root@kali:~# command-not-found -h
Usage: command-not-found [options] <command-name>
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -d DATA_DIR, --data-dir=DATA_DIR
                        use this path to locate data fields
  --ignore-installed, --ignore-installed
                        ignore local binaries and display the available
                        packages
  --no-failure-msg      don't print '<command-name>: command not found'
```

### `man`

官方给出的调用示例：`man update-command-not-found`

```text
root@kali:~# man update-command-not-found
update-com...-not-found(8)  Command not found helper update-com...-not-found(8)
NAME
     update-command-not-found - update the command-not-found cache
SYNOPSIS
     update-command-not-found [-h|--help|-n|--no-apt-file]
DESCRIPTION
     update-command-not-found  updates  the  cache (databases) for command-not-
     found using the files in /var/cache/apt/apt-file,  which  are  fetched  by
     apt-file.
OPTIONS
     -h or --help
            Print the help message
     -n or --no-apt-file
            Do not run apt-file update before updating the cache.
AUTHOR
     command-not-found  was  written  by  Zygmunt Krynicki, update-command-not-
     found was written by Julian Andres Klode <
[email protected]
>
     This manual page was written by Julian Andres Klode  <
[email protected]
>  for
     the Debian project, but may be used by others.
0.2.26-1                           2008-10-24        update-com...-not-found(8)
Updated on: 2026-May-25
 Edit this page
cifs-utils
cutecom
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install command-not-found`，再执行 `command-not-found --version` 2>/dev/null || `command-not-found -V`
- [ ] **2.** **读官方帮助** —— `command-not-found -h`，需要细节时 `man command-not-found`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: command-not-found [options] <command-name>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/command-not-found/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/command-not-found/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/command-not-found/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
