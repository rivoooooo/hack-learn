# cowpatty（WPA/WPA2-PSK 离线字典攻击）

> **一句话**：拿到一个包含 **WPA/WPA2 四次握手**的抓包文件 + 一个字典 + 正确的 SSID，就能在本地离线逐一验证候选口令——**每一次猜测都在你自己的 CPU 上完成，不向目标 AP 发一个包**。
> **分类**：口令攻击 / 无线凭据离线破解 ｜ **Kali 包**：`cowpatty`（命令 `cowpatty`、`genpmk`）｜ **官方文档**：<https://www.kali.org/tools/cowpatty/> ｜ 上游：<https://www.willhackforsushi.com/?page_id=50>

---

## 1. 它解决什么问题

WPA2-PSK 的安全性**完全取决于口令强度**。协议本身没有可破解的密码学缺陷（四次握手是安全的），所以攻击面只剩一个：**口令太弱**。

于是攻击流程是：

```
① 抓到一次完整的四次握手（= 拿到验证口令所需的全部材料）
              ↓
② 离线拿字典逐个尝试候选口令
              ↓
③ 口令对 → 算出正确的 PMK → 握手校验通过 → 口令就是它
```

**关键点：第 ② 步完全离线**。这意味着：

- **不向 AP 发包**（不会被 IDS/WIPS 抓到「在爆破」）；
- **速度只受自己 CPU/GPU 限制**（可以慢慢跑几天）；
- **怎么测都行**（不需要目标在线）。

**cowpatty 在这个链条里的位置**：它是**最经典的 WPA 字典攻击实现之一**（作者 Joshua Wright），特点是**简单、直白、结果清晰**，并且有一个「加速器」`genpmk`。

**对比同类**：

| 工具 | 定位 | 差异 |
|------|------|------|
| **cowpatty** | **WPA-PSK 字典攻击** | 最直白的实现；有 `genpmk` 预计算（**PMK 预计算对同一 SSID 的多次破解有用**） |
| **aircrack-ng** | 无线全家桶（抓包 + 破解） | **功能覆盖面最广**，是标准工作流；破解部分与 cowpatty 同类。见 [`../05-无线攻击/aircrack-ng.md`](../05-无线攻击/aircrack-ng.md) |
| **hashcat** | **GPU 通用 hash 破解** | 支持 WPA（`-m 22000`），**速度碾压 CPU 工具**（单卡可达百万级/秒）。**现代首选**。见 [`hashcat.md`](hashcat.md) |
| **john** | CPU hash 破解 | 也支持 WPA（`--format=wpapsk`）。见 [`john.md`](john.md) |
| **wifite / bettercap** | 自动化编排 | 把「扫描→抓握手→破解」串起来。见 [`../05-无线攻击/wifite.md`](../05-无线攻击/wifite.md)、[`../05-无线攻击/bettercap.md`](../05-无线攻击/bettercap.md) |

**选型建议（2026 年的现实）**：

- **有 GPU** → 用 **hashcat**（`-m 22000`）。cowpatty 的 CPU 速度在弱口令以外基本不够用；
- **只有 CPU、字典小、想快速验证** → cowpatty 很合适（输出直观、依赖少）；
- **需要「同一 SSID 反复测多个抓包」** → `genpmk` 的 PMK 预计算能显著加速；
- **学习协议原理** → cowpatty 是最好的教具（`-c` 还能先「只检查握手是否完整」）。

---

## 2. 工作原理

先看 WPA2-PSK 的密钥派生链（**这是理解「为什么字典攻击成立」「为什么加盐让它失效」的关键**）：

```
   口令 passphrase（人输入的，8-63 字符）
        │
        │  ① PBKDF2-HMAC-SHA1
        │     PMK = PBKDF2(passphrase, SSID, 4096 次迭代, 256 bit)
        │     ⚠️ 注意：salt 是【SSID】，而且固定迭代 4096 次
        ▼
      PMK（256 bit，Pairwise Master Key）
        │
        │  ② 四次握手中交换的 nonce（ANonce / SNonce）+ MAC 地址
        │     PTK = PRF(PMK, "Pairwise key expansion", min(AA,SPA)||max(AA,SPA)||min(ANonce,SNonce)||max(ANonce,SNonce))
        ▼
      PTK（Pairwise Transient Key）
        │
        │  ③ 从 PTK 里切出 KCK（Key Confirmation Key）
        ▼
      MIC = HMAC(KCK, 握手消息的某些字段)      ← 握手消息里就带着这个 MIC
```

**破解的全部逻辑就藏在这条链里**：

```
候选口令 p
   │
   ├─ PMK' = PBKDF2(p, SSID, 4096, 256)          ← ① 最贵的一步
   │
   ├─ PTK' = PRF(PMK', nonce, MAC)               ← ② 便宜
   │
   ├─ MIC' = HMAC(KCK', 握手消息)                ← ③ 便宜
   │
   └─ MIC' == 抓包里的 MIC ?  → 相等则 p 就是口令
```

**三个关键结论**：

**① 为什么「加盐」能让彩虹表失效**

PBKDF2 的 salt 是 **SSID**。也就是说：**同一个口令在不同 SSID 下会算出完全不同的 PMK**。

```
口令 "12345678"
    在 SSID "HomeWiFi"   下 → PMK_A
    在 SSID "CompanyWiFi" 下 → PMK_B     ← 完全不同
```

所以：

