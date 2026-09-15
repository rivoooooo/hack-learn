# tiger（Linux 主机安全审计与 HIDS）

> **一句话**：一整套 shell + C 写的检查脚本，把 Unix/Linux 主机的账号、权限、配置文件、服务、文件完整性逐项体检，出一份带解释的安全报告——既能「一次性审计」，也能用 cron 定期跑做**主机入侵检测（HIDS）**。
> **分类**：漏洞分析 / 主机安全审计（HIDS）｜ **Kali 包**：`tiger`（命令 `tiger`、`tigercron`、`tigexp`）｜ **官方文档**：<https://www.kali.org/tools/tiger/> ｜ 上游：<http://savannah.nongnu.org/projects/tiger>

---

## 1. 它解决什么问题

系统「装好了、跑起来了」不等于「配置是安全的」。Tiger 的定位是**配置与状态的主机侧体检**：

- 有没有 UID 为 0 的异常账号、空口令账号、不该存在的家目录；
- 关键文件权限对不对（`/etc/passwd`、`/etc/shadow`、`/tmp`、`/` 等）；
- 有没有不该监听的端口、不该启动的服务；
- 系统二进制有没有被替换（**文件完整性即 HIDS 的核心**）；
- 有没有「不属于任何软件包」的可疑文件（Kali 包特别针对 Debian 做了这项检查）。

**对比同类（选型很重要）**：

| 工具 | 定位 | 差异 |
|------|------|------|
| **Tiger** | **主机配置审计 + 基础 HIDS** | 历史久（1994 年 TAMU），Debian/Kali 有专门检查（md5sums、非包文件、监听进程）；输出**带解释** |
| **Lynis** | Unix/Linux 安全审计 | **现代主流选择**：检查项更多、输出更结构化、有硬化建议评分；见 [`lynis.md`](lynis.md) |
| **AIDE / Tripwire / Integrit** | **文件完整性监控（FIM）** | 专注「文件是否被改」，不查配置；Tiger 会**调用**它们补齐这块 |
| **OSSEC / Wazuh** | 完整 HIDS（日志 + FIM + 主动响应） | 企业级；Tiger 轻量、无 agent、纯本地脚本 |
| **checksecurity / yasat / lsat** | 轻量检查脚本 | 检查项少；Tiger 官方描述里就写了「若只想要少量检查，用这些」 |
| **rootkit hunter（rkhunter）/ chkrootkit** | Rootkit 检测 | Tiger 可**调用** chkrootkit 做补充 |

**Kali/Debian 官方包描述里给的选型建议**（原文要点）：

> 「Tiger 的替代品包括 **lynis** 和 **ossec**。如果你只想做少量检查，试试 checksecurity、lsat 或 yasat。」

**结论**：**新项目优先 Lynis**；Tiger 的价值在于**历史积累的检查项 + 可读的「问题解释」+ 可定期跑的 HIDS 模式**，适合当「第二双眼睛」或需要「报告里带人话解释」时用。两者都跑一遍，取并集，成本很低。

---

## 2. 工作原理

Tiger 不是单个程序，而是**一个脚本集合 + 一份配置 + 一份「基线」**：

```
                        /etc/tiger/tigerrc            ← 主配置：开/关哪些检查
                               │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
  ┌───────────┐         ┌───────────┐          ┌───────────────┐
  │ tiger      │         │ tigercron │          │ tigexp        │
  │ 一次性全量  │         │ 定期增量   │          │ 解释生成器     │
  │ 审计        │         │ (HIDS)    │          │ (把编号→人话) │
  └─────┬─────┘         └─────┬─────┘          └───────────────┘
        │                      │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────────────────────────────┐
        │ 检查模块（每个是一个脚本，检查一类东西）       │
        │   check_accounts   账号/口令/UID 异常         │
        │   check_passwd     口令策略与空口令           │
        │   check_perms      文件权限（.rhosts、/etc…）  │
        │   check_services   服务与监听端口             │
        │   check_root       网络配置/内核参数          │
        │   check_devices    /dev 权限与异常设备         │
        │   check_netrc      凭据文件                    │
        │   check_logfiles   日志文件权限与轮转          │
        │   check_known      **文件完整性（签名比对）**   │
        │   …（Debian 版本另有 md5sums / 非包文件 / 监听进程检查）│
        └──────────────────┬───────────────────────────┘
                           ▼
        ┌──────────────────────────────────────────────┐
        │ 输出：security.report.<主机>.<日期>.<时间>     │  /var/log/tiger/
        │ 每条问题带一个编号 (e.g. [acc001w])           │
        │  + 可选 explain.report（解释只出现一次）       │
        └──────────────────────────────────────────────┘
```

**关键机制**：

