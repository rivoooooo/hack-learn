# enum4linux（Windows / Samba 枚举的瑞士军刀）

> **一句话**：把 `smbclient`、`rpcclient`、`net`、`nmblookup` 这些 Samba 工具串起来，一次性枚举 Windows / Samba 主机的用户、共享、组、口令策略和系统信息。
> **分类**：信息搜集 ｜ **Kali 包**：`enum4linux` ｜ **官方文档**：<https://labs.portcullis.co.uk/tools/enum4linux/>

## 1. 它解决什么问题

在 Windows 环境里，你要回答的问题通常是这些：**有哪些共享？能匿名读吗？有哪些用户？口令策略怎么样？域控在哪？**

这些问题的答案分散在 NBT、SMB、RPC、LDAP 几个协议里，手工一条条拼很烦。enum4linux 就是那个"一次全问一遍"的包装器——它本质上是 Samba 套件的编排脚本。

| 工具 | 定位 | 何时用 |
|------|------|--------|
| **enum4linux** | 一键跑完所有 SMB/RPC 枚举 | 首次接触一台 Windows/Samba 主机 |
| [smbclient](smbclient.md) | 交互式访问共享（像 ftp 一样 ls/get/put） | 知道共享名后，实际读写文件 |
| [nbtscan](nbtscan.md) | NetBIOS 名字表扫描 | 快速拿主机名/用户名/MAC |
| [nmap](nmap.md) | `--script smb-*` 系列 | 需要在扫描里顺带做枚举 |
| `rpcclient` | 手工 RPC 调用 | enum4linux 覆盖不到的细分项 |
| `enum4linux-ng`（非 Kali 默认包） | Python 重写版，输出 JSON/YAML | 需要结构化输出时 |

> enum4linux 的 **RID cycling（RID 循环枚举）** 是它最有价值的独门功能：即使匿名会话拿不到用户列表，只要允许匿名 SID/名称翻译，就能通过遍历 RID（500、501、1000、1001…）把用户名一个个"猜"出来。

## 2. 工作原理

```text
                 enum4linux -a <target>
                          │
   ┌──────────────────────┼───────────────────────────────────┐
   │                      │                                   │
 [nmblookup]        [smbclient]                        [rpcclient]
  名字/域/工作组      -L 列共享                            │
                     -N 匿名会话                          ├─ enumdomusers     列用户
   │                      │                              ├─ enumdomgroups    列组
   │                      │                              ├─ querydominfo     域信息
   └──────────────────────┼──────────────────────────────┴─ getdompwinfo    口令策略
                          │
                    [polenum] 解析口令策略
                          │
   ┌──────────────────────┴───────────────────────────────┐
   │ RID cycling：lookupsid 已知用户 → 拿 SID              │
   │  然后对 RID 500..RID_MAX 逐个查名字                   │
   │  （Samba 常见的 RID 段是 3000–3050）                   │
   └──────────────────────┬───────────────────────────────┘
                          │
                   统一格式化成文本报告
```

关键机制：

- **`-a` = `-U -S -G -P -r -o -n -i`**，等价于"能做的都做一遍"。不指定任何选项时默认就是 `-a`。
- **匿名优先**：默认用空用户名/空口令（`-u "" -p ""`）做匿名会话。很多老旧 Samba/Windows 配置允许匿名枚举。
- **RID cycling 的前提**：Windows NT/2000 的 `RestrictAnonymous=1`，或 XP/2003 上开启"网络访问：允许匿名 SID/名称转换"。**这个设置在 2003 之后的系统默认已关闭**，所以现代系统上 RID cycling 往往失败。
- **`-K n` 优化**：对域控来说 RID 是稀疏的，`-K` 让脚本在连续 n 个 RID 都没对应用户时才停止，避免遍历到 65535。

## 3. 安装与快速上手

```bash
sudo apt install enum4linux
enum4linux -h
command -v enum4linux   # /usr/bin/enum4linux
```

最小可用命令：

