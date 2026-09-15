# ffuf（快速 Web Fuzzer）

> **一句话**：把字典里的内容替换到 URL / 请求头 / POST 数据里任意位置的 `FUZZ` 关键字上，按状态码、响应长度、内容等条件筛选出"有意义的结果"。
> **分类**：Web 应用 ｜ **Kali 包**：`ffuf` ｜ **官方文档**：<https://github.com/ffuf/ffuf>

## 1. 它解决什么问题

目录爆破只是 fuzz 的一个特例。真正的问题是：**我想把"变动的部分"放在任意位置**——

- URL 路径：`/FUZZ`
- GET 参数：`?id=FUZZ`
- POST 数据：`{"user":"FUZZ"}`
- **请求头**：`Host: FUZZ`（虚拟主机发现）、`X-Forwarded-For: FUZZ`
- **多个位置同时变**：`?user=FUZZ&pass=W2`

ffuf 的 `FUZZ` 关键字 + 多字典 + 强大的 matcher/filter，让它成为最灵活的 Web fuzzer。

| 工具 | 强项 | 弱项 |
|------|------|------|
| **ffuf** | **fuzz 位置任意、多字典、多模式、递归、matcher/filter 极丰富、支持原始 HTTP 请求文件** | 输出不如 gobuster 直观；默认无"软 404 预检查" |
| [gobuster](gobuster.md) | 模式化（dir/dns/vhost/s3/gcs/tftp）、有预检查 | fuzz 灵活性不如 ffuf |
| [wfuzz](wfuzz.md) | 老牌，插件体系 | 慢（Python）、语法繁琐 |
| [dirb](dirb.md) | 简单、默认字典好 | 只能做目录爆破 |

**核心机制**：ffuf 把请求里所有 `FUZZ`（可自定义关键字）替换成字典内容，发出去，然后：

1. **Matcher（匹配）**：只保留满足条件的响应（默认 `-mc 200-299,301,302,307,401,403,405,500`）。
2. **Filter（过滤）**：排除满足条件的响应。

**Matcher 和 Filter 的优先级是：先匹配，再过滤**。所以常见的用法是 `-mc all`（全匹配）+ `-fs 42`（排除长度为 42 的响应）——**这是对付"软 404"最标准的写法**。

## 2. 工作原理

```text
   ffuf -w wordlist.txt -u https://target/FUZZ -mc all -fs 42
        │
   ┌────┴─────────────────────────────────────────────────────────┐
   │ ① 解析参数与字典                                              │
   │    -w file:KEYWORD 可为每个字典指定不同关键字                   │
   │    多字典时用 -mode 决定组合方式：                              │
   │      clusterbomb（默认）：笛卡尔积（每个词 × 每个词）            │
   │      pitchfork  ：并行推进（第 n 个词配第 n 个词）               │
   │      sniper     ：固定位置逐个替换（单字典特化）                 │
   └────┬─────────────────────────────────────────────────────────┘
        │
   ┌────┴─────────────────────────────────────────────────────────┐
   │ ②（可选）自动校准 -ac                                          │
   │    自动发送一组随机 payload，学习"默认响应"的特征                │
   │    （状态码/长度/词数/行数），自动加入 filter                     │
   │    → 大幅减少软 404 造成的假阳性                                │
   └────┬─────────────────────────────────────────────────────────┘
        │
   ┌────┴─────────────────────────────────────────────────────────┐
   │ ③ 并发请求（-t 线程，默认 40；-rate 限速）                       │
   │    每完成一个响应就立即与 matcher/filter 比对                    │
   └────┬─────────────────────────────────────────────────────────┘
        │
   ┌────┴─────────────────────────────────────────────────────────┐
   │ ④ 输出：命中的结果直接打印（含状态码/长度/词数/行数/耗时）       │
   │    -c 着色；-v 显示完整 URL 与重定向目标                        │
   │    -o 输出文件；-of 格式：json/ejson/html/md/csv/ecsv/all       │
   │    -od 把匹配结果（响应体）保存到目录                           │
   │    按 ENTER 进入**交互模式**：动态调整 filter、管理递归队列、     │
   │    保存当前结果 → 这是 ffuf 最被低估的功能                       │
   └────────────────────────────────────────────────────────────────┘
```