- **编号化输出**：每条结论是一个短编号（如 `acc001w`、`perm002a`），**`tigexp <编号>` 可以把编号翻成详细解释与建议**。这是 Tiger 相对现代工具的最大特色——**报告可读**。
- **`-G` 生成签名基线**：`tiger -G` 对系统二进制做 MD5 + 权限快照。**HIDS 依赖这一步**：没有基线，`check_known` 无法判断「文件是否被改」。
- **`-l` 指定报告目录、`-w` 指定临时目录、`-b` 指定二进制目录**：Tiger 的 C 模块如果没预编译，**首次运行会尝试现场编译**（需要编译器），所以 `-b` 指向一个有写权限的目录很重要。
- **`tigercron` 是「增量模式」**：它按 `tigerrc` 里的策略决定本次该跑哪些检查（不是每次都全量），并**与上次报告比较**，只报变化——这正是 HIDS 的形态：**信噪比来自「变化」而不是「绝对状态」**。
- **`tigerrc` 决定检查的开/关**：每个检查项都有开关（如 `Tiger_Check_PASSWD=Y`）。**默认可能开了很多项，导致报告很长**——工程上应先关掉噪音项，把报告压到「可行动」的规模。
- **报告形态**：`-H` 输出带本地链接的 HTML；`-e` 把解释直接插在每条消息后面（报告会变很长）；`-E` 生成独立的解释报告（每种消息只解释一次）。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install tiger
command -v tiger tigercron tigexp
```

```console
root@kali:~# command -v tiger tigercron tigexp
/usr/sbin/tiger
/usr/sbin/tigercron
/usr/sbin/tigexp
```

```bash
sudo tiger -h
```

```console
root@kali:~# tiger -h
Tiger UN*X security checking system
   Developed by Texas A&M University, 1994
   Updated by the Advanced Research Corporation, 1999-2002
   Further updated by Javier Fernandez-Sanguino, 2001-2018
   Contributions by Francisco Manuel Garcia Claramonte, 2009-2010
   Covered by the GNU General Public License (GPL)

Tiger, version
Usage: ./tiger [-vthqGSH]  [-B dir] [-l dir|@host] [-w dir] [-b dir] [-e|-E] [-c config] [-A arch] [-O os] [-R release]

       -v     Show the Tiger version.

       -t     Run in test mode.

       -h     Show usage (this help).

       -q     Supress messages to be as quiet as possible, only
              security messages will be shown.

       -B name
              Specify  the directory where tiger is installed.  If
              not specified, '/usr/lib/tiger' is used.

       -l name
              Specify the name of the directory where Tiger  will
              write  the  security  report.  This defaults to
              '/var/log/tiger'. The filename  of the report will be of
              the form 'security.report.host-name.date.time.'
              If the directory  begins  with a @, the name will
              be interpreted as a tiger logging server.

       -w name
              Specify a directory to  use  for  creating  scratch
              files.  This defaults to '/var/lib/tiger/work'.

       -b name
              Specify  the  directory which contains (or will con-
              tain) the binaries generated from  the C  modules.
              If  the  systems  directories contain all the  bina-
              ries, they will be used directly  from  there.   If
              not,  then  if the  bindir  contains the binaries,
              these will be used.  If none are  found  in  either
              place,  then  an attempt  will be made to compile the
              C code and install the executables into the bindir.

       -c name
              Specify  an  alternate  name for the tigerrc control
              file.  The default is '/etc/tiger/tigerrc'.

       -e     This option will cause explanations to be  inserted
              into  the  security  report following each message.
              This can greatly increase the size of  the  report,
              as explanations may appear repeatedly.

       -E     This  option  indicates that a separate explanation
              report should be  created,  with  explanations  for
              each  type  of  message  only  appearing once.  The
              filename of the explanation report will be  of  the
              form 'explain.report.hostname.date.time.'

       -G     Generate  the signatures (MD5 hashes and file permissions)
              for system binary files.

       -H     This option  will  format  the  report  into  HTML  creat-
              ing local links to the problem descriptions.

       -S     This option indicates that a surface level check of
              the  configuration  files  of  any diskless clients
              served by this machine should  be  checked  at the
              same  time.   The  checks will not be as in depth as
              they would be if run on the client itself.

Overrides for values detected  by the configuration system:
       -A arch
              Specify  an  alternate  architecture for tiger

       -O os
              Specify  an  alternate  operating system for tiger

       -R release
              Specify  an  alternate  operating system release

