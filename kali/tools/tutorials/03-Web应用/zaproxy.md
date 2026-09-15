# zaproxy（OWASP ZAP：Web 应用安全测试代理）

> **一句话**：一个能当**拦截代理**、又能当**自动化扫描器**的 Web 安全测试平台——手工浏览器测试（改包、重放、爆破）和自动化主动扫描（爬虫 + 规则）都在一个工具里，还是开源的。
> **分类**：Web 应用 / 代理与自动化扫描 ｜ **Kali 包**：`zaproxy`（命令 `zaproxy`、`owasp-zap`）｜ **官方文档**：<https://www.kali.org/tools/zaproxy/> ｜ 上游：<https://www.zaproxy.org>

---

## 1. 它解决什么问题

Web 应用测试需要**两种截然不同的工作模式**，ZAP 把两者放进同一个工具：

| 模式 | 需要什么 | ZAP 的能力 |
|------|----------|------------|
| **手工测试**（占真实工作量的 70%+） | **拦截代理**：看/改/重放每一个请求 | ZAP 作为 HTTP(S) 代理，浏览器流量全经过它；Breakpoints、Repeater（Request Editor）、Fuzzer |
| **自动化扫描** | 爬虫 + 漏洞规则 + 报告 | Spider / AJAX Spider / Active Scan / Passive Scan + 报告导出 |

再加三件真实工作中必需的能力：

- **认证测试**：能配置表单/脚本/Session 认证，让扫描器「登录后再扫」；
- **API 测试**：导入 OpenAPI / GraphQL / Postman 定义直接测 API；
- **CI 集成**：`-cmd -quickurl ... -quickout ...` 一条命令跑完出报告；`-autorun` 跑可版本化的自动化计划（YAML）。

**对比同胞（选型是最关键的一节）**：

| 维度 | **OWASP ZAP** | **Burp Suite** | 其他 |
|------|---------------|----------------|------|
| 授权/价格 | **开源免费**（Apache 2.0） | Community 免费但**限功能**；Pro 商业收费 | —— |
| 拦截代理 | ✅ 完整 | ✅ 更成熟（Repeater/Intruder 体验最好） | mitmproxy 更偏脚本化（见 [`../07-嗅探与欺骗/mitmproxy.md`](../07-嗅探与欺骗/mitmproxy.md)） |
| 自动化扫描 | ✅ **免费版就有完整主动扫描** | **主动扫描是 Pro 功能** | —— |
| CI 集成 | ✅ `-cmd`/`-autorun`，官方有 Docker 镜像 | 需 Pro / 自研 | nikto/nuclei 更轻（见 [`nikto.md`](../02-漏洞分析/nikto.md)、[`nuclei.md`](../02-漏洞分析/nuclei.md)） |
| 认证/AJAX 应用 | ✅ 有，配置略繁琐 | ✅ 更好用 | —— |
| 插件生态 | 官方 Marketplace + 社区 | BApp Store（部分需 Pro） | —— |
| 上手曲线 | 平缓 | 中等 | —— |

**结论**：

- **预算有限 / 要自动化 / 要进 CI** → **ZAP**；
- **纯手工深入测试、追求效率** → Burp（多数人两个都装：Burp 手工、ZAP 自动化）；
- **只做「快速看一眼有没有明显问题」** → nikto/nuclei 更轻。

**ZAP 常被低估的一点**：它的 **Passive Scan（被动扫描）** 在**代理模式下自动运行**——你正常浏览目标站点时，它就在后台检查响应头、Cookie 属性、信息泄露等**不需要攻击性请求**的问题。这是**零成本**的额外覆盖。

---

## 2. 工作原理

ZAP 有两种身份：**代理（Proxy）** 和 **扫描引擎（Scanner）**。

```
┌──────────────────────────── 代理模式（手工测试） ────────────────────────────┐
   浏览器 ──► [ ZAP Proxy :8080 ] ──► 目标站点
                  │
                  ├─ ① 拦截（Breakpoints）：暂停请求/响应，人工修改
                  ├─ ② 历史（History）：所有经过的请求都被记录（可搜索、可重放）
                  ├─ ③ 被动扫描（Passive Scan）：对每个响应自动跑「不需要攻击」的检查
                  │      ・安全响应头缺失（CSP/HSTS/X-Content-Type-Options…）
                  │      ・Cookie 属性（HttpOnly/Secure/SameSite）
                  │      ・信息泄露（Server 版本、注释、错误栈）
                  │      ・反 CSRF 机制缺失
                  └─ ④ 手动工具：Request Editor（Repeater）/ Fuzzer / Encoder
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────── 扫描模式（自动化） ──────────────────────────────┐
   目标 URL
      │
      ├─ ① 爬取（Spider）        传统爬虫：解析 HTML 链接/表单
      │         （AJAX Spider）  用真实浏览器跑 JS，抓 SPA/动态站点
      │
      ├─ ② 构建「站点树（Sites Tree）」= 已知的所有 URL + 参数
      │
      ├─ ③ 被动扫描（Passive）   对爬到的所有响应跑非攻击性检查
      │
      └─ ④ 主动扫描（Active Scan）
               对每个「URL + 参数」注入一堆测试载荷：
                 SQL 注入 / XSS / 路径穿越 / 命令注入 / XXE /
                 SSRF / CRLF / 反序列化 / 参数污染 / 备份文件…
               用「响应差异 + 规则库」判定是否命中 → Alert
                          │
                          ▼
              Alert（告警）：风险等级 + 置信度 + 证据 + 修复建议
                          │
                          ▼
                   报告（HTML/JSON/MD/XML）
└──────────────────────────────────────────────────────────────────────────────┘
```

**关键概念**：

