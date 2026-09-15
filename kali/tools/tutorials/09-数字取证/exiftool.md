# ExifTool（元数据读取与写入）

> **一句话**：读取（并可按需写入）几乎**所有**文件格式的内部元数据——不只是照片的 EXIF，还包括文档的作者/修订历史、视频的拍摄设备、PDF 的生产工具、甚至 Office 文件的**最后保存者**。
> **分类**：数字取证 / 元数据与文件属性 ｜ **Kali 包**：`libimage-exiftool-perl`（命令 `exiftool`）｜ **官方文档**：<https://exiftool.org/> ｜ `man exiftool`

---

## 1. 它解决什么问题

元数据在取证里往往比文件**内容**更值钱：

| 你想知道 | 元数据给的答案 |
|----------|----------------|
| 这张照片是谁拍的、在哪拍的、什么设备 | EXIF：`Make`、`Model`、`DateTimeOriginal`、`GPSPosition` |
| 这张照片是真的吗？被编辑过吗 | `Software`（Photoshop 等）、`ModifyDate` 与 `CreateDate` 不一致 |
| 这份文档的作者是谁、最后谁保存的 | Office/PDF：`Author`、`LastModifiedBy`、`CreateDate`、`ModifyDate` |
| 文档是不是从某个模板/某台机器产生的 | `Company`、`Template`、生产者工具链 |
| 这个文件是不是「伪装」的 | `FileType`、`MIMEType` 与扩展名不一致 |
| 视频是不是被剪辑过 | 编码器、时长、创建时间 |
| 有没有隐藏的缩略图/嵌入内容 | `-b -ThumbnailImage`、`-ee` 提取嵌入对象 |

**[`sleuthkit.md`](sleuthkit.md) 给你文件系统的 MAC 时间（文件层）；exiftool 给你文件内部的元数据（内容层）** —— 两者交叉比对常能发现「文件系统时间被篡改」这类反取证迹象。

对比同类：

| 工具 | 定位 | 差异 |
|------|------|------|
| **ExifTool** | 元数据**读写**，支持格式极广 | 事实标准；`-json`/`-csv` 输出便于脚本化 |
| **`exifprobe` / `exiv2`** | 元数据读取（Kali 均在清单中） | 更轻量/更专注图片；格式覆盖面不如 exiftool |
| **`sleuthkit`** | 文件系统层时间 | 与 exiftool 交叉验证 |
| **`bulk-extractor`** | 特征提取（含 EXIF 扫描器） | 在**没有文件本体**时也能从字节流里捞 EXIF，见 [`bulk-extractor.md`](bulk-extractor.md) |
| **`identify`（ImageMagick）** | 图像属性 | 只做图像、不做全格式元数据 |

> **取证铁律**：**只用 exiftool 读，绝不用它写。** 写入会改变文件内容与哈希，破坏证据（写入场景只用于「自己造的测试素材」或「明确授权的元数据脱敏」）。

---

## 2. 工作原理

```
文件（图片/文档/视频/PDF/音视频/甚至某些二进制）
   │
   ├─ 识别格式（用 libmagic + 内置格式表）
   │
   ├─ 按格式解析元数据块：
   │    JPEG  → EXIF（TIFF IFD）、IPTC、XMP、ICC、MakerNotes（厂商私有）
   │    PNG   → tEXt/zTXt/iTXt 块
   │    TIFF  → IFD 链
   │    PDF   → Info 字典 + XMP
   │    DOCX/XLSX/PPTX → 包内 docProps/core.xml、app.xml（XMP）
   │    MP4/MOV → moov/udta 原子
   │    HTML  → meta 标签
   │    PE/ELF → 版本资源/注释段
   │
   ├─ 输出：按「组（group）」组织
   │    [EXIF] [GPS] [XMP] [IPTC] [MakerNotes] [PDF] [Composite] [File] [System]
   │    每组内是「标签 = 值」
   │
   └─ 计算派生（Composite）标签：如 GPSPosition、ImageSize、ShutterSpeed
```

**关键概念**：

