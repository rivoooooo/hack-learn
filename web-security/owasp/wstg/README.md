# WSTG 方法论总纲

> 官方项目主页：<https://owasp.org/www-project-web-security-testing-guide/>
> 稳定版：v4.2（2020-12-03）｜开发版：最新（向 v5.0 推进）
> 相关文件：[测试清单 checklist.md](checklist.md)｜[Top 10 总览](../top10/README.md)

WSTG（Web Security Testing Guide，Web 安全测试指南）是 OWASP 面向 Web 应用开发与安全从业者产出的**首要网络安全测试资源**，为渗透测试人员与组织提供了一套最佳实践框架。如果说 [Top 10](../top10/README.md) 回答"怕什么"，WSTG 就是回答"**怎么测**"。

## 一、编号体系怎么看

每个测试场景有一个标识符，格式为：

```
WSTG-<category>-<number>
```

- `category`：4 个大写字母的分类代码，标识测试类型或弱点类型。
- `number`：从 `01` 到 `99` 的两位零填充数字。

例如 `WSTG-INFO-02` 表示"信息搜集"分类下的第 2 个测试（指纹识别 Web 服务器）。

**重要：标识符在不同版本间可能变化。** 因此官方建议在其他文档、报告或工具中优先使用带版本号的格式：

```
WSTG-<version>-<category>-<number>
```

例如 `WSTG-v41-INFO-02` 明确表示"4.1 版中的第 2 个信息搜集测试"。若省略 `<version>`，则应理解为指向**最新内容**。

**链接规范：** 引用 WSTG 场景时应使用带版本的链接，而不要用 `stable` 或 `latest`（这两个一定会变），例如：

```
https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server
```

## 二、测试分类总览

WSTG 稳定版（v4.2）按 12 个分类组织；**最新开发版新增了第 13 个分类（WebAssembly）**。下表给出全部 13 个分类、代码、覆盖阶段与测试项数量。

| 序号 | 分类（中文 / English） | 代码 | 覆盖阶段 | 测试项数 |
| --- | --- | --- | --- | --- |
| 1 | 信息搜集 / Information Gathering | `INFO` | 侦察与测绘 | 10 |
| 2 | 配置与部署管理 / Configuration and Deployment Management | `CONF` | 环境与加固 | 14 |
| 3 | 身份管理 / Identity Management | `IDNT` | 账号生命周期 | 5 |
| 4 | 认证 / Authentication | `ATHN` | 证明身份 | 11 |
| 5 | 授权 / Authorization | `ATHZ` | 权限判定 | 5（含 2 个子项） |
| 6 | 会话管理 / Session Management | `SESS` | 认证后状态 | 11 |
| 7 | 注入 / Injection | `INPV` | 输入进入解释器 | 23（含 9 个子项） |
| 8 | 错误处理 / Error Handling | `ERRH` | 异常与信息泄露 | 2 |
| 9 | 弱加密 / Weak Cryptography | `CRYP` | 传输与存储加密 | 4 |
| 10 | 业务逻辑 / Business Logic | `BUSL` | 业务流程与规则 | 10 |
| 11 | 客户端 / Client-side | `CLNT` | 浏览器侧 | 15（含 1 个子项） |
| 12 | API 测试 / API Testing | `APIT` | API 与 GraphQL | 5（含概述与 GraphQL） |
| 13 | WebAssembly 测试 / WebAssembly Testing | `WASM` | 新兴（仅概述） | 暂只有概述 |

> 最新开发版分类与 v4.2 的差异：新增了 `WSTG-INPV-20` 批量赋值、`WSTG-INPV-21` CSV 注入、`WSTG-INPV-22` 原型链污染、`WSTG-INPV-23` 不安全反序列化，以及 `WSTG-CLNT-15` 客户端模板注入等项目；分类 7 的名称在开发版中由 "Input Validation Testing" 改为 "Injection"。核对具体编号时请以你使用的版本为准。

### 各分类分别测什么

