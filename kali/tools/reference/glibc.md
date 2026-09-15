# glibc

> GNU C Library: Documentation Contains the complete GNU C Library ChangeLog. The GNU C Library Reference manual has been moved into glibc-doc-reference for licensing reasons.

> **功能分类**：信息搜集 ｜ **Kali 包**：`glibc` ｜ **官方文档**：<https://www.kali.org/tools/glibc/>

## 1. 安装

```bash
sudo apt update
sudo apt install glibc-doc
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.43 |
| 架构 | any |
| 可执行命令 | `glibc-doc`、`glibc-source`、`libc-bin`、`getconf`、`getent`、`iconv`、`iconvconfig`、`ld.so`、`ldconfig`、`ldd`、`locale`、`localedef`、`pldd`、`tzselect`、`zdump`、`zic`、`libc-dev-bin`、`gencat`、`libc-devtools`、`memusage`、`memusagestat`、`mtrace`、`sotruss`、`sprof`、`libc-gconv-modules-extra`、`libc-l10n`、`libc0.3`、`libc0.3-dbg`、`libc0.3-dev`、`libc0.3-udeb`、`libc6`、`libc6-amd64`、`libc6-dbg`、`libc6-dev`、`libc6-dev-amd64`、`libc6-dev-i386`、`libc6-dev-mips32`、`libc6-dev-mips64`、`libc6-dev-mipsn32`、`libc6-dev-powerpc`、`libc6-dev-ppc64`、`libc6-dev-sparc`、`libc6-dev-sparc64`、`libc6-dev-x32`、`libc6-i386`、`libc6-mips32`、`libc6-mips64`、`libc6-mipsn32`、`libc6-powerpc`、`libc6-ppc64`、`libc6-sparc`、`libc6-sparc64`、`libc6-udeb`、`libc6-x32`、`libc6.1`、`libc6.1-dbg`、`libc6.1-dev`、`libc6.1-udeb`、`locales`、`locale-gen`、`update-locale`、`validlocale`、`locales-all`、`nscd` |
| 依赖 | `libc6`、`getconf` |
| 安装体积 | 3.83 MB |
| 官网 | <https://www.gnu.org/software/libc/libc.html> |
| 源码仓库 | <https://salsa.debian.org/glibc-team/glibc> |
| 包追踪 | <https://pkg.kali.org/pkg/glibc> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
glibc-doc -h          # 查看用法
man glibc-doc         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 64 个可执行命令，下面是官方页面内嵌的帮助原文。

### `getconf`

官方给出的调用示例：`getconf --help`

```text
root@kali:~# getconf --help
Usage: getconf [-v SPEC] VAR
  or:  getconf [-v SPEC] PATH_VAR PATH
Get the configuration value for variable VAR, or for variable PATH_VAR
for path PATH.  If SPEC is given, give values for compilation
environment SPEC.
For bug reporting instructions, please see:
<http://www.debian.org/Bugs/>.
```

### `getent`

官方给出的调用示例：`getent --help`

```text
root@kali:~# getent --help
Usage: getent [OPTION...] database [key ...]
Get entries from administrative database.
  -A, --no-addrconfig        do not filter out unsupported IPv4/IPv6 addresses
                             (with ahosts*)
  -i, --no-idn               disable IDN encoding
  -s, --service=CONFIG       Service configuration to be used
  -?, --help                 Give this help list
      --usage                Give a short usage message
  -V, --version              Print program version
Mandatory or optional arguments to long options are also mandatory or optional
for any corresponding short options.
Supported databases:
ahosts ahostsv4 ahostsv6 aliases ethers group gshadow hosts initgroups
netgroup networks passwd protocols rpc services shadow
For bug reporting instructions, please see:
<http://www.debian.org/Bugs/>.
```

### `iconv`

官方给出的调用示例：`iconv --help`

```text
root@kali:~# iconv --help
Usage: iconv [OPTION...] [FILE...]
Convert encoding of given files from one encoding to another.
 Input/Output format specification:
  -f, --from-code=NAME       encoding of original text
  -t, --to-code=NAME         encoding for output
 Information:
  -l, --list                 list all known coded character sets
 Output control:
  -c                         omit invalid characters from output
  -o, --output=FILE          output file
  -s, --silent               suppress warnings
      --verbose              print progress information
  -?, --help                 Give this help list
      --usage                Give a short usage message
  -V, --version              Print program version
