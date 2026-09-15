# testdisk

> Partition scanner and disk recovery tool TestDisk checks the partition and boot sectors of your disks. It is very useful in forensics, recovering lost partitions. It works with : DOS/Windows FAT12, FAT16 and FAT32 NTFS ( Windows NT/2K/XP )

> **功能分类**：通用工具 ｜ **Kali 包**：`testdisk` ｜ **官方文档**：<https://www.kali.org/tools/testdisk/>

## 1. 安装

```bash
sudo apt update
sudo apt install testdisk
```

| 项目 | 内容 |
|------|------|
| 版本 | 7.2 |
| 架构 | any |
| 可执行命令 | `photorec`、`fidentify`、`qphotorec`、`testdisk` |
| 依赖 | `libc6`、`libext2fs2t64`、`libncursesw6`、`libntfs-3g90`、`libtinfo6`、`ntfs-3g` |
| 安装体积 | 528 KB |
| 官网 | <https://www.cgsecurity.org/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/testdisk> |
| 包追踪 | <https://pkg.kali.org/pkg/testdisk> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
photorec -h          # 查看用法
man photorec         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `fidentify`

> 官方示例调用：`fidentify -h`

```text
root@kali:~# fidentify -h
Usage: fidentify [--check] [+file_format] [directory|file]
       fidentify --version
fidentify determines the file type, the 'extension', by using the same database as PhotoRec.
By default, all known file formats are searched unless one is specifically enabled.
```

### `photorec`

> 官方示例调用：`photorec -h`

```text
root@kali:~# photorec -h
PhotoRec 7.2, Data Recovery Utility, February 2024
Christophe GRENIER <
[email protected]
>
https://www.cgsecurity.org
Usage: photorec [/log] [/debug] [/d recup_dir] [file.dd|file.e01|device]
       photorec /version
/log          : create a photorec.log file
/debug        : add debug information
PhotoRec searches for various file formats (JPEG, Office...). It stores files
in the recup_dir directory.
```

### `qphotorec`

> 官方示例调用：`qphotorec -h`

```text
root@kali:~# qphotorec -h
Usage: qphotorec
       qphotorec /version
QPhotoRec searches various file formats (JPEG, Office...), it stores them
in recup_dir directory.
```

### `testdisk`

> 官方示例调用：`testdisk -h`

```text
root@kali:~# testdisk -h
TestDisk 7.2, Data Recovery Utility, February 2024
Christophe GRENIER <
[email protected]
>
https://www.cgsecurity.org
Usage: testdisk [/log] [/debug] [file.dd|file.e01|device]
       testdisk /list  [/log]   [file.dd|file.e01|device]
       testdisk /version
/log          : create a testdisk.log file
/debug        : add debug information
/list         : display current partitions
TestDisk checks and recovers lost partitions
It works with :
- BeFS (BeOS)                           - BSD disklabel (Free/Open/Net BSD)
- CramFS, Compressed File System        - DOS/Windows FAT12, FAT16 and FAT32
- XBox FATX                             - Windows exFAT
- HFS, HFS+, Hierarchical File System   - JFS, IBM's Journaled File System
- Linux btrfs                           - Linux ext2, ext3 and ext4
- Linux GFS2                            - Linux LUKS
- Linux Raid                            - Linux Swap
- LVM, LVM2, Logical Volume Manager     - Netware NSS
- Windows NTFS                          - ReiserFS 3.5, 3.6 and 4
- Sun Solaris i386 disklabel            - UFS and UFS2 (Sun/BSD/...)
- XFS, SGI's Journaled File System      - Wii WBFS
- Sun ZFS
Updated on: 2026-Aug-25
 Edit this page
tcpreplay
testssl.sh
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install testdisk`，再执行 `photorec --version` 2>/dev/null || `photorec -V`
- [ ] **2.** **读官方帮助** —— `photorec -h`，需要细节时 `man photorec`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: fidentify [--check] [+file_format] [directory|file]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/testdisk/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[testdisk](../../tools/tutorials/09-数字取证/testdisk.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/testdisk/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/testdisk/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