- **标签组（-G）**：同一个概念可能有多份来源（EXIF 的 `DateTimeOriginal`、XMP 的 `DateTimeOriginal`、文件系统的 `FileModifyDate`）。**用 `-G` 看组名，避免张冠李戴**。
- **`-a`（allow duplicates）**：默认只显示每个标签的「第一个」值；`-a` 显示全部重复标签（**取证必加**，否则可能漏掉关键的另一份时间）。
- **`-u`（unknown）**：显示工具的格式表里没有的未知标签（**取证必加**，未知标签可能正是隐藏信息）。
- **`-s`（short）**：显示标签的**短名**（如 `DateTimeOriginal`），而不是描述（`Date/Time Original`）。脚本化时用 `-s`（**稳定**），人读时不用。
- **`-j`（JSON）/ `-csv`**：结构化输出，便于导入 SIEM/表格/脚本。
- **`Composite` 组**：由 exiftool 根据其他标签**计算**出来的（如 `GPSPosition` 组合经纬度、`ImageSize` 组合宽高）。**注意它是派生值，不是原始数据**。
- **MakerNotes**：厂商私有块，可能含**序列号**（`SerialNumber`）——**取证里非常有价值**（能关联到具体设备）。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install libimage-exiftool-perl
command -v exiftool
exiftool -ver
```

```console
$ exiftool -ver
13.55
```

最短用法（读单个文件）：

```bash
exiftool photo.jpg
```

```console
ExifTool Version Number         : 13.55
File Name                       : photo.jpg
Directory                       : .
File Size                       : 3.2 MB
File Modification Date/Time     : 2024:09:14 10:12:41+08:00
File Access Date/Time           : 2024:09:15 09:00:02+08:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Exif Byte Order                 : Little-endian (Intel, II)
Make                            : Canon
Camera Model Name               : Canon EOS 5D Mark IV
Software                        : Adobe Photoshop 25.0 (Windows)
Modify Date                     : 2024:09:14 10:20:00
Date/Time Original              : 2024:09:13 18:42:11
Create Date                     : 2024:09:13 18:42:11
Serial Number                   : 012345678901
GPS Latitude                    : 31 deg 13' 12.00" N
GPS Longitude                   : 121 deg 28' 12.00" E
GPS Position                    : 31 deg 13' 12.00" N, 121 deg 28' 12.00" E
Image Size                      : 6720x4480
...
```

**这一屏里已经有三条可用于结论的信息**：① 设备是 Canon EOS 5D Mark IV（序列号 `012345678901`）；② 拍摄时间 2024-09-13 18:42:11（**原始时间**）；③ 修改时间是 2024-09-14 10:20、`Software: Adobe Photoshop` —— **说明该照片在拍摄后被编辑过**。

---

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-a, --duplicates` | 显示**重复标签**的全部值 | **取证必加**（否则漏掉另一份时间/另一份 GPS） |
| `-u, --unknown` | 显示**未知标签** | **取证必加**（未知标签可能是关键线索） |
| `-g, --group` | 按**标签组**分节显示 | 人读时最清晰（分组为 `[EXIF]`、`[XMP]`…） |
| `-G, --group-names` | 在每行**前加组名** | 脚本化/CSV 时用（保证语义明确） |
| `-s, --short` | 用**短标签名**（稳定标识） | 脚本化必用；人读可不加 |
| `-j, --json` | **JSON 输出** | 导入 SIEM/程序处理 |
| `-csv` | **CSV 输出** | 导入表格/Excel；批量整理 |
| `-T, --tab` | 制表符分隔输出 | 与 `grep/awk` 配合 |
| `-n, --numeric` | 输出**原始数值**（不格式化） | GPS 换算成十进制度的近似值时用 |
| `-d <fmt>` | 自定义**日期格式** | 如 `-d '%Y-%m-%d %H:%M:%S'`；统一时间线格式 |
| `-r, --recurse` | 递归目录 | 批量分析整个目录树 |
| `-ext <ext>`（可重复） | 只处理指定扩展名 | 只看 `jpg`/`pdf`/`docx` |
| `-i, --ignore` | 忽略某些文件（模式） | 排除已知无害文件 |
| `-if <expr>` | **条件过滤**（Perl 表达式） | 「只列出带 GPS 的照片」等强大筛选 |
| `-p <fmt>` | 自定义输出模板 | 只打印关心的字段（报告表格） |
| `-w <file>` / `-w! <file>` | 结果写文件（`-w!` 覆盖） | 留证 |
| `-o <file>` | 指定输出文件 | 批量转写时 |
| `-b, --binary` | **二进制输出**（如提取缩略图） | `-b -ThumbnailImage > thumb.jpg` |
| `-ee, --extractEmbedded` | 提取**嵌入式**数据（视频内的 EXIF、嵌入对象） | 视频/复杂容器用 |
| `-api largefilesupport=1` | 大文件支持（>4GB） | 视频/大镜像 |
| `-v <n>` | 详细（调试）输出 | 排错；`-v3` 看解析过程 |
| `-validate` | **校验元数据一致性** | **取证必用**：能发现被刻意篡改/矛盾的时间 |
| `-htmlDump` | 输出可浏览的 HTML 结构报告 | 报告配图/深度分析 |
| `-overwrite_original` | **写入时不保留备份**（危险） | **取证场景禁止** |
| `-TagsFromFile <src>` | 从另一个文件复制标签（写入） | 仅用于自造素材 |
| `-all=` | **删除所有元数据**（写入） | 仅用于授权脱敏；**会改变哈希** |
| `-charset` / `-lang` | 字符集/语言 | 中文标签显示问题 |

