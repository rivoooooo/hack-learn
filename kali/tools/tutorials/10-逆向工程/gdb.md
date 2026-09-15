# GDB（GNU 调试器）

> **一句话**：在程序**运行**的过程中停下来看寄存器、内存、调用栈，一步步执行并改变它的行为——逆向与漏洞利用的「显微镜」。
> **分类**：逆向工程 / 动态调试 ｜ **Kali 包**：`gdb`（命令 `gdb`、`gdb-multiarch`、`gdbserver`；**Kali 官方工具清单中有 `gdb` 条目**）｜ **官方文档**：<https://sourceware.org/gdb/documentation/> ｜ `man gdb`

---

## 1. 它解决什么问题

静态工具（[`objdump.md`](objdump.md)、[`radare2.md`](radare2.md)、[`ghidra.md`](ghidra.md)）告诉你「程序**看起来**是什么样」。但很多问题只有**跑起来**才能回答：

| 问题 | 静态分析 | GDB |
|------|----------|-----|
| 这个函数到底被调用了没？参数是什么？ | 靠读代码猜 | 下断点，实际看到参数值 |
| 缓冲区溢出时，覆盖了返回地址吗？覆盖成了什么？ | 靠算偏移 | 断在崩溃点，直接看 `$rsp`/`$rip` |
| 这个加密的密钥是运行时算出来的什么？ | 极难静态推 | 断在加密函数，直接读内存 |
| 这个分支为什么走了 else？ | 靠推条件 | 断在 `jmp` 前，看标志寄存器 |
| 程序崩溃在哪一行？ | 只能看 core/日志 | 直接跑出 `SIGSEGV` 的位置与上下文 |
| 我想跳过 license 校验 | 需要打补丁改文件 | 运行时 `set $rip=...` / 改返回值 |

**GDB 是「动态」这一半，静态工具是「静态」那一半，两者必须配合。**

对比同类：

| 工具 | 定位 | 差异 |
|------|------|------|
| **GDB** | 命令行调试器（Linux 原生） | 最通用；可脚本化（Python API）；插件生态强 |
| **`gdb-multiarch`** | 多架构 GDB | 调试 ARM/MIPS 二进制（IoT 固件常用）；见 [`binwalk.md`](../09-数字取证/binwalk.md) |
| **`edb-debugger`** | 图形化调试器（Kali 清单中） | 类 OllyDbg 的界面，适合不习惯命令行的人 |
| **`radare2`/`rizin`（`-d`）** | 逆向框架自带调试器 | 反汇编与调试一体，可远程调试；见 [`radare2.md`](radare2.md) |
| **`ltrace`/`strace`** | 库调用/系统调用跟踪 | **不需要源码也不需断点**，直接看调用序列；见 [`ltrace.md`](ltrace.md) |
| **`ghidra`** | 反编译 + 调试 | 有图形反编译视图与调试器集成；见 [`ghidra.md`](ghidra.md) |

---

## 2. 工作原理

### 2.1 用户态调试的底层：ptrace

Linux 上 GDB 调试用户态程序的核心是 **`ptrace(2)`** 系统调用：

```
gdb ./target
   │
   ├─ fork() 出子进程 → 子进程调用 ptrace(PTRACE_TRACEME) → execve(target)
   │     （从此子进程的任何「信号/断点/系统调用」都会被内核暂停并通知父进程）
   │
   ├─ 设断点：把目标地址的**第一个字节替换为 0xCC**（int3 指令）
   │     ├─ 程序执行到 0xCC → CPU 触发 int3 异常 → 内核暂停进程 → 通知 GDB
   │     └─ GDB 把原字节写回、把 rip 回退 1 字节 → 你就「停在了断点」上
   │
   ├─ 读写内存/寄存器：ptrace(PTRACE_PEEKDATA / POKEDATA / GETREGS / SETREGS)
   │     → 这就是为什么 GDB 能「看寄存器」和「改值」
   │
   ├─ 单步：PTRACE_SINGLESTEP（硬件单步）或设置 TF 标志
   │
   └─ 继续运行：PTRACE_CONT
```

**这解释了几件重要的事**：

- **为什么断点数量有限？** 软件断点要改内存，理论上无限；但**硬件断点**受 CPU 调试寄存器限制（x86 上 4 个）。
- **为什么不能调试 setuid 程序？** 出于安全，内核**禁止**对 setuid/提权程序做 ptrace（否则任何用户都能劫持 root 程序）。绕过方式：以 root 运行 GDB，或复制一份并去掉 setuid 位。
- **为什么反调试能生效？** 程序自己调用 `ptrace(PTRACE_TRACEME)` —— 若已被调试则返回失败，从而判断「我正在被调试」。**逆向时遇到这种情况需要 patch 掉这个检查。**
- **为什么容器里调试受限？** 需要 `SYS_PTRACE` capability（Docker 的 `--cap-add=SYS_PTRACE`，或 `--security-opt seccomp=unconfined`）。

