# snort（网络入侵检测 / 防御系统）

> **一句话**：把网卡（或 pcap 文件）上的每一个包按规则集逐条匹配，命中就告警或丢弃——一台机器就能做「流量层 IDS/IPS」，是开源的 Snort/Suricata/Zeek 三巨头里规则生态最老牌的那个。
> **分类**：漏洞分析 / 网络流量检测（NIDS/NIPS）｜ **Kali 包**：`snort`（命令 `snort`，附带 `snort2lua`、`u2spewfoo`、`u2boat`、`show_flows`）｜ **官方文档**：<https://www.kali.org/tools/snort/> ｜ 上游：<https://www.snort.org>、<https://docs.snort.org>

---

## 1. 它解决什么问题

主机侧有 EDR/HIDS，但**流量侧**必须有独立的检测点，因为：

- 攻击流量在到达主机前就能被看见（**扫描、爆破、漏洞利用尝试、C2 回连**）；
- 主机日志可能被清理、被绕过，但**网络上的字节骗不了人**；
- 合规要求（等保、PCI-DSS）普遍要求网络层入侵检测。

Snort 承担的就是「网络层的规则引擎」：

| 需求 | Snort 的做法 |
|------|--------------|
| 「有人在扫我的端口」 | 端口扫描预处理器 / 规则匹配 SYN 特征 |
| 「有人在打这个漏洞」 | 用 payload 特征规则匹配 HTTP/其他协议的利用流量 |
| 「内网有主机在回连 C2」 | 匹配域名/URI/JA3 等特征 |
| 「我要阻断，不只是告警」 | IPS 模式（`-Q` + afpacket DAQ）inline 丢包 |
| 「我要事后复盘」 | pcap 模式（`-r`）离线重放，规则调优 |

**对比同类**：

| 工具 | 定位 | 差异 |
|------|------|------|
| **Snort** | 规则驱动 NIDS/NIPS | 规则生态最大（Talos 商业规则 + 社区规则）；单包匹配为主 |
| **Suricata** | 规则驱动 NIDS/NIPS + 文件提取 | 兼容 Snort 规则，多线程更好，生态更新；**新项目通常优先 Suricata** |
| **Zeek**（原 Bro） | **行为/协议日志分析** | 不做规则匹配，产结构化日志，适合「不知道找什么」时的探索；与 Snort 互补 |
| **Wireshark / tcpdump** | 抓包与人工分析 | 无人值守、无规则匹配能力；见 [`../07-嗅探与欺骗/wireshark.md`](../07-嗅探与欺骗/wireshark.md)、[`../07-嗅探与欺骗/tcpdump.md`](../07-嗅探与欺骗/tcpdump.md) |
| **YARA** | **文件/样本**特征匹配 | 扫的是磁盘上的文件，不是网络流；见 [`yara.md`](yara.md) |
| **Host-based（Lynis/Tiger）** | 主机配置审计 | 管系统和文件，不管流量；见 [`tiger.md`](tiger.md)、[`lynis.md`](lynis.md) |

> **Snort 2 vs Snort 3**：Kali 现在打包的是 **Snort 3**（`pkg.kali.org` 显示 `3.12.2.0`）。Snort 3 是**重写**：配置从 `snort.conf` 变成 **Lua**（`snort.lua`），命令行参数也有变化。**网上大量教程是 Snort 2 的，直接照抄会报错**。本文按 Snort 3 写。

---

## 2. 工作原理

Snort 3 的处理链路可以拆成五段：

```
                 ┌──────────────────────────────────────────┐
  网卡 / pcap ──►│ ① DAQ（Data Acquisition）                │
  stdin / socket │    pcap（默认）/ afpacket（IPS）/ hext…  │
                 └────────────────┬─────────────────────────┘
                                  ▼
                 ┌──────────────────────────────────────────┐
                 │ ② 解码器（Decoder）                      │
                 │    逐层解开 eth / ip / tcp / udp / icmp  │
                 │    → 生成「包 + 流」上下文                │
                 └────────────────┬─────────────────────────┘
                                  ▼
                 ┌──────────────────────────────────────────┐
                 │ ③ 预处理器 / Inspector                   │
                 │    stream：流重组（TCP 乱序、分片）      │
                 │    http_inspect / ftp / dns / smtp / ssh │
                 │    port_scan：扫描检测                   │
                 │    → 归一化后的「协议字段」              │
                 └────────────────┬─────────────────────────┘
                                  ▼
                 ┌──────────────────────────────────────────┐
                 │ ④ 规则引擎（检测）                        │
                 │    规则头：action proto src sport -> dst dport│
                 │    规则体：content/pcre/flow/byte_test…   │
                 │    fast_pattern 预筛 → 多模式匹配         │
                 └────────────────┬─────────────────────────┘
                                  ▼
                 ┌──────────────────────────────────────────┐
                 │ ⑤ 输出（Logger）                          │
                 │    -A alert_fast / alert_full / alert_json│
                 │       / alert_csv / cmg / unified2 …     │
                 │    → 控制台 / 文件 / syslog               │
                 └──────────────────────────────────────────┘
```

