# rizin

> Reverse engineering framework and command-line toolset Rizin is a fork of the radare2 reverse engineering framework with a focus on usability, working features and code cleanliness. Rizin is portable and it can be used to analyze binaries,…

> **功能分类**：数字取证 ｜ **Kali 包**：`rizin` ｜ **官方文档**：<https://www.kali.org/tools/rizin/>

## 1. 安装

```bash
sudo apt update
sudo apt install rizin
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.9.1 |
| 架构 | any |
| 可执行命令 | `librizin-common`、`librizin-dev`、`librizin0`、`rizin`、`rz-ar`、`rz-asm`、`rz-ax`、`rz-bin`、`rz-diff`、`rz-find`、`rz-gg`、`rz-hash`、`rz-run`、`rz-sign`、`rz-test` |
| 依赖 | `libc6`、`librizin0` |
| 安装体积 | 334 KB |
| 官网 | <https://rizin.re/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/rizin> |
| 包追踪 | <https://pkg.kali.org/pkg/rizin> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
librizin-common -h          # 查看用法
man librizin-common         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 15 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rizin`

> 官方示例调用：`rizin -h`

```text
root@kali:~# rizin -h
Usage: rizin [-ACdfLMnNqStuvwzX] [-P patch] [-p prj] [-a arch] [-b bits] [-i file]
             [-s addr] [-B baddr] [-m maddr] [-c cmd] [-e k=v] file|pid|-|--|=
 --         Run rizin without opening any file
 =          Same as 'rizin malloc://512'
 -          Read file from stdin
 -=         Perform R=! command to run all commands remotely
 -0         Print \x00 after init and every command
 -1         Redirect stderr to stdout
 -2         Close stderr file descriptor (silent warning messages)
 -a arch    Set asm.arch
 -A         Run 'aaa' command to analyze all referenced code
 -b bits    Set asm.bits
 -B baddr   Set base address for PIE binaries
 -c 'cmd..' Execute rizin command
 -C         File is host:port (alias for -cR+http://%%s/cmd/)
 -d         Debug the executable 'file' or running process 'pid'
 -D backend Enable debug mode (e cfg.debug=true)
 -e k=v     Evaluate config var
 -E endian  Endianness -E big or -E little
 -f         Block size = file size
 -F binplug Force to use that rbin plugin
 -h, -hh    Show help message, -hh for long
 -H [var]   Display variable
 -i file    Run script file
 -I file    Run script file before the file is opened
 -k OS/kern Set asm.os (linux, macos, w32, netbsd, ...)
 -l lib     Load plugin file
 -L         List supported IO plugins
 -m addr    Map file at given address (loadaddr)
 -M         Do not demangle symbol names
 -n, -nn    Do not load RzBin info (-nn only load bin structures)
 -N         Do not load user settings and scripts
 -NN        Do not load any script or plugin
 -q         Quiet mode (no prompt) and quit after -i and -c
 -qq        Quiet mode (no prompt) and force quit
 -p p.rzdb  Load project file
 -r rz-run  Specify rz-run profile to load (same as -e dbg.profile=X)
 -R rule    Specify custom rz-run directive
 -s addr    Initial seek
 -T         Do not compute file hashes
 -u         Set bin.filter=false to get raw sym/sec/cls names
 -v, -V     Show rizin version (-V show lib versions)
 -w         Open file in write mode
 -x         Open without exec-flag (asm.emu will not work), See io.exec
 -X         Same as -e bin.usextr=false (useful for dyldcache)
 -z, -zz    Do not load strings or load them even in raw
```

### `rz-ar`

> 官方示例调用：`rz-ar -h`

```text
root@kali:~# rz-ar -h
Usage: rz-ar [-hlqv] [-o outdir] archive [member ...]
 -h     Show this help
 -l     List matching members
 -o dir Set output directory (default .)
 -q     Quiet mode
 -v     Show version information
```

### `rz-asm`

> 官方示例调用：`rz-asm -h`

