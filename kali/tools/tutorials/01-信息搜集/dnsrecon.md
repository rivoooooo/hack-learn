# dnsrecon（DNS 枚举与域传输检测）

> **一句话**：围绕一个域名，把能问 DNS 拿到的情报（NS/A/MX/SRV/TXT/PTR）一次性问完，并顺带测区域传输、子域爆破、缓存窥探。
> **分类**：信息搜集 ｜ **Kali 包**：`dnsrecon` ｜ **官方文档**：<https://github.com/darkoperator/dnsrecon>

## 1. 它解决什么问题

拿到一个域名之后，"外部资产面"几乎全是 DNS 问题：这个域有哪些名称服务器？邮件走哪里？有没有可直接拉取的区域文件（AXFR）？有没有一些没被链接出来的子域？

同类工具的分工：

| 工具 | 特点 | 何时用 |
|------|------|--------|
| **dnsrecon** | 枚举类型最全（std/rvl/brt/srv/axfr/zonesnoop/tld/zonewalk/crt…），可存 SQLite/JSON/CSV | 想要"一次跑完常见检查" |
| [dnsenum](dnsenum.md) | Perl 实现，侧重 AXFR + 谷歌抓取 + whois 反查网段 | 需要顺带发现**不连续的 IP 段** |
| [fierce](fierce.md) | 轻量，专做"非连续 IP 空间"发现 | 目标域名较小时快速摸底 |
| [amass](amass.md) | OWASP 项目，被动数据源 + 主动爆破 + 图谱数据库 | 需要长期跟踪资产面变化 |
| [theharvester](theharvester.md) | 面向 OSINT（邮箱、员工、子域） | 社会工程学前的信息收集 |

## 2. 工作原理

dnsrecon 是一堆 DNS 查询策略的集合，按 `-t TYPE` 选择具体策略：

```text
                    目标域名 example.com
                            │
   ┌────────────────────────┼────────────────────────┐
   │                        │                        │
 [被动/标准]             [主动探测]                [旁路数据源]
 std: NS/SOA/A/AAAA      axfr: 对每个 NS 发 AXFR    crt: 查 crt.sh 证书透明度
 mx, SRV 枚举            brt: 用字典猜子域           bing/yand: 搜索引擎抓取
 caa, txt                 rvl: 对 IP 段反查 PTR      snoop: DNS 缓存窥探
 zonewalk: DNSSEC NSEC 链式遍历                    tld: 换 TLD 再试
   │                        │                        │
   └────────────────────────┴────────────────────────┘
                            │
                  去重 / 过滤 wildcard
                            │
              SQLite / XML / CSV / JSON 落地
```

几个关键机制：

- **区域传输（AXFR）**：DNS 主从同步用的完整区域文件传输。若配置不当，任何客户端都能把整个域的记录一次性拿走——结果比任何爆破都完整。`-t axfr` 就是逐个 NS 试。
- **通配符检测**：很多域配了 `*.example.com`，会把任意名字都解析成功。dnsrecon 会先探测一个随机名字，若也被解析出同一 IP，就标记为 wildcard，避免爆破结果全是假阳性（`-f` 可过滤）。
- **DNSSEC NSEC 遍历（zonewalk）**：如果域开启 DNSSEC 且用 NSEC 而非 NSEC3，NSEC 记录本身就是"按字母序排列的下一个名字"，可以像链表一样把整个区域枚举出来。
- **默认并发**：查找/爆破/反查是并发的，用 `--threads` 控制。

## 3. 安装与快速上手

```bash
sudo apt install dnsrecon
dnsrecon --help | head -30
```

最小可用命令：

```bash
# 1) 标准枚举：SOA、NS、A、AAAA、MX、SRV
dnsrecon -d example.com

# 2) 对演练域名做区域传输测试（zonetransfer.me 是官方提供的合法练习域）
dnsrecon -d zonetransfer.me -t axfr

# 3) 子域爆破
dnsrecon -d example.com -t brt \
  -D /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-d <domain>` | 目标域名 | 位置核心参数 |
