# nikto（Web 服务器漏洞扫描）

> **一句话**：对 Web 服务器做一次"体检"——检查错误配置、危险文件、默认页面、过期软件，以及 6700+ 条已知问题。
> **分类**：漏洞分析 ｜ **Kali 包**：`nikto` ｜ **官方文档**：<https://github.com/sullo/nikto>

## 1. 它解决什么问题

[whatweb](../01-信息搜集/whatweb.md) 告诉你"这是什么技术"，[nuclei](nuclei.md) 用模板做精确匹配。nikto 处在两者之间，它回答的是：

**这台 Web 服务器有没有明显的配置问题？** 比如：

- `/admin/` 目录没有访问控制
- 服务器版本号暴露、Banner 泄露
- 存在备份文件（`index.php.bak`、`www.zip`）
- 存在默认安装页面、示例脚本、测试页面
- HTTP 方法（`PUT`、`DELETE`）被错误开启
- 已知的过期组件（旧版 phpMyAdmin、旧版 Web 服务器）

| 工具 | 定位 | 特点 |
|------|------|------|
| **nikto** | Web 服务器**配置与已知问题**扫描 | 内置 6700+ 检查项，覆盖面极广；误报相对多 |
| [nuclei](nuclei.md) | 基于模板的**精确**漏洞验证 | 误报极低，模板可自定义 |
| [wpscan](../03-Web应用/wpscan.md) | WordPress 专项 | CMS 层面更深 |
| [whatweb](../01-信息搜集/whatweb.md) | 指纹识别 | 不报问题，只报技术栈 |
| [searchsploit](searchsploit.md) | 本地漏洞库检索 | 需要先知道组件和版本 |

**重要认知**：nikto 是"广撒网"的工具，输出里会有假阳性。它是一个**线索生成器**，不是一个结论生成器——每条结果都需要人工或 [nuclei](nuclei.md) 复核。

## 2. 工作原理

```text
   nikto -h http://target:8080
        │
   ┌────┴──────────────────────────────────────────────────┐
   │ ① 识别目标响应基线                                     │
   │    - 请求一个不存在的路径（如 /nikto-test-12345）       │
   │    - 记录返回的 404 页面特征（长度/内容哈希）           │
   │    → 后续任何"和这个不一样"的响应都可能是真命中          │
   │    （-no404 可关闭此步，速度更快但误报更多）             │
   └────┬──────────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────────┐
   │ ② 依次跑插件（默认 ALL），每个插件带一批测试用例        │
   │    数据库文件（.db）里是具体的路径/特征：               │
   │      db_tests       常见文件与目录                     │
   │      db_variables   参数名                            │
   │      db_realms      认证域                            │
   │      db_dictionary  字典词                            │
   │      db_404_strings 404 关键字                        │
   │      db_server_msgs 服务器错误消息                     │
   │    -Tuning 可只跑关心的类别（如只跑 2+b 类）            │
   └────┬──────────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────────┐
   │ ③ 输出 + 分级                                          │
   │    + 命中（可能存在的信息泄露/配置问题）                │
   │    - 失败/无结果                                       │
   │    -Display 控制显示哪些额外信息（重定向/Cookie/200 等）│
   └────┬──────────────────────────────────────────────────┘
        │
   -o out.json / -Format json / csv / htm / xml / txt
```

几个关键机制：

- **404 基线检测**：这是 nikto 减少误报的核心手段。很多服务器对不存在的路径返回 200 + 一个友好页面，如果不做基线比对，所有测试都会"命中"。
- **插件与数据库分离**：插件是逻辑，数据库是"要测什么"。`-update` 更新这两者。
- **`-Tuning` 是控制范围的关键**：默认跑全部会非常慢且噪声大。按类别筛选是实战必备技巧。
- **`-Single` 单请求模式**：交互式地发一个请求看详细响应，用来**复核**某个可疑发现，或者研究服务器的响应特征。
- **`-Display` 决定"看得见什么"**：默认只显示命中项，打开 `3`（显示所有 200）能看到被忽略的细节——复核时很有用。

## 3. 安装与快速上手

```bash
sudo apt install nikto
nikto -Version
nikto -Help | head -40
```

最小可用命令：

