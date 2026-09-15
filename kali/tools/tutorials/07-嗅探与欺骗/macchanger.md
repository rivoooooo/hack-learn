# MAC changer（网卡 MAC 地址修改）

> **一句话**：查看和修改网络接口的 MAC 地址——可以指定、随机生成、或伪装成其他厂商的地址。
> **分类**：嗅探与欺骗 ｜ **Kali 包**：`macchanger` ｜ **官方文档**：<https://github.com/alobbs/macchanger>

## 1. 它解决什么问题

**MAC 地址是链路层的身份标识**，在很多场景里被当作「设备身份」使用：

| 依赖 MAC 的场景 | 后果 |
| --- | --- |
| 路由器 MAC 白名单 | 换了设备就上不了网 |
| 酒店的按设备计费 WiFi | 换 MAC 可以重置计时 |
| 企业 NAC（网络准入控制） | 用 MAC 判断是否准入 |
| 网络监控/审计 | 用 MAC 追踪设备 |
| 商家/公共 WiFi 的用户追踪 | ⚠️ **用 MAC 跨网络跟踪同一设备** |
| 无线网络的客户端识别 | — |

**macchanger 解决的三个问题**：

| 需求 | 说明 |
| --- | --- |
| **隐私** | ⭐ 防止被商家、广告商、公共 WiFi 用 MAC 跨网络追踪（**这是最正当的用途**） |
| **测试** | 在授权的渗透测试中，验证 MAC 过滤/白名单是否真的生效 |
| **兼容** | 有些驱动程序/虚拟化场景需要修改 MAC |

**「MAC 欺骗」这个叫法容易让人以为是攻击技术，但它最常见的用途其实是隐私保护**——现代操作系统（iOS 14+、Android 10+、Windows 10+）都内置了「MAC 随机化」功能，macchanger 做的是同一件事，只是更灵活。

## 2. 工作原理

### 2.1 MAC 地址的结构

一个 48 位的 MAC 地址：

```
AA:BB:CC:DD:EE:FF
└────┬────┘└──┬──┘
  OUI           设备序号
（厂商前缀）    （由厂商分配）

第 1 个字节的最低位 = 单播/组播标志（0 = 单播）
第 1 个字节的次低位 = 全局/本地标志（0 = 全局唯一，1 = 本地管理）
```

**举个例子**：

```
08:00:27:AA:BB:CC
└──┬──┘
08:00:27 = PCS Systemtechnik GmbH / Oracle VirtualBox
           （所以这是一个 VirtualBox 虚拟机）

00:0C:29:AA:BB:CC
└──┬──┘
00:0C:29 = VMware, Inc.
```

**⭐ OUI（Organizationally Unique Identifier）查询**能直接告诉你设备的厂商——这是一个极有价值的侦察信息（见第 7 节）。

**「本地管理地址」（Locally Administered Address）**：

```
加 02: 到第一个字节 → 表示这是一个「本地管理」的地址（不是厂商分配的）
例如：08:00:27:AA:BB:CC  →  0A:00:27:AA:BB:CC
                              ↑
                        0x08 | 0x02 = 0x0A
```

**⭐ 这一点很重要**：**规范地修改 MAC 时应该设置「本地管理」位**（即第一个字节与 `0x02` 做 OR）——这样网络设备能识别出「这是本地修改过的地址」，不会与真实的厂商地址冲突。

macchanger 的 `-m` / `-r` / `-a` 都会自动处理这个位。

### 2.2 修改 MAC 的原理

| 层级 | 机制 |
| --- | --- |
| **硬件层** | 网卡的 MAC 固化在 EEPROM 里（**通常无法软件修改**） |
| **驱动层** | 驱动有一个「当前 MAC」的寄存器值，**可以覆盖 EEPROM 的值** |
| **软件层** | 操作系统用驱动提供的值来构造帧 |

**macchanger 改的是驱动层的值**，所以：

| 特性 | 说明 |
| --- | --- |
| **重启后恢复** | ⚠️ 驱动重新加载后回到原始的 MAC |
| **需要接口 down** | 改 MAC 前必须先关闭接口 |
| **特权要求** | 需要 root 或 `CAP_NET_ADMIN` |
| **不改 EEPROM** | 原始的出厂 MAC 始终保留（`-p` 可以恢复它） |
| **虚拟机/容器** | 大多数虚拟网卡支持 |

**⭐ 为什么必须「先 down 再改再 up」**：

```
接口处于 up 状态时，驱动已经在使用当前的 MAC
→ 直接改会被拒绝或无效
→ 必须先 down（驱动释放）→ 改 → up（驱动重新读取）
```

### 2.3 macchanger 的各种「改法」

| 参数 | 生成方式 | 特点 |
| --- | --- | --- |
| `-m XX:XX:...` | **用户指定** | 完全可控 |
| `-r` | **完全随机** | 随机 OUI + 随机设备号（可能看起来像随机厂商的地址） |
| `-a` | **同类型厂商的随机 MAC** | 保留「这是一块无线网卡/有线网卡」的特征 |
| `-A` | **任意厂商的随机 MAC** | 可能变成看起来像别的类型的设备 |
| `-e` | 配合上述参数，**只改设备号不改厂商前缀** | 保持厂商一致 |
| `-p` | **恢复出厂 MAC** | 从 EEPROM 读回原值 |
| `-l` | 列出已知厂商的 OUI | 用于查找特定厂商的前缀 |

**`-r` / `-a` / `-A` 的区别**：

| | `-r`（random） | `-a`（another, same kind） | `-A`（another, any kind） |
| --- | --- | --- | --- |
| OUI | 随机（可能是任意厂商） | **同类型设备的厂商**（无线→无线） | **任意厂商** |
| 看起来像 | 某个随机厂商的设备 | 同类设备的另一个 | 任意设备 |
| 适合 | 完全不想被关联 | ⭐ **保持设备类型一致** | 特殊场景 |

