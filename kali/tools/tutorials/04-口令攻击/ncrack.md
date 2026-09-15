# ncrack（Nmap 风格的网络认证爆破器）

> **一句话**：语法与 Nmap 高度相似的网络认证破解器，带时序模板、连接控制与断点续跑，适合大规模、长周期的认证审计。
> **分类**：口令攻击 ｜ **Kali 包**：`ncrack` ｜ **官方文档**：<https://nmap.org/ncrack/>

## 1. 它解决什么问题

ncrack 由 Nmap 团队开发，定位是「**像用 Nmap 一样做认证审计**」。它的目标用户是需要在企业网络中做**大规模、长时间、可控节奏**认证测试的人。

| 场景 | 更合适的选择 |
| --- | --- |
| 单目标快速试几个密码 | [hydra](hydra.md) |
| 多主机 × 多用户的大批量扫描 | [medusa](medusa.md) |
| **要精细控制连接数/超时/重试/时序，或要跑很长时间** | **ncrack** |
| 要定制 HTTP 请求、做非登录类爆破 | [patator](patator.md) |

ncrack 的差异化能力：

1. **Nmap 式目标语法**：`192.168.1.1`、`192.168.1.0/24`、`192.168.1-20.1`、`10.0.0-255.1-254`、`scanme.nmap.org` 都能直接写。
2. **可直接吃 Nmap 输出**：`-iX nmap.xml` / `-iN scan.txt`，把扫描结果直接转成攻击目标。
3. **时序模板 `-T0~5`**：从「偏执模式」到「疯狂模式」，无需手工推算 `-t`。
4. **服务级参数**（`cl`/`CL`/`at`/`cd`/`cr`/`to`）：可以针对每个服务单独调优。
5. **`--resume` / `--save`**：长任务断点续跑。

## 2. 工作原理

### 2.1 与 Nmap 的架构关系

ncrack 与 Nmap 共用底层网络库（nsock），因此：

- **动态自适应**：依据网络反馈自动调整并发与超时，网络抖动时不会像固定并发工具那样大面积误判。
- **时序模板**：`-T0`（偏执，5 分钟一探）到 `-T5`（疯狂，假设极快网络）。默认是 `-T3`。
- **运行时交互**：运行中按 `v` 提高详细度、`p` 暂停、`q` 退出，与 Nmap 一致。

### 2.2 服务规范语法

ncrack 有两种指定服务的方式：

```text
# 标准写法：service://target
ssh://192.168.56.10
rdp://192.168.56.10:3389

# 非标准写法：用 -p 统一指定服务，作用于所有目标
ncrack -p ssh,ftp:3500,25 192.168.56.10 192.168.56.11
#                              ↑ 这里 3500 是 ssh 的端口，25 是 ftp 的端口（顺序对应）
```

**服务级参数**写在目标后面，用逗号分隔：

```text
ssh://10.0.0.10,at=10,cl=30      # 这个主机上 ssh：每次连接试 10 个凭据，最少 30 条并发连接
```

作用域有三种：

| 形式 | 作用范围 |
| --- | --- |
| `service://target,key=val` | **该主机**的该服务 |
| `-m ssh:at=50` | 所有 **该类型服务** |
| `-g cd=3000` | **全局** |

### 2.3 时序参数的含义

| 参数 | 全称 | 含义 |
| --- | --- | --- |
| `cl` | min connection limit | 最少并发连接数 |
| `CL` | max connection limit | 最多并发连接数 |
| `at` | authentication tries | **每条连接**上尝试多少个凭据（然后重连） |
| `cd` | connection delay | 每次发起连接之间的延迟 |
| `cr` | connection retries | 连接重试次数上限 |
| `to` | time-out | 该服务的总时间上限 |

**`at` 是最能提升速度的参数**：同一条 TCP 连接上连续做多次认证尝试，省掉了重复的 TCP/协议握手开销。但它也更容易触发服务端的「同连接失败计数」防护。

### 2.4 与离线破解的速度对比

与 [hydra](hydra.md)/[medusa](medusa.md) 一样，ncrack 受网络往返与服务端策略约束，速度只能是**每秒几十到几百次**量级，远低于 [hashcat](hashcat.md) 的离线 GPU 速度。因此 ncrack 的正确用法是**小而精的字典 + 大量目标**，而不是**大字典 + 少量目标**。

## 3. 安装与快速上手

