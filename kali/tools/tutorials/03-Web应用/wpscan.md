# wpscan（WordPress 黑盒漏洞扫描）

> **一句话**：针对 WordPress 站点做专项扫描——识别版本、枚举插件/主题/用户、匹配已知漏洞、甚至做口令爆破。
> **分类**：Web 应用 ｜ **Kali 包**：`wpscan` ｜ **官方文档**：<https://wpscan.com/wordpress-security-scanner>

## 1. 它解决什么问题

WordPress 承载了互联网上很大比例的网站，而它的**攻击面极其集中**：

- **核心版本**：旧版核心有大量已知漏洞。
- **插件**：这是真正的重灾区——**绝大多数 WP 漏洞来自插件**，而一个站点往往装了几十个。
- **主题**：同理。
- **用户枚举**：`/?author=1`、REST API、登录页报错都能泄露用户名，为口令爆破提供输入。
- **配置文件备份**：`wp-config.php~`、`wp-config.php.bak` 里通常有数据库凭据。
- **XML-RPC**：`xmlrpc.php` 的 `system.multicall` 允许**一次请求尝试几百个口令**，绕过登录限速。

通用扫描器（[nikto](../02-漏洞分析/nikto.md)、[nuclei](../02-漏洞分析/nuclei.md)）要么太泛，要么需要你自己写模板。wpscan 是**为 WordPress 定制的**，它知道该看哪些文件、哪些端点、哪些版本号在哪。

| 工具 | 定位 |
|------|------|
| **wpscan** | WordPress 专项：指纹 + 枚举 + 漏洞匹配 + 口令爆破 |
| [whatweb](../01-信息搜集/whatweb.md) | 判断"是不是 WordPress"（wpscan 的前置步骤） |
| [nuclei](../02-漏洞分析/nuclei.md) | 用通用模板做补充检测 |
| [searchsploit](../02-漏洞分析/searchsploit.md) | 拿到插件版本后查 EXP |
| [gobuster](gobuster.md) / [ffuf](ffuf.md) | 目录爆破（WPScan 的枚举是"语义化"的，dirb 类工具是"字典化"的，互补） |

**关键点**：wpscan 的漏洞数据来自 **WPScan 漏洞数据库**（WPScan Vulnerability Database）。免费使用有**每日 API 请求数限制**，需要到 <https://wpscan.com/> 注册免费 API token 才能真正用起来。

## 2. 工作原理

```text
   wpscan --url https://target --enumerate vp,vt,u
        │
   ┌────┴────────────────────────────────────────────────────────────┐
   │ ① 确认目标是 WordPress（--force 可跳过）                          │
   │    检查 /wp-login.php、/wp-admin/、meta generator 等特征         │
   └────┬────────────────────────────────────────────────────────────┘
        │
   ┌────┴────────────────────────────────────────────────────────────┐
   │ ② 探测模式（--detection-mode，默认 mixed）                        │
   │    passive   : 只被动分析已经拿到的响应（不额外发包，最安静）      │
   │    aggressive: 主动请求已知路径来判断（最准，也最吵）             │
   │    mixed     : 先用被动，不确定时再主动（默认）                    │
   │    → --stealthy 是"random UA + 全部 passive"的别名               │
   └────┬────────────────────────────────────────────────────────────┘
        │
   ┌────┴────────────────────────────────────────────────────────────┐
   │ ③ 版本与指纹识别                                                  │
   │    WordPress 核心版本：读 RSS/readme/meta/静态资源版本号           │
   │    主题、插件、timthumb、配置文件备份、DB 导出文件                 │
   │    用户枚举：/?author=N、REST API /wp-json/wp/v2/users、登录报错   │
   └────┬────────────────────────────────────────────────────────────┘
        │
   ┌────┴────────────────────────────────────────────────────────────┐
   │ ④ 漏洞匹配：把发现的核心/插件/主题版本 与 WPScan 漏洞库比对        │
   │    需要 API token（--api-token）；免费额度有每日上限              │
   │    输出含 CVE、标题、修复版本、参考链接                            │
   └────┬────────────────────────────────────────────────────────────┘
        │
   ┌────┴────────────────────────────────────────────────────────────┐
   │ ⑤（可选）口令攻击                                                  │
   │    -P <密码字典> -U <用户名>                                     │
   │    自动选择攻击方式（--password-attack 可强制）：                  │
   │      wp-login          : 传统登录表单                            │
   │      xmlrpc            : XML-RPC 单次调用                        │
   │      xmlrpc-multicall  : **一次请求批量尝试**（--multicall-max-   │
   │                          passwords 默认 500），最难被限速拦住      │
   └────────────────────────────────────────────────────────────────────┘
```