### 2.2 符号与调试信息

| 情况 | `gdb` 表现 | 怎么办 |
|------|-----------|--------|
| 编译时 `-g`（含 DWARF 调试信息） | 能显示**源码行、变量名、函数名、类型** | 最佳体验 |
| 有符号但无调试信息（未 strip） | 显示函数名（`main`、`check_license`），但无源码 | 仍可调试，靠反汇编 |
| **已 strip**（无符号） | 只显示地址（`0x401136`） | 靠 [`objdump.md`](objdump.md)/[`ghidra.md`](ghidra.md) 找关键地址，再在 GDB 里下断点 |

**编译一份带调试信息的练习程序**：

```bash
gcc -g -O0 -o target target.c        # -g 带调试信息，-O0 不做优化（便于调试）
```

**`-O2` 的坑**：优化会**重排/内联/删除**代码，导致「断点打不上」「变量显示 `<optimized out>`」。**逆向练习时优先用 `-O0`**；如果只能拿到 `-O2` 的二进制，就要靠反汇编理解。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install gdb
# 多架构（调试 ARM/MIPS 固件二进制时必须）
sudo apt install gdb-multiarch
# 源码与文档
sudo apt install gdb-source
```

```bash
gdb --version
```

```console
GNU gdb (GDB) 17.2
```

```bash
gdb --help | head -20
```

```console
This is the GNU debugger.  Usage:

    gdb [options] [executable-file [core-file or process-id]]
    gdb [options] --args executable-file [inferior-arguments ...]

Selection of debuggee and its files:

  --args             Arguments after executable-file are passed to inferior.
  --core=COREFILE    Analyze the core dump COREFILE.
  --exec=EXECFILE    Use EXECFILE as the executable.
  --pid=PID          Attach to running process PID.
  --directory=DIR    Search for source files in DIR.
  ...
```

最短流程：

```bash
gdb ./target
```

```console
(gdb) break main
Breakpoint 1 at 0x1149: file target.c, line 12.
(gdb) run
Starting program: /tmp/lab/target

