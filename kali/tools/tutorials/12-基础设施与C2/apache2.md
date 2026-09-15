# Apache HTTP Server（重定向器与 Payload 托管）

> **一句话**：不只是一个"网站服务器"——在红队基础设施里，它承担两个关键角色：**载荷/内容托管**（让目标稳定下载）与 **C2 重定向器**（把 C2 藏在正常的 Web 流量后面，按条件分流）。
> **分类**：基础设施与 C2 / 重定向器 ｜ **Kali 包**：`apache2`（命令 `apache2`、`apache2ctl`、`a2enmod`、`a2ensite`、`htpasswd`、`ab` 等）｜ **官方文档**：<https://httpd.apache.org/docs/2.4/> ｜ `man apache2`

---

## 1. 它解决什么问题

初学 C2 时最容易犯的错是：**把 C2 服务端直接暴露出来**。后果有两个：

1. **暴露即被测**：蓝队/威胁情报做一次端口扫描或指纹识别，就能确定"这是 Sliver/CS/Metasploit"，并直接封锁甚至反制；
2. **访问不受控**：任何人扫描到你的端口都能连上来（包括防御方主动探测）。

正确的做法是**在前面放一层"看起来正常"的 Web 服务器**，它负责：

| 角色 | Apache 提供的能力 |
|------|-------------------|
| **重定向器（Redirector）** | 按 **User-Agent / 路径 / Host / Header** 条件转发；不匹配就返回一个正常网站 |
| **多后端分流** | 同一入口按域名/路径转发到**不同 C2 会话** |
| **Payload 托管** | 稳定的 HTTP(S) 下载点；控制 MIME/文件名/响应头 |
| **TLS 终结** | 用**可信证书**（Let's Encrypt）避免告警 |
| **访问控制** | `Require ip`/基本认证/限速，把来源限制在授权范围 |
| **日志与审计** | 记录全部请求（含 UA/Referer），是**授权演练的证据来源** |
| **内容伪装** | 替换 Server 头、定制错误页、返回真实站点内容 |

对比同类：

| 工具 | 定位 | 差异 |
|------|------|------|
| **Apache** | 应用层重定向器 | 功能全（mod_rewrite/proxy/headers）；配置略重 |
| **Nginx** | 同类 | 性能更好、配置更简洁；**不在本仓库抓取的 Kali 工具清单中**（清单里只有 `apache2`），故本文用 Apache |
| **`socat`** | 传输层转发 | 一条命令搞定，但**做不了按 UA/路径分流**；见 [`socat.md`](socat.md) |
| **`chisel`** | HTTP 隧道 | 用于穿透，不是重定向器；见 [`../08-后渗透/chisel.md`](../08-后渗透/chisel.md) |
| **CDN / 云函数** | 商业重定向 | 更隐蔽（共享 IP、真实证书），但需要账号与费用 |

**一句话**：**socat 是"把线接上"，Apache 是"把线接到哪里要看你像不像自己人"。**

---

## 2. 工作原理

```
                     ┌────────── Apache（对外 80/443）──────────┐
目标/客户端 ──TLS──► │  ① TLS 终结（mod_ssl，可信证书）          │
                     │  ② 条件判断（mod_rewrite / mod_proxy）     │
                     │       ├─ 匹配 C2 特征（UA/路径/Header）    │
                     │       │     └─► 反代到后端 C2（127.0.0.1:8443）│
                     │       └─ 不匹配                            │
                     │             └─► 返回一个正常站点内容（伪装） │
                     │  ③ 日志（mod_log_config，含 UA/Referer）    │
                     │  ④ 访问控制（Require ip / 基本认证 / 限速）  │
                     └────────────────────────────────────────────┘

另一条线（Payload 托管）：
   /var/www/html/payload/  ←  文件放在这里，目标用 HTTP(S) 下载
        └─ 可控制 MIME、文件名、目录列表、响应头
```

### 关键机制（Debian/Kali 的目录结构）

| 路径 | 作用 |
|------|------|
| `/etc/apache2/apache2.conf` | 主配置 |
| `/etc/apache2/ports.conf` | **监听端口**（80/443 在这里改） |
| `/etc/apache2/sites-available/` | 站点配置（**可用的**） |
| `/etc/apache2/sites-enabled/` | 站点配置（**生效的**，通常是符号链接） |
| `/etc/apache2/mods-available/` | 可用模块 |
| `/etc/apache2/mods-enabled/` | 已启用模块（`a2enmod` 就是在这里建链接） |
| `/etc/apache2/conf-available/` | 可用全局片段（`a2enconf` 启用） |
| `/var/www/html/` | **默认站点根目录**（Payload 托管常放这里） |
| `/var/log/apache2/access.log`、`error.log` | 日志 |

**红队最常用的四个模块**：

