# dirb（经典 Web 目录爆破）

> **一句话**：用自带的字典扫描 Web 服务器上存在（或隐藏）的目录与文件，并根据响应自动递归深入。
> **分类**：Web 应用 ｜ **Kali 包**：`dirb` ｜ **官方文档**：<https://dirb.sourceforge.net/>

## 1. 它解决什么问题

dirb 是目录爆破工具的"老前辈"。它做的事和 [gobuster](gobuster.md) dir 模式、[ffuf](ffuf.md) 类似，但有两个特点让它至今仍有价值：

1. **开箱即用**：`dirb http://target` 就够了——它会自动用内置字典、自动处理 404、自动递归。**零配置上手成本最低。**
2. **递归是"默认行为"**：发现目录后会**自动**用它继续扫下一层，不需要额外参数。

| 工具 | 上手难度 | 递归 | 速度 | 适合 |
|------|---------|------|------|------|
| **dirb** | 最低（一条命令） | **默认开启** | 中 | 快速摸底、教学、演示 |
| [gobuster](gobuster.md) | 低 | 需切模式/重跑 | 高 | 模式化批量任务 |
| [ffuf](ffuf.md) | 中 | 需 `-recursion` | **最高** | 复杂 fuzz 与精细过滤 |
| [wfuzz](wfuzz.md) | 中高 | 需 `-R` | 中 | 老脚本/插件生态 |

**定位**：dirb 适合**第一步快速摸底**——先用它几分钟看个大概，再用 [ffuf](ffuf.md) 对大字典、大范围做精细扫描。它的输出格式和递归行为也让它很适合写进简单的自动化脚本。

## 2. 工作原理

```text
   dirb http://192.168.56.101
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ① 加载字典                                                 │
   │    默认：/usr/share/dirb/wordlists/common.txt              │
   │    （dirb 的默认字典比 gobuster 的 common.txt 更"重"，       │
   │      包含更多常见应用路径）                                 │
   │    Kali 上还带了 /usr/share/dirb/wordlists/big.txt 等       │
   └────┬──────────────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ② 探测 404 基线                                            │
   │    请求一个随机不存在的路径，记录其特征                       │
   │    -f 可开启更精细的 NOT_FOUND 检测（减少假阳性）             │
   └────┬──────────────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ③ 逐个请求 + 判断                                           │
   │    与基线不同的响应视为"存在"，打印：                        │
   │      +  HTTP 200 OK（可访问）                              │
   │      ==> DIRECTORY: /admin/  （目录，会记入递归队列）        │
   │      --> 302（重定向），-l 会打印 Location 头                │
   │      +  HTTP 403 Forbidden（存在但禁止）                    │
   │      -N <code> 可忽略指定状态码                             │
   │      -X <ext> 扩展名：把每个词再试 word.ext                 │
   └────┬──────────────────────────────────────────────────────┘
        │
   ┌────┴──────────────────────────────────────────────────────┐
   │ ④ 递归（默认行为，-r 关闭 / -R 交互式选择）                  │
   │    对每个 ==> DIRECTORY 的目录，用同一字典再扫一遍          │
   │    → 这是 dirb 最省心也最危险的地方（可能跑很久）            │
   └────────────────────────────────────────────────────────────┘
```

几个要点：

- **`-r` 关闭递归**是控制时长的关键参数。不加会一直往下钻。
- **`-R` 交互式递归**：每发现一个目录就问你要不要扫，适合人工逐层判断。
- **`-z <毫秒>` 是请求间隔**（延迟），是被限速或不想被发现时的基本手段。
- **`-N <code>` 忽略某个状态码**：例如目标把所有不存在的路径都返回 403 时，用 `-N 403` 过滤掉。
- **`-X` 加扩展名**，如 `-X .php,.bak`（注意 dirb 的扩展名带点）。

## 3. 安装与快速上手

