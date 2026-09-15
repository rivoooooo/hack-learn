# A09:2025 安全日志与告警失效（Security Logging and Alerting Failures）

> 官方详情页：<https://top10.owasp.org/2025/A09_2025-Security_Logging_and_Alerting_Failures/>
> 排名：**第 9 位**（2021 版也是第 9 位，**改名**：原 "Security Logging and **Monitoring** Failures" 安全日志与监控失效 → "**Alerting**" 告警）
> CWE 数量：5 个｜平均发生率：3.91%｜相关 CVE：**仅 723 条**
> 主要 CWE：CWE-117 日志输出中和不当、CWE-532 敏感信息写入日志、CWE-778 日志记录不足

## 一句话理解

日志与告警失效是**出了事你却不知道，或者知道了也没人行动**——关键事件没记、记录格式无法消费、日志可被篡改、有日志无告警，导致入侵可长期潜伏。

## 风险原理

官方对改名的解释很关键：**"日志很完善但没有告警，在识别安全事件方面几乎没有价值"**。因此把"监控（Monitoring）"改为"告警（Alerting）"，强调"能触发行动"。

失效通常发生在链条的任一环：

1. **采集缺失。** 可审计事件（登录、失败登录、高价值交易）没记录，或只记成功不记失败。
2. **内容不足。** 警告与错误产生空泛、不清晰、无上下文的日志。
3. **完整性未保护。** 日志可被篡改或删除。
4. **未监控。** 应用与 API 的日志无人分析可疑活动。
5. **仅本地存储。** 未备份、未集中、易丢失。
6. **告警阈值与升级流程缺失。** 或告警发出但无人及时查看。
7. **渗透测试与 DAST 扫描无法触发告警。** 这是检验"告警是否有效"的绝佳手段——如果扫描器狂扫都没告警，真实攻击也不会有。
8. **无法近实时检测/升级/告警。**
9. **日志本身成为泄露源或注入点。** 日志中写入敏感信息（PII/PHI）或未正确编码导致日志注入（CWE-117、CWE-532）。
10. **告警用例缺失或过时**，或**误报过多**导致 SOC 团队过载、真实告警被淹没。

> 官方特别提到"蜜标（honeytoken）"：在数据库/数据/身份中埋入正常业务永不使用的诱饵，任何访问都会产生几乎零误报的日志，非常适合告警。

ASCII 数据流图：

```
攻击者扫描/爆破/注入
        |
        v
[应用] --(1) 没记日志 ----------> 事件消失
        --(2) 记了但格式杂乱 -----> 无法被 SIEM 解析
        --(3) 记了、可解析，无告警 -> 日志沉睡在磁盘
        --(4) 告警发出，阈值/流程缺失 -> 无人响应
        |
        v
   入侵长期潜伏（官方示例：可能潜伏 7 年以上才被发现）
```

## 典型场景与真实案例模式

> 以下场景取自 **OWASP 官方 A09 页面正文引用的真实事件**描述，此处抽象化转述。

- **缺乏监控导致入侵长期未被发现。** 官方示例：某儿童健康计划网站运营方因缺乏监控与日志，未能发现入侵；最终由外部方通知才得知攻击者访问并修改了数百万儿童的健康记录。事后复盘发现开发者未处理重大漏洞，且由于没有日志与监控，数据泄露**可能自 2013 年起持续了七年以上**。
- **第三方云托管方延迟通报。** 官方示例：某大型航空公司发生涉及数百万乘客十余年个人数据（含护照与信用卡数据）的泄露，泄露发生在第三方云托管商处，且由该托管商在事发一段时间后才通知航司。
- **支付应用漏洞 + 监控缺失。** 官方示例：某欧洲大型航空公司因支付应用安全漏洞被利用，攻击者窃取超过 40 万条客户支付记录，最终被隐私监管机构罚款 2000 万英镑。
- **只记成功不记失败。** 登录审计只记录成功登录，导致撞库/爆破的大量失败尝试没有任何痕迹。
- **日志注入。** 用户可控字段（用户名、User-Agent）未中和就写入日志，攻击者插入换行与伪造日志行，污染审计记录或注入终端转义序列。
- **日志含敏感数据。** 把完整口令、令牌、身份证号、银行卡号写入日志，日志系统一旦被读取即造成二次泄露。
- **只告警不行动。** SIEM 产生海量误报，真实攻击告警被淹没；或缺少 playbook，告警收到后无人知道该做什么。

## 怎么测

对应 WSTG 测试项：

- [WSTG-ERRH-01](../wstg/checklist.md) 错误处理不当
- [WSTG-ERRH-02](../wstg/checklist.md) 堆栈跟踪
- [WSTG-CONF-02](../wstg/checklist.md) 应用平台配置
- [WSTG-CONF-05](../wstg/checklist.md) 管理接口枚举

**手工测试步骤**

