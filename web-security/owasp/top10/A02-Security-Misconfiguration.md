# A02:2025 安全配置错误（Security Misconfiguration）

> 官方详情页：<https://top10.owasp.org/2025/A02_2025-Security_Misconfiguration/>
> 排名：**第 2 位**（2021 版为第 5 位，**上升 3 位**）
> CWE 数量：16 个｜平均发生率：3.00%｜相关 CVE：1,375
> 主要 CWE：CWE-16 Configuration、CWE-611 外部实体引用限制不当（XXE）

## 一句话理解

安全配置错误就是**软件本身没写错，但装错了、开错了、忘了关**——默认口令没改、调试模式没关、目录列举没关、安全响应头没发，攻击者无需写一行代码就能利用。

## 风险原理

配置错误是"系统在安全维度上被设置成了错误的值"。它不是代码缺陷，而是**部署态缺陷**。2025 版把它从第 5 位提到第 2 位，官方解释很直接：*现代软件的行为越来越多由配置驱动，因此配置错误的占比自然上升*。数据中 100% 被测应用都存在某种配置问题。

常见的错误配置来源：

1. **缺少统一加固流程。** 开发/Q A/生产环境配置不一致，生产环境只是"开发环境改了个数据库地址"。
2. **开启了不必要的功能。** 示例应用、测试页面、调试端点、多余端口、多余账号权限。
3. **默认凭据未变更。** 中间件管理后台、数据库、云服务控制台仍是默认账号口令。
4. **错误信息过度。** 直接把堆栈跟踪（stack trace）返回给用户，泄露框架版本与代码路径。
5. **向后兼容优先于安全。** 为了兼容旧客户端，保留了不安全的协议或算法。
6. **缺失安全响应头。** 没有 `Content-Security-Policy`、`Strict-Transport-Security`、`X-Content-Type-Options`、`X-Frame-Options` 等。
7. **云存储权限开放。** 对象存储桶（如 S3 bucket）默认可公开读取或被错误设为 `public-read`。
8. **XXE。** XML 解析器允许外部实体引用（CWE-611），攻击者可通过文件读取、SSRF 达成信息泄露。

ASCII 数据流图：

```
开发环境配置                生产环境期望              实际生产环境
 debug=True        ────►    debug=False      ────►   debug=True（忘了改）
 默认口令 admin    ────►    强口令           ────►   admin/admin（没改）
 目录列举 on       ────►    关闭             ────►   开启 -> /backup/ 可浏览
 无安全响应头      ────►    完整 CSP+HSTS    ────►   全都缺失
```

## 典型场景与真实案例模式

> 以下为"某类系统常见的模式"归纳，不指向具体厂商事件。

- **中间件管理后台。** Jenkins/Tomcat Manager/RabbitMQ 管理界面暴露在公网且使用默认口令，攻击者借此直接获得命令执行能力（脚本控制台）。
- **调试端点未关闭。** 生产环境保留了框架的 `/debug`、`/actuator`、`/__debug__`、`phpinfo()` 页面，泄露环境变量、数据库连接串、密钥。
- **云对象存储。** 对象存储桶策略被设为公有读，导致备份文件、客户数据可被批量枚举下载（常见模式：桶名可预测 + 开启 ListBucket）。
- **目录列举。** Web 服务器开启了目录索引，攻击者浏览到 `/assets/` 下的源码压缩包、`.map` 文件，反推业务逻辑。
- **详细的错误页面。** 应用抛出未捕获异常，返回完整堆栈，暴露 ORM 名称、表名、文件绝对路径，为后续注入攻击提供情报。
- **XXE。** 接受 XML 的接口（老式 SOAP、SVG 上传、Office 文档解析）未禁用外部实体，攻击者构造实体引用读取 `/etc/passwd` 或探测内网。
- **缺失 CORS/安全头。** 未配置 `X-Content-Type-Options: nosniff` 导致 MIME 嗅探型 XSS；未配置 HSTS 导致 SSL 剥离。

## 怎么测

对应 WSTG 测试项：

- [WSTG-CONF-01](../wstg/checklist.md) 网络基础设施配置
- [WSTG-CONF-02](../wstg/checklist.md) 应用平台配置
- [WSTG-CONF-03](../wstg/checklist.md) 文件扩展名处理
- [WSTG-CONF-04](../wstg/checklist.md) 旧备份与未引用文件
- [WSTG-CONF-05](../wstg/checklist.md) 基础设施与应用管理接口枚举
- [WSTG-CONF-06](../wstg/checklist.md) HTTP 方法
- [WSTG-CONF-07](../wstg/checklist.md) HTTP 严格传输安全（HSTS）
- [WSTG-CONF-09](../wstg/checklist.md) 文件权限
- [WSTG-CONF-10](../wstg/checklist.md) 子域名接管
- [WSTG-CONF-11](../wstg/checklist.md) 云存储
- [WSTG-CONF-12](../wstg/checklist.md) 内容安全策略（CSP）
- [WSTG-CONF-14](../wstg/checklist.md) 其他 HTTP 安全响应头配置错误
- [WSTG-ERRH-01](../wstg/checklist.md) 错误处理不当
- [WSTG-ERRH-02](../wstg/checklist.md) 堆栈跟踪

