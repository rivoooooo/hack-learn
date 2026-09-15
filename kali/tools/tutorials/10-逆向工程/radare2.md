# Radare2（逆向工程框架）

> **一句话**：一个「十六进制编辑器 + 反汇编器 + 分析器 + 调试器」四合一的开源逆向框架，**全命令行、可脚本化、支持几十种架构**——服务器上没有图形界面时的主力工具。
> **分类**：逆向工程 / 静态与动态分析 ｜ **Kali 包**：`radare2`（命令 `radare2`/`r2`、`rabin2`、`radiff2`、`rafind2`、`ragg2`、`rahash2`、`rasm2`、`rax2`、`ravc2`）｜ **官方文档**：<https://book.radare.org/> ｜ 项目：<https://github.com/radareorg/radare2>

---

## 1. 它解决什么问题

逆向的日常工作其实是三类操作的循环：

1. **看清结构**（这个二进制是什么？有哪些函数、字符串、导入？）
2. **理解逻辑**（这个函数在干什么？谁调用了它？）
3. **验证假设**（跑起来，看寄存器与内存）

多数工具只覆盖其中一项：[`objdump.md`](objdump.md) 只会反汇编；[`gdb.md`](gdb.md) 只会调试；`strings` 只会找字符串。**Radare2 把三者放进同一套环境**，而且共享同一份「分析结果」：

| 你想做的事 | 其他工具 | Radare2 |
|------------|----------|---------|
| 找字符串 | `strings` | `iz` / `izz`（**带地址，可直接跳转**） |
| 反汇编 | `objdump -d` | `pdf @ main`（**带交叉引用与变量注释**） |
| 找「谁调用了这个函数」 | 手工 grep 反汇编 | `axt @ sym.check`（**交叉引用分析**） |
| 看控制流 | 手工读跳转 | `VV`（**ASCII 控制流图**） |
| 动态调试 | `gdb` | `r2 -d`（**调试器与反汇编器共享状态**） |
| 批量/自动化 | Shell 拼凑 | `r2 -c '...'`、r2pipe（**编程接口**） |
| 打补丁 | 十六进制编辑器 | `wx`（**直接改字节**） |

对比同类：

| 工具 | 定位 | 差异 |
|------|------|------|
| **radare2** | 全功能框架（CLI） | 学习曲线陡；灵活度最高、可脚本化 |
| **`rizin`** | radare2 的**社区分叉** | 命令与 r2 高度相似（`rz-*` 系列）；见 [`rizin.md`](rizin.md) |
| **`cutter`**（Kali 包 `rizin-cutter`） | rizin 的**图形界面** | 基于 rizin 的 Qt GUI，命令仍是 rizin 的 |
| **`ghidra`** | **反编译器** | 输出「类 C 代码」，逻辑理解最快；见 [`ghidra.md`](ghidra.md) |
| **`gdb`** + 插件 | 动态调试 | 调试体验更成熟；见 [`gdb.md`](gdb.md) |
| **`objdump` / `readelf`** | 单点工具 | 无需交互，适合脚本；见 [`objdump.md`](objdump.md) |

**实用建议**：**Ghidra 读逻辑，radare2 做批量与补丁，GDB 做精细动态调试**。三者配合是当前开源逆向的标准组合。

---

## 2. 工作原理

```
r2 target
   │
   ├─ ① 加载：IO 层（io）读文件/进程/内存；RBin 解析格式（ELF/PE/Mach-O/…）
   │      用 rabin2 的同一套解析器 → 得到节、符号、导入、字符串
   │
   ├─ ② 分析（aa / aaa）：
   │      · 从入口点与导出符号出发，递归识别函数
   │      · 识别基本块与跳转 → 构建控制流图（CFG）
   │      · 扫描字符串引用、数据引用 → 建立**交叉引用（xref）**
   │      · 识别函数参数与局部变量（部分靠启发式）
   │      结果存在内存里的「项目」中（可用 ps/pso 保存）
   │
   ├─ ③ 交互：命令由「子命令首字母」组成（**记住这个规律就入门了一半**）
   │      a*  分析       i*  信息      p*  打印/反汇编   s   定位
   │      f*  标志       /   搜索      w*  写入/补丁     d*  调试
   │      o*  打开文件   q   退出      V   可视模式      ?   帮助
   │
   └─ ④ 可视化：V（hexdump/反汇编视图）、VV（控制流图）、V!（面板）
```

### 2.1 命令体系的核心规律

Radare2 的命令是**单字母前缀 + 子命令**。掌握这几个前缀就能自主探索：

| 前缀 | 类别 | 典型命令 |
|------|------|----------|
| `i` | **信息**（info） | `iI`（文件头）、`ii`（导入）、`ie`（入口）、`is`（符号）、`iz`/`izz`（字符串）、`iS`（节） |
| `a` | **分析**（analyze） | `aa`/`aaa`（分析）、`afl`（函数列表）、`af`（函数内）、`ax`（交叉引用）、`ar`（寄存器） |
| `p` | **打印**（print） | `pd`（反汇编）、`pdf`（反汇编整个函数）、`px`（hexdump）、`ps`（字符串）、`pc`（反汇编+注释） |
| `s` | **定位**（seek） | `s main`、`s 0x401146`、`s+8`（相对跳转） |
| `f` | 标志（flag） | `f`（列表）、`f sym.main`（创建标志） |
| `/` | **搜索** | `/x <hex>`、`/ <string>`、`/r`（引用）、`/a`（汇编指令） |
| `w` | **写入**（write） | `wx`（写字节）、`wa`（写汇编）、`wo`（写操作） |
| `d` | **调试**（debug） | `db`（断点）、`dc`（继续）、`ds`（单步）、`dr`（寄存器）、`dpx`（栈） |
| `o` | 打开（open） | `o`（列表）、`oo+`（以写模式重开） |
| `V` | 可视模式 | `V`、`VV`、`V!`、`Vp` |
| `q` | 退出 | `q`、`q!`（强制） |
| `?` | **帮助** | `?`、`a?`、`pd?`（**最重要的命令，卡住就按 `?`**） |

