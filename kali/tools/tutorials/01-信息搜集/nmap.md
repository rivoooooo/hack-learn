# nmap（端口扫描与资产测绘的基准工具）

> **一句话**：探测目标主机是否在线、开放了哪些端口、跑着什么服务与版本、是什么操作系统。
> **分类**：信息搜集 ｜ **Kali 包**：`nmap` ｜ **官方文档**：<https://nmap.org/book/man.html>

## 1. 它解决什么问题

任何一次渗透测试或应急排查，第一步都是回答同一组问题：**这台机器活着吗？开了哪些端口？上面跑的是什么？**

nmap 一次把这几件事都做了，并且是同类工具里的"事实标准"：

| 工具 | 定位 | 什么时候用 |
|------|------|-----------|
| **nmap** | 功能最全，服务/系统识别 + 脚本引擎 | 默认选择，需要准确结论时 |
| [masscan](masscan.md) | 无状态异步扫描，追求"一个网段多快扫完" | 先快速摸清"哪些 IP:端口 是开的"，再来 nmap 精扫 |
| [netdiscover](netdiscover.md) / [arp-scan](arp-scan.md) | 二层 ARP 发现 | 只想知道同网段有哪些主机，不发 TCP 包 |
| [fping](../02-漏洞分析/fping.md) | 纯 ICMP 批量存活探测 | 只需要存活列表，不需要端口 |
| [hping3](hping3.md) | 手工构造单个数据包 | 需要自定义 TCP 标志位、绕过简单过滤 |

一句话选型：**广域网段先 masscan 出"活口清单"，再对活口用 nmap 做精细扫描。**

## 2. 工作原理

nmap 的核心是"发一个精心构造的探测包，从回包推断状态"。以最常用的 SYN 扫描（`-sS`）为例：

```text
       nmap（攻击机）                         目标主机
            |                                     |
            |---- TCP SYN  ->  tcp/80 ----------->|   （半开连接，不发 ACK）
            |                                     |
       +----+-------------------------------------+----+
       | 收到 SYN/ACK  -> 端口 open（立刻发 RST 断开） |
       | 收到 RST/ACK  -> 端口 closed                 |
       | 没有任何响应  -> 端口 filtered（被防火墙丢包）|
       +----------------------------------------------+
```

不同扫描类型的本质区别在于"用什么包、怎么判断"：

- `-sS` SYN 半开：不发第三次握手，快且不产生完整连接日志（需 root）。
- `-sT` 全连接：调用系统 `connect()`，用普通用户权限也能跑，但慢、且会在目标留下完整连接记录。
- `-sU` UDP：发 UDP 包，靠 ICMP 端口不可达判断 closed，`open|filtered` 情况很多。
- `-sN/-sF/-sX` NULL/FIN/Xmas：设置特殊 TCP 标志位，用于绕过只看 SYN 的简易 ACL。

服务识别（`-sV`）是另一层：拿到开放端口后，nmap 再发送一组探针（banner 抓取 + 特征匹配），把 `80/tcp` 变成 `80/tcp open http nginx 1.24.0`。

扫描流程可以概括成四阶段：

```text
1. 主机发现  ->  -sn / -Pn / -PS / -PE
2. 端口扫描  ->  -sS / -sT / -sU，配合 -p、--top-ports
3. 服务识别  ->  -sV（+ -O 系统识别）
4. NSE 脚本  ->  --script 执行 Lua 脚本做漏洞探测/枚举
```

nmap 还有一套脚本引擎 **NSE**（Nmap Scripting Engine），脚本按类别组织：`default`、`safe`、`discovery`、`vuln`、`brute`、`exploit` 等。`-sC` 等价于 `--script=default`。

## 3. 安装与快速上手

```bash
sudo apt install nmap
nmap --help | head -30
nmap --version
```

最小可用命令：

```bash
# 1) 扫最常见的 1000 个端口（默认行为）
nmap 192.168.56.101

# 2) 常用"体检"组合：版本+默认脚本+系统+路由，4 档速度
nmap -A -T4 192.168.56.101

# 3) 全端口 + 不 ping（穿透禁 ICMP 的主机）
nmap -p- -Pn -T4 192.168.56.101
```

> 只在**你有授权的目标**上扫描。公网上只有 `scanme.nmap.org` 是 nmap 官方明确允许扫描的练习目标，且要求低频率（`-T2` 或更低）。

## 4. 核心参数详解

