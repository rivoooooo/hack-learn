# sliver

> Implant framework This package contains a general purpose cross-platform implant framework that supports C2 over Mutual-TLS, HTTP(S), and DNS. Implants are dynamically compiled with unique X.509 certificates signed by a per-instance certif…

> **功能分类**：通用工具 ｜ **Kali 包**：`sliver` ｜ **官方文档**：<https://www.kali.org/tools/sliver/>

## 1. 安装

```bash
sudo apt update
sudo apt install sliver
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.7.1 |
| 架构 | amd64 |
| 可执行命令 | `sliver`、`sliver-client`、`sliver-server` |
| 安装体积 | 290.89 MB |
| 官网 | <https://github.com/BishopFox/sliver> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sliver> |
| 包追踪 | <https://pkg.kali.org/pkg/sliver> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sliver -h          # 查看用法
man sliver         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sliver-client`

> 官方示例调用：`sliver-client -h`

```text
root@kali:~# sliver-client -h
Usage:
  sliver-client [flags]
  sliver-client [command]
Available Commands:
  completion  Generate the autocompletion script for the specified shell
  console     Start the sliver client console
  help        Help about any command
  implant     Implant commands
  import      Import a client configuration file
  mcp         Start the MCP stdio server
  version     Print version and exit
Flags:
  -h, --help        help for sliver-client
      --rc string   path to rc script file
Use "sliver-client [command] --help" for more information about a command.
```

### `sliver-server`

> 官方示例调用：`sliver-server -h`

```text
root@kali:~# sliver-server -h
Usage:
  sliver-server [flags]
  sliver-server [command]
Available Commands:
  builder     Start the process as an external builder
  completion  Generate the autocompletion script for the specified shell
  daemon      Force start server in daemon mode
  export-ca   Export certificate authority
  help        Help about any command
  import-ca   Import certificate authority
  operator    Generate operator configuration files
  unpack      Unpack assets and exit
  version     Print version and exit
Flags:
  -h, --help        help for sliver-server
      --rc string   path to rc script file
Use "sliver-server [command] --help" for more information about a command.
Updated on: 2026-Mar-13
 Edit this page
sipvicious
spike
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sliver`，再执行 `sliver --version` 2>/dev/null || `sliver -V`
- [ ] **2.** **读官方帮助** —— `sliver -h`，需要细节时 `man sliver`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sliver/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[sliver](../../tools/tutorials/12-基础设施与C2/sliver.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sliver/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sliver/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
