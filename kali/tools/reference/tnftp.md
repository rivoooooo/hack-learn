# tnftp

> tnftp Enhanced ftp client tnftp is what many users affectionately call the enhanced ftp client in NetBSD ( http://www.netbsd.org ).

> **功能分类**：通用工具 ｜ **Kali 包**：`tnftp` ｜ **官方文档**：<https://www.kali.org/tools/tnftp/>

## 1. 安装

```bash
sudo apt update
sudo apt install tnftp
```

| 项目 | 内容 |
|------|------|
| 版本 | 20260211 |
| 架构 | any |
| 可执行命令 | `ftp`、`tnftp` |
| 依赖 | `libc6`、`libedit2`、`libssl3t64` |
| 安装体积 | 259 KB |
| 官网 | <https://en.wikipedia.org/wiki/Tnftp> |
| 源码仓库 | <https://salsa.debian.org/debian/tnftp> |
| 包追踪 | <https://pkg.kali.org/pkg/tnftp> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ftp -h          # 查看用法
man ftp         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tnftp`

> 官方示例调用：`tnftp -h`

```text
root@kali:~# tnftp -h
tnftp: -h: unknown option
usage: tnftp [-46AadefginpRtVv] [-b BUFSIZE] [-H HEADER] [-N NETRC] [-o OUTPUT]
           [-P PORT] [-q QUITTIME] [-r RETRY] [-s SRCADDR] [-T DIR,MAX[,INC]]
           [-x XFERSIZE]
           [[USER@]HOST [PORT]]
           [[USER@]HOST:[PATH][/]]
           [file:///PATH]
           [ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH[/][;type=TYPE]]
           [http://[USER[:PASSWORD]@]HOST[:PORT]/PATH]
           [https://[USER[:PASSWORD]@]HOST[:PORT]/PATH]
           ...
       tnftp -u URL FILE ...
       tnftp -?
Updated on: 2026-May-25
 Edit this page
tightvnc
tree
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install tnftp`，再执行 `ftp --version` 2>/dev/null || `ftp -V`
- [ ] **2.** **读官方帮助** —— `ftp -h`，需要细节时 `man ftp`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `ftp -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/tnftp/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/tnftp/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/tnftp/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
