# crunch（字典生成器）

> **一句话**：按字符集、长度、模式、字符重复限制等规则，生成定向口令字典。
> **分类**：口令攻击 ｜ **Kali 包**：`crunch` ｜ **官方文档**：<https://sourceforge.net/projects/crunch-wordlist/>

## 1. 它解决什么问题

字典是口令爆破的弹药。现成字典（[rockyou](wordlists.md)、[seclists](wordlists.md)）覆盖的是**大众化**口令习惯，但真实目标往往有**组织特有的口令规则**：

- 公司强制「大写开头 + 姓名 + 4 位数字」→ `Zhangwei2026`
- 设备默认口令是「厂商名 + 固定后缀」→ `huawei@123`
- 已知口令长度固定 8 位且只含小写字母和数字

这类**有结构**的口令，用 `crunch` 按规则生成，比用几十 GB 的通用字典高效得多。

与其他字典工具的分工：

| 工具 | 输入 | 输出 |
| --- | --- | --- |
| **crunch** | 字符集 / 模式 / 长度规则 | **穷举式**定向字典 |
| [cewl](cewl.md) | 一个网站 | 从网页文本中抽取的**词表** |
| [wordlists](wordlists.md) / [seclists](wordlists.md) | 现成字典 | 通用字典 |
| [hashcat](hashcat.md) `--stdout` | 掩码规则 | 与 crunch 同类，但生成速度更快 |

> 实务提示：如果只是要「按掩码生成」，`hashcat --stdout -a 3 '?u?l?l?l?l?d?d'` 通常比 crunch 快很多。crunch 的优势在于**模式占位符、字符重复限制、分片文件和管道直连**这些更细的控制。

## 2. 工作原理

crunch 的核心模型是：

```
从字符集的第 1 个字符开始，按「字典序」逐位递增，直到达到 max-len 的全字符组合
```

例如 `crunch 1 2 abc`：先输出 `a,b,c`，再到 `aa,ab,ac,ba,bb,bc,ca,cb,cc`。

- **总组合数** = `字符集大小 ^ 长度`（长度取 min 到 max 的每一档求和）。
- 默认字符集顺序是**小写字母 → 大写字母 → 数字 → 符号**，这个顺序不能乱，否则 `-t` 模式会错位。
- **`-t` 模式占位符**（这是 crunch 最实用的功能）：

| 占位符 | 插入 |
| --- | --- |
| `@` | 小写字母 |
| `,` | 大写字母 |
| `%` | 数字 |
| `^` | 符号 |

`crunch 8 8 -t @@@@%%%% ` 生成「4 位小写 + 4 位数字」的全部组合，正好匹配「abcd1234」这种常见企业口令结构。

- **`-p` 排列模式**：`crunch 4 5 -p dog cat bird` 生成的是 3 个词的**全排列**（`3! = 6` 个结果），而不是笛卡尔积。这是「口令是几个词拼起来」场景的正确工具，比 `hashcat -a 1` 更直观。
- **输出可分片**：`-b`（按大小）和 `-c`（按行数）配合 `-o START`，把巨大字典切成多个文件。
- **可管道**：不写 `-o` 时输出到 stdout，可以直接喂给 `aircrack-ng`、`airolib-ng`、`john --pipe`、`hashcat`。**这是 crunch 最有价值的用法**——避免把几十 GB 写到磁盘。

### 体积估算

`crunch` 启动时会先算给你看：

```
Crunch will now generate the following amount of data: 117440512 bytes
112 MB
0 GB
Crunch will now generate the following number of lines: 16777216
```

并且**会等 3 秒**再开始生成——这是给你按 `Ctrl-C` 的机会。看到这个提示一定要先算清楚：

```
2600 万个组合 × 每个 12 字节 ≈ 300 MB
26 个字符 ^ 8 位 ≈ 2.1 × 10^11 = 2088 亿个组合 × 10 字节 ≈ 2 TB
```

**这就是为什么大字典要管道给 hashcat 而不是写盘。**

## 3. 安装与快速上手

```bash
sudo apt install crunch
crunch -h                       # 极简，只有一句
man crunch | head -60           # 真正的文档在 man 里
```

快速上手：