- **经典彩虹表（预先算好 hash→明文）在这里失效**——因为没有固定 salt，你得为**每一个 SSID**各建一套表；
- 但**「针对某个特定 SSID 预计算」依然有意义**（这就是 `genpmk` 干的事）：同一区域若有多个 AP 共用同一个 SSID（常见：连锁店、企业多 AP、`NETGEAR`/`TP-LINK` 默认名），**一次预计算可复用多次**。

**② 为什么 `genpmk` 的预计算有意义**

`PBKDF2` 4096 次迭代是**整个流程里唯一昂贵的一步**（② ③ 只是几次 HMAC）。`genpmk` 做的事就是**把「字典 → PMK」这一步提前算完并落盘**：

```
字典（明文口令列表） ──[PBKDF2 4096]──► hashfile（口令 → PMK 映射）
                                            │
                        cowpatty -d hashfile 时只做 ②③（极快）
```

**代价**：hashfile 只对**那一个 SSID** 有效。换算下来：

| | 不预计算（`-f`） | 预计算（`-d`） |
|---|---|---|
| 每候选口令成本 | 完整 PBKDF2 + ②③ | 只做 ②③ |
| 速度 | 慢（PBKDF2 主导） | **快很多** |
| 存储 | 无额外 | hashfile（**通常比字典大得多**） |
| 适用 | 一次性破解 | **同一 SSID 反复破解** |

> **PMKID 攻击的补充**：除四次握手外，2018 年 Jens Steube 发现的 **PMKID 攻击**（从 AP 的第一个 EAPOL 消息里直接拿到可离线验证的 PMKID，**不需要抓到完整四次握手，也不需要客户端**）已成为现代首选。`hashcat -m 22000` 同时支持 **EAPOL 握手** 与 **PMKID**。cowpatty 只处理**四次握手抓包**。

**③ cowpatty 的输入与输出**

```
输入：
  -r capture.pcap    libpcap 格式、含四次握手的抓包
  -s "SSID"          网络名（必须完全一致，包括大小写/空格）
  -f dictionary      字典（明文口令，每行一个）
  -d hashfile        genpmk 生成的预计算文件（与 -f 二选一）

可选：
  -c                 只检查抓包里有没有有效的四次握手（不破解）
  -v                 详细输出（可叠加，越多越详细）

输出：
  "The PSK is \"xxxx\"."     ← 命中
  或 "Passphrase not in dictionary" / 无输出   ← 未命中
```

`cowpatty` 会先**解析抓包、验证四次握手的完整性**（能从中恢复出 ANonce/SNonce/MAC/MIC），再开始逐口令验证。**如果握手不完整，它会直接告诉你数据不足**——这正是 `-c` 的用途。

---

## 3. 安装与快速上手

```bash
sudo apt install cowpatty
command -v cowpatty genpmk
cowpatty -V
```

```console
root@kali:~# cowpatty -V
cowpatty 4.8 - WPA-PSK dictionary attack. <jwright@hasborg.com>
```

```bash
cowpatty -h
```

```console
root@kali:~# cowpatty -h
cowpatty 4.8 - WPA-PSK dictionary attack. <jwright@hasborg.com>

Usage: cowpatty [options]

	-f 	Dictionary file
	-d 	Hash file (genpmk)
	-r 	Packet capture file
	-s 	Network SSID (enclose in quotes if SSID includes spaces)
	-c 	Check for valid 4-way frames, does not crack
	-h 	Print this help information and exit
	-v 	Print verbose information (more -v for more verbosity)
	-V 	Print program version and exit
```

```bash
genpmk -h
```

```console
root@kali:~# genpmk -h
genpmk 1.3 - WPA-PSK precomputation attack. <jwright@hasborg.com>
Usage: genpmk [options]

	-f 	Dictionary file
	-d 	Output hash file
	-s 	Network SSID
	-h 	Print this help information and exit
	-v 	Print verbose information (more -v for more verbosity)
	-V 	Print program version and exit

After precomputing the hash file, run cowpatty with the -d argument.
```

**官方示例（来自 Kali 工具页）**：

```console
# ① 预计算
root@kali:~# genpmk -f /usr/share/wordlists/nmap.lst -d cowpatty_dict -s securenet
genpmk 1.3 - WPA-PSK precomputation attack. <jwright@hasborg.com>
File cowpatty_dict does not exist, creating.
key no. 1000: pinkgirl
1641 passphrases tested in 3.60 seconds: 456.00 passphrases/second
```

```console
# ② 用预计算结果破解
root@kali:~# cowpatty -d cowpatty_dict -r Kismet-20181113-13-37-00-1.pcapdump -s 6F36E6
cowpatty 4.8 - WPA-PSK dictionary attack. <jwright@hasborg.com>

Collected all necessary data to mount crack against WPA2/PSK passphrase.
Starting dictionary attack. Please be patient.

The PSK is "12345678".

5 passphrases tested in 0.00 seconds: 50000.00 passphrases/second
```

**最小可用（不预计算，直接打）**：

```bash
cowpatty -f /usr/share/wordlists/rockyou.txt -r handshake.pcap -s "MyNetwork"
```

> ⚠️ **`rockyou.txt` 在 Kali 里是压缩的**（`/usr/share/wordlists/rockyou.txt.gz`）。**必须先解压**，否则 cowpatty 会把 gz 二进制当字典读，永远不命中：
> ```bash
> sudo gunzip -k /usr/share/wordlists/rockyou.txt.gz
> ```

---

## 4. 核心参数详解

> 全部取自上面的 `cowpatty -h` / `genpmk -h` 原文。

