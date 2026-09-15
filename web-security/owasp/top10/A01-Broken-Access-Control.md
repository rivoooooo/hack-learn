# A01:2025 失效的访问控制（Broken Access Control）

> 官方详情页：<https://top10.owasp.org/2025/A01_2025-Broken_Access_Control/>
> 排名：**第 1 位**（2021 版也是第 1 位）
> CWE 数量：40 个（本版上限）｜平均发生率：约 3.74%｜相关 CVE：32,654

## 一句话理解

访问控制（Access Control）负责"谁能对什么做什么"，而失效的访问控制就是**服务端没有真正检查这个权限**——攻击者只要改一个 ID、改一个 URL、改一个请求体，就能读写本不该碰的数据。

## 风险原理

访问控制的核心错误只有一个：**把权限判断放在了攻击者能控制的地方，或者干脆忘了判断。**

正确的模型是"默认拒绝（deny by default）"：除公开资源外，一切访问都要显式授权。常见失效形式：

1. **只在前端做控制。** 按钮藏起来了，但对应的 API 没有校验。
2. **信任客户端提交的标识。** 用 URL 参数里的 `acct=xxx`、`orderId=xxx` 直接查库，不校验归属。
3. **越权链路缺失。** 列表接口校验了，详情/导出/删除接口忘了校验。
4. **元数据可篡改。** 用未验签的 JWT 声明、Cookie 里的 `role=admin`、隐藏表单字段来决定权限。
5. **CORS 配置过宽。** 允许任意 Origin 携带凭证，等于把跨域读取权送给了攻击者。
6. **目录列举 / 强制浏览。** 直接猜 URL 访问到未链接的管理页或备份文件。

> **2025 版重要变化：SSRF 并入本类别。** 服务端请求伪造（Server-Side Request Forgery，SSRF，CWE-918）在 2021 版是独立类别，2025 版归入 A01。原因是 SSRF 本质是"服务端被诱导去访问它本不该访问的资源"，属于访问控制边界被突破。本类别还纳入了传统上属于"会话/数据泄露"的 CWE-200、CWE-201、CWE-352（CSRF）、CWE-601（开放重定向）等。

ASCII 数据流图（水平越权 / IDOR）：

```
攻击者浏览器                 Web 服务器                    数据库
     |                          |                            |
     |-- GET /api/order/1001 -->|                            |
     |                          |-- SELECT * FROM orders --->|
     |                          |      WHERE id=1001         |
     |                          |      -- 没有 AND user_id=? |
     |                          |<-- 返回 1001 号订单内容 ----|
     |<-- 200 OK（他人的订单）---|                            |
     |                          |                            |
     |-- GET /api/order/1002 -->|  （改一个数字即可遍历）      |
```

## 典型场景与真实案例模式

> 以下为"某类系统常见的模式"归纳，不指向任何具体厂商事件。

- **电商/外卖类系统的订单接口。** 列表页做了归属过滤，但 `GET /orders/{id}` 详情接口只按主键查询。
- **SaaS 多租户后台。** 前端根据 `tenant_id` 隐藏菜单，后端接口不校验 `tenant_id`，导致跨租户读写（横向越权）。
- **企业管理系统。** `/admin` 目录做了 Basic 认证保护，但 `/admin/api/*` 的代理路径未纳入同一条规则，直接访问即可绕过（强制浏览）。
- **文件下载服务。** 下载接口用文件名拼接路径 `download?file=../../etc/passwd`，既越权又路径穿越（path traversal，CWE-22）。
- **开放平台/回调白名单。** 只对跳转域名做前缀匹配，`https://trusted.com.evil.com` 被误判为可信，形成开放重定向（CWE-601）。
- **内部服务。** 上传图片时接受远程 URL，服务端直接去拉取该 URL（SSRF，CWE-918），可用来探测内网、读取云元数据服务。

## 怎么测

对应 WSTG 测试项：

- [WSTG-ATHZ-01](../wstg/checklist.md) 目录穿越与文件包含测试
- [WSTG-ATHZ-02](../wstg/checklist.md) 绕过授权模式
- [WSTG-ATHZ-03](../wstg/checklist.md) 权限提升
- [WSTG-ATHZ-04](../wstg/checklist.md) 不安全的直接对象引用（IDOR）
- [WSTG-ATHZ-05](../wstg/checklist.md) OAuth 弱点
- [WSTG-IDNT-01](../wstg/checklist.md) 角色定义审查
- [WSTG-APIT-02](../wstg/checklist.md) API 对象级授权失效
- [WSTG-APIT-04](../wstg/checklist.md) API 功能级授权失效
- [WSTG-INPV-19](../wstg/checklist.md) SSRF

**手工测试步骤（准备两个账号 A、B，A 为普通用户，如有条件再准备管理员）**

