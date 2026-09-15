# hash-identifier（哈希类型识别）

> **一句话**：输入一段哈希值，通过长度与字符集特征推断它可能是哪种算法，从而决定用哪个破解模式。
> **分类**：口令攻击 ｜ **Kali 包**：`hash-identifier` ｜ **官方文档**：<https://github.com/blackploit/hash-identifier>

## 1. 它解决什么问题

破解流程里最容易出错、也最容易被忽略的一步是**确定哈希类型**。

以 [hashcat](hashcat.md) 为例：`-m` 写错不会报错，只会静静地跑完然后告诉你 `Exhausted`——你花了两小时，结果是错的。

以 [john](john.md) 为例：格式识别失败时会直接说 `No password hashes loaded`。

**判断哈希类型为什么难**：哈希输出是**定长十六进制（或 base64）串，本身不带任何算法标识**。例如：

```
5f4dcc3b5aa765d61d8327deb882cf99
```

长度 32、纯十六进制 → 可能是 MD5、NTLM、MD4、LM 的一半、各种 MD5 变体……**单看这串字符，你无法区分**。能做的只有「按长度和字符集排除不可能项，给出候选列表」。

hash-identifier 就做这件事：一个交互式 Python 脚本，把输入与内置特征库比对，输出「可能的哈希类型」和「可能性较低的类型」。

### 它的局限（必须先说清楚）

| 局限 | 说明 |
| --- | --- |
| **只靠长度与字符集** | 32 位十六进制永远会同时匹配 MD5、NTLM、MD4 等一大堆 |
| **不能确认** | 输出的是候选，不是答案。**真正的确认靠上下文** |
| 交互式 | 只有一个输入框，不适合脚本批量处理 |
| 项目较老 | 更新不频繁，新算法（如 Argon2、yescrypt）覆盖有限 |

**判断哈希类型的正确顺序**：

```text
1) 看上下文 ← 最重要！
   哈希是从哪来的？Windows SAM → NTLM；/etc/shadow → crypt；数据库 → 看应用框架
        ↓
2) 看前缀/格式
   $1$ → md5crypt    $2a$/$2b$ → bcrypt    $6$ → sha512crypt
   $P$ → phpass      $apr1$ → Apache MD5
        ↓
3) 看长度与字符集（hash-identifier 在这里发挥作用）
        ↓
4) 交叉验证
   用 john / hashcat 的识别功能，或用 hashid / haiti 等更现代的替代品
```

## 2. 工作原理

### 2.1 特征匹配

hash-identifier 内置一张表，每条记录描述一种算法哈希的**长度**和**字符集限制**。输入一串字符后：

1. 计算长度、判断字符集（十六进制 / base64 / 其他）；
2. 遍历特征表，把匹配的算法分别归入「Possible（可能）」和「Least Possible（可能性较低）」两组；
3. 「Possible」通常对应**长度完全吻合且字符集明确**的算法；「Least Possible」是**长度也吻合但需要额外条件**的算法（例如带固定前缀、带盐、是某个变体）。

以官方示例的输入 `098f6bcd4621d373cade4e832627b4f6`（32 位十六进制）为例：

```
Possible Hashs:
[+]  MD5
[+]  Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))

Least Possible Hashs:
[+]  RAdmin v2.x
[+]  NTLM
[+]  MD4
[+]  MD2
[+]  MD5(HMAC)
...
[+]  md5($salt.$pass)
[+]  md5(md5($pass))
...
```

**如何解读这个结果**：

- 32 位十六进制 = 128 位输出 → 所有 MD4/MD5 家族的算法都符合，所以列表长得出奇。
- `MD5` 进了 Possible，`NTLM` 进了 Least Possible —— 这是因为 NTLM 的哈希**没有固定前缀**但**上下文通常是 Windows**；工具用启发式把「裸 32 位十六进制」优先判为 MD5。
- 这一屏输出**对新手最有价值的其实是那串长长的 Least Possible 列表**：它告诉你「光靠这串字符，这些都有可能」，从而让你意识到**必须去找上下文**。

### 2.2 常见哈希的特征（比工具更好用的知识）