### 4.1 cowpatty

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-r <file>` | **抓包文件**（libpcap 格式，含四次握手） | 必需。格式支持 `.pcap`/`.cap`/`.pcapdump`（Kismet/airodump-ng 产物） |
| `-s "<SSID>"` | **网络名** | 必需。**必须与目标 SSID 完全一致**（大小写、空格、隐藏 SSID 尤其注意）。**SSID 含空格必须加引号** |
| `-f <file>` | **字典文件**（明文口令，每行一个） | 与 `-d` 二选一；**必须先解压 `.gz`** |
| `-d <file>` | **genpmk 生成的 hashfile** | 与 `-f` 二选一；**更快**，但只对生成时的那个 SSID 有效 |
| `-c` | **只检查四次握手是否有效，不破解** | **拿到抓包后的第一步**——先确认「材料够不够」，省得白跑几小时 |
| `-v` | 详细输出（`-v -v` 更详细） | 排错、想看到进度时用 |
| `-h` | 打印帮助 | —— |
| `-V` | 打印版本 | —— |

**`-f` 与 `-d` 不能同时用**（逻辑上互斥）。同时给的行为未定义，**不要这么用**。

### 4.2 genpmk

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-f <file>` | **输入字典** | 必需；建议先按 SSID 相关的密码规律裁剪字典（提高命中率） |
| `-d <file>` | **输出 hashfile** | 必需；**文件不存在时会自动创建**（输出会提示 `File ... does not exist, creating.`） |
| `-s "<SSID>"` | **目标 SSID** | 必需；**决定了这个 hashfile 能用在哪** |
| `-v` | 详细输出 | —— |
| `-h` / `-V` | 帮助 / 版本 | —— |

**输出内容解读**：

```
key no. 1000: pinkgirl                              ← 每 1000 个口令打印一次进度（含口令样本）
1641 passphrases tested in 3.60 seconds: 456.00 passphrases/second
      │                        │              │
      │                        │              └─ 预计算速率（受 CPU 限制，纯单线程 PBKDF2）
      │                        └─ 耗时
      └─ 字典里的条目数
```

**预估磁盘占用**：hashfile 里每个条目是「口令 + 32 字节 PMK」，加上结构化存储开销。**一个百万条字典生成的 hashfile 通常在几十到上百 MB 量级**——生成前先看磁盘空间。

### 4.3 与 WPA 相关的辅助工具（同一条工作流）

| 工具 | 用途 | 教程 |
|------|------|------|
| `airmon-ng` | 把网卡切到监听模式 | [`../05-无线攻击/airmon-ng.md`](../05-无线攻击/airmon-ng.md) |
| `airodump-ng` | **抓四次握手**（`--bssid` + `-c` + `-w`） | [`../05-无线攻击/airodump-ng.md`](../05-无线攻击/airodump-ng.md) |
| `aireplay-ng` | **发 deauth 逼客户端重连**（触发新握手） | [`../05-无线攻击/aireplay-ng.md`](../05-无线攻击/aireplay-ng.md) |
| `aircrack-ng` | 同类字典攻击（也能验证握手） | [`../05-无线攻击/aircrack-ng.md`](../05-无线攻击/aircrack-ng.md) |
| `hashcat` / `john` | GPU / CPU 通用破解（支持 WPA + PMKID） | [`hashcat.md`](hashcat.md)、[`john.md`](john.md) |
| `wifite` | 自动化整条链 | [`../05-无线攻击/wifite.md`](../05-无线攻击/wifite.md) |
| `coWPAtty` | 本工具 | —— |

---

## 5. 实战演练

> **环境声明**：**这是本教程法律风险最高的一篇，请务必读完。**
> - **必须是你自己的 AP**，或**获得书面授权**的目标（如企业无线安全评估项目、CTF 无线赛题、你自己家里的路由器）；
> - **测试过程会向目标 AP 发送 deauth 帧（解除认证），会短暂中断该网络所有用户的连接**——在别人的网络上这属于**干扰通信**，是明确违法的；
> - **绝对不要**在公共场所（商场、机场、写字楼、邻居家、酒店）做扫描、抓包、deauth；
> - 本教程的所有命令**只应针对你自己的测试 AP**；
> - 建议用**自己买的一台旧路由器 + 一台测试客户端**搭一个独立实验室。

### 场景 0：搭一个属于你自己的无线试验台（**强烈建议先做这一步**）

```text
┌─────────────────────────┐        ┌──────────────────────────┐
│ 测试 AP（你自己的路由器）│        │ Kali（虚拟机 + USB 网卡） │
│  SSID: WPA-LAB           │◄──────►│ wlan0（监听）             │
│  PSK : 12345678          │  2.4G  │ eth0（上网/可选）         │
└─────────────────────────┘        └──────────────────────────┘
        ▲
        │ 一台测试客户端（手机/另一台电脑）连上去产生流量
```

**要点**：

1. **AP 用你自己的**（老路由器刷 OpenWrt，或直接用路由器的访客网络）；
2. **把 AP 的 PSK 设为一个「你知道答案」的弱口令**（如 `12345678`）——这样你才能验证工具「真的能破出来」；
3. **Kali 需要一个支持监听模式的 USB 无线网卡**（虚拟机要能直通 USB）；
4. **在一个不会有别人 Wi-Fi 的环境**（或至少确认你只操作自己 AP 的 BSSID）；
5. 全程用 **BSSID 精确锁定**自己的 AP（`--bssid`），避免误伤邻居的网络。

### 场景 1：抓握手 → 检查握手 → 字典破解

**1a. 抓一个四次握手**（流程细节见 [`../05-无线攻击/airodump-ng.md`](../05-无线攻击/airodump-ng.md)）