**⭐ 隐私场景推荐 `-a`**——它保持你的设备看起来还是「一块网卡」，而不是变成看起来像打印机或摄像头的地址（那样反而更可疑）。

### 2.4 现代替代：操作系统内置的 MAC 随机化

| 系统 | 功能 | 位置 |
| --- | --- | --- |
| **iOS 14+** | 「私有 Wi-Fi 地址」 | 默认开启 |
| **Android 10+** | 「随机 MAC」 | 默认开启（按网络） |
| **Windows 10/11** | 「随机硬件地址」 | 设置 → 网络 → Wi-Fi → 随机硬件地址 |
| **macOS** | 「私有 Wi-Fi 地址」 | 默认开启 |
| **Linux NetworkManager** | `wifi.cloned-mac-address=random` | `nmcli` 配置 |

**⚠️ 一个重要区别**：

| | 系统内置随机化 | macchanger |
| --- | --- | --- |
| 时机 | **每次连接时**（或每次开机） | 手动（你决定何时） |
| 范围 | 通常只对 Wi-Fi | 任意接口（有线/无线） |
| 灵活性 | 低 | ⭐ **高**（可指定具体 MAC） |
| 持久性 | 由系统策略管理 | ⚠️ **重启失效**（需要脚本） |

**⭐ 实务建议**：**日常隐私用系统内置功能就够了**（它更安全、更自动化）。**macchanger 更适合：**

- 需要**指定**一个特定 MAC（如测试 MAC 白名单）；
- 需要对**有线**接口改 MAC；
- 需要在脚本里精确控制。

## 3. 安装与快速上手

```bash
sudo apt install macchanger
macchanger -h
```

**⚠️ Debian/Kali 的安装会问一个互动问题**：

```
Should macchanger automatically change the MAC address of a network device at boot?

  1. Yes
  2. No
```

**建议选 `No`**（除非你确实想要开机自动随机化）：

| 选项 | 后果 |
| --- | --- |
| `Yes` | 每次开机**自动随机化所有网卡 MAC** → 可能导致网络配置（DHCP 保留、MAC 白名单）失效 |
| `No` | 手动控制 ⭐ |

**如果选错了，重新配置**：

```bash
sudo dpkg-reconfigure macchanger
```

**最短工作流**：

```bash
# 1) 看当前 MAC
macchanger -s eth0

# 2) 关闭接口
sudo ip link set eth0 down

# 3) 改成随机（同类型厂商）
sudo macchanger -a eth0

# 4) 开启接口
sudo ip link set eth0 up

# 5) 验证
macchanger -s eth0
ip link show eth0
```

**一行版**：

```bash
sudo ip link set eth0 down && sudo macchanger -a eth0 && sudo ip link set eth0 up
```

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-h, --help` | 帮助 | — |
| `-V, --version` | 版本 | — |
| **`-s, --show`** | **显示当前 MAC**（并打印当前网卡信息） | ⭐ 不改，只看 |
| **`-m XX:XX:XX:XX:XX:XX`** | **设置为指定 MAC** | ⭐ 需要特定地址时用 |
| `--mac XX:XX:XX:XX:XX:XX` | 同上（等号形式） | — |
| **`-r, --random`** | **完全随机 MAC** | 随机 OUI + 随机设备号 |
| **`-a, --another`** | **同类型厂商的随机 MAC** | ⭐ **推荐**（保持设备类型特征） |
| `-A` | 任意厂商的随机 MAC | 可能看起来像别的设备类型 |
| `-e, --ending` | **只改设备号，不改变厂商前缀** | 配合 `-a` / `-r` / `-A` 使用 |
| **`-p, --permanent`** | **恢复出厂（永久）MAC** | ⭐ 用完恢复 |
| `-l, --list[=关键字]` | **列出已知厂商** | `-l Cisco` 找 Cisco 的 OUI |
| `-b, --bia` | 假装是「烧录地址」（BIA） | 罕见 |

### 关键参数的组合用法

| 组合 | 效果 |
| --- | --- |
| `macchanger -A eth0` | 任意厂商的随机 MAC |
| `macchanger -A -e eth0` | 随机厂商前缀 + 随机设备号（`-A` 的默认行为） |
| `macchanger -a eth0` | 同类型厂商的随机 MAC |
| `macchanger -r eth0` | 完全随机 |
| **`macchanger -m 00:11:22:33:44:55 eth0`** | 精确指定 |
| `macchanger -p eth0` | 恢复出厂 MAC |

### `-l` 的用法

```bash
# 列出所有已知厂商（数千条）
macchanger -l | head -20