**关键机制详解**：

- **`FUZZ` 关键字**：默认是 `FUZZ`，可以用 `-w file:KEY` 改成别的（如 `W1`、`W2`），从而在同一个请求里 fuzz 多个位置。
- **matcher/filter 维度完全对称**：
  - Matcher：`-mc`（状态码）、`-ms`（响应大小）、`-mw`（词数）、`-ml`（行数）、`-mr`（正则）、`-mt`（首字节耗时）
  - Filter：`-fc`、`-fs`、`-fw`、`-fl`、`-fr`、`-ft`
  - `-mmode` / `-fmode` 设为 `and` 或 `or`（默认 `or`）控制多条件组合方式。
- **`-ac` 自动校准**：ffuf 会发一批随机路径，统计其响应特征，自动加到 filter 里。**这是对付软 404 最省事的方式**，比手工 `-fs` 靠谱。
- **交互模式**：跑长任务时按 ENTER 可以实时改 filter（`fs`/`fc`/`fw`/`fl`/`ft`）、看结果（`show`）、管递归队列（`queueshow`/`queuedel`/`queueskip`）、保存 JSON（`savejson`）。改 filter 后会**追溯删除内存中已被过滤掉的假阳性**——这个设计非常实用。
- **`-request` 原始请求文件**：从 Burp 复制请求就能直接 fuzz，不用手工拼所有 header。
- **`-recursion`**：自动对发现的目录递归爆破（URL 必须以 `FUZZ` 结尾）。

## 3. 安装与快速上手

```bash
sudo apt install ffuf
ffuf -V
ffuf -h | head -40
```

最小可用命令：

```bash
# 1) 目录爆破
ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://192.168.56.101/FUZZ

# 2) 自动校准 + 只看有意义的结果
ffuf -w common.txt -u http://192.168.56.101/FUZZ -ac -c

# 3) 虚拟主机发现（fuzz Host 头）
ffuf -w subs.txt -u http://192.168.56.101/ -H "Host: FUZZ.example.lab" -mc 200 -fs 0
```

## 4. 核心参数详解

### HTTP 选项

| 参数 | 作用 | 建议 |
|------|------|------|
| `-u <url>` | 目标 URL（含 `FUZZ`） | 必填 |
| `-X <method>` | HTTP 方法（默认 GET） | 如 `POST`、`PUT` |
| `-d <data>` | POST 数据（含 `FUZZ`） | — |
| `-H <"Name: Value">` | 自定义头（可多次） | `-H "Host: FUZZ"` 是 vhost 发现的用法 |
| `-b <"N1=V1; N2=V2">` | Cookie 数据 | 也可用 `-H "Cookie: ..."` |
| `-cc` / `-ck` | 客户端证书 / 私钥 | 双向 TLS |
| `-http2` | 使用 HTTP/2 | — |
| `-ignore-body` | 不获取响应体 | **大范围扫描时提速** |
| `-r` | 跟随重定向 | 默认不跟随 |
| `-raw` | 不对 URI 编码 | 需要发送原始字符时 |
| `-sni <host>` | 指定 TLS SNI | **不支持 FUZZ 关键字** |
| `-timeout <sec>` | 请求超时（默认 10） | — |
| `-x <url>` | 代理（`http://` 或 `socks5://`） | 配合 Burp |

### 递归

| 参数 | 作用 | 建议 |
|------|------|------|
| `-recursion` | 递归扫描；**只支持 `FUZZ` 关键字，且 URL 必须以 `FUZZ` 结尾** | 目录爆破自动深入 |
| `-recursion-depth <n>` | 最大递归深度（默认 0 = 不限） | 设 2~3 防止爆炸 |
| `-recursion-strategy <default\|greedy>` | `default` 只在重定向时递归；`greedy` 对所有命中都递归 | `greedy` 更全但请求量大 |

### 通用选项

