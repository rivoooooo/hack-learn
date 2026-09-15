# scapy（Python 数据包构造与嗅探）

> **一句话**：用 Python 代码把网络协议**一层一层拼出来**再发出去、收回来——「发一个自定义 ICMP、构造一个畸形 TCP、解剖一个捕获的包、做一次 ARP 扫描」都是几行代码；它不是「某个扫描器」，而是**一个让你自己写扫描器的库**。
> **分类**：嗅探与欺骗 / 数据包构造与解析 ｜ **Kali 包**：`python3-scapy`（命令 `scapy`、`scapy3`）｜ **官方文档**：<https://www.kali.org/tools/scapy/> ｜ 上游：<https://scapy.net>、<https://scapy.readthedocs.io>

---

## 1. 它解决什么问题

有一类需求，**用现成工具做不了，因为「要发的包」根本不存在现成的工具**：

- 想发一个**半开的 TCP 连接**（只发 SYN，看有没有 SYN-ACK）→ 没有现成命令；
- 想构造一个**故意畸形的包**（坏长度、错误校验和、非法的 TCP 标志组合）→ 需要自己拼字节；
- 想发一个**特定 TTL 的 ICMP** 做 traceroute，并且**同时看回包是从哪一跳来的** → 需要自己解析 ICMP 载荷里的原始 IP 头；
- 想**批量发 ARP 请求**做主机发现并收集 MAC → 自己写逻辑；
- 想**解析一个 pcap 里的每个包**，按自己的规则统计/改写 → 需要类库。

**Scapy 的定位就是「自己写」**：

| 需求 | 现成工具 | **Scapy** |
|------|----------|-----------|
| 标准端口扫描 | `nmap` | 可以写，但没必要 |
| **自定义/畸形包** | 基本没有 | **核心能力** |
| **协议级实验** | 很受限 | **任意层任意字段** |
| **pcap 解析与改写** | `tshark`（功能固定） | **用 Python 逻辑任意处理** |
| **协议模糊测试** | `boofuzz` 等 | Scapy 是常用底层库 |
| **快速自动化** | 脚本调 `nmap` 解析输出（脆弱） | **直接拿到结构化对象** |

**对比同类**：

| 工具 | 定位 | 差异 |
|------|------|------|
| **Scapy** | **任意协议构造/解析库（Python）** | 最灵活；**要自己写逻辑**；慢于专用工具 |
| **`hping3`** | 命令行自定义包发送 | 好用但**字段组合有限**；见 [`../01-信息搜集/hping3.md`](../01-信息搜集/hping3.md) |
| **`nmap`** | 专业扫描器 | **快、准、有指纹库**；见 [`../01-信息搜集/nmap.md`](../01-信息搜集/nmap.md) |
| **`nping`**（nmap 附带） | 命令行包构造 | 介于 hping3 与 scapy 之间 |
| **`tcpdump` / `wireshark`** | 抓包/分析 | 强在**人工分析**；Scapy 强在**程序化处理**；见 [`tcpdump.md`](tcpdump.md)、[`wireshark.md`](wireshark.md) |
| **`arpspoof` / `ettercap` / `bettercap`** | 现成的 ARP 欺骗 | 一键可用；Scapy 可以**自己实现并定制** |
| **`npcap`/`pcap`**（C 库） | 底层库 | Scapy 是**默认自带协议的 Python 封装**，开发效率高得多 |

**一句话选型**：

- **常规任务** → 用现成工具（nmap/tcpdump/…），**更快更准**；
- **现成工具表达不了的需求** → **Scapy**；
- **要写自动化/集成/协议研究/模糊测试** → **Scapy**。

---

## 2. 工作原理

### 2.1 核心模型：`/` 运算符把「层」叠起来

```python
pkt = Ether() / IP(dst="10.0.0.1") / TCP(dport=80, flags="S") / Raw(load=b"hello")
#     └─二层─┘   └─────三层─────┘   └──────四层────────┘   └─载荷─┘
```

**`/` 不是除法，是「层叠运算符」**（官方文档称之为 *layering operator*）。它的语义是：

> 把左边的层作为右边的**下层**，自动处理「上层协议字段」的填充（如 IP 的 `proto`、Ether 的 `type`）。

```
        构造时（自上而下 / 自下而上都行）
        ┌────────────────────────────────────────────┐
Ether() / IP() / TCP() / Raw(bytes)
        │      │      │        │
        │      │      │        └─ 原始字节载荷
        │      │      └─ 传输层（TCP/UDP/ICMP…）
        │      └─ 网络层（IP/IPv6/ARP…）
        └─ 链路层（Ether/RadioTap/Dot11…）
                    │
                    ▼  发送时：逐层封装 → 二进制字节流
               bytes(pkt)
                    │
                    ▼
        ┌────────────────────────────────────────────┐
        │  解析时：拿到的字节流 → 逐层解出「对象」      │
        │  pkt[IP].src / pkt[TCP].flags / pkt[Raw].load │
        └────────────────────────────────────────────┘
```

### 2.2 Scapy 的四个核心能力

**① 构造（Build）**：用类名 + 字段参数描述包

```python
IP(dst="10.0.0.1", ttl=1) / ICMP()
```

**② 发送与接收（Send / Receive）**：一层层封装好、发出去、收回来、配对

| 函数 | 工作层次 | 发送 | 接收 | 说明 |
|------|----------|------|------|------|
| `send()` | L3（IP） | ✅ | ❌ | 只发不关心回包 |
| `sendp()` | **L2（以太帧）** | ✅ | ❌ | 需要指定 `iface`；**构造 ARP/二层帧必须用它** |
| `sr()` | L3 | ✅ | ✅ | **返回「请求/响应」配对列表** |
| `sr1()` | L3 | ✅ | ✅ | 只返回**第一个**响应（最常用） |
| `srp()` / `srp1()` | **L2** | ✅ | ✅ | 二层版本的 `sr`/`sr1` |
| `sniff()` | 抓包 | ❌ | ✅ | 抓包并按条件过滤、回调处理 |

**关键区别**：

- **`send`/`sr` 走 L3**（内核负责路由与以太头）→ **适合发 IP 包**；
- **`sendp`/`srp` 走 L2**（你自己给完整以太帧）→ **ARP、需要指定网卡、需要精确控制源 MAC 时必须用它**；
- **`sr` 会做「请求-响应配对」**（用 seq/端口等匹配），返回 `(answered, unanswered)` 两个列表——**这是 Scapy 相对裸 socket 的巨大优势**。

**③ 嗅探（Sniff）**

```python
sniff(iface="eth0", filter="tcp port 80", prn=lambda p: p.summary(), count=10)
```

- `filter` 用 **BPF 语法**（和 tcpdump 一样）——**由内核/libpcap 过滤，效率高**；
- `prn` 是每个包的回调函数；
- `count` 达到数量自动停止；`timeout` 超时停止；`stop_filter` 自定义停止条件。

**④ 解析与分析（Dissect）**

