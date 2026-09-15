# dex2jar（Android dex ↔ jar / smali 转换工具集）

> **一句话**：把 Android 的 `classes.dex`（Dalvik 字节码）**翻译成 Java 的 `.class`/`.jar`**，再用 Java 反编译器读源码；反过来也能把 `.jar` 转回 dex、把 dex 拆成 smali（或把 smali 装回 dex）——**Android 逆向的基本搬运工具**。
> **分类**：逆向工程 / Android 应用分析 ｜ **Kali 包**：`dex2jar`（命令 `d2j-dex2jar`、`d2j-dex2smali`、`d2j-smali`、`d2j-apk-sign` 等一整套 `d2j-*`）｜ **官方文档**：<https://www.kali.org/tools/dex2jar/> ｜ 上游：<https://github.com/pxb1988/dex2jar/tree/2.x>

---

## 1. 它解决什么问题

Android 应用的代码在 APK 里长这样：

```
app.apk（其实是个 zip）
├── AndroidManifest.xml     ← 二进制 XML（不是纯文本！）
├── classes.dex             ← 【Dalvik 字节码】—— 应用的真实逻辑
├── classes2.dex ...        ← 方法数超过 64K 时的分包（multidex）
├── resources.arsc          ← 编译后的资源索引
├── res/                    ← 资源
├── META-INF/               ← 签名
└── lib/arm64-v8a/*.so      ← 原生库（Native 代码，dex2jar 管不了）
```

**问题**：`.dex` 是**为 Dalvik/ART 虚拟机设计的指令集**，不是给 JVM 的。**Java 反编译器（JD-GUI、Procyon、CFR）读不了 `.dex`**。

**dex2jar 的作用就是做这个「翻译」**：

```
   classes.dex ──[d2j-dex2jar]──► classes-dex2jar.jar ──[JD-GUI / CFR / Procyon]──► Java 源码
        │
        └──────[d2j-dex2smali]──► *.smali（可读的汇编）──[编辑器改]──[d2j-smali]──► 新的 dex
```

**对比同类（选型非常关键）**：

| 工具 | 方向 | 特点 |
|------|------|------|
| **dex2jar** | dex → **jar**（JVM class） | 生态成熟；**依赖 Java 反编译器才能读源码**；是本篇主题 |
| **`jadx` / `jadx-gui`** | dex → **Java 源码（一步到位）** | **现代首选**：不用中间 jar，反编译质量通常更好；直接出可读 Java |
| **`apktool`** | apk → **smali + 资源** | **改包首选**：能把 APK 完整拆开、改 smali、再重新打包签名 |
| **`baksmali` / `smali`** | dex ↔ smali | 与 dex2jar 的 `d2j-dex2smali` / `d2j-smali` 功能重叠 |
| **`jd-gui` / `CFR` / `Procyon` / `fernflower`** | jar → Java 源码 | **dex2jar 的下游**——配合使用 |
| **`radare2` / `ghidra` / `rizin`** | 原生库 / DEX 反汇编 | 处理 `lib/*.so`（JNI）时要它们；见 [`radare2.md`](radare2.md)、[`ghidra.md`](ghidra.md)、[`rizin.md`](rizin.md) |
| **`frida` / `objection`** | 动态插桩 | **运行时**看/改行为——静态分析搞不定时的下一站 |

**dex2jar 今天还值得学吗**：

| 需求 | 更推荐 | 为什么还学 dex2jar |
|------|--------|-------------------|
| **看 Java 源码** | **`jadx`** | jadx 更好用；但 dex2jar **给你一个 jar**，可以用任何 Java 工具链处理（比如用 CFR、用 IDE 搜代码、用字节码工具再加工） |
| **改 smali 重新打包** | **`apktool`** | dex2jar 也能 `dex→smali→改→smali→dex`，在处理**已有 dex 而非 apk** 时有优势 |
| **需要 `.jar` 这个中间产物** | **dex2jar** | 后面的工具链（ASM、javap、jar2dex、weaver）都吃 jar |
| **jar → dex（打包）** | **dex2jar** | `d2j-jar2dex` 是这个工具集独有的能力 |

**一句话**：**「看源码」用 `jadx`；「改包」用 `apktool`；但只要你需要在「jar / dex / smali」这三种形态之间搬运，dex2jar 就是那套瑞士军刀。**

---

## 2. 工作原理

### 2.1 为什么不能直接反编译 dex

关键在于**两套指令集和对象模型的差异**：

```
                    Java 世界                          Android 世界
   ┌──────────────────────────────┐    ┌──────────────────────────────────┐
   │ 源码 .java                    │    │ 源码 .java                        │
   │      ↓ javac                  │    │      ↓ javac                      │
   │ 字节码 .class（JVM 栈机）      │    │ 字节码 .class                      │
   │      ↓ jar 打包               │    │      ↓ dx / d8                    │
   │ .jar（一堆 .class）            │    │ 字节码 .dex（【寄存器机】）        │
   │                              │    │  多个 class 合并进一个 dex         │
   └──────────────────────────────┘    └──────────────────────────────────┘
```

| 差异 | JVM（.class） | Dalvik/ART（.dex） |
|------|---------------|---------------------|
| **机器模型** | **栈式**虚拟机（操作数栈） | **寄存器式**虚拟机（v0-vN 寄存器） |
| **文件粒度** | 一个类一个 `.class` | **所有类合并进一个 `.dex`** |
| **常量池** | 每个 class 独立 | **全局共享**（这是 dex 体积小的主因） |
| **指令集** | `aload_0` / `invokevirtual` | `move-object` / `invoke-virtual` |
| **API 引用** | 直接引用类名 | **方法/字段用索引引用** |

**所以 dex2jar 不是「解压」，是「翻译」**——把寄存器机指令映射回 JVM 栈机指令。

### 2.2 dex2jar 的四个组件（官方描述）

```
┌───────────────────────────────────────────────────────────────────────┐
│ ① dex-reader      读 .dex/.odex（轻量 API，类似 ASM）                  │
│ ② dex-translator  负责转换：dex 指令 → dex-ir → ASM 字节码             │
│ ③ dex-ir          中间表示                                            │
│ ④ dex-tools       对 .class/.jar 做各种加工（签名、weave、access…）     │
└───────────────────────────────────────────────────────────────────────┘
```

**转换链**：

```
   classes.dex
        │  ① dex-reader 解析
        ▼
   dex-ir（中间表示）
        │  ② dex-translator
        ▼
   ASM 字节码（JVM）
        │  ③ 写出
        ▼
   classes-dex2jar.jar
        │  ④ 反编译器（JD-GUI / CFR / Procyon / fernflower）
        ▼
   Java 源码（可读）
```

**为什么反编译结果常常「能看但别扭」**：

| 原因 | 现象 |
|------|------|
| **寄存器 → 栈的映射不完美** | 出现临时变量、变量名丢失（`var1`、`v0`） |
| **编译优化（dx/d8/R8）** | 内联、去虚化 → 结构变了 |
| **混淆（ProGuard/R8）** | 类名/方法名变成 `a`、`b`、`c` |
| **try/catch 与 finally** | 可能被重写成奇怪的结构 |
| **lambda / 字符串拼接 / JSR/RET** | 容易出现「反编译失败」的片段 |
| **de-sugaring**（脱糖） | 语法糖被展开，看到的不是原始语法 |

> **结论**：**dex2jar / jadx 的输出都是「近似源码」，不是原始源码**。读的时候要按「字节码语义」去理解，而不是期望它逐字还原。

### 2.3 三个方向（这就是 dex2jar 的价值）

```
        ┌───────────────── d2j-dex2jar ─────────────────┐
  .dex ─┤                                                ├─► .jar（给 Java 工具链）
        └───────────────── d2j-dex2smali ───────────────┘
                                                         └─► .smali（可读可改的汇编）

  .smali ──── d2j-smali ────► .dex          （改完重新打包）

  .jar ────── d2j-jar2dex ──► .dex          （JVM 字节码 → Dalvik 字节码，需要 dx/d8）
```

