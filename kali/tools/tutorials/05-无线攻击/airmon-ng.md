# airmon-ng（无线网卡监听模式管理）

> **一句话**：把无线网卡切换成监听模式（monitor mode）、列出网卡与芯片信息、检查并清理会干扰抓包的进程。
> **分类**：无线攻击 ｜ **Kali 包**：`aircrack-ng`（airmon-ng 是套件中的一个脚本）｜ **官方文档**：<https://www.aircrack-ng.org/doku.php?id=airmon-ng>

## 1. 它解决什么问题

**802.11 抓包的第一步永远是「让网卡能听到所有帧」**。默认情况下网卡工作在托管模式（managed）——它只接收发给自己的帧。要抓别人的握手包，必须切到监听模式。

airmon-ng 就是做这件事的：

| 它做什么 | 为什么需要 |
| --- | --- |
| 列出无线接口、驱动、芯片组 | **判断网卡是否支持监听/注入**的唯一入口 |
| 切换监听模式 | [airodump-ng](airodump-ng.md) 等工具的前提 |
| 切回托管模式 | 收尾恢复上网 |
| 检查/清理干扰进程 | `NetworkManager`、`wpa_supplicant` 会反复把网卡切回托管模式，导致抓包中途失败 |

**注意它不做什么**：airmon-ng **不做抓包、不做注入、不做破解**。它只是「准备阶段」的工具。如果你只想跑一条命令搞定一切，用 [wifite](wifite.md)。

## 2. 工作原理

### 2.1 网卡的工作模式

| 模式 | 内核层面 | 效果 |
| --- | --- | --- |
| `managed` | 正常的 station 模式 | 只收自己的帧，能上网 |
| `monitor` | 接收所有 802.11 帧（含 FCS） | **抓包必需** |
| `AP` / `master` | 网卡自己当 AP | `airbase-ng` / `bettercap` 用 |
| `IBSS` | Ad-hoc | 罕见 |

### 2.2 两种实现方式

airmon-ng 通过 **`iw`** 操作网卡的无线扩展。早期（2013 年前）驱动会给同一块网卡创建两个虚拟接口（如 `wlan0` + `mon0`）；现代 `mac80211` 驱动采用 **vif（virtual interface）** 方式：

```
mac80211 monitor mode vif enabled for [phy0]wlan0 on [phy0]wlan0mon
mac80211 station mode vif disabled for [phy0]wlan0
```

**含义**：

- 它**新建了一个接口 `wlan0mon`**（注意后缀 `mon`）；
- 同时**禁用了原来的托管模式接口** `wlan0`。

**这解释了两件事**：

1. **接口名会变**——后续命令要用 `wlan0mon` 而不是 `wlan0`。老机器的接口名可能是 `mon0`，**以实际输出为准**。
2. **切过去之后就不能上网了**——因为托管模式被禁用。这是设计如此，不是故障。

### 2.3 为什么要杀掉 NetworkManager

`NetworkManager`、`wpa_supplicant`、`dhclient`、`avahi-daemon` 这些进程会：

- 定期扫描可用网络 → **强迫网卡离开监听模式**去扫频；
- 尝试自动连接 → 又切换一次模式；
- 结果是：**抓包刚开始还行，几十秒后突然什么都抓不到了**。

airmon-ng 的 `check kill` 就是预先清理它们。

**代价**：杀掉 `NetworkManager` 后**你的有线/无线网络都会断**。必须记住收尾时恢复：

```bash
sudo airmon-ng stop wlan0mon
sudo systemctl restart NetworkManager
```

### 2.4 硬件能力矩阵（决定你能做什么）

| 能力 | 需要什么 | 依赖 |
| --- | --- | --- |
| 监听（抓包） | `iw list` 里有 `monitor` | 驱动支持 |
| 注入（deauth） | 网卡固件+驱动支持 raw 帧注入 | **比监听要求更高** |
| AP 模式 | `iw list` 里有 `AP` | 驱动支持 |

**判断能否注入的唯一可靠方法**：实测 `aireplay-ng --test <iface>`（见 [aireplay-ng](aireplay-ng.md)）。

**常见好用的芯片组**：