```python
pkt = Ether(raw_bytes)          # 从字节流解析
pkt.show()                      # 逐层展开所有字段
pkt.summary()                   # 一行摘要
pkt[IP].dst                     # 按协议层取字段
pkt.haslayer(TCP)               # 是否含某层
pkt[Raw].load                   # 原始载荷
```

### 2.3 为什么 Scapy 能「发任意包」——它绕过了内核协议栈

```
   普通 socket（如 nc / curl）
       你的程序 ──► 内核 TCP/IP 栈 ──► 网卡
                      ▲
                      └── 内核会「帮你」处理：加 IP 头、加 TCP 头、校验和、
                          重传、拥塞控制……你【无法】构造非法或不完整的包

   Scapy（raw socket / AF_PACKET）
       你的程序 ──► 直接写网卡（绕过内核）
                      ▲
                      └── 你【自己】决定每一个字节：
                          可以发 ttl=0、可以发 flags=""（无标志位）、
                          可以给错误的校验和、可以发半个握手
```

**这是 Scapy 的威力所在，也是它的合法性风险所在**——它能做「正常工具做不到」的事，而这正是**授权测试**与**攻击**的分界线。

**代价**：

| 代价 | 说明 |
|------|------|
| **需要 root / `CAP_NET_RAW`** | 原始套接字是特权操作 |
| **慢** | 纯 Python，逐包构造；**不是扫描器，别拿它扫 /16** |
| **没有内核的可靠性** | 不会自动重传；丢包就是丢了 |
| **要看得到回包** | 需要网络路径允许回包到达（NAT/路由/防火墙都可能挡住） |

### 2.4 三个「必须理解」的细节

**① `sr1()` 收不到回包时返回 `None`** —— 「没响应」与「发失败」要分开判断。

**② `sniff()` 的 `prn` 回调里不要做耗时操作** —— 会丢包。要处理就用 `AsyncSniffer` 或先落盘再离线分析。

**③ 校验和默认是「延迟计算」的** —— Scapy 在发送前才填校验和。**抓包/解析时看到的 `chksum=None` 是正常的**，用 `pkt.show2()` 可以显示填充后的值。

---

## 3. 安装与快速上手

```bash
sudo apt install python3-scapy
command -v scapy scapy3
python3 -c 'import scapy; print(scapy.__version__)'
```

```console
root@kali:~# python3 -c 'import scapy; print(scapy.__version__)'
2.6.1
```

```bash
scapy -h
```

```console
root@kali:~# scapy -h
Usage: scapy.py [-c new_startup_file] [-p new_prestart_file] [-C] [-P] [-H]
Args:
	-H: header-less start
	-C: do not read startup file
	-P: do not read pre-startup file
```

**`scapy` 是一个交互式 Python shell**（本质就是「帮你 import 了 scapy 的 python」）：

```bash
sudo scapy
```

```console
                                 aSPY//YASa
                     apyyyyCY//////////YCa       |
                    sY//////YSpcs  scpCY//Pp     | Welcome to Scapy
 ayp ayyyyyyySCP//Pp           syY//C            | Version 2.6.1
 AYAsAYYYYYYYY///Ps              cY//S           |
         pCCCCY//p          cSSps y//Y           | https://github.com/secdev/scapy
         SPPPP///a          pP///AC//Y           |
              A//A            cyP////C           | Have fun!
              p///Ac            sC///a           |
              P////YCpc           A//A           | We are in France, we say Skappee.
       scccccp///pSP///p          p//Y           | OK? Merci.
      sY/////////y  caa           S//P           |
       cayCyayP//Ya              pY/Yy           |
        sY/PsY////YCc            aC//Yp
         sc  sccaCY//PCypaapyCP//YSs
                  spCPY//////YPSps
                       ccaacs
                                       using IPython 8.28.0
>>>
```

```python
>>> # 第一条命令：看看有多少协议可以构造
>>> ls()                       # 列出所有可用的「协议层」
>>> ls(IP)                     # 看 IP 层有哪些字段和默认值
>>> show_interfaces()          # 看有哪些网卡
```

**最小可用（发一个 ping，看回包）**：

```python
>>> pkt = IP(dst="127.0.0.1") / ICMP()
>>> pkt.summary()
'IP / ICMP 127.0.0.1 > 127.0.0.1 icmp-echo 0'
>>> reply = sr1(pkt, timeout=2, verbose=0)
>>> reply.show()
###[ IP ]###
  version   = 4
  ihl       = 5
  ...
  src       = 127.0.0.1
  dst       = 127.0.0.1
###[ ICMP ]###
  type      = 0
  code      = 0
  ...
  id        = 1234
  seq       = 0
```

**用脚本（更常见）**：

```python
#!/usr/bin/env python3
from scapy.all import ICMP, IP, sr1

reply = sr1(IP(dst="127.0.0.1") / ICMP(), timeout=2, verbose=0)
print("回包:", reply.summary() if reply else "无响应")
```

```bash
sudo python3 /tmp/ping.py
```

> **权限**：发原始包需要 root 或 `CAP_NET_RAW`。想不用 sudo：
> ```bash
> sudo setcap cap_net_raw,cap_net_admin=eip "$(readlink -f "$(command -v python3)")"
> ```
> （**注意这会扩大 python3 的权限，生产机上别这么做**。）

---

## 4. 核心参数详解

Scapy 的「参数」有两类：**命令行参数**（很少）和 **Python API**（主体）。

