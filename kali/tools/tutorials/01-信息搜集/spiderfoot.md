# spiderfoot（OSINT 自动化与攻击面测绘）

> **一句话**：给一个域名/IP/邮箱/人名，自动跑 200+ 个 OSINT 模块，把散落在公开渠道的资产、泄露、关联实体聚合成一张关系图——既能做渗透前的侦察，也能做防御侧的「我们暴露了什么」体检。
> **分类**：信息搜集 / OSINT 自动化 ｜ **Kali 包**：`spiderfoot`（命令 `spiderfoot`、`spiderfoot-cli`）｜ **官方文档**：<https://www.kali.org/tools/spiderfoot/> ｜ 上游：<https://www.spiderfoot.net>

---

## 1. 它解决什么问题

OSINT 侦察的痛点**不是「查不到」，而是「查不完、串不起来」**：

- 一个域名要查 WHOIS、DNS 记录、子域、证书透明日志、Shodan/Censys、GitHub 泄露、HIBP 邮箱泄露、网页元数据……
- 这些查询分散在几十个站点/API/CLI 工具里，**手工做一次就要几小时**；
- 更关键的是：**结果之间的关联没人帮你连**——「这个子域解析到那个 IP，那个 IP 上还挂着另一个域名，那个域名 WHOIS 用同一个邮箱」这条链**必须自动化才能发现**。

SpiderFoot 就是这个「自动化 + 关联」层：

```
目标（域名/IP/邮箱/人名/ASN/子网）
        │
        ├─ 200+ 模块并发展开（每个模块产出一批「事件」）
        │
        └─ 事件之间自动触发新模块（发现子域 → 查子域；发现 IP → 查 IP；发现邮箱 → 查泄露）
                        │
                        └─ 关联规则（correlation rule）把孤立事件升级为「发现（Finding）」
```

对比同类：

| 工具 | 定位 | 与 SpiderFoot 的差异 |
|------|------|----------------------|
| **SpiderFoot** | **自动化 OSINT 编排 + 关联分析** | 模块最多、有 Web UI 与 CLI、有 correlation 规则；**被动优先** |
| **recon-ng** | 模块化 Web 侦察框架 | 更像「命令行工作台」，需手工逐模块执行；见 [`recon-ng.md`](recon-ng.md) |
| **theHarvester** | 邮箱/子域/主机收集 | **单点工具**，不做关联；常与 SpiderFoot 互补，见 [`theharvester.md`](theharvester.md) |
| **amass** | 攻击面测绘（子域为主） | 子域枚举更强（DNS 爆破/被动源），关联弱；见 [`amass.md`](amass.md) |
| **Maltego** | 图形化 OSINT/关系图 | 商业闭源；SpiderFoot 开源且能用 CLI 批处理 |
| **Shodan/Censys CLI** | 单数据源查询 | 是 SpiderFoot 的**数据源之一**（需要 API key） |

**一句话选型**：要「一次跑完、自动串关系、能出报告」→ SpiderFoot；要「单点精确、脚本化拼装」→ recon-ng / theHarvester。

---

## 2. 工作原理

SpiderFoot 的核心抽象只有两个：**事件（Event）** 和 **模块（Module）**。

```
                    ┌───────────────────────────────┐
   种子目标 ───────► │  Event: DOMAIN_NAME            │
   (-s example.com) │  Event: IP_ADDRESS             │
                    │  Event: EMAILADDR ...          │
                    └───────────────┬───────────────┘
                                    │  事件作为「输入」分发给所有模块
                                    ▼
        ┌──────────────────────────────────────────────────────┐
        │  Module（每个模块声明：能消费哪些事件类型 / 产出哪些） │
        │   sfp_dnsresolve   → INTERNET_NAME, IP_ADDRESS        │
        │   sfp_crt          → INTERNET_NAME（证书透明日志）     │
        │   sfp_whois        → DOMAIN_WHOIS                     │
        │   sfp_haveibeenpwned → EMAILADDR_COMPROMISED          │
        │   sfp_shodan       → TCP_PORT_OPEN, VULNERABILITY…    │
        └───────────────────┬──────────────────────────────────┘
                            │  产出新事件
                            ▼
                 ┌──────────────────────────┐
                 │  事件队列（继续分发）      │   ← 这就是「自动展开」
                 │  新事件 → 又触发新模块     │
                 └──────────┬───────────────┘
                            ▼
                 ┌──────────────────────────┐
                 │  Correlation Rules        │  ← 关联规则
                 │  e.g. 「同一邮箱注册了多个域名」│
                 │       「子域解析到内网 IP」   │
                 └──────────┬───────────────┘
                            ▼
                  Finding（可读结论，进报告）
```

