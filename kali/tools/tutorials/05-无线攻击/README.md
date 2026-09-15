# 05 · 无线攻击（Wireless Attacks）

本目录覆盖 Kali 中 802.11 无线审计相关的工具教程，从网卡准备、抓包、注入、破解到自动化与检测。

**先读这一句**：无线攻击的法律风险**远高于**有线侧——因为无线电信号天然跨越物理边界，「我家的网卡收到了邻居的信号」**不是**合法使用他人网络的理由。**本目录的所有内容仅限你自己拥有的 Wi-Fi 网络与路由器、隔离实验室、或已书面授权的目标。** 详见每篇文末的法律章节。

## 工具清单

| 工具 | 一句话 | 难度 | 教程 |
| --- | --- | --- | --- |
| `aircrack-ng` | **套件总览**：从监听、抓包、注入到破解的完整链路与原理 | ★★ | [aircrack-ng.md](aircrack-ng.md) |
| `airmon-ng` | 网卡切监听模式、列网卡与芯片组、清理干扰进程 | ★ | [airmon-ng.md](airmon-ng.md) |
| `airodump-ng` | 侦察所有 AP 与客户端，锁定目标抓握手/PMKID/IV | ★★ | [airodump-ng.md](airodump-ng.md) |
| `aireplay-ng` | 注入伪造帧：注入测试、deauth、ARP 重放 | ★★★ | [aireplay-ng.md](aireplay-ng.md) |
| `wifite` | 把上面这条链路封成一条命令，全自动抓包与破解 | ★ | [wifite.md](wifite.md) |
| `reaver` | 攻击 WPS 的 8 位 PIN（含 Pixie-Dust） | ★★ | [reaver.md](reaver.md) |
| `kismet` | 被动侦测 + **WIDS 告警** + 可查询的设备历史库 | ★★★ | [kismet.md](kismet.md) |
| `bettercap` | 模块化 MITM 与无线侦察框架，支持 caplet 与 REST API | ★★★ | [bettercap.md](bettercap.md) |
| `hashcat`（跨目录） | 用 GPU 破解抓到的握手/PMKID（`-m 22000`） | ★★★ | [../04-口令攻击/hashcat.md](../04-口令攻击/hashcat.md) |

## 学习顺序

**第 0 步 · 先搞清能不能做（否则后面全是浪费时间）**

1. [airmon-ng.md](airmon-ng.md) —— 用 `iw list` 和 `airmon-ng` 确认网卡支持监听/注入。**这是整个目录的前提。**
   - 没有支持监听的网卡 → 走「**只用抓包文件练习**」路径（见 [airodump-ng](airodump-ng.md) 场景 4），仍然能学到 90%。

**第 1 步 · 理解原理（不要跳）**

2. [aircrack-ng.md](aircrack-ng.md) —— **先读这篇**。它讲清了 802.11 四次握手、PMKID、WEP、WPA/WPA2/WPA3 的差异，以及「为什么需要注入」。不读这篇，后面的命令都是照抄。

**第 2 步 · 手工走一遍完整链路**

3. [airodump-ng.md](airodump-ng.md) —— 侦察 + 抓包。**核心是理解表格每一列的含义。**
4. [aireplay-ng.md](aireplay-ng.md) —— 注入测试 + deauth 抓握手。**先做 `--test`**。
5. 回到 [aircrack-ng.md](aircrack-ng.md) 用 `aircrack-ng` 破解，然后换 [hashcat](../04-口令攻击/hashcat.md) 用 GPU。

**第 3 步 · 换一条攻击路径**

6. [reaver.md](reaver.md) —— WPS 路径。**不需要字典**，但有前提（AP 必须开 WPS）。
7. 对比两条路径的优劣（见 [reaver](reaver.md) 第 7 节）。

**第 4 步 · 自动化与框架**

8. [wifite.md](wifite.md) —— 一条命令走完。**用 `-v` 观察它调用的底层命令**，这是最好的复习方式。
9. [bettercap.md](bettercap.md) —— 当你需要把无线侦察与 MITM/自动化结合时。

**第 5 步 · 换到防守视角（最有价值的一步）**

