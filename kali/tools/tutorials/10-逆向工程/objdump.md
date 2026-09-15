# objdump（反汇编与目标文件分析）

> **一句话**：GNU binutils 里的「万能查看器」——把一个可执行文件/目标文件/库拆开看：文件头、节表、符号表、重定位、以及**反汇编机器码**。
> **分类**：逆向工程 / 静态分析 ｜ **Kali 包**：**不在 Kali 官方工具清单中** —— `objdump` 来自 **`binutils`** 包（Kali 的 `autopsy` 等工具会依赖它）。**它不是 Kali 专有工具**，任何 Linux 发行版都一样。
> **官方文档**：<https://sourceware.org/binutils/docs/binutils/objdump.html> ｜ `man objdump`

---

## 1. 它解决什么问题

逆向的第一步永远是「**先看清文件的结构**」。你手上有的是一个二进制 blob，需要知道：

- 它是 ELF 还是 PE？32 位还是 64 位？静态还是动态链接？
- 有哪些节（`.text`/`.data`/`.rodata`/`.plt`/`.got`）？分别在哪、多大、权限是什么？
- 有哪些函数和符号？（未 strip 时直接看到函数名）
- 它调用了哪些库函数（`printf@plt`）？
- 某段机器码对应什么汇编指令？
- 保护机制（NX / PIE / RELRO / Canary）开了哪些？

`objdump` 一条命令就能回答其中大部分。**优点是：几乎所有 Linux 都有、无需图形界面、输出可 grep、可脚本化。**

| 你想知道 | objdump 参数 |
|----------|--------------|
| 文件格式与架构 | `-f`（`file` 命令的加强版） |
| 节表（大小/地址/权限） | `-h` |
| 节内容（十六进制） | `-s -j .data` |
| 符号表 | `-t`（所有符号，含调试符号）/ `-T`（动态符号） |
| 重定位 | `-r`（静态）/ `-R`（动态） |
| 反汇编 | `-d`（可执行节）/ `-D`（全部节） |
| 带源码反汇编 | `-S`（需 `-g` 编译） |
| 程序头（段表）/ 动态信息 | `-p` |
| 全部信息 | `-x` |
| 调试信息 | `-g`（DWARF 解析） |

对比同类：

| 工具 | 定位 | 差异 |
|------|------|------|
| **objdump** | 反汇编 + 目标文件分析 | 系统自带、**反汇编最权威（来自 binutils）**；无交互、无反编译 |
| **`readelf`** | **只读 ELF 结构** | ELF 专用、结构输出更清晰；**不做反汇编** |
| **`nm` / `strings`** | 符号 / 字符串 | 单一用途 |
| **`radare2` / `rizin`** | 交互式逆向框架 | 有分析、交叉引用、图形、调试；见 [`radare2.md`](radare2.md)、[`rizin.md`](rizin.md) |
| **`ghidra`** | **反编译器** | 输出「类 C 代码」，理解逻辑最快；见 [`ghidra.md`](ghidra.md) |
| **`gdb`** | 动态调试 | 跑起来看；见 [`gdb.md`](gdb.md) |
| **`ltrace` / `strace`** | 调用跟踪 | 看「调了哪些库/系统调用」；见 [`ltrace.md`](ltrace.md) |

**推荐组合用法**：**`file` + `readelf -h` 看身份 → `objdump -d` 看代码 → `ghidra` 反编译读逻辑 → `gdb` 动态验证**。objdump 是这条链里**最基础、最不可替代的一环**（尤其在没有 GUI 的服务器上）。

---

## 2. 工作原理

objdump 依赖 **BFD（Binary File Descriptor）库**——binutils 里负责「用统一接口读写各种目标文件格式」的抽象层。

```
objdump -d target
   │
   ├─ BFD 识别格式（ELF64/ELF32/PE/COFF/a.out/…）与架构（x86-64/ARM/MIPS/…）
   │     └─ 所以同一份 objdump 通过 -b/-m 可处理多种格式
   │
   ├─ 读取节（section）表 → 找到标记为「可执行」的节（通常是 .text）
   │
   ├─ 逐条解码机器码 → 用架构对应的**反汇编器**（x86 用 i386-dis）输出汇编
   │     └─ 反汇编是「线性扫描」：从节起点开始逐条解码
   │        （与「递归下降」相比，会把数据误判为指令，反之亦然）
   │
   └─ 输出文本（可 grep / 重定向 / 用 awk 处理）
```

### 关键概念

