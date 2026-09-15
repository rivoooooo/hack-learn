# A08:2025 软件或数据完整性失效（Software or Data Integrity Failures）

> 官方详情页：<https://top10.owasp.org/2025/A08_2025-Software_or_Data_Integrity_Failures/>
> 排名：**第 8 位**（2021 版也是第 8 位，**改名**：原 "Software **and** Data Integrity Failures" → "Software **or** Data Integrity Failures"）
> CWE 数量：14 个｜平均发生率：2.75%｜相关 CVE：3,331
> 主要 CWE：CWE-829 从不信任控制域引入功能、CWE-915 动态确定对象属性的修改控制不当、CWE-502 不可信数据反序列化

## 一句话理解

软件或数据完整性失效是**在没有验证完整性/来源的前提下，就把代码或数据当成了可信的**——常用于不验签的自动更新、不校验的 CDN/插件引入、不安全反序列化、CI/CD 拉取未验证的制品。

## 风险原理

核心是**信任边界没有被维护**。当你假设"来自更新服务器的东西一定是官方的""这个序列化对象一定是自己生成的""这个前端库一定没被改"，攻击者只要污染这条链路，就能让恶意内容"合法地"被执行。

官方定义：涉及代码与基础设施**未防止无效或不可信的代码/数据被当作可信有效**。

与 [A03 软件供应链失效](A03-Software-Supply-Chain-Failures.md) 的分工（官方明确说明）：

- **A08 更底层**：聚焦"是否验证了软件、代码、数据制品的完整性"，即信任边界与完整性校验本身。
- **A03 更宏观**：整个供应链生态（依赖、构建系统、分发基础设施）的失效与妥协。

两者有交叠，但 A08 的观察视角是"签名、校验、序列化完整性"。

三类典型失效：

1. **从不信任控制域引入功能。** 应用依赖第三方插件、库、模块、CDN；DNS 映射把子域指向第三方，导致 Cookie 被第三方接收（CWE-829、CWE-830）。
2. **CI/CD 不校验制品。** 从不可信位置拉代码/制品且不验签，或不提供完整性校验（CWE-494）。
3. **不安全反序列化。** 把编码/序列化后的对象交给客户端，客户端可修改后回传，服务端反序列化即可能 RCE（CWE-502）。此外还有 CWE-915：批量把请求中的字段绑定到对象属性，导致攻击者能修改本不该改的属性。

ASCII 数据流图（不安全反序列化）：

```
服务端                     客户端（攻击者可控）
  |-- 序列化合法状态 (base64 rO0...) -->|
  |                                     | 篡改/构造恶意序列化数据
  |<-- 回传恶意对象 --------------------|
  | 反序列化（无校验）-> 触发 gadget chain -> RCE
```

## 典型场景与真实案例模式

> 以下为"某类系统常见的模式"归纳，部分场景取自官方页面示例的抽象化。

- **不验签的自动更新。** 官方示例：许多家用路由器、机顶盒、设备固件不通过签名验证更新，未签名固件成为攻击目标，且往往只能"在下一版本修复并等旧版本自然淘汰"，无法补救。
- **子域指向第三方导致 Cookie 泄露。** 官方示例：公司为方便把 `myCompany.SupportProvider.com` 映射到 `support.myCompany.com`，于是所有设在 `myCompany.com` 上的 Cookie（含认证 Cookie）都会发给支持服务商，任何能访问服务商基础设施的人都能窃取全部用户 Cookie 并劫持会话。
- **从不信任来源获取包。** 官方示例：开发者找不到某个包的更新版本，就从非官方包管理器之外的网站下载；该包未签名，无法验证完整性，内含恶意代码。
- **不安全反序列化导致 RCE。** 官方示例：某 React 应用调用一组 Spring Boot 微服务，为实现"不可变"而把用户状态序列化后在请求间来回传递。攻击者注意到 base64 中 `rO0` 的 Java 对象签名，用 Java Deserialization Scanner 取得远程代码执行。
- **CI/CD 拉取未验证制品。** 流水线从外部仓库/URL 拉取构建产物且不校验签名，攻击者替换该产物即污染全部下游。
- **CDN/前端库被篡改。** 直接引用第三方 CDN 脚本且不校验 SRI（子资源完整性），CDN 被入侵即全站被注入。