**smali 是什么**：**Dex 的「汇编语言」**——可读、可改、可用文本编辑。

```smali
# 一个 smali 方法长这样（这就是 dalvik 字节码的文本形式）
.method public static isRooted()Z
    .registers 2
    const/4 v0, 0x0
    :try_start_0
    new-instance v1, Ljava/io/File;
    const-string v0, "/system/xbin/su"
    invoke-direct {v1, v0}, Ljava/io/File;-><init>(Ljava/lang/String;)V
    invoke-virtual {v1}, Ljava/io/File;->exists()Z
    move-result v0
    :goto_0
    return v0
.end method
```

**读懂 smali 的基本规则**：

| 记号 | 含义 |
|------|------|
| `.method` / `.end method` | 方法定义 |
| `.registers N` | 这个方法用多少个寄存器 |
| `v0`、`v1` | 寄存器（`p0` = this，`p1`+ = 参数） |
| `const/4 v0, 0x0` | 把 0 放进 v0（`/4` 表示 4 位立即数） |
| `invoke-virtual` | 调用实例方法（虚方法） |
| `invoke-direct` | 调用构造函数 / 私有方法 |
| `invoke-static` | 调用静态方法 |
| `move-result` | 取上一次调用的返回值 |
| `sget` / `sput` / `iget` / `iput` | 读写静态/实例字段 |
| `Ljava/io/File;` | 类型描述符（L 开头、; 结尾） |
| `Z` `I` `V` `Ljava/lang/String;` | boolean / int / void / String |

**改 smali 是「重打包」的核心**——因为 Java 源码改完还要重新编译（而你没有原始工程），**直接改 smali 更直接**。

---

## 3. 安装与快速上手

```bash
sudo apt install dex2jar
# 会装以下命令
for c in d2j-dex2jar d2j-dex2smali d2j-smali d2j-apk-sign d2j-jar2dex d2j-dex-weaver d2j-decrypt-string; do
  printf '%-22s ' "$c"; command -v "$c" || echo MISSING
done
```

```console
d2j-dex2jar           /usr/bin/d2j-dex2jar
d2j-dex2smali         /usr/bin/d2j-dex2smali
d2j-smali             /usr/bin/d2j-smali
d2j-apk-sign          /usr/bin/d2j-apk-sign
d2j-jar2dex           /usr/bin/d2j-jar2dex
d2j-dex-weaver        /usr/bin/d2j-dex-weaver
d2j-decrypt-string    /usr/bin/d2j-decrypt-string
```

```bash
d2j-dex2jar -h
```

```console
root@kali:~# d2j-dex2jar -h
usage: d2j-dex2jar [options] <file0> [file1 ... fileN]
options:
 --skip-exceptions            skip-exceptions
 -d,--debug-info              translate debug info
 -e,--exception-file <file>   detail exception file, default is $current_dir/[file-name]-error.zip
 -f,--force                   force overwrite
 -h,--help                    Print this help message
 -n,--not-handle-exception    not handle any exceptions thrown by dex2jar
 -nc,--no-code
 -o,--output <out-jar-file>   output .jar file, default is $current_dir/[file-name]-dex2jar.jar
 -os,--optmize-synchronized   optimize-synchronized
 -p,--print-ir                print ir to System.out
 -r,--reuse-reg               reuse register while generate java .class file
 -s                           same with --topological-sort/-ts
 -ts,--topological-sort       sort block by topological, that will generate more readable code, default enabled
version: reader-2.1-SNAPSHOT, translator-2.1-SNAPSHOT, ir-2.1-SNAPSHOT
```

```bash
d2j-dex2smali -h      # 输出与 d2j-baksmali 相同
```

```console
root@kali:~# d2j-dex2smali -h
usage: d2j-baksmali [options] <dex>
options:
 -b,--no-debug-info            [not impl] don't write out debug info (.local, .param, .line, etc.)
 -f,--force                    force overwrite
 -h,--help                     Print this help message
 -l,--use-locals               output the .locals directive with the number of non-parameter registers, rather than the .register
 -o,--output <out>             output dir of .smali files, default is $current_dir/[jar-name]-out/
 -p,--no-parameter-registers   use the v<n> syntax instead of the p<n> syntax for registers mapped to method parameters
version: 2.1-SNAPSHOT
online help: https://sourceforge.net/p/dex2jar/wiki/Smali
```

```bash
d2j-smali -h
```

```console
root@kali:~# d2j-smali -h
usage: d2j-smali [options] [--] [<smali-file>|folder]*
options:
 --                             read smali from stdin
 -a,--api-level <API_LEVEL>     [not impl] numeric api-level, default 14 (ICS)
 -h,--help                      Print this help message
 -o,--output <FILE>             the dex file to be written, default out.dex
 -v,--version                   prints the version then exits
 -x,--allow-odex-instructions   [not impl] allow odex instructions
```

**最小可用（走一遍「apk → dex → jar」）**：

```bash
mkdir -p /tmp/dex-lab && cd /tmp/dex-lab

# ① 拿一个 APK：用你自己编译的、或 Kali 自带的示例
ls /usr/share/metasploit-framework/data/android/apk/ 2>/dev/null

# ② 从 APK 里取出 dex（APK 就是 zip）
unzip -o /usr/share/metasploit-framework/data/android/apk/*.apk 'classes*.dex' -d ./apk-unpacked 2>/dev/null || true
ls -l ./apk-unpacked/

# ③ dex → jar
d2j-dex2jar ./apk-unpacked/classes.dex -o ./app.jar
ls -l ./app.jar

# ④ 用 Java 工具看（三选一）
#    a) JD-GUI（图形界面）
#       sudo apt install jd-gui && jd-gui ./app.jar
#    b) 命令行反编译器 CFR（下载 cfr.jar 后）
#       java -jar cfr.jar ./app.jar --outputdir ./src-java
#    c) javap 看类与方法签名（不需要额外工具，JDK 自带）
javap -classpath ./app.jar -p "$(unzip -l ./app.jar | awk '/\.class$/{print $4; exit}' | sed 's#/#.#g; s#\.class$##')" 2>/dev/null | head -20
```

**如果只想「直接看源码」，用 `jadx`**（一条命令，不用中间 jar）：

```bash
sudo apt install jadx
jadx -d /tmp/dex-lab/src-jadx /usr/share/metasploit-framework/data/android/apk/*.apk
ls /tmp/dex-lab/src-jadx/sources/ | head
jadx-gui /usr/share/metasploit-framework/data/android/apk/*.apk     # 图形界面
```

---

## 4. 核心参数详解

> 全部取自上面的 `-h` 原文（`d2j-dex2jar` / `d2j-dex2smali` / `d2j-smali`），以及 Kali 工具页给出的其余 `d2j-*` 用法。

### 4.1 命令全景

