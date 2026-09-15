# Gophish（钓鱼演练平台）

> **一句话**：一个开源的**钓鱼模拟与安全意识培训平台**——建模板、导入目标名单、设定发送节奏、实时看"谁点了谁输了口令"，并自动生成报表。
> **分类**：社会工程 / 安全意识演练 ｜ **Kali 包**：`gophish`（命令 `gophish-start`、`gophish-stop`）｜ **官方文档**：<https://getgophish.com/documentation/> ｜ 项目：<https://github.com/gophish/gophish>

---

## 1. 它解决什么问题

[`set.md`](set.md) 的 SET 适合"演示一次钓鱼长什么样"。但企业做**安全意识演练**时，需求是不一样的：

| 企业演练的真实需求 | SET | **Gophish** |
|--------------------|-----|-------------|
| 一次发给 500 人，**分批发、控制节奏** | ❌ 手工 | ✅ 时间线 + 目标组 |
| 实时看**谁打开了、谁点了链接、谁提交了口令** | 弱 | ✅ **仪表盘 + 事件时间线** |
| 出**报表**给管理层（点击率/提交率/上报率） | ❌ | ✅ 内置报表 + 导出 |
| 多个**模板**复用与版本管理 | ❌ | ✅ Landing Page / Email Template 独立管理 |
| **API 集成**（接 HR 系统、自动同步名单） | ❌ | ✅ 完整 REST API |
| 留**合规记录**（发了谁、什么时候、结果） | ❌ | ✅ 全流程落库 |
| 生成**恶意载荷**配合 C2 | ✅ | ❌ 不做载荷（**这是刻意的定位**） |

**一句话定位**：**Gophish 是"钓鱼演练的度量与流程工具"，不是攻击工具**。它的设计目标就是让人**可重复、可量化、可合规**地测试「员工会不会被钓」以及「我们的邮件防护有没有用」。

对比同类：

| 工具 | 定位 | 差异 |
|------|------|------|
| **Gophish** | 演练平台 | 模板/分组/时间线/报表/API；不做载荷 |
| **`set`** | 社工手法工具箱 | 各种社工向量（Web/邮件/介质/短信）；统计弱；见 [`set.md`](set.md) |
| **商业平台**（KnowBe4、Cofense 等） | 商业演练 | 内容库更大、合规报告更完善 |
| **`dnstwist`** | 仿冒域名研究 | 辅助场景真实性（域名像不像）；Kali 清单中有 |

---

## 2. 工作原理

```
┌──────────────── Kali ────────────────────────────────┐
│ gophish（单一 Go 二进制）                              │
│   ├─ Admin Server（默认 https://127.0.0.1:3333）      │
│   │     └─ Web UI + REST API（/api/…，用 API Key 认证）│
│   ├─ Phishing Server（默认 0.0.0.0:80 / :443）        │
│   │     ├─ GET /?rid=xxxx   → 返回 Landing Page（打开记录）│
│   │     ├─ POST /?rid=xxxx  → 记录提交的字段（凭据记录）│
│   │     └─ GET /static/…    → 附件/图片               │
│   └─ SQLite 数据库（gophish.db，默认在同目录）          │
└──────────────────────────────────────────────────────┘
        ▲                      ▲
        │ 发件（SMTP）          │ 目标点击（HTTP/HTTPS）
        │                      │
   ┌────┴────┐          ┌──────┴──────────────────────┐
   │ SMTP 服务 │          │ 目标员工（浏览器）            │
   └─────────┘          │  · 邮件里带唯一 rid 链接       │
                        │  · 打开 → 记录 Open/Click      │
                        │  · 提交表单 → 记录 Submitted   │
                        └───────────────────────────────┘
```

### 核心概念（**理解这五个对象，就会用 Gophish**）

