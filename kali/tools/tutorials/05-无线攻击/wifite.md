# Wifite2（无线审计自动化）

> **一句话**：把 [airmon-ng](airmon-ng.md) → [airodump-ng](airodump-ng.md) → [aireplay-ng](aireplay-ng.md) → [aircrack-ng](aircrack-ng.md) / [reaver](reaver.md) / [hashcat](../04-口令攻击/hashcat.md) 这条链路封装成一条命令，交互式选择目标后全自动完成抓包与破解。
> **分类**：无线攻击 ｜ **Kali 包**：`wifite` ｜ **官方文档**：<https://github.com/kimocoder/wifite2>

## 1. 它解决什么问题

手工做一次 WPA 抓包+破解，需要跨三个终端、敲七八条命令、记十几个参数。Wifite2 把这些变成：

```bash
sudo wifite
```

然后在一个界面里选目标、看进度、拿结果。

**它的定位**：

| 需求 | 用谁 |
| --- | --- |
| 快速审计一批网络，不想记参数 | **wifite** |
| 要理解每一步发生了什么 | 手工用 [airmon-ng](airmon-ng.md) / [airodump-ng](airodump-ng.md) / [aireplay-ng](aireplay-ng.md) |
| 要精细控制（特定攻击方式、特定时机） | 手工链路或 [bettercap](bettercap.md) |
| 只打 WPS | [reaver](reaver.md)（wifite 也封装它） |

**它调用了什么**：

| 环节 | 底层工具 |
| --- | --- |
| 开监听模式 | `airmon-ng` 或 `iw` |
| 扫描与抓包 | `airodump-ng`（或 `tshark`） |
| deauth | `aireplay-ng` |
| WPS 攻击 | `reaver` 或 `bully` |
| 破解 WPA | `aircrack-ng`（可选 hashcat） |
| 解析抓包 | `tshark`（依赖项之一） |
| 数据库 | `ieee-data`（MAC 厂商 OUI） |

**关键事实**：wifite **不是新技术的实现**，而是**编排层**。所以它的能力上限 = 底层工具的能力上限。它也不会绕过 PMF、不会破解 WPA3。

## 2. 工作原理

### 2.1 四个阶段的自动流水线

```
[1] 准备   启用监听模式（自动选网卡 / 或按 -i 指定）
              ↓
[2] 扫描   跳频监听，列出所有 AP（含 WPS/PMKID/客户端信息）
              ↕ 交互：你在界面上选择攻击哪些目标（或 -p 全部自动）
              ↓
[3] 攻击   对每个目标按策略依次尝试：
             ├─ WPS PIN / Pixie-Dust（如果 --wps 且 AP 支持）
             ├─ PMKID 抓取（默认开启，最快，不需要客户端）
             ├─ 握手抓取（airodump + 定向 deauth）
             └─ WEP（如果目标是 WEP）
              ↓
[4] 破解   抓到的数据立刻喂给 aircrack-ng（用 --dict 指定的字典）
```

### 2.2 PMKID 优先 —— wifite2 的核心改进

Wifite2 默认的攻击顺序是 **PMKID → 握手**，这是有道理的：

| | PMKID | 握手 |
| --- | --- | --- |
| 需要客户端 | ❌ **不需要** | ✅ 需要 |
| 需要 deauth | ❌ | ✅ |
| 对被攻击网络的影响 | **几乎无**（只发一个关联请求） | **明显**（客户端掉线重连） |
| 成功率 | 看 AP 是否在 RSN IE 带 PMKID | 看是否有客户端 |

**所以 wifite 默认先试 PMKID**——这既更快，也更「安静」。只有 PMKID 失败才会走 deauth 抓握手。

你可以用 `--no-pmkid` 关掉它，或用 `--pmkid` **只**用 PMKID。

### 2.3 交互 vs 自动

| 模式 | 触发 | 适用 |
| --- | --- | --- |
| **交互模式** | `sudo wifite` | 扫描后列出目标，按 `Ctrl+C` 结束扫描，然后逐个提示你确认 |
| **自动模式** | `-p <秒数>` / `--pillage` | 扫描 N 秒后**自动攻击所有目标**，无需人工确认 |
| **无限模式** | `-inf` | 持续扫描并攻击新出现的目标 |

**自动模式的风险**：`-p` 会**攻击它看到的所有网络**。如果你在居民区跑，那会攻击到邻居的 Wi-Fi——**这是违法的**。务必在**隔离环境**或**明确只有自己网络**的地方使用，且强烈建议配合 `-b`/`--bssid` 之类的限制（见第 8 节）。

