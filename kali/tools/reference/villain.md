# villain

> High level C2 framework Villain is a C2 framework that can handle multiple TCP socket & HoaxShell-based reverse shells, enhance their functionality with additional features and share them among connected sibling servers.

> **功能分类**：通用工具 ｜ **Kali 包**：`villain` ｜ **官方文档**：<https://www.kali.org/tools/villain/>

## 1. 安装

```bash
sudo apt update
sudo apt install villain
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.2.1 |
| 架构 | all |
| 可执行命令 | `villain` |
| 依赖 | `python3`、`python3-netifaces`、`python3-pycryptodome`、`python3-pyperclip`、`python3-requests` |
| 安装体积 | 326 KB |
| 官网 | <https://github.com/t3l3machus/Villain> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/villain> |
| 包追踪 | <https://pkg.kali.org/pkg/villain> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
villain -h          # 查看用法
man villain         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `villain`

> 官方示例调用：`villain -h`

```text
root@kali:~# villain -h
usage: Villain.py [-h] [-p PORT] [-x HOAX_PORT] [-n REVERSE_TCP_PORT]
                  [-f FILE_SMUGGLER_PORT] [-i] [-c CERTFILE] [-k KEYFILE] [-v]
                  [-q]
options:
  -h, --help            show this help message and exit
  -p, --port PORT       Team server port (default: 6501).
  -x, --hoax-port HOAX_PORT
                        HoaxShell server port (default: 8080 via http, 443 via
                        https).
  -n, --reverse-tcp-port REVERSE_TCP_PORT
                        Reverse TCP multi-handler port (default: 4443).
  -f, --file-smuggler-port FILE_SMUGGLER_PORT
                        Http file smuggler server port (default: 8888).
  -i, --insecure        Allows any Villain client (sibling server) to connect
                        to your instance without prompting you for
                        verification.
  -c, --certfile CERTFILE
                        Path to your ssl certificate (for HoaxShell https
                        server).
  -k, --keyfile KEYFILE
                        Path to the private key for your certificate (for
                        HoaxShell https server).
  -v, --version         Show program's version number and exit.
  -q, --quiet           Do not print the banner on startup.
Updated on: 2025-Dec-09
 Edit this page
vboot-utils
vlan
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install villain`，再执行 `villain --version` 2>/dev/null || `villain -V`
- [ ] **2.** **读官方帮助** —— `villain -h`，需要细节时 `man villain`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `villain -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/villain/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/villain/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/villain/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
