# NIST SP 800 系列导读：安全规范与评估

> 本页所有**编号、全称、发布日期、取代关系**均抓取自 NIST CSRC 官方页面
> （<https://csrc.nist.gov/publications/sp800> 及各文档详情页，抓取日期 2026-09-15）。
> 凡我未从官方页面核实的章节结构，均已标注 `> ⚠️ 待核实`，未做推测。

---

## 1. SP 800 系列是什么

**NIST** 是**美国国家标准与技术研究院**（National Institute of Standards and Technology）。**CSRC** 是其下的**计算机安全资源中心**（Computer Security Resource Center），负责发布安全相关的系列出版物。

NIST 的信息技术实验室（ITL，Information Technology Laboratory）的职责（官方原文，摘自 SP 800-115 前言）：

> ITL 开发测试方法、参考数据、概念验证实现与技术分析，以推进信息技术的开发与高效使用。其职责包括为联邦计算机系统中敏感的非密信息制定技术、物理、管理与管理的标准与指南，以实现成本有效的安全与隐私保护。**SP 800 系列报告 ITL 在计算机安全方面的研究、指南与推广工作，以及其与产业界、政府与学术界的协作活动。**

### SP 800 系列与其他系列的区分

| 系列 | 是什么 |
| --- | --- |
| **SP 800 系列** | 计算机安全与隐私的技术指南、控制目录、测试方法。**本页主题。** |
| SP 500 系列 | 信息技术（非安全）相关 |
| SP 1800 系列 | 网络安全实践指南（NCCoE 实践项目） |
| FIPS 系列 | 联邦信息处理标准，是**强制性**标准（如 FIPS 140-3 密码模块） |

### 怎么读 SP 800 系列

1. **先看状态（Status）**：`Final`（正式）/ `Draft`（草案）/ `Initial Public Draft`（初稿）。**考试、合同、合规场景一律以 Final 为准。**
2. **看取代关系（Supersedes）**：SP 800 系列更新频繁，很多老教程引用的 Revision 已经过期。**引用前必须确认是不是当前版本。**
3. **看关键词（Keywords）与主题（Topics）**：官方页面上的 Keywords 是快速定位文档用途的索引。
4. **区分"是什么"与"怎么做"**：
   - `SP 800-53` 是**控制目录**（要做什么控制）；
   - `SP 800-53A` 是**评估方法**（怎么验证控制有效）；
   - `SP 800-115` 是**技术测试方法**（怎么动手测）。
   三者常被混用，实际是"要求—验证—执行"三层。

### SP 800 系列在本模块中的位置

| 标准 | 在本模块中的角色 |
| --- | --- |
| [OWASP / WSTG](../owasp/README.md) | 具体 Web 风险的测试方法（怎么做） |
| [MITRE ATT&CK](../mitre-attack/README.md) | 对手行为建模 |
| [PTES](../ptes/README.md) | 项目流程骨架 |
| [Exploit-DB](../exploit-db/README.md) | 利用代码 |
| [CWE](../cwe/README.md) | 弱点分类 |
| **NIST SP 800** | **规范依据、控制要求、评估方法与验收标准** |

一句话：**PTES 告诉你"按什么流程走"，SP 800-115 告诉你"这个方法学是否成立、检查表该怎么搭"，SP 800-53 告诉你"应该有哪些控制"，SP 800-53A 告诉你"怎么验证控制真的有效"。**

---

## 2. 重点文档一览

下表只列出我**从官方页面核实过编号与全称**的文档。

