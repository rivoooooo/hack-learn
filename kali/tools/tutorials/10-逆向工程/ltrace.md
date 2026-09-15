# ltrace（库函数调用跟踪）

> **一句话**：让程序跑起来，**把每次调用动态库函数的「函数名 + 参数 + 返回值」打印出来**——不用源码、不用下断点，直接看「它到底调了谁、传了什么」。
> **分类**：逆向工程 / 动态分析 ｜ **Kali 包**：**不在 Kali 官方工具清单中** —— `ltrace` 来自 Debian 的 **`ltrace`** 包。**它不是 Kali 专有工具。**
> **官方文档**：<https://www.ltrace.org/> ｜ `man ltrace`

---

## 1. 它解决什么问题

有一类问题**静态工具很难回答**：

- 这个程序里埋了很多字符串比较（`strcmp`），**哪一个才是真正的口令校验？**
- 它是怎么解析配置文件的？（调了 `fopen`/`fgets`/`strtok`？）
- 它的输入经过了哪些处理？（`strlen`/`memcpy`/`atoi`/加密函数？）
- 它连了哪个域名/端口？（`getaddrinfo`/`connect`？）
- 崩溃前最后调用的库函数是什么？

`ltrace` 的答案最直接：**把这些调用按时间顺序全打出来**。

```console
$ ltrace ./login
__libc_start_main(0x401176, 2, 0x7ffd..., 0x401250 <unfinished ...>
strcmp("admin", "admin")                       = 0
strcmp("hunter2", "s3cr3t")                    = -8      ← 这就是口令比较！
printf("Access denied\n")                      = 14
+++ exited (status 1) +++
```

**一眼就看到了「它拿我输入的东西和什么比较」**。这比在 IDA/Ghidra 里翻几百行反汇编快得多。

对比同类：

| 工具 | 跟踪对象 | 需要的权限/条件 |
|------|----------|-----------------|
| **`ltrace`** | **动态库函数调用**（`libc`、`libcrypto`…） | 程序需**动态链接**；调试权限（同 GDB） |
| **`strace`** | **系统调用**（`open`/`read`/`write`/`connect`/`execve`…） | 同上 |
| **`gdb`** | 任意（寄存器/内存/断点） | 最强也最重；见 [`gdb.md`](gdb.md) |
| **`objdump`** | 静态反汇编 | 无需运行；见 [`objdump.md`](objdump.md) |
| **Frida / `LD_PRELOAD` hook** | 任意函数（含内部函数） | 更灵活（可改参数/返回值），但配置更复杂 |

**ltrace 与 strace 的关系**（**最容易搞混的一点**）：

- **`ltrace` 看「用户态库函数」**：`strcmp`、`printf`、`malloc`、`AES_encrypt`、`fopen`…
- **`strace` 看「内核系统调用」**：`openat`、`read`、`write`、`socket`、`connect`、`ioctl`…
- **`printf` 是库函数，但它内部会调用 `write` 系统调用** → 你会看到 `ltrace` 里有 `printf`，`strace` 里有 `write`。**两者互补，通常两个都跑。**

**局限（必须知道）**：

1. **只能跟踪动态链接的函数**——**静态链接的程序（含大部分 Go 程序）ltrace 完全无效**（因为没有 PLT 调用）；
2. **看不到内部函数**（`check_password()` 是程序自己的函数，不是库函数）→ 需要 GDB/静态分析；
3. **有性能开销**（每个库调用都要中断处理）；
4. **有反调试/环境检测的程序可能拒绝运行**；
5. **优化过的代码可能内联掉库调用**（如 `strcmp` 被内联为几条指令）→ 就看不到了。

---

## 2. 工作原理