> **r2 最大特点**：`?` 是万能的。忘了语法就 `pd?` 看帮助。**用 r2 的能力就是「用 `?` 的能力」。**

### 2.2 项目与持久化

分析一个二进制可能花几小时。r2 的**项目**保存分析结果：

```bash
r2 -p myproject target.bin    # 加载/创建项目
```

```
[0x00401060]> Ps myproject     # 保存
[0x00401060]> Po myproject     # 打开
[0x00401060]> P              # 列出项目
```

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install radare2
r2 -v
```

```console
root@kali:~# r2 -h
Usage: r2 [-ACdfjLMnNqStuvwzX] [-P patch] [-p prj] [-a arch] [-b bits] [-c cmd]
          [-s addr] [-B baddr] [-m maddr] [-i script] [-e k=v] file|pid|-|--|=
 --           run radare2 without opening any file
 -            same as 'r2 malloc://512'
 =            read file from stdin (use -i and -c to run cmds)
 -a [arch]    set asm.arch
 -A           run 'aaa' command to analyze all referenced code
 -b [bits]    set asm.bits
 -B [baddr]   set base address for PIE binaries
 -c 'cmd..'   execute radare command
 -d           debug the executable 'file' or running process 'pid'
 -D [backend] enable debug mode (e cfg.debug=true)
 -e k=v       evaluate config var
 -i [file]    run rlang program, r2script file or load plugin
 -j           use json for -v, -L and maybe others
 -n, -nn      do not load RBin info (-nn only load bin structures)
 -q           quiet mode (no prompt) and quit after -i
 -w           open file in write mode
 -z, -zz      do not load strings or load them even in raw
```

配套命令（**每个都是独立的 CLI 工具，可单独使用**）：

| 命令 | 作用 | 类比 |
|------|------|------|
| `r2` / `radare2` | 主程序（交互/批处理/调试） | —— |
| `rabin2` | **二进制信息提取**（头、节、符号、导入、字符串） | `readelf` + `strings` + `nm` |
| `radiff2` | **二进制差异比较**（含函数级、字符串级） | `diff` + `BinDiff` 思路 |
| `rafind2` | **字节/字符串/正则搜索** | `grep` + `strings` |
| `rahash2` | **哈希/加密工具**（可校验、可分块、可加解密） | `md5sum` 增强版 |
| `rasm2` | **汇编/反汇编**（支持多架构） | `objdump` 的汇编方向 |
| `ragg2` | **生成 shellcode / 编译 asm 为裸二进制** | `nasm` + shellcode 生成器 |
| `rax2` | **进制/格式转换**（hex/dec/float/base64/时间） | `printf` + `base64` |
| `ravc2` | 生成 VC 工程（Windows 相关） | —— |

最短流程（**带分析启动**）：

```bash
r2 -A -q ./target
```

```console
[0x00401060]> afl
0x00401126    1 44           sym.add
0x00401146    1 49           sym.main
0x004011a0    1 22           entry0
[0x00401146]> pdf
```

> **注意**：`-A`（等于 `aaa`）在**大文件上会很慢**。小文件用 `-A`，大文件先 `aa`，需要时再 `aaaa`（更深入但更慢）。

---

## 4. 核心参数详解

### 4.1 `r2` 启动参数（真实参数，来自 `r2 -h`）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-A` | 启动即执行 `aaa`（**全量分析**） | 小文件首选 |
| `-a [arch]` | 设置 `asm.arch`（架构） | `-a arm`、`-a x86` |
| `-b [bits]` | 设置 `asm.bits`（位数） | `-b 32`、`-b 64` |
| `-B [baddr]` | **设置基址**（PIE 二进制） | 与运行时基址对齐 |
| `-c 'cmd..'` | **执行命令后退出**（可重复） | **批量化/脚本化的核心** |
| `-d` | **调试模式**（调试文件或指定 pid 的进程） | `r2 -d ./target`、`r2 -d <pid>` |
| `-e k=v` | 设置配置变量 | `-e asm.syntax=intel`（**常用！**） |
| `-i [file]` | 启动后运行脚本文件 | 自动化 |
| `-q` | 静默模式（不打印横幅，`-i` 后退出） | 脚本化 |
| `-w` | **以写模式打开**（可打补丁） | 补丁用（**先备份**） |
| `-n` / `-nn` | 不加载 RBin 信息 / 只加载 bin 结构 | 非常规文件 |
| `-p [prj]` | 加载/创建**项目** | 大型分析续做 |
| `-s [addr]` | 起始定位地址 | `-s main` |
| `-m [addr]` | 把文件映射到指定地址（加载地址） | 裸二进制/固件 |
| `-k [OS/kern]` | 设置 `asm.os` | `-k linux`、`-k w32` |
| `-j` | JSON 输出（对 `-v`/`-L` 等） | 脚本化 |
| `-L` / `-LL` | 列出 IO 插件 / 核心插件 | 排错 |
| `-F [plugin]` | 强制指定 RBin 插件 | 格式识别失败时 |
| `-x` | 打开时不加执行标志 | 纯数据文件 |
| `-z` / `-zz` | 不加载字符串 / 加载 raw 字符串 | 大文件加速 |
| `-N` / `-NN` | 不加载用户配置 / 不加载任何脚本与插件 | 排除配置干扰 |
| `-P [file]` | 应用 rapatch 补丁文件并退出 | 补丁 |
| `=` | 从 stdin 读文件 | `cat x | r2 -c 'pd 20' =` |