| 概念 | 含义 | 逆向中为什么重要 |
|------|------|------------------|
| **节（section）** | 链接视角的划分：`.text`（代码）、`.data`（已初始化数据）、`.bss`（未初始化）、`.rodata`（只读数据）、`.plt`/`.got`（动态链接跳转/地址表） | 找字符串去 `.rodata`；找全局变量去 `.data`；找函数去 `.text` |
| **段（segment）** | 加载视角的划分（`LOAD`、`GNU_STACK` 等），`readelf -l` 看 | 决定运行时的内存权限（NX 就来自 `GNU_STACK` 是否可执行） |
| **`.plt` / `.got`** | 动态调用：`call printf@plt` → 跳到 `.plt` 桩 → 通过 `.got` 里保存的真实地址 | 找「调用了哪些库函数」看 `@plt`；GOT 覆盖类漏洞看 `.got` |
| **符号（symbol）** | 名字 ↔ 地址的映射 | 未 strip 时，函数名直接告诉你**每个函数是干什么的** |
| **重定位（relocation）** | 链接/加载时需要「填地址」的位置 | 分析 PIE、GOT/PLT 机制 |
| **DWARF 调试信息** | `-g` 编译产生的源码级信息 | 有它就能把地址还原成 `file.c:42` |
| **PIE** | 位置无关可执行文件 | 有 PIE 时 objdump 显示的地址是**相对偏移**，运行时还要加基址 |

**反汇编的两大局限**（必须知道，否则会误判）：

1. **代码与数据混在一起**：`.text` 里可能嵌着跳转表/常量池。线性扫描会把数据当指令反汇编出「看起来合理但其实是垃圾」的代码。
2. **间接跳转/调用无法静态确定目标**：`call rax`、`jmp [rdx*8+0x4040]`（跳转表）在静态视图里看不到目标——**这类「分派逻辑」需要 [gdb.md](gdb.md) 动态跟**。

---

## 3. 安装与快速上手

objdump 随 binutils 提供（几乎总是已安装）：

```bash
# 若不存在
sudo apt update && sudo apt install binutils
objdump --version
```

```console
GNU objdump (GNU Binutils) 2.47
```

```bash
objdump --help | head -40
```

```console
Usage: objdump <option(s)> <file(s)>
 Display information from object <file(s>).
 At least one of the following switches must be given:
  -a, --archive-headers    Display archive header information
  -f, --file-headers       Display the contents of the overall file header
  -p, --private-headers    Display object format specific file header contents
  -h, --[section-]headers  Display the contents of the section headers
  -x, --all-headers        Display the contents of all headers
  -d, --disassemble        Display assembler contents of executable sections
  -D, --disassemble-all    Display assembler contents of all sections
  ...
```

**最短三连**（先看身份、再看节、最后看代码）：

```bash
file target
objdump -f target
objdump -h target
objdump -d target | head -40
```

支持的格式与架构（用来判断「能不能处理这个文件」）：

```bash
objdump -i | head -20
```

```console
BFD header file version (GNU Binutils) 2.47
elf64-x86-64
 (header little endian, data little endian)
  i386
elf32-i386
...
```

---

## 4. 核心参数详解

### 4.1 信息类（不需反汇编）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-f, --file-headers` | **文件头**（格式、架构、入口点、标志） | 第一步 |
| `-h, --section-headers`（`--headers`） | **节表**（名称、大小、VMA/LMA、对齐、标志） | 找 `.text`/`.rodata`/`.got` |
| `-x, --all-headers` | **全部头**（`-a -f -h -p -r -t` 的合集） | 一次性概览 |
| `-p, --private-headers` | **格式私有头**（ELF 就是程序头/动态段） | 看段权限、动态库依赖 |
| `-s, --full-contents` | 节的**完整十六进制内容** | `-s -j .rodata` 看只读字符串 |
| `-t, --syms` | **符号表**（含调试符号） | **找函数名/全局变量** |
| `-T, --dynamic-syms` | **动态符号表** | 看导入/导出了哪些库函数 |
| `-r, --reloc` | 静态**重定位**条目 | 分析链接过程 |
| `-R, --dynamic-reloc` | **动态重定位**（GOT 条目） | 分析 GOT/PLT |
| `-g, --debugging` | **DWARF 调试信息** | 有 `-g` 编译时有价值 |
| `-W, --dwarf[=...]` | 细粒度 DWARF 段显示 | `--dwarf=info` 看类型/变量 |
| `-a, --archive-headers` | 静态库（`.a`）成员头 | 分析 `.a` |
| `-L, --process-links` | 处理分离的 debuginfo 文件 | 发行版把调试信息分包时用 |
| `-G, --stabs` | STABS 调试信息（老格式） | 少见 |
| `-i, --info` | **列出支持的格式与架构** | 判断能否处理目标文件 |
| `-H, --help` / `-v, --version` | 帮助 / 版本 | —— |

