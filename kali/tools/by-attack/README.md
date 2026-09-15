# 按攻击阶段查工具

Kali 官网的工具首页把工具按**攻击/防御阶段**组织，命名参考 MITRE ATT&CK 的战术（Tactics）。
本目录是这套结构的本地化快照，共 **16 个分类、47 个子类别、501 条命令级条目**。

数据来源：<https://www.kali.org/tools/>

---

## 16 个分类

| # | 分类 | 子类 | 命令数 | 这个阶段要干什么 |
|---|------|------|--------|------------------|
| 1 | [侦察（Reconnaissance）](reconnaissance.md) | 8 | 87 | 动手之前了解目标：主机、身份、网络、Web 面 |
| 2 | [资源开发（Resource Development）](resource-development.md) | 1 | 40 | 搭攻击基础设施：C2、重定向器、Payload 托管 |
| 3 | [初始访问（Initial Access）](initial-access.md) | 1 | 11 | 打进第一台机器：Web 漏洞、口令、钓鱼、暴露服务 |
| 4 | [执行（Execution）](execution.md) | 1 | 6 | 在目标上运行代码 |
| 5 | [持久化（Persistence）](persistence.md) | 1 | 8 | 维持访问：账号、服务、计划任务、后门 |
| 6 | [权限提升（Privilege Escalation）](privilege-escalation.md) | 1 | 6 | 从普通用户到 root / SYSTEM |
| 7 | [防御规避（Defense Evasion）](defense-evasion.md) | 1 | 23 | 绕过检测：混淆、加壳、日志清除、免杀 |
| 8 | [凭据访问（Credential Access）](credential-access.md) | 8 | 62 | 拿凭据：内存转储、哈希、Kerberos、口令破解 |
| 9 | [发现（Discovery）](discovery.md) | 11 | 80 | 摸清内网：主机、账户、共享、进程、服务 |
| 10 | [横向移动（Lateral Movement）](lateral-movement.md) | 1 | 3 | 横向扩散：远程执行、凭据复用、协议隧道 |
| 11 | [收集（Collection）](collection.md) | 1 | 14 | 收集高价值数据 |
| 12 | [命令与控制（Command and Control）](command-and-control.md) | 3 | 37 | 建立稳定通道：C2 框架、隧道、隐蔽协议 |
| 13 | [数据外泄（Exfiltration）](exfiltration.md) | 1 | 3 | 把数据带出去 |
| 14 | [影响（Impact）](impact.md) | 1 | 10 | 造成影响（红队演练中仅作演示） |
| 15 | [数字取证（Forensics）](forensics.md) | 5 | 76 | 事后取证：镜像、雕复、时间线、内存 |
| 16 | [服务与其它工具（Services and Other Tools）](services-and-other-tools.md) | 2 | 35 | 系统服务、开发与通用工具 |

---

## 怎么用这套分类

### 一次完整的演练顺序

```
1  侦察          找目标、探边界
2  资源开发      准备 C2 与 Payload（红队内部准备，不接触目标）
3  初始访问      打进第一台机器
4  执行          在目标上跑起代码
5  持久化        别一重启就没了
6  权限提升      拿到管理员
7  防御规避      让 EDR / 日志看不见你
8  凭据访问      偷更多的钥匙
9  发现          用钥匙打开更多门
10 横向移动      一台变一片
11 收集          找值钱的东西
12 命令与控制    保持稳定通道
13 数据外泄      带出去
14 影响          证明"能造成多大破坏"（授权演练才做）
```

### 蓝队 / 取证视角

分类 15（数字取证）与 16（服务与其它工具）是防守方的入口：
用取证工具做镜像、时间线、内存分析；用这些工具回答"发生了什么、影响范围多大"。

反过来，把 1–14 阶段的攻击动作映射到 ATT&CK 技术编号，
就能做检测覆盖度分析——具体方法见
[`web-security/mitre-attack/`](../../../web-security/mitre-attack/)。

---

## 与 ATT&CK 的关系（重要区别）

| 项目 | 本目录 | [MITRE ATT&CK](../../../web-security/mitre-attack/) |
|------|--------|-----------------------------------------------------|
| 是什么 | Kali **工具**的阶段分类 | 攻击者**行为**的知识库 |
| 回答 | "这个阶段我有哪些工具可用" | "这个攻击行为叫什么、编号是多少" |
| 粒度 | 工具命令 | 战术（Tactic）与技术（Technique） |
| 权威来源 | Kali 官网 | MITRE |

> ⚠️ Kali 的这 16 个分类**只是借用 ATT&CK 的命名风格**，并非 ATT&CK 官方分类，
> 数量也不等于 ATT&CK 的战术数（企业域当前为 15 个，且包含 Kali 没有单独列出的
> `TA0042 Resource Development`、`TA0112 Defense Impairment` 等差异项）。
> 做正式的技术映射时**以 MITRE 官网为准**。

---

## 其它查法

| 需求 | 去哪 |
|------|------|
| 按包名/命令名查细节 | [`../catalog/`](../catalog/) |
| 全量 A–Z 清单 | [`../catalog/all-tools.md`](../catalog/all-tools.md) |
| 重点工具的完整教程 | [`../tutorials/`](../tutorials/) |
| 命令行搜索 | `awk -F'\t' '$4=="凭据访问"' data/kali-tools.tsv` |

---

## 数据来源与重新生成

```bash
python3 scripts/fetch_kali_categories.py    # 抓取官网分类树
python3 scripts/gen_kali_index.py           # 生成本目录
```

详细说明见 [`scripts/README.md`](../../../scripts/README.md)。
