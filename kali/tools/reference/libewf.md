# libewf

> Collection of tools for reading and writing EWF files Libewf is a library with support for reading and writing the Expert Witness Compression Format (EWF). This library allows you to read media information of EWF files in the SMART (EWF-S0…

> **功能分类**：数字取证 ｜ **Kali 包**：`libewf` ｜ **官方文档**：<https://www.kali.org/tools/libewf/>

## 1. 安装

```bash
sudo apt update
sudo apt install ewf-tools
```

| 项目 | 内容 |
|------|------|
| 版本 | 20140816 |
| 架构 | any |
| 可执行命令 | `ewf-tools`、`ewfacquire`、`ewfacquirestream`、`ewfdebug`、`ewfexport`、`ewfinfo`、`ewfmount`、`ewfrecover`、`ewfverify`、`libewf-dev`、`libewf2`、`python3-libewf` |
| 依赖 | `libc6`、`libewf2`、`libfuse3-4`、`libssl3t64`、`ewfacquire` |
| 安装体积 | 6.64 MB |
| 官网 | <https://github.com/libyal/libewf-legacy> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/libewf> |
| 包追踪 | <https://pkg.kali.org/pkg/libewf> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ewf-tools -h          # 查看用法
man ewf-tools         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 12 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ewfacquire`

官方给出的调用示例：`ewfacquire -h`

```text
root@kali:~# ewfacquire -h
ewfacquire 20140816
Use ewfacquire to acquire data from a file or device and store it in the EWF
format (Expert Witness Compression Format).
Usage: ewfacquire [ -A codepage ] [ -b number_of_sectors ]
                  [ -B number_of_bytes ] [ -c compression_values ]
                  [ -C case_number ] [ -d digest_type ] [ -D description ]
                  [ -e examiner_name ] [ -E evidence_number ] [ -f format ]
                  [ -g number_of_sectors ] [ -l log_filename ]
                  [ -m media_type ] [ -M media_flags ] [ -N notes ]
                  [ -o offset ] [ -p process_buffer_size ]
                  [ -P bytes_per_sector ] [ -r read_error_retries ]
                  [ -S segment_file_size ] [ -t target ] [ -T toc_file ]
                  [ -2 secondary_target ] [ -hqRsuvVwx ] source
	source: the source file(s) or device
	-A:     codepage of header section, options: ascii (default),
	        windows-874, windows-932, windows-936, windows-949,
	        windows-950, windows-1250, windows-1251, windows-1252,
	        windows-1253, windows-1254, windows-1255, windows-1256,
	        windows-1257 or windows-1258
	-b:     specify the number of sectors to read at once (per chunk),
	        options: 16, 32, 64 (default), 128, 256, 512, 1024, 2048, 4096,
	        8192, 16384 or 32768
	-B:     specify the number of bytes to acquire (default is all bytes)
	-c:     specify the compression values as: level or method:level
	        compression method options: deflate (default)
	        compression level options: none (default), empty-block,
	        fast or best
	-C:     specify the case number (default is case_number).
	-d:     calculate additional digest (hash) types besides md5, options:
	        sha1, sha256
	-D:     specify the description (default is description).
	-e:     specify the examiner name (default is examiner_name).
	-E:     specify the evidence number (default is evidence_number).
	-f:     specify the EWF file format to write to, options: ewf, smart,
	        ftk, encase2, encase3, encase4, encase5, encase6 (default),
	        encase7, encase7-v2, linen5, linen6, linen7, ewfx
	-g      specify the number of sectors to be used as error granularity
	-h:     shows this help
	-l:     logs acquiry errors and the digest (hash) to the log_filename
	-m:     specify the media type, options: fixed (default), removable,
	        optical, memory
	-M:     specify the media flags, options: logical, physical (default)
	-N:     specify the notes (default is notes).
	-o:     specify the offset to start to acquire (default is 0)
	-p:     specify the process buffer size (default is the chunk size)
	-P:     specify the number of bytes per sector (default is 512)
	        (use this to override the automatic bytes per sector detection)
	-q:     quiet shows minimal status information
	-r:     specify the number of retries when a read error occurs (default
	        is 2)
	-R:     resume acquiry at a safe point
	-s:     swap byte pairs of the media data (from AB to BA)
	        (use this for big to little endian conversion and vice versa)
	-S:     specify the segment file size in bytes (default is 1.4 GiB)
	        (minimum is 1.0 MiB, maximum is 7.9 EiB for encase6
	        and encase7 format and 1.9 GiB for other formats)
	-t:     specify the target file (without extension) to write to
	-T:     specify the file containing the table of contents (TOC) of
	        an optical disc. The TOC file must be in the CUE format.
	-u:     unattended mode (disables user interaction)
	-v:     verbose output to stderr
	-V:     print version
	-w:     zero sectors on read error (mimic EnCase like behavior)
	-x:     use the chunk data instead of the buffered read and write
	        functions.
	-2:     specify the secondary target file (without extension) to write
	        to
```

### `ewfacquirestream`

官方给出的调用示例：`ewfacquirestream -h`

```text
root@kali:~# ewfacquirestream -h
ewfacquirestream 20140816
Use ewfacquirestream to acquire data from a pipe and store it in the EWF format
(Expert Witness Compression Format).
Usage: ewfacquirestream [ -A codepage ] [ -b number_of_sectors ]
                        [ -B number_of_bytes ] [ -c compression_values ]
                        [ -C case_number ] [ -d digest_type ]
                        [ -D description ] [ -e examiner_name ]
                        [ -E evidence_number ] [ -f format ]
                        [ -l log_filename ] [ -m media_type ]
                        [ -M media_flags ] [ -N notes ]
                        [ -o offset ] [ -p process_buffer_size ]
                        [ -P bytes_per_sector ] [ -S segment_file_size ]
                        [ -t target ] [ -2 secondary_target ]
                        [ -hqsvVx ]
	Reads data from stdin
	-A: codepage of header section, options: ascii (default),
	    windows-874, windows-932, windows-936, windows-949,
	    windows-950, windows-1250, windows-1251, windows-1252,
	    windows-1253, windows-1254, windows-1255, windows-1256,
	    windows-1257 or windows-1258
	-b: specify the number of sectors to read at once (per chunk), options:
	    16, 32, 64 (default), 128, 256, 512, 1024, 2048, 4096, 8192, 16384
	    or 32768
	-B: specify the number of bytes to acquire (default is all bytes)
	-c: specify the compression values as: level or method:level
	    compression method options: deflate (default)
	    compression level options: none (default), empty-block,
	    fast or best
	-C: specify the case number (default is case_number).
	-d: calculate additional digest (hash) types besides md5, options:
	    sha1, sha256
	-D: specify the description (default is description).
	-e: specify the examiner name (default is examiner_name).
	-E: specify the evidence number (default is evidence_number).
	-f: specify the EWF file format to write to, options: ftk, encase2,
	    encase3, encase4, encase5, encase6 (default), encase7, linen5,
	    linen6, linen7, ewfx
	-h: shows this help
	-l: logs acquiry errors and the digest (hash) to the log_filename
	-m: specify the media type, options: fixed (default), removable,
	    optical, memory
	-M: specify the media flags, options: logical, physical (default)
	-N: specify the notes (default is notes).
	-o: specify the offset to start to acquire (default is 0)
	-p: specify the process buffer size (default is the chunk size)
	-P: specify the number of bytes per sector (default is 512)
	-q: quiet shows minimal status information
	-s: swap byte pairs of the media data (from AB to BA)
	    (use this for big to little endian conversion and vice versa)
	-S: specify the segment file size in bytes (default is 1.4 GiB)
	    (minimum is 1.0 MiB, maximum is 7.9 EiB for encase6 and
	    encase7 format and 1.9 GiB for other formats)
	-t: specify the target file (without extension) to write to (default
	    is image)
	-v: verbose output to stderr
	-V: print version
	-x: use the chunk data instead of the buffered read and write functions.
	-2: specify the secondary target file (without extension) to write to
```

### `ewfdebug`

官方给出的调用示例：`ewfdebug -h`

```text
root@kali:~# ewfdebug -h
ewfdebug 20140816
Use ewfdebug to analyze EWF file(s).
Usage: ewfdebug [ -A codepage ] [ -hqvV ] ewf_files
	ewf_files: the first or the entire set of EWF segment files
	-A:        codepage of header section, options: ascii (default),
	           windows-874, windows-932, windows-936, windows-949,
	           windows-950, windows-1250, windows-1251, windows-1252,
	           windows-1253, windows-1254, windows-1255, windows-1256,
	           windows-1257 or windows-1258
	-h:        shows this help
	-q:        quiet shows minimal status information
	-v:        verbose output to stderr
	-V:        print version
```

### `ewfexport`

官方给出的调用示例：`ewfexport -h`

```text
root@kali:~# ewfexport -h
ewfexport 20140816
Use ewfexport to export data from the EWF format (Expert Witness Compression
Format) to raw data or another EWF format.
Usage: ewfexport [ -A codepage ] [ -b number_of_sectors ]
                 [ -B number_of_bytes ] [ -c compression_values ]
                 [ -d digest_type ] [ -f format ] [ -l log_filename ]
                 [ -o offset ] [ -p process_buffer_size ]
                 [ -S segment_file_size ] [ -t target ] [ -hqsuvVwx ] ewf_files
	ewf_files: the first or the entire set of EWF segment files
	-A:        codepage of header section, options: ascii (default),
	           windows-874, windows-932, windows-936, windows-949,
	           windows-950, windows-1250, windows-1251, windows-1252,
	           windows-1253, windows-1254, windows-1255, windows-1256,
	           windows-1257 or windows-1258
	-b:        specify the number of sectors to read at once (per chunk),
	           options: 16, 32, 64 (default), 128, 256, 512, 1024, 2048,
	           4096, 8192, 16384 or 32768 (not used for raw and files
	           formats)
	-B:        specify the number of bytes to export (default is all bytes)
	-c:        specify the compression values as: level or method:level
	           compression method options: deflate (default)
	           compression level options: none (default), empty-block,
	           fast or best
	-d:        calculate additional digest (hash) types besides md5,
	           options: sha1, sha256 (not used for raw and files format)
	-f:        specify the output format to write to, options:
	           raw (default), files (restricted to logical volume files), ewf,
	           smart, encase1, encase2, encase3, encase4, encase5, encase6,
	           encase7, encase7-v2, linen5, linen6, linen7, ewfx
	-h:        shows this help
	-l:        logs export errors and the digest (hash) to the log_filename
	-o:        specify the offset to start the export (default is 0)
	-p:        specify the process buffer size (default is the chunk size)
	-q:        quiet shows minimal status information
	-s:        swap byte pairs of the media data (from AB to BA)
	           (use this for big to little endian conversion and vice
	           versa)
	-S:        specify the segment file size in bytes (default is 1.4 GiB)
	           (minimum is 1.0 MiB, maximum is 7.9 EiB for raw, encase6
	           and encase7 format and 1.9 GiB for other formats)
	           (not used for files format)
	-t:        specify the target file to export to, use - for stdout
	           (default is export) stdout is only supported for the raw
	           format
	-u:        unattended mode (disables user interaction)
	-v:        verbose output to stderr
	-V:        print version
	-w:        zero sectors on checksum error (mimic EnCase like behavior)
	-x:        use the chunk data instead of the buffered read and write
	           functions.
```

### `ewfinfo`

官方给出的调用示例：`ewfinfo -h`

```text
root@kali:~# ewfinfo -h
ewfinfo 20140816
Use ewfinfo to determine information about the EWF format (Expert Witness
Compression Format).
Usage: ewfinfo [ -A codepage ] [ -d date_format ] [ -f format ]
               [ -ehimvVx ] ewf_files
	ewf_files: the first or the entire set of EWF segment files
	-A:        codepage of header section, options: ascii (default),
	           windows-874, windows-932, windows-936, windows-949,
	           windows-950, windows-1250, windows-1251, windows-1252,
	           windows-1253, windows-1254, windows-1255, windows-1256,
	           windows-1257 or windows-1258
	-d:        specify the date format, options: ctime (default),
	           dm (day/month), md (month/day), iso8601
	-e:        only show EWF read error information
	-f:        specify the output format, options: text (default),
	           dfxml
	-h:        shows this help
	-i:        only show EWF acquiry information
	-m:        only show EWF media information
	-v:        verbose output to stderr
	-V:        print version
```

### `ewfmount`

官方给出的调用示例：`ewfmount -h`

```text
root@kali:~# ewfmount -h
ewfmount 20140816
Use ewfmount to mount an Expert Witness Compression Format (EWF) image file
Usage: ewfmount [ -f format ] [ -X extended_options ] [ -hvV ] image mount_point
	image:       an Expert Witness Compression Format (EWF) image file
	mount_point: the directory to serve as mount point
	-f:          specify the input format, options: raw (default), files (restricted to
	             logical volume files)
	-h:          shows this help
	-v:          verbose output to stderr, while ewfmount will remain running in the
	             foreground
	-V:          print version
	-X:          extended options to pass to sub system
```

### `ewfrecover`

官方给出的调用示例：`ewfrecover -h`

```text
root@kali:~# ewfrecover -h
ewfrecover 20140816
Use ewfrecover to recover data from corrupt EWF (Expert Witness
Compression Format) files.
Usage: ewfrecover [ -A codepage ]
                  [ -l log_filename ]
                  [ -p process_buffer_size ]
                  [ -t target ] [ -hquvVx ] ewf_files
	ewf_files: the first or the entire set of EWF segment files
	-A:        codepage of header section, options: ascii (default),
	           windows-874, windows-932, windows-936, windows-949,
	           windows-950, windows-1250, windows-1251, windows-1252,
	           windows-1253, windows-1254, windows-1255, windows-1256,
	           windows-1257 or windows-1258
	-h:        shows this help
	-l:        logs recover errors and the digest (hash) to the
	           log_filename
	-p:        specify the process buffer size (default is the chunk size)
	-q:        quiet shows minimal status information
	-t:        specify the target file to recover to (default is recover)
	-u:        unattended mode (disables user interaction)
	-v:        verbose output to stderr
	-V:        print version
	-x:        use the chunk data instead of the buffered read and write
	           functions.
```

### `ewfverify`

官方给出的调用示例：`ewfverify -h`

```text
root@kali:~# ewfverify -h
ewfverify 20140816
Use ewfverify to verify data stored in the EWF format (Expert Witness
Compression Format).
Usage: ewfverify [ -A codepage ] [ -d digest_type ] [ -f format ]
                 [ -l log_filename ] [ -p process_buffer_size ]
                 [ -hqvVwx ] ewf_files
	ewf_files: the first or the entire set of EWF segment files
	-A:        codepage of header section, options: ascii (default),
	           windows-874, windows-932, windows-936, windows-949,
	           windows-950, windows-1250, windows-1251, windows-1252,
	           windows-1253, windows-1254, windows-1255, windows-1256,
	           windows-1257 or windows-1258
	-d:        calculate additional digest (hash) types besides md5,
	           options: sha1, sha256
	-f:        specify the input format, options: raw (default),
	           files (restricted to logical volume files)
	-h:        shows this help
	-l:        logs verification errors and the digest (hash) to the
	           log_filename
	-p:        specify the process buffer size (default is the chunk size)
	-q:        quiet shows minimal status information
	-v:        verbose output to stderr
	-V:        print version
	-w:        zero sectors on checksum error (mimic EnCase like behavior)
	-x:        use the chunk data instead of the buffered read and write
	           functions.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install ewf-tools`，再执行 `ewf-tools --version` 2>/dev/null || `ewf-tools -V`
- [ ] **2.** **读官方帮助** —— `ewf-tools -h`，需要细节时 `man ewf-tools`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ewfacquire [ -A codepage ] [ -b number_of_sectors ]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/libewf/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/libewf/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/libewf/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