# 查找特定厂商
macchanger -l Cisco | head -10
macchanger -l "Apple" | head -10
macchanger -l | grep -i -m5 'vmware\|virtualbox'
```

**注意事项**：

| 事项 | 说明 |
| --- | --- |
| OUI 数据库的时效性 | macchanger 的内置列表**可能较旧**；新的 OUI 可能查不到 |
| 输出格式 | `厂商前缀 - 厂商名` |

### 手动方式（不用 macchanger）

macchanger 只是「方便」。你也可以用 `ip` 直接改：

```bash
sudo ip link set eth0 down
sudo ip link set eth0 address 02:11:22:33:44:55
sudo ip link set eth0 up
```

**⭐ 两者的区别**：

| | `ip link set address` | macchanger |
| --- | --- | --- |
| 依赖 | 无（`iproute2` 自带） | 需要装 macchanger |
| 随机生成 | ❌ 需自己生成 | ✅ 内置多种策略 |
| 恢复出厂值 | ⚠️ 需要自己记住原值 | ✅ `-p` |
| OUI 查询 | ❌ | ✅ `-l` |
| 输出信息 | 无 | ✅ 打印厂商信息 |

**⭐ 实务建议**：**用 macchanger 生成 MAC，用 `ip` 快速设置**，或直接用 macchanger 一步完成。

## 5. 实战演练

**环境声明**：修改**你自己设备**的 MAC 是完全正常的操作（隐私保护、测试）。

**⚠️ 但用修改后的 MAC 去绕过他人的 MAC 白名单/接入控制，属于未授权访问。**

### 场景 1：查看当前 MAC（不做任何修改）

```bash
macchanger -s eth0
```

**预期输出**

```
Current MAC:   08:00:27:aa:bb:cc (PCS Systemtechnik GmbH)
Permanent MAC: 08:00:27:aa:bb:cc (PCS Systemtechnik GmbH)
```

| 字段 | 含义 |
| --- | --- |
| `Current MAC` | **当前生效的 MAC**（可能被改过） |
| `Permanent MAC` | **出厂 MAC**（从 EEPROM 读，无法软件修改） |
| 括号里 | **厂商**（OUI 查询结果） |

**⭐ 这个输出的教学价值**：

```
- "Current" 和 "Permanent" 不同的可能性：
  ① 你改过 MAC；
  ② macchanger 的 debconf 配置了开机自动随机化；
  ③ NetworkManager 配置了 cloned-mac-address。

- 厂商识别：08:00:27 = VirtualBox，说明这是个虚拟机。
  这在渗透测试的侦察阶段很有用（判断目标是物理机还是虚拟环境）。
```

**也看看系统的视角**：

```bash
ip link show eth0
# 2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 ...
#     link/ether 08:00:27:aa:bb:cc brd ff:ff:ff:ff:ff:ff
#                ↑ 这就是当前 MAC

# 或
cat /sys/class/net/eth0/address
```

### 场景 2：改成随机 MAC（隐私保护的标准用法）

**步骤 1：先记下原值**（便于恢复）

```bash
ORIG_MAC=$(cat /sys/class/net/eth0/address)
echo "原 MAC: $ORIG_MAC"
```

**步骤 2：关闭接口并修改**

```bash
sudo ip link set eth0 down
sudo macchanger -a eth0
sudo ip link set eth0 up
```

**预期输出**

```
Current MAC:   08:00:27:aa:bb:cc (PCS Systemtechnik GmbH)
Permanent MAC: 08:00:27:aa:bb:cc (PCS Systemtechnik GmbH)
New MAC:       0a:1b:2c:3d:4e:5f (Unknown)
```

**⭐ 逐行解读**：

| 行 | 含义 |
| --- | --- |
| `Current MAC` | 修改前 |
| `Permanent MAC` | 出厂值（**始终不变**） |
| **`New MAC`** | ⭐ 新的 MAC |
| `(Unknown)` | OUI 不在数据库里 → 说明这是随机生成的地址 |

**⭐ 为什么是新 MAC 的第一个字节是 `0a`**：

```
0x08 | 0x02 = 0x0A
      ↑
   设置「本地管理」位
```

**macchanger 自动设置了「本地管理」位**——这是规范的做法。

**步骤 3：验证**

```bash
macchanger -s eth0
# Current MAC:   0a:1b:2c:3d:4e:5f (Unknown)
# Permanent MAC: 08:00:27:aa:bb:cc (PCS Systemtechnik GmbH)

ip link show eth0 | grep ether
# link/ether 0a:1b:2c:3d:4e:5f brd ff:ff:ff:ff:ff:ff
```

**⭐ ⭐ 但这里有一个重要的现实**：

> **DHCP 分配给你的 IP** 是基于**原来的 MAC** 的。
> 改 MAC 后，**DHCP 租约可能失效** → 你需要**重新获取 IP**。

```bash
# 重新获取 DHCP
sudo dhclient -r eth0      # 释放
sudo dhclient eth0         # 重新获取

# 或者用 NetworkManager
sudo nmcli device reapply eth0
# 或者重连
sudo nmcli connection down "有线连接 1" && sudo nmcli connection up "有线连接 1"
```

**⚠️ 如果你是 SSH 到这台机器的**：**改 MAC 会断开你的 SSH 连接**（因为 IP 会变）。

**⭐ 正确的做法**：

| 场景 | 建议 |
| --- | --- |
| 物理机本地操作 | 直接改，然后重连 DHCP |
| **通过 SSH 操作** | ⚠️ **用 `nohup`/`screen`/`tmux` 包裹**，否则命令执行到一半连接就断了 |
| 虚拟机（通过控制台） | 直接改 |

**安全的 SSH 改 MAC 方式**：

```bash
# 在 tmux/screen 里
sudo ip link set eth0 down && \
  sudo macchanger -a eth0 && \
  sudo ip link set eth0 up && \
  sudo dhclient -r eth0 && \
  sudo dhclient eth0
```

### 场景 3：指定一个特定的 MAC

**用途**：测试你自己的 MAC 白名单是否生效。

```bash
sudo ip link set eth0 down
sudo macchanger -m 00:11:22:33:44:55 eth0
sudo ip link set eth0 up
```

**预期输出**

```
Current MAC:   0a:1b:2c:3d:4e:5f (Unknown)
Permanent MAC: 08:00:27:aa:bb:cc (PCS Systemtechnik GmbH)
New MAC:       00:11:22:33:44:55 (Cimsys Inc)
```

**⭐ 注意括号里的 `Cimsys Inc`** —— 因为 `00:11:22` 是一个真实的 OUI。**如果你随便编一个 MAC，可能正好落在某个厂商的 OUI 范围内**，这时 macchanger 会显示出那个厂商。

**⚠️ 常见错误**：

| 错误 | 说明 |
| --- | --- |
| 用**组播地址**（第一个字节最低位为 1） | 例如 `01:...` —— 网卡不会接受这种单播 MAC |
| 用**全零或全 F** | `00:00:00:00:00:00` 或 `FF:FF:FF:FF:FF:FF` 都是特殊值 |
| 与网络里已有设备冲突 | ⚠️ **会造成 MAC 冲突**，破坏网络 |
| 忘了设「本地管理」位 | 会伪装成某个真实厂商的设备（可能不适合隐私场景） |

**⭐ 规范做法**：如果想手动指定一个「安全的」地址，用 `02:` 开头（`0x02` 就是本地管理位）：

```bash
sudo macchanger -m 02:aa:bb:cc:dd:ee eth0
```

### 场景 4：只改设备号，保留厂商前缀

**用途**：你的设备是 Cisco 网卡，想让它看起来还是 Cisco 的（只是换了具体设备）。

```bash
# 保留 OUI，随机化设备号
sudo ip link set eth0 down
sudo macchanger -e -a eth0     # 或 macchanger -e -r eth0
sudo ip link set eth0 up
```

**`-e` 的效果**：

```
原：  08:00:27:aa:bb:cc
新：  08:00:27:xx:yy:zz     ← 只改了后 3 字节
      └──┬──┘
   厂商前缀保持不变
