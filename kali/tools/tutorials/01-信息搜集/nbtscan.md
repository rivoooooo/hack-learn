# nbtscan（NetBIOS 名字表扫描）

> **一句话**：向网段内每台主机发 NetBIOS 状态查询，把 IP、计算机名、登录用户名和 MAC 地址列成一张表。
> **分类**：信息搜集 ｜ **Kali 包**：`nbtscan` ｜ **官方文档**：<https://github.com/resurrecting-open-source-projects/nbtscan>

## 1. 它解决什么问题

在 Windows 占比高的内网里，你扫到的是一堆 IP，但不知道谁是谁。`nbtscan` 用 UDP 137 的 **NetBIOS 状态查询**，一条命令就能把 IP ↔ 计算机名 ↔ 登录用户 ↔ MAC 对应起来。

它和同类工具的分工：

| 工具 | 协议 | 拿到的信息 | 速度 |
|------|------|-----------|------|
| **nbtscan** | NetBIOS（UDP 137） | IP、NetBIOS 名、登录用户名、MAC | 很快（无连接） |
| [arp-scan](arp-scan.md) | ARP（二层） | IP、MAC、网卡厂商 | 最快，但只在本网段 |
| [netdiscover](netdiscover.md) | ARP（主动/被动） | IP、MAC、厂商 | 快，本网段 |
| [nmap](nmap.md) `-sn` + `--script nbstat` | 多协议 | 更全但更慢 | 慢 |
| [enum4linux](enum4linux.md) | SMB/RPC | 用户、共享、口令策略 | 慢但深 |

**关键特性**：nbtscan **只对实现了 NetBIOS 的主机有效**——Windows 和运行 Samba 的 Unix。普通 Linux、路由器、网络设备不会响应（这是设计预期，不是 bug）。

## 2. 工作原理

```text
   nbtscan 192.168.1.0/24
        │
        │ 对每个地址发一个 NetBIOS Node Status Request
        │（UDP 137，无连接、无三次握手）
        ▼
   ┌──────────────────────────────────────────────┐
   │  目标 NetBIOS 栈返回 Node Status Response     │
   │  内含「NetBIOS 名字表」：                      │
   │     DPTSERVER  <00> UNIQUE   工作站服务        │
   │     DPTSERVER  <20> UNIQUE   文件服务（可共享） │
   │     DEPARTMENT <00> GROUP    域名              │
   │     DEPARTMENT <1c> GROUP    域控组            │
   │     ADMINISTRATOR <03> UNIQUE 当前登录用户      │
   └──────────────────────────────────────────────┘
        │
        ├── 默认输出：IP / 计算机名 / 是否可共享 / 用户名 / MAC
        └── -v 输出：完整名字表（含 <xx> 后缀，标明服务类型）
```

几个要点：

- **无连接协议**：所以快，也不需要三次握手，防火墙只按状态检测很难拦。
- **`<20>` 后缀**：表示该机在跑 File Server Service，也就是"有共享能力"。默认输出的 `Server` 列就是这个意思。
- **`<03>` 后缀**：当前登录的用户名。如果无人登录，这里显示的就是计算机名。
- **默认并发 + 重传**：`-m` 控制重传次数（默认 0）。丢包多的网络里加 `-m 2` 能提高命中率。
- **`-r` 使用本地 137 端口**：Windows 95 只响应来自 137 端口的查询（现代系统不需要）。

## 3. 安装与快速上手

```bash
sudo apt install nbtscan
nbtscan -h 2>&1 | head -20    # 用法在 man page 与 -h 输出中
man nbtscan
```

最小可用命令：

```bash
# 1) 扫整个 C 段
nbtscan 192.168.1.0/24

# 2) 扫地址范围
nbtscan 192.168.1.25-137

# 3) 详细模式：打印每台主机的完整 NetBIOS 名字表
nbtscan -v 192.168.1.0/24
```

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `<target>` | 目标：`192.168.1.1`（单 IP）、`192.168.1.0/24`（网段）、`192.168.1.1-127`（范围） | 三种格式任选 |
| `-f <file>` | 从文件读 IP 列表（替代位置参数） | 只扫已知活主机，避免全网段噪声 |
| `-v` | 详细输出，打印每台主机的完整名字表 | 分析服务角色时必开 |
| `-d` | 打印完整数据包内容 | 调试/协议学习；**与 `-v`、`-s`、`-h` 互斥** |
| `-e` | 输出 `/etc/hosts` 格式 | 直接追加到 hosts 文件做临时命名 |
| `-l` | 输出 `lmhosts` 格式 | Windows lmhosts 兼容 |
| `-s <sep>` | 脚本友好输出：无表头，字段用 `<sep>` 分隔 | 自动化解析（如 `-s :`） |
| `-h` | 打印服务名的可读名称（如 `<20>` → `File Server Service`） | **只能与 `-v` 搭配使用** |
| `-t <sec>` | 等待响应超时秒数（默认 1） | 慢链路/跨网段调到 2~3 |
| `-b <bps>` | 输出限速（比特/秒） | 慢链路上避免丢包 |
| `-m <n>` | 重传次数（默认 0） | 丢包环境用 `-m 2` |
| `-r` | 使用本地 137 端口发查询 | 老系统（Win95）才需要；**需要 root** |
| `-q` | 抑制 banner 和错误信息 | 脚本化 |
| `--help` | 帮助 | — |

