# gobuster（目录、DNS 与虚拟主机爆破）

> **一句话**：用字典快速爆破 Web 目录/文件、子域名、虚拟主机名、对象存储桶和 TFTP 文件。
> **分类**：Web 应用 ｜ **Kali 包**：`gobuster` ｜ **官方文档**：<https://github.com/OJ/gobuster>

## 1. 它解决什么问题

网站里总有一些**没有链接指向、但可以被直接访问**的资源：备份文件、管理目录、测试页面、`.git/` 目录、上传接口……

gobuster 用字典一条条去请求，根据 **HTTP 状态码和响应长度**判断哪些路径真实存在。它有 7 种工作模式，不只是目录爆破：

| 模式 | 作用 |
|------|------|
| `dir` | 爆破 Web 目录与文件（最常用） |
| `dns` | 爆破子域名（支持通配符检测） |
| `vhost` | 爆破虚拟主机名（**不发 DNS 请求，改 Host 头**） |
| `fuzz` | 用 `FUZZ` 关键字做自定义 fuzz |
| `s3` / `gcs` | 枚举开放的 AWS S3 / Google Cloud Storage 桶 |
| `tftp` | 枚举 TFTP 服务器上的文件 |

| 工具 | 语言 | 特点 | 何时用 |
|------|------|------|--------|
| **gobuster** | Go | 模式最多（含 S3/GCS/TFTP）、速度快、**会对结果做校验（precheck）** | 想要"一站式"多用途爆破 |
| [ffuf](ffuf.md) | Go | **fuzz 能力最强**（多字典、多位置、递归、matcher/filter 极丰富） | 需要复杂 fuzz 或精细过滤 |
| [dirb](dirb.md) | C | 老牌，默认字典好、有"递归"和"找到就继续"的智能 | 简单场景、教学 |
| [wfuzz](wfuzz.md) | Python | 历史久，支持 fuzz 与插件 | 老脚本兼容 |
| `feroxbuster`（非 Kali 默认） | Rust | 递归 + 提取链接 | 需要自动递归 |

**选型口诀**：只想快速跑一遍目录 → [dirb](dirb.md)；要**速度与精度控制** → gobuster 或 [ffuf](ffuf.md)；要**复杂 fuzz**（多参数、多字典、递归、精细过滤）→ [ffuf](ffuf.md)。

## 2. 工作原理

```text
   gobuster dir -u http://target -w wordlist.txt
        │
   ┌────┴───────────────────────────────────────────────────────┐
   │ ① 预检查（precheck）—— gobuster 区别于其他工具的关键设计     │
   │    - 请求一个不存在的随机路径，记录"404 基线"               │
   │    - 检测目标是否对所有路径都返回 200（软 404）              │
   │    - 如果基线异常，默认**拒绝继续**（避免结果全是假阳性）     │
   │      --force 可强制继续（会得到大量噪声）                    │
   └────┬───────────────────────────────────────────────────────┘
        │
   ┌────┴───────────────────────────────────────────────────────┐
   │ ② 并发发送请求（-t 线程，默认 10）                           │
   │    每个线程从 wordlist 取一个条目，拼到 URL 后面请求          │
   │    -x php,html 会把每个词再扩展成 word.php / word.html       │
   │    -e 打印完整 URL；-f 给每个词加尾斜杠                       │
   └────┬───────────────────────────────────────────────────────┘
        │
   ┌────┴───────────────────────────────────────────────────────┐
   │ ③ 结果判定（两套机制）                                        │
   │    -s  正向白名单：只报告这些状态码（如 200,301,302,403）      │
   │    -b  反向黑名单：排除这些状态码（**默认排除 404**）          │
   │    -xl 按响应长度排除（对付"软 404 页面长度恒定"的情况）       │
   │    -n  不显示状态码；-hl 隐藏响应长度                         │
   └────┬───────────────────────────────────────────────────────┘
        │
   输出：`[状态码] [长度] [完整路径]`，或写文件（-o）
```