```bash
# 1) 全量枚举（默认行为）
enum4linux 192.168.56.101

# 2) 显式指定全部简单枚举选项
enum4linux -a 192.168.56.101

# 3) 只列共享 + 只列用户，速度快
enum4linux -S -U 192.168.56.101
```

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `<ip>` | 目标 IP（位置参数，必需） | 一次一台；批量请写脚本循环 |
| `-a` | **全部简单枚举**：`-U -S -G -P -r -o -n -i` | 不加任何选项时默认启用 |
| `-U` | 获取用户列表 | 目标信息量最大的一项 |
| `-M` | 获取机器列表（`*`：受限） | 域环境下找成员机 |
| `-S` | 获取共享列表 | 找可读/可写共享 |
| `-P` | 获取口令策略信息 | 决定后续爆破可行性（锁定阈值/最小长度） |
| `-G` | 获取组和组成员列表 | 找管理员组，识别高价值账号 |
| `-d` | 详细模式，作用于 `-U` 和 `-S` | 需要更多字段时加 |
| `-u <user>` | 指定用户名（默认空串 = 匿名） | 拿到低权账号后带上提升枚举效果 |
| `-p <pass>` | 指定口令（默认空串 = 匿名） | 与 `-u` 配套 |
| `-r` | 通过 **RID cycling** 枚举用户 | enum4linux 的核心能力 |
| `-R <range>` | 指定 RID 范围（默认 `500-550`），隐含 `-r` | 想扫更大范围时用，如 `500-2000` |
| `-K <n>` | 连续 n 个 RID 无对应用户才停止（隐含 `-r`） | **域控场景推荐**，比固定范围高效 |
| `-l` | 通过 LDAP（389/TCP）取有限信息 | 仅域控有效 |
| `-s <file>` | 用字典猜共享名（share name brute force） | 隐藏共享（如 `$` 结尾）的发现手段 |
| `-k <user[,user2]>` | 指定"已知存在"的用户名，用于取 SID | 配合 `-r`，提高 RID 起点准确性 |
| `-o` | 获取操作系统信息 | 确认版本，决定后续 EXP |
| `-i` | 获取打印机信息 | 打印机常是信息泄露点 |
| `-w <workgroup>` | 手工指定工作组 | 通常能自动发现，无需指定 |
| `-n` | 执行 `nmblookup`（类似 `nbtstat`） | 拿 NetBIOS 名字 |
| `-v` | 详细模式，打印实际执行的命令 | 排查"为什么没结果"时必开 |
| `-A` | **激进模式**：对共享做写入检查 | **会修改目标状态，慎用** |
| `-h` | 帮助 | — |

## 5. 实战演练

**环境**：本地实验室，全部为自建靶机。

- 靶机 A：Metasploitable2（`192.168.56.101`），内含 Samba 3.x，**故意配置为可匿名枚举**——非常适合练习。
- 靶机 B（可选）：Windows 7 / Server 2008 R2 实验虚拟机（关闭"匿名 SID/名称转换"能对比现代系统的差异）。
- 攻击机：Kali（`192.168.56.10`）。

### 场景 1：一次性全量枚举

```bash
enum4linux -a 192.168.56.101 | tee enum_full.txt
```

预期输出片段：

```text
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ )

 ==========================
|    Target Information    |
 ==========================
Target ........... 192.168.56.101
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none

 =============================================
|    Share Enumeration on 192.168.56.101      |
 =============================================
	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	tmp             Disk      oh noes!
	opt             Disk
	IPC$            IPC       IPC Service (metasploitable server (Samba 3.0.20-Debian))
	ADMIN$          IPC       IPC Service (metasploitable server (Samba 3.0.20-Debian))

 ==========================================
|    Users on 192.168.56.101 via RID       |
 ==========================================
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1000 Unix User\msfadmin (Local User)
...
```

解读：
- `tmp` 共享注释是 `oh noes!`——这是 Metasploitable2 的经典可写共享。
- `S-1-22-1-1000 Unix User\msfadmin` 是通过 RID cycling 枚举出来的 Unix 用户。
- `Known Usernames` 那一行是脚本内置的常见用户名提示。

### 场景 2：只做用户与口令策略（信息量/时间比最高）

```bash
enum4linux -U -P -G 192.168.56.101
```

预期输出片段：

