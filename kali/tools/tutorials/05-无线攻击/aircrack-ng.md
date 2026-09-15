# aircrack-ng（无线审计套件总览）

> **一句话**：一个完整的 802.11 无线审计工具套件——从网卡切换到监听模式、抓包、注入、破解，全部由这一组命令行工具完成。
> **分类**：无线攻击 ｜ **Kali 包**：`aircrack-ng` ｜ **官方文档**：<https://www.aircrack-ng.org/>

## 1. 它解决什么问题

大多数人第一次听到 `aircrack-ng`，以为它是「一个破解 Wi-Fi 密码的命令」。实际上它是**一整套工具**，覆盖无线审计的完整链路：

```text
[1] 准备网卡        airmon-ng       → 打开监听模式
[2] 侦察            airodump-ng     → 发现 AP 与客户端，抓包
[3] 干扰/注入       aireplay-ng     → 抓握手、抓 IV、deauth
[4] 预处理          wpaclean / airdecap-ng / airolib-ng
[5] 破解            aircrack-ng     → WEP / WPA-PSK 破解
[附] 搭建假 AP      airbase-ng
[附] 全自动         besside-ng / wesside-ng
[附] 构造/统计      packetforge-ng / ivstools / kstats
```

**本套件的定位**：CPU 友好、脚本化程度高、覆盖全流程。**它的破解环节不是最快的**——大字典场景应该交给 [hashcat](../04-口令攻击/hashcat.md) `-m 22000`（GPU 加速）。

| 需求 | 用谁 |
| --- | --- |
| 抓握手包 | [airodump-ng](airodump-ng.md) |
| 触发客户端重连以加速抓包 | [aireplay-ng](aireplay-ng.md)（deauth） |
| 测网卡是否支持注入 | [aireplay-ng](aireplay-ng.md) `--test` |
| 破解 WEP / 小字典 WPA | **aircrack-ng** |
| 破解 WPA 大字典 | [hashcat](../04-口令攻击/hashcat.md) `-m 22000` |
| 全自动一条龙 | [wifite](wifite.md) |
| 打 WPS | [reaver](reaver.md) |

## 2. 工作原理

### 2.1 网卡的三种模式

| 模式 | 能做什么 |
| --- | --- |
| **Managed（管理模式）** | 正常上网。只能收到发给自己的帧 |
| **Monitor（监听模式）** | 收到**所有** 802.11 帧（包括别人的），是抓包的**前提** |
| **Master/AP** | 网卡自己充当 AP（`airbase-ng` 用） |

**关键约束**：

- **不是所有网卡都支持监听模式**，更不是所有网卡都支持**注入（injection）**。
- 判断标准是网卡的芯片组，不是品牌。
- 需要支持监听+注入的常见芯片组：Atheros AR9271、Ralink RT3070/RT3572、Realtek RTL8812AU/RTL8814AU、部分 Intel 网卡（监听可以，注入受限）。

**检查方法**：

```bash
# 1) 列出所有无线接口
iw dev
# phy#0
#         Interface wlan0
#                 type managed

# 2) 看网卡支持的模式（关键：monitor 和 AP）
iw list | grep -A 12 'Supported interface modes'
#         Supported interface modes:
#                  * IBSS
#                  * managed
#                  * AP
#                  * AP/VLAN
#                  * monitor        ← 有 monitor 才能抓包
#                  * P2P-client
#                  ...

# 3) 芯片组信息
lsusb          # USB 网卡
lspci          # 内置/PCIe 网卡
airmon-ng      # 列出网卡、驱动、芯片组
```

### 2.2 802.11 的连接过程

要理解破解，必须先理解「客户端如何加入一个 WPA2 网络」：

```
[1] 扫描     客户端广播 Probe Request → AP 回 Probe Response
[2] 认证     Authentication（开放系统，两个帧）
[3] 关联     Association Request / Response
[4] 四次握手  ← ★ 破解的关键就在这里
```

**四次握手（4-way handshake）**：

```
        客户端 STA                                    AP（接入点）
            │                                            │
            │  ←─── ① ANonce（AP 生成的一次性随机数）      │
            │                                            │
            │  ───→  ② SNonce + MIC（客户端一次性随机数）  │
            │                                            │
            │  ←─── ③ GTK + MIC                          │
            │                                            │
            │  ───→  ④ ACK + MIC                         │
            │                                            │
```

**密钥派生链条**：

```text
PMK  = PBKDF2-HMAC-SHA1(passphrase, SSID, 4096 次迭代, 256 位)
                                     ↑
                          盐就是 SSID！所以换了 SSID，PMK 完全不同

PTK  = PRF(PMK, ANonce, SNonce, AP_MAC, STA_MAC)
                ↑ 这就解释了为什么抓包必须包含 msg1 和 msg2（或 msg3 和 msg4）
                  —— 缺了 Nonce 就没法算出 PTK

MIC  = 用 PTK 的一部分（KCK）对握手报文做的完整性校验
       ✓ 如果猜测的口令算出的 PMK → PTK → MIC 与抓到的 MIC 一致，就说明猜对了
```

**这就是离线破解的本质**：对字典里的每一个候选口令，

```
候选口令 → PBKDF2(SSID, 4096) → PMK → PRF → PTK → 算 MIC → 与抓到的 MIC 比对
```

**一次比对 = 4096 次 SHA-1 迭代 + 若干次 HMAC**。这就是为什么 WPA 破解比 MD5 慢好几个数量级——**PBKDF2 的 4096 次迭代是 2004 年故意设计来拖慢攻击的**。

### 2.3 PMKID —— 客户端无关的攻击

2018 年 hashcat 作者 Jens Steube 发现了一条捷径：**PMKID**。

```
PMKID = HMAC-SHA1-128(PMK, "PMK Name" || AP_MAC || STA_MAC)
```

**关键点**：PMKID 的计算**只需要 PMK 和两个 MAC 地址，不需要客户端参与**。

这意味着：