### 4.2 信息类命令（`i`）

| 命令 | 作用 | 使用建议 |
|------|------|----------|
| `iI` | **文件头信息**（格式、架构、位数、字节序、是否 PIE、是否静态） | 第一步 |
| `iS` | **节表**（名称、地址、大小、权限） | 找 `.text`/`.rodata` |
| `ii` | **导入表**（调用了哪些库函数） | 判断语言与依赖 |
| `iE` | **导出表**（提供了哪些符号） | 库/插件分析 |
| `is` | **符号表** | **未 strip 时直接看函数名** |
| `iz` | **数据节里的字符串** | 找常量/错误信息/密钥 |
| `izz` | **整个文件里的字符串**（含 raw） | 更全（含被压缩/嵌入的） |
| `ie` | 入口点 | 分析起点 |
| `iM` / `im` | main 函数 / 内存映射 | —— |
| `iH` | 头字段（类似 `rabin2 -H`） | —— |
| `it` | 文件签名/哈希 | —— |
| `i~<str>` | **用 `~` 过滤输出**（内建 grep） | `iS~text`、`izz~passwd`（**极常用**） |

### 4.3 分析类命令（`a`）

| 命令 | 作用 | 使用建议 |
|------|------|----------|
| `aa` | 基本分析（识别函数与符号引用） | 大文件先跑它 |
| `aaa` | 更全（含更多引用与字符串分析） | `-A` 就是它 |
| `aaaa` | 最全（更慢，含实验性分析） | 小文件/需要时 |
| `afl` | **函数列表**（地址、大小、名字） | **分析的入口**；`afl~main` 过滤 |
| `af` | 在当前地址创建函数 | 手动标注 |
| `afn <name>` | **重命名当前函数** | **分析中最常用的动作之一**（把 `fcn.00401a20` 改成 `check_license`） |
| `afvn <old> <new>` | 重命名局部变量 | 让反汇编可读 |
| `pdf` | **反汇编当前函数**（带注释、交叉引用、变量） | **最常用命令**；`pdf @ sym.main` |
| `pdc` | 伪 C 反编译（内置简化反编译器） | 快速看逻辑（不如 Ghidra 完整） |
| `pdr` | 递归反汇编 | —— |
| `axt <addr\|sym>` | **谁调用了它**（xref to） | **关键**：`axt @ sym.strcmp` |
| `axf <addr\|sym>` | 它调用了谁（xref from） | 顺着调用链往下走 |
| `axtj` / `axfj` | 上两者的 **JSON** 输出 | 脚本化 |
| `axg` | 交叉引用图 | —— |
| `ar` | 寄存器（调试时） | —— |
| `afvd` | 显示当前函数的局部变量与参数 | —— |
| `afv` | 变量列表 | —— |
| `ao` | 分析当前指令（操作数详情） | —— |
| `aae` | 执行 ESIL 模拟分析 | 高级 |
| `aflj` | 函数列表 JSON | 脚本/统计函数数量 |
| `afi` | 当前函数信息 | 参数个数、栈大小等 |

### 4.4 打印与可视化（`p` / `V`）

| 命令 | 作用 | 使用建议 |
|------|------|----------|
| `pd <n>` | 反汇编 n 条指令 | `pd 20` |
| `pdj <n>` | 反汇编（JSON） | 脚本化 |
| `pdf` | 整个当前函数 | **主力** |
| `px <n>` | hexdump n 字节 | `px 64` |
| `pxw` / `pxq` / `pxr` | 按 word/qword/引用 显示 | 看指针 |
| `ps` | 打印字符串 | —— |
| `pc` | 反汇编 + 注释（含操作数解释） | 理解指令语义 |
| `p8 <n>` | 打印原始字节（hex string） | 复制补丁字节 |
| `pt` | 显示类型/结构体 | —— |
| `V` | **可视模式**（hexdump 与反汇编联动） | 手动导航 |
| `VV` | **控制流图**（ASCII 图） | **快速理解分支结构** |
| `V!` | 面板模式（多窗口） | 高级用法 |
| `Vp` | 可视模式：反汇编 | —— |
| `Vd` / `Vdd` | 调试相关视图 | 配合 `-d` |
| `e asm.syntax=intel` | **切成 Intel 语法** | **建议一开始就设** |
| `e scr.color=3` | 彩色输出 | 视觉辅助 |
| `~<str>` | 过滤器（grep） | `pdf~call`（只看调用指令，**效率提升神器**） |
| `~?<regex>` | 正则过滤 | 更精确 |