几个关键机制：

- **枚举选项 `-e` 是可以组合的**：`-e vp,vt,u` = 只枚举"有漏洞的插件"+"有漏洞的主题"+"用户"。**不要裸跑 `-e ap,at`**（所有插件+所有主题）——那会发上万次请求。
- **`--plugins-detection` 默认是 `passive`**，比全局的 `mixed` 更保守。想更准可以设 `aggressive`。
- **XML-RPC multicall 是 wpscan 的特色能力**：`system.multicall` 允许一次请求里塞多个方法调用，所以**一次 HTTP 请求就能试 500 个口令**（默认值），这让基于"请求频率"的登录限速几乎失效。**这是防守方必须知道的一个点。**
- **`--stealthy`** = `--random-user-agent --detection-mode passive --plugins-version-detection passive`——完全不主动探测的配置。

## 3. 安装与快速上手

```bash
sudo apt install wpscan
wpscan --version
wpscan --hh | head -60      # 完整帮助
```

最小可用命令：

```bash
# 1) 最基础的扫描
wpscan --url http://192.168.56.101/wordpress

# 2) 枚举有漏洞的插件、主题和用户
wpscan --url http://192.168.56.101/wordpress --enumerate vp,vt,u

# 3) 带上 API token（能拿到漏洞详情）
wpscan --url https://target --api-token YOUR_TOKEN --enumerate vp
```

> 首次使用建议先到 <https://wpscan.com/> 注册免费账号拿 API token，否则很多漏洞信息拿不到。

## 4. 核心参数详解

### 基础

| 参数 | 作用 | 建议 |
|------|------|------|
| `--url <URL>` | 目标 URL。支持 http/https，未写协议默认 http。**除 `update`/`help`/`hh`/`version` 外必填** | — |
| `-h, --help` | 简要帮助 | — |
| `--hh` | **完整帮助**（选项非常多，进阶参数都在这里） | — |
| `--version` | 版本 | — |
| `-v, --verbose` | 详细模式 | 排障 |
| `--[no-]banner` | 是否显示 banner（默认显示） | 脚本化时 `--no-banner` |
| `-o, --output <FILE>` | 输出到文件 | — |
| `-f, --format <FMT>` | 输出格式：`cli`、`cli-no-colour`、`cli-no-color`、`json` | **`json` 用于流水线** |

### 请求与连接

| 参数 | 作用 | 建议 |
|------|------|------|
| `--detection-mode <mixed\|passive\|aggressive>` | 探测模式（默认 mixed） | 生产环境用 `passive` |
| `--user-agent <UA>` / `--ua <UA>` | 自定义 UA | — |
| `--random-user-agent` / `--rua` | 每次扫描随机 UA | 规避简单过滤 |
| `--http-auth <login:password>` | HTTP Basic 认证 | — |
| `-t, --max-threads <n>` | 最大线程数（默认 5） | 别调太高 |
| `--throttle <毫秒>` | 两次 Web 请求之间的等待毫秒数；**设了之后 max threads 会被强制为 1** | **限速关键参数** |
| `--request-timeout <秒>` | 请求超时（默认 60） | — |
| `--connect-timeout <秒>` | 连接超时（默认 30） | — |
| `--disable-tls-checks` | 关闭 TLS 证书校验 | 自签证书场景 |
| `--proxy <protocol://IP:port>` | 代理（支持协议取决于 cURL 编译选项） | 配 Burp |
| `--proxy-auth <login:password>` | 代理认证 | — |
| `--cookie-string <COOKIE>` | 请求携带的 Cookie，格式 `k1=v1[; k2=v2]` | 需要登录态时 |
| `--cookie-jar <FILE>` | Cookie 读写文件（默认 `/tmp/wpscan/cookie_jar.txt`） | — |