### 2.4 WPS 攻击原理（wifite 封装了 reaver）

| 攻击 | 原理 | 耗时 |
| --- | --- | --- |
| **PIN 暴力** | WPS PIN 是 8 位数字，但**第 8 位是前 7 位的校验位**，且 AP 通常分两次验证（前 4 位 / 后 4 位）→ 实际只需约 **11000 次尝试** | 数小时（受 AP 锁定策略影响） |
| **Pixie-Dust** | 利用某些芯片组**随机数生成器弱**的缺陷，从一次 WPS 交互中直接推导出 PIN | **数秒到数分钟**（如果 AP 有漏洞） |

Pixie-Dust 是 wifite 里性价比最高的攻击：**如果 AP 芯片有缺陷，几秒钟就能拿到 PSK**。wifite 会自动尝试它（`--wps` 时）。

详见 [reaver](reaver.md)。

### 2.5 为什么 wifite 有时看起来「什么都没做」

常见原因：

| 现象 | 原因 |
| --- | --- |
| 一直停在扫描界面 | 需要你按 `Ctrl+C` 才能进入选择阶段（交互模式） |
| 目标全是灰色/跳过 | 目标不支持 wifite 能做的攻击（如纯 WPA3） |
| 抓到手握但立刻说 crack failed | 默认字典 `/usr/share/dict/wordlist-probable.txt` 很小 → 用 `--dict` 换字典 |
| 攻击 WPS 时反复重试 | AP 有 WPS 锁定机制（`--ignore-locks` 可强攻，但会拖很久） |

## 3. 安装与快速上手

```bash
sudo apt install wifite
wifite -h
```

**注意**：`wifite -h` 的输出**依赖是否加 `-v`**：

- `wifite -h` → 简短帮助
- `wifite -h -v` → **完整帮助**（包含所有参数）

```bash
wifite -h -v | less
```

**最短工作流**：

```bash
# 1) 交互模式（推荐新手）
sudo wifite

# 2) 只攻击 WPA/WPA2，跳过 WEP 和 WPS
sudo wifite --wpa

# 3) 先用小字典试，再指定大字典
sudo wifite --wpa --dict /usr/share/wordlists/rockyou.txt

# 4) 只做 PMKID（完全不用 deauth，对网络影响最小）
sudo wifite --pmkid
```

## 4. 核心参数详解