### 目标指定

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `192.168.56.0/24` | CIDR 网段 | 内网摸排首选 |
| `192.168.56.1-20` | 地址范围 | 少量不连续主机 |
| `-iL hosts.txt` | 从文件读目标（每行一个） | masscan/其他工具输出的清单直接喂进来 |
| `-iR 100` | 随机选 100 个公网 IP | 仅用于研究扫描引擎，别拿来做"攻击" |
| `--exclude 10.0.0.1,10.0.0.5` | 排除指定主机 | 剔除网关、打印机等易被打挂的设备 |
| `--excludefile skip.txt` | 从文件排除 | 大批量任务的排除清单 |

### 主机发现

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-sn` | 只做 ping 扫描，不扫端口 | 快速拿存活主机清单；比 `-p-` 快一个数量级 |
| `-Pn` | 跳过主机发现，直接扫端口 | 目标禁 ICMP/禁 ping 时必加，否则会误报"主机 down" |
| `-PS22,80,443` | TCP SYN 方式探测这些端口 | 穿透只封 ICMP 的防火墙 |
| `-PE` / `-PP` | ICMP echo / timestamp 探测 | 传统 ping 发现 |
| `-n` | 不做 DNS 反向解析 | 扫大网段时显著提速 |
| `-R` / `--dns-servers` | 强制反解 / 指定 DNS 服务器 | 需要主机名情报时 |

### 端口与扫描类型

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-p 22,80,443` | 指定端口 | 精确复核 |
| `-p-` | 全部 65535 个端口 | 会慢很多；建议先 masscan 再 nmap 复核 |
| `-p 1-1024` / `-p U:53,T:80` | 范围 / 混合协议 | 按需组合 |
| `--top-ports 100` | 只扫最常见的 N 个端口 | 快速普查 |
| `-F` | 快速模式（= `--top-ports 100`） | 时间紧时的默认选择 |
| `-sS` | SYN 半开扫描（默认，需 root） | 首选，快且隐蔽性相对好 |
| `-sT` | 全连接扫描 | 无 root 权限时使用 |
| `-sU` | UDP 扫描 | DNS/SNMP/NTP 必扫，但慢，配 `--top-ports` 限制 |
| `-sN/-sF/-sX` | NULL/FIN/Xmas 扫描 | 绕过只看 SYN 的简易过滤 |
| `-sA` | ACK 扫描 | 专门用来**判断防火墙规则集**，不能判断端口开放 |

### 识别与脚本

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-sV` | 服务与版本识别 | 有版本才有后续 `searchsploit` |
| `--version-intensity 0-9` | 版本探测强度 | 0=最轻（`--version-light`），9=最全 |
| `-O` | 操作系统识别 | 需要至少一个开放+一个关闭的端口 |
| `--osscan-guess` / `--osscan-limit` | 大胆猜测 / 只在有把握时猜 | 前者提高命中率也提高误报率 |
| `-A` | = `-sV -O -sC --traceroute` | 一句话拿到最多信息，噪声也最大 |
| `-sC` | 运行 default 类脚本 | 等价 `--script=default` |
| `--script vuln` | 运行漏洞类脚本 | 高风险，可能触发告警甚至影响服务 |
| `--script-args k=v` | 给脚本传参 | 如 `--script-args=smbuser=guest` |
| `--script-updatedb` | 更新脚本数据库 | 安装新脚本包后执行 |

### 性能与规避

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-T0`…`-T5` | 时间模板（数字越大越快） | 默认 T3；授权内网用 T4；脆弱设备/公网用 T2 |
| `--min-rate 1000` | 每秒至少发 1000 个包 | 比 `-T4` 更可控的提速方式 |
| `--max-rate 500` | 限速上限 | 保护老旧设备，避免打挂 |
| `--max-retries 1` | 减少重传 | 网络稳定时提速 |
| `--host-timeout 5m` | 单主机超时 | 避免卡在某个不响应主机上 |
| `--scan-delay 100ms` | 探针间隔 | 绕过基于速率的 IDS |
| `-f` / `--mtu 8` | 分片 | 规避简单包过滤 |
| `-D RND:10` | 用 10 个随机诱饵 | 混淆来源，几乎只在红队场景使用 |
| `--source-port 53` | 伪装源端口 | 绕过"只放行 DNS"的规则 |