**关键机制**：

- **事件驱动**：SpiderFoot 不写「执行流程」，只定义「事件 → 模块 → 事件」。所以目标越挖越多是**自然结果**，而非写死的流程。
- **`-u` 用例决定模块集合**：
  - `passive`：**只用第三方数据源**，不直接触碰目标（最适合授权边界模糊时，也最不易被发现）；
  - `footprint`：目标自身与公开数据源混合（做资产清单）；
  - `investigate`：**会主动连接目标**（端口扫描、HTTP 抓取），**必须已获授权**；
  - `all`：全部模块（噪音大、易被目标日志记录）。
- **`-x` STRICT MODE**：只启用「能直接消费你给的目标类型」的模块，并关闭事件再展开。用于**限定爆炸半径**（不想让它漫游到无关资产）。
- **模块分类（`-M` 输出里的 `type`）**：`Internal`（内置，不需 key）/ `External`（调第三方站点/API）/ `API key`（需要你自己申请 key，如 Shodan、HIBP、VirusTotal）。
- **Web UI 与 CLI 是同一引擎**：`spiderfoot -l 127.0.0.1:5001` 起 Web 服务；不加 `-s` 时也可直接命令行出结果。

> **与 `-t` 的关系**：`-t` 指定「**只收集哪些事件类型**」，SpiderFoot 会**自动选出让这些事件所需的模块子集**；`-m` 则是「手工点名模块」。`-f` 会过滤掉未在 `-t` 里要求的其他事件类型。

---

## 3. 安装与快速上手

```bash
sudo apt install spiderfoot
command -v spiderfoot spiderfoot-cli
spiderfoot -h
```

```console
root@kali:~# spiderfoot -h
usage: sf.py [-h] [-d] [-l IP:port] [-m mod1,mod2,...] [-M] [-C scanID]
             [-s TARGET] [-t type1,type2,...]
             [-u {all,footprint,investigate,passive}] [-T] [-o {tab,csv,json}]
             [-H] [-n] [-r] [-S LENGTH] [-D DELIMITER] [-f]
             [-F type1,type2,...] [-x] [-q] [-V] [-max-threads MAX_THREADS]

SpiderFoot 4.0.0: Open Source Intelligence Automation.

options:
  -h, --help            show this help message and exit
  -d, --debug           Enable debug output.
  -l IP:port            IP and port to listen on.
  -m mod1,mod2,...      Modules to enable.
  -M, --modules         List available modules.
  -C, --correlate scanID
                        Run correlation rules against a scan ID.
  -s TARGET             Target for the scan.
  -t type1,type2,...    Event types to collect (modules selected
                        automatically).
  -u {all,footprint,investigate,passive}
                        Select modules automatically by use case
  -T, --types           List available event types.
  -o {tab,csv,json}     Output format. Tab is default.
  -H                    Don't print field headers, just data.
  -n                    Strip newlines from data.
  -r                    Include the source data field in tab/csv output.
  -S LENGTH             Maximum data length to display. By default, all data
                        is shown.
  -D DELIMITER          Delimiter to use for CSV output. Default is ,.
  -f                    Filter out other event types that weren't requested
                        with -t.
  -F type1,type2,...    Show only a set of event types, comma-separated.
  -x                    STRICT MODE. Will only enable modules that can
                        directly consume your target, and if -t was specified
                        only those events will be consumed by modules. This
                        overrides -t and -m options.
  -q                    Disable logging. This will also hide errors!
  -V, --version         Display the version of SpiderFoot and exit.
  -max-threads MAX_THREADS
                        Max number of modules to run concurrently.
```

