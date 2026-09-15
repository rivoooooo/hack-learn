# havoc

> Modern and malleable post-exploitation C2 framework Havoc is a modern, malleable post-exploitation command and control framework made for penetration testers, red teams, and blue teams.

> **功能分类**：通用工具 ｜ **Kali 包**：`havoc` ｜ **官方文档**：<https://www.kali.org/tools/havoc/>

## 1. 安装

```bash
sudo apt update
sudo apt install havoc
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.6~git20251218.c84f775 |
| 架构 | amd64 |
| 可执行命令 | `havoc` |
| 依赖 | `gcc-mingw-w64-i686-win32`、`gcc-mingw-w64-x86-64-win32`、`libc6`、`libgcc-s1`、`libpython3.13`、`libqt5core5t64` |
| 安装体积 | 27.13 MB |
| 官网 | <https://github.com/HavocFramework/Havoc> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/havoc> |
| 包追踪 | <https://pkg.kali.org/pkg/havoc> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
havoc -h          # 查看用法
man havoc         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `havoc`

> 官方示例调用：`havoc -h`

```text
root@kali:~# havoc -h
Havoc Framework [Version: 0.7] [CodeName: Bites The Dust]
Usage:
  havoc [flags]
  havoc [command]
Available Commands:
  client      client command
  help        Help about any command
  server      teamserver command
Flags:
  -h, --help   help for havoc
Use "havoc [command] --help" for more information about a command.
Updated on: 2026-Mar-02
 Edit this page
hashcat-utils
hb-honeypot
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install havoc`，再执行 `havoc --version` 2>/dev/null || `havoc -V`
- [ ] **2.** **读官方帮助** —— `havoc -h`，需要细节时 `man havoc`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/havoc/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/havoc/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/havoc/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