| 编号 | 全称（English） | 中文名 | 发布 | 状态 | 取代 |
| --- | --- | --- | --- | --- | --- |
| **SP 800-115** | Technical Guide to Information Security Testing and Assessment | 信息安全测试与评估技术指南 | 2008-09 | Final | SP 800-42（2003-10-15） |
| **SP 800-53 Rev. 5** | Security and Privacy Controls for Information Systems and Organizations | 信息系统与组织的安全与隐私控制 | 2020-09 | Final | SP 800-53 Rev. 4（2015-01-22） |
| **SP 800-53A Rev. 5** | Assessing Security and Privacy Controls in Information Systems and Organizations | 评估信息系统与组织的安全与隐私控制 | 2022-01 | Final | SP 800-53A Rev. 4（2014-12-18） |
| **SP 800-53B** | （见下方待核实说明） | 控制基线 | — | Final | — |
| **SP 800-61 Rev. 3** | Incident Response Recommendations and Considerations for Cybersecurity Risk Management | 面向网络安全风险管理的安全事件响应建议与考量 | 2025-04 | Final | SP 800-61 Rev. 2 |
| **SP 800-40 Rev. 4** | Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology | 企业补丁管理规划指南：技术的预防性维护 | 2022-04 | Final | SP 800-40 Rev. 3（2013-07-22） |
| **SP 800-123** | Guide to General Server Security | 通用服务器安全指南 | 2008-07 | Final | — |
| **SP 800-207** | Zero Trust Architecture | 零信任架构 | 2020-08-11 | Final | — |
| **SP 800-207A** | A Zero Trust Architecture Model for Access Control in Cloud-Native Applications in Multi-Cloud Environments | 多云环境中云原生应用访问控制的零信任架构模型 | 2023-09-13 | Final | — |
| **SP 800-30 Rev. 1** | Guide for Conducting Risk Assessments | 风险评估实施指南 | 2012-09 | Final | SP 800-30（2002-07-01） |
| **SP 800-137** | Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations | 联邦信息系统与组织的信息安全持续监控 | 2011-09-30 | Final | — |
| **SP 800-137A** | Assessing Information Security Continuous Monitoring (ISCM) Programs: Developing an ISCM Program Assessment | 评估信息安全持续监控项目：构建 ISCM 项目评估 | 2020-05-21 | Final | — |
| **SP 800-145** | The NIST Definition of Cloud Computing | NIST 云计算定义 | 2011-09-28 | Final | — |
| **SP 800-144** | Guidelines on Security and Privacy in Public Cloud Computing | 公有云计算的安全与隐私指南 | 2011-12-09 | Final | — |
| **SP 800-146** | Cloud Computing Synopsis and Recommendations | 云计算概要与建议 | 2012-05-29 | Final | — |
| **SP 800-150** | Guide to Cyber Threat Information Sharing | 网络威胁信息共享指南 | 2016-10-04 | Final | — |
| **SP 800-215** | Guide to a Secure Enterprise Network Landscape | 安全企业网络环境指南 | 2022-11-17 | Final | — |
| **SP 800-204C** | Implementation of DevSecOps for a Microservices-based Application with Service Mesh | 面向微服务应用与服务网格的 DevSecOps 实施 | 2022-03-08 | Final | — |
| **SP 800-204D** | Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines | DevSecOps CI/CD 流水线中集成软件供应链安全的策略 | 2024-02-12 | Final | — |

> ⚠️ **待核实项**
>
> 1. **SP 800-53B**：官方 SP 800-53 Rev. 5 页面仅以 "Publication Parts" 形式链出 SP 800-53B，**其完整标题未在已抓取页面中给出**。它的作用是提供控制基线（baseline），具体全称与版本请打开 <https://csrc.nist.gov/pubs/sp/800/53/b/final> 核对。
> 2. **SP 800-53 Rev. 5 与 SP 800-61 Rev. 3 存在后续小幅更新**：官方在 SP 800-53 Rev. 5 页面上给了 "errata update"（2020-12-10）与 `SP 800-53 Rev. 5 (upd1)` 链接；SP 800-53A 页面显示 2025-08-27 发布了 Release 5.2.0（新增 SA-15(13)、SA-24、SI-02(07) 三条评估程序）。**引用版本号时请以官网当前指向的 upd 版本为准。**
> 3. 上表的**发布日期**取自各文档详情页的 "Date Published" 字段或列表页中标题块后的日期。NIST 列表页的日期与条目的对应关系在 HTML 抽取时容易错位，因此我只收录了前缀日期与标题后日期**一致**的条目；不一致的（如 SP 800-146）以标题后日期为准。

---

## 3. 逐篇导读

### 3.1 SP 800-115 — Technical Guide to Information Security Testing and Assessment

| 项 | 内容 |
| --- | --- |
| 编号 | SP 800-115 |
| 全称 | Technical Guide to Information Security Testing and Assessment |
| 中文 | 信息安全测试与评估技术指南 |
| 发布 | 2008 年 9 月 |
| 取代 | SP 800-42（2003-10-15） |
| 作者 | Karen Scarfone（NIST）、Murugiah Souppaya（NIST）、Amanda Cody（BAH）、Angela Orebaugh（BAH） |
| 官方入口 | <https://csrc.nist.gov/pubs/sp/800/115/final> |
| DOI | 10.6028/NIST.SP.800-115 |
| 页数 | 80 页（官方标注 "Spec. Publ. 800-115, 80 pages (Sep. 2008)"） |

