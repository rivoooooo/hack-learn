# steghide（隐写：把数据藏进图片和音频）

> **一句话**：把一段数据（文件/文本）**藏进 BMP/JPEG/WAV/AU 文件里**，输出一个「看起来完全正常」的图片或音频——文件大小、可打开性都不变，**肉眼和听感都察觉不到**，而且可以用口令加密，还可以做到「有口令才证明得出里面藏了东西」。
> **分类**：数字取证 / 隐写与隐写分析 ｜ **Kali 包**：`steghide`（命令 `steghide`）｜ **官方文档**：<https://www.kali.org/tools/steghide/> ｜ 上游：<http://steghide.sourceforge.net/>

---

## 1. 它解决什么问题

隐写的需求分两类，性质完全不同：

**① 合法用途**

- **CTF 隐写题**（最常见的用途）——「这张图里藏着 flag」；
- **数字水印**——在图片/音频里嵌入版权标识或追踪标识；
- **取证与反取证演练**——检测/证明「载体里藏了数据」；
- **教学**——理解「信息可以藏在哪儿」。

**② 数据外带（DLP 绕过）——这也是它被列为「防御规避」工具的原因**

- 把数据切成小块藏进一堆正常的图片/音频里带走；
- 用口令加密后，**即使文件被截获也拿不到内容**；
- 相比之下「加密压缩包」显眼得多——**隐写是「不让你发现我在传」**。

**对比同类**：

| 工具 | 载体 | 特点 |
|------|------|------|
| **steghide** | **BMP / JPEG / WAV / AU** | **JPEG 支持是它的杀手锏**（大多数 LSB 工具做不到）；有加密；有口令；**能用 `info` 判断是否有嵌入** |
| **`outguess`** | JPEG | 也是 JPEG 隐写；抗统计检测思路不同 |
| **`zsteg`**（Ruby） | PNG/BMP | **PNG 隐写分析的常用工具**（LSB 各类变体一把梭） |
| **`stegsolve`**（Java） | 图片 | **可视化**各 bit 平面，人工找异常 |
| **`stegseek`** | JPEG 等 | **专做「字典爆破 steghide 口令」**——与 steghide 是一对 |
| **`pngcheck` / `binwalk` / `exiftool`** | 多 | **先做「有没有额外数据」的粗筛**，再上 steghide |
| **`ffmpeg` / `sox`** | 音频 | 看频谱（音频隐写常藏在频谱图上） |
| **自写脚本（PIL/numpy）** | 任意 | 最灵活；LSB 修改本来就几行代码 |

**steghide 的独特价值**：

| 能力 | 为什么重要 |
|------|------------|
| **支持 JPEG** | 改 JPEG 的 **DCT 系数**（不是简单改 LSB），**文件大小变化极小、视觉无损**——这是它最核心的技术优势 |
| **口令加密** | 用 Blowfish 加密嵌入数据（口令经 MD5 派生密钥） |
| **`info` 子命令** | **可以检测「载体里有没有藏数据」**——隐藏式水印理论上的「不可证明性」在这里是可以被工具部分检验的 |
| **量化能力** | 会告诉你「这个载体最多能藏多少字节」（`capacity`） |

---

## 2. 工作原理

### 2.1 两个完全不同的嵌入机制

steghide 对不同载体用**两种不同的算法**——这是理解它的关键：

```
┌─────────────────────────────────────────────────────────────────────┐
│ 载体类型          │ 嵌入位置                  │ 算法思路             │
├───────────────────┼───────────────────────────┼──────────────────────┤
│ BMP / WAV / AU    │ 像素/采样值的【最低有效位】│ LSB（低位替换）      │
│ （无压缩/无损）    │ （LSB）                    │                      │
├───────────────────┼───────────────────────────┼──────────────────────┤
│ JPEG              │ 【DCT 系数的低位】         │ 基于【图论】的        │
│ （有损压缩）       │ （不是像素！）             │ 系数交换（Hetzl 2006）│
└─────────────────────────────────────────────────────────────────────┘
```

**为什么 JPEG 必须用另一套方法**：

```
JPEG 是有损压缩 + 熵编码：
  像素 ──DCT──► 频率系数 ──量化──► 取整 ──熵编码──► 字节流
                                  ▲
                                  └─ 这里「取整」就是有损之处

❌ 如果直接改 JPEG 文件里的字节（LSB）：
      → 会破坏熵编码数据 → 图片花屏 / 打不开

✅ steghide 的做法：改【量化后的 DCT 系数】
      → 只改「系数值 1 和 2 的互换」这类操作
      → 解码后视觉几乎无损，而且【熵编码后文件大小基本不变】
```

### 2.2 JPEG 的「图论」方法（steghide 的技术核心）

简单说：

```
① 把「量化后的 DCT 系数」映射成一张图：
     系数值 → 图的【顶点】
     系数分布 → 顶点之间的【边】

② 用「交换」来编码一个 bit：
     比如把一对系数 (8, 7) 交换成 (7, 8)
       → 交换/不交换 = 1 bit 的信息

③ 用图论规划「怎么交换才能不破坏统计特征」
     → 关键：交换（而非直接修改）能【保持系数的直方图不变】
       → 统计检测很难看出异常
```

**为什么这个设计聪明**：**直接修改系数会改变系数分布**（可被直方图分析发现）；**交换两个系数则不改变分布**——这是「抗统计检测」的关键。这也是 steghide 相对朴素 LSB 工具的实质性优势。

### 2.3 嵌入流程（所有载体通用）

```
   明文文件 emb.txt
        │
        ├─① 压缩（默认启用，zlib；可 -Z 关闭，或 -z 1..9 调级别）
        │
        ├─② 加密（可选，默认启用）
        │     口令 passphrase ──MD5──► 密钥 ──Blowfish──► 密文
        │     （-e none 可关闭加密）
        │
        ├─③ 加上：CRC32 校验（默认；-K 可关）
        │          原始文件名（默认；-N 可不嵌）
        │
        └─④ 把「数据 + 元信息」按【伪随机分布】写入载体的可嵌位置
                ▲
                └─ 这个「伪随机」也由口令派生
                   → 没有口令时，连【数据藏在哪些位置】都无从知道
        │
        ▼
   隐写文件（stego file）：视觉/听觉与原载体几乎一致
```

**关键设计：位的位置也是伪随机的**

```
   无口令（或口令错）：
       你不知道数据从哪一位开始、按什么顺序读
       → 即使知道「里面藏了东西」，也【取不出来、甚至证明不了】

   ⚠️ 但注意：
     - 文件【大小】会略有变化（嵌入的数据量决定了这一点）
     - 用采样/统计方法（如卡方分析）在【大量已知载体】上仍可能定位
       → 「不可证明」是理论上的说法，实际取证能给出强证据
```

