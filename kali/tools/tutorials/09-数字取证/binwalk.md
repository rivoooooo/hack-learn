# binwalk（二进制/固件结构分析）

> **一句话**：把任意二进制文件（固件、镜像、可疑文件）当成「一摞嵌套的压缩包」拆开看——识别内嵌的文件签名、自动提取、算熵定位加密/压缩区、还能做反汇编与二进制对比。
> **分类**：数字取证 / 二进制与固件分析 ｜ **Kali 包**：`binwalk`（命令 `binwalk`）｜ **官方文档**：<https://github.com/ReFirmLabs/binwalk> ｜ `man binwalk`

---

## 1. 它解决什么问题

有一类取证对象**没有文件系统可讲**：

- **路由器/IoT 固件**（`.bin`）：里面是「厂商头 + 引导程序 + 内核 + 压缩的根文件系统」，一层套一层；
- **可疑的二进制 blob**：不知道是什么、里面有没有藏东西；
- **被混淆/加壳的文件**：需要先判断「哪一段是压缩数据、哪一段是代码」；
- **被截断的镜像**：想确认「文件系统头在第几字节」。

`file` 命令只能告诉你「这是什么」，**binwalk 告诉你「里面有什么、在哪、有多大」**：

```console
$ binwalk -B firmware.bin

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             TRX firmware header, little endian, image size: 37883904 bytes ...
28            0x1C            uImage header, header size: 64 bytes, ..., image name: "DD-WRT"
92            0x5C            Linux kernel ARM boot executable zImage (little-endian)
2460          0x99C           device tree image (dtb)
23432         0x5B88          xz compressed data
3145756       0x30001C        UBI erase count header, version: 1, ...
```

**这一屏输出就回答了「固件由哪些部分组成、各部分从哪开始」**——这是固件分析的第一步，也是 binwalk 最经典的用法。

对比同类：

| 工具 | 定位 | 差异 |
|------|------|------|
| **binwalk** | 二进制/固件**结构**分析 + 提取 + 熵 | 一个工具覆盖「识别→提取→分析」 |
| **`file` / `libmagic`** | 文件类型识别 | binwalk 复用 libmagic 的签名，但能**扫描整个文件**而不只是开头 |
| **`foremost`/`scalpel`** | 文件雕刻 | 面向「恢复删除的文件」；binwalk 面向「拆解已知结构」 |
| **`bulk-extractor`** | 特征提取 | 提邮箱/URL/凭据；binwalk 提**结构** |
| **`firmware-mod-kit`、`firmware-analysis-toolkit`** | 固件分析套件 | Kali 也有；binwalk 是其中的基础环节 |
| **`radare2`/`ghidra`** | 逆向反汇编 | binwalk 的 `-Y` 只做「架构猜测」；深度反汇编交给它们，见 [`../10-逆向工程/radare2.md`](../10-逆向工程/radare2.md) |

---

## 2. 工作原理

```
输入二进制
   │
   ├─① 签名扫描（-B，默认行为）
   │     用 libmagic + 内置的固件专用签名库（比 file 命令的签名更全：
   │     压缩流、文件系统、引导程序、固件头、Linux 内核…）
   │     逐偏移扫描 → 输出「偏移 | 十六进制偏移 | 描述」
   │
   ├─② 提取（-e / -D）
   │     命中可提取的类型 → 调用外部工具解压
   │       xz → xz -d；gzip → gunzip；squashfs → unsquashfs；
   │       LZMA → lzma；zip → unzip；tar → tar …
   │     输出到 _<文件名>.extracted/ 目录
   │
   ├─③ 递归提取（-M，matryoshka「套娃」）
   │     对①提取出的每个文件**再跑一遍 binwalk**
   │     默认递归 8 层（-d 可调）——固件常是多层嵌套
   │
   ├─④ 熵分析（-E）
   │     按块计算香农熵（0.0–1.0）：
   │       熵≈0        → 全零/填充（未使用区域、擦除块）
   │       熵≈0.5–0.7  → 普通代码/文本
   │       熵≈0.95+    → 压缩或加密数据
   │     输出 ASCII 熵图 + PNG（-J），阈值 -H/-L 可标出「上升沿/下降沿」
   │
   ├─⑤ 反汇编扫描（-Y）
   │     用 capstone 逐段尝试反汇编，猜 CPU 架构（ARM/MIPS/x86…）
   │
   ├─⑥ 原始压缩流扫描（-X deflate / -Z lzma）
   │     找**没有文件头**的裸压缩流（-X 无签名 deflate 很常见于固件）
   │
   └─⑦ 二进制对比（-W 等）
         两个固件版本/两个镜像逐字节 diff，找「哪个字节变了」
```

