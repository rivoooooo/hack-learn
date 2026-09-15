# nishang

> Collection of PowerShell scripts and payloads Nishang is a framework and collection of scripts and payloads which enables usage of PowerShell for offensive security and post exploitation during Penetration Tests. The scripts are written on…

> **功能分类**：Web 应用 ｜ **Kali 包**：`nishang` ｜ **官方文档**：<https://www.kali.org/tools/nishang/>

## 1. 安装

```bash
sudo apt update
sudo apt install nishang
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.7.6 |
| 架构 | all |
| 可执行命令 | `nishang` |
| 依赖 | `kali-defaults` |
| 安装体积 | 6.41 MB |
| 官网 | <https://github.com/samratashok/nishang> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/nishang> |
| 包追踪 | <https://pkg.kali.org/pkg/nishang> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# ls -l /usr/share/nishang/
total 48
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Antak-WebShell
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Backdoors
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Escalation
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Execution
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Gather
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Misc
-rw-r--r-- 1 root root  495 Jun  4 11:14 nishang.psm1
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Pivot
drwxr-xr-x 2 root root 4096 Jun  4 11:15 powerpreter
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Prasadhak
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Scan
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Utility
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ls`

> 官方示例调用：`ls -l /usr/share/nishang/`

```text
root@kali:~# ls -l /usr/share/nishang/
total 48
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Antak-WebShell
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Backdoors
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Escalation
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Execution
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Gather
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Misc
-rw-r--r-- 1 root root  495 Jun  4 11:14 nishang.psm1
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Pivot
drwxr-xr-x 2 root root 4096 Jun  4 11:15 powerpreter
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Prasadhak
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Scan
drwxr-xr-x 2 root root 4096 Jun  4 11:15 Utility
```

### `nishang`

> 官方示例调用：`nishang -h`

```text
root@kali:~# nishang -h
> nishang ~ Collection of PowerShell scripts and payloads
/usr/share/nishang
|-- ActiveDirectory
|-- Antak-WebShell
|-- Backdoors
|-- Bypass
|-- Client
|-- Escalation
|-- Execution
|-- Gather
|-- MITM
|-- Misc
|-- Pivot
|-- Prasadhak
|-- Scan
|-- Shells
|-- Utility
|-- nishang.psm1
`-- powerpreter
Updated on: 2025-Dec-09
 Edit this page
nextnet
obsidian
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install nishang`，再执行 `nishang --version` 2>/dev/null || `nishang -V`
- [ ] **2.** **读官方帮助** —— `nishang -h`，需要细节时 `man nishang`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `nishang -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/nishang/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/execution.md`](../../tools/by-attack/execution.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/nishang/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/nishang/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
