# amass（OWASP 攻击面测绘与资产发现）

> **一句话**：用被动数据源 + 主动探测，把目标组织的域名、子域、IP、ASN 关系挖干净，并存进图数据库方便长期跟踪。
> **分类**：信息搜集 ｜ **Kali 包**：`amass` ｜ **官方文档**：<https://github.com/owasp-amass/amass>

## 1. 它解决什么问题

一次性地把子域列出来不难，难的是**持续跟踪一个组织的攻击面变化**：上周新上了哪个子域？哪个 IP 换了归属？哪家公司其实和目标是同一组织？

amass 是 OWASP 旗舰项目，它把"侦察"从"跑一次命令"变成"维护一份资产图谱"：

- 内置 **40+ 被动数据源**（证书透明度、威胁情报、Web 归档、whois、路由注册库……）。
- 支持**主动技术**：DNS 爆破、NSEC 区域遍历、反向 DNS 扫段、证书名抓取、名称变形猜测。
- 结果写入**图数据库（OAM，Open Asset Model）**，可以按时间点对比（`track`）、按关系查询（`assoc`）、生成图（`viz`）。

| 工具 | 定位 |
|------|------|
| **amass** | 资产图谱 + 长期跟踪 + 关系查询；最"重"也最全 |
| [theHarvester](theharvester.md) | 快，偏向邮箱与人 |
| [dnsrecon](dnsrecon.md) / [dnsenum](dnsenum.md) / [fierce](fierce.md) | 单次 DNS 枚举，轻量 |
| [recon-ng](recon-ng.md) | 框架 + SQL 表，模块可插拔 |

## 2. 工作原理

amass v5 被拆成**子命令 + 收集引擎**两层：

```text
              amass <子命令>
   ┌──────────┬────────┬────────┬────────┬────────┬────────┐
   │  enum    │ engine │  subs  │ assoc  │ track  │  viz   │
   └────┬─────┴────┬───┴────┬───┴────┬───┴────┬───┴────┬───┘
        │          │        │        │        │        │
   启动枚举，   后台常驻  从图库里  按"三元组"  对比历史  生成关系图
   写入 OAM     收集引擎  读子域    做关联查询   找新资产
        │
        ▼
   图数据库（OAM）默认在 ~/.config/amass/ 下的 SQLite/图库
```

**enum 的执行流程**：

```text
 1. 数据源查询阶段（被动，默认）
      并发查询所有已启用的数据源（证书透明度、Shodan、VirusTotal...）
      每个数据源返回一批 name / ASN / CIDR / IP
                    │
 2. 主动技术阶段（可选，按需开启）
      -active   : 真实 DNS 查询、证书名抓取、区域传输
      -brute    : 用字典爆破子域（-w 指定字典，-wm 支持 hashcat 风格掩码）
      -alts     : 名称变形（dev→dev1、dev-test、test-dev...）
      -asn/-cidr/-addr : 直接按 ASN / 网段 / IP 段扩展
                    │
 3. 递归发现
      -max-depth / -min-for-recursive 控制递归深度
                    │
 4. 结果落库 + 输出
      -oA 前缀生成输出文件；数据同时进 OAM 图库
```

## 3. 安装与快速上手

```bash
sudo apt install amass
amass -h
amass enum -h | head -40
```

最小可用命令：

```bash
# 1) 最基础的被动枚举
amass enum -d example.com

# 2) 被动 + 主动 + 输出到文件
amass enum -d example.com -active -oA amass_example

# 3) 枚举后单独查看子域列表
amass subs -d example.com -names
```

## 4. 核心参数详解

### 顶层子命令

| 子命令 | 作用 | 使用建议 |
|--------|------|----------|
| `amass enum` | 执行枚举并写入图库（最常用） | 日常主力 |
| `amass engine` | 启动常驻收集引擎（HTTP 服务，默认 `127.0.0.1:4000`） | 需要多次枚举复用引擎时 |
| `amass subs` | 从图库中读取并按域名展示子域 | 枚举完的"看结果"入口 |
| `amass assoc` | 按"三元组"（实体-关系-实体）在图库里做关联查询 | 关系分析进阶用法 |
| `amass track` | 对比历史枚举，找出新增资产 | 定期巡检 |
| `amass viz` | 生成关系图 | 汇报用 |

