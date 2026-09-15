# Linux 内核学习总纲

本目录是网络安全学习库中的「Linux 内核」模块。目标是从可运行的实验出发，建立对内核结构、构建流程、模块开发与内核安全的可操作理解，而不是停留在术语背诵。

- 源码位置：`kernel/src/linux`（由 [`scripts/fetch_linux_kernel.sh`](../scripts/fetch_linux_kernel.sh) 拉取）
- 本地实测版本：**7.3.0-rc3**（`make -s kernelversion` 输出，见下文「版本实测记录」）
- 文档语言：简体中文；代码、命令、路径、宏名、函数名保留原文

---

## 1. 内核是什么

内核是常驻内存、运行在 CPU 最高特权级（x86-64 的 ring0）上的那段程序。它同时扮演两个角色：

| 角色 | 含义 | 典型代码位置 |
| --- | --- | --- |
| 资源抽象层（虚拟机） | 把裸硬件包装成进程、地址空间、文件、socket 等抽象 | `mm/`、`fs/`、`net/` |
| 资源管理者（调度器） | 决定谁在什么时候使用 CPU、内存、设备，并强制隔离 | `kernel/sched/`、`mm/` |

### 1.1 内核空间与用户空间的区别

| 维度 | 用户空间 | 内核空间 |
| --- | --- | --- |
| CPU 特权级 | ring3 | ring0（x86-64 另有 ring1/2，Linux 不使用） |
| 地址空间 | 每个进程独立，受页表保护 | 所有进程共享同一份内核地址空间（`current` 指向当前进程） |
| 进入方式 | — | 系统调用、中断、异常、陷入（trap） |
| 出错后果 | 进程收到信号被杀 | Oops / panic，通常整机不可用 |
| 可用 API | libc、系统调用 | 内核内部函数，**没有** libc、没有浮点（除非专门保存 FPU 状态） |
| 栈 | 8 MB 左右，可增长 | 通常 16 KB（x86-64 `THREAD_SIZE`），不能随意深递归 |
| 内存分配 | `malloc`，可睡眠 | `kmalloc`/`vmalloc`，睡眠规则取决于上下文 |

用户态程序无法直接访问内核地址（由页表的 U/S 位、SMAP/SMEP 硬件特性共同保证）。要内核替你做事，只能通过明确定义的入口（系统调用、ioctl、procfs/sysfs 文件等）——**这些入口就是内核的攻击面**，详见 [04-内核安全与攻防](docs/04-内核安全与攻防.md)。

### 1.2 整体架构图

```
+------------------------------------------------------------------+
|                         用户空间 (ring3)                          |
|   应用程序   glibc   systemd   iproute2   bpftrace ...            |
|        |            |           |            |                    |
+--------|------------|-----------|------------|--------------------+
         | 系统调用 (syscall)      | ioctl/mmap | bpf() 系统调用
=========|============|===========|============|====================
         v            v           v            v
+------------------------------------------------------------------+
|                         内核空间 (ring0)                          |
|                                                                  |
|  [系统调用入口]  arch/x86/entry/  entry_64.S -> do_syscall_64()    |
|                                                                  |
|  +----------------+  +----------------+  +--------------------+  |
|  | 进程/调度       |  | 内存管理        |  | 文件系统            |  |
|  | kernel/sched/  |  | mm/            |  | fs/  VFS + ext4/   |  |
|  | kernel/fork.c  |  | mm/mmap.c      |  | xfs/btrfs/...      |  |
|  | kernel/exit.c  |  | mm/page_alloc.c|  | fs/open.c          |  |
|  +----------------+  +----------------+  +--------------------+  |
|                                                                  |
|  +----------------+  +----------------+  +--------------------+  |
|  | 网络协议栈      |  | 设备驱动        |  | 安全子系统          |  |
|  | net/           |  | drivers/       |  | security/          |  |
|  | net/ipv4/      |  | drivers/char/  |  | security/selinux/  |  |
|  | net/core/      |  | drivers/net/   |  | security/lockdown/ |  |
|  +----------------+  +----------------+  +--------------------+  |
|                                                                  |
|  [通用基础设施]                                                    |
|   include/linux/   内核内部 API 头文件                             |
|   lib/             通用库（rbtree, xarray, bitmap, string...）     |
|   kernel/locking/  自旋锁/互斥量/RCU                               |
|   kernel/trace/    ftrace / tracepoint / kprobe                   |
|   crypto/          加密算法                                        |
|                                                                  |
+------------------------------------------------------------------+
         | 平台相关层
         v
+------------------------------------------------------------------+
|  arch/x86/    启动、页表、中断向量、GDT/IDT、CPU 特性、KVM、entry    |
+------------------------------------------------------------------+
         |
         v
+------------------------------------------------------------------+
|  硬件：CPU / MMU / 内存 / PCI / 磁盘 / 网卡 / 中断控制器             |
+------------------------------------------------------------------+
```