> **写入类参数（`-overwrite_original`、`-all=`、`-TagsFromFile`）在取证中一律禁用**。它们只用于：① 自己造的实验素材；② 明确授权的元数据脱敏（且必须记录操作并重新计算哈希）。

---

## 5. 实战演练

> **环境声明**：以下使用**自建素材**（自己拍的照片、自己生成的文档）、**公开的取证样本**（NIST CFReDS 提供的图片/文档样本，包含带 GPS 与编辑痕迹的素材）、或**已获授权**的案件材料。
> **禁止**对未经授权的他人文件提取元数据（**照片元数据含拍摄地点与设备序列号，属敏感个人信息**）。

### 场景 1：单张图片的「完整身份」调查

```bash
# ① 最详细的一次读取（-a 显示重复、-u 显示未知、-g 分组）
exiftool -a -u -g photo.jpg
```

```console
---- ExifTool ----
ExifTool Version Number         : 13.55
---- System ----
File Name                       : photo.jpg
File Size                       : 3.2 MB
File Modification Date/Time     : 2024:09:14 10:12:41+08:00
File Access Date/Time           : 2024:09:15 09:00:02+08:00
File Inode Change Date/Time     : 2024:09:14 10:12:41+08:00
---- File ----
File Type                       : JPEG
MIME Type                       : image/jpeg
---- EXIF ----
Make                            : Canon
Camera Model Name               : Canon EOS 5D Mark IV
Orientation                     : Horizontal (normal)
Software                        : Adobe Photoshop 25.0 (Windows)
Modify Date                     : 2024:09:14 10:20:00
Date/Time Original              : 2024:09:13 18:42:11
Create Date                     : 2024:09:13 18:42:11
Serial Number                   : 012345678901
---- GPS ----
GPS Latitude Ref                : North
GPS Latitude                    : 31 deg 13' 12.00"
GPS Longitude Ref               : East
GPS Longitude                   : 121 deg 28' 12.00"
GPS Altitude                    : 12.4 m
---- Composite ----
GPS Position                    : 31 deg 13' 12.00" N, 121 deg 28' 12.00" E
Image Size                      : 6720x4480
Megapixels                      : 30.1
```

**解读 → 三条取证结论**：

| 观察 | 结论 |
|------|------|
| `Date/Time Original = 2024-09-13 18:42:11` vs `Modify Date = 2024-09-14 10:20:00` | **拍摄与修改相差近 16 小时**，说明文件在拍摄后被处理 |
| `Software: Adobe Photoshop 25.0 (Windows)` | **经过图像编辑软件处理**（不是相机直出） |
| `Serial Number: 012345678901` + `GPS Position: 31°13'12"N 121°28'12"E` | **设备可识别、地点可定位** → 高度敏感个人信息 |

```bash
# ② 只看时间相关的所有标签（交叉验证是否有矛盾）
exiftool -a -G -time:all photo.jpg
```

```console
[File]          File Modification Date/Time     : 2024:09:14 10:12:41+08:00
[File]          File Access Date/Time           : 2024:09:15 09:00:02+08:00
[EXIF]          Modify Date                     : 2024:09:14 10:20:00
[EXIF]          Date/Time Original              : 2024:09:13 18:42:11
[EXIF]          Create Date                     : 2024:09:13 18:42:11
[XMP]           Modify Date                     : 2024:09:14 10:20:03
[XMP]           Metadata Date                   : 2024:09:14 10:20:03
```

