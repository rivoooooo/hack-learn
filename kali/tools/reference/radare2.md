# radare2

> Free and advanced command line hexadecimal editor The project aims to create a complete, portable, multi-architecture, unix-like toolchain for reverse engineering. It is composed by an hexadecimal editor (radare) with a wrapped IO layer su…

> **功能分类**：数字取证 ｜ **Kali 包**：`radare2` ｜ **官方文档**：<https://www.kali.org/tools/radare2/>

## 1. 安装

```bash
sudo apt update
sudo apt install radare2
```

| 项目 | 内容 |
|------|------|
| 版本 | 6.0.4 |
| 架构 | any |
| 可执行命令 | `libradare2-6.0.0t64`、`libradare2-common`、`libradare2-dev`、`radare2`、`r2`、`r2agent`、`r2pm`、`r2r`、`r2sdb`、`rabin2`、`radiff2`、`rafind2`、`ragg2`、`rahash2`、`rapatch2`、`rarun2`、`rasign2`、`rasm2`、`ravc2`、`rax2` |
| 依赖 | `libc6`、`libradare2-6.0.0t64`、`r2` |
| 安装体积 | 3.58 MB |
| 官网 | <https://www.radare.org> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/radare2> |
| 包追踪 | <https://pkg.kali.org/pkg/radare2> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libradare2-6.0.0t64 -h          # 查看用法
man libradare2-6.0.0t64         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 20 个可执行命令，下面是官方页面内嵌的帮助原文。

### `r2`

官方给出的调用示例：`r2 -h`

```text
root@kali:~# r2 -h
Usage: r2 [-ACdfjLMnNqStuvwzX] [-P patch] [-p prj] [-a arch] [-b bits] [-c cmd]
          [-s addr] [-B baddr] [-m maddr] [-i script] [-e k=v] file|pid|-|--|=
 --           run radare2 without opening any file
 -            same as 'r2 malloc://512'
 =            read file from stdin (use -i and -c to run cmds)
 -=           perform !=! command to run all commands remotely
 -0           print \x00 after init and every command
 -1           redirect stderr to stdout
 -2           close stderr file descriptor (silent warning messages)
 -a [arch]    set asm.arch
 -A           run 'aaa' command to analyze all referenced code
 -b [bits]    set asm.bits
 -B [baddr]   set base address for PIE binaries
 -c 'cmd..'   execute radare command
 -C           file is host:port (alias for -c+=http://%s/cmd/)
 -d           debug the executable 'file' or running process 'pid'
 -D [backend] enable debug mode (e cfg.debug=true)
 -e k=v       evaluate config var
 -f           block size = file size
 -F [binplug] force to use that rbin plugin
 -h, -hh      show help message, -hh for long
 -H ([var])   display variable
 -i [file]    run rlang program, r2script file or load plugin
 -I [file]    run script file before the file is opened
 -j           use json for -v, -L and maybe others
 -k [OS/kern] set asm.os (linux, macos, w32, netbsd, ...)
 -L, -LL      list supported IO plugins (-LL list core plugins)
 -m [addr]    map file at given address (loadaddr)
 -M           do not demangle symbol names
 -n, -nn      do not load RBin info (-nn only load bin structures)
 -N           do not load user settings and scripts
 -NN          do not load any script or plugin
 -q           quiet mode (no prompt) and quit after -i
 -qq          quit after running all -c and -i
 -Q           quiet mode (no prompt) and quit faster (quickLeak=true)
 -p [prj]     use project, list if no arg, load if no file
 -P [file]    apply rapatch file and quit
 -r [rarun2]  specify rarun2 profile to load (same as -e dbg.profile=X)
 -R [rr2rule] specify custom rarun2 directive (uses base64 dbg.profile)
 -s [addr]    initial seek
 -S           start r2 in sandbox mode
 -t           load rabin2 info in thread
 -u           set bin.filter=false to get raw sym/sec/cls names
 -v, -V       show radare2 version (-V show lib versions)
 -w           open file in write mode
 -x           open without exec-flag (asm.emu will not work), See io.exec
 -X           same as -e bin.usextr=false (useful for dyldcache)
 -z, -zz      do not load strings or load them even in raw
```

### `r2agent`

官方给出的调用示例：`r2agent -h`

```text
root@kali:~# r2agent -h
Usage: r2agent [-adhsLjv] [-p port]
  -a        listen for everyone (localhost by default)
  -d        run in daemon mode (background)
  -h        show this help message
  -s        run in sandbox mode
  -u        enable http authorization access
  -t        user:password authentication file
  -p [port] specify listening port (defaults to 8080)
  -L        list currently loaded r2 sessions and exit
  -v        show r2 version information and exit
  -j        output JSON when used with -v or -L
```

