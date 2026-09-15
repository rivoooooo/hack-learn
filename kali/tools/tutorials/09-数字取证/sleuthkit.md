# The Sleuth Kit（TSK，文件系统取证命令行套件）

> **一句话**：一套直接「读磁盘镜像内部结构」的命令行工具——列出分区、解析文件系统、按 inode 提取文件与元数据、重建时间线，**不依赖操作系统挂载**。
> **分类**：数字取证 / 文件系统分析 ｜ **Kali 包**：`sleuthkit`（安装后提供 `fls`、`icat`、`mmls`、`fsstat`、`blkls`、`istat`、`ifind`、`tsk_recover`、`mactime`、`hfind`、`img_stat`、`jls` 等）｜ **官方文档**：<https://www.sleuthkit.org/sleuthkit/> ｜ Wiki：<https://wiki.sleuthkit.org/>

---

## 1. 它解决什么问题

拿到镜像后，**不要直接 `mount`**：挂载会修改元数据（`atime`）、触发文件系统日志重放，可能破坏证据；而且挂载**看不到已删除的文件**。

TSK 的工作方式是「**以只读方式解析文件系统数据结构**」，因此它能做到挂载做不到的事：

| 你想知道 | 挂载后能看吗 | TSK 命令 |
|----------|--------------|----------|
| 分区表长什么样、各分区偏移多少 | 只能靠 `fdisk` 猜 | `mmls` |
| 文件系统类型、块大小、inode 数 | 部分 | `fsstat` |
| **已删除文件**的列表 | ❌ 看不到 | `fls -d` |
| 按 inode 号提取文件（**包括已删除**，只要数据块未被覆盖） | ❌ | `icat` |
| 文件的 MAC 时间（修改/访问/变更）与 inode 元数据 | 有限 | `istat`、`tsk_gettimes` |
| 某个数据块属于哪个文件 | ❌ | `ifind -d <block>` |
| 未分配空间中残留的内容 | ❌ | `blkls`（导出未分配空间） |
| 按时间线排列所有文件活动 | ❌ | `mactime`（配 `fls -m`） |
| 批量恢复文件（含删除） | ❌ | `tsk_recover` |

对比同类：

| 工具 | 层 | 说明 |
|------|-----|------|
| **TSK** | 命令行 / 库 | 精确、可脚本化，是 Autopsy 的**底层引擎** |
| **`autopsy`** | 图形界面 | TSK 的 Web 前端（Kali 包为经典浏览器版），见 [`autopsy.md`](autopsy.md) |
| **`foremost` / `scalpel`** | 文件雕刻 | **不解析文件系统**，靠文件头尾「雕刻」；TSK 失败时作为兜底，见 [`foremost.md`](foremost.md) |
| **`bulk-extractor`** | 特征提取 | 也不解析文件系统，专扫正则特征，见 [`bulk-extractor.md`](bulk-extractor.md) |
| **`binwalk`** | 嵌入数据 | 面向固件，见 [`binwalk.md`](binwalk.md) |

**关系一句话**：**TSK 解析结构 → 找不到时用雕刻（foremost/scalpel）兜底 → 特征提取（bulk-extractor）补充 → 元数据（exiftool）落地细节。**

---

## 2. 工作原理

### 2.1 磁盘 → 分区 → 文件系统 → inode → 数据块

```
磁盘镜像（raw / E01）
 ├─ 分区表（MBR 512B / GPT 支持）
 │    └─ 分区 1，起始偏移 1 MiB（= 2048 扇区 × 512 B）
 │         └─ 文件系统（NTFS / ext4 / FAT / HFS+ / APFS…）
 │              ├─ 元数据区：inode 表 / MFT（NTFS）
 │              │    └─ 每个 inode/MFT 记录：权限、大小、MAC 时间、数据块指针
 │              ├─ 数据区：数据块（NTFS 叫簇 cluster）
 │              └─ 未分配空间（unallocated）：已删除文件的数据可能还在
 └─ （GPT）备份分区表在磁盘末尾
```

