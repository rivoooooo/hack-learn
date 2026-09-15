# dcfldd（取证级磁盘镜像获取）

> **一句话**：`dd` 的取证加强版——**边写镜像边算哈希、实时进度、可校验、可分卷**，保证「你拿到的镜像与原始介质逐位一致且可证明」。
> **分类**：数字取证 / 镜像获取（Acquisition）｜ **Kali 包**：`dcfldd`（命令 `dcfldd`）｜ **官方文档**：<https://github.com/resurrecting-open-source-projects/dcfldd> ｜ `man dcfldd`

---

## 1. 它解决什么问题

数字取证的**第一原则是「不改变原始证据」**，第二原则是「**能证明你没改变它**」。普通 `dd` 有两个致命缺陷：

1. **没有哈希**——你无法证明镜像与原始介质一致；
2. **没有进度**——几百 GB 的盘复制到一半你不知道还剩多久。

dcfldd 由美国国防部计算机取证实验室（DCFL）开发，就是为解决这两点：

| 需求 | `dd` | `dcfldd` |
|------|------|----------|
| 边复制边算哈希 | ❌（要复制完再单独算） | ✅ `hash=sha256` |
| 分段哈希（可定位损坏区段） | ❌ | ✅ `hashwindow=1G` |
| 实时进度与预计完成时间 | ❌（需 `status=progress`） | ✅ `status=on` |
| 一次写多个目标（双备份） | ❌ | ✅ 多个 `of=` |
| 分卷（便于光盘/传输） | ❌ | ✅ `split=4G` |
| 复制后校验 | ❌ | ✅ `vf=<file>` |
| 块大小默认 | 512 B（慢） | **32 KiB**（快得多） |

对比同类：

| 工具 | 定位 | 差异 |
|------|------|------|
| **`dcfldd`** | 命令行镜像获取 | 哈希 + 进度 + 分卷，纯 dd 风格 |
| **`dc3dd`** | 另一款取证 dd | 同样有哈希/进度；Kali 也在清单里 |
| **`guymager`** | 图形界面获取 | 点几下就行，适合现场；支持 E01/DD |
| **`ddrescue`** | 坏盘救援 | 擅长大面积坏道重试，取证也常用 |
| **`libewf`（`ewfacquire`）** | **E01 格式**获取 | 生成压缩、可分段、带元数据的 E01 |
| **`autopsy`/`sleuthkit`** | 镜像**分析** | 获取之后的步骤，见 [`sleuthkit.md`](sleuthkit.md) |

**镜像格式速览**（选格式时先想清楚要做什么）：

| 格式 | 说明 | 优点 | 缺点 |
|------|------|------|------|
| **原始格式（raw/dd）** | 逐扇区的字节流，`.dd`/`.img`/`.raw` | 任何工具都能读；可 `mount -o loop`；可 `mmls`/`fls` | 体积=介质容量（无压缩）；分段需自己管 |
| **E01（EnCase Evidence File）** | 分块 + 压缩 + CRC + 元数据（`ewfacquire` 生成） | 体积小、可校验、可记录案卷信息 | 分析工具需支持（TSK 支持 `-i ewf`）；写性能较低 |
| **AFF4** | 现代开源取证格式 | 支持稀疏与加密 | 生态相对小（Kali 有 `afflib`） |
| **VMDK/VHDX** | 虚拟机磁盘 | 虚拟机直接挂载 | 取证元数据能力弱 |

> **实践建议**：**授权环境内做分析，raw + 单独保存哈希清单**最省事；**需要交付/长期保存**时用 E01（压缩 + 内置校验 + 元数据）。

---

## 2. 工作原理

```
① 写保护（硬件写阻断器 / 只读挂载 / 软阻断）
        │
② dcfldd 读源（块设备或镜像文件）
        │   每个读入块：更新滚动哈希 → 写入目标 → 更新进度
        ▼
③ 输出
   ├─ 镜像文件（可 split 分卷）
   ├─ hashlog：总哈希 + 每 hashwindow 的分段哈希
   ├─ errlog：读错误日志（坏道位置）
   └─ 状态输出：已复制字节 / 百分比 / 速度 / 预计剩余时间
        │
④ 校验：dcfldd vf=<镜像> if=<源>   ← 逐位比对（或对镜像重算哈希与记录比对）
        │
⑤ 移交分析：sleuthkit / autopsy / bulk-extractor / foremost / scalpel
```