### 4.1 `scapy` 命令的选项

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-H` | **header-less 启动**（不打印 banner） | 脚本/管道里用，输出干净 |
| `-C` | **不读启动文件**（`~/.config/scapy/…`） | 排除「本地配置干扰」时排查用 |
| `-P` | **不读 pre-startup 文件** | 同上 |
| `-c <file>` | 指定**新的 startup 文件** | 定制默认 import 与设置 |
| `-p <file>` | 指定**新的 pre-startup 文件** | 更早阶段加载（定义 `conf` 之类） |

### 4.2 协议层速查（最常用的几个）

| 层 | 常用字段 | 备注 |
|----|----------|------|
| `Ether(src=, dst=, type=)` | MAC 地址；`type=0x0800`(IPv4)/`0x0806`(ARP) | 用 `sendp`/`srp` 发 |
| `IP(src=, dst=, ttl=, proto=, flags=, frag=)` | 网络层 | `flags="DF"`/`"MF"`；`frag=` 用于分片 |
| `IPv6(src=, dst=, hlim=)` | IPv6 | 注意用 `hlim` 不是 `ttl` |
| `TCP(sport=, dport=, flags=, seq=, ack=, window=)` | 传输层 | **`flags` 是字符串**，如 `"S"`、`"SA"`、`"FPA"`、`""`（无标志） |
| `UDP(sport=, dport=, len=, chksum=)` | 传输层 | UDP 扫描用它 |
| `ICMP(type=, code=, id=, seq=)` | 网络层 | `type=8` echo request，`0` echo reply |
| `ARP(op=, psrc=, pdst=, hwsrc=, hwdst=)` | 链路层 | **ARP 扫描/欺骗必须用 `sendp`/`srp`** |
| `DNS(rd=, qd=)` + `DNSQR(qname=, qtype=)` | 应用 | DNS 查询常用组合 |
| `Raw(load=b"...")` | **原始载荷** | 放自定义字节（HTTP 请求、payload…） |
| `Padding` / `Pad` | 填充 | 构造特定长度的包 |

**TCP `flags` 取值**（字符串拼接）：`F`(FIN) `S`(SYN) `R`(RST) `P`(PSH) `A`(ACK) `U`(URG) `E`(ECE) `C`(CWR)

| 组合 | 含义 |
|------|------|
| `"S"` | **SYN**（连接请求 / 半开扫描） |
| `"SA"` | SYN-ACK |
| `"A"` | ACK |
| `"FA"` | FIN-ACK（关闭） |
| `"R"` | RST |
| `"FPU"` | **NULL 扫描用的空标志**（注意：真实 NULL 扫描是 **`flags=""`**） |
| `""` | 无标志（NULL 扫描）—— 有些系统会回 RST，有些直接丢 |

### 4.3 发送/接收函数速查（**这张表决定了实际用法**）

| 函数 | 层次 | 发 | 收 | 返回 | 典型用途 |
|------|------|----|----|------|----------|
| `send(pkt)` | L3 | ✅ | ❌ | 无 | 批量发（如压测、洪泛实验） |
| `sendp(pkt, iface=)` | L2 | ✅ | ❌ | 无 | 发 ARP/自定义以太帧 |
| `sr(pkts, timeout=, retry=, verbose=)` | L3 | ✅ | ✅ | `(answered, unanswered)` | 批量请求-响应 |
| `sr1(pkt, timeout=, verbose=)` | L3 | ✅ | ✅ | **第一个响应或 `None`** | **最常用** |
| `srp()` / `srp1()` | L2 | ✅ | ✅ | 同上 | ARP 扫描（`srp1` 收单个） |
| `sniff(iface=, filter=, prn=, count=, timeout=, store=)` | —— | ❌ | ✅ | 包列表 | 抓包/被动监听 |
| `AsyncSniffer(...)` | —— | ❌ | ✅ | 可后台运行的对象 | **长期抓包**（不阻塞主流程） |
| `traceroute(target, ...)` | L3 | ✅ | ✅ | 跳与 RTT | 内置 traceroute |
| `arping(target, ...)` | L2 | ✅ | ✅ | 结果字符串 | 内置 ARP ping |
| `wrpcap(file, pkts)` | —— | —— | —— | 无 | **把包写成 pcap** |
| `rdpcap(file)` | —— | —— | —— | 包列表 | **读 pcap** |
| `PcapReader(file)` | —— | —— | —— | 迭代器 | **大 pcap 流式读取**（省内存） |

### 4.4 关键参数（发送/嗅探函数）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `timeout=<s>` | 等待响应/嗅探的秒数 | **必设**，否则 `sr1` 可能等很久 |
| `retry=<n>` | 重试次数 | 丢包环境调大 |
| `verbose=<0/1/2>` | 输出详细度 | **`verbose=0` 是脚本里的标准写法**（关掉进度输出） |
| `iface=<name>` | 指定网卡 | **`sendp`/`sniff` 必须指定**（多网卡时尤其） |
| `filter=<bpf>` | **BPF 过滤**（同 tcpdump） | `"tcp port 80"`、`"icmp"`、`"arp"`；**大幅降低 CPU** |
| `prn=<func>` | 每个包的回调 | 回调要快；重活交队列 |
| `count=<n>` | 抓/收到 N 个后停 | 配合 `timeout` 双保险 |
| `store=<0/1>` | 是否保存包到内存 | 长期抓包设 `store=0` **防内存爆掉** |
| `inter=<s>` | 发送间隔 | 慢速/避免洪泛 |
| `loop=<0/1>` | 循环发送 | 压测；**注意合法性与负载** |
| `l2socket` / `socket` | 自定义底层套接字 | 高级用法 |
| `conf.verb = 0` | **全局**关闭啰嗦输出 | 脚本开头设一次 |
| `conf.iface = "eth0"` | 全局默认网卡 | 避免每次传 `iface` |

### 4.5 解析与输出辅助

| 方法/函数 | 作用 |
|-----------|------|
| `pkt.show()` | **逐层展开所有字段与值**（调试必用） |
| `pkt.show2()` | **先完成校验和/长度计算再显示**（看「实际发出去的包」） |
| `pkt.summary()` | 一行摘要 |
| `pkt[IP].src` | 按层取字段 |
| `pkt.haslayer(TCP)` | 是否含某层 |
| `pkt.getlayer(TCP)` | 取某层对象（没有则 `None`） |
| `pkt[Raw].load` | 原始载荷 |
| `ls(SomeLayer)` | **列出该层所有字段与默认值**（忘了字段名就查它） |
| `ls()` | 列出所有可用协议层 |
| `hexdump(pkt)` | 十六进制转储 |
| `sprintf("%IP.src%:%TCP.sport%")` | 用格式串取值（`prn` 里很方便） |

---

## 5. 实战演练

> **环境声明**：Scapy 发的是**原始包**，能力远超普通工具。
> - **只在你自己拥有/授权的网络里发包**。发送畸形包、伪造源地址、洪泛、ARP 欺骗**都会实质影响他人网络**；
> - 本文所有示例都限定在**本机回环（`127.0.0.1`）**、**你自己的局域网**或**自建靶场**；
> - 建议在**一次性虚拟机**里练习；
> - **切勿**对公司/公共网络做下面的任何一层/二层操作。

### 场景 1：从「发一个包」到「解析一个包」（三种方式各来一遍）

**1a. 交互式：ICMP ping 并解剖回包**

```bash
sudo scapy -H
```

```python
>>> from scapy.all import *
>>> conf.verb = 0                    # 关掉啰嗦输出
>>> pkt = IP(dst="127.0.0.1") / ICMP()
>>> pkt.show()                       # 看看我要发的包长什么样
###[ IP ]###
  version   = 4
  ihl       = None
  tos       = 0x0
  len       = None
  id        = 1
  flags     =
  frag      = 0
  ttl       = 64
  proto     = icmp
  chksum    = None                    ← 注意：校验和是延迟计算的
  src       = 127.0.0.1
  dst       = 127.0.0.1
  \options   \
###[ ICMP ]###
     type      = echo-request
     code      = 0
     chksum    = None
     id        = 0x0
     seq       = 0x0
```

```python
>>> pkt.show2()                      # 用「实际发送时的值」再显示一遍
###[ IP ]###
  ...
  len       = 28                      ← 现在有值了
  chksum    = 0x5a1b                  ← 校验和也算好了
  ...
