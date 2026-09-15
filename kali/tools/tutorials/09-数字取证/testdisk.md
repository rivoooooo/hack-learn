# testdisk（分区恢复 / PhotoRec 文件雕刻）

> **一句话**：当分区表被写坏、分区被误删、磁盘变成「未分配」时，用 `TestDisk` 找回分区结构；当文件系统本身已经不可靠时，用它的兄弟工具 `PhotoRec` **绕过文件系统、按文件签名直接从裸扇区里把文件「雕」出来**。
> **分类**：数字取证 / 磁盘与分区恢复 ｜ **Kali 包**：`testdisk`（命令 `testdisk`）、`photorec`（命令 `photorec`、`fidentify`）、`qphotorec`（命令 `qphotorec`）｜ **官方文档**：<https://www.kali.org/tools/testdisk/> ｜ 上游：<https://www.cgsecurity.org>

---

## 1. 它解决什么问题

有一类故障是「数据还在，但操作系统看不见了」：

| 故障 | 具体表现 | 谁来救 |
|------|----------|--------|
| **分区表损坏 / 误删分区** | 磁盘在系统里显示为「未分配」；`lsblk` 里只剩盘符没有分区 | **TestDisk** |
| **引导扇区（boot sector）损坏** | 分区还在，但挂载失败、提示文件系统类型错误 | **TestDisk**（`Advanced` → `Boot`） |
| **文件系统严重损坏** | 分区能识别但 `fsck` 也救不回来 | **PhotoRec**（无视文件系统） |
| **格式化后想恢复** | 文件系统被重建，元数据全丢 | **PhotoRec** |
| **删除文件 / 存储卡照片丢失** | 分区和文件系统都好，只是文件没了 | PhotoRec（或文件系统级的恢复工具） |
| **存储卡/相机卡损坏** | 相机的 DCIM 读不出来 | **PhotoRec**（就是为这个场景设计的） |

**关键差异：TestDisk 恢复「结构」，PhotoRec 恢复「内容」**

```
TestDisk  ──► 修复【分区表 / 引导扇区】──► 分区重新可见 ──► 文件系统级完整恢复
                    （目录结构、文件名都保住）

PhotoRec  ──► 无视分区表与文件系统，扫描【每一个扇区】找文件签名
                    （文件名和目录结构【丢失】，但内容能救回来）
```

**对比同类**：

| 工具 | 层次 | 特点 |
|------|------|------|
| **TestDisk** | **分区表 / 引导扇区** | **结构级恢复**：修好分区后文件名、目录都在；交互式 TUI |
| **PhotoRec**（同包） | **文件签名雕刻（carving）** | **内容级恢复**：无视文件系统；**文件名全丢**；支持格式极多（官方列出 30+ 种） |
| **`foremost` / `scalpel`** | 文件雕刻 | 基于**可配置的签名定义文件**，更灵活；见 [`foremost.md`](foremost.md)、[`scalpel.md`](scalpel.md) |
| **`sleuthkit`（`fls`/`icat`/`tsk_recover`）** | 文件系统取证 | **保留文件名与时间戳**（比雕刻强），但要求文件系统元数据还在。见 [`sleuthkit.md`](sleuthkit.md) |
| **`autopsy`** | 图形化取证平台 | 底层就是 sleuthkit；适合可视化。见 [`autopsy.md`](autopsy.md) |
| **`dcfldd`/`dd`** | 镜像与克隆 | **任何恢复的第一步**：先做镜像，不要在原件上操作。见 [`dcfldd.md`](dcfldd.md) |
| **`gpart` / `gparted`** | 分区工具 | **会写盘**；取证场景应避免 |
| **商业工具**（R-Studio、EaseUS 等） | 综合 | 有图形化和更全的格式支持，但闭源、需付费 |

**选型原则（顺序很重要）**：

```
① 先镜像（dcfldd/dd）         ← 永远的第一步
② 先修结构（TestDisk）        ← 如果分区还能救回来，别急着雕刻
③ 结构救不回来 → 再雕刻（PhotoRec / foremost / scalpel）
④ 如果文件系统元数据还在 → 优先用 sleuthkit（能保留文件名）
```

**为什么顺序不能反**：**雕刻得到的文件没有名字和目录**——能救回 500 张照片但不知道哪张是哪张。**能修结构就修结构**。

---

## 2. 工作原理

### 2.1 TestDisk：在磁盘上「找备份的分区信息」

```
MBR 分区表（512 字节，位于 LBA 0）
┌──────────────────────────────────────────────────────────┐
│ 446 字节 引导代码 │ 分区项×4（每个 16 字节）│ 0x55AA 签名 │
└──────────────────────────────────────────────────────────┘
   ▲                              ▲
   │ 常被误写坏的地方               └─ 每个分区项记录：起始 LBA、大小、类型、启动标志
   │
   │ 但！现代硬盘还有【备份】：
   │   - GPT：主表在 LBA 1，【备份表在磁盘末尾】  ← GPT 损坏时先去读它
   │   - NTFS：分区末尾有【备份引导扇区】
   │   - ext2/3/4：每个块组都有【超级块备份】
   ▼
TestDisk 的工作：
   ① 读主分区表 → 不完整/损坏？
   ② 读【备份】分区表 / 超级块 → 恢复结构
   ③ 都不行 → 【按文件系统特征扫描全盘】，找出所有「看起来像分区开始的地方」
   ④ 把结果列给你 → 你确认后【写回】分区表
```

**TestDisk 三种「找分区」手段**：

| 手段 | 原理 | 速度 | 完整度 |
|------|------|------|--------|
| **读主分区表** | 直接解析 LBA 0/1 | 瞬间 | 表坏了就没结果 |
| **读备份（GPT 在盘尾）** | 读 LBA-1 的 GPT 备份表 | 瞬间 | **表坏但盘尾完好时最有效** |
| **Quick Search** | 扫描分区表**残留**与常见位置 | 快（分钟级） | 一般 |
| **Deeper Search** | **按各文件系统的特征逐扇区扫描**，找每个分区的**引导扇区/超级块** | **慢（可数小时）** | **最完整** |

**这就是为什么官方流程是「先 Quick Search，找不到再 Deeper Search」**——后者可能跑几小时。

### 2.2 PhotoRec：文件签名雕刻（carving）

**雕刻（carving）的全部原理**：

```
在一个没有文件系统的裸块设备上，"文件" 只是【一段特定模式的字节】：

  JPEG 文件通常这样：
      偏移 X:  FF D8 FF E0  ←──── 头部签名（SOI + APP0）
      ...      （图像数据）
      偏移 Y:  FF D9        ←──── 尾部签名（EOI）

  雕刻器的工作就是：
      ① 扫描所有扇区，找头部签名
      ② 从那里开始，一直读到找到【尾部签名】（或读到大小上限）
      ③ 把这段字节写成一个文件：f0000123.jpg

  PDF：
      头：%PDF-
      尾：%%EOF

  ZIP/docx/xlsx：
      头：PK\x03\x04
      尾：中央目录结束记录 PK\x05\x06
```

**关键点**：

| 特性 | 说明 |
|------|------|
| **不依赖文件系统** | 所以**格式化过、文件系统损坏、元数据全丢**都能救 |
| **必须能通过「文件类型识别器」** | PhotoRec 会**再用内部数据库校验**头部，丢弃「只是巧合像签名」的假阳性 |
| **文件名与目录结构丢失** | 只能按格式命名（`f0000123.jpg`） |
| **不能恢复碎片化文件** | 文件被拆成多段时，只能恢复第一段（**这是雕刻的固有局限**） |
| **覆盖是致命的** | 数据一旦被新数据覆盖，**任何工具都救不回来** |

