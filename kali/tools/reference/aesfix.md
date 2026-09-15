# aesfix

> Tool for correcting bit errors in an AES key schedule This program illustrates a technique for correcting bit errors in an AES key schedule. It should be used with the output of the aeskeyfind program. It is limited to AES-128 key schedule…

> **功能分类**：密码学与隐写 ｜ **Kali 包**：`aesfix` ｜ **官方文档**：<https://www.kali.org/tools/aesfix/>

## 1. 安装

```bash
sudo apt update
sudo apt install aesfix
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0.1 |
| 架构 | any |
| 可执行命令 | `aesfix` |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6` |
| 安装体积 | 41 KB |
| 官网 | <https://citp.princeton.edu/our-work/memory/code/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/aesfix> |
| 包追踪 | <https://pkg.kali.org/pkg/aesfix> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
aesfix -h          # 查看用法
man aesfix         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man aesfix`

```text
root@kali:~# man aesfix
aesfix(1)                        User Commands                        aesfix(1)
NAME
     aesfix - Correct bit errors in an AES key schedules
SYNOPSIS
     aesfix SCHEDULE-FILE
DESCRIPTION
     Corrects bit errors in an AES key schedule read from the specified hex-en-
     coded file.
BUGS
     Likely.
SEE ALSO
     biosmemimage(1), aeskeyfind(1) aesfix(1)
AUTHOR
     aesfix was written by Nadia Heninger and J. Alex Halderman.
     This manual page was written by Jacob Appelbaum <
[email protected]
> for
     the Debian system (but may be used by others).  Permission is granted to
     copy, distribute and/or modify this document under the terms of the GNU
     General Public License, Version 2 or any later version published by the
     Free Software Foundation.
User Commands                      08-17-2008                         aesfix(1)
Updated on: 2026-May-25
 Edit this page
adaptixc2
aircrack-ng
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install aesfix`，再执行 `aesfix --version` 2>/dev/null || `aesfix -V`
- [ ] **2.** **读官方帮助** —— `aesfix -h`，需要细节时 `man aesfix`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `aesfix -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/aesfix/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/aesfix/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/aesfix/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
