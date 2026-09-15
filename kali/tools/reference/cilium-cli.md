# cilium-cli

> Cilium CLI (program) This package contains a CLI to install, manage & troubleshoot Kubernetes clusters running Cilium.

> **功能分类**：通用工具 ｜ **Kali 包**：`cilium-cli` ｜ **官方文档**：<https://www.kali.org/tools/cilium-cli/>

## 1. 安装

```bash
sudo apt update
sudo apt install cilium-cli
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.19.1 |
| 架构 | any |
| 可执行命令 | `cilium-cli`、`cilium` |
| 依赖 | `libc6`、`cilium` |
| 安装体积 | 186.62 MB |
| 官网 | <https://github.com/cilium/cilium-cli> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/cilium-cli> |
| 包追踪 | <https://pkg.kali.org/pkg/cilium-cli> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
cilium-cli -h          # 查看用法
man cilium-cli         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cilium`

官方给出的调用示例：`cilium -h`

```text
root@kali:~# cilium -h
CLI to install, manage, & troubleshooting Cilium clusters running Kubernetes.
Cilium is a CNI for Kubernetes to provide secure network connectivity and
load-balancing with excellent visibility using eBPF
Examples:
Install Cilium in current Kubernetes context
  $ cilium install
Check status of Cilium
  $ cilium status
Enable the Hubble observability layer
  $ cilium hubble enable
Perform a connectivity test
  $ cilium connectivity test
Usage:
  cilium [flags]
  cilium [command]
Available Commands:
  bgp          Access to BGP control plane
  clustermesh  Multi Cluster Management
  completion   Generate the autocompletion script for the specified shell
  config       Manage Configuration
  connectivity Connectivity troubleshooting
  context      Display the configuration context
  encryption   Cilium encryption
  features     Report which features are enabled in Cilium agents
  help         Help about any command
  hubble       Hubble observability
  install      Install Cilium in a Kubernetes cluster using Helm
  multicast    Manage multicast groups
  status       Display status
  sysdump      Collects information required to troubleshoot issues with Cilium and Hubble
  uninstall    Uninstall Cilium using Helm
  upgrade      Upgrade a Cilium installation a Kubernetes cluster using Helm
  version      Display detailed version information
Flags:
      --as string                  Username to impersonate for the operation. User could be a regular user or a service account in a namespace.
      --as-group stringArray       Group to impersonate for the operation, this flag can be repeated to specify multiple groups.
      --context string             Kubernetes configuration context
      --helm-release-name string   Helm release name (default "cilium")
  -h, --help                       help for cilium
      --kubeconfig string          Path to the kubeconfig file
  -n, --namespace string           Namespace Cilium is running in. Can also be set via CILIUM_NAMESPACE env var (default "kube-system")
Use "cilium [command] --help" for more information about a command.
Updated on: 2026-Mar-02
 Edit this page
chaosreader
cisco-global-exploiter
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cilium-cli`，再执行 `cilium-cli --version` 2>/dev/null || `cilium-cli -V`
- [ ] **2.** **读官方帮助** —— `cilium-cli -h`，需要细节时 `man cilium-cli`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cilium-cli/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cilium-cli/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cilium-cli/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
