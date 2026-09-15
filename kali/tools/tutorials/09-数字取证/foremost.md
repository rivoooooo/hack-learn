# Foremost（文件雕刻 / File Carving）

> **一句话**：**不依赖文件系统**，只靠「文件头 + 文件尾 + 内部结构」在原始字节流里把图片、文档、压缩包一个个「雕」出来——专治元数据已毁、文件被删的场合。
> **分类**：数字取证 / 文件雕刻（Forensic Carving）｜ **Kali 包**：`foremost`（命令 `foremost`；配置 `foremost.conf`）｜ **官方文档**：<http://foremost.sourceforge.net/> ｜ `man foremost`

---

## 1. 它解决什么问题

[`sleuthkit.md`](sleuthkit.md) 靠**文件系统元数据**工作。如果元数据也没了（分区被格式化、inode 表被清、镜像只剩字节流），TSK 就无能为力——但你想要的文件**数据可能还在盘上**。

Foremost 的思路完全不同：**不认识文件系统，只认识文件格式的「签名」**。

```
原始字节流：... FF D8 FF E0 ... JPEG 数据 ... FF D9 ... [填充] ... 25 50 44 46 (PDF) ... %%EOF ... [填充]  25 50 44 46 (PDF) ...
              └────────── 一个 JPEG ──────────┘                └────────── 一个 PDF ──────────┘
```

它扫描整个字节流，发现 `FF D8 FF E0`（JPEG 起始）就开始「收集」，直到遇到 `FF D9`（JPEG 结束）——**收出来的就是文件**。文件名丢了、目录结构丢了，**但内容回来了**。

| 场景 | TSK（`fls`/`icat`） | Foremost |
|------|---------------------|----------|
| inode 元数据完好 | ✅ 精确（**有文件名、有时间、有归属**） | 可以，但不如 TSK 精确 |
| inode 表被清 / 分区被格式化 | ❌ 无法定位 | ✅ **雕刻出内容** |
| 未分配空间里的残留 | 部分（`blkls -A` 后仍需雕刻） | ✅ **正是它的主场** |
| 需要「这个文件原本叫什么」 | ✅ | ❌ 只能靠序号命名（如 `00000012.jpg`） |
| 需要文件时间戳 | ✅ | ❌（只能靠雕刻出的 EXIF 等内部元数据） |

**结论**：**TSK 与 Foremost 是互补的，不是替代关系**。原则是「**先 TSK，TSK 不行再雕刻**」。

对比同类：

| 工具 | 说明 |
|------|------|
| **Foremost** | 老牌、稳定、配置简单；**按类型内置头尾签名**（`foremost.conf`） |
| **`scalpel`** | Foremost 0.69 的**重写版**：更快、支持更大文件/更灵活的配置、支持块对齐限制；见 [`scalpel.md`](scalpel.md) |
| **`bulk-extractor`** | 不做「恢复文件」，只提特征；见 [`bulk-extractor.md`](bulk-extractor.md) |
| **`photorec`（testdisk 包）** | 交互式、支持更多文件系统与类型，适合个人数据恢复 |

---

## 2. 工作原理

```
输入（镜像 / 分区 / 未分配空间 / 单个大文件）
   │
   ├─ 按块顺序扫描（默认在 512 字节边界上找头）
   │
   ├─ 命中「文件头签名」（来自 foremost.conf）
   │     ├─ 开始收集字节，直到命中该类型的「文件尾签名」
   │     ├─ 若超过 maximum size 仍未找到尾 → 由 -a 参数决定是否仍保存
   │     └─ 若启用了内部结构校验（如 JPEG 的 SOI/EOI 配对），会做基本验证
   │
   └─ 输出：
        output/
          ├─ jpg/  00000000.jpg  00000001.jpg ...
          ├─ pdf/  00000000.pdf ...
          ├─ doc/  ...
          └─ audit.txt   ← 雕刻审计报告（**报告里必引用的证据**）
```

**关键机制**：