```bash
# 6 位纯小写字母数字，写到文件
crunch 6 6 0123456789abcdef -o 6chars.txt

# 4 位小写 + 4 位数字，直接管道给 hashcat（不落盘）
crunch 8 8 -t @@@@%%%% | hashcat -m 0 -a 0 hashes.txt

# 3 个词的全排列
crunch 4 5 -p dog cat bird
```

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `<min-len>` | 最小长度（**必填**） | 即使不用也要写占位数字 |
| `<max-len>` | 最大长度（**必填**） | 与 min 相同即定长 |
| `[charset]` | 自定义字符集 | 顺序必须是：小写 → 大写 → 数字 → 符号；不用的类型用 `+` 占位 |
| `-o FILE` | 输出文件 | 写 `START` 可自动按块命名 |
| `-o START` | 自动分片命名 | 与 `-b` / `-c` 配合使用 |
| `-b number[type]` | 限定每个输出文件的大小 | 类型：`kb mb gb kib mib gib`；**数字与单位之间不能有空格**。需配 `-o START` |
| `-c number` | 限定每个输出文件的行数 | 需配 `-o START`；`-c 6000` = 每 6000 行一个文件 |
| `-t @,%^` | 模式占位符 | **最实用**：`@@@@%%%%` = 4 小写 + 4 数字 |
| `-l` | 配合 `-t` 时，把 `-t` 里的某些字符当**字面量** | 例如 `-t p@ss,%^` 想让 `@` 保持字面量时用 `-l` |
| `-d numbersymbol` | 限制**连续重复字符**的个数 | `-d 2@` = 小写字母最多连续 2 个，跳过 `aaa`；`-d 3%` = 数字最多连续 3 个 |
| `-s startblock` | 从指定字符串开始生成 | 断点续生成；**恢复时若不写 `-s`，务必先改名旧文件** |
| `-e string` | 在指定字符串处提前停止 | 只跑一部分区间时用 |
| `-i` | 反转输出顺序 | 默认 `aaa,aab,...`；加 `-i` 变成 `aaa,baa,caa,...` |
| `-p charset` 或 `-p w1 w2 ...` | **排列**模式（不重复字符的全排列） | **必须是最后一个选项**；不能与 `-s` 同用；min/max 长度被忽略但仍需写 |
| `-q FILE` | 从文件读词并做排列 | 类似 `-p`，但输入来自文件 |
| `-f FILE charset-name` | 从 `charset.lst` 加载预设字符集 | 预设文件在 `/usr/share/crunch/charset.lst` |
| `-r` | 从上次中断处恢复生成 | 只在用 `-o` 时有效；命令必须与原来完全一致（去掉 `-s`） |
| `-u` | 禁用百分比进度线程 | 输出重定向到管道时用（**会影响顺序**，慎用） |
| `-z gzip\|bzip2\|lzma\|7z` | 压缩输出 | gzip 最快，7z 最小（但 7z 不删原文件） |
| `--stdout` | 强制输出到 stdout | 管道场景显式声明 |

**`+` 占位符规则**：字符集参数里，如果你只想指定部分类型，其余用 `+` 占位。例如 `crunch 4 4 + + 123 + -t %%@^` 表示「数字集用 `123`，其余用默认集」。

## 5. 实战演练

**环境声明**：以下所有操作都在**你自己的机器**上生成**用于测试你自己系统**的字典。本教程不涉及对任何非授权目标的使用。

### 场景 1：定长穷举（基础）

**目标**：生成 6 位小写字母数字字典，用于测试你自己的 6 位 PIN 类口令。

```bash
# 1) 先估算规模
python3 -c "print('组合数:', 36**6, '≈', 36**6*7/1024/1024/1024, 'GB')"
# 组合数: 2176782336 ≈ 14.1 GB
```

14 GB 太大 → **不落盘，直接管道**给 hashcat：

```bash
crunch 6 6 0123456789abcdefghijklmnopqrstuvwxyz | hashcat -m 0 hashes.txt
```

**预期输出（crunch 部分）**

```
Crunch will now generate the following amount of data: 15237476352 bytes
14531 MB
14 GB
Crunch will now generate the following number of lines: 2176782336

crunch: 100% completed generating output
```

`hashcat` 会边收边算，磁盘不会被塞满。

### 场景 2：模式占位符（企业口令结构）

**目标**：你的靶场规定了「用户名首字母大写 + 4 位数字」，例如 `Abcd1234`。

```bash
# 4 位小写 + 4 位数字
crunch 8 8 -t @@@@%%%% -o /tmp/structure8.txt
wc -l /tmp/structure8.txt
# 456976
```

—— 只有 45 万条、约 4 MB，比 rockyou 的 1400 万条小得多，但**命中率会远高于**通用字典。

配合规则进一步变形：

```bash
crunch 8 8 -t @@@@%%%% | hashcat -m 0 -a 0 hashes.txt -r rules/toggles1.rule
```

**解读**：这体现了口令审计的核心方法论——**先用结构缩小空间，再用规则处理变形**。

### 场景 3：字符重复限制（排除不可能的候选）

**目标**：很多系统禁止「连续 3 个相同字符」，生成时应跳过 `aaa` 这类词。