| `-t <type>` | 枚举类型 | 见下方"枚举类型表" |
| `-n <ns_server>` | 指定 DNS 服务器 | 换用公共 DNS 规避本地污染 |
| `-iL <file>` | 从文件读多个域名 | 批量任务 |
| `-D <dictionary>` | 爆破用字典 | 推荐 seclists 的 `subdomains-top1million-*` |
| `-f` | 过滤通配符解析的假结果 | 爆破时**强烈建议加上** |
| `--iw` | 即使发现通配符也继续爆破 | 默认会因通配符而放弃爆破 |
| `-r <range>` | 反查的 IP 段，`first-last` 或 `range/bitmask` | 配合 `-t rvl` |
| `-a` | 标准枚举时附加 AXFR | 相当于 `-t std` + `axfr` |
| `-s` | 反查 SPF 记录里的 IP 段 | 常能发现旁站网段 |
| `-w` | 深度 whois 分析并反查发现的 IP 段 | 耗时较长但信息量大 |
| `-k` | 查 crt.sh（证书透明度） | 被动，不接触目标，优先用 |
| `-b` / `-y` | Bing / Yandex 抓取子域 | 可能被搜索引擎封 |
| `-z` | DNSSEC zone walk | 目标必须开 DNSSEC 且用 NSEC |
| `--shodan` | 对发现的网段查 Shodan | 需要 API key |
| `--threads N` | 并发线程数 | 爆破时 10~50，太高会被限速 |
| `--lifetime N` | 单次查询等待秒数（默认 3.0） | 网络差时调大 |
| `--tcp` | 用 TCP 做 DNS 查询 | 回包被截断或需要绕过 UDP 限制时 |
| `--db out.sqlite` | 结果存 SQLite | 多次扫描结果比对 |
| `-x/-c/-j <file>` | XML / CSV / JSON 输出 | 与其他工具对接用 JSON |
| `--loglevel` | DEBUG/INFO/WARNING/ERROR/CRITICAL | 排查时用 DEBUG |
| `-v` | 详细输出 | 排查假阳性 |

**枚举类型表**（`-t` 取值）：

| 值 | 含义 |
|----|------|
| `std` | SOA、NS、A、AAAA、MX、SRV（默认可省略类型时的基础集） |
| `rvl` | 对给定 CIDR/IP 段做反向 PTR 查询 |
| `brt` | 用字典爆破域名与主机名 |
| `srv` | 专门枚举 SRV 记录 |
| `axfr` | 对全部 NS 测区域传输 |
| `bing` / `yand` | Bing / Yandex 搜索子域 |
| `crt` | crt.sh 证书透明度查询 |
| `caa` | CAA 记录 |
| `snoop` | 对 NS 做 DNS 缓存窥探（需 `-D` 提供域名字典） |
| `tld` | 去掉 TLD 后对 IANA 全部 TLD 逐个尝试 |
| `zonewalk` | 基于 NSEC 的 DNSSEC 区域遍历 |

## 5. 实战演练

**环境**：以下仅使用公开的合法演练资源，不针对任何未授权目标。

- `zonetransfer.me`：DigiNinja 提供的**专门用于练习区域传输**的域名。
- `example.com`：IANA 保留示例域。
- 自建实验域：在本地 bind9 里建 `lab.local` 区域（见第 7 节）。

### 场景 1：标准枚举摸清骨架

```bash
dnsrecon -d zonetransfer.me -t std
```

预期输出片段：

```text
[*] Performing General Enumeration of Domain: zonetransfer.me
[*]      SOA nsztm1.digi.ninja 81.4.108.41
[*]      NS nsztm1.digi.ninja 81.4.108.41
[*]      NS nsztm2.digi.ninja 167.88.136.10
[*]      A zonetransfer.me 5.196.105.14
[*]      MX 10 ASPMX.L.GOOGLE.COM 74.125.68.26
[*]      TXT zonetransfer.me "google-site-verification=..."
[*] Enumerating SRV Records
```

