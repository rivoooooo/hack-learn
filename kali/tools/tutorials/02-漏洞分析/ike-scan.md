# ike-scan（IPsec VPN / IKE 服务发现与指纹）

> **一句话**：向目标发 IKE Phase-1 请求，发现哪些主机在跑 IPsec VPN、用的是什么实现，并从 Aggressive Mode 响应中拿到可用于离线爆破的预共享密钥参数。
> **分类**：漏洞分析 ｜ **Kali 包**：`ike-scan` ｜ **官方文档**：<https://github.com/royhills/ike-scan>

## 1. 它解决什么问题

IPsec VPN 是很多组织唯一的"远程入口"。但与 HTTP/SSH 不同，**IKE 跑在 UDP 500/4500 上，没有 banner，扫描器也很难识别**。你看到的是什么？

```text
$ nmap -sU -p500 vpn.example.com
500/udp open|filtered isakmp
```

`open|filtered` 什么信息都没给。ike-scan 的价值就是把这个问号变成具体答案：

- 这个 UDP 500 到底是 IKE VPN，还是别的什么？
- 用的是哪种 IKE 实现？（Cisco / Checkpoint / Windows / StrongSwan / 各种设备）
- 支持 Aggressive Mode 吗？（**这是最关键的一项**——Aggressive Mode + PSK 会让哈希暴露，可离线爆破）
- 支持哪些加密算法、DH 组？（拿到后可以用来尝试连接或做合规检查）

| 工具 | 定位 |
|------|------|
| **ike-scan** | IKE 专用：发现、指纹、Aggressive Mode PSK 抓取 |
| `psk-crack`（同包） | 对 ike-scan 导出的 PSK 参数做离线字典破解 |
| [nmap](../01-信息搜集/nmap.md) `--script ike-version` | 简单识别 IKE 版本/厂商 |
| `nmap -sU -p500` | 只能告诉你端口"可能开着" |
| `ipsec-tools` / `strongswan` | 真正的 VPN 客户端（用于验证连通性） |

**关键认知**：ike-scan 本身**不发漏洞利用代码**，它做的是协议层的探测与信息导出。它的"杀伤力"来自 Aggressive Mode 的设计缺陷——**预共享密钥的哈希可以被离线爆破**，而这是 IKEv2 之前的常见配置。

## 2. 工作原理

```text
   ike-scan 192.168.56.101
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ① 构造 IKE Phase-1 请求（默认 Main Mode），UDP 发到 500      │
   │    内含：                                                 │
   │      - ISAKMP Header（cookie 用来匹配回包）                │
   │      - SA / Proposal / Transform 载荷                     │
   │        （默认 transform 集合是 itsec 设计的一组常见组合）    │
   │      - 可选 Vendor ID 载荷（--vendor，用于探测实现）         │
   └────┬──────────────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ② 有响应 = 该主机在跑 IKE。记录：                          │
   │      - 响应时间（用于 backoff 指纹）                        │
   │      - 回包解码内容（厂商 ID、Notify 消息、payload 结构）     │
   └────┬──────────────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ③ 指纹识别（三种技术）                                      │
   │    (a) Backoff 指纹：重传的间隔模式是各实现的"指纹"          │
   │        ike-scan 用 --showbackoff 把观测到的序列与          │
   │        ike-backoff-patterns 参考文件比对                    │
   │    (b) Vendor ID 指纹：匹配厂商私有 Vendor ID               │
   │    (c) 私有 Notify 消息码                                   │
   └────┬──────────────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ④ Aggressive Mode 专项（--aggressive）                      │
   │    请求里带上 ID 载荷（--id）。若服务端用 PSK 认证，         │
   │    它会在响应里返回：                                        │
   │      - 响应者的 nonce                                       │
   │      - 完整的 PSK 哈希相关的参数                             │
   │    这些参数足以做**离线**字典/暴力破解。                     │
   │    --pskcrack 把这些参数导出成 psk-crack 可用的格式          │
   └────────────────────────────────────────────────────────────────┘
```

