# phpsploit

> Stealth post-exploitation framework This package contains a remote control framework, aiming to provide a stealth interactive shell-like connection over HTTP between client and web server. It is a post-exploitation tool capable to maintain…

> **功能分类**：通用工具 ｜ **Kali 包**：`phpsploit` ｜ **官方文档**：<https://www.kali.org/tools/phpsploit/>

## 1. 安装

```bash
sudo apt update
sudo apt install phpsploit
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.2 |
| 架构 | all |
| 可执行命令 | `phpsploit` |
| 依赖 | `php`、`python3`、`python3-extproxy`、`python3-phpserialize`、`python3-pygments`、`python3-pyparsing`、`python3-socks` |
| 安装体积 | 877 KB |
| 官网 | <https://github.com/nil0x42/phpsploit> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/phpsploit> |
| 包追踪 | <https://pkg.kali.org/pkg/phpsploit> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
phpsploit -h          # 查看用法
man phpsploit         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `phpsploit`

> 官方示例调用：`phpsploit -h`

```text
root@kali:~# phpsploit -h
usage: phpsploit [-h] [-v] [-c <FILE>] [-l <SESSION>] [-t <URL>] [-s <FILE>]
                 [-e <CMD>] [-i]
The stealth post-exploitation framework
options:
  -h, --help            show this help message and exit
  -v, --version         output version information and exit
  -c, --config <FILE>   use alternative configuration file
  -l, --load <SESSION>  load session file
  -t, --target <URL>    set remote TARGET URL
  -s, --source <FILE>   run commands from file (disables interactive mode)
  -e, --eval <CMD>      run phpsploit command (disables interactive mode)
  -i, --interactive     force interactive mode if unset by `-e` or `-s`
Updated on: 2025-Dec-09
 Edit this page
phpggc
pipal
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install phpsploit`，再执行 `phpsploit --version` 2>/dev/null || `phpsploit -V`
- [ ] **2.** **读官方帮助** —— `phpsploit -h`，需要细节时 `man phpsploit`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `phpsploit -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/phpsploit/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/phpsploit/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/phpsploit/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
