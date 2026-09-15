# 03 · Web 应用（Web Application）工具教程

Web 应用是本仓库中**最贴近实战**的一类目标：不需要拿到 shell，一个 URL 就可能直接通向数据库或服务器。

本目录收录 8 个 Kali 官方工具，覆盖 Web 测试的四条主线：**指纹与防护识别 → 内容发现 → 漏洞检测与利用 → CMS 专项**。

## 工具清单

| 工具 | 一句话 | 难度 | 教程 |
|------|--------|------|------|
| `sqlmap` | 自动化 SQL 注入检测与利用，从检测到拖库一站式 | ★★★ | [sqlmap.md](sqlmap.md) |
| `gobuster` | 目录/DNS/虚拟主机/对象存储爆破，模式最全 | ★★☆ | [gobuster.md](gobuster.md) |
| `ffuf` | 最快的 Web fuzzer，`FUZZ` 关键字可放任意位置 | ★★★ | [ffuf.md](ffuf.md) |
| `dirb` | 经典目录爆破，零配置、默认递归 | ★☆☆ | [dirb.md](dirb.md) |
| `wfuzz` | 载荷类型丰富，过滤器是表达式，有插件体系 | ★★☆ | [wfuzz.md](wfuzz.md) |
| `commix` | 自动化 OS 命令注入检测与利用 | ★★★ | [commix.md](commix.md) |
| `wpscan` | WordPress 黑盒专项扫描：版本/插件/用户/口令 | ★★☆ | [wpscan.md](wpscan.md) |
| `wafw00f` | WAF 指纹识别，动手前先搞清楚"守卫是谁" | ★☆☆ | [wafw00f.md](wafw00f.md) |

难度说明：★☆☆ 上手即可用；★★☆ 需要理解参数与场景；★★★ 需要理解框架/协议模型或涉及高危利用。

## 学习顺序建议

### 第一步：先学会"看"（★☆☆）

1. **[wafw00f](wafw00f.md)** —— 只发 7~12 个请求就能判断防护情况。**每次 Web 测试的第一步都应该是它。**
2. **[dirb](dirb.md)** —— 零配置的目录爆破。用它建立"网站里有什么"的直觉，同时理解什么是"软 404"。

### 第二步：把内容发现做精（★★☆）

3. **[gobuster](gobuster.md)** —— 学参数化的爆破：状态码白黑名单、扩展名、`--discover-backup`、递归、vhost 模式。
4. **[ffuf](ffuf.md)** —— **重点学 matcher/filter 体系**和 `-ac` 自动校准。这是从"跑一遍脚本"到"能精准控制结果"的关键一步。
5. **[wfuzz](wfuzz.md)** —— 对比 ffuf，理解 `-z` 载荷类型（`range`/`list`/`permutation`）和 `--hc BBB` 基线机制的价值。

### 第三步：漏洞检测与利用（★★★）

6. **[sqlmap](sqlmap.md)** —— **本目录最重的工具**。重点：`-p` 提速、`--level`/`--risk` 的取舍、`--technique` 选择、`-r` 读原始请求、`--dump` 系列。
7. **[commix](commix.md)** —— 与 sqlmap 同构（都是"检测 4 种技术 + 利用"），对照学习能更快理解这类工具的设计。
8. **[wpscan](wpscan.md)** —— 从通用工具转向专项工具。理解"语义化枚举"（知道该看哪些端点）比"字典化枚举"高效在哪。

## 常见工作流

### 工作流一：Web 目标标准流程

```text
wafw00f              —— 有没有 WAF？是哪家？（决定后续策略与限速）
        ↓
whatweb（01-信息搜集）—— 什么技术栈？
        ↓
dirb -r 摸底          —— 快速看一层
        ↓
gobuster / ffuf 全量   —— 大字典 + 扩展名 + 备份文件发现
        ↓
对发现的 .php/.aspx    —— sqlmap / commix 测注入
        ↓
nuclei（02-漏洞分析）  —— 用模板做精确验证
```

### 工作流二：WordPress 专项

```text
whatweb | grep -i wordpress      —— 确认是 WP
        ↓
wpscan --enumerate vp,vt,cb,dbe,u1-20
        ↓
插件版本 → searchsploit / WPScan 漏洞库
        ↓
用户列表 → wpscan 口令攻击（授权内）或分析用户名规律
        ↓
cb/dbe 命中 → 下载配置文件备份 → 数据库凭据
```