- **头/尾签名**：定义在 `foremost.conf`（默认从 `foremost.conf` 读取，Kali 上可用 `-c` 指定）。签名是**字节序列 + 可选偏移/长度**。
- **`-a`（全部头）**：**不做错误检测**，只要看到头就写出数据。对**损坏文件**有用（能拿到部分内容），但会产生大量垃圾。
- **`-q`（quick mode）**：只在 **512 字节边界**上搜索头。**快 10 倍以上**，但如果文件头不在扇区对齐位置就会漏（例如在磁盘镜像里，文件通常是对齐的；在内存转储里往往不对齐）。
- **`-d`（indirect block detection，间接块检测）**：针对 UNIX 文件系统（ext2/3/4）——**跟随 inode 的间接块指针**，从而把「不连续的碎片」拼起来。**这是 Foremost 处理 ext 文件系统碎片的关键能力**（默认关闭，因为会显著变慢）。
- **不解析文件系统**：所以对**加密容器**内的数据无效（加密后无签名）。
- **`-w`（只写审计文件）**：**先干跑一次**，看看「如果雕刻会雕出什么」，再决定是否真的写盘——非常实用的技巧。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install foremost
command -v foremost
foremost -h
```

```console
root@kali:~# foremost -h
foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick Mikus.
$ foremost [-v|-V|-h|-T|-Q|-q|-a|-w-d] [-t <type>] [-s <blocks>] [-k <size>] 
	[-b <size>] [-c <file>] [-o <dir>] [-i <file] 

-V  - display copyright information and exit
-t  - specify file type.  (-t jpeg,pdf ...) 
-d  - turn on indirect block detection (for UNIX file-systems) 
-i  - specify input file (default is stdin) 
-a  - Write all headers, perform no error detection (corrupted files) 
-w  - Only write the audit file, do not write any detected files to the disk 
-o  - set output directory (defaults to output)
-c  - set configuration file to use (defaults to foremost.conf)
-q  - enables quick mode. Search are performed on 512 byte boundaries.
-Q  - enables quiet mode. Suppress output messages. 
-v  - verbose mode. Logs all messages to screen
```

官方文档示例（在镜像里找文档与图片）：

```bash
foremost -t doc,jpg,pdf,xls -i image.dd
```

```console
Processing: image.dd
|*|
```

```console
$ ls output/
audit.txt  jpg  pdf
```

> **注意**：输出默认在**当前目录下的 `output/`**（若目录已存在且有内容，Foremost 行为会受影响——建议每次显式 `-o` 到全新目录）。

---

## 4. 核心参数详解

以下为 `foremost -h` 的**完整真实参数**：

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-i <file>` | **输入文件**（镜像/分区/任意字节流） | 可省略（从 stdin 读）；建议显式指定 |
| `-o <dir>` | **输出目录**（默认 `output`） | **每次用全新目录**，避免混淆不同任务 |
| `-t <type>` | **指定要雕刻的类型**（逗号分隔） | **`-t` 不是必须的**：不指定时按配置里的全部类型雕（慢且杂） |
| `-c <file>` | 使用指定的**配置文件** | 默认 `foremost.conf`；自定义类型时用 |
| `-a` | **写出所有头，不做错误检测** | **损坏文件救援**用；会大量产出垃圾，务必配合 `-o` 新目录 |
| `-q` | **快速模式**：只在 512 字节边界搜索 | 磁盘镜像上提速 10 倍以上；**内存转储/不齐整数据上会漏** |
| `-Q` | 安静模式（不输出进度） | 脚本化时用 |
| `-v` | 详细模式（把所有消息打到屏幕） | 排错用 |
| `-V` | 显示版权信息并退出 | —— |
| `-h` | 帮助 | —— |
| `-d` | **开启间接块检测**（针对 UNIX 文件系统） | ext2/3/4 镜像上**强烈建议开**（能把碎片拼起来）；会明显变慢 |
| `-s <blocks>` | **跳过输入开头的 N 个块** | 定向雕刻某个分区（配合块大小换算） |
| `-k <size>` | 限制雕刻文件的大小上限 | 防止一个「假头」把整盘都吞进去（默认上限见配置文件） |
| `-b <size>` | 设置块大小（字节） | 与 `-s`/`-q` 配合；默认 512 |
| `-T` | （见帮助 `-T` 项，用于按时间戳命名/标记输出） | 老版本行为，通常不用 |
| `-w` | **只写审计文件，不写任何雕刻出的文件** | **干跑**：先看会雕出什么，再决定是否真的写 |
| `-B`（部分版本）/ `-w` 变体 | 与 `-w` 相关的批处理行为 | 以 `-h` 为准 |

