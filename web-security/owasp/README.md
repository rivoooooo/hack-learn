# OWASP 模块总纲

本目录整理 OWASP（Open Worldwide Application Security Project，开放式全球应用安全项目）的核心公开标准，目标是让你能**从零开始，照着做一次完整的 Web 渗透测试**，并能把结论映射回具体的风险条目和修复方案。

> 本目录内容仅用于**授权测试与合法靶场**。对未授权系统发起测试属于违法行为。

## 一、OWASP 是什么

OWASP 是一个非营利组织，产出的不是"工具"，而是**行业共识性的文档标准**。它本身不给认证、不给证书，只负责把全球安全从业者的经验固化成公开可引用的清单。最常被引用的三个标准分工如下：

| 标准 | 全称 | 回答的问题 | 一句话定位 |
| --- | --- | --- | --- |
| **Top 10** | OWASP Top 10 | "最该担心的风险是什么？" | 讲**风险**：按严重程度排名的十大风险类别，面向开发与管理层 |
| **WSTG** | Web Security Testing Guide（Web 安全测试指南） | "这些风险具体怎么测？" | 讲**怎么测**：逐条测试用例 + 可执行步骤，面向测试者 |
| **ASVS** | Application Security Verification Standard（应用安全验证标准） | "测到什么程度才算合格？" | 讲**验收标准**：可逐条勾选的验证要求 + 三个等级，面向甲方与合规 |

### 三者的关系（一句话记忆）

- **Top 10 告诉你怕什么**（风险全景，10 个）
- **WSTG 告诉你怎么证明它存在**（测试手法，上百条测试项）
- **ASVS 告诉你做到哪一步算过关**（验证要求，可度量、可写进合同）

典型工作流：用 **Top 10** 排优先级 → 用 **WSTG** 逐条测试取证 → 用 **ASVS** 等级（L1/L2/L3）判定项目是否达标 → 用 **Cheat Sheets**（防御速查表）落地修复。

> 注意：Top 10 是"风险类别"，不是漏洞列表，也不是测试清单。**不能用 Top 10 直接当测试用例**——那是 WSTG 的职责。

### 当前版本（写作时以官网为准）

- **Top 10：当前已发布版本为 OWASP Top 10:2025**（2025 年发布，取代 2021 版）。2025 版有两个新类别、一次合并，共 248 个 CWE。详见 [top10/README.md](top10/README.md)。
- **WSTG：稳定版为 v4.2（2020-12-03）**，最新开发版正在向 v5.0 推进。编号体系为 `WSTG-<分类>-<序号>`。详见 [wstg/README.md](wstg/README.md)。
- **ASVS：当前稳定版为 5.0.0**（2025-05-30 在 Global AppSec EU Barcelona 发布），要求编号形如 `v5.0.0-1.2.5`。

## 二、本目录文件索引

| 文件 | 一句话说明 | 推荐阅读顺序 |
| --- | --- | --- |
| [README.md](README.md) | 本文件：三标准分工 + 学习路线 | 1 |
| [top10/README.md](top10/README.md) | Top 10:2025 总览：十大风险表、排序变化与原因、如何映射到自己的项目 | 2 |
| [top10/A01-Broken-Access-Control.md](top10/A01-Broken-Access-Control.md) | A01 失效的访问控制（含 SSRF 合并说明） | 4 |
| [top10/A02-Security-Misconfiguration.md](top10/A02-Security-Misconfiguration.md) | A02 安全配置错误 | 4 |
| [top10/A03-Software-Supply-Chain-Failures.md](top10/A03-Software-Supply-Chain-Failures.md) | A03 软件供应链失效（2025 新增/扩展） | 4 |
| [top10/A04-Cryptographic-Failures.md](top10/A04-Cryptographic-Failures.md) | A04 加密失效 | 4 |
| [top10/A05-Injection.md](top10/A05-Injection.md) | A05 注入 | 4 |
| [top10/A06-Insecure-Design.md](top10/A06-Insecure-Design.md) | A06 不安全设计 | 4 |
| [top10/A07-Authentication-Failures.md](top10/A07-Authentication-Failures.md) | A07 认证失效 | 4 |
| [top10/A08-Software-or-Data-Integrity-Failures.md](top10/A08-Software-or-Data-Integrity-Failures.md) | A08 软件或数据完整性失效 | 4 |
| [top10/A09-Security-Logging-and-Alerting-Failures.md](top10/A09-Security-Logging-and-Alerting-Failures.md) | A09 安全日志与告警失效 | 4 |
| [top10/A10-Mishandling-of-Exceptional-Conditions.md](top10/A10-Mishandling-of-Exceptional-Conditions.md) | A10 异常条件处理不当（2025 新增） | 4 |
| [wstg/README.md](wstg/README.md) | WSTG 方法论：13 个测试分类、编号体系、测试流程 | 3 |
| [wstg/checklist.md](wstg/checklist.md) | 可直接复制使用的 WSTG 测试清单（勾选框形式） | 5 |
| [labs.md](labs.md) | 合法靶场练习指南：Juice Shop / WebGoat / DVWA / bWAPP | 6 |

