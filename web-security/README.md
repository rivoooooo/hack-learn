# Web 与安全标准模块总纲

本模块把 **6 套安全标准**放在一起讲，因为它们各自只回答一个维度的问题，**必须组合使用才构成完整的攻防知识体系**。

> 版本与编号均以各官方站点的当前状态为准。本模块各子页已在页内标注抓取日期与核实边界。
> 各官方站点更新频繁，**动手前请回到官方页面核对版本**。

---

## 1. 先建立全局认知：6 份标准分别回答什么问题

初学者最容易犯的错误，是把这 6 套编号体系混着用——比如用 ATT&CK 编号代替 CWE 报弱点，或者拿 NIST 的控制目录当测试清单。**它们不是同层替代品，而是不同层级的工具。**

| # | 标准 | 一句话定位 | **回答什么问题** | 编号体系 | 视角 | 典型误用 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **OWASP / WSTG** | Web 风险与测试方法 | 「Web 应用**该测哪些项**？**怎么测**？」 | `A01:2025`…`A10:2025`（Top 10 风险分类）；WSTG 的测试项编号 | 应用层风险 | 把 Top 10 当漏洞清单逐条打勾 |
| 2 | **MITRE ATT&CK** | 对手战术与技术 | 「攻击者**用什么行为**达成目的？」 | `TAxxxx`（战术）、`Txxxx[.xxx]`（技术/子技术）、`Gxxxx`（组织）、`Sxxxx`（软件） | 对手行为 | 用 ATT&CK 编号代替 CWE/CVE 报漏洞 |
| 3 | **PTES** | 渗透测试流程标准 | 「一次渗透测试**按什么步骤做**？每步产出什么？」 | 无编号体系，7 个阶段 | 项目流程 | 把它当技术手册读（技术细节在 Technical Guidelines 与 WSTG） |
| 4 | **Exploit-DB** | 漏洞利用库 | 「这个漏洞**有没有能跑的利用代码**？」 | `EDB-ID`（如 50592） | 武器/利用代码 | 以为 EDB 里搜不到就等于没漏洞 |
| 5 | **CWE** | 弱点类型字典 | 「这个缺陷**属于哪一类弱点**？」 | `CWE-<数字>`（如 CWE-89） | 弱点类型 | 把 CWE 当成某个具体漏洞的编号（那是 CVE） |
| 6 | **NIST SP 800** | 安全规范与评估方法 | 「**应该有哪些控制**？**怎么评估**？验收标准是什么？」 | `SP 800-xxx`（如 SP 800-115、800-53、800-61、800-40） | 规范与合规 | 拿 SP 800-53 的控制目录当测试清单用 |

### 一个例子把六者串起来

假设你发现某系统的订单查询接口可以越权读取他人订单：

| 标准 | 在这个例子里回答什么 |
| --- | --- |
| **CWE** | 这是 `CWE-639` Authorization Bypass Through User-Controlled Key（类型）——同类问题还有 `CWE-862` 缺失授权、`CWE-863` 授权不正确 |
| **CVE** | 如果是产品化的第三方组件，会有一个 `CVE-20XX-XXXXX`（实例）；自研业务逻辑缺陷通常没有 CVE |
| **Exploit-DB** | 自研逻辑缺陷通常没有公开 EDB 条目，需要自研 PoC；若是组件漏洞，先查 `searchsploit --cve` |
| **ATT&CK** | 攻击者利用公网应用的行为 → `T1190` Exploit Public-Facing Application |
| **OWASP** | 归属 `A01:2025 Broken Access Control`（该分类含 40 个 CWE，官方称 100% 被测应用都存在某种形式的访问控制失效） |
| **PTES** | 这是阶段四"漏洞分析"的产出，需要走证据取证、风险评级，进入阶段七报告 |
| **NIST SP 800** | 报告中把发现映射到 SP 800-53 的控制族（如 AC 访问控制）；补丁与整改排期依据 SP 800-40；验收标准可引用 SP 800-115 的评估方法 |

**看出来了吗**：一个技术发现，在这 6 套标准里各有各的坐标。**专业报告的价值就在于把这 6 个坐标都标出来**——只写"发现越权"是不完整的。