### `r2pm`

官方给出的调用示例：`r2pm -h`

```text
root@kali:~# r2pm -h
Usage: r2pm [-flags] [pkgs...]
Commands:
 -a [repository]   add or -delete external repository
 -c ([git/dir])    clear source cache (R2PM_GITDIR)
 -ci <pkgname>     clean + install
 -cp               clean the user's home plugin directory
 -d,doc [pkgname]  show documentation and source for given package
 -e [pkgname]      edit using $EDITOR the given package script
 -f                force operation (Use in combination of -U, -i, -u, ..)
 -gi <pkg>         global install (system-wide)
 -h                display this help message
 -H ([variable])   list all or selected r2pm environment variables
 -i <pkgname>      install/update package and its dependencies (see -c, -g)
 -I                information about the repository and installed packages
 -j                json output
 -l                list installed packages
 -q                be quiet
 -r [cmd ...args]  run shell command with R2PM_BINDIR in PATH
 -R <pkgname>      reload plugin (See R2PM_RELOAD code block package)
 -s [<keyword>]    search available packages in database matching a string
 -t [YYYY-MM-DD]   set a moment in time to pull the code from the git packages
 -u <pkgname>      uninstall package (see -f to force uninstall)
 -uci <pkgname>    uninstall + clean + install
 -ui <pkgname>     uninstall + install
 -U                download/initialize or update database (-f for a clean clone)
 -UU               same as -U but upgrade all the installed r2 plugins
 -v                show version
```

### `r2r`

官方给出的调用示例：`r2r -h`

```text
root@kali:~# r2r -h
Usage: r2r [-qvVnLi] [-C dir] [-F dir] [-f file] [-o file] [-s test] [-t seconds] [-j threads] [test file/dir | @test-type]
 -C [dir]     chdir before running r2r (default follows executable symlink + test/new
 -F [dir]     run fuzz tests (open and default analysis) on all files in the given dir
 -L           log mode (better printing for CI, logfiles, etc.)
 -V           verbose
 -f [file]    file to use for json tests (default is bins/elf/crackme0x00b)
 -g           run the tests specified via '// R2R' comments in modified source files
 -h           print this help
 -H           display environment variables
 -i           interactive mode
 -j [threads] how many threads to use for running tests concurrently (default is 8)
 -n           do nothing (don't run any test, just load/parse them)
 -o [file]    output test run information in JSON format to file
 -q           quiet
 -s [test]    set R2R_SKIP_(TEST)=1 to skip running that test type
 -S [0-100]   set R2R_SHALLOW=N to skip a random percentage of tests
 -t [seconds] timeout per test (default is (60*60))
 -u           do not git pull/clone test/bins (See R2R_OFFLINE)
 -v           show version
R2R_SKIP_ARCHOS=0  # do not run the arch-os-specific tests
R2R_SKIP_JSON=0    # do not run the JSON tests
R2R_SKIP_FUZZ=0    # do not run the fuzz tests
R2R_SKIP_UNIT=0    # do not run the unit tests
R2R_SKIP_CMD=0     # do not run the cmds tests
R2R_SKIP_ASM=0     # do not run the rasm2 tests
R2R_JOBS=8         # maximum parallel jobs
R2R_TIMEOUT=3600   # timeout after 1 minute (60 * 60)
R2R_OFFLINE=0      # same as passing -u
R2R_SHALLOW=0      # skip 0-100% random tests
R2R_RADARE2=radare2 # radare2 binary to launch
Supported test types: @asm @json @unit @fuzz @arch @cmd
OS/Arch for archos tests: linux-x86_64
```

### `r2sdb`

官方给出的调用示例：`r2sdb -h`

```text
root@kali:~# r2sdb -h
usage: sdb [-0cCdDehjJrtv|-D A B] [-|db] [.file]|[-=]|==||[-+][(idx)key[:json|=value] ..]
  -0      terminate results with \x00
  -c      count the number of keys database
  -C      create foo.{c,h} for embedding (uses gperf)
  -d      decode base64 from stdin
  -D      diff two databases
  -e      encode stdin as base64
  -g [..] grep expression
  -G      print database in gperf format
  -h      show this help
  -j      output in json
  -o [f]  output file name for -C -t
  -J      enable journaling
  -r      process .sdb.txt files in the given path
  -t      use textmode (for -C)
  -v      show version information
usage: sdb [-0cCdDehjJrtv|-D A B] [-|db] [.file]|[-=]|==||[-+][(idx)key[:json|=value] ..]
```

