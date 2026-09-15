# lynis（Unix/Linux 系统安全审计）

> **一句话**：把一台 Linux/Unix 主机的配置从头到尾检查一遍，给出"可改进项"清单——它是**主机加固审计**，不是漏洞扫描器。
> **分类**：漏洞分析 ｜ **Kali 包**：`lynis` ｜ **官方文档**：<https://cisofy.com/lynis/>

## 1. 它解决什么问题

前面几类工具都在问"目标有没有能被利用的漏洞"。lynis 问的是另一个问题：

**这台机器的配置安全吗？** 具体包括：

- 有没有设置 GRUB 口令、是否启用了 SELinux/AppArmor
- SSH 配置是否合理（是否允许 root 登录、是否用密钥、加密算法是否过时）
- 有没有不必要的服务在监听
- 密码策略、账户锁定、sudo 配置
- 日志与审计是否开启（syslog、auditd）
- 文件权限、SUID 文件、home 目录权限
- 有没有安装安全更新、是否有 EOL（生命周期结束）的软件包
- 内核参数（`sysctl`）的加固状态

| 工具 | 定位 | 输出 |
|------|------|------|
| **lynis** | 主机配置加固审计（**防守视角为主**） | 警告/建议 + 加固指数 |
| [nuclei](nuclei.md) / [nikto](nikto.md) | 网络服务漏洞扫描（**攻击视角**） | 漏洞命中 |
| OpenSCAP / `oscap` | 按标准基线（CIS/STIG）精确打分 | 合规评分报告 |
| `auditd` / `aide` | 运行时审计与完整性监控 | 事件流 |

**关键定位**：lynis 是少数**从防守方角度设计**的 Kali 工具。它不需要 root 也能跑（但 root 能看到更多），最常用的场景是：

1. **渗透测试拿到 shell 后**：找提权线索（SUID、可写配置、过期内核）。
2. **蓝队做基线核查**：定期审计自己的服务器，跟踪加固进度。

## 2. 工作原理

```text
   lynis audit system
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ① 引导阶段（bootstrap）                                    │
   │    读取 default.prf + 自定义 profile                       │
   │    检查运行环境：是否有 root、OS 类型、是否容器             │
   │    生成/读取 host ID（用于多次审计结果对比）                │
   └────┬──────────────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ② 按"分组"顺序执行数百项测试                                │
   │    分组大致顺序：                                          │
   │      boot / kernel / authentication / shell / services     │
   │      / networking / storage / logging / hardening ...      │
   │    每个测试有唯一 ID，如 SSH-7408、KRNL-6000、FILE-7524     │
   │    测试引用"控制项"（control），如 CONTROL-013              │
   └────┬──────────────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ③ 结果分三类写日志/报告                                     │
   │    [ OK ]     已符合要求                                    │
   │    [ WARNING ] 明确的风险点（应修复）                        │
   │    [ SUGGESTION ] 改进建议（非必须）                        │
   │    hardening index：加固指数（只有 root 完整扫描才给出）     │
   └────┬──────────────────────────────────────────────────────┘
        │
   输出：
     /var/log/lynis.log       日志（完整细节）
     /var/log/lynis-report.dat 结构化报告（可 diff 对比）
```

关键机制：

- **测试 ID 是稳定的**：比如 `SSH-7408` 永远是"是否允许 root 用 SSH 登录"这一项。所以可以用 `--tests SSH-7408` 只跑它，也可以在多次审计之间做 diff。
- **加固指数（Hardening Index）**：0~100 的分数，只有拿到足够权限时才会完整计算。它不是"安全分数"，而是**改进空间的量化指标**——值得用来跟踪趋势。
- **`lynis-report.dat` 是可 diff 的**：这是 lynis 最实用的副产品。把每次审计的报告存下来，就能精确看到"这次比上次多修了哪些"。
- **不是漏洞扫描**：lynis 不会发网络包。它读本地配置。所以它对远程目标无效——**必须在目标主机上运行**（或挂载目标文件系统用 `--rootdir`）。

## 3. 安装与快速上手

```bash
sudo apt install lynis
sudo lynis --version
sudo lynis --help
```

最小可用命令：