**解读（**这是元数据取证最核心的技巧**）**：

| 时间 | 来源 | 含义 |
|------|------|------|
| `Date/Time Original` | EXIF（相机写入） | **拍摄时间（最可信）** |
| `Create Date` | EXIF | 文件创建时间（相机写入） |
| `Modify Date`（EXIF） | 编辑软件 | **被修改的时间** |
| `Metadata Date`（XMP） | 编辑软件 | 元数据最后修改时间 |
| `File Modification Date/Time` | **文件系统** | 文件本身最后被写入的时间 |
| `File Access Date/Time` | **文件系统** | 最后被读取的时间（**注意：读取本文件本身也会更新它！**） |

**判断篡改的正规方法**：**EXIF 时间应早于或等于文件系统时间**。如果出现「EXIF 拍摄时间**晚于**文件系统修改时间」，说明有人**手改了 EXIF 时间**或**改过系统时钟**——这是伪造照片的重要依据。

```bash
# ③ 校验元数据一致性（-validate，取证必备）
exiftool -validate -warning -a photo.jpg
```

```console
Validate                        : 5 Warnings (44 minor)
Warning                         : [minor] Entries in IFD0 were out of sequence. Fixed.
Warning                         : [minor] Bad format (0) for MakerNotes entry 15
Warning                         : [minor] Overlapping MakerNotes entries
```

**解读**：`-validate` 会指出**结构层面的异常**（IFD 顺序错乱、重叠条目、坏格式）。**「条目重叠」「顺序错乱」常出现在被工具手工改写过的文件里**——这是「元数据被篡改过」的技术证据。

```bash
# ④ 提取缩略图（缩略图常保留「编辑前的样子」！）
exiftool -b -ThumbnailImage photo.jpg > thumb.jpg
file thumb.jpg
```

```console
thumb.jpg: JPEG image data, 160x120
```

**解读**：**这是实战中极易被忽视的高价值技巧**——如果原图被裁掉了某个敏感内容，但**嵌入缩略图没更新**，缩略图里可能还能看到原始画面。同理 `-b -PreviewImage`。

```bash
# ⑤ 用 -htmlDump 生成结构报告（含偏移，可回到刻雕/二进制层）
exiftool -htmlDump photo.jpg > /evidence/photo_structure.html
grep -o '<td>[0-9]*</td>' /evidence/photo_structure.html | head -5
```

### 场景 2：批量分析（目录树 + CSV + 条件筛选）

**2a. 批量导出为 CSV（报告表格直接用）**

```bash
exiftool -r -csv -ext jpg -ext jpeg -ext png \
   -FileName -CreateDate -DateTimeOriginal -ModifyDate \
   -Make -Model -SerialNumber -Software -GPSLatitude -GPSLongitude \
   /evidence/photos > /evidence/photos_meta.csv
head -5 /evidence/photos_meta.csv
```

```console
SourceFile,FileName,CreateDate,DateTimeOriginal,ModifyDate,Make,Model,SerialNumber,Software,GPSLatitude,GPSLongitude
/evidence/photos/a.jpg,a.jpg,2024:09:13 18:42:11,2024:09:13 18:42:11,2024:09:14 10:20:00,Canon,Canon EOS 5D Mark IV,012345678901,Adobe Photoshop 25.0 (Windows),31 deg 13' 12.00",121 deg 28' 12.00"
```

**2b. 条件筛选：只列出「带 GPS 的」文件（`-if`）**

```bash
exiftool -r -ext jpg -if '$GPSLatitude' -T -FileName -GPSPosition /evidence/photos
```

```console
a.jpg	31 deg 13' 12.00" N, 121 deg 28' 12.00" E
c.jpg	39 deg 54' 32.00" N, 116 deg 23' 29.00" E
```

**2c. 条件筛选：找「被 Photoshop 处理过」的文件**

```bash
exiftool -r -if '$Software =~ /Photoshop|GIMP/i' -T -FileName -Software /evidence/photos
```

```console
a.jpg	Adobe Photoshop 25.0 (Windows)
```

**2d. 找「EXIF 时间缺失」的文件（可疑迹象）**

```bash
exiftool -r -ext jpg -if 'not $DateTimeOriginal' -T -FileName /evidence/photos
```

