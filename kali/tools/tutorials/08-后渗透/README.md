# 08 · 后渗透（Post-Exploitation）

> 本目录是 Kali 工具精讲教程的第 8 篇：**拿到第一台机器的 shell 之后怎么办**。
> 主干闭环：**提权 → 抓凭据 → 复用凭据横向 → 铺隧道打更深内网**。
> 上游：[`../06-漏洞利用/`](../06-漏洞利用/) ｜ 下游：[`../09-数字取证/`](../09-数字取证/)、[`../12-基础设施与C2/`](../12-基础设施与C2/)
> 相关索引：[`../../index.md`](../../index.md) ｜ 分类速查：[`../../catalog/post-exploitation.md`](../../catalog/post-exploitation.md)、[`../../catalog/passwords.md`](../../catalog/passwords.md)、[`../../by-attack/lateral-movement.md`](../../by-attack/lateral-movement.md)、[`../../by-attack/credential-access.md`](../../by-attack/credential-access.md)

---

## 工具清单

| 工具 | 一句话 | 难度 | 教程 |
|------|--------|------|------|
| **impacket** | 用 Linux 说 Windows 协议：抓哈希、Kerberos 攻击、远程执行（`impacket-*` 系列） | ⭐⭐⭐⭐ | [`impacket.md`](impacket.md) |
| **crackmapexec** | 一条命令把凭据在整片网段试一遍（**已停止维护**） | ⭐⭐⭐ | [`crackmapexec.md`](crackmapexec.md) |
| **netexec** | CME 的官方后继（`nxc`），模块更多、维护活跃 | ⭐⭐⭐ | [`netexec.md`](netexec.md) |
| **bloodhound** | 把 AD 关系画成图，算「我离域管几步」 | ⭐⭐⭐ | [`bloodhound.md`](bloodhound.md) |
| **evil-winrm** | WinRM 交互式 shell，支持密码/哈希/票据 | ⭐⭐ | [`evil-winrm.md`](evil-winrm.md) |
| **mimikatz** | 从 LSASS/SAM/NTDS 提取明文、哈希、票据 | ⭐⭐⭐⭐ | [`mimikatz.md`](mimikatz.md) |
| **chisel** | HTTP 隧道，把内网端口反向搬到 Kali（单文件） | ⭐⭐⭐ | [`chisel.md`](chisel.md) |
| **ligolo-ng** | TUN 隧道，内网网段像直连一样（支持 UDP/ICMP） | ⭐⭐⭐ | [`ligolo-ng.md`](ligolo-ng.md) |
| **proxychains4** | 让任意 TCP 工具走 SOCKS 代理链 | ⭐⭐ | [`proxychains4.md`](proxychains4.md) |
| **linpeas / winpeas** | 提权枚举套件（PEASS-ng），彩色标注所有可疑点 | ⭐⭐ | [`linpeas.md`](linpeas.md) |
| **linux-exploit-suggester** | 按内核版本匹配公开提权 EXP（含可信度分级） | ⭐⭐⭐ | [`linux-exploit-suggester.md`](linux-exploit-suggester.md) |
| **weevely** | PHP 隐蔽 WebShell + 40 余个后利用模块 | ⭐⭐ | [`weevely.md`](weevely.md) |
| **powershell-empire** | PowerShell/Python 后渗透代理框架（C2） | ⭐⭐⭐⭐ | [`powershell-empire.md`](powershell-empire.md) |

> **读法建议**：
> - Windows/AD 方向先读 **impacket → netexec → bloodhound → evil-winrm → mimikatz**；
> - 网络穿透方向读 **chisel → ligolo-ng → proxychains4**；
> - Linux 提权读 **linpeas → linux-exploit-suggester**；
> - Web 落脚读 **weevely**；完整 C2 框架读 **powershell-empire**（或 [`../12-基础设施与C2/sliver.md`](../12-基础设施与C2/sliver.md)）。

---

## 学习顺序

