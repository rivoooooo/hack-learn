# 09 · 数字取证（Digital Forensics）

> 本目录是 Kali 工具精讲教程的第 9 篇：**从「拿到一块介质/一个镜像」到「得出可写进报告的结论」**。
> 主干闭环：**获取（镜像 + 哈希）→ 结构（分区/文件系统）→ 内容（文件/删除/雕刻）→ 特征（元数据/凭据）→ 时间线 → 结论**。
> 上游：[`../08-后渗透/`](../08-后渗透/)（攻防视角）｜ 下游：[`../10-逆向工程/`](../10-逆向工程/)、[`../11-社会工程与报告/`](../11-社会工程与报告/)
> 相关索引：[`../../index.md`](../../index.md) ｜ 分类速查：[`../../catalog/forensics.md`](../../catalog/forensics.md)、[`../../by-attack/forensics.md`](../../by-attack/forensics.md)

---

## 工具清单

| 工具 | 一句话 | 难度 | 教程 |
|------|--------|------|------|
| **dcfldd** | 取证级镜像获取：边复制边算哈希、进度、分卷、校验 | ⭐⭐ | [`dcfldd.md`](dcfldd.md) |
| **sleuthkit** | 文件系统命令行套件：`mmls`/`fsstat`/`fls`/`icat`/`istat`/`tsk_recover`/`mactime` | ⭐⭐⭐ | [`sleuthkit.md`](sleuthkit.md) |
| **autopsy** | TSK 的图形界面（Kali 打包为经典浏览器版，端口 9999） | ⭐⭐ | [`autopsy.md`](autopsy.md) |
| **bulk-extractor** | 不解析文件系统，直接扫字节流提特征（邮箱/URL/IP/卡号/密钥）+ 直方图 | ⭐⭐ | [`bulk-extractor.md`](bulk-extractor.md) |
| **foremost** | 文件雕刻：靠文件头尾从原始字节流恢复文件（含 ext 间接块检测） | ⭐⭐ | [`foremost.md`](foremost.md) |
| **scalpel** | 高速文件雕刻：自定义签名、簇对齐、**覆盖率图**、`yes/yes` 质量标记 | ⭐⭐⭐ | [`scalpel.md`](scalpel.md) |
| **binwalk** | 二进制/固件结构分析：签名扫描、递归提取、熵图（定位加密/压缩区） | ⭐⭐⭐ | [`binwalk.md`](binwalk.md) |
| **exiftool** | 元数据读写：EXIF/GPS/设备序列号、文档作者与修订历史、结构校验 | ⭐⭐ | [`exiftool.md`](exiftool.md) |

> **四个工具的分工一句话**：
> **dcfldd 拿下来 → sleuthkit 看结构 → foremost/scalpel 兜底抢救 → bulk-extractor 捞特征 → exiftool 落细节 → binwalk 管固件 → autopsy 做图形复核**。
>
> **关于 volatility3**：`volatility3`（内存取证框架）**不在本仓库抓取的 Kali 官方工具清单中**（清单里只有配套的 `dwarf2json`），因此本目录**未收录**，改为用真实存在于清单的 **`bulk-extractor`** 承担「内存/镜像的字节流特征提取」这一职责（它支持内存转储输入，并能通过 `-S carve_net_memory=1` 从内存里雕刻网络包）。需要完整内存取证时请自行按官方文档部署 volatility3。

---

## 学习顺序

```
① 观念与纪律（先读，别跳过）
     · 只读原则 / 写阻断 / 哈希 / 保管链 / 易失性顺序
     · 概念：raw vs E01、inode/MFT、MAC 时间、未分配空间、熵
     → dcfldd.md 第 2、9 节 + sleuthkit.md 第 2 节

② 获取         dcfldd.md        ← 镜像 + sha256 + 错误日志 + 校验
③ 结构         sleuthkit.md     ← mmls（换算 -o）、fsstat（块大小/类型）
④ 内容         sleuthkit.md     ← fls（含 -d 已删除）→ istat → icat / tsk_recover
⑤ 时间线       sleuthkit.md     ← fls -m + mactime（**记住设时区**）
⑥ 兜底         foremost.md / scalpel.md   ← blkls -A 导出未分配空间再雕刻
⑦ 特征         bulk-extractor.md          ← 先摸清「有什么」（直方图优先读）
⑧ 细节         exiftool.md                ← 元数据、设备序列号、篡改判定
⑨ 固件/二进制  binwalk.md                  ← 签名扫描 + 熵图 + 递归提取
⑩ 图形复核     autopsy.md                  ← 复现命令行结论，便于交付
```

