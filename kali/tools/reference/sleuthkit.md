# sleuthkit

> Tools for forensics analysis on volume and filesystem data The Sleuth Kit, also known as TSK, is a collection of UNIX-based command line file and volume system forensic analysis tools. The filesystem tools allow you to examine filesystems …

> **功能分类**：数字取证 ｜ **Kali 包**：`sleuthkit` ｜ **官方文档**：<https://www.kali.org/tools/sleuthkit/>

## 1. 安装

```bash
sudo apt update
sudo apt install sleuthkit
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.14.0 |
| 架构 | any |
| 可执行命令 | `libsleuthkit-java`、`libsleuthkit-jni`、`libtsk-dev`、`libtsk23`、`sleuthkit`、`blkcalc`、`blkcat`、`blkls`、`blkstat`、`fcat`、`ffind`、`fiwalk`、`fls`、`fsstat`、`hfind`、`icat`、`ifind`、`ils`、`img_cat`、`img_stat`、`istat`、`jcat`、`jls`、`jpeg_extract`、`mactime`、`mmcat`、`mmls`、`mmstat`、`pstat`、`sigfind`、`sorter`、`srch_strings`、`tsk_comparedir`、`tsk_gettimes`、`tsk_imageinfo`、`tsk_loaddb`、`tsk_recover`、`usnjls` |
| 依赖 | `file`、`libafflib0t64`、`libbfio1`、`libc6`、`libdate-manip-perl`、`libewf2`、`libgcc-s1`、`libstdc++6`、`libtsk23`、`libvhdi1`、`libvmdk1`、`libvslvm1t64` 等 |
| 安装体积 | 1.09 MB |
| 官网 | <https://www.sleuthkit.org/sleuthkit> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sleuthkit> |
| 包追踪 | <https://pkg.kali.org/pkg/sleuthkit> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libsleuthkit-java -h          # 查看用法
man libsleuthkit-java         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 38 个可执行命令，下面是官方页面内嵌的帮助原文。

### `blkcalc`

官方给出的调用示例：`blkcalc --help`

```text
root@kali:~# blkcalc --help
blkcalc: invalid option -- '-'
Invalid argument: --help
usage: blkcalc [-dsu unit_addr] [-vV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] image [images]
Slowly calculates the opposite block number
	One of the following must be given:
	  -d: The given address is from a 'dd' image
	  -s: The given address is from a 'blkls -s' (slack) image
	  -u: The given address is from a 'blkls' (unallocated) image
	-f fstype: The file system type (use '-f list' for supported types)
	-i imgtype: The format of the image file (use '-i list' for supported types)
	-b dev_sector_size: The size (in bytes) of the device sectors
	-o imgoffset: The offset of the file system in the image (in sectors)
	-P pooltype: Pool container type (use '-P list' for supported types)
	-B pool_volume_block: Starting block (for pool volumes only)
	-v: verbose output to stderr
	-V: Print version
```

### `blkcat`

官方给出的调用示例：`blkcat --help`

```text
root@kali:~# blkcat --help
blkcat: invalid option -- '-'
Invalid argument: --help
usage: blkcat [-ahsvVw] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] [-k password] [-u usize] image [images] unit_addr [num]
	-a: displays in all ASCII
	-h: displays in hexdump-like fashion
	-i imgtype: The format of the image file (use '-i list' for supported types)
	-b dev_sector_size: The size (in bytes) of the device sectors
	-o imgoffset: The offset of the file system in the image (in sectors)
	-P pooltype: Pool container type (use '-p list' for supported types)
	-B pool_volume_block: Starting block (for pool volumes only)
	-f fstype: File system type (use '-f list' for supported types)
	-k password: Decryption password for encrypted volumes
	-s: display basic block stats such as unit size, fragments, etc.
	-v: verbose output to stderr
	-V: display version
	-w: displays in web-like (html) fashion
	-u usize: size of each data unit in image (for raw, blkls, swap)
	[num] is the number of data units to display (default is 1)