**取证完整性的核心概念**：

- **保管链（Chain of Custody）**：从扣押到分析的**每一次交接**都要有记录（谁、何时、做了什么）。缺一环，证据在法庭上就可能不被采信。
- **哈希校验值**：源与镜像的哈希一致 → 证明镜像忠实。**在获取时就算，在每次访问前重算比对**。
- **写阻断（Write Blocker）**：物理阻断器最可靠；其次是软件只读（`blockdev --setro`）或直接对**已制作的镜像**（而非在线系统盘）操作。
- **易失性数据优先**：内存、网络连接、运行进程比磁盘更「短命」，按 RFC 3227 的易失性顺序采集。

dcfldd 的 `hashwindow` 把镜像切成若干窗口分别算哈希——**如果流传输中出现损坏，你可以精确定位到哪一段**，而不用整盘重来。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install dcfldd
dcfldd --version
```

```bash
dcfldd --help
```

最常用的一条命令（**取证现场的标准姿势**）：

```bash
sudo dcfldd if=/dev/sdb of=/evidence/disk01.dd \
            hash=sha256 hashlog=/evidence/disk01.sha256 \
            bs=32M status=on \
            errlog=/evidence/disk01.err
```

```console
0+1064224 records in
0+1064224 records out
125034840064 bytes (125 GB) copied, 862.4 s, 145 MB/s

Total (sha256): f3a1c9e2b7d4...  /evidence/disk01.dd
```

**先认识你的源设备**（别写错盘符，这是最危险的错误）：

```bash
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,MODEL
sudo fdisk -l /dev/sdb
sudo blkid /dev/sdb
```

**写入取证的注意事项**：

- **优先对镜像操作**：能离线分析就不要动原盘；
- 原盘分析时务必先设只读：`sudo blockdev --setro /dev/sdb`（并无法保证 100% 安全）；
- 输出目录要有**足够空间**（原始镜像 ≈ 介质容量）。

---

## 4. 核心参数详解

以下是 `dcfldd --help` 的**真实参数**（按用途分组）：

### 4.1 输入输出与块大小

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `if=FILE` | 输入（源） | 块设备 `/dev/sdb`、镜像 `evidence.dd`、或 `/dev/zero` |
| `of=FILE` | 输出（镜像） | 可写**多个** `of=` 做双备份 |
| `of:=COMMAND` | 把输出管道给命令 | 如 `of:='gzip -c > img.dd.gz'` |
| `bs=BYTES` | 同时设 `ibs` 与 `obs` | 默认 **32768**；大介质用 `32M` 提速 |
| `ibs=BYTES` / `obs=BYTES` | 分别设读写块 | 一般不用动 |
| `cbs=BYTES` | 转换缓冲大小 | 配合 `conv=` |
| `count=BLOCKS` | 只复制 N 个输入块 | 取部分（如只取分区） |
| `limit=BYTES` | 按**字节**限制长度 | 比 `count` 直观 |
| `skip=BLOCKS` | 跳过输入开头的块 | 定位分区偏移（配 `ibs`） |
| `seek=BLOCKS` | 输出跳过块 | 拼接镜像时用 |
| `conv=KEYWORDS` | 转换选项（同 `dd`） | 谨慎使用，会改变字节流 |

### 4.2 哈希与校验

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `hash=NAME` | 计算哈希：`md5`/`sha1`/`sha256`/`sha384`/`sha512` | **`sha256` 起步**；`md5`/`sha1` 已不推荐单独使用 |
| `hashlog=FILE` | 哈希结果写入文件 | 与镜像一起归档，作为**校验凭据** |
| `hashlog:=COMMAND` | 哈希结果管道给命令 | 自动上传到证据服务器（谨慎） |
| `hashwindow=BYTES` | **每 N 字节算一次哈希** | 大镜像建议开（如 `1G`），便于定位损坏 |
| `hashconv=[before\|after]` | 哈希在转换前/后计算 | **必须写 `before`** 才能证明「源」的一致性 |
| `hashformat=FORMAT` | 分段哈希的输出格式 | 便于脚本解析 |
| `totalhashformat=FORMAT` | 总哈希的输出格式 | 同上 |
| `vf=FILE` | **校验**：把 `FILE` 与输入逐位比对 | 复制完成后做一次 |
| `verifylog=FILE` | 校验结果写文件 | 保管链留证 |

### 4.3 分卷、状态、日志

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `split=BYTES` | 每 N 字节切一个新文件 | 便于刻盘/传输（如 `split=4G`） |
| `splitformat=[TEXT\|MAC\|WIN]` | 分卷命名规则 | 跨平台交付时注意 |
| `status=[on\|off]` | 显示实时状态 | **必须开**，大镜像时救命 |
| `statusinterval=N` | 每 N 块更新状态 | 刷太快就调大 |
| `sizeprobe=[if\|of\|BYTES]` | 百分比计算的基准 | 默认探测；不确定时显式给字节数 |
| `errlog=FILE` | 错误信息写文件 | **坏盘场景必开** |
| `pattern=HEX` | 用指定字节模式作为输入 | 擦除/覆写测试 |
| `textpattern=TEXT` | 用重复文本作为输入 | 同上 |
| `diffwr=[on\|off]` | 仅当内容不同才写入 | 增量更新镜像（**取证慎用**） |

---

## 5. 实战演练

> **环境声明**：以下全部在你**自有或已获授权**的设备/镜像上进行。
> **最容易犯的致命错误是写错 `of=`**（把源盘写坏）。请务必：
> 1. 先用 `lsblk`/`fdisk -l` 确认设备名；
> 2. 在**虚拟机 + 虚拟磁盘**上练习（推荐用 **NIST CFReDS** 公开取证镜像，或自己造一个实验镜像）；
> 3. 绝不在生产设备上执行擦除/覆写类操作。

### 场景 1：造一个「作案现场」（先有可练的镜像）

在没有真实案件材料的情况下，**自己造证据**是最安全的练习方式：

```bash
# ① 造一个 256MB 的虚拟磁盘
dd if=/dev/zero of=/tmp/disk.img bs=1M count=256

