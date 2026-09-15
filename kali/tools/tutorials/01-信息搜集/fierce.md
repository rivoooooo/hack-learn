# fierce（轻量 DNS 扫描与非连续 IP 空间发现）

> **一句话**：在打端口扫描之前，先用 DNS 把目标的域名、子域和"散落各处的网段"找出来。
> **分类**：信息搜集 ｜ **Kali 包**：`fierce` ｜ **官方文档**：<https://github.com/mschwager/fierce>

## 1. 它解决什么问题

[nmap](nmap.md)、[nikto](../02-漏洞分析/nikto.md)、OpenVAS 都有一个共同前提：**你得先知道要扫哪个 IP 段、哪些主机名**。fierce 填的就是这个空档——它不做漏洞利用，也不漫无目的地扫全网，只围绕指定域做一件事：**找到可能的目标，包括那些内网地址意外泄露到公网 DNS 的网段**。

定位是 [nmap](nmap.md) 的"前一步"。

| 工具 | 侧重 |
|------|------|
| **fierce** | 半轻量；发现"非连续 IP 空间"；渗透测试起步阶段 |
| [dnsrecon](dnsrecon.md) | 枚举类型最全，输出结构化（SQLite/JSON） |
| [dnsenum](dnsenum.md) | 多线程 + whois 网段推导 + 谷歌抓取 |
| [amass](amass.md) | 长期资产面跟踪，被动数据源 + 图谱 |

## 2. 工作原理

```text
        fierce --domain example.com --subdomains www mail dev
                            │
   ┌────────────────────────┴────────────────────────┐
   │ 1. 解析目标域 A 记录                             │
   │ 2. 逐个子域解析（或从 --subdomain-file 读取）     │
   │ 3. 对每个 NS 尝试 AXFR（区域传输）                │
   └────────────────────────┬────────────────────────┘
                            │ 得到一批 IP
   ┌────────────────────────┴────────────────────────┐
   │ 4. 邻域扩展（这是 fierce 的核心）                │
   │    --traverse N : 在发现的 IP 前后各扫 N 个      │
   │                   （不跨越 C 段边界）            │
   │    --wide       : 扫描发现 IP 所在的整个 /24     │
   │ 5. 对扩展出的 IP 做 PTR 反查，得到新主机名        │
   │ 6. 对新主机名再解析 → 迭代，拼出完整网段         │
   └────────────────────────┬────────────────────────┘
                            │
          --search 限定只保留感兴趣的域
          --connect 对非私网 IP 试一次 HTTP 连接
```

核心洞察是：**组织常把一块连续 IP 分配给一个域，即使 DNS 里只暴露了其中一台**。靠 `--traverse` / `--wide` 往邻居 IP 摸一圈，往往能捞出没被列出的主机名，甚至发现内网地址（`10.x`/`192.168.x`）被误写进公网记录。

## 3. 安装与快速上手

```bash
sudo apt install fierce
fierce --help
```

最小可用命令：

```bash
# 1) 只测区域传输（fierce 最经典的用法）
fierce --domain zonetransfer.me

# 2) 指定几个子域一起看
fierce --domain example.com --subdomains www mail dev admin

# 3) 内网网段反查（配合内部 DNS）
fierce --dns-servers 10.0.0.1 --range 10.0.0.0/24
```

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `--domain <domain>` | 要测试的域名 | 与 `--range` 二选一 |
| `--subdomains <a> <b> ...` | 手工指定要试的子域列表 | 少量、明确的候选名 |
| `--subdomain-file <file>` | 从文件读子域（一行一个） | 与 `--subdomains` 互斥；批量时用 |
| `--range <cidr>` | 直接指定要扫描的内网段（CIDR） | 内网资产盘点；配合 `--dns-servers` |
| `--dns-servers <ip...>` | 反查使用的 DNS 服务器 | 内网必须指定内网 DNS |
| `--dns-file <file>` | 从文件读 DNS 服务器 | 多解析器场景 |
| `--traverse <N>` | 在发现的 IP 前后各扫 N 个地址 | **尊重 C 段边界**，不会跨进相邻子网；N 取 5~30 比较克制 |
| `--wide` | 扫描发现 IP 所在的整个 /24 | 覆盖更全，但请求量 = 256 倍，慎用 |
| `--search <d1> <d2>` | 邻域扩展时只保留匹配这些域的结果 | 减少噪声，避免把云服务商的邻居全捞进来 |
| `--connect` | 对非 RFC1918 地址尝试 HTTP 连接 | 能确认"有 Web 服务"，但会留下访问日志，谨慎 |
| `--delay <sec>` | 每次查询之间等待秒数 | 默认无延迟；被限速时加 1~2 秒 |
| `--tcp` | 用 TCP 而非 UDP 做 DNS 查询 | 大响应被截断时 |

