# mitmproxy（HTTP/HTTPS 中间人代理）

> **一句话**：一个能拦截、查看、修改、重放 HTTP 和 HTTPS 流量的交互式中间人代理，是分析 Web 应用与 API 的瑞士军刀。
> **分类**：嗅探与欺骗 ｜ **Kali 包**：`mitmproxy`（含 `mitmdump`、`mitmweb`）｜ **官方文档**：<https://mitmproxy.org>

## 1. 它解决什么问题

Wireshark 能看所有协议，但**看不了 HTTPS 的内容**（TLS 加密）。而现代 Web 应用几乎全是 HTTPS。

**mitmproxy 解决的就是这个问题**——它充当**有证书的中间人**：

```
[客户端] ──── TLS（信任 mitmproxy 的 CA）───→ [mitmproxy]
                                                  │ 解密 → 明文分析
                                                  │ 重新加密
                                                  ↓
[服务器] ←──── TLS（真实证书）────────────── [mitmproxy]
```

**它提供三个程序**：

| 程序 | 界面 | 用途 |
| --- | --- | --- |
| **`mitmproxy`** | 交互式 TUI（终端界面） | ⭐ 手动分析、逐条查看、修改 |
| **`mitmdump`** | 无界面（命令行） | ⭐ **脚本化、自动化、管道** |
| **`mitmweb`** | Web UI（浏览器） | 图形化分析，适合不熟悉 TUI 的人 |

**与[ettercap](ettercap.md) / [bettercap](../05-无线攻击/bettercap.md) 的定位区别**：

| | mitmproxy | ettercap / bettercap |
| --- | --- | --- |
| 层级 | **应用层**（HTTP/HTTPS/HTTP2/WebSocket） | **网络层**（ARP 投毒 + 任意协议嗅探） |
| 加密 | ⭐ **自己伪造证书解密** | 需要证书才能解 SSL |
| 修改内容 | ⭐⭐ **非常灵活**（Python 脚本） | etterfilter（声明式，受限） |
| 重放 | ⭐ **有 Replay 功能** | 无 |
| 协议范围 | HTTP(S) 为主（+ 任意 TCP） | 所有 IP 协议 |

**关键理解**：

> **mitmproxy 不负责「把流量引导过来」**。它只是一个代理服务器——**客户端必须主动把流量发给它**。
>
> 要让客户端的流量自动经过 mitmproxy，需要配合：
> - 客户端手工设置代理（**最简单，完全合法**）；
> - 透明代理（需要 iptables 重定向，通常配合 ARP 投毒或网关位置）；
> - PAC 文件 / WPAD（见 [responder](responder.md)）；
> - 客户端 App 的代理配置。

**⭐ 最合法也最实用的场景**：**在自己的设备上设置代理，分析自己的流量**。这是抓包分析、API 调试、移动 App 逆向的常规做法。

## 2. 工作原理

### 2.1 三种代理模式

| 模式 | 客户端如何配置 | 说明 |
| --- | --- | --- |
| **Regular（常规代理）** | 客户端**显式设置** HTTP 代理地址 | ⭐ **最常用、最简单、最透明** |
| **Transparent（透明代理）** | 客户端**不知道**有代理 | 需要 iptables 重定向；配合 ARP 投毒/网关 |
| **Reverse（反向代理）** | 无需客户端配置，直接连 mitmproxy | 用于代理单个后端服务 |
| **Upstream（上游代理）** | mitmproxy 自己再走一个代理 | 链路式代理 |
| **SOCKS5** | 客户端用 SOCKS5 代理 | — |
| **WireGuard** | 通过 WireGuard 隧道接入 | 适合移动设备 |

**Regular 模式的流量路径**：

```
[客户端（设置了代理 127.0.0.1:8080）]
        ↓
   发 HTTP 请求给 127.0.0.1:8080（请求行里是完整 URL）
        ↓
[mitmproxy]
   ├─ 解析请求
   ├─ 如果是 HTTPS：对客户端伪装成目标服务器（用自签证书）
   └─ 转发给真实服务器
        ↓
[真实服务器]
```

**⭐ 为什么 Regular 模式最简单**：客户端**明确知道**自己在用一个代理，所以：

- 代理地址和端口是明明白白配置的；
- **不需要 ARP 投毒、不需要修改网络**；
- HTTP 请求里带完整 URL（`GET http://example.com/path HTTP/1.1`）。

### 2.2 证书是核心

**HTTPS 的拦截完全依赖于「客户端信任 mitmproxy 的 CA」**：

```
为什么能解密：
  1. mitmproxy 生成一对自己的 CA 证书（首次运行时）
  2. 你把 mitmproxy 的 CA 装进客户端的信任库
  3. 客户端发 HTTPS 请求时，mitmproxy 用「为这个域名临时签发的证书」应答
  4. 客户端校验这个证书 → 发现是由「受信任的 mitmproxy CA」签发的 → ✅ 接受
  5. 于是客户端与 mitmproxy 之间是 TLS；mitmproxy 与服务器之间是另一个 TLS
  6. mitmproxy 在中间能看明文

为什么解不开：
  1. 客户端不信任 mitmproxy 的 CA → 客户端看到证书错误 → ❌ 连接失败
  2. App 用了「证书固定」（pinning）→ 即使 CA 被信任，App 也只接受特定的证书 → ❌
  3. 客户端使用 mTLS（双向证书）→ 无法伪装 → ❌
```

**⭐ 这三条「解不开」的原因，正好对应三项防御措施**：

| 防御 | 效果 |
| --- | --- |
| **不安装未知 CA** | 用户培训 + 设备管理策略（MDM 不允许装用户 CA） |
| **证书固定（certificate pinning）** | App 内置特定证书/公钥，即使 CA 被信任也不接受 |
| **mTLS（客户端证书）** | 双向认证，中间人无法提供有效的客户端证书 |
| 加上 **HSTS** | 强制 HTTPS，阻止降级到 HTTP |

**首次运行时生成的证书文件**：

```bash
ls -la ~/.mitmproxy/
# mitmproxy-ca.pem              ← CA 证书（用于安装）
# mitmproxy-ca-cert.pem         ← 同上（PEM 格式）
# mitmproxy-ca-cert.cer         ← DER 格式（Windows/Android 用）
# mitmproxy-ca-cert.p12         ← PKCS#12（Windows 导入用）
# mitmproxy-ca-cert.pcap        ← pcap 格式
# mitmproxy-ca-cert.pem
# mitmproxy-ca-key.pem          ← ⚠️ 私钥（绝不要泄露）
```

**⭐ 安装到客户端**：

| 客户端 | 方法 |
| --- | --- |
| **Linux（系统级）** | `sudo cp ~/.mitmproxy/mitmproxy-ca-cert.pem /usr/local/share/ca-certificates/mitmproxy.crt && sudo update-ca-certificates` |
| **Firefox（独立信任库）** | 设置 → 隐私与安全 → 证书 → 查看证书 → 导入 → 选 `mitmproxy-ca-cert.pem` → 勾选「信任由此 CA 标识的网站」 |
| **Chrome/Chromium** | 用系统信任库（Linux 上按上面第 1 条即可） |
| **Windows** | 双击 `mitmproxy-ca-cert.p12` → 导入到「受信任的根证书颁发机构」 |
| **macOS** | 导入到钥匙串，然后在证书详情里设为「始终信任」 |
| **Android** | 设置 → 安全 → 加密与凭据 → 从存储安装 → 选 `.cer`（⚠️ **Android 7+ 后用户 CA 不被 App 信任**，见下） |
| **iOS** | 安装描述文件，然后在「设置 → 通用 → 关于本机 → 证书信任设置」中**手动启用** |
| **curl** | `curl --cacert ~/.mitmproxy/mitmproxy-ca-cert.pem ...` 或 `curl -x http://127.0.0.1:8080 --proxy-insecure` |

**⚠️ Android 7+ 的重要限制**：

> 从 Android 7（API 24）开始，**App 默认只信任系统 CA，不信任用户安装的 CA**。
>
> 这意味着：**即使你装了 mitmproxy 的证书，App 的 HTTPS 流量依然无法拦截**。
>
> 这是**故意的安全设计**——它让「在手机上装个证书就能抓 App 流量」变得困难。

**绕过这个限制的方法**（按侵入性排序）：

