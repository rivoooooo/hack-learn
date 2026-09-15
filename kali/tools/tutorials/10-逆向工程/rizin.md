# Rizin（radare2 社区分叉 · 含 Cutter 图形界面）

> **一句话**：radare2 的**社区分叉**——把 r2 里「半成品、不稳定、不常用」的部分清理掉，保留可用的分析能力，命令与 r2 **高度相似**（`rz-*` 系列），并配套 **Cutter** 图形界面。
> **分类**：逆向工程 / 静态与动态分析 ｜ **Kali 包**：`rizin`（命令 `rizin`、`rz-bin`、`rz-asm`、`rz-hash`、`rz-diff`、`rz-find`、`rz-gg`、`rz-run`、`rz-ar`、`rz-ax`、`rz-test` 等）；图形界面来自 **`rizin-cutter`**（命令 `cutter`）｜ **官方文档**：<https://rizin.re/> ｜ 项目：<https://github.com/rizinorg/rizin>

---

## 1. 它解决什么问题

与 [`radare2.md`](radare2.md) 解决**同样的问题**（结构、逻辑、验证、补丁），差异在**工程取向**：

| 维度 | radare2 | **Rizin** |
|------|---------|-----------|
| 治理模式 | 主要由原作者主导 | **社区共治**（fork 后的开放治理） |
| 目标 | 试验性功能多、覆盖广 | **「能用的功能才保留」**：可用性、代码整洁、行为可预期 |
| 稳定性 | 命令/行为在大版本间变化较多 | **更保守**：不轻易改命令语义 |
| 反编译 | `pdc`（内置简化） | `pdc` + 配合 `rz-ghidra`（插件）可实现 Ghidra 反编译集成 |
| 图形界面 | 无官方 GUI（社区有第三方） | **官方维护 Cutter**（Qt GUI） |
| 包与命令 | `r2`/`rabin2`/`radiff2`… | `rizin`/`rz-bin`/`rz-diff`/`rz-asm`/`rz-hash`… |
| Kali 打包 | `radare2` 包 | `rizin` 包 + `rizin-cutter` 包（提供 `cutter`） |

**怎么选**：

- **想要图形界面** → Rizin + **Cutter**（Kali 里 `apt install rizin-cutter`）；
- **习惯命令行并且要最新特性** → radare2；
- **要稳定、可预期的行为（写脚本/团队协作）** → Rizin；
- **两者命令几乎通用**：会一个就会另一个（把 `r2` 换成 `rizin`、`rabin2` 换成 `rz-bin`）。

对比同类：

| 工具 | 定位 | 差异 |
|------|------|------|
| **Rizin** | 命令行逆向框架 | r2 的稳定分支取向 |
| **`cutter`（rizin-cutter 包）** | **图形界面** | 底层就是 rizin；反汇编/控制流图/调试/脚本一体 |
| **`radare2`** | 命令行框架 | 试验功能更多；见 [`radare2.md`](radare2.md) |
| **`ghidra`** | 反编译器 | 输出伪 C 代码；见 [`ghidra.md`](ghidra.md) |
| **`gdb`** | 调试器 | 精细调试更强；见 [`gdb.md`](gdb.md) |

---

## 2. 工作原理

与 radare2 完全一致（同一套代码血统），**核心命令体系相同**：

```
rizin target
   │
   ├─ 加载：IO 层 + RzBin（格式解析：ELF/PE/Mach-O/DEX/固件…）
   ├─ 分析：aa/aaa → 识别函数、基本块、CFG、交叉引用
   ├─ 交互命令（前缀规律与 r2 相同）：
   │    i*  信息      a*  分析      p*  打印/反汇编
   │    s   定位      f*  标志      /   搜索
   │    w*  写入      d*  调试      o*  打开
   │    V   可视      q   退出      ?   帮助
   └─ 插件：rz-ghidra（反编译）、rz-decompiler 等
```

**rizin 相对 r2 的关键变化（迁移时会遇到的差异）**：

