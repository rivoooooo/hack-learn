# nasm

> General-purpose x86 assembler Netwide Assembler. NASM will currently output flat-form binary files, a.out, COFF and ELF Unix object files, and Microsoft 16-bit DOS and Win32 object files. Also included is NDISASM, a prototype x86 binary-fi…

> **功能分类**：信息搜集 ｜ **Kali 包**：`nasm` ｜ **官方文档**：<https://www.kali.org/tools/nasm/>

## 1. 安装

```bash
sudo apt update
sudo apt install nasm
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.01 |
| 架构 | any |
| 可执行命令 | `nasm`、`ndisasm` |
| 依赖 | `libc6` |
| 安装体积 | 3.67 MB |
| 官网 | <https://www.nasm.us/> |
| 源码仓库 | <https://salsa.debian.org/debian/nasm> |
| 包追踪 | <https://pkg.kali.org/pkg/nasm> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
nasm -h          # 查看用法
man nasm         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `nasm`

官方给出的调用示例：`nasm -h`

```text
root@kali:~# nasm -h
Usage: nasm [-@ response_file] [options...] [--] filename
  Options:
    -v (or --v)    print the NASM version number and exit
    -@ file        response file; one command line option per line
    -h             list command line options and exit (also --help)
    -h -opt        show additional help for option "-opt"
    -h all         show all available command line help
    -h topics      show list of help topics (also -h list)
    -o outfile     write output to outfile
    --keep-all     output files will not be removed even if an error happens
    -Xformat       specify error reporting format (see -h -X)
    -s             redirect messages to stdout
    -Zfile         redirect messages to file
    --info[=lvl]   display optional informational messages
    --debug[=lvl]  display NASM internal debugging messages
    -M...          generate Makefile dependencies (see -h -M)
    -f format      select output file format (see -h -f)
    -g             generate debugging information
    -F format      select a debugging format (see -h -F)
    -gformat       same as -g -F format
    -l listfile    write listing to a list file
    -Lflags...     add information to the list file (see -h -L)
    -Oflags...     select optimization (see -h -O)
    -t             assemble in limited SciTech TASM compatible mode
    -E (or -e)     preprocess only (writes output to stdout by default)
    -a             don't preprocess (assemble only)
    -Ipath         add a pathname to the include file path
    -Pfile         pre-include a file (also --include)
    -Dmacro[=str]  pre-define a macro
    -Umacro        undefine a macro
    -w+x           enable warning x  (see -h -w)(also -Wx)
    -w-x           disable warning x (also -Wno-x)
    -w[+-]error    promote all warnings to errors (also -Werror)
    -w[+-]error=x  promote warning x to errors (also -Werror=x)
    --pragma str   pre-executes a specific %pragma
    --before str   add line (usually a preprocessor statement) before the input
    --bits nn      set bits to nn (equivalent to --before "BITS nn")
    --no-line      ignore %line directives in input
    --gprefix str  prepend the given string to the names of all extern,
                   common and global symbols (also --prefix)
    --gpostfix str append the given string to the names of all extern,
                   common and global symbols (also --postfix)
    --lprefix str  prepend the given string to local symbols
    --lpostfix str append the given string to local symbols
    --reproducible attempt to produce run-to-run identical output
    --limit-X val  set execution limit X (see -h --limit)
```

### `ndisasm`

官方给出的调用示例：`ndisasm -h`

```text
root@kali:~# ndisasm -h
usage: ndisasm [-aihlruvw] [-b bits] [-o origin] [-s sync...]
               [-e bytes] [-k start,bytes] [-p vendor] file
   -a or -i activates auto (intelligent) sync
   -b 16, -b 32 or -b 64 sets the processor mode
   -u same as -b 32
   -l same as -b 64
   -w wide output (avoids continuation lines)
   -h displays this text
   -r or -v displays the version number
   -e skips <bytes> bytes of header
   -k avoids disassembling <bytes> bytes from position <start>
   -p selects the preferred vendor instruction set (intel, amd, cyrix, idt)
Learn more with
OffSec
Want to learn more about nasm? get access to in-depth training and hands-on labs:
Low Level Programming - x86 Skill Path
Exploit Development Essentials
Updated on: 2025-Dec-09
 Edit this page
name-that-hash
nasty
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install nasm`，再执行 `nasm --version` 2>/dev/null || `nasm -V`
- [ ] **2.** **读官方帮助** —— `nasm -h`，需要细节时 `man nasm`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: nasm [-@ response_file] [options...] [--] filename`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/nasm/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/nasm/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/nasm/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