**关键概念**：

- **熵（entropy）**：binwalk 的熵图是**定位「加密/压缩区」的最快工具**。看到一大片 1.0 的高熵区，基本可以断定「这里是加密或压缩的数据」——**这也解释了为什么取证/逆向在这里往往卡住**。
- **`-e` 提取依赖外部工具**：binwalk 自己不实现解压，而是调用系统里的 `xz`/`gunzip`/`unsquashfs`（来自 `squashfs-tools`）/`7z` 等。**缺工具就会「识别到了但提取失败」**。
- **`-M` 套娃**：固件典型层次是 `固件头 → 内核(压缩) → 根文件系统(squashfs/UBIFS, 压缩)`，所以要递归。
- **`-B` 与默认行为**：v2 里**默认就是签名扫描**，`-B` 是显式写法（Kali 官方示例用的是 `-B`）。
- **版本注意**：binwalk v2.x 已宣布 EOL（帮助信息里有 `[NOTICE] Binwalk v2.x will reach EOL in 12/12/2025`）；上游的 **v3.x 是 Rust 重写**，参数有变化。**本文按 Kali 打包的 v2.4.3 写**。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install binwalk
# 提取所需的解压工具（重要！否则只能识别不能提取）
sudo apt install squashfs-tools p7zip-full xz-utils lzma unzip tar cpio
command -v binwalk
binwalk -h
```

```console
root@kali:~# binwalk -h

Binwalk v2.4.3
Original author: Craig Heffner, ReFirmLabs
https://github.com/OSPG/binwalk

Usage: binwalk [OPTIONS] [FILE1] [FILE2] [FILE3] ...
...
[NOTICE] Binwalk v2.x will reach EOL in 12/12/2025. Please migrate to binwalk v3.x
```

官方示例（对固件做签名扫描）：

```bash
binwalk -B ddwrt-linksys-wrt1200ac-webflash.bin
```

```console
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             TRX firmware header, little endian, image size: 37883904 bytes, CRC32: 0x95C5DF32, flags: 0x1, version: 1, header size: 28 bytes, loader offset: 0x1C, linux kernel offset: 0x0, rootfs offset: 0x0
28            0x1C            uImage header, header size: 64 bytes, header CRC: 0x780C2742, created: 2018-10-10 02:12:20, image size: 2150281 bytes, Data Address: 0x8000, Entry Point: 0x8000, data CRC: 0xA097CFEA, OS: Linux, CPU: ARM, image type: OS Kernel Image, compression type: none, image name: "DD-WRT"
92            0x5C            Linux kernel ARM boot executable zImage (little-endian)
2460          0x99C           device tree image (dtb)
23432         0x5B88          xz compressed data
23776         0x5CE0          xz compressed data
2117484       0x204F6C        device tree image (dtb)
3145756       0x30001C        UBI erase count header, version: 1, EC: 0x0, VID header offset: 0x800, data offset: 0x1000
```

**从这一屏能读出的情报**：

| 观察 | 结论 |
|------|------|
| `TRX firmware header` | 这是一个 TRX 格式固件（常见于 Broadcom 路由器） |
| `image size: 37883904` | 固件总大小 |
| `uImage header ... image name: "DD-WRT"` | 厂商/固件名（**直接暴露身份**） |
| `CPU: ARM` | 目标架构 → 后续逆向要用 ARM 工具链 |
| `xz compressed data` | 压缩区 → 需要解压才能继续分析 |
| `UBI erase count header` | 根文件系统是 UBI 格式（嵌入式常见） |

---

## 4. 核心参数详解

以下为 `binwalk -h` 的**完整真实参数**（按官方分组）。

### 4.1 签名扫描（最常用）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-B, --signature` | 扫描文件签名（**默认行为**） | 第一步永远先跑它 |
| `-R, --raw <str>` | 扫描**指定的字节序列** | 找自定义魔术字（如厂商标记） |
| `-A, --opcodes` | 扫描常见可执行指令特征 | 快速判断「哪段是代码」 |
| `-m, --magic <file>` | 使用自定义 magic 文件 | 加自有格式签名 |
| `-b, --dumb` | 关闭「智能关键字」（更机械的匹配） | 结果太少/太杂时试 |
| `-I, --invalid` | 也显示被标记为 invalid 的结果 | 默认过滤掉了部分弱匹配 |
| `-x, --exclude <str>` | **排除**匹配某字符串的结果 | 去噪音（如排除满屏的 `gzip` 假阳性） |
| `-y, --include <str>` | **只显示**匹配某字符串的结果 | 只看 `squashfs`/`uImage` |

