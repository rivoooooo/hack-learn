# wfuzz（Web 模糊测试与爆破框架）

> **一句话**：用 `FUZZ` / `FUZ2Z` 关键字把字典或生成的载荷注入到 URL、POST 数据、请求头、Cookie 的任意位置，再用丰富的过滤条件筛出真正的结果。
> **分类**：Web 应用 ｜ **Kali 包**：`wfuzz` ｜ **官方文档**：<https://wfuzz.readthedocs.io/>

## 1. 它解决什么问题

wfuzz 是 Web fuzz 领域的老牌工具（Python），它的设计思想是：

1. **载荷（payload）+ 关键字**：`-z` 定义一组载荷，`FUZZ`、`FUZ2Z`、`FUZ3Z`… 是占位符，wfuzz 会把载荷逐个替换进去。
2. **过滤器表达式**：`--filter` 支持完整的逻辑表达式（`c/l/w/h` 配合 `and/or/=/</>/!=`），比单纯的"排除某状态码"强得多。
3. **插件式**：`-e` 可以列出 encoders / payloads / iterators / printers / scripts，生态完整。

| 工具 | 语言 | 特点 |
|------|------|------|
| **wfuzz** | Python | 载荷类型丰富（file/list/range/hexrand/permutation/…）、过滤器是**表达式**、有插件脚本体系 |
| [ffuf](ffuf.md) | Go | 快，matcher/filter 丰富，交互模式好用 |
| [gobuster](gobuster.md) | Go | 模式化，带预检查 |
| [dirb](dirb.md) | C | 最简单，零配置 |

**wfuzz 的主要优势**：
- **`-z` 的载荷类型非常多**：不只有字典文件，还有 `range`（数字范围）、`list`（内联列表）、`permutation`（排列组合）、`hexrand`（随机十六进制）等——**不需要准备字典文件就能做参数 fuzz**。
- **`--filter` 是表达式**：可以写 `c=200 and h<100` 这样的复合条件。
- **`BBB` 基线机制**：`--hc BBB` 表示"隐藏与基线响应相同的状态码"，wfuzz 会自动先发一个基线请求。

**注意**：wfuzz 2.x → 3.x 的 CLI 有过调整。本教程以 Kali 当前版本（3.x）为准，并保留 2.x 中仍然有效的写法。

## 2. 工作原理

```text
   wfuzz -z file,words.txt -u http://target/FUZZ --hc 404
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ① 解析 -z 载荷定义（type,parameters[,encoder]）             │
   │    file,words.txt            从文件读                      │
   │    list,a-b-c                内联列表（默认用 - 分隔）       │
   │    range,1-10                数字范围                     │
   │    hexrand,0x0-0xff          随机十六进制                  │
   │    permutation,ab             字符排列组合（爆破神器）        │
   │    names,example.com         子域名生成                    │
   │    ipnet,192.168.0.0/24       网段枚举                     │
   │    stdin / burpstate / dirwalk ...                        │
   │    每个 -z 对应一个关键字：第 1 个 FUZZ，第 2 个 FUZ2Z …      │
   │    可用 -m 指定组合迭代器（默认 product）                     │
   └────┬──────────────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ② 组合请求：把载荷代入 URL / -d / -H / -b / -X 里的关键字    │
   │    同一请求里可以同时用 FUZZ 与 FUZ2Z                        │
   └────┬──────────────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ③ 并发发送（-t 并发数，-s 请求间延迟，-p 代理）              │
   └────┬──────────────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ④ 过滤与展示                                                │
   │    --hc/hl/hw/hh  按 状态码/行数/词数/字符数 隐藏            │
   │    --sc/sl/sw/sh  按 状态码/行数/词数/字符数 显示            │
   │    --ss/hs <re>   按响应内容正则 显示/隐藏                   │
   │    --filter <expr> 复合表达式过滤                            │
   │    BBB 特殊值：表示"取基线响应的值"                          │
   │       例：--hc BBB  → 隐藏与基线状态码相同的响应              │
   │    -o <printer> 选择输出格式；-f file,printer 同时落盘        │
   │    --efield/--field 自定义展示字段                            │
   └────────────────────────────────────────────────────────────┘
```