```bash
# 1) 基础扫描（明确指向 80 端口）
nikto -h http://192.168.56.101

# 2) 指定端口
nikto -h 192.168.56.101 -p 8080

# 3) 只跑配置与信息泄露类，快很多
nikto -h http://192.168.56.101 -Tuning 23 -nointeractive
```

> `-h` 在这里是 `-host` 的缩写（nikto 区分大小写：`-h` = host，`-Help` 才是帮助）。这一点和多数工具相反，容易踩坑。

## 4. 核心参数详解

### 目标

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-h <host>` / `-host <host>` / `-url <host>` | 目标：IP、主机名、URL，或**包含主机列表的文件**；`-` 表示 stdout | 可解析 `nmap -oG` 输出 |
| `-p <port>` / `-port <port>` | 目标端口，支持范围 `80-90` 与列表 `80,88,90`；默认 80 | 多端口用逗号 |
| `-ssl` | 强制在指定端口上用 SSL | **扫 HTTPS 必加**，否则要先等 HTTP 超时，慢很多 |
| `-nossl` | 禁用 SSL | 明确知道不是 HTTPS 时 |
| `-nosslkeepalive` | 关闭 TLS 连接复用 | 某些老服务器对 keep-alive 有问题时 |
| `-vhost <name>` | 设置发送的 `Host` 头 | **虚拟主机场景的关键**：同一 IP 不同站点 |
| `-root <dir>` | 给所有请求加前缀，格式 `/directory` | 应用全在子目录下时 |
| `-ipv4` / `-ipv6` | 只用 IPv4 / 只用 IPv6 | 双栈环境 |
| `-check6` | 测试 IPv6 连通性 | 排查 |
| `-noslash` | 去掉 URL 末尾斜杠（`/admin/` → `/admin`） | 某些服务器对斜杠敏感 |

### 范围与调优（最影响效率）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-Tuning <x>` | 只跑指定类别的测试 | 见下方类别表 |
| `-Cgidirs <v>` | 扫描哪些 CGI 目录：`none`、`all`，或字面值如 `/cgi/`（**带尾部斜杠**） | 默认用 config.txt 里的全部，通常过多 |
| `-Plugins <list>` | 指定插件列表（`ALL` / `NONE` / 逗号分隔的名字） | 用 `-list-plugins` 查名字 |
| `-list-plugins` | 列出全部插件后退出 | 找插件名 |
| `-mutate <n>` | 变异测试（组合/猜测），会大幅增加请求量 | 见下方变异表 |
| `-mutate-options <..>` | 给变异提供额外信息（如字典文件） | 配 `-mutate 6` |
| `-findonly` | 只发现 HTTP(S) 端口并报告 `Server` 头，不做安全扫描 | 快速探测 |
| `-no404` | 关闭 404 猜测。请求更少（适合慢链路/嵌入式），但**误报更多** | 默认别用 |
| `-404string` / `-404code` | 手工指定"找不到"的特征串/状态码 | 自动基线不准时 |

