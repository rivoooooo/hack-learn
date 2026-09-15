# wafw00f（Web 应用防火墙指纹识别）

> **一句话**：判断目标站点前面有没有 WAF、是哪一家的产品——在动手之前先搞清楚"守卫是谁"。
> **分类**：Web 应用 ｜ **Kali 包**：`wafw00f` ｜ **官方文档**：<https://github.com/EnableSecurity/wafw00f>

## 1. 它解决什么问题

当你对目标发起扫描或注入测试时，会遇到这些情况：

- 请求突然全变成 `403` / `406` / 自定义拦截页
- 响应头多出 `cf-ray`、`x-sucuri-id`、`server: cloudflare`
- 明明该有回显的地方全被过滤掉了

这些通常说明**前面有 WAF**。知道"有没有 WAF、是哪家的"决定了两件事：

1. **要不要调整策略**：Cloudflare 和 ModSecurity 的绕过思路完全不同。
2. **报告怎么写**：扫描结果被 WAF 干扰时，要能说明"结果可能不完整"。

wafw00f 就是回答这个问题的工具。

| 工具 | 定位 |
|------|------|
| **wafw00f** | 专做 WAF 识别（180+ 产品特征） |
| [nmap](../01-信息搜集/nmap.md) `--script http-waf-detect` | 简单判断"有没有 WAF" |
| [nikto](../02-漏洞分析/nikto.md) | 扫描时会顺带提示 WAF，但不专精 |
| 手工看响应头 | 最快的初步判断（`cf-ray`、`x-sucuri-id` 等） |

**核心价值**：wafw00f 提供的是**决策输入**——"我在打谁"。它是整个 Web 测试流程的**第一步**，而不是最后一步。

## 2. 工作原理

wafw00f 用三种互补的技术依次判断：

```text
   wafw00f https://target
        │
   ┌────┴─────────────────────────────────────────────────────────────┐
   │ ① 正常请求（Normal request）                                       │
   │    发一个普通的 GET 请求，分析响应：                                │
   │      - 响应头特征（cf-ray、x-sucuri-id、server: ...）              │
   │      - Cookie 名（如 `__cfduid`、`incap_ses_*`）                   │
   │      - 响应体里的产品字符串、拦截页特征                             │
   │      - 状态码异常                                                  │
   └────┬─────────────────────────────────────────────────────────────┘
        │ 未命中？
   ┌────┴─────────────────────────────────────────────────────────────┐
   │ ② 恶意请求（Malicious request）                                    │
   │    发一个**看起来像攻击**的请求，例如带常见注入 payload 的参数：      │
   │      ?a=1' OR '1'='1                                             │
   │      ?x=<script>alert(1)</script>                                │
   │      ?p=../../etc/passwd                                         │
   │    正常服务器会返回 404/400/200；WAF 通常会**主动拦截**并给出        │
   │    403/406/501，或者返回自己的拦截页面。                            │
   │    → "同一路径，正常请求 OK、恶意请求被拦" 是 WAF 存在的最强证据     │
   └────┬─────────────────────────────────────────────────────────────┘
        │ 未命中？
   ┌────┴─────────────────────────────────────────────────────────────┐
   │ ③ 触发产品特定的指纹                                                │
   │    每个 WAF 产品有自己的"死穴"：                                    │
   │      - 特定的拦截页面文案                                          │
   │      - 特定路径的固定响应（如某些 WAF 的 / 返回固定字符串）          │
   │      - 特定的响应头组合                                            │
   │    wafw00f 内置 180+ 条产品指纹规则（`plugins/` 目录）              │
   └────┬─────────────────────────────────────────────────────────────┘
        │
   输出：
     [+] The site https://target is behind Cloudflare (Cloudflare Inc.) WAF.
     or
     [-] No WAF detected by the generic detection
```

几个关键点：

- **默认只报告"最可能是哪一个"**——即**第一个命中的规则**。加 `-a`（`--findall`）会列出**所有**匹配的 WAF（有些站点是 WAF 套 WAF）。
- **`-r`（`--noredirect`）不跟随重定向**。默认会跟随，这有时会让你误判（重定向后的页面可能来自 CDN 而不是 WAF）。
- **`-t <name>` 可以只测某一个 WAF 产品**。
- **`-l` 列出所有支持的 WAF**——这是了解它覆盖范围的直接方式。
- **误报是存在的**：CDN、反向代理、某些安全插件都可能被误判为 WAF。**结果要结合响应头人工复核。**

## 3. 安装与快速上手

```bash
sudo apt install wafw00f
wafw00f --version
wafw00f --help
wafw00f -l | head -30      # 列出支持的 WAF
```