## 5. 实战演练

**环境**：本地实验室。**只扫描你自己搭建或已获得授权的网段**——nbtscan 虽然只是只读查询，但向一个网段发上百个 NetBIOS 查询属于明显的扫描行为。下面所有演练都在自建的 Host-Only 网络中进行。靶机同网段（`192.168.56.0/24`），其中：

- `192.168.56.101`：Metasploitable2（跑 Samba，会响应 NetBIOS）
- `192.168.56.10`：Kali 攻击机
- 纯 Linux/路由设备不会出现在结果里——这正是验证工具行为的好例子

### 场景 1：网段快速普查

```bash
nbtscan 192.168.56.0/24
```

预期输出片段：

```text
Doing NBT name scan for addresses from 192.168.56.0/24

IP address       NetBIOS Name     Server    User             MAC address
------------------------------------------------------------------------------
192.168.56.101   METASPLOITABLE   <server>  METASPLOITABLE   00-00-00-00-00-00
```

解读：
- `METASPLOITABLE` 出现在 `Server` 列，说明它在跑文件服务（`<20>` 后缀存在）——值得进一步查共享。
- `MAC address` 是 `00-00-00-00-00-00`：这是 **Samba 的行为**（它就这么回复），不是工具出错。真实 Windows 会给出真实 MAC。
- `User` 列显示 `METASPLOITABLE`，说明当前无交互登录用户，于是回落到计算机名。

### 场景 2：详细模式看完整名字表

```bash
nbtscan -v -h 192.168.56.101
```

预期输出片段：

```text
NetBIOS Name Table for Host 192.168.56.101:

Incomplete packet, 323 bytes long.

Name             Service          Type
----------------------------------------
METASPLOITABLE   <00>             UNIQUE     Workstation Service
METASPLOITABLE   <20>             UNIQUE     File Server Service
METASPLOITABLE   <03>             UNIQUE     Messenger Service
MSHOME           <00>             GROUP      Domain Name
MSHOME           <1e>             GROUP      Browser Service Elections
MSHOME           <1d>             UNIQUE     Master Browser
__MSBROWSE__     <01>             GROUP      Master Browser

Adapter address: 00-00-00-00-00-00
----------------------------------------
```

解读（这张表信息量很大）：

| 后缀 | 含义 | 情报价值 |
|------|------|----------|
| `<00> UNIQUE` | 工作站服务 | 计算机名 |
| `<20> UNIQUE` | 文件服务器服务 | **有共享可查** |
| `<00> GROUP` | 域/工作组名 | 这里是 `MSHOME` |
| `<1d> UNIQUE` | 主浏览器 | 该机是网段里的浏览器主机 |
| `<1e> GROUP` | 浏览器选举 | 说明存在浏览服务 |
| `__MSBROWSE__ <01>` | 主浏览器组 | 同上 |

拿到 `<20>` 就可以直接去 [enum4linux](enum4linux.md) 列共享了。

### 场景 3：脚本友好输出 + 结果入表

```bash
nbtscan -v -s : 192.168.56.0/24 | tee nbtscan_out.txt
# 输出形如：
# 192.168.56.101:METASPLOITABLE:00U
# 192.168.56.101:METASPLOITABLE:20U
# 192.168.56.101:MSHOME:00G

awk -F: '$3=="00U"{print $1"\t"$2}' nbtscan_out.txt | sort -u > ip_name_map.tsv
column -t ip_name_map.tsv
```

预期输出片段：

```text
192.168.56.101  METASPLOITABLE
```

解读：`-s :` 去掉表头和字段头，`-v` 让每台主机的**每条**名字表记录都单独输出一行，格式为 `IP:名字:后缀类型`。这样既好解析，又保留了服务类型信息（`00U` 工作站、`20U` 文件服务、`00G` 域/工作组）。典型用法是**生成 IP→主机名映射**，供后续报告或 hosts 文件使用（`-e` 可直接输出 `/etc/hosts` 格式）。

## 6. 输出解读

### 默认输出列

| 列 | 含义 | 下一步 |
|----|------|--------|
| `IP address` | 响应的主机 | 记录 |
| `NetBIOS Name` | 计算机名 | 命名/资产识别 |
| `Server` | 有 `<server>` 标记即跑着文件服务 | 去 `smbclient -L` / [enum4linux](enum4linux.md) |
| `User` | 当前登录用户名（无人登录则等于计算机名） | **真实用户名情报**，可做口令喷洒候选（授权内） |
| `MAC address` | 网卡物理地址 | 厂商识别；Samba 常回全 0 |