---

## 2. 两两关系速查

有几组关系特别容易被搞混，单独列出来。

### CWE（类型）vs CVE（实例）vs EDB-ID（利用代码）

```
CWE-89  「SQL 注入这一类弱点」
   ├── CVE-2026-1111  某产品 3.2 版的 SQL 注入实例
   │       └── EDB-51000   针对它的 PoC
   ├── CVE-2026-2222  另一个产品的 SQL 注入实例
   │       └── （暂无公开 EXP）
   └── CVE-2026-3333  第三个实例
           └── EDB-51111
```

- **CWE 是类型，CVE 是实例。** 一个 CWE 对应成千上万个 CVE。
- **一个 CVE 可以有多个 EDB 条目**（不同作者的不同实现）；**一个 EDB 条目也可以对应多个 CVE**。
- **EDB 只收录有公开 exp/PoC 的漏洞**，所以"EDB 搜不到" ≠ "没有漏洞"。
- **大量 EDB 条目没有 CVE**（老式本地提权 PoC、通用绕过思路等）。

### OWASP Top 10（风险分类）vs CWE（弱点类型）

- **OWASP Top 10 是风险视角**，一个分类对应**多个** CWE。2025 版共在 10 个分类下映射 **248 个 CWE**（官方数据），平均每类约 25 个。
- **CWE Top 25 是弱点视角**，每条就是一个具体弱点类型，共 25 条。
- **实操分工**：对决策者汇报用 OWASP 分类（"你有访问控制问题"），对开发排期用 CWE 编号（"请修 CWE-862 和 CWE-639 这两处"）。
- 详见 [CWE 模块的对照总览](./cwe/README.md#5-cwe-与-owasp-top-102025-的对照总览)。

### PTES（流程）vs NIST SP 800-115（方法学与验收）

- **PTES 管"按什么顺序走"**（7 阶段），有威胁建模与后渗透这两个 SP 800-115 没有的部分。
- **SP 800-115 管"手法是否完整、计划是否完备、数据怎么处理"**（三类技术 + 三阶段方法学 + 评估计划必答五问 + 数据处理四环节），并把"检查（Examination）"与"测试（Testing）"严格分开——**前者通常不影响目标系统**，这在可用性敏感的场景里是关键的裁剪依据。
- **推荐用法**：用 PTES 定流程骨架，用 SP 800-115 补强被你跳过的环节。详见 [NIST SP 800-115 专篇第 8 节](./nist/800-115.md#8-与-ptes-的异同)。

### 威胁建模：PTES 有，SP 800-115 没有

SP 800-115 的 Discovery → Attack 是**能力驱动**（扫到什么打什么）；PTES 的 Threat Modeling 是**目标驱动**（先定哪些路径值得打）。**ATT&CK 是填这一步最好的工具**——用攻击组织（`Gxxxx`）的真实 TTP 做基线，比凭经验排优先级可靠得多。

---

## 3. 子目录索引

### OWASP 部分

| 页面 | 内容 |
| --- | --- |
| [owasp/README.md](./owasp/README.md) | OWASP 模块总览与定位 |
| [owasp/top10/README.md](./owasp/top10/README.md) | **OWASP Top 10:2025** 十个风险分类总览 |
| [owasp/top10/A01-Broken-Access-Control.md](./owasp/top10/A01-Broken-Access-Control.md) | A01 访问控制失效 |
| [owasp/top10/A02-Security-Misconfiguration.md](./owasp/top10/A02-Security-Misconfiguration.md) | A02 安全配置错误 |
| [owasp/top10/A03-Software-Supply-Chain-Failures.md](./owasp/top10/A03-Software-Supply-Chain-Failures.md) | A03 软件供应链失效 |
| [owasp/top10/A04-Cryptographic-Failures.md](./owasp/top10/A04-Cryptographic-Failures.md) | A04 加密机制失效 |
| [owasp/top10/A05-Injection.md](./owasp/top10/A05-Injection.md) | A05 注入 |
| [owasp/top10/A06-Insecure-Design.md](./owasp/top10/A06-Insecure-Design.md) | A06 不安全设计 |
| [owasp/top10/A07-Authentication-Failures.md](./owasp/top10/A07-Authentication-Failures.md) | A07 认证失效 |
| [owasp/top10/A08-Software-or-Data-Integrity-Failures.md](./owasp/top10/A08-Software-or-Data-Integrity-Failures.md) | A08 软件或数据完整性失效 |
| [owasp/top10/A09-Security-Logging-and-Alerting-Failures.md](./owasp/top10/A09-Security-Logging-and-Alerting-Failures.md) | A09 安全日志与告警失效 |
| [owasp/top10/A10-Mishandling-of-Exceptional-Conditions.md](./owasp/top10/A10-Mishandling-of-Exceptional-Conditions.md) | A10 异常情况处理不当 |
| [owasp/wstg/README.md](./owasp/wstg/README.md) | **WSTG**（Web 安全测试指南）导读 |
| [owasp/wstg/checklist.md](./owasp/wstg/checklist.md) | WSTG 测试项检查表 |
| [owasp/labs.md](./owasp/labs.md) | OWASP / WSTG 练习 |

> 注：仓库根下另有一个 `web-security/wstg/` 空目录。**WSTG 的内容在 [owasp/wstg/](./owasp/wstg/README.md) 下**，请以该路径为准。

### MITRE ATT&CK

| 页面 | 内容 |
| --- | --- |
| [mitre-attack/README.md](./mitre-attack/README.md) | ATT&CK 是什么；**企业域 15 个战术**全表（含 ID）；Mobile 12 个、ICS 12 个；技术编号规则 `Txxxx.xxx`；三个技术域区别；Navigator 热力图操作步骤；红队/蓝队/Purple Team 三种用法 |
| [mitre-attack/mapping-guide.md](./mitre-attack/mapping-guide.md) | 把测试发现映射到 ATT&CK 技术编号（3 个完整示例 + 7 类常见映射错误 + 自查清单） |
| [mitre-attack/labs.md](./mitre-attack/labs.md) | 练习：创建层 → 导出/导入 JSON → 模拟 APT 的 TTP 覆盖度分析 → 生成热力图 |

### PTES

| 页面 | 内容 |
| --- | --- |
| [ptes/README.md](./ptes/README.md) | **7 个阶段**逐阶段讲：目标、输入、输出、关键动作、常见失误；与 SP 800-115 的关系 |
| [ptes/templates.md](./ptes/templates.md) | 可直接套用的交付物模板：授权书 SOW 要点、范围表、测试计划、每日进度记录、漏洞记录表（含 **CVSS v4.0 字段规范**）、最终报告结构 |
| [ptes/labs.md](./ptes/labs.md) | 练习：为假想目标（星海医疗器械）写完整测试计划与授权书，含六项任务与验收清单 |

### Exploit-DB

| 页面 | 内容 |
| --- | --- |
| [exploit-db/README.md](./exploit-db/README.md) | EDB 是什么；EDB-ID；检索方式（网页 / `searchsploit` / CVE 映射）；**全部 searchsploit 参数逐条核实**；条目字段解读（以 EDB-50592 为例）；exploit 与 shellcode 的区别 |
| [exploit-db/labs.md](./exploit-db/labs.md) | 练习：安装 searchsploit → 用 CVE 检索 → 落地并阅读分析 → 在合法靶场做最小验证 |

### CWE

| 页面 | 内容 |
| --- | --- |
| [cwe/README.md](./cwe/README.md) | CWE 是什么；编号体系；CWE/CVE 关系；**2025 年 Top 25 完整表格**（ID、官方名称、中文、典型后果、分值、KEV 计数、名次变化、**OWASP Top 10:2025 归属**）；如何指导代码审计与安全需求 |
| [cwe/audit-guide.md](./cwe/audit-guide.md) | **12 个重点弱点**的代码审计检查点：易出现的代码模式、grep 思路、误报排除 |
| [cwe/labs.md](./cwe/labs.md) | 练习：3 段自拟有缺陷代码，定位 CWE 编号并修复（含答案、根因、最小验证思路、修复代码、误报排除） |

### NIST SP 800

| 页面 | 内容 |
| --- | --- |
| [nist/README.md](./nist/README.md) | SP 800 系列是什么；**19 篇重点文档导读**（编号、全称、发布、取代关系、解决什么问题、实际用途）；三个最容易踩的坑 |
| [nist/800-115.md](./nist/800-115.md) | **SP 800-115 专篇**：完整章节结构；三阶段方法学；**三类技术手法**；测试视角；渗透测试四阶段；评估计划必答五问；数据处理四环节；与 PTES 的异同；如何借用其检查表结构 |
| [nist/labs.md](./nist/labs.md) | 练习：为虚构的内部系统（云帆物流结算平台）设计完整安全评估方案，含分批裁剪与跨标准对齐 |

---

## 4. 实战工作流：从接单到交付，6 套标准各管一段

下面是一条**端到端的推荐工作流**。每一项都标注了「用哪套标准 + 落在哪个文件」。

```
┌─────────────────────────────────────────────────────────────┐
│ 阶段 0  接单与授权                                            │
│   用：PTES 阶段一（Pre-engagement）+ NIST SP 800-115 第 6 章   │
│   ─────────────────────────────────────────────────────       │
│   • 授权书、范围表、RoE  → ptes/templates.md                  │
│   • RoE 官方模板        → SP 800-115 附录 B                   │
│   • 法律考量与法务参与   → SP 800-115 第 6.6 节               │
│   • 评估计划"必答五问"   → nist/800-115.md 第 9.2 节          │
│   • 评估人员独立账号     → SP 800-115 第 6.4.2 节             │
│   • 数据处理四环节       → SP 800-115 第 7.4 节               │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 阶段 1  情报收集                                              │
│   用：PTES 阶段二 + SP 800-115 第四章（Target Identification）│
│   ─────────────────────────────────────────────────────       │
│   • 被动/主动情报分层，主动扫描必须已授权                     │
│   • 端口与服务识别 → 用 searchsploit --nmap 把指纹转成候选 EXP │
│   • 核对公网地址归属（WHOIS）→ SP 800-115 第 5.2.2 节脚注 20  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 阶段 2  威胁建模  ← 这一步决定了后面所有工作的优先级           │
│   用：PTES 阶段三 + MITRE ATT&CK                              │
│   ─────────────────────────────────────────────────────       │
│   • 选一个与自身行业匹配的攻击组织（Gxxxx）                   │
│   • 用 Navigator 的 Search & Multiselect 一次性选中该组织的    │
│     全部技术 → 导出"基线层"                                  │
│   • 对基线层做环境适用性过滤（Platform Filter）               │
│   • 产出：排好序的攻击路径清单 + ATT&CK 映射                  │
│   → mitre-attack/README.md 第 7 节、mitre-attack/labs.md 实验2 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 阶段 3  Web 应用测试                                          │
│   用：OWASP Top 10 + WSTG                                     │
│   ─────────────────────────────────────────────────────       │
│   • 按 OWASP Top 10:2025 十个分类确认覆盖范围                 │
│   • 用 WSTG 检查表逐项执行（这是"具体怎么测"的答案）          │
│   • 注意：扫描器输出只是线索，不是结论                        │
│   → owasp/top10/、owasp/wstg/checklist.md                     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 阶段 4  漏洞分析与验证                                        │
│   用：PTES 阶段四 + NIST SP 800-115 第五章（Validation）       │
│        + Exploit-DB + CWE                                     │
│   ─────────────────────────────────────────────────────       │
│   • 参数化/数据流分析 → cwe/audit-guide.md                    │
│   • 找现成 EXP       → searchsploit --cve / --nmap            │
│   • 人工验证可利用性 → 这一步不能省（扫描器只说"可能存在"）   │
│   • 弱点归类         → cwe/README.md 的 2025 Top 25           │
│   • 行为映射         → mitre-attack/mapping-guide.md          │
│   • 产出：已验证漏洞清单（含证据、前置条件、影响）            │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 阶段 5  利用与后渗透                                          │
│   用：PTES 阶段五、六 + MITRE ATT&CK（执行与记录）             │
│   ─────────────────────────────────────────────────────       │
│   • 每次利用记录：时间戳、源 IP、目标、手法、EXP 编号、结果   │
│   • 触发 RoE 停手条件立即停手并通报                           │
│   • 后渗透聚焦"业务影响"，不是"再拿一台机器"                  │
│   • 清理清单必须逐项列出                                      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 阶段 6  定验收标准与整改建议                                  │
│   用：NIST SP 800-40（补丁）+ SP 800-53/53A（控制与评估）      │
│        + SP 800-61 Rev.3（事件响应）+ SP 800-207（架构）       │
│   ─────────────────────────────────────────────────────       │
│   • 补丁类建议：按"识别—排优先级—获取—安装—验证"五步写        │
│     优先级依据：有无公开 EXP + 是否在 KEV + 是否命中 Top 25    │
│     + 是否暴露公网（→ nist/README.md 第 3.4 节）              │
│   • 把发现映射到 SP 800-53 的控制族，让客户按控制项排期        │
│   • 架构级整改（内网可信假设不成立）→ 引用 SP 800-207          │
│   • 检测能力评估 → SP 800-61 Rev.3                            │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 阶段 7  报告与交付                                            │
│   用：PTES 阶段七 + NIST SP 800-115 第八章                    │
│   ─────────────────────────────────────────────────────       │
│   • 报告结构（执行摘要/方法论/发现/风险评级/修复建议/附录）    │
│     → ptes/templates.md 第 6 节                               │
│   • 每个发现的五要素：CWE + CVE + EDB-ID + CVSS + ATT&CK       │
│   • 必须写明限制：未覆盖的范围、固有限制、未验证的可疑点       │
│   • 附：数据销毁确认函、评估账号禁用记录、清理清单             │
└─────────────────────────────────────────────────────────────┘
```

### 这张图的三个要点

1. **编号体系的分工不能混。** 一个发现要同时给出「CWE（类型）+ CVE（实例，若有）+ EDB-ID（利用代码，若有）+ CVSS（严重度）+ ATT&CK（行为）+ OWASP 分类（风险归属）」六个坐标。只写"发现越权"是不完整的报告。
2. **"扫描 ≠ 验证"是贯穿全程的红线。** SP 800-115 第 5.2.1 节的原文说得最清楚：**漏洞扫描器只检查漏洞可能存在，而渗透测试的攻击阶段利用漏洞来确认其存在**。任何未经验证的扫描结果都**不能**进入报告的正式发现章节。
3. **威胁建模（阶段 2）是最容易被跳过、却最影响结论有效性的一步。** 没有它，你的测试就是"能力驱动"的——只反映你会什么，不反映客户真正的威胁态势。

---

## 5. 快速上手路径

如果你第一次接触这个模块，建议按下面的顺序读。

### 路径 A：我要做一次渗透测试（实操优先）

```
1. ptes/README.md                        ← 先建立流程骨架（7 阶段）
2. ptes/templates.md                     ← 拿到授权书/范围表/计划/记录的模板
3. ptes/labs.md                          ← 动手写一遍，跑通一遍流程感
4. mitre-attack/README.md                ← 学会威胁建模的工具（第 7 节 Navigator 操作）
5. mitre-attack/mapping-guide.md         ← 学会把发现映射成技术编号
6. owasp/wstg/checklist.md               ← 具体测 Web 时对着打勾
7. exploit-db/README.md                  ← 找 EXP 时查参数
8. cwe/README.md                         ← 归类发现时查 Top 25
9. nist/800-115.md                       ← 最后补上"计划是否完备、数据怎么处理、手法是否漏了"
```

### 路径 B：我要做代码审计

```
1. cwe/README.md                         ← 建立弱点类型认知，看清 2025 Top 25
2. cwe/audit-guide.md                    ← 12 个重点弱点的代码模式 + grep 思路 + 误报排除
3. cwe/labs.md                           ← 动手定位 3 段有缺陷代码
4. owasp/top10/                          ← 补上风险分类视角，便于和业务沟通
5. mitre-attack/mapping-guide.md         ← 把代码缺陷映射成攻击行为（打通到防守侧）
6. nist/README.md 第 3.1、3.2 节         ← 把发现上升为安全需求（CWE → SP 800-53 控制）
```

### 路径 C：我是防守方 / 蓝队

```
1. mitre-attack/README.md                ← 建立对手行为语言
2. mitre-attack/labs.md                  ← 做一次 TTP 覆盖度热力图
3. mitre-attack/mapping-guide.md         ← 看懂红队报告里的编号
4. cwe/README.md                         ← 从"修漏洞"转向"消除弱点类"
5. nist/README.md 第 3.3、3.4 节         ← 事件响应（SP 800-61 Rev.3）与补丁管理（SP 800-40）
6. nist/README.md 第 3.6 节              ← 零信任（SP 800-207）作为架构级整改依据
```

### 路径 D：我要给团队建评估能力（管理视角）

```
1. nist/800-115.md 第 9.3 节             ← 用 SP 800-115 第 6.1 节的五项做评估政策自评
2. nist/800-115.md 第 9.1 节             ← 三类技术 × 四阶段覆盖度矩阵
3. nist/labs.md                          ← 完整走一遍方案设计（含分批裁剪）
4. ptes/README.md                        ← 阶段组织与交付物清单
5. ptes/templates.md                     ← 全套交付物模板
```

---

## 6. 本模块自学自测

读完全部子页后，你应该能回答下面这些问题。**答不上来的，回到对应页面重读。**

| # | 问题 | 答案在哪 |
| --- | --- | --- |
| 1 | 企业域 ATT&CK 有几个战术？Mobile 和 ICS 各几个？为什么三套编号不互通？ | [mitre-attack/README.md](./mitre-attack/README.md) |
| 2 | ATT&CK 的技术编号规则是什么？`T1566.001` 属于哪个技术？ | [mitre-attack/README.md 第 6 节](./mitre-attack/README.md#6-技术编号规则-txxxx-与-txxxxxxx) |
| 3 | 用 Navigator 做热力图时，二值覆盖度该怎么配渐变？ | [mitre-attack/README.md 第 7 节](./mitre-attack/README.md#7-用-attck-navigator-做覆盖度热力图) |
| 4 | "Pass the Hash" 属于哪个战术？（提示：不是凭据访问） | [mitre-attack/mapping-guide.md 示例三](./mitre-attack/mapping-guide.md#示例三内网已立足后的凭据转储--计划任务持久化--定时外泄) |
| 5 | PTES 的 7 个阶段分别是什么？哪三个阶段最容易被跳过？ | [ptes/README.md](./ptes/README.md) |
| 6 | CVSS v4.0 的 Base 指标有几个？向量字符串的固定顺序是什么？ | [ptes/templates.md 第 5.2 节](./ptes/templates.md#52-cvss-字段填写规范) |
| 7 | 授权书上最容易被忽视、却最关键的一项是什么？ | [ptes/templates.md 第 1.1 节第 2 项](./ptes/templates.md#11-必备条款) |
| 8 | `searchsploit -w` 和 `-m` 分别做什么？`-t` 为什么能降噪？ | [exploit-db/README.md 第 3.2 节](./exploit-db/README.md#32-命令行检索searchsploit) |
| 9 | exploit 与 shellcode 的本质区别是什么？ | [exploit-db/README.md 第 5 节](./exploit-db/README.md#5-exploit-与-shellcode-的区别) |
| 10 | 2025 CWE Top 25 的第 1 位是什么？它的分值是多少？ | [cwe/README.md 第 3 节](./cwe/README.md#3-2025-年-cwe-top-25-最危险软件弱点) |
| 11 | 哪个 CWE 的 KEV 计数最高？这说明了什么？ | [cwe/README.md 第 3 节](./cwe/README.md#3-2025-年-cwe-top-25-最危险软件弱点) |
| 12 | CWE-862 和 CWE-639 有什么区别？ | [cwe/audit-guide.md 第 9 节](./cwe/audit-guide.md#9-cwe-639-通过用户可控键绕过授权idor) |
| 13 | SP 800-115 里的"三类技术"是哪三类？"Planning" 是技术还是阶段？ | [nist/800-115.md 第 3 节](./nist/800-115.md#3-三类技术手法technical-assessment-techniques) |
| 14 | SP 800-115 要求评估计划回答哪五个基本问题？ | [nist/800-115.md 第 5.2 节](./nist/800-115.md#52-评估计划assessment-plan第-65-节) |
| 15 | 为什么 Review 类手法在"不能影响业务"的窗口里也能做？ | [nist/800-115.md 第 3.1 节](./nist/800-115.md#31-审查类手法review-techniques) |
| 16 | SP 800-53 和 SP 800-53A 的区别是什么？ | [nist/README.md 第 3.2 节](./nist/README.md#32-sp-800-53-rev-5--security-and-privacy-controls-for-information-systems-and-organizations) |

---

## 7. 来源 URL

本模块各子页已独立列出完整来源。以下是各标准的**官方入口**，便于你随时核对最新版本。

### OWASP

- OWASP Top 10 项目主页：<https://owasp.org/www-project-top-ten/>
- OWASP Top 10:2025 引言（十个分类）：<https://owasp.org/Top10/2025/0x00_2025-Introduction/>
- OWASP WSTG（Web Security Testing Guide）：<https://owasp.org/www-project-web-security-testing-guide/>

### MITRE ATT&CK

- ATT&CK 官网：<https://attack.mitre.org/>
- 企业矩阵：<https://attack.mitre.org/matrices/enterprise/>
- 企业战术列表（15 个）：<https://attack.mitre.org/tactics/enterprise/>
- 移动战术列表（12 个）：<https://attack.mitre.org/tactics/mobile/>
- 工控战术列表（12 个）：<https://attack.mitre.org/tactics/ics/>
- 入门指南（核心概念与用法）：<https://attack.mitre.org/resources/getting-started/>
- 版本历史：<https://attack.mitre.org/resources/versions/>
- ATT&CK Navigator：<https://mitre-attack.github.io/attack-navigator/>
- Navigator 仓库与 USAGE 文档：<https://github.com/mitre-attack/attack-navigator>

### PTES

- PTES 主页（7 个阶段）：<http://www.pentest-standard.org/index.php/Main_Page>
- 主页 Web Archive 快照（主站不可达时）：<http://web.archive.org/web/2023/http://www.pentest-standard.org/index.php/Main_Page>
- PTES Technical Guidelines：<http://www.pentest-standard.org/index.php/PTES_Technical_Guidelines>
- CVSS 官方站点：<https://www.first.org/cvss/>
- CVSS v4.0 规范：<https://www.first.org/cvss/v4.0/specification-document>
- CVSS v4.0 计算器：<https://www.first.org/cvss/calculator/4.0>

### Exploit-DB

- Exploit-DB 首页：<https://www.exploit-db.com/>
- 关于 Exploit-DB：<https://www.exploit-db.com/about-exploit-db>
- 高级检索页：<https://www.exploit-db.com/search>
- 条目示例 EDB-50592：<https://www.exploit-db.com/exploits/50592>
- Shellcode 分区：<https://www.exploit-db.com/shellcodes>
- searchsploit 官方手册：<https://www.exploit-db.com/serchsploit>
- Exploit-DB 源码仓库：<https://github.com/offensive-security/exploitdb>
- NVD（CVE 详情）：<https://nvd.nist.gov/>

### CWE

- CWE 官网：<https://cwe.mitre.org/>
- CWE Top 25 门户：<https://cwe.mitre.org/top25/>
- **2025 CWE Top 25 完整排名表**：<https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html>
- 2025 方法论：<https://cwe.mitre.org/top25/archive/2025/2025_methodology.html>
- 2025 Top 10 KEV Weaknesses：<https://cwe.mitre.org/top25/archive/2025/2025_kev_list.html>
- 2025 "On the Cusp" 列表：<https://cwe.mitre.org/top25/archive/2025/2025_onthecusp_list.html>
- CWE 数据索引：<https://cwe.mitre.org/data/index.html>
- 条目定义 URL 形式：`https://cwe.mitre.org/data/definitions/<数字>.html`

### NIST SP 800

- SP 800 系列总列表：<https://csrc.nist.gov/publications/sp800>
- SP 800-115（Technical Guide to Information Security Testing and Assessment，2008-09）：<https://csrc.nist.gov/pubs/sp/800/115/final>
- SP 800-115 官方 PDF：<https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-115.pdf>
- SP 800-53 Rev. 5（Security and Privacy Controls for Information Systems and Organizations，2020-09）：<https://csrc.nist.gov/pubs/sp/800/53/r5/final>
- SP 800-53A Rev. 5（Assessing Security and Privacy Controls，2022-01）：<https://csrc.nist.gov/pubs/sp/800/53/a/r5/final>
- SP 800-61 Rev. 3（Incident Response Recommendations and Considerations for Cybersecurity Risk Management，2025-04）：<https://csrc.nist.gov/pubs/sp/800/61/r3/final>
- SP 800-40 Rev. 4（Guide to Enterprise Patch Management Planning，2022-04）：<https://csrc.nist.gov/pubs/sp/800/40/r4/final>
- SP 800-123（Guide to General Server Security，2008-07）：<https://csrc.nist.gov/pubs/sp/800/123/final>
- SP 800-207（Zero Trust Architecture，2020-08-11）：<https://csrc.nist.gov/pubs/sp/800/207/final>
- SP 800-30 Rev. 1（Guide for Conducting Risk Assessments，2012-09）：<https://csrc.nist.gov/pubs/sp/800/30/r1/final>

---

## 8. 关于本模块的核实边界

本模块对"编号类"事实采取了统一的处理原则：**凡是编号（ATT&CK 技术 ID、CWE-ID、CVE 编号、EDB-ID、SP 800 编号与全称、OWASP 分类 ID），都必须来自实际抓取的官方页面；无法核实的，明确标注 `> ⚠️ 待核实` 并说明原因，不做编造。**

各子页末尾均列有实际来源 URL 与核实说明。如果你发现某个编号与当前官方页面不符，**以官方页面为准**——本模块的抓取日期是 **2026-09-15**，此后官方更新过的内容以官网当前状态为准。

各子页明确的待核实项汇总：

| 页面 | 待核实内容 |
| --- | --- |
| [mitre-attack/README.md](./mitre-attack/README.md) | — （战术 ID、数量、版本均已核实） |
| [mitre-attack/labs.md](./mitre-attack/labs.md) | 示例层文件中的 `versions.navigator` 与 `versions.layer` 具体版本号（建议以自己导出一次的结果为准） |
| [mitre-attack/mapping-guide.md](./mitre-attack/mapping-guide.md) | 示例中引用的部分技术页（T1003/T1059/T1105/T1190/T1204/T1213/T1505/T1550/T1552/T1021/T1053/T1039/T1041/T1560/T1071）**未逐条打开官网核对正文定义**，编号与名称取自 ATT&CK 官网通用编号体系 |
| [ptes/README.md](./ptes/README.md) | 各阶段页面的具体条目（主站不可达）；已给出各阶段官方 URL 供核对 |
| [ptes/README.md](./ptes/README.md)、[ptes/templates.md](./ptes/templates.md) | 交付物模板是教学性整理，非 PTES 官方模板 |
| [exploit-db/README.md](./exploit-db/README.md) | `EDB Verified` 的判定流程说明；Type / Platform 的完整枚举；源码安装方式 |
| [cwe/README.md](./cwe/README.md) | **CWE-770 与 OWASP Top 10:2025 的对应关系**（未在已核实的 A01/A02/A04/A05/A06/A07/A08/A10 映射清单中找到） |
| [nist/README.md](./nist/README.md) | SP 800-53B 的完整标题；SP 800-53 / 800-53A 的后续 upd 版本号 |
| [nist/README.md](./nist/README.md)、[nist/800-115.md](./nist/800-115.md) | 除 SP 800-115 外，其余文档的**内部章节结构**未逐条抓取（只描述了官方摘要层面的内容） |

---

## 9. 相关模块

本仓库还包括：

- `kali/` —— Kali Linux 工具与教程
- `linux/` —— Linux 基础、命令、内核与实践
- `kernel/` —— 内核源码相关
- `data/`、`scripts/` —— 数据与抓取脚本

（这些目录由本模块之外的协作者维护。）

---

**祝你学得扎实。记住三件事：编号不编、扫描不等于验证、威胁建模不能跳。**
