# John the Ripper（离线哈希破解器）

> **一句话**：把各种来源的哈希/加密文件转换成统一格式后，在本地高速枚举出明文口令。
> **分类**：口令攻击 ｜ **Kali 包**：`john`（+ `john-data`）｜ **官方文档**：<https://github.com/openwall/john>

## 1. 它解决什么问题

[hydra](hydra.md) 走网络猜密码，john 走**离线破解**：你手上已经有一份哈希，要把它还原成明文。

john 的两个核心能力：

1. **格式转换**：自带上百个 `*2john` 转换器，把 ZIP、PDF、Office 文档、SSH 私钥、KeePass 数据库、Windows 注册表 SAM、Wi-Fi 握手包、各类钱包……统统转成一行「用户名:哈希」文本。
2. **高速破解**：内置多种攻击模式（单条规则、字典+规则、掩码、增量、PRINCE、Markov），并对哈希格式做了高度优化。

与 [hashcat](hashcat.md) 的取舍：

| | john（jumbo） | hashcat |
| --- | --- | --- |
| 强项 | **格式转换器极多**、CPU 优化好、纯 CPU 环境够用 | **GPU 加速最强**、分布式、规则语言与内核极丰富 |
| 弱项 | 大规模 GPU 场景不如 hashcat | 拿到奇怪的文件格式时要自己找转换工具 |
| 典型分工 | 用来**提取哈希**并做首次试探 | 提取后丢给 hashcat 用 GPU 跑大字典 |

实务上的标准链路：`*2john` 提取 → `john --wordlist` 试小字典 → 没出 → 交给 `hashcat` 用 GPU。

## 2. 工作原理

### 2.1 离线破解为什么比在线快几个数量级

在线爆破受 RTT 和服务端限流约束，每秒最多几十上百次。离线破解只需要 CPU/GPU 算力，没有网络往返，没有锁定策略。

### 2.2 哈希格式决定速度上限

哈希算法的设计目标不同，直接决定破解速度：

| 算法 | 特点 | 相对速度（同硬件） |
| --- | --- | --- |
| MD5 / NTLM | 无盐、设计极快 | 极快（基准） |
| SHA-1 / SHA-256 | 无盐、比 MD5 慢但仍是快速哈希 | 快（SHA-256 明显慢于 MD5） |
| md5crypt (`$1$`) | 有盐、迭代 1000 次 | 慢千倍量级 |
| sha512crypt (`$6$`) | 有盐、迭代约 5000 次 | 更慢 |
| bcrypt (`$2a$`/`$2b$`) | 有盐、**可调 cost** | cost 越高越慢；cost=12 比 MD5 慢多个数量级 |
| scrypt / Argon2 | 内存硬（memory-hard） | 加 GPU 收益大幅下降，因为瓶颈是显存带宽 |

**关键结论**：写报告时不要说「某 GPU 每秒能跑多少亿个 bcrypt」。真正可靠的说法是引用 `john --test` / `hashcat -b` 在**你实际硬件**上跑出来的 benchmark 数字。

### 2.3 攻击模式的原理

| 模式 | 原理 | 适用 |
| --- | --- | --- |
| Single（`--single`） | 用用户名 + GECOS 字段 + 字典词，套用大量变形规则生成候选 | **第一步必跑**。人类设置口令总与自己的账号名相关 |
| Wordlist（`--wordlist`） | 逐行读字典去比对 | 主战场，配 [rockyou](wordlists.md) / [seclists](wordlists.md) |
| Wordlist + Rules（`--rules`） | 对字典每个词套变形规则（大小写、加数字、l33t 替换…） | 用小字典 + 大规则，常常胜过用大字典 |
| Incremental（`--incremental`） | 基于**字符频率统计**（Markov 式）优先生成「像人设的」口令，而非纯字典序 | 无可用字典时 |
| Mask（`--mask`） | 按位置指定字符集，如 `?u?l?l?l?l?d?d` | 已知口令结构（如公司默认口令 `Abcd1234`） |
| PRINCE（`--prince`） | 把单词表里的词两两组合成短语 | 口令是「两个词拼起来」时 |
| Loopback（`--loopback`） | 从已破解的 `.pot` 里取词再变形 | 同一组织内口令风格相似时效果显著 |

### 2.4 Pot 文件与会话

- 破解结果存在 `~/.john/john.pot`（pot，即 "pot file"）。
- `john --show` 把哈希文件与 pot 对照，输出已破解的明文。
- `john --restore` 恢复被中断的会话；`--session=NAME` 命名会话。

## 3. 安装与快速上手

```bash
sudo apt install john
john --help | head -40        # 选项极多，建议直接看 man
john --list=formats | head -20
john --list=build-info
```

最短的工作流：

