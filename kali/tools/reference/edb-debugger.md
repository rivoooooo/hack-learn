# edb-debugger

> Cross platform x86/x86-64 debugger edb is a graphical cross platform x86/x86-64 debugger. It was inspired by Ollydbg, but aims to function on x86 and x86-64 as well as multiple OS’s. Linux is the only officially supported platform at the m…

> **功能分类**：数字取证 ｜ **Kali 包**：`edb-debugger` ｜ **官方文档**：<https://www.kali.org/tools/edb-debugger/>

## 1. 安装

```bash
sudo apt update
sudo apt install edb-debugger
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3.0 |
| 架构 | amd64 |
| 可执行命令 | `edb-debugger`、`edb`、`edb-debugger-plugins` |
| 依赖 | `edb-debugger-plugins`、`libc6`、`libcapstone5`、`libcgraph8`、`libdouble-conversion3`、`libgcc-s1`、`libgvc7`、`libqt5core5t64` |
| 安装体积 | 1.68 MB |
| 官网 | <https://github.com/eteran/edb-debugger> |
| 源码仓库 | <https://salsa.debian.org/debian/edb-debugger> |
| 包追踪 | <https://pkg.kali.org/pkg/edb-debugger> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Screenshots
edb
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

官方给出的调用示例：`man edb`

```text
root@kali:~# man edb
EDB(1)                                                                   EDB(1)
NAME
     edb - graphical debugger and disassembler for executables
SYNOPSIS
      edb [OPTION]... [TARGET]
DESCRIPTION
     edb  (Evan's  Debugger)  is a modular and modern disassembler and debugger
     for binary ELF files based on ptrace API and the capstone disassembly  li-
     brary.
     --help
            Show usage and exit.
     --symbols <file>
            generate symbols map for file <file>
     --attach <pid>
            attach the process of PID <pid> to debugger
     --run <program> [args...]
            open <program> in debugger with optional [args...]
     --version
            show version string and exit.
     --dump-version
            show version and exit.
EXAMPLE
     edb --symbols /lib/libc.so.6 > libc.so.6.map
          Will generate symbols for libc and save it in a text file. It's useful if you store this map files in the symbols directory configured in edb's preferences.
     for i in $(ls /lib); do edb --symbols $i > $(basename $i).map; done
           Useful to generate maps for all libs you have in /lib.
     edb --run /bin/ls
           Will open the ls program binary in debugger.
     edb --attach 1720
          Attach the process of PID 1720 to debugger.
AUTHOR
     Written by Evan Teran <
[email protected]
>
REPORTING BUGS
     Report    any    bugs    or    requests    for   features   via   BTS   on
     https://github.com/eteran/edb-debugger/issues
COPYRIGHT
     Copyright  (C)  2008  CodeF00.  Licensed  GPLv2:   GNU   GPL   version   2
     <http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt>. This is free soft-
     ware: you are free to change and redistribute it. There is NO WARRANTY, to
     the extent permitted by law.
                                 December 2011                           EDB(1)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install edb-debugger`，再执行 `edb-debugger --version` 2>/dev/null || `edb-debugger -V`
- [ ] **2.** **读官方帮助** —— `edb-debugger -h`，需要细节时 `man edb-debugger`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `edb-debugger -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/edb-debugger/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/edb-debugger/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/edb-debugger/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