**为什么 Aggressive Mode 危险**：

| 模式 | 密钥交换流程 | 是否泄露可爆破的哈希 |
|------|-------------|-------------------|
| Main Mode | 6 条消息，身份信息在加密隧道内 | 否（默认安全） |
| Aggressive Mode | 3 条消息，**响应者过早发送含身份的哈希** | **是**（仅当用 PSK 认证） |

所以标准的加固建议是：**要么用 Main Mode + PSK，要么用 Aggressive Mode + 证书认证（而非 PSK）**。

## 3. 安装与快速上手

```bash
sudo apt install ike-scan
ike-scan --version
ike-scan --help | head -40
command -v psk-crack     # 同包附带的离线破解工具
```

最小可用命令：

```bash
# 1) 发现哪些主机在跑 IKE
sudo ike-scan 192.168.56.101

# 2) 带 vendor ID 探测实现
sudo ike-scan -e 192.168.56.0/24 2>/dev/null

# 3) Aggressive Mode 探测（检查是否可抓 PSK 参数）
sudo ike-scan -A -n test -M 192.168.56.101
```

## 4. 核心参数详解

### 目标与传输

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `[hosts...]` | 目标列表（除用 `--file` 外必须提供） | 支持 CIDR/范围 |
| `-f, --file=<fn>` | 从文件读目标；`-` 表示 stdin | 批量 |
| `-s, --sport=<p>` | UDP 源端口（默认 500，`0`=随机） | 部分实现要求源端口为 500 |
| `-d, --dport=<p>` | UDP 目的端口（默认 500） | NAT-T 用 4500（`--nat-t` 会自动改） |
| `-T, --tcp[=<n>]` | 改用 TCP 传输；`1`=Checkpoint 的 RAW IKE over TCP（默认），`2`=Cisco 的封装模式 | **只能指定单个目标**；短写 `-T2`（数值要紧跟） |
| `-O, --tcptimeout=<n>` | TCP 连接超时秒数（默认 10） | 仅 TCP 模式 |
| `-N, --nodns` | 不做 DNS 解析，目标必须是 IP | 加快速度 |
| `-R, --random` | 随机化目标顺序 | 避免按顺序扫被识别 |
| `--sourceip=<s>` | 指定源 IP（或 `random`） | **需要 root，且「不会收到回包」**（因为回包发到伪地址） |

### 时序与带宽

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-r, --retry=<n>` | 每个目标总尝试次数（默认 3） | 丢包环境加大 |
| `-t, --timeout=<n>` | 每目标首次超时毫秒数（默认 500） | 跨公网调大到 1000~2000 |
| `-b, --backoff=<b>` | 超时倍增因子（默认 1.50） | 与 `--showbackoff` 的指纹有关，一般不改 |
| `-B, --bandwidth=<n>` | 出场带宽 bit/s（默认 56000；可加 `K`/`M`，十进制） | 与 `-i` 互斥 |
| `-i, --interval=<n>` | 最小包间隔（默认毫秒；加 `u` 为微秒，`s` 为秒） | 与 `-B` 互斥 |

### 输出

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-v, --verbose` | 详细进度（可叠加：1 每轮完成情况与无效 cookie；2 每个收发包；3 扫描前打印主机/Vendor ID/backoff 列表） | 排障 |
| `-q, --quiet` | **不解码**返回包（输出行更短） | 只要"谁是 IKE 主机"时 |
| `-M, --multiline` | 把 payload 解码分成多行（每行以 TAB 开头） | **payload 多时强烈建议加**，可读性大幅提升 |
| `--timestamp` | 给每个收到的包显示时间戳 | 分析 backoff |
| `--shownum` | 在 IP 前显示主机序号 | 同一目标多次探测时看哪些被忽略 |

