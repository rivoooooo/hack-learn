# spire

> Toolchain of APIs for establishing trust between software systems This package contains SPIRE (the SPIFFE Runtime Environment). It is a toolchain of APIs for establishing trust between software systems across a wide variety of hosting plat…

> **功能分类**：通用工具 ｜ **Kali 包**：`spire` ｜ **官方文档**：<https://www.kali.org/tools/spire/>

## 1. 安装

```bash
sudo apt update
sudo apt install spire
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.15.0 |
| 架构 | amd64 |
| 可执行命令 | `spire`、`spire-agent`、`spire-server` |
| 依赖 | `libc6`、`spire-agent` |
| 安装体积 | 204.56 MB |
| 官网 | <https://github.com/spiffe/spire> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/spire> |
| 包追踪 | <https://pkg.kali.org/pkg/spire> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
spire -h          # 查看用法
man spire         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `spire-agent`

> 官方示例调用：`spire-agent -h`

```text
root@kali:~# spire-agent -h
Usage: spire-agent [--version] [--help] <command> [<args>]
Available commands are:
    api
    healthcheck    Determines agent health status
    run            Runs the agent
    validate       Validates a SPIRE agent configuration file
```

### `spire-server`

> 官方示例调用：`spire-server -h`

```text
root@kali:~# spire-server -h
Usage: spire-server [--version] [--help] <command> [<args>]
Available commands are:
    agent
    bundle
    entry
    federation
    healthcheck          Determines server health status
    jwt
    localauthority
    logger
    run                  Runs the server
    token
    upstreamauthority
    validate             Validates a SPIRE server configuration file
    x509
Updated on: 2026-Jun-17
 Edit this page
sn0int
ssldump
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install spire`，再执行 `spire --version` 2>/dev/null || `spire -V`
- [ ] **2.** **读官方帮助** —— `spire -h`，需要细节时 `man spire`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: spire-agent [--version] [--help] <command> [<args>]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/spire/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/spire/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/spire/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