Breakpoint 1, main () at target.c:12
12	    int x = atoi(argv[1]);
(gdb) next
(gdb) print x
$1 = 42
(gdb) info registers rip rsp rbp
rip            0x555555555149      0x555555555149 <main+4>
rsp            0x7fffffffe0e0      0x7fffffffe0e0
rbp            0x7fffffffe1f0      0x7fffffffe1f0
```

---

## 4. 核心参数详解

### 4.1 启动参数（命令行）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `gdb <prog>` | 加载程序 | —— |
| `--args <prog> <a1> <a2>` | 带参数启动 | 参数含空格/特殊字符时必用 |
| `--core=<file>` | 分析 **core dump** | 崩溃分析 |
| `--pid=<pid>` | **attach 到运行中的进程** | 需要在容器/宿主机有 `SYS_PTRACE` 权限 |
| `-x <file>` / `--command` | 启动时执行**命令脚本** | 自动化（配合 `-batch`） |
| `-ex '<cmd>'` | 启动时执行单条命令（可多次） | 一行式调试（**极实用**） |
| `-batch` | 执行完命令后退出（非交互） | **脚本化/CI/CTF 自动化必备** |
| `-q` / `--silent` | 不打印版本横幅 | 脚本输出更干净 |
| `--nh` | 不读 `~/.gdbinit` | 排除插件干扰（排错神器） |
| `-nx` | 不执行任何 init 文件 | 同上，更彻底 |
| `--readnow` / `--readnever` | 立即/不读符号表 | 大程序加速启动 |
| `--write` | 允许写入可执行文件与 core | **危险**（修改原程序） |
| `-w`（配合） | —— | —— |
| `-tui` | 启动 **TUI 界面**（分屏看源码/汇编） | 配合 `layout asm` |
| `--directory=<DIR>` | 源码搜索路径 | 源码在别处时用 |

### 4.2 最常用的执行控制命令

| 命令 | 缩写 | 作用 | 使用建议 |
|------|------|------|----------|
| `break <位置>` | `b` | 下断点 | `b main`、`b *0x401136`（**无符号时按地址**）、`b file.c:42` |
| `tbreak` | `tb` | **临时断点**（命中一次后删除） | 一次性的观察点 |
| `break <addr> if <cond>` | — | **条件断点** | `b *0x401136 if $rdi==0x1337` |
| `watch <expr>` | `wa` | **观察点**（值变化时中止） | 找「谁改了这个变量」 |
| `rwatch` / `awatch` | — | 读/读写观察点 | 找「谁读了这个地址」 |
| `catch syscall <name>` | — | 系统调用断点 | `catch syscall ptrace` 抓反调试 |
| `run [args]` | `r` | 运行 | `r $(python3 -c 'print("A"*100)')` |
| `continue` | `c` | 继续到下一个断点 | —— |
| `next` | `n` | **单步（跨过函数调用）** | 源码级 |
| `step` | `s` | **单步（进入函数）** | 源码级 |
| `nexti` / `stepi` | `ni` / `si` | **汇编级单步** | 无源码时的主要手段 |
| `finish` | `fin` | 运行到当前函数返回 | 快速看返回值 |
| `until <line>` | `u` | 运行到指定行 | 跳出循环 |
| `jump <addr>` | `j` | **跳转**（改变执行流） | 绕过校验（也会跳过初始化，慎用） |
| `kill` | `k` | 终止被调试程序 | —— |

### 4.3 查看信息（**逆向时的核心**）

| 命令 | 作用 | 说明 |
|------|------|------|
| `info registers` | 所有寄存器 | `info registers rip rsp rbp rax` 指定 |
| `print <expr>` / `p` | 打印表达式 | `p $rax`、`p *(int*)($rbp-0x10)`、`p/x $rip` |
| `x/<n><fmt><size> <addr>` | **检查内存** | `x/16xb $rsp`（16 字节 hex）、`x/s $rdi`（字符串）、`x/8i $rip`（反汇编 8 条） |
| `x/i $rip` | 反汇编当前指令 | **最常用的一条** |
| `disassemble` / `disas` | 反汇编函数 | `disas main`、`disas /r main`（带机器码） |
| `info breakpoints` | 断点列表 | `delete <n>` 删除；`disable <n>` 禁用 |
| `info functions` | 列出所有函数 | **无源码时找目标函数的第一步** |
| `info variables` | 列出全局变量 | —— |
| `backtrace` / `bt` | **调用栈** | `bt full`（含局部变量）、`bt 10`（前 10 层） |
| `frame <n>` | 切换到栈帧 | 配合 `bt` 看每一层的参数与局部变量 |
| `info frame` | 当前栈帧详情 | 看 saved rip/rbp |
| `info proc mappings` | **内存映射** | 找 libc 基址、堆/栈范围（**漏洞利用必用**） |
| `info threads` | 线程列表 | `thread <n>` 切换 |
| `info sharedlibrary` | 已加载的库 | 找 libc 是否已解析 |
| `ptype <type>` | 类型定义 | 有调试信息时看结构体布局 |
| `p sizeof(struct X)` | 结构体大小 | —— |
| `info symbol <addr>` | 地址属于哪个符号 | **收到崩溃地址时第一步** |

### 4.4 修改状态（**逆向/利用的关键能力**）

| 命令 | 作用 | 场景 |
|------|------|------|
| `set var x = 1` | 改局部/全局变量 | 跳过判断 |
| `set $rax = 0` | **改寄存器** | 让函数返回 0（绕过校验） |
| `set $rip = <addr>` | **改指令指针** | 直接跳转到目标代码 |
| `set {int}0x7fffffffe100 = 1` | 改内存 | 修改标志/结构体字段 |
| `set $eflags \|= 0x40` | 改标志寄存器（ZF=1） | 让条件跳转走我们想要的分支 |
| `call <func>(args)` | **在目标进程中调用函数** | 直接调用 `system("/bin/sh")`（授权环境下验证漏洞） |
| `print $rax = 0` | 打印并赋值 | 一行完成 |

### 4.5 界面与常用辅助

| 命令 | 作用 |
|------|------|
| `layout asm` / `layout regs` / `layout src` / `layout split` | **TUI 分屏**：汇编/寄存器/源码 |
| `Ctrl-x a` | 进入/退出 TUI |
| `Ctrl-l` | 刷新 TUI 花屏 |
| `focus cmd` | 焦点切到命令窗口 |
| `set disassembly-flavor intel` | **用 Intel 语法**（默认 AT&T） | 强烈建议放进 `.gdbinit` |
| `set pagination off` | 关闭分页 | 脚本化必需 |
| `set print pretty on` | 结构体美观输出 | —— |
| `define <name>` … `end` | 定义自定义命令 | 沉淀常用操作 |
| `python` … `end` | **执行 Python 脚本** | 自动化、解析内存、批量分析 |
| `record` / `reverse-continue` | **记录与反向执行** | 「时光倒流」式调试（性能开销大） |
| `generate-core-file` | 导出 core | 事后分析 |
| `attach <pid>` / `detach` | 附加/分离 | 调试运行中的服务 |
| `quit` / `q` | 退出 | —— |

### 4.6 增强插件（**强烈建议装一个**）

Kali 上可通过 pip/脚本安装（**不在 Kali 官方工具清单中**，需自行部署；也可先用 `gdb` 官方能力）：

| 插件 | 特点 | 安装方式 |
|------|------|----------|
| **GEF**（GDB Enhanced Features） | 单文件、轻量、命令丰富（`vmmap`、`heap`、`checksec`、`pattern`） | <https://github.com/hugsy/gef> |
| **pwndbg** | 功能最全（`heap`、`vis_heap_chunks`、`telescope`、`context`） | <https://github.com/pwndbg/pwndbg> |
| **PEDA** | 经典（`pattern create`/`pattern offset`、`checksec`） | <https://github.com/longld/peda> |

**怎么选**：做 pwn/CTF 优先 **pwndbg**（功能最全）；追求轻量用 **GEF**。**三个不要同时装**（互相冲突）。

**插件带来的高价值命令**（以 pwndbg/GEF 为例）：

| 命令 | 作用 |
|------|------|
| `checksec` | 查看二进制启用的保护（NX、PIE、Canary、RELRO） |
| `vmmap` | 彩色内存映射（快速找 libc 基址与可写段） |
| `telescope $rsp` / `x/32gx $rsp` | 栈回溯式查看（自动解析指针指向） |
| `pattern create 200` / `pattern offset $rip` | **精确计算溢出偏移**（pwn 必备） |
| `got` / `plt` | 查看 GOT/PLT 表 |
| `heap` / `bins` | 堆结构与 bin（做堆利用时必备） |
| `context` | 一屏汇总：寄存器 + 栈 + 反汇编 + 回溯 |
| `searchmem` / `search-pattern` | 在内存里搜字符串/字节 |
| `rop` / `ropgadget`（外部） | 找 ROP gadget |

---

## 5. 实战演练

> **环境声明**：以下全部使用**自己编写的练习程序**（或 CTF 靶题、你自己的靶场）。**禁止**用它调试你不拥有的生产系统进程、绕过你不拥有授权的软件许可，或对他人系统进行未授权调试。
> 下面的例子用自编程序，**自己编译、自己拥有**。

### 场景 1：从零开始调一个程序（源码级 + 无源码级）

**Step 1：准备一个练习程序**

```bash
mkdir -p /tmp/lab && cd /tmp/lab
cat > target.c <<'EOF'
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check(char *pw) {
    char buf[16];
    strcpy(buf, pw);                 /* 故意做的溢出点（练习用） */
    return strcmp(buf, "s3cr3t") == 0;
}