### `amass enum` 常用参数

**输入与范围**

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-d <domain>` | 根域名，可逗号分隔或重复多次 | 支持多域 |
| `-df <file>` | 从文件读根域名 | 批量任务 |
| `-asn <n,...>` | 按 ASN 扩展 | 已知目标自持 ASN 时效果极好 |
| `-cidr <cidr,...>` | 按 CIDR 扩展 | 与 ASN 配合 |
| `-addr <ip/range>` | 按 IP 或范围（如 `192.168.1.1-254`）扩展 | 内网/已知段 |
| `-nf <file>` | 提供"已知子域"清单 | 把其他工具结果喂进来省时间 |
| `-exclude <src,...>` | 排除某些数据源 | 某个源老超时时 |
| `-include <src,...>` | 只使用指定数据源 | 精确控制 |
| `-list` | 列出所有可用数据源 | 排查"为什么没结果" |

**主动程度**

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| （默认） | 被动模式 | 默认就是 passive，最安静 |
| `-active` | 尝试区域传输 + 证书名抓取 | 有明确授权时开；会产生真实 DNS 请求 |
| `-brute` | 搜索引擎之后执行字典爆破 | 显著增加请求量 |
| `-w <wordlist>` | 爆破字典 | 用 seclists 的 DNS 字典 |
| `-wm <masks>` | hashcat 风格字典掩码 | 高级爆破 |
| `-alts` | 生成名称变体（`alts` = alternations） | 常能捞到 `-dev`、`-staging` 之类 |
| `-aw <wordlist>` / `-awm <masks>` | 变体生成用的字典/掩码 | 与 `-alts` 配套 |
| `-max-depth <n>` | 爆破的最大子域标签层数 | 别设太大 |
| `-min-for-recursive <n>` | 递归爆破前需见到的标签数（默认 1） | 提高可减少噪声 |
| `-norecursive` | 关闭递归爆破 | 控制时长 |
| `-rigid` | 禁止范围扩展 | 严格限定在给定范围内 |

**数据源与解析器**

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-config <file>` | 指定 YAML 配置（含数据源 API key） | 生产用法；密钥别提交 Git |
| `-dir <dir>` | 输出/图库目录 | 项目隔离 |
| `-oA <prefix>` | 命名所有输出文件的路径前缀 | 推荐 |
| `-tr <ip,...>` | 可信 DNS 解析器 | 用可信解析器避免污染 |
| `-rf <file>` | 从文件读可信解析器 | — |
| `-r <ip,...>` / `-rf` | 不可信解析器（用于暴力解析） | 与 `-tr` 区分开 |
| `-iface <iface>` | 指定网卡 | 多网卡/需要指定源 |
| `-p <ports>` | 主动检测时使用的端口（默认 `80,443`） | — |
| `-timeout <min>` | 无进展超时分钟数（默认 30） | 大任务调大 |
| `-bl <name,...>` / `-blf <file>` | 黑名单子域 / 黑名单文件 | 排除已知无关的大域 |
| `-demo` | 输出脱敏（演示用） | 录屏/演示时用 |
| `-silent` | 关闭进度输出 | 脚本化 |
| `-nocolor` | 关闭颜色 | 重定向到文件 |
| `-v` | 输出状态/调试信息 | 排查 |
| `-log <file>` | 错误写入日志文件 | 长任务留痕 |

### `amass subs` 常用参数

| 参数 | 作用 |
|------|------|
| `-d <domain>` / `-df <file>` | 指定域名 |
| `-dir <dir>` | 图库所在目录（要与 enum 时一致） |
| `-names` | 只打印发现的名字 |
| `-ip` / `-ipv4` / `-ipv6` | 附带显示 IP |
| `-summary` | 只打印 ASN 汇总表 |
| `-show` | 打印指定枚举索引 + 域名的结果 |
| `-o <file>` | 输出到文件 |
| `-silent` / `-nocolor` | 静默 / 无色 |

### `amass track` 常用参数