### 4.5 搜索（`/`）

| 命令 | 作用 | 使用建议 |
|------|------|----------|
| `/x <hex>` | 搜十六进制字节 | `/x 909090` |
| `/ <string>` | 搜字符串 | 精确的常量匹配 |
| `/w <string>` | 搜宽字符（UTF-16） | Windows 程序常用 |
| `/a <asm>` | **搜汇编指令** | `/a mov eax, 1`（找特定指令模式） |
| `/r <addr>` | 搜引用（谁引用了这个地址） | 找「谁用了这个字符串/全局变量」 |
| `/p` | 搜并生成反汇编 | —— |
| `/i` | 在当前函数内搜指令 | —— |
| `/R` | 搜 ROP gadget | 找 gadget |
| `//` | 重复上次搜索 | —— |

### 4.6 写入与补丁（`w`，**需 `-w` 打开**）

| 命令 | 作用 | 使用建议 |
|------|------|----------|
| `wx <hex>` | **写字节** | `wx 9090`（把指令改成 nop） |
| `wa <asm>` | **写汇编**（自动汇编） | `wa jmp 0x401200` |
| `woa` | 覆盖汇编 | 更彻底的替换 |
| `wv` | 写数值 | —— |
| `wz <string>` | 写字符串 | —— |
| `wt` | 写文件内容 | —— |
| `Ci` / `Cl` | 生成补丁文件（可选） | 可导出 patch 而不是直接改 |
| `e io.cache=true` | **缓存写操作**（不立即落盘） | **推荐**：先缓存修改，确认后 `wci` 提交 |

**补丁的标准流程**（**授权 CTF / 自有程序**）：

```
r2 -w ./target
[0x...]> e io.cache=true      # 先进入缓存模式（不改原文件）
[0x...]> s 0x401170
[0x...]> pd 5                 # 确认这几条指令
[0x...]> wx 9090909090        # 改（缓存在内存里）
[0x...]> pd 5                 # 再确认
[0x...]> wci                  # 提交到文件（cache 提交）
[0x...]> q
```

---

## 5. 实战演练

> **环境声明**：以下使用**自己编写的练习程序**、**CTF 靶题**、**开源软件（在其许可范围内）**。
> **禁止**对非自有软件逆向以规避许可/DRM（《著作权法》相关），或窃取商业秘密（《反不正当竞争法》第 9 条），或对未授权系统利用漏洞（《刑法》第 285/286 条）。

### 场景 1：快速摸清一个未知二进制（10 条命令）

```bash
mkdir -p /tmp/lab && cd /tmp/lab
cat > crackme.c <<'EOF'
#include <stdio.h>
#include <string.h>
static int check(const char *s) {
    if (strlen(s) != 8) return 0;
    if (s[0] != 'r' || s[1] != '2') return 0;
    if (strcmp(s + 2, "OOKS!") != 0) return 0;   /* r2OOKS! */
    return 1;
}
int main(void) {
    char buf[64];
    printf("Password: ");
    if (!fgets(buf, sizeof buf, stdin)) return 1;
    buf[strcspn(buf, "\n")] = 0;
    puts(check(buf) ? "Correct!" : "Wrong!");
    return 0;
}
EOF
gcc -O0 -o crackme crackme.c
```

```bash
r2 -q ./crackme   # 先不分析，用信息命令摸底
```

```console
[0x00401060]> iI
arch     x86
baddr    0x400000
binsz    15997
bintype  elf
bits     64
class    ELF64
compiler GCC: (Debian ...)
endian   little
havecode true
intrp    /lib64/ld-linux-x86-64.so.2
lang     c
machine  AMD x86-64 architecture
os       linux
static   false
stripped false
subsys   linux
```

**解读（关键两行）**：`stripped false` → **符号还在**（省一半功夫）；`static false` → 动态链接（可以用 [`ltrace.md`](ltrace.md)）。

```console
[0x00401060]> is~FUNC
[0x00401060]> is~check       ← 用 ~ 过滤，直接找目标函数
13  0x00001126 0x00401126 LOCAL FUNC   8 check
50  0x00001146 0x00401146 LOCAL FUNC  49 main
```

**解读**：**`~` 过滤器是 r2 的效率核心**。`is~check` 直接定位 `check` 在 `0x401126`。

```console
[0x00401060]> izz~Password
117 0x00002004 0x00402004 10 10   .rodata ascii Password: 
148 0x00002227 0x00002227 29 29   .rodata ascii Password: file too long
```

```console
[0x00401060]> aa          ← 基本分析
[0x00401060]> afl~check
0x00401126    4 73           sym.check
[0x00401060]> pdf @ sym.check     ← 反汇编这个函数
```