解读：这一步就把目标的基础设施画出来了——NS 在哪、邮件去哪、有没有 TXT 泄露云服务商。SOA 里的 NS 名称是后续 AXFR 的攻击面。

### 场景 2：区域传输测试（最有价值的单点检查）

```bash
dnsrecon -d zonetransfer.me -t axfr
```

预期输出片段：

```text
[*] Checking for Zone Transfer for zonetransfer.me name servers
[*] Resolving SRV record for _dns._tcp.zonetransfer.me
[+] Zone Transfer was successful!! DNS Server: nsztm1.digi.ninja
[*]      SOA nsztm1.digi.ninja 81.4.108.41
[*]      NS nsztm1.digi.ninja 81.4.108.41
[*]      A admin.zonetransfer.me 5.196.105.14
[*]      A vpn.zonetransfer.me 174.36.30.15
[*]      A internal.zonetransfer.me 10.10.10.10
[*]      A roblogic.zonetransfer.me 5.196.105.14
...
[+] 30 Records found
```

解读：`Zone Transfer was successful!!` 是高危配置错误。注意 `internal.zonetransfer.me 10.10.10.10`——内网地址泄露给了外部。这条发现通常会直接写进报告的高危项。

### 场景 3：子域爆破 + 通配符过滤

```bash
dnsrecon -d example.com -t brt -f --threads 20 \
  -D /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  -j brutesult.json
```

预期输出片段：

```text
[*] Performing host and subdomain brute force against example.com
[*] 	 A www.example.com 93.184.216.34
[*] 	 CNAME mail.example.com ...
[+] 5 Records Found
```

解读：
- `-f` 过滤掉通配符造成的假解析结果，否则 5000 个字典项可能"全部命中"。
- 若输出里出现 `Wildcard resolution detected`，说明该域配了 `*` 记录，任何字典都会全中；此时只有真正不同的 IP 才可能是真子域。
- `-j` 输出 JSON，方便跟历史结果做 diff，发现新增资产。

### 场景 4（进阶）：被动数据源 + 网段反查

```bash
# 先用证书透明度被动拿子域（不接触目标）
dnsrecon -d example.com -k

# 反查 SPF 里暴露的网段
dnsrecon -d example.com -t std -s

# 对发现的 C 段做 PTR 反查
dnsrecon -d example.com -t rvl -r 93.184.216.0/24
```

解读：`-k`（crt.sh）和 `-s`（SPF 反查）都可能在你"碰到"目标之前就给出大量资产清单，属于低噪声手段。`-r` 反查能发现同一段里未在 DNS 中列出的主机。

## 6. 输出解读

| 行首/字段 | 含义 | 下一步动作 |
|-----------|------|-----------|
| `[*]` | 普通信息（正在做什么） | — |
| `[+]` | 有效发现 | 记录进资产表 |
| `[-]` | 失败/无结果 | 换 NS 或换查询方式 |
| `Zone Transfer was successful` | AXFR 成功，可拿到整份区域 | 立即导出全文，逐条核对 |
| `Wildcard resolution detected` | 通配符污染 | 加 `-f`，或只保留 IP 与基线不同的记录 |
| `A <name> <ip>` | 解析记录 | 把 IP 送去 [nmap](nmap.md) 扫端口 |
| `MX` / `TXT` / `SPF` | 邮件与验证信息 | 拿云厂商、邮件服务线索 |

落地到动作：

```text
dnsrecon -t std → 拿到 IP 列表 → 去重后 nmap -sV 扫端口
dnsrecon -k     → 拿到子域列表 → 逐个 whatweb 做指纹
```

## 7. 与其他工具配合