| 项目 | r2 | rizin |
|------|----|-------|
| 主命令 | `r2` / `radare2` | **`rizin`** |
| bin 工具 | `rabin2` | **`rz-bin`** |
| 汇编工具 | `rasm2` | **`rz-asm`** |
| 哈希工具 | `rahash2` | **`rz-hash`** |
| 差异比较 | `radiff2` | **`rz-diff`**（且有 `-d myers/leven/ssdeep/lcs-roll` 多种算法） |
| 搜索工具 | `rafind2` | **`rz-find`** |
| shellcode | `ragg2` | **`rz-gg`** |
| 进制转换 | `rax2` | **`rz-ax`** |
| 运行环境 | `rarun2` | **`rz-run`**（改为**指令/脚本文件**风格，不再只吃 profile） |
| 项目文件 | `.r2` 项目 | **`.rzdb`** 项目（`-p` 加载） |
| 脚本 | r2 脚本 | **rz 脚本 + 支持 `-i` 脚本、`#!` shebang 脚本** |
| 调试 | `-d` | `-d`（同样支持） |

**交互命令层面**：`aa`/`aaa`/`afl`/`pdf`/`axt`/`VV`/`~` 过滤器/`wx`/`wa` **全部相同**——**本文不再重复讲这些命令，请直接看 [`radare2.md`](radare2.md) 第 4–6 节**，那里讲得最细。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install rizin
# 图形界面（Cutter，基于 rizin）
sudo apt install rizin-cutter
rz-bin -v
rizin -v
```

```console
root@kali:~# rizin -h
Usage: rizin [-ACdfLMnNqStuvwzX] [-P patch] [-p prj] [-a arch] [-b bits] [-i file]
             [-s addr] [-B baddr] [-m maddr] [-c cmd] [-e k=v] file|pid|-|--|=
 --         Run rizin without opening any file
 =          Same as 'rizin malloc://512'
 -          Read file from stdin
 -A         Run 'aaa' command to analyze all referenced code
 -a arch    Set asm.arch
 -b bits    Set asm.bits
 -B baddr   Set base address for PIE binaries
 -c 'cmd..' Execute rizin command
 -d         Debug the executable 'file' or running process 'pid'
 -e k=v     Evaluate config var
 -E endian  Endianness -E big or -E little
 -p p.rzdb  Load project file
 -q         Quiet mode (no prompt) and quit after -i and -c
 -w         Open file in write mode
 -z, -zz    Do not load strings or load them even in raw