**TSK 命令与这一层的对应关系**：

| 层 | 命令 | 作用 |
|----|------|------|
| 镜像/设备 | `img_stat` | 看镜像格式与大小（是否支持 E01） |
| 分区 | `mmls`、`mmstat`、`mmcat` | 列出/查看/提取分区 |
| 文件系统 | `fsstat` | 类型、块大小、inode 范围、标签 |
| 目录与文件名 | `fls`、`ffind` | 列目录、按名字找 inode |
| inode/MFT | `istat`、`ifind` | 查看元数据、按块/名反查 inode |
| 文件内容 | `icat`、`fcat` | 按 inode 输出内容 |
| 未分配空间 | `blkls`、`blkcat`、`blkstat`、`blkcalc` | 导出/查看/计算块 |
| 时间线 | `tsk_gettimes`、`mactime` | 生成正文时间线 |
| 恢复 | `tsk_recover`、`tsk_comparedir` | 批量恢复、与目录比对 |
| NTFS 专有 | `jls`/`usnjls`（USN 日志）、`fls -e`（ADS） | 日志与备用数据流 |
| 哈希查找 | `hfind` | 与 NSRL 等哈希库批量比对（快速筛掉已知文件） |

### 2.2 关键概念：inode、MAC 时间、时区

- **inode（NTFS 里是 MFT 记录）**：文件的一切元数据都在这里，**文件名不一定属于 inode**（NTFS 中文件名在目录项里，所以一个 inode 可以有多个名字或「孤儿」）。
- **MAC 时间**：`M`odified（内容修改）、`A`ccessed（访问）、`C`hanged（元数据变更，NTFS 里对应 MFT 记录修改）。**NTFS 还有 `B`orn/Created（创建时间）**。做时间线必须区分这四类。
- **时区**：NTFS 存 UTC，很多时间戳展示需要显式指定时区（TSK 用 `-z`）。**忘记时区是时间线分析最常见的致命错误。**

### 2.3 两个模式：`-f`（明确类型）与 `-i`（镜像类型）

- **`-f <fs>`**：明确指出文件系统类型（`ntfs`、`ext4`、`fat`、`hfs`…），跳过自动探测，**更快更准**。
- **`-i <img>`**：镜像格式（`raw` 默认、`ewf` 对应 E01、`aff`、`vmdk`）。分析 E01 必须加 `-i ewf`。
- **`-o <offset>`**：分区起始的**扇区数**（`mmls` 输出的 `Start` 列），几乎所有命令都需要。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install sleuthkit
```

TSK 会自动在 `$PATH` 里提供工具（无需指定路径）：

```bash
command -v fls icat mmls fsstat blkls istat ifind mactime tsk_recover
```

```console
$ fls -h
fls 4.14.0 - List file and directory names in a disk image.

usage: fls [-adDFlhpruvV] [-f fstype] [-i imgtype] [-b dev_sector_size]
           [-o imgoffset] [-P pooltype] [-B pool_volume_block] [-z zone]
           [-s seconds] [-m mount_point] image [images] [inode]
...
```

典型三段式流程：

```bash
# ① 看分区
mmls image.dd
# ② 看文件系统
fsstat -o 2048 image.dd
# ③ 列文件
fls -r -o 2048 -f ext4 image.dd
```

> **一次都不用挂载**，这是取证分析的正确姿势。

---

## 4. 核心参数详解

### 4.1 通用参数（几乎所有 TSK 命令都支持）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-f <fstype>` | 指定文件系统类型 | `ntfs`/`ext4`/`fat`/`hfs`；**显式指定更可靠** |
| `-i <imgtype>` | 镜像格式 | `raw`（默认）、`ewf`（E01）、`aff`、`vmdk` |
| `-b <size>` | 设备扇区大小 | 4Kn 设备需设 4096 |
| `-o <offset>` | 分区起始**扇区数** | 取自 `mmls` 的 `Start` 列；**最常忘的参数** |
| `-P <pooltype>` / `-B` | 存储池（ZFS/btrfs 等） | 高级场景 |
| `-z <zone>` | **时区**（如 `UTC`、`CST6CDT`、`Asia/Shanghai`） | 时间线分析必设；不设会得到偏移错误的时间 |
| `-s <seconds>` | 时间偏移补偿 | 处理已知的时间偏差 |
| `-v` / `-V` | 详细输出 / 版本 | 排错 |

