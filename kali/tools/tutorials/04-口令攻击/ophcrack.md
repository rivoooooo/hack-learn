# Ophcrack（彩虹表 Windows 口令破解器）

> **一句话**：用预计算的彩虹表（rainbow table）破解 Windows 的 LM/NTLM 口令哈希，擅长在几秒内恢复「字母数字组合」类口令。
> **分类**：口令攻击 ｜ **Kali 包**：`ophcrack`（GUI）/ `ophcrack-cli`（命令行）｜ **官方文档**：<https://ophcrack.sourceforge.net/>

## 1. 它解决什么问题

[hashcat](hashcat.md) 用 GPU **实时计算**哈希；Ophcrack 走的是另一条路：**用预先算好的表去查**。

| | 实时计算（hashcat / john） | 查表（Ophcrack） |
| --- | --- | --- |
| 原理 | 每次尝试现场算一次哈希 | 预先算好「哈希↔明文」的压缩映射，运行时查找 |
| 速度 | 取决于算力（GPU 最快） | 取决于**磁盘 I/O 与内存**，与算力几乎无关 |
| 成本结构 | 时间（几小时到几年） | **空间**（预先下载/购买几十 GB 到 TB 的表） |
| 适用 | 任意算法，只要有算力 | **只对特定算法+特定字符集+特定长度**有效 |
| 覆盖盲区 | 无（理论上可穷尽） | 表里没有的组合**永远查不到** |

**结论：Ophcrack 的价值在于「覆盖范围内快得离谱」**——典型的 LM 哈希（字母数字、长度 ≤ 14）在合适的表下**几秒内出结果**。超出表的覆盖范围，则完全无能为力。

因此 Ophcrack 在今天的实战定位是：

- **Windows 取证 / 应急响应**：从内存镜像或磁盘镜像里拿到 SAM 后，快速恢复口令以便进一步调查；
- **教学演示**：彩虹表原理的经典案例；
- **对非常弱的口令做快速初筛**。

对**强口令**（长度 > 14、含符号、或用 NTLM 且已禁用 LM），Ophcrack 基本无效，应该转向 [hashcat](hashcat.md)。

## 2. 工作原理

### 2.1 从 Hellman 到彩虹表

**哈希函数的单向性**让「正向计算」很容易、「反向」不可能。但如果预先把「明文 → 哈希」的结果全存下来查表，需要的空间是天文数字（例如小写字母 8 位就有 2000 亿条）。

**Hellman 的折中（time-memory trade-off）** 的思路：

1. 定义一个**归约函数 R**：把哈希值映射回一个「看起来像明文」的字符串（例如取哈希的某些字节，对字符集取模）。
2. 交替应用 `H`（哈希）与 `R`（归约），形成一条**链**：

```
明文 p0 ──H──→ h0 ──R──→ p1 ──H──→ h1 ──R──→ p2 ... ──H──→ hk
```

3. **只保存链的起点 `p0` 和终点 `hk`**，中间的全都丢掉。
4. 查表时：待破解哈希 `h` 先 `R`，再看结果是否等于某条链的终点；不等就继续 `H∘R` 迭代。一旦匹配上某条链的终点，就从该链的起点重跑一遍，中间就会经过我们要求的明文。

这样把「存所有哈希」变成「存每条链的两个端点」，空间大幅下降，代价是查询时要重跑链。

**彩虹表（rainbow table）是对 Hellman 的改进**：

- Hellman 方案里**所有链用同一个 R 函数**，容易产生链之间的**碰撞与合并**，导致有效覆盖率下降。
- Rainbow table 让**第 i 步用第 i 个不同的归约函数 `R_i`**。这样两条链只有在「同一步」才可能合并，碰撞概率大幅降低，覆盖率显著提升。

**一次查询是「查多条链」**：现代彩虹表由成千上万条链组成，查询时对每个可能的终点位置做匹配。

### 2.2 Ophcrack 的两个关键概念

**① 表（table）**：一个目录，里面是若干 `.bin` 文件（链的数据）+ `.index` 文件（加速查找）。Ophcrack 用 `-d` 指定表的基目录，用 `-t` 指定用哪些表。