- **被动 vs 主动（最重要的区分）**：
  | | 被动扫描 | 主动扫描 |
  |---|---|---|
  | 会不会发攻击性请求 | **不会**（只看已有响应） | **会**（大量注入） |
  | 风险 | 极低 | **会触发 WAF/告警、可能破坏数据** |
  | 覆盖 | 配置类问题 | 注入类问题 |
  | 何时用 | **任何时候**（含测试生产只读） | **只在授权环境**，最好在预发 |
- **Alert 的两个维度**：
  - **Risk（风险）**：High / Medium / Low / Informational；
  - **Confidence（置信度）**：High / Medium / Low / False Positive。
  **「High risk + Low confidence」必须人工核实**——这是 ZAP 报告最容易被误读的地方。
- **Session（会话）**：ZAP 把「本次测试的全部状态」存在一个 session 里（`-newsession`/`-session`）。**测试一个目标一个 session**，否则历史记录混在一起没法分析。
- **Context（上下文）**：把「目标范围」显式定义为一组 URL 正则 + 包含/排除规则。**没有 Context，爬虫和主动扫描可能跑到站外**（这是最危险的操作失误）。
- **认证（Authentication）**：告诉 ZAP「怎么登录」，之后主动扫描会带着会话跑（否则只能扫到未登录可见的部分）。
- **自动化计划（Automation Framework）**：`-autorun plan.yaml` 用一种声明式 YAML 描述「环境 + 爬取 + 扫描 + 报告」的完整流程。**这是把 ZAP 用进 CI 的正路**（比命令行参数拼装可控、可版本化）。
- **Add-on（插件）**：ZAP 的功能大量来自插件，`-addoninstall <id>`、`-addonlist` 可以在命令行管理。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install zaproxy
command -v zaproxy owasp-zap
```

```console
root@kali:~# command -v zaproxy owasp-zap
/usr/bin/zaproxy
/usr/bin/owasp-zap
```

```bash
zaproxy -version
zaproxy -h        # 与 owasp-zap -h 等价，同一个启动脚本
```

```console
root@kali:~# zaproxy -h
Found Java version 25.0.4
Available memory: 7941 MB
Using JVM args: -Xmx1985m
Usage:
	zap.sh [Options]
Core options:
	-version                 Reports the ZAP version
	-cmd                     Run inline (exits when command line options complete)
	-daemon                  Starts ZAP in daemon mode, i.e. without a UI
	-config <kvpair>         Overrides the specified key=value pair in the configuration file
	-configfile <path>       Overrides the key=value pairs with those in the specified properties file
	-dir <dir>               Uses the specified directory instead of the default one
	-installdir <dir>        Overrides the code that detects where ZAP has been installed with the specified directory
	-h                       Shows all of the command line options available, including those added by add-ons
	-help                    The same as -h
	-newsession <path>       Creates a new session at the given location
	-session <path>          Opens the given session after starting ZAP
	-lowmem                  Use the database instead of memory as much as possible - this is still experimental
	-experimentaldb          Use the experimental generic database code, which is not surprisingly also still experimental
	-nostdout                Disables the default logging through standard output
	-loglevel <level>        Sets the log level, overriding the values specified in the log4j2.properties file in the home directory
	-sbomzip <path>          Creates a zip file containing all of the available SBOMs
	-suppinfo                Reports support info to the command line and exits
	-silent                  Ensures ZAP does not make any unsolicited requests, including check for updates
Add-on options:
	-graphqlfile <path>       Imports a GraphQL Schema from a File
	-graphqlurl <url>         Imports a GraphQL Schema from a URL
	-graphqlendurl <url>      Sets the Endpoint URL
	-script <script>         Run the specified script from commandline or load in GUI
	-postmanfile <path>          Imports a Postman collection from the specified file name.
	-postmanurl <url>            Imports a Postman collection from the specified URL.
	-postmanendpointurl <url>    The endpoint URL, to override the base URLs present in the Postman collection.
	-notel                   Turns off telemetry calls
	-addoninstall <addOnId>   Installs the add-on with specified ID from the ZAP Marketplace
	-addoninstallall          Install all available add-ons from the ZAP Marketplace
	-addonuninstall <addOnId> Uninstalls the Add-on with specified ID
	-addonupdate              Update all changed add-ons from the ZAP Marketplace
	-addonlist                List all of the installed add-ons
	-quickurl <target url>   The URL to attack, e.g. http://www.example.com
	-quickout <filename>     The file to write the HTML/JSON/MD/XML results to (based on the file extension)
	-quickprogress:          Display progress bars while scanning
	-zapit <target url>      The URL to perform a quick 'reconnaissance' scan on, e.g. http://www.example.com The -cmd option must be specified
	-autorun <source>        Run the automation jobs specified in the file or from the URL
	-autogenmin <filename>   Generate template automation file with the key parameters
	-autogenmax <filename>   Generate template automation file with all parameters
	-autogenconf <filename>  Generate template automation file using the current configuration
	-autocheck <source>      Check the specified automation plan in the file or from the URL
	-certload <path>         Loads the Root CA certificate from the specified file name
	-certpubdump <path>      Dumps the Root CA public certificate into the specified file name, this is suitable for importing into browsers
	-certfulldump <path>     Dumps the Root CA full certificate (including the private key) into the specified file name, this is suitable for importing into ZAP
	-host <host>             Overrides the host of the main proxy, specified in the configuration file
	-port <port>             Overrides the port of the main proxy, specified in the configuration file
	-hud                     Launches a browser configured to proxy through ZAP with the HUD enabled, for use in daemon mode
	-hudurl <url>            Launches a browser as per the -hud option with the specified URL
	-hudbrowser <browser>    Launches a browser as per the -hud option with the specified browser, supported options: Chrome, Firefox by default Firefox
	-openapifile <path>      Imports an OpenAPI definition from the specified file name
	-openapiurl <url>        Imports an OpenAPI definition from the specified URL
	-openapitargeturl <url>  The Target URL, to override the server URL present in the OpenAPI definition. Refer to the help for supported format.