```text
 ==================================================
|    Password Policy Information for 192.168...    |
 ==================================================
[+] Attaching to 192.168.56.101 using a NULL share
[+] Trying protocol 139/SMB...
[+] Found domain(s):
    [+] METASPLOITABLE
[+] Password Info for Domain: METASPLOITABLE
    [+] Minimum password length: 5
    [+] Password history length: None
    [+] Maximum password age: Not Set
    [+] Password Complexity Flags: 000000
    [+] Reset Account Lockout Counter: 1800 seconds
    [+] Lockout Threshold: None
    [+] Lockout Duration: 1800 minutes
	[+] Minimum password age: 0 days
```

解读：
- `Lockout Threshold: None` → **可以做口令爆破而不必担心锁定账号**。
- `Password Complexity Flags: 000000` → 不要求复杂度。
- 这两条结合 `Minimum password length: 5`，说明目标口令策略非常弱，可以放心跑 [hydra](https://www.kali.org/tools/hydra/) 之类的爆破（授权内）。

### 场景 3：RID cycling 深度枚举

```bash
# 已知一个存在的用户名，用它当 SID 起点；扫 500-2000 的 RID
enum4linux -r -R 500-2000 -k msfadmin 192.168.56.101
```

预期输出片段：

```text
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1000 Unix User\msfadmin (Local User)
S-1-22-1-1001 Unix User\user (Local User)
S-1-22-1-1002 Unix User\service (Local User)
```

解读：RID cycling 能拿到"用户列表 API 不给你、但 SID 翻译给你"的用户名。**这是 enum4linux 最大的价值点**。

对域控，改用 `-K`：

```bash
enum4linux -K 10 -k administrator 10.0.0.10
```

### 场景 4（进阶）：认证后枚举 + 隐藏共享爆破

```bash
# 拿到低权账号后，带上凭据再枚举一次，结果通常丰富得多
enum4linux -a -u lowpriv -p 'Password123' 192.168.56.101

# 用字典猜隐藏共享名
echo -e "backup\nhr\nfinance\nadmin\ndev" > shares.txt
enum4linux -s shares.txt 192.168.56.101
```

解读：匿名枚举拿不到的东西，低权账号往往能拿到。`-s` 用字典枚举共享名，是发现 `backup$`、`hr$` 这类**隐藏共享**（`$` 结尾）的标准手段——它们在 `smbclient -L` 里不会出现。

## 6. 输出解读

| 输出区块 | 含义 | 下一步 |
|----------|------|--------|
| `Target Information` | 目标、RID 范围、口令 | 确认参数正确 |
| `Share Enumeration` 表 | 共享名 + 类型 + 注释 | 关注 `Disk` 类型和可疑注释 |
| `Read/Write access` 提示 | 匿名是否可读写 | 匿名可写 → 高危 |
| `Users on ... via RID` | 通过 RID 枚举出的用户 | 用户名清单 → 口令喷洒（授权内） |
| `Password Policy Information` | 锁定阈值、最小长度、复杂度 | 决定爆破策略 |
| `Group Memberships` | 组成员 | 找 Domain Admins / sudo 组 |
| `OS Information` | 系统版本 | 去 [searchsploit](../02-漏洞分析/searchsploit.md) 查 EXP |
| `Printer Information` | 打印机信息 | 可能泄露驱动/主机名 |
| `[+] Found domain(s)` | 域/工作组名 | 后续 Kerberos 攻击的前提 |

**关键判断规则**：

| 现象 | 风险判断 |
|------|----------|
| 匿名可列共享 | 中危（信息泄露） |
| 匿名可读写共享 | **高危**（可投毒、可植入） |
| 匿名可枚举用户 | 中危（为爆破提供清单） |
| RID cycling 成功 | 中危（同上的另一条路径） |
| `Lockout Threshold: None` | 高危前提（可无限爆破） |
| 匿名可取口令策略 | 中危 |

## 7. 与其他工具配合

```bash
# 1) nmap 发现 445/139 -> enum4linux 枚举
nmap -p139,445 --open -oG - 192.168.56.0/24 | grep -oP '\d+\.\d+\.\d+\.\d+' | sort -u > smb_hosts.txt
while read ip; do enum4linux -a "$ip" > "enum_$ip.txt"; done < smb_hosts.txt

# 2) enum4linux 结果 -> smbclient 实际访问
smbclient -N -L //192.168.56.101          # 列共享
smbclient -N //192.168.56.101/tmp         # 匿名进共享（Metasploitable2 可写）

# 3) 用户清单 -> 口令喷洒（授权内，注意锁定策略）
#    用 enum4linux -P 先确认 Lockout Threshold
cut -d'\' -f2 enum_full.txt | grep 'Local User' | awk '{print $1}' > users.txt
# hydra -L users.txt -p 'Password123' smb://192.168.56.101

# 4) 系统版本 -> 漏洞库
grep -i "OS Information" -A 5 enum_full.txt | grep -i "samba\|windows"
searchsploit samba 3.0.20
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `[E] Server doesn't allow session using username '', password ''.` | 目标禁止匿名会话 | 正常；加 `-u`/`-p` 带凭据，或改走 RID cycling |
| RID cycling 返回 `NT_STATUS_ACCESS_DENIED` | 现代 Windows 默认关闭匿名 SID 翻译 | 需要有效凭据；对 Win2003+ 大多无效 |
| 枚举出 0 个用户但共享正常 | `RestrictAnonymous` 已启用 | 这是安全配置生效，不是工具坏了 |
| `-s` 猜共享报大量错误 | 字典太大 / 目标限速 | 用小字典；加 `-v` 看实际命令 |
| 结果里出现 `<server>` 之类的占位 | 输出解析问题 | 以 `-v` 模式看原始 `smbclient` 输出 |
| `-A` 模式回来后目标共享被改了 | `-A` 会做**写入检查** | **只在授权演练中使用**，生产环境绝不要用 |
| 输出太长难以分析 | 全量枚举信息量大 | `tee` 存盘后用 `grep` 分段看 |
| `-l`（LDAP）无结果 | 目标不是域控，或 389 未开放 | 仅对 DC 有意义 |
| 脚本本身报 Perl 警告 | 老代码兼容性 | 忽略，或用 `enum4linux-ng` |
| 枚举很慢 | SMB 超时重试 | 检查 139/445 是否真的开放；用 `-v` 观察卡在哪一步 |

## 9. 防御视角（蓝队）

- **核心原则：关闭匿名访问**。
  - Windows：组策略 `网络访问：不允许匿名枚举 SAM 帐户和共享`（`RestrictAnonymous=1`）与 `网络访问：不允许匿名枚举 SAM 帐户和共享` + `不允许匿名 SID/名称转换`（`RestrictAnonymousSAM`、`EveryoneIncludesAnonymous=0`）。Windows 2003 之后默认已收紧，但**很多域环境仍被改回宽松**，需定期核查。
  - Samba：`restrict anonymous = 2`、`map to guest = never`、`null passwords = no`。
- **共享权限**：
  - 移除不必要的共享；共享名不要用 `backup`、`hr` 这类可猜词。
  - 不要给 `Everyone` 写权限；Metasploitable2 那种匿名可写 `tmp` 是必须消除的配置。
- **口令策略**：设置锁定阈值（例如 5 次/15 分钟），可显著降低爆破可行性——enum4linux 的 `-P` 正是利用"没有锁定策略"这一前提。
- **检测**：
  - SMB 侧：匿名 `IPC$` 连接、`enumdomusers`、`lookupsid` 等 RPC 调用会在 **Windows 安全日志** 里留下记录（事件 ID 4624/4625 的匿名登录、SMB 会话建立）。
  - RID cycling 的特征是**对同一目标的密集 `lookupsid` 调用**，可在 EDR/SIEM 里按"单位时间内 RPC SID 查询次数"设阈值。
  - 网络侧：短时间内大量 `lsarpc`/`samr` 命名管道请求。
- **发现响应的动作**：如果是渗透演练，检测到 `-A` 的写入检查说明共享写权限没管住——这是最需要修的问题。

## 10. 参考

- 官方项目页：<https://labs.portcullis.co.uk/tools/enum4linux/>
- 源码（含完整 usage 文本）：<https://github.com/CiscoCXSecurity/enum4linux>
- Kali 工具页：<https://www.kali.org/tools/enum4linux/>
- 用法核实：本教程参数取自 `enum4linux v0.9.1` 源码中的 usage 文本（`enum4linux.pl` 第 137–191 行）
- 相关 man page：`man smbclient`、`man nbtscan`

---

**相关教程**：[smbclient](smbclient.md) ｜ [nbtscan](nbtscan.md) ｜ [nmap](nmap.md) ｜ [searchsploit](../02-漏洞分析/searchsploit.md)
