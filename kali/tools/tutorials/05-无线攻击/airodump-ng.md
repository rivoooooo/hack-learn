# airodump-ng（802.11 抓包与侦察）

> **一句话**：被动监听并列出所有可见的 AP 与客户端，锁定目标抓取 WPA 握手包 / PMKID / WEP IV。
> **分类**：无线攻击 ｜ **Kali 包**：`aircrack-ng` ｜ **官方文档**：<https://www.aircrack-ng.org/doku.php?id=airodump-ng>

## 1. 它解决什么问题

拿到一块能监听的网卡之后，你要回答三个问题：

1. **周围有哪些网络？**（SSID、BSSID、信道、加密方式、信号强度）
2. **谁连着哪个网络？**（客户端 MAC —— **这决定了你能不能抓到握手**）
3. **怎么把我要的数据抓下来？**（握手包、PMKID、WEP IV、全部流量）

airodump-ng 就是干这个的。它是整个 [aircrack-ng](aircrack-ng.md) 套件里**最常用、也最该先掌握**的工具。

**它的三个使用模式**：

| 模式 | 命令 | 用途 |
| --- | --- | --- |
| 全信道扫描 | `airodump-ng wlan0mon` | 侦察：看有哪些网络 |
| 锁定目标抓包 | `airodump-ng -c 6 --bssid AA:... -w cap wlan0mon` | **抓握手/PMKID** |
| 从文件回放 | `airodump-ng -r cap-01.cap` | **无网卡也能分析抓包文件** |

第三种模式很重要：**没有无线硬件的读者完全可以用它完成大部分练习**。

## 2. 工作原理

### 2.1 两种扫描方式的区别

| | airodump-ng 默认（被动） | `-x`（主动扫描模拟） |
| --- | --- | --- |
| 做法 | 只接收，不发送任何东西 | 主动发 Probe Request |
| 可检测性 | **完全不可检测** | 会被 WIDS 发现 |
| 能发现什么 | 只在 AP 定期广播 Beacon 时发现 | 能主动询问隐藏 SSID |
| 推荐 | ✅ 默认用这个 | 只在必要时（比如找隐藏网络） |

**核心事实**：**airodump-ng 默认完全不发射任何帧**。它是纯被动的。这使得它在网络层面不可检测——这一点对蓝队很重要（见第 9 节）。

### 2.2 Beacon 帧与 AP 列表

AP 大约每 **100 ms（10 Hz）** 广播一次 **Beacon 帧**，里面包含：

| 字段 | 内容 |
| --- | --- |
| BSSID | AP 的 MAC 地址 |
| SSID | 网络名（可为空或隐藏） |
| Channel | 信道 |
| RSN/WPA IE | 加密方式（WPA2/WPA3、CCMP/TKIP、PSK/802.1X） |
| Supported Rates | 速率 |
| Timestamp | AP 的 uptime（`--uptime` 可显示） |

airodump-ng 通过被动接收 Beacon 来构建 AP 列表（表格上半部分），并在 `Beacons` 列显示收到的 Beacon 数量。

### 2.3 客户端列表与「关联」的判断

airodump-ng 从所有帧中提取 **MAC 地址**，把没有出现在任何 Beacon 里的 MAC 识别为客户端（表格下半部分）。判断「客户端属于哪个 AP」的依据是：

| 帧类型 | 含义 |
| --- | --- |
| Data 帧的 ToDS/FromDS 位 | 客户端 ↔ AP 的数据通信 |
| **Association Request/Response** | 客户端已关联到某个 BSSID |
| **Reassociation** | 客户端漫游到另一个 AP |
| Probe Request 里的 SSID | 客户端**曾经连过**的网络（非常有情报价值） |
| EAPOL 帧 | 握手过程 |

**`Probes` 列的价值**：客户端会主动探测它记得的 SSID。这能暴露：
- 该设备连接过的所有网络（用来做邪恶孪生的目标）；
- 隐藏网络的真实 SSID（客户端探测时会明文发出）。

### 2.4 跳频与「为什么必须锁定信道」

网卡在任一时刻**只能监听一个信道**（除非有多张网卡）。airodump-ng 默认的行为是：

```
在 2.4 GHz 的 1~14 信道之间循环跳频，每个信道停留约 250 ms
```

**问题**：如果目标 AP 在 6 信道，而网卡只有 1/14 的时间在 6 信道，那么：

- Beacon 会漏掉（但影响不大，因为 Beacon 每 100 ms 一次）；
- **握手包极可能漏掉**——握手只有 4 个帧，转瞬即逝，**错过就没了**。

**解决**：抓目标时**必须** `-c <信道>` 锁定，并且用 `--bssid` 过滤（`--bssid` 隐含不跳频）。

**`RXQ` 列的含义**：接收质量百分比。锁定单一信道时 RXQ 通常接近 100%；如果 RXQ 很低，说明网卡在跳频或有干扰。

### 2.5 WPA 握手如何被捕获

[aircrack-ng](aircrack-ng.md) 已详述四次握手。在 airodump-ng 的视角：