```bash
sudo apt install dirb
dirb --help 2>&1 | head -20   # dirb 用 -h 之外的写法：直接跑 dirb 无参会打印用法
ls /usr/share/dirb/wordlists/
```

最小可用命令：

```bash
# 1) 一条命令搞定（默认字典 + 默认递归）
dirb http://192.168.56.101

# 2) 关闭递归（只扫一层，速度快）
dirb http://192.168.56.101 -r

# 3) 加扩展名
dirb http://192.168.56.101 -X .php,.html,.bak
```

## 4. 核心参数详解

`dirb` 的用法是 `dirb <url_base> [<wordlist_file(s)>] [options]`——**字典是位置参数**，可以给多个。

| 参数 | 作用 | 建议 |
|------|------|------|
| `<url_base>` | 目标 URL | 不加协议时默认 http |
| `<wordlist_file>` | 字典文件（可多个，位置参数） | 不写则用默认字典 |
| `-a <agent>` | 自定义 User-Agent（默认 `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)`） | 换成现代浏览器 UA |
| `-b` | 不合并 URL 里的 `/../` 或 `/./` 序列 | 路径遍历测试 |
| `-c <cookie>` | 设置 Cookie | **需要登录态时必加** |
| `-E <cert>` | 客户端证书文件 | 双向 TLS |
| `-f` | **更精细的 NOT_FOUND（404）检测** | 假阳性多时加，会稍慢 |
| `-H <header>` | 添加自定义请求头 | 如 `-H "Host: example.lab"` |
| `-i` | 大小写不敏感搜索 | 目标对大小写不敏感时 |
| `-l` | 打印 `Location` 头（重定向目标） | 想知道 302 去哪了 |
| `-N <nf_code>` | **忽略指定 HTTP 状态码** | 排除干扰码，如 `-N 403` |
| `-o <file>` | 输出到文件 | 推荐 |
| `-p <proxy[:port]>` | 使用代理（默认端口 1080） | 配合 Burp |
| `-P <user:pass>` | 代理认证 | — |
| `-r` | **不递归搜索** | **控制时长的关键** |
| `-R` | **交互式递归**（逐个询问是否扫描该目录） | 人工逐层判断 |
| `-S` | 静默模式，不显示测试过的词 | 输出干净 |
| `-t` | 不强制给 URL 加尾斜杠 `/` | 默认会强制加 |
| `-u <user:pass>` | HTTP Basic 认证 | — |
| `-v` | 也显示不存在的页面（默认不显示） | **调试用**（能看出工具是否正常工作） |
| `-w` | 遇到 WARNING 不停止 | 有大字典/重复词时用 |
| `-x <extensions_file>` | 从**文件**读扩展名列表 | 扩展名多时 |
| `-X <extensions>` | 直接指定扩展名（逗号分隔） | 常用 |
| `-z <msecs>` | 请求之间的延迟毫秒数 | **限速与规避** |

**默认字典路径**：`/usr/share/dirb/wordlists/common.txt`
Kali 还提供：`big.txt`（更大）、`small.txt`、`indexes.txt`、`vulns/` 等。

## 5. 实战演练

**环境**：本地实验环境。

- Metasploitable2：`http://192.168.56.101`（内置 Mutillidae、DVWA、phpMyAdmin、WebDAV）
- DVWA 容器：`http://192.168.56.102:8080`
- 攻击机 Kali：`192.168.56.10`

> 只对授权目标爆破。dirb 默认会**递归**，在大型站点上可能跑很久——先用 `-r` 摸底。

### 场景 1：一条命令的默认扫描

```bash
dirb http://192.168.56.101 -o dirb_msf.txt
```

预期输出片段：