最小可用命令：

```bash
# 1) 最基本的检测
wafw00f https://target.example.com

# 2) 列出所有匹配的 WAF（而不是只报第一个）
wafw00f -a https://target.example.com

# 3) 批量检测
wafw00f -i urls.txt -o results.txt
```

## 4. 核心参数详解

| 参数 | 作用 | 建议 |
|------|------|------|
| `<URL>` | 目标 URL（位置参数，可多个） | 需要完整 URL（含协议） |
| `-v, --verbose` | 详细输出 | 看它到底发什么、命中哪条规则 |
| `-a, --findall` | **找出所有匹配的 WAF**，而非只报第一个 | **推荐加**——能发现 WAF 链 |
| `-r, --noredirect` | 不跟随重定向 | 结果可疑时用 |
| `-t, --test <NAME>` | 只针对指定 WAF 做检测（用 `-l` 查名称） | 验证某个猜测 |
| `-l, --list` | 列出所有支持的 WAF 产品 | 先跑一次了解覆盖面 |
| `-i, --input-file <FILE>` | 从文件读目标（可含 csv/json/text，csv/json 需要 `url` 列/字段） | 批量 |
| `-o, --output <FILE>` | 输出到文件 | — |
| `-f, --format <FMT>` | 强制输出格式（csv / json / text） | **不写时按 `-o` 的文件扩展名推断** |
| `-p, --proxy <URL>` | 使用代理 | 配 Burp；也可用于隐藏来源 |
| `-H, --headers <FILE>` | 从文件读自定义头（冒号分隔的 name/value） | 需要特殊头时 |
| `-T, --timeout <SEC>` | 请求超时秒数（默认 7） | 慢站点调大 |
| `-V, --version` | 版本 | — |
| `--no-colors` | 关闭颜色输出 | 重定向到文件 |

**关于 `-i` 的输入格式**：支持 csv、json、text。
- `text`：一行一个 URL。
- `csv` / `json`：需要有一个名为 `url` 的列或元素。

## 5. 实战演练

**环境**：

- **有 WAF 的合法目标**：一些公开站点确实部署了 WAF（例如很多使用 Cloudflare 的站点）。**对公网目标做 wafw00f 的探测是低频、无害的**（就几个请求），但仍建议只对你有授权或明确允许测试的目标使用。
- **本地实验环境**：
  - Metasploitable2 的 DVWA（无 WAF）：`http://192.168.56.101`
  - 自建 ModSecurity + Nginx：`docker run -d -p 8082:80 owasp/modsecurity-crs:nginx`（用 OWASP CRS 规则集的官方镜像）

> wafw00f 只发**几个**请求，噪声极小，但它会发送**看起来像攻击的 payload**——这会在目标的 WAF 日志里留下记录。**授权演练时提前告知防守方**。

### 场景 1：检测无 WAF 的本地靶机（基线）

```bash
wafw00f http://192.168.56.101
```

预期输出：

```text
                   ______
                  /      \
                 (  W00f! )
                  \  ____/
                  ,,    __             ____
             ,,,_)   \__/  ___/\      (  W00f! )
            (,  \   /  \  ( _ )       \  w00f/
              \   \_/    \/  _/         )  /
               \     \   /   \    ___  (__/
                \_____\ /_____/   (___)

    WAFW00F
    https://github.com/EnableSecurity/wafw00f

[*] Checking http://192.168.56.101
[+] Generic Detection results:
[-] No WAF detected by the generic detection
[~] Number of requests: 7
```

解读：`[-] No WAF detected by the generic detection` 说明这个 DVWA 靶机没有任何 WAF 保护——**这正是我们先在本地练手的原因**。`Number of requests: 7` 说明整个检测只发了 7 个请求，非常轻量。

### 场景 2：检测有 WAF 的目标

```bash
# 本地 ModSecurity 靶场
docker run -d --name modsec -p 8082:80 owasp/modsecurity-crs:nginx
wafw00f http://192.168.56.102:8082

# 公网目标（示例：某使用 Cloudflare 的站点，低频探测）
wafw00f -a https://example.com
```

预期输出片段（检测到 WAF）：

```text
[*] Checking http://192.168.56.102:8082
[+] The site http://192.168.56.102:8082 is behind ModSecurity (SpiderLabs) WAF.
[~] Number of requests: 7
```

多次运行可能看到同一产品被不同规则命中：

```text
[+] The site https://example.com is behind Cloudflare (Cloudflare Inc.) WAF.
[+] The site https://example.com is behind Cloudflare Bot Management WAF.
[~] Number of requests: 12
```