**先摸清模块与事件类型**（这一步能省大量试错）：

```bash
spiderfoot -M | head -40          # 有哪些模块、类型、需要什么 key
spiderfoot -T | head -30          # 有哪些事件类型（-t 的取值）
```

**最小可用**（纯被动，一条命令出 CSV）：

```bash
spiderfoot -s example.com -u passive -o csv > sf_passive.csv
```

**起 Web UI**（推荐交互式使用，结果可视化）：

```bash
spiderfoot -l 127.0.0.1:5001
# 浏览器打开 http://127.0.0.1:5001
```

---

## 4. 核心参数详解

> 全部取自上面的 `spiderfoot -h` 原文。

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-s TARGET` | 指定扫描目标 | 域名/IP/主机名/子网/ASN/邮箱/人名皆可；**一次只给一个目标** |
| `-u {all,footprint,investigate,passive}` | **按用例自动选模块**（最常用） | 首选 `passive`；确认授权后用 `investigate`；`all` 噪音大 |
| `-t type1,type2,...` | 只收集指定**事件类型** | 想要「只要子域和 IP」时用；SpiderFoot 自动选模块 |
| `-m mod1,mod2,...` | 手工点名模块 | 已知要哪个数据源时用（如只跑 `sfp_haveibeenpwned`） |
| `-M, --modules` | **列出所有可用模块** | 开工前必跑：看模块名 + 是否需要 API key |
| `-T, --types` | **列出所有事件类型** | 结合 `-t` 使用 |
| `-x` | **STRICT MODE** | 只启用能直接消费目标的模块，且不再展开新事件；**限制范围/降噪首选** |
| `-f` | 过滤掉未用 `-t` 请求的其他事件类型 | 与 `-t` 搭配，输出更干净 |
| `-F type1,type2,...` | 只**显示**给定类型的事件 | 与 `-f` 不同：`-f` 是「不收集」，`-F` 是「不显示」 |
| `-o {tab,csv,json}` | 输出格式（默认 `tab`） | 进报告/脚本用 `csv`/`json` |
| `-H` | 不打印字段表头，只出数据 | 二次解析用 |
| `-r` | 在 tab/csv 里附带**来源数据字段** | 追溯「这条信息从哪来的」 |
| `-n` | 去掉数据中的换行 | 避免 CSV 行被撑断 |
| `-S LENGTH` | 单条数据最大显示长度 | 抓到大段 HTML/证书时截断 |
| `-D DELIMITER` | CSV 分隔符（默认 `,`） | 数据含逗号时改 `-D ';'` |
| `-q` | 关闭日志输出 | **注意：同时会隐藏错误**，排错时不要加 |
| `-d, --debug` | 打开调试输出 | 模块静默失败时用 |
| `-l IP:port` | 启动 Web 服务并监听 | 交互分析首选；默认建议绑 `127.0.0.1` |
| `-C scanID` | 对已有 scan 重跑关联规则 | 改了 correlation 规则后重算 Finding |
| `-max-threads N` | 并发模块数上限 | 限速/防被第三方 API 封禁 |

### spiderfoot-cli（连 Web 服务的交互式客户端）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-s URL` | SpiderFoot 服务地址（默认 `http://127.0.0.1:5001`） | 远程分析机时用 |
| `-u USER` / `-p PASS` | 用户名密码 | 生产环境**用 `-P PASSFILE` 代替 `-p`**（避免密码进 shell 历史/进程列表） |
| `-P PASSFILE` | 从文件读密码 | 推荐 |
| `-e FILE` | 从文件执行命令（脚本化） | 批量建扫描 |
| `-l FILE` / `-n` | 历史记录文件 / 关闭历史 | `-n` 防止敏感目标名落盘 |
| `-o FILE` | 把命令与输出落到文件 | 留证 |
| `-i` | 允许不安全的 SSL 连接 | 自签证书环境（谨慎） |
| `-k` | 关闭彩色输出 | 转成纯文本报告 |
| `-q` | 静默，只报错 | 脚本化 |