### `rabin2`

官方给出的调用示例：`rabin2 -h`

```text
root@kali:~# rabin2 -h
Usage: rabin2 [-AcdeEghHiIjJlLMqrRsSUvVxzZ] [-@ at] [-a arch] [-b bits] [-B addr]
              [-C F:C:D] [-f str] [-m addr] [-n str] [-N m:M] [-P[-P] pdb]
              [-o str] [-O help] [-k query] [-D lang mangledsymbol] file
 -@ [addr]       show section, symbol or import at addr
 -A              list sub-binaries and their arch-bits pairs
 -a [arch]       set arch (x86, arm, .. or <arch>_<bits>)
 -b [bits]       set bits (32, 64 ...)
 -B [addr]       override base address (pie bins)
 -c              list classes
 -cc             list classes in header format
 -C [fmt:C:D]    create [elf,mach0,pe] with Code and Data hexpairs (see -a)
 -d              show debug/dwarf information
 -D lang name    demangle symbol name (-D all for bin.demangle=true)
 -e              program entrypoint
 -ee             constructor/destructor entrypoints
 -E              globally exportable symbols
 -f [str]        select sub-bin named str
 -F [binfmt]     force to use that bin plugin (ignore header check)
 -g              same as -SMZIHVResizcld -SS -SSS -ee (show all info)
 -G [addr]       load address . address to header
 -h              this help message
 -H              header fields
 -i              imports (symbols imported from libraries)
 -I              binary info
 -j              output in json
 -J ([var])      display variable
 -k [sdb-query]  run sdb query. for example: '*'
 -K [algo]       calculate checksums (md5, sha1, ..)
 -l              linked libraries
 -L [plugin]     list supported bin plugins or plugin details
 -m [addr]       show source line at addr
 -M              main (show address of main symbol)
 -n [str]        show section, symbol or import named str
 -N [min:max]    force min:max number of chars per string (see -z and -zz)
 -o [str]        output file/folder for write operations (out by default)
 -O [str]        write/extract operations (-O help)
 -p              show always physical addresses
 -P              show debug/pdb information
 -PP             download pdb file for binary
 -q              be quiet, just show fewer data
 -qq             show less info (no addr/size for -z for ex.)
 -Q              show load address used by dlopen (non-aslr libs)
 -r              radare output
 -R              relocations
 -s              symbols
 -S              sections
 -SS             segments
 -SSS            sections mapping to segments
 -t              display file hashes
 -T              display file signature
 -u              unfiltered (no rename duplicated symbols/sections)
 -U              resoUrces
 -v              display version and quit
 -V              show binary version information
 -w              display try/catch blocks
 -x              extract bins contained in file
 -X [fmt] [f] .. package in fat or zip the given files and bins contained in file
 -z              strings (from data section)
 -zz             strings (from raw bins [e bin.str.raw=1])
 -zzz            dump raw strings to stdout (for huge files)
 -Z              guess size of binary program
Environment:
R2_NOPLUGINS	                      # same as r2 -N. Dont load shared plugins
RABIN2_ARGS	                      # ignore cli and use these program arguments
RABIN2_CHARSET	e cfg.charset         # set default value charset for -z strings
RABIN2_CODESIGN_VERBOSE	                      # show codesign details at parse time
RABIN2_DEBASE64	e bin.str.debase64    # try to debase64 all strings
RABIN2_DEMANGLE	e bin.demangle        # dont demangle symbols if value is 0
RABIN2_DEMANGLE_CMD	e bin.demangle.cmd    # try to purge false positives
RABIN2_DEMANGLE_TRYLIB	e bin.demangle.trylib # load Swift libs to demangle (default: false)
RABIN2_LANG	e bin.lang            # assume lang for demangling
RABIN2_MACHO_NOFUNCSTARTS	                      # if set it will ignore the FUNCSTART information
RABIN2_MACHO_NOSWIFT	                      # avoid parsing the swift metadata
RABIN2_MACHO_SKIPFIXUPS	                      # do not parse the mach-o chained fixups
RABIN2_MAXSTRBUF	e bin.str.maxbuf      # specify maximum buffer size
RABIN2_PDBSERVER	e pdb.server          # use alternative PDB server
RABIN2_PREFIX	e bin.prefix          # prefix symbols/sections/relocs with a specific string
RABIN2_STRFILTER	e bin.str.filter      # r2 -qc 'e bin.str.filter=??' -
RABIN2_STRPURGE	e bin.str.purge       # try to purge false positives
RABIN2_SYMSTORE	e pdb.symstore        # path to downstream symbol store
RABIN2_VERBOSE	e bin.verbose         # show debugging messages from the parser
```

