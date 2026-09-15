# penelope

> Advanced shell handler for penetration testing and CTFs Penelope is a modern shell handler designed for penetration testers and CTF players. It provides a highly capable alternative to basic netcat listeners, streamlining reverse and bind …

> **功能分类**：通用工具 ｜ **Kali 包**：`penelope` ｜ **官方文档**：<https://www.kali.org/tools/penelope/>

## 1. 安装

```bash
sudo apt update
sudo apt install penelope
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.21.0 |
| 架构 | all |
| 可执行命令 | `penelope` |
| 依赖 | `python3` |
| 安装体积 | 228 KB |
| 官网 | <https://github.com/brightio/penelope> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/penelope> |
| 包追踪 | <https://pkg.kali.org/pkg/penelope> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
penelope -h          # 查看用法
man penelope         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `penelope`

官方给出的调用示例：`penelope -h`

```text
root@kali:~# penelope -h
usage: penelope [-p PORTS] [-i ] [-c ] [-j ] [-a] [-l] [-h] [-L] [-T] [-CT] [-M] [-m ] [-S] [-ms ] [-C] [-U] [-O] [-s] [-prefix ] [-N ] [-v] [-d]
                [-dd] [-cu]
                [args ...]
Penelope Shell Handler
positional arguments:
  args                          Arguments for -s/--serve and SSH reverse shell modes
options:
  -p, --ports PORTS             Ports (comma separated) to listen/connect/serve, depending on -i/-c/-s options
                                (Default: 4444/5555/8000)
Reverse or Bind shell?:
  -i, --interface               Local interface/IP to listen. (Default: 0.0.0.0)
  -c, --connect                 Bind shell Host
  -j, --jump                    Reverse shell jump endpoints
Hints:
  -a, --payloads                Show sample reverse shell payloads for active Listeners
  -l, --interfaces              List available network interfaces
  -h, --help                    show this help message and exit
Session Logging:
  -L, --no-log                  Disable session log files
  -T, --no-timestamps           Disable timestamps in logs
  -CT, --no-colored-timestamps  Disable colored timestamps in logs
Misc:
  -M, --menu                    Start in the Main Menu
  -m, --maintain                Keep N sessions per target
  -S, --single-session          Accommodate only the first created session
  -ms, --max-sessions           Max active sessions per host (default 5, 0 = reject all new)
  -C, --no-attach               Do not auto-attach on new sessions
  -U, --no-upgrade              Disable shell auto-upgrade
  -O, --oscp-safe               Enable OSCP-safe mode
File server:
  -s, --serve                   Run HTTP file server mode
  -prefix, --url-prefix         URL path prefix
Debug:
  -N, --no-bins                 Simulate missing binaries on target (comma-separated)
  -v, --version                 Print version and exit
  -d, --debug                   Enable debug output
  -dd, --dev-mode               Enable developer mode
  -cu, --check-urls             Check hardcoded URLs health and exit
Updated on: 2026-Aug-25
 Edit this page
peass-ng
php-defaults
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install penelope`，再执行 `penelope --version` 2>/dev/null || `penelope -V`
- [ ] **2.** **读官方帮助** —— `penelope -h`，需要细节时 `man penelope`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `penelope -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/penelope/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/penelope/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/penelope/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