Mandatory or optional arguments to long options are also mandatory or optional
for any corresponding short options.
For bug reporting instructions, please see:
<http://www.debian.org/Bugs/>.
```

### `iconvconfig`

官方给出的调用示例：`iconvconfig --help`

```text
root@kali:~# iconvconfig --help
Usage: iconvconfig [OPTION...] [DIR...]
Create fastloading iconv module configuration file.
      --nostdlib             Do not search standard directories, only those on
                             the command line
  -o, --output=FILE          Put output in FILE instead of installed location
                             (--prefix does not apply to FILE)
      --prefix=PATH          Prefix used for all file accesses
  -?, --help                 Give this help list
      --usage                Give a short usage message
  -V, --version              Print program version
Mandatory or optional arguments to long options are also mandatory or optional
for any corresponding short options.
For bug reporting instructions, please see:
<http://www.debian.org/Bugs/>.
```

### `ld.so`

官方给出的调用示例：`ld.so --help`

```text
root@kali:~# ld.so --help
Usage: ld.so [OPTION]... EXECUTABLE-FILE [ARGS-FOR-PROGRAM...]
You have invoked 'ld.so', the program interpreter for dynamically-linked
ELF programs.  Usually, the program interpreter is invoked automatically
when a dynamically-linked executable is started.
You may invoke the program interpreter program directly from the command
line to load and run an ELF executable file; this is like executing that
file itself, but always uses the program interpreter you invoked,
instead of the program interpreter specified in the executable file you
run.  Invoking the program interpreter directly provides access to
additional diagnostics, and changing the dynamic linker behavior without
setting environment variables (which would be inherited by subprocesses).
  --list                list all dependencies and how they are resolved
  --verify              verify that given object really is a dynamically linked
                        object we can handle
  --inhibit-cache       Do not use /etc/ld.so.cache
  --library-path PATH   use given PATH instead of content of the environment
                        variable LD_LIBRARY_PATH
  --glibc-hwcaps-prepend LIST
                        search glibc-hwcaps subdirectories in LIST
  --glibc-hwcaps-mask LIST
                        only search built-in subdirectories if in LIST
  --inhibit-rpath LIST  ignore RUNPATH and RPATH information in object names
                        in LIST
  --audit LIST          use objects named in LIST as auditors
  --preload LIST        preload objects named in LIST
  --argv0 STRING        set argv[0] to STRING before running
  --list-tunables       list all tunables with minimum and maximum values
  --list-diagnostics    list diagnostics information
  --help                display this help and exit
  --version             output version information and exit
This program interpreter self-identifies as: /lib64/ld-linux-x86-64.so.2
Shared library search path:
  (libraries located via /etc/ld.so.cache)
  /lib/x86_64-linux-gnu (system search path)
  /usr/lib/x86_64-linux-gnu (system search path)
  /lib (system search path)
  /usr/lib (system search path)
Subdirectories of glibc-hwcaps directories, in priority order:
  x86-64-v4
  x86-64-v3
  x86-64-v2 (supported, searched)
```

### `ldconfig`

官方给出的调用示例：`ldconfig --help`

```text
root@kali:~# ldconfig --help
Usage: ldconfig [OPTION...]
Configure Dynamic Linker Run Time Bindings.
  -c, --format=FORMAT        Format to use: new (default), old, or compat
  -C CACHE                   Use CACHE as cache file
  -f CONF                    Use CONF as configuration file
  -i, --ignore-aux-cache     Ignore auxiliary cache file
  -l                         Manually link individual libraries.
  -n                         Only process directories specified on the command
                             line.  Don't build cache.
  -N                         Don't build cache
  -p, --print-cache          Print cache
  -r ROOT                    Change to and use ROOT as root directory
  -v, --verbose              Generate verbose messages
  -X                         Don't update symbolic links
  -?, --help                 Give this help list
      --usage                Give a short usage message
  -V, --version              Print program version
