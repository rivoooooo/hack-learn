# CWE 通用弱点枚举：给缺陷"分门别类"

> 本页 Top 25 排名、分数、CWE 名称、KEV 计数均抓取自 **2025 版** CWE Top 25 官方列表
> （<https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html>，抓取日期 2026-09-15）。
> OWASP 对应关系抓取自 OWASP Top 10:2025 各分类的 "List of Mapped CWEs" 官方文档。

---

## 1. CWE 是什么

CWE（Common Weakness Enumeration，通用弱点枚举）是 MITRE 维护的**软件与硬件弱点类型字典**。它给"这一类代码/设计缺陷"分配一个稳定编号和名称。

CWE 关注的是**类型（type）**，不是**实例（instance）**。这是理解它的关键。

### 举个例子说清

假设某公司的 CMS 在 2026 年 3 月被发现登录框可以注入 SQL：

| 体系 | 回答的问题 | 该例中的值 |
| --- | --- | --- |
| **CWE** | 这属于**哪一类**缺陷？ | `CWE-89` Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') |
| **CVE** | 这是**哪一个具体**漏洞实例？ | 例如 `CVE-2026-XXXXX`（分配给该 CMS 该版本的具体漏洞） |
| **Exploit-DB** | 有没有**能跑的利用代码**？ | 例如 `EDB-ID yyyyy`（若已有公开 PoC） |
| **CVSS** | 这个实例**有多严重**？ | 例如 `CVSS:4.0/...` 与基础分 |
| **[ATT&CK](../mitre-attack/README.md)** | 利用它属于**什么攻击行为**？ | 例如 `T1190` Exploit Public-Facing Application |

**一句话**：**CWE 是类型，CVE 是实例。** 一个 CWE 可以对应成千上万个 CVE。

### 为什么要用 CWE

- **修复一个 CWE，消灭一整类 CVE。** 修掉一处 SQL 注入只是修了一个 CVE；把 SQL 注入这类弱点从编码规范里根除，未来同类 CVE 就不会产生。这就是 CWE 对 SDLC（软件开发生命周期）最大的价值。
- **让不同工具、不同团队说同一种话。** SAST 工具、代码审计报告、渗透报告、采购要求、漏洞管理平台都用 CWE 编号对接，避免"你说的注入和我说的注入不是一回事"。
- **支撑安全需求与验收。** 可以把"CWE Top 25 中的 X 条必须在设计阶段消除"写进开发规范与合同验收条款。

---

## 2. 编号体系

- **编号形式**：`CWE-<数字>`，例如 `CWE-79`、`CWE-89`、`CWE-918`。
- **查看定义**：统一 URL 形式 `https://cwe.mitre.org/data/definitions/<数字>.html`，例如 <https://cwe.mitre.org/data/definitions/89.html>。
- **编号永久稳定**，改名不改号；被废弃的条目会标记为 Deprecated/Prohibited 但编号保留（例如 `CWE-320 Key Management Errors (Prohibited)`）。
- **条目之间是图结构，不是平铺列表**。核心关系：
  - **ChildOf / ParentOf**：父子关系，构成层级（如 `CWE-77` Command Injection 是 `CWE-78` OS Command Injection 的父类）。
  - **PeerOf**：同级关系。
  - **CanPrecede / CanFollow**：可能的前后因果链（例如"整数溢出"可以导致"缓冲区溢出"）。
  - **CanAlsoBe**：视角差异。
- **有"视角（View）"的概念**。同一个弱点在不同视角下有不同组织方式，常见的有按研究概念的视角、按开发概念的视角等。**做代码审计时用"按开发概念"的视角更实用**，因为它贴近代码结构。
- 官方完整数据索引：<https://cwe.mitre.org/data/index.html>

### CWE 与 CVE 的关系

- **CVE 记录会关联 CWE**（NVD 的每条 CVE 上通常有 `Weakness Enumeration` 字段），但**这个关联常常不完整或不精确**——历史上大量 CVE 的 CWE 字段为空或写作 "NVD-CWE-noinfo"。
- **不要反向推断**："CWE-89 的 CVE 很多"不代表 CWE-89 最危险（因为不同类别被标注的完整度不同）。CWE Top 25 的分值算法本身就是为了修正这类偏差。
- **两者不能互相替代**：CWE 用于"防未来"，CVE 用于"管现在"。

---

