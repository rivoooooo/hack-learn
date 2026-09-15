# patator（模块化万能爆破框架）

> **一句话**：用「生成器 + 模块 + 响应动作」三段式模型，对任意协议做登录爆破、用户枚举、内容模糊测试。
> **分类**：口令攻击 ｜ **Kali 包**：`patator` ｜ **官方文档**：<https://github.com/lanjelot/patator>

## 1. 它解决什么问题

[hydra](hydra.md)、[medusa](medusa.md)、[ncrack](ncrack.md) 都是「**固定的登录爆破器**」——它们的模块写死了请求格式。当你遇到这些情况时，它们就无能为力：

- 登录接口需要先发一个请求拿 token，再带 token 提交；
- 需要按响应里的**某个字段**判断成功，而不是简单的关键字；
- 目标不是「登录」而是「枚举」：用 SMTP `VRFY` 枚举用户、用 `dns_reverse` 做反向解析、用 `snmp_login` 猜 community string；
- 需要对 HTTP 参数做**模糊测试**。

patator 就是解决这类问题的：它把一次尝试抽象成三段：

```
[生成器 Generator]        →    [模块 Module]         →    [动作 Action]
 从文件/组合/范围产生          用这些值构造一个请求         根据响应决定
 user / password / IP           并发发出去                    忽略 / 记录 / 重试
```

对比：

| 工具 | 适用 |
| --- | --- |
| [hydra](hydra.md) | 标准协议、单机、快速验证 |
| [medusa](medusa.md) | 多主机 × 多用户的大批量扫描 |
| [ncrack](ncrack.md) | 需要精细时序控制的大规模审计 |
| **patator** | **非标准认证流程、自定义请求、枚举与模糊测试** |

## 2. 工作原理

### 2.1 三段式模型

**① 生成器（Generator）** —— 决定「候选值从哪来」：

| 生成器 | 语法 | 含义 |
| --- | --- | --- |
| `FILE` | `user=FILE0 0=logins.txt` | 从文件逐行读；`0` 是文件编号 |
| `COMBO` | `user=COMBO00 password=COMBO01 0=combos.txt` | 从同一个文件**成对**取值（按列），避免笛卡尔积 |
| `RANGE` | `payload=RANGE1 1=int:0-1` | 数字/字符区间迭代 |
| `NET` | `host=NET0 0=8.8.8.0/24` | 把 CIDR / IP 范围展开成主机列表 |

`FILE0` 里的 `0` 与 `0=文件名` 的 `0` 对应；多个生成器用不同的编号（`FILE0`、`FILE1`、`COMBO00`/`COMBO01`、`RANGE2`…）。

**② 模块（Module）** —— 决定「请求长什么样、发到哪里」。模块把生成器的值填进请求里，并发发出。

**③ 动作（Action）** —— 决定「收到响应后干什么」。这是 patator 最灵活的地方：

```text
-x ignore:fgrep='Access denied for user'     # 响应里含此串 → 忽略（视为失败）
-x ignore:code=500                            # 状态码 500 → 忽略
-x ignore:time=0-3                            # 3 秒内返回 → 忽略（太快通常意味着被拒）
-x ignore,reset,retry:code=500                # 复合动作：忽略 + 重置连接 + 重试
```

| 动作 | 含义 |
| --- | --- |
| `ignore` | 丢弃这条结果，不打印 |
| `reset` | 重置/重建连接 |
| `retry` | 重试这次尝试 |
| `free` | 释放资源 |
| `stop` | 停止整个任务 |

**`-x` 在「收到非预期响应」时触发，`-y` 在「收到预期响应」时触发。** 语法统一为：

```text
-[xy] [action[,action...]]:[test][!=]=value
```

可用的 `test` 包括 `code`、`size`、`mesg`、`time`、`fgrep`、`egrep` 等。

### 2.2 为什么要用 actions 而不是自己写脚本

因为**「区分失败与成功」是爆破中最容易出错的一步**。SMTP 服务器可能在 `250` 成功码里也返回失败文本；HTTP 表单可能永远返回 200 但正文内容不同。patator 把这件事显式化成一条可读的规则：

```bash
-x ignore:fgrep='Login incorrect'
```

——「响应正文里包含 `Login incorrect` 的就是失败」。这条规则写在命令行上，可审计、可复现，比埋在 Python 脚本里的 `if` 要清晰得多。

### 2.3 速度上限与前面几节相同