```
ltrace ./target
   │
   ├─ 创建子进程，用 ptrace(PTRACE_TRACEME) + execve 启动目标
   │     （与 gdb 相同的底层：ptrace）
   │
   ├─ 在目标的「动态链接器切换到目标程序之前」接管控制
   │
   ├─ 对每个被 PLT 跳转的库函数入口**下断点**
   │     ├─ 命中时：读寄存器取参数 → 打印「函数名(参数...)」
   │     │        （参数按 ABI：rdi/rsi/rdx/rcx/r8/r9；字符串会自动解引用）
   │     └─ 返回时：读 rax → 打印「 = 返回值」
   │
   └─ 依此类推，形成时间序列
       （所以输出形如：func(args) = retval）
```

**关键机制**：

- **PLT 桩（Procedure Linkage Table）**：动态链接的函数调用都会先跳到 `.plt` 里的桩，再由桩跳转到真实地址。ltrace 就是**在这些桩上挂钩**（所以它只能看到外部库函数）。
- **参数解码**：ltrace 需要知道每个函数的**原型（参数个数与类型）**才能正确解码。它从 `/etc/ltrace.conf`（或 `/usr/share/ltrace/*.conf`）读取「函数原型描述」。
  - **没配置的函数**：参数会显示为「原始的 4 个十六进制值」（`func(0x... , 0x..., 0x..., 0x...)`），**看起来像垃圾** → 这就是你需要手工加配置的原因。
  - 这也是为什么有时 `printf` 显示得漂亮、而某个自定义库函数显示得不漂亮。
