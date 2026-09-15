# whatweb（Web 指纹识别）

> **一句话**：回答"这是什么网站"——识别 CMS、博客平台、JS 库、Web 服务器、分析工具、嵌入式设备，并附带版本号、邮箱、SQL 报错等线索。
> **分类**：信息搜集 ｜ **Kali 包**：`whatweb` ｜ **官方文档**：<https://github.com/urbanadventurer/WhatWeb>

## 1. 它解决什么问题

发现一个 Web 服务之后，下一步是判断它"由什么构成"：用什么 CMS？哪个版本？Web 服务器是什么？有没有暴露的管理后台？

whatweb 有 **1800+ 插件**，每个插件负责识别一类技术。它和同类工具的分工：

| 工具 | 特点 | 何时用 |
|------|------|--------|
| **whatweb** | 插件最多、有攻击强度分级（1/3/4）、多种日志格式 | 需要"一次识别很多种技术" |
| `curl -I` + 肉眼看 | 最轻量 | 只想看响应头 |
| `httpx` / `httprobe` | 批量存活与标题 | 大规模资产存活探测 |
| [wpscan](../03-Web应用/wpscan.md) | WordPress 深度扫描 | 确认是 WP 后深挖 |
| [nmap](nmap.md) `-sV` | 服务层版本识别 | 想知道 Web 服务器层面的版本 |
| `wafw00f` | WAF 识别 | 想知道前面有没有 WAF |

**关键区别**：whatweb 的重点是**应用层技术栈**（CMS/框架/JS 库），nmap `-sV` 的重点是**服务层软件**（nginx/Apache 版本）。两者互补。

## 2. 工作原理

whatweb 的核心是"插件 + 强度分级"：

```text
   whatweb -a 3 http://target
        │
   ┌────┴──────────────────────────────────────────────┐
   │ ① 发一个基础 HTTP 请求（GET /）                    │
   │    拿到响应头、响应体、状态码、重定向链             │
   └────┬──────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────┐
   │ ② 用 1800+ 插件逐一匹配，每个插件有多个测试：      │
   │    - HTTP 头（Server / X-Powered-By / Set-Cookie）│
   │    - HTML 特征（<meta name="generator">、注释）    │
   │    - 静态文件指纹（favicon md5、/wp-content/ 路径）│
   │    - 已知文件的 md5（--custom-plugin 的 :md5=>）   │
   │    - 正则匹配（版本号、邮箱、SQL 报错串）           │
   └────┬──────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────┐
   │ ③ 按强度决定要不要继续发请求：                     │
   │    -a 1  Stealthy    每个目标只发 1 个请求         │
   │    -a 3  Aggressive  命中后追加请求（能拿版本号）   │
   │    -a 4  Heavy       对所有插件 URL 都试（很慢）    │
   └────┬──────────────────────────────────────────────┘
        │
   输出：简要一行 / 详细 / XML / JSON / SQL / MagicTree / MongoDB
```

**为什么要分级？** 因为级别越高越准确，但也越"吵"（请求越多、越容易被 WAF 拦）。扫描公网网站应该用 `-a 1`，渗透测试环境可以用 `-a 3`。

举例说明插件的"多点验证"：WordPress 插件有 15+ 个测试，除了 `meta generator` 标签，还会检查 favicon、默认安装文件、登录页、相对链接里是否含 `/wp-content/`。所以**删掉 generator 标签也不影响识别**。

## 3. 安装与快速上手

```bash
sudo apt install whatweb
whatweb --version
whatweb --short-help
```

最小可用命令：

```bash
# 1) 最简（默认强度 1，只发一个请求）
whatweb http://192.168.56.102

# 2) 详细输出（含插件描述）
whatweb -v http://192.168.56.102

# 3) 激进模式，尽量拿准确版本
whatweb -a 3 http://192.168.56.102
```

## 4. 核心参数详解

