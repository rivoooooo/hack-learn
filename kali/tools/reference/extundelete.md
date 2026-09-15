# extundelete

> Utility to recover deleted files from ext3/ext4 partition extundelete uses the information stored in the partition’s journal to attempt to recover a file that has been deleted. There is no guarantee that any particular file will be able to…

> **功能分类**：数字取证 ｜ **Kali 包**：`extundelete` ｜ **官方文档**：<https://www.kali.org/tools/extundelete/>

## 1. 安装

```bash
sudo apt update
sudo apt install extundelete
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.2.4 |
| 架构 | any |
| 可执行命令 | `extundelete` |
| 依赖 | `libc6`、`libcom-err2`、`libext2fs2t64`、`libgcc-s1`、`libstdc++6` |
| 安装体积 | 152 KB |
| 官网 | <http://extundelete.sourceforge.net/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/extundelete> |
| 包追踪 | <https://pkg.kali.org/pkg/extundelete> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Read the partition (/dev/sda1) and restore (–restore-file) the given file name (root/importantfile):
root@kali:~# extundelete /dev/sda1 --restore-file root/importantfile
WARNING: Extended attributes are not restored.
WARNING: EXT3_FEATURE_INCOMPAT_RECOVER is set.
The partition should be unmounted to undelete any files without further data loss.
If the partition is not currently mounted, this message indicates
it was improperly unmounted, and you should run fsck before continuing.
If you decide to continue, extundelete may overwrite some of the deleted
files and make recovering those files impossible.  You should unmount the
file system and check it with fsck before using extundelete.
Would you like to continue? (y/n)
y
Loading filesystem metadata ... 192 groups loaded.
Loading journal descriptors ... 29495 descriptors loaded.
Writing output to directory RECOVERED_FILES/
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `extundelete`

> 官方示例调用：`extundelete /dev/sda1 --restore-file root/importantfile`

```text
root@kali:~# extundelete /dev/sda1 --restore-file root/importantfile
WARNING: Extended attributes are not restored.
WARNING: EXT3_FEATURE_INCOMPAT_RECOVER is set.
The partition should be unmounted to undelete any files without further data loss.
If the partition is not currently mounted, this message indicates
it was improperly unmounted, and you should run fsck before continuing.
If you decide to continue, extundelete may overwrite some of the deleted
files and make recovering those files impossible.  You should unmount the
file system and check it with fsck before using extundelete.
Would you like to continue? (y/n)
y
Loading filesystem metadata ... 192 groups loaded.
Loading journal descriptors ... 29495 descriptors loaded.
Writing output to directory RECOVERED_FILES/
```

### `extundelete --help`

> 官方示例调用：`extundelete --help`

```text
root@kali:~# extundelete --help
Usage: extundelete [options] [--] device-file
Options:
  --version, -[vV]       Print version and exit successfully.
  --help,                Print this help and exit successfully.
  --superblock           Print contents of superblock in addition to the rest.
                         If no action is specified then this option is implied.
  --journal              Show content of journal.
  --after dtime          Only process entries deleted on or after 'dtime'.
  --before dtime         Only process entries deleted before 'dtime'.
Actions:
  --inode ino            Show info on inode 'ino'.
  --block blk            Show info on block 'blk'.
  --restore-inode ino[,ino,...]
                         Restore the file(s) with known inode number 'ino'.
                         The restored files are created in ./RECOVERED_FILES
                         with their inode number as extension (ie, file.12345).
  --restore-file 'path'  Will restore file 'path'. 'path' is relative to root
                         of the partition and does not start with a '/'
                         The restored file is created in the current
                         directory as 'RECOVERED_FILES/path'.
  --restore-files 'path' Will restore files which are listed in the file 'path'.
                         Each filename should be in the same format as an option
                         to --restore-file, and there should be one per line.
  --restore-directory 'path'
                         Will restore directory 'path'. 'path' is relative to the
                         root directory of the file system.  The restored
                         directory is created in the output directory as 'path'.
  --restore-all          Attempts to restore everything.
  -j journal             Reads an external journal from the named file.
  -b blocknumber         Uses the backup superblock at blocknumber when opening
                         the file system.
  -B blocksize           Uses blocksize as the block size when opening the file
                         system.  The number should be the number of bytes.
  --log 0                Make the program silent.
  --log filename         Logs all messages to filename.
--log D1=0,D2=filename   Custom control of log messages with comma-separated
   Examples below:       list of options.  Dn must be one of info, warn, or
   --log info,error      error.  Omission of the '=name' results in messages
   --log warn=0          with the specified level to be logged to the console.
   --log error=filename  If the parameter is '=0', logging for the specified
                         level will be turned off.  If the parameter is
                         '=filename', messages with that level will be written
                         to filename.
   -o directory          Save the recovered files to the named directory.
                         The restored files are created in a directory
                         named 'RECOVERED_FILES/' by default.
Updated on: 2025-Dec-09
 Edit this page
ext4magic
eyewitness
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install extundelete`，再执行 `extundelete --version` 2>/dev/null || `extundelete -V`
- [ ] **2.** **读官方帮助** —— `extundelete -h`，需要细节时 `man extundelete`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: extundelete [options] [--] device-file`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/extundelete/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/extundelete/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/extundelete/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