```bash
# 1) 标准系统审计（首次使用就跑这个）
sudo lynis audit system

# 2) 快速模式（不问问题、用完即走）
sudo lynis audit system --quick

# 3) 只输出警告，适合放进 cron
sudo lynis audit system --warnings-only
```

## 4. 核心参数详解

### 扫描模式（命令）

| 命令 | 作用 | 使用建议 |
|------|------|----------|
| `audit system` | 系统审计（**最常用**） | 本地主机加固检查 |
| `audit system remote <host>` | 生成远程扫描所需的命令 | 生成脚本后在目标上执行 |
| `upload-only` | 上传已有的报告数据文件 | 配合 Lynis Enterprise |
| `show <param>` | 显示信息（配置、路径、分类、分组等） | `lynis show groups`、`lynis show categories`、`lynis show help` |
| `generate <param>` | 生成特定内容（如 host ID） | — |
| `configure <param>` | 修改/新增配置文件设置 | — |
| `update <param>` | 更新相关操作 | 如更新定义 |

### 通用选项

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `--auditor <name>` | 记录审计者姓名（含空格要加双引号） | 正式审计留痕 |
| `--cronjob` | cron 安全模式：无颜色、无提问、无停顿 | **放进 cron 时用这个** |
| `--quick`（`-Q`） | 快速扫描，不等待用户输入 | 默认行为，可省略 |
| `--quiet`（`-q`） | 静默，不向屏幕输出，隐含快速模式 | 纯脚本化 |
| `--warnings-only` | 静默，但显示警告 | **最适合日常巡检** |
| `--wait` | 每节结束后停顿等待用户按键 | 教学/逐步演示；与 `--quick` 相反 |
| `--pentest` | 非特权扫描（渗透测试常用），部分需要 root 的测试会跳过 | **拿到 shell 后的低权限审计** |
| `--forensics` | 对运行中或已挂载的系统做审计（配 `--rootdir`） | 应急响应/离线分析 |
| `--rootdir <dir>` | 指定根目录（审计已挂载的另一个系统） | 配合 `--forensics`；取证场景 |
| `--verbose` | 显示更多细节（包括找不到的组件） | 排查"为什么某项没跑" |
| `--debug` | 调试信息 | 排障 |
| `--developer` | 开发测试用的详细信息 | 写自定义测试时 |
| `--no-colors` | 关闭颜色输出 | 重定向到文件 |
| `--reverse-colors` | 适配浅色背景终端 | — |
| `--no-log` | 把日志重定向到 `/dev/null`（防止敏感信息落盘） | **共享主机/敏感环境** |
| `--logfile <path>` | 自定义日志文件（默认 `/var/log/lynis.log`） | — |
| `--report-file <file>` | 自定义报告文件（默认 `/var/log/lynis-report.dat`） | 多主机集中收集 |
| `--profile <file>` | 使用自定义 profile | **生产环境必用**（见第 5 节场景 4） |
| `--plugin-dir <dir>` | 自定义插件目录 | — |
| `--no-plugins` | 不运行任何已启用的插件 | 排查插件干扰 |
| `--use-cwd` | 在当前工作目录运行（用同目录的 profile/插件） | 便携运行 |
| `--tests <ID...>` | **只跑指定的测试**（多个测试要用引号包起来） | 精确复核某一项 |
| `--tests-from-category <cat>` | 只跑指定分类的测试 | 用 `lynis show categories` 查可用值 |
| `--tests-from-group <group>` | 只跑指定分组的测试 | 用 `lynis show groups` 查可用值 |
| `--check-update` | 检查更新 | — |
| `--dump-options` | 打印所有可用选项 | 排障 |
| `--upload` | 上传数据到 Lynis Enterprise | 需 profile 中 `upload=yes` |

### 退出码（脚本化时很有用）

| 退出码 | 含义 |
|--------|------|
| `0` | 正常结束 |
| `1` | 致命错误 |
| `64` | 未知参数或不完整 |
| `65` | 遇到不正确数据 |
| `66` | 无法打开文件/目录 |
| `78` | 发现 1 个或多个警告/配置错误（需 profile 中 `error-on-warnings=yes`） |