**支持的常用类型（`-t` 可用值，来自默认配置）**：

| 类型 | 说明 |
|------|------|
| `jpeg` / `jpg` | 图片（最常见的雕刻目标） |
| `png` / `gif` / `bmp` / `tif` | 其它图片格式 |
| `pdf` | PDF 文档 |
| `doc` / `docx` / `xls` / `ppt` | Office 文档（旧格式头尾明确，**比 OOXML 更容易雕**） |
| `zip` / `rar` / `gz` / `7z` | 压缩包（**数据泄露取证的常见目标**） |
| `html` / `htm` | 网页 |
| `exe` / `dll` | 可执行文件（PE 头） |
| `avi` / `mov` / `mp4` / `wmv` | 视频 |
| `mp3` / `wav` | 音频 |
| `ole` | OLE 复合文档 |
| `all` | 所有已配置类型 |

> **`-t` 的选择策略**：**不要无脑用 `all`**。先想清楚「我在找什么」——比如数据泄露案件通常只关心 `zip,tar,gz,doc,pdf,xls,jpg`。**类型越少，越快、越干净。**

---

## 5. 实战演练

> **环境声明**：以下全部使用**自建实验镜像**（生成方法见 [`dcfldd.md` 场景 1](dcfldd.md#场景-1造一个作案现场先有可练的镜像)）或**公开发布的取证样本**（NIST CFReDS）。
> **禁止**对未经授权的设备、镜像或数据执行雕刻与分析。**特别注意**：雕刻会大量写出文件到磁盘，请确保目标磁盘空间充足、且**不要写到证据所在的分区**。

### 场景 1：从镜像里雕刻出图片和文档（第一次使用）

```bash
# ① 先弄清镜像结构（不要盲目雕刻整盘）
mmls /evidence/disk.img
```

```console
      Slot      Start        End          Length       Description
004:  00        0000002048   000000524287   000000522240   Linux filesystem
```

```bash
# ② 从整个镜像直接雕刻（不做分区偏移处理，让 foremost 自己扫）
mkdir -p /evidence/carve1
foremost -t jpg,png,pdf,zip -i /evidence/disk.img -o /evidence/carve1 -v
```

```console
Processing: /evidence/disk.img
|*|
```

```console
$ ls -R /evidence/carve1 | head -20
/evidence/carve1:
audit.txt  jpg  pdf  zip

/evidence/carve1/jpg:
00000000.jpg

/evidence/carve1/pdf:
00000000.pdf
```

```bash
# ③ 看审计报告（这是报告里必须引用的证据）
cat /evidence/carve1/audit.txt
```

```console
Foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick Mikus
Audit File

Foremost started at Sat Sep 15 11:20:03 2024
Invocation: foremost -t jpg,png,pdf,zip -i /evidence/disk.img -o /evidence/carve1 -v
Output directory: /evidence/carve1
Configuration file: /etc/foremost.conf
------------------------------------------------------------------
File: /evidence/disk.img
Start:  Sat Sep 15 11:20:03 2024
Length: 256 MB (268435456 bytes)

Num	 Name (bs=512)	       Size	 File Offset	 Comment 

0:	00000000.jpg 	      4096 B 	  0 B
1:	00000000.pdf 	      1024 B 	  131072 B
* 
Finish: Sat Sep 15 11:20:05 2024

2 FILES EXTRACTED
	
jpg:= 1
pdf:= 1
------------------------------------------------------------------
```

**解读（`audit.txt` 逐列）**：

| 列 | 含义 | 用途 |
|----|------|------|
| `Num` | 该类型的序号 | 与文件名对应 |
| `Name (bs=512)` | **文件偏移（以 512 字节块为单位）** | **乘以 512 得到字节偏移** → 可回到 TSK 反查归属 |
| `Size` | 雕刻出的字节数 | 与实际文件大小比对（可能被截断） |
| `File Offset` | 字节偏移（部分版本提供） | 同上 |
| `Comment` | 附加信息（如是否因未找到尾而截断） | 判断文件是否损坏 |
| `N FILES EXTRACTED` | 各类型统计 | 报告中的量化结论 |

**重要**：`Name (bs=512)` 这一列就是**把雕刻结果与 TSK 连起来的桥梁**：

```bash
# 00000000.pdf 的偏移 = 131072 字节 → 块号 = 131072 / 4096 = 32
ifind -o 2048 -f ext4 -d $(expr 131072 / 4096 / 1024) /evidence/disk.img 2>/dev/null
# 更稳妥的做法：用 TSK 的块号定义（fsstat 查块大小）
fsstat -o 2048 /evidence/disk.img | grep -i 'block size'
```

### 场景 2：先干跑（`-w`）、再定向雕刻、最后处理碎片

**2a. 干跑：先看「如果雕会雕出什么」**

```bash
# -w：只写 audit.txt，不写文件 → 几秒钟就知道结果量级
mkdir -p /evidence/carve-dry
foremost -w -t all -i /evidence/disk.img -o /evidence/carve-dry
cat /evidence/carve-dry/audit.txt | tail -30
```

```console
	Num	 Name (bs=512)	       Size	 File Offset	 Comment 

0:	00000000.jpg 	      4096 B 	  0 B
1:	00000000.pdf 	      1024 B 	  131072 B
2:	00000000.zip 	      65536 B 	  524288 B
3:	00000000.doc 	      20480 B 	  1048576 B
*
Finish: Sat Sep 15 11:21:10 2024

4 FILES EXTRACTED
```

**解读**：**这是最重要的技巧**——`-w` 让你在不写出任何文件（不占空间、不污染目录）的情况下，**先知道有没有值得雕的东西**。

**2b. 定向雕刻：只雕我关心的类型，并开启间接块检测**

```bash
mkdir -p /evidence/carve-zip
foremost -t zip,rar,gz,7z,doc,xls,pdf -d -i /evidence/disk.img -o /evidence/carve-zip
```

```console
Processing: /evidence/disk.img
|*|
```

```bash
ls -lh /evidence/carve-zip/zip/
file /evidence/carve-zip/zip/*
```

```console
-rw-r--r-- 1 root root 64K Sep 15 11:25 /evidence/carve-zip/zip/00000000.zip
/evidence/carve-zip/zip/00000000.zip: Zip archive data, at least v2.0 to extract
```

**解读**：`-d`（间接块检测）专为 ext2/3/4 设计——**当文件在磁盘上不连续（碎片化）时，靠 inode 的间接块指针把碎片拼起来**。**不加 `-d` 时，碎片化的大文件往往只能雕出第一段**。代价是明显变慢。

```bash
# 校验雕出来的压缩包完整性（重要！）
unzip -t /evidence/carve-zip/zip/00000000.zip
```

```console
Archive:  /evidence/carve-zip/zip/00000000.zip
    testing: secret/                  OK
    testing: secret/employees.csv     OK
No errors detected in compressed data of /evidence/carve-zip/zip/00000000.zip.
```

**解读**：**`unzip -t` 通过 = 雕刻完整**。这类「可验证的雕刻结果」在报告里价值极高。反之如果报 `unexpected end of file`，说明文件被截断或碎片未拼全——需要在报告里如实说明「仅恢复部分内容」。

```bash
# 解出内容（数据泄露取证的证据本体）
unzip -o /evidence/carve-zip/zip/00000000.zip -d /evidence/export/zip_content
ls -l /evidence/export/zip_content/secret/
head -3 /evidence/export/zip_content/secret/employees.csv
```

**2c. 处理「找不到尾」的情况（`-a` 与损坏文件）**

```bash
# 破损文件：只写所有头，不做校验
mkdir -p /evidence/carve-all
foremost -a -t jpg -i /evidence/unallocated.bin -o /evidence/carve-all
```

```bash
# 结果里会有很多「半截图」——用工具批量筛出可用的
for f in /evidence/carve-all/jpg/*.jpg; do
  identify "$f" >/dev/null 2>&1 || echo "损坏: $f"
done 2>/dev/null | head
```

```console
损坏: /evidence/carve-all/jpg/00000007.jpg
损坏: /evidence/carve-all/jpg/00000012.jpg
```

**解读**：`-a` 的产出**必须做二次筛选**。可用的办法：`file`、`identify`（ImageMagick）、`pdftotext`、`unzip -t` —— **「能被解析器正常工作流打开的」才算有效证据**。

### 场景 3：雕刻「未分配空间」——最有效的定向策略

**为什么不该直接雕整盘**：整盘里 90% 是操作系统文件，全部雕出来会产生海量噪音（几千个无关的图标/文档），**既慢又难分析**。

**正确做法**：先用 TSK 导出未分配空间，再雕刻。

```bash
# ① 确认分区偏移与块大小
mmls /evidence/disk.img | grep 'Linux filesystem'
fsstat -o 2048 /evidence/disk.img | grep -iE 'block size|file system type'
```

```console
File System Type: Ext4
Block Size: 4096
```

```bash
# ② 导出未分配空间（已删除文件的数据就在这里）
blkls -A -o 2048 /evidence/disk.img > /evidence/unallocated.bin
ls -lh /evidence/unallocated.bin
```

```console
-rw-r--r-- 1 root root 96M Sep 15 11:30 /evidence/unallocated.bin
```

```bash
# ③ 只雕这一小部分（快得多，噪音少得多）
mkdir -p /evidence/carve-unalloc
foremost -t jpg,pdf,doc,zip,txt -d -i /evidence/unallocated.bin -o /evidence/carve-unalloc
cat /evidence/carve-unalloc/audit.txt | tail -12
```

```console
   Num	 Name (bs=512)	       Size	 File Offset	 Comment 

0:	00000003.jpg 	     12288 B 	   1536 B
1:	00000001.pdf 	      2048 B 	   1024 B
2:	00000002.zip 	     32768 B 	   4096 B
*
2 FILES EXTRACTED
```

**解读**：**未分配空间通常只占整盘的 5%–30%，但包含着「已删除文件」的全部内容**。在这个子集上雕刻，效率提升一个数量级，结果也更干净。**这是实战中最推荐的雕刻姿势。**

```bash
# ④ 与 bulk-extractor 交叉验证（同一个未分配空间，两种思路）
bulk_extractor -o /evidence/bulk-unalloc -j 8 /evidence/unallocated.bin
head -5 /evidence/bulk-unalloc/email.txt
```

见 [`bulk-extractor.md`](bulk-extractor.md)。

```bash
# ⑤ 记录完整操作（保管链）
cat >> /evidence/chain_of_custody.txt <<'EOF'
2024-09-15 11:30  blkls -A -o 2048 disk.img > unallocated.bin（导出未分配空间，96MB）
2024-09-15 11:35  foremost -t jpg,pdf,doc,zip,txt -d（雕刻未分配空间）
                  → 输出 /evidence/carve-unalloc，audit.txt 记录 3 个文件
2024-09-15 11:40  unzip -t 验证 zip 完整性：通过
EOF
```

---

## 6. 输出解读

### 6.1 `audit.txt`（报告必引）

| 字段 | 含义 | 报告里怎么写 |
|------|------|--------------|
| `Foremost started at` / `Invocation` | 时间与**完整命令行** | **原样抄进保管链文档**（可复现性） |
| `Configuration file` | 使用的配置 | 说明「用了哪些签名定义」 |
| `Num` | 序号 | 对应文件名 |
| `Name (bs=512)` | **偏移（512 字节块为单位）** | ×512 = 字节偏移 → 反查归属 |
| `Size` | 雕刻出的字节数 | 与真实大小比对，判断是否完整 |
| `Comment` | 附加说明（如 `(unable to locate EOF)`） | **有注释说明文件可能不完整** |
| `N FILES EXTRACTED` + 分类型统计 | 量化结论 | 「共恢复 X 个文件，其中 JPG Y 个、PDF Z 个」 |

### 6.2 雕刻结果的质量判断

| 检查方式 | 命令 | 通过的含义 |
|----------|------|------------|
| 类型识别 | `file <file>` | 文件头解析成功 |
| 图片完整性 | `identify <file>` 或 `file` | 能被解码器读取 |
| PDF 完整性 | `pdftotext <file> -` 或 `pdfinfo` | 结构完整 |
| 压缩包完整性 | `unzip -t` / `7z t` / `tar -tf` | **内部 CRC 校验通过（最强证据）** |
| Office 文档 | `libreoffice --headless --convert-to txt` | 能打开 |
| 哈希 | `sha256sum <file>` | 记录证据校验值 |

**关键原则**：**能在报告里写「该文件内部校验通过」远好于「雕刻出一个文件」**。前者是证据，后者只是线索。

### 6.3 常见「雕不出来/雕得不对」的原因

| 现象 | 原因 |
|------|------|
| 数量远少于预期 | 用了 `-q`（只在 512 边界找头），或文件头不在对齐位置 |
| 大文件只有开头一小段 | 文件碎片化，未加 `-d`（indirect block detection） |
| 文件全是「半截」 | 用了 `-a`（不做错误检测），或数据确实被覆盖 |
| 完全雕不出任何东西 | 数据被加密、被安全擦除（覆写）、或被压缩在无签名的容器里 |
| 结果与需求无关（大量图标） | 未限定类型（应显式 `-t`），或直接雕了整盘（应先导出未分配空间） |

---

## 7. 与其他工具配合

```
① 获取镜像（dcfldd / ddrescue / libewf）                      dcfldd.md
        │
② 结构分析（mmls / fsstat）→ 拿到分区偏移与块大小               sleuthkit.md
        │
③ 元数据还在？
   ├─ 是 → TSK 精确恢复（fls -d / istat / icat / tsk_recover）    sleuthkit.md
   └─ 否 / 还想兜底 → blkls -A 导出未分配空间
                              │
④ 雕刻：foremost（本文） / scalpel（更快更灵活）                scalpel.md
        │   └─ 输出 audit.txt（偏移→归属） + 按类型分目录的文件
        │
⑤ 特征提取（另一条线）：bulk_extractor（邮箱/URL/IP/凭据/直方图） bulk-extractor.md
        │
⑥ 细节：exiftool（拍摄设备/时间/GPS/GPS 定位）                 exiftool.md
        │
⑦ 固件/嵌套结构：binwalk（嵌套文件/压缩流/熵图）                binwalk.md
        │
⑧ 图形化复核：autopsy                                          autopsy.md
```

**典型闭环**：

```bash
blkls -A -o 2048 disk.img > unalloc.bin
foremost -t jpg,zip,pdf -d -i unalloc.bin -o carved
bulk_extractor -o bulk -R carved            # 对雕刻结果再提特征
exiftool carved/jpg/*.jpg | grep -i 'gps\|date'
```

- 元数据解析与归属：[`sleuthkit.md`](sleuthkit.md) ｜ 图形复核：[`autopsy.md`](autopsy.md)
- 更快的雕刻器：[`scalpel.md`](scalpel.md) ｜ 特征提取：[`bulk-extractor.md`](bulk-extractor.md)
- 元数据：[`exiftool.md`](exiftool.md) ｜ 固件：[`binwalk.md`](binwalk.md) ｜ 获取：[`dcfldd.md`](dcfldd.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 输出目录已有内容导致混乱 | 默认 `output/` 复用 | **每次 `-o` 到全新目录** |
| `Disk space` 耗尽 | `-a` + `all` 类型产生海量数据 | 先 `-w` 干跑；限定 `-t`；雕未分配空间而不是整盘 |
| 雕刻出的文件全是 0 字节或半截 | 头命中但尾没找到 | 检查是否被覆盖；用 `-a` 尝试抢救（并逐个人工验证）；加 `-d` 处理碎片 |
| 大文件只恢复开头 | 碎片化 + 未开 `-d` | 加 `-d`（仅对 UNIX 文件系统有效） |
| 数量明显偏少 | 用了 `-q`（512 边界搜索） | 去掉 `-q`（慢但全） |
| 图片打不开 | 雕刻内容不完整 | `-a` 模式下常见；用 `identify`/`file` 批量筛选 |
| `foremost.conf` 找不到 | 不在当前目录 | 用 `-c /etc/foremost.conf` 显式指定（Kali 上的实际位置用 `dpkg -L foremost` 过滤 `.conf` 查） |
| 加密盘里雕不出东西 | 数据加密（高熵） | 无法雕刻；需先解密 |
| 结果里有大量系统文件 | 直接雕了整盘 | 先 `blkls -A` 导出未分配空间 |
| 想按文件名/时间恢复 | 雕刻不保留元数据 | 用 TSK（`icat`/`tsk_recover`）而不是雕刻 |
| 运行极慢 | 全盘 + `-a` + 全部类型 + `-d` | 定向：先 `-w` 干跑 → 限定类型 → 只雕未分配空间 |

---

## 9. 防御视角（蓝队 / 应急响应）

Foremost 对蓝队有两个方向：

**方向一：应急响应中「抢救证据」**

| 场景 | 用法 |
|------|------|
| 攻击者删除工具/数据 | 对未分配空间雕刻出被删文件（与 `fls -d` 互补） |
| 分区被格式化 / inode 表被清 | 直接雕刻整盘或未分配空间（TSK 失效时的兜底） |
| 数据外带取证 | 雕刻 `zip/rar/7z`，用 `unzip -t` 验证完整性 → 证明「确实打包带走了什么」 |
| 找回被删的日志/脚本 | 雕刻 `txt/log/html`，配合时间线定位 |
| 恢复被删图片/截图 | 雕刻 `jpg/png`，再用 [`exiftool.md`](exiftool.md) 看拍摄时间与设备 |

**方向二：理解「为什么删除不可靠」（推动整改）**

| 现实 | 含义 |
|------|------|
| 删除文件 ≠ 数据消失 | 只要块未被覆盖，雕刻就能拿回来（**本工具就是证明**） |
| 快速格式化 ≠ 抹除 | 元数据被清，但数据块通常在 → 雕刻有效 |
| 仅「清空回收站」/`shred` 单个文件 | 其它副本（缩略图缓存、临时文件、日志、备份）随手可雕 |
| **安全擦除/全盘加密**才是有效控制 | 因此**终端全盘加密（BitLocker/FileVault/LUKS）是最高性价比的整改项** |

**蓝队建议**：

1. 把 `mmls` → `fsstat` → `blkls -A` → `foremost -t <关心类型> -d` 做成 IR 脚本的一环；
2. 对**含敏感数据的终端强制全盘加密**（否则设备丢失/被扣押时，数据等于明文交付）；
3. 涉密数据**销毁流程**要真正做安全擦除（且 SSD 需用厂商工具/加密擦除），不能只 `rm`；
4. 报告里对雕刻结果**做完整性与哈希记录**（`unzip -t` + `sha256sum`）。

---

## 10. 参考

- Foremost 官网与文档：<http://foremost.sourceforge.net/>
- Kali 工具页：<https://www.kali.org/tools/foremost/>
- 配置文件位置：`dpkg -L foremost | grep conf`、`man foremost`
- NIST CFReDS 公开取证镜像（雕刻练习素材）：<https://cfreds.nist.gov/>
- 本地命令：`foremost -h`、`man foremost`

## ⚠️ 法律与伦理

雕刻出的文件是**完整的原始内容**——很可能包含他人照片、聊天记录、文档、凭据、金融信息。未经授权获取或查看可能触犯：

- 《刑法》第 285 条（非法获取计算机信息系统数据）、**第 253 条之一（侵犯公民个人信息罪）**；
- 《网络安全法》《数据安全法》《个人信息保护法》。

**必须遵守**：

1. **书面授权**：明确授权分析对象、范围与目的；
2. **最小必要**：只雕刻与案件相关的类型与区域（用 `-t` 与「只雕未分配空间」控制范围），**不要无差别 `-t all` 全盘雕刻**；
3. **产出按敏感数据管理**：加密存储、限定人员、访问留痕；
4. **报告脱敏**：不粘贴私人图像、聊天内容、凭据；只给统计与脱敏样例；
5. **结案销毁**：按约定安全删除所有雕刻产物与中间文件（`unallocated.bin` 同样敏感！）；
6. **不要写到证据分区**：雕刻会大量写盘，必须写到独立的工作盘。

本教程请仅在**自建实验镜像**或 **NIST CFReDS 公开样本**上练习。