### 显示与输出

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-Display <v>` | 控制显示内容 | 见下方显示码表 |
| `-o <file>` | 输出到文件（已存在则**追加**）；`.` 自动命名 | 推荐显式命名 |
| `-Format <fmt>` | 输出格式：`csv`、`json`、`htm`、`xml`、`txt`、`sql`、`sqld` | 不指定则按 `-o` 的扩展名推断 |
| `-Save <dir>` | 把阳性响应保存到目录（`.` 自动命名） | 留证据 |
| `-maxtime <t>` | 每个主机的最大测试时间（如 `1h`、`60m`、`3600s`） | **大目标必设**，防止跑不完 |
| `-nointeractive` | 关闭交互功能 | 脚本化必加 |
| `-nocookies` | 不在后续请求里使用响应 Cookie | 避免被会话影响 |
| `-useragent <UA>` | 自定义 User-Agent | 绕过基于 UA 的拦截 |
| `-Add-header <hdr>` | 追加 HTTP 头，可多次使用 | 如 `-Add-header "X-Forwarded-For: 127.0.0.1"` |

**`-Tuning` 类别表**：

| 值 | 类别 |
|----|------|
| `0` | 文件上传 |
| `1` | 有意思的文件 / 常见于日志中的文件 |
| `2` | 配置错误 / 默认文件 |
| `3` | 信息泄露 |
| `4` | 注入（XSS / 脚本 / HTML） |
| `5` | 远程文件获取（Web 根目录内） |
| `6` | 拒绝服务 |
| `7` | 远程文件获取（整服务器） |
| `8` | 命令执行 / 反弹 Shell |
| `9` | SQL 注入 |
| `a` | 认证绕过 |
| `b` | 软件识别 |
| `c` | 远程源代码包含 |
| `x` | **反转逻辑**：包含除指定类别外的全部 |

用法示例：`-Tuning 23` = 只跑"配置错误/默认文件" + "信息泄露"；`-Tuning x6` = 跑全部但**排除拒绝服务类**（很实用，避免把目标打挂）。

**`-Display` 显示码表**：

| 值 | 含义 |
|----|------|
| `1` | 显示重定向 |
| `2` | 显示收到的 Cookie |
| `3` | 显示所有 200/OK 响应 |
| `4` | 显示需要认证的 URL |
| `D` | 调试输出 |
| `E` | 显示所有 HTTP 错误 |
| `P` | 向 stdout 打印进度 |
| `S` | 输出中打码 IP 与主机名 |
| `V` | 详细输出 |

**`-evasion` 规避码表**（LibWhisker 的 IDS 规避技术）：

| 值 | 技术 |
|----|------|
| `1` | 随机 URI 编码（非 UTF8） |
| `2` | 目录自引用（`/./`） |
| `3` | 提前结束 URL |
| `4` | 前置长随机串 |
| `5` | 伪造参数 |
| `6` | 用 TAB 作为请求分隔符 |
| `7` | 改变 URL 大小写 |
| `8` | 使用 Windows 目录分隔符（`\`） |
| `A` | 用回车 `0x0d` 作为请求分隔符 |
| `B` | 用二进制值 `0x0b` 作为请求分隔符 |
| `R` | 每个请求随机 User-Agent |

**`-mutate` 变异码表**：

| 值 | 技术 |
|----|------|
| `1` | 用所有根目录组合测试所有文件 |
| `2` | 猜测口令文件名字 |
| `3` | 通过 Apache `/~user` 枚举用户名 |
| `4` | 通过 cgiwrap `/cgi-bin/cgiwrap/~user` 枚举用户名 |
| `5` | 爆破子域名（假设主机名是父域） |
| `6` | 用字典文件猜测目录名 |

### 其他

| 参数 | 作用 |
|------|------|
| `-Pause <sec>` | 每个测试之间的延迟（秒） |
| `-timeout <sec>` | 请求超时（默认 10 秒） |
| `-id <id:pass>` | HTTP Basic 认证（也支持 `id:pass:realm`） |
| `-useproxy` | 使用配置文件中定义的代理 |
| `-config <file>` | 使用指定配置文件替代 `config.txt` |
| `-Option <k=v>` | 覆盖 nikto.conf 中的选项，可多次使用 |
| `-nolookup` | 不做 DNS 反解 |
| `-dbcheck` | 检查扫描数据库语法错误 |
| `-update` | 从 cirt.net 更新插件与数据库 |
| `-nocheck` | 启动时不检查更新 |
| `-Single` | 单请求模式：交互式指定一次请求并显示详细输出 |
| `-RSAcert <file>` / `-key <file>` | 客户端证书 / 私钥（双向 TLS） |
| `-Version` | 显示版本 |
| `-Help` | 扩展帮助 |

## 5. 实战演练

**环境**：本地实验环境，全部为自建靶机。

- DVWA 容器：`docker run -d -p 8080:80 vulnerables/web-dvwa` → `http://192.168.56.102:8080`
- Metasploitable2（内置 Mutillidae、DVWA、phpMyAdmin 等）：`http://192.168.56.101`
- 攻击机 Kali：`192.168.56.10`

> nikto 会对目标发起**数千个请求**，噪声极大。只对你有授权的目标使用，生产环境扫描前务必告知运维。

### 场景 1：基础扫描（先看全貌）

```bash
nikto -h http://192.168.56.101 -nointeractive -o /tmp/nikto_msf.txt
```