```

最短流程：

```bash
rizin -A -q ./crackme
```

```console
[0x00401060]> afl~check
0x00401126    4 73           sym.check
[0x00401060]> pdf @ sym.check
[0x00401060]> axt @ sym.imp.strcmp
[0x00401060]> VV
```

**图形界面**：

```bash
cutter                     # 打开 GUI，在里面 File → Open 选择二进制
```

```console
# Cutter 首次启动会让你选择主题与配置；之后可以：
#   - 左侧：函数/字符串/导入/符号列表（点击即跳转）
#   - 中间：反汇编 / 图形（控制流图）/ 十六进制视图切换
#   - 底部：命令输入框（支持 rizin 命令）+ 输出
#   - 右键函数：重命名、查看反编译（需 rz-ghidra 插件）
```

---

## 4. 核心参数详解

### 4.1 `rizin` 启动参数（真实参数）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-A` | 启动即执行 `aaa`（全量分析） | 小文件首选 |
| `-a <arch>` | 设置架构 | `-a arm`、`-a x86` |
| `-b <bits>` | 设置位数 | `-b 32`、`-b 64` |
| `-B <baddr>` | **设置基址**（PIE） | 与运行时对齐 |
| `-c 'cmd..'` | **执行命令**（可重复） | 脚本化核心 |
| `-d` | **调试模式**（文件或 pid） | `rizin -d ./target` |
| `-D <backend>` | 调试后端 | 指定 debug 后端 |
| `-e k=v` | 设置配置变量 | `-e asm.syntax=intel` |
| `-E <endian>` | 字节序（`big`/`little`） | 裸二进制分析 |
| `-i <file>` | 启动后运行脚本文件 | 自动化 |
| `-I <file>` | **在打开文件之前**运行脚本 | 需要先改配置时用 |
| `-k <OS/kern>` | 设置 `asm.os` | `-k linux`、`-k w32` |
| `-l <lib>` | 加载插件文件 | —— |
| `-L` | 列出 IO 插件 | 排错 |
| `-m <addr>` | 映射文件到指定地址（加载地址） | 裸二进制/固件 |
| `-M` | 不 demangle 符号名 | 想保留原名时 |
| `-n` / `-nn` | 不加载 RzBin 信息 / 只加载结构 | 非常规文件 |
| `-N` / `-NN` | 不加载用户配置 / 不加载任何脚本与插件 | **排错神器** |
| `-p <p.rzdb>` | **加载项目文件** | 大型分析续做 |
| `-q` / `-qq` | 静默（`-i`/`-c` 后退出）/ 强制退出 | 脚本化 |
| `-r <rz-run>` | 指定 `rz-run` profile | 调试时设置环境 |
| `-R <rule>` | 自定义 rz-run 指令 | —— |
| `-s <addr>` | 起始定位地址 | `-s main` |
| `-T` | **不计算文件哈希** | 大文件加速启动 |
| `-u` | `bin.filter=false`（保留原始符号/节名） | 名字被改得看不懂时用 |
| `-w` | **以写模式打开**（可打补丁） | 先备份 |
| `-x` | 打开时不加执行标志 | 纯数据文件 |
| `-X` | `bin.usextr=false` | dyldcache 等场景 |
| `-z` / `-zz` | 不加载字符串 / 连 raw 字符串一起加载 | 大文件加速 |
| `--` | 不打开任何文件启动 | 纯计算/调试 attach |

### 4.2 配套工具参数要点

| 工具 | 关键参数 | 说明 |
|------|----------|------|
| **`rz-bin`** | `-I`（信息）、`-S`（节）、`-s`（符号）、`-i`（导入）、`-z`/`-zz`/`-zzz`（字符串）、`-j`（JSON）、`-g`（**全量信息**）、`-K <algo>`（算校验和）、`-d`（DWARF）、`-Y`（**推测固件基址候选**） | 不开交互，最适合脚本与快速摸底 |
| **`rz-asm`** | `-a`（架构）、`-b`（位数）、`-d`/`-D`（反汇编）、`-s`（语法 `intel`/`att`）、`-F in:out`（过滤器如 `att2intel`）、`-E`（ESIL）、`-I`（RzIL）、`-L`（列插件） | 汇编/反汇编译器 |
| **`rz-hash`** | `-a algo1,algo2`、`-B`（逐块）、`-b size`、`-c hash`（**比对**）、`-f/-t`（起止偏移）、`-E`/`-D`（加/解密）、`-S`（种子）、`-K`（HMAC 密钥）、`-j`（JSON）、`-qq`（只输出值） | 比 `md5sum` 强：**可分块、可比对、可加解密** |
| **`rz-diff`** | `-t <bytes\|lines\|functions\|classes\|imports\|sections\|strings\|symbols\|entries\|fields\|libraries>`、`-d <myers\|leven\|ssdeep\|lcs-roll>`、`-C`（代码差异）、`-g`（函数图对比）、`-j`（JSON）、`-H`（可视化） | **`-t functions` 是最实用的**（函数级差异） |
| **`rz-find`** | `-s <str>`、`-w <str>`（宽字符）、`-x <hex>`、`-e <regex>`、`-z`（零结尾字符串）、`-m`（**magic 雕刻**）、`-i`（识别类型）、`-M <mask>`、`-a <align>` | 搜索 + 文件类型识别 |
| **`rz-gg`** | `-a`/`-b`/`-k`（架构/位数/OS）、`-i <shellcode 插件>`、`-E <encoder>`、`-f <raw\|c\|pe\|elf\|mach0\|python\|javascript>`、`-p`（padding）、`-S <str>`、`-L`（列插件） | **生成 shellcode / 把 asm 编译成裸二进制**（**授权 CTF/靶场用**） |
| **`rz-ax`** | 进制/格式转换（hex↔dec、float、base64、IP、时间戳、raw↔hexstr）、`-e`（交换字节序）、`-c`（C 字符串） | 数据换算 |
| **`rz-run`** | **指令/脚本文件风格**：`rz-run [directives \| script.rz] [-- program [args]]`；`-l`（列出指令）、`-t`（输出模板）、`-w`（等待终端） | 与 r2 的 `rarun2` 语义不同（**迁移注意点**） |
| **`rz-ar`** | 归档（ar 格式）操作 | —— |
| **`rz-test`** | 回归测试 | 开发用 |

