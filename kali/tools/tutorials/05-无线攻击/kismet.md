# Kismet（无线网络侦测与 WIDS）

> **一句话**：被动的 802.11 / 蓝牙 / SDR 侦测、嗅探与无线入侵检测系统（WIDS），能记录你周围所有无线设备的历史，并对 deauth 洪泛、可疑 AP 等行为告警。
> **分类**：无线攻击 ｜ **Kali 包**：`kismet`（元包，含 `kismet-core` 与各类捕获驱动）｜ **官方文档**：<https://www.kismetwireless.net/>

## 1. 它解决什么问题

前面几篇工具都是「**进攻**」视角：[airodump-ng](airodump-ng.md) 抓包、[aireplay-ng](aireplay-ng.md) 注入、[reaver](reaver.md) 打 WPS。

**Kismet 是这条链路上唯一站在防守一侧的工具**：

| 能力 | 说明 |
| --- | --- |
| **被动侦测** | 列出所有可见的 AP、客户端、**所有探测过但不在范围内的网络** |
| **长时间记录** | 把发现持久化到数据库（kismetdb），**做基线** |
| **WIDS 告警** | 检测 deauth 洪泛、可疑 BSSID、AP 配置变更、客户端异常行为等 |
| **多频段** | Wi-Fi（2.4/5/6 GHz）、蓝牙、部分 SDR（RTL-SDR 等） |
| **客户端全图** | 不只是「现在连着的」，还有「曾经连过的」（从 Probe Request 提取） |
| **Web UI** | 浏览器界面，可远程访问，适合挂机长期运行 |

**它同时是进攻方的侦察工具**（列出目标）**和防守方的监控工具**（检测攻击）。本教程重点讲**防守用法**——因为市面上这类中文资料最少，而它最有价值。

**与其他工具的对比**：

| | [airodump-ng](airodump-ng.md) | **Kismet** |
| --- | --- | --- |
| 定位 | 抓包/侦察（一次性） | **长期侦测 + WIDS**（持续） |
| 数据持久化 | CSV/PCAP 文件 | **SQLite 数据库（可查询）** |
| 告警 | ❌ | ✅ |
| 客户端历史 | 只有当前看到的 | **含所有 Probe 过的网络** |
| 界面 | 终端表格 | **Web UI** |
| 多硬件 | 一张网卡 | **同时用多张网卡 + 蓝牙 + SDR** |
| 资源占用 | 小 | 较大（长期运行时） |

**选型**：

| 需求 | 用谁 |
| --- | --- |
| 抓一个握手包 | [airodump-ng](airodump-ng.md) |
| 自动抓+破 | [wifite](wifite.md) |
| **长期监控无线环境 / 检测攻击** | **Kismet** |
| 做无线勘测（wardriving） | Kismet（有 GPS 支持，可导出 GPX/KML） |
| 模块化的 MITM 与侦察 | [bettercap](bettercap.md) |

## 2. 工作原理

### 2.1 三层架构

```
┌─────────────────────────────────────────────┐
│  kismet（服务器进程）                        │
│    ├── 加载 /etc/kismet/kismet.conf 等配置    │
│    ├── 管理数据源（datasource）               │
│    ├── 存储设备、发现、告警到 kismetdb        │
│    ├── 运行插件（如 kismetdb、eventbus）      │
│    └── 提供 Web UI（HTTP + WebSocket）        │
└───────────────┬─────────────────────────────┘
                │ WebSocket（默认 2501 端口）
                ↓
┌─────────────────────────────────────────────┐
│  kismet_cap_*（捕获驱动，独立进程）           │
│    ├── kismet_cap_linux_wifi   （Wi-Fi）      │
│    ├── kismet_cap_linux_bluetooth（蓝牙）     │
│    ├── kismet_cap_sdr_rtl433 / rtladsb 等     │
│    └── 每个驱动一个进程，崩溃不影响主程序      │
└─────────────────────────────────────────────┘
                ↑
        数据源（datasource）
        -i wlan0mon / wlan1 / hci0 / rtl433:...
```

**关键设计点**：

1. **捕获驱动是独立进程**——这是 Kismet 相对 airodump-ng 的工程优势。某张网卡/驱动出问题不会拖垮整个系统。
2. **服务器与界面分离**——Web UI 可以通过网络访问，所以你可以把 Kismet 跑在一台小机器上，从另一台机器监控（**分布式侦测**）。
3. **捕获驱动可以远程连接**——`kismet_cap_*` 支持 `--connect` 连到远程 Kismet 服务器，把远端网卡的数据回传。

### 2.2 设备（device）模型

Kismet 把每个发现的实体都抽象成 **device**，并维护它们的历史：

| Device 类型 | 来源 |
| --- | --- |
| `Wi-Fi AP` | Beacon / Probe Response |
| `Wi-Fi Client` | Data 帧 / Probe Request / Association |
| `Wi-Fi Bridged` | AP 之间的桥接 |
| `Bluetooth` | 蓝牙广播 |
| `SDR devices`（433 MHz 等） | RTL-SDR 等 |

每个 device 上会累积多种 **记录（record）**：

| 记录类型 | 内容 |
| --- | --- |
| `SSID` | 网络名（一个 AP 可能有多个 SSID） |
| `BSSID` | AP 的 MAC |
| `Client MAC` | 客户端 MAC |
| **`Probe SSID`** | ⭐ **客户端主动探测过的所有网络名** |
| `Crypt` / `WPA` | 加密与 WPA 信息 |
| `Manufacturer` | 厂商（OUI 查询） |
| `Signal`（RSSI） | 信号强度历史 |
| `GPS` | 位置（配 GPS 时） |
| `Channel` | 信道 |
| `Uptime` | AP 在线时长（从 Beacon Timestamp 推导） |

**这就是 Kismet 比 airodump-ng 强的地方**：airodump-ng 给你一张实时表格；**Kismet 给你一个可查询的设备历史库**。

### 2.3 WIDS 与告警

Kismet 内置了大量 **alert（告警）** 类型。对蓝队最有价值的几类：

| 告警类型 | 触发条件 | 对应攻击 |
| --- | --- | --- |
| `DEAUTHFLOOD` | 短时间内大量 deauth 帧 | ⭐ [aireplay-ng](aireplay-ng.md) / [wifite](wifite.md) 的 deauth 攻击 |
| `DISASSOCTRAFFIC` | 大量 disassoc 帧 | 另一种干扰手法 |
| `BSSTIMESTAMP` | **Beacon 的 Timestamp 异常跳变** | **邪恶孪生 / 伪造 AP**（攻击者的时钟与真实 AP 不同步） |
| `BCASTDISASSOC` | 广播形式的 disassoc | 干扰 |
| `CHANCHANGE` | AP 突然改信道（正常的也可能触发） | 可疑 |
| `CRYPTCHANGE` | **AP 的加密方式突然改变** | **降级攻击 / 邪恶孪生** |
| `SSIDCHANGE` | SSID 变化 | 可疑 |
| `APSPOOF` | 检测到 AP 被伪造（同 BSSID 不同 SSID 特征） | 邪恶孪生 |
| `ADVCRYPTCHANGE` | 通告的加密能力变化 | 降级 |
| `BSSID_SPOOF` | BSSID 被伪造 | 攻击 |
| `NETSTUMBLER` | 检测到 NetStumbler 类工具的特征 | 有人在扫描 |
| `LUMSENTRY` | 检测到 NetStumbler/Lucent 探测 | 有人在扫描 |
| `PROBENOASSOC` | 大量 Probe 但无关联（注入测试特征） | [aireplay-ng](aireplay-ng.md) `--test` |
| `KARMA` | 检测到 Karma 攻击（响应所有 Probe 的假 AP） | 邪恶孪生变种 |
| `WPSBRUTE` | WPS PIN 暴力特征 | ⭐ [reaver](reaver.md) |