| 参数 | 作用 | 建议 |
|------|------|------|
| `-V` | 显示版本 | — |
| `-ac` | **自动校准过滤条件** | **强烈建议默认加上** |
| `-acc <str>` | 自定义自动校准字符串（可多次，隐含 `-ac`） | 高级 |
| `-ach` | 按主机做自动校准 | 多目标时 |
| `-ack <keyword>` | 自动校准用的关键字（默认 `FUZZ`） | — |
| `-acs <str>` | 自定义自动校准策略（可多次，隐含 `-ac`） | 高级 |
| `-c` | 彩色输出 | 推荐 |
| `-config <file>` | 从配置文件加载 | 固化常用参数 |
| `-json` | JSON 输出（按行分隔的 JSON 记录） | 流水线 |
| `-maxtime <sec>` | 整个进程最长时间 | **长任务必设** |
| `-maxtime-job <sec>` | 每个 job 最长时间 | — |
| `-noninteractive` | 禁用交互控制台 | 脚本化 |
| `-p <sec\|range>` | 请求之间的延迟（如 `0.1` 或 `0.1-2.0` 随机范围） | **生产环境必设** |
| `-rate <n>` | 每秒请求数上限（默认 0 = 不限） | 替代 `-t` 的另一种限速方式 |
| `-s` | 静默模式，不打印额外信息 | 脚本化 |
| `-sa` | 遇任何错误就停止（隐含 `-sf` 和 `-se`） | — |
| `-se` | 遇可疑错误就停止 | — |
| `-sf` | 当 >95% 响应是 403 时停止 | 被 WAF 拦时自动止损 |
| `-scraperfile <f>` / `-scrapers <groups>` | 自定义/选择主动抓取器组（默认 all） | 从响应里提取更多信息 |
| `-search <hash>` | 从 ffuf 历史中搜索某个 FFUFHASH 结果 | 找回历史输出 |
| `-t <n>` | 并发线程数（默认 40） | 内网 40~100；公网 10~20 |
| `-v` | 详细输出（显示完整 URL 和重定向目标） | — |

### Matcher（匹配）

| 参数 | 作用 | 建议 |
|------|------|------|
| `-mc <codes\|all>` | 匹配状态码（默认 `200-299,301,302,307,401,403,405,500`） | 想全部匹配用 `-mc all`（配合 filter） |
| `-ms <sizes>` | 匹配响应大小 | — |
| `-mw <n>` | 匹配响应词数 | — |
| `-ml <n>` | 匹配响应行数 | — |
| `-mr <regex>` | 匹配正则 | 如 `-mr "root:"` |
| `-mt <cond>` | 匹配到首字节耗时（`>100` 或 `<100` 毫秒） | 检测延迟型行为 |
| `-mmode <and\|or>` | matcher 组合方式（默认 or） | — |

### Filter（过滤）

| 参数 | 作用 | 建议 |
|------|------|------|
| `-fc <codes>` | 过滤状态码（支持范围） | 如 `-fc 404,403` |
| `-fs <sizes>` | **过滤响应大小** | **对付软 404 的主力**：`-fs 42` |
| `-fw <n>` | 过滤响应词数 | — |
| `-fl <n>` | 过滤响应行数 | 常用于"行数恒定的错误页" |
| `-fr <regex>` | 过滤正则 | 如 `-fr "not found"` |
| `-ft <cond>` | 过滤首字节耗时 | 排除慢响应 |
| `-fmode <and\|or>` | filter 组合方式（默认 or） | — |

### 输入

| 参数 | 作用 | 建议 |
|------|------|------|
| `-w <file[:KEYWORD]>` | 字典文件，可为每个字典指定关键字 | 多字典 = 多 `-w` |
| `-mode <clusterbomb\|pitchfork\|sniper>` | 多字典组合方式（默认 clusterbomb） | 见下方说明 |
| `-e <exts>` | 逗号分隔的扩展名列表（扩展 `FUZZ`） | 目录爆破加后缀 |
| `-D` | DirSearch 字典兼容模式（与 `-e` 配合） | — |
| `-ic` | 忽略字典里的注释行 | — |
| `-enc <encoders>` | 关键字的编码器，如 `FUZZ:urlencode b64encode` | 特殊字符处理 |
| `-request <file>` | 从原始 HTTP 请求文件读取（含 `FUZZ`） | **从 Burp 导出后直接用** |
| `-request-proto <proto>` | 与原始请求配合的协议（默认 https） | — |
| `-input-cmd <cmd>` | 用命令产出输入（需 `-input-num`，会覆盖 `-w`） | 动态字典 |
| `-input-num <n>` | 输入条数（与 `-input-cmd` 配合，默认 100） | — |
| `-input-shell <sh>` | 运行命令使用的 shell | — |