### 目标识别与更新

| 参数 | 作用 | 建议 |
|------|------|------|
| `--force` | **不检查目标是否运行 WordPress**，强制扫描 | 目标隐藏了 WP 特征时用 |
| `--[no-]update` | 是否更新漏洞数据库 | 建议先 `--update` |
| `--api-token <TOKEN>` | WPScan API token | **强烈建议配置**（免费额度有限） |
| `--wp-content-dir <DIR>` | 自定义 wp-content 目录 | 非标准安装 |
| `--wp-plugins-dir <DIR>` | 自定义插件目录 | — |

### 枚举 `-e, --enumerate`

**可用取值**：

| 值 | 含义 | 说明 |
|----|------|------|
| `vp` | **有漏洞的插件** | 最常用，噪声最小 |
| `ap` | 所有插件 | **请求量巨大** |
| `p` | 插件（= popular plugins，需注意版本差异） | — |
| `vt` | **有漏洞的主题** | 常用 |
| `at` | 所有主题 | 请求量大 |
| `t` | 主题 | — |
| `tt` | Timthumb 文件 | 旧版主题常见的缩略图库漏洞点 |
| `cb` | **配置备份文件**（`wp-config.php.bak` 之类） | **收益高** |
| `dbe` | 数据库导出文件 | 常有 `.sql` 泄露 |
| `u` | **用户 ID 范围**（如 `u1-5`，分隔符 `-`，不带参数默认 `1-10`） | **为口令爆破提供用户名** |
| `m` | 媒体 ID 范围（如 `m1-15`，默认 `1-100`） | **注意：需要固定链接设置为 "Plain" 才能检测到** |

**规则**：
- 多个值用 `,` 分隔。
- **默认值**：`All Plugins, Config Backups`（即 `ap,cb`）——**注意这个默认很"重"**。
- **无参数时**的默认值：`vp,vt,tt,cb,dbe,u,m`。
- **互斥组**（每组只能选一个）：`vp, ap, p` 与 `vt, at, t`。

| 相关参数 | 作用 | 建议 |
|----------|------|------|
| `--exclude-content-based <REGEXP_OR_STRING>` | 排除匹配该正则的响应（大小写不敏感，同时检查头和体；**正则定界符不需要写**） | 排除统一错误页 |
| `--plugins-detection <MODE>` | 插件枚举用这个模式，而非全局 `--detection-mode`（默认 `passive`） | 想更准设 `aggressive` |
| `--plugins-version-detection <MODE>` | 插件版本检测用这个模式（默认 `mixed`） | — |

### 口令攻击

| 参数 | 作用 | 建议 |
|------|------|------|
| `-P, --passwords <FILE>` | 口令字典文件。**若未提供 `-U`，会自动先做用户枚举** | — |
| `-U, --usernames <LIST>` | 用户名列表：`'a1'`、`'a1,a2,a3'`、`'/tmp/a.txt'` | 先用 `-e u` 拿到 |
| `--multicall-max-passwords <N>` | XML-RPC multicall 每次请求最多带多少口令（默认 500） | — |
| `--password-attack <ATTACK>` | 强制指定攻击方式：`wp-login` / `xmlrpc` / `xmlrpc-multicall` | 默认自动选择 |

### 便捷开关

| 参数 | 等价于 |
|------|--------|
| `--stealthy` | `--random-user-agent --detection-mode passive --plugins-version-detection passive` |

> 更多选项（如 `--exclude-content-based` 之外的进阶项、`--wp-content-dir` 相关、`--plugins-version-all` 等）用 **`wpscan --hh`** 查看完整列表。