**关键概念**：

- **关键字**：第 1 个 `-z`/`-w` 对应 `FUZZ`，第 2 个对应 `FUZ2Z`，第 3 个对应 `FUZ3Z`……括号形式 `FUZZ{baseline}` 用于基线。
- **基线（BBB）**：wfuzz 会先发一个"基线请求"，把它的 状态码/行数/词数/字符数 记下来。之后用 `BBB` 就能引用这些值——**这是 wfuzz 最优雅的设计**，一条 `--hc BBB` 就能自动过滤掉软 404，不需要手工量长度。
- **`-R` 递归**：指定最大递归深度，对发现的路径继续用同一载荷 fuzz。
- **`-V alltype`**：**不需要写 FUZZ 关键字**，自动对所有参数（GET/POST）做爆破。
- **scripts（插件）**：`--script=<plugins>` 运行插件扫描，`--script-args` 传参。例如 `--script=robots`、`--script=links`。`-A` 是 `--script=default -v -c` 的别名。

## 3. 安装与快速上手

```bash
sudo apt install wfuzz
wfuzz --version
wfuzz -h | head -40
wfuzz -e payloads     # 列出所有载荷类型
wfuzz -e printers     # 列出所有输出格式
wfuzz -e encoders     # 列出所有编码器
wfuzz -e scripts      # 列出所有插件
```

最小可用命令：

```bash
# 1) 目录爆破（-w 是 -z file,<wordlist> 的别名）
wfuzz -w /usr/share/wfuzz/wordlist/general/common.txt http://192.168.56.101/FUZZ

# 2) 参数 fuzz：不带字典，直接枚举数字
wfuzz -z range,1-100 http://192.168.56.101/page.php?id=FUZZ

# 3) 用基线自动过滤软 404
wfuzz -w /usr/share/seclists/Discovery/Web-Content/common.txt \
      --hc BBB http://192.168.56.103:3000/FUZZ
```

## 4. 核心参数详解

### 目标与载荷

| 参数 | 作用 | 建议 |
|------|------|------|
| `-u <url>` | 目标 URL（含关键字） | 也可把 URL 作为位置参数 |
| `-w <wordlist>` | 字典文件（= `-z file,<wordlist>`） | 最常用 |
| `-z <payload>` | 定义载荷：`类型,参数[,编码器]` | **核心参数**，可重复 |
| `--zP <params>` | 给前一个 `-z`/`-w` 提供额外参数 | 高级 |
| `-m <iterator>` | 载荷组合迭代器（默认 `product` 笛卡尔积） | 多载荷时用 |
| `--slice <filter>` | 过滤载荷元素（须紧跟在 `-z` 后） | 精细控制 |
| `-V alltype` | **所有参数爆破**（`allvars` + `allpost`），不需要 FUZZ | 无脑全参数扫 |

**常用载荷类型**（`wfuzz -e payloads` 查看全部）：

| 类型 | 用法示例 | 说明 |
|------|---------|------|
| `file` | `-z file,words.txt` | 从文件读（最常用） |
| `list` | `-z list,admin-test-dev` | 内联列表，默认分隔符是 `-` |
| `range` | `-z range,1-100` | 数字范围 |
| `hexrand` | `-z hexrand,0x0-0xff` | 随机十六进制 |
| `permutation` | `-z permutation,abcdef` | 字符排列组合（**爆破短口令/短名称**） |
| `names` | `-z names,example.com` | 生成子域名 |
| `ipnet` | `-z ipnet,192.168.0.0/24` | 网段枚举 |
| `iprange` | `-z iprange,192.168.0.1-192.168.0.254` | IP 范围 |
| `buffer_overflow` | — | 生成递增长度的字符串 |
| `stdin` | 管道输入 | — |
| `burpstate` | — | 从 Burp state 文件读 |
| `dirwalk` | — | 目录遍历 payload |
| `wfuzzp` | — | 复用之前的 wfuzz 结果 |

