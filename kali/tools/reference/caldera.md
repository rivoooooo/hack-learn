# caldera

> Scalable Automated Adversary Emulation Platform This package contains a cyber security framework designed to easily automate adversary emulation, assist manual red-teams, and automate incident response.

> **功能分类**：通用工具 ｜ **Kali 包**：`caldera` ｜ **官方文档**：<https://www.kali.org/tools/caldera/>

## 1. 安装

```bash
sudo apt update
sudo apt install caldera
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.3.0 |
| 架构 | all |
| 可执行命令 | `caldera` |
| 依赖 | `adduser`、`curl`、`git`、`golang-go`、`python3`、`python3-aioftp`、`python3-aiohttp`、`python3-aiohttp-apispec`、`python3-aiohttp-jinja2`、`python3-aiohttp-security`、`python3-aiohttp-session`、`python3-asyncssh` 等 |
| 安装体积 | 69.94 MB |
| 官网 | <https://github.com/mitre/caldera> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/caldera> |
| 包追踪 | <https://pkg.kali.org/pkg/caldera> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
caldera -h          # 查看用法
man caldera         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `caldera`

> 官方示例调用：`caldera -h`

```text
root@kali:~# caldera -h
usage: server.py [-h] [-E ENVIRONMENT]
                 [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--fresh]
                 [-P PLUGINS] [--insecure] [--uidev UIDEVHOST] [--build]
 ██████╗ █████╗ ██╗     ██████╗ ███████╗██████╗  █████╗
██╔════╝██╔══██╗██║     ██╔══██╗██╔════╝██╔══██╗██╔══██╗
██║     ███████║██║     ██║  ██║█████╗  ██████╔╝███████║
██║     ██╔══██║██║     ██║  ██║██╔══╝  ██╔══██╗██╔══██║
╚██████╗██║  ██║███████╗██████╔╝███████╗██║  ██║██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
options:
  -h, --help            show this help message and exit
  -E, --environment ENVIRONMENT
                        Select an env. file to use
  -l, --log {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level
  --fresh               remove object_store on start
  -P, --plugins PLUGINS
                        Start up with a single plugin
  --insecure            Start caldera with insecure default config values.
                        Equivalent to "-E default".
  --uidev UIDEVHOST     Start VueJS dev server for front-end alongside the
                        caldera server. Provide hostname, i.e. localhost.
  --build               Build the VueJS front-end to serve it from the caldera
                        server.
Updated on: 2026-Aug-25
 Edit this page
caido-cli
calico
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install caldera`，再执行 `caldera --version` 2>/dev/null || `caldera -V`
- [ ] **2.** **读官方帮助** —— `caldera -h`，需要细节时 `man caldera`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `caldera -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/caldera/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/caldera/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/caldera/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