| 命令 | 方向 | 一句话 |
|------|------|--------|
| **`d2j-dex2jar`** | **dex → jar** | **最常用**：把 dex 翻成 JVM 字节码 |
| **`d2j-dex2smali`** | dex → **smali** | 拆成可读可改的汇编（同 `d2j-baksmali`） |
| **`d2j-smali`** | **smali → dex** | 把改完的 smali 装回 dex |
| `d2j-baksmali` | dex → smali | 与 `d2j-dex2smali` 相同（别名/同一实现） |
| **`d2j-jar2dex`** | **jar → dex** | 调用 `dx` 把 JVM 字节码转成 dex |
| `d2j-jar2jasmin` | jar → jasmin | 拆成 jasmin（另一种汇编语法） |
| `d2j-jasmin2jar` | jasmin → jar | 装回 jar |
| **`d2j-apk-sign`** | —— | **用测试证书给 APK 签名**（重打包后必需） |
| `d2j-std-apk` | —— | **把 APK 清理成标准 zip**（修复对齐/冗余） |
| `d2j-asm-verify` | —— | **校验 jar 里的 .class 是否合法**（改字节码后验证） |
| `d2j-dex-recompute-checksum` | —— | **重算 dex 的 CRC 与 SHA-1**（改过 dex 后必须做，否则安装失败） |
| `d2j-jar-access` | —— | 增删 class/method/field 的**访问修饰符** |
| `d2j-jar-weaver` | —— | 在 jar 里**替换 invoke 调用**（AOP 式织入） |
| `d2j-dex-weaver` | —— | 在 dex 里替换 invoke |
| `d2j-decrypt-string` | —— | **静态解密被混淆的字符串**（配合指定解密方法） |
| `d2j-jar-remap` | —— | 重命名包/类/方法/字段（去混淆） |
| `d2j-init-deobf` | —— | 生成去混淆配置模板 |
| `d2j-class-version-switch` | —— | 切换 .class 的版本号 |
| `d2j-dex-dump` | —— | 把 dex/apk dump 成 jar |
| `dex2jar`（**已废弃**） | —— | 旧命令，会提示 `use the d2j-dex2jar if possible` |

### 4.2 `d2j-dex2jar` 参数

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `<file0> [file1 ...]` | **输入的 dex/odex/apk** | 可以一次给多个；**给 apk 也能处理** |
| `-o, --output <jar>` | 输出 jar 路径 | 默认 `$PWD/[文件名]-dex2jar.jar` |
| `-f, --force` | **覆盖已存在的输出** | 脚本化必加 |
| `-d, --debug-info` | **翻译调试信息**（行号、局部变量名） | **强烈建议加**：反编译后可读性明显提升（能看到行号） |
| `-nc, --no-code` | 不生成代码（只生成方法签名骨架） | 只想看「有哪些类/方法」时**快得多** |
| `-r, --reuse-reg` | 复用寄存器来生成 class | 某些混淆代码能改善结果 |
| `-ts, --topological-sort`（`-s`） | **按拓扑排序基本块** | **默认启用**；能让生成代码更可读 |
| `-os, --optmize-synchronized` | 优化 `synchronized` 块 | 目标用了同步块时试 |
| `-e, --exception-file <zip>` | 把详细异常写到 zip | **排错必备**：反编译抛异常时看里面 |
| `--skip-exceptions` | 跳过异常 | 想「能出多少出多少」时用 |
| `-n, --not-handle-exception` | 不做异常处理（更快，但可能崩） | 不推荐（除非你确定不需要） |
| `-p, --print-ir` | **打印中间表示到 stdout** | **深度排错/研究**用 |
| `-h, --help` | 帮助 | —— |

### 4.3 `d2j-dex2smali`（= `d2j-baksmali`）参数

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `<dex>` | 输入的 dex | 必需 |
| `-o, --output <dir>` | smali 输出目录 | 默认 `$PWD/[文件名]-out/` |
| `-f, --force` | 覆盖 | 脚本化必加 |
| `-l, --use-locals` | 输出 `.locals`（非参数寄存器数）而不是 `.registers` | 手工改 smali 时 `.locals` 更直观（**推荐**） |
| `-p, --no-parameter-registers` | 用 `v<n>` 而不是 `p<n>` 表示参数 | 需要与某些工具对齐时用 |
| `-b, --no-debug-info` | 不写调试信息（**当前版本标记 [not impl]**） | —— |
| `-h, --help` | 帮助 | —— |

### 4.4 `d2j-smali` 参数

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `[<smali-file>\|<folder>]*` | **要汇编的 smali 文件或目录** | 给目录会递归处理 |
| `--` | **从 stdin 读 smali** | 管道/脚本化 |
| `-o, --output <FILE>` | 输出 dex，默认 `out.dex` | 显式指定更清晰 |
| `-v, --version` | 打印版本 | —— |
| `-a, --api-level` | API 级别（**当前 [not impl]**） | —— |
| `-x, --allow-odex-instructions` | 允许 odex 指令（**当前 [not impl]**） | —— |
| `-h, --help` | 帮助 | —— |

### 4.5 其余关键命令的用法（来自 Kali 工具页）

| 命令 | 用法 |
|------|------|
| **`d2j-apk-sign`** | `d2j-apk-sign [options] <apk>`<br>`-o <out.apk>` 输出（默认 `<name>-signed.apk`）、`-t/--tiny` 用 tiny 签名、`-f` 覆盖 |
| **`d2j-asm-verify`** | `d2j-asm-verify [options] <jar0> [jar1 ...]`<br>`-d/--detail` 打印详细错误 |
| `d2j-dex-recompute-checksum` | `d2j-dex-recompute-checksum [options] dex`<br>`-o <out.dex>`（默认 `[name]-rechecksum.dex`） |
| `d2j-jar2dex` | `d2j-jar2dex [options] <dir>`<br>`-o <out.dex>` |
| `d2j-jar-access` | `d2j-jar-access [options] <jar>`<br>`-ac/-af/-am <ACC>` 加访问、`-rc/-rf/-rm <ACC>` 去访问、`-rd` 去调试信息 |
| `d2j-dex-weaver` | `d2j-dex-weaver [options] dex`<br>`-c <config>`、`-s <stub>`、`-o <out.dex>` |
| `d2j-jar-weaver` | `d2j-jar-weaver [options] jar`<br>`-c <config>`、`-s <stub jar>`、`-o <out.jar>` |
| `d2j-decrypt-string` | `d2j-decrypt-string [options] <jar>`<br>`-mn/-mo/-pd` 指定解密方法名/所属类/参数描述符、`-t` 参数类型、`-da` 深度分析、`-d` 删除解密方法 |
| `d2j-class-version-switch` | `d2j-class-version-switch <version> <old.jar> <new.jar>` |
| `d2j-std-apk` | `d2j-std-apk [options] <zip>`<br>`-o <out>` |
| `d2j-jar2jasmin` | `d2j-jar2jasmin [options] <jar>`<br>`-d` 反汇编调试信息、`-e <enc>` 编码、`-o <dir>` |
| `d2j-jasmin2jar` | `d2j-jasmin2jar [options] <jar>`<br>`-cv <ver>` class 版本、`-g` 自动生成行号、`-o <jar>` |

---

## 5. 实战演练

> **环境声明**：全部使用**你有权分析的应用**：
> - **你自己编译的 APK**（最推荐：你可以对照源码验证反编译质量）；
> - **开源应用的 APK**（如 F-Droid 上的开源软件）；
> - **CTF 的 Android 题目**；
> - Kali 自带的**示例 dex**（`/usr/share/metasploit-framework/data/android/apk/`）；
> - **恶意样本**（如 MalwareBazaar 的分析样本）——**必须在隔离虚拟机中处理，禁止联网**。
> **禁止**：分析他人的商业应用用于破解/去广告/盗版；绕过他人应用的技术保护措施。

### 场景 0：先造一个「自己的 APK」（这样你才知道正确答案）

如果你没有现成的 APK，**先自己编一个**——这是最有价值的练习方式，因为**你能对照源码验证每一步**。

```bash
# ① 安装 Android 构建工具（或用 Docker 的 android SDK 镜像）
command -v gradle || sudo apt install -y gradle
command -v javac || sudo apt install -y default-jdk

# ② 造一个最小的 Android 工程（这里是「结构示意」，实际需要 android SDK）
mkdir -p /tmp/myapp/src/com/example/lab && cd /tmp/myapp/src/com/example/lab
cat > Lab.java <<'EOF'
package com.example.lab;

public class Lab {
    private static final String SECRET = "CTF{d2j_lab}";

    public static boolean isRooted() {
        String[] paths = {"/system/xbin/su", "/system/bin/su", "/sbin/su"};
        for (String p : paths) {
            if (new java.io.File(p).exists()) return true;
        }
        return false;
    }

    public static String getToken(String user) {
        return SECRET + ":" + user.hashCode();
    }
}
EOF
echo "已写好示例类（实际打包需要 Android SDK / dx / d8）"
```