```text
-----------------
DIRB v2.22
By The Dark Raver
-----------------

START_TIME: Tue Sep 15 18:10:22 2026
URL_BASE: http://192.168.56.101/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612

---- Scanning URL: http://192.168.56.101/ ----
==> DIRECTORY: http://192.168.56.101/dav/
+ http://192.168.56.101/index.php (CODE:200|SIZE:891)
==> DIRECTORY: http://192.168.56.101/phpMyAdmin/
+ http://192.168.56.101/robots.txt (CODE:200|SIZE:26)
+ http://192.168.56.101/server-status (CODE:403|SIZE:288)
==> DIRECTORY: http://192.168.56.101/test/

---- Entering directory: http://192.168.56.101/dav/ ----
+ http://192.168.56.101/dav/index.html (CODE:200|SIZE:45)
==> DIRECTORY: http://192.168.56.101/phpMyAdmin/
...

-----------------
END_TIME: Tue Sep 15 18:14:03 2026
DOWNLOADED: 18448 - FOUND: 9
-----------------
```

解读：
- `==> DIRECTORY:` 标记目录，**会被加入递归队列**（下面能看到 `---- Entering directory ----`）。
- `(CODE:200|SIZE:891)` 是状态码 + 响应长度。
- `(CODE:403|SIZE:288)` 说明路径存在但禁止访问——**有价值**（例如 `/server-status` 是 Apache 状态页，403 说明它开着）。
- 末尾 `DOWNLOADED: 18448 - FOUND: 9` 是统计：**递归让实际请求数从 4612 涨到 18448**——这就是为什么大型站点要用 `-r`。

### 场景 2：不递归 + 带扩展名（快速摸底）

```bash
dirb http://192.168.56.101 -r -X .php,.txt,.bak,.zip -z 100 -o dirb_fast.txt
```

解读：
- `-r` 只扫一层，`-z 100` 每请求间隔 100ms 限速。这两个是最常用的"温和模式"。
- `-X .php,.txt,.bak,.zip` 会把 4612 个词扩展成 18448 个请求——**扩展名会让请求数线性增长**，注意控制数量。
- 发现 `.bak`/`.zip` 就是**源码/备份泄露**，价值极高。

### 场景 3：需要登录态 + 虚拟主机

```bash
# 需要登录（先从浏览器或 curl 拿到 Cookie）
dirb http://192.168.56.102:8080/ \
  -c "PHPSESSID=abc123def456; security=low" \
  -a "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" \
  -r -o dirb_dvwa.txt

# 虚拟主机：用 -H 指定 Host 头
dirb http://192.168.56.101/ -r \
  -H "Host: admin.example.lab" \
  -o dirb_vhost.txt
```

解读：`-c` 需要在**登录状态下**从浏览器 DevTools 或 `curl -i` 里拿到完整 Cookie。`-H "Host: ..."` 让 dirb 请求的是**虚拟主机**，而不是 IP 对应的默认站点。

### 场景 4：代理 + 观察流量

```bash
# 先启动 Burp（监听 8080），然后
dirb http://192.168.56.101/ -r -p 127.0.0.1:8080 -o dirb_burp.txt
```

解读：把所有请求经过 Burp，可以**在 Proxy History 里看到 dirb 发的每个请求**——这既方便调试（看清 404 基线是什么样），也是学习工具行为的好办法。同理可用于排查 WAF 拦截。

### 场景 5：处理"全是 403"的目标

```bash
# 有些服务器对任何路径都返回 403（拒绝列目录）
dirb http://target/ -r -v 2>&1 | head -30
# 如果看到所有路径都 403（包括明显不存在的随机词），说明"存在即 403"
# 这时用 -N 忽略 403，只关心其他状态码
dirb http://target/ -r -N 403 -o dirb_filtered.txt

# 或者用更精细的 404 检测
dirb http://target/ -r -f -o dirb_fine.txt
```

解读：`-v` 显示所有结果（包括不存在的），**这是确认"工具是否正常工作"的最快方式**——如果连不存在的随机路径也显示 403/200，说明基线判断失效，需要用 `-N` 或 `-f`。

## 6. 输出解读

### 结果标记

