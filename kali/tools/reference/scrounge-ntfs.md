# scrounge-ntfs

> Data recovery program for NTFS filesystems Scrounge NTFS is a data recovery program for NTFS filesystems. It reads each block of the hard disk and try to rebuild the original filesystem tree into a directory. This package is useful in fore…

> **功能分类**：数字取证 ｜ **Kali 包**：`scrounge-ntfs` ｜ **官方文档**：<https://www.kali.org/tools/scrounge-ntfs/>

## 1. 安装

```bash
sudo apt update
sudo apt install scrounge-ntfs
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.9 |
| 架构 | any |
| 可执行命令 | `scrounge-ntfs` |
| 依赖 | `libc6` |
| 安装体积 | 49 KB |
| 官网 | <http://thewalter.net/stef/software/scrounge/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/scrounge-ntfs> |
| 包追踪 | <https://pkg.kali.org/pkg/scrounge-ntfs> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
scrounge-ntfs -h          # 查看用法
man scrounge-ntfs         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `scrounge-ntfs`

> 官方示例调用：`scrounge-ntfs --help`

```text
root@kali:~# scrounge-ntfs --help
scrounge-ntfs: invalid option -- '-'
usage: scrounge-ntfs -l disk
  List all drive partition information.
usage: scrounge-ntfs -s disk
  Search drive for NTFS partitions.
usage: scrounge-ntfs [-m mftoffset] [-c clustersize] [-o outdir] disk start end
  Scrounge data from a partition
  -m         Offset to mft (in sectors)
  -c         Cluster size (in sectors, default of 8)
  -o         Directory to put scrounged files in
  disk       The raw disk partitios (ie: /dev/hda)
  start      First sector of partition
  end        Last sector of partition
Updated on: 2025-Dec-09
 Edit this page
scalpel
sctpscan
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install scrounge-ntfs`，再执行 `scrounge-ntfs --version` 2>/dev/null || `scrounge-ntfs -V`
- [ ] **2.** **读官方帮助** —— `scrounge-ntfs -h`，需要细节时 `man scrounge-ntfs`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `scrounge-ntfs -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/scrounge-ntfs/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/scrounge-ntfs/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/scrounge-ntfs/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