```text
root@kali:~# rz-asm -h
Usage: rz-asm [-ACdDehLBvw] [-a arch] [-b bits] [-m plugin] [-o addr] [-s syntax]
             [-f file] [-F fil:ter] [-i skip] [-l len] 'code'|hex|-
 -a arch     Set architecture to assemble/disassemble (see -L)
 -A          Show Analysis information from given hexpairs
 -b bits     Set cpu register size (8, 16, 32, 64) (RZ_ASM_BITS)
 -B          Binary input/output (-l is mandatory for binary input)
 -c cpu      Select specific CPU (depends on arch)
 -C          Output in C format
 -d, -D      Disassemble from hexpair bytes (-D show hexpairs)
 -e          Use big endian instead of little endian
 -I          Display lifted RzIL code (same input as in -d, IL is also validated)
 -E          Display ESIL expression (same input as in -d)
 -f file     Read data from file
 -F in:out   Specify input and/or output filters (att2intel, x86.pseudo, ...)
 -h, -hh     Show this help, -hh for long
 -i len      Ignore N bytes of the input buffer
 -j          Output in JSON format
 -k kernel   Select operating system (linux, windows, darwin, ..)
 -l len      Input/Output length
 -L          List Asm plugins: (a=asm, d=disasm, A=analyze, e=ESIL, I=RzIL)
 -m plugin   List supported CPUs for the chosen plugin
 -o, -@ addr Set start address for code (default 0)
 -O file     Output file name (rz-asm -Bf a.asm -O a)
 -p          Run SPP over input for assembly
 -q          Quiet mode
 -s syntax   Select syntax (intel, att)
 -v          Show version information
 -x          Use hex dwords instead of hex pairs when assembling.
 -w          Describe opcode
 If '-l' value is greater than output length, output is padded with nops
 If the last argument is '-' reads from stdin
Environment:
 RZ_ARCH      e asm.arch # architecture to assemble/disassemble (same as rz-asm -a)
 RZ_ASM_ARCH             # architecture to assemble/disassemble (same as rz-asm -a)
 RZ_ASM_BITS             # cpu register size (8, 16, 32, 64) (same as rz-asm -b)
 RZ_BITS      e asm.bits # cpu register size (8, 16, 32, 64) (same as rz-asm -b)
 RZ_DEBUG                # if defined, show error messages and crash signal
 RZ_NOPLUGINS            # do not load shared plugins (speedup loading)
```

### `rz-ax`

> 官方示例调用：`rz-ax -h`

```text
root@kali:~# rz-ax -h
Usage: rz-ax [options] [expr ...]
If expr is not provided, reads from stdin
 int     ->  hex               ;  rz-ax 10
 hex     ->  int               ;  rz-ax 0xa
 -int    ->  hex               ;  rz-ax -77
 -hex    ->  int               ;  rz-ax 0xffffffb3
 int     ->  bin               ;  rz-ax b30
 int     ->  ternary           ;  rz-ax t42
 bin     ->  int               ;  rz-ax 1010d
 ternary ->  int               ;  rz-ax 1010dt
 float   ->  hex               ;  rz-ax 3.33f
 hex     ->  float             ;  rz-ax Fx40551ed8
 oct     ->  hex               ;  rz-ax 35o
 hex     ->  oct               ;  rz-ax Ox12 (O is a letter)
 bin     ->  hex               ;  rz-ax 1100011b
 hex     ->  bin               ;  rz-ax Bx63
 ternary ->  hex               ;  rz-ax 212t
 hex     ->  ternary           ;  rz-ax Tx23
 raw     ->  hex               ;  rz-ax -S < /binfile
 hex     ->  raw               ;  rz-ax -s 414141
 = base                         ;  rz-ax =10 0x46 -> output in base 10
 -l                            ;  append newline to output (for -E/-D/-r/..
 -a      show ascii table      ;  rz-ax -a
 -b      bin -> str            ;  rz-ax -b 01000101 01110110
 -B      str -> bin            ;  rz-ax -B hello
 -d      force integer         ;  rz-ax -d 3 -> 3 instead of 0x3
 -e      swap endianness       ;  rz-ax -e 0x33
 -D      base64 decode
 -E      base64 encode
 -f      floating point        ;  rz-ax -f 6.3+2.1
 -F      stdin slurp code hex  ;  rz-ax -F < shellcode.[c/py/js]
 -h      show this help        ;  rz-ax -h
 -i      dump as C byte array  ;  rz-ax -i < bytes
 -I      IP address <-> LONG   ;  rz-ax -I 3530468537
 -k      keep base             ;  rz-ax -k 33+3 -> 36
 -L      bin -> hex(bignum)    ;  rz-ax -L 111111111 # 0x1ff
 -n      int value -> hexpairs ;  rz-ax -n 0x1234 # 34120000
 -o      octalstr -> raw       ;  rz-ax -o \162 \172 # rz
 -N      binary number         ;  rz-ax -N 0x1234 # \x34\x12\x00\x00
 -r      rz style output       ;  rz-ax -r 0x1234
 -s      hexstr -> raw         ;  rz-ax -s 43 4a 50
 -S      raw -> hexstr         ;  rz-ax -S < /bin/ls > ls.hex
 -t      Unix tstamp -> str    ;  rz-ax -t 1234567890
 -m      MS-DOS tstamp -> str  ;  rz-ax -m 1234567890
 -W      Win32 tstamp -> str   ;  rz-ax -W 1234567890
 -x      hash string           ;  rz-ax -x linux osx
 -u      units                 ;  rz-ax -u 389289238 # 317.0M
 -w      signed word           ;  rz-ax -w 16 0xffff
 -v      version               ;  rz-ax -v
 -p      position of set bits  ;  rz-ax -p 0xb3
```