---

## 5. 实战演练

> **环境声明**：以下目标**必须是你自己的域名/服务器，或你已获得书面授权的目标**。
> - 用 `-u passive` 时，请求**只发给第三方数据源**（WHOIS、证书日志、公开 API），不接触目标本身，风险最低；
> - 用 `-u investigate` / `-u all` 时 SpiderFoot **会主动连接目标**（端口、HTTP），**必须先有授权**；
> - 拿自己注册的测试域名（或 `example.com` 这类保留域名）做实验最安全。
> **禁止**对未授权的第三方做 OSINT 聚合（即便是「公开信息」，聚类分析后也可能构成对个人信息的违规处理）。

### 场景 1：被动侦察自己的域名（最安全的起手式）

```bash
# ① 先看有哪些模块可用、哪些需要 API key
spiderfoot -M | head -30
```

```console
root@kali:~# spiderfoot -M | head -30
Module name          Type       Description
-------------------  ---------  ------------------------------
sfp_abuseipdb        API key    Check if an IP is in AbuseIPDB's ...
sfp_accounts         External   Look for possible associated accounts ...
sfp_crt              External   Gather hostnames from historical ...
sfp_dnsbrute         External   Attempt to discover subdomains by ...
sfp_dnsresolve       Internal   Resolve domain names ...
sfp_haveibeenpwned   API key    Check HaveIBeenPwned for compromised ...
...
```

**解读**：`Internal` 的模块不依赖外部服务，一定能跑；`API key` 的模块**没有 key 就会静默跳过**（这是「明明勾了模块却没结果」的最常见原因）。

```bash
# ② 纯被动扫描，输出 CSV
spiderfoot -s example.com -u passive -o csv > sf_example.csv
wc -l sf_example.csv
head -5 sf_example.csv
```

```console
root@kali:~# wc -l sf_example.csv
312 sf_example.csv

root@kali:~# head -5 sf_example.csv
"Updated","Type","Module","Source","Data"
"2026-09-15 10:02:11","Internet Name","sfp_crt","example.com","www.example.com"
"2026-09-15 10:02:11","Internet Name","sfp_crt","example.com","api.example.com"
"2026-09-15 10:02:12","IP Address","sfp_dnsresolve","www.example.com","93.184.216.34"
"2026-09-15 10:02:13","Domain Whois","sfp_whois","example.com","..."
```

**解读**：CSV 的五列就是 SpiderFoot 的「事件模型」——

| 列 | 含义 | 用途 |
|----|------|------|
| `Type` | 事件类型（= `-t` / `-F` 的取值） | 按类型过滤 |
| `Module` | **哪条信息是谁产出的** | 溯源、判断可信度 |
| `Source` | 该事件的「父」实体 | 构建关系图（谁发现了谁） |
| `Data` | 实际内容 | 情报本体 |

```bash
# ③ 只看「攻击面」相关的事件：子域和 IP
awk -F'","' '$2=="Internet Name" || $2=="IP Address"' sf_example.csv | head
# 或者直接在扫描时就限定类型
spiderfoot -s example.com -u passive -t INTERNET_NAME,IP_ADDRESS -F INTERNET_NAME,IP_ADDRESS -o csv
```

**解读**：`-t` 限定收集类型、`-f` 丢弃其他类型、`-F` 限定显示类型。三者叠加可以把 300 行压成 30 行**只含资产的清单**——这正是「攻击面台账」该有的样子。

### 场景 2：Web UI 交互分析 + 关联规则出 Finding

```bash
# ① 起 Web UI（只绑本机）
spiderfoot -l 127.0.0.1:5001
```

浏览器打开 `http://127.0.0.1:5001` → `New Scan`：
- **Scan Target**：`example.com`
- **Scan Name**：`asm-2026-09-15`
- **Use Case**：先选 `Passive`，跑完再考虑 `Footprint`
- 底部 `Scan` 开始。

```console
# ② 用 CLI 也连同一个服务（可选）
root@kali:~# spiderfoot-cli -s http://127.0.0.1:5001
sf> scanlist
sf> scaninfo <scanID>
sf> output <scanID>
```

