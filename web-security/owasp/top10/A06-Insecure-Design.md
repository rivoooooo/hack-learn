# A06:2025 不安全设计（Insecure Design）

> 官方详情页：<https://top10.owasp.org/2025/A06_2025-Insecure_Design/>
> 排名：**第 6 位**（2021 版为第 4 位，**下降 2 位**）
> CWE 数量：39 个｜平均发生率：1.86%（全榜最低之一）｜相关 CVE：7,647
> 主要 CWE：CWE-256 凭据保护不当、CWE-269 权限管理不当、CWE-434 危险类型文件上传无限制、CWE-501 信任边界违反、CWE-522 凭据保护不足

## 一句话理解

不安全设计是**缺失或无效的"控制设计"**——不是代码写错了，而是从一开始就没设计出能抵御该类攻击的机制。**再完美的实现也救不了缺失的设计。**

## 风险原理

官方明确区分两件事：

- **不安全设计（design flaw，设计缺陷）**：缺少必要的安全控制。例如"加购物车"流程根本没有设计防刷机制。
- **不安全实现（implementation defect，实现缺陷）**：控制设计了，但代码写错了。例如设计了限流但限流条件写反了。

两者的**根因、发生阶段、修复方式都不同**：设计缺陷必须在需求与设计阶段修，实现缺陷在编码阶段修。这是本类别独立成类的理由。

官方给出的三个关键组成部分：

1. **需求与资源管理。** 与业务方共同确定保护需求（机密性、完整性、可用性、真实性），明确暴露面、是否需要租户隔离，并规划安全设计与测试的预算。
2. **安全设计。** 一种持续评估威胁的文化与方法论；把威胁建模融入需求梳理会议（refinement session），关注数据流与访问控制的变化；明确定义**正常流与失败流**并取得相关方确认。
3. **安全开发生命周期（SDL）。** 安全设计模式、铺好的路（paved road）、安全组件库、恰当工具、威胁建模，以及用于改进流程的事故复盘。

官方特别提到"左移（shift-left）"还不够——要**进一步左移到编码之前的需求与设计阶段**（Secure by Design）。

ASCII 数据流图（设计缺陷 vs 实现缺陷）：

```
不安全设计：
  需求: "用户可以领优惠券"          <-- 从未定义"同一用户能领几次"
  -> 实现再完美，也挡不住无限领取（业务逻辑漏洞）

不安全实现：
  需求: "同一用户最多领 1 次"
  设计: 领券前查询已领次数
  实现: if (count > 1) reject;     <-- 边界写错，实际允许 2 次
```

## 典型场景与真实案例模式

> 以下为"某类系统常见的模式"归纳，部分场景取自官方页面示例的抽象化描述。

- **基于"知识问答"的找回密码。** 官方明确指出：安全问题答案不能作为身份证据（多人都可能知道答案），这被 NIST 800-63b 与 ASVS 禁止。属于典型的设计缺陷，应整体移除并改为更安全的方案。
- **业务量折扣被滥用。** 官方示例：某影院允许团体折扣且满 15 人需付定金——攻击者按业务流程建模后，用几个请求一次性预订 600 个座位，造成收入损失。
- **无防机器人的抢购场景。** 官方示例：电商未防黄牛脚本，导致高端显卡被批量抢购转售，引发公关危机与用户不满。正确做法是设计时加入反机器人机制与领域规则（如"上架后数秒内完成的购买视为异常"）。
- **无限制文件上传。** 允许上传任意类型文件且不做内容校验，攻击者可上传 Web Shell（CWE-434）。这是设计阶段就该定的"允许列表"缺失。
- **信任边界违反。** 把客户端传入的 `price`、`isAdmin`、`userId` 当作可信（CWE-501、CWE-472）。
- **凭据保护不足。** 设计时选择把凭据明文或弱加密存放（CWE-256、CWE-522）。
- **无租户隔离设计。** 多租户系统只靠应用层 `WHERE tenant_id=?`，而没有在设计上做数据隔离（CWE-653 隔离不足）。
- **流程可被跳过。** 多步审批流没有服务端状态机约束，攻击者直接跳到"已批准"状态（对应 WSTG-BUSL-06）。

## 怎么测

不安全设计很难用工具自动发现，主要靠**业务流程分析 + 威胁建模 + 手工逻辑测试**：

- [WSTG-BUSL-01](../wstg/checklist.md) 业务逻辑数据校验
- [WSTG-BUSL-02](../wstg/checklist.md) 伪造请求的能力
- [WSTG-BUSL-03](../wstg/checklist.md) 完整性校验
- [WSTG-BUSL-05](../wstg/checklist.md) 功能使用次数限制
- [WSTG-BUSL-06](../wstg/checklist.md) 绕过工作流
- [WSTG-BUSL-07](../wstg/checklist.md) 应用滥用防护
- [WSTG-BUSL-08](../wstg/checklist.md) 上传意外文件类型
- [WSTG-BUSL-10](../wstg/checklist.md) 支付功能
- [WSTG-IDNT-02](../wstg/checklist.md) 用户注册流程
- [WSTG-IDNT-03](../wstg/checklist.md) 账号开通流程