### 目标指定

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `<TARGETs>` | URL、主机名、IP、文件名、CIDR、`x.x.x-x` 范围 | 支持大范围批量 |
| `-i, --input-file=FILE` | 从文件读目标列表 | 大批量必用 |
| `--url-prefix` | 给目标 URL 加前缀 | 如统一加 `https://` |
| `--url-suffix` | 给目标 URL 加后缀 | 如统一加 `/crossdomain.xml` |
| `--url-pattern` | 把目标插入 URL 模板（需配合 `-i`） | 如 `www.example.com/%insert%/robots.txt` |

### 攻击强度（最关键的参数）

| 参数 | 级别 | 行为 | 使用建议 |
|------|------|------|----------|
| `-a 1`（默认） | Stealthy | 每个目标只发 1 个请求，跟随重定向 | **扫描公网/生产站点用这个** |
| `-a 3` | Aggressive | 命中 level-1 插件后追加请求 | 授权渗透测试；能拿到更准确的版本 |
| `-a 4` | Heavy | 对所有插件的 URL 都尝试，请求量巨大 | 只在完全授权的实验环境用 |

### HTTP 选项

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-U, --user-agent=AGENT` | 自定义 User-Agent（默认 `WhatWeb/0.4.9`） | 需要伪装时 |
| `-H, --header` | 添加/替换 HTTP 头（空值表示删除） | 如 `-H "User-Agent:"` 删除默认 UA |
| `--follow-redirect=WHEN` | 何时跟随重定向：`never`/`http-only`/`meta-only`/`same-site`/`always`（默认 `always`） | 只看原始响应时用 `never` |
| `--max-redirects=NUM` | 最大重定向次数（默认 10） | — |
| `-u, --user=<user:password>` | HTTP Basic 认证 | 有凭据时能识别后台 |
| `-c, --cookie=COOKIES` | 携带 Cookie，如 `name=value; n2=v2` | 已登录状态下的指纹 |

### 代理

| 参数 | 作用 |
|------|------|
| `--proxy <host[:port]>` | 设置代理（默认端口 8080） |
| `--proxy-user <user:password>` | 代理认证 |

### 插件

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-l, --list-plugins` | 列出全部插件 | 找插件名 |
| `-I, --info-plugins[=SEARCH]` | 列出插件并显示详细信息（可按关键词搜索） | 了解某个插件做什么 |
| `--search-plugins=STRING` | 按关键词搜索插件 | 快速定位 |
| `-p, --plugins=LIST` | 只选用指定插件（逗号分隔，支持 `+`/`-` 修饰） | **大幅提速**的关键手段 |
| `-g, --grep=STRING\|REGEXP` | 只显示匹配的插件结果 | 从大量输出里筛关键项 |
| `--custom-plugin=DEFINITION` | 命令行定义自定义插件 | 见下方示例 |
| `--dorks=PLUGIN` | 列出该插件相关的 Google dorks | 找更多同类站点 |

自定义插件语法（`--custom-plugin`）：

```bash
# 按页面文本匹配
whatweb --custom-plugin=":text=>'powered by abc'" http://target
# 按正则匹配并提取版本
whatweb --custom-plugin=":version=>/powered[ ]?by ab[0-9]/" http://target
# 按文件 md5 匹配已知指纹
whatweb --custom-plugin=":md5=>'8666257030b94d3bdb46e05945f60b42'" http://target
```

