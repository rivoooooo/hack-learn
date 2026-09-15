# 02 · 漏洞分析（Vulnerability Analysis）工具教程

漏洞分析阶段的任务是**把"有什么服务"变成"有什么问题"**。与信息搜集不同，这一步会主动与目标产生更多交互，也更容易被检测到——所以噪声控制和授权确认在这里尤其重要。

本目录收录 7 个 Kali 官方工具（`lynis`、`fping`、`ike-scan` 在 Kali 官方分类中被归为"漏洞分析"，本目录沿用官方分组）。

## 工具清单

| 工具 | 一句话 | 难度 | 教程 |
|------|--------|------|------|
| `nikto` | Web 服务器配置与已知问题扫描（6700+ 检查项） | ★★☆ | [nikto.md](nikto.md) |
| `nuclei` | 基于 YAML 模板的精确漏洞扫描，误报低、可自定义 | ★★★ | [nuclei.md](nuclei.md) |
| `lynis` | Linux/Unix 主机配置加固审计（防守视角） | ★★★ | [lynis.md](lynis.md) |
| `searchsploit` | 本地 Exploit-DB 检索，把服务版本变成可用 EXP | ★☆☆ | [searchsploit.md](searchsploit.md) |
| `openssl` | TLS/SSL 握手诊断、证书分析、Heartbleed 前提检测 | ★★★ | [openssl.md](openssl.md) |
| `fping` | 批量 ICMP 存活探测，脚本友好的清单生成器 | ★☆☆ | [fping.md](fping.md) |
| `ike-scan` | IPsec/IKE VPN 发现、指纹与 PSK 参数抓取 | ★★★ | [ike-scan.md](ike-scan.md) |

难度说明：★☆☆ 上手即可用；★★☆ 需要理解参数与场景；★★★ 需要理解协议或框架模型。

## 学习顺序建议

### 第一步：先掌握"把结果结构化"的两个工具（★☆☆）

1. **[searchsploit](searchsploit.md)** —— 最简单也最常用。学会它，nmap 的结果才有意义。
2. **[fping](fping.md)** —— 学会用极简工具生成输入清单，理解"退出码即接口"的脚本化思路。

### 第二步：Web 与 TLS 两条主线（★★☆）

3. **[nikto](nikto.md)** —— 第一个真正的漏洞扫描器。重点学 **`-Tuning` 控制范围**和**如何复核误报**。
4. **[openssl](openssl.md)** —— TLS 诊断的通用语言。重点学 `s_client -brief`、证书链验证、以及 Heartbleed 的正确检测路径。

### 第三步：主机侧与精确检测（★★★）

5. **[lynis](lynis.md)** —— 换成防守视角看系统。学 `warning` vs `suggestion` 的区分，以及用 diff 跟踪加固进展。
6. **[nuclei](nuclei.md)** —— 现代漏洞扫描的核心工具。学模板过滤（`-severity`/`-tags`/`-etags`）、OAST 机制、写自己的模板。
7. **[ike-scan](ike-scan.md)** —— 最"专"的一个。理解 IKE 的 Main/Aggressive Mode 差异，以及为什么 PSK + Aggressive 是设计缺陷。

## 常见工作流

### 工作流一：Web 目标（从指纹到验证）

```text
whatweb / nmap -sV（指纹）
        ↓
nikto -Tuning 23（广撒网找线索）
        ↓
nuclei -severity medium,high,critical（精确验证）
        ↓
curl / 手工复核命中项
        ↓
searchsploit（有版本号的拿去查 EXP）
```

### 工作流二：服务与 TLS

```text
nmap -sV -oX scan.xml
        ↓
searchsploit --nmap scan.xml（批量找 EXP）
        ↓
nmap --script "ssl-enum-ciphers,ssl-cert,ssl-heartbleed"
        ↓
openssl s_client -brief / -showcerts（逐项确认）
```

### 工作流三：主机加固审计（蓝队视角）

```text
lynis audit system --quick（基线）
        ↓
按 warning 清单整改
        ↓
lynis audit system --tests "SSH-7408"（单项复核）
        ↓
报告归档 + diff 跟踪趋势
```

### 工作流四：网络层与外网入口

```text
fping -a -g <网段>（存活清单）
        ↓
nmap -sV -iL alive.txt（服务识别）
        ↓
ike-scan（发现 IPsec VPN 网关）
        ↓
nmap -sU -p500,4500（确认开放）
```

## 噪声与授权提醒（比信息搜集更严格）

- **nikto** 会发**数千个请求**，且包含"拒绝服务"类测试（类别 6）。生产环境扫描前务必告知运维，并用 `-Tuning x6` 排除 DoS 类别。
- **nuclei** 默认 150 请求/秒。对生产环境请降到 `-rl 20`，并用 `-etags dos,fuzz` 排除有副作用的模板。
- **ike-scan** 的候选目标通常是 **VPN 网关**——这是安全团队重点监控的对象。探测行为会被记录，务必事先取得书面授权并告知对方。
- **lynis** 是只读的，唯一风险是**报告里包含主机敏感信息**。共享主机上建议加 `--no-log`。
- **openssl s_client** 的探测很"轻"，但逐版本/逐套件枚举会产生大量 TLS 握手失败——在高安全环境里同样会被识别。
- **searchsploit** 与 **fping** 风险最低（前者纯本地查询，后者同 [nmap](../01-信息搜集/nmap.md) 的存活探测）。

## 与其他分类的衔接

- 本分类的输入通常来自 [01-信息搜集](../01-信息搜集/README.md)：`nmap` 的端口与版本、`whatweb` 的技术栈。
- 发现具体的 Web 漏洞（SQL 注入、命令注入、目录爆破）后，去 [03-Web应用](../03-Web应用/README.md) 用 [sqlmap](../03-Web应用/sqlmap.md)、[commix](../03-Web应用/commix.md)、[ffuf](../03-Web应用/ffuf.md) 做深入验证与利用。
- `lynis` 的核查结论可以直接支撑主机加固与合规工作（CIS/ISO 27001 映射）。
- `ike-scan` 挖到的 PSK 参数需要离线破解——这属于口令攻击范畴（Kali 分类 `passwords`）。