```

> ⚠️ 上面的选项列表**包含 add-on 提供的选项**，**随安装的插件不同而变化**。以你本机的 `zaproxy -h` 为准。

**启动方式一：图形界面（最常用）**

```bash
zaproxy
```

**启动方式二：daemon（无界面，当代理服务器用）**

```bash
zaproxy -daemon -host 127.0.0.1 -port 8080
```

**启动方式三：一条命令快速扫描出报告（CI 友好）**

```bash
zaproxy -cmd -quickurl http://127.0.0.1:8080/ -quickout /tmp/zap-report.html -quickprogress
```

**生成并运行自动化计划（推荐的正路）**

```bash
zaproxy -autogenmin /tmp/zap-plan-min.yaml      # 生成最小模板
cat /tmp/zap-plan-min.yaml
zaproxy -autocheck /tmp/zap-plan-min.yaml       # 先校验计划
zaproxy -autorun /tmp/zap-plan-min.yaml         # 执行
```

---

## 4. 核心参数详解

> 全部取自上面的 `zaproxy -h` 原文（含 add-on 选项）。**选项名的大小写与连字符必须完全照写**（ZAP 的参数风格比较特殊）。

### 4.1 核心（启动模式与配置）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-version` | 打印 ZAP 版本 | 排错/记录环境 |
| `-h` / `-help` | 显示**全部**选项（含 add-on） | **以它为准**；不同插件下选项不同 |
| `-daemon` | **无界面守护模式** | 当代理服务器、被其他工具驱动时用 |
| `-cmd` | **命令行模式，做完即退出** | **CI/脚本必加**（否则 ZAP 会一直挂着） |
| `-config <kvpair>` | 覆盖配置项（`key=value`） | 细粒度调参的标准方式，可重复 |
| `-configfile <path>` | 用 properties 文件批量覆盖配置 | 一套配置多环境复用 |
| `-dir <dir>` | 用指定目录替代默认目录 | 隔离配置/插件，便于多实例 |
| `-installdir <dir>` | 覆盖「安装目录探测结果」 | 自编译/特殊安装时用 |
| `-newsession <path>` | **新建会话** | **每次测试一个新会话**（否则历史混在一起） |
| `-session <path>` | 打开已有会话 | 继续上次测试 |
| `-lowmem` | 尽量用数据库替代内存（实验性） | 大扫描 + 小内存机器 |
| `-experimentaldb` | 实验性通用数据库后端 | 一般情况下别开 |
| `-nostdout` | 关闭标准输出日志 | 由外部收集日志时用 |
| `-loglevel <level>` | 设置日志级别 | 排错时调高 |
| `-silent` | **不发任何「非请求性」流量**（含检查更新） | **护网/严格隔离环境必加** |
| `-suppinfo` | 输出支持信息并退出 | 报 bug 时用 |
| `-sbomzip <path>` | 导出所有组件的 SBOM 包 | 供应链合规 |

### 4.2 快速扫描（一条命令出报告）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-quickurl <url>` | 要扫描的目标 | **必须搭配 `-cmd`** |
| `-quickout <file>` | 报告文件，**格式由扩展名决定**（HTML/JSON/MD/XML） | 出 `.html` 给人看、`.json` 给 CI |
| `-quickprogress` | 显示进度条 | 交互式运行时用；**CI 里建议不加**（进度条会污染日志） |
| `-zapit <url>` | **只做快速侦察扫描**（需 `-cmd`） | 比 quickurl 更轻，快速摸底 |

### 4.3 自动化计划（Automation Framework，推荐）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-autorun <source>` | **执行自动化计划**（本地文件或 URL） | **CI 的正路**：计划文件进版本控制 |
| `-autogenmin <file>` | 生成**最小**参数计划模板 | 上手起点 |
| `-autogenmax <file>` | 生成**全参数**计划模板 | 查所有可用配置项 |
| `-autogenconf <file>` | 用**当前配置**生成计划 | 「GUI 里调好了，导出成计划」——**极实用** |
| `-autocheck <source>` | **只校验**计划，不执行 | **CI 里先校验再跑** |

### 4.4 代理与证书

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-host <host>` | 覆盖主代理监听地址 | **默认绑本机最安全**；绑 `0.0.0.0` 前想清楚 |
| `-port <port>` | 覆盖主代理端口 | 默认 8080；与 Burp 冲突时改 |
| `-certload <path>` | 加载指定根 CA 证书 | 复用已有 CA |
| `-certpubdump <path>` | **导出根 CA 公钥证书** | **导入浏览器信任**（做 HTTPS 拦截的前提） |
| `-certfulldump <path>` | 导出**含私钥**的完整证书 | **⚠️ 极高敏感**：私钥泄露 = 可中间人任何流量 |

### 4.5 HUD（浏览器内界面）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-hud` | 启动「配好代理 + 开启 HUD」的浏览器 | **daemon 模式下手工测试的推荐方式** |
| `-hudurl <url>` | 同上，并直接打开指定 URL | —— |
| `-hudbrowser <browser>` | 指定浏览器（默认 Firefox，支持 Chrome） | 按本机装了哪个用 |

