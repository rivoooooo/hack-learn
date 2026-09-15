# arp-scan（二层 ARP 主机发现与网卡指纹）

> **一句话**：在本地网段发 ARP 请求，拿到所有在线主机的 IP + MAC + 网卡厂商，二层发现最可靠的手段。
> **分类**：信息搜集 ｜ **Kali 包**：`arp-scan` ｜ **官方文档**：<https://github.com/royhills/arp-scan>

## 1. 它解决什么问题

"这台主机在线吗"这个问题，不同协议给的答案可靠度完全不同：

| 探测方式 | 能否被防火墙挡住 | 覆盖范围 | 结论可靠度 |
|---------|-----------------|---------|-----------|
| ICMP ping | **能**（禁 ping 就失效） | 可跨网段 | 低（禁 ping 即假阴性） |
| TCP SYN 到某端口 | **能**（端口过滤即失效） | 可跨网段 | 中 |
| **ARP 请求** | **不能**（链路层协议，主机必须响应） | **仅本网段** | **极高** |

ARP 是链路层协议，**同一广播域内的所有 IPv4 主机都会响应 ARP 请求，包括开了防火墙的主机**。所以"我在这个网段里到底有多少台机器"这个问题，arp-scan 给出的答案是最完整的。

代价：**ARP 不能路由**，只能在本地网段使用。

| 工具 | 强项 |
|------|------|
| **arp-scan** | 二层发现 + 网卡厂商指纹 + 可以伪造 ARP 包字段 |
| [netdiscover](netdiscover.md) | 主动/被动 ARP 扫描，支持无线场景 |
| [nbtscan](nbtscan.md) | 额外拿 NetBIOS 名和用户名 |
| [nmap](nmap.md) `-sn -PR` | 只想在 nmap 流程里顺带做 ARP 发现 |

## 2. 工作原理

```text
   arp-scan -l （或 arp-scan 10.0.0.0/24）
        │
        │ 对每个目标地址发一个 ARP Request（以太网广播 ff:ff:ff:ff:ff:ff）
        ▼
   ┌──────────────────────────────────────────────────────────┐
   │  ARP Request: "谁是 10.0.0.20？告诉 10.0.0.10"            │
   └──────────────────────────────────────────────────────────┘
        │
        │ 目标主机必须回 ARP Reply（链路层协议，无法用主机防火墙屏蔽）
        ▼
   ┌──────────────────────────────────────────────────────────┐
   │  ARP Reply: "10.0.0.20 是 00:1a:2b:3c:4d:5e"             │
   └──────────────────────────────────────────────────────────┘
        │
        ├─ 用 IEEE OUI 注册表(ieee-oui.txt) 反查 MAC 前 3 字节
        ├─ 用自定义映射(mac-vendor.txt) 补充
        └─ 输出： <IPv4>  <MAC>  <厂商>
```

关键机制：

- **单播 vs 广播**：默认发广播（`--destaddr` 默认 `ff:ff:ff:ff:ff:ff`）。也可以发单播地址，或组播地址。
- **每个目标发一次，失败重发一次**（默认 `--retry=2`，即最多 2 次尝试）。
- **带宽控制**：默认 256000 bit/s（约每秒 500 个包）。300 台主机大概 1 秒左右发完。`--interval` 更精确地控制包间隔。
- **厂商识别**：读 `ieee-oui.txt`。用 `get-oui` 可以更新这个文件到最新的 IEEE 数据（Kali 包里带了 `get-oui`）。
- **可用在无 IPv4 地址的接口上**：`--arpspa` 可以设置 ARP 请求里的源 IP，甚至能扫一个你没有 IP 的网段。
- **主动欺骗能力**：`--arpspa dest` 会把请求的源地址设成目标自己的地址（会触发某些系统的地址冲突告警）——这已经属于**攻击行为**，不要随便用。

## 3. 安装与快速上手

```bash
sudo apt install arp-scan
arp-scan --help | head -30
arp-scan --version     # 会显示 libpcap 版本与是否含 capabilities 支持
```