```

**⭐ 什么场景用 `-e`**：

| 场景 | 说明 |
| --- | --- |
| 想让设备「看起来正常」 | 保留厂商特征，不显得可疑 |
| MAC 白名单按 OUI 放行 | 只改设备号就能过 |
| 避免 OUI 变化导致的兼容问题 | 某些驱动/交换机对 OUI 敏感 |

### 场景 5：恢复出厂 MAC

```bash
sudo ip link set eth0 down
sudo macchanger -p eth0
sudo ip link set eth0 up

# 重置 DHCP
sudo dhclient -r eth0 && sudo dhclient eth0
```

**预期输出**

```
Current MAC:   0a:1b:2c:3d:4e:5f (Unknown)
Permanent MAC: 08:00:27:aa:bb:cc (PCS Systemtechnik GmbH)
New MAC:       08:00:27:aa:bb:cc (PCS Systemtechnik GmbH)
```

**⭐ `-p` 是从「Permanent MAC」读出来的**——这个值来自网卡的 EEPROM，**macchanger 改不了它**。

**这是 macchanger 的一个安全特性**：**你永远不会「弄丢」原始的 MAC**。

### 场景 6：MAC 随机化的持久化（重启后仍然生效）

**问题**：`ip link set` 或 macchanger 改的 MAC **重启后就没了**。

**解决方案（按推荐度排序）**：

**① NetworkManager 的内置功能**（⭐ **推荐**）

```bash
# 查看当前配置
nmcli connection show "有线连接 1" | grep cloned-mac-address

# 设置为「每次连接随机」
nmcli connection modify "有线连接 1" \
  wifi.cloned-mac-address random \
  802-3-ethernet.cloned-mac-address random

# 或者「每次连接稳定随机」（同一网络用同一个 MAC，更实用）
nmcli connection modify "有线连接 1" \
  wifi.cloned-mac-address stable \
  802-3-ethernet.cloned-mac-address stable

# 应用
nmcli connection up "有线连接 1"
```

**`cloned-mac-address` 的取值**：

| 值 | 含义 |
| --- | --- |
| `permanent` | 用出厂 MAC（默认） |
| `preserve` | 保留当前值 |
| `random` | **每次连接都换一个新的** |
| `stable` | ⭐ **对同一网络保持稳定**（推荐——既保护隐私，又不会因为每次换 MAC 而触发异常告警） |
| `00:11:22:...` | 指定固定值 |

**⭐ `stable` 的好处**：

| | `random` | `stable` |
| --- | --- | --- |
| 每次连接 | 新 MAC | 同一网络同一 MAC |
| 隐私 | 更好 | 好（不同网络不同 MAC） |
| 网络**稳定** | ❌ 每次换 MAC 会导致 DHCP 记录混乱、日志难以关联 | ✅ 可正常关联 |
| 触发的告警 | ⚠️ 网络监控会觉得「设备一直变」很可疑 | 少 |

**② systemd 服务（最可控）**

```bash
sudo tee /etc/systemd/system/macchanger.service <<'EOF'
[Unit]
Description=Randomize MAC address on boot
Before=network-pre.target
Wants=network-pre.target

[Service]
Type=oneshot
ExecStart=/bin/sh -c 'ip link set eth0 down && macchanger -a eth0 && ip link set eth0 up'
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable macchanger.service
```

**⚠️ 注意**：这个服务在网卡还没完全就绪时可能失败。更稳的做法是用 udev 规则或 NetworkManager。

**③ udev 规则**

```
# /etc/udev/rules.d/70-mac-random.rules
ACTION=="add", SUBSYSTEM=="net", KERNEL=="eth0", RUN+="/sbin/ip link set dev %k address 02:aa:bb:cc:dd:ee"
```

**⭐ 推荐**：**用 NetworkManager 的 `cloned-mac-address`**（方案 ①）——它最干净、最不容易出问题。

### 场景 7：验证 MAC 真的变了（用 tcpdump）

**这是一个很实用的验证方法**——证明「网卡实际发出的帧用的是新 MAC」。

```bash
# 1) 改 MAC
sudo ip link set eth0 down && sudo macchanger -a eth0 && sudo ip link set eth0 up

# 2) 用 tcpdump 抓包，看实际的 MAC（必须加 -e）
sudo tcpdump -i eth0 -e -nn -c 5
```

**预期输出**

```
14:40:01.123456 0a:1b:2c:3d:4e:5f > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 42: ...
                └────────┬────────┘
              新 MAC 出现在实际发送的帧里 ✅
