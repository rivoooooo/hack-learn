# lvm2

> Linux Logical Volume Manager This is LVM2, the rewrite of The Linux Logical Volume Manager. LVM supports enterprise level volume management of disk and disk subsystems by grouping arbitrary disks into volume groups. The total capacity of v…

> **功能分类**：数字取证 ｜ **Kali 包**：`lvm2` ｜ **官方文档**：<https://www.kali.org/tools/lvm2/>

## 1. 安装

```bash
sudo apt update
sudo apt install lvm2
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.03.31 |
| 架构 | linux-any |
| 可执行命令 | `dmeventd`、`dmsetup`、`blkdeactivate`、`dmstats`、`dmsetup-udeb`、`libdevmapper-dev`、`libdevmapper-event1.02.1`、`libdevmapper1.02.1`、`libdevmapper1.02.1-udeb`、`liblvm2-dev`、`liblvm2cmd2.03`、`lvm2`、`fsadm`、`lvchange`、`lvconvert`、`lvcreate`、`lvdisplay`、`lvextend`、`lvm`、`lvmconfig`、`lvmdiskscan`、`lvmdump`、`lvmpolld`、`lvmsadc`、`lvmsar`、`lvreduce`、`lvremove`、`lvrename`、`lvresize`、`lvs`、`lvscan`、`pvchange`、`pvck`、`pvcreate`、`pvdisplay`、`pvmove`、`pvremove`、`pvresize`、`pvs`、`pvscan`、`vgcfgbackup`、`vgcfgrestore`、`vgchange`、`vgck`、`vgconvert`、`vgcreate`、`vgdisplay`、`vgexport`、`vgextend`、`vgimport`、`vgimportclone`、`vgmerge`、`vgmknodes`、`vgreduce`、`vgremove`、`vgrename`、`vgs`、`vgscan`、`vgsplit`、`lvm2-dbusd`、`lvmdbusd`、`lvm2-lockd`、`lvmlockctl`、`lvmlockd`、`lvm2-udeb` |
| 依赖 | `dmeventd`、`dmsetup`、`libaio1t64`、`libblkid1`、`libc6`、`libdevmapper-event1.02.1`、`libedit2`、`libselinux1`、`libsystemd0`、`libudev1`、`fsadm` |
| 安装体积 | 3.96 MB |
| 官网 | <https://sourceware.org/lvm2/> |
| 源码仓库 | <https://salsa.debian.org/lvm-team/lvm2> |
| 包追踪 | <https://pkg.kali.org/pkg/lvm2> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
dmeventd -h          # 查看用法
man dmeventd         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 65 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dmeventd`

> 官方示例调用：`dmeventd -h`

```text
root@kali:~# dmeventd -h
Usage:
dmeventd [-d [-d [-d]]] [-e path] [-f] [-h] [i] [-l] [-R] [-V] [-?]
   -d       Log debug messages to syslog (-d, -dd, -ddd)
   -e       Select a file path checked on exit
   -f       Don't fork, run in the foreground
   -h       Show this help information
   -i       Query running instance of dmeventd for info
   -l       Log to stdout,stderr instead of syslog
   -?       Show this help information on stderr
   -R       Restart dmeventd
   -V       Show version of dmeventd
```

### `blkdeactivate`

> 官方示例调用：`blkdeactivate -h`