**`BSSTIMESTAMP` 是检测邪恶孪生最有效的一招**：

> 真 AP 的 Beacon 里有一个 Timestamp 字段，记录它开机以来的微秒数，**单调递增**。攻击者的假 AP **无法伪造这个值**（因为它的时钟不同步）。所以同一 BSSID 出现 Timestamp **倒退或跳变**，就是**有另一个设备在冒充它**。

### 2.4 Kismet 的被动性

**Kismet 默认是完全被动的**——它不发送任何帧（除了可选的「信道探测」和「AP 连接测试」，这些默认关闭）。

这带来：

| 优点 | 缺点 |
| --- | --- |
| **完全不可检测**（网络层） | 也很少主动发现隐藏 AP |
| 适合长期挂机监控 | 有些 AP 不广播就看不到 |

**这与 [airodump-ng](airodump-ng.md) 一致**——两者都是被动监听。这也是为什么「检测无线攻击」只能靠**观察攻击者的帧**，而不能靠「检测监听者」。

### 2.5 kismetdb —— 可查询的历史库

Kismet 把数据存进 **SQLite 数据库**（`kismetdb`）。这是它相对其他工具最大的工程优势：

```bash
# 数据库位置（默认在 log 目录）
ls -lh ~/kismet-*.kismet

# 直接用 sqlite3 查询
sqlite3 kismet-20260915.kismet "SELECT device FROM devices LIMIT 5;"
```

**配套的 kismetdb 工具**（随 `kismet-logtools` 提供）：

| 工具 | 作用 |
| --- | --- |
| `kismetdb_statistics` | 打印数据库统计摘要 |
| `kismetdb_dump_devices` | 导出设备表为 JSON |
| `kismetdb_to_pcap` | **从数据库导出 pcap**（重要：后期可以重新分析原始帧） |
| `kismetdb_to_wiglecsv` | 导出 WiGLE CSV（可上传到 WiGLE 做地图） |
| `kismetdb_to_kml` | 导出 KML（Google Earth 可视化） |
| `kismetdb_to_gpx` | 导出 GPX（GPS 轨迹） |
| `kismetdb_clean` | 清理旧数据 |
| `kismetdb_strip_packets` | 剥离原始包（保留设备信息，大幅减小体积） |

**这意味着**：你可以**先被动记录几天几周**，之后再用 `kismetdb_to_pcap` 把流量导出来给 Wireshark 慢慢分析。**这是做基线检测的正确姿势**。

## 3. 安装与快速上手

```bash
sudo apt install kismet
kismet --help 2>&1 | head -30
```

**元包结构**：

| 包 | 内容 |
| --- | --- |
| `kismet` | 元包（拉取下面这些） |
| `kismet-core` | 主程序 + `kismet_server` + `kismetdb` 驱动 |
| `kismet-capture-linux-wifi` | **Wi-Fi 捕获驱动**（最常用） |
| `kismet-capture-linux-bluetooth` | 蓝牙捕获 |
| `kismet-capture-sdr-rtl433` 等 | SDR 捕获（433 MHz、ADS-B、气象站等） |
| `kismet-logtools` | **kismetdb 工具集** |
| `kismet-capture-common` | setuid 捕获二进制的 debconf 文件 |

**最短工作流**：

```bash
# 1) 启动（默认会尝试自动发现数据源）
sudo kismet

# 2) 从另一台机器的浏览器访问 Web UI
#    http://<kismet主机IP>:2501/
```

**指定数据源**（推荐，避免自动发现选错网卡）：

```bash
sudo kismet -c wlan0
```

**运行时的注意事项**：

- Kismet 会警告「以 root 运行不推荐」——这是**设计如此**，因为捕获需要特权。生产环境应使用 setuid 的捕获驱动 + 非特权主进程（Kali 的包默认已配置好）。
- 按 `Ctrl+C` 退出前，**等它把数据写入数据库**（会打印 `Shutting down...`）。

## 4. 核心参数详解

### 4.1 核心选项

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-c, --capture-source <spec>` | **指定数据源**（可多次） | ⭐ **最常用的参数**。`-c wlan0`、`-c wlan0mon`、`-c wlan0:channel=6` |
| `-C, --enable-capture-sources <list>` | 启用逗号分隔的已配置数据源 | 配置文件里定义了但默认禁用时用 |
| `-f, --config-file <file>` | 使用指定的配置文件 | 多套配置切换 |
| `--confdir <path>` | 使用替代的配置目录 | 默认 `/etc/kismet/` |
| `--homedir <path>` | 使用替代的 HOME 目录 | 隔离运行 |
| `--override <flavor>` | 使用**配置 override**（配置变体） | ⭐ 生产用：把自定义配置**与包管理的默认配置分离**（升级不会覆盖） |
| `--no-ncurses` | 禁用 ncurses 包装界面，输出纯文本 | ⭐ **脚本化/作为服务运行时必加** |
| `--no-line-wrap` | 不折行（便于 grep） | ⭐ 脚本化时用 |
| `-s, --silent` | 设置完成后关闭 stdout 输出 | 后台运行 |
| `--daemonize` | 后台守护进程化 | 作为服务运行 |
| `--debug` | 调试模式（禁用崩溃处理、ncurses 包装） | 配合 GDB |
| `--no-plugins` | 不加载任何插件 | 排查插件导致的崩溃 |
| `-h, --help` | 帮助 | — |
| `-v, --version` | 版本 | — |

### 4.2 日志选项

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-p, --log-prefix <dir>` | **日志/数据库输出目录** | ⭐ 长期运行时指向大分区 |
| `-t, --log-title <title>` | 日志标题（写入日志模板的 title 字段） | 便于事后区分多次运行 |
| `-T, --log-types <t1,t2,...>` | 生成的日志类型 | 只想要 kismetdb 时可关掉别的 |
| `-n, --no-logging` | 本次运行完全关闭日志 | ⭐ **纯监控不留痕迹时用** |

### 4.3 数据源（capture source）语法

`-c` 的参数是一个数据源规范，格式灵活：

| 写法 | 含义 |
| --- | --- |
| `-c wlan0` | 用 `wlan0` 作为数据源（Kismet 会自动处理监听模式） |
| `-c wlan0mon` | 已经是监听模式的接口 |
| `-c wlan0:channel=6` | 锁定信道 6 |
| `-c wlan0:channel=1,6,11` | 在这三个信道间跳 |
| `-c wlan0:hop=true` | 启用跳频 |
| `-c wlan0:name=wifi1` | 给数据源起名 |
| `-c wlan0:add_channels=2.4GHz` | 追加监听整个 2.4 GHz 频段 |
| `-c wlan0:add_channels=5GHz` | 追加 5 GHz |
| `-c wlan0:add_channels=6GHz` | 追加 6 GHz（需要支持 6 GHz 的网卡） |
| `-c wlan0:hop_rate=1` | 跳频速率（每秒跳几个信道） |
| `-c wlan1:type=linuxwifi` | 显式指定驱动类型 |
| `-c hci0` | 蓝牙设备 |
| `-c 'rtl433-0:...'` | SDR 设备 |
| `-c wlan0:uuid=...` | 用 UUID 引用已配置的数据源 |

