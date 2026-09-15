# util-linux

> Miscellaneous system utilities This package contains a number of important utilities, most of which are oriented towards maintenance of your system. Some of the more important utilities included in this package allow you to view kernel mes…

> **功能分类**：信息搜集 ｜ **Kali 包**：`util-linux` ｜ **官方文档**：<https://www.kali.org/tools/util-linux/>

## 1. 安装

```bash
sudo apt update
sudo apt install util-linux
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.42.2 |
| 架构 | any |
| 可执行命令 | `bsdextrautils`、`col`、`colcrt`、`colrm`、`column`、`hd`、`hexdump`、`look`、`rev`、`ul`、`bsdutils`、`renice`、`script`、`scriptlive`、`scriptreplay`、`wall`、`eject`、`eject-udeb`、`fdisk`、`cfdisk`、`sfdisk`、`fdisk-udeb`、`lastlog2`、`libblkid-dev`、`libblkid1`、`libblkid1-udeb`、`libfdisk-dev`、`libfdisk1`、`libfdisk1-udeb`、`liblastlog2-2`、`liblastlog2-dev`、`libmount-dev`、`libmount1`、`libmount1-udeb`、`libpam-lastlog2`、`libsmartcols-dev`、`libsmartcols1`、`libsmartcols1-udeb`、`libuuid1`、`libuuid1-udeb`、`login`、`nologin`、`mount`、`losetup`、`swapoff`、`swapon`、`umount`、`rfkill`、`util-linux`、`agetty`、`blkdiscard`、`blkid`、`blockdev`、`choom`、`chrt`、`dmesg`、`fallocate`、`findfs`、`findmnt`、`flock`、`fsck`、`fsfreeze`、`fstrim`、`getopt`、`getty`、`hardlink`、`i386`、`ionice`、`ipcmk`、`ipcrm`、`ipcs`、`linux32`、`linux64`、`logger`、`lsblk`、`lscpu`、`lsipc`、`lslocks`、`lsns`、`mcookie`、`mkfs`、`mkswap`、`more`、`mountpoint`、`namei`、`nsenter`、`partx`、`prlimit`、`readprofile`、`rtcwake`、`runuser`、`setarch`、`setpriv`、`setsid`、`setterm`、`su`、`sulogin`、`swaplabel`、`taskset`、`uclampset`、`unshare`、`whereis`、`wipefs`、`x86_64`、`zramctl`、`util-linux-extra`、`addpart`、`bits`、`blkpr`、`blkzone`、`chcpu`、`chmem`、`copyfilerange`、`coresched`、`ctrlaltdel`、`delpart`、`enosys`、`exch`、`fadvise`、`fincore`、`fsck.cramfs`、`fsck.minix`、`getino`、`hwclock`、`isosize`、`ldattach`、`lsclocks`、`lsfd`、`lsirq`、`lslogins`、`lsmem`、`mkfs.bfs`、`mkfs.cramfs`、`mkfs.minix`、`newgrp`、`pipesz`、`pivot_root`、`rename.ul`、`resizepart`、`sg`、`switch_root`、`waitpid`、`wdctl`、`util-linux-locales`、`util-linux-udeb`、`uuid-dev`、`uuid-runtime`、`uuidd`、`uuidgen`、`uuidparse` |
| 依赖 | `libblkid1`、`libc6`、`libcap-ng0`、`libcrypt1`、`libmount1`、`libpam-modules`、`libpam-runtime`、`libpam0g`、`libselinux1`、`libsmartcols1`、`libsystemd0`、`libtinfo6` 等 |
| 安装体积 | 4.54 MB |
| 官网 | <https://github.com/util-linux/util-linux> |
| 源码仓库 | <https://salsa.debian.org/debian/util-linux> |
| 包追踪 | <https://pkg.kali.org/pkg/util-linux> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
bsdextrautils -h          # 查看用法
man bsdextrautils         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 150 个可执行命令，下面是官方页面内嵌的帮助原文。

### `col`

> 官方示例调用：`col --help`

```text
root@kali:~# col --help
Usage:
 col [options]
