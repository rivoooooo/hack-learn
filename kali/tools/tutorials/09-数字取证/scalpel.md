# Scalpel（高速文件雕刻）

> **一句话**：Foremost 0.69 的**彻底重写版**——雕刻更快、可自定义头尾签名、支持按簇对齐、能生成「雕刻覆盖率图」来证明「哪些区域被查过、哪些没查」。
> **分类**：数字取证 / 文件雕刻（Forensic Carving）｜ **Kali 包**：`scalpel`（命令 `scalpel`；配置 `/etc/scalpel/scalpel.conf`）｜ **官方文档**：`man scalpel` ｜ 上游：<https://github.com/nolaforensix/scalpel-1.60>

---

## 1. 它解决什么问题

雕刻（carving）本身不新鲜——[`foremost.md`](foremost.md) 就能做。但实战里 Foremost 会遇到三个瓶颈：

1. **慢**：只支持固定类型与固定块对齐策略；
2. **不可控**：不告诉你「它到底检查了镜像的哪些部分」；
3. **不灵活**：想加一个自定义文件格式（比如某行业的专有格式），很难。

Scalpel 针对性解决这三点：

| 问题 | Scalpel 的答案 |
|------|----------------|
| 慢 | 更高效的头/尾搜索与内存管理；可只雕你关心的类型 |
| 不可控 | **`-m` 生成雕刻覆盖率 blockmap**，`-u` 可「只雕覆盖率图里没查过的区域」 |
| 不灵活 | 配置文件里可**自定义任意头尾签名 + 最大雕刻长度 + 是否大小写敏感** |
| 碎片/对齐问题 | `-q <clustersize>` **按簇对齐雕刻**（避免在对齐要求严格的格式上雕出垃圾） |
| 想先看结果 | `-p` **预览模式**（只写审计日志，不写文件） |

对比同类：

| 工具 | 定位 | 关键差异 |
|------|------|----------|
| **Scalpel** | 文件雕刻 | **覆盖率图**（可证明「检查范围」）、簇对齐、灵活签名配置 |
| **Foremost** | 文件雕刻 | 更老牌、内置类型多、`-d` 支持 ext 间接块拼接；见 [`foremost.md`](foremost.md) |
| **`photorec`** | 交互式恢复 | 面向个人数据恢复，图形/TUI，支持 FS 结构 |
| **`bulk-extractor`** | 特征提取 | 不恢复文件；擅长「捞内容」，见 [`bulk-extractor.md`](bulk-extractor.md) |
| **`magicrescue` / `extundelete` / `ext4magic`** | 定向恢复 | 针对特定文件系统/文件系统日志；Kali 均在清单中 |

**实践建议**：两个雕刻器都装、**交叉使用**——`foremost` 内置签名全、上手快；`scalpel` 灵活、可证明覆盖率。**在报告里写「两个独立的雕刻器都恢复了同一文件」，可信度更高**。

---

## 2. 工作原理

```
① 读取配置文件 /etc/scalpel/scalpel.conf
   每一行定义一个类型的签名：
     # 注释
     doc  y  20000000  \x50\x4b\x03\x04  \x50\x4b\x05\x06
     ↑    ↑     ↑            ↑                ↑
   扩展名 是否  最大雕刻长度   文件头            文件尾
        大小写敏感
        │
② 扫描输入（镜像）：
   ├─ 默认：逐字节找文件头（-b 兼容模式下行为不同）
   ├─ -q <clustersize>：只在簇边界找头（对齐严格格式用）
   └─ 找到头 → 收集到文件尾（或到达最大长度）→ 输出文件
        │
③ 输出：
   ├─ -o <dir>  按类型分子目录存放雕刻结果
   ├─ audit.txt 审计日志（**列出「本该雕出」的候选与结果**）
   ├─ -m <file> 生成/更新**覆盖率 blockmap**
   └─ -t <dir>  指定 blockmap 存放目录
        │
④ -u 使用 blockmap：跳过「已经雕过」的区域
   → 增量雕刻（先雕一部分类型，再雕其他类型时不重复扫描）
```