| 前缀 / 长度 | 算法 | hashcat `-m` | john `--format=` |
| --- | --- | --- | --- |
| 32 位 hex（无前缀） | MD5 | 0 | raw-md5 |
| 32 位 hex（无前缀） | NTLM | 1000 | nt |
| 40 位 hex | SHA-1 | 100 | raw-sha1 |
| 64 位 hex | SHA-256 | 1400 | raw-sha256 |
| 128 位 hex | SHA-512 | 1700 | raw-sha512 |
| `$1$` 开头 | md5crypt（Unix、Cisco） | 500 | md5crypt |
| `$2a$` / `$2b$` / `$2y$` | bcrypt | 3200 | bcrypt |
| `$5$` | sha256crypt | 7400 | sha256crypt |
| `$6$` | sha512crypt | 1800 | sha512crypt |
| `$P$` / `$H$` | phpass（WordPress、phpBB） | 400 | phpass |
| `$apr1$` | Apache MD5 | 1600 | md5crypt（变体） |
| `{SSHA}` | LDAP SSHA | 111 | ldap（限长） |
| `aad3b435b51404eeaad3b435b51404ee` | **LT/PtH 空 LM 哈希** | — | — |
| 32 位 hex 且来自 Windows SAM | NTLM | 1000 | nt |
| 48 位 hex（`0x`前缀） | MySQL 4.1+（`mysql_native_password`） | 300 | mysql |
| `*` + 40 位 hex | MySQL 4.1+ 带星号 | 300 | mysql |
| `$argon2i$` / `$argon2id$` | Argon2 | 34000 | — |
| `$y$` | yescrypt | — | yescrypt |

**关键观察**：凡是**带 `$算法$` 前缀**的，格式自带标识，**根本不需要 hash-identifier**。真正需要识别工具的只有那些**裸的十六进制串**。

### 2.3 Windows 场景的一个实用技巧

Windows 的 `SAM` 里存放的是 **LM 哈希 + NTLM 哈希** 两个 32 位十六进制值，用 `:` 连接：

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
                                 ↑ LM（全 aad3b... 表示 LM 哈希被禁用）    ↑ NTLM
```

- `aad3b435b51404eeaad3b435b51404ee` 是「空口令的 LM 哈希」，在 Vista 之后系统默认禁用 LM，所以这个值是**固定填充**。
- `31d6cfe0d16ae931b73c59d7e0c089c0` 是「空口令的 NTLM 哈希」。

**这两个值是固定的**——看到它们就知道该账户**当前是空口令**，不需要破解。

## 3. 安装与快速上手

```bash
sudo apt install hash-identifier
hash-identifier
```

启动后是**交互式**的：粘贴哈希，回车，看输出。

```
   #########################################################################
   #     __  __             __       ______    _____                       #
   #    /\ \/\ \           /\ \     /\__  _\  /\  _ `\                     #
   #    \ \ \_\ \     __      ____ \ \ \___ \/_/\ \/  \ \ \/\ \            #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.1 #
   #                                 By Zion3R                            #
   #                            www.Blackploit.com                        #
   #                               Root@Blackploit.com                    #
   #########################################################################

   -------------------------------------------------------------------------
 HASH: 098f6bcd4621d373cade4e832627b4f6
```

**注意**：hash-identifier **没有实质性的命令行参数**。官方文档里 `hash-identifier -h` 也只是打印 banner 然后继续等输入（输出里显示 `Not Found.` 后接着 `HASH:`）——说明它把 `-h` 当成了待识别的哈希输入。**不要指望用它做批处理。**

### 更现代的替代品

| 工具 | 优势 | 安装 |
| --- | --- | --- |
| `hashcat --identify` | 与 hashcat 的 `-m` 号**直接对应**，最实用 | 自带（hashcat 包） |
| `john --show=formats` | 针对 john 已加载的哈希文件 | 自带（john 包） |
| `hashid` | 可脚本化，支持 `-m` 输出 hashcat 模式号 | `pipx install hashid` |
| `haiti` | 特征库较新，输出清晰 | `gem install haiti-hash` |

**推荐工作流**：

```bash
# 首选：hashcat 直接识别（输出就是 -m 号）
hashcat --identify hash.txt