### 4.1 设置类

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-v, --verbose` | 显示更多信息（**打印它执行的每条命令和输出**） | ⭐ **新手必加** —— 这是学习底层链路的唯一途径 |
| `-i [interface]` | 指定无线接口，如 `wlan0mon`（默认会问你） | 多网卡时用；也可先手工 `airmon-ng start` |
| `-c [channel]` | 只扫描指定信道，如 `1,3-6`（默认扫描全部 2.4 GHz） | 已知目标信道可大幅加速 |
| `-inf, --infinite` | 无限攻击模式（持续扫描并攻击新目标） | 长时间无人值守时用 |
| `-mac, --random-mac` | 随机化网卡 MAC | 减少被追踪，但**也提示了「这有人在扫描」** |
| `-p [scan_time]` / `--pillage` | 扫描 N 秒后**自动攻击所有目标** | ⚠️ **高风险**：会攻击视野内所有网络 |
| `--kill` | 杀掉与 airmon/airodump 冲突的进程 | **推荐加**，等价于 `airmon-ng check kill` |
| `-pow, --power [min_power]` | 只攻击信号强度 ≥ 该值的网络 | `-pow 50` 只打很强的（通常是自己的） |
| `--skip-crack` | 只抓包，不破解 | 想自己用 hashcat 跑 GPU 时用 |
| `-first, --first [attack_max]` | 只攻击前 N 个目标 | 与 `-p` 配合限制范围 |
| `-ic, --ignore-cracked` | 隐藏之前已破解的目标 | 重复运行时用 |
| `--clients-only` | 只显示有客户端关联的网络 | 想抓握手时用（有客户端的才抓得到） |
| `--nodeauths` | **被动模式：永不 deauth 客户端** | ⭐ **对网络影响最小**；配合 `--clients-only` 使用 |
| `--daemon` | 退出后把网卡恢复成托管模式 | ⭐ **推荐加** —— 省去手工恢复 |

### 4.2 WEP 类（历史）

| 参数 | 作用 |
| --- | --- |
| `--wep` | 只显示 WEP 网络 |
| `--require-fakeauth` | 伪认证失败就放弃该目标（默认关） |
| `--keep-ivs` | 保留 `.IVS` 文件，用同一 IVS 格式抓包与破解（默认关） |

### 4.3 WPA 类

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `--wpa` | **只显示 WPA/WPA2 网络**（可能包含 WPS） | ⭐ 最常用 |
| `--wpa3` | 只显示 WPA3 网络（SAE/OWE） | ⚠️ 抓到也无法离线破解；主要用于**识别** |
| `--owe` | 只显示 OWE（Enhanced Open）网络 | 罕见 |
| `--new-hs` | 只抓新握手，忽略 `hs/` 目录里已有的 | 重复运行时用 |
| `--dict [file]` | 破解用的字典（默认 `/usr/share/dict/wordlist-probable.txt`） | ⭐ **必改**。默认字典很小 |

**默认字典的坑**：`/usr/share/dict/wordlist-probable.txt` 只有几千条，**破解成功率很低**。**一定要用 `--dict` 换成 [rockyou](../04-口令攻击/wordlists.md) 或自己的定向字典**。

### 4.4 WPS 类

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `--wps` | 只显示开启了 WPS 的网络 | 配合 `--wps-only` |
| `--wps-only` | **只用 WPS PIN 与 Pixie-Dust 攻击**（不做握手） | WPS 开着时性价比最高 |
| `--bully` | 用 `bully` 做 WPS 攻击（默认用 `reaver`） | 换工具试试成功率 |
| `--reaver` | 用 `reaver` 做 WPS 攻击（默认） | — |
| `--ignore-locks` | AP 报告 WPS 锁定后**不停止** | ⚠️ 会被 AP 长时间拒绝；且**这是明显的暴力行为** |

### 4.5 PMKID 类

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `--pmkid` | **只用 PMKID 抓取**，不做 WPS/WPA 握手攻击 | ⭐ **对网络影响最小** |
| `--no-pmkid` | **不用** PMKID 抓取 | 目标 AP 不支持 PMKID 时减少无用尝试 |
| `--pmkid-timeout [sec]` | PMKID 抓取的等待时间（默认 300 秒） | 目标多时调小 |

### 4.6 命令类

| 参数 | 作用 |
| --- | --- |
| `--cracked` | 打印之前已破解的 AP 列表 |
| `--ignored` | 打印被忽略的 AP 列表 |
| `--check [file]` | 检查 `.cap` 文件（或 `hs/*.cap` 全部文件）里是否有 WPA 握手 |
| `--crack` | **显示破解某个已抓握手的命令**（不实际执行） |
| `--update-db` | 从 IEEE 注册处更新本地 MAC 前缀数据库 |

**`--check` 的实用价值**：跑完一轮后，用它检查 `hs/` 目录里到底有哪些抓包真的含握手：

```bash
sudo wifite --check
```

## 5. 实战演练

**环境声明**：以下全部在**你自己拥有的 Wi-Fi 网络与路由器**上执行，或隔离实验室、已授权目标。**`-p/--pillage` 与 deauth 会攻击视野内的所有网络——在居民区/办公区运行属于违法行为**。务必先读第 8 节的「避免误伤」小节。

### 场景 1：交互模式（推荐新手，最安全的用法）

**步骤 1：启动**

```bash
sudo wifite --wpa -pow 50 --nodeauths --daemon
```

逐个参数解释：

| 参数 | 作用 |
| --- | --- |
| `--wpa` | 只看 WPA/WPA2 |
| `-pow 50` | **只显示信号 ≥ 50 dBm 的网络** → 保证只针对近处的（通常是你自己的） |
| `--nodeauths` | **永不 deauth** → 对网络影响最小 |
| `--daemon` | 退出后自动把网卡恢复成托管模式 |

**步骤 2：看扫描界面**

```
  .;'                     `;,
 .;'  ,;'             `;,  `;,   WiFite v2.8.2
.;'  ,;'  ,;'     `;,  `;,  `;,
::   ::   :   ( )   :   ::   ::  automated wireless auditor
':.  ':.  ':. /_\ ,:'  ,:'  ,:'
 ':.  ':.    /___\    ,:'  ,:'   designed for Linux
  ':.       /_____\      ,:'
           /       \

 [+] Conflicting processes have been killed
 [+] enabling monitor mode on wlan0... done
 [+] initializing scan (wlan0mon), updates at 2 sec intervals, CTRL+C when ready.

  NUM  ESSID          CH  ENCR  POWER  WPS?  CLIENT
  ---  -------------  --  ----  -----  ----  ------
    1  lab-test        6  WPA2   62dB   yes   2
    2  home-guest     11  WPA2   38dB   no    1
```

| 列 | 含义 |
| --- | --- |
| `NUM` | 编号，稍后选择用 |
| `ESSID` | 网络名 |
| `CH` | 信道 |
| `ENCR` | 加密方式 |
| `POWER` | 信号强度 |
| `WPS?` | 是否开启 WPS（`yes` 表示可以尝试 WPS 攻击） |
| `CLIENT` | 关联的客户端数量（`0` 表示抓不到握手） |

**步骤 3：按 `Ctrl+C` 结束扫描**

```
 [+] select target(s) (1-2) separated by commas, dashes, or all [all]:
```

**提示输入目标编号**。

**步骤 4：输入目标**

```text
1
```

**步骤 5：观察自动攻击流程**

```
 [+] attacking lab-test (AA:BB:CC:DD:EE:FF)
 [+] PMKID attack on lab-test
 [+] sending association request...
 [+] PMKID capture succeeded!  ← 如果成功，到这里就直接进破解
     ↗ 或者
 [+] PMKID attack failed
 [+] starting WPA handshake capture
 [+] deauthing clients...  （--nodeauths 时跳过）
 [+] captured a handshake!
 [+] cracking with aircrack-ng
     using wordlist: /usr/share/dict/wordlist-probable.txt
 [+] cracked! key: labpassword123
```

**关键输出行解读**：

| 行 | 含义 |
| --- | --- |
| `PMKID capture succeeded` | ✅ 不需要客户端就拿到了可离线验证的数据 |
| `PMKID attack failed` | 该 AP 不在 RSN IE 里带 PMKID → 转去抓握手 |
| `captured a handshake!` | ✅ 抓到四次握手 |
| `cracked! key: ...` | ✅ **结果** |
| `not cracked` | 字典里没有 |

**步骤 6：退出并恢复**

`--daemon` 会自动恢复网卡。否则手工：

```bash
sudo airmon-ng stop wlan0mon
sudo systemctl restart NetworkManager
```

### 场景 2：只做 PMKID（对网络影响最小）

**这是最「温和」的攻击方式**：不需要客户端，不需要 deauth，对网络几乎无影响。

```bash
sudo wifite --pmkid --pmkid-timeout 120 --kill \
  --dict /usr/share/wordlists/rockyou.txt \
  --daemon
```

| 参数 | 作用 |
| --- | --- |
| `--pmkid` | 只用 PMKID |
| `--pmkid-timeout 120` | 每个目标等 120 秒 |
| `--kill` | 杀掉冲突进程 |
| `--dict` | 用 rockyou 破解 |
| `--daemon` | 退出恢复网卡 |

**预期输出**

```
 [+] attacking lab-test (AA:BB:CC:DD:EE:FF)
 [+] sending association request to lab-test
 [+] received PMKID! saving to hs/lab-test.pmkid
 [+] cracking PMKID with hashcat/aircrack-ng
 [+] cracked! key: labpassword123
```

### 场景 3：WPS 攻击（如果是自己的路由器）

**前提**：你**自己的路由器**开启了 WPS（很多家用路由器默认开启，这本身就是一个该修的配置问题）。

```bash
sudo wifite --wps-only --kill --daemon
```

**预期输出**

```
 [+] attacking lab-test (AA:BB:CC:DD:EE:FF)
 [+] WPS attack: Pixie-Dust
 [+] running reaver...
 [+] Pixie-Dust attack succeeded in 12 seconds!
 [+] WPS PIN: 12345670
 [+] WPA PSK: labpassword123
 [+] Access Point saved to wps/lab-test.wpc
```

**两种结果的解读**：

| 结果 | 含义 | 耗时 |
| --- | --- | --- |
| `Pixie-Dust attack succeeded` | ✅ AP 芯片有随机数缺陷，**直接算出 PIN 和 PSK** | 秒~分钟 |
| `Pixie-Dust attack failed` → 转 PIN 暴力 | AP 没有该缺陷，只能逐个试 PIN | 数小时，且可能被锁定 |

**关键结论**：**WPS 是家用网络中性价比最高的攻击面**。这就是为什么「关闭 WPS」是路由器加固的第一步。

### 场景 4：只抓包，用 hashcat 破解（GPU 加速）

wifite 的破解是 CPU（`aircrack-ng`）。要跑大字典，应该只抓包，再交给 [hashcat](../04-口令攻击/hashcat.md)。

**步骤 1：只抓不破**

```bash
sudo wifite --wpa --skip-crack --kill --daemon
```

**步骤 2：看抓到了什么**

```bash
ls -lh hs/
# -rw-r--r-- 1 root root 1.1M ... hs/lab-test_AA-BB-CC-DD-EE-FF.cap

# 用 wifite 自带的检查功能
sudo wifite --check
# 或直接看
aircrack-ng hs/lab-test_AA-BB-CC-DD-EE-FF.cap
```

**步骤 3：转成 hashcat 格式并破解**

```bash
hcxpcapngtool -o /tmp/wifi.22000 hs/*.cap
hashcat -m 22000 /tmp/wifi.22000 /usr/share/wordlists/rockyou.txt -O

# 结果
hashcat -m 22000 /tmp/wifi.22000 --show
```

**这条路径比 wifite 直接破解快 10~100 倍**（GPU vs CPU）——**这是 wifite 最正确的用法**。

### 场景 5：用 `-v` 学习底层命令（强烈推荐的学法）

`-v` 会**打印 wifite 实际执行的每条命令**。这是理解 [aircrack-ng](aircrack-ng.md) 套件工作原理的最佳途径。

```bash
sudo wifite --wpa -v --nodeauths
```

**预期输出（节选）**

```
 [+] running: airmon-ng check kill
 [+] running: airmon-ng start wlan0
 [+] running: airodump-ng --write /tmp/wifite-xxxx --output-format csv,pcap wlan0mon
 [+] running: airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w hs/lab-test wlan0mon
 [+] running: aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF wlan0mon
 [+] running: aircrack-ng -a 2 -b AA:BB:CC:DD:EE:FF -w /usr/share/dict/wordlist-probable.txt hs/lab-test.cap
```

**边看边对照本目录的其他教程**：每一条命令都能在 [airmon-ng](airmon-ng.md) / [airodump-ng](airodump-ng.md) / [aireplay-ng](aireplay-ng.md) / [aircrack-ng](aircrack-ng.md) 里找到完整解释。

**这是把「会用工具」变成「懂原理」的最快路径。**

## 6. 输出解读

### 扫描表

| 列 | 含义 | 判读 |
| --- | --- | --- |
| `NUM` | 目标编号 | 选择时用 |
| `ESSID` | 网络名 | `hidden` 表示隐藏 SSID |
| `CH` | 信道 | — |
| `ENCR` | 加密方式 | `WEP`=可快速破解；`WPA2`=可离线破解；`WPA3`=不可离线破解；`OPEN`=无加密 |
| `POWER` | 信号 | 越低（负得越多）越差 |
| `WPS?` | 是否开 WPS | `yes` = **最高价值目标** |
| `CLIENT` | 客户端数 | `0` = 无法抓握手（但 PMKID 仍可试） |

### 攻击流程的进度行

| 输出 | 含义 | 下一步 |
| --- | --- | --- |
| `enabling monitor mode on wlan0... done` | ✅ 监听模式已开 | — |
| `PMKID capture succeeded` | ✅ 拿到 PMKID | 直接进破解 |
| `PMKID attack failed` | AP 不带 PMKID | 转握手抓取 |
| `deauthing clients...` | 正在发 deauth | **注意：这会影响网络** |
| `captured a handshake!` | ✅ 抓到握手 | 进破解 |
| `cracked! key: XXXX` | ✅ **拿到口令** | 结束 |
| `not cracked` | 字典里没有 | 换字典，或用 hashcat |
| `No valid handshakes found` | 没抓到有效握手 | 见排错 |
| `target is WPA3` | WPA3（SAE） | **无法离线破解** |
| `WPS is locked` | AP 锁定了 WPS | `--ignore-locks` 可强攻，但会拖很久 |

### 输出文件

| 路径 | 内容 |
| --- | --- |
| `hs/` | 抓到的 `.cap` 与 `.pmkid` 文件 |
| `hs/*.cap` | 握手抓包（pcap） |
| `hs/*.pmkid` | PMKID |
| `wps/` | WPS 攻击结果（`.wpc` 文件） |
| `cracked.json` | **已破解的 AP 与口令**（JSON） |
| `wifi/` 或临时目录 | 中间文件 |

```bash
# 查看已破解的
sudo wifite --cracked

# 或直接看 JSON
cat cracked.json | python3 -m json.tool
```

**`cracked.json` 的结构**（简化）：

```json
[
  {
    "bssid": "AA:BB:CC:DD:EE:FF",
    "essid": "lab-test",
    "key": "labpassword123",
    "date": "2026-09-15 11:45:02"
  }
]
```

**判断成功**：`cracked! key: ...` 出现，或 `cracked.json` 里有记录。

**下一步**：

| 结果 | 动作 |
| --- | --- |
| 拿到口令 | 用 [aircrack-ng](aircrack-ng.md) 的 `airdecap-ng` 解密流量；在报告中记录口令强度问题 |
| 没破解出 | 换成 hashcat：`--skip-crack` 抓包 → `hcxpcapngtool` → hashcat |
| 目标是 WPA3 | 无法离线破解；检查是否为 WPA3/WPA2 混合模式 |
| WPS 开着但 PIN 攻不下 | 见 [reaver](reaver.md) 的排错小节 |

## 7. 与其他工具配合

```text
                     ┌────────── wifite（编排层）──────────┐
                     │                                    │
sudo wifite ────────►│  airmon-ng  → 切监听模式            │
                     │  airodump-ng → 扫描 + 抓包           │
                     │  aireplay-ng → deauth               │
                     │  reaver/bully → WPS                 │
                     │  aircrack-ng → CPU 破解              │
                     └────────────────────────────────────┘
                                    ↓ --skip-crack
                     ┌────────────────────────────────────┐
                     │  hcxpcapngtool → hashcat -m 22000  │
                     │         （GPU 破解，快 10~100×）     │
                     └────────────────────────────────────┘

[字典] cewl / crunch / wordlists
[替代方案] bettercap（模块化，更可控）
[WIDS]     kismet（蓝队视角）
```

| 组合 | 说明 |
| --- | --- |
| **wifite `-v` → [aircrack-ng](aircrack-ng.md) 系列** | **最佳学习路径**：看 wifite 打印的命令，去对应教程查细节 |
| **wifite `--skip-crack` → [hashcat](../04-口令攻击/hashcat.md)** | **最佳性能路径**：抓包用 wifite，破解用 GPU |
| **wifite → [cewl](../04-口令攻击/cewl.md)** | 用 CeWL 造组织相关字典喂给 `--dict` |
| **wifite → [wordlists](../04-口令攻击/wordlists.md)** | 换掉那个很小的默认字典 |
| **[reaver](reaver.md)** | wifite 的 `--wps-only` 就是调它。想精细控制 WPS 攻击就直接用 reaver |
| **[bettercap](bettercap.md)** | 想做更灵活的攻击组合（不只是抓包破解）时用它 |
| **[kismet](kismet.md)** | 蓝队：检测 wifite 产生的 deauth 与探测行为 |

**一个重要的提醒**：wifite 会**自动保存解析出的凭证到 `cracked.json`**。在授权的渗透测试中，**这些数据属于客户的敏感数据**，必须按 ROE 的要求处理（加密存储、规定期限内删除）。不要留在个人机器上。

## 8. 常见坑与排错

### 8.1 避免误伤（最重要的一节）

| 坑 | 后果 | 解决 |
| --- | --- | --- |
| **用 `-p/--pillage` 在居民区/办公区跑** | **攻击了邻居/同事的网络——违法** | ⭐ 只在隔离环境用；或**坚决不加 `-p`**（用交互模式逐个确认） |
| 忘了加 `-pow` / 没限制目标 | 攻击范围不可控 | 加 `-pow 50`（只看强信号）；用交互模式手工选目标 |
| `-inf` 无人值守跑整晚 | 攻击了视野内所有新出现的网络 | 不要这样做 |
| 没加 `--nodeauths` | 会自动 deauth 客户端 → 中断他人连接 | ⭐ **加上 `--nodeauths`**；优先用 `--pmkid` |
| 忘了加 `--daemon` | 退出后网卡停留在监听模式，无法上网 | 加 `--daemon`；或手工 `airmon-ng stop` |

**一句话原则**：

> **在开始前，先确认你视野内的每一个 AP 都是你的，或者都已授权。**
> 做不到，就**不要用自动模式**，改用交互模式并手工核对每个目标。

### 8.2 技术排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `wifite: command not found` | 未安装 | `sudo apt install wifite` |
| `No wireless interfaces found` | 网卡未识别 / 不支持监听 | 见 [airmon-ng](airmon-ng.md) 的排错 |
| 一直卡在扫描界面 | 交互模式需要你按 `Ctrl+C` | 按 `Ctrl+C` 进入选择阶段 |
| 目标列表是空的 | 没发现任何网络 | 检查网卡是否真的在监听；检查 `-c` 信道限制是否过窄 |
| 目标全被跳过 | wifite 认为不支持攻击 | 可能是 WPA3 或隐藏 SSID；用 `-v` 看原因 |
| `PMKID attack failed` 所有目标 | 目标 AP 都不带 PMKID | 正常；wfite 会转去抓握手 |
| `captured a handshake!` 但立刻 `not cracked` | **默认字典太小** | ⭐ `--dict /usr/share/wordlists/rockyou.txt` |
| WPS 攻击一直重试 | AP 有 WPS 锁定 | 换目标；或 `--ignore-locks`（会拖很久） |
| `WPS is locked` | AP 被锁 | 等锁定期结束（通常几分钟到几小时） |
| 抓不到握手 | 没有客户端 / 目标有 PMF / 信道问题 | `--clients-only` 筛出有客户端的；目标有 PMF 时 deauth 无效 |
| 破解很慢 | wifite 用 `aircrack-ng`（CPU） | `--skip-crack` 抓包 → hashcat GPU |
| 退出后上不了网 | 监听模式未恢复 | `sudo airmon-ng stop wlan0mon && sudo systemctl restart NetworkManager`；下次加 `--daemon` |
| `-h` 输出不完整 | 需要加 `-v` | `wifite -h -v` |
| 虚拟机里不工作 | USB 直通 | 用物理机 + USB 网卡 |
| 攻击后自己断网 | deauth 影响到了自己（你的设备也在目标网络上） | **正常**：你把自己的设备也踢了。这也是为什么要在实验专用网络上操作 |

### 8.3 一个实际会遇到的尴尬场景

**场景**：你在自己的笔记本上跑 wifite 攻击自己的路由器，结果笔记本自己掉线了。

**原因**：`aireplay-ng --deauth` 是广播/定向的，如果你的笔记本也连在这个网络上，它**也被踢了**。

**解决**：

```bash
# 1) 用另一个设备连 Wi-Fi（不是跑 wifite 的那台）
# 2) 或者只扫描不 deauth
sudo wifite --wpa --pmkid --nodeauths
# 3) 或者用网线连接 Kali，只用无线网卡做攻击
```

**这个体验其实很有教育意义**——它直观地展示了 deauth 的破坏性。想象一下在真实网络中这会造成什么后果。

## 9. 防御视角（蓝队）

wifite 本身没有新技术，它是**已有攻击的自动化**。所以蓝队的对策与 [aireplay-ng](aireplay-ng.md) / [airodump-ng](airodump-ng.md) 一致，但有一点需要强调：

### 9.1 wifite 的自动化特征

| 特征 | 说明 | 检测 |
| --- | --- | --- |
| 行为连贯且快速 | 扫描 → 攻击 → 破解一气呵成，缺少人工停顿 | 时序分析：**deauth 紧跟在扫描之后** |
| 系统性遍历 | 会依次尝试 PMKID → WPS → 握手 | 同一 BSSID 短时间内遭受多种攻击 |
| 使用默认参数 | 例如固定的字典、固定的 deauth 数量 | 流量特征匹配（但攻击者可改） |
| **默认 reason code 7** | `aireplay-ng` 的默认值 | reason code 分布检测 |
| PMKID 探测 | 发送关联请求后立即断开 | AP 日志异常 |

### 9.2 缓解措施

| 措施 | 对 wifite 的效果 |
| --- | --- |
| **WPA3-SAE（纯 WPA3）** | ✅ **让 WPS/PMKID/握手三条路全部失效** |
| **关闭 WPS** | ✅ 消除 wifite 最高性价比的攻击路径 |
| **802.11w / PMF** | ✅ 阻断 deauth |
| **长随机 PSK（≥ 20 位）** | ✅ 让破解在时间上不可行 |
| MAC 随机化（客户端侧） | 减少客户端追踪 |
| 降低发射功率 | 缩小可被扫描的范围 |

**关键洞察**：

> **wifite 的行为清单，正好就是一份路由器加固清单。**
>
> wifite 会尝试：PMKID → WPS → 握手 → 字典破解 → deauth
>
> 那么对应的加固就是：**WPA3 + 关闭 WPS + PMF + 长 PSK**。
>
> 只要这四项做到，wifite（以及它调用的所有底层工具）就**完全无从下手**。

### 9.3 检测规则

```text
# 规则 1：系统性攻击（wifite 的签名行为）
if count(deauth, bssid=X, 5m) > 0
   and count(assoc_requests, bssid=X, 5m) > 20
   and count(distinct attack_types, bssid=X, 5m) > 1
then alert "systematic wireless attack against BSSID X (likely automated)"

# 规则 2：PMKID 探测
if count(assoc_requests, 60s) > 50 and count(data_frames, 60s) < 5
then alert "possible PMKID harvesting"

# 规则 3：WPS 暴力
if count(wps_m4_messages, 60s) > 30
then alert "possible WPS brute-force"

# 规则 4：deauth 洪泛（见 aireplay-ng）
if count(deauth_frames, 10s) > 20
then alert "possible deauth flood"
```

**推荐工具**：[kismet](kismet.md)（自带 WIDS 与告警）、企业 AP 控制器的 WIPS 功能。

### 9.4 一个容易被忽略的运营视角

**wifite 会写 `cracked.json`。** 在授权的渗透测试中：

| 事项 | 要求 |
| --- | --- |
| 数据分类 | 无线凭据是**敏感数据**，按客户的数据分类标准处理 |
| 存储 | 加密存储；不放在个人设备上 |
| 删除 | 项目结束后按 ROE 规定的期限删除 |
| 传输 | 不通过未加密渠道发送 |
| 记录 | 保留操作日志以备审计 |

**这也是蓝队/合规视角需要知道的事**：即使攻击是授权的，**数据处理不当仍然违规**。

## 10. 参考

- 官方仓库：<https://github.com/kimocoder/wifite2>
- Kali 工具页：<https://www.kali.org/tools/wifite/>
- 本机帮助：`wifite -h`（简短）、**`wifite -h -v`（完整）**
- 相关本目录：[aircrack-ng](aircrack-ng.md)（套件总览）、[airmon-ng](airmon-ng.md)、[airodump-ng](airodump-ng.md)、[aireplay-ng](aireplay-ng.md)、[reaver](reaver.md)、[kismet](kismet.md)、[bettercap](bettercap.md)
- 相关其他目录：[hashcat](../04-口令攻击/hashcat.md)、[wordlists](../04-口令攻击/wordlists.md)、[cewl](../04-口令攻击/cewl.md)

## ⚠️ 法律与伦理

**wifite 是本目录中法律风险最高的工具**，原因不在于它的技术，而在于**它把攻击自动化了**：

1. **`-p/--pillage` 会自动攻击视野内的所有网络**——在居民区或办公区运行，会导致你**在不知情的情况下攻击了邻居和同事的网络**。「我不知道它打的是别人」**不是抗辩理由**；
2. **默认会自动 deauth**——这在多数司法辖区构成**干扰通信**；
3. **它是「一键式」的**——降低了攻击门槛，也降低了使用者的谨慎程度；
4. **它会自动保存破解出的凭据**——涉及数据处理的合规问题。

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十六条 | **破坏计算机信息系统罪** —— deauth 造成网络中断 |
| 《刑法》 | 第二百八十五条 | 非法侵入计算机信息系统；非法获取计算机信息系统数据 |
| 《无线电管理条例》 | 相关条款 | 擅自使用无线电频率、干扰合法无线电业务 |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《个人信息保护法》 | 相关条款 | 截获通信内容、破解凭据涉及个人信息处理 |

**本教程仅适用于**：

- ✅ **你自己拥有的 Wi-Fi 网络与你自己的路由器**
- ✅ 有**书面授权**、明确列出授权 SSID、时间窗**以及允许的干扰行为**的无线渗透测试
- ✅ 你自己搭建的隔离无线实验室
- ✅ 授权的 CTF 靶场

**使用前的强制检查清单**：

```text
[ ] 我视野内的每一个 AP 都是我的，或者都已获得书面授权？
[ ] 我已经加上了 --nodeauths（或至少不用 -p 自动模式）？
[ ] 我已经用 -pow 限制了信号强度（只针对近处的自己网络）？
[ ] 我知道 --daemon 会在退出后恢复网卡？
[ ] 我了解 cracked.json 里的数据需要按合规要求处理？
```

**任何一项打不上勾，就不要运行自动模式。**

**最安全的学习方式**：用 `-v` 参数观察 wifite 打印的底层命令，然后**手工执行那些命令**（在你自己网络上），配合本目录 [airmon-ng](airmon-ng.md) / [airodump-ng](airodump-ng.md) / [aireplay-ng](aireplay-ng.md) 的教程理解每一步。这样你既能学到东西，又完全掌控了攻击的范围。