| 芯片组 | 监听 | 注入 | 备注 |
| --- | --- | --- | --- |
| Atheros AR9271 | ✅ | ✅ | USB，最经典，5 GHz 不支持 |
| Ralink RT3070 / RT3572 | ✅ | ✅ | USB，稳定 |
| Realtek RTL8812AU / RTL8814AU | ✅ | ✅ | 支持 5 GHz，需编译驱动 |
| Ralink RT5572 | ✅ | ✅ | 双频 |
| 多数 Intel 内置网卡 | ✅ | ❌/受限 | **常见坑**：能抓不能注入 |
| Broadcom（多数 Mac/部分笔记本） | ❌ | ❌ | 基本不能用 |

## 3. 安装与快速上手

airmon-ng 随 `aircrack-ng` 一起安装：

```bash
sudo apt install aircrack-ng
airmon-ng -h
```

**官方帮助输出**：

```
usage: airmon-ng <start|stop> <interface> [channel] or airmon-ng <check|check kill>
```

**最短工作流**：

```bash
# 1) 看网卡
sudo airmon-ng

# 2) 清理干扰进程
sudo airmon-ng check kill

# 3) 开启监听
sudo airmon-ng start wlan0

# 4) ……用 airodump-ng / aireplay-ng 干活……

# 5) 恢复
sudo airmon-ng stop wlan0mon
sudo systemctl restart NetworkManager
```

## 4. 核心参数详解

### 4.1 子命令

| 子命令 | 作用 | 使用建议 |
| --- | --- | --- |
| `airmon-ng`（无参数） | 列出所有无线接口、驱动、芯片组 | **每次开始前先跑这个** |
| `airmon-ng start <iface> [channel]` | 开启监听模式 | 可选带信道，如 `start wlan0 6` |
| `airmon-ng stop <iface>` | 关闭监听，恢复托管模式 | 收尾必做 |
| `airmon-ng check` | 只列出可能干扰的进程，**不杀** | 想先看看有什么 |
| `airmon-ng check kill` | 列出并**杀掉**干扰进程 | 抓包前推荐；**会断网** |

### 4.2 可选参数

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `<channel>` | 开启监听时直接锁定信道 | 已知目标信道时**强烈建议**，避免跳频丢包 |
| `--verbose` | 显示系统/发行版/内核/驱动详细信息 | **报 bug 时必加** |
| `--debug` | 比 `--verbose` 更详细（含 shell 信息、驱动来源、USB ID） | 深入排错 |
| `-h` / `--help` | 显示用法 | — |

### 4.3 相关的手工替代命令

当 airmon-ng 因驱动特殊而失效时，可以用 `iw` 手工切换：

```bash
# 切到监听模式
sudo ip link set wlan0 down
sudo iw wlan0 set monitor control
sudo ip link set wlan0 up

# 确认
iw dev wlan0 info
#         type monitor          ← 成功

# 锁定信道
sudo iw dev wlan0 set channel 6

# 切回托管
sudo ip link set wlan0 down
sudo iw wlan0 set type managed
sudo ip link set wlan0 up
```

### 4.4 检查网卡能力的命令

```bash
# 列出所有无线设备
iw dev

# 网卡支持的模式（关键）
iw list | grep -A 12 'Supported interface modes'

# 支持的信道（判断 2.4G/5G）
iw list | grep -A 30 'Frequencies'

# 当前模式与信道
iw dev wlan0 info
iwconfig wlan0

# 芯片组
lsusb          # USB 网卡
lspci          # PCIe/内置
```

## 5. 实战演练

**环境声明**：本目录所有无线操作**仅限你自己拥有的 Wi-Fi 网络与路由器**，或有书面授权的测试目标，或隔离实验室。**deauth 等注入操作会中断他人通信，严禁对非自有网络执行。**

### 场景 1：检查网卡能力（每次开工的第一步）

**步骤 1：看接口列表**

```bash
sudo airmon-ng
```

**预期输出**

```
PHY	Interface	Driver		Chipset

phy0	wlan0		ath9k_htc	Atheros Communications, Inc. AR9271 802.11n
```

| 列 | 含义 |
| --- | --- |
| `PHY` | 物理设备编号（一块网卡可能有多个 vif） |
| `Interface` | 接口名，**后续命令用这个** |
| `Driver` | 内核驱动 |
| `Chipset` | 芯片组，**决定能力** |

**如果这里什么都没有** → 网卡未被识别，检查 USB 直通/驱动。