**多字典组合模式**：

| 模式 | 行为 | 请求数 |
|------|------|--------|
| `clusterbomb`（默认） | 笛卡尔积：A 的每个词配 B 的每个词 | \|A\| × \|B\| |
| `pitchfork` | 并行推进：第 n 个词配第 n 个词 | max(\|A\|, \|B\|) |
| `sniper` | 单字典特化，逐个位置替换 | — |

### 输出

| 参数 | 作用 | 建议 |
|------|------|------|
| `-o <file>` | 结果写入文件 | — |
| `-of <fmt>` | 输出格式：`json`（默认）、`ejson`、`html`、`md`、`csv`、`ecsv`、`all` | `all` 一次出全部 |
| `-od <dir>` | 把匹配结果的响应体保存到目录 | 留证据 |
| `-or` | 没有结果时不创建输出文件 | — |
| `-audit-log <file>` | 记录所有请求、响应与配置 | 完整审计 |
| `-debug-log <file>` | 内部日志 | 排障 |

### 交互模式命令

按 **ENTER** 进入，然后可用：

| 命令 | 作用 |
|------|------|
| `fc` / `afc [v]` | （重）配置 / 追加状态码过滤 |
| `fl` / `afl [v]` | 行数过滤 |
| `fw` / `afw [v]` | 词数过滤 |
| `fs` / `afs [v]` | 响应大小过滤 |
| `ft` / `aft [v]` | 耗时过滤 |
| `rate [v]` | 调整每秒请求数 |
| `show` | 打印当前所有匹配结果 |
| `savejson [file]` | 保存当前匹配到文件 |
| `queueshow` / `queuedel [n]` / `queueskip` | 查看/删除/跳过递归队列 |
| `restart` | 重置状态并从头重新开始当前 job |
| `resume` | 恢复当前 job（同 ENTER） |
| `help` | 帮助 |

> **重要提示**：负向匹配（被 filter 掉的）**不会存到内存**，所以"放宽 filter"无法找回已丢弃的结果——这种情况要用 `restart`。

## 5. 实战演练

**环境**：本地实验环境。

- DVWA 容器：`http://192.168.56.102:8080`
- Metasploitable2：`http://192.168.56.101`
- Juice Shop：`docker run -d -p 3000:3000 bkimminich/juice-shop` → `http://192.168.56.103:3000`
- 攻击机 Kali：`192.168.56.10`

> 只对授权目标 fuzz。生产环境请用 `-rate` 或 `-p` 限速，并用 `-t` 降低并发。

### 场景 1：目录爆破（含自动校准）

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt \
     -u http://192.168.56.101/FUZZ \
     -mc all -ac -c -t 40
```

预期输出片段：

```text
        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/   v2.2.1
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.56.101/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: all
________________________________________________