| 方法 | 侵入性 | 前提 |
| --- | --- | --- |
| 用 `mitmproxy` 抓**浏览器**流量 | 低 | 浏览器信任用户 CA |
| 用**抓包 App 自己的代理设置**（如果支持） | 低 | App 支持 |
| 修改 APK（改 `network_security_config.xml`） | 中 | 需要重打包 + 重签名 |
| **用 root 把 CA 装到系统信任库** | 高 | 需要 root |
| 用 Frida/Objection 绕过 pinning | 高 | 需要 root + 逆向能力 |

**⭐ 这些都是「改变客户端信任配置」的操作**——在授权测试中**必须明确写在 ROE 里**，且**不应以规避检测为目的**。

### 2.3 拦截与修改

mitmproxy 的核心能力是**在请求/响应经过时拦截并修改**：

```
[客户端] ──── 请求 ────→ [mitmproxy 拦截] ──── 修改后转发 ────→ [服务器]
                              ↑
                    可以：改方法、改 URL、改 header、改 body
                    
[客户端] ←─── 响应 ───── [mitmproxy 拦截] ←──── 服务器响应 ──── [服务器]
                              ↑
                    可以：改状态码、改 header、改 body
```

**交互式（TUI）中的按键**：

| 按键 | 作用 |
| --- | --- |
| `i` | **设置拦截过滤器** |
| `a` | 放行（accept） |
| `A` | 放行所有（accept all） |
| `r` | **编辑当前请求/响应**（会打开编辑器） |
| `e` | 编辑某个字段 |
| `d` | 删除 |
| `R` | **Replay**（重放） |
| `Enter` | 查看详情 |
| `Tab` | 在请求/响应/详情之间切换 |
| `q` | 返回 / 退出 |
| `?` | 帮助 |

**编辑 `r`** 会调用 `$EDITOR`（Vim 默认）打开一个临时文件，你可以直接改请求行、header、body，保存后 mitmproxy 用修改后的内容转发。

**⚠️ 这个功能很强，但也容易被滥用**：
- 修改**自己的**请求：完全正常（API 测试、参数探测）；
- 修改**别人的**请求：这是主动篡改他人数据（对应 etterfilter 那条法律章节）。

### 2.4 脚本化（mitmproxy 的真正威力）

**mitmproxy 提供完整的事件驱动的 Python API**。一个脚本长这样：

```python
# add_header.py —— 给所有请求加一个 header
from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    flow.request.headers["X-Debug"] = "1"

def response(flow: http.HTTPFlow) -> None:
    print(f"{flow.request.method} {flow.request.pretty_url} -> {flow.response.status_code}")
```

用法：

```bash
mitmdump -s add_header.py
```

**常用事件钩子**：

| 钩子 | 触发时机 |
| --- | --- |
| `request(flow)` | 收到请求（转发前） |
| `response(flow)` | 收到响应（返回客户端前） |
| `http_connect(flow)` | HTTP CONNECT（HTTPS 建隧道时） |
| `tls_clienthello(data)` | 客户端 TLS ClientHello（可以看 SNI） |
| `error(flow)` | 连接错误 |
| `load(l)` / `done()` | 脚本加载/卸载 |
| `websocket_message(flow)` | WebSocket 消息 |

**⭐ 这让 mitmproxy 从「一个抓包工具」变成「一个可编程的 HTTP 处理框架」**——你可以用它做：

| 用途 | 说明 |
| --- | --- |
| **自动化 API 测试** | 对每个响应做断言 |
| **批量修改请求/响应** | 注入 header、改参数 |
| **提取特定数据** | 从响应里提取 token/JSON 字段 |
| **流量统计** | 统计 API 调用、错误率、耗时 |
| **重放与模糊测试** | 结合 Replay 与脚本 |

### 2.5 Replay 与保存

| 功能 | 说明 |
| --- | --- |
| **保存流量** | `-w flows.mitm`（mitmproxy 自有格式） |
| **读取流量** | `-r flows.mitm` |
| **Replay 客户端请求** | `-C flows.mitm` |
| **Replay 服务器响应** | `-S flows.mitm` |
| **交互式 Replay** | TUI 里按 `R` |
| **导出为其他格式** | 用 `--set save_stream_file=` 或脚本 |

**⭐ Replay 的实用价值**：

| 场景 | 说明 |
| --- | --- |
| **复现问题** | 保存一次失败请求，反复重放调试 |
| **API 测试** | 抓一次真实请求，改参数后重放，看服务端如何反应 |
| **模糊测试** | 重放 + 脚本自动改参数 |

**Replay 服务器响应**（`-S`）特别有用：

```
把服务器响应缓存下来，之后离线重放
→ 前端开发时不需要后端在线
→ 或者观察「相同请求不同响应的差异」
```

### 2.6 mitmdump 的过滤器

`mitmdump` 支持**过滤器表达式**（与 TUI 里的 `f` 相同语法）：

| 过滤器 | 含义 |
| --- | --- |
| `~u example.com` | URL 匹配 |
| `~u /api/` | URL 路径匹配 |
| `~m POST` | 方法匹配 |
| `~c 200` | 状态码匹配 |
| `~t application/json` | Content-Type 匹配 |
| `~h "Host: example"` | Header 匹配 |
| `~b "password"` | Body 匹配 |
| `~q` | 匹配请求 |
| `~s` | 匹配响应 |
| `!~u static` | 取反 |

**用法**：

```bash
mitmdump '~u example.com & ~m POST'
```

## 3. 安装与快速上手

```bash
sudo apt install mitmproxy
mitmproxy --version
mitmdump --help | head -40
```

**最短工作流（分析自己的浏览器流量）**：

```bash
# 1) 启动代理（默认监听 8080）
mitmproxy
# 或 mitmweb（Web UI）
# 或 mitmdump（无界面）

# 2) 让浏览器走这个代理
#    Firefox: 设置 → 网络设置 → 手动配置代理 → HTTP 代理 127.0.0.1:8080
#    或命令行启动：
#    chromium --proxy-server=127.0.0.1:8080

# 3) 安装 CA 证书
#    浏览器访问 http://mitm.it  → 按平台下载安装证书

# 4) 在 mitmproxy 界面里看流量
```

**⭐ `http://mitm.it` 是官方提供的证书下载页**——只要流量经过了 mitmproxy，访问这个地址就能按平台下载证书。**这是最方便的安装方式。**

**用环境变量让命令行工具走代理**：

```bash
export http_proxy=http://127.0.0.1:8080
export https_proxy=http://127.0.0.1:8080
# 或者用 curl 的 -x
curl -x http://127.0.0.1:8080 --proxy-insecure https://example.com
```

## 4. 核心参数详解

> 三个程序（`mitmproxy` / `mitmdump` / `mitmweb`）的**大部分参数完全相同**。下面以 `mitmdump` 为准，差异在最后标注。

### 4.1 通用选项

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `-h, --help` | 帮助 | — |
| `--version` | 版本 | — |
| `--options` | 列出所有选项及默认值 | ⭐ **探索工具的最佳入口** |
| `--commands` | 列出所有命令及签名 | — |
| `--set <option>[=<value>]` | 设置选项 | ⭐ 最灵活的配置方式 |
| `--mode, -m <MODE>` | 代理模式（可多次指定） | 见 4.3 |
| `-q, --quiet` | 安静 | — |
| `-v, --verbose` | 提高日志详细度 | 排错用 |
| `-r, --rfile <PATH>` | **从文件读 flows** | 离线分析 |
| `-w, --save-stream-file <PATH>` | **把 flows 流式写入文件** | 前缀 `+` 表示追加；支持 `strftime` 格式 |
| `-s, --scripts <SCRIPT>` | **加载 Python 脚本**（可多次） | ⭐ mitmproxy 的威力所在 |
| `--anticache` / `--no-anticache` | 去掉可能触发 304 的请求头 | ⭐ **调试验证码/缓存问题时很有用** |
| `--showhost` / `--no-showhost` | 用 Host 头构造 URL | 默认关闭（防恶意 Host 头误导分析） |
| `--show-ignored-hosts` | 记录被忽略的 flows | 注意：会大量增加内存 |
| `--stickycookie <FILTER>` | 粘性 cookie 过滤器 | — |
| `--stickyauth <FILTER>` | 粘性认证过滤器 | — |
| `--anticomp` / `--no-anticomp` | 让服务器返回未压缩数据 | ⭐ **改 body 前必须开**（否则内容是 gzip） |
| `--flow-detail <LEVEL>` | **显示详细级别**：`0`安静 / `1`URL+状态码 / `2`+headers / `3`+截断 body / `4`全部 | ⭐ `mitmdump` 用 `2` 最合适 |