10. [kismet.md](kismet.md) —— 检测 deauth 洪泛、伪造 AP、WPS 暴力。**做一次红蓝对抗演练**：一边用 [wifite](wifite.md) 攻击自己的实验网络，一边看 Kismet 的告警。

## 环境准备

### 硬件（最关键的一环）

**无线审计的成败几乎完全取决于网卡**。「支持监听」和「支持注入」是两种不同的能力——**很多网卡能听不能打**。

| 芯片组 | 监听 | 注入 | 5 GHz | 备注 |
| --- | --- | --- | --- | --- |
| **Atheros AR9271** | ✅ | ✅ | ❌ | USB，最经典，稳定，推荐入门 |
| **Ralink RT3070 / RT3572** | ✅ | ✅ | ❌/部分 | USB，稳定 |
| **Realtek RTL8812AU** | ✅ | ✅ | ✅ | USB，需编译驱动 |
| **Realtek RTL8814AU** | ✅ | ✅ | ✅ | USB，性能较好 |
| Ralink RT5572 | ✅ | ✅ | ✅ | 双频 |
| **多数 Intel 内置网卡** | ✅ | ❌/受限 | — | ⚠️ **最常见的坑：能抓不能注入** |
| 多数 Broadcom | ❌ | ❌ | — | 基本不可用 |

**检查你的网卡**：

```bash
# 1) 支持的模式（必须有 monitor）
iw list | grep -A 12 'Supported interface modes'

# 2) 芯片组与驱动
sudo airmon-ng
sudo airmon-ng --verbose     # 看驱动来源：K=内核（好）V=厂商（差）S=staging（差）

# 3) 注入能力（唯一可靠的验证方法）
sudo airmon-ng check kill
sudo airmon-ng start wlan0
sudo aireplay-ng --test wlan0mon     # 看 30/30: 100% 这样的比率
```

**没有合适硬件怎么办**：

| 替代方案 | 说明 |
| --- | --- |
| **只分析已有的抓包文件** | ⭐ **最推荐**。用 `airodump-ng -r file.cap`、`aircrack-ng file.cap`、`tshark -r file.cap`。覆盖 90% 的知识点，且完全合法 |
| Wireshark 官方示例抓包 | <https://wiki.wireshark.org/SampleCaptures> 有 802.11 示例 |
| 自己以前抓的自有网络抓包 | 最真实 |
| USB 网卡（几十元起） | AR9271 是最便宜好用的选择 |

### 虚拟机注意事项

**在虚拟机里做无线抓包很麻烦**，请优先用**物理机 + USB 网卡**：

| 环境 | 说明 |
| --- | --- |
| 物理机 Kali | ✅ **最省事，推荐** |
| VirtualBox | 需要 **USB 直通**（`设备 → USB → 勾选网卡`），宿主机不能同时占用 |
| VMware | 需要 USB 直通；PCIe 网卡通常不可直通（除非有 VT-d） |
| WSL / Docker | ❌ 不可用 |

`airmon-ng --verbose` 会直接告诉你环境情况：

```
Detected VM using lspci
This appears to be a VMware Virtual Machine
If your system supports VT-d, it may be possible to use PCI devices
If your system does not support VT-d, you can only use USB wifi cards
```

### 工具安装

```bash
sudo apt install aircrack-ng wifite reaver kismet bettercap hcxtools
```

| 包 | 提供 |
| --- | --- |
| `aircrack-ng` | 整个套件（airmon-ng / airodump-ng / aireplay-ng / aircrack-ng / airdecap-ng / airolib-ng / airbase-ng …） |
| `wifite` | 自动化工具（依赖 aircrack-ng / reaver / tshark） |
| `reaver` | reaver + wash |
| `kismet` | 元包（含 kismet-core、各类捕获驱动、kismet-logtools） |
| `bettercap` | bettercap |
| `hcxtools` | ⭐ **hcxdumptool / hcxpcapngtool**（PMKID 抓取与现代格式转换，**必装**） |
| `wordlists` | 字典（破解环节用，见 [../04-口令攻击/wordlists.md](../04-口令攻击/wordlists.md)） |

