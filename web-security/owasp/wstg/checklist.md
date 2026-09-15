# WSTG 测试清单（可复制使用）

> 基于 OWASP WSTG 最新开发版整理。勾选框形式，按 13 个分类组织。
> 每条格式：`WSTG 编号` + 中文名称（English original）。
> 使用方式：复制本文件到你的测试记录中，逐条勾选并在"判定"栏记录通过/不通过/不适用。

**测试信息**

- 目标系统：
- 测试版本 / 提交：
- 测试人：
- 测试日期：
- 授权范围：
- 使用的 WSTG 版本：（v4.2 / latest）

---

## 1. 信息搜集（Information Gathering / `WSTG-INFO`）

- [ ] `WSTG-INFO-01` 通过搜索引擎侦察信息泄露（Conduct Search Engine Reconnaissance for Information Leakage）
- [ ] `WSTG-INFO-02` 指纹识别 Web 服务器（Fingerprint Web Server）
- [ ] `WSTG-INFO-03` 审查 Web 服务器元文件中的信息泄露（Review Webserver Metafiles for Information Leakage）
- [ ] `WSTG-INFO-04` 攻击面识别（Attack Surface Identification）
- [ ] `WSTG-INFO-05` 审查网页内容中的信息泄露（Review Web Page Content for Information Leakage）
- [ ] `WSTG-INFO-06` 识别应用入口点（Identify Application Entry Points）
- [ ] `WSTG-INFO-07` 测绘应用的执行路径（Map Execution Paths Through Application）
- [ ] `WSTG-INFO-08` 指纹识别 Web 应用框架（Fingerprint Web Application Framework）
- [ ] `WSTG-INFO-09` 指纹识别 Web 应用（Fingerprint Web Application）
- [ ] `WSTG-INFO-10` 测绘应用架构（Map Application Architecture）

## 2. 配置与部署管理（Configuration and Deployment Management / `WSTG-CONF`）

- [ ] `WSTG-CONF-01` 网络基础设施配置（Network Infrastructure Configuration）
- [ ] `WSTG-CONF-02` 应用平台配置（Application Platform Configuration）
- [ ] `WSTG-CONF-03` 文件扩展名处理与敏感信息（File Extensions Handling for Sensitive Information）
- [ ] `WSTG-CONF-04` 审查旧备份与未引用文件中的敏感信息（Review Old Backup and Unreferenced Files for Sensitive Information）
- [ ] `WSTG-CONF-05` 枚举基础设施与应用管理接口（Enumerate Infrastructure and Application Admin Interfaces）
- [ ] `WSTG-CONF-06` HTTP 方法（HTTP Methods）
- [ ] `WSTG-CONF-07` HTTP 严格传输安全（HTTP Strict Transport Security）
- [ ] `WSTG-CONF-08` RIA 跨域策略（RIA Cross Domain Policy）
- [ ] `WSTG-CONF-09` 文件权限（File Permission）
- [ ] `WSTG-CONF-10` 子域名接管（Subdomain Takeover）
- [ ] `WSTG-CONF-11` 云存储（Cloud Storage）
- [ ] `WSTG-CONF-12` 内容安全策略（Content Security Policy）
- [ ] `WSTG-CONF-13` 路径混淆（Path Confusion）
- [ ] `WSTG-CONF-14` 其他 HTTP 安全响应头配置错误（Other HTTP Security Header Misconfigurations）

## 3. 身份管理（Identity Management / `WSTG-IDNT`）

- [ ] `WSTG-IDNT-01` 角色定义（Role Definitions）
- [ ] `WSTG-IDNT-02` 用户注册流程（User Registration Process）
- [ ] `WSTG-IDNT-03` 账号开通流程（Account Provisioning Process）
- [ ] `WSTG-IDNT-04` 账号枚举与可猜用户账号（Account Enumeration and Guessable User Account）
- [ ] `WSTG-IDNT-05` 弱或未强制的用户名策略（Weak or Unenforced Username Policy）