---

## 5. 实战演练

> **环境声明**：全部使用**自己编写的练习程序**、CTF 靶题、开源软件（在许可范围内）。**禁止**对非自有软件逆向以规避许可/DRM，或窃取商业秘密，或对未授权系统利用漏洞。
> 沿用 [`radare2.md`](radare2.md) 第 5 节的 `crackme.c`（自编），演示 rizin 的用法与差异。

### 场景 1：命令行快速摸底（与 r2 几乎相同）

```bash
mkdir -p /tmp/lab && cd /tmp/lab
# 复用 radare2.md 场景 1 的程序，或自己写一个
cat > crackme.c <<'EOF'
#include <stdio.h>
#include <string.h>
static int check(const char *s) {
    if (strlen(s) != 8) return 0;
    if (s[0] != 'r' || s[1] != 'z') return 0;
    return strcmp(s + 2, "OOKS!") == 0;   /* rzOOKS! */
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
# ① 不开交互，先用 rz-bin 摸清结构（等价 rabin2）
rz-bin -I ./crackme
rz-bin -s ./crackme | grep -i check
rz-bin -z ./crackme | head
```

```console
arch     x86
baddr    0x400000
bintype  elf
bits     64
class    ELF64
lang     c
machine  AMD x86-64 architecture
os       linux
static   false
stripped false
```

```console
14  0x00001126 0x00401126 LOCAL  FUNC   8 check
54  0x00001146 0x00401146 LOCAL  FUNC  49 main
```

```console
nth paddr      vaddr      len size section type  string
0   0x00002004 0x00402004 10  11   .rodata ascii Password: 
1   0x0000200f 0x0040200f 8   9    .rodata ascii Correct!
2   0x00002018 0x00402018 6   7    .rodata ascii Wrong!
3   0x0000201f 0x0040201f 5   6    .rodata ascii OOKS!
```

**解读**：`rz-bin` 一次调用就拿到了「架构 + 是否 strip + 函数地址 + 所有字符串」。**`stripped false` 与 `OOKS!` 一起出现，基本就锁定了校验逻辑**。

```bash
# ② 交互式分析
rizin -A -q ./crackme
```

```console
[0x00401060]> afl~check
0x00401126    4 73           sym.check
[0x00401060]> pdf @ sym.check
```

```console
            ;-- check:
            ; CALL XREF from sym.main @ 0x4011c5(x)
┌ 73: sym.check (int64_t arg1);
│           0x00401126      endbr64
│           0x0040112a      push  rbp
│           ...
│           0x0040113d      call  sym.imp.strlen
│           0x00401142      cmp   rax, 8
│       ┌─< 0x00401146      je    0x40114c
│       │   0x00401148      mov   eax, 0
│      ┌──< 0x40114d      jmp   0x4011a2
│      │└─> 0x0040114c      mov   rax, qword [rbp - 0x18]
│      │    0x00401150      movzx eax, byte [rax]
│      │    0x00401153      cmp   al, 0x72           ; 'r'
│      │┌─< 0x00401155      jne   0x4011a0
│      ││   0x00401157      mov   rax, qword [rbp - 0x18]
│      ││   0x0040115b      movzx eax, byte [rax + 1]
│      ││   0x0040115e      cmp   al, 0x7a           ; 'z'
│      ││┌─< 0x00401160      jne   0x4011a0
│      │││   0x00401162      mov   rax, qword [rbp - 0x18]
│      │││   0x00401166      add   rax, 2
│      │││   0x00401169      lea   rsi, [0x0040201f]  ; "OOKS!"
│      │││   0x00401170      mov   rdi, rax
│      │││   0x00401173      call  sym.imp.strcmp
```