int main(int argc, char **argv) {
    if (argc < 2) { printf("usage: %s <password>\n", argv[0]); return 1; }
    if (check(argv[1])) {
        printf("Access granted\n");
    } else {
        printf("Access denied\n");
    }
    return 0;
}
EOF
gcc -g -O0 -fno-stack-protector -no-pie -o target target.c
```

```bash
# 确认保护状态（先了解自己在调什么）
checksec --file=./target 2>/dev/null || readelf -h ./target | grep Type
```

```console
Type:                              EXEC (Executable file)     ← 非 PIE，地址固定
```

**Step 2：源码级调试（有 `-g` 时最舒服）**

```bash
gdb -q ./target
```

```console
(gdb) set disassembly-flavor intel
(gdb) break check
Breakpoint 1 at 0x401176: file target.c, line 6.
(gdb) run wrongpass
Breakpoint 1, check (pw=0x7fffffffe6f8 "wrongpass") at target.c:6
6	    strcpy(buf, pw);
(gdb) next
7	    return strcmp(buf, "s3cr3t") == 0;
(gdb) print buf
$1 = "wrongpass\000\000\000\000\000\000\000"
(gdb) print sizeof(buf)
$2 = 16
(gdb) x/24xb buf
0x7fffffffe6d0:	0x77	0x72	0x6f	0x6e	0x67	0x70	0x61	0x73
0x7fffffffe6d8:	0x73	0x00	0x00	0x00	0x00	0x00	0x00	0x00
0x7fffffffe6e0:	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00
```

**解读**：`buf` 只有 **16 字节**，但 `strcpy` **没有长度检查** → 只要密码长度 ≥ 16 就会**覆盖栈上相邻的变量与保存的返回地址**。这就是经典的栈溢出。用 `finish` 让 `check` 返回，再观察 `$rsp`：

```console
(gdb) finish
Run till exit from #0  check (pw=0x7fffffffe6f8 "wrongpass") at target.c:7
0x00000000004011d3 in main (argc=2, argv=0x7fffffffe7e8) at target.c:12
Value returned is $3 = 0
(gdb) info registers rip rsp rbp
rip            0x4011d3            0x4011d3 <main+59>
rsp            0x7fffffffe6f0
rbp            0x7fffffffe6f0
```

**Step 3：改状态绕过校验（授权练习中用来说明「客户端校验不可靠」）**

```console
(gdb) break check
(gdb) run wrongpass
Breakpoint 1, check (pw=...) at target.c:6
(gdb) finish                 # 让 check 跑完再改返回值
(gdb) set $rax = 1           # 强制返回「成功」
(gdb) continue
```

```console
Access granted
```

**解读**：**你刚刚没有破解密码，只是让程序相信校验通过了**。这在真实场景里的意义是：**「有没有授权」的最终判断如果发生在客户端/本地，就一定可以被绕过** —— 这也是为什么 license 校验必须放到服务器端。

**Step 4：无源码调试（真实逆向的常态）**

```bash
# 造一个 strip 过的版本（无符号）
gcc -O2 -s -o target_stripped target.c
gdb -q ./target_stripped
```

```console
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401030  printf@plt
...
0x0000000000401130  main                       ← 还留着 main
```

```console
# 若连 main 都没有，就用 objdump 找入口，再顺着调用找关键函数
(gdb) break *0x401130        # 按地址下断点
Breakpoint 1 at 0x401130
(gdb) run wrongpass
Breakpoint 1, 0x0000000000401130 in main ()
(gdb) disas /r $rip, $rip+64
```

```console
Dump of assembler code from 0x401130 to 0x401170:
   0x0000000000401130 <main+0>:	push   rbp
   0x0000000000401131 <main+1>:	mov    rbp,rsp
   0x0000000000401134 <main+4>:	sub    rsp,0x10
