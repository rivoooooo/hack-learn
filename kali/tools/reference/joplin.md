# joplin

> Open source note taking and to-do application This package contains a free, open source note taking and to-do application, which can handle a large number of notes organised into notebooks. The notes are searchable, can be copied, tagged a…

> **功能分类**：通用工具 ｜ **Kali 包**：`joplin` ｜ **官方文档**：<https://www.kali.org/tools/joplin/>

## 1. 安装

```bash
sudo apt update
sudo apt install joplin
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.7.1 |
| 架构 | amd64 |
| 可执行命令 | `joplin`、`joplin-cli` |
| 依赖 | `libasound2t64`、`libatk-bridge2.0-0t64`、`libatk1.0-0t64`、`libatspi2.0-0t64`、`libc6`、`libcairo2`、`libcups2t64`、`libdbus-1-3`、`libexpat1`、`libgbm1`、`libgcc-s1`、`libglib2.0-0t64` 等 |
| 安装体积 | 410.70 MB |
| 官网 | <https://github.com/laurent22/joplin> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/joplin> |
| 包追踪 | <https://pkg.kali.org/pkg/joplin> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
joplin -h          # 查看用法
man joplin         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `joplin-cli`

> 官方示例调用：`joplin-cli -h`

```text
root@kali:~# joplin-cli -h
Unknown flag: -h
Type `joplin help` for usage information.
Updated on: 2026-May-25
 Edit this page
ipv6toolkit
krbrelayx
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install joplin`，再执行 `joplin --version` 2>/dev/null || `joplin -V`
- [ ] **2.** **读官方帮助** —— `joplin -h`，需要细节时 `man joplin`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `joplin -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/joplin/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/joplin/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/joplin/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
