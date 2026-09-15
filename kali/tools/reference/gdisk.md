# gdisk

> GPT fdisk text-mode partitioning tool GPT fdisk (aka gdisk) is a text-mode partitioning tool that provides utilities for Globally Unique Identifier (GUID) Partition Table (GPT) disks. Features: Edit GUID partition table definitions

> **功能分类**：通用工具 ｜ **Kali 包**：`gdisk` ｜ **官方文档**：<https://www.kali.org/tools/gdisk/>

## 1. 安装

```bash
sudo apt update
sudo apt install gdisk
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0.10 |
| 架构 | any |
| 可执行命令 | `gdisk`、`cgdisk`、`fixparts`、`sgdisk` |
| 依赖 | `libc6`、`libgcc-s1`、`libncursesw6`、`libpopt0`、`libstdc++6`、`libtinfo6`、`libuuid1`、`cgdisk` |
| 安装体积 | 967 KB |
| 官网 | <http://sourceforge.net/projects/gptfdisk/> |
| 源码仓库 | <https://salsa.debian.org/debian/gdisk> |
| 包追踪 | <https://pkg.kali.org/pkg/gdisk> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gdisk -h          # 查看用法
man gdisk         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man cgdisk`

```text
root@kali:~# man cgdisk
CGDISK(8)                       GPT fdisk Manual                      CGDISK(8)
NAME
     cgdisk - Curses-based GUID partition table (GPT) manipulator
SYNOPSIS
     cgdisk [ -a ] device
DESCRIPTION
     GPT  fdisk is a text-mode family of programs for creation and manipulation
     of partition tables. The cgdisk member of this family  employs  a  curses-
     based  user interface for interaction using a text-mode menuing system. It
     will automatically convert an old-style Master Boot Record (MBR) partition
     table or BSD disklabel stored without an  MBR  carrier  partition  to  the
     newer  Globally  Unique Identifier (GUID) Partition Table (GPT) format, or
     will load a GUID partition table. Other members of this program family are
     gdisk (the most feature-rich program of the group, with a non-curses-based
     interactive user interface) and sgdisk (which is driven  via  command-line
     options  for use by experts or in scripts).  FixParts is a related program
     for fixing a limited set of problems with MBR disks.
     For information on MBR vs. GPT, as well as GPT terminology and  structure,
     see   the   extended   GPT   fdisk   documentation   at  https://www.rods-
     books.com/gdisk/ or consult Wikipedia.
     The cgdisk program employs a user interface similar  to  that  of  Linux's
     cfdisk,  but cgdisk modifies GPT partitions. It also has the capability of
     transforming MBR partitions or BSD disklabels into  GPT  partitions.  Like
     the  original cfdisk program, cgdisk does not modify disk structures until
     you explicitly write them to disk, so if you make a mistake, you can  exit
     from the program with the Quit option to leave your partitions unmodified.
     Ordinarily,  cgdisk  operates  on  disk  device files, such as /dev/sda or
     /dev/hda under Linux, /dev/disk0 under Mac OS X, or /dev/ad0  or  /dev/da0
     under FreeBSD. The program can also operate on disk image files, which can
     be  either  copies of whole disks (made with dd, for instance) or raw disk
     images used by emulators such as QEMU or VMWare. Note that only  raw  disk
     images  are  supported; cgdisk cannot work on compressed or other advanced
     disk image formats.
     Upon start, cgdisk attempts to identify the partition type in use  on  the
     disk.  If  it  finds valid GPT data, cgdisk will use it. If cgdisk finds a
     valid MBR or BSD disklabel but no GPT data, it will attempt to convert the
     MBR or disklabel into GPT form. (BSD disklabels are likely to  have  unus-
     able  first and/or final partitions because they overlap with the GPT data
     structures, though.) Upon exiting with the 'w' option, cgdisk replaces the
     MBR or disklabel with a GPT. This action is  potentially  dangerous!  Your
     system  may  become  unbootable,  and partition type codes may become cor-
     rupted if the disk uses unrecognized type codes.  Boot problems  are  par-
     ticularly  likely  if you're multi-booting with any GPT-unaware OS. If you
     mistakenly launch cgdisk on an MBR disk, you can safely exit  the  program
     without making any changes by using the Quit option.
     When  creating  a  fresh partition table, certain considerations may be in
     order:
     *      For data (non-boot) disks, and for boot disks  used  on  BIOS-based
            computers  with  GRUB as the boot loader, partitions may be created
            in whatever order and in whatever sizes are desired.
     *      Boot disks for EFI-based systems require an  EFI  System  Partition
            (GPT  fdisk  internal code 0xEF00) formatted as FAT-32.  The recom-
            mended size of this partition is between 100 and 300 MiB.  Boot-re-
            lated files are stored here. (Note that GNU Parted identifies  such
            partitions as having the "boot flag" set.)
     *      The  GRUB  2 boot loader for BIOS-based systems makes use of a BIOS
            Boot Partition (GPT fdisk internal code 0xEF02), in which the  sec-
            ondary  boot loader is stored, without the benefit of a filesystem.
            This partition can typically be quite small (roughly 32  KiB  to  1
            MiB), but you should consult your boot loader documentation for de-
            tails.
     *      If  Windows  is  to  boot  from a GPT disk, a partition of type Mi-
            crosoft Reserved (GPT fdisk internal code 0x0C01)  is  recommended.
            This  partition should be about 128 MiB in size. It ordinarily fol-
            lows the EFI System Partition and immediately precedes the  Windows
            data  partitions.  (Note that old versions of GNU Parted create all
            FAT partitions as this type, which actually makes the partition un-
            usable for normal file storage in both Windows and Mac OS X.)
     *      Some OSes' GPT utilities create some  blank  space  (typically  128
            MiB)  after  each  partition.  The  intent is to enable future disk
            utilities to use this space. Such free space is not required of GPT
            disks, but creating it may help in future disk maintenance. You can
            use GPT fdisk's relative partition positioning  option  (specifying
            the  starting sector as '+128M', for instance) to simplify creating
            such gaps.
OPTIONS
     Only one command-line option is accepted, aside from the device  filename:
     -a.  This  option alters the highlighting of partitions and blocks of free
     space: Instead of using ncurses, when -a is used cgdisk uses a ">"  symbol
     to  the  left of the selected partition or free space.  This option is in-
     tended for use on limited display devices such  as  teletypes  and  screen
     readers.
     Interactions  with cgdisk occur with its interactive text-mode menus.  The
     display is broken into two interactive parts:
     *      The partition display area, in which partitions  and  gaps  between
            them (marked as "free space") are summarized.
     *      The  option  selection  area, in which buttons for the main options
            appear.
     In addition, the top of the display shows the program's name  and  version
     number,  the device filename associated with the disk, and the disk's size
     in both sectors and IEEE-1541 units (GiB, TiB, and so on).
     You can use the following keys to move among the various  options  and  to
     select among them:
     up arrow
            This key moves the partition selection up by one partition.
     down arrow
            This key moves the partition selection down by one partition.
     Page Up
            This key moves the partition selection up by one screen.
     Page Down
            This key moves the partition selection down by one screen.
     right arrow
            This key moves the option selection to the right by one item.
     left arrow
            This key moves the option selection to the left by one item.
     Enter  This  key activates the currently selected option. You can also ac-
            tivate an option by typing the capitalized letter in  the  option's
            name on the keyboard, such as a to activate the Align option.
     If  more  partitions  exist  than  can be displayed in one screen, you can
     scroll between screens using the partition selection keys, much  as  in  a
     text editor.
     Available  options  are  as  described below. (Note that cgdisk provides a
     much more limited set of options than its sibling gdisk. If  you  need  to
     perform  partition  table  recovery, hybrid MBR modification, or other ad-
     vanced operations, you should consult the gdisk documentation.)
     Align  Change the sector alignment value. Disks with more logical  sectors
            than physical sectors (such as modern Advanced Format drives), some
            RAID  configurations,  and many SSD devices, can suffer performance
            problems if partitions are not aligned properly for their  internal
            data  structures.  On new disks, GPT fdisk attempts to align parti-
            tions on 1 MiB boundaries (2048-sectors on disks with 512-byte sec-
            tors) by default, which optimizes performance for all of these disk
            types. On pre-partitioned disks, GPT fdisk attempts to identify the
            alignment value used on that disk, but will set 8-sector  alignment
            on disks larger than 300 GB even if lesser alignment values are de-
            tected.  In  either  case,  it can be changed by using this option.
            The alignment value also affects the default end sector value  when
            creating  a  new  partition;  it will be aligned to one less than a
            multiple of the alignment value, when possible.  This  should  keep
            partitions a multiple of the alignment value in size. Some disk en-
            cryption  tools require partitions to be sized to some value, typi-
            cally 4096 bytes, so the default alignment of 1 MiB works well  for
            them.
     Backup
            Save  partition data to a backup file. You can back up your current
            in-memory partition table to a disk file using this option. The re-
            sulting file is a binary file consisting of the protective MBR, the
            main GPT header, the backup GPT header, and one copy of the  parti-
            tion  table,  in that order. Note that the backup is of the current
            in-memory data structures, so  if  you  launch  the  program,  make
            changes,  and  then  use  this option, the backup will reflect your
            changes.
     Delete
            Delete a partition. This action deletes the entry from  the  parti-
            tion  table but does not disturb the data within the sectors origi-
            nally allocated to the partition on the disk.  If  a  corresponding
            hybrid MBR partition exists, gdisk deletes it, as well, and expands
            any  adjacent  0xEE  (EFI GPT) MBR protective partition to fill the
            new free space.
     Help   Print brief descriptions of all the options.
     Info   Show detailed partition information. The summary information  shown
            in  the partition display area necessarily omits many details, such
            as the partitions' unique GUIDs and  the  partitions'  sector-exact
            start and end points. The Info option displays this information for
            a single partition.
     Load   Load  partition data from a backup file. This option is the reverse
            of the Backup option. Note that restoring partition data from  any-
            thing but the original disk is not recommended.
     naMe   Change  the  GPT  name  of  a  partition. This name is encoded as a
            UTF-16 string, but proper entry and display of anything beyond  ba-
            sic ASCII values requires suitable locale and font support. For the
            most  part,  Linux ignores the partition name, but it may be impor-
            tant in some OSes. GPT fdisk sets a default name based on the  par-
            tition  type  code.  Note  that the GPT partition name is different
            from the filesystem name, which is encoded in the filesystem's data
            structures. Note also that to activate this item by typing its  al-
            phabetic  equivalent,  you  must use M, not the more obvious N, be-
            cause the latter is used by the next option....
     New    Create a new partition. You enter a starting sector, a size, a type
            code, and a name. The start sector can  be  specified  in  absolute
            terms  as  a  sector  number or as a position measured in kibibytes
            (K), mebibytes (M), gibibytes (G), tebibytes (T), or pebibytes (P);
            for instance, 40M specifies a position 40MiB from the start of  the
            disk. You can specify locations relative to the start or end of the
            specified default range by preceding the number by a '+' symbol, as
            in  +2G to specify a point 2GiB after the default start sector. The
            size value can use the K, M, G, T, and P  suffixes,  too.  Pressing
            the  Enter  key with no input specifies the default value, which is
            the start of the largest available block for the start  sector  and
            the full available size for the size.
     Quit   Quit from the program without saving your changes.  Use this option
            if you just wanted to view information or if you make a mistake and
            want to back out of all your changes.
     Type   Change  a single partition's type code. You enter the type code us-
            ing a two-byte hexadecimal number. You may also enter  a  GUID  di-
            rectly,  if  you  have one and cgdisk doesn't know it. If you don't
            know the type code for your partition, you can type L to see a list
            of known type codes.  The type code list may optionally be filtered
            by a search string; for instance, entering linux shows only  parti-
            tion  type  codes  with descriptions that include the string Linux.
            This search is performed case-insensitively.
     Verify
            Verify disk. This option checks for a variety of problems, such  as
            incorrect  CRCs  and  mismatched  main and backup data. This option
            does not automatically correct most problems, though; for that, you
            must use gdisk. If no problems are found, this command  displays  a
            summary of unallocated disk space.
     Write  Write data. Use this command to save your changes.
BUGS
     Known bugs and limitations include:
     *      The  program  compiles correctly only on Linux, FreeBSD, and Mac OS
            X. In theory, it should compile under Windows if  the  Ncurses  li-
            brary for Windows is installed, but I have not tested this capabil-
            ity.  Linux versions for x86-64 (64-bit), x86 (32-bit), and PowerPC
            (32-bit) have been tested, with the x86-64 version having seen  the
            most  testing. Under FreeBSD, 32-bit (x86) and 64-bit (x86-64) ver-
            sions have been tested. Only 32-bit versions for Mac OS X has  been
            tested by the author.
     *      The  FreeBSD version of the program can't write changes to the par-
            tition table to a disk when existing partitions on  that  disk  are
            mounted.  (The  same  problem exists with many other FreeBSD utili-
            ties, such as gpt, fdisk, and dd.) This limitation can be  overcome
            by typing sysctl kern.geom.debugflags=16 at a shell prompt.
     *      The  program  can  load only up to 128 partitions (4 primary parti-
            tions and 124 logical partitions) when converting from MBR  format.
            This limit can be raised by changing the #define MAX_MBR_PARTS line
            in the basicmbr.h source code file and recompiling; however, such a
            change  will  require  using  a larger-than-normal partition table.
            (The limit of 128 partitions was chosen because that number  equals
```