Filter out reverse line feeds from standard input.
Options:
 -b, --no-backspaces    do not output backspaces
 -f, --fine             permit forward half line feeds
 -p, --pass             pass unknown control sequences
 -h, --tabs             convert spaces to tabs
 -x, --spaces           convert tabs to spaces
 -l, --lines NUM        buffer at least NUM lines
 -H, --help             display this help
 -V, --version          display version
For more details see col(1).
```

### `colcrt`

> 官方示例调用：`colcrt -h`

```text
root@kali:~# colcrt -h
Usage:
 colcrt [options] [<file>...]
Filter nroff output for CRT previewing.
Options:
 -,  --no-underlining    suppress all underlining
 -2, --half-lines        print all half-lines
 -h, --help              display this help
 -V, --version           display version
For more details see colcrt(1).
```

### `colrm`

> 官方示例调用：`colrm -h`

```text
root@kali:~# colrm -h
Usage:
 colrm [startcol [endcol]]
Filter out the specified columns from standard input.
Options:
 -h, --help     display this help
 -V, --version  display version
For more details see colrm(1).
```

### `column`

> 官方示例调用：`column -h`

```text
root@kali:~# column -h
Usage:
 column [options] [<file>...]
Columnate lists.
Options:
 -t, --table                      create a table
 -n, --table-name <name>          table name for JSON output
 -O, --table-order <columns>      specify order of output columns
     --table-colorscheme <name>   specify color scheme name
 -C, --table-column <properties>  define column
 -N, --table-columns <names>      comma separated columns names
 -l, --table-columns-limit <num>  maximal number of input columns
 -E, --table-noextreme <columns>  don't count long text in these columns
                                    to the column's width
 -d, --table-noheadings           don't print header
 -m, --table-maxout               fill all available space
 -e, --table-header-repeat        repeat header for each page
 -K, --table-header-as-columns    use the first row as table header
 -H, --table-hide <columns>       don't print the columns
 -R, --table-right <columns>      right align text in these columns
 -T, --table-truncate <columns>   truncate text in the columns when necessary
 -W, --table-wrap <columns>       wrap text in the columns when necessary
     --wrap-separator <string>    wrap at this separator (requires --table-wrap)
 -L, --keep-empty-lines           don't ignore empty lines
 -J, --json                       use JSON output format for table
 -r, --tree <column>              column to use tree-like output for the table
 -i, --tree-id <column>           line ID to specify child-parent relation
 -p, --tree-parent <column>       parent to specify child-parent relation
 -c, --output-width <width>       width of output in number of characters
 -o, --output-separator <string>  columns separator for table output
                                    (default is two spaces)
 -s, --input-separator, --separator <string>
                                    possible table delimiters
 -x, --fillrows                   fill rows before columns
 -S, --use-spaces <number>        minimal whitespaces between columns (no tabs)
     --color[=<when>]             colorize output (auto, always or never)
                                    colors are enabled by default
 -h, --help                       display this help
 -V, --version                    display version
For more details see column(1).
```

### `hd`

> 官方示例调用：`hd -h`

```text
root@kali:~# hd -h
Usage:
 hd [options] <file>...
Display file contents in hexadecimal, decimal, octal, or ascii.
Options:
 -b, --one-byte-octal      one-byte octal display
 -X, --one-byte-hex        one-byte hexadecimal display
 -c, --one-byte-char       one-byte character display
 -C, --canonical           canonical hex+ASCII display
 -d, --two-bytes-decimal   two-byte decimal display
 -o, --two-bytes-octal     two-byte octal display
 -x, --two-bytes-hex       two-byte hexadecimal display
 -L, --color[=<mode>]      interpret color formatting specifiers
                             colors are enabled by default
 -e, --format <format>     format string to be used for displaying data
 -f, --format-file <file>  file that contains format strings
 -n, --length <length>     interpret only length bytes of input
 -s, --skip <offset>       skip offset bytes from the beginning
 -v, --no-squeezing        output identical lines
 -h, --help                display this help
 -V, --version             display version