### 输出

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-oN out.txt` | 普通文本 | 人看 |
| `-oX out.xml` | XML | 喂给 Metasploit/后续工具 |
| `-oG out.gnmap` | grepable | 老脚本处理 |
| `-oA base` | 一次输出三种格式 | 推荐，后续想用哪种都行 |
| `--open` | 只显示开放的端口 | 结果干净，建议默认加上 |
| `--reason` | 显示判断依据（syn-ack/rst 等） | 排查误报时必加 |
| `-v` / `-vv` | 实时输出进度 | 全端口扫描时看进度 |

## 5. 实战演练

**环境**：以下全部在本地实验环境执行，不涉及任何未授权目标。

- 靶机 A：`192.168.56.101`（Metasploitable2 虚拟机）
- 靶机 B：`192.168.56.102`（DVWA 容器，`docker run -d -p 8080:80 vulnerables/web-dvwa`）
- 攻击机：Kali（`eth1` = 192.168.56.10，Host-Only 网络）

> 若你想复现，可自建 VirtualBox Host-Only 网络，或对 `scanme.nmap.org` 做低频扫描。

### 场景 1：摸清网段有哪些主机（轻量第一步）

```bash
sudo nmap -sn 192.168.56.0/24
```

预期输出片段：

```text
Nmap scan report for 192.168.56.1
Host is up (0.0011s latency).
Nmap scan report for 192.168.56.10
Host is up (0.00032s latency).
Nmap scan report for 192.168.56.101
Host is up (0.00051s latency).
Nmap scan report for 192.168.56.102
Host is up (0.00048s latency).
```

解读：`-sn` 不发端口探测，只回答"哪些 IP 活着"。这一步通常是渗透流程中"发现主机"的第一个动作，几秒钟就能画出资产轮廓。

### 场景 2：对单个靶机做体检式扫描

```bash
sudo nmap -sS -sV -sC -O --open -T4 -oA recon_target_a 192.168.56.101
```

预期输出片段（节选）：

```text
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
80/tcp   open  http        Apache httpd 2.2.8 ((Ubuntu) DAV/2)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X
3306/tcp open  mysql       MySQL 5.0.51a-3ubuntu5
| mysql-info:
|   Protocol: 10
|   Version: 5.0.51a-3ubuntu5
...
|_http-title: Metasploitable2 - Linux

OS details: Linux 2.6.9 - 2.6.33
```

解读：
- `vsftpd 2.3.4` 是著名的"笑脸后门"版本（CVE-2011-2523），直接记下来去 `searchsploit` 查。
- `-sC` 带来了 `mysql-info`、`http-title` 等额外情报，省下手工探测。
- `-oA recon_target_a` 生成 `recon_target_a.nmap/.xml/.gnmap` 三个文件，XML 后面可以导进 Metasploit。
- 输出末尾会有一句提示本次扫描耗时，全端口扫描时这个时间会很可观。

### 场景 3：大面积网段的"先粗后细"策略

第一步，用 masscan 快速拿到全端口开放清单（详见 [masscan.md](masscan.md)）：

```bash
sudo masscan 192.168.56.0/24 -p1-65535 --rate 2000 -oL masscan_ports.txt
```

第二步，只对确认开放的端口用 nmap 做服务识别：

```bash
awk '{print $4}' masscan_ports.txt | sort -u > live_hosts.txt
sudo nmap -sV -sC -Pn -iL live_hosts.txt --open -T4 -oA recon_all
```

解读：直接对 /24 网段跑 `nmap -p- -sV` 可能要几十分钟；masscan 用异步发包几分钟就能出"活口表"，nmap 只做精扫。这是实战里最常见的分工。

### 场景 4（进阶）：用 NSE 脚本做专项枚举

```bash
# SMB 相关枚举
sudo nmap -p445 --script "smb-os-discovery,smb-enum-shares,smb-enum-users" 192.168.56.101

# HTTP 常见信息
nmap -p80 --script "http-title,http-headers,http-methods" 192.168.56.102

# 漏洞类脚本（慎用，可能触发告警/影响服务）
sudo nmap -p445 --script vuln 192.168.56.101
```

预期输出片段：

```text
| smb-enum-shares:
|   account_used: guest
|   \\192.168.56.101\IPC$:
|     Type: STYPE_IPC_HIDDEN
|   \\192.168.56.101\tmp:
|     Type: STYPE_DISKTREE
|     Anonymous access: READ/WRITE
|_    Current user access: READ/WRITE
```

解读：`Anonymous access: READ/WRITE` 意味着匿名可读写共享，是典型的高危配置错误，应立刻记录并在报告中标注。

## 6. 输出解读

| 字段 | 含义 | 下一步动作 |
|------|------|-----------|
| `STATE` = `open` | 有服务在监听 | 记录端口 + 服务版本 |
| `STATE` = `closed` | 主机在，端口无监听 | 一般忽略；可用于 `-O` 系统识别 |
| `STATE` = `filtered` | 被防火墙丢包/丢弃 | 换 `-sA`、换源端口、分片后再试 |
| `STATE` = `open|filtered` | 无法区分（常见于 UDP） | 用 `-sV` 或专用 UDP 脚本进一步确认 |
| `VERSION` 列 | 服务名 + 版本号 | 直接拿去 `searchsploit` 查 EXP |
| `OS details` | 系统识别结果 | 决定后续 Payload 平台 |
| `|_http-title` 等 | NSE 脚本附加信息 | 往往直接暴露 CMS/后台入口 |
| `Host script results` | 主机级脚本结论 | SMB/NetBIOS/SMTP 枚举结论常在这里 |

把输出变成动作的典型链路：

```text
nmap -sV  ->  得到 "vsftpd 2.3.4"
          ->  searchsploit vsftpd 2.3.4
          ->  得到 Metasploit 模块 exploit/unix/ftp/vsftpd_234_backdoor
          ->  msfconsole 加载模块验证