**为什么 gobuster 的"预检查"很重要？** 很多现代框架（Django、Next.js、Spring Boot）对不存在的路径返回 `200 OK` + 一个友好页面。这时爆破工具会**报告几千个"存在的路径"**。gobuster 的做法是：先探测基线，如果发现"所有路径都返回同一个页面"，就停下来告诉你——这是它比老工具更实用的地方。

**模式差异**：

- `dir` 走 HTTP 请求，看状态码。
- `dns` 走 **DNS 查询**，看能不能解析出 A/AAAA 记录；`-c` 还会检查 CNAME；`-wc` 在检测到通配符解析（`*.example.com`）时强制继续。
- `vhost` 走 **HTTP + 自定义 Host 头**：`-u` 填 IP，`-H "Host: FUZZ.example.com"`（或 `--append-domain`）。这样能发现**只在内网 DNS 注册、公网 DNS 看不到**的站点。
- `s3`/`gcs` 直接请求桶的 HTTP 端点，看返回码判断桶存在与可读性。

## 3. 安装与快速上手

```bash
sudo apt install gobuster
gobuster version
gobuster help dir        # 每个模式的参数分开看
```

最小可用命令：

```bash
# 1) 目录爆破（最常用）
gobuster dir -u http://192.168.56.101 -w /usr/share/seclists/Discovery/Web-Content/common.txt

# 2) 带扩展名
gobuster dir -u http://192.168.56.101 -w common.txt -x php,html,txt,bak

# 3) 子域名爆破
gobuster dns -d example.com -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

## 4. 核心参数详解

### 模式

| 模式 | 说明 |
|------|------|
| `dir` | 目录/文件枚举（可写 `--dir`） |
| `dns` | 子域名枚举（`--dns`） |
| `vhost` | 虚拟主机枚举（`--vhost`） |
| `fuzz` | 自定义 fuzz（`--fuzz`） |
| `s3` / `gcs` | AWS / GCS 桶枚举 |
| `tftp` | TFTP 文件枚举 |

### 全局 / 通用

| 参数 | 作用 | 建议 |
|------|------|------|
| `-w, --wordlist <path>` | 字典路径；`-` 表示从 STDIN 读 | 必填 |
| `-t, --threads <n>` | 并发线程数（默认 10） | 内网 20~50；公网 5~10 |
| `-d, --delay <dur>` | 每个线程两次请求之间的等待（如 `1500ms`） | 限速与规避 |
| `--timeout <dur>` | HTTP 超时（默认 10s） | — |
| `-o, --output <file>` | 结果写入文件 | 推荐 |
| `-q, --quiet` | 不打印 banner 与噪声 | 脚本化 |
| `-v, --verbose` | 详细输出（含错误） | 排障 |
| `--no-error`（`-ne`） | 不显示错误 | 批量时减少噪声 |
| `--no-progress`（`-np`） | 不显示进度 | — |
| `--no-color`（`-nc`） | 关闭颜色 | 重定向到文件 |
| `-p, --pattern <file>` | 替换模式文件 | 高级 |
| `--debug` | 调试输出 | 排障 |

### HTTP 相关（`dir`/`vhost`/`fuzz` 通用）

| 参数 | 作用 | 建议 |
|------|------|------|
| `-u, --url <url>` | 目标 URL | 必填（`tftp`/`dns` 除外） |
| `-c, --cookies <c>` | Cookie 字符串 | 需要登录态时 |
| `-H, --headers <h>` | 自定义头（可多次），如 `-H 'Host: x'` | **vhost 模式的核心** |
| `-U, --username` / `-P, --password` | HTTP Basic 认证 | — |
| `-m, --method <m>` | HTTP 方法（默认 `GET`） | 如 `POST` |
| `-a, --useragent <ua>` | 自定义 UA | — |
| `-rua, --random-agent` | 随机 UA | 绕过简单 UA 过滤 |
| `--proxy <url>` | 代理（http/socks5） | 配合 Burp |
| `-k, --no-tls-validation` | 跳过 TLS 证书校验 | 自签证书场景 |
| `-r, --follow-redirect` | 跟随重定向 | **默认不跟随**；跟随时注意结果会变 |
| `--retry` / `--retry-attempts <n>` | 超时重试 / 重试次数（默认 3） | 慢链路 |
| `--client-cert-pem` / `--client-cert-pem-key` / `--client-cert-p12` / `--client-cert-p12-password` | 客户端证书相关 | 双向 TLS |
| `-iface, --interface <if>` | 指定网卡 | 多网卡 |
| `--local-ip <ip>` | 指定本地源 IP | 与 `--interface` 互斥 |
| `--tls-renegotiation` | 启用 TLS 重协商 | 老服务器 |

### dir 模式专属

| 参数 | 作用 | 建议 |
|------|------|------|
| `-s, --status-codes <list>` | **正向**状态码白名单（支持范围 `200,300-400`） | 如 `-s 200,204,301,302,307,401,403` |
| `-b, --status-codes-blacklist <list>` | **反向**黑名单（**默认 `404`**，设置后会覆盖 `-s`） | 默认够用；想更严格时用 `-b 404,400,302` |
| `-x, --extensions <ext>` | 追加扩展名（逗号分隔） | `-x php,asp,aspx,jsp,html,js,bak,zip` |
| `-X, --extensions-file <file>` | 从文件读扩展名 | 扩展名很多时 |
| `-e, --expanded` | 打印完整 URL | 结果给其他工具用时**建议加** |
| `-n, --no-status` | 不打印状态码 | 输出更干净 |
| `-hl, --hide-length` | 不打印响应长度 | — |
| `-f, --add-slash` | 给每个请求加尾斜杠 | 目标是"目录型"应用时 |
| `-xl, --exclude-length <list>` | 按响应长度排除（支持范围 `203-206`） | **软 404 但长度恒定时用** |
| `-db, --discover-backup` | 发现文件后自动尝试多个备份扩展名（`.bak`、`.old`…） | **实战很实用**，能挖到源码备份 |
| `--force` | 预检查失败时强制继续 | 慎用（结果会充满假阳性） |

### dns 模式专属

| 参数 | 作用 | 建议 |
|------|------|------|
| `-do, --domain <d>` | 目标域名 | 必填 |
| `-c, --check-cname` | 同时检查 CNAME 记录 | 建议加 |
| `-to, --timeout <dur>` | DNS 解析超时（默认 1s） | 内网 DNS 慢时调大 |
| `-wc, --wildcard` | 检测到通配符时强制继续 | 目标有 `*.example.com` 时 |
| `-nf, --no-fqdn` | 不加尾部点，让解析器使用 search domain | 内网场景 |
| `--resolver <server>` | 自定义 DNS 服务器（`server` 或 `server:port`） | **内网爆破必用内网 DNS** |
| `--protocol <udp\|tcp>` | 自定义解析器的协议（默认 udp） | TCP 用于大响应 |

### vhost 模式专属

| 参数 | 作用 | 建议 |
|------|------|------|
| `-u, --url <url>` | **通常填目标 IP** | 因为要靠 Host 头区分站点 |
| `-ad, --append-domain` | 把 URL 里的域名追加到字典词后（否则字典里必须是完整 FQDN） | 常用 |
| `-do, --domain <d>` | 用 IP 做 URL 时要追加的域名；留空则从 URL 提取 | — |
| `-xl, --exclude-length <list>` | 按响应长度排除 | **vhost 模式几乎必须用** |
| `-xs, --exclude-status <list>` | 按状态码排除 | — |
| `-xh, --exclude-hostname-length` | 根据响应中动态主机名长度自动调整排除长度 | 高级技巧 |
| `--force` | 结果不保证时强制执行 | — |

### fuzz 模式专属

| 参数 | 作用 |
|------|------|
| `-u, --url <url>` | 含 `FUZZ` 关键字的 URL，如 `http://t/?FUZZ=1` |
| `-b, --exclude-statuscodes <list>` | 排除的状态码 |
| `-xl, --exclude-length <list>` | 排除的响应长度 |
| `-B, --body <body>` | 请求体（含 `FUZZ`） |