Report bugs at http://savannah.nongnu.org/projects/tiger
```

**Kali 打包后关键路径**：

| 路径 | 内容 |
|------|------|
| `/etc/tiger/tigerrc` | **主配置**（每个检查的开关） |
| `/etc/tiger/tiger.ignore` | 忽略清单（把已知安全的项排除） |
| `/etc/tiger/hosts/` | 各主机的基线/配置（HIDS 用） |
| `/usr/lib/tiger/` | 脚本与签名数据 |
| `/var/log/tiger/` | **默认报告目录**（`security.report.*`、`explain.report.*`） |
| `/var/lib/tiger/work/` | 临时工作目录 |

**最小可用（先跑一次全量审计）**：

```bash
# ① 一次性全量审计，报告进 /var/log/tiger/，同时生成独立解释报告
sudo tiger -E

# ② 看报告
sudo ls -l /var/log/tiger/
sudo head -60 /var/log/tiger/security.report.*
```

**建立基线（**这是 HIDS 的前置步骤，务必在系统「干净」时做**）**：

```bash
sudo tiger -G
```

**定期跑（HIDS 模式）**——Kali 安装 `tiger` 时会带 cron：

```bash
ls -l /etc/cron.d/tiger /etc/cron.daily/tiger* 2>/dev/null
cat /etc/cron.d/tiger 2>/dev/null
```

```console
# 典型内容：每天/每周跑 tigercron
```

> **重要**：默认 cron 可能会**自动发邮件**给 root。在没有本地 MTA 的 Kali 上，邮件会静默失败——需要自己配 MTA 或改成「写文件 + 外部告警」。

---

## 4. 核心参数详解

> 全部取自上面的 `tiger -h` 原文。`tigercron`、`tigexp` 见后。

### 4.1 运行控制

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-h` | 显示用法 | —— |
| `-v` | 显示版本 | **注意**：Kali 打包的版本号字符串可能为空（`Tiger, version ` 后面空白），这是上游/Bug，不代表安装失败 |
| `-t` | **测试模式** | 先用它确认「会不会真的跑起来、跑哪些检查」，再正式跑 |
| `-q` | 尽量安静，**只输出安全相关消息** | **首次跑必加**（否则会看到大量信息性输出） |
| `-G` | **生成系统二进制签名（MD5 + 权限）** | **建立 HIDS 基线的唯一开关**；只在系统可信状态执行 |
| `-S` | 顺带做「无盘客户端的表层配置检查」 | 仅在有多客户端场景用 |

### 4.2 路径与配置

| 参数 | 作用 | 默认值 | 使用建议 |
|------|------|--------|----------|
| `-B <dir>` | Tiger 安装目录 | `/usr/lib/tiger` | 自定义安装时用 |
| `-l <dir\|@host>` | **报告输出目录** | `/var/log/tiger` | 目录名以 `@` 开头则视为「tiger 日志服务器」，报告发过去 |
| `-w <dir>` | 临时文件目录 | `/var/lib/tiger/work` | 空间不足/权限问题时改 |
| `-b <dir>` | C 模块二进制目录 | 系统目录 | **首次运行需编译时指向可写目录** |
| `-c <file>` | 备用配置文件 | `/etc/tiger/tigerrc` | 做「多套策略」：如 `-c /etc/tiger/tigerrc-cis` |

### 4.3 报告形态

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-e` | 把解释**直接插在每条消息后** | 报告会**非常长**（同一解释重复出现）；适合一次性细读 |
| `-E` | 生成**独立的解释报告**（每种解释只出现一次） | **推荐**：报告保持精简，解释单独一份 |
| `-H` | 生成 **HTML** 报告，带本地链接到问题说明 | **交给领导/客户看**用这个；也便于归档 |

### 4.4 环境覆盖（一般不用）

| 参数 | 作用 |
|------|------|
| `-A <arch>` | 覆盖自动探测的架构 |
| `-O <os>` | 覆盖操作系统 |
| `-R <release>` | 覆盖系统发行版本 |

> 这三个只在「把某主机的报告拿去另一台机器分析」或探测出错时用。

### 4.5 `tigercron`（HIDS 定期模式）

`tigercron -h` **输出与 `tiger -h` 完全相同**（同一份帮助），但**语义不同**：它读 `tigerrc` 里的策略，决定本次跑哪些检查，并**与上次结果比较只报变化**。

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-q` | 只输出安全消息 | cron 里建议加 |
| `-l <dir>` | 报告目录 | 与 `tiger` 共用 |
| `-c <file>` | 策略文件 | 想给 cron 用不同策略时 |
| `-E` / `-H` | 独立解释报告 / HTML | 定期归档 |

### 4.6 `tigexp`（解释生成器）

```bash
tigexp <消息编号>
```

例：报告里出现 `acc001w`，运行 `tigexp acc001w` 会打印这条消息的**完整解释与修复建议**。