## 4. 认证（Authentication / `WSTG-ATHN`）

- [ ] `WSTG-ATHN-01` 凭据是否通过加密通道传输（Credentials Transported over an Encrypted Channel）
- [ ] `WSTG-ATHN-02` 默认凭据（Default Credentials）
- [ ] `WSTG-ATHN-03` 弱锁定机制（Weak Lock Out Mechanism）
- [ ] `WSTG-ATHN-04` 绕过认证模式（Bypassing Authentication Schema）
- [ ] `WSTG-ATHN-05` 不安全的"记住密码"（Vulnerable Remember Password）
- [ ] `WSTG-ATHN-06` 浏览器缓存弱点（Browser Cache Weaknesses）
- [ ] `WSTG-ATHN-07` 弱认证方法（Weak Authentication Methods）
- [ ] `WSTG-ATHN-08` 弱安全问题答案（Weak Security Question Answer）
- [ ] `WSTG-ATHN-09` 弱的口令修改或重置功能（Weak Password Change or Reset Functionalities）
- [ ] `WSTG-ATHN-10` 替代通道中的弱认证（Weaker Authentication in Alternative Channel）
- [ ] `WSTG-ATHN-11` 多因素认证（Multi-Factor Authentication）

## 5. 授权（Authorization / `WSTG-ATHZ`）

- [ ] `WSTG-ATHZ-01` 目录穿越与文件包含（Testing Directory Traversal File Include）
- [ ] `WSTG-ATHZ-02` 绕过授权模式（Testing for Bypassing Authorization Schema）
- [ ] `WSTG-ATHZ-03` 权限提升（Testing for Privilege Escalation）
- [ ] `WSTG-ATHZ-04` 不安全的直接对象引用（Testing for Insecure Direct Object References）
- [ ] `WSTG-ATHZ-05` OAuth 弱点（Testing for OAuth Weaknesses）
  - [ ] `WSTG-ATHZ-05.1` OAuth 授权服务器弱点（OAuth Authorization Server Weaknesses）
  - [ ] `WSTG-ATHZ-05.2` OAuth 客户端弱点（OAuth Client Weaknesses）

## 6. 会话管理（Session Management / `WSTG-SESS`）

- [ ] `WSTG-SESS-01` 会话管理方案（Session Management Schema）
- [ ] `WSTG-SESS-02` Cookie 属性（Cookies Attributes）
- [ ] `WSTG-SESS-03` 会话固定（Session Fixation）
- [ ] `WSTG-SESS-04` 暴露的会话变量（Exposed Session Variables）
- [ ] `WSTG-SESS-05` 跨站请求伪造（Cross Site Request Forgery）
- [ ] `WSTG-SESS-06` 登出功能（Logout Functionality）
- [ ] `WSTG-SESS-07` 会话超时（Session Timeout）
- [ ] `WSTG-SESS-08` 会话困惑（Session Puzzling）
- [ ] `WSTG-SESS-09` 会话劫持（Session Hijacking）
- [ ] `WSTG-SESS-10` JSON Web Token（JSON Web Tokens）
- [ ] `WSTG-SESS-11` 并发会话（Concurrent Sessions）

## 7. 注入（Injection / `WSTG-INPV`）

- [ ] `WSTG-INPV-01` 反射型跨站脚本（Reflected Cross Site Scripting）
- [ ] `WSTG-INPV-02` 存储型跨站脚本（Stored Cross Site Scripting）
- [ ] `WSTG-INPV-03` HTTP 动词篡改（HTTP Verb Tampering）
- [ ] `WSTG-INPV-04` HTTP 参数污染（HTTP Parameter Pollution）
- [ ] `WSTG-INPV-05` SQL 注入（SQL Injection）
  - [ ] `WSTG-INPV-05.1` Oracle
  - [ ] `WSTG-INPV-05.2` MySQL
  - [ ] `WSTG-INPV-05.3` SQL Server
  - [ ] `WSTG-INPV-05.4` PostgreSQL
  - [ ] `WSTG-INPV-05.5` MS Access
  - [ ] `WSTG-INPV-05.6` NoSQL 注入（NoSQL Injection）
  - [ ] `WSTG-INPV-05.7` ORM 注入（ORM Injection）
  - [ ] `WSTG-INPV-05.8` 客户端注入（Client-side）