| 对象 | 是什么 | 关键点 |
|------|--------|--------|
| **Sending Profile** | 发件配置（SMTP 服务器、端口、凭据、发件人） | 用**自有演练域名**；SPF/DKIM/DMARC 要配好 |
| **Landing Page** | 落地的"登录页" | 两种来源：**手工导入 HTML**（推荐）或 **Import Site**（抓取真实站点） |
| **Email Template** | 邮件正文 | 支持 `{{.FirstName}}`、`{{.URL}}`、`{{.TrackingURL}}` 等**模板变量**；用 `{{.URL}}` 做唯一追踪链接 |
| **Users & Groups** | 目标名单（CSV/手工） | 字段：`First Name`、`Last Name`、`Email`、`Position`；**只能导入你被授权测试的名单** |
| **Campaign** | 一次演练（= 模板 + 页面 + 分组 + 时间线） | 启动后自动发信，实时记录事件 |

### 事件模型（**报表就是基于这四个事件**）

| 事件 | 触发条件 | 含义 |
|------|----------|------|
| **Email Sent** | SMTP 投递成功 | 邮件已发出 |
| **Email Opened** | 邮件内的**追踪像素**被加载 | 员工打开了邮件（**注意：图片被代理预览会误报**） |
| **Clicked Link** | 访问 `{{.URL}}` | 员工点了链接（**最关键的行为指标之一**） |
| **Submitted Data** | 在 Landing Page 提交了表单 | **最严重**：员工输入了凭据 |
| **Email Reported** | 员工点了"上报钓鱼"按钮/插件 | **最希望看到的指标**（上报率体现安全意识） |

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install gophish
command -v gophish-start gophish-stop
```

启动：

```bash
sudo gophish-start
```

```console
[*] Web UI: https://127.0.0.1:3333
[i] You might need to refresh your browser once it opens

 Default credentials:
   user: admin
   password: kali-gophish
```

> **Kali 打包版本默认口令是 `admin / kali-gophish`**（上游官方版本是 `admin / gophish`，首次登录会强制改）。**上线前必须改掉。**

浏览器打开 `https://127.0.0.1:3333`（**自签证书，需在浏览器里点"继续访问"**），用默认口令登录 → 立即修改口令。

停止：

```bash
sudo gophish-stop
```

配置（端口、数据库、TLS）：

```bash
sudo find / -name 'config.json' -path '*gophish*' 2>/dev/null
```

```console
/etc/gophish/config.json
```

```json
{
  "admin_server": {
    "listen_url": "127.0.0.1:3333",
    "use_tls": true,
    "cert_path": "gophish_admin.crt",
    "key_path": "gophish_admin.key"
  },
  "phish_server": {
    "listen_url": "0.0.0.0:80",
    "use_tls": false
  },
  "db_name": "sqlite3",
  "db_path": "gophish.db",
  "migrations_prefix": "db/db_"
}
```

**关键点**：

- **`admin_server.listen_url`** 默认只监听 `127.0.0.1` → 远程管理需改成内网地址（**不要暴露到公网**）；
- **`phish_server.listen_url`** 是**目标要访问的地址**（钓鱼页监听）→ 必须是目标可达的 IP:端口；用 443 + 真实证书效果最好；
- **`use_tls`**：管理界面用 HTTPS（自签即可）；钓鱼服务器若对外，建议用**可信证书**（否则浏览器警告会直接暴露）。

---

## 4. 核心参数详解

Gophish 没有命令行参数（就两个启动脚本），真正的"参数"是 **Web UI 表单字段 + API 字段**。下面按对象列出最关键的字段。

### 4.1 Sending Profile（发件配置）

| 字段 | 作用 | 使用建议 |
|------|------|----------|
| `Name` | 配置名 | 如 `lab-smtp` |
| `Interface Type` | SMTP 类型 | 一般选 `SMTP` |
| `Host` / `Port` | SMTP 服务器 | 用**自有演练域名的 SMTP**（不要用公共邮箱） |
| `Username` / `Password` | 认证 | 用专用账号（**别用个人邮箱**） |
| `From` | 发件人显示 | 如 `IT 服务台 <it-helpdesk@drill.example.com>` |
| `Ignore Certificate Errors` | 忽略 TLS 证书错误 | 自建 SMTP 时可能需要 |
| `Envelope Sender`（如有） | 信封发件人 | 与 SPF 对齐 |