=> 0x0000000000401138 <main+8>:	cmp    edi,0x2
```

**解读**：**无符号时的标准工作流**：

1. 用 [`objdump.md`](objdump.md) 或 [`ghidra.md`](ghidra.md) 静态找到「关键判断地址」；
2. 在 GDB 里 `break *<addr>`；
3. `si`/`ni` 单步，`x/i $rip` 看指令，`info registers` 看状态；
4. 用 `$rdi/$rsi/$rdx/$rcx/$r8/$r9`（**System V AMD64 的前 6 个参数**）读函数参数。

### 场景 2：栈溢出与偏移计算（pwn 的标准流程）

```bash
# ① 确认保护
gcc -g -O0 -fno-stack-protector -no-pie -o overflow overflow.c
checksec --file=./overflow
```

```console
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

**解读**：`No canary`（无栈保护）、`No PIE`（地址固定）→ **最容易被利用的组合**，适合学习。

```bash
# ② 用长输入触发崩溃，找到崩溃点
gdb -q ./overflow
```

```console
(gdb) run $(python3 -c 'print("A"*100)')
Program received signal SIGSEGV, Segmentation fault.
0x000000000040101a in ?? ()
(gdb) info registers rip rsp
rip            0x4141414141414141        ← 返回地址被 'AAAA...' 覆盖了！
rsp            0x7fffffffe768
(gdb) x/8gx $rsp
0x7fffffffe768:	0x4141414141414141	0x4141414141414141
```

**解读**：`rip = 0x4141414141414141` 说明**返回地址被 `0x41`（'A'）覆盖** → 存在溢出且可控。

```console
# ③ 精确计算「偏移」（从 buf 起始到返回地址的字节数）
#   方法 A：pwndbg / GEF / PEDA 的 pattern
(gdb) pattern create 200
(gdb) run <pattern-string>
(gdb) pattern offset $rip
```

```console
[+] Found at offset 24 (little-endian search) likely
```

```console
# 方法 B：不用插件也能算（手动数）
(gdb) break *0x4011XX        # 在函数返回前（ret 指令处）下断点
(gdb) run $(python3 -c 'print("A"*100)')
(gdb) p/x $rsp               # ret 时 rsp 指向返回地址
(gdb) p/x $rbp-0x10          # buf 的起始（示例）
# 偏移 = $rsp - buf_start = ...
```

**解读**：拿到偏移（例如 24）后，就可以构造 `b'A'*24 + p64(target_addr)`。**在授权 CTF/靶场里，下一步是找可跳转的目标地址（如 `win()` 函数或 `system`）**。

> ⚠️ **本节只是为了理解原理**。**在实际环境中利用漏洞需要明确授权**（CTF 比赛、授权渗透测试、自己的靶场）。详见文末法律提示。

### 场景 3：动态分析「密钥是怎么算出来的」+ 反调试对抗

**3a. 拦截加密函数，直接读出密钥**

```bash
# 目标程序在运行时才会算出密钥（静态看不到）
gdb -q ./crypto_app
```

```console
(gdb) break AES_set_encrypt_key
Function "AES_set_encrypt_key" not defined.
Make breakpoint pending on future shared library load? (y or [n]) y
Breakpoint 1 (AES_set_encrypt_key) pending.
(gdb) run
Breakpoint 1, AES_set_encrypt_key (userKey=0x7fffffffd8a0 "\x01\x02...", bits=128, key=...) at aes.c
(gdb) x/16xb userKey
0x7fffffffd8a0:	0x9a	0x3f	0x21	0x0c	0x77	0x2b	0x00	0x00
0x7fffffffd8a8:	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00
```

**解读**：**密钥在内存里被直接读出来了**。这就是动态调试相对静态分析的最大优势：**运行时的中间值（密钥、解密结果、派生值）静态工具根本看不到**。