**PhotoRec 支持的文件类型**（官方列出的一部分）：`.au` `.avi/.wav` `.bmp` `.bz2` `.c` `.crw` `.ctg` **FAT 子目录** `.doc` `.dsc` `.html` **`.jpg`** `.mov` `.mp3` `.mpg` `.mrw` `.orf` `.pdf` `.pl` **`.png`** `.raf` `.raw` `.rdc` `.rtf` `.sh` `.tar` `.tiff` `.wma` `.x3f` `.zip`

> **注意两件事**：
> 1. **PhotoRec 也能恢复「FAT 子目录」**——对 FAT 分区，它还能把目录结构恢复一部分（比纯雕刻强）；
> 2. **不支持的类型救不了**（比如专有格式），这时要用 [`foremost.md`](foremost.md) / [`scalpel.md`](scalpel.md) 自定义签名。

**`fidentify` 是什么**：**用 PhotoRec 的同一套数据库来「识别文件类型」**——`file` 命令的替代/补充。

```bash
fidentify /path/to/dir          # 递归识别目录里所有文件的「扩展名」
fidentify +jpg file.bin         # 限定只按 jpg 签名判断
```

### 2.3 ⚠️ 铁律：**永远不要在待恢复的盘上写东西**

```
   ❌ 错误做法（把数据写没了）
   ┌──────────────┐         ┌────────────────────────┐
   │ 待恢复的盘   │◄────────│ 恢复出来的文件写回原盘  │  ← 覆盖掉还没恢复的数据！
   └──────────────┘         └────────────────────────┘

   ✅ 正确做法
   ┌──────────────┐   只读   ┌──────────────┐   镜像   ┌──────────────┐
   │ 原始磁盘     │─────────►│ dcfldd/dd 镜像│─────────►│ 镜像文件      │
   └──────┬───────┘          └──────────────┘          └──────┬───────┘
          │ 立即停止使用原盘                                    │
          │                                                    ▼
          │                                    ┌──────────────────────────┐
          └─ 保持原样做证据 ──►                │ 在【另一块盘】上做恢复     │
                                              └──────────────────────────┘
```

**为什么这是铁律**：

- 雕刻扫描的是**空闲/未分配区域**——**你往里写任何东西都可能覆盖掉待恢复的文件**；
- 恢复出的文件**默认写到当前目录**——如果你 `cd` 到了待恢复的盘，等于一边救一边毁；
- **对磁盘的写入是即时且不可逆的**。

> **kali 上的额外提醒**：**不要用文件管理器自动挂载**待恢复的盘（自动挂载会写日志/刷新超级块/创建 `lost+found`）。**先 `umount`，或从一开始就用只读方式挂载**（`mount -o ro,noload` — `noload` 对 ext 系特别重要，它跳过日志重放，避免改盘）。

---

## 3. 安装与快速上手

```bash
sudo apt install testdisk          # testdisk
sudo apt install photorec          # photorec + fidentify
sudo apt install qphotorec         # PhotoRec 的图形界面
command -v testdisk photorec qphotorec fidentify
```

```console
root@kali:~# command -v testdisk photorec qphotorec fidentify
/usr/sbin/testdisk
/usr/sbin/photorec
/usr/sbin/qphotorec
/usr/sbin/fidentify
```

```bash
testdisk -h
```

```console
root@kali:~# testdisk -h
TestDisk 7.2, Data Recovery Utility, February 2024
Christophe GRENIER <grenier@cgsecurity.org>
https://www.cgsecurity.org

Usage: testdisk [/log] [/debug] [file.dd|file.e01|device]
       testdisk /list  [/log]   [file.dd|file.e01|device]
       testdisk /version

/log          : create a testdisk.log file
/debug        : add debug information
/list         : display current partitions

TestDisk checks and recovers lost partitions
It works with :
- BeFS (BeOS)                           - BSD disklabel (Free/Open/Net BSD)
- CramFS, Compressed File System        - DOS/Windows FAT12, FAT16 and FAT32
- XBox FATX                             - Windows exFAT
- HFS, HFS+, Hierarchical File System   - JFS, IBM's Journaled File System
- Linux btrfs                           - Linux ext2, ext3 and ext4
- Linux GFS2                            - Linux LUKS
- Linux Raid                            - Linux Swap
- LVM, LVM2, Linux Logical Volume Manager    - Netware NSS
- Windows NTFS                          - ReiserFS 3.5, 3.6 and 4
- Sun Solaris i386 disklabel            - UFS and UFS2 (Sun/BSD/...)
- XFS, SGI's Journaled File System      - Wii WBFS
- Sun ZFS
```

```bash
photorec -h
```

```console
root@kali:~# photorec -h
PhotoRec 7.2, Data Recovery Utility, February 2024
Christophe GRENIER <grenier@cgsecurity.org>
https://www.cgsecurity.org

Usage: photorec [/log] [/debug] [/d recup_dir] [file.dd|file.e01|device]
       photorec /version

/log          : create a photorec.log file
/debug        : add debug information

PhotoRec searches for various file formats (JPEG, Office...). It stores files
in the recup_dir directory.
```

```bash
fidentify -h
```

```console
root@kali:~# fidentify -h

Usage: fidentify [--check] [+file_format] [directory|file]
       fidentify --version

fidentify determines the file type, the 'extension', by using the same database as PhotoRec.
By default, all known file formats are searched unless one is specifically enabled.
```

```bash
qphotorec -h
```

```console
root@kali:~# qphotorec -h

Usage: qphotorec
       qphotorec /version

QPhotoRec searches various file formats (JPEG, Office...), it stores them
in recup_dir directory.
```

**先看看有哪些盘（只读操作，安全）**：

```bash
sudo testdisk /list
```

```console
root@kali:~# sudo testdisk /list
Disk /dev/nvme0n1 - 512 GB / 476 GiB - CHS 62260 255 63, sector size=512
  #  Start        End    Size  Id  Type
  1  2048  1048575   511M   EF  EFI System
  2  1048576  1050623   1M   0B  W95 FAT32
  ...
Disk /dev/sdb - 15 GB / 14 GiB - CHS 1878 255 63, sector size=512
  Partition                  Start        End    Size in sectors
  >  1 P FAT32                8064    7831551    7823488 [PHOTOS]
```

**这就是「先看盘、不写盘」的安全起手式。**

**注意 Kali 上的路径**：`testdisk`/`photorec` 装在 `/usr/sbin/`，**普通用户可能不在 `PATH` 里**——用完整路径或 `sudo`（`sudo` 下 `/usr/sbin` 通常在 PATH 里）。

---

## 4. 核心参数详解

> 命令行参数取自上面的 `-h` 原文；交互式界面的按键是 TestDisk/PhotoRec 的 TUI（**没有命令行等价物**）。

### 4.1 `testdisk` 命令行

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `file.dd` / `file.e01` / `device` | **直接指定要操作的对象**（镜像文件、E01 证据镜像、块设备） | **强烈建议传镜像文件而不是物理盘**（场景 2 就是这么做的） |
| `/log` | **生成 `testdisk.log`** | **取证场景必加**：记录你做了哪些操作（可追溯性） |
| `/debug` | 输出调试信息 | 排错、报告 bug 时用 |
| `/list` | **只列出当前分区**后退出 | **只读**；恢复前的第一次「看盘」 |
| `/version` | 打印版本 | 记录环境 |

**`/list` 是唯一一个真正「无副作用」的入口**——它只读分区表并打印。**任何正式操作前都先 `/list` 一下。**

### 4.2 `photorec` 命令行

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `file.dd` / `file.e01` / `device` | 要扫描的对象 | **可以是镜像文件**（推荐的练习方式） |
| `/d <dir>` | **恢复文件的输出目录**（替代默认的 `recup_dir`） | **必须指向另一块盘！** 这是最关键的一个参数 |
| `/log` | 生成 `photorec.log` | 记录扫描过程与配置（**取证的证据链**） |
| `/debug` | 调试输出 | 排错 |
| `/version` | 版本 | —— |

> **默认输出目录名是 `recup_dir`**（会自增为 `recup_dir.1`、`recup_dir.2`…）。**如果当前目录就是待恢复的盘，就会覆盖数据。** 所以**几乎总是应该显式给 `/d`**。

