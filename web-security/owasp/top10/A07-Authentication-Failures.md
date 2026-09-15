# A07:2025 认证失效（Authentication Failures）

> 官方详情页：<https://top10.owasp.org/2025/A07_2025-Authentication_Failures/>
> 排名：**第 7 位**（2021 版也是第 7 位，**改名**：原 "Identification and Authentication Failures" 识别与认证失效）
> CWE 数量：36 个｜平均发生率：2.92%｜相关 CVE：7,147
> 主要 CWE：CWE-259 硬编码口令、CWE-297 证书主机名校验不当、CWE-287 认证不当、CWE-384 会话固定、CWE-798 硬编码凭据

## 一句话理解

认证失效是**系统把一个不是合法用户的身份当成了合法用户**——通过弱口令、撞库、绕过认证逻辑、复用会话、错误信任令牌等手段。

## 风险原理

认证要回答"你是谁"。失效发生在三个环节：

1. **凭据本身弱或可枚举。** 默认口令、弱口令、泄露口令、可被爆破或撞库。
2. **认证逻辑可绕过。** 存在替代路径（备用接口、直接访问内部页、参数控制）、可捕获重放、信任客户端声明。
3. **认证后状态管理失败。** 会话标识不轮换、登出后不失效、令牌作用域/受众未校验。

2025 版改名是因为原名的 "Identification"（识别）部分与此类别的 36 个 CWE 不再匹配，新名字更准确。官方也指出：标准化的认证框架（如 OIDC、Passkey）的使用正在产生积极影响。

官方列出的脆弱点：允许撞库/混合撞库（密码喷洒，如 `Password1!`、`Password2!` 递增）、允许暴力破解且不快速阻断、允许默认/弱/知名口令、允许用已知泄露凭据注册、使用弱找回密码流程（知识问答）、明文/加密/弱哈希存储口令、MFA 缺失或无效、MFA 不可用时有弱回退、会话标识出现在 URL/隐藏字段等不安全位置、登录成功后复用同一会话标识、登出或超时后未正确失效会话/令牌（尤其 SSO）、未正确断言凭据的 scope 与 audience。

> 注意与 [A04 加密失效](A04-Cryptographic-Failures.md) 的边界：A07 关注"认证机制本身"，**口令的存储算法弱**归 A04，但"允许弱口令注册"归 A07。

ASCII 数据流图（密码喷洒/撞库）：

```
攻击者                    目标登录接口
  |-- admin / Password1! -->|  401
  |-- admin / Password2! -->|  401
  |-- admin / Password3! -->|  200  <-- 成功：弱口令 + 无锁定
  |
  |  （同一组泄露凭据横向尝试多个站点：撞库）
```

## 典型场景与真实案例模式

> 以下为"某类系统常见的模式"归纳，部分场景取自官方页面示例的抽象化。

- **撞库与密码喷洒。** 官方强调：攻击者会基于人类习惯"递增"口令（如把 `Winter2025` 改成 `Winter2026`，把 `ILoveMyDog6` 改成 `ILoveMyDog7`），这种"混合撞库/密码喷洒"比传统撞库更有效。若没有反自动化措施，登录接口就成了"口令预言机"。
- **默认口令未更改。** 管理后台、设备、数据库使用出厂默认账号口令。
- **认证绕过。** 通过备用路径（如 `/api/v2/`、移动端接口、`.json` 后缀、直接请求内部页）绕过认证检查。
- **会话固定（Session Fixation）。** 登录成功后不重新生成会话 ID，攻击者预先设定的会话 ID 在受害者登录后变为有效（CWE-384）。
- **会话超时未实现。** 官方示例：用户在公共电脑上直接关闭标签页而未登出；或 SSO 场景下只能单点登录却不能单点登出，导致用户以为已登出但其他应用仍保持认证。
- **MFA 有弱回退。** 提供"短信验证码"或"跳过 MFA"按钮作为回退，攻击者直接走回退路径。
- **JWT 未校验 `aud`/`iss`/scope。** 令牌本为服务 A 签发，却被用来访问服务 B。
- **账号枚举。** 登录/注册/找回密码返回不同消息（"用户不存在" vs "密码错误"），为攻击者提供有效用户名清单。

