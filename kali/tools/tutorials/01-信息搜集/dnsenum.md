# dnsenum（多线程 DNS 信息枚举与非连续网段发现）

> **一句话**：用多线程把一个域名的 DNS 记录、子域、区域传输和 whois 网段一次挖出来，重点是发现"不连续的 IP 段"。
> **分类**：信息搜集 ｜ **Kali 包**：`dnsenum` ｜ **官方文档**：<https://github.com/SparrowOchon/dnsenum2>

## 1. 它解决什么问题

一个组织的公网资产很少老老实实待在同一个 C 段里：总部一个段、CDN 一个段、收购来的子公司又是另一个段。dnsenum 的独特价值就是**通过 DNS + 谷歌抓取 + whois 反查，把散落在各处的网段拼出来**，并写入 `domain_ips.txt`。

与 [dnsrecon](dnsrecon.md) 的对比：

| 维度 | dnsenum | dnsrecon |
|------|---------|----------|
| 实现 | Perl，多线程 | Python |
| 强项 | whois 网段推导、谷歌抓取子域、递归爆破有 NS 的子域 | 枚举类型更全、DNSSEC/crt.sh/缓存窥探 |
| 输出 | `domain_ips.txt`（非连续 IP 块）+ `--subfile` 子域文件 | SQLite/XML/CSV/JSON |
| 适合 | "找出所有网段" | "一次跑完全部 DNS 检查" |

两者互补，实战中经常都跑一遍再取并集。

## 2. 工作原理

dnsenum 按固定流水线依次执行 9 步：

```text
 1. A 记录查询          ──►  目标域解析到哪些 IP
 2. NS 记录（多线程）    ──►  名称服务器清单（AXFR 的目标）
 3. MX 记录（多线程）    ──►  邮件服务器
 4. AXFR（多线程）       ──►  逐个 NS 尝试区域传输
 5. 谷歌抓取             ──►  查询 "-www site:domain"，从 SERP 里捡子域
 6. 子域爆破（必需 -f）  ──►  读字典猜名字；-r 时对有 NS 的子域递归爆破
 7. Class C 网段推算     ──►  从前面结果按 /24 归并，对每段做 whois
 8. 反查 PTR（多线程）    ──►  对网段里的 IP 做反向解析
 9. 汇总                 ──►  非连续 IP 块写入 domain_ips.txt
```

关键机制：

- **网段推算**：把 `93.184.216.34`、`93.184.216.7` 归到 `93.184.216.0/24`，然后对整个 /24 做 whois，whois 返回的 `NetRange` 可能比 /24 大得多，于是又得到新网段——如此迭代。
- **`--enum` 快捷方式**：等价于 `--threads 5 -s 20 -w`，是"一键跑完整流程"的入口。
- **递归爆破（`-r`）**：如果 `dev.example.com` 自己也有 NS 记录（独立子区），就再对它跑一遍爆破字典。

## 3. 安装与快速上手

```bash
sudo apt install dnsenum
dnsenum --help
```

最小可用命令：

```bash
# 1) 一键跑完整枚举流程（含谷歌抓取 + whois 网段）
dnsenum --enum example.com

# 2) 只做基础枚举 + 子域爆破（跳过耗时的 whois/反查）
dnsenum --noreverse -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt example.com

# 3) 测试区域传输
dnsenum --noreverse --enum -f words.txt zonetransfer.me
```

## 4. 核心参数详解

### 通用

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `<domain>` | 目标域名（位置参数） | 必填 |
| `--dnsserver <server>` | 所有 A/NS/MX 查询走此 DNS（AXFR/PTR 仍走域自身 NS） | 本地 DNS 被污染时使用 |
| `--enum` | = `--threads 5 -s 20 -w` | 想少打字就加这个 |
| `--noreverse` | 跳过反查 | 大网段反查极慢，时间紧时加 |
| `--private` | 显示并保存私网 IP | 内网实验域会用上 |
| `--subfile <file>` | 把有效子域写入文件 | 后续喂给 httpx/whatweb |
| `-t, --timeout <sec>` | TCP/UDP 超时（默认 10 秒） | 慢链路加大到 20 |
| `--threads <n>` | 并发线程数 | 5~20；太高会被上游限速 |
| `-v, --verbose` | 显示全部进度与错误 | 排查假阴性 |
| `--nocolor` | 关闭颜色 | 输出重定向到文件时 |

