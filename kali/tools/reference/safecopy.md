# safecopy

> Data recovery tool for problematic or damaged media Safecopy tries to get as much data from SOURCE as possible, even resorting to device specific low level operations if applicable. This is achieved by identifying problematic or damaged ar…

> **功能分类**：数字取证 ｜ **Kali 包**：`safecopy` ｜ **官方文档**：<https://www.kali.org/tools/safecopy/>

## 1. 安装

```bash
sudo apt update
sudo apt install safecopy
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.7 |
| 架构 | any |
| 可执行命令 | `safecopy` |
| 依赖 | `libc6` |
| 安装体积 | 97 KB |
| 官网 | <http://safecopy.sf.net> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/safecopy> |
| 包追踪 | <https://pkg.kali.org/pkg/safecopy> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
safecopy -h          # 查看用法
man safecopy         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `safecopy`

官方给出的调用示例：`safecopy -h`

```text
root@kali:~# safecopy -h
Safecopy 1.7 by CorvusCorax
Usage: safecopy [options] <source> <target>
Options:
	--stage1 : Preset to rescue most of the data fast,
	           using no retries and avoiding bad areas.
	           Presets: -f 10% -r 10% -R 1 -Z 0 -L 2 -M BaDbLoCk
	                    -o stage1.badblocks
	--stage2 : Preset to rescue more data, using no retries
	           but searching for exact ends of bad areas.
	           Presets: -f 128* -r 1* -R 1 -Z 0 -L 2
	                    -I stage1.badblocks
	                    -o stage2.badblocks
	--stage3 : Preset to rescue everything that can be rescued
	           using maximum retries, head realignment tricks
	           and low level access.
	           Presets: -f 1* -r 1* -R 4 -Z 1 -L 2
	                    -I stage2.badblocks
	                    -o stage3.badblocks
	All stage presets can be overridden by individual options.
	-b <size> : Blocksize for default read operations.
	            Set this to the physical sectorsize of your media.
	            Default: 1*
	            Hardware block size if reported by OS, otherwise 4096
	-f <size> : Blocksize when skipping over badblocks.
	            Higher settings put less strain on your hardware,
	            but you might miss good areas in between two bad ones.
	            Default: 16*
	-r <size> : Resolution in bytes when searching for the exact
	            beginning or end of a bad area.
	            If you read data directly from a device there is no
	            need to set this lower than the hardware blocksize.
	            On mounted filesystems however, read blocks
	            and physical blocks could be misaligned.
	            Smaller values lead to very thorough attempts to read
	            data at the edge of damaged areas,
	            but increase the strain on the damaged media.
	            Default: 1*
	-R <number> : At least that many read attempts are made on the first
	              bad block of a damaged area with minimum resolution.
	              More retries can sometimes recover a weak sector,
	              but at the cost of additional strain.
	              Default: 3
	-Z <number> : On each error, force seek the read head from start to
	              end of the source device as often as specified.
	              That takes time, creates additional strain and might
	              not be supported by all devices or drivers.
	              Default: 1
	-L <mode> : Use low level device calls as specified:
	                   0  Do not use low level device calls
	                   1  Attempt low level device calls
	                      for error recovery only
	                   2  Always use low level device calls
	                      if available
	            Supported low level features in this version are:
	                SYSTEM  DEVICE TYPE   FEATURE
	                Linux   cdrom/dvd     bus/device reset
	                Linux   cdrom         read sector in raw mode
	                Linux   floppy        controller reset, twaddle
	            Default: 1
	--sync : Use synchronized read calls (disable driver buffering).
	         Safecopy will use O_DIRECT if supported by the OS
	         and O_SYNC otherwise.
	         Default: Asynchronous read buffering by the OS is allowed
	--forceopen : Keep trying to reopen the source after a read errer
	              useful for USB drives that go away temporarily.
	              Warning: This can cause safecopy to hang
	                       until aborted manually!
	              Default: Abort on fopen() error
	-s <blocks> : Start position where to start reading.
	              Will correspond to position 0 in the destination file.
	              Default: block 0
	-l <blocks> : Maximum length of data to be read.
	              Default: Entire size of input file
	-I <badblockfile> : Incremental mode. Assume the target file already
	                    exists and has holes specified in the badblockfile.
	                    It will be attempted to retrieve more data from
	                    the listed blocks or from beyond the file size
	                    of the target file only.
	                    Warning: Without this option, the destination file
	                    will be emptied prior to writing.
	                    Use -I /dev/null if you want to continue a previous
	                    run of safecopy without a badblock list.
	                    Implies: -c 0 if -c is not specified
	                    Default: none ( /dev/null if -c is given )
	-i <bytes> : Blocksize to interpret the badblockfile given with -I.
	             Default: Blocksize as specified by -b
	-c <blocks> : Continue copying at this position.
	              This allows continuing if the output is a block device
	              with a fixed size as opposed to a growable file,
	              where safecopy cannot determine how far it already got.
	              The blocksize used is the same as for the -I option.
	              -c 0 will continue at the current destination size.
	              Implies: -I /dev/null if -I is not specified
	              Default: none, 0 if -I is specified
	-X <badblockfile> : Exclusion mode. If used together with -I,
	                    excluded blocks override included blocks.
	                    Safecopy will not read or write any data from
	                    areas covered by exclude blocks.
	                    Default: none ( 0 if -I is given )
	-x <bytes> : Blocksize to interpret the badblockfile given with -X.
	             Default: Blocksize as specified by -b
	-o <badblockfile> : Write a badblocks/e2fsck compatible bad block file.
	                    Default: none
	-S <seekscript> : Use external script for seeking in input file.
	                  (Might be useful for tape devices and similar).
	                  Seekscript must be an executable that takes the
	                  number of blocks to be skipped as argv1 (1-64)
	                  the blocksize in bytes as argv2
	                  and the current position (in bytes) as argv3.
	                  Return value needs to be the number of blocks
	                  successfully skipped, or 0 to indicate seek failure.
	                  The external seekscript will only be used
	                  if lseek() fails and we need to skip over data.
	                  Default: none
	-M <string> : Mark unrecovered data with this string instead of
	              skipping it. This helps in later finding corrupted
	              files on rescued file system images.
	              The default is to zero unreadable data on creation
	              of output files, and leaving the data as it is
	              on any later run.
	              Warning: When used in combination with
	              incremental mode (-I) this may overwrite data
	              in any block that occurs in the -I file.
	              Blocks not in the -I file, or covered by the file
	              specified with -X are save from being overwritten.
	              Default: none
	--debug <level> : Enable debug output. Level is a bit field,
	                  add values together for more information:
	                     program flow:     1
	                     IO control:       2
	                     badblock marking: 4
	                     seeking:          8
	                     incremental mode: 16
	                     exclude mode:     32
	                  or for all debug output: 255
	                  Default: 0
	-T <timingfile> : Write sector read timing information into
	                  this file for later analysis.
	                  Default: none
	-h | --help : Show this text