```

**⭐ 这个验证很有价值**：

| 验证点 | 说明 |
| --- | --- |
| 出方向的帧用的是新 MAC | ✅ 证明驱动层已生效 |
| 收到的帧（如果有） | 目的地址是新 MAC 才算真正「占用了」这个地址 |

**`tcpdump -e` 是必须的**——不加 `-e` 看不到链路层的 MAC。

## 6. 输出解读

### `macchanger -s` 的输出

```
Current MAC:   0a:1b:2c:3d:4e:5f (Unknown)
Permanent MAC: 08:00:27:aa:bb:cc (PCS Systemtechnik GmbH)
```

| 行 | 含义 | 关注点 |
| --- | --- | --- |
| `Current MAC` | 当前生效的 | 如果 ≠ Permanent，说明被改过 |
| `Permanent MAC` | 出厂值（EEPROM） | **无法软件修改** |
| `(厂商名)` | OUI 查询结果 | ⭐ **侦察信息**：能判断设备类型 |

**⭐ `(Unknown)` 的含义**：

```
- 这是随机生成的 MAC（OUI 不在数据库里）
- 或者 OUI 数据库较旧，不认识新的厂商前缀
```

### 修改时的输出

```
Current MAC:   08:00:27:aa:bb:cc (PCS Systemtechnik GmbH)   ← 改之前
Permanent MAC: 08:00:27:aa:bb:cc (PCS Systemtechnik GmbH)   ← 出厂值
New MAC:       0a:1b:2c:3d:4e:5f (Unknown)                  ← ⭐ 改之后
```

**判断成功**：出现 `New MAC:` 行，且 `ip link show` 里显示的是新值。

### `-l` 的输出

```
$ macchanger -l | head -5
Misc MACs:
000000 - XEROX CORPORATION
000001 - XEROX CORPORATION
000002 - XEROX CORPORATION
...
```

**格式**：`OUI前6位 - 厂商名`

### 常见错误输出

| 输出 | 含义 | 解决 |
| --- | --- | --- |
| `ERROR: Can't change MAC: interface up or not permitted` | ⚠️ **接口是 up 状态** | ⭐ 先 `ip link set eth0 down` |
| `ERROR: This device does not support changing MAC` | 驱动/硬件不支持 | 换网卡或驱动 |
| `ERROR: unable to find device eth0` | 接口名错 | `ip link` 看接口名 |
| `ERROR: Permission denied` | 没有权限 | `sudo` |
| `ERROR: Invalid MAC address` | MAC 格式错 | 用 `XX:XX:XX:XX:XX:XX`（6 组十六进制） |
| 命令成功但 `ip link` 显示还是旧值 | 接口没重新 up，或驱动不吃 | 确认 down→改→up 的顺序 |

## 7. 与其他工具配合

```text
[侦察阶段]
  ├─ macchanger -s eth0        → 看自己的 MAC 与厂商
  ├─ macchanger -l <厂商>       → 查特定厂商的 OUI
  └─ ip neigh / arp -a         → 看邻居的 MAC → 反查厂商 → 判断设备类型

[测试阶段]
  ├─ macchanger -a eth0        → 随机化（隐私 / 测试 MAC 过滤）
  └─ macchanger -m <MAC> eth0  → 指定 MAC（测白名单）

[验证阶段]
  ├─ tcpdump -i eth0 -e -nn    → ⭐ 验证实际的帧里用了新 MAC
  ├─ Wireshark / tshark        → 同样的验证
  └─ dhclient / nmcli          → 重新获取 IP

[恢复阶段]
  └─ macchanger -p eth0        → 恢复出厂 MAC
```

| 组合 | 说明 |
| --- | --- |
| **macchanger ↔ [tcpdump](tcpdump.md)** | ⭐ **验证 MAC 是否真的变了**：`tcpdump -i eth0 -e -nn` |
| **macchanger ↔ [Wireshark](wireshark.md)** | 同样的验证，或用它从 pcap 里分析 MAC |
| **macchanger ↔ [ettercap](ettercap.md)** | 改 MAC 后再做 ARP 投毒（减少被追踪）；ettercap 的输出里也有 MAC |
| **macchanger ↔ [bettercap](../05-无线攻击/bettercap.md)** | bettercap 的 `mac.changer` 模块提供等价功能 |
| **macchanger ↔ [wifite](../05-无线攻击/wifite.md)** | wifite 的 `-mac` 参数会随机化 MAC |
| **[airmon-ng](../05-无线攻击/airmon-ng.md)** | 无线侦察时会看到大量 MAC + 厂商信息 |

**⭐ 「MAC → 厂商 → 设备类型」的侦察用法**：

```bash
# 1) 看邻居的 MAC
ip neigh
# 192.168.1.10 dev eth0 lladdr b8:27:eb:aa:bb:cc REACHABLE

# 2) 反查厂商
macchanger -l | grep -i 'b827eb'
# 或直接看本地数据库

# 3) 判断设备类型
# b8:27:eb = Raspberry Pi Foundation
# 08:00:27 = VirtualBox
# 00:0c:29 = VMware
# 00:50:56 = VMware
# 52:54:00 = QEMU/KVM
# 00:16:3e = Xen
# 00:15:5d = Hyper-V
```

**⭐ 这份「虚拟化厂商 OUI 清单」在渗透测试中很有用**——它能让你一眼看出「这台主机是虚拟机还是物理机」，以及「用的是什么虚拟化平台」。

**虚拟化平台 OUI 速查**：