## 5. 实战演练

**环境**：本地实验环境。lynis 检查的是**运行它的那台机器**，所以：

- 靶机 A：一台 Ubuntu/Debian 实验虚拟机（允许随便改配置、随便审计）。
- 靶机 B（效果更明显）：故意配置得"不安全"的虚拟机——开 root SSH 登录、装几个过期服务、设个弱口令策略。
- 攻击机 Kali：`192.168.56.10`——**也可以直接审计 Kali 本身**，这是最容易上手的起点。

> **注意**：lynis 是只读审计工具，**不会修改任何配置**。风险主要来自"审计报告里包含主机敏感信息"，共享主机上建议用 `--no-log`。

### 场景 1：第一次审计（就从审计本机开始）

```bash
sudo lynis audit system --quick
```

预期输出片段：

```text
[ Lynis 3.1.6 ]

################################################################################
  Lynis comes with ABSOLUTELY NO WARRANTY. This is free software, and you are
  welcome to redistribute it under the terms of the GNU General Public License.
  See LICENSE file for details.
################################################################################

[+] Initializing program
------------------------------------
  - Detecting OS...                                           [ DONE ]
  - Checking profiles...                                      [ DONE ]

  ---------------------------------------------------
  Program version:           3.1.6
  Operating system:          Linux
  Operating system name:     Ubuntu
  Operating system version:  22.04
  ---------------------------------------------------

[+] Boot and services
------------------------------------
  - Checking boot loader files...                             [ FOUND ]
    - Checking /etc/default/grub...                           [ FOUND ]
  - Checking running services...                              [ DONE ]
  ...
  - Checking sensitive files...                               [ DONE ]
      - /etc/shadow                                            [ OK ]
      - /etc/ssh/sshd_config                                   [ OK ]
  ...

[+] Kernel Hardening
------------------------------------
  - Comparing sysctl key pairs with scan profile...
    - kernel.randomize_va_space                                [ OK ]
    - kernel.dmesg_restrict                                    [ SUGGESTION ]
    ...
```

末尾的摘要：

```text
  Hardening index : 63 [############        ]
  Tests performed : 275
  Plugins enabled : 1

  Files:
  - Test and debug information     : /var/log/lynis.log
  - Report data                    : /var/log/lynis-report.dat
```

解读：
- **`Hardening index : 63`** 是本次审计的量化结果。63 在默认安装的 Ubuntu 上是典型值——**说明有大量改进空间，不代表"不安全"**。
- `Tests performed : 275` 表示跑了多少项测试。
- **`[ SUGGESTION ]` 是建议，`[ WARNING ]` 才是需要修的问题**。区分这两者是读懂 lynis 报告的关键。

### 场景 2：只看警告 + 统计 /var/log/lynis.log 报告报告类型

```bash
# 只看警告
sudo lynis audit system --warnings-only

# 从报告文件里统计各种结果的数量
sudo grep -oP '^\w+\[\]\=\S+$' /var/log/lynis-report.dat | head -5
echo "--- 警告 ---"
sudo grep -c "^warning\[\]" /var/log/lynis-report.dat
echo "--- 建议 ---"
sudo grep -c "^suggestion\[\]" /var/log/lynis-report.dat
echo "--- 加固指数 ---"
sudo grep "^hardening_index" /var/log/lynis-report.dat
echo "--- 警告明细 ---"
sudo grep "^warning\[\]" /var/log/lynis-report.dat
```

预期输出片段：

```text
--- 警告 ---
4
--- 建议 ---
37
--- 加固指数 ---
hardening_index=63
--- 警告明细 ---
warning[]=SSH-7408|Consider hardening SSH configuration|AllowTcpForwarding (set YES to NO)|-
warning[]=PKGS-7392|Found one or more vulnerable packages||
warning[]=KRNL-6000|One or more sysctl values differ from the scan profile|kernel.dmesg_restrict (set 1 to 0)|
warning[]=DEB-0880|Found some information disclosure in the MOTD|/etc/motd|
```

解读：`lynis-report.dat` 是**逐行 key=value / key[]=value|...** 的结构化格式。`warning[]` 行的字段用 `|` 分隔：`测试ID|描述|具体项|当前值`。这个文件非常适合脚本处理，也是多主机集中收集的基础。