**如果不想折腾 Android SDK，用现成的 dex**：

```bash
# Kali 自带示例 dex（在 metasploit 的 android payload 里）
find /usr/share/metasploit-framework/data/android -name '*.dex' 2>/dev/null | head
# 或从任何开源 APK 里取
APK=/path/to/your/apk.apk
unzip -o "$APK" 'classes*.dex' -d /tmp/dex-lab/unpacked
ls -l /tmp/dex-lab/unpacked/
```

### 场景 1：dex → jar → Java 源码（主流程）

```bash
cd /tmp/dex-lab

# ① 看一眼 dex 是什么
file /tmp/dex-lab/unpacked/classes.dex
ls -l /tmp/dex-lab/unpacked/classes.dex
```

```console
/tmp/dex-lab/unpacked/classes.dex: Dalvik dex file version 035
-rw-r--r-- 1 root root 1234567 ... classes.dex
```

**解读**：

| 观察 | 含义 |
|------|------|
| `Dalvik dex file version 035` | dex 版本（035 = Android 早期；`038`/`039` 较新） |
| **有多个 `classes2.dex`、`classes3.dex`** | **multidex**：方法数超过 64K → **每个都要单独转换**！ |

```bash
# ② dex → jar（加 -d 翻译调试信息，提升可读性）
d2j-dex2jar -d -f -o ./app.jar /tmp/dex-lab/unpacked/classes.dex
ls -lh ./app.jar
```

```console
root@kali:~# d2j-dex2jar -d -f -o ./app.jar /tmp/dex-lab/unpacked/classes.dex
dex2jar classes.dex -> ./app.jar
-rw-r--r-- 1 root root 1.2M ... ./app.jar
```

**如果有多个 dex（multidex）——逐个转**：

```bash
for d in /tmp/dex-lab/unpacked/classes*.dex; do
  base=$(basename "$d" .dex)
  d2j-dex2jar -d -f -o "/tmp/dex-lab/${base}.jar" "$d"
done
ls -lh /tmp/dex-lab/*.jar
```

**解读**：**multidex 是新手最容易漏的点**——只转 `classes.dex` 会**丢掉大部分代码**。检查方法：

```bash
# 用并集的方式确认没漏
for j in /tmp/dex-lab/classes*.jar; do
  echo "== $j =="
  unzip -l "$j" | grep -c '\.class$'
done
```

```bash
# ③ 看 jar 里有什么（不需要反编译器就能做）
unzip -l ./app.jar | head -20
```

```console
Archive:  ./app.jar
  Length      Date    Time    Name
---------  ---------- -----   ----
      512  2026-09-15 10:30   com/example/lab/Lab.class
      ...
```

```bash
# ④ 用 JDK 自带的 javap 看类结构（最轻量）
CLS=$(unzip -l ./app.jar | awk '/\.class$/{print $4; exit}')
CLASS_NAME=$(echo "$CLS" | sed 's#/#.#g; s#\.class$##')
javap -classpath ./app.jar -p "$CLASS_NAME"
```

```console
Compiled from "Lab.java"
public class com.example.lab.Lab {
  private static final java.lang.String SECRET;
  public com.example.lab.Lab();
  public static boolean isRooted();
  public static java.lang.String getToken(java.lang.String);
  static {};
}
```

**解读（`javap` 的价值）**：

| 输出 | 含义 |
|------|------|
| `-p` | **显示 private 成员**（不加 `-p` 只看 public） |
| `public static boolean isRooted()` | 方法签名 + **返回类型**（`Z` 在 smali 里就是 boolean） |
| `static {}` | **静态初始化块**（常量赋值常在这里） |
| 还需要看字节码 | 加 `-c`：`javap -c -p -classpath ./app.jar com.example.lab.Lab` |

```bash
# ⑤ 反编译成 Java 源码（以 CFR 为例；JD-GUI 是图形界面版）
#    下载 cfr.jar（或用 apt 装的 jd-cli）
sudo apt install -y jd-cli 2>/dev/null || true
jd-cli ./app.jar -od /tmp/dex-lab/src-java
find /tmp/dex-lab/src-java -name '*.java' | head
cat "$(find /tmp/dex-lab/src-java -name 'Lab.java' | head -1)"
```

```java
package com.example.lab;

public class Lab {
    private static final String SECRET = "CTF{d2j_lab}";

    public static boolean isRooted() {
        String[] paths = new String[]{"/system/xbin/su", "/system/bin/su", "/sbin/su"};
        for (String p : paths) {
            if (new File(p).exists()) {
                return true;
            }
        }
        return false;
    }

    public static String getToken(String user) {
        return SECRET + ":" + user.hashCode();
    }
}
```

**解读**：**注意这里的 `SECRET` 是明文**——因为 `static final String` 常量会**在编译期被内联**。这是 Android 逆向里最常见的「意外收获」：

| 现象 | 原因 |
|------|------|
| **硬编码密钥/URL 明文可见** | 编译期内联 + 无混淆 |
| 字符串变成了乱码/加密调用 | **有字符串混淆**（用 `d2j-decrypt-string` 处理，见场景 3） |
| 类名/方法名是 `a`、`b`、`c` | **有 ProGuard/R8 混淆** |

**⑥ 与 `jadx` 对比（推荐同时用，互为印证）**：

```bash
sudo apt install -y jadx
jadx -d /tmp/dex-lab/src-jadx /tmp/dex-lab/unpacked/classes.dex
diff -u "$(find /tmp/dex-lab/src-java -name 'Lab.java' | head -1)" \
        "$(find /tmp/dex-lab/src-jadx -name 'Lab.java' | head -1)" | head -40
```

**解读**：**dex2jar + 反编译器** 与 **jadx** 的结果**经常不同**（尤其是复杂的控制流、try/catch、lambda）：

| 情况 | 怎么选 |
|------|--------|
| jadx 反编译失败/输出崩 | 用 dex2jar + CFR/Procyon 试 |
| dex2jar 输出难读 | 用 jadx |
| **两者输出不一致** | **都不可尽信**，去看 `javap -c` 的**字节码**才是真相 |
| **必须确认实现细节** | **一定回到 smali / 字节码** |

### 场景 2：改应用（dex → smali → 改 → dex → 签名）

**这是「重打包」的核心流程**。**只在你自己拥有/授权的应用上做。**

**2a. dex → smali**

```bash
cd /tmp/dex-lab
d2j-dex2smali -f -l -o /tmp/dex-lab/smali-out /tmp/dex-lab/unpacked/classes.dex
# -l : 用 .locals 而不是 .registers（手工改更直观）
find /tmp/dex-lab/smali-out -name '*.smali' | head
```

```console
/tmp/dex-lab/smali-out/com/example/lab/Lab.smali
```

```bash
# 看 smali 长什么样
sed -n '1,60p' /tmp/dex-lab/smali-out/com/example/lab/Lab.smali
```

```smali
.class public Lcom/example/lab/Lab;
.super Ljava/lang/Object;
.source "Lab.java"

# static fields
.field private static final SECRET:Ljava/lang/String; = "CTF{d2j_lab}"

# direct methods
.method public constructor <init>()V
    .locals 0

    .line 6
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static isRooted()Z
    .locals 6

    const/4 v0, 0x3

    new-array v1, v0, [Ljava/lang/String;
    ...
```

**解读（这是读懂 smali 的最好方式）**：

