# bulk-extractor

> Extracts information without parsing filesystem bulk_extractor is a C++ program that scans a disk image, a file, or a directory of files and extracts useful information without parsing the file system or file system structures. The results…

> **功能分类**：数字取证 ｜ **Kali 包**：`bulk-extractor` ｜ **官方文档**：<https://www.kali.org/tools/bulk-extractor/>

## 1. 安装

```bash
sudo apt update
sudo apt install bulk-extractor
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.1.1 |
| 架构 | amd64 |
| 可执行命令 | `bulk-extractor`、`bulk_extractor` |
| 依赖 | `libc6`、`libewf2`、`libexpat1`、`libgcc-s1`、`libgcrypt20`、`libre2-11-absl20260526`、`libstdc++6`、`zlib1g`、`bulk_extractor` |
| 安装体积 | 15.82 MB |
| 官网 | <https://github.com/simsong/bulk_extractor> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/bulk-extractor> |
| 包追踪 | <https://pkg.kali.org/pkg/bulk-extractor> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Extract files to the output directory (-o bulk-out) after analyzing the image file (xp-laptop-2005-07-04-1430.img):
root@kali:~# bulk_extractor -o bulk-out xp-laptop-2005-07-04-1430.img
bulk_extractor version: 1.3
Hostname: kali
Input file: xp-laptop-2005-07-04-1430.img
Output directory: bulk-out
Disk Size: 536715264
Threads: 1
Phase 1.
13:02:46 Offset 0MB (0.00%) Done in n/a at 13:02:45
13:03:39 Offset 67MB (12.50%) Done in  0:06:14 at 13:09:53
13:04:43 Offset 134MB (25.01%) Done in  0:05:50 at 13:10:33
13:04:55 Offset 201MB (37.51%) Done in  0:03:36 at 13:08:31
13:06:01 Offset 268MB (50.01%) Done in  0:03:15 at 13:09:16
13:06:48 Offset 335MB (62.52%) Done in  0:02:25 at 13:09:13
13:07:04 Offset 402MB (75.02%) Done in  0:01:25 at 13:08:29
13:07:20 Offset 469MB (87.53%) Done in  0:00:39 at 13:07:59
All Data is Read; waiting for threads to finish...
Time elapsed waiting for 1 thread to finish:
     (please wait for another 60 min .)
Time elapsed waiting for 1 thread to finish:
    6 sec (please wait for another 59 min 54 sec.)
Thread 0: Processing 520093696

Time elapsed waiting for 1 thread to finish:
    12 sec (please wait for another 59 min 48 sec.)
Thread 0: Processing 520093696

Time elapsed waiting for 1 thread to finish:
    18 sec (please wait for another 59 min 42 sec.)
Thread 0: Processing 520093696

Time elapsed waiting for 1 thread to finish:
    24 sec (please wait for another 59 min 36 sec.)
Thread 0: Processing 520093696

Time elapsed waiting for 1 thread to finish:
    30 sec (please wait for another 59 min 30 sec.)
Thread 0: Processing 520093696

All Threads Finished!
Producer time spent waiting: 335.984 sec.
Average consumer time spent waiting: 0.143353 sec.
*******************************************
** bulk_extractor is probably CPU bound. **
**    Run on a computer with more cores  **
**      to get better performance.       **
*******************************************
Phase 2. Shutting down scanners
Phase 3. Creating Histograms
   ccn histogram...   ccn_track2 histogram...   domain histogram...
   email histogram...   ether histogram...   find histogram...
   ip histogram...   tcp histogram...   telephone histogram...
   url histogram...   url microsoft-live...   url services...
   url facebook-address...   url facebook-id...   url searches...

Elapsed time: 378.5 sec.
Overall performance: 1.418 MBytes/sec.
Total email features found: 899
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `bulk_extractor`

> 官方示例调用：`bulk_extractor -o bulk-out xp-laptop-2005-07-04-1430.img`

```text
root@kali:~# bulk_extractor -o bulk-out xp-laptop-2005-07-04-1430.img
bulk_extractor version: 1.3
Hostname: kali
Input file: xp-laptop-2005-07-04-1430.img
Output directory: bulk-out
Disk Size: 536715264
Threads: 1
Phase 1.
13:02:46 Offset 0MB (0.00%) Done in n/a at 13:02:45
13:03:39 Offset 67MB (12.50%) Done in  0:06:14 at 13:09:53
13:04:43 Offset 134MB (25.01%) Done in  0:05:50 at 13:10:33
13:04:55 Offset 201MB (37.51%) Done in  0:03:36 at 13:08:31
13:06:01 Offset 268MB (50.01%) Done in  0:03:15 at 13:09:16
13:06:48 Offset 335MB (62.52%) Done in  0:02:25 at 13:09:13
13:07:04 Offset 402MB (75.02%) Done in  0:01:25 at 13:08:29
13:07:20 Offset 469MB (87.53%) Done in  0:00:39 at 13:07:59
All Data is Read; waiting for threads to finish...
Time elapsed waiting for 1 thread to finish:
     (please wait for another 60 min .)