### 4.2 `fls`（列目录，最常用）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-r` | 递归 | 全盘列表 |
| `-l` | **长格式**（含 MAC 时间与大小） | 做时间线必用 |
| `-m <挂载点>` | **正文格式**（配合 `mactime`） | 如 `-m /`；生成时间线输入 |
| `-d` | 只显示**已删除**条目 | 找被删文件 |
| `-D` | 只显示**目录** | 快速看结构 |
| `-F` | 只显示**文件** | —— |
| `-a` | 显示 `.` 与 `..` | —— |
| `-p` | 显示全路径 | 便于人读 |
| `-u` | 显示未分配的 inode（**孤儿文件**） | NTFS 中「文件被删但 MFT 记录还在」 |
| `-e` | 显示 ADS（备用数据流，NTFS） | 找隐藏数据流 |
| `-h` | 显示 inode 号（人类可读） | 需要 inode 号做 `icat` 时 |
| `-s` | 显示时间戳（**秒精度**，便于脚本） | —— |
| `[inode]` | 只列该 inode 对应目录 | 定向分析 |

### 4.3 `icat`（按 inode 提取）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `image inode` | 输出该 inode 的内容到 stdout | 重定向到文件 |
| `-r` | 恢复文件（**不用稀疏文件语义**，NTFS 上更完整） | NTFS 镜像恢复时加 `-r` |
| `-h` | 显示 inode 号（辅助） | —— |
| `-s` | 只输出稀疏文件的已分配区域 | 特殊场景 |

### 4.4 其它高频命令的关键参数

| 命令 | 关键参数 | 说明 |
|------|----------|------|
| `mmls` | `-a`（含未分配）、`-t`（显示 DOS 分区类型表）、`-B`、`-r`（递归到 DOS 子分区） | `Start` 列即 `-o` 的值（**注意 mmls 的偏移单位也是扇区**） |
| `fsstat` | `-t`（统计信息） | 看块大小、inode 范围、是否为 NTFS |
| `blkls` | `-A`（只输出未分配块）、`-e`（输出所有块）、`-s`（稀疏） | `blkls -A` 是「导出未分配空间」的标准做法 |
| `blkcat` | `image block [num]` | 输出指定块内容 |
| `blkstat` | `image block` | 看某块是否已分配 |
| `istat` | `image inode` | 查看 inode 全部元数据（时间、权限、数据块指针、ADS） |
| `ifind` | `-d <block>`（按数据块）、`-n <name>`（按名）、`-p <path>`（按路径） | 反查 inode |
| `ffind` | `-d <dir_inode> <name>` | 按名字在目录中找 inode |
| `tsk_recover` | `-e`（含已删除）、`-a`（所有文件）、`-d <dir>`、`-o <offset>` | 批量恢复 |
| `tsk_gettimes` | `-m`、`-z` | 替代 `fls -m`，生成正文时间线输入 |
| `mactime` | `-b <body>`、`-d`（CSV）、`-z`、`-i day\|hour`、`-y`（年） | 生成人类可读时间线 |
| `hfind` | `-f <hashdb>`、`-i`、`-q` | 与 NSRL 哈希库比对（筛掉已知无害文件） |
| `img_stat` | `image` | 确认镜像格式（是否 E01 等） |
| `jls` | `-o <offset> image inode` | 读 NTFS $LogFile 记录（**取证金矿**） |
| `usnjls` | 同上 | 读 USN 变更日志（记录文件增删改的日志） |
| `sigfind` | `-o <offset> -t <hex>` | 按签名搜索（如 `-t 55AA` 找引导扇区） |