### 指纹与模式

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-A, --aggressive` | 使用 **Aggressive Mode**（默认是 Main Mode） | **PSK 抓取的前提** |
| `-n, --id=<id>` | 设置 ID 载荷（字符串，或 `0x` 开头的十六进制） | 仅 Aggressive Mode；常见填 `test` 或域名 |
| `-y, --idtype=<n>` | ID 类型（默认 3 = ID_USER_FQDN） | 见 RFC 2407 4.6.2；常见 1=IP、2=FQDN、3=USER_FQDN |
| `-g, --dhgroup=<n>` | DH 组（默认 2；可选 1,2,5,14,15,16,17,18，MODP only） | 仅 Aggressive Mode / IKEv2 |
| `-m, --auth=<n>` | 认证方法（默认 1 = PSK） | RFC 定义 1~5；Checkpoint hybrid=64221；GSS=65001；XAUTH=65001~65010 |
| `-e, --vendor=<v>` | 发送十六进制 Vendor ID 字符串（可多次） | 探测特定实现的响应行为 |
| `-a, --trans=<t>` | 自定义 transform（可多次） | 见下方说明 |
| `-l, --lifetime=<s>` | IKE 生命周期秒数（默认 28800；`none` 表示不发送该属性） | 与 `--trans` 配合 |
| `-z, --lifesize=<s>` | IKE lifesize（KB，默认 0） | — |
| `-o, --showbackoff[=<n>]` | **显示 backoff 指纹表**（可选参数：收到最后一个包后再等 N 秒，默认 60） | 短写必须是 `-o25`（数值紧跟） |
| `-u, --fuzz=<n>` | backoff 模式匹配容差毫秒数（默认 500） | 调大提高容忍度但假阳性增多 |
| `-p, --patterns=<f>` | backoff 模式参考文件 | 默认 `/usr/local/share/ike-scan/ike-backoff-patterns` |
| `-I, --vidpatterns=<f>` | Vendor ID 模式参考文件 | 默认 `/usr/local/share/ike-scan/ike-vendor-ids` |
| `-P, --pskcrack[=<f>]` | **导出 Aggressive Mode PSK 参数**（可指定输出文件） | **只能指定单个目标**；短写 `-Pfile`（数值紧跟） |
| `-c, --noncelen=<n>` | nonce 长度字节数（默认 20） | **减小 nonce 可加快 PSK 爆破**；仅 Aggressive Mode |
| `-G, --gssid=<n>` | GSS ID（十六进制） | Windows 2000 需配 `--auth=65001` |

### 手工构造畸形包（协议模糊测试）

| 参数 | 作用 | 注意 |
|------|------|------|
| `-L, --headerlen=<n>` | 手动设置 ISAKMP 头长度（`+n`/`-n`/`n`） | **设成错误值可能干扰 VPN 服务器** |
| `-Z, --mbz=<n>` | 保留（MBZ）字段取值（默认 0，范围 0-255） | 使包不符合 RFC |
| `-E, --headerver=<n>` | ISAKMP 头版本（默认 0x10 = v1.0） | 不合规 |
| `-C, --certreq=<c>` | 添加 CertificateRequest 载荷（十六进制） | 探测对证书请求的响应 |
| `-D, --doi=<d>` | SA DOI（默认 1 = IPsec） | 非标准值 |
| `-S, --situation=<s>` | SA Situation（默认 1 = SIT_IDENTITY_ONLY） | — |
| `-j, --protocol=<p>` | Proposal 协议 ID（默认 1 = PROTO_ISAKMP） | — |
| `-k, --transid=<t>` | Transform ID（默认 1 = KEY_IKE） | — |
| `--spisize=<n>` | Proposal SPI 大小（默认 0） | 非 0 会附加随机 SPI |
| `--hdrflags=<n>` / `--hdrmsgid=<n>` | ISAKMP 头标志 / 消息 ID | — |
| `--cookie=<n>` | 指定 initiator cookie（十六进制） | **只能单个目标** |
| `--exchange=<n>` | 交换类型（ike-scan 只真正支持 2=Main、4=Aggressive） | 其他值只改头部 |
| `--nextpayload=<n>` | ISAKMP 头的 next payload | — |
| `--randomseed=<n>` | 设定 PRNG 种子（使随机数据可复现） | 复现实验用 |

**`--trans` 的两种写法**：

```bash
# 新写法：attr=value 对（推荐，清楚）
sudo ike-scan --trans="(1=7,14=128,2=1,3=3,4=5)" <target>
# 含义：Enc=AES/128, Hash=MD5, Auth=RSA sig, DH Group=5