Arguments:
 Values for <length> and <offset> may be followed by a suffix: KiB, MiB,
 GiB, TiB, PiB, EiB, ZiB, or YiB (where the "iB" is optional).
For more details see hexdump(1).
```

### `hexdump`

> 官方示例调用：`hexdump -h`

```text
root@kali:~# hexdump -h
Usage:
 hexdump [options] <file>...
Display file contents in hexadecimal, decimal, octal, or ascii.
Options:
 -b, --one-byte-octal      one-byte octal display
 -X, --one-byte-hex        one-byte hexadecimal display
 -c, --one-byte-char       one-byte character display
 -C, --canonical           canonical hex+ASCII display
 -d, --two-bytes-decimal   two-byte decimal display
 -o, --two-bytes-octal     two-byte octal display
 -x, --two-bytes-hex       two-byte hexadecimal display
 -L, --color[=<mode>]      interpret color formatting specifiers
                             colors are enabled by default
 -e, --format <format>     format string to be used for displaying data
 -f, --format-file <file>  file that contains format strings
 -n, --length <length>     interpret only length bytes of input
 -s, --skip <offset>       skip offset bytes from the beginning
 -v, --no-squeezing        output identical lines
 -h, --help                display this help
 -V, --version             display version
Arguments:
 Values for <length> and <offset> may be followed by a suffix: KiB, MiB,
 GiB, TiB, PiB, EiB, ZiB, or YiB (where the "iB" is optional).
For more details see hexdump(1).
```

### `look`

> 官方示例调用：`look -h`

```text
root@kali:~# look -h
Usage:
 look [options] <string> [<file>...]
Display lines beginning with a specified string.
Options:
 -a, --alternative        use the alternative dictionary
 -d, --alphanum           compare only blanks and alphanumeric characters
 -f, --ignore-case        ignore case differences when comparing
 -t, --terminate <char>   define the string-termination character
 -h, --help               display this help
 -V, --version            display version
For more details see look(1).
```

### `rev`

> 官方示例调用：`rev -h`

```text
root@kali:~# rev -h
Usage:
 rev [options] [<file> ...]
Reverse lines characterwise.
Options:
 -0, --zero     use the NUL byte as line separator
 -h, --help     display this help
 -V, --version  display version
For more details see rev(1).
```

### `ul`

> 官方示例调用：`ul -h`

```text
root@kali:~# ul -h
Usage:
 ul [options] [<file> ...]
Do underlining.
Options:
 -t, -T, --terminal TERMINAL  override the TERM environment variable
 -i, --indicated              underlining is indicated via a separate line
 -h, --help                   display this help
 -V, --version                display version
For more details see ul(1).
```

### `renice`

> 官方示例调用：`renice -h`

```text
root@kali:~# renice -h
Usage:
 renice [-n|--priority|--relative] <priority> [-p|--pid] <pid>...
 renice [-n|--priority|--relative] <priority>  -g|--pgrp <pgid>...
 renice [-n|--priority|--relative] <priority>  -u|--user <user>...
Alter the priority of running processes.
Options:
 -n <num>               specify the 'absolute' nice value,
                          but 'relative' when POSIXLY_CORRECT is set
 --priority <num>       specify the 'absolute' nice value
 --relative <num>       specify the 'relative' nice value
 -p, --pid              interpret arguments as process ID (default)
 -g, --pgrp             interpret arguments as process group ID
 -u, --user             interpret arguments as username or user ID
 -h, --help             display this help
 -V, --version          display version
For more details see renice(1).
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install util-linux`，再执行 `bsdextrautils --version` 2>/dev/null || `bsdextrautils -V`
- [ ] **2.** **读官方帮助** —— `bsdextrautils -h`，需要细节时 `man bsdextrautils`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/util-linux/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[set](../../tools/tutorials/11-社会工程与报告/set.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/util-linux/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/util-linux/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