**关键概念**：

- **配置文件格式**：`<扩展名> <大小写敏感:y/n> <最大长度> <头签名> <尾签名>`。头尾签名用 `\xNN` 转义或直接写可打印字符。**改这个文件就能支持任意格式**——这是 Scalpel 相对 Foremost 的灵活性所在。
- **最大雕刻长度**：防止一个错误的「头」导致把整盘数据都写成一个巨大文件（**必须设**）。
- **blockmap（覆盖率图）**：一个二进制文件，**第一个 32 位无符号整数是块大小**，之后每个 32 位条目对应镜像里一个块，记录「有多少个雕刻出的文件包含这个块」。用途：① `-u` 实现增量雕刻；② **在报告里说明「我们检查了哪些区域」**（避免「你为什么漏掉了那个文件」的质疑）。
- **`-b`/`-r`（foremost 0.69 兼容模式）**：`-b` 表示「即使没找到尾部也雕出」（类似 foremost 的 `-a`）；`-r` 表示「重叠头只取第一个」。
- **`-p` 预览**：只写审计日志——**和 foremost 的 `-w` 对应**，是「先干跑」的标准技巧。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install scalpel
command -v scalpel
scalpel -h
```

```console
root@kali:~# scalpel -h
Scalpel version 1.60
Written by Golden G. Richard III, based on Foremost 0.69.
Carves files from a disk image based on file headers and footers.

Usage: scalpel [-b] [-c <config file>] [-d] [-h|V] [-i <file>]
                 [-m blocksize] [-n] [-o <outputdir>] [-O num] [-q clustersize]
                 [-r] [-s num] [-t <blockmap file>] [-u] [-v]
                 <imgfile> [<imgfile>] ...
```

最短用法：

```bash
# 1) 先准备配置（默认 /etc/scalpel/scalpel.conf 里大部分类型是注释掉的，必须自己开）
dpkg -L scalpel | grep conf
sudo grep -vE '^\s*#|^\s*$' /etc/scalpel/scalpel.conf | head
```

```console
# 若上面输出为空，说明默认配置里所有类型都被注释了（这是 Scalpel 的设计：默认什么都不雕）
```

```bash
# 2) 解除需要的类型注释（示例：开启 jpg/pdf/zip）
sudo sed -i -E 's/^#\s*(jpg|pdf|zip)\s+/\1 /' /etc/scalpel/scalpel.conf
sudo grep -E '^(jpg|pdf|zip)\s' /etc/scalpel/scalpel.conf
```

```console
jpg	y	20000000	\xff\xd8\xff\xe0\x00\x10	\xff\xd9
pdf	y	50000000	%PDF	%%EOF
zip	y	20000000	\PK\x03\x04	\PK\x05\x06
```

```bash
# 3) 雕刻
sudo scalpel -o /evidence/scalpel-out /evidence/disk.img
```

```console
Scalpel version 1.60
Written by Golden G. Richard III, based on Foremost 0.69.
Opening target "/evidence/disk.img"

Image file size: 256 MB
Output directory: /evidence/scalpel-out
...
Carving done.

