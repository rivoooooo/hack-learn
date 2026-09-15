# theHarvester（OSINT 收集：邮箱、子域、主机与员工信息）

> **一句话**：从公开数据源（搜索引擎、证书透明度、威胁情报平台、PGP 服务器）批量收集一个组织的邮箱地址、子域名、主机和相关人员信息。
> **分类**：信息搜集 ｜ **Kali 包**：`theharvester`（命令名 `theHarvester`） ｜ **官方文档**：<https://github.com/laramies/theHarvester>

## 1. 它解决什么问题

渗透测试的"侦察"阶段有三条线：技术资产（子域、IP、端口）、**人员资产**（邮箱、员工姓名、职位）、凭据泄露线索。theHarvester 用一条命令同时触及这三条线，而且默认是**被动**的——大部分数据源只是查询第三方数据库，不向目标发出任何请求。

| 工具 | 侧重 | 数据性质 |
|------|------|----------|
| **theHarvester** | 邮箱 / 员工 / 子域 / 主机，多数据源聚合 | 以被动为主，可开主动 DNS 爆破 |
| [amass](amass.md) | 攻击面测绘，图谱数据库，长期跟踪 | 被动 + 主动爆破 |
| [dnsrecon](dnsrecon.md) / [fierce](fierce.md) | 纯 DNS 层枚举 | 主动 |
| [recon-ng](recon-ng.md) | 模块化框架，可写自己的模块 | 混合 |

关键差异：**theHarvester 是唯一把"人"和"邮箱"作为一等公民的工具**。它直接服务于后续的钓鱼演练、口令喷洒（password spraying）和社工话术设计。

## 2. 工作原理

```text
        theHarvester -d example.com -b duckduckgo,crtsh,otx,urlscan -l 300
                              │
        ┌─────────────────────┴──────────────────────┐
        │           按 -b 选择数据源（并发）           │
        ├────────────────────────────────────────────┤
        │ 搜索引擎类 : duckduckgo, yahoo, brave, mojeek│
        │ 证书透明度 : crtsh, certspotter             │
        │ 情报平台   : shodan, censys, fofa, netlas,  │
        │              zoomeye, hunter, intelx, otx   │
        │ 攻击面平台 : securityTrails, subdomaincenter│
        │ 泄露/人员  : dehashed, haveibeenpwned,      │
        │              hunter, rocketreach, tomba     │
        │ 归档/代码  : waybackarchive, github-code,   │
        │              gitlab, commoncrawl            │
        └─────────────────────┬──────────────────────┘
                              │
                 去重 → 分类（emails / hosts / ips）
                              │
        ┌─────────────────────┴──────────────────────┐
        │ 可选主动阶段：                                │
        │   -c  DNS 爆破     -n  PTR 反查 /24          │
        │   -r  批量解析     -t  子域接管检测          │
        │   -a  API 端点扫描 --screenshot 截图         │
        └─────────────────────┬──────────────────────┘
                              │
                     -f name → name.json / name.xml / name.jsonl
```

要点：

- **大部分源需要 API Key**。密钥放在 `api-keys.yaml`（或 `~/.theHarvester/api-keys.yaml`），`-q` 可以静默缺 key 的警告。没有 key 时，能用的主要是不需要认证的搜索/证书/归档类源。
- **`-b` 是逗号分隔的源列表**，可用值在 `--source` 的 help 里完整列出（见下）。
- **主动阶段是可选开关**，默认不发请求到目标；一旦加了 `-c`/`-n`/`-r`，就会向目标 DNS 发查询，属于主动行为。

## 3. 安装与快速上手

```bash
sudo apt install theharvester
theHarvester --help | head -30
# 注意命令名是大写 H 开头的 theHarvester
```

最小可用命令：