```bash
# ① 网卡进监听模式
sudo airmon-ng start wlan0
iwconfig                     # 确认出现 wlan0mon

# ② 锁定自己的 AP 抓包（-c 是信道，--bssid 是自己的 AP）
sudo airodump-ng wlan0mon                                   # 先找到自己的 BSSID 与信道
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w /tmp/lab wlan0mon
```

```console
# airodump-ng 顶部出现关键提示：
BSSID              PWR  Beacons  #Data  CH  ENC   CIPHER  AUTH  ESSID
AA:BB:CC:DD:EE:FF  -42      120     18   6  WPA2  CCMP    PSK   WPA-LAB

# 抓到手时（右上角）：
CH  6 ][ Elapsed: 2 mins ][ 2026-09-15 10:30 ][ WPA handshake: AA:BB:CC:DD:EE:FF
```

**1b. 强制客户端重连以拿到握手**（**只对自己的 AP**）

```bash
# 开第三个终端，向「自己的 AP」发 2 个 deauth 帧
sudo aireplay-ng --deauth 2 -a AA:BB:CC:DD:EE:FF wlan0mon
```

**解读**：`--deauth 2` 让 AP 把已连接的客户端踢下线，客户端会自动重连——**重连过程中就会产生新的四次握手**。`airodump-ng` 右上角出现 `WPA handshake: <BSSID>` 就说明抓到了。

> **这一步就是「干扰通信」**。在你自己的实验室里无所谓；**在别人的网络上这是违法且会造成他人断网**。

**1c. 先检查握手是否完整（`-c`）**

```bash
cowpatty -c -r /tmp/lab-01.cap -s "WPA-LAB"
```

```console
root@kali:~# cowpatty -c -r /tmp/lab-01.cap -s "WPA-LAB"
cowpatty 4.8 - WPA-PSK dictionary attack. <jwright@hasborg.com>

Collected all necessary data to mount crack against WPA2/PSK passphrase.
```

```console
# 数据不足时（握手不完整 / SSID 写错）：
Could not retrieve necessary data from the capture file.
Ensure you have captured all four EAPoL frames and specified the correct SSID
```

**解读**：`-c` 是**必做的第一步**。它回答两个问题：

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `Collected all necessary data...` | **材料齐了**（ANonce/SNonce/MAC/MIC 都拿到了） | 可以开始破解 |
| `Could not retrieve necessary data...` | 材料不全 | 继续抓（可能是缺一个 EAPOL 帧）；**核对 SSID 是否完全一致** |

**注意**：`-c` **也会打印 EAPOL/MAC 等详细信息**（配合 `-v` 更多）——这是排查「为什么抓不到」的好工具。

**1d. 直接字典破解（不预计算）**

```bash
# 先准备一个小字典做首次验证（含正确答案 12345678）
cat > /tmp/lab-dict.txt <<'EOF'
password
123456
12345678
admin
qwerty
WPA-LAB
EOF

cowpatty -f /tmp/lab-dict.txt -r /tmp/lab-01.cap -s "WPA-LAB"
```

```console
root@kali:~# cowpatty -f /tmp/lab-dict.txt -r /tmp/lab-01.cap -s "WPA-LAB"
cowpatty 4.8 - WPA-PSK dictionary attack. <jwright@hasborg.com>

Collected all necessary data to mount crack against WPA2/PSK passphrase.
Starting dictionary attack. Please be patient.

The PSK is "12345678".

6 passphrases tested in 0.01 seconds: 600.00 passphrases/second
```

**解读**：

| 输出 | 含义 |
|------|------|
| `Collected all necessary data...` | 握手有效 |
| `The PSK is "..."` | **命中**，引号里就是口令 |
| `N passphrases tested in T seconds: R passphrases/second` | **本次的实际速率**——**用它估算大字典要跑多久** |
| （无 `The PSK is`，直接结束） | **字典里没有正确口令**（未命中） |

**用 rockyou 跑一次真实规模**（先解压！）：

```bash
sudo gunzip -k /usr/share/wordlists/rockyou.txt.gz
wc -l /usr/share/wordlists/rockyou.txt
# 先只取前 10 万条做「时间估算」
head -n 100000 /usr/share/wordlists/rockyou.txt > /tmp/rockyou-100k.txt

time cowpatty -f /tmp/rockyou-100k.txt -r /tmp/lab-01.cap -s "WPA-LAB"
```

```console
# 典型的 CPU 速率：几百 ~ 几千 passphrase/second（取决于 CPU 与实现）
# 于是：100 万条字典 ≈ 几分钟到几十分钟；完整 rockyou（1400 万条）≈ 数小时到一天
```

**这条速度曲线是理解「为什么现在都用 GPU」的关键**：

| 平台 | 典型 WPA 速率 | 1400 万条 rockyou 耗时（估算） |
|------|---------------|-------------------------------|
| **cowpatty（单 CPU 核）** | 数百 ~ 数千 /秒 | **数小时 ~ 一天以上** |
| **hashcat + 中端 GPU** | **数十万 ~ 数百万 /秒** | **几十秒 ~ 几分钟** |

→ **真实项目请用 [`hashcat.md`](hashcat.md)（`-m 22000`）**。cowpatty 的价值在于**教学、快速验证、以及无 GPU 的轻量场景**。

### 场景 2：`genpmk` 预计算加速（同一 SSID 的重复破解）

**什么时候值得预计算**：

- 你要对**同一个 SSID** 的**多个抓包**反复尝试（例如企业有 20 个 AP 都叫 `CompanyWiFi`，抓到 10 个不同的握手）；
- 你要用**不同的字典**对同一 SSID 反复测试（先小字典试，不行再换大的）。

**2a. 生成 hashfile**