| 标记 | 含义 | 价值 |
|------|------|------|
| `+ http://... (CODE:200\|SIZE:891)` | 存在且可访问 | 高 |
| `==> DIRECTORY: http://...` | **目录**，会递归扫 | 高 |
| `+ ... (CODE:403\|SIZE:288)` | 存在但禁止访问 | **高**（路径真实存在） |
| `+ ... (CODE:301/302)` | 重定向（`-l` 显示去向） | 中高 |
| `+ ... (CODE:500)` | 服务器错误 | **值得单独跟进** |
| `---- Entering directory: ... ----` | 开始递归扫描该目录 | — |
| `!! WARNING: ...` | 警告（如字典有重复词） | `-w` 忽略 |

### 统计行

```text
DOWNLOADED: 18448 - FOUND: 9
```

| 字段 | 含义 |
|------|------|
| `DOWNLOADED` | 实际发出的请求数（**含递归产生的**） |
| `FOUND` | 被判定为"存在"的结果数 |

**`DOWNLOADED` 远大于字典行数说明递归在起作用**——这也是评估"这次扫描有多吵"的依据。

### 判断要点

1. **`FOUND` 数远小于 `DOWNLOADED` 是正常的**（大多数路径不存在）。
2. **`FOUND` 异常大**（比如等于字典行数）说明基线判断失效——用 `-v` 验证。
3. **目录（`==>`）优先看**，因为递归会带来更多发现。
4. **403 列表要逐条看**——`/server-status`、`/phpMyAdmin/`、`/.git/` 这类即使 403 也很重要。

## 7. 与其他工具配合

```bash
# 1) dirb 摸底 -> gobuster/ffuf 精扫
dirb http://192.168.56.101 -r -S -o dirb_quick.txt
grep -oP '(?<=DIRECTORY: )\S+' dirb_quick.txt > dirs.txt
while read -r d; do
  ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt \
       -u "${d}FUZZ" -mc all -ac -s
done < dirs.txt

# 2) dirb 结果 -> whatweb 指纹
grep -oP 'http://\S+(?= \(CODE:200)' dirb_quick.txt | while read -r u; do
  whatweb -a 1 "$u"
done

# 3) dirb 找到的 .php -> sqlmap
dirb http://192.168.56.101 -r -X .php -S -o dirb_php.txt
grep -oP 'http://\S+\.php(?= \(CODE:200)' dirb_php.txt | while read -r u; do
  sqlmap -u "$u?id=1" --batch --smart --level 1 --risk 1
done

# 4) 统计各状态码的分布
grep -oP 'CODE:\d+' dirb_msf.txt | sort | uniq -c | sort -rn

# 5) 用 Burp 代理跑一遍，Proxy History 里复盘所有请求
dirb http://192.168.56.101/ -r -p 127.0.0.1:8080
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| 跑了很久停不下来 | **递归默认开启**，一层层往下钻 | `-r` 关闭；或用 `-R` 交互式逐层确认 |
| 结果里几乎每条都"命中" | 目标对不存在的路径也返回 200/403（软 404） | `-N <该状态码>` 忽略；`-f` 精细 404 检测；`-v` 先确认基线 |
| 想扫更深但没递归 | 用了 `-r` | 去掉 `-r`；或对已发现的目录单独再跑一次 |
| 明确存在的路径没扫出来 | 字典太小 / 扩展名没加 | 换 `big.txt`；用 `-X` 加扩展名 |
| 需要登录但全是 302 到 login | Cookie 未正确传入 | `-c` 里给完整 Cookie；用 `-l` 看 Location 确认被重定向到哪 |
| 被 WAF 拦成 403 风暴 | 请求太快 | `-z 500` 加延迟；`-a` 换 UA；`-p` 走代理 |
| 中文路径/编码问题 | dirb 较老，对非 ASCII 支持一般 | 改用 [ffuf](ffuf.md) 并配 `-enc` |
| `-X` 后请求量爆炸 | 扩展名让请求数 ×N | 控制扩展名数量；用 `-r` 减少递归放大 |
| 输出里 `!! WARNING` 后停止 | 字典里有重复/异常词 | `-w` 忽略警告继续 |
| HTTPS 自签证书失败 | 证书校验 | dirb 没有 `-k` 类参数；可先用 `-p` 代理，或改用 [ffuf](ffuf.md) `-k`/`gobuster` `-k` |
| 想扫描非标准端口 | URL 里写端口即可 | `dirb http://target:8080/` |
| 单位时间发现太多，输出刷屏 | 未静默 | `-S` |