1. **确定应被记录的事件清单，逐个验证。** 至少包括：成功/失败登录、登出、口令修改/重置、MFA 变更、权限/角色变更、访问控制失败、输入校验失败、高价值交易、管理操作、应用异常。
   ```bash
   # 做一次失败登录，然后检查日志（需有日志访问权限）
   curl -s -X POST https://target/login -d 'u=admin&p=wrong'
   # 在应用日志/集中日志平台搜索该事件，确认记录了：时间、来源IP、账号、结果
   ```
2. **验证格式可被消费。** 日志应为结构化（JSON）或明确的键值格式，包含时间戳（含时区/UTC）、事件类型、主体、来源、结果、关联 ID（request-id）。
3. **验证日志完整性。** 尝试以应用自身权限修改/删除日志，若可行则为缺陷。检查是否使用 append-only 存储或防篡改机制。
4. **验证日志中不含敏感数据。** 提交含敏感值的请求（如口令、令牌），检查日志是否将其原样记录：
   ```bash
   # 提交后搜索日志中是否出现该明文口令/令牌
   grep -i 'SuperSecretPass' /var/log/app/*.log
   ```
5. **测试日志注入。**
   ```bash
   # 在会被记录到日志的字段中提交换行与伪造日志
   curl -s https://target/ -A $'Mozilla/5.0\nERROR admin login succeeded from 10.0.0.1'
   ```
   然后检查日志中是否出现一条伪造的独立日志行。修复需对日志输出做中和（CWE-117）。
6. **用扫描器验证告警是否触发。** 官方明确指出：**DAST 工具（Burp、ZAP）的扫描应触发告警**。运行一次授权扫描，确认 SOC/监控是否能收到告警。
   ```bash
   # 仅对授权目标执行
   zap-cli quick-scan -s all https://target
   ```
   若无任何告警，说明检测能力不足。
7. **审查告警用例与 playbook。** 检查是否定义了阈值（如 5 分钟内失败登录 N 次）、升级路径、责任人、响应时限，以及 playbook 是否最新。
8. **检查蜜标。** 是否在数据库/数据中埋入诱饵账号或诱饵记录用于高置信度告警。

## 代码示例

### 易受攻击的代码（Python —— 记录不足 + 记录敏感信息 + 日志注入）

```python
import logging
logging.basicConfig(level=logging.INFO, filename="app.log")

@app.post("/login")
def login():
    u = request.form["username"]
    p = request.form["password"]

    # 危险 1：把明文口令写入日志（CWE-532）
    # 危险 2：未中和用户输入，用户可在 username 中插入换行伪造日志（CWE-117）
    logging.info(f"login attempt user={u} pass={p}")

    user = authenticate(u, p)
    if not user:
        # 危险 3：失败登录没有独立、可告警的日志事件，也没有告警
        return "failed", 401

    # 危险 4：登录成功无审计上下文（IP、UA、request-id）
    return "ok"
```

### 修复后的代码

```python
import json
import logging
import re
import time
import uuid
from flask import g, request

# 修复 1：结构化日志，便于 SIEM 消费
logger = logging.getLogger("auth")
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)

_SAFE = re.compile(r"[\r\n\t]")

def safe(v: str) -> str:
    """中和换行/制表符，防止日志注入（CWE-117）"""
    return _SAFE.sub("_", str(v))[:256]

def audit(event: str, outcome: str, **extra):
    record = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),  # UTC
        "event": event,
        "outcome": outcome,
        "request_id": getattr(g, "request_id", None),
        "src_ip": request.remote_addr,
        "user_agent": safe(request.headers.get("User-Agent", "")),
        **extra,
    }
    logger.info(json.dumps(record, ensure_ascii=False))

@app.before_request
def _rid():
    g.request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())

@app.post("/login")
def login():
    u = request.form["username"]
    p = request.form["password"]

    user = authenticate(u, p)

    if not user:
        # 修复 2：失败登录作为独立告警事件；不记录口令；账号做必要脱敏
        audit("auth.login", "failure", account=safe(u)[:64])
        # 修复 3：触发告警（示例：按账号/IP 聚合后的速率阈值）
        metrics.increment("auth.login.failure", tags={"account": u[:64]})
        maybe_alert("auth.bruteforce", account=u, ip=request.remote_addr)
        return "invalid credentials", 401   # 统一消息，防枚举

    audit("auth.login", "success", account=safe(u)[:64], user_id=user.id)
    metrics.increment("auth.login.success")
    return "ok"
```

```python
# 修复 4：应用启动时配置全局异常处理，确保异常一定被记录（配合 A10）
@app.errorhandler(Exception)
def on_error(e):
    logger.exception(json.dumps({
        "event": "app.exception",
        "request_id": getattr(g, "request_id", None),
        "path": request.path,
        "type": type(e).__name__,
    }))
    return {"error": "Internal Server Error"}, 500
```

## 防御清单

