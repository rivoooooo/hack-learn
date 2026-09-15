# OWASP Top 10 总览

## 一、版本说明

OWASP Top 10 是"开发者迈向更安全编码的第一步"。截至本文写作时，**官网声明的当前已发布版本是 OWASP Top 10:2025**，取代此前的 2017 版与 2021 版。这是该系列的**第 8 版**。

与本目录相关的版本事实：

- 2025 版共映射 **248 个 CWE**（2021 版约 400 个 CWE 参与分析，2017 版约 30 个）。2025 版把每个类别的 CWE 数量**上限设为 40 个**。
- 数据来源：本版收集了约 175k 条 CVE→CWE 映射记录（2021 版为 125k），并且**不再限制只统计 Top 25 CWE**。
- 排序方法：依然"数据知情，但不盲从数据"——先按数据排出 12 个候选类别，再允许社区调查把 **2 个类别**推荐/提拔进榜单。

> 结论：**如果你在别处看到的还是"A01 失效的访问控制、A02 加密失效、A03 注入…"那套 2021 排序，那是旧版本。** 本库统一以 2025 版为准。

## 二、十大风险一览表

| 编号 | 官方英文名称 | 中文译名 | 官方详情页 | 本目录文档 |
| --- | --- | --- | --- | --- |
| A01:2025 | Broken Access Control | 失效的访问控制 | [链接](https://top10.owasp.org/2025/A01_2025-Broken_Access_Control/) | [A01](A01-Broken-Access-Control.md) |
| A02:2025 | Security Misconfiguration | 安全配置错误 | [链接](https://top10.owasp.org/2025/A02_2025-Security_Misconfiguration/) | [A02](A02-Security-Misconfiguration.md) |
| A03:2025 | Software Supply Chain Failures | 软件供应链失效 | [链接](https://top10.owasp.org/2025/A03_2025-Software_Supply_Chain_Failures/) | [A03](A03-Software-Supply-Chain-Failures.md) |
| A04:2025 | Cryptographic Failures | 加密失效 | [链接](https://top10.owasp.org/2025/A04_2025-Cryptographic_Failures/) | [A04](A04-Cryptographic-Failures.md) |
| A05:2025 | Injection | 注入 | [链接](https://top10.owasp.org/2025/A05_2025-Injection/) | [A05](A05-Injection.md) |
| A06:2025 | Insecure Design | 不安全设计 | [链接](https://top10.owasp.org/2025/A06_2025-Insecure_Design/) | [A06](A06-Insecure-Design.md) |
| A07:2025 | Authentication Failures | 认证失效 | [链接](https://top10.owasp.org/2025/A07_2025-Authentication_Failures/) | [A07](A07-Authentication-Failures.md) |
| A08:2025 | Software or Data Integrity Failures | 软件或数据完整性失效 | [链接](https://top10.owasp.org/2025/A08_2025-Software_or_Data_Integrity_Failures/) | [A08](A08-Software-or-Data-Integrity-Failures.md) |
| A09:2025 | Security Logging and Alerting Failures | 安全日志与告警失效 | [链接](https://top10.owasp.org/2025/A09_2025-Security_Logging_and_Alerting_Failures/) | [A09](A09-Security-Logging-and-Alerting-Failures.md) |
| A10:2025 | Mishandling of Exceptional Conditions | 异常条件处理不当 | [链接](https://top10.owasp.org/2025/A10_2025-Mishandling_of_Exceptional_Conditions/) | [A10](A10-Mishandling-of-Exceptional-Conditions.md) |

各类别的官方统计（平均发生率 Avg Incidence Rate = 被测应用中至少含一个该类别 CWE 的比例）：

| 编号 | CWE 数量 | 平均发生率 | 官方总 CVEs |
| --- | --- | --- | --- |
| A01 | 40 | 3.74%（另一处口径 3.73%） | 32,654 |
| A02 | 16 | 3.00% | 1,375 |
| A03 | 6（官方正文亦提及 5 个核心 CWE） | 5.72% | 11 |
| A04 | 32 | 3.80% | 2,185 |
| A05 | 37 | 3.08% | 62,445 |
| A06 | 39 | 1.86% | 7,647 |
| A07 | 36 | 2.92% | 7,147 |
| A08 | 14 | 2.75% | 3,331 |
| A09 | 5 | 3.91% | 723 |
| A10 | 24 | 2.95% | 3,416 |

> 特别注意 A03：它的**发生率最高（5.72%）**，但 CVE 数量最少（仅 11 条）。官网解释为"测试与记录跟不上"，同时该类别 CVE 的**平均利用分与影响分最高**。

## 三、相对 2021 版的排序变化与原因

| 类别 | 2021 排名 → 2025 排名 | 变化 | 官方给出的原因 |
| --- | --- | --- | --- |
| A01 失效的访问控制 | #1 → #1 | 保持 | 仍是第一大风险；数据中**发生率最高**、相关 CVE 数第二多 |
| A02 安全配置错误 | #5 → #2 | **↑3** | 软件工程越来越依赖"配置"，配置错误在数据中更普遍 |
| A03 软件供应链失效 | #6#（原"易受攻击和过时的组件"）→ #3 | **↑3 + 扩展** | 社区调查中 50% 受访者把它排第一；范围从"已知漏洞组件"扩展到整个供应链 |
| A04 加密失效 | #2 → #4 | **↓2** | 被 A02、A03 挤下两位 |
| A05 注入 | #3 → #5 | **↓2** | 被 A02、A03 挤下两位；XSS 频率高但影响低拉低了平均影响分 |
| A06 不安全设计 | #4 → #6 | **↓2** | 威胁建模与安全设计在业界有可见改善 |
| A07 认证失效 | #7 → #7 | 保持（**改名**） | 原名"识别与认证失效"，改名以更准确反映其 36 个 CWE |
| A08 软件或数据完整性失效 | #8 → #8 | 保持（**改名**） | 原名"软件**和**数据完整性失效"，改为"或（or）"以澄清范围 |
| A09 日志与告警失效 | #9 → #9 | 保持（**改名**） | 原名"安全日志与**监控**失效"，改为"**告警（Alerting）**"，强调"能触发行动" |
| A10 异常条件处理不当 | 新增 → #10 | **新类别** | 新类别，24 个 CWE，聚焦错误处理不当、逻辑错误、fail open（失效开放） |

### 三个必须记住的结构性变化

1. **SSRF（服务端请求伪造，CWE-918）被并入 A01 失效的访问控制。** 2021 版中它是独立类别；2025 版归入 A01。
2. **A03 是"扩展"而非"改名"。** 从 `Vulnerable and Outdated Components`（易受攻击和过时的组件）扩展为整个软件供应链生态（依赖、构建系统、分发基础设施）。
3. **A10 是新类别。** 把原本被归为"代码质量差"的 24 个 CWE 提出来，明确为安全类别。

### 类别的组织逻辑：优先"根因"而非"症状"

2025 版明确说明：CWE 分根因型（如"加密失效""配置错误"）与症状型（如"敏感数据泄露""拒绝服务"）。**本版尽可能按根因分类**，因为根因更利于给出识别与修复指导。平均每类 25 个 CWE，下界是 A03/A09 的 5–6 个，上界是 A01 的 40 个。

## 四、如何把 Top 10 映射到自己的项目

不要做"逐条打勾"，而要做"风险画像"。推荐四步：

**第 1 步：按技术栈裁剪 CWE。** Top 10 是类别，不是 CWE 清单。下载官方 CWE 映射表后，先剔除你技术栈里不存在的语言/框架相关 CWE。例如纯前端项目不需要关心 J2EE 配置类 CWE（CWE-5、CWE-11）。

**第 2 步：按"是否可测"分流。** 有些类别（A05 注入、A01 访问控制）非常容易自动化测试；有些（A03 供应链、A09 日志告警）很难通过黑盒测出。后者应靠**代码审计 / 流程审计 / SBOM 工具**覆盖，而不是指望扫描器。

**第 3 步：把类别翻译成需求，写进用户故事。** 例如：

- A01 → "作为普通用户，我不能通过修改 `orderId` 读取他人订单。"
- A07 → "作为注册用户，我修改密码后所有旧会话立即失效。"
- A03 → "每个构建产物都必须能追溯到 SBOM，且发布前经过 SCA 扫描。"

**第 4 步：把需求对接验收标准。** 上面这些"验收"级别的语句，本质就是 ASVS 的验证要求。用它来定义"通过/不通过"，而不是用 Top 10 的类别名。

### 映射速查表（Top 10 → WSTG → ASVS）

| Top 10 类别 | 主要对应的 WSTG 分类 | 相关 Cheat Sheet（修复） |
| --- | --- | --- |
| A01 访问控制 | ATHZ、IDNT、APIT | Authorization Cheat Sheet |
| A02 配置错误 | CONF | Configuration / HTTP Headers Cheat Sheet |
| A03 供应链 | INFO（架构测绘）、CONF | Vulnerable Dependency Management、Dependency Graph SBOM |
| A04 加密失效 | CRYP | Password Storage、Cryptographic Storage、Transport Layer Protection |
| A05 注入 | INPV、CLNT | Injection Prevention、SQL Injection Prevention、Query Parameterization |
| A06 不安全设计 | BUSL、IDNT | Secure Product Design |
| A07 认证失效 | ATHN、SESS | Authentication、Session Management |
| A08 完整性失效 | INPV（反序列化）、BUSL | Deserialization、Software Supply Chain Security |
| A09 日志告警失效 | ERRH、CONF | Logging、Application Logging Vocabulary |
| A10 异常处理不当 | ERRH、BUSL | Error Handling、Logging |

## 来源

- <https://owasp.org/www-project-top-ten/>
- <https://owasp.org/Top10/2025/>
- <https://top10.owasp.org/2025/0x00_2025-Introduction/>