解读：
- **`-a` 的价值在这里体现**：同一个站点可能同时命中多条规则（Cloudflare 的基础 WAF + Bot Management）。只报第一个（默认行为）会漏掉信息。
- `Number of requests` 是判断"这次检测有多吵"的依据。**12 个请求就完成识别，成本极低**。

### 场景 3：详细模式看它到底怎么判断的

```bash
wafw00f -v https://example.com
```

预期输出片段：

```text
[*] Checking https://example.com
[*] Sending request to https://example.com
[*] Request: GET / HTTP/1.1
[*] Response status: 200
[*] Response headers: {'server': 'cloudflare', 'cf-ray': '...', ...}
[*] Testing for Cloudflare
[*] Sending malicious request
[*] Response status: 403
[*] Matched rule: cloudflare (Cloudflare Inc.)
[+] The site https://example.com is behind Cloudflare (Cloudflare Inc.) WAF.
```

解读：`-v` 让你看到**判断依据**——响应头里的 `server: cloudflare` 和 `cf-ray` 是最直接的证据。**这比只看结论有用得多**，因为当结论可疑时，你能自己判断它是不是误报。

### 场景 4：批量检测 + JSON 输出

```bash
cat > urls.txt <<'EOF'
https://target1.example.com
https://target2.example.com
https://target3.example.com
EOF

wafw00f -i urls.txt -o waf_scan.json -f json --no-colors
cat waf_scan.json | head -40
```

预期输出片段（JSON 结构）：

```json
[
    {
        "url": "https://target1.example.com",
        "detected": true,
        "firewall": "Cloudflare (Cloudflare Inc.)",
        "manufacturer": "Cloudflare Inc."
    },
    {
        "url": "https://target2.example.com",
        "detected": false,
        "firewall": "None",
        "manufacturer": "None"
    }
]
```

解读：`-i`（从文件读）+ `-f json`（JSON 格式）是**接入资产清单流水线**的标准组合。可以先对一批资产做 WAF 摸底，再决定哪些目标值得投入更多测试资源。

用 `jq` 加工：

```bash
jq -r '.[] | [.url, (.detected|tostring), .firewall] | @tsv' waf_scan.json | column -t
jq -r '.[] | select(.detected==true) | .url' waf_scan.json > waf_protected.txt
```

### 场景 5：只测某个产品 + 走代理观察

```bash
# 1) 先看支持哪些产品名
wafw00f -l | grep -i -E "cloudflare|modsecurity|sucuri|imperva"

# 2) 只测指定产品（验证猜想）
wafw00f -t Cloudflare https://target.example.com

# 3) 不跟随重定向（怀疑重定向干扰判断时）
wafw00f -r https://target.example.com

# 4) 走 Burp 代理，观察它到底发了什么请求
wafw00f -v -p http://127.0.0.1:8080 https://target.example.com

# 5) 带自定义头（某些站点需要特定头才响应）
cat > headers.txt <<'EOF'
X-Forwarded-For:127.0.0.1
Accept-Language:en-US
EOF
wafw00f -H headers.txt https://target.example.com
```

解读：
- `-t` 用于**验证特定假设**——比如你已经从响应头猜到了是 Cloudflare，用 `-t Cloudflare` 做定向确认。
- `-p` 走 Burp 能在 Proxy History 里看到 wafw00f 发的 7~12 个请求，**这既方便调试，也能评估这次检测会在对方 WAF 日志里留下什么**。

## 6. 输出解读

### 结果类型

| 输出 | 含义 |
|------|------|
| `[+] The site <URL> is behind <产品> (<厂商>) WAF.` | **检测到 WAF**，并给出产品与厂商 |
| `[-] No WAF detected by the generic detection` | 通用检测未发现 WAF |
| `[~] Number of requests: N` | 本次检测发出的请求数 |
| `[*] Checking <URL>` | 正在检测的目标 |
| `[!] ...` | 错误/异常 |

### JSON 字段

| 字段 | 含义 |
|------|------|
| `url` | 目标 URL |
| `detected` | 是否检测到（布尔） |
| `firewall` | WAF 产品名（未检测到时为 `None`） |
| `manufacturer` | 厂商（未检测到时为 `None`） |

### 常见 WAF 与识别特征（人工复核用）