```

```python
>>> ans = sr1(pkt, timeout=2)
>>> print("有没有回包:", ans is not None)
有没有回包: True
>>> ans[ICMP].type                   # 0 = echo-reply
0
>>> ans.src                          # 回包来源
'127.0.0.1'
```

**解读**：

| 观察 | 含义 |
|------|------|
| `pkt.show()` 里 `chksum = None`、`len = None` | **Scapy 的延迟计算**：字段在发送前才填。**这是正常现象** |
| `pkt.show2()` 里都有了值 | 这就是「实际发出去的那个包」 |
| `sr1()` 返回一个包对象 | **响应里所有层的字段都能按名取**——这是 Scapy 的核心价值 |
| `ans[ICMP].type == 0` | ICMP 类型 0 = echo reply，说明对端回了 |

**1b. 脚本化：把「发出去」和「什么时候收不到」都写清楚**

```python
#!/usr/bin/env python3
"""最小 ping：区分「有回包 / 超时 / 底层发送失败」三种情况"""
import sys
from scapy.all import ICMP, IP, conf, sr1

conf.verb = 0

def ping(dst: str, timeout: float = 2.0) -> None:
    pkt = IP(dst=dst) / ICMP()
    try:
        ans = sr1(pkt, timeout=timeout)
    except PermissionError:
        print("需要 root 或 CAP_NET_RAW 权限", file=sys.stderr)
        sys.exit(1)
    if ans is None:
        print(f"{dst}: 无响应（超时 / 被过滤 / 目标不可达）")
    elif ans.haslayer(ICMP):
        t = ans[ICMP].type
        if t == 0:
            print(f"{dst}: 回包来自 {ans.src}，TTL={ans.ttl}")
        elif t == 3:
            print(f"{dst}: 目标不可达（ICMP type 3 code {ans[ICMP].code}）")
        else:
            print(f"{dst}: 收到 ICMP type={t} code={ans[ICMP].code}，来自 {ans.src}")

if __name__ == "__main__":
    ping(sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1")
```

```bash
sudo python3 /tmp/myping.py 127.0.0.1
sudo python3 /tmp/myping.py 10.0.0.1     # 只测你自己网段里的地址
```

```console
127.0.0.1: 回包来自 127.0.0.1，TTL=64
```

**解读**：**关键是把「`ans is None`」当成一个明确的第三态**。新手最常见的错误是：

```python
# ❌ 会 AttributeError（None 没有 .haslayer）
ans = sr1(...)
print(ans.haslayer(ICMP))
```

**1c. 抓包 + 解析（用 `sniff` 看真实流量）**

```bash
# 先起一个本地 HTTP 服务作为流量来源
python3 -m http.server 8000 --directory /tmp &
curl -s http://127.0.0.1:8000/ >/dev/null
```

```python
#!/usr/bin/env python3
"""抓 5 个包，打印每层摘要 + HTTP 载荷前 80 字节"""
from scapy.all import Raw, TCP, conf, sniff

conf.verb = 0

def on_packet(pkt):
    print("-" * 60)
    print(pkt.summary())                       # 一行摘要
    if pkt.haslayer(TCP):
        t = pkt[TCP]
        print(f"  {t.sport} -> {t.dport}  flags={t.flags}  seq={t.seq}")
    if pkt.haslayer(Raw):
        load = bytes(pkt[Raw].load)[:80]
        print("  payload:", load)

sniff(iface="lo", filter="tcp port 8000", prn=on_packet, count=5, timeout=10)
```

```bash
sudo python3 /tmp/sniff_http.py
```

```console
------------------------------------------------------------
Ether / IP / TCP 127.0.0.1:52344 > 127.0.0.1:8000 S
  52344 -> 8000  flags=S  seq=1234567890
------------------------------------------------------------
Ether / IP / TCP 127.0.0.1:8000 > 127.0.0.1:52344 SA
  8000 -> 52344  flags=SA  seq=987654321
------------------------------------------------------------
Ether / IP / TCP 127.0.0.1:52344 > 127.0.0.1:8000 PA
  52344 -> 8000  flags=PA  seq=1234567891
  payload: b'GET / HTTP/1.1\r\nHost: 127.0.0.1:8000\r\nUser-Agent: curl/8.9.1\r\nAccept: */*\r\n\r\n'
```

**解读**：

| 观察 | 含义 |
|------|------|
| `flags=S` → `flags=SA` → `flags=PA` | **能逐帧看到 TCP 握手与数据传输**——这是最好的 TCP 教学 |
| `payload: b'GET / HTTP/1.1...'` | **HTTP 就是明文文本**，能直接读出来（所以 HTTP 必须配 TLS） |
| `filter="tcp port 8000"` | BPF 过滤在**内核层**执行，**不浪费 Python 性能** |
| `count=5, timeout=10` | 双重停止条件 |

### 场景 2：ARP 扫描与「自写扫描器」（**只在自己的局域网**）

**2a. ARP 主机发现（自己写一个 ARP 扫描器）**

```python
#!/usr/bin/env python3
"""ARP 扫描：向本网段发 ARP 请求，收集「活着的主机 → MAC」

⚠️ 只在你自己的局域网/实验网段运行。
"""
import ipaddress
from scapy.all import ARP, Ether, conf, srp

conf.verb = 0
NET = "192.168.1.0/24"          # ← 改成你自己的网段
IFACE = "eth0"                  # ← 改成你自己的网卡（show_interfaces() 可查）
TIMEOUT = 3

def arp_scan(net: str, iface: str, timeout: float = 3.0):
    target = str(ipaddress.ip_network(net).network_address)
    # ⚠️ 用一个 IP 作「典型目标」会只问一个；要扫全网段用下面的广播形式
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=net)
    answered, _ = srp(pkt, iface=iface, timeout=timeout)
    results = [(r.psrc, r.hwsrc) for _, r in answered]
    return sorted(set(results))

if __name__ == "__main__":
    hosts = arp_scan(NET, IFACE, TIMEOUT)
    print(f"存活主机（{len(hosts)} 台）:")
    for ip, mac in hosts:
        print(f"  {ip:<16} {mac}")
```

```bash
sudo python3 /tmp/arp_scan.py
```

```console
存活主机（4 台）:
  192.168.1.1       aa:bb:cc:dd:ee:ff
  192.168.1.20      11:22:33:44:55:66
  192.168.1.31      77:88:99:aa:bb:cc
  192.168.1.100     de:ad:be:ef:00:01
```

**解读（为什么 ARP 扫描要用 `srp` 而不是 `sr`）**：

| 要点 | 说明 |
|------|------|
| **ARP 是二层协议** | 必须**自己构造以太帧**（`Ether()/ARP()`），所以用 **`srp`（L2 收发）** |
| **必须指定 `iface`** | 二层没有「路由」，必须明确从哪块网卡发 |
| **广播 MAC** | `dst="ff:ff:ff:ff:ff:ff"` |
| **只覆盖本地二层域** | **ARP 不能跨网段**——跨网段要用 nmap/ICMP |
| **比 nmap 快且安静** | ARP 请求没有 TCP/IP 层，很多防火墙不拦；但**仍然会被 ARP 监控记录** |

**2b. TCP SYN 扫描（半开）——「自己写端口扫描器」**

```python
#!/usr/bin/env python3
"""TCP SYN（半开）扫描 + 结果的四种判定

必须用 root 运行；只扫你自己拥有/授权的主机。
"""
import sys
from scapy.all import ICMP, IP, TCP, conf, sr

