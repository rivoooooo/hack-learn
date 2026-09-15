# recon-ng（模块化 Web 侦察框架）

> **一句话**：像 Metasploit 那样用"模块 + 数据库 + 工作区"的方式组织开源情报侦察，结果自动入库、可跨模块流转。
> **分类**：信息搜集 ｜ **Kali 包**：`recon-ng` ｜ **官方文档**：<https://github.com/lanmaster53/recon-ng>

## 1. 它解决什么问题

单点工具的问题在于**结果不互通**：[theHarvester](theharvester.md) 给你一个子域列表，[dnsrecon](dnsrecon.md) 给你一堆 A 记录，[whatweb](whatweb.md) 给你指纹——但你要手工把它们串起来。

recon-ng 提供的是**统一数据模型**：`domains`、`hosts`、`contacts`、`credentials`、`ports`、`vulnerabilities` 等表。任何一个模块把数据写进表里，后续模块就能直接读这张表作为输入。

```text
   模块 A（找子域）  ──写──►  hosts 表  ──读──►  模块 B（解析 IP）
                              │
                              ├──► 模块 C（反查 hosts）
                              └──► 模块 D（证书 SAN 扩展）
```

| 工具 | 定位 |
|------|------|
| **recon-ng** | 框架，模块可插拔、数据可复用、工作区可隔离 |
| [theHarvester](theharvester.md) | 单一命令，快速拿邮箱/子域 |
| [amass](amass.md) | 专精 DNS/资产图谱 |
| [Maltego](https://www.maltego.com/) | 图形化关系分析（recon-ng 的"可视化"竞品） |

**核心设计**：recon-ng **只做侦察，不做利用**。要打漏洞去 Metasploit，要做社工去 SET。

## 2. 工作原理

```text
   recon-ng -w pentest1
        │
        ├── 工作区（workspace）= 一个独立 SQLite 库
        │     ~/.recon-ng/workspaces/pentest1/data.db
        │
        ├── 模块仓库
        │     内置：<安装目录>/modules/
        │     用户：~/.recon-ng/modules/
        │
        └── 交互式 Shell（readline + Tab 补全）
              │
     ┌────────┴────────┐
     │ 全局模式         │  workspaces / show modules / keys / spool ...
     │ 模块模式         │  use <模块>；set SOURCE ...；run
     └────────┬────────┘
              │
        模块执行流程（以 recon/domains-hosts/hackertarget 为例）
              │
     1. 读 options 里的 SOURCE（域名）
     2. 调用外部 API 拿到子域/IP 列表
     3. 去重后 INSERT 到 hosts / domains 表
     4. 打印 "N rows added"
```

模块命名规则 `类别-输入类型-输出类型/名称`，读法很直观：

- `recon/domains-hosts/hackertarget`：侦察类，输入 `domains`，输出 `hosts`。
- `recon/hosts-hosts/resolve`：输入 `hosts`，输出 `hosts`（解析成 IP）。
- `recon/domains-contacts/whois_pocs`：输入 `domains`，输出 `contacts`（whois 联系人）。

所以典型用法就是"顺着 输入→输出 类型把模块串起来"。

## 3. 安装与快速上手

```bash
sudo apt install recon-ng
recon-ng -h
```

最小可用会话：

```bash
recon-ng -w demo          # -w 指定工作区，不存在则创建
```

会话内：

```text
[recon-ng][default] > workspaces list
[recon-ng][default] > show modules
[recon-ng][default] > use recon/domains-hosts/hackertarget
[recon-ng][default][hackertarget] > set SOURCE example.com
SOURCE => example.com
[recon-ng][default][hackertarget] > run
```

批处理（无交互）：

```bash
recon-ng -w demo -r script.rc      # -r 从资源文件读取命令
```

## 4. 核心参数详解

### 命令行参数

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-w <workspace>` | 加载/创建工作区 | 一个项目一个工作区，别混 |
| `-r <filename>` | 从资源文件执行命令后退出 | CI/批量任务 |
| `--no-version` | 关闭版本检查 | Debian/Kali 下默认已关闭 |
| `--no-analytics` | 关闭分析上报 | Kali 下默认已关闭 |
| `--no-marketplace` | 禁用远程模块管理 | 离线环境 |
| `--stealth` | 禁用所有被动请求 | **注意**：man page 描述为"禁用所有被动请求"，谨慎理解其语义 |
| `-v, --version` | 显示版本 | — |
| `-h, --help` | 帮助 | — |

### 全局模式命令

| 命令 | 作用 | 使用建议 |
|------|------|----------|
| `workspaces list` | 列出所有工作区 | 开局先看 |
| `workspaces create <name>` / `workspaces select <name>` / `workspaces remove <name>` | 增删选工作区 | 也可用启动参数 `-w` |
| `show modules` | 列出可用模块（可加前缀过滤，如 `show modules recon/domains-hosts`） | 找模块的第一步 |
| `show schema` | 显示数据库表结构 | 写模块/写 SQL 前必看 |
| `show dashboard` | 各表记录数概览 | 判断当前进度 |
| `show tables` 类查询 | 直接 `show <表名>` 列出表内容 | 等价于 `query` |
| `keys list` / `keys add <name> <value>` | 管理 API 密钥 | 密钥存在工作区库里，不要提交 Git |
| `query <SQL>` | 直接对工作区 SQLite 执行 SQL | 灵活提取数据 |
| `add <table> ...` / `delete <table> ...` | 手工增删记录 | 导入外部数据 |
| `search <regex>` | 在所有表中搜索 | 找某个域名出现过哪些地方 |
| `spool start <file>` / `spool stop` | 把输出同时写到文件 | 留档 |
| `record start <file>` / `record stop` | 记录你输入的命令到资源文件 | **做完一次手工流程后用它生成 `.rc`** |
| `resource <file>` | 执行资源文件 | 与命令行 `-r` 等价 |
| `shell <cmd>` | 执行系统命令 | 不离开 recon-ng 打外部命令 |
| `load <module>` / `use <module>` | 加载模块 | 两者等价（`do_use = do_load`） |
| `back` | 从模块模式返回全局 | — |
| `exit` | 退出 | — |

### 模块模式命令

| 命令 | 作用 | 使用建议 |
|------|------|----------|
| `show options` | 显示模块参数、是否必填、是否已设置 | 每次 `use` 后第一件事 |
| `show info` | 模块说明、作者、数据源 | 判断是否值得跑 |
| `show inputs` / `show source` | 模块源码 | 看清它到底发什么请求 |
| `show globals` | 全局参数 | — |
| `set <OPTION> <value>` | 设置参数（`set` 也可设全局项） | `SOURCE` 是域名类模块的入口 |
| `unset <OPTION>` | 清除参数 | — |
| `run` | 执行模块 | — |

### 常用模块（Kali 内置，已核实）

| 模块 | 输入→输出 | 用途 |
|------|-----------|------|
| `recon/domains-hosts/hackertarget` | domains→hosts | 免 key，从 HackerTarget 拿子域 |
| `recon/domains-hosts/brute_hosts` | domains→hosts | 字典爆破子域 |
| `recon/domains-hosts/certificate_transparency` | domains→hosts | 证书透明度日志挖子域 |
| `recon/domains-hosts/ssl_san` | domains→hosts | 从 TLS 证书 SAN 扩子域 |
| `recon/domains-hosts/google_site_web` | domains→hosts | Google `site:` 抓子域 |
| `recon/domains-hosts/bing_domain_web` | domains→hosts | Bing 抓子域 |
| `recon/domains-hosts/netcraft` | domains→hosts | Netcraft 主机搜索 |
| `recon/domains-hosts/mx_spf_ip` | domains→hosts | 从 MX/SPF 记录推导主机 |
| `recon/domains-hosts/threatcrowd` | domains→hosts | ThreatCrowd |
| `recon/domains-hosts/shodan_hostname` | domains→hosts | Shodan 主机名（需 key） |
| `recon/hosts-hosts/resolve` | hosts→hosts | 把主机名解析成 IP |
| `recon/hosts-hosts/reverse_resolve` | hosts→hosts | 对 IP 做 PTR 反查 |
| `recon/hosts-hosts/freegeoip` / `ipinfodb` | hosts→hosts | IP 地理/归属 |
| `recon/hosts-ports/shodan_ip` | hosts→ports | Shodan 端口信息（需 key） |
| `recon/domains-contacts/whois_pocs` | domains→contacts | whois 联系人 |
| `recon/domains-contacts/pgp_search` | domains→contacts | PGP 公钥库找邮箱 |
| `recon/domains-contacts/metacrawler` | domains→contacts | 元数据爬取邮箱 |
| `recon/domains-vulnerabilities/ghdb` | domains→vulnerabilities | Google Hacking 数据库匹配 |
| `recon/companies-multi/whois_miner` | companies→companies | whois 挖关联公司 |
| `recon/companies-multi/github_miner` | companies→... | GitHub 挖组织/成员 |
| `recon/contacts-credentials/hibp_breach` | contacts→credentials | HaveIBeenPwned 泄露查询 |
| `discovery/info_disclosure/interesting_files` | — | 探测常见敏感文件 |
| `discovery/info_disclosure/cache_snoop` | — | DNS 缓存窥探 |
| `import/csv_file` / `import/list` | 文件→表 | 把外部清单导入工作区 |

> 模块名格式为 `<类别>/<输入>-<输出>/<名称>`；用 `show modules` 能看到当前工作区实际可用的完整列表。除内置模块外，还可以把第三方模块放到 `~/.recon-ng/modules/` 下加载。

## 5. 实战演练

**环境**：全部使用公开合法资源。`example.com` 是 IANA 保留示例域；若想有"真实感"，可用你自己注册的测试域名。**不要对未授权域名跑爆破类模块。**

### 场景 1：第一个工作区——拿子域并入库

```bash
recon-ng -w lab
```

```text
[recon-ng][lab] > show modules
[recon-ng][lab] > use recon/domains-hosts/hackertarget
[recon-ng][lab][hackertarget] > show options

  Name    Current Value  Required  Description
  ------  -------------  --------  -----------
  SOURCE                 yes       source of input (see 'show info' for details)

[recon-ng][lab][hackertarget] > set SOURCE example.com
SOURCE => example.com
[recon-ng][lab][hackertarget] > run

[*] [host] www.example.com (93.184.216.34)
[*] 1 total (1 new) hosts found.
[recon-ng][lab][hackertarget] > back
[recon-ng][lab] > show hosts

  rowid  host            ip_address     region  country  latitude  longitude  module
  -----  --------------  -------------  ------  -------  --------  ---------  -------------
  1      www.example.com  93.184.216.34                                  hackertarget
```

解读：这是 recon-ng 的"Hello World"。注意 `module` 列记录了数据来源，方便回溯是谁写进来的。

### 场景 2：串起"域名 → 子域 → IP → 反查"流水线

```text
[recon-ng][lab] > use recon/domains-hosts/certificate_transparency
[recon-ng][lab][certificate_transparency] > set SOURCE example.com
[recon-ng][lab][certificate_transparency] > run
[recon-ng][lab][certificate_transparency] > back

[recon-ng][lab] > use recon/hosts-hosts/resolve
[recon-ng][lab][resolve] > run
[*] [host] www.example.com => 93.184.216.34
[*] 1 total (0 new) hosts found.

[recon-ng][lab][resolve] > back
[recon-ng][lab] > use recon/hosts-hosts/reverse_resolve
[recon-ng][lab][reverse_resolve] > run
[recon-ng][lab][reverse_resolve] > back

[recon-ng][lab] > show dashboard
[recon-ng][lab] > query SELECT host, ip_address FROM hosts WHERE ip_address IS NOT NULL
```

预期输出片段：

```text
  host                 ip_address
  -------------------  -------------
  www.example.com      93.184.216.34
  1 rows returned
```

解读：`resolve` 与 `reverse_resolve` 不需要设置 `SOURCE`——它们**自动读取 `hosts` 表**。这正是框架的价值：数据在表里，模块之间自动衔接。

### 场景 3：用资源文件做可重复的自动化流程

先用 `record` 把手工过程录下来：

```text
[recon-ng][lab] > record start osint.rc
[recon-ng][lab] > use recon/domains-hosts/hackertarget
[recon-ng][lab][hackertarget] > set SOURCE example.com
[recon-ng][lab][hackertarget] > run
[recon-ng][lab][hackertarget] > back
[recon-ng][lab] > record stop
```

生成的 `osint.rc` 内容形如：

```text
use recon/domains-hosts/hackertarget
set SOURCE example.com
run
back
```

之后可以一条命令跑完整流程：

```bash
recon-ng -w lab2 -r osint.rc
```

解读：`record` 是 recon-ng 里最被低估的功能——**手工调通一次，自动重跑无数次**。CI 或定期资产巡检就靠它。

### 场景 4（进阶）：配置 API 密钥 + SQL 精炼结果

```text
[recon-ng][lab] > keys add shodan_api <YOUR_KEY>
[recon-ng][lab] > keys list

[recon-ng][lab] > use recon/hosts-ports/shodan_ip
[recon-ng][lab][shodan_ip] > run
[recon-ng][lab][shodan_ip] > back

[recon-ng][lab] > query SELECT host, ip_address, port, banner FROM ports ORDER BY host
[recon-ng][lab] > spool start lab_report.txt
[recon-ng][lab] > show dashboard
[recon-ng][lab] > spool stop
```

解读：密钥用 `keys add` 存进工作区数据库（**不要写进脚本提交到 Git**）。`query` 让你直接用 SQL 拿到任意视图；`spool` 把会话输出留档。查到的端口后续可以直接喂给 [nmap](nmap.md) 复核。

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `[recon-ng][<工作区>] >` | 全局模式提示符 | — |
| `[recon-ng][<工作区>][<模块>] >` | 已在模块模式 | `set` 后 `run` |
| `[*] [host] ... (ip)` | 模块写入一条 host 记录 | 继续跑下游模块 |
| `N total (M new)` | 共 N 条，其中 M 条是新入库的 | M=0 说明数据源与前序模块重叠 |
| `[!] Invalid ...` | 参数/输入不合法 | `show options` 检查必填项 |
| `N rows returned` | `query`/`show` 的结果行数 | — |
| `show dashboard` 各表计数 | 当前情报总量 | 判断还缺哪类数据 |
| `[!] Key not found` | 缺 API 密钥 | `keys add` |

把结果变成动作：

```text
show hosts            → 挑出有 IP 的记录 → nmap -sV 扫端口
show contacts         → 邮箱/人员清单 → 社工范围评估（授权内）
show vulnerabilities  → GHDB 命中的敏感 URL → 手工复核
```

## 7. 与其他工具配合

```bash
# 1) recon-ng 导出 -> nmap 扫端口
#   会话内：
#   [recon-ng][lab] > query SELECT DISTINCT ip_address FROM hosts WHERE ip_address IS NOT NULL
#   或直接用 sqlite3 读工作区库：
sqlite3 ~/.recon-ng/workspaces/lab/data.db \
  "SELECT DISTINCT ip_address FROM hosts WHERE ip_address IS NOT NULL;" > ips.txt
sudo nmap -sV -iL ips.txt --open -oA recon_ng_scan

# 2) 外部清单导入 recon-ng
#   会话内：
#   [recon-ng][lab] > use import/list
#   [recon-ng][lab][list] > set SOURCE /tmp/subs.txt
#   [recon-ng][lab][list] > run

# 3) recon-ng 结果 -> httpx/whatweb
sqlite3 ~/.recon-ng/workspaces/lab/data.db "SELECT DISTINCT host FROM hosts;" | \
  sed 's/^/https:\/\//' > urls.txt
httpx -l urls.txt -title -status-code -o live.txt

# 4) 与 theHarvester 互补：先 theHarvester 拿邮箱，再导入 recon-ng 做关联
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `show modules` 列表很短 | 用户模块目录为空（Kali 只内置一部分） | 内置模块已够用；第三方模块放到 `~/.recon-ng/modules/` |
| `run` 报 `SOURCE is required` | 模块需要输入但未设置 | `show options` 看到 `Required: yes` 的项，逐个 `set` |
| `[*] 0 total (0 new) hosts found` | 数据源限制了该域，或数据已在库里 | 换模块（如 `certificate_transparency`）；先 `show dashboard` 看是否已有 |
| `[!] Key ... not found` | 模块需要 API key | `keys add <name> <value>`；`keys list` 确认 |
| 模块跑完但 `show hosts` 为空 | 模块输出到别的表（如 `contacts`/`ports`） | 看 `show info`，或直接 `show dashboard` |
| 换了工作区却发现数据"丢了" | 每个工作区是独立 SQLite 文件 | `workspaces list` 确认当前工作区名 |
| 工作区数据库损坏 | 并发写 / 异常退出 | 备份 `~/.recon-ng/workspaces/<name>/data.db` 后重建 |
| Tab 补全不工作 | 缺少 `readline` | `sudo apt install python3-readline`（多数系统自带） |
| 爆破类模块把目标惹毛了 | `brute_hosts` 是**主动**行为 | 明确授权后再用；优先用被动模块 |
| 密钥被提交到 Git | 密钥存在工作区库里但脚本里常明文 | `.gitignore` 排除工作区目录与 `.rc` 文件 |

## 9. 防御视角（蓝队）

- **区分被动与主动模块**（关键！）：
  - **被动**（无法从网络侧检测）：`hackertarget`、`certificate_transparency`、`netcraft`、`threatcrowd`、`whois_pocs`、`pgp_search`。它们查第三方数据库，你的日志里什么都没有。
  - **主动**（可检测）：`brute_hosts`、`resolve`（DNS 查询）、`reverse_resolve`（PTR 查询）、`interesting_files`（HTTP 探测）、`cache_snoop`（DNS 缓存窥探）。
  - **防守重点放在"减少被动源里的信息量"**，而不是指望检测查询。
- **可检测的主动行为与对应日志**：
  - `brute_hosts` → 递归解析器上大量 `NXDOMAIN`，配 RRL + NXDOMAIN 速率告警。
  - `reverse_resolve` → 顺序的 `in-addr.arpa` PTR 查询。
  - `interesting_files` → Web 日志里对 `/.git/`、`/.env`、`/backup.zip` 等的 404 扫描，WAF 规则可直接覆盖。
  - `cache_snoop` → 对同一解析器的非递归查询模式异常。
- **减少情报面**：
  - 用通配符证书，减少 CT 日志中的名称数量。
  - 内部系统不要签发公众信任证书，或使用私有 CA。
  - PGP 公钥里的邮箱是 `pgp_search` 的直接输入——建议用角色邮箱。
  - whois 联系人信息按隐私条例做脱敏（GDPR 下多数注册商已默认隐藏）。
- **响应建议**：把 recon-ng 的模块行为映射成检测规则清单，定期在演练中验证规则是否触发。

## 10. 参考

- 官方仓库：<https://github.com/lanmaster53/recon-ng>
- 官方 Wiki（Usage Guide，模块与命令详解）：<https://github.com/lanmaster53/recon-ng/wiki>
- man page：`man recon-ng`（覆盖命令行参数；交互命令见 Wiki）

---

**相关教程**：[theharvester](theharvester.md) ｜ [amass](amass.md) ｜ [dnsrecon](dnsrecon.md) ｜ [dnsenum](dnsenum.md) ｜ [fierce](fierce.md) ｜ [nmap](nmap.md)