```text
root@kali:~# blkdeactivate -h
blkdeactivate: Utility to deactivate block devices
  blkdeactivate [options] [device...]
    - Deactivate block device tree.
      If devices are specified, deactivate only supplied devices and their holders.
  Options:
    -e | --errors                       Show errors reported from tools
    -h | --help                         Show this help message
    -d | --dmoptions     DM_OPTIONS     Comma separated DM specific options
    -l | --lvmoptions    LVM_OPTIONS    Comma separated LVM specific options
    -m | --mpathoptions  MPATH_OPTIONS  Comma separated DM-multipath specific options
    -r | --mdraidoptions MDRAID_OPTIONS Comma separated MD RAID specific options
    -o | --vdooptions    VDO_OPTIONS    Comma separated VDO specific options
    -u | --umount                       Unmount the device if mounted
    -v | --verbose                      Verbose mode (also implies -e)
  Device specific options:
    DM_OPTIONS:
      retry           retry removal several times in case of failure
      force           force device removal
    LVM_OPTIONS:
      retry           retry removal several times in case of failure
      wholevg         deactivate the whole VG when processing an LV
    MDRAID_OPTIONS:
      wait            wait for resync, recovery or reshape to complete first
    MPATH_OPTIONS:
      disablequeueing disable queueing on all DM-multipath devices first
    VDO_OPTIONS:
      configfile=file use specified VDO configuration file
```

### `dmsetup`

> 官方示例调用：`dmsetup -h`

```text
root@kali:~# dmsetup -h
Usage:
```

### `dmstats`

> 官方示例调用：`dmstats -h`

```text
root@kali:~# dmstats -h
Usage:
```

### `fsadm`

> 官方示例调用：`fsadm -h`

```text
root@kali:~# fsadm -h
fsadm: Utility to resize or check the filesystem on a device
  fsadm [options] check <device>
    - Check the filesystem on device using fsck
  fsadm [options] resize <device> [<new_size>[BKMGTPE]]
    - Change the size of the filesystem on device to new_size
  Options:
    -h | --help         Show this help message
    -v | --verbose      Be verbose
    -e | --ext-offline  unmount filesystem before ext2/ext3/ext4 resize
    -f | --force        Bypass sanity checks
    -n | --dry-run      Print commands without running them
    -l | --lvresize     Resize given device (if it is LVM device)
    -c | --cryptresize  Resize given crypt device
    -y | --yes          Answer "yes" at any prompts
  new_size - Absolute number of filesystem blocks to be in the filesystem,
             or an absolute size using a suffix (in powers of 1024).
             If new_size is not supplied, the whole device is used.
```

### `lvchange`

> 官方示例调用：`lvchange -h`