```bash
# 1) 把 /etc/shadow 与 /etc/passwd 合并成 john 能读的格式
sudo unshadow /etc/passwd /etc/shadow > ~/hashes.txt

# 2) 先跑单条规则模式（几秒到几分钟）
john --single ~/hashes.txt

# 3) 再上字典 + 规则
john --wordlist=/usr/share/wordlists/rockyou.txt --rules ~/hashes.txt

# 4) 查看结果
john --show ~/hashes.txt
```

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `--single[=SECTION]` | 单条规则模式 | **永远第一个跑**，成本低收益高 |
| `--wordlist=FILE` / `--stdin` | 字典模式 | 主战场；`--stdin` 可接 `crunch` 管道 |
| `--pipe` | 类似 `--stdin` 但批量读，**允许配合规则** | 从管道喂字典且要套规则时用它 |
| `--rules[=SECTION]` | 启用词变形规则 | 小字典 + `--rules` 常优于裸大字典 |
| `--rules=:rule[;..]` | 直接内联即时规则 | 临时试一条规则不用改配置文件 |
| `--incremental[=MODE]` | 增量模式 | 无字典时用；`--incremental=All` 空间巨大 |
| `--mask=MASK` | 掩码模式 | 已知结构时最快，如 `--mask='?u?l?l?l?l?d?d'` |
| `--prince=FILE` | PRINCE 模式 | 口令是短语组合时 |
| `--loopback[=FILE]` | 从 pot 取词回炉 | 同一批目标重复破解时效果显著 |
| `--format=NAME` | 强制指定哈希格式 | 自动识别失败时**必须**手动指定，见 `--list=formats` |
| `--show[=left]` | 显示已破解（`=left` 显示未破解） | 汇报用 `--show`；排查遗漏用 `--show=left` |
| `--show=formats` | 以 JSON 打印哈希文件的格式信息 | 不确定格式时先跑这个 |
| `--test[=TIME]` | 基准测试 | **写报告前先跑**，拿到本机真实速度 |
| `--list=WHAT` | 列出能力（formats / build-info / rules …） | 探索工具时的第一站 |
| `--pot=NAME` | 指定 pot 文件 | 多项目隔离，避免结果串味 |
| `--session=NAME` / `--restore[=NAME]` | 会话命名 / 恢复 | 长任务必用 |
| `--status[=NAME]` | 查看运行中会话状态 | 另开终端按 `Ctrl+C` 亦可打印状态 |
| `--fork=N` | 分叉 N 个进程 | 多核 CPU 提速 |
| `--node=MIN-MAX/TOTAL` | 分布式分片 | 多机跑同一份哈希 |
| `--min-length` / `--max-length` | 限制候选长度 | 已知口令长度范围时显著缩小空间 |
| `--max-run-time=N` | N 秒后优雅退出 | 限时任务 |
| `--encoding=NAME` | 输入编码 | 字典含非 UTF-8 字符时（见排错） |
| `--field-separator-char=C` | 改字段分隔符 | 哈希里含 `:` 时 |
| `--keep-guessing` | 找到碰撞后继续找 | 罕见场景 |

### 常用 `*2john` 转换器

位于 `john` 与 `john-data` 两个包。常用的包括：

| 转换器 | 输入 |
| --- | --- |
| `unshadow` | `/etc/passwd` + `/etc/shadow` |
| `zip2john` | 加密 ZIP |
| `rar2john` | 加密 RAR |
| `7z2john` | 加密 7-Zip |
| `office2john` / `pdf2john` | Office 文档 / PDF |
| `ssh2john` | 带口令的 SSH 私钥 |
| `keepass2john` | KeePass `.kdbx` |
| `gpg2john` | GPG 私钥 |
| `bitlocker2john` | BitLocker 镜像 |
| `luks2john` / `truecrypt2john` / `vmx2john` | 各类加密卷 |
| `hccapx2john` / `wpapcap2john` | Wi-Fi WPA 握手包 |
| `keyring2john` / `1password2john` / `lastpass2john` / `bitwarden2john` | 密码管理器库 |
| `kirbi2john` / `ccache2john` | Kerberos 票据 |
| `pfx2john` / `pem2john` / `openssl2john` | 证书与 OpenSSL 加密文件 |

用法统一是「`xxx2john 文件 > hash.txt`，然后 `john hash.txt`」。用 `--list=formats` 查看 john 能识别哪些格式。

## 5. 实战演练

**环境声明**：以下所有操作均在**你自己的机器或你搭建的靶机**上执行。示例使用本机 `/etc/shadow`（你自己的 Kali 虚拟机）和自建靶场文件。**严禁对任何未授权系统的哈希进行操作**——即使是「别人给你的哈希文件」，也可能涉及非授权数据。