- **INFO 信息搜集**：不碰业务逻辑，先把目标"看透"——搜索引擎侦察、服务器/框架/应用指纹、metafile（robots.txt、sitemap）审查、攻击面识别、入口点与执行路径测绘、架构测绘。
- **CONF 配置与部署管理**：网络与平台配置、文件扩展名处理、旧备份与未引用文件、管理接口枚举、HTTP 方法、HSTS、RIA 跨域策略、文件权限、子域名接管、云存储、CSP、路径混淆、其他安全响应头。
- **IDNT 身份管理**：角色定义、注册流程、账号开通流程、账号枚举与可猜用户名、用户名策略强弱。
- **ATHN 认证**：凭据是否走加密通道、默认凭据、锁定机制、认证模式绕过、"记住密码"、浏览器缓存、弱认证方法、弱安全问题、口令修改/重置、替代通道认证、MFA。
- **ATHZ 授权**：路径穿越与文件包含、绕过授权模式、权限提升、不安全直接对象引用（IDOR）、OAuth 弱点。
- **SESS 会话管理**：会话方案、Cookie 属性、会话固定、暴露的会话变量、CSRF、登出功能、超时、会话困惑（Session Puzzling）、会话劫持、JWT、并发会话。
- **INPV 注入**：反射/存储 XSS、HTTP 动词篡改、参数污染、SQL 注入（多数据库/NoSQL/ORM/客户端）、LDAP、XML、SSI、XPath、IMAP/SMTP、代码注入与文件包含、命令注入、格式串、潜伏漏洞、响应拆分、请求走私、Host 头注入、SSTI、SSRF、批量赋值、CSV 注入、原型链污染、不安全反序列化。
- **ERRH 错误处理**：错误处理不当、堆栈跟踪泄露。
- **CRYP 弱加密**：弱传输层安全、填充预言、未加密通道发送敏感信息、弱加密原语。
- **BUSL 业务逻辑**：数据校验、能否伪造请求、完整性校验、流程时序、功能使用次数限制、绕过工作流、应用滥用防护、上传意外文件类型、上传恶意文件、支付功能。
- **CLNT 客户端**：DOM 型与自 DOM 型 XSS、JavaScript 执行、HTML 注入、客户端 URL 重定向、CSS 注入、客户端资源操纵、CORS、Cross Site Flashing、点击劫持、WebSockets、Web Messaging、浏览器存储、跨站脚本包含（XSSI）、反向标签劫持（Reverse Tabnabbing）、客户端模板注入。
- **APIT API 测试**：API 侦察、API 对象级授权失效（BOLA）、过度数据暴露、API 功能级授权失效（BFLA）、GraphQL。
- **WASM WebAssembly 测试**：目前仅有概述，是仍在发展的分类。

## 三、测试流程

WSTG 的分类顺序本身就是推荐的执行顺序——**后面的测试依赖前面得到的信息**。推荐流程：

```
0. 范围与授权确认（不属于 WSTG 条目，但必须先做）
        |
        v
1. 信息搜集 (INFO)  ──────────────► 产出：资产清单、入口点、技术栈、架构图
        |
        v
2. 配置与部署管理 (CONF) ─────────► 产出：加固缺陷、暴露的管理面、安全头缺失
        |
        v
3. 身份管理 (IDNT) + 认证 (ATHN) ─► 产出：账号枚举、弱认证、默认凭据、MFA 缺陷
        |
        v
4. 授权 (ATHZ) + 会话管理 (SESS) ─► 产出：水平/垂直越权、会话固定、CSRF
        |
        v
5. 注入 (INPV) ───────────────────► 产出：XSS/SQLi/命令注入/SSRF/SSTI/反序列化
        |
        v
6. 错误处理 (ERRH) + 弱加密 (CRYP) ► 产出：信息泄露、明文传输、弱算法
        |
        v
7. 业务逻辑 (BUSL) ───────────────► 产出：竞态、流程绕过、支付逻辑缺陷
        |
        v
8. 客户端 (CLNT) + API (APIT) ────► 产出：DOM XSS、CORS、BOLA/BFLA
```

### 阶段说明