**编码器**：`-z file,words.txt,url` 或链式 `md5@sha1`、`md5-sha1`（多编码器生成多个变体）。
`wfuzz -e encoders` 可列出全部（如 `url`、`double url`、`base64`、`md5`、`sha1`、`hexlify`、`uri_hex`…）。

### 请求构造

| 参数 | 作用 | 建议 |
|------|------|------|
| `-X <method>` | HTTP 方法（也可写 `FUZZ` 来爆破方法） | `-X FUZZ` + `-z list,GET-POST-HEAD` |
| `-d <postdata>` | POST 数据（可含关键字） | `-d "user=FUZZ&pass=FUZ2Z"` |
| `-H <headers>` | 请求头，格式 `"Name: value"` 或 `"N1: v1,N2: v2"`；可重复 | `-H "Host: FUZZ"` |
| `-b <cookie>` | Cookie；可重复 | `-b cookie=FUZZ` |
| `--basic` / `--ntlm` / `--digest` | 认证，格式 `user:pass`、`FUZZ:FUZZ`、`domain\FUZ2Z:FUZZ` | 可用关键字爆破凭据 |
| `-p <ip:port[:type]>` | 代理（type 可为 `SOCKS4`/`SOCKS5`/`HTTP`，省略为 HTTP）；可重复 | 多代理轮换 |
| `-t <n>` | 并发连接数（默认 10） | 内网 20~40 |
| `-s <n>` | 请求之间的延迟秒数（默认 0） | **限速** |
| `--req-delay <sec>` | 单次请求最大耗时（默认 90） | — |
| `--conn-delay <sec>` | 连接阶段最大耗时（默认 90） | — |
| `-L, --follow` | 跟随 HTTP 重定向 | — |
| `-Z` | 扫描模式（忽略连接错误） | 大范围扫描 |
| `-R <depth>` | **递归路径发现**，depth 为最大递归层数 | 目录爆破深入 |
| `--ip <addr>` | 指定解析到的主机 | 测试特定后端 |

### 过滤与展示

| 参数 | 作用 | 建议 |
|------|------|------|
| `--hc <codes>` | 隐藏指定状态码（支持 `N,N` 列表；可用 `BBB` 取基线值） | 最常用：`--hc 404` 或 `--hc BBB` |
| `--hl <n>` | 隐藏指定行数 | 软 404 行数恒定时用 |
| `--hw <n>` | 隐藏指定词数 | — |
| `--hh <n>` | 隐藏指定字符数（响应长度） | **对付软 404 的主力** |
| `--sc/--sl/--sw/--sh <v>` | 反向：**只显示**指定 状态码/行数/词数/字符数 | 如 `--sc 200` |
| `--ss <regex>` | 只显示内容匹配正则的响应 | — |
| `--hs <regex>` | 隐藏内容匹配正则的响应 | — |
| `--filter <expr>` | **复合过滤表达式** | 见下方说明 |
| `--prefilter <expr>` | 在 fuzz 之前过滤载荷元素 | 减少无用请求 |
| `--field <f>` / `--efield <f>` | 完全替换 / 追加输出字段 | 见下方说明 |
| `-o <printer>` | 输出打印器（格式） | `-o json`、`-o raw`、`-o html` 等 |
| `-f <file,printer>` | 结果同时写入文件（省略 printer 则用 raw） | 落盘 |
| `-c` | 彩色输出 | 推荐 |
| `-v` | 详细输出 | — |
| `--dry-run` | 只打印将要发出的请求，不实际发送 | **调试利器** |
| `--prev` | 打印上一次的 HTTP 请求 | 复盘 |

**`--filter` 表达式语法**：

```text
字段：c（状态码） l（行数） w（词数） h（字符数）
运算：=  <  >  !=  <=  >=
逻辑：and  or
关键字：FUZZ, FUZ2Z, ...
基线：FUZZ{baseline_value}
```

示例：

```bash
--filter "c=200 and w>100"        # 只保留 200 且词数 > 100
--filter "h<50 or c!=404"         # 字符数 < 50 或 状态码不是 404
--filter "c!=BBB"                 # 不显示与基线状态码相同的响应
--hc BBB                          # 上面这句的简写形式
```

**`--field` / `--efield`**：