**必做的一步**——解压字典：

```bash
sudo gunzip /usr/share/wordlists/rockyou.txt.gz
```

### 实验环境（**这是最重要的准备**）

**唯一安全且合法的做法**是搭建完全属于你自己的隔离无线环境：

```text
┌─────────────────────────────────────────────────────┐
│  隔离无线实验环境（推荐配置）                          │
│                                                      │
│  [旧家用路由器]  ← 你买的/闲置的，SSID 如 "lab-test"   │
│      │              口令你自己设（如 labpassword123）  │
│      │                                               │
│  [你的 Kali]     ← 物理机 或 装了 USB 直通的虚拟机     │
│      └─ 一块支持监听+注入的 USB 网卡                    │
│                                                      │
│  [一台测试设备]  ← 你不再使用的旧手机/笔记本            │
│                    连到 lab-test，用来产生握手          │
│                                                      │
│  [可选] 屏蔽措施 ← 屏蔽箱 / Faraday 袋 / 远离他人的房间 │
└─────────────────────────────────────────────────────┘
```

**几个关键点**：

| 要点 | 说明 |
| --- | --- |
| **路由器必须是你自己的** | 旧路由器很便宜；**不要用邻居的 Wi-Fi 实验** |
| **降低发射功率** | 把路由器功率调低到只覆盖你的房间——**这是防止误伤邻居的关键** |
| **隔离位置** | 在地下室/远离窗户的房间；有条件用 Faraday 袋 |
| **测试设备** | 用一台旧手机连着，这样你能自己触发握手（关 Wi-Fi 再开），**完全不需要 deauth** |
| **功率控制** | 如果你能收到邻居的 AP，那么邻居也能收到你的——**双向都是问题** |

### 靶场（如需扩展练习）

| 靶场 | 说明 |
| --- | --- |
| **自建路由器实验室** | ⭐ **首选**，完全可控，包含 WPS/PMKID/WPA3 等所有场景 |
| 支持 WPS 的旧路由器 | 练 [reaver](reaver.md)（新款路由器多有 WPS 锁定，旧款更适合学习） |
| RWCTF / 相关 CTF 的无线题目 | 有授权，可能提供抓包文件 |
| Wireshark 示例抓包 | 无硬件也能练分析 |

### 抓包文件练习（无硬件路径）

```bash
# 1) 找本机已有的示例抓包
find /usr/share -name '*.cap' -o -name '*.pcap' 2>/dev/null | head

# 2) 从文件回放（不做任何实际抓包）
sudo airodump-ng -r capture.cap
aircrack-ng capture.cap

# 3) 深入分析
tshark -r capture.cap -Y 'eapol'
tshark -r capture.cap -Y 'wlan.fc.type_subtype == 0x0c'   # deauth 帧
wireshark capture.cap

# 4) 尝试破解
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b <BSSID> capture.cap

# 5) 导出给 hashcat
hcxpcapngtool -o /tmp/wifi.22000 capture.cap
hashcat -m 22000 /tmp/wifi.22000 /usr/share/wordlists/rockyou.txt -O
```

**这条路径覆盖：握手结构、EAPOL 报文、破解流程、hashcat 转换——只缺「抓包手感」。**

## 技术速查

### 完整链路（手工）

```bash
# 0) 准备
sudo airmon-ng check kill
sudo airmon-ng start wlan0
sudo aireplay-ng --test wlan0mon          # 确认注入能力

# 1) 侦察
sudo airodump-ng wlan0mon
# 记下：BSSID、CH、客户端 STATION

# 2) 抓包（终端 A）
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w /tmp/cap wlan0mon

# 3) deauth（终端 B）—— 仅限自有网络
sudo aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF -c 12:34:56:78:9A:BC wlan0mon

# 4) 看到 "WPA handshake:" 后 Ctrl+C，然后破解
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b AA:BB:CC:DD:EE:FF /tmp/cap-01.cap

# 5) 或交给 GPU
hcxpcapngtool -o /tmp/wifi.22000 /tmp/cap-01.cap
hashcat -m 22000 /tmp/wifi.22000 /usr/share/wordlists/rockyou.txt -O

# 6) 收尾
sudo airmon-ng stop wlan0mon
sudo systemctl restart NetworkManager
```

