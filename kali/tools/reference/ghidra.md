# ghidra

> Software Reverse Engineering Framework This package contains a software reverse engineering (SRE) framework created and maintained by the National Security Agency Research Directorate. This framework includes a suite of full-featured, high…

> **功能分类**：事件响应 ｜ **Kali 包**：`ghidra` ｜ **官方文档**：<https://www.kali.org/tools/ghidra/>

## 1. 安装

```bash
sudo apt update
sudo apt install ghidra
```

| 项目 | 内容 |
|------|------|
| 版本 | 12.1.3 |
| 架构 | amd64 |
| 可执行命令 | `ghidra` |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6`、`openjdk-25-jdk` |
| 安装体积 | 823.27 MB |
| 官网 | <https://github.com/NationalSecurityAgency/ghidra> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ghidra> |
| 包追踪 | <https://pkg.kali.org/pkg/ghidra> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ghidra -h          # 查看用法
man ghidra         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ghidra`

官方给出的调用示例：`ghidra -h`

```text
root@kali:~# ghidra -h
Exited with error.  Run in foreground (fg) mode for more details.
Updated on: 2026-Aug-25
 Edit this page
gemini-cli
glibc
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ghidra`，再执行 `ghidra --version` 2>/dev/null || `ghidra -V`
- [ ] **2.** **读官方帮助** —— `ghidra -h`，需要细节时 `man ghidra`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `ghidra -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ghidra/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[ghidra](../../tools/tutorials/10-逆向工程/ghidra.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ghidra/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ghidra/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