```bash
# 追加显示字段（保留默认输出，再加额外字段）
wfuzz -z range --zD 0-5 -u "http://t/page.php?id=FUZZ" --efield r --efield h
#   r = 重定向位置，h = 响应字符数

# 完全替换输出字段
wfuzz -z range --zD 0-5 -u "http://t/page.php?id=FUZZ" --field url
```

### 其他

| 参数 | 作用 | 建议 |
|------|------|------|
| `-e <type>` | 列出可用 encoders/payloads/iterators/printers/scripts | 探索工具能力 |
| `--recipe <file>` | 从文件读选项 | 固化配置 |
| `--dump-recipe <file>` | 把当前选项导出为 recipe | 复用 |
| `--oF <file>` | 保存 fuzz 结果（之后可用 `wfuzzp` 载荷复用） | 结果传递 |
| `--interact` | （beta）捕获按键以交互 | — |
| `--no-cache` | 关闭缓存 | 调试 |
| `--script=<plugins>` | 运行插件扫描（逗号分隔的插件文件或类别） | 如 `--script=robots` |
| `--script-help=<plugins>` | 查看插件帮助 | — |
| `--script-args <n1=v1,...>` | 给插件传参 | 如 `--script-args=links.regex=.*js$` |
| `-A` | = `--script=default -v -c` | 快速启用默认插件集 |
| `-h` / `--help` | 简要 / 高级帮助 | — |
| `--version` | 版本 | — |

## 5. 实战演练

**环境**：本地实验环境。以下演练**全部针对你自己搭建的靶机**，不涉及任何未授权目标。

- DVWA 容器：`http://192.168.56.102:8080`
- Metasploitable2（含 Mutillidae、DVWA）：`http://192.168.56.101`
- Juice Shop（软 404 典型）：`docker run -d -p 3000:3000 bkimminich/juice-shop` → `http://192.168.56.103:3000`
- 攻击机 Kali：`192.168.56.10`

> wfuzz 的官方文档示例使用 `testphp.vulnweb.com`（Acunetix 提供的**公开练习站点**）。本教程的演练全部改成本地靶机。

### 场景 1：目录爆破（含详情输出）

```bash
wfuzz -c -v -w /usr/share/wfuzz/wordlist/general/common.txt \
      --hc 404 --hw 12 http://192.168.56.101/FUZZ
```

预期输出片段：

```text
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://192.168.56.101/FUZZ
Total requests: 950

=====================================================================
ID           Response   Lines    Word     Chars       Payload
=====================================================================

000000013:   403        10 L     20 W     289 Ch      ".htaccess"
000000015:   403        10 L     20 W     289 Ch      ".htpasswd"
000000078:   200        30 L     45 W     891 Ch      "index.php"
000000163:   301        10 L     20 W     332 Ch      "phpmyadmin"
000000712:   301        10 L     20 W     320 Ch      "test"

Total time: 12.345678
Processed Requests: 950
Filtered Requests: 945
Requests/sec.: 76.9
```

解读：
- `-v` 让输出包含 `ID / Response / Lines / Word / Chars / Payload` 五列——**这五个维度正好对应过滤器能用的字段**。
- `--hc 404` 隐藏 404，`--hw 12` 隐藏词数为 12 的响应（用来排除某个软 404 页面）。
- 末尾的 `Filtered Requests: 945` 说明过滤生效了。
- `-c` 加颜色，方便肉眼在长输出里找 200/301。

### 场景 2：用基线（BBB）自动排除软 404

```bash
# Juice Shop 是 SPA，对任意路径都返回 200 + 同一个页面
wfuzz -c -w /usr/share/seclists/Discovery/Web-Content/common.txt \
      --hc BBB http://192.168.56.103:3000/FUZZ
```

预期输出片段：

```text
Target: http://192.168.56.103:3000/FUZZ
Total requests: 4614

=====================================================================
ID           Response   Lines    Word     Chars       Payload
=====================================================================

000000018:   200        34 L     58 W     2508 Ch     "rest"
000000212:   200        4 L      7 W      61 Ch      "robots.txt"
000000301:   302        1 L      4 W      24 Ch      "assets"

Total time: 62.1
Processed Requests: 4614
Filtered Requests: 4611
```