```text
root@kali:~# lvchange -h
  lvchange - Change the attributes of logical volume(s)
  Change a general LV attribute.
  For options listed in parentheses, any one is
  required, after which the others are optional.
  lvchange
	( -C|--contiguous y|n,
	  -p|--permission rw|r,
	  -r|--readahead auto|none|Number,
	  -k|--setactivationskip y|n,
	  -Z|--zero y|n,
	  -M|--persistent n,
	     --addtag Tag,
	     --deltag Tag,
	     --alloc contiguous|cling|cling_by_tags|normal|anywhere|inherit,
	     --compression y|n,
	     --deduplication y|n,
	     --detachprofile,
	     --metadataprofile String,
	     --profile String,
	     --setautoactivation y|n,
	     --errorwhenfull y|n,
	     --discards passdown|nopassdown|ignore,
	     --cachemode writethrough|writeback|passthrough,
	     --cachepolicy String,
	     --cachesettings String,
	     --minrecoveryrate Size[k|UNIT],
	     --maxrecoveryrate Size[k|UNIT],
	     --vdosettings String,
	     --integritysettings String,
	     --writebehind Number,
	     --writemostly PV[:t|n|y] )
	 VG|LV|Tag|Select ...
	[ -a|--activate y|n|ay ]
	[    --poll y|n ]
	[    --monitor y|n ]
	[ COMMON_OPTIONS ]
  Resynchronize a mirror or raid LV.
  Use to reset 'R' attribute on a not initially synchronized LV.
  lvchange --resync VG|LV|Tag|Select ...
	[ -a|--activate y|n|ay ]
	[ COMMON_OPTIONS ]
  Resynchronize or check a raid LV.
  lvchange --syncaction check|repair VG|LV|Tag|Select ...
	[ COMMON_OPTIONS ]
  Reconstruct data on specific PVs of a raid LV.
  lvchange --rebuild PV VG|LV|Tag|Select ...
	[ COMMON_OPTIONS ]
  Activate or deactivate an LV.
  lvchange -a|--activate y|n|ay VG|LV|Tag|Select ...
	[ -P|--partial ]
	[ -K|--ignoreactivationskip ]
	[    --activationmode partial|degraded|complete ]
	[    --poll y|n ]
	[    --monitor y|n ]
	[    --ignorelockingfailure ]
	[    --sysinit ]
	[    --readonly ]
	[ COMMON_OPTIONS ]
  Reactivate an LV using the latest metadata.
  lvchange --refresh VG|LV|Tag|Select ...
	[ -P|--partial ]
	[    --activationmode partial|degraded|complete ]
	[    --poll y|n ]
	[    --monitor y|n ]
	[ COMMON_OPTIONS ]
  Start or stop monitoring an LV from dmeventd.
  lvchange --monitor y|n VG|LV|Tag|Select ...
	[ COMMON_OPTIONS ]
  Start or stop processing an LV conversion.
  lvchange --poll y|n VG|LV|Tag|Select ...
	[    --monitor y|n ]
	[ COMMON_OPTIONS ]
  Make the minor device number persistent for an LV.
  lvchange -M|--persistent y --minor Number LV
	[ -j|--major Number ]
	[ -a|--activate y|n|ay ]
	[    --poll y|n ]
	[    --monitor y|n ]
	[ COMMON_OPTIONS ]
  Common options for command:
	[ -A|--autobackup y|n ]
	[ -f|--force ]
	[ -S|--select String ]
	[    --ignoremonitoring ]
	[    --noudevsync ]
	[    --reportformat basic|json|json_std ]
  Common options for lvm:
	[ -d|--debug ]
	[ -h|--help ]
	[ -q|--quiet ]
	[ -v|--verbose ]
	[ -y|--yes ]
	[ -t|--test ]
	[    --commandprofile String ]
	[    --config String ]
	[    --driverloaded y|n ]
	[    --nolocking ]
	[    --lockopt String ]
	[    --longhelp ]
	[    --profile String ]
	[    --version ]
	[    --devicesfile String ]
	[    --devices PV ]
	[    --nohints ]
	[    --journal String ]
  Use --longhelp to show all options and advanced commands.
```

### `lvconvert`

> 官方示例调用：`lvconvert -h`

