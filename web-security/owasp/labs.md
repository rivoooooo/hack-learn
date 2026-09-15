# 靶场练习指南

> 本文件中的所有命令**仅用于本地或自有环境中的合法靶场**。禁止对未授权系统使用其中的任何技术。
>
> 相关文件：[模块总纲](README.md)｜[Top 10 总览](top10/README.md)｜[WSTG 方法论](wstg/README.md)｜[测试清单](wstg/checklist.md)

## 一、为什么要用靶场

OWASP 官方把"故意存在漏洞的应用"定位为**安全环境**：在不触发真实 IDS（入侵检测系统）、不伤害任何真实系统的前提下练习攻击工具与测试方法论。OWASP 通过 [Vulnerable Web Applications Directory Project](https://owasp.org/www-project-vulnerable-web-applications-directory/)（VWAD，易受攻击 Web 应用目录）汇总了离线、容器化、在线与移动端的各类靶场。

**练习靶场与真实测试的区别：**

| 维度 | 靶场 | 真实（授权）目标 |
| --- | --- | --- |
| 目的 | 练工具、练手法、建立肌肉记忆 | 发现真实风险 |
| 提示 | 有提示/分数/教程 | 无提示 |
| 业务逻辑 | 简化、可预期 | 复杂、有历史包袱 |
| 噪音 | 少 | 多（误报、环境干扰） |
| 报告 | 不用写 | 必须写清复现步骤与影响 |

因此：**靶场练"怎么做"，真实测试练"如何判断值不值得做、如何证明影响"**。

## 二、环境准备

先确认 Docker 可用：

```bash
docker --version
docker run --rm hello-world
```

统一约定：所有靶场只监听 `127.0.0.1`，避免暴露到局域网。练习完成后及时停止并清理容器。

```bash
docker ps                 # 查看运行中的容器
docker stop <容器名>
docker rm <容器名>
```

---

## 三、OWASP Juice Shop

**定位**：OWASP 官方维护的现代化、复杂的不安全 Web 应用，**覆盖 OWASP Top 10 全部类别**。前端为 SPA（单页应用），适合练习 API 测试、客户端测试与现代前端架构下的漏洞。是进阶首选。

**版本参考**：官方文档写作时示例版本为 v20.2.0；`latest` 镜像构建自 `master` 分支，内部使用 Node.js 24.x。

### 安装（Docker）

```bash
docker pull bkimminich/juice-shop
docker run -d -p 127.0.0.1:3000:3000 bkimminich/juice-shop
```

访问 <http://localhost:3000>。

若在 Windows 的 VirtualBox 虚拟机内使用 Docker，还需把宿主机的 `127.0.0.1:3000` 转发到虚拟机的 `0.0.0.0:3000`（TCP）。

**系统要求（官方）**：

- 最低：256 MB RAM、200 millicpu CPU、300 MB 可用磁盘空间
- 推荐：384 MB RAM、400 millicpu CPU、800 MB 可用磁盘空间

**指定版本 / 预览版**：

```bash
docker pull bkimminich/juice-shop:v20.2.0     # 指定发布版本
docker pull bkimminich/juice-shop:snapshot    # develop 分支预览版
```

**可选依赖**：

- AI Chat 功能需要外部 LLM 提供方（默认连接本地 Ollama `http://localhost:11434/v1`），不是必需。
- 两个 Web3 挑战需要 Alchemy 以太坊测试网 API Key，不是必需。

### 覆盖的漏洞类别

覆盖 Top 10 全部类别，尤其擅长：

- A01 访问控制：IDOR、越权、JWT 篡改（覆盖最集中）
- A02 配置错误：泄露的管理端点、错误信息
- A04 加密失效：弱口令哈希、明文凭据
- A05 注入：SQL 注入、NoSQL 注入、XSS（反射/存储/DOM）
- A06 不安全设计：支付与购物车逻辑、竞态
- A07 认证失效：认证绕过、口令重置逻辑
- A08 完整性失效：不安全反序列化
- A09 日志与告警：需要结合做题时的请求异常分析
- A10 异常处理：错误路径触发

### 推荐练习顺序

1. 先做**信息搜集类**挑战（找隐藏路径、找备份文件），练习 `WSTG-INFO` 与 `WSTG-CONF-04`。
2. 再做**认证与访问控制**（用/不用管理账号各走一遍），练习 `WSTG-ATHN`、`WSTG-ATHZ-04`。
3. 然后做**注入类**（先反射 XSS，再存储 XSS，最后 SQL/NoSQL 注入），练习 `WSTG-INPV-01/02/05`。
4. 接着做**业务逻辑与加密**。
5. 最后挑战**反序列化、SSRF、原型链污染**等高级项，练习 `WSTG-INPV-19/22/23`。

> 官方配套教学书《Pwning OWASP Juice Shop》提供逐题提示与解法，卡住时再查，不要一开始就看。

---

## 四、OWASP WebGoat

**定位**：OWASP 官方维护的**教学型**故意不安全应用，基于 Java。它以"课程"形式组织，每题有讲解与提示，最适合**入门**。容器内自带 WebWolf（攻击者客户端），使攻击流量完全留在容器内。

### 安装（Docker）

```bash
docker pull webgoat/webgoat
docker run --name webgoat -it -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 webgoat/webgoat
```

- 访问 WebGoat：<http://localhost:8080/WebGoat>（**注意 `localhost:8080/` 根路径不提供页面**）
- 访问 WebWolf：<http://localhost:9090/WebWolf>（同样根路径无页面）

首次访问会要求登录，需要先在登录页**创建测试账号**。账号在容器停止后仍保留，但删除容器后消失。允许创建不安全的用户名/口令组合（如 `kalikali` / `Kali1234`），因为这是教学环境。

> 官方提示：将端口映射到 `localhost:8080` 更稳妥，某些企业笔记本会拦截映射到 80 端口。

**桌面版（含预装攻击工具的 Linux 桌面）**：

```bash
docker run -p 127.0.0.1:3000:3000 webgoat/webgoat-desktop
```

访问 <http://localhost:3000/>。

### 覆盖的漏洞类别

课程式覆盖，包含但不限于：

- 访问控制（如 "Hijack a session" 会话劫持）
- 认证缺陷（JWT、口令重置、认证绕过）
- 注入（SQL 注入进阶、XXE、命令注入）
- 客户端（XSS、CSRF）
- 密码学（不安全的加密、哈希）
- 请求伪造（SSRF）
- 反序列化
- 日志伪造

### WebWolf 提供的工具

WebWolf 是配套的攻击者服务端，提供：文件上传区、邮件测试邮箱、JWT 工具、HTTP 请求展示。当题目需要"接收带外请求""接收邮件""伪造 JWT"时使用它。

### 推荐练习顺序

1. **Introduction** 与 **General** 分类，熟悉界面与提示机制。
2. **Authentication Flaws**（JWT、口令重置、认证绕过）——对应 A07。
3. **Access Control Flaws**（含会话劫持）——对应 A01、SESS。
4. **Injection Flaws**（SQL 注入、XXE、命令注入）——对应 A05。
5. **Cross-Site Scripting / CSRF**——对应 INPV、SESS-05。
6. **Request Forgeries（SSRF）** 与 **Insecure Deserialization**——对应 A05/A08 高级项。
7. **Cryptography** 与 **Logging**——对应 A04、A09。

---

## 五、DVWA（Damn Vulnerable Web Application）

**定位**：经典 PHP/MySQL 靶场，**界面简单、难度可调**（Low / Medium / High / Impossible 四档）。最大的价值是**同一漏洞在四个难度下的代码对比**，让你直观理解"防护如何被绕过""什么才是真正的修复"。适合理解漏洞**原理**。

### 安装（Docker）

```bash
docker pull vulnerables/web-dvwa
docker run -d -p 127.0.0.1:8080:80 vulnerables/web-dvwa
```

访问 <http://localhost:8080>。

首次使用：

1. 默认账号 `admin` / 口令 `password` 登录。
2. 进入后点击 **Create / Reset Database** 初始化数据库。
3. 在 **DVWA Security** 页面把难度设为 `Low` 开始练习。

> 若 8080 端口被占用，可改为 `-p 127.0.0.1:8888:80` 等其它端口。

### 覆盖的漏洞类别

- Brute Force（暴力破解）——A07
- Command Injection（命令注入）——A05
- CSRF——SESS-05
- File Inclusion（文件包含）——A05
- File Upload（文件上传）——A06
- SQL Injection（普通与盲注）——A05
- Weak Session IDs（弱会话 ID）——A04/A07
- XSS（反射型、存储型、DOM 型）——A05
- CSP Bypass（内容安全策略绕过）——A02
- JavaScript Attacks（客户端攻击）——CLNT
- Open HTTP Redirect（开放重定向）——A01
- Insecure CAPTCHA（不安全验证码）——A06

### 推荐练习顺序

1. **SQL Injection**：先用 Low 体验 `' OR '1'='1`，再切 High 观察过滤逻辑与绕过方式。
2. **Command Injection**：用 `127.0.0.1; id` 验证，再对比 High 的过滤。
3. **XSS 三种类型**：理解反射/存储/DOM 的差别。
4. **File Inclusion / File Upload**：理解路径穿越与上传利用。
5. **CSRF**：理解为什么需要 token。
6. **Brute Force / Weak Session IDs**：理解认证与会话强度。
7. 最后用 **Impossible** 档的源码通读一遍——这是 Learn 到"正确修复"的关键。

---

## 六、bWAPP（buggy Web Application）

**定位**：覆盖漏洞种类最多的开源 PHP 靶场之一（超过 100 种），包含大量较偏门与 OWASP Top 10 覆盖不到的项目。适合在掌握基础后**拓宽覆盖面**。可按漏洞清单筛选练习。

### 安装（Docker，社区镜像）

```bash
docker pull raesene/bwapp
docker run -d -p 127.0.0.1:8080:80 raesene/bwapp
```

访问安装页并初始化数据库：

```
http://localhost:8080/install.php      # 点击安装/初始化数据库
http://localhost:8080/bWAPP/login.php  # 安装完成后进入
```

默认账号：`bee` / 口令 `bug`。

> 该镜像是社区维护的（基于 `raesene/bWAPP` 与 `mattrayner/lamp`），不同标签行为可能略有差异。若端口或路径不符，先访问根路径确认实际入口。

### 覆盖的漏洞类别

数量众多，典型包括：SQL 注入（含各种数据库与盲注）、XSS（反射/存储/DOM）、OS 命令注入、PHP 代码注入、文件包含与目录穿越、任意文件上传、XML/XPath/XXE、LDAP 注入、SSRF、CSRF、会话固定、点击劫持、不安全的直接对象引用、心跳类逻辑缺陷、Cookie 与加密缺陷等。

### 推荐练习顺序

1. 先用顶部的**漏洞筛选**功能，把范围收窄到与 [WSTG 清单](wstg/checklist.md) 对应的项。
2. 按 WSTG 分类顺序推进：注入类 → 认证/会话类 → 访问控制类 → 客户端类。
3. 每完成一类，回到 [checklist.md](wstg/checklist.md) 勾选对应条目，形成"测试 → 记录"的闭环。
4. 与 DVWA 对照：同一个漏洞（如 SQL 注入）在两个靶场里的实现与防御差异，有助于理解"漏洞不是模板，取决于上下文"。

---

## 七、靶场与 WSTG / Top 10 的对应练习表

| 练习目标 | 推荐靶场 | 对应 WSTG 分类 | 对应 Top 10 |
| --- | --- | --- | --- |
| 信息搜集、入口点枚举 | Juice Shop、bWAPP | INFO、CONF-04/05 | A02 |
| 安全配置与响应头 | Juice Shop、DVWA(CSP Bypass) | CONF-06/07/12/14 | A02 |
| 认证缺陷与爆破 | WebGoat、DVWA、Juice Shop | ATHN、IDNT-04 | A07 |
| 会话与 CSRF | WebGoat、DVWA、bWAPP | SESS-02/03/05/10 | A07、A01 |
| 授权与 IDOR | Juice Shop（最集中）、bWAPP | ATHZ-04、APIT-02/04 | A01 |
| SQL / NoSQL 注入 | DVWA、bWAPP、Juice Shop | INPV-05.* | A05 |
| XSS（三类） | DVWA、bWAPP、Juice Shop | INPV-01/02、CLNT-01 | A05 |
| 命令注入 / 文件包含 / 上传 | DVWA、bWAPP | INPV-11/12、BUSL-08/09 | A05、A06 |
| SSRF | WebGoat、Juice Shop | INPV-19 | A01 |
| 不安全反序列化 | WebGoat、Juice Shop | INPV-23 | A08 |
| 原型链污染 | Juice Shop | INPV-22 | A05 |
| 业务逻辑 / 支付 / 竞态 | Juice Shop | BUSL-05/06/10 | A06 |
| 客户端（DOM XSS、CORS、点击劫持） | Juice Shop、bWAPP | CLNT-01/07/09 | A05、A02 |
| API 与 GraphQL | Juice Shop | APIT-01..04、99 | A01、A05 |
| 错误处理与日志 | WebGoat、DVWA | ERRH-01/02、A09 | A10、A09 |

## 八、练习心法

1. **先记录再动手。** 每道题先写清"我想验证什么假设"，再发请求。这与真实测试一致。
2. **用代理工具。** 全程用 Burp Suite Community 或 OWASP ZAP 拦截，避免"看页面猜结果"。
3. **对照 WSTG 编号。** 每完成一个练习，回到 [checklist.md](wstg/checklist.md) 勾选对应条目，把"做过"变成"覆盖过"。
4. **难度对比法。** 在 DVWA 中故意在 Low / Medium / High 之间来回切换，反复问："这一版为什么能挡住/挡不住？"
5. **读源码。** 尤其是 Impossible 档与 Juice Shop 的挑战源码，理解"修复"是在哪一行生效的。
6. **不要只收集答案。** 记住 payload 没有价值，理解**为什么这个 payload 在这个上下文有效**才有价值。
7. **收尾清理。** 练习结束停止并删除容器，保持本机干净：
   ```bash
   docker stop $(docker ps -q --filter ancestor=bkimminich/juice-shop)
   docker rm webgoat
   ```

## 来源

- <https://owasp.org/www-project-vulnerable-web-applications-directory/>
- <https://devguide.owasp.org/en/07-training-education/01-vulnerable-apps/>
- <https://devguide.owasp.org/en/07-training-education/01-vulnerable-apps/02-webgoat/>
- <https://pwning.owasp-juice.shop/companion-guide/latest/part1/running.html>
- <https://owasp.org/www-project-webgoat/>
- <https://owasp.org/www-project-juice-shop/>
