# terraform

> Tool for building, changing, and versioning infrastructure This package contains a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as cu…

> **功能分类**：通用工具 ｜ **Kali 包**：`terraform` ｜ **官方文档**：<https://www.kali.org/tools/terraform/>

## 1. 安装

```bash
sudo apt update
sudo apt install terraform
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6.3 |
| 架构 | any |
| 可执行命令 | `terraform` |
| 依赖 | `libc6` |
| 安装体积 | 77.16 MB |
| 官网 | <https://github.com/hashicorp/terraform> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/terraform> |
| 包追踪 | <https://pkg.kali.org/pkg/terraform> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
terraform -h          # 查看用法
man terraform         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `terraform`

官方给出的调用示例：`terraform -h`

```text
root@kali:~# terraform -h
Usage: terraform [global options] <subcommand> [args]
The available commands for execution are listed below.
The primary workflow commands are given first, followed by
less common or more advanced commands.
Main commands:
  init          Prepare your working directory for other commands
  validate      Check whether the configuration is valid
  plan          Show changes required by the current configuration
  apply         Create or update infrastructure
  destroy       Destroy previously-created infrastructure
All other commands:
  console       Try Terraform expressions at an interactive command prompt
  fmt           Reformat your configuration in the standard style
  force-unlock  Release a stuck lock on the current workspace
  get           Install or upgrade remote Terraform modules
  graph         Generate a Graphviz graph of the steps in an operation
  import        Associate existing infrastructure with a Terraform resource
  login         Obtain and save credentials for a remote host
  logout        Remove locally-stored credentials for a remote host
  metadata      Metadata related commands
  output        Show output values from your root module
  providers     Show the providers required for this configuration
  refresh       Update the state to match remote systems
  show          Show the current state or a saved plan
  state         Advanced state management
  taint         Mark a resource instance as not fully functional
  test          Execute integration tests for Terraform modules
  untaint       Remove the 'tainted' state from a resource instance
  version       Show the current Terraform version
  workspace     Workspace management
Global options (use these before the subcommand, if any):
  -chdir=DIR    Switch to a different working directory before executing the
                given subcommand.
  -help         Show this help output, or the help for a specified subcommand.
  -version      An alias for the "version" subcommand.
Learn more with
OffSec
Want to learn more about terraform? get access to in-depth training and hands-on labs:
Introduction to Cloud Security: 19. Introduction to Terraform
Updated on: 2025-Dec-09
 Edit this page
termineter
tftpd32
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install terraform`，再执行 `terraform --version` 2>/dev/null || `terraform -V`
- [ ] **2.** **读官方帮助** —— `terraform -h`，需要细节时 `man terraform`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: terraform [global options] <subcommand> [args]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/terraform/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/terraform/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/terraform/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
