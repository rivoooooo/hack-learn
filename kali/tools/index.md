# Kali 工具库总览

收录 Kali Linux 官方工具文档中的 **780** 个工具包、**501** 条命令级条目，覆盖 **16** 个功能分类。全部数据由脚本从官网同步，可随时复核。

## 两种查法

| 你想做什么 | 去哪查 |
|------------|--------|
| 按**攻击阶段**找工具（先侦察？要提权？） | [按功能分类](#功能分类导航) |
| 按**包名/命令名**找细节 | [catalog/ 按包速查](catalog/all-tools.md) |
| **从零开始用一个工具**（安装 → 官方示例 → 参数 → 实践清单） | [reference/ 工具参考文档](reference/README.md) |
| 学重点工具的完整用法（原理 + 靶场实操） | [tutorials/](tutorials/README.md) |
| 直接搜索 | `grep -i '关键词' data/kali-tools.tsv` |

## 功能分类导航

Kali 官方按**攻击/防御阶段**组织工具（命名参考 MITRE ATT&CK 战术）。下表按官方顺序排列：

| 分类 | 子类 | 命令数 | 说明 | 目录 |
|------|------|--------|------|------|
| **侦察** | 8 | 87 | 在动手之前尽可能了解目标：主机、身份、网络与 Web 面。 | [Reconnaissance](by-attack/reconnaissance.md) |
| **资源开发** | 1 | 40 | 搭建攻击基础设施：C2 服务器、重定向器、Payload 托管。 | [Resource Development](by-attack/resource-development.md) |
| **初始访问** | 1 | 11 | 打进第一台机器：Web 漏洞、口令、钓鱼、暴露服务。 | [Initial Access](by-attack/initial-access.md) |
| **执行** | 1 | 6 | 在目标上运行代码：命令执行、脚本宿主、宏与解释器滥用。 | [Execution](by-attack/execution.md) |
| **持久化** | 1 | 8 | 维持访问：账号、服务、计划任务、后门与 rootkit。 | [Persistence](by-attack/persistence.md) |
| **权限提升** | 1 | 6 | 从普通用户到 root/SYSTEM：内核漏洞、配置错误、令牌滥用。 | [Privilege Escalation](by-attack/privilege-escalation.md) |
| **防御规避** | 1 | 23 | 绕过检测：混淆、加壳、日志清除、免杀与白利用。 | [Defense Evasion](by-attack/defense-evasion.md) |
| **凭据访问** | 8 | 62 | 拿凭据：内存转储、哈希、Kerberos 攻击、口令破解。 | [Credential Access](by-attack/credential-access.md) |
| **发现** | 11 | 80 | 摸清内网：主机、账户、共享、进程与服务发现。 | [Discovery](by-attack/discovery.md) |
| **横向移动** | 1 | 3 | 横向扩散：远程执行、凭据复用、协议隧道。 | [Lateral Movement](by-attack/lateral-movement.md) |
| **收集** | 1 | 14 | 收集高价值数据：文件、屏幕、键盘、邮件与数据库。 | [Collection](by-attack/collection.md) |
| **命令与控制** | 3 | 37 | 建立稳定通道：C2 框架、隧道、隐蔽协议。 | [Command And Control](by-attack/command-and-control.md) |
| **数据外泄** | 1 | 3 | 把数据带出去：通道选择、分块与伪装。 | [Exfiltration](by-attack/exfiltration.md) |
| **影响** | 1 | 10 | 造成影响：破坏、加密（勒索）、服务中断与擦除（红队演练中仅作演示）。 | [Impact](by-attack/impact.md) |
| **数字取证** | 5 | 76 | 事后取证：镜像、雕复、时间线、内存与日志分析。 | [Forensics](by-attack/forensics.md) |
| **服务与其它工具** | 2 | 35 | 系统服务、开发与通用工具。 | [Services And Other Tools](by-attack/services-and-other-tools.md) |

## 按包速查（全量）

| 分组 | 包数 | 目录 |
|------|------|------|
| 信息搜集 | 91 | [catalog/information-gathering.md](catalog/information-gathering.md) |
| 漏洞分析 | 38 | [catalog/vulnerability.md](catalog/vulnerability.md) |
| Web 应用 | 54 | [catalog/web.md](catalog/web.md) |
| 口令攻击 | 34 | [catalog/passwords.md](catalog/passwords.md) |
| 无线攻击 | 47 | [catalog/wireless.md](catalog/wireless.md) |
| 漏洞利用 | 8 | [catalog/exploitation.md](catalog/exploitation.md) |
| 嗅探与欺骗 | 14 | [catalog/sniffing-spoofing.md](catalog/sniffing-spoofing.md) |
| 后渗透 | 13 | [catalog/post-exploitation.md](catalog/post-exploitation.md) |
| 数字取证 | 89 | [catalog/forensics.md](catalog/forensics.md) |
| 逆向工程 | 2 | [catalog/reverse-engineering.md](catalog/reverse-engineering.md) |
| 报告与记录 | 4 | [catalog/reporting.md](catalog/reporting.md) |
| 硬件攻击 | 5 | [catalog/hardware.md](catalog/hardware.md) |
| 密码学与隐写 | 6 | [catalog/crypto-stego.md](catalog/crypto-stego.md) |
| 识别与指纹 | 12 | [catalog/identify.md](catalog/identify.md) |
| 检测 | 1 | [catalog/detect.md](catalog/detect.md) |
| 防护 | 4 | [catalog/protect.md](catalog/protect.md) |
| Top 10 常用 | 4 | [catalog/top10.md](catalog/top10.md) |
| 事件响应 | 2 | [catalog/respond.md](catalog/respond.md) |
| Windows 资源 | 7 | [catalog/windows-resources.md](catalog/windows-resources.md) |
| 通用工具 | 345 | [catalog/utils.md](catalog/utils.md) |

全量 A–Z 清单：▶ [catalog/all-tools.md](catalog/all-tools.md)

## 使用示例

```bash
# 找所有口令攻击类工具
awk -F'\t' '$3=="passwords" {print $2, "|", $6}' data/kali-tools.tsv

# 按 ATT&CK 分类名过滤
awk -F'\t' '$4=="凭据访问" {print $2}' data/kali-tools.tsv

# 搜索描述里含 SQL 注入的工具
grep -i 'sql injection' data/kali-tools.tsv | cut -f1,2
```

## 数据来源与维护

```bash
# 重新同步工具元数据（约 800 个页面，1–2 分钟）
python3 scripts/fetch_kali_tools.py --workers 6
# 重新同步功能分类树
python3 scripts/fetch_kali_categories.py
# 重新生成本目录
python3 scripts/gen_kali_index.py
```

- 工具元数据：<https://www.kali.org/tools/all-tools/>
- 功能分类树：<https://www.kali.org/tools/>
- 未被功能分类收录的包：362 个（多为依赖库或元包）