| 参数 | 作用 |
|------|------|
| `-d <domain>` / `-df <file>` | 域名 |
| `-since "<01/02 15:04:05 2006 MST>"` | 只看该时间之后发现的资产 |
| `-dir <dir>` | 图库目录 |
| `-silent` / `-nocolor` | 静默 / 无色 |

## 5. 实战演练

**环境**：全部使用公开合法目标。`example.com` 为 IANA 保留示例域；也可用你自己的测试域名以获得更丰富的结果。**`-active`、`-brute` 属主动行为，只能在授权范围内使用。**

### 场景 1：纯被动枚举（最安静，适合外部侦察第一步）

```bash
amass enum -d example.com -oA amass_passive
```

预期输出片段（进度行会被实时刷新）：

```text
www.example.com
mail.example.com
[...] 1 names discovered ...
[...] 2 names discovered ...
```

解读：默认被动模式只查第三方数据源，**目标侧完全无感知**。这也是 amass 最适合的第一步——先看看公开渠道已经泄露了多少。

### 场景 2：加入主动技术

```bash
amass enum -d example.com -active -brute -alts \
  -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  -oA amass_active
```

预期输出片段：

```text
[...] Starting the enumeration for example.com
[...] Querying Certificate Transparency (crt.sh)
[...] Querying ... (multiple data sources)
[Cert] www.example.com
[Brute] dev.example.com
[...] 12 names discovered ...
```

解读：
- `-active` 会向目标 DNS 发真实查询，并尝试区域传输与证书名抓取。
- `-brute` 用字典猜名字。
- `-alts` 对已发现名字做变形（`dev` → `dev1`、`staging-dev`），常能捡到漏网之鱼。
- 三者一起用噪声最大，务必确认授权。

### 场景 3：从图库读结果 + 找新增资产

```bash
# 第一次枚举
amass enum -d example.com -dir ~/amass_proj -oA first
amass subs -d example.com -dir ~/amass_proj -names -o subs_1.txt

# 隔一段时间再枚举一次，然后对比
amass enum -d example.com -dir ~/amass_proj -oA second
amass track -d example.com -dir ~/amass_proj

amass subs -d example.com -dir ~/amass_proj -names -o subs_2.txt
diff subs_1.txt subs_2.txt
```

预期输出片段（track）：

```text
[...] New names discovered:
      newapi.example.com
[...] Removed names:
      oldblog.example.com
```

解读：`-dir` 让多次枚举共享同一个图库时，`track` 才能做对比。**新出现的子域是重点排查对象**——新上线的服务往往还没经过安全加固。

### 场景 4：按 ASN / 网段扩展 + 关系查询

```bash
# 已知目标自持 ASN（示例：AS15169 为公开示例），按 ASN 扩展资产
amass enum -asn 15169 -oA by_asn

# 从图库里做关联查询：由域名找出其关联的 IP，再看这些 IP 还关联了哪些域名
amass assoc -dir /tmp/amass_proj -t1 "domain=example.com" -t2 "domain/ip-address=*" \
            -t3 "ip-address/domain=*"
amass assoc -h    # 查看三元组写法
```

解读：`assoc` 用的是"实体-关系-实体"三元组查询。**最实用的模式是"反向找旁站"**：共享同一 IP 的其他域名往往属于同一组织，是横向扩展的入口。三元组语法以 `amass assoc -h` 为准。

## 6. 输出解读

| 输出/前缀 | 含义 | 下一步 |
|-----------|------|--------|
| `[Src] name` 形式的行 | 由某个数据源发现的名字 | 汇总去重 |
| `[...] N names discovered` | 已发现名字计数 | 判断是否收敛 |
| `-oA <prefix>` 生成的文件 | 输出文件集合 | 后续解析/入库 |
| `amass subs -names` | 简洁名字列表 | 直接喂给 httpx |
| `amass track` 的 `New/Removed names` | 与历史对比的变化 | **重点排查新增项** |
| `amass subs -summary` | ASN 汇总 | 判断资产归属 |
| `amass assoc` 结果 | 关系查询结果 | 找旁站/关联组织 |
| 长时间无新名字 | 被动源已穷尽 | 考虑加 `-active`/`-brute`（需授权） |

## 7. 与其他工具配合