### `rz-bin`

> 官方示例调用：`rz-bin -h`

```text
root@kali:~# rz-bin -h
Usage: rz-bin [-AcdeEghHiIjlLMqrRsSUvVxzZ] [-@ at] [-a arch] [-b bits] [-B addr]
              [-C F:C:D] [-f str] [-m addr] [-n str] [-N m:M] [-P pdb]
              [-o str] [-O str] [-k query] [-D lang symname] file
 -@ addr      Show section, symbol, or import at the given address
 -A           List sub-binaries and their arch-bits pairs
 -a arch      Set arch (x86, arm, .. or <arch>_<bits>)
 -b bits      Set bits (32, 64 ...)
 -B addr      Override base address (pie bins)
 -c           List classes
 -cc          List classes in header format
 -C fmt:C:D   Create [elf,mach0,pe] with Code and Data hexpairs (see -a)
 -d           Show debug/dwarf information
 -dd          Load debug/dwarf information from debuginfod server
 -D lang name Demangle symbol name (-D all for bin.demangle=true)
 -e           Entrypoint
 -ee          Constructor/destructor entrypoints
 -E           Globally exportable symbols
 -f mach      Select sub-binary for the machine [mach].
 -F binfmt    Force to use that bin plugin (ignore header check)
 -g           Same as -SMZIHVResizcld -SS -SSS -ee (show all info)
 -G addr      Load address . offset to header
 -h           Show this help
 -H           Header fields
 -i           Import (symbols imported from libraries)
 -I           Binary info
 -j           Output in JSON
 -k sdb-query Run sdb query. for example: '*'
 -K algo      Calculate checksums (md5, sha1, ..)
 -l           Linked libraries
 -L [plugin]  List supported bin plugins or plugin details
 -m addr      Show source line at addr
 -M           Main (show address of main symbol)
 -n str       Show section, symbol or import named str
 -N min:max   Force min:max number of chars per string (see -z and -zz)
 -o str       Output file/folder for write operations (out by default)
 -O str       Write/extract operations (-O help)
 -p           Show physical addresses
 -P           Show debug/pdb information
 -PP          Download pdb file for binary
 -q           Quiet mode, just show fewer data
 -qq          Show less info (no offset/size for -z for ex.)
 -Q           Show load address used by dlopen (non-aslr libs)
 -r           Show output in rizin format
 -R           Show relocations
 -s           Symbols
 -S           Sections
 -SS          Segments
 -SSS         Sections mapping to segments
 -T           Display file signature
 -u           Unfiltered (no rename duplicated symbols/sections)
 -U           Resources
 -v           Show version information
 -V           Show binary version information
 -w           Display try/catch blocks
 -x           Extract bins contained in file
 -Y           Calculate all the possibles base address candidates of a firmware bin
 -z           Show strings (from data section)
 -zz          Show strings (from raw strings from bin)
 -zzz         Dump raw strings to stdout (for huge files)
 -Z           Guess size of binary program
Environment:
 RZ_BIN_CODESIGN_VERBOSE:                               # make code signatures verbose
 RZ_BIN_DEBUGINFOD_URLS:  e bin.dbginfo.debuginfod_urls # use alternative debuginfod server
 RZ_BIN_DEMANGLE=0:       e bin.demangle                # do not demangle symbols
 RZ_BIN_LANG:             e bin.lang                    # assume lang for demangling
 RZ_BIN_MAXSTRBUF:        e search.str.max_length       # specify maximum buffer size
 RZ_BIN_PDBSERVER:        e pdb.server                  # use alternative PDB server
 RZ_BIN_PREFIX:           e bin.prefix                  # prefix symbols/sections/relocs with a specific string
 RZ_BIN_STRFILTER:        e bin.str.filter              # rizin -qc 'e bin.str.filter=??' -
 RZ_BIN_STRPURGE:         e bin.str.purge               # try to purge false positives
 RZ_BIN_SYMSTORE:         e pdb.symstore                # path to downstream PDB symbol store
 RZ_CONFIG:                                             # config file
 RZ_COLOR:                                              # enables/disables colors support
 RZ_UTF8:                                               # enables/disables utf8 support
 RZ_NOPLUGINS:                                          # do not load plugins
```