**关键概念**：

- **DAQ 决定「被动还是阻断」**：`pcap`（默认）= 只旁路监听（IDS）；`afpacket` + `-Q` = inline（IPS，可 `drop`）。
- **规则 = 规则头 + 规则体**：规则头决定「哪些包值得看」（协议/IP/端口/方向），规则体决定「什么样的内容算命中」。
- **`flow` 与流重组**：`flow:established,to_server` 这类关键字让规则只在已建立连接的上行包上匹配，**大幅降低误报**。
- **`fast_pattern`**：给规则里最「稀有」的那个 `content` 打上标记，Snort 用它做**预筛**（先多模式匹配，命中再跑其余条件）。**不加 fast_pattern 会让规则变慢且可能不准**（Snort 会自己挑一个，但挑得不一定对）。
- **内置规则（builtin rules）**：Snort 3 自带一批「用模块实现」的伪规则（如 `http_inspect` 的异常检测），可以用 `--lua 'ips = { enable_builtin_rules = true }'` 打开。
- **配置是 Lua**：`snort.lua` 里的 `HOME_NET`、`EXTERNAL_NET`、`ips = {}`、`alert_fast = {}` **都是 Lua 变量**，可以用 `--lua` 在命令行覆盖，不必改文件。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install snort
command -v snort snort2lua u2spewfoo
snort -V
```

```console
root@kali:~# snort -V
   ,,_     -*> Snort++ <*-
  o"  )~   Version 3.12.2.0
   ''''    By Martin Roesch & The Snort Team
           http://snort.org/contact#team
           Copyright (C) 2014-2026 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using DAQ version 3.0.19
           Using LuaJIT version 2.1.0-beta3
           Using LZMA version 5.6.4
```

> 实际 `-V` 输出因版本而异；**用 `-V` 确认版本，因为它决定了参数与配置格式（2 还是 3）**。

```bash
snort --help | head -40        # 概览
snort -?                       # 命令行选项速查（--help-options 等价）
snort --help-modules           # 列出所有模块
snort --help-module stream     # 看某个模块的说明
snort --help-config | grep -i home   # 搜配置项
```

**Kali 打包后关键路径**：

| 路径 | 内容 |
|------|------|
| `/etc/snort/snort.lua` | **主配置**（Snort 3 的 Lua 配置） |
| `/etc/snort/snort_defaults.lua` | 默认变量（`HOME_NET`、规则路径等） |
| `/etc/snort/rules/` | 规则文件目录（`snort-rules-default` 提供社区规则） |
| `/etc/snort/snort.conf` | **Snort 2 遗留**，Snort 3 不用它（用 `snort2lua` 转换） |

**验证配置能否加载**（本机没装 snort 时也可照此核对路径）：

```bash
sudo snort -c /etc/snort/snort.lua -T
```

```console
...
Snort successfully validated the configuration (with 0 warnings).
o")~   Snort exiting
```

```bash
# 用一个小 pcap 快速跑一遍 IDS（先自己抓一段无害流量）
sudo tcpdump -i any -w /tmp/demo.pcap -c 200 &
sudo snort -c /etc/snort/snort.lua -r /tmp/demo.pcap -A alert_fast
```

**三种运行模式要记住**：

| 模式 | 命令骨架 | 用途 |
|------|----------|------|
| **嗅探（sniffer）** | `snort -r f.pcap -L dump -d -e` | 把包打印出来看 |
| **记录（logger）** | `snort -r f.pcap -L pcap -l /dir` 或 `-A unified2` | 落盘存证 |
| **IDS/IPS** | `snort -c snort.lua -r f.pcap -A alert_fast`（IDS）/ `-Q --daq afpacket -i "eth0:eth1"`（IPS） | 检测/阻断 |

---

## 4. 核心参数详解

> 以下选项取自 Snort 3 上游 `src/main/snort_module.cc` 的参数表与 `doc/user/usage.txt`（Snort 3.12.x）。

### 4.1 配置与规则

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-c <conf>` | 指定主配置（Lua） | **必加**；Kali 上是 `/etc/snort/snort.lua` |
| `-T` | **测试配置并退出** | **改配置/规则后第一件事**；不加它直接跑会「报错在运行时」 |
| `-R <rules>` | 把规则文件加入默认策略 | 自写规则常用（`-R /tmp/local.rules`） |
| `--rule "<text>"` | 直接在命令行给规则文本 | 临时验证单条规则，**可重复多次** |
| `--stdin-rules` | 从 stdin 读规则直到 EOF 或 `END` | 脚本化、管道测试 |
| `--lua "<chunk>"` | 用 Lua 片段**覆盖/扩展配置** | **不改文件做实验**：`--lua 'ips = { enable_builtin_rules = true }'`，可重复 |
| `--warn-all` | 打开所有警告 | 排错时开，能暴露规则/配置隐患 |
| `--pedantic`（`-x`） | 警告升级为致命错误 | CI / 上线前严格校验 |
| `--rule-path <path>` | 规则文件搜索路径 | 分隔多个目录 |
| `-C` | 打印配置后退出 | 确认「最终生效的配置长什么样」 |
| `--dump-config all\|top` | 以 **JSON** 导出配置 | 审计/比对 |
| `--dump-config-text` | 以文本导出配置 | 人读 |
| `--dump-defaults [prefix]` | 导出模块默认值（Lua 格式） | 写配置的参考 |
| `--script-path <path>` | LuaJIT 脚本路径 | 用 Lua 规则选项扩展 |
| `--plugin-path <path>` | 插件目录（冒号分隔） | 加载 snort_extra 的 `alert_ex` 等 |

### 4.2 输入源（DAQ）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-i <iface>...` | 监听接口列表 | 多接口写在一个字符串里：`-i "eth0 eth1"` |
| `-r <pcap>` | 读 pcap（等价 `--pcap-list`） | **离线调规则的标准做法** |
| `--pcap-dir <dir>` | 递归读目录下所有 pcap | 批量复盘 |
| `--pcap-filter '*.pcap'` | 配 `--pcap-dir` 的文件过滤 | 只读某类 |
| `--pcap-show` | 打印当前正在读哪个 pcap | 批量时定位 |
| `--pcap-loop <n>` | 重复读 n 次（0=直到终止） | 循环压测规则性能 |
| `--daq <type>` | 选 DAQ：`pcap`/`afpacket`/`hext`/`file`/`socket` | **IPS 用 afpacket**；无网卡环境用 `hext` |
| `--daq-mode passive\|inline\|read-file` | 强制 DAQ 工作模式 | 一般自动推断，特殊场景手指定 |
| `--daq-var name=value` | DAQ 扩展参数 | 如 `--daq-var dlt=1` |
| `--bpf "<filter>"` | **BPF 过滤**（tcpdump 语法） | **第一道降载手段**：只把关心的流量喂给 Snort |
| `-n <count>` | 处理 count 个包后停止 | 快速冒烟测试 |
| `-s <snap>` / `--snaplen` | snaplen（默认 1518） | 要匹配大 payload 时调大 |
| `-k <mode>` | 校验和模式 `all\|noip\|notcp\|noudp\|noicmp\|none` | **虚拟机/网卡 offload 环境必须用 `-k none`**，否则包被误判丢弃 |

### 4.3 输出与告警

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-A <mode>` | **告警模式**：`none` / `cmg` / `alert_fast` / `alert_full` / `alert_json` / `alert_csv` / `unified2` … | 人看用 `alert_fast`；进 SIEM 用 `alert_json` 或 `unified2` |
| `-L <mode>` | 日志模式：`none` / `dump` / `pcap` / `log_*` | 想看包内容用 `-L dump`；存包用 `-L pcap` |
| `-d` | dump 应用层数据 | 与 `-L dump` 搭配 |
| `-e` | 显示二层头 | 与 `-L dump` 搭配 |
| `-X` | 从链路层开始 dump 原始包数据 | 需要看完整帧时 |
| `-l <logdir>` | 日志目录 | 默认当前目录，建议显式指定 |
| `-q` | 静默（不打印正常日志） | 脚本化；**注意别把错误也吞了** |
| `-v` | verbose | 调试 |
| `-O` | **混淆告警里的 IP** | 演示/对外分享时保护隐私 |
| `-B <mask>`（默认 `255.255.255.255/32`） | 用 CIDR 掩码混淆 IP | 更彻底脱敏 |
| `-M` | 日志消息进 syslog（**不是告警**） | 与系统日志统一管理 |
| `-U` / `-y` | 时间戳用 UTC / 带上年份 | 取证**强烈建议加**（跨时区、跨年不出错） |
| `--id-subdir` / `--run-prefix` | 多线程时按线程号建子目录/加前缀 | 多线程落盘防覆盖 |

### 4.4 运行控制

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-Q` | **inline（IPS）模式** | 配合 `--daq afpacket -i "eth0:eth1"`；此时 `drop` 动作才生效 |
| `-z <count>` / `--max-packet-threads` | 最大包处理线程数（0=按 CPU 核数） | 多队列网卡下必须配合 DAQ 设置 |
| `-D` | 后台守护进程模式 | 生产环境 |
| `-u <user>` / `-g <group>` | 初始化后降权运行 | **生产必加**（降权减小被攻破后果） |
| `-t <dir>` | chroot | 生产加固 |
| `--create-pidfile` | 创建 PID 文件 | 配合 systemd/脚本管理 |
| `--pause` | 启动后暂停，等 `resume()` | 交互调试 |
| `--plugin-path` + `-A alert_ex` | 用外部插件告警 | 演示插件机制 |
| `-?` / `--help-options` | 命令行选项帮助 | 忘了参数就查它 |

### 4.5 规则语法（Snort 3）

**骨架**：

```snort
action protocol src_ip src_port direction dst_ip dst_port ( option; option; ... )
```

```snort
alert tcp $EXTERNAL_NET 80 -> $HOME_NET any
(
    msg:"Attack attempt!";
    flow:to_client,established;
    file_data;
    content:"1337 hackz 1337",fast_pattern,nocase;
    service:http;
    sid:1;
)
```

| 部分 | 取值 | 说明 |
|------|------|------|
| `action` | `alert` / `log` / `pass` / `drop` / `reject` / `block` | `drop`/`reject` **仅 inline（`-Q`）有效** |
| `protocol` | `tcp` / `udp` / `icmp` / `ip` / `http` / `dns` … | Snort 3 支持**服务名**（如 `http`），更易读 |
| `src_ip` / `dst_ip` | `any` / IP / CIDR / `$HOME_NET` / `[a,b]` / `!x` | 变量在 `snort.lua` 里定义 |
| `direction` | `->`（单向）/ `<>`（双向） | `<>` 慎用，性能与误报都差 |
| `src_port` / `dst_port` | `any` / 具体端口 / `[80,443]` / `!80` | —— |

**常用规则选项**：

| 选项 | 作用 | 建议 |
|------|------|------|
| `msg:"..."` | 告警文本 | 必写，写清「命中了什么」 |
| `sid:<n>` | **规则唯一 ID** | **自定义规则用 ≥ 1000000**（避免与官方规则冲突） |
| `rev:<n>` | 修订号 | 改规则就 +1 |
| `gid:<n>` | 生成器 ID | 默认 1（文本规则）；自定义一般不改 |
| `content:"..."` | 匹配 payload 字节串 | **最核心的匹配原语**；用 `\|XX\|` 表示十六进制字节 |
| `nocase` | 大小写无关 | 文本协议常用 |
| `depth` / `offset` | 限定从包/距离起点起 N 字节内匹配 | 精确控制匹配位置 |
| `distance` / `within` | 相对上一个 content 的位置约束 | 构造「字段顺序」特征 |
| `fast_pattern` | 把该 content 作为预筛锚点 | 多 content 规则**必加**，性能关键 |
| `flow:to_server,established` | 只看「已建立连接、发往服务端」的包 | **降误报最有效的选项** |
| `flowbits:set,x` / `isset,x` | 跨包状态机 | 做多步攻击链检测 |
| `pcre:"/regex/imx"` | 正则匹配 | 灵活但**慢**，能不用就不用 |
| `byte_test` / `byte_jump` | 二进制字段比较/跳转 | 检测协议长度/版本字段 |
| `service:http` | 声明规则适用的服务 | Snort 3 用它提升匹配效率 |
| `classtype:<class>` | 规则分类 | 影响优先级与告警归类 |
| `reference:<system>,<id>` | 关联 CVE/Bugtraq/url | **报告与溯源必备** |
| `metadata:` | 任意键值元数据 | 如 `metadata:service http;` |
| `priority:<n>` | 优先级 | 决定告警排序 |

**注释**：`#` 单行注释，`/* ... */` 行内或多行注释。

**Snort 3 相对 Snort 2 的规则差异（重要）**：

- **不需要转义换行**：Snort 3 忽略规则里的多余空白，**不再要求行尾 `\` 续行**；规则可以跨行写得很整齐。
- **服务感知**：可以直接用 `http` 作为协议、用 `service:` 限定。
- **规则头也参与优化**：Snort 3 会把 IP/端口条件编进匹配树。

---

## 5. 实战演练

> **环境声明**：以下全部在**你自己的机器/自建靶机/自建 pcap**上做。
> - **只听不做**：`snort -i <iface>` 是**只读旁路**，不修改流量；
> - **IPS（`-Q` + afpacket）会改流量**，**绝不能在别人的网络上做**，企业内部部署也需变更审批；
> - **不要**把公司网络的 pcap 外带或公开（含内部 IP、URL、凭据）；
> - 本文所有示例使用**自造 pcap**（用 `tcpdump` 抓自己的 loopback 或 `hext` DAQ 生成）。

### 场景 1：三种模式跑同一个 pcap（嗅探 → 记录 → 检测）

```bash
# 造一段无害流量：本机循环访问一个本地 HTTP 服务
python3 -m http.server 8000 &
curl -s http://127.0.0.1:8000/ >/dev/null
sudo tcpdump -i lo -w /tmp/demo.pcap -c 100 port 8000
ls -l /tmp/demo.pcap
```

**① 嗅探模式（把包打出来看）**

```bash
snort -r /tmp/demo.pcap -L dump -d -e -n 5
```

```console
root@kali:~# snort -r /tmp/demo.pcap -L dump -d -e -n 5
...
06/15-10:02:31.918441 001:02:00:00:00:00 -> 001:02:00:00:00:01 type:0x800 len:0x4E
127.0.0.1:52344 -> 127.0.0.1:8000 TCP TTL:64 TOS:0x0 ID:0 IpLen:20 DgmLen:64 DF
*******A* Seq: 0x...  Ack: 0x...  Win: 0x1000  TcpLen: 32
TCP Options (3) => NOP NOP TS: ...
```

**解读**：`-L dump` 输出的是「人类可读的包摘要」，`-d` 加了应用层数据、`-e` 加了二层头。这就是 Snort 的**嗅探模式**——功能上等价于 `tcpdump -e -X` 的精简版。

**② 记录模式（落盘存证）**

```bash
mkdir -p /tmp/snort-logs
snort -r /tmp/demo.pcap -L pcap -l /tmp/snort-logs -U
ls -l /tmp/snort-logs/
```

```console
root@kali:~# ls -l /tmp/snort-logs/
-rw-r--r-- 1 root root  ...  snort.log.20260915100231
```

**解读**：`-L pcap` 把**原始包**写盘（可再被 Wireshark/Snort 二次分析），`-U` 用 UTC 时间戳。**取证场景一定加 `-U`**，否则跨时区/跨年对不上。

**③ IDS 模式（规则匹配）**

```bash
# 先写一条「本地自定义规则」：任何到 8000 端口、payload 含 GET 的包就告警
cat > /tmp/local.rules <<'EOF'
alert tcp any any -> any 8000 (
    msg:"LOCAL test - HTTP GET to port 8000";
    flow:to_server,established;
    content:"GET",fast_pattern,nocase;
    service:http;
    classtype:not-suspicious;
    reference:url,example.com/local-rule;
    sid:1000001;
    rev:1;
)
EOF

# 先校验配置+规则
sudo snort -c /etc/snort/snort.lua -R /tmp/local.rules -T
```

```console
Snort successfully validated the configuration (with 0 warnings).
o")~   Snort exiting
```

```bash
# 跑离线检测，告警打到控制台
sudo snort -c /etc/snort/snort.lua -R /tmp/local.rules -r /tmp/demo.pcap -A alert_fast -k none -q
```

```console
06/15-10:02:31.918441 [**] [1:1000001:1] "LOCAL test - HTTP GET to port 8000" [**] [Classification: Not Suspicious Traffic] [Priority: 3] {TCP} 127.0.0.1:52344 -> 127.0.0.1:8000
06/15-10:02:31.919002 [**] [1:1000001:1] "LOCAL test - HTTP GET to port 8000" [**] [Classification: Not Suspicious Traffic] [Priority: 3] {TCP} 127.0.0.1:52344 -> 127.0.0.1:8000
```

**解读（`alert_fast` 每行格式）**：

```
时间戳  [**] [gid:sid:rev] "msg" [**] [分类] [优先级] {协议} 源IP:端口 -> 目的IP:端口
  │            │                     │        │        │
  │            │                     │        │        └─ 命中的连接五元组
  │            │                     │        └─ classtype/priority
  │            │                     └─ 规则分类（classtype）
  │            └─ **gid:sid:rev** —— 定位规则的唯一坐标
  └─ UTC 时间戳（因为加了 -U）
```

**`gid:sid:rev` 是排错的第一入口**：拿它去规则文件里 `grep sid:1000001` 就能找到这条规则。

### 场景 2：写一条「像样」的检测规则并做误报调优

**2a. 先用 `--rule` 在命令行快速验证规则语法**（不用建文件）：

```bash
sudo snort -c /etc/snort/snort.lua \
  --rule 'alert tcp any any -> any 22 ( msg:"LOCAL ssh brute force single pkt"; flow:to_server,established; content:"SSH-2.0-",fast_pattern; sid:1000002; rev:1; )' \
  -r /tmp/demo.pcap -A alert_fast -q
```

**2b. 用 BPF 降载 + 用 flow 降误报**

```bash
# 只把 22 端口流量喂给 snort（BPF 做第一层过滤），且规则只在「已建立连接的上行方向」匹配
sudo snort -c /etc/snort/snort.lua -R /tmp/local.rules \
  --bpf "port 22 or port 8000" \
  -r /tmp/demo.pcap -A alert_json -k none 2>/dev/null | head -3
```

```console
{ "timestamp" : "2026-06-15T10:02:31.918441+0000", "gid" : 1, "sid" : 1000001, "rev" : 1,
  "msg" : "LOCAL test - HTTP GET to port 8000", "proto" : "TCP",
  "src_addr" : "127.0.0.1", "src_port" : 52344, "dst_addr" : "127.0.0.1", "dst_port" : 8000,
  "eth_len" : 14, "tcp_len" : 32, "pkt_num" : 3, "action" : "allow", "class" : "Not Suspicious Traffic", "priority" : 3 }
```

**解读**：`-A alert_json` 出的 JSON **可以直接进 Elasticsearch/SIEM/日志平台**。字段含义：

| 字段 | 含义 |
|------|------|
| `gid`/`sid`/`rev` | 规则坐标 |
| `msg` | 规则描述 |
| `proto`/`src_*`/`dst_*` | 命中流量的五元组 |
| `pkt_num` | 在输入流中的包序号（配合 pcap 定位） |
| `action` | `allow`（alert 规则在 IDS 模式下的动作） |
| `class`/`priority` | 分类与优先级 |

**2c. 误报调优的基本手法**

```bash
# 问题：某条规则刷屏
# ① 定位规则
grep -rn "sid:1000001" /tmp/local.rules

# ② 缩小匹配面：加 offset/depth 限定字段位置，或加 flow 限定方向
#    改前（太宽）:
#      content:"GET",fast_pattern,nocase;
#    改后（只匹配请求行开头的 GET）:
#      content:"GET",fast_pattern,nocase,depth:4,offset:0;

# ③ 或者直接抑制（suppress）——不改规则，只压告警
echo 'suppress = { { gid = 1, sid = 1000001, track = "by_src", ip = "127.0.0.1" } }' >> /tmp/suppress.lua
sudo snort -c /etc/snort/snort.lua -R /tmp/local.rules \
  --lua "$(cat /tmp/suppress.lua)" -r /tmp/demo.pcap -A alert_fast -q
# 结果：来自 127.0.0.1 的该 sid 告警不再输出，其他源仍告警
```

**解读**：**「抑制」比「删规则」更专业**——规则本体保留（能力还在），只针对已知 benign 的来源/目标压低噪音。生产环境的标准做法是 `threshold`/`suppress`/`rate_filter` 三件套。

**2d. 上线前的严格校验（CI 里跑）**

```bash
sudo snort -c /etc/snort/snort.lua -R /tmp/local.rules -T --warn-all --pedantic
```

```console
# --pedantic 把警告变成错误：有任何警告都会非 0 退出
```

**解读**：把这一行放进 CI，**规则写错就会拦住合并**。这是把 NIDS 规则当代码管理的起点。

### 场景 3：只有 pcap、没有网卡也能测——hext DAQ 与目录批处理

**3a. 用 `hext` DAQ 从 stdin 造包**（不需要网卡、不需要 pcap 文件，非常适合教学与 CI）

```bash
sudo snort -c /etc/snort/snort.lua -R /tmp/local.rules -A alert_fast -q \
  --daq-dir /usr/lib/snort/daqs --daq hext -i tty << 'END'
$packet 127.0.0.1 52344 -> 127.0.0.1 8000
"GET / HTTP/1.1\r\n"
"Host: localhost\r\n"
"\r\n"
END
```

**解读**：`--daq hext` 让你用**文本语法直接描述一个包**（`$packet 源IP 源端口 -> 目的IP 目的端口`，后面是 payload 字节串）。这是**验证单条规则的最快方式**：不用抓包、不用网卡、不用建 pcap 文件。

**3b. 批量复盘一个目录的 pcap**

```bash
sudo snort -c /etc/snort/snort.lua -R /tmp/local.rules \
  --pcap-dir /tmp/pcaps --pcap-filter '*.pcap' --pcap-show \
  -z 4 -A unified2 -l /var/log/snort --id-subdir -U
ls /var/log/snort/
```

```console
root@kali:~# ls /var/log/snort/
0/  1/  2/  3/
```
用 `u2spewfoo` 把 unified2 二进制事件转成可读文本：

```bash
u2spewfoo /var/log/snort/0/snort.log.* | head -20
```

```console
(Event)
         sensor id: 0    event id: 4  event second: 1781000000   event microsecond: 146591
         sig id: 1000001 gen id: 1   revision: 1  classification: 0
         priority: 3 ip source: 127.0.0.1 ip destination: 127.0.0.1
         src port: 52344 dest port: 8000 protocol: 6 impact_flag: 0  blocked: 0
Packet
         ...
```

**解读**：`--pcap-dir` + `-z 4` 是**回放历史流量的主力手段**——把「上个月的抓包」按新规则重跑，验证规则效果。`unified2` 是 Snort 的二进制事件格式，**`u2spewfoo` 是它的读工具**（也可直接被某些 SIEM 采集器解析）。

**与 Snort 2 配置迁移**（Kali 里带了 `snort2lua`）：

```bash
snort2lua -c /etc/snort/snort.conf -o /tmp/snort3-from-snort2.lua
sudo snort -c /tmp/snort3-from-snort2.lua -T
```

**解读**：如果你有老的 Snort 2 部署，`snort2lua` 能把 `snort.conf` 转成 Lua。**转换结果需要人工复核**（部分模块参数无一对一映射），转换后必须 `-T` 验证。

---

## 6. 输出解读

### 6.1 告警行的结构（`-A alert_fast`）

```
[TIMESTAMP] [**] [gid:sid:rev] "message" [**] [Classification: <class>] [Priority: <n>] {PROTO} src:sport -> dst:dport
```

| 位置 | 含义 | 下一步动作 |
|------|------|------------|
| 时间戳 | 事件时间（`-U` 为 UTC） | 与主机日志对齐做时间线 |
| `gid:sid:rev` | 规则坐标 | `grep` 定位规则 → 判断真/误报 |
| `message` | 规则语义 | 直接就是告警说明 |
| `Classification` | 分类（classtype） | 决定响应等级 |
| `Priority` | 优先级（越小越紧急） | 排序处理 |
| 五元组 | 命中连接 | 定位资产、查内网归属 |

### 6.2 不同 `-A` 模式怎么选

| 模式 | 形态 | 适用 |
|------|------|------|
| `alert_fast` | 一行一条 | 交互调试、看控制台 |
| `alert_full` | 多行，含包头 | 详细分析 |
| `alert_json` | JSON | **进 SIEM / 日志平台** |
| `alert_csv` | 逗号分隔 | 表格/脚本处理 |
| `cmg` | 紧凑格式 | 配合 `1>out 2>err 3>log` 分流 |
| `unified2` | **二进制** | 长时间留存、给 SIEM 采集器、配 `u2spewfoo` 读 |
| `none` | 不告警 | 只做 `-L` 记录/性能测试 |

### 6.3 怎么看「这次有没有检出」

| 观察 | 结论 |
|------|------|
| 一条告警都没有 | 要么流量本身干净，要么**规则没生效**（`-R` 没加？`sid` 冲突？`-T` 有报错？先用 `--rule` 单条验证） |
| 同一 `sid` 刷屏 | **误报**：加 `flow`/`depth`/`offset` 收紧，或用 `suppress` 压制 |
| 告警在但没抓到包 | 检查 `-k none`（校验和 offload 导致的丢包）与 BPF 是否过滤掉了 |
| 期望的规则没命中 | 用 `-d -e` 看实际包内容，确认 payload 与 `content` 是否真的匹配（大小写/编码/分片/流重组） |
| 性能告警（丢包） | 看启动时打印的 `Packet Statistics`；加 `-z`（更多线程）或加 BPF 降载 |

---

## 7. 与其他工具配合

```
                    ┌───────────────────────────────────────────┐
 抓包/流量源 ──────► │ tcpdump / dumpcap  →  pcap               │
 (或网卡旁路)        │ 见 07-嗅探与欺骗/tcpdump.md、wireshark.md │
                    └────────────────┬──────────────────────────┘
                                     ▼
                              snort -r x.pcap -A ...
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        ▼                            ▼                            ▼
  告警 → SIEM                 原始包 → Wireshark           文件落盘 → YARA
  (alert_json/unified2)       逐包验证规则为何命中        (stream 抓文件)
        │                            │                            │
        └─► 与主机日志关联 ◄─ Tiger/Lynis 主机审计 ──► 应急响应时间线
```

- **流量抓取**：[`../07-嗅探与欺骗/tcpdump.md`](../07-嗅探与欺骗/tcpdump.md)（离线抓包）、[`../07-嗅探与欺骗/wireshark.md`](../07-嗅探与欺骗/wireshark.md)（图形化逐包分析）
- **样本侧检测**：[`yara.md`](yara.md) —— Snort 管**流量特征**，YARA 管**文件特征**，两者常配对部署
- **主机侧审计**：[`tiger.md`](tiger.md)、[`lynis.md`](lynis.md) —— 网络 + 主机双向覆盖
- **漏洞面验证**：[`nuclei.md`](nuclei.md) 主动扫漏洞 → 用 Snort 看「扫描流量长什么样」，反向写检测规则
- **配置迁移**：`snort2lua`（Snort 2 → 3）
- **事件读取**：`u2spewfoo`（unified2 → 文本）

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `ERROR: ... unknown option` / 配置加载失败 | **照抄了 Snort 2 教程**（`-c snort.conf`、`-D`、`-A console` 等已变） | 用 `snort -V` 确认是 3.x；查 `snort --help-options`；配置改成 Lua |
| 一条告警都没有 | `-R` 没加（自写规则没加载）／`sid` 与已有规则冲突／配置里 `ips` 未启用 | 加 `-R`；自定义规则用 `sid >= 1000000`；`-T` 看警告 |
| **配置校验通过但运行时无检测** | 配置 `-T` 通过 ≠ 规则已加载 | 用 `--dump-rule-meta` 或 `-C` 确认规则在最终配置里 |
| 虚拟机里大量丢包/告警异常 | **网卡校验和 offload** 让包校验和「看起来错误」 | **加 `-k none`**（最常见的坑） |
| 规则不命中但 Wireshark 里明明有 | payload 被分片/乱序，或大小写、编码（URL 编码/UTF-16）不同 | 开 `stream`（默认有）；用 `nocase`；看归一化后内容（`http_inspect`）；必要时 `pcre` |
| `fast_pattern` 报错「more than one」 | 一条规则只能有一个 `fast_pattern` | 只给最稀有的那个 content 加 |
| 自定义 `sid` 报冲突 | sid 落在官方规则区间 | **自定义规则统一用 1000000 以上** |
| IPS 模式 `drop` 不生效 | 没开 `-Q` 或 DAQ 不是 inline | `-Q --daq afpacket -i "eth0:eth1"` |
| `drop`/`reject` 在离线 pcap 模式下无意义 | 离线无「丢包」动作可执行 | 离线只验证「能检出」，阻断要在 inline 部署验证 |
| 告警时间与本地时钟对不上 | 默认是本地时间/缺年份 | 加 `-U`（UTC）；`-y` 带年份 |
| 多线程日志互相覆盖 | 文件名不含线程号 | 加 `--id-subdir` 或 `--run-prefix` |
| 规则数量大后性能崩 | 缺 `fast_pattern`、用大量 `pcre`、`<>` 双向规则 | 加 `fast_pattern`、少用 `pcre`、避免 `<>`；加 `--bpf` 降载 |
| `--help-*` 之后的选项「不生效」 | **`--help-*`/`--list-*` 会抢占后续处理** | 把这类选项放在命令行**最后** |
| 起不来：端口/权限 | 非 root 抓包、接口不存在、afpacket 需要 `CAP_NET_RAW` | `sudo` 运行；`ip link` 确认接口名 |

---

## 9. 防御视角（蓝队）

Snort 本身就是蓝队工具，但「装上去」离「有用」还有三步：**规则质量、降噪、闭环**。

| 场景 | 做法 | 价值 |
|------|------|------|
| 边界检测 | inline 部署 + `-Q`，对明确恶意特征用 `drop` | 直接阻断已知攻击 |
| 内网横向检测 | 在核心交换机镜像口旁路部署，重点看 SMB/RDP/SSH/OA 端口 | 发现横向移动 |
| C2 回连检测 | 匹配已知 C2 URI/UA/JA3 + 用 `metadata` 管理 | 发现失陷主机 |
| 规则治理 | 用 `suppress`/`threshold`/`rate_filter` 降噪；定期看「哪个 sid 最吵」 | **降噪是 NIDS 成败的核心** |
| 变更验证 | `--pedantic` 进 CI，规则变更走代码评审 | 规则即代码 |
| 流量留存 | `-A unified2` + 轮转 + `u2spewfoo` 检索 | 事后取证 |
| 审计合规 | 保留告警与配置快照 | 等保/PCI 证据链 |

**蓝队的五条硬建议**：

1. **先降噪再谈检出**：一个每天出 10 万条误报的 NIDS 等于没有——`suppress`/`threshold` 优先级高于加新规则；
2. **规则要有 `reference`**：每条规则关联 CVE/公告，否则半年后没人知道它在防什么；
3. **BPF 是第一道门**：用 `--bpf` 只喂关心的流量，比堆硬件便宜；
4. **校验和 offload 是虚拟机环境的最大坑**：部署脚本里固化 `-k none`；
5. **IPS 部署要谨慎**：`drop` 一个误报规则等于「自己给自己断网」，必须灰度 + 可快速回滚。

**应急响应中的用法**：

```bash
# 事件后用当时留存的全流量 pcap 跑最新规则集，重建攻击时间线
sudo snort -c /etc/snort/snort.lua -R /etc/snort/rules/local.rules \
  --pcap-dir /evidence/pcaps --pcap-filter '*.pcap' \
  -A alert_json -l /evidence/snort-out -U --id-subdir
# 把告警时间线与主机日志（syslog/auth.log）对齐
```

**注意**：全流量留存涉及**员工通信内容**，需在合规框架内（明示告知、访问控制、留存期限制）进行。

---

## 10. 参考

- Kali 工具页（含 `snort -h` 与 `u2spewfoo` man 摘要）：<https://www.kali.org/tools/snort/>
- Kali 包跟踪（版本 `3.12.2.0`）：<https://pkg.kali.org/pkg/snort>
- Snort 3 官方文档：<https://docs.snort.org>
- 官方命令行用法（`usage.txt`）：<https://github.com/snort3/snort3/blob/master/doc/user/usage.txt>
- 命令行选项定义（权威参数表）：<https://github.com/snort3/snort3/blob/master/src/main/snort_module.cc>
- 规则语法：<https://docs.snort.org/rules/>
- 本地命令：`snort -V`、`snort -?`、`snort --help-modules`、`snort --help-config | grep <x>`、`man u2spewfoo`、`man snort2lua`
- 配套教程：[`yara.md`](yara.md)、[`tiger.md`](tiger.md)、[`../07-嗅探与欺骗/tcpdump.md`](../07-嗅探与欺骗/tcpdump.md)

## ⚠️ 法律与伦理

Snort 是**双用途**工具——它既能防护，也是攻击者用来「测试自己 payload 能否被检测」的工具。

- **被动监听的风险**：在**非自有网络**上抓包/监听，可能违反《网络安全法》第 27 条（不得从事非法侵入、干扰他人网络的活动）与《刑法》第 285/286 条；
- **IPS 会修改流量**：inline 丢包属于**主动干扰**，未经授权在他人网络上部署 `drop` 规则可能构成破坏计算机信息系统（《刑法》第 286 条）；
- **内容留存涉及通信秘密**：全流量留存可能触及《宪法》第 40 条（通信自由与通信秘密）、《个人信息保护法》《数据安全法》，需合法授权与合规流程；
- **规则可被反向利用**：攻击者可以用 Snort 测「我的流量会不会被检测」以做规避——这属于**研究和防御测试**范畴，但**不得用于规避他人的安全检测去实施攻击**。

**必须遵守**：

1. **只监听你有权管理的网络**：自己的实验环境、自建靶场、获得书面授权的企业网络；
2. **IPS（`-Q` + `drop`）必须先有变更授权**，并准备回滚方案；
3. **不公开未脱敏的 pcap/告警**（用 `-O`/`-B` 混淆 IP，删除 payload）；涉及内部信息的材料不得外带；
4. **全流量留存**需明示告知、限定留存期、严格访问控制；
5. **不要把 Snort 用于「检测他人网络」**——即使网络是开放的（如酒店 Wi-Fi），监听他人通信仍可能违法；
6. **规则编写与测试**只在自己的环境里做。
