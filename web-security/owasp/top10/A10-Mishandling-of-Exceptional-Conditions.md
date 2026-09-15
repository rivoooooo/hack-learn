# A10:2025 异常条件处理不当（Mishandling of Exceptional Conditions）

> 官方详情页：<https://top10.owasp.org/2025/A10_2025-Mishandling_of_Exceptional_Conditions/>
> 排名：**第 10 位（2025 版全新类别）**
> CWE 数量：24 个｜平均发生率：2.95%｜相关 CVE：3,416
> 主要 CWE：CWE-209 错误信息含敏感信息、CWE-234 未处理缺失参数、CWE-274 权限不足处理不当、CWE-476 空指针解引用、CWE-636 未安全失败（fail open，失效开放）

## 一句话理解

异常条件处理不当是**程序在遇到"预料之外的情况"时没有正确阻止、识别或响应**——结果是崩溃、行为不可预测，或者最危险的：**本该拒绝却选择了放行（fail open）**。

## 风险原理

官方定义：当程序未能预防、检测和响应异常与不可预测的情况时，就会导致崩溃、异常行为，有时还会造成漏洞。它可以是三种失败的任意组合：

1. **没有预防**该异常情况发生；
2. **没有识别**出情况正在发生；
3. **事后响应**很差或根本没有响应。

官方给出一个可直接套用的判据：**"任何时候应用不确定自己的下一条指令是什么，就已经是异常条件处理不当。"**

异常条件的来源：缺失/糟糕/不完整的输入校验；在函数之外的高层才做错误处理（太晚）；意外的环境状态（内存、权限、网络）；不一致的异常处理；或完全未处理的异常，使系统陷入未知且不可预测的状态。

这类问题会引发许多不同漏洞：逻辑缺陷、溢出、竞态条件、欺诈交易，以及内存、状态、资源、时序、认证、授权方面的问题，进而影响机密性、可用性和完整性。

> 官方解释为什么单列这一类：以前这类 CWE 常被归为"代码质量差"，太笼统；单列后能给出更好的指导。**好消息是 24 个 CWE 中有不少此前就在其他类别中，因此它其实是"被显式化"，而非全新风险。**

ASCII 数据流图（fail open 的经典形态）：

```
正常：  校验失败 --> 拒绝访问
异常：  校验过程抛异常 --(未捕获)--> 异常被吞掉 --> 代码继续执行 --> 授予访问
                                                  ^^^^^^^^^^^^
                                        "不确定时选择了放行" = fail open
```

## 典型场景与真实案例模式

> 以下场景取自 **OWASP 官方 A10 页面正文给出的示例**，此处转述。

- **资源耗尽导致拒绝服务（DoS）。** 官方示例：应用在处理文件上传时捕获了异常，但异常后**没有正确释放资源**；每次异常都留下被锁定/不可用的资源，累积到资源耗尽为止。
- **敏感数据经错误信息泄露。** 官方示例：数据库错误处理不当，把完整的系统错误信息暴露给用户。攻击者持续制造错误，利用这些敏感系统信息来完善 SQL 注入攻击——错误信息就是侦察情报。
- **交易状态损坏 / 竞态。** 官方示例：多步金融交易（扣款 → 入账 → 记录流水）在遭遇网络中断时，若系统没有正确地**整体回滚（fail closed）**，攻击者可能耗空用户账户，或利用竞态把资金多次转入目标账户。
- **异常被吞掉导致继续执行。** `catch (Exception e) { }` 空捕获，或捕获后只打日志不改变控制流，导致后续代码在错误状态下继续运行。
- **缺少默认分支。** `switch` 缺 `default`、条件链缺兜底分支，出现未覆盖的取值时走到未定义路径（CWE-478）。
- **未检查返回值。** 关键操作（如权限校验、资金扣减、文件写入）的返回值未检查，失败被静默忽略（CWE-252、CWE-391）。
- **空指针/除零导致崩溃。** 未对缺失参数、空对象、零值做处理，导致服务崩溃（CWE-476、CWE-369）。
- **无资源上限。** 任何 IT 资源若"无上限"，会导致应用缺乏韧性、拒绝服务、暴力破解成功与异常云账单。官方强调：**任何东西都不应是无上限的**。