### 4.2 Landing Page（落地页）

| 字段 | 作用 | 使用建议 |
|------|------|----------|
| `Name` | 页面名 | —— |
| `Import Site` | **抓取真实站点**生成页面 | **只抓你有权测试的站点**；抓取结果常需手工修 |
| `HTML`（源码视图） | 手工编辑页面 | **推荐**：自己写一个简单登录页，可控且不涉及他人版权 |
| `Capture Submitted Data` | **记录提交的表单字段** | 演练核心功能（**勾选前想清楚合规要求**） |
| `Capture Passwords` | 额外记录密码字段 | **很多组织禁止勾选**——只统计"是否提交"而不保存口令 |
| `Redirect To` | 提交后跳转的真实地址 | 让员工"看起来登录成功了"，减少怀疑 |
| `URL`（生成的追踪链接） | 每个目标唯一链接 | 用于区分"谁点了" |

### 4.3 Email Template（邮件模板）

| 字段 | 作用 | 说明 |
|------|------|------|
| `Name` | 模板名 | —— |
| `Subject` | 主题 | 演练建议加统一标记（或演练后说明） |
| `Text` / `HTML` | 正文 | 支持 HTML |
| `{{.FirstName}}` / `{{.LastName}}` / `{{.Position}}` | 目标字段变量 | 「个性化」是提升点击率的手法，演练中可用 |
| **`{{.URL}}`** | **唯一追踪链接** | **必须有**（点击统计依赖它） |
| `{{.TrackingURL}}` | 追踪像素链接 | 打开统计依赖它（Gophish 会自动注入） |
| `{{.BaseURL}}` | 钓鱼服务器 Base URL | 用于引用附件/静态资源 |
| `Add Files` | 附件 | 演练可用无害附件（如 PDF）；**不要用真实恶意文件** |

### 4.4 Users & Groups（目标名单）

CSV 格式（**第一行是表头，字段名要对应**）：

```csv
First Name,Last Name,Email,Position
Alice,Chen,alice.chen@drill.example.com,财务部
Bob,Li,bob.li@drill.example.com,研发部
```

### 4.5 Campaign（演练）

| 字段 | 作用 | 使用建议 |
|------|------|----------|
| `Name` | 演练名 | 如 `2026-Q1-安全意识演练` |
| `Email Template` | 使用哪个模板 | —— |
| `Landing Page` | 使用哪个页面 | —— |
| `URL` | 生成的追踪 URL 前缀 | **必须是目标可达的地址**（`phish_server` 的地址） |
| `Launch Date` | 开始时间 | 与演练窗口对齐 |
| `Send Emails By` | 在此时刻前发完 | **控制发送节奏**（避免触发邮件限流/被识别为群发） |
| `Sending Profile` | 用哪个发件配置 | —— |
| `Groups` | 发给哪些组 | **只能是你被授权测试的名单** |

### 4.6 API（**自动化与集成**）

| 项目 | 说明 |
|------|------|
| API Key 位置 | Web UI → `Account Settings` → `API Key` |
| 认证方式 | 请求头 `Authorization: <API_KEY>` |
| Base URL | `https://127.0.0.1:3333/api/` |
| 常用端点 | `/api/campaigns/`、`/api/templates/`、`/api/pages/`、`/api/groups/`、`/api/smtp/`、`/api/campaigns/{id}/results` |
| 典型用途 | 从 HR/IAM 系统同步名单、批量创建演练、自动拉取结果生成周报 |

---

## 5. 实战演练

> **环境声明（与 SET 同样严格）**：
> 本演练**只能**在以下环境进行：① **企业已批准的安全意识演练**（有制度依据、告知程序、管理层批准）；② **自建的实验环境**（你自己的域名、自己的邮箱、你自己的测试账号）。
> **必须做到**：只发给**已批准的演练名单**；**设置 `Capture Passwords=false`**（只统计提交行为，不保存真实口令）；演练后**立即清理并澄清**。
> **绝对禁止**：对真实员工、真实邮箱、你无授权的组织发起任何钓鱼活动——这可能触犯《刑法》第 285 条、**第 253 条之一（侵犯公民个人信息罪）**、《网络安全法》《个人信息保护法》。