1. **枚举所有资源标识符。** 登录 A，浏览一遍应用，用代理工具（Burp/ZAP）记录所有出现数字 ID、UUID、文件名的请求。
2. **水平越权（IDOR）**：把 A 的请求里的 ID 换成 B 的 ID，重放，观察是否返回 B 的数据。
   ```bash
   curl -s -H "Cookie: session=<A的会话>" https://target/api/order/1002
   ```
3. **垂直越权**：用 A 的会话访问管理接口。
   ```bash
   curl -s -o /dev/null -w "%{http_code}\n" -H "Cookie: session=<A的会话>" https://target/admin/users
   # 返回 200 且非登录页 = 缺陷
   ```
4. **HTTP 方法绕过**：如果 `POST /admin/action` 返回 403，试 `GET`、`PUT`、`PATCH`、`DELETE`，以及加 `X-HTTP-Method-Override` 头。
5. **路径/大小写/编码绕过**：
   ```
   /admin        -> 403
   /admin/       -> 200?
   /Admin        -> 200?
   /%61dmin      -> 200?
   /admin/..;/admin/ -> 200?
   ```
6. **JWT 元数据篡改**：把 JWT 用 `base64url` 解出 payload，改 `role`、`sub`、`tenant` 后重新编码（不改签名）观察是否被接受；再试 `alg: none` 与 HS/RS 混淆。
7. **SSRF**：对任何"填 URL"的功能（头像导入、Webhook、PDF 生成、图片代理）提交内部地址：
   ```
   http://127.0.0.1:8080/
   http://169.254.169.254/latest/meta-data/     # 云元数据
   http://[::1]/
   http://0x7f000001/                            # 十六进制绕过
   ```
8. **强制浏览**：用目录爆破（如 `ffuf`）探测未链接路径，并检查 `.git/`、`.svn/`、`backup.zip`、`*.bak`、`*.old`。
   ```bash
   ffuf -u https://target/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt -mc all -fc 404
   ```

## 代码示例

### 易受攻击的代码（Python / Flask）

```python
from flask import Flask, request, jsonify
from db import query

app = Flask(__name__)

@app.get("/api/order/<int:order_id>")
def get_order(order_id):
    # 危险：只按主键查，没有校验订单归属当前用户
    row = query("SELECT * FROM orders WHERE id = %s", (order_id,))
    return jsonify(row)

@app.get("/api/admin/users")
def admin_users():
    # 危险：只在模板里隐藏了菜单，接口完全没有角色校验
    return jsonify(query("SELECT id, email, role FROM users", None))
```

### 修复后的代码

```python
from functools import wraps
from flask import Flask, request, jsonify, abort
from db import query

app = Flask(__name__)

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        user = get_current_user()          # 由服务端会话派生，绝不来自请求参数
        if not user:
            abort(401)
        request.user = user
        return f(*args, **kwargs)
    return wrapper

def require_role(role):
    def deco(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if request.user["role"] != role:   # 服务端再次校验角色
                abort(403, "Forbidden")
            return f(*args, **kwargs)
        return wrapper
    return deco

@app.get("/api/order/<int:order_id>")
@login_required
def get_order(order_id):
    # 关键修复：把归属条件写进 WHERE，让数据库层保证越权不可见
    row = query(
        "SELECT * FROM orders WHERE id = %s AND user_id = %s",
        (order_id, request.user["id"]),
    )
    if row is None:
        abort(404)        # 返回 404 而非 403，避免泄露"该资源存在"
    return jsonify(row)

@app.get("/api/admin/users")
@login_required
@require_role("admin")
def admin_users():
    return jsonify(query("SELECT id, email, role FROM users", None))
```

> 修复要点：**访问控制必须落在服务端**；归属校验写进查询条件；统一的装饰器/中间件集中实现，避免"某个接口忘了加"。

### SSRF 的修复（Node.js / Express）

```js
// 危险：直接请求用户提供的 URL
app.post('/fetch', async (req, res) => {
  const r = await fetch(req.body.url);
  res.send(await r.text());
});
```

```js
// 修复：协议白名单 + 域名白名单 + 解析后校验 IP，禁止内网与元数据地址
const { URL } = require('url');
const dns = require('dns').promises;
const net = require('net');
const ipaddr = require('ipaddr.js');

const ALLOWED_HOSTS = new Set(['cdn.example.com', 'images.example.com']);

function isPrivate(ip) {
  const addr = ipaddr.parse(ip);
  return ['private', 'loopback', 'linkLocal', 'uniqueLocal', 'unspecified'].includes(
    addr.range()
  );
}

app.post('/fetch', async (req, res) => {
  const u = new URL(req.body.url);
  if (u.protocol !== 'https:' || !ALLOWED_HOSTS.has(u.hostname)) {
    return res.status(400).send('blocked');
  }
  // 关键：解析后再校验真实 IP，防止 DNS rebinding
  const { address } = await dns.lookup(u.hostname);
  if (isPrivate(address)) return res.status(400).send('blocked');

  // 仍建议：禁用重定向、设置超时、限制响应体大小
  const r = await fetch(u, { redirect: 'error', signal: AbortSignal.timeout(3000) });
  res.send(await r.text());
});
```