### 4.2 提取（拆开固件）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-e, --extract` | **自动提取已知类型** | 核心参数；产物在 `_<file>.extracted/` |
| `-M, --matryoshka` | **递归提取**（对提取结果再扫再提） | **固件分析必加**（多层嵌套） |
| `-d, --depth <n>` | 递归深度（默认 8） | 层数多时调大（注意磁盘空间） |
| `-C, --directory <str>` | 提取到自定义目录 | 便于组织证据 |
| `-D, --dd <type[:ext[:cmd]]>` | **按类型定向提取**并可选执行命令 | 只提某一段（如 `-D 'xz:bin'`） |
| `-j, --size <n>` | 限制每个提取文件的**大小上限** | 防止「假头」吞掉整个文件 |
| `-n, --count <n>` | 限制提取文件数量 | 结果爆炸时保命 |
| `-r, --rm` | 提取后**删除雕刻出的中间文件** | 省空间（会丢失原始切片） |
| `-z, --carve` | **只雕刻数据，不调用解压工具** | 想自己解压时用 |
| `-V, --subdirs` | 按偏移建子目录 | 结构更清晰 |
| `-0, --run-as <str>` | 以指定用户身份运行外部解压工具 | **安全加固**：避免以 root 运行不可信解压工具 |
| `-1, --preserve-symlinks` | 不清理指向提取目录外的符号链接 | **危险**（符号链接攻击）；除非必要不要开 |

### 4.3 熵分析（判断加密/压缩）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-E, --entropy` | 计算并绘制**熵图** | 定位压缩/加密区 |
| `-F, --fast` | 更快的熵分析（精度略低） | 大文件先粗看 |
| `-J, --save` | 把熵图保存为 **PNG** | **报告配图必备** |
| `-Q, --nlegend` | 图上去掉图例 | 出图时美化 |
| `-N, --nplot` | 不生成图形（只输出数值） | 脚本化 |
| `-H, --high <float>` | **上升沿**阈值（默认 0.95） | 标记「进入高熵区」的位置 |
| `-L, --low <float>` | **下降沿**阈值（默认 0.85） | 标记「离开高熵区」的位置 |

### 4.4 反汇编与原始压缩流

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-Y, --disasm` | 用 capstone 猜测 CPU 架构 | 快速判断固件架构 |
| `-T, --minsn <n>` | 判定有效指令序列的最小条数（默认 500） | 调大减少误判 |
| `-k, --continue` | 不要在第一个匹配处停止 | 配合 `-Y` |
| `-X, --deflate` | 扫描**裸 deflate 流**（无 gzip/zlib 头） | 固件里很常见 |
| `-Z, --lzma` | 扫描**裸 LZMA 流** | 同上 |
| `-P, --partial` | 浅层但更快的扫描 | 大文件初筛 |
| `-S, --stop` | 第一个结果后停止 | 只想知道「有没有」 |

### 4.5 二进制对比

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-W, --hexdump` | 对多个文件做 hexdump / diff | 比较两个固件版本 |
| `-G, --green` | 只显示**所有文件都相同**的字节 | 找「共同部分」 |
| `-i, --red` | 只显示**所有文件都不同**的字节（注意这里的 `-i` 是 red 而非 include） | 找「版本差异」 |
| `-U, --blue` | 只显示**部分文件不同**的字节 | —— |
| `-u, --similar` | 只显示所有文件都相同的行 | —— |
| `-w, --terse` | diff 全部但只 hexdump 第一个文件 | 减少输出 |