## 5. 实战演练

**环境**：本地实验环境。

- 在实验虚拟机上用 Docker 起一个 WordPress（**故意装一个旧版插件**用于演示）：

```bash
docker run -d --name wp -p 8081:80 wordpress:6.0-php7.4-apache
# 完成安装向导后，手工安装一个已知有漏洞的旧版插件，例如：
#   wget https://downloads.wordpress.org/plugin/contact-form-7.5.3.1.zip
#   在后台"插件 → 上传插件"里安装（不要升级）
```

- 攻击机 Kali：`192.168.56.10`

> ⚠️ wpscan 的枚举与口令攻击会向目标发大量请求。**只对授权目标使用**；口令爆破在生产环境属于高危操作，必须先取得书面授权并确认没有账号锁定策略。

### 场景 1：基础扫描 + 用户枚举

```bash
wpscan --url http://192.168.56.101:8081 \
       --enumerate vp,vt,u \
       --api-token YOUR_TOKEN \
       -o wpscan_out.txt -f cli-no-color
```

预期输出片段：

```text
_______________________________________________________________
        __          _______   _____
        \ \        / /  __ \ / ____|
         \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
          \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
           \  /\  /  | |     ____) | (__| (_| | | | |
            \/  \/   |_|    |_____/ \___|\__,_|_| |_|

        WordPress Security Scanner by the WPScan Team
                       Version 3.8.25

       @_WPScan_, @ethicalhack3r, @erwan_lr, @_FireFart_
_______________________________________________________________

[i] Updating the Database ...
[i] Update completed.

[+] URL: http://192.168.56.101:8081/
[+] Started: Tue Sep 15 18:30:00 2026

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.54 (Debian)
 | Found By: Headers (Passive Detection)

[+] XML-RPC seems to be enabled: http://192.168.56.101:8081/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/

[+] WordPress readme found: http://192.168.56.101:8081/readme.html

[+] Upload directory has listing enabled: http://192.168.56.101:8081/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://192.168.56.101:8081/wp-cron.php

[+] WordPress version 6.0 identified (Outdated, released on 2022-05-24).
 | Found By: Rss Generator (Passive Detection)
 |  - http://192.168.56.101:8081/feed/, <generator>https://wordpress.org/?v=6.0</generator>
 |  - http://192.168.56.101:8081/, <generator>https://wordpress.org/?v=6.0</generator>

[+] WordPress theme in use: twentytwentytwo
...

[+] Enumerating Vulnerable Plugins (via Passive Methods)
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] contact-form-7
 | Location: http://192.168.56.101:8081/wp-content/plugins/contact-form-7/
 | Latest Version: 5.8.5 (up to date)
 | The version could not be determined
...
```

解读（**输出里每一段都值得看**）：

| 发现 | 含义 | 风险 |
|------|------|------|
| `Server: Apache/2.4.54` | 服务器版本暴露 | 低（信息泄露） |
| `XML-RPC seems to be enabled` | **`xmlrpc.php` 可访问** | **中高**：可用于 `system.multicall` 批量爆破，也可用于 pingback SSRF/DoS |
| `readme.html found` | 默认文件存在 | 低（会泄露版本） |
| `Upload directory has listing enabled` | **`wp-content/uploads/` 目录列表开启** | **中**：可枚举所有上传文件 |
| `WP-Cron seems to be enabled` | `wp-cron.php` 外部可访问 | 低（可被滥用作 DoS 放大器） |
| `WordPress version 6.0 identified (Outdated)` | **核心版本过期** | **高**：查该版本的已知 CVE |
| `Plugin(s) Identified` | 插件与版本 | **高价值**：拿去匹配漏洞库 |

### 场景 2：只枚举高价值项（实战推荐配置）

```bash
wpscan --url http://192.168.56.101:8081 \
       --enumerate vp,vt,cb,dbe,u1-20 \
       --plugins-detection aggressive \
       --api-token YOUR_TOKEN \
       --throttle 200 \
       --random-user-agent \
       -o wpscan_full.txt -f json
```