## 3. 2025 年 CWE Top 25 最危险软件弱点

**年份：2025**。数据集覆盖 **39,080** 条 CVE 记录（来源：<https://cwe.mitre.org/top25/>）。

评分方式：把每个 CWE 关联的 CVE 数量与 CVSS 可利用性/影响分数综合计算出一个分值（Score）。`CVEs in KEV` 列是该 CWE 下被收录进 [CISA KEV 目录](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)（Known Exploited Vulnerabilities，已知被利用漏洞）的 CVE 数量——**这一列非常值得看清**：它表示"真正被在野利用过"的数量。

| 排名 | CWE-ID | 官方名称（English） | 中文说明 | 典型后果 | 分值 | KEV | 名次变化 | OWASP Top 10:2025 归属 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CWE-79 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') | 网页生成时未正确中性化输入（跨站脚本 XSS） | 会话劫持、冒充用户、窃取敏感页面数据 | 60.38 | 7 | 0 | **A05 Injection** |
| 2 | CWE-89 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') | SQL 命令中特殊元素未正确中性化（SQL 注入） | 数据库全量读取/篡改/删除、常升级为 RCE | 28.72 | 4 | +1 | **A05 Injection** |
| 3 | CWE-352 | Cross-Site Request Forgery (CSRF) | 跨站请求伪造 | 以受害者身份执行未授权操作（转账、改密） | 13.64 | 0 | +1 | **A01 Broken Access Control** |
| 4 | CWE-862 | Missing Authorization | 缺失授权 | 任意用户访问本无权访问的功能或数据 | 13.28 | 0 | +5 | **A01 Broken Access Control** |
| 5 | CWE-787 | Out-of-bounds Write | 越界写 | 内存破坏、任意代码执行、崩溃 | 12.68 | **12** | -3 | 内存安全类，Top 10 未单列 |
| 6 | CWE-22 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') | 路径名未限制在受限目录内（路径穿越） | 读写任意文件、泄露配置与凭据、覆盖文件 | 8.99 | 10 | -1 | **A01 Broken Access Control** |
| 7 | CWE-416 | Use After Free | 释放后使用 | 内存破坏、UAF 型 RCE（浏览器/内核常见） | 8.47 | **14** | +1 | 内存安全类，Top 10 未单列 |
| 8 | CWE-125 | Out-of-bounds Read | 越界读 | 内存信息泄露（可绕过 ASLR）、崩溃 | 7.88 | 3 | -2 | 内存安全类，Top 10 未单列 |
| 9 | CWE-78 | Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') | OS 命令中特殊元素未正确中性化（OS 命令注入） | 以服务进程权限执行任意系统命令 | 7.85 | **20** | -2 | **A05 Injection** |
| 10 | CWE-94 | Improper Control of Generation of Code ('Code Injection') | 代码生成控制不当（代码注入） | 任意代码执行；常出现在模板引擎、动态求值 | 7.57 | 7 | +1 | **A05 Injection** |
| 11 | CWE-120 | Buffer Copy without Checking Size of Input ('Classic Buffer Overflow') | 未检查输入长度的缓冲区复制（经典缓冲区溢出） | 内存破坏、栈上代码执行、崩溃 | 6.96 | 0 | 新入榜 | 内存安全类，Top 10 未单列 |
| 12 | CWE-434 | Unrestricted Upload of File with Dangerous Type | 未限制上传危险类型文件 | 上传 Web Shell 直接获得服务器权限 | 6.87 | 4 | -2 | **A06 Insecure Design** |
| 13 | CWE-476 | NULL Pointer Dereference | 空指针解引用 | 崩溃（DoS）；在特定场景下可被利用 | 6.41 | 0 | **+8** | **A10 Mishandling of Exceptional Conditions** |
| 14 | CWE-121 | Stack-based Buffer Overflow | 栈缓冲区溢出 | 覆盖返回地址劫持控制流 | 5.75 | 4 | 新入榜 | 内存安全类，Top 10 未单列 |
| 15 | CWE-502 | Deserialization of Untrusted Data | 反序列化不可信数据 | 直接 RCE（Java/Python/PHP 反序列化链） | 5.23 | 11 | +1 | **A08 Software or Data Integrity Failures** |
| 16 | CWE-122 | Heap-based Buffer Overflow | 堆缓冲区溢出 | 堆元数据破坏、可控写、RCE | 5.21 | 6 | 新入榜 | 内存安全类，Top 10 未单列 |
| 17 | CWE-863 | Incorrect Authorization | 授权不正确 | 越权（水平/垂直），访问他人资源或管理功能 | 4.14 | 4 | +1 | **A01 Broken Access Control** |
| 18 | CWE-20 | Improper Input Validation | 输入校验不当 | 各类注入与逻辑绕过的上游根因 | 4.09 | 2 | **-6** | **A05 Injection** |
| 19 | CWE-284 | Improper Access Control | 访问控制不当 | 未授权访问各类资源 | 4.07 | 1 | 新入榜 | **A01 Broken Access Control** |
| 20 | CWE-200 | Exposure of Sensitive Information to an Unauthorized Actor | 向未授权主体暴露敏感信息 | 个人信息/凭据/内部信息泄露 | 4.01 | 1 | -3 | **A01 Broken Access Control** |
| 21 | CWE-306 | Missing Authentication for Critical Function | 关键功能缺失认证 | 未认证即可调用敏感功能（如改配置、执行任务） | 3.47 | 11 | +4 | **A07 Authentication Failures** |
| 22 | CWE-918 | Server-Side Request Forgery (SSRF) | 服务端请求伪造 | 探测内网、读取云元数据凭据、绕过网络边界 | 3.36 | 0 | -3 | **A01 Broken Access Control**（2025 起 SSRF 并入 A01） |
| 23 | CWE-77 | Improper Neutralization of Special Elements used in a Command ('Command Injection') | 命令中特殊元素未正确中性化（命令注入） | 执行非预期命令（含 OS 命令、程序参数） | 3.15 | 2 | **-10** | **A05 Injection** |
| 24 | CWE-639 | Authorization Bypass Through User-Controlled Key | 通过用户可控键绕过授权 | IDOR：改 ID 即可读写他人数据 | 2.62 | 0 | **+6** | **A01 Broken Access Control** |
| 25 | CWE-770 | Allocation of Resources Without Limits or Throttling | 资源分配无限制或限流 | 资源耗尽型 DoS、云账单失控 | 2.54 | 0 | +1 | ⚠️ 见下方说明 |