### 4.2 反汇编类

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-d, --disassemble` | **只反汇编可执行节**（`.text`） | **最常用** |
| `-D, --disassemble-all` | 反汇编**所有节** | 代码藏在数据节里时用（会产生大量噪音） |
| `--disassemble=<sym>` | 只反汇编指定**符号**起 | `--disassemble=main`（很实用） |
| `-S, --source` | **混合显示源码与汇编** | 有 `-g` 时信息量最大 |
| `-l, --line-numbers` | 显示行号与文件名 | 配合 `-d`/`-S` |
| `-z, --disassemble-zeroes` | 不跳过全零块 | 默认会「…」省略零区 |
| `--start-address=ADDR` | 只反汇编 **≥ ADDR** 的部分 | **定向分析某个函数**（速度快） |
| `--stop-address=ADDR` | 只反汇编 **< ADDR** 的部分 | 与上面配对 |
| `--no-show-raw-insn` | 不显示机器码字节 | 输出更干净（默认显示） |
| `--insn-width=WIDTH` | 每行显示的机器码字节数 | 排版 |
| `--visualize-jumps` | **用 ASCII 画跳转箭头** | 快速看清控制流（现代 binutils 有） |
| `--visualize-jumps=color` | 带颜色 | 终端里用 |
| `--disassembler-color=on` | 汇编语法高亮 | —— |
| `-C, --demangle[=STYLE]` | **还原 C++/Rust 混淆名** | C++ 程序**必加**（否则看到 `_ZN3Foo3barEv`） |
| `-M, --disassembler-options=OPT` | 传给反汇编器的选项 | **`-M intel` 用 Intel 语法**（默认 AT&T） |
| `-j, --section=NAME` | 只处理指定节 | `-d -j .text`、`-s -j .rodata` |
| `-b, --target=BFDNAME` | 指定目标格式 | 处理裸二进制时用 |
| `-m, --architecture=MACHINE` | 指定架构 | 交叉分析（如 `-m i386`） |
| `-EB` / `-EL` | 假设大端 / 小端 | 处理未知二进制 |
| `-F, --file-offsets` | 显示**文件偏移** | 与 hexdump/补丁工具配合 |
| `-w, --wide` | 宽输出（>80 列） | 长指令行不换行 |
| `-I, --include=DIR` | 源码搜索目录 | 配合 `-S` |
| `--adjust-vma=OFFSET` | 调整显示的地址 | 与 `gdb` 里的基址对齐 |
| `--show-all-symbols` | 显示同一地址的所有符号 | 别名/局部标签 |

### 4.3 i386/x86-64 专用反汇编选项（`-M` 后的值）

| 选项 | 作用 |
|------|------|
| `intel` | **Intel 语法**（`mov eax, 1`）—— 推荐 |
| `att` | AT&T 语法（默认，`movl $1, %eax`） |
| `x86-64` / `i386` / `i8086` | 强制 64/32/16 位模式 |
| `addr64` / `addr32` / `addr16` | 假设地址宽度 |
| `data32` / `data16` | 假设数据宽度 |
| `intel-mnemonic` / `att-mnemonic` | 混用语法与助记符风格 |
| `suffix` | AT&T 下总是显示指令后缀（`b`/`w`/`l`/`q`） |
| `annotate-immediates` | 标注与符号匹配的立即数 |

用法：

```bash
objdump -d -M intel target | head -30
```

### 4.4 其他常用组合（记住这几条就够用）

| 目的 | 命令 |
|------|------|
| 快速体检 | `file t && objdump -f t && objdump -h t` |
| Intel 语法反汇编（C++ 去混淆） | `objdump -d -M intel -C t` |
| 只看 main | `objdump -d -M intel --disassemble=main t` |
| 找字符串所在的节 | `objdump -s -j .rodata t \| less` |
| 看导入的库函数 | `objdump -T t \| grep UND` |
| 看 GOT 重定位 | `objdump -R t` |
| 带源码调试视图 | `objdump -d -S -l -M intel t` |
| 强控制流可视化 | `objdump -d -M intel --visualize-jumps=color t` |
| 定位文件偏移（补丁用） | `objdump -d -F -M intel t` |
| 分析静态库成员 | `objdump -a libfoo.a` |

---

## 5. 实战演练

> **环境声明**：以下使用**自己编写的练习程序**或**开源软件（在其许可范围内）**。
> **禁止**：对非自有软件逆向以规避许可/DRM（可能违反《著作权法》）、窃取商业秘密（《反不正当竞争法》），或对未授权系统利用漏洞（《刑法》第 285/286 条）。

### 场景 1：给一个陌生二进制做「体检」

```bash
mkdir -p /tmp/lab && cd /tmp/lab
cat > hello.c <<'EOF'
#include <stdio.h>
int add(int a, int b) { return a + b; }
int main(void) {
    printf("sum=%d\n", add(2, 3));
    return 0;
}
EOF
gcc -g -O0 -o hello hello.c
```

```bash
# ① 身份识别：格式、架构、入口点、类型
objdump -f hello
```

```console
hello:     file format elf64-x86-64
architecture: i386:x86-64, flags 0x00000112:
EXEC_P, HAS_SYMS, D_PAGED
start address 0x0000000000401040
```

**解读**：`elf64-x86-64` = 64 位 ELF；`EXEC_P` = 是**可执行文件**（不是目标文件/库）；`HAS_SYMS` = **还有符号表**（没被 strip，调试会轻松很多）；`start address` = 入口（通常是 `_start`，**不是 `main`**）。

```bash
# ② 节表：代码在哪、字符串在哪、多大
objdump -h hello
```

```console
Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .interp       0000001c  0000000000400238  0000000000400238  00000238  2**0
  1 .note.gnu.property 00000020 ...
 12 .plt          00000030  0000000000401020  0000000000401020  00001020  2**4
 13 .text         00000195  0000000000401060  0000000000401060  00001060  2**4
 15 .rodata       0000000c  0000000000402000  0000000000402000  00002000  2**2
 21 .data         00000004  0000000000404020  0000000000404020  00003020  2**3
 22 .bss          00000008  0000000000404024  0000000000404024  00003024  2**3
 25 .got.plt      00000030  0000000000404000  0000000000404000  00003000  2**3