**⭐ `--anticache` 的用途**：当你**重放**或**修改请求**时，服务器可能返回 `304 Not Modified`（因为带了 `If-None-Match`/`If-Modified-Since`）。`--anticache` 会去掉这些头，**强制服务器返回完整内容**。

### 4.2 代理选项

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `--listen-host <HOST>` | 监听地址 | 想让别的设备连进来时设为 `0.0.0.0`（⚠️ 注意暴露风险） |
| `--listen-port, -p <PORT>` | **监听端口**（默认 8080） | ⭐ 最常用 |
| `--server` / `--no-server, -n` | 是否启动代理服务器（默认启用） | `-n` 用于纯离线脚本处理 |
| **`--ignore-hosts <HOST>`** | **忽略这些主机**（直接转发，不处理） | ⭐⭐ **非常重要**！见下 |
| `--allow-hosts <HOST>` | 只处理这些主机（`ignore-hosts` 的反面） | — |
| `--tcp-hosts <HOST>` | 通用 TCP SSL 代理模式 | 拦截非 HTTP 的 TLS 流量 |
| `--upstream-auth <USER:PASS>` | 给上游代理加 HTTP Basic 认证 | — |
| `--proxyauth <SPEC>` | **要求客户端代理认证** | ⭐ 生产部署时必用 |
| `--store-streamed-bodies` | 保存流式 body | 会增加内存 |
| `--rawtcp` / `--no-rawtcp` | 是否支持原始 TCP | — |
| `--http2` / `--no-http2` | 是否支持 HTTP/2 | — |

**⭐⭐ `--ignore-hosts` 是最重要的一个参数。** 为什么：

> **不要把不该拦截的流量也拦下来。**
>
> mitmproxy 会为**每一个** HTTPS 域临时签证书、做中间人解密。这带来：
> - **性能开销**（每个连接两次 TLS 握手）；
> - **安全风险**（你的机器上会流过大量解密后的敏感流量）；
> - **兼容性问题**（有些客户端会因证书问题报错）；
> - **法律问题**（拦截了与你测试目标无关的流量）。
>
> **正确做法**：**只拦截你要分析的目标**。

```bash
# 只拦截 example.com，其他全部直通
mitmproxy --allow-hosts 'example\.com'

# 或者：忽略一堆不该碰的（如银行、软件更新、遥测）
mitmproxy --ignore-hosts '(.*\.apple\.com|.*\.microsoft\.com|.*\.googleapis\.com|.*bank.*)'
```

**⭐ 推荐用 `--allow-hosts`（白名单）而不是 `--ignore-hosts`（黑名单）** —— 白名单更安全。

### 4.3 代理模式（`-m` / `--mode`）

| 模式 | 写法 | 用途 |
| --- | --- | --- |
| **Regular** | `regular`（默认） | ⭐ 客户端显式设置代理 |
| **Local** | `local` | 拦截本机进程的流量（无需设置代理） |
| **Transparent** | `transparent` | 客户端不知情（需 iptables 重定向） |
| **Reverse** | `reverse:http://host:port` | 反向代理到某个后端 |
| **Upstream** | `upstream:http://proxy:port` | 链路式代理 |
| **SOCKS5** | `socks5` | SOCKS5 代理 |
| **WireGuard** | `wireguard[:PATH]` | WireGuard 隧道 |

**可以为某个模式指定不同的监听端口**：

```bash
mitmdump -m regular@8080 -m socks5@1080
```

### 4.4 SSL / 证书选项

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `--certs <SPEC>` | 指定证书（格式 `[domain=]path`） | 用固定证书代替自动生成 |
| `--cert-passphrase <PASS>` | 证书私钥的口令 | ⚠️ **命令行上会出现在进程列表里**——用配置文件代替 |
| `--ssl-insecure, -k` | **不验证上游服务器证书** | ⭐ 上游有用自签证书时用 |
| `--no-ssl-insecure` | 验证上游证书（默认） | — |

**⚠️ `-k`（`--ssl-insecure`）的风险**：

```
开启后，mitmproxy 不校验证书链
→ 它自己会成为一个「可被中间人」的端点
→ 如果上游是对手控制的，你分析的数据可能是假的
```

**⭐ 只在明确知道上游用了自签证书（如内部测试环境）时用 `-k`。**

### 4.5 重放选项

| 参数 | 作用 |
| --- | --- |
| `--client-replay, -C <PATH>` | **重放客户端请求**（可多次） |
| `--server-replay, -S <PATH>` | **重放服务器响应**（可多次） |
| `--server-replay-kill-extra` | 重放时杀掉没有对应响应的请求（已废弃，用 `server_replay_extra`） |
| `--server-replay-extra {forward,kill,204,400,404,500}` | 没有可重放响应时的行为 |
| `--server-replay-reuse` | 响应可重复使用 |
| `--server-replay-refresh` | 刷新响应里的日期/过期头 |

### 4.6 映射与修改（命令行版）

| 参数 | 作用 | 格式 |
| --- | --- | --- |
| `--map-remote, -M <PATTERN>` | 把远程 URL 映射到另一个远程 URL | `[/flow-filter]/url-regex/replacement` |
| `--map-local <PATTERN>` | 把远程 URL 映射到本地文件 | `[/flow-filter]/url-regex/file-or-dir` |
| `--modify-body, -B <PATTERN>` | **修改响应体** | `[/flow-filter]/regex/[@]replacement`（`@` 表示替换值来自文件） |
| `--modify-headers, -H <PATTERN>` | **修改 header** | `[/flow-filter]/header-name/[@]header-value`（value 为空表示删除该 header） |

**这些参数非常实用**——**不需要写脚本就能做常见的修改**：

```bash
# 把 example.com 的所有请求映射到本地目录（前端 Mock）
mitmdump --map-local '/~u example\.com/api/(.*)/tmp/mocks/\1'

# 修改响应体（把 "production" 换成 "staging"）
mitmdump --modify-body '/~u example\.com/production/staging'

# 加一个 header
mitmdump --modify-headers '/~u example\.com/X-Debug/1'

# 删除一个 header
mitmdump --modify-headers '/~u example\.com/Server/' 
```

### 4.7 三个程序的差异

| | `mitmproxy` | `mitmdump` | `mitmweb` |
| --- | --- | --- | --- |
| 界面 | 交互式 TUI | 无（纯输出） | Web UI |
| 独有参数 | `--console-layout {horizontal,single,vertical}`、`--console-layout-headers` | `--flow-detail <0-4>` | `--web-port`、`--web-host`、`--web-open-browser` |
| 独有过滤器 | `--intercept FILTER`、`--view-filter FILTER` | — | `--intercept FILTER` |

### 4.8 mitmproxy TUI 的常用按键

| 按键 | 作用 |
| --- | --- |
| `?` | 帮助 |
| `q` | 返回上一级 |
| `Q` | 退出（需确认） |
| `f` | **设置显示过滤器** |
| `i` | **设置拦截过滤器** |
| `a` | 放行 |
| `A` | 放行所有 |
| `r` | 编辑当前 flow |
| `e` | 编辑字段 |
| `d` | 删除 flow |
| `R` | **Replay** |
| `Enter` | 查看 flow 详情 |
| `Tab` | 切换（请求/响应/详情） |
| `z` | 清空 |
| `m` | 标记 |
| `w` | 保存 flows |

## 5. 实战演练

**环境声明**：以下所有操作**都在你自己的设备上、分析你自己的流量**。这是 mitmproxy 的**标准用法**，完全合法。

**⚠️ 只有当你要分析**别人的**流量时，才需要证书安装到别人设备上——那必须有书面授权。**

### 场景 1：分析自己的浏览器流量（最标准、最合法）

**步骤 1：启动 mitmproxy**

```bash
mitmproxy --listen-port 8080
```

**预期输出**

```
Loading 1 script...
Loaded 0 flows.
Listening at http://*:8080
```

**步骤 2：配置浏览器代理**

**Firefox**（推荐，因为它的证书信任库独立）：

```
设置 → 网络设置 → 手动代理配置
  HTTP 代理:  127.0.0.1  端口 8080
  HTTPS 代理: 127.0.0.1  端口 8080
  ☑ 也将此代理用于 HTTPS
```

