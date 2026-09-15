# recoverjpeg

> Recover JFIF (JPEG) pictures and MOV movies recoverjpeg tries to recover JFIF (JPEG) pictures and MOV movies from a peripheral. This may be useful if you mistakenly overwrite a partition or if a device such as a digital camera memory card …

> **功能分类**：数字取证 ｜ **Kali 包**：`recoverjpeg` ｜ **官方文档**：<https://www.kali.org/tools/recoverjpeg/>

## 1. 安装

```bash
sudo apt update
sudo apt install recoverjpeg
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.6.3 |
| 架构 | any |
| 可执行命令 | `recoverjpeg`、`recovermov`、`remove-duplicates`、`sort-pictures` |
| 依赖 | `exif`、`imagemagick`、`libc6`、`libgcc-s1`、`libstdc++6`、`python3` |
| 安装体积 | 65 KB |
| 官网 | <https://www.rfc1149.net/devel/recoverjpeg> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/recoverjpeg> |
| 包追踪 | <https://pkg.kali.org/pkg/recoverjpeg> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
recoverjpeg -h          # 查看用法
man recoverjpeg         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `recoverjpeg`

官方给出的调用示例：`recoverjpeg -h`

```text
root@kali:~# recoverjpeg -h
Usage: recoverjpeg [options] file|device
Options:
   -b blocksize   Block size in bytes (default: 512)
   -d format      Directory format string in printf syntax
   -f format      File format string in printf syntax
   -h             This help message
   -i index       Initial picture index
   -m maxsize     Max jpeg file size in bytes (default: 6m)
   -o directory   Restore jpeg files into this directory
   -q             Be quiet
   -r readsize    Size of disk reads in bytes (default: 128m)
   -s cutoff      Minimal file size in bytes to restore
   -S skipsize    Size to skip at the beginning
   -v             Be verbose
   -V             Display version and exit
```

### `recovermov`

官方给出的调用示例：`recovermov -h`

```text
root@kali:~# recovermov -h
Usage: recovermov [options] file|device
Options:
   -b blocksize   Block size in bytes
                  (default: 512)
   -n base_name   Basename of the mov files to create
                  (default: "video_")
   -h             This help message
   -i index       Initial movie index
   -o directory   Restore mov files into this directory
   -V             Display version and exit
```

### `man`

官方给出的调用示例：`man remove-duplicates`

```text
root@kali:~# man remove-duplicates
REMOVE-DUPLICATES(1)                                       REMOVE-DUPLICATES(1)
NAME
     remove-duplicates  - remove duplicates of the same file in the current di-
     rectory
SYNOPSIS
     remove-duplicate [-f]
DESCRIPTION
     Removes duplicates of the same file in the  current  directory  if  -f  is
     given.   If  -f  is not given, duplicate will be identified twice (once in
     every direction).
OPTIONS
     -f
COPYRIGHT
     Copyright (c) 2004-2016 Samuel  Tardieu
[email protected]
.   This  is  free
     software;  see  the  source for copying conditions.  There is NO warranty;
     not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     If recoverjpeg saves your day and you liked it, you are welcome to send me
     the best rescued ones by email (please send only 800x600 versions  of  the
     pictures)  and authorize me to put them online (indicate which contact in-
     formation you want me to use for credits).
SEE ALSO
     recoverjpeg(1) sort-pictures(1)
AUTHORS
     Samuel Tardieu
[email protected]
User Manuals                   November 12, 2016           REMOVE-DUPLICATES(1)
```

### `man（示例）`

官方给出的调用示例：`man sort-pictures`

```text
root@kali:~# man sort-pictures
SORT-PICTURES(1)                                               SORT-PICTURES(1)
NAME
     sort-pictures - sort pictures according to exif date
SYNOPSIS
     sort-pictures
DESCRIPTION
     Sort-pictures uses the exif tags in jpeg pictures recovered by recoverjpeg
     in directories.  It creates hard links to organize sorted pictures.
     Running  sort-pictures will scan the current directory for files named af-
     ter the template image?????*.jpg (image followed by at least five  charac-
     ters  followed  by .jpg).  A new hardlink will be created for each file in
     one of the following directories:
     * invalid The picture is an invalid JFIF file.
     * small The picture size is less than 100,000 bytes.
     * undated Sort-pictures was unable to determine the date  of  the  picture
       from the exif tags.
     * YYYY-MM-DD  A  directory  representing the date at which the picture was
       taken.
SEE ALSO
     recoverjpeg(1) remove-duplicates(1)
COPYRIGHT
     Copyright (c) 2004-2016 Samuel  Tardieu
[email protected]
.   This  is  free
     software;  see  the  source for copying conditions.  There is NO warranty;
     not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
AUTHORS
     Samuel Tardieu
[email protected]
User Manuals                   November 12, 2016               SORT-PICTURES(1)
Updated on: 2026-May-25
 Edit this page
rake
reglookup
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install recoverjpeg`，再执行 `recoverjpeg --version` 2>/dev/null || `recoverjpeg -V`
- [ ] **2.** **读官方帮助** —— `recoverjpeg -h`，需要细节时 `man recoverjpeg`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: recoverjpeg [options] file|device`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/recoverjpeg/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/recoverjpeg/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/recoverjpeg/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
