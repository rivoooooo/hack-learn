# hashcat（GPU 加速哈希破解器）

> **一句话**：利用 GPU/CPU 并行算力对 300 多种哈希算法执行高速离线爆破，是目前最快的口令恢复工具。
> **分类**：口令攻击 ｜ **Kali 包**：`hashcat`（+ `hashcat-data`）｜ **官方文档**：<https://hashcat.net/hashcat/>

## 1. 它解决什么问题

[john](john.md) 强在「各种文件格式都能提取」，hashcat 强在「**提取完之后算得最快**」。

| | hashcat | john |
| --- | --- | --- |
| 目标 | 极致的每秒尝试数 | 极广的输入格式与易用性 |
| 硬件 | **GPU 优先**，多卡/分布式 | CPU 为主，GPU 支持有限 |
| 规则语言 | 极丰富（`rules/` 下上千条） | 类似，但生态较小 |
| 格式转换 | 需自备工具（`hcxtools`、`*2john`） | **自带上百个 `*2john`** |

标准分工：**用 john 的 `*2john` 提取哈希，用 hashcat 跑 GPU**。

## 2. 工作原理

### 2.1 五个要素

一次 hashcat 运行由五样东西决定：

```
hashcat  -m <哈希类型号>  -a <攻击模式号>  <哈希文件>  [字典/掩码/规则]  [其他选项]
          ↑                ↑
     告诉它算什么       告诉它怎么猜
```

- `-m`：哈希类型号。**写错 `-m` 一定跑不出结果**，且通常不会报错，只会静静地说 "Exhausted"。所以第一步永远是 `hashcat --identify file` 或 `hashcat -H`。
- `-a`：攻击模式号。
- 后面是候选口令来源（字典文件、掩码、规则）。

### 2.2 GPU 为什么快

GPU 有成千上万个简单核心，天生适合「同一套指令、海量数据并行」的哈希计算。hashcat 的关键工程手段：

- **Kernel**：每种哈希算法一个高度优化的计算内核。
- **Markov 链**：默认对掩码模式使用字符频率统计，把「更可能出现的字符」排在前面，从而在同样的 keyspace 里更早命中。
- **Bitmap（位图）**：跳过重复候选，避免做无用功。
- **规则引擎**：在 GPU 内部生成候选，不用 CPU 逐条喂数据。
- **Rules / Brain**：多机协同时用 brain 服务共享已尝试过的候选，避免重复计算。
- `-O`（optimized kernel）开启后速度大幅提升，但会**限制候选口令长度**（各算法上限不同）。长口令时不能开。
- `-w 1..4` 调节负载档位，换取速度与桌面响应性的平衡。

### 2.3 攻击模式

| `-a` | 模式 | 说明 |
| --- | --- | --- |
| `0` | Straight（字典） | 逐行读字典，可配 `-r` 规则 |
| `1` | Combination（组合） | 两个字典做笛卡尔积：`word1+word2` |
| `3` | Brute-force / Mask | 按掩码生成，如 `?a?a?a?a?a?a` |
| `6` | Hybrid Wordlist + Mask | 字典词 + 尾缀掩码，如 `password?d?d` |
| `7` | Hybrid Mask + Wordlist | 前缀掩码 + 字典词，如 `?d?dpassword` |
| `9` | Association | 用已知明文/规则关联推断同组哈希 |

> 说明：历史上还讨论过 `-a 2`（Toggle-Case）、`-a 4`（Permutation）、`-a 5`（Table-Lookup），但**当前版本的 help 里只列出 0/1/3/6/7/9**。不要照搬旧文档里的 `-a 2/4/5`。

### 2.4 常用哈希类型号