.htaccess               [Status: 403, Size: 289, Words: 20, Lines: 10, Duration: 4ms]
.htpasswd               [Status: 403, Size: 289, Words: 20, Lines: 10, Duration: 3ms]
cgi-bin/                [Status: 403, Size: 287, Words: 20, Lines: 10, Duration: 4ms]
index.php               [Status: 200, Size: 891, Words: 45, Lines: 30, Duration: 5ms]
phpMyAdmin/             [Status: 301, Size: 332, Words: 20, Lines: 10, Duration: 4ms]
test/                   [Status: 301, Size: 320, Words: 20, Lines: 10, Duration: 4ms]
:: Progress: [4614/4614] :: Job [1/1] :: 892 req/sec :: Duration: [0:00:06] :: Errors: 0 ::
```

解读：
- `-mc all` + `-ac` 的组合：**全匹配，再靠自动校准把"默认响应"过滤掉**。这比手工 `-fs` 更适应各种目标。
- 输出列含义：`状态码 / 响应大小 / 词数 / 行数 / 耗时`。**这五个维度就是 matcher/filter 的全部维度**——你可以用其中任何一个来区分真假结果。
- `Duration` 也是有用信息：某些注入点的响应时间会明显更长。

### 场景 2：对付软 404（手工定位 + 精确过滤）

```bash
# 第一步：先看"不存在的路径"返回什么
ffuf -w <(echo "thispathdoesnotexist12345") -u http://192.168.56.103:3000/FUZZ -mc all -c
```

预期输出：

```text
thispathdoesnotexist12345 [Status: 200, Size: 26542, Words: 4021, Lines: 134, Duration: 28ms]
```

解读：**状态码是 200，但这是"找不到"页面**（典型的 SPA/现代框架行为）。记住 Size=26542。

```bash
# 第二步：按响应长度过滤
ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt \
     -u http://192.168.56.103:3000/FUZZ \
     -mc all -fs 26542 -c -o ffuf_juiceshop.json
```

预期输出片段：

```text
rest                    [Status: 200, Size: 2508, Words: 58, Lines: 34, Duration: 15ms]
robots.txt              [Status: 200, Size: 61, Words: 7, Lines: 4, Duration: 3ms]
assets                  [Status: 302, Size: 24, Words: 4, Lines: 1, Duration: 4ms]
```

解读：`-fs 26542` 把所有长度为 26542 的"软 404"过滤掉，剩下的就是**真正的有效路径**。这就是 ffuf 最核心的用法。

**如果有多条基线长度**（不同的 404 页），可以叠起来：`-fs 26542,1234,5678`，或者用 `-fl`（按行数）`-fw`（按词数）——**行数和词数往往比长度更稳定**。

### 场景 3：虚拟主机发现（fuzz Host 头）

```bash
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
     -u http://192.168.56.101/ \
     -H "Host: FUZZ.example.lab" \
     -mc all -ac -c -t 50
```

预期输出片段：

```text
admin                   [Status: 200, Size: 4213, Words: 320, Lines: 88, Duration: 5ms]
default                 [Status: 200, Size: 108, Words: 12, Lines: 1, Duration: 4ms]
intranet                [Status: 200, Size: 12984, Words: 1102, Lines: 245, Duration: 6ms]
```

解读：
- `-H "Host: FUZZ.example.lab"` 让 ffuf 用字典替换 Host 头——**这是发现"DNS 里查不到但 Web 服务器会路由"的站点的标准手法**。
- 默认站点（不匹配任何 vhost 时）的响应会被 `-ac` 或 `-fs` 过滤掉。
- `-mc all` 在这里很关键：有些 vhost 会返回 302/403，用默认 matcher 会漏掉。

### 场景 4：参数 fuzz 与 POST 数据 fuzz

```bash
# GET 参数 fuzz
ffuf -w params.txt -u "http://192.168.56.101/index.php?FUZZ=test" \
     -mc all -fs 891 -c

# POST 数据 fuzz（含多个位置）
ffuf -w /usr/share/seclists/Usernames/top-usernames-shortlist.txt:USER \
     -w /usr/share/seclists/Passwords/darkweb2017-top100.txt:PASS \
     -mode pitchfork \
     -u http://192.168.56.101/login.php \
     -X POST -d "username=USER&password=PASS&Login=Login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -mc all -fr "Login failed" -c

# JSON body fuzz
ffuf -w entries.txt -u http://192.168.56.103:3000/api/login \
     -X POST -H "Content-Type: application/json" \
     -d '{"email":"FUZZ","password":"x"}' \
     -fr "error" -c