Time elapsed waiting for 1 thread to finish:
    6 sec (please wait for another 59 min 54 sec.)
Thread 0: Processing 520093696
Time elapsed waiting for 1 thread to finish:
    12 sec (please wait for another 59 min 48 sec.)
Thread 0: Processing 520093696
Time elapsed waiting for 1 thread to finish:
    18 sec (please wait for another 59 min 42 sec.)
Thread 0: Processing 520093696
Time elapsed waiting for 1 thread to finish:
    24 sec (please wait for another 59 min 36 sec.)
Thread 0: Processing 520093696
Time elapsed waiting for 1 thread to finish:
    30 sec (please wait for another 59 min 30 sec.)
Thread 0: Processing 520093696
All Threads Finished!
Producer time spent waiting: 335.984 sec.
Average consumer time spent waiting: 0.143353 sec.
*******************************************
** bulk_extractor is probably CPU bound. **
**    Run on a computer with more cores  **
**      to get better performance.       **
*******************************************
Phase 2. Shutting down scanners
Phase 3. Creating Histograms
   ccn histogram...   ccn_track2 histogram...   domain histogram...
   email histogram...   ether histogram...   find histogram...
   ip histogram...   tcp histogram...   telephone histogram...
   url histogram...   url microsoft-live...   url services...
   url facebook-address...   url facebook-id...   url searches...
Elapsed time: 378.5 sec.
Overall performance: 1.418 MBytes/sec.
Total email features found: 899
```

### `bulk_extractor -h`

> 官方示例调用：`bulk_extractor -h`

```text
root@kali:~# bulk_extractor -h
bulk_extractor version 2.1.1: A high-performance flexible digital forensics program.
Usage:
  bulk_extractor [OPTION...] image_name
  -A, --offset_add arg          Offset added (in bytes) to feature locations
                                (default: 0)
  -b, --banner_file arg         Path of file whose contents are prepended to
                                top of all feature files
  -C, --context_window arg      Size of context window reported in bytes
                                (default: 16)
  -d, --debug arg               enable debugging (default: 1)
  -D, --debug_help              help on debugging
  -E, --enable_exclusive arg    disable all scanners except the one specified.
                                Same as -x all -E scanner.
  -e, --enable arg              enable a scanner (can be repeated)
  -x, --disable arg             disable a scanner (can be repeated)
  -f, --find arg                search for a pattern (can be repeated)
  -F, --find_file arg           read patterns to search from a file (can be
                                repeated)
  -G, --pagesize arg            page size in bytes (default: 16777216)
  -g, --marginsize arg          margin size in bytes (default: 4194304)
  -j, --threads arg             number of threads (default: 6)
  -J, --no_threads              read and process data in the primary thread
  -M, --max_depth arg           max recursion depth (default: 12)
      --max_bad_alloc_errors arg
                                max bad allocation errors (default: 3)
      --max_minute_wait arg     maximum number of minutes to wait until all
                                data are read (default: 60)
      --notify_main_thread      Display notifications in the main thread after
                                phase1 completes. Useful for running with
                                ThreadSanitizer
      --notify_async            Display notificaitons asynchronously (default)
  -o, --outdir arg              output directory [REQUIRED]
  -P, --scanner_dir arg         directories for scanner shared libraries (can
                                be repeated). Default directories include
                                /usr/local/lib/bulk_extractor,
                                /usr/lib/bulk_extractor and any directories
                                specified in the BE_PATH environment variable.
  -p, --path arg                print the value of <path>[:length][/h][/r] with
                                optional length, hex output, or raw output.
  -q, --quit                    no status or performance output
  -r, --alert_list arg          file to read alert list from
  -R, --recurse                 treat image file as a directory to recursively
                                explore
  -S, --set arg                 set a name=value option (can be repeated)
  -s, --sampling arg            random sampling parameter frac[:passes]
  -V, --version                 Display PACKAGE_VERSION (currently) 2.1.1
  -w, --stop_list arg           file to read stop list from
  -Y, --scan arg                specify <start>[-end] of area on disk to scan
  -z, --page_start arg          specify a starting page number
  -Z, --zap                     wipe the output directory (recursively) before
                                starting
  -0, --no_notify               disable real-time notification
  -1, --version1                version 1.0 notification (console-output)
  -H, --info_scanners           report information about each scanner
  -h, --help                    print help screen
Global config options:
   -S notify_rate=1    seconds between notificaiton update (notify_rate)
   -S debug_histogram_malloc_fail_frequency=0    Set >0 to make histogram maker fail with memory allocations (debug_histogram_malloc_fail_frequency)
   -S hash_alg=sha1    Specifies hash algorithm to be used for all hash calculations (hash_alg)
   -S report_read_errors=1    Report read errors (report_read_errors)