conf.verb = 0

def syn_scan(dst: str, ports, timeout: float = 2.0):
    """返回 {port: (状态, 说明)}"""
    pkts = IP(dst=dst) / TCP(dport=list(ports), flags="S")
    answered, unanswered = sr(pkts, timeout=timeout)

    result = {}
    for sent, recv in answered:
        port = sent[TCP].dport
        if recv.haslayer(TCP):
            tcp = recv[TCP]
            if tcp.flags & 0x12 == 0x12:        # SYN+ACK
                result[port] = "open"
                # 礼貌地发 RST 关闭这个半开连接（避免占用对端资源）
                sr(IP(dst=dst) / TCP(dport=port, flags="R", seq=tcp.ack), timeout=1)
            elif tcp.flags & 0x04:              # RST
                result[port] = "closed"
        elif recv.haslayer(ICMP) and recv[ICMP].type == 3:
            # ICMP 不可达（type 3）：code 1/2/3/9/10/13 通常表示被过滤
            result[port] = f"filtered (icmp code {recv[ICMP].code})"

    for p in ports:
        result.setdefault(p, "filtered / no response")
    return result

if __name__ == "__main__":
    dst = sys.argv[1]
    ports = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else [22, 80, 443, 8000]
    for port, state in sorted(syn_scan(dst, ports).items()):
        print(f"{dst}:{port}\t{state}")
```

```bash
sudo python3 /tmp/syn_scan.py 127.0.0.1 22,80,443,8000
```

```console
127.0.0.1:22	filtered / no response
127.0.0.1:80	closed
127.0.0.1:443	closed
127.0.0.1:8000	open
```

**解读（这是 Scapy 相对 nc 的关键差异）**：

| 观察 | 含义 |
|------|------|
| `flags="S"` 只发 SYN | **半开扫描**：不发三次握手的第三个 ACK，连接不建立 → **应用层无日志** |
| **收到 SYN+ACK（0x12）** | 端口**开放** |
| **收到 RST（0x04）** | 端口**关闭** |
| **什么都没收到** | **被过滤**（防火墙丢包）——和 `nc` 的「超时」含义一致 |
| **主动发 RST 收尾** | **这是「体面」的做法**：不留下半开连接，减少对目标的影响 |
| `sr(pkts, ...)` 传**一批包** | **Scapy 会自动做请求-响应配对**（按 seq/端口匹配）——这是手写 socket 很难做对的 |

**⚠️ 为什么你几乎不该用 Scapy 做端口扫描**：

| 维度 | Scapy | nmap |
|------|-------|------|
| 速度 | 慢（Python 逐包） | **快**（C，并行，多阶段） |
| 准确性 | 要自己处理重传/超时/ICMP | **已处理** |
| 服务识别 | **没有** | **有（-sV）指纹库** |
| 建议 | **用于「理解扫描原理」和「定制特殊探测」** | **实际扫描用 nmap** |

→ 见 [`../01-信息搜集/nmap.md`](../01-信息搜集/nmap.md)。**Scapy 写扫描器的价值在于「能定制」，不在于「快」。**

**2c. 用 TTL 自定义值做「逐跳探测」（理解 traceroute 原理）**

```python
#!/usr/bin/env python3
"""手工 traceroute：逐跳增加 TTL，靠 ICMP 超时回包发现路径

只对你自己拥有/授权的目标使用。
"""
import sys
from scapy.all import ICMP, IP, UDP, conf, sr1

conf.verb = 0

def hop_probe(dst: str, ttl: int, timeout: float = 1.0):
    # 用 UDP 到高端口：中间路由器会回 ICMP time-exceeded（type 11）
    probe = IP(dst=dst, ttl=ttl) / UDP(dport=33434)
    ans = sr1(probe, timeout=timeout)
    if ans is None:
        return None, None
    if ans.haslayer(ICMP) and ans[ICMP].type == 11:
        return ans.src, "hop"
    if ans.haslayer(ICMP) and ans[ICMP].type == 3:
        return ans.src, "destination (unreachable/port)"
    return ans.src, f"icmp type={ans[ICMP].type}" if ans.haslayer(ICMP) else "other"

if __name__ == "__main__":
    dst = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    for ttl in range(1, 16):
        src, kind = hop_probe(dst, ttl)
        if src is None:
            print(f"ttl={ttl:2d}  *")
        else:
            print(f"ttl={ttl:2d}  {src}  ({kind})")
        if kind and kind.startswith("destination"):
            break
```

```bash
sudo python3 /tmp/my_traceroute.py 127.0.0.1
```

```console
ttl= 1  * 
ttl= 2  *
...
ttl= 1  127.0.0.1  (destination (unreachable/port))
```

**解读（traceroute 的全部原理就在这里）**：

| 现象 | 原因 |
|------|------|
| 中间路由器回 **ICMP type 11（time exceeded）** | 它收到 TTL=0 的包 → 丢弃并发 ICMP 超时 |
| 目的主机回 **ICMP type 3（destination unreachable，code 3 = port unreachable）** | UDP 打到没人监听的高端口 |
| `*` 不响应 | 中间设备禁止发 ICMP（很常见）或限速 |

**注意**：Scapy 已经内置了 `traceroute("10.0.0.1")`。**自己写一遍是为了理解原理**——这正是 Scapy 的定位。

### 场景 3：pcap 离线分析 + 与 tcpdump/Wireshark 分工

**3a. 用 tcpdump 抓、用 Scapy 分析（推荐的分工）**

```bash
# ① tcpdump 负责高效抓包（C 实现，快）
sudo tcpdump -i lo -w /tmp/http.pcap -c 50 'tcp port 8000' &
curl -s http://127.0.0.1:8000/ >/dev/null
sleep 1
ls -l /tmp/http.pcap
```

```python
#!/usr/bin/env python3
"""离线分析 pcap：统计会话、提取 HTTP 请求、按目的地聚合"""
from collections import Counter
from scapy.all import PcapReader, IP, TCP, Raw

PCAP = "/tmp/http.pcap"

sessions = Counter()
hosts = Counter()
requests = []

# PcapReader 是「流式」的，大文件也不会吃光内存
with PcapReader(PCAP) as reader:
    for pkt in reader:
        if not pkt.haslayer(IP):
            continue
        hosts[pkt[IP].dst] += 1
        if pkt.haslayer(TCP):
            t = pkt[TCP]
            # 归一化「会话」：小端口在前，便于聚合两个方向
            a, b = sorted([t.sport, t.dport])
            sessions[(pkt[IP].src, pkt[IP].dst, a, b)] += 1
        if pkt.haslayer(Raw):
            load = bytes(pkt[Raw].load)
            if load.startswith((b"GET ", b"POST ", b"HEAD ", b"PUT ", b"DELETE ")):
                requests.append(load.split(b"\r\n", 1)[0].decode("latin-1"))