**锁定 vs 跳频的取舍**：

| | 锁定信道 | 跳频 |
| --- | --- | --- |
| 好处 | **不漏包**（单信道完整捕获） | 覆盖多个信道（看到更多网络） |
| 坏处 | 只能看一个信道 | **会漏包**（每信道只停留一小会儿） |
| 适用 | 目标明确的深度监控 | 广域侦测/勘测 |

**多网卡的最优配置**：一张锁定目标信道做深度监控，另一张跳频做广域感知。

```bash
sudo kismet -c wlan0:channel=6 -c wlan1:add_channels=2.4GHz
```

### 4.4 配置文件

| 文件 | 作用 |
| --- | --- |
| `/etc/kismet/kismet.conf` | **主配置** |
| `/etc/kismet/kismet_logging.conf` | 日志与数据库设置 |
| `/etc/kismet/kismet_httpd.conf` | Web UI 设置（端口、认证） |
| `/etc/kismet/kismet_alerts.conf` | **告警规则**（WIDS 的核心） |
| `/etc/kismet/kismet_memory.conf` | 内存/资源限制 |
| `/etc/kismet/kismet_80211.conf` | 802.11 相关设置 |
| `/etc/kismet/kismet_bluetooth.conf` | 蓝牙设置 |
| `/etc/kismet/kismet_uav.conf` | 无人机（Remote ID）设置 |
| `/etc/kismet/kismet_site.conf` | **本机专属设置（不会被升级覆盖）** |

**关键实践**：

```bash
# 查看当前生效的主要配置
grep -v '^#' /etc/kismet/kismet.conf | grep -v '^$' | head -40

# 查看告警相关配置
grep -i 'alert\|deauth' /etc/kismet/kismet_alerts.conf | head -40
```

**推荐做法**：**改 `/etc/kismet/kismet_site.conf`**（或使用 `--override <flavor>`），而不是直接改 `kismet.conf`——这样包升级不会覆盖你的修改。

### 4.5 kismetdb 工具

| 工具 | 关键参数 | 作用 |
| --- | --- | --- |
| `kismetdb_statistics` | `--in <db>` | 打印统计摘要（设备数、包数、时间范围） |
| `kismetdb_dump_devices` | `--in <db>`、`--out <json>` | 导出设备为 JSON |
| `kismetdb_to_pcap` | `--in <db>`、`--out <pcap>`、`--since <time>`、`--until <time>` | 导出 pcap（可带时间范围） |
| `kismetdb_to_wiglecsv` | `--in <db>`、`--out <csv>` | 导出 WiGLE CSV |
| `kismetdb_to_kml` | `--in`、`--out` | 导出 KML |
| `kismetdb_to_gpx` | `--in`、`--out` | 导出 GPX 轨迹 |
| `kismetdb_clean` | `--in`、`--days <n>` | 删除 n 天前的数据 |
| `kismetdb_strip_packets` | `--in`、`--out` | 剥离原始包（大幅减小体积，保留设备信息） |

## 5. 实战演练

**环境声明**：Kismet 默认被动监听。但**被动接收他人通信本身在多数司法辖区即违法**。以下所有操作**仅限你自己拥有的无线环境**、隔离实验室、有书面授权的场地。**在自己的家里/办公室对「自己视野内的邻居 AP」做长期监控同样是违法的**——请使用隔离房间或不接收他人信号的受控环境。

### 场景 1：基础启动与 Web UI

**步骤 1：看看有哪些无线接口**

```bash
sudo airmon-ng
iw dev
```

**步骤 2：启动 Kismet（指定数据源）**

```bash
sudo kismet -c wlan0 --no-ncurses --log-prefix ~/kismet-logs/
```

| 参数 | 作用 |
| --- | --- |
| `-c wlan0` | 用 `wlan0` 作数据源（Kismet 会自己处理监听模式） |
| `--no-ncurses` | 禁用 ncurses 包装，输出纯文本（便于看日志） |
| `--log-prefix ~/kismet-logs/` | 日志与数据库输出到这个目录 |

**预期输出（节选）**

```
INFO: Reading from config file /etc/kismet/kismet.conf
INFO: No 'dronelisten' config line and no command line drone-listen argument given, Kismet drone server will not be enabled.
INFO: Created alert tracker...
INFO: Creating device tracker...
INFO: Registered 80211 PHY as id
INFO: Kismet starting as user 'kismet' with datasource privileges
INFO: Listening on port 2501
INFO: Kismet web server is now accepting connections at http://localhost:2501/
```

**关键行**：

| 行 | 含义 |
| --- | --- |
| `Reading from config file /etc/kismet/kismet.conf` | **配置文件位置** |
| `Kismet web server is now accepting connections at http://localhost:2501/` | ⭐ **Web UI 地址与端口** |

**注意**：如果你以 root 启动，Kismet 会警告：

```
ERROR: Kismet was started as root, NOT launching external control binary.
       This is NOT the preferred method of starting Kismet as Kismet will
       continue to run as root the entire time.  Please read the README
       file section about Installation & Security and be sure this is what
       you want to do.
```

**这说明它降级了**——正常安装下，Kismet 会以非特权用户运行主进程，只有捕获驱动用 setuid。**如果看到这个警告，说明你的包安装不完整**（缺 `kismet-capture-common` 的配置）：`sudo dpkg-reconfigure kismet-capture-common`。

**步骤 3：打开 Web UI**

```bash
# 本机
xdg-open http://localhost:2501/

# 或从另一台机器（需在 kismet_httpd.conf 里允许远程访问）
# http://<kismet主机IP>:2501/
```

**首次访问需要设置用户名与密码**（Kismet 从 2020 版开始强制 Web 认证）。

**Web UI 的主要页面**：

| 页面 | 内容 |
| --- | --- |
| **Dashboard** | 概览：设备数、数据包数、告警数 |
| **Data Sources** | 数据源列表与状态（哪个网卡在跑、收了多少包） |
| **Devices** | ⭐ **所有发现的设备**（AP、客户端、蓝牙…），可筛选、排序、查看详情 |
| **Alerts** | ⭐ **WIDS 告警列表** |
| **Channels** | 信道占用统计 |
| **GPS** | 位置信息 |
| **Messages** | 系统消息 |

**最有用的两个页面是 `Devices` 和 `Alerts`**。

### 场景 2：建立自己的无线基线（蓝队核心用法）

**目标**：知道「正常状态下我的无线环境长什么样」，从而能发现异常。

**步骤 1：选择数据源配置**

```bash
# 锁定你的 AP 所在信道（深度监控一个信道，不漏包）
sudo kismet -c wlan0:channel=6 \
  --log-prefix ~/kismet-baseline/ \
  --log-title baseline-2026-09-15 \
  --no-ncurses --silent
```