| 模块 | 作用 | 启用 |
|------|------|------|
| **`mod_rewrite`** | **按条件重写/分流** | `sudo a2enmod rewrite` |
| **`mod_proxy` + `mod_proxy_http`** | **反向代理到后端** | `sudo a2enmod proxy proxy_http` |
| **`mod_ssl`** | TLS/HTTPS | `sudo a2enmod ssl` |
| **`mod_headers`** | 修改/删除响应头（伪装） | `sudo a2enmod headers` |

**为什么"条件分流"是核心**：C2 植入体回连时会带上特定特征（User-Agent、URI、Cookie、Host）。Apache 据此判断「这是不是我的植入体」：

- **是** → 转发给后端 C2；
- **不是**（扫描器、防御方探测、普通用户）→ 返回一个**真实存在的正常网站**。

这样无论谁来看，前置 IP 站在明面上都只是个普通网站。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install apache2
sudo systemctl enable --now apache2
apache2 -v
```

```console
Server version: Apache/2.4.x (Debian)
Server built:   ...
```

```bash
# 验证默认站点
curl -s http://127.0.0.1/ | head -5
sudo ss -lntp | grep -E ':80|:443'
```

```console
LISTEN 0 511 *:80 *:* users:(("apache2",pid=...,fd=4))
```

常用管理命令（**Debian/Kali 特有，务必记住**）：

```bash
# 启用模块 / 站点 / 配置片段
sudo a2enmod rewrite proxy proxy_http ssl headers
sudo a2ensite my-redirector
sudo a2enconf security

# 停用
sudo a2dismod rewrite
sudo a2dissite 000-default

# 配置语法检查（改完配置必做！）
sudo apache2ctl configtest        # 或 sudo apache2 -t
sudo apache2ctl -S                # 列出所有虚拟主机与监听（排错神器）

# 重载/重启
sudo systemctl reload apache2     # 优雅重载（推荐）
sudo systemctl restart apache2    # 彻底重启
```

---

## 4. 核心参数详解

### 4.1 命令行工具与参数

| 命令/参数 | 作用 | 使用建议 |
|-----------|------|----------|
| `apache2 -v` | 版本 | 确认版本（不同版本指令有差异） |
| `apache2 -t` / `apache2ctl configtest` | **语法检查** | **每次改配置后必跑** |
| `apache2ctl -S` | 列出**虚拟主机与监听** | 排错第一命令（"为什么我的请求走错了 vhost"） |
| `apache2ctl -D DUMP_MODULES` | 列出**已加载模块** | 确认 mod_rewrite/proxy 是否真的启用 |
| `apache2 -V` | 编译参数（`-D` 与 MPM 信息） | 排错 |
| `apache2 -k start/stop/restart/graceful` | 控制进程 | 一般用 `systemctl` |
| `apache2 -X` | 调试模式（单进程、前台） | 调试启动问题 |
| `apache2 -f <file>` | 指定配置文件 | 多实例 |
| `apache2 -d <dir>` | 指定 ServerRoot | 多实例 |
| `apache2 -M` | 列出已加载模块（简写） | 与 DUMP_MODULES 等价 |
| `apache2 -l` | 列出编译进（静态）的模块 | —— |
| `apache2 -L` | 列出所有可用指令及说明 | **查 directive 语法最权威** |
| `apache2ctl graceful` | 优雅重启（不中断现有连接） | 生产化推荐 |
| `a2enmod` / `a2dismod` | 启用/停用模块 | —— |
| `a2ensite` / `a2dissite` | 启用/停用站点 | —— |
| `a2enconf` / `a2disconf` | 启用/停用配置片段 | —— |
| `a2query -m <mod>` | 查询模块是否启用 | 脚本化检查 |
| `htpasswd` | **生成基本认证口令文件** | 给管理路径加认证（`-c` 创建、`-n` 输出到 stdout、`-B` bcrypt） |
| `htdigest` | 生成摘要认证文件 | —— |
| `ab` | 简易压测（`ab -n 1000 -c 10 http://...`） | **仅对自己拥有的服务使用** |
| `rotatelogs` / `logresolve` / `split-logfile` | 日志处理 | 长周期运行时的日志管理 |
| `htcacheclean` | 清理 mod_cache 缓存 | —— |

### 4.2 核心配置指令（**重定向器真正要用的**）