These scanners enabled; disable with -x:
   -x accts - disable scanner accts
     -S ssn_mode=0    0=Normal; 1=No `SSN' required; 2=No dashes required
     -S min_phone_digits=7    Min. digits required in a phone
   -x aes - disable scanner aes
     -S scan_aes_128=1    Scan for 128-bit AES keys; 0=No, 1=Yes
     -S scan_aes_192=0    Scan for 192-bit AES keys; 0=No, 1=Yes
     -S scan_aes_256=1    Scan for 256-bit AES keys; 0=No, 1=Yes
   -x base64 - disable scanner base64
   -x elf - disable scanner elf
   -x email - disable scanner email
   -x evtx - disable scanner evtx
   -x exif - disable scanner exif
     -S exif_debug=0    debug exif decoder
   -x facebook - disable scanner facebook
   -x find - disable scanner find
   -x gps - disable scanner gps
   -x gzip - disable scanner gzip
     -S gzip_max_uncompr_size=268435456    maximum size for decompressing GZIP objects
   -x httplogs - disable scanner httplogs
   -x json - disable scanner json
   -x kml_carved - disable scanner kml_carved
   -x msxml - disable scanner msxml
   -x net - disable scanner net
     -S carve_net_memory=0    Carve network  memory structures
     -S min_carve_packet_bytes=40    Smallest network packet to carve
   -x ntfsindx - disable scanner ntfsindx
   -x ntfslogfile - disable scanner ntfslogfile
   -x ntfsmft - disable scanner ntfsmft
   -x ntfsusn - disable scanner ntfsusn
   -x pdf - disable scanner pdf
     -S pdf_dump_hex=0    Dump the contents of PDF buffers as hex
     -S pdf_dump_text=0    Dump the contents of PDF buffers showing extracted text
   -x rar - disable scanner rar
     -S rar_find_components=1    Search for RAR components
     -S rar_find_volumes=1    Search for RAR volumes
   -x sqlite - disable scanner sqlite
   -x utmp - disable scanner utmp
   -x vcard_carved - disable scanner vcard_carved
   -x vin - disable scanner vin
     -S vin_debug=0    Enable VIN scanner debugging
   -x windirs - disable scanner windirs
     -S opt_weird_file_size=157286400    Threshold for FAT32 scanner
     -S opt_weird_file_size2=536870912    Threshold for FAT32 scanner
     -S opt_weird_cluster_count=67108864    Threshold for FAT32 scanner
     -S opt_weird_cluster_count2=268435456    Threshold for FAT32 scanner
     -S opt_max_bits_in_attrib=3    Ignore FAT32 entries with more attributes set than this
     -S opt_max_weird_count=2    Number of 'weird' counts to ignore a FAT32 entry
     -S opt_last_year=2031    Ignore FAT32 entries with a later year than this
   -x winlnk - disable scanner winlnk
   -x winpe - disable scanner winpe
   -x winprefetch - disable scanner winprefetch
   -x zip - disable scanner zip
     -S zip_min_uncompr_size=6    Minimum size of a ZIP uncompressed object
     -S zip_max_uncompr_size=268435456    Maximum size of a ZIP uncompressed object
     -S zip_name_len_max=1024    Maximum name of a ZIP component filename
These scanners disabled; enable with -e:
   -e base16 - enable scanner base16
   -e hiberfile - enable scanner hiberfile
   -e outlook - enable scanner outlook
   -e wordlist - enable scanner wordlist
     -S word_min=6    Minimum word size
     -S word_max=16    Maximum word size
     -S max_output_file_size=100000000    Maximum size of the words output file
     -S strings=0    Scan for strings instead of words
   -e xor - enable scanner xor
     -S xor_mask=255    XOR mask value, in decimal
Options for setting carve mode in feature recorders that support carving:
   -S evtx_carved_carve_mode=n  where n=[0,1,2]
   -S jpeg_carve_mode=n  where n=[0,1,2]
   -S kml_carved_carve_mode=n  where n=[0,1,2]
   -S ntfsindx_carved_carve_mode=n  where n=[0,1,2]
   -S ntfslogfile_carved_carve_mode=n  where n=[0,1,2]
   -S ntfsmft_carved_carve_mode=n  where n=[0,1,2]
   -S ntfsusn_carved_carve_mode=n  where n=[0,1,2]
   -S rar_carve_mode=n  where n=[0,1,2]
   -S sqlite_carved_carve_mode=n  where n=[0,1,2]
   -S unrar_carved_carve_mode=n  where n=[0,1,2]
   -S utmp_carved_carve_mode=n  where n=[0,1,2]
   -S vcard_carve_mode=n  where n=[0,1,2]
   -S winpe_carved_carve_mode=n  where n=[0,1,2]
   -S zip_carve_mode=n  where n=[0,1,2]
Carve mode 0: do not carve; mode 1: carve encoded data; mode 2: carve everything.
Updated on: 2026-Aug-25
 Edit this page
braa
burpsuite
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install bulk-extractor`，再执行 `bulk-extractor --version` 2>/dev/null || `bulk-extractor -V`
- [ ] **2.** **读官方帮助** —— `bulk-extractor -h`，需要细节时 `man bulk-extractor`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/bulk-extractor/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[bulk-extractor](../../tools/tutorials/09-数字取证/bulk-extractor.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/bulk-extractor/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/bulk-extractor/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