**解读**：与 r2 的输出格式一致 —— `; CALL XREF from`、`; 'r'`、`; "OOKS!"` 这些注释让**答案（`rzOOKS!`）直接可读**。

```bash
# ③ 交叉引用（谁用了 strcmp / "OOKS!"）
```

```console
[0x00401060]> axt @ sym.imp.strcmp
sym.check 0x401173 [CALL] call sym.imp.strcmp
[0x00401060]> axt @ 0x0040201f
sym.check 0x401169 [DATA] lea rsi, [0x0040201f]
[0x00401060]> pdc @ sym.check
```

```c
int sym.check (int64_t arg1) {
    if (sym.imp.strlen (arg1) != 8) return 0;
    if (*(char *)arg1 != 'r' || *(char *)(arg1 + 1) != 'z') return 0;
    if (sym.imp.strcmp ((arg1 + 2), "OOKS!") != 0) return 0;
    return 1;
}
```

### 场景 2：Cutter 图形界面（不想背命令就用它）

```bash
sudo apt install rizin-cutter
cutter
```

**Cutter 的操作地图**（上手只需要记这些）：

| 位置 | 内容 | 用途 |
|------|------|------|
| **左侧栏** | Functions / Strings / Imports / Symbols / Sections | **点击即跳转**（比命令快） |
| **中间视图** | Disassembly / Graph（控制流图）/ Hex / Decompiler | 切换标签看不同视角 |
| **底部命令框** | 输入 **rizin 命令** | GUI 与 CLI 混用（**这是 Cutter 最大的优势**） |
| **右键函数** | Rename / Decompile / Add Comment / X-Refs | **X-Refs 就是 `axt` 的图形版** |
| **快捷键** | 空格（切换 Hex/Disasm）、`G`（跳地址）、`;`（加注释）、`N`（重命名） | 高频动作 |

**典型流程（在 Cutter 里完成一轮分析）**：

```
1. File → Open → 选 crackme        → 自动分析（进度条走完）
2. 左侧 Functions 里找 check        → 双击跳转
3. 中间切到 Graph 视图              → 看分支结构（等价 VV）
4. 右键 check → X-Refs             → 看谁调用了它（等价 axt）
5. 右侧 Decompiler（需 rz-ghidra）  → 看伪 C 代码（等价 pdc，但更完整）
6. 重命名函数/变量（N 键）           → 让分析结果可读
7. 底部命令框输入 px 64 / izz~pass   → 需要时回到 CLI
```

**解读**：**Cutter 的价值是「图形导航 + CLI 兜底」**。它底层完全就是 rizin —— **你在 Cutter 里学到的命令，在纯命令行 rizin 里同样可用**（反之亦然）。

### 场景 3：rz-diff 版本比对 + rz-asm / rz-find 辅助

**3a. 函数级差异（找「新版改了什么」）**

```bash
# 造两个版本（模拟「厂商打了个补丁」）
sed 's/!= 8/!= 9/' crackme.c > crackme_v2.c
gcc -O0 -o crackme_v2 crackme_v2.c
```

```bash
rz-diff -t functions ./crackme ./crackme_v2
```

```console
0x00401126 sym.check
  A: 73 bytes
  B: 73 bytes
  match: 0.93
```

```bash
# 更细：字节级差异 + 可视化
rz-diff -H ./crackme ./crackme_v2 | head -20
```

```bash
# 只看字符串差异（找新增/删除的字符串）
rz-diff -t strings ./crackme ./crackme_v2
```

**解读**：`rz-diff -t functions` 的 `match` 比率能告诉你「哪个函数被改了」——**这是「从补丁反推漏洞」的最高效路径**（**只在授权的研究/CTF 中使用**）。