**Web UI 里看什么**：

| 视图 | 内容 | 报告价值 |
|------|------|----------|
| **Browse** | 按事件类型分组的全部数据 | 明细 |
| **Graph** | 实体关系图（域名—IP—证书—邮箱） | **一页看懂攻击面结构** |
| **Correlations / Findings** | 关联规则命中的结论 | **可直接写进报告** |
| **Export** | CSV/JSON/GEXF | 交下游工具 |

**关联规则（Correlation）为什么重要**：它把「一堆孤立事件」升级为「一条结论」。例如：

```
Rule: "Multiple domains share the same server IP"
  事件1: DOMAIN_NAME example.com       → IP 203.0.113.10
  事件2: DOMAIN_NAME staging.example.net → IP 203.0.113.10
  事件3: DOMAIN_NAME legacy.example.org  → IP 203.0.113.10
  ────────────────────────────────────────────────
  Finding: 三个域名共用一个 IP → 若拿下其中一个，另两个可能同源沦陷
           （且 legacy.* 往往是防护最弱的那个）
```

**排除干扰事件**：SpiderFoot 有个内置的 **exclude list**（`Settings → Exclude`），把 `example.com` 自己的主域、CDN 域名、第三方分析脚本域名加进去，否则 Finding 里全是噪音。

```bash
# ③ 改了关联规则后，对已有扫描重算 Finding
spiderfoot -C <scanID>
```

### 场景 3：用 `-x` 严格模式做「只查授权的那个目标」

**问题**：`-u investigate` 会顺着事件展开，可能漂到你**没被授权**的资产上（比如发现子域是托管商 IP，然后去扫托管商）。

**做法**：`-x` 只启用能直接消费你给的目标类型的模块，**不再展开**：

```bash
# 目标是一个 IP：只跑「能直接吃 IP」的模块，不做二次扩散
spiderfoot -s 203.0.113.10 -x -o csv > sf_ip_strict.csv
head -10 sf_ip_strict.csv
```

```console
"Updated","Type","Module","Source","Data"
"2026-09-15 11:20:01","IP Address","sfp_dnsresolve","203.0.113.10","203.0.113.10"
"2026-09-15 11:20:03","BGP AS","sfp_ipinfo","203.0.113.10","AS64500 Example Networks"
"2026-09-15 11:20:04","TCP Port","sfp_portscan_tcp","203.0.113.10","80"
```

**解读**：`-x` 是**法律/范围合规**的安全阀——它保证「我只查了你让我查的那个东西」。在正式项目里，**先 `-x` 拿最小集，确认范围无误再开更大用例**。

**给模块补 API key**（让 API key 类模块能工作）：

```bash
# Web UI: Settings → 填入 Shodan / HIBP / VirusTotal 等 key → Save
# 之后重跑同一目标，会多出这些模块的产出
spiderfoot -s example.com -u footprint -m sfp_shodan,sfp_haveibeenpwned -o csv
```

**解读**：API key 模块是 OSINT 的「高价值增量」——端口/服务指纹（Shodan）、凭据泄露（HIBP）、样本情报（VirusTotal）。**没有 key 时这些模块不会报错，只是不出结果**。

---

## 6. 输出解读

### 6.1 CLI 输出的核心字段

| 字段 | 含义 | 判断方法 |
|------|------|----------|
| `Updated` | 事件时间 | 判断「是不是本次扫描的新发现」 |
| `Type` | 事件类型 | **决定这条信息的价值等级**（见下表） |
| `Module` | 产出模块 | 判断数据源可靠性；`API key` 模块的结果通常更硬 |
| `Source` | 上游实体 | **构建关系链**：Source → Data 就是一条边 |
| `Data` | 内容 | 情报本体 |

### 6.2 事件的「价值等级」（按扫描目标类型）

