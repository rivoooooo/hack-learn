# 07 · 嗅探与欺骗（Sniffing & Spoofing）

本目录覆盖 Kali 中在网络层与应用层「观察流量」和「改变流量」的工具。

```text
                    嗅探（观察）                欺骗（改变）
                 ─────────────────         ─────────────────
网络层            tcpdump / Wireshark        ettercap / macchanger
                 （抓包、协议分析）          （ARP 投毒、MAC 伪装）
                          ↓                          ↓
应用层            Wireshark（HTTP/TLS）       mitmproxy（HTTP/HTTPS）
                          ↓                          ↓
名称解析          Wireshark / tcpdump         responder（LLMNR/NBT-NS）
```

**核心心智模型**：

| | 嗅探 | 欺骗 |
| --- | --- | --- |
| 做什么 | 被动接收、记录、分析 | 主动发送伪造的数据 |
| 网络层可见性 | ⚠️ 基本不可检测（纯被动） | ⚠️ **可检测**（有流量特征） |
| 法律性质 | 截获通信 | 主动干预通信 |

**⭐ 本目录最重要的一个事实**：

> **在交换网络中，你默认只能看到自己的流量。**
> 「看到别人的流量」需要主动手段（端口镜像 / ARP 投毒），而 ARP 投毒**只在你自己拥有或明确授权的网络上才合法**。
>
> 详见 [ettercap](ettercap.md) 与 [bettercap](../05-无线攻击/bettercap.md)。

## 工具清单

| 工具 | 一句话 | 难度 | 教程 |
| --- | --- | --- | --- |
| `tcpdump` | 命令行抓包，BPF 过滤器在内核执行，服务器抓包首选 | ★★ | [tcpdump.md](tcpdump.md) |
| `wireshark` / `tshark` | 逐层协议解剖、流跟踪、统计、解密（含 tshark 命令行） | ★★ | [wireshark.md](wireshark.md) |
| `ettercap` | ARP/ICMP/DHCP/NDP 投毒 + 凭据解析 + etterfilter 内容篡改 | ★★★ | [ettercap.md](ettercap.md) |
| `responder` | LLMNR/NBT-NS/mDNS 投毒，捕获 NetNTLM 哈希 | ★★ | [responder.md](responder.md) |
| `mitmproxy` | HTTP/HTTPS 中间人代理，拦截修改、Replay、Python 脚本 | ★★ | [mitmproxy.md](mitmproxy.md) |
| `macchanger` | 查看/修改网卡 MAC | ★ | [macchanger.md](macchanger.md) |
| `bettercap`（跨目录） | 模块化 MITM 框架，ARP/DNS 投毒 + Wi-Fi + REST API | ★★★ | [../05-无线攻击/bettercap.md](../05-无线攻击/bettercap.md) |

## 学习顺序

**第 1 步 · 先学会「看」（完全合法，且是后续一切的基础）**

1. [tcpdump.md](tcpdump.md) —— 学会抓包与 **BPF 过滤器**。这是「网络可见性」的入口。
2. [wireshark.md](wireshark.md) —— 学会**显示过滤器**与协议树。**重点看第 2.2 节「捕获过滤器 vs 显示过滤器」的对照表**——这是初学者最容易混淆的地方。

**⭐ 这两篇是纯「观察」技能**，你在自己的设备上用完全合法。**把它们练熟再考虑下一步。**

**第 2 步 · 理解「网络层发生了什么」**

3. [macchanger.md](macchanger.md) —— 短小但知识点密集：**MAC → 厂商 → 设备类型**的侦察思路；MAC 不是安全边界。

**第 3 步 · 应用层（最有实际价值的方向）**

4. [mitmproxy.md](mitmproxy.md) —— ⭐ **推荐重点学**。在自己的设备上设置代理分析自己的流量，是**完全合法且实用**的技能（API 调试、Web 安全测试、App 分析）。

**第 4 步 · 名称解析投毒（内网渗透中成功率最高的一类）**

5. [responder.md](responder.md) —— 先看 **2.1 节**理解 LLMNR/NBT-NS/mDNS 的缺陷，再学**场景 1（`-A` 分析模式）**。它展示了一个几乎每个 Windows 网络都存在的问题。