Valid parameters for -f -r -b <size> options are:
	<integer>	Amount in bytes - i.e. 1024
	<percentage>%	Percentage of whole file/device size - e.g. 10%
	<number>*	-b only, number times blocksize reported by OS
	<number>*	-f and -r only, number times the value of -b
Description of output:
	. : Between 1 and 1024 blocks successfully read.
	_ : Read of block was incomplete. (possibly end of file)
	    The blocksize is now reduced to read the rest.
	|/| : Seek failed, source can only be read sequentially.
	> : Read failed, reducing blocksize to read partial data.
	! : A low level error on read attempt of smallest allowed size
	    leads to a retry attempt.
	[xx](+yy){ : Current block and number of bytes continuously
	             read successfully up to this point.
	X : Read failed on a block with minimum blocksize and is skipped.
	    Unrecoverable error, destination file is padded with zeros.
	    Data is now skipped until end of the unreadable area is reached.
	< : Successful read after the end of a bad area causes
	    backtracking with smaller blocksizes to search for the first
	    readable data.
	}[xx](+yy) : current block and number of bytes of recent
	             continuous unreadable data.
Copyright 2012 CorvusCorax
This is free software. You may redistribute copies of it under
the terms of the GNU General Public License version 2 or above.
	<http://www.gnu.org/licenses/gpl2.html>.
There is NO WARRANTY, to the extent permitted by law.
Updated on: 2026-Mar-02
 Edit this page
rtpflood
sara
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install safecopy`，再执行 `safecopy --version` 2>/dev/null || `safecopy -V`
- [ ] **2.** **读官方帮助** —— `safecopy -h`，需要细节时 `man safecopy`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: safecopy [options] <source> <target>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/safecopy/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/safecopy/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/safecopy/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