```bash
genpmk -f /tmp/lab-dict.txt -d /tmp/lab.hash -s "WPA-LAB"
```

```console
root@kali:~# genpmk -f /tmp/lab-dict.txt -d /tmp/lab.hash -s "WPA-LAB"
genpmk 1.3 - WPA-PSK precomputation attack. <jwright@hasborg.com>
File /tmp/lab.hash does not exist, creating.
6 passphrases tested in 0.01 seconds: 600.00 passphrases/second
ls -l /tmp/lab.hash
```

```console
# 用大字典时能看到进度（官方示例格式）：
key no. 1000: pinkgirl
1641 passphrases tested in 3.60 seconds: 456.00 passphrases/second
```

**2b. 用 hashfile 破解（对比速度）**

```bash
time cowpatty -d /tmp/lab.hash -r /tmp/lab-01.cap -s "WPA-LAB"
```

```console
root@kali:~# time cowpatty -d /tmp/lab.hash -r /tmp/lab-01.cap -s "WPA-LAB"
cowpatty 4.8 - WPA-PSK dictionary attack. <jwright@hasborg.com>

Collected all necessary data to mount crack against WPA2/PSK passphrase.
Starting dictionary attack. Please be patient.

The PSK is "12345678".

50 passphrases tested in 0.00 seconds: 50000.00 passphrases/second

real	0m0.003s
```

**解读（速度对比是本节的重点）**：

| 方式 | 本例速率（官方示例值） | 为什么 |
|------|------------------------|--------|
| `-f dict`（每次现算 PBKDF2） | 456 口令/秒 | 每个候选都要跑 **4096 次迭代的 PBKDF2** |
| `-d hash`（预计算） | **50000 口令/秒** | 只做 HMAC 验证，**PBKDF2 已经提前算完了** |

→ **快约 100 倍**。但代价是：

| 代价 | 说明 |
|------|------|
| **hashfile 只对一个 SSID 有效** | SSID 变了，PMK 全错，必须重新 `genpmk` |
| **磁盘占用** | 通常比原字典大不少 |
| **生成本身要花时间** | 生成的总时间 ≈ 直接破解的时间（因为贵的那步一样要做） |

**所以预计算的正确用法是**：「**这份字典 × 这个 SSID** 会被反复用」时才值得。用一次就扔掉的话，直接 `-f` 反而更快。

**2c. SSID 对结果的影响（亲手验证「加盐」的意义）**

```bash
# 用「错误的 SSID」跑同一个抓包
cowpatty -f /tmp/lab-dict.txt -r /tmp/lab-01.cap -s "WPA-LAB-WRONG"
```

```console
Collected all necessary data to mount crack against WPA2/PSK passphrase.
Starting dictionary attack. Please be patient.

Could not find a matching PSK in the specified dictionary.
```

**解读**：**字典里明明有 `12345678`，但 SSID 写错就破不出来**。原因就是 **SSID 是 PBKDF2 的 salt**：

```
PBKDF2("12345678", "WPA-LAB",       4096) → PMK 匹配   ✅
PBKDF2("12345678", "WPA-LAB-WRONG", 4096) → PMK 不匹配 ❌
```

**这就是「为什么不能给 WPA2-PSK 建通用彩虹表」的直接演示**，也是 `-s` 必须**完全精确**（包括大小写、空格、隐藏 SSID 的真实值）的原因。

> **隐藏 SSID 怎么办**：`airodump-ng` 在抓到与该 AP 关联的客户端时能恢复出真实 SSID；或从探测请求/关联请求里获取。**总之必须拿到准确的 SSID**。

### 场景 3：字典策略 + 与 hashcat 对比 + 「破不出来」的正确结论

**3a. 用「定向字典」提高命中率**（比无脑堆大字典有效得多）

```bash
# 思路：把口令限制在「该场景最可能的形态」上
#  - 该地区的手机号（11 位）
#  - 常见弱口令 Top 1000
#  - 与 SSID 相关的组合（公司名 + 年份、路由器默认格式）
#  - 8 位纯数字（很多路由器默认就是这个格式）

# ① 常见弱口令（来自 Kali 自带词表 + 你自己整理）
ls /usr/share/wordlists/
# ② 用 crunch 生成 8 位纯数字（见 04-口令攻击/crunch.md）
crunch 8 8 0123456789 -o /tmp/8digit.txt
# ③ 数字结尾的常见模式
crunch 6 8 abcdefghijklmnopqrstuvwxyz0123456789 -t @@@@@@%% -o /tmp/letters-num.txt
```

**解读**：**字典质量 > 字典大小**。真实案例里，一个大范围的中文机构 Wi-Fi 口令分布往往集中在：

| 模式 | 举例 | 生成方式 |
|------|------|----------|
| 8 位纯数字 | `12345678`、`88888888` | `crunch 8 8 0123456789` |
| 手机号 | `13800138000` | 按号段生成 |
| 常见弱口令 | `password`、`admin123` | 词表 Top-N |
| 机构名 + 年份 | `Company2024` | 手工规则 |
| 路由器默认 | `NETGEAR`/`TP-LINK` 的默认格式 | 厂商文档 |
| 键盘走位 | `qwertyui`、`1qaz2wsx` | 常见词表含 |

```bash
# 把定向字典合并（去重）后跑
cat /tmp/8digit.txt /tmp/letters-num.txt /usr/share/wordlists/rockyou.txt 2>/dev/null | sort -u > /tmp/targeted.txt
wc -l /tmp/targeted.txt
cowpatty -f /tmp/targeted.txt -r /tmp/lab-01.cap -s "WPA-LAB"
```