| 参数 | 作用 |
| --- | --- |
| `wlan0:channel=6` | **锁定信道**（不跳频，保证不漏帧） |
| `--log-title` | 给这次运行的日志打标签，便于事后区分 |
| `--silent` | 减少 stdout 输出 |

**步骤 2：让它跑一段时间**

对于家用环境，建议**至少 24 小时**（覆盖设备上线下线的完整周期）。对于企业环境，建议**至少一周**。

**步骤 3：查看统计**

```bash
# 找到数据库文件
ls -lh ~/kismet-baseline/

# 看统计摘要
kismetdb_statistics --in ~/kismet-baseline/*.kismet
```

**预期输出**

```
KismetDB version: 9
Total packets: 1842937
First packet time: 2026-09-15 00:00:12
Last packet time: 2026-09-15 23:59:58
Total devices: 342
Total alerts: 12
```

**步骤 4：导出设备清单作为基线**

```bash
kismetdb_dump_devices --in ~/kismet-baseline/*.kismet --out ~/baseline-devices.json
python3 -c "
import json
d = json.load(open('$HOME/baseline-devices.json'))
print('设备总数:', len(d))
for dev in d[:5]:
    print(dev.get('kismet.device.base.key'), dev.get('kismet.device.base.macaddr'))
"
```

**步骤 5：把基线做成「允许清单」**

```bash
# 提取所有本环境的 BSSID 作为允许清单
kismetdb_dump_devices --in ~/kismet-baseline/*.kismet --out /tmp/baseline.json
python3 - <<'EOF'
import json
d = json.load(open('/tmp/baseline.json'))
bssids = sorted({
    dev['kismet.device.base.macaddr'] for dev in d
    if 'kismet.device.base.macaddr' in dev
})
with open('/tmp/allowed-bssids.txt', 'w') as f:
    f.write('\n'.join(bssids) + '\n')
print(f'写入 {len(bssids)} 个 BSSID')
EOF

head /tmp/allowed-bssids.txt
```

**这个清单就是你的「正常设备表」**。之后定期对比，就能发现新增的可疑设备。

**步骤 6：定期对比，发现新设备**

```bash
# 新的监控运行
sudo kismet -c wlan0:channel=6 --log-prefix ~/kismet-today/ --silent --no-ncurses
# （跑一段时间后 Ctrl+C）

# 导出并对比
kismetdb_dump_devices --in ~/kismet-today/*.kismet --out /tmp/today.json
python3 - <<'EOF'
import json
today = json.load(open('/tmp/today.json'))
allowed = set(open('/tmp/allowed-bssids.txt').read().split())
new = []
for dev in today:
    mac = dev.get('kismet.device.base.macaddr')
    if mac and mac not in allowed:
        new.append((mac, dev.get('kismet.device.base.name', '?'),
                    dev.get('kismet.device.base.type', '?')))
print(f'新增设备: {len(new)} 个')
for mac, name, typ in new[:20]:
    print(f'  {mac}  {typ}  {name}')
EOF
```

**⭐ 这就是 Kismet 最有价值的用法**：不是「看当前有什么」，而是**「看有什么变化」**。

### 场景 3：检测 deauth 攻击（WIDS 实战）

**目标**：当有人在你的无线环境里跑 [aireplay-ng](aireplay-ng.md) `--deauth` 或 [wifite](wifite.md) 时，**发现自己被打**。

**步骤 1：确认告警配置已启用**

```bash
grep -i 'deauth' /etc/kismet/kismet_alerts.conf
```

**预期输出（节选）**

```
# Deauth flood
alert DEAUTHFLOOD "deauthflood" "DEAUTHFLOOD,IEEE80211_DEAUTH" 1000 300 5 5
```

**配置字段解读**：

```
alert <名称> "<描述>" "<过滤条件>" <阈值> <窗口毫秒> <限制> <突发>
                        ↑              ↑      ↑
              DEAUTHFLOOD 类型     触发阈值  时间窗口(ms)
                                      5        5000
                                      = 5 秒内 1000 个 deauth 帧
```

**步骤 2：启动 Kismet 监控**

```bash
sudo kismet -c wlan0:channel=6 --log-prefix ~/kismet-wids/ --no-ncurses
```

**步骤 3：在另一个终端/设备上，对自己的网络做 deauth（仅限自实验！）**

```bash
# ⚠️ 仅限你自己的网络！
sudo aireplay-ng --deauth 20 -a AA:BB:CC:DD:EE:FF wlan0mon
```

**步骤 4：观察 Kismet 的告警**

Web UI 的 **Alerts** 页面会出现：

```
DEAUTHFLOOD  AA:BB:CC:DD:EE:FF  2026-09-15 14:22:31  ...
```

或者在终端输出里看到类似行：

```
ALERT: DEAUTHFLOOD AA:BB:CC:DD:EE:FF ...
```

**步骤 5：从数据库查询告警**

```bash
sqlite3 ~/kismet-wids/*.kismet "SELECT ts_sec, header, json FROM alerts LIMIT 10;"
# 或用 kismetdb 工具导出
kismetdb_dump_devices --in ~/kismet-wids/*.kismet --out /tmp/alerts.json
```

**⭐ 这个练习的价值**：它让你**亲眼看到**攻击在防守侧长什么样。这是理解「WIDS 如何工作」最快的路径。

**注意**：`DEAUTHFLOOD` 的默认阈值是 **5 秒内 1000 个 deauth 帧**。`aireplay-ng --deauth 5` 只发 5×64=320 个，**可能不会触发默认阈值**。要测试时可以用更大的 count，或**调整告警阈值**：

```bash
# 在 /etc/kismet/kismet_site.conf 里覆盖（不要改原文件）
sudo tee -a /etc/kismet/kismet_site.conf <<'EOF'
# 降低 deauth 告警阈值用于测试（生产环境按实际调整）
alert DEAUTHFLOOD "deauthflood" "DEAUTHFLOOD,IEEE80211_DEAUTH" 100 5000 5 5
EOF
```

**这正是蓝队需要做的事**：**根据自己的环境调整阈值**。默认值偏保守（避免误报），实际环境里可能需要更敏感。

### 场景 4：检测邪恶孪生 / 伪造 AP

**目标**：有人在你的环境里用 [bettercap](bettercap.md) / [airbase-ng](aircrack-ng.md) 建了一个同名假 AP。

**Kismet 的检测方式**：

| 告警 | 原理 |
| --- | --- |
| **`BSSTIMESTAMP`** | ⭐ **最有效**。真 AP 的 Beacon Timestamp 单调递增；假 AP 无法伪造 → 出现「Timestamp 倒退」 |
| `CRYPTCHANGE` | 假 AP 的加密配置与真 AP 不一致 |
| `SSIDCHANGE` | 同一 BSSID 出现不同 SSID |
| `APSPOOF` | 综合特征判定 AP 被伪造 |
| `BCASTDISASSOC` | 伪造 AP 常发广播 disassoc 把客户端赶到自己这来 |

**做法**：

```bash
# 1) 建立基线（场景 2 已做）
# 2) 持续监控，关注 Alerts 页面
# 3) 出现 BSSTIMESTAMP / CRYPTCHANGE / APSPOOF 告警时立即排查
```