**Chromium（命令行）**：

```bash
chromium --proxy-server=127.0.0.1:8080
```

**步骤 3：安装 CA 证书**

在浏览器里访问：

```
http://mitm.it
```

**预期页面**：显示各平台（Apple / Windows / Android / Firefox / Linux）的证书下载链接。

| 平台 | 说明 |
| --- | --- |
| **Firefox** | 点 Firefox 下载 `.pem`，然后在浏览器里：设置 → 隐私与安全 → 证书 → 查看证书 → 导入 → 选该文件 → 勾选「信任由此 CA 标识的网站」 |

**⭐ 你也可以直接用 `http_proxy` 环境变量让命令行工具走代理**——但注意 `curl` 需要 `--proxy-insecure` 或指定 `--cacert`：

```bash
curl -x http://127.0.0.1:8080 --proxy-insecure https://example.com
# 或者
curl -x http://127.0.0.1:8080 --cacert ~/.mitmproxy/mitmproxy-ca-cert.pem https://example.com
```

**步骤 4：在 TUI 里查看流量**

mitmproxy 界面分三部分：

```
┌──────────────────────────────────────────────────────────────┐
│ 1  GET  https://example.com/                    ← flow 列表   │
│ 2  POST https://api.example.com/login                        │
│ 3  GET  https://cdn.example.com/style.css                    │
├──────────────────────────────────────────────────────────────┤
│ GET / HTTP/1.1                     ← 请求详情（按 Enter 后）  │
│ Host: example.com                                            │
│ User-Agent: Mozilla/5.0 ...                                  │
│ Accept: text/html,...                                        │
├──────────────────────────────────────────────────────────────┤
│ HTTP/1.1 200 OK                    ← 响应详情                │
│ Content-Type: text/html                                        │
│ Content-Length: 1256                                          │
└──────────────────────────────────────────────────────────────┘
```

**常用操作**：

| 按键 | 做什么 |
| --- | --- |
| `f` | 过滤（例如 `~u api` 只看 API） |
| `Enter` | 进入某个 flow 的详情 |
| `Tab` | 在「请求 / 响应 / 详情」之间切换 |
| `q` | 返回 |

**步骤 5：过滤只看 API 流量**

按 `f`，输入：

```
~u /api/
```

或者要过滤 JSON 响应：

```
~t application/json
```

**⭐ 这是分析 API 的最高效方式**——把静态资源（CSS/JS/图片）过滤掉，只看 API 调用。

### 场景 2：拦截并修改请求（API 测试）

**步骤 1：设置拦截过滤器**

在 TUI 里按 `i`，输入：

```
~u /api/login
```

**⭐ 此后只有匹配这个过滤器的请求会被拦截**——其他流量正常通过。

**步骤 2：触发一个被拦截的请求**

在浏览器里登录一个测试应用。

**⭐ 此时浏览器会「卡住」**——因为请求被 mitmproxy 拦下了，等你决定。

**步骤 3：放行或修改**

| 按键 | 作用 |
| --- | --- |
| `a` | 放行（原样转发） |
| `A` | 放行所有（取消拦截） |
| **`r`** | **编辑**（打开 $EDITOR） |

**按 `r` 会打开编辑器**（默认 Vim），内容类似：

```
POST /api/login HTTP/1.1
Host: app.example.com
Content-Type: application/json
Content-Length: 42

{"username":"alice","password":"wrong"}
```

**改内容**（例如把 `wrong` 改成 `correct`），保存退出，mitmproxy 就会用修改后的内容转发。

**⚠️ 如果 body 是 gzip 压缩的**，你会看到乱码。此时需要**启动时加 `--anticomp`**：

```bash
mitmproxy --anticomp
```

**⭐ 这就是「修改自己的请求」的标准用法**——用于：

| 用途 | 说明 |
| --- | --- |
| **越权测试** | 改 `user_id` 看能不能访问别人的数据 |
| **参数探测** | 改参数看服务端如何反应 |
| **绕过客户端校验** | 客户端校验只是「用户体验」，服务端必须独立校验 |
| **测试边界值** | 改数字、改长度、改类型 |

**⭐⭐ 关键安全原则**：

> **「改请求能成功」不是 mitmproxy 的问题，而是服务端的漏洞。**
>
> 如果改 `user_id` 就能访问别人的数据，那是**服务端缺少授权校验**（对应 OWASP 的 **BOLA/IDOR**）。
> mitmproxy 只是把这个问题**暴露出来**。

### 场景 3：用 mitmdump 做脚本化分析

**步骤 1：写一个统计脚本**

```python
# stats.py —— 统计 API 调用与错误率
from mitmproxy import http
import collections

stats = collections.Counter()
errors = []

def response(flow: http.HTTPFlow) -> None:
    url = flow.request.pretty_url
    # 只看 API
    if "/api/" not in url:
        return

    path = flow.request.path.split("?")[0]
    status = flow.response.status_code
    stats[f"{flow.request.method} {path} -> {status}"] += 1

    if status >= 400:
        errors.append({
            "method": flow.request.method,
            "url": url,
            "status": status,
        })

def done():
    print("\n===== API 调用统计 =====")
    for key, n in stats.most_common():
        print(f"{n:5d}  {key}")

    print("\n===== 错误请求 =====")
    for e in errors:
        print(f"{e['status']}  {e['method']} {e['url']}")
```

**步骤 2：运行**

```bash
mitmdump -s stats.py -q
```

**步骤 3：在浏览器里操作应用，然后在 mitmdump 里按 `Ctrl+C`**

**预期输出**

```
===== API 调用统计 =====
   45  GET /api/users -> 200
   23  POST /api/login -> 200
   12  GET /api/orders -> 200
    8  GET /api/admin/settings -> 403     ← ⚠️ 403 多次，值得关注
    3  GET /api/users/9999 -> 404

===== 错误请求 =====
403  GET https://app.example.com/api/admin/settings
404  GET https://app.example.com/api/users/9999
```

**⭐ 这个脚本的价值**：

| 发现 | 说明 |
| --- | --- |
| 大量的 403 | 可能有权限问题，或者有人在探测越权 |
| 404 于 `/api/users/9999` | 可能在枚举用户 ID |
| 异常的 API 路径 | 可能有未公开的接口 |

**这是「用 mitmproxy 做安全分析」的核心形态**——**把流量变成可统计的数据**。

### 场景 4：保存流量并离线重放

**步骤 1：保存流量**

```bash
mitmdump -w /tmp/session.mitm -q
# 操作应用产生流量
# Ctrl+C
```

**步骤 2：离线读取**

```bash
# 用 TUI 打开
mitmproxy -r /tmp/session.mitm

# 或用 mitmdump 过滤查看
mitmdump -r /tmp/session.mitm '~u /api/ & ~m POST' --flow-detail 2
```

**步骤 3：重放客户端请求（`-C`）**

```bash
# 把之前保存的请求重放一遍（对服务器再发一次）
mitmdump -r /tmp/session.mitm -C /tmp/session.mitm
```

**⚠️ 重放会真的向服务器发请求**——注意不要对生产系统做有副作用的重放（如「删除」请求）。

**步骤 4：重放服务器响应（`-S`，用于 Mock）**

```bash
# 用保存的响应来响应新请求（不再访问真实服务器）
mitmdump -S /tmp/session.mitm
```

**⭐ 这个功能的实用场景**：

| 场景 | 说明 |
| --- | --- |
| **前端开发** | 后端不在线时用缓存的响应 |
| **离线测试** | 不依赖真实服务 |
| **对比分析** | 相同请求不同响应的差异 |

### 场景 5：命令行修改（不写脚本）

```bash
# 1) 加一个 header
mitmdump --modify-headers '/~u example\.com/X-Debug/1'

# 2) 删除 Server header
mitmdump --modify-headers '/~u example\.com/Server/'

# 3) 替换响应体里的字符串
mitmdump --modify-body '/~u example\.com/v1\.0/v2\.0'

# 4) 把某个 API 映射到本地文件（Mock）
mkdir -p /tmp/mock
echo '{"status":"mocked"}' > /tmp/mock/status.json
mitmdump --map-local '/~u example\.com/api/status/tmp/mock/status.json'

# 5) 把请求映射到另一个服务器（测试环境切换）
mitmdump --map-remote '/~u api\.example\.com/https://api.staging.example.com'
```