**解决什么问题**（官方摘要要点）

- 帮助组织**规划并实施**技术的安全测试与检查（test and examination）；
- 分析发现并制定缓解策略；
- 提供设计与维护测试与检查流程的实务建议；
- 用途包括：发现系统或网络中的漏洞、**验证是否符合政策或其他要求**；
- **官方特别声明**：本指南**不打算呈现一个完整的安全测试与检查项目**，而是提供关键技术要素的概览，重点在具体技术手法、每种手法的**优点与局限**，以及使用建议。

**核心内容**（章节结构来自官方 PDF 目录，已逐条核实）

| 章节 | 标题 |
| --- | --- |
| 1 | Introduction（Authority / Purpose and Scope / Audience / Document Structure） |
| 2 | Security Testing and Examination Overview（Assessment Methodology、Technical Assessment Techniques、Comparing Tests and Examinations、Testing Viewpoints：External/Internal、Overt/Covert） |
| 3 | **Review Techniques**（Documentation Review、Log Review、Ruleset Review、System Configuration Review、Network Sniffing、File Integrity Checking） |
| 4 | **Target Identification and Analysis Techniques**（Network Discovery、Network Port and Service Identification、Vulnerability Scanning、Wireless Scanning：Passive/Active/Device Location Tracking/Bluetooth） |
| 5 | **Target Vulnerability Validation Techniques**（Password Cracking、Penetration Testing、Social Engineering） |
| 6 | **Security Assessment Planning**（Assessment Policy、Prioritizing and Scheduling、Selecting and Customizing Techniques、Assessment Logistics、Assessment Plan Development、Legal Considerations） |
| 7 | Security Assessment Execution（Coordination、Assessing、Analysis、Data Handling：Collection/Storage/Transmission/Destruction） |
| 8 | Post-Testing Activities（Mitigation Recommendations、Reporting、Remediation/Mitigation） |

**附录**：A—Live CD Distributions for Security Testing；**B—Rules of Engagement Template**；C—Application Security Testing and Examination；D—Remote Access Testing；E—Resources；F—Glossary；G—Acronyms and Abbreviations。

**对渗透工作的实际用途**

- **附录 B 的 Rules of Engagement Template 可以直接拿来补强 PTES 前期交互阶段的 RoE。** 这是官方提供的、可直接套用的模板，比自己编更省事也更有说服力。
- 第 3～5 章的三类技术（Review / Target Identification / Target Vulnerability Validation）是一份**完整性检查表**：用它检查"我这轮测试是不是漏掉了某一类手法"。
- 第 6 章的 Assessment Logistics、Assessor Selection and Skills、Assessment Plan Development 是**项目规划**的官方依据。
- 第 7 章的 Data Handling 四个环节（收集/存储/传输/销毁）是**数据处理条款**的依据，可直接引用到授权书里。
- 第 2 章的 Testing Viewpoints（External/Internal、Overt/Covert）提供了一个**测试视角分类**，比笼统地说"黑盒/白盒"更严谨。

**专篇**：[800-115.md](./800-115.md)

---

### 3.2 SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations

| 项 | 内容 |
| --- | --- |
| 编号 | SP 800-53 Rev. 5 |
| 全称 | Security and Privacy Controls for Information Systems and Organizations |
| 中文 | 信息系统与组织的安全与隐私控制 |
| 发布 | 2020 年 9 月 |
| 取代 | SP 800-53 Rev. 4（2015-01-22） |
| 作者 | Joint Task Force（联合工作组） |
| 官方入口 | <https://csrc.nist.gov/pubs/sp/800/53/r5/final> |
| 勘误 | 官方标注 2020-12-10 发布 errata update；另有 upl1 版本 |

**解决什么问题**（官方摘要要点）