### 4.3 `fidentify` 命令行

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `directory\|file` | 要识别的目标（可递归目录） | 恢复出一堆无扩展名文件时用它套类型 |
| `+file_format` | **只按指定格式判断**（如 `+jpg`） | 缩小判断范围，避免误判 |
| `--check` | 自检模式 | 验证安装完整性 |
| `--version` | 版本 | —— |

### 4.4 TestDisk 交互式菜单（**这才是主要用法**）

**主流程（分区恢复）**：

| 界面 | 选项 | 作用 |
|------|------|------|
| **磁盘选择** | 列出所有 `/dev/sdX`、`/dev/nvmeXnY` 及镜像文件 | 选**要恢复的对象**（优先选镜像文件） |
| **分区表类型** | `Intel`（MBR）/ `EFI GPT` / `None` / `Mac` / `Sun` / … | **TestDisk 通常自动识别正确类型**；不确定就接受默认 |
| | `None` | **不做分区表分析**，直接进 `Advanced`（用于整个盘就是一个文件系统、或想逐分区分析） |
| **主菜单** | `Analyse` | **开始分析分区结构** ← 最常用 |
| | `Advanced` | 低级操作：`Boot`（引导扇区）、`Undelete`（文件系统级取消删除）、`Image Creation`（做镜像）、`Superblock`（备份超级块） |
| | `Geometry` | 磁盘几何参数（CHS） |
| | `Options` | 让 TestDisk 无提示运行等选项 |
| | `Quit` | 退出（**会问你保存不保存**） |
| **Analyse 后** | `Quick Search` | 快速扫描分区残留 |
| | `Deeper Search` | **深扫全盘**（慢但完整） |
| | `Backup` | 用备份分区表恢复 |
| **找到分区后** | 列表用 `P` 键**预览该分区的文件**（**关键：先确认「这是对的那个分区」**） | |
| | `Continue` | 接受结果，进入下一屏 |
| | `Write` | **把分区表写回磁盘** ← **这是唯一会写盘的动作，会改结构！** |
| | `Quit` | 放弃 |
| **Advanced 菜单** | `Boot` | **修复引导扇区**（NTFS/ext 系）：`Rebuild BS` / `Repair MFT` / `Backup BS` / `Dump` |
| | `Undelete` | **文件系统级取消删除**（前提：文件系统元数据还在）——**能保留文件名！** |
| | `Image Creation` | 在 TestDisk 里做镜像（等价 `dd`） |
| | `Superblock` | 用**备份超级块**恢复 ext 系文件系统 |

**关键按键（全流程通用）**：

| 键 | 作用 |
|----|------|
| `↑` `↓` | 移动选择 |
| `←` `→` | 切换页面/选项 |
| `Enter` | 确认 |
| `p` | **预览选中分区的文件列表**（**确认正确性的关键**） |
| `a` | 全选 |
| `:` | 在 `Undelete` 里**选择**当前项 |
| `c` | **复制选中项**（`Undelete` 里用它把文件拷出来） |
| `C` / `Shift+C` | 切换其它文件选择 |
| `u` | 取消选中 |
| `h` | 帮助 |
| `q` | 退出/返回 |

**⚠️ 最重要的两个动作的差别**：

| 动作 | 会写盘吗 | 用途 |
|------|----------|------|
| `Quick Search` / `Deeper Search` / `P` 预览 | **不会**（只读） | **随便试，安全** |
| **`Write`** | ✅ **会改分区表** | **只在确认无误后按** |
| **`Undelete` 里 `c` 复制文件** | ✅ 会写到**你指定的目标目录** | 确保目标是**另一块盘** |

### 4.5 PhotoRec 交互式流程（6 步）

| 步骤 | 界面 | 选择什么 |
|------|------|----------|
| ① | 磁盘选择 | 要扫描的盘/镜像 |
| ② | 分区选择 | 具体分区；或 **`No partition` / 整盘**（分区表坏掉时选这个） |
| ③ | **文件系统类型** | `ext2/ext3/ext4` / `FAT/NTFS/exFAT` / `other`（**选错不会损坏数据，但可能影响「是否只扫空闲区」的判断**） |
| ④ | **扫描范围** | **`Free`** = 只扫**空闲/未分配区**（**推荐，快得多**）<br>**`Whole`** = 扫**整个分区**（分区被格式化过、或要找回更旧的文件时用） |
| ⑤ | **输出目录** | **必须选另一块盘上的目录** ← 最关键 |
| ⑥ | 开始 | 按 `C` 开始（或回车） |

扫描过程中会实时显示「已找到 N 个文件」；可以随时 `Ctrl-C` 停止。

**输出结构**：

```
recup_dir.1/
├── f0000001.jpg
├── f0000002.jpg
├── f0000003.pdf
├── ...
└── report.xml        ← 记录每个文件的原位置（**取证价值**）
```

| 产物 | 含义 |
|------|------|
| `f0000123.<ext>` | **雕刻出的文件**（`f` = file，编号递增，扩展名来自签名识别） |
| `report.xml` | **每个恢复文件的原始偏移/大小等信息**——**写报告时这是证据** |

---

## 5. 实战演练

> ## ⚠️ 本节前提（**必须读完再动手**）
>
> **本题的所有练习必须在「虚拟磁盘 / 临时磁盘」上做，绝不在真实硬盘上做。**
>
> **1. 为什么**：
> - `TestDisk` 的 `Write` 会**改分区表**；`PhotoRec` 会**向目标盘写大量文件**；
> - 在真实系统盘上做，**轻则分区丢失，重则整个系统不可启动**；
> - 在只有一块盘的机器上「练恢复」，**你恢复出的文件本身就是对数据的覆盖**。
>
> **2. 怎么做（推荐顺序）**：
> - **方式 A（最推荐）**：**一次性虚拟机 + 挂载一块虚拟磁盘**（VMware/VirtualBox/QEMU 里加一块 1-2 GB 的虚拟盘）；
> - **方式 B**：**U 盘 / SD 卡**（你自己的，且里面没有重要数据）；
> - **方式 C**：**纯文件镜像**（`dd if=/dev/zero` 造一个 `disk.img`，全程在文件上操作）；
> - **方式 D**：**回环设备**（`losetup` 把一个镜像文件变成 `/dev/loopN`）。
>
> **3. 铁律**：
> - **恢复输出目录必须在另一块盘上**；
> - **不要用文件管理器自动挂载待恢复的分区**；
> - **先做镜像**（`dcfldd`/`dd`），把镜像当「原件」做实验——这样玩坏了可以重新造。

**先把「练习盘」造出来（这样你可以无限次重来）**：

```bash
# 造一个 512 MB 的镜像文件（这就是你的「练习盘」）
dd if=/dev/zero of=/tmp/lab-disk.img bs=1M count=512 status=progress
ls -lh /tmp/lab-disk.img
```

```console
-rw-r--r-- 1 root root 512M Sep 15 10:30 /tmp/lab-disk.img
```

### 场景 1：把测试盘分区、放文件、然后**故意删掉分区表**，再用 TestDisk 恢复

**1a. 给练习盘分区并写入文件（模拟一个正常使用的盘）**

```bash
# 把镜像挂成回环设备
sudo losetup -fP /tmp/lab-disk.img
LOOP=$(losetup -j /tmp/lab-disk.img | cut -d: -f1)
echo "练习盘设备: $LOOP"
lsblk "$LOOP"
```

```console
练习盘设备: /dev/loop0
NAME      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0       7:0    0  512M  0 loop
```

```bash
# 建分区表 + 一个分区
sudo parted -s "$LOOP" mklabel msdos
sudo parted -s "$LOOP" mkpart primary fat32 1MiB 100%
sudo partprobe "$LOOP"; sleep 1
sudo mkfs.vfat -F 32 "${LOOP}p1"
lsblk "$LOOP"
```