**⭐ 这些参数让 mitmproxy 变成一个「HTTP 层的瑞士军刀」**——不需要写脚本就能做常见修改。

### 场景 6：抓取移动 App 的流量（自己的设备）

**⚠️ 前提**：手机是**你自己的**。

**步骤 1：让 mitmproxy 监听所有接口**

```bash
mitmproxy --listen-host 0.0.0.0 --listen-port 8080
```

**⚠️ 安全警告**：

> `--listen-host 0.0.0.0` 会让**网络里任何设备**都能连到你的 8080 端口。
> - 在公共网络上**绝不要这样做**；
> - 只在**隔离实验网络**（如你自己的手机热点）里用；
> - **强烈建议加 `--proxyauth`**：

```bash
mitmproxy --listen-host 0.0.0.0 --listen-port 8080 \
  --proxyauth 'myuser:mypassword'
```

**步骤 2：在手机上设置代理**

```
设置 → WLAN → 长按当前网络 → 修改网络 → 高级 → 代理 → 手动
  主机名: <你的Kali IP>
  端口:   8080
```

**步骤 3：在手机上安装 CA 证书**

1. 手机浏览器访问 `http://mitm.it`；
2. 下载对应平台的 `.cer`；
3. 安装（Android：设置 → 安全 → 加密与凭据 → 从存储安装；iOS：安装描述文件后**还要在「证书信任设置」里手动启用**）。

**步骤 4：观察流量**

**⭐ 现实预期**：

| 流量类型 | 能否抓 |
| --- | --- |
| 浏览器（Chrome/Safari）的 HTTPS | ✅ **通常可以** |
| **Android 7+ 的 App HTTPS** | ⚠️ **多数不可以**（App 只信任系统 CA） |
| 用了证书固定的 App | ❌ **不可以** |
| 用 mTLS 的 App | ❌ **不可以** |
| 明文 HTTP 的 App | ✅ 可以 |

**看到的现象**：

```
如果 App 抓不到：
  - mitmproxy 里可能只看到 CONNECT 请求（然后连接失败）
  - App 可能报「网络错误」
  → 这正说明「证书固定」或「只信任系统 CA」起作用了
```

**⭐ 这几条「抓不到」的原因就是防御措施**：

| 你抓不到的原因 | 对应的防御 |
| --- | --- |
| App 只信任系统 CA | **Android 7+ 的默认安全设计** |
| 证书固定 | **App 内置了特定证书/公钥** |
| mTLS | **双向认证** |
| TLS 1.3 + ECH | 隐藏 SNI |

**⭐ 重要提醒**：

> **在手机上安装 mitmproxy 的 CA 会显著降低该设备的安全性** ——
> 因为此后**任何**持有那个 CA 私钥的人都能拦截这台设备的 HTTPS。
>
> **测试完成后应该：**
> 1. 卸载 CA 证书；
> 2. 移除代理设置；
> 3. 如果是测试专用设备，最好直接重置。

### 场景 7：透明代理模式（配合网络位置）

**⚠️ 这一节涉及「让客户端不知情地走代理」——需要你在网络中有相应位置。**

**前提**：你在**你自己控制的**网络（例如你的实验室路由器）上。

**步骤 1：配置 iptables 重定向**

```bash
# 启用 IP 转发
sudo sysctl -w net.ipv4.ip_forward=1

# 把出方向的 HTTP/HTTPS 重定向到 mitmproxy
# ⚠️ 注意：要排除 mitmproxy 自己产生的流量，否则会死循环
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 \
  -j REDIRECT --to-ports 8080
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 \
  -j REDIRECT --to-ports 8080

# 排除本机流量（避免死循环）
sudo iptables -t nat -A OUTPUT -m owner --uid-owner <mitmproxy用户> -j RETURN
```

**步骤 2：以透明模式启动 mitmproxy**

```bash
mitmproxy --mode transparent --listen-port 8080
```

**步骤 3：客户端仍需信任 CA**

**⭐ 关键点**：**透明模式只解决「流量如何到达 mitmproxy」，不解决「证书信任」**。

> 客户端**仍然必须信任 mitmproxy 的 CA**，否则 HTTPS 会失败。
>
> 透明模式的「透明」只体现在**客户端不需要配置代理**，而不是「不需要信任证书」。

**透明模式的三种典型部署位置**：

| 位置 | 说明 | 合法性 |
| --- | --- | --- |
| **你自己的实验室网关** | 你在网关上跑 mitmproxy | ✅ 合法（你自己的网络） |
| **公司网关（有授权）** | 企业安全设备做 TLS 检查 | ⚠️ 需要**明确授权 + 告知用户** |
| ARP 投毒 + 透明代理 | 攻击者位置 | ❌ **未授权即违法**（见 [ettercap](ettercap.md)） |

**⭐ 企业做 TLS 检查的合规要点**：

```text
1. 有明确的政策（写在员工手册/隐私政策里）
2. 有告知机制
3. 有例外清单（银行、医疗、个人邮箱等应排除）
4. 有访问审计
5. 数据处理合规
```

## 6. 输出解读

### TUI 的 flow 列表

```
     #  Method  URL                                     Code  Size
     1  GET     https://example.com/                     200   1.2k
     2  POST    https://api.example.com/login            200   345
     3  GET     https://cdn.example.com/app.js           304   0
     4  GET     https://api.example.com/users/123        403   89
     ∞  GET     https://static.example.com/logo.png     200   4.5k
```

| 列 | 含义 | 关注点 |
| --- | --- | --- |
| `#` | flow 编号 | 引用时用 |
| `Method` | HTTP 方法 | — |
| `URL` | 完整 URL | — |
| **`Code`** | **状态码** | ⭐ 4xx/5xx 是重点 |
| `Size` | 响应大小 | — |
| `∞` | 表示这个 flow 还在进行中 | — |

### 状态码速查（分析时的重点）

| 状态码 | 含义 | 分析价值 |
| --- | --- | --- |
| 200 | 成功 | — |
| **301/302** | 重定向 | 看跳转到哪里 |
| 304 | 未修改 | 缓存命中（用 `--anticache` 可以避免） |
| **401** | 未认证 | 认证失败 |
| **403** | **已认证但无权限** | ⭐ **越权测试的关键** |
| 404 | 不存在 | 可能在枚举资源 |
| **500** | 服务端错误 | ⭐ **可能触发了 bug**（输入异常导致崩溃） |
| 502/503 | 网关/服务不可用 | — |

**⭐ 安全测试中最关注的是 200/403 的对比**：

```
场景：改请求里的 user_id
  user_id=123 → 200（自己的数据）
  user_id=124 → 200 ⚠️ 别人的数据也返回了 → 越权漏洞（IDOR）
  user_id=124 → 403 ✅ 正确拒绝
```

### 请求/响应详情

mitmproxy 会展示完整的 HTTP 报文：

```
                GET /api/users/123 HTTP/1.1
                Host: api.example.com
                User-Agent: Mozilla/5.0
                Authorization: Bearer eyJhbGciOi...
                Accept: application/json

                HTTP/1.1 200 OK
                Content-Type: application/json; charset=utf-8
                Content-Length: 245

                {"id":123,"username":"alice","email":"alice@example.com"}
```

**⚠️ 注意 `Authorization: Bearer eyJ...`** —— 这是 **JWT**。mitmproxy 会把它完整显示出来。

**⭐ 这本身就是一个安全提醒**：

> **任何能看到你 HTTP 流量的人都能看到你的 token。**
> 在公共 Wi-Fi 上不设代理，但攻击者可以做 ARP 投毒——
> **这就是为什么必须用 HTTPS（让 token 加密）+ 为什么不能有 HSTS 降级。**

**mitmproxy 还提供 JWT 的自动解析**——在详情里会展开 JWT 的 header/payload（虽然不验证签名）。

### mitmdump 的输出

```bash
mitmdump --flow-detail 2
```

**`--flow-detail` 的级别**：

| 级别 | 输出内容 |
| --- | --- |
| `0` | 什么都不打印（安静） |
| `1` | 简化的请求 URL + 响应状态码 |
| `2` | 完整 URL + 状态码 + HTTP headers |
| `3` | `2` + 截断的响应内容（截断阈值 512 行） |
| `4` | `3` + 不截断任何内容 |

**示例（level 2）**：