```

**解读（每列的含义）**：

| 列 | 含义 |
|----|------|
| `Size` | 节大小 |
| `VMA` | **虚拟地址**（运行时地址；PIE 时是偏移） |
| `LMA` | 加载地址（固件/裸机场景会有区别） |
| **`File off`** | **文件内偏移** → 用 hexdump/补丁工具改这一段时用这个值 |
| `Algn` | 对齐要求 |

**关键结论**：代码在 `.text`（地址 `0x401060`，大小 `0x195`）；只读字符串在 `.rodata`（`0x402000`）；全局变量在 `.data`/`.bss`；动态跳转表在 `.plt`/`.got.plt`。

```bash
# ③ 符号表：直接看到函数名（未 strip 的福利）
objdump -t hello | grep -E 'F .text'
```

```console
0000000000401126 l     F .text	0000000000000020              add
0000000000401146 l     F .text	000000000000001b              main
0000000000401060 g     F .text	0000000000000021              _start
```

**解读**：`F` = 函数符号（`l`=local、`g`=global），后面是大小与名字。**`add` 在 `0x401126`，`main` 在 `0x401146`** —— 这两个地址可以直接拿去 `gdb` 下断点（`b *0x401146`）。

```bash
# ④ 导入了哪些库函数（看 @plt）
objdump -T hello | grep -i 'UND'
```

```console
0000000000000000      DF *UND*	0000000000000000  GLIBC_2.2.5 printf
0000000000000000      DF *UND*	0000000000000000  GLIBC_2.34  __libc_start_main
```

**解读**：`UND`（undefined）= **需要外部库提供**。看到 `printf`、`__libc_start_main` 就知道这是 libc 程序。

### 场景 2：反汇编并读懂逻辑（Intel 语法 + 定向分析）

```bash
# ① 只看 main（--disassemble=<sym> 高效定向）
objdump -d -M intel -C --disassemble=main hello
```

```console
0000000000401146 <main>:
  401146:	f3 0f 1e fa          	endbr64
  40114a:	55                   	push   rbp
  40114b:	48 89 e5             	mov    rbp,rsp
  40114e:	bf 05 00 00 00       	mov    edi,0x5
  401153:	b8 00 00 00 00       	mov    eax,0x0
  401158:	e8 c9 ff ff ff       	call   401126 <add>
  40115d:	89 c6                	mov    esi,eax
  40115f:	48 8d 3d 9e 0e 00 00 	lea    rdi,[rip+0xe9e]        # 402004 <_IO_stdin_used+0x4>
  401166:	b8 00 00 00 00       	mov    eax,0x0
  40116b:	e8 c0 fe ff ff       	call   401030 <printf@plt>
  401170:	b8 00 00 00 00       	mov    eax,0x0
  401175:	5d                   	pop    rbp
  401176:	c3                   	ret