```console
NAME      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0       7:0    0  512M  0 loop
└─loop0p1   7:1    0  511M  0 part
```

```bash
# 放一些「要被恢复的文件」进去
sudo mkdir -p /mnt/labdisk
sudo mount "${LOOP}p1" /mnt/labdisk
# 造几张「假照片」（最小合法 PNG/JPEG 头，便于 PhotoRec 识别）
for i in $(seq 1 5); do
  printf '\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00' > "/mnt/labdisk/photo$i.jpg"
  head -c 20000 /dev/urandom >> "/mnt/labdisk/photo$i.jpg"
  printf '\xff\xd9' >> "/mnt/labdisk/photo$i.jpg"
done
printf '%%PDF-1.4\n%% test doc\n%%%%EOF\n' > /mnt/labdisk/doc1.pdf
echo 'hello, this is a test text file' > /mnt/labdisk/notes.txt
ls -l /mnt/labdisk/
sudo umount /mnt/labdisk
```

```console
root@kali:~# ls -l /mnt/labdisk/
-rw-r--r-- 1 root root    41 ... doc1.pdf
-rw-r--r-- 1 root root    29 ... notes.txt
-rw-r--r-- 1 root root 20022 ... photo1.jpg
...
```

**1b. 存储这张「盘」的现状（便于之后对比）**

```bash
# 记录一个「已知正常」的镜像，用于对比与回滚
sudo dd if=/tmp/lab-disk.img of=/tmp/lab-disk-GOOD.img bs=1M status=none
md5sum /tmp/lab-disk.img /tmp/lab-disk-GOOD.img
```

```console
# 两个哈希一致 = 备份成功。之后玩坏了就用 GOOD 重新开始：
#   sudo dd if=/tmp/lab-disk-GOOD.img of=/tmp/lab-disk.img bs=1M
```

**1c. 故意毁掉分区表（模拟「误删分区」）**

```bash
sudo losetup -d "$LOOP" 2>/dev/null || true
sudo losetup -fP /tmp/lab-disk.img
LOOP=$(losetup -j /tmp/lab-disk.img | cut -d: -f1)

# 把 MBR 的前 512 字节清空 —— 分区表就没了
sudo dd if=/dev/zero of="$LOOP" bs=512 count=1 conv=notrunc
sudo partprobe "$LOOP"; sleep 1
lsblk "$LOOP"
```

```console
NAME      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0       7:0    0  512M  0 loop      ← 分区没了！
```

```bash
# 系统现在认为这是一块「没有分区的盘」，无法挂载
sudo mount "${LOOP}p1" /mnt/labdisk 2>&1 | head -2
```

```console
mount: /mnt/labdisk: special device /dev/loop0p1 does not exist.
```

**解读**：**这就是「分区被删」的典型症状**——`lsblk` 里只剩设备名，没有分区。**数据其实还在原来的扇区里，只是「地图」丢了。**

**1d. 用 TestDisk 恢复分区表**

```bash
# ⚠️ 关键：对【镜像文件】操作，而不是物理盘 —— 这样最安全，也最容易回滚
sudo testdisk /log /tmp/lab-disk.img
```

**交互步骤（逐步对照）**：

```
① 主界面：[Create]（创建日志） / [Append] / [No Log]
     → 用 ← → 选 [Create]，回车
        （你已经加了 /log 参数，这里选 Create 会把日志写到 testdisk.log）

② Disk selection（选择要分析的盘）
     → 用 ↑ ↓ 选中 "/tmp/lab-disk.img"，回车

③ Partition table type（分区表类型）
     → TestDisk 会猜（这里猜 Intel）
     → 如果它猜的是别的，用 ← → 切到 [Intel]，回车

④ 主菜单
     → 选 [Analyse]，回车
     → 提示 "Should TestDisk search for partition created under Vista or later?"
       （是否搜索 Vista 以后创建的分区）：选 [Y] 或 [N] 均可，这里选 N

⑤ Analyse 结果
     → 显示 "No partition found or selected for recovery" 或无结果
     → 选 [Quick Search]，回车
```

**Quick Search 找到分区后**：

```
结构：Partition                Start        End    Size in sectors
       * FAT32                    2048     1048575     1046528 [NO NAME]

（用 ↑ ↓ 移动，用 ← → 在 [Continue] / [Deeper Search] / [Quit] 之间切换）
```

```console
# ⚠️ 最关键的一步：按 p 预览这个分区的文件！
#    这是确认「ToolDisk 找到的是不是对的那个分区」的唯一直接证据
```

按 `p` 后应该看到：

```console
Directory /
 drwxr-xr-x  ...  .
 drwxr-xr-x  ...  ..
 -rw-r--r--  ...  doc1.pdf
 -rw-r--r--  ...  notes.txt
 -rw-r--r--  ...  photo1.jpg
 ...
```

**解读（为什么必须先按 `p`）**：

- 如果**能看到正确的文件列表** → **这就是对的分区**，可以继续；
- 如果看到的是**一堆乱码/不相关的文件** → **候选错了**，应该 `Deeper Search` 或换方案；
- **`p` 是只读的**，随便试。

**确认后写出**：

```
⑥ 按 ↵（回车）退出预览 → 回到结果页
⑦ 用 ← → 选 [Continue]，回车
⑧ 看到分区列表（带 * 或 P 标记），用 ← → 选 [Write]，回车
⑨ 确认提示："Confirm ... write partition structure to disk?" → 输入 Y，回车
⑩ 提示重启系统 → 对镜像无所谓，选 [Quit] 退出 TestDisk
```

```bash
# ⑪ 让内核重新读分区表
sudo partprobe "$LOOP"; sleep 1
lsblk "$LOOP"
```

```console
NAME      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0       7:0    0  512M  0 loop
└─loop0p1   7:1    0  511M  0 part      ← 分区回来了！
```

```bash
# ⑫ 挂载验证：文件名、目录结构都在
sudo mount -o ro "${LOOP}p1" /mnt/labdisk
ls -l /mnt/labdisk/
sha256sum /mnt/labdisk/photo1.jpg
sudo umount /mnt/labdisk
```

**解读（这就是 TestDisk 的价值）**：**分区表修好了，文件名、目录、时间戳全部保留**——这是**结构级恢复**，比雕刻强得多。

```bash
# 查看 TestDisk 留下的日志（取证的证据链）
cat testdisk.log | head -40
```

**1e. 如果 `Quick Search` 找不到 —— 用 `Deeper Search`**

```bash
sudo testdisk /log /tmp/lab-disk.img
# ④ 主菜单 → [Analyse] → 回车
# ⑤ 出现 "No partition found" 或结果不全时，选 [Deeper Search]
#    ⚠️ 这一步会逐扇区扫描，可能跑很久（大磁盘可数小时）
```

**解读**：

| 手段 | 何时用 | 时间 |
|------|--------|------|
| `Quick Search` | 默认第一步 | 秒~分钟 |
| **`Deeper Search`** | Quick 找不到；或分区表被大面积破坏 | **分钟~小时** |
| `Backup` | **GPT 盘**：主表坏了但盘尾备份表完好 | 秒 |

**1f. 备份表恢复（GPT 特别有用）**

```bash
# 造一个 GPT 盘，然后只毁掉【主表】（保留盘尾备份）
dd if=/dev/zero of=/tmp/gpt-lab.img bs=1M count=256 status=none
LOOP2=$(sudo losetup -f --show /tmp/gpt-lab.img)
sudo parted -s "$LOOP2" mklabel gpt
sudo parted -s "$LOOP2" mkpart primary ext4 1MiB 100%
sudo partprobe "$LOOP2"; sleep 1
sudo losetup -d "$LOOP2"

# 只清掉前 1 MiB（主 GPT 表 + 主分区表）
sudo losetup -fP /tmp/gpt-lab.img
LOOP2=$(losetup -j /tmp/gpt-lab.img | cut -d: -f1)
sudo dd if=/dev/zero of="$LOOP2" bs=512 count=2048 conv=notrunc
sudo partprobe "$LOOP2"; lsblk "$LOOP2"       # 分区消失
```

