# hexstrike-ai

> AI-Powered MCP Cybersecurity Automation Platform This package contains an HexStrike AI MCP v6.0 which features a multi-agent architecture with autonomous AI agents, intelligent decision-making, and vulnerability intelligence.

> **功能分类**：通用工具 ｜ **Kali 包**：`hexstrike-ai` ｜ **官方文档**：<https://www.kali.org/tools/hexstrike-ai/>

## 1. 安装

```bash
sudo apt update
sudo apt install hexstrike-ai
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0~git20260306.8333779 |
| 架构 | all |
| 可执行命令 | `hexstrike-ai`、`hexstrike_mcp`、`hexstrike_server` |
| 依赖 | `mitmproxy`、`python3`、`python3-aiohttp`、`python3-bs4`、`python3-flask`、`python3-mcp`、`python3-psutil`、`python3-pwntools`、`python3-requests`、`python3-selenium`、`hexstrike_mcp` |
| 安装体积 | 2.75 MB |
| 官网 | <https://github.com/0x4m4/hexstrike-ai> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/hexstrike-ai> |
| 包追踪 | <https://pkg.kali.org/pkg/hexstrike-ai> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
hexstrike-ai -h          # 查看用法
man hexstrike-ai         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hexstrike_mcp`

> 官方示例调用：`hexstrike_mcp -h`

```text
root@kali:~# hexstrike_mcp -h
usage: hexstrike_mcp.py [-h] [--server SERVER] [--timeout TIMEOUT] [--debug]
Run the HexStrike AI MCP Client
options:
  -h, --help         show this help message and exit
  --server SERVER    HexStrike AI API server URL (default:
                     http://127.0.0.1:8888)
  --timeout TIMEOUT  Request timeout in seconds (default: 300)
  --debug            Enable debug logging
```

### `hexstrike_server`

> 官方示例调用：`hexstrike_server -h`

```text
root@kali:~# hexstrike_server -h
2026-09-14 06:00:05,657 - __main__ - INFO - 🔧 Process pool worker 0 started
2026-09-14 06:00:05,657 - __main__ - INFO - 🔧 Process pool worker 1 started
2026-09-14 06:00:05,657 - __main__ - INFO - 🔧 Process pool worker 2 started
2026-09-14 06:00:05,657 - __main__ - INFO - 🔧 Process pool worker 3 started
██╗  ██╗███████╗██╗  ██╗███████╗████████╗██████╗ ██╗██╗  ██╗███████╗
██║  ██║██╔════╝╚██╗██╔╝██╔════╝╚══██╔══╝██╔══██╗██║██║ ██╔╝██╔════╝
███████║█████╗   ╚███╔╝ ███████╗   ██║   ██████╔╝██║█████╔╝ █████╗
██╔══██║██╔══╝   ██╔██╗ ╚════██║   ██║   ██╔══██╗██║██╔═██╗ ██╔══╝
██║  ██║███████╗██╔╝ ██╗███████║   ██║   ██║  ██║██║██║  ██╗███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝
┌─────────────────────────────────────────────────────────────────────┐
│  🚀 HexStrike AI - Blood-Red Offensive Intelligence Core        │
│  ⚡ AI-Automated Recon | Exploitation | Analysis Pipeline          │
│  🎯 Bug Bounty | CTF | Red Team | Zero-Day Research              │
└─────────────────────────────────────────────────────────────────────┘
[INFO] Server starting on 127.0.0.1:8888
[INFO] 150+ integrated modules | Adaptive AI decision engine active
[INFO] Blood-red theme engaged – unified offensive operations UI
usage: hexstrike_server.py [-h] [--debug] [--port PORT]
Run the HexStrike AI API Server
options:
  -h, --help   show this help message and exit
  --debug      Enable debug mode
  --port PORT  Port for the API server (default: 8888)
Updated on: 2026-Aug-25
 Edit this page
heartleech
hivex
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install hexstrike-ai`，再执行 `hexstrike-ai --version` 2>/dev/null || `hexstrike-ai -V`
- [ ] **2.** **读官方帮助** —— `hexstrike-ai -h`，需要细节时 `man hexstrike-ai`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `hexstrike-ai -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hexstrike-ai/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[hexstrike-ai](../../tools/tutorials/12-基础设施与C2/hexstrike-ai.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hexstrike-ai/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hexstrike-ai/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