```
GET https://api.example.com/users/123
                 ← 请求头
                 Host: api.example.com
                 Authorization: Bearer ...
                 
                 ← 响应
                 200 OK
                 Content-Type: application/json
```

### 常见现象与判读

| 现象 | 含义 | 处理 |
| --- | --- | --- |
| 只看到 `CONNECT` 后就没了 | 客户端拒绝了你的证书 | 装 CA；或者 App 有证书固定 |
| 页面提示「证书无效」 | 客户端不信任 mitmproxy CA | 安装 CA |
| **只在 HTTP 有效，HTTPS 报错** | 同上 | 同上 |
| 响应体是乱码 | gzip 压缩 | 加 `--anticomp` |
| 返回 304 而不是内容 | 缓存 | 加 `--anticache` |
| 看不到某个 App 的流量 | 证书固定 / 只信任系统 CA / mTLS | 见 2.2 节的说明 |
| 上游返回证书错误 | 上游是自签证书 | 加 `-k`（`--ssl-insecure`） |
| 部分资源加载失败 | CDN 用了不同的证书 | 检查 `--ignore-hosts` 设置 |

**判断成功**：

| 目标 | 成功标志 |
| --- | --- |
| 代理生效 | mitmproxy 里出现 flow |
| HTTPS 解密 | 能看到请求/响应的明文内容（不是 `<binary>`） |
| 拦截生效 | 客户端请求「卡住」，等待你按 `a` 或 `r` |
| 脚本生效 | 脚本里的 `print()` 有输出 |
| 保存成功 | `-w` 指定的文件存在且非空 |

**下一步**：

| 情况 | 动作 |
| --- | --- |
| 看到敏感的明文凭据/token | **记录为安全问题**（为什么没加密？） |
| 发现 403 频繁出现 | 检查是否有越权问题 |
| 发现异常的 API 路径 | 记录为「未公开接口」风险点 |
| 需要批量分析 | 写 Python 脚本（`-s`） |
| 需要给报告留证据 | `-w` 保存 flows，但**注意其中含凭据** |

## 7. 与其他工具配合

```text
┌──── 流量引导层（三选一）──────────────────────────┐
│ ① 客户端手工设置代理（⭐ 最简单、最合法）          │
│ ② 透明代理（iptables 重定向，需网络位置）          │
│ ③ ARP 投毒 + 透明代理（⚠️ 仅自有/授权网络）        │
└──────────────────┬───────────────────────────────┘
                   ↓
┌──── 拦截与分析层 ────────────────────────────────┐
│ mitmproxy（TUI 手动分析）                        │
│ mitmdump（脚本化、自动化）                       │
│ mitmweb（Web UI）                               │
│   ├─ 拦截与修改（i / r）                         │
│   ├─ 保存 flows（-w）→ 离线重放（-r）            │
│   ├─ Replay（R / -C / -S）                       │
│   └─ Python 脚本（-s）⭐ 核心能力                │
└──────────────────┬───────────────────────────────┘
                   ↓
┌──── 深度分析层 ──────────────────────────────────┐
│ 脚本 → JSON/CSV → jq / python                    │
│ Wireshark（看 TLS 层的细节）                     │
│ 手动测试（改参数、测越权）                        │
└──────────────────────────────────────────────────┘
```

| 组合 | 说明 |
| --- | --- |
| **mitmproxy ↔ [Wireshark](wireshark.md)** | ⭐ **互补**。mitmproxy 看 HTTP 应用层；Wireshark 看 TCP/TLS 层。**Wireshark 甚至可以读 mitmproxy 的密钥日志**（用 `SSLKEYLOGFILE` 或设置 `--set tls_version_client_min=...`） |
| **mitmproxy ↔ [ettercap](ettercap.md)** | ettercap 提供 ARP 投毒 + 网络层嗅探；mitmproxy 提供应用层的精细控制。**可以串联**（ettercap 把流量引到 mitmproxy） |
| **mitmproxy ↔ [responder](responder.md)** | responder 的 WPAD 模块可以让浏览器**自动**把流量发到你的代理——**这曾经是一个非常有效的组合**（现在多被 HSTS 阻断） |
| **mitmproxy ↔ [bettercap](../05-无线攻击/bettercap.md)** | bettercap 做 MITM 与流量重定向；mitmproxy 做应用层分析 |
| **mitmproxy → [hashcat](../04-口令攻击/hashcat.md)** | 如果抓到哈希（如 NTLM）→ 离线破解 |
| **mitmproxy ↔ [curl](wireshark.md)** | ⭐ **用 curl 复现 mitmproxy 里看到的请求**——这是最实用的组合 |
| **[macchanger](macchanger.md)** | 改 MAC（注意：这不是为了规避检测） |

**⭐ 与 curl 的组合特别值得展开**：

mitmproxy 的 TUI 里按 `Enter` 进入某个 flow，然后可以**复制整个请求**。之后在终端里用 curl 复现：

```bash
# 从 mitmproxy 复制出来的请求，用 curl 复现
curl -X POST https://api.example.com/login \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGciOi...' \
  -d '{"username":"alice","password":"test"}'
```

**为什么这很有用**：

| 用途 | 说明 |
| --- | --- |
| **精确复现** | curl 参数明确，便于记录和分享 |
| **自动化** | curl 能写进脚本 |
| **对比测试** | 改一个参数，看服务端如何反应 |
| **报告取证** | curl 命令是可复现的证据 |

**⭐ 「mitmproxy 观察 → curl 复现 → 改参数测试」是 Web 安全测试的黄金流程。**

## 8. 常见坑与排错

### 8.1 证书问题（最常见）

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| 浏览器提示「您的连接不是私密连接」 | **CA 未安装或未信任** | 访问 `http://mitm.it` 下载安装 |
| 只在 HTTP 有效，HTTPS 全失败 | 同上 | 同上 |
| **curl 报证书错误** | curl 用系统信任库，不认 mitmproxy CA | `--cacert ~/.mitmproxy/mitmproxy-ca-cert.pem` 或 `--proxy-insecure` |
| **Firefox 仍报证书错误** | Firefox 用**独立信任库**，不受系统影响 | 在 Firefox 里单独导入 |
| 装完证书还是不行（Android） | ⭐ **Android 7+ 只信任系统 CA** | 见 2.2 节的说明（需 root 或改 APK） |
| iOS 装了描述文件还是不行 | ⭐ **iOS 需要在「证书信任设置」里手动启用** | 设置 → 通用 → 关于本机 → 证书信任设置 → 打开对应开关 |
| 某个 App 抓不到 | **证书固定（pinning）** | 这是**防御措施生效**，不是 bug |

**⭐ 证书问题的自查清单**：

```text
[ ] 访问 http://mitm.it 能打开吗？（能打开说明代理生效）
[ ] 对应平台的证书装了吗？
[ ] 装完后**重启浏览器/App**了吗？
[ ] 是 Firefox 吗？（它用独立信任库）
[ ] 是 iOS 吗？（需要在「证书信任设置」里启用）
[ ] 是 Android 7+ 吗？（只信任系统 CA）
```

### 8.2 代理配置问题

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| mitmproxy 里一个 flow 都没有 | 客户端没真正走代理 | 检查代理设置；`curl -x` 测试 |
| 只能看到本机程序的流量 | 别的设备没配代理 | 用 `--listen-host 0.0.0.0`（⚠️ 注意安全） |
| `Address already in use` | 8080 被占用 | 换端口 `-p 8081`；或 `ss -tlnp \| grep 8080` |
| 客户端连不上代理 | 防火墙挡了 | `sudo ufw allow 8080`；或检查 `--listen-host` |
| **客户端设置代理后完全上不了网** | mitmproxy 挂了，或代理地址错 | 检查 mitmproxy 是否在跑；用 IP 而不是 hostname |
| 连接**死循环** | mitmproxy 自己也走了代理 | 确保 mitmproxy 自己的流量不走自己的代理 |

### 8.3 内容显示问题

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| **响应体是乱码** | gzip 压缩 | ⭐ `--anticomp` |
| 返回 304 而不是内容 | 缓存（带了 `If-None-Match`） | ⭐ `--anticache` |
| 响应显示 `<binary>` | 二进制内容（图片/字体） | 正常——用 `--flow-detail` 或过滤掉 |
| HTTP/2 流量显示异常 | 协议解析问题 | `--no-http2`（退到 HTTP/1.1） |
| WebSocket 看不到内容 | 需要专门查看 | 脚本里用 `websocket_message` 钩子 |
| 大文件导致内存爆掉 | 流式 body 被完整加载 | `--no-store-streamed-bodies` |