### `radare2`

官方给出的调用示例：`radare2 -h`

```text
root@kali:~# radare2 -h
Usage: r2 [-ACdfjLMnNqStuvwzX] [-P patch] [-p prj] [-a arch] [-b bits] [-c cmd]
          [-s addr] [-B baddr] [-m maddr] [-i script] [-e k=v] file|pid|-|--|=
 --           run radare2 without opening any file
 -            same as 'r2 malloc://512'
 =            read file from stdin (use -i and -c to run cmds)
 -=           perform !=! command to run all commands remotely
 -0           print \x00 after init and every command
 -1           redirect stderr to stdout
 -2           close stderr file descriptor (silent warning messages)
 -a [arch]    set asm.arch
 -A           run 'aaa' command to analyze all referenced code
 -b [bits]    set asm.bits
 -B [baddr]   set base address for PIE binaries
 -c 'cmd..'   execute radare command
 -C           file is host:port (alias for -c+=http://%s/cmd/)
 -d           debug the executable 'file' or running process 'pid'
 -D [backend] enable debug mode (e cfg.debug=true)
 -e k=v       evaluate config var
 -f           block size = file size
 -F [binplug] force to use that rbin plugin
 -h, -hh      show help message, -hh for long
 -H ([var])   display variable
 -i [file]    run rlang program, r2script file or load plugin
 -I [file]    run script file before the file is opened
 -j           use json for -v, -L and maybe others
 -k [OS/kern] set asm.os (linux, macos, w32, netbsd, ...)
 -L, -LL      list supported IO plugins (-LL list core plugins)
 -m [addr]    map file at given address (loadaddr)
 -M           do not demangle symbol names
 -n, -nn      do not load RBin info (-nn only load bin structures)
 -N           do not load user settings and scripts
 -NN          do not load any script or plugin
 -q           quiet mode (no prompt) and quit after -i
 -qq          quit after running all -c and -i
 -Q           quiet mode (no prompt) and quit faster (quickLeak=true)
 -p [prj]     use project, list if no arg, load if no file
 -P [file]    apply rapatch file and quit
 -r [rarun2]  specify rarun2 profile to load (same as -e dbg.profile=X)
 -R [rr2rule] specify custom rarun2 directive (uses base64 dbg.profile)
 -s [addr]    initial seek
 -S           start r2 in sandbox mode
 -t           load rabin2 info in thread
 -u           set bin.filter=false to get raw sym/sec/cls names
 -v, -V       show radare2 version (-V show lib versions)
 -w           open file in write mode
 -x           open without exec-flag (asm.emu will not work), See io.exec
 -X           same as -e bin.usextr=false (useful for dyldcache)
 -z, -zz      do not load strings or load them even in raw
```

### `radiff2`

官方给出的调用示例：`radiff2 -h`

```text
root@kali:~# radiff2 -h
Usage: radiff2 [-options] [-A[A]] [-B #] [-g sym] [-m graph_mode][-t %] [file] [file]
  -a [arch]  specify architecture plugin to use (x86, arm, ..)
  -A [-A]    run aaa or aaaa after loading each binary (see -C)
  -b [bits]  specify register size for arch (16 (thumb), 32, 64, ..)
  -B [baddr] define the base address to add the offsets when listing
  -c [cmd]   run given command on every RCore instance
  -C         graphdiff code (columns: off-A, match-ratio, off-B) (see -A)
  -d         use delta diffing
  -D         show disasm instead of hexpairs
  -e [k=v]   set eval config var value for all RCore instances
  -f [help]  select output format (see '-f help' for details)
  -g [arg]   graph diff of [sym] or functions in [off1,off2]
  -i [help]  compare bin information (symbols, strings, classes, ..)
  -j         output in json format (see -f json)
  -l [addr]  specify final offset (length) for diffing, same format as -o
  -m [mode]  choose the graph output mode (aditsjJ)
  -n         count of changes
  -o [addr]  specify initial offset for diffing, can use A:B format
  -O         code diffing with opcode bytes only
  -p         use physical addressing (io.va=false) (only for radiff2 -AC)
  -q         quiet mode (disable colors, reduce output)
  -r         output in radare commands
  -s         compute edit distance (no substitution, Eugene W. Myers O(ND) diff algorithm)
  -ss        compute Levenshtein edit distance (substitution is allowed, O(N^2))
  -S [name]  sort code diff (name, namelen, addr, size, type, dist) (only for -C or -g)
  -t [0-100] set threshold for code diff (default is 70%)
  -T         analyze files in threads (EXPERIMENTAL, 30% faster and crashy)
  -x         show two column hexdump diffing
  -X         use xpatch format for the diffing output
  -u         unified output (---+++)
  -U         unified output using system 'diff'
  -v         show version information
  -V         be verbose (current only for -s)
```