> `--subdomains` 与 `--subdomain-file` 互斥；`--dns-servers` 与 `--dns-file` 互斥。

## 5. 实战演练

**环境**：全部使用公开合法练习资源或本地自建服务。

- `zonetransfer.me`：DigiNinja 提供的 AXFR 练习域
- `example.com`：IANA 保留示例域
- 本地 bind9 的 `lab.local` 与 `10.0.0.0/24`（第 7 节给出搭建方法）

### 场景 1：区域传输测试（fierce 的招牌用法）

```bash
fierce --domain zonetransfer.me
```

预期输出片段：

```text
NS: nsztm1.digi.ninja. nsztm2.digi.ninja.
SOA: nsztm1.digi.ninja. (81.4.108.41)

Zone: success
{  admin.zonetransfer.me. 5.196.105.14
   vpn.zonetransfer.me. 174.36.30.15
   internal.zonetransfer.me. 10.10.10.10
   roblogic.zonetransfer.me. 5.196.105.14  }
```

解读：`Zone: success` 表示拿到了完整区域文件，等价于"DNS 城堡的钥匙都交出来了"。`internal.zonetransfer.me. 10.10.10.10` 是典型的**内网地址泄露**——公网可直接看到内部网段规划。

### 场景 2：指定子域 + 邻域遍历

```bash
fierce --domain example.com --subdomains www mail dev --traverse 10
```

预期输出片段：

```text
NS: a.iana-servers.net. b.iana-servers.net.
SOA: ...

Trying zone transfer: a.iana-servers.net. -> REFUSED
Trying zone transfer: b.iana-servers.net. -> REFUSED

Subdomains:
  www.example.com   93.184.216.34
  mail.example.com  ...

Traversing 10 IPs before and after 93.184.216.34 (within 93.184.216.0/24)
  reverse lookup 93.184.216.24 -> ...
```

解读：`--traverse 10` 只扫前后 10 个地址，且**不会越过 /24 边界**，代价可控。反查出来的新主机名如果属于同一组织，会一并加入结果。

### 场景 3：内网网段资产盘点

```bash
fierce --dns-servers 10.0.0.1 --range 10.0.0.0/24
```

预期输出片段：

```text
Now performing reverse lookups on 10.0.0.0/24
10.0.0.1  -> gw.lab.local
10.0.0.10 -> kali.lab.local
10.0.0.20 -> srv-web.lab.local
10.0.0.30 -> srv-db.lab.local
```

解读：这是内网渗透/资产盘点最常用的一步。把 DNS 里存在但没记录在 CMDB 的主机找出来，然后交给 [nmap](nmap.md) 扫端口。

### 场景 4（进阶）：`--wide` + `--search` 控制范围

```bash
# 只保留匹配 example.com / example.net 的邻居，避免把所有云主机都捞进来
fierce --domain example.com --wide --search example.com example.net
```

解读：`--wide` 会对每个发现 IP 扫整个 /24（256 次反查），量大且容易撞到同机房其他客户。**务必配合 `--search`**，否则结果里会混进大量无关域名。

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `NS: ...` | 名称服务器 | 逐个单独测 AXFR |
| `Zone: success` + 记录列表 | AXFR 成功 | 高危发现；导出全部记录 |
| `Trying zone transfer ... REFUSED` | 拒绝传输 | 正常结果，继续 |
| `Subdomains:` 区块 | 解析成功的子域 | 汇总后交给 httpx/whatweb |
| `Traversing N IPs ...` | 正在做邻域扩展 | 关注新出现的反查名 |
| `10.x.x.x` / `192.168.x.x` | 公网 DNS 里泄露的私网地址 | 直接写入报告的高危项 |
| `HTTP: 200`（配 `--connect`） | 对非私网地址成功建立 HTTP 连接 | 用 whatweb 做指纹 |
| 输出为空 | 子域不存在 / NS 拒绝 / DNS 不可达 | 换 `--dns-servers`，或检查 `--domain` 拼写 |