| 产品 | 响应头/特征线索 |
|------|---------------|
| Cloudflare | `server: cloudflare`、`cf-ray`、`cf-cache-status` |
| Sucuri | `x-sucuri-id`、`x-sucuri-cache`、`server: Sucuri/Cloudproxy` |
| Imperva / Incapsula | `x-cdn: Incapsula`、Cookie `incap_ses_*`、`visid_incap_*` |
| Akamai | `server: AkamaiGHost`、`x-akamai-transformed`、`akamai-grn` |
| AWS WAF / CloudFront | `x-amz-cf-id`、`x-amz-cf-pop`、`server: CloudFront` |
| F5 BIG-IP ASM | `x-wa-info`、Cookie `TS*`（如 `TS01a1b2c3`） |
| ModSecurity | 拦截页里含 `ModSecurity`、`This error was generated by Mod_Security` |
| Barracuda | Cookie `barra_counter_session` |
| Fastly | `x-fastly-request-id`、`x-served-by`、`via: 1.1 varnish` |
| WordPress 插件型 | 拦截页里有插件品牌的 logo/文案（如 Wordfence、Sucuri Security） |

> **手工复核建议**：`curl -i https://target/ | head -20` 看响应头，往往一眼就能确认 wafw00f 的结论对不对。这是验证"是 WAF 还是 CDN"最快的方式。

### 判断要点

1. **`No WAF detected` 不等于"没有防护"**：目标可能用的是自研 WAF（没有已知指纹），或者 WAF 只在特定路径/特定 payload 上才拦截。
2. **CDN 常被误判为 WAF**：CDN 和 WAF 经常是同一家的产品（Cloudflare 既是 CDN 也是 WAF），有时无法严格区分。
3. **`-a` 的完整列表比单条结论更有价值**：能看出"防护是几层"。
4. **结果要结合响应头复核**——wafw00f 是"线索生成器"，不是"结论生成器"。

## 7. 与其他工具配合