## 怎么测

对应 WSTG 测试项（部分需结合代码审计与流程审计）：

- [WSTG-INPV-23](../wstg/checklist.md) 不安全反序列化
- [WSTG-INPV-20](../wstg/checklist.md) 批量赋值（Mass Assignment）
- [WSTG-CONF-10](../wstg/checklist.md) 子域名接管
- [WSTG-CONF-11](../wstg/checklist.md) 云存储
- [WSTG-SESS-02](../wstg/checklist.md) Cookie 属性
- [WSTG-CLNT-13](../wstg/checklist.md) 跨站脚本包含（XSSI）

**手工测试步骤**

1. **寻找序列化数据。** 在 Cookie、隐藏字段、请求体、URL 中寻找序列化特征：
   - Java：base64 解码后以 `rO0AB`（`0xACED0005`）开头，或原始二进制以 `AC ED 00 05` 开头。
   - PHP：`O:8:"stdClass":...` 形式。
   - Python pickle：以 `\x80\x04` 开头的字节串。
   - .NET：`AAEAAAD/////`（base64）或 `BinaryFormatter` 特征。
   ```bash
   # 示例：检查 Cookie 是否含 Java 序列化对象
   echo '<base64值>' | base64 -d 2>/dev/null | xxd | head
   ```
2. **篡改并回传。** 对反序列化数据做无害测试：修改一个字段值，观察是否被接受以及是否触发异常堆栈（堆栈会暴露类名，便于构造 gadget chain）。
3. **测试批量赋值（Mass Assignment）。** 在正常请求中额外加入敏感字段，观察是否被绑定：
   ```bash
   curl -X PUT https://target/api/profile -H 'Content-Type: application/json' \
     -d '{"name":"x","role":"admin","isVerified":true,"balance":999999}'
   ```
   然后再次查询确认属性是否真的被修改。
4. **检查子资源完整性（SRI）。** 查看页面引用的第三方脚本是否带 `integrity` 属性。
   ```bash
   curl -s https://target/ | grep -oE '<script[^>]*src="https?://[^"]+"[^>]*>'
   ```
   缺少 `integrity="sha384-..."` 即为风险。
5. **检查第三方子域与 Cookie 作用域。** 列出所有子域，确认是否有指向第三方的 CNAME；检查认证 Cookie 是否设在过宽的父域（如 `.example.com`）。
   ```bash
   dig +short CNAME support.target.com
   curl -sI https://target/login | grep -i set-cookie
   ```
6. **审计自动更新机制。** 更新包是否验签？更新服务器是否可被劫持？是否有回滚保护？
7. **审计 CI/CD 制品完整性。** 制品是否有签名与来源证明？是否校验下载物的哈希/签名后再使用？
8. **使用工具辅助。** 对 Java 应用可用 `ysoserial` 生成测试载荷（**仅在授权靶场**），对 .NET 可用 `ysoserial.net`。

## 代码示例

### 易受攻击的代码（Python —— 不安全反序列化）

```python
import pickle
from flask import Flask, request, make_response

app = Flask(__name__)

@app.post("/save")
def save_state():
    user_state = {"cart": request.json["cart"], "theme": request.json["theme"]}
    # 危险：pickle 序列化后交给客户端保存
    token = pickle.dumps(user_state)
    resp = make_response("ok")
    resp.set_cookie("state", token.hex())
    return resp

@app.get("/load")
def load_state():
    # 危险：直接反序列化客户端回传数据 —— 可导致远程代码执行
    state = pickle.loads(bytes.fromhex(request.cookies["state"]))
    return {"state": state}
```