| `-m` | 算法 |
| --- | --- |
| `0` | MD5 |
| `10` | md5($pass.$salt) |
| `100` | SHA1 |
| `400` | phpass（WordPress / phpBB `$P$`） |
| `500` | md5crypt（Unix `$1$`、Cisco-IOS） |
| `1000` | NTLM |
| `1400` | SHA2-256 |
| `1700` | SHA512 |
| `1800` | sha512crypt（Unix `$6$`） |
| `3000` | LM |
| `3200` | bcrypt（`$2*$`） |
| `5500` / `5600` | NetNTLMv1 / NetNTLMv2 |
| `7300` | IPMI2 RAKP |
| `8900` | scrypt |
| `9400` / `9500` / `9600` | MS Office 2007 / 2010 / 2013 |
| `10500` | PDF（1.4–1.6） |
| `11600` | 7-Zip |
| `12500` / `13000` | RAR3-hp / RAR5 |
| `13100` | Kerberos 5 TGS-REP（etype 23，Kerberoasting） |
| `18200` | Kerberos 5 AS-REP（etype 23，ASREPRoasting） |
| `13600` | WinZip（AES） |
| `22000` | **WPA-PBKDF2-PMKID+EAPOL**（Wi-Fi WPA/WPA2 握手包，当前推荐） |

完整清单用 `hashcat -hh`（或 `--hash-info`）查询，特定类型细节用 `hashcat -H -m <号>`。

### 2.5 为什么速度差异是数量级级别的

同一个「8 位小写字母」候选空间，MD5 与 bcrypt 的耗时可能相差**上亿倍**。原因：

| 因素 | 影响 |
| --- | --- |
| 迭代次数 | md5crypt 迭代 1000 次、sha512crypt 迭代数千次 |
| 可调 cost | bcrypt 的 cost 每 +1，工作量翻倍 |
| 内存硬度 | scrypt/Argon2 需要大量内存，GPU 的并行度被显存带宽限制 |

**报告写法**：不要凭印象写数字。跑 `hashcat -b -m 0` 与 `hashcat -b -m 3200`，把输出的 `Speed.#1` 记录下来。

## 3. 安装与快速上手

```bash
sudo apt install hashcat
hashcat --version
hashcat -I                    # 检查可用后端设备（OpenCL/CUDA）
hashcat -b                    # 基准测试（先确认能用）
```

最小工作流：

```bash
# 1) 识别哈希类型
hashcat --identify hash.txt

# 2) 字典攻击
hashcat -m 0 -a 0 hash.txt /usr/share/wordlists/rockyou.txt

# 3) 看结果
hashcat -m 0 hash.txt --show
```

## 4. 核心参数详解

### 4.1 必需参数

| 参数 | 作用 | 建议 |
| --- | --- | --- |
| `-m, --hash-type N` | 哈希类型号 | **最容易出错的地方**，用 `--identify` 或 `-H` 确认 |
| `-a, --attack-mode N` | 攻击模式号 | 默认 `0`（字典） |
| `hashfile` | 含哈希的文件 | 每行一个；可带 `username:hash`，配 `--username` |
| `wordlist` / `mask` | 候选来源 | 字典路径或掩码字符串 |

### 4.2 常用运行控制

| 参数 | 作用 | 建议 |
| --- | --- | --- |
| `-o FILE` | 结果写文件 | 审计留档 |
| `--outfile-format=1,2,3` | 输出内容：1=hash[:salt]、2=plain、3=hex_plain | 只要明文用 `--outfile-format=2` |
| `--outfile-json` | JSON 输出 | 接自动化 |
| `-j` / `-k` | 左/右单条规则 | `-j 'c'` 大写首字母 |
| `-r FILE` | 规则文件 | `-r rules/best64.rule` 是性价比最高的一步 |
| `-1..-8` | 自定义字符集 `?1..?8` | `-1 '?l?d' -a 3 '?1?1?1?1?1?1'` |
| `-i` / `--increment` | 掩码递增 | `?a?a?a?a?a?a?a?a` 配 `-i --increment-max=8`，从小到大自动跑完 |
| `-s N` / `-l N` | 跳过 N 个 / 限制 N 个 | 分布式分片或限时任务 |
| `--keyspace` | 只打印 keyspace 不跑 | **跑之前先估工作量**，强烈建议 |
| `--runtime=N` | N 秒后停止 | 限时跑 |
| `--session=NAME` / `--restore` | 会话名 / 恢复 | 长任务必用 |
| `--status` / `--status-timer=1` | 状态屏 | 交互运行时按 `s` 亦可 |
| `--potfile-path` | 指定 pot 文件 | 项目隔离 |
| `--show` / `--left` | 显示已破解 / 未破解 | 汇报与排查 |
| `--username` | 忽略哈希行里的用户名部分 | `user:hash` 格式时必需 |
| `--remove` | 破解后从哈希文件删除该行 | 大批量任务 |
| `--force` | 忽略警告 | 只在明确知道后果时用 |
| `-w 1..4` | 负载档位（1 低 4 极高） | 桌面机用 `-w 2`；专用机 `-w 3` |
| `-O` | 优化内核（限制口令长度） | 短口令场景必开，速度提升明显 |
| `-D 1/2/3` | 设备类型：CPU/GPU/FPGA | `-D 2` 只用 GPU |
| `-d N` | 指定设备编号 | 多卡时用 |
| `-b` / `--benchmark` | 基准测试 | 拿真实速度数据 |
| `--self-test-disable` | 跳过自检 | 只在自检误报时用 |