patator 同样是在线爆破：网络往返 + 服务端策略决定速度上限。不同于 [hashcat](hashcat.md) 的离线 GPU 路径，patator 每秒只能做到**几十到几百次尝试**。**不要用 patator 跑大字典**。

### 2.4 支持的模块

```text
ftp_login     ssh_login     telnet_login   smtp_login     smtp_vrfy
smtp_rcpt     finger_lookup http_fuzz      rdp_gateway    ajp_fuzz
pop_login     pop_passd     imap_login     ldap_login     dcom_login
smb_login     smb_lookupsid rlogin_login   vmauthd_login  mssql_login
oracle_login  mysql_login   mysql_query    rdp_login      pgsql_login
vnc_login     dns_forward   dns_reverse    snmp_login     ike_enum
unzip_pass    keystore_pass sqlcipher_pass umbraco_crack  tcp_fuzz
dummy_test
```

注意其中几个非登录模块的价值：

- `smtp_vrfy` / `smtp_rcpt` / `finger_lookup`：**用户枚举**。
- `dns_forward` / `dns_reverse`：DNS 查询与批量反向解析。
- `smb_lookupsid`：通过 SID 枚举 Windows 用户。
- `mysql_query`：**对 SQL 查询做爆破**（不只登录）。
- `unzip_pass` / `keystore_pass` / `sqlcipher_pass`：本地文件的离线口令测试（这部分是「本地」而非网络）。
- `http_fuzz`：HTTP 模糊测试。

## 3. 安装与快速上手

```bash
sudo apt install patator
patator -h                       # 全局帮助 + 模块列表
patator --help-modules           # 所有模块的帮助
patator ssh_login --help         # 单个模块的完整参数
```

**patator 的正确启动姿势永远是先看模块帮助**：

```bash
patator <module> --help
```

冒烟测试（用自带测试模块）：

```bash
patator dummy_test name=FILE0 0=<(printf 'a\nb\nc\n')
```

## 4. 核心参数详解

> 说明：patator 的参数分两层——**全局参数**（`patator -h` 显示）与**模块参数**（`patator <模块> --help` 显示）。模块参数随模块不同而变化，因此下面把「通用语法」和「典型模块参数」分开讲。**写脚本前务必以本机 `--help` 输出为准。**

### 4.1 全局与调用形式

| 参数 / 形式 | 作用 | 建议 |
| --- | --- | --- |
| `patator <模块> [KEY=VALUE ...]` | 模块名后用 `key=value` 传参 | 核心调用形式 |
| `-h` | 全局帮助（含模块列表） | 第一站 |
| `--help-modules` | 所有模块及其参数 | 第二站 |
| `<模块> --help` | 单模块完整参数与示例 | **写命令前必看** |
| `-x <动作>:<条件>` | 收到**非预期**响应时的动作 | 用来「忽略失败」，见下 |
| `-y <动作>:<条件>` | 收到**预期**响应时的动作 | 用来「锁定成功」 |
| `-e <动作>` | 出错时的动作 | 网络不稳时配合 `retry` |
| `-l <目录>` | 把每个响应保存到该目录 | 事后逐个比对响应时**极其有用** |
| `-L <文件>` | 结果写文件 | 审计留档 |
| `-o <文件>` | 保存结果 | — |
| `--timeout=<秒>` | 单次请求超时 | 高延迟链路调大 |
| `--max-retries=<N>` | 最大重试次数 | 丢包网络下防误判 |
| `--rate-limit=<N>` | 限制每秒请求数 | **规避账户锁定与限流的关键参数** |
| `--resume=<字符串>` | 用之前保存的状态续跑 | 长任务被打断后 |

### 4.2 生成器语法（所有模块通用）

| 写法 | 含义 |
| --- | --- |
| `user=FILE0 0=users.txt` | 从 `users.txt` 逐行读用户名 |
| `password=FILE1 1=pw.txt` | 从另一个文件读口令（**两个 FILE 会产生笛卡尔积**） |
| `user=COMBO00 password=COMBO01 0=combos.txt` | 从同一个文件按列成对读，**不做笛卡尔积** |
| `payload=RANGE1 1=int:0-1` | 数字区间 |
| `host=NET0 0=192.168.1.0/24` | 展开网段 |

**关键区别**：`FILE0 + FILE1` 是笛卡尔积（N×M 次尝试），`COMBO00 + COMBO01` 是成对（N 次尝试）。**大多数审计场景应该用 `COMBO`**——它更精确、更不容易触发锁定。