### 输出与日志

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-v, --verbose` | 详细输出（含插件描述）；用两次为调试模式 | 分析时用 |
| `--colour=WHEN` / `--color=WHEN` | `never` / `always` / `auto` | 重定向到文件时用 `never` |
| `-q, --quiet` | 不向 stdout 输出简要日志 | 配合日志文件使用时 |
| `--no-errors` | 抑制错误消息 | 批量扫描时**强烈建议** |
| `--log-brief=FILE` | 一行式简要输出到文件 | 快速留档 |
| `--log-verbose=FILE` | 详细输出到文件 | 报告素材 |
| `--log-json=FILE` | JSON 输出 | **与后续脚本对接的首选** |
| `--log-json-verbose=FILE` | JSON 详细格式 | — |
| `--log-xml=FILE` | XML 输出 | — |
| `--log-errors=FILE` | 错误日志 | 排查 |
| `--log-sql=FILE` + `--log-sql-create=FILE` | SQL INSERT / 建表语句 | 入库分析 |
| `--log-magictree=FILE` | MagicTree XML | 老牌报告工具 |
| `--log-object=FILE` | Ruby 对象检查格式 | 调试 |
| `--log-mongo-*` / `--log-elastic-*` | MongoDB / Elasticsearch 输出 | 集中化存储 |

### 性能

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-t, --max-threads=NUM` | 并发线程数（默认 25） | 大规模扫描可提高，但别把目标打死 |
| `--open-timeout=SEC` | 连接超时（默认 15） | — |
| `--read-timeout=SEC` | 读取超时（默认 30） | — |
| `--wait=SEC` | 每次连接之间等待秒数 | 单线程 + 慢速模式 |
| `--debug` | 插件报错时抛出异常（而非吞掉） | 调试自定义插件 |

### 其他

| 参数 | 作用 |
|------|------|
| `-h, --help` | 完整帮助 |
| `--short-help` | 简短帮助 |
| `--version` | 版本信息 |

## 5. 实战演练

**环境**：本地实验环境。

- DVWA 容器：`docker run -d -p 8080:80 vulnerables/web-dvwa` → `http://192.168.56.102:8080`
- WordPress 容器（用于演示 CMS 识别）：`docker run -d -p 8081:80 wordpress`
- Metasploitable2（含 Mutillidae、DVWA 等多个 Web 应用）：`http://192.168.56.101`

> 对公网目标做指纹识别请用 `-a 1`，并且只对你**有授权**的目标操作。

### 场景 1：单个目标的快速指纹

```bash
whatweb http://192.168.56.102:8080
```

预期输出片段：

```text
http://192.168.56.102:8080 [200 OK] Apache[2.4.25], Country[RESERVED][ZZ],
HTML5, HTTPServer[Debian Linux][Apache/2.4.25 (Debian)],
IP[192.168.56.102], JQuery, Meta-Author[Your Name], PHP[7.0.33],
PasswordField[password], Script, Title[DVWA], X-Powered-By[PHP/7.0.33]
```

解读（一行里信息量很大）：
- `Apache[2.4.25]` + `PHP[7.0.33]` → 技术栈与版本，可直接去 [searchsploit](../02-漏洞分析/searchsploit.md) 查。
- `JQuery` → 前端库。
- `Title[DVWA]` → **这本身就是最强的指纹**，说明目标是 DVWA 靶场。
- `PasswordField[password]` → 存在密码输入框，有登录表单。

### 场景 2：激进模式挖版本号

```bash
whatweb -a 3 -v http://192.168.56.102:8080
```

预期输出片段：

```text
http://192.168.56.102:8080 [200 OK] Apache[2.4.25], ...
    Apache
        Version: 2.4.25
        Certainty: 100%
        ...
    PHP
        Version: 7.0.33
        Certainty: 100%
```

解读：`-a 3` 会在命中后追加请求，所以版本号更准、确信度（Certainty）更高。`-v` 会显示每个插件的匹配依据——对照它就知道"为什么会识别成这个"，排错时非常有用。

### 场景 3：批量扫描网段 + JSON 输出

```bash
# 扫描整个网段的 80 端口（--no-errors 抑制连接失败噪声）
whatweb --no-errors -a 1 --url-prefix http:// 192.168.56.0/24 \
        --log-json whatweb.json --log-brief whatweb.txt

head -20 whatweb.txt
python3 -c "
import json
d=json.load(open('whatweb.json'))
for e in d:
    print(e['target'], '->', ','.join(sorted(e['plugins'].keys())))
"
```

预期输出片段：

