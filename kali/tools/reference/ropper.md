# ropper

> Rop gadget finder and binary information tool This package contains scripts that display info about files in different formats and find gadgets to build ROPs chains for different architectures (x86/x86_64, ARM/ARM64, MIPS, PowerPC). For di…

> **功能分类**：通用工具 ｜ **Kali 包**：`ropper` ｜ **官方文档**：<https://www.kali.org/tools/ropper/>

## 1. 安装

```bash
sudo apt update
sudo apt install ropper
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.13.8 |
| 架构 | all |
| 可执行命令 | `ropper` |
| 依赖 | `python3`、`python3-capstone`、`python3-filebytes`、`python3-pkg-resources` |
| 安装体积 | 402 KB |
| 官网 | <https://scoding.de/ropper/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ropper> |
| 包追踪 | <https://pkg.kali.org/pkg/ropper> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ropper -h          # 查看用法
man ropper         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ropper`

官方给出的调用示例：`ropper -h`

```text
root@kali:~# ropper -h
usage: ropper [-h] [--help-examples] [-v] [--console] [-f <file> [<file> ...]]
              [-r] [-a <arch>] [--section <section>] [--string [<string>]]
              [--hex] [--asm [<asm> [H|S|R] ...]] [--disasm <opcode>]
              [--disassemble-address <address:length>] [-i] [-e] [--imagebase]
              [-c] [-s] [-S] [--imports] [--symbols] [--set <option>]
              [--unset <option>] [-I <imagebase>] [-p] [-j <reg>]
              [--stack-pivot] [--inst-count <n bytes>] [--search <regex>]
              [--quality <quality>] [--opcode <opcode>]
              [--instructions <instructions>] [--type <type>] [--detailed]
              [--all] [--cfg-only] [--chain <generator>] [-b <badbytes>]
              [--nocolor] [--clear-cache] [--no-load] [--analyse <quality>]
              [--semantic constraint] [--count-of-findings <count of gadgets>]
              [--single]
You can use ropper to display information about binary files in different file formats
    and you can search for gadgets to build rop chains for different architectures
supported filetypes:
  ELF
  PE
  Mach-O
  Raw
supported architectures:
  x86 [x86]
  x86_64 [x86_64]
  MIPS [MIPS, MIPS64]
  ARM/Thumb [ARM, ARMTHUMB]
  ARM64 [ARM64]
  PowerPC [PPC, PPC64]
  SPARC [SPARC64]
available rop chain generators:
  execve (execve[=<cmd>], default /bin/sh) [Linux x86, x86_64]
  mprotect  (mprotect address=0xdeadbeef size=0x10000) [Linux x86, x86_64]
  virtualprotect (virtualprotect address=0xdeadbeef) [Windows x86]
options:
  -h, --help            show this help message and exit
  --help-examples       Print examples
  -v, --version         Print version
  --console             Starts interactive commandline
  -f, --file <file> [<file> ...]
                        The file to load
  -r, --raw             Loads the file as raw file
  -a, --arch <arch>     The architecture of the loaded file
  --section <section>   The data of the this section should be printed
  --string [<string>]   Looks for the string <string> in all data sections
  --hex                 Prints the selected sections in a hex format
  --asm [<asm> [H|S|R] ...]
                        A string to assemble and a format of the output
                        (H=HEX, S=STRING, R=RAW, default: H)
  --disasm <opcode>     Opcode to disassemble (e.g. ffe4, 89c8c3, ...)
  --disassemble-address <address:length>
                        Disassembles instruction at address <address>
                        (0x12345678:L3). The count of instructions to
                        disassemble can be specified (0x....:L...)
  -i, --info            Shows file header [ELF/PE/Mach-O]
  -e                    Shows EntryPoint
  --imagebase           Shows ImageBase [ELF/PE/Mach-O]
  -c, --dllcharacteristics
                        Shows DllCharacteristics [PE]
  -s, --sections        Shows file sections [ELF/PE/Mach-O]
  -S, --segments        Shows file segments [ELF/Mach-O]
  --imports             Shows imports [ELF/PE]
  --symbols             Shows symbols [ELF]
  --set <option>        Sets options. Available options: aslr nx
  --unset <option>      Unsets options. Available options: aslr nx
  -I <imagebase>        Uses this imagebase for gadgets
  -p, --ppr             Searches for 'pop reg; pop reg; ret' instructions
                        [only x86/x86_64]
  -j, --jmp <reg>       Searches for 'jmp reg' instructions (-j reg[,reg...])
                        [only x86/x86_64]
  --stack-pivot         Prints all stack pivot gadgets
  --inst-count <n bytes>
                        Specifies the max count of instructions in a gadget
                        (default: 6)
  --search <regex>      Searches for gadgets
  --quality <quality>   The quality for gadgets which are found by search (1 =
                        best)
  --opcode <opcode>     Searches for opcodes (e.g. ffe4 or ffe? or ff??)
  --instructions <instructions>
                        Searches for instructions (e.g. "jmp esp", "pop eax;
                        ret")
  --type <type>         Sets the type of gadgets [rop, jop, sys, all]
                        (default: all)
  --detailed            Prints gadgets more detailed
  --all                 Does not remove duplicate gadgets
  --cfg-only            Filters out gadgets which fail the Microsoft CFG
                        check. Only for PE files which are compiled with CFG
                        check enabled (check DllCharachteristics) [PE]
  --chain <generator>   Generates a ropchain [generator parameter=value[
                        parameter=value]]
  -b, --badbytes <badbytes>
                        Set bytes which should not contains in gadgets
  --nocolor             Disables colored output
  --clear-cache         Clears the cache
  --no-load             Don't load the gadgets automatically when start the
                        console (--console)
  --analyse <quality>   just used for the implementation of semantic search
  --semantic constraint
                        semantic search for gadgets
  --count-of-findings <count of gadgets>
                        Max count of gadgets which will be printed with
                        semantic search (0 = undefined, default: 5)
  --single              No multiple processes are used for gadget scanning
Updated on: 2025-Dec-09
 Edit this page
robotstxt
routerkeygenpc
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ropper`，再执行 `ropper --version` 2>/dev/null || `ropper -V`
- [ ] **2.** **读官方帮助** —— `ropper -h`，需要细节时 `man ropper`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `ropper -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ropper/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ropper/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ropper/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