```console
suspicious1.jpg
suspicious2.jpg
```

**解读**：**元数据被「清洗」过的文件（例如社交平台转发、或刻意 `-all=` 删除）往往丢失 `DateTimeOriginal`**。在一批照片里，**「唯一几张没有拍摄时间的」通常值得单独关注**。

**2e. 找「扩展名与真实类型不符」的文件**

```bash
exiftool -r -T -FileName -FileType -MIMEType /evidence/photos | awk '$2 != "JPEG" && $2 != "PNG"'
```

```console
not_really.jpg	PDF	application/pdf
```

**解读**：扩展名是 `.jpg` 但 `FileType` 是 PDF → 典型的**伪装**（反取证手法之一）。这也能用 `file` 命令发现，但 **exiftool 的 `FileType` 更结构化，且能同时给出 MIME**。

**2f. 文档批量的作者与修订历史（Office/PDF）**

```bash
exiftool -r -ext docx -ext xlsx -ext pptx -ext pdf -csv \
   -FileName -Author -Creator -LastModifiedBy -CreateDate -ModifyDate -Producer \
   -Company -Template /evidence/docs > /evidence/docs_meta.csv
head -5 /evidence/docs_meta.csv
```

```console
SourceFile,FileName,Author,Creator,LastModifiedBy,CreateDate,ModifyDate,Producer,Company,Template
/evidence/docs/report.pdf,report.pdf,张伟,,,,2024:09:10 09:11:00,pdfTeX-1.40.25,,
/evidence/docs/q3.docx,q3.docx,李娜,李娜,王强,2024:08:01 10:00:00,2024:09:12 17:22:00,,ACME 公司,Normal.dotm
```

**解读（文档元数据的取证价值）**：

| 字段 | 含义 | 取证价值 |
|------|------|----------|
| `Author` / `Creator` | 原始作者 | 归属与责任 |
| `LastModifiedBy` | **最后修改者** | **可能与 Author 不同**（说明文件经他人修改） |
| `Company` / `Template` | 公司名、模板路径 | **可推断文件来源组织**（泄密溯源的关键） |
| `Producer`（PDF） | 生成工具 | 判断「是原始生成还是打印/转换而来」 |
| `CreateDate` / `ModifyDate` | 创建/修改 | 时间线（注意时区！） |

**⚠️ 时区提醒**：PDF/Office 元数据里的时间**常常没有时区信息**，会按本地时区解释。**报告里必须说明「元数据时间的时区未知/按 UTC+8 解释」**，否则时间线会错。

### 场景 3：视频、嵌入数据与「无文件本体」场景

**3a. 视频元数据（含 GPS）**

```bash
exiftool -api largefilesupport=1 -a -u -g video.mp4 | head -40
```

```console
---- QuickTime ----
Create Date                     : 2024:09:13 18:42:11
Duration                        : 32.50 s
Android Version                 : 13
---- QuickTime Keys ----
Location Information            : +31.2200+121.4700/
Make                            : Apple
Model                           : iPhone 14 Pro
Software                        : 17.4
```

**解读**：手机视频同样带 `Location Information`（GPS）与设备型号。**这是「谁在何时何地拍了这个视频」的直接证据。**

**3b. 提取嵌入数据（`-ee`）**

```bash
exiftool -ee -a -u video.mp4 | head -30
exiftool -ee -b -ThumbnailImage video.mp4 > video_thumb.jpg 2>/dev/null
file video_thumb.jpg
```

```console
video_thumb.jpg: JPEG image data, 320x240
```

**3c. 把 exiftool 与 bulk-extractor / TSK 交叉验证**

**场景**：你在未分配空间里雕出了一张照片（见 [`foremost.md`](foremost.md)），现在要确定「它来自哪台设备」。

```bash
# ① 雕刻结果 → 元数据
exiftool -a -u -G carved/jpg/00000003.jpg | grep -iE 'model|serial|software|date'
```

```console
[EXIF]  Camera Model Name  : Canon EOS 5D Mark IV
[EXIF]  Serial Number      : 012345678901
[EXIF]  Date/Time Original : 2024:09:13 18:42:11
```

```bash
# ② 与「嫌疑设备」拍摄的照片比对（同一序列号 → 同一台机器）
exiftool -T -SerialNumber /evidence/known_device_photos/*.jpg | sort -u
```

```console
012345678901
```

