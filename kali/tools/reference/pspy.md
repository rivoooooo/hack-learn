# pspy

> Monitor Linux processes without root permissions pspy is a command line tool designed to snoop on processes without need for root permissions. It allows you to see commands run by other users, cron jobs, etc. as they execute. Great for enu…

> **功能分类**：通用工具 ｜ **Kali 包**：`pspy` ｜ **官方文档**：<https://www.kali.org/tools/pspy/>

## 1. 安装

```bash
sudo apt update
sudo apt install pspy
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.2.1 |
| 架构 | amd64 |
| 可执行命令 | `pspy`、`pspy-binaries` |
| 依赖 | `libc6` |
| 安装体积 | 9.21 MB |
| 官网 | <https://github.com/DominicBreuker/pspy> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/pspy> |
| 包追踪 | <https://pkg.kali.org/pkg/pspy> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
pspy -h          # 查看用法
man pspy         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pspy`

官方给出的调用示例：`pspy -h`

```text
root@kali:~# pspy -h
pspy - version: 1.2.1 - Commit SHA: kali
     ██▓███    ██████  ██▓███ ▓██   ██▓
    ▓██░  ██▒▒██    ▒ ▓██░  ██▒▒██  ██▒
    ▓██░ ██▓▒░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░
    ▒██▄█▓▒ ▒  ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░
    ▒██▒ ░  ░▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░
    ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒
    ░▒ ░     ░ ░▒  ░ ░░▒ ░     ▓██ ░▒░
    ░░       ░  ░  ░  ░░       ▒ ▒ ░░
                   ░           ░ ░
                               ░ ░
Usage:
  pspy [flags]
Flags:
  -c, --color                        color the printed events (default true)
      --debug                        print detailed error messages
  -d, --dirs stringArray             watch these dirs
  -f, --fsevents                     print file system events to stdout
  -h, --help                         help for pspy
  -i, --interval int                 scan every 'interval' milliseconds for new processes (default 100)
      --ppid                         record process ppids
  -p, --procevents                   print new processes to stdout (default true)
  -r, --recursive_dirs stringArray   watch these dirs recursively (default [/usr,/tmp,/etc,/home,/var,/opt])
  -t, --truncate int                 truncate process cmds longer than this (default 2048)
```

### `pspy-binaries`

官方给出的调用示例：`pspy-binaries -h`

```text
root@kali:~# pspy-binaries -h
> pspy ~ Monitor Linux processes without root permissions
/usr/share/pspy
|-- pspy32
|-- pspy32s
|-- pspy64
`-- pspy64s
Learn more with
OffSec
Want to learn more about pspy? get access to in-depth training and hands-on labs:
KeyVault (Lab)
Mantis (Lab)
Updated on: 2026-Jun-17
 Edit this page
myrescue
rdesktop
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install pspy`，再执行 `pspy --version` 2>/dev/null || `pspy -V`
- [ ] **2.** **读官方帮助** —— `pspy -h`，需要细节时 `man pspy`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/pspy/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/pspy/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/pspy/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