**3b. 把同一份抓包交给 hashcat，直观感受差距**

```bash
# hashcat 需要 22000 格式：用 aircrack-ng 或 hcxtools 转换
sudo apt install hcxtools 2>/dev/null
hcxpcapngtool -o /tmp/lab.22000 /tmp/lab-01.cap     # 新版 hcxtools
# 或（老工具）：wpaclean / aircrack-ng 也能产出
ls -l /tmp/lab.22000 && head -1 /tmp/lab.22000

# 用 hashcat 跑同一份字典（-m 22000 = WPA-PBKDF2-PMKID+EAPOL）
hashcat -m 22000 /tmp/lab.22000 /tmp/targeted.txt --force --potfile-disable
```

```console
# hashcat 的速率（Speed）通常是 cowpatty 的几十到上千倍
```

**解读（这是本篇最重要的一条工程结论）**：

| | cowpatty | hashcat |
|---|---|---|
| 计算单元 | CPU | **GPU** |
| 典型速率 | 数百 ~ 数千 /秒 | **数十万 ~ 数百万 /秒** |
| 是否支持 PMKID | ❌（只处理四次握手） | ✅（`-m 22000` 同时支持） |
| 适用 | 教学、快速验证、小字典 | **真实评估** |

详见 [`hashcat.md`](hashcat.md)。

**3c. 「破不出来」时该得出什么结论**

```bash
# 假设跑完一个大字典仍未命中
cowpatty -f /tmp/targeted.txt -r /tmp/lab-01.cap -s "WPA-LAB"
```

```console
Collected all necessary data to mount crack against WPA2/PSK passphrase.
Starting dictionary attack. Please be patient.

Could not find a matching PSK in the specified dictionary.
```

**这个「未命中」本身就是有价值的结论**——它意味着：

| 结论 | 在报告里怎么写 |
|------|----------------|
| 口令**不在字典范围内** | 「经 X 万条常见口令字典测试，未恢复出该网络 PSK；**说明口令强度高于常见弱口令水平**」 |
| **不等于「无法破解」** | 换更大的字典/GPU/规则仍可能命中——**不要写「该网络不可破解」** |
| 应该给出的**量化建议** | 「建议 PSK ≥ 12 位、含大小写数字符号、非常见词；并启用 **WPA3-SAE**」 |

**⚠️ 最容易犯的错**：把「字典没命中」写成人身/组织「安全」的结论，或者反过来把「字典命中」当成「协议不安全」——**两者都错**：

- **协议没有缺陷**，问题在**口令太弱**；
- 口令强 = 离线攻击不可行（**这正是 PBKDF2 4096 次迭代 + 每 SSID 加盐的设计目的**）。

---

## 6. 输出解读

### 6.1 关键输出行

| 输出 | 含义 | 判断 |
|------|------|------|
| `cowpatty 4.8 - WPA-PSK dictionary attack. <jwright@hasborg.com>` | 启动横幅 | 正常 |
| `Collected all necessary data to mount crack against WPA2/PSK passphrase.` | **抓到并解析出完整握手** | ✅ 可以继续 |
| `Could not retrieve necessary data from the capture file.` | **握手数据不足** | ❌ 重新抓包；核对 `-s` |
| `Starting dictionary attack. Please be patient.` | 开始逐口令验证 | —— |
| `The PSK is "xxxxxxxx".` | **命中！引号内即口令** | 记录（这是取证/评估的关键结果） |
| `Could not find a matching PSK in the specified dictionary.` | **未命中** | **不是失败，是结论**（口令不在字典范围） |
| `N passphrases tested in T seconds: R passphrases/second` | 速率统计 | **用 `R` 反推大字典需要多久** |

### 6.2 速率 → 时间的换算（工程上必须会算）

```
预计耗时 = 字典行数 ÷ 实测速率 (passphrases/second)

例：字典 14,000,000 条，实测 500 条/秒
    → 14,000,000 ÷ 500 = 28,000 秒 ≈ 7.8 小时
```

**先跑一个小样本拿速率，再决定要不要跑全量**——这是最省时间的一条实践。

### 6.3 「未命中」后该做什么

| 下一步 | 说明 |
|--------|------|
| 换**更大的字典** | rockyou 全量、常见中文口令表 |
| 换**更聪明的字典** | 用 `crunch` 按目标特征生成（见 [`crunch.md`](crunch.md)、[`cewl.md`](cewl.md) 从站点抓词） |
| **换 GPU 工具** | hashcat `-m 22000`（**性价比最高的提升**） |
| 试**规则变形** | hashcat 的 `-r` 规则（`password` → `P@ssw0rd!`） |
| 确认**材料无误** | SSID 是否完全一致；握手是否完整（`-c`） |
| 得出结论 | 「口令强于字典覆盖范围」——写成量化结论 |

---

## 7. 与其他工具配合

```
   ① 监听与扫描                         见 05-无线攻击/
      airmon-ng（开监听）                 airmon-ng.md
      airodump-ng（扫描 + 抓握手）         airodump-ng.md
      kismet（发现设备）                   kismet.md
                │
   ② 逼客户端重连，拿到握手
      aireplay-ng --deauth                 aireplay-ng.md
                │
   ③ 验证握手材料
      cowpatty -c                          ← 本文
      （或 aircrack-ng 也能验证握手）
                │
   ④ 破解
      ├─ cowpatty -f dict     ← 本文（CPU，直白）
      ├─ cowpatty -d hash     ← 本文（genpmk 预计算，同 SSID 复用）
      ├─ aircrack-ng -w       → aircrack-ng.md（同类，全家桶）
      ├─ hashcat -m 22000     → hashcat.md（**GPU，首选**）
      └─ john --format=wpapsk → john.md（CPU）
                │
   ⑤ 字典来源
      rockyou / wordlists      → wordlists.md
      crunch（规则生成）        → crunch.md
      cewl（从网站抓词）        → cewl.md
                │
   ⑥ 进入网络后的下一步
      nmap / netexec / responder → 01-信息搜集/、08-后渗透/
```