### 场景 1：自建实验环境，跑通第一次演练

**Step 1：准备"演练域"与邮件出口**

```bash
# 实验环境建议：
#  - 一个自有域名（如 drill.lab）与其 SMTP（或本机 MailHog/Mailpit 收信测试）
#  - 或完全内网：用一台你能控制的 SMTP（如 postfix）作为发件服务

# 本机快速起一个"收信服务器"（用于验证邮件确实发出，不适合演练真人）
# 可用 MailHog / Mailpit 之类的测试 SMTP
docker run -d --name mailpit -p 1025:1025 -p 8025:8025 axllent/mailpit
```

**Step 2：启动 Gophish 并登录**

```bash
sudo gophish-start
```

```console
[*] Web UI: https://127.0.0.1:3333
 Default credentials:
   user: admin
   password: kali-gophish
```

```bash
# 浏览器打开（自签证书需手动接受）
firefox https://127.0.0.1:3333 &
```

登录后**第一件事：改口令**（右上角 → Account Settings）。

**Step 3：建 Sending Profile（指向你的测试 SMTP）**

```
Sending Profiles → New Profile
  Name:       lab-smtp
  Host:       127.0.0.1:1025         （示例：Mailpit 的 SMTP 端口）
  Username:   （留空或按你的配置）
  Password:   （留空或按你的配置）
  From:       IT 服务台 <it-helpdesk@drill.example.com>
  → Send Test Email → 填你自己的邮箱 → 检查收件箱（或 Mailpit 的 8025 Web UI）
```

**解读**：**先能发出去，再谈演练。** `Send Test Email` 是最容易漏掉的一步——它能在几分钟内发现 SMTP/SPF/TLS 的问题。

**Step 4：建 Landing Page（**自己写**，不抓别人站点）**

```
Landing Pages → New Page
  Name:   drill-login
  HTML:   （粘贴下面这段）
  勾选：  Capture Submitted Data
  勾选：  Capture Passwords          ← 生产演练中很多组织选择【不勾】
  Redirect To: https://intranet.drill.example.com/   （真实的内部首页，或一个"感谢参与"页）

  → Save Page
```

```html
<!doctype html>
<html><head><meta charset="utf-8"><title>统一身份认证</title></head>
<body style="font-family:sans-serif;max-width:420px;margin:80px auto">
  <h2>统一身份认证</h2>
  <p>请重新登录以继续（演练页面）</p>
  <form method="POST">
    <p><input name="username" placeholder="工号 / 邮箱" style="width:100%;padding:8px"></p>
    <p><input name="password" type="password" placeholder="口令" style="width:100%;padding:8px"></p>
    <p><button type="submit" style="width:100%;padding:10px">登 录</button></p>
  </form>
</body></html>
```

**解读**：**自己写页面有三个好处**：① 不涉及他人版权/外观抄袭；② 可在页面上**明确标注"演练页面"**（强烈推荐，符合伦理且仍能测出行为）；③ 可控、可复现。

**Step 5：建 Email Template（含唯一追踪链接）**

```
Email Templates → New Template
  Name:    drill-template
  Subject: [安全演练] 请核对你的设备登录信息
  HTML:
    <p>你好 {{.FirstName}}，</p>
    <p>我们检测到你的账号在新设备上登录，请点击下方链接确认：</p>
    <p><a href="{{.URL}}">核对登录信息</a></p>
    <p>—— IT 服务台</p>
  Text: （纯文本版本，可留空）
  → Save Template
```

**解读**：`{{.URL}}` 是**必需的唯一追踪链接**（Gophish 会为每个目标生成不同 rid）。没有它，点击统计就没有数据。

**Step 6：导入目标名单并建演练**

CSV（**只放你自己/知情参与者的邮箱**）：

```csv
First Name,Last Name,Email,Position
Test,User,test1@drill.example.com,IT
Test,User,test2@drill.example.com,财务
```

