# samba

> SMB/CIFS file, print, and login server for Unix Samba is an implementation of the SMB/CIFS protocol for Unix systems, providing support for cross-platform file and printer sharing with Microsoft Windows, OS X, and other Unix systems. Samba…

> **功能分类**：信息搜集 ｜ **Kali 包**：`samba` ｜ **官方文档**：<https://www.kali.org/tools/samba/>

## 1. 安装

```bash
sudo apt update
sudo apt install samba
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.24.6 |
| 架构 | any |
| 可执行命令 | `ctdb`、`ctdb_diagnostics`、`ctdbd`、`ltdbtool`、`onnode`、`ping_pong`、`ldb-tools`、`ldbadd`、`ldbdel`、`ldbedit`、`ldbmodify`、`ldbrename`、`ldbsearch`、`libldb-dev`、`libldb2`、`libnss-winbind`、`libpam-winbind`、`libsmbclient`、`libsmbclient-dev`、`libsmbclient0`、`libtalloc-dev`、`libtalloc2`、`libtdb-dev`、`libtdb1`、`libtevent-dev`、`libtevent0`、`libtevent0t64`、`libwbclient-dev`、`libwbclient0`、`python3-ldb`、`python3-samba`、`samba-gpupdate`、`samba-tool`、`python3-talloc`、`python3-tdb`、`registry-tools`、`regdiff`、`regpatch`、`regshell`、`regtree`、`samba`、`eventlogadm`、`mvxattr`、`nmbd` |
| 依赖 | `libbsd0`、`libc6`、`libcups2t64`、`libdbus-1-3`、`libgnutls30t64`、`libldap2`、`libldb2`、`libndr6`、`libpopt0`、`libtalloc2`、`libtdb1`、`libtevent0t64` 等 |
| 安装体积 | 5.01 MB |
| 官网 | <https://www.samba.org> |
| 源码仓库 | <https://salsa.debian.org/samba-team/samba> |
| 包追踪 | <https://pkg.kali.org/pkg/samba> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ctdb -h          # 查看用法
man ctdb         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 44 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ctdb`

官方给出的调用示例：`ctdb --help`

```text
root@kali:~# ctdb --help
Usage: [OPTION...]
  -d, --debug=STRING       debug level
  -t, --timelimit=INT      timelimit (in seconds)
  -n, --node=INT           node specification - integer
  -Y                       enable machine readable output
  -x, --separator=CHAR     specify separator for machine readable output
  -X                       enable machine parsable output with separator |
  -v, --verbose            enable verbose output
  -T, --maxruntime=INT     die if runtime exceeds this limit (in seconds)
Help options:
  -?, --help               Show this help message
      --usage              Display brief usage message
```

### `ctdb_diagnostics`

官方给出的调用示例：`ctdb_diagnostics -h`

```text
root@kali:~# ctdb_diagnostics -h
Failed to read nodes from "/etc/ctdb/nodes"
Usage: ctdb_diagnostics [OPTION] ...
  options:
    -n <nodes>  Comma separated list of nodes to operate on
    -c          Ignore comment lines (starting with '#') in file comparisons
    -l          Run in local mode
    -w          Ignore whitespace in file comparisons
    --no-ads    Do not use commands that assume an Active Directory Server
```

### `ctdbd`

官方给出的调用示例：`ctdbd --help`

```text
root@kali:~# ctdbd --help
Usage: [OPTION...]
  -i, --interactive     don't fork, log to stderr
Help options:
  -?, --help            Show this help message
      --usage           Display brief usage message
```

### `ltdbtool`

官方给出的调用示例：`ltdbtool -h`

```text
root@kali:~# ltdbtool -h
Usage: ltdbtool [options] <command>
Options:
   -s {0|32|64}    specify how to determine the ctdb record header size
                   for the input database:
                   0: no ctdb header
                   32: ctdb header size of a 32 bit system (20 bytes)
                   64: ctdb header size of a 64 bit system (24 bytes)
                   default: 32 or 64 depending on the system architecture
   -S <num>        the number of bytes to interpret as ctdb record header
                   for the input database (beware!)
   -o {0|32|64}    specify how to determine the ctdb record header size
                   for the output database
                   0: no ctdb header
                   32: ctdb header size of a 32 bit system (20 bytes)
                   64: ctdb header size of a 64 bit system (24 bytes)
                   default: 32 or 64 depending on the system architecture
   -O <num>        the number of bytes to interpret as ctdb record header
                   for the output database (beware!)
   -e              Include empty records, defaults to off
   -p              print header (for the dump command), defaults to off
   -h              print this help
Commands:
  help                         print this help
  dump <db>                    dump the db to stdout
  convert <in_db> <out_db>     convert the db
```