保存结果：

```bash
fierce --domain zonetransfer.me > fierce_zonetransfer.txt
fierce --dns-servers 10.0.0.1 --range 10.0.0.0/24 > internal_dns.txt
```

## 7. 与其他工具配合

```bash
# fierce 输出 -> 提取主机名 -> whatweb 指纹
fierce --domain example.com --subdomains www mail dev | \
  grep -oP '[\w.-]+\.example\.com' | sort -u > subs.txt

while read h; do whatweb -a 1 "http://$h" 2>/dev/null; done < subs.txt

# fierce 反查结果 -> nmap 扫端口
fierce --dns-servers 10.0.0.1 --range 10.0.0.0/24 | \
  grep -oP '^\d+\.\d+\.\d+\.\d+' | sort -u > ips.txt
sudo nmap -sV -iL ips.txt --open -oA fierce_then_nmap

# 自建可练习的实验域（合法 AXFR 目标）
sudo apt install bind9
# /etc/bind/named.conf.local:
#   zone "lab.local" { type master; file "/etc/bind/db.lab.local";
#                      allow-transfer { 127.0.0.1; 10.0.0.0/24; }; };
sudo systemctl restart bind9
fierce --dns-servers 127.0.0.1 --domain lab.local
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| 输出里没有 Zone 段落 | 该域不开放 AXFR（绝大多数情况） | 正常；改看 Subdomains 与反查结果 |
| `--subdomains` 和 `--subdomain-file` 同时写 | 参数互斥 | 只保留一个 |
| 内网段全部反查失败 | 用的是公网 DNS，解析不到内网 PTR | `--dns-servers <内网DNS>` |
| `--wide` 结果里全是无关域名 | 同 /24 是云服务商共享段 | 加 `--search <自己的域>` |
| 被上游 DNS 限速 / 查询超时 | 无延迟高频查询 | `--delay 1`；或改用 `--tcp` |
| `--connect` 触发了目标告警 | 主动 HTTP 连接会留下日志 | 明确授权再用；优先不加该参数 |
| 域名拼写错误导致全部 NXDOMAIN | — | 先用 `dig +short A <domain>` 验证 |
| Python 版本相关报错 | 老版本 fierce 依赖 | `sudo apt install --reinstall fierce` |

## 9. 防御视角（蓝队）

- **AXFR**：把 `allow-transfer` 收紧到只有从服务器；公网 NS 一律 `none`。这是 fierce 最容易一次拿到全部信息的入口。
- **邻域遍历的可见性**：`--traverse` / `--wide` 会产生"对整段做 PTR 反查"的明显模式。在递归解析器日志里，表现为同一源 IP 对 `x.y.z.0/24` 的 `in-addr.arpa` 顺序查询。可对此设置阈值告警。
- **不要泄露内网网段**：公网区域文件里绝不能出现 `10.`/`172.16-31.`/`192.168.` 地址；用 split-horizon DNS 隔离内外视图。
- **子域命名**：避免 `dev`、`test`、`vpn`、`internal` 这类高猜测率名字直接暴露；能走通配符证书 + 单入口就别铺一堆子域。
- **反向解析区域**：只对必要网段开放 PTR 区域；不开放 PTR 能显著降低邻域发现收益。

## 10. 参考

- 官方仓库：<https://github.com/mschwager/fierce>
- 中文快速上手可用 `fierce --help` 的 argparse 输出
- 区域传输练习域：<https://digi.ninja/projects/zonetransferme.php>
- man page：`man fierce`

---

**相关教程**：[dnsrecon](dnsrecon.md) ｜ [dnsenum](dnsenum.md) ｜ [amass](amass.md) ｜ [theharvester](theharvester.md) ｜ [nmap](nmap.md) ｜ [whatweb](whatweb.md)