### 4.3 内置字符集（掩码用）

| 符号 | 含义 |
| --- | --- |
| `?l` | `a-z` |
| `?u` | `A-Z` |
| `?d` | `0-9` |
| `?h` | `0-9a-f` |
| `?H` | `0-9A-F` |
| `?s` | 特殊符号 |
| `?a` | `?l?u?d?s` |
| `?b` | 全部 0x00–0xff 字节 |

## 5. 实战演练

**环境声明**：以下全部在**你自己的机器**上执行，使用的哈希来自你自己创建的测试文件、你自己的虚拟机、或你自建的靶场。**严禁对任何非授权哈希运行**。

### 场景 1：从零破解一个 MD5（入门，理解流程）

```bash
# 1) 造一个自己的测试哈希
printf '5f4dcc3b5aa765d61d8327deb882cf99' > /tmp/md5.txt   # "password" 的 MD5

# 2) 让 hashcat 猜类型
hashcat --identify /tmp/md5.txt
# The following hash-mode match the hash: 0

# 3) 先估工作量（掩码模式）
hashcat -m 0 -a 3 --keyspace '?l?l?l?l?l?l'
# 308915776

# 4) 字典攻击
hashcat -m 0 -a 0 /tmp/md5.txt /usr/share/wordlists/rockyou.txt -O -w 2

# 5) 看结果
hashcat -m 0 /tmp/md5.txt --show
# 5f4dcc3b5aa765d61d8327deb882cf99:password
```

### 场景 2：字典 + 规则（实战中最常用的一步）

规则能把小字典放大成很多倍**且命中率更高**的候选集。

```bash
# 只用 10 万词的字典
hashcat -m 0 -a 0 /tmp/md5.txt /usr/share/wordlists/rockyou.txt -r rules/best64.rule

# 叠加多条规则
hashcat -m 0 -a 0 hashes.txt dict.txt -r rules/best64.rule -r rules/toggles1.rule

# 内联规则（左规则把首字母大写）
hashcat -m 0 -a 0 hashes.txt dict.txt -j 'c'
```

**解读**：如果「裸字典」跑不出但「字典 + best64」跑出来了，说明目标的换词习惯就在规则的覆盖范围内——这本身是一条有价值的情报。

### 场景 3：掩码与混合模式（已知口令结构）

```bash
# 已知是 4 位小写 + 4 位数字
hashcat -m 0 -a 3 hashes.txt '?l?l?l?l?d?d?d?d'

# 已知是「常见词 + 4 位数字」
hashcat -m 0 -a 6 hashes.txt dict.txt '?d?d?d?d'

# 已知是「年份前缀 + 常见词」
hashcat -m 0 -a 7 hashes.txt '?d?d?d?d' dict.txt

# 不确定长度：从 1 位到 10 位自动递增
hashcat -m 0 -a 3 hashes.txt '?a?a?a?a?a?a?a?a?a?a' -i --increment-min=1 --increment-max=10
```

**注意**：`-i` 配合 `?a` 时空间增长极快，务必先用 `--keyspace` 估算。

### 场景 4：Wi-Fi 握手包（与无线教程衔接）

```bash
# 由 airodump-ng 得到的 .cap，转成 hashcat 22000 格式
hcxpcapngtool -o ~/wifi.22000 ~/capture-01.cap
# 或用 aircrack-ng 直接产出（见 aircrack-ng -j / -I）

hashcat -m 22000 ~/wifi.22000 /usr/share/wordlists/rockyou.txt -O
hashcat -m 22000 ~/wifi.22000 --show
```