Scalpel done.  Time elapsed: 4 seconds.
```

> **最容易踩的坑**：**Scalpel 默认配置里所有类型都是注释掉的**（与 Foremost 不同，Foremost 不指定 `-t` 会雕全部内置类型）。**不配 `scalpel.conf` 就什么也雕不出来**，这是初学者 90% 的困惑来源。

---

## 4. 核心参数详解

以下为 `scalpel -h` 的**完整真实参数**：

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `<imgfile> [...]` | 输入镜像（**可多个**） | 支持同时处理多个镜像 |
| `-c <config file>` | **指定配置文件** | 默认 `scalpel.conf`；强烈建议**每个案件一份专用配置** |
| `-o <outputdir>` | 输出目录 | 每个任务用**全新目录** |
| `-i <file>` | 从文件读取「镜像文件列表」 | 批量处理时用（一个路径一行） |
| `-d` | **生成头/尾签名数据库**；绕过某些优化以发现所有尾部 | **实验性**：性能下降，但能发现被优化跳过的尾部 |
| `-b` | **foremost 0.69 兼容模式**：即使没找到尾部，也在达到最大长度时雕出 | 抢救破损文件；**产出需二次验证** |
| `-r` | **foremost 0.69 兼容：重叠头只取第一个** | 老工具结果复现 |
| `-n` | **不给雕出的文件加扩展名** | 想要「无扩展名文件」时用（一般不用） |
| `-O <num>` | **不按类型分目录**（`-O 1` 时所有文件放一起） | 结果类型少、想平铺时用 |
| `-q <clustersize>` | **只在簇边界上找头**（按簇对齐雕刻） | 对**要求对齐**的格式（如某些图片/视频）减少误报；需知道簇大小 |
| `-s <num>` | **跳过每个镜像开头的 N 字节** | 定向雕刻分区内部（偏移换算） |
| `-m <blocksize>` | **生成/更新雕刻覆盖率 blockmap**（块大小） | 报告「检查范围」；配合 `-t` 指定存放目录 |
| `-t <blockmap file>` | **指定 blockmap 目录** | **实验性**，与 `-m`/`-u` 配合 |
| `-u` | **使用 blockmap：只雕「尚未被任何文件覆盖」的区域** | **增量雕刻**：先雕一种类型，再雕另一种时不重复扫 |
| `-v` | 详细模式 | 排错 |
| `-V` | 显示版权信息并退出 | —— |
| `-h` | 帮助 | —— |

**关于 `-m` / `-u` 的实战意义（这是 Scalpel 最独特的能力）**：

| 用法 | 价值 |
|------|------|
| `-m 512 -t /evidence/bm` | 生成覆盖率图 → **报告可写「本镜像 100% 区域经雕刻检查」** |
| 先雕图片（`-m` 记录），再雕文档（`-u`） | **`-u` 跳过已被图片占用的区域** → 文档雕刻更快、更干净 |
| 多轮雕刻后查看 blockmap | 找出「从未被任何文件覆盖」的区域 → **这些区域值得单独关注**（可能是被安全擦除、加密、或还有未雕出的东西） |

**配置文件格式（`scalpel.conf`）**：

```
# 扩展名  大小写敏感  最大长度   头签名                   尾签名
jpg       y           20000000   \xff\xd8\xff\xe0\x00\x10   \xff\xd9
pdf       y           50000000   %PDF                       %%EOF
doc       y           30000000   \xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1  \x00\x00\x00\x00\x00\x00\x00\x00
zip       y           20000000   \x50\x4b\x03\x04           \x50\x4b\x05\x06
gif       y           10000000   GIF8                       ;
png       y           20000000   \x89PNG                    IEND
```

| 字段 | 含义 | 注意 |
|------|------|------|
| 扩展名 | 输出文件的扩展名 | 自定义格式可写任意名 |
| 大小写敏感 | `y`/`n` | 文本型签名（如 `%PDF`）一般 `y` |
| **最大长度** | 单个文件的字节上限 | **必设**，否则一个假头可能吞掉整盘 |
| 头签名 | 起始字节序列 | 支持 `\xNN`、`\n`、`\t` 等转义 |
| 尾签名 | 结束字节序列 | 有些格式（如 ZIP）有多个可能的尾 |

---

## 5. 实战演练

> **环境声明**：全部使用**自建实验镜像**（生成方法见 [`dcfldd.md` 场景 1](dcfldd.md#场景-1造一个作案现场先有可练的镜像)）或**公开发布的取证样本**（NIST CFReDS）。
> **禁止**对未经授权的镜像或设备执行雕刻。雕刻会大量写盘，**务必输出到独立工作盘**。

### 场景 1：从零配置到第一次成功雕刻（避开「什么都不出」的坑）

**Step 1：确认默认配置状态**

```bash
sudo grep -cE '^\s*#' /etc/scalpel/scalpel.conf
sudo grep -vE '^\s*#|^\s*$' /etc/scalpel/scalpel.conf | wc -l
```

```console
412
0
```

**解读**：**412 行被注释，0 行生效** —— 这就是「跑了半天什么都没雕出来」的典型原因。

**Step 2：为本次任务写一份**专用**配置（**推荐做法，不要改全局文件**）**

```bash
sudo cp /etc/scalpel/scalpel.conf /evidence/scalpel-lab.conf
sudo tee -a /evidence/scalpel-lab.conf > /dev/null <<'EOF'