## 怎么测

对应 WSTG 测试项：

- [WSTG-ATHN-01](../wstg/checklist.md) 凭据是否通过加密通道传输
- [WSTG-ATHN-02](../wstg/checklist.md) 默认凭据
- [WSTG-ATHN-03](../wstg/checklist.md) 弱锁定机制
- [WSTG-ATHN-04](../wstg/checklist.md) 绕过认证模式
- [WSTG-ATHN-05](../wstg/checklist.md) 不安全的"记住密码"
- [WSTG-ATHN-06](../wstg/checklist.md) 浏览器缓存弱点
- [WSTG-ATHN-07](../wstg/checklist.md) 弱认证方法
- [WSTG-ATHN-08](../wstg/checklist.md) 弱安全问题答案
- [WSTG-ATHN-09](../wstg/checklist.md) 弱口令修改/重置功能
- [WSTG-ATHN-10](../wstg/checklist.md) 替代通道中的弱认证
- [WSTG-ATHN-11](../wstg/checklist.md) 多因素认证
- [WSTG-IDNT-04](../wstg/checklist.md) 账号枚举与可猜用户名
- [WSTG-IDNT-05](../wstg/checklist.md) 弱或未强制的用户名策略
- [WSTG-SESS-03](../wstg/checklist.md) 会话固定
- [WSTG-SESS-10](../wstg/checklist.md) JSON Web Token

**手工测试步骤**

1. **测试默认凭据。** 对登录页与管理后台尝试常见组合：
   ```
   admin/admin, admin/password, admin/admin123, root/root,
   administrator/password, test/test
   ```
2. **账号枚举。** 分别提交"存在的用户名 + 错口令"与"不存在的用户名 + 任意口令"，比较响应体、状态码、响应时间差异。
   ```bash
   curl -s -o /dev/null -w '%{http_code} %{time_total}\n' -X POST https://target/login -d 'u=admin&p=wrong'
   curl -s -o /dev/null -w '%{http_code} %{time_total}\n' -X POST https://target/login -d 'u=nosuchuser123&p=wrong'
   ```
   再对注册、找回密码流程做同样比较。
3. **测试锁定与限流。** 对同一账号/同一 IP 连续发送多次错误口令，观察是否锁定、延迟递增、出现验证码。
   ```bash
   for i in $(seq 1 15); do
     curl -s -o /dev/null -w "%{http_code}\n" -X POST https://target/login -d 'u=admin&p=wrong'$i
   done
   ```
   注意同时测试是否存在"通过大小写变化用户名、加空格、换 IP 头绕过锁定"。
4. **测试认证绕过。** 对已知需登录的页面尝试：
   ```
   直接访问 /admin、/dashboard
   加 .json / ; / %00 / ..;/ 等变形
   修改或删除 Authorization / Cookie 头
   伪造 X-Forwarded-For / X-Original-URL / X-Rewrite-URL
   ```
5. **测试会话固定。** 记录未登录时的会话 ID，登录后检查该 ID 是否变化（应变化）。
6. **测试登出与会话失效。** 登录后记录 Cookie，登出，再用旧 Cookie 请求受保护接口——应返回 401/403。
   ```bash
   curl -s -o /dev/null -w '%{http_code}\n' -H 'Cookie: session=<登出前的会话>' https://target/api/me
   ```
7. **测试 JWT。** 解码 payload，检查 `aud`、`iss`、`exp`、scope；尝试 `alg: none`、算法混淆（RS256→HS256）、篡改字段。
   ```bash
   echo '<jwt>' | cut -d. -f2 | base64 -d 2>/dev/null | jq
   ```
8. **测试 MFA。** 确认是否可关闭、是否有弱回退、验证码是否可爆破（多次尝试是否被限制）、是否有"记住设备"长期令牌可被窃取。
9. **测试"记住我"。** 检查持久化 Cookie 是否为可预测的序列值（可枚举）、是否可通过修改 Cookie 冒充他人。

## 代码示例

### 易受攻击的代码（PHP —— 弱口令策略 + 会话固定 + 账号枚举）

