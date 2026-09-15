# fatcat

> FAT filesystem explore, extract, repair, and forensic tool fatcat is a tool to explore, extract, repair and forensic FAT filesystem. Its features: - Get information about FAT filesystem; - Explore FAT file system; - Read file or extract di…

> **功能分类**：通用工具 ｜ **Kali 包**：`fatcat` ｜ **官方文档**：<https://www.kali.org/tools/fatcat/>

## 1. 安装

```bash
sudo apt update
sudo apt install fatcat
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1.1 |
| 架构 | any |
| 可执行命令 | `fatcat` |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6` |
| 安装体积 | 141 KB |
| 官网 | <https://github.com/Gregwar/fatcat> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/fatcat> |
| 包追踪 | <https://pkg.kali.org/pkg/fatcat> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
fatcat -h          # 查看用法
man fatcat         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `fatcat`

> 官方示例调用：`fatcat -h`

```text
root@kali:~# fatcat -h
fatcat v1.1.0, Gregwar <
[email protected]
>
Usage: fatcat disk.img [options]
  -i: display information about disk
  -O [offset]: global offset (may be partition place)
  -F [format]: output format (default, json)
Browsing & extracting:
  -l [dir]: list files and directories in the given path
  -L [cluster]: list files and directories in the given cluster
  -r [path]: reads the file given by the path
  -R [cluster]: reads the data from given cluster
  -s [size]: specify the size of data to read from the cluster
  -d: enable listing of deleted files
  -x [directory]: extract all files to a directory, deleted files included if -d
                  will start with rootDirectory, unless -c is provided
* -S: write scamble data in unallocated sectors
* -z: write scamble data in unallocated sectors
FAT Hacking
  -@ [cluster]: Get the cluster address and information
  -2: analysis & compare the 2 FATs
  -b [file]: backup the FATs (see -t)
* -p [file]: restore (patch) the FATs (see -t)
* -w [cluster] -v [value]: write next cluster (see -t)
  -t [table]: specify which table to write (0:both, 1:first, 2:second)
* -m: merge the FATs
  -o: search for orphan files and directories
* -f: try to fix reachable directories
Entries hacking
  -e [path]: sets the entry to hack, combined with:
* -c [cluster]: sets the entry cluster
* -s [size]: sets the entry size
* -a [attributes]: sets the entry attributes
  -k [cluster]: try to find an entry that point to that cluster
*: These flags writes on the disk, and may damage it, be careful
Updated on: 2025-Dec-09
 Edit this page
faraday-agent-dispatcher
fcrackzip
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install fatcat`，再执行 `fatcat --version` 2>/dev/null || `fatcat -V`
- [ ] **2.** **读官方帮助** —— `fatcat -h`，需要细节时 `man fatcat`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: fatcat disk.img [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/fatcat/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/fatcat/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/fatcat/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