```
-d /path/to/tables -t xp_free_fast,0,3:vista_free
   ↑                          ↑       ↑  ↑
 表目录                       表名   用第0、3号文件  第二个表名
```

**② 覆盖范围（coverage）**：每张表都有明确的「字符集 × 长度」定义，例如：

| 表名 | 覆盖 |
| --- | --- |
| `xp_free_fast` | LM / 字母数字，较短长度 |
| `xp_free_small` | LM，更长一点的字母数字 |
| `vista_free` | NTLM / 字母数字，较长长度 |
| `vista_proba` 等 | 付费表，覆盖更大字符集（含符号）与更长长度 |

**表的文件名通常就说明了它的覆盖范围**——选表之前先看名字。官方免费表的说明在 <https://ophcrack.sourceforge.net/tables.php>。

### 2.3 Ophcrack 的「双哈希」处理

Windows 的 SAM 里每个账户有 **LM 哈希 + NTLM 哈希**：

- **LM 哈希**：把口令切成两个 7 字符块，**全部转成大写**，用 DES 加密固定串。这导致：
  - 口令被**截断到 14 字符**；
  - **大小写不敏感**（`Password` 和 `PASSWORD` 的 LM 哈希相同）；
  - 只要口令是字母数字，就能用较小的表覆盖。
  - Vista 之后系统**默认禁用 LM**（SAM 里的值固定为 `aad3b435b51404eeaad3b435b51404ee`）。
- **NTLM 哈希**：大小写敏感、无长度截断，覆盖它需要大得多的表。

**Ophcrack 的实用策略**：先试 LM（快、表小），失败再试 NTLM（慢、表大）。GUI 版本会自动分两阶段跑，你可以从界面看到 "LM hash" / "NT hash" 两个进度条。

### 2.4 为什么表里没有就永远查不到

彩虹表是**有限集合的映射**。表的定义包含了：

- 哪个哈希算法（LM 还是 NTLM）；
- 使用哪些字符（例如只有小写+数字，还是含大小写）；
- 明文的最大长度。

如果你的口令**包含表里没有的字符**（例如 `@`、`!`），或者**长度超过表的定义**，那么无论跑多久都查不到——因为**表里根本不存在条目的起点**。

这与 hashcat 的掩码/字典模式形成鲜明对比：hashcat 只要时间够，理论上一定能穷尽。

### 2.5 与 hashcat 的速度对比

| 场景 | Ophcrack（有合适的表） | hashcat（GPU） |
| --- | --- | --- |
| LM、字母数字、≤ 14 位 | **秒级** | 秒级到分钟级 |
| NTLM、字母数字、≤ 8 位 | 秒级（需 `vista_*` 表） | 秒级 |
| NTLM、含符号、12 位 | **表里没有 = 无解** | 可行（小时量级） |
| 加盐算法（bcrypt/Argon2） | **不支持**（彩虹表对带盐哈希失效） | 支持但很慢 |

**彩虹表的一个根本限制**：**它只对「无盐哈希」有效**。因为每条链固定了明文，一旦加了盐，同一条链就要为每个盐重算一次——表会膨胀到不可行的规模。这解释了一个重要的防御原则：

> **加盐（salt）是抵御彩虹表最有效的手段**。现代所有口令存储方案（bcrypt、scrypt、Argon2、以及 Unix 的 `$6$`）都自带随机盐，因此都对彩虹表免疫。

## 3. 安装与快速上手

```bash
# GUI 版本
sudo apt install ophcrack

# 纯命令行版本
sudo apt install ophcrack-cli

ophcrack-cli -h
```

快速上手（命令行）：

```bash
# 1) 准备好表目录与哈希文件
#    哈希文件为 pwdump 格式（见 5.1 节）
# 2) 跑
ophcrack-cli -d /usr/share/ophcrack/tables -t vista_free -f hashes.txt
```

**关于彩虹表本身**：Kali 的 `ophcrack` 包**不包含表**。表需要另外获取：

| 来源 | 说明 |
| --- | --- |
| 官方免费表 | <https://ophcrack.sourceforge.net/tables.php> —— `xp_free_*`、`vista_free` 等，几百 MB 到数 GB |
| 官方付费表 | 覆盖更大字符集与长度，几十 GB 到 TB 级 |