### `onnode`

官方给出的调用示例：`onnode --help`

```text
root@kali:~# onnode --help
/usr/bin/onnode: illegal option -- -
Usage: onnode [OPTION] ... <NODES> <COMMAND> ...
  options:
    -c          Run in current working directory on specified nodes.
    -f          Specify nodes file, overriding default.
    -i          Keep standard input open - the default is to close it.
    -n          Allow nodes to be specified by name.
    -p          Run command in parallel on specified nodes.
    -P          Push given files to nodes instead of running commands.
    -q          Do not print node addresses (overrides -v).
    -v          Print node address even for a single node.
  <NODES>       "all", "any", "ok" (or "healthy"), "con" (or "connected") ; or
                a node number (0 base); or
                a hostname (if -n is specified); or
                list (comma separated) of <NODES>; or
                range (hyphen separated) of node numbers.
```

### `man`

官方给出的调用示例：`man ping_pong`

```text
root@kali:~# man ping_pong
PING_PONG(1)             CTDB - clustered TDB database             PING_PONG(1)
NAME
     ping_pong - measures the ping-pong byte range lock latency
SYNOPSIS
     ping_pong {-r | -w | -rw} [-m] [-c] {FILENAME} {NUM-LOCKS}
DESCRIPTION
     ping_pong measures the byte range lock latency. It is especially useful on
     a  cluster of nodes sharing a common lock manager as it will give some in-
     dication of the lock manager's performance under stress.
     FILENAME is a file on shared storage to use for byte range locking tests.
     NUM-LOCKS is the number of byte range locks, so  needs  to  be  (strictly)
     greater than the number of nodes in the cluster.
OPTIONS
     -r
         test read performance
     -w
         test write performance
     -m
         use mmap
     -c
         validate the locks
EXAMPLES
     Testing lock coherence
               ping_pong test.dat N
     Testing lock coherence with lock validation
               ping_pong -c test.dat N
     Testing IO coherence
               ping_pong -rw test.dat N
SEE ALSO
     ctdb(7), https://wiki.samba.org/index.php/Ping_pong
AUTHOR
     This documentation was written by Mathieu Parent
COPYRIGHT
     Copyright (C) 2002 Andrew Tridgell
     This  program  is  free software; you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the Free
     Software Foundation; either version 3 of the License, or (at your  option)
     any later version.
     This  program is distributed in the hope that it will be useful, but WITH-
     OUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY  or
     FITNESS  FOR  A PARTICULAR PURPOSE. See the GNU General Public License for
     more details.
     You should have received a copy of the GNU General  Public  License  along
     with this program; if not, see http://www.gnu.org/licenses.
ctdb                               08/13/2026                      PING_PONG(1)
```

### `ldbadd`

官方给出的调用示例：`ldbadd --help`

```text
root@kali:~# ldbadd --help
Usage: [OPTION...]
  -H, --url=URL                   database URL
  -b, --basedn=DN                 base DN
  -e, --editor=PROGRAM            external editor
  -s, --scope=SCOPE               search scope
  -v, --verbose                   increase verbosity
      --trace                     enable tracing
  -i, --interactive               input from stdin
  -r, --recursive                 recursive delete
      --modules-path=PATH         modules path
      --num-searches=INT          number of test searches
      --num-records=INT           number of test records
  -a, --all                       (|(objectClass=*)(distinguishedName=*))
      --nosync                    non-synchronous transactions
  -S, --sorted                    sort attributes
  -o OPTION                       ldb_connect option
      --controls=STRING           controls
      --show-binary               display binary LDIF
      --paged                     use a paged search
      --show-deleted              show deleted objects
      --show-recycled             show recycled objects
      --show-deactivated-link     show deactivated links
      --reveal                    reveal ldb internals
      --relax                     pass relax control
      --cross-ncs                 search across NC boundaries
      --extended-dn               show extended DNs
Help options:
  -?, --help                      Show this help message
      --usage                     Display brief usage message
```