解读：**`--hc BBB` 是 wfuzz 相对其他工具最优雅的地方**——它自动发一个基线请求，测出"不存在的路径返回什么状态码"，然后隐藏所有与之相同的响应。上面这个例子里，软 404 也是 200，但基线检测让 wfuzz 知道"200 也代表不存在"，于是只剩三个真实结果。

> 注意：`BBB` 比较的是**状态码**。如果软 404 也是 200 但长度不同，`--hc BBB` 就不够了，需要用 `--hh BBB`（比较字符数）。

### 场景 3：无需字典的参数 fuzz（`-z range` / `-z list`）

```bash
# 1) 数字型参数：枚举 id
wfuzz -c -z range,1-100 --hl 97 http://192.168.56.101/page.php?id=FUZZ

# 2) 内联列表：不需要准备字典文件
wfuzz -c -z list,admin-test-dev-backup http://192.168.56.101/FUZZ

# 3) HTTP 方法爆破
wfuzz -c -z list,GET-HEAD-POST-TRACE-OPTIONS -X FUZZ http://192.168.56.101/

# 4) 短口令排列组合（permutation 会生成字符的所有排列）
wfuzz -c -z permutation,abc12 -d "user=admin&pass=FUZZ" \
      --sc 200 http://192.168.56.101/login.php
```

解读：
- `-z range,1-100` 完全不用字典——**探测数字型参数（`id=`、`user_id=`）时极其方便**。
- `-z list,a-b-c` 用内联列表，适合只有几个候选值的场景。
- `-X FUZZ` 爆破 HTTP 方法，能发现 `PUT`/`DELETE` 这类危险方法是否被开启（配合 `--sc 200`）。
- `permutation` 会生成字符的**所有排列**（`abc` → `abc`、`acb`、`bac`…），适合短口令/枚举短名称——注意它的组合数会阶乘级增长，别用太长的字符集。

### 场景 4：多关键字 + 多载荷（用户名密码爆破）

```bash
wfuzz -c -z file,/usr/share/seclists/Usernames/top-usernames-shortlist.txt \
         -z file,/usr/share/seclists/Passwords/darkweb2017-top100.txt \
      --sc 302 \
      -d "username=FUZZ&password=FUZ2Z&Login=Login" \
      http://192.168.56.102:8080/login.php
```

预期输出片段：

```text
=====================================================================
ID           Response   Lines    Word     Chars       Payload
=====================================================================

000000147:   302        0 L      0 W      0 Ch        "admin - password"

Total requests: 1700
```

解读：
- **第一个 `-z` → `FUZZ`，第二个 `-z` → `FUZ2Z`**。默认迭代器是 `product`（笛卡尔积），所以请求数 = 17 × 100 = 1700。
- `--sc 302` 只显示状态码为 302 的响应——**DVWA 登录成功会重定向到 `index.php`，失败则留在 `login.php`**，所以 302 是成功的标志。
- 拿到凭据后，把 Cookie 带上做目录爆破（见场景 5）。

**如果想"用户名和密码一一对应"**（比如从泄露库里拿到的用户名-密码对）：

```bash
# 用 -m 指定迭代器（改为 zip 之类的并行推进）
wfuzz -c -z file,userpass_pairs.txt -m zip -d "cred=FUZZ" http://target/login
```

### 场景 5：需要登录态 + 递归 + 代理观察

```bash
# 1) 带 Cookie 做目录爆破
wfuzz -c -w /usr/share/seclists/Discovery/Web-Content/common.txt \
      -b "PHPSESSID=abc123; security=low" \
      --hc 404 \
      http://192.168.56.102:8080/FUZZ

# 2) 递归（最大深度 2）
wfuzz -c -w /usr/share/seclists/Discovery/Web-Content/raft-small-directories.txt \
      -R 2 --hc 404 --hc BBB \
      http://192.168.56.101/FUZZ

# 3) 走 Burp 代理，事后在 Proxy History 里复盘
wfuzz -c -w /usr/share/seclists/Discovery/Web-Content/common.txt \
      -p 127.0.0.1:8080 --hc 404 \
      http://192.168.56.101/FUZZ

# 4) 先用 --dry-run 确认将要发出的请求长相
wfuzz -z range --zD 0-3 -u "http://192.168.56.101/page.php?id=FUZZ" --dry-run
```