解读：这是"信息量/噪声"比最好的一组配置：
- `vp,vt` 只找**有漏洞的**插件和主题（而不是把所有插件列一遍），大幅减少请求。
- `cb,dbe` 找**配置备份和数据库导出**——一旦命中就是数据库凭据泄露。
- `u1-20` 枚举前 20 个用户 ID（用于后续口令攻击）。**WP 的用户 ID 通常是连续的**，所以小范围就够。
- `--plugins-detection aggressive` 让插件版本识别更准（代价是更多请求）。
- `--throttle 200`（每请求间隔 200ms，且线程数被强制为 1）+ `--random-user-agent` 是温和模式。
- `-f json` 让结果可被 `jq` 处理。

**用 `jq` 提取关键信息**：

```bash
jq -r '.plugins | to_entries[] | "\(.key) \(.value.version.number // "unknown")"' wpscan_full.txt
jq -r '.version.number' wpscan_full.txt
jq -r '.users | to_entries[] | "\(.key) \(.value)"' wpscan_full.txt
```

### 场景 3：口令攻击（授权演练）

```bash
# 第一步：先枚举用户
wpscan --url http://192.168.56.101:8081 -e u1-10 --api-token YOUR_TOKEN

# 第二步：对已知用户做口令攻击
wpscan --url http://192.168.56.101:8081 \
       -U admin \
       -P /usr/share/wordlists/rockyou.txt \
       --password-attack xmlrpc-multicall \
       --multicall-max-passwords 500 \
       --throttle 500 \
       --api-token YOUR_TOKEN
```

预期输出片段：

```text
[+] Performing password attack on Xmlrpc Multicall against 1 user/s
[SUCCESS] - admin / password123
[+] Valid Combinations Found:
 | Username: admin, Password: password123
```

解读：
- `--password-attack xmlrpc-multicall` 用 XML-RPC 的 `system.multicall`，**一次请求带 500 个口令**。这就是它比传统登录爆破高效得多的原因，也是**防守方必须关闭 XML-RPC 的理由**。
- `--throttle 500` 大幅放慢，减少对目标的影响，也是授权演练的基本要求。
- 拿到有效凭据后，可以直接登录后台 → 上传恶意插件/主题 → 拿到 RCE。

**如果目标关闭了 XML-RPC**，退回到 `wp-login`：

```bash
wpscan --url http://target -U admin -P passwords.txt --password-attack wp-login
```

**注意**：WordPress 官方有登录失败限速插件，也可能有 WAF。`wp-login` 方式很容易被拦住或触发账号锁定。

### 场景 4：隐身模式 + 代理观察

```bash
# --stealthy 等价于 --random-user-agent --detection-mode passive --plugins-version-detection passive
wpscan --url https://target --stealthy --api-token YOUR_TOKEN

# 走 Burp 代理，观察 wpscan 发的每个请求
wpscan --url http://192.168.56.101:8081 --enumerate vp,u \
       --proxy http://127.0.0.1:8080 --disable-tls-checks
```

解读：
- **`--stealthy` 不主动探测**——所有判断都基于"已经拿到的响应"。这最安静，但识别率也最低（拿不到版本的插件就报不出来）。
- 走 Burp 代理能**看到 wpscan 到底请求了哪些路径**，这对理解它的工作原理、以及评估"这次扫描有多吵"很有用。

### 场景 5：处理非标准安装 + 强制扫描

```bash
# 目标把 wp-content 改了名，或者用了自定义插件目录
wpscan --url http://target/blog \
       --wp-content-dir assets --wp-plugins-dir ext \
       --enumerate vp,u

# 目标隐藏了 WordPress 特征（比如改了 meta generator），强制扫描
wpscan --url http://target --force --enumerate vp,vt,cb,dbe,u

# 需要登录态的扫描
wpscan --url http://target \
       --cookie-string "wordpress_logged_in_xxx=abc123; wp-settings-1=xyz" \
       --enumerate ap
```