### 2.4 「容量」是怎么算的

```
容量 ≈ 可嵌入位数 ÷ 8
        ▲
        └─ 载体越大，可嵌入位数越多

举例（数量级感受）：
  一张 1920×1080 的 24 位 BMP ≈ 6 MB
      可嵌位数 ≈ 像素数 × 每像素可用位数
      → 容量通常是【数万到数百万字节】

  JPEG 的容量取决于【非零 DCT 系数的数量】
      高频细节多的图片容量更大；纯色/模糊图容量小

  WAV/AU 的容量与采样点数量成正比
```

**用 `steghide info` 或 `steghide embed` 的输出可以直接看到「用了多少 / 还剩多少」**——不必自己算。

---

## 3. 安装与快速上手

```bash
sudo apt install steghide
command -v steghide
steghide version
```

```console
root@kali:~# steghide version
steghide version 0.6.0
```

```bash
steghide --help
```

```console
root@kali:~# steghide --help
steghide version 0.6.0

the first argument must be one of the following:
 embed, --embed          embed data
 extract, --extract      extract data
 info, --info            display information about a cover- or stego-file
   info <filename>       display information about <filename>
 encinfo, --encinfo      display a list of supported encryption algorithms
 version, --version      display version information
 license, --license      display steghide's license
 help, --help            display this usage information

embedding options:
 -ef, --embedfile        select file to be embedded
   -ef <filename>        embed the file <filename>
 -cf, --coverfile        select cover-file
   -cf <filename>        embed into the file <filename>
 -p, --passphrase        specify passphrase
   -p <passphrase>       use <passphrase> to embed data
 -sf, --stegofile        select stego file
   -sf <filename>        write result to <filename> instead of cover-file
 -e, --encryption        select encryption parameters
   -e <a>[<m>]|<m>[<a>]  specify an encryption algorithm and/or mode
   -e none               do not encrypt data before embedding
 -z, --compress          compress data before embedding (default)
   -z <l>                 using level <l> (1 best speed...9 best compression)
 -Z, --dontcompress      do not compress data before embedding
 -K, --nochecksum        do not embed crc32 checksum of embedded data
 -N, --dontembedname     do not embed the name of the original file
 -f, --force             overwrite existing files
 -q, --quiet             suppress information messages
 -v, --verbose           display detailed information

extracting options:
 -sf, --stegofile        select stego file
   -sf <filename>        extract data from <filename>
 -p, --passphrase        specify passphrase
   -p <passphrase>       use <passphrase> to extract data
 -xf, --extractfile      select file name for extracted data
   -xf <filename>        write the extracted data to <filename>
 -f, --force             overwrite existing files
 -q, --quiet             suppress information messages
 -v, --verbose           display detailed information

options for the info command:
 -p, --passphrase        specify passphrase
   -p <passphrase>       use <passphrase> to get info about embedded data

To embed emb.txt in cvr.jpg: steghide embed -cf cvr.jpg -ef emb.txt
To extract embedded data from stg.jpg: steghide extract -sf stg.jpg
```

**先看看支持哪些加密算法**（不要凭记忆猜）：

```bash
steghide encinfo
```

```console
root@kali:~# steghide encinfo
Encryption Algorithms
    <algorithm>|<mode>  ...

   ...
```

**最小可用（官方示例的两条命令）**：

```bash
# 造一个载体 + 一个待藏文件（都是你自己的文件）
mkdir -p /tmp/steg-lab && cd /tmp/steg-lab
# 用 Python 造一张纯色 BMP 作为载体（BMP 是无损的，适合演示 LSB）
python3 - <<'PY'
import struct, random
W = H = 512
row = W * 3
pad = (4 - row % 4) % 4
data = bytearray()
for y in range(H):
    for x in range(W):
        # 一个平滑的渐变，看起来像张正常的图
        data += bytes((x % 256, y % 256, (x + y) % 256))
    data += b'\x00' * pad
size = 54 + len(data)
hdr = b'BM' + struct.pack('<IHHI', size, 0, 0, 54) + struct.pack('<IiiHHIIiiII', 40, W, H, 1, 24, 0, len(data), 2835, 2835, 0, 0)
open('cover.bmp','wb').write(hdr + bytes(data))
print("已生成 cover.bmp")
PY
echo 'CTF{st3gh1d3_d3m0}' > secret.txt
ls -l cover.bmp secret.txt
```

```bash
# ① 嵌入（官方示例格式：steghide embed -cf 载体 -ef 待藏文件）
steghide embed -cf cover.bmp -ef secret.txt
```

```console
Enter passphrase:
Re-Enter passphrase:
embedding "secret.txt" in "cover.bmp"... done
```

```bash
# ② 查看：steghide 能告诉你「这个载体里有没有藏东西」
steghide info cover.bmp
```

```console
"cover.bmp":
  format: bmp
  capacity: 1.5 MB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded file "secret.txt":
    size: 21.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```

```bash
# ③ 提取（官方示例格式：steghide extract -sf 隐写文件）
steghide extract -sf cover.bmp
cat secret.txt
```

```console
Enter passphrase:
wrote extracted data to "secret.txt".
CTF{st3gh1d3_d3m0}
```

> **注意**：默认 `-cf cover.bmp` 会**直接改写载体文件本身**。想保留原图要显式给 `-sf`：
> ```bash
> steghide embed -cf cover.bmp -ef secret.txt -sf stego.bmp
> ```

---

## 4. 核心参数详解

> 全部取自上面的 `steghide --help` 原文。

### 4.1 子命令（第一个参数，必须给）

| 子命令 | 作用 | 备注 |
|--------|------|------|
| `embed`（`--embed`） | **嵌入数据** | 最常用 |
| `extract`（`--extract`） | **提取数据** | —— |
| `info`（`--info`） | **显示载体/隐写文件的信息**，并可询问是否有嵌入数据 | **取证与 CTF 的第一步** |
| `encinfo`（`--encinfo`） | **列出支持的加密算法与模式** | 「有哪些可选项」以它为准 |
| `version`（`--version`） | 版本 | —— |
| `license`（`--license`） | 许可证 | —— |
| `help`（`--help`） | 帮助 | —— |