```console
            ;-- check:
            ; CALL XREF from sym.main @ 0x4011c0(x)
┌ 73: sym.check (int64_t arg1);
│ afv: vars(1:sp[0x18..0x18])
│           0x00401126      endbr64
│           0x0040112a      push  rbp
│           0x0040112b      mov   rbp, rsp
│           0x0040112e      sub   rsp, 0x20
│           0x00401132      mov   qword [rbp - 0x18], rdi    ; arg1
│           0x00401136      mov   rax, qword [rbp - 0x18]
│           0x0040113a      mov   rdi, rax
│           0x0040113d      call  sym.imp.strlen           ; size_t strlen(const char *s)
│           0x00401142      cmp   rax, 8
│       ┌─< 0x00401146      je    0x40114c
│       │   0x00401148      mov   eax, 0
│      ┌──< 0x40114d      jmp   0x4011a2
│      │└─> 0x40114c      mov   rax, qword [rbp - 0x18]
│      │    0x00401150      movzx eax, byte [rax]
│      │    0x00401153      cmp   al, 0x72             ; 'r'
│      │┌─< 0x00401155      jne   0x4011a0
│      ││   0x00401157      mov   rax, qword [rbp - 0x18]
│      ││   0x0040115b      movzx eax, byte [rax + 1]
│      ││   0x0040115e      cmp   al, 0x32             ; '2'
│      ││┌─< 0x00401160      jne   0x4011a0
│      │││   0x00401162      mov   rax, qword [rbp - 0x18]
│      │││   0x00401166      add   rax, 2
│      │││   0x00401169      lea   rsi, [0x0040200c]    ; "OOKS!"
│      │││   0x00401170      mov   rdi, rax
│      │││   0x00401173      call  sym.imp.strcmp
│      │││   0x00401178      test  eax, eax
│      │││┌─< 0x0040117a      jne   0x4011a0
│      ││││   0x0040117c      mov   eax, 1
│      ││││   0x00401180      jmp   0x4011a2
```

**解读（这就是 r2 的价值所在）**：

| 特性 | 好处 |
|------|------|
| `;-- check:` + `; CALL XREF from sym.main @ 0x4011c0` | **自动标注了「谁调用了它」**（不需手工 grep） |
| `sym.imp.strlen` / `strcmp` 带注释 `; size_t strlen(const char *s)` | **函数原型直接给出** |
| `lea rsi, [0x0040200c] ; "OOKS!"` | **自动解引用字符串**（不用再去 `.rodata` 翻） |
| ASCII 竖线画出的分支缩进 | **控制流一眼可见** |
| `arg1`、`[rbp - 0x18]` | 参数与局部变量标注 |

**答案直接读出来了**：长度 = 8，第 0 字节 `'r'`，第 1 字节 `'2'`，后面（从 `s+2`）等于 `"OOKS!"` → **口令是 `r2OOKS!`**。

```bash
# 验证
echo 'r2OOKS!' | ./crackme
```

```console
Password: Correct!
```

### 场景 2：交叉引用 + 控制流图（找「真正的判断点」）

```bash
# 造一个稍微复杂点的目标：多个检查函数，看 r2 怎么帮我们排序优先级
objdump -d -M intel crackme > /dev/null   # 对比一下：objdump 的输出没有 xref 与注释
```

```console
[0x00401060]> axt @ sym.imp.strcmp      ← 谁调用了 strcmp？
sym.check 0x401173 [CALL] call sym.imp.strcmp
[0x00401060]> axt @ 0x0040200c          ← 谁引用了 "OOKS!" 这个地址？
sym.check 0x401169 [DATA] lea rsi, [0x0040200c]
```

**解读**：`axt`（xref to）是**逆向中最重要的分析命令**。它回答「**这个函数/字符串/全局变量被谁用了**」——而这正是理解程序结构的主线。

```console
[0x00401060]> s sym.check        ← 定位到 check
[0x00401060]> VV                 ← 控制流图（ASCII）
```

```console
┌────────────────────────────────────────┐
│  0x00401126                            │
│ ;-- check:                             │
│ endbr64                                │
│ push rbp                               │
│ mov rbp, rsp                           │
│ sub rsp, 0x20                          │
│ mov qword [rbp - 0x18], rdi            │
│ ...                                    │
│ call sym.imp.strlen                    │
│ cmp rax, 8                             │
└────────────────────────────────────────┘
        │
        ├─────────────────────────┐
        ▼                         ▼
┌───────────────────────┐  ┌────────────────────┐
│ 0x0040114c            │  │ 0x00401148        │
│ mov rax, qword [...]  │  │ mov eax, 0        │
│ movzx eax, byte [rax] │  │ jmp 0x4011a2      │
│ cmp al, 0x72 ; 'r'    │  └────────────────────┘
│ ...
```

**解读**：`VV` 把分支结构画成树——**一眼看出「4 个连续的检查，任一失败就跳到返回 0」**。比逐条读跳转指令快得多。按 `q` 退出图，按方向键导航。

```console
[0x00401060]> pdf @ sym.main~call    ← 只看 main 里的 call 指令
0x004011a5      call  sym.imp.printf
0x004011b3      call  sym.imp.fgets
0x004011c0      call  sym.check
0x004011c5      call  sym.imp.puts
```

**解读**：`~call` 过滤把「整个函数的调用序列」压成 4 行——**这是 r2 的 `~` 过滤器最实用的场景之一**。

```console
[0x00401060]> pdc @ sym.check      ← 内置伪 C 反编译（快速版）
```

```c
int sym.check (int64_t arg1) {
    if (sym.imp.strlen (arg1) != 8) {
        return 0;
    }
    if (*(char *)arg1 != 'r' || *(char *)(arg1 + 1) != '2') {
        return 0;
    }
    if (sym.imp.strcmp ((arg1 + 2), "OOKS!") != 0) {
        return 0;
    }
    return 1;
}
```