### 场景 3：审计一台"有问题的"实验机，并验证修复效果

```bash
# 1) 故意把实验靶机配置得不安全（只在你自己的靶机上做！）
sudo sed -i 's/^#*PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
sudo sed -i 's/^#*PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo systemctl restart ssh

# 2) 审计
sudo lynis audit system --quick -Q

# 3) 找到相关警告
sudo grep "^warning\[\]" /var/log/lynis-report.dat | grep -i ssh

# 4) 修复后只跑 SSH 相关测试（不用跑全套，几秒钟出结果）
sudo lynis audit system --tests "SSH-7408 SSH-7413" --quick
```

预期输出片段（修复前后对比）：

```text
# 修复前
warning[]=SSH-7408|Consider hardening SSH configuration|PermitRootLogin (set yes to no)|-

# 只跑单项复核
[+] SSH Support
------------------------------------
  - Checking sshd_config parameters...                        [ WARNING ]
    - PermitRootLogin                                          [ WARNING ]
```

解读：`--tests "SSH-7408"` 是**最高效的复核方式**——改完配置立刻跑单项测试，几秒钟确认。这比每次都跑 275 项测试实用得多。**测试 ID 的稳定性正是为这个场景设计的。**

### 场景 4（进阶）：自定义 profile + 定期巡检 + 结果 diff

**第 1 步：创建自定义 profile**（放在当前目录，用 `--use-cwd` 加载）

```bash
cat > lab.prf <<'EOF'
# 自定义审计 profile
# 排除不需要的测试（比如容器环境里不适用内核参数的检查）
skip-test=KRNL-6000

# 记录审计者
auditor="安全组"

# 发现警告时用退出码 78 返回（便于 cron 告警）
error-on-warnings=yes

# 不把敏感数据写盘
# no-log 只能命令行传，profile 里用下面这项控制日志细节
EOF

sudo lynis audit system --profile lab.prf --cronjob --use-cwd
echo "退出码: $?"
```

**第 2 步：放进 cron 做每周巡检**

```bash
# /etc/cron.weekly/lynis-audit
#!/bin/sh
REPORT="/var/log/lynis-report-$(date +%Y%m%d).dat"
/usr/sbin/lynis audit system --cronjob --report-file "$REPORT" \
    --logfile /var/log/lynis-cron.log >/dev/null 2>&1
# 保留最近 12 份
ls -1t /var/log/lynis-report-*.dat | tail -n +13 | xargs -r rm -f
```

**第 3 步：用 diff 跟踪加固进展**

```bash
# 对比两周的报告，只看警告项的变化
sudo diff <(grep "^warning\[\]" /var/log/lynis-report-20260901.dat | sort) \
          <(grep "^warning\[\]" /var/log/lynis-report-20260908.dat | sort)
```

预期输出片段：

```text
< warning[]=SSH-7408|Consider hardening SSH configuration|PermitRootLogin (set yes to no)|-
> warning[]=PKGS-7392|Found one or more vulnerable packages||
```

解读：`<` 是已修复的（SSH 那项没了），`>` 是新增的（出现了过期软件包警告）。**这个 diff 就是你给管理层看的"本周安全改进"。** lynis 相比一次性扫描工具的最大价值就在这里——它产出的是可比较、可跟踪的数据。

### 场景 5：渗透测试场景——低权限找提权线索

```bash
# 拿到一个低权限 shell 后（--pentest 不需要 root）
lynis audit system --pentest --quick

# 关注这几类：SUID 文件、可写的配置文件、过期内核
sudo grep -E "^(warning|suggestion)\[\]" /var/log/lynis-report.dat | grep -Ei "suid|writable|kernel|expos"
```

解读：`--pentest` 会跳过需要 root 的测试，但**剩下的测试里恰恰包含最有提权价值的线索**：SUID 文件、world-writable 脚本、可写服务配置、过期内核版本。这些是 `linpeas` 之类工具的输出重点，而 lynis 更"官方"且不需要额外下载。

**离线/取证场景**（审计已挂载的另一个系统）：