**各环节的衔接要点**：

| 从 | 到 | 关键动作 |
|----|----|----------|
| `airodump-ng` | `cowpatty` | 产物是 `.cap`（libpcap）。**文件名可能是 `-01.cap`**（多文件时会滚动成 `-01`, `-02`…） |
| `airodump-ng` | `cowpatty`（Kismet 产物） | Kismet 的 `.pcapdump` 也能被 cowpatty 读（官方示例就是这么用） |
| `cowpatty -f` | `hashcat` | 先转 22000 格式（`hcxpcapngtool` / `hcxtools`），再 `-m 22000` |
| `genpmk` 的 hashfile | **不能给 hashcat 用** | hashfile 是 cowpatty 专有格式；hashcat 需要 22000 格式 |
| `cowpatty` 命中 | 后续 | 拿到 PSK ≠ 拿到网络访问权（**还有 MAC 过滤、VLAN、portal 认证、网络隔离等**） |

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `Could not retrieve necessary data from the capture file.` | **握手不完整**；或 **SSID 不对**；或抓包里根本没有目标网络 | `-c -v` 看细节；核对 SSID（含大小写/空格）；继续抓直到 `airodump-ng` 显示 `WPA handshake:` |
| 字典里有正确口令但**不命中** | **SSID 写错**（PBKDF2 的 salt 就是 SSID） | 用 `airodump-ng` 确认精确 SSID；隐藏 SSID 需从客户端关联报文恢复 |
| 命中不了，字典是 `rockyou.txt.gz` | **没解压**（cowpatty 读了 gzip 二进制） | `sudo gunzip -k /usr/share/wordlists/rockyou.txt.gz` |
| SSID 含空格导致参数解析错 | 没加引号 | `-s "My WiFi"` |
| 速率极低（几十/秒） | CPU 慢；或用了 `-f` 每次现算 PBKDF2 | 用 `-d` 预计算；或换 hashcat（GPU） |
| `-f` 和 `-d` 同时给了 | 参数互斥 | 二选一 |
| `genpmk` 生成的 hashfile 用在别的 SSID 上 → 永远不命中 | **hashfile 绑定 SSID** | 重新 `genpmk -s <正确SSID>` |
| 磁盘写满 | hashfile 比字典大得多 | 先算空间；用 `-f` 直接跑而不落盘 |
| `capture file` 是 Kismet 的 `.pcapdump`，报格式错 | 版本/格式问题 | 用 `tshark`/`tcpdump` 转成标准 pcap：`tshark -r in.pcapdump -w out.pcap` |
| 网卡进不了监听模式 | 驱动/芯片不支持 | 用支持 monitor mode 的 USB 网卡（见 [`airmon-ng.md`](../05-无线攻击/airmon-ng.md)） |
| `aireplay-ng --deauth` 没效果 | 信道不对；或客户端用了 802.11w（PMF） | `--bssid` 锁定、`-c` 指定信道；**PMF 启用时 deauth 无效**（这本身是好事，写进报告） |
| 抓到的是**别人的**握手 | 没锁 BSSID | **必须 `--bssid` 精确锁定自己的 AP**（法律要求） |
| 在虚拟机上抓不到 2.4G/5G | 无线网卡没直通给虚拟机 | 用 USB 直通，或直接在宿主 Linux 上跑 |
| 全量 rockyou 跑太久 | CPU + 1400 万条 | **先小样本估速率**；换 hashcat |
| 报告里写「该网络无法破解」 | 把「字典未命中」当成了「不可破解」 | **改成量化结论**：未在 N 条常见口令内恢复，建议提升口令强度 / 启用 WPA3 |

---

## 9. 防御视角（蓝队 / 网络管理）

WPA2-PSK 的防御非常明确：**让离线攻击在算力上不可行**。

| 风险 | 加固手段 | 说明 |
|------|----------|------|
| **口令太弱**（离线破解成功） | **PSK ≥ 12 位**，非常见词、含大小写数字符号 | 让字典/规则攻击的空间大到不可行 |
| 多人共用一个 PSK | **WPA2-Enterprise（802.1X）** 或 **WPA3-SAE** | 每人独立凭据，可追溯、可吊销 |
| **离线攻击本身**（抓到握手就能慢慢算） | **WPA3-SAE** | **SAE 用「对等实体同时认证」（Dragonfly 握手）抵抗离线字典攻击**——这是根本性的改进 |
| 握手可被抓 | 用 **WPA3-SAE**；启用 **802.11w（PMF）** 防 deauth | PMF 让 `aireplay-ng --deauth` 失效 |
| **PMKID 攻击**（无需客户端） | WPA3；或避免使用易受影响的实现 | PMKID 攻击不依赖完整四次握手 |
| 前向保密 | **WPA3-SAE + 支持 802.11w 的 AP/客户端** | 即使 PSK 泄露，历史流量也不可解（取决于实现） |
| 企业环境 | **EAP-TLS（证书）** + RADIUS | 比 PEAP/MSCHAPv2 更强（后者有已知攻击） |
| 默认 SSID/PSK 未改 | **安装时立刻改 SSID 与管理密码** | 厂商默认格式是字典里的高频项 |
| 巡检 | 定期用**授权的**无线评估检查 PSK 强度 | 用本教程的方法，**只对自己/授权网络** |