```python
import itsdangerous
from flask import Flask, request, make_response, abort

app = Flask(__name__)
signer = itsdangerous.URLSafeSerializer(app.config["STATE_SECRET"])   # 密钥来自 KMS/环境

@app.post("/save")
def save_state():
    # 修复 A：改用安全的 JSON + HMAC 签名，且不反序列化任意对象
    payload = {"cart": request.json["cart"], "theme": request.json["theme"]}
    token = signer.dumps(payload)          # 自带完整性校验
    resp = make_response("ok")
    resp.set_cookie("state", token, secure=True, httponly=True, samesite="Lax")
    return resp

@app.get("/load")
def load_state():
    try:
        # 修复 B：验签失败直接拒绝；只解析为 JSON 基础类型
        state = signer.loads(request.cookies["state"])
    except itsdangerous.BadSignature:
        abort(400, "invalid state")
    return {"state": state}
```

### 易受攻击的代码（Node.js —— 批量赋值）

```js
// 危险：直接把请求体整体赋给数据模型，攻击者可覆盖 role / balance
app.put('/api/user/:id', async (req, res) => {
  const user = await User.findByPk(req.params.id);
  await user.update(req.body);          // req.body 可含 role: "admin"
  res.json(user);
});
```

```js
// 修复：显式白名单字段，其余一律忽略
const EDITABLE_FIELDS = ['displayName', 'avatarUrl', 'locale'];

app.put('/api/user/:id', requireSelfOrAdmin, async (req, res) => {
  const user = await User.findByPk(req.params.id);
  const updates = {};
  for (const f of EDITABLE_FIELDS) {
    if (Object.prototype.hasOwnProperty.call(req.body, f)) updates[f] = req.body[f];
  }
  // 显式校验：任何试图修改非白名单字段的请求都应被拒绝并记录
  const unexpected = Object.keys(req.body).filter(k => !EDITABLE_FIELDS.includes(k));
  if (unexpected.length) {
    req.log.warn({ uid: req.user.id, unexpected }, 'mass assignment attempt');
    return res.status(400).json({ error: 'unexpected fields', unexpected });
  }
  await user.update(updates);
  res.json(user);
});
```

### 子资源完整性（HTML）

```html
<!-- 危险：引用第三方 CDN 脚本但不校验完整性 -->
<script src="https://cdn.example.com/lib.js"></script>
```

```html
<!-- 修复：添加 SRI，浏览器会在完整性不匹配时拒绝执行 -->
<script src="https://cdn.example.com/lib.js"
        integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
        crossorigin="anonymous"></script>
```

## 防御清单

- [ ] 用**数字签名**或类似机制验证软件/数据来自预期来源且未被篡改。
- [ ] 库与依赖只从可信仓库消费；高风险场景使用内部 vetted 仓库（npm/Maven 代理）。
- [ ] 对代码与配置变更建立**审查流程**，避免恶意代码进入流水线。
- [ ] CI/CD 流水线做好隔离、配置与访问控制，保证流经的代码完整性。
- [ ] **绝不**接收来自不可信客户端的未签名/未加密序列化数据；必须时先做完整性或签名校验。
- [ ] 序列化优先使用**只含数据的格式**（JSON）而非能执行构造函数的格式（pickle、Java 原生序列化、BinaryFormatter）。
- [ ] 前端第三方脚本使用 **SRI（子资源完整性）**。
- [ ] 认证 Cookie 不要放在过宽的父域上，避免被第三方子域接收。
- [ ] 自动更新必须验签，并考虑防降级/回滚保护。
- [ ] 接口采用**字段白名单**绑定，禁止把请求体整体赋给模型（防 CWE-915 批量赋值）。
- [ ] 参考 [Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)、[Software Supply Chain Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html)、[Infrastructure as Code Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html)。