**手工测试步骤**

1. **枚举管理接口与敏感路径。**
   ```bash
   ffuf -u https://target/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -mc all -fc 404
   # 重点看 /admin /manager /actuator /debug /console /phpinfo.php /.git/ /.env /backup.zip
   ```
2. **检查安全响应头。**
   ```bash
   curl -sI https://target/ | grep -iE 'strict-transport|content-security|x-content-type|x-frame|referrer-policy|permissions-policy'
   ```
   缺失或不安全（如 CSP 含 `unsafe-inline`）即为问题。
3. **测试 HTTP 方法。**
   ```bash
   curl -s -X OPTIONS -i https://target/ | grep -i allow
   curl -s -X TRACE -i https://target/
   curl -s -X DELETE -i https://target/index.html
   ```
   只应开放业务必需的方法（通常仅 GET/POST，必要时 PUT/DELETE 且有授权）。
4. **触发错误看返回。** 提交非法类型、超长参数、非法 JSON，观察是否返回堆栈、框架版本、SQL 语句。
   ```bash
   curl -s 'https://target/api/search?q=%27' | head -50
   curl -s -X POST https://target/api/json -H 'Content-Type: application/json' -d '{"a":'
   ```
5. **检查目录列举与备份文件。**
   ```bash
   for f in .git/HEAD .env backup.zip www.zip db.sql .DS_Store; do
     code=$(curl -s -o /dev/null -w '%{http_code}' https://target/$f); echo "$f -> $code";
   done
   ```
6. **测试 XXE。** 对接受 XML 的接口提交：
   ```xml
   <?xml version="1.0"?>
   <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
   <foo>&xxe;</foo>
   ```
   若响应中出现 `/etc/passwd` 内容，则存在 XXE。再测带外（OOB）变体探测内网。
7. **云存储检查。** 用目标域名/组织名推测桶名，测试匿名列取：
   ```bash
   aws s3 ls s3://<bucket-name> --no-sign-request
   curl -s https://<bucket>.s3.amazonaws.com/
   ```
8. **扫描自动化加固基线。** 用 `nuclei -t http/misconfiguration/` 或 Nikto 快速覆盖常见配置错误。

## 代码示例

### 易受攻击的代码（Node.js / Express）

```js
const express = require('express');
const app = express();

// 危险 1：生产环境仍开启详细错误
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message, stack: err.stack });  // 泄露堆栈
});

// 危险 2：没有任何安全响应头（默认无 CSP / HSTS / nosniff）
app.get('/', (req, res) => res.send('hello'));

app.listen(3000);
```

### 修复后的代码

```js
const express = require('express');
const helmet = require('helmet');

const app = express();

// 统一安全响应头：CSP、HSTS、nosniff、frame-ancestors、referrer-policy 等
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],            // 不使用 unsafe-inline
      objectSrc: ["'none'"],
      frameAncestors: ["'none'"],
    },
  },
  hsts: { maxAge: 31536000, includeSubDomains: true, preload: true },
}));

app.get('/', (req, res) => res.send('hello'));

// 统一错误处理：记录详细日志到服务端，只向用户返回通用信息
app.use((err, req, res, next) => {
  req.log.error({ err }, 'unhandled error');       // 详细内容只进服务端日志
  res.status(500).json({ error: 'Internal Server Error' });  // 对外最小化
});

app.listen(3000);
```

### XXE 的修复（Java）

```java
// 危险：默认解析器允许外部实体
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
DocumentBuilder db = dbf.newDocumentBuilder();
Document doc = db.parse(userInputStream);
```

```java
// 修复：完全禁用 DTD 与外部实体
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);   // 首选：直接禁 DTD
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
dbf.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);
dbf.setXIncludeAware(false);
dbf.setExpandEntityReferences(false);

DocumentBuilder db = dbf.newDocumentBuilder();
Document doc = db.parse(userInputStream);
```

> 若业务必须支持 DTD，则至少禁用外部实体与外部 DTD 加载，并设置 `XMLConstants.ACCESS_EXTERNAL_DTD`/`ACCESS_EXTERNAL_SCHEMA` 为空字符串。

## 防御清单

