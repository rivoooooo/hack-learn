# subversion

> Advanced version control system Apache Subversion, also known as svn, is a centralised version control system. Version control systems allow many individuals (who may be distributed geographically) to collaborate on a set of files (source …

> **功能分类**：信息搜集 ｜ **Kali 包**：`subversion` ｜ **官方文档**：<https://www.kali.org/tools/subversion/>

## 1. 安装

```bash
sudo apt update
sudo apt install subversion
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.14.5 |
| 架构 | any |
| 可执行命令 | `libapache2-mod-svn`、`libsvn-dev`、`libsvn-doc`、`libsvn-java`、`libsvn-perl`、`libsvn1`、`python3-subversion`、`ruby-svn`、`subversion`、`svn`、`svnadmin`、`svnauthz`、`svnauthz-validate`、`svnbench`、`svndumpfilter`、`svnfsfs`、`svnlook`、`svnmucc`、`svnrdump`、`svnserve`、`svnsync`、`svnversion`、`subversion-tools`、`fsfs-access-map`、`fsfs-stats`、`svn-backup-dumps`、`svn-bisect`、`svn-clean`、`svn-hot-backup`、`svn-mergeinfo-normalizer`、`svn-populate-node-origins-index`、`svn-vendor`、`svn_apply_autoprops`、`svn_load_dirs`、`svnraisetreeconflict`、`svnwrap` |
| 依赖 | `libapr1t64`、`libaprutil1t64`、`libc6`、`libsvn1`、`svn` |
| 安装体积 | 4.73 MB |
| 官网 | <http://subversion.apache.org/> |
| 源码仓库 | <https://salsa.debian.org/jamessan/subversion> |
| 包追踪 | <https://pkg.kali.org/pkg/subversion> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libapache2-mod-svn -h          # 查看用法
man libapache2-mod-svn         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 36 个可执行命令，下面是官方页面内嵌的帮助原文。

### `svn`

官方给出的调用示例：`svn -h`

```text
root@kali:~# svn -h
usage: svn <subcommand> [options] [args]
Subversion command-line client.
Type 'svn help <subcommand>' for help on a specific subcommand.
Type 'svn --version' to see the program version and RA modules,
     'svn --version --verbose' to see dependency versions as well,
     'svn --version --quiet' to see just the version number.
Most subcommands take file and/or directory arguments, recursing
on the directories.  If no arguments are supplied to such a
command, it recurses on the current directory (inclusive) by default.
Available subcommands:
   add
   auth
   blame (praise, annotate, ann)
   cat
   changelist (cl)
   checkout (co)
   cleanup
   commit (ci)
   copy (cp)
   delete (del, remove, rm)
   diff (di)
   export
   help (?, h)
   import
   info
   list (ls)
   lock
   log
   merge
   mergeinfo
   mkdir
   move (mv, rename, ren)
   patch
   propdel (pdel, pd)
   propedit (pedit, pe)
   propget (pget, pg)
   proplist (plist, pl)
   propset (pset, ps)
   relocate
   resolve
   resolved
   revert
   status (stat, st)
   switch (sw)
   unlock
   update (up)
   upgrade
Subversion is a tool for version control.
For additional information, see http://subversion.apache.org/
```

### `svnadmin`

官方给出的调用示例：`svnadmin -h`

```text
root@kali:~# svnadmin -h
general usage: svnadmin SUBCOMMAND REPOS_PATH  [ARGS & OPTIONS ...]
Subversion repository administration tool.
Type 'svnadmin help <subcommand>' for help on a specific subcommand.
Type 'svnadmin --version' to see the program version and FS modules.
Available subcommands:
   build-repcache
   crashtest
   create
   delrevprop
   deltify
   dump
   dump-revprops
   freeze
   help (?, h)
   hotcopy
   info
   list-dblogs
   list-unused-dblogs
   load
   load-revprops
   lock
   lslocks
   lstxns
   pack
   recover
   rev-size
   rmlocks
   rmtxns
   setlog
   setrevprop
   setuuid
   unlock
   upgrade
   verify
```

### `svnauthz`

官方给出的调用示例：`svnauthz -h`

```text
root@kali:~# svnauthz -h
general usage: svnauthz SUBCOMMAND TARGET [ARGS & OPTIONS ...]
               svnauthz-validate TARGET
If the command name starts with 'svnauthz-validate', runs in
pre-1.8 compatibility mode: run the 'validate' subcommand on TARGET.
Type 'svnauthz help <subcommand>' for help on a specific subcommand.
Type 'svnauthz --version' to see the program version.
Available subcommands:
   help (?, h)
   validate
   accessof
```

### `svnbench`

官方给出的调用示例：`svnbench -h`

```text
root@kali:~# svnbench -h
usage: svnbench <subcommand> [options] [args]
Subversion benchmarking tool.
Type 'svnbench help <subcommand>' for help on a specific subcommand.
Type 'svnbench --version' to see the program version and RA modules
  or 'svnbench --version --quiet' to see just the version number.
Most subcommands take file and/or directory arguments, recursing
on the directories.  If no arguments are supplied to such a
command, it recurses on the current directory (inclusive) by default.
Available subcommands:
   help (?, h)
   null-blame
   null-export
   null-list (ls)
   null-log
   null-info
Subversion is a tool for version control.
For additional information, see http://subversion.apache.org/
```

### `svndumpfilter`

官方给出的调用示例：`svndumpfilter -h`

```text
root@kali:~# svndumpfilter -h
general usage: svndumpfilter SUBCOMMAND [ARGS & OPTIONS ...]
Subversion repository dump filtering tool.
Type 'svndumpfilter help <subcommand>' for help on a specific subcommand.
Type 'svndumpfilter --version' to see the program version.
Available subcommands:
   exclude
   include
   help (?, h)
```

### `svnfsfs`

官方给出的调用示例：`svnfsfs -h`

```text
root@kali:~# svnfsfs -h
general usage: svnfsfs SUBCOMMAND REPOS_PATH  [ARGS & OPTIONS ...]
Subversion FSFS repository manipulation tool.
Type 'svnfsfs help <subcommand>' for help on a specific subcommand.
Type 'svnfsfs --version' to see the program version.
Available subcommands:
   help (?, h)
   dump-index
   load-index
   stats
```

### `svnlook`

官方给出的调用示例：`svnlook -h`

```text
root@kali:~# svnlook -h
general usage: svnlook SUBCOMMAND REPOS_PATH [ARGS & OPTIONS ...]
Subversion repository inspection tool.
Type 'svnlook help <subcommand>' for help on a specific subcommand.
Type 'svnlook --version' to see the program version and FS modules.
Note: any subcommand which takes the '--revision' and '--transaction'
      options will, if invoked without one of those options, act on
      the repository's youngest revision.
Available subcommands:
   author
   cat
   changed
   date
   diff
   dirs-changed
   filesize
   help (?, h)
   history
   info
   lock
   log
   propget (pget, pg)
   proplist (plist, pl)
   tree
   uuid
   youngest
```

### `svnmucc`

官方给出的调用示例：`svnmucc -h`

```text
root@kali:~# svnmucc -h
usage: svnmucc ACTION...
Subversion multiple URL command client.
Type 'svnmucc --version' to see the program version and RA modules.
  Perform one or more Subversion repository URL-based ACTIONs, committing
  the result as a (single) new revision.
Actions:
  cp REV SRC-URL DST-URL : copy SRC-URL@REV to DST-URL
  mkdir URL              : create new directory URL
  mv SRC-URL DST-URL     : move SRC-URL to DST-URL
  rm URL                 : delete URL
  put SRC-FILE URL       : add or modify file URL with contents copied from
                           SRC-FILE (to read from standard input, use "--"
                           to stop option processing followed by "-" to
                           indicate standard input)
  propset NAME VALUE URL : set property NAME on URL to VALUE
  propsetf NAME FILE URL : set property NAME on URL to value read from FILE
  propdel NAME URL       : delete property NAME from URL
Valid options:
  -h, -? [--help]        : display this text
  -m [--message] ARG     : use ARG as a log message
  -F [--file] ARG        : read log message from file ARG
  -u [--username] ARG    : commit the changes as username ARG
  -p [--password] ARG    : use ARG as the password
  --password-from-stdin  : read password from stdin
  -U [--root-url] ARG    : interpret all action URLs relative to ARG
  -r [--revision] ARG    : use revision ARG as baseline for changes
  --with-revprop ARG     : set revision property in the following format:
                               NAME[=VALUE]
  --non-interactive      : do no interactive prompting (default is to
                           prompt only if standard input is a terminal)
  --force-interactive    : do interactive prompting even if standard
                           input is not a terminal
  --trust-server-cert    : deprecated;
                           same as --trust-server-cert-failures=unknown-ca
  --trust-server-cert-failures ARG
                           with --non-interactive, accept SSL server
                           certificates with failures; ARG is comma-separated
                           list of 'unknown-ca' (Unknown Authority),
                           'cn-mismatch' (Hostname mismatch), 'expired'
                           (Expired certificate),'not-yet-valid' (Not yet
                           valid certificate) and 'other' (all other not
                           separately classified certificate errors).
  -X [--extra-args] ARG  : append arguments from file ARG (one per line;
                           use "-" to read from standard input)
  --config-dir ARG       : use ARG to override the config directory
  --config-option ARG    : use ARG to override a configuration option
  --no-auth-cache        : do not cache authentication tokens
  --version              : print version information
```

### `svnrdump`

官方给出的调用示例：`svnrdump -h`

```text
root@kali:~# svnrdump -h
general usage: svnrdump SUBCOMMAND URL [-r LOWER[:UPPER]]
Subversion remote repository dump and load tool.
Type 'svnrdump help <subcommand>' for help on a specific subcommand.
Type 'svnrdump --version' to see the program version and RA modules.
Available subcommands:
   dump
   load
   help (?, h)
```

### `svnserve`

官方给出的调用示例：`svnserve -h`

```text
root@kali:~# svnserve -h
usage: svnserve [-d | -i | -t | -X] [options]
Subversion repository server.
Type 'svnserve --version' to see the program version.
Valid options:
  -d [--daemon]            : daemon mode
  -i [--inetd]             : inetd mode
  -t [--tunnel]            : tunnel mode
  -X [--listen-once]       : listen-once mode (useful for debugging)
  -r [--root] ARG          : root of directory to serve
  -R [--read-only]         : force read only, overriding repository config file
  --config-file ARG        : read configuration from file ARG
  --listen-port ARG        : listen port. The default port is 3690.
                             [mode: daemon, listen-once]
  --listen-host ARG        : listen hostname or IP address
                             By default svnserve listens on all addresses.
                             [mode: daemon, listen-once]
  -6 [--prefer-ipv6]       : prefer IPv6 when resolving the listen hostname
                             [IPv4 is preferred by default. Using IPv4 and IPv6
                             at the same time is not supported in daemon mode.
                             Use inetd mode or tunnel mode if you need this.]
  -c [--compression] ARG   : compression level to use for network transmissions
                             [0 .. no compression, 5 .. default,
                              9 .. maximum compression]
  -M [--memory-cache-size] ARG : size of the extra in-memory cache in MB used to
                             minimize redundant operations.
                             Default is 16.
                             0 switches to dynamically sized caches.
                             [used for FSFS and FSX repositories only]
  --cache-txdeltas ARG     : enable or disable caching of deltas between older
                             revisions.
                             Default is yes.
                             [used for FSFS and FSX repositories only]
  --cache-fulltexts ARG    : enable or disable caching of file contents
                             Default is yes.
                             [used for FSFS and FSX repositories only]
  --cache-revprops ARG     : enable or disable caching of revision properties.
                             Consult the documentation before activating this.
                             Default is no.
                             [used for FSFS and FSX repositories only]
  --cache-nodeprops ARG    : enable or disable caching of node properties
                             Default is yes.
                             [used for FSFS repositories only]
  --client-speed ARG       : Optimize network handling based on the assumption
                             that most clients are connected with a bitrate of
                             ARG Mbit/s.
                             Default is 0 (optimizations disabled).
  --block-read ARG         : Parse and cache all data found in block instead
                             of just the requested item.
                             Default is no.
                             [used for FSFS repositories in 1.9 format only]
  -T [--threads]           : use threads instead of fork [mode: daemon]
  --min-threads ARG        : Minimum number of server threads, even if idle.
                             Capped to max-threads; minimum value is 0.
                             Default is 1.
                             [used only with --threads]
  --max-threads ARG        : Maximum number of server threads, even if there
                             are more connections.  Minimum value is 1.
                             Default is 256.
                             [used only with --threads]
  --max-request-size ARG   : Maximum acceptable size of a client request in MB.
                             This implicitly limits the length of paths and
                             property values that can be sent to the server.
                             Also the peak memory usage for protocol handling
                             per server thread or sub-process.
                             0 disables the size check; default is 16.
  --max-response-size ARG  : Maximum acceptable server response size in MB.
                             Longer responses get truncated and return an
                             error.  This limits the server load e.g. when
                             checking out at the wrong path level.
                             Default is 0 (disabled).
  --foreground             : run in foreground (useful for debugging)
                             [mode: daemon]
  --single-thread          : handle one connection at a time in the parent
                             process (useful for debugging)
  --log-file ARG           : svnserve log file
  --pid-file ARG           : write server process ID to file ARG
                             [mode: daemon, listen-once]
  --tunnel-user ARG        : tunnel username (default is current uid's name)
                             [mode: tunnel]
  -h [--help]              : display this help
  --virtual-host           : virtual host mode (look for repo in directory
                             of provided hostname)
  --version                : show program version information
  -q [--quiet]             : no progress (only errors) to stderr
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install subversion`，再执行 `libapache2-mod-svn --version` 2>/dev/null || `libapache2-mod-svn -V`
- [ ] **2.** **读官方帮助** —— `libapache2-mod-svn -h`，需要细节时 `man libapache2-mod-svn`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `libapache2-mod-svn -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/subversion/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/subversion/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/subversion/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