1. 当它收到 **EAPOL 帧**（握手报文），会尝试把同一个 4 次握手的 msg1+msg2（或 msg3+msg4）配对；
2. 配对成功（MIC 可验证）就在右上角显示：

```
][ WPA handshake: AA:BB:CC:DD:EE:FF
```

3. **同一个 BSSID 只提示一次**——之后再抓到新的握手不会重复提示；
4. 所有 EAPOL 帧都保存在 `.cap` 文件里。

**`.cap` 与 `.csv` 与 `.kismet.netxml`**：

| 文件 | 内容 |
| --- | --- |
| `cap-01.cap` | **完整的原始帧**（pcap 格式）——**破解用这个** |
| `cap-01.csv` | 表格数据的 CSV（AP 列表、客户端列表） |
| `cap-01.kismet.csv` / `.netxml` | Kismet 兼容格式 |
| `cap-01.log.csv` | 日志（新版） |

**注意**：文件名会自动带序号（`-01`、`-02`…），每次重启 airodump 序号递增。`--write-interval` 控制 CSV 的写盘间隔。

### 2.6 PMKID 捕获

PMKID 存在于 RSN IE 中（见 [aircrack-ng](aircrack-ng.md) 2.3 节）。airodump-ng 的 `--wps` 选项会显示 WPS 信息，但要抓 PMKID 更推荐：

```bash
# hcxdumptool 是专门为 PMKID 设计的工具
sudo hcxdumptool -i wlan0mon -o dump.pcapng --enable_status=1
hcxpcapngtool -o hash.22000 dump.pcapng
```

**为什么用 hcxdumptool**：PMKID 通常需要**主动发一个关联请求**才能从 AP 拿到（这与 airodump 的纯被动模式冲突）。`hcxdumptool` 主动发帧，抓取效率高得多。

### 2.7 WEP 的 IV 捕获

WEP 破解需要大量 IV（见 [aircrack-ng](aircrack-ng.md) 2.5 节）。airodump-ng 的 `--ivs` 选项可以**只保存 IV**，文件小得多：

```bash
sudo airodump-ng --ivs -w wep-capture -c 6 wlan0mon
# 生成 wep-capture-01.ivs
```

配合 [aireplay-ng](aireplay-ng.md) 的 ARP 重放攻击加速 IV 收集。

## 3. 安装与快速上手

```bash
sudo apt install aircrack-ng
airodump-ng --help | head -60
```

**最短工作流**（假设已完成 [airmon-ng](airmon-ng.md) 的准备工作）：

```bash
# 1) 侦察
sudo airodump-ng wlan0mon

# 2) 锁定目标抓包（Ctrl+C 停下来）
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w /tmp/cap wlan0mon

# 3) 另一个终端触发重连
sudo aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF wlan0mon

# 4) 看到 WPA handshake 提示后停止，破解
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b AA:BB:CC:DD:EE:FF /tmp/cap-01.cap
```

## 4. 核心参数详解

### 4.1 主选项

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `<interface>[,<iface>,...]` | 监听接口（**可给多个**，用逗号分隔） | 多块网卡可同时监听多个信道 |
| `--write <prefix>` | 抓包文件前缀 | **抓包必须加**，否则数据只在屏幕上 |
| `-c <channels>` / `--channel <channels>` | **锁定信道**（可多个，如 `1,6,11`） | **抓目标必加** |
| `-C <frequencies>` | 用 MHz 频率指定（而非信道号） | 5 GHz 频段更直观 |
| `--band <abg>` | 跳频时使用的频段：`a`=5G，`b`=2.4G，`g`=2.4G | 默认只跳 2.4 GHz；5 GHz 用 `--band a` |
| `-r <file>` | **从 pcap/ivs 文件读取**（不做实际抓包） | **无网卡时的练习路径** |
| `--real-time` | 从文件读时模拟真实到达速率 | 演示用 |
| `-w` 的补充：`--output-format <formats>` | 输出格式：`pcap`/`ivs`/`csv`/`gps`/`kismet`/`netxml`/`logcsv` | 默认 pcap+csv+kismet |
| `--write-interval <seconds>` | 文件写盘间隔 | 默认 1 秒；磁盘 I/O 高可调大 |
| `--ivs` | **只保存 IV**（WEP 专用） | WEP 抓包时文件小得多 |
| `--beacons` | 把**所有 Beacon** 写入 dump 文件 | 需要完整帧时用；文件会变大 |
| `--update <secs>` | **屏幕刷新间隔**（默认 1 秒） | 慢速终端调大 |
| `-f <msecs>` | 跳频时每信道停留毫秒数（默认约 250） | — |
| `--berlin <secs>` | 多久没收到包就从屏幕移除 AP/客户端（默认 120 秒） | 长时间扫描时调大 |
| `--showack` | 显示 ack/cts/rts 统计 | 调优 |
| `-h` | `--showack` 时隐藏已知客户端 | — |
| `-x <msecs>` | **主动扫描模拟**（会发射 Probe Request） | ⚠️ 可被检测；仅在必要时 |
| `-a` | 过滤掉未关联的客户端 | 减少噪声 |
| `-z` | 过滤掉已关联的客户端 | 只看未关联的（找 probe 情报） |
| `--uptime` | 从 Beacon Timestamp 显示 AP 的在线时长（uptime） | **换过固件/重启过的 AP 一眼可见** |
| `--manufacturer` | 显示厂商（OUI 查询） | 需要 `airodump-ng-oui-update` 更新 OUI 库 |
| `--wps` | 显示 WPS 信息 | 配合 [reaver](reaver.md) 时用 |
| `--ignore-negative-one` | 抑制 `fixed channel <iface>: -1` 提示 | 老驱动常见问题 |
| `--background <enable>` | 覆盖后台检测 | 罕见 |
| `--cswitch <method>` | 跳频方式：`0`=FIFO（默认），`1`=轮询，`2`=跳到最后 | 多网卡调优 |

