# magicrescue

> Recover files by looking for magic bytes Magic Rescue scans a block device for file types it knows how to recover and calls an external program to extract them. It looks at “magic bytes” (file patterns) in file contents, so it can be used …

> **功能分类**：数字取证 ｜ **Kali 包**：`magicrescue` ｜ **官方文档**：<https://www.kali.org/tools/magicrescue/>

## 1. 安装

```bash
sudo apt update
sudo apt install magicrescue
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1.10 |
| 架构 | any |
| 可执行命令 | `magicrescue`、`dupemap`、`magicsort` |
| 依赖 | `dcraw`、`flac`、`libc6`、`libgdbm-compat4t64`、`libjpeg-turbo-progs`、`mpg123`、`sqlite3`、`unzip`、`zip`、`dupemap` |
| 安装体积 | 257 KB |
| 官网 | <https://github.com/jbj/magicrescue> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/magicrescue> |
| 包追踪 | <https://pkg.kali.org/pkg/magicrescue> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
magicrescue -h          # 查看用法
man magicrescue         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dupemap`

> 官方示例调用：`dupemap -h`

```text
root@kali:~# dupemap -h
Usage: dupemap [OPTIONS] OPERATION PATH...
Where OPERATION is one of the operations listed in the manpage.
Options:
  -d DATABASE   Read/write from a database on disk
  -I FILE       Read input file names from this file ("-" for stdin)
  -m MINSIZE    Exclude files below this size
  -M MAXSIZE    Exclude files above this size
```

### `magicrescue`

> 官方示例调用：`magicrescue -h`

```text
root@kali:~# magicrescue -h
Usage: magicrescue [-I FILE] [-M MODE] [-O [+-=][0x]OFFSET] [-b BLOCKSIZE]
	-d OUTPUT_DIR -r RECIPE1 [-r RECIPE2 [...]] DEVICE1 [DEVICE2 [...]]
  -b  Only consider files starting at a multiple of BLOCKSIZE.
  -d  Mandatory.  Output directory for found files.
  -r  Mandatory.  Recipe name, file or directory.
  -I  Read input file names from this file ("-" for stdin)
  -M  Produce machine-readable output to stdout.
  -O  Resume from specified offset (hex or decimal) in the first device.
```

### `magicsort`

> 官方示例调用：`magicsort -h`

```text
root@kali:~# magicsort -h
Usage: magicsort DIRECTORY
Will invoke your system's file(1) utility to categorize all the files found
by magicrescue.
Updated on: 2026-Mar-02
 Edit this page
mac-robber
maltego-teeth
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install magicrescue`，再执行 `magicrescue --version` 2>/dev/null || `magicrescue -V`
- [ ] **2.** **读官方帮助** —— `magicrescue -h`，需要细节时 `man magicrescue`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: dupemap [OPTIONS] OPERATION PATH...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/magicrescue/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/magicrescue/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/magicrescue/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