**步骤 2：看支持的模式**

```bash
iw list | grep -A 12 'Supported interface modes'
```

**预期输出**

```
	Supported interface modes:
		 * IBSS
		 * managed
		 * AP
		 * AP/VLAN
		 * monitor
		 * P2P-client
		 * P2P-GO
		 * P2P-device
```

**判读**：

| 看到 | 结论 |
| --- | --- |
| 有 `monitor` | ✅ 可以抓包 |
| 有 `AP` | ✅ 可以建假 AP（`airbase-ng` / `bettercap`） |
| **没有 `monitor`** | ❌ **换网卡**。软件层面无解 |

**步骤 3：看驱动来源（重要）**

```bash
sudo airmon-ng --verbose
```

**预期输出（节选）**

```
Distributor ID:	Kali
Description:	Kali GNU/Linux Rolling

Linux kali 6.x.x-kali-amd64 #1 SMP ... x86_64 GNU/Linux

K indicates driver is from 6.x.x-kali-amd64
V indicates driver comes directly from the vendor, almost certainly a bad thing
S indicates driver comes from the staging tree, these drivers are meant for reference not actual use, BEWARE

X[PHY]Interface		Driver[Stack]-FirmwareRev		Chipset			Extended Info

K[phy0]wlan0		ath9k_htc[mac80211]-1.4			Qualcomm Atheros Communications AR9271 802.11n		mode managed
```

**关键看前缀字母**：

| 前缀 | 含义 | 建议 |
| --- | --- | --- |
| `K` | 驱动来自内核 | ✅ 最稳定 |
| `V` | 厂商驱动 | ⚠️ 「almost certainly a bad thing」——常与注入不兼容 |
| `S` | staging 树 | ⚠️ 「meant for reference not actual use」 |
| `?` | 来源未知 | 需要自行排查 |

**看到 `V` 或 `S` 就是强烈的换卡信号**——你会遇到各种诡异问题（抓不到、注入失败、掉线）。

### 场景 2：开启监听模式（与官方示例一致）

**步骤 1：检查干扰进程**

```bash
sudo airmon-ng check
```

**预期输出**

```
Found 5 processes that could cause trouble.
If airodump-ng, aireplay-ng or airtun-ng stops working after
a short period of time, you may want to kill (some of) them!

  PID Name
  718 NetworkManager
  870 dhclient
 1104 avahi-daemon
 1105 avahi-daemon
 1115 wpa_supplicant
```

**步骤 2：清理它们**

```bash
sudo airmon-ng check kill
```

**预期输出**

```
Killing these processes:

  PID Name
  870 dhclient
 1115 wpa_supplicant
```

**⚠️ 此时你的网络已断开**。这是预期行为。

**步骤 3：开启监听并锁定信道**

```bash
sudo airmon-ng start wlan0 6
```

**预期输出**

```
PHY	Interface	Driver		Chipset

phy0	wlan0		ath9k_htc	Atheros Communications, Inc. AR9271 802.11n

		(mac80211 monitor mode vif enabled for [phy0]wlan0 on [phy0]wlan0mon)
		(mac80211 station mode vif disabled for [phy0]wlan0)
```

**关键信息**：

- 新接口名是 **`wlan0mon`** —— **后续所有命令都要用它**。
- 因为带上了信道参数 `6`，网卡已锁定在 6 信道（不跳频）。

**步骤 4：确认新接口**

```bash
iw dev wlan0mon info
```

**预期输出**

```
Interface wlan0mon
	ifindex 4
	wdev 0x100000001
	addr 00:c0:ca:xx:xx:xx
	type monitor            ← ★ 确认是 monitor
	channel 6 (2437 MHz), width: 20 MHz, center1: 2437 MHz
	txpower 20.00 dBm
```

**看到 `type monitor` 和 `channel 6` 就成功了。**

### 场景 3：收尾恢复（最容易被忘记的一步）

```bash
sudo airmon-ng stop wlan0mon
```

**预期输出**

```
PHY	Interface	Driver		Chipset

phy0	wlan0mon	ath9k_htc	Atheros Communications, Inc. AR9271 802.11n

		(mac80211 station mode vif enabled on [phy0]wlan0)
		(mac80211 monitor mode vif disabled for [phy0]wlan0mon)
```