**解读**：`pdc` 给出「够用的伪 C」。**逻辑复杂时用 Ghidra 的反编译器更好**（见 [`ghidra.md`](ghidra.md)）；逻辑简单时 `pdc` 已经足够。

### 场景 3：动态调试与补丁（r2 -d + r2 -w）

**3a. 用 r2 自带调试器跑起来**

```bash
r2 -d ./crackme
```

```console
[0x7f2c...]> db sym.check        ← 下断点
[0x7f2c...]> dc                  ← 继续
hit breakpoint at: 0x401126
[0x00401126]> dr                 ← 看寄存器
rax = 0x00000000 ...
rdi = 0x7ffd1a2b3c40             ← 第 1 个参数（我们输入的指针）
[0x00401126]> ps @ rdi           ← 看参数内容（ps = 打印字符串）
Wrong
```

**解读（r2 调试器的特色）**：**反汇编器与调试器共享同一个「当前位置」** —— 断下来之后 `pdf`、`px`、`ps @ rdi` 直接可用，**不需要像 GDB 那样切换上下文**。

```console
[0x00401126]> dc
Correct!
```

**3b. 用 `-d` + `-c` 做无人值守调试（脚本化）**

```bash
r2 -d -q -c 'db sym.check; dc; dr; ps @ rdi; pd 5; q' ./crackme
```

**解读**：`r2 -c '...'` 是**把 r2 变成可脚本化工具**的关键。可以放进 Shell 循环批量分析样本。

**3c. 打补丁（绕过 check 函数，**授权 CTF / 自有程序**）**

```bash
# 目标：让 check 永远返回 1（"Correct!"）
r2 -w ./crackme_copy      # 先复制一份再改！
```

```console
[0x00401060]> s sym.check
[0x00401060]> pdf~mov eax     ← 找「给返回值赋值」的位置
0x0040117c      mov eax, 1
0x00401148      mov eax, 0
0x0040119a      mov eax, 0
[0x00401060]> s 0x00401126    ← 函数入口
[0x00401060]> e io.cache=true ← 先进缓存模式（不立即写盘）
[0x00401060]> wa "mov eax, 1; ret"   ← 直接把函数改成「返回 1」
[0x00401060]> pd 3
0x00401126      mov eax, 1
0x0040112b      ret
0x0040112c      (原指令剩余)
[0x00401060]> wci             ← 提交到文件
[0x00401060]> q
```

```bash
# 验证补丁
echo 'anything' | ./crackme_copy
```

```console
Password: Correct!
```

**解读**：**这就是「客户端校验必然可绕」的最直接证明**。`e io.cache=true` + `wci` 的工作方式很值得学：**先在内存里预览修改效果，确认无误再落盘**（避免改错文件）。

**3d. 与 GDB / Ghidra 的分工**

| 任务 | 更适合 |
|------|--------|
| 批量分析一堆样本、提取函数/字符串清单 | **r2（`-c` 脚本化 + JSON）** |
| 精细调试（复杂断点、观察点、多线程、core dump） | [`gdb.md`](gdb.md) |
| 读懂复杂业务逻辑 | [`ghidra.md`](ghidra.md) |
| 打补丁/改字节 | **r2（`-w` + `wx`/`wa` + `io.cache`）** |
| 图形化探索 | `cutter`（`rizin-cutter` 包，基于 rizin）或 Ghidra |

### 场景 4：bat 命令 —— 用批处理做「一键分析」

r2 支持**批处理文件（`.r2` 脚本）**，把常用分析流程固化下来：

```bash
cat > /tmp/lab/triage.r2 <<'EOF'
# ===== 二进制快速体检脚本（r2 -i triage.r2 ./target）=====
e asm.syntax=intel
e scr.color=3
echo "=== 文件头 ==="
iI
echo "=== 节表 ==="
iS
echo "=== 导入函数（前 30）==="
ii~[0,2,3]:0,30
echo "=== 可疑字符串（关键字）==="
izz~pass
izz~key
izz~secret
izz~admin
echo "=== 危险函数引用 ==="
axt @ sym.imp.system
axt @ sym.imp.execve
axt @ sym.imp.strcpy
echo "=== 函数数量 ==="
aflc
echo "=== 完成 ==="
EOF
r2 -A -q -i /tmp/lab/triage.r2 ./crackme
```

**解读**：这份脚本就是**「拿到一个陌生二进制时的固定动作」**——把「安全审计/恶意样本初筛」的套路固化成可复用脚本。**在样本分析场景，这比每次手工敲命令高效得多。**

```bash
# 只用命令行（不用脚本文件）也能一次性做很多事
r2 -q -c 'aa; afl~sym.; izz~pass; axt @ sym.imp.strcmp; q' ./crackme
```

---

## 6. 输出解读

### 6.1 `pdf` 输出的标记

| 标记 | 含义 | 价值 |
|------|------|------|
| `;-- <name>:` | 函数名/标志 | 函数边界 |
| `; CALL XREF from <caller> @ <addr>` | **调用者** | **不用手工找调用关系** |
| `; DATA XREF from ...` | 数据引用者 | 找「谁读了这个变量」 |
| `; <原型注释>` | 库函数原型（来自 r2 的类型库） | 参数含义 |
| `; "string"` | **自动解引用的字符串** | **常量在下一行就能看到** |
| `arg1`、`var_18h`、`local_20h` | 参数/局部变量命名 | 数据流追踪 |
| `┌ │ └ <` 等 ASCII 线条 | 控制流图 | 分支结构 |
| `sym.imp.<name>` | **导入的库函数**（PLT 调用） | 判断程序能力 |
| `fcn.00401a20` | **未命名的函数**（r2 自动起名） | 需要手工 `afn` 改名 |
| `sub.<名称>_<序号>` | 库内局部符号 | —— |