最小可用命令：

```bash
# 1) 扫本机所在网段（自动按接口地址+掩码生成目标）
sudo arp-scan --localnet

# 2) 扫指定网段
sudo arp-scan 192.168.56.0/24

# 3) 只扫几台主机并显示厂商
sudo arp-scan 192.168.56.10 192.168.56.101 192.168.56.102
```

## 4. 核心参数详解

### 通用

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-h, --help` | 帮助 | — |
| `-v, --verbose` | 详细进度信息，可重复最多 3 次 | 排查"为什么没结果" |
| `-V, --version` | 版本、libpcap 版本、capabilities 支持 | 权限问题排查时看 |
| `-I, --interface=<s>` | 指定网卡 | 多网卡/无线场景**强烈建议显式指定** |

### 目标选择

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `[hosts...]` | 目标列表：IP、主机名、CIDR、范围 `a-b`、`net:mask` | 常用的 CIDR 与范围形式 |
| `-l, --localnet` | 按接口地址与掩码自动生成目标 | 最常用；**与 `--file`/位置参数互斥** |
| `-f, --file=<s>` | 从文件读目标，一行一个；`-` 表示 stdin | 与 [nmap](nmap.md) 输出串联 |

### 输出格式

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-q, --quiet` | 极简输出：只显示 IP 和 MAC | 不需要厂商信息时更快；此时 `--format` 只能用 `${ip}` `${mac}` |
| `-x, --plain` | 去掉表头表尾，只输出主机行 | 脚本解析用 |
| `-g, --ignoredups` | 不显示重复回包（默认会标 `(DUP: n)`） | 有重复响应时（可能是 ARP 欺骗/多网卡）用 |
| `-D, --rtt` | 显示往返时间（毫秒） | 判断"是否同一台机器" |
| `-F, --format=<s>` | 自定义输出格式 | 见下方字段表 |
| `-d, --resolve` | 把响应地址解析成主机名 | 需要反向 DNS 时 |
| `-N, --numeric` | 目标必须是 IP（不做主机名解析） | 大列表可减少启动时间 |

`--format` 可用字段：`${ip}`、`${name}`、`${mac}`、`${hdrmac}`、`${vendor}`、`${padding}`、`${framing}`、`${vlan}`、`${proto}`、`${dup}`、`${rtt}`。转义：`\n` `\r` `\t` `\\`。

```bash
# 示例：输出 "IP MAC 厂商"
sudo arp-scan --localnet --format='${ip}\t${mac}\t${vendor}'
```

### 时序与重试

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-r, --retry=<i>` | 每台主机总尝试次数（默认 2） | 减到 1 会更快，但丢包时可能漏 |
| `-b, --backoff=<f>` | 超时倍数因子（默认 1.50） | 一般不用改 |
| `-t, --timeout=<i>` | 每台主机首次超时毫秒数（默认 500） | 大网段可减到 100 提速；跨设备可加大 |
| `-i, --interval=<x>` | 最小发包间隔（毫秒，加 `u` 为微秒） | 与 `-B` 二选一 |
| `-B, --bandwidth=<x>` | 出场带宽 bit/s（默认 256000；可加 K/M） | **`-i` 与 `-B` 不能同时用** |

### 构造 ARP 包（进阶/欺骗）

| 参数 | 作用 | 注意 |
|------|------|------|
| `-s, --arpspa=<a>` | 设置 ARP 请求的源 IPv4 地址，或写 `dest` | 用于无 IP 接口；写成 `dest` 会触发目标地址冲突告警（**攻击性**） |
| `-u, --arpsha=<m>` | 设置 ARP 源 MAC（ar$sha 字段） | 与 `--srcaddr`（以太网头）不同 |
| `-w, --arptha=<m>` | 设置 ARP 目标 MAC | 默认 0，请求包不用 |
| `-H, --arphrd=<i>` | ARP 硬件类型（默认 1=Ethernet） | 6=IEEE802 有些系统也响应 |
| `-p, --arppro=<i>` | ARP 协议类型（默认 0x0800） | — |
| `-a, --arphln=<i>` / `-P, --arppln=<i>` | 硬件/协议地址长度（默认 6 / 4） | — |
| `-o, --arpop=<i>` | ARP 操作码（默认 1=Request） | — |
| `-S, --srcaddr=<m>` | 以太网头源 MAC | — |
| `-T, --destaddr=<m>` | 以太网头目标 MAC（默认广播） | 改成单播可减少对全网的打扰 |
| `-y, --prototype=<i>` | 以太网协议类型（默认 0x0806） | — |
| `-L, --llc` | 使用 RFC 1042 LLC/SNAP 封装 | 802.2 网络 |
| `-Q, --vlan=<i>` | 带 802.1Q VLAN 标签（0–4095） | 跨 VLAN 探测 |

### 厂商库

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-O, --ouifile=<s>` | 指定 IEEE OUI 厂商库 | 默认当前目录 `ieee-oui.txt`，再找 `/usr/share/arp-scan/ieee-oui.txt` |
| `-m, --macfile=<s>` | 指定自定义厂商映射 | 默认 `/etc/arp-scan/mac-vendor.txt` |
| `get-oui` | 更新 `ieee-oui.txt` 到最新 IEEE 数据 | 厂商识别不准时执行 |