### `ldbdel`

官方给出的调用示例：`ldbdel --help`

```text
root@kali:~# ldbdel --help
Usage: [OPTION...]
  -H, --url=URL                   database URL
  -b, --basedn=DN                 base DN
  -e, --editor=PROGRAM            external editor
  -s, --scope=SCOPE               search scope
  -v, --verbose                   increase verbosity
      --trace                     enable tracing
  -i, --interactive               input from stdin
  -r, --recursive                 recursive delete
      --modules-path=PATH         modules path
      --num-searches=INT          number of test searches
      --num-records=INT           number of test records
  -a, --all                       (|(objectClass=*)(distinguishedName=*))
      --nosync                    non-synchronous transactions
  -S, --sorted                    sort attributes
  -o OPTION                       ldb_connect option
      --controls=STRING           controls
      --show-binary               display binary LDIF
      --paged                     use a paged search
      --show-deleted              show deleted objects
      --show-recycled             show recycled objects
      --show-deactivated-link     show deactivated links
      --reveal                    reveal ldb internals
      --relax                     pass relax control
      --cross-ncs                 search across NC boundaries
      --extended-dn               show extended DNs
Help options:
  -?, --help                      Show this help message
      --usage                     Display brief usage message
```

### `ldbedit`

官方给出的调用示例：`ldbedit --help`

```text
root@kali:~# ldbedit --help
Usage: [OPTION...]
  -H, --url=URL                   database URL
  -b, --basedn=DN                 base DN
  -e, --editor=PROGRAM            external editor
  -s, --scope=SCOPE               search scope
  -v, --verbose                   increase verbosity
      --trace                     enable tracing
  -i, --interactive               input from stdin
  -r, --recursive                 recursive delete
      --modules-path=PATH         modules path
      --num-searches=INT          number of test searches
      --num-records=INT           number of test records
  -a, --all                       (|(objectClass=*)(distinguishedName=*))
      --nosync                    non-synchronous transactions
  -S, --sorted                    sort attributes
  -o OPTION                       ldb_connect option
      --controls=STRING           controls
      --show-binary               display binary LDIF
      --paged                     use a paged search
      --show-deleted              show deleted objects
      --show-recycled             show recycled objects
      --show-deactivated-link     show deactivated links
      --reveal                    reveal ldb internals
      --relax                     pass relax control
      --cross-ncs                 search across NC boundaries
      --extended-dn               show extended DNs
Help options:
  -?, --help                      Show this help message
      --usage                     Display brief usage message
```

### `ldbmodify`

官方给出的调用示例：`ldbmodify --help`

```text
root@kali:~# ldbmodify --help
Usage: [OPTION...]
  -H, --url=URL                   database URL
  -b, --basedn=DN                 base DN
  -e, --editor=PROGRAM            external editor
  -s, --scope=SCOPE               search scope
  -v, --verbose                   increase verbosity
      --trace                     enable tracing
  -i, --interactive               input from stdin
  -r, --recursive                 recursive delete
      --modules-path=PATH         modules path
      --num-searches=INT          number of test searches
      --num-records=INT           number of test records
  -a, --all                       (|(objectClass=*)(distinguishedName=*))
      --nosync                    non-synchronous transactions
  -S, --sorted                    sort attributes
  -o OPTION                       ldb_connect option
      --controls=STRING           controls
      --show-binary               display binary LDIF
      --paged                     use a paged search
      --show-deleted              show deleted objects
      --show-recycled             show recycled objects
      --show-deactivated-link     show deactivated links
      --reveal                    reveal ldb internals
      --relax                     pass relax control
      --cross-ncs                 search across NC boundaries
      --extended-dn               show extended DNs
Help options:
  -?, --help                      Show this help message
      --usage                     Display brief usage message
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install samba`，再执行 `ctdb --version` 2>/dev/null || `ctdb -V`
- [ ] **2.** **读官方帮助** —— `ctdb -h`，需要细节时 `man ctdb`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: [OPTION...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/samba/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/samba/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/samba/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