### 4.2 过滤选项（都很实用）

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `--bssid <bssid>` | 只看指定 AP（**可多次**） | **抓包必加** |
| `--essid <essid>` | 按网络名过滤（可多次） | SSID 可被伪造，不如 BSSID 可靠 |
| `--essid-regex <regex>` | 按正则过滤 ESSID | 批量筛选同前缀的网络 |
| `--encrypt <suite>` | 按加密套件过滤（可多次） | 例如只看 WEP |
| `--netmask <netmask>` | 按子网掩码过滤 | 罕见 |
| `--min-packets <int>` | 至少收到 N 个包才显示（默认 2） | 减少噪声 |
| `--min-power <int>` | 过滤弱信号（默认 -120） | `--min-power -70` 只看近处的 |
| `--min-rxq <int>` | 过滤低 RXQ（默认 0） | 需配 `-c` 或 `-C` |

### 4.3 信道/频段

| 参数 | 作用 |
| --- | --- |
| `--ht20` / `--ht40-` / `--ht40+` | 设置 802.11n 的带宽（HT20/HT40-） |
| `--ignore-other-chans` | 过滤掉其他信道（需配 `-c`） |
| `--cswitch <method>` | 跳频方式 |

### 4.4 界面相关

| 参数 | 作用 |
| --- | --- |
| `--help` | 显示帮助 |
| 运行中按 `a` | 在「AP 列表」与「客户端列表」之间切换显示 |
| 运行中按 `o` / `p` / `s` / `d` | 排序切换（`o`=按包数、`p`=PWR、`s`=STA、`d`=Data） |
| 运行中按 `r` | 按 BSSID 排序 |
| 运行中按 `Tab` | 在排序字段之间循环 |
| 运行中按 `空格` | 冻结/解冻显示 |
| `Ctrl+C` | 停止 |

## 5. 实战演练

**环境声明**：以下全部操作针对**你自己拥有的 Wi-Fi 网络与路由器**，或隔离实验室、已授权的测试目标。**严禁对任何非自有网络执行**。第 4 个场景完全不需要无线网卡，是最安全的学法。

### 场景 1：全信道侦察（第一步）

**前置**：已完成 [airmon-ng](airmon-ng.md) 的准备工作。

```bash
sudo airmon-ng check kill
sudo airmon-ng start wlan0
sudo airodump-ng wlan0mon
```

**预期输出**

```
 CH 13 ][ Elapsed: 24 s ][ 2026-09-15 11:05

 BSSID              PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID
 AA:BB:CC:DD:EE:FF  -42      240       58    2   6  130   WPA2 CCMP   PSK  lab-test
 11:22:33:44:55:66  -61      168        0    0  11  130   WPA2 CCMP   PSK  home-net
 22:33:44:55:66:77  -74      102        4    0   1   54   WEP  WEP         foo-legacy
 33:44:55:66:77:88  -88       44        0    0   6  130   WPA3 CCMP   SAE  modern-net
 44:55:66:77:88:99  -55      190       31    1   6  130   WPA2 CCMP   PSK  <length: 12>

 BSSID              STATION            PWR   Rate    Lost    Frames  Notes  Probes
 AA:BB:CC:DD:EE:FF  12:34:56:78:9A:BC  -38   1e- 1      0       58
 AA:BB:CC:DD:EE:FF  98:76:54:32:10:FE  -52   1e- 1      0       12
 11:22:33:44:55:66   AA:BB:CC:11:22:33  -60   0-1       0        4           lab-test
```

**逐列解读（AP 表）**：

| 列 | 含义 | 关注点 |
| --- | --- | --- |
| `CH` | 当前扫描到的信道 | 记下目标的信道 |
| `Elapsed` | 已运行时间 | — |
| `BSSID` | AP 的 MAC | **记下目标** |
| `PWR` | 信号强度 dBm。**-30 最强，-90 很弱** | 低于 -80 抓包会困难 |
| `Beacons` | 收到的 Beacon 帧数 | 一直在涨说明 AP 正常广播 |
| `#Data` | 数据帧数量 | **有数据说明有客户端活动** |
| `#/s` | 每秒数据帧数 | 高流量网络抓握手更容易（EAPOL 可能自然出现） |
| `CH` | 信道 | — |
| `MB` | 最大速率 | — |
| `ENC` | 加密类型（`WEP`/`WPA`/`WPA2`/`WPA3`/`OPN`） | **决定攻击方式** |
| `CIPHER` | 密码算法（`CCMP`/`TKIP`/`WEP`） | TKIP 比 CCMP 弱 |
| `AUTH` | 认证（`PSK`/`MGT`/`SAE`） | `SAE` = WPA3，**无法离线破解** |
| `ESSID` | 网络名 | `<length: 12>` = **隐藏 SSID**（只暴露长度） |