- 提供**安全与隐私控制的目录（catalog）**，用于保护组织的运营与资产、个人、其他组织及国家，抵御来自敌对攻击、人为错误、自然灾害、结构性失效、外国情报实体以及隐私风险等多样的威胁与风险；
- 控制是**灵活、可定制**的，作为组织级风险管理流程的一部分实施；
- 控制项来自使命与业务需求、法律、行政命令、指令、法规、政策、标准与指南；
- **同时覆盖"功能性"（功能与机制有多强）与"保障性"（对控制所提供的安全/隐私能力有多大信心）两个视角**——官方明确说明，兼顾二者才能确保 IT 产品及其支撑系统足够可信。

**核心结构：20 个控制族（Control Families）**

以下控制族名称直接抓取自官方页面（按官方列表顺序）：

| 英文 | 中文 |
| --- | --- |
| Access Control | 访问控制 |
| Awareness and Training | 意识与培训 |
| Audit and Accountability | 审计与可追溯性 |
| Assessment, Authorization and Monitoring | 评估、授权与监控 |
| Configuration Management | 配置管理 |
| Contingency Planning | 应急规划 |
| Identification and Authentication | 标识与认证 |
| Incident Response | 事件响应 |
| Maintenance | 维护 |
| Media Protection | 介质保护 |
| Physical and Environmental Protection | 物理与环境防护 |
| Planning | 规划 |
| Program Management | 项目管理 |
| Personnel Security | 人员安全 |
| PII Processing and Transparency | 个人身份信息处理与透明性 |
| Risk Assessment | 风险评估 |
| System and Services Acquisition | 系统与服务采购 |
| System and Communications Protection | 系统与通信保护 |
| System and Information Integrity | 系统与信息完整性 |
| Supply Chain Risk Management | 供应链风险管理 |

**对渗透工作的实际用途**

- **把渗透发现映射到控制项编号。** 客户是联邦或受监管行业时，报告里写"发现对应 AC-3 访问控制执行、IA-5 认证器管理未落实"，比只写技术细节更能推动整改——因为对方的整改排期就是按控制项走的。
- **用控制族做覆盖度检查。** 一轮测试如果不涉及人员安全（PS）、物理与环境（PE）、应急规划（CP），要在报告的限制章节说明，避免客户误以为"报告里没有的就是安全的"。
- **注意受众差异**：SP 800-53 是"控制目录"，不是测试方法。**不要拿它当测试清单用**——测试方法用 SP 800-115，评估方法用 SP 800-53A。

**配套文档**

- **SP 800-53A Rev. 5 — Assessing Security and Privacy Controls in Information Systems and Organizations**（评估方法与评估程序），2022-01，取代 Rev. 4。官方摘要：提供**方法学与评估程序**，用于在有效的风险管理框架内评估系统与组织所采用的安全与隐私控制；评估程序在系统开发生命周期的各阶段执行，与 SP 800-53 Rev. 5 的控制项一致；程序**可定制**，可根据组织的风险容忍度裁剪，并提供了构建评估计划与分析评估结果的指南。关键词中包含 **OSCAL**（Open Security Controls Assessment Language，开放安全控制评估语言）。入口：<https://csrc.nist.gov/pubs/sp/800/53/a/r5/final>
- **SP 800-53B**（控制基线，作为 SP 800-53 Rev. 5 的 "Publication Parts"）⚠️ 全称待核实，见上表说明。

---

### 3.3 SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management

| 项 | 内容 |
| --- | --- |
| 编号 | SP 800-61 Rev. 3 |
| 全称 | Incident Response Recommendations and Considerations for Cybersecurity Risk Management |
| 中文 | 面向网络安全风险管理的安全事件响应建议与考量 |
| 发布 | 2025 年 4 月 |
| 取代 | 取代 SP 800-61 Rev. 2 |
| 官方入口 | <https://csrc.nist.gov/pubs/sp/800/61/r3/final> |
| 官方 PDF | <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf> |

**解决什么问题**

官方摘要：本出版物旨在协助组织把**网络安全事件响应（incident response）**的建议与考量**融入网络安全风险管理**之中。

**这一版最重要的变化**

从标题就能看出来：Rev. 2 的标题是 "Computer Security Incident Handling Guide"（计算机安全事件处理指南），而 **Rev. 3 把"事件响应"重新定位为"网络安全风险管理"的一部分**。这不是改个名字，而是**视角的转变**：事件响应不再是一个孤立的应急流程，而是与风险管理、治理、持续改进打通。

> ⚠️ 待核实：本页未逐条核实 Rev. 3 的章节结构。**它的具体阶段划分与章节标题请打开官方 PDF 目录核对**，不要在报告中引用未经核实的"阶段名称"。