```php
<?php
session_start();

// 危险 1：登录成功后不重新生成会话 ID（会话固定）
$stmt = $pdo->prepare("SELECT id, password_hash FROM users WHERE username = ?");
$stmt->execute([$_POST['username']]);
$user = $stmt->fetch();

if (!$user) {
    // 危险 2：泄露"用户不存在"，可枚举账号
    exit("该用户名不存在");
}

if (!password_verify($_POST['password'], $user['password_hash'])) {
    exit("密码错误");
}

// 危险 3：没有失败计数、没有锁定、没有延迟 -> 可无限爆破
$_SESSION['uid'] = $user['id'];
// 危险 4：口令用 MD5 存储（同时违反 A04）
```

### 修复后的代码

```php
<?php
session_start();

const MAX_ATTEMPTS = 5;
const LOCK_SECONDS = 900;

function fail(string $key, PDO $pdo): void {
    $pdo->prepare("INSERT INTO login_attempts(k, created_at) VALUES(?, NOW())")->execute([$key]);
}

// 修复 1：以"账号+IP"做失败计数与锁定，且返回统一消息
$key = strtolower(trim($_POST['username'])) . '|' . $_SERVER['REMOTE_ADDR'];
$count = $pdo->prepare("SELECT COUNT(*) FROM login_attempts WHERE k=? AND created_at > NOW() - INTERVAL ? SECOND");
$count->execute([$key, LOCK_SECONDS]);
if ($count->fetchColumn() >= MAX_ATTEMPTS) {
    http_response_code(429);
    exit("尝试次数过多，请稍后再试");   // 不区分账号是否存在
}

$stmt = $pdo->prepare("SELECT id, password_hash FROM users WHERE username = ?");
$stmt->execute([$_POST['username']]);
$user = $stmt->fetch();

$genericError = "用户名或密码错误。";     // 修复 2：统一消息，杜绝账号枚举

if (!$user) {
    // 修复 3：即使账号不存在也执行一次哈希运算，抹平响应时间差异
    password_verify($_POST['password'], '$2y$12$invalidinvalidinvalidinvalidinvalidinvalidinvalidinva');
    fail($key, $pdo);
    exit($genericError);
}

if (!password_verify($_POST['password'], $user['password_hash'])) {
    fail($key, $pdo);
    exit($genericError);
}

// 修复 4：登录成功必须重新生成会话 ID（防会话固定）
session_regenerate_id(true);

// 修复 5：口令使用 password_hash()（bcrypt/Argon2），而非 MD5
if (password_needs_rehash($user['password_hash'], PASSWORD_ARGON2ID)) {
    $new = password_hash($_POST['password'], PASSWORD_ARGON2ID);
    $pdo->prepare("UPDATE users SET password_hash=? WHERE id=?")->execute([$new, $user['id']]);
}

$_SESSION['uid'] = $user['id'];
$_SESSION['created'] = time();
// 清理失败记录
$pdo->prepare("DELETE FROM login_attempts WHERE k=?")->execute([$key]);
```

### 登出与超时（通用要点）

```python
# 修复：登出必须在服务端销毁会话，而不只是删客户端 Cookie
@app.post("/logout")
@login_required
def logout():
    session_store.delete(request.session_id)   # 服务端撤销
    resp = jsonify(ok=True)
    resp.delete_cookie("session", path="/")
    return resp
```

## 防御清单

- [ ] 尽可能**强制多因素认证（MFA）**，抵御撞库、暴力破解与凭据复用。
- [ ] 鼓励使用密码管理器，帮助用户选择更强口令。
- [ ] **绝不**发布或部署默认凭据，尤其是管理员账号。
- [ ] 注册/改密时对**弱口令**做检查（如对比常见弱口令列表、检查是否泄露）。
- [ ] 对新账号与改密校验**已知泄露凭据**（如 haveibeenpwned 类服务）。
- [ ] 口令策略对齐 **NIST 800-63b 5.1.1**：不强制定期轮换（除非怀疑泄露）、不强制复杂度组合规则、要求足够长度。
- [ ] 注册、找回密码、API 通道统一消息，**防止账号枚举**。
- [ ] 失败尝试**限制或递增延迟**，同时防止自身造成 DoS；记录失败并告警。
- [ ] 使用服务端安全的会话管理器：登录后生成**高熵新会话 ID**，不放入 URL，存入安全 Cookie，登出/空闲/绝对超时后失效。
- [ ] 校验令牌的**预期用途**（JWT 校验 `aud`、`iss`、scope）。
- [ ] 优先购买使用成熟加固的认证/身份/会话系统（转移风险），而非自研。
- [ ] 参考 [Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)、[Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)、[Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)。