### 4.6 导入 API 定义（测 API 的关键）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-openapifile <path>` | 导入 **OpenAPI/Swagger** 定义（文件） | REST API 测试首选 |
| `-openapiurl <url>` | 从 URL 导入 OpenAPI 定义 | 有些服务提供 `/openapi.json` |
| `-openapitargeturl <url>` | 覆盖定义里的 server 地址 | **定义里写的是生产地址、要测测试环境时必用** |
| `-graphqlfile <path>` | 导入 GraphQL Schema（文件） | GraphQL API |
| `-graphqlurl <url>` | 从 URL 导入 GraphQL Schema | 可配内省查询 |
| `-graphqlendurl <url>` | 设置 GraphQL 端点 URL | —— |
| `-postmanfile <path>` | 导入 Postman collection（文件） | 已有 Postman 集合时最省事 |
| `-postmanurl <url>` | 从 URL 导入 Postman collection | —— |
| `-postmanendpointurl <url>` | 覆盖 collection 里的 base URL | **测试环境切换的关键** |

### 4.7 插件与脚本

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-addonlist` | 列出已安装插件 | 确认某功能是否可用 |
| `-addoninstall <id>` | 安装指定插件 | 想用某功能（如 AJAX Spider、OpenAPI）时 |
| `-addoninstallall` | 安装全部插件 | **首次配置**时省事（体积大） |
| `-addonuninstall <id>` | 卸载插件 | —— |
| `-addonupdate` | 更新所有有变化的插件 | 定期更新规则库 |
| `-script <script>` | 从命令行运行脚本 | 用脚本扩展/自动化 |
| `-notel` | **关闭遥测** | **企业环境建议加** |

### 4.8 GUI 里最常用的操作（不是命令行，但必须知道）

| 功能 | 位置 | 用途 |
|------|------|------|
| **Sites Tree** | 左侧 | 所有已知 URL 的树状视图 |
| **History** | 底部 | 全部请求记录，可搜索/重放 |
| **Request Editor（Repeater）** | 右键请求 → Open/Resend | 手工改一个请求反复发 |
| **Break** | 顶部工具条 | 拦截并修改请求/响应（比 Burp 的 Intercept 更细，可拦响应） |
| **Fuzzer** | 右键请求 → Attack → Fuzz | 参数爆破（类似 Burp Intruder） |
| **Spider / AJAX Spider** | 右键站点 → Attack | 传统爬虫 / 浏览器爬虫 |
| **Active Scan** | 右键站点 → Attack | 主动扫描（**注意范围**） |
| **Context / Scope** | 顶部/Sites 右键 | **限定扫描范围 —— 每次都要设** |
| **Session Properties** | 菜单 | 认证、上下文、扫描策略 |
| **Report** | 菜单 Report | 导出 HTML/JSON/MD/XML |

---

## 5. 实战演练

> **环境声明**：以下全部使用**本机自建靶场**（DVWA，见 [`dvwa.md`](../03-Web应用/dvwa.md)）或**你拥有/获得书面授权的目标**。
> - **被动扫描**可以在任何授权目标上安全运行（不发攻击请求）；
> - **主动扫描会发大量注入请求**：可能**触发 WAF 封禁**、**污染数据**、**拖垮站点**。**只能在自己的靶场/预发环境/明确授权的目标上做**；
> - **永远先设置 Scope/Context**——ZAP 的爬虫会跟随链接到站外；
> - **HTTPS 拦截需要信任 ZAP 的 CA**，只在**你自己的浏览器/一次性虚拟机**里导入。

### 场景 1：手工测试的最小闭环（代理 + 被动扫描 + Repeater）

**1a. 起 DVWA 靶场**（见 [`dvwa.md`](../03-Web应用/dvwa.md)，这里用 Docker 版本）

```bash
git clone https://github.com/digininja/DVWA.git /tmp/DVWA 2>/dev/null || true
cd /tmp/DVWA && docker compose up -d
# 浏览器打开 http://localhost:4280 → Setup DVWA → Create/Reset Database
# 默认账号 admin / password
```

```bash
# 1b. 启动 ZAP GUI
zaproxy &
```

**1c. 设置范围（Context）—— 这步不能跳**

GUI 里：

1. 顶部工具条 → **Sites** 面板中右键 → `New Context...`（或菜单 → 分析 → Context）
2. Context 名：`dvwa-local`
3. **Include in Context**：`http://localhost:4280/.*`
4. **Exclude from Context**：把登出、危险操作排除，例如
   ```
   http://localhost:4280/logout\.php
   http://localhost:4280/setup\.php
   ```
5. 顶部 **Scope 图标**（绿色的十字圈）→ 选中该 Context → **只扫 Scope 内的目标**

**解读**：**「Include/Exclude」是 ZAP 的安全带**。没有它，爬虫会跟着 `http://localhost:4280` 页面里的外链跑到站外（DVWA 页面里有指向 OWASP 的链接）。

**1d. 配置浏览器走 ZAP 代理**

| 方式 | 做法 |
|------|------|
| **推荐：HUD** | `zaproxy -hud -hudurl http://localhost:4280` → 自动起配好代理的 Firefox |
| 手动 | 浏览器代理设 `127.0.0.1:8080`（HTTP+HTTPS 都设） |
| 证书 | 访问 `http://zap` → 下载 ZAP 根 CA → 导入浏览器「受信任的根证书颁发机构」 |

**1e. 正常浏览 = 被动扫描自动跑**

用配好代理的浏览器登录 DVWA（`admin`/`password`），逐一点开菜单：SQL Injection、XSS (Reflected)、File Upload…

```console
# ZAP 底部的 "Alerts" 标签会实时出现告警，例如：
#   Low / Medium  Missing Anti-clickjacking Header
#   Medium        Cookie No HttpOnly Flag
#   Low           X-Content-Type-Options Header Missing
#   Informational Server Leaks Version Information via "Server" HTTP Response Header Field
```

**解读**：**这就是被动扫描的价值**——你什么攻击性操作都没做，只是正常浏览，ZAP 就把「响应头/Cookie 配置类问题」全列出来了。**这类问题在任何时候都可以测，风险为零。**

**1f. 手工改包（Repeater）——把「可疑」变成「确认」**