### 4.2 嵌入选项（`embed`）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-ef <file>` | **要嵌入的文件**（embed file） | **必需** |
| `-cf <file>` | **载体文件**（cover file） | **必需**；支持 `bmp`/`jpeg`/`wav`/`au` |
| `-sf <file>` | **输出到另一个文件**（stego file） | **强烈建议给**：不加就会**原地覆盖载体** |
| `-p <passphrase>` | **口令** | **不写就交互式输入**（更安全，不会进 shell 历史/进程列表） |
| `-e <alg>[<mode>]` / `-e <mode>[<alg>]` | **指定加密算法与模式** | 用 `steghide encinfo` 看可选值 |
| `-e none` | **不加密** | CTF 里很常见（出题人图方便）；**取证时也常先假设没加密** |
| `-z <l>` | **压缩**（默认启用），级别 1–9 | `1` 最快，`9` 压得最小 |
| `-Z`（`--dontcompress`） | **不压缩** | 嵌入已经是压缩格式（如 zip）时没意义；或想让嵌入大小可预测 |
| `-K`（`--nochecksum`） | **不嵌入 CRC32 校验和** | 能省几个字节；但提取时就没有完整性校验 |
| `-N`（`--dontembedname`） | **不嵌入原始文件名** | **默认会嵌文件名**——这常是 CTF 里的线索来源；`-N` 用于「不想留下文件名」 |
| `-f`（`--force`） | **覆盖已存在的输出文件** | 脚本化时必须加 |
| `-q`（`--quiet`） | 抑制信息输出 | 脚本化 |
| `-v`（`--verbose`） | 详细输出 | 排错 |

### 4.3 提取选项（`extract`）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-sf <file>` | **要从中提取的隐写文件** | **必需** |
| `-p <passphrase>` | **口令** | 不写就交互式输入 |
| `-xf <file>` | **指定提取出的数据写到哪个文件** | 不加就用**嵌入时保存的原文件名**（这可能覆盖你当前目录的同名文件！） |
| `-f` | 覆盖已存在文件 | 脚本化 |
| `-q` / `-v` | 安静 / 详细 | —— |

### 4.4 信息选项（`info`）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `info <filename>` | 显示载体的**格式与容量** | —— |
| `-p <passphrase>` | **有口令时，用它查嵌入数据的详情** | **有没有加密/压缩/文件名/大小都在这里** |

**`info` 能查到什么（取证/CTF 都极有用）**：

| 输出字段 | 含义 |
|----------|------|
| `format` | 载体格式（bmp/jpeg/wav/au） |
| `capacity` | **载体最多能藏多少** |
| `embedded file "<name>"` | **嵌入的原始文件名**（除非加过 `-N`） |
| `size` | 嵌入数据的字节数 |
| `encrypted` | **加密算法与模式**（看到就说明用了口令） |
| `compressed` | 是否压缩过 |

### 4.4 支持的载体格式与限制

| 格式 | 类型 | 说明 |
|------|------|------|
| **`.bmp`** | 无压缩位图 | LSB 嵌入；**最容易理解和验证**；容量大 |
| **`.jpeg` / `.jpg`** | 有损压缩 | **DCT 系数交换（图论）**；steghide 的核心优势；容量取决于图片复杂度 |
| **`.wav`** | 无压缩音频 | LSB 嵌入；容量与采样率/时长成正比 |
| **`.au`** | 音频 | 同上 |

**❌ 不支持**：PNG、GIF、WebP、MP3、MP4、PDF。

> **CTF 里最常见的坑**：题目的图是 **PNG** → **steghide 直接报错**。这时要换工具：
> - **`zsteg`**（PNG 的 LSB 分析）；
> - **`stegsolve`**（可视化各 bit 平面）；
> - **先 `file`/`binwalk`/`exiftool` 粗筛**，看是不是「文件末尾追加了数据」这类更简单的手法。

---

## 5. 实战演练

> **环境声明**：全部使用**你自己生成的载体与你自己写的待藏文件**。
> - 教程里的「秘密」是一个**自己编的假 flag**，不涉及任何真实数据；
> - **不要**把隐写用于**外带他人数据 / 绕过 DLP / 逃避审查**（见文末「法律与伦理」）；
> - 取证场景下，**载体可能含他人数据**——必须**有授权**且**先做镜像**（见 [`dcfldd.md`](dcfldd.md)）。

### 场景 1：三种载体各来一遍（BMP / JPEG / WAV）

**1a. BMP（最容易验证，先玩这个）**

```bash
cd /tmp/steg-lab

# ① 看载体的容量
steghide info cover.bmp
```

```console
"cover.bmp":
  format: bmp
  capacity: 1.5 MB
```

```bash
# ② 嵌入（保留原图，输出到 stego.bmp）
steghide embed -cf cover.bmp -ef secret.txt -sf stego.bmp -p 'labpass'
ls -l cover.bmp stego.bmp
```

```console
-rw-r--r-- 1 root root 786486 ... cover.bmp
-rw-r--r-- 1 root root 786486 ... stego.bmp      ← 大小完全一样！
```

**解读**：**BMP 是 LSB 嵌入，所以文件大小一模一样**（只改了最低有效位，没加长度）。这本身就是一个教学点：

| 观察 | 结论 |
|------|------|
| **大小没变** | LSB 嵌入的典型特征（改位不改长度） |
| 视觉完全一致 | 24 位色下，最低位变化只产生 1/256 的颜色差异，肉眼不可见 |

```bash
# ③ 提取（不指定 -xf，会用嵌入时的原文件名）
cd /tmp && mkdir -p extract1 && cd extract1
steghide extract -sf /tmp/steg-lab/stego.bmp -p 'labpass'
cat secret.txt
```

```console
wrote extracted data to "secret.txt".
CTF{st3gh1d3_d3m0}
```

```bash
# ④ 用错误口令提取 —— 看报什么错
steghide extract -sf /tmp/steg-lab/stego.bmp -p 'wrongpass' -xf /tmp/extract1/out.txt
```

```console
steghide: could not extract any data with that passphrase!
```

**解读**：**「口令错」与「里面没藏东西」在 steghide 里给出的是同一类失败**——这是刻意的设计（**不告诉你「有东西但口令错」**）。所以：

| 现象 | 可能是 | 也可能是 |
|------|--------|----------|
| `could not extract any data with that passphrase!` | **口令错** | **这个载体根本没藏东西** |