- **不需要等客户端连接**，也不需要 deauth；
- **只需要向 AP 发一个认证请求**，AP 的第一个握手报文里就可能带上 PMKID；
- 抓到一个 PMKID 就能离线验证候选口令。

| | 四次握手 | PMKID |
| --- | --- | --- |
| 需要客户端在线 | ✅ 需要 | ❌ 不需要（**clientless**） |
| 需要 deauth | 通常需要 | 不需要 |
| 抓包难度 | 中等（要抓全 msg1+msg2） | 低（AP 主动给） |
| 支持 WPA3 | — | WPA3 的 transition mode 仍可能暴露 |

**工具**：

```bash
# hcxdumptool + hcxpcapngtool（现代主流方式）
sudo hcxdumptool -i wlan0mon -o dump.pcapng --enable_status=1
hcxpcapngtool -o hash.22000 dump.pcapng
hashcat -m 22000 hash.22000 wordlist.txt

# airodump-ng 也支持抓 PMKID
sudo airodump-ng wlan0mon --bssid AA:BB:CC:DD:EE:FF -c 6 -w cap --wps
```

### 2.4 WPA / WPA2 / WPA3 的差异

| | WPA（WPA1） | WPA2 | WPA3-Personal |
| --- | --- | --- | --- |
| 加密 | TKIP | CCMP（AES） | CCMP |
| 密钥协商 | 4-way handshake | 4-way handshake | **SAE（Dragonfly）** |
| 口令→密钥 | PBKDF2（4096） | PBKDF2（4096） | **SAE 握手，不做 PBKDF2 派生** |
| 被动抓包 + 离线字典 | **有效** | **有效** | **无效**（这是 WPA3 的核心改进） |
| PMF（管理帧保护） | 无 | 可选（802.11w） | **强制** |
| deauth 攻击 | 有效 | 通常有效（除非启用 PMF） | **被 PMF 阻止** |
| 攻击面 | 握手 + WPS | 握手 + PMKID + WPS | 主要剩**在线**猜测与降级/transition 模式 |

**WPA3-SAE 为什么难打**：

- SAE 是**基于密码的认证密钥交换**，双方通过 Dragonfly 握手直接协商出密钥，**没有可离线验证的 MIC**。
- 攻击者即使抓到完整的 SAE 交换，也**无法离线判断某个口令是否正确**——每次验证都必须与 AP 真实交互（在线攻击）。
- SAE 还设计了**防降级**（H2E、anti-clogging）与**前向保密**。
- **已知需要警惕的场景**：**WPA3/WPA2 混合模式（transition mode）**。为了兼容老设备，AP 同时开放 WPA2，此时攻击者可以只对 WPA2 部分下手（包括 deauth、抓握手、PMKID）。**混合模式是现实中 WPA3 实际防护效果打折的主要原因。**

### 2.5 WEP 为什么一分钟就能破

WEP 用 RC4 加一个 **24 位 IV（初始化向量）**。24 位只有 16777216 个值，且规范建议每个包换一次 IV——**在繁忙网络中几小时就会重复**。

IV 重复 + RC4 的弱密钥特性 → 收集足够多的加密包后，**统计攻击可以恢复密钥**：

| 攻击 | 所需 IV 数（量级） |
| --- | --- |
| PTW（Pyshkin–Tews–Weinmann，现代主流，`aircrack-ng` 默认） | 约 4 万 |
| KoreK（更老的统计攻击） | 数十万 |

**WEP 已经完全不可用**：2001 年就被攻破，2004 年成为标准反面教材，2006 年后 WPA2 普及。**在 2026 年还看到 WEP，等于看到一个「没有锁的门」**——这也是为什么它的教程价值主要在于讲原理，实战中几乎遇不到。

### 2.6 为什么需要「注入」

**deauth 攻击**是为了解决一个现实问题：**抓不到握手**。

- 客户端加入网络时才有握手，而你通常是事后才到现场；
- 发出**伪造的 deauthentication 帧**（以 AP 的名义），让客户端误以为被踢下线；
- 客户端自动重连 → **产生新的四次握手** → 你就能抓到了。

**这需要网卡支持「注入」（injection）**——能发送任意原始的 802.11 帧。这就是为什么 `aireplay-ng --test` 是必做的检查。

**重要说明**：deauth 会**短暂中断他人的网络连接**，在大多数司法辖区属于干扰通信。**只能对自己拥有的网络使用**。

## 3. 安装与快速上手

```bash
sudo apt install aircrack-ng
aircrack-ng --help | head -40
```

套件内的全部命令：

```bash
dpkg -L aircrack-ng | grep -E '/(s?bin|usr/bin)/'
# /usr/bin/airbase-ng
# /usr/bin/aircrack-ng
# /usr/bin/airdecap-ng
# /usr/bin/airdecloak-ng
# /usr/bin/aireplay-ng
# /usr/bin/airmon-ng
# /usr/bin/airodump-ng
# /usr/bin/airodump-ng-oui-update
# /usr/bin/airolib-ng
# /usr/bin/airserv-ng
# /usr/bin/airtun-ng
# /usr/bin/besside-ng
# /usr/bin/easside-ng
# /usr/bin/ivstools
# /usr/bin/kstats
# /usr/bin/makeivs-ng
# /usr/bin/packetforge-ng
# /usr/bin/tkiptun-ng
# /usr/bin/wesside-ng
# /usr/bin/wpaclean
```

**最小完整流程**（对自己拥有的 Wi-Fi 与路由器）：