### 8.4 上游问题

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `Certificate verify failed`（上游） | 上游用了自签证书 | `-k`（`--ssl-insecure`）⚠️ 注意风险 |
| 上游超时 | 网络问题 | 检查网络；或 `--set connection_timeout=` |
| 部分域名的请求失败 | 客户端固定了证书 | 正常（防御生效） |
| 想拦截非 HTTP 的 TLS | 需要通用 TCP 模式 | `--tcp-hosts` |

### 8.5 脚本问题

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `No module named mitmproxy` | 脚本没跑在 mitmproxy 的环境里 | 用 `mitmdump -s script.py` 而不是 `python script.py` |
| 脚本报错但 mitmproxy 继续跑 | 默认不中断 | 看错误输出；用 `-v` 提高详细度 |
| 改 body 不生效 | content-encoding 是 gzip | `--anticomp`；或在脚本里解压再改 |
| 脚本里拿不到 `flow.response` | 在 `request` 钩子里访问了 response | `response` 只在 `response` 钩子里有 |
| 想对同一 flow 做多次修改 | 单次事件 | 用 `flow.intercept()` 暂停 |

### 8.6 安全相关（重要）

| 风险 | 缓解 |
| --- | --- |
| **`--listen-host 0.0.0.0` 暴露代理** | ⭐ **加 `--proxyauth user:pass`**；只在隔离网络用 |
| 在公共 Wi-Fi 上开着 `0.0.0.0` | ❌ **绝对不要** |
| **CA 私钥泄露** | `~/.mitmproxy/mitmproxy-ca-key.pem` **绝不要提交到 git、绝不外传** |
| flows 文件含凭据 | `-w` 保存的文件**含明文 token/密码** → 加密存储、限期删除 |
| 长期留着手机上的 CA | ⭐ **测试完就卸载** |
| 用 `-k` 导致自己可被 MITM | 只在必要且明确知道上游是自签时用 |

**⭐ 关于 CA 私钥**：

```bash
ls -la ~/.mitmproxy/mitmproxy-ca-key.pem
```

**这个文件的重要性**：

> **持有它的人可以为任意域名签发证书**（只要受害者信任这个 CA）。
>
> 如果它泄露了：
> 1. 攻击者可以为你的银行域名签证书；
> 2. 任何信任了这个 CA 的设备都会被劫持；
> 3. **这不只是「你的数据泄露」，而是「所有信任该 CA 的设备的通信都变得可被伪造」**。

**保护措施**：

```bash
chmod 600 ~/.mitmproxy/mitmproxy-ca-key.pem

# .gitignore（如果 mitmproxy 相关文件在工作目录）
cat >> .gitignore <<'EOF'
.mitmproxy/
*.mitm
mitmproxy-ca*.pem
EOF
```

**⭐ 如果 CA 私钥泄露了怎么办**：

```
1. 立即在所有设备上卸载该 CA 证书
2. 删除 ~/.mitmproxy/ 并重新生成
3. 重新安装新 CA
4. 检查是否有异常流量
```

## 9. 防御视角（蓝队）

mitmproxy 是**测试人员的工具**，但它的存在也给出了**一份防御清单**。

### 9.1 攻击链与对策

```
mitmproxy 能成功解密 HTTPS 的前提链：
  ① 客户端设置了代理（或流量被重定向）        ← 对策 A
  ② 客户端信任了 mitmproxy 的 CA              ← 对策 B
  ③ 客户端没有证书固定（pinning）              ← 对策 C
  ④ 没有 mTLS（双向认证）                     ← 对策 D
  ⑤ 没有 HSTS 阻止降级                        ← 对策 E

断掉任何一环，mitmproxy 就抓不到内容。
```

**⭐ 完整的防御（需要多环配合）**：

| 对策 | 措施 | 有效性 |
| --- | --- | --- |
| **A** | 网络分段 + 禁止未授权代理 | ⚠️ 中（用户可自设代理） |
| **B** | ⭐ **不允许在受管设备上安装用户 CA**（MDM 策略） | ✅ 高 |
| **C** | ⭐⭐ **证书固定（certificate pinning）** | ✅ **最高** |
| **D** | mTLS（客户端证书） | ✅ 高 |
| **E** | **HSTS（含 preload）** | ✅ 高 |
| 附加 | **SRI（子资源完整性）** | ✅ 防内容篡改 |
| 附加 | **CSP** | ✅ 防注入脚本执行 |

### 9.2 最重要的三条

```text
1. 移动 App 启用证书固定（pinning）
   → 让「装个 CA 就能抓 App」失效
   → 这是对抗 mitmproxy 最有效的手段

2. 不在受管设备上允许安装用户 CA
   → 通过 MDM 策略禁止
   → 这是 corporate 环境的标准做法

3. 全站 HSTS（含 preload）
   → 阻止任何降级到 HTTP 的尝试
   → 也防止通过 HTTP 引导到假代理
```

### 9.3 具体配置

**① 证书固定（Android）**

```xml
<!-- res/xml/network_security_config.xml -->
<network-security-config>
    <domain-config>
        <domain includeSubdomains="true">api.example.com</domain>
        <pin-set expiration="2027-12-31">
            <pin digest="SHA-256">AAAA...=</pin>   <!-- 主证书的公钥哈希 -->
            <pin digest="SHA-256">BBBB...=</pin>   <!-- 备用（轮换用） -->
        </pin-set>
    </domain-config>
</network-security-config>
```

**⭐ 关键点**：

| 要点 | 说明 |
| --- | --- |
| **必须有备用 pin** | 否则证书轮换时 App 全部失效 |
| **必须设置 `expiration`** | 避免「忘了轮换导致 App 永久失联」 |
| **pin 的是公钥的哈希，不是证书** | 证书轮换时只要公钥不变就不需要发新版 App |
| 用 **HPKP 风格的备份机制** | 避免单点故障 |

**② 证书固定（iOS）**

```swift
// 使用 URLSession 的 delegate 校验证书
func urlSession(_ session: URLSession,
                didReceive challenge: URLAuthenticationChallenge,
                completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {

    guard let serverTrust = challenge.protectionSpace.serverTrust,
          let certificate = SecTrustGetCertificateAtIndex(serverTrust, 0) else {
        completionHandler(.cancelAuthenticationChallenge, nil)
        return
    }

    // 计算公钥哈希，与内置的 pin 比对
    let serverPublicKey = SecCertificateCopyKey(certificate)
    let serverKeyData = SecKeyCopyExternalRepresentation(serverPublicKey!, nil)! as Data
    let serverHash = SHA256.hash(data: serverKeyData)

    guard pinnedHashes.contains(serverHash) else {
        completionHandler(.cancelAuthenticationChallenge, nil)
        return
    }
    completionHandler(.useCredential, URLCredential(trust: serverTrust))
}
```

**③ 桌面/Web 侧**

```
# HSTS（必须包含 preload 才完整）
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload

# 提交到 HSTS preload 列表
# https://hstspreload.org/

# CSP（防注入脚本执行）
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-...'

# SRI（防子资源篡改）
<script src="https://cdn.example.com/lib.js"
        integrity="sha384-..." crossorigin="anonymous"></script>
```

**④ 企业终端管理**

| 措施 | 说明 |
| --- | --- |
| **MDM 策略：禁止安装用户 CA** | ⭐ 核心措施 |
| 证书信任库审计 | 定期检查设备上是否有多余的 CA |
| 禁用浏览器自动代理发现（WPAD） | 组策略 |
| 强制代理（或禁止绕过代理） | 有代理的环境 |
| 证书透明度（CT）监控 | 发现为你的域名签发的异常证书 |
| 设备合规检查 | 不合规设备拒绝接入 |

**⭐ 「禁止安装用户 CA」为什么是关键**：

> 如果能自由安装 CA，那么 mitmproxy（以及任何持私钥的人）就能解密这台设备上的**所有** HTTPS 流量。
>
> 这不仅是「测试人员能抓包」，更是「任何持有私钥的人都能抓包」。

### 9.4 检测

**mitmproxy 的行为是有痕迹的**：