| smali 片段 | 对应的 Java |
|------------|-------------|
| `.class public Lcom/example/lab/Lab;` | `public class com.example.lab.Lab` |
| `.field ... SECRET:Ljava/lang/String; = "CTF{d2j_lab}"` | `private static final String SECRET = "CTF{d2j_lab}"` |
| `.method public static isRooted()Z` | `public static boolean isRooted()` |
| `.locals 6` | 用了 6 个**非参数**寄存器 |
| `const/4 v0, 0x3` | `v0 = 3` |
| `new-array v1, v0, [Ljava/lang/String;` | `String[] v1 = new String[v0]` |
| `p0` | `this`（实例方法）；静态方法里 `p0` 是第一个参数 |

**2b. 改 smali（做一个「无害的可见修改」作为练习）**

**最稳妥的练习：改一个字符串常量**（比如把欢迎语改掉），因为它**不改变字节码结构**。

```bash
cd /tmp/dex-lab/smali-out

# ① 找一个字符串常量
grep -rn 'const-string' com/example/lab/Lab.smali | head
grep -rn '"CTF{d2j_lab}"' . | head
```

```console
./com/example/lab/Lab.smali:8:.field private static final SECRET:Ljava/lang/String; = "CTF{d2j_lab}"
```

```bash
# ② 备份 → 修改
cp -r /tmp/dex-lab/smali-out /tmp/dex-lab/smali-orig
sed -i 's/"CTF{d2j_lab}"/"CTF{MODIFIED_BY_D2J}"/' com/example/lab/Lab.smali
grep -n 'MODIFIED_BY_D2J' com/example/lab/Lab.smali
```

**2c. smali → dex**

```bash
cd /tmp/dex-lab
d2j-smali -o /tmp/dex-lab/patched.dex /tmp/dex-lab/smali-out
ls -l /tmp/dex-lab/patched.dex
file /tmp/dex-lab/patched.dex
```

```console
-rw-r--r-- 1 root root 1234567 ... /tmp/dex-lab/patched.dex
/tmp/dex-lab/patched.dex: Dalvik dex file version 035
```

**2d. ⚠️ 关键一步：重算 dex 校验和**

```bash
d2j-dex-recompute-checksum -f -o /tmp/dex-lab/patched-fixed.dex /tmp/dex-lab/patched.dex
```

**解读**：**改了 dex 的内容后，dex 头里的 CRC32 与 SHA-1 就失效了**——Android 在加载时会校验，**不重算会直接崩溃/拒绝加载**。这是「改完 dex 装不上」的**最常见原因**。

**2e. 打包回 APK 并签名**

```bash
cd /tmp/dex-lab

# ① 把修好的 dex 放回 APK（用 zip 替换）
cp /path/to/your/apk.apk ./app-patched.apk
cd /tmp/dex-lab && zip -j app-patched.apk patched-fixed.dex    # 注意：要放到根目录并改名 classes.dex
# 更严谨的做法（保持 zip 结构与原名）：
mkdir -p repack-root && cp patched-fixed.dex repack-root/classes.dex
cd repack-root && zip -X -r ../app-patched.apk . -x '*.dex.orig'

# ② 用 dex2jar 的测试证书签名（未签名/签名错误的 APK 装不上）
d2j-apk-sign -f -o /tmp/dex-lab/app-signed.apk /tmp/dex-lab/app-patched.apk
ls -l /tmp/dex-lab/app-signed.apk
```

```console
# -t/--tiny 用更小的测试证书；不加则用默认测试证书
```

**解读（重打包为什么总要签名）**：

| 事实 | 说明 |
|------|------|
| **Android 要求 APK 有签名** | 否则无法安装 |
| **原签名在你改动后必然失效** | 签名是对整个包内容的摘要 |
| **签名不同 = 无法覆盖安装** | 必须**卸载旧版**再装；**且不能上架到应用商店** |
| `d2j-apk-sign` 用的是**测试证书** | 仅用于**本地安装测试**，不是发布用 |

**验证**：

```bash
# ① 用 apksigner 看签名信息（Android SDK 工具；或用 keytool）
unzip -l /tmp/dex-lab/app-signed.apk | grep -i 'META-INF'
# ② 装到你的测试机/模拟器（仅限你自己的设备）
adb install -r /tmp/dex-lab/app-signed.apk
```

**2f. 更省事的替代：用 `apktool` 做「拆包 → 改 smali → 打包」**

```bash
sudo apt install -y apktool
apktool d -f -o /tmp/apktool-out app.apk          # 拆：得到 smali + 资源
# （改 smali…）
apktool b /tmp/apktool-out -o app-rebuilt.apk     # 装回
d2j-apk-sign -f -o app-signed.apk app-rebuilt.apk # 签名（dex2jar 也能干这步）
```

**对比**：

| 流程 | 优点 | 缺点 |
|------|------|------|
| **dex2jar 全流程** | 对**已有 dex**很直接；工具集完整 | 要自己管 zip 结构、重算校验和 |
| **apktool** | **一步拆、一步装**，自动处理资源和校验和 | 需要 apktool；对「只有 dex 没有 apk」不适用 |

### 场景 3：混淆样本的处理（字符串解密 / 去混淆）

**3a. 识别字符串混淆**

```bash
cd /tmp/dex-lab
jd-cli ./app.jar -od /tmp/dex-lab/src-java2 2>/dev/null
grep -rn 'decrypt\|decode\|StringFog\|\\u00' /tmp/dex-lab/src-java2 --include='*.java' | head
```

**典型混淆后的代码**：

```java
// 混淆前：  Log.d("TAG", "https://api.example.com/v1/login");
// 混淆后：
Log.d("TAG", DecryptTool.a("aGVsbG8gd29ybGQ="));
// 或者
Log.d("TAG", "\u0f2a\u0f31\u0f4d...");
```

**3b. 用 `d2j-decrypt-string` 静态解密**

```bash
d2j-decrypt-string -h
```

```console
root@kali:~# d2j-decrypt-string -h
usage: d2j-decrypt-string [options] <jar>
options:
 -cp,--classpath <cp>                 add extra lib to classpath
 -d,--delete                          delete the method which can decrypt the strings
 -da,--deep-analyze                   use dex2jar IR to static analyze and find more values like byte[]
 -f,--force                           force overwrite
 -h,--help                            Print this help message
 -m,--methods <cfg>                   a file contain a list of methods
 -mn,--decrypt-method-name <name>     owner of the method which can decrypt the strings
 -mo,--decrypt-method-owner <owner>   example: java.lang.String
 -o,--output <out>                    output .jar, default $current_dir/[jar-name]-decrypted.jar
 -pd,--parameters-descriptor <type>   descriptor for the method
 -t,--arg-types <type>                comma-separated types: boolean,byte,short,char,int,long,float,double,string
 -v,--verbose                         show more info
```

```bash
# 前提：你已经从反编译结果里找到了「解密方法」的坐标
d2j-decrypt-string \
  -mo com/example/obf/DecryptTool \
  -mn a \
  -pd Ljava/lang/String; \
  -t string \
  -da \
  -f \
  -o /tmp/dex-lab/app-decrypted.jar \
  /tmp/dex-lab/app.jar
```

**解读（各参数的含义）**：

| 参数 | 含义 | 怎么找 |
|------|------|--------|
| `-mo <owner>` | **解密方法的所属类**（`a/b/c` 形式） | 在反编译结果里看 `DecryptTool.a("...")` → owner 是 `DecryptTool` |
| `-mn <name>` | **方法名** | 同上（`a`） |
| `-pd <desc>` | **参数描述符** | 参数是 String → `Ljava/lang/String;` |
| `-t <types>` | 参数类型列表（逗号分隔） | 参数是字符串 → `string` |
| `-da` | **深度静态分析**（连 `byte[]` 之类的间接值也尝试求出来） | **强烈建议加**，能解出更多字符串 |
| `-d` | **连解密方法一起删掉**（去混淆更彻底） | 输出更干净，但改动更大 |
| `-cp` | 加 classpath（解密方法依赖其他库时） | 报 `NoClassDefFoundError` 时加 |

**3c. 如果 `d2j-decrypt-string` 搞不定——回到 smali / 动态分析**