```

解读：
- 多字典用 `文件:关键字` 的语法为每个字典指定关键字。`-mode pitchfork` 是**并行推进**——适合"用户名密码一一对应"的场景。
- `-fr "Login failed"` 过滤掉失败页面，只保留成功（响应里不含该字符串）的请求。
- JSON fuzz 时注意 `-d` 里的引号：外层用单引号，内层用双引号。

### 场景 5（进阶）：从 Burp 导出请求 + 递归 + 限速

```bash
# 1) 从 Burp 复制原始请求到 req.txt，把要 fuzz 的位置改成 FUZZ
cat req.txt
#   GET /api/v1/FUZZ HTTP/1.1
#   Host: api.example.lab
#   Authorization: Bearer eyJhbGci...
#   User-Agent: Mozilla/5.0 ...
#
ffuf -request req.txt -request-proto https \
     -w /usr/share/seclists/Discovery/Web-Content/api-endpoints.txt \
     -mc all -ac -c -t 20 -rate 20 \
     -o api_endpoints.json -of json

# 2) 递归目录爆破（URL 必须以 FUZZ 结尾）+ 深度限制
ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-small-directories.txt \
     -u http://192.168.56.101/FUZZ \
     -recursion -recursion-depth 2 -recursion-strategy greedy \
     -mc all -ac -c -maxtime 300

# 3) 生产环境友好参数（严格限速 + 生产安全）
ffuf -w wordlist.txt -u https://production.example.com/FUZZ \
     -mc all -ac -t 5 -p 0.5 \
     -maxtime 600 \
     -o prod_fuzz.json -of json \
     -H "User-Agent: Mozilla/5.0 (compatible; InternalAudit/1.0)"
```

解读：
- `-request` 免去了手工复制所有 header（尤其是 token），**是最贴近实战的用法**。
- `-recursion-strategy greedy` 会对**所有命中**递归（不只是重定向），覆盖更全但请求量成倍增长——务必配 `-recursion-depth`。
- `-t 5 -p 0.5`（5 线程 + 每次请求间隔 0.5 秒）是生产环境的基本礼仪。
- `-maxtime 600` 保证任务不会无限跑下去。

### 场景 6：交互模式（长任务中途调优）

```bash
ffuf -w big_wordlist.txt -u http://192.168.56.101/FUZZ -mc all -c
# 任务运行中按 ENTER，然后：
#   fs 891          # 追加"过滤长度为 891"（把软 404 去掉）
#   show            # 看看当前真实结果
#   fc 403          # 顺手把 403 也过滤掉
#   savejson out.json
#   resume          # 继续
```

解读：**这是 ffuf 相比其他 fuzzer 最大的体验优势**。发现结果全是噪声时不用中断重跑，直接加 filter 就行；而且加了 filter 后，**内存里已被误匹配的假阳性会被追溯删除**。

## 6. 输出解读

### 命中行格式

```text
/path   [Status: 200, Size: 891, Words: 45, Lines: 30, Duration: 5ms]
```

| 字段 | 含义 | 用途 |
|------|------|------|
| 输入值 | 字典里替换 `FUZZ` 的那个词 | — |
| `Status` | HTTP 状态码 | matcher `-mc` / filter `-fc` |
| `Size` | 响应体字节数 | **filter `-fs` 的主力维度** |
| `Words` | 响应词数 | filter `-fw`（通常比 Size 稳定） |
| `Lines` | 响应行数 | filter `-fl`（最稳定的维度之一） |
| `Duration` | 请求耗时 | filter `-ft`；也可观察延迟型行为 |
| `:: Progress / Job / req-sec / Duration / Errors` | 进度统计 | 判断是否需要调速率 |

### 状态码价值判断

| 状态码 | 价值 |
|--------|------|
| `200` | 直接可访问（但注意排查软 404） |
| `301/302/307` | 重定向，值得跟踪目标（`-v` 会显示 `-->` 目标） |
| `401` | 需要认证（有资源，可能弱口令） |
| `403` | 存在但禁止（**路径真实存在**，值得尝试绕过） |
| `405` | 方法不被允许（说明路径存在，可试其他方法 `-X`） |
| `500` | 服务器错误（**值得单独跟进**，可能触发异常行为） |
| `200` 但 Size 与基线相同 | **软 404，假阳性** |

### JSON 输出的字段（`-of json`）

```json
{
  "results": [
    {
      "input": {"FUZZ": "admin"},
      "position": 1,
      "status": 200,
      "length": 4213,
      "words": 320,
      "lines": 88,
      "content-type": "text/html",
      "redirectlocation": "",
      "url": "http://192.168.56.101/admin",
      "duration": 5231000,
      "scraper": {}
    }
  ],
  "config": { ... }
}
```

用 `jq` 提取：

```bash
ffuf -w words.txt -u http://target/FUZZ -mc all -ac -o out.json -of json -s
jq -r '.results[] | [.status, .length, .url] | @tsv' out.json | column -t
```

### 判断要点

1. **先确定"基线响应"**，再决定 filter 维度。**行数和词数通常比大小更稳定**（大小会因动态内容变化）。
2. **`-ac` 是省事的选择，手工 `-fs`/`-fl` 是精确的选择**。目标简单时 `-ac` 够用；目标复杂（多个不同错误页）时手工更可靠。
3. **`500` 不要过滤掉**——它往往指向"某个参数让服务端崩了"这种真正有意思的点。
4. **`Duration` 异常长的响应值得单独看**——可能是时间型注入或后端慢查询。

## 7. 与其他工具配合

```bash
# 1) gobuster 找目录 -> ffuf fuzz 参数
gobuster dir -u http://192.168.56.101 -w common.txt -q -e | grep -oP 'http\S+(?=.*Status: 200)' > urls.txt
while read -r u; do
  ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt \
       -u "$u?FUZZ=test" -mc all -ac -s -o "fuzz_$(basename $u).json" -of json