# ② 分区并格式化（模拟一块有数据的盘）
sudo losetup -fP /tmp/disk.img
losetup -a | grep disk.img
```

```console
/dev/loop0: []: (/tmp/disk.img)
```

```bash
# ③ 在 loop0p1 上建文件系统（假设分区已创建）
sudo mkfs.ext4 -q /dev/loop0p1
sudo mkdir -p /mnt/lab && sudo mount /dev/loop0p1 /mnt/lab

# ④ 放入「证据」：一个 JPEG、一个 PDF、一份删除的文本
printf 'password=LabSecret123\n' | sudo tee /mnt/lab/secret.txt
sudo cp /usr/share/pixmaps/debian-logo.png /mnt/lab/photo.jpg
sudo cp README.md /mnt/lab/report.pdf 2>/dev/null || echo "report" | sudo tee /mnt/lab/report.pdf
sudo rm /mnt/lab/secret.txt          # 故意删除，制造「恢复」需求
sudo sync && sudo umount /mnt/lab && sudo losetup -d /dev/loop0
```

**解读**：现在 `/tmp/disk.img` 就是一个「有已删除文件」的取证练习镜像。**这套自造镜像可以在无网络、无第三方样本的情况下反复练习整个链条**（获取 → 分析 → 恢复）。

### 场景 2：用 dcfldd 获取镜像（含哈希与校验）

```bash
# ① 明确源与目标
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
sudo mkdir -p /evidence
df -h /evidence
```

```console
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda3       500G   20G  480G   5% /evidence
```

```bash
# ② 获取（边算哈希、边显示进度、错误日志）
sudo dcfldd if=/tmp/disk.img of=/evidence/disk.img \
            hash=sha256 hashlog=/evidence/disk.sha256 \
            hashwindow=64M hashconv=before \
            bs=4M status=on \
            errlog=/evidence/disk.err
```

```console
256+0 records in
256+0 records out
268435456 bytes (268 MB) copied, 1.83 s, 147 MB/s