```bash
# 0) 检查
sudo airmon-ng
sudo airmon-ng check kill
iw list | grep -A 12 'Supported interface modes'

# 1) 开监听
sudo airmon-ng start wlan0
# → 接口变成 wlan0mon

# 2) 侦察
sudo airodump-ng wlan0mon

# 3) 锁定目标抓包（假设目标在 6 信道）
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w /tmp/cap wlan0mon

# 4) 另一个终端：deauth 逼客户端重连（只在自有网络做）
sudo aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF wlan0mon

# 5) 看到 airodump 显示 WPA handshake: AA:BB:... 就可停止
#    退出 airodump（Ctrl+C）

# 6) 破解
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b AA:BB:CC:DD:EE:FF /tmp/cap-01.cap

# 7) 或者导出给 hashcat 用 GPU
aircrack-ng -j /tmp/cap-01.cap /tmp/out        # 生成 .hccapx
# 或
hcxpcapngtool -o /tmp/wifi.22000 /tmp/cap-01.cap
hashcat -m 22000 /tmp/wifi.22000 /usr/share/wordlists/rockyou.txt

# 8) 收尾：恢复网卡
sudo airmon-ng stop wlan0mon
sudo systemctl restart NetworkManager
```

## 4. 核心参数详解

`aircrack-ng` 自身的参数（完整解析 WEP/WPA 破解）：

### 通用参数

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-a <mode>` | 强制攻击模式：`1`=WEP，`2`=WPA-PSK | 通常自动判断；有多网络混在抓包文件里时显式指定 |
| `-e <essid>` | 按网络名选择目标 | 比 `-b` 更易读，但 SSID 可被伪造 |
| `-b <bssid>` | 按 AP 的 MAC 选择目标 | **最可靠**，推荐 |
| `-p <nbcpu>` | 使用的 CPU 数（默认全部） | 想留出 CPU 给别的任务时调小 |
| `-q` | 安静模式（不打印状态屏） | 脚本化时用 |
| `-C <macs>` | 把多个 AP 的包合并成一个虚拟 AP | 同一网络的多个 AP（BSSID）时用 |
| `-l <file>` | 把破解出的密钥写入文件 | 留档 |

### 静态 WEP 破解参数

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-n <nbits>` | WEP 密钥长度：`64/128/152/256/512` | 默认自动；不确定时不用指定 |
| `-c` | 只搜字母数字 | 一般不用（自动识别更好） |
| `-t` | 只搜 BCD（二进制编码十进制）字符 | 罕见 |
| `-h` | 针对 Fritz!BOX 的数字密钥 | 特定设备 |
| `-d <mask>` | 使用密钥掩码，如 `A1:XX:CF:YY` | 已知部分密钥时大幅加速 |
| `-m <maddr>` | 按 MAC 过滤可用包 | 指定客户端 MAC 时 |
| `-i <index>` | WEP 密钥索引（1-4），默认任意 | — |
| `-f <fudge>` | 暴力搜索的 fudge factor，默认 2 | — |
| `-k <korek>` | 禁用某个 KoreK 攻击方法（1-17） | 排错 |
| `-x` / `-x0` | 禁用最后一字节的暴力搜索 | — |
| `-x1` | 最后一字节暴力（默认） | — |
| `-x2` | 最后两字节暴力 | 密钥不完整时用 |
| `-K` | 只用旧的 KoreK 攻击（不用 PTW） | 排错对比 |
| `-s` | 破解时以 ASCII 显示密钥 | 观感更好 |
| `-M <num>` | 最多使用多少个 IV | 控制内存 |
| `-P <num>` | PTW 调试：`1`=禁用 Klein，`2`=PTW | 排错 |
| `-1` | 只用一次 PTW 尝试破解 | — |
| `-D` | WEP decloak（跳过损坏的 keystream） | 抓包质量差时 |
| `-V` | 可视化检查模式 | 观察 PTW 的统计 |

### WEP 与 WPA-PSK 通用

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-w <words>` | 字典文件路径（可以是多个） | 配 [wordlists](../04-口令攻击/wordlists.md) |
| `-N <file>` | 新建会话文件 | 长任务 |
| `-R <file>` | 恢复已有会话文件 | 断点续跑 |

### WPA-PSK 专属

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-j <file>` | 生成 **hashcat v3.6+ 的 HCCAPX** 文件 | 交给 [hashcat](../04-口令攻击/hashcat.md) 前用这个 |
| `-J <file>` | 生成旧版 HCCAP 文件 | 老版本 hashcat |
| `-E <file>` | 生成 EWSA 项目文件 v3 | 商业工具用 |
| `-I <str>` | **PMKID 字符串**（对应 hashcat `-m 16800`） | 有 PMKID 时可直接用 |
| `-r <DB>` | 使用 airolib-ng 数据库（预计算 PMK） | **比字典快得多**，见下 |
| `-S` | WPA 破解速度测试 | 先测速度再决定字典大小 |
| `-Z <sec>` | 速度测试的运行秒数 | 配 `-S` |

### SIMD

| 参数 | 作用 |
| --- | --- |
| `--simd-list` | 列出本机可用的 SIMD 架构 |
| `--simd=<option>` | 指定使用：`generic` / `avx512` / `avx2` / `avx` / `sse2` / `altivec` / `power8` / `asimd` / `neon` |

### 其他

| 参数 | 作用 |
| --- | --- |
| `-u` | 显示 CPU 数量与 SIMD 支持情况 |
| `--help` | 显示帮助 |

### 套件内其他命令的参数要点