### 几个必须看出来的趋势

1. **XSS 与 SQL 注入的分数差距极大（60.38 vs 28.72）**，XSS 几乎是第二名的两倍。这与 OWASP 的判断一致：注入类里 XSS 是"高频低危"，SQL 注入是"低频高危"。
2. **KEV 计数与排名并不一致。** CWE-78 OS 命令注入的 KEV 有 **20** 条，为全表最高，但只排第 9；CWE-416 Use After Free 的 KEV 有 **14** 条，排第 7。**这提示：排名反映"普遍性与影响面"，KEV 反映"实际被在野利用"。做优先级排序时两者都要看。**
3. **内存安全类占了 6 席**（CWE-787、416、125、120、121、122）。OWASP Top 10 是 Web 应用视角，不单列内存安全；但如果你的系统含 C/C++ 组件、内核模块、浏览器引擎，这 6 类必须单独立项。
4. **授权类（访问控制）在 OWASP 侧被高度强调**：本表 25 条里有 **8 条**落在 `A01:2025 Broken Access Control`（CWE-352、862、22、863、284、200、918、639）。OWASP Top 10:2025 明确写出 A01 含 40 个 CWE，且"100% 的被测应用都存在某种形式的访问控制失效"。
5. **CWE-476 上升 8 名、CWE-77 下降 10 名**，是 2025 版里变化最大的两项。CWE-476 的上升与 OWASP 2025 新增 `A10:2025 Mishandling of Exceptional Conditions`（异常情况处理不当）是同一个趋势的两种体现：**异常路径的安全问题正在被单独重视。**

### 官方还发布了另外两份 2025 列表