```
                  ┌──────────────────────────────────────────┐
                  │  0. 概念地基：Windows 认证与凭据来源        │
                  │  NTLM vs Kerberos、NT hash vs NetNTLMv2、  │
                  │  SAM/LSA/NTDS/LSASS 分别在存什么           │
                  │  → 见 impacket.md 第 2 节                  │
                  └───────────────┬──────────────────────────┘
                                  ▼
   1. 我在这台机器上能做什么？  ──► linpeas（枚举）→ linux-exploit-suggester（内核）
                                  │
   2. 我手上这个凭据能打多远？  ──► netexec（批量）→ crackmapexec（对比）
                                  │
   3. 打进去之后怎么操作？      ──► evil-winrm（交互）→ impacket（精确）
                                  │
   4. 凭据从哪来、怎么扩大？    ──► mimikatz（本机）→ impacket-secretsdump（远程）
                                  │
   5. 下一步该打哪里？          ──► bloodhound（攻击路径）
                                  │
   6. 怎么进更深的内网？        ──► chisel / ligolo-ng → proxychains4
                                  │
   7. Web 场景的落脚点          ──► weevely
                                  │
   8. 想要完整 C2 框架          ──► powershell-empire（或 ../12 的 sliver）
```

**建议节奏**：在一套自建 AD 靶场上把下面这条链**完整走通 3 遍**：

```
低权 shell → linpeas 提权 → mimikatz 抓哈希 → netexec 验证凭据范围
   → evil-winrm 落脚 → bloodhound 找路径 → secretsdump 拿域哈希
   → impacket-ticketer 伪造票据 → 全域控制
```

---

## 环境准备

### 攻击机（Kali）

```bash
sudo apt update
sudo apt install -y impacket crackmapexec netexec bloodhound evil-winrm mimikatz \
                    chisel ligolo-ng proxychains4 peass linux-exploit-suggester \
                    weevely powershell-empire

# 常用配套（上游/下游章节）
sudo apt install -y hashcat exploitdb metasploit-framework ncat socat
```

验证：

```bash
command -v impacket-secretsdump nxc crackmapexec evil-winrm nxc chisel ligolo-proxy proxychains4 linpeas weevely
ls /usr/share/windows-resources/mimikatz/
ls /usr/share/peass/
```

配置一次 `proxychains4`：

```bash
sudo cp /etc/proxychains4.conf /etc/proxychains4.conf.bak
sudo sed -i 's/^strict_chain/dynamic_chain/' /etc/proxychains4.conf
grep -A3 '\[ProxyList\]' /etc/proxychains4.conf
```

BloodHound CE 需要一次性初始化（**做一次即可**）：

```bash
sudo bloodhound-setup
sudo bloodhound-start        # Web UI: http://127.0.0.1:8080  默认 admin/admin
```

Empire 首次也要初始化（**默认口令必须立刻改**）：

```bash
sudo powershell-empire setup && sudo powershell-empire server
sudo starkiller-start        # http://127.0.0.1:1337  默认 empireadmin/password123
```

### 靶场（**必须是你拥有或已获书面授权**）

| 靶场 | 类型 | 适合练什么 | 获取方式 |
|------|------|-----------|----------|
| **GOAD**（Game of Active Directory） | 多域 AD 靶场 | BloodHound 路径、Kerberoasting、DCSync、委派滥用、横向 | <https://github.com/Orange-Cyberdefense/GOAD> |
| **自建 AD 实验室** | 1 DC + 2~3 成员机 | 从零理解 AD，权限可控 | 自装 Windows Server（**Host-Only**）+ 域内 Win10 |
| **Metasploitable 2/3** | Linux | Linux 提权（linpeas）、Web 后利用（weevely） | 官方 OVA |
| **TryHackMe** | 在线靶机 | 后渗透系统化练习（含 AD 房间） | 注册后开房间 |
| **HackTheBox** | 在线靶机 | 真实感强，含 AD 机器 | 注册后开靶机 + VPN |
| **VulnHub** | 离线镜像 | 无网络依赖的完整靶机 | 官网下载 OVA |
| **DVWA / Juice Shop** | Web 应用 | WebShell 落点、上传/命令执行 | Docker 一行起 |

网络拓扑建议（**隔离优先**）：