## 怎么测

对应 WSTG 测试项：

- [WSTG-ERRH-01](../wstg/checklist.md) 错误处理不当
- [WSTG-ERRH-02](../wstg/checklist.md) 堆栈跟踪
- [WSTG-BUSL-03](../wstg/checklist.md) 完整性校验
- [WSTG-BUSL-04](../wstg/checklist.md) 流程时序
- [WSTG-BUSL-05](../wstg/checklist.md) 功能使用次数限制
- [WSTG-BUSL-10](../wstg/checklist.md) 支付功能
- [WSTG-INPV-05](../wstg/checklist.md) SQL 注入（用于验证错误信息泄露的有用性）

**手工测试步骤**

1. **制造异常并观察行为。**
   ```
   删除必填参数：     POST /api/transfer  body 缺少 amount
   提交非法类型：     {"amount": "abc"}
   提交越界值：       {"amount": -1}、{"amount": 999999999999999999}
   提交空对象：       {"amount": null}
   超长字符串：       username = "A"*100000
   畸形 JSON：        {"a":
   错误 Content-Type：Content-Type: text/plain 但 body 是 JSON
   ```
   观察：是返回通用错误，还是崩溃/堆栈/500？是否仍执行了部分逻辑？
2. **检查错误信息是否泄露敏感内容。** 触发各类错误（数据库、模板、文件、类型），搜索响应中的关键字：
   ```bash
   curl -s 'https://target/api/item?id=%27' | grep -iE 'traceback|stack|ORA-|PostgreSQL|SQLSTATE|at [a-zA-Z]+\.|/var/www|\.java:|\.py:'
   ```
3. **测试"fail open"倾向。** 关键场景：让校验组件"失效"（如提交畸形数据使校验器抛错），观察是默认拒绝还是默认放行。
   ```
   正常：  权限字段缺失 -> 拒绝
   攻击：  提交使权限解析抛错的数据 -> 是否被当成"无限制"而放行？
   ```
4. **测试并发与时序（竞态）。** 对多步交易并发发送，观察是否出现部分成功、重复入账、余额为负。
   ```bash
   seq 1 30 | xargs -P 30 -I{} curl -s -o /dev/null -w '%{http_code}\n' \
     -H 'Cookie: session=<s>' -X POST https://target/api/transfer \
     -d 'to=acctB&amount=1000'
   ```
   随后查询双方余额，核对总账是否守恒。
5. **测试资源耗尽。** 大量并发上传大文件、触发大量错误，观察资源是否正确释放、是否有速率限制与配额。
   ```bash
   # 仅对授权目标/靶场
   for i in $(seq 1 200); do curl -s -F 'file=@big.jpg' https://target/upload & done; wait
   ```
6. **中断多步流程。** 在交易中途断开连接（如发送部分 body 后关闭），检查服务端是否正确回滚，而不是留下"半完成"状态。
7. **代码审计检查点。** 搜索危险模式：
   ```bash
   # 空捕获 / 只打日志的捕获 / 未检查返回值
   grep -rEn 'catch\s*\(.*\)\s*\{\s*\}|except\s*:\s*pass|except Exception:\s*pass' --include='*.java' --include='*.py' .
   grep -rEn 'switch\s*\(' --include='*.java' .        # 检查是否有 default
   ```
8. **检查无上限接口。** 是否对查询条数、分页大小、上传大小、请求频率、并发生成设置了上限。

## 代码示例

### 易受攻击的代码（Java —— fail open + 空捕获 + 信息泄露）

```java
public boolean isAuthorized(User user, Resource res) {
    try {
        return aclService.check(user, res);      // 可能抛异常（如 ACL 服务不可用）
    } catch (Exception e) {
        // 危险 1：fail open —— 异常时默认放行
        log.warn("acl check failed, allowing");  // 危险 2：只打日志不改变控制流
        return true;
    }
}

public BigDecimal getBalance(String accountId) {
    // 危险 3：不检查 accountId 是否为 null -> 可能触发 NULL Pointer
    Account a = repo.findById(accountId).orElse(null);
    return a.getBalance();                        // 危险 4：NPE
}

public void transfer(String from, String to, BigDecimal amount) {
    // 危险 5：三步非原子、无回滚；中途失败会留下不一致状态
    accounts.debit(from, amount);                 // 若此处成功
    accounts.credit(to, amount);                  // 而此处失败 => 总账不守恒
    ledger.record(from, to, amount);
}
```