```bash
# 1) 最基础：只用一个被动源
theHarvester -d example.com -b crtsh

# 2) 多个被动源 + 限制结果数
theHarvester -d example.com -b duckduckgo,crtsh,otx,urlscan -l 300

# 3) 被动 + 主动 DNS 解析 + 保存结果
theHarvester -d example.com -b crtsh,duckduckgo -r -f harvest_demo
```

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-d, --domain` | 要搜索的公司名或域名（必填） | 支持域名、公司名，或在 `--routeviews` 下的 ASN/IP/CIDR |
| `-b, --source` | 数据源列表（逗号分隔） | 见下方"常用数据源" |
| `-l, --limit` | 每个源最多取多少条结果（默认 500） | 0 表示不限；调小可加快速度 |
| `-S, --start` | 结果分页起始偏移（默认 0） | 分批抓取时用 |
| `-r, --dns-resolve` | 解析发现的主机名，可传解析器列表或文件 | 需要"确认存活"时加 |
| `-n, --dns-lookup` | 对发现 IPv4 所在的 /24 做 PTR 反查 | 主动行为；会显著增加请求量 |
| `-c, --dns-brute` | 对域做 DNS 爆破 | 主动行为；需要有可用 wordlist |
| `-w, --wordlist` | 给 `--api-scan` 用的端点字典 | 与 `-a` 配套 |
| `-a, --api-scan` | 扫描 API 端点 | 高级用法，可能需要 key |
| `-t, --take-over` | 检测发现的子域是否存在"子域接管"迹象 | 高危发现的快速筛查 |
| `-e, --dns-server` | 指定 DNS 服务器 | 内网/指定解析器场景 |
| `-p, --proxies` | 使用 `proxies.yaml` 中的代理 | 需要隐藏来源或绕过地域限制 |
| `-s, --shodan` | 对发现的 IP 查询 Shodan | 需要 API key |
| `--screenshot <dir>` | 对可访问主机截图 | 会**直接**用浏览器访问目标，属主动行为 |
| `-f, --filename` | 结果写为 `NAME.json` / `NAME.xml` / `NAME.jsonl` | 强烈建议加 |
| `-q, --quiet` | 不提示缺失的 API key | 脚本化运行时加 |

**常用数据源**（`-b` 可取值，完整列表见 `--help`）：

| 类别 | 示例值 | 是否需要 key |
|------|--------|--------------|
| 搜索引擎 | `duckduckgo`、`yahoo`、`mojeek`、`brave`、`baidu` | 多数不需要 |
| 证书透明度 | `crtsh`、`certspotter` | 不需要 |
| 威胁情报 | `otx`、`urlscan`、`hackertarget`、`rapiddns` | `urlscan` 建议有 key |
| 商业平台 | `shodan`、`censys`、`fofa`、`zoomeye`、`netlas`、`securityTrails`、`virustotal` | 需要 |
| 人员/泄露 | `hunter`、`rocketreach`、`tomba`、`dehashed`、`haveibeenpwned` | 需要 |
| 归档/代码 | `waybackarchive`、`commoncrawl`、`github-code`、`gitlab` | GitHub 需 token 才稳定 |

## 5. 实战演练

**环境**：`example.com` 是 IANA 保留示例域，可安全用于演示；无 key 时只用被动源，不会向目标发任何包。若要加强演练效果，可对自己注册的测试域名操作（例如你自己买的一个便宜域名）。

### 场景 1：只用免 key 的被动源做最小侦察

```bash
theHarvester -d example.com -b crtsh,duckduckgo,otx,urlscan -l 200
```

预期输出片段：

```text
*******************************************************************
*  _   _                                            _             *
* | |_| |__   ___    /\  /\__ _ _ ____   _____  ___| |_ ___ _ __  *
...
[*] Target: example.com

[*] Searching crtsh.

[*] Hosts found: 12
---------------------
www.example.com:93.184.216.34
...

[*] No emails found.
```

解读：`crtsh` 从证书透明度日志里反查主机名，往往一次就能给出比字典爆破更多的子域，而且**完全不接触目标**。`No emails found` 很正常——被动源能拿到邮箱的前提是有公开页面暴露。

### 场景 2：被动 + 主动解析，输出结构化结果

```bash
theHarvester -d example.com -b crtsh,duckduckgo,hackertarget,rapiddns \
             -l 300 -r -f harvest_example
ls -l harvest_example.*
```

预期输出片段：

```text
[*] Searching hackertarget.
[*] Searching rapiddns.

[*] Hosts found: 42
---------------------
...

[*] IPs found: 8
------------------

[*] Emails found: 0
-------------------

[*] Interesting Urls found: 3
----------------------------
https://example.com/.well-known/security.txt
```

解读：`-r` 会把主机名解析成 IP（主动 DNS 查询），`-f harvest_example` 生成 `harvest_example.json`、`.xml`、`.jsonl`。JSON 里的 `hosts` / `ips` / `emails` 三类数组可以直接喂给后续脚本。

### 场景 3：带 API key 的深度收集（需要自行申请 key）

先把 key 写进配置文件（不要提交到 Git）：

```yaml
# ~/.theHarvester/api-keys.yaml
shodan:
  - YOUR_SHODAN_KEY
hunter:
  - YOUR_HUNTER_KEY
censys:
  id: YOUR_CENSYS_ID
  secret: YOUR_CENSYS_SECRET
```

```bash
theHarvester -d your-test-domain.example -b shodan,hunter,securityTrails,censys \
             -l 500 -s -f deep_osint
```

预期输出片段：

```text
[*] Emails found: 27
--------------------
admin@your-test-domain.example
sales@your-test-domain.example
...