**逐列解读（客户端表）**：

| 列 | 含义 | 关注点 |
| --- | --- | --- |
| `BSSID` | 客户端关联的 AP（空=未关联） | — |
| `STATION` | 客户端 MAC | — |
| `PWR` | 客户端信号强度 | — |
| `Rate` | 速率 | — |
| `Lost` | 丢失的数据包数 | — |
| `Frames` | 与该 AP 的帧数 | — |
| `Notes` | 备注 | — |
| `Probes` | **客户端主动探测的 SSID** | **情报金矿**：暴露它连过的所有网络 |

**关键判断**：

| 观察 | 结论 |
| --- | --- |
| 目标 AP 下有客户端 | ✅ **可以抓握手** |
| 目标 AP 下没有客户端 | ⚠️ 只能用 PMKID，或等客户端上线 |
| `AUTH` 是 `SAE`（WPA3） | ⚠️ **纯 WPA3 无法离线破解**；检查是否同时广播 WPA2 |
| `ENC` 是 `WEP` | 🔓 几分钟就能破（但 2026 年基本遇不到） |
| `ESSID` 是 `<length: N>` | 隐藏 SSID。**客户端 Probe 会暴露真名** |

按 `Ctrl+C` 停止。

### 场景 2：锁定目标抓 WPA 握手（核心流程）

**步骤 1：锁定信道与 BSSID 开始抓包**

```bash
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w /tmp/wpa wlan0mon
```

**预期输出**

```
 CH  6 ][ Elapsed: 5 s ][ 2026-09-15 11:12

 BSSID              PWR RXQ  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID
 AA:BB:CC:DD:EE:FF  -42 100      185       42    3   6  130   WPA2 CCMP   PSK  lab-test

 BSSID              STATION            PWR   Rate    Lost    Frames  Notes  Probes
 AA:BB:CC:DD:EE:FF  12:34:56:78:9A:BC  -38    1e- 1      0       42
```

| 参数 | 作用 |
| --- | --- |
| `-c 6` | **锁定信道**（不锁定几乎抓不到握手） |
| `--bssid AA:...` | 只关注目标 AP（**隐含不跳频**） |
| `-w /tmp/wpa` | 写入 `/tmp/wpa-01.cap` 等 |

**`RXQ 100` 是好现象**——说明网卡稳定在这个信道上。

**步骤 2：另一个终端触发客户端重连**

```bash
# ⚠️ 仅限自有网络！deauth 会中断通信
sudo aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF wlan0mon
```

（[aireplay-ng](aireplay-ng.md) 详解此命令）

**步骤 3：观察抓包终端**

```
 CH  6 ][ Elapsed: 45 s ][ 2026-09-15 11:13 ][ WPA handshake: AA:BB:CC:DD:EE:FF
```

**`WPA handshake: ...` 出现 = 成功**。按 `Ctrl+C` 停止。

**步骤 4：检查抓到的文件**

```bash
ls -lh /tmp/wpa-01.*
# -rw-r--r-- 1 root root 1.2M ... /tmp/wpa-01.cap     ← 破解用这个
# -rw-r--r-- 1 root root  12K ... /tmp/wpa-01.csv     ← 表格数据
# -rw-r--r-- 1 root root  45K ... /tmp/wpa-01.kismet.csv
# -rw-r--r-- 1 root root  60K ... /tmp/wpa-01.kismet.netxml
```

**步骤 5：验证握手并破解**

```bash
# 用 aircrack-ng 检查抓包文件里有什么
aircrack-ng /tmp/wpa-01.cap
```

**预期输出**

```
                               Aircrack-ng 1.7

      [00:00:00] 2/2 keys tested (1245.32 k/s)

                    Number of networks: 1
            Network BSSID: AA:BB:CC:DD:EE:FF
             Network ESSID: lab-test
            Network Cipher: CCMP (WPA2)

      Number of EAPOL candidates: 1
      ...
```

或者直接进入破解：

```bash
printf 'wrongpass\nlabpassword123\n' > /tmp/lab.txt
aircrack-ng -w /tmp/lab.txt -b AA:BB:CC:DD:EE:FF /tmp/wpa-01.cap
```

**步骤 6：清理并导出给 hashcat**

```bash
# 只保留握手，文件变小（便于传输）
wpaclean /tmp/clean.cap /tmp/wpa-01.cap

# 转成 hashcat 格式
hcxpcapngtool -o /tmp/wifi.22000 /tmp/wpa-01.cap
hashcat -m 22000 /tmp/wifi.22000 /usr/share/wordlists/rockyou.txt -O
```