解读：
- `-b` 传 Cookie（可重复多个 `-b`）。
- `-R 2` 递归深度 2。**注意递归会让请求数成倍增长**，配合 `--hc BBB` 减少噪声。
- `-p host:port` 走代理；也可以 `-p localhost:2222:SOCKS5` 指定类型，多个 `-p` 可轮换代理。
- `--dry-run` 是 wfuzz 很实用的调试功能——**不实际发请求，只打印会发出的 URL**，用来确认关键字替换是否符合预期（新手常犯的错是关键字位置写错）。

### 场景 6：插件（scripts）与自定义输出字段

```bash
# 1) 查看可用插件
wfuzz -e scripts | head -20

# 2) 用 robots 插件（自动读取并解析 robots.txt）
wfuzz --script=robots -z list,robots.txt http://192.168.56.101/FUZZ

# 3) 用 links 插件抓取页面里的链接，并只保留 .js
wfuzz -z list --zD http://192.168.56.101/ \
      --script=links --script-args=links.regex=.*js$,links.enqueue=False \
      -u FUZZ -o field --field plugins.links.link

# 4) 快捷方式：-A = --script=default -v -c
wfuzz -A -w /usr/share/seclists/Discovery/Web-Content/common.txt --hc 404 \
      http://192.168.56.101/FUZZ

# 5) JSON 输出 + 落盘
wfuzz -c -w words.txt --hc 404 -o json -f /tmp/wfuzz_out.json,json \
      http://192.168.56.101/FUZZ
```

解读：
- **插件系统是 wfuzz 区别于 gobuster/ffuf 的特色**。`links` 插件能从响应里提取链接并可作为新的 fuzz 输入；`robots` 插件会解析 robots.txt 并枚举其中的 Disallow 路径。
- `--field plugins.links.link` 直接输出插件产生的字段——这让 wfuzz 可以当作**爬虫 + 管道**使用。
- `-f file,printer` 一次写到文件，注意格式要跟 printer 名对应。

## 6. 输出解读

### 详细输出列（`-v`）

| 列 | 含义 | 对应过滤器字段 |
|----|------|---------------|
| `ID` | 请求序号 | — |
| `Response` | HTTP 状态码 | `c`（`--hc`/`--sc`） |
| `Lines` | 响应行数 | `l`（`--hl`/`--sl`） |
| `Word` | 响应词数 | `w`（`--hw`/`--sw`） |
| `Chars` | 响应字符数（长度） | `h`（`--hh`/`--sh`） |
| `Payload` | 代入关键字的载荷值 | — |

### 末尾统计

| 行 | 含义 |
|----|------|
| `Total requests` | 总请求数（载荷组合数） |
| `Processed Requests` | 实际处理数 |
| `Filtered Requests` | 被过滤掉的数量 |
| `Requests/sec.` | 平均速率 |
| `Total time` | 总耗时 |

### 状态码价值判断

| 状态码 | 价值 |
|--------|------|
| `200` | 可访问（**但要先用 `--hc BBB` 或 `--hh` 排除软 404**） |
| `301/302` | 重定向（`--efield r` 可显示 Location） |
| `401` | 需要认证 |
| `403` | 路径存在但禁止（**有价值**） |
| `405` | 方法不允许（说明路径存在） |
| `500` | 服务端错误（**值得单独跟进**） |

### 判断要点

1. **先跑一次 `--dry-run`**，确认关键字替换是对的。
2. **优先用 `--hc BBB`**——它让"软 404"自动消失，是最省心的过滤方式。
3. **`Charts` 输出本身也值得看**：如果所有响应都集中在某个长度上，说明有一个统一的错误页，用 `--hh <该长度>` 排掉。
4. **wfuzz 的速度不如 ffuf/gobuster**（Python 实现 + 默认 10 并发）。大字典场景建议先调 `-t`，或直接换 [ffuf](ffuf.md)。