- [ ] 建立**可重复的加固流程**：Dev/QA/Prod 配置一致，仅凭据不同，且可自动化部署一个全新安全环境。
- [ ] 最小化平台：移除示例应用、文档、测试页面、无用框架与功能。
- [ ] 绝不保留默认口令，尤其是管理账号；首次启动强制改密。
- [ ] 关闭调试模式、详细错误与堆栈返回；统一用中央错误处理拦截。
- [ ] 关闭目录列举；确保 `.git`、`.env`、备份、源码映射文件不在 Web 根目录。
- [ ] 发送安全响应头：`Content-Security-Policy`、`Strict-Transport-Security`、`X-Content-Type-Options: nosniff`、`X-Frame-Options`/`frame-ancestors`、`Referrer-Policy`。
- [ ] 只开放必要 HTTP 方法，禁用 `TRACE`。
- [ ] 云存储桶权限最小化，禁止匿名 ListBucket，定期审计权限。
- [ ] 所有 XML 解析器禁用 DTD 与外部实体（XXE）。
- [ ] 用身份联邦、短期凭据、角色机制替代在代码/配置中硬编码静态密钥。
- [ ] 自动化校验各环境配置：把配置基线纳入 CI（如 `nuclei`、`osquery`、CIS Benchmark）。
- [ ] 参考 [Configuration Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Configuration_Cheat_Sheet.html) 与 [XXE Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)。

## 常见坑

- **坑 1：只在生产环境手动改，没写进自动化。** 下次重建环境时配置回退，漏洞重现。加固必须代码化（Infrastructure as Code）。
- **坑 2：以为"关掉错误显示"就安全了。** 错误信息可能仍进入响应头、日志接口、监控面板；要确保敏感细节不出网。
- **坑 3：只检查主域名安全头。** 子域、API 子域、静态资源 CDN 常被漏掉，而攻击者正是从最弱的那台下手。
- **坑 4：`X-Frame-Options: ALLOW-FROM` 已废弃。** 现代浏览器不支持，点击劫持防护应改用 CSP 的 `frame-ancestors`。
- **坑 5：CSP 里加 `unsafe-inline` 和 `unsafe-eval` 等于没加。** 只启用 `CSP: report-only` 而不真正拦截也一样。
- **坑 6：以为不用 DOCTYPE 就安全了。** XXE 也能通过 XInclude、SVG、DOCX/XLSX 等复合文档格式注入，要按"解析器"层面统一加固。
- **坑 7：默认凭据只查了登录页。** 中间件（Tomcat/Jenkins/Grafana/Kibana）、数据库、消息队列、缓存服务的默认口令往往才是真正的入口。

## 自测题

**1. 一个 REST API 在参数类型错误时返回 `{"error":"invalid input syntax for type integer: \"abc\" at character 42"}`。这属于哪类问题，危害是什么？**

<details><summary>答案</summary>

属于 A02（配置错误 / 错误信息过度）叠加 A10（异常条件处理不当）。它泄露了底层数据库类型（PostgreSQL）、SQL 解析细节与字符位置，为 SQL 注入提供情报。修复：对外返回通用错误，细节只进服务端日志。
</details>

**2. 攻击者在目标站点上成功读取 `/etc/passwd`，入口是一个上传头像的 XML 接口。这是哪类漏洞？关键修复点是什么？**

<details><summary>答案</summary>

XXE（XML 外部实体注入，CWE-611），归入 A02。关键修复：在 XML 解析器上禁用 DTD 与外部实体（`disallow-doctype-decl`、`external-general-entities=false` 等），并限制对外部资源的访问。
</details>

**3. 为什么"生产环境关闭了调试模式"仍可能不够？**

<details><summary>答案</summary>

因为调试能力可能通过其他方式残留：独立的 `/actuator`、`/debug` 端点、独立的调试端口、监控代理暴露的 `env`/`heapdump` 端点、源码 map 文件等。需要把"关闭调试"扩展为"移除一切非必要端点与能力"，并自动化校验。
</details>

**4. 应用设置了 `Access-Control-Allow-Origin: *` 且 `Access-Control-Allow-Credentials: true`。浏览器会允许跨域携带 Cookie 读取吗？**

<details><summary>答案</summary>

不会——规范禁止 `*` 与凭证同时生效，浏览器会拒绝该组合。但这属于错误的配置意图，且很多开发者会改成"反射任意 Origin"，那才是真正危险的（任意站点可携带用户凭证读取数据）。应使用精确的允许列表。
</details>

**5. 发现目标开启了目录列举，且 `/.git/` 可访问。攻击者能获得什么？**

<details><summary>答案</summary>

可下载整个 `.git` 仓库对象，重建完整历史源码，从中发现硬编码密钥、被删除但仍在历史中的凭据、内部接口与逻辑缺陷。应关闭目录列举并把 `.git` 排除在 Web 根目录外。
</details>

## 来源

- <https://top10.owasp.org/2025/A02_2025-Security_Misconfiguration/>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management/README>
- <https://cheatsheetseries.owasp.org/cheatsheets/Configuration_Cheat_Sheet.html>
- <https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html>
