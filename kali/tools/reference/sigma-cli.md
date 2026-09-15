# sigma-cli

> Sigma command line interface This package contains the Sigma command line interface using the pySigma library to manage, list and convert Sigma rules into query languages.

> **功能分类**：通用工具 ｜ **Kali 包**：`sigma-cli` ｜ **官方文档**：<https://www.kali.org/tools/sigma-cli/>

## 1. 安装

```bash
sudo apt update
sudo apt install sigma-cli
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.1.0 |
| 架构 | all |
| 可执行命令 | `sigma-cli` |
| 依赖 | `python3`、`python3-click`、`python3-colorama`、`python3-prettytable`、`python3-sigma` |
| 安装体积 | 126 KB |
| 官网 | <https://github.com/SigmaHQ/sigma-cli> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sigma-cli> |
| 包追踪 | <https://pkg.kali.org/pkg/sigma-cli> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sigma-cli -h          # 查看用法
man sigma-cli         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sigma-cli`

官方给出的调用示例：`sigma-cli -h`

```text
root@kali:~# sigma-cli -h
Usage: sigma-cli [OPTIONS] COMMAND [ARGS]...
Options:
  -h, --help  Show this message and exit.
Commands:
  analyze  Analyze Sigma rule sets
  check    Check Sigma rules for validity and best practices (not yet...
  convert  Convert Sigma rules into queries.
  list     List available targets or processing pipelines.
  plugin   pySigma plugin management (backends, processing pipelines and...
  pysigma  pySigma library management commands.
  version  Print version of Sigma CLI.
Updated on: 2026-Aug-25
 Edit this page
sidguesser
sippts
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sigma-cli`，再执行 `sigma-cli --version` 2>/dev/null || `sigma-cli -V`
- [ ] **2.** **读官方帮助** —— `sigma-cli -h`，需要细节时 `man sigma-cli`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sigma-cli [OPTIONS] COMMAND [ARGS]...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sigma-cli/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sigma-cli/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sigma-cli/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