```bash
# 思路 1：看 smali 里的字符串表，手工解（简单编码常见）
grep -rn 'const-string' /tmp/dex-lab/smali-out --include='*.smali' | head -20

# 思路 2：用 radare2 / rizin 看 dex 的字符串区（有些混淆只是「换编码」）
r2 -q -c 'izz' /tmp/dex-lab/unpacked/classes.dex 2>/dev/null | head -20
#   见 10-逆向工程/radare2.md、rizin.md

# 思路 3：动态分析（最有确定性）—— 用 Frida hook 解密方法的返回值
#   （这属于动态插桩，超出本篇范围；静态路走不通时的下一站）
```

**3d. 去混淆（重命名）**

```bash
d2j-init-deobf -h
```

```console
root@kali:~# d2j-init-deobf -h
usage: d2j-init-deobf [options] <jar>
options:
 -f,--force                force overwrite
 -h,--help                 Print this help message
 -max,--max-length <MAX>   do the rename if the length > MIN, default is 40
 -min,--min-length <MIN>   do the rename if the length < MIN, default is 2
 -o,--output <out-file>    output .jar file, default $current_dir/[file-name]-deobf-init.txt
```

```bash
# ① 生成去混淆配置（把「名字太短」的类/方法都列出来准备改名）
d2j-init-deobf -o /tmp/dex-lab/deobf.txt /tmp/dex-lab/app.jar
head -20 /tmp/dex-lab/deobf.txt

# ② 手工编辑 deobf.txt（这个工具不会替你猜名字——你要结合逻辑自己命名）
#    格式是「旧名 → 新名」的映射

# ③ 应用重命名
d2j-jar-remap -c /tmp/dex-lab/deobf.txt -f -o /tmp/dex-lab/app-renamed.jar /tmp/dex-lab/app.jar
```

**解读**：**去混淆的名字必须靠人**——工具只能列出「该改哪些」，**「改成什么」取决于你对代码逻辑的理解**。这是 Android 逆向里最花时间的部分。

```bash
# ④ 改完字节码后必须验证（否则可能生成非法 class）
d2j-asm-verify -d /tmp/dex-lab/app-renamed.jar
```

### 场景 4（可选）：native 库与「dex 之外」的部分

**dex2jar 只管 dex——APK 里还有它管不了的东西**：

```bash
# 看 APK 里有没有原生库
unzip -l /path/to/apk.apk | grep -E '\.so$' | head
```

```console
     123456  2026-01-01 00:00   lib/arm64-v8a/libnative-lib.so
```

| APK 里的内容 | 用什么分析 |
|--------------|------------|
| `classes*.dex` | **dex2jar / jadx** |
| `lib/*/*.so` | **radare2 / rizin / Ghidra**（见 [`radare2.md`](radare2.md)、[`ghidra.md`](ghidra.md)、[`rizin.md`](rizin.md)） |
| `AndroidManifest.xml`（二进制） | **apktool**（会解码成文本）或 `aapt2 dump` |
| `resources.arsc` | apktool / `aapt2` |
| `assets/`、`res/raw/` | 直接看（可能是密钥、配置、证书、Dex 二次加载的载荷） |

```bash
# 判断「关键逻辑在 Java 还是 native」
#   ① 反编译 dex，找 System.loadLibrary / native 方法声明
grep -rn 'native \|loadLibrary' /tmp/dex-lab/src-java 2>/dev/null | head
```

```java
public class NativeBridge {
    static { System.loadLibrary("native-lib"); }
    public static native String getSecret();   // ← 逻辑在 .so 里，dex2jar 到此为止
}
```

**解读**：**这是静态分析的边界**——Java 层只看到「调用 native 方法」，**实现要转去分析 `.so`**：

```bash
# 用 radare2 打开 .so 看导出符号
unzip -o /path/to/apk.apk 'lib/arm64-v8a/*' -d /tmp/dex-lab/native
r2 -q -c 'iE' /tmp/dex-lab/native/lib/arm64-v8a/libnative-lib.so | head -20
# 用 Ghidra 做深度反编译（图形界面更适合）
```

**结论**：**dex2jar 是 Android 静态分析的「第一段」，不是全部**。完整的链路是：

```
APK ──unzip/apktool──►
      ├─ classes*.dex ──dex2jar──► jar ──反编译器──► Java 源码 ──读完
      ├─ lib/*.so      ──radare2/Ghidra/rizin──► 汇编/C ──继续读
      ├─ AndroidManifest.xml ──apktool──► 文本（权限、组件、intent-filter）
      ├─ resources.arsc / res/ ──apktool──► 资源
      └─ assets/ ──直接看──► 配置/证书/二次载荷（甚至又一个 dex！）
                                          ▲
                                          └─ 遇到就再来一轮（多层嵌套很常见）
```

**清理**：

```bash
rm -rf /tmp/dex-lab /tmp/apktool-out
```

---

## 6. 输出解读

### 6.1 `d2j-dex2jar` 的输出

```
dex2jar classes.dex -> ./app.jar
```

| 现象 | 含义 |
|------|------|
| `-> ./app.jar` | **成功** |
| 报错并输出 stack trace | 转换失败；**用 `-e <file.zip>` 看详细异常** |
| **没有报错但 jar 是空的** | dex 里没有能转换的代码（比如全是 native 声明）；或 dex 加密了 |
| 输出了大量 `Exception ... but continue` | 部分方法转换失败（**加 `-e` 收集**，看是哪些） |

**生成 jar 后的检查**：

```bash
unzip -l app.jar | grep -c '\.class$'     # 有多少个类
unzip -l app.jar | awk '/\.class$/{print $4}' | head -20   # 包名结构（能看出混淆程度）
```

| 观察 | 结论 |
|------|------|
| 包名是 `com/example/lab/...` | **没混淆** |
| 包名是 `a/a/a.class`、`b/c.class` | **ProGuard/R8 混淆** |
| 有 `$$` 结尾的类 | 编译器生成的**匿名类 / lambda** |
| 有 `R$id`、`R$string` | 资源类（通常不用看） |

### 6.2 反编译结果的整体判读

| 观察 | 结论 | 下一步 |
|------|------|--------|
| 源码基本可读 | 没混淆或轻混淆 | 直接读 |
| 类/方法名是单字母 | **有混淆** | 结合**字符串常量**和**调用关系**推断用途；或去动态分析 |
| 字符串是乱码 / 都是 `X.a("...")` | **字符串混淆** | `d2j-decrypt-string` |
| 大量 `native` 声明 | **逻辑在 .so** | 转 radare2 / Ghidra |
| 反编译某方法报错/输出 `/* 无法反编译 */` | 控制流复杂/字节码怪异 | **看 smali**（`d2j-dex2smali`）；或 `javap -c` |
| 代码里全是 `Reflection`/`Class.forName` | 动态加载/反分析 | 找**被加载的类名来源**（常在字符串里） |
| 有 `DexClassLoader` / `loadDex` | **二次加载（加壳/动态载荷）** | `assets/` 里找载荷 dex；静态分析到此为止 → 动态 hook |

### 6.3 「改 smali 重打包」的成败判断

| 阶段 | 成功标志 | 失败原因与解决 |
|------|----------|----------------|
| `d2j-dex2smali` | 目录里出现 `.smali` 文件 | dex 加密/加壳 → 需要先脱壳 |
| 改 smali | 语法正确（缩进/指令名/寄存器数） | **寄存器数写错会编译失败**（`.locals` 声明与实际使用不匹配） |
| `d2j-smali` | 输出合法的 dex（`file` 显示 `Dalvik dex file`） | 语法错误会报行号 |
| **重算校验和** | `d2j-dex-recompute-checksum` 无报错 | **漏了这步 → 装不上/崩溃** |
| zip 回 APK | APK 结构完整（`unzip -t` 通过） | **替换 dex 时改变了压缩方式/对齐** |
| **签名** | `d2j-apk-sign` 输出 `-signed.apk` | 没签名 → 无法安装 |
| 安装 | `adb install` 成功 | **签名不一致 → 必须先卸载旧版** |
| 运行 | 应用正常启动，修改生效 | 崩溃 → 看 `adb logcat`（很可能是 dex 校验/寄存器错误） |