Mandatory or optional arguments to long options are also mandatory or optional
for any corresponding short options.
For bug reporting instructions, please see:
<http://www.debian.org/Bugs/>.
```

### `ldd`

官方给出的调用示例：`ldd --help`

```text
root@kali:~# ldd --help
Usage: ldd [OPTION]... FILE...
      --help              print this help and exit
      --version           print version information and exit
  -d, --data-relocs       process data relocations
  -r, --function-relocs   process data and function relocations
  -u, --unused            print unused direct dependencies
  -v, --verbose           print all information
For bug reporting instructions, please see:
<http://www.debian.org/Bugs/>.
```

### `locale`

官方给出的调用示例：`locale --help`

```text
root@kali:~# locale --help
Usage: locale [OPTION...] NAME
  or:  locale [OPTION...] [-a|-m]
Get locale-specific information.
 System information:
  -a, --all-locales          Write names of available locales
  -m, --charmaps             Write names of available charmaps
 Modify output format:
  -c, --category-name        Write names of selected categories
  -k, --keyword-name         Write names of selected keywords
  -v, --verbose              Print more information
  -?, --help                 Give this help list
      --usage                Give a short usage message
  -V, --version              Print program version
For bug reporting instructions, please see:
<http://www.debian.org/Bugs/>.
```

### `localedef`

官方给出的调用示例：`localedef --help`

```text
root@kali:~# localedef --help
Usage: localedef [OPTION...] NAME
  or:  localedef [OPTION...] [--add-to-archive|--delete-from-archive] FILE...
  or:  localedef [OPTION...] --list-archive [FILE]
Compile locale specification
 Input Files:
  -f, --charmap=FILE         Symbolic character names defined in FILE
  -i, --inputfile=FILE       Source definitions are found in FILE
  -u, --repertoire-map=FILE  FILE contains mapping from symbolic names to UCS4
                             values
 Output control:
  -c, --force                Create output even if warning messages were issued
      --no-hard-links        Do not create hard links between installed
                             locales
      --no-warnings=<warnings>   Comma-separated list of warnings to disable;
                             supported warnings are: ascii, intcurrsym
      --posix                Strictly conform to POSIX
      --prefix=PATH          Optional output file prefix
      --quiet                Suppress warnings and information messages
  -v, --verbose              Print more messages
      --warnings=<warnings>  Comma-separated list of warnings to enable;
                             supported warnings are: ascii, intcurrsym
 Archive control:
      --add-to-archive       Add locales named by parameters to archive
  -A, --alias-file=FILE      locale.alias file to consult when making archive
      --big-endian           Generate big-endian output
      --delete-from-archive  Remove locales named by parameters from archive
      --list-archive         List content of archive
      --little-endian        Generate little-endian output
      --no-archive           Don't add new data to archive
      --replace              Replace existing archive content
  -?, --help                 Give this help list
      --usage                Give a short usage message
  -V, --version              Print program version
Mandatory or optional arguments to long options are also mandatory or optional
for any corresponding short options.
System's directory for character maps : /usr/share/i18n/charmaps
		       repertoire maps: /usr/share/i18n/repertoiremaps
		       locale path    : /usr/lib/locale:/usr/share/i18n
For bug reporting instructions, please see:
<http://www.debian.org/Bugs/>.
```

### `pldd`

官方给出的调用示例：`pldd --help`

```text
root@kali:~# pldd --help
Usage: pldd [OPTION...] PID
List dynamic shared objects loaded into process.
  -?, --help                 Give this help list
      --usage                Give a short usage message
  -V, --version              Print program version
For bug reporting instructions, please see:
<http://www.debian.org/Bugs/>.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install glibc-doc`，再执行 `glibc-doc --version` 2>/dev/null || `glibc-doc -V`
- [ ] **2.** **读官方帮助** —— `glibc-doc -h`，需要细节时 `man glibc-doc`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: getconf [-v SPEC] VAR`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/glibc/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/glibc/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/glibc/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
