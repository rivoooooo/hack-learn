# yara（恶意样本模式匹配）

> **一句话**：用一门小语言把「恶意样本长什么样」写成规则（文本串、十六进制字节、正则 + 布尔逻辑），然后拿规则去批量扫描磁盘上的文件、目录、进程内存——杀软的「特征引擎」开源版。
> **分类**：漏洞分析 / 恶意样本与文件特征检测 ｜ **Kali 包**：`yara`（命令 `yara`、`yarac`）｜ **官方文档**：<https://www.kali.org/tools/yara/> ｜ 上游：<https://virustotal.github.io/yara/>

---

## 1. 它解决什么问题

当你面对**大量文件**时，问题是「从哪些文件里认出哪一类」：

- 应急响应：拿到可疑主机，需要从 50 万文件里找出「同一家族的样本」；
- 恶意软件研究：已经分析出一个样本，需要**在样本库里找出同源变种**；
- 内存取证：内存镜像里搜「解密后的 C2 配置」；
- 威胁狩猎：把「已知 IoC」变成可复用、可版本管理的规则；
- 供应链检查：扫包里的可疑文件。

**哈希（IoC）不够用**，因为它「一字节变、全盘不中」；YARA 的定位是**结构化、可表达、可维护的特征描述**：

| 需求 | hash IoC | **YARA** |
|------|----------|----------|
| 精确匹配已知样本 | ✅ | ✅ |
| 匹配**变种**（改了部分字节） | ❌ | ✅（通配、正则、多条件） |
| 表达「行为/结构条件」 | ❌ | ✅（PE 节、导入表、熵、文件大小） |
| 可读、可评审、可版本管理 | 差 | ✅（规则即代码） |
| 跨平台批量扫描 | 需自造 | ✅（`-r` 递归 + `-p` 多线程） |

**对比同类**：