# 补充：hashid 支持批量与脚本化
hashid -m '098f6bcd4621d373cade4e832627b4f6'

# 交互式看候选列表
hash-identifier
```

## 4. 核心参数详解

hash-identifier 本身没有可配置参数。因此下表列出**替代工具的实用参数**——这才是能落地的东西。

### 4.1 `hashcat --identify`

| 参数 | 作用 | 建议 |
| --- | --- | --- |
| `--identify <file>` | 识别文件里每行哈希的类型 | 输出直接给出 `-m` 号 |
| `--identify` 配合 `--username` | 忽略 `user:hash` 的用户名部分 | 文件含用户名时**必须**加 |
| `hashcat -H -m <号>` | 查看某模式的详细说明与示例哈希 | 确认 `-m` 是否选对 |
| `hashcat -hh` | 列出所有支持的哈希模式 | 探索 |

### 4.2 `hashid`

| 参数 | 作用 | 建议 |
| --- | --- | --- |
| `hashid <hash>` | 识别单个哈希 | — |
| `-m` / `--mode` | 以 hashcat 模式号格式输出 | 直接抄进 hashcat 命令 |
| `-j` / `--john` | 以 john 格式输出 | 配 john |
| `-f <file>` | 从文件批量识别 | **批量场景首选** |
| `-e` / `--extended` | 显示扩展哈希列表 | 需要更多候选时 |
| `-o <file>` | 输出到文件 | 生成报告 |

### 4.3 `john` 侧的识别

| 参数 | 作用 | 建议 |
| --- | --- | --- |
| `john --show=formats hashfile` | 以 JSON 打印 john 对每个哈希的格式判断 | 不确定格式时的第一站 |
| `john --list=formats` | 列出 john 支持的全部格式名 | 配合 `--format=` 使用 |
| `john --list=subformats` | 列出 `--format=crypt` 的子格式 | — |

### 4.4 手工判断速查（比任何工具都可靠的部分）

| 观察 | 结论 |
| --- | --- |
| 有 `$2b$12$` 这类前缀 | bcrypt，cost 是中间那个数（12） |
| 有 `$6$` 前缀 | sha512crypt |
| **没有前缀**、32 位 hex | MD5 或 NTLM —— **看来源定**（Windows 用 `-m 1000`，Unix Web 应用用 `-m 0`） |
| 32 位 hex，来自 `SAM`/`secretsdump` | NTLM（`-m 1000`） |
| 48 位 hex | MySQL `mysql_native_password`（`-m 300`） |
| 40 位 hex | SHA-1（`-m 100`） |
| base64 结尾带 `=` 且长度 24 | 常见于某些应用的自定义方案，需看源码 |

## 5. 实战演练

**环境声明**：本节使用的哈希均由**你自己在本地生成**。**严禁**对从非授权途径获得的哈希进行识别与破解。

### 场景 1：生成一批已知类型的哈希，验证识别结果

**步骤 1：用自己的工具生成对照样本**

```bash
# 用 openssl 生成各种哈希
printf 'password' | openssl dgst -md5        # 32 hex  → MD5
printf 'password' | openssl dgst -sha1       # 40 hex  → SHA-1
printf 'password' | openssl dgst -sha256     # 64 hex  → SHA-256
printf 'password' | openssl dgst -sha512     # 128 hex → SHA-512

# 用 john 自带的工具生成 Unix crypt 风格
openssl passwd -1 -salt abcd password        # $1$abcd$...  → md5crypt
openssl passwd -5 -salt abcd password        # $5$abcd$...  → sha256crypt
openssl passwd -6 -salt abcd password        # $6$abcd$...  → sha512crypt
```

**预期输出示例**

```
5f4dcc3b5aa765d61d8327deb882cf99
5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb9...
$1$abcd$8FQd/rJ1lVwLpZ2mHMR0k.
$5$abcd$uJ0YM1qPDGZ5r1eWuMYq...
$6$abcd$YYSH0y1UBHtHiNB0aC7Q...
```

**步骤 2：用 hashid 批量识别**

```bash
cat > /tmp/samples.txt <<'EOF'
5f4dcc3b5aa765d61d8327deb882cf99
5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
$1$abcd$8FQd/rJ1lVwLpZ2mHMR0k.
$6$abcd$YYSH0y1UBHtHiNB0aC7Q...
EOF