```bash
# 把目标磁盘挂到 /mnt/target，然后
sudo lynis audit system --forensics --rootdir /mnt/target --quick
```

## 6. 输出解读

### 三种结果标记

| 标记 | 含义 | 处理方式 |
|------|------|----------|
| `[ OK ]` | 该项已符合要求 | 无需动作 |
| `[ WARNING ]` | 明确的风险点 | **应修复**，纳入整改清单 |
| `[ SUGGESTION ]` | 改进建议 | 视环境取舍，不必全做 |

**新手最容易犯的错误是把 SUGGESTION 当成漏洞上报。** 一份完整的 Ubuntu 审计通常有 30~50 条 SUGGESTION，这很正常。

### `lynis-report.dat` 关键字段

| 字段 | 含义 |
|------|------|
| `hardening_index=` | 加固指数（0~100） |
| `warning[]=TEST-ID\|描述\|具体项\|当前值` | 警告明细 |
| `suggestion[]=TEST-ID\|描述\|...` | 建议明细 |
| `tests_performed=` | 执行的测试数 |
| `os=` / `os_name=` / `os_version=` | 系统信息 |
| `hostid=` | 主机 ID（多次审计对比用） |
| `installed_packages[]=` | 已安装包（可能很长） |
| `kernel_version=` | 内核版本 |

### 常见测试 ID 速查

| 测试 ID | 检查内容 |
|---------|----------|
| `SSH-7408` | SSH 配置加固（root 登录、算法等） |
| `SSH-7413` | SSH 是否允许空口令 |
| `KRNL-6000` | sysctl 与扫描 profile 的差异 |
| `KRNL-5820` | 内核版本是否过期 |
| `PKGS-7392` | 是否存在有已知漏洞的软件包 |
| `FILE-7524` | 敏感文件权限 |
| `AUTH-9282` | 密码策略 |
| `AUTH-9262` | 密码过期相关 |
| `HRDN-7230` | 恶意软件扫描工具是否安装 |
| `LOGG-2130` | 日志与审计配置 |
| `DEB-0880` | MOTD 信息泄露 |

> 完整列表：`lynis show groups`、`lynis show categories`；测试定义在 `/usr/share/lynis/include/tests_*`。

### 加固指数怎么用

- **不要追求 100**：某些项在特定环境下无法达成（比如容器里改不了内核参数）。
- **看趋势比看绝对值重要**：从 63 → 72 说明这轮整改有效。
- **按环境定目标**：生产服务器可以到 80+，开发机 60 分也算合理。

## 7. 与其他工具配合