| 事件类型（示例） | 含义 | 行动 |
|------------------|------|------|
| `Internet Name` / `Subdomain` | 发现子域 | 加入资产清单 → 逐个做 `whatweb`/`nmap` |
| `IP Address` | 解析到的 IP | 判断是自建还是 CDN/云 |
| `TCP Port` / `UDP Port` | 开放端口 | 与 `nmap` 结果交叉验证 |
| `Email Address` | 邮箱 | 钓鱼面/用户名枚举面 → 交 `theharvester` 补全 |
| `Email Address Compromised` | **邮箱在泄露库中** | **高优先级**：密码可能被复用 |
| `Password` / `Leaked Credential` | 泄露凭据 | **最高优先级**，立即整改 |
| `Domain Whois` | WHOIS 信息 | 找注册人/邮箱/历史 |
| `SSL Certificate` | 证书 | 从 SAN 字段**反推子域**（很有效） |
| `Vulnerability` | 漏洞情报 | 与 `searchsploit`/`nuclei` 联动 |
| `Finding` / `Correlation` | **关联结论** | **直接写报告** |

### 6.3 怎么判断「这次扫描有没有价值」

1. **有没有 Finding**：没有 Finding 说明都是孤立事件，需要补模块或补 API key；
2. **子域数量**：`Internet Name` 事件数远大于预期 → 攻击面比想的宽（重点写报告）；
3. **证书 SAN 交叉**：从 `SSL Certificate` 里挖出的名字往往比 DNS 暴力枚举更全；
4. **有没有 `Compromised` 类事件**：有则**必须**在报告里置顶（凭据泄露是可直接利用的风险）。

---

## 7. 与其他工具配合

```
① 目标确认（自有/授权）
        │
② spiderfoot -u passive ──► 资产与关联全景（子域/IP/邮箱/证书/泄露）
        │
        ├─► 子域清单 ──► amass（补 DNS 爆破/更多被动源）  ../01-信息搜集/amass.md
        ├─► 邮箱清单 ──► theHarvester（补更多邮箱/主机）   theharvester.md
        ├─► 端口线索 ──► nmap -sV（精确服务指纹）          nmap.md
        ├─► Web 资产 ──► whatweb（指纹）→ nikto（扫描）     whatweb.md / ../02-漏洞分析/nikto.md
        ├─► 漏洞线索 ──► searchsploit / nuclei             ../02-漏洞分析/searchsploit.md
        ├─► 自研模块化侦察 ──► recon-ng                    recon-ng.md
        └─► 关系图落地 ──► Export GEXF → Gephi / Maltego
```

- **先广后深**：SpiderFoot 出「面」，`nmap`/`nikto`/`nuclei` 出「点」。
- **先被动后主动**：SpiderFoot `-u passive` 确定范围 → 授权确认 → `nmap` 主动扫。
- **证书是最好用的子域来源**：把 SpiderFoot 抓到的证书与 `amass` 的结果取并集。
- 扫描完的资产台账建议交 [`recon-ng.md`](recon-ng.md) 或表格管理，便于复测对比。

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 勾了很多模块但没结果 | **模块需要 API key**，没 key 就静默跳过 | 看 `-M` 的 Type 列；在 Web UI Settings 填入 key |
| `-u passive` 也「访问了目标」 | 部分 External 模块会取目标页面（如 `sfp_spider` 在某些用例下） | 只跑明确被动的模块：`-m sfp_crt,sfp_whois,sfp_dnsresolve` |
| Web UI 打不开 | 端口占用/绑错地址 | `spiderfoot -l 127.0.0.1:5001`；换端口 |
| 结果里全是自己的主域噪音 | 没配 exclude list | Web UI → Settings → Exclude 加入主域/CDN/第三方域名 |
| 扫描「跑不完」/一直增长 | 事件不断展开（DNS 爆破→大量子域→每个再解析） | 用 `-x` 严格模式；或 `-u passive`；或 `-max-threads` 限速 |
| 第三方 API 返回 429/封禁 | 并发太高触发限流 | 调低 `-max-threads`，或减少 API key 模块 |
| 用了 `-q` 后什么都不知道 | `-q` **同时关闭错误输出** | 排错时去掉 `-q`，用 `-d` |
| CSV 行错乱/串行 | `Data` 里含换行或逗号 | 加 `-n`（去换行）、`-D ';'` 换分隔符 |
| 结果无法复现 | 第三方数据本身在变 | 保留原始 CSV + 时间戳；报告注明「数据快照时间」 |
| 想重算 Finding 但不知道怎么算 | 需要 scanID | Web UI 里能看到 scanID；CLI 用 `-C <scanID>` |

