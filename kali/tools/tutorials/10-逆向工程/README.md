# 10 · 逆向工程（Reverse Engineering）

> 本目录是 Kali 工具精讲教程的第 10 篇：**从「一个二进制/固件」到「我明白它在干什么」**。
> 主干闭环：**静态反汇编（objdump）→ 反编译读逻辑（Ghidra / r2 / rizin）→ 动态验证（GDB / ltrace）→ 需要时补丁与批处理**。
> 上游：[`../09-数字取证/`](../09-数字取证/)（提取二进制）｜ 下游：[`../11-社会工程与报告/`](../11-社会工程与报告/)（报告与记录）
> 相关索引：[`../../index.md`](../../index.md) ｜ 分类速查：[`../../catalog/reverse-engineering.md`](../../catalog/reverse-engineering.md)、[`../../by-attack/forensics.md`](../../by-attack/forensics.md)

---

## 工具清单

| 工具 | 一句话 | 难度 | 教程 |
|------|--------|------|------|
| **ghidra** | 反编译器：把汇编还原成类 C 代码，配类型系统、交叉引用、脚本与版本比对 | ⭐⭐⭐ | [`ghidra.md`](ghidra.md) |
| **radare2** | 命令行逆向框架：`r2` + `rabin2`/`radiff2`/`rasm2`/`rahash2`… 全流程可脚本化 | ⭐⭐⭐⭐ | [`radare2.md`](radare2.md) |
| **rizin** | radare2 的社区分叉（`rz-*` 系列），配套 **Cutter** 图形界面 | ⭐⭐⭐ | [`rizin.md`](rizin.md) |
| **gdb** | 动态调试器：断点、寄存器、栈、改状态；`gdb-multiarch` 调 ARM/MIPS | ⭐⭐⭐ | [`gdb.md`](gdb.md) |
| **objdump** | 反汇编 + 目标文件分析（binutils 提供，**非 Kali 专有工具**） | ⭐⭐ | [`objdump.md`](objdump.md) |
| **ltrace** | 库函数调用跟踪：直接看「调了谁、传了什么参数」（ltrace 包，**非 Kali 专有工具**） | ⭐⭐ | [`ltrace.md`](ltrace.md) |

> **关于包来源（重要）**：
> - `ghidra`、`radare2`、`rizin`（含 `rizin-cutter` 提供 `cutter`）、`gdb`（含 `gdb-multiarch`/`gdbserver`）**都在 Kali 官方工具清单中**；
> - **`objdump` 不在清单中** —— 它来自 Debian 的 **`binutils`** 包（`sudo apt install binutils`）；
> - **`ltrace` 不在清单中** —— 它来自 Debian 的 **`ltrace`** 包（`sudo apt install ltrace`）。
> 这两个工具**不是 Kali 特有**，任何 Linux 发行版都一样，本文据此如实说明。

---

## 学习顺序

```
① 静态基础（先会「读机器码」）
   objdump.md      → -f/-h/-d/-s/-t/-T、Intel 语法、地址↔文件偏移换算
        │
② 动态基础（会「看运行时」）
   ltrace.md       → 库调用序列（字符串参数、文件名、导入哪些函数）
   gdb.md          → 断点/单步/寄存器/栈/改状态；ptrace 原理与反调试
        │
③ 交互分析（会「用框架」）
   radare2.md      → aa/afl/pdf/axt/VV/~ 过滤/wx 补丁/脚本化
   rizin.md        → rz-* 系列 + Cutter 图形界面
        │
④ 反编译（会「读伪代码」）
   ghidra.md       → 导入→分析→Decompile→重命名/类型→交叉引用→Headless 批处理
        │
⑤ 组合与自动化
   Ghidra Headless / r2 -c 批处理 / GDB 自动化脚本
```

**建议节奏**：用**自编的 crackme**（本目录各篇第 5 节都有完整源码）走通三遍：

```
objdump -d 看结构 → ghidra 反编译找口令逻辑 → gdb 断点验证
   → r2 打补丁验证「客户端校验可绕」→ ghidra headless 批量导出函数清单
```

---

## 环境准备