**建议节奏**：用**自建实验镜像**（见 [`dcfldd.md` 场景 1](dcfldd.md#场景-1造一个作案现场先有可练的镜像)）把下面这条链**完整走 3 遍**，并每次写一份「时间线 + 证据清单 + 哈希」的报告草稿：

```
自制镜像（含已删除文件）→ dcfldd 获取（sha256）
  → mmls/fsstat → fls -d 找删除 → istat 看删除时间 → icat 提取
  → blkls -A → foremost/scalpel 雕刻 → exiftool 看元数据
  → fls -m + mactime 出时间线 → bulk-extractor 出特征清单
```

---

## 环境准备

### 分析机（Kali）

```bash
sudo apt update
sudo apt install -y dcfldd sleuthkit autopsy bulk-extractor foremost scalpel binwalk \
                    libimage-exiftool-perl squashfs-tools p7zip-full xz-utils lzma cpio

# 常用辅助
sudo apt install -y ddrescue guymager libewf testdisk   # 获取与救援
sudo apt install -y hashdeep                            # 批量哈希（完整性清单）
```

验证：

```bash
command -v dcfldd fls icat mmls fsstat istat blkls tsk_recover mactime \
           bulk_extractor foremost scalpel binwalk exiftool autopsy
exiftool -ver
binwalk -h | head -3
```

### 工作目录规范（**建议固定下来**）

```
/evidence/
├── case-2024-001/
│   ├── 00-原始镜像/      disk.img          ← 只读，封存
│   ├── 01-校验/          disk.sha256        ← 哈希与校验记录
│   ├── 02-工作副本/                          ← 所有分析都在这上面做
│   ├── 03-未分配空间/    unallocated.bin
│   ├── 04-雕刻结果/      carved-foremost/ carved-scalpel/
│   ├── 05-提取文件/      recovered/
│   ├── 06-特征提取/      bulk-out/
│   ├── 07-时间线/        bodyfile.txt timeline.csv
│   ├── 08-元数据/        meta.csv
│   └── 保管链.txt        chain_of_custody.txt   ← 每次操作都追加一行
```

**关键原则**：
- 原始镜像**只读封存**（`chmod 444`，或放在只读挂载上）；
- **绝不向证据分区写入**（雕刻与恢复会大量写盘 → 输出到独立工作盘）；
- 每次操作**追加保管链记录**（时间、工具、完整命令行、结果）。

### 练习素材（合法来源）

| 素材 | 获取方式 | 适合练习 |
|------|----------|----------|
| **自建实验镜像** | 见 [`dcfldd.md` 场景 1](dcfldd.md#场景-1造一个作案现场先有可练的镜像) | 全流程（推荐起点） |
| **NIST CFReDS** | <https://cfreds.nist.gov/>（公开取证参考数据集） | 真实感的图片/文档/删除文件样本 |
| **DD-WRT / OpenWrt 官方固件** | 官网下载（开源固件） | binwalk 固件拆解（Kali 官方示例即用此类） |
| **自身设备镜像** | 你自己淘汰的旧硬盘/U 盘 | 真实数据、风险自控 |
| **Cellebrite / Digital Corpora 公开样本** | 公开数据集合 | 大规模练习 |

> ⚠️ **不要**从未经授权的设备获取镜像，也不要下载来源不明的「取证练习镜像」（可能含他人真实数据）。

---

## 环境准备清单（自检）

```bash
# 1) 工具齐全
for t in dcfldd mmls fsstat fls icat istat blkls tsk_recover mactime \
         bulk_extractor foremost scalpel binwalk exiftool autopsy; do
  printf '%-16s %s\n' "$t" "$(command -v $t || echo MISSING)"
done

# 2) 解压工具齐全（binwalk 提取依赖）
for t in unsquashfs 7z xz lzma cpio unzip; do
  printf '%-12s %s\n' "$t" "$(command -v $t || echo MISSING)"
done

# 3) 自造一个练习镜像并跑通第一轮
dd if=/dev/zero of=/tmp/lab.img bs=1M count=64
mmls /tmp/lab.img || echo "（未分区属正常，见 dcfldd.md 场景 1 造带分区的镜像）"

# 4) 哈希工具与校验流程
sha256sum /tmp/lab.img | tee /tmp/lab.sha256
sha256sum -c /tmp/lab.sha256

# 5) 时区（时间线分析前必须明确）
timedatectl | head -3
cat /etc/timezone 2>/dev/null
```

---

## 核心方法论（**比工具更重要**）

| 原则 | 含义 | 对应工具/操作 |
|------|------|---------------|
| **不改变证据** | 只读、写阻断、原始镜像封存 | `blockdev --setro`、硬件写阻断器、`chmod 444` |
| **可证明未改变** | 每次访问前后校验哈希 | `sha256sum`、`dcfldd hash=`、`hashdeep` |
| **保管链完整** | 记录谁/何时/做了什么 | `chain_of_custody.txt`（含**完整命令行**） |
| **工作副本** | 分析在副本上做 | `cp` 一份再分析 |
| **易失性优先** | 内存/连接/进程 → 磁盘 | 内存转储 → [`bulk-extractor.md`](bulk-extractor.md) 提特征 |
| **时间基准明确** | 记录时区与系统时间 | `mactime -z`、`fls -z`、报告写明时区 |
| **多工具交叉验证** | 同一结论用两条独立路径复现 | TSK ↔ Autopsy；foremost ↔ scalpel；exiftool ↔ TSK |
| **结论可复现** | 报告里给出可重跑的命令 | 所有命令原样记录 |
| **敏感数据最小化** | 只看必要的、按敏感数据管理产出 | 限定类型/区域；加密存储；脱敏报告 |

---

## 与其它章节的衔接

| 你手上的东西 | 去哪里 |
|--------------|--------|
| 一块硬盘/一个镜像文件 | [`dcfldd.md`](dcfldd.md)（获取）→ [`sleuthkit.md`](sleuthkit.md)（结构） |
| 想快速知道「有没有敏感数据」 | [`bulk-extractor.md`](bulk-extractor.md) |
| 文件被删/分区被格式化 | [`sleuthkit.md`](sleuthkit.md)（`fls -d`/`tsk_recover`）→ [`foremost.md`](foremost.md)/[`scalpel.md`](scalpel.md) |
| 固件、可疑 `.bin` | [`binwalk.md`](binwalk.md) |
| 照片/文档来源与设备关联 | [`exiftool.md`](exiftool.md) |
| 想要图形界面复核与案件管理 | [`autopsy.md`](autopsy.md) |
| 提取出的二进制要深度分析 | [`../10-逆向工程/README.md`](../10-逆向工程/README.md) |
| 报告怎么写 | [`../11-社会工程与报告/README.md`](../11-社会工程与报告/README.md) |
| 攻防视角（这些技术在攻击侧怎么用） | [`../08-后渗透/README.md`](../08-后渗透/README.md) |

---

## ⚠️ 法律与伦理

**数字取证处理的是他人的全部数据**（文档、照片、聊天、凭据、位置记录）。未经授权的获取或分析可能触犯：

- 《刑法》第 285 条：非法获取计算机信息系统数据罪；
- 《刑法》**第 253 条之一**：侵犯公民个人信息罪（**GPS 定位、照片元数据属敏感个人信息**）；
- 《刑法》第 252 条：侵犯通信自由罪（涉邮件/通信内容时）；
- 《网络安全法》《数据安全法》《个人信息保护法》。

**使用前提（缺一不可）**：

1. **书面授权**：设备所有者或司法机关的授权；企业内部调查需有制度依据并履行告知程序；
2. **最小必要**：只分析与事件相关的范围，避免浏览与案件无关的私密内容；
3. **只读纪律**：原始镜像封存、工作副本分析、**绝不写入证据**；
4. **访问留痕**：分析过程本身也要有保管链（谁、何时、看了什么）；
5. **加密存储与限时销毁**：所有产出（含未分配空间、雕刻结果、特征 CSV）按敏感数据管理；
6. **报告脱敏**：不包含真实个人信息、凭据、私密内容与完整定位信息；
7. **练习只用自建素材或公开样本**（自建实验镜像、NIST CFReDS、开源固件）。
