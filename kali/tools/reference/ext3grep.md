# ext3grep

> Tool to help recover deleted files on ext3 filesystems ext3grep is a simple tool intended to aid anyone who accidentally deletes a file on an ext3 filesystem, only to find that they wanted it shortly thereafter. This package is useful in f…

> **功能分类**：数字取证 ｜ **Kali 包**：`ext3grep` ｜ **官方文档**：<https://www.kali.org/tools/ext3grep/>

## 1. 安装

```bash
sudo apt update
sudo apt install ext3grep
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.10.2 |
| 架构 | alpha |
| 可执行命令 | `ext3grep` |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6` |
| 安装体积 | 299 KB |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/ext3grep> |
| 包追踪 | <https://pkg.kali.org/pkg/ext3grep> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ext3grep -h          # 查看用法
man ext3grep         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ext3grep`

> 官方示例调用：`ext3grep --help`

```text
root@kali:~# ext3grep --help
Running ext3grep version 0.10.2
Usage: ext3grep [options] [--] device-file
Options:
  --version, -[vV]       Print version and exit successfully.
  --help,                Print this help and exit successfully.
  --superblock           Print contents of superblock in addition to the rest.
                         If no action is specified then this option is implied.
  --print                Print content of block or inode, if any.
  --ls                   Print directories with only one line per entry.
                         This option is often needed to turn on filtering.
  --accept filen         Accept 'filen' as a legal filename. Can be used multi-
                         ple times. If you change any --accept you must remove
                         BOTH stage* files!
  --accept-all           Simply accept everything as filename.
  --journal              Show content of journal.
  --show-path-inodes     Show the inode of each directory component in paths.
Filters:
  --group grp            Only process group 'grp'.
  --directory            Only process directory inodes.
  --after dtime          Only entries deleted on or after 'dtime'.
  --before dtime         Only entries deleted before 'dtime'.
  --deleted              Only show/process deleted entries.
  --allocated            Only show/process allocated inodes/blocks.
  --unallocated          Only show/process unallocated inodes/blocks.
  --reallocated          Do not suppress entries with reallocated inodes.
                         Inodes are considered 'reallocated' if the entry
                         is deleted but the inode is allocated, but also when
                         the file type in the dir entry and the inode are
                         different.
  --zeroed-inodes        Do not suppress entries with zeroed inodes. Linked
                         entries are always shown, regardless of this option.
  --depth depth          Process directories recursively up till a depth
                         of 'depth'.
Actions:
  --inode-to-block ino   Print the block that contains inode 'ino'.
  --inode ino            Show info on inode 'ino'.
                         If --ls is used and the inode is a directory, then
                         the filters apply to the entries of the directory.
                         If you do not use --ls then --print is implied.
  --block blk            Show info on block 'blk'.
                         If --ls is used and the block is the first block
                         of a directory, then the filters apply to entries
                         of the directory.
                         If you do not use --ls then --print is implied.
  --histogram=[atime|ctime|mtime|dtime|group]
                         Generate a histogram based on the given specs.
                         Using atime, ctime or mtime will change the
                         meaning of --after and --before to those times.
  --journal-block jblk   Show info on journal block 'jblk'.
  --journal-transaction seq
                         Show info on transaction with sequence number 'seq'.
  --dump-names           Write the path of files to stdout.
                         This implies --ls but suppresses it's output.
  --search-start str     Find blocks that start with the fixed string 'str'.
  --search str           Find blocks that contain the fixed string 'str'.
  --search-inode blk     Find inodes that refer to block 'blk'.
  --search-zeroed-inodes Return allocated inode table entries that are zeroed.
  --inode-dirblock-table dir
                         Print a table for directory path 'dir' of directory
                         block numbers found and the inodes used for each file.
  --show-journal-inodes ino
                         Show copies of inode 'ino' still in the journal.
  --restore-inode ino[@seqnr][,ino[@seqnr],...]
                         Restore the file(s) with known inode number 'ino'.
                         The restored files are created in ./RESTORED_FILES/
                         with their inode number as extension (ie, inode.12345).
                         If '@seqnr' is provided then (only) the journal entry
                         with that sequence number is used, otherwise the latest
                         entry is used (if any). You can use that in the case a
                         a file was overwritten or truncated, rather than deleted.
  --restore-file 'path' [--restore-file 'path' ...]
                         Will restore file 'path'. 'path' is relative to the
                         root of the partition and does not start with a '/' (it
                         must be one of the paths returned by --dump-names).
                         The restored directory, file or symbolic link is
                         created in the current directory as 'RESTORED_FILES/path'.
  --restore-all          As --restore-file but attempts to restore everything.
                         The use of --after is highly recommended because the
                         attempt to restore very old files will only result in
                         them being hard linked to a more recently deleted file
                         and as such pollute the output.
  --show-hardlinks       Show all inodes that are shared by two or more files.
Updated on: 2025-Dec-09
 Edit this page
exploitdb-papers
ext4magic
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ext3grep`，再执行 `ext3grep --version` 2>/dev/null || `ext3grep -V`
- [ ] **2.** **读官方帮助** —— `ext3grep -h`，需要细节时 `man ext3grep`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ext3grep [options] [--] device-file`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ext3grep/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ext3grep/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ext3grep/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
