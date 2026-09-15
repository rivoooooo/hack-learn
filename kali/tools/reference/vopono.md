# vopono

> Run applications through VPN tunnels with temporary network namespaces vopono is a tool to run applications through VPN tunnels via temporary network namespaces. This allows you to run only a handful of applications through different VPNs …

> **功能分类**：通用工具 ｜ **Kali 包**：`vopono` ｜ **官方文档**：<https://www.kali.org/tools/vopono/>

## 1. 安装

```bash
sudo apt update
sudo apt install vopono
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0.1 |
| 架构 | any |
| 可执行命令 | `vopono` |
| 依赖 | `libc6`、`libgcc-s1`、`nftables` |
| 安装体积 | 14.74 MB |
| 官网 | <https://github.com/jamesmcm/vopono> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/vopono> |
| 包追踪 | <https://pkg.kali.org/pkg/vopono> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
vopono -h          # 查看用法
man vopono         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `vopono`

> 官方示例调用：`vopono -h`

```text
root@kali:~# vopono -h
Launch applications in a temporary VPN network namespace
Usage: vopono [OPTIONS] [COMMAND]
Commands:
  daemon     Run or inspect the privileged root vopono daemon
  exec       Execute an application with the given VPN connection
  check      Check network connectivity of a running namespace
  list       List running vopono namespaces and applications
  status     Show active namespaces and applications
  providers  List provider capabilities and configuration state
  provider   Inspect a provider
  stop       Stop a running application or namespace
  sync       Synchronise local server lists with VPN providers
  servers    List possible server configs for VPN provider, beginning with prefix
  help       Print this message or the help of the given subcommand(s)
Options:
  -v, --verbose  Verbose output
      --silent   Suppress all output including application output
  -A, --askpass  read sudo password from program specified in SUDO_ASKPASS environment variable
  -h, --help     Print help
  -V, --version  Print version
Updated on: 2026-Aug-25
 Edit this page
vim
vpnc
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install vopono`，再执行 `vopono --version` 2>/dev/null || `vopono -V`
- [ ] **2.** **读官方帮助** —— `vopono -h`，需要细节时 `man vopono`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: vopono [OPTIONS] [COMMAND]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/vopono/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/vopono/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/vopono/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