**手工测试步骤**

1. **画出正常流程与失败流。** 对每个关键流程（注册、下单、支付、退款、改密、邀请、领券），手动画出状态机，标出每个状态的进入条件。
2. **测试"跳过步骤"。** 直接请求最后一步的接口，看服务端是否校验前置状态：
   ```bash
   # 正常：POST /order -> POST /pay -> POST /confirm
   # 攻击：直接
   curl -X POST -H 'Cookie: session=<s>' https://target/api/order/confirm -d 'orderId=123'
   ```
3. **测试"重复执行"。** 对同一操作连续调用，观察是否有幂等性或次数限制：
   ```bash
   for i in $(seq 1 20); do
     curl -s -H 'Cookie: session=<s>' -X POST https://target/api/coupon/claim -d 'code=WELCOME'
   done
   ```
4. **测试"数量/边界"。** 提交负数、超大值、超出业务上限的值：
   ```
   quantity=-1
   quantity=0
   quantity=999999
   price=0.01
   ```
5. **测试竞态条件（race condition）。** 并发发送同一请求，看能否绕过"仅一次"限制：
   ```bash
   # 使用并发工具同时发送 N 个请求
   seq 1 20 | xargs -P 20 -I{} curl -s -o /dev/null -w '%{http_code}\n' \
     -H 'Cookie: session=<s>' -X POST https://target/api/withdraw -d 'amount=100'
   ```
6. **测试支付逻辑。** 修改金额、币种、数量、优惠券叠加，观察服务端是否信任客户端提交的价格。
7. **测试上传限制。** 上传不在允许列表中的类型/双扩展名/内容与扩展名不符的文件：
   ```
   shell.php
   shell.php.jpg
   shell.jpg（内容为 PHP 代码，Magic Bytes 伪装为 JPEG）
   ```
8. **对找回密码做设计审查。** 若流程基于"知识问答"，本身就是设计缺陷——不要只测答案能否猜中。

## 代码示例

### 易受攻击的代码（Node.js —— 信任客户端提交的价格与权限）

```js
// 危险：价格、折扣、角色全部来自客户端请求体，且没有服务端校验业务规则
app.post('/api/order', async (req, res) => {
  const { productId, quantity, price, couponCode, isVip } = req.body;

  const total = price * quantity;
  const finalTotal = isVip ? total * 0.5 : total;   // 客户端说自己是 VIP 就打 5 折

  await db.order.create({ data: { productId, quantity, finalTotal, couponCode } });
  res.json({ ok: true, finalTotal });
});
```

```js
// 危险：多步退款流程可被直接跳到"已退款"状态
app.post('/api/refund/approve', async (req, res) => {
  await db.refund.update({ where: { id: req.body.id }, data: { status: 'APPROVED' } });
  res.json({ ok: true });
});
```

### 修复后的代码（服务端权威 + 状态机 + 幂等）

```js
// 修复 1：价格由服务端权威数据计算；VIP 身份取自会话，不取自请求体
app.post('/api/order', async (req, res) => {
  const { productId, quantity, couponCode } = req.body;

  // 正向校验业务边界
  if (!Number.isInteger(quantity) || quantity < 1 || quantity > 99) {
    return res.status(400).json({ error: 'invalid quantity' });
  }

  const product = await db.product.findUnique({ where: { id: productId } });
  if (!product || !product.onSale) return res.status(400).json({ error: 'unavailable' });

  let total = product.price * quantity;             // 价格来自数据库
  if (couponCode) {
    const coupon = await applyCoupon(couponCode, req.user.id);  // 内含次数/归属校验
    total = coupon.apply(total);
  }
  if (req.user.isVip) total = total * 0.5;          // 身份来自服务端会话

  // 用幂等键防止重复下单
  const order = await db.order.create({
    data: { userId: req.user.id, productId, quantity, total, idemKey: req.header('Idempotency-Key') },
  });
  res.json({ ok: true, orderId: order.id, total });
});
```

```js
// 修复 2：退款必须经过状态机校验，不能跳步；且需要角色授权
const REFUND_TRANSITIONS = {
  REQUESTED: ['REVIEWING', 'REJECTED'],
  REVIEWING: ['APPROVED', 'REJECTED'],
  APPROVED: [],           // 终态，不可再变
  REJECTED: [],
};

app.post('/api/refund/approve', requireRole('finance'), async (req, res) => {
  const refund = await db.refund.findUnique({ where: { id: req.body.id } });
  if (!refund) return res.status(404).json({ error: 'not found' });

  // 只有处于 REVIEWING 状态才允许批准；且需校验申请人不是审批人（职责分离）
  if (refund.status !== 'REVIEWING') {
    return res.status(409).json({ error: `invalid state: ${refund.status}` });
  }
  if (refund.requestedBy === req.user.id) {
    return res.status(403).json({ error: 'segregation of duties required' });
  }

  await db.refund.update({ where: { id: refund.id }, data: { status: 'APPROVED' } });
  res.json({ ok: true });
});
```

## 防御清单