**解读**：**序列号一致 → 该雕刻出的照片确实由这台设备拍摄**。这是「设备关联」的强证据。

```bash
# ③ 与文件系统时间交叉验证（EXIF 时间 vs 文件 MAC 时间）
fls -l -o 2048 /evidence/disk.img | grep -i jpg
```

```console
r/r 13:	photo.jpg	2024-09-14 10:12:41 (CST)	...	3276800
```

| 层 | 时间 | 解读 |
|----|------|------|
| EXIF `DateTimeOriginal` | 2024-09-13 18:42:11 | 拍摄 |
| EXIF `ModifyDate` | 2024-09-14 10:20:00 | 被编辑 |
| 文件系统 M 时间 | 2024-09-14 10:12:41 | 文件写入磁盘（**应注意：早于 EXIF ModifyDate 说明 EXIF 被改过或时间来自别处**） |

**这类「跨层时间不一致」正是反取证/伪造的技术证据**——也正是 exiftool + TSK 联合分析的价值所在。

**3d. 无文件本体的情况（只有未分配空间/内存）**

如果连文件都雕不出来（数据被覆盖得只剩片段），可以用 **bulk-extractor 的 exif 扫描器**从字节流里直接捞 EXIF：

```bash
bulk_extractor -o /evidence/bulk-exif -E exif -j 8 /evidence/unalloc.bin
head -20 /evidence/bulk-exif/exif.txt
```

见 [`bulk-extractor.md`](bulk-extractor.md)。

---

## 6. 输出解读

### 6.1 标签组速查（`-g` 的分节）

| 组 | 内容 | 取证价值 |
|----|------|----------|
| `[System]` / `[File]` | **文件系统**信息（时间、权限、大小、MIME） | 与 TSK 交叉验证；**`FileAccessDate` 会被本次读取更新** |
| `[EXIF]` | 相机写入的原始信息 | **拍摄时间、设备、序列号（最可信）** |
| `[GPS]` | 经纬度、海拔、方向 | **地点定位（敏感个人信息）** |
| `[XMP]` | Adobe 等软件的 XMP | 编辑历史、`Metadata Date` |
| `[IPTC]` | 新闻/图库元数据 | 标题、关键词、作者 |
| `[MakerNotes]` | 厂商私有 | **机身序列号、快门次数、镜头** |
| `[PDF]` / `[XMP-PDF]` | PDF 生产者、创建/修改时间 | 文档溯源 |
| `[QuickTime]` / `[Keys]` | 视频元数据 | 拍摄设备、GPS、时长 |
| `[Composite]` | **派生/计算值** | 便捷但**非原始数据**（报告应引原始标签） |
| `[ICC_Profile]` | 色彩配置 | 判断是否经过专业图像流程 |

### 6.2 高价值标签（报告直接引用）

| 标签 | 含义 | 结论方向 |
|------|------|----------|
| `DateTimeOriginal` | 拍摄时间（相机写入） | **最可信的时间基准** |
| `ModifyDate`（EXIF/XMP） | 编辑时间 | 与拍摄时间差 = 编辑痕迹 |
| `Software` | 处理软件 | Photoshop/GIMP → **非原始文件** |
| `Make` / `Model` | 设备厂商/型号 | 设备识别 |
| `SerialNumber`（MakerNotes） | **机身序列号** | **设备唯一关联** |
| `GPSPosition` / `GPSLatitude/Longitude` | 经纬度 | 地点 |
| `Author` / `LastModifiedBy` | 文档作者/最后修改者 | 归属与责任 |
| `Company` / `Template` | 组织与模板 | **泄露溯源** |
| `Producer` / `Creator` | 生成工具链 | 判断处理流程 |
| `FileType` / `MIMEType` | 真实类型 | 发现伪装 |
| `Validate` / `Warning` | 结构异常 | **篡改/手工改写的证据** |
| `ThumbnailImage` | 嵌入缩略图 | **可能是编辑前的画面** |

### 6.3 成功判据

- **时间自洽**：EXIF 时间 ≤ 文件系统时间（否则需解释）；
- **结构校验通过**：`-validate` 无 warning（有 warning 需在报告中说明）；
- **跨工具一致**：exiftool 的 `FileType` 与 `file`/TSK 结论一致；
- **能形成闭环**：元数据（拍摄/编辑时间、设备序列号）能与其他证据（文件系统时间、雕刻偏移、设备记录）互相印证。