### 核心原理速查

| 概念 | 要点 |
| --- | --- |
| **四次握手** | ANonce ↔ SNonce + MIC。抓到 msg1+msg2（或 msg3+msg4）才能离线验证口令 |
| **PMK** | `PBKDF2-HMAC-SHA1(口令, SSID, 4096 次)` —— **SSID 是盐** |
| **PTK** | 由 PMK + ANonce + SNonce + 两个 MAC 派生 |
| **MIC** | 用 PTK 校验握手 —— 候选口令算出的 MIC 匹配即命中 |
| **破解慢的原因** | PBKDF2 的 4096 次迭代（2004 年故意设计来拖慢攻击） |
| **PMKID** | `HMAC-SHA1-128(PMK, "PMK Name" \|\| AP_MAC \|\| STA_MAC)` —— **不需要客户端** |
| **WPA3-SAE** | 没有可离线验证的 MIC → **无法离线字典破解**（核心改进） |
| **WPA3 的软肋** | **WPA3/WPA2 混合模式**——攻击者可以对 WPA2 部分下手 |
| **PMF / 802.11w** | 管理帧加 MIC → **deauth 失效**。WPA3 强制启用 |
| **WPS 缺陷** | PIN 8 位但第 8 位是校验位；且 AP **分两次验证**（前 4 位 / 后 4 位）→ **约 11000 次尝试** |
| **Pixie-Dust** | 利用芯片随机数弱 → **一次交互就能离线算出 PIN 和 PSK**，不受锁定影响 |
| **WEP** | 24 位 IV 重复 + RC4 弱密钥 → **约 4 万个 IV（PTW）即可破** |

### 成功率与耗时的现实预期

| 攻击 | 前提 | 典型耗时 | 现代成功率 |
| --- | --- | --- | --- |
| WEP 破解 | 目标是 WEP | 1~3 分钟 | ⚠️ 2026 年几乎遇不到 |
| WPA2 握手 + 字典 | 有客户端 + 字典命中 | 秒级（抓到后） | 中（取决于口令强度） |
| WPA2 PMKID | AP 的 RSN IE 带 PMKID | 秒级 | 中 |
| WPS Pixie-Dust | AP 芯片有随机数缺陷 | **秒~分钟** | ⚠️ 低（2014 年后多已修复） |
| WPS PIN 暴力 | AP 开 WPS 且无锁定 | 数小时~数天 | ⚠️ 低（多数有锁定） |
| **WPA3-SAE** | — | — | ❌ **无法离线破解** |

**结论**：**现代路由器的正确配置下，这些攻击基本都行不通。** 这既是学习它们的理由（理解为什么要这样配置），也是防御章节存在的原因。

## 防守速查（本目录最有价值的部分）

> **无线安全的核心是一条**：**让即使被抓到的流量也无法利用**。

| 措施 | 防住什么 | 优先级 |
| --- | --- | --- |
| **WPA3-SAE（首选纯模式）** | 握手/PMKID 离线破解、字典攻击 | ⭐⭐⭐ |
| **管理帧保护（PMF / 802.11w）** | **deauth 攻击** | ⭐⭐⭐ |
| **关闭 WPS** | [reaver](reaver.md) 的 PIN 暴力与 Pixie-Dust | ⭐⭐⭐ |
| **PSK ≥ 20 位且随机** | 字典/规则破解 | ⭐⭐⭐ |
| **802.1X + EAP-TLS（企业）** | 共享 PSK 的所有问题；邪恶孪生 | ⭐⭐⭐ |
| **降低发射功率** | 缩小可被监听/攻击的边界 | ⭐⭐ |
| **访客网络完全隔离** | 影响范围 | ⭐⭐ |
| **Kismet 部署 + 基线** | **发现** deauth、伪造 AP、WPS 暴力 | ⭐⭐ |
| **禁用 WEP / TKIP；升级固件** | 已知协议缺陷、Pixie-Dust 缺陷 | ⭐⭐ |