```bash
# 5 位：3 小写 + 2 数字，但小写最多连续 2 个
crunch 5 5 -d 2@ -t @@@%% | head -20
```

**预期输出片段**

```
aab00
aab01
aab02
...
aac00        ← 注意没有 aaa**
```

对比 `crunch 5 5 -t @@@%%`（无 `-d`）会包含 `aaa00`。**用 `-d` 排除不可能的组合，等价于把字典压缩了**。

多个限制可以叠加：

```bash
crunch 10 10 -t @@@^%%%%^^ -d 2@ -d 3% -b 20mb -o START
```

### 场景 4：排列模式（口令是多词组合）

**目标**：口令是 2~3 个常见词的拼接。

```bash
crunch 1 1 -p dog cat bird
```

**预期输出**

```
birdcatdog
birddogcat
catbirddog
catdogbird
dogbirdcat
dogcatbird
```

**解读**：6 个结果 = `3!`，而不是 `3^3 = 27`。**排列模式跳过了「同一个词重复出现」的组合**，这正是人类设口令的行为习惯。

从文件读词：

```bash
cat > /tmp/words.txt <<'EOF'
Summer
Winter
Company
2026
EOF
crunch 1 1 -q /tmp/words.txt
```

### 场景 5：大字典分片 + 压缩

**目标**：必须落盘时（例如要交给别人用），切成固定大小并压缩。

```bash
crunch 8 8 abcdefghijklmnopqrstuvwxyz -o START -b 20mib -z gzip

ls -lh aaaa-*.txt.gz
# -rw-r--r-- 1 root root  18M aaaa-gvfed.txt.gz
# -rw-r--r-- 1 root root  18M gvfee-ombqy.txt.gz
# ...
```

| 参数 | 作用 |
| --- | --- |
| `-o START` | 文件名自动按「起始词-结束词」命名 |
| `-b 20mib` | 每个文件 20 MiB（`mib` 是 1024 进制，`mb` 是 1000 进制） |
| `-z gzip` | gzip 压缩 |

**断点续跑**：

```bash
# 原命令（假设跑到 dogcatbirdzy 中断）
crunch 1 5 -o START -c 6000

# 续跑：去掉原来的 -s，改成 -r
crunch 1 5 -o START -c 6000 -r
```

### 场景 6：从 charset.lst 加载预设字符集

```bash
grep -c '^#' /usr/share/crunch/charset.lst
head -20 /usr/share/crunch/charset.lst

# 使用预设字符集
crunch 8 8 -f /usr/share/crunch/charset.lst mixalpha-numeric-all-space -o /tmp/mixed.txt
```

`charset.lst` 里常用预设：`loweralpha`、`upperalpha`、`numeric`、`mixalpha`、`mixalpha-numeric`、`mixalpha-numeric-all-space`、`hex-lower`、`hex-upper`、`symbols14`、`ualpha-numeric` 等。

## 6. 输出解读

```
Crunch will now generate the following amount of data: 15237476352 bytes
14531 MB
14 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 2176782336
```

| 字段 | 含义 | 怎么用 |
| --- | --- | --- |
| `amount of data` | 预计总字节数 | **落盘前必看**——决定是否该改成管道 |
| `number of lines` | 预计总行数 | 除以破解速率 = 预估耗时 |
| `crunch: 100% completed generating output` | 生成完成 | 正常结束 |
| `crunch: 47% completed generating output`（`-o` 时每 10 秒打印） | 进度 | 估算剩余时间 |
| `Please press [Ctrl-C] to stop now`（启动后 3 秒） | 中止窗口 | 数字超预期时立即按 `Ctrl-C` |

**判断成功**：无报错 + 输出行数与预估一致（`wc -l` 核对）。

**下一步**：

- 行数远大于可用时间/空间 → 改用 `-t` 缩小结构，或直接管道给 hashcat。
- 生成的文件要给别人 → 先 `-z gzip`，再核对 `wc -l`。

## 7. 与其他工具配合

crunch 在管道里的价值最高（有官方文档明确支持的两条链路）：

```bash
# crunch → aircrack-ng（破解 WPA 握手包）
crunch 2 4 abcdefghijklmnopqrstuvwxyz | aircrack-ng /root/Mycapfile.cap -e MyESSID -w-

# crunch → airolib-ng（预计算 PMK 数据库）
crunch 10 10 12345 --stdout | airolib-ng testdb -import passwd -

# crunch → john（注意 --pipe 才支持规则）
crunch 8 8 -t @@@@%%%% | john --pipe --rules hashes.txt

# crunch → hashcat --stdout
crunch 8 8 -t @@@@%%%% | hashcat -m 0 -a 0 hashes.txt
```

**`-w-` 的含义**：告诉 aircrack-ng「字典从 stdin 读」。