```bash
# 用 TestDisk 的 Backup 选项从盘尾恢复
sudo testdisk /log /tmp/gpt-lab.img
# ③ 分区表类型 → 选 [EFI GPT]
# ④ 主菜单 → [Analyse]
# ⑤ TestDisk 通常会提示 "Backup GPT found"，选 [Backup] 用它恢复
# ⑥ 按 p 预览确认 → [Continue] → [Write] → Y
```

**解读**：**GPT 在磁盘末尾保存了一份完整的备份分区表**——所以「只坏了开头」的 GPT 盘恢复率极高。**TestDisk 会自动去找这份备份。**

### 场景 2：PhotoRec 恢复「格式化之后」的文件

场景 1 用的是「分区表坏了」——**结构能修**。现在模拟更糟的情况：**分区表完好，但文件系统被重建（格式化）**，元数据全丢。

**2a. 造出「被格式化」的现场**

```bash
# 复用场景 1 的盘（或者用 GOOD 镜像重置）
sudo losetup -d "$LOOP" 2>/dev/null; sudo losetup -fP /tmp/lab-disk.img
LOOP=$(losetup -j /tmp/lab-disk.img | cut -d: -f1)

# 写入文件、正常卸载
sudo mkdir -p /mnt/labdisk
sudo mount "${LOOP}p1" /mnt/labdisk 2>/dev/null || true
sudo umount /mnt/labdisk 2>/dev/null || true

# ⚠️ 关键：重新格式化（只重建 FAT，不填 0）—— 文件内容还在扇区里
sudo mkfs.vfat -F 32 "${LOOP}p1"
sudo partprobe "$LOOP"; sleep 1
lsblk "$LOOP"
```

```bash
# 挂上看看：文件全没了（这就是「格式化后」）
sudo mount "${LOOP}p1" /mnt/labdisk
ls -la /mnt/labdisk/
sudo umount /mnt/labdisk
```

```console
total 16
drwxr-xr-x  2 root root 16384 Jan  1  1970 .
drwxr-xr-x 12 root root  4096 Sep 15 10:40 ..
```
→ **一个文件都没有**。

**2b. 用 PhotoRec 雕刻**

```bash
# ⚠️ 恢复输出目录必须【不在】待恢复的盘上！
mkdir -p /tmp/recovered
sudo photorec /log /d /tmp/recovered /tmp/lab-disk.img
```

**交互步骤**：

```
① Disk selection → 选 "/tmp/lab-disk.img"，回车
② Partition selection
     → 选分区（不是 "No partition"），回车
     ⚠️ 如果分区表也坏了，这里选 "No partition" / 整个磁盘
③ File system type
     → 这里选 [FAT/NTFS/exFAT]（我们的盘是 FAT32）
       不确定就选 [other]（PhotoRec 会按「整个分区」处理）
④ 选择扫描范围
     → [Free]      只扫【空闲/未分配区域】  ← 推荐，快
     → [Whole]     扫描【整个分区】          ← 格式化后要找回更早的文件时用
     → 这里选 [Free]，回车
⑤ Select destination directory
     → 用 ↑ ↓ 找到 /tmp/recovered（**在另一块盘/文件系统上！**），按 C 确认
       （用 ← → 可以在不同目录树间切换，用 .. 往上级走）
⑥ 开始
     → 按 C 开始扫描（或回车，视界面提示）
     → 屏幕下方实时显示 "N files found"
     → 扫完会提示 "N files saved in /tmp/recovered/recup_dir.1/"
```

```console
root@kali:~# ls -l /tmp/recovered/recup_dir.1/
total ...
-rw-r--r-- 1 root root    41 ... f0000001.pdf
-rw-r--r-- 1 root root    29 ... f0000002.txt
-rw-r--r-- 1 root root 20022 ... f0000003.jpg
-rw-r--r-- 1 root root 20022 ... f0000004.jpg
-rw-r--r-- 1 root root 20022 ... f0000005.jpg
...
-rw-r--r-- 1 root root  ...  report.xml
```

**解读（这是雕刻的本质）**：

| 观察 | 含义 |
|------|------|
| **`f0000003.jpg`** 这样的名字 | **文件名丢失**（元数据被格式化掉了）；只按**签名**确定扩展名 |
| **所有文件在一个目录里** | **目录结构丢失**（除了 FAT 分区能恢复部分子目录） |
| **数量可能多于原文件数** | 签名误判 + 碎片残留，会有假阳性 |
| **`.txt` 可能很少或没有** | 纯文本**没有可靠签名** → **雕刻基本救不回 txt**（这是雕刻的固有短板） |
| `report.xml` | 记录每个文件在原盘上的位置 → **报告用** |

**验证恢复质量**：

```bash
# ① 用 md5 对比「能对上的」文件（照片内容应该一致）
md5sum /tmp/recovered/recup_dir.1/f*.jpg | sort
```

```bash
# ② 用 fidentify 复核类型（它和 PhotoRec 共用同一套数据库）
fidentify /tmp/recovered/recup_dir.1/
```

```console
/tmp/recovered/recup_dir.1/f0000001.pdf: pdf
/tmp/recovered/recup_dir.1/f0000003.jpg: jpg
...
```

```bash
# ③ 看 report.xml，把「恢复的文件」映射回原始偏移
head -30 /tmp/recovered/recup_dir.1/report.xml
```

**解读**：`report.xml` + `fidentify` 的组合，是**把雕刻结果写进取证报告的标配**：

| 工具 | 作用 |
|------|------|
| `report.xml` | 恢复文件的**原始位置与大小**（证据） |
| `fidentify` | **独立复核**文件类型（不是靠扩展名猜） |

**2c. 对比 `Free` 与 `Whole` 的差别**

```bash
# 再来一次，这次扫整个分区（Whole）——找回「更早被格式化掉」的文件
mkdir -p /tmp/recovered-whole
sudo photorec /log /d /tmp/recovered-whole /tmp/lab-disk.img
# ④ 这次选 [Whole]
```

**对比结果**：

```bash
echo "Free  扫描恢复数: $(ls /tmp/recovered/recup_dir.1/ | grep -c '^f')"
echo "Whole 扫描恢复数: $(ls /tmp/recovered-whole/recup_dir.1/ | grep -c '^f')"
```

| 模式 | 扫什么 | 何时用 |
|------|--------|--------|
| **`Free`** | 只扫**未被占用的扇区** | **默认**：当前文件系统还在，只是文件被删/被覆盖 |
| **`Whole`** | 扫**整个分区**（含已分配区域） | 分区被**格式化过多次**；要找**更早**的数据；或**分区表/文件系统完全无法识别** |

**代价**：`Whole` 慢得多，且会有更多假阳性。

### 场景 3：全流程判读、与同类工具对比、能救什么不能救什么

**3a. 完整判读流程（从故障现象到工具选择）**

```
症状：数据不见了
   │
   ├─ ① 立刻停止使用该盘（不要再写入！）
   │        ↓
   ├─ ② 做镜像（dcfldd/dd）—— 之后所有操作都在镜像上做
   │        ↓
   ├─ ③ 分区还在吗？ lsblk / fdisk -l
   │        │
   │        ├─ 分区【不在】→ TestDisk（[Analyse] → Quick/Deeper Search → p 预览 → Write）
   │        │        ↓
   │        │   修好后挂载，文件应该都在 ← 【最优结局】
   │        │
   │        └─ 分区【在】但挂载失败
   │                 ↓
   │            ④ 文件系统能用吗？ fsck 能修吗？（在镜像上试）
   │                 │
   │                 ├─ 能修 → 修完挂载，文件都在
   │                 │
   │                 └─ 不能修 → ⑤ 文件系统元数据还在？
   │                          │
   │                          ├─ 在 → 用 sleuthkit（fls/icat/tsk_recover）
   │                          │        ← **能保留文件名与时间戳**（比雕刻强）
   │                          │
   │                          └─ 不在 → ⑥ 用 PhotoRec 雕刻
   │                                   ← 文件名丢失，但内容能救
   └─ 每个阶段都要记录：做了什么、时间、结果（取证要求）
```