```bash
sudo apt update
sudo apt install -y ghidra radare2 rizin rizin-cutter gdb gdb-multiarch binutils ltrace

# 可选但强烈建议
sudo apt install -y strace file readelf    # readelf 随 binutils
sudo apt install -y python3-pip            # Ghidra 脚本/qemu 等
sudo apt install -y qemu-user              # 无硬件时模拟 ARM/MIPS 二进制
sudo apt install -y binutils-arm-linux-gnueabi binutils-mips-linux-gnu   # 交叉反汇编

# GDB 增强插件（三选一，不要同时装）
#   pwndbg: https://github.com/pwndbg/pwndbg
#   GEF   : https://github.com/hugsy/gef
#   PEDA  : https://github.com/longld/peda
```

验证：

```bash
for t in ghidra r2 radare2 rizin rz-bin cutter gdb gdb-multiarch gdbserver objdump ltrace strace; do
  printf '%-14s %s\n' "$t" "$(command -v $t || echo MISSING)"
done
java -version 2>&1 | head -2         # Ghidra 需要 JDK
r2 -v | head -2
ghidra 2>/dev/null &                 # 首次启动同意协议后即可关闭
```

### 练习素材（合法来源，**必须自己拥有或获授权**）

| 素材 | 获取方式 | 适合练什么 |
|------|----------|------------|
| **自编 crackme**（各篇第 5 节） | 直接 `gcc` 编译 | 全流程（**推荐起点**） |
| **CTF 靶题** | 各 CTF 平台（picoCTF、CTFtime 等公开题目） | 真实感强、**明确允许逆向** |
| **开源软件** | 自行编译（`gcc -g -O0` 或 `-O2 -s` 对比） | 有源码对照，学习效率最高 |
| **公开恶意样本库** | VirusTotal / MalwareBazaar / theZoo（**仅在隔离环境**） | 防御分析能力 |
| **crackmes.one** | <https://crackmes.one/>（专门用于练习逆向的合法题目站） | 分级练习 |
| **固件二进制** | OpenWrt/DD-WRT 官方固件（开源） | ARM/MIPS 逆向（配合 [`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md)） |

---

## 环境准备清单（自检）

```bash
# 1) 造一个练习目标（同时有带符号与 strip 两个版本）
mkdir -p /tmp/revlab && cd /tmp/revlab
printf '#include <stdio.h>\n#include <string.h>\nint main(int c,char**v){if(c<2)return 1;puts(strcmp(v[1],"pass")?"no":"yes");return 0;}\n' > t.c
gcc -g -O0 -o t_dbg t.c
gcc -O2 -s -o t_strip t.c
file t_dbg t_strip

# 2) objdump 能用
objdump -d -M intel --disassemble=main t_dbg | head

# 3) gdb 能下断点
gdb -q -batch -ex 'b main' -ex 'run pass' -ex 'bt' ./t_dbg | head

# 4) ltrace 能看到 strcmp
ltrace -e strcmp ./t_strip pass 2>&1 | head -3

# 5) r2 / rizin 能分析
r2 -A -q -c 'afl~main; q' ./t_dbg
rizin -A -q -c 'afl~main; q' ./t_dbg

# 6) radiff2 / rz-diff 能比对
radiff2 -C ./t_dbg ./t_strip | head -5
rz-diff -t functions ./t_dbg ./t_strip | head -5

# 7) Ghidra Headless 能跑
/usr/share/ghidra/support/analyzeHeadless /tmp/revlab/proj T -import /tmp/revlab/t_dbg -deleteProject 2>&1 | tail -3
```

---

## 工具选择速查

| 你的任务 | 首选 | 备用 |
|----------|------|------|
| 读懂复杂逻辑（最快） | **ghidra**（反编译） | rizin + Cutter |
| 快速看结构（命令行） | **objdump** / `rz-bin -I/-S/-s` | r2 `iI;iS;is` |
| 找「谁调用了这个函数」 | **ghidra 按 `X`** | r2 `axt` |
| 看控制流分支 | **ghidra Function Graph** | r2 `VV` |
| 精确动态调试 | **gdb**（+ pwndbg/gef） | r2 `-d` |
| 看「调用了哪些库函数」 | **ltrace** | gdb 断点 |
| 看「系统调用/文件/网络」 | **strace** | —— |
| 批量处理样本 | **ghidra Headless** / `r2 -c` | `rz-bin` + Shell |
| 打补丁改字节 | **r2 `-w`+`wa`**（可缓存预览） | ghidra Patch Instruction |
| 版本/样本比对 | **ghidra Version Tracking** | `rz-diff -t functions`、`radiff2 -C` |
| ARM/MIPS 固件二进制 | **ghidra**（选对 processor） | `arm-linux-gnueabi-objdump`、`rz-bin -Y` |
| 汇编↔字节互转 | **`rasm2` / `rz-asm`** | `objdump -b binary -m ...` |

---

## 核心概念速查

| 概念 | 一句话 | 详见 |
|------|--------|------|
| **ptrace** | Linux 用户态调试的内核接口（GDB/ltrace 都靠它）；断点 = 写 `0xCC` | [`gdb.md`](gdb.md) 第 2 节 |
| **AT&T vs Intel 语法** | 默认 AT&T；`-M intel` / `e asm.syntax=intel` 切 Intel | [`objdump.md`](objdump.md)、[`radare2.md`](radare2.md) |
| **PIE / ASLR** | 地址随机化：静态工具显示的是偏移 | 各篇「常见坑」 |
| **PLT/GOT** | 动态调用的跳转表与地址表；`@plt` 就是外部库函数 | [`objdump.md`](objdump.md) |
| **stripped** | 符号被删除（`strip`）→ 函数变成 `FUN_00401xxx` | [`ghidra.md`](ghidra.md) 场景 2 |
| **P-code / RzIL / ESIL** | 中间表示（IR）：让反编译与模拟分析跨架构 | [`ghidra.md`](ghidra.md)、[`radare2.md`](radare2.md) |
| **反编译不是原码** | 变量名/类型是推断结果，需要人工重命名与标注 | [`ghidra.md`](ghidra.md) 场景 2 |
| **交叉引用（xref）** | 「谁用了它 / 它用了谁」——理解结构的主线 | `axt` / `X` 键 |
| **调用约定** | System V AMD64：参数在 `rdi/rsi/rdx/rcx/r8/r9`，返回值 `rax` | [`gdb.md`](gdb.md) 第 6 节 |
| **反调试** | `ptrace` 自检、时序检测、代码校验和 | [`gdb.md`](gdb.md) |
| **加壳/混淆** | 高熵、`pdc`/反编译混乱；先脱壳再分析 | [`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md) 熵分析 |