WPA 用的是 **PBKDF2-HMAC-SHA1，迭代 4096 次**，所以单个候选的成本远高于裸 MD5——这类任务的推荐做法是：**先用小字典 + 规则试，不行再上 GPU 长时间跑**。

### 场景 5：基准测试（写报告用）

```bash
hashcat -b -m 0        # MD5
hashcat -b -m 1000     # NTLM
hashcat -b -m 1800     # sha512crypt
hashcat -b -m 3200     # bcrypt
```

记录 `Speed.#1.........: xxxx H/s`。**只有这个数字才是可复现的**。

## 6. 输出解读

```
hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 CUDA 12.2) - Platform #1 [NVIDIA Corporation]
* Device #1: NVIDIA GeForce RTX 3060, 11956/12288 MB (3000 MB allocatable), 28MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 31

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 64

Status...........: Cracked
Hash.Mode........: 0 (MD5)
Hash.Target......: 5f4dcc3b5aa765d61d8327deb882cf99
Time.Started.....: Mon Sep 15 10:30:00 2026 (2 secs)
Time.Estimated...: Mon Sep 15 10:30:02 2026 (0 secs)
Kernel.Feature...: Optimized Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Mod........: Rules (rules/best64.rule)
Speed.#1.........:  8920.9 MH/s (34.02ms) @ Accel:32 Loops:64 Thr:512 Vec:1
Recovered........: 1/1 (100.00%) Digests
Progress.........: 14344384/14344384 (100.00%)
Rejected.........: 0/14344384 (0.00%)
Restore.Point....: 14344384/14344384 (100.00%)
Candidates.#1....: qwertyui -> qwerty
```

| 字段 | 含义 | 怎么用 |
| --- | --- | --- |
| `Device #1: ... 12288 MB (3000 MB allocatable)` | 显卡与可用显存 | 如果 `allocatable` 很小，说明系统还有其他 GPU 占用 |
| `Maximum password length supported by kernel: 31` | 当前 `-O` 下支持的最大长度 | 目标口令可能更长时**不要开 `-O`** |
| `Rules: 64` | 实际生效的规则条数 | 规则没加载成功时可发现 |
| `Status: Cracked` / `Exhausted` | **破解成功 / 候选空间已跑完仍未命中** | `Exhausted` 就是要换策略的信号 |
| `Speed.#1: 8920.9 MH/s` | 每秒多少百万次哈希 | 报告里的速度数据 |
| `Recovered: 1/1 (100.00%)` | 命中率 | 批量任务关注这个 |
| `Progress: 100.00%` | keyspace 进度 | 估算剩余时间 |
| `Candidates.#1` | 当前正在尝试的候选样例 | 排错用 |

**判断成功**：`Status...........: Cracked`。

**下一步**：

- `Exhausted` → 换字典、加规则、加掩码位置，或换攻击模式。
- 速度太低 → 检查 `-O`、`-w`、`-D 2`（只用 GPU）。
- 出现 `WARN: Not Enough Free Device Memory` → 减小 `-n`/`-u`/`--kernel-accel`。

## 7. 与其他工具配合

```text
[提取哈希]  john 的 *2john / unshadow / hcxpcapngtool / secretsdump
        ↓
[识别类型]  hashcat --identify  →  拿到 -m 号
        ↓
[小字典试探] hashcat -a 0 dict.txt -r rules/best64.rule
        ↓（没出）
[掩码/混合]  -a 3 / -a 6 / -a 7 / -i 递增
        ↓（没出）
[大规模]  分布式（--brain / -s -l 分片）或等待
        ↓
[回填报告] hashcat --show / --left
```

与其他教程的衔接：