### `man fixparts`

> 官方示例调用：`man fixparts`

```text
root@kali:~# man fixparts
FIXPARTS(8)                     FixParts Manual                     FIXPARTS(8)
NAME
     fixparts - MBR partition table repair utility
SYNOPSIS
     fixparts device
DESCRIPTION
     FixParts  (aka  fixparts) is a text-mode menu-driven program for repairing
     certain types of problems with Master Boot Record (MBR) partition  tables.
     The program has three design goals, although a few additional features are
     supported, as well:
     *      It  can  remove stray GUID Partition Table (GPT) data, which can be
            left behind on a disk that was once used as a GPT disk but then in-
            completely converted to the more common (as of 2011) MBR form.
     *      It can repair mis-sized extended partitions  --  either  partitions
            that  extend  beyond  the  physical end of the disk or that overlap
            with nearby primary partitions. FixParts is designed in such a  way
            that  this type of repair occurs automatically, so if it's the only
            problem with your disk, you can launch the program and then immedi-
            ately save the partition table, making no manual changes,  and  the
            program will fix the problem.
     *      You  can  change  primary  partitions  into  logical  partitions or
            vice-versa, within constraints imposed by the MBR data structures.
     Additional features include the ability to change partition type codes  or
     boot/active flags, to delete partitions, and to recompute CHS values. With
     the possible exception of recomputing CHS values, these secondary features
     are  better performed with fdisk, because fixparts' design means that it's
     likely to alter partition numbering even when such  changes  are  not  re-
     quested.
     The  fixparts  program employs a user interface similar to that of Linux's
     fdisk, but fixparts is much more specialized. Most importantly, you  can't
     create new partitions with fixparts, although you can change primary/logi-
     cal assignment.
     In the MBR scheme, partitions come in three varieties:
     primary
            These  partitions  are defined in the first sector of the hard disk
            and are limited in number to four. Some OSes, such as  Windows  and
            FreeBSD, must boot from a primary partition.
     extended
            Extended  partitions are specialized primary partitions. They serve
            as holding areas for logical partitions.
     logical
            A disk can contain an arbitrary number of logical partitions  (fix-
            parts, however, imposes a limit of 124 logical partitions). All the
            logical  partitions  reside inside a single extended partition, and
            are defined using a linked-list data  structure.  This  fact  means
            that  every logical partition must be preceded by at least one sec-
            tor of unallocated space to hold its defining  data  structure  (an
            Extended Boot Record, or EBR).
     These  distinctions mean that primary and logical partitions cannot be ar-
     bitrarily interspersed. A disk can contain one  to  three  primary  parti-
     tions,  a  block  of one or more logical partitions, and one to three more
     primary partitions (for a total of three primary partitions, not  counting
     the  extended partition). Primary partitions may not be sandwiched between
     logical partitions, since this would  mean  placing  a  primary  partition
     within  an  extended  partition  (which is just a specific type of primary
     partition).
     Unlike most disk utilities, fixparts' user interface ignores extended par-
     titions. Internally, the program discards the information on the  original
     extended partition and, when you tell it to save its changes, it generates
     a  new  extended partition to contain the then-defined logical partitions.
     This is done because most of the repairs and manipulations the  tool  per-
     forms require generating a fresh extended partition, so keeping the origi-
     nal in the user interface would only be a complication.
     Another unusual feature of fixparts' user interface is that partition num-
     bers  do  not  necessarily  correlate with primary/logical status. In most
     utilities, partitions 1-4 correspond to primary partitions, whereas parti-
     tions 5 and up are logical partitions. In fixparts, any  partition  number
     may be assigned primary or logical status, so long as the rules for layout
     described  earlier  are  obeyed. When the partition table is saved, parti-
     tions will be assigned appropriately and then tools such as the Linux ker-
     nel and fdisk will give them conventional numbers.
     When it first starts, fixparts performs a scan for GPT data. If  the  disk
     looks  like  a conventional GPT disk, fixparts refuses to run. If the disk
     appears to be a conventional MBR disk but GPT signatures  are  present  in
     the  GPT primary or secondary header areas, fixparts offers to delete this
     extraneous data. If you tell it to do so, the  program  immediately  wipes
     the  GPT  header  or headers. (If only one header was found, only that one
     header will be erased, to minimize the risk of damaging a boot  loader  or
     other data that might have overwritten just one of the GPT headers.)
     With  the  exception of optionally erasing leftover GPT data when it first
     starts, fixparts keeps all changes in memory until the user writes changes
     with the w command. Thus, you can adjust your partitions in the  user  in-
     terface  and  abort  those  changes  by  typing  q  to quit without saving
     changes.
OPTIONS
     The fixparts utility supports no command-line options, except for specifi-
     cation of the target device.
     Most interactions with fixparts occur with its interactive text-mode menu.
     Specific functions are:
     a      Toggle the active/boot flag. This flag is  required  by  some  boot
            loaders and OSes.
     c      Recompute the cylinder/head/sector (CHS) values for all partitions.
            CHS  addressing  mode is largely obsolete, but some OSes and utili-
            ties complain if they don't like the CHS  values.  Note  that  fix-
            parts'  CHS values are likely to be incorrect on disks smaller than
            about 8 GiB except on Linux.
     l      Change a partition's status to logical. This option will only  work
            if  the  current partition layout supports such a change. Note that
            if changing a partition's status in this way is not currently  pos-
            sible, making some other change may make it possible. For instance,
            omitting  a partition that precedes the target partition may enable
            converting a partition to logical form if there had  been  no  free
            sectors between the two partitions.
     o      Omit  a partition. Once omitted, the partition will still appear in
            the fixparts partition list, but it will be flagged as omitted. You
            can subsequently convert it to primary or logical form with  the  r
            or  l  commands,  respectively.  When you save your changes with w,
            though, the partition will be lost.
     p      Display basic partition summary  data.  This  includes  partition's
            number,  the  boot/active flag's status, starting and ending sector
            numbers, primary/logical/omitted status, whether or not the  parti-
            tion  may  be  converted  to  logical form, and the partition's MBR
            types code.
     q      Quit from the program without saving your changes.  Use this option
            if you just wanted to view information or if you make a mistake and
            want to back out of all your changes.
     r      Change a partition's status to primary. This option will only  work
            if  the  current partition layout supports such a change. Note that
            every partition can theoretically become a primary  partition,  al-
            though  in  some  configurations,  making  this change will require
            omitting some partitions.  If fixparts refuses to allow changing  a
            partition  to  primary, you may need to convert other partitions to
            logical form or omit them entirely.
     s      Sort partition entries. This option orders partitions in  the  dis-
            play to match their on-disk positions, which can make understanding
            the  disk layout easier in some cases. This option has no effect on
            the ultimate ordering of logical partitions, which are  sorted  be-
            fore  being  saved.  The  order  of primary partitions in the final
            saved partition table may be  affected  by  this  option.  In  both
            cases,  as  already  noted, the partition numbers displayed by fix-
            parts may not be the same as those used by the kernel or  displayed
            by other partitioning tools.
     t      Change  a  partition's  type  code. You enter the type code using a
            one-byte hexadecimal number.
     w      Write data. Use this command to save your changes and exit from the
            program.
     ?      Print the menu. Type this command (or any other  unrecognized  com-
            mand) to see a summary of available options.
BUGS
     Known bugs and limitations include:
     *      The  program  compiles  correctly only on Linux, FreeBSD, Mac OS X,
            and Windows.  Linux versions for x86-64 (64-bit), x86 (32-bit), and
            PowerPC (32-bit) have been tested, with the x86-64  version  having
            seen  the  most  testing.  Under  FreeBSD,  32-bit (x86) and 64-bit
            (x86-64) versions have been tested. Only 32-bit versions for Mac OS
            X and Windows have been tested.
     *      The FreeBSD version of the program can't write changes to the  par-
            tition  table  to  a disk when existing partitions on that disk are
            mounted. (The same problem exists with many  other  FreeBSD  utili-
            ties,  such as gpt, fdisk, and dd.) This limitation can be overcome
            by typing sysctl kern.geom.debugflags=16 at a shell prompt.
     *      The program can load only up to 128 partitions  (4  primary  parti-
            tions  and  124  logical  partitions).  This limit can be raised by
            changing the #define MAX_MBR_PARTS line in  the  basicmbr.h  source
            code file and recompiling.
     *      The  program  can  read partitions only if the disk has correct LBA
            partition descriptors. These descriptors should be present  on  any
            disk  over  8  GiB in size or on smaller disks partitioned with any
            but very ancient software.
     *      The program makes no effort to preserve partition numbers. This can
            have consequences for boot loaders and for mounting filesystems via
            /etc/fstab. It may be necessary to edit configuration files or even
            to re-install your boot loader.
     *
            The program may change the order of partitions in the partition ta-
            ble.
AUTHORS
     Primary author: Roderick W. Smith (
[email protected]
)
     Contributors:
     * Yves Blusseau (
[email protected]
)
     * David Hubbard (
[email protected]
)
     * Justin Maggard (
[email protected]
)
     * Dwight Schauer (
[email protected]
)
     * Florian Zumbiehl (
[email protected]
)
SEE ALSO
     cfdisk(8), cgdisk(8), fdisk(8), mkfs(8), parted(8),  sfdisk(8),  gdisk(8),
     sgdisk(8).
     https://en.wikipedia.org/wiki/Master_boot_record
     https://www.rodsbooks.com/fixparts/
AVAILABILITY
     The  fixparts  command  is  part of the GPT fdisk package and is available
     from Rod Smith.
Roderick W. Smith                    1.0.10                         FIXPARTS(8)
```