| 命令 | 用途 | 关键参数 |
| --- | --- | --- |
| `airmon-ng` | 监听模式 | `start/stop/check <iface> [channel]` —— 见 [airmon-ng](airmon-ng.md) |
| `airodump-ng` | 抓包与侦察 | `-c` 信道、`--bssid`、`-w` 前缀、`--wps` —— 见 [airodump-ng](airodump-ng.md) |
| `aireplay-ng` | 注入攻击 | `--deauth`、`--test`、`--fakeauth` —— 见 [aireplay-ng](aireplay-ng.md) |
| `airdecap-ng` | 用已知密钥解密已有 pcap | `-w`（WEP 密钥）、`-p`（WPA 口令）、`-e`（SSID）、`-b`（BSSID）、`-l`（保留 802.11 头）、`-o`（输出文件） |
| `airolib-ng` | 预计算 PMK 数据库 | `--import essid/passwd`、`--batch`、`--stats`、`--verify`、`--export cowpatty` |
| `airbase-ng` | 伪造 AP | `-a`（BSSID）、`-e`（ESSID）、`-c`（信道）、`-z/-Z`（WPA/WPA2 标签）、`-P`（响应所有 probe） |
| `besside-ng` | 全自动抓包破解 | `-b`（BSSID）、`-c`（信道）、`-W`（仅 WPA）、`-v` |
| `packetforge-ng` | 构造/注入自定义帧 | `--arp`/`--udp`/`--icmp`/`--null`、`-w`（输出文件）、`-y`（PRGA 文件） |
| `wpaclean` | 清理 pcap，只留握手 | `wpaclean <out.cap> <in.cap> [in2.cap]...` |
| `makeivs-ng` | 生成含 IV 的测试 pcap | 调试用 |
| `ivstools` | IVS 格式合并/转换 | — |
| `kstats` | 统计 KoreK 攻击效果 | 调试 |
| `airserv-ng` | 把网卡通过网络共享给其他主机 | 分布式抓包 |
| `airtun-ng` | 建隧道（注入/接收） | — |
| `easside-ng` | 无客户端时破解 WEP | — |
| `wesside-ng` | 自动 WEP 破解 | — |
| `tkiptun-ng` | TKIP 注入 | 研究用 |
| `airdecloak-ng` | 去除 WEP 的 cloaking | — |
| `airgraph-ng` | 从 CSV 生成拓扑图 | 可视化报告 |
| `buddy-ng` | easside-ng 的辅助组件 | — |

## 5. 实战演练

**环境声明（本目录全部章节适用）**：

> 以下所有无线操作**只能**在以下环境进行：
>
> - **你自己拥有的 Wi-Fi 网络与你自己的路由器**；
> - 你**自己搭建的隔离无线实验室**（例如：一个旧路由器 + 一块支持监听的网卡，在 Faraday 屏蔽箱/远离他人的环境中）；
> - 有**书面授权**的无线渗透测试（明确授权 SSID、时间窗、攻击类型）；
> - 专门设计用于无线练习的 CTF/靶场。
>
> **严禁**对邻居的 Wi-Fi、公司网络、公共场所热点执行本目录的任何命令。**deauth 攻击会中断他人的网络通信**，在多数司法辖区构成违法。

**推荐的隔离实验环境**：

```text
[一块支持监听+注入的 USB 网卡] → 你的 Kali 虚拟机
        ↓
[自备的旧家用路由器] 设置 SSID "lab-test"，口令你已知
        ↓
[一台测试设备] 手机/笔记本，连上该 SSID，用于产生握手
```

### 场景 0：硬件检查（必做，否则后面全是浪费时间）

**步骤 1：看网卡支持什么模式**

```bash
iw list | grep -A 12 'Supported interface modes'
```

**判读**：

```
* monitor      ← 必须有这个才能抓包
* AP           ← 有它才能用 airbase-ng 建假 AP
```

如果**没有 `monitor`**：这块网卡不能用，换一块（Atheros AR9271、Ralink RT3070、Realtek RTL8812AU 是常见的好选择）。

**步骤 2：看 airmon-ng 的识别结果**

```bash
sudo airmon-ng
```

**预期输出**

```
PHY     Interface       Driver          Chipset

phy0    wlan0            ath9k_htc      Atheros Communications, Inc. AR9271 802.11n
```

`Chipset` 一列很关键——上网搜一下这块芯片是否支持注入。

**步骤 3：确认是 USB 还是 PCIe**

```bash
lsusb | grep -i wireless
lspci | grep -i network
```

**没有合适硬件怎么办？** 见下面「场景 4：只用抓包文件练习」。

### 场景 1：完整流程 —— 抓 WPA2 握手包并破解

**目标**：你自己的路由器，SSID `lab-test`，口令你自己设的（例如 `labpassword123`）。

**步骤 1：开启监听模式**

```bash
sudo airmon-ng check kill
sudo airmon-ng start wlan0
```

**预期输出**

```
Found 2 processes that could cause trouble.
Killing these processes:

  PID Name
 1234 wpa_supplicant
 5678 NetworkManager

PHY     Interface       Driver          Chipset
phy0    wlan0           ath9k_htc       Atheros ... AR9271

                (mac80211 monitor mode vif enabled for [phy0]wlan0 on [phy0]wlan0mon)
                (mac80211 station mode vif disabled for [phy0]wlan0)
```

**注意输出里的接口名**：新版是 `wlan0mon`，老版可能是 `mon0`。**后面所有命令都要用实际的名字**。

**步骤 2：侦察，找到目标**

```bash
sudo airodump-ng wlan0mon
```

**预期输出**

```
 BSSID              PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID
 AA:BB:CC:DD:EE:FF  -42       85       12    0   6  130   WPA2 CCMP   PSK  lab-test
 11:22:33:44:55:66  -67      140        0    0   1  130   WPA2 CCMP   PSK  neighbor-net

 BSSID              STATION            PWR   Rate    Lost    Frames  Notes  Probes
 AA:BB:CC:DD:EE:FF  12:34:56:78:9A:BC  -38    0-1      0       23
```

**解读**：

| 列 | 含义 | 关注点 |
| --- | --- | --- |
| `BSSID` | AP 的 MAC | 记下目标的值 |
| `PWR` | 信号强度（dBm） | -30 很强，-80 很弱 |
| `CH` | 信道 | **抓包必须锁定这个信道** |
| `ENC / CIPHER / AUTH` | 加密 / 密码算法 / 认证方式 | `WPA2 CCMP PSK` 是典型家用配置 |
| `ESSID` | 网络名 | — |
| 下半部分 `STATION` | **已连接的客户端 MAC** | **有客户端 = 能抓握手** |

**关键判断**：如果**下半部分为空**（没有客户端），抓握手的成功率会很低——需要用 PMKID 方式，或者等客户端上线。

**步骤 3：锁定信道抓包**

```bash
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w /tmp/wpa wlan0mon
```