预期输出片段：

```text
- Nikto v2.6.1
---------------------------------------------------------------------------
+ Target IP:          192.168.56.101
+ Target Hostname:    192.168.56.101
+ Target Port:        80
+ Start Time:         2026-09-15 17:40:00 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.2.8 (Ubuntu) DAV/2
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type.
+ No CGI Directories found (use '-Cgidirs all' to force check all possible dirs)
+ Apache/2.2.8 appears to be outdated (current is at least 2.4.62).
+ /phpMyAdmin/: phpMyAdmin directory found.
+ /phpMyAdmin/changelog.php: phpMyAdmin changelog found, version appears to be 2.11.1.
+ OSVDB-12184: /?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings.
+ /icons/README: Apache default file found.
+ /test/: This might be interesting.
+ 8910 requests: 0 error(s) and 12 item(s) reported on remote host
+ End Time:           2026-09-15 17:52:00 (GMT-4) (720 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

解读（逐条意义）：

| 输出 | 含义 | 严重度 |
|------|------|--------|
| `Server: Apache/2.2.8` | 版本号直接暴露 | 低（但为后续利用提供输入） |
| `X-Frame-Options header is not present` | 可能被点击劫持 | 低 |
| `Apache/2.2.8 appears to be outdated` | 组件过期 | 中（具体看 CVE） |
| `/phpMyAdmin/` 存在 + 版本 `2.11.1` | **高价值**：旧版 phpMyAdmin 有多个 RCE | 高 |
| `/test/` 存在 | 可能有测试代码 | 中 |
| `8910 requests: ... 12 item(s)` | 统计：请求数 / 发现数 | — |

### 场景 2：聚焦高信噪比的类别（实战推荐）

```bash
nikto -h http://192.168.56.101 -Tuning 23 -nointeractive \
      -maxtime 10m -o /tmp/nikto_tuning.json -Format json
```

解读：
- `-Tuning 23` = 只跑「配置错误/默认文件」+「信息泄露」，跳过注入类（那类交给 [sqlmap](../03-Web应用/sqlmap.md) 和 [nuclei](nuclei.md)）。
- `-maxtime 10m` 防止无限制地测下去。
- `-Format json` 让结果可被脚本处理。

**排除危险类别**的写法：

```bash
# 跑全部，但排除"拒绝服务"(6) 类——避免把目标打挂
nikto -h http://192.168.56.101 -Tuning x6 -nointeractive
```

### 场景 3：HTTPS / 非标准端口 / 虚拟主机

```bash
# HTTPS：必须加 -ssl，否则每个请求都要等 HTTP 超时
nikto -h 192.168.56.102 -p 8443 -ssl -nointeractive

# 非标准端口的 HTTP
nikto -h 192.168.56.102 -p 8080 -nointeractive

# 虚拟主机：同一 IP 上不同站点
nikto -h 192.168.56.102 -p 80 -vhost www.example.lab
```

解读：`-vhost` 是很多人忽略的参数。**反向代理/共享 IP 托管场景下，不带正确的 Host 头扫到的根本不是目标应用**。

### 场景 4：快速端口发现 + 批量扫描

```bash
# 只发现 HTTP/S 端口并报告 Server 头（不扫描）
nikto -h 192.168.56.102 -p 80,443,8000,8080,8443 -findonly -nointeractive

# 批量：从 nmap 的 grepable 输出直接喂给 nikto
sudo nmap -p80,443,8080 --open -oG - 192.168.56.0/24 | awk '/Ports:/{print $2}' > web_hosts.txt
nikto -h web_hosts.txt -nointeractive -maxtime 5m -o /tmp/nikto_batch.csv -Format csv

# 批量 HTTPS
nikto -h web_hosts.txt -p 443 -ssl -nointeractive -o /tmp/nikto_443.csv -Format csv
```

解读：`-findonly` 是一个被低估的参数——它只做"这个端口是不是 HTTP、Server 头是什么"，用于批量普查**极快**。`-h <文件>` 可以直接吃主机列表（也支持 `nmap -oG` 格式），省掉自己写循环。

### 场景 5：复核可疑发现（`-Single` + `-Display`）

```bash
# 单请求模式：手工指定请求，看完整响应
nikto -h http://192.168.56.101 -Single