# ---- 本次案件需要雕出的类型（实验环境）----
jpg     y       20000000        \xff\xd8\xff\xe0\x00\x10      \xff\xd9
png     y       20000000        \x89PNG                       IEND
pdf     y       50000000        %PDF                          %%EOF
zip     y       20000000        \x50\x4b\x03\x04              \x50\x4b\x05\x06
doc     y       30000000        \xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1
txt     y       10000000        \x00\x00\x00\x00
EOF
```

> **注意**：`txt` 没有明确的头尾，上面的写法只是为了演示格式——**真实场景不要把无头尾的格式写进雕刻配置**（会产出大量垃圾）。要提文本用 [`bulk-extractor.md`](bulk-extractor.md) 的 `wordlist` 扫描器或 `strings`。

**Step 3：预览（`-p` 不存在于 scalpel，用 `-v` + 小范围先试）**

Scalpel 没有 `-p` 预览参数；**用「小范围试雕」代替**：

```bash
# 只在未分配空间上试雕（快、干净）
blkls -A -o 2048 /evidence/disk.img > /evidence/unalloc.bin
ls -lh /evidence/unalloc.bin
sudo scalpel -c /evidence/scalpel-lab.conf -o /evidence/scalpel-test /evidence/unalloc.bin
```

```console
Scalpel version 1.60
Opening target "/evidence/unalloc.bin"
Image file size: 96 MB
Output directory: /evidence/scalpel-test
Carving done.
Scalpel done.  Time elapsed: 2 seconds.
```

```bash
ls -R /evidence/scalpel-test
cat /evidence/scalpel-test/audit.txt
```

```console
Scalpel version 1.60
Command line: scalpel -c /evidence/scalpel-lab.conf -o /evidence/scalpel-test /evidence/unalloc.bin
Started at: Sat Sep 15 11:45:02 2024
Completed at: Sat Sep 15 11:45:04 2024
Output directory: /evidence/scalpel-test
Configuration file: /evidence/scalpel-lab.conf

Input file: /evidence/unalloc.bin
File Offset | Carved File Name     | Carved File Size | Header/Footer Found
0            jpg/00000000.jpg       12288            yes/yes
131072       pdf/00000000.pdf       2048             yes/yes
524288       zip/00000001.zip       32768            yes/yes
655360       jpg/00000002.jpg       4096             yes/no
```

**解读（audit.txt 逐列）**：

| 列 | 含义 | 用途 |
|----|------|------|
| `File Offset` | **字节偏移**（注意：Scalpel 直接给字节，不像 Foremost 给 512 块号） | **除以块大小得到块号 → 用 TSK `ifind -d` 反查归属** |
| `Carved File Name` | 输出路径（按类型分子目录） | 定位结果文件 |
| `Carved File Size` | 雕出的字节数 | 与真实大小比对 |
| **`Header/Footer Found`** | **`yes/yes` = 头尾都找到（最可信）**；`yes/no` = 没找到尾（长度截断，可能不完整） | **报告里只把 `yes/yes` 的作为「完整恢复」，`yes/no` 标注为「部分内容」** |

**这是 Scalpel 相对 Foremost 的一个明显优势**：`audit.txt` 直接告诉你每个文件是否找到尾部——**质量判据一目了然**。

```bash
# 验证完整性
file /evidence/scalpel-test/zip/00000001.zip
unzip -t /evidence/scalpel-test/zip/00000001.zip
identify /evidence/scalpel-test/jpg/00000000.jpg 2>/dev/null || file /evidence/scalpel-test/jpg/00000000.jpg
```

```console
No errors detected in compressed data of /evidence/scalpel-test/zip/00000001.zip.
/evidence/scalpel-test/jpg/00000000.jpg: JPEG image data, JFIF standard 1.01, 240x240
```

### 场景 2：覆盖率 blockmap + 增量雕刻（Scalpel 的独门能力）

**为什么需要它**：取证报告最怕被问「你怎么证明你检查了所有区域？」——blockmap 就是这个证明。

```bash
# ① 第一轮：雕图片，同时生成覆盖率图（块大小 512）
mkdir -p /evidence/bm
sudo scalpel -c /evidence/scalpel-jpg.conf \
     -o /evidence/scalpel-r1 -m 512 -t /evidence/bm /evidence/disk.img