```bash
# 1) 流程第一步：先摸 WAF，再决定策略
wafw00f -a https://target | tee waf_result.txt
# 如果有 WAF，后续扫描就要考虑限速/绕过

# 2) 批量资产摸底
cat assets.txt | wafw00f -i /dev/stdin -f json -o waf_all.json --no-colors
jq -r '.[] | select(.detected) | "\(.url)\t\(.firewall)"' waf_all.json | column -t

# 3) 有 WAF -> 用限速和伪装参数的扫描
wafw00f https://target > /tmp/w
if grep -q "is behind" /tmp/w; then
  echo "检测到 WAF，使用温和参数"
  nikto -h https://target -Pause 1 -useragent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -Tuning 23
  nuclei -u https://target -rl 10 -c 5 -silent
else
  echo "未检测到 WAF"
  nikto -h https://target
fi

# 4) 用 sqlmap 的 tamper 应对检测到的 WAF（先确认是哪家）
wafw00f -a https://target
sqlmap -u "https://target/page.php?id=1" --tamper="space2comment,between" --random-agent --delay 1

# 5) nmap 的通用 WAF 检测（交叉验证）
sudo nmap -p443 --script http-waf-detect,http-waf-fingerprint target

# 6) 加上 nuclei 的 WAF 检测模板
nuclei -u https://target -tags waf -silent
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `No WAF detected` 但明显有拦截 | WAF 只在被攻击时拦截（正常请求不拦），或指纹未知 | 用 [nmap](../01-信息搜集/nmap.md) `--script http-waf-detect` 交叉验证；手工看响应头；注意自研 WAF 无法识别 |
| 检测到 WAF 但明显是误报 | CDN / 反代 / 安全插件被误判 | `-v` 看命中规则；`curl -i` 复核响应头 |
| 结果与上次不同 | 不同 CDN 节点、不同规则命中顺序 | 多跑几次；用 `-a` 看完整列表 |
| 请求超时 | 默认 7 秒太短 | `-T 20` |
| 批量检测时某几个 URL 报错 | URL 格式不对 / 网络不可达 | 确保 URL 带协议；`-v` 看具体错误 |
| 输出全是颜色转义符 | ANSI 颜色 | `--no-colors` |
| `-i` 的 csv/json 读取失败 | 文件里没有 `url` 列/字段 | 确保字段名是 `url`；或改成一行的 text 格式 |
| `-f` 报不支持的格式 | 格式名写错 | 只支持 `csv` / `json` / `text` |
| `-t` 报找不到产品 | 产品名拼写不对 | `wafw00f -l` 查准确名称（区分大小写） |
| 检测结果里没有 Cloudflare，但响应头有 `cf-ray` | 该变体未命中规则 | 以响应头为准——**工具给线索，人工下结论** |

## 9. 防御视角（蓝队）

这一节的角度比较特殊：**wafw00f 是攻击者的"侦察工具"，而蓝队应该反过来用它做自检和加固验证。**

### 作为自检工具

```bash
# 定期检查自己的资产是否暴露了 WAF/CDN 指纹
wafw00f -a https://my-site.example
```

关注两点：

1. **如果检测到 WAF，说明 wafw00f 能识别出来——攻击者也能。** 但这本身不是问题；WAF 的价值是拦截，不是隐藏。
2. **如果检测不到 WAF，而你以为部署了** —— 那可能是：
   - WAF 规则集没生效（配置错误）
   - WAF 只保护了部分路径（**常见问题**）
   - 你的 WAF 有指纹泄露问题

### WAF 部署的常见误区

| 误区 | 说明 |
|------|------|
| **只在主域名前部署，子域/API 没保护** | 很多组织只保护 `www`，忘了 `api.`、`admin.`、`staging.`——**这些恰恰是攻击重点** |
| **只开检测模式（DetectionOnly），没开拦截** | ModSecurity 默认可能是 `DetectionOnly`，只记日志不拦——**务必确认 `SecRuleEngine On`** |
| **把 WAF 当唯一防线** | WAF 是**缓解**，不是**修复**。SQL 注入的根因在代码里，`--tamper` 绕过 WAF 是常态 |
| **CDN 的 WAF 默认规则不够** | 很多 CDN 的免费档只做基础防护，业务层漏洞仍需自建规则 |
| **WAF 日志没人看** | 攻击者会反复尝试绕过。**WAF 日志是最有价值的低频信号源**，必须接入告警 |

### 减少指纹泄露（可选）

如果确实需要降低被识别的概率：

- **自定义拦截页面**：把 WAF 默认的 403 页面换成业务自己的错误页，去掉产品名、logo、特征字符串。
- **清理响应头**：去掉 `server` 版本信息；协商能否隐藏 `x-*` 类厂商头（CDN 一般不允许改，这是取舍）。
- **统一错误响应**：让"被 WAF 拦截"和"资源不存在"返回**一样**的页面，避免攻击者用"403 vs 404"的差异倒推规则。

> **但要清醒认识**：隐藏指纹只提高成本，不提供安全。有经验的测试者靠"发送恶意 payload 看响应差异"就能判断 WAF 存在（这正是 wafw00f 的核心方法之一）。**加固的重点应该在减少漏洞，而不是隐藏 WAF。**

### 可检测的 wafw00f 行为

| 行为 | 检测特征 |
|------|---------|
| 它发送的请求 | 7~12 个请求，其中有**明显的攻击 payload**（`' OR '1'='1`、`<script>`、`../`） |
| 请求规律 | 先一个正常 GET，紧接着几个带攻击参数的同路径请求——**这个模式很独特** |
| UA | 默认是 Python `requests` 库的 UA（如 `python-requests/2.x`）——**这是很好的识别点** |
| 判定依据 | WAF 日志里会看到"同一源 IP 在极短时间内先正常访问、再发攻击 payload" |

**检测规则建议**：

```text
- 单源 IP 在 30s 内对同一路径先发正常 GET、随后发含注入/XSS/路径遍历 payload 的请求
- UA 匹配 python-requests（在非 API 流量中出现即为异常）
- 同一源 IP 对同一站点的"攻击 payload 请求数"为小数值（3~8 个）后停止
```

**重要提醒**：wafw00f 的流量**很小**，靠速率阈值抓不到。**真正有效的检测点是"攻击 payload 出现在请求里"**——即使只有一两个请求，也应该告警。这类"低频探测"往往是后续大规模攻击的前奏。

## 10. 参考

- 官方仓库（含 180+ WAF 指纹插件）：<https://github.com/EnableSecurity/wafw00f>
- WAF 产品清单（项目维护）：<https://github.com/EnableSecurity/wafw00f/tree/master/wafw00f/plugins>
- Kali 工具页：<https://www.kali.org/tools/wafw00f/>
- man page：`man wafw00f`（Kali 包未附带 man page；用 `wafw00f --help` 与 `wafw00f -l`）
- 用法核实：本教程参数取自上游 `wafw00f/main.py` 中 `OptionParser` 的实际选项定义（`-v/-a/-r/-t/-o/-f/-i/-l/-p/-V/-H/-T/--no-colors`，已逐项提取核对）

---

**相关教程**：[sqlmap](sqlmap.md) ｜ [wpscan](wpscan.md) ｜ [nikto](../02-漏洞分析/nikto.md) ｜ [nuclei](../02-漏洞分析/nuclei.md) ｜ [whatweb](../01-信息搜集/whatweb.md) ｜ [nmap](../01-信息搜集/nmap.md)