done < urls.txt

# 2) ffuf 发现可疑参数 -> sqlmap 验证注入
ffuf -w params.txt -u "http://target/page.php?FUZZ=1" -mc all -fs 891 -s -o p.json -of json
jq -r '.results[].input.FUZZ' p.json | while read -r param; do
  sqlmap -u "http://target/page.php?$param=1" --batch --smart -p "$param" --level 1
done

# 3) ffuf 结果 -> 按状态码分类输出
jq -r '.results[] | [.status, .url] | @tsv' out.json | sort -n | column -t
jq '[.results[] | select(.status==500)] | length' out.json    # 有多少个 500

# 4) ffuf 保存响应体 -> 人工复核
ffuf -w words.txt -u http://target/FUZZ -mc all -ac -od ./responses/
ls responses/ | head

# 5) 从 Burp 流量直接 fuzz
#    Burp 里右键 → Copy to file → req.txt，改掉要 fuzz 的位置
ffuf -request req.txt -w words.txt -mc all -ac -c
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| 结果成千上万条，全是同一长度 | 软 404 | `-ac` 自动校准；或手工 `-fs <该长度>` |
| `-ac` 也没效果 | 目标对不同路径返回**不同长度**的错误页 | 改用 `-fl`（行数）或 `-fw`（词数）；或 `-fr <错误页面特征>` |
| 明明有的路径没发现 | matcher 太严 | `-mc all`（默认 matcher 不含 500 之外的有些码）；检查是否需要 `-r` |
| `-r` 之后结果全变 200 | 跟随重定向把 302 变 200 | 想保留原始状态码就别加 `-r` |
| URL 里有特殊字符导致 400 | ffuf 自动编码 | 加 `-raw` 不编码；或用 `-enc FUZZ:urlencode` |
| Host 头 fuzz 全部命中 | 未排除默认站点响应 | `-ac` 或 `-fs <默认长度>` |
| `-recursion` 报错 | URL 没有以 `FUZZ` 结尾，或 `FUZZ` 被改成别的关键字 | 改回标准写法：`-u http://t/FUZZ` |
| 递归把磁盘/时间跑爆 | 无限深度 | `-recursion-depth 2`；`-maxtime` |
| 被 WAF 封 IP | 默认 40 线程太快 | `-t 5 -p 0.5` 或 `-rate 20`；`-H "User-Agent: ..."` 换 UA |
| 想放宽 filter 但结果回不来 | 负向匹配不存内存 | 交互模式里用 `restart` 重跑 |
| POST fuzz 全部返回同一结果 | 缺少必要的 Content-Type 头 | 加 `-H "Content-Type: application/json"`（或 urlencoded） |
| 多字典时请求数爆炸 | `-mode clusterbomb` 是笛卡尔积 | 需要一一对应时用 `-mode pitchfork` |
| JSON 输出里没有响应体 | 默认不保存响应体 | 用 `-od <dir>` 保存 |
| 脚本里跑但被交互模式卡住 | 默认会尝试进交互 | 加 `-noninteractive` 或 `-s` |