## 7. 与其他工具配合

```bash
# 1) wfuzz 的 --oF 结果可以被 wfuzzp 载荷复用
wfuzz -w words.txt --oF results.fuzz --hc 404 http://192.168.56.101/FUZZ
wfuzz -z wfuzzp,results.fuzz --hc 404 http://192.168.56.101/FUZZ/deeper/

# 2) wfuzz 发现参数 -> sqlmap
wfuzz -c -z range,1-20 -o json -f /tmp/w.json,json \
      "http://192.168.56.101/page.php?id=FUZZ" --hc BBB
jq -r '.[].payload' /tmp/w.json | while read -r v; do
  sqlmap -u "http://192.168.56.101/page.php?id=$v" --batch --smart --level 1
done

# 3) wfuzz 模块（插件）链接提取 -> 再 fuzz
wfuzz -z list --zD http://192.168.56.101/ \
      --script=links --script-args=links.regex=.*\.php$ \
      -u FUZZ -o field --field plugins.links.link > php_links.txt
while read -r l; do wfuzz -w params.txt --hc BBB "${l}?FUZZ=1"; done < php_links.txt

# 4) 三件套分工：dirb 摸底 -> gobuster 全量 -> wfuzz 参数 fuzz
dirb http://192.168.56.101 -r -S -o d.txt
gobuster dir -u http://192.168.56.101 -w big.txt -x php,bak -o g.txt
wfuzz -z range,1-1000 --hc BBB "http://192.168.56.101/product.php?id=FUZZ"

# 5) 用 recipe 固化一套常用参数
wfuzz --dump-recipe myrecipe.json -w words.txt --hc BBB -c -t 20 -u http://target/FUZZ
wfuzz --recipe myrecipe.json     # 之后一条命令复现
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| 结果全是 404/200，看不出有用的 | 软 404 / 未过滤 | `--hc BBB` 或 `--hh <基线长度>`；先 `--dry-run` 确认关键字 |
| `FUZ2Z` 没被替换 | 只有一个 `-z`/`-w`，或者写错了关键字序号 | 第 1 个载荷是 `FUZZ`，第 2 个是 `FUZ2Z`（数字在中间） |
| 打印出"语法错误/无效载荷" | `-z` 的 type 名拼错 | `wfuzz -e payloads` 查正确名称 |
| 速度很慢 | Python + 默认 10 并发 | `-t 30`；大字典换 [ffuf](ffuf.md) |
| 被 WAF 封 | 请求过快 | `-s 0.5`（请求间隔）；`-p` 轮换代理；换 UA `-H "User-Agent: ..."` |
| `-b` 传 Cookie 无效 | 需要多个 `-b` 或含特殊字符 | 每个 Cookie 一个 `-b`；或用 `-H "Cookie: ..."` |
| POST 爆破没反应 | 缺 Content-Type | 加 `-H "Content-Type: application/x-www-form-urlencoded"` |
| `--filter` 报表达式错误 | 语法写错（缺空格/操作符不对） | 格式为 `c=200 and w>100`；比较用 `=`/`!=`/`<`/`>` |
| `BBB` 没起作用 | 用错了字段：`--hc BBB` 比的是状态码 | 要按长度比就用 `--hh BBB`；基线不同页面时会失效 |
| 递归把时间跑爆 | `-R` 深度太大 | `-R 1` 或 `-R 2`；配合 `--hc BBB` 减噪 |
| 输出里中文乱码 | 编码 | 设置 `PYTHONIOENCODING=utf-8` |
| 想复用上次的结果 | 不知道能不能 | `--oF` 保存后，用 `-z wfuzzp,<file>` 复用 |
| `--script` 插件报错 | 插件名写错或参数缺失 | `wfuzz -e scripts` 查名字；`--script-help=<plugin>` 看用法 |

## 9. 防御视角（蓝队）

wfuzz 的流量特征与 [gobuster](gobuster.md)/[ffuf](ffuf.md) 属于同一类（字典爆破），但它有几个**可辨识的额外特征**：

| 特征 | 说明 |
|------|------|
| **默认 UA** | `Wfuzz/3.1.0`（或 `Wfuzz/2.x`），可 `-H` 修改 |
| **载荷模式可辨识** | `-z range` 会产生**连续递增的数字**请求（`?id=1`、`?id=2`…）——正常用户不会这样 |
| **`permutation` 的特征** | 会产生大量"字符集相同、顺序不同"的请求串——很独特 |
| **方法爆破** | `-X FUZZ` 会对同一 URL 依次发 GET/HEAD/POST/PUT/DELETE——**服务器日志里能看到同一路径的不同方法**，这是很明显的特征 |
| **插件产生的二次请求** | `--script=links` 会先抓页面再对提取的链接发请求，呈现"爬虫 + 爆破"的混合模式 |
| **404/403 风暴** | 与所有字典爆破工具相同的通用特征 |

### 检测规则建议

```text
- UA 匹配 (?i)wfuzz
- 单源 IP 60s 内 404 数量 > 100
- 同一路径在短时间内出现多种 HTTP 方法（GET/HEAD/POST/PUT/DELETE/TRACE/OPTIONS）
- 参数值呈连续数字递增模式（?id=1,2,3,4...）
- 请求路径命中敏感词表（\.git/|\.env|\.bak|admin|backup|phpinfo|server-status）
```

**方法爆破的检测特别值得做**：很多服务器**没有限制 TRACE/OPTIONS/PUT**，`-X FUZZ` 一跑就能发现。反过来，蓝队只要在日志里统计"每个路径出现的不同方法数"，就能抓到这类扫描。

### 缓解措施

1. **统一 404 响应**（同上，见其他工具的防御章节）：状态码 + 长度 + 内容完全一致，返回 404 而不是 200。
2. **限制 HTTP 方法**：显式只允许 `GET/POST/HEAD`，其余返回 405；**禁用 TRACE、PUT、DELETE**（除非业务确实需要）。这一步能直接废掉方法爆破。
3. **速率限制与自动封禁**：网关单源限速；对 404 风暴源自动加黑名单。
4. **请求参数类型校验**：对 `id` 这类参数做类型与范围校验，连续数字枚举会返回统一错误页而非真实数据。
5. **校验 Host 头**：反代只接受已知域名。
6. **移除敏感资源**：备份文件、`.git/`、`.env`、测试目录——这是所有目录爆破工具的共同收益来源。

### 紫队用法

```bash
# 自查三件事
wfuzz -c -z list,GET-HEAD-POST-PUT-DELETE-TRACE-OPTIONS -X FUZZ \
      --sc 200 http://my-site.example/          # 1) 有没有多开的方法