```text
root@kali:~# lvconvert -h
  lvconvert - Change logical volume layout
  Convert LV to linear.
  lvconvert --type linear LV
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Convert LV to striped.
  lvconvert --type striped LV
	[ -I|--stripesize Size[k|UNIT] ]
	[ -R|--regionsize Size[m|UNIT] ]
	[ -i|--interval Number ]
	[    --stripes Number ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Convert LV to type mirror (also see type raid1),
  lvconvert --type mirror LV
	[ -m|--mirrors [+|-]Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ -R|--regionsize Size[m|UNIT] ]
	[ -i|--interval Number ]
	[    --stripes Number ]
	[    --mirrorlog core|disk ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Convert LV to raid or change raid layout
  (a specific raid level must be used, e.g. raid1).
  lvconvert --type raid LV
	[ -m|--mirrors [+|-]Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ -R|--regionsize Size[m|UNIT] ]
	[ -i|--interval Number ]
	[    --stripes Number ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Convert LV to raid1 or mirror, or change number of mirror images.
  lvconvert -m|--mirrors [+|-]Number LV
	[ -R|--regionsize Size[m|UNIT] ]
	[ -i|--interval Number ]
	[    --mirrorlog core|disk ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Convert raid LV to change number of stripe images.
  lvconvert --stripes Number LV
	[ -i|--interval Number ]
	[ -R|--regionsize Size[m|UNIT] ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Convert raid LV to change the stripe size.
  lvconvert -I|--stripesize Size[k|UNIT] LV
	[ -i|--interval Number ]
	[ -R|--regionsize Size[m|UNIT] ]
	[ COMMON_OPTIONS ]
  Split images from a raid1 or mirror LV and use them to create a new LV.
  lvconvert --splitmirrors Number -n|--name LV_new LV
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Split images from a raid1 LV and track changes to origin for later merge.
  lvconvert --splitmirrors Number --trackchanges LV
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Merge LV images that were split from a raid1 LV.
  lvconvert --mergemirrors VG|LV|Tag ...
	[ COMMON_OPTIONS ]
  Convert LV to a thin LV, using the original LV as an external origin.
  lvconvert --type thin --thinpool LV LV
	[ -T|--thin ]
	[ -c|--chunksize Size[k|UNIT] ]
	[ -r|--readahead auto|none|Number ]
	[ -W|--wipesignatures y|n ]
	[ -Z|--zero y|n ]
	[    --originname LV_new ]
	[    --poolmetadata LV ]
	[    --poolmetadatasize Size[m|UNIT] ]
	[    --poolmetadataspare y|n ]
	[    --metadataprofile String ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Convert LV to a thin LV, using LV as thin-pool data volume.
  lvconvert --type thin LV
	[ -T|--thin ]
	[ -c|--chunksize Size[k|UNIT] ]
	[ -r|--readahead auto|none|Number ]
	[ -W|--wipesignatures y|n ]
	[ -Z|--zero y|n ]
	[    --poolmetadata LV ]
	[    --poolmetadatasize Size[m|UNIT] ]
	[    --poolmetadataspare y|n ]
	[    --metadataprofile String ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Attach a cache pool to an LV, converts the LV to type cache.
  lvconvert --type cache --cachepool LV LV
	[ -H|--cache ]
	[ -Z|--zero y|n ]
	[ -c|--chunksize Size[k|UNIT] ]
	[ -r|--readahead auto|none|Number ]
	[ -W|--wipesignatures y|n ]
	[    --cachemetadataformat auto|1|2 ]
	[    --cachemode writethrough|writeback|passthrough ]
	[    --cachepolicy String ]
	[    --cachesettings String ]
	[    --poolmetadata LV ]
	[    --poolmetadatasize Size[m|UNIT] ]
	[    --poolmetadataspare y|n ]
	[    --metadataprofile String ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Attach a writecache to an LV, converts the LV to type writecache.
  lvconvert --type writecache --cachevol LV LV
	[    --cachesettings String ]
	[ COMMON_OPTIONS ]
  Attach a cache to an LV, converts the LV to type cache.
  lvconvert --type cache --cachevol LV LV
	[ -H|--cache ]
	[ -Z|--zero y|n ]
	[ -c|--chunksize Size[k|UNIT] ]
	[    --cachemetadataformat auto|1|2 ]
	[    --cachemode writethrough|writeback|passthrough ]
	[    --cachepolicy String ]
	[    --cachesettings String ]
	[    --poolmetadatasize Size[m|UNIT] ]
	[ COMMON_OPTIONS ]
  Add a writecache to an LV, using a specified cache device.
  lvconvert --type writecache --cachedevice PV LV
	[    --cachesize Size[m|UNIT] ]
	[    --cachesettings String ]
	[ COMMON_OPTIONS ]
  Add a cache to an LV, using a specified cache device.
  lvconvert --type cache --cachedevice PV LV
	[ -c|--chunksize Size[k|UNIT] ]
	[    --cachesize Size[m|UNIT] ]
	[    --cachesettings String ]
	[ COMMON_OPTIONS ]
  Convert LV to type thin-pool.
  lvconvert --type thin-pool LV
	[ -I|--stripesize Size[k|UNIT] ]
	[ -c|--chunksize Size[k|UNIT] ]
	[ -r|--readahead auto|none|Number ]
	[ -W|--wipesignatures y|n ]
	[ -Z|--zero y|n ]
	[    --stripes Number ]
	[    --discards passdown|nopassdown|ignore ]
	[    --errorwhenfull y|n ]
	[    --pooldatavdo y|n ]
	[    --compression y|n ]
	[    --deduplication y|n ]
	[    --vdosettings String ]
	[    --poolmetadata LV ]
	[    --poolmetadatasize Size[m|UNIT] ]
	[    --poolmetadataspare y|n ]
	[    --metadataprofile String ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Convert LV to type cache-pool.
  lvconvert --type cache-pool LV
	[ -Z|--zero y|n ]
	[ -c|--chunksize Size[k|UNIT] ]
	[ -r|--readahead auto|none|Number ]
	[ -W|--wipesignatures y|n ]
	[    --cachemetadataformat auto|1|2 ]
	[    --cachemode writethrough|writeback|passthrough ]
	[    --cachepolicy String ]
	[    --cachesettings String ]
	[    --poolmetadata LV ]
	[    --poolmetadatasize Size[m|UNIT] ]
	[    --poolmetadataspare y|n ]
	[    --metadataprofile String ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Convert LV to type vdopool.
  lvconvert --type vdo-pool LV
	[ -n|--name LV_new ]
	[ -V|--virtualsize Size[m|UNIT] ]
	[ -r|--readahead auto|none|Number ]
	[ -W|--wipesignatures y|n ]
	[ -Z|--zero y|n ]
	[    --compression y|n ]
	[    --deduplication y|n ]
	[    --vdosettings String ]
	[    --metadataprofile String ]
	[ COMMON_OPTIONS ]
  Detach a cache from an LV.
  lvconvert --splitcache LV
	[    --cachesettings String ]
	[ COMMON_OPTIONS ]
  Merge thin LV into its origin LV.
  lvconvert --mergethin LV ...
	[ COMMON_OPTIONS ]
  Merge COW snapshot LV into its origin.
  lvconvert --mergesnapshot LV ...
	[ -i|--interval Number ]
	[ COMMON_OPTIONS ]
  Combine a former COW snapshot (second arg) with a former
  origin LV (first arg) to reverse a splitsnapshot command.
  lvconvert --type snapshot LV LV
	[ -s|--snapshot ]
	[ -c|--chunksize Size[k|UNIT] ]
	[ -Z|--zero y|n ]
	[ COMMON_OPTIONS ]
  Replace failed PVs in a raid or mirror LV.
  Repair a thin pool.
  Repair a cache pool.
  lvconvert --repair LV
	[ -i|--interval Number ]
	[ -k|--setactivationskip y|n ]
	[    --usepolicies ]
	[    --poolmetadataspare y|n ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Replace specific PV(s) in a raid LV with another PV.
  lvconvert --replace PV LV
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Poll LV to continue conversion.
  lvconvert --startpoll LV
	[ COMMON_OPTIONS ]
  Add or remove data integrity checksums to raid images.
  lvconvert --raidintegrity y|n LV
	[    --raidintegritymode String ]
```