> **注意**：`-i` 在「二进制对比」组里是 `--red`，而**不是**「include」的意思（include 是 `-y`）。这是 binwalk 参数里最容易搞混的地方。

### 4.6 通用

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-l, --length <n>` | 只扫描前 N 字节 | 只关心头部时加速 |
| `-o, --offset <n>` | 从指定偏移开始扫描 | 定向分析某一段 |
| `-O, --base <n>` | 给所有输出偏移**加基数** | 扫描切片时让偏移与整体对齐 |
| `-K, --block <n>` | 设置块大小 | —— |
| `-g, --swap <n>` | 每 n 字节反转后再扫描 | 大端/小端疑难场景 |
| `-f, --log <file>` | 结果写日志文件 | **报告留证** |
| `-c, --csv` | 结果输出为 CSV | 便于脚本处理 |
| `-t, --term` | 输出适配终端宽度 | 窄终端 |
| `-q, --quiet` | 抑制 stdout | 脚本化 |
| `-v, --verbose` | 详细输出 | 排错 |
| `-a, --finclude <regex>` | 只扫描**文件名**匹配正则的输入 | 批量目录处理 |
| `-p, --fexclude <regex>` | 跳过**文件名**匹配正则的输入 | 排除无关文件 |
| `-s, --status <port>` | 启用状态服务端口 | 长任务监控进度 |

---

## 5. 实战演练

> **环境声明**：以下使用**自建 / 公开合法素材**：
> - **固件**：自己路由器的官方固件（**你拥有**）、或 OpenWrt/DD-WRT 等**开源固件**、或厂商公开下载的固件包。**部分固件的 EULA 禁止逆向，请先确认法律与授权**。
> - **通用二进制**：自己编译的程序、公开的 CTF 附件、你自己造的嵌套压缩包。
> **禁止**分析来源不明的他人设备镜像；**禁止**把 binwalk 的提取流程用在需要授权的商业固件上（先看许可）。

### 场景 1：拆一个固件（从识别到拿到根文件系统）

```bash
# ① 先看是什么、有多大
file firmware.bin
ls -lh firmware.bin
```

```console
firmware.bin: data
-rw-r--r-- 1 user user 32M Sep 15 12:00 firmware.bin
```

```console
# file 只说 data —— 典型的固件情况，交给 binwalk
```

```bash
# ② 签名扫描（先只看结构，不提取）
binwalk -B firmware.bin
```

```console
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             TRX firmware header, little endian, image size: 37883904 bytes, flags: 0x1, version: 1, header size: 28 bytes
28            0x1C            uImage header, header size: 64 bytes, created: 2018-10-10 02:12:20, image size: 2150281 bytes, OS: Linux, CPU: ARM, image name: "DD-WRT"
92            0x5C            Linux kernel ARM boot executable zImage (little-endian)
23432         0x5B88          xz compressed data
3145756       0x30001C        UBI erase count header, version: 1, EC: 0x0, VID header offset: 0x800, data offset: 0x1000
```

**解读（这是固件分析的「地图」）**：

| 偏移 | 内容 | 下一步 |
|------|------|--------|
| `0x0` | TRX 固件头 | 说明是 TRX 打包（Broadcom） |
| `0x1C` | uImage 头，`CPU: ARM` | **确认架构 = ARM**（后续逆向要对应工具链） |
| `0x5C` | ARM zImage 内核 | —— |
| `0x5B88` | xz 压缩数据 | 解压后是内核或根文件系统 |
| `0x30001C` | UBI 头 | 根文件系统在 UBI 卷里（**要配合 `ubireader` 处理**） |

```bash
# ③ 自动提取（递归拆套娃）
sudo binwalk -e -M -C /evidence/fw firmware.bin
```

```console
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
...
WARNING: Extractor.execute failed to run external extractor 'unsquashfs -f -d ...': [Errno 2] No such file or directory: 'unsquashfs'
```

**解读**：**这就是最常见的坑**——识别到了 squashfs，但系统里没有 `unsquashfs` → **提取失败**。解决：

```bash
sudo apt install squashfs-tools
# 相关解压工具全家桶
sudo apt install p7zip-full xz-utils lzma cpio unzip tar
```

```bash
# ④ 重新提取
sudo binwalk -e -M -C /evidence/fw firmware.bin
ls -la /evidence/fw/
```

```console
_evidence/fw/_firmware.bin.extracted/
   5CE0.xz
   5CE0/
   ...