**对渗透工作的实际用途**

- **渗透测试的"停手条件"与通报义务，本质上是事件响应流程的一部分。** 在 [PTES 授权书](../ptes/templates.md#12-授权书正文骨架) 里写的"发现真实入侵痕迹立即停手并通报"，落地时对的就是客户的事件响应流程。写 RoE 时**应该索取客户的事件响应联系人清单与分级标准**。
- **报告里的"检测与响应能力评估"章节**可以引用本文档作为方法论依据。
- **给防守方的价值**：渗透测试中"多久被发现"（time to detect）是核心指标之一，这与事件响应能力直接相关。把这个数据交给客户，比只给漏洞列表有用得多。

---

### 3.4 SP 800-40 Rev. 4 — Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology

| 项 | 内容 |
| --- | --- |
| 编号 | SP 800-40 Rev. 4 |
| 全称 | Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology |
| 中文 | 企业补丁管理规划指南：技术的预防性维护 |
| 发布 | 2022 年 4 月 |
| 取代 | SP 800-40 Rev. 3（2013-07-22） |
| 作者 | Murugiah Souppaya（NIST）、Karen Scarfone（Scarfone Cybersecurity） |
| 官方入口 | <https://csrc.nist.gov/pubs/sp/800/40/r4/final> |
| DOI | 10.6028/NIST.SP.800-40r4 |

**解决什么问题**（官方摘要要点）

- **企业补丁管理**的定义：在整个组织内**识别、排优先级、获取、安装并验证**补丁、更新与升级的过程；
- 官方指出实践中存在一个张力：**业务/使命负责人与安全/技术管理者之间对补丁的价值存在分歧**；
- 本文档把补丁定位为**计算技术预防性维护的关键组成部分**——是"做生意的成本"，是组织达成使命必须做的事；
- 讨论影响企业补丁管理的常见因素，并建议**建立企业级策略**，以简化并落地补丁工作，同时降低风险；
- 结论：通过企业补丁管理实现预防性维护，有助于**防止入侵、数据泄露、运营中断及其他不利事件**。

**对渗透工作的实际用途**

- **渗透报告里最高频的修复建议就是"打补丁"。** 本文档给了这个建议的**方法论支撑**：不是"升级一下"，而是"识别 → 排优先级 → 获取 → 安装 → 验证"五步，且要有企业级策略。
- **帮你写出可执行的建议**。例如不要写"及时打补丁"，而是写："将 CVE-XXXX 纳入本月补丁周期，在预生产验证后于变更窗口部署，并通过配置核查脚本验证安装结果（依据 SP 800-40 Rev. 4 的识别—排优先级—获取—安装—验证流程）"。
- **"排优先级"这一环是价值最高的**。客户补丁永远打不完，报告应给出**排序依据**：是否有公开 EXP（查 [Exploit-DB](../exploit-db/README.md)）、是否在 KEV 目录（在野利用）、是否为 [CWE Top 25](../cwe/README.md) 中命中率高的弱点类、是否暴露在公网。这四条组合起来，就是一份可落地的补丁优先级建议。
- **注意文档主题关联**：官方页面把本文档与**行政命令 14028**（Executive Order 14028，改善国家网络安全）关联，说明补丁管理在监管语境下的重要性在提升。

---

### 3.5 SP 800-123 — Guide to General Server Security

| 项 | 内容 |
| --- | --- |
| 编号 | SP 800-123 |
| 全称 | Guide to General Server Security |
| 中文 | 通用服务器安全指南 |
| 发布 | 2008 年 7 月 |
| 作者 | Karen Scarfone（NIST）、Wayne Jansen（NIST）、Miles Tracy（Federal Reserve Information Technology） |
| 官方入口 | <https://csrc.nist.gov/pubs/sp/800/123/final> |
| DOI | 10.6028/NIST.SP.800-123 |
| 关联法规 | OMB Circular A-130 |

**解决什么问题**（官方摘要要点）

- 帮助组织理解**为通过网络通信提供服务（服务器的主要功能）而进行安全加固与维护时，所执行的基础性活动**；
- 讨论为什么需要保护服务器；
- 为**选择、实施与维护必要的安全控制**提供建议。

**覆盖的控制族**（官方页面列出）：Access Control、Audit and Accountability、Configuration Management、Identification and Authentication、Incident Response、Maintenance、Physical and Environmental Protection、Planning、System and Communications Protection、System and Information Integrity。

**对渗透工作的实际用途**

- **主机加固类发现的整改依据。** 当你发现"SSH 允许密码登录且 root 可直连"、"Web 目录存在备份文件"、"服务器未做最小化安装"时，引用本文档比引用通用安全常识更有分量。
- **对应用安全配置的交叉引用**：OWASP 的 `A02:2025 Security Misconfiguration`（安全配置错误）页面在参考列表中直接引用了本文档（标题为 "NIST Guide to General Server Hardening"）。**这是两个体系打通的直接证据**——Web 应用的配置类问题可以同时引用 OWASP 分类与 SP 800-123。
- **注意时效**：本文档发布于 2008 年，**部分具体技术建议（如特定协议版本、特定工具）已过时**。引用时取其**方法论与检查维度**，具体技术参数请对照当前版本的厂商加固基线（如 CIS Benchmarks）。

---

### 3.6 SP 800-207 — Zero Trust Architecture

| 项 | 内容 |
| --- | --- |
| 编号 | SP 800-207 |
| 全称 | Zero Trust Architecture |
| 中文 | 零信任架构 |
| 发布 | 2020-08-11 |
| 官方入口 | <https://csrc.nist.gov/pubs/sp/800/207/final> |

**配套文档**：**SP 800-207A — A Zero Trust Architecture Model for Access Control in Cloud-Native Applications in Multi-Cloud Environments**（多云环境中云原生应用访问控制的零信任架构模型），2023-09-13。入口：<https://csrc.nist.gov/pubs/sp/800/207/a/final>

**解决什么问题**

SP 800-207 给出了**零信任架构（Zero Trust Architecture, ZTA）**的官方定义与参考模型，核心思想是**不再以"网络位置"作为信任依据**——不因为请求来自内网就自动信任，每次访问都要基于身份、设备、上下文等做**动态授权决策**。

> ⚠️ 待核实：本页未逐条核实 SP 800-207 的章节结构与它给出的组件名称（如策略引擎、策略执行点等具体术语的中文译法与官方措辞）。**引用具体组件名与流程时请打开官方 PDF 核对。**

**对渗透工作的实际用途**

- **改变内网渗透的叙事方式。** 在零信任模型下，"我打进了内网"不再是终局——**攻击者仍需在每个资源访问点重新通过授权决策**。所以渗透报告里"横向移动到 XX 台主机"的价值判断会变：要说明**这些访问在零信任下会不会被拦、靠什么拦**。
- **为"内网可信假设"类发现定级。** 当你发现某个内网服务完全依赖 IP 白名单做认证（对应 [CWE](../cwe/README.md) 中的"依赖 IP 地址进行认证"类弱点），可以引用 ZTA 原则说明这个设计在架构层面就不成立，而不只是"配置问题"。
- **给客户的架构整改建议有了官方依据**。从"建议做微隔离"升级为"建议按 SP 800-207 的 ZTA 模型重构访问决策路径"。
- **云原生场景用 800-207A**：如果客户是多云 / 云原生架构，讨论容器与服务网格间的访问控制时，800-207A 比 800-207 更对口。

---

### 3.7 其他值得知道的文档

| 编号 | 全称 | 中文 | 发布 | 一句话用途 |
| --- | --- | --- | --- | --- |
| **SP 800-30 Rev. 1** | Guide for Conducting Risk Assessments | 风险评估实施指南 | 2012-09 | 风险评估的官方方法学（取代 2002 年原版），用于把技术发现转成组织风险语言 |
| **SP 800-137** | Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations | 联邦信息系统与组织的信息安全持续监控 | 2011-09-30 | 持续监控（ISCM）的框架；渗透测试的"时点快照"与持续监控是互补关系 |
| **SP 800-137A** | Assessing Information Security Continuous Monitoring (ISCM) Programs: Developing an ISCM Program Assessment | 评估信息安全持续监控项目 | 2020-05-21 | 怎么评估 ISCM 项目本身做得好不好 |
| **SP 800-145** | The NIST Definition of Cloud Computing | NIST 云计算定义 | 2011-09-28 | 云计算的权威定义；讨论云环境测试范围与责任边界时的共同语言 |
| **SP 800-144** | Guidelines on Security and Privacy in Public Cloud Computing | 公有云计算的安全与隐私指南 | 2011-12-09 | 公有云场景的安全与隐私考量 |
| **SP 800-146** | Cloud Computing Synopsis and Recommendations | 云计算概要与建议 | 2012-05-29 | 云计算的采用建议；与 800-144/145 配套 |
| **SP 800-150** | Guide to Cyber Threat Information Sharing | 网络威胁信息共享指南 | 2016-10-04 | 威胁情报共享；红蓝对抗的产物如何沉淀成可共享情报 |
| **SP 800-215** | Guide to a Secure Enterprise Network Landscape | 安全企业网络环境指南 | 2022-11-17 | 企业网络架构安全；讨论网络分段与边界演进的依据 |
| **SP 800-204C** | Implementation of DevSecOps for a Microservices-based Application with Service Mesh | 面向微服务应用与服务网格的 DevSecOps 实施 | 2022-03-08 | 微服务 + 服务网格下的安全实施 |
| **SP 800-204D** | Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines | DevSecOps CI/CD 流水线中集成软件供应链安全的策略 | 2024-02-12 | **软件供应链安全**，对应 OWASP `A03:2025 Software Supply Chain Failures` |

**SP 800-30 Rev. 1 补充说明**（官方摘要要点）：为联邦信息系统与组织提供**风险评估**指南，是对 SP 800-39 指南的细化；风险评估在风险管理层级的所有三个层级上开展，是整个风险管理流程的一部分，为高层领导/管理者提供**决定适当行动方案所需的信息**。关键词：成本效益分析、剩余风险、风险、风险评估、风险管理、风险缓解、安全控制、威胁与脆弱性。

---

## 4. 怎么把 SP 800 用进日常工作

| 场景 | 用哪篇 | 怎么用 |
| --- | --- | --- |
| 设计一次安全评估方案 | **SP 800-115** 第 6 章 | 套用它的评估规划结构：政策 → 优先级与排期 → 技术选择 → 后勤 → 计划编写 → 法律考量 |
| 检查这轮测试手法是否完整 | **SP 800-115** 第 3～5 章 | 用四类技术（Review / Target Identification / Target Vulnerability Validation / Planning）做完整性核对 |
| 写规则约定（RoE） | **SP 800-115** 附录 B | 官方提供的 RoE 模板，直接补强 PTES 的前期交互文档 |
| 约定数据处理与销毁 | **SP 800-115** 第 7.4 节 | 数据收集/存储/传输/销毁四个环节逐一约定，写进授权书 |
| 把发现映射到控制项 | **SP 800-53 Rev. 5** 的 20 个控制族 | 让监管行业客户按控制项排整改计划 |
| 验证控制是否有效 | **SP 800-53A Rev. 5** | 用官方评估程序，而不是自己编检查表 |
| 设计事件响应与停手条件 | **SP 800-61 Rev. 3** | 索取客户的事件响应分级与联系人清单，写进 RoE |
| 写补丁类修复建议 | **SP 800-40 Rev. 4** | 按"识别—排优先级—获取—安装—验证"五步写，并给出排序依据 |
| 主机加固类发现 | **SP 800-123** | 取其检查维度；具体参数对照当前加固基线 |
| 架构级整改建议 | **SP 800-207** / **SP 800-207A** | 从"配置问题"升级为"架构假设不成立" |
| 把技术发现转成组织风险 | **SP 800-30 Rev. 1** | 风险评估的官方语言与流程 |
| 供应链类发现 | **SP 800-204D** | 对应 OWASP A03:2025 |

---

## 5. 三个最容易踩的坑

1. **把 SP 800-53 当测试清单用。** 它是**控制目录**（要求），不是测试方法。拿它做测试清单，会出现大量无法执行、无法观察、无法取证的条目。测试方法用 SP 800-115。
2. **引用过期的 Revision。** SP 800-53 已经到 Rev. 5，SP 800-61 已经到 Rev. 3，SP 800-40 已经到 Rev. 4。网上大量资料仍在引用 Rev. 2 / Rev. 3 / Rev. 4 的旧结构。**引用前必须打开官网确认当前版本。**
3. **把草案当正式标准引用。** 列表页中大量条目是 `Draft` 或 `Initial Public Draft` 状态，会随意见征集变化。合规、合同、考试场景一律以 `Final` 为准。

---

## 6. 延伸阅读

- [800-115.md](./800-115.md)：SP 800-115 专篇（四类技术、测试前/中/后方法论、与 PTES 的异同、检查表结构借用）
- [labs.md](./labs.md)：练习——按 SP 800-115 的结构为一个内部系统设计一次安全评估方案
- [../ptes/README.md](../ptes/README.md)：流程骨架（与 SP 800-115 互补）
- [../cwe/README.md](../cwe/README.md)：弱点分类（用于把技术发现上升为可治理的弱点类）
- [../mitre-attack/README.md](../mitre-attack/README.md)：对手行为建模（与 SP 800-53 的控制项可交叉引用）
- 上级总纲：[../README.md](../README.md)

## 7. 来源 URL

**NIST CSRC 官方**

- SP 800 系列出版物总列表：<https://csrc.nist.gov/publications/sp800>
- **SP 800-115**（Technical Guide to Information Security Testing and Assessment，2008-09，取代 SP 800-42）：<https://csrc.nist.gov/pubs/sp/800/115/final>
  - 官方 PDF（本页第 3.1 节章节结构即抓取自该 PDF 目录）：<https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-115.pdf>
- **SP 800-53 Rev. 5**（Security and Privacy Controls for Information Systems and Organizations，2020-09，20 个控制族即抓取自该页）：<https://csrc.nist.gov/pubs/sp/800/53/r5/final>
- **SP 800-53A Rev. 5**（Assessing Security and Privacy Controls in Information Systems and Organizations，2022-01）：<https://csrc.nist.gov/pubs/sp/800/53/a/r5/final>
- **SP 800-53B**（控制基线）：<https://csrc.nist.gov/pubs/sp/800/53/b/final>
- **SP 800-61 Rev. 3**（Incident Response Recommendations and Considerations for Cybersecurity Risk Management，2025-04）：<https://csrc.nist.gov/pubs/sp/800/61/r3/final>
  - 官方 PDF：<https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf>
- **SP 800-40 Rev. 4**（Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology，2022-04）：<https://csrc.nist.gov/pubs/sp/800/40/r4/final>
- **SP 800-123**（Guide to General Server Security，2008-07）：<https://csrc.nist.gov/pubs/sp/800/123/final>
- **SP 800-207**（Zero Trust Architecture，2020-08-11）：<https://csrc.nist.gov/pubs/sp/800/207/final>
- **SP 800-207A**（多云云原生零信任访问控制模型，2023-09-13）：<https://csrc.nist.gov/pubs/sp/800/207/a/final>
- **SP 800-30 Rev. 1**（Guide for Conducting Risk Assessments，2012-09）：<https://csrc.nist.gov/pubs/sp/800/30/r1/final>

**交叉引用的其他体系文档**

- OWASP A02:2025 Security Misconfiguration（其参考列表引用 SP 800-123）：<https://owasp.org/Top10/2025/A02_2025-Security_Misconfiguration/>
- OWASP A03:2025 Software Supply Chain Failures（与 SP 800-204D 对应）：<https://owasp.org/Top10/2025/A03_2025-Software_Supply_Chain_Failures/>
- CVSS 官方（用于风险评级）：<https://www.first.org/cvss/>

> ⚠️ **本页的核实边界（请务必读过）**
>
> 1. **已逐条核实**：上表所有文档的**编号、完整标题、发布日期、取代关系**均来自 NIST CSRC 官方页面（SP 800-115 的章节结构来自官方 PDF 目录；SP 800-53 Rev. 5 的 20 个控制族来自官方详情页）。
> 2. **未逐条核实**：除 SP 800-115 外，其余文档的**章节标题与内部结构**我未从官方 PDF 逐条抓取，因此本页对这些文档只描述"解决什么问题"（基于官方摘要）与"用途"，**没有编造章节名**。需要引用具体章节时，请打开对应的官方 PDF 核对目录。
> 3. **SP 800-61 Rev. 3、SP 800-207、SP 800-30 Rev. 1** 的**内部阶段/组件名称**（如事件响应的阶段划分、ZTA 的组件名）本页**未给出**，因为未核实。请以官方 PDF 为准。
> 4. **本页的"对渗透工作的实际用途"部分是我基于文档摘要与行业实践给出的应用建议**，不是 NIST 官方原文，请勿当作官方要求引用。