Total (sha256): 8b1f0c9a7e3d2f...   /evidence/disk.img
```

```bash
# ③ 看哈希日志（含分段哈希，可定位损坏区间）
cat /evidence/disk.sha256
```

```console
0 - 67108864: 2f7a...c1
67108864 - 134217728: 91bd...3e
134217728 - 201326592: 4c02...88
201326592 - 268435456: aa17...d0
Total: 8b1f0c9a7e3d2f...
```

```bash
# ④ 独立复核（第二个工具算一遍，交叉验证）
sha256sum /tmp/disk.img /evidence/disk.img
```

```console
8b1f0c9a7e3d2f...  /tmp/disk.img
8b1f0c9a7e3d2f...  /evidence/disk.img
```

**解读（这是取证的「交付物」）**：

| 文件 | 作用 |
|------|------|
| `/evidence/disk.img` | 分析用镜像（**原始证据应封存**） |
| `/evidence/disk.sha256` | 完整性凭据（含分段哈希 + 总哈希） |
| `/evidence/disk.err` | 读错误记录（有坏道时是关键证据） |

`hashconv=before` 表示哈希算的是**从源读到的原始数据**，而不是经过转换后的——这是能作为证据的前提。

```bash
# ⑤ 校验副本（可选，但强烈建议做一次）
sudo dcfldd if=/tmp/disk.img of=/dev/null vf=/evidence/disk.img \
            verifylog=/evidence/disk.verify status=on
cat /evidence/disk.verify
```

```console
Total (sha256): 8b1f0c9a7e3d2f...
Verification: /evidence/disk.img matches input
```

### 场景 3：坏盘与分卷（实战中的两个难缠场景）

**场景 3a：坏道盘（读错误要记录，而不是中断）**

```bash
# 用较大的 bs 并开启错误日志；必要时配合 ddrescue 重试坏道
sudo dcfldd if=/dev/sdb of=/evidence/bad.dd \
            bs=512 conv=noerror,sync \
            hash=sha256 hashlog=/evidence/bad.sha256 \
            errlog=/evidence/bad.err status=on
```

```console
dcfldd: error reading '/dev/sdb': Input/output error  (offset 0x1f4a0000)
0+1024 records in
```

```bash
# 看坏在哪
cat /evidence/bad.err
```

**解读**：`conv=noerror,sync` 让 dcfldd **跳过错误并补零填充**，保证偏移不错位（取证里必须保持偏移对齐，否则后续文件系统分析全乱）。但**坏道密集时 dcfldd 会很慢**，此时改用 `ddrescue`：

```bash
sudo apt install ddrescue
sudo ddrescue -d -r3 /dev/sdb /evidence/bad.dd /evidence/bad.map
```

```console
GNU ddrescue 1.27
Press Ctrl-C to interrupt
     ipos:  15204352 B,  opos:  15204352 B, non-tried:  ...
   rescued:  14000000 B,  errsize:     100 kB,  errors:       12
```

**解读**：`ddrescue` 的 `.map` 文件让**中断后可以继续**，并优先抢救健康区域——这是坏盘取证的标准做法。救完再用 dcfldd 或 `sha256sum` 记录哈希。

**场景 3b：分卷（超大镜像或需要交付）**

```bash
sudo dcfldd if=/dev/sdb of=/evidence/part.dd \
            split=4G splitformat=TEXT \
            hash=sha256 hashlog=/evidence/part.sha256 \
            bs=4M status=on