hashid -m -f /tmp/samples.txt
```

**步骤 3：用 hashcat 交叉验证**

```bash
hashcat --identify /tmp/samples.txt
```

**解读**：

- **带前缀的两行**（`$1$`、`$6$`）会被准确识别——因为格式自带标识。
- **裸十六进制行**会出现多个候选（MD5/SHA-1/SHA-256 之间按长度区分，所以这次能分开；但 32 位那行在 MD5 与 NTLM 之间无法区分）。

### 场景 2：交互式使用 hash-identifier（理解它的输出结构）

```bash
hash-identifier
```

在 `HASH:` 提示后粘贴：

```
098f6bcd4621d373cade4e832627b4f6
```

**预期输出**（节选）

```
Possible Hashs:
[+]  MD5
[+]  Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))

Least Possible Hashs:
[+]  RAdmin v2.x
[+]  NTLM
[+]  MD4
[+]  MD2
[+]  MD5(HMAC)
...
```

**正确的解读方式**：

1. 这**不是**「答案是 MD5」——而是「最可能是 MD5，但也可能是列出的其他所有算法」。
2. 真正决定答案的是**上下文**：如果这串哈希来自 Linux Web 应用的数据库 → MD5（`-m 0`）；如果来自 Windows SAM → NTLM（`-m 1000`）。
3. **实践结论**：遇到「二者皆可」的情况，**两个都试一次**。跑 `-m 0` 和 `-m 1000` 各几秒钟，成本远低于纠结。

按 `Ctrl+C` 退出。

### 场景 3：从「已知格式」反推场景（真实工作流）

**情境**：你在自己的靶机上拿到了 `/etc/shadow` 的一行：

```
webapp:$6$rBzL1NJv$J8j9mGqK0a9WvV5N7lT3xO2yQ1cZ4bF6dH8iE0gS2kU4nP6tR9sA1dF3gH5jK7lZ9x:19000:0:99999:7:::
```

**步骤 1：看前缀 → `$6$` → sha512crypt**，不需要任何工具。

**步骤 2：hash-identifier 确认**

```
HASH: $6$rBzL1NJv$J8j9mGqK0a9WvV5N7lT3xO2yQ1cZ4bF6dH8iE0gS2kU4nP6tR9sA1dF3gH5jK7lZ9x
```

**步骤 3：john 直接跑（john 会根据 `$6$` 自动选格式）**

```bash
echo 'webapp:$6$rBzL1NJv$J8j9mGqK0a9WvV5N7lT3xO2yQ1cZ4bF6dH8iE0gS2kU4nP6tR9sA1dF3gH5jK7lZ9x' > /tmp/shadow-line.txt
john --show=formats /tmp/shadow-line.txt | head -20
john --wordlist=/usr/share/wordlists/rockyou.txt /tmp/shadow-line.txt
```

**步骤 4：hashcat 等价命令**

```bash
hashcat -m 1800 /tmp/shadow-line.txt /usr/share/wordlists/rockyou.txt
```

**解读**：这个流程演示了「**尽量少依赖识别工具**」的原则——有前缀就查表，没前缀才上工具，最后用两个破解器交叉验证。

### 场景 4：Windows SAM 场景（含固定值的识别）

```bash
cat > /tmp/sam.txt <<'EOF'
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
EOF