# 打开"显示所有 200 响应"，看看被跳过的内容
nikto -h http://192.168.56.101 -Display 3 -nointeractive 2>&1 | head -60

# 用 curl 复核某个可疑路径（最可靠的验证方式）
curl -sI http://192.168.56.101/phpMyAdmin/ | head -5
curl -s http://192.168.56.101/phpMyAdmin/changelog.php | grep -i "version"
```

解读：nikto 的每条结果是**线索**。上面用 `curl` 直接验证 `/phpMyAdmin/changelog.php` 里是否真有版本号——这才是"确认"。

## 6. 输出解读

### 行首符号

| 符号 | 含义 |
|------|------|
| `+` | 一条发现（信息/潜在问题） |
| `-` | 普通状态/失败信息 |
| `+ OSVDB-xxxxx:` | 关联到 OSVDB 漏洞 ID |
| `+ /path: description` | 路径 + 问题描述 |

### 关键字段

| 字段 | 含义 | 下一步 |
|------|------|--------|
| `Server:` | 服务器与版本 | 记下版本 → [searchsploit](searchsploit.md) |
| `X-Frame-Options ... not present` | 安全响应头缺失 | 属加固建议，非漏洞 |
| `X-Content-Type-Options header is not set` | 同上 | 加固建议 |
| `appears to be outdated` | 版本过期 | 查该版本 CVE |
| `/path/: ... found` | 发现的敏感路径 | **curl 复核** |
| `version appears to be X` | 推测的组件版本 | 置信度较低，需复核 |
| `No CGI Directories found` | CGI 目录探测无结果 | 可用 `-Cgidirs all` 强制 |
| `N requests: E error(s) and M item(s)` | 统计：请求数/错误数/发现数 | 判断扫描是否正常完成 |
| `End Time ... (720 seconds)` | 耗时 | 时间过长时用 `-maxtime` 或收窄 `-Tuning` |

### 严重度判断（人工分级建议）

| 发现类型 | 建议严重度 |
|---------|-----------|
| 敏感文件可下载（备份、配置、日志） | 高 |
| 旧版 CMS/管理面板（如 phpMyAdmin 2.x） | 高 |
| 目录列表开启（`Options +Indexes`） | 中 |
| 默认/示例页面、默认文件 | 中低 |
| 缺少安全响应头 | 低（加固项） |
| 服务器版本号暴露 | 低（信息泄露） |
| 声称的 SQL 注入 / XSS / 命令执行 | **必须复核**，nikto 这类结果误报率高 |

## 7. 与其他工具配合

```bash
# 1) nmap 发现 Web 端口 -> nikto
sudo nmap -p80,443,8080,8443 --open -oG - 192.168.56.0/24 | awk '/Ports:/{print $2}' > web.txt
nikto -h web.txt -nointeractive -maxtime 5m -o nikto_all.html -Format htm

# 2) whatweb 指纹 -> nikto 定点扫描
whatweb -a 1 http://192.168.56.101 | grep -q phpMyAdmin && \
  nikto -h http://192.168.56.101/phpMyAdmin/ -nointeractive

# 3) nikto 线索 -> nuclei 精确验证
nikto -h http://192.168.56.101 -Tuning 23 -o nikto.json -Format json -nointeractive
nuclei -u http://192.168.56.101 -o nuclei_out.txt