```bash
# 1) dnsrecon JSON -> 提取所有 A 记录 IP -> nmap
dnsrecon -d example.com -t std -j dns.json
python3 - <<'EOF'
import json
d = json.load(open('dns.json'))
ips = {r['address'] for r in d if r.get('type') in ('A','AAAA') and 'address' in r}
open('ips.txt','w').write('\n'.join(sorted(ips)))
EOF
sudo nmap -sV -iL ips.txt --open -oA dns_scan

# 2) 子域列表 -> whatweb / httpx 指纹
dnsrecon -d example.com -t brt -f -D words.txt -j b.json
python3 -c "import json;print('\n'.join(r['name'] for r in json.load(open('b.json')) if r.get('type')=='A'))" > subs.txt

# 3) 直接调用 dig 复核某条结论（排除脚本 bug）
dig +short AXFR example.com @ns1.example.com
dig +trace example.com
```

自建实验域（合法的可练习 AXFR 目标）：

```bash
sudo apt install bind9
# 在 named.conf.local 中定义 zone "lab.local"，并允许 10.0.0.0/24 传输
sudo systemctl restart bind9
dnsrecon -d lab.local -n 127.0.0.1 -t axfr
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `Could not resolve domain` / 全部超时 | 本地 DNS 不通或被污染 | `-n 1.1.1.1` 指定公共 DNS；或加 `--tcp` |
| 爆破结果"全部命中" | 域配了通配符 `*` | 加 `-f`；或先看是否提示 wildcard |
| `Zone Transfer was successful` 但记录很少 | 只有部分 NS 开放 AXFR | 逐个 NS 单独测：`dig AXFR @nsX` |
| 速度极慢 | 反查 + whois 阶段在跑 | 加 `--noreverse`；或分开跑只用 `-t` 指定类型 |
| `[!] DNSSEC ... NSEC3` zonewalk 失败 | 域使用 NSEC3 而非 NSEC | NSEC3 无法遍历，改用 `-k` crt.sh |
| Bing/Yandex 抓取被拒 | 搜索引擎反爬 | 换 `-k`（crt.sh）等被动源 |
| `sqlite3` 报错写不进 | 目录权限 | 换 `--db /tmp/out.sqlite` |
| 结果里出现大量 `*.in-addr.arpa` | 反查 PTR 未过滤 | 用 `-e <regexp>` 排除无效主机名 |

## 9. 防御视角（蓝队）

- **AXFR**：这是最该堵的口。在 bind9 中只允许从服务器做传输：
  ```text
  zone "example.com" {
      type master;
      file "/etc/bind/db.example.com";
      allow-transfer { 10.0.0.2; };   # 只允许从 NS
  };
  ```
- **子域爆破检测**：`NXDOMAIN` 响应会呈现明显的"同一源 IP、大量顺序字典词、高 QPS"模式。可在递归解析器（Unbound/BIND）上开启 `response rate limiting (RRL)`，并监控 NXDOMAIN 比例突增。
- **通配符不是安全措施**：配 `*` 记录只会增加噪声，不会阻止爆破。
- **信息最小化**：
  - 不要把内网地址（如 `10.10.10.10`）写进公网区域文件。
  - `TXT` 里避免残留云厂商验证串、内部工具地址。
  - 关闭 `version.bind` 泄露（`version none;`）。
- **DNSSEC 建议用 NSEC3**（加盐哈希），避免 NSEC 链式遍历。

## 10. 参考

- 官方仓库：<https://github.com/darkoperator/dnsrecon>
- 区域传输练习域：<https://digi.ninja/projects/zonetransferme.php>
- 证书透明度查询：<https://crt.sh/>
- man page：`man dnsrecon`

---

**相关教程**：[dnsenum](dnsenum.md) ｜ [fierce](fierce.md) ｜ [amass](amass.md) ｜ [theharvester](theharvester.md) ｜ [nmap](nmap.md)