### `rafind2`

官方给出的调用示例：`rafind2 -h`

```text
root@kali:~# rafind2 -h
Usage: rafind2 [-mBXnzZhqv] [-a align] [-b sz] [-f/t from/to] [-[e|s|S] str] [-x hex] -|file|dir ..
 -a [align] only accept aligned hits
 -b [size]  set block size
 -B         use big endian instead of the little one (See -V)
 -c         disable colourful output (mainly for for -X)
 -e [regex] search for regex matches (can be used multiple times)
 -E         perform a search using an esil expression
 -f [from]  start searching from address 'from'
 -F [file]  read the contents of the file and use it as keyword
 -h         show this help
 -i         identify filetype (r2 -nqcpm file)
 -j         output in JSON
 -L         list all io plugins (same as r2 for now)
 -m         magic search, file-type carver
 -M [str]   set a binary mask to be applied on keywords
 -n         do not stop on read errors
 -r         print using radare commands
 -s [str]   search for a string (more than one string can be passed)
 -S [str]   search for a wide string (more than one string can be passed).
 -t [to]    stop search at address 'to'
 -q         quiet: fewer output do not show headings or filenames.
 -v         print version and exit
 -V [s:num | s:num1,num2] search for a value or range in the specified endian (-V 4:123 or -V 4:100,200)
 -x [hex]   search for hexpair string (909090) (can be used multiple times)
 -X         show hexdump of search results
 -z         search for zero-terminated strings
 -Z         show string found on each search hit
```

### `ragg2`

官方给出的调用示例：`ragg2 -h`

```text
root@kali:~# ragg2 -h
Usage: ragg2 [-FOLsrxhvz] [-a arch] [-b bits] [-k os] [-o file] [-I path]
             [-i sc] [-E enc] [-B hex] [-c k=v] [-C file] [-p pad] [-q off]
             [-S string] [-f fmt] [-nN dword] [-dDw off:hex] [-e expr] file|f.asm|-
 -a [arch]       select architecture (x86, mips, arm)
 -b [bits]       register size (32, 64, ..)
 -B [hexpairs]   append some hexpair bytes
 -c [k=v]        set configuration options
 -C [file]       append contents of file
 -d [off:dword]  patch dword (4 bytes) at given offset
 -D [off:qword]  patch qword (8 bytes) at given offset
 -e [egg-expr]   take egg program from string instead of file
 -E [encoder]    use specific encoder. see -L
 -f [format]     output format (raw, c, pe, elf, mach0, python, javascript)
 -F              output native format (osx=mach0, linux=elf, ..)
 -h              show this help
 -H ([var])      display variable
 -i [shellcode]  include shellcode plugin, uses options. see -L
 -I [path]       add include path
 -k [os]         operating system's kernel (linux,bsd,osx,w32)
 -L              list all plugins (shellcodes and encoders)
 -n [dword]      append 32bit number (4 bytes)
 -N [dword]      append 64bit number (8 bytes)
 -o [file]       output file
 -O              use default output file (filename without extension or a.out)
 -p [padding]    add padding after compilation (padding=n10s32)
                 ntas : begin nop, trap, 'a', sequence
                 NTAS : same as above, but at the end
 -P [size]       prepend debruijn pattern
 -q [fragment]   debruijn pattern offset
 -r              show raw bytes instead of hexpairs
 -s              show assembler
 -S [string]     append a string
 -v              show version
 -w [off:hex]    patch hexpairs at given offset
 -x              execute
 -X [hexpairs]   execute rop chain, using the stack provided
 -z              output in C string syntax
R2_NOPLUGINS	do not load any plugin
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install radare2`，再执行 `libradare2-6.0.0t64 --version` 2>/dev/null || `libradare2-6.0.0t64 -V`
- [ ] **2.** **读官方帮助** —— `libradare2-6.0.0t64 -h`，需要细节时 `man libradare2-6.0.0t64`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: r2 [-ACdfjLMnNqStuvwzX] [-P patch] [-p prj] [-a arch] [-b bits] [-c cmd]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/radare2/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[radare2](../../tools/tutorials/10-逆向工程/radare2.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/radare2/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/radare2/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