**验证一个可疑 AP**：

```bash
# 用 airodump-ng 看它的详细信息（这是侦察，不是攻击）
sudo airodump-ng -c 6 --bssid <可疑BSSID> wlan0mon
```

对比它与你基线中的记录：

| 对比项 | 真 AP | 可疑 AP |
| --- | --- | --- |
| BSSID | 基线里的 | **相同或很相似（仿冒）** |
| 信道 | 基线里的 | 可能是不同信道 |
| 加密配置 | 基线里的 | **可能不同（降级）** |
| 信号强度 | 稳定（-50 左右） | **突然很强（就在附近）** |
| Beacon 间隔 | 约 100ms | **可能不规律** |
| **Timestamp** | **单调递增** | **跳变/倒退** |

**⭐ 这就是为什么「建立基线」是蓝队的核心工作**：没有基线，你无法判断「这个突然出现的强信号 AP 是不是正常的」。

### 场景 5：从 kismetdb 导出 pcap 做深度分析

**为什么有用**：Kismet 长期运行产生的数据库很大，但你**可以先只记录设备信息（剥离原始包），需要时再回溯**。

**方法 A：先剥离，后分析**

```bash
# 剥离原始包，只保留设备元数据（体积大幅缩小）
kismetdb_strip_packets --in ~/kismet-baseline/kismet-20260915.kismet \
                       --out ~/kismet-baseline/stripped.kismet

ls -lh ~/kismet-baseline/*.kismet
```

**方法 B：需要时导出 pcap 给 Wireshark**

```bash
# 导出整个时间范围的 pcap
kismetdb_to_pcap --in ~/kismet-baseline/kismet-20260915.kismet \
                 --out ~/baseline.pcap

# 只导出某个时间段（例如攻击发生的那 10 分钟）
kismetdb_to_pcap --in ~/kismet-baseline/kismet-20260915.kismet \
                 --out ~/attack-window.pcap \
                 --since "2026-09-15 14:20:00" \
                 --until "2026-09-15 14:30:00"

# 用 Wireshark / tshark 分析
tshark -r ~/attack-window.pcap -Y 'wlan.fc.type_subtype == 0x0c'   # 只看 deauth
wireshark ~/attack-window.pcap
```

**常用 Wireshark 过滤器（802.11 入侵分析）**：

| 过滤器 | 作用 |
| --- | --- |
| `wlan.fc.type_subtype == 0x0c` | **Deauthentication 帧** |
| `wlan.fc.type_subtype == 0x0a` | **Disassociation 帧** |
| `wlan.fc.type_subtype == 0x08` | **Beacon 帧** |
| `wlan.fc.type_subtype == 0x04` | Probe Request |
| `wlan.fc.type_subtype == 0x05` | Probe Response |
| `wlan.fc.type_subtype == 0x00` | Association Request |
| `eapol` | 握手报文 |
| `wlan.ssid contains "lab"` | 特定 SSID |
| `wlan.bssid == aa:bb:cc:dd:ee:ff` | 特定 AP |

**统计 deauth 的源地址分布**：

```bash
tshark -r ~/attack-window.pcap -Y 'wlan.fc.type_subtype == 0x0c' \
  -T fields -e wlan.sa -e wlan.da -e wlan.fixed.reason_code | \
  sort | uniq -c | sort -rn | head -20
```

**⭐ 这一步的意义**：把「Kismet 告警了」变成「**我知道攻击来自哪个 MAC、针对哪个目标、用的什么 reason code、持续了多久**」。这才是可以用来写安全事件报告的证据。

### 场景 6：把 WiGLE 格式导出（勘测报告）

```bash
# 导出 WiGLE CSV（可上传到 wigle.net 生成地图）
kismetdb_to_wiglecsv --in ~/kismet-logs/kismet-20260915.kismet \
                     --out ~/survey.csv

head -3 ~/survey.csv
# 需要 GPS 数据才有坐标；无 GPS 时坐标为 0
```

**有 GPS 时的完整勘测**：

```bash
sudo kismet -c wlan0 --use-gpsd-gps --log-prefix ~/kismet-wardrive/
```

**⚠️ 勘测的法律边界**：

- **对你自己拥有的场地**做勘测 → 合法（这是企业做无线覆盖评估的常规做法）；
- **开着车在街上扫描他人的 Wi-Fi** → **在很多司法辖区违法**（「wardriving」的法律地位因地区而异，在中国大陆属于未经授权获取他人网络信息）；
- 上传到 WiGLE 时会**公开你的位置数据**——注意隐私。

## 6. 输出解读

### 启动输出

```
INFO: Reading from config file /etc/kismet/kismet.conf
INFO: No 'dronelisten' config line and no command line drone-listen argument given, Kismet drone server will not be enabled.
INFO: Created alert tracker...
INFO: Creating device tracker...
INFO: Registered 80211 PHY as id
INFO: Listening on port 2501
INFO: Kismet web server is now accepting connections at http://localhost:2501/
```

| 行 | 含义 | 关注点 |
| --- | --- | --- |
| `Reading from config file ...` | 配置文件路径 | 确认用的是预期配置 |
| `Created alert tracker` | ✅ **WIDS 已启用** | 没有这行说明告警被禁用 |
| `Creating device tracker` | ✅ 设备跟踪已启用 | — |
| `Registered 80211 PHY as id` | ✅ Wi-Fi 数据源已注册 | 没有类似的 `Registered ...` 行 = 数据源没起来 |
| `Listening on port 2501` | Web UI 端口 | 访问地址 |
| `Kismet was started as root, NOT launching external control binary` | ⚠️ **降级运行，用 root 跑主进程** | 见场景 1 的说明 |

### 每个数据源的状态（Web UI → Data Sources）

| 字段 | 含义 | 正常值 |
| --- | --- | --- |
| `Name` | 数据源名 | — |
| `Type` | 类型（`linuxwifi` 等） | — |
| `Packets` | 收到的包数 | **持续增长** |
| `Channels` | 监听的频段/信道 | 与配置一致 |
| `Channel` | 当前信道 | 跳频时会变化 |
| `Errors` | 错误数 | **应该为 0 或很少** |
| `Hop` | 是否跳频 | — |

**`Packets` 不增长 = 数据源有问题**（网卡没进监听模式、或信道没信号）。

### Alerts 页面

| 字段 | 含义 |
| --- | --- |
| `Type` | 告警类型（如 `DEAUTHFLOOD`） |
| `Device` | 触发告警的设备（BSSID/MAC） |
| `Time` | 首次触发时间 |
| `Last` | 最后一次触发时间 |
| `Count` | 累计触发次数 |

**列里 `Count` 持续增长说明攻击仍在进行**。

### 关键告警的判读