[*] People found: 14
--------------------
Zhang San - CTO
Li Si - IT Manager
```

解读：邮箱 + 人员 + 职位是社工与钓鱼演练的输入。**在授权范围内使用**——对真实组织收集个人邮箱属于隐私敏感操作，必须有书面授权和明确的用途说明。

### 场景 4：子域接管快速筛查（被动发现 + 主动确认）

```bash
theHarvester -d example.com -b crtsh -t -f takeover_check
```

预期输出片段：

```text
[*] Checking for subdomain takeovers
[-] No takeover indicators found.
```

解读：`-t` 不跟随重定向，只检查"供应商门控"特征（比如页面提示 `NoSuchBucket`、`Heroku | No such app`）。**这只是指示，不是确认**——命中后必须人工复核 CNAME 链与供应商控制权。

## 6. 输出解读

| 输出区块 | 含义 | 下一步 |
|----------|------|--------|
| `[*] Searching <source>` | 正在查询某个源 | — |
| `Hosts found` | 子域/主机名清单 | 解析后交给 httpx / whatweb |
| `IPs found` | 解析出的 IP | 去重后 nmap 扫端口 |
| `Emails found` | 邮箱地址 | 交给社工/钓鱼演练范围评估 |
| `People found` | 姓名 + 职位 | 社工话术设计（授权内） |
| `Interesting Urls` | 有信息价值的 URL | 手工打开看 |
| `No emails found` | 该源无结果 | 换 `hunter`/`hunterhow` 等专门源 |
| `API key not found` 警告 | 缺少该源密钥 | 配 `api-keys.yaml`，或 `-q` 静音 |

`-f NAME` 的输出结构（JSON）：

```json
{
  "hosts": ["www.example.com:93.184.216.34"],
  "ips": ["93.184.216.34"],
  "emails": []
}
```

## 7. 与其他工具配合

```bash
# 1) theHarvester -> httpx -> whatweb：子域指纹流水线
theHarvester -d example.com -b crtsh -f h1
jq -r '.hosts[]' h1.json | cut -d: -f1 | sort -u > subs.txt
httpx -l subs.txt -o live.txt -status-code -title
while read -r line; do whatweb -a 1 "$line"; done < live.txt

# 2) theHarvester IP -> nmap
jq -r '.ips[]' h1.json | sort -u > ips.txt
sudo nmap -sV -iL ips.txt --open -oA osint_scan

# 3) 把邮箱清单交给钓鱼演练平台（授权内）
jq -r '.emails[]' h1.json | sort -u > targets_email.txt

# 4) 与 amass 互补：theHarvester 管人，amass 管子域图谱
amass enum -d example.com -o amass_subs.txt
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| 命令找不到 | 写成小写 `theharvester` | Kali 里命令名是 `theHarvester`（大写 H） |
| 大量 `Missing API key` | 多数源需要密钥 | 配置 `~/.theHarvester/api-keys.yaml`，或 `-q` 静音 |
| 某个源一直无结果 | 源已下线 / 改了 API / 被限速 | 换 `crtsh`、`hackertarget`、`rapiddns` 等免 key 源 |
| `-r` 后结果为空 | 解析器不可达或被限速 | 加 `-e 1.1.1.1` 或 `--dns-resolvers` |
| 输出重复项很多 | 多源叠加 | 用 `jq` / `sort -u` 去重 |
| Shodan 报配额耗尽 | 免费 key 额度小 | 降低 `-l`，或换 `shodanInternetDB`（免 key） |
| `--screenshot` 触发了目标告警 | 该参数会真实访问目标 | 明确授权后用；平时别开 |
| 结果文件互相覆盖 | `-f` 同名会覆盖 | 用带时间戳的文件名 |
| 搜索源返回 403 | 搜索引擎反爬 | 配置 `-p proxies.yaml` 代理 |

## 9. 防御视角（蓝队）

- **被动源无法从网络侧检测**：`crtsh`、`securityTrails`、`shodan` 查的是第三方数据库，你的 WAF/IDS 什么都看不到。这是 OSINT 的本质——**要防的是"信息本身存在"，而不是"有人来查"**。
- **减少可被收集的信息**：
  - 邮箱：用别名/角色邮箱（`support@`）替代个人邮箱；避免在官网、GitHub commit、招聘页暴露员工姓名+邮箱组合。
  - 子域：使用**通配符证书**减少证书透明度日志里的名称数量；对内部系统不要签发公众信任证书。
  - 人员：LinkedIn 等平台上的组织架构是社工的最大情报源，这属于管理措施范畴。
- **可检测的主动行为**：
  - `-c` DNS 爆破 → 大量 `NXDOMAIN`，用递归解析器的 RRL + NXDOMAIN 速率告警。
  - `-n` /24 反查 → 顺序的 `in-addr.arpa` PTR 查询模式。
  - `--screenshot` → 目标 Web 日志里出现无 Referer、短停留的浏览器请求。
  - 这些可以在 DNS 日志和 Web 日志里做关联告警。
- **子域接管的防守**：定期自查所有 CNAME 指向的外部服务是否仍被自己控制；把不再使用的子域及时从 DNS 删除。

## 10. 参考

- 官方仓库：<https://github.com/laramies/theHarvester>
- Wiki（数据源与 API key 配置）：<https://github.com/laramies/theHarvester/wiki>
- 证书透明度查询：<https://crt.sh/>
- man page：`man theHarvester`（Kali 包未附带 man page，可用 `theHarvester --help`）

---

**相关教程**：[recon-ng](recon-ng.md) ｜ [amass](amass.md) ｜ [dnsrecon](dnsrecon.md) ｜ [dnsenum](dnsenum.md) ｜ [fierce](fierce.md) ｜ [whatweb](whatweb.md)