**第 5 步 · 网络层 MITM（法律风险最高，务必读法律章节）**

6. [ettercap.md](ettercap.md) —— 先读 **第 2 节原理**，再读**第 9 节防御**（有完整的交换机配置示例）。
7. [../05-无线攻击/bettercap.md](../05-无线攻击/bettercap.md) —— 现代替代方案，更容易自动化。

**第 6 步 · 红蓝对抗演练**

把「攻击」和「防御」连起来：

```bash
# 终端 1（红队）：ettercap 做 ARP 投毒
sudo ettercap -T -q -i eth0 -M arp:remote /<靶机IP>/ /<网关IP>/

# 终端 2（蓝队）：用 arpwatch 检测
sudo arpwatch -i eth0

# 终端 3（分析）：tcpdump 记录一切
sudo tcpdump -i eth0 -w /tmp/evidence.pcap

# 观察：arpwatch 是否告警？tcpdump 里能否看到「同一 IP 对应两个 MAC」？
```

**这个演练的价值无可替代**——它让你理解「攻击长什么样」和「如何被发现」。

## 环境准备

### 硬件

本目录的工具对硬件要求**很低**（不像 05 无线攻击需要特定网卡）：

| 工具 | 要求 |
| --- | --- |
| tcpdump / Wireshark | 任何网卡；虚拟机也能用 |
| mitmproxy | 任何网卡；**会自己起代理服务** |
| macchanger | 大多数网卡；⚠️ 部分虚拟网卡/驱动受限 |
| ettercap / responder | ⚠️ **需要能看到目标的流量** → 必须在同一广播域 |

### 实验环境（**最关键**）

**交换网络的现实**：

```
[主机 A] ──── [交换机] ──── [主机 B]
                 │
            [你的 Kali]
            ← ARP 投毒前：只能看到广播 + 自己的流量
            ← ARP 投毒后：能看到 A↔B 的流量（但只在你自己网络上才合法）
```

**三种环境对比**：

| 环境 | 能否看到别人的流量 | 合法性 |
| --- | --- | --- |
| **host-only 虚拟网络**（你的 Kali + 你的靶机） | ✅ | ✅ **推荐** |
| **你自己完全掌控的物理隔离 VLAN** | ✅ | ✅ |
| 公司/家庭/公共网络 | ❌ 不要试 | ❌ **违法** |

**推荐的最小环境**：

```text
VirtualBox host-only 网络 192.168.56.0/24
├── Kali（攻击机/分析机）
│   └── 网络设置 → 高级 → 混杂模式 → 「允许全部」
└── 靶机（Metasploitable2 / 自建 Windows 虚拟机 / 自建 Linux 服务）
```

**⚠️ 虚拟机的常见坑**：

```
❌ 抓不到包 → 忘了开混杂模式
    VirtualBox：设置 → 网络 → 高级 → 混杂模式 → 「允许全部」
    VMware：网络适配器 → 勾选混杂模式
```

### 工具安装

```bash
sudo apt install tcpdump wireshark wireshark-common tshark \
                 ettercap-text-only etterfilter etterlog \
                 responder mitmproxy macchanger arpwatch
```

**Wireshark 的权限配置（必做）**：

```bash
sudo dpkg-reconfigure wireshark-common    # 选 Yes
sudo usermod -aG wireshark $USER
newgrp wireshark
```

**⭐ 为什么要配这个**：**不要用 root 跑 Wireshark**——它有几万个解析器（大量 C 代码），历史上出现过很多解析漏洞。用普通用户 + capability 是正确模型。

**ettercap 的包拆分**：

```bash
sudo apt install ettercap-text-only      # 纯文本版（无图形依赖，推荐）
# 或
sudo apt install ettercap-graphical       # GTK 版
```

### 证书准备（mitmproxy）

```bash
# 启动一次，自动生成 CA
mitmproxy &
sleep 2
kill %1

ls -la ~/.mitmproxy/
# mitmproxy-ca-cert.pem   ← 用于安装到客户端信任库
# mitmproxy-ca-key.pem    ← ⚠️ 私钥，绝不要泄露！

# 保护私钥
chmod 600 ~/.mitmproxy/mitmproxy-ca-key.pem
```

**⭐ 一个必须记住的安全要点**：