| 告警 | 严重性 | 可能的含义 | 下一步 |
| --- | --- | --- | --- |
| **`DEAUTHFLOOD`** | 🔴 高 | 有人在执行 deauth 攻击（抓握手或纯干扰） | 立即排查；导出该时间窗的 pcap 分析源 MAC |
| **`BSSTIMESTAMP`** | 🔴 高 | **邪恶孪生 / 伪造 AP** | 定位可疑 BSSID 的物理位置 |
| `CRYPTCHANGE` | 🟠 中 | 加密降级或 AP 被替换 | 对比基线 |
| `SSIDCHANGE` | 🟠 中 | AP 被替换或配置变更 | 对比基线 |
| `APSPOOF` | 🔴 高 | AP 伪造 | 立即排查 |
| `BCASTDISASSOC` | 🟠 中 | 伪造 AP 在把客户端赶过来 | 配合 `BSSTIMESTAMP` 判断 |
| `NETSTUMBLER` / `LUMSENTRY` | 🟡 低 | 有人在用工具扫描 | 通常是误报（很多正常客户端也触发） |
| `PROBENOASSOC` | 🟡 低 | 大量 Probe 无关联（注入测试特征） | 提高警惕 |
| `KARMA` | 🔴 高 | Karma 攻击（响应所有 Probe 的假 AP） | 立即排查 |
| `WPSBRUTE` | 🔴 高 | ⭐ **有人在跑 [reaver](reaver.md)** | 立即排查；检查自己的 WPS 是否开启 |

**⭐ 如果你的环境里出现 `WPSBRUTE` 告警——那是有人在打你的 WPS。第一件事：确认你的 WPS 是关闭的。**

### 判断成功 / 数据在哪

| 产物 | 位置/形式 |
| --- | --- |
| SQLite 数据库 | `~/kismet-*/kismet-YYYYMMDD.kismet` |
| 日志 | `~/kismet-*/Kismet-*.log` |
| 原始 pcap（可选） | `~/kismet-*/Kismet-*.pcapng`（需在配置里开启） |
| Web UI | `http://<host>:2501/` |
| 统计摘要 | `kismetdb_statistics --in <db>` |

## 7. 与其他工具配合

```text
┌───────────── 进攻方视角 ─────────────┐
│ airmon-ng → airodump-ng → aireplay-ng → aircrack-ng/hashcat │
│                    ↓                                        │
│              这些行为会被 Kismet 检测到                       │
└─────────────────────────────────────────────────────────────┘
                             ↓
┌───────────── 防守方视角（Kismet）─────────────┐
│ kismet（长期监听）                              │
│   ├→ Alerts（DEAUTHFLOOD / BSSTIMESTAMP / WPSBRUTE）│
│   ├→ kismetdb（SQLite 历史库）                   │
│   │     ├→ kismetdb_statistics（统计）            │
│   │     ├→ kismetdb_dump_devices（设备清单/基线）  │
│   │     ├→ kismetdb_to_pcap（回溯原始帧）         │
│   │     │      └→ wireshark / tshark（深度分析）  │
│   │     ├→ kismetdb_to_wiglecsv（覆盖地图）       │
│   │     └→ kismetdb_to_kml / to_gpx（地理可视化） │
│   └→ Web UI（实时监控）                          │
└─────────────────────────────────────────────────┘
```

| 组合 | 说明 |
| --- | --- |
| **Kismet → Wireshark/tshark** | ⭐ **最有价值的组合**：长期被动记录 → 事后导出特定时间窗的 pcap → 深度分析 |
| **Kismet → [airodump-ng](airodump-ng.md)** | Kismet 告警后，用 airodump-ng 精确查看可疑 AP/BSSID |
| **Kismet → [bettercap](bettercap.md)** | 两者都有侦察能力，但定位不同：Kismet 长期被动监控，bettercap 主动交互 |
| **Kismet ↔ [wifite](wifite.md) / [aireplay-ng](aireplay-ng.md)** | ⭐ **红蓝对抗演练**：一边用 wifite 攻击自己的实验网络，一边看 Kismet 告警 |
| **Kismet → 企业 SIEM** | 通过日志/API 把告警送入集中化监控 |
| **Kismet 多实例（远程捕获）** | `kismet_cap_* --connect <host>:2501` 把远端网卡数据汇总到中心服务器 |

**做一次红蓝对抗演练（强烈推荐）**：

```text
终端 1（防守）：sudo kismet -c wlan0:channel=6 --no-ncurses
终端 2（进攻）：sudo wifite --wpa -pow 50        # 仅限自己的实验网络

在 Kismet Web UI 的 Alerts 页面观察：
  - DEAUTHFLOOD 何时出现？
  - 持续多久？
  - 攻击者用了多少 deauth？
  - 你能从 pcap 里定位到攻击者的 MAC 吗？
```

**这个演练的价值无可替代**——它把「进攻教程」和「防守教程」真正连起来了。

## 8. 常见坑与排错

### 8.1 启动与数据源

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `Kismet was started as root, NOT launching external control binary` | 缺 `kismet-capture-common` 的 setuid 配置 | `sudo dpkg-reconfigure kismet-capture-common`；或按官方文档配置 setuid |
| `No data sources found` / 没有任何数据源 | `-c` 参数没给，或网卡不支持 | 显式加 `-c wlan0`；用 `iw list` 确认支持 monitor |
| Web UI 打不开 | 端口冲突 / 防火墙 / 只监听 localhost | 检查 `kismet_httpd.conf` 的 `httpd_listen`；`ss -tlnp \| grep 2501` |
| 端口 2501 被占用 | 已有 Kismet 实例在跑 | `pkill kismet` 或换端口 |
| `Failed to open datasource` | 网卡被别的程序占用 | `sudo airmon-ng check kill`；停掉 NetworkManager |
| **`Packets` 不增长** | 数据源起来了但收不到包 | 检查信道是否与目标一致；检查 `Errors`；网卡是否真的是监听模式 |
| 网卡在 Kismet 里不能跳频 | 某些驱动在别的程序切过模式后状态异常 | 先 `airmon-ng stop` 再让 Kismet 自己管理网卡 |
| 蓝牙数据源起不来 | 缺 `kismet-capture-linux-bluetooth` 或权限 | `sudo apt install kismet-capture-linux-bluetooth`; `hciconfig` 确认蓝牙可用 |
| 以 root 跑导致数据库文件属主混乱 | 主进程用了 root | 用 `dpkg-reconfigure` 修复；或改 `kismet.conf` 里的 `log_prefix` 到一个可写目录 |
| `--confdir` 改了但配置没生效 | 用了错误的路径，或缺文件 | 先只改一个文件验证；用 `--debug` 看它读了哪些配置 |

### 8.2 资源与性能

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| 数据库长得飞快 | 默认会记录原始包 | ⭐ 定期 `kismetdb_strip_packets`；或配置里关掉 pcap 日志 |
| 磁盘满 | 长期运行 + 大数据库 | `kismetdb_clean --in <db> --days 7`；`--log-prefix` 指向大分区 |
| 内存占用高 | 设备数极多（如密集办公区） | 调整 `kismet_memory.conf` 里的限制 |
| CPU 高 | 多数据源 + 跳频 + 高流量 | 减少数据源；锁定信道（不跳频）；增大 `hop_rate` |
| Kismet 跑了几天后卡顿 | 数据库过大 | 定期清理；或每天一个数据库（默认就是按天分文件） |