| 指令 | 作用 | 关键点 |
|------|------|--------|
| `Listen <port>` | 监听端口（`ports.conf`） | 多端口/多 IP 在此声明 |
| `<VirtualHost *:80>` / `<VirtualHost *:443>` | **虚拟主机** | 分流的基本单位 |
| `ServerName` / `ServerAlias` | 域名匹配 | 多域分流 |
| `DocumentRoot` | 站点根目录 | Payload 托管位置 |
| **`LoadModule`** | 加载模块 | 由 `a2enmod` 自动管理 |
| **`RewriteEngine On`** | 启用重写 | mod_rewrite |
| **`RewriteCond <TestString> <CondPattern> [flags]`** | **重写条件**（如匹配 UA/Header/来源） | **分流的判断逻辑** |
| **`RewriteRule <Pattern> <Substitution> [flags]`** | 重写规则 | `[P]` = 交给 mod_proxy（反代）、`[R=302,L]` = 重定向、`[L]` = 停止后续规则 |
| **`ProxyPass <path> <url>`** | 反向代理 | `ProxyPass / http://127.0.0.1:8443/` |
| **`ProxyPassReverse <path> <url>`** | 修正后端返回的 Location/重定向 | 与 `ProxyPass` 配套 |
| `ProxyPreserveHost On` | 保留原始 Host 传给后端 | C2 常需要 |
| **`Header set/unset/always <Name> <Value>`** | 修改/删除响应头 | **伪装 Server 头**（mod_headers） |
| `ServerTokens Prod` | Server 头只显示 `Apache` | 减少信息泄露（伪装用） |
| `ServerSignature Off` | 错误页不显示版本 | 同上 |
| `ErrorDocument 404 /index.html` | 自定义错误页 | 让"不匹配的请求"看起来正常 |
| `Require ip <CIDR>` | **访问控制（来源限制）** | **授权测试必须限制来源** |
| `AuthType Basic` + `AuthUserFile` | 基本认证 | 保护管理路径 |
| `SSLEngine on` / `SSLCertificateFile` / `SSLCertificateKeyFile` | TLS | mod_ssl |
| `CustomLog <file> <format>` | **自定义日志格式**（含 UA/Referer） | **分析"谁连上来了"** |
| `LogLevel warn` | 日志级别 | 排错时调 `debug` |
| `Options -Indexes` | **禁止目录列表** | 安全基本项 |
| `AddType <mime> <ext>` | 强制 MIME 类型 | **伪装文件下载类型**（如让 `.exe` 以 `.txt` 类型返回） |
| `Options +FollowSymLinks` | 允许符号链接 | —— |
| `SetEnvIf` | 按条件设环境变量 | 配合限速/日志 |

---

## 5. 实战演练

> **环境声明**：以下全部在**完全隔离的自建实验室**中进行（自己的 Kali、自己的靶机、Host-Only 网络）。
> **Apache 本身是完全合法的服务器软件**。但**用它托管恶意载荷、或用它把流量转发到未授权目标的 C2，属于违法犯罪**（《刑法》第 285/286 条）。授权测试中必须：**限制 `Require ip` 到授权网段**、**在约定时间窗内运行**、**测试结束拆除重定向器**。

### 场景 1：Payload 托管（把"下载点"做稳做像）

**Step 1：准备目录与文件**

```bash
sudo mkdir -p /var/www/html/assets
# 授权演练中：放入你自己生成的、用于自有靶机的载荷
sudo cp /tmp/lab/lab-implant.exe /var/www/html/assets/logo_update.bin
sudo chown -R www-data:www-data /var/www/html/assets
```

**Step 2：一个"看起来正常"的托管配置**

```bash
sudo tee /etc/apache2/sites-available/assets.conf > /dev/null <<'EOF'
<VirtualHost *:80>
    ServerName cdn.drill.example.com
    DocumentRoot /var/www/html

    # 安全与伪装的基本项
    ServerTokens Prod
    ServerSignature Off
    Options -Indexes                      # 禁止目录列表

    <Directory /var/www/html/assets>
        Require all granted
        Options -Indexes -ExecCGI
        # 让 .bin 以通用二进制类型返回（避免奇怪的 Content-Type 引起怀疑）
        AddType application/octet-stream .bin
    </Directory>

    # 不匹配的请求返回一个正常首页（伪装）
    ErrorDocument 404 /index.html

    # 详细日志：记录 UA 与 Referer，便于分析"谁在访问"
    LogFormat "%h %l %u %t \"%r\" %>s %b \"%{User-Agent}i\" \"%{Referer}i\"" drill
    CustomLog ${APACHE_LOG_DIR}/assets_access.log drill
    ErrorLog  ${APACHE_LOG_DIR}/assets_error.log
</VirtualHost>
EOF
sudo a2ensite assets
sudo apache2ctl configtest && sudo systemctl reload apache2
```

```bash
# 验证
curl -s -o /dev/null -w 'status=%{http_code} type=%{content_type} size=%{size_download}\n' \
  http://127.0.0.1/assets/logo_update.bin
```

```console
status=200 type=application/octet-stream size=1258291
```

**解读（Payload 托管的关键点）**：

| 配置 | 作用 |
|------|------|
| `ServerTokens Prod` + `ServerSignature Off` | 不暴露 Apache 版本与 OS（减少指纹信息） |
| `Options -Indexes` | 攻击者/防御方看不到目录列表（**不暴露你放了哪些文件**） |
| `AddType application/octet-stream .bin` | 统一为普通二进制类型（**避免"这个文件类型很可疑"**） |
| `ErrorDocument 404 /index.html` | 404 也返回正常首页 → 扫描器看到的"像个人畜无害的站点" |
| `CustomLog ... User-Agent/Referer` | **记录访问者的 UA 与来源** → 你能看出**是谁在访问**（植入体？扫描器？防御方？） |