```
Users & Groups → New Group → 名称 drill-group → Bulk Import Users → 粘贴 CSV → Save
```

```
Campaigns → New Campaign
  Name:           2026-Q1-安全意识演练
  Email Template: drill-template
  Landing Page:   drill-login
  URL:            http://192.168.56.5          ← 目标可达的 Gophish 钓鱼服务器地址
  Launch Date:    现在
  Send Emails By: 10 分钟后
  Sending Profile: lab-smtp
  Groups:         drill-group
  → Launch
```

**Step 7：观察实时事件**

```
Campaigns → 点进刚建的演练 → 看结果表格
```

```console
Email         Email Opened   Clicked Link   Submitted Data   Reported
test1@...     ✔ 12:00:31     ✔ 12:00:45     ✔ 12:01:02       —
test2@...     ✔ 12:03:10     —              —                —
```

**解读**：**这就是 Gophish 相对于 SET 的核心价值——事件级可度量**。你可以立刻算出：

- **打开率** = Opened / Sent
- **点击率** = Clicked / Sent
- **提交率** = Submitted / Sent（**最需要关注的指标**）
- **上报率** = Reported / Sent（**最能反映安全意识成熟度**）

```bash
# 用 API 拉结果（便于自动化出周报）
API_KEY='<从 Account Settings 复制>'
curl -sk -H "Authorization: $API_KEY" \
  https://127.0.0.1:3333/api/campaigns/1/results | python3 -m json.tool | head -40
```

### 场景 2：企业演练的正确姿势（流程比工具重要）

**一次合规演练的标准流程（**建议固化成清单**）**：

| 阶段 | 动作 | 产出 |
|------|------|------|
| **1. 授权** | 取得管理层批准；确认制度依据（员工手册/信息安全政策含演练条款）；明确演练范围与时间窗 | **书面批准记录** |
| **2. 设计** | 选主题（**避免恐慌性主题**）、选择目标群体、决定是否记录口令（**建议不记录**） | 演练方案 |
| **3. 准备** | 配 SMTP（SPF/DKIM/DMARC）、准备 Landing Page（**页面上标注演练**）、准备名单 | 演练配置 |
| **4. 预演** | 发给项目组 3–5 人，验证链路与统计 | 预演报告 |
| **5. 执行** | 按时间线发送；**实时监控**（若发现有人真的输入了凭据，要能立刻处置） | 事件数据 |
| **6. 澄清** | **演练结束后立即**向所有参与者发澄清邮件（说明这是演练、不要复用该口令、如何上报） | 澄清邮件 |
| **7. 复盘** | 统计指标；**对上报者表扬**；对点击者做**教育而非惩罚** | 演练报告 |
| **8. 清理** | 删除页面、名单、日志、数据库；销毁任何记录的凭据 | 清理记录 |

**演练报告的核心指标（写进报告）**：

| 指标 | 计算 | 建议目标 |
|------|------|----------|
| 打开率 | Opened / Sent | **不追求"越低越好"**（邮件网关过滤会显著降低它，说明防护有效） |
| **点击率** | Clicked / Sent | 越低越好；行业基线常在 5%–20% |
| **提交率** | Submitted / Sent | **最关键**：>2% 就应推动 MFA |
| **上报率** | Reported / Sent | **越高越好**（成熟组织 >30%） |
| 首报时间 | 第一个上报的时间差 | 越快说明"人在检测"有效 |

**解读**：**"上报率"是比"点击率"更有价值的指标**。一个点击率高但上报率也高的组织，其实际风险往往低于"点击率低但没人上报"的组织。

### 场景 3：与 SET、防御措施配合，验证防护链

**3a. 用 Gophish 验证邮件网关与 MFA**

```
① 演练 A（无 MFA 场景）：Gophish 的 Landing Page → 提交即"成功"
② 演练 B（有 MFA 场景）：Design 一个"要求输入验证码"的页面
     → 若员工仍会输入：说明 MFA 也挡不住社工（改推 FIDO2/Passkey）
     → 若员工在此停手：说明 MFA 起到了心理防线作用
```