### s3 / gcs / tftp

| 参数 | 作用 |
|------|------|
| `-m, --max-files <n>` | 列出桶内文件的最大数量（默认 5） |
| `-s, --show-files` | 显示找到的桶里的文件（默认 true） |
| `-s, --server <ip>`（tftp） | 目标 TFTP 服务器 |
| `-to, --timeout`（tftp） | TFTP 超时（默认 1s） |

## 5. 实战演练

**环境**：本地实验环境。

- Metasploitable2：`http://192.168.56.101`（内置 Mutillidae、DVWA、phpMyAdmin 等）
- DVWA 容器：`http://192.168.56.102:8080`
- 攻击机 Kali：`192.168.56.10`

> 字典使用 Kali 自带的 `seclists`（`sudo apt install seclists`），路径在 `/usr/share/seclists/`。**只对授权目标爆破。**

### 场景 1：基础目录爆破

```bash
gobuster dir -u http://192.168.56.101 \
  -w /usr/share/seclists/Discovery/Web-Content/common.txt \
  -t 30 -o gobuster_msf.txt
```

预期输出片段：

```text
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.56.101
[+] Method:                  GET
[+] Threads:                 30
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 286]
/.htaccess            (Status: 403) [Size: 289]
/.htpasswd            (Status: 403) [Size: 289]
/cgi-bin/             (Status: 403) [Size: 287]
/dav/                 (Status: 401) [Size: 288]
/index.php            (Status: 200) [Size: 891]
/phpMyAdmin/          (Status: 301) [Size: 332] [--> http://192.168.56.101/phpMyAdmin/]
/test/                (Status: 301) [Size: 320] [--> http://192.168.56.101/test/]
Progress: 4614 / 4614 (100.00%)
===============================================================
```