---

## 9. 防御视角（蓝队 / 企业安全）

SpiderFoot 对蓝队最大的价值是**「用攻击者的眼睛看自己」**——它挖到的每一条，攻击者也能挖到。

| 场景 | 用法 | 价值 |
|------|------|------|
| 外部攻击面测绘 | `-u footprint` 跑自有主域 | 输出「我们对外暴露了什么」的权威清单 |
| 影子资产发现 | 关注 `Internet Name` 中**不在 CMDB 里的子域** | 影子 IT / 遗忘的测试环境是常见入口 |
| 凭据泄露监控 | `sfp_haveibeenpwned` 盯企业邮箱域 | 员工邮箱进泄露库 → 强制改密 + 排查复用 |
| 证书 SAN 审计 | 看 `SSL Certificate` 事件 | 证书里意外暴露的内部主机名（如 `jenkins-int.corp`） |
| 供应链暴露 | 关注共享 IP/共享证书的第三方域名 | 关联实体的风险传导 |
| 变更监控 | 定期跑同一目标，**diff 两次 CSV** | 新增子域/开放端口 = 变更告警 |
| 泄露报告 | 把 Finding 导出 | 支撑「需要整改的暴露项」汇报 |

**蓝队的三个硬建议**：

1. **证书是最大的泄露源之一**——签发时用通配符或严格 SAN 列表，别把 `internal-*` 这种名字放进公开证书；
2. **定期自查**：把 SpiderFoot 排进月度任务，比对上次输出，重点关注新增子域；
3. **邮箱泄露要自动化**：接入 HIBP 类 API 定期跑，比人工查快得多。

**关于「被动」的边界**：即便是第三方数据源聚合，**对个人信息（邮箱、人名）的批量处理在《个人信息保护法》下属于处理活动**，企业自查应限定在自有资产与自有员工范围。

---

## 10. 参考

- Kali 工具页（含 `spiderfoot -h` 与 `spiderfoot-cli -h` 原文）：<https://www.kali.org/tools/spiderfoot/>
- 上游官网与文档：<https://www.spiderfoot.net>
- Kali 包跟踪：<https://pkg.kali.org/pkg/spiderfoot>
- 本地命令：`spiderfoot -h`、`spiderfoot -M`、`spiderfoot -T`、`spiderfoot-cli -h`
- 配套教程：[`recon-ng.md`](recon-ng.md)、[`theharvester.md`](theharvester.md)、[`amass.md`](amass.md)、[`nmap.md`](nmap.md)

## ⚠️ 法律与伦理

OSINT 工具让「公开信息」变得**可聚合、可关联**，而聚合后的结论往往**远超出单条公开信息的敏感度**：

- 《个人信息保护法》：**对个人信息的自动化收集、聚合成像属于「处理」行为**，需具备合法性基础；仅因「信息是公开的」不等于可以任意批量处理；
- 《数据安全法》：涉及重要数据和批量数据的处理需合规；
- 《网络安全法》第 27 条：**不得从事非法侵入、干扰他人网络的活动**——`-u investigate` / `-u all` 会主动连接目标，**未经授权即属违规**；
- 《刑法》第 285 条：非法获取计算机信息系统数据。

**必须遵守**：

1. **只对自有资产或获得书面授权的目标**运行 `-u investigate` / `-u all`；
2. 范围不明确时**只用 `-u passive`**，并用 `-x` 把爆炸半径压到最小；
3. **不要**把挖到的凭据、私钥、泄露数据用于登录或访问任何系统；
4. 涉及第三方人员信息时，**最小化收集、限制存储、定期销毁**；
5. 报告脱敏：不公开可直接利用的凭据与内部主机名；
6. 发现泄露应通过**正规漏洞披露流程**告知相关方，而非公开。