| 参数 | 作用 |
| --- | --- |
| `-c 6` | 锁定信道 6（**必须**，否则会跳频丢包） |
| `--bssid AA:...` | 只看这个 AP |
| `-w /tmp/wpa` | 抓包写 `/tmp/wpa-01.cap`、`/tmp/wpa-01.csv` 等 |

**预期输出（关键行）**

```
 CH  6 ][ Elapsed: 12 s ][ 2026-09-15 11:20

 BSSID              PWR RXQ  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID
 AA:BB:CC:DD:EE:FF  -42 100      185       42    3   6  130   WPA2 CCMP   PSK  lab-test

 BSSID              STATION            PWR   Rate    Lost    Frames  Notes  Probes
 AA:BB:CC:DD:EE:FF  12:34:56:78:9A:BC  -38    1e- 1      0      42
```

**步骤 4：另一个终端触发重连**

```bash
sudo aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF wlan0mon
```

**预期输出**

```
11:21:03  Waiting for beacon frame (BSSID: AA:BB:CC:DD:EE:FF) on channel 6
11:21:04  Sending 64 directed DeAuth (code 7). STMAC: [12:34:56:78:9A:BC] [ 8|14 ACKs]
```

**解读**：发送 64 个定向 deauth 帧，收到 8 个 ACK。ACK 数 > 0 说明**注入成功**。

**步骤 5：观察 airodump-ng，抓到握手**

回到抓包终端，右上角出现：

```
 CH  6 ][ Elapsed: 45 s ][ 2026-09-15 11:21 ][ WPA handshake: AA:BB:CC:DD:EE:FF
```

**`WPA handshake: AA:BB:CC:DD:EE:FF` 就是成功标志**。此时按 `Ctrl+C` 停止抓包。

**步骤 6：破解（小字典先试）**

```bash
# 准备一个小字典（自己的口令）
printf 'wrongpass\nlabpassword123\ntest1234\n' > /tmp/lab.txt

aircrack-ng -w /tmp/lab.txt -b AA:BB:CC:DD:EE:FF /tmp/wpa-01.cap
```

**预期输出**

```
                               Aircrack-ng 1.7

      [00:00:00] 3/3 keys tested (1245.32 k/s)

      Time left: 0 seconds                                      0.24%

                           KEY FOUND! [ labpassword123 ]


      Master Key     : 1B 2C 3D 4E 5F 60 71 82 93 A4 B5 C6 D7 E8 F9 0A ...
      Transient Key  : ...
      EAPOL HMAC     : ...
```

**`KEY FOUND! [ labpassword123 ]` 就是结果。**

**步骤 7：收尾**

```bash
sudo airmon-ng stop wlan0mon
sudo systemctl restart NetworkManager
```

### 场景 2：用 hashcat 加速（大字典的正确做法）

`aircrack-ng` 的破解是 **CPU + 单机**的，速度大约每秒几千到几万次。同硬件下 GPU 的 [hashcat](../04-口令攻击/hashcat.md) 能快**一到两个数量级**。

**步骤 1：转换抓包格式**

```bash
# 方式 A：aircrack-ng 自带（生成 HCCAPX）
aircrack-ng -j /tmp/wpa-converted /tmp/wpa-01.cap
ls /tmp/wpa-converted*
# /tmp/wpa-converted.hccapx      ← 老格式

# 方式 B（推荐）：hcxpcapngtool 生成 hashcat 22000 格式
sudo apt install hcxtools
hcxpcapngtool -o /tmp/wifi.22000 /tmp/wpa-01.cap
cat /tmp/wifi.22000
# WPA*01*...*labtest*...       ← 22000 格式的一行
```

**步骤 2：hashcat 跑**

```bash
hashcat -m 22000 /tmp/wifi.22000 /usr/share/wordlists/rockyou.txt -O
hashcat -m 22000 /tmp/wifi.22000 /tmp/lab.txt --show
```

**为什么用 `-m 22000` 而不是 `-m 16800`**：22000 是 hashcat 6.0 引入的统一格式，**同时支持 PMKID 与 EAPOL（握手）**，且兼容 2500（WPA-EAPOL-PBKDF2）、16800（PMKID）等旧模式。

**步骤 3：PMKID 场景（不需要客户端）**

如果你手上是 PMKID 而不是握手包：

```bash
# 用 aircrack-ng 直接解 PMKID
aircrack-ng -w /tmp/lab.txt -I <PMKID字符串> /tmp/wpa-01.cap
# 或
hcxpcapngtool -o /tmp/pmkid.22000 dump.pcapng
hashcat -m 22000 /tmp/pmkid.22000 /tmp/lab.txt
```

### 场景 3：使用 airolib-ng 预计算 PMK（大字典的加速技巧）

**原理**：字典里每个候选口令对**固定 SSID** 的 PMK 是固定的。PBKDF2 的 4096 次迭代占了一次尝试的大部分时间。如果**先算好 PMK 存库**，之后每次破解只需做 PRF + MIC 比对——**快得多**。

**代价**：预计算本身要花时间，**只在你需要反复破解同一个 SSID 的多个抓包时划算**。

```bash
# 1) 建库
airolib-ng /tmp/lab.db --stats

# 2) 导入 SSID 与字典
airolib-ng /tmp/lab.db --import essid <(echo 'lab-test')
airolib-ng /tmp/lab.db --import passwd /usr/share/wordlists/rockyou.txt

# 3) 批量计算 PMK（这一步最慢，去泡杯茶）
airolib-ng /tmp/lab.db --batch

# 4) 查看统计
airolib-ng /tmp/lab.db --stats

# 5) 用库来破解（-r 代替 -w）
aircrack-ng -r /tmp/lab.db -b AA:BB:CC:DD:EE:FF /tmp/wpa-01.cap
```

`--batch` 输出的进度会显示 `Computed 12345 PMK in ...`。第 5 步的破解速度会比纯字典模式**快一个数量级量级**（因为它跳过了 PBKDF2）。