解读：
- `200` = 存在且可访问；`301` = 重定向（通常目录，会显示 `-->` 目标）；`401` = 需要认证（**有价值**：说明那里有受保护资源）；`403` = 存在但禁止访问（**同样有价值**：路径真实存在）。
- `/dav/ (Status: 401)` —— WebDAV 接口，值得进一步测试。
- `/test/` —— 测试目录往往权限宽松。
- **注意**：默认只排除 404，所以 403/401 也会报出来——这些**不是噪声，是重要线索**。

### 场景 2：带扩展名 + 自动找备份文件

```bash
gobuster dir -u http://192.168.56.101/dvwa \
  -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt \
  -x php,txt,bak,old,zip,tar.gz \
  --discover-backup \
  -t 30 -e -o gobuster_dvwa.txt
```

预期输出片段：

```text
/config.inc.php          (Status: 200) [Size: 3952]
/config.inc.php.bak      (Status: 200) [Size: 3931]
/setup.php               (Status: 200) [Size: 1234]
/robots.txt              (Status: 200) [Size: 26]
```

解读：**`--discover-backup` 是这个场景的核心**——它在找到 `/config.inc.php` 后自动尝试 `.bak`、`.old`、`.php~` 等备份后缀。**源码备份文件泄露数据库凭据是最典型的"低成本高收益"发现**。

### 场景 3：子域名爆破

```bash
gobuster dns -d example.com \
  -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  -c --timeout 3s -t 50 --resolver 1.1.1.1 -o gobuster_dns.txt
```

预期输出片段：