**3b. 与 `foremost` / `scalpel` / `sleuthkit` 的选择**

```bash
# sleuthkit：文件系统元数据还在时，能保留文件名
sudo fls -r -m / /tmp/lab-disk.img          # 列出所有文件（含已删除的，带 * 标记）
sudo tsk_recover -e /tmp/lab-disk.img /tmp/recovered-tsk   # 恢复
```

```bash
# foremost：用签名定义文件雕刻（可自定义格式）
sudo foremost -i /tmp/lab-disk.img -o /tmp/recovered-fm -t jpg,pdf
```

**对比表（决定用哪个）**：

| 情况 | 首选工具 | 能保住文件名吗 |
|------|----------|----------------|
| 分区表坏了 | **TestDisk** | ✅ 能（修好结构后） |
| 引导扇区坏了 | **TestDisk → Advanced → Boot** | ✅ 能 |
| 文件被删（文件系统还好） | **TestDisk → Advanced → Undelete** 或 **sleuthkit** | ✅ **能** |
| 文件系统损坏、元数据丢失 | **PhotoRec**（或 foremost/scalpel） | ❌ **不能** |
| 格式化过（元数据被重建） | **PhotoRec** | ❌ 不能 |
| 存储卡照片 | **PhotoRec**（专为此场景） | ❌ 不能 |
| 需要自定义签名（专有格式） | **foremost / scalpel** | ❌ 不能 |
| 只是要「按类型捞回所有图片」 | PhotoRec / foremost 都行 | ❌ 不能 |

**3c. 「能救什么、救不了什么」——必须写进报告的现实**

| 能救 | 说明 |
|------|------|
| **分区结构** | TestDisk 修表后，目录/文件名/时间戳完整 |
| **已删除文件（元数据还在）** | TestDisk 的 Undelete 或 sleuthkit |
| **连续存放的文件内容** | 雕刻（PhotoRec） |
| **照片/视频/文档/压缩包** | 有明确签名的格式 |

| **救不了 / 打折** | 原因 |
|-------------------|------|
| **已被覆盖的数据** | 物理上没了，**任何工具都救不了** |
| **碎片化的文件** | 雕刻只能按「头→尾」连续取，多段文件只能救第一段 |
| **纯文本文件（.txt、源码）** | **没有可靠签名**，雕刻识别不出来 |
| **专有格式** | 签名数据库里没有 |
| **加密容器（LUKS/BitLocker）** | 没有密钥就是乱码；熵分析能定位但解不开 |
| **文件名与目录结构（雕刻时）** | 元数据丢了就没有 |
| **inode 相关的元数据（时间戳、属主）** | 同上 |

```bash
# 验证「覆盖会致命」：在格式化后的盘上写入新数据，再雕刻一次
sudo mount "${LOOP}p1" /mnt/labdisk
sudo dd if=/dev/urandom of=/mnt/labdisk/bigfile.bin bs=1M count=100 status=none   # 覆盖 100MB
sudo umount /mnt/labdisk
mkdir -p /tmp/recovered-after
sudo photorec /log /d /tmp/recovered-after /tmp/lab-disk.img
# ⑤ 选 Free → 对比恢复数量：明显变少
echo "格式化后:      $(ls /tmp/recovered/recup_dir.1/ | grep -c '^f')"
echo "被覆盖 100MB 后: $(ls /tmp/recovered-after/recup_dir.1/ | grep -c '^f')"
```

**解读**：**这就是「第一时间停止使用该盘」的量化依据**——**每写入 1 MB 新数据，就有 1 MB 的旧数据永久消失**。

**3d. 用一个完整的小实验把「三种工具」串起来**

```bash
# ① 正常盘 → 删掉【文件】（不动分区表）
sudo mount "${LOOP}p1" /mnt/labdisk 2>/dev/null || { sudo mkfs.vfat -F 32 "${LOOP}p1"; sudo mount "${LOOP}p1" /mnt/labdisk; }
for i in 1 2 3; do printf '\xff\xd8\xff\xe0' > "/mnt/labdisk/del$i.jpg"; head -c 15000 /dev/urandom >> "/mnt/labdisk/del$i.jpg"; printf '\xff\xd9' >> "/mnt/labdisk/del$i.jpg"; done
sync && sudo umount /mnt/labdisk
sudo mount "${LOOP}p1" /mnt/labdisk
rm -v /mnt/labdisk/del*.jpg                  # 只删文件
sync && sudo umount /mnt/labdisk

# ② 此时【文件系统完好，只是文件被删】→ TestDisk 的 Undelete 能【保留文件名】！
sudo testdisk /log /tmp/lab-disk.img
#    ③ 类型 Intel → ④ 主菜单选 [Advanced] → 选分区 → [Undelete]
#    ⑤ ↑↓ 移动，用 : 选中 del1.jpg …（绿色/红色表示可恢复性）
#    ⑥ 按 C 选择目标目录（**另一块盘！**），按 c 复制
#    ⑦ 验证：恢复出来的文件名就是 del1.jpg / del2.jpg / del3.jpg
```

```bash
# ③ 对比：PhotoRec 对同一场景只能给出 f00xxxx.jpg（名字丢了）
mkdir -p /tmp/recovered-del
sudo photorec /log /d /tmp/recovered-del /tmp/lab-disk.img
ls /tmp/recovered-del/recup_dir.1/ | head
```

**解读（这组对比极具教学价值）**：

| 场景 | 工具 | 结果 |
|------|------|------|
| **文件被删，文件系统还好** | **TestDisk → Advanced → Undelete** | **能拿到 `del1.jpg`（文件名保留）** |
| 同上 | PhotoRec | 只能拿到 `f00000xx.jpg`（名字丢了） |

→ **再次印证选型原则**：**能修结构/能用文件系统工具，就别上雕刻。**

**3e. 清理**

```bash
sudo umount /mnt/labdisk 2>/dev/null
sudo losetup -d "$LOOP" 2>/dev/null
sudo losetup -D
rm -rf /tmp/lab-disk.img /tmp/lab-disk-GOOD.img /tmp/gpt-lab.img /tmp/recovered* /tmp/labdisk
```

---

## 6. 输出解读

### 6.1 TestDisk 的输出

**分区列表行**：

```
Partition                  Start        End    Size in sectors
 * FAT32                    2048     1048575     1046528 [PHOTOS]
 │   │                        │           │           │        │
 │   │                        │           │           │        └─ 卷标（如果有）
 │   │                        │           │           └─ 大小（扇区数）
 │   │                        │           └─ 结束 LBA
 │   │                        └─ 起始 LBA
 │   └─ 文件系统类型
 └─ 标记：* = 可启动(active)，P = 主分区，L = 逻辑分区，D = 已删除
```

| 标记 | 含义 |
|------|------|
| `*` | 可启动分区（active） |
| `P` | 主分区（Primary） |
| `L` | 逻辑分区（在扩展分区里） |
| `D` | **已删除**（TestDisk 用这个标记它认为被删的分区） |
| `E` | 扩展分区 |
| `N` | —— |

**判断要点**：

| 观察 | 结论 |
|------|------|
| 分区类型/大小/起始位置**与预期一致** | 这是正确的分区 |
| 分区的 `Start` 是 **2048 / 63 / 1MiB 对齐** 的 | **这是正常的现代分区**（不要怀疑对齐；不对齐才可疑） |
| 同一区域出现**多个重叠候选** | **必须用 `p` 逐个预览**，选文件正确的那一个 |
| 分区大小**明显不对**（比如整个盘当成了一个分区） | 可能把「整盘」误判为分区——用 `p` 验证 |
| Start/End **超出磁盘范围** | 明显错误，不要 Write |