```

## 7. 与其他工具配合

```bash
# 1) masscan 发现 -> nmap 精扫
sudo masscan 10.0.0.0/24 -p1-65535 --rate 3000 -oL m.txt
awk '{print $4}' m.txt | sort -u > hosts.txt
sudo nmap -sV -iL hosts.txt -oA fine --open

# 2) nmap XML -> Metasploit 数据库
msfconsole -q -x 'db_import /path/recon_target_a.xml; hosts; services'

# 3) nmap -oG -> 快速提取开放端口
nmap -sS -oG - 192.168.56.101 | awk '/Ports:/{print $0}'

# 4) nmap 端口结果 -> whatweb / nikto 复核 HTTP
nmap -p80,443 --open -oG - 192.168.56.102 | grep -q 80 && \
  whatweb http://192.168.56.102:8080
```

也可以和 [fping](../02-漏洞分析/fping.md) 配合：先用 fping 拿存活清单，再 `nmap -iL` 扫端口。

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `QUITTING! ... requires root privileges` | 用了 `-sS`/`-O`/`-sU` 等需要 raw socket 的选项 | 加 `sudo`，或改用 `-sT` |
| 所有主机都显示 `Host seems down` | 目标禁 ICMP/禁 ping | 加 `-Pn` |
| 扫描结果里出现大量 `filtered` | 防火墙丢包或速率限制 | 降速 `-T2`、`--max-rate 100`、加 `--scan-delay`；或换 `--source-port 53` |
| 全端口扫描跑到一半卡住 | 某主机不响应导致重传 | 降低 `--max-retries`，加 `--host-timeout 5m` |
| `-sV` 报 `service fingerprint` 超时 | 服务响应慢或受速率限制 | 用 `--version-intensity 2`、`-T2` |
| 同一台机器两次扫描结果不同 | 网络抖动 / 服务负载 | 加 `--reason` 看判断依据，重要结论二次确认 |
| 目标设备被打挂（嵌入式/工控设备） | 发包速率过高 | 用 `-T1`/`-T2`、`--max-rate 10`；生产网慎扫 |
| `--script vuln` 触发了告警 | NSE 漏洞脚本特征明显 | 明确授权后再用，并提前告知防守方 |

## 9. 防御视角（蓝队）

- **检测**：SYN 扫描的典型特征是"大量半开连接"——短时间内同一源 IP 对多端口只发 SYN 不回 ACK。IDS 规则（Suricata/Snort）可对 `SYN` 无后续 `ACK` 的比例做阈值告警。
- **主机侧**：`netstat`/`ss` 里不会有完整连接，但防火墙日志能记录被拒绝的 SYN。Linux 上可看 `iptables -L -v -n` 的计数增长。
- **缓解**：
  - 默认拒绝（default-deny）入站策略，只放行必要端口，让扫描结果全是 `filtered`。
  - 开启 SYN cookies、限制 `tcp_syn` 半开连接数（`net.ipv4.tcp_max_syn_backlog`、`sysctl net.ipv4.tcp_syncookies=1`）。
  - 用 fail2ban 或防火墙 connlimit 对高频扫描源做临时封禁。
  - 关闭不必要的服务与 banner：少暴露一份版本号，就少一条 `searchsploit` 命中。
- **隐蔽性提示**：`-T0`/`-T1` 的慢速扫描很难靠速率阈值发现，蓝队更应关注"**同一源 IP 对同一网段的多台主机做相同端口序列探测**"这种模式。

## 10. 参考

- 官方参考手册（通读一遍就够用一辈子）：<https://nmap.org/book/man.html>
- NSE 脚本库：<https://nmap.org/nsedoc/>
- 官方允许扫描的练习目标：<https://scanme.nmap.org/>
- man page：`man nmap`
- man page（脚本引擎）：`man nmap-scripts`

---

**相关教程**：[masscan](masscan.md) ｜ [fping](../02-漏洞分析/fping.md) ｜ [netdiscover](netdiscover.md) ｜ [arp-scan](arp-scan.md) ｜ [hping3](hping3.md) ｜ [whatweb](whatweb.md) ｜ [searchsploit](../02-漏洞分析/searchsploit.md) ｜ [nikto](../02-漏洞分析/nikto.md)