```text
[+] Domain:     example.com
[+] Threads:    50
[+] Resolver:   1.1.1.1
[+] Timeout:    3s
===============================================================
www.example.com
mail.example.com
dev.example.com
===============================================================
```

**内网 DNS 的场景（内网渗透必用）**：

```bash
gobuster dns -d lab.local \
  -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  --resolver 10.0.0.1 --timeout 5s -nf -o internal_dns.txt
```

解读：
- `-c` 会同时检查 CNAME——**CNAME 指向外部服务时是"子域接管"的候选**。
- `--resolver` 是关键：内网域名必须用内网 DNS 才解析得到。
- `-nf`（no-fqdn）不加尾部点，让解析器走 search domain——内网 split-horizon 场景需要。
- **如果遇到 `Wildcard DNS detected` 提示**，说明该域配了 `*.example.com`，此时默认会停止。要强行跑就用 `-wc`，但结果里会有大量假阳性。

### 场景 4：虚拟主机爆破（发现隐藏站点）

```bash
# -u 填 IP，靠 Host 头区分站点
gobuster vhost -u http://192.168.56.101 \
  -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  --append-domain -t 30 --exclude-length 286
```

预期输出片段：

```text
Found: admin.example.lab Status: 200 [Size: 4213]
Found: intranet.example.lab Status: 200 [Size: 12984]
Found: staging.example.lab Status: 301 [Size: 0]
```

解读：
- **vhost 模式的价值**：这些站点**在 DNS 里可能根本查不到**（只在内网注册，或走通配符），但 Web 服务器根据 `Host` 头会把它们路由出来。
- `--append-domain` 让字典里的 `admin` 变成 `admin.<URL 的域名>`。
- `--exclude-length` **几乎是必须的**——因为默认站点的响应长度是固定的，不排除的话每个词都会"命中"。可以先用一次不带排除的扫描，看看默认响应的长度是多少。

### 场景 5：云存储桶枚举 + 组合工作流

```bash
# 枚举开放的 S3 桶
gobuster s3 -w bucket_names.txt -t 30 -o s3_buckets.txt

# 枚举 GCS 桶
gobuster gcs -w bucket_names.txt -t 30

# TFTP 服务器文件枚举
gobuster tftp -s 192.168.56.101 -w /usr/share/seclists/Discovery/Infrastructure/common-router-passwords.txt
```

**组合工作流（最有价值的一条）**：

```bash
# 1) gobuster 找出所有目录（含 403/401）
gobuster dir -u http://192.168.56.101 -w common.txt -e -q -o dirs.txt

# 2) 提取所有状态码为 200/301/401/403 的路径
grep -oP '(?<=^)/\S+(?=\s+\(Status)' dirs.txt | sort -u > paths.txt

# 3) 把路径喂给 whatweb / nikto 做进一步检查
while read -r p; do whatweb -a 1 "http://192.168.56.101$p" 2>/dev/null; done < paths.txt

# 4) 把 200 且是 PHP 的路径交给 sqlmap
grep -E '\(Status: 200\)' dirs.txt | grep -oP '^/\S+\.php' > php_files.txt
```

## 6. 输出解读

### 标准输出行

```text
/path                 (Status: 200) [Size: 891] [--> http://target/path/]
```

| 部分 | 含义 | 判断价值 |
|------|------|----------|
| `/path` | 发现的路径 | — |
| `Status: 200` | 存在且可访问 | **高**（尤其是管理/上传/备份类路径） |
| `Status: 301/302` | 重定向 | 高（目录）；`-->` 显示去向 |
| `Status: 401` | 需要认证 | **高**（受保护资源，说明有东西） |
| `Status: 403` | 存在但禁止 | **高**（路径真实存在，常可绕过） |
| `Size: N` | 响应体长度 | 用于识别"软 404"（长度都相同） |
| `Progress: x / y` | 进度 | — |

### 状态码优先级（渗透视角）