---

## 7. 与其他工具配合

```
① 取证链前端：dcfldd（镜像）→ sleuthkit（文件系统）           dcfldd.md / sleuthkit.md
        │
② 定位到具体文件（TSK）→ icat 提取出来
        │
③ 元数据层分析（本文 exiftool）
        │
        ├─► 时间线：EXIF 拍摄/编辑时间 × 文件系统 MAC 时间 → 交叉验证
        ├─► 设备关联：SerialNumber / Model → 与已知设备照片比对
        ├─► 地点：GPSPosition
        ├─► 溯源：Author / Company / Template / Producer
        ├─► 篡改判定：-validate 警告 + 时间矛盾 + Software 字段
        ├─► 隐藏信息：-b ThumbnailImage（编辑前画面）
        └─► 批量筛选：-if + -csv（找带 GPS 的、被 PS 改的、缺时间的）
        │
④ 互补工具
   ├─ bulk-extractor：无文件本体时从字节流捞 EXIF（exif 扫描器）  bulk-extractor.md
   ├─ foremost / scalpel：先雕出文件再分析                       foremost.md / scalpel.md
   ├─ binwalk：从固件/二进制里提取出的文件做元数据                  binwalk.md
   └─ autopsy：图形化浏览（底层同样读元数据）                      autopsy.md
```

**典型闭环命令**：

```bash
# 雕刻 → 元数据 → 特征
foremost -t jpg,doc,pdf -i unalloc.bin -o carved
exiftool -r -csv -FileName -DateTimeOriginal -Software -SerialNumber carved > meta.csv
bulk_extractor -o bulk -R carved
sha256sum carved/jpg/* > hashes.txt      # 证据校验值（必须）
```