```text
http://192.168.56.101 -> Apache,Country,HTML5,HTTPServer,IP,Meta-Refresh,PHP,Title
http://192.168.56.102 -> Apache,HTML5,HTTPServer,IP,JQuery,PHP,Title
```

解读：JSON 格式的 `plugins` 字典是所有识别结果的机器可读形式，非常适合做资产技术栈清单。批量扫描时 `--no-errors` 能避免大量 refused/timeout 噪声。

### 场景 4（进阶）：只跑关心的插件 + grep 筛选 + 自定义指纹

```bash
# 只跑少量插件，大幅提速（适合大网段）
whatweb -a 3 -p "WordPress,MetaGenerator,Title,HTTPServer,X-Powered-By" \
        --no-errors http://192.168.56.0/24

# 只显示含 "WordPress" 或版本号的结果
whatweb -a 3 --grep "WordPress|Version" http://192.168.56.101

# 自定义插件：在页面上找特定字符串
whatweb --custom-plugin=":text=>'phpMyAdmin'" http://192.168.56.101

# 列出 WordPress 插件相关的 Google dork（找同类站点）
whatweb --dorks WordPress
```

解读：`-p` 是最实用的提速手段——1800 个插件里可能只有十几个和你的目标相关。`--grep` 则是在输出侧做过滤。`--dorks` 能给出对应的搜索引擎语法，配合 [theHarvester](theharvester.md) 之类的工具能横向扩展资产。

## 6. 输出解读

一行式简要输出的结构是：`URL [状态码] 插件[值], 插件[值], ...`

| 字段 | 含义 | 下一步 |
|------|------|--------|
| `[200 OK]` | HTTP 状态码 | 非 200 时注意是否被重定向/拦截 |
| `Apache[2.4.25]` / `nginx[1.24.0]` | Web 服务器与版本 | → `searchsploit` |
| `PHP[7.0.33]` | 服务端语言与版本 | → `searchsploit` |
| `X-Powered-By[...]` | 框架标识（常暴露绝对版本） | 高价值指纹 |
| `WordPress[6.4]` | CMS 与版本 | → [wpscan](../03-Web应用/wpscan.md) |
| `JQuery[...]` | 前端库版本 | 查已知 XSS 漏洞 |
| `Title[...]` | 页面标题 | 判断应用身份 |
| `PasswordField[...]` | 存在密码字段 | 存在登录入口 |
| `Meta-Author[...]` | meta 作者 | 可能泄露开发者信息 |
| `Country[...]` / `IP[...]` | IP 地理与地址 | — |
| `Email[...]` | 页面上出现的邮箱 | OSINT 输入 |
| `Cookies[...]` | Cookie 名 | 有时能推断框架（如 `PHPSESSID`） |

**判断要点**：

- **版本号是核心价值**：有了精确版本，就能直接查已知漏洞。`X-Powered-By: PHP/7.0.33` 这种是白送的情报。
- **`Certainty` 低于 100%** 说明是推测（比如只靠 favicon 匹配），报告里要标注置信度。
- **确认 CMS 后换专用工具**：识别出 WordPress 就交给 [wpscan](../03-Web应用/wpscan.md)，比 whatweb 深得多。

## 7. 与其他工具配合

