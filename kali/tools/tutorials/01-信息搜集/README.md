# 01 · 信息搜集（Information Gathering）工具教程

信息搜集是渗透测试的第一阶段，目标是**在不惊动目标的前提下尽可能画出资产地图**：有哪些域名、哪些 IP、哪些主机、跑着什么服务。

本目录收录 15 个 Kali 官方工具，全部可在 <https://www.kali.org/tools/> 核对到对应包。

## 工具清单

| 工具 | 一句话 | 难度 | 教程 |
|------|--------|------|------|
| `nmap` | 端口扫描与服务/系统识别的基准工具，功能最全 | ★★☆ | [nmap.md](nmap.md) |
| `masscan` | 无状态异步扫描，几分钟扫完一个 B 段 | ★★☆ | [masscan.md](masscan.md) |
| `dnsrecon` | DNS 枚举与区域传输检测，枚举类型最全 | ★★☆ | [dnsrecon.md](dnsrecon.md) |
| `dnsenum` | 多线程 DNS 枚举 + whois 网段推导 | ★★☆ | [dnsenum.md](dnsenum.md) |
| `fierce` | 轻量 DNS 扫描，专找非连续 IP 空间 | ★☆☆ | [fierce.md](fierce.md) |
| `theHarvester` | OSINT 收集：邮箱、子域、主机、员工 | ★★☆ | [theharvester.md](theharvester.md) |
| `recon-ng` | 模块化 Web 侦察框架（工作区 + SQL 数据库） | ★★★ | [recon-ng.md](recon-ng.md) |
| `amass` | OWASP 攻击面测绘与资产图谱，支持长期跟踪 | ★★★ | [amass.md](amass.md) |
| `enum4linux` | Windows/Samba 一键枚举：用户、共享、组、口令策略 | ★★☆ | [enum4linux.md](enum4linux.md) |
| `smbclient` | SMB 共享访问客户端（ftp 风格），验证读写权限 | ★★☆ | [smbclient.md](smbclient.md) |
| `nbtscan` | NetBIOS 名字表扫描，拿主机名/用户名/MAC | ★☆☆ | [nbtscan.md](nbtscan.md) |
| `arp-scan` | 二层 ARP 发现 + 网卡厂商指纹，最可靠的本网段探测 | ★☆☆ | [arp-scan.md](arp-scan.md) |
| `netdiscover` | 主动/被动 ARP 侦察，支持零流量被动监听 | ★☆☆ | [netdiscover.md](netdiscover.md) |
| `hping3` | 自定义 TCP/IP 包构造，做防火墙审计与协议实验 | ★★★ | [hping3.md](hping3.md) |
| `whatweb` | Web 指纹识别，1800+ 插件识别 CMS/框架/版本 | ★☆☆ | [whatweb.md](whatweb.md) |

难度说明：★☆☆ 上手即可用；★★☆ 需要理解参数与场景；★★★ 需要理解协议或框架模型。

## 学习顺序建议

按"从域名到主机，再到服务"的自然顺序推进：

### 第一步：建立网络与 DNS 的基本手感（★☆☆）

1. **[arp-scan](arp-scan.md)** —— 先学会"同网段内最可靠的存活判断"。
2. **[netdiscover](netdiscover.md)** —— 理解被动侦察的价值（零流量、不可检测）。
3. **[fierce](fierce.md)** —— 第一个 DNS 工具，理解区域传输为什么危险。
4. **[whatweb](whatweb.md)** —— 看到一个 Web 服务后该问什么。

### 第二步：把两条主线走通（★★☆）

域名线：
5. **[dnsrecon](dnsrecon.md)** —— DNS 枚举类型全景，学会看输出判断配置问题。
6. **[dnsenum](dnsenum.md)** —— 对比 dnsrecon，学 whois 网段推导。
7. **[theHarvester](theharvester.md)** —— 转向 OSINT（人、邮箱）。

网络线：
8. **[nmap](nmap.md)** —— **核心中的核心**，必须练到能不查手册写出常用组合。
9. **[masscan](masscan.md)** —— 学会"先粗后细"的扫描策略。
10. **[nbtscan](nbtscan.md)** —— Windows 环境的第一步。
11. **[enum4linux](enum4linux.md)** —— SMB 枚举的全流程。
12. **[smbclient](smbclient.md)** —— 从"知道有共享"到"验证能读什么"。

### 第三步：框架与进阶技术（★★★）

13. **[amass](amass.md)** —— 资产图谱思维，长期跟踪资产变化。
14. **[recon-ng](recon-ng.md)** —— 用框架把前面所有工具的结果串起来。
15. **[hping3](hping3.md)** —— 最底层，理解 TCP/IP 与防火墙行为。

## 常见工作流

### 工作流一：外部资产摸排（黑盒）

```text
theHarvester / amass（子域 + 邮箱）
        ↓
dnsrecon / dnsenum（解析 + AXFR）
        ↓
masscan（全端口快扫）
        ↓
nmap -sV（精扫 + 版本）
        ↓
whatweb（Web 指纹）→ searchsploit（找漏洞）
```

### 工作流二：内网主机发现（内网）

```text
arp-scan / netdiscover（二层发现）
        ↓
nmap -sn（跨网段存活）→ nbtscan（NetBIOS 命名）
        ↓
enum4linux（SMB 枚举）→ smbclient（共享访问）
        ↓
nmap -p- -sV（全端口精扫）
```

### 工作流三：可复现的资产管理

```text
amass（长期跟踪）→ 导入 recon-ng 工作区
        ↓
recon-ng 模块串联 + SQL 查询
        ↓
定期 diff 找新增资产
```

## 法律与授权提醒

- **只扫描你有明确书面授权的目标。** 对未授权目标的端口扫描、DNS 爆破、SMB 枚举在很多司法辖区都属于违法行为。
- 合法的练习目标：
  - `scanme.nmap.org`（nmap 官方允许，需低频）
  - `zonetransfer.me`（DigiNinja 提供的区域传输练习域）
  - 你自建的靶场（Metasploitable2 / DVWA / Juice Shop / 本地 bind9 / 自建 Samba）
- 主动类操作（`-brute`、DNS 爆破、共享写入检查）**噪声大且可能影响目标**，务必提前与目标方沟通。

## 与其他分类的衔接

- 拿到指纹后，去 [02-漏洞分析](../02-漏洞分析/README.md) 用 [nuclei](../02-漏洞分析/nuclei.md)、[nikto](../02-漏洞分析/nikto.md)、[searchsploit](../02-漏洞分析/searchsploit.md) 找漏洞。
- 发现 Web 目录结构后，去 [03-Web应用](../03-Web应用/README.md) 用 [gobuster](../03-Web应用/gobuster.md)、[ffuf](../03-Web应用/ffuf.md) 做目录爆破，用 [sqlmap](../03-Web应用/sqlmap.md) 测注入。