```console
(gdb) backtrace
#0  AES_set_encrypt_key (...)
#1  0x00005555555552a1 in derive_key (seed=0x7fffffffda00 "hunter2") at crypto.c:42
#2  0x0000555555555410 in main (...)
```

**解读**：`backtrace` 直接告出「密钥是从 `derive_key("hunter2")` 派生的」——**一句命令定位了算法入口**，比静态硬啃快得多。

**3b. 反调试与绕过（理解防御机制）**

```bash
# 很多程序用 ptrace 自检来检测调试器
gdb -q ./antidebug
```

```console
(gdb) run
Program exited with code 01.        ← 没崩溃，直接退出：说明检测到调试了
```

```console
# 快速判断：是不是 ptrace 自检？
(gdb) catch syscall ptrace
Catchpoint 1 (syscall 'ptrace' [101])
(gdb) run
Catchpoint 1 (call to syscall ptrace), 0x00007ffff7ee2f5a in ptrace ()
(gdb) finish
(gdb) p $rax
$1 = -1                            ← PTRACE_TRACEME 失败（因为已被调试）
```

**解读**：`ptrace` 返回 `-1` → 程序知道自己在被调试。**理解这个机制**是逆向的基础；**绕过方法**（如修改返回值或跳过检测分支）：

```console
(gdb) break *0x4011XX            # 在检测分支处下断点
(gdb) commands
> set $eax = 0                   # 假装没被调试
> continue
> end
```

**替代方案**：用 **`gdb --pid` attach 之前先启动**，或使用支持「隐藏调试状态」的插件/内核模块（**这属于高级对抗技术，仅在授权研究与 CTF 中使用**）。

**3c. 用 Python 脚本自动化（GDB 的可编程性）**

```bash
cat > /tmp/lab/auto.gdb <<'EOF'
set pagination off
set confirm off
set disassembly-flavor intel
break main
run
# 打印入口处的前 10 条指令
x/10i $rip
info registers
# 遍历可写内存段，找可疑字符串
info proc mappings
quit
EOF
gdb -q -batch -x /tmp/lab/auto.gdb ./target
```

**解读**：`-batch -x` 让 GDB 变成**可脚本化的分析工具**，可以放进 CI 或批量处理一堆样本。

### 场景 4：调试远程/嵌入式目标（gdb + gdbserver）

固件里的二进制（ARM/MIPS）不能直接在 x86 Kali 上跑，需要用 **gdbserver + gdb-multiarch**：

```bash
# ① 目标机（或 qemu-user）上启动 gdbserver
gdbserver :1234 ./arm_binary
```

```console
Process ./arm_binary created; pid = 1234
Listening on port 1234
```

```bash
# ② Kali 上用多架构 GDB 连接
gdb-multiarch -q ./arm_binary
```

```console
(gdb) set architecture arm
(gdb) target remote 192.168.56.102:1234
Remote debugging using 192.168.56.102:1234
(gdb) break main
(gdb) continue
```

**解读**：这是**物联网固件逆向的标准流程**（配合 [`binwalk.md`](../09-数字取证/binwalk.md) 提取出的二进制）。**纯用户态二进制**也可以先用 `qemu-arm -g 1234 ./arm_binary` 起一个模拟环境，再用 `gdb-multiarch` 连——**不需要真实设备**。

---

## 6. 输出解读

### 6.1 寄存器（x86-64 System V）

| 寄存器 | 作用 | 逆向中怎么用 |
|--------|------|--------------|
| `rip` | **指令指针** | 崩溃地址 / 当前执行位置 |
| `rsp` | **栈顶指针** | `x/32gx $rsp` 看栈；溢出时 `rsp` 处常是被覆盖的返回地址 |
| `rbp` | 栈帧基址 | `$rbp-0x10` 之类的局部变量定位 |
| `rax` | 累加器 / **返回值** / 变参函数参数个数 | `set $rax=0` 绕过校验 |
| `rdi`, `rsi`, `rdx`, `rcx`, `r8`, `r9` | **函数参数 1–6** | 断在函数入口看参数 |
| `rdi`（函数入口处） | 第 1 个参数 | `char *s` 时用 `x/s $rdi` 看字符串 |
| `eflags` | **标志位**（ZF/CF/SF/OF） | 条件跳转的依据；`set $eflags \|= 0x40` 设 ZF |
| `cs`, `ss`, `fs`, `gs` | 段寄存器 | `fs` 在 x86-64 上指向 **TLS**（`fs:[0x28]` 是栈 canary） |

### 6.2 崩溃信号

| 信号 | 含义 | 常见原因 |
|------|------|----------|
| `SIGSEGV` | 段错误（非法内存访问） | 野指针、溢出错位、读空指针 |
| `SIGABRT` | 主动 abort | 堆破坏被检测（glibc 的 `*** stack smashing detected ***`） |
| `SIGILL` | 非法指令 | 执行了数据、跳错地址 |
| `SIGFPE` | 算术错误 | 除零 |
| `SIGTRAP` | 断点/陷阱 | **正常**（断点就是在用 int3） |
| `SIGINT` | Ctrl-C | 手动中断 |