| 用法 | 作用 |
|------|------|
| `tigexp acc001w` | 单个编号的详细解释 |
| `tigexp -w` | 列出所有**警告级**消息编号 |
| `tigexp -W` | 列出警告级 + 说明 |
| `tigexp -f` | 完整列表 |

> 参数以本机 `tigexp -h` / `man tigexp` 为准（Kali 页面里 `tigexp --help` 输出为空，属已知的小瑕疵）。**核心用法就是「给编号出解释」**。

### 4.7 `tigerrc` 里最该关心的开关

`tigerrc` 是**控制报告长度的关键**。常见开关（以本机 `/etc/tiger/tigerrc` 为准）：

| 配置项（示例） | 作用 |
|----------------|------|
| `Tiger_Check_PASSWD` | 口令与账号策略检查 |
| `Tiger_Check_ACCOUNTS` | 账号一致性（UID/GID/家目录/空口令） |
| `Tiger_Check_PERMS` | 关键文件权限 |
| `Tiger_Check_SERVICES` | 服务与监听端口 |
| `Tiger_Check_DEVICES` | `/dev` 与设备文件 |
| `Tiger_Check_NETRC` | `.netrc`/凭据文件 |
| `Tiger_Check_LOGFILES` | 日志文件权限/轮转 |
| `Tiger_Check_KNOWN` | **文件完整性（需先 `-G` 建基线）** |
| `Tiger_Check_ROOT` | 内核/网络参数 |
| `Tiger_Check_CRON` | cron 任务审计 |
| `Tiger_Check_EMBEDDED` | 嵌入脚本/异常文件 |
| `Tiger_Show_SUID` | 是否列出所有 SUID 文件 |
| `Tiger_Mail_RCPT` | 报告收件人（邮件发送） |
| `Tiger_Get_Shells` | 是否抓取 shell 列表做对比 |

**用法建议**：

```bash
# 只关心「权限 + 账号」类检查：编辑 tigerrc 把其他项关掉，
# 或单独跑某个检查脚本
sudo /usr/lib/tiger/check_accounts
sudo /usr/lib/tiger/check_perms
```

**逐个检查脚本单独跑**是排错和聚焦的关键——不必每次都全量。

---

## 5. 实战演练

> **环境声明**：以下全部在**你自己拥有或获得授权的主机/虚拟机上**执行。
> - **首选一次性虚拟机**（`snap` 快照，跑完直接回滚）；
> - Tiger 的检查脚本会**读取**系统大量文件并**写入** `/var/log/tiger`、`/var/lib/tiger/work`，属于**只读为主 + 少量写日志**，但仍建议在快照 VM 上做；
> - `-G` 会**生成基线**（写入签名数据），**不要在生产主机随意重建基线**（会掩盖已有篡改）；
> - `-l @host`（发报告到远程）会把主机安全信息**外发**，需评估合规性。

### 场景 1：一台新装主机的第一次审计

```bash
# ① 测试模式：先看它会跑什么，不产生报告
sudo tiger -t -q 2>&1 | head -30
```

```console
root@kali:~# sudo tiger -t -q 2>&1 | head -30
Tiger UN*X security checking system
...
--CONFIG--
Tiger_Check_PASSWD   = Y
Tiger_Check_ACCOUNTS = Y
Tiger_Check_PERMS    = Y
...
```

**解读**：`-t` 会打印**实际生效的配置**。这一步能立刻回答两个问题：「会跑哪些检查」「配置从哪读的」。**这一步不做就正式跑，很容易得到一份 3000 行看不懂的报告。**

```bash
# ② 正式跑：-q 只输出安全问题，-E 生成独立解释报告，-H 同时出 HTML
sudo tiger -q -E -H
sudo ls -l /var/log/tiger/
```

```console
root@kali:~# sudo ls -l /var/log/tiger/
-rw-r----- 1 root root  ...  security.report.kali.2026-09-15-10-20
-rw-r----- 1 root root  ...  explain.report.kali.2026-09-15-10-20
-rw-r----- 1 root root  ...  security.report.kali.2026-09-15-10-20.html
```

```bash
# ③ 看报告（先只看「有问题的」那部分）
sudo grep -n -E '^--[A-Z]+|FAIL|WARN|INFO' /var/log/tiger/security.report.kali.* | head -40
```

```console
--ACCOUNTS--
# Performing check of passwd, shadow and group files...
--WARN-- [acc001w] Login ID nobody is not present in passwd
--WARN-- [acc006w] Login ID games has no home directory defined
--INFO-- [acc009i] Login ID daemon has no login shell.
--PERMS--
--WARN-- [perm011w] The file /etc/passwd is not owned by root
...
```

**解读（报告的三层结构）**：