```

### `blkls`

官方给出的调用示例：`blkls --help`

```text
root@kali:~# blkls --help
blkls: invalid option -- '-'
Invalid argument: --help
usage: blkls [-aAelvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] image [images] [start-stop]
	-e: every block (including file system metadata blocks)
	-l: print details in time machine list format
	-a: Display allocated blocks
	-A: Display unallocated blocks
	-f fstype: File system type (use '-f list' for supported types)
	-i imgtype: The format of the image file (use '-i list' for supported types)
	-b dev_sector_size: The size (in bytes) of the device sectors
	-o imgoffset: The offset of the file system in the image (in sectors)
	-P pooltype: Pool container type (use '-P list' for supported types)
	-B pool_volume_block: Starting block (for pool volumes only)
	-s: print slack space only (other flags are ignored
	-v: verbose to stderr
	-V: print version
```

### `blkstat`

官方给出的调用示例：`blkstat --help`

```text
root@kali:~# blkstat --help
blkstat: invalid option -- '-'
Invalid argument: --help
usage: blkstat [-vV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] image [images] addr
	-f fstype: File system type (use '-f list' for supported types)
	-k password: Decryption password for encrypted volumes
	-i imgtype: The format of the image file (use '-i list' for supported types)
	-b dev_sector_size: The size (in bytes) of the device sectors
	-o imgoffset: The offset of the file system in the image (in sectors)
	-P pooltype: Pool container type (use '-P list' for supported types)
	-B pool_volume_block: Starting block (for pool volumes only)
	-v: Verbose output to stderr
	-V: Print version
```

### `fcat`

官方给出的调用示例：`fcat --help`

```text
root@kali:~# fcat --help
fcat: invalid option -- '-'
Invalid argument: --help
usage: fcat [-hRsvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] file_path image [images]
	-h: Do not display holes in sparse files
	-R: Suppress recovery errors
	-s: Display slack space at end of file
	-i imgtype: The format of the image file (use '-i list' for supported types)
	-b dev_sector_size: The size (in bytes) of the device sectors
	-f fstype: File system type (use '-f list' for supported types)
	-o imgoffset: The offset of the file system in the image (in sectors)
	-P pooltype: Pool container type (use '-p list' for supported types)
	-B pool_volume_block: Starting block (for pool volumes only)
	-v: verbose to stderr
	-V: Print version
```

### `ffind`

官方给出的调用示例：`ffind --help`

```text
root@kali:~# ffind --help
ffind: invalid option -- '-'
Invalid argument: --help
usage: ffind [-aduvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] image [images] inode
	-a: Find all occurrences
	-d: Find deleted entries ONLY
	-u: Find undeleted entries ONLY
	-f fstype: Image file system type (use '-f list' for supported types)
	-i imgtype: The format of the image file (use '-i list' for supported types)
	-b dev_sector_size: The size (in bytes) of the device sectors
	-o imgoffset: The offset of the file system in the image (in sectors)
	-P pooltype: Pool container type (use '-p list' for supported types)
	-B pool_volume_block: Starting block (for pool volumes only)
	-v: Verbose output to stderr
	-V: Print version
```

### `fiwalk`

官方给出的调用示例：`fiwalk -h`

```text
root@kali:~# fiwalk -h
usage: fiwalk [options] iso-name
Default behavior: Just print the file system statistics and exit.
options:
    -c config.txt   read config.txt for metadata extraction tools
    -C nn           only process nn files, then do a clean exit
include/exclude parameters; may be repeated.
    -n pattern  = only match files for which the filename matches
                  the pattern.
              example: -n .jpeg -n .jpg will find all JPEG files
              Case is ignored. Will not match orphan files.
Ways to make this program run faster:
    -I ignore NTFS system files
    -g just report the file objects - don't get the data
    -O only walk allocated files
    -b do not report byte runs if data not accessed
    -z do not calculate MD5 or SHA1 values
    -Gnn - Only process the contents of files smaller than nn gigabytes (default 2)
           (Specify -G0 to remove space restrictions)
Ways to make this program run slower:
    -M = Report MD5 for each file (default on)
    -1 = Report SHA1 for each file (default on)
    -S nnnn = Perform sector hashes every nnnn bytes
    -f = Report the output of the 'file' command for each
Output options:
    -m = Output in SleuthKit 'Body file' format
    -A<file> = ARFF output to <file>
    -X<file> = XML output to a <file> (full DTD)
         -X0 = Write output to filename.xml
    -Z       = zap (erase) the output file
    -x       = XML output to stdout (no DTD)
    -T<file> = Walkfile output to <file>
    -a <audit.txt> = Read the scalpel audit.txt file
Misc:
    -d = debug this program
    -v = Enable SleuthKit verbose flag
SleuthKit Version: 4.14.0
AFFLIB Version:    3.7.22
LIBEWF Version:    20140816
```

### `fls`

官方给出的调用示例：`fls --help`

```text
root@kali:~# fls --help
fls: invalid option -- '-'
Invalid argument: --help
usage: fls [-adDFlhpruvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-m dir/] [-o imgoffset] [-z ZONE] [-s seconds] image [images] [inode]
	If [inode] is not given, the root directory is used
	-a: Display "." and ".." entries
	-d: Display deleted entries only
	-D: Display only directories
	-F: Display only files
	-l: Display long version (like ls -l)
	-i imgtype: Format of image file (use '-i list' for supported types)
	-b dev_sector_size: The size (in bytes) of the device sectors
	-f fstype: File system type (use '-f list' for supported types)
	-m: Display output in mactime input format with
	      dir/ as the actual mount point of the image
	-h: Include MD5 checksum hash in mactime output
	-o imgoffset: Offset into image file (in sectors)
	-P pooltype: Pool container type (use '-P list' for supported types)
	-B pool_volume_block: Starting block (for pool volumes only)
	-S snap_id: Snapshot ID (for APFS only)
	-p: Display full path for each file
	-r: Recurse on directory entries
	-u: Display undeleted entries only
	-v: verbose output to stderr
	-V: Print version
	-z: Time zone of original machine (i.e. EST5EDT or GMT) (only useful with -l)
	-s seconds: Time skew of original machine (in seconds) (only useful with -l & -m)
	-k password: Decryption password for encrypted volumes
```

### `fsstat`

官方给出的调用示例：`fsstat --help`

```text
root@kali:~# fsstat --help
fsstat: invalid option -- '-'
Invalid argument: --help
usage: fsstat [-tvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] image
	-t: display type only
	-i imgtype: The format of the image file (use '-i list' for supported types)
	-b dev_sector_size: The size (in bytes) of the device sectors
	-f fstype: File system type (use '-f list' for supported types)
	-o imgoffset: The offset of the file system in the image (in sectors)
	-P pooltype: Pool container type (use '-P list' for supported types)
	-B pool_volume_block: Starting block (for pool volumes only)
	-v: verbose output to stderr
	-V: Print version
	-k password: Decryption password for encrypted volumes
```

### `hfind`

官方给出的调用示例：`hfind -h`

```text
root@kali:~# hfind -h
hfind: invalid option -- 'h'
usage: hfind [-eqVa] [-c] [-f lookup_file] [-i db_type] db_file [hashes]
	-e: Extended mode - where values other than just the name are printed
	-q: Quick mode - where a 1 is printed if it is found, else 0
	-V: Print version to STDOUT
	-c db_name: Create new database with the given name.
	-a: Add given hashes to the database.
	-f lookup_file: File with one hash per line to lookup
	-i db_type: Create index file for a given hash database type
	db_file: The path of the hash database, must have .kdb extension for -c option
	[hashes]: hashes to lookup (STDIN is used otherwise)
	Supported index types: nsrl-md5, nsrl-sha1, md5sum, encase, hk
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install sleuthkit`，再执行 `libsleuthkit-java --version` 2>/dev/null || `libsleuthkit-java -V`
- [ ] **2.** **读官方帮助** —— `libsleuthkit-java -h`，需要细节时 `man libsleuthkit-java`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `libsleuthkit-java -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sleuthkit/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[sleuthkit](../../tools/tutorials/09-数字取证/sleuthkit.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sleuthkit/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sleuthkit/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