```

**解读（x86-64 System V 调用约定）**：

| 指令 | 含义 |
|------|------|
| `push rbp` / `mov rbp,rsp` | **函数序言**：建立栈帧 |
| `mov edi,0x5` | **参数 1 = 5**（`add` 的第 1 个参数在 `edi`） |
| （缺 `mov esi,3` 是因为优化/常量传播，`-O0` 下通常会有） | —— |
| `call 401126 <add>` | **调用 add**（objdump 已标注符号名） |
| `mov esi,eax` | **返回值 `eax` → 第 2 个参数 `esi`**（`add` 的结果传给 `printf`） |
| `lea rdi,[rip+0xe9e]` | **第 1 个参数 = 字符串地址**（`rip` 相对寻址）→ 注释显示 `# 402004` |
| `call 401030 <printf@plt>` | 调用 printf（走 PLT） |
| `pop rbp` / `ret` | **函数尾声**：恢复栈帧、返回 |

**关键技巧**：

- **`@plt` 后缀 = 动态库函数** → 一眼看出「这个程序用了哪些库能力」；
- **`lea rdi,[rip+...]`** 几乎总是「装载一个字符串/全局地址」→ 用 `objdump -s -j .rodata` 看那个地址上是什么；
- `endbr64` 是 CET（控制流强制）指令，现代编译器都会插入，**不是恶意代码**。

```bash
# ② 看那个字符串到底是什么
objdump -s -j .rodata hello
```

```console
Contents of section .rodata:
 402000 01000200 00000000 73756d3d 25640a00  ........sum=%d..
```

**解读**：右侧 ASCII 列直接给出 `sum=%d\n` —— **`.rodata` 里的字符串是逆向时最直接的线索**（错误信息、URL、密钥、格式串）。

```bash
# ③ 用 ASCII 箭头可视化控制流（有分支时特别有用）
objdump -d -M intel --visualize-jumps=color --disassemble=add hello
```

```console
0000000000401126 <add>:
  401126:	f3 0f 1e fa          	endbr64
  40112a:	55                   	push   rbp
  40112b:	48 89 e5             	mov    rbp,rsp
  40112e:	89 7d fc             	mov    DWORD PTR [rbp-0x4],edi
  401131:	89 75 f8             	mov    DWORD PTR [rbp-0x8],esi
  401134:	8b 55 fc             	mov    edx,DWORD PTR [rbp-0x4]
  401137:	8b 45 f8             	mov    eax,DWORD PTR [rbp-0x8]
  40113a:	01 d0                	add    eax,edx
  40113c:	5d                   	pop    rbp
  40113d:	c3                   	ret
```

**解读**：`add` 的实现是「把 `edi`/`esi`（参数 1/2）存到栈上自己的局部变量，再读出来相加，结果放 `eax`」——典型的 `-O0` 未优化代码。**看懂了这些，就能识别「编译器生成的样板」与「真正的业务逻辑」**。

### 场景 3：C++ 去混淆 + 从崩溃地址定位代码 + 与 GDB 联动

**3a. C++ 符号还原**

```bash
objdump -d -C -M intel --disassemble=main cpp_target | grep -A5 'call'
```

```console
  4011a5:	e8 56 fe ff ff       	call   401000 <std::ostream::operator<<(int)@plt>
  4011b2:	e8 39 fe ff ff       	call   401020 <Box::getArea() const@plt>
```

**解读**：**没有 `-C` 你会看到 `_ZN3Box7getAreaEv` 这种混淆名**。`-C` 让 objdump 用 C++ 的 demangler 还原成 `Box::getArea() const` —— **可读性提升巨大**。

**3b. 只有崩溃地址时怎么定位（实战超常用）**

假设你在日志/EDR 里看到崩溃或异常地址 `0x401158`：

```bash
# ① 这个地址属于哪个函数？
objdump -d -M intel hello | grep -B20 '^  401158:'
```

```console
0000000000401146 <main>:
  ...
  401153:	b8 00 00 00 00       	mov    eax,0x0
  401158:	e8 c9 ff ff ff       	call   401126 <add>
```

**解读**：**`0x401158` 是 `main` 里调用 `add` 的那条 `call` 指令**。**「给一个地址，还原出『它在哪个函数、哪条指令、在做什么』」是逆向最基础也最有用的技能。**

```bash
# ② 反向：从符号找地址（给 gdb 下断点用）
objdump -t hello | awk '$4==".text" && $NF=="add" {print $1}'
```

```console
0000000000401126
```