以 DVWA 的 **SQL Injection (low)** 为例：

1. 在 DVWA 页面提交 `id=1`（正常请求）
2. ZAP → **History** → 找到 `GET .../vulnerabilities/sqli/?id=1&Submit=Submit`
3. 右键 → **Open/Resend with Request Editor**（Repeater）
4. 把 `id=1` 改成：
   ```
   id=1' OR '1'='1
   ```
5. 点 **Send** → 看响应

```console
# 响应里出现全部用户（而 `id=1` 只有一个）
ID: 1' OR '1'='1
First name: admin
Surname: admin
ID: 1' OR '1'='1
First name: Gordon
Surname: Brown
...
```

**解读**：**Repeater 是「把扫描器的疑点变成证据」的地方**。ZAP 报的 Alert 只给出「可能有 SQL 注入」，人工在 Repeater 里构造确认性 payload 才能定论。

**1g. 用 Fuzzer 做参数爆破**（DVWA 的 **Brute Force** 模块）

1. 登录页抓一个 `GET /vulnerabilities/brute/?username=admin&password=abc&Login=Login`
2. 右键 → **Attack → Fuzz**
3. 选中 `abc` 位置 → **Add** → 选 **File Fuzzers** → 字典（或用 `/usr/share/wordlists/` 里的列表）
4. 按 **Start Fuzzer**

**解读**：Fuzzer 会逐条替换并发请求，你按**响应长度/状态码**排序找「不一样的那个」。这就是参数爆破的基本手法（Burp 里对应 Intruder）。**只能对自己的靶场/授权目标用。**

### 场景 2：自动化扫描（Quick Scan → 报告 → 复测）

**2a. 命令行一条龙（CI 友好）**

```bash
zaproxy -cmd -quickurl http://localhost:4280/ \
        -quickout /tmp/zap-dvwa.html \
        -quickprogress
ls -lh /tmp/zap-dvwa.html
```

**解读**：`-cmd` 让它「做完就走」（不加会一直挂着），`-quickurl` 会自动跑「爬取 → 被动 → 主动」并直接出报告。**这是最省事的自动化入口**，适合快速摸底。

**2b. 分步做（可控性更高）**

GUI 里：

1. Sites 树里右键 `http://localhost:4280` → **Attack → Spider…** → 选 Context → Start
2. 爬完后 → 右键 → **Attack → AJAX Spider…**（DVWA 是传统 PHP，AJAX Spider 收益不大；**SPA 站点则必须用它**）
3. 右键 → **Attack → Active Scan…** → 选 Context → Start

```console
# ZAP 底部 "Active Scan" 标签会显示进度与发现的告警
# 典型告警（DVWA 故意留的洞）：
#   High   SQL Injection            （sqli 模块）
#   High   Cross Site Scripting     （xss_r / xss_s）
#   High   Remote OS Command Injection（exec）
#   High   Path Traversal           （fi）
#   High   Remote File Inclusion    （fi）
#   Medium Absence of Anti-CSRF Tokens
```

**2c. 导出报告（多格式按需）**

| 目标 | 命令（GUI 菜单 Report → Generate Report） | 说明 |
|------|-------------------------------------------|------|
| 给人看 | 选 **HTML** | 带图表，适合交付 |
| 给 CI/平台 | 选 **JSON** 或 **XML** | 可程序化解析 |
| 给工单系统 | 选 **Markdown** | 直接贴进 issue |
| 给合规 | 选 **HTML + XML** | 证据 + 机读 |

**2d. 修复后复测（识别「真修了」而不是「扫不到了」）**

修改 DVWA 的安全级别（**DVWA Security → high/impossible**），再跑一次同一套扫描：

```bash
zaproxy -cmd -quickurl http://localhost:4280/ -quickout /tmp/zap-dvwa-after.html
```

**解读（这是最容易做错的一步）**：告警数量下降**不等于**漏洞修好了，可能的假象有：

| 假象 | 原因 | 怎么排除 |
|------|------|----------|
| 告警少了，但其实「扫不到了」 | `impossible` 级别改了逻辑/参数名，扫描器的 payload 没适配 | **手工在 Repeater 里复现原 payload** |
| 同一漏洞换了 URL 还在 | 修复只覆盖了部分入口 | 对比两次报告里**同一 Alert 的 URL 集合** |
| 告警变成 `Informational` | 只是被降级，问题可能还在 | 看置信度与证据 |

### 场景 3：认证扫描 + API 扫描 + 自动化计划进 CI

**3a. 配认证，让扫描器「登录后再扫」**

DVWA 的登录是表单认证（`login.php` → 字段 `username`/`password`/`Login`）。GUI 里：

1. Sites 右键 → **Include in Context**（已做）
2. **Context → Authentication**：
   - Authentication Method：**Form-based**
   - Login URL：`http://localhost:4280/login.php`
   - Login Request POST Data：`username={%username%}&password={%password%}&Login=Login`
   - Username/Password：`admin` / `password`
3. Options 里关闭 **"Session Management"** 的「自动检测」（DVWA 用 PHPSESSID）
4. **Context → Users → Add**：`admin` / `password`
5. 右键站点 → **Attack → Active Scan** → 在对话框里选该 User

```console
# 登录后能扫到的告警明显变多（例如需要登录的 xss_s、upload 模块）
```

**解读**：**「未登录扫描」的覆盖率可能不到 30%**——大量功能在登录后。**配认证是提升覆盖率最有效的单项投入。**

**3b. 测 API（OpenAPI 导入）**

```bash
# 假设你的测试环境有 OpenAPI 定义
zaproxy -cmd -openapiurl http://localhost:8081/v3/api-docs \
        -openapitargeturl http://localhost:8081 \
        -quickurl http://localhost:8081/ \
        -quickout /tmp/zap-api.json
```