| 检测点 | 方法 |
| --- | --- |
| **异常 CA** | ⭐ **审计设备的证书信任库**，找出非标准的 CA |
| **证书颁发者异常** | ⭐ 服务端日志里看到证书链中有奇怪的中介 CA |
| **代理配置** | 检测终端上的系统代理设置（`gsettings get org.gnome.system.proxy mode`） |
| **PAC 文件** | 检测系统中是否配置了 WPAD/PAC |
| **网络拓扑异常** | 检测异常的 ARP、路由、透明代理 |
| **TLS 指纹** | ⭐ **JA3/JA4 指纹**——mitmproxy 的 TLS 指纹与真实浏览器不同 |
| **证书透明度日志** | ⭐ 监控 CT 日志中为你的域名签发的异常证书 |

**⭐ TLS 指纹（JA3/JA4）是一个很实用的检测手段**：

```
浏览器访问你的站点 → JA3 = <浏览器的指纹>
mitmproxy 代理访问你的站点 → JA3 = <mitmproxy/OpenSSL 的指纹>

如果服务端看到「Chrome 的 User-Agent」但「OpenSSL 的 JA3」→ 说明中间有代理
```

**证书透明度（CT）监控**：

```bash
# 查询 CT 日志中为你的域名签发的证书
# 有在线工具与 API（如 crt.sh）
curl -s "https://crt.sh/?q=example.com&output=json" | \
  python3 -c "import json,sys; [print(c['issuer_name'], c['name_value']) for c in json.load(sys.stdin)]" | \
  sort -u | head -20
```

**⭐ 如果 CT 日志里出现了你没有申请过的证书——那是一个高优先级的安全事件。**

**服务端侧的检测脚本思路**：

```bash
# 从 Web 服务器日志里提取 TLS 指纹（需要服务器支持 JA3 记录）
# Nginx：需要编译 ngx_http_ssl_fingerprint 模块
# 之后可以统计 JA3 分布，发现异常指纹
```

### 9.5 一个重要的认知

**mitmproxy 的价值在于它展示了一件事**：

> **HTTPS 的安全性完全依赖于「信任链的完整性」。**
>
> 一旦信任链被破坏（装了不该装的 CA），**HTTPS 就等于 HTTP**。
>
> 这就是为什么：
> - 「装个证书就能抓 App」是**设计上的**问题（Android 7+ 已经修复）；
> - **证书固定**是移动安全的基本要求；
> - **不在设备上装用户 CA** 是企业安全的红线。

**⭐ 另一点**：

> **mitmproxy 也能抓「明文 HTTP」**——而且**不需要装任何证书**。
>
> 如果你的应用还在用 HTTP 传凭据（Basic 认证、明文表单），那**不需要任何攻击技巧就能被嗅探**。

**因此最基础的防御是**：

```text
1. 全站 HTTPS（没有例外）
2. 全站 HSTS（含 preload）
3. 移动 App 证书固定
4. 不在受管设备上允许用户 CA
```

## 10. 参考

- 官方站点：<https://mitmproxy.org>
- **官方文档**：<https://docs.mitmproxy.org/>
- 官方仓库：<https://github.com/mitmproxy/mitmproxy>
- **脚本 API 文档**：<https://docs.mitmproxy.org/stable/addons-overview/>
- 证书安装指南：<https://docs.mitmproxy.org/stable/concepts-certificates/>
- Kali 工具页：<https://www.kali.org/tools/mitmproxy/>
- 本机帮助：`mitmproxy -h`、`mitmdump -h`、`mitmweb -h`
- **查看全部选项**：`mitmdump --options`
- **查看全部命令**：`mitmdump --commands`
- 证书目录：`~/.mitmproxy/`
- 证书下载页（运行时常量）：`http://mitm.it`
- 相关本目录：[wireshark](wireshark.md)（含 tshark）、[tcpdump](tcpdump.md)、[ettercap](ettercap.md)、[responder](responder.md)、[macchanger](macchanger.md)
- 相关其他目录：[bettercap](../05-无线攻击/bettercap.md)、[hashcat](../04-口令攻击/hashcat.md)

## ⚠️ 法律与伦理

**mitmproxy 的法律性质取决于「你拦截的是谁的流量」。**

| 场景 | 合法性 |
| --- | --- |
| ✅ **在自己的设备上设置代理，分析自己的流量** | **完全合法**——这是标准的开发/测试做法 |
| ✅ 在**你自己的**实验环境里分析你自己的 App | 合法 |
| ✅ 有**书面授权**的渗透测试（明确授权目标与范围） | 合法 |
| ⚠️ 企业做 TLS 检查 | 需要**明确政策 + 告知用户 + 例外清单 + 合规的数据处理** |
| ❌ **在别人的设备上装 CA 并拦截** | **违法** |
| ❌ **用 ARP 投毒把别人流量引到你的代理** | **违法**（见 [ettercap](ettercap.md)） |
| ❌ 在公共 Wi-Fi 上开着 `0.0.0.0` 的开放代理 | 违法且极度危险 |

**特别警告**：

> **`~/.mitmproxy/mitmproxy-ca-key.pem` 是一个「万能钥匙」。**
>
> 拥有它就能为**任意域名**签发证书——只要受害者信任这个 CA。
>
> **如果这个私钥泄露：**
> - 攻击者可以为你的网银域名签发假证书；
> - 任何信任该 CA 的设备（可能是你手机上的所有 App）都会被劫持。
>
> **这不是「你的数据泄露」，而是「所有信任该 CA 的设备的通信都变得可伪造」。**
>
> 因此：
> - **绝不外传该私钥**；
> - **绝不提交到 git**；
> - **测试完成后从设备上卸载 CA**；
> - **定期审计设备上是否有多余的 CA**。

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条 | **非法侵入计算机信息系统罪** / **非法获取计算机信息系统数据罪** |
| 《刑法》 | 第二百八十六条 | 破坏计算机信息系统罪（修改他人流量） |
| 《刑法》 | 第二百五十三条之一 | **侵犯公民个人信息罪**（截获通信内容、凭据） |
| 《刑法》 | 第二百六十六条 | 诈骗罪（若用假代理做钓鱼） |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《个人信息保护法》 | 相关条款 | 截获、处理个人信息的合法性基础 |
| 《数据安全法》 | 相关条款 | 数据处理活动的合规要求 |

**本教程仅适用于**：

- ✅ **你自己的设备、你自己的流量**（这是 mitmproxy 最标准、也最有价值的用法）
- ✅ 你自己搭建的隔离实验环境
- ✅ 有**书面授权**、明确列出授权目标的渗透测试
- ✅ 移动 App 逆向/测试，且**设备是你自己的**（或客户授权的测试设备）

**严禁**：

- ❌ 在别人的设备上安装 CA 证书
- ❌ 用 ARP 投毒 / WPAD 把他人流量引到你的代理
- ❌ 在公共网络上开放 `0.0.0.0` 的代理
- ❌ 保留、分析、分享他人流量的 flows 文件
- ❌ 泄露 CA 私钥
- ❌ 把 flows 文件（含明文 token/密码）提交到代码仓库

**使用前的强制检查清单**：

```text
[ ] 这个代理只服务于我自己的设备吗？
[ ] 我用的 --listen-host 是 127.0.0.1 还是 0.0.0.0？
    → 如果是 0.0.0.0，我加了 --proxyauth 吗？在隔离网络里吗？
[ ] 我拦截的范围是否用 --allow-hosts 限定在测试目标内？
[ ] ~/.mitmproxy/mitmproxy-ca-key.pem 的权限是 600 吗？
[ ] 我保存的 flows 文件（含凭据）准备好怎么处理了吗？
[ ] 测试结束后我会卸载设备上的 CA 吗？
```

**任何一项打不上勾，就不要运行。**

**最安全的学法（也是最有价值的用法）**：

```text
⭐⭐ 在自己的设备上设置代理，分析自己的 Web 应用/API 流量
   → 这完全合法，而且是开发/测试的标准做法
   → 能学到：HTTP/HTTPS 解析、拦截修改、脚本化、Replay
   → 覆盖了 100% 的知识点

✅ 用 mitmdump -s 写脚本做流量统计与分析
✅ 用 -w 保存 flows，用 -r 离线分析（不接触任何网络）
✅ 读证书固定的文档，理解为什么它是必要的
```

**最后一句**：**mitmproxy 是最好的「理解 HTTPS 信任模型」的教学工具**——它让你亲眼看到「信任一个 CA 意味着什么」。学会用它之后，你会更谨慎地对待每一个要求你「安装证书」的提示。