```bash
# ③ 拿到地址后进入动态调试
gdb -q hello -ex 'set disassembly-flavor intel' -ex 'b *0x401126' -ex 'run' \
    -ex 'info registers rdi rsi' -ex 'x/i $rip' -batch
```

```console
Breakpoint 1 at 0x401126
Breakpoint 1, 0x0000000000401126 in add ()
rdi            0x5                 5        ← 参数 1 = 5（与静态反汇编一致）
rsi            0x3                 3        ← 参数 2 = 3
=> 0x401126 <add>:	endbr64
```

**解读**：**静态（objdump）提出的假设，用动态（GDB）验证** —— 这就是逆向的标准闭环。见 [`gdb.md`](gdb.md)。

**3c. 与 radare2/ghidra 的衔接**

```bash
# radare2：把 objdump 看到的地址直接丢进去分析
radare2 -A -q -c 's 0x401146; pdf' hello
```

```console
# 或 ghidra：导入二进制后按地址跳转（G 键）到 0x401146 看反编译结果
```

- 需要「伪 C 代码」→ [`ghidra.md`](ghidra.md) ｜ 需要交互探索/调试 → [`radare2.md`](radare2.md)

### 场景 4：交叉架构、裸二进制与补丁

**4a. 交叉架构反汇编（无对应硬件也能看）**

```bash
# 假设手上是 ARM 的目标文件（例如从固件里提取的）
file busybox_arm
```

```console
busybox_arm: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked
```

```bash
# objdump 需要 BFD 支持该架构：用 -i 确认；若不支持则装交叉 binutils
objdump -i | grep -i arm || echo "本机 objdump 不支持 ARM，需安装 binutils-arm-linux-gnueabi"
```

```bash
sudo apt install binutils-arm-linux-gnueabi binutils-mips-linux-gnu
arm-linux-gnueabi-objdump -d busybox_arm | head -20      # ARM 没有 -M intel（那是 x86 专用）
```

**解读**：**交叉工具的命名规律是 `<target>-objdump`**。IoT 固件逆向几乎必然用到这一套（见 [`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md)）。

**4b. 裸二进制（没有 ELF 头，如 shellcode/固件片段）**

```bash
# 用 -b binary 告诉 objdump「这是裸数据」，-m 指定架构
objdump -b binary -m i386:x86-64 -D -M intel shellcode.bin | head -20
```

```console
0000000000000000 <.data>:
   0:	48 31 c0             	xor    rax,rax
   3:	50                   	push   rax
   4:	48 bb 2f 62 69 6e 2f 	movabs rbx,0x68732f6e69622f
```

**解读**：**`-b binary -m <arch>` 是分析任意二进制的万能钥匙**（固件、shellcode、未知 blob）。见 [`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md)。

**4c. 用文件偏移定位、配合补丁（**授权 CTF / 自有程序**）**

```bash
# -F 显示文件偏移，方便与 hexdump/编辑器对应
objdump -d -F -M intel --disassemble=main hello | head
```

```console
0000000000401146 <main>:
/usr/bin/objdump: ... (file offsets 见各节 File off)
# 更直接：把「虚拟地址 → 文件偏移」换算出来
readelf -S hello | grep -A1 '\.text'
```

```console
  [13] .text             PROGBITS        0000000000401060  00001060
```

**解读**：**该节 `VMA = 0x401060`，`File off = 0x1060`** → 换算公式：`文件偏移 = 虚拟地址 - 0x401060 + 0x1060`。这就是「把逆向发现的 `jz` 改成 `jnz`（0x74→0x75）」时**该改文件里哪个字节**的计算方式。

---

## 6. 输出解读

### 6.1 反汇编行结构

```
  401158:	e8 c9 ff ff ff       	call   401126 <add>
  ──────  ───────────────       ────   ──────────────   ─────
   ①      ②                     ③      ④               ⑤
```

| 位置 | 含义 | 用途 |
|------|------|------|
| ① 地址 | 虚拟地址（PIE 时是偏移） | 下断点、算偏移 |
| ② 机器码 | 原始字节 | **打补丁时改的就是这些字节** |
| ③ 助记符 | 指令 | 控制流分析 |
| ④ 操作数 | 地址/寄存器/立即数 | 数据流分析 |
| ⑤ 符号注释 | `<add>`、`<printf@plt>` | **最快看懂「在调用什么」的地方** |

### 6.2 常见「符号提示词」