- **无线**：[airodump-ng](../05-无线攻击/airodump-ng.md) 抓包 → [aircrack-ng](../05-无线攻击/aircrack-ng.md) 或 `hcxpcapngtool` 转 → hashcat `-m 22000`。
- **嗅探**：[responder](../07-嗅探与欺骗/responder.md) 抓 NetNTLMv2 → hashcat `-m 5600`。
- **口令攻击内部**：[crunch](crunch.md) 生成定向字典 → `hashcat -a 0`；[cewl](cewl.md) 爬站造字典 → `hashcat -a 6`。

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `No devices found/left` | OpenCL/CUDA 驱动未装 | 安装显卡厂商驱动 + `pocl-opencl-icd`（CPU）或 `nvidia-opencl-icd`；`hashcat -I` 确认 |
| `CL_OUT_OF_RESOURCES` / `Not enough free device memory` | 显存不足 | 降 `-n`、`-u`、`-w`；关掉占显存的其他程序；`--backend-devices-keepfree` |
| 一直 `Exhausted` 但字典里确实有 | `-m` 号写错 | `hashcat --identify` 或 `hashcat -H -m 0` 核对 |
| `Token length exception` / `Separator unmatched` | 哈希文件格式不对（多了换行、冒号、用户名） | 清理文件；`user:hash` 时加 `--username` |
| 开了 `-O` 后跑不出长口令 | 优化内核对口令长度有限制 | 去掉 `-O`；看 `Maximum password length supported by kernel` |
| GPU 温度报警 / 降频 | 负载档位过高 | `-w 2`，`--hwmon-temp-abort=90` |
| 破解慢得不像 GPU | 实际跑在 CPU 上 | `-D 2` 强制 GPU；`hashcat -I` 看设备列表 |
| 规则文件报错 | 规则语法或路径错 | 用 `-r /usr/share/hashcat/rules/best64.rule` 绝对路径 |
| 掩码里 `?` 被 shell 吞掉 | 未加引号 | 掩码**必须**加单引号：`'?d?d?d?d'` |
| `--keyspace` 之后进程仍在跑 | `--keyspace` 应单独用 | 别和 `-a 0` 字典模式混用 |
| WPA 破解极慢 | PBKDF2 迭代 4096 次，成本高 | 正常；用规则而非长度扩充，优先小字典 |
| 中文口令跑不出来 | 编码问题 | `--encoding-from` / `--encoding-to` 指定编码 |

## 9. 防御视角（蓝队）

| 风险 | 检测 | 缓解 |
| --- | --- | --- |
| GPU 大规模离线破解 | 攻击者在**自己机器**上跑，你的网络里看不到——所以**不能靠流量检测** | 唯一有效防线是让哈希「难拿」和「难算」 |
| 弱哈希算法 | 审计数据库/配置中的哈希前缀：`$1$`(md5crypt)、裸 MD5、LM | 迁移到 bcrypt/scrypt/Argon2；Windows 禁用 LM 并启用 Credential Guard |
| WPA 握手包被抓 | 检测 deauth 洪泛（它是抓握手的常用前置动作） | WPA3-SAE；启用 802.11w（PMF）；对 deauth 告警 |
| NetNTLM 哈希被抓 | 检测 LLMNR/NBT-NS/mDNS 应答异常 | 禁用 LLMNR 与 NBT-NS、强制 SMB 签名 |
| 口令可被规则命中 | 定期自己做口令审计（需授权） | 强制长度 ≥ 12、禁用高风险词库、MFA |

**蓝队要点**：hashcat 是在对手自己的硬件上跑的，**网络上没有可观测的流量特征**。这正说明：

> 口令安全 = 哈希不可获取（访问控制、最小权限） + 哈希不可计算（慢哈希、长口令、MFA）。

## 10. 参考

- 官方文档与 wiki：<https://hashcat.net/hashcat/>、<https://hashcat.net/wiki/>
- Kali 工具页：<https://www.kali.org/tools/hashcat/>
- 本机手册：`man hashcat`、`hashcat -h`、`hashcat -hh`、`hashcat -H -m <号>`、`hashcat -I`
- 本机规则目录：`/usr/share/hashcat/rules/`
- 相关：[john](john.md)、[hash-identifier](hash-identifier.md)、[wordlists](wordlists.md)、[crunch](crunch.md)

## ⚠️ 法律与伦理

未经授权获取、破解他人口令哈希，属于《中华人民共和国刑法》第二百八十五条第二款「非法获取计算机信息系统数据罪」的典型情形；《网络安全法》第二十七条亦明确禁止此类活动。即使只是「跑一下看看」，只要目标不是你的，就已经越线。

**本教程仅适用于**：你自己系统的口令强度自查、有书面授权的渗透测试、CTF 靶场、教学演示。请务必注意：**拿着别人给的哈希文件去破解，同样违法。**