| OUI | 平台 |
| --- | --- |
| `00:05:69` / `00:0C:29` / `00:1C:14` / `00:50:56` | VMware |
| `08:00:27` | VirtualBox |
| `52:54:00` | QEMU/KVM |
| `00:16:3E` | Xen |
| `00:15:5D` | Microsoft Hyper-V |
| `AC:DE:48` | 随机的「私有地址」（RFC 规定） |
| `02:...` | 本地管理（通常是手动改过的） |

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| **`Can't change MAC: interface up`** | ⭐ 接口没有 down | `sudo ip link set eth0 down` → 改 → `up` |
| 改了但 `ip link` 显示旧值 | 接口层没重新初始化 | 确认执行了 `up`；必要时用 `ip link set eth0 down; ip link set eth0 up` |
| **改完上不了网** | ⭐ DHCP 租约基于旧 MAC | `sudo dhclient -r eth0 && sudo dhclient eth0`；或重连 NetworkManager |
| **改完 SSH 断开** | IP 变了（DHCP 重新分配） | 用 `tmux`/`nohup` 包裹命令；或下一次用新 IP 连 |
| **重启后又变回旧 MAC** | ⭐ 修改只作用于驱动层 | 用 NetworkManager `cloned-mac-address`（见场景 6） |
| `This device does not support changing MAC` | 驱动不支持 | 换网卡/驱动；虚拟机可能需要在 hypervisor 里允许 |
| 无线网卡改 MAC 后连不上 | AP 记住了旧 MAC，或有 MAC 过滤 | 正常（这是防御生效）；恢复原 MAC 或用白名单内的 MAC |
| `macchanger` 交互式提问卡住脚本 | 安装时的 debconf 提问 | `sudo dpkg-reconfigure macchanger`；脚本里用 `DEBIAN_FRONTEND=noninteractive` |
| 改成了组播地址导致不工作 | 第一个字节最低位为 1 | 用单播地址（第一个字节最低位为 0） |
| MAC 冲突（两台设备同 MAC） | 手工指定了别人在用的 MAC | ⚠️ **立即改掉**；用随机生成的更安全 |
| 虚拟机克隆后 MAC 冲突 | 克隆时复制了 MAC | ⭐ 在 hypervisor 里重新生成 MAC，或用 macchanger |
| `macchanger -p` 后仍不是出厂值 | 极少数驱动不支持读回 EEPROM | 手动设置回原值 |

**⭐ 一个和虚拟机相关的经典坑**：

> **克隆虚拟机后，两台虚拟机有相同的 MAC** → 网络冲突。
>
> **解决**：
> - VirtualBox：`VBoxManage modifyvm <vm> --macaddress1 auto`
> - VMware：编辑 `.vmx` 里的 `ethernet0.address` 为 `ethernet0.generatedAddress`
> - 或用 `macchanger -a` 手动随机化

**另一个常见问题**：

```bash
# macchanger 的 debconf 选了「开机自动随机化」，导致网络配置失效
# 检查
ls /etc/network/if-pre-up.d/macchanger 2>/dev/null

# 修复
sudo dpkg-reconfigure macchanger    # 选 No
```

## 9. 防御视角（蓝队）

**首先要明确一件事**：**MAC 欺骗不是一个漏洞——它是一个「身份标识不可信」的现实。**

> MAC 地址**从来没有被设计成安全边界**。它可以被轻易修改，而且现代操作系统**默认就在随机化它**。
>
> 因此：**任何依赖 MAC 做安全决策的机制都是不可靠的**。

### 9.1 攻击面与对策

| 依赖 MAC 的机制 | MAC 欺骗的效果 | 对策 |
| --- | --- | --- |
| **MAC 白名单**（路由器/AP） | ⚠️ **只要知道一个允许的 MAC 就能绕过** | ⭐ **不要用 MAC 白名单做安全控制**；用 802.1X |
| **MAC 过滤**（防火墙规则） | ⚠️ 绕过 | 用 IP+认证，不用 MAC |
| **NAC 基于 MAC 的准入** | ⚠️ 绕过 | ⭐ **用 802.1X（EAP-TLS）** |
| DHCP 的 MAC 保留 | 会拿到新 IP（不是安全问题，是运维麻烦） | 改用基于客户端标识的方式 |
| 网络监控的「设备追踪」 | ⚠️ 追踪失效 | 改用其他信号（行为分析、认证） |
| **公共 WiFi 的按时计费** | ⚠️ 可以重置计时 | 用账号认证 |
| 商家/广告商的跨网络追踪 | ✅ **被阻止（这是好事）** | — |

### 9.2 最重要的三条

```text
1. 不要用 MAC 白名单做安全控制
   → MAC 可以被任意修改，用它做访问控制是「安全剧场」
   → 正确做法：802.1X + EAP-TLS（每个设备独立证书）

2. 用 802.1X（EAP-TLS）代替 MAC 认证
   → 设备的身份由「私钥」证明，而不是「MAC」
   → 私钥无法被猜测或复制（除非设备被攻破）

3. 端口安全（Port Security）用于防泛洪/防交换机攻击，不用来授权
   → 它能限制一个端口的 MAC 数量（防 MAC 泛洪）
   → 但它不能证明「这个 MAC 是合法的」
```

**⭐ 一个关键的认知区别**：

| 机制 | 能防什么 | 不能防什么 |
| --- | --- | --- |
| **MAC 白名单** | 防「不知道白名单内容的人」 | ❌ 防不住「知道一个合法 MAC 的人」（MAC 是可以被观察到的！） |
| **端口安全** | 防 MAC 泛洪攻击、防一个端口接多设备 | ❌ 防不住改 MAC 绕过 |
| **802.1X（EAP-TLS）** | ⭐ **防住 MAC 欺骗**（认证基于私钥） | — |

**⭐ 为什么 MAC 白名单「看起来安全但实际不安全」**：

```
MAC 地址是明文的，而且会出现在：
  - 交换机的 CAM 表（网络里有权限的人能看到）
  - ARP 表（同网段所有人能看到）
  - Wi-Fi 的帧里（监听者能看到）
  - DHCP 请求里

→ 攻击者只要「观察一次」，就知道了所有合法设备的 MAC
→ 然后伪装成其中一个
```

**⭐ 所以「MAC 白名单」的防御强度约等于「把允许的 MAC 印在名片上发出去」。**

### 9.3 具体措施

**① 用 802.1X 代替 MAC 认证**