**`p` 预览里要看的**：

| 观察 | 结论 |
|------|------|
| 能看到熟悉的文件名/目录 | **正确** |
| 一片乱码或大量无意义名字 | **错误候选**，继续找 |
| 空目录 | 可能是同类型但不对的分区 |

### 6.2 PhotoRec 的输出

**扫描过程输出**：

```
PhotoRec 7.2, Data Recovery Utility, February 2024
...
Disk /tmp/lab-disk.img - 512 MB / 488 MiB - CHS ...
     Partition                  Start        End    Size in sectors
   P FAT32                      2048     1048575     1046528

   N files found          ← 实时计数（关键指标）
```

| 观察 | 含义 |
|------|------|
| 计数**持续增长** | 正在找到文件，正常 |
| 计数**长时间不动** | 可能在扫描大片全零区域；耐心等，或 `Ctrl-C` |
| 计数**极大**（远超预期） | 可能有大量假阳性（尤其 `Whole` 模式 + 乱数据） |

**恢复结果目录**：

```
recup_dir.1/
├── f0000001.jpg      ← f + 8 位数字 + 识别出的扩展名
├── f0000002.pdf
├── ...
└── report.xml        ← 每个恢复文件的原偏移/大小
```

| 产物 | 解读 |
|------|------|
| `fXXXXXXXX.<ext>` | **扩展名来自签名识别，不是原文件名** |
| 数量 > 原始文件数 | 正常（有假阳性，也有同一文件被识别多次） |
| 数量远低于预期 | 可能：① 数据被覆盖；② 该类型没有签名（如 txt）；③ 应改用 `Whole` |
| `report.xml` | **报告里引用「文件来自偏移 X」的依据** |

**质量判断**：

| 检查 | 方法 |
|------|------|
| 文件能不能打开 | `file` / `fidentify` / 直接打开 |
| 内容是完整的吗 | 看文件大小、能否解密/渲染（照片能看、PDF 能开） |
| 是不是假阳性 | 用 `fidentify` 复核；随机抽样打开 |
| 有多少重复 | `md5sum * \| sort \| uniq -d -w32 \| head` |

### 6.3 报告该怎么写（取证场景）

| 必备要素 | 从哪来 |
|----------|--------|
| **镜像哈希**（操作前） | `sha256sum image.img` |
| **工具与版本** | `testdisk /version`、`photorec /version` |
| **执行的操作序列** | `testdisk.log` / `photorec.log`（**这就是加 `/log` 的意义**） |
| **恢复了什么、从哪个偏移** | `report.xml` |
| **文件类型的独立复核** | `fidentify` |
| **恢复后的哈希**（与原件对比） | `sha256sum` |
| **未能恢复的部分及原因** | 「被覆盖」「类型无签名」「碎片化」 |

---

## 7. 与其他工具配合

```
   ① 现场保护（最关键）
      立即停止使用设备；不要自动挂载；必要时断电保盘
                        │
   ② 做镜像（先在原盘上做一次只读镜像）
      dcfldd / dd / ewfacquire         → ../09-数字取证/dcfldd.md
      ★ 之后所有操作都在【镜像】上做
                        │
   ③ 结构级恢复（优先！）
      TestDisk：Analyse / Advanced(Boot, Undelete, Superblock)
      ├─ 分区表坏了 → Analyse → Write
      ├─ 引导扇区坏了 → Advanced → Boot → Rebuild BS
      └─ ext 超级块坏了 → Advanced → Superblock
                        │
   ④ 文件系统级恢复（元数据还在时）
      sleuthkit（fls / icat / tsk_recover）  → sleuthkit.md
      autopsy（图形化）                       → autopsy.md
      ★ 能保留文件名与时间戳
                        │
   ⑤ 内容级恢复（元数据没了）
      PhotoRec（签名数据库最全，专为存储卡设计）  → 本文
      foremost（可自定义签名）                   → foremost.md
      scalpel（配置文件驱动，更快）              → scalpel.md
                        │
   ⑥ 恢复结果的整理
      fidentify（复核类型）  → 本文
      exiftool（看照片元数据/时间）→ exiftool.md
      bulk-extractor（再捞一遍邮箱/URL/凭据）→ bulk-extractor.md
                        │
   ⑦ 深度分析
      binwalk（提取嵌套结构）→ binwalk.md
      yara（恶意样本扫描）    → ../02-漏洞分析/yara.md
      strings / radare2 / ghidra（可执行文件）
```

**关键配合点**：

| 组合 | 怎么做 |
|------|--------|
| **dcfldd → testdisk/photorec** | **永远先镜像**；`testdisk /log image.dd` 直接在镜像上操作，物理盘不动 |
| **testdisk + photorec** | **先 TestDisk 修结构**，修好了就不用雕刻（省时且结果更好） |
| **photorec + fidentify** | 雕刻完用 `fidentify` **独立复核**文件类型 |
| **photorec + exiftool** | 恢复出的照片用 `exiftool` 读拍摄时间/设备，**重建时间线** |
| **photorec → bulk-extractor** | 雕刻没救回的文本类内容，用 bulk-extractor 再捞特征 |
| **testdisk + sleuthkit** | 结构修好后用 sleuthkit 做文件系统级分析（含已删除文件的元数据） |
| **恢复结果 + yara** | 对恢复出的可执行文件做恶意样本扫描 |

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| **恢复出的文件把还没恢复的数据覆盖了** | **输出目录在待恢复的盘上**（最严重的错误） | **`/d` 必须指向另一块盘**；操作前 `pwd` 确认 |
| 挂载后 `lost+found` 里多了一堆文件 | **用了读写挂载**（系统在写盘） | **只读挂载**：`mount -o ro`；ext 系加 **`noload`**：`mount -o ro,noload` |
| `testdisk`/`photorec` 命令找不到 | 装在 `/usr/sbin`，普通用户 PATH 里没有 | 用 `sudo`，或 `/usr/sbin/testdisk` |
| 看不到想恢复的盘 | 设备名不对；或盘被别的进程占用 | `lsblk`、`sudo fdisk -l` 确认；先 `umount` |
| TestDisk 找到的分区**大小/类型明显不对** | 候选误判；或用错了分区表类型 | **先按 `p` 预览验证**；必要时改分区表类型（Intel↔EFI GPT）；用 `Deeper Search` |
| `Quick Search` **一个分区都没找到** | 分区表被大面积破坏；或整盘被写过 | 用 **`Deeper Search`**；或改用 **`Backup`**（GPT 盘尾备份）；或直接上 PhotoRec |
| **`Write` 之后分区没出现** | 内核没重读分区表 | `sudo partprobe <dev>`；或 `sudo partx -u <dev>`；或重插设备 |
| GPT 盘「主表坏了」 | 盘尾还有备份 | TestDisk 选 `EFI GPT` → `Analyse` → 用 `Backup` 恢复 |
| ext 分区挂载报「超级块损坏」 | 主超级块坏了 | TestDisk `Advanced` → `Superblock`，用备份超级块恢复；或 `mke2fs -n` 看备份位置后 `e2fsck -b <blk>` |
| PhotoRec 恢复出一堆**打不开的碎片** | 文件**碎片化**了，雕刻只能取第一段 | 改用 sleuthkit（如果元数据还在）；或接受现实 |
| **`.txt`/源码文件一个都没恢复** | **纯文本没有可靠签名** | 用 **`bulk-extractor`** 或 `strings`；或对特定内容自定义 foremost 签名 |
| 恢复数量远超原始文件数 | 假阳性（乱数据里碰巧出现签名） | 用 `fidentify` 复核；抽样打开；`md5sum` 去重 |
| 恢复数量远低于预期 | ① 数据被覆盖；② 该类型无签名；③ 用了 `Free` 但应该用 `Whole` | 换 `Whole`；检查是否已经写过盘；换工具 |
| PhotoRec 扫描极慢 | 盘大 + `Whole` 模式 | 先用 `Free`；或用镜像（比物理盘快）；关掉不必要的类型（如果界面支持） |
| 扫描中途程序崩溃 | 磁盘有坏道 / 镜像不完整 | 用 `ddrescue` 先做「容错镜像」，再在镜像上扫描 |
| 恢复的图片**只能看一半** | 后半段被覆盖 | 物理事实，无法恢复 |
| E01 证据镜像打不开 | 需要相应支持 | `testdisk` 支持 `.e01`；否则先用 `ewfexport` 转成 raw |
| `/dev/sdX` 上误操作了 | 忘了用镜像 | **立刻停止**；如果只是分区表被写错，用 TestDisk 再修回来；**不要继续写** |
| LUKS 加密盘扫描出一堆乱码 | 没解密 | 先 `cryptsetup luksOpen` 解密（需密钥），再恢复；**没有密钥无法恢复** |