**纵向读法**（推荐）：一次 `write()` 从用户态到磁盘要穿过 `arch/x86/entry` → `fs/read_write.c` → VFS → 具体文件系统 → `block/` → `drivers/`。这条链在 [02-源码结构与阅读方法](docs/02-源码结构与阅读方法.md#63-调用链实证一次-write-从用户态到设备) 中逐跳给出真实函数名与文件路径。

---

## 2. 本目录索引

| 文件 | 内容 | 适合阶段 |
| --- | --- | --- |
| [docs/01-内核构建与调试.md](docs/01-内核构建与调试.md) | `make defconfig` → 编译 → QEMU 启动的完整流程；printk/dynamic_debug/ftrace/KASAN/GDB 等调试手段；常见构建错误 | 任何路线第 1 步；必须先做完 |
| [docs/02-源码结构与阅读方法.md](docs/02-源码结构与阅读方法.md) | 顶层 24 个目录逐个说明；`kernel/`、`mm/`、`fs/`、`net/`、`arch/x86/` 重点文件；syscall 表与调用链实证；核心数据结构定义位置 | 有可运行内核之后 |
| [docs/03-内核模块开发.md](docs/03-内核模块开发.md) | Hello World 模块、外部模块 Makefile、模块参数、字符设备驱动、并发与锁、Oops 阅读 | 想写代码而不是只读代码 |
| [docs/04-内核安全与攻防.md](docs/04-内核安全与攻防.md) | 攻击面分类、经典漏洞类型的结构性说明、防御机制与 `CONFIG_` 选项、加固自查清单、syzkaller 合法研究路径 | 已能读内核代码，转向安全方向 |
| [docs/05-动手实验清单.md](docs/05-动手实验清单.md) | 20 个由易到难的实验，每个含目标/前置/步骤/验证标准/延伸思考 | 全程当练习册用 |
| [docs/06-学习资源与版本速查.md](docs/06-学习资源与版本速查.md) | 权威书籍与在线资源、邮件列表礼仪、版本号与 `uname -r` 解读 | 全程随时查阅 |

---

## 3. 三条学习路线

三条路线在第 1 阶段完全重合（都要先能自己编译并启动一个内核）。分歧点在阶段 2。

### 3.1 路线 A：系统管理员视角

关注「内核如何影响我的服务」，目标是能解释线上现象、能安全地调整内核参数。

| 阶段 | 内容 | 里程碑（能独立做到） |
| --- | --- | --- |
| A1 | 读 [docs/01](docs/01-内核构建与调试.md)，用发行版内核跑通 `dmesg`/`/proc`/`/sys` 常用观测点 | 用 `dmesg` 时间戳对齐一次服务故障的时间线 |
| A2 | 读 [docs/02](docs/02-源码结构与阅读方法.md) 的 `mm/`、`fs/`、`net/` 部分 | 看懂 `/proc/meminfo`、`/proc/slabinfo`、`ss -s` 输出背后对应的内核子系统 |
| A3 | 调度与内存子系统实验（实验 8/9/16） | 用 cgroup v2 复现一次内存压力，说清 `memory.current` 的来源 |
| A4 | 用 ftrace/perf 做一次线上延迟归因 | 给出「哪个内核函数占了延迟」而不是「CPU 很忙」 |

**不推荐**管理员路线去读 `arch/x86/entry/` 汇编，性价比低。

### 3.2 路线 B：内核模块 / 驱动开发者

关注「如何写正确的内核代码」，核心难点不是 API，而是并发、上下文与生命周期。

| 阶段 | 内容 | 里程碑 |
| --- | --- | --- |
| B0 | 完成 [docs/01](docs/01-内核构建与调试.md)，能编译出带 `CONFIG_DEBUG_INFO` 和 KASAN 的内核 | QEMU 里启动自编译内核并看到 KASAN 就绪日志 |
| B1 | [docs/03](docs/03-内核模块开发.md) 的 Hello World 与 `module_param` | `insmod`/`rmmod` 循环 100 次不泄漏 |
| B2 | 字符设备驱动 + `copy_to_user`/`copy_from_user` | 写出可通过 `cat`/`echo` 访问的设备节点 |
| B3 | 并发与锁：自旋锁、互斥量、RCU（[docs/03](docs/03-内核模块开发.md#6-并发与锁基础)） | 用 KCSAN 或 lockdep 发现并修复一处自己写的竞态 |
| B4 | 读真实驱动的等价实现：`drivers/char/misc.c`、`drivers/char/mem.c` | 能解释 `misc_register()` 为你做了什么 |
| B5 | 向上游提交一个 `checkpatch.pl` 通过的补丁（[docs/06](docs/06-学习资源与版本速查.md#4-邮件列表与社区)） | 收到至少一次 review 回复 |

### 3.3 路线 C：内核安全研究者

前提：已经能读内核 C 代码、能读懂 Oops、能在 QEMU+GDB 下单步。**只在自有或书面授权的环境中研究。**

| 阶段 | 内容 | 里程碑 |
| --- | --- | --- |
| C1 | 攻击面测绘：用 `grep -rn SYSCALL_DEFINE` 列出全部系统调用，按子系统分组 | 能说出一类子系统（如 `io_uring`）的入口函数与参数校验位置 |
| C2 | 漏洞类型训练（[docs/04](docs/04-内核安全与攻防.md#3-经典漏洞类型)） | 在 KASAN 内核里自造一个 UAF 并读懂报告 |
| C3 | 防御机制：读懂 KPTI/KASLR/SMEP/SMAP/CET/CFI 各自的防护边界 | 能说明「KASLR 泄露一个内核指针」为什么值钱 |
| C4 | 模糊测试：搭 syzkaller，跑通一个驱动/subsystem | 拿到一份可去重、可复现的 crash 报告 |
| C5 | 上游报告流程（[docs/06](docs/06-学习资源与版本速查.md#5-如何提问与报告问题)） | 按 `Documentation/process/` 的规范发出报告并获得回应 |

### 3.4 路线选择建议

- 只想让服务更稳 → A
- 想写驱动/内核模块 → B
- 想做漏洞挖掘/CTF 内核题 → C（但 C1 前必须补完 B1~B3）

---

## 4. 环境准备

### 4.1 编译与调试工具（Debian / Kali / Ubuntu）

```bash
sudo apt update
sudo apt install -y \
  build-essential bc bison flex rsync \
  libssl-dev libelf-dev libncurses-dev \
  dwarves pahole \
  gcc gcc-multilib \
  make git wget curl xz-utils cpio \
  qemu-system-x86 qemu-utils \
  gdb \
  busybox-static \
  linux-perf bpftrace \
  python3 python3-pip
```

说明（首次出现的英文术语给出中文解释）：

| 包 | 作用 |
| --- | --- |
| `make` / `gcc` / `binutils` | Kbuild 构建三件套；`binutils` 随 `build-essential` 安装，提供 `ld`/`objdump`/`readelf`/`nm` |
| `bison` / `flex` | 生成 Kconfig 解析器与 dtc 词法分析器；缺失会直接构建失败 |
| `libssl-dev` | 内核模块签名与 `certs/` 自签证书；缺失会报 `openssl/bio.h: No such file` |
| `libelf-dev` | `tools/objtool` 与 BTF 生成需要；缺失会报 `elfutils/libelf.h` |
| `libncurses-dev` | `make menuconfig` 的 TUI 依赖；缺失时报 `Unable to find the ncurses library` |
| `dwarves`（提供 `pahole`） | 由 DWARF 调试信息生成 BTF（BPF Type Format，BPF 类型格式）。现代内核默认 `CONFIG_DEBUG_INFO_BTF=y`，缺 `pahole` 会失败 |
| `qemu-system-x86` | 跑自编译内核的虚拟机 |
| `gdb` | 配合 QEMU 的 `-s -S` 做源码级单步 |
| `busybox-static` | 制作最小 initramfs（初始内存文件系统）的 `/bin/busybox`，静态链接免去 libc 依赖 |
| `linux-perf`（提供 `perf`） | 采样剖析；部分发行版包名为 `linux-tools-$(uname -r)` |
| `bpftrace` | eBPF 高级跟踪语言前端 |

> 若使用 Arch / Omarchy（本项目当前宿主机即为 Arch）：
> ```bash
> sudo pacman -S --needed base-devel bc bison flex libelf openssl ncurses pahole \
>   qemu-full gdb busybox perf bpftrace
> ```

### 4.2 按需追加（只在对应路线安装）

| 场景 | 工具 | 安装 |
| --- | --- | --- |
| 内核安全研究 | syzkaller | 见 [docs/04](docs/04-内核安全与攻防.md#6-合法研究路径) |
| 崩溃转储分析 | `crash`、`makedumpfile` | `sudo apt install crash kdump-tools` |
| 静态检查 | `sparse`、`smatch`、`coccinelle` | `sudo apt install sparse coccinelle` |
| Rust 内核模块 | `rustc`、`bindgen` | 需匹配 `rust/` 要求的版本 |

### 4.3 硬件与磁盘要求

编译一个全量内核（`defconfig` + `CONFIG_DEBUG_INFO`）峰值占用：

- 磁盘：源码工作树约 **1.8 GB**，`.git` 约 **296 MB**，构建产物（`O=` 外部构建目录）建议预留 **10~20 GB**
- 内存：`make -j$(nproc)` 每并发任务约 1~1.5 GB；16 GB 内存建议 `make -j8`

查看当前实际占用：

```bash
du -sh kernel/src/linux kernel/src/linux/.git
```

### 4.4 工具自检

```bash
for t in gcc clang make flex bison qemu-system-x86_64 gdb pahole bpftrace perf cpio; do
  printf '%-22s' "$t"
  command -v "$t" >/dev/null 2>&1 && echo "OK  $($t --version 2>/dev/null | head -1)" || echo "缺失"
done
```

---

## 5. 获取内核源码

### 5.1 使用本仓库脚本

```bash
# 默认：浅克隆主线 master（推荐，够用）
bash scripts/fetch_linux_kernel.sh

# 完整历史（需要 git log / git blame 追溯某行代码的来历时）
bash scripts/fetch_linux_kernel.sh --full

# 拉取 stable 分支 linux-6.12.y（生产环境对齐用）
bash scripts/fetch_linux_kernel.sh --stable
```

国内网络先设镜像再执行：

```bash
export KERNEL_MIRROR=https://gitclone.com/github.com/torvalds/linux.git
bash scripts/fetch_linux_kernel.sh
```

### 5.2 浅克隆 vs 完整克隆

| 维度 | `--depth 1`（浅克隆） | `--full`（完整克隆） |
| --- | --- | --- |
| 命令 | `git clone --depth 1 --branch master <url>` | `git clone --branch master <url>` |
| `.git` 体积 | 约 **300 MB** | 5 GB 以上 |
| 工作树体积 | 约 **1.8 GB**（文件内容与完整克隆一致） | 约 1.8 GB |
| 可否 `git log` / `git blame` | ❌（只有 1 个 commit） | ✅ |
| 可否 `git bisect` 定位回归 | ❌ | ✅ |
| 学习源码结构 / 编译内核 | ✅ 完全够用 | ✅ |

**结论**：读结构、写模块、编译内核只需浅克隆。只有当你需要回答「这行代码是哪次提交引入的、为什么改」时才升级为完整克隆。升级方式：

```bash
cd kernel/src/linux
git fetch --unshallow           # 从浅变完整，增量下载
```

### 5.3 版本实测记录

本仓库拉取时段的实测数据（可复现）：

```bash
cd kernel/src/linux
make -s kernelversion           # 依赖 Makefile 的 VERSION/PATCHLEVEL/SUBLEVEL/EXTRAVERSION
head -6 Makefile
git log -1 --format='%H %cd'
```

实测结果：

| 项 | 值 |
| --- | --- |
| `make -s kernelversion` | `7.3.0-rc3` |
| `Makefile` 顶部 | `VERSION = 7`、`PATCHLEVEL = 3`、`SUBLEVEL = 0`、`EXTRAVERSION = -rc3`、`NAME = Baby Opossum Posse` |
| 克隆方式 | `git clone --depth 1 --branch master https://github.com/torvalds/linux.git` |
| 最新提交 | `587858367581b9c55c3690f4e63382ad622719d4`（2026-09-14 10:41:30 -0700） |
| 顶层目录数 | 24 个目录 + 15 个顶层文件（`Makefile`、`Kconfig`、`Kbuild`、`COPYING`、`CREDITS`、`LICENSES`、`MAINTAINERS`、`README` 等） |
| 源码规模（不含 `tools/`） | 约 33 584 个 `*.c` 文件、1 927 个 `Kconfig*` 文件 |
| 磁盘占用 | 工作树 + `.git` 合计约 **2.1 GB** |

> 版本号语义、主线/LTS 对应关系见 [docs/06-学习资源与版本速查.md](docs/06-学习资源与版本速查.md#6-版本速查)。
> ⚠️ 源码的版本会随你重新克隆而变化；上表只代表本仓库当前快照。**写文档、做实验前请先自己跑一遍 `make -s kernelversion` 确认。**

---

## 6. 安全与法律边界

- 加载内核模块 = 获得 ring0 权限，**只在虚拟机或你完全拥有的测试机上练习**。
- 编译安装内核会改写 `/boot` 与 bootloader 配置，操作前备份并确认回滚方式（见 [docs/01](docs/01-内核构建与调试.md#7-把自编译内核装到本机-危险)）。
- 内核漏洞研究仅限自有环境或有书面授权（如漏洞赏金项目范围）的目标。未经授权对他人系统进行漏洞利用属于违法行为。

---

## 7. 下一步

```bash
cd kernel/src/linux
make defconfig
make -j$(nproc)
```

然后打开 [docs/01-内核构建与调试.md](docs/01-内核构建与调试.md)。