### 结果判断要点

- **没有结果 ≠ 主机不在线**：可能是纯 Linux、网络设备、或 NetBIOS 被禁用。用 [arp-scan](arp-scan.md) / [nmap](nmap.md) `-sn` 才是通用的存活判断。
- **`User` 列泄露真实用户名**：这是 nbtscan 相对其他存活扫描的独有价值。
- **`<20>` 存在 = 有共享**：直接进入 SMB 枚举阶段。

## 7. 与其他工具配合

```bash
# 1) nmap 存活发现 -> nbtscan 命名
sudo nmap -sn 192.168.56.0/24 -oG - | awk '/Up$/{print $2}' > alive.txt
nbtscan -f alive.txt

# 2) nbtscan -> enum4linux：有 <20>（文件服务）的主机进 SMB 深枚举
nbtscan -v -s : -f alive.txt | awk -F: '$3=="20U"{print $1}' | sort -u > smb_hosts.txt
while read ip; do enum4linux -a "$ip" > "enum_$ip.txt"; done < smb_hosts.txt

# 3) nbtscan -> smbclient：直接列共享
nbtscan -v -s : -f alive.txt | awk -F: '$3=="20U"{print $1}' | sort -u | while read ip; do
  echo "=== $ip ==="; smbclient -N -L "//$ip"
done

# 4) 生成 /etc/hosts 片段（实验室临时命名，别写进生产环境）
nbtscan -e 192.168.56.0/24 | tee /tmp/hosts_lab
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| 结果为空，但主机确实在线 | 目标是纯 Linux / 网络设备，未实现 NetBIOS | 这是预期行为；改用 [arp-scan](arp-scan.md) 或 [nmap](nmap.md) |
| MAC 列全是 `00-00-00-00-00-00` | Samba 就这么回复 | 不是错误；需要真实 MAC 用 [arp-scan](arp-scan.md) |
| `Connection reset by peer`（Windows 2000） | 137 关闭，目标回 ICMP 端口不可达，Win2000 把它报成连接重置 | 忽略即可（nbtscan FAQ 明确说明） |
| 结果时有时无 | UDP 丢包 | 加 `-m 2`（重传），或 `-t 2`（更长超时） |
| `-h` 报参数冲突 | `-h`（可读服务名）只能和 `-v` 一起用 | 改成 `nbtscan -v -h <target>` |
| `-d` 报参数冲突 | `-d` 与 `-v`/`-s`/`-h` 互斥 | 只保留一个 |
| 跨网段（三层）扫描无结果 | 137 UDP 通常不跨路由器转发 | 在本网段内使用 |
| `-r` 报权限错误 | 使用本地 137 端口需要 raw socket | 加 `sudo` |
| 大网段扫描慢 | 默认串行等待超时 | 缩小范围，或先用 [nmap](nmap.md) 筛出存活主机再用 `-f` |

## 9. 防御视角（蓝队）

- **直接关掉**：NetBIOS over TCP/IP 在现代网络中基本没有存在必要。
  - Windows：网卡属性 → IPv4 → 高级 → WINS → 选择「禁用 TCP/IP 上的 NetBIOS」；或组策略统一下发。
  - Samba：`disable netbios = yes`，并关闭 137–139 端口。
- **防火墙**：在边界与主机防火墙封禁 UDP 137、TCP 139（如果不需要 SMBv1/旧共享）。
- **检测**：
  - **网络侧**：同一源 IP 对整段地址连发 UDP 137 是极明显的扫描特征。IDS 规则可以直接对「单位时间内同一源对多个目标 IP 的 137 端口请求数量」告警。
  - **主机侧**：Windows 事件日志中与 NetBIOS 名称查询相关的记录（较难直接观测），主要依赖网络侧检测。
- **信息最小化**：
  - `<03>` 后缀暴露登录用户名是 nbtscan 的核心收益点，禁用 NetBIOS 直接消除这一泄露。
  - 不要把主机名命名为 `dc01`、`sql-prod` 这类直接暴露角色的名字。
- **注意**：nbtscan 是**无害的只读查询**，不会修改目标任何状态。它属于典型的信息泄露问题，而不是可利用漏洞。

## 10. 参考

- 官方仓库（含完整 FAQ）：<https://github.com/resurrecting-open-source-projects/nbtscan>
- Kali 工具页：<https://www.kali.org/tools/nbtscan/>
- man page：`man nbtscan`（含 NetBIOS 后缀对照表，值得通读）
- 用法核实：本教程参数取自 `nbtscan 1.7.2` 的 man page

---

**相关教程**：[enum4linux](enum4linux.md) ｜ [smbclient](smbclient.md) ｜ [arp-scan](arp-scan.md) ｜ [netdiscover](netdiscover.md) ｜ [nmap](nmap.md)
