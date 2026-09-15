# 06 · 漏洞利用（Exploitation）

> 本目录是 Kali 工具精讲教程的第 6 篇：把「发现漏洞」变成「拿到会话」。
> 上游：`../05-无线攻击/` ｜ 下游：`../07-嗅探与欺骗/`、[`../08-后渗透/`](../08-后渗透/)
> 相关索引：[`../../index.md`](../../index.md) ｜ 分类速查：[`../../catalog/exploitation.md`](../../catalog/exploitation.md)、[`../../by-attack/initial-access.md`](../../by-attack/initial-access.md)

---

## 工具清单

| 工具 | 一句话 | 难度 | 教程 |
|------|--------|------|------|
| **metasploit-framework** | 漏洞利用全流程框架：模块体系 + 数据库 + workspace + 会话管理 | ⭐⭐⭐ | [`metasploit-framework.md`](metasploit-framework.md) |
| **msfvenom** | Payload 生成器：一条命令把反弹 shell 输出成 exe/elf/php/war/raw | ⭐⭐ | [`msfvenom.md`](msfvenom.md) |
| **searchsploit** | Exploit-DB 本地离线检索，并把 PoC 取出来改改就能跑 | ⭐⭐ | [`searchsploit.md`](searchsploit.md) |
| **beef-xss** | 浏览器利用框架：hook 住浏览器后做客户端侧后利用与内网侦察 | ⭐⭐⭐ | [`beef-xss.md`](beef-xss.md) |

> 三个工具的定位差异：**searchsploit 负责「找」，msfvenom 负责「造」，Metasploit 负责「打与管」**，BeEF 负责「浏览器侧」。
> 漏洞成因与原理分析请配合 `kali/tools/by-attack/` 下的分类索引阅读；漏洞库与编号规范见 [`../../catalog/top10.md`](../../catalog/top10.md)。

---

## 学习顺序

```
1. metasploit-framework.md   ← 先建立「框架 + 数据库 + 会话」的整体心智模型
        │
        ├─► 2. searchsploit.md      ← 学会在没有现成模块时取用公开 PoC
        │
        ├─► 3. msfvenom.md          ← 学会自己生成 Payload 并配 handler
        │
        └─► 4. beef-xss.md          ← 客户端方向：浏览器 hook 与内网侦察
                     │
                     ▼
        进入 08-后渗透（提权 / 凭据 / 隧道 / 横向）
```

**建议节奏**：先只用自制靶机把「`db_nmap` → `services` → `search` → `use` → `check` → `run` → `sessions`」这条链跑通 3 遍，再学 Payload 与 PoC 适配。

---

## 环境准备

### 攻击机（Kali）

```bash
sudo apt update
sudo apt install -y metasploit-framework exploitdb beef-xss

sudo msfdb init                 # 初始化 Metasploit 数据库
sudo systemctl enable --now postgresql
msfconsole -q -x "db_status; exit"
```

验证：

```bash
command -v msfconsole msfvenom searchsploit beef-xss-start
ls /usr/share/exploitdb/ | head
```

### 靶机（**必须是你拥有或已获授权的环境**）

| 靶场 | 获取方式 | 适合练习 |
|------|----------|----------|
| **Metasploitable 2 / 3** | 官方 OVA，导入 VirtualBox/VMware | Metasploit 入门（vsftpd、UnrealIRCd、Samba） |
| **DVWA / bWAPP / Juice Shop** | Docker 一行起：`docker run -d -p 80:80 vulnerables/web-dvwa` | Web 类 EXP、BeEF hook（XSS） |
| **VulnHub** | 下载 OVA 离线靶机 | 无网络依赖的完整靶机 |
| **HackTheBox / TryHackMe** | 注册后开靶机（免费档可用） | 真实感强的靶机，自带 VPN |
| **自建 Windows 评测虚拟机** | 自装未打补丁的 Win10/Server（**断网或仅主机网络**） | SMB/WinRM、后渗透、凭据抓取 |

网络拓扑建议：

```
[ Kali 攻击机 ] 192.168.56.101
        │  仅主机网络（Host-Only）/ 内部网络（Internal）
[ 靶机 A ] 192.168.56.102   ← Metasploitable
[ 靶机 B ] 192.168.56.50    ← Windows 客户端（配合 BeEF 勾选）
```

**把靶机放在 Host-Only 或 Internal 网络，禁止桥接到生产网段。**

---

## 环境准备清单（自检）

```bash
# 1) 攻击机与靶机是否互通
ping -c 2 192.168.56.102

# 2) 靶机服务是否可见
sudo nmap -sV -p 21,22,80,445 192.168.56.102

# 3) Metasploit 数据库是否正常
msfconsole -q -x "db_status; workspace; exit"

# 4) Exploit-DB 索引是否可用
searchsploit vsftpd | head

# 5) BeEF 是否可启动（用完立刻 stop）
sudo beef-xss-start && ss -lntp | grep 3000 && sudo beef-xss-stop
```

---

## 相关链接

- 上游情报收集与扫描：`../01-信息搜集/`
- 口令攻击（拿到 hash 之后）：[`../04-口令攻击/`](../04-口令攻击/)
- 嗅探与欺骗（ARP/DNS 中间人）：[`../07-嗅探与欺骗/`](../07-嗅探与欺骗/)
- 后渗透完整链条：[`../08-后渗透/README.md`](../08-后渗透/README.md)
- 基础设施与 C2：[`../12-基础设施与C2/README.md`](../12-基础设施与C2/README.md)

## ⚠️ 法律与伦理

本目录所有工具均属攻击性工具。**只能在书面授权的渗透测试、CTF 竞赛、自建靶场与教学环境中使用。** 未授权利用可能触犯《刑法》第 285、286 条及《网络安全法》，并需承担民事赔偿。上机前请确认授权范围（目标、时间窗、允许手法），全程留痕，测试结束清理后门与凭据。