### 4.3 动作条件（`-x` / `-y` 的 `<条件>`）

| 条件 | 示例 | 含义 |
| --- | --- | --- |
| `code` | `-x ignore:code=500` | HTTP/协议状态码等于 |
| `code!=` | `-x ignore:code!=0` | 状态码不等于 |
| `size` | `-x ignore:size=1234` | 响应长度 |
| `mesg` | `-x ignore:mesg='Login incorrect.'` | 消息字段等于 |
| `time` | `-x ignore:time=0-3` | 响应耗时落在区间内 |
| `fgrep` | `-x ignore:fgrep='Access denied for user'` | 正文**包含**该固定字符串 |
| `fgrep!=` | `-x ignore:fgrep!=google.com` | 正文**不包含** |
| `egrep` | `-x ignore:egrep='error\|failed'` | 正则匹配 |
| 复合 | `-x ignore,reset,retry:code=500` | 多个动作同时生效 |

### 4.4 典型模块参数（举例）

以下是从 Kali 官方示例中确认的用法，**具体参数名以 `patator <模块> --help` 为准**：

| 模块 | 典型参数 |
| --- | --- |
| `mysql_login` | `user=`、`password=`、`host=` |
| `ssh_login` | `host=`、`user=`、`password=`、`port=` |
| `http_fuzz` | `url=`、`body=`、`method=`、`before_urls=`、`accept_cookie=`、`follow=` |
| `smtp_vrfy` | `host=`、`user=` |
| `dns_reverse` | `host=`（可配 `NET0` 生成器） |
| `unzip_pass` | `file=`、`password=` |

## 5. 实战演练

**环境声明**：以下全部在**你自己搭建的隔离靶场**中执行（自建 Kali + 自建 MySQL/HTTP 服务/靶机）。**严禁对任何未授权主机执行**。

### 场景 1：MySQL 登录爆破（官方示例的完整解读）

```bash
# 1) 先看模块参数
patator mysql_login --help | head -40

# 2) 准备字典
printf 'toor\nroot\npassword\n123456\n' > ~/passes.txt

# 3) 执行：user 固定为 root，password 从文件读
patator mysql_login user=root password=FILE0 0=~/passes.txt \
    host=127.0.0.1 \
    -x ignore:fgrep='Access denied for user'
```

**预期输出**

```
12:30:36 patator    INFO - Starting Patator 1.1.0
12:30:36 patator    INFO -
12:30:36 patator    INFO - code  size | candidate                          |   num | mesg
12:30:36 patator    INFO - ----------------------------------------------------------------------
12:30:37 patator    INFO - 0     16   | toor                               |  4493 | 5.5.37-0+wheezy1
12:30:37 patator    INFO - Hits/Done/Skip/Fail/Size: 1/4493/0/0/4493, Avg: 3582 r/s, Time: 0h 0m 1s
```

逐列解读：

| 列 | 含义 |
| --- | --- |
| `code` | 协议返回码 |
| `size` | 候选值长度 |
| `candidate` | **正在尝试的候选值**（这里是口令 `toor`） |
| `num` | 已尝试的序号 |
| `mesg` | 响应消息（这里是 MySQL 版本号 `5.5.37-0+wheezy1`——**这本身就是有价值的情报**） |
| `Hits/Done/Skip/Fail/Size` | 命中 / 已完成 / 跳过 / 失败 / 总数 |

**关键点**：`-x ignore:fgrep='Access denied for user'` 让所有「拒绝访问」的行被丢弃，**屏幕上剩下的就只有命中**。这就是 patator 的设计哲学。

### 场景 2：HTTP 表单 + 动态 token（patator 的杀手场景）

假设你自己的靶场登录页会先返回一个 token，提交时必须带上它。

```bash
patator http_fuzz \
    url='http://192.168.56.10/login.php' \
    method=POST \
    body='username=admin&password=FILE0&token=TOKEN' \
    0=~/passes.txt \
    before_urls='http://192.168.56.10/login.php' \
    accept_cookie=1 \
    follow=0 \
    -x ignore:fgrep='Username or password incorrect'
```