- [ ] 建立并运行**安全开发生命周期（SDL）**，让 AppSec 专业人员参与安全与隐私控制的设计评估。
- [ ] 建立**安全设计模式库 / 铺好的路组件**，让开发者默认走安全路径。
- [ ] 对关键部分（认证、访问控制、业务逻辑、关键流程）做**威胁建模**，并把它当作培养安全思维的教学工具。
- [ ] 把**安全需求写进用户故事**（含滥用场景 misuse-case），与业务方共同确认正常流与失败流。
- [ ] 在应用各层（前端到后端）加入**合理性校验（plausibility check）**。
- [ ] 编写单元/集成测试，验证关键流程能抵御威胁模型中的攻击。
- [ ] 按暴露面与保护需求做**分层隔离**（网络层与系统层）；多租户系统做**租户隔离设计**。
- [ ] 服务端拥有最终权威：价格、权限、状态、次数限制**绝不信任客户端**。
- [ ] 关键流程用**状态机**约束，强制职责分离（如申请人≠审批人）。
- [ ] 所有写操作考虑**幂等性**，并对"仅一次"限制使用原子操作或分布式锁防竞态。
- [ ] 文件上传使用**允许列表 + 内容嗅探 + 存储与执行分离**。
- [ ] 使用 [OWASP SAMM](https://owaspsamm.org/) 结构化安全开发工作。
- [ ] 参考 [Secure Product Design Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet.html)。

## 常见坑

- **坑 1：以为"加个 WAF 就能防业务逻辑漏洞"。** WAF 看的是请求特征，业务逻辑漏洞的每个请求都"看起来正常"。
- **坑 2：把设计缺陷当实现缺陷修。** 如果需求没定义"不能做什么"，在代码里打补丁只会按下葫芦浮起瓢。
- **坑 3：忽略"失败流"的设计。** 只设计了成功路径，失败/超时/部分成功时的状态未定义，导致数据不一致（详见 [A10](A10-Mishandling-of-Exceptional-Conditions.md)）。
- **坑 4：竞态条件被当成理论问题。** "仅领一次""仅用一次"的校验若不原子，并发即可绕过。必须用数据库唯一约束、原子更新或分布式锁。
- **坑 5：依赖客户端做限制。** 前端禁用按钮、前端校验数量都不可信。服务端必须独立校验。
- **坑 6：用"知识问答"类找回密码。** 官方与 NIST 都明确反对。答案不是身份证据。
- **坑 7：威胁建模做成一次性文档。** 应融入每次需求梳理，随数据流与访问控制变化持续更新。

## 自测题

**1. 某应用的退款流程是"用户申请 → 财务审批 → 打款"。攻击者直接调用打款接口成功。这属于设计缺陷还是实现缺陷？**

<details><summary>答案</summary>

通常是设计缺陷（缺失状态机与步骤校验的设计），也可能叠加实现缺陷（设计了状态校验但没写）。但因为"多步流程必须有服务端状态约束"属于设计层面的要求，根因归于 A06。修复：用状态机约束流转，只有 APPROVED 状态才允许打款，并做职责分离。
</details>

**2. 应用限制"每个用户只能领一张优惠券"，代码逻辑是先查询已领数量、若为 0 则发放。并发 20 个请求会发生什么？**

<details><summary>答案</summary>

可能全部通过"已领数量为 0"的检查（TOCTOU 竞态），导致重复发放多张券。修复：使用数据库唯一约束（如 `UNIQUE(user_id, coupon_id)`）或原子条件更新，让"检查+写入"在一条语句/一个事务内完成。
</details>

**3. 为什么"基于安全问题找回密码"被官方和 NIST 明确反对？**

<details><summary>答案</summary>

因为安全问题的答案不是可信的身份证据——多个人可能知道答案，答案可能从社交媒体获得，且用户倾向于设置低熵答案。它属于设计缺陷（不应通过更好的实现来修补），应当整体移除，改为基于邮件/短信的一次性令牌或更安全的机制。
</details>

**4. 上传功能检查了文件扩展名，为什么仍可能被上传 Web Shell？**

<details><summary>答案</summary>

因为扩展名可被绕过：双扩展名（`shell.php.jpg`，取决于服务器解析规则）、大小写（`.PHP`）、空字节、内容与扩展名不符（扩展名是 jpg 但内容是 PHP，可配合服务器配置缺陷执行）。更根本的问题是设计上把"用户上传目录"与"可执行目录"放在了一起。应使用允许列表 + 内容检测 + 重命名 + 存储与执行彻底分离。
</details>

**5. 官方为什么说"左移还不够"？**

<details><summary>答案</summary>

因为左移到编码阶段仍然太晚——很多风险（如业务逻辑缺陷、信任边界划分、租户隔离）必须在**需求与设计阶段**决定，编码阶段只是实现。需要进一步左移到需求编写与应用设计，即 Secure by Design。
</details>

## 来源

- <https://top10.owasp.org/2025/A06_2025-Insecure_Design/>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic/README>
- <https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet.html>
- <https://owaspsamm.org/model/design/threat-assessment/>