| 层级 | 形式 | 含义 |
|------|------|------|
| **章节** | `--ACCOUNTS--`、`--PERMS--`、`--SERVICES--` | 检查类别 |
| **条目** | `--WARN-- [acc001w] ...` | 一条发现，**带编号** |
| **编号** | `acc001w` | **`w` = warning，`i` = info，`a` = alert/注意**；`acc` 是检查域前缀 |

**先看 `w` 和 `a`，`i` 大多可以忽略**——这是让报告变得可处理的第一条纪律。

```bash
# ④ 把编号翻成人话 + 修复建议
sudo tigexp acc001w
```

```console
root@kali:~# sudo tigexp acc001w
Login ID nnnnn is not present in passwd.
...
This means that ... (解释成因与风险)
To fix: ... (修复建议)
```

**解读**：**这才是 Tiger 的核心价值**——报告不是一个「分数」，而是「问题 + 为什么是问题 + 怎么修」。把报告里的所有 `w`/`a` 编号批量喂给 `tigexp`，就能生成一份**可直接落地的整改清单**：

```bash
# ⑤ 批量提取编号并逐个解释（生成整改清单）
sudo grep -oE '\[[a-z]+[0-9]+[wai]\]' /var/log/tiger/security.report.kali.* \
  | tr -d '[]' | sort -u > /tmp/tiger_ids.txt
wc -l /tmp/tiger_ids.txt
while read -r id; do
  echo "===== $id ====="
  sudo tigexp "$id"
done < /tmp/tiger_ids.txt > /tmp/tiger_actions.txt
head -40 /tmp/tiger_actions.txt
```

**解读**：这一步把「一份 3000 行报告」变成「一份 20 条的整改清单」。**这才是审计该交付的东西。**

### 场景 2：建立基线 + 用 HIDS 模式抓「文件被改」

**这是一个「两阶段」练习**，必须在**可信状态**下建基线。

```bash
# ── 阶段 1：在干净的系统上建立基线 ──
sudo tiger -G
sudo ls -l /usr/lib/tiger/systems/ 2>/dev/null || sudo find / -name '*.sig' -path '*tiger*' 2>/dev/null | head
```

```console
root@kali:~# sudo tiger -G
Tiger UN*X security checking system
...
--INFO-- Generating signatures for system binaries...
--INFO-- Signatures written.
```

```bash
# ── 阶段 2：故意改一个系统二进制（模拟入侵/被篡改）──
# ⚠️ 只在一次性虚拟机里做！这里用「加一个字节」的方式，不改功能
sudo cp /usr/bin/false /root/false.bak
echo '# tampered' | sudo tee -a /usr/bin/false >/dev/null
sudo ls -l /usr/bin/false
```

```bash
# ── 阶段 3：跑完整性检查，看能否抓到 ──
sudo /usr/lib/tiger/check_known 2>&1 | head -20
# 或者跑全量（check_known 会包含在 tigerrc 开启时）
sudo tiger -q -E
sudo grep -n -i 'known\|signature\|integrity\|md5' /var/log/tiger/security.report.kali.* | head -20
```

```console
--WARN-- [sig002w] Checksum for the file /usr/bin/false changed (was: <基线哈希>, now: <当前哈希>)
```

**解读（这是 HIDS 的本质）**：

| 阶段 | 关键点 |
|------|--------|
| 建基线 | **必须在「确信系统未被入侵」时做**。基线本身就 = 「可信快照」 |
| 篡改 | 任何对受监控文件的改动都会导致哈希/权限不匹配 |
| 复检 | `check_known` 报「哈希变化」→ **要么是正常升级，要么是入侵** |

**关键纪律**：
1. **系统打补丁/升级后必须重建基线并记录**（否则天天告警）；
2. **基线文件本身要保护**（存到只读介质/另一台机器）；
3. **告警不是结论，是线索**——先确认是不是自己改的（查包管理器日志 `dpkg.log`、`apt` history）。

```bash
# 确认「这个改动是不是包管理器做的」
grep -n '/usr/bin/false' /var/log/dpkg.log* 2>/dev/null | tail
# 恢复被测文件
sudo cp /root/false.bak /usr/bin/false
```

### 场景 3：用 tigercron 做定期 HIDS + 报告对比（自动化）

**3a. 先看 Kali 自带的 cron 是怎么配的**

```bash
cat /etc/cron.d/tiger 2>/dev/null
ls -l /etc/cron.daily/ | grep -i tiger
cat /etc/tiger/tigerrc | grep -i -E 'mail|cron|rcpt' | head
```

**3b. 自己写一份「只报变化」的定期任务**（比默认更可控）