| 参数 | 作用 |
| --- | --- |
| `url=` | 目标地址 |
| `method=POST` | 请求方法 |
| `body=` | 请求体，`FILE0` 是口令占位符 |
| `before_urls=` | **先访问这个 URL**（拿 cookie / token） |
| `accept_cookie=1` | 接受并沿用 cookie |
| `follow=0` | 不跟随重定向（避免成功后被 302 掩盖差异） |
| `-x ignore:fgrep=...` | 失败判定 |

**关于动态 token**：patator 的 `before_urls` 能处理会话 cookie，但**不能自动提取并回填页面里的 CSRF token**。这类场景需要写 patator 脚本（Python 插件）或在 `before_urls` 之后再发一次带正则提取的请求。**如果 token 是硬需求，正确做法是写一个小 Python 脚本，而不是硬凑命令行**——patator 的模块化设计正是为了让你能方便地扩展。

### 场景 3：用户枚举（非登录型爆破）

这是 patator 区别于 hydra/medusa 的地方——**枚举**。

```bash
# SMTP VRFY 枚举有效邮箱用户
patator smtp_vrfy host=192.168.56.10 user=FILE0 0=~/users.txt \
    port=25 -x ignore:fgrep='User unknown'

# DNS 反向解析一批网段
patator dns_reverse host=NET0 0=192.168.56.0/24 \
    -x ignore:code=3
```

输出解读：

- `smtp_vrfy`：**没有被 `ignore` 掉的行就是「用户存在」**——反过来说，`-x ignore` 里的条件就是「不存在的特征」。
- `dns_reverse`：`code=3` 是 DNS 的 NXDOMAIN，忽略掉 = 只保留有 PTR 记录的主机。

### 场景 4：低速慢猜（用 `--rate-limit` 规避锁定）

```bash
patator ssh_login host=192.168.56.10 \
    user=COMBO00 password=COMBO01 0=~/combos.txt \
    port=22 \
    --rate-limit=0.2 \
    --timeout=10 \
    -x ignore:fgrep='Permission denied'
```

- `COMBO00/COMBO01`：用户名与口令成对，**不做笛卡尔积**。
- `--rate-limit=0.2`：每秒 0.2 次请求（即 5 秒一次）。
- `-x ignore:fgrep='Permission denied'`：丢弃失败行。

这种配置对「账户锁定」策略是无效的——因为每个账号 5 分钟才被试一次。

## 6. 输出解读

```
code  size | candidate           |   num | mesg
--------------------------------------------------------------------------------------
0     16   | toor                |  4493 | 5.5.37-0+wheezy1
Hits/Done/Skip/Fail/Size: 1/4493/0/0/4493, Avg: 3582 r/s, Time: 0h 0m 1s
```

| 字段 | 含义 | 下一步 |
| --- | --- | --- |
| `code` | 协议状态码 | 异常的 `code` 值往往意味着「这条不是普通失败」 |
| `size` | 候选长度 | 排错用 |
| `candidate` | 当前候选值 | **命中时这里就是答案** |
| `num` | 序号 | 估算进度 |
| `mesg` | 响应消息 | **常含版本号等情报**（如 MySQL 版本） |
| `Hits/Done/Skip/Fail/Size` | 命中/完成/跳过/失败/总数 | `Fail` 高说明网络或参数有问题 |
| `Avg: N r/s` | 平均速率 | 与 `--rate-limit` 对照 |
| `Time:` | 已运行时长 | — |

**判断成功**：屏幕上**没有被 `-x ignore` 过滤掉的任何行**都是「非普通失败」——需要人工审视。这是 patator 与 hydra 输出逻辑最大的区别：**它不告诉你是「成功」，它告诉你是「不是我们认识的失败」**。

如果不确定条件怎么写，用 `-l <目录>` 把所有响应落盘，然后逐个 `grep` 比对：

```bash
patator http_fuzz url=... -l /tmp/responses/
grep -rl 'incorrect' /tmp/responses/ | wc -l      # 有多少条是失败
ls /tmp/responses/ | wc -l                        # 总响应数
```

## 7. 与其他工具配合

```text
[枚举] patator smtp_vrfy / smb_lookupsid / dns_reverse  → 用户与主机清单
        ↓
[生成字典] cewl / crunch / seclists
        ↓
[爆破] patator <module>  →  弱口令 / 有效用户 / 情报（版本号）
        ↓
[离线扩充] john / hashcat（用 unzip_pass 类模块的结果或 dump 出的哈希）
```