**解读**：**MFA 的价值不只是技术阻断，还有心理上的"到此为止"效应**。

**3b. 用 SET 做手法研究，用 Gophish 做度量**

```bash
# SET：快速验证"克隆+收凭据"的手法可行性（在自建靶站上）
sudo setoolkit
#   1 → 2 → 3 → 2（Credential Harvester + Site Cloner）

# Gophish：把同样的手法做成可度量的演练
#   在 Landing Pages 里用 "Import Site" 抓自建靶站，或直接用上文的 HTML
```

**3c. 与 `dnstwist` 联动，评估仿冒域名风险**

```bash
# 生成你公司域名的仿冒变体（用于「品牌保护自检」）
dnstwist --registered example.com | head -20
```

```console
Domain                    DNS-A    Registrar          ...
examp1e.com               1.2.3.4  Example Registrar  ...
exarnple.com              -        ...
```

**解读**：`dnstwist` 的输出可以直接用于**：① 购买/监控关键仿冒域名；② 在 Gophish 演练中使用"像真的"域名**（**必须是你自己注册的演练域**，不能使用他人域名）。

**3d. 报告留档**

```bash
# 导出演练结果（CSV/JSON）交给 Dradis / Cherrytree 做报告
curl -sk -H "Authorization: $API_KEY" \
  https://127.0.0.1:3333/api/campaigns/1/results > /evidence/drill-results.json

# 用 dradis 汇总多个来源的结果
sudo dradis-start        # http://127.0.0.1:3000
```

见 [`dradis.md`](dradis.md)、[`cherrytree.md`](cherrytree.md)。

---

## 6. 输出解读

### 6.1 仪表盘（Dashboard）

| 指标 | 含义 | 注意 |
|------|------|------|
| `Campaigns` | 演练总数与状态（`In Progress`/`Completed`/`Queued`） | 完成后可导出报表 |
| `Emails Sent` | 已投递 | 失败会单独显示（SMTP 拒绝/退信） |
| `Emails Opened` | 追踪像素被加载 | **可能误报**（企业邮件代理预取图片会"假打开"） |
| `Clicked Link` | 唯一链接被访问 | 最可靠的行为指标之一 |
| `Submitted Data` | 表单被提交 | **最严重** |
| `Email Reported` | 员工上报 | **最希望看到**（需配置上报方式：邮件/按钮/插件） |
| `Errors` | 发送失败 | 通常是 SMTP 认证/SPF/限流 |

### 6.2 单次演练的结果表

| 列 | 含义 | 用途 |
|----|------|------|
| `Email` | 目标地址 | 定位到人（**报告里建议脱敏成部门/数量统计**） |
| `Status` | `Sending`/`Sent`/`Error` | 排查投递问题 |
| `Opened` / `Clicked` / `Submitted` / `Reported` | 各事件时间戳 | 计算指标；也能看出"谁最先点"（用于针对性培训） |
| `Details`（点击 Submitted 可看） | **提交的字段** | **只在获得明确授权且合规允许时才看**；报告必须脱敏 |

### 6.3 关键判断

| 现象 | 说明 | 建议动作 |
|------|------|----------|
| 打开率高但点击率低 | 邮件主题吸引人，但员工对链接警惕 | 说明培训有效，继续保持 |
| **点击率高 + 提交率高** | **凭据可被钓走** | **推动 MFA + 条件访问**（最高优先级） |
| 上报率低（<5%） | 没有上报渠道或不敢报 | 建一键上报；**公开表扬上报者** |
| 大量 `Error` | SPF/DKIM/SMTP 配置问题 | 先修发件基础设施 |
| Opened 数远大于实际人数 | 邮件代理预取图片误报 | 以 `Clicked` 为主指标 |

---

## 7. 与其他工具配合

