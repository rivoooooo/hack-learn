# imhex

> Hex Editor for Reverse Engineers, Programmers This package contains a Hex Editor for Reverse Engineers, Programmers and people who value their retinas when working at 3 AM.

> **功能分类**：通用工具 ｜ **Kali 包**：`imhex` ｜ **官方文档**：<https://www.kali.org/tools/imhex/>

## 1. 安装

```bash
sudo apt update
sudo apt install imhex
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.38.1 |
| 架构 | amd64 |
| 可执行命令 | `imhex`、`imhex-updater` |
| 依赖 | `libbz2-1.0`、`libc6`、`libcurl4t64`、`libdbus-1-3`、`libfmt10`、`libfreetype6`、`libgcc-s1`、`libglfw3`、`liblzma5`、`libmagic1t64`、`libmbedcrypto16`、`libssh2-1t64` 等 |
| 安装体积 | 90.15 MB |
| 官网 | <https://github.com/WerWolv/ImHex> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/imhex> |
| 包追踪 | <https://pkg.kali.org/pkg/imhex> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
imhex -h          # 查看用法
man imhex         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `imhex`

官方给出的调用示例：`imhex -h`

```text
root@kali:~# imhex -h
```

### `imhex-updater`

官方给出的调用示例：`imhex-updater -h`

```text
root@kali:~# imhex-updater -h
ImHex Updater - You should probably not run this on its own
Usage: updater <version-type>
  version-type: The type of version to update to. Can be either 'stable' or 'nightly'.
Updated on: 2026-Mar-02
 Edit this page
iaxflood
impacket
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install imhex`，再执行 `imhex --version` 2>/dev/null || `imhex -V`
- [ ] **2.** **读官方帮助** —— `imhex -h`，需要细节时 `man imhex`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: updater <version-type>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/imhex/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/imhex/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/imhex/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