然后恢复网络管理：

```bash
sudo systemctl restart NetworkManager
# 老系统用： sudo service network-manager start
```

**验证已恢复上网**：

```bash
iw dev wlan0 info | grep type
# 	type managed

nmcli device status
ping -c 2 1.1.1.1
```

### 场景 4：信道操作

**列出可用信道（2.4 GHz）**：

```bash
iwlist wlan0mon channel 2>/dev/null | head -20
# 或
iw phy phy0 info | grep -A 40 'Frequencies'
```

**运行中改信道**：

```bash
sudo iw dev wlan0mon set channel 11
iw dev wlan0mon info | grep channel
```

**注意**：`airodump-ng` 会自己管信道。如果你用 `-c 6` 指定了信道，**不要**再手工改——否则会冲突导致抓不到包。

### 场景 5：没有合适硬件时怎么办

**你完全可以只学「文件分析」这条路径**——不需要任何无线网卡：

```bash
# 1) 找本机已有的抓包文件
find /usr/share -name '*.cap' -o -name '*.pcap' 2>/dev/null | head

# 2) 用 airodump-ng 从文件「回放」（注意：airodump 有 -r 参数可从文件读）
sudo airodump-ng -r capture.cap

# 3) 用 aircrack-ng 直接分析
aircrack-ng capture.cap

# 4) 用 Wireshark / tshark 深入看 802.11 与 EAPOL 报文
tshark -r capture.cap -Y 'eapol' -c 10
wireshark capture.cap
```

**这条路径同样覆盖 90% 的知识点**：握手结构、EAPOL 报文、破解流程、hashcat 转换。你唯一学不到的是「真实抓包的手感」。

**同时要清楚一件事**：**在虚拟机里做无线抓包很麻烦**。

| 环境 | 说明 |
| --- | --- |
| 物理机 Kali | ✅ 最省事 |
| VirtualBox | 需要 **USB 直通**（`设备 → USB → 勾选网卡`），且宿主机不能同时占用 |
| VMware | 需要 USB 直通；PCIe 网卡通常不可直通（除非 VT-d） |
| WSL | ❌ 基本不可用 |
| Docker | ❌ 不可用 |

`airmon-ng --verbose` 会直接告诉你环境情况：

```
Detected VM using lspci
This appears to be a VMware Virtual Machine
If your system supports VT-d, it may be possible to use PCI devices
If your system does not support VT-d, you can only use USB wifi cards
```

## 6. 输出解读

### 接口列表

```
PHY	Interface	Driver		Chipset

phy0	wlan0		ath9k_htc	Atheros Communications, Inc. AR9271 802.11n
```

| 列 | 含义 | 怎么用 |
| --- | --- | --- |
| `PHY` | 物理设备索引 | 多网卡时区分 |
| `Interface` | 接口名 | **后续命令的参数** |
| `Driver` | 内核驱动 | 上网搜兼容性 |
| `Chipset` | 芯片组 | **决定监听/注入能力** |

### 模式切换的确认行

| 输出行 | 含义 |
| --- | --- |
| `mac80211 monitor mode vif enabled for [phy0]wlan0 on [phy0]wlan0mon` | ✅ 监听模式 vif 已启用，接口名 `wlan0mon` |
| `mac80211 station mode vif disabled for [phy0]wlan0` | ✅ 托管模式已禁用（**这就是断网的原因**） |
| `mac80211 station mode vif enabled on [phy0]wlan0` | ✅ （stop 时）托管模式已恢复 |
| `mac80211 monitor mode vif disabled for [phy0]wlan0mon` | ✅ （stop 时）监听模式已关闭 |
| `(monitor mode enabled on mon0)` | 老驱动（如 madwifi-ng），接口名是 `mon0` |
| `Interface wlan0mon is not in monitor mode` | ❌ 切换失败 |

**判断成功**：`iw dev <iface> info` 显示 `type monitor`。

## 7. 与其他工具配合