- **`-f` 跟随子进程**：默认只跟主进程；程序 `fork` 出的子进程需要 `-f`。
- **`-e <filter>` 过滤表达式**：可以只跟踪某些函数（`-e strcmp+printf`），**这是让输出可读的关键**。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install ltrace
command -v ltrace
ltrace --version
```

```console
ltrace 0.7.3
```

```bash
ltrace --help 2>&1 | head -40
```

最简用法：

```bash
ltrace ./target
```

```console
__libc_start_main(0x401176, 1, 0x7ffcf8e1a9b8, 0x401250 <unfinished ...>
puts("usage: ./target <password>"...)                 = 35
+++ exited (status 1) +++
```

> **`<unfinished ...>` 的含义**：这是「函数开始执行」的那一行（还没返回）；等它返回时会补上 `= 返回值`。**看到 `<unfinished ...>` 说明这个调用还没结束**，在多线程/长函数里很常见。

**先确认目标「能被跟踪」**：

```bash
file ./target | tr ',' '\n' | grep -i 'statically\|dynamically'
```

```console
 dynamically linked
```

> 若显示 `statically linked` → **ltrace 无效**（静态链接没有 PLT），请改用 [`strace`]（系统调用仍可跟踪）或 [`gdb.md`](gdb.md)。

---

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-e <filter>` | **只跟踪匹配的函数**（过滤表达式） | **最重要的参数**：`-e strcmp+strncmp+memcmp` 让输出聚焦 |
| `-x <filter>` | 反向过滤：**排除**匹配的函数 | 去掉噪音（如排除 `malloc+free`） |
| `-l, --library <lib>` | 只跟踪指定库 | `-l libcrypto.so`（只看加密函数） |
| `-f` | **跟随 fork/vfork 出的子进程** | 程序自己起子进程时**必加** |
| `-p <pid>` | attach 到**已运行的进程** | 调试守护进程/服务 |
| `-o <file>` | 输出写文件 | **输出很长时必用**（再 grep） |
| `-s <n>` | **打印字符串的最大长度**（默认 32） | **调大（如 `-s 256`）才能看到完整的参数值** |
| `-n <n>` | 缩进层级（美化为树形） | `-n 2` 看调用层级 |
| `-a <n>` | 对齐输出的列宽 | 排版 |
| `-i` | **打印每条调用在程序中的指令地址** | 反向定位「哪条指令发起了这次调用」（**与 objdump 联动**） |
| `-r` | 打印**相对时间**（自程序启动起的秒数） | 分析时序（如「卡在哪一步」） |
| `-t` / `-tt` / `-ttt` | 时间戳：`HH:MM:SS` / 含微秒 / 含**微秒+日期** | 与日志对齐 |
| `-T` | 打印**每次调用的耗时** | **找性能瓶颈**（哪个调用慢） |
| `-c` | **统计模式**：汇总每个函数被调用的次数与耗时 | 快速看「哪些函数被狂调」 |
| `-D, --debug` | 显示 ltrace 自身的调试信息 | ltrace 本身出问题（如 `Couldn't find .dynsym`）时用 |
| `-d`（部分版本） | 同上/详细信息 | 以 `--help` 为准 |
| `-u <user>` | 以指定用户运行被跟踪程序 | 降权运行 |
| `-g`（部分版本） | 不显示未在配置中定义的参数 | 输出更干净 |
| `-F <file>` | 使用自定义的**原型配置文件** | **关键**：让自定义库函数参数可读 |
| `-A <n>` | 每行最多显示的数组元素个数 | 数组参数 |
| `-b`（部分版本） | 主循环中不打印内部错误 | 噪音过滤 |
| `-w <n>` | 设置输出宽度 | 排版 |
| `-h, --help` / `-V, --version` | 帮助 / 版本 | —— |

**`-e` 过滤表达式的写法**（**这是用好 ltrace 的核心技能**）：

| 写法 | 含义 |
|------|------|
| `-e strcmp` | 只跟踪 `strcmp` |
| `-e strcmp+strncmp+memcmp` | 跟踪多个（用 `+` 连接） |
| `-e '@libc.so'` | 跟踪 libc 里的所有函数 |
| `-e 'open*'` | 支持通配符（以 `open` 开头的函数） |
| `-e 'strcmp[1]'` | 跟踪并只显示第 1 个参数（**聚焦特定参数**） |
| `-x malloc+free` | 排除这些函数 |

---

## 5. 实战演练

> **环境声明**：以下使用**自己编写的练习程序**。**禁止**跟踪不属于你、且未获授权的程序进程（尤其生产服务）——那属于非法获取计算机信息系统数据（见文末法律提示）。

### 场景 1：找出口令校验点（最简单也最有用的用法）

```bash
mkdir -p /tmp/lab && cd /tmp/lab
cat > login.c <<'EOF'
#include <stdio.h>
#include <string.h>
int main(int argc, char **argv) {
    if (argc < 2) { puts("usage: ./login <password>"); return 1; }
    if (strcmp(argv[1], "s3cr3t") == 0)   /* 真正的校验 */
        puts("Access granted");
    else
        puts("Access denied");
    return 0;
}
EOF
gcc -O0 -o login login.c
```

```bash
# 全部跟踪（输出会比较杂，但先看看规模）
ltrace ./login wrong
```

```console
__libc_start_main(0x401176, 2, 0x7ffd5d0c0a88, 0x401250 <unfinished ...>
strlen("wrong")                        = 5
strcmp("wrong", "usage: ./login <password>") = 23
...
strcmp("wrong", "s3cr3t")              = -7        ← 目标出现！
puts("Access denied" <unfinished ...>
+++ exited (status 0) +++
```

```bash
# 聚焦：只看字符串比较
ltrace -e strcmp+strncmp+strcasecmp ./login wrong
```

```console
strcmp("wrong", "s3cr3t")              = -7
+++ exited (status 0) +++
```

**解读（这就是 ltrace 最核心的价值）**：

| 输出 | 含义 |
|------|------|
| `strcmp("wrong", "s3cr3t")` | 程序把**我的输入**和 **`"s3cr3t"`** 比较 |
| `= -7` | 返回负值 = 不相等（`strcmp` 返回字典序差值） |
| `= 0` | **相等 → 校验通过** |

```bash
# 验证：用正确的字符串
ltrace -e strcmp+strncmp+strcasecmp ./login s3cr3t
```

```console
strcmp("s3cr3t", "s3cr3t")             = 0
puts("Access granted"Access granted
)                                      = 15
+++ exited (status 0) +++
```

**结论**：**用一条 `ltrace -e strcmp` 就找出了硬编码口令**。这就是为什么「客户端硬编码校验」毫无安全性可言。

> **现实提醒**：这类练习在 CTF/靶场里非常常见。**但不要对你不拥有的程序这么干**（见文末）。

### 场景 2：看清「输入被怎么处理」（字符串加长 + 时间 + 调用地址）

```bash
cat > parse.c <<'EOF'
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(int argc, char **argv) {
    char buf[128];
    if (argc < 2) return 1;
    strncpy(buf, argv[1], sizeof(buf)-1);
    buf[sizeof(buf)-1] = '\0';
    char *user = strtok(buf, ":");
    char *pass = strtok(NULL, ":");
    printf("user=%s pass=%s len=%zu\n", user ? user : "(null)",
           pass ? pass : "(null)", strlen(argv[1]));
    if (pass && atoi(pass) == 1337) puts("PIN ok");
    return 0;
}
EOF
gcc -O0 -o parse parse.c
```

```bash
# -s 256 让参数完整显示；-i 打印调用地址；-r 打印相对时间
ltrace -e 'strtok+strncpy+strlen+atoi+printf' -s 256 -i -r ./parse "alice:1337"
```

```console
[0.000421] strncpy(0x7ffd1b2a3b60, "alice:1337", 127)       = 0x7ffd1b2a3b60
   [0x4011e3] strtok(0x7ffd1b2a3b60, ":")                    = 0x7ffd1b2a3b60
   [0x401203] strtok(NULL, ":")                              = 0x7ffd1b2a3b67
   [0x401230] strlen("alice:1337")                           = 10
   [0x401245] printf("user=%s pass=%s len=%zu\n", "alice", "1337", 10) = 27
user=alice pass=1337 len=10
   [0x40126f] atoi("1337")                                   = 1337
PIN ok
+++ exited (status 0) +++
```

**解读（三个技巧叠加）**：

| 技巧 | 收获 |
|------|------|
| `-e <函数列表>` | 输出只剩关心的调用，**可读性从「不可读」变成「一眼看懂」** |
| `-s 256` | 默认 32 字节会截断长参数（如 `alice:1337` 后面的内容被吃掉）→ **调大** |
| `-i` | 每条调用前的 `[0x4011e3]` 是**发起调用的指令地址** |

**`-i` 的威力**：有了 `0x401203`，你可以立刻回到静态视图：

```bash
objdump -d -M intel --start-address=0x4011f0 --stop-address=0x401215 ./parse
```

```console
  4011fb:	48 8d 05 12 0e 00 00 	lea    rax,[rip+0xe12]        # 402014
  401202:	48 89 c7             	mov    rdi,rax
  401205:	e8 46 fe ff ff       	call   401050 <strtok@plt>
```

**解读**：**`ltrace -i` 给出的地址 → `objdump` 反汇编 → 精确看到「哪个常量、哪条指令」**。这就是**动态与静态联动的标准手法**。

```bash
# 看调用耗时（-T）与统计（-c）
ltrace -c -T ./parse "alice:1337" 2>&1 | tail -15
```

```console
% time     seconds  usecs/call     calls      function
------ ----------- ----------- --------- --------- --------------------
 33.33    0.000121         121         1 printf
 22.22    0.000081          81         1 atoi
...
------ ----------- ----------- --------- --------- --------------------
100.00    0.000363                     5 total
```

**解读**：`-c` 汇总「调用次数与耗时」。**在分析「程序卡在哪」时非常有用**（比如某个 `read` 耗时 3 秒 → 它在等网络/用户输入）。

### 场景 3：库调用追踪 vs 系统调用追踪（ltrace + strace 对照）

```bash
cat > netprobe.c <<'EOF'
#include <stdio.h>
#include <stdlib.h>
int main(void) {
    FILE *f = fopen("/etc/hostname", "r");
    if (!f) { perror("fopen"); return 1; }
    char line[256];
    if (fgets(line, sizeof line, f)) printf("hostname: %s", line);
    fclose(f);
    /* 触发一次网络解析（练习用；无网络时会失败） */
    system("getent hosts localhost > /dev/null 2>&1");
    return 0;
}
EOF
gcc -O0 -o netprobe netprobe.c
```

```bash
# ① 库函数视角（ltrace）：看到 fopen/fgets/fclose/system
ltrace -e 'fopen+fgets+fclose+system+perror' ./netprobe
```

```console
fopen("/etc/hostname", "r")            = 0x55c2a3f0e2a0
fgets("kali\n", 256, 0x55c2a3f0e2a0)   = 0x7ffd...
printf("hostname: %s", "kali\n"hostname: kali
)                                     = 14
fclose(0x55c2a3f0e2a0)                 = 0
system("getent hosts localhost > /dev/null 2>&1" <unfinished ...>
--- SIGCHLD (Child exited) ---
<... system resumed>)                  = 0
+++ exited (status 0) +++
```

```bash
# ② 系统调用视角（strace）：看到 openat/read/close/clone/execve
strace -e trace=openat,read,close,execve,clone ./netprobe 2>&1 | head -20
```

```console
openat(AT_FDCWD, "/etc/hostname", O_RDONLY) = 3
read(3, "kali\n", 4096)                = 5
close(3)                               = 0
clone(child_stack=NULL, flags=CLONE_CHILD_CLEARTID|...) = 12345
execve("/bin/sh", ["sh", "-c", "getent hosts localhost > /dev/null 2>&1"], ...) = 0
```

**解读（对照表）**：

| 行为 | ltrace 看到 | strace 看到 |
|------|-------------|-------------|
| 打开文件 | `fopen("/etc/hostname", "r")` | `openat(AT_FDCWD, "/etc/hostname", O_RDONLY)` |
| 读文件 | `fgets("kali\n", 256, ...)` | `read(3, "kali\n", 4096)` |
| 关闭 | `fclose(...)` | `close(3)` |
| 执行命令 | `system("getent ...")` | `clone(...)` + `execve("/bin/sh", ...)` |

**关键结论**：

- **ltrace 更「语义化」**（能直接看到文件名、模式字符串）；
- **strace 更「底层」**（能看到文件描述符、真实的内核行为，包括 `system()` 内部起的子进程）；
- **`system()` 这种调用在 ltrace 里只是一行，但在 strace 里会暴露它起了 `/bin/sh`** —— 这也是安全审计里 strace 更重要的原因。

> **`ltrace` 对静态链接/Go 程序无效**：这类程序没有 PLT 调用。Go 程序请改用 `strace`（Go 仍走系统调用），或用 `gdb` 在特定函数下断点。

### 场景 4：跟踪运行中的进程 / 加固库（attach + 指定库）

**4a. attach 到运行中的服务（**仅限你拥有的系统**）**

```bash
# 假设你自己起了一个测试服务
./myserver &
```

```console
[1] 12345
```

```bash
# 需要权限（同 gdb：ptrace_scope 限制）
sudo ltrace -p 12345 -e 'recv+send+strcmp' -T
```

```console
[pid 12345] recv(4, "GET / HTTP/1.1\r\n", 8192, 0)  = 16
[pid 12345] strcmp("GET", "POST")                   = 1
[pid 12345] send(4, "HTTP/1.1 200 OK\r\n...", 123, 0) = 123
```

**解读**：`[pid ...]` 前缀说明在多进程/多线程下（配合 `-f` 时常见）。**attach 场景必须加 `-f`** 才能看到它 fork 出的处理进程。

**4b. 只看某个库（`-l`），例如加密库**

```bash
# 假设程序用了 libcrypto（OpenSSL）
ltrace -l libcrypto.so.3 -e 'EVP_*+AES_*+SHA256*' ./crypto_app 2>&1 | head -20
```

```console
EVP_DigestInit_ex(0x55a..., 0x7f..., 0) = 1
EVP_DigestUpdate(0x55a..., "password", 8) = 1
EVP_DigestFinal_ex(0x55a..., 0x7ffd..., 0x7ffd...) = 1
```

**解读**：**追踪加密库调用可以直接看出「它在对什么数据做哈希/加密」**（这里是 `"password"`）。这是**分析「本地加密逻辑」的有效手段**——但注意：**如果目标是保护用户数据，这就是它被分析的现实**（见第 9 节蓝队视角）。

**4c. 让自定义库函数参数可读（`-F` 原型配置）**

如果输出里出现「看不懂的十六进制」，说明 ltrace 不知道那个函数的原型：

```console
my_custom_func(0x7ffd1234, 0x9, 0x402010, 0) = 1     ← 参数没法解读
```

```bash
# 写一个原型描述文件
cat > /tmp/lab/myproto.conf <<'EOF'
# 格式：返回类型 函数名(参数类型, ...);
int my_custom_func(char*, int, char*, int);
EOF
ltrace -F /tmp/lab/myproto.conf -e my_custom_func ./target
```

```console
my_custom_func("secret", 9, "0x402010", 0) = 1       ← 第 1 个参数可读了
```

**解读**：`-F` 让 ltrace 能解码自定义库函数。**系统库的现成配置在 `/usr/share/ltrace/*.conf`**（可用 `dpkg -L ltrace` 查看实际路径）。

---

## 6. 输出解读

### 6.1 行格式

```
strcmp("wrong", "s3cr3t")              = -7
────── ────────────────                 ──
  ①           ②                          ③
```

| 位置 | 含义 |
|------|------|
| ① 函数名 | 被调用（或即将返回）的**库函数** |
| ② 参数列表 | 已按 ABI 解码（字符串自动解引用，显示为 `"..."`） |
| ③ 返回值 | `= 值`（指针显示为 `0x...`，字符串显示为 `"..."`） |

**特殊标记**：

| 标记 | 含义 |
|------|------|
| `<unfinished ...>` | 函数**开始**执行（还没返回） |
| `<... func resumed>` | 之前那个未完成的函数**返回了** |
| `--- SIGCHLD (Child exited) ---` | 收到信号（子进程退出） |
| `+++ exited (status N) +++` | 程序退出，返回码 N |
| `--- SIGSEGV ... ---` | 崩溃（段错误） |
| `[pid NNNN]` | 该调用来自哪个进程/线程（多进程场景） |
| `[0.000421]` | `-r`：相对时间 |
| `[0x4011e3]` | `-i`：发起调用的指令地址 |

### 6.2 高价值函数速查（**按「想知道什么」挑 `-e` 过滤**）

| 想知道 | 跟踪这些函数 |
|--------|--------------|
| **有没有硬编码口令/密钥** | `strcmp`、`strncmp`、`strcasecmp`、`memcmp`、`bcrypt`、`crypt` |
| 文件与配置访问 | `fopen`、`open`、`fgets`、`fread`、`access`、`stat` |
| 字符串处理（解析逻辑） | `strtok`、`strcpy`、`strncpy`、`sprintf`、`snprintf`、`strlen` |
| 数值解析 | `atoi`、`atol`、`strtol`、`sscanf` |
| 内存布局（找关键缓冲区） | `malloc`、`calloc`、`realloc`、`memcpy`、`memmove` |
| 加密/哈希 | `EVP_*`、`AES_*`、`SHA*`、`MD5*`、`RAND_*` |
| 网络行为 | `getaddrinfo`、`gethostbyname`、`connect`、`recv`、`send`、`SSL_*` |
| 执行外部命令 | `system`、`popen`、`exec*` |
| 时间/随机（找种子） | `time`、`gettimeofday`、`rand`、`srand`、`random` |
| 环境与用户 | `getenv`、`getuid`、`geteuid`、`setuid` |
| 动态加载 | `dlopen`、`dlsym` |

### 6.3 成功判据

- **能指出「关键判断发生在哪个库调用」**（如 `strcmp` 返回 0 的那一次）；
- **能用 `-i` 拿到调用地址**，并在 objdump/gdb 里对应上；
- **输出中参数不再被截断**（`-s` 已调大）；
- **能找到「静态看不出来的运行时值」**（如实际比较的字符串、实际请求的域名）。

---

## 7. 与其他工具配合

```
① 先判断「能不能用 ltrace」
   file t                     → 动态链接？(statically linked = ltrace 无效)
   objdump -T t | grep UND    → 导入了哪些库函数（决定 -e 过滤什么）
        │
② 动态跟踪
   ├─ ltrace -e <关键库函数>  ← 本文：库调用语义（字符串、文件名）
   ├─ strace -e trace=<...>   → 系统调用（fd、网络、子进程）
   └─ ltrace -i → 拿调用地址 → objdump --start-address 看那条指令
        │
③ 静态对照
   ├─ objdump -d -M intel -C  → 反汇编（objdump.md）
   ├─ radare2 / rizin         → 交叉引用、控制流（radare2.md / rizin.md）
   └─ ghidra                  → 伪 C 代码（ghidra.md）
        │
④ 深入动态
   └─ gdb（断在库函数上、看完整调用栈、改返回值）  ← gdb.md
```

**典型闭环**：

```bash
# 1) ltrace 找出关键库调用与参数
ltrace -e 'strcmp+strncmp' -s 128 -i ./login wrong
# 2) 用 -i 的地址回到反汇编
objdump -d -M intel --start-address=0x401176 --stop-address=0x401200 ./login
# 3) 用 gdb 断在 strcmp 上验证 + 直接读参数
gdb -q ./login -ex 'b strcmp' -ex 'run wrong' -ex 'x/s $rdi' -ex 'x/s $rsi' -batch
```

```console
Breakpoint 1, __strcmp_avx2 () ...
0x7ffd...:	"wrong"
0x402004:	"s3cr3t"
```

- 静态反汇编：[`objdump.md`](objdump.md) ｜ 动态调试：[`gdb.md`](gdb.md)
- 交互式框架：[`radare2.md`](radare2.md)、[`rizin.md`](rizin.md) ｜ 反编译器：[`ghidra.md`](ghidra.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 什么输出都没有 | 目标是**静态链接**（含 Go/Rust 静态编译） | 改用 `strace`（系统调用仍在）或 [`gdb.md`](gdb.md) |
| 输出里全是「看不懂的十六进制参数」 | ltrace **不知道该函数的原型** | 写 `-F` 原型配置；或判断是否值得追（内部函数本来就不在 ltrace 范围内） |
| 字符串参数被截断（出现 `...`） | 默认只打印 32 字节 | **`-s 256`**（或更大） |
| 输出太长无法阅读 | 没过滤 | **`-e <函数列表>` / `-x <排除列表>` / `-l <库>`** |
| 看不到子进程的调用 | 默认不跟随 fork | **加 `-f`** |
| `ptrace: Operation not permitted` | 权限不足 / 容器缺 `SYS_PTRACE` / Yama 限制 / 目标是 setuid | `sudo`；容器加 `--cap-add=SYS_PTRACE`；调整 `ptrace_scope`（**仅自己的机器**） |
| `Couldn't find .dynsym` / 无法初始化 | 目标是静态/被加壳/非常规格式 | 用 `-D` 看 ltrace 自身调试信息；改走 strace 或 gdb |
| 看不到期望的函数（如 `strcmp`） | 被编译器**内联**了（`-O2` 常见） | 用 `-O0` 版本；或改用 `strace`（系统调用不会被内联）/gdb |
| attach 的进程立刻崩溃/行为异常 | 目标有反调试检测 | 理解机制即可；**不要在生产服务上做**（见第 9 节） |
| 性能极差、程序变慢很多 | ltrace 每个调用都中断 | 缩小 `-e` 范围；或用 `-c` 统计模式；或用 `LTRACE_*` 采样（视版本） |
| 多线程输出交错难读 | 默认合并输出 | `-o file` 写文件后分析；`-f` 看清 pid 前缀 |
| 时间戳与日志对不上 | 时区/时间基准不同 | 用 `-ttt`（含日期）并注意时区；`-r` 看相对时间 |
| `-e` 过滤器写错没生效 | 表达式语法/通配符不对 | 先不加 `-e` 跑一次，确认函数名拼写；再用 `-e 'func*'` |

---

## 9. 防御视角（蓝队 / 软件保护）

ltrace 的价值在于「**它证明了运行时数据对本地攻击者是可见的**」。

| 攻击者能用它做什么 | 防御方应该怎么做 |
|--------------------|------------------|
| 看到硬编码的**口令/密钥**（`strcmp("x","s3cr3t")`） | **不要把秘密放在客户端**：所有校验与加密密钥放服务端 |
| 看到**实际访问的文件/域名**（`fopen`/`getaddrinfo` 参数） | 敏感路径与内部主机名不要硬编码在客户端；用服务端下发 |
| 看到**加密前的明文**（`EVP_DigestUpdate(..., "password", 8)`） | 明白「本地加密不能保护数据不被本人读取」；用服务端密钥 + 最小数据下发 |
| 定位**关键校验点**（`-i` 拿到地址） | 客户端校验仅用于 UX；**安全边界必须在服务端** |
| 排除/绕过**客户端许可证检查** | 许可校验放服务端；或用不可绕过的硬件绑定（仍有成本） |
| 分析**运行中的服务**（`-p`）以观察其行为 | 生产服务器限制 `ptrace`（`yama/ptrace_scope=1/2`）、关键进程设 `PR_SET_DUMPABLE=0`、容器不加 `SYS_PTRACE` |
| 通过 `-l libcrypto.so` 观察**加密流程** | 关键操作放 TEE/HSM；不把可逆密钥放进程内存 |

**蓝队可检测/加固的三条**：

1. **限制 ptrace**：`/proc/sys/kernel/yama/ptrace_scope = 1`（或 2），并给敏感服务设置 `prctl(PR_SET_DUMPABLE, 0)`；
2. **审计 attach 行为**：auditd 监听 `ptrace` 系统调用（对数据库、SSH、Web 服务进程的 attach 是**高价值告警**）；
3. **不要依赖客户端安全**：任何一个 ltrace 输出都在提醒你——**攻击者拥有本机 = 拥有本机所有明文**。

**软件加固的现实结论**：`strip`、加壳、反调试、混淆都只是**抬高成本**；**真正的边界是「服务端校验 + 不把秘密交给不受信任的客户端」**。

---

## 10. 参考

- ltrace 官网：<https://www.ltrace.org/>
- Debian 包页（含手册与配置位置）：<https://packages.debian.org/ltrace>
- Kali 说明：`ltrace` **不在** Kali 官方工具清单中，来自 Debian 的 **`ltrace`** 包。安装：`sudo apt install ltrace`
- 本地手册与配置：`man ltrace`、`ltrace --help`、`dpkg -L ltrace`（查看 `/usr/share/ltrace/*.conf` 原型文件）
- 配套阅读：[`strace`]（`man strace`、系统调用视角）、[`objdump.md`](objdump.md)、[`gdb.md`](gdb.md)、[`ghidra.md`](ghidra.md)

## ⚠️ 法律与伦理

`ltrace` 会**读取目标进程的全部运行时数据**（包括其中的口令、密钥、文件内容）。对**不属于你**的程序或进程使用时，可能触犯：

- 《刑法》第 285 条（非法获取计算机信息系统数据、非法控制计算机信息系统）；
- 对**非自有软件**做逆向以**规避技术措施/DRM**（《著作权法》相关规定与许可协议）；
- **窃取商业秘密**（《反不正当竞争法》第 9 条）；
- 若涉及他人个人信息，还可能触犯《刑法》第 253 条之一（侵犯公民个人信息罪）与《个人信息保护法》。

**请严格遵守**：

1. **只跟踪你自己编写的程序**、**CTF 靶题**、**书面授权的研究目标**、或**你拥有并有权分析的软件**；
2. **绝不对生产服务或他人的进程 attach**（这既是法律问题，也可能导致服务异常）；
3. 发现商业软件漏洞请走**厂商漏洞披露流程**；
4. 在自己的机器上测试时，也请**避免 attach 系统关键服务**以防影响系统稳定性；
5. 本教程所有示例请用第 5 节的自编程序（`login.c`/`parse.c`/`netprobe.c`）复现。