## 常见坑

- **坑 1：把"客户端回传的状态"当作可信。** 任何经过客户端往返的数据都必须视为不可信，必须签名或服务端存储。
- **坑 2：以为"数据是 base64 的"就安全。** Base64 是编码不是加密，也不提供完整性。攻击者可随意解码、修改、重新编码。
- **坑 3：依赖 JSON 就一定安全。** JSON 本身比 pickle 安全，但若反序列化后直接做**批量属性绑定**（如把 JSON 映射到 ORM 对象），仍会引入 CWE-915。
- **坑 4：SRI 只加在部分脚本上。** 任何一个未加 SRI 的第三方脚本都是突破口；动态注入的脚本 SRI 也需通过 `integrity` 属性显式设置。
- **坑 5：只对"下载的包"验签，忘了构建产物。** 中间产物与最终制品同样需要完整性保护。
- **坑 6：Cookie 域设得过宽。** `Domain=.example.com` 会让所有子域（包括第三方托管子域）都能收到认证 Cookie。
- **坑 7：自动更新不防降级。** 只验签不校验版本，攻击者可用旧版有漏洞但签名有效的固件实施降级攻击。

## 自测题

**1. 在请求体里发现一个字段的值 base64 解码后以 `rO0AB` 开头。这说明什么？可能有什么风险？**

<details><summary>答案</summary>

这是 Java 原生序列化对象的特征（魔数 `0xACED0005`）。若服务端会对客户端可控的该数据做反序列化，攻击者可构造 gadget chain 实现远程代码执行（CWE-502），归入 A08。修复：不使用 Java 原生序列化承载客户端数据，改用 JSON + 签名。
</details>

**2. 应用把用户状态用 `pickle` 序列化后放进 Cookie，用普通 Base64 编码，不签名。攻击者能做什么？**

<details><summary>答案</summary>

可解码 Cookie、构造恶意 pickle 载荷、重新编码后发送。`pickle.loads` 会执行对象构造逻辑，攻击者可借 `__reduce__` 执行任意命令，取得远程代码执行。修复：改用 JSON 承载状态并加 HMAC 签名，或把状态存服务端。
</details>

**3. 什么是"批量赋值（Mass Assignment）"，它为什么归 A08 而不是 A01？**

<details><summary>答案</summary>

批量赋值指框架把请求参数自动绑定到对象属性，攻击者通过多传字段（如 `role=admin`、`balance=999999`）修改本不该修改的属性。它归 A08 的原因是其根因是"未验证就信任来自客户端的数据/属性声明"，属于完整性失效（CWE-915）；虽然后果常表现为越权（A01），但根因层在 A08。修复：字段白名单绑定。
</details>

**4. 公司把 `support.company.com` CNAME 到一个第三方客服 SaaS。为什么这会导致认证 Cookie 泄露？**

<details><summary>答案</summary>

因为认证 Cookie 常设在父域 `.company.com` 上，浏览器会把该 Cookie 发送给所有 `*.company.com` 子域，包括指向第三方的 `support.company.com`。第三方（或其被攻陷的基础设施）即可获取所有用户的认证 Cookie。修复：把认证 Cookie 限定在具体主机（不设宽 Domain），并谨慎规划第三方子域。
</details>

**5. 为什么"给第三方 CDN 脚本加 SRI"能提高安全性？**

<details><summary>答案</summary>

SRI（子资源完整性）让浏览器在加载脚本前计算其哈希并与 `integrity` 属性比对，不匹配则拒绝执行。这样即使 CDN 被入侵或脚本被中间人替换，篡改后的脚本也不会执行。注意它需要配合 `crossorigin` 且无法防御"CDN 提供合法但含漏洞的旧版本"这类问题。
</details>

## 来源

- <https://top10.owasp.org/2025/A08_2025-Software_or_Data_Integrity_Failures/>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Injection/README>
- <https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html>
- <https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html>