### 场景 3：抓 PMKID（不需要客户端）

**问题**：目标 AP 当前**没有客户端**连接，抓不到握手。

**解决**：PMKID 攻击——**只要 AP 支持，就能在客户端缺席时拿到可离线验证的数据**。

```bash
# 方式 A：hcxdumptool（推荐，专为 PMKID 设计）
sudo apt install hcxtools
sudo hcxdumptool -i wlan0mon -o /tmp/dump.pcapng --enable_status=1
# 观察输出里的 [PMKID] 或 [EAPOL] 行
# Ctrl+C 停止

# 转换并破解
hcxpcapngtool -o /tmp/hash.22000 /tmp/dump.pcapng
hashcat -m 22000 /tmp/hash.22000 /usr/share/wordlists/rockyou.txt

# 方式 B：只用 airodump-ng（--wps 会显示 WPS 信息，也能抓到含 PMKID 的帧）
sudo airodump-ng --bssid AA:BB:CC:DD:EE:FF -c 6 -w /tmp/pmkid --wps wlan0mon
```

**注意**：`hcxdumptool` **会主动发送帧**（不再是纯被动），因此在网络层面**可能被 WIDS 检测到**。这也是它与 airodump-ng 的关键区别。

**PMKID 与握手的取舍**：

| | 握手 | PMKID |
| --- | --- | --- |
| 需要客户端 | ✅ | ❌ |
| 需要 deauth | ✅（通常） | ❌ |
| 会被 WIDS 发现 | deauth 会被发现 | hcxdumptool 主动发帧会被发现 |
| 成功率 | 看客户端是否在线 | 看 AP 是否在 RSN IE 里带 PMKID（不是所有 AP 都带） |

**实战建议：两种都试**。

### 场景 4：从文件回放（不需要无线网卡）

**这是最安全、也最实用的练习路径**。

```bash
# 从文件读取并显示（不做任何实际抓包）
sudo airodump-ng -r /tmp/wpa-01.cap
```

**预期输出**：与真实扫描相同的两张表。

**能学到的**：表格所有字段的含义、AP/客户端关系、信道、加密方式。

**不能学的**：真实抓包的手感（信号强度、跳频、deauth 时机）。

**配套分析手段**：

```bash
# 用 aircrack-ng 看网络与握手摘要
aircrack-ng /tmp/wpa-01.cap

# 用 tshark 看 EAPOL 报文（握手的四个帧）
tshark -r /tmp/wpa-01.cap -Y 'eapol'
#    1   0.000000  AA:BB:CC:DD:EE:FF → 12:34:56:78:9A:BC EAPOL 155 Key (Message 1 of 4)
#    2   0.001234  12:34:56:78:9A:BC → AA:BB:CC:DD:EE:FF EAPOL 155 Key (Message 2 of 4)
#    3   0.002345  AA:BB:CC:DD:EE:FF → 12:34:56:78:9A:BC EAPOL 155 Key (Message 3 of 4)
#    4   0.003456  12:34:56:78:9A:BC → AA:BB:CC:DD:EE:FF EAPOL 155 Key (Message 4 of 4)

# 看完整详情
tshark -r /tmp/wpa-01.cap -Y 'eapol' -V | head -80

# 用 Wireshark 图形化查看（推荐新手）
wireshark /tmp/wpa-01.cap
```

**在 Wireshark 里要看的**：

- `无线 → WLAN Traffic`（统计 → WLAN Traffic）：网络与客户端汇总；
- 过滤器 `eapol`：只看握手；
- 过滤器 `wlan.fc.type_subtype == 8`：只看 Beacon；
- 过滤器 `wlan.ssid`：含 SSID 的帧；
- `Preferences → Protocols → IEEE 802.11 → Decryption keys`：配置口令后可**直接解密数据帧**（前提是你知道口令）。

**用已有的示例抓包**：

```bash
# 找本机的示例文件
find /usr/share -name '*.cap' -o -name '*.pcap' 2>/dev/null | head

# Wireshark 官方示例抓包（含 802.11）
# https://wiki.wireshark.org/SampleCaptures
```

### 场景 5：找隐藏 SSID（利用 Probe 情报）

**背景**：AP 可以配置为「不广播 SSID」（`ESSID` 显示为 `<length: N>`）。但这**不是真正的隐藏**——因为：

1. 客户端关联时**必须明文发送 SSID**；
2. 客户端会**主动 Probe** 它记得的网络名。

**做法**：

```bash
# 1) 显示未关联的客户端（它们正在发 Probe）
sudo airodump-ng -z wlan0mon
```

**看 `Probes` 列**：客户端探测的 SSID 会显示在本行的 `STATION` 附近。

```bash
# 2) 或者等到有客户端关联/重连，SSID 会出现在目标 AP 的行里
#    因为 Association/Reassociation 帧里带 SSID
```

**解读**：`Probes` 列的信息价值极高——它告诉你**这台设备曾经连过哪些网络**。这也是「邪恶孪生」攻击选择目标的依据（攻击者会伪装成设备记得的网络名）。