```bash
sudo apt install ncrack
ncrack -h 2>&1 | head -50
```

最短工作流：

```bash
# 单目标
ncrack -v --user root -P /usr/share/wordlists/rockyou.txt 192.168.56.10:22

# 多目标 + 从 Nmap XML 读目标
ncrack -v -T4 -iX ~/nmap.xml --user admin -P pw.txt -p ssh,rdp
```

## 4. 核心参数详解

### 4.1 目标指定

| 参数 | 作用 | 建议 |
| --- | --- | --- |
| 位置参数 | 主机名 / IP / CIDR / 网段范围 | `192.168.0.0/24`、`10.0.0-255.1-254` |
| `-iL FILE` | 从文件读主机/网段列表 | 最常用 |
| `-iX FILE` | 从 Nmap `-oX` XML 输出读 | **与 Nmap 串联的关键** |
| `-iN FILE` | 从 Nmap `-oN` 普通输出读 | 只有普通输出时用 |
| `--exclude` | 排除主机/网段 | **保护关键设备不被误测，强烈建议使用** |
| `--excludefile FILE` | 从文件读排除列表 | 同上 |
| `-sL` / `--list` | 只列目标与服务，不实际连接 | **开跑前先自检目标范围** |

### 4.2 服务指定

| 参数 | 作用 |
| --- | --- |
| `-p service-list` | 对所有非标准写法目标应用的服务列表 |
| `service://target` | 标准写法，可带端口与主机级参数 |
| `-m service:options` | 服务类型级参数 |
| `-g options` | 全局参数 |
| `--connection-limit N` | 全局总并发连接上限 |
| `--stealthy-linear` | 每台主机只用一条连接、串行推进；**覆盖所有其他时序参数** |

### 4.3 时序与性能

| 参数 | 作用 | 建议 |
| --- | --- | --- |
| `-T0..-T5` | 时序模板，越大越快 | 局域网靶场 `-T4`；跨公网 `-T2`；真实企业设备 `-T1` |
| `cl=N` | 最少并发连接 | — |
| `CL=N` | 最多并发连接 | 与 `--connection-limit` 配合做总闸 |
| `at=N` | 每条连接尝试多少凭据 | **提速首选**；但更易触发同连接防护 |
| `cd=3000` | 连接间隔（毫秒或带单位） | 规避限流的最直接手段 |
| `cr=N` | 连接重试次数 | 丢包网络下防误判 |
| `to=1h` | 服务总超时 | 长任务必设 |

> 时间单位：默认秒；可加 `ms`（毫秒）、`m`（分）、`h`（时），例如 `cd=500ms`、`to=1h`。

### 4.4 认证参数

| 参数 | 作用 | 建议 |
| --- | --- | --- |
| `-U FILE` | 用户名文件 | — |
| `--user list` | 逗号分隔的用户名列表 | 数量少时方便 |
| `-P FILE` | 口令文件 | 配 [rockyou](wordlists.md) |
| `--pass list` | 逗号分隔口令列表 | 口令喷洒时用 |
| `--passwords-first` | 先遍历口令再换用户 | 默认相反（先遍历用户） |
| `--pairwise` | 用户名与口令成对推进 | 两边数量相同时避免笛卡尔积 |

### 4.5 输出与恢复

| 参数 | 作用 |
| --- | --- |
| `-oN FILE` | 普通格式输出 |
| `-oX FILE` | XML 格式输出 |
| `-oA BASENAME` | 同时输出两种格式 |
| `-v` / `-vv` | 提高详细度，可叠加 |
| `-d[level]` | 调试级别，最高 10 有意义 |
| `--log-errors` | 错误也写入输出文件 |
| `--append-output` | 追加而非覆盖 |
| `--resume FILE` | 恢复上次会话 |
| `--save FILE` | 指定恢复文件名 |
| `-f` | 每个服务找到一组凭据即停 |
| `-6` | 启用 IPv6 |
| `--proxy type://host:port` | 通过 socks4/4a/http 代理连接 |
| `--datadir DIR` | 自定义数据目录 |

### 4.6 支持的模块

`SSH, RDP, FTP, Telnet, HTTP(S), Wordpress, POP3(S), IMAP, CVS, SMB, VNC, SIP, Redis, PostgreSQL, MQTT, MySQL, MSSQL, MongoDB, Cassandra, WinRM, OWA, DICOM`

