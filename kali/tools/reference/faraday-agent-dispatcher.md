# faraday-agent-dispatcher

> Helper to develop integrations with Faraday (Python 3) This package contains Faraday Agents Dispatcher. It helps user develop integrations with Faraday written in any language. This package installs the library for Python 3.

> **功能分类**：通用工具 ｜ **Kali 包**：`faraday-agent-dispatcher` ｜ **官方文档**：<https://www.kali.org/tools/faraday-agent-dispatcher/>

## 1. 安装

```bash
sudo apt update
sudo apt install faraday-agent-dispatcher
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.2.1 |
| 架构 | all |
| 可执行命令 | `faraday-agent-dispatcher`、`faraday-dispatcher` |
| 依赖 | `python3`、`python3-aiohttp`、`python3-click`、`python3-faraday-agent-parameters-types`、`python3-faraday-plugins`、`python3-gvm`、`python3-itsdangerous`、`python3-psutil`、`python3-requests`、`python3-socketio`、`python3-syslog-rfc5424-formatter`、`python3-websockets` 等 |
| 安装体积 | 284 KB |
| 官网 | <https://github.com/infobyte/faraday_agent_dispatcher> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/faraday-agent-dispatcher> |
| 包追踪 | <https://pkg.kali.org/pkg/faraday-agent-dispatcher> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
faraday-agent-dispatcher -h          # 查看用法
man faraday-agent-dispatcher         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `faraday-dispatcher`

官方给出的调用示例：`faraday-dispatcher -h`

```text
root@kali:~# faraday-dispatcher -h
Usage: faraday-dispatcher [OPTIONS] COMMAND [ARGS]...
Options:
  -v, --version  Show the version and exit.
  -h, --help     Show this message and exit.
Commands:
  config-wizard  faraday-dispatcher config_wizard
  run            faraday-dispatcher run
Updated on: 2025-Dec-09
 Edit this page
eyewitness
fatcat
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install faraday-agent-dispatcher`，再执行 `faraday-agent-dispatcher --version` 2>/dev/null || `faraday-agent-dispatcher -V`
- [ ] **2.** **读官方帮助** —— `faraday-agent-dispatcher -h`，需要细节时 `man faraday-agent-dispatcher`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: faraday-dispatcher [OPTIONS] COMMAND [ARGS]...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/faraday-agent-dispatcher/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/faraday-agent-dispatcher/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/faraday-agent-dispatcher/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