```

```bash
ls -R /evidence/fw/_firmware.bin.extracted/ | head -20
```

```console
/evidence/fw/_firmware.bin.extracted/:
5CE0  5CE0.xz  squashfs-root

/evidence/fw/_firmware.bin.extracted/squashfs-root:
bin  dev  etc  lib  mnt  proc  root  sbin  sys  tmp  usr  var  www
```

**解读**：**拿到 `squashfs-root/` 就等于拿到了固件的完整文件系统**。后续可以做：

```bash
# 看版本、找凭据、找硬编码密钥（这些是固件分析的核心目标）
cat /evidence/fw/_firmware.bin.extracted/squashfs-root/etc/banner 2>/dev/null
sudo grep -rIl 'root:' /evidence/fw/_firmware.bin.extracted/squashfs-root/etc/ 2>/dev/null
sudo grep -rIn 'password\|passwd\|secret\|API_KEY' \
   /evidence/fw/_firmware.bin.extracted/squashfs-root/etc/ 2>/dev/null | head
```

```console
/etc/passwd:root:x:0:0:root:/root:/bin/sh
/etc/shadow:root:$1$abcdefgh$...:0:0:99999:7:::
```

```bash
# 找「不该有的东西」：调试接口、后门账号、私钥
sudo find /evidence/fw/_firmware.bin.extracted/squashfs-root -name '*.pem' -o -name 'id_rsa*' 2>/dev/null
sudo grep -rIn 'telnetd\|dropbear' /evidence/fw/_firmware.bin.extracted/squashfs-root/etc/init.d/ 2>/dev/null
```

**解读**：固件分析的经典产出就是这三类：**默认/硬编码凭据、调试后门、私钥与证书**。

### 场景 2：定位「被加密/压缩的区域」——熵分析的威力

```bash
# ① 先看熵图（保存 PNG 用于报告）
binwalk -E -J -Q firmware.bin
ls -l firmware.bin.png
```

```bash
# ② 只看数值（不画图），快速定位高低熵边界
binwalk -E -N firmware.bin | head -20
```

```console
DECIMAL       HEXADECIMAL     ENTROPY
--------------------------------------------------------------------------------
0             0x0             0.201
16384         0x4000          0.184
32768         0x8000          0.995      ← 高熵起始
...
```

**解读（熵图怎么读）**：

```
1.0 ┤                    ████████████████████          ████████
    │                    ████████████████████          ████████
0.9 ┤                    ████████████████████          ████████
0.7 ┤        ▄▄▄▄▄       ████████████████████   ▄▄▄▄   ████████
0.5 ┤  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ████████████████████ ▄▄▄▄▄▄▄  ████████
0.0 ┤                    ████████████████████          ████████  ▄▄▄▄▄▄
    └─────────────────────────────────────────────────────────────
      固件头+内核        xz 压缩区（内核/根fs）        加密区？