ls -lh /evidence/
```

```console
-rw-r--r-- 1 root root 4.0G part.dd.001
-rw-r--r-- 1 root root 4.0G part.dd.002
-rw-r--r-- 1 root root 1.2G part.dd.003
-rw-r--r-- 1 root root  97B part.sha256
```

```bash
# 合并（分析前）
cat /evidence/part.dd.00* > /evidence/whole.dd
sha256sum /evidence/whole.dd     # 应与 hashlog 的 Total 一致
```

**解读**：分卷必须记录**顺序与哈希**，并在交付说明里写清。合并后哈希必须与记录一致，否则整个证据链失效。

**命令链**：获取（dcfldd）→ 分析（[`sleuthkit.md`](sleuthkit.md)：`mmls`/`fls`/`icat`）→ 文件雕刻（[`foremost.md`](foremost.md)/[`scalpel.md`](scalpel.md)）→ 元数据（[`exiftool.md`](exiftool.md)）。

---

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `N+0 records in / out` | 读入/写出块数（**两者应相等**） | 不相等说明有读错误或长度限制 |
| `bytes (X GB) copied, Y s, Z MB/s` | 总量与速率 | 速率异常低 → 介质有问题或接口瓶颈 |
| `Total (sha256): ...` | 总哈希 | 与源比对、写入报告 |
| 分段哈希清单 | 每个窗口的哈希 | 出现不一致时可定位损坏区间 |
| `dcfldd: error reading ...: Input/output error` | **坏道** | 记录 offset → 用 `ddrescue` 重救 |
| `Verification: ... matches input` | 校验通过 | 证据可用 |
| `Verification: ... does NOT match` | **校验失败** | 立即停止，重新获取（介质/线缆/目标盘有问题） |
| `hashconv=after` 的结果 | 哈希算的是转换后数据 | **不能**用来证明源的一致性，取证场景禁止 |
| `split` 产出的 `.001/.002…` | 分卷 | 合并后校验哈希 |

**成功判据**：`records in == records out`、总哈希与源一致、校验通过、`errlog` 无内容（或错误已被记录并说明）。

---

## 7. 与其他工具配合

```
【获取阶段】
  写阻断器/只读挂载
      │
      ├─ dcfldd ──► raw 镜像 + sha256 + errlog      （本文）
      ├─ ddrescue ──► 坏盘抢救 + .map 续传
      ├─ libewf（ewfacquire）──► E01（压缩/分段/内置校验）
      └─ guymager ──► 图形界面获取（现场作业）
              │
【分析阶段】
      ├─ mmls / fsstat ──► 分区与文件系统结构       （sleuthkit.md）
      ├─ fls / icat ──► 列目录/按 inode 提取
      ├─ tsk_recover ──► 批量恢复文件
      ├─ bulk-extractor ──► 无文件系统解析的特征提取（邮箱/IP/URL/卡号）
      ├─ foremost / scalpel ──► 文件雕刻（恢复被删除内容）
      ├─ binwalk ──► 固件/嵌入文件与熵分析
      └─ exiftool ──► 元数据（时间、设备、GPS）
              │
【报告阶段】
      时间线（mactime / tsk_gettimes）→ 关键字段 → 结论