```text
                        ┌── airmon-ng ──┐
                        │ 准备阶段      │
[网卡] → iw list 检查 → airmon-ng check kill
                        │
                        └→ airmon-ng start wlan0 [channel]
                                    ↓
                            wlan0mon（监听接口）
                                    ↓
        ┌───────────────────────────┼──────────────────────────┐
        ↓                           ↓                          ↓
   airodump-ng                aireplay-ng                 kismet / bettercap
   （抓包侦察）                （注入/deauth）              （被动侦测）
        ↓                           │
        └───────────┬───────────────┘
                    ↓
              aircrack-ng / hashcat
                    ↓
             airdecap-ng（解密流量）
                    ↓
        airmon-ng stop wlan0mon → 恢复上网
```

| 上游 | 本工具 | 下游 |
| --- | --- | --- |
| `iw list` / `lsusb` 确认硬件 | **airmon-ng 切模式** | [airodump-ng](airodump-ng.md) 抓包 |
| — | airmon-ng check kill | [aireplay-ng](aireplay-ng.md) 注入 |
| — | — | [kismet](kismet.md) 被动侦测 |
| — | — | [wifite](wifite.md)（自动完成以上全部） |

**注意**：[wifite](wifite.md) 和 [bettercap](bettercap.md) 会**自己调用 airmon-ng**（或等价操作）来切模式，所以用它们时**不需要**手工先 `airmon-ng start`。

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `iw list` 里没有 `monitor` | 网卡/驱动不支持 | **换网卡**（AR9271 / RT3070 / RTL8812AU） |
| `airmon-ng start` 报 `monitor mode enable failed` | 驱动不支持 vif 切换 | 试手工：`ip link set wlan0 down; iw wlan0 set monitor control; ip link set wlan0 up`；或换卡 |
| 接口名不是 `wlan0mon` | 旧驱动/不同发行版 | **以输出为准**，老版可能是 `mon0` |
| 切了监听后**上不了网** | 托管模式被禁用（**设计如此**） | 正常。收尾 `airmon-ng stop` + `systemctl restart NetworkManager` |
| `check kill` 后网络彻底断了 | 杀掉了 NetworkManager/dhclient | 恢复：`sudo systemctl restart NetworkManager` |
| **抓了几十秒后突然什么都抓不到** | NetworkManager 或别的进程把网卡切回去了 | `airmon-ng check kill` **再** `start`；确认没有残留进程（`ps aux \| grep -E 'NetworkManager\|wpa_supplicant'`） |
| 切换后原接口 `wlan0` 消失了 | mac80211 vif 的行为 | 正常，用 `wlan0mon` |
| `airmon-ng` 输出为空 | 没有任何无线接口 | 检查 USB 直通 / 驱动 / `dmesg \| tail` |
| 虚拟机里找不到网卡 | USB 直通未配置 | VirtualBox：`设备 → USB → 选中网卡`；确保宿主机没占用 |
| 网卡能监听但 deauth 无效 | **Intel 等芯片常见：能监听不能注入** | 换卡；用 `aireplay-ng --test` 确认 |
| `dmesg` 里有 firmware 加载失败 | 缺固件包 | `sudo apt install firmware-atheros firmware-ralink firmware-realtek` |
| 驱动前缀是 `V` 或 `S` | 厂商/staging 驱动 | 换成内核自带驱动（前缀 `K`）的网卡 |
| `Channel -1` | 网卡未同步信道 | `iw dev wlan0mon set channel <n>`；或在 airodump 用 `-c` |
| 收尾后 Wi-Fi 列表是空的 | NetworkManager 未重启 | `sudo systemctl restart NetworkManager`，必要时 `sudo rfkill unblock all` |

## 9. 防御视角（蓝队）

**airmon-ng 本身不发射任何信号**——它只是把网卡切到「只听不说」的接收状态。这意味着：

| 事实 | 对蓝队的含义 |
| --- | --- |
| 监听模式不发送任何帧 | **在网络上完全不可检测**（没有流量特征） |
| 无法从网络侧判断有人在监听 | ❌ 不存在「检测到监听模式网卡」的网络层方法 |
| 唯一可观测的是下游行为 | deauth 洪泛、钓鱼 AP、大量关联请求（PMKID） |

**因此蓝队的着力点只能是「下游行为」与「让监听无收益」**：

