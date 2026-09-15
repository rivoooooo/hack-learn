# CWE 实验：给有缺陷的代码定位 CWE 编号并修复

本实验给你 **3 段自拟的有缺陷代码**（虚构，未从任何真实项目复制）。每段都**故意埋了多个弱点**。

**任务**：对每段代码

1. 找出所有弱点，给每个弱点标注 **CWE 编号**与名称；
2. 说明**根因**（为什么这是弱点，而不是"因为没过滤"这种表层说法）；
3. 写出**最小验证思路**（在授权环境怎么证明它存在）；
4. 给出**修复代码**，并说明修复对应哪个 CWE 的标准对策。

**然后对照每段后面的"答案与解析"**。答案里的 CWE 编号与名称均来自 [2025 CWE Top 25](./README.md#3-2025-年-cwe-top-25-最危险软件弱点) 与 CWE 官方定义库 <https://cwe.mitre.org/>。

> **红线**：本实验的代码**只允许在你本机隔离环境中运行**用于验证理解。任何针对未授权系统的测试均属违法。

---

## 实验前的准备

建议先读 [audit-guide.md](./audit-guide.md)，把"代码模式 → grep 思路 → 误报排除"三段式方法用起来。

**答题卡模板**（每段代码用一份）

```
【代码 N】

弱点 1
  CWE 编号与名称：
  出问题的那一行（行号 + 代码）：
  根因（一句话）：
  最小验证思路：
  修复方案（贴代码）：
  误报排除考虑（为什么这确实不是误报）：

弱点 2
  ...

（如果你认为某处"看着像但不是"，也写下来，标注为"排除项"并给理由）
```

---

## 代码 1：Python Flask 报表下载服务

```python
# report_service.py  ——  虚构代码，仅用于教学
import os
import sqlite3
from flask import Flask, request, send_file

app = Flask(__name__)
BASE_DIR = "/srv/reports"
DB = "/srv/app/app.db"

def get_db():
    conn = sqlite3.connect(DB)
    return conn

@app.route("/api/report")
def get_report():
    report_id = request.args.get("id", "")
    conn = get_db()
    cur = conn.cursor()
    # 第 15 行
    cur.execute("SELECT title, owner_id, file_path FROM reports WHERE id = " + report_id)
    row = cur.fetchone()
    if not row:
        return {"error": "not found"}, 404
    title, owner_id, file_path = row

    # 第 22 行
    resp = send_file(os.path.join(BASE_DIR, file_path))
    resp.headers["Content-Disposition"] = 'attachment; filename="' + title + '"'
    return resp

@app.route("/admin/cleanup")
def cleanup():
    # 第 28 行
    conn = get_db()
    conn.execute("DELETE FROM reports WHERE created_at < date('now', '-90 day')")
    conn.commit()
    return {"ok": True}

@app.route("/api/ping")
def ping():
    # 第 35 行
    host = request.args.get("host", "127.0.0.1")
    result = os.popen("ping -c 1 " + host).read()
    return {"output": result}
```

### 你该找出几个？

至少 **4 个**弱点，外加 **1 个"看着像但不是"的排除项**。

---

<details>
<summary>👉 点击展开：代码 1 的答案与解析</summary>

**弱点 1 — SQL 注入**

- **CWE**：`CWE-89` Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')｜Top 25 排名 **第 2 位**
- **位置**：第 15 行 `cur.execute("SELECT ... WHERE id = " + report_id)`
- **根因**：把 HTTP 查询参数**拼接进 SQL 语句结构**，数据与代码未分离。`report_id = "1 OR 1=1"` 会改变查询语义。
- **最小验证**：`GET /api/report?id=1 OR 1=1` 返回了本不该返回的记录；或用 `id=1 UNION SELECT ...` 探测列数。
- **修复**：

  ```python
  cur.execute("SELECT title, owner_id, file_path FROM reports WHERE id = ?", (report_id,))
  ```
  （如果 `id` 语义上必须是数字，还应先 `int()` 校验并在失败时返回 400——但那属于输入校验，**不能替代参数化**。）

**弱点 2 — 缺失授权（水平越权）**

- **CWE**：`CWE-862` Missing Authorization｜Top 25 排名 **第 4 位**（也可细分为 `CWE-639` 通过用户可控键绕过授权，排名第 24 位）
- **位置**：第 15～24 行整段。查询取出了 `owner_id`，但**从未使用它**，也没有任何登录态校验。
- **根因**：接口**没有任何认证与授权步骤**；进一步看，即便加了登录，代码也**没有校验"当前用户是否有权访问 owner_id 对应的报表"**。这正是"授权检查缺失"，而不是"检查写错了"。
- **最小验证**：匿名请求 `GET /api/report?id=1` 即返回数据 → 缺失认证/授权；再换 `id=2` 拿到他人资源 → 确认越权。
- **修复**（修正后的完整片段）：

  ```python
  from flask_login import login_required, current_user

  @app.route("/api/report")
  @login_required                                   # 认证
  def get_report():
      report_id = request.args.get("id", "")
      if not report_id.isdigit():
          return {"error": "bad id"}, 400
      conn = get_db()
      cur = conn.cursor()
      cur.execute(
          "SELECT title, file_path FROM reports WHERE id = ? AND owner_id = ?",
          (int(report_id), current_user.id),        # 授权：把主体约束写进查询条件
      )
      row = cur.fetchone()
      if not row:
          return {"error": "not found"}, 404        # 不区分"不存在"与"无权限"，避免枚举
      title, file_path = row
      ...
  ```
  **要点**：授权条件必须**在服务端查询里带上主体约束**，而不是在返回后做过滤。

**弱点 3 — 路径穿越**

- **CWE**：`CWE-22` Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')｜Top 25 排名 **第 6 位**
- **位置**：第 22 行 `send_file(os.path.join(BASE_DIR, file_path))`
- **根因**：`file_path` 来自数据库，而数据库的值来自上游——**上游又被 SQL 注入点污染**，并且此处从未做"限制在 BASE_DIR 内"的处理。
  **注意这个组合**：SQL 注入让攻击者能控制 `file_path` 的值，从而把"只能读报表目录"变成"读任意文件"。**弱点会链式放大**，这正是审计时必须做数据流分析、而不是逐行孤立看的原因。
- **额外陷阱**：`os.path.join(BASE_DIR, file_path)` 在 `file_path` 是**绝对路径**时会**丢弃 BASE_DIR**（Python 的既定行为）。所以"用了 join 就安全"是错的。
- **最小验证**：先通过 SQL 注入或直接构造数据把 `file_path` 设为 `/etc/passwd` 与 `../../etc/passwd`，观察两种写法是否都能读出。
- **修复**：

  ```python
  import os

  def safe_join(base: str, untrusted: str) -> str:
      base_abs = os.path.realpath(base)
      # 丢掉任何目录部分，只保留文件名，避免绝对路径与 ../ 生效
      candidate = os.path.realpath(os.path.join(base_abs, os.path.basename(untrusted)))
      if candidate != base_abs and not candidate.startswith(base_abs + os.sep):
          raise ValueError("path traversal detected")
      return candidate

  resp = send_file(safe_join(BASE_DIR, file_path))
  ```
  **三个要点**：(a) 先 `realpath` 规范化；(b) 比较时补 `os.sep`，防止 `/srv/reports-evil` 前缀匹配 `/srv/reports`；(c) 用 `basename` 从根上消掉目录成分。

**弱点 4 — 响应头注入（HTTP 响应拆分）**

- **CWE**：`CWE-113` Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Response Splitting')｜**2025 Top 25 未入榜**（属"On the Cusp"方向的特例，其父类 `CWE-93` 亦未入榜）
- **位置**：第 23 行 `resp.headers["Content-Disposition"] = 'attachment; filename="' + title + '"'`
- **根因**：`title` 是数据库字段（上游可被 SQL 注入控制），未做 CRLF 与引号处理就拼进响应头，可注入额外头部（如 `Set-Cookie`）。
- **最小验证**：让 `title` 含 `\r\nSet-Cookie: a=b`，观察响应是否多出该头部。多数现代框架会拒绝含 CRLF 的头部值（Python 的 werkzeug 会抛异常），**所以这条要实际测，不能只看代码下结论**——这正是"必须动态验证"的典型例子。
- **修复**：

  ```python
  from urllib.parse import quote
  safe_name = quote(title, safe="")
  resp.headers["Content-Disposition"] = f'attachment; filename="{safe_name}"; filename*=UTF-8\'\'{safe_name}'
  ```

**弱点 5 — 命令注入**

- **CWE**：`CWE-78` Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')｜Top 25 排名 **第 9 位**（**KEV 计数 20，为全表最高**）
- **位置**：第 35 行 `os.popen("ping -c 1 " + host)`
- **根因**：`os.popen` **经由 shell 执行**，`host = "127.0.0.1; id"` 会执行第二条命令。
- **最小验证**：`GET /api/ping?host=127.0.0.1;id`，观察返回是否包含 `uid=`。
- **修复**：

  ```python
  import shlex
  import subprocess

  if not re.fullmatch(r"[A-Za-z0-9._-]{1,253}", host):
      return {"error": "invalid host"}, 400

  # 不经 shell，参数以列表传递
  proc = subprocess.run(
      ["ping", "-c", "1", host],
      capture_output=True, text=True, timeout=5, shell=False,
  )
  ```
  **要点**：(a) 不用 shell；(b) 空白名单校验（比黑名单可靠）；(c) 加 `timeout` 防止资源耗尽。

**弱点 6 — 关键功能缺失认证**

- **CWE**：`CWE-306` Missing Authentication for Critical Function｜Top 25 排名 **第 21 位**（**KEV 计数 11**）
- **位置**：第 27～31 行 `@app.route("/admin/cleanup")`
- **根因**：一个**删除数据的运维功能**没有任何认证。任何能访问该服务的人都能触发全量清理。
- **最小验证**：匿名 `curl -X GET http://127.0.0.1:5000/admin/cleanup`（**在测试库上做，且先备份**）观察是否真删除了数据。
- **修复**：

  ```python
  @app.route("/admin/cleanup", methods=["POST"])     # 改 POST 避免被预取/爬虫误触
  @login_required
  @require_role("admin")
  def cleanup():
      # 加审计日志
      app.logger.warning("cleanup triggered by %s", current_user.id)
      ...
  ```
  **要点**：(a) 加认证 **和** 角色授权；(b) 写操作改 `POST`（顺带缓解 CSRF 与误触）；(c) 留审计日志。

**排除项（看着像但不是）**

- **第 15 行的 SQL 同时"读出了 owner_id"这件事本身不是弱点**——`SELECT owner_id` 是正常的。**真正的弱点是"取出来了却没有用它做授权判断"**（弱点 2）。
  把"能读敏感字段"当作弱点，是最常见的判定错误。**要报的是"缺少控制"，不是"数据被取出"。**

**另一个可选排除项**：`date('now','-90 day')` 是**字面量 SQL 表达式**，不含用户输入 → 第 29 行的 `DELETE` 语句**本身不是 SQL 注入**。它是弱点 6（缺失认证）的载体。

**本段代码的弱点链（写报告时应画出来）**

```
匿名请求 /api/report
   └─ CWE-306/862  无认证无授权 → 直接可访问
        └─ CWE-89  SQL 注入 → 控制 file_path 的值
             └─ CWE-22 路径穿越 → 读任意文件
        └─ CWE-113 响应头注入（若框架未拦）

匿名请求 /api/ping
   └─ CWE-78 命令注入 → 服务器上执行任意命令
        └─ 升格为完整服务器失陷
```

</details>

---

## 代码 2：Node.js + Express 用户中心

```javascript
// server.js  ——  虚构代码，仅用于教学
const express = require('express');
const mysql = require('mysql2/promise');
const cookieParser = require('cookie-parser');
const app = express();

app.use(express.json());
app.use(cookieParser());

const pool = mysql.createPool({
  host: '127.0.0.1',
  user: 'app',
  password: 'App@2024!Prod',          // 第 13 行
  database: 'appdb'
});

function auth(req, res, next) {
  const token = req.cookies.session;
  if (!token) return res.status(401).json({ error: 'unauthorized' });
  // 第 21 行：直接相信 Cookie 里的 userId
  req.user = { id: Number(token) };
  next();
}

// 第 26 行
app.get('/api/profile', auth, async (req, res) => {
  const uid = req.query.user_id || req.user.id;
  const [rows] = await pool.query(`SELECT id, name, phone, bio FROM users WHERE id = ${uid}`);
  if (!rows.length) return res.status(404).json({ error: 'not found' });
  res.json(rows[0]);
});

app.post('/api/transfer', auth, async (req, res) => {
  const { toUserId, amount } = req.body;
  const [r] = await pool.query(
    `UPDATE accounts SET balance = balance - ? WHERE user_id = ? AND balance >= ?`,
    [amount, req.user.id, amount]
  );
  if (r.affectedRows === 0) return res.status(400).json({ error: 'insufficient' });
  await pool.query(`UPDATE accounts SET balance = balance + ? WHERE user_id = ?`, [amount, toUserId]);
  res.json({ ok: true });
});

// 第 44 行
app.get('/render', (req, res) => {
  const name = req.query.name || 'guest';
  res.send(`<html><body><h1>Hello, ${name}</h1></body></html>`);
});

// 第 50 行
app.get('/download', auth, async (req, res) => {
  const target = req.query.target;
  const resp = await fetch(target);
  const buf = Buffer.from(await resp.arrayBuffer());
  res.set('Content-Type', 'application/octet-stream');
  res.send(buf);
});

app.listen(3000);
```

### 你该找出几个？

至少 **5 个**弱点，外加 **1 个"看着像但不是"的排除项**。

---

<details>
<summary>👉 点击展开：代码 2 的答案与解析</summary>

**弱点 1 — 硬编码凭据**

- **CWE**：`CWE-798` Use of Hard-coded Credentials
- **OWASP 归属**：`A07:2025 Authentication Failures`（官方映射清单中有 CWE-798）
- **位置**：第 13 行 `password: 'App@2024!Prod'`
- **根因**：生产数据库口令写死在源码里。源码进入版本库后，口令会永久留存于 Git 历史，即使后续删除也没用；任何能读到代码的人（含外包、离职员工、CI 日志）都拿到凭据。
- **最小验证**：`git log -p -- server.js | grep -i password` 能检索出历史明文。
- **修复**：

  ```javascript
  const pool = mysql.createPool({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,      // 由 Secret Manager / K8s Secret 注入
    database: process.env.DB_NAME,
  });
  ```
  **要点**：修复不只是改这行——**必须轮换这个已泄露的口令**，并清理 Git 历史（`git filter-repo` 等）。只改代码不轮换 = 没修。

**弱点 2 — 凭据/身份完全依赖客户端可控值（认证绕过）**

- **CWE**：`CWE-565` Reliance on Cookies without Validation and Integrity Checking（同时命中 `CWE-287` Improper Authentication、`CWE-302` Authentication Bypass by Assumed-Immutable Data）
- **位置**：第 19～23 行 `auth` 中间件
- **根因**：把 Cookie 的**明文值**直接当作 `userId`，没有任何签名或校验。Cookie 是**客户端存储**，用户随手就能改成任意值。
- **最小验证**：设置 `Cookie: session=1` 以用户 1 的身份访问 `/api/profile`；再改成 `session=2`，若能读到其他用户数据即确认。
- **修复**：

  ```javascript
  const jwt = require('jsonwebtoken');

  function auth(req, res, next) {
    const token = req.cookies.session;
    if (!token) return res.status(401).json({ error: 'unauthorized' });
    try {
      const payload = jwt.verify(token, process.env.JWT_SECRET, { algorithms: ['HS256'] });
      req.user = { id: payload.sub };
    } catch {
      return res.status(401).json({ error: 'unauthorized' });
    }
    next();
  }
  ```
  **要点**：认证令牌必须有**完整性保护**（签名/加密）。同时设 `httpOnly`、`Secure`、`SameSite` 属性。

**弱点 3 — SQL 注入**

- **CWE**：`CWE-89`｜Top 25 第 2 位
- **位置**：第 28 行 `` `SELECT ... WHERE id = ${uid}` ``
- **根因**：模板字符串拼接进 SQL。
- **最小验证**：`GET /api/profile?user_id=1 OR 1=1`。
- **修复**：

  ```javascript
  const uid = Number(req.query.user_id || req.user.id);
  if (!Number.isInteger(uid)) return res.status(400).json({ error: 'bad id' });
  const [rows] = await pool.query(
    'SELECT id, name, phone, bio FROM users WHERE id = ?', [uid]
  );
  ```

**弱点 4 — 水平越权（IDOR）：授权逻辑被用户可控参数覆盖**

- **CWE**：`CWE-639` Authorization Bypass Through User-Controlled Key｜Top 25 第 **24** 位
- **位置**：第 27 行 `const uid = req.query.user_id || req.user.id;`
- **根因**：**这是本条最值得记住的一处**。代码"看起来"有授权——它默认用会话里的 `req.user.id`。但一个 `|| req.query.user_id` 就让**查询参数优先于会话主体**。攻击者只要带上 `?user_id=<任意值>`，就能读取任何人的资料。
  **教训**：授权不能建立在"用户没传这个参数"的假设上。
- **最小验证**：`GET /api/profile?user_id=1002`（自己登录为 1001）。
- **修复**：

  ```javascript
  // 普通用户只能看自己；管理员查看他人需走独立接口并做角色校验
  const uid = req.user.id;
  ```
  如确实需要管理员查看他人资料，**必须显式判断角色**，且该接口应单独审计。

**弱点 5 — 不安全的事务处理（业务逻辑绕过）**

- **CWE**：`CWE-841` Improper Enforcement of Behavioral Workflow（并命中 `CWE-362` Race Condition 的潜在风险）
- **OWASP 归属**：`A06:2025 Insecure Design`（官方映射清单中有 CWE-841、CWE-362）
- **位置**：第 33～40 行 `/api/transfer`
- **根因**：转账是**两步 UPDATE**（扣款 + 入账），但**没有放在同一个事务里**，也没有幂等键：
  - 第 2 步失败（如 `toUserId` 不存在、数据库报错）时，第 1 步的扣款已经生效 → **钱凭空消失**。
  - 并发重复提交可导致重复入账 → **钱凭空增加**。
  - 缺少收款方校验（`toUserId` 完全由客户端给，未验证其存在与状态）。
- **最小验证**：在授权测试环境，(a) 用不存在的 `toUserId` 调用，查付款方余额是否被扣；(b) 并发发送同一请求，查是否重复入账。
- **修复**：

  ```javascript
  app.post('/api/transfer', auth, async (req, res) => {
    const { toUserId, amount, idempotencyKey } = req.body;
    const amt = Number(amount);
    if (!Number.isInteger(amt) || amt <= 0) return res.status(400).json({ error: 'bad amount' });

    const conn = await pool.getConnection();
    try {
      await conn.beginTransaction();

      // 幂等：同一 key 只处理一次
      const [dup] = await conn.query(
        'SELECT 1 FROM transfers WHERE idem_key = ? FOR UPDATE', [idempotencyKey]);
      if (dup.length) { await conn.rollback(); return res.json({ ok: true, dup: true }); }

      const [r] = await conn.query(
        'UPDATE accounts SET balance = balance - ? WHERE user_id = ? AND balance >= ?',
        [amt, req.user.id, amt]);
      if (r.affectedRows === 0) throw new Error('insufficient');

      const [r2] = await conn.query(
        'UPDATE accounts SET balance = balance + ? WHERE user_id = ? AND status = ?',
        [amt, toUserId, 'active']);
      if (r2.affectedRows === 0) throw new Error('invalid payee');

      await conn.query('INSERT INTO transfers (idem_key, from_user, to_user, amount) VALUES (?,?,?,?)',
        [idempotencyKey, req.user.id, toUserId, amt]);

      await conn.commit();
      res.json({ ok: true });
    } catch (e) {
      await conn.rollback();
      res.status(400).json({ error: e.message });
    } finally {
      conn.release();
    }
  });
  ```
  **要点**：(a) 事务包裹；(b) 校验收款方是否存在且可收款；(c) 幂等键防重复；(d) 行锁防并发。

**弱点 6 — 跨站脚本 XSS**

- **CWE**：`CWE-79`｜Top 25 第 **1** 位（分值 60.38，几乎是第二名的两倍）
- **位置**：第 45～47 行 `/render`，`res.send(\`<h1>Hello, ${name}</h1>\`)`
- **根因**：把查询参数**未编码**地插入 HTML 输出上下文。
- **最小验证**：`/render?name=<img src=x onerror=alert(document.domain)>`，浏览器弹出即确认。
- **修复**：

  ```javascript
  const escapeHtml = (s) => String(s).replace(/[&<>"']/g,
    c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

  app.get('/render', (req, res) => {
    const name = escapeHtml(req.query.name || 'guest');
    res.type('html').send(`<html><body><h1>Hello, ${name}</h1></body></html>`);
  });
  ```
  生产项目应使用成熟的模板引擎（EJS/Handlebars/Nunjucks 等**默认转义**的配置），而不是手工拼接字符串。

**弱点 7 — 服务端请求伪造（SSRF）**

- **CWE**：`CWE-918`｜Top 25 第 **22** 位
- **位置**：第 51～56 行 `/download`，`await fetch(target)` 且 `target` 直接来自查询参数
- **根因**：让服务端请求用户指定 URL，且**无任何目标地址限制**。
- **放大价值**：可访问云元数据端点（如 `http://169.254.169.254/...`）窃取实例凭据，或探测内网资产。同时该接口把响应**原样返回**给攻击者，等于给了"读内网"的能力，危害远高于盲 SSRF。
- **最小验证**：在测试环境 `GET /download?target=http://169.254.169.254/latest/meta-data/`（若有该元数据服务），或指向内网一个仅内网可达的服务，确认能取到内容。
- **修复**：

  ```javascript
  const ALLOWED_HOSTS = new Set(['files.example.com', 'cdn.example.com']);
  const dns = require('dns').promises;
  const net = require('net');

  function isPrivateIp(ip) {
    // 覆盖 10/8、172.16/12、192.168/16、127/8、169.254/16、0.0.0.0、::1、fc00::/7 等
    // 生产实现建议使用成熟库，如 ip-address / netmask
    ...
  }

  app.get('/download', auth, async (req, res) => {
    let u;
    try { u = new URL(req.query.target); } catch { return res.status(400).json({ error: 'bad url' }); }

    if (!['http:', 'https:'].includes(u.protocol)) return res.status(400).json({ error: 'bad protocol' });
    if (!ALLOWED_HOSTS.has(u.hostname))              return res.status(403).json({ error: 'host not allowed' });

    // 解析后校验 IP，防止白名单域名被解析到内网
    const { address } = await dns.lookup(u.hostname);
    if (isPrivateIp(address)) return res.status(403).json({ error: 'private ip' });

    const resp = await fetch(u, { redirect: 'manual' });   // 关键：不自动跟随重定向
    ...
  });
  ```
  **四个必须覆盖的绕过点**（缺一个都不算修好，详见 [audit-guide CWE-918](./audit-guide.md#12-cwe-918-服务端请求伪造ssrf)）：
  1. **重定向**：必须 `redirect: 'manual'`，或对每一跳重新校验；
  2. **DNS 重绑定 / TOCTOU**：解析校验与实际连接可能不是同一个 IP，最稳的做法是**连接到已校验的 IP**并设置 `Host` 头；
  3. **各种地址表示**：`http://2130706433/`、`http://[::1]/`、`http://expected.com@169.254.169.254/`；
  4. **协议**：白名单只允许 `http:` / `https:`。

**排除项（看着像但不是）**

- **第 35～37 行的参数化查询不是 SQL 注入**：

  ```javascript
  `UPDATE accounts SET balance = balance - ? WHERE user_id = ? AND balance >= ?`,
  [amount, req.user.id, amount]
  ```
  这是**正确的参数绑定**，`?` 由驱动替换为安全的字面量。**不要因为它出现在一个有问题的方法里就一并报为注入。**
  （不过 `amount` 的**类型/范围**未校验是另一个真实问题——属于输入校验与业务逻辑范畴，见弱点 5。）

**本段代码的弱点链**

```
改 Cookie: session=999
   └─ CWE-565/287/302 认证完全基于客户端可控值 → 冒充任意用户
        └─ 该 Cookie 可被 XSS(CWE-79) 窃取 → 会话劫持

GET /api/profile?user_id=1002
   └─ CWE-639 用户可控键覆盖会话主体 → 读任意用户资料
        └─ CWE-89 SQL 注入（同一处）
             └─ 库内凭据已因 CWE-798 硬编码而暴露

POST /api/transfer 失败/并发
   └─ CWE-841 事务与幂等缺失 → 资金不一致

GET /download?target=http://169.254.169.254/...
   └─ CWE-918 SSRF → 窃取云凭据 → 云环境失陷
```

</details>

---

## 代码 3：Java Spring Boot 文档预览服务

```java
// DocController.java  ——  虚构代码，仅用于教学
package com.example.doc;

import java.io.*;
import java.net.*;
import javax.servlet.http.*;

@RestController
public class DocController {

    private static final String DOC_ROOT = "/opt/app/docs/";

    @GetMapping("/api/doc/preview")
    public void preview(@RequestParam String path, HttpServletResponse response) throws Exception {
        // 第 15 行
        File f = new File(DOC_ROOT + path);
        response.setContentType("text/plain");
        try (InputStream in = new FileInputStream(f)) {
            in.transferTo(response.getOutputStream());
        }
    }

    @GetMapping("/api/doc/import")
    public String importFromUrl(@RequestParam String url) throws Exception {
        // 第 24 行
        URL u = new URL(url);
        HttpURLConnection conn = (HttpURLConnection) u.openConnection();
        conn.setConnectTimeout(3000);
        try (BufferedReader r = new BufferedReader(new InputStreamReader(conn.getInputStream()))) {
            StringBuilder sb = new StringBuilder();
            String line;
            while ((line = r.readLine()) != null) sb.append(line);
            return sb.toString();
        }
    }

    @PostMapping("/api/doc/template")
    public String render(@RequestBody String tmpl, @RequestParam String name) throws Exception {
        // 第 37 行：使用模板引擎渲染"用户提交的模板文本"
        TemplateEngine engine = new TemplateEngine();
        Map<String, Object> vars = new HashMap<>();
        vars.put("name", name);
        return engine.process(tmpl, vars);
    }

    @PostMapping("/api/doc/restore")
    public String restore(@RequestBody byte[] body) throws Exception {
        // 第 46 行
        try (ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(body))) {
            Object o = ois.readObject();
            return "restored: " + o.getClass().getName();
        }
    }
}
```

### 你该找出几个？

至少 **4 个**弱点，外加 **1 个"看着像但不是"的排除项**。

---

<details>
<summary>👉 点击展开：代码 3 的答案与解析</summary>

**弱点 1 — 路径穿越**

- **CWE**：`CWE-22`｜Top 25 第 **6** 位
- **位置**：第 15～19 行 `new File(DOC_ROOT + path)`
- **根因**：字符串拼接路径，未限制在 `DOC_ROOT` 内。`path = "../../etc/passwd"` 或 `path = "/etc/passwd"`（Java 拼接时绝对路径不会丢弃前段，但 `../` 仍会生效）可读出任意文件。
- **额外风险**：**该接口没有任何认证**，未认证即可读文件 → 同时命中 `CWE-306`。
- **最小验证**：`GET /api/doc/preview?path=../../../../etc/passwd`（测试环境）。
- **修复**：

  ```java
  private static final Path DOC_ROOT = Paths.get("/opt/app/docs").toRealPath();

  @GetMapping("/api/doc/preview")
  @PreAuthorize("hasRole('USER')")                    // 补上授权
  public void preview(@RequestParam String path, HttpServletResponse response) throws Exception {
      // 只取文件名，从根上消除目录成分
      Path target = DOC_ROOT.resolve(Paths.get(path).getFileName()).normalize().toRealPath();

      if (!target.startsWith(DOC_ROOT)) {
          response.sendError(HttpServletResponse.SC_BAD_REQUEST, "invalid path");
          return;
      }
      response.setContentType("application/octet-stream");   // 不要用 text/plain 之外的推断
      try (InputStream in = Files.newInputStream(target)) {
          in.transferTo(response.getOutputStream());
      }
  }
  ```
  **要点**：(a) 用 `Path.normalize()` + `toRealPath()` 解析符号链接；(b) `startsWith(DOC_ROOT)` 做目录约束；(c) 关于 `text/plain`：**保持固定 Content-Type 而不是由输入决定**，可避免 MIME 混淆带来的问题。

**弱点 2 — SSRF**

- **CWE**：`CWE-918`｜Top 25 第 **22** 位
- **位置**：第 23～31 行 `/api/doc/import`
- **根因**：`new URL(url)` 后直接 `openConnection()`，目标完全由用户指定。
- **放大因素**：该接口把响应正文**原样返回**，是可读型 SSRF；且**无认证**，外部可直接打。
- **最小验证**：`GET /api/doc/import?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/`（若在云上）。
- **修复**：同 [audit-guide CWE-918](./audit-guide.md#12-cwe-918-服务端请求伪造ssrf) 的四点要求。Java 版本的要点：

  ```java
  @GetMapping("/api/doc/import")
  @PreAuthorize("hasRole('USER')")
  public String importFromUrl(@RequestParam String url) throws Exception {
      URI uri = new URI(url);
      if (!Set.of("http", "https").contains(uri.getScheme())) throw new IllegalArgumentException("bad scheme");
      InetAddress addr = InetAddress.getByName(uri.getHost());       // 解析
      if (addr.isAnyLocalAddress() || addr.isLoopbackAddress()
          || addr.isLinkLocalAddress() || addr.isSiteLocalAddress()
          || addr.isMulticastAddress()) {
          throw new IllegalArgumentException("private address");
      }
      // 生产环境还应：不自动跟随重定向；连接到已校验的 IP 并设置 Host 头；
      // 出站网络层做白名单（最可靠）
      ...
  }
  ```
  **注意**：`InetAddress.is*` 系列**覆盖不全**（例如不覆盖 CGNAT 段与 IPv6 唯一本地地址），生产实现应使用成熟的内网地址判定库，并在网络层再加一道出站策略。

**弱点 3 — 服务端模板注入（SSTI）**

- **CWE**：`CWE-94` Improper Control of Generation of Code ('Code Injection')｜Top 25 第 **10** 位
- **位置**：第 36～41 行 `/api/doc/template`，`engine.process(tmpl, vars)`，其中 `tmpl` 来自**请求体**
- **根因**：**这是本段最隐蔽、也最容易被漏判的一条。**
  模板引擎的问题不在于"渲染模板"，而在于**谁控制模板文本**：
  - 用户控制**变量值** → 安全（引擎会转义/按值处理）；
  - 用户控制**模板文本** → 危险（可以写模板语法去访问宿主语言运行时）。
  这里 `tmpl` 就是模板文本，因此攻击者可以在模板里写表达式去调用任意方法、读环境变量、执行命令（取决于是哪个引擎及其沙箱强度）。
- **最小验证**：提交一个用于探测"是否会被求值"的模板（例如尝试输出一个由表达式计算出的值而非字面量）。**在测试环境做。**
- **修复**：

  ```java
  // 正确做法：模板文本由服务端固定，用户只能提供变量值
  @PostMapping("/api/doc/render")
  @PreAuthorize("hasRole('USER')")
  public String render(@RequestParam String name) {
      Context ctx = new Context();
      ctx.setVariable("name", name);                       // 值，不是模板
      return engine.process("doc-view", ctx);              // 模板名，由服务端解析
  }
  ```
  **要点**：把接口从"接受模板文本"改成"接受模板名 + 变量值"。**这类弱点无法靠"过滤模板字符串"修好**，必须改设计。

**弱点 4 — 反序列化不可信数据**

- **CWE**：`CWE-502` Deserialization of Untrusted Data｜Top 25 第 **15** 位（**KEV 计数 11**）
- **位置**：第 45～49 行 `/api/doc/restore`，`new ObjectInputStream(...).readObject()`
- **根因**：Java 原生反序列化会把字节流**还原成对象并触发其 `readObject` / `readResolve` 等回调**，利用类路径上的 gadget 链可直接实现 RCE。而这里的字节流来自**请求体**，完全不可信；接口**也没有认证**。
- **识别特征**：Java 序列化流以魔数 `AC ED 00 05` 开头，Base64 后通常以 **`rO0AB`** 开头。抓包看到请求体以此为前缀，几乎可以确定是原生 Java 反序列化入口。
- **最小验证**：在测试环境用一个已知的、无害的探测 gadget（如触发 DNS 查询而非命令执行的链）确认反序列化确实被触发。**切勿在生产或未授权环境测试。**
- **修复**：

  ```java
  // 首选：彻底不用原生 Java 反序列化，改用 JSON（Jackson/Gson）
  @PostMapping("/api/doc/restore")
  @PreAuthorize("hasRole('USER')")
  public RestoreResult restore(@RequestBody DocDto dto) {     // 结构化绑定，不是 readObject
      ...
  }
  ```
  如果因兼容性**必须**反序列化，则必须：
  1. 加认证与授权；
  2. 使用**对象输入过滤器**白名单（`ObjectInputFilter`，JDK 9+），只允许预期的类；
  3. 反序列化前先验证签名/MAC（若数据由可信方产生）；
  4. 在受限进程中处理，并对返回内容不回显对象信息。

  ```java
  ObjectInputFilter filter = ObjectInputFilter.Config.createFilter(
      "com.example.doc.dto.*;java.base/*;!*");     // 只允许白名单，其余全部拒绝
  ois.setObjectInputFilter(filter);
  ```
  **要点**："只允许白名单 + 拒绝其他一切"（`!*`）是关键，黑名单（列举已知 gadget）永远赶不上新链的发现速度。

**排除项（看着像但不是）**

- **第 26 行的 `conn.setConnectTimeout(3000)` 不是"SSRF 防护措施"**，虽然它看起来像在做安全加固。
  设置超时只能**限制耗时**，完全不能阻止请求发往内网——攻击者照样能读到内网服务的内容。**看到超时配置就判"已有 SSRF 防护"是十分常见的误判。**
  真正的防护必须包含**目标地址限制**（协议白名单 + 主机白名单 + 解析后 IP 校验 + 不跟随重定向 + 网络层出站策略）。

**本段代码的弱点链**

```
GET /api/doc/preview?path=../../../../etc/passwd
   └─ CWE-306 无认证 + CWE-22 路径穿越 → 匿名读任意文件

GET /api/doc/import?url=http://169.254.169.254/...
   └─ CWE-306 无认证 + CWE-918 SSRF → 窃取云实例凭据 → 云环境失陷

POST /api/doc/template  { 恶意模板 }
   └─ CWE-94 SSTI → 通过模板语法触达宿主运行时 → RCE

POST /api/doc/restore   [AC ED 00 05 ...]
   └─ CWE-502 反序列化 → gadget 链 RCE
```

</details>

---

## 进阶实验：把弱点归类成修复任务

拿到上面 3 段代码的全部答案后，做一次**归类合并**——这是 [审计指南第 5 节](./audit-guide.md#审计工作流建议) 要求的最后一步。

### 任务

1. 把三段代码里所有确认的弱点**按 CWE 合并**，统计每类出现几次。
2. 对每一类，写出**一条**修复方案（而不是每处写一条），以及**这条方案能不能批量消除该类问题**。

### 参考答法（示例）

| CWE | 出现位置 | 次数 | 一条修复方案 | 能否批量消除 |
| --- | --- | --- | --- | --- |
| CWE-89 SQL 注入 | 代码1 第15行、代码2 第28行 | 2 | 建立"所有 SQL 必须参数化"的编码规范 + CI 中加入 SAST 规则 + 禁止自定义拼接 SQL 的高危 API（`raw`/`extra`） | ✅ 可以——改规范 + 上工具 |
| CWE-862/639 授权缺失/越权 | 代码1 第15行、代码2 第27行、代码3 第15行 | 3 | 引入统一的**服务端资源授权组件**，要求"每条查询必须携带主体约束或显式声明为公开资源" | ✅ 可以——但要改设计，不是改一行 |
| CWE-22 路径穿越 | 代码1 第22行、代码3 第15行 | 2 | 提供统一的 `safeJoin(base, untrusted)` 工具函数，纳入代码规范并禁止直接 `open(base + user)` | ✅ 可以 |
| CWE-78/94 RCE 类 | 代码1 第35行、代码3 第37行、代码3 第46行 | 3 | 禁用清单：不走 shell 执行命令；不接受用户提交的模板文本；不使用原生反序列化 | ✅ 可以——靠架构与规范约束 |
| CWE-918 SSRF | 代码2 第51行、代码3 第23行 | 2 | 提供统一的"出站请求"组件，内置协议/主机/IP/重定向四道校验 + 网络层出站白名单 | ✅ 可以 |
| CWE-798 硬编码凭据 | 代码2 第13行 | 1 | 全面改用 Secret Manager 注入 + CI 加密钥扫描 + 轮换历史泄露口令 | ✅ 可以 |

**这次归并的价值在于让下面这个结论变得清晰**：

> 12 个技术发现，本质上是 **6 类弱点**；其中 4 类可以靠**一次规范/工具改造**批量消除，不需要逐个修。

这就是 CWE 的核心方法论——**从"修漏洞"转向"消灭弱点类"。**

---

## 总验收清单

- [ ] 代码 1 找出 ≥4 个弱点，且写明了"SQL 注入让 file_path 可控 → 放大为路径穿越"这条链
- [ ] 代码 1 识别出"读出了 owner_id 却没做授权"这个真正的弱点
- [ ] 代码 2 找出 ≥5 个弱点，且指出 `|| req.query.user_id` 是 IDOR 的关键
- [ ] 代码 2 识别出转账接口的**事务与幂等问题**（不只是"没校验金额"）
- [ ] 代码 2 的排除项：正确判定参数化查询**不是**注入
- [ ] 代码 3 找出 ≥4 个弱点，且识别出 **SSTI 的本质是"用户控制了模板文本"**
- [ ] 代码 3 写出 CWE-502 的关键修复要点：**白名单 + `!*` 拒绝其余**，而不是黑名单
- [ ] 代码 3 的排除项：正确判定 `setConnectTimeout` **不是** SSRF 防护
- [ ] 每个弱点都写了 CWE 编号与**官方名称**（到 cwe.mitre.org 核对了名称）
- [ ] 每个弱点都写了"误报排除考虑"
- [ ] 建议的修复都**可执行**（不出现"加强校验"、"注意安全"这类空话）
- [ ] 完成了进阶实验的归类合并，得出了"几类弱点、哪几类可批量消除"的结论
- [ ] 全程只在隔离/授权环境验证，未对任何未授权系统发起测试

---

## 常见判定错误自查

| 错误 | 纠正 |
| --- | --- |
| 把"数据被取出"当成弱点 | 弱点是"缺少控制"，不是"读了字段" |
| 把有问题的同一段代码全部标红 | 同一段里参数化查询是安全的，必须逐句判定 |
| 看到 `int()` / `Number()` 转换就判无注入 | 正确，但要注意转换失败的处理路径与类型边界 |
| 看到超时/长度限制就判"已有防护" | 超时≠地址限制；长度限制≠输出编码 |
| 用黑名单（如"禁止 `../`"）当修复 | 编码、双重编码、反斜杠、Unicode 归一化都能绕过；应用白名单 + 规范化后校验 |
| 把 SSRF 和开放重定向混为一谈 | SSRF 是服务端发请求，开放重定向（CWE-601）是让浏览器跳转，影响面完全不同 |
| 把 CWE-862 和 CWE-639 混用 | 862 是"没检查"，639 是"检查了但依据可被用户控制" |
| 把 CWE-78 和 CWE-88 混用 | 78 是能执行额外命令；88 是只改变参数语义（如 `--output=/etc/passwd`） |
| 只写"这里有反序列化" | 必须补：数据是否不可信 + 是否有白名单 + 是否有认证，三者共同决定是否成立 |

---

## 来源 URL

- 2025 CWE Top 25（本页所有 CWE 编号、官方名称、排名的来源）：<https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html>
- CWE Top 25 门户（年份与数据集规模）：<https://cwe.mitre.org/top25/>
- CWE 条目官方定义（核对名称与 `Potential Mitigations`）：`https://cwe.mitre.org/data/definitions/<数字>.html`
  - 本页涉及：CWE-22、77、78、79、89、94、113、287、302、306、362、434、502、565、601、639、798、841、862、863、918
- CWE 数据索引（层级与视角关系，用于理解父子弱点）：<https://cwe.mitre.org/data/index.html>
- OWASP Top 10:2025（用于本页的 OWASP 归属）：
  - 引言（十个分类）：<https://owasp.org/Top10/2025/0x00_2025-Introduction/>
  - A01 Broken Access Control：<https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/>
  - A05 Injection：<https://owasp.org/Top10/2025/A05_2025-Injection/>
  - A06 Insecure Design：<https://owasp.org/Top10/2025/A06_2025-Insecure_Design/>
  - A07 Authentication Failures：<https://owasp.org/Top10/2025/A07_2025-Authentication_Failures/>
  - A08 Software or Data Integrity Failures：<https://owasp.org/Top10/2025/A08_2025-Software_or_Data_Integrity_Failures/>

> ⚠️ **说明**
> 1. 三段代码均为**为本实验编写的虚构代码**，未从任何真实项目复制，其中的域名、路径、凭据均为占位值。示例中出现的 `App@2024!Prod` 是**故意编造的示例口令**，请勿在任何真实系统中使用类似形式。
> 2. 修复代码是**教学级实现**，用于说明修复方向。生产使用需要考虑并发、错误处理、日志脱敏、性能等完整工程约束；其中 SSRF 的 IP 判定、反序列化过滤器、路径规范化等都有成熟的库可用，**优先使用成熟库而非自行实现**。
> 3. `CWE-113`、`CWE-565`、`CWE-287`、`CWE-302`、`CWE-841`、`CWE-601` 等编号在 **2025 CWE Top 25 中未出现**（Top 25 只有 25 条），它们来自 CWE 官方定义库与 OWASP Top 10:2025 的映射清单。本页已分别注明其来源，未把它们混入 Top 25 的排名叙述。
> 4. 本页对 `os.path.join`、`Path.normalize`、`InetAddress.is*` 系列等 API 行为的描述，属于通行认知，**具体版本的边界行为请以官方文档为准**并实际测试。