### `rz-diff`

> 官方示例调用：`rz-diff -h`

```text
root@kali:~# rz-diff -h
Usage: rz-diff [options] <file0> <file1>
 -a arch      Specify architecture plugin to use (x86, arm, ..)
 -b bits      Specify register size for arch (16 (thumb), 32, 64, ..)
 -d myers     Compute edit distance using Eugene W. Myers' O(ND) algorithm (no substitution)
 -d leven     Compute edit distance using Levenshtein O(N^2) algorithm (with substitution)
 -d lcs-roll  Compute edit distance using Myers+FastCDC with chunk size 128 (-0 to change chunk size)
 -d ssdeep    Compute edit distance using Context triggered piecewise hashing comparison
 -i           Use command line arguments instead of files (only for -d)
 -H           Hexadecimal visual mode
 -h           Show this help
 -j           JSON output
 -q           Quiet output
 -v           Show version information
 -V           Be more verbose (stderr output)
 -K theme     Set a give color theme (see rizin 'eco' command)
 -e k=v       Set an evaluable config variable
 -A           Compare virtual and physical addresses
 -B           Run 'aaa' when loading the bin
 -C           Disable colors
 -T           Show timestamp information
 -S WxH       Set the width and height of the terminal for visual mode
 -0 cmd       Input for file0 when option -t 'commands' is given.
              The same value will be set for file1, if -1 is not set.
 -1 cmd       Input for file1 when option -t 'commands' is given.
 -t bytes     Compare raw bytes in the files (only for small files)
 -t lines     Compare text files
 -t functions Compare functions found in the files
              optional -0 <fcn name|offset> to compare only one function
 -t classes   Compare classes found in the files
 -t command   Compare command output returned when executed in both files
              requires -0 <cmd> and -1 <cmd> is optional
 -t entries   Compare entries found in the files
 -t fields    Compare fields found in the files
 -t graphs    Compare 2 functions and outputs in graphviz/dot format
              requires -0 <fcn name|offset> and -1 <fcn name|offset> is optional
 -t imports   Compare imports found in the files
 -t libraries Compare libraries found in the files
 -t sections  Compare sections found in the files
 -t strings   Compare strings found in the files
 -t symbols   Compare symbols found in the files
Palette colors can be changed by adding the following lines inside the $HOME/.rizinrc file
  ec diff.unknown blue  | offset color
  ec diff.match   green | match color
  ec diff.unmatch red   | mismatch color
Environment variables
  RZ_COLOR              | enables/disables colors support
```

### `rz-find`

> 官方示例调用：`rz-find -h`

```text
root@kali:~# rz-find -h
Usage: rz-find [-mXnzZhqvV] [-a align] [-b sz] [-f/t from/to] [-[e|s|w|S|I] str] [-x hex] [-R cmd] -|file|dir ..
 -a align Only accept aligned hits
 -b size  Set block size
 -e regex Search for regex matches (can be used multiple times)
 -E cmd   Execute shell command for each file found.
 -R cmd   Execute Rizin command for each search hit.
 -f from  Start searching from address 'from'
 -F file  Read the contents of the file and use it as keyword
 -h       Show this help
 -i       Identify filetype (magic signatures)
 -j       Output in JSON
 -m       Magic search, file-type carver
 -M str   Set a binary mask to be applied on keywords
 -n       Do not stop on read errors
 -r       Print using rizin commands
 -s str   Search for a specific string (can be used multiple times)
 -w str   Search for a specific wide string (can be used multiple times). Assumes str is UTF-8.
 -I str   Search for an entry in import table.
 -S str   Search for a symbol in symbol table.
 -t to    Stop search at address 'to'
 -q       Quiet - do not show headings (filenames) above matching contents (default for searching a single file)
 -v       Show version information
 -V       Verbose: prints each file scanned
 -x hex   Search for hexpair string (909090) (can be used multiple times)
 -X       Show hexdump of search results
 -z       Search for zero-terminated strings
 -Z       Show string found on each search hit
```

### `rz-gg`