### `lvcreate`

> 官方示例调用：`lvcreate -h`

```text
root@kali:~# lvcreate -h
  lvcreate - Create a logical volume
  Create a linear LV.
  lvcreate -L|--size Size[m|UNIT] VG
	[ --type linear ] (implied)
	[ -l|--extents Number[PERCENT] ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Create a striped LV.
  lvcreate -i|--stripes Number -L|--size Size[m|UNIT] VG
	[ --type striped ] (implied)
	[ -l|--extents Number[PERCENT] ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Create a raid1 or mirror LV.
  lvcreate -m|--mirrors Number -L|--size Size[m|UNIT] VG
	[ --type raid1|mirror ] (implied)
	[ -l|--extents Number[PERCENT] ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ -R|--regionsize Size[m|UNIT] ]
	[    --mirrorlog core|disk ]
	[    --minrecoveryrate Size[k|UNIT] ]
	[    --maxrecoveryrate Size[k|UNIT] ]
	[    --raidintegrity y|n ]
	[    --raidintegritymode String ]
	[    --raidintegrityblocksize Number ]
	[    --integritysettings String ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Create a raid LV (a specific raid level must be used, e.g. raid1).
  lvcreate --type raid -L|--size Size[m|UNIT] VG
	[ -l|--extents Number[PERCENT] ]
	[ -m|--mirrors Number ]
	[ -i|--stripes Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ -R|--regionsize Size[m|UNIT] ]
	[    --minrecoveryrate Size[k|UNIT] ]
	[    --maxrecoveryrate Size[k|UNIT] ]
	[    --raidintegrity y|n ]
	[    --raidintegritymode String ]
	[    --raidintegrityblocksize Number ]
	[    --integritysettings String ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Create a raid10 LV.
  lvcreate -m|--mirrors Number -i|--stripes Number -L|--size Size[m|UNIT] VG
	[ --type raid10 ] (implied)
	[ -l|--extents Number[PERCENT] ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ -R|--regionsize Size[m|UNIT] ]
	[    --minrecoveryrate Size[k|UNIT] ]
	[    --maxrecoveryrate Size[k|UNIT] ]
	[    --raidintegrity y|n ]
	[    --raidintegritymode String ]
	[    --raidintegrityblocksize Number ]
	[    --integritysettings String ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Create a COW snapshot LV of an origin LV.
  lvcreate -s|--snapshot -L|--size Size[m|UNIT] LV
	[ --type snapshot ] (implied)
	[ -l|--extents Number[PERCENT] ]
	[ -i|--stripes Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ -c|--chunksize Size[k|UNIT] ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Create a thin pool.
  lvcreate --type thin-pool -L|--size Size[m|UNIT] VG
	[ -l|--extents Number[PERCENT] ]
	[ -i|--stripes Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ -T|--thin ]
	[ -c|--chunksize Size[k|UNIT] ]
	[    --thinpool LV_new ]
	[    --discards passdown|nopassdown|ignore ]
	[    --errorwhenfull y|n ]
	[    --pooldatavdo y|n ]
	[    --compression y|n ]
	[    --deduplication y|n ]
	[    --vdosettings String ]
	[    --poolmetadatasize Size[m|UNIT] ]
	[    --poolmetadataspare y|n ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Create a cache pool.
  lvcreate --type cache-pool -L|--size Size[m|UNIT] VG
	[ -l|--extents Number[PERCENT] ]
	[ -i|--stripes Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ -H|--cache ]
	[ -c|--chunksize Size[k|UNIT] ]
	[    --cachemode writethrough|writeback|passthrough ]
	[    --cachepolicy String ]
	[    --cachesettings String ]
	[    --cachemetadataformat auto|1|2 ]
	[    --poolmetadatasize Size[m|UNIT] ]
	[    --poolmetadataspare y|n ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Create a thin LV in a thin pool.
  lvcreate -V|--virtualsize Size[m|UNIT] --thinpool LV VG
	[ --type thin ] (implied)
	[ -T|--thin ]
	[ COMMON_OPTIONS ]
  Create a thin LV that is a snapshot of an existing thin LV.
  lvcreate -s|--snapshot LV
	[ --type thin ] (implied)
	[ COMMON_OPTIONS ]
  Create a thin LV that is a snapshot of an external origin LV.
  lvcreate --type thin --thinpool LV LV
	[ -T|--thin ]
	[ COMMON_OPTIONS ]
  Create a LV that returns VDO when used.
  lvcreate --type vdo -L|--size Size[m|UNIT] VG
	[ -l|--extents Number[PERCENT] ]
	[ -i|--stripes Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ -V|--virtualsize Size[m|UNIT] ]
	[    --vdo ]
	[    --vdopool LV_new ]
	[    --compression y|n ]
	[    --deduplication y|n ]
	[    --vdosettings String ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Create a new LV, then attach the specified cachepool
  which converts the new LV to type cache.
  lvcreate --type cache -L|--size Size[m|UNIT] --cachepool LV VG
	[ -l|--extents Number[PERCENT] ]
	[ -i|--stripes Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ -H|--cache ]
	[ -c|--chunksize Size[k|UNIT] ]
	[    --cachemode writethrough|writeback|passthrough ]
	[    --cachepolicy String ]
	[    --cachesettings String ]
	[    --cachemetadataformat auto|1|2 ]
	[    --poolmetadatasize Size[m|UNIT] ]
	[    --poolmetadataspare y|n ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Create a new LV, then attach the specified cachevol
  which converts the new LV to type cache.
  lvcreate --type cache -L|--size Size[m|UNIT] --cachevol LV VG
	[ -l|--extents Number[PERCENT] ]
	[ -i|--stripes Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ -c|--chunksize Size[k|UNIT] ]
	[    --cachemode writethrough|writeback|passthrough ]
	[    --cachepolicy String ]
	[    --cachesettings String ]
	[    --cachemetadataformat auto|1|2 ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Create a new LV, then attach a cachevol created from
  the specified cache device, which converts the
  new LV to type cache.
  lvcreate --type cache -L|--size Size[m|UNIT] --cachedevice PV VG
	[ -l|--extents Number[PERCENT] ]
	[ -i|--stripes Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ -c|--chunksize Size[k|UNIT] ]
	[    --cachesize Size[m|UNIT] ]
	[    --cachemode writethrough|writeback|passthrough ]
	[    --cachepolicy String ]
	[    --cachesettings String ]
	[    --cachemetadataformat auto|1|2 ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Create a new LV, then attach the specified cachevol
  which converts the new LV to type writecache.
  lvcreate --type writecache -L|--size Size[m|UNIT] --cachevol LV VG
	[ -l|--extents Number[PERCENT] ]
	[ -i|--stripes Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[    --cachesettings String ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Create a new LV, then attach a cachevol created from
  the specified cache device, which converts the
  new LV to type writecache.
  lvcreate --type writecache -L|--size Size[m|UNIT] --cachedevice PV VG
	[ -l|--extents Number[PERCENT] ]
	[ -i|--stripes Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[    --cachesize Size[m|UNIT] ]
	[    --cachesettings String ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Common options for command:
	[ -a|--activate y|n|ay ]
	[ -A|--autobackup y|n ]
	[ -C|--contiguous y|n ]
	[ -M|--persistent y|n ]
	[ -j|--major Number ]
	[ -k|--setactivationskip y|n ]
	[ -K|--ignoreactivationskip ]
	[ -n|--name String ]
	[ -p|--permission rw|r ]
	[ -r|--readahead auto|none|Number ]
	[ -W|--wipesignatures y|n ]
	[ -Z|--zero y|n ]
	[    --addtag Tag ]
	[    --alloc contiguous|cling|cling_by_tags|normal|anywhere|inherit ]
	[    --setautoactivation y|n ]
	[    --ignoremonitoring ]
	[    --metadataprofile String ]
	[    --minor Number ]
	[    --monitor y|n ]
	[    --nosync ]
	[    --noudevsync ]
	[    --reportformat basic|json|json_std ]
  Common options for lvm:
	[ -d|--debug ]
	[ -h|--help ]
	[ -q|--quiet ]
	[ -v|--verbose ]
	[ -y|--yes ]
```