| 状态码 | 价值判断 |
|--------|---------|
| `200` | 直接可访问，最高价值 |
| `302/301` | 重定向到登录页/实际目录，值得跟踪 |
| `401` | 有认证，可尝试弱口令/默认凭据 |
| `403` | 路径存在，可尝试绕过（`/path/`、`/path/.`、`/path%2e/`） |
| `500` | 服务器内部错误，可能触发异常的行为（**值得单独跟进**） |
| `404` | 默认被排除 |

### 判断要点

1. **响应长度是排除假阳性的关键**：如果所有结果 `Size` 都一样，说明目标有软 404 页面。用 `-xl <长度>` 排除。
2. **403/401 不是噪声**——它们是"此处有东西"的强信号。
3. **`--discover-backup` 的收益极高**：源码备份常含数据库凭据、API key。
4. **`-x` 的扩展名要贴合技术栈**：IIS 用 `asp,aspx`；Tomcat 用 `jsp`；PHP 用 `php,inc`；前端项目加 `js,map`。

## 7. 与其他工具配合

```bash
# 1) nmap 找 Web 端口 -> gobuster 爆破
sudo nmap -p80,443,8080 --open -oG - 192.168.56.0/24 | awk '/80\/open/{print "http://"$2}' > urls.txt
while read -r u; do
  gobuster dir -u "$u" -w /usr/share/seclists/Discovery/Web-Content/common.txt -q -o "gb_$(echo $u|tr '/:' '__').txt"
done < urls.txt

# 2) gobuster 目录 -> ffuf 参数 fuzz（互补）
gobuster dir -u http://target -w common.txt -q -e | grep -oP 'http\S+(?=.*200)' > found_urls.txt
while read -r u; do ffuf -u "$u?FUZZ=test" -w params.txt -mc all -fs 0; done < found_urls.txt

# 3) gobuster 找到的文件 -> sqlmap
grep -E '\.php.*Status: 200' gb.txt | grep -oP '^/\S+\.php' | while read -r p; do
  sqlmap -u "http://target$p?id=1" --batch --smart --level 1 --risk 1
done

# 4) gobuster dns -> httpx/whatweb
gobuster dns -d example.com -w subs.txt -q | grep -oP '^[\w.-]+$' > found_subs.txt
httpx -l found_subs.txt -title -status-code -o live.txt

# 5) gobuster vhost 发现的站点 -> 加 hosts 或直接用 Host 头访问
curl -H "Host: admin.example.lab" http://192.168.56.101/
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `the server returned a status code that is not 404 for a random path` 后中止 | **预检查失败**（软 404 或 WAF 拦截） | 用 `-xl <长度>` 排除基线长度；确认 URL 正确；万不得已 `--force`（结果会很脏） |
| 结果里几乎所有词都"命中" | 软 404 / 通配符 | `-xl` 排除固定长度；检查是否被 WAF 拦成同一页面 |
| 什么都跑不出来 | URL 写错 / 需要认证 / 被 302 到登录页 | 加 `-c "session=xxx"`；用 `-r` 跟随重定向观察；先手工 `curl -I` 确认 |
| DNS 模式全无结果 | 用了公网 DNS 解析内网域名 | `--resolver <内网DNS>` |
| DNS 模式提示 Wildcard detected | 目标配了 `*.domain` | 加 `-wc`（并接受噪声），或改用 [amass](../01-信息搜集/amass.md) 的被动源 |
| vhost 模式全部命中 | 未排除默认站点响应长度 | 先跑一次看 `Size`，再加 `-xl <该长度>` |
| 速度太慢 | 线程 10 + 网络延迟 | `-t 30`~`50`；但公网目标别超过 10 |
| 被 WAF 封 IP | 请求频率太高 | `-t 5 -d 500ms`；换 UA `-rua`；走代理 `--proxy` |
| HTTPS 自签证书报错 | 证书校验失败 | `-k` |
| 想跟随重定向但结果变少/变多 | 跟随重定向会把 302 变成 200 | 用 `-r` 前先想清楚是否需要 |
| 字典太大跑不完 | 用了 100 万行的字典 | 先用 `common.txt`（4600 行）快速过一遍，再按需上大字典 |
| 扩展名爆炸导致请求量大增 | `-x` 里扩展名太多 | `-x` 每个扩展名都会让请求数 ×N，控制在 5 个以内 |
| 输出中文乱码 | 终端编码 | `--no-color` 并检查 `LANG` |

## 9. 防御视角（蓝队）

- **gobuster 的流量特征非常清晰**：
  - 单个源 IP 短时间内请求**大量不存在的路径**（绝大多数返回 404）。正常用户几乎不产生 404 风暴。
  - 请求**没有 Referer、没有静态资源加载**，User-Agent 是 `gobuster/3.8.2`（默认不改）。
  - 路径模式来自**公开字典**（SecLists 的 `common.txt`、`raft-*`），内容高度可预测。
- **检测规则建议**：
  - WAF/IDS：单源 IP 在 60 秒内 404 数量 > 100 → 告警。
  - 匹配常见爆破路径词表（`/admin`、`/backup`、`/.git/`、`/.env`、`/phpinfo.php`、`/wp-login.php`）。
  - UA 匹配 `gobuster|ffuf|dirb|wfuzz|feroxbuster`。
  - `--discover-backup` 会产生 `.bak`/`.old`/`.zip` 后缀的密集请求——**这组后缀是可以专门做规则的特征**。
- **缓解措施（按效果排序）**：
  1. **统一 404 响应**：所有不存在的路径返回**完全相同的状态码、长度、内容**。这让"按长度排除"和"软 404 检测"都失效，爆破结果会充满假阳性、变得不可用。（注意：不要用 200+友好页面——那反而让攻击者通过 `-xl` 一键过滤。）
  2. **速率限制与封禁**：对单源 IP 的请求速率设限；对高频 404 源自动临时封禁（fail2ban 之类）。
  3. **不在 Web 根目录放敏感文件**：`.git/`、`.env`、`*.bak`、`*.sql`、`*.zip`、`phpinfo.php`、测试目录——**这些是 gobuster 的主要收益来源，删掉就等于消除大部分风险**。
  4. **部署 WAF**：对 `--discover-backup`、常见管理路径做拦截（提高成本，但可被绕过）。
  5. **认证前置**：管理接口不应靠"路径难猜"来保护，应该在反向代理层要求认证。
- **特别提醒**：**`/phpMyAdmin/`、`/admin/`、`/test/` 这类"存在但 403/401"的路径是最危险的**——它们告诉攻击者"这里有东西，只是需要绕过"。真正的加固不是返回 403，而是**移除这些资源**或**在前面加认证**。
- **紫队用法**：定期用 gobuster 跑自己的资产，检查是否有不该存在的路径暴露。这比等外部报告更主动。

## 10. 参考

- 官方仓库（含每个模式的完整参数）：<https://github.com/OJ/gobuster>
- Kali 工具页：<https://www.kali.org/tools/gobuster/>
- 字典资源（Kali 自带）：<https://github.com/danielmiessler/SecLists>
- man page：`man gobuster`（只列全局参数）；**模式参数用 `gobuster help <mode>`**
- 用法核实：本教程参数取自 `gobuster 3.8.2` 的 man page，并与上游 `cli/options.go` 及 `cli/{dir,dns,vhost,fuzz,s3,gcs,tftp}/*.go` 中的实际 flag 定义交叉核对

---

**相关教程**：[ffuf](ffuf.md) ｜ [dirb](dirb.md) ｜ [wfuzz](wfuzz.md) ｜ [sqlmap](sqlmap.md) ｜ [wpscan](wpscan.md) ｜ [whatweb](../01-信息搜集/whatweb.md) ｜ [nmap](../01-信息搜集/nmap.md)