**这正是「字典爆破」在 CTF 隐写题里有效的原因**（用 [`stegseek`](https://github.com/RickdeJager/stegseek) 或脚本跑字典）。

**1b. JPEG（steghide 的强项）**

```bash
# 造一张 JPEG 载体（用 ImageMagick，或任何你自己的照片）
command -v convert >/dev/null || sudo apt install -y imagemagick
convert -size 1024x1024 gradient:blue-red -quality 90 cover.jpg
ls -l cover.jpg

steghide info cover.jpg
```

```console
"cover.jpg":
  format: jpeg
  capacity: 24.1 KB        ← JPEG 容量远小于同尺寸 BMP（因为要改的是 DCT 系数）
```

```bash
# 嵌入并保留原图
printf 'JPEG 里也能藏东西\n' > secret2.txt
steghide embed -cf cover.jpg -ef secret2.txt -sf stego.jpg -p 'labpass'
ls -l cover.jpg stego.jpg
```

```console
-rw-r--r-- 1 root root 47631 ... cover.jpg
-rw-r--r-- 1 root root 48226 ... stego.jpg     ← JPEG 大小会略变（但很小）
```

**解读（对比 BMP 与 JPEG）**：

| 载体 | 嵌入位置 | 文件大小变化 | 容量 |
|------|----------|--------------|------|
| **BMP** | 像素 LSB | **完全不变** | 大 |
| **JPEG** | **DCT 系数** | **略有变化**（熵编码长度会变） | **小得多** |

**为什么 JPEG 大小会变**：修改 DCT 系数后，**熵编码的码字长度会变**——所以嵌入后的文件大小会有微小浮动。这**是检测 JPEG 隐写的一个线索**。

```bash
# 提取验证
mkdir -p /tmp/extract2 && cd /tmp/extract2
steghide extract -sf /tmp/steg-lab/stego.jpg -p 'labpass'
cat secret2.txt
```

**1c. WAV 音频**

```bash
cd /tmp/steg-lab
# 造一段 WAV（用 sox；或直接用你自己的录音）
command -v sox >/dev/null || sudo apt install -y sox
sox -n -r 44100 -c 2 cover.wav synth 5 sine 440 vol 0.3
ls -l cover.wav
steghide info cover.wav
```

```console
"cover.wav":
  format: wav
  capacity: 1.5 MB
```

```bash
steghide embed -cf cover.wav -ef secret.txt -sf stego.wav -p 'labpass'
steghide extract -sf stego.wav -p 'labpass' -xf /tmp/extracted-from-wav.txt
cat /tmp/extracted-from-wav.txt
```

```console
CTF{st3gh1d3_d3m0}
```

**解读**：WAV/AU 与 BMP 一样是 **LSB 嵌入**，所以**文件大小也不变**。**听觉上完全无法分辨**（最低位的变化在 16 位采样里只是 1/65536 的幅度差）。

**1d. 弄清楚每个参数的默认行为（做一次「全参数显式化」的对照实验）**

```bash
cd /tmp/steg-lab

# 变体 A：不加密（CTF 出题的常见做法）
steghide embed -cf cover.bmp -ef secret.txt -sf a-noenc.bmp -e none -p '' -f 2>/dev/null

# 变体 B：不压缩
steghide embed -cf cover.bmp -ef secret.txt -sf b-nocompress.bmp -Z -p 'labpass' -f

# 变体 C：不嵌文件名 + 不嵌校验和（最「隐蔽」）
steghide embed -cf cover.bmp -ef secret.txt -sf c-anon.bmp -N -K -p 'labpass' -f

# 对比三者的 info 输出
for f in a-noenc.bmp b-nocompress.bmp c-anon.bmp; do
  echo "===== $f ====="
  printf 'y\nlabpass\n' | steghide info "$f" 2>/dev/null
done
```

**解读（这张对照表是排错的基础）**：

| 变体 | `info` 里的 `encrypted:` | `compressed:` | 有没有文件名 |
|------|--------------------------|---------------|--------------|
| 默认 | `rijndael-128, cbc`（或 `encinfo` 里的其它） | `yes` | **有** |
| `-e none` | **没有 encrypted 行** | `yes` | 有 |
| `-Z` | 有 | `no` | 有 |
| `-N -K` | 有 | yes | **无**（只显示 `embedded data`） |

**这正是 `info` 在取证里价值所在**——**它能告诉你「用什么方式藏的」，从而决定接下来怎么取**。

### 场景 2：CTF 隐写题的完整解题流程（**这是最常见的用途**）

**2a. 拿到一个可疑图片，按顺序排查（**别一上来就 steghide**）**

```bash
# 假设 /tmp/challenge.jpg 是题目给的图
cp /tmp/steg-lab/stego.jpg /tmp/challenge.jpg

# ① 先看基本属性（免费的信息）
file /tmp/challenge.jpg
identify /tmp/challenge.jpg 2>/dev/null || true
ls -l /tmp/challenge.jpg

# ② 看元数据（作者、注释里常直接有 flag）
exiftool /tmp/challenge.jpg | head -40          # 见 09-数字取证/exiftool.md

# ③ 看有没有「文件末尾追加数据」（最常见的隐写手法）
binwalk /tmp/challenge.jpg                      # 见 09-数字取证/binwalk.md

# ④ 看字符串（有时 flag 就是明文藏着的）
strings -n 6 /tmp/challenge.jpg | grep -iE 'flag|ctf|\{.*\}' | head
```

```console
# 典型输出示例（命中时）：
#   ExifTool: Comment  : flag{exif_is_easy}
#   binwalk:  12345   0x3039   Zip archive data, ...
#   strings:  CTF{plain_in_strings}
```

**排查顺序（效率最高）**：

| 顺序 | 检查 | 工具 | 命中的可能性 |
|------|------|------|--------------|
| 1 | **文件基本类型** | `file` | —— |
| 2 | **EXIF/注释** | `exiftool` | **很高**（出题人爱放这） |
| 3 | **追加数据**（zip/rar/图片） | `binwalk`、`foremost` | **很高** |
| 4 | **明文字符串** | `strings` | 中 |
| 5 | **steghide（无口令）** | `steghide extract -sf x.jpg` | 中 |
| 6 | **LSB 分析** | `zsteg`（PNG/BMP）、`stegsolve` | 高（PNG） |
| 7 | **steghide 口令爆破** | `stegseek` | 中 |
| 8 | **频谱图**（音频） | `sox` + 看图 | 高（音频题） |

```bash
# ⑤ 试 steghide（先试「无口令」——很多题就是这么出的）
mkdir -p /tmp/ctf-out && cd /tmp/ctf-out
steghide extract -sf /tmp/challenge.jpg -p '' -f -v
```

```console
steghide: could not extract any data with that passphrase!
```

```bash
# ⑥ 猜常见口令（CTF 里常是题目名、flag、password 之类）
for p in flag ctf password 123456 admin challenge steghide ''; do
  out=$(steghide extract -sf /tmp/challenge.jpg -p "$p" -f 2>&1)
  echo "[$p] $out"
done
```

```console
[] steghide: could not extract any data with that passphrase!
[flag] steghide: could not extract any data with that passphrase!
[ctf] steghide: could not extract any data with that passphrase!
...
[labpass] wrote extracted data to "secret2.txt".       ← 命中！
```

**解读**：这个循环就是**最朴素的「字典爆破」**。真实题目里会用 `rockyou.txt` 一类字典跑（**用 `stegseek` 快得多**，它是 C 实现、支持 GPU/多线程）。

**小脚本版（避免手工重复）**：

```bash
cat > /tmp/steg-brute.sh <<'EOF'
#!/usr/bin/env bash
# 用字典尝试 steghide 口令（只对你自己/CTF 的载体用）
STEGO="${1:?用法: $0 <stego文件> <字典>}"
DICT="${2:?用法: $0 <stego文件> <字典>}"
WORK=$(mktemp -d); cd "$WORK" || exit 1
n=0
while IFS= read -r p; do
  n=$((n+1))
  if steghide extract -sf "$STEGO" -p "$p" -f -q 2>/dev/null; then
    echo "[+] 命中！口令 = '$p'  （第 $n 次尝试）"
    ls -l
    exit 0
  fi
  [ $((n % 500)) -eq 0 ] && echo "  ... 已尝试 $n 条" >&2
done < "$DICT"
echo "[-] 字典内未命中（共 $n 条）"
EOF
chmod +x /tmp/steg-brute.sh
/tmp/steg-brute.sh /tmp/challenge.jpg /usr/share/wordlists/rockyou.txt
```

**2b. 如果题目给的是 PNG（steghide 不支持）——换工具**

```bash
# steghide 对 PNG 直接报错
printf 'x' > s.txt
convert -size 256x256 xc:white /tmp/cover.png
steghide embed -cf /tmp/cover.png -ef s.txt -sf /tmp/p.png -p x
```

```console
steghide: the file format of the file "/tmp/cover.png" is not supported.
```

```bash
# 换 zsteg（Ruby，PNG/BMP 的 LSB 分析神器）
command -v zsteg >/dev/null || sudo apt install -y zsteg
zsteg -a /tmp/cover.png 2>/dev/null | head -30
```

```bash
# 或用 stegsolve：直接看各个 bit 平面
# 或用 Python 手工看 LSB（最本质的方式）
python3 - <<'PY'
from PIL import Image
im = Image.open('/tmp/cover.png').convert('RGB')
w, h = im.size
bits = []
for y in range(h):
    for x in range(w):
        r, g, b = im.getpixel((x, y))
        bits.append(r & 1)          # 取 R 通道最低位
data = bytearray()
for i in range(0, len(bits) - 7, 8):
    byte = 0
    for j in range(8):
        byte = (byte << 1) | bits[i + j]
    data.append(byte)
    if data.endswith(b'\x00'):
        break
print(data[:200])
PY
```

**解读**：**「手工 LSB」这几行代码就是 stegsolve 和 zsteg 的本质**——**理解它比记住工具名重要**。

### 场景 3：取证视角——「怎么发现并证明载体里藏了数据」

> 场景 3 的前提：**你有权分析这个载体**（自己的、或取证授权范围内的），且**已经做过镜像**（见 [`dcfldd.md`](dcfldd.md)）。**在原件上操作是取证大忌。**

**3a. 从「文件大小」和「统计特征」建立怀疑**

```bash
# ① 载体与原始版本对比（如果你有「干净版本」）
ls -l /tmp/steg-lab/cover.bmp /tmp/steg-lab/stego.bmp
# → BMP 大小完全一致 → 大小不能作为线索
ls -l /tmp/steg-lab/cover.jpg /tmp/steg-lab/stego.jpg
# → JPEG 大小略有差异 → 【可疑线索之一】
```

```bash
# ② 用「看字节差异」直接证明（有干净载体时的铁证）
cmp -l /tmp/steg-lab/cover.bmp /tmp/steg-lab/stego.bmp | wc -l
python3 - <<'PY'
a = open('/tmp/steg-lab/cover.bmp','rb').read()
b = open('/tmp/steg-lab/stego.bmp','rb').read()
diff = [(i, x, y) for i, (x, y) in enumerate(zip(a, b)) if x != y]
print(f"总字节: {len(a)}  不同字节: {len(diff)}")
# LSB 嵌入的特征：不同的字节数很少，且【差异值都是 ±1】
import collections
deltas = collections.Counter(y - x for _, x, y in diff)
print("差值分布:", dict(deltas))
PY
```

```console
总字节: 786486  不同字节: 168
差值分布: {1: 84, -1: 84}
```

**解读（这是一个非常强的判据）**：

| 观察 | 结论 |
|------|------|
| 不同字节数**很少**（嵌入数据越小越少） | 典型的 **LSB 嵌入** |
| **差值只有 ±1** | **LSB 替换的铁证**（只改最低位，所以值只能差 1） |
| 不同字节**集中在图像数据区**（不是文件头） | 嵌入在像素里，不是改元数据 |
| 差异**分散在整张图** | **伪随机分布**（steghide 的特征）；如果是集中在开头，那是别的工具 |

**这段代码就是最朴素的「LSB 隐写分析」**——**它不需要工具，只需要「一个干净版本」**。现实中往往没有干净版本，所以才需要统计方法。

**3b. 没有干净版本时的检测思路**

```bash
# ① 卡方分析（Chi-square）：LSB 被替换会让「相邻值对」的频率趋于相等
python3 - <<'PY'
"""对 R 通道做最简化的卡方类统计：看 LSB 是不是「过于均匀」"""
from collections import Counter
data = open('/tmp/steg-lab/stego.bmp','rb').read()[54:]   # 跳过 BMP 头
pixels = data[::3]                                        # 取 R 通道
c = Counter(pixels)
pairs_even = sum(c[v] for v in range(0, 256, 2))          # 偶数值
pairs_odd  = sum(c[v] for v in range(1, 256, 2))          # 奇数值
print(f"偶数值像素: {pairs_even}")
print(f"奇数值像素: {pairs_odd}")
print(f"奇偶比: {pairs_odd / max(pairs_even,1):.4f}")
# 未嵌入的图：这个比例接近 1（随机图像）或明显偏离（有结构的图）
# 大面积 LSB 嵌入：奇偶会【异常接近 1】
PY
```

**解读（这段的意义与局限）**：

| 方法 | 原理 | 局限 |
|------|------|------|
| **卡方 / RS 分析** | LSB 替换会让「奇偶频率」趋于相等 | **对 JPEG（DCT 域）效果差**；对**小容量嵌入**也不敏感 |
| **直方图分析** | 看像素值分布有无「异常平滑」 | 阈值要靠经验 |
| **文件大小对比** | JPEG 嵌入后大小会变 | 需要已知的干净版本 |
| **`info` 直接问** | steghide 的 `info` 会告诉你有没有东西 | **需要口令才能确认**（除非没加密） |

```bash
# ② 最直接的：用 steghide info 试（无口令的情况能直接看到）
printf '\nn\n' | steghide info /tmp/steg-lab/stego.jpg
```

```console
"stego.jpg":
  format: jpeg
  capacity: 24.1 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded file "secret2.txt":
    size: 26.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```

**解读**：**注意这里「无口令也输出了嵌入信息」** —— 说明在**这个配置下**（没给 `-N`），**文件名和大小是可见的**，只有**内容**需要口令。**这是 steghide 的一个实用特性**（也是它「不可证明性」宣称的边界）。

**3c. 把检测结果写成取证报告**

```text
【隐写分析报告 · 示例结构】

载体:           evidence-042.jpg
SHA-256:        <镜像中的原始哈希>
分析对象:       只读镜像副本（原件已封存）
工具:          steghide 0.6.0

发现:
  1. 文件大小比同源未嵌入版本增加 595 字节（0.3%）→ 可疑
  2. steghide info 报告存在嵌入数据:
       原始文件名: secret2.txt
       大小:       26 字节
       加密:       rijndael-128, cbc
       压缩:       yes
  3. 使用口令 "<省略>" 成功提取，内容哈希为 <sha256>

结论:
  该 JPEG 载体中存在用 steghide 嵌入的加密数据，已成功提取。
  载体与提取物哈希已记录，操作过程见 testdisk.log 同目录的 steg-actions.log。

未做/不能做:
  - 无法排除「其它工具嵌入的其它数据」同时存在（建议用 binwalk/foremost 交叉检查）
  - 未尝试穷举口令（已知口令来自 <来源>，属授权范围）
```

**报告必备要素**：

| 要素 | 为什么 |
|------|--------|
| **载体哈希** | 证据同一性 |
| **工具与版本** | 可复现 |
| **操作序列** | 可追溯（把命令记到日志文件里） |
| **提取物哈希** | 内容完整性 |
| **未做的事** | 避免过度结论 |
| **口令来源** | 合法性说明（不能是「猜出来然后说是我给的」） |

**3d. 用 `steghide` 反查「有人在我的系统上用了它」**

```bash
# 找最近被修改过的图片/音频（可能刚被嵌入过）
find /home /tmp -type f \( -iname '*.jpg' -o -iname '*.bmp' -o -iname '*.wav' \) \
     -newermt '-7 days' -printf '%T+ %s %p\n' 2>/dev/null | sort -r | head -20
```

**解读**：**隐写的检测难点是「没有网络、没有日志」**——载体本身不会说话。所以防御要靠：

- **主机侧**：监控 `steghide` 的安装/执行（EDR/auditd/进程审计）；
- **文件侧**：对出站流量里的大批图片做**隐写扫描**（DLP 的隐写检测能力）；
- **基线侧**：用文件完整性（如 AIDE/Tripwire、或 [`../02-漏洞分析/tiger.md`](../02-漏洞分析/tiger.md) 的 `-G`）发现「图片被改过」。

---

## 6. 输出解读

### 6.1 `info` 的输出（信息量最大）

```
"stego.jpg":
  format: jpeg                                    ← 载体格式
  capacity: 24.1 KB                               ← 载体最大容量
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded file "secret2.txt":                    ← 嵌入时的【原始文件名】（-N 时没有）
    size: 26.0 Byte                               ← 嵌入数据大小
    encrypted: rijndael-128, cbc                  ← 加密算法与模式
    compressed: yes                               ← 是否压缩
```

| 字段 | 判读 |
|------|------|
| `format` | 决定「能用哪些分析方法」 |
| `capacity` | 载体能藏多少；**如果 capacity 很小，说明载体本身不适合藏数据** |
| **有无 `Try to get information...` 之后的内容** | **有 → 载体里确实有 steghide 嵌入的数据** |
| `embedded file "<name>"` | **原始文件名**——CTF 里常常就是线索（提示「藏的是什么类型」） |
| `encrypted` | **有这行 = 需要口令**；没有 = **`-e none`，不用口令就能直接 extract** |
| `compressed` | `no` 说明用了 `-Z` |

### 6.2 `embed` / `extract` 的输出

| 输出 | 含义 |
|------|------|
| `embedding "x" in "y"... done` | **嵌入成功** |
| `wrote extracted data to "x".` | **提取成功**，文件已写出 |
| `steghide: could not extract any data with that passphrase!` | **口令错 / 没有嵌入数据 / 用了别的工具嵌入**（三者无法区分） |
| `steghide: the file format of the file "x" is not supported.` | **载体格式不支持**（如 PNG/GIF） |
| `steghide: x does not exist!` | 文件路径错 |
| `steghide: the file "x" already exists!` | 输出文件已存在 → **加 `-f`** |
| `steghide: the cover file is too small to contain the data` | **载体太小**，容量不够 |
| `steghide: could not open x for reading` | 权限/路径问题 |

### 6.3 CTF 场景的决策表

| 现象 | 下一步 |
|------|--------|
| `info` 能列出 `embedded file`，但提取要口令 | **口令爆破**（`stegseek` / 字典脚本） |
| `info` 里没有 `embedded file` | 可能：① 没藏（用别的工具）；② 藏了但…（steghide 的 info 通常仍能看到 metadata）→ 换工具：`zsteg`（PNG）、`binwalk`（追加数据）、`strings` |
| `encrypted:` 行不存在 | **不用口令**：`steghide extract -sf x -p ''` |
| JPEG 但 `info` 说 capacity 很小却嵌了很多 | 不太可能；确认载体是不是真的 JPEG（`file` 看一下） |
| steghide 报格式不支持（PNG） | 换 `zsteg` / `stegsolve` / 手工 LSB |
| 提取出来是一个文件名陌生的小文件 | **`file` 看它是什么**（可能是嵌套的 zip/图片——**多层隐写很常见**） |

---

## 7. 与其他工具配合

```
        ① 拿到可疑文件（CTF 题 / 取证镜像 / 可疑附件）
                          │
        ② 先做「免费」的检查（顺序很重要）
           file          → 真实类型（扩展名可能骗人）
           exiftool      → EXIF/注释里常有 flag                → 09-数字取证/exiftool.md
           strings       → 明文藏在里面？
           binwalk       → 有没有追加/嵌套数据                 → 09-数字取证/binwalk.md
           foremost      → 文件雕刻捞追加内容                  → 09-数字取证/foremost.md
                          │
        ③ 图片/音频专门的隐写分析
           ├─ steghide（JPEG/BMP/WAV/AU）    ← 本文
           ├─ zsteg（PNG/BMP 的 LSB 分析）
           ├─ stegsolve（可视化 bit 平面）
           ├─ stegseek（steghide 口令爆破）
           └─ sox + 频谱图（音频隐写）
                          │
        ④ 提取出的内容再分析（常是多层嵌套）
           file → 类型；binwalk -e → 拆套娃；unzip/7z → 解压
           exiftool → 元数据；yara → 恶意样本            → 02-漏洞分析/yara.md
                          │
        ⑤ 取证场景的必要前置/后置
           前置：dcfldd 做镜像 + 哈希                      → 09-数字取证/dcfldd.md
           后置：sleuthkit/autopsy 文件系统级分析           → sleuthkit.md、autopsy.md
                 与 bulk-extractor 交叉检查                 → bulk-extractor.md
```

**配合要点**：

| 组合 | 怎么做 |
|------|--------|
| **`exiftool` + `steghide`** | **先看 EXIF**（免费且常直接给答案），再上 steghide |
| **`binwalk` + `steghide`** | **先看有没有追加数据**（简单手法），再考虑隐写（复杂手法） |
| **`steghide` + `stegseek`** | steghide 负责嵌入/提取，stegseek 负责**快速爆破口令** |
| **`strings` + `zsteg`/`steghide`** | 明文类先被 strings 拿到；二进制类交给隐写工具 |
| **`steghide` + `dcfldd`** | **取证时先镜像**，在镜像副本上做隐写分析（原件封存） |
| **`steghide` + 文件完整性** | 用 [`../02-漏洞分析/tiger.md`](../02-漏洞分析/tiger.md) / AIDE 发现「图片被改过」 |
| **`steghide` + `yara`** | 提取出的内容如果是可执行文件，用 YARA 判恶意 |

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `the file format ... is not supported` | **载体是 PNG/GIF/WebP/MP3** | 换工具：`zsteg`（PNG/BMP 的 LSB）、`stegsolve`、`foremost`（追加数据）；或先转成 BMP/JPEG |
| `the cover file is too small to contain the data` | **容量不足** | 用更大的载体；或先 `-z 9` 压得更小；或分片藏 |
| `the file "x" already exists!` | 输出已存在 | **加 `-f`** |
| **载体被原地改写了** | **没加 `-sf`**（默认就地覆盖） | 下次**一定加 `-sf <新文件>`**；补救：从备份/镜像恢复 |
| `could not extract any data with that passphrase!` | 口令错 / 没藏 / 用的不是 steghide | 先 `steghide info <file>`（**能看出有没有 steghide 嵌入**）；再试常见口令/爆破 |
| `info` 里看不到 `embedded file` | ① 真的没藏 steghide 数据；② 嵌入时用了 `-N`？ | 用 `binwalk`/`strings`/`foremost` 交叉验证；换其它隐写工具 |
| 提取出的文件**没有扩展名**（`-N` 嵌入的） | 没嵌原始文件名 | `file <提取物>`；`fidentify`（见 [`testdisk.md`](testdisk.md)）判类型 |
| 提取出来的东西**打不开** | 提取被截断；或载体被二次压缩（如聊天软件转发图片） | **微信/QQ/微博转发会把图片重新压缩 → 隐写数据被破坏** → 要**原始文件** |
| **JPEG 提取失败，BMP 能成功** | JPEG 被重新编码过（有损） | **隐写最怕有损重编码**：JPEG 一旦被再次有损压缩，DCT 系数就变了。**必须用原始文件** |
| 提取出的内容乱码 | ① 用了错误的加密参数；② 提取的是被压缩/加密的密文 | 用 `info` 看 `encrypted`/`compressed`；一般 `extract` 会自动处理 |
| 口令里有特殊字符导致 shell 解析错 | 没加引号 | `-p 'my$pass!'` **用单引号** |
| `-p` 出现在 **shell 历史**里 | 参数明文可见 | **不写 `-p`**，让 steghide 交互式提示输入（也避免出现在 `ps` 里） |
| 嵌入后**图片视觉变了** | 载体是**有损格式又被改了很多**；或载体本身质量差 | 用更高质量的载体；JPEG 用 `-quality 90+` 的图 |
| BMP 嵌入后**大小完全一样**，怀疑没成功 | **这是正常的**（LSB 不改长度） | 用 `steghide info` 确认；或 `cmp -l 原图 隐写图` 看差异字节数
| WAV 提取后音频听不出差别 | 正常（LSB 只改幅度最低位） | 用 `steghide info` 确认 |
| 大文件藏不进去 | 容量 = 载体可嵌位数/8 | 换更大载体；或**分片藏到多个载体**（隐蔽性更好） |
| 载体是**截图**，容量很小 | 截图边缘/纯色区域多 → JPEG 可嵌系数少 | 用细节丰富的照片（噪点多、纹理多 → 容量大） |
| `steghide` 在 Windows 上提取不了 | 文件在传输中被处理过（邮件附件重编码、云盘处理） | 用**原始二进制文件**传输（zip 打包后再传） |

---

## 9. 防御视角（蓝队）

steghide 被 Kali 归类到**「防御规避」**——因为它用来**把数据藏起来绕过检测**。蓝队的应对思路有三层：**预防、检测、响应**。

### 9.1 预防（减少可乘之机）

| 措施 | 说明 |
|------|------|
| **DLP（数据防泄漏）** | 对**出站**做内容检测；**逐字节比对已知敏感文件** |
| **限制载体外发** | 禁止/审计大批图片、音频的外发（**隐写需要载体**） |
| **图片重编码（作为策略）** | 对外发图片做**有损重编码**——**会破坏隐写数据**（副作用是画质下降） |
| **终端管控** | 禁用/审计 `steghide`、`zsteg`、`stegsolve` 等工具的安装与执行 |
| **最小化数据可获取性** | 敏感数据不进个人终端 → 没得藏 |
| **水印（反向用法）** | 对内部文档加**可见/不可见水印**，泄露后可追责 |

### 9.2 检测

| 检测点 | 方法 | 局限 |
|--------|------|------|
| **进程执行** | EDR/auditd 监控 `steghide`、`stegseek`、`zsteg` 的运行 | 攻击者可改名/用自研脚本 |
| **文件系统** | 监控「图片/音频被修改」——用 **AIDE/Tripwire** 或 [`../02-漏洞分析/tiger.md`](../02-漏洞分析/tiger.md) 的文件完整性 | 新文件没有基线 |
| **文件大小异常** | 对 JPEG，嵌入会让**大小变化**；对 BMP/WAV，**大小不变**（这条对大文件无效） | 需要「原版对比」 |
| **统计异常** | 卡方/RS 分析检测 LSB 替换 | **对 JPEG（DCT 域）效果差**；小容量嵌入不敏感 |
| **DLP 的隐写检测** | 商业 DLP 有隐写分析模块 | 误报率高、性能开销大 |
| **出站流量** | 大批「看起来正常」的图片流向外部 → 行为分析 | 阈值难定 |
| **邮件/网盘** | 附件类型白名单 + 内容审查 | 加密后内容不可见 |

**一个实用的「低成本组合」**：

```
① 对出站的图片做【有损重编码】（会破坏 LSB 与多数 DCT 嵌入）
② 对关键终端审计 steghide 类工具的执行
③ 对内部敏感文档做【逐字节指纹】匹配（DLP）
④ 关键图片素材做【哈希基线】，发现被改动
```

### 9.3 响应（怀疑数据被隐写外带）

```bash
# ① 固定证据（先镜像！不要在原文件上操作）
sudo dcfldd if=/dev/sdX of=/evidence/disk.img hash=sha256 hashlog=/evidence/disk.sha256
#    见 09-数字取证/dcfldd.md

# ② 找「最近被改动的图片/音频」
find /mnt/evidence -type f \( -iname '*.jpg' -o -iname '*.bmp' -o -iname '*.wav' -o -iname '*.au' \) \
     -newermt '2026-09-01' -printf '%T+ %s %p\n' | sort -r | head -50

# ③ 对这些文件做快速筛查（只读！）
for f in <上面筛出的文件>; do
  printf 'y\n\n' | steghide info "$f" 2>/dev/null | grep -q 'embedded' && echo "可疑: $f"
done

# ④ 用 binwalk/foremost 检查「追加数据」类手法
binwalk /mnt/evidence/suspicious.jpg
foremost -i /mnt/evidence/suspicious.jpg -o /evidence/foremost-out

# ⑤ 记录一切操作（证据链）
#    把上面的命令与输出重定向到 /evidence/actions.log 并加时间戳
```

**蓝队的五条硬建议**：

1. **「删除/格式化」不能保护数据**，**隐写也不能被「网络层」抓到**——对策必须是**数据侧（DLP + 重编码）与主机侧（工具审计）的组合**；
2. **图片做有损重编码**是成本最低、效果最广的「反 stego」手段（**但要接受画质损失**，需评估是否可接受）；
3. **不要只依赖统计检测**——对 JPEG 和小容量嵌入都不敏感；
4. **取证必须有镜像 + 哈希 + 操作日志**，否则结论不可采信；
5. **告警不要只看「steghide 进程」**——攻击者可以用自写脚本做同样的 LSB 修改，**行为与数据侧才是主战场**。

**一个常被忽略的点**：**steghide 的嵌入口令默认来自交互输入**。这意味着在终端录屏/命令行审计里**看不到口令**——**「发现有人用了 steghide」和「知道口令」是两件事**。

---

## 10. 参考

- Kali 工具页（含 `steghide --help` 原文）：<https://www.kali.org/tools/steghide/>
- 上游项目（含算法说明与技术论文链接）：<http://steghide.sourceforge.net/>
- 算法依据（JPEG 的图论方法）：Stefan Hetzl, *A graph-theoretic approach to steganography*（steghide 文档中给出）
- Kali 包跟踪：<https://pkg.kali.org/pkg/steghide>
- 本地命令与自省：`steghide --help`、`steghide encinfo`、`steghide info <file>`、`steghide version`、`man steghide`
- 配套教程：[`exiftool.md`](exiftool.md)、[`binwalk.md`](binwalk.md)、[`foremost.md`](foremost.md)、[`scalpel.md`](scalpel.md)、[`bulk-extractor.md`](bulk-extractor.md)、[`dcfldd.md`](dcfldd.md)、[`testdisk.md`](testdisk.md)、[`../02-漏洞分析/yara.md`](../02-漏洞分析/yara.md)

## ⚠️ 法律与伦理

steghide 是**「隐藏信息存在」**的工具——它天然容易被用于**规避监管与数据防泄漏**，法律风险集中在**「藏什么」与「藏了要干什么」**。

**① 合法用途**

| 场景 | 是否合规 |
|------|----------|
| **CTF 隐写题** | ✅ |
| **学习隐写/隐写分析原理** | ✅ |
| **自有文件的数据隐藏（个人使用）** | ✅ |
| **数字水印（自有作品）** | ✅ |
| **授权取证中的隐写分析** | ✅（需授权 + 证据规范） |

**② 违法用途（明确禁止）**

| 行为 | 涉及法律 |
|------|----------|
| **用隐写外带公司/他人的敏感数据** | 《刑法》第 285 条（非法获取计算机信息系统数据）、《反不正当竞争法》、《保守国家秘密法》（涉密数据） |
| **规避 DLP / 审计 / 监管** | 视数据性质，可能构成上述犯罪或行政违法 |
| **在他人系统中植入隐写载荷（后门）** | 《刑法》第 285 条、**第 286 条（非法控制）** |
| **传播涉密/违法内容** | 《网络安全法》《数据安全法》《个人信息保护法》 |
| **对他人设备做隐写分析（取证）而未经授权** | **未经授权分析他人数据同样违法** |

**③ 做取证时的额外要求**

- **必须有明确授权**（司法程序、企业制度、当事人同意）；
- **必须先做镜像**（[`dcfldd.md`](dcfldd.md)）、**只读操作**、**记录操作日志与哈希**；
- **提取出的口令与内容属核心证据**，需**妥善保管、限制访问、不得泄露**；
- **不要越过授权范围去「试试还有没有别的东西」**——超范围取证会污染证据链，也可能违法。

**④ 报告与披露**

- 隐写分析结论**可能泄露检测方法**（对方会换手法），外发前评估披露范围；
- 提取出的内容若涉及他人隐私/个人信息，**必须脱敏**（《个人信息保护法》）；
- 发现的隐蔽外带渠道，应通过**正式安全事件流程**上报，**不要自行公开**。

**必须遵守**：

1. **只对你自己拥有、或获得明确授权的文件/设备**做嵌入与隐写分析；
2. **CTF/教学/自有文件**可以自由使用；**涉及他人数据一律需要授权**；
3. **绝不**用隐写帮助自己或他人外带组织数据、规避监管；
4. **取证场景先镜像、留哈希、记日志**，形成可追溯的证据链；
5. **不传播**可直接用于规避 DLP 的「操作手册」式内容；
6. 发现疑似隐写外带，**走正式上报流程**，不擅自处置或公开。