**Step 3：从日志看出"谁来过"（**这是重定向器的第二大价值**）**

```bash
sudo tail -20 /var/log/apache2/assets_access.log
```

```console
192.168.56.50 - - [02/Mar/2026:10:31:02 +0800] "GET /assets/logo_update.bin HTTP/1.1" 200 1258291 "Microsoft BITS/7.8" "-"
203.0.113.77  - - [02/Mar/2026:10:35:41 +0800] "GET / HTTP/1.1" 200 1234 "Mozilla/5.0 (compatible; Nmap Scripting Engine)" "http://cdn.drill.example.com/"
```

**解读**：第一行是目标（Windows BITS）下载载荷；第二行是**扫描器在探测你的域名**（UA 直接写着 `Nmap Scripting Engine`）。

| 观察 | 含义 | 动作（授权演练中） |
|------|------|--------------------|
| UA 是 `Microsoft BITS` 之类 | 目标在下载 | 正常 |
| UA 是扫描器/安全厂商/未知 | **有人在探测你** | 记录并上报；考虑降低暴露（换域名/换路径） |
| 大量来自同一 IP 的 404 | 有人在扫目录 | 记录；`Options -Indexes` 已阻止泄露 |
| Referer 指向你的域名 | 有人在浏览器里访问 | 正常（伪装页在起作用） |

### 场景 2：C2 重定向器（**本教程最重要的配置**）

**目标**：让对外只暴露一个"正常网站"，只有**带特定特征的请求**才被转发到后端 C2。

```
目标/Kali 植入体 ──► Apache:443（cdn.drill.example.com，可信证书）
                        ├─ UA/路径匹配 → 反代到 127.0.0.1:8443（Sliver 的 https 监听器）
                        └─ 其它 → 返回正常站点（/var/www/html/index.html）
```

**Step 1：先起后端 C2（内网本地，不对外）**

```console
# Sliver 侧（示例，见 sliver.md）：https 监听器 + 一个伪装网站
sliver > https --lport 8443 --domain cdn.drill.example.com
sliver > website add-content --website cdn.drill.example.com --file /var/www/html/index.html
```

**Step 2：启用模块并拿到可信证书**

```bash
sudo a2enmod rewrite proxy proxy_http ssl headers
sudo apache2ctl configtest && sudo systemctl reload apache2

# 证书：真实场景用 Let's Encrypt（certbot）
sudo apt install certbot python3-certbot-apache
sudo certbot --apache -d cdn.drill.example.com
# 演练环境若无公网域名，可用自签（但浏览器会告警 → 等于自我暴露）
```

**Step 3：写重定向器配置**

```bash
sudo tee /etc/apache2/sites-available/redirector.conf > /dev/null <<'EOF'
<VirtualHost *:80>
    ServerName cdn.drill.example.com
    # 全部重定向到 HTTPS（真实网站的做法）
    RewriteEngine On
    RewriteRule ^/?(.*) https://%{SERVER_NAME}/$1 [R=301,L]
</VirtualHost>

<VirtualHost *:443>
    ServerName cdn.drill.example.com

    SSLEngine on
    SSLCertificateFile    /etc/letsencrypt/live/cdn.drill.example.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/cdn.drill.example.com/privkey.pem

    DocumentRoot /var/www/html
    ServerTokens Prod
    ServerSignature Off
    Options -Indexes
    ErrorDocument 404 /index.html

    RewriteEngine On

    # ---- 条件：只有带特定特征的请求才转到后端 C2 ----
    # ① 匹配特定 User-Agent（植入体配置的 UA）
    RewriteCond %{HTTP_USER_AGENT} "^Mozilla/5\.0 \(Windows NT 10\.0; Win64; x64\).*Edge/1[2-9]" [NC]
    # ② 匹配特定 URI 前缀（植入体配置的回连路径）
    RewriteCond %{REQUEST_URI} "^/api/v2/telemetry"
    # ③ 来源限制（授权测试必须做：只允许授权网段）
    RewriteCond %{REMOTE_ADDR} "^192\.168\.56\."
    RewriteRule ^/(.*)$ http://127.0.0.1:8443/$1 [P,L]

    # ---- 其它请求：返回正常站点（伪装）----
    ProxyPassReverse / http://127.0.0.1:8443/

    # ---- 伪装响应头：删掉会暴露"我在代理"的头 ----
    Header unset X-Backend-Server
    Header always unset X-Powered-By
    Header always edit Set-Cookie ^(.*)$ $1;SameSite=Lax

    # ---- 日志：完整记录，便于分析 ----
    LogFormat "%h %t \"%r\" %>s %b UA=\"%{User-Agent}i\"" redir
    CustomLog ${APACHE_LOG_DIR}/redirector_access.log redir
    ErrorLog  ${APACHE_LOG_DIR}/redirector_error.log
</VirtualHost>
EOF
sudo a2ensite redirector && sudo a2dissite 000-default
sudo apache2ctl configtest && sudo systemctl reload apache2
sudo apache2ctl -S
```