# 4) nikto 发现版本 -> searchsploit 找 EXP
nikto -h http://192.168.56.101 | grep -oP 'phpMyAdmin[^,]*version appears to be \K[\d.]+'
searchsploit phpMyAdmin 2.11
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `-h` 想查帮助却当成主机 | nikto 中 `-h` = `-host`；帮助是 `-Help` | 记牢这个反直觉的设计 |
| 扫描 HTTPS 极慢 | 没加 `-ssl`，每个请求都要先等 HTTP 超时 | 加 `-ssl` |
| 结果里一大堆"发现"，全是假的 | 服务器对不存在路径返回 200 + 友好页，404 基线失效 | 用 `-404code`/`-404string` 手工指定；或 `-Display 3` 看真实响应 |
| 扫描时间不可控（几小时） | 默认跑全部插件与 CGI 目录 | `-Tuning 23`、`-Cgidirs none`、`-maxtime 10m` |
| 被 WAF 封了 IP | 请求量太大 | `-Pause 1`、`-useragent` 换 UA、`-evasion 1,7`、或换 `-Tuning` |
| `-Tuning x6` 之类的语法报错 | `x` 只能出现在开头 | `x` 之后要跟要排除的类别，如 `x6` |
| 扫到的是"另一个网站" | 共享 IP / 反代，Host 头不对 | 加 `-vhost <正确的域名>` |
| 输出文件越跑越大 | `-o` 对已存在文件是**追加** | 每次换文件名，或先删除 |
| JSON 输出格式不符合预期 | 没指定 `-Format` 时按扩展名推断，可能得到 txt | 显式加 `-Format json` |
| `No CGI Directories found` 后没有进一步探测 | 默认只测 config.txt 里的 CGI 目录 | `-Cgidirs all`（会显著变慢） |
| 把测试环境打挂了 | 跑到"拒绝服务"类测试（类别 6） | `-Tuning x6` 排除 |

## 9. 防御视角（蓝队）

- **nikto 的流量特征极其明显**——这是蓝队最有利的地方：
  - **请求量**：单个源 IP 在短时间内产生数千个 404 请求，路径集中在 `/admin/`、`/backup/`、`/phpMyAdmin/`、`/test/`、`/*.bak`、`/*.old`。
  - **UA**：默认 `Mozilla/5.0 (compatible; Nikto/2.6.1 ...)`，直接可匹配。
  - **固定路径模式**：nikto 的测试数据库里有大量固定字符串，属于高置信度的指纹。
- **检测规则建议**：
  - WAF/IDS 规则：请求路径命中"敏感文件词表"（`.bak`、`.old`、`.zip`、`.git/`、`/phpinfo.php`）的**计数阈值**告警。
  - 对单个源 IP 单位时间内的 404 数量设阈值（正常用户几乎不产生 404 风暴）。
  - UA 直接匹配 `Nikto`。
- **缓解措施**：
  - **减少暴露**：删除示例页面、`/icons/README`、默认安装目录、测试目录。nikto 的大多数命中来自"本来就不该存在的东西"。
  - **关闭目录列表**：Apache `Options -Indexes`，nginx `autoindex off`。
  - **补全安全响应头**：`X-Frame-Options`、`X-Content-Type-Options`、`Content-Security-Policy`——这样 nikto 的响应头类发现会直接清零，减少报告噪声。
  - **隐藏版本号**：`ServerTokens Prod`（Apache）、`server_tokens off`（nginx）、`expose_php = Off`（PHP）。
  - **移除备份文件**：Web 根目录下不能有 `.bak`/`.old`/`.zip`/`.tar.gz`，这是最容易被 nikto 翻出来也最危险的一类。
  - **边界限速**：对单源请求速率做限制，让大规模扫描变慢甚至不可行。
- **注意**：nikto 是**只读扫描**（默认不修改目标），但类别 6 的 DoS 测试可能影响服务可用性——防守方不需要专门为此加固，但运维侧要避免在生产上跑 nikto 的全量测试。

## 10. 参考

- 官方仓库（含 `documentation/nikto.1` 完整手册）：<https://github.com/sullo/nikto>
- Kali 工具页：<https://www.kali.org/tools/nikto/>
- man page：`man nikto`
- 用法核实：本教程参数取自 `nikto 2.6.1` 的 man page 与上游 `program/plugins/nikto_core.plugin` 中 `general_config`/`usage` 的实际选项定义（`-h` 为 `-host` 缩写的行为已用 `Getopt::Long::Configure("no_ignore_case")` 实测确认）

---

**相关教程**：[nuclei](nuclei.md) ｜ [searchsploit](searchsploit.md) ｜ [openssl](openssl.md) ｜ [whatweb](../01-信息搜集/whatweb.md) ｜ [nmap](../01-信息搜集/nmap.md) ｜ [wpscan](../03-Web应用/wpscan.md) ｜ [sqlmap](../03-Web应用/sqlmap.md)
