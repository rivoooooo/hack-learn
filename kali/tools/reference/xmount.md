# xmount

> Tool for crossmounting between disk image formats xmount allows you to convert on-the-fly between multiple input and output harddisk image formats. xmount creates a virtual file system using FUSE (Filesystem in Userspace) that contains a v…

> **功能分类**：数字取证 ｜ **Kali 包**：`xmount` ｜ **官方文档**：<https://www.kali.org/tools/xmount/>

## 1. 安装

```bash
sudo apt update
sudo apt install xmount
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3.1 |
| 架构 | linux-any |
| 可执行命令 | `xmount` |
| 依赖 | `libafflib0t64`、`libc6`、`libewf2`、`libfuse3-4`、`zlib1g` |
| 安装体积 | 337 KB |
| 官网 | <https://www.sits.lu/xmount> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/xmount> |
| 包追踪 | <https://pkg.kali.org/pkg/xmount> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
xmount -h          # 查看用法
man xmount         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `xmount`

> 官方示例调用：`xmount -h`

```text
root@kali:~# xmount -h
xmount v1.3.1 Copyright (c) 2024 - 2026 by SITS Sarl <
[email protected]
>
Usage:
  xmount [fopts] <xopts> <mntp>
Options:
  fopts:
    -d : Enable FUSE's and xmount's debug mode.
    -h : Display this help message.
    -s : Run single threaded.
    -o no_allow_other : Disable automatic addition of FUSE's allow_other option.
    -o <fopts> : Specify fuse mount options. Will also disable automatic addition of FUSE's allow_other option!
  xopts:
    --cache <cfile> : Enable virtual write support.
      <cfile> specifies the cache file to use.
    --in <itype> <ifile> : Input image format and source file(s). May be specified multiple times.
      <itype> can be "qcow", "qcow2", "qemu", "raw", "dd", "vdi", "aewf", "aaff", "aff", "aff3", "ewf".
      <ifile> specifies the source file. If your image is split into multiple files, you have to specify them all!
    --inopts <iopts> : Specify input library specific options.
      <iopts> specifies a comma separated list of key=value options. See below for details.
    --info : Print out infos about used compiler and libraries.
    --morph <mtype> : Morphing function to apply to input image(s). If not specified, defaults to "combine".
      <mtype> can be "unallocated", "byteswap", "raid0", "combine".
    --morphopts <mopts> : Specify morphing library specific options.
      <mopts> specifies a comma separated list of key=value options. See below for details.
    --offset <off> : Move the output image data start <off> bytes into the input image(s).
    --out <otype> : Output image format. If not specified, defaults to "raw".
      <otype> can be "raw", "dmg", "vdi", "vhd", "vmdk", "vmdks".
    --owcache <file> : Same as --cache <file> but overwrites existing cache file.
    --rocache <file> : Same as --cache <file> but does **not** allow further writes.
    --sizelimit <size> : The data end of input image(s) is set to no more than <size> bytes after the data start.
    --version : Same as --info.
  mntp:
    Mount point where output image should be located.
Infos:
  * One --in option and a mount point are mandatory!
  * If you specify --in multiple times, data from all images is morphed into one output image using the specified morphing function.
  * For VMDK emulation, you have to uncomment "user_allow_other" in /etc/fuse.conf or run xmount as root.
Input / Morphing library specific options:
  Input / Morphing libraries might support an own set of options to configure / tune their behaviour.
  Libraries supporting this feature (if any) and their options are listed below.
  - libxmount_input_vdi.so
    vdilog       : Path for writing log file(must exist).
                   The files created in this directory will be named log_<pid>.
  - libxmount_input_aewf.so
    aewfmaxmem   : Maximum amount of RAM cache, in MiB, for image offset tables. Default: 10 MiB
    aewfmaxfiles : Maximum number of concurrently opened image segment files. Default: 10
    aewfstats    : Output statistics at regular intervals to this directory (must exist).
                   The files created in this directory will be named stats_<pid>.
    aewfrefresh  : The update interval, in seconds, for the statistics (aewfstats must be set). Default: 10s.
    aewflog      : Path for writing log file (must exist).
                   The files created in this directory will be named log_<pid>.
    aewfthreads  : Max. number of threads for parallelized decompression. Default: System CPUs (6)
                   A value of 1 switches back to old, single-threaded legacy functions.
  - libxmount_input_aaff.so
    aaffmaxmem   : Maximum amount of RAM cache, in MiB, for image seek offsets. Default: 10 MiB
    aafflog      : Log file name.
    Specify full path for aafflog. The given file name is extended by _<pid>.
    The AFF format has been declared as deprecated by its inventor!
  - libxmount_morphing_unallocated.so
    unallocated_fs : Specify the filesystem to extract unallocated blocks from. Supported filesystems are: 'hfs', 'fat'. Default: autodetect.
  - libxmount_morphing_raid.so
    raid_chunksize : Specify the chunk size to use in bytes. Defaults to 524288 (512k).
Updated on: 2026-Aug-25
 Edit this page
wsgidav
xplico
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install xmount`，再执行 `xmount --version` 2>/dev/null || `xmount -V`
- [ ] **2.** **读官方帮助** —— `xmount -h`，需要细节时 `man xmount`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/xmount/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/xmount/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/xmount/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