---

## 9. 防御视角（蓝队 / 运维）

TestDisk/PhotoRec 在蓝队手里主要是**应急恢复**与**取证**工具，但防御的关键在**减少「需要恢复」的机会**。

| 场景 | 做法 |
|------|------|
| **防止误删分区/误格式化** | 关键数据盘与系统盘分离；操作前备份分区表（`sfdisk -d /dev/sdX > backup.txt`，GPT 用 `sgdisk --backup`） |
| **快速恢复能力** | 定期备份**分区表 + 引导扇区**，与数据分开存放 |
| **缩短恢复窗口** | 快照（LVM/ZFS/btrfs/虚拟机快照）+ 版本化备份 + 异地副本 |
| **勒索软件** | **离线/不可变备份**（3-2-1 原则）；勒索后**不要恢复运行时写过的盘**（可能已被加密） |
| **取证能力** | 预先准备**只读取证工具包**（`dcfldd`、`testdisk`、`sleuthkit`、`autopsy`），并**在演练中验证过** |
| **事件响应流程** | 明确「谁有权做镜像、镜像存哪、哈希怎么记录」——**哈希与操作日志是证据链** |
| **数据残留控制** | 淘汰/转卖的盘**必须安全擦除**（`dd` 覆写 / ATA Secure Erase / 消磁），否则 PhotoRec 能把你的旧数据全捞回来 |
| **SSD 的 TRIM** | SSD 上 TRIM 会真正清掉数据 → **删除后恢复率低**（好事也是坏事）；取证时注意 TRIM 已执行的情况 |
| **加密** | 全盘加密（LUKS/BitLocker）让「捡到盘/被偷盘」时恢复不可行——**这是最有效的数据保护** |

**蓝队/运维的六条硬建议**：

1. **`sfdisk -d` / `sgdisk --backup` 备份分区表**，和备份数据放在一起——**恢复分区表只要几秒**；
2. **淘汰介质必须擦除**：PhotoRec 能把你「以为删掉了」的东西全部捞回来。**转卖/报废前做完整覆写或 Secure Erase**；
3. **SSD 上删数据不可靠**（磨损均衡 + 快照），敏感数据必须**全盘加密**；
4. **演练恢复**：定期在虚拟机上练一次「分区丢失 → TestDisk 恢复」「格式化 → PhotoRec 雕刻」，**别等真出事才第一次用**；
5. **应急时的第一条纪律是「停止使用该设备」**——这是唯一能保住恢复率的动作；
6. **取证必须留哈希与操作日志**（`testdisk /log`、`sha256sum`），否则结论不可采信。

**「数据残留」这个风险值得单独强调**：

```text
售出/报废的硬盘里，PhotoRec 能恢复出什么？

  - 已删除的文件内容
  - 文件系统的历史结构（格式化过多次也能分层挖出）
  - 操作系统残留、配置文件、缓存
  - 浏览器历史、凭据缓存、SSH 私钥残留

→ 结论：用「删除 + 格式化」来处置介质是【无效的】。
   必须【覆写】或【加密】或【物理销毁】。
```

---

## 10. 参考

- Kali 工具页（含 `testdisk -h`、`photorec -h`、`fidentify -h`、`qphotorec -h` 原文）：<https://www.kali.org/tools/testdisk/>
- 上游（CGSecurity，含 TestDisk/PhotoRec 官方文档与文件格式支持列表）：<https://www.cgsecurity.org>
- TestDisk 文档：<https://www.cgsecurity.org/wiki/TestDisk>
- PhotoRec 文档与支持的文件格式：<https://www.cgsecurity.org/wiki/PhotoRec>
- Data Recovery 手册（作者写的免费书）：<https://www.cgsecurity.org/wiki/Recovering_deleted_files>
- Kali 包跟踪：<https://pkg.kali.org/pkg/testdisk>
- 本地命令：`testdisk -h`、`testdisk /list`、`testdisk /version`、`photorec -h`、`fidentify -h`、`qphotorec -h`、`man testdisk`、`man photorec`
- 配套教程：[`dcfldd.md`](dcfldd.md)、[`sleuthkit.md`](sleuthkit.md)、[`autopsy.md`](autopsy.md)、[`foremost.md`](foremost.md)、[`scalpel.md`](scalpel.md)、[`bulk-extractor.md`](bulk-extractor.md)、[`binwalk.md`](binwalk.md)、[`exiftool.md`](exiftool.md)

## ⚠️ 法律与伦理

数据恢复工具的能力**恰好等于「数据擦除工具的反面」**——它们能读回「你以为删掉了」的数据，因此法律风险集中在**对他人数据的接触**上。

**① 必须获得授权**

- 对**他人磁盘/存储介质**执行 TestDisk/PhotoRec，属于**读取他人数据**：

  - 《网络安全法》第 27 条：不得**窃取网络数据**；
  - 《刑法》第 285 条：**非法获取计算机信息系统数据**；
  - 《民法典》人格权编与《个人信息保护法》：未经同意处理他人个人信息；
- **捡到/继承/回收来的硬盘不是「无主物」**——里面的数据仍受法律保护。**必须走正式渠道归还或依法处置**，不要自己去「看看里面有什么」。

**② 取证场景的特殊要求（证据可采信）**

- **必须先做镜像、算哈希、记录操作日志**（`dcfldd` + `sha256sum` + `testdisk /log`）；
- **原介质应封存**，所有分析在镜像副本上进行；
- **操作过程要可复现、可回溯**（这也是加 `/log` 的原因）；
- **保全链（chain of custody）** 要完整记录：谁、何时、对什么、做了什么；
- 民事/刑事诉讼中，**取证过程不合规可能导致证据不被采纳**。

**③ 企业环境**

- 对**员工设备**做数据恢复/取证，需有**合法的内部制度与告知**（很多司法辖区有明确要求）；
- 恢复出的数据可能含**员工个人信息与通信内容**，应**最小化处理、限定用途、限期销毁**；
- 涉及客户数据的介质在**报废/转售前必须安全擦除**，否则可能构成**数据泄露**（可能触发《个人信息保护法》的报告义务）。

**④ 数据恢复不是「万能」的**

- **已被覆盖的数据在物理上消失**——宣称能恢复的是虚假宣传；
- 恢复出的碎片可能**不完整/不可读**，**不要对当事人作过度承诺**；
- **不要在唯一副本上操作**——一次误操作可能让「本可恢复」变成「完全不可恢复」。

**必须遵守**：

1. **只对自己拥有的介质、或获得明确授权的介质**做恢复与取证；
2. **第一时间做镜像**，此后**只在镜像上操作**；**恢复输出必须写到另一块盘**；
3. **记录哈希与操作日志**，保全证据链；
4. **捡到/回收的介质**走**归还/依法处置**流程，不擅自查看内容；
5. **报告脱敏**：不公开恢复出的个人数据、凭据、隐私内容；
6. **淘汰介质做安全擦除**（覆写 / Secure Erase / 加密 / 物理销毁）——**这是你自己数据安全的一部分**。