**解读**：`-openapiurl` 把 API 的**每个端点 + 参数**都变成待测目标（比爬虫可靠得多，因为 API 没有 HTML 链接可爬）。`-openapitargeturl` 用来把定义里的服务地址**改指向测试环境**——**这个参数用错就会去扫生产**。

**3c. 自动化计划（YAML）——CI 的正路**

```bash
zaproxy -autogenmin /tmp/plan.yaml
cat /tmp/plan.yaml
```

```yaml
env:
  contexts:
  - name: "<context name>"
    urls:
    - "<URL>"
jobs:
- type: passiveScan-config
  parameters:
    maxAlertsPerRule: 10
...
- type: spider
...
- type: passiveScan-wait
- type: activeScan
- type: report
  parameters:
    template: modern
    reportFile: <report file>
    reportDir: <report dir>
```

把它改成你的靶场，**先校验再跑**：

```bash
cat > /tmp/plan.yaml <<'EOF'
env:
  contexts:
  - name: "dvwa"
    urls:
    - "http://localhost:4280/"
    includePaths:
    - "http://localhost:4280/.*"
    excludePaths:
    - "http://localhost:4280/logout.*"
    - "http://localhost:4280/setup.*"
  parameters:
    failOnError: true
    progressToStdout: true

jobs:
- type: passiveScan-config
  parameters:
    maxAlertsPerRule: 20
    scanOnlyInScope: true

- type: spider
  parameters:
    context: "dvwa"
    maxDuration: 2
    maxDepth: 5

- type: ajaxSpider
  parameters:
    context: "dvwa"
    maxDuration: 2

- type: passiveScan-wait
  parameters:
    maxDuration: 2

- type: activeScan
  parameters:
    context: "dvwa"
    maxScanDurationInMins: 5
    policy: "Default Policy"

- type: report
  parameters:
    template: "traditional-html"
    reportFile: "zap-dvwa-report"
    reportDir: "/tmp/zap-reports"
EOF

zaproxy -autocheck /tmp/plan.yaml     # 先校验
zaproxy -autorun /tmp/plan.yaml       # 再执行
ls -lh /tmp/zap-reports/
```

**解读**：自动化计划的三个关键点：

| 关键点 | 为什么 |
|--------|--------|
| **`includePaths` + `excludePaths`** | 用声明式的范围限制替代「手动点 Context」；**进 CI 的唯一安全方式** |
| **`maxDuration` / `maxScanDurationInMins`** | **必须有时间上限**，否则 CI 会挂死；也限制对目标的总负载 |
| **`passiveScan-wait`** | 主动扫描前等被动扫描跑完，否则报告不完整 |
| **`report`** | 让 CI 直接拿到产物 |

**3d. 用 `-autogenconf` 把 GUI 配置导出成计划**（省时间的技巧）

```bash
# 在 GUI 里把所有参数调好（认证、策略、报告模板…）
# 然后导出成计划文件，之后 CI 就用这份文件
zaproxy -cmd -autogenconf /tmp/plan-from-gui.yaml
cat /tmp/plan-from-gui.yaml
```

**解读**：**这是「GUI 探索 → 自动化落地」的最佳路径**——手动调参最直观，但进去 CI 必须是文件。`-autogenconf` 把两者打通。

**3e. 清理**

```bash
cd /tmp/DVWA && docker compose down
```

---

## 6. 输出解读

### 6.1 Alert 的两个维度（**读懂 ZAP 报告的关键**）

| 维度 | 取值 | 含义 |
|------|------|------|
| **Risk（风险）** | `High` / `Medium` / `Low` / `Informational` | **影响有多大**（如果真存在） |
| **Confidence（置信度）** | `High` / `Medium` / `Low` / `False Positive` | **有多确定它真的存在** |

**四象限处理原则**：

| | Confidence 高 | Confidence 低 |
|---|---|---|
| **Risk 高** | **立即处理** | **必须人工验证**（可能是误报，也例外可能是最值钱的洞） |
| **Risk 低** | 排期处理 | 可忽略（或加进「可接受风险」清单） |

> **最常见的误读**：「High risk」就直接写进报告。**必须看 Confidence 并用 Repeater 复现**——ZAP 的高风险低置信告警里，误报比例不低（尤其是反射型 XSS 的启发式判定）。

### 6.2 一条 Alert 里有什么

| 字段 | 内容 | 怎么用 |
|------|------|--------|
| Name | 漏洞类型 | 映射到 CWE/OWASP Top 10 |
| Risk / Confidence | 见上 | 定优先级 |
| **URL** | 受影响的具体 URL | **复现入口** |
| **Parameter** | 受影响的参数 | 定位注入点 |
| Evidence | 触发证据（响应片段/请求片段） | 判断真假 |
| **Description** | 漏洞原理 | 报告可直接引用 |
| **Solution** | 修复建议 | 报告里的「整改建议」 |
| Reference | CWE / OWASP 链接 | 报告引用 |
| CWE ID | 标准编号 | 与 Jira/工单系统对齐 |

### 6.3 报告格式选择

| 格式 | 适合 | 说明 |
|------|------|------|
| HTML（traditional / modern） | 交付、评审 | 有图有表，人读 |
| **JSON** | **CI、平台集成** | 机读；ZAP 还有专门的 JSON API |
| **XML** | 与 JUnit/CI 工具链集成 | 也可被其他扫描平台消费 |
| **Markdown** | 贴进工单/Wiki | 轻量 |
| SARIF（部分模板） | 代码扫描平台 | 若模板支持 |

### 6.4 扫描「跑得好不好」的判断