### `lvdisplay`

> 官方示例调用：`lvdisplay -h`

```text
root@kali:~# lvdisplay -h
  lvdisplay - Display information about a logical volume
  lvdisplay
	[ -m|--maps ]
	[ COMMON_OPTIONS ]
	[ VG|LV|Tag ... ]
  Display output in columns like lvs.
  lvdisplay -C|--columns
	[ -o|--options String ]
	[ -O|--sort String ]
	[    --aligned ]
	[    --binary ]
	[    --headings none|abbrev|full|0|1|2 ]
	[    --nameprefixes ]
	[    --noheadings ]
	[    --nosuffix ]
	[    --rows ]
	[    --separator String ]
	[    --unbuffered ]
	[    --unquoted ]
	[ COMMON_OPTIONS ]
	[ VG|LV|Tag ... ]
  Generate colon separated output.
  lvdisplay -c|--colon
	[ COMMON_OPTIONS ]
	[ VG|LV|Tag ... ]
  Common options for command:
	[ -a|--all ]
	[ -H|--history ]
	[ -S|--select String ]
	[    --configreport log|vg|lv|pv|pvseg|seg ]
	[    --foreign ]
	[    --ignorelockingfailure ]
	[    --logonly ]
	[    --readonly ]
	[    --reportformat basic|json|json_std ]
	[    --segments ]
	[    --shared ]
	[    --units [Number]r|R|h|H|b|B|s|S|k|K|m|M|g|G|t|T|p|P|e|E ]
  Common options for lvm:
	[ -d|--debug ]
	[ -h|--help ]
	[ -q|--quiet ]
	[ -v|--verbose ]
	[ -y|--yes ]
	[ -t|--test ]
	[    --commandprofile String ]
	[    --config String ]
	[    --driverloaded y|n ]
	[    --nolocking ]
	[    --lockopt String ]
	[    --longhelp ]
	[    --profile String ]
	[    --version ]
	[    --devicesfile String ]
	[    --devices PV ]
	[    --nohints ]
	[    --journal String ]
  Use --longhelp to show all options and advanced commands.
```