---

## 5. 实战演练

> **环境声明**：以下使用**自建实验镜像**（按 [`dcfldd.md` 场景 1](dcfldd.md#场景-1造一个作案现场先有可练的镜像) 的方法生成）或**公开取证样本**（NIST CFReDS <https://cfreds.nist.gov/>）。
> **禁止**对未经授权的真实设备执行镜像获取或分析。分析阶段一律在**镜像副本**上进行，原始镜像封存。

### 场景 1：从「一个 .dd 文件」到「文件清单」

```bash
# ① 确认镜像格式与分区结构
img_stat /evidence/disk.img
mmls /evidence/disk.img
```

```console
GUID Partition Table (EFI)
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Safety Table
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  Meta      0000000001   0000000001   0000000001   GPT Header
003:  Meta      0000000002   0000000033   0000000032   Partition Table
004:  00        0000002048   000000524287   000000522240   Linux filesystem
```

**解读**：`004: 00` 分区的 `Start = 2048`（扇区）。**这个数字就是后续所有命令的 `-o 2048`**。这是 TSK 使用中最关键的一步。

```bash
# ② 文件系统概览
fsstat -o 2048 /evidence/disk.img | head -25
```

```console
FILE SYSTEM INFORMATION
--------------------------------------------
File System Type: Ext4
Block Size: 4096
Block Range: 0 - 65279
Inode Range: 1 - 16384
Root Directory: 2
...
```

```bash
# ③ 列根目录（先不加 -r，看结构）
fls -o 2048 /evidence/disk.img
```

```console
r/r 2:	.
r/r 2:	..
d/d 11:	lost+found
r/r 12:	secret.txt
r/r 13:	photo.jpg
r/r 14:	report.pdf
```

```bash
# ④ 递归 + 长格式（含时间与大小）
fls -r -l -o 2048 /evidence/disk.img > /evidence/fls_out.txt
head -20 /evidence/fls_out.txt
```

```console
r/r 12:	secret.txt	2024-09-14 10:12:03 (CST)	2024-09-14 10:12:03 (CST)	2024-09-14 10:12:03 (CST)	20	0	0
r/r 13:	photo.jpg	2024-09-14 10:12:41 (CST)	...
```

```bash
# ⑤ 按 inode 提取内容（icat 是「读 inode」而不是「按路径读文件」）
icat -o 2048 /evidence/disk.img 12
```

```console
password=LabSecret123
```

**解读**：这就是 TSK 的威力——**你根本没挂载这个镜像**，却直接读出了文件内容。用 `icat > out.txt` 把内容落到工作目录：

```bash
mkdir -p /evidence/out
icat -o 2048 /evidence/disk.img 13 > /evidence/out/photo.jpg
file /evidence/out/photo.jpg
```

```console
/evidence/out/photo.jpg: PNG image data, 240 x 240, 8-bit/color RGBA, non-interlaced
```

**注意**：`file` 说是 PNG（因为源文件其实是 png 改名成 jpg），这本身就是一条**有价值的勘察结论**（扩展名与真实类型不符）。

### 场景 2：恢复已删除文件（TSK 真正不可替代的能力）

```bash
# ① 列出已删除条目
fls -d -r -l -o 2048 /evidence/disk.img
```

```console
r/r * 15:	deleted_secret.txt	2024-09-14 10:13:00 (CST)	...	128	0	0
d/d * 16:	deleted_dir
```

**解读**：**`*` 号表示「已删除但元数据仍在」**（`fls -d` 的标记）。`15` 是 inode 号。

```bash
# ② 看这个 inode 的元数据（判断数据块是否还在）
istat -o 2048 /evidence/disk.img 15
```

```console
inode: 15
Allocated
Group: 0
Generation Id: 1651620213
uid / gid: 0 / 0
mode: rrw-r--r--
size: 128
num of links: 0
Inode Times:
Accessed:	2024-09-14 10:13:00.123456 (CST)
File Modified:	2024-09-14 10:13:00.123456 (CST)
Inode Modified:	2024-09-14 10:13:05.000000 (CST)
Deleted:	2024-09-14 10:13:05.000000 (CST)
Direct Blocks:
4417 0 0 0 0 0 0 0 0 0 0 0
```

**解读（逐项）**：

| 字段 | 含义 | 判断 |
|------|------|------|
| `num of links: 0` | 链接数为 0 → **确实是已删除** | —— |
| `Deleted: <时间>` | 删除时间（ext4 有记录） | **时间线关键证据** |
| `Direct Blocks: 4417 ...` | 数据块指针还在 → **内容可能未覆盖** | 好消息，可以恢复 |

```bash
# ③ 提取已删除文件内容
icat -o 2048 /evidence/disk.img 15
```

```console
employee_id=1024
salary=185000
```

```bash
# ④ 批量恢复（保留目录结构；-e 包含已删除）
tsk_recover -e -o 2048 /evidence/disk.img /evidence/recovered
find /evidence/recovered -type f | head
```

```console
/evidence/recovered/secret.txt
/evidence/recovered/photo.jpg
/evidence/recovered/report.pdf
/evidence/recovered/$OrphanFiles/deleted_secret.txt      ← 孤儿文件（已删除）进这里
```

**解读**：`tsk_recover -e` 会把已删除文件放进 `$OrphanFiles/` 目录。**这是「恢复文件」的标准操作**——比手工 `icat` 每个 inode 高效得多。

```bash
# ⑤ 如果数据块已被覆盖，icat 会失败 → 转用文件雕刻兜底
icat -o 2048 /evidence/disk.img 15 > /tmp/x 2>/dev/null || echo "块已覆盖"
```

```bash
# 导出未分配空间，再交给 foremost/scalpel 雕刻（见 foremost.md / scalpel.md）
blkls -A -o 2048 /evidence/disk.img > /evidence/unallocated.bin
ls -lh /evidence/unallocated.bin
```

```console
-rw-r--r-- 1 root root 96M /evidence/unallocated.bin
```

**解读**：`blkls -A` 导出**所有未分配块**——已删除文件的数据就藏在这里。这是雕刻工具的**理想输入**（比雕刻整盘快得多，噪音也小）。

### 场景 3：正文时间线（mactime）与 NTFS 日志

```bash
# ① 生成正文格式（-m 指定挂载点，作为路径前缀）
fls -r -m / -o 2048 /evidence/disk.img > /evidence/bodyfile.txt
wc -l /evidence/bodyfile.txt
```

```console
42 /evidence/bodyfile.txt
```

```bash
# ② 生成人类可读时间线（务必带时区）
mactime -b /evidence/bodyfile.txt -z CST6CDT -d > /evidence/timeline.csv
head -5 /evidence/timeline.csv
```

```console
Date,Size,Type,Mode,UID,GID,Meta,File Name
Sat Sep 14 2024 10:12:03,20,macb,rrw-r--r--,0,0,12,/secret.txt
Sat Sep 14 2024 10:12:41,4096,macb,rrw-r--r--,0,0,13,/photo.jpg
Sat Sep 14 2024 10:13:00,128,.a.b,rrw-r--r--,0,0,15,(deleted) /deleted_secret.txt
Sat Sep 14 2024 10:13:05,128,..c.,rrw-r--r--,0,0,15,(deleted) /deleted_secret.txt
```

**解读（这是取证分析的核心产出）**：

| 列 | 含义 | 怎么读 |
|----|------|--------|
| `Date` | 事件时间 | 按时间排序看「谁先谁后」 |
| `macb` 四个字母 | **M**odified/**A**ccessed/**C**hanged/**B**orn（创建） | 哪位有字母说明该时间等于此行时间 |
| `.a.b` | 只有 Accessed 与 Born | 出现在**访问**行 |
| `..c.` | 只有 Changed | 元数据变更行 |
| `(deleted)` | 该条目已删除 | 关键证据 |
| `Meta`（inode） | 关联到 inode，便于回查 | 用 `istat` 看详情 |

**据此可写出结论**：`photo.jpg` 在 10:12:41 创建 → `deleted_secret.txt` 在 10:13:00 被创建、10:13:05 被删除。**时间线就是「还原发生了什么」的骨架**。

```bash
# ③ NTFS 场景：读 USN 日志与 $LogFile（文件增删改的完整审计）
fls -o 2048 -f ntfs image.dd                      # 先确认是 NTFS
usnjls -o 2048 image.dd 6 | head -40              # inode 6 = $Extend/$UsnJrnl
jls -o 2048 image.dd 8 | head -40                 # inode 8 = $LogFile
```

**解读**：NTFS 的 `$UsnJrnl`/`$LogFile` 记录了**文件系统层面的每一次变更**（重命名、删除、移动）。**攻击者删除工具、清理痕迹的动作往往在这里留痕**——这是「反取证对抗」的关键取证点。

```bash
# ④ 用哈希库快速筛掉已知无害文件（NSRL）
hfind -i nsrl-md5 /usr/share/hashsets/NSRL 2>/dev/null || echo "需先准备 NSRL 哈希库"
```

```bash
# ⑤ 查看备用数据流（ADS，隐藏数据常见藏身处）
fls -r -e -o 2048 -f ntfs image.dd | grep ':'
```

---

## 6. 输出解读

### 6.1 `mmls` 输出

| 字段 | 含义 | 用途 |
|------|------|------|
| `Slot` | 分区槽位 | —— |
| `Start` | **起始扇区号** | **就是 `-o` 的值** |
| `End` / `Length` | 结束扇区 / 扇区数 | 计算分区大小 |
| `Description` | 分区类型 | 判断哪个是数据分区 |
| `Meta`（分区表/GPT 头） | 元数据区域 | 分析分区表篡改时会用到 |

### 6.2 `fls -l` 输出

| 列 | 含义 |
|----|------|
| `r/r` / `d/d` | **条目类型/元数据类型**：`r`=常规文件、`d`=目录、`v/v`=虚拟、`l/l`=符号链接 |
| `*` | **已删除**（`-d` 标记） |
| `<inode>` | inode 号（`icat` 的输入） |
| 名称 | 文件名（带 `(deleted)` 的是删除条目） |
| 三组时间 | 通常是 **M / A / C**（顺序以 man 为准，建议显式用 `-m` + `mactime` 避免歧义） |
| 大小 | 字节数（**NTFS 上可能显示为已分配大小**） |

### 6.3 `istat` 输出（取证价值最高的单条输出）

| 字段 | 含义 | 判断要点 |
|------|------|----------|
| `Allocated` / `Not Allocated` | inode 是否还被使用 | `Not Allocated` + `num of links: 0` = 已删除 |
| `num of links` | 硬链接数 | 0 → 已删除 |
| `size` | 逻辑大小 | 与实际恢复出的字节数比对（不一致=被截断/覆盖） |
| `Accessed/File Modified/Inode Modified/Deleted` | **四个时间** | 时间线核心 |
| `Direct Blocks` | 数据块指针 | 指针还在 = 数据可能还在 |
| `uid/gid/mode` | 所有者与权限 | 关联到「谁创建了它」 |

### 6.4 成功判据

- `filenames in == filenames out`（`fls -m` 与 `mactime -b` 的条目数一致）；
- `icat` 输出的字节数与 `istat` 的 `size` 一致；
- 恢复出的文件能被 `file` 正确识别（类型与扩展名可交叉验证）；
- 时间线单调合理（没有「未来时间」等矛盾——出现时说明**时区或时钟被篡改**，本身是重要发现）。

---

## 7. 与其他工具配合

```
镜像（dcfldd / ddrescue / E01）
   │
   ├─ mmls ──► 分区偏移（-o）───┐
   │                            ▼
   ├─ fsstat ──► 文件系统类型/块大小
   │
   ├─ fls -r -m ──► bodyfile ──► mactime ──► 时间线（报告主线）
   │      └─ -d ──► 已删除条目 ──► istat ──► icat → 恢复文件
   │                                   └─ 失败 ──► blkls -A（未分配空间）
   │                                                     │
   │                          foremost / scalpel ◄───────┘   （雕刻兜底）
   │
   ├─ bulk-extractor ──► 邮箱/IP/URL/卡号等特征（不依赖文件系统）
   ├─ binwalk ──► 嵌入式固件镜像
   └─ exiftool ──► 恢复出的图片/文档 → 拍摄设备、时间、GPS
                        │
                        ▼
                 autopsy（图形化复现同一套结论）
```

- 获取镜像：[`dcfldd.md`](dcfldd.md)
- 图形界面（TSK 的前端）：[`autopsy.md`](autopsy.md)
- 特征提取：[`bulk-extractor.md`](bulk-extractor.md)
- 文件雕刻：[`foremost.md`](foremost.md)、[`scalpel.md`](scalpel.md)
- 固件/嵌入数据：[`binwalk.md`](binwalk.md)
- 元数据：[`exiftool.md`](exiftool.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `Cannot determine file system type` | 没给 `-f`，自动探测失败 | 显式 `-f ext4`/`-f ntfs`；或用 `fsstat` 先确认 |
| `Invalid magic value (not a disk image)` | **`-o` 偏移错**（最最常见的坑） | 用 `mmls` 拿到正确的 `Start`（单位是**扇区**，不是字节） |
| 结果全乱/文件名乱码 | 文件系统类型猜错 | 明确 `-f`；确认分区是否加密（LUKS/BitLocker） |
| E01 镜像报格式错误 | 没指定镜像类型 | 加 `-i ewf`（必要时装 `libewf`） |
| `fls -l` 的时间与预期差几小时 | **时区**未设 | 加 `-z UTC`（或用目标系统时区），并在报告里写明基准 |
| `icat` 输出为空/0 字节 | 数据块已被覆盖或指针已清 | 改用 `blkls -A` 导出未分配空间 + 雕刻（foremost/scalpel） |
| 恢复出的文件打不开 | 内容被部分覆盖（稀疏/碎片） | 用 `icat -r`（NTFS 更完整）；或按 `istat` 的块指针手工 `blkcat` 拼接 |
| 全盘文件系统加密 | LUKS/BitLocker/FileVault | TSK 无法直接解析；需先解密（合法取得的密钥/恢复密钥） |
| `tsk_recover` 恢复出巨量垃圾 | 未过滤 | 先 `fls` 定向分析，或用哈希库（NSRL）过滤已知文件 |
| 分区表显示多个可疑分区 | 分区表被篡改/隐藏分区 | 用 `mmls -a` 看未分配区；`sigfind -t 55AA` 找隐藏引导扇区；必要时 `blkls` 全盘雕刻 |
| 时间线出现「未来时间」 | 系统时钟被篡改/时区错 | 这本身是**重要发现**（反取证迹象），要交叉验证其他证据 |
| NTFS 上文件名与 inode 对不上 | 文件名在目录项，inode 可能成孤儿 | 用 `fls -u`（未分配 inode）找孤儿；`icat` 内容仍可读 |
| 命令跑得非常慢 | 全盘 `-r` + 大镜像 | 先定位目录/inode 再定向；必要时只 `blkls -A` 到 SSD 上处理 |

---

## 9. 防御视角（蓝队 / 应急响应）

TSK 在蓝队手里有两个用途：**事件响应取证** 与 **攻击痕迹验证**。

| 场景 | TSK 的用法 | 关注点 |
|------|------------|--------|
| 入侵后取证 | 对镜像做 `fls -r -m` + `mactime` | 建立「首次落地时间 / 工具上传时间 / 数据外带时间」的时间线 |
| 找攻击者留下的工具 | `fls -d`（已删除）+ `tsk_recover -e` | 攻击者删除的 exp、隧道工具、webshell 常能被恢复 |
| 找 webshell | `fls -r` 看 Web 目录新增/修改时间异常的文件 | 与发布记录比对 |
| 验证「是否清日志」 | `fls` 看 `/var/log/*` 的大小与时间；`istat` 看是否被截断（size 变小） | 日志被截断/删除 = 反取证证据 |
| **NTFS 变更审计** | `usnjls` / `jls` | 记录文件的增删改重命名，是攻击者最难清理的痕迹之一 |
| 数据泄露取证 | `fls -e`（ADS）+ 恢复的压缩包 | 打包外带的数据往往能从时间线识别 |
| 云/虚拟机场景 | TSK 支持 VMDK（`-i vmdk`） | 虚拟机镜像直接分析，无需启动 |
| 基线对比 | `tsk_comparedir` 与已知良好副本比对 | 快速定位被改动的文件 |

**给蓝队的实操建议**：

1. **把 `mmls` + `fsstat` + `fls -r -m` + `mactime` 做成固定脚本**，事件响应时一键跑出时间线；
2. **保留一份「已知良好」的文件清单/哈希库**（如 NSRL），用 `hfind` 快速筛选异常文件；
3. **不要依赖被入侵系统上的工具**（`ls`/`find` 可能被替换为 rootkit），**离线用 TSK 分析是更可信的路径**；
4. 关注 **`Deleted:` 时间**、**日志文件 size 突变**、**空白时间窗**——这些往往是攻击者活动的边界。

---

## 10. 参考

- The Sleuth Kit 官网与下载：<https://www.sleuthkit.org/sleuthkit/>
- TSK Wiki（每个命令的手册与技巧）：<https://wiki.sleuthkit.org/>
- Kali 工具页：<https://www.kali.org/tools/sleuthkit/>
- NIST CFReDS 公开取证镜像：<https://cfreds.nist.gov/>
- NIST NSRL 哈希库（用于筛除已知文件）：<https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl>
- 时间线方法：`man mactime`、`man fls`、`man istat`、`man tsk_recover`、`man usnjls`

## ⚠️ 法律与伦理

分析磁盘镜像意味着**读取他人全部数字生活**：文档、照片、聊天、邮件、凭据、位置记录。未经授权的获取或访问可能触犯：

- 《刑法》第 285 条（非法获取计算机信息系统数据）、第 253 条之一（侵犯公民个人信息罪）、第 252 条（侵犯通信自由罪，涉邮件/通信内容时）；
- 《网络安全法》《数据安全法》《个人信息保护法》。

**合法前提**：

1. 手持**设备所有者或司法机关的书面授权**；企业内部调查需有制度依据并履行告知程序；
2. 采集与分析范围**最小必要**，避免浏览与案件无关的私密内容；
3. 数据**加密存储**、限定访问人员、记录访问日志（分析过程本身也要有保管链）；
4. **只读分析**：绝不修改原始镜像；工作副本单独存放；
5. 报告与沟通中**脱敏**，不包含真实个人信息、凭据与私密内容；
6. 结案后按约定**安全销毁**副本。

本教程请仅在**自建实验镜像**或 **NIST CFReDS 公开样本**上练习。