以 Cisco 交换机为例：

```text
! 启用 802.1X
aaa new-model
aaa authentication dot1x default group radius
aaa authorization network default group radius

dot1x system-auth-control

radius server ISE
 address ipv4 10.0.0.50 auth-port 1812 acct-port 1813
 key <共享密钥>

interface range GigabitEthernet0/1-24
 switchport mode access
 authentication port-control auto
 dot1x pae authenticator
 authentication host-mode multi-domain
 spanning-tree portfast
```

**⭐ 802.1X + EAP-TLS 的强度来自**：

| 要素 | 说明 |
| --- | --- |
| **客户端证书** | 每个设备一张，私钥不可导出（TPM） |
| **证书吊销** | 设备丢失/被盗时可以吊销 |
| **双向认证** | 服务器也要证明自己（防假认证服务器） |
| **无法伪造** | 攻击者没有私钥就无法通过 |

**② 如果必须用 MAC 相关机制（过渡期）**

```text
- 用 MAB（MAC Authentication Bypass）仅作为「过渡」或「打印机等哑设备」的兜底
- MAB 的 RADIUS 认证应该绑定到「端口 + MAC」而不是仅 MAC
- 定期审计 MAB 列表
- 明确文档化「MAB 是弱认证」
```

**⚠️ MAB（MAC Authentication Bypass）的问题**：

```
MAB 就是「用 MAC 做认证」的正式说法，本质仍然是「MAC 白名单」。
它存在的唯一理由是「哑设备（打印机、摄像头）不支持 802.1X」。

风险：
  - 攻击者可以伪装成打印机的 MAC
  - 打印机的位置通常端口隔离较差

缓解：
  - 把 MAB 设备放到独立的 VLAN
  - 严格限制该 VLAN 的访问
  - 绑定端口（同一个 MAC 只能出现在同一个端口）
```

**③ 端口安全（防泛洪，不是授权）**

```text
interface GigabitEthernet0/2
 switchport port-security
 switchport port-security maximum 3
 switchport port-security violation restrict
 switchport port-security mac-address sticky
```

**⭐ 端口安全的正确用途**：

| 用途 | 说明 |
| --- | --- |
| ✅ **防 MAC 泛洪攻击** | 限制一个端口的 MAC 数量，防止 CAM 表被撑爆 |
| ✅ **限制一个端口接入的设备数** | 防止一个端口插交换机接一堆设备 |
| ❌ **不用来「授权」** | sticky MAC 仍然可以被绕过（只是增加了观察难度） |

**④ 检测与监控**

| 检测点 | 方法 |
| --- | --- |
| **MAC 频繁变化** | ⭐ 监控同一端口/IP 的 MAC 变化频率 |
| **同一 MAC 出现在多个端口** | 端口安全的告警 / 交换机的 MAC 移动事件 |
| **OUI 异常** | 例如本应是 Dell 的设备突然变成 Apple 的 OUI |
| **虚拟化 OUI 出现在物理网段** | `08:00:27`（VirtualBox）出现在服务器网段 = 可疑 |
| **本地管理地址** | `02:` / `06:` / `0a:` 开头 = 被改过的 MAC（**注意：现代系统的隐私随机化也用这类地址，会有误报**） |
| **MAC 与 DHCP 记录不符** | 监控 DHCP 日志 |

**⭐ 检测脚本思路**：

```bash
#!/usr/bin/env bash
# 说明：监控本网段内的 MAC 变化（仅在你被授权监控的网络上运行）
# 需要 arpwatch 或类似工具
set -euo pipefail

LOG=/var/log/mac-watch.log
KNOWN=/var/lib/mac-watch/known-macs.txt

mkdir -p "$(dirname "$KNOWN")"
touch "$KNOWN"

while true; do
  ip neigh show | awk '/lladdr/{print $1, $5}' | while read -r ip mac; do
    if ! grep -q "^$ip $mac$" "$KNOWN"; then
      if grep -q "^$ip " "$KNOWN"; then
        OLD=$(grep "^$ip " "$KNOWN" | awk '{print $2}')
        echo "$(date -Is) ⚠️ MAC 变化: $ip  $OLD -> $mac" | tee -a "$LOG"
      else
        echo "$(date -Is) 新设备: $ip  $mac" | tee -a "$LOG"
      fi
      sed -i "/^$ip /d" "$KNOWN"
      echo "$ip $mac" >> "$KNOWN"
    fi
  done
  sleep 30
done
```

**⭐ 用现成工具更好**：

```bash
sudo apt install arpwatch
sudo arpwatch -i eth0
# 自动记录所有 MAC/IP 变化到 /var/lib/arpwatch/arp.dat
# 并可以配置邮件告警
```

**⑤ 关于「客户端 MAC 随机化」的两面性**

**现代系统的 MAC 随机化（iOS 14+ / Android 10+ / Windows 10+）对你的监控造成的影响**：

| 影响 | 说明 |
| --- | --- |
| ⚠️ 合法的设备追踪失效 | 日志里同一设备每次一个新 MAC |
| ⚠️ DHCP 记录混乱 | 大量「新设备」 |
| ✅ **但这是隐私保护的正确方向** | 不应该阻止 |
| ✅ 对「攻击者伪装 MAC」的检测也没影响 | 因为伪装从来不依赖随机化 |

**⭐ 企业环境的正确做法**：

```
1. 不要试图「禁用客户端的 MAC 随机化」（这会被视为侵犯隐私）
2. 用 802.1X 做认证（不依赖 MAC）
3. 用「稳定的随机 MAC」（如 Windows 的 per-network random）便于关联
4. 接受「MAC 不是身份」这个事实
```

**⑥ 一个务实的迁移路径**