```

| 熵值区间 | 含义 | 行动 |
|----------|------|------|
| **≈0.0** | 全零/填充 | 未使用区域、擦除块 → 一般无信息（但可能有残留碎片） |
| **0.5–0.8** | 代码/文本/结构化数据 | 可以静态分析 |
| **≥0.95** | **压缩或加密** | 尝试提取解压；若是加密则需密钥 |

```bash
# ③ 用阈值标记高低熵边界（默认 0.95/0.85）
binwalk -E -N -H 0.99 -L 0.90 firmware.bin | awk 'NR>2' | head -30
```

**解读**：**一片持续 0.99+ 且无法解压的区域 = 加密数据**。在报告里这是一条硬结论：「偏移 `X` 至 `Y` 为高熵不可解析数据，疑似加密；无密钥无法进一步分析」。**这本身就是有价值的取证结论**（说明「此处存在刻意保护的数据」）。

```bash
# ④ 裸压缩流（没有 gzip/xz 头的，很常见）
binwalk -X firmware.bin           # 裸 deflate
binwalk -Z firmware.bin           # 裸 LZMA
```

```console
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zlib compressed data, default compression
1048576       0x100000        LZMA compressed data, properties: 0x5D, ...
```

### 场景 3：对比两个固件版本 + 与逆向工具衔接

**3a. 找「厂商在新版本里改了什么」（挖 0day 的经典手法）**

```bash
# 准备：拿到同一设备两个版本的官方固件
ls -lh fw_v1.0.bin fw_v2.0.bin
```

```bash
# 逐字节对比（-W hexdump，-i/--red 只看不同的字节）
binwalk -W -i fw_v1.0.bin fw_v2.0.bin -f /evidence/diff.log
head -30 /evidence/diff.log
```

```console
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
00000000      00000000        00 00 00 00  00 00 00 00  |........|
00001000      00001000        FF FF FF FF  00 00 00 00  |ÿÿÿÿ....|     ← 变化的字节
...
```

```bash
# 只看「所有文件都相同」的部分（找共同基线）
binwalk -W -G fw_v1.0.bin fw_v2.0.bin | head
```

**解读**：**版本 diff 的意义**——安全补丁会体现在「某段代码被改动」上。**差异集中的位置往往就是新修的漏洞所在**（如果你在做「授权范围内的漏洞研究」，这是最有效的方向之一）。

**3b. 判断固件的 CPU 架构（决定后续用什么逆向工具）**

```bash
binwalk -Y -T 200 firmware.bin | head -20
```

```console
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
92            0x5C            ARM executable code, 32-bit (little-endian), ...
```

```bash
# 与 file/其他工具交叉验证
file /evidence/fw/_firmware.bin.extracted/squashfs-root/bin/busybox
readelf -h /evidence/fw/_firmware.bin.extracted/squashfs-root/bin/busybox | head -12
```

```console
ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, ...
```

**解读**：架构确认后就可以交给 [`../10-逆向工程/radare2.md`](../10-逆向工程/radare2.md) 或 [`../10-逆向工程/ghidra.md`](../10-逆向工程/ghidra.md) 做反汇编。**binwalk 定位于「结构」，不做深度反编译**。

**3c. 与其它取证工具串联**

```bash
# 对提取出的文件系统再做一轮「特征与凭据」扫描
bulk_extractor -o /evidence/bulk-fw -R /evidence/fw/_firmware.bin.extracted/ -j 8
head -10 /evidence/bulk-fw/email.txt
```

```bash
# 对提取出的证书/私钥文件看元数据与有效期
exiftool /evidence/fw/_firmware.bin.extracted/squashfs-root/etc/*.pem 2>/dev/null | head -20
```

```bash
# 把结构清单写进报告
binwalk -B -f /evidence/fw_structure.log firmware.bin
cat /evidence/fw_structure.log
```

见 [`bulk-extractor.md`](bulk-extractor.md)、[`exiftool.md`](exiftool.md)。

---

## 6. 输出解读

### 6.1 签名扫描输出

| 字段 | 含义 | 报告/分析价值 |
|------|------|---------------|
| `DECIMAL` | 十进制偏移 | 定位、切片（`-D`/`dd`） |
| `HEXADECIMAL` | 十六进制偏移 | 与逆向工具地址对照 |
| `DESCRIPTION` | 命中的签名描述 | **核心情报**：格式、架构、压缩方式、大小、时间 |

**高价值描述关键词**：

| 描述里出现 | 含义 | 行动 |
|------------|------|------|
| `uImage` / `TRX` / `UBI` / `UBIFS` / `JFFS2` | 固件/文件系统格式 | 用对应工具解（`ubireader`、`jefferson`…） |
| `CPU: ARM/MIPS/x86` | 目标架构 | 选对应逆向工具链 |
| `xz/gzip/LZMA/Zlib compressed data` | 压缩区 | 提取解压 |
| `squashfs` / `cramfs` | 只读根文件系统 | `unsquashfs` |
| `device tree` / `dtb` | 硬件描述 | 分析硬件配置 |
| `certificate` / `private key` | **证书 / 私钥** | **立刻记录（凭据泄露）** |
| `PNG/JPEG` | 图片（可能是 logo/界面） | —— |

### 6.2 提取产物结构

```
_<原文件名>.extracted/
  ├─ <偏移16进制>            ← 按偏移命名的提取结果
  ├─ <偏移16进制>.<扩展名>    ← 原始切片（如 5CE0.xz）
  └─ squashfs-root/         ← 解开的根文件系统（如果有）
```

### 6.3 熵图与阈值

| 阈值参数 | 默认 | 含义 |
|----------|------|------|
| `-H`（high） | 0.95 | **上升沿**：从这个熵值以上认为「进入高熵区」 |
| `-L`（low） | 0.85 | **下降沿**：低于此值认为「离开高熵区」 |

**报告写法**：「偏移 0x5B88–0x300000 为持续高熵区（熵值 0.99），经 xz 解压后得到根文件系统；偏移 0x30001C 起为高熵区且所有已知压缩工具均无法解析，判定为加密数据。」

---

## 7. 与其他工具配合

```
① 获取固件（官方下载 / 自有设备 dump）
        │
② binwalk -B ──► 结构地图（偏移 / 类型 / 架构）
        │
        ├─► binwalk -E -J ──► 熵图：定位压缩/加密区（报告配图）
        │
        ├─► binwalk -e -M ──► 提取 + 递归拆套娃 → squashfs-root/
        │        │
        │        ├─► grep 凭据/密钥/后门 → 凭据泄露结论
        │        ├─► bulk-extractor -R ──► 特征与凭据（bulk-extractor.md）
        │        ├─► exiftool ──► 证书/图片元数据（exiftool.md）
        │        ├─► radare2 / ghidra ──► 二进制深度逆向（../10-逆向工程/）
        │        └─► 文件系统分析：sleuthkit（sleuthkit.md）
        │
        ├─► binwalk -W -i ──► 两版本 diff（找补丁/漏洞位置）
        │
        └─► binwalk -X / -Z ──► 裸压缩流（无头的 deflate/LZMA）
                        │
                 无法解压 → 判定为加密数据（写进报告）
```

- 二进制深度逆向：[`../10-逆向工程/radare2.md`](../10-逆向工程/radare2.md)、[`../10-逆向工程/ghidra.md`](../10-逆向工程/ghidra.md)
- 文件系统分析（提取出的镜像）：[`sleuthkit.md`](sleuthkit.md)
- 特征与凭据提取：[`bulk-extractor.md`](bulk-extractor.md) ｜ 元数据：[`exiftool.md`](exiftool.md)
- 雕刻（无结构时的兜底）：[`foremost.md`](foremost.md)、[`scalpel.md`](scalpel.md) ｜ 获取：[`dcfldd.md`](dcfldd.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `Extractor.execute failed ... unsquashfs: No such file or directory` | **缺解压工具（最常见）** | `sudo apt install squashfs-tools p7zip-full xz-utils lzma cpio` |
| 只识别不提取 | 没加 `-e`；或缺对应解压器 | 加 `-e -M`；补装工具 |
| 提取结果里没有根文件系统 | 多层嵌套只拆了一层 | 加 `-M`；或手动对 `<偏移>.xz` 再跑一遍 binwalk |
| 提取出巨量垃圾文件 | 假头 + 无大小限制 | `-j <size>` 限大小、`-n <count>` 限数量、`-y <str>` 只提取关心的类型 |
| 输出太多看不清 | 满屏假阳性（如大量 `gzip`） | `-x gzip` 排除；或 `-y squashfs` 只看关心的 |
| 高熵区解不开 | **加密数据** | 无密钥不可解；**在报告中如实写为「疑似加密数据」** |
| `-i` 效果不对 | `-i` 在对比组里是 `--red`（不是 include） | 想只显示某类型用 **`-y`** |
| 熵图为空/很平 | 文件太小或块太大 | 小文件熵分析意义有限；调块大小 `-K` |
| 递归到很深的层次 | `-d` 默认 8 | `-d 4` 限制；注意磁盘空间 |
| 磁盘被写满 | `-M` + `-e` 产生大量中间文件 | 加 `-r`（提取后删中间切片）；或输出到独立大盘 |
| 以 root 运行解压工具的风险 | binwalk 会调用外部解压器处理**不可信数据** | 用 `-0 <user>` 以低权用户运行解压；在隔离虚拟机里分析专用固件 |
| 符号链接攻击 | `-1` 不清理指向外部的软链 | **不要开 `-1`**（默认是安全的） |
| 命令与网上教程不一致 | 网上多是 v2 参数，v3 已变更 | 确认 `binwalk -h` 的版本；v2.x 已 EOL |

---

## 9. 防御视角（蓝队 / 设备安全）

binwalk 对蓝队/设备安全的用途，主要在**固件安全评估**与**供应链/设备取证**：

| 场景 | 用法 | 价值 |
|------|------|------|
| 设备安全评估 | 拆厂商固件，找**默认口令、硬编码密钥、调试后门** | 输出可直接落地的整改项（别把 telnet 后门留在出厂固件里） |
| 供应链检查 | 对采购设备固件做「结构 + 凭据」扫描 | 发现「预装后门/调试接口」 |
| 物联网资产梳理 | `-B` 确认固件格式与架构 | 规划固件升级与漏洞管理 |
| 固件版本比对 | `-W -i` 对比两个版本 | 确认「厂商是否真的修了那个洞」（验证补丁有效性） |
| 加密判断 | `-E` 熵分析 | 确认「是否存在未公开的加密数据/私有协议」 |
| 事件取证 | 对可疑 `.bin`/固件做结构分析 | 判断是不是工具、是否含恶意载荷 |
| 报告配图 | `-E -J` 保存熵图 PNG | 直观展示「压缩区/加密区/代码区」的分布 |

**设备/固件安全的三条硬建议**：

1. **不发布含调试接口的固件**：telnetd、串口 shell、隐藏账号是 IoT 事故的第一大原因；
2. **不硬编码凭据与私钥**：固件一旦公开（很多厂商官网可下载），等于把凭据交给了所有人（**binwalk 就是验证这一点最快的工具**）；
3. **敏感数据必须加密且密钥不可在固件中**：否则熵图能定位、提取能解开——**「内有加密」不等于「安全」**。

**应急响应中的注意点**：分析**来源不明**的固件/二进制时，**务必在隔离虚拟机中进行**，并用 `-0` 以低权用户执行解压（历史上出现过「恶意文件名/符号链接攻击解压器」的案例）。

---

## 10. 参考

- binwalk 官方仓库（含 v2/v3 说明）：<https://github.com/ReFirmLabs/binwalk>
- Kali 工具页：<https://www.kali.org/tools/binwalk/>
- 本地命令：`binwalk -h`、`man binwalk`
- 固件分析相关：OpenWrt / DD-WRT 官网（获取**开源固件**做练习）、`firmware-mod-kit`（Kali 工具清单中）
- 经典学习样本：DD-WRT 官方发布固件（Kali 官方文档示例使用的即是此类公开固件）
- 深度逆向工具：[`../10-逆向工程/radare2.md`](../10-逆向工程/radare2.md)、[`../10-逆向工程/ghidra.md`](../10-逆向工程/ghidra.md)

## ⚠️ 法律与伦理

固件可能包含**厂商的专有代码、第三方版权组件、以及硬编码的凭据与私钥**。分析行为可能涉及：

- **著作权与许可**：许多固件 EULA 明确禁止逆向工程；分析前**必须先确认许可条款**（开源固件如 OpenWrt/DD-WRT 通常允许）；
- 《著作权法》相关规定（规避技术措施、复制与改编）；
- 若固件中包含**用户凭据、证书私钥**，还涉及《个人信息保护法》《数据安全法》；
- 若将提取出的**凭据/私钥用于访问**相关设备或服务，则可能触犯《刑法》第 285 条（非法侵入/非法获取计算机信息系统数据）。

**必须遵守**：

1. **只分析你有权分析的对象**：自有设备固件、开源固件、明确授权的研究目标（如厂商漏洞赏金计划范围内的固件）；
2. **先读 EULA/许可**，不确定就不要分析；
3. **发现的凭据/私钥不得用于访问任何系统**，应通过**厂商漏洞披露流程**上报；
4. **隔离环境分析**：来源不明的固件在一次性虚拟机中处理（用 `-0` 降低解压器提权风险）；
5. **报告脱敏**：不公开可直接利用的后门细节与完整凭据（遵循负责任的漏洞披露）；
6. **数据销毁**：结案后清理提取产物与中间文件。
