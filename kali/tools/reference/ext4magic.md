# ext4magic

> Recover deleted files from ext3 or ext4 partitions ext4magic is a file carver (or file carving). It can be used when recovering from disasters or in digital forensics activities. The deletion of files in ext3/4 filesystems can not be easil…

> **功能分类**：数字取证 ｜ **Kali 包**：`ext4magic` ｜ **官方文档**：<https://www.kali.org/tools/ext4magic/>

## 1. 安装

```bash
sudo apt update
sudo apt install ext4magic
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.3.2 |
| 架构 | any |
| 可执行命令 | `ext4magic` |
| 依赖 | `libblkid1`、`libbz2-1.0`、`libc6`、`libext2fs2t64`、`libmagic1t64`、`libuuid1`、`zlib1g` |
| 安装体积 | 235 KB |
| 官网 | <http://ext4magic.sf.net/ext4magic_en.html> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/ext4magic> |
| 包追踪 | <https://pkg.kali.org/pkg/ext4magic> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ext4magic -h          # 查看用法
man ext4magic         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ext4magic`

> 官方示例调用：`ext4magic -h`

```text
root@kali:~# ext4magic -h
ext4magic : Error: Missing device name and options.
ext4magic -M [-j <journal_file>] [-d <target_dir>] <filesystem>
ext4magic -m [-j <journal_file>] [-d <target_dir>] <filesystem>
ext4magic [-S|-J|-H|-V|-T] [-x] [-j <journal_file>] [-B n|-I n|-f <file_name>|-i <input_list>] [-t n|[[-a n][-b n]]] [-d <target_dir>] [-R|-r|-L|-l] [-Q] <filesystem>
Updated on: 2025-Dec-09
 Edit this page
ext3grep
extundelete
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ext4magic`，再执行 `ext4magic --version` 2>/dev/null || `ext4magic -V`
- [ ] **2.** **读官方帮助** —— `ext4magic -h`，需要细节时 `man ext4magic`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `ext4magic -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ext4magic/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ext4magic/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ext4magic/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