```console
VirtualHost configuration:
*:443  cdn.drill.example.com (/etc/apache2/sites-available/redirector.conf:12)
*:80   cdn.drill.example.com (/etc/apache2/sites-available/redirector.conf:1)
```

**解读（`apache2ctl -S` 就是"我的配置到底生效了吗"的答案）**。

**Step 4：验证分流（**这一步必须做，否则你不知道自己配对了没有**）**

```bash
# ① 模拟"植入体"：UA 与路径都匹配 → 应该被转发到后端 C2
curl -sk -o /dev/null -w 'C2 路径: %{http_code}\n' \
  -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/124.0' \
  'https://cdn.drill.example.com/api/v2/telemetry?session=test' \
  --resolve cdn.drill.example.com:443:127.0.0.1
```

```console
C2 路径: 200
```

```bash
# ② 模拟"扫描器/普通访客"：不匹配 → 应该拿到正常站点
curl -sk -o /dev/null -w '普通访问: %{http_code}\n' \
  -A 'Mozilla/5.0 (compatible; Nmap Scripting Engine)' \
  'https://cdn.drill.example.com/' \
  --resolve cdn.drill.example.com:443:127.0.0.1
```

```console
普通访问: 200
```

```bash
# ③ 看日志确认两条路径分别走了哪里
sudo tail -5 /var/log/apache2/redirector_access.log
```

```console
127.0.0.1 - - [02/Mar/2026:11:02:10 +0800] "GET /api/v2/telemetry?session=test HTTP/1.1" 200 42 UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) ... Edge/124.0"
127.0.0.1 - - [02/Mar/2026:11:02:25 +0800] "GET / HTTP/1.1" 200 1234 UA="Mozilla/5.0 (compatible; Nmap Scripting Engine)"
```

**解读**：**这就是重定向器的完整验证闭环**：

| 测试 | 期望 | 说明 |
|------|------|------|
| 匹配 UA + 路径 + 来源 | 转发到 C2（后端返回内容） | 植入体能工作 |
| 不匹配 | 返回正常站点 | 扫描器/防御方看到的是普通网站 |
| 来源不在授权网段 | **不转发**（返回正常站点） | `RewriteCond %{REMOTE_ADDR}` 生效 → **保护自己** |

**Step 5：检查"伪装"是否到位（**别人看到什么**）**

```bash
# 看响应头（Server 头是否暴露过多信息）
curl -skI --resolve cdn.drill.example.com:443:127.0.0.1 https://cdn.drill.example.com/ | head -12
```

```console
HTTP/1.1 200 OK
Date: ...
Server: Apache
Content-Type: text/html; charset=UTF-8
...
```

```bash
# 看 404 行为（是否泄露目录结构）
curl -sk -o /dev/null -w '%{http_code}\n' \
  --resolve cdn.drill.example.com:443:127.0.0.1 https://cdn.drill.example.com/nonexistent
```

```console
404
```

**解读**：`Server: Apache`（不是 `Apache/2.4.x (Debian)`）说明 `ServerTokens Prod` 生效；`/nonexistent` 返回 404 但内容是你自定义的页面说明 `ErrorDocument` 生效。**这些细节决定了"别人一眼看出这是攻击基础设施"还是"看起来像个正经 CDN 子域"。**

### 场景 3：多后端分流、访问控制与日志分析

**3a. 同一入口分流到多个后端（多目标演练）**

```apache
# 按 Host 分流（不同演练目标用不同域名）
<VirtualHost *:443>
    ServerName ops.drill.example.com
    RewriteEngine On
    RewriteRule ^/(.*)$ http://127.0.0.1:8443/$1 [P,L]
    ProxyPassReverse / http://127.0.0.1:8443/
</VirtualHost>

<VirtualHost *:443>
    ServerName cdn.drill.example.com
    RewriteEngine On
    RewriteRule ^/(.*)$ http://127.0.0.1:9443/$1 [P,L]
    ProxyPassReverse / http://127.0.0.1:9443/
</VirtualHost>
```

**解读**：一个 Apache 入口 + 多个域名 = **多个演练项目互不干扰**（每个目标一个域名/一个 C2 会话），且**对外只暴露一个 IP**。

**3b. 访问控制（**授权测试的合规底线**）**

```apache
<VirtualHost *:443>
    ServerName cdn.drill.example.com
    # 只允许授权网段访问（防止被他人利用，也防止超范围测试）
    <Location "/api/v2">
        Require ip 192.168.56.0/24
        Require ip 10.10.0.0/16
    </Location>

    # 给管理/调试路径加基本认证
    <Location "/debug">
        AuthType Basic
        AuthName "restricted"
        AuthUserFile /etc/apache2/.htpasswd
        Require valid-user
    </Location>
</VirtualHost>
```

```bash
# 生成口令文件（-B 用 bcrypt，别用默认的弱哈希）
sudo htpasswd -cB /etc/apache2/.htpasswd drilladmin
sudo apache2ctl configtest && sudo systemctl reload apache2
```