## 防御清单

- [ ] 除公开资源外，**默认拒绝**；权限检查写在服务端可信代码里。
- [ ] 访问控制机制**在一个地方实现、全局复用**，不要每个接口手写一遍。
- [ ] 按"记录归属"而非"记录 ID"建模：`WHERE owner_id = current_user`。
- [ ] 所有 API 方法（GET/POST/PUT/PATCH/DELETE）都做功能级授权检查。
- [ ] 关闭 Web 服务器目录列举，确保 `.git`、`.env`、备份文件不在 Web 根目录下。
- [ ] 记录访问控制失败并告警（尤其重复失败）。
- [ ] 对 API 和控制器访问实施限流，增加自动化遍历成本。
- [ ] 登出后服务端使会话标识失效；无状态 JWT 设置短过期时间，长生命周期用 refresh token + 撤销机制。
- [ ] CORS 尽量最小化，不使用 `Access-Control-Allow-Origin: *` 搭配携带凭证。
- [ ] 对出站请求（SSRF 面）使用允许列表、协议与端口白名单，禁止访问内网与元数据地址。
- [ ] 把访问控制写进单元测试与集成测试。
- [ ] 参考 [Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) 与 [SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)。

## 常见坑

- **坑 1：前端隐藏 ≠ 访问控制。** 攻击者直接用 `curl` 调接口，前端代码一行都不执行。任何"JS 里判断了角色"都不算防护。
- **坑 2：只在列表接口校验。** 详情、搜索、导出、批量操作、WebSocket 推送都是常见漏网接口。
- **坑 3：用"不可预测的 ID"当访问控制。** UUID 只是增加难度，不是授权。UUID 会通过分享链接、日志、导出文件泄露。
- **坑 4：先查后改的竞态（TOCTOU）。** 先 `SELECT` 校验归属，再 `UPDATE`，两条语句之间资源可能被换主。应把校验与操作放进同一条带条件的语句。
- **坑 5：返回 403 泄露资源存在性。** 在 IDOR 场景中，若"存在但无权限"返回 403、"不存在"返回 404，攻击者可据此枚举资源。统一返回 404 更安全。
- **坑 6：只挡 `127.0.0.1` 的 SSRF 黑名单。** 必须做**解析后 IP 校验**，因为 `127.1`、`0x7f000001`、`[::1]`、`2130706433`、DNS rebinding 都能绕过字符串黑名单。
- **坑 7：CORS 只校验 Host 是否"包含"白名单域名。** `evil-trusted.com` 会匹配 `trusted.com`，必须做精确域名匹配或正则锚定。

## 自测题

**1. 某接口 `GET /api/invoice/{id}` 在收到不属于当前用户的 ID 时返回 403，收到不存在的 ID 时返回 404。这有什么问题？**

<details><summary>答案</summary>

可以据此枚举系统中存在哪些发票 ID（区分"存在但无权"与"不存在"）。修复方式是两种情况统一返回 404，或统一返回一个不泄露存在性的错误。
</details>

**2. 应用在 JWT 的 payload 里放了 `{"role":"user"}`，服务端读取该字段决定权限，但没有校验签名。攻击者能做什么？**

<details><summary>答案</summary>

可以把 `role` 改成 `admin` 后重新 base64url 编码并原样发送，服务端仍会信任该字段，实现垂直越权。修复：必须验签，且授权信息不应只依赖客户端可读的声明；敏感操作要回源校验。
</details>

**3. 为什么"用 UUID 代替自增 ID"不能算作访问控制措施？**

<details><summary>答案</summary>

UUID 只是降低了猜解概率（"隐蔽式安全"），不是授权。UUID 会通过邮件链接、分享链接、日志、导出文件、第三方集成泄露。正确的做法是服务端按归属校验。
</details>

**4. 下面这条出处防 SSRF 的判断哪里不足？`if (url.startsWith("http://127.0.0.1")) reject();`**

<details><summary>答案</summary>

字符串前缀黑名单极易绕过：`http://127.0.0.1.evil.com`、`http://127.1/`、`http://0x7f000001/`、`http://2130706433/`、`http://[::1]/`、DNS rebinding 均可行。正确做法是解析域名后对**真实 IP** 做内网范围判断，并使用允许列表。
</details>

**5. 攻击者把 `POST /api/admin/deleteUser` 的 403 通过改成 `GET` 变成 200；这说明服务端犯了什么错误？**

<details><summary>答案</summary>

说明授权规则是按"路径"而非"方法+路径"配置的，或者框架的方法级安全配置不完整（本例中 `GET` 方法漏了授权）。修复：所有 HTTP 方法统一走同一套授权中间件，或显式禁止未使用的方法。
</details>

## 来源

- <https://top10.owasp.org/2025/A01_2025-Broken_Access_Control/>
- <https://owasp.org/Top10/2025/>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization/README>
- <https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html>