## 5. 实战演练

**环境声明**：以下全部在**你自己的隔离实验环境**中执行（自建 Kali + 靶机，host-only 网络）。**严禁对任何未授权主机执行**，并且**务必用 `--exclude` 保护你的网关和其他关键设备**。

### 场景 1：单目标 RDP 爆破（理解服务级参数）

```bash
ncrack -v -T4 --user victim -P ~/pw-small.txt rdp://192.168.56.10:3389,at=3,CL=2
```

输出：

```
Starting Ncrack 0.7 ( http://ncrack.org ) at 2026-09-15 10:40 CST

Discovered credentials for rdp on 192.168.56.10 3389/tcp:
192.168.56.10 3389/tcp rdp: 'victim' 's3cr3t'

Ncrack done: 1 service scanned in 43.00 seconds.
Probes sent: 128 | timed-out: 0 | prematurely-closed: 0
```

- `at=3`：每条连接试 3 个口令再重连。
- `CL=2`：最多 2 条并发连接——**RDP 服务对并发很敏感，高并发容易让目标会话异常**，这是为什么这里显式压低。
- `Discovered credentials for rdp …`：**命中行**。

### 场景 2：与 Nmap 串联（ncrack 的招牌用法）

**步骤 1：先用 Nmap 找到开放认证服务的机器**

```bash
nmap -p 22,3389,21,3306,5432 --open -oX ~/nmap-auth.xml 192.168.56.0/24
```

**步骤 2：先干跑一遍，确认目标范围正确**

```bash
ncrack -sL -iX ~/nmap-auth.xml --user admin -P ~/pw-small.txt
```

`-sL` 会列出 ncrack 解析出的所有 host+service 组合。**这一步非常重要**：确认里面没有你不该碰的机器。

**步骤 3：正式执行，显式排除网关**

```bash
ncrack -v -T3 -iX ~/nmap-auth.xml \
       --user admin --user root \
       -P ~/pw-small.txt \
       --exclude 192.168.56.1 \
       -g CL=5,to=30m \
       --save ~/ncrack-session \
       -oA ~/ncrack-result
```

参数解读：

| 参数 | 含义 |
| --- | --- |
| `-iX` | 目标来自 Nmap XML |
| `--exclude 192.168.56.1` | **排除网关**，防止把自己网络打挂 |
| `-g CL=5,to=30m` | 全局：总并发 ≤ 5，每个服务最多跑 30 分钟 |
| `--save` | 保存会话，可断点续跑 |
| `-oA` | 输出普通格式 + XML |

**步骤 4：中断后恢复**

```bash
ncrack --resume ~/ncrack-session
```

### 场景 3：低速慢猜（规避锁定）

真实的账户锁定策略通常是「5 次失败锁定 15 分钟」。要绕开它，需要**极低速率 + 分散用户**：

```bash
ncrack -v -T0 \
       -U ~/users.txt -P ~/spray-3.txt \
       -p ssh \
       --passwords-first \
       -g cd=20000,CL=1 \
       192.168.56.10 \
       -oN ~/slow-scan.txt
```

| 参数 | 作用 |
| --- | --- |
| `-T0` | 最慢的时序模板 |
| `cd=20000` | 每次连接间隔 20 秒 |
| `CL=1` | 只允许 1 条并发连接 |
| `--passwords-first` | 每个用户只试 3 个口令（`spray-3.txt` 只有 3 行），避免单账户被锁定 |

这不是「更快的攻击」，而是**更慢、更隐蔽的审计方式**——同时也是蓝队需要能检测的模式（低频、多账号、长期）。

## 6. 输出解读

| 输出 | 含义 | 下一步 |
| --- | --- | --- |
| `Discovered credentials for <svc> on H P/tcp:` | **命中**，下一行给出 `'user' 'pass'` | 手工验证；确认后停止该服务 |
| `Failed to connect` | 服务不可达 | 检查端口/防火墙 |
| `Connection refused` | 端口未开放 | 用 `-sL` 或 nmap 复核服务列表 |
| `Login failed: invalid credentials`（`-vv`） | 普通失败 | 正常 |
| `Service <svc> not supported` | 模块不支持该协议变种 | 换 hydra/patator |
| `Ncrack done: N service scanned in T seconds` | 收尾统计 | — |
| `Probes sent / timed-out / prematurely-closed` | 网络质量指标 | `timed-out` 占比高 → 降 `-T`、加 `cr` |
| `0 credentials found` | 未命中 | 换字典/用户表，或该服务用密钥/MFA |