### 6.2 信息命令的输出重点

| 命令 | 重点看什么 |
|------|------------|
| `iI` | `stripped`（是否被 strip）、`static`（静态/动态）、`bits`、`arch`、`os`、`bintype` |
| `iS` | 节名与权限（找 `.text`/`.rodata`/`.data`/`.got`） |
| `ii` | 导入函数名（**能推断程序功能**：`system`→执行命令、`socket`→网络、`EVP_*`→加密） |
| `is` | 函数与全局符号（**未 strip 时信息量最大**） |
| `iz` / `izz` | 字符串（错误信息、URL、路径、密钥线索） |
| `afl` | 函数数量与大小（**大函数往往是核心逻辑**） |
| `axt` | 「谁用了它」（**理解结构的主线**） |

### 6.3 成功判据

- 能列出「关键函数及其作用」（`afl` + `pdf` + `axt`）；
- 能把「某个字符串/常量」关联到「哪个函数用了它」（`/r`、`axt`）；
- 能画出关键函数的控制流（`VV`）；
- 静态结论能被 `r2 -d` 或 [`gdb.md`](gdb.md) 动态验证。

---

## 7. 与其他工具配合

```
① 结构摸底
   ├─ rabin2 -I/-S/-s/-i/-z     ← 不开交互，直接出信息（最适合脚本）
   ├─ r2 -q -c 'iI; iS; ii; izz'  ← 一条命令出全套
   └─ file / readelf / objdump    ← 交叉验证（objdump.md）
        │
② 交互分析（本文）
   ├─ aa/aaa → afl → pdf @ <func> → axt @ <addr> → VV
   ├─ ~ 过滤（pdf~call / izz~passwd / afl~sym.）
   ├─ afn/afvn 重命名（把 fcn.xxx 变成可读名字）
   └─ pdc（内置伪 C）；复杂逻辑 → ghidra.md
        │
③ 动态验证
   ├─ r2 -d ./target（集成反汇编+调试）
   └─ gdb + pwndbg/gef（更成熟的调试体验）  ← gdb.md
        │
④ 补丁与批量
   ├─ r2 -w + wx/wa + e io.cache=true + wci
   ├─ r2 -c '...' 批处理 / -i 脚本
   └─ radiff2（两版本差异）/ rafind2（搜索）/ rahash2（哈希）
        │
⑤ 图形化（不想用命令行时）
   └─ cutter（Kali 包 rizin-cutter，基于 rizin） / ghidra
```

**配套小工具速用（都在 `radare2` 包里）**：

```bash
rabin2 -I ./crackme              # 二进制信息（等价 readelf -h 的加强版）
rabin2 -z ./crackme              # 字符串（带地址）
rabin2 -i ./crackme              # 导入表
rafind2 -s "OOKS!" ./crackme     # 搜字符串
rafind2 -x 4f4f4b53 ./crackme    # 搜字节
radiff2 -C old new               # 函数级差异比较
rahash2 -a md5,sha256 ./crackme  # 多算法哈希
rasm2 -d -a x86 -b 64 554889e5   # 反汇编 hex
rasm2 -a x86 -b 64 'mov eax, 1'  # 汇编成 hex
rax2 0x401126                    # 进制转换
```

