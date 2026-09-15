# metasploitmcp

> MCP Server for Metasploit A Model Context Protocol (MCP) server for Metasploit Framework integration.

> **功能分类**：通用工具 ｜ **Kali 包**：`metasploitmcp` ｜ **官方文档**：<https://www.kali.org/tools/metasploitmcp/>

## 1. 安装

```bash
sudo apt update
sudo apt install metasploitmcp
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0~git20260205.afc792d |
| 架构 | all |
| 可执行命令 | `metasploitmcp` |
| 依赖 | `python3`、`python3-fastapi`、`python3-fastmcp`、`python3-mcp`、`python3-pymetasploit3`、`python3-uvicorn` |
| 安装体积 | 104 KB |
| 官网 | <https://github.com/GH05TCREW/MetasploitMCP> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/metasploitmcp> |
| 包追踪 | <https://pkg.kali.org/pkg/metasploitmcp> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
metasploitmcp -h          # 查看用法
man metasploitmcp         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `metasploitmcp`

官方给出的调用示例：`metasploitmcp -h`

```text
root@kali:~# metasploitmcp -h
usage: MetasploitMCP.py [-h] [--transport {http,stdio}] [--host HOST]
                        [--port PORT] [--reload] [--find-port] [--debug]
Run Streamlined Metasploit MCP Server
options:
  -h, --help            show this help message and exit
  --transport {http,stdio}
                        MCP transport mode to use (http=SSE, stdio=direct
                        pipe)
  --host HOST           Host to bind the HTTP server to (default: 127.0.0.1)
  --port PORT           Port to listen on (default: find available from 8085)
  --reload              Enable auto-reload (for development)
  --find-port           Force finding an available port starting from --port
                        or 8085
  --debug               Make output more verbose
Updated on: 2026-May-25
 Edit this page
mdbtools
msitools
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install metasploitmcp`，再执行 `metasploitmcp --version` 2>/dev/null || `metasploitmcp -V`
- [ ] **2.** **读官方帮助** —— `metasploitmcp -h`，需要细节时 `man metasploitmcp`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `metasploitmcp -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/metasploitmcp/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/metasploitmcp/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/metasploitmcp/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