## 6. 输出解读

### 屏幕界面速查

```
 CH  6 ][ Elapsed: 45 s ][ 2026-09-15 11:13 ][ WPA handshake: AA:BB:CC:DD:EE:FF
                ↑                    ↑                    ↑
            已运行时间            当前时间          ★ 抓到握手的标志
```

**右上角的提示栏是最重要的信息区**：

| 显示 | 含义 |
| --- | --- |
| `WPA handshake: <BSSID>` | ✅ **抓到握手**，可以停止了 |
| `WPA handshake: <BSSID>` 后面无内容 | 握手不完整（只有一部分 EAPOL） |
| （什么都没有） | 还没抓到握手 |
| `fixed channel wlan0mon: -1` | 信道未同步（老驱动问题） |

### AP 表关键字段的判读规则

| 字段 | 判读规则 |
| --- | --- |
| `PWR` | **-30 到 -50**：很好；**-50 到 -70**：可用；**-70 到 -85**：勉强；**低于 -85**：抓包会很不稳定 |
| `Beacons` 停滞 | AP 可能关闭了广播，或信号太弱，或网卡跑偏了信道 |
| `#Data` 一直为 0 | 没有客户端活动（也可能有客户端但很闲） |
| `ENC` | `OPN`=开放；`WEP`=可破；`WPA`/`WPA2`=可离线破解；`WPA3`=SAE，不可离线破解 |
| `AUTH` | `PSK`=预共享密钥；`MGT`=802.1X（需要证书）；`SAE`=WPA3 |
| `CIPHER` | `CCMP`=AES（强）；`TKIP`=老算法（弱，有已知攻击）；`WEP`=已破 |
| `ESSID` = `<length: N>` | 隐藏 SSID |

### 客户端表的关键字段

| 字段 | 含义 | 情报价值 |
| --- | --- | --- |
| `STATION` | 客户端 MAC | 前 3 字节是厂商 OUI |
| `BSSID` 为空 | 客户端**未关联**任何 AP | 它正在探测（看 `Probes`） |
| `Probes` | 客户端主动探测的 SSID | ⭐ **暴露设备连过的所有网络** |
| `Frames` | 与该 AP 的帧数 | 数量在涨 = 设备活跃 = 更容易抓到握手 |

### 文件输出

| 文件 | 内容 | 用途 |
| --- | --- | --- |
| `<prefix>-01.cap` | 完整原始帧（pcap） | **破解、分析** |
| `<prefix>-01.csv` | AP/客户端表格 CSV | 生成报告、`airgraph-ng` 画图 |
| `<prefix>-01.kismet.csv` / `.netxml` | Kismet 兼容格式 | 导入 kismet 数据库 |
| `<prefix>-01.log.csv` | 日志（新版） | 时间线分析 |
| `<prefix>-01.ivs` | 仅 IV（配 `--ivs`） | WEP 破解 |
| `<prefix>-01.gps` | GPS 坐标（配 `--gpsd`） | 车载勘测（wardriving） |

**序号规则**：每次启动 airodump-ng 对同一个前缀，序号递增（`-01`、`-02`…）。**别把两次抓包搞混**。

**判断成功**：右上角出现 `WPA handshake:`，或 `aircrack-ng file.cap` 显示 `Number of EAPOL candidates: 1`。

**下一步**：

| 情况 | 动作 |
| --- | --- |
| 抓到握手 + 小字典 | 直接用 [aircrack-ng](aircrack-ng.md) 破解 |
| 抓到握手 + 要跑大字典 | 导出 22000 → [hashcat](../04-口令攻击/hashcat.md) |
| 抓不到握手（无客户端） | 用 PMKID（`hcxdumptool`） |
| 抓不到握手（有客户端但 deauth 无效） | 注入失败 → [aireplay-ng](aireplay-ng.md) `--test` 诊断 |
| 目标是 WPA3 | **无法离线破解**；确认是否为混合模式 |
| 目标是 WEP | 用 `--ivs` 抓 IV + [aireplay-ng](aireplay-ng.md) ARP 重放加速 |

## 7. 与其他工具配合

```text
[airmon-ng start] → wlan0mon
        ↓
[airodump-ng 侦察] → 找目标 AP + 客户端 + 信道
        ↓
[airodump-ng 锁定抓包 -c <ch> --bssid <bssid> -w cap]
        ↑
[aireplay-ng --deauth]（触发重连，加速抓包）
        ↓
   ┌────┴─────────────────────────────┐
   ↓                                  ↓
[aircrack-ng 破解]              [hcxpcapngtool → 22000]
   ↓                                  ↓
[airdecap-ng 解密流量]          [hashcat -m 22000]（GPU，快 10~100×）
   ↓                                  ↓
[wireshark 分析明文]            [结果]
```