| 观察 | 含义 | 下一步 |
|------|------|--------|
| Sites Tree 里 URL 很少 | 爬虫没爬动（JS 渲染/需要登录） | 上 **AJAX Spider**；**配认证** |
| 主动扫描很快结束 | 待测 URL 少；或 Scope 设太窄 | 检查 Context；先爬够再扫 |
| 告警全是 Informational | 只跑了被动扫描 | 确认主动扫描真的执行了（看 Active Scan 标签） |
| 告警数量异常多且重复 | 同一问题在不同 URL/参数重复 | 报告里按 Alert 类型聚合，别按条数看 |
| 目标出现异常/被封 | 主动扫描太激进 | 降线程、加延时、缩小范围、错峰 |

---

## 7. 与其他工具配合

```
   ┌──────────── 侦察层 ────────────┐
   nmap → 发现 Web 端口             ../01-信息搜集/nmap.md
   whatweb → 指纹/CDN/框架          ../01-信息搜集/whatweb.md
   wafw00f → 有没有 WAF             ../03-Web应用/wafw00f.md
              │
              ▼
   ┌──────────── 目录与入口 ─────────┐
   gobuster / ffuf / dirb → 目录与文件
              │  ../03-Web应用/gobuster.md、ffuf.md、dirb.md
              ▼
   ┌──────────── ZAP：主战场 ────────┐
    代理（手工 + 被动扫描）           ← 主战场
      │  ├─► Burp/mitmproxy 交叉验证
      │  ├─► Repeater/Fuzzer 手工确认
      │  └─► 导出请求 → 交 sqlmap 深挖
      │
    主动扫描（粗筛 + 覆盖）
      │
      └─► 报告（HTML/JSON）→ 工单/平台
              │
              ▼
   ┌──────────── 专用工具深挖 ───────┐
   sqlmap → SQL 注入自动化           ../03-Web应用/sqlmap.md
   commix → 命令注入                  ../03-Web应用/commix.md
   wpscan → WordPress 专项            ../03-Web应用/wpscan.md
   wcvs   → 缓存投毒/欺骗             ../02-漏洞分析/web-cache-vulnerability-scanner.md
   nikto  → 服务器配置类              ../02-漏洞分析/nikto.md
   nuclei → 模板化快速覆盖            ../02-漏洞分析/nuclei.md
              │
              ▼
        靶场练习：dvwa（基础）→ ZAP（自动化）。../03-Web应用/dvwa.md
```

**几条实用的配合模式**：

| 组合 | 怎么做 |
|------|--------|
| **ZAP ↔ Burp** | 两个都是代理，**别同时开**（端口冲突）。常见分工：Burp 手工、ZAP 自动化；或让 ZAP 走 Burp 代理（反之亦可），用其中一个看流量 |
| **ZAP → sqlmap** | ZAP 的 Active Scan 报 SQL 注入 → 右键该请求 → 复制 → `sqlmap -r request.txt --batch` 深挖（见 [`../03-Web应用/sqlmap.md`](../03-Web应用/sqlmap.md)） |
| **ZAP → commix** | 命令注入同理（见 [`../03-Web应用/commix.md`](../03-Web应用/commix.md)） |
| **ZAP ↔ mitmproxy** | 需要脚本化改写流量时用 mitmproxy（见 [`../07-嗅探与欺骗/mitmproxy.md`](../07-嗅探与欺骗/mitmproxy.md)） |
| **gobuster/ffuf → ZAP** | 先用爆破工具把目录挖出来，再把 URL 塞进 ZAP 的 Sites Tree（或导入清单）→ **大幅提高扫描覆盖面** |
| **ZAP → wcvs** | 缓存类漏洞 ZAP 覆盖很弱，交专门的 WCVS（见 [`web-cache-vulnerability-scanner.md`](../02-漏洞分析/web-cache-vulnerability-scanner.md)） |
| **ZAP + nuclei** | ZAP 管「深度 + 手工」，nuclei 管「广度 + 快速模板」 |

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| 命令跑完不退出 | **没加 `-cmd`**（GUI/daemon 会常驻） | CI/脚本里**必加 `-cmd`** |
| HTTPS 站点全是证书告警 / 页面打不开 | **未信任 ZAP 根 CA** | `-certpubdump /tmp/zap-ca.cer` → 导入浏览器受信任根证书 |
| `-certfulldump` 导出的文件泄露 | 里面**含私钥**，可中间人任意流量 | **只在一次性环境用，用完即删** |
| 主动扫描跑到站外 | **没设 Context/Scope** | 每次测试先设 Include/Exclude；报告里核对 URL 是否越界 |
| 扫描器扫不到功能（覆盖率低） | 目标需要登录；或 SPA 靠 JS 渲染 | **配认证**（Context → Authentication + Users）；**用 AJAX Spider** |
| 主动扫描把目标打挂了 | 默认策略激进；无时间上限 | 用**自定义 Scan Policy**降速；计划里设 `maxScanDurationInMins`；错峰测试 |
| 被 WAF 封 IP | 主动扫描特征明显 | 先与运维协调白名单；降并发；必要时在预发环境测 |
| 端口 8080 被占用 | 与 Burp/其他服务冲突 | `-port 8090`（并在浏览器代理里同步改） |
| 导入 OpenAPI 后扫到了生产 | `-openapitargeturl` 没设 | **必须**用它覆盖成测试环境地址；导入前先看定义里的 server |
| Automation 计划报错 | 计划里 URL/Context 名不匹配；模板名写错 | 先 `-autocheck` 校验；用 `-autogenmax` 看合法取值 |
| 报告模板名不存在 | 模板随插件/版本变化 | GUI 里 Report → 看可选模板名；或用 `-addonlist` 确认报告插件 |
| 每次启动都联网检查更新 | 默认行为 | **加 `-silent`**；`-notel` 关遥测 |
| 内存不足 | 大站点 + 大量 URL | `-lowmem`；给 JVM 更多内存（环境变量/`-config` 调 `-Xmx`） |
| 告警数量巨大无法处理 | 同类问题重复 + 未聚合 | 报告按 **Alert 类型**聚合；设置 `maxAlertsPerRule`；先把 Informational 滤掉 |
| 复测「告警变少」但漏洞还在 | 扫描器适配不上新逻辑 | **手工 Repeater 复现原 payload** 才算验证 |