### 随机化

| 参数 | 作用 |
|------|------|
| `-R, --random` | 随机化目标顺序，避免顺序扫被识别 |
| `--randomseed=<i>` | 固定随机种子，使顺序可复现 |

## 5. 实战演练

**环境**：本地 VirtualBox Host-Only 网络。攻击机 Kali（`192.168.56.10`，网卡 `eth1`）；靶机有宿主机接口 `192.168.56.1`、Metasploitable2 `192.168.56.101`、DVWA 容器 `192.168.56.102`。

### 场景 1：一条命令摸清本地网段

```bash
sudo arp-scan -I eth1 --localnet
```

预期输出片段：

```text
Interface: eth1, type: EN10MB, MAC: 08:00:27:aa:bb:cc, IPv4: 192.168.56.10
Starting arp-scan 1.10.0 with 256 hosts (https://github.com/royhills/arp-scan)
192.168.56.1    0a:00:27:00:00:01       Advanced Micro Devices, Inc.
192.168.56.10   08:00:27:aa:bb:cc       PCS Systemtechnik GmbH
192.168.56.101  08:00:27:1a:2b:3c       PCS Systemtechnik GmbH
192.168.56.102  08:00:27:4d:5e:6f       PCS Systemtechnik GmbH

4 packets received by filter, 0 packets dropped by kernel
Ending arp-scan: 256 hosts scanned in 0.823 seconds (311.06 hosts/sec). 4 responded
```

解读：
- `PCS Systemtechnik GmbH` 是 VirtualBox 虚拟网卡的 OUI（`08:00:27`）——**厂商字段直接暴露了「这是虚拟机」**，这是非常有价值的情报。
- `08:00:27` 出现在 `192.168.56.1` 但 OUI 显示 `0a:00:27`（VMware 的 Host-Only 适配器风格）——不同虚拟化平台的 OUI 各不相同，可用来识别宿主机。
- 最后一行给出扫描速率（311 hosts/sec），可用于估算大网段耗时。

### 场景 2：只拿 IP 与 MAC，做脚本输入

```bash
sudo arp-scan -I eth1 --localnet --plain --quiet | tee arp_out.txt
awk '{print $1}' arp_out.txt > ips.txt
wc -l ips.txt
```

预期输出片段：

```text
192.168.56.1    0a:00:27:00:00:01
192.168.56.10   08:00:27:aa:bb:cc
192.168.56.101  08:00:27:1a:2b:3c
192.168.56.102  08:00:27:4d:5e:6f
```

解读：`--plain` 去掉表头表尾，`--quiet` 只保留 IP 和 MAC。这是把 arp-scan 接入自动化流水线的标准姿势：产出一份**最完整的存活 IP 清单**，再交给 [nmap](nmap.md) 精扫。