| 组合 | 说明 |
| --- | --- |
| **airmon-ng → airodump-ng** | 必须先切监听模式 |
| **airodump-ng ↔ aireplay-ng** | 抓包 + deauth 是标配组合 |
| **airodump-ng → aircrack-ng** | 直接消费 `.cap` 文件 |
| **airodump-ng → hashcat** | 通过 `hcxpcapngtool` 或 `aircrack-ng -j` |
| **airodump-ng → airdecap-ng** | 已知口令时解密流量 |
| **airodump-ng → wireshark/tshark** | 深入分析帧结构与 EAPOL |
| **airodump-ng → reaver** | 从 `--wps` 发现的目标启动 WPS 攻击 |
| **airodump-ng → airgraph-ng** | 从 CSV 生成网络拓扑图 |
| **[wifite](wifite.md)** | 内部调用 airodump-ng，全自动 |

**注意**：[wifite](wifite.md) 和 [bettercap](bettercap.md) 会自己调用 airodump-ng/等价逻辑，**用它们时不需要手工先跑 airodump-ng**。

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| **抓了几十秒突然什么都抓不到** | NetworkManager/wpa_supplicant 把网卡切回托管模式 | `sudo airmon-ng check kill` 后**重新** `airmon-ng start` |
| `WPA handshake:` 一直不出现 | ① 信道没锁定 → 加 `-c`；② 没有客户端 → 用 PMKID；③ deauth 无效 → 见下；④ 距离太远 |
| `RXQ` 很低（< 50） | 跳频干扰，或有别的东西在抢网卡 | 加 `-c` 锁定；确认没有第二个进程在用网卡 |
| `#Data` 一直是 0 | 客户端很闲（只发 Beacon，没数据） | 正常；握手与数据量无关，只要客户端在 |
| `fixed channel wlan0mon: -1` | 老驱动无法确定信道 | 加 `--ignore-negative-one`；或 `iw dev wlan0mon set channel 6` |
| 有 AP 但**客户端表为空** | 没有客户端关联，或客户端离得太远 | 等；或改用 PMKID |
| 隐藏 SSID 抓不到名字 | AP 不广播 SSID | 等客户端关联（会明文发送 SSID）；或看其他客户端的 `Probes` 列 |
| `--manufacturer` 没有输出 | OUI 数据库未更新 | `sudo airodump-ng-oui-update` |
| `.cap` 文件巨大 | 抓了太久，或有高流量网络 | 只抓目标（`--bssid`）；用 `--ivs`（WEP）；及时按 `Ctrl+C` |
| `.csv` 文件为空/不完整 | `--write-interval` 太长，或异常退出 | 正常按 `Ctrl+C` 退出；调小 `--write-interval` |
| 破解时说 `No valid WPA handshakes found` | 握手不完整 | 重新抓；`wpaclean` 清理后重试；多发几次 deauth |
| 文件名序号混乱 | 多次运行同一前缀 | 每次抓包用不同前缀（如 `-w /tmp/cap-run1`） |
| 5 GHz 的网络扫不到 | 默认只跳 2.4 GHz | 加 `--band a`（或 `--band abg`） |
| 抓包文件在虚拟机里打不开 | USB 直通/文件权限 | 检查权限；文件归 root 所有，用 `sudo` 或 `chown` |
| 用 `-r` 从文件读时提示没数据 | 文件里确实没有相应帧 | `aircrack-ng file.cap` 或 `tshark -r file.cap` 先确认内容 |
| 抓到了握手但破解不出 | 口令不在字典里 | 换字典；用 [cewl](../04-口令攻击/cewl.md)/[crunch](../04-口令攻击/crunch.md) 造定向字典；用 [hashcat](../04-口令攻击/hashcat.md) GPU |

## 9. 防御视角（蓝队）

### 9.1 核心事实：被动监听不可检测

airodump-ng 默认**只接收、不发射**。这意味着：

| 事实 | 对蓝队的含义 |
| --- | --- |
| 监听模式不产生任何流量 | 网络侧**无法检测** |
| 没有「异常的帧」可以匹配 | 不存在基于协议的检测规则 |
| **唯一可观测的是下游行为** | deauth、关联请求洪泛、假 AP |

**因此蓝队的工作不是「检测监听」，而是「让监听无收益」**。

### 9.2 攻击面与对策

| airodump-ng 能获取的 | 蓝队对策 | 有效性 |
| --- | --- | --- |
| AP 列表、SSID、信道、加密方式 | **隐藏 SSID**（仅轻微增加难度，不是有效防护）；降低发射功率减少覆盖 | ⚠️ 低 |
| **客户端 MAC 列表** | **MAC 随机化**（现代手机/Windows 已默认） | ✅ 中 |
| **客户端的 Probe 列表**（连过的网络） | MAC 随机化 + 关闭「自动连接开放网络」 | ✅ 中 |
| **WPA 握手包** | **WPA3-SAE**（无法离线验证口令）；**长随机 PSK（≥ 20 位）**；**PMF** | ✅ **高** |
| **PMKID** | WPA3-SAE；部分 AP 可关闭相关特性 | ✅ 高 |
| WEP IV | **弃用 WEP** | ✅ 必做 |
| deauth 的效果 | **802.11w（PMF）** —— 管理帧保护会忽略伪造的 deauth | ✅ **高** |