hashcat --identify /tmp/sam.txt --username
# 或
hashid -m -f /tmp/sam.txt
```

**解读**：

- 格式是 `用户名:UID:LM:NTLM:::（7 个冒号字段）`。
- `aad3b435b51404eeaad3b435b51404ee` = **空 LM 哈希**（Vista 之后默认禁用 LM，这是固定填充）。
- `31d6cfe0d16ae931b73c59d7e0c089c0` = **空 NTLM 哈希**。
- **这两个值出现在一起 = 该账号当前是空口令**，直接就知道答案，不用跑破解。

```bash
# 若要用 hashcat 跑这类哈希，记得加 --username
hashcat -m 1000 --username /tmp/sam.txt /usr/share/wordlists/rockyou.txt
```

## 6. 输出解读

hash-identifier 的输出只有两个区块：

| 区块 | 含义 | 怎么用 |
| --- | --- | --- |
| `Possible Hashs:` | **长度与字符集完全吻合**的算法 | 从最上面那一两个开始试 |
| `Least Possible Hashs:` | 长度也吻合、但需要额外条件（前缀、盐、变体）的算法 | **这一列表的意义是「提醒你还不能确定」** |

**判断准则**：

```
如果 Possible 列表只有 1 项  → 大概率就是它（但仍需上下文确认）
如果 Possible 列表有 2~3 项  → 全部试一遍，取最先命中的
如果 Possible 列表超过 3 项  → 说明输入特征太少，必须去找上下文
```

**识别结果 → 下一步动作的映射表**：

| 识别结果 | hashcat `-m` | john `--format=` | 建议策略 |
| --- | --- | --- | --- |
| MD5 | 0 | raw-md5 | 字典优先，很快 |
| NTLM | 1000 | nt | 字典优先，很快；先查是否为空哈希 |
| SHA-1 | 100 | raw-sha1 | 字典优先 |
| SHA-256 / SHA-512 | 1400 / 1700 | raw-sha256 / raw-sha512 | 字典 + 规则 |
| md5crypt (`$1$`) | 500 | md5crypt | 字典（慢千倍，别用掩码） |
| sha512crypt (`$6$`) | 1800 | sha512crypt | 小字典，别用大字典 |
| bcrypt (`$2b$`) | 3200 | bcrypt | **小字典 + 精确规则**，大字典不现实 |
| phpass (`$P$`) | 400 | phpass | 字典 + 规则 |
| MySQL native | 300 | mysql | 字典优先 |
| Argon2 | 34000 | — | 大字典基本不可行 |

**最后一步永远是**：用 `hashcat -H -m <号>` 查看该模式的官方说明与**示例哈希**，把你手上的哈希和示例对比一下——格式一致才动手。

## 7. 与其他工具配合

```text
[拿到一段哈希]
        ↓
[有前缀？] ── 是 ──→ 直接查前缀表 ─→ -m 号
        │
        否
        ↓
[hash-identifier / hashid -m / hashcat --identify]  →  候选列表
        ↓
[交叉验证] hashcat -H -m <号>  对比示例哈希格式
        ↓
[破解] john --wordlist 或 hashcat -a 0 / -a 3
        ↓