| 出现 | 含义 |
|------|------|
| `@plt` | 动态库函数（`printf@plt`、`strcmp@plt`） |
| `<函数名>` | objdump 命中符号表，直接给名字 |
| `_IO_stdin_used+0x4` | 只读节内的字符串（名字是编译器起的） |
| `endbr64` | CET 控制流强制（现代编译器常规插入） |
| `nop` / `nop WORD PTR` | 对齐填充 |
| `call rax` / `jmp QWORD PTR [rax*8+...]` | **间接调用/跳转表** → 静态看不到目标，**必须动态跟** |
| `fs:0x28` | 栈 canary（`__stack_chk_fail` 附近） |

### 6.3 保护机制快速判断（objdump + readelf）

| 保护 | 怎么看出来 | 含义 |
|------|-----------|------|
| **PIE** | `objdump -f` 显示 `DYN`（而非 `EXEC_P`） | 地址随机化 → 逆向要按偏移算，利用要泄露基址 |
| **NX** | `readelf -l \| grep GNU_STACK` 无 `E`（可执行）标志 | 栈不可执行 |
| **Canary** | 反汇编里出现 `fs:0x28` 与 `<__stack_chk_fail@plt>` | 栈保护 |
| **RELRO** | `readelf -d \| grep BIND_NOW`（Full / Partial） | GOT 是否只读 |
| **Fortify** | 出现 `__printf_chk` 等 `_chk` 函数 | 编译期加固 |

```bash
# 一条命令体检（同 5-场景 1 的用法）
file t && objdump -f t | grep -E 'EXEC_P|DYN' && readelf -l t | grep GNU_STACK
```

### 6.4 成功判据

- 能**说出每个关键函数的地址与作用**；
- 能把「某个行为」（如「打印字符串」）**对应到具体指令序列**；
- 能在需要时**把地址换算成文件偏移**（补丁/打点）；
- 静态得出的结论能**用 GDB 动态验证**。

---

## 7. 与其他工具配合

```
① 身份与结构
   file / objdump -f / objdump -h / readelf -h -l -S / checksec
        │
② 代码理解（静态）
   ├─ objdump -d -M intel -C            ← 本文：反汇编（权威、可脚本化）
   ├─ objdump -d -S -l                  ← 有调试信息时混排源码
   ├─ radare2 / rizin -A -c 'pdf @ main' ← 交互探索 + 交叉引用（radare2.md / rizin.md）
   └─ ghidra                            ← 反编译「类 C 代码」（ghidra.md）
        │
③ 数据与调用
   ├─ objdump -s -j .rodata             ← 只读字符串（线索最密集）
   ├─ objdump -T | grep UND             ← 导入了哪些库函数
   ├─ objdump -R                        ← GOT 重定位
   └─ strings -t x / nm                 ← 字符串与符号
        │
④ 动态验证（跑起来）
   ├─ gdb（断点/寄存器/栈/改状态）        ← gdb.md
   └─ ltrace / strace（库调用/系统调用）   ← ltrace.md
        │
⑤ 交叉架构 / 固件
   ├─ binutils-<target>（arm/mips 的 objdump）  ../09-数字取证/binwalk.md
   └─ objdump -b binary -m <arch> -D            ← 分析裸 blob
```