## 9. 防御视角（蓝队）

ffuf 的流量特征与 [gobuster](gobuster.md) 高度相似（都属于字典爆破），但有几个**额外的检测点**：

| 特征 | 说明 |
|------|------|
| **UA 默认值** | `Fuzz Faster U Fool v2.2.1`（`-H` 可改） |
| **404/403 风暴** | 单源 IP 短时间产生大量 404/403 |
| **固定节奏** | 默认不限速时请求速率恒定且很高（几百 req/s） |
| **Host 头变化** | 同一 IP + **大量不同 Host 头**——这是 vhost fuzz 的独有特征，很多日志/网关都会记录 Host，**容易检测** |
| **字典指纹** | 路径来自公开字典（SecLists），高度可预测 |
| **`-od` 会拉取完整响应体** | 表现为"响应体被完整读取"的请求模式 |

### 检测规则建议

```text
- UA 匹配 (?i)(ffuf|Fuzz Faster U Fool|gobuster|feroxbuster|dirb|wfuzz)
- 单源 IP 60s 内 404 数量 > 100
- 同一源 IP 60s 内出现 > 20 个不同 Host 头（vhost 爆破特征）
- 请求路径命中敏感词表（\.git/|\.env|\.bak|admin|backup|phpinfo）
- 请求速率恒定且 > 50 req/s
```

### 缓解措施

1. **统一错误响应**（最重要）：
   - 所有不存在的路径返回**完全相同**的状态码、长度、内容。
   - **关键细节**：不要返回 `200 + 友好页面`。那虽然能"欺骗"只看状态码的工具，但攻击者用 `-fs` 一条命令就能过滤掉，反而把真实结果暴露得更干净。**最有效的做法是返回 404 + 完全一致的短响应**。
2. **速率限制**：网关/WAF 对单源 IP 做请求速率限制；对高频 404 源自动封禁（fail2ban + Nginx 日志）。
3. **Host 头校验**：反向代理**必须校验 Host 头**，只接受已知域名，其余返回 444/400。这能直接废掉 `-H "Host: FUZZ"` 这类虚拟主机爆破——**这是最容易被忽视但收益很高的加固项**。
4. **减少可发现资产**：删除备份文件、`.git/`、`.env`、测试目录。ffuf 的收益大部分来自"本不该存在的东西"。
5. **管理接口前置认证**：在反向代理层就对 `/admin`、`/api/internal` 强制认证，而不是让应用自己返回 403。
6. **部署 WAF**：对常见字典路径和 UA 做拦截，提高成本。

### 紫队用法

用 ffuf 对自己的资产做三类检查，它们分别对应不同的加固项：

```bash
# 1) 目录是否存在不该暴露的路径 → 对应"减少可发现资产"
# 2) Host 头 fuzz 是否发现未知 vhost   → 对应"Host 头校验"
# 3) 参数 fuzz 是否有 500 响应         → 对应"输入校验"
```

## 10. 参考

- 官方仓库（含 Wiki 与示例）：<https://github.com/ffuf/ffuf>
- Kali 工具页：<https://www.kali.org/tools/ffuf/>
- 字典资源：<https://github.com/danielmiessler/SecLists>
- man page：`man ffuf`（内容完整，含交互模式命令表）
- 用法核实：本教程参数取自 `ffuf 2.2.1` 的 man page（其内容基于上游 README，已逐项核对）

---

**相关教程**：[gobuster](gobuster.md) ｜ [dirb](dirb.md) ｜ [wfuzz](wfuzz.md) ｜ [sqlmap](sqlmap.md) ｜ [commix](commix.md) ｜ [wpscan](wpscan.md) ｜ [whatweb](../01-信息搜集/whatweb.md)