### 8.3 WIDS 相关

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| **完全不产生 `DEAUTHFLOOD` 告警** | 阈值太高（默认 5 秒内 1000 个） | ⭐ 在 `kismet_site.conf` 里降低阈值 |
| 大量 `NETSTUMBLER` 误报 | 很多正常客户端也会触发探测特征 | 在 `kismet_alerts.conf` 里禁用该告警 |
| 告警太多，看不过来 | 默认阈值不适合你的环境 | ⭐ **按自己的环境调阈值**——这是 WIDS 部署的核心工作 |
| 收不到告警但攻击确实发生了 | ① 信道没锁定（漏帧）；② 攻击者在别的信道；③ 信号太远 | 锁定目标信道；多网卡覆盖；靠近 |
| `BSSTIMESTAMP` 误报 | 有些 AP 固件的 Timestamp 确实不正常 | 把它加入基线并记录为已知问题 |
| 数据库里的 alerts 表为空 | 告警只在内存中，或日志类型没包含 | 检查 `-T` 日志类型；Kismet 的告警默认写入数据库 |

### 8.4 一个实际的排错流程

```text
Kismet 没有检测到攻击
│
├─ 数据源在正常工作吗？
│    → Web UI → Data Sources → Packets 是否在增长？
│    → 不增长 → 检查网卡模式/信道/是否被占用
│
├─ 信道锁定对了吗？
│    → 攻击发生在 6 信道，你监听 11 信道 → 什么都看不到
│    → Kismet 的 -c wlan0:channel=6 显式锁定
│
├─ 告警阈值合理吗？
│    → 默认 DEAUTHFLOOD 是 5s/1000 帧，小规模攻击不会触发
│    → 降低阈值测试
│
├─ 攻击者在范围内吗？
│    → 信号强度：Device 详情里的 RSSI
│    → 太远 → 增大覆盖（多网卡/更好的天线）
│
└─ 攻击类型有对应告警吗？
     → 检查 kismet_alerts.conf 里该类型是否被注释掉了
     → 用 grep 查找对应告警定义
```

## 9. 防御视角（蓝队）

**这一整节就是 Kismet 的存在理由。** 本节给出一个可落地的无线安全监控方案。

### 9.1 部署架构

**单点监控（小环境）**：

```bash
# 一台小机器（树莓派/旧笔记本）+ 一块支持监听的 USB 网卡
sudo kismet -c wlan0:channel=6 \
  --log-prefix /var/log/kismet/ \
  --log-title home-baseline \
  --silent --no-ncurses --daemonize
```

**多点分布式（企业环境）**：

```text
[监控点 1：会议室]  ─┐
[监控点 2：前台]    ─┼─→ [中心 Kismet 服务器] ─→ [Web UI / SIEM]
[监控点 3：机房]    ─┘         ↑
                        kismet_cap_* --connect <server>:2501
```

**每个监控点的数据源建议**：

| 监控点 | 数据源配置 | 目的 |
| --- | --- | --- |
| 关键区域 | `channel=<关键信道>` | 深度监控，不漏帧（检测 deauth） |
| 覆盖大范围 | `add_channels=2.4GHz` | 广域感知，发现新设备 |
| 5 GHz 环境 | `add_channels=5GHz` | 现代设备多在 5 GHz |
| 蓝牙 | `-c hci0` | BLE 设备（如有需求） |

**⚠️ 隔离要求**：如果监控点会接收到**非授权区域**的信号，必须采取隔离措施（方向性天线、降低灵敏度、屏蔽）。**不能以「我在监控自己的网络」为由接收邻区的通信。**

### 9.2 三类核心检测

#### ① 检测 deauth 攻击（抓握手的前置动作）

| 项 | 内容 |
| --- | --- |
| 告警 | `DEAUTHFLOOD`、`DISASSOCTRAFFIC`、`BCASTDISASSOC` |
| 原理 | 正常网络中 deauth 是**罕见事件**（只有设备主动断开时才出现）。突然出现大量 deauth 一定异常 |
| 阈值建议 | 先按默认跑一周，观察基线；然后设成「基线的 3~5 倍」 |
| 事后分析 | 导出该时间窗 pcap，统计 deauth 的源 MAC / reason code 分布 |

**为什么这条最有价值**：deauth 是**任何 WPA 握手捕获攻击的必经步骤**（除了 PMKID）。检测到 deauth 洪泛 ≈ 检测到有人在抓你的握手。

#### ② 检测伪造 AP / 邪恶孪生

| 项 | 内容 |
| --- | --- |
| 告警 | **`BSSTIMESTAMP`**（最有效）、`CRYPTCHANGE`、`SSIDCHANGE`、`APSPOOF`、`KARMA` |
| 原理 | 真 AP 的 Beacon Timestamp 单调递增；假 AP 的时钟无法同步 → **Timestamp 倒退** |
| 关键前提 | **必须先建立 BSSID 基线**（否则无法判断哪个是真的） |

**`BSSTIMESTAMP` 为什么这么强**：

> 攻击者要伪造这个字段，必须**精确知道真 AP 的 Timestamp 值并持续同步**。假 AP 一旦重启、或网络抖动导致丢了几帧 Beacon，Timestamp 就会偏离——**这个时序特性极难伪造**。

#### ③ 检测 WPS 暴力

| 项 | 内容 |
| --- | --- |
| 告警 | `WPSBRUTE` |
| 原理 | [reaver](reaver.md) 会在短时间内产生大量 WPS 交互（M4/M5/M6/M7 消息） |
| 应对 | **立即确认自己的 WPS 是否开启**；如开启则关闭 |

### 9.3 基线建设（蓝队最重要的日常工作）

**没有基线，WIDS 就是一堆噪声。** 建立基线的完整流程：

```text
第 1 步：收集（1~4 周）
  sudo kismet -c wlan0:channel=<关键信道> --log-prefix /var/log/kismet/baseline/
  → 覆盖完整的业务周期（工作日、周末、白天、夜间）

第 2 步：提取允许清单
  kismetdb_dump_devices --in <db> --out baseline.json
  → 提取所有 BSSID / 客户端 MAC

第 3 步：标注
  对每条记录标注：这是什么设备？属于哪个部门？在哪个位置？
  → 这是运维工作，但从长远看极有价值

第 4 步：调阈值
  观察基线期内各类告警的触发频率
  → 把阈值设为「基线峰值 × 3~5 倍」

第 5 步：持续对比
  定期（每天/每周）运行并 diff 新增设备
  → 新增设备需人工确认是否为授权设备
```

**一条实用的对比脚本**：

```bash
#!/usr/bin/env bash
# 说明：对比无线设备基线，发现新增设备。仅用于自有/授权网络的监控。
set -euo pipefail

BASELINE=/var/log/kismet/allowed-bssids.txt
DB="$1"

kismetdb_dump_devices --in "$DB" --out /tmp/current.json

python3 - "$BASELINE" /tmp/current.json <<'EOF'
import json, sys
allowed = set(open(sys.argv[1]).read().split())
devices = json.load(open(sys.argv[2]))
new = []
for d in devices:
    mac = d.get('kismet.device.base.macaddr')
    if mac and mac not in allowed:
        new.append((mac,
                    d.get('kismet.device.base.type', '?'),
                    d.get('kismet.device.base.name', '')))
print(f"新增设备: {len(new)}")
for mac, typ, name in new:
    print(f"  {mac:20s} {typ:20s} {name}")
EOF
```