**蓝队的五条硬建议**：

1. **直接上 WPA3-SAE**（如果设备支持）——它从协议层面消灭了离线字典攻击；
2. **启用 802.11w（PMF）**：防 deauth 导致的「强制重连抓握手」；
3. **PSK 长度 ≥ 12 且随机**：可用密码管理器生成；**不要用手机号、机构名+年份、8 位数字**；
4. **访客网络与业务网络隔离**：即使访客 PSK 被破，也进不了内网；
5. **不要相信「我设的是中文/特殊字符所以安全」**：如果它在常见口令词表/规则里，一样会被命中。

**检测思路（无线侧）**：

| 事件 | 检测手段 |
|------|----------|
| 有人在做无线勘察 | WIDS/WIPS（如 Kismet 的 IDS 功能、厂商 WIPS）看探测请求与 monitor 模式设备 |
| 有人在发 deauth | WIPS 的 deauth 洪水告警；**启用 PMF 后这类攻击直接失效** |
| 有人在抓包 | 部署监控 radio（专用传感器）看异常监听行为 |
| 弱口令被用于接入 | AP/RADIUS 日志里看同一 PSK 的异常接入（Enterprise 模式下有用户名可查） |

**⚠️ 重要提醒**：**「检测到有人在扫 Wi-Fi」不代表被入侵**，很多是手机/系统的正常行为。**判定要基于证据链**。

---

## 10. 参考

- Kali 工具页（含 `cowpatty -h`、`genpmk -h` 与两个官方示例）：<https://www.kali.org/tools/cowpatty/>
- 上游（Joshua Wright 的工具页）：<https://www.willhackforsushi.com/?page_id=50>
- 源码与发行：<https://www.willhackforsushi.com/code/cowpatty/>
- Kali 包跟踪：<https://pkg.kali.org/pkg/cowpatty>
- 本地命令：`cowpatty -h`、`cowpatty -V`、`genpmk -h`
- WPA/WPA2 密钥派生（PBKDF2 + PRF）规范：IEEE 802.11i / RFC 2898（PBKDF2）
- PMKID 攻击（现代替代路径）：参见 hashcat 的 22000 格式说明
- 配套教程：[`../05-无线攻击/airodump-ng.md`](../05-无线攻击/airodump-ng.md)、[`../05-无线攻击/aireplay-ng.md`](../05-无线攻击/aireplay-ng.md)、[`../05-无线攻击/aircrack-ng.md`](../05-无线攻击/aircrack-ng.md)、[`hashcat.md`](hashcat.md)、[`john.md`](john.md)、[`wordlists.md`](wordlists.md)、[`crunch.md`](crunch.md)

## ⚠️ 法律与伦理

**这是本教程法律风险最高的一片。请逐条读完。**

**① 未授权无线测试是明确的违法行为**

- 《网络安全法》第 27 条：**不得从事非法侵入他人网络、干扰他人网络正常功能、窃取网络数据等危害网络安全的活动**；
- 《刑法》第 285 条：非法侵入计算机信息系统、**非法获取计算机信息系统数据**——**「无线网络」属于计算机信息系统**，未经授权接入并破解口令属于此列；
- 《刑法》第 288 条：**擅自设置、使用无线电台（站），或者擅自使用无线电频率，干扰无线电通讯秩序**——发送 deauth 帧干扰他人无线通信可能触及；
- 《无线电管理条例》：无线频谱是国家资源，**未经批准擅自使用/干扰无线电业务**属于违法行为；
- 各国法律大同小异：美国 CFAA、英国 Computer Misuse Act 等同样将未授权访问 Wi-Fi 入罪。

**② 「信号覆盖到我这里」不等于「我可以连/我可以测」**

- 邻居的 Wi-Fi、商场的免费 Wi-Fi、公司的办公 Wi-Fi、酒店的 Wi-Fi —— **即使你收到了信号，甚至即使它是「开放的」，未授权破解/接入/抓包都是违法的**；
- **抓取他人无线流量**还涉及《宪法》第 40 条（通信自由与通信秘密）、《个人信息保护法》。

**③ `aireplay-ng --deauth` 会实际造成他人断网**

- 这**不是「只读测试」，是主动干扰**；
- 在别人的网络上做，**等于让该网络所有用户短时断网**——既违法，也极容易被察觉和追责。

**④ 破解得到的凭据不能用于任何访问**

- 破解成功后**仅仅「验证口令正确」**就已足够（写入报告：口令强度不足）；
- **不得**用该 PSK 接入网络、访问任何资源、做任何后续操作；
- 发现的弱口令应通过**授权报告中约定的流程**告知客户/相关部门。

**必须遵守**：

1. **只对自己拥有的网络，或在书面授权范围内的网络**做无线测试（授权应明确：**范围、时间窗、允许使用的技术手段**，尤其是**是否允许 deauth**）；
2. **必须用 `--bssid` 精确锁定目标 AP**，绝不误伤邻近网络；
3. **不抓取、不存储、不分析**授权范围之外的任何无线流量；抓到的数据按敏感数据处理；
4. **不在公共场所演练**本教程的任何命令（哪怕只是扫描）；
5. **练习请自建实验室**：自己的旧路由器 + 自己的 USB 网卡 + 一次性虚拟机（场景 0）；
6. **报告脱敏**：不公开真实的 PSK、BSSID、抓包文件；
7. 若在授权评估中命中弱口令，**只做「强度不足」的结论**，并建议客户升级到 **WPA3-SAE + 802.11w**。