```bash
# 1) nmap 找 Web 端口 -> whatweb 指纹
sudo nmap -p80,443,8080,8443 --open -oG - 192.168.56.0/24 | \
  awk '/Ports:/{print "http://"$2}' > urls.txt
whatweb --no-errors -a 1 -i urls.txt --log-json web_fp.json

# 2) whatweb -> searchsploit：指纹转漏洞查询
whatweb -a 1 http://192.168.56.101 | tr ',' '\n' | grep -oP '\w+\[\K[^\]]+' | sort -u > versions.txt
while read v; do echo "=== $v ==="; searchsploit "$v"; done < versions.txt

# 3) whatweb 判断是不是 WordPress -> wpscan
whatweb -a 1 http://target:8081 | grep -q WordPress && \
  wpscan --url http://target:8081 --enumerate vp,vt,u

# 4) 批量资产的 JSON 汇总分析
whatweb --no-errors -i urls.txt --log-json all.json
jq -r '.[] | [.target, (.plugins.HTTPServer[0] // "-"), (.plugins.PHP[0] // "-")] | @tsv' all.json | column -t
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| 输出只有 `IP` 和 `Title`，没有技术栈 | `-a 1` 只发一个请求，未命中需要追加请求的插件 | 用 `-a 3` |
| 目标被 WAF 拦住 / 返回 403 | 强度过高或 UA 被识别 | 降回 `-a 1`；`-U` 换 UA；加 `--wait 1` |
| 批量扫描输出大量 `Connection refused` | 网段里大部分主机没开 80 | `--no-errors` |
| 扫描极慢 | 默认 25 线程 + 大量 timeout | `--open-timeout 5 --read-timeout 10`；`-t 50`；缩小范围 |
| 同一目标两次结果不同 | 重定向目标不同 / 负载均衡 | `--follow-redirect=never` 看原始响应 |
| 识别出错误的技术 | 插件误报（只靠 favicon 等弱特征） | 看 `-v` 的 `Certainty`；多插件交叉验证 |
| 输出的颜色转义字符污染日志文件 | ANSI 颜色 | `--color never` |
| 想扫描 https 但主机名不匹配证书 | — | 加 `-H "Host: ..."` 或用 `--url-prefix https://` |
| JSON 里字段名和预期不同 | 插件名大小写/结构差异 | 先 `head` 看一条记录再写 `jq` |
| `-p` 指定插件后什么都没识别出来 | 插件名拼写错误 | `-l` 列出所有插件名，或 `--search-plugins` |

## 9. 防御视角（蓝队）

- **whatweb 是主动扫描**：`-a 1` 只发 1 个请求，很隐蔽；`-a 3`/`-a 4` 会发大量特征请求，**很容易被 WAF/IDS 识别**（请求路径、UA `WhatWeb/0.4.9`、固定间隔）。
- **检测**：
  - UA 直接匹配 `WhatWeb`（默认不改 UA）。
  - 单个源 IP 在短时间内请求大量**已知静态资源路径**（`/wp-content/`、`/favicon.ico`、`/cgi-bin/`、`/phpmyadmin/`）——典型的指纹扫描模式。
  - 请求顺序与正常用户浏览完全不同（无静态资源加载、无 Referer）。
- **缓解**：
  - **减少 banner 泄露**：关闭 `ServerTokens Full`（Apache）、`server_tokens off`（nginx）、隐藏 `X-Powered-By`（PHP `expose_php = Off`）。
  - **保持组件更新**：whatweb 给出的版本号是漏洞利用的直接输入，及时打补丁能消除大部分收益。
  - **统一错误页**，避免通过差异化响应暴露技术栈。
  - **WAF 规则**：针对默认 `WhatWeb` UA 和特征路径做拦截或限速。
- **反制思路**：可以故意在页面上投放**假的 generator 标签 / 假版本号**，让扫描工具得出错误结论（属于欺骗性防御，需评估对业务的影响）。

## 10. 参考

- 官方仓库（含完整选项与插件列表）：<https://github.com/urbanadventurer/WhatWeb>
- 项目主页：<https://morningstarsecurity.com/research/whatweb>
- Kali 工具页：<https://www.kali.org/tools/whatweb/>
- man page：`man whatweb`
- 用法核实：本教程参数取自 `whatweb 0.6.4` 的 man page

---

**相关教程**：[nmap](nmap.md) ｜ [theharvester](theharvester.md) ｜ [wpscan](../03-Web应用/wpscan.md) ｜ [nikto](../02-漏洞分析/nikto.md) ｜ [searchsploit](../02-漏洞分析/searchsploit.md) ｜ [gobuster](../03-Web应用/gobuster.md)