[无前缀且候选多] 两个候选都跑一遍，取命中者
```

**与其他教程的衔接**：

- **[john](john.md)**：`john --show=formats` 是最可靠的识别方式之一（因为它同时告诉你 john 用什么插件解析）。
- **[hashcat](hashcat.md)**：`--identify` 的输出**直接就是 `-m` 号**，衔接最顺。
- **[responder](../07-嗅探与欺骗/responder.md)**：抓到 NetNTLM 哈希后，第一步就是识别是 v1 还是 v2（`-m 5500` vs `-m 5600`），格式里会明确区分。
- **[airodump-ng](../05-无线攻击/airodump-ng.md) → [aircrack-ng](../05-无线攻击/aircrack-ng.md)**：WPA 握手包不是「哈希」，用 `-m 22000`，不需要本工具识别。
- **[unshadow](wordlists.md) + [john](john.md)**：从 `/etc/shadow` 拿到的哈希**自带前缀**，通常不需要 hash-identifier。

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| `hash-identifier -h` 输出 `Not Found.` | 它没有真正的命令行参数，把 `-h` 当成哈希输入了 | 直接运行 `hash-identifier` 交互输入；脚本化用 `hashid -m` |
| 识别出「MD5」但破解跑不出来 | 实际是 NTLM 或其他同长度算法 | 两个都跑（`-m 0` 与 `-m 1000`） |
| 输入被截断或报 `Not Found.` | 哈希里混入了空格、换行、引号 | 用 `cat -A` 检查；去掉首尾空白 |
| 带盐的哈希识别成错的类型 | 盐是应用自定义拼接的，工具只看长度 | 去读应用源码或数据库结构；用 `--identify` 配合 `-H` 对示例哈希 |
| 批量识别时 `hashid` 只输出第一个 | 未加 `-f` | 用 `hashid -f file.txt` |
| 拿到一堆 32 位 hex 无法区分 | 特征本身不足 | 看来源（Windows → NTLM，其他 → MD5）；**两个都试** |
| 新算法识别不出来（Argon2、yescrypt） | hash-identifier 特征库较老 | 用 `hashcat --identify` 或 `john --show=formats` |
| 以为是哈希但其实是 base64 编码的数据 | 误判 | 试试 `base64 -d`；或看长度是否符合某个哈希的输出长度 |
| 识别对了但 `-m` 号抄错 | 手工抄写错误 | 用 `hashcat --identify` 直接复制输出 |

## 9. 防御视角（蓝队）

哈希识别本身是攻击者**进攻流程中的一小步**，对蓝队而言重点是「不要给对方可识别的东西」——但完全隐藏哈希类型在技术上不可行。所以蓝队的着力点在别处：

| 风险 | 检测 | 缓解 |
| --- | --- | --- |
| 哈希值泄露到外部 | 检测含**定长十六进制串**的响应/日志外泄（DLP 规则：长 ≥ 32 的连续 hex） | 应用**绝不返回**哈希；错误信息里不带 `$1$`/`$6$` 这类前缀 |
| 错误信息泄露用户是否存在 | `$1$abcd$...` 这类**带盐哈希**若被回显，攻击者可直接识别算法 | 登录失败的响应**完全统一**；不返回任何哈希片段 |
| 用户名枚举 | 观察「响应时间差」与「错误文本差异」 | 统一错误文本 + 固定响应时间（dummy hash 计算） |
| 弱哈希算法 | 审计存储层看到的哈希前缀 | 迁移到 `$2b$`（bcrypt）/Argon2/yescrypt；**Windows 侧禁用 LM** |
| 空口令账户 | 检测固定值 `31d6cfe0d16ae931b73c59d7e0c089c0`（NTLM 空哈希）与 `aad3b...`（LM 空哈希）出现在导出中 | 定期审计 AD 中的空口令账户；强制口令策略 |

**一条具体的防御实践：恒定时间与"诱饵哈希"**

```php
// 概念示意：无论用户是否存在，都执行一次哈希比较
$hash = $userExists ? $storedHash : '$2y$10$dummydummydummydummydummydu'; // 固定诱饵
$ok = password_verify($input, $hash);
if (!$ok) { echo '用户名或密码错误'; }   // 统一文本
```

**要点**：蓝队的目标不是「让 hash-identifier 失效」，而是：

> **让攻击者拿不到哈希**（访问控制、最小权限、不泄露） + **拿到也算不动**（bcrypt/Argon2 + 长口令 + MFA）。

## 10. 参考

- 官方仓库：<https://github.com/blackploit/hash-identifier>
- Kali 工具页：<https://www.kali.org/tools/hash-identifier/>
- 本机命令：`hash-identifier`（交互式）
- 更现代替代品：`hashcat --identify`（hashcat 包）、`john --show=formats`（john 包）、`hashid`、`haiti`
- 相关：[hashcat](hashcat.md)、[john](john.md)、[wordlists](wordlists.md)

## ⚠️ 法律与伦理

**识别哈希类型本身不违法**，但它是**破解的前置步骤**。若被识别的哈希来自未经授权的系统，则本教程后续的任何操作都可能构成：

- 《中华人民共和国刑法》第二百八十五条「非法侵入计算机信息系统罪」/「非法获取计算机信息系统数据罪」；
- 《中华人民共和国网络安全法》第二十七条所禁止的危害网络安全活动。

**本教程仅适用于**：你自己系统的口令强度自查、有书面授权的渗透测试、CTF 靶场、教学演示。**拿到不明来源的哈希时，正确的动作是不要碰它。**