- [ ] `WSTG-INPV-06` LDAP 注入（LDAP Injection）
- [ ] `WSTG-INPV-07` XML 注入（XML Injection）
- [ ] `WSTG-INPV-08` SSI 注入（SSI Injection）
- [ ] `WSTG-INPV-09` XPath 注入（XPath Injection）
- [ ] `WSTG-INPV-10` IMAP SMTP 注入（IMAP SMTP Injection）
- [ ] `WSTG-INPV-11` 代码注入（Code Injection）
  - [ ] `WSTG-INPV-11.1` 文件包含（File Inclusion）
- [ ] `WSTG-INPV-12` 命令注入（Command Injection）
- [ ] `WSTG-INPV-13` 格式串注入（Format String Injection）
- [ ] `WSTG-INPV-14` 潜伏漏洞（Incubated Vulnerability）
- [ ] `WSTG-INPV-15` HTTP 响应拆分（HTTP Response Splitting）
- [ ] `WSTG-INPV-16` HTTP 请求走私（HTTP Request Smuggling）
- [ ] `WSTG-INPV-17` Host 头注入（Host Header Injection）
- [ ] `WSTG-INPV-18` 服务端模板注入（Server-side Template Injection）
- [ ] `WSTG-INPV-19` 服务端请求伪造（Server-Side Request Forgery）
- [ ] `WSTG-INPV-20` 批量赋值（Mass Assignment）
- [ ] `WSTG-INPV-21` CSV 注入（CSV Injection）
- [ ] `WSTG-INPV-22` 原型链污染（Prototype Pollution）
- [ ] `WSTG-INPV-23` 不安全反序列化（Insecure Deserialization）

## 8. 错误处理（Error Handling / `WSTG-ERRH`）

- [ ] `WSTG-ERRH-01` 错误处理不当（Improper Error Handling）
- [ ] `WSTG-ERRH-02` 堆栈跟踪（Stack Traces）

## 9. 弱加密（Weak Cryptography / `WSTG-CRYP`）

- [ ] `WSTG-CRYP-01` 弱传输层安全（Weak Transport Layer Security）
- [ ] `WSTG-CRYP-02` 填充预言（Padding Oracle）
- [ ] `WSTG-CRYP-03` 通过未加密通道发送敏感信息（Sensitive Information Sent via Unencrypted Channels）
- [ ] `WSTG-CRYP-04` 弱加密原语（Weak Cryptographic Primitives）

## 10. 业务逻辑（Business Logic / `WSTG-BUSL`）

- [ ] `WSTG-BUSL-01` 业务逻辑数据校验（Business Logic Data Validation）
- [ ] `WSTG-BUSL-02` 伪造请求的能力（Ability to Forge Requests）
- [ ] `WSTG-BUSL-03` 完整性校验（Integrity Checks）
- [ ] `WSTG-BUSL-04` 流程时序（Process Timing）
- [ ] `WSTG-BUSL-05` 功能使用次数限制（Number of Times a Function Can Be Used Limits）
- [ ] `WSTG-BUSL-06` 绕过工作流（Circumvention of Work Flows）
- [ ] `WSTG-BUSL-07` 应用滥用防护（Defenses Against Application Misuse）
- [ ] `WSTG-BUSL-08` 上传意外文件类型（Upload of Unexpected File Types）
- [ ] `WSTG-BUSL-09` 上传恶意文件（Upload of Malicious Files）
- [ ] `WSTG-BUSL-10` 支付功能（Payment Functionality）