---

## 与其它章节的衔接

| 你手上的东西 | 去哪里 |
|--------------|--------|
| 从镜像/固件里提取出的二进制 | [`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md) → 本目录 |
| 需要先确认文件类型与保护 | [`objdump.md`](objdump.md)、`file`、`readelf` |
| 想快速知道「有什么功能」 | [`ltrace.md`](ltrace.md)（库调用）+ [`ghidra.md`](ghidra.md)（字符串/导入） |
| 要精确验证某个假设 | [`gdb.md`](gdb.md) |
| 要批量处理一堆样本 | [`ghidra.md`](ghidra.md) 的 Headless 模式 |
| 结果要写进报告 | [`../11-社会工程与报告/README.md`](../11-社会工程与报告/README.md) |
| 攻防视角（漏洞利用） | [`../06-漏洞利用/README.md`](../06-漏洞利用/README.md)、[`../08-后渗透/README.md`](../08-后渗透/README.md) |

---

## ⚠️ 法律与伦理

逆向工程本身是**合法的技术活动**（互操作性研究、安全分析、恶意样本分析、教学、CTF、开源开发），但**目的与对象**决定了合法性。可能违法的情形：

- **规避技术措施/DRM**（非自有软件逆向以破解许可）——《著作权法》相关规定与许可协议；
- **窃取商业秘密**（分析竞争对手软件的核心算法）——《反不正当竞争法》第 9 条；
- **利用逆向发现的漏洞攻击未授权系统**——《刑法》第 285 条（非法侵入计算机信息系统、非法获取计算机信息系统数据、非法控制）、第 286 条（破坏计算机信息系统）；
- **分析来源不明的他人设备数据**——《个人信息保护法》《数据安全法》《刑法》第 253 条之一。

**使用前提**：

1. **只分析你拥有的、明确授权的、CTF 靶题、或开源软件（在其许可范围内）**；
2. **补丁/导出只改副本**，保持原始样本与证据不变（这点在取证与样本分析里尤其重要）；
3. **发现的漏洞走厂商披露流程**，不公开可直接利用的细节；
4. **恶意样本分析在隔离环境**（断网虚拟机 + 快照），并按组织流程共享 IOC；
5. **记录操作过程**（用了什么工具、什么命令、得到什么结论），便于复核与被质疑时自证；
6. 本目录全部示例请用**自己编写的练习程序**（各篇第 5 节提供源码）在自己的机器上复现。