## 常见坑

- **坑 1：锁定机制反而成了 DoS 工具。** 只按"用户名"锁定，攻击者可用错误口令反复尝试他人的用户名使受害者被锁。应按"账号+IP"组合并递增延迟，或使用验证码。
- **坑 2：返回不同错误消息。** "用户名不存在"与"密码错误"的区分是最常见的账号枚举来源；找回密码、注册同样会泄露。
- **坑 3：只在前端做口令强度校验。** 攻击者直接调 API 注册弱口令。服务端必须独立校验。
- **坑 4：登录后不轮换会话 ID。** 这就是会话固定的根源，很多框架默认行为需要显式调用（如 `session_regenerate_id`）。
- **坑 5：登出只删客户端 Cookie。** 服务端会话仍有效，旧 Cookie 被窃取后依旧可重放。必须服务端撤销。
- **坑 6：JWT 校验不完整。** 只验签名不验 `exp`/`aud`/`iss`，或允许 `alg: none`、允许 HS/RS 混淆，均可导致认证被绕过。
- **坑 7：MFA 可被"回退"绕过。** 提供"跳过 MFA""改用短信"等选项时，攻击者会直奔最弱路径。
- **坑 8：一个加密通道不等于认证安全。** 强制 HTTPS 只解决传输窃听，不解决弱口令、爆破、会话固定。

## 自测题

**1. 某登录接口对不存在的用户名返回"该账号不存在"，对存在的用户名返回"密码错误"。这属于哪类问题？危害是什么？**

<details><summary>答案</summary>

账号枚举（WSTG-IDNT-04），归入 A07 认证失效。攻击者可批量枚举出系统中真实存在的用户名，为后续爆破/撞库/钓鱼提供精准目标。修复：所有失败情况返回统一消息（"用户名或密码错误"）与相近的响应时间。
</details>

**2. 用户登录成功后会话 ID 没有变化。这叫什么漏洞？攻击者如何利用？**

<details><summary>答案</summary>

会话固定（Session Fixation，CWE-384）。攻击者先访问站点获得一个会话 ID，再通过链接/诱骗让受害者在携带该 ID 的情况下登录；由于登录后 ID 不变，攻击者已知的这个 ID 现在就是受害者的有效会话，可直接接管。修复：登录成功时强制 `session_regenerate_id(true)` / 生成全新高熵会话 ID。
</details>

**3. 为什么"每 90 天强制用户改密码"现在被认为是不良实践？**

<details><summary>答案</summary>

NIST 800-63b 与官方指南都反对强制定期轮换：它鼓励用户选择可预测的变体（`Pass1` → `Pass2` → `Pass3`）并把口令记在便签上，实际降低安全性。正确做法是：不强制定期轮换，但一旦怀疑泄露立即强制重置，并配合 MFA、泄露凭据检测与长度要求。
</details>

**4. 应用的 JWT 由服务 A 签发，服务 B 只校验签名就接受。问题在哪？**

<details><summary>答案</summary>

服务 B 没有校验 `aud`（受众）与 `iss`（签发者）以及 scope。攻击者若能在任何由同一密钥签发的服务（或通过其他途径获得合法令牌）拿到令牌，就能用它访问服务 B，实现跨服务越权。修复：每个服务校验 `aud`/`iss`/`exp`/scope，并尽量让各服务使用独立的受众与密钥。
</details>

**5. 应用提供了 MFA，但同时在登录页有一个"暂时跳过两步验证"的链接。这算安全吗？**

<details><summary>答案</summary>

不算。任何弱回退都会成为攻击者的首选路径，使 MFA 形同虚设。若确实需要回退，应使用同等强度的替代因子（如备用一次性代码），并受同样的限流与告警约束，而不是简单跳过。
</details>

## 来源

- <https://top10.owasp.org/2025/A07_2025-Authentication_Failures/>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication/README>
- <https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html>
- <https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html>