> 官方示例调用：`rz-gg -h`

```text
root@kali:~# rz-gg -h
Usage: rz-gg [-FOLsrxhvz] [-a arch] [-b bits] [-k os] [-o file] [-I path]
             [-i sc] [-e enc] [-B hex] [-c k=v] [-C file] [-p pad] [-q off]
             [-S string] [-f fmt] [-nN dword] [-dDw off:hex] file|f.asm|-
 -a arch      Select architecture (x86, mips, arm)
 -b bits      Set Register size (32, 64, ..)
 -B hexpairs  Append some hexpair bytes
 -c k=v       Set configuration options
 -C file      Append contents of file
 -d off:dword Patch dword (4 bytes) at given offset
 -D off:qword Patch qword (8 bytes) at given offset
 -e encoder   Use specific encoder. see -L
 -f format    Output format (raw, c, pe, elf, mach0, python, javascript)
 -F           Output native format (osx=mach0, linux=elf, ..)
 -h           Show this help
 -i shellcode Include shellcode plugin, uses options. see -L
 -I path      Add include path
 -k kernel    Operating system's kernel (linux,bsd,osx,w32)
 -L           List all plugins (shellcodes and encoders)
 -n dword     Append 32bit number (4 bytes)
 -N qword     Append 64bit number (8 bytes)
 -o file      Output file
 -O           Use default output file (filename without extension or a.out)
 -p padding   Add padding after compilation (padding=n10s32)
              ntas : begin nop, trap, 'a', sequence
              NTAS : same as above, but at the end
 -P size      Prepend debruijn sequence of given length
 -q fragment  Debruijn pattern offset
 -r           Show raw bytes instead of hexpairs
 -s           Show assembler
 -S string    Append a string
 -v           Show version information
 -V           Increase the verbosity
 -w off:hex   Patch hexpairs at given offset
 -x           Execute
 -X           Execute rop chain, using the stack provided
 -z           Output in C string syntax
```

### `rz-hash`

> 官方示例调用：`rz-hash -h`

```text
root@kali:~# rz-hash -h
Usage: rz-hash [-vhBkjLq] [-b S] [-a A] [-c H] [-E A] [-D A] [-s S] [-x S] [-f O] [-t O] [files|-] ...
 -v        Show version information
 -h        Show this help
 -         Input read from stdin instead from a file
 -a algo   Hash algorithm to use and you can specify multiple ones by
           Appending a comma (example: sha1,md4,md5,sha256)
 -B        Output the calculated value for each block
 -b size   Set the block size
 -c value  Compare calculated value with a given one (hexadecimal)
 -e endian Set the endianness (default: 'big' accepted: 'big' or 'little')
 -D algo   Decrypt the given input; use -S to set key and -I to set IV (if needed)
 -E algo   Encrypt the given input; use -S to set key and -I to set IV (if needed)
 -f from   Start the calculation at given offset
 -t to     Stop the calculation at given offset
 -I iv     Set the initialization vector (IV)
 -i times  Repeat the calculation N times
 -j        Output the result as a JSON structure
 -k        Output the calculated value using openssh's randomkey algorithm
 -L        List all algorithms
 -q        Set quiet mode (use -qq to get only the calculated value)
 -S seed   Set the seed for -a, use '^' to append it before the input, use '@'
           Prefix to load it from a file and '-' from read it
 -K key    Set the hmac key for -a and the key for -E/-D, use '@' prefix to
           Load it from a file and '-' from read it
           From stdin (you can combine them)
 -s string Input read from a zero-terminated string instead from a file
 -x hex    Input read from a hexadecimal value instead from a file
           All the input (besides -s/-x/-c) can be hexadecimal or strings
           If 's:' prefix is specified
```

### `rz-run`

> 官方示例调用：`rz-run -h`

```text
root@kali:~# rz-run -h
Usage: rz-run [directives | script.rz] [-- program [args]]
 -h                Show this help
 -l                Show profile directives
 -t                Output template profile
 -v                Show version information
 -w                Wait for incoming terminal process
 -- program [args] Run program
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install rizin`，再执行 `librizin-common --version` 2>/dev/null || `librizin-common -V`
- [ ] **2.** **读官方帮助** —— `librizin-common -h`，需要细节时 `man librizin-common`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: rizin [-ACdfLMnNqStuvwzX] [-P patch] [-p prj] [-a arch] [-b bits] [-i file]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rizin/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[rizin](../../tools/tutorials/10-逆向工程/rizin.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rizin/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rizin/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