```

- 分区与文件系统分析：[`sleuthkit.md`](sleuthkit.md)
- 图形化分析：[`autopsy.md`](autopsy.md)
- 特征与凭据提取：[`bulk-extractor.md`](bulk-extractor.md)
- 文件雕刻：[`foremost.md`](foremost.md)、[`scalpel.md`](scalpel.md)
- 固件与嵌入数据：[`binwalk.md`](binwalk.md)
- 元数据：[`exiftool.md`](exiftool.md)
- 上游（攻防视角）：[`../08-后渗透/README.md`](../08-后渗透/README.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| **写错了 `of=`，把源盘写坏** | 手工敲设备名 | **执行前 3 遍核对 `lsblk`**；用 `sudo blockdev --setro` 保护源；在虚拟机上练熟 |
| `Permission denied` | 非 root | `sudo dcfldd ...` |
| `No space left on device` | 输出分区不足 | 原始镜像≈介质容量；换盘或先用 `gzip`/E01 压缩 |
| `error reading: Input/output error` | 坏道 | 加 `conv=noerror,sync` 并使用 `errlog`；严重时用 `ddrescue` |
| 校验失败 | 目标盘坏 / 内存问题 / 线缆 | 换盘重做；校验用 `vf=` 或独立 `sha256sum` |
| `bs` 太小导致极慢 | 默认块小/介质慢 | `bs=32M` 左右；确认 USB/SATA 接口正常 |
| 分卷合并后哈希不符 | 漏卷/顺序错 | 按 `.001 .002` 顺序合并；核对每卷大小 |
| `dd`/`dcfldd` 在运行中的系统上镜像不一致 | 文件系统在变化 | 取证时用**只读挂载/写阻断器**，或对已停机的介质操作；在线系统优先采集易失性数据 |
| 哈希只有 `md5` | 老流程遗留 | 现代取证至少 `sha256`（或同时提供多种） |
| `hashconv` 没写，结果对不上 | 默认在转换后计算 | 显式写 `hashconv=before` |
| `sizeprobe` 导致百分比乱跳 | 无法探测源大小（管道/设备） | 显式 `sizeprobe=<字节数>` 或关闭百分比 |
| 进度条刷屏淹没输出 | `statusinterval` 太小 | 调大 `statusinterval` |
| 用了 `diffwr=on` 后发现镜像与源不一致 | 只写了差异块 | **取证场景禁止使用**（它是增量更新语义） |
| 分析时偏移错乱 | 复制时用了 `skip`/`count` 或 `conv` 改变了长度 | 重新获取完整镜像；分区内分析用 `-o <offset>` 而不是复制时裁剪 |

---

## 9. 防御视角（蓝队 / 应急响应）

取证获取是**应急响应的第一步**，对蓝队来说它同时是「能力」也是「纪律」：

| 环节 | 要求 | 说明 |
|------|------|------|
| **不要立刻拔电源** | 先采集易失性数据 | 内存、进程、网络连接、登录会话一旦丢失不可恢复（见易失性顺序 RFC 3227） |
| **写保护** | 使用硬件写阻断器 | 软件只读有绕过风险；写阻断器能出报告，是法庭上的有力证据 |
| **镜像 + 哈希** | 每次获取都记录 `sha256` | 没有哈希的镜像在仲裁/司法场景基本无证明力 |
| **保管链文档** | 谁、何时、从哪台设备、用了什么工具与参数 | dcfldd 的完整命令行应原样记录 |
| **工作副本原则** | 原镜像封存，只在副本上分析 | 避免分析过程污染证据 |
| **访问前重算哈希** | 每次打开镜像前校验 | 证明「我在保管期间没有改动」 |
| **日志留存** | `errlog`、`verifylog`、`hashlog` 一并归档 | 与镜像同等级别保管 |
| **时间基准** | 记录采集时区与系统时间 | 时间线分析的前提（见 [`sleuthkit.md`](sleuthkit.md) 的时区参数） |
| **授权与隐私** | 采集范围要有授权/法律依据 | 镜像含大量个人信息，涉及《个人信息保护法》 |

**常见应急失误**（值得写进你的 IR 手册）：

1. 直接 `mount` 嫌疑盘 → 改了 `atime`、触发文件系统恢复日志 → 证据被污染；
2. 只做 `cp -r` 而不做镜像 → 丢失已删除文件与元数据；
3. 忘记记录**时区**与主机时间 → 时间线全错；
4. 用同一块移动硬盘存多个案件 → 保管链混乱。

---

## 10. 参考

- dcfldd 官方仓库（含完整用法与示例）：<https://github.com/resurrecting-open-source-projects/dcfldd>
- Kali 工具页：<https://www.kali.org/tools/dcfldd/>
- NIST 取证参考镜像（公开练习样本）：<https://cfreds.nist.gov/>
- NIST SP 800-86《Guide to Integrating Forensic Techniques into Incident Response》
- RFC 3227《Guidelines for Evidence Collection and Archiving》（易失性顺序）
- 本地命令：`dcfldd --help`、`man dcfldd`、`man dd`、`man ddrescue`

## ⚠️ 法律与伦理

**磁盘镜像包含他人全部数据**（文档、照片、聊天记录、凭据），属于高度敏感的个人信息与企业数据。未经授权的获取、查看、复制、传播可能触犯：

- 《刑法》第 285 条（非法获取计算机信息系统数据）、第 253 条之一（侵犯公民个人信息罪）；
- 《网络安全法》《数据安全法》《个人信息保护法》。

**合法前提**：

1. 获得**设备所有者或司法机关的书面授权**（企业内部调查需有制度依据与员工告知）；
2. 采集范围**最小必要**（只取与事件相关的介质与目录）；
3. 数据**加密存储**、限定访问人员、按约定时限销毁；
4. 报告与对外沟通中**脱敏**（不含真实个人信息与凭据）。

本教程请仅在**自建实验镜像**（如第 5 节场景 1 的方法）或 **NIST CFReDS 公开样本**上练习，不要对任何未经授权的设备执行镜像获取。