**看到崩溃时固定动作顺序**：

```
1) info registers rip rsp rbp        ← 崩溃在哪、栈在哪
2) x/i $rip                          ← 那条指令是什么
3) bt                                ← 调用栈（谁调的）
4) info symbol $rip                  ← 这个地址属于哪个函数
5) x/8gx $rsp                        ← 栈上有什么
6) info proc mappings                ← 地址属于哪个段（libc? 堆? 栈?）
```

### 6.3 常见提示的含义

| 提示 | 含义 | 解决 |
|------|------|------|
| `No symbol table is loaded` | 二进制被 strip 了 | `info functions` / 按地址下断点；或先逆向找地址 |
| `Value optimized out` | 编译器优化（`-O2`）导致变量不可见 | 改看反汇编；或换 `-O0` 版本 |
| `Cannot access memory at address 0x...` | 地址无效（解引用空/野指针） | 检查寄存器值是否合理 |
| `Program received signal SIGSEGV` | 崩溃 | 按 6.2 的固定顺序分析 |
| `args must be given before` / 断点 pending | 库还没加载 | 答 `y` 设为 pending；或在 `main` 后再下断点 |
| `ptrace: Operation not permitted` | 权限/容器限制，或目标是 setuid | `sudo`、加 `SYS_PTRACE`、或去掉 setuid |
| `Missing separate debuginfos` | 缺系统库符号 | `debuginfo-install glibc`（可选，不影响主要调试） |

---

## 7. 与其他工具配合

```
① 静态概览（先看清「长什么样」）
   ├─ file / readelf -h            → 架构、类型、保护
   ├─ checksec                     → NX/PIE/Canary/RELRO
   ├─ objdump -d                   → 反汇编（objdump.md）
   ├─ ltrace / strace              → 库调用/系统调用序列（ltrace.md）
   ├─ radare2 / rizin              → 反汇编 + 分析 + 自带调试器（radare2.md/rizin.md）
   └─ ghidra                       → 反编译出「类 C 代码」（ghidra.md）
        │   （拿到关键函数地址）
        ▼
② 动态调试（本文，GDB）
   ├─ break *<addr> / b <func>     → 断点
   ├─ si/ni + x/i $rip             → 逐条指令
   ├─ info registers / x/gx $rsp   → 寄存器与栈
   ├─ set $rax=0 / set $rip=...    → 改状态绕过校验
   └─ call system("/bin/sh")       → 直接调用（**授权环境验证漏洞**）
        │
③ 利用与验证
   ├─ pwndbg/gef/peda 插件         → pattern offset / vmmap / heap
   ├─ ROPgadget / ropper           → 找 gadget
   └─ 写 exp（Python + pwntools）   → 授权 CTF/靶场
        │
④ 嵌入式/远程
   ├─ gdb-multiarch + gdbserver    → ARM/MIPS 二进制
   └─ qemu-user（-g 端口）          → 无设备时的模拟调试
```