| 工具 | 定位 | 差异 |
|------|------|------|
| **YARA** | **文件/内存特征规则引擎** | 扫「文件内容」，规则语言强、生态大（VirusTotal 内置） |
| **Snort** | **网络流量**规则引擎 | 扫的是「数据包」，不是文件；见 [`snort.md`](snort.md) |
| **ClamAV** | 完整杀毒引擎 | 有自己的签名库 + 扫描守护进程；YARA 更灵活、适合自写规则 |
| **`grep`/`strings`** | 文本搜索 | 不能表达「A 且 B 且文件大小在范围内且 PE 有某节」 |
| **binwalk / bulk-extractor** | 结构拆分 / 特征提取 | 用于产出候选文件，再做 YARA 扫描；见 [`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md)、[`../09-数字取证/bulk-extractor.md`](../09-数字取证/bulk-extractor.md) |

**一句话选型**：有「一批文件 + 想批量判定它们是不是某类东西」的需求 → YARA。

---

## 2. 工作原理

YARA 的模型极简：**规则 = 字符串集合 + 布尔条件**。

```
        规则文件 (.yar / .yara)
   ┌──────────────────────────────────────────────┐
   │  rule Ransom_LockBit : ransomware            │  ← 规则名 + 标签
   │  {                                            │
   │      meta:                                    │  ← 元信息（给人看）
   │          author = "blue@example.com"          │
   │          description = "..."                  │
   │                                              │
   │      strings:                                 │  ← 待匹配的原子
   │          $a = "LockBit" nocase ascii wide     │
   │          $b = { 4D 5A 90 00 }                 │
   │          $c = /C:\\Users\\[^\\]+\\AppData/    │
   │                                              │
   │      condition:                               │  ← 布尔表达式
   │          2 of them and filesize < 5MB         │
   │  }                                            │
   └──────────────────────────────────────────────┘
                        │
           ① 编译（yarac 可预编译成 .yarc）
                        ▼
   ┌──────────────────────────────────────────────┐
   │  扫描引擎：                                   │
   │    - 对每个字符串抽出「原子（atom）」（2-4 字节）│
   │    - 用 Aho–Corasick 多模式匹配快速扫过文件    │
   │    - 候选命中 → 在候选位置验证完整字符串       │
   │    - 正则/十六进制通配 → 有 Regexp/字节匹配器  │
   │    - 自左向右过筛：所有 strings 先独立求值，   │
   │      再由 condition 做布尔组合                 │
   └──────────────────┬───────────────────────────┘
                      ▼
              规则名 + 标签 + 匹配到的字符串与偏移
```

**关键概念**：

- **原子（atom）与快筛**：YARA 把每个字符串拆成短原子，建多模式匹配表**一次性扫完整文件**，命中原子后才做完整匹配。所以**字符串越长越具体，扫描越快越准**；全是 2 字节通配的规则会又慢又误报。
- **`condition` 是灵魂**：`2 of them`、`any of ($a*)`、`all of them`、`for any i in (1..#a)` 这些写法让规则可以表达「模糊但仍可控」的条件。
- **字符串修饰符**：
  - `nocase`：大小写无关（**不能与 `xor`/`base64` 连用**）；
  - `wide`：按 UTF-16 匹配（每字符间插 `0x00`）——**Windows 字符串必加**；
  - `ascii`：与 `wide` 同时用时表示「两种编码都试」；
  - `fullword`：要求两侧是非字母数字（避免 `domain` 命中 `mydomain.com`）；
  - `xor`：单字节 XOR 匹配，`xor(0x01-0xff)` 可限定密钥范围（**不能与 `nocase`/`base64` 连用**）；
  - `base64` / `base64wide`：自动生成 3 种 base64 编码形式（**不能与 `nocase`/`xor`/`fullword` 连用**）；
  - `private`：命中了但**不在输出里显示**（常用来做「辅助条件字符串」）。
- **模块（module）**：`import "pe"` 后可以用 `pe.entry_point`、`pe.imphash()`、`pe.sections` 等**结构化属性**——这是 YARA 从「找字节」升级到「看结构」的关键（对加壳/混淆样本尤其有用）。
- **`yarac` 预编译**：把规则编译成二进制 `.yarc`，扫描时用 `-C` 加载 —— **启动更快**（规则多的时候差别明显），也便于分发（不必带规则原文）。
- **扫描目标**：文件/目录（`-r`）、**进程内存**（给 PID）、以及 `--scan-list` 的清单。

---

## 3. 安装与快速上手

```bash
sudo apt install yara
command -v yara yarac
yara --version
```

```console
root@kali:~# yara --version
4.5.8
```

```bash
yara -h
```

```console
root@kali:~# yara -h
YARA 4.5.8, the pattern matching swiss army knife.
Usage: yara [OPTION]... [NAMESPACE:]RULES_FILE... FILE | DIR | PID

Mandatory arguments to long options are mandatory for short options too.

       --atom-quality-table=FILE           path to a file with the atom quality table
  -C,  --compiled-rules                    load compiled rules
  -c,  --count                             print only number of matches
  -E,  --strict-escape                     warn on unknown escape sequences
  -d,  --define=VAR=VALUE                  define external variable
  -q,  --disable-console-logs              disable printing console log messages
       --fail-on-warnings                  fail on warnings
  -f,  --fast-scan                         fast matching mode
  -h,  --help                              show this help and exit
  -i,  --identifier=IDENTIFIER             print only rules named IDENTIFIER
       --max-process-memory-chunk=NUMBER   set maximum chunk size while reading process memory (default=1073741824)
  -l,  --max-rules=NUMBER                  abort scanning after matching a NUMBER of rules
       --max-strings-per-rule=NUMBER       set maximum number of strings per rule (default=10000)
  -x,  --module-data=MODULE=FILE           pass FILE's content as extra data to MODULE
  -n,  --negate                            print only not satisfied rules (negate)
  -N,  --no-follow-symlinks                do not follow symlinks when scanning
  -w,  --no-warnings                       disable warnings
  -m,  --print-meta                        print metadata
  -D,  --print-module-data                 print module data
  -M,  --module-names                      show module names
  -e,  --print-namespace                   print rules' namespace
  -S,  --print-stats                       print rules' statistics
  -s,  --print-strings                     print matching strings
  -L,  --print-string-length               print length of matched strings
  -X,  --print-xor-key                     print xor key and plaintext of matched strings
  -g,  --print-tags                        print tags
  -r,  --recursive                         recursively search directories
       --scan-list                         scan files listed in FILE, one per line
  -z,  --skip-larger=NUMBER                skip files larger than the given size when scanning a directory
  -k,  --stack-size=SLOTS                  set maximum stack size (default=16384)
  -t,  --tag=TAG                           print only rules tagged as TAG
  -p,  --threads=NUMBER                    use the specified NUMBER of threads to scan a directory
  -a,  --timeout=SECONDS                   abort scanning after the given number of SECONDS
  -v,  --version                           show version information

Send bug reports and suggestions to: vmalvarez@virustotal.com.
```

**最小可用**（先用无害的 EICAR 测试串验证整条链路）：

```bash
# EICAR 测试文件：业界通用的「无害反病毒测试串」
printf 'X5O!P%%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*' > /tmp/eicar.txt

# 写一条规则
cat > /tmp/eicar.yar <<'EOF'
rule EICAR_Test_File
{
    meta:
        author = "tutorial"
        description = "Matches the EICAR anti-malware test file"
    strings:
        $eicar = "EICAR-STANDARD-ANTIVIRUS-TEST-FILE" nocase
    condition:
        $eicar
}
EOF

yara /tmp/eicar.yar /tmp/eicar.txt
```

```console
root@kali:~# yara /tmp/eicar.yar /tmp/eicar.txt
EICAR_Test_File /tmp/eicar.txt
```

**用 `yarac` 预编译**：

```bash
yarac /tmp/eicar.yar /tmp/eicar.yarc
yara -C /tmp/eicar.yarc /tmp/eicar.txt
```

---

## 4. 核心参数详解

> 全部取自上面的 `yara -h` 原文。

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-r, --recursive` | **递归扫描目录** | 应急响应主力：`yara -r rules.yar /` |
| `-p, --threads=N` | 扫描目录时用 N 个线程 | 大目录必加（如 `-p $(nproc)`） |
| `-s, --print-strings` | **打印命中的字符串与其偏移** | 写规则/验证规则必用；报告里能给出证据 |
| `-L, --print-string-length` | 打印命中字符串长度 | 配合 `-s` 判断是否截断/变形 |
| `-m, --print-meta` | 打印规则的 `meta` 字段 | 让输出带上作者/描述，报告可直接引用 |
| `-g, --print-tags` | 打印规则标签 | 按家族/类型分类 |
| `-e, --print-namespace` | 打印规则命名空间 | 多规则库共存时区分来源 |
| `-t, --tag=TAG` | **只运行带某标签的规则** | 规则库很杂时按标签筛选 |
| `-i, --identifier=NAME` | **只运行名为 NAME 的规则** | 调试单条规则 |
| `-n, --negate` | **只打印「不匹配」的规则** | 反向验证规则是否真的会漏 |
| `-c, --count` | 只输出匹配数量 | 统计批量扫描的整体命中率 |
| `-C, --compiled-rules` | 加载预编译规则（`.yarc`） | 规则多时提速、便于分发 |
| `-w, --no-warnings` | 关闭警告 | 规则库有历史遗留警告时 |
| `--fail-on-warnings` | **有警告就失败** | **CI 里必加**：规则写错会拦住合并 |
| `-d, --define=VAR=VALUE` | 定义**外部变量** | 规则里用 `external` 变量做参数化 |
| `-x, --module-data=MODULE=FILE` | 给某模块传外部数据 | 如给 `cuckoo` 模块喂 JSON |
| `-f, --fast-scan` | 快速扫描模式 | 只关心「中没中」不关心细节时 |
| `-l, --max-rules=N` | 命中 N 条规则后中止 | 批量筛查时避免单文件刷屏 |
| `-z, --skip-larger=N` | 跳过大于 N 字节的文件 | **跳过超大文件/镜像**，防扫描卡死 |
| `-a, --timeout=SEC` | 超时中止 | 防止某文件触发灾难性回溯正则 |
| `-k, --stack-size=N` | 最大栈槽数（默认 16384） | 极复杂规则报「stack overflow」时调大 |
| `-N, --no-follow-symlinks` | 不跟随符号链接 | **扫根目录时防止符号链接环路** |
| `-D, --print-module-data` | 打印模块数据 | 调试 `pe`/`elf` 模块 |
| `-M, --module-names` | 显示可用模块 | 看本机 YARA 支持哪些模块 |
| `-E, --strict-escape` | 对未知转义序列告警 | 规则里正则转义写错时能发现 |
| `-X, --print-xor-key` | 打印 XOR 密钥与明文 | 分析被 XOR 混淆的样本时**极有用** |
| `-S, --print-stats` | 打印规则统计（性能） | 优化慢规则 |
| `--scan-list` | 从文件读「待扫描文件清单」（每行一个） | 与 `find` 配合做精确清单扫描 |
| `--atom-quality-table=FILE` | 自定义原子质量表 | 高级性能调优 |

**`yarac`（编译器）**：

```console
root@kali:~# yarac -h
Usage: yarac [OPTION]... [NAMESPACE:]SOURCE_FILE... OUTPUT_FILE

       --atom-quality-table=FILE        path to a file with the atom quality table
  -d,  --define=VAR=VALUE               define external variable
       --fail-on-warnings               fail on warnings
  -h,  --help                           show this help and exit
  -E,  --strict-escape                  warn on unknown escape sequences
       --max-strings-per-rule=NUMBER    set maximum number of strings per rule (default=10000)
  -w,  --no-warnings                    disable warnings
  -v,  --version                        show version information
```

---

## 5. 实战演练

> **环境声明**：全部使用**无害的测试样本与自有文件**：
> - **EICAR 测试文件**：业界标准的无害反病毒测试串，可安全创建/传播（大多数 AV 会把它当病毒告警，这是预期行为）；
> - **自建样本**：自己写的脚本、自己编译的二进制、公开的恶意样本分析**教学数据集**（如 theZoo、MalwareBazaar 的**分析用样本**——**必须在隔离虚拟机中处理**）；
> - **扫描自己的文件**：自己的下载目录、自己的取证镜像。
> **禁止**：扫描他人设备/服务器；传播真实恶意样本。

### 场景 1：EICAR 端到端验证 + 递归扫描 + 性能参数

```bash
# ① 造一个「扫描靶场目录」：一个 EICAR、一个正常文件、一个深层嵌套
mkdir -p /tmp/yaralab/deep/nested
printf 'X5O!P%%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*' > /tmp/yaralab/deep/nested/eicar.txt
echo "this is a completely benign file" > /tmp/yaralab/benign.txt
find /tmp/yaralab -type f
```

```console
root@kali:~# find /tmp/yaralab -type f
/tmp/yaralab/deep/nested/eicar.txt
/tmp/yaralab/benign.txt
```

```bash
# ② 多线程递归扫描，打印命中字符串与偏移
yara -r -p "$(nproc)" -s -m -g /tmp/eicar.yar /tmp/yaralab
```

```console
EICAR_Test_File /tmp/yaralab/deep/nested/eicar.txt
0x0:$eicar: EICAR-STANDARD-ANTIVIRUS-TEST-FILE
author: tutorial
description: Matches the EICAR anti-malware test file
```

**解读（输出结构）**：

```
<规则名> <文件路径>
0x<十六进制偏移>:$<字符串标识符>: <命中的实际内容>
<meta 键>: <meta 值>          ← 因为加了 -m
```

- `-r` 让 YARA 进到 `deep/nested/` 这个深层目录（**不加 `-r` 只扫顶层文件**，这是最常见的「为什么没扫到」）；
- `-s` 给出**偏移 + 命中的原文字节**——这是报告里的「证据」，比单说「命中了」强得多；
- `benign.txt` 没有输出，说明规则没有误报。

```bash
# ③ 大目录扫描：跳过超大文件、限制超时、防符号链接环路
yara -r -p 8 -z 50M -a 60 -N -s /tmp/eicar.yar /tmp/yaralab
```

```bash
# ④ 只关心「中没中」时用 -c（只输出数量）
yara -r -c /tmp/eicar.yar /tmp/yaralab
```

```console
root@kali:~# yara -r -c /tmp/eicar.yar /tmp/yaralab
1
```

```bash
# ⑤ 反向验证（-n）：如果规则太宽，这里会看到大量「不该匹配却匹配了」的文件
yara -r -n /tmp/eicar.yar /tmp/yaralab
```

### 场景 2：写「像样」的规则——多条件、编码修饰符、PE 模块

**2a. 多字符串 + 布尔条件（模拟「家族特征组合」）**

```bash
cat > /tmp/family.yar <<'EOF'
rule Suspicious_Family_A : demo malware
{
    meta:
        author      = "tutorial"
        description = "三组特征中命中两组 + 大小限制"
        reference   = "internal-demo-only"
        tlp         = "clear"

    strings:
        // 1) 明显的指示串（Windows 上常见 UTF-16）
        $s1 = "This program cannot be run in DOS mode" ascii wide

        // 2) 十六进制字节（PE 头的一部分）
        $s2 = { 4D 5A }

        // 3) 正则：Windows 路径
        $s3 = /[A-Za-z]:\\Users\\[^\\]{1,32}\\AppData/ nocase

        // 4) 一个「辅助条件」字符串，命中也不显示
        $helper = "kernel32.dll" nocase private

    condition:
        filesize < 10MB and
        $s2 at 0 and                 // 必须是 PE 文件（MZ 在偏移 0）
        ( 2 of ($s1, $s3) or $helper )
}
EOF

# 先用无害文件验证语法是否正确、是否能跑通
yara -s -m /tmp/family.yar /tmp/eicar.txt
yara -s -m /tmp/family.yar /tmp/yaralab/benign.txt
```

**解读（这条规则用到的语法点）**：

| 语法 | 含义 | 为什么有用 |
|------|------|------------|
| `ascii wide` | ASCII 和 UTF-16 两种编码都试 | Windows 二进制里的字符串是 UTF-16 |
| `{ 4D 5A }` | 十六进制字节序列 | 匹配不可打印的二进制特征 |
| `/[A-Za-z]:\\Users\\.../ nocase` | 正则 + 大小写无关 | 表达「一个家族的模式」而不是一个固定串 |
| `private` | 命中但**不显示** | 只作为辅助判据，避免污染输出 |
| `$s2 at 0` | **要求匹配位置在偏移 0** | 判断「这是不是一个 PE 文件」 |
| `filesize < 10MB` | 文件大小条件 | 排除「大文件里偶然出现这些串」的误报 |
| `2 of ($s1, $s3)` | 集合条件：命中其中 2 个 | **模糊但有界**——变种容错 |

```bash
# 拿一个真实的 PE 二进制来试（用系统里的一个无害 exe 样本，或自己造的）
yara -s -m /tmp/family.yar /usr/share/metasploit-framework/data/templates/*.exe 2>/dev/null | head
```

**2b. 用 `pe` 模块做结构化判断**（对加壳/混淆样本很有用）

```bash
cat > /tmp/pe_demo.yar <<'EOF'
import "pe"
import "hash"

rule PE_High_Entropy_Small_Section_No_Imports : demo packed
{
    meta:
        description = "可疑加壳迹象：小文件 + 高熵节 + 极少的导入"
    condition:
        pe.is_pe and
        filesize < 2MB and
        pe.number_of_sections <= 3 and
        pe.number_of_imported_functions < 10 and
        for any section in pe.sections : ( section.raw_data_size > 0 and
                                           math.entropy(section.offset, section.raw_data_size) > 7.2 )
}
EOF

yara -s -m -D /tmp/pe_demo.yar /path/to/a/pe/file.exe
```

**解读**：这条规则**完全不看具体字符串**，只看**结构 + 熵**：

| 条件 | 含义 | 加壳样本的典型表现 |
|------|------|--------------------|
| `pe.is_pe` | 是 PE 文件 | 前置条件 |
| `pe.number_of_sections <= 3` | 节很少 | 加壳后常被合并 |
| `pe.number_of_imported_functions < 10` | 导入函数极少 | 加壳 stub 只导入 `LoadLibrary`/`GetProcAddress` |
| `math.entropy(...) > 7.2` | **某节熵很高** | 压缩/加密的载荷 |

**这就是 YARA 区别于「字符串搜索」的地方**：它可以表达**结构性的可疑特征**，对「字符串被加密」的样本依然有效。

> 变量名以本机模块为准：`yara -D` 会打印模块数据；不确定的字段先 `yara -M` 看模块列表，再查 <https://yara.readthedocs.io/en/stable/modules/pe.html>。

**2c. `xor` 与 `-X`：处理被 XOR 混淆的样本**

```bash
cat > /tmp/xor.yar <<'EOF'
rule Demo_XOR_String
{
    strings:
        $a = "This program cannot" xor(0x01-0xff) wide ascii
    condition:
        $a
}
EOF

# -X 会打印出「用的什么 XOR 密钥 + 解出的明文」
yara -s -X -L /tmp/xor.yar /tmp/suspicious.bin
```

```console
Demo_XOR_String /tmp/suspicious.bin
0x12c:$a:xor(0x5a) = 54 68 69 73 ...
```

**解读**：`-X` 直接告诉你**密钥和解密结果**——这在样本分析里等于「顺手做了一次单字节 XOR 解密」，比手工爆破快得多。

### 场景 3：与取证流程配合——批量清单、进程内存、CI 校验

**3a. 用 `--scan-list` 只扫「清单里的文件」（精确控制范围）**

```bash
# 从取证镜像里挑出所有可执行文件，再交给 yara
find /mnt/evidence -type f \( -name '*.exe' -o -name '*.dll' -o -name '*.ps1' -o -name '*.sh' \) > /tmp/targets.txt
wc -l /tmp/targets.txt
yara --scan-list -p 8 -s -m /tmp/family.yar /tmp/targets.txt > /tmp/yara_hits.txt
cat /tmp/yara_hits.txt
```

**解读**：`--scan-list` 是「**先筛后扫**」的关键——先用 `find` 把范围收到「真正需要判定的文件」，再让 YARA 扫。对 TB 级镜像，这比无脑 `-r /` 快几个数量级。

**3b. 扫进程内存（应急响应中找「已解密的内存马/C2 配置」）**

```bash
# 先找到可疑进程（示例：你自己的测试进程）
pgrep -a python3
# 对该 PID 的内存做 YARA 扫描（需要 root 权限）
sudo yara -s -m /tmp/family.yar $(pgrep -f 'my_test_process')
```

```console
Demo_XOR_String 12345
0x7f2c40001020:$a: ...
```

**解读**：YARA 支持**直接以 PID 为扫描目标**，扫的是该进程的内存映射。**这是内存马检测的核心手段**——文件已经删了，内存里还在。参数 `--max-process-memory-chunk` 用来控制每次读多少内存（默认 1 GiB）。

**3c. 把规则库当代码管：编译 + 严格校验（CI 友好）**

```bash
# ① 严格校验：有警告就失败
yara --fail-on-warnings -w- /tmp/eicar.yar /tmp/yaralab/benign.txt 2>&1 | head
# 或统一放 set -e 脚本里
if ! yarac --fail-on-warnings /tmp/eicar.yar /tmp/out.yarc; then
  echo "规则有警告，拒绝发布" >&2; exit 1
fi

# ② 预编译并分发（扫描端不再需要规则原文）
yarac /tmp/eicar.yar /tmp/rules.yarc
ls -l /tmp/rules.yarc
sudo cp /tmp/rules.yarc /opt/yara-rules/current.yarc

# ③ 线上只用预编译规则扫描（启动更快）
yara -C -r -p "$(nproc)" -s -m -g /opt/yara-rules/current.yarc /tmp/yaralab
```

```bash
# ④ 用 -S 看规则性能，找出「又慢又没用」的规则
yara -r -S /tmp/eicar.yar /tmp/yaralab
```

```console
rule                 strings  1.00M     2.00M     4.00M
EICAR_Test_File            1    0.2       0.2       0.2  ...
```

**解读**：`-S` 给出「每条规则扫描 X MB 数据花了多少秒」——**性能治理的入口**。规则库里通常有 5% 的规则吃掉 90% 的扫描时间，把它们优化（加长原子/删掉纯通配）收益最大。

**3d. 从 `-r` 递归到真实目录时的实用组合**（救援盘/U 盘扫描）

```bash
# 扫一个 U 盘（只读挂载！扫描不应写盘）
sudo mkdir -p /mnt/usb
sudo mount -o ro /dev/sdX1 /mnt/usb
sudo yara -r -p 4 -z 100M -a 30 -N -s -m -g /opt/yara-rules/current.yarc /mnt/usb > /tmp/usb_scan.txt
wc -l /tmp/usb_scan.txt
sudo umount /mnt/usb
```

---

## 6. 输出解读

### 6.1 默认输出

```
<规则名> <被扫文件路径>
```

加 `-s` 后，每个命中的字符串单独一行：

```
0x<偏移>:$<字符串标识符>: <命中的原始字节/文本>
```

| 字段 | 含义 | 用途 |
|------|------|------|
| `规则名` | 哪条规则命中 | 判定「是什么」 |
| `文件路径` | 哪个文件命中 | 定位证据 |
| `0x偏移` | 命中位置 | **报告里给出「证据在文件何处」** |
| `$identifier` | 哪个字符串命中 | 对应规则的可读性设计 |
| 命中内容 | **实际匹配到的字节** | 最强证据；也是发现「变种」的线索 |

### 6.2 加了 `-m` / `-g` 之后的元数据行

```
author: blue@example.com
description: 三组特征中命中两组 + 大小限制
tlp: clear
```

| 给规则加的 meta | 为什么值得写 |
|------------------|--------------|
| `author` | 出事能找到人 |
| `description` | 半年后自己还看得懂 |
| `reference` | 关联 CVE / 情报报告 |
| `tlp` / `date` / `hash` | 分层共享与版本管理 |

### 6.3 怎么判断结果

| 观察 | 结论 | 下一步 |
|------|------|--------|
| 期望的文件**没有**命中 | 规则/修饰符/扫描范围问题 | 用 `-s -L` 看实际字节；确认 `wide`/`nocase`/`-r` 是否该加 |
| 大量**非预期文件**命中 | 规则太宽 | 加 `fullword`、加长字符串、加 `filesize`、加 `flow` 式结构条件 |
| 命中了但 `-s` 没显示字符串 | 命中的是 `private` 字符串；或条件是纯结构（无 strings） | 正常现象；用 `-D` 看模块数据 |
| 扫得很慢 | 有「短原子 + 大量通配」的规则 | `-S` 找出来优化；或 `-z` 跳过大文件 |
| 规则报 `stack overflow` | 递归/正则太复杂 | 调大 `-k`，或简化条件 |
| 报了 warning | 建议：**别忽略** | `-E` 查未知转义；CI 里加 `--fail-on-warnings` |

---

## 7. 与其他工具配合

```
   ┌─────────────── 取证/响应链 ───────────────┐
   镜像 → 挂载只读 → 找候选文件 → YARA 扫描 → 命中清单
   (dcfldd/autopsy)  (find/sleuthkit)  (yara)      │
                                                    ▼
                                          隔离样本 → 分析（radare2/ghidra）
                                                    │
                                                    ▼
                                          提取新特征 → 更新 YARA 规则
                                                    │
   ┌─────────────── 情报/狩猎链 ───────────────────┐
   Threat Intel IoC ──► YARA 规则 ──► 全网/全盘扫描
                            │
                            └─► 命中样本 → VirusTotal 查同源 → 回溯入口点
```

- **样本获取/结构拆分**：[`../09-数字取证/binwalk.md`](../09-数字取证/binwalk.md)（拆固件/嵌套）、[`../09-数字取证/foremost.md`](../09-数字取证/foremost.md)（文件雕刻）
- **特征提取（产出候选）**：[`../09-数字取证/bulk-extractor.md`](../09-数字取证/bulk-extractor.md)（邮箱/URL/凭据）
- **文件系统级分析**：[`../09-数字取证/sleuthkit.md`](../09-数字取证/sleuthkit.md)、[`../09-数字取证/autopsy.md`](../09-数字取证/autopsy.md)
- **镜像与证据固定**：[`../09-数字取证/dcfldd.md`](../09-数字取证/dcfldd.md)（**先做哈希固定，再扫描**）
- **元数据/隐藏数据**：[`../09-数字取证/exiftool.md`](../09-数字取证/exiftool.md)、[`steghide.md`](../09-数字取证/steghide.md) ← 隐写分析
- **网络侧配对**：[`snort.md`](snort.md) —— Snort 管流量特征、YARA 管文件特征
- **深度分析**：[`../10-逆向工程/ghidra.md`](../10-逆向工程/ghidra.md)、[`../10-逆向工程/radare2.md`](../10-逆向工程/radare2.md) —— 命中后判「到底干什么」

**推荐工作流**：

```
① dcfldd 做镜像 + 记录哈希（证据固定）
② 只读挂载 / autopsy 浏览文件系统
③ find 筛出「值得扫的文件」清单
④ yara -r -s -m 扫描 → 命中清单 + 命中偏移（证据）
⑤ 隔离样本 → 逆向确定行为
⑥ 把新发现写成新规则 → 回归测试（--fail-on-warnings）→ 发布 .yarc
⑦ 全网/全盘复扫，评估影响面
```

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 目录里明明有命中文件却没扫到 | **没加 `-r`**（默认不递归） | 加 `-r` |
| 本该命中的字符串没命中 | 编码不对（UTF-16 却没 `wide`）、大小写不同却没 `nocase` | 加 `wide` / `ascii` / `nocase`；用 `-s` 看实际字节 |
| 误报太多 | 字符串太短/太常见；缺结构条件 | 加长字符串、加 `fullword`、加 `filesize`/`pe.is_pe` 等结构条件 |
| `error: rule ... syntax error` | 语法错（缺分号、正则未闭合、标识符用保留字） | 报错行号会给；保留字如 `all`/`any`/`and` 不能当规则名 |
| `warning: string ... may slow down scanning` | 规则里有「低质量原子」（纯通配/超短串） | 优化字符串；或明知故犯用 `-w`；**CI 里用 `--fail-on-warnings` 拦住** |
| `nocase` 与 `xor` 一起用报错 | **修饰符互斥**（`nocase` 不能与 `xor`/`base64` 连用） | 拆成两条字符串分别写 |
| `fullword` + `base64` 报错 | 同上，互斥 | 去掉其一 |
| 扫描超慢 / 卡死 | 大文件 + 复杂正则；递归进入 `/proc`、`/sys`、网络挂载 | `-z` 跳过大文件、`-a` 设超时、`-N` 不跟随符号链接；**别对整个 `/` 无脑扫** |
| `stack overflow` | 复杂正则/递归条件 | 调大 `-k`；或改用 `byte_test` 等更高效写法 |
| 扫进程内存报权限错 | 需要 root / ptrace 权限 | `sudo` 运行；容器里可能被 seccomp 限制 |
| `.yarc` 加载失败 | 预编译规则版本与扫描端 YARA 版本不匹配 | 用同版本 `yarac` 重新编译 |
| `import "pe"` 报模块不存在 | YARA 编译时未启用该模块 | 用 `-M` 看本机支持的模块；Debian/Kali 包通常已带常用模块 |
| `-X` 没输出密钥 | 命中的字符串不是 `xor` 修饰的 | `-X` 只对 `xor` 字符串有意义 |
| 多规则文件加载顺序问题 | 跨文件引用规则需**先定义后引用** | 被引用的规则放在前面文件里 |
| 外部变量未定义报错 | 规则用了 `external` 变量但没给值 | 扫描时加 `-d VAR=VALUE` |

---

## 9. 防御视角（蓝队）

YARA 是**蓝队的核心工具之一**——它把「威胁情报」变成「可执行、可回归、可版本管理的检测资产」。

| 场景 | 做法 | 价值 |
|------|------|------|
| 变种检测 | 用「多特征 + 2 of them」而非单一 hash | 抗轻微变形，命中率远高于 hash 黑名单 |
| 内存马/无文件攻击 | 扫进程内存（PID 目标） | 文件已删、内存仍在的载荷唯一可检 |
| 勒索软件前置 | 对共享目录做「写入即扫」 | 早期发现加密器落地 |
| 供应链检查 | 扫构建产物/依赖包 | 发现被投毒的包 |
| 威胁狩猎 | 把情报报告里的 IoC 翻译成 YARA | 从「被动等告警」变「主动找」 |
| 规则质量治理 | `--fail-on-warnings` + `-S` 性能剖析 + 代码评审 | 规则库不腐化 |
| 事件复盘 | 全盘扫描历史镜像 | 确定影响面与时间线 |

**蓝队的五条硬建议**：

1. **YARA 规则要进版本控制**，附 `meta`（作者/日期/参考），走代码评审；
2. **不要只写 hash 规则**——hash 规则在样本变形后 100% 失效，价值几乎为零；
3. **性能要治理**：用 `-S` 定期体检，把「慢规则」优化或降级为「按需跑」；
4. **发布走 `.yarc` 预编译**：保证扫描端与规则端一致，启动快；
5. **测试集回归**：维护一个「已知恶意 + 已知良性」的测试集，每次改规则都跑一遍，防误报爆炸。

**规则样例的写法取向（真实蓝队风格）**：

```yara
rule Ransom_Generic_Note_And_Ext : ransomware
{
    meta:
        author      = "blue-team"
        date        = "2026-09-15"
        description = "勒索信文件名 + 大量加密扩展名引用"
        reference   = "internal-IR-2026-0142"
        tlp         = "amber"

    strings:
        $note1 = "Your files have been encrypted" nocase wide ascii
        $note2 = "recover your files" nocase wide ascii
        $note3 = "bitcoin" nocase wide ascii

    condition:
        uint16(0) == 0x5A4D and      // 是 PE（MZ）
        filesize < 8MB and
        2 of ($note1, $note2, $note3)  // 容错：命中任意两个
}
```

**注意**：`tlp` 这类共享标记要在实际情报共享流程里一致使用；规则内容可能包含**攻击者尚未知晓的检测方法**，外发前应评估披露风险。

---

## 10. 参考

- Kali 工具页（含 `yara -h` 与 `yarac -h` 原文）：<https://www.kali.org/tools/yara/>
- YARA 官方文档：<https://yara.readthedocs.io/en/stable/>
- 规则编写指南：<https://yara.readthedocs.io/en/stable/writingrules.html>
- PE 模块参考：<https://yara.readthedocs.io/en/stable/modules/pe.html>
- 上游仓库：<https://github.com/VirusTotal/yara>
- 本地命令：`yara -h`、`yarac -h`、`yara -M`（模块列表）、`yara -D`（模块数据）
- 配套教程：[`snort.md`](snort.md)、[`../09-数字取证/bulk-extractor.md`](../09-数字取证/bulk-extractor.md)、[`../09-数字取证/foremost.md`](../09-数字取证/foremost.md)

## ⚠️ 法律与伦理

YARA 本身是**防御工具**，但围绕它有明确的法律边界：

- **真实恶意样本属于高危物品**：获取、存储、传播恶意样本可能违反《网络安全法》《刑法》第 285/286 条（提供侵入/非法控制计算机程序、工具）；**教学与研究中只使用 EICAR 等无害样本，或来源合法、隔离存放的分析样本**；
- **扫描目标必须合法**：对**他人设备、服务器、云环境**做 YARA 扫描（尤其是扫内存）属于未授权访问，可能触犯《刑法》第 285 条；
- **证据完整性**：取证扫描前**必须先做镜像与哈希固定**（见 [`../09-数字取证/dcfldd.md`](../09-数字取证/dcfldd.md)），并在**只读挂载**下扫描，避免破坏证据；
- **规则内容可能敏感**：包含未公开检测逻辑的规则外发可能削弱己方防御，也涉及**情报密级/共享协议（TLP）**；
- **个人信息**：扫描用户终端可能接触到个人文件，需在合规框架内并最小化处理。

**必须遵守**：

1. **只用无害测试样本（EICAR）或合法获得的样本**做规则开发与演练；
2. **只在自有/授权环境**扫描；真实恶意样本**必须在隔离虚拟机/专用分析机**中处理，禁止联网；
3. **扫描前固定证据**（镜像 + 哈希），扫描时挂载只读；
4. **不传播样本、不公开未脱敏的命中文档内容**；
5. 发现的攻击证据应交由**正式应急/法务流程**处理，不擅自处置或对外披露。