**注意**：**库与 SSID 绑定**。同一个库不能用于别的 ESSID（因为 SSID 是 PBKDF2 的盐）。

### 场景 4：没有合适硬件怎么办 —— 只用抓包文件练习

这是**最安全的练习方式**：不发射任何信号，只分析已有的抓包文件。

**获取练习抓包文件的合法途径**：

| 来源 | 说明 |
| --- | --- |
| `aircrack-ng` 自带测试包 | 安装后查找 `.cap` 测试文件 |
| Wireshark 示例抓包 | <https://wiki.wireshark.org/SampleCaptures> 有 802.11 示例 |
| 自己以前抓的自有网络抓包 | 最真实 |
| CTF 靶场提供的抓包 | 有授权 |

```bash
# 查找本机的示例抓包
find /usr/share -name '*.cap' -o -name '*.pcap' 2>/dev/null | head -20

# 用 aircrack-ng 分析（不需要网卡）
aircrack-ng /tmp/wpa-01.cap

# 用 airodump-ng 从文件回放（-r 参数）
sudo airodump-ng -r /tmp/wpa-01.cap

# 用 wpaclean 清理，只保留握手
wpaclean /tmp/clean.cap /tmp/wpa-01.cap

# 用 tshark / wireshark 分析
tshark -r /tmp/wpa-01.cap -Y 'eapol' -c 20
wireshark /tmp/wpa-01.cap
```

**这条路径同样能学到 90% 的知识**：握手结构、EAPOL 报文、字典破解流程、hashcat 转换。**唯一的差别是你不能练「抓包」这一步**。

### 场景 5：解密已经抓到的加密流量

**前提**：你已经用合法手段知道了口令（比如你自己的网络）。

```bash
# WPA：用口令解密
airdecap-ng -p labpassword123 -e lab-test -b AA:BB:CC:DD:EE:FF /tmp/wpa-01.cap
# 生成 /tmp/wpa-01-dec.cap

# WEP：用密钥解密
airdecap-ng -w 1A2B3C4D5E -e lab-test /tmp/wep-01.cap

# 保留 802.11 头（默认会去掉）
airdecap-ng -l -p labpassword123 -e lab-test /tmp/wpa-01.cap

# 用 Wireshark 打开解密后的文件
wireshark /tmp/wpa-01-dec.cap
```

**Wireshark 侧也可以在图形界面里配置解密**：`Preferences → Protocols → IEEE 802.11 → Decryption keys`，添加 `wpa-pwd` 或 `wpa-psk`。

## 6. 输出解读

### aircrack-ng 的破解输出

```
                               Aircrack-ng 1.7

      [00:00:02] 14344392/14344392 keys tested (7211452.32 k/s)

      Time left: 0 seconds                                     100.00%

                           KEY FOUND! [ labpassword123 ]


      Master Key     : 1B 2C 3D 4E 5F 60 71 82 93 A4 B5 C6 D7 E8 F9 0A
                       1B 2C 3D 4E 5F 60 71 82 93 A4 B5 C6 D7 E8 F9 0A

      Transient Key  : 3C 4D 5E 6F 70 81 92 A3 B4 C5 D6 E7 F8 09 1A 2B
                       3C 4D 5E 6F 70 81 92 A3 B4 C5 D6 E7 F8 09 1A 2B
                       3C 4D 5E 6F 70 81 92 A3 B4 C5 D6 E7 F8 09 1A 2B
                       3C 4D 5E 6F 70 81 92 A3 B4 C5 D6 E7 F8 09 1A 2B

      EAPOL HMAC     : 4D 5E 6F 70 81 92 A3 B4 C5 D6 E7 F8 09 1A 2B 3C
```

| 字段 | 含义 | 价值 |
| --- | --- | --- |
| `N/M keys tested (X k/s)` | 已试 N 个，共 M 个；速率 X 千次/秒 | 估算耗时 |
| `Time left` | 预计剩余时间 | **决定是否换 hashcat** |
| `KEY FOUND! [ ... ]` | **口令明文** | 结果 |
| `Master Key` | PMK（32 字节） | 可用于 `airdecap-ng -k` 解密流量 |
| `Transient Key` | PTK（64 字节，4 段） | 解密数据帧 |
| `EAPOL HMAC` | 握手的 MIC | 验证用 |

### 抓包失败的常见信号

| 信号 | 含义 | 解决 |
| --- | --- | --- |
| airodump 上半部分有 AP，下半部分**空** | 没有客户端连接 | 换 PMKID 方式，或等客户端上线 |
| `WPA handshake:` 一直不出现 | 没抓到完整握手（缺 msg1 或 msg2） | 多发几次 deauth；确认 `-c` 锁定同一信道 |
| deauth 的 ACK 数为 0 | **注入失败** | 换网卡；检查是否支持注入；用 `aireplay-ng --test` 验证 |
| 信道不匹配 | airodump 在跳频而目标在别的信道 | 显式加 `-c <信道>` |
| `No networks found` | 网卡没进监听模式 | `airmon-ng start` 是否成功？接口名对不对？ |

**判断成功**：`KEY FOUND!` 出现。

**下一步**：

| 结果 | 动作 |
| --- | --- |
| 找到口令 | 用 `airdecap-ng -p` 解密流量；在报告中记录口令强度问题 |
| 没找到 | 导出 HCCAPX/22000 → [hashcat](../04-口令攻击/hashcat.md) 用 GPU 跑大字典；或 [cewl](../04-口令攻击/cewl.md) 造定向字典 |
| 握手没抓到 | 用 [aireplay-ng](aireplay-ng.md) 多发 deauth；或改用 PMKID |
| 目标是 WPA3 | 见 2.4 节——**纯 WPA3 无法离线破解**；检查是否为混合模式 |

## 7. 与其他工具配合