```bash
# /etc/cron.d/my-tiger-hids
sudo tee /etc/cron.d/my-tiger-hids >/dev/null <<'EOF'
# 每天 03:30 跑一次 HIDS 模式，报告写入 /var/log/tiger
30 3 * * * root /usr/sbin/tigercron -q -E -l /var/log/tiger >/dev/null 2>&1
EOF
sudo chmod 644 /etc/cron.d/my-tiger-hids
sudo cat /etc/cron.d/my-tiger-hids
```

**3c. 报告对比：把「今天」和「昨天」diff 出来（最实用的技巧）**

```bash
# 手动模拟：跑两次，比较报告差异
sudo tiger -q -E -l /tmp/tiger-run1 >/dev/null 2>&1
# （做点变化，比如新建一个 SUID 文件）
sudo cp /usr/bin/find /tmp/suid_demo && sudo chmod u+s /tmp/suid_demo
sudo tiger -q -E -l /tmp/tiger-run2 >/dev/null 2>&1

# 去掉日期/主机名等易变行后 diff
diff <(sudo sed 's/[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}[^ ]*//' /tmp/tiger-run1/security.report.*) \
     <(sudo sed 's/[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}[^ ]*//' /tmp/tiger-run2/security.report.*) \
  | head -30
```

```console
> --WARN-- [perm006w] The file /tmp/suid_demo is a SUID file and should not be there
```

**解读**：**HIDS 的正确读法是「diff」而不是「通读」**：

| 关注 | 含义 |
|------|------|
| 新增的 `--WARN--` 行 | **变化 = 最可能的异常**（今天多了一个 SUID 文件） |
| 消失的行 | 通常代表「被修好了」，但也可能是「日志被删了」 |
| 稳定不变的行 | 已知基线噪音 → 应写进 `tiger.ignore` 压掉 |

```bash
# 清理演示文件
sudo rm -f /tmp/suid_demo
```

**3d. 把已知安全项写进忽略清单**（降噪）

```bash
# /etc/tiger/tiger.ignore 的格式与用法以本机文件为准
sudo head -30 /etc/tiger/tiger.ignore 2>/dev/null
```

**解读**：把「已经确认安全、但每次都会告警」的项加进忽略清单，是让 HIDS **可持续运行**的前提。**没有降噪的 HIDS 会在两周内被所有人无视。**

---

## 6. 输出解读

### 6.1 消息行的格式

```
--<级别>-- [<编号>] <描述>
```

| 位置 | 取值 | 含义 |
|------|------|------|
| 级别 | `--WARN--` | 需要注意，可能存在风险 |
| | `--INFO--` | 信息性（多数可忽略，除非在做合规取证） |
| | `--FAIL--` / `--ALERT--` | 严重（视版本），优先处理 |
| 编号 | 如 `acc001w` | **前缀=检查域，数字=条目，尾字母=级别** → 喂给 `tigexp` |
| 描述 | 一句话 | 涉及的文件/账号/服务 |

**编号前缀速查**（以本机 `tigexp` 输出为准）：

| 前缀 | 检查域 |
|------|--------|
| `acc` | accounts（账号） |
| `perm` | permissions（权限） |
| `pass` / `passwd` | 口令策略 |
| `sig` / `known` | 文件完整性签名 |
| `svc` / `serv` | 服务 |
| `dev` | 设备 |
| `net` / `netrc` | 网络/凭据文件 |
| `log` | 日志文件 |
| `root` | 内核/系统参数 |
| `cron` | 计划任务 |

### 6.2 报告结构

```
security.report.<host>.<date>-<time>
  ├── 头部：Tiger 版本、主机、时间、配置摘要
  ├── --ACCOUNTS--     账号检查
  ├── --PERMS--        权限检查
  ├── --SERVICES--     服务检查
  ├── --FILES--        文件/完整性
  ├── ...
  └── 结尾：统计（各检查执行情况）
explain.report.<host>.<date>-<time>     ← 加了 -E 才有：编号→解释
security.report.<host>.<date>-<time>.html ← 加了 -H 才有
```

### 6.3 怎么判断与下一步

| 观察 | 判断 | 下一步 |
|------|------|--------|
| `--WARN-- [acc...]` 空口令/异常 UID 0 | **高危** | 立即锁账号、查登录日志 |
| `--WARN-- [perm...]` 关键文件权限 | 可被本地提权利用 | 按 `tigexp` 建议改权限 |
| `--WARN-- [sig...]` 哈希变化 | **要么是升级，要么是入侵** | 查 `dpkg.log`/`apt` 历史 → 不是升级就要启动应急 |
| 大量 `--INFO--` | 噪音 | 关闭对应检查项或写 `tiger.ignore` |
| 报告几乎为空 | 系统干净 **或** 检查没跑 | 先 `-t` 确认检查项是否开启 |
| 同一 WARN 每次都有 | 未整改或已接受的风险 | 整改 → 或明确「接受风险」并记录到忽略清单 |