```bash
# 排错必备：看设备日志
adb logcat -d | grep -iE 'dex|verify|ClassNotFound|AndroidRuntime' | tail -30
```

---

## 7. 与其他工具配合

```
   拿到 APK / dex
        │
        ├─ 0) 先看「是不是加壳」——加壳的 APK dex 是加密的
        │     （用 apktool 拆看 dex 是否异常小；或看 assets 里有没有大文件）
        │                        │
        │                        └─ 加壳 → 需先【脱壳】（动态 dump / Frida hook DexClassLoader）
        │                                  本篇不覆盖，属于进阶
        ▼
   ① 拆包
      unzip（取 dex/so/assets）
      apktool（完整拆：二进制 XML → 文本、资源、smali）
                    │
                    ├─► classes*.dex ──[d2j-dex2jar]──► jar ──► 反编译器 ──► Java 源码
                    │           └──────[d2j-dex2smali]──► smali（改它）
                    │                                        │
                    │                          [编辑] ──[d2j-smali]──► dex
                    │                                        │
                    │                          [d2j-dex-recompute-checksum]（必须！）
                    │                                        │
                    │                                   zip 回 APK
                    │                                        │
                    │                                  [d2j-apk-sign]（必须！）
                    │
                    ├─► lib/*.so ──► radare2 / rizin / ghidra    → 10-逆向工程/
                    ├─► AndroidManifest.xml / res / assets ──► 直接看（apktool 解码）
                    └─► assets 里的可疑文件 ──► binwalk / file / 再来一轮
                                                    → 09-数字取证/binwalk.md

   ② 静态分析跑不动时的下一站
      Frida / objection（动态插桩）
      jadx-gui（交互式看源码，体验更好）
      模拟器 + adb logcat（看运行时行为）
```

**配合要点**：

