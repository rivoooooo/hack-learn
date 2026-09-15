# calico

> Networking and network security solution for Kubernetes This package contains the command line tool for calico. Calico is a widely adopted, battle-tested open source networking and network security solution for Kubernetes, virtual machines…

> **功能分类**：通用工具 ｜ **Kali 包**：`calico` ｜ **官方文档**：<https://www.kali.org/tools/calico/>

## 1. 安装

```bash
sudo apt update
sudo apt install calicoctl
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.32.1 |
| 架构 | any |
| 可执行命令 | `calicoctl` |
| 依赖 | `libc6`、`calicoctl` |
| 安装体积 | 64.69 MB |
| 官网 | <https://github.com/projectcalico/calico> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/calico> |
| 包追踪 | <https://pkg.kali.org/pkg/calico> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
calicoctl -h          # 查看用法
man calicoctl         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `calicoctl`

官方给出的调用示例：`calicoctl -h`

```text
root@kali:~# calicoctl -h
Usage:
  calicoctl [options] <command> [<args>...]
    create       Create a resource by file, directory or stdin.
    replace      Replace a resource by file, directory or stdin.
    apply        Apply a resource by file, directory or stdin.  This creates a resource
                 if it does not exist, and replaces a resource if it does exists.
    patch        Patch a preexisting resource in place.
    delete       Delete a resource identified by file, directory, stdin or resource type and
                 name.
    get          Get a resource identified by file, directory, stdin or resource type and
                 name.
    label        Add or update labels of resources.
    validate     Validate a resource by file, directory or stdin without applying it.
    ipam         IP address management.
    node         Calico node management.
    version      Display the version of this binary.
    datastore    Calico datastore management.
    cluster      Access cluster information.
Options:
  -h --help                    Show this screen.
  -l --log-level=<level>       Set the log level (one of panic, fatal, error,
                               warn, info, debug) [default: panic]
     --context=<context>       The name of the kubeconfig context to use.
     --allow-version-mismatch  Allow client and cluster versions mismatch.
Description:
  The calicoctl command line tool is used to manage Calico network and security
  policy, to view and manage endpoint configuration, and to manage a Calico
  node instance.
  See 'calicoctl <command> --help' to read about a specific subcommand.
Updated on: 2026-Aug-25
 Edit this page
caldera
capstone
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install calicoctl`，再执行 `calicoctl --version` 2>/dev/null || `calicoctl -V`
- [ ] **2.** **读官方帮助** —— `calicoctl -h`，需要细节时 `man calicoctl`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/calico/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/calico/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/calico/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