```
① 演练设计
   dnstwist（仿冒域名研究，Kali 清单中）→ 挑选"像真的"演练域（自己注册）
   OSINT（组织架构、员工邮箱格式）→ 名单构造（**仅限授权名单**）
        │
② 平台
   ├─ gophish：可度量、可报表、有 API          ← 本文
   └─ set：社工手法验证（Web/邮件/介质/短信）    ← set.md
        │
③ 载荷（如需测试"点击后"的防护）
   msfvenom / powershell-empire / sliver         ← ../06-漏洞利用/msfvenom.md、../08-后渗透/powershell-empire.md、../12-基础设施与C2/sliver.md
        │
④ 结果汇总与报告
   cherrytree（个人笔记/报告草稿） / dradis（协作报告）  ← cherrytree.md、dradis.md
        │
⑤ 防护验证（蓝队视角）
   邮件网关（SPF/DKIM/DMARC）、URL 重写、附件沙箱、MFA/条件访问、浏览器反钓鱼
```

- 社工手法工具箱：[`set.md`](set.md) ｜ 报告工具：[`cherrytree.md`](cherrytree.md)、[`dradis.md`](dradis.md)
- 载荷与 C2：[`../06-漏洞利用/msfvenom.md`](../06-漏洞利用/msfvenom.md)、[`../12-基础设施与C2/sliver.md`](../12-基础设施与C2/sliver.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 打不开 `https://127.0.0.1:3333` | 自签证书/服务未起 | 浏览器点"继续访问"；`sudo gophish-start`；`ss -lntp \| grep 3333` |
| 远程访问不了管理界面 | 默认只监听 `127.0.0.1` | 改 `config.json` 的 `admin_server.listen_url` 为内网地址（**不要暴露公网**） |
| 忘了管理密码 | Kali 默认 `admin/kali-gophish`（上游是 `admin/gophish`） | 用默认口令；或删 `gophish.db` 重新初始化（**会丢数据**） |
| `Send Test Email` 失败 | SMTP 地址/端口/认证/证书 | 先用 `swaks`/`openssl s_client` 单独验证 SMTP；检查 `Ignore Certificate Errors` |
| 邮件全部进垃圾箱 | **SPF/DKIM/DMARC 没配** | 配好三者并把 DMARC 设到 `p=quarantine/reject`；用自有演练域 |
| 目标点不开链接 | `URL` 填的是 `127.0.0.1` 或不可达地址 | 填 `phish_server.listen_url` 对应、且目标能访问的地址 |
| 统计全是"Opened"但没人看 | 邮件代理预取图片（**假打开**） | 以 `Clicked` 为主指标；或去掉追踪像素 |
| 端口 80 被占用 | Apache/nginx 在跑 | `sudo ss -lntp \| grep :80`；改 `phish_server.listen_url` 端口 |
| 目标浏览器报证书警告 | 钓鱼服务器用了自签证书 | **用真实证书**（Let's Encrypt），否则演练效果与真实性都受影响 |
| Campaign 卡在 `Queued` | `Send Emails By` 太远/SMTP 限流 | 调整发送窗口；降低速率；检查 SMTP 限额 |
| 想给名单分组发送 | 未建多个 Group | 建多个 Group + 多个 Campaign（或调整发送窗口） |
| API 返回 401 | 未带头/Key 错 | `-H "Authorization: <API_KEY>"`（从 Account Settings 复制） |
| 数据丢/要迁移 | SQLite 在本地 | 备份 `gophish.db` 与 `config.json`；生产化可换数据库（按官方文档） |
| 演练后被投诉 | 未事先告知/未澄清 | **必须**在制度中明确并演练后立即澄清（这是流程问题，不是技术问题） |

---

## 9. 防御视角（蓝队）

Gophish 在蓝队手里是**主动验证防御有效性的工具**——它的价值恰恰在于**让防御变得可度量**。

| 演练能验证的防御 | 观察指标 | 若"没挡住"该怎么办 |
|------------------|----------|---------------------|
| **邮件网关过滤** | 发送成功率/退信率/是否被判垃圾邮件 | 完善 SPF/DKIM/DMARC；调整网关策略；URL 重写 |
| **附件沙箱** | 带附件模板的投递情况 | 附件类型白名单、沙箱策略 |
| **URL 重写与点击时检测** | 点击率是否显著下降 | 收紧 URL 重写策略 |
| **MFA / 条件访问** | **提交率**（提交后能否真的登录） | **推动 MFA 与条件访问（最高 ROI）** |
| **浏览器反钓鱼** | 访问 Landing Page 时是否有警告 | 确保客户端保护开启并更新 |
| **员工意识** | **上报率**与首报时间 | 建立上报渠道；培训；**表扬上报者** |
| **EDR（针对"点击后"）** | 后续载荷是否被拦 | EDR 策略、ASR 规则、WDAC/AppLocker |

**蓝队落地清单**：

1. **建立"演练—度量—改进"闭环**：每季度一次，跟踪**点击率与上报率趋势**（趋势比单次数值重要）；
2. **强制 MFA + 条件访问**：即使凭据被钓走也不能直接用——**这是整套防护中最关键的一环**；
3. **DMARC `p=reject` + SPF + DKIM 全配**：从源头减少伪造发件人的成功率；
4. **一键上报 + 正向激励**：**奖励上报者**（咖啡券、公开表扬）；对点击者做"事后教育"，**不要惩罚**（惩罚会导致瞒报）；
5. **把演练结果写进管理层报告**：用「点击率/提交率/上报率」三个数字说话，比任何技术术语都有说服力；
6. **合规底线**：只演练已批准名单；**建议关闭 `Capture Passwords`**；演练后立即清理数据。

---

## 10. 参考

- Gophish 官方文档（含 API、配置、模板变量）：<https://getgophish.com/documentation/>
- Gophish 仓库：<https://github.com/gophish/gophish>
- Kali 工具页：<https://www.kali.org/tools/gophish/>
- 本地资源：`sudo gophish-start`（会打印 Web UI 与默认口令）、`config.json`
- 配套教程：[`set.md`](set.md)、[`cherrytree.md`](cherrytree.md)、[`dradis.md`](dradis.md)
- 参考标准：NIST SP 800-50《Building an Information Technology Security Awareness and Training Program》、NIST SP 800-115（社会工程测试的授权要求）

## ⚠️ 法律与伦理（**本节请完整阅读**）

Gophish 是**为合规演练设计的工具**，但**一旦用于未授权对象，就是犯罪工具**。

**可能触犯的法律**：

- 《刑法》**第 285 条**：非法侵入计算机信息系统罪、非法获取计算机信息系统数据罪、非法控制计算机信息系统罪；
- 《刑法》**第 253 条之一**：**侵犯公民个人信息罪**（收集的账号口令、员工邮箱与行为数据均属个人信息）；
- 《刑法》**第 252 条**：侵犯通信自由罪（**拦截/阅读他人邮件内容**）；
- 《网络安全法》第 27 条、《数据安全法》、《个人信息保护法》（未经同意处理个人信息；**未告知的钓鱼演练在很多法域下本身就是违法处理个人信息**）。

**强制要求（缺一不可）**：

1. **管理层书面批准 + 制度依据**：员工手册或信息安全政策中必须明确"组织可能开展安全意识演练"（否则连"自己公司员工"都不能随便钓）；
2. **演练范围与时间窗书面确定**，并获得相应授权；
3. **只针对已批准的演练名单**，绝不扩大范围（**"顺手测一下同事"是违规的**）；
4. **建议关闭 `Capture Passwords`**：只统计"是否提交"，**不保存真实口令**（很多组织的合规要求就是这样）；
5. **演练结束立即澄清并清理**：发澄清邮件、删除页面与数据库中的凭据记录、销毁导出文件；
6. **报告严格脱敏**：只给统计数字与部门维度，**不要逐人点名**（点名会造成劳动纠纷与信任破裂）；
7. **绝不在演练中投递真实恶意载荷**（那会让"演练"变成"真实攻击"）；
8. **不确定是否有授权，就不要执行。**

**最后一句**：钓鱼演练的目的是**保护员工**，不是**抓住员工**。任何让员工感到被羞辱或被监视的做法，都会破坏安全文化，最终降低组织的真实安全水平。