---

## 7. 与其他工具配合

```
                    ┌─────────────────────────────┐
   主机安全基线 ────► │ tiger（配置审计 + HIDS）      │
                    │  -G 建基线 / tigercron 定期   │
                    └──────────┬──────────────────┘
                               │
   ┌───────────────────────────┼───────────────────────────────┐
   ▼                           ▼                               ▼
 Lynis（现代审计，取并集）  AIDE/Tripwire（强化 FIM）    rkhunter/chkrootkit
   │                           │                       （rootkit 检测）
   └──────────────┬────────────┘
                  ▼
              整合成一份整改清单 → 变更管理 → 复测
                  ▲
                  │
        Nmap（外部视角）/ Snort（流量视角）
```

- **现代审计主力**：[`lynis.md`](lynis.md) —— **Tiger + Lynis 一起跑，取并集**是最低成本提高覆盖率的方法
- **外部攻击面**：[`../01-信息搜集/nmap.md`](../01-信息搜集/nmap.md) —— 主机内部审计 + 外部端口扫描，两侧对照
- **网络侧检测**：[`snort.md`](snort.md) —— 主机 HIDS（Tiger）+ 网络 NIDS（Snort）
- **漏洞面**：[`searchsploit.md`](searchsploit.md) —— 审计发现的服务版本 → 查对应 EXP
- **文件完整性强化**：Tiger 可调用 `AIDE`/`Tripwire`/`Integrit`（Tiger 官方描述明确说了这点）
- **Rootkit 检测**：Tiger 可调用 `chkrootkit`
- **证据固定（取证场景）**：[`../09-数字取证/dcfldd.md`](../09-数字取证/dcfldd.md)

**推荐组合流程**：

```
① 系统装好、确认干净 → tiger -G 建基线
② 配置 tigerrc / tiger.ignore 降噪
③ cron 跑 tigercron（每天）+ lynis audit system（每周）
④ 报告 diff → 只处理「变化」→ 整改 → 记录
⑤ 每季度全量审计 + 重建基线（升级后必须重建）
```

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 报告的版本号是空的 | Kali 打包的上游小瑕疵（`Tiger, version ` 后无内容） | **不是安装失败**；用 `dpkg -l tiger` 看包版本 |
| 首次运行很慢/报编译错误 | C 模块**未预编译，现场编译**，缺 gcc/make | `apt install gcc make`；或用 `-b` 指向可写目录 |
| 报告几千行，没法读 | 未加 `-q`；未做 `tigerrc` 降噪 | **加 `-q`**；关掉不关心的检查项；用 `tiger.ignore` |
| 报告里满屏 `--INFO--` | 信息级消息未被过滤 | 只处理 `w`/`a`；或用 `grep -v INFO` |
| `check_known` 报大量哈希变化 | 系统刚升级过；或**基线太旧**；或被入侵 | 查 `dpkg.log`；确认是升级就**重建基线**；否则启动应急 |
| `-G` 之后没抓到篡改 | 基线是在「已被污染」的状态下建的 | **必须在可信状态重建**；并把基线文件存到只读介质 |
| cron 跑了但没人知道 | 默认靠**邮件**通知，Kali 常无 MTA | 配 MTA，或改成「写文件 + 外部告警」（参考场景 3 的自定义 cron） |
| `Permission denied` | 普通用户跑 Tiger | `sudo` 运行（要读 shadow 等） |
| 临时目录写入失败 | `/var/lib/tiger/work` 权限/空间问题 | `-w /tmp/tiger-work`（确保存在且可写） |
| `-l @host` 发不出去 | 远程 tiger 日志服务器未配置 / 网络不通 | 先本地跑通；远程需按官方文档配接收端 |
| 改了 `tigerrc` 没生效 | 用了默认配置路径，实际指定了 `-c` | 检查是否传了 `-c`；`tiger -t` 会打印生效的配置 |
| Debian 特有检查（非包文件、监听进程）报很多 | 系统里确实有非包管理的文件（自编译程序、手册页） | 逐个确认来源；把已知合法的写入 `tiger.ignore` |
| 报告时间戳很乱 | 用了本地时间但跨时区 | 统一 UTC 或在报告外层记录时区 |
| 与其他审计工具结论冲突 | 检查口径不同 | **取并集**而非二选一；把两边的结论都进整改清单 |

---

## 9. 防御视角（蓝队）

Tiger 本身就是主机侧防御工具，蓝队用法分**「一次性加固」**和**「持续监测」**两条线：