> **`~/.mitmproxy/mitmproxy-ca-key.pem` 是一个「万能钥匙」**——
> 持有它就能为**任意域名**签发证书。
>
> 泄露它的后果不是「你的数据泄露」，而是「**所有信任该 CA 的设备的通信都变得可伪造**」。
>
> 绝不提交到 git，绝不外传，测试后从设备上卸载 CA。

### 靶场

| 靶场 | 适合练什么 |
| --- | --- |
| **你自己的 Kali + 一台靶机（host-only）** | ⭐ **够用**。ARP 投毒、抓包、分析 |
| **自建 Windows 虚拟机** | ⭐ [responder](responder.md) 的 NetNTLM 捕获、SMB 签名检查 |
| **DVWA / Juice Shop** | [mitmproxy](mitmproxy.md) 的拦截修改、越权测试 |
| **Metasploitable2** | 明文协议（FTP/Telnet）的凭据嗅探 |
| **公开的示例 pcap** | ⭐ **零风险**。见 Wireshark 官方示例：<https://wiki.wireshark.org/SampleCaptures> |
| **你自己的工作站点** | [mitmproxy](mitmproxy.md) 分析自己的 API |

## 技术速查

### 按需求选工具

| 你要做什么 | 用谁 |
| --- | --- |
| 在服务器上抓包落盘 | ⭐ [tcpdump](tcpdump.md) |
| 打开一个 pcap 逐层分析 | ⭐ [wireshark](wireshark.md) |
| 脚本化提取字段/统计 | ⭐ [wireshark](wireshark.md) 的 `tshark -T fields` |
| 看 HTTP/HTTPS 的**内容** | ⭐ [mitmproxy](mitmproxy.md) |
| 让流量经过我（同一网段） | [ettercap](ettercap.md) / [bettercap](../05-无线攻击/bettercap.md) |
| 抓 NetNTLM 哈希 | ⭐ [responder](responder.md) |
| 改 MAC | [macchanger](macchanger.md) |
| 从 pcap 里提取明文凭据 | ⭐ [ettercap](ettercap.md) 的 `-r` 模式（**不需要 MITM！**） |
| 检测 ARP 投毒 | `arpwatch` / [tcpdump](tcpdump.md) `-e 'arp.opcode == 2'` |

### 常用命令速查

```bash
# ---------- 抓包 ----------
sudo tcpdump -i eth0 -nn -c 20                        # 抓 20 个包
sudo tcpdump -i eth0 -w cap.pcap -C 100 -W 20         # 环形缓冲（最多 2GB）
sudo tcpdump -i eth0 -nn -A 'tcp port 80'             # 看 HTTP 明文
sudo tcpdump -i eth0 -nn -e 'arp.opcode == 2'         # 看 ARP 应答（含 MAC）

# ---------- 分析 ----------
capinfos -A cap.pcap                                  # 先看文件信息
tshark -r cap.pcap -Y 'http.request' -T fields -e http.host -e http.request.uri
wireshark cap.pcap                                    # GUI 深入分析
tshark -r cap.pcap --export-objects http,./out/       # 从 pcap 里捞文件

# ---------- 离线提取凭据（不需要 MITM）----------
sudo ettercap -T -q -r cap.pcap -L parsed.log
etterlog -p parsed.log                                # ⭐ 一键提取凭据

# ---------- MITM（⚠️ 仅自有/授权网络）----------
sudo ettercap -T -q -i eth0 -M arp:remote /<靶机>/ /<网关>/

# ---------- 名称解析投毒 ----------
sudo responder -I eth0 -A                             # ⭐ 只分析，不投毒（最安全）
sudo responder -I eth0 -w -v                          # 投毒 + WPAD

# ---------- 应用层代理（分析自己的流量）----------
mitmproxy                                             # TUI
mitmweb                                               # Web UI
mitmdump -s script.py                                 # 脚本化

# ---------- MAC ----------
macchanger -s eth0                                    # 查看
sudo ip link set eth0 down && sudo macchanger -a eth0 && sudo ip link set eth0 up
```

### 关键协议速查