ls -l /evidence/bm/
```

```console
-rw-r--r-- 1 root root 524288 Sep 15 12:00 /evidence/bm/disk.img.map
```

**解读**：blockmap 的大小 ≈ 镜像块数 × 4 字节。256 MB 镜像按 512 字节分块 = 524288 块 × 4 字节。

```bash
# ② 第二轮：雕文档，用 -u 只扫「第一轮没覆盖」的区域
sudo scalpel -c /evidence/scalpel-doc.conf \
     -o /evidence/scalpel-r2 -u -m 512 -t /evidence/bm /evidence/disk.img
```

```console
Scalpel version 1.60
Opening target "/evidence/disk.img"
Using coverage blockmap from /evidence/bm/disk.img.map
Skipping already-carved regions...
Carving done.
Scalpel done.  Time elapsed: 1 second.
```

**解读**：**第二轮明显更快**（跳过了已被图片覆盖的区域）。这在实际案件里（几百 GB 镜像、多轮雕刻）能节省大量时间。

```bash
# ③ 找出「从未被任何雕刻文件覆盖」的区域（值得单独关注的盲区）
python3 - <<'EOF'
import struct
p = '/evidence/bm/disk.img.map'
data = open(p,'rb').read()
blk = struct.unpack('<I', data[:4])[0]
entries = struct.unpack(f'<{len(data)//4 - 1}I', data[4:4*((len(data)//4)-1)*1])
zero = [i for i,v in enumerate(entries) if v == 0]
print(f"块大小: {blk} 字节")
print(f"总块数: {len(entries)}")
print(f"未被覆盖块数: {len(zero)} ({len(zero)*100.0/len(entries):.2f}%)")
if zero:
    print(f"未被覆盖起始偏移: {zero[0]*blk} 字节 (0x{zero[0]*blk:x})")
EOF
```

```console
块大小: 512 字节
总块数: 522240
未被覆盖块数: 486144 (93.09%)
未被覆盖起始偏移: 2048 字节 (0x800)
```

**解读**：93% 未被覆盖是**正常的**（大部分区域是文件系统元数据与未雕出的文件类型）。**重点不是百分比，而是「未被覆盖的区域里还有没有别的东西」**——这才是报告里可以写「我们检查了 X 区域，未发现其他可雕刻内容」的依据。

**报告写法示例**：

> 对镜像 `/evidence/disk.img`（256 MB）执行了基于 Scalpel 1.60 的两轮雕刻（JPEG、PDF/ZIP），并使用 512 字节粒度的覆盖率 blockmap 跟踪检查范围。覆盖率图显示 93.09% 的块未被雕刻文件覆盖，主要为文件系统元数据区与未匹配任何配置签名的数据。

### 场景 3：自定义格式 + 簇对齐 + 与 Foremost 交叉验证

**3a. 自定义一个专有格式（举例：某行业日志格式）**

假设你要找的文件以 `LOGSTART` 开头、以 `LOGEND` 结尾：

```bash
sudo tee -a /evidence/scalpel-custom.conf > /dev/null <<'EOF'
# 自定义格式：以 LOGSTART 开头，以 LOGEND 结尾，最大 5MB
mylog   y   5000000   LOGSTART   LOGEND
EOF
sudo scalpel -c /evidence/scalpel-custom.conf -o /evidence/scalpel-custom /evidence/disk.img
sudo grep -c 'yes/yes' /evidence/scalpel-custom/audit.txt
```

```console
7
```

**解读**：自定义签名的能力让 Scalpel 可以处理**任何有明确头尾的格式**（行业日志、嵌入式数据、游戏存档等）。**这是 Foremost 难以做到的**（要改 C 代码或 magic 文件）。

**3b. 簇对齐（`-q`）减少误报**

```bash
fsstat -o 2048 /evidence/disk.img | grep -i 'block size'
```

```console
Block Size: 4096
```

```bash
# 只在 4096 字节边界上找头 → 减少「图片数据里碰巧出现 JPEG 头」的误报
sudo scalpel -c /evidence/scalpel-jpg.conf -q 4096 \
     -o /evidence/scalpel-aligned /evidence/disk.img
```

```console
Scalpel done.  Time elapsed: 3 seconds.
```

```bash
# 对比：对齐 vs 不对齐的结果数量
echo "不对齐: $(ls /evidence/scalpel-r1/jpg | wc -l)"
echo "对齐:   $(ls /evidence/scalpel-aligned/jpg | wc -l)"
```

```console
不对齐: 12
对齐:   7
```

**解读**：**5 个差异就是「未对齐的假阳性」**（往往是某张图片内部嵌了缩略图或另一张图的字节序列）。**对齐雕刻牺牲少量覆盖率换取准确性**——对「文件在磁盘上总是按簇对齐」的常规场景是划算的。

**3c. 交叉验证（两个工具都跑一遍）**

```bash
mkdir -p /evidence/foremost-x
foremost -t jpg,zip,pdf -i /evidence/unalloc.bin -o /evidence/foremost-x
echo "scalpel : $(ls /evidence/scalpel-test/jpg /evidence/scalpel-test/zip /evidence/scalpel-test/pdf 2>/dev/null | wc -l)"
echo "foremost: $(ls /evidence/foremost-x/jpg /evidence/foremost-x/zip /evidence/foremost-x/pdf 2>/dev/null | wc -l)"
```

```console
scalpel : 4
foremost: 4
```

```bash
# 内容级比对（用哈希确认「是否真的是同一个文件」）
sha256sum /evidence/scalpel-test/zip/*.zip /evidence/foremost-x/zip/*.zip
```

```console
a1b2c3...  /evidence/scalpel-test/zip/00000001.zip
a1b2c3...  /evidence/foremost-x/zip/00000000.zip
```

**解读**：**两个独立实现的雕刻器恢复了同一个文件（哈希一致）** → 在报告里，这个结论的可信度显著高于单一工具的产出。

---

## 6. 输出解读

### 6.1 `audit.txt`（Scalpel 的核心证据文件）

| 列 | 含义 | 报告里怎么写 |
|----|------|--------------|
| `Command line` | **完整命令行** | 原样抄进保管链（可复现） |
| `Started/Completed at` | 起止时间 | 说明耗时与操作时间窗 |
| `Configuration file` | 使用的配置 | 说明「用了哪些签名」 |
| `File Offset` | **字节偏移** | ÷ 块大小 = 块号 → TSK `ifind` 反查归属 |
| `Carved File Name` | 输出路径 | 证据文件定位 |
| `Carved File Size` | 字节数 | 与真实大小比对 |
| **`Header/Footer Found`** | `yes/yes`（完整）/ `yes/no`（可能不完整） | **只把 `yes/yes` 写成「完整恢复」** |

### 6.2 blockmap（覆盖率图）

| 用途 | 说明 |
|------|------|
| `-u` 增量雕刻 | 跳过已覆盖区域，提速 |
| 报告「检查范围」 | 证明「我们对全盘/指定区域做了雕刻检查」 |
| 找盲区 | 从未被覆盖的区域值得单独关注（可能被加密/擦除/有未配置的类型） |
| 注意 | 格式是**私有二进制**（首 4 字节为块大小，之后每块一个 32 位计数）；**报告里要说明「本图为工具私有格式」**，别声称它是标准格式 |

### 6.3 完整性判断（**必做**）

| 类型 | 校验命令 | 通过 = 完整 |
|------|----------|-------------|
| ZIP/RAR/7z | `unzip -t` / `7z t` | 内部 CRC 通过（**最强证据**） |
| JPEG/PNG | `identify` / `file` | 能被解码 |
| PDF | `pdfinfo` / `pdftotext` | 结构完整 |
| Office（OLE） | `libreoffice --headless --convert-to txt` | 能打开 |
| 任意 | `sha256sum` | 记录证据校验值 |

---

## 7. 与其他工具配合

```
① 获取镜像：dcfldd / ddrescue / libewf                          dcfldd.md
② 结构：mmls（找分区偏移）→ fsstat（找块大小）                    sleuthkit.md
③ 元数据可用？
   ├─ 可用 → TSK 精确恢复（fls -d / istat / icat / tsk_recover）   sleuthkit.md
   └─ 不可用 / 需兜底 → blkls -A 导出未分配空间
                              │
④ 雕刻（交叉使用两个工具，结果互证）
   ├─ scalpel（本文）：灵活性 + 覆盖率图 + yes/yes 质量标记
   └─ foremost：内置类型全 + -d 间接块拼接                         foremost.md
                              │
⑤ 特征提取（另一条线，不做恢复）：bulk-extractor                  bulk-extractor.md
   └─ 对雕刻结果目录跑 -R 递归扫描，二次提特征
                              │
⑥ 细节：exiftool（图片/文档元数据）                              exiftool.md
⑦ 嵌套结构：binwalk（压缩流/嵌入文件/熵）                          binwalk.md
⑧ 图形复核：autopsy                                               autopsy.md
```

**典型闭环命令**：

```bash
blkls -A -o 2048 disk.img > unalloc.bin
scalpel -c case.conf -o carve-s -m 512 -t bm unalloc.bin      # 覆盖率 + 质量标记
foremost -t jpg,zip,pdf -d -i unalloc.bin -o carve-f          # 交叉验证
bulk_extractor -o bulk -R carve-s                             # 对结果再提特征
sha256sum carve-s/zip/*.zip > hashes.txt                      # 证据校验值
```

- 文件系统精确恢复：[`sleuthkit.md`](sleuthkit.md) ｜ 另一个雕刻器：[`foremost.md`](foremost.md)
- 特征提取：[`bulk-extractor.md`](bulk-extractor.md) ｜ 元数据：[`exiftool.md`](exiftool.md)
- 固件：[`binwalk.md`](binwalk.md) ｜ 图形界面：[`autopsy.md`](autopsy.md) ｜ 获取：[`dcfldd.md`](dcfldd.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| **跑完什么都没雕出来** | `scalpel.conf` 里所有类型都被注释（**默认状态**） | 开启需要的类型，或用 `-c` 指定自定义配置 |
| 配置文件里没有我要的格式 | 内置列表有限 | 按「扩展名/大小写/最大长度/头/尾」格式自行添加 |
| 雕出一个几百 MB 的「文件」 | 头签名误命中，且**最大长度设得太大** | 把最大长度改小（如 20 MB）；用 `-q` 做簇对齐 |
| 结果里全是假阳性 | 未做簇对齐 / 头签名过于宽松 | `-q <clustersize>`；收紧头签名（加更多特征字节） |
| 大文件只有开头 | 碎片化（Scalpel **不做间接块拼接**） | 改用 [`foremost.md`](foremost.md) 的 `-d`（ext 专用）；或先用 TSK 恢复 |
| `Header/Footer Found: yes/no` 很多 | 没找到尾部（数据被截断/覆盖） | 报告里标注为「部分内容」；可试 `-b`（兼容模式）抢救 |
| 输出目录已有内容 | 目录复用 | 每次 `-o` 新目录；或先清理 |
| `Permission denied` | 非 root 或输出目录无权限 | `sudo scalpel ...` |
| blockmap 巨大 | 块大小太小（如 `-m 1`） | 用 512 或 4096 这类与设备扇区/簇一致的大小 |
| `-u` 后什么都没雕 | blockmap 显示区域都已被上一轮覆盖 | 正常（说明上一轮覆盖到了）；换用更小的块大小重做，或换类型 |
| 结果与 Foremost 数量不一致 | 两者的头尾签名定义不同、对齐策略不同 | **交叉验证后以「能被解析器打开」者为准**，并在报告中说明差异 |
| 加密盘里雕不出东西 | 数据加密（高熵，无签名） | 无法雕刻；需先解密 |
| 输出写到证据盘 | 未指定 `-o` 到工作盘 | 永远输出到独立工作盘 |

---

## 9. 防御视角（蓝队 / 应急响应）

| 场景 | Scalpel 的用法 | 价值 |
|------|----------------|------|
| 分区/元数据被破坏 | 直接对镜像雕刻 | TSK 失效时的**兜底恢复能力** |
| 数据外带取证 | 雕 `zip/rar/7z` + `unzip -t` 验证 | 证明「确实打包带走了可读的数据」 |
| 攻击者删除工具 | 雕可执行文件/脚本（需自定义签名） | 恢复攻击工具本体，用于**样本分析**（见 [`../10-逆向工程/README.md`](../10-逆向工程/README.md)） |
| **证明检查范围** | `-m` 生成覆盖率图 | **回应「你为什么漏掉了 X 文件」的质疑** |
| 处理超大镜像 | `-u` 增量雕刻 | 多轮雕刻不重复劳动（几百 GB 场景实用） |
| 敏感格式定向 | 自定义签名（行业专有格式） | 通用工具无法处理时唯一的办法 |
| 完整性论证 | `audit.txt` 的 `yes/yes` + `unzip -t` | 报告可信度 |

**蓝队角度的核心认知（与 [`foremost.md`](foremost.md) 相同但更强调「不可控性」）**：

- **删除 ≠ 销毁**：雕刻能复原 → 唯一的有效控制是**全盘加密 + 安全擦除**；
- **格式化 ≠ 销毁**：元数据被清但数据块通常在 → 雕刻有效；
- **雕刻覆盖不了加密数据**：这也是为什么「全盘加密」是性价比最高的整改项；
- **SSD 的 TRIM 会让雕刻失效**：SSD 上被删除的数据可能已被控制器擦除 → 取证时要注意「TRIM 是否开启」（这本身是需要在报告里说明的技术前提）；
- **有覆盖率图才是专业做法**：报告里写「检查了 X% 的区域、未覆盖区域为 Y」远比「我们跑了雕刻」有说服力。

---

## 10. 参考

- Scalpel 项目（1.60）：<https://github.com/nolaforensix/scalpel-1.60>
- Kali 工具页：<https://www.kali.org/tools/scalpel/>
- 本地文档：`man scalpel`、`scalpel -h`
- NIST CFReDS 公开取证镜像（练习素材）：<https://cfreds.nist.gov/>
- 相关论文：Richard III, G.G. & Roussev, V. *Scalpel: A Frugal, High Performance File Carver*（DFRWS 2005）
- 配置文件位置：`dpkg -L scalpel`（找 `scalpel.conf`）

## ⚠️ 法律与伦理

雕刻出的文件是**完整的原始内容**，可能包含他人照片、聊天记录、文档、凭据与金融信息。未经授权的获取或查看可能触犯：

- 《刑法》第 285 条（非法获取计算机信息系统数据）、**第 253 条之一（侵犯公民个人信息罪）**；
- 《网络安全法》《数据安全法》《个人信息保护法》。

**必须遵守**：

1. **书面授权**：明确授权对象、范围与目的；企业内部调查需有制度依据；
2. **最小必要**：只在必要类型与区域内雕刻（用 `-s`/`-u` 限定、用专门配置只开必需类型），**不做无差别全盘雕刻**；
3. **产出按敏感数据管理**：加密存储、限定人员、访问留痕；**blockmap 与 `unalloc.bin` 同样敏感**；
4. **报告脱敏**：只给统计与脱敏样例，不粘贴私人内容与凭据；
5. **结案销毁**：按约定安全删除所有中间文件与雕刻产物；
6. **不写证据盘**：输出必须落在独立工作盘。

本教程请仅在**自建实验镜像**或 **NIST CFReDS 公开样本**上练习。