print(f"包总数: {sum(hosts.values())}")
print(f"会话数: {len(sessions)}")
print("Top 目标:")
for ip, n in hosts.most_common(5):
    print(f"  {ip:<18} {n}")
print(f"HTTP 请求行（{len(requests)} 条）:")
for r in requests[:10]:
    print("  ", r)
```

```bash
python3 /tmp/analyze_pcap.py
```

```console
包总数: 50
会话数: 3
Top 目标:
  127.0.0.1          50
HTTP 请求行（1 条）:
   GET / HTTP/1.1
```

**解读**：

| 技术点 | 说明 |
|--------|------|
| **`PcapReader` 而非 `rdpcap`** | **流式迭代**，处理 GB 级 pcap 不会 OOM；`rdpcap` 会全部读进内存 |
| **`Counter` 聚合** | 这才是 Scapy 的优势——**用 Python 逻辑任意统计**，tshark 的表达力比不上 |
| **`Raw` 判断 HTTP** | 应用层就是 `Raw` 载荷，自己按协议规则解析 |
| **tcpdump 抓 + Scapy 分析** | **最佳分工**：抓到快、分析灵活 |

**3b. 用 Scapy 生成 pcap（构造测试数据）**

```python
#!/usr/bin/env python3
"""构造一批包并写成 pcap —— 用于「造测试数据」或「喂给其它工具」"""
from scapy.all import Ether, IP, TCP, Raw, wrpcap

elapsed = 0
pkts = []
for i in range(3):
    pkts.append(
        Ether() / IP(src="10.0.0.10", dst="10.0.0.20") /
        TCP(sport=40000 + i, dport=80, flags="PA", seq=1000 + i) /
        Raw(load=f"GET /page{i} HTTP/1.1\r\nHost: target.local\r\n\r\n".encode())
    )
wrpcap("/tmp/synthetic.pcap", pkts)
print(f"写出 {len(pkts)} 个包到 /tmp/synthetic.pcap")
```

```bash
python3 /tmp/gen_pcap.py
# 用其它工具验证这个文件（证明它是合法 pcap）
tcpdump -r /tmp/synthetic.pcap -n
python3 /tmp/analyze_pcap.py   # ← 把 PCAP 变量改成 /tmp/synthetic.pcap 也能跑
```

**解读**：**「造 pcap」是 Scapy 一个被低估的能力**——你可以用它：

- 为 IDS（如 [`snort.md`](../02-漏洞分析/snort.md)）生成测试流量；
- 复现一个只在特定报文序列下才触发的 bug；
- 构造「畸形包」测试解析器的健壮性（**模糊测试**）。

```bash
# 让 snort 检测你自己造的流量（离线，完全安全）
sudo snort -c /etc/snort/snort.lua -r /tmp/synthetic.pcap -A alert_fast -k none
```

**3c. 与 Wireshark / tcpdump 的分工表**

| 任务 | 首选工具 | 为什么 |
|------|----------|--------|
| **实时抓包** | `tcpdump` | C 实现，快；见 [`tcpdump.md`](tcpdump.md) |
| **逐包人工分析、跟流、看图** | **Wireshark** | GUI + 解码最全；见 [`wireshark.md`](wireshark.md) |
| **程序化统计/提取/改写** | **Scapy** | Python 逻辑任意 |
| **构造自定义/畸形包** | **Scapy** | 唯一能做到的工具 |
| **协议模糊测试** | Scapy（作为底层） | 可生成海量变体 |
| **大 pcap 的聚合统计** | Scapy（`PcapReader`）或 `tshark -z` | 各有优势 |
| **长期在线抓包 + 规则匹配** | Zeek / Snort / tcpdump | Scapy 不适合长时间在线 |

**3d. 一个完整闭环：造包 → 侦测 → 分析**

```bash
# ① 造一个「明显可疑」的流量（大量 SYN 到不同端口 = 端口扫描特征）
python3 - <<'PY'
from scapy.all import Ether, IP, TCP, Raw, wrpcap
pkts = [Ether()/IP(src="10.0.0.99", dst="10.0.0.20")/TCP(sport=50000+i, dport=p, flags="S")
        for i, p in enumerate(range(1, 101))]
wrpcap("/tmp/scan.pcap", pkts)
print("生成", len(pkts), "个 SYN 包")
PY

# ② 喂给 IDS 看能不能检出
sudo snort -c /etc/snort/snort.lua -r /tmp/scan.pcap -A alert_fast -k none -q | head -5

# ③ 用 Scapy 离线统计「同一源 IP 扫了多少个不同端口」
python3 - <<'PY'
from collections import defaultdict
from scapy.all import PcapReader, IP, TCP
seen = defaultdict(set)
for pkt in PcapReader("/tmp/scan.pcap"):
    if pkt.haslayer(TCP):
        seen[pkt[IP].src].add(pkt[TCP].dport)
for src, ports in seen.items():
    print(f"{src} 尝试了 {len(ports)} 个不同端口（扫描特征）")
PY
```

```console
10.0.0.99 尝试了 100 个不同端口（扫描特征）
```

**解读**：**这个闭环才是 Scapy 的真实用法**：

```
Scapy 造包  →  给检测工具（Snort/自研）验证规则  →  Scapy 离线统计验证结论
   ▲                                                        │
   └──────────── 发现检测盲区 → 调整规则 / 改攻击面 ◄────────┘