| 场景 | 做法 | 价值 |
|------|------|------|
| 上线前基线审计 | 新装机跑 `tiger -q -E` + `lynis audit system` | 交付前把明显问题清掉 |
| 合规取证 | `-H` 出 HTML 报告归档 | 等保/ISO 27001 的证据材料 |
| 文件完整性监控 | `-G` 建基线 + `tigercron` 定期跑 | **检测系统二进制被替换**（rootkit/后门的典型手法） |
| 变更检测 | 报告 diff（只处理变化） | **HIDS 的信噪比来自变化** |
| 提权面收敛 | 关注 `perm*`、SUID/SGID、异常 owner | 减少本地提权路径 |
| 账号治理 | 关注 `acc*`、UID 0、空口令、无家目录 | 清除遗留/影子账号 |
| 事件响应 | 对受害主机跑全量 + 完整性检查 | 判断「哪些文件被动过」 |

**蓝队的六条硬建议**：

1. **基线只在可信状态建立**，并**存到另一台机器/只读介质**（否则攻击者改基线就白干）；
2. **升级/打补丁后必须重建基线**，同时记录变更窗口（避免告警风暴）；
3. **报告必须降噪到「可行动」的规模**——用 `tigerrc` + `tiger.ignore`，否则两周后没人看；
4. **HIDS 看的是 diff**：把「昨天 vs 今天」的差异作为主要告警源；
5. **邮件不是告警通道**：Kali/容器环境普遍没有 MTA，要接外部告警（日志平台、Syslog、IM）；
6. **Tiger + Lynis 双工具**：口径互补，成本极低，覆盖率明显更高。

**Tiger 的固有局限（要清楚）**：

- **不是实时**：cron 粒度（通常天级），无法替代实时 HIDS（Wazuh/OSSEC/审计子系统 auditd）；
- **基于文件与配置**：**检测不到纯内存攻击**（无文件恶意软件、内存马）——那块要靠内存取证与 EDR；
- **依赖基线可信**：基线被污染则后续全失效；
- **只覆盖本机**：多机需要集中收集报告（用 `-l @host` 或外部采集）。

**与审计子系统配合**：把 Tiger 的**周期体检**与 `auditd` 的**实时审计**结合——Tiger 管「配置是否偏离基线」，auditd 管「此刻谁在做什么」。

---

## 10. 参考

- Kali 工具页（含 `tiger -h`、`tigercron -h` 原文）：<https://www.kali.org/tools/tiger/>
- Kali 包跟踪：<https://pkg.kali.org/pkg/tiger>
- 上游项目（Savannah）：<http://savannah.nongnu.org/projects/tiger>
- 本地命令与路径：`tiger -h`、`tigercron -h`、`tigexp <编号>`、`man tiger`、`man tigexp`、`/etc/tiger/tigerrc`、`/etc/tiger/tiger.ignore`
- 配套教程：[`lynis.md`](lynis.md)（现代主机审计，**最推荐一起用**）、[`snort.md`](snort.md)（网络侧 NIDS）、[`../01-信息搜集/nmap.md`](../01-信息搜集/nmap.md)（外部视角）

## ⚠️ 法律与伦理

Tiger 是**本地审计**工具，但只要涉及「审计谁的系统」，法律边界立刻出现：

- **必须获得授权**：Tiger 会读取 `/etc/shadow` 等敏感文件、枚举全部账号与监听服务，**在非自有主机上运行属于未授权访问**，可能触犯《刑法》第 285 条（非法获取计算机信息系统数据）；
- **报告含敏感信息**：`security.report.*` 包含账号列表、权限缺陷、服务清单——**这是攻击者最想要的地图**。必须：
  - 严格文件权限（默认已是 `640 root`），存放于受控位置；
  - **不得**把报告发到外部邮箱/公开仓库/网盘；
  - 用 `-l @host` 外发时，评估通道加密与接收方授权。
- **法务与取证场景**：作为证据使用时，需保证**工具版本可复核、操作过程可追溯、报告未被篡改**（配合 [`../09-数字取证/dcfldd.md`](../09-数字取证/dcfldd.md) 的证据固定流程）；
- **基线数据**：`-G` 生成的签名数据同样敏感（可反推系统软件版本与补丁状况），需与报告同等保护；
- **员工隐私**：审计可能触及个人文件（家目录、历史命令），应在**已明示的合规框架**内进行，遵循最小必要原则。

**必须遵守**：

1. **只审计你拥有或获得书面授权的主机**；
2. **报告与基线数据按敏感数据保护**，不公开、不外发、不留副本；
3. **`-G` 重建基线**是变更操作，需纳入变更管理（旧基线要归档，不能直接丢弃）；
4. **审计发现的高危项**（如空口令、哈希变化的系统文件）应立即进入**正式应急流程**，不擅自处置；
5. **在一次性虚拟机上练习**本教程的所有场景，避免影响真实系统。