```bash
# 用算法选项做真值比对
rz-diff -d ssdeep ./crackme ./crackme_v2       # 上下文分块哈希相似度
rz-diff -d myers ./crackme ./crackme_v2        # 编辑距离（不許替换）
rz-diff -d leven ./crackme ./crackme_v2        # Levenshtein 编辑距离
```

**3b. 汇编/反汇编译 + 搜索**

```bash
# 反汇编一段 hex（x86-64）
rz-asm -a x86 -b 64 -d 554889e54883ec20
```

```console
push rbp
mov rbp, rsp
sub rsp, 0x20
```

```bash
# 汇编一条指令看字节
rz-asm -a x86 -b 64 'mov eax, 1; ret'
```

```console
b801000000c3
```

```bash
# 转换语法（AT&T → Intel）
rz-asm -a x86 -b 64 -d -F att2intel 488b45f8
```

```console
mov rax, qword [rbp - 8]
```

```bash
# 搜索：字符串 / 宽字符 / 正则 / magic 雕刻 / 偏移对齐
rz-find -s "OOKS!" ./crackme
```

```console
0x0000201f hit0_0 "OOKS!"
```

```bash
rz-find -e 'r.OOKS' ./crackme            # 正则
rz-find -x 4f4f4b53 ./crackme            # 搜字节
rz-find -i ./crackme                     # 识别文件类型
```

**3c. 哈希与校验（`rz-hash` 比 `md5sum` 强在哪）**

```bash
# 多算法 + 逐块 + JSON
rz-hash -a md5,sha256 -j ./crackme | head -20
```

```bash
# 分块哈希（大文件/镜像分析时有用）
rz-hash -a sha256 -b 4096 -B -qq ./crackme | head -3
```

```bash
# 校验：与已知哈希比对（脚本友好）
KNOWN=$(rz-hash -a sha256 -qq ./crackme)
rz-hash -a sha256 -c "$KNOWN" ./crackme && echo "哈希一致"
```

```bash
# 从偏移处哈希（配合 TSK 分析镜像里的某一段）
rz-hash -a sha256 -f 0 -t 4096 ./crackme
```

**3d. 脚本化（把分析流程固化）**

```bash
cat > /tmp/lab/triage.rz <<'EOF'
# ===== rizin 批量体检脚本（rizin -i triage.rz ./sample）=====
e asm.syntax=intel
e scr.color=3
echo "== 文件头 =="
iI~stripped,static,bits,arch
echo "== 函数数 =="
aflc
echo "== 可疑字符串 =="
izz~pass
izz~key
izz~http
echo "== 危险 API 引用 =="
axt @ sym.imp.system
axt @ sym.imp.execve
axt @ sym.imp.strcpy
EOF
rizin -A -q -i /tmp/lab/triage.rz ./crackme
```

```bash
# 或用 -c 一行搞定（适合放进 Shell 循环批量处理样本）
for f in ./samples/*; do
  echo "### $f"
  rizin -q -c 'aa; aflc; izz~pass; axt @ sym.imp.system; q' "$f"
done
```

---

## 6. 输出解读

**与 radare2 完全一致**（同一套命令与输出格式）。请直接参考 [`radare2.md`](radare2.md) 第 6 节：

- `pdf` 输出的标记（`;-- name:`、`; CALL XREF from`、`; "string"`、ASCII 控制流线）；
- 信息命令的重点（`iI` 的 `stripped`/`static`、`ii` 的导入函数、`izz` 的字符串）；
- `VV` 控制流图的读法。

**rizin 特有/增强的部分**：