### 工作流三：参数 fuzz 三件套

```text
ffuf  -mc all -ac -u "http://t/page.php?FUZZ=1"   —— 找参数名
        ↓
wfuzz -z range,1-1000 --hc BBB "…?id=FUZZ"        —— 枚举参数值
        ↓
sqlmap -p id --level 3 --risk 1                    —— 验证注入
        ↓
commix -p id                                       —— 验证命令注入
```

### 工作流四：vhost 与隐藏资产

```text
gobuster vhost --append-domain -u http://IP   —— 发现 Host 头路由的站点
        ↓
子站点逐个 whatweb / gobuster dir
        ↓
对比默认站点，找出"不该存在"的入口
```

## 工具选择速查

| 我想…… | 用 |
|--------|----|
| 快速看网站有哪些目录 | [dirb](dirb.md) |
| 控制状态码/扩展名/备份文件 | [gobuster](gobuster.md) |
| 把字典/载荷放到请求头、Cookie、JSON 体里 | [ffuf](ffuf.md) 或 [wfuzz](wfuzz.md) |
| 不写字典，直接枚举数字或用内联列表 | [wfuzz](wfuzz.md) |
| 对发现的参数做注入验证 | [sqlmap](sqlmap.md)（SQL）/ [commix](commix.md)（命令） |
| 扫 WordPress | [wpscan](wpscan.md) |
| 知道前面有没有 WAF | [wafw00f](wafw00f.md) |
| 大范围扫描且需要限速 | [ffuf](ffuf.md) `-rate` / [gobuster](gobuster.md) `-d` / [wpscan](wpscan.md) `--throttle` |

## 最小化靶场环境

```bash
# DVWA（SQL 注入 / 命令注入 / 文件包含等经典漏洞）
docker run -d -p 8080:80 vulnerables/web-dvwa

# OWASP Juice Shop（现代 SPA，典型的软 404 场景）
docker run -d -p 3000:3000 bkimminich/juice-shop

# WordPress（配合 wpscan 练习）
docker run -d -p 8081:80 wordpress

# ModSecurity + OWASP CRS（练 wafw00f 与绕过）
docker run -d -p 8082:80 owasp/modsecurity-crs:nginx

# Metasploitable2（内置 Mutillidae、DVWA、phpMyAdmin、WebDAV）
# 用虚拟机导入即可
```

## 法律与授权提醒

Web 应用测试是**最容易越界**的一类操作：

- **注入测试会修改或读取目标数据**。SQL 注入的 `--dump` 会拉取真实数据；命令注入的 `--file-write` 会往服务器写文件。**没有书面授权绝不要做。**
- **口令爆破（wpscan `-P`）会对账号造成实际影响**（触发锁定、产生大量失败登录日志）。必须先确认有无锁定策略，并用 `--throttle` 大幅限速。
- **工具的"只读"要仔细确认**：
  - `wafw00f` 会发送攻击 payload（虽然只有几个请求，但会在 WAF 日志留痕）。
  - `nikto` 的 `-Tuning 6`（DoS 类）可能影响服务可用性，生产环境用 `-Tuning x6` 排除。
  - `commix`/`sqlmap` 的利用参数（`--os-shell`、`--file-write`）是**破坏性**操作。
- **合法练习目标**：自建靶场（上面那几条 Docker 命令）、DVWA、Juice Shop、bWAPP、`testphp.vulnweb.com`（Acunetix 公开练习站，注意遵守其使用条款）。
- **演练结束后清理**：如果工具在目标上创建了临时文件或表（sqlmap 的 `--cleanup`、commix 写进去的 WebShell），**必须清理干净**。

## 与其他分类的衔接

- 本分类的**输入**通常来自 [01-信息搜集](../01-信息搜集/README.md)：`nmap` 找到的 Web 端口、`whatweb` 识别的技术栈。
- 本分类发现的**指纹与版本**需要去 [02-漏洞分析](../02-漏洞分析/README.md) 用 [searchsploit](../02-漏洞分析/searchsploit.md)、[nuclei](../02-漏洞分析/nuclei.md) 进一步匹配和验证。
- 通过 Web 漏洞拿到的 shell，后续属于 [08-后渗透](../08-后渗透/) 范畴（提权、横向）。
- 从 Web 泄露的凭据哈希，属于口令攻击范畴（Kali 分类 `passwords`）。