**部署 Kismet 做检测**：

```bash
# 建立基线（1~4 周）
sudo kismet -c wlan0:channel=<关键信道> --log-prefix /var/log/kismet/baseline/

# 提取允许清单
kismetdb_dump_devices --in /var/log/kismet/baseline/*.kismet --out baseline.json

# 持续监控并对比新增设备
# 关注 Alerts 页面：DEAUTHFLOOD / BSSTIMESTAMP / CRYPTCHANGE / WPSBRUTE
```

详见 [kismet.md](kismet.md) 第 9 节。

## 法律与伦理（**必读，本目录风险最高**）

### 为什么无线比有线更危险

| 原因 | 说明 |
| --- | --- |
| **信号跨越物理边界** | 你无法证明「只覆盖了我自己的财产」。收到了邻居的信号 ≠ 可以用 |
| **监听即接收他人通信** | 在很多司法辖区，**即使不破解**，单纯截获通信已违法 |
| **deauth 是主动干扰** | 会**真实中断**他人网络，属于破坏行为 |
| **设备信息涉及个人信息** | 客户端 Probe 数据能暴露用户去过的地方（酒店、公司、家庭） |

### 相关法律责任（中国大陆）

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条 | 非法侵入计算机信息系统；**非法获取计算机信息系统数据** |
| 《刑法》 | 第二百八十六条 | **破坏计算机信息系统**（deauth 造成断网） |
| 《刑法》 | 第二百五十三条之一 | **侵犯公民个人信息**（Probe 数据暴露行踪） |
| 《无线管理条例》 | 相关条款 | 擅自使用无线电频率、干扰合法无线电业务 |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《个人信息保护法》 | 相关条款 | 截获/处理个人信息的合法性基础 |

### 明确禁止

- ❌ 对邻居、公司、公共场所的任何 Wi-Fi 执行本目录的任何命令
- ❌ 在居民区/办公区运行 [wifite](wifite.md) `-p` 自动模式（会攻击视野内所有网络）
- ❌ deauth 任何不属于你的网络
- ❌ 用设备记录了他人通信内容或设备信息后保留/分享
- ❌ 把包含他人信息的数据库上传到 WiGLE 等公开平台
- ❌ 把授权范围外的主机纳入扫描（多测一个 SSID 都是越权）

### 明确允许

- ✅ **你自己拥有的 Wi-Fi 网络与你自己的路由器**
- ✅ 有**书面授权**、明确列出授权 SSID、时间窗与允许的注入行为的渗透测试
- ✅ 你自己搭建的**隔离**无线实验室（有屏蔽/降功率措施，不影响他人）
- ✅ 授权的 CTF 靶场
- ✅ **只分析已有的抓包文件**（不发射任何信号，不接收任何他人通信）

**如果你只是想学习**：请搭建一个隔离环境（旧路由器 + USB 网卡 + 旧手机），或走「抓包文件分析」路径。**两者的学习效果都不打折扣，而且完全不会伤害任何人。**

## 相关目录

- [04 · 口令攻击](../04-口令攻击/README.md) —— 字典准备、[hashcat](../04-口令攻击/hashcat.md) `-m 22000` 破解 WPA 握手
- [07 · 嗅探与欺骗](../07-嗅探与欺骗/README.md) —— [ettercap](../07-嗅探与欺骗/ettercap.md) / [responder](../07-嗅探与欺骗/responder.md) / [mitmproxy](../07-嗅探与欺骗/mitmproxy.md) / [wireshark](../07-嗅探与欺骗/wireshark.md)（与 [bettercap](bettercap.md) 的 MITM 能力互补）

## 参考

- Kali 工具分类：<https://www.kali.org/tools/>
- aircrack-ng 官方文档：<https://www.aircrack-ng.org/doku.php>
- Kismet 官方文档：<https://www.kismetwireless.net/docs/>
- bettercap 官方文档：<https://www.bettercap.org/modules/>
- Wireshark 802.11 示例抓包：<https://wiki.wireshark.org/SampleCaptures>
- 本仓库工具清单来源：`data/kali-tools.tsv`、`data/kali-tools.json`