`-oA` 生成的 XML 可以用 Nmap 生态的解析脚本继续处理。

## 7. 与其他工具配合

```text
[nmap --open -oX]  ─┐
                    ├→ ncrack -iX  ─→ 弱口令清单（-oX）
[--exclude 关键设备] ┘
                              ↓
                     [john / hashcat] 登录后 dump 哈希，离线扩大
```

- **{nmap, ncrack}**：ncrack 的 `-iX` 直接消费 Nmap XML，这是最顺滑的工作流。
- **{ncrack, hydra}**：ncrack 报「模块不支持」的服务，用 hydra 单点重试（hydra 协议覆盖更广）。
- **{ncrack, medusa}**：需要极高吞吐的多目标扫描时用 medusa；需要精细时序控制时用 ncrack。
- **{ncrack, patator}**：需要定制 HTTP 请求或非标准认证流程时用 patator。

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `-iX` 报 XML 解析错误 | Nmap XML 不完整或被截断 | 重新生成；确认 nmap 跑完 |
| 全部 `Connection refused` | `-p` 指定的服务端口写错 | 记住非标准写法的端口**按服务列表顺序对应**；建议改用标准写法 `ssh://host:port` |
| `Failed to resolve` | DNS 问题 | 用 IP |
| 大量 `timed-out` | 网络质量差或 `-T` 太高 | 降 `-T`，加 `cr`、`cd` |
| 目标看门狗/RDP 会话异常 | 并发连接过多 | 显式设 `CL=1`~`CL=2` |
| 跑一半被打断 | 会话未保存 | 用 `--save`；中断后用 `--resume` |
| `at=` 调高后目标大量拒绝 | 同连接失败计数触发防护 | 降 `at`，加 `cd` |
| 结果 XML 里没有命中记录 | `-f` 之外还用了 `-oA` 但被覆盖 | 确认文件名；用 `--append-output` |
| 不小心扫到生产设备 | **没设 `--exclude`** | 立即停止；以后一律先 `-sL` 自检 + 显式排除 |

## 9. 防御视角（蓝队）

| 风险 | 检测 | 缓解 |
| --- | --- | --- |
| Nmap 先扫描、ncrack 后爆破 | 端口扫描告警（同源 IP 大量 SYN）是最早的信号 | 部署端口扫描检测；关闭不必要端口 |
| 同连接多次认证（`at` 特征） | 单条 TCP 连接上出现多条认证失败记录 | 服务端限制「同连接失败次数」，强制重连 |
| `--stealthy-linear` 式极慢扫描 | 单连接、长周期、跨多主机的低频失败 | 长期日志聚合与基线偏离检测（单点窗口检测不到） |
| RDP/SSH 被爆破 | 事件 ID 4625 突增；SSH 日志 `Failed password` | 强制 MFA、限制来源 IP、RDP 走网关、SSH 只用密钥 |
| 关键设备被误测 | — | 蓝队可主动要求红队在 ROE 中列出排除清单 |

**蓝队要点**：ncrack 的 `-T0` + `cd=20000` 这类配置说明**「低频分散」的攻击无法靠阈值规则发现**，必须靠**跨主机、跨时间的聚合分析**。

## 10. 参考

- 官方文档与手册：<https://nmap.org/ncrack/>、<https://nmap.org/ncrack/man.html>
- Kali 工具页：<https://www.kali.org/tools/ncrack/>
- 本机手册：`man ncrack`、`ncrack -h`
- 相关：[hydra](hydra.md)、[medusa](medusa.md)、[patator](patator.md)、[wordlists](wordlists.md)

## ⚠️ 法律与伦理

未经授权对他人系统或网络设备进行认证猜测，可能构成《中华人民共和国刑法》第二百八十五条「非法侵入计算机信息系统罪」/「非法获取计算机信息系统数据罪」，以及《网络安全法》第二十七条所禁止的行为。ncrack 的批量特性会使其行为性质更严重。

**本教程仅适用于**：你自己的网络与设备、有书面授权的渗透测试与合规审计、CTF 靶场、隔离教学环境。**务必在授权范围内使用 `--exclude` 明确排除关键设备**，任何「顺手测一下」都可能构成越权。