- 反汇编基础：[`objdump.md`](objdump.md) ｜ 动态调试：[`gdb.md`](gdb.md) ｜ 库调用：[`ltrace.md`](ltrace.md)
- 反编译器：[`ghidra.md`](ghidra.md) ｜ rizin（r2 分叉）：[`rizin.md`](rizin.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `afl` 只列出少数函数 / 没有函数 | 还没分析 | 先 `aa`（或启动时 `-A`）；大文件用 `aa` 而不是 `aaaa` |
| `-A` 启动非常慢 | `aaa` 在大二进制上开销大 | 先 `aa`，需要时 `aaf`/`aac`；或只分析指定地址范围 |
| 显示的地址与运行时不一致 | 二进制是 **PIE** | `-B <运行时基址>`，或按偏移计算（见 [`gdb.md`](gdb.md) 的 `info proc mappings`） |
| 汇编语法看着别扭 | 默认 AT&T | **`e asm.syntax=intel`**（或启动 `-e asm.syntax=intel`）；放进 `~/.radare2rc` 永久生效 |
| 反汇编出现大量 `invalid` | 把数据当代码（未对齐起点） | `s` 到正确的函数入口；`af` 手动定义函数；用 `pdc`/`VV` 看整体 |
| `pdf` 显示 `fcn.00401a20` 之类名字 | 未 strip 但 r2 没认出语义 / 已 strip | `afn <新名字>` 重命名（**边分析边命名是效率关键**） |
| 断点打不上（`-d`） | 地址是 PIE 偏移 / 反调试 | 用符号名 `db sym.check`；`e dbg.bpinmaps`；检查是否被 `ptrace` 自检拦住 |
| `-d` 报 ptrace 权限错误 | Yama / 容器缺 `SYS_PTRACE` | `sudo`、加 `--cap-add=SYS_PTRACE`（**仅自己的环境**） |
| 打补丁后程序不能用 | 覆盖了过长的指令序列 / 未处理对齐 | 用 `e io.cache=true` 先预览；`wa` 后 `pd` 检查；必要时用 `wx` 手工 nop 填充 |
| 补丁没生效 | 用了 `io.cache` 但没 `wci` 提交；或文件被重新编译 | 检查是否 `wci`；确认运行的是改过的副本 |
| `izz` 结果太多/太少 | 默认只扫数据节 / raw 模式 | 用 `izz`（全文件）；`-zz` 启动参数改变字符串加载策略 |
| 输出刷屏找不到重点 | 没用过滤器 | **`~`**：`pdf~call`、`izz~pass`、`afl~main`、`iS~text` |
| 忘记命令语法 | —— | **按 `?`**：`pd?`、`a?`、`w?`；或 `?$`（查看所有环境变量） |
| 配置文件干扰行为 | `~/.radare2rc` 有自定义设置 | `r2 -N`（不读配置）排错 |
| 大文件分析吃内存 | r2 把分析结果放内存 | 用项目（`Ps`）保存；分区域分析；关闭不必要的分析（`-z`） |

---

## 9. 防御视角（蓝队 / 恶意样本分析）

radare2 在防守方的**主要用途是恶意样本分析**（这是完全正当且必要的工作），其次是二进制加固评估。

| 场景 | 用 r2 怎么做 | 产出 |
|------|--------------|------|
| **恶意样本初筛** | 用 5-场景 4 的 `triage.r2` 脚本 | 导入函数、字符串、可疑 API 引用清单 |
| 判断样本能力 | `ii`（导入表）、`axt @ sym.imp.system` 等 | 「会不会执行命令/联网/加密文件」 |
| 找 C2 地址/密钥 | `izz~http`、`izz~key`、`iz` | IOC（域名/IP/URL） |
| 找持久化/后门特征 | `izz~run`、`izz~cron`、`izz~systemd` | 行为线索 |
| 反调试/加壳识别 | 无符号 + 高熵节 + `pdc` 混乱 | 判定是否加壳/混淆（配合 [`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md) 的熵分析） |
| 生成 YARA 特征输入 | `izz` + `rafind2` 提取独特字节串 | YARA 规则素材 |
| 二进制加固评估 | 看是否 strip、是否有 canary/PIE/RELRO | 加固建议 |
| **供应链核对** | `rabin2 -I/-i/-S` 与官方版本对比 | 发现被替换/植入的二进制 |

**蓝队/安全工程可落地的三条**：

1. **样本分析在隔离环境进行**（断网虚拟机、快照），并记录 `rahash2` 得到的哈希（用于情报共享）；
2. **把「可疑 API 组合」做成检测规则**：例如同一二进制同时引用 `socket` + `connect` + `system` + `unlink`，在服务端二进制里是**极不正常**的组合；
3. **生产环境监控逆向工具的使用**（`r2`/`gdb`/`objdump`/`strings` 出现在应用服务器上通常是异常信号）。

**开发侧加固的现实结论**：`strip`、加壳、混淆、反调试**只是抬高成本**；`stripped true` 的二进制依然能用 r2/Ghidra 分析（本教程的例子就演示了这一点）。**真正的秘密不能放在客户端。**

---

## 10. 参考

- Radare2 官方书籍（**最权威的命令参考**）：<https://book.radare.org/>
- Radare2 仓库与 Wiki：<https://github.com/radareorg/radare2>
- Kali 工具页：<https://www.kali.org/tools/radare2/>
- 配套工具手册：`man rabin2`、`man radiff2`、`man rafind2`、`man rahash2`、`man rasm2`、`man rax2`
- 本地命令：`r2 -h`、`r2 -hh`（长帮助）、交互内 `?`
- 相关教程：[`rizin.md`](rizin.md)、[`ghidra.md`](ghidra.md)、[`gdb.md`](gdb.md)、[`objdump.md`](objdump.md)、[`ltrace.md`](ltrace.md)

## ⚠️ 法律与伦理

radare2 是**合法性明确的开发与安全工具**：调试自己的程序、分析恶意样本、CTF、授权的漏洞研究、开源软件研究都在正当用途内。但以下行为可能违法：

- **逆向非自有软件以规避技术措施/DRM**（《著作权法》相关规定与许可协议）；
- **窃取商业秘密**（《反不正当竞争法》第 9 条）；
- 对**未授权系统**利用逆向发现的漏洞（《刑法》第 285/286 条）；
- 分析**来源不明的他人设备数据**（《个人信息保护法》《数据安全法》）。

**请遵守**：

1. 只分析**自己的程序**、**CTF 靶题**、**开源软件（在其许可范围内）**、**授权的研究目标**、**恶意样本（在做防御分析时）**；
2. **打补丁只改副本**（本教程的 `r2 -w ./crackme_copy` 就是这个意思），绝不改原始样本（保持取证价值）；
3. 发现商业软件漏洞走**厂商披露流程**；恶意样本的 IOC 共享遵循所在组织的流程；
4. 本教程所有示例请用第 5 节的自编程序（`crackme.c`）复现。