# 旧写法：enc[/len],hash,auth,group
sudo ike-scan --trans=7/256,1,1,5 <target>
# 含义：Enc=AES-256, Hash=MD5, Auth=shared key, DH Group=5
```

常用属性号（RFC 2409 附录 A）：`1`=Encryption、`2`=Hash、`3`=Auth、`4`=DH Group、`14`=Key Length。

## 5. 实战演练

**环境**：本地实验环境。**只对你有授权的目标使用。**

- 靶机 A：在实验虚拟机上起一个 StrongSwan 或 libreswan 的 IPsec 服务（配置 Aggressive Mode + PSK，用于演示）。
- 靶机 B：pfSense / OPNsense 之类的开源防火墙虚拟机（内置 IPsec）。
- 攻击机 Kali：`192.168.56.10`。
- 也可对自己的云上 VPN 网关做合规自查（前提是有权限）。

> ⚠️ ike-scan 的候选目标通常是**组织的 VPN 网关**——这是高价值资产，扫描行为会被安全团队重点关注。**务必事先取得书面授权。**

### 场景 1：发现 IKE 主机（最小用法）

```bash
sudo ike-scan 192.168.56.101
```

预期输出（存在 IKE 服务）：

```text
Starting ike-scan 1.9.5 with 1 hosts (http://www.nta-monitor.com/tools/ike-scan/)
192.168.56.101	Main Mode Handshake returned HDR=(CKY-R=1a2b3c4d5e6f7890) SA=(Enc=3DES Hash=SHA1 Auth=PSK Group=2:modp1024 LifeType=Seconds LifeDuration=28800) VID=...

Ending ike-scan 1.9.5: 1 hosts scanned in 0.123 seconds (8.13 hosts/sec). 1 returned handshake; 0 returned notify
```

预期输出（没有 IKE 服务）：

```text
Starting ike-scan 1.9.5 with 1 hosts
192.168.56.200	Not responding

Ending ike-scan 1.9.5: 1 hosts scanned in 0.075 seconds (13.33 hosts/sec). 0 returned handshake; 0 returned notify
```

解读关键行：
- `Main Mode Handshake returned` —— **确认是 IKE 服务**（不是随便什么 UDP 500 的服务）。
- `SA=(Enc=3DES Hash=SHA1 Auth=PSK Group=2:modp1024 LifeType=Seconds LifeDuration=28800)` —— **服务端支持的算法集**。
  - `Enc=3DES` —— 3DES 是弱加密，应该升级。
  - `Hash=SHA1` —— SHA1 也应该淘汰。
  - `Auth=PSK` —— **预共享密钥认证**，是 Aggressive Mode 可爆破的前提。
  - `Group=2:modp1024` —— DH 组 2 只有 1024 位，属于弱参数。
- `CKY-R=` —— 响应者的 cookie。

> 这一行 SA 就已经是一份"TLS 配置体检"的等价物。**只要看到 `Enc=3DES`、`Hash=SHA1`、`Group=2`，就可以确定这个 VPN 网关的配置多年未更新。**

### 场景 2：网段扫描 + 厂商指纹

```bash
sudo ike-scan -M -e 192.168.56.0/24 2>/dev/null | tee ike_scan.txt
```

预期输出片段：

```text
Starting ike-scan 1.9.5 with 256 hosts
192.168.56.101	Main Mode Handshake returned
	HDR=(CKY-R=a1b2c3d4e5f60718)
	SA=(Enc=3DES Hash=SHA1 Auth=PSK Group=2:modp1024 LifeType=Seconds LifeDuration=28800)
	VID=4f4573746172746572... (Cisco)
	VID=09002689dfd6b712... (Cisco)
Ending ike-scan: 256 hosts scanned in 32.1 seconds. 1 returned handshake; 0 returned notify
```

解读：
- `-M`（multiline）把每个 payload 放到单独一行，**输出可读性完全不同**，payload 多的时候必须加。
- `VID=` 是 Vendor ID，括号里的 `(Cisco)` 就是**厂商指纹**——ike-scan 用 `ike-vendor-ids` 参考文件匹配出来的。
- 加密方式决定用哪个 `--trans` 组合去继续探测。

### 场景 3：Backoff 指纹识别实现

```bash
# -o 显示 backoff 表；可选参数是"收到最后一个包后再等多少秒"（默认 60）
# 短写时数值必须紧跟：-o25，不能写 -o 25
sudo ike-scan -o25 -t 1000 -r 5 192.168.56.101
```

预期输出片段：

```text
Starting ike-scan 1.9.5 with 1 hosts
192.168.56.101	Main Mode Handshake returned HDR=(CKY-R=...) SA=(...) VID=...

--- Backoff Table ---
Time(ms)  Target
    1000  192.168.56.101
    1500  192.168.56.101
    2250  192.168.56.101
    3375  192.168.56.101
    5062  192.168.56.101

--- Backoff Fingerprint ---
192.168.56.101	= 1.50x (StrongSwan / FreeS/WAN)
```

解读：**每个 IKE 实现的重传间隔模式不同**，这个"节奏"就成了指纹。ike-scan 把观测到的间隔与 `ike-backoff-patterns` 里的参考模式比对，给出实现名称。这是 ike-scan 名字里"scan"的真正含义——它不只是发现，还会**识别实现**。

`--fuzz`（默认 500ms）控制容差：网络抖动大时调大，但假阳性也会增加。

### 场景 4：Aggressive Mode 探测与 PSK 参数导出（核心场景）

```bash
# 第一步：确认服务端是否响应 Aggressive Mode
sudo ike-scan -A -n test -M 192.168.56.101
```

预期输出（**服务端支持且用 PSK**）：

```text
Starting ike-scan 1.9.5 with 1 hosts
192.168.56.101	Aggressive Mode Handshake returned
	HDR=(CKY-R=deadbeefcafe0001)
	SA=(Enc=3DES Hash=SHA1 Auth=PSK Group=2:modp1024 LifeType=Seconds LifeDuration=28800)
	KeyExchange(128 bytes)
	Nonce(20 bytes)
	ID(Type=ID_USER_FQDN, Value=test)
	Hash(20 bytes)
	VID=...
Ending ike-scan: 1 hosts scanned. 1 returned handshake

--- Aggressive Mode PSK parameters (for psk-crack) ---
[IKE Aggressive Mode PSK parameters]
sha1_hash = ...
g_xr = ...
g_xi = ...
cky_r = ...
cky_i = ...
sai_b = ...
idir_b = ...
ni_b = ...
nr_b = ...
```

预期输出（**服务端不支持 Aggressive Mode**）：

```text
192.168.56.101	Notify message 14 (NO-PROPOSAL-CHOSEN/EQUAL-PAYLOAD)
```
或
```text
192.168.56.101	Not responding
```

第二步：把参数导出到文件，交给 `psk-crack` 离线爆破：

```bash
sudo ike-scan -A -n test -Pparam.txt 192.168.56.101
cat param.txt

# 字典攻击（-d / --dictionary 指定字典文件）
psk-crack -d /usr/share/wordlists/rockyou.txt param.txt

# 暴力破解：字符集为纯数字，尝试最长 8 位
psk-crack --bruteforce 8 --charset 0123456789 param.txt
```

解读（**这一节是本教程最重要的一段**）：

- `Nonce(20 bytes)` + `KeyExchange` + `Hash` 一起构成了**足以离线验证 PSK 猜测**的全部材料。
- **减短 nonce 可以加快爆破**：`-c 8`（最小允许值）会让服务端返回更短的 nonce，准备计算的哈希数据更少。
- `psk-crack` 是 ike-scan 包自带的工具，配合字典（`rockyou.txt`）或暴力模式（`--bruteforce` + `--charset`）工作。
- **爆破是否成功，完全取决于 PSK 的强度**。强 PSK（长随机串）基本不可能破；`password123` 这类几分钟就出来。
- 输出里的 `Notify message 14 (NO-PROPOSAL-CHOSEN)` 说明服务端拒绝了提案——这本身也是有用的信息（说明 Aggressive Mode 被关掉了，或需要不同的 `--trans`）。

### 场景 5：用自定义 transform 探测具体算法支持

```bash
# 探测是否支持 AES-256 + SHA256 + DH Group 14（现代组合）
sudo ike-scan --trans="(1=7,14=256,2=5,3=1,4=14)" 192.168.56.101

# 探测是否支持弱算法（如果支持，说明配置需要加固）
sudo ike-scan --trans="(1=1,2=1,3=1,4=1)" 192.168.56.101   # DES + MD5 + PSK + Group1

# 用 -a 传入多组 transform 看哪些被接受
sudo ike-scan \
  --trans=5,2,1,2 \
  --trans=7/256,1,1,5 \
  --trans="(1=7,14=128,2=1,3=3,4=5)" \
  192.168.56.101
```

解读：
- 如果服务端对 `1=1`（DES）回了 `handshake returned`，说明**它仍然支持 DES**——这在任何现代标准里都是必须修掉的问题。
- 多组 `--trans` 可以一次性把候选算法集都问一遍，看哪些被接受。这是**做 VPN 配置合规核查**的高效方式。
- 注意：属性号含义见 RFC 2409 附录 A；`14` 是 Key Length，必须放在 Enc 之后。

## 6. 输出解读

### 三条状态线

| 输出 | 含义 |
|------|------|
| `Main Mode Handshake returned` | **确认是 IKE 服务**，且支持 Main Mode（几乎必然） |
| `Aggressive Mode Handshake returned` | 支持 Aggressive Mode（**如果同时是 PSK 认证 → 可爆破**） |
| `Notify message N (...)` | 服务端回了 Notify（如 `NO-PROPOSAL-CHOSEN`），说明是 IKE 但不接受你的提案 |
| `Not responding` | 无响应（服务未运行 / 被过滤 / 超时太短） |
| 结尾统计 `N returned handshake; M returned notify` | 本次扫描的汇总 |

### payload 解码

| payload | 含义 | 关注点 |
|---------|------|--------|
| `HDR=(CKY-R=...)` | ISAKMP 头，`CKY-R` 是响应者 cookie | — |
| `SA=(Enc=... Hash=... Auth=... Group=... LifeType=... LifeDuration=...)` | **服务端支持的 SA 组合** | **最重要的一行**：Enc/Hash/Group 是否过时；Auth 是否为 PSK |
| `VID=...(厂商名)` | Vendor ID 与指纹匹配结果 | 识别具体实现 |
| `KeyExchange(N bytes)` | DH 公钥 | Aggressive Mode 下是爆破材料 |
| `Nonce(N bytes)` | 随机数 | Aggressive Mode 下是爆破材料 |
| `ID(Type=..., Value=...)` | 身份载荷 | 确认 `--id` 被接受 |
| `Hash(N bytes)` | PSK 哈希 | 爆破的验证目标 |
| `--- Backoff Table ---` | 重传时间序列 | 指纹输入 |
| `--- Backoff Fingerprint ---` | 实现识别结果 | 如 `1.50x (StrongSwan / FreeS/WAN)` |

### SA 字段的风险判断

| 字段 | 安全值 | 风险值 |
|------|--------|--------|
| `Enc` | AES / AES-GCM | `DES`、`3DES` |
| `Hash` | SHA2-256 及以上 | `MD5`、`SHA1` |
| `Auth` | `RSA sig` / 证书 | `PSK`（配合 Aggressive Mode 时高危） |
| `Group` | 14 (2048) 及以上 | `1` (768)、`2` (1024) |
| `LifeDuration` | 常规 28800 秒 | 过长或异常值 |

**最高危组合**：`Auth=PSK` + 响应 Aggressive Mode。这两条同时成立，就意味着**存在可离线爆破的预共享密钥**。

## 7. 与其他工具配合

```bash
# 1) nmap 找 UDP 500/4500 -> ike-scan 确认与枚举
sudo nmap -sU -p500,4500 --open -oG - 192.168.56.0/24 | awk '/UDP/{print $2}' > ike_hosts.txt
while read -r h; do
  echo "=== $h ==="
  sudo ike-scan -M -A "$h"
done < ike_hosts.txt

# 2) nmap 的 ike-version 脚本 + ike-scan 交叉验证
sudo nmap -sU -p500 --script ike-version 192.168.56.101
sudo ike-scan -M 192.168.56.101

# 3) ike-scan 导出 PSK 参数 -> psk-crack 离线爆破（授权内）
sudo ike-scan -A -n test -P/lab/ike-params.txt 192.168.56.101
psk-crack -d /usr/share/wordlists/rockyou.txt /lab/ike-params.txt

# 4) 拿到 PSK 后用 strongswan/ipsec-tools 验证连通（授权内，验证发现）
#    /etc/ipsec.conf 中配置对应 PSK 与网关，然后：
#    sudo ipsec up <conn-name>

# 5) 批量合规核查：只关心弱算法是否还开着
for h in $(cat ike_hosts.txt); do
  printf "%-16s " "$h"
  sudo ike-scan --trans="(1=1,2=1,3=1,4=1)" -q "$h" 2>/dev/null | grep -q "Handshake returned" \
    && echo "警告：支持 DES/MD5/Group1" || echo "OK"
done
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `Not responding`，但确认有 VPN | UDP 500 被过滤 / 超时太短 | `-t 2000 -r 5`；确认 `-d 500`；公网目标调大超时 |
| 只回 `Notify message 14` | 服务端不支持你发去的提案 | 用 `--trans` 试更多组合；或换 `-A`（Aggressive） |
| `-P` 报"只能指定单个目标" | `--pskcrack` 限制单目标 | 一次只给一个 IP |
| `-o 25` 报参数错误 | 短选项的数值必须紧跟 | 写 `-o25`（`-T2`、`-Pfile` 同理） |
| `-i` 和 `-B` 同时用报错 | 两者是同一底层变量的不同表达 | 只保留一个 |
| 非 root 无法用 `-s 500` | 绑定 <1024 端口需要特权 | `sudo` |
| `--sourceip` 后完全收不到回包 | **设计如此**（回包发往伪地址） | 需要配合能收到该地址流量的位置嗅探 |
| 输出一行太长看不清 | 未解码或多 payload | 加 `-M`（multiline）；或用 `-q` 只看是否有响应 |
| `--trans` 报语法错误 | 括号是 shell 特殊字符；或属性号不对 | 加引号：`--trans="(1=7,14=128,2=1,3=3,4=5)"`；属性号查 RFC 2409 附录 A |
| `Auth=PSK` 但抓不到 PSK 参数 | 服务端不支持 Aggressive Mode | 说明配置相对安全；这是"好消息" |
| psk-crack 跑了很久没结果 | PSK 强度足够高 | 这是预期结果——**强 PSK 就是有效的防护** |
| 扫描惊动了对方的 SOC | VPN 网关是高价值监控目标 | **事先取得书面授权**，并告知对方安全团队 |

## 9. 防御视角（蓝队）

这是本教程最有价值的一节——**IKE 的加固项非常明确。**

### 核心加固清单

| 优先级 | 措施 | 原因 |
|--------|------|------|
| **高** | **禁用 Aggressive Mode**（或只允许配合证书认证使用） | 直接消除 PSK 离线爆破的前提 |
| **高** | 使用**证书认证**替代 PSK | 从设计上避免哈希暴露 |
| 高 | 如果必须用 PSK，使用**长随机强密钥**（≥ 20 字符随机） | 让爆破在计算上不可行 |
| 高 | 迁移到 **IKEv2** | IKEv2 的 Aggressive Mode 不暴露 PSK 哈希；且支持更现代的算法 |
| 中 | 淘汰弱算法：禁 DES/3DES、禁 MD5/SHA1 | 3DES 有 SWEET32 等已知弱点 |
| 中 | DH 组升级到 **Group 14（2048 位）及以上** | Group 1/2 强度不足 |
| 中 | 限制 VPN 网关的公网暴露（只对特定来源开放 500/4500） | 减少攻击面 |
| 中 | 启用速率限制与失败告警 | 探测与爆破都会产生高频握手 |
| 低 | 统一生命周期参数（28800 秒是常规值） | 避免异常配置被发现 |

### 可检测的流量特征

ike-scan 的探测流量**非常规整，特征明显**：

- **无 cookie 匹配的 Phase-1 请求**：ike-scan 会发大量 Main Mode 请求。**VPN 设备日志里会出现大量"未完成的 Phase-1"**——正常用户会完成整个握手，扫描器不会。
- **重复相同提案的请求**：ike-scan 的默认 transform 集是固定的。多个目标收到**完全相同的 SA 提案**，这是扫描器的强指纹。
- **Aggressive Mode 探测**：正常的 Aggressive Mode 客户端会带着真实 ID（如 `user@corp.com`）；ike-scan 常带 `test` 或明显的探测值。
- **高频包**：`-B` / `-i` 控制速率，但默认 56 kbit/s 对单目标仍属高频。

### 检测规则建议

- **设备侧**（Cisco ASA / FortiGate / pfSense 等）：
  - 对"Phase-1 失败/未完成"的事件设阈值告警。
  - 对同一源 IP 的 IKE 协商尝试频率设限（很多设备支持 IKE DoS 防护 / cookie challenge）。
  - **启用 IKE cookie 挑战（anti-DoS）**，这会显著提高扫描与爆破的成本。
- **网络侧**：
  - 对 UDP 500/4500 做流量基线：正常流量是"少量、长会话"；扫描是"大量、短促、无后续"。
  - 把 VPN 网关的 500/4500 限制为**只对已知来源 IP 开放**——这是最彻底的缓解（攻击者根本连不上）。

### 需要特别提醒的一点

**"能抓到 PSK 参数" ≠ "PSK 会被破"**。ike-scan 的价值在于**暴露了一个设计上的信息泄露点**，而防护的重心应该是：

1. 关掉 Aggressive Mode（消除泄露点）；
2. 用证书认证（消除 PSK）；
3. 如果前两者都做不到，就用足够强的 PSK（让泄露点变得无用）。

这三层里，**第 1 层投入最小、收益最大**。

## 10. 参考

- 官方仓库（含 `psk-crack` 与 backoff 指纹论文）：<https://github.com/royhills/ike-scan>
- 项目主页：<https://www.nta-monitor.com/tools-resources/security-tools/ike-scan>
- UDP backoff 指纹论文（随包发布 `udp-backoff-fingerprinting-paper.txt`）
- RFC 2409（IKE）：<https://www.rfc-editor.org/rfc/rfc2409>
- RFC 2408（ISAKMP）：<https://www.rfc-editor.org/rfc/rfc2408>
- RFC 2407（IPsec DOI，含 Identification 类型）：<https://www.rfc-editor.org/rfc/rfc2407>
- Kali 工具页：<https://www.kali.org/tools/ike-scan/>
- man page：`man ike-scan` ｜ `man psk-crack`
- 用法核实：本教程参数取自 `ike-scan 1.9.5` 的 man page

---

**相关教程**：[nmap](../01-信息搜集/nmap.md) ｜ [fping](fping.md) ｜ [openssl](openssl.md) ｜ [nuclei](nuclei.md) ｜ [hping3](../01-信息搜集/hping3.md)