```text
阶段 1（当前）：
  - 审计：有多少设备依赖 MAC 白名单/MAB？
  - 记录：哪些是真正需要 MAC 的（哑设备）

阶段 2：
  - 对支持 802.1X 的设备启用 802.1X + EAP-TLS
  - 把 MAB 设备移到独立的 VLAN，严格限制访问

阶段 3：
  - 消除所有「用 MAC 做安全控制」的地方
  - 只保留端口安全（防泛洪）
  - 认证全部基于「证书 + 用户」
```

### 9.4 一个容易被忽略的点

**MAC 欺骗最常见的「攻击」其实是最无害的那个**：

| 场景 | 性质 |
| --- | --- |
| 用户开启系统自带的 MAC 随机化 | ✅ **隐私保护，完全正当** |
| 用户用一个随机 MAC 连公共 WiFi | ✅ 正当 |
| **攻击者伪装成合法 MAC 绕过白名单** | ❌ **未授权访问** |
| **攻击者伪装 MAC 混淆溯源** | ❌ 妨碍调查 |

**⭐ 从蓝队角度**：

> **你无法区分「隐私保护」和「恶意伪装」**——两者在网络上看起来一样。
>
> **因此不要试图阻止 MAC 随机化**（那会伤害正常用户的隐私），而要：
> 1. **停止依赖 MAC 做安全决策**；
> 2. **用认证（802.1X）建立真正的信任**；
> 3. **监控异常模式**（同一端口的 MAC 频繁变化、OUI 异常、虚拟化 OUI 出现在物理网段）。

**⭐ 一句话总结**：

> **MAC 欺骗之所以有效，是因为有人把 MAC 当成了身份。**
> **修好这一点，MAC 欺骗就失去了大部分价值。**

## 10. 参考

- 官方仓库：<https://github.com/alobbs/macchanger>
- Kali 工具页：<https://www.kali.org/tools/macchanger/>
- 本机手册：`man macchanger`、`macchanger -h`
- IEEE OUI 查询（权威来源）：<https://standards-oui.ieee.org/oui/oui.txt>
- 相关 RFC：
  - RFC 7042（MAC 地址格式与 IANA 分配的字段）
  - 关于「本地管理地址」的规范
- NetworkManager 的 MAC 随机化：`man nm-settings`（查 `cloned-mac-address`）
- Kali 工具页（相关）：<https://www.kali.org/tools/ettercap/>、<https://www.kali.org/tools/bettercap/>
- 相关本目录：[ettercap](ettercap.md)、[wireshark](wireshark.md)、[tcpdump](tcpdump.md)、[responder](responder.md)、[mitmproxy](mitmproxy.md)
- 相关其他目录：[bettercap](../05-无线攻击/bettercap.md)、[wifite](../05-无线攻击/wifite.md)、[airmon-ng](../05-无线攻击/airmon-ng.md)

## ⚠️ 法律与伦理

**修改你自己设备的 MAC 是完全合法的**——这是隐私保护的标准做法，现代操作系统甚至默认就在做这件事。

**关键在于「你用它做什么」**：

| 行为 | 合法性 |
| --- | --- |
| ✅ **修改自己设备的 MAC 保护隐私** | **完全合法**（系统自带功能） |
| ✅ 在自己搭建的实验环境里测试 MAC 相关配置 | 合法 |
| ✅ 有**书面授权**的渗透测试中验证 MAC 过滤的有效性 | 合法 |
| ❌ **用伪造的 MAC 绕过他人的 MAC 白名单** | **未授权访问——违法** |
| ❌ **用伪造的 MAC 冒充他人设备** | 违法（可能构成诈骗） |
| ❌ **用伪造的 MAC 规避计费**（酒店、机场 WiFi） | 违法（可能构成盗窃/诈骗） |
| ❌ **用伪造的 MAC 妨碍安全事件调查** | 妨碍司法/毁灭证据 |

**特别说明「绕过 MAC 白名单」**：

> 很多人认为「我知道一个合法的 MAC，所以我连上了没问题」。
>
> **这是错的。** MAC 白名单是网络所有者设定的**访问控制措施**。绕过它 = **未授权访问**，无论你是否「知道那个 MAC」。
>
> 而且 MAC 地址是**明文可见的**——它从来不是一个秘密。所以「MAC 白名单」本质上是「凭观察就能通过的门」。

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条 | **非法侵入计算机信息系统罪** / **非法获取计算机信息系统数据罪** |
| 《刑法》 | 第二百八十六条 | 破坏计算机信息系统罪 |
| 《刑法》 | 第二百六十六条 | 诈骗罪（用假 MAC 骗取服务） |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《网络安全法》 | 第二十四条 | 网络运营者应要求用户提供真实身份信息（**说明 MAC 不是身份**） |
| 《个人信息保护法》 | 相关条款 | 用 MAC 追踪个人行踪涉及个人信息处理 |

**本教程仅适用于**：

- ✅ **修改你自己拥有的设备的 MAC**（隐私保护、测试）
- ✅ 你自己搭建的隔离实验环境
- ✅ 有**书面授权**的渗透测试（明确授权目标与范围）
- ✅ 分析你自己抓取的流量中的 MAC

**严禁**：

- ❌ 伪造 MAC 绕过任何非授权网络的访问控制
- ❌ 伪造 MAC 冒充他人设备
- ❌ 用伪造 MAC 规避计费或审计
- ❌ 用伪造 MAC 妨碍安全事件调查

**⭐ 一个实用建议**：

> 如果你只是想**保护隐私**（在公共 WiFi 上不被追踪），**直接用系统的内置 MAC 随机化功能**就够了：
> - iOS/Android/macOS：默认开启；
> - Windows：设置 → 网络 → Wi-Fi → 随机硬件地址 → 开启。
>
> **这不需要 macchanger，也不需要 root，而且更安全。**

**最后一句**：**MAC 从来不是身份，也不该被当成身份。** 无论你是在保护自己的隐私，还是在设计网络的访问控制，这句话都成立。