## 三、学习路线：从零到能独立做一次 Web 渗透测试

### 阶段 0：建立词汇表（半天）

先读本文件与 [top10/README.md](top10/README.md)，能说清"风险类别 / 测试项 / 验证要求"三者的区别。不要急着开工具。

### 阶段 1：把靶场跑起来（半天）

按 [labs.md](labs.md) 用 Docker 起两个靶场：

```bash
docker run -d -p 127.0.0.1:3000:3000 bkimminich/juice-shop
docker run --name webgoat -it -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 webgoat/webgoat
```

### 阶段 2：逐类理解 Top 10（2–3 天）

按 A01 → A10 顺序精读本目录的十篇文档。每篇都要完成"代码示例"和"自测题"，确保能解释：**为什么这段代码会出问题，修复为什么有效**。

### 阶段 3：掌握 WSTG 方法论（2–3 天）

读 [wstg/README.md](wstg/README.md)，理解 13 个分类的先后依赖：信息搜集 → 配置管理 → 身份 → 认证 → 授权 → 会话 → 注入 → 错误处理 → 密码学 → 业务逻辑 → 客户端 → API。然后用 [wstg/checklist.md](wstg/checklist.md) 对靶场做一次全流程勾选。

### 阶段 4：完成第一次完整测试（3–5 天）

选 **OWASP Juice Shop**（覆盖 Top 10 全类别）作为目标，按下面的流程走一遍：

1. **信息搜集（INFO）**：指纹识别、入口点枚举、架构测绘。
2. **配置测试（CONF）**：检查安全响应头、目录列举、备份文件、HTTP 方法。
3. **身份与认证（IDNT/ATHN）**：账号枚举、默认口令、锁定机制、会话固定。
4. **授权（ATHZ）**：水平越权（IDOR）、垂直越权、强制浏览。
5. **输入验证（INPV）**：XSS、SQL 注入、命令注入、SSRF、模板注入。
6. **业务逻辑（BUSL）**：竞态、流程绕过、支付逻辑。
7. **客户端（CLNT）**：DOM XSS、点击劫持、CORS 配置。
8. **输出报告**：每条发现必须写清"复现步骤 + 证据 + 对应 WSTG 编号 + 对应 Top 10 类别 + 修复建议（引用 Cheat Sheet）"。

### 阶段 5：对真实（授权）目标复盘（持续）

把上面的清单应用到你有**书面授权**的目标上。此时的重点从"找到漏洞"转为"区分真实风险与噪音"，也就是用 ASVS 等级去校准测试深度。

## 四、常用官方链接

- Top 10 项目主页：<https://owasp.org/www-project-top-ten/>
- Top 10:2025 发布页：<https://owasp.org/Top10/2025/>
- WSTG 项目主页：<https://owasp.org/www-project-web-security-testing-guide/>
- WSTG 稳定版：<https://owasp.github.io/www-project-web-security-testing-guide/stable/>
- ASVS 项目主页：<https://owasp.org/www-project-application-security-verification-standard/>
- 防御速查表系列：<https://cheatsheetseries.owasp.org/>

## 来源

- <https://owasp.org/www-project-top-ten/>
- <https://owasp.org/Top10/2025/>
- <https://owasp.org/www-project-web-security-testing-guide/>
- <https://owasp.org/www-project-application-security-verification-standard/>
- <https://cheatsheetseries.owasp.org/>