- 文件系统时间与恢复：[`sleuthkit.md`](sleuthkit.md) ｜ 图形界面：[`autopsy.md`](autopsy.md)
- 无文件本体时的 EXIF 提取：[`bulk-extractor.md`](bulk-extractor.md)
- 雕刻：[`foremost.md`](foremost.md)、[`scalpel.md`](scalpel.md) ｜ 固件：[`binwalk.md`](binwalk.md) ｜ 获取：[`dcfldd.md`](dcfldd.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 只看到一部分标签 | 默认隐藏**重复**与**未知**标签 | **加 `-a -u`**（取证必须） |
| 中文字段名/中文值乱码 | 终端/字符集 | `-charset filename=UTF8`、`-lang zh-cn`；或输出到文件再读 |
| 时间差了 8 小时 | 元数据无时区，被按本地时区解释 | 用 `-d` 统一格式；**报告写明时区基准** |
| GPS 是度分秒，不好用 | 默认格式化输出 | `-n` 输出十进制度；或 `-c '%.6f'` 自定义格式 |
| `FileAccessDate` 每次都在变 | **读取文件本身就更新 atime** | 取证时注意：**你的分析行为会改变 atime**（要事先记录或挂载 `noatime`） |
| 批量处理报「文件不存在」 | 路径/通配符问题 | 用 `-r` + 目录；或用 `find ... -exec exiftool {} +` |
| 上万文件太慢 | 每个文件启动开销 | 用 `exiftool -@ argfile`（**参数文件**）批量；或 `-r` 一次传目录 |
| 想看「编辑前的画面」 | 只看了主图 | `-b -ThumbnailImage > thumb.jpg`；也试 `-b -PreviewImage` |
| `-validate` 报一堆 warning | 文件被多个工具改过/结构不规范 | **不要忽略**：report 里如实记录（可能是篡改迹象，也可能只是工具不规范） |
| 写入类操作导致哈希变化 | 用了 `-overwrite_original` / `-all=` | **取证严禁写入**；如必须脱敏，先记录原始哈希并重新计算 |
| 大视频读不出来 | 缺大文件支持 | `-api largefilesupport=1` |
| 视频里的 EXIF 看不到 | 元数据在嵌入流里 | `-ee`（extractEmbedded） |
| 标签名在脚本里对不上 | 用了描述名而不是短名 | 脚本里一律加 **`-s`**（短标签名稳定） |
| 想把结果导入表格 | 输出格式不对 | `-csv` 或 `-j`；注意 `-r` 时 `SourceFile` 列是完整路径 |

---

## 9. 防御视角（蓝队 / 隐私保护）

exiftool 在蓝队场景有两面：**取证时用它提取元数据**，**防护时用它评估自己的元数据泄露面**。

| 场景 | 用法 | 价值 |
|------|------|------|
| 泄密溯源 | `-csv -Author -LastModifiedBy -Company -Template` 批量导出 | 定位「哪份文档、谁做的、哪家公司的模板」 |
| 钓鱼/社工溯源 | 分析附件文档的元数据 | `Producer`/`Template`/`Author` 常能暴露攻击者的工具链与习惯 |
| 图片伪造识别 | `-validate` + 时间矛盾 + `Software` | 判断「这张照片是否被动过」 |
| 数字水印/设备关联 | `SerialNumber` + `Model` | 关联到具体设备 |
| 站点元数据泄露自检 | `exiftool -r -csv` 扫自家站点上传的图片 | **发现「照片带 GPS」的隐私泄露** |
| 内容发布前脱敏 | `exiftool -all= <file>`（**仅对自有素材**） | 删除上传图片的 GPS/作者信息 |
| 合规检查 | 批量检查文档是否残留「内部」标签 | 防止发布外泄内部信息 |
| 事件时间线 | EXIF 时间 × 文件系统时间 | 建立跨层时间线 |

**蓝队/组织的实操建议**：

1. **给上传功能加「元数据剥离」**：用户上传的图片在服务端用 exiftool（或图像库）去掉 EXIF/GPS，避免用户隐私泄露与内部信息外泄；
2. **发布流程加元数据检查**：对外发布的 PDF/Office 文档检查 `Author`/`Company`/`LastModifiedBy`（**这是最常见的无意泄露渠道**）；
3. **给员工做「照片门」培训**：手机默认开启 GPS 定位写入照片，公开分享前应清理；
4. **取证时只用只读方式**：任何写入都会破坏证据；
5. **保留原始元数据副本**：分析时导出 `-csv`/`-json`/`-htmlDump` 作为证据附件，避免反复读取（也避免 atime 不断变化）。

---

## 10. 参考

- ExifTool 官网（最权威的标签与参数参考）：<https://exiftool.org/>
- ExifTool 标签索引（按格式/组查标签含义）：<https://exiftool.org/TagNames/>
- 官方常见问题（含取证相关建议）：<https://exiftool.org/faq.html>
- Kali 工具页（libimage-exiftool-perl）：<https://www.kali.org/tools/libimage-exiftool-perl/>
- NIST CFReDS 公开取证样本（含带元数据的图片/文档）：<https://cfreds.nist.gov/>
- 本地命令：`exiftool -h`、`man exiftool`、`exiftool -list`（支持的格式列表）、`exiftool -listw`（可写标签）

## ⚠️ 法律与伦理

**照片元数据包含拍摄地点（GPS）、时间、设备序列号 —— 这属于敏感个人信息；文档元数据包含作者、公司、修订历史 —— 可能涉及商业秘密。** 未经授权提取与分析可能触犯：

- 《刑法》第 253 条之一（侵犯公民个人信息罪，**GPS 定位信息属敏感个人信息**）；
- 《刑法》第 285 条（非法获取计算机信息系统数据）；
- 《网络安全法》《数据安全法》《个人信息保护法》。

**必须遵守**：

1. **书面授权**：明确授权范围、目的与数据用途；企业内部调查需有制度依据；
2. **最小必要**：只提取与案件相关的字段（**不要无差别导出所有 GPS 与设备信息**）；
3. **只读**：**严禁写入类参数**（`-overwrite_original`、`-all=`、`-TagsFromFile`），否则会改变证据（哈希变化 = 证据链断裂）；
4. **注意自身行为的影响**：读取会更新 `atime`，分析前应记录原始状态，必要时在只读挂载上操作；
5. **数据加密与限时销毁**：导出的 CSV/JSON/HTML 属于敏感数据副本，按同一等级管理；
6. **报告脱敏**：不公开完整 GPS 坐标、设备序列号、真实姓名与公司内部信息，示例用 `31.22°N, 121.47°E`、`0123****8901` 这类脱敏形式；
7. **发布前脱敏**（自有内容）：对外发布的图片/文档应先用元数据清理，避免无意泄露。

本教程请仅在**自建素材**、**NIST CFReDS 公开样本**或**已获授权**的材料上练习。