---

## 9. 防御视角（蓝队 / 开发）

ZAP 是**攻防同源**的工具：它的告警清单**就是防守方的整改清单**。

| ZAP 常见告警 | 蓝队/开发的整改动作 |
|--------------|---------------------|
| Missing Anti-clickjacking Header | 加 `X-Frame-Options: DENY` 或 CSP `frame-ancestors` |
| Cookie No HttpOnly Flag / Without Secure / SameSite | Cookie 加 `HttpOnly; Secure; SameSite=Lax/Strict` |
| X-Content-Type-Options Header Missing | 加 `X-Content-Type-Options: nosniff` |
| Strict-Transport-Security 缺失 | 加 HSTS（先确认全站 HTTPS 就绪） |
| Server Leaks Version Information | 关掉/改写 `Server`、`X-Powered-By` 等头 |
| Absence of Anti-CSRF Tokens | 引入 CSRF token 校验 |
| SQL Injection / XSS / Command Injection | 参数化查询 + 输出编码 + 输入白名单 |
| Path Traversal / File Inclusion | 路径规范化 + 白名单 + 禁止用户控制路径 |
| 备份文件/源码泄露（`.git`、`.bak`、`*.zip`） | 部署流程排除；Web 服务器拒绝访问隐藏/备份文件 |
| 应用报错泄露堆栈 | 生产关闭详细错误；统一错误页 |

**蓝队的五条硬建议**：

1. **把 ZAP 的被动扫描接进 CI**（`-autorun`，只跑 passive）：**零风险**，能拦住大部分「配置类退步」；
2. **主动扫描放预发环境**，并在报告里明确「扫描环境」，避免把测试环境的问题当生产问题；
3. **Alert 必须人工确认**再进工单——尤其是 Active Scan 的启发式结论；
4. **用 `-silent` + `-notel`** 做企业内的合规部署（否则工具本身会外发请求）；
5. **定期用 ZAP 做「差距分析」**：修复前后各扫一次，对比 Alert 集合，验证整改没有漏入口。

**检测「有人在用 ZAP 扫我」**：

| 特征 | 说明 |
|------|------|
| User-Agent 含 `ZAP` | 默认 UA 就是标识（攻击者会改，但初级用户不会） |
| 请求头 `X-ZAP-*` / 特定参数名 | ZAP 的特征注入 |
| 短时间大量参数变体请求 | 主动扫描的指纹 |
| 同一 URL 被注入大量 payload 模式（`'`、`<script>`、`../`） | 主动扫描特征 |
| 来源 IP 的请求序列与 ZAP 的爬取顺序一致 | 高级特征 |

**注意**：护网/攻防演练中，用 ZAP 做授权扫描**必须提前报备**，否则会被蓝队封禁甚至误判为真实攻击。

---

## 10. 参考

- Kali 工具页（含 `zaproxy -h` 完整原文）：<https://www.kali.org/tools/zaproxy/>
- ZAP 官网与文档：<https://www.zaproxy.org/docs/>
- Automation Framework 文档：<https://www.zaproxy.org/docs/automate/automation-framework/>
- 上游仓库：<https://github.com/zaproxy/zaproxy>
- Kali 包跟踪：<https://pkg.kali.org/pkg/zaproxy>
- 本地命令：`zaproxy -h`、`zaproxy -version`、`zaproxy -autogenmin /tmp/plan.yaml`
- 配套教程：[`dvwa.md`](../03-Web应用/dvwa.md)、[`sqlmap.md`](../03-Web应用/sqlmap.md)、[`wpscan.md`](../03-Web应用/wpscan.md)、[`../02-漏洞分析/web-cache-vulnerability-scanner.md`](../02-漏洞分析/web-cache-vulnerability-scanner.md)

## ⚠️ 法律与伦理

ZAP 的**主动扫描会对目标发起大量攻击性请求**（SQL 注入、XSS、命令注入载荷），这与「被动浏览」的法律含义完全不同：

- 《网络安全法》第 27 条：**不得从事非法侵入他人网络、干扰他人网络正常功能、窃取网络数据等危害网络安全的活动**——未经授权的主动扫描即属此类；
- 《刑法》第 285 条（非法获取计算机信息系统数据）、**第 286 条（破坏计算机信息系统）**——主动扫描可能**改变/删除数据、导致服务不可用**（尤其是重放/注入写操作时）；
- 主动扫描会**触发目标 WAF/IDS 告警**，可能被认定为真实攻击，带来法律与业务后果；
- **HTTPS 拦截涉及解密他人通信**：只在你自己的浏览器/设备上信任 ZAP 的 CA；
- 导入 OpenAPI/Postman 定义时，若 `-openapitargeturl` 未正确指向测试环境，可能**直接扫到生产系统**。

**必须遵守**：

1. **只在自建靶场（DVWA 等）或获得书面授权的目标上做主动扫描**；
2. **必须设置 Scope/Context 与 Exclude**，把范围严格限定在授权目标；
3. **主动扫描尽可能放在预发/测试环境**；对生产环境只做**被动扫描**且需授权；
4. **测试前通知运维/蓝队**，约定时间窗与限速要求；
5. **`-certfulldump` 导出的含私钥证书在使用后立即删除**，不得留存或传播；
6. **报告脱敏**：不公开可直接利用的 payload、内部 URL、数据片段；
7. 发现的漏洞通过**负责任的披露流程**上报，不擅自利用、不扩大影响。