### `gdisk`

> 官方示例调用：`gdisk -h`

```text
root@kali:~# gdisk -h
GPT fdisk (gdisk) version 1.0.10
```

### `sgdisk`

> 官方示例调用：`sgdisk --help`

```text
root@kali:~# sgdisk --help
Usage: sgdisk  [OPTION...] <device>
  -A, --attributes=list|[partnum:show|or|nand|xor|=|set|clear|toggle|get[:bitnum|hexbitmask]]     operate on partition attributes
  -a, --set-alignment=value                                                                       set sector alignment
  -b, --backup=file                                                                               backup GPT to file
  -B, --byte-swap-name=partnum                                                                    byte-swap partition's name
  -c, --change-name=partnum:name                                                                  change partition's name
  -C, --recompute-chs                                                                             recompute CHS values in protective/hybrid MBR
  -d, --delete=partnum                                                                            delete a partition
  -D, --display-alignment                                                                         show number of sectors per allocation block
  -e, --move-second-header                                                                        move second/backup header to end of disk
  -E, --end-of-largest                                                                            show end of largest free block
  -f, --first-in-largest                                                                          show start of the largest free block
  -F, --first-aligned-in-largest                                                                  show start of the largest free block, aligned
  -g, --mbrtogpt                                                                                  convert MBR to GPT
  -G, --randomize-guids                                                                           randomize disk and partition GUIDs
  -h, --hybrid=partnum[:partnum...][:EE]                                                          create hybrid MBR
  -i, --info=partnum                                                                              show detailed information on partition
  -I, --align-end                                                                                 align partition end points
  -j, --move-main-table=sector                                                                    change the start sector of the main partition table
  -k, --move-backup-table=sector                                                                  change the start sector of the second/backup partition table
  -l, --load-backup=file                                                                          load GPT backup from file
  -L, --list-types                                                                                list known partition types
  -m, --gpttombr=partnum[:partnum...]                                                             convert GPT to MBR
  -n, --new=partnum:start:end                                                                     create new partition
  -N, --largest-new=partnum                                                                       create largest possible new partition
  -o, --clear                                                                                     clear partition table
  -O, --print-mbr                                                                                 print MBR partition table
  -p, --print                                                                                     print partition table
  -P, --pretend                                                                                   make changes in memory, but don't write them
  -r, --transpose=partnum:partnum                                                                 transpose two partitions
  -R, --replicate=device_filename                                                                 replicate partition table
  -s, --sort                                                                                      sort partition table entries
  -S, --resize-table=numparts                                                                     resize partition table
  -t, --typecode=partnum:{hexcode|GUID}                                                           change partition type code
  -T, --transform-bsd=partnum                                                                     transform BSD disklabel partition to GPT
  -u, --partition-guid=partnum:guid                                                               set partition GUID
  -U, --disk-guid=guid                                                                            set disk GUID
  -v, --verify                                                                                    check partition table integrity
  -V, --version                                                                                   display version information
  -z, --zap                                                                                       zap (destroy) GPT (but not MBR) data structures
  -Z, --zap-all                                                                                   zap (destroy) GPT and MBR data structures
Help options:
  -?, --help                                                                                      Show this help message
      --usage                                                                                     Display brief usage message
Updated on: 2026-May-25
 Edit this page
fwbuilder
git
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install gdisk`，再执行 `gdisk --version` 2>/dev/null || `gdisk -V`
- [ ] **2.** **读官方帮助** —— `gdisk -h`，需要细节时 `man gdisk`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sgdisk  [OPTION...] <device>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gdisk/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gdisk/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gdisk/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