```text
                    ┌─────────────────────────────────────────┐
                    │            aircrack-ng 套件              │
                    │                                         │
[网卡] → airmon-ng ─┤→ airodump-ng（抓包）                    │
                    │        ↑                                │
                    │   aireplay-ng（deauth / 注入）           │
                    │        ↓                                │
                    │   wpaclean（清理）                       │
                    │        ↓                                │
                    │   aircrack-ng（CPU 破解）                │
                    │        ↓                                │
                    │   airolib-ng（预计算加速）                │
                    └─────────────────────────────────────────┘
                                 ↓ -j / hcxpcapngtool
                    ┌─────────────────────────────────────────┐
                    │  hashcat -m 22000（GPU 破解，快 10~100×） │
                    └─────────────────────────────────────────┘

[一体化] wifite（调用上述全部）
[WPS]    reaver / wash
[被动]   kismet（WIDS / 侦测）
[现代]   bettercap（wifi.recon 模块 + PMKID）
[字典]   cewl / crunch / wordlists
```

**关键衔接点**：

| 从 | 到 | 命令 |
| --- | --- | --- |
| airodump-ng | aircrack-ng | 直接 `.cap` 文件 |
| aircrack-ng | hashcat | `aircrack-ng -j out cap` → `.hccapx`；或用 `hcxpcapngtool` |
| aircrack-ng | Wireshark | `airdecap-ng -p <pw>` 解密后打开 |
| 任意抓包 | 22000 格式 | `hcxpcapngtool -o out.22000 in.cap` |
| Wi-Fi 口令字典 | cewl/crunch | 用 [cewl](../04-口令攻击/cewl.md) 爬组织站点，或 [crunch](../04-口令攻击/crunch.md) 按结构生成 |

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `iw list` 里**没有 `monitor`** | 网卡驱动/芯片不支持监听 | **换网卡**。软件层面无解 |
| `airmon-ng start` 后没有新接口 | 驱动不支持 `mac80211` 的 vif | 更新驱动；或用 `ip link set wlan0 down; iw wlan0 set monitor control; ip link set wlan0 up` 手工切 |
| `airmon-ng check kill` 后**断网了** | 它杀掉了 `NetworkManager` 和 `wpa_supplicant` | **这是预期行为**。收尾时 `sudo airmon-ng stop wlan0mon && sudo systemctl restart NetworkManager` |
| `ERROR: Could not determine current channel` | 网卡未锁定信道 | 显式加 `-c <信道>` |
| `aireplay-ng --deauth` 输出 ACK 数 0 | **注入不工作** | 用 `aireplay-ng --test wlan0mon` 验证；换网卡；某些驱动需要关掉 `mac80211` 的功率管理 |
| `aireplay-ng --test` 报 `No answer to probe request` | 网卡注入被驱动阻止 | 换网卡；试 `--ignore-negative-one` |
| 抓到的是 `.cap` 但 aircrack 说 `No networks found` | 抓包文件里没有目标，或未锁定信道 | 用 `airodump-ng -r file.cap` 检查内容 |
| `No valid WPA handshakes found` | 握手不完整（缺 msg1 或 msg2） | 重新抓；`wpaclean` 清理后重试；多发 deauth |
| 破解很慢（几千 k/s） | aircrack-ng 是 CPU 实现 | **导出给 hashcat** 用 GPU |
| 字典行数很多但一秒就完了 | 抓包文件里没有有效握手，或 `-b` 指定错 | 用 `wpaclean` 清理并确认握手存在 |
| 目标是 WPA3 但抓到了握手 | 可能是**混合模式**（WPA3/WPA2 transition） | 只能对 WPA2 部分下手；纯 WPA3 无法离线破解 |
| `hcxpcapngtool` 不输出 22000 格式 | 抓包里没有有效 PMKID/EAPOL | 检查抓包质量；用 `hcxpcapngtool -v` 看诊断 |
| 网卡在虚拟机里不工作 | USB 直通未配置 | VirtualBox/VMware 里把 USB 设备直通给虚拟机 |
| 在虚拟机里监听不到任何东西 | 无线直通问题 | **推荐用物理机 + USB 网卡**，或配置 USB 直通 |
| 破解出了口令但连不上 | 抓的是旧口令（路由器改过） | 确认抓包时间；重新抓 |
| `-w` 字典是 `.gz` | 未解压 | `gunzip`（见 [wordlists](../04-口令攻击/wordlists.md)） |

### 一张排错决策图

```text
抓不到握手
├── 没有客户端？
│     → 改用 PMKID（hcxdumptool / airodump --wps）
│     → 或等客户端上线
├── 有客户端但 deauth 无效？（ACK = 0）
│     → 注入失败 → 换网卡 / aireplay-ng --test 诊断
├── deauth 有效但抓不到完整握手？
│     → 信道没锁定 → 加 -c
│     → 客户端离太远 → 靠近 AP
│     → 多发几次 deauth（每次 3~5 个就够，太多会造成拒绝服务）
└── 目标启用了 PMF（802.11w）？
      → deauth 会被忽略 → 只能被动等待自然握手，或改用 PMKID
```

## 9. 防御视角（蓝队）

### 9.1 攻击面与对策总表

| 攻击 | 前提 | 蓝队对策 | 有效性 |
| --- | --- | --- | --- |
| 监听 + 抓握手 | 网卡支持监听 | **无法阻止**（被动接收） | ❌ 被动监听不可防 |
| 离线字典破解口令 | 抓到握手/PMKID | **WPA3-SAE**（首选）；**长随机 PSK（≥ 20 字符）** | ✅ 有效 |
| deauth 攻击 | 无 PMF | **启用 802.11w（PMF）** | ✅ 有效 |
| PMKID 抓取 | WPA2 的 RSN IE | WPA3-SAE；或在 AP 上禁用相关特性 | ✅ 有效 |
| WPS PIN 暴力 | WPS 开启 | **关闭 WPS**（尤其是 PIN 方式） | ✅ 有效 |
| 伪造 AP / 邪恶孪生 | 客户端会主动连接同名 SSID | **802.1X/EAP-TLS（证书认证）**；WPA3；客户端配置「不自动连接开放网络」 | ✅ 有效 |
| WEP 破解 | 网络使用 WEP | **立刻换成 WPA3 或 WPA2-AES** | ✅ 必做 |

