# legion

> Semi-automated network penetration testing tool This package contains an open source, easy-to-use, super-extensible and semi-automated network penetration testing tool that aids in discovery, reconnaissance and exploitation of information …

> **功能分类**：信息搜集 ｜ **Kali 包**：`legion` ｜ **官方文档**：<https://www.kali.org/tools/legion/>

## 1. 安装

```bash
sudo apt update
sudo apt install legion
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.7.0 |
| 架构 | any |
| 可执行命令 | `legion` |
| 依赖 | `dirbuster`、`dnsmap`、`enum4linux` |
| 安装体积 | 7.51 MB |
| 官网 | <https://github.com/Hackman238/legion> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/legion> |
| 包追踪 | <https://pkg.kali.org/pkg/legion> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
legion -h          # 查看用法
man legion         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `legion`

> 官方示例调用：`legion -h`

```text
root@kali:~# legion -h
usage: legion.py [-h] [--mcp-server] [--headless] [--web] [--tool-audit |
                 --tool-install-plan {kali,ubuntu} |
                 --tool-install {kali,ubuntu}] [--web-port WEB_PORT]
                 [--web-bind-all] [--web-transparent-ui]
                 [--input-file INPUT_FILE] [--discovery] [--staged-scan]
                 [--output-file OUTPUT_FILE] [--run-actions]
Start Legion
options:
  -h, --help            show this help message and exit
  --mcp-server          Start MCP server for AI integration
  --headless            Run Legion in headless (CLI) mode
  --web                 Run Legion with the local Flask web interface
  --tool-audit          Print a tool availability audit and exit
  --tool-install-plan {kali,ubuntu}
                        Print the generated install script for missing tools
                        on the selected platform and exit
  --tool-install {kali,ubuntu}
                        Run the generated install plan for missing tools on
                        the selected platform and exit
  --web-port WEB_PORT   Local web interface port
  --web-bind-all        When used with --web, bind the web interface to
                        0.0.0.0 instead of 127.0.0.1
  --web-transparent-ui  When used with --web, enable transparent UI effects
  --input-file INPUT_FILE
                        Text file with targets (hostnames, subnets, IPs, etc.)
  --discovery           Enable host discovery (default: enabled)
  --staged-scan         Enable staged scan
  --output-file OUTPUT_FILE
                        Output file (.legion or .json)
  --run-actions         Run scripted actions/automated attacks after
                        scan/import
Updated on: 2026-May-25
 Edit this page
kustomize
libimage-exiftool-perl
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install legion`，再执行 `legion --version` 2>/dev/null || `legion -V`
- [ ] **2.** **读官方帮助** —— `legion -h`，需要细节时 `man legion`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `legion -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/legion/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/legion/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/legion/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