| 组合 | 怎么做 |
|------|--------|
| **`dex2jar` + `jd-cli`/JD-GUI/CFR** | **标配**：dex2jar 出 jar，反编译器出源码 |
| **`dex2jar` + `jadx`** | **交叉验证**：两者输出不一致时，回到 `javap -c` / smali |
| **`dex2jar` + `apktool`** | apktool 拆包（拿 smali 与资源），dex2jar 处理**已有的 dex**（或做 jar 方向的加工） |
| **`dex2jar` + `radare2`/`ghidra`** | Java 层看完了看 native 层（[`radare2.md`](radare2.md)、[`ghidra.md`](ghidra.md)） |
| **`d2j-jar2dex` + `dx`** | 把自写/改过的 Java 代码转成 dex（做测试载荷/补丁） |
| **`dex2jar` + `d2j-asm-verify`** | **改过字节码必须验证**，否则生成的 class 可能非法 |
| **`binwalk`** | APK 里嵌套另一个 APK/dex/zip 时，用 binwalk 定位（[`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md)） |
| **`apksigner` / `keytool`** | 验证签名的真正内容（`d2j-apk-sign` 只是方便封装） |

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 只拿到了 `classes.dex`，**反编译发现代码不全** | **multidex**：还有 `classes2.dex`、`classes3.dex`… | **逐个转换**（`for d in classes*.dex; do d2j-dex2jar "$d"; done`） |
| **改完 smali 重打包后应用闪退** | **没重算 dex 校验和** | `d2j-dex-recompute-checksum -o fixed.dex patched.dex` |
| 安装报 `INSTALL_PARSE_FAILED_NO_CERTIFICATES` | **没签名** | `d2j-apk-sign -f -o signed.apk patched.apk` |
| 安装报签名冲突 | 签名与原版不同 | **先卸载原版**；或（不可能）拿到原签名密钥 |
| `d2j-smali` 报语法错误 | smali 改错了（指令名/寄存器编号/ `.locals` 与使用不匹配） | 看报错行号；**`.locals N` 必须 ≥ 实际用到的寄存器数** |
| `d2j-dex2jar` 输出一堆异常 | 部分方法无法转换（复杂控制流/混淆） | 用 `-e err.zip` 收集异常；`--skip-exceptions` 先出结果；对失败的方法**看 smali** |
| 反编译出来是 `/* decompilation failed */` | 字节码复杂/被特意构造 | `javap -c` 看字节码；或 `d2j-dex2smali` 读 smali |
| 反编译出来完全看不懂（全是 `a.a(a)`） | **强混淆** | `d2j-decrypt-string`（字符串）+ 人肉去混淆（`d2j-init-deobf` + `d2j-jar-remap`）+ 动态分析 |
| `d2j-decrypt-string` 报找不到方法 | `-mo`/`-mn`/`-pd` 写错了 | 在反编译结果里**精确定位**解密方法的类与签名；参数类型不对会静默解不出 |
| `d2j-decrypt-string` 报 `NoClassDefFoundError` | 解密方法依赖别的库 | `-cp <额外jar>` 加 classpath |
| `d2j-jar2dex` 失败 | **需要 `dx`/`d8`**（Android SDK build-tools 里的工具） | 装 Android build-tools，或 `apt install d8`（若可用）；`dx` 已废弃，新项目用 `d8` |
| APK 里的 `AndroidManifest.xml` 打不开 | 是**二进制 XML** | 用 **apktool**（会解码成文本）；或 `aapt2 dump xmltree` |
| 改完的 APK **体积暴涨** | zip 重新打包方式变了（压缩级别/对齐） | 用 `apktool b`（会正确处理）；或 `zipalign` 对齐 |
| `adb install` 成功但启动就崩 | dex 校验失败 / smali 改错 | `adb logcat -d \| grep -i dex` |
| 拿到 `.odex` 处理不了 | odex 是**依赖于特定系统镜像**的优化版 dex | `d2j-dex2jar` 支持 odex，但需要匹配的 boot classpath；**优先找原始 dex** |
| dex 只有几十 KB 但 APK 有 50 MB | **加壳**（真代码在 assets 里，运行时解密加载） | 需要**脱壳**（动态 dump）；静态分析到此为止 |
| `dex2jar` 命令提示 deprecated | 旧版命令 | 用 **`d2j-dex2jar`** |
| 反编译结果「少了常量」 | `static final` 被**内联**了 | 正常现象；常量在**使用处**已展开 |
| 分析要长期做但结果无法复现 | 没记录工具版本与命令 | **每次分析都记录**：`d2j-dex2jar -h` 的版本行、完整命令、输入文件的 SHA-256 |

---

## 9. 防御视角（蓝队 / 移动安全）

dex2jar 是**攻击者用来分析你 App 的工具**——蓝队/开发的对策是**让分析变难**，同时**自己能分析**。

### 9.1 应用加固（提高逆向成本）

| 手段 | 作用 | 局限 |
|------|------|------|
| **代码混淆（R8/ProGuard）** | 类/方法/字段重命名为无意义名 | 只是**提高阅读成本**，不阻止分析 |
| **字符串加密（StringFog 等）** | 硬编码字符串变成解密调用 | 可被 `d2j-decrypt-string` / 动态 hook 解开 |
| **商业加壳（梆梆、爱加密、腾讯乐固…）** | dex 加密 + 运行时解密 | 需要**专门脱壳**；但**脱壳技术同样成熟** |
| **完整性校验 / 反调试 / 反注入** | 检测 Frida、调试器、改包 | 也是**猫鼠游戏**，且会增加崩溃与兼容性问题 |
| **把敏感逻辑放 native（.so）** | 提高分析门槛 | 仍需逆向 `.so`；且 native 也不是不可逆 |
| **服务端放真逻辑** | **最有效** | 客户端只做展示 —— **这是唯一根本性的手段** |

**关键认知**：

```
❌ 错误想法：「上了混淆/加壳就安全了」
✅ 正确想法：「客户端的一切都会被看到。秘密必须在服务端。」

  你放在客户端的：密钥、算法、业务规则——
  都只是【提高成本】，不是【保证安全】。
  真正的防线是：即使攻击者完全读懂你的客户端，他也拿不到不该拿的东西。
```

### 9.2 检测「有人在分析我的应用」

| 检测点 | 方法 |
|--------|------|
| **官方渠道外分发** | 监控应用市场 / 论坛 / 网盘 上的**改包版本**（哈希与官方包比对） |
| **签名不一致** | 定期扫全网，找**包名相同但签名不同**的 APK |
| **完整性校验（运行时）** | App 自检 dex/so 哈希，不匹配就降级或上报 |
| **反调试/反注入** | 检测 `ptrace`、`TracerPid`、Frida 端口/库名（**注意误报与稳定性**） |
| **服务端异常行为** | 改包版通常有**奇怪的 API 调用模式**（大量探测、参数异常） |
| **应用商店的仿冒 App** | 用应用商店的侵权投诉通道 |

### 9.3 蓝队/开发能主动做的事

| 场景 | 做法 |
|------|------|
| **自己的 App 安全评估** | **自己先用 dex2jar/jadx 拆一遍**——你能看到什么，攻击者就能看到什么 |
| **敏感信息自查** | 在反编译结果里 `grep` 关键字（`api_key`、`secret`、`password`、URL、云服务 AK/SK） |
| **CI 里加「反编译自检」** | 每次发版自动反编译并扫敏感字符串（**成本极低、收益极高**） |
| **第三方 SDK 审计** | 反编译看**引入的 SDK 带了什么**（有些 SDK 会内嵌密钥或回传数据） |
| **恶意 App 分析** | dex2jar 也是**防御工具**：分析恶意 APK 的行为（**在隔离环境**） |
| **应急响应** | 拿到可疑 APK，拆开看权限、C2 地址、数据外发逻辑 |

**一个非常实用的自检脚本（在自己的 CI 里跑）**：

```bash
#!/usr/bin/env bash
# 对自己发布前的 APK 做「敏感信息泄露」自检
APK="${1:?用法: $0 app.apk}"
WORK=$(mktemp -d); cd "$WORK" || exit 1

unzip -q "$APK" 'classes*.dex'
for d in classes*.dex; do d2j-dex2jar -f -o "${d%.dex}.jar" "$d" >/dev/null 2>&1; done
jd-cli ./*.jar -od ./src >/dev/null 2>&1

echo "=== 可能的敏感信息 ==="
grep -rInE '(api[_-]?key|secret|token|password|passwd|AKID|access[_-]?key)' ./src --include='*.java' | head -30
echo
echo "=== 硬编码 URL ==="
grep -rhoE 'https?://[a-zA-Z0-9./?=_%:-]+' ./src --include='*.java' | sort -u | head -30
echo
echo "=== 云服务凭据痕迹 ==="
grep -rInE '(AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35}|sk_live_[0-9a-zA-Z]{24})' ./src --include='*.java' | head
```

**运行这个脚本能在发版前拦下大量低级事故**（硬编码密钥、内网地址、测试凭据）。

---

## 10. 参考

- Kali 工具页（含全部 `d2j-*` 命令的 `-h` 输出）：<https://www.kali.org/tools/dex2jar/>
- 上游仓库（2.x 分支）：<https://github.com/pxb1988/dex2jar/tree/2.x>
- 官方 Wiki（Smali / Jasmin / DexWeaver / JarWeaver 用法说明）：<https://sourceforge.net/p/dex2jar/wiki/>
- Kali 包跟踪：<https://pkg.kali.org/pkg/dex2jar>
- 本地命令与自省：`d2j-dex2jar -h`、`d2j-dex2smali -h`、`d2j-smali -h`、`d2j-apk-sign -h`、`d2j-decrypt-string -h`、`d2j-init-deobf -h`、`dex2jar`（已废弃）
- 相关工具与规范：
  - Android DEX 格式规范：<https://source.android.com/docs/core/runtime/dex-format>
  - `jadx`（**推荐的 dex→Java 一步到位工具**）：<https://github.com/skylot/jadx>
  - `apktool`（拆包/重打包首选）：<https://apktool.org/>
- 配套教程：[`radare2.md`](radare2.md)、[`rizin.md`](rizin.md)、[`ghidra.md`](ghidra.md)、[`objdump.md`](objdump.md)、[`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md)

## ⚠️ 法律与伦理

Android 逆向的**合法边界非常清晰**，请逐条确认：

**① 可以做的**

| 场景 | 说明 |
|------|------|
| **分析自己开发/自己拥有的 App** | ✅ |
| **分析开源应用**（F-Droid 等来源，遵守其许可证） | ✅ |
| **CTF 的 Android 题目** | ✅（遵守比赛规则） |
| **获得书面授权的安全评估** | ✅（在授权范围内） |
| **恶意样本分析**（在隔离环境中，出于防御目的） | ✅ |
| **学术研究**（合规审查通过、数据合规） | ✅ |

**② 不能做的（明确违法/违规）**

| 行为 | 涉及法律 |
|------|----------|
| **破解他人商业软件**（去广告、解锁付费、绕过授权） | 《著作权法》（规避技术措施）、《反不正当竞争法》；情节严重可能触犯《刑法》第 217 条（侵犯著作权罪） |
| **重打包他人 App 并分发** | 著作权侵权 + 可能涉及《刑法》第 285 条之三（**提供侵入、非法控制计算机信息系统的程序、工具**） |
| **植入后门/恶意代码后重打包** | 《刑法》第 285/286 条 |
| **提取他人应用中的密钥后用于访问其服务** | 《网络安全法》第 27 条、《刑法》第 285 条 |
| **绕过 DRM / 技术保护措施** | 各国法律普遍禁止（DMCA 1201 等；中国《著作权法》第 49 条） |
| **用分析结果泄露未公开漏洞** | 违反负责任披露；可能构成帮助侵权 |
| **分析他人设备上的 App / 抓取他人数据** | 《个人信息保护法》《数据安全法》 |

**③ 关于「加壳/混淆」的重要提醒**

- **绕过他人应用的技术保护措施本身就可能违法**（《著作权法》第 49 条：不得规避技术措施）；
- **即使是为了「研究」，也不等于可以规避他人的保护措施**——研究豁免有严格的法定条件与范围；
- 你的授权范围**不覆盖第三方 SDK 和第三方库**——分析它们可能涉及**第三方的权利**。

**④ 恶意样本分析的特殊要求**

- **必须在隔离的虚拟机/专用设备**中进行，**禁止联网**（样本可能有 C2 回连）；
- **不要在主工作机上解包**（有些恶意 APK 会利用解包工具的漏洞）；
- **样本与提取物按核心证据保管**，不传播；
- **不上传到公共平台**（除非是专门的、合规的样本库，且已脱敏）。

**⑤ 报告与披露**

- 分析结论涉及**未公开漏洞**时，走**负责任披露**流程（先联系厂商）；
- **脱敏后再外发**：不公开可复现的完整利用链、不公开他人的密钥/凭据；
- 提取到的**用户数据/个人信息**不得留存、不得外传。

**必须遵守**：

1. **只分析你自己拥有、开源、CTF 题目、或获得书面授权的应用**；
2. **不破解商业软件、不重打包分发、不绕过技术保护措施**；
3. **不在他人设备上安装/修改应用**；
4. **恶意样本只在隔离环境分析**，禁止联网与传播；
5. **发现的漏洞通过厂商披露流程上报**，不擅自公开；
6. **研究/评估涉及的敏感信息严格保密**，用完销毁。