| 下游行为 | 检测 | 缓解 |
| --- | --- | --- |
| **被动抓握手** | 不可检测 | 让握手无价值 → **WPA3-SAE**（无法离线验证口令）+ 长随机 PSK |
| deauth 洪泛 | 统计 deauth 帧速率；**正常网络几乎不应出现 deauth** | **启用 802.11w（PMF）** —— 这是对 deauth 的直接防护 |
| PMKID 抓取 | AP 日志里异常的关联请求 | 升级到 WPA3-SAE |
| 客户端重连风暴 | 短时间内大量 STA 重新关联 | PMF + 监控 |
| 邪恶孪生 | 同一 SSID 出现多个 BSSID，其中一个信号异常强 | WIPS；**802.1X/EAP-TLS**（每个设备独立证书，假 AP 无法完成认证） |

### 物理与运营层面的措施

| 措施 | 说明 |
| --- | --- |
| **屏蔽箱 / Faraday 袋** | 对高安全场景，物理屏蔽胜过一切协议。测试实验室本身就应放在屏蔽环境里 |
| **降低发射功率** | 把 AP 功率调到只覆盖必要范围，减少可被监听的边界 |
| **访客网络物理隔离** | 访客 Wi-Fi 单独 VLAN + 完全隔离内网 |
| **禁用 WPS** | 直接消除 [reaver](reaver.md) 的攻击面 |
| **定期无线勘测** | 定期用 [kismet](kismet.md) 做基线扫描，发现未授权 AP |
| **员工培训** | 邪恶孪生的主要入口是**用户主动连接**，不是技术漏洞 |

### 检测规则思路

```text
# deauth 洪泛（最可检测的无线攻击信号）
if count(deauth_frames, 10s) > 20
then alert "possible deauth flood"

# 同一 reason code 的大量 deauth（工具默认 reason 7）
if count(deauth where reason_code == 7, 60s) > 50
then alert "possible automated deauth (handshake capture attempt)"

# 客户端重连风暴（deauth 的间接后果）
if count(association_requests, 60s) > 100 and distinct_stations > 10
then alert "possible deauth-induced reconnection storm"

# 未知 BSSID（邪恶孪生 / 未授权 AP）
if bssid not in baseline_bssid_list
then alert "rogue access point detected"
```

**蓝队核心结论**：

> **监听模式在网络上不可检测**，所以你无法「抓现行」。有效的防护只有两条：
> 1. **物理/信号层面**：限制覆盖范围，隔离敏感区域；
> 2. **协议层面**：WPA3 + PMF + 802.1X，让即使被抓到的流量也**无法离线破解**。

## 10. 参考

- 官方文档：<https://www.aircrack-ng.org/doku.php?id=airmon-ng>
- 官方站点：<https://www.aircrack-ng.org/>
- Kali 工具页：<https://www.kali.org/tools/aircrack-ng/>
- 本机手册：`man airmon-ng`、`airmon-ng -h`
- 排错：`sudo airmon-ng --verbose`、`sudo airmon-ng --debug`
- 相关本目录：[aircrack-ng](aircrack-ng.md)（套件总览）、[airodump-ng](airodump-ng.md)、[aireplay-ng](aireplay-ng.md)、[wifite](wifite.md)、[kismet](kismet.md)、[bettercap](bettercap.md)

## ⚠️ 法律与伦理

无线信号天然跨越物理边界，这使得无线相关行为的法律风险远高于有线侧。

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条 | 非法侵入计算机信息系统；非法获取计算机信息系统数据 |
| 《刑法》 | 第二百八十六条 | 破坏计算机信息系统 |
| 《无线电管理条例》 | 相关条款 | 擅自使用无线电频率、干扰合法无线电业务 |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《个人信息保护法》 | 相关条款 | 截获通信内容涉及个人信息处理 |

**注意**：**即使只是「切到监听模式看一眼」，只要接收的是他人通信，在很多司法辖区就已构成违法**。切模式这个动作本身不违法，但一旦开始接收并分析非自有网络的流量，性质就变了。

**本教程仅适用于**：

- ✅ **你自己拥有的 Wi-Fi 网络与你自己的路由器**
- ✅ 有**书面授权**、明确列出授权 SSID 与时间窗的无线渗透测试
- ✅ 你自己搭建的隔离无线实验室（有屏蔽措施，不干扰他人）
- ✅ CTF 靶场 / 授权的无线练习平台

**严禁**：对邻居、公司、公共场所的任何 Wi-Fi 执行本目录的任何命令。**只分析已有的抓包文件是最安全、也是完全足够的学法**。