```bash
# 1) amass -> httpx -> whatweb 指纹流水线
amass enum -d example.com -oA amass_out
amass subs -d example.com -names | sort -u > subs.txt
httpx -l subs.txt -status-code -title -o live.txt
awk '{print $1}' live.txt | while read -r u; do whatweb -a 1 "$u"; done

# 2) amass -> nmap：先用外部工具解析出 IP 再扫端口
amass subs -d example.com -ip | awk '{print $NF}' | sort -u > ips.txt
sudo nmap -sV -iL ips.txt --open -oA amass_scan

# 3) 其他工具的结果喂给 amass 当"已知子域"
theHarvester -d example.com -b crtsh -f h1
jq -r '.hosts[]' h1.json | cut -d: -f1 > known.txt
amass enum -d example.com -nf known.txt -oA amass_refined

# 4) 证书透明度辅助：amass 的 CT 数据源与 crt.sh 查询互为验证
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| 结果远少于预期 | 未配置数据源 API key | `amass enum -list` 看可用源；在 `-config` 的 YAML 里填 key |
| `-active`/`-brute` 结果为空 | 目标 DNS 屏蔽或解析器不可用 | 指定可信解析器 `-tr 1.1.1.1,8.8.8.8` |
| 大量明显的假名字 | 名称变形过于激进 | 关掉 `-alts`；或用 `-include` 限定高质量源 |
| 任务长时间不结束 | 递归爆破 + 大字典 + 深深度 | `-norecursive`、`-max-depth 2`、换小字典 |
| 结果文件找不到 | 用了 `-dir` 但没记路径 | 统一固定一个 `-dir`，配合 `-oA` 前缀 |
| `track` 没有输出 | 两次枚举图库目录不同 | 两次都必须用同一个 `-dir` |
| 内存/磁盘被吃满 | 图库长期不清理 | 定期清理旧 `-dir`；`-timeout` 限制单次运行 |
| 运行报引擎连接错误 | `-engine` 指向的引擎未启动 | 去掉 `-engine`，或先启动 `amass engine` |
| 数据源限流 / 403 | 无 key 的公共源限速 | 配 key，或 `-exclude <该源>` |

## 9. 防御视角（蓝队）

- **分清被动与主动**（同 recon-ng 的逻辑）：
  - 被动数据源查询（默认行为）**在你这侧完全不可见**。你能做的只有减少"已经被收录"的信息。
  - `-active`（真实 DNS / 区域传输 / 证书抓取）、`-brute`（字典爆破）、反向 DNS 扫段是**可检测的**。
- **可检测的主动行为**：
  - `-brute`：大量 `NXDOMAIN`，同源 IP 高 QPS。递归解析器开 **RRL**，并对 NXDOMAIN 比例设阈值。
  - `-active` 的区域传输尝试：NS 日志里有 `AXFR` 请求记录（即使 REFUSED 也会记）。
  - 证书名抓取：会对 `443` 发起 TLS 连接，边缘设备可记录到"对大量子域做 TLS 握手"的模式。
- **减少被动情报面**：
  - 通配符证书减少 CT 日志条目；内部系统用私有 CA 或自签证书。
  - 避免把内部命名规则（`-dev`、`-staging`、`-test`）暴露在公众可查的记录里。
  - whois 隐私保护开启，减少 `-asn`/路由库推导出的组织关联。
- **资产治理**：amass 的 `track` 思路反过来也是蓝队的工具——**定期自查自己有没有新增的、没人认领的子域**。未认领的子域是子域接管的高危区。

## 10. 参考

- 官方仓库与文档：<https://github.com/owasp-amass/amass>
- 用户指南：<https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md>
- 教程：<https://github.com/owasp-amass/amass/blob/master/doc/tutorial.md>
- OWASP 项目主页：<https://owasp.org/www-project-amass/>
- 用法核实：本教程参数取自 `amass v5.1.1` 的 `amass -h` / `amass enum -h` / `amass subs -h` / `amass track -h` / `amass assoc -h` 实际输出

---

**相关教程**：[theharvester](theharvester.md) ｜ [recon-ng](recon-ng.md) ｜ [dnsrecon](dnsrecon.md) ｜ [dnsenum](dnsenum.md) ｜ [fierce](fierce.md) ｜ [nmap](nmap.md)