wfuzz -c -w common.txt --hc BBB http://my-site.example/FUZZ   # 2) 有没有暴露路径
wfuzz -c -z range,1-50 --hc BBB "http://my-site.example/api/item?id=FUZZ"  # 3) 有没有越权枚举
```

## 10. 参考

- 官方文档：<https://wfuzz.readthedocs.io/>
- 官方仓库：<https://github.com/xmendez/wfuzz>
- Kali 工具页：<https://www.kali.org/tools/wfuzz/>
- 自带字典目录：`ls /usr/share/wfuzz/wordlist/`
- man page：`man wfuzz`（Kali 包内的 man page 版本较旧，为 2.2.11；3.x 的参数可用 `wfuzz --help` 与 `wfuzz -e payloads/printers/scripts` 查看）
- 用法核实：本教程参数取自 man page，并用上游 `docs/user/basicusage.rst` 与 `docs/user/advanced.rst` 中的实际命令示例交叉核对 3.x 语法（`-z`、`--zP`、`--zD`、`--slice`、`--field`/`--efield`、`--filter`、`--prefilter`、`-R`、`-o`、`-f`、`--efield` 等）

---

**相关教程**：[ffuf](ffuf.md) ｜ [gobuster](gobuster.md) ｜ [dirb](dirb.md) ｜ [sqlmap](sqlmap.md) ｜ [commix](commix.md) ｜ [wpscan](wpscan.md)