### 场景 3：自定义格式 + 往返时间辅助判断

```bash
sudo arp-scan -I eth1 192.168.56.0/24 \
  --rtt --format='${ip}\t${mac}\t${vendor}\t${rtt}ms'
```

预期输出片段：

```text
192.168.56.1	0a:00:27:00:00:01	Advanced Micro Devices, Inc.	0.412ms
192.168.56.101	08:00:27:1a:2b:3c	PCS Systemtechnik GmbH	0.523ms
```

解读：`${rtt}` 在排查**同一 IP 由多台设备响应**（ARP 欺骗/HA 集群）时很有用——不同响应时间往往意味着不同物理设备。若看到 `(DUP: 2)` 之类的标记，说明该 IP 回了多个包，需要警惕。

### 场景 4（进阶）：更新厂商库提高指纹准确率

```bash
# 更新 IEEE OUI 数据（需要网络）
sudo get-oui -v
ls -l /usr/share/arp-scan/ieee-oui.txt

# 添加自己的自定义映射（例如公司内网设备的 MAC 段）
echo "00:11:22	MyCompany-VoIP-Phone" | sudo tee -a /etc/arp-scan/mac-vendor.txt
sudo arp-scan -I eth1 --localnet
```

解读：交换机、IP 电话、打印机、摄像头这些设备往往能被 OUI 精确识别。**设备类型清单本身就是攻击面地图**——比如发现一堆 IP 摄像头，就知道该查默认口令问题了。

**跨 VLAN 探测（授权环境）**：

```bash
sudo arp-scan --interface=eth1 --vlan=100 10.100.0.0/24
```

## 6. 输出解读

| 字段 | 含义 | 下一步 |
|------|------|--------|
| 第一列 IP | 响应的主机地址 | 存入清单 |
| 第二列 MAC | 链路层地址 | 用于厂商识别、去重、设备追踪 |
| 第三列 厂商 | OUI 反查结果 | 判断设备类型（虚拟化/摄像头/打印机） |
| `(DUP: n)` | 该 IP 回包 n 次 | 怀疑 ARP 欺骗或 HA 冗余 |
| `${rtt}` | 往返时间 | 判断是否同一设备 |
| `Starting arp-scan 1.10.0 with 256 hosts` | 工具版本与目标数量 | 核对目标范围是否正确 |
| `N hosts scanned in T seconds (R hosts/sec)` | 速率统计 | 估算大网段耗时 |
| `N responded` | 响应主机数 | 与预期对比 |

**判断要点**：

- **arp-scan 的"没响应"比 ping 的"没响应"可靠得多**——同网段内 ARP 没回复，基本可以断定主机不在线（或做了 ARP 抑制，少见）。
- **虚拟化 OUI 是宝**：`08:00:27`（VirtualBox）、`00:0C:29`/`00:50:56`（VMware）、`00:15:5D`（Hyper-V）、`52:54:00`（KVM/QEMU）——一眼看出哪些是虚拟机，往往对应测试环境或云主机。
- **ARP 结果包含防火墙主机**：这是它比端口扫描更"诚实"的原因。

## 7. 与其他工具配合