### 修复后的代码

```java
public boolean isAuthorized(User user, Resource res) {
    try {
        return aclService.check(user, res);
    } catch (Exception e) {
        // 修复 1：fail closed —— 无法确定时一律拒绝
        log.error("acl check failed, denying access", e);
        alert("acl.service.failure", Map.of("user", user.getId(), "resource", res.getId()));
        return false;
    }
}

public BigDecimal getBalance(String accountId) {
    // 修复 2：入口处显式校验参数，明确处理缺失值
    if (accountId == null || accountId.isBlank()) {
        throw new BadRequestException("accountId is required");   // 映射为 400，而非 500
    }
    Account a = repo.findById(accountId)
        .orElseThrow(() -> new NotFoundException("account not found"));  // 明确 404
    return a.getBalance();
}

@Transactional                                                    // 修复 3：单事务，原子
public void transfer(String from, String to, BigDecimal amount) {
    if (amount == null || amount.signum() <= 0) {
        throw new BadRequestException("amount must be positive");
    }
    // 修复 4：条件更新（原子），并把"检查余额"和"扣减"合并，防竞态
    int updated = accounts.debitIfSufficient(from, amount);
    if (updated == 0) {
        throw new ConflictException("insufficient funds");        // 事务回滚
    }
    accounts.credit(to, amount);
    ledger.record(from, to, amount);
    // 任何一步抛异常 -> 整个事务回滚（fail closed），并抛出错误告知用户
}
```

### 修复后的代码（Python —— 全局兜底 + 资源释放 + 上限）

```python
@app.errorhandler(Exception)
def handle_unexpected(e):
    # 修复 5：全局异常处理器兜底，保证"没有漏网的异常"
    logger.exception("unhandled", extra={"request_id": g.request_id})
    return {"error": "Internal Server Error"}, 500    # 对外最小化信息

@app.post("/upload")
def upload():
    tmp_path = None
    try:
        tmp_path = save_temp(request.files["file"])
        return process(tmp_path)
    except Exception:
        logger.exception("upload failed", extra={"request_id": g.request_id})
        return {"error": "upload failed"}, 500
    finally:
        # 修复 6：无论成功失败都释放资源，避免资源耗尽
        if tmp_path:
            os.unlink(tmp_path)

@app.get("/search")
def search():
    # 修复 7：显式上限，任何东西都不应无上限
    limit = min(int(request.args.get("limit", 20)), 100)
    page = max(int(request.args.get("page", 1)), 1)
    return query_items(q=request.args.get("q"), limit=limit, offset=(page - 1) * limit)
```

> 修复原则：**在异常发生处就近捕获与处理**；对外只给通用错误，细节进日志；**不确定时一律 fail closed**；多步交易必须原子回滚；所有资源加上限。

## 防御清单

- [ ] 预期最坏情况：**在异常发生的地方就近捕获并处理**（不是等它冒泡到高层）。
- [ ] 捕获后要做**有意义的事**：向用户以可理解的方式报错、记录日志、必要时告警。
- [ ] 配置**全局异常处理器**兜底，防止有异常漏网。
- [ ] 配置监控/可观测性，识别重复错误或攻击模式，并能响应、防御或阻断。
- [ ] 多步交易出错时**整体回滚并重来（fail closed）**，不要试图"从中途恢复"。
- [ ] **所有资源都加上限**：速率限制、资源配额、节流。任何无上限的东西都会导致缺乏韧性、DoS、暴力破解与异常账单。
- [ ] 对高重复度的相同错误，考虑只输出频率统计（在原消息上追加，避免干扰自动化日志与监控）。
- [ ] 严格输入校验 + 对必须接受的危险字符做净化/转义。
- [ ] **集中化**错误处理、日志、监控与告警；应用不应有多套处理逻辑，应统一在同一处、以相同方式执行。
- [ ] 建立项目安全需求，做威胁建模/安全设计评审、代码评审或静态分析，并对系统做压力、性能与渗透测试。
- [ ] 组织层面统一异常处理方式，便于审计与复核。
- [ ] 对外错误信息最小化，避免堆栈与系统细节泄露（与 [A02](A02-Security-Misconfiguration.md) 协同）。
- [ ] 参考 [Error Handling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html)、[Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)。