**解读**：`Require ip` 是**必须的**——它确保你的重定向器**不会成为对全网开放的开放代理**（开放代理本身在很多司法辖区就是问题，且会被他人滥用）。

**3c. 日志分析（**从日志里看"谁在跟你说话"**）**

```bash
# 统计访问量最高的 UA（看有多少是植入体、多少是扫描器）
sudo awk -F'UA="' '{print $2}' /var/log/apache2/redirector_access.log \
  | sed 's/"$//' | sort | uniq -c | sort -rn | head -10
```

```console
    142 Mozilla/5.0 (Windows NT 10.0; Win64; x64) ... Edge/124.0     ← 植入体回连
     31 Mozilla/5.0 (compatible; Nmap Scripting Engine)              ← 被扫描
      8 curl/8.5.0                                                   ← 手工探测
```

```bash
# 找出所有"非植入体"的来源 IP（潜在的防御方探测）
sudo grep -v 'Edge/124' /var/log/apache2/redirector_access.log \
  | awk '{print $1}' | sort | uniq -c | sort -rn | head
```

**解读（重定向器的第二大价值）**：**日志是"是否被发现"的唯一可靠信号**。

| 观察 | 含义 | 建议 |
|------|------|------|
| 大量未知 UA 访问 C2 特征路径 | **有人在试探你的 C2** | 记录并上报（授权演练中的重要发现） |
| 同一 IP 高频 404 | 目录爆破 | `Options -Indexes` 已挡住泄露 |
| UA 含安全厂商特征 | **被安全设备盯上** | 立即评估是否需要更换基础设施 |
| 只在演练时间窗外有访问 | **有人在长期监控你的资产** | 这是需要向客户报告的发现 |

**3d. 收尾：拆除重定向器（**必须做**）**

```bash
sudo a2dissite redirector assets
sudo a2ensite 000-default
sudo systemctl reload apache2
rm -f /var/www/html/assets/logo_update.bin
sudo rm -f /etc/apache2/sites-available/redirector.conf
# 保留日志用于报告，然后按约定销毁
sudo grep -c . /var/log/apache2/redirector_access.log
```

**解读**：**测试结束必须做到"基础设施可回收"**：停服务、删配置、删载荷、留日志（作为证据）后按约定销毁。**这既是对客户的交付要求，也是保护自己的方式。**

---

## 6. 输出解读

### 6.1 配置检查输出

| 输出 | 含义 | 动作 |
|------|------|------|
| `Syntax OK` | 配置语法正确 | 可以 reload |
| `Syntax error on line N of ...` | **配置有错** | 按行号修；**不要在有语法错时 reload**（会失败但可能留隐患） |
| `apache2ctl -S` 列出 vhost 与端口 | 生效的虚拟主机与监听 | 确认"请求走哪个 vhost" |
| `apache2ctl -M` 里的 `rewrite_module (shared)` | 模块已加载 | 没看到就 `a2enmod` |
| `Could not reliably determine the server's fully qualified domain name` | 未设 `ServerName`（警告） | 在配置里加 `ServerName` |

### 6.2 访问日志（自定义格式）

```console
<来源IP> <时间> "<请求行>" <状态码> <字节数> UA="<User-Agent>"
```

| 字段 | 分析价值 |
|------|----------|
| 来源 IP | 谁在访问（**结合 `Require ip` 判断是否越界**） |
| 请求行（含 URI/查询串） | 走的是 C2 路径还是伪装路径 |
| 状态码 | `200` 正常；`403` 被访问控制拦（配置生效）；`404` 目录爆破；`500` **后端 C2 出问题** |
| 字节数 | 植入体回连的典型尺寸（异常大/小都值得看） |
| **UA** | **区分植入体 / 扫描器 / 安全厂商的关键字段** |
| Referer（如记录） | 浏览器访问的来源 |

**关键判断**：

| 现象 | 含义 |
|------|------|
| C2 路径返回 `500`/`502` | 后端 C2 挂了或 `ProxyPass` 地址不对 |
| C2 路径返回 `403` | **你的 `Require ip` 把植入体也拦了**（常见失误） |
| 伪装路径返回 `200` 且内容正常 | 伪装生效 |
| 出现大量不同 UA 访问 C2 路径 | **C2 已被发现并在被分析** |

---

## 7. 与其他工具配合

```
① 载荷生成
   msfvenom / sliver generate          ← ../06-漏洞利用/msfvenom.md、sliver.md
        │
② 托管（让目标稳定下载）
   apache2（DocumentRoot + 正确的 MIME/伪装）        ← 本文
        │
③ C2 后端（不对外暴露）
   sliver（mtls/https/dns） / empire / metasploit   ← sliver.md、../08-后渗透/powershell-empire.md
        │
④ 前置重定向器（对外只暴露这一层）
   apache2（mod_rewrite 条件分流 + mod_proxy 反代）  ← 本文
   socat（更简单的纯端口转发）                       ← socat.md
        │
⑤ 通路与横向
   chisel / ligolo-ng / proxychains4                ← ../08-后渗透/
        │
⑥ 记录与报告
   cherrytree / dradis                              ← ../11-社会工程与报告/
```