### 9.2 优先级最高的五条措施

```text
1. 升级到 WPA3-SAE（或至少 WPA2-AES + PMF），彻底弃用 WEP 与 TKIP
2. 关闭 WPS（BIOS/管理界面里的 "Wi-Fi Protected Setup" 设为 Disabled）
3. PSK 长度 ≥ 20 位且随机（不要用词表里可能出现的组合）
4. 企业环境用 802.1X + EAP-TLS（每个设备独立证书），避免共享 PSK
5. 启用管理帧保护（802.11w / PMF）以阻断 deauth
```

### 9.3 检测与监控

无线侧的检测与有线侧逻辑不同，核心是 **WIDS（无线入侵检测系统）**：

| 行为 | 检测方式 | 工具 |
| --- | --- | --- |
| **deauth 洪泛** | 统计单位时间内的 deauth/disassoc 帧数量；**正常网络中 deauth 应该是罕见的** | [kismet](kismet.md)、WIDS 功能、企业 AP 控制器的告警 |
| **基于同一原因的批量 deauth** | deauth 的 reason code 分布异常集中（工具默认用 code 7） | kismet 告警 / 自定义解析 |
| **邪恶孪生（Evil Twin）** | 同一 SSID 出现多个 BSSID，其中一个是本地的、信号突然很强 | [kismet](kismet.md)、WIPS |
| **伪造 AP** | 出现未授权的 BSSID；加密配置与基线不同 | WIPS |
| **PMKID 探测** | AP 收到异常大量的关联请求（PMKID 攻击的副产品） | AP 日志 |
| **监听的网卡** | **无法可靠检测**（被动接收，不发射任何东西） | ❌ |
| **WPS 暴力** | AP 的 WPS 状态机异常、大量 M4/M6 报文 | AP 日志 + WIPS |

**deauth 检测的规则思路**：

```text
if count(deauth_frames, src=bssid, 10s) > 20
   or count(distinct reason_codes, 60s) == 1 and deauth_count > 10
then alert "possible deauth flood / handshake capture attempt"
```

**注意**：现代工具（如 `mdk4`）可以**伪造源 MAC**，让 deauth 看起来来自不同的 BSSID，从而绕过基于源地址的简单阈值规则。因此更可靠的做法是：

- 统计**总的** deauth 帧速率（不区分源）；
- 结合**同一时间窗内是否有新的客户端重连**（deauth 会导致重连 → 重连风暴是强信号）。

### 9.4 一个容易被忽略的点：物理层与人员

- **屏蔽箱 / Faraday 袋**：对高安全区域，物理屏蔽比任何协议都有效。
- **访客网络隔离**：把访客 Wi-Fi 与内网彻底隔离，即使访客 Wi-Fi 被攻破也不影响内网。
- **不要用公司名/产品名做 SSID**：SSID 是 PBKDF2 的盐，同时也是 [cewl](../04-口令攻击/cewl.md) 的素材。
- **员工培训**：不要连接来源不明的同名热点（邪恶孪生的主要入口是**用户主动连接**，而不是技术漏洞）。

## 10. 参考

- 官方站点与文档：<https://www.aircrack-ng.org/>
- 官方文档（各工具详解）：<https://www.aircrack-ng.org/doku.php?id=aircrack-ng>
- Kali 工具页：<https://www.kali.org/tools/aircrack-ng/>
- 本机手册：`man aircrack-ng`、`man airmon-ng`、`man airodump-ng`、`man aireplay-ng`、`man airdecap-ng`、`man airolib-ng`、`man airbase-ng`
- 本机帮助：`aircrack-ng --help`、`airodump-ng --help`、`aireplay-ng --help`
- 相关本目录：[airmon-ng](airmon-ng.md)、[airodump-ng](airodump-ng.md)、[aireplay-ng](aireplay-ng.md)、[wifite](wifite.md)、[reaver](reaver.md)、[kismet](kismet.md)、[bettercap](bettercap.md)
- 相关其他目录：[hashcat](../04-口令攻击/hashcat.md)、[wordlists](../04-口令攻击/wordlists.md)、[cewl](../04-口令攻击/cewl.md)

## ⚠️ 法律与伦理

无线攻击相关行为的法律风险**远高于**有线侧，原因有三：

1. **无线信号天然跨越物理边界**——你很难证明「信号只覆盖了我自己的财产」；
2. **监听本身即在接收他人通信**——在许多司法辖区，即使不破解，单纯的截获通信内容已违法；
3. **deauth 等注入攻击属于干扰通信**，可能构成破坏计算机信息系统。

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条 | 非法侵入计算机信息系统；非法获取计算机信息系统数据 |
| 《刑法》 | 第二百八十六条 | 破坏计算机信息系统（deauth 造成网络中断属于此类） |
| 《无线电管理条例》 | 相关条款 | 擅自使用无线电频率、干扰合法无线电业务 |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《个人信息保护法》 | 相关条款 | 截获、窃取通信内容涉及个人信息处理 |

**本教程仅适用于**：

- ✅ **你自己拥有的 Wi-Fi 网络与你自己的路由器**
- ✅ 有**书面授权**、明确列出授权 SSID 与时间窗的无线渗透测试
- ✅ 你自己搭建的隔离无线实验室（有屏蔽措施，不干扰他人）
- ✅ CTF 靶场 / 专门授权的无线练习平台

**严禁**：

- ❌ 对邻居、公司、公共场所的任何 Wi-Fi 执行本文任何命令
- ❌ deauth 任何不属于你的网络（会中断他人通信）
- ❌ 在授权范围之外扩大目标（多测一个 SSID 都是越权）
- ❌ 将抓到的握手包用于任何非授权目的

**如果你只是想学习**：请使用「场景 4：只用抓包文件练习」的方式，或在自己的隔离环境中搭建实验网络。**这是最安全、也是完全足够的学法。**