完整的口令工作流：

```text
[结构情报] 目标强制口令规则（大写开头 + 4 位数字）
        ↓
[crunch 定向生成]  crunch 8 8 -t ,@@@%%%%
        ↓
[管道给破解器]    hashcat / john --pipe / aircrack-ng
        ↓
[规则变形补充]    叠加 rules 处理大小写与 l33t 替换
```

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| 磁盘被写满 | 用 `-o` 生成了几十 GB 字典 | 用 `--stdout` + 管道；或用 `-o START -b 20mib` 分片 |
| `crunch: error: You must specify a charset` | 字符集与长度参数个数不匹配 | 顺序必须是小写→大写→数字→符号；缺的类型用 `+` 占位 |
| `The maximum and minimum length should be the same size as the pattern you specified` | `-t` 模式里有需要转义的 shell 字符（`& * 空格 \ ( ) \| ' " ; < >`） | 用引号包起来或加 `\`：`crunch 4 4 -t "&*d@"` |
| 生成结果与预期不符 | 字符集**顺序写错** | 严格「小写 大写 数字 符号」，不用的用 `+` |
| `-p` 报错 | `-p` 不是最后一个参数，或与 `-s` 同用 | `-p` 必须放最后；不要与 `-s` 同用 |
| 生成到一半想接着来 | 中断 | 用 `-r` 续跑（**命令必须完全一致**，只是把 `-s` 换成 `-r`） |
| 输出文件少了几个 | 磁盘满，或文件名以 `.` 开头被「隐藏」 | `df -h` 查空间；`ls -la` 查隐藏文件 |
| `-z 7z` 后原文件还在 | 7z 不自动删除源文件 | 手动 `rm` |
| 管道给 john 时规则没生效 | 用了 `--stdin` 而非 `--pipe` | 管道 + 规则**必须**用 `john --pipe` |
| 想用 `-u` 提高速度但顺序乱了 | `-u` 会禁用进度线程，可能影响输出顺序 | 需要严格顺序时不要用 `-u` |
| crunch 生成速度慢 | 单线程实现 | 改用 `hashcat --stdout -a 3` 生成（快得多） |

## 9. 防御视角（蓝队）

crunch 是攻击者用来**为你的组织定制字典**的工具，所以蓝队要做的是**让这个字典无法生效**：

| 攻击者的做法 | 蓝队的对策 |
| --- | --- |
| 用 `-t @@@@%%%%` 生成「4 小写 + 4 数字」 | **禁止纯结构化的口令**：强制长度 ≥ 12、必须包含非常见词、禁止与用户名相关 |
| 用 `-p` 组合公司相关词、产品名、年份 | 禁止使用公司名/产品名/年份/季节等可猜元素 |
| 用 `-d` 排除不可能的候选以缩小空间 | 反向利用：**口令策略应主动排除低熵空间**，比如要求最小熵（可用 zxcvbn 之类的强度评估器强制） |
| 生成后离线跑 GPU | 部署**慢哈希**（bcrypt/scrypt/Argon2），让离线破解在时间上不可行 |
| 生成后在线爆破 | 失败计数 + 锁定 + MFA + 验证码 |

**口令策略建议（可落地的基线）**：

```text
长度 ≥ 12（管理员账号 ≥ 16）
禁止出现在已泄露口令库（Have I Been Pwned k-Anonymity API 或本地泄露库）
禁止包含用户名、公司名、产品名的任何变形
不使用周期性强制轮换（会促使用户选择可预测的规律，如 Summer2026 → Autumn2026）
所有远程入口强制 MFA
```

**关键洞察**：crunch 的价值在于「口令有规律」。**口令策略的目标就是消灭规律**。

## 10. 参考

- 官方项目页：<https://sourceforge.net/projects/crunch-wordlist/>
- Kali 工具页：<https://www.kali.org/tools/crunch/>
- 本机手册：`man crunch`、`crunch -h`（很短，**以 man 为准**）
- 预设字符集：`/usr/share/crunch/charset.lst`
- 相关：[wordlists](wordlists.md)、[cewl](cewl.md)、[hashcat](hashcat.md)、[john](john.md)、[hydra](hydra.md)

## ⚠️ 法律与伦理

使用本工具生成的字典对他人系统进行口令破解，可能构成《中华人民共和国刑法》第二百八十五条「非法侵入计算机信息系统罪」/「非法获取计算机信息系统数据罪」；《网络安全法》第二十七条亦明令禁止。字典生成本身合法，但**生成后如何使用决定其性质**。

**本教程仅适用于**：为自有系统做口令强度自查、有书面授权的渗透测试、CTF 靶场、教学演示。请勿将本文生成的字典用于任何未授权目标。