| 项目 | 说明 |
|------|------|
| `rz-bin -Y` | **推测固件二进制的基址候选**（配合 [`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md) 做固件分析有用） |
| `rz-asm -I` | 输出 **RzIL**（中间语言）并校验——适合做**语义级分析/去混淆研究** |
| `rz-diff -d ssdeep / myers / leven / lcs-roll` | 多种**差异算法**，可按场景选（相似度 vs 编辑距离） |
| `rz-diff -t <类型>` | 按**函数/字符串/导入/节/类/符号**等维度比对（比字节 diff 更有语义） |
| `-T` 启动参数 | 不计算文件哈希（大文件启动加速） |
| `-p *.rzdb` | 项目文件为 `.rzdb` 格式 |

---

## 7. 与其他工具配合

```
① 结构摸底
   rz-bin -I/-S/-s/-i/-z/-g   ← 不开交互（最适合脚本）
   rizin -q -c 'iI; iS; ii; izz'  ← 一条命令出全套
        │
② 交互分析（同 radare2 的命令体系）
   aa/aaa → afl → pdf @ <func> → axt @ <addr> → VV → pdc
   ~ 过滤器（pdf~call / izz~passwd）
   afn 重命名（把 fcn.xxx 变成可读）
        │
③ 图形化（Cutter）
   cutter → 左侧列表跳转 / Graph 视图 / X-Refs / Decompiler（需 rz-ghidra）
        │
④ 动态验证
   rizin -d ./target（集成调试） / rz-run（设置运行环境）
   gdb + pwndbg/gef（更成熟的调试器）  ← gdb.md
        │
⑤ 差异与批量
   rz-diff -t functions（版本比对）/ rz-find（搜索）/ rz-hash（哈希）
   rizin -c '...' 批处理 / -i 脚本
        │
⑥ 需要伪 C 代码
   rz-ghidra 插件 / cutter 的 Decompiler / ghidra（独立工具）  ← ghidra.md
```

**配套工具速用**：

```bash
rz-bin -I ./crackme             # 二进制信息
rz-bin -z ./crackme             # 字符串（带地址）
rz-bin -i ./crackme             # 导入表
rz-find -s "OOKS!" ./crackme    # 搜字符串
rz-find -m ./firmware.bin       # magic 雕刻
rz-diff -t functions a b        # 函数级差异
rz-hash -a sha256 -qq ./crackme # 哈希
rz-asm -a x86 -b 64 -d 554889e5 # 反汇编
rz-asm -a x86 -b 64 'ret'       # 汇编
rz-ax 0x401126                  # 进制转换
rz-run -t                       # 输出 rz-run 模板
```

- radare2（母项目，命令详解）：[`radare2.md`](radare2.md)
- 反编译器：[`ghidra.md`](ghidra.md) ｜ 调试：[`gdb.md`](gdb.md) ｜ 反汇编基础：[`objdump.md`](objdump.md) ｜ 库调用：[`ltrace.md`](ltrace.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 照着 r2 教程敲命令报错 | **工具名前缀不同**（`rabin2`→`rz-bin` 等） | 见第 2 节的对照表 |
| `afl` 空/函数很少 | 没分析 | 先 `aa`（或 `-A`） |
| 汇编语法看着别扭 | 默认 AT&T | `e asm.syntax=intel`（或 `-e asm.syntax=intel`） |
| 地址与运行时不一致 | PIE | `-B <运行时基址>` |
| `-d` 报 ptrace 权限错误 | Yama / 容器缺 `SYS_PTRACE` | `sudo`、加 `--cap-add=SYS_PTRACE`（**仅自己的环境**） |
| 想用反编译但 `pdc` 太简单 | 内置反编译是简化版 | 装 **rz-ghidra** 插件（Cutter 里开 Decompiler 标签），或用 [`ghidra.md`](ghidra.md) |
| Cutter 里看不到 Decompiler 标签 | 未装 rz-ghidra | `apt search rz-ghidra` / 按 Cutter 文档安装插件 |
| Cutter 打开大文件卡住 | 全量分析开销大 | 先在 CLI 用 `aa` 部分分析并存项目；或在 Cutter 里选择较轻的分析选项 |
| `rz-run` 用法与 `rarun2` 不一样 | rizin 改了语义（指令/脚本风格） | `rz-run -l` 列指令、`rz-run -t` 出模板 |
| 项目文件打不开 | r2 的 `.r2` 项目与 rizin 的 `.rzdb` **不通用** | 用各自工具生成的项目文件 |
| 补丁没生效 | 用了 `io.cache` 未提交 | `wci` 提交；或确认改的是副本 |
| `rz-diff` 的输出看不懂 | 缺少 `-t`/`-d` 选择 | 常用：`rz-diff -t functions a b`、`rz-diff -t strings a b` |

---

## 9. 防御视角（蓝队 / 恶意样本分析）

**与 radare2 完全相同**（同一套分析能力），请参考 [`radare2.md`](radare2.md) 第 9 节。rizin 场景下的补充：

| 场景 | rizin 的便利之处 |
|------|------------------|
| **样本家族比对** | `rz-diff -t functions` / `-d ssdeep` 快速判断「两个样本是否同源」（**恶意样本分析中最常用的手段**） |
| IOC 提取 | `rz-bin -z` + `rz-find -e`（正则搜 URL/IP） |
| 固件二进制基址推测 | `rz-bin -Y`（配合 [`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md)） |
| 团队协作 | Cutter 的图形界面便于**向非逆向同事展示结论**（截图、标注、重命名后保存项目） |
| 二进制加固评估 | `rz-bin -I` 看 `stripped`/`static`；配合 canary/PIE 检查 |
| 供应链核对 | `rz-bin -I/-i/-S` 与官方版本对比 |