### 谷歌抓取

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-s, --scrap <n>` | 最多抓取 n 个子域 | 必须配合抓取才生效；太大容易被 Google 封 |
| `-p, --pages <n>` | 抓取谷歌结果页数（默认 20） | 与 `-s` 配合 |

> 抓取依赖 `WWW::Mechanize`；支持从环境变量 `http_proxy` / `HTTP_PROXY` 读代理，被 Google 拦时可用代理绕。

### 爆破

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-f, --file <file>` | 爆破字典（**必需**，覆盖默认 `dns.txt`） | 用 seclists 的 DNS 字典 |
| `-r, --recursion` | 对有 NS 记录的子域递归爆破 | 会显著增加时长 |
| `-u, --update <a\|g\|r\|z>` | 用结果回写字典：a=全部，g=谷歌，r=反查，z=区域传输 | 让字典越跑越"懂"这个域 |

### whois / 反查

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-w, --whois` | 对推算出的 C 段做 whois | 会产生**巨大**网段，耗时且反查量爆炸 |
| `-d, --delay <sec>` | whois 查询间最大随机延迟（默认 3 秒） | whois 服务器会限连接数，别关掉 |
| `-e, --exclude <regexp>` | 反查时排除匹配正则的 PTR | 过滤 `ip-*-*-*-*.static` 之类无效名 |

## 5. 实战演练

**环境**：仅使用公开合法练习资源 + 本地自建实验域。

- `zonetransfer.me`：官方提供的 AXFR 练习域
- `example.com`：IANA 保留示例域
- 本地 `lab.local`：自建 bind9 区域（见第 7 节）

### 场景 1：基础枚举（不碰 whois，速度快）

```bash
dnsenum --noreverse --enum example.com
```

预期输出片段：

```text
-----   example.com   -----

Host's addresses:
__________________
example.com.                            300      IN    A        93.184.216.34

Name Servers:
______________
a.iana-servers.net.                     172800   IN    A        199.43.135.53

Mail (MX) Servers:
___________________
.

Trying Zone Transfers and getting Bind Versions:
_________________________________________________
Trying Zone Transfer for example.com on a.iana-servers.net ...
AXFR record query failed: REFUSED

Brute forcing with subdomains-top1million-5000.txt:
______________________________________________________
www.example.com.                        3600     IN    A        93.184.216.34

done. 1 addresses found
```

解读：`AXFR record query failed: REFUSED` 是**正常且安全**的结果；只有出现 `Zone Transfer successful` 才是配置问题。

### 场景 2：区域传输练习 + 子域文件输出

```bash
dnsenum --noreverse --subfile subs.txt -f words.txt zonetransfer.me
cat subs.txt
```

预期输出片段：

```text
Trying Zone Transfer for zonetransfer.me on nsztm1.digi.ninja ...
AXFR record query failed: REFUSED
Trying Zone Transfer for zonetransfer.me on nsztm2.digi.ninja ...
Zone Transfer successful. 30 records found.

Following subdomains were found:
admin.zonetransfer.me
vpn.zonetransfer.me
internal.zonetransfer.me
roblogic.zonetransfer.me
```

解读：注意 `nsztm1` 拒绝、`nsztm2` 允许——**只测一个 NS 会漏判**。`--subfile` 把所有来源的有效子域汇总下来，直接可用于下一步探测。

### 场景 3（进阶）：whois 网段推导发现旁站资产

```bash
dnsenum --enum -f words.txt -w example.com
cat domain_ips.txt
```

预期输出片段：

```text
Whois Queries Results:
______________________
NetRange:       93.184.216.0 - 93.184.216.255
CIDR:           93.184.216.0/24
OrgName:        Edgecast Inc.