| 协议 | 端口 | Responder 相关 | 说明 |
| --- | --- | --- | --- |
| LLMNR | UDP 5355 | ⭐ 投毒目标 | 无认证的局域网名称解析 |
| NBT-NS | UDP 137 | ⭐ 投毒目标 | NetBIOS 名称解析 |
| mDNS | UDP 5353 | ⭐ 投毒目标 | Bonjour 风格 |
| WPAD | TCP 80 / 3141 | ⭐ 投毒目标 | 代理自动发现（DNS 里常没有记录）|
| SMB | TCP 445 | ⭐ 凭据主要来源 | Windows 自动认证 |
| Kerberos | TCP/UDP 88 | 中继目标 | — |
| LDAP | TCP 389 | 中继目标 | 应改用 636 (LDAPS) |
| ARP | — | — | **无认证** → [ettercap](ettercap.md) 的投毒基础 |

### 哈希类型速查（从 [responder](responder.md) 到 [hashcat](../04-口令攻击/hashcat.md)）

| 类型 | hashcat `-m` | 说明 |
| --- | --- | --- |
| NetNTLMv1 | **5500** | ⚠️ 弱得多（48 位有效熵） |
| NetNTLMv2 | **5600** | Vista+ 默认 |
| NTLM（裸哈希） | **1000** | 不是「响应」，是哈希值本身 |

**⭐ 最常见的错误**：把 NetNTLMv2 用 `-m 1000` 去破——**模式号写错不会报错，只会一直跑不出结果**。用 `hashcat --identify` 确认。

## 防守速查（本目录的另一半价值）

> **本目录的每个工具都对应一项防御措施。** 这是最该带走的东西。

| 攻击 | 防御 | 优先级 |
| --- | --- | --- |
| **ARP 投毒**（[ettercap](ettercap.md)） | ⭐ **DHCP Snooping + Dynamic ARP Inspection（DAI）** | ⭐⭐⭐ |
| **DHCP 投毒** | DHCP Snooping + 端口安全 | ⭐⭐⭐ |
| **IPv6 NDP 投毒** | RA Guard；不需要 IPv6 就**关掉** | ⭐⭐⭐ |
| **LLMNR/NBT-NS 投毒**（[responder](responder.md)） | ⭐ **禁用 LLMNR + NBT-NS + mDNS**（组策略） | ⭐⭐⭐ |
| **NTLM 中继** | ⭐ **启用 SMB 签名 + LDAP 签名** | ⭐⭐⭐ |
| **NetNTLMv2 捕获** | 禁用 NTLM（迁到 Kerberos）；服务账户用 gMSA | ⭐⭐ |
| **明文凭据嗅探** | ⭐ **全程 TLS**：HTTPS / SSH / SFTP / IMAPS / SMTPS / LDAPS / SNMPv3 | ⭐⭐⭐ |
| **HTTPS 中间人**（[mitmproxy](mitmproxy.md)） | ⭐⭐ **证书固定（pinning）** + HSTS preload + 禁止装用户 CA | ⭐⭐⭐ |
| **内容篡改**（etterfilter） | HSTS + **SRI（子资源完整性）** + **CSP** | ⭐⭐ |
| **MAC 欺骗**（[macchanger](macchanger.md)） | ⭐ **不要用 MAC 做访问控制**；改用 802.1X + EAP-TLS | ⭐⭐⭐ |
| **流量丢弃干扰** | 难以直接防（靠监控发现） | ⭐ |
| **WPAD 劫持** | 在 DNS 里加 `wpad` 记录（变相防御）+ 禁用浏览器自动发现代理 | ⭐⭐ |

### 五条最高 ROI 的措施

```text
1. DHCP Snooping + Dynamic ARP Inspection
   → 彻底阻断 ARP/DHCP 投毒

2. 组策略禁用 LLMNR / NBT-NS / mDNS
   → 让 Responder 完全没有攻击面

3. 启用 SMB 签名（+ LDAP 签名）
   → 让 NTLM 中继失效

4. 全程 HTTPS + HSTS preload + 移动 App 证书固定
   → 让凭据嗅探与内容篡改失效

5. 不用 MAC 做访问控制，改用 802.1X + EAP-TLS
   → 让 MAC 欺骗失去价值
```

### 检测手段

