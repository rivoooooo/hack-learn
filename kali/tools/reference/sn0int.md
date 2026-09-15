# sn0int

> Semi-automatic OSINT framework and package manager sn0int is a semi-automatic OSINT framework and package manager. It was built for IT security professionals and bug hunters to gather intelligence about a given target or about yourself. sn…

> **功能分类**：通用工具 ｜ **Kali 包**：`sn0int` ｜ **官方文档**：<https://www.kali.org/tools/sn0int/>

## 1. 安装

```bash
sudo apt update
sudo apt install sn0int
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.26.1 |
| 架构 | any |
| 可执行命令 | `sn0int` |
| 依赖 | `libc6`、`libgcc-s1`、`libseccomp2`、`libsodium26`、`libsqlite3-0`、`publicsuffix` |
| 安装体积 | 16.86 MB |
| 官网 | <https://github.com/kpcyrd/sn0int> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sn0int> |
| 包追踪 | <https://pkg.kali.org/pkg/sn0int> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sn0int -h          # 查看用法
man sn0int         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sn0int`

官方给出的调用示例：`sn0int -h`

```text
root@kali:~# sn0int -h
Usage: sn0int [OPTIONS] [COMMAND]
Commands:
  run          Run a module directly
  sandbox      For internal use
  login        Login to the registry for publishing
  new          Create a new module
  publish      Publish a script to the registry
  install      Install a module from the registry
  search       Search in the registry
  pkg          The sn0int package manager
  add          Insert into the database
  select       Select from the database
  delete       Delete from the database
  activity     Query logged activity
  scope        Include entities in the scope
  noscope      Exclude entities from scope
  autoscope    Manage autoscope rules
  autonoscope  Manage autonoscope rules
  rescope      Rescope all entities based on autonoscope rules
  workspace    Manage workspaces
  cal          Calendar
  notify       Notify
  fsck         Verify blob storage for corrupt and dangling blobs
  export       Export a workspace for external processing
  stats        Show statistics about your current workspace
  repl         Run a lua repl
  paths        Show paths of various file system locations
  completions  Generate shell completions
  help         Print this message or the help of the given subcommand(s)
Options:
  -w, --workspace <WORKSPACE>  Select a different workspace instead of the default [env: SN0INT_WORKSPACE=]
  -h, --help                   Print help
  -V, --version                Print version
Updated on: 2026-Jun-17
 Edit this page
shell-gpt
spire
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sn0int`，再执行 `sn0int --version` 2>/dev/null || `sn0int -V`
- [ ] **2.** **读官方帮助** —— `sn0int -h`，需要细节时 `man sn0int`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sn0int [OPTIONS] [COMMAND]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sn0int/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sn0int/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sn0int/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