解读：
- `--wp-content-dir` / `--wp-plugins-dir` 用于**做过安全加固（目录改名）**的站点。
- `--force` 跳过"是不是 WordPress"的检查——当目标隐藏了特征但你确定它是 WP 时使用。
- 带 Cookie 扫描能在**登录态下枚举更多内容**（例如已安装插件的完整列表）。

## 6. 输出解读

### 输出结构

| 区块 | 内容 |
|------|------|
| `Interesting Finding(s)` | 逐条列出：服务器头、XML-RPC、readme、目录列表、WP-Cron、版本、主题等 |
| `[+] WordPress version X identified` | 核心版本（含 `Outdated` 标记与发布日期） |
| `[+] WordPress theme in use` | 当前主题与版本 |
| `[+] Enumerating Vulnerable Plugins` | 有漏洞的插件 |
| `[+] Enumerating Vulnerable Themes` | 有漏洞的主题 |
| `[+] Enumerating Config Backups` | 配置文件备份 |
| `[+] Enumerating DB Exports` | 数据库导出 |
| `[+] Enumerating Users` | 用户列表 |
| `[SUCCESS] - user / pass` | 口令攻击成功 |
| `Finished` | 结束（含耗时、请求数等统计） |

### 每条发现的字段

| 字段 | 含义 |
|------|------|
| `Found By: Headers (Passive Detection)` | 通过响应头被动发现 |
| `Found By: Rss Generator (Passive Detection)` | 通过 RSS 的 generator 标签发现 |
| `Found By: Direct Access (Aggressive Detection)` | 通过主动请求该路径发现 |
| `Confidence: 100%` | 置信度 |
| `References:` | 相关文档/漏洞参考链接 |

### 枚举结果的用法

| 结果 | 后续动作 |
|------|---------|
| 核心版本 + `Outdated` | `searchsploit wordpress <版本>`；查 WordPress 官方 CVE |
| 插件 + 版本 | `searchsploit <plugin> <版本>`；到 WPScan 漏洞库查 |
| 主题 + 版本 | 同上（主题也常有文件上传/包含漏洞） |
| `cb`/`dbe` 命中 | **立即下载并检查**（可能含数据库凭据） |
| 用户列表 | 口令攻击的输入；也可用于社工 |

### 判断要点

1. **`Outdated` 只是"版本旧"，不等于"有可利用漏洞"**——但值得逐条查。
2. **插件的命中率远高于核心**：如果扫描只报"核心过期"，收益有限；报出插件版本才真正有价值。
3. **`The version could not be determined`** 很常见——插件作者常去掉版本号。此时可以尝试 `--plugins-detection aggressive`，或手工看该插件的 `readme.txt`。
4. **`XML-RPC seems to be enabled` 是最值得关注的非漏洞发现**——它本身不是漏洞，但它把"口令爆破"的成本降到极低。

## 7. 与其他工具配合