### 场景 1：破解本机用户口令（Linux shadow）

**步骤 1：提取哈希**

```bash
sudo unshadow /etc/passwd /etc/shadow > ~/hashes.txt
head -1 ~/hashes.txt
# root:$6$xxxxxxxx$....:0:0:root:/root:/bin/bash
```

`$6$` 表示 **sha512crypt**。这个格式天然很慢，字典要小而精。

**步骤 2：先跑 single**

```bash
john --single ~/hashes.txt
```

**步骤 3：再看格式、跑字典**

```bash
john --show=formats ~/hashes.txt | head -5   # 确认插件识别正确
john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt ~/hashes.txt
```

**步骤 4：查看结果**

```bash
john --show ~/hashes.txt
# root:toor
# 1 password hash cracked, 4 left
```

### 场景 2：破解加密 ZIP

**步骤 1：制作一个属于你自己的测试压缩包**

```bash
echo "hello" > /tmp/secret.txt
zip -e /tmp/test.zip /tmp/secret.txt     # 交互式输入口令，例如 pass1234
```

**步骤 2：提取哈希并破解**

```bash
zip2john /tmp/test.zip > /tmp/zip.hash
john --wordlist=/usr/share/wordlists/rockyou.txt /tmp/zip.hash
john --show /tmp/zip.hash
# /tmp/test.zip/secret.txt:pass1234:secret.txt:test.zip:test.zip
```

输出格式是 `文件名:口令:内部路径:压缩包名`。注意 john 的 `zip2john` 对 **AES 加密的 ZIP** 支持有限，遇到 `WinZip AES` 建议改用 `hashcat -m 13600`。

### 场景 3：SSH 私钥口令 + 掩码模式（进阶）

**步骤 1：提取**

```bash
ssh2john ~/.ssh/id_rsa > /tmp/ssh.hash
cat /tmp/ssh.hash     # id_rsa:$sshng$...
```

**步骤 2：已知口令结构是「常见词 + 4 位数字」，用掩码更划算**

```bash
# 先跑字典
john --wordlist=/usr/share/wordlists/rockyou.txt /tmp/ssh.hash

# 已知结构：ash?d?d?d?d —— 用掩码暴力
john --mask='ash?d?d?d?d' /tmp/ssh.hash

# 让 john 自己探索长度范围
john --incremental --min-length=6 --max-length=8 /tmp/ssh.hash
```