```bash
# 1) 渗透测试：拿到低权 shell -> lynis 找提权线索
lynis audit system --pentest --quick
grep -E "^(warning|suggestion)\[\]" /var/log/lynis-report.dat | grep -Ei "suid|writable"

# 2) 多主机集中审计
for h in web01 web02 db01; do
  ssh "$h" 'sudo lynis audit system --cronjob --report-file /tmp/lynis.dat' 
  scp "$h:/tmp/lynis.dat" "reports/${h}-$(date +%F).dat"
done
# 汇总各主机的加固指数
grep -H "^hardening_index" reports/*.dat | sed 's|reports/||'

# 3) lynis 发现过期软件包 -> 精确定位
grep "^warning\[\]=PKGS-7392" /var/log/lynis-report.dat
# 然后手工确认（不同发行版命令不同）
sudo apt list --upgradable 2>/dev/null | head -20
# 或
sudo dnf check-update

# 4) lynis（主机侧）+ nuclei（服务侧）联合评估
lynis audit system --warnings-only
nuclei -u https://$(hostname -f) -severity high,critical -silent
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| 加固指数缺失 / 显示 `0` | 没用 root 运行 | `sudo lynis audit system` |
| 大量测试显示 `[ SKIPPED ]` | 权限不足或系统不支持 | 用 `sudo`；`--verbose` 看跳过原因 |
| 审计卡住不动 | 默认会等用户按键 | 加 `--quick` 或 `--cronjob` |
| 输出里全是颜色转义符 | 终端/重定向不支持 ANSI | `--no-colors` |
| `lynis` 报"不安全的输入字符" | 参数里有特殊字符 | 检查参数；用引号包裹 |
| 报告文件里含主机敏感信息 | 默认会记录详细配置 | `--no-log`（或用 `--logfile /dev/null`） |
| 容器里报一堆内核/引导相关警告 | 容器共享宿主机内核 | 用 profile `skip-test=KRNL-6000` 之类排除；这些项在容器里没意义 |
| 每次都提示 hostid 变化 | 换机器/重建容器 | 用 `lynis generate hostid` 固化或忽略 |
| cron 里跑出大量邮件 | 默认输出到 stdout | `--cronjob` + 重定向到 `/dev/null` |
| 想看某项测试到底检查了什么 | 不知道测试定义在哪 | 在 `/usr/share/lynis/include/tests_*` 里搜测试 ID |
| 运行时报缺文件 | 上次扫描被中断 | 删掉 `/var/log/lynis.log` 与 `report.dat` 后重跑 |
| `--tests` 传多个 ID 失败 | 需要以字符串整体传入 | 加引号：`--tests "SSH-7408 SSH-7413"` |

## 9. 防御视角（蓝队）

lynis **本身就是蓝队工具**，这一节直接讲怎么把它用成一套加固流程。

- **把它当"体检 + 趋势跟踪"用**：
  1. **基线**：在新部署的服务器上跑一次，记下加固指数与警告清单。
  2. **定期巡检**：用 cron 每周跑一次，报告归档并保留 12 份。
  3. **diff 驱动改进**：每周对比警告项，修复的关闭、新增的评估。
  4. **指标化**：加固指数作为团队 KPI 之一（注意不要唯分数论）。
- **优先级建议**（按投入产出比排序）：
  | 优先级 | 检查项 | 说明 |
  |--------|--------|------|
  | 高 | SSH 配置（`SSH-7408`） | 禁 root 登录、禁口令认证、限算法，一次改永久受益 |
  | 高 | 有漏洞的软件包（`PKGS-7392`） | 补丁是最基础的防线 |
  | 高 | 内核/系统过期（`KRNL-5820`） | 提权漏洞的主要来源 |
  | 中 | 密码策略（`AUTH-9282`） | 配合锁定策略，抑制爆破 |
  | 中 | 日志与审计（`LOGG-2130`） | 没有日志就没有检测 |
  | 中 | sysctl 加固（`KRNL-6000`） | `dmesg_restrict`、`kptr_restrict`、`randomize_va_space` |
  | 低 | MOTD / banner 信息泄露（`DEB-0880`） | 减少信息收益 |
- **配合检测能力建设**：
  - lynis 告诉你"配置哪里弱"，但**不告诉你有没有人正在攻击**。要和 `auditd`、`fail2ban`、集中日志（rsyslog/journal → SIEM）配套使用。
  - `LOGG-2130` 相关的建议应该优先做——因为**日志与审计是其他所有检测手段的前提**。
- **对渗透测试方的提醒**：lynis 的 `--pentest` 输出对攻击方同样是"提权路线图"。所以从防守角度看，**跑一遍 lynis 看看"如果我是低权用户，能从这里拿到什么"** 是最务实的自查方式。
- **合规映射**：lynis 的测试项与 CIS Benchmark、ISO 27001 控制项有对应关系（在 `/usr/share/lynis/db/` 里有映射数据），可以直接用来支撑合规审计的证据收集。

## 10. 参考

- 官方项目页：<https://cisofy.com/lynis/>
- 官方仓库：<https://github.com/CISOfy/lynis>
- 支持文档：<https://cisofy.com/support/>
- 加固指南（按发行版）：<https://cisofy.com/documentation/>
- Kali 工具页：<https://www.kali.org/tools/lynis/>
- man page：`man lynis`
- 用法核实：本教程参数取自 `lynis 3.1.6` 的 man page，并与上游 `include/parameters` 中的实际参数解析逻辑交叉核对

---

**相关教程**：[nuclei](nuclei.md) ｜ [nikto](nikto.md) ｜ [searchsploit](searchsploit.md) ｜ [openssl](openssl.md) ｜ [nmap](../01-信息搜集/nmap.md)