- 动态调试：[`gdb.md`](gdb.md) ｜ 调用跟踪：[`ltrace.md`](ltrace.md)
- 一体化框架：[`radare2.md`](radare2.md)、[`rizin.md`](rizin.md) ｜ 反编译器：[`ghidra.md`](ghidra.md)
- 固件场景：[`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `file format not recognized` | 不是可识别的目标格式（裸 blob/固件片段） | `objdump -b binary -m i386:x86-64 -D file` |
| `can't disassemble for architecture` | 该架构不在本机 BFD 支持列表 | `objdump -i` 确认；装交叉 binutils（`binutils-arm-linux-gnueabi`） |
| 反汇编出「乱七八糟的指令」 | 把数据当代码（线性扫描），或架构/位数猜错 | 用 `--start-address/--stop-address` 限定范围；确认 `-M` 位数 |
| 全是 `(bad)` 或 `.byte` | 起始地址没对齐到指令边界 | 调整 `-b`/`--start-address`；或换 radare2/ghidra 的分析 |
| 看不到函数名 | 二进制被 **strip** | `objdump -T`（动态符号仍在）；用 [`ghidra.md`](ghidra.md) 识别函数边界 |
| C++ 名字是 `_ZN...` | 没开 demangle | **加 `-C`** |
| AT&T 语法看不习惯 | 默认 AT&T | **加 `-M intel`** |
| 地址与运行时对不上 | 程序是 **PIE**，objdump 显示的是偏移 | 运行时基址 + 偏移；`gdb` 里 `info proc mappings` 拿基址；或 `--adjust-vma` |
| 输出太长 | 全量反汇编 | `--disassemble=<sym>` 定向；`--start-address/--stop-address` 限定 |
| 大文件输出极慢 | objdump 处理慢（尤其 C++ 大程序） | 用 `-j .text` + 地址范围；或改用 radare2/ghidra |
| `-s` 看节内容是一堆 hex | 这是设计如此 | 看右侧 ASCII 列；或用 `strings -t x` 配合地址 |
| `-g` 没有输出 | 编译时未加 `-g` | 无调试信息，改看反汇编；发行版分离的 debuginfo 用 `-L` 或装 `-dbgsym` 包 |
| `--visualize-jumps` 无效果 | binutils 版本较老 | 升级 binutils；或用 radare2 的控制流图 |
| 想改一个字节但不知道改哪 | 缺地址↔文件偏移换算 | `readelf -S` 拿节 VMA 与 File off，做减法 |

---

## 9. 防御视角（蓝队 / 软件保护）

objdump 是**纯静态读取工具**，本身不改变任何东西。对防御方的意义在两方面：

| 视角 | 内容 |
|------|------|
| **攻击者会用它做什么** | 快速摸清二进制结构、找字符串里的硬编码密钥/内部 URL、找库调用（判断语言与依赖）、定位校验函数 |
| **因此防御方应该怎么做** | ① **不要在二进制里硬编码密钥/口令/内部地址**（`strings` + `objdump -s` 一眼就看出来）；② **符号与调试信息应 strip**（`strip` 只是抬高门槛，但确实增加了成本）；③ **关键逻辑不要放在客户端**（见 [`gdb.md`](gdb.md) 场景 1 的结论）；④ 用**代码签名 + 完整性校验**防止被改（但要清楚**这些也能被绕过**） |
| **检测角度** | objdump 是离线工具，**没有运行时痕迹**；但如果有人在生产服务器上跑了逆向工具，进程/文件审计（auditd、EDR）可以捕获（`objdump`/`readelf`/`strings` + 目标为生产二进制） |
| **供应链视角** | 拿到第三方二进制时用 objdump 快速核对「是否与声称的版本/来源一致」（节表、符号、库依赖是否异常） |

**蓝队/开发可落地的四条**：

1. **发布前 `strip` 并移除调试信息**（至少不要带完整符号），同时**不要把源码路径与内部主机名留在二进制里**；
2. **不在客户端二进制里放密钥**（`objdump -s -j .rodata` + `strings` 就是审计手段，攻击者也会用）；
3. **对关键二进制做完整性校验与签名**，并在运行时验证（但要明白这不是绝对防护）；
4. **审计生产环境上的逆向工具使用**（`objdump`/`readelf`/`gdb`/`radare2` 出现在应用服务器上通常是异常信号）。

---

## 10. 参考

- GNU binutils 官方文档 · objdump：<https://sourceware.org/binutils/docs/binutils/objdump.html>
- binutils 手册页：`man objdump`
- Kali 说明：`objdump` **不在** Kali 官方工具清单中，来自 Debian 的 **`binutils`** 包（`autopsy` 等工具的依赖）。安装：`sudo apt install binutils`
- 配合阅读：[`gdb.md`](gdb.md)、[`ltrace.md`](ltrace.md)、[`radare2.md`](radare2.md)、[`rizin.md`](rizin.md)、[`ghidra.md`](ghidra.md)
- 本地命令：`objdump --help`、`objdump -i`、`info binutils`（如有）、`readelf --help`

## ⚠️ 法律与伦理

objdump 是**完全合法的开发与安全工具**（分析自己的程序、调试、CTF、开源软件研究、恶意样本分析都在正当用途内）。但以下行为可能违法：

- **逆向非自有软件以规避技术措施/DRM**（可能违反《著作权法》相关条款及许可协议）；
- **窃取商业秘密**（《反不正当竞争法》第 9 条）；
- **对未授权系统利用通过逆向发现的漏洞**（《刑法》第 285/286 条）；
- **分析他人设备中提取的二进制**而不具备授权（涉及《个人信息保护法》《数据安全法》）。

**请遵守**：

1. 只分析**自己的程序**、**开源软件（在其许可范围内）**、**CTF 靶题**、**书面授权的研究目标**；
2. 发现商业软件漏洞走**厂商漏洞披露流程**，不公开可直接利用的细节；
3. 恶意样本分析在**隔离环境**进行（断网虚拟机）；
4. 本教程示例请用自己编写的练习程序（如 5-场景 1 的 `hello.c`）复现。