- 反汇编基础：[`objdump.md`](objdump.md) ｜ 库调用追踪：[`ltrace.md`](ltrace.md)
- 一体化逆向框架：[`radare2.md`](radare2.md)、[`rizin.md`](rizin.md) ｜ 反编译器：[`ghidra.md`](ghidra.md)
- 固件里提取的二进制：[`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `No symbol table is loaded` | 二进制被 strip | `info functions` 看剩余符号；用 [`objdump.md`](objdump.md)/[`ghidra.md`](ghidra.md) 找地址后 `b *0x...` |
| 断点打不上/`Cannot insert breakpoint` | 地址是数据段、或 ASLR 导致地址变化 | 用函数名下断点；或用 `b *base+offset`（先 `info proc mappings` 取基址） |
| `Value optimized out` | `-O2` 优化 | 换 `-O0` 编译的版本调试；或只看反汇编 |
| `ptrace: Operation not permitted` | 容器缺 `SYS_PTRACE` / 目标是 setuid / 有 Yama 限制 | `docker --cap-add=SYS_PTRACE`；`sudo`；`echo 0 > /proc/sys/kernel/yama/ptrace_scope`（**仅自己的机器**） |
| 程序一启动就检测到调试 | 反调试（ptrace 自检/时间差/父进程检查） | `catch syscall ptrace` 定位；改返回值/跳分支；**仅授权环境** |
| AT&T 语法看不懂 | 默认汇编语法 | `.gdbinit` 里加 `set disassembly-flavor intel` |
| TUI 花屏 | 终端尺寸变化 | `Ctrl-l` 刷新；或 `layout regs` 重设 |
| 多个插件冲突/报错 | 同时装了 pwndbg+gef+peda | 只保留一个；用 `gdb --nh -nx` 排除 |
| `call system("/bin/sh")` 卡住 | 程序已崩溃/没有可用 shell 环境 | 先 `set disable-randomization on`、确保程序状态正常；或换 `execve` |
| 远程调试连不上 | gdbserver 未启动/端口/网络 | 目标上确认 `Listening on port`；`target remote <ip>:<port>`；检查防火墙 |
| 多架构二进制跑不起来 | 架构不匹配（ARM 在 x86 上） | `qemu-arm -g 1234 ./binary` + `gdb-multiarch` |
| 改了寄存器但程序行为没变 | 改错了寄存器（如返回值是 `eax` 而非 `rax` 高位）/被后续指令覆盖 | 确认 ABI（返回值在 `eax`）；`si` 单步验证 |
| 断点太多拖慢程序 | 软件断点 + ptrace 开销 | 用条件断点精确命中；或减少断点数量 |

---

## 9. 防御视角（蓝队 / 软件防护）

GDB 是**攻击者的工具**，对防御方的启示主要在「**让逆向与调试变难**」以及「**检测调试/注入行为**」。

| 攻击者能力 | 防御手段 | 说明 |
|------------|----------|------|
| 用 GDB attach 运行中的服务 | `ptrace_scope=1`（Yama）、`PR_SET_DUMPABLE=0`、seccomp 限制 `ptrace` | 默认 Ubuntu 已开 Yama；**不要让关键服务可被任意用户 ptrace** |
| 读内存拿密钥 | 密钥不常驻内存、用后立即擦除（`explicit_bzero`）、放进 TPM/HSM | **GDB 都能读到** —— 这是「内存中一定有明文」的证明 |
| 绕过本地校验 | **把安全判断放服务端**；本地只做 UX | 见 5-场景 1：客户端校验必然可绕 |
| 调试 setuid 程序 | 内核已禁止（安全设计）；**不要用 setuid 作为唯一防线** | 用 capabilities/服务拆分替代 |
| 反调试技术（ptrace 自检、时序检测、代码校验和） | 提高逆向成本 | **只是「抬高门槛」，不是绝对防护**；不要以为加了反调试就安全 |
| 检测调试/注入 | EDR 监控 `ptrace(PTRACE_ATTACH)`、`process_vm_readv`、`/proc/<pid>/mem` 写入 | 生产服务器上「谁在 attach 我的进程」是**高价值告警** |
| 内存中的凭据被 dump | 保护关键进程（Yama、只读内存段、机密进 TEE） | 见 [`../08-后渗透/mimikatz.md`](../08-后渗透/mimikatz.md) 的同类思路 |

**蓝队可落地的三条**：

1. **生产服务器限制 ptrace**：`/proc/sys/kernel/yama/ptrace_scope = 1`（或 2），并在关键服务上设 `PR_SET_DUMPABLE=0`；
2. **监控 attach 行为**：auditd 规则监听 `ptrace` 系统调用（尤其对数据库、Web 服务、SSH 进程的 attach）；
3. **不要把「客户端校验」「内存中的密钥」当成安全边界**：GDB 的存在本身就证明了「攻击者拥有本机控制权 = 拥有全部秘密」。

---

## 10. 参考

- GDB 官方文档（含 GDB/MI、Python API）：<https://sourceware.org/gdb/documentation/>
- GDB 官方 Wiki：<https://sourceware.org/gdb/wiki/>
- Kali 工具页（gdb）：<https://www.kali.org/tools/gdb/>
- GEF：<https://github.com/hugsy/gef> ｜ pwndbg：<https://github.com/pwndbg/pwndbg> ｜ PEDA：<https://github.com/longld/peda>
- 本地手册与资源：`man gdb`、`gdb --help`、`info gdb`、`gdb-multiarch --version`、`man gdbserver`、`man ptrace`

## ⚠️ 法律与伦理

GDB 是**合法的开发与安全研究工具**（调试自己写的程序、分析自己的软件、CTF、授权漏洞研究都是正当用途）。但以下行为可能违法：

- 对**没有权限的系统/进程**进行 attach 或内存读取（可能触犯《刑法》第 285 条：非法获取计算机信息系统数据）；
- **绕过软件许可/DRM** 以规避付费（可能违反《著作权法》关于技术措施的规定与许可协议）；
- 对**非自有软件**逆向以获取商业秘密（可能触犯《反不正当竞争法》第 9 条）；
- 利用调试得到的漏洞攻击未授权系统（《刑法》第 285/286 条）。

**请遵守**：

1. 只在**自己的程序、CTF 靶题、书面授权的研究目标、开源软件（在其许可范围内）**上使用；
2. 发现商业软件漏洞时，通过**厂商漏洞披露流程**上报，不要公开可直接利用的细节；
3. 授权测试中的调试操作要**记录时间与范围**，避免触碰生产系统；
4. 本教程的所有示例请用**自己编写的练习程序**（如 5-场景 1 的 `target.c`）在自己机器上复现。