**重定向器方案选型**：

| 场景 | 方案 |
|------|------|
| 只是把端口转到 C2（不需要按条件分流） | **`socat`**（一条命令） |
| 需要按 UA/路径/域名分流，或需要伪装成正常网站 | **Apache（mod_rewrite + mod_proxy）** |
| 需要 TLS 终结 + 可信证书 | **Apache（mod_ssl）** 或 socat 的 `OPENSSL-LISTEN` |
| 需要穿透企业 HTTP 代理 | `chisel`（反向 SOCKS over HTTP） |

- 简单中继：[`socat.md`](socat.md) ｜ C2 框架：[`sliver.md`](sliver.md)
- 隧道：[`../08-后渗透/chisel.md`](../08-后渗透/chisel.md)、[`../08-后渗透/ligolo-ng.md`](../08-后渗透/ligolo-ng.md)、[`../08-后渗透/proxychains4.md`](../08-后渗透/proxychains4.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `Syntax error on line N` | 配置写错（少了 `</VirtualHost>`、指令拼错） | 按行号修；用 `apache2 -L` 查指令 |
| 改了配置没生效 | 忘了 reload / 站点没 `a2ensite` | `sudo a2ensite <site>` → `apache2ctl configtest` → `systemctl reload apache2` |
| 请求走了默认站点 | `000-default` 还在、或 `ServerName` 不匹配 | `sudo a2dissite 000-default`；`apache2ctl -S` 确认匹配 |
| `RewriteRule` 不生效 | 没启用 `mod_rewrite`，或 `AllowOverride` 不允许 `.htaccess`，或路径正则写错 | `a2enmod rewrite`；`apache2ctl -M`；在 vhost 里直接写规则（不依赖 .htaccess） |
| 反代报 `503 Service Unavailable` | 后端 C2 没起/地址端口错 | `curl` 直接访问后端端口验证；检查 `ProxyPass` 地址 |
| 反代后后端收到错误的 Host | 缺 `ProxyPreserveHost On` | 加上；C2 常依赖 Host |
| 反代后重定向跑丢 | 缺 `ProxyPassReverse` | 补上 |
| **`Require ip` 把植入体也拦了** | 条件过严（限制到了 C2 路径） | 把 `Require` 限定在**管理路径**，C2 路径按 UA/路径判断；或把植入体来源加入白名单 |
| 端口 80/443 起不来 | 被 `socat`/nginx/其它服务占用 | `sudo ss -lntp \| grep -E ':80\|:443'`；停冲突服务 |
| 浏览器报证书错误 | 自签证书 | **用 Let's Encrypt 真实证书**（自签 = 自我暴露） |
| 日志里看到大量扫描器 UA | **你的基础设施被发现了** | 记录并上报；考虑更换域名/路径/前置 IP |
| 403 Forbidden（普通路径） | 权限/`Require` 配置 | 检查 `<Directory>` 的 `Require` 与文件权限（`www-data` 可读） |
| `Options -Indexes` 后访问目录 403 | 这是**预期行为** | 给目录加 `index.html`，或允许列表（不建议） |
| 中文乱码 | 未设 `AddDefaultCharset utf-8` | 加上；或按需指定 |
| 磁盘被日志写满 | 未做日志轮转 | 用 `logrotate`（Debian 默认已有 `/etc/logrotate.d/apache2`） |
| 想多实例/多端口 | 端口占用/配置混用 | 用 `Listen` + 多个 vhost；或 `-f`/`-d` 起独立实例 |

---

## 9. 防御视角（蓝队）

Apache 在红队手里是**重定向器与托管点**，对蓝队而言则是**两面**：既是要防御的**被滥用组件**，也是**自己可以用的加固工具**。

### 9.1 作为"被利用的基础设施"如何检测

| 红队做法 | 检测信号 | 缓解 |
|----------|----------|------|
| **重定向器**（按 UA/路径分流） | 服务器上出现**非业务 vhost**；配置里出现 `RewriteRule ... [P]`；日志中出现大量第三方域名 | **配置基线管理**（Ansible/配置审计）；怀疑主机时检查 `/etc/apache2/sites-enabled/` |
| **托管恶意载荷** | Web 目录出现可执行文件/二进制；`Content-Type: application/octet-stream` 的非常规文件被大量下载 | 文件完整性监控；**Web 根目录禁止存放可执行文件**；出站/下载行为检测 |
| **TLS 到可疑后端** | Apache 进程向内部 IP 的特定端口建立长连接（`mod_proxy` 的特征） | 主机侧出站限制；服务不应能发起任意出站连接 |
| **日志被用于侦察** | —— | 这属于攻击方行为，蓝队可反向利用：**看自己日志中是否有异常 UA 访问**（也是威胁狩猎线索） |
| **被改成开放代理**（未设 `Require ip`） | 你的服务器出现在开放代理扫描列表中；大量外部 IP 通过它访问第三方 | 强制 `Require ip`/`ProxyRequests Off`（**默认 Off，别打开**） |

### 9.2 作为"防御方工具"的正确用法（**这才是蓝队该做的事**）

| 场景 | 用 Apache 怎么做 |
|------|------------------|
| 反向代理保护内部应用 | `mod_proxy` 把应用藏在后面，只暴露 443 |
| **统一 TLS 与证书管理** | `mod_ssl` + Let's Encrypt + HSTS |
| **安全响应头** | `Header always set Strict-Transport-Security ...`、`X-Content-Type-Options nosniff`、`X-Frame-Options DENY`、`Content-Security-Policy` |
| 隐藏版本信息 | `ServerTokens Prod` + `ServerSignature Off` |
| 访问控制与认证 | `Require ip`、`AuthType Basic`（配合 mTLS 更好） |
| 速率限制 | `mod_ratelimit`；或前置 WAF/网关 |
| 禁止危险方法 | `<LimitExcept GET POST HEAD> Require all denied </LimitExcept>` |
| 日志与审计 | `CustomLog` 记录 UA/Referer + 集中日志（**注意：日志里会含个人信息，需合规管理**） |
| 目录与上传安全 | `Options -Indexes -ExecCGI`；上传目录 **禁止执行 PHP**（`php_admin_flag engine off`） |

```apache
# 蓝队加固示例（可直接用于生产站点）
<VirtualHost *:443>
    ServerName app.example.com
    ServerTokens Prod
    ServerSignature Off
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
    Header always set X-Content-Type-Options "nosniff"
    Header always set X-Frame-Options "DENY"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
    <Directory /var/www/app>
        Options -Indexes -ExecCGI
        AllowOverride None
        Require all granted
        <LimitExcept GET POST HEAD>
            Require all denied
        </LimitExcept>
    </Directory>
</VirtualHost>
```

**蓝队落地清单（按 ROI 排序）**：

1. **配置基线 + 变更告警**：任何新 vhost、新 `RewriteRule [P]`、新 `LoadModule proxy*` 都应告警（**这能抓住重定向器的部署**）；
2. **Web 根目录禁止可执行与二进制文件**（配合 FIM）；
3. **服务出站限制**：Web 服务器**不应该**能随意向外/向内网发起连接（这能掐死重定向器与 SSRF）；
4. **上传目录禁止执行**：配合 [`../08-后渗透/weevely.md`](../08-后渗透/weevely.md) 的防御章节；
5. **日志集中化**：本地日志可被清（对手可能删日志），集中收集才有取证价值。

---

## 10. 参考

- Apache HTTP Server 官方文档（2.4）：<https://httpd.apache.org/docs/2.4/>
- 指令速查（按字母序，包含全部 mod 指令）：<https://httpd.apache.org/docs/2.4/mod/directives.html>
- `mod_rewrite` 详细文档（**重定向器的核心**）：<https://httpd.apache.org/docs/2.4/mod/mod_rewrite.html>
- `mod_proxy` 文档：<https://httpd.apache.org/docs/2.4/mod/mod_proxy.html>
- Kali 工具页：<https://www.kali.org/tools/apache2/>
- 本地资源：`apache2 -L`（列出全部指令）、`apache2ctl -S`、`apache2ctl -M`、`man apache2`、`/etc/apache2/` 目录
- 相关教程：[`socat.md`](socat.md)、[`sliver.md`](sliver.md)、[`../08-后渗透/README.md`](../08-后渗透/README.md)

## ⚠️ 法律与伦理

**Apache 是最普通、最合法的服务器软件**（互联网上一半以上的站点都用它）。风险完全来自**你用它承载什么、转发到哪里**：

- **托管恶意载荷**并诱导他人下载执行：可能触犯《刑法》第 285 条（非法获取计算机信息系统数据、非法控制计算机信息系统）、第 286 条（破坏计算机信息系统）；
- **搭建 C2 重定向器**攻击未授权目标：同上，且通常被认定为**共同犯罪**的一环；
- **把服务器配成开放代理/转发器**：可能违反《网络安全法》第 27 条，且会被他人滥用并牵连到你；
- **未设访问控制的转发器**还会让**你无法证明"我只测试了授权范围"**——这对蓝队/司法认定非常不利。

**使用要求**：

1. **只在授权范围与时间窗内转发/托管**；`RewriteCond %{REMOTE_ADDR}` 与 `Require ip` **不是可选项，是必需项**；
2. **使用可信证书**（自签证书会让浏览器告警，等于主动暴露）；
3. **日志完整保留**（它既是分析工具，也是"我做了什么"的证据）；
4. **测试结束拆除**：`a2dissite` + 删配置 + 删载荷 + 停服务，并保留拆除记录；
5. **绝不把服务器配成开放代理**（`ProxyRequests` 保持默认 Off）；
6. 本教程示例请在**完全隔离的自建实验室**中复现（自己的域名、自己的靶机、Host-Only 网络）。