- **{patator, hydra}**：patator 负责「非标准流程」（带 token、带 cookie、要枚举），hydra 负责「标准协议大批量」。两者是互补而非替代。
- **{patator, ncrack/medusa}**：先 patator 精确定位「哪种响应代表成功」，再用 ncrack/medusa 大规模跑标准协议。
- **{patator, wordlists}**：字典统一走 [wordlists](wordlists.md) / seclists。
- **{patator, john/hashcat}**：`unzip_pass` / `keystore_pass` 是**本地**测试，与 john 的 `zip2john` 是不同路线，可以互相验证。

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| 结果里什么也不剩（全被过滤） | `-x ignore` 条件把成功也过滤掉了 | **先不加 `-x`，或加 `-l /tmp/resp/` 落盘**，观察真实响应再写条件 |
| 结果里失败行一大堆 | `-x` 条件写错/不匹配 | 用 `fgrep` 而不要用 `mesg=`（`mesg` 要求精确相等） |
| `Module not found` | 模块名拼错 | `patator -h` 看模块列表 |
| 参数报 `unexpected keyword` | 模块参数名写错或该模块无此参数 | `patator <模块> --help` |
| 碰到动态 CSRF token 就失效 | patator 不能自动提取回填页面 token | 写 patator Python 脚本，或改用专门的自动化框架 |
| `Fail` 计数很高 | 网络超时、连接被拒 | 调大 `--timeout`、加 `--max-retries` |
| 目标开始拒绝全部连接 | 速率过高触发 IPS | 加 `--rate-limit`，或减少并发 |
| 字典是 `.gz` | 未解压 | `gunzip`（见 [wordlists](wordlists.md)） |
| 中文乱码 | 编码 | `iconv` 转 UTF-8；`http_fuzz` 注意 `Content-Type` |
| 跑得极慢 | 在线爆破的固有速度 | 换小字典 + `COMBO` 生成器，别用笛卡尔积 |

## 9. 防御视角（蓝队）

| 风险 | 检测 | 缓解 |
| --- | --- | --- |
| 用户枚举（VRFY / RCPT / SID lookup / 时间差异） | 检测同一源对 `VRFY`、`RCPT TO`、SID 查询的高频调用；账号是否存在导致的**响应时间差** | 禁用 SMTP `VRFY`/`EXPN`、统一错误响应（不区分「用户不存在」与「口令错误」）、限制 LDAP/SMB 匿名查询 |
| 表单爆破 | 登录失败速率、`POST /login` 频率、失败后紧接成功 | 失败计数 + 账户锁定 + **CAPTCHA**（对 patator 这类工具最有效的一招，因为 patator 不会解验证码） |
| 带 cookie/会话的爆破 | 单会话 cookie 上大量失败请求 | 限制单会话的登录尝试次数、会话超时 |
| 低速慢猜 | 阈值规则完全无效 | 需要**长期基线**：某账号在 24 小时内被从离散源尝试多次 |
| 版本信息泄露 | patator 输出里出现服务器版本号 | 生产环境隐藏 banner（如 MySQL `--skip-version` 类配置、HTTP `Server` 头剥离） |

**蓝队要点**：patator 的 `-x ignore:fgrep=...` 说明**攻击者会主动研究你的错误响应格式**。所以：

> 最好的防护是**让成功与失败在响应上不可区分**（统一错误文本、统一响应时间、统一状态码），再加上**MFA** 和**验证码**。

## 10. 参考

- 官方仓库与文档：<https://github.com/lanjelot/patator>
- Kali 工具页：<https://www.kali.org/tools/patator/>
- 本机手册：`patator -h`、`patator --help-modules`、`patator <模块> --help`
- 相关：[hydra](hydra.md)、[medusa](medusa.md)、[ncrack](ncrack.md)、[cewl](cewl.md)、[wordlists](wordlists.md)

## ⚠️ 法律与伦理

未经授权对他人系统或网络服务进行口令猜测、用户枚举或请求模糊测试，可能构成《中华人民共和国刑法》第二百八十五条「非法侵入计算机信息系统罪」/「非法获取计算机信息系统数据罪」，以及第二百八十六条「破坏计算机信息系统罪」（模糊测试可能造成服务异常）；《网络安全法》第二十七条亦明令禁止。

**本教程仅适用于**：你自己拥有的系统、有书面授权的渗透测试、CTF 靶场、隔离教学环境。特别注意：**即使只是「枚举用户」而不试口令，也已构成未授权探测**。