**蓝队三条**（与 r2 相同）：

1. **样本分析在隔离环境**，记录 `rz-hash` 得到哈希用于情报共享；
2. **把「可疑 API 组合」做成检测规则**（`socket`+`connect`+`system`+`unlink` 等在服务端二进制里极不正常）；
3. **生产环境监控逆向工具使用**（`rizin`/`cutter`/`r2`/`gdb` 出现在应用服务器上是异常信号）。

**开发侧加固的现实结论**：`strip`、加壳、混淆**只是抬高成本**；本教程的例子（`stripped false`）与 r2 的例子都说明——**只要拿到二进制，静态分析就能还原大部分逻辑**。真正的秘密必须留在服务端。

---

## 10. 参考

- Rizin 官网与文档：<https://rizin.re/> ｜ 文档索引：<https://rizin.re/pages/guide/>
- Rizin 仓库：<https://github.com/rizinorg/rizin>
- Cutter（图形界面）：<https://cutter.re/> ｜ 仓库：<https://github.com/rizinorg/cutter>
- rz-ghidra（反编译插件）：<https://github.com/rizinorg/rz-ghidra>
- Kali 工具页：<https://www.kali.org/tools/rizin/>、（Cutter 见 `rizin-cutter` 包）
- 本地命令：`rizin -h`、`rz-bin -h`、`rz-asm -h`、`rz-hash -h`、`rz-diff -h`、`rz-find -h`、`rz-gg -h`、`rz-run -h`、`rz-ax -h`，交互内 `?`
- 相关教程：[`radare2.md`](radare2.md)（命令详解）、[`ghidra.md`](ghidra.md)、[`gdb.md`](gdb.md)、[`objdump.md`](objdump.md)、[`ltrace.md`](ltrace.md)

## ⚠️ 法律与伦理

Rizin/Cutter 是**完全合法的开发、安全研究、恶意样本分析工具**。但以下行为可能违法：

- **逆向非自有软件以规避技术措施/DRM**（《著作权法》相关规定与许可协议）；
- **窃取商业秘密**（《反不正当竞争法》第 9 条）；
- 对**未授权系统**利用逆向发现的漏洞（《刑法》第 285/286 条）；
- 分析**来源不明的他人设备数据**（《个人信息保护法》《数据安全法》）。

**请遵守**：

1. 只分析**自己的程序**、**CTF 靶题**、**开源软件（在其许可范围内）**、**授权的研究目标**或**恶意样本（防御分析目的）**；
2. **打补丁只改副本**（保持原始样本/证据不被改动）；
3. 发现商业软件漏洞走**厂商漏洞披露流程**；
4. 本教程示例请用第 5 节的自编程序（`crackme.c`）复现。