- **[2025 CWE Top 10 KEV Weaknesses](https://cwe.mitre.org/top25/archive/2025/2025_kev_list.html)**：按 CISA KEV 目录中"实际被在野利用"的弱点重新排名。**做优先级排序时，这份列表比 Top 25 更贴近"正在被打的"。**
- **[2025 "On the Cusp" Weaknesses List](https://cwe.mitre.org/top25/archive/2025/2025_onthecusp_list.html)**：15 条"差一点进 Top 25"的弱点。**做长期治理时值得一并纳入，避免只盯 Top 25 而被趋势变化打个措手不及。**

> ⚠️ **待核实项**：CWE-770（Allocation of Resources Without Limits or Throttling）未出现在我已核实的 OWASP Top 10:2025 官方映射清单中。我已逐一核对 A01、A02、A04、A05、A06、A07、A08、A10 的 "List of Mapped CWEs"（见本页第 8 节来源），均未包含 CWE-770。它可能落在 A03 或 A09 中，也可能在 2025 版中不再被映射。**结论：CWE-770 与 OWASP Top 10:2025 的对应关系请以官方 A03 / A09 页面为准，本页不做推测。**
>
> 另注：OWASP Top 10:2025 是当前版本（来源：<https://owasp.org/www-project-top-ten/>，"The most current released version is the OWASP Top Ten 2025"）。如果你看到的是 2021 版，分类编号与名称都不同（例如 2021 的 A01 也是 Broken Access Control，但 2025 的 A03 变成了 Software Supply Chain Failures，是 2021 没有的新分类）。

---

## 4. 用 CWE 指导代码审计

CWE 在代码审计里扮演三个角色：

### 4.1 制定审计清单

不要漫无目的地读代码。做法：

1. 确定技术栈（语言、框架、数据库、是否有 C 组件）。
2. 从 CWE Top 25 中**筛出与你的技术栈相关的**。例如纯 Java Web 项目里 CWE-121/122/120 的相关性远低于 CWE-79/89/862/639 与 CWE-502。
3. 按"可能的严重度 × 命中概率"排序成审计清单。
4. 对每一条准备：**易出现的代码模式 + 检索思路 + 误报排除**。这三项的具体写法见 [audit-guide.md](./audit-guide.md)。

### 4.2 把发现归类

审计中发现的每个问题都应落到一个 CWE。这一步的价值：

- **同一 CWE 的多个发现应合并成一条修复项**。报告的"发现数"是 12 个还是 3 个，取决于有没有按 CWE 合并。按 CWE 合并能让客户看到"你其实只有 3 类问题"，修复工作量骤降。
- **CWE 决定了往哪儿找修法**。CWE 定义的 "Potential Mitigations" 段落就是官方的修复方向索引。
- **让你和 SAST 工具对齐**。工具报的也是 CWE 编号，可以直接比对覆盖率。

### 4.3 定义安全需求与验收标准

这是 CWE 最有长期价值的地方：

```
把"CWE Top 25 中与本项目技术栈相关的 N 条，必须在设计评审阶段给出对策"
写入项目安全需求基线。

在设计评审检查表里逐条列出这 N 条，要求设计文档明确说明"本设计如何防止 CWE-XXX"。

在验收阶段，用 SAST 工具按 CWE 编号统计，要求这 N 条在扫描结果中为零或已登记豁免理由。
```

这样 CWE 就从"审计员的参考"变成了"开发流程的一部分"。

---

## 5. CWE 与 OWASP Top 10:2025 的对照总览

**OWASP Top 10:2025 十个分类（官方原文列表）**

| ID | 名称 | 中文 | 映射的 CWE 数（官方） |
| --- | --- | --- | --- |
| A01:2025 | Broken Access Control | 访问控制失效 | 40 |
| A02:2025 | Security Misconfiguration | 安全配置错误 | 16 |
| A03:2025 | Software Supply Chain Failures | 软件供应链失效 | 5 |
| A04:2025 | Cryptographic Failures | 加密机制失效 | 32 |
| A05:2025 | Injection | 注入 | 37 |
| A06:2025 | Insecure Design | 不安全设计 | 39 |
| A07:2025 | Authentication Failures | 认证失效 | 36 |
| A08:2025 | Software or Data Integrity Failures | 软件或数据完整性失效 | 14 |
| A09:2025 | Security Logging & Alerting Failures | 安全日志与告警失效 | 5 |
| A10:2025 | Mishandling of Exceptional Conditions | 异常情况处理不当 | 24 |

官方说明：本版共在 10 个分类下映射 **248 个 CWE**，而 MITRE 可下载字典中共有 **968 个 CWE**。

**两者关系小结**

- **OWASP Top 10 是"风险视角"**，一个分类对应**多个** CWE（平均约 25 个）。它回答"这一类风险有多普遍"。
- **CWE Top 25 是"弱点视角"**，每条就是一个具体弱点类型。它回答"哪个具体缺陷最该修"。
- **交叉点**：CWE Top 25 里的 25 条，有 15 条落在 OWASP 分类中（主要是 A01 的 8 条 + A05 的 6 条 + A06/A07/A08/A10 各 1 条），另外 6 条是内存安全类，OWASP 不单列。
- **实操建议**：用 OWASP 分类对决策者汇报（"你有访问控制问题"），用 CWE 编号对开发排期（"请修 CWE-862 和 CWE-639 这两处"）。

---

## 6. 延伸阅读

- [audit-guide.md](./audit-guide.md)：按 Top 25 中 8 个重点弱点写的代码审计检查点（代码模式、grep 思路、误报排除）
- [labs.md](./labs.md)：练习——给有缺陷的代码定位 CWE 编号并修复
- [../ptes/README.md](../ptes/README.md)：CWE 在渗透测试流程的哪一步用
- [../exploit-db/README.md](../exploit-db/README.md)：CWE（类型）+ CVE（实例）+ EDB-ID（利用代码）三层关系
- [../mitre-attack/README.md](../mitre-attack/README.md)：弱点被利用后的行为建模
- [../nist/README.md](../nist/README.md)：SP 800-53 的控制项与 SP 800-40 的补丁管理
- 上级总纲：[../README.md](../README.md)

## 7. 来源 URL

**CWE 官方**

- CWE Top 25 门户（年份、数据集规模 39,080 条 CVE、KEV 列表与 On the Cusp 列表入口）：<https://cwe.mitre.org/top25/>
- **2025 CWE Top 25 完整排名表**（排名、CWE-ID、名称、分值、CVEs in KEV、名次变化）：<https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html>
- 2025 版方法论：<https://cwe.mitre.org/top25/archive/2025/2025_methodology.html>
- 2025 版关键洞察：<https://cwe.mitre.org/top25/archive/2025/2025_key_insights.html>
- 2025 Top 10 KEV Weaknesses：<https://cwe.mitre.org/top25/archive/2025/2025_kev_list.html>
- 2025 "On the Cusp" 列表：<https://cwe.mitre.org/top25/archive/2025/2025_onthecusp_list.html>
- CWE 数据索引（全部条目、视角、层级关系）：<https://cwe.mitre.org/data/index.html>
- CWE 官网：<https://cwe.mitre.org/>
- 条目定义 URL 形式：`https://cwe.mitre.org/data/definitions/<数字>.html`（例：<https://cwe.mitre.org/data/definitions/89.html>）

**OWASP Top 10:2025（用于本页的 CWE ↔ OWASP 对应关系）**

- OWASP Top 10 项目主页（确认 2025 为当前版本）：<https://owasp.org/www-project-top-ten/>
- 2025 版引言（十个分类、变更说明、248 个 CWE / 968 个 CWE 的说法）：<https://owasp.org/Top10/2025/0x00_2025-Introduction/>
- A01:2025 Broken Access Control（40 个 CWE 清单）：<https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/A01_2025-Broken_Access_Control.md>
- A02:2025 Security Misconfiguration（16 个 CWE）：<https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/A02_2025-Security_Misconfiguration.md>
- A04:2025 Cryptographic Failures（32 个 CWE）：<https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/A04_2025-Cryptographic_Failures.md>
- A05:2025 Injection（37 个 CWE）：<https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/A05_2025-Injection.md>
- A06:2025 Insecure Design（39 个 CWE）：<https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/A06_2025-Insecure_Design.md>
- A07:2025 Authentication Failures（36 个 CWE）：<https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/A07_2025-Authentication_Failures.md>
- A08:2025 Software or Data Integrity Failures（14 个 CWE）：<https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/A08_2025-Software_or_Data_Integrity_Failures.md>
- A10:2025 Mishandling of Exceptional Conditions（24 个 CWE）：<https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/A10_2025-Mishandling_of_Exceptional_Conditions.md>
- CISA KEV 目录（在野利用漏洞）：<https://www.cisa.gov/known-exploited-vulnerabilities-catalog>

> **说明**：本页的 CWE ↔ OWASP 对应关系是我从上述每个分类页面的 "List of Mapped CWEs" 段落逐条比对得出的，不是推测。凡未在这些已核实清单中找到的（如 CWE-770），已明确标注为待核实，未做推断。