| 要检测 | 用什么 | 关键信号 |
| --- | --- | --- |
| **ARP 投毒** | `arpwatch` / [tcpdump](tcpdump.md) | ⭐ **同一 IP 出现两个 MAC** |
| **LLMNR/NBT-NS 投毒** | [tcpdump](tcpdump.md) / Zeek | 大量多播应答来自非 DNS 服务器的 IP |
| **明文凭据** | [tcpdump](tcpdump.md) / [wireshark](wireshark.md) | 出现 `Authorization:` / `USER` / `PASS` |
| **数据外传** | [wireshark](wireshark.md) `-z conv` | 内网主机向陌生公网 IP 传大量数据 |
| **C2 心跳** | [wireshark](wireshark.md) | 固定间隔的小包 |
| **DNS 隧道** | [wireshark](wireshark.md) | 超长域名 / 大量 TXT 查询 |
| **Kerberoasting** | [wireshark](wireshark.md) | 大量 `kerberos.msg_type == 30` |
| **HTTPS 中间人** | 证书审计 / JA3 指纹 / CT 日志 | 异常的 CA、TLS 指纹与 UA 不匹配 |

**⭐ 一行检测 ARP 投毒**：

```bash
sudo tcpdump -i eth0 -nn -e 'arp.opcode == 2' 2>/dev/null | \
  awk '{print $(NF-2), $NF}' | sort -u | \
  awk '{c[$1]++; m[$1]=m[$1]" "$2} END {for (i in c) if (c[i]>1) print "⚠️ ARP 投毒?", i, m[i]}'
```

## 法律与伦理（**必读**）

### 三个层次的法律风险

| 层次 | 行为 | 法律性质 |
| --- | --- | --- |
| **观察** | tcpdump / Wireshark 抓包 | ⚠️ **截获他人通信即违法**——不需要破解或利用 |
| **欺骗** | ARP/DNS/名称解析投毒 | ❌ **主动干预他人通信**——性质更严重 |
| **篡改** | 修改流量内容、伪造认证 | ❌❌ **修改他人数据**——最严重 |

### 核心原则

> **1. 「我只是看看，没有攻击」不是抗辩理由。**
> **2. 「我家的网卡能收到邻居的信号」不是授权。**
> **3. 「我是公司运维」不等于有监控同事流量的授权。**
> **4. 「MAC 是公开的，所以我能用」是错的**——绕过访问控制本身就是违法。
> **5. 「只是学习目的」不构成抗辩。**

### 相关法律责任（中国大陆）

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条 | **非法侵入计算机信息系统罪** / **非法获取计算机信息系统数据罪** |
| 《刑法》 | 第二百八十六条 | **破坏计算机信息系统罪**（投毒导致断网、篡改内容） |
| 《刑法》 | 第二百五十三条之一 | **侵犯公民个人信息罪**（窃取凭据、截获通信内容） |
| 《刑法》 | 第二百六十六条 | 诈骗罪（用假代理/篡改做钓鱼） |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《个人信息保护法》 | 相关条款 | 收集、存储、处理个人信息需有合法性基础 |
| 《数据安全法》 | 相关条款 | 数据处理活动的合规要求 |
| 《治安管理处罚法》 | 相关条款 | 偷窥、窃听他人隐私 |

### 明确允许

- ✅ **抓你自己的流量**（你自己的设备、你自己的网络）——这是开发/运维/安全测试的标准做法
- ✅ **在你自己的设备上设置 mitmproxy 分析自己的流量**
- ✅ **分析公开的示例 pcap**（零风险的学习方式）
- ✅ 你自己搭建的 **host-only 虚拟网络**（只有你的 Kali + 你的靶机）
- ✅ 有**书面授权**、明确列出授权网段/时间窗/攻击类型的渗透测试
- ✅ **被正式授权**的企业安全监控（有政策、有告知、有例外清单）

### 明确禁止

- ❌ 抓取任何非自有、非授权网络的流量
- ❌ 对同事、家人、邻居、顾客的设备抓包
- ❌ **在家庭网络上做 ARP 投毒**（家人的设备不是你的设备）
- ❌ 运行 [responder](responder.md)——**它没有「只针对单个目标」的选项，攻击面是整个广播域**
- ❌ 在别人的设备上安装 CA 证书
- ❌ 在公共网络上开放 `0.0.0.0` 的代理
- ❌ 伪造 MAC 绕过任何非授权网络的访问控制
- ❌ 保留、分析、分享他人的 pcap / flows / 哈希