## 9. 防御视角（蓝队）

dirb 的流量特征与 [gobuster](gobuster.md)、[ffuf](ffuf.md) 同属一类，但有几个**独有的指纹**：

| 特征 | 说明 |
|------|------|
| **默认 User-Agent** | `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)`——**这是 2001 年的 IE6 UA**，现代浏览器绝不会用。这是**极高置信度的检测点**。 |
| **默认字典特征** | dirb 的 `common.txt` 有其特定的词序与内容（含大量应用路径） |
| **递归带来的请求倍增** | 同一源 IP 对同一站点的**多级路径**产生密集 404（`/a/b/c` 形态） |
| **URL 尾部斜杠** | dirb 默认会强制给 URL 加 `/`（`-t` 可关），产生特定形态的请求 |

### 检测规则建议

```text
# 1) 最简单有效的一条：UA 匹配
- User-Agent 精确匹配 "MSIE 6.0; Windows NT 5.1"

# 2) 404 风暴
- 单源 IP 60s 内 404 数量 > 100

# 3) 递归特征：多级路径的密集 404
- 同一 IP 对 /a/b/* 形态路径的请求数异常

# 4) 敏感路径词表
- 路径匹配 (\.git/|\.env|\.bak|\.old|admin|backup|phpinfo|server-status|wp-login)
```

### 缓解措施

1. **统一 404 响应**：所有不存在的路径返回**完全一致**的状态码 + 长度 + 内容。这会让 dirb 的基线检测失效或产生大量假阳性。
   - 注意：**不要返回 200 + 友好页面**——那反而让攻击者一条 `-N 200` 或 `-fs <len>` 就把噪声清干净了，而真实结果仍然清晰可辨。返回 404 + 一致短响应才是最优。
2. **限制请求速率**：网关/WAF 单源限速；对 404 风暴源自动封禁（fail2ban 结合 Nginx access log）。
3. **校验 Host 头**：反代只接受已知域名，其他返回 444。这能废掉 `-H "Host: ..."` 类和 vhost 爆破。
4. **移除敏感资源**：`.git/`、`.env`、`*.bak`、`*.zip`、`server-status`、测试目录。**这些是 dirb 的主要收益来源。**
5. **管理路径前置认证**：不要依赖"路径难猜"或 403 来保护管理接口。
6. **记录并告警 UA**：IE6 UA 在现代流量里占比应该接近 0，出现即告警——**这是投入产出比最高的一条规则**。

### 紫队用法

```bash
# 自查：我的站点在常见字典下会暴露什么？
dirb https://my-site.example -r -S -o selfaudit.txt
# 关注：CODE:200 的路径、DIRECTORY 标记、任何 .bak/.zip/.git
```

## 10. 参考

- 项目主页：<https://dirb.sourceforge.net/>
- Kali 工具页：<https://www.kali.org/tools/dirb/>
- 自带字典目录：`ls /usr/share/dirb/wordlists/`
- man page：`man dirb`（简要）；直接运行 `dirb` 不带参数会打印用法
- 用法核实：本教程参数取自 Debian 包 `dirb 2.22` 的 man page

---

**相关教程**：[gobuster](gobuster.md) ｜ [ffuf](ffuf.md) ｜ [wfuzz](wfuzz.md) ｜ [sqlmap](sqlmap.md) ｜ [whatweb](../01-信息搜集/whatweb.md)