- [ ] 确保所有**登录、访问控制、服务端输入校验失败**都能被记录，且带足够用户上下文，保留时间足以支持延迟取证。
- [ ] 应用中**每个安全控制的成功与失败**都要记录。
- [ ] 日志采用**日志管理系统易于消费的格式**（结构化/JSON）。
- [ ] 日志数据**正确编码**，防止日志注入或对日志/监控系统的攻击。
- [ ] 所有交易具备**带完整性控制的审计轨迹**（如 append-only 表），防篡改与删除。
- [ ] 所有抛错的交易**回滚后重来，始终 fail closed（失效关闭）**。
- [ ] 对可疑行为**发出告警**；为开发者提供编码指引，或直接采购相应系统。
- [ ] DevSecOps 与安全团队建立**有效的监控告警用例与 playbook**，让 SOC 能快速响应。
- [ ] 在数据库、数据、身份中埋入**蜜标（honeytoken）**作为近乎零误报的告警源。
- [ ] 可选：用行为分析与 AI 辅助降低误报。
- [ ] 建立或采用**事件响应与恢复计划**（如 NIST 800-61r2 或更高版本），并培训开发者识别攻击与事件。
- [ ] 检查并消除日志中的敏感信息（口令、令牌、PII/PHI、卡号）。
- [ ] 参考 [Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)、[Application Logging Vocabulary Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Application_Logging_Vocabulary_Cheat_Sheet.html)。

## 常见坑

- **坑 1：只记成功，不记失败。** 失败登录、失败授权、失败校验才是攻击的主要信号。
- **坑 2：日志有但没人看。** 没有告警阈值与响应流程，日志只是磁盘占用。官方明确："完善的日志但无告警，几乎无价值。"
- **坑 3：日志里写敏感信息。** 会把日志系统变成新的泄露面。口令、令牌、PII 必须脱敏或排除。
- **坑 4：不中和用户输入。** 攻击者可在用户名/UA 中插入换行伪造日志行，误导取证甚至注入终端转义序列。
- **坑 5：只存本地、不做备份。** 攻击者拿到主机权限后第一件事往往是删日志；本地单副本等于没有审计。
- **坑 6：误报淹没真实告警。** 阈值设置不当，SOC 被淹没后对真实事件脱敏。需要调优与分级。
- **坑 7：从不验证告警是否有效。** 官方建议：渗透测试与 DAST 扫描**应当触发告警**——如果扫描都没告警，说明检测形同虚设。
- **坑 8：日志时间不同步。** 各主机时钟不一致会使跨系统关联分析失效；应统一时钟与时区（推荐 UTC）。

## 自测题

**1. 团队部署了 ELK，日志收集齐全，但从未配置任何告警规则。这属于 A09 的失效吗？**

<details><summary>答案</summary>

属于。官方 2025 版特意把"监控"改为"告警"，说明"有日志无告警"仍是失效状态。没有告警就无法触发行动，入侵可长期潜伏。修复：定义告警用例、阈值、升级路径与 playbook，并定期用扫描验证告警会被触发。
</details>

**2. 攻击者在 `User-Agent` 中提交了 `Mozilla/5.0\nERROR admin login succeeded`，导致日志中出现一条伪造的成功登录记录。这是什么问题？**

<details><summary>答案</summary>

日志注入（Log Injection / CWE-117，日志输出中和不当）。未对写入日志的用户输入做换行/控制字符中和，攻击者可伪造、篡改审计记录或注入终端转义序列。修复：对日志字段做输出中和（去除/转义 `\r\n\t` 与控制字符），使用结构化日志并对值做编码。
</details>

**3. 为什么"只把日志存在应用服务器本地"是高风险的？**

<details><summary>答案</summary>

攻击者获得主机权限后通常会清理日志以清除痕迹；本地单副本也容易因磁盘故障、重装而丢失。应集中到独立的日志系统，设置访问控制与只追加/防篡改机制，并做好备份与保留策略。
</details>

**4. 官方为什么说"渗透测试与 DAST 扫描应触发告警"，这与 A09 有什么关系？**

<details><summary>答案</summary>

这是验证告警是否有效的最直接手段：如果一次明显的自动化扫描都无法触发任何告警，那么真实攻击（手法类似但更隐蔽）也不会被检测到。因此它既是检测能力验证，也是 A09 的验收标准之一。
</details>

**5. 什么是"蜜标（honeytoken）"，为什么它特别适合告警？**

<details><summary>答案</summary>

蜜标是埋入数据库/数据/身份中的诱饵（如一个无人使用的诱饵账号、诱饵记录、诱饵凭据），正常业务永不访问它。任何访问都极可能是攻击行为，因此能产生**近乎零误报**的告警，非常适合在高噪音环境中提供高置信度信号。
</details>

## 来源

- <https://top10.owasp.org/2025/A09_2025-Security_Logging_and_Alerting_Failures/>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/08-Error_Handling/README>
- <https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html>
- <https://cheatsheetseries.owasp.org/cheatsheets/Application_Logging_Vocabulary_Cheat_Sheet.html>