**放置位置**：把解压后的表目录放到任意路径，用 `-d` 指向它即可。常见约定是 `/usr/share/ophcrack/tables/`。

```bash
# 示例：下载并解压官方 vista_free 表
sudo mkdir -p /usr/share/ophcrack/tables
cd /usr/share/ophcrack/tables
# 从官方页面下载 vista_free.zip 后：
sudo unzip vista_free.zip
ls
# vista_free/
```

> **务必从官方来源获取表**：彩虹表是二进制数据，第三方来源存在篡改风险（表被替换 → 查出的明文是错的，或包含恶意内容）。

## 4. 核心参数详解

`ophcrack` 与 `ophcrack-cli` 的参数**完全相同**（`-h` 输出一致），区别只在有没有 Qt 图形界面：

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-f FILE` | 从文件加载哈希（pwdump 或 session 格式） | **主入口** |
| `-w DIR` | 从目录加载加密的 SAM 文件 | 直接在 Windows 系统盘上跑时用 |
| `-d DIR` | 指定**表的基目录** | 必须与 `-t` 配合 |
| `-t table1[,a[,b,...]][:table2[,a,...]]` | 指定用哪些表、表里的哪些文件 | 语法见下 |
| `-g` | **禁用 GUI**（命令行模式） | 在 `ophcrack`（GUI 包）里跑批处理时**必加** |
| `-r` | 启动后立即开始破解（仅 GUI） | 配合 `-g` 做无人值守 |
| `-o FILE` | 以 pwdump 格式写出结果 | 结果落地，接后续流程 |
| `-l FILE` | 日志输出到文件 | 审计留档 |
| `-x FILE` | 导出 CSV 格式数据 | 做统计报表 |
| `-n NUM` | 使用 NUM 个线程 | 多核时调大 |
| `-p NUM` | 预加载级别：`0`=不预载，`1`=载索引，`2`=载索引+链尾，`3`=全部（默认） | 内存充足就保持 3；内存紧张降到 1 |
| `-A` / `-a` | 启用 / 禁用 **audit 模式**（默认禁用） | audit 模式先跑表再对未命中的做暴力，适合盘查 |
| `-B` / `-b` | 启用 / 禁用**暴力破解**（默认启用） | 表覆盖不全时靠暴力补，但很慢 |
| `-e` | 不显示空口令 | 输出更干净 |
| `-i` / `-I` | 隐藏 / 显示用户名（默认显示） | 只关心哈希时用 `-i` |
| `-q` | 安静模式 | 脚本化 |
| `-v` | 详细输出 | 排错 |
| `-D` | 大量调试信息 | 排查表加载失败 |
| `-u` | 破解结束时显示统计 | 生成报告 |
| `-c FILE` | 使用指定的配置文件 | 多套环境切换 |
| `-s` | 禁用会话自动保存 | — |
| `-S FILE` | 指定会话文件路径 | 长任务断点续跑 |
| `-C COMMAND` | 恢复 PIN 后执行命令（对应 reaver 的 `-C`，此处为 ophcrack 的会话命名参数之一，见本机 `-h`） | 以本机 `-h` 为准 |

> **注意**：`-C` 在不同版本含义可能不同。**以 `ophcrack-cli -h` 的实际输出为准**——本教程引用的输出见下方。

### `-t` 的语法详解

```text
-t 表名1[,文件号[,文件号...]][:表名2[,文件号...]]
```

| 写法 | 含义 |
| --- | --- |
| `-t vista_free` | 用 `vista_free` 表目录下**全部**文件 |
| `-t xp_free_fast,0,3` | 只用 `xp_free_fast` 表的第 0 和第 3 号文件 |
| `-t xp_free_fast,0,3:vista_free` | 两个表：前者只用 0/3 号文件，后者用全部 |

**为什么会有「文件号」**：大表被切成多个 `.bin`，每个覆盖不同的字符/长度区间。只跑一部分可以节省时间和内存。**先用完整的表跑**，除非你明确知道只需要某个区间。

### 官方 `-h` 输出（供对照）

```
ophcrack 3.8.0 by Objectif Securite (http://www.objectif-securite.ch)

Usage: ophcrack [OPTIONS]
Cracks Windows passwords with Rainbow tables

  -a              disable audit mode (default)
  -A              enable audit mode
  -b              disable bruteforce
  -B              enable bruteforce (default)
  -c config_file  specify the config file to use
  -D              display (lots of!) debugging information
  -d dir          specify tables base directory
  -e              do not display empty passwords
  -f file         load hashes from the specified file (pwdump or session)
  -g              disable GUI
  -h              display this information
  -i              hide usernames
  -I              show usernames (default)
  -l file         log all output to the specified file
  -n num          specify the number of threads to use
  -o file         write cracking output to file in pwdump format
  -p num          preload (0 none, 1 index, 2 index+end, 3 all default)
  -q              quiet mode
  -r              launch the cracking when ophcrack starts (GUI only)
  -s              disable session auto-saving
  -S session_file specify the file to use to automatically save the progress of the search
  -u              display statistics when cracking ends
  -t table1[,a[,b,...]][:table2[,a[,b,...]]]
                  specify which table to use in the directory given by -d
  -v              verbose
  -w dir          load hashes from encrypted SAM file in directory dir
  -x file         export data in CSV format to file

Example:	ophcrack -g -d /path/to/tables -t xp_free_fast,0,3:vista_free -f in.txt
```

## 5. 实战演练

**环境声明**：以下操作必须在**你自己的 Windows 虚拟机 / 你自己拥有的机器**上取得 SAM 哈希，或使用**专门设计的练习靶机**（例如自己用 `chntpw` 在虚拟机里改口令后导出 SAM）。**严禁**对任何非授权系统提取或破解 SAM。

### 场景 1：破解你自己虚拟机的 Windows 口令（GUI）

**步骤 1：在 Windows 虚拟机里创建几个测试账户**

在**你自己的** Windows 虚拟机里（非域环境，便于演示）：

```powershell
# 在 Windows 虚拟机中执行（管理员 PowerShell）
net user testuser1 pass123 /add
net user testuser2 Password /add
net user testuser3 qwerty12345 /add
```

**步骤 2：导出哈希（在虚拟机里用 pwdump 类工具）**

在合法的取证/测试流程中，通常通过以下方式取得 SAM：

| 方式 | 说明 |
| --- | --- |
| 离线挂载磁盘镜像 | 取证常用。挂载 VHD/VMDK，复制 `C:\Windows\System32\config\SAM` 与 `SYSTEM` |
| 内存镜像提取 | 用取证工具从内存 dump 中提取 |
| 虚拟机快照挂载 | 用 `libguestfs`/`guestfish` 挂载快照 |

**在 Kali 里从磁盘镜像提取**（针对你自己的虚拟机镜像）：

```bash
# 需要同时拿到 SAM 与 SYSTEM（SYSTEM 里有解密 SAM 所需的 boot key）
sudo apt install libguestfs-tools

# 查看镜像里的分区
sudo virt-filesystems -a ~/win-test.vmdk -l

# 复制出 SAM 与 SYSTEM
mkdir -p /tmp/reg
sudo guestfish --ro -a ~/win-test.vmdk -m /dev/sda2 \
  download /Windows/System32/config/SAM /tmp/reg/SAM : \
  download /Windows/System32/config/SYSTEM /tmp/reg/SYSTEM

ls -l /tmp/reg/
```

**从 SAM + SYSTEM 提取 pwdump 格式哈希**：

```bash
# 方式一：secretsdump（impacket 工具集，需另行安装）
sudo apt install python3-impacket
secretsdump.py -sam /tmp/reg/SAM -system /tmp/reg/SYSTEM LOCAL -outputfile /tmp/hashes

# 方式二：samdump2（Kali 自带）
sudo apt install samdump2
samdump2 /tmp/reg/SYSTEM /tmp/reg/SAM > /tmp/hashes-pwdump.txt
cat /tmp/hashes-pwdump.txt
```

**预期输出（pwdump 格式）**

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
testuser1:1001:aad3b435b51404eeaad3b435b51404ee:8b7b8c9c2e1a3d5f7b9c1e3a5d7f9b1c:::
testuser2:1002:aad3b435b51404eeaad3b435b51404ee:5f4dcc3b5aa765d61d8327deb882cf99:::
testuser3:1003:aad3b435b51404eeaad3b435b51404ee:1a1dc91c907325c69271ddf0c944bc72:::
```

格式：`用户名:UID:LM哈希:NTLM哈希:::`（7 个冒号字段）。

| 字段 | 解读 |
| --- | --- |
| `aad3b435b51404eeaad3b435b51404ee` | **空 LM 哈希**（Vista 之后 LM 默认禁用，固定填充） |
| `31d6cfe0d16ae931b73c59d7e0c089c0` | **空 NTLM 哈希**（Administrator 是空口令） |
| 后面 32 位 hex | 真实的 NTLM 哈希 |

**步骤 3：准备彩虹表**

```bash
sudo mkdir -p /usr/share/ophcrack/tables
cd /usr/share/ophcrack/tables
# 从 https://ophcrack.sourceforge.net/tables.php 下载 vista_free.zip 后：
sudo unzip vista_free.zip
ls -lh
```

**步骤 4：开始破解（GUI）**

```bash
ophcrack
```

界面流程：

1. **Load → PWDUMP file** → 选择 `/tmp/hashes-pwdump.txt`；
2. **Tables** 按钮 → 选择表目录（`/usr/share/ophcrack/tables`）→ 勾选 `vista_free`；
3. 点击 **Crack**；
4. 观察两个进度条：**LM hash** 阶段 → **NT hash** 阶段。

**预期结果**：`testuser2` 的 NTLM 哈希 `5f4dcc3b5aa765d61d8327deb882cf99`（即 `password`）应在 `vista_free` 表**几秒内**被查出。`testuser3` 的 `qwerty12345`（11 位）能否命中取决于表的覆盖长度定义——**这正是「表里没有就查不到」的直观体现**。

### 场景 2：命令行批处理（生产用法）

```bash
ophcrack-cli \
  -g \
  -d /usr/share/ophcrack/tables \
  -t vista_free \
  -f /tmp/hashes-pwdump.txt \
  -o /tmp/cracked-pwdump.txt \
  -l /tmp/ophcrack.log \
  -x /tmp/ophcrack.csv \
  -n 4 \
  -u
```

| 参数 | 作用 |
| --- | --- |
| `-g` | **禁用 GUI** —— 批处理必加 |
| `-d` / `-t` | 表目录与表名 |
| `-f` | 输入哈希文件 |
| `-o` | 结果以 pwdump 格式输出（**可再次被 ophcrack 或其他工具消费**） |
| `-l` | 日志 |
| `-x` | CSV 导出（做统计） |
| `-n 4` | 4 线程 |
| `-u` | 结束时打印统计 |

**预期输出片段**

```
ophcrack 3.8.0 by Objectif Securite
...
Found    1 hash(es) ...
testuser2:1002:aad3b435b51404eeaad3b435b51404ee:8b7b8c9c2e1a3d5f7b9c1e3a5d7f9b1c:password
```

**结果文件 `/tmp/cracked-pwdump.txt` 是标准 pwdump 格式**——这意味着你可以直接把它喂给下一步（比如用 [hashcat](hashcat.md) 对未命中的部分继续跑）。

### 场景 3：组合策略 —— 先表后算（最实用的打法）

Ophcrack 的最大价值是**快速筛掉弱口令**，让 [hashcat](hashcat.md) 把算力集中在剩下的硬骨头上。

**步骤 1：用 Ophcrack 筛一遍（秒级）**

```bash
ophcrack-cli -g -d /usr/share/ophcrack/tables -t vista_free:x11_free \
  -f /tmp/hashes-pwdump.txt -o /tmp/step1-solved.txt -q
```

**步骤 2：找出未命中的部分**

```bash
# 先取出所有 NTLM 哈希
cut -d: -f4 /tmp/hashes-pwdump.txt | sort -u > /tmp/all-ntlm.txt

# 取出已破解的口令对应的哈希...
# 更直接的做法：用 -o 输出的文件反推（ophcrack 会把破解出的明文追加到第 7 字段）
```

**步骤 3：把剩下的交给 hashcat**

```bash
hashcat -m 1000 -a 0 /tmp/left-ntlm.txt /usr/share/wordlists/rockyou.txt -O
hashcat -m 1000 -a 0 /tmp/left-ntlm.txt /usr/share/wordlists/rockyou.txt -r rules/best64.rule
```

**这个「表 + 算」的组合是 Windows 口令恢复的标准工作流**：表处理 80% 的弱口令（几秒），GPU 处理剩下的 20%（可能几小时）。

### 场景 4：理解「表选错就白跑」

**实验设计**：用同一个哈希，分别用「字符集不覆盖」的表去跑。

```bash
# 假设某口令是 "P@ssw0rd!"（含符号与感叹号）
# 1) 用只覆盖字母数字的免费表
ophcrack-cli -g -d /usr/share/ophcrack/tables -t vista_free -f /tmp/hashes-pwdump.txt
# 结果：查不到

# 2) 换上覆盖符号的表（需付费表）
# 结果：可能查到
```

**解读**：这不是工具的问题，而是**彩虹表的固有边界**。看到 `-t` 里表的名字（如 `*_free`）就该想到：**免费表 = 免费午餐不存在 = 覆盖范围有限**。

**结论**：**任何 `@`、`!`、`#` 或长度超过表定义的口令，Ophcrack 都无能为力**。这类口令必须交给 [hashcat](hashcat.md) 的掩码/字典/规则模式。

### 场景 5：Audit 模式（盘查所有账户）

```bash
ophcrack-cli -A -g -d /usr/share/ophcrack/tables -t vista_free -f /tmp/hashes-pwdump.txt
```

- `-A`（enable audit mode）：**对表未命中的哈希启动暴力破解**，尽量把所有账户都试出来（能试出来的前提下）。
- `-a`（默认）：只跑表，跑不出的就放弃——**速度优先**。

**选择建议**：

| 目标 | 用哪个 |
| --- | --- |
| 快速知道「有多少弱口令」 | `-a`（默认） |
| 取证场景，要求尽可能恢复 | `-A`（但耗时可能极长） |

## 6. 输出解读

### GUI 输出

| 界面元素 | 含义 |
| --- | --- |
| **User** 列 | 用户名 |
| **LM Hash** 列 | LM 哈希值 |
| **NT Hash** 列 | NTLM 哈希值 |
| **LM Pwd 1 / LM Pwd 2** | **破解出的 LM 口令被分成两半** —— 因为 LM 把口令切成两个 7 字符块分别加密。例如 `PASSWORD1234` 会显示成 `PASSWOR` + `D1234` |
| **NT Pwd** | 破解出的 NTLM 口令（大小写敏感，完整） |
| 两个进度条 | LM 阶段、NT 阶段 |
| `Found x/y` | 找到 x 个，共 y 个 |

**关键解读技巧**：

- **LM 的两半**把结果显示成两块，不要以为是两个不同的口令。看到 `LM Pwd 1` + `LM Pwd 2`，**拼起来**才是完整口令。
- **LM 结果全是大小写**：因为 LM 会把口令转成大写，所以 LM 破解出的明文**全部是大写**。真实口令的大小写可能不同——**以 NT 列的结果为准**。

### 命令行输出

```
Found    2 hash(es)
testuser2::8b7b8c9c2e1a3d5f7b9c1e3a5d7f9b1c:password
testuser1::a1b2c3d4e5f60718293a4b5c6d7e8f90:PASSWORD1234
```

| 字段 | 含义 |
| --- | --- |
| `Found N hash(es)` | **命中数量**——最重要的一行 |
| `用户名::哈希:明文` | pwdump 简化格式 |
| `-o` 输出的文件 | 与输入同格式，第 7 字段填入明文（**可被后续工具复用**） |
| `-u` 的统计 | 覆盖率、耗时等 |

**判断成功**：`Found` 数字 > 0；`-o` 文件里第 7 字段非空。

**下一步**：

| 情况 | 动作 |
| --- | --- |
| 全部命中 | 结束，生成报告 |
| 部分命中 | **未命中部分交给 [hashcat](hashcat.md)** —— 这是标准接力 |
| 全部未命中 | 检查：用了正确的表吗？哈希类型是 LM 还是 NTLM？表覆盖了字符集和长度吗？ |
| 大量账户显示空口令 | 立即上报（这是高危风险） |

## 7. 与其他工具配合

```text
[取得 SAM]  ← 磁盘镜像挂载 / 内存镜像 / 快照
        ↓
[提取哈希]  samdump2 / secretsdump.py  →  pwdump 格式
        ↓
[表筛第一遍] ophcrack-cli  →  秒级解出弱口令
        ↓（未命中的部分）
[算力第二遍] hashcat -m 1000  →  GPU 跑字典/掩码/规则
        ↓（仍未命中）
[结论]      强口令，或表/字典覆盖不足 → 如实汇报
```

**与其他教程的衔接**：

| 组合 | 说明 |
| --- | --- |
| **Ophcrack → [hashcat](hashcat.md)** | 最典型。表秒解弱口令，GPU 攻坚。`-o` 的输出可直接被 hashcat `--username` 读取 |
| **Ophcrack → [john](john.md)** | john 也能读 pwdump 格式（`--format=nt`），适合已有 john 工作流时 |
| **[hash-identifier](hash-identifier.md)** | 不确定是 LM 还是 NTLM 时先识别；但 pwdump 格式里 LM/NTLM 位置固定，一般不需要 |
| **[medusa](medusa.md)/[hydra](hydra.md) → Ophcrack** | 在线爆破拿到的口令可用于推测同组织其他人的口令结构（但在授权测试中这属于「口令复用」分析，需谨慎） |
| **[responder](../07-嗅探与欺骗/responder.md) → Ophcrack** | **不适用**：Responder 抓到的是 NetNTLM 挑战/响应，**不是** NTLM 哈希，不能用彩虹表，只能实时猜（hashcat `-m 5600`） |

**关于一个常见误解**：NetNTLM（`-m 5500`/`5600`）**不能**用 Ophcrack 破解。彩虹表只适用于**无盐的、纯粹的哈希值**。NetNTLM 是挑战-响应式，每次交互的挑战都不同，必须实时计算。

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `No tables found` / 找不到表 | `-d` 目录不对，或表未解压 | `ls -R /usr/share/ophcrack/tables` 检查；确认解压出了 `*.bin` 和 `*.index` |
| 表加载了但秒退 | 表名写错 | 表名是**目录名**，用 `ls` 核对 |
| `-t vista_free` 报找不到 | 表名大小写或拼写错 | 严格照目录名写 |
| 全部口令都显示为空 | pwdump 文件格式错，或 SAM/SYSTEM 不配套 | 先用 `cat` 看文件；SAM 与 SYSTEM 必须来自**同一台机器** |
| LM 结果只出现一半 | 正常行为 —— LM 是两块 | 把 `LM Pwd 1` 与 `LM Pwd 2` 拼起来 |
| LM 破出来全是大写 | **LM 的设计如此**（转大写） | 以 NT 列结果为准 |
| 表跑完了但什么都没找到 | 口令含符号/超长，超出表的覆盖范围 | 换覆盖更大的表，或改用 [hashcat](hashcat.md) |
| 内存爆了 / 系统卡死 | `-p 3`（全部预载）占用大量内存 | 降到 `-p 1`（只载索引） |
| 速度比预期慢很多 | 磁盘 I/O 瓶颈 | 把表放在 **SSD** 上；避免网络盘 |
| GUI 起不来（无 X 环境） | 服务器无图形 | 用 `ophcrack-cli` |
| `ophcrack` 在脚本里卡住 | 没加 `-g`，弹了 GUI | 脚本里**必须**加 `-g` |
| 结果被覆盖 | 多次运行指向同一 `-o` 文件 | 每次用不同文件名，或用 `-l` 分开记录 |
| 从第三方下载的表不好用/结果可疑 | 表被篡改 | **只从官方下载** <https://ophcrack.sourceforge.net/tables.php> |

## 9. 防御视角（蓝队）

Ophcrack 的**根本弱点是它依赖「无盐哈希」**。这直接给出了最有效的防御：

| 攻击者的做法 | 蓝队的对策 |
| --- | --- |
| 用彩虹表查 LM/NTLM 哈希 | **禁用 LM 哈希**（组策略：网络安全：不要在下次更改密码时存储 LAN Manager 的哈希值），并在注册表设置 `NoLMHash=1` |
| 用彩虹表查 NTLM | NTLM 无法加盐（协议决定），所以对策是**让哈希拿不到**（见下）+ **长口令**（超出表的覆盖） |
| 从磁盘镜像提 SAM | **BitLocker + TPM**：镜像加密后 SAM 拿不到；DPAPI/凭据保护 |
| 从内存提取 | **Credential Guard**（Windows 10+）隔离 LSASS 中的凭据 |
| 用短口令（表能覆盖） | **强制长度 ≥ 14**（管理员 ≥ 16）。表的覆盖长度上限通常就是 14（LM）——**超过 14 位，LM 直接失效** |
| 用字母数字口令 | 强制包含**符号**：多数免费表不覆盖符号，这直接让 Ophcrack 失效 |

### 一组具体的 Windows 加固措施

```powershell
# 1) 禁止存储 LM 哈希（组策略/注册表）
# 路径：计算机配置 → Windows 设置 → 安全设置 → 本地策略 → 安全选项
#   "网络安全: 不要在下次更改密码时存储 LAN Manager 的哈希值" → 已启用

# 2) 通过 PowerShell 检查当前策略
Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Lsa' -Name NoLMHash

# 3) 启用 Credential Guard（需 UEFI 锁 + 虚拟化安全）
Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard

# 4) 审计空口令账户（Ophcrack 输出里 31d6cfe0... 就是空口令）
Get-LocalUser | Where-Object { $_.Enabled -and $_.PasswordLastSet -eq $null }

# 5) 审计口令长度策略
net accounts
```

### 检测

| 信号 | 说明 |
| --- | --- |
| SAM/SYSTEM 注册表文件被复制 | 审计 `C:\Windows\System32\config\SAM` 的**读取**行为（非 `SYSTEM` 进程读取即告警）；Sysmon Event ID 1 + 文件访问审计 |
| 卷影副本被创建后立即访问 | `vssadmin create shadow` / `wmic shadowcopy call create` |
| LSASS 内存被读取 | Sysmon Event ID 10（ProcessAccess）+ `GrantedAccess 0x1010` 类掩码 |
| 磁盘镜像被挂载 | 对 BitLocker 未加密的机器，物理访问无法检测 → **所以必须用 BitLocker** |
| 离线破解本身 | **不可检测**（发生在攻击者自己的机器上） |

**蓝队核心结论**：

> Ophcrack 完美地展示了「**彩虹表 vs 加盐**」这场军备竞赛。加盐让彩虹表失去意义——这就是为什么 Unix 的 `$6$`、bcrypt、Argon2 全都自带随机盐。Windows 侧的对应措施是：**禁用 LM + BitLocker + Credential Guard + 长度 ≥ 14 + 强制符号**。

## 10. 参考

- 官方站点与彩虹表下载：<https://ophcrack.sourceforge.net/>、<https://ophcrack.sourceforge.net/tables.php>
- Kali 工具页：<https://www.kali.org/tools/ophcrack/>
- 本机手册：`man ophcrack`、`ophcrack -h`、`ophcrack-cli -h`（两者输出相同）
- 相关：[hashcat](hashcat.md)、[john](john.md)、[hash-identifier](hash-identifier.md)、[wordlists](wordlists.md)

## ⚠️ 法律与伦理

提取与破解他人计算机的 Windows 账户哈希，属于《中华人民共和国刑法》第二百八十五条第二款「非法获取计算机信息系统数据罪」的典型情形；若涉及入侵行为则同时构成第一款「非法侵入计算机信息系统罪」。《网络安全法》第二十七条亦明确禁止此类活动。**企业取证场景必须由有资质的主体按法定程序进行**，普通个人即使「只是看看」也已越线。

另需注意：**从第三方网站下载彩虹表存在供应链风险**（二进制数据、体积大、难以人工审阅），务必只从官方来源获取。

**本教程仅适用于**：你自己拥有的计算机（可用你自己的 Windows 虚拟机完整演练）、有书面授权的取证与渗透测试、CTF 靶场、教学演示。请勿对任何非自有设备提取或破解 SAM。