Non-Contiguous IP Blocks:
___________________________
93.184.216.0/24
```

解读：`domain_ips.txt` 里可能同时出现多个不连续段。这些段是后续 [nmap](nmap.md) 扫描的范围依据——但**注意 whois 得到的网段可能是云服务商的大段**，扫描前必须确认所有权边界，不要越界。

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `Host's addresses` | 目标 A 记录 | 主体 IP |
| `Name Servers` | NS 清单 | 逐个测 AXFR |
| `Trying Zone Transfer ... REFUSED` | 服务器拒绝传输 | 正常，继续 |
| `Zone Transfer successful` | 可用 AXFR 拿到全区域 | 高危发现，记录并导出 |
| `Brute forcing with <dict>` | 爆破结果 | 存 `--subfile` |
| `done. N addresses found` | 本次有效地址数 | N=0 时检查通配符/DNS |
| `domain_ips.txt` | 非连续 IP 块 | 交给 nmap 划范围 |
| `Google search results` | 抓到的子域 | 与爆破结果取并集 |

## 7. 与其他工具配合

```bash
# dnsenum -> nmap：把子域解析结果送去扫端口
dnsenum --noreverse --subfile subs.txt -f words.txt example.com
sed 's/\.$//' subs.txt | sort -u > subs_clean.txt
dnsx -l subs_clean.txt -a -resp -o resolved.txt   # 或 dnsrecon/bulk 解析
awk '{print $2}' resolved.txt | sort -u > ips.txt
sudo nmap -sV -iL ips.txt --open -oA enum_scan

# 自建可练习 AXFR 的实验域
sudo apt install bind9
# 编辑 /etc/bind/named.conf.local：
#   zone "lab.local" { type master; file "/etc/bind/db.lab.local"; allow-transfer { 127.0.0.1; 10.0.0.0/24; }; };
sudo systemctl restart bind9
dnsenum --noreverse --enum -f words.txt lab.local
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `Can't load Net::DNS` 等模块缺失 | Perl 依赖未装 | `sudo apt install --reinstall dnsenum`（会拉齐依赖） |
| 谷歌抓取阶段卡死 / 报 IO 错误 | Google 反爬拦截 | 设 `http_proxy` 环境变量；或跳过抓取（不写 `-s`） |
| 明明有子域却爆破不到 | 域配了通配符 `*`，或字典太小 | 换更大字典；先手工 `dig random.example.com` 判断通配符 |
| `-w` 跑到天亮 | Class C + whois 递归产生海量网段 | 不要和 `-w` 一起用默认反查；改 `--noreverse` |
| 子域被枚举但 PTR 全被过滤 | 默认排除"不匹配域名"的 PTR | 加 `-v` 看完整结果 |
| 输出乱码/转义序列 | 终端不支持 ANSI 颜色 | `--nocolor` |
| 域名末尾多一个点导致比对失败 | 脚本输出为 FQDN（带 `.`） | 处理时 `sed 's/\.$//'` |
| 结果与 dnsrecon 不一致 | 查询的 NS 不同 / 缓存不同 | 统一 `--dnsserver 1.1.1.1` |

## 9. 防御视角（蓝队）

- **AXFR 是最应该关的门**：`allow-transfer` 只放从服务器；外网 NS 一律 `allow-transfer { none; };`。dnsenum 的 AXFR 步骤会被 NS 日志完整记录（REFUSED 也会记），可作为告警源。
- **爆破检测**：大量 `NXDOMAIN` + 顺序字典词是典型特征。递归解析器开 RRL，日志侧对"单源 IP NXDOMAIN 速率"设阈值。
- **whois 阶段无法在 DNS 侧检测**（那是查注册库），但可以通过"异常的反查 PTR 请求量"发现问题——如果对方开始对你整个 /24 做 PTR，说明你的网段已被列入清单。
- **降低信息收益**：
  - 子域不要用可猜的名字（`dev`、`test`、`admin`）直接暴露在公网 DNS。
  - 内部服务用独立域 + 分割 DNS（split-horizon），不要在公网区域文件里写内网地址。
  - 关闭 `version.bind`，避免泄露 BIND 版本。

## 10. 参考

- 官方仓库（dnsenum2，Kali 收录版本上游）：<https://github.com/SparrowOchon/dnsenum2>
- 区域传输练习域：<https://digi.ninja/projects/zonetransferme.php>
- man page：`man dnsenum`

---

**相关教程**：[dnsrecon](dnsrecon.md) ｜ [fierce](fierce.md) ｜ [amass](amass.md) ｜ [theharvester](theharvester.md) ｜ [nmap](nmap.md)