```

---

## 6. 输出解读

### 6.1 `show()` 的关键字段（按层）

**IP 层**

| 字段 | 含义 | 判读 |
|------|------|------|
| `src` / `dst` | 源/目的 IP | 是否被伪造（看是否与本网段不符） |
| `ttl` | 生存时间 | **初始 TTL 可反推操作系统**（64=Linux/macOS 常见，128=Windows 常见）——收到时 TTL 已减去路径跳数 |
| `proto` | 上层协议号 | 6=TCP, 17=UDP, 1=ICMP |
| `flags` | `DF`/`MF` | 分片相关 |
| `id` | IP 标识 | **同一 id 的分片属于同一个原始包** |
| `chksum = None` | 未计算（延迟计算） | 正常；`show2()` 可看实际值 |

**TCP 层**

| 字段 | 含义 | 判读 |
|------|------|------|
| `flags` | 标志位：`S`/`A`/`F`/`R`/`P` | **`S`→`SA`→`A` 是握手；`FA` 是关闭；`R` 是拒绝** |
| `sport`/`dport` | 源/目的端口 | 服务端口 vs 临时端口 |
| `seq`/`ack` | 序列号/确认号 | **配对请求与响应靠它们** |
| `window` | 窗口大小 | **也可用于被动指纹**（不同 OS 默认值不同） |
| `options` | TCP 选项 | MSS/窗口缩放/Timestamp —— 指纹的另一来源 |

**ICMP 层**

| type | 含义 | 判读 |
|------|------|------|
| `0` | Echo Reply | **ping 成功** |
| `8` | Echo Request | 你发出的 ping |
| `3` | Destination Unreachable | 目标不可达（看 `code`：0=网络, 1=主机, 3=端口, 9/10/13=被过滤） |
| `11` | Time Exceeded | **TTL 耗尽** → traceroute 的每一跳 |
| `5` | Redirect | 有设备在做重定向（可能是正常的，也可能是投毒） |

### 6.2 `sr()` / `sr1()` 的返回值怎么读

```python
answered, unanswered = sr(pkts, timeout=2)
```

| 变量 | 内容 | 含义 |
|------|------|------|
| `answered` | `[(sent_pkt, recv_pkt), ...]` | **有响应的**（Scapy 已配对） |
| `unanswered` | `[sent_pkt, ...]` | 超时/无响应的 |
| `sr1` 的返回 | 包对象 **或 `None`** | `None` 必须单独处理 |

**三种结果对应三种网络语义**：

| 结果 | 网络含义 |
|------|----------|
| 有响应且是预期的包 | 可达且服务有响应 |
| 有响应但是 RST / ICMP 不可达 | **可达但被拒绝**（端口关闭 / 被过滤） |
| **无响应（`None`）** | **被丢弃**（防火墙 DROP）或路径不通 |

**「RST」与「无响应」是两回事**——这是扫描判读的核心。

### 6.3 判断「我的脚本为什么没收到回包」

| 排查项 | 检查方法 |
|--------|----------|
| 权限够不够 | 用 `sudo`；`PermissionError` 会直接报 |
| 网卡选对了没 | `show_interfaces()`；`sendp`/`sniff` 显式传 `iface` |
| 回包能不能回来 | 在自己机器上先 `ping`/`nc -zv` 验证**可达性** |
| 校验和有没有算 | 用 `show2()` 看实际发出的包 |
| BPF 过滤是否过窄 | 先把 `filter` 去掉再试 |
| 是否在虚拟机/NAT 后 | NAT 会改变源 IP，回包可能到不了你的抓包点 |
| 是不是被 `filter` 之外的层丢了 | 用 `sniff(filter="")` 全抓，看有没有回包 |

---

## 7. 与其他工具配合

```
   ① 抓包层
      tcpdump（高效抓包）        → tcpdump.md
      Wireshark（人工分析）      → wireshark.md
                    │  pcap
                    ▼
   ② Scapy（程序化：构造 / 解析 / 统计 / 造数据）
      ├─► 构造自定义/畸形包 → 喂给 IDS 验证规则（snort.md）
      ├─► 实现特殊探测（如自定义 TCP 选项、特定 TTL 组合）
      ├─► 离线统计大 pcap → 出结论（比 tshark 更灵活）
      └─► 造 pcap 测试数据 → 给其他工具当输入
                    │
   ③ 与「官方扫描器」的分工
      nmap（快、准、有指纹）      → ../01-信息搜集/nmap.md
      hping3（命令行自定义包）    → ../01-信息搜集/hping3.md
      masscan（超高速）           → ../01-信息搜集/masscan.md
                    │
   ④ 二层操作（只在自己的网络）
      ARP 扫描/欺骗自研 ↔ ettercap / bettercap / responder
                               → ../07-嗅探与欺骗/
                    │
   ⑤ 模糊测试
      Scapy 生成变体 → 目标程序/协议解析器
                    │
   ⑥ 学习与教学
      对照 Wireshark 的同一 pcap，逐字段理解
