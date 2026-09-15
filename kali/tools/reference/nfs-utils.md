# nfs-utils

> Header files and docs for libnfsidmap Contains the header files and documentation for libnfsidmap for use in developing applications that use the libnfsidmap library. libnfsidmap provides functions to map between NFSv4 names (which are of …

> **功能分类**：信息搜集 ｜ **Kali 包**：`nfs-utils` ｜ **官方文档**：<https://www.kali.org/tools/nfs-utils/>

## 1. 安装

```bash
sudo apt update
sudo apt install libnfsidmap-dev
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.9.2 |
| 架构 | any |
| 可执行命令 | `libnfsidmap-dev`、`libnfsidmap1`、`nfs-common`、`mount.nfs`、`mount.nfs4`、`mountstats`、`nfsconf`、`nfsidmap`、`nfsiostat`、`nfsstat`、`rpc.gssd`、`rpc.idmapd`、`rpc.statd`、`rpc.svcgssd`、`rpcctl`、`rpcdebug`、`showmount`、`sm-notify`、`start-statd`、`umount.nfs`、`umount.nfs4`、`nfs-kernel-server`、`exportfs`、`fsidd`、`nfsdcld`、`nfsdclddb`、`nfsdclnts`、`nfsdctl`、`nfsref`、`rpc.mountd`、`rpc.nfsd` |
| 依赖 | `libnfsidmap1`、`libnfsidmap1` |
| 安装体积 | 110 KB |
| 官网 | <https://linux-nfs.org/> |
| 源码仓库 | <https://salsa.debian.org/kernel-team/nfs-utils> |
| 包追踪 | <https://pkg.kali.org/pkg/nfs-utils> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libnfsidmap-dev -h          # 查看用法
man libnfsidmap-dev         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 31 个可执行命令，下面是官方页面内嵌的帮助原文。

### `mount.nfs`

官方给出的调用示例：`mount.nfs -h`

```text
root@kali:~# mount.nfs -h
usage: mount.nfs remotetarget dir [-rvVwfnsh] [-o nfsoptions]
options:
	-r		Mount file system readonly
	-v		Verbose
	-V		Print version
	-w		Mount file system read-write
	-f		Fake mount, do not actually mount
	-n		Do not update /etc/mtab
	-s		Tolerate sloppy mount options rather than fail
	-h		Print this help
	nfsoptions	Refer to mount.nfs(8) or nfs(5)
```

### `mount.nfs4`

官方给出的调用示例：`mount.nfs4 -h`

```text
root@kali:~# mount.nfs4 -h
usage: mount.nfs4 remotetarget dir [-rvVwfnsh] [-o nfsoptions]
options:
	-r		Mount file system readonly
	-v		Verbose
	-V		Print version
	-w		Mount file system read-write
	-f		Fake mount, do not actually mount
	-n		Do not update /etc/mtab
	-s		Tolerate sloppy mount options rather than fail
	-h		Print this help
	nfsoptions	Refer to mount.nfs(8) or nfs(5)
```

### `mountstats`

官方给出的调用示例：`mountstats -h`

```text
root@kali:~# mountstats -h
usage: mountstats [-h] {mountstats,nfsstat,iostat} ...
positional arguments:
  {mountstats,nfsstat,iostat}
                        sub-command help
    mountstats          Display a combination of per-op RPC statistics, NFS
                        event counts, and NFS byte counts. This is the default
                        sub-command if no sub-command is given.
    nfsstat             Display nfsstat-like statistics.
    iostat              Display iostat-like statistics.
options:
  -h, --help            show this help message and exit
For specific sub-command help, run 'mountstats SUB-COMMAND -h|--help'
```

### `nfsconf`

官方给出的调用示例：`nfsconf -h`

```text
root@kali:~# nfsconf -h
nfsconf: invalid option -- 'h'
Usage: nfsconf [-v] [--file filename.conf] ...
Options:
 -v			Increase Verbosity
 --file filename.conf	Load this config file
     (Default config file: /etc/nfs.conf
 --modified "info"	Use "info" in file modified header
Modes:
  --dump [outputfile]
      Outputs the configuration to the named file
  --get [--arg subsection] {section} {tag}
      Output one specific config value
  --entry [--arg subsection] {section} {tag}
      Output the uninterpreted config entry
  --isset [--arg subsection] {section} {tag}
      Return code indicates if config value is present
  --set [--arg subsection] {section} {tag} {value}
      Set and Write a config value
  --unset [--arg subsection] {section} {tag}
      Remove an existing config value
```

### `nfsidmap`

官方给出的调用示例：`nfsidmap -h`

```text
root@kali:~# nfsidmap -h
nfsidmap: Usage: nfsidmap [-vh] [-c || [-u|-g|-r key] || -d || -l || [-t timeout] key desc]
```

### `nfsiostat`

官方给出的调用示例：`nfsiostat -h`

```text
root@kali:~# nfsiostat -h
Usage: nfsiostat [ <interval> [ <count> ] ] [ <options> ] [ <mount point> ]
 Sample iostat-like program to display NFS client per-mount' statistics.  The
<interval> parameter specifies the amount of time in seconds between each
report.  The first report contains statistics for the time since each file
system was mounted.  Each subsequent report contains statistics collected
during the interval since the previous report.  If the <count> parameter is
specified, the value of <count> determines the number of reports generated at
<interval> seconds apart.  If the interval parameter is specified without the
<count> parameter, the command generates reports continuously. If one or more
<mount point> names are specified, statistics for only these mount points will
be displayed.  Otherwise, all NFS mount points on the client are listed.
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  Statistics Options:
    File I/O is displayed unless one of the following is specified:
    -a, --attr          displays statistics related to the attribute cache
    -d, --dir           displays statistics related to directory operations
    -p, --page          displays statistics related to the page cache
  Display Options:
    Options affecting display format:
    -s, --sort          Sort NFS mount points by ops/second
    -l LIST, --list=LIST
                        only print stats for first LIST mount points
    -m, --megabytes     display throughput in megabytes per second (MB/s)
                        instead of kilobytes per second (kB/s)
```

### `nfsstat`

官方给出的调用示例：`nfsstat --help`

```text
root@kali:~# nfsstat --help
Usage: nfsstat [OPTION]...
  -m, --mounts		Show statistics on mounted NFS filesystems
  -c, --client		Show NFS client statistics
  -s, --server		Show NFS server statistics
  -2			Show NFS version 2 statistics
  -3			Show NFS version 3 statistics
  -4			Show NFS version 4 statistics
  -o [facility]		Show statistics on particular facilities.
     nfs		NFS protocol information
     rpc		General RPC information
     net		Network layer statistics
     fh			Usage information on the server's file handle cache
     io			Usage information on the server's io statistics
     ra			Usage information on the server's read ahead cache
     rc			Usage information on the server's request reply cache
     all		Select all of the above
  -v, --verbose, --all	Same as '-o all'
  -r, --rpc		Show RPC statistics
  -n, --nfs		Show NFS statistics
  -Z[#], --sleep[=#]	Collects stats until interrupted.
			    Cumulative stats are then printed
          		    If # is provided, stats will be output every
			    # seconds.
  -S, --since file	Shows difference between current stats and those in 'file'
  -l, --list		Prints stats in list format
  --version		Show program version
  --help		What you just did
```

### `rpc.gssd`

官方给出的调用示例：`rpc.gssd -h`

```text
root@kali:~# rpc.gssd -h
rpc.gssd: invalid option -- 'h'
usage: rpc.gssd [-f] [-l] [-M] [-n] [-v] [-r] [-p pipefsdir] [-k keytab] [-d ccachedir] [-t timeout] [-R preferred realm] [-D] [-H] [-U upcall timeout] [-C]
```

### `rpc.idmapd`

官方给出的调用示例：`rpc.idmapd -h`

```text
root@kali:~# rpc.idmapd -h
Usage: rpc.idmapd [-hfvCS] [-p path] [-c path]
```

### `rpc.statd`

官方给出的调用示例：`rpc.statd -h`

```text
root@kali:~# rpc.statd -h
usage: rpc.statd [options]
      -h, -?, --help       Print this help screen.
      -F, --foreground     Foreground (no-daemon mode)
      -d, --no-syslog      Verbose logging to stderr.  Foreground mode only.
      -p, --port           Port to listen on
      -o, --outgoing-port  Port for outgoing connections
      -V, -v, --version    Display version information and exit.
      -n, --name           Specify a local hostname.
      -P                   State directory path.
      -N                   Run in notify only mode.
      -L, --no-notify      Do not perform any notification.
      -H                   Specify a high-availability callout program.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install libnfsidmap-dev`，再执行 `libnfsidmap-dev --version` 2>/dev/null || `libnfsidmap-dev -V`
- [ ] **2.** **读官方帮助** —— `libnfsidmap-dev -h`，需要细节时 `man libnfsidmap-dev`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: nfsconf [-v] [--file filename.conf] ...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/nfs-utils/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/nfs-utils/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/nfs-utils/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