### `lvextend`

> 官方示例调用：`lvextend -h`

```text
root@kali:~# lvextend -h
  lvextend - Add space to a logical volume
  Extend an LV by a specified size.
  lvextend -L|--size [+]Size[m|UNIT] LV
	[ -l|--extents [+]Number[PERCENT] ]
	[ -r|--resizefs ]
	[ -i|--stripes Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[    --poolmetadatasize [+]Size[m|UNIT] ]
	[    --fs String ]
	[    --fsmode String ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Extend an LV by specified PV extents.
  lvextend LV PV ...
	[ -r|--resizefs ]
	[ -i|--stripes Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[    --fs String ]
	[    --fsmode String ]
	[ COMMON_OPTIONS ]
  Extend a pool metadata SubLV by a specified size.
  lvextend --poolmetadatasize [+]Size[m|UNIT] LV
	[ -i|--stripes Number ]
	[ -I|--stripesize Size[k|UNIT] ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Extend an LV according to a predefined policy.
  lvextend --usepolicies LV
	[ -r|--resizefs ]
	[    --fs String ]
	[    --fsmode String ]
	[ COMMON_OPTIONS ]
	[ PV ... ]
  Common options for command:
	[ -A|--autobackup y|n ]
	[ -f|--force ]
	[ -m|--mirrors Number ]
	[ -n|--nofsck ]
	[    --alloc contiguous|cling|cling_by_tags|normal|anywhere|inherit ]
	[    --nosync ]
	[    --noudevsync ]
	[    --reportformat basic|json|json_std ]
	[    --type linear|striped|snapshot|raid|mirror|thin|thin-pool|vdo|vdo-pool|cache|cache-pool|writecache ]
  Common options for lvm:
	[ -d|--debug ]
	[ -h|--help ]
	[ -q|--quiet ]
	[ -v|--verbose ]
	[ -y|--yes ]
	[ -t|--test ]
	[    --commandprofile String ]
	[    --config String ]
	[    --driverloaded y|n ]
	[    --nolocking ]
	[    --lockopt String ]
	[    --longhelp ]
	[    --profile String ]
	[    --version ]
	[    --devicesfile String ]
	[    --devices PV ]
	[    --nohints ]
	[    --journal String ]
  Use --longhelp to show all options and advanced commands.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install lvm2`，再执行 `dmeventd --version` 2>/dev/null || `dmeventd -V`
- [ ] **2.** **读官方帮助** —— `dmeventd -h`，需要细节时 `man dmeventd`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/lvm2/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/lvm2/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/lvm2/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