```bash
# 1) arp-scan -> nmap：最完整的存活清单 + 端口精扫
sudo arp-scan -I eth1 --localnet --plain --quiet | awk '{print $1}' > ips.txt
sudo nmap -sV -iL ips.txt --open -oA arp_then_nmap

# 2) arp-scan -> netdiscover/nbtscan 交叉验证
sudo arp-scan -I eth1 --localnet --plain | awk '{print $1}' > ips.txt
nbtscan -f ips.txt

# 3) arp-scan -> whatweb（先筛出 80/443 开了的主机）
#    会话中：
sudo nmap -p80,443 --open -iL ips.txt -oG - | awk '/Ports:/{print $2}' > web_ips.txt
while read ip; do whatweb -a 1 "http://$ip"; done < web_ips.txt

# 4) 设备类型盘点：按厂商聚合
sudo arp-scan -I eth1 --localnet --format='${vendor}' | sort | uniq -c | sort -rn
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `pcap_lookupdev: no suitable device found` / 结果为空 | 自动选网卡选错了 | `-I <网卡名>` 显式指定；用 `ip -br a` 确认 |
| `ERROR: ... Permission denied` | 需要 CAP_NET_RAW | 用 `sudo`；或 `sudo setcap cap_net_raw+p $(which arp-scan)` |
| 结果里没有某个确定在线的主机 | 目标开了 ARP 抑制 / 在别的 VLAN / 是三层路由对端 | 确认网段；跨 VLAN 用 `--vlan`；三层对端本来就不会响应 |
| 出现大量 `(DUP: n)` | 可能有人在 ARP 欺骗，或目标做了 HA/多网卡 | 加 `-g` 忽略重复；**如果是异常重复，按安全事件排查** |
| 扫自己所在的网段时看不到自己 | 正常，本地接口通常不响应自己的广播 | 无需处理 |
| 大网段扫描很慢 | 默认带宽 256 kbit/s、超时 500 ms | `-B 1M` 或 `-t 100` 提速；`-r 1` 减少重试 |
| 厂商列显示 `(Unknown)` | OUI 库过旧 | `sudo get-oui -v` 更新 |
| VM 上结果异常少 | 虚拟网络设为 NAT 而非桥接/Host-Only | 换成桥接或 Host-Only 后重试 |
| `--interval` 和 `--bandwidth` 同时用时报警 | 两参数互斥 | 只保留一个 |
| 目标网段没配 IP（如只做二层发现） | 接口无 IPv4 | `--arpspa=<任意本网段地址>` |

## 9. 防御视角（蓝队）

- **ARP 扫描本身无法被"防住"**：ARP 是链路层必需协议，主机必须响应。你能做的是**检测**和**减少暴露**。
- **检测**：
  - **交换机侧**：短时间内一个 MAC 对大量不同目标发 ARP Request（广播风暴式模式）。比正常主机的 ARP 行为密集得多。支持 **Dynamic ARP Inspection (DAI)** 的交换机可开启，并监控日志。
  - **主机侧**：`arpwatch` 之类的工具可以监控 ARP 表变化异常。
  - **异常检测点**：注意 `--arpspa dest` 这类伪造源地址的用法会触发**IP 地址冲突告警**（Windows 会弹"检测到 IP 地址冲突"），这是很强的入侵信号。
- **缓解**：
  - **端口隔离 / 私有 VLAN（PVLAN）**：把同一 VLAN 内主机互相隔离，ARP 扫描只能看到网关。
  - **DAI + DHCP Snooping**：交换机只允许合法的 IP-MAC 绑定通过 ARP，同时能检测欺骗。
  - **802.1X**：未认证设备接不进来，从源头减少可被扫描的面。
- **信息泄露治理**：
  - 设备厂商 OUI 无法隐藏（MAC 前 3 字节是 IEEE 分配的），所以**减少暴露的办法是别把敏感设备放在同一个广播域**。
  - 打印机、摄像头、IP 电话这类"看得见就想去试默认口令"的设备，必须与办公网段隔离。
- **对比 netdiscover**：netdiscover 的被动模式（`-p`）完全不发包，只能靠监听 ARP 流量发现主机——**这在防守方角度是"不可能检测"的**。所以针对 ARP 发现的防守重点永远在"网络分段"而不是"流量检测"。

## 10. 参考

- 官方仓库（含完整选项文档）：<https://github.com/royhills/arp-scan>
- Kali 工具页：<https://www.kali.org/tools/arp-scan/>
- IEEE OUI 注册表：<https://standards-oui.ieee.org/oui/oui.txt>
- man page：`man arp-scan` ｜ `man get-oui`
- 用法核实：本教程参数取自 `arp-scan 1.10.0` 的 man page

---

**相关教程**：[netdiscover](netdiscover.md) ｜ [nbtscan](nbtscan.md) ｜ [nmap](nmap.md) ｜ [enum4linux](enum4linux.md) ｜ [hping3](hping3.md)