```
[ Kali 攻击机 ] 192.168.56.5
        │  Host-Only / Internal 网络（禁止桥接生产网）
┌───────┴──────────────────────────────┐
│ 域控 DC01  192.168.56.10             │
│ 成员机 WEB01 192.168.56.20           │
│ 成员机 APP01 192.168.56.30           │
│ 双网卡跳板 10.10.20.10（内网侧）      │  ← 用来练隧道与多层穿透
│ 内网主机   10.10.20.5                │
└──────────────────────────────────────┘
```

---

## 环境准备清单（自检）

```bash
# 1) 基础连通
ping -c 2 192.168.56.10

# 2) Windows 核心端口
sudo nmap -sV -p 445,5985,3389,88,389 192.168.56.10

# 3) Impacket 工具齐全
ls /usr/bin/impacket-* | wc -l

# 4) 批量验证工具可用
nxc smb 192.168.56.10                       # 无凭据也能拿到主机指纹与签名状态
crackmapexec smb 192.168.56.10

# 5) 提权枚举脚本就绪
ls -l /usr/share/peass/linpeas/linpeas.sh
ls /usr/share/linux-exploit-suggester/

# 6) 隧道工具
chisel -h | head -5
command -v ligolo-proxy ligolo-agent
proxychains4 --help

# 7) WinRM 通道（靶机需已启用 WinRM）
nxc winrm 192.168.56.20 -u <user> -p '<pass>'

# 8) BloodHound / Empire（可选）
sudo bloodhound-start && curl -sk https://127.0.0.1:8080 -o /dev/null -w '%{http_code}\n'
```

---

## 与其它章节的衔接

| 你手上的东西 | 去哪个工具 |
|--------------|------------|
| 一个 shell，不知道能提权到什么程度 | [`linpeas.md`](linpeas.md) → [`linux-exploit-suggester.md`](linux-exploit-suggester.md) |
| 一个域名/用户名/口令（或哈希） | [`netexec.md`](netexec.md)、[`crackmapexec.md`](crackmapexec.md) |
| 哈希想破解成明文 | `../04-口令攻击/`（hashcat/john） |
| 哈希/票据想直接登录 | [`evil-winrm.md`](evil-winrm.md)、[`impacket.md`](impacket.md) |
| 不知道接下来打哪里 | [`bloodhound.md`](bloodhound.md) |
| 想抓更多凭据 | [`mimikatz.md`](mimikatz.md)、[`impacket.md`](impacket.md) |
| 发现内网但访问不到 | [`chisel.md`](chisel.md)、[`ligolo-ng.md`](ligolo-ng.md)、[`proxychains4.md`](proxychains4.md) |
| Web 应用拿了命令执行 | [`weevely.md`](weevely.md) |
| 需要长期维持访问 | [`powershell-empire.md`](powershell-empire.md)、[`../12-基础设施与C2/sliver.md`](../12-基础设施与C2/sliver.md) |
| 中继/投毒（LLMNR/NTLM Relay） | `../07-嗅探与欺骗/` + `impacket-ntlmrelayx` |
| 事后如何取证分析 | [`../09-数字取证/README.md`](../09-数字取证/README.md) |

---

## ⚠️ 法律与伦理

**本目录收录的工具全部是高风险攻击工具。** 未授权使用可能触犯：

- 《刑法》第 285 条：非法侵入计算机信息系统罪、非法获取计算机信息系统数据罪、**非法控制计算机信息系统罪**；
- 《刑法》第 286 条：破坏计算机信息系统罪；
- 《网络安全法》《数据安全法》《个人信息保护法》（凭据与 AD 数据大量涉及个人信息）。

**使用前提（缺一不可）**：

1. 有**书面授权**（明确目标范围、时间窗、允许手法，尤其是「凭据提取」「C2 植入」「口令爆破强度」需单独确认）；
2. 在**隔离环境**或约定的靶场中进行，避免误伤生产；
3. 与蓝队/运维**事先对齐**，避免真的锁死账号或导致业务中断；
4. 测试结束**清理**所有后门、计划任务、服务与投放文件；
5. 提取的凭据**加密保存、限时销毁**，报告中一律脱敏。
