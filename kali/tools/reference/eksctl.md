# eksctl

> Official CLI for Amazon EKS (program) eksctl is a simple CLI tool for creating clusters on EKS - Amazon’s new managed Kubernetes service for EC2. It is written in Go, and uses CloudFormation. You can create a cluster in minutes with just o…

> **功能分类**：通用工具 ｜ **Kali 包**：`eksctl` ｜ **官方文档**：<https://www.kali.org/tools/eksctl/>

## 1. 安装

```bash
sudo apt update
sudo apt install eksctl
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.230.0 |
| 架构 | amd64 |
| 可执行命令 | `eksctl` |
| 安装体积 | 146.11 MB |
| 官网 | <https://github.com/weaveworks/eksctl> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/eksctl> |
| 包追踪 | <https://pkg.kali.org/pkg/eksctl> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
eksctl -h          # 查看用法
man eksctl         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `eksctl`

官方给出的调用示例：`eksctl -h`

```text
root@kali:~# eksctl -h
The official CLI for Amazon EKS
Usage: eksctl [command] [flags]
Commands:
  eksctl anywhere                        EKS anywhere
  eksctl associate                       Associate resources with a cluster
  eksctl completion                      Generates shell completion scripts for bash, zsh or fish
  eksctl create                          Create resource(s)
  eksctl delete                          Delete resource(s)
  eksctl deregister                      Deregister a non-EKS cluster
  eksctl disassociate                    Disassociate resources from a cluster
  eksctl drain                           Drain resource(s)
  eksctl enable                          Enable features in a cluster
  eksctl get                             Get resource(s)
  eksctl help                            Help about any command
  eksctl info                            Output the version of eksctl, kubectl and OS info
  eksctl register                        Register a non-EKS cluster
  eksctl scale                           Scale resources(s)
  eksctl set                             Set values
  eksctl unset                           Unset values
  eksctl update                          Update resource(s)
  eksctl upgrade                         Upgrade resource(s)
  eksctl utils                           Various utils
  eksctl version                         Output the version of eksctl
Common flags:
  -C, --color string   toggle colorized logs (valid options: true, false, fabulous) (default "true")
  -d, --dumpLogs       dump logs to disk on failure if set to true
  -h, --help           help for this command
  -v, --verbose int    set log level, use 0 to silence, 4 for debugging and 5 for debugging with AWS debug logging (default 3)
Use 'eksctl [command] --help' for more information about a command.
For detailed docs go to https://eksctl.io/
Updated on: 2026-Aug-25
 Edit this page
dvwa
ethtool
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install eksctl`，再执行 `eksctl --version` 2>/dev/null || `eksctl -V`
- [ ] **2.** **读官方帮助** —— `eksctl -h`，需要细节时 `man eksctl`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: eksctl [command] [flags]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/eksctl/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/eksctl/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/eksctl/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