### 9.3 优先级最高的六条措施

```text
1. 升级到 WPA3-SAE（纯 WPA3 模式，不要停留在 WPA3/WPA2 混合模式）
2. PSK 长度 ≥ 20 位且随机（不要出现在任何字典里）
3. 启用 802.11w / PMF（阻断 deauth）
4. 关闭 WPS
5. 企业环境用 802.1X + EAP-TLS（每设备独立证书）
6. 降低 AP 发射功率到必要覆盖范围；敏感区域用屏蔽措施
```

**关于隐藏 SSID 的一个重要提醒**：

> **隐藏 SSID 不是安全措施**。攻击者可以：
> 1. 等待客户端关联（Association 帧明文带 SSID）；
> 2. 观察其他客户端的 Probe Request（它们会主动喊出网络名）；
> 3. 发送 deauth 迫使客户端重连，从而捕获 SSID。
>
> **隐藏 SSID 只增加了几秒钟的难度，却给运维带来麻烦**。不要依赖它。

### 9.4 检测规则思路

虽然监听不可检测，但**下游行为可以**：

```text
# 1) deauth 洪泛（最常见的抓握手前置动作）
if count(deauth_frames, src=bssid, 10s) > 20
then alert "possible deauth flood / handshake capture attempt"

# 2) 单调的 deauth reason code（工具默认用 7）
if count(deauth where reason == 7, 60s) > 50 and distinct_stations > 5
then alert "possible automated deauth"

# 3) 客户端重连风暴（deauth 的间接后果）
if count(assoc_requests, 60s) > 100 and distinct_stations > 10
then alert "possible deauth-induced reconnect storm"

# 4) 未知 BSSID（假 AP / 邪恶孪生）
if bssid not in baseline_bssid_list
then alert "rogue AP detected"

# 5) 同一 SSID 出现多个 BSSID（邪恶孪生）
if count(distinct bssid where ssid = X) > expected_count
then alert "possible evil twin on SSID X"

# 6) 大量未关联的关联请求（PMKID 攻击的副产品）
if count(assoc_requests from unassociated stations, 60s) > 50
then alert "possible PMKID harvesting"
```

**推荐工具**：[kismet](kismet.md)（自带 WIDS 功能）、企业 AP 控制器的内置 WIPS、或自建基于 Kismet 的告警。

### 9.5 一个容易被忽视的点

**`Probes` 列暴露的隐私问题**值得单独强调：

> 你的手机在待机时会**持续广播它连接过的所有网络名**。这不仅是攻击者的情报来源，**本身也是隐私泄露**（暴露你去过的酒店、公司、家庭网络名）。
>
> 对策：**开启 MAC 随机化**（Android/iOS/Windows 10+ 都有此选项），并**删除不需要的已保存网络**。

## 10. 参考

- 官方文档：<https://www.aircrack-ng.org/doku.php?id=airodump-ng>
- 官方站点：<https://www.aircrack-ng.org/>
- Kali 工具页：<https://www.kali.org/tools/aircrack-ng/>
- 本机手册：`man airodump-ng`
- 本机帮助：`airodump-ng --help`（完整参数表）
- Wireshark 的 802.11 示例抓包：<https://wiki.wireshark.org/SampleCaptures>
- 相关本目录：[aircrack-ng](aircrack-ng.md)（套件总览）、[airmon-ng](airmon-ng.md)、[aireplay-ng](aireplay-ng.md)、[wifite](wifite.md)、[reaver](reaver.md)、[kismet](kismet.md)、[bettercap](bettercap.md)
- 相关其他目录：[hashcat](../04-口令攻击/hashcat.md)、[wordlists](../04-口令攻击/wordlists.md)、[tcpdump](../07-嗅探与欺骗/tcpdump.md)、[wireshark](../07-嗅探与欺骗/wireshark.md)

## ⚠️ 法律与伦理

**监听本身就是接收他人通信**。在许多司法辖区，**即使不破解，单纯截获通信内容已构成违法**。

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条 | 非法侵入计算机信息系统；非法获取计算机信息系统数据 |
| 《刑法》 | 第二百八十六条 | 破坏计算机信息系统（deauth 造成网络中断） |
| 《无线电管理条例》 | 相关条款 | 擅自使用无线电频率、干扰合法无线电业务 |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《个人信息保护法》 | 相关条款 | 截获通信内容涉及个人信息处理 |

**本教程仅适用于**：

- ✅ **你自己拥有的 Wi-Fi 网络与你自己的路由器**
- ✅ 有**书面授权**、明确列出授权 SSID 与时间窗的无线渗透测试
- ✅ 你自己搭建的隔离无线实验室（有屏蔽措施）
- ✅ CTF 靶场 / 授权的无线练习平台

**强烈推荐的学习方式**：**用「场景 4：从文件回放」的方式**——它不需要无线网卡，不发射任何信号，不接收任何他人通信，但能覆盖 90% 的知识点（字段含义、握手结构、破解流程、hashcat 转换）。

**严禁**：对邻居、公司、公共场所的任何 Wi-Fi 执行本文任何命令。
