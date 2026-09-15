# kali-tweaks

> Tool to adjust advanced configuration settings for Kali Linux This package provides tweaks for Kali Linux. This include things like: Shell configuration APT mirrors configuration Kali Linux metapackages installation and removal

> **功能分类**：通用工具 ｜ **Kali 包**：`kali-tweaks` ｜ **官方文档**：<https://www.kali.org/tools/kali-tweaks/>

## 1. 安装

```bash
sudo apt update
sudo apt install kali-tweaks
```

| 项目 | 内容 |
|------|------|
| 版本 | 2026.2.0 |
| 架构 | all |
| 可执行命令 | `kali-tweaks` |
| 依赖 | `kali-defaults`、`python3`、`python3-newt` |
| 安装体积 | 157 KB |
| 官网 | <https://gitlab.com/kalilinux/packages/kali-tweaks> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/kali-tweaks> |
| 包追踪 | <https://pkg.kali.org/pkg/kali-tweaks> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
kali-tweaks -h          # 查看用法
man kali-tweaks         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `kali-tweaks`

官方给出的调用示例：`kali-tweaks -h`

```text
root@kali:~# kali-tweaks -h
 ┌───────────────────────────────┤ Main Menu ├────────────────────────────────┐
 │                                                                            │
 │ Hardening              Configure the system for extra security             │
 │ Metapackages           Install specific subsets of tools for particular ne │
 │ Network Repositories   Configure network repositories for APT sources      │
 │ Shell & Prompt         Configure the shell and command prompt              │
 │ Virtualization         Additional configurations for Virtual Machines      │
 │                                                                            │
 │                                                                            │
 │                                                                            │
 │                                                                            │
 │                                                                            │
 │                                                                            │
 │                                                                            │
 │                                                                            │
 │                <Select>                              <Quit>                │
 │                                                                            │
 └────────────────────────────────────────────────────────────────────────────┘
  <Tab>/<Alt-Tab> between elements   |  <Space> selects   |  <F12> next screen
Updated on: 2026-Aug-25
 Edit this page
kali-meta
kubernetes-helm
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install kali-tweaks`，再执行 `kali-tweaks --version` 2>/dev/null || `kali-tweaks -V`
- [ ] **2.** **读官方帮助** —— `kali-tweaks -h`，需要细节时 `man kali-tweaks`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `kali-tweaks -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/kali-tweaks/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/kali-tweaks/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/kali-tweaks/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