### 推荐的学习路径（覆盖 100% 知识点，零法律风险）

```text
⭐ 阶段 1：纯分析（完全合法）
   ① 抓你自己的流量：sudo tcpdump -i eth0 -w mine.pcap
   ② 打开公开的示例 pcap：https://wiki.wireshark.org/SampleCaptures
   ③ 用 ettercap -r 离线解析已有 pcap（不做任何 MITM！）
   ④ 用 mitmproxy 分析你自己的 Web 应用流量

   → 能学到：BPF 语法、显示过滤器、协议分析、凭据提取、HTTP 拦截

⭐ 阶段 2：隔离环境（完全隔离）
   ① host-only 虚拟网络 + 你自己的靶机
   ② 在里面做 ARP 投毒、responder 投毒、etterfilter 篡改
   ③ 同时用 arpwatch / tcpdump 做检测，理解「攻击长什么样」

   → 能学到：MITM 全流程、检测手段

⭐ 阶段 3：读防御文档（最有价值）
   ① 交换机 DAI/DHCP Snooping 的配置
   ② 组策略禁用 LLMNR
   ③ 组策略启用 SMB 签名
   ④ 证书固定的实现
   ⑤ 802.1X + EAP-TLS 的部署

   → 这是把「会用工具」变成「能改善安全状况」的关键
```

**⭐ 特别强调「阶段 1 的第 ③ 条」**：

> `sudo ettercap -T -q -r capture.pcap -L parsed.log` 然后 `etterlog -p parsed.log`
>
> **这条命令能提取凭据，但完全不需要 MITM、不投毒、不影响任何网络。**
>
> 它覆盖了 70% 的学习价值（协议解析、凭据提取、etterlog 使用），**法律风险为零**。

### 数据处理合规（针对授权测试人员）

> **即使攻击是授权的，数据处理不当仍然违规。**

| 事项 | 要求 |
| --- | --- |
| 数据分类 | 抓包文件、flows、哈希都是**敏感数据**，按客户的数据分类标准处理 |
| 存储 | 加密存储；**不放在个人设备上** |
| `.gitignore` | 至少确保 `*.pcap`、`*.cap`、`*.mitm`、`cracked.json` 不被误提交 |
| 传输 | 不通过未加密渠道发送 |
| 删除 | 项目结束后按 ROE 规定的期限彻底删除 |
| 报告 | **不包含完整凭据/口令**（除非 ROE 明确要求），用占位符替代 |
| 访问审计 | 谁看过这些数据要有记录 |
| CA 私钥 | ⭐ **绝不外传；测试后从设备上卸载 CA** |

```bash
# 建议加入 .gitignore
cat >> .gitignore <<'EOF'
*.pcap
*.pcapng
*.cap
*.mitm
*.22000
*.kismet
cracked.json
.mitmproxy/
EOF
```

## 相关目录

- [04 · 口令攻击](../04-口令攻击/README.md) —— [hashcat](../04-口令攻击/hashcat.md) `-m 5500`/`-m 5600` 破 NetNTLM；[cewl](../04-口令攻击/cewl.md) 造定向字典
- [05 · 无线攻击](../05-无线攻击/README.md) —— [bettercap](../05-无线攻击/bettercap.md)（模块化 MITM + Wi-Fi）、[kismet](../05-无线攻击/kismet.md)（WIDS 检测）、[airodump-ng](../05-无线攻击/airodump-ng.md)（无线抓包 → [wireshark](wireshark.md) 分析）

## 参考

- Kali 工具分类：<https://www.kali.org/tools/>
- tcpdump 官方：<https://www.tcpdump.org/manpages/pcap-filter.7.html>
- Wireshark 官方：<https://www.wireshark.org/docs/dfref/>
- mitmproxy 官方：<https://docs.mitmproxy.org/>
- Responder 官方：<https://github.com/lgandx/Responder>
- Ettercap 官方：<https://ettercap.github.io/ettercap/>
- Wireshark 示例抓包：<https://wiki.wireshark.org/SampleCaptures>
- 本仓库工具清单来源：`data/kali-tools.tsv`、`data/kali-tools.json`