**把它挂到 cron 上，每天跑一次**：这是最实用的无线监控落地方式。

### 9.4 与整体加固的关系

Kismet 是**检测层**，它需要配合**防护层**才能真正有效：

| 层次 | 措施 | 效果 |
| --- | --- | --- |
| **检测层（Kismet）** | deauth 告警、伪造 AP 告警、WPS 暴力告警 | 发现问题 |
| **防护层（配置）** | **WPA3-SAE**、**PMF/802.11w**、**关闭 WPS**、长随机 PSK | **让攻击无效** |
| **网络层** | 访客网络隔离、802.1X + EAP-TLS | 限制影响范围 |
| **物理层** | 降低发射功率、方向性天线、屏蔽 | 缩小攻击面 |
| **管理层** | 员工培训（不连陌生热点）、定期勘测 | 减少人为风险 |

**关键理解**：

> **检测 ≠ 防护。** 你可以在 Kismet 里看到 `DEAUTHFLOOD`，但如果没有启用 PMF，攻击**依然会成功**（你的客户端依然掉线，握手依然被抓）。
>
> **Kismet 的价值是「让你知道发生了什么」，而「阻止它发生」需要配置层面的加固。**

**因此正确的优先级是**：

```text
1. 开启 PMF（阻止 deauth）        ← 预防
2. 关闭 WPS（阻止 WPS 攻击）       ← 预防
3. 升级 WPA3（阻止离线破解）        ← 预防
4. 部署 Kismet（发现其它攻击）      ← 检测
5. 建立基线并持续对比               ← 检测
```

### 9.5 一个常被忽略的价值：取证与事后分析

Kismet 的数据库是**时间序列的历史记录**。这带来一个独特价值：

> **当安全事件发生时，你可以回溯之前的无线活动。**

例如：

```text
用户报告："昨天下午 3 点我的网络断了几分钟"

你的操作：
1. 打开 Kismet 数据库
2. 查询昨天 14:50 - 15:10 的告警
3. 发现 DEAUTHFLOOD（14:58 - 15:02）
4. 导出该时间窗 pcap
5. 用 tshark 统计 deauth 的源 MAC
6. 在基线里查这个 MAC → 不在基线中 → 可疑设备
7. 结合物理位置信息定位
```

**这是纯靠实时监控做不到的**——必须有历史数据库。

**这也是为什么「用 Kismet 长期记录」值得投入存储成本**。

## 10. 参考

- 官方站点：<https://www.kismetwireless.net/>
- 官方文档：<https://www.kismetwireless.net/docs/>
- **命令行选项**：<https://www.kismetwireless.net/docs/readme/starting/commandline/>
- **配置文件说明**：<https://www.kismetwireless.net/docs/readme/configuring/configfiles/>
- 数据源与捕获驱动：<https://www.kismetwireless.net/docs/readme/datasources/>
- Kali 工具页：<https://www.kali.org/tools/kismet/>
- 本机手册：`man kismet`、`kismet --help`、`man kismetdb_statistics` 等
- 本机配置目录：**`/etc/kismet/`**（主配置 `kismet.conf`）
- 本机工具：`kismetdb_statistics`、`kismetdb_dump_devices`、`kismetdb_to_pcap`、`kismetdb_to_wiglecsv`、`kismetdb_to_kml`、`kismetdb_to_gpx`、`kismetdb_clean`、`kismetdb_strip_packets`
- 相关本目录：[aircrack-ng](aircrack-ng.md)（套件总览）、[airmon-ng](airmon-ng.md)、[airodump-ng](airodump-ng.md)、[aireplay-ng](aireplay-ng.md)、[wifite](wifite.md)、[reaver](reaver.md)、[bettercap](bettercap.md)
- 相关其他目录：[wireshark](../07-嗅探与欺骗/wireshark.md)、[tshark](../07-嗅探与欺骗/wireshark.md)、[tcpdump](../07-嗅探与欺骗/tcpdump.md)

## ⚠️ 法律与伦理

Kismet 默认被动监听，**这在法律上比主动注入工具更微妙，但风险依然很高**：

| Kismet 的行为 | 法律性质 |
| --- | --- |
| 接收 Beacon 帧（广播帧） | 争议较小，但**接收本身仍属「截获通信」** |
| **接收 Data 帧（含明文内容）** | ⚠️ **截获通信内容** |
| **记录客户端的 Probe Request（暴露用户去过的网络）** | ⚠️ **涉及个人信息** |
| 长期存储、导出、上传（如 WiGLE） | ⚠️ **数据处理与公开传播** |
| 对他人网络做勘测（wardriving） | ⚠️ 在多数司法辖区**违法** |

**关键点**：**「我只是在监听，没有攻击」不是合法的抗辩理由。** 「截获他人通信」本身就是法律禁止的行为。

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条第二款 | **非法获取计算机信息系统数据罪** |
| 《刑法》 | 第二百五十三条之一 | **侵犯公民个人信息罪**（Probe 数据暴露用户行踪） |
| 《无线电管理条例》 | 相关条款 | 擅自使用无线电频率 |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《个人信息保护法》 | 相关条款 | 收集、存储、处理个人信息需有合法性基础 |
| 《数据安全法》 | 相关条款 | 数据处理活动的合规要求 |

**本教程仅适用于**：

- ✅ **你自己拥有的无线环境**，且**采取了隔离措施确保不接收他人信号**（屏蔽房间、方向性天线、降低灵敏度）
- ✅ 有**书面授权**、明确列出监控范围与目的的无线安全监控（如企业 WIPS 部署）
- ✅ 你自己搭建的隔离无线实验室
- ✅ 授权的 CTF 靶场

**⚠️ 特别注意「邻居的信号」问题**：

> 即使你只是在自己家里跑 Kismet，**你大概率也会收到邻居的 Wi-Fi 信号**。
> 「我家的设备接收到了邻居的信号」**不能作为合法性依据**——你必须：
> - 使用 **Faraday 屏蔽**（屏蔽房间/屏蔽箱）；
> - 或使用**方向性天线 + 降低功率**，把接收范围限制在自己的场地内；
> - 或**在数据处理上只保留自己设备的记录**（但这要求你能可靠区分）。
>
> **做不到隔离，就不要运行。**

**严禁**：

- ❌ 对邻居、公司、公共场所的任何无线环境做监控
- ❌ 开着车/走着路做 wardriving 扫描他人网络
- ❌ 记录、存储、导出他人的通信内容或设备信息
- ❌ 把包含他人信息的数据库上传到 WiGLE 等公开平台
- ❌ 把 Kismet 数据库当作「公开数据」分享

**推荐的学习方式（完全合法）**：

```text
✅ 在一个屏蔽的隔离环境（或用极低功率 + 方向性天线）里，
   用自己的几个设备建立基线，然后用 wifite 攻击自己的网络，
   观察 Kismet 的告警。
   → 这覆盖了 100% 的知识点：设备模型、WIDS 告警、基线对比、pcap 回溯
✅ 分析 Kismet 自带的示例数据库（如果有）
✅ 阅读官方文档与告警类型列表
```

**Kismet 的真正价值在于防守。** 请把它用在**保护自己的网络**上——这也正是它的设计初衷（它是一个 WIDS 框架，而不是攻击工具）。