```bash
# 1) whatweb 判断是不是 WordPress -> wpscan
whatweb -a 1 http://192.168.56.101:8081 | grep -qi wordpress && \
  wpscan --url http://192.168.56.101:8081 --enumerate vp,vt,u --api-token $WPS_TOKEN

# 2) wpscan JSON -> 提取插件版本 -> searchsploit
wpscan --url http://target --enumerate vp --api-token $WPS_TOKEN -f json -o wp.json --no-banner
jq -r '.plugins | to_entries[] | "\(.key) \(.value.version.number // "")"' wp.json | while read -r name ver; do
  echo "=== $name $ver ==="; searchsploit "$name $ver" | head -5
done

# 3) wpscan 用户列表 -> 口令喷洒（授权内）
jq -r '.users | keys[]' wp.json > wp_users.txt
# hydra -L wp_users.txt -p 'Password123' -s 8081 192.168.56.101 http-post-form \
#   "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:ERROR"

# 4) gobuster 补充字典化枚举（wpscan 是语义化枚举，互补）
gobuster dir -u http://target/wp-content/plugins/ \
  -w /usr/share/seclists/Discovery/Web-Content/CMS/wp-plugins.fuzz.txt

# 5) nuclei 用 WordPress 相关模板补充
nuclei -u http://target -tags wordpress -severity medium,high,critical -silent

# 6) 结果做成可跟踪的报告
wpscan --url http://target --enumerate vp,vt,cb,dbe,u --api-token $WPS_TOKEN \
       -f json -o "wp_$(date +%F).json" --no-banner --disable-tls-checks
# 下周再跑一次，diff 找新增暴露
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `The remote website is up, but does not seem to be running WordPress.` | 目标隐藏了 WP 特征，或不是 WP | 确认 URL 路径（很多站点在子目录）；确认后加 `--force` |
| 漏洞信息全是"版本未知"或没有 CVE | 未配置 API token 或超出免费额度 | 到 wpscan.com 注册并 `--api-token <token>` |
| 扫描到一半大量超时 | 默认 5 线程 + 60s 请求超时 | `-t 3`、`--request-timeout 30`；加 `--throttle 300` |
| 被 WAF 拦截（大量 403/429） | 请求过快 | `--throttle 500`、`--random-user-agent`、`--stealthy`；或走代理 |
| 扫描非常慢 | 用了 `-e ap,at`（所有插件+主题） | 改用 `-e vp,vt`（只找有漏洞的） |
| 插件版本识别不出 | 插件作者去掉了版本号；默认 passive 模式识别有限 | `--plugins-detection aggressive`；或手工读该插件的 `readme.txt` |
| 用户枚举为空 | 目标禁用了 `?author=` 和 REST API 用户端点 | 试 `--enumerate u1-20`；或用 [gobuster](gobuster.md) 从登录页报错枚举 |
| `m` 媒体枚举无结果 | **需要固定链接设置为 "Plain"** | 这是已知限制，改用其他枚举项 |
| 口令攻击被拦/无效 | 有登录限速/WAF；XML-RPC 被关 | `--password-attack wp-login`；或用 `--throttle` 放慢 |
| TLS 证书错误 | 自签证书 | `--disable-tls-checks` |
| 结果文件是彩色转义符 | 默认带颜色 | `-f cli-no-color`（或 `cli-no-colour`） |
| 需要更新漏洞库 | 数据过期 | `wpscan --update` |
| 输出太长难以分析 | 默认输出信息量大 | `-f json` 后用 `jq` 提取 |

## 9. 防御视角（蓝队）

WordPress 的加固项**非常明确**，这一节可以直接当检查清单用。

### 加固清单（按优先级）

| 优先级 | 措施 | 说明 |
|--------|------|------|
| **最高** | **关闭 XML-RPC** | 直接废掉 `xmlrpc-multicall` 批量爆破与 pingback 滥用。可在 Nginx/Apache 层拦截 `/xmlrpc.php`，或用插件禁用 |
| **最高** | **及时更新核心、主题、插件** | 绝大多数 WP 漏洞来自未更新的插件。**自动更新要开** |
| **最高** | **删除不用的主题和插件** | 未启用的插件（尤其是旧版）仍然是攻击面——**它们照样能被请求到** |
| 高 | **强口令 + 双因素认证（2FA）** | 口令爆破的第一道防线；2FA 基本让爆破失效 |
| 高 | **登录失败限速与账户锁定** | 降低爆破可行性（对 `wp-login` 有效；对 `xmlrpc-multicall` 效果有限，因为它是批量请求） |
| 高 | **禁用目录列表** | `wp-content/uploads/` 的 `Options -Indexes`；否则攻击者能枚举所有上传文件 |
| 中 | **删除 `readme.html`、`license.txt`** | 减少版本信息泄露 |
| 中 | **修改默认用户名** | 不要用 `admin`；`-e u` 能枚举出真实用户名，但至少减少"默认用户+弱口令"的组合 |
| 中 | **保护 `wp-config.php`** | 禁止通过 Web 访问；检查目录下没有 `.bak`/`.old`/`.txt` 备份 |
| 中 | **禁用文件编辑** | `wp-config.php` 里设 `define('DISALLOW_FILE_EDIT', true);`，避免后台直接改 PHP 拿 RCE |
| 中 | **限制 `wp-cron.php` 外部访问** | 防止被当作 DoS 放大器 |
| 中 | **WAF** | 拦截常见 WP 攻击路径与爆破特征 |
| 中 | **及时清理未使用的上传文件与旧备份** | 减少 `cb`/`dbe` 枚举的收益 |
| 低 | 隐藏 WP 特征（改路径、去版本号） | 只提高成本，不解决根本问题；`--force` 仍可扫描 |

### 可检测的扫描行为

| wpscan 行为 | 检测特征 |
|------------|---------|
| 版本与指纹识别 | 访问 `/readme.html`、`/feed/`、`/?ver=` 等；**UA 默认是 `WPScan v3.8.x (https://wpscan.com/wordpress-security-scanner)`** |
| 插件枚举 | 对 `/wp-content/plugins/<大量插件名>/` 的密集请求（`--plugins-detection aggressive` 时更明显） |
| 主题枚举 | 同上，`/wp-content/themes/<主题名>/` |
| 配置备份枚举 | 请求 `wp-config.php.bak`、`wp-config.php~`、`.save` 等**特定后缀** |
| 数据库导出枚举 | 请求 `*.sql` 路径 |
| 用户枚举 | 请求 `/?author=1`、`/?author=2`… 或 REST API `/wp-json/wp/v2/users` |
| XML-RPC 探测 | `POST /xmlrpc.php` 带 `system.listMethods` |
| **multicall 爆破** | **单个 `POST /xmlrpc.php` 请求体很大（含 500 个口令）**——这是很独特的特征，请求体大小异常 |
| `--stealthy` | 只有被动分析，**几乎无法从流量上检测**（除了 UA） |

### 检测规则建议

```text
- UA 匹配 (?i)wpscan
- 单源 IP 60s 内对 /wp-content/plugins/ 的请求数 > 50（插件枚举）
- 请求 /?author= 且 author 参数为连续数字
- 请求路径匹配 (wp-config\.php(\.(bak|old|save|txt|zip))?|\.sql$|\.env)
- POST /xmlrpc.php 且 Content-Length > 100000（multicall 批量爆破）
- POST /xmlrpc.php 且请求体含 system.multicall（**高置信度**）
```

**`system.multicall` 是最值得做的一条规则**——正常业务几乎不会用到它，而它正是批量爆破的核心。

### 蓝队自查

```bash
# 用 wpscan 自己扫自己（授权范围内，配置低强度参数）
wpscan --url https://my-site.example \
       --enumerate vp,vt,cb,dbe,u1-10 \
       --api-token $WPS_TOKEN \
       --throttle 500 \
       --stealthy
```

把结果中的 `vp`/`vt` 命中项做成一览表，逐条打补丁——这是 WordPress 站点最有效的漏洞管理方式。

## 10. 参考

- 官方站点与漏洞库：<https://wpscan.com/>
- 官方仓库：<https://github.com/wpscanteam/wpscan>
- Kali 工具页：<https://www.kali.org/tools/wpscan/>
- WordPress 官方加固指南：<https://developer.wordpress.org/advanced-administration/security/hardening/>
- man page：`man wpscan`（覆盖主要选项）；**完整选项用 `wpscan --hh`**
- 用法核实：本教程参数取自 Debian 包 `wpscan 4.1.0` 的 man page（含枚举取值、互斥组、默认值等细节）

---

**相关教程**：[sqlmap](sqlmap.md) ｜ [commix](commix.md) ｜ [gobuster](gobuster.md) ｜ [ffuf](ffuf.md) ｜ [wafw00f](wafw00f.md) ｜ [whatweb](../01-信息搜集/whatweb.md) ｜ [searchsploit](../02-漏洞分析/searchsploit.md) ｜ [nuclei](../02-漏洞分析/nuclei.md)