**步骤 3：多核加速与断点续跑**

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt --fork=4 --session=ssh-job /tmp/ssh.hash
# 中断后
john --restore=ssh-job
```

### 场景 4：基准测试（写报告前必做）

```bash
john --test=5 --format=sha512crypt
john --test=5 --format=bcrypt
```

把两条输出里的 `Many salts:` 与 `Only one salt:` 数字记录下来——这才是可以写进报告的、**可复现**的速度数据。

## 6. 输出解读

```
Loaded 5 password hashes with 5 different salts (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Remaining 4 password hashes with 4 different salts
Will run 4 OpenMP threads
Proceeding with single mode...
Press 'q' or Ctrl-C to abort, almost any other key for status
toor             (root)
1g 0:00:00:00 DONE (2026-09-15 10:22) 1.000g/s 12.5p/s 12.5c/s 12.5C/s 0.0/s 0.0/s
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

| 字段 | 含义 |
| --- | --- |
| `Loaded N password hashes with M different salts` | 载入的哈希数与盐数。**盐数越多，逐哈希破解越慢**（GPU 并行度下降） |
| `(sha512crypt, crypt(3) $6$ …)` | 自动识别出的格式。识别错会导致跑不出结果 |
| `1g … DONE` | 破解成功 1 个；`g/s` = guesses/s |
| `12.5p/s` | 每秒处理的口令数（对应 `--test` 里的 `Only one salt` 速度） |
| `toor (root)` | **命中结果：明文 `toor`，属于用户 `root`** |
| `1 password hash cracked, 4 left`（`--show`） | 统计行 |

**判断成功**：`--show` 里出现的 `user:password` 行。

**下一步**：

- 命中率高 → 说明策略有效，加大规则力度或换 PRINCE。
- 完全没出 → 先 `--show=formats` 确认格式识别正确，再考虑换攻击模式。
- 慢得离谱 → 用 `--test` 确认速度，然后换 hashcat + GPU。

## 7. 与其他工具配合

```text
[拿到加密文件/哈希]  ← zip2john / ssh2john / unshadow / bitlocker2john …
        ↓
[格式确认] john --show=formats
        ↓
[快速试探] john --single → --wordlist（小字典） → --mask / --incremental
        ↓
[上 GPU] john --show --format=...  导出 → hashcat -m <对应模式号>
        ↓
[结果回填] john --show / hashcat --show
```

- **{john, hydra}**：hydra 在线拿一个入口，登录后 dump 出哈希 → john 离线扩大战果。
- **{responder, john}**：`responder` 抓到 NetNTLM 哈希 → 转成 hashcat 的 `-m 5600` 格式 → 离线破解（NetNTLMv2 无法直接「解密」，只能猜）。
- **{airodump-ng/aircrack-ng, john}**：抓 WPA 握手包 → `wpapcap2john`/`hccapx2john` → john 或 `hashcat -m 22000`。
- **{crunch, john}**：`crunch 8 8 -t @@@@%%%% | john --pipe --rules`，把规则也套上。

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `No password hashes loaded` | 格式没识别出来 | `john --show=formats 文件`；再不行 `--format=<名>` 手动指定 |
| `Unknown ciphertext format name requested` 后接 `--format` 名 | 格式名拼错 | 用 `john --list=formats` 拿准确名称 |
| 字典读进来是乱码 / `0g` 但字典明明有 | 字典是 `.gz` 压缩包，未解压 | `gunzip /usr/share/wordlists/rockyou.txt.gz` |
| 中文口令破解失败 | 字典编码不是 UTF-8 | `iconv -f GBK -t UTF-8 in.txt > out.txt`，再用 `--encoding` |
| 单核跑得慢 | 未启用多线程 | `--fork=N`（N = 物理核数） |
| 结果「莫名其妙」只有几行 | 结果在 pot 里，未用 `--show` | 一律用 `john --show` 而非看屏幕输出 |
| 忘了上次结果，重复跑 | pot 会跳过已破解项 | 正常行为；换项目时用 `--pot=` 隔离 |
| `zip2john` 报 AES 相关错误 | WinZip AES 不被支持 | 用 `hashcat -m 13600` |
| 内存不足 / 进程被杀 | `--incremental` 或大字典预载 | `--save-memory=1..3`、`--mem-file-size` |
| GPU 没被用上 | john 的 GPU 支持有限 | 改用 hashcat + 已装好的 OpenCL/CUDA 驱动 |
| 破解 sha512crypt/bcrypt 极慢 | 算法本身设计如此 | 缩小字典、加规则而非加长度；或接受「跑不完」的结论并如实汇报 |

## 9. 防御视角（蓝队）

| 风险 | 检测 | 缓解 |
| --- | --- | --- |
| `/etc/shadow` 被读走 | 审计 `open/read` shadow 的行为（auditd 规则 `-w /etc/shadow -p r`）；非 root 进程读取即高优先级告警 | 限制 root 提权路径、部署 SELinux/AppArmor、文件完整性监控（AIDE） |
| SAM/NTDS.dit 被 dump | 检测卷影副本创建、`ntdsutil`/`vssadmin` 异常调用、LSASS 内存读取 | Windows Credential Guard、限制管理员权限、EDR |
| 弱哈希算法 | 审计 `/etc/shadow` 中是否还有 `$1$`（md5crypt）、`$5$` | 迁移到 `$6$`（sha512crypt）或 yescrypt；Windows 侧禁用 LM 哈希 |
| 口令可被字典命中 | 定期用同样的工具对自己做口令强度审计（**须提前授权**） | 强制长度、禁用口令复用、MFA、定期轮换 |
| 备份/文档被拖走 | 检测大量文件外传 | 加密静态数据（LUKS/BitLocker）、最小权限、DLP |

**要点**：john 的可怕之处不在工具本身，而在于「**哈希一旦泄露，防护就只剩算法强度**」。所以蓝队的真正工作是**让哈希拿不到**（访问控制）+ **让哈希拿到也算不动**（慢哈希 + 长度策略）。

## 10. 参考

- 官方仓库：<https://github.com/openwall/john>
- Kali 工具页：<https://www.kali.org/tools/john/>
- 本机手册：`man john`、`john --help`、`john --list=build-info`、`john --list=formats`
- 文档目录（安装后）：`/usr/share/doc/john/`
- 相关：[hashcat](hashcat.md)、[hash-identifier](hash-identifier.md)、[ophcrack](ophcrack.md)、[wordlists](wordlists.md)

## ⚠️ 法律与伦理

对他人的口令哈希进行破解，等同于试图获取他人系统与数据，可能构成《中华人民共和国刑法》第二百八十五条第二款「非法获取计算机信息系统数据罪」，以及《网络安全法》第二十七条所禁止的入侵行为。即便哈希是「别人给你的」，只要该数据不属于你或未获授权，破解行为本身即违法。

**本教程仅适用于**：你自己系统的口令强度自测、有书面授权的渗透测试、CTF 靶场、以及教学演示环境。**切勿**对任何非授权哈希运行本文命令，也不要为规避检测而改动手法。