## 11. 客户端（Client-side / `WSTG-CLNT`）

- [ ] `WSTG-CLNT-01` DOM 型跨站脚本（Testing for DOM-Based Cross Site Scripting）
  - [ ] `WSTG-CLNT-01.1` 自 DOM 型跨站脚本（Testing for Self DOM Based Cross-Site Scripting）
- [ ] `WSTG-CLNT-02` JavaScript 执行（Testing for JavaScript Execution）
- [ ] `WSTG-CLNT-03` HTML 注入（Testing for HTML Injection）
- [ ] `WSTG-CLNT-04` 客户端 URL 重定向（Testing for Client-side URL Redirect）
- [ ] `WSTG-CLNT-05` CSS 注入（Testing for CSS Injection）
- [ ] `WSTG-CLNT-06` 客户端资源操纵（Testing for Client-side Resource Manipulation）
- [ ] `WSTG-CLNT-07` 跨域资源共享（Testing for Cross Origin Resource Sharing）
- [ ] `WSTG-CLNT-08` Cross Site Flashing（Testing for Cross Site Flashing）
- [ ] `WSTG-CLNT-09` 点击劫持（Testing for Clickjacking）
- [ ] `WSTG-CLNT-10` WebSockets（Testing for WebSockets）
- [ ] `WSTG-CLNT-11` Web Messaging（Testing for Web Messaging）
- [ ] `WSTG-CLNT-12` 浏览器存储（Testing for Browser Storage）
- [ ] `WSTG-CLNT-13` 跨站脚本包含（Testing for Cross Site Script Inclusion）
- [ ] `WSTG-CLNT-14` 反向标签劫持（Testing for Reverse Tabnabbing）
- [ ] `WSTG-CLNT-15` 客户端模板注入（Testing for Client-side Template Injection）

## 12. API 测试（API Testing / `WSTG-APIT`）

- [ ] `WSTG-APIT-01` API 侦察（API Reconnaissance）
- [ ] `WSTG-APIT-02` API 对象级授权失效（API Broken Object Level Authorization）
- [ ] `WSTG-APIT-03` 过度数据暴露（Excessive Data Exposure）
- [ ] `WSTG-APIT-04` API 功能级授权失效（API Broken Function Level Authorization）
- [ ] `WSTG-APIT-99` GraphQL

## 13. WebAssembly 测试（WebAssembly Testing / `WSTG-WASM`）（开发中）

- [ ] `WSTG-WASM-00` WebAssembly 测试概述（WebAssembly Testing Overview）
  - 注：该分类在最新开发版中**仅有概述**，尚无独立编号的测试项。

---

## 判定汇总表

| 分类 | 总项数 | 通过 | 不通过 | 不适用 | 备注 |
| --- | --- | --- | --- | --- | --- |
| INFO | 10 |  |  |  |  |
| CONF | 14 |  |  |  |  |
| IDNT | 5 |  |  |  |  |
| ATHN | 11 |  |  |  |  |
| ATHZ | 5（+2 子项） |  |  |  |  |
| SESS | 11 |  |  |  |  |
| INPV | 23（+9 子项） |  |  |  |  |
| ERRH | 2 |  |  |  |  |
| CRYP | 4 |  |  |  |  |
| BUSL | 10 |  |  |  |  |
| CLNT | 15（+1 子项） |  |  |  |  |
| APIT | 5 |  |  |  |  |
| WASM | 1（仅概述） |  |  |  |  |

## 不通过项记录

| 编号 | WSTG 编号 | 问题描述 | 对应 Top 10 | 严重程度 | 修复建议 | 证据 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## 来源

- <https://owasp.org/www-project-web-security-testing-guide/>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/>
- <https://owasp.github.io/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Injection/README>
- <https://owasp.github.io/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side/README>
- <https://owasp.github.io/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/12-API_Testing/README>