## 常见坑

- **坑 1：空 `catch` 块。** `catch (Exception e) {}` 或 `except: pass` 是所有问题的源头——错误被吞掉，程序在未知状态下继续跑。
- **坑 2：fail open。** 最常见也最危险：校验组件出问题时"默认放行"。**必须改为 fail closed**。
- **坑 3：只回滚一部分。** 多步交易中途失败只回滚了部分步骤，留下不一致状态（最典型是资金不守恒）。
- **坑 4：用异常做控制流。** 把"参数非法"当成异常一路抛出并在高层处理，会导致处理太晚、上下文丢失。应在发生处就近处理。
- **坑 5：异常里泄露堆栈。** 面向用户的错误应通用，堆栈只进服务端日志。但注意"只打日志"不等于"处理了"——控制流也必须正确改变。
- **坑 6：忘记释放资源。** 文件句柄、数据库连接、锁、临时文件在异常路径上必须通过 `finally`/`using`/`defer` 释放，否则累积到资源耗尽。
- **坑 7：没有上限。** 无分页上限、无上传大小上限、无速率限制，等于把 DoS 能力送给攻击者。
- **坑 8：`catch (Exception)` 过广。** 会连"本该传播的业务异常"一起吞掉，掩盖真实问题（CWE-396）。应尽量捕获具体类型，并在最外层保留一个兜底。
- **坑 9：认为"异常处理不当"只是代码质量问题。** 2025 版明确把它作为独立安全类别；它可导致逻辑缺陷、竞态、欺诈交易与认证绕过。

## 自测题

**1. 权限校验函数在 ACL 服务不可用时捕获异常并返回 `true`。这叫什么问题，正确做法是什么？**

<details><summary>答案</summary>

这叫 fail open（未安全失败，CWE-636）。系统在无法确定权限时选择了放行，攻击者可通过使 ACL 服务不可用（或构造让其抛错的输入）来绕过授权。正确做法是 **fail closed**：无法确定时一律拒绝，同时记录错误并告警。
</details>

**2. 转账流程为"扣款 → 入账 → 记流水"，三步之间没有事务。网络在扣款后中断会发生什么？**

<details><summary>答案</summary>

扣款成功但入账未执行，导致总账不守恒——用户资金凭空消失。若攻击者能主动制造中断（如断网、超时），还可构造重复入账等竞态。修复：把三步放进同一事务，任何一步失败整体回滚（fail closed），并对"检查+扣减"使用原子条件更新防竞态。
</details>

**3. 为什么官方说"任何东西都不应是无上限的"？**

<details><summary>答案</summary>

因为无上限会导致：应用缺乏韧性、拒绝服务、让暴力破解得以成功（登录尝试无上限）、以及异常的云账单（无配额）。应尽可能加上速率限制、资源配额与节流，在异常发生之前就预防。
</details>

**4. 应用捕获了上传异常并打日志，但没有清理临时文件。长期运行会发生什么？**

<details><summary>答案</summary>

每次异常都留下一个被占用/未清理的临时文件，逐渐耗尽磁盘空间或文件句柄，最终导致拒绝服务（对应官方示例中的资源耗尽）。修复：用 `finally`/`using`/`defer` 确保异常路径上也释放资源。
</details>

**5. 一个 `switch(status)` 语句没有 `default` 分支。这与 A10 有什么关系？**

<details><summary>答案</summary>

缺少默认分支（CWE-478）意味着当出现未覆盖的取值时，控制流会走向未定义或"什么都不做"的路径。若该 `switch` 用于授权或状态判断，可能出现"既不放行也不拒绝"的模糊状态，或意外落到不安全的默认行为。修复：始终提供 `default` 分支，并在无法识别状态时采取 fail closed 的显式处理。
</details>

## 来源

- <https://top10.owasp.org/2025/A10_2025-Mishandling_of_Exceptional_Conditions/>
- <https://top10.owasp.org/2025/0x00_2025-Introduction/>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/08-Error_Handling/README>
- <https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html>
