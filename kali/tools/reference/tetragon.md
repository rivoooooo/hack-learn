# tetragon

> EBPF-based Security Observability and Runtime Enforcement (tetra CLI) Cilium’s new Tetragon component enables powerful realtime, eBPF-based Security Observability and Runtime Enforcement. Tetragon detects and is able to react to security-s…

> **功能分类**：通用工具 ｜ **Kali 包**：`tetragon` ｜ **官方文档**：<https://www.kali.org/tools/tetragon/>

## 1. 安装

```bash
sudo apt update
sudo apt install tetragon
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.7.0 |
| 架构 | amd64 |
| 可执行命令 | `tetragon`、`tetra` |
| 依赖 | `bpftool`、`libc6`、`tetra` |
| 安装体积 | 50.70 MB |
| 官网 | <https://github.com/cilium/tetragon> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/tetragon> |
| 包追踪 | <https://pkg.kali.org/pkg/tetragon> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
tetragon -h          # 查看用法
man tetragon         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tetra`

> 官方示例调用：`tetra -h`

```text
root@kali:~# tetra -h
Tetragon CLI
Usage:
  tetra [flags]
  tetra [command]
Available Commands:
  bugtool       Produce a tar archive with debug information
  completion    Generate the autocompletion script for the specified shell
  cri           connect to CRI
  eventlog      Manage event exporter logging parameters
  explain       List the fields for supported resources
  getevents     Print events
  help          Help about any command
  info          Retrieve information from the server
  loglevel      Get and dynamically change the log level
  policytest    Tetragon policy tests
  probe         Probe for eBPF system features availability
  status        Print health status
  tracingpolicy Manage tracing policies
  version       Print version from CLI and server
Flags:
  -d, --debug                   Enable debug messages
  -h, --help                    help for tetra
      --max-recv-size int       Maximum gRPC message size in bytes the client can receive (default 10485760)
      --retries int             Connection retries with exponential backoff (default 1)
      --server-address string   gRPC server address
      --timeout duration        Connection timeout (default 30s)
Use "tetra [command] --help" for more information about a command.
Learn more with
OffSec
Want to learn more about tetragon? get access to in-depth training and hands-on labs:
Cloud Essentials: 2. Cloud Architecture Overview
Updated on: 2026-May-25
 Edit this page
swaks
thc-ipv6
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install tetragon`，再执行 `tetragon --version` 2>/dev/null || `tetragon -V`
- [ ] **2.** **读官方帮助** —— `tetragon -h`，需要细节时 `man tetragon`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/tetragon/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/tetragon/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/tetragon/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