1. **信息搜集**是一切的基础。没有资产清单，后面的测试就是随机撞运气。
2. **配置测试**通常在信息搜集刚结束时做，因为此时你已经知道技术栈。
3. **身份与认证**要先于授权——必须先能当"某个用户"，才能测"这个用户能越权做什么"。
4. **注入**测试量大，建议按参数清单逐个覆盖，而不是随机猜。
5. **业务逻辑**无法自动化，必须理解业务才能测。这是最依赖人、也最容易出高价值漏洞的阶段。
6. **客户端与 API** 常被忽略，但在现代前后端分离架构中往往是主战场。

## 四、如何把 WSTG 条目转成测试用例清单

WSTG 是"参考手册"，不是"执行清单"。落地时必须把它翻译成带**目标、步骤、预期结果、证据**的测试用例。

### 单条测试用例模板

```markdown
### TC-ATHN-02-01 默认凭据测试

- **WSTG 编号**：WSTG-ATHN-02（Default Credentials）
- **对应 Top 10**：A07 认证失效
- **测试目标**：验证管理员后台在部署时未保留出厂默认口令
- **前置条件**：已获取管理后台 URL；已获授权测试
- **测试数据**：admin/admin、admin/password、administrator/password 等
- **测试步骤**：
  1. 访问 /admin/login
  2. 依次提交上述凭据组合
  3. 记录每次响应的状态码与页面内容
- **预期结果**：所有默认组合均认证失败，且失败不留可枚举的系统信息
- **实际结果**：（填写）
- **证据**：（截图/请求响应导出/录屏）
- **判定**：通过 / 不通过 / 不适用
- **修复建议**：首次启动强制改密；参考 Authentication Cheat Sheet
```

### 测试用例总表模板

| 用例编号 | WSTG 编号 | 测试项名称 | 对应 Top 10 | 优先级 | 前置条件 | 预期结果 | 判定 | 证据链接 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-INFO-01-01 | WSTG-INFO-01 | 搜索引擎信息泄露侦察 | A02 | 中 | 已知目标域名 | 无敏感信息被索引 |  |  |
| TC-CONF-06-01 | WSTG-CONF-06 | HTTP 方法测试 | A02 | 中 | 已确认 Web 服务器 | 仅开放必要方法 |  |  |
| TC-ATHN-02-01 | WSTG-ATHN-02 | 默认凭据 | A07 | 高 | 已定位登录入口 | 默认凭据无效 |  |  |
| TC-ATHZ-04-01 | WSTG-ATHZ-04 | IDOR | A01 | 高 | 有两个测试账号 | 无法读取他人资源 |  |  |
| TC-INPV-05-01 | WSTG-INPV-05 | SQL 注入 | A05 | 高 | 已枚举参数 | 参数化查询，无注入 |  |  |
| TC-BUSL-05-01 | WSTG-BUSL-05 | 功能使用次数限制 | A06 | 高 | 存在"限一次"功能 | 并发下仍限一次 |  |  |

### 优先级建议

- **高**：可能直接导致数据泄露、越权或代码执行的项（ATHZ、INPV、ATHN、BUSL 支付相关）。
- **中**：信息泄露、配置缺陷、会话问题。
- **低**：纯粹的信息搜集与加固建议类。

### 可复制的执行清单

逐条勾选式的完整清单见 [checklist.md](checklist.md)，按 13 个分类组织，每条带 WSTG 编号与中英文名称。

## 五、与 Top 10、ASVS 的配合

| 步骤 | 使用哪个标准 | 产出 |
| --- | --- | --- |
| 排优先级 | Top 10 | 本次测试重点关注的风险类别 |
| 设计测试用例 | WSTG | 具体测试项 + 步骤 + 预期结果 |
| 判定是否达标 | ASVS（按 L1/L2/L3 等级） | 通过/不通过 + 差距清单 |
| 落地修复 | Cheat Sheets | 修复方案与代码示例 |

具体映射见 [top10/README.md 的映射速查表](../top10/README.md)。

## 来源

- <https://owasp.org/www-project-web-security-testing-guide/>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/>
- <https://owasp.github.io/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/README>
- <https://owasp.org/www-project-application-security-verification-standard/>