```

**Scapy 在各环节的「最佳角色」**：

| 环节 | Scapy 的角色 | 更好的选择 |
|------|--------------|------------|
| 快速扫端口 | ❌ 太慢 | nmap / masscan |
| **构造特殊包** | ✅ **最佳** | hping3（功能有限） |
| **解析 pcap 做统计** | ✅ **最佳** | tshark（表达力弱于 Python） |
| **造测试流量** | ✅ **最佳** | 几乎没有替代 |
| **协议实验/教学** | ✅ **最佳** | —— |
| 实时长期监控 | ❌ 不适合 | Snort / Zeek |
| 二层攻击 | ⚠️ 可自研 | ettercap / bettercap（现成） |

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `PermissionError: [Errno 1] Operation not permitted` | **没有原始套接字权限** | `sudo` 运行；或 `setcap cap_net_raw,cap_net_admin=eip`（谨慎） |
| `sr1()` 一直返回 `None` | 目标不响应 / 被防火墙 DROP / **网卡选错** / 回包路由不到你 | 先 `ping`/`nc -zv` 验证可达；检查 `iface`；检查 VM/NAT |
| `sendp()` 报需要 `iface` | **二层发送必须指定网卡** | `sendp(pkt, iface="eth0")` |
| 发出去的包 `chksum=None` | **延迟计算**（正常） | 用 `pkt.show2()` 看实际值 |
| 抓不到包 | `filter` 太窄；`iface` 错；抓的是错误的网卡 | 去掉 `filter` 先全抓；`show_interfaces()` 确认 |
| 抓包脚本内存爆掉 | `sniff()` 默认 `store=1`，长期运行会累积 | **`store=0`**；或用 `AsyncSniffer` + 定期落盘 |
| `prn` 回调里丢包 | 回调做了耗时操作（写文件/网络请求） | 回调只入队；重活交给别的线程/进程 |
| 大 pcap 读取 OOM | 用了 `rdpcap()`（全部载入内存） | 改用 **`PcapReader()`** 流式读 |
| 想发带 NULL 标志的 TCP 但没生效 | `flags=""` 有些实现不接受；NULL 扫描本来响应率就低 | 明确用 `flags=""`；接受「无响应」是正常结果 |
| ARP 扫描扫不到别的网段 | **ARP 不能跨网段** | 跨网段用 nmap/ICMP |
| ARP 扫描结果为空 | 选错网卡；或全用虚拟机 NAT 网络（NAT 下二层不透明） | 用**桥接**模式；`show_interfaces()` 确认 |
| `sr()` 配对错乱 | 请求包区分度不够（同 seq/同端口） | 让每个请求有不同 `seq`/`id`；或用 `sport` 区分 |
| 抓包顺序/时间不对 | 用了 `count` + `timeout` 提前停 | 用 `wrpcap` 先落盘再离线分析 |
| 伪造源 IP 后收不到回包 | **回包会发给伪造的源地址，不会回到你这里** | 这是物理事实；需要能看到该路径的流量（不能就改用真实源） |
| Wireshark 打不开我的 pcap | 文件不完整（脚本中途退出） | 用 `wrpcap()` 正确写出；确认包列表非空 |
| 与 sudo 下 python 的 import 冲突 | 用户级 `pip install` 的包 sudo 下不可见 | **用系统包 `python3-scapy`**；或 `sudo -E` 保留环境 |
| 在容器里发不出包 | 容器缺少 `CAP_NET_RAW` | `docker run --cap-add=NET_RAW`（仅实验环境） |

---

## 9. 防御视角（蓝队）

Scapy 的技能对蓝队有直接价值——**因为攻击者用它做的事，正是蓝队要检测的事**。

| Scapy 能做的「攻击动作」 | 蓝队的检测/加固 |
|--------------------------|-----------------|
| **ARP 扫描 / ARP 欺骗** | 交换机 **DAI（动态 ARP 检测）**；ARP 表异常监控；静态 ARP（关键主机）；见 [`../07-嗅探与欺骗/ettercap.md`](../07-嗅探与欺骗/ettercap.md) |
| **SYN 半开扫描** | IDS/防火墙看「大量 SYN 无后续 ACK」；SYN 速率限制 |
| **畸形包/非法标志组合** | IDS 规则（如 NULL/FIN/XMAS 扫描特征）；**协议栈要做健壮性测试** |
| **TTL 逐跳探测** | 边界过滤 ICMP time-exceeded；限制对外 traceroute 信息 |
| **伪造源 IP** | **uRPF / 反向路径校验**；BCP38 出向过滤 |
| **自定义载荷 / 模糊测试** | 对解析器做 fuzz 测试；WAF/IPS 覆盖异常输入 |
| **伪造 DNS 查询洪泛** | DNS 查询速率限制；响应比检测 |

**蓝队的六条硬建议**：

1. **写自己的检测规则**：用 Scapy **造出攻击流量**，喂给 Snort/自研检测器，**验证规则真的能检出**（这是第 5 章场景 3 的闭环）；
2. **做协议栈健壮性测试**：用 Scapy 生成畸形包，**在测试环境**验证你的服务/设备不会崩（**这是防御性 fuzz，合规**）；
3. **交换机侧加固**：DAI、DHCP snooping、端口安全、ARP 检查——**二层是很多企业最薄弱的一环**；
4. **边界做 uRPF**：防伪造源地址；
5. **监控「异常包构造模式」**：大量结构相似但字段变化的包（扫描/fuzz 特征）；大量 SYN 无 ACK；非标准 TCP 标志组合；
6. **把 Scapy 用在「验证」而不是「猜测」上**：怀疑某条 IDS 规则能不能检出某类流量？**用 Scapy 造出来试**。

**「用 Scapy 做检测器」的现实评价**：

| 场景 | 是否现实 |
|------|----------|
| **离线分析 pcap、验证假设** | ✅ **非常合适**（最佳用途） |
| **造测试数据验证检测规则** | ✅ **非常合适** |
| **写一次性专项检测脚本** | ✅ 合适 |
| **生产环境实时抓包检测** | ❌ 性能不够，用 Snort/Suricata/Zeek |
| **在大量主机上部署为 agent** | ❌ 依赖重（Python + 原始套接字） |

---

## 10. 参考

- Kali 工具页（含 `scapy -h` 原文）：<https://www.kali.org/tools/scapy/>
- Scapy 官网：<https://scapy.net>
- **Scapy 官方文档（最重要的参考）**：<https://scapy.readthedocs.io/en/latest/>
  - 用法总览：<https://scapy.readthedocs.io/en/latest/usage.html>
  - 发送与接收：<https://scapy.readthedocs.io/en/latest/usage.html#sending-and-receiving-packets>
  - 嗅探：<https://scapy.readthedocs.io/en/latest/usage.html#sniffing>
- 上游仓库：<https://github.com/secdev/scapy>
- 本地命令与自省：`scapy -h`、`ls()`、`ls(IP)`、`show_interfaces()`、`man scapy`（若有）
- 配套教程：[`tcpdump.md`](tcpdump.md)、[`wireshark.md`](wireshark.md)、[`../01-信息搜集/hping3.md`](../01-信息搜集/hping3.md)、[`../01-信息搜集/nmap.md`](../01-信息搜集/nmap.md)、[`../02-漏洞分析/snort.md`](../02-漏洞分析/snort.md)

## ⚠️ 法律与伦理

**Scapy 是本教程里「能力/风险比」最高的工具之一**：它能构造任意包，因此也最容易越过法律边界。

**① 发送原始包本身就是危险动作**

- **伪造源 IP**（`IP(src="...")`）：可能被用于反射/放大攻击（DNS/NTP/memcached 反射），属于《刑法》第 285/286 条范畴；也违反网络运营者的 BCP38 要求；
- **发送畸形包**：可能导致对端协议栈崩溃（DoS）→ 破坏计算机信息系统；
- **洪泛（`send(..., loop=1)`）**：直接构成拒绝服务；
- **ARP 欺骗 / 二层伪造**：导致他人流量被劫持/篡改 → 同时触犯《网络安全法》第 27 条、《刑法》第 285/286 条，并可能违反《个人信息保护法》（窃听通信内容）。

**② 「扫描」也是法律行为**

- **ARP 扫描**只影响本地二层域，但在**公司/公共网络**上做，属于未经授权的信息收集；
- **端口扫描**：对非授权主机扫描，可能被认定为「非法侵入的预备行为」；
- **必须**：只扫自己的网段/主机，或获得书面授权。

**③ 抓包即涉及通信秘密**

- 用 `sniff()` 抓到的可能是**他人的通信内容**：
  - 《宪法》第 40 条：公民的通信自由和通信秘密受法律保护；
  - 《个人信息保护法》《数据安全法》；
- **只在自己的设备/自己的网络抓包**；在企业环境抓包需合法授权与告知。

**④ 明确允许的场景**

| 场景 | 是否合规 |
|------|----------|
| 在**自己的机器/虚拟机**上做协议实验 | ✅ |
| 在**自己的局域网**做 ARP 扫描/教学 | ✅（不影响他人前提下） |
| **获得书面授权的**渗透测试 | ✅（按授权范围） |
| **CTF 比赛**中按规则使用 | ✅ |
| **对自己的服务做健壮性 fuzz 测试** | ✅（防御性） |
| 对**他人网络**扫描/欺骗/洪泛 | ❌ **违法** |
| 在**公司网络**未经批准抓包/扫段 | ❌ 违规（且可能违法） |
| 用伪造源 IP 做反射/放大 | ❌ **严重违法** |

**必须遵守**：

1. **只在自己拥有/授权的主机和网络里发包与抓包**；练习用**一次性虚拟机 + 隔离网络**；
2. **绝不对公网/他人目标做洪泛、伪造源 IP、畸形包攻击**；
3. **抓到的流量按敏感数据保护**：不存储无关内容、不外带、用完销毁；
4. **发现的问题通过正式渠道上报**，不擅自扩大影响；
5. **分享代码时**：教学用的「造包/解析」片段可以分享，但**可直接用于攻击他人网络的完整工具不应公开传播**（《刑法》第 285 条之三：提供侵入、非法控制计算机信息系统的程序、工具）；
6. **在授权测试中**，所有发包操作都要**记录时间、目标、用途**，便于事后说明与复盘。
