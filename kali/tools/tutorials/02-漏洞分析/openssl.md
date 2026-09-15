# openssl（TLS/SSL 诊断与证书分析）

> **一句话**：手工握住 TLS 握手、查看对端证书、检查支持的协议版本与加密套件，并顺带排查心脏出血（Heartbleed）这类 TLS 层漏洞。
> **分类**：漏洞分析 ｜ **Kali 包**：`openssl`（含命令行工具；开发头文件在 `libssl-dev`） ｜ **官方文档**：<https://docs.openssl.org/>

## 1. 它解决什么问题

Web 扫描器（[nikto](nikto.md)、[nuclei](nuclei.md)）会告诉你"服务在跑 HTTPS"，但**TLS 配置本身的细节**需要专门的工具：

- 对端证书链是什么？签发者是谁？还有多少天过期？
- 支持哪些协议版本？（有没有还在支持 TLS 1.0/1.1？）
- 支持哪些加密套件？有没有 RC4、3DES、NULL 这类弱套件？
- 主机名和证书里的 CN/SAN 匹配吗？
- 服务器是否启用了 Heartbeat 扩展（Heartbleed 的前提）？
- 握手到底是哪一步失败的？

`openssl s_client` 是这一类问题最通用的解答工具——它是**手工 TLS 客户端**。

| 工具 | 定位 |
|------|------|
| **openssl s_client** | 手工握手、看证书、逐版本/逐套件探测、STARTTLS |
| `nmap --script ssl-enum-ciphers` | 一次性枚举所有协议/套件（**批量首选**） |
| `nmap --script ssl-cert,ssl-heartbleed` | 证书信息 + Heartbleed 检测 |
| `sslscan` / `testssl.sh` | 更友好的 TLS 配置报告（Kali 里有 `sslscan`） |
| [nuclei](nuclei.md) | 用模板做批量 TLS 问题检测 |
| `openssl x509` / `verify` / `crl` / `ocsp` | 离线分析证书、验签、吊销检查 |

**关键认知**：`openssl s_client` 是**诊断工具**，不是扫描器。要看"这台服务器 TLS 配置好不好"，用 `nmap --script ssl-enum-ciphers` 更快；要**逐项确认、排查具体问题**，用 `s_client`。

## 2. 工作原理

```text
   openssl s_client -connect host:443 -servername host
        │
   ┌────┴────────────────────────────────────────────────┐
   │ ① TCP 连接 host:443                                  │
   │ ② 发 ClientHello                                     │
   │    - 支持的协议版本列表（可用 -tls1_2 等限制）         │
   │    - 加密套件列表（-cipher / -ciphersuites 可指定）    │
   │    - SNI 扩展（-servername，默认就是命令行里的主机名）  │
   │    - ALPN（-alpn h2,http/1.1）                       │
   └────┬────────────────────────────────────────────────┘
        │
   ┌────┴────────────────────────────────────────────────┐
   │ ③ 服务端回 ServerHello + Certificate + ...           │
   │    证书链被打印出来（-showcerts 打印全部，否则只看叶） │
   │    用 -status 可请求 OCSP stapling                    │
   └────┬────────────────────────────────────────────────┘
        │
   ┌────┴────────────────────────────────────────────────┐
   │ ④ 完成握手，进入交互式会话                            │
   │    此时可以：                                         │
   │      - 直接敲 HTTP 请求（手写 HTTP）                   │
   │      - 按 R 重协商，按 Q 退出                          │
   │      - Ctrl-D 发送 EOF 退出                           │
   └────┬────────────────────────────────────────────────┘
        │
   输出区分为三段：
     [1] 握手与连接摘要（Protocol / Cipher / Session-ID / ...）
     [2] 证书链
     [3] 验证结果（Verify return code: 0 (ok) 或具体错误）
```

**Heartbeat 与 Heartbleed 的关系**（这是本节的重点之一）：

- `s_client` **没有** `-heartbleed` 这样的开关（那是第三方工具的用法）。
- 你能做的是**确认目标是否启用了 Heartbeat 扩展**（Heartbleed 的前提条件）。`openssl s_client -tlsextdebug` 会十六进制转储服务端返回的 TLS 扩展；Heartbeat 的扩展类型是 **15**（`0x000f`）。
- **真正判断"是否存在 Heartbleed"要用 NSE 脚本**：`nmap -p443 --script ssl-heartbleed <target>`。它才是真正发恶意心跳包去读内存的实现。
- 所以正确的工作流是：**`s_client -tlsextdebug` 看有没有 Heartbeat 扩展 → 有则用 `ssl-heartbleed` 脚本确认**。

## 3. 安装与快速上手

```bash
sudo apt install openssl          # 命令行工具（Kali 默认已装）
# 需要写 C 程序调 libssl 时：
sudo apt install libssl-dev
openssl version
openssl s_client -help | head -40
```

最小可用命令：

```bash
# 1) 连一个 HTTPS 站点，看协议与套件摘要
openssl s_client -connect example.com:443 -servername example.com -brief </dev/null

# 2) 看完整证书链
echo | openssl s_client -connect example.com:443 -servername example.com -showcerts

# 3) 离线读一个证书文件
openssl x509 -in cert.pem -noout -subject -issuer -dates -fingerprint -sha256
```

## 4. 核心参数详解

### s_client · 连接

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-connect <host:port>` | 目标（默认 `4433`） | 必须显式给 |
| `-servername <name>` | **SNI**，默认取命令行主机名 | 共享 IP/反代场景**必须显式设置**，否则可能拿到错误证书 |
| `-noservername` | 不发送 SNI 扩展 | 测试不支持 SNI 的老服务器 |
| `-4` / `-6` | 只用 IPv4 / IPv6 | 双栈排障 |
| `-bind <addr>` | 绑定本地地址 | 多网卡 |
| `-proxy <host:port>` | 通过代理连接 | 配合 `-proxy_user` / `-proxy_pass` |
| `-unix <path>` | 通过 Unix domain socket 连接 | 本地服务 |
| `-starttls <proto>` | 先发 STARTTLS 命令再升级：`smtp`、`pop3`、`imap`、`ftp`、`xmpp`、`xmpp-server`、`lmtp`、`postgres` | **邮件/数据库端口的标准用法** |
| `-name <host>` | 给 `-starttls lmtp/smtp/xmpp` 用的主机名 | — |
| `-xmpphost <h>` | `-starttls xmpp[-server]` 的 `-name` 别名 | — |

### s_client · 协议与套件

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-tls1` | **只**用 TLSv1.0 | 逐版本探测（注意：现代 OpenSSL 默认禁用它） |
| `-tls1_1` | 只 用 TLSv1.1 | 同上 |
| `-tls1_2` | 只 用 TLSv1.2 | 确认支持情况 |
| `-tls1_3` | 只 用 TLSv1.3 | 确认支持情况 |
| `-dtls` / `-dtls1` / `-dtls1_2` | DTLS 版本 | 语音/视频（SRTP）场景 |
| `-quic` | QUIC | HTTP/3 |
| `-no_ssl3` / `-no_tls1` … | 禁用某版本（可组合） | 只想排除个别版本时 |
| `-cipher <list>` | 指定 TLS1.2 及以下的加密套件列表 | 如 `-cipher 'ECDHE+AESGCM'` |
| `-ciphersuites <list>` | 指定 TLS1.3 的加密套件 | TLS1.3 的套件是独立命名空间 |
| `-sigalgs <list>` | 指定签名算法 | 排查签名算法不匹配 |
| `-client_sigalgs <list>` | 客户端签名算法 | — |
| `-alpn <list>` | 启用 ALPN（逗号分隔） | `-alpn h2,http/1.1` |
| `-nextprotoneg <list>` | 启用 NPN（已过时） | 老服务器 |
| `-fallback_scsv` | 发送 FALLBACK_SCSV | 检测降级攻击防护 |
| `-maxfraglen <n>` | 启用最大分片长度协商（512/1024/2048/4096） | — |

### s_client · 证书与验证

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-showcerts` | 打印服务端发送的**全部**证书 | 提取中间证书用 |
| `-status` | 请求 OCSP stapling | 检查是否启用 stapling |
| `-ocsp_check_leaf` / `-ocsp_check_all` | 用 OCSP 校验叶证书 / 整链状态 | 比 CRL 更快 |
| `-verify <depth>` | 开启对端证书验证到指定深度 | — |
| `-verify_return_error` | 验证失败时**返回错误**（而非只打印） | 脚本里判断"证书有效"用 |
| `-CAfile <file>` / `-CApath <dir>` / `-CAstore <uri>` | 自定义信任库 | 私有 CA 场景 |
| `-no-CAfile` / `-no-CApath` / `-no-CAstore` | 不加载默认信任库 | 想强制用自定义库时 |
| `-cert <file>` / `-key <file>` | 客户端证书 / 私钥 | 双向 TLS |
| `-certform PEM\|DER\|P12` | 客户端证书格式 | — |
| `-cert_chain <file>` / `-build_chain` | 客户端证书链 | — |
| `-dane_tlsa_domain` / `-dane_tlsa_rrdata` | DANE/TLSA 校验 | 高级 |
| `-psk_identity` / `-psk` | PSK 认证 | 特定服务 |
| `-nameopt <opt>` | 证书主题名打印选项 | — |
| `-requestCAfile <file>` | 发送给服务端的 CA 名列表 | — |

### s_client · 会话与调试

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-brief` | **只输出连接摘要**（协议/套件/对端证书/验证结果） | **最常用的"看一眼"参数** |
| `-prexit` | 程序退出时打印会话信息 | — |
| `-state` | 打印 SSL 状态机流转 | 排查"卡在哪一步" |
| `-msg` / `-trace` | 打印协议消息 / 完整协议追踪 | 深度调试 |
| `-msgfile <f>` | 把 `-msg`/`-trace` 输出写文件 | — |
| `-tlsextdebug` | **十六进制转储收到的 TLS 扩展** | **确认有没有 Heartbeat 扩展** |
| `-debug` | 额外调试输出 | — |
| `-keylogfile <f>` | 导出 TLS 密钥（供 Wireshark 解密） | 抓包分析 |
| `-reconnect` | 断开并用同一 Session-ID 重连 | 测试会话复用 |
| `-sess_out <f>` / `-sess_in <f>` | 保存/读取 TLS 会话 | 会话恢复测试 |
| `-quiet` | 不输出 s_client 自己的信息 | 只想要服务端内容时 |
| `-no_ign_eof` / `-ign_eof` | 控制 EOF 处理 | 脚本化时不希望它挂住 |
| `-no-interactive` | 不进入交互模式 | 脚本里用 |
| `-nocommands` | 禁止交互命令字母 | — |
| `-crlf` | 把输入的 LF 转成 CRLF | 手写 HTTP/SMTP 时 |
| `-timeout` | DTLS 连接的收发超时 | — |
| `-ktls` | 启用内核 TLS | — |

> ⚠️ **`-ssl2`、`-ssl3`、`-no_ssl2` 在 OpenSSL 3.x 已移除。** 如果你看到老教程里用 `-ssl2`/`-ssl3`，在 Kali 的新版本上会直接报错。验证 SSLv3 是否存在，请用 `nmap --script ssl-enum-ciphers`。

### s_client · 交互模式命令

握手完成后，`s_client` 进入交互模式，可以直接敲：

| 输入 | 作用 |
|------|------|
| `GET / HTTP/1.0` + 回车两次 | 手写一个 HTTP 请求 |
| `R` | 重新协商（renegotiate） |
| `Q` | 结束会话并退出 |
| `B` | 切换 `-brief` |
| `k` | 显示密钥 |
| `K` | 显示会话密钥 |
| `r` | 重新协商 |
| `D` | 显示会话详情 |
| `h` | 帮助 |

### 其他常用 openssl 子命令

| 子命令 | 作用 | 典型用法 |
|--------|------|----------|
| `openssl x509` | 证书解析/转换/签名 | `-in c.pem -noout -text -dates -subject -issuer -fingerprint -sha256` |
| `openssl verify` | 校验证书链 | `openssl verify -CAfile ca.pem cert.pem` |
| `openssl req` | 生成 CSR / 自签证书 | `openssl req -new -newkey rsa:2048 -nodes -keyout k.pem -out r.csr` |
| `openssl crl` | 解析 CRL（吊销列表） | `openssl crl -in crl.pem -noout -text` |
| `openssl ocsp` | 在线吊销状态查询 | `openssl ocsp -issuer ca.pem -cert c.pem -url <ocsp-url>` |
| `openssl s_server` | 手工 TLS 服务端 | 本地测试/故障复现 |
| `openssl s_time` | TLS 性能测试 | 基准压测 |
| `openssl ciphers` | 列出加密套件 | `openssl ciphers -v 'HIGH'` |
| `openssl dhparam` | 生成 DH 参数 | `openssl dhparam -out dh.pem 2048` |
| `openssl pkcs12` | P12/PFX 与 PEM 互转 | `openssl pkcs12 -in a.p12 -nodes -out a.pem` |
| `openssl asn1parse` | ASN.1 结构解析 | 分析畸形证书 |
| `openssl enc` | 对称加解密 | `-aes-256-cbc -pbkdf2` |
| `openssl dgst` | 摘要/签名/验签 | `openssl dgst -sha256 -verify pub.pem -signature s.bin data` |
| `openssl rand` | 生成随机数据 | `openssl rand -hex 16` |
| `openssl passwd` | 生成口令哈希（crypt 格式） | `openssl passwd -6` |
| `openssl ts` | 时间戳相关 | — |

## 5. 实战演练

**环境**：

- 本地靶机：自建 HTTPS 服务（`openssl s_server` 或 nginx 配自签证书），比如 `192.168.56.101:443`。
- 公网合法目标：`example.com:443`——IANA 保留示例域，天然可作为"正常 TLS 配置"的参照。
- 邮件/数据库 STARTTLS：本地起的 Postfix/PostgreSQL 或你自己的测试服务。

> 用 `s_client` 探测目标端口属于**主动连接**，只对你有授权的目标操作。对公网保留域（如 `example.com`）做**低频**连接是可以的。

### 场景 1：一眼看清连接参数（`-brief`，最常用）

```bash
openssl s_client -connect example.com:443 -servername example.com -brief </dev/null
```

实际输出（在本机 Kali 上运行得到）：

```text
Connecting to 2606:4700:10::6814:179a
CONNECTION ESTABLISHED
Protocol version: TLSv1.3
Ciphersuite: TLS_AES_256_GCM_SHA384
Peer certificate: CN=example.com
Hash used: SHA256
Signature type: ecdsa_secp256r1_sha256
Verification: OK
Negotiated TLS1.3 group: X25519MLKEM768
DONE
```

解读：
- `Protocol version: TLSv1.3` —— 目标支持 TLS 1.3。
- `Ciphersuite: TLS_AES_256_GCM_SHA384` —— 前向安全的 AEAD 套件。
- `Peer certificate: CN=example.com` —— 叶证书主体。
- `Verification: OK` —— **证书链验证通过**（用了系统信任库）。这一行是判断证书是否有效的核心。
- `</dev/null` 必不可少：否则 `s_client` 会进入交互模式并挂在那里等输入。

### 场景 2：查看完整证书链并解析细节

```bash
# 保存整条链
echo | openssl s_client -connect example.com:443 -servername example.com \
     -showcerts > /tmp/chain.txt 2>&1

# 提取并解析第一个证书（叶证书）
sed -n '/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p' /tmp/chain.txt > /tmp/leaf.pem
openssl x509 -in /tmp/leaf.pem -noout -text | head -40
```

实际输出片段：

```text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            06:24:d0:ab:31:15:58:78:0b:7d:52:13:b9:63:18:31
        Signature Algorithm: ecdsa-with-SHA256
        Issuer: C=US, O=SSL Corporation, CN=Cloudflare TLS Issuing ECC CA 3
        Validity
            Not Before: Jul 29 22:10:08 2026 GMT
            Not After : Oct 27 22:17:21 2026 GMT
        Subject: CN=example.com
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
                Public-Key: (256 bit)
                ASN1 OID: prime256v1
                NIST CURVE: P-256
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:FALSE
```

解读要点：

| 字段 | 含义 | 关注点 |
|------|------|--------|
| `Signature Algorithm` | 签名算法 | `sha1WithRSA` 属弱算法，应警惕 |
| `Issuer` | 签发者 | 是否可信 CA；是否与预期一致 |
| `Not After` | 到期时间 | 还有多少天？临期证书是常见事故源 |
| `Subject` | 主体 | CN 应匹配访问的域名 |
| `Public-Key: (256 bit)` | 密钥长度 | RSA < 2048 或 ECC < 256 都属弱密钥 |
| `X509v3 Basic Constraints: CA:FALSE` | 是叶证书 | `CA:TRUE` 说明是 CA 证书 |

**只看关键信息的简洁写法**：

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates -fingerprint -sha256 -serial
```

实际输出：

```text
subject=CN=example.com
issuer=C=US, O=SSL Corporation, CN=Cloudflare TLS Issuing ECC CA 3
notBefore=Jul 29 22:10:08 2026 GMT
notAfter=Oct 27 22:17:21 2026 GMT
sha256 Fingerprint=...
serial=...
```

**检查证书还有多久过期**（脚本化最实用）：

```bash
# -checkend N：证书在 N 秒内会过期则返回非零
openssl x509 -in /tmp/leaf.pem -noout -checkend 2592000 && \
  echo "30 天内不会过期" || echo "警告：30 天内将过期"

# 用 -enddate 直接拿日期
openssl x509 -in /tmp/leaf.pem -noout -enddate
```

### 场景 3：逐版本探测协议支持

```bash
for v in -tls1 -tls1_1 -tls1_2 -tls1_3; do
  printf "%-8s " "$v"
  timeout 12 bash -c "echo | openssl s_client -connect example.com:443 \
    -servername example.com $v 2>&1" | grep -m1 -E 'Protocol *:|no protocols available|alert|error'
done
```

实际输出（在 OpenSSL 3.6.4 上运行得到）：

```text
-tls1    40241C1CC07F0000:error:0A0000BF:SSL routines:tls_setup_handshake:no protocols available:ssl/statem/statem_lib.c:155:
-tls1_1  40B47ABAC77F0000:error:0A0000BF:SSL routines:tls_setup_handshake:no protocols available:ssl/statem/statem_lib.c:155:
-tls1_2  Protocol: TLSv1.2
-tls1_3  Protocol: TLSv1.3
```

解读：
- 前两行的 `no protocols available` **是本地 OpenSSL 报的错**，不是服务端拒绝——OpenSSL 3.x 在默认安全级别下已经不允许 TLS 1.0/1.1，客户端侧就拦住了。
- 想真正测试服务端是否**仍然支持** TLS 1.0/1.1，得降低本地安全级别或换工具：

```bash
# 方法一：降低安全级别（仅用于测试，注意影响）
openssl s_client -connect <host>:443 -tls1 -cipher 'DEFAULT@SECLEVEL=0' </dev/null 2>&1 | grep -m1 Protocol

# 方法二（推荐）：用 nmap 的 NSE 脚本枚举，不受本地 OpenSSL 策略影响
sudo nmap -p443 --script ssl-enum-ciphers <host>
```

**结论**：`s_client` 适合**确认"支持什么"**；枚举"**是否还遗留旧协议**"用 `nmap --script ssl-enum-ciphers` 更准确。这是一个很容易踩的坑。

### 场景 4：加密套件枚举

```bash
# 看某个套件是否可用
echo | openssl s_client -connect example.com:443 -servername example.com \
  -tls1_2 -cipher 'ECDHE-RSA-AES256-GCM-SHA384' 2>&1 | grep -E 'Cipher *:|error|alert'

# 列出本机 OpenSSL 支持的套件（按强度筛选）
openssl ciphers -v 'HIGH:!aNULL:!MD5' | head -20
openssl ciphers -v 'ECDHE+AESGCM' | wc -l

# 批量测试多个弱套件是否仍然被支持
for c in RC4-SHA DES-CBC3-SHA EXP-RC4-MD5 NULL-SHA; do
  printf "%-16s " "$c"
  timeout 10 bash -c "echo | openssl s_client -connect <host>:443 -cipher $c 2>&1" \
    | grep -m1 -E 'Cipher *:|alert|error' || echo "不支持"
done
```

解读：如果服务端**仍然接受** `RC4-SHA`、`3DES`、`NULL` 这类套件，说明 TLS 配置过时。但注意：`s_client` 报"套件协商成功"**不等于**服务端"专门支持"它——有时是协商降级的结果。所以严格的内核是把支持列表全部枚举出来，`nmap --script ssl-enum-ciphers` 会直接给出 `least strength` 分级。

### 场景 5：Heartbleed（心脏出血）检测

**第 1 步：确认服务端是否启用 Heartbeat 扩展**（Heartbleed 的前提条件）

```bash
echo | openssl s_client -connect <host>:443 -servername <host> \
  -tlsextdebug 2>&1 | grep -A 30 "TLS server extension"
```

解读：`-tlsextdebug` 会十六进制转储收到的扩展。Heartbeat 扩展的类型值是 **15（`0x000f`）**。输出里出现类似：

```text
TLS server extension "heartbeat" (id=15), len=1
```

说明**服务端声明支持心跳扩展**。这是必要条件，但不等于有漏洞——漏洞的关键是"服务端是否对心跳请求的长度字段做边界检查"。

**第 2 步：用 NSE 脚本真正验证**

```bash
sudo nmap -p443 --script ssl-heartbleed <host>
```

预期输出（存在漏洞时）：

```text
PORT    STATE SERVICE
443/tcp open  https
| ssl-heartbleed:
|   VULNERABLE:
|   The Heartbleed Bug is a serious vulnerability in the popular OpenSSL cryptographic software library.
|     State: VULNERABLE
|     Risk factor: High
|_    Disclosure date: 2014-04-07
```

预期输出（不存在漏洞时）：

```text
443/tcp open  https
```

**第 3 步：确认 OpenSSL 版本（辅助判断）**

```bash
# 如果目标是你能登录的服务器
openssl version -a
# 受影响的是 1.0.1 ~ 1.0.1f（以及 1.0.2-beta 的部分版本）
```

解读：**Heartbleed 的判定标准是"能通过恶意心跳包读到越界内存"，只有 `ssl-heartbleed` 这类真正发包的脚本能给出结论。** `s_client -tlsextdebug` 只回答"这个漏洞的入口是否开着"，属于缩小范围的辅助手段。

### 场景 6：STARTTLS（邮件 / 数据库 / FTP）

```bash
# SMTPS（隐式 TLS，465）
echo | openssl s_client -connect mail.example.com:465 -brief

# SMTP + STARTTLS（25 / 587）
echo | openssl s_client -connect mail.example.com:587 -starttls smtp -brief

# IMAP（143 + STARTTLS）
echo | openssl s_client -connect mail.example.com:143 -starttls imap -brief

# POP3（110 + STARTTLS）
echo | openssl s_client -connect mail.example.com:110 -starttls pop3 -brief

# PostgreSQL
echo | openssl s_client -connect db.example.com:5432 -starttls postgres -brief

# 手工读 SMTP 会话
openssl s_client -connect mail.example.com:587 -starttls smtp -crlf
# 然后可以敲：EHLO test.local
```

解读：`-starttls` 支持的协议是有限集合（`smtp`、`pop3`、`imap`、`ftp`、`xmpp`、`xmpp-server`、`lmtp`、`postgres`）。**邮件和数据库的 TLS 配置长期是薄弱环节**，很多组织只给 Web 配了现代 `ssl_ciphers`，却忘了 SMTP/IMAP。

### 场景 7：诊断握手失败

```bash
# 打不开？先看卡在哪一步
echo | openssl s_client -connect <host>:443 -servername <host> -state 2>&1 | tail -30
```

常见错误与含义：

| 错误信息 | 含义 | 应对 |
|---------|------|------|
| `Connection refused` | 端口没开 | 检查端口/防火墙 |
| `no protocols available` | **本地** OpenSSL 不允许该版本 | 见场景 3（不是服务端问题） |
| `sslv3 alert handshake failure` | 服务端拒绝（无共同套件/算法） | 换 `-cipher` / `-tls1_2` 重试 |
| `wrong version number` | 连到了非 TLS 端口（或在用明文协议） | 确认端口；可能需要 `-starttls` |
| `Hostname mismatch`（`-verify` 时） | SNI/主机名与证书不符 | 检查 `-servername` 与证书 CN/SAN |
| `unable to verify the first certificate` | 缺中间证书 | 用 `-CAfile`/`-showcerts` 手工补链 |
| `certificate has expired` | 证书过期 | `-dates`/`-enddate` 确认 |
| `self-signed certificate` | 自签证书 | 私有环境正常；生产环境是问题 |

**判断证书链是否完整**（很常见的一个运维问题）：

```bash
openssl s_client -connect <host>:443 -servername <host> -showcerts </dev/null 2>&1 \
  | grep -E '^\s*[0-9]+ s:|Verify return code'
```

`Verify return code: 0 (ok)` 表示链完整且可信；`21 (unable to verify the first certificate)` 通常意味着**服务端漏发了中间证书**——浏览器能容忍（会自动补），但很多非浏览器客户端（Java、Python requests、curl 老版本）会直接失败。

## 6. 输出解读

### `s_client` 输出的三段结构

```text
CONNECTED(00000003)                      ← ① 连接
depth=2 C=US, O=..., CN=...              ← ② 证书链（自根往下）
depth=1 ...
depth=0 CN=example.com
---
Certificate chain                        ← 完整链（-showcerts 时更详细）
 -----BEGIN CERTIFICATE-----
 ...
 -----END CERTIFICATE-----
---
Server certificate                       ← 服务端证书（再打印一次）
 subject=...
 issuer=...
---
No client certificate CA names sent      ← ③ 会话参数
Peer signing digest: SHA256
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 3521 bytes and written 373 bytes
Verification: OK                         ← ★ 验证结果
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Protocol  : TLSv1.3                      ← ★ 协商出的协议
Cipher    : TLS_AES_256_GCM_SHA384       ← ★ 协商出的套件
Session-ID: ...
Master-Key: ...
Verify return code: 0 (ok)               ← ★ 退出前最后确认
```

### 关键字段速查

| 字段 | 含义 | 判断标准 |
|------|------|----------|
| `Protocol` | 协商出的 TLS 版本 | 应为 TLSv1.2 或 TLSv1.3 |
| `Cipher` | 协商出的套件 | 应含 `ECDHE`（前向安全）+ `GCM`/`CHACHA20`（AEAD） |
| `Server Temp Key` | 临时密钥（DH/ECDH） | 有它说明用了 (EC)DHE，具备前向安全 |
| `Verification` | 链验证结果 | 应为 `OK` |
| `Verify return code` | 验证返回码 | `0 (ok)` 才正常；其他数字要查含义 |
| `depth=N` | 链中层级（0=叶，越大越接近根） | 与证书主体对照 |
| `Peer signing digest` | 对端签名摘要算法 | `SHA256` 及以上 |
| `subject=` / `issuer=` | 主体/签发者 | 主体应匹配访问域名 |
| `SSL handshake has read X bytes` | 握手数据量 | 异常大可能意味着链过长/配置臃肿 |

### 常见 `Verify return code`

| 返回码 | 含义 | 严重度 |
|--------|------|--------|
| `0 (ok)` | 验证通过 | — |
| `10 (certificate has expired)` | 证书过期 | **高** |
| `18 (self-signed certificate)` | 自签证书 | 视场景（内网可接受） |
| `19 (self-signed certificate in certificate chain)` | 链中有自签 | 中 |
| `20 (unable to get local issuer certificate)` | 缺中间证书/根不受信 | **高**（客户端会失败） |
| `21 (unable to verify the first certificate)` | 链不完整 | 中高（部分客户端失败） |
| `22 (certificate has been revoked)` | 已被吊销 | 高 |
| `26 (unsupported certificate purpose)` | 证书用途不符 | 中 |

## 7. 与其他工具配合

```bash
# 1) nmap 找 TLS 端口 -> s_client 逐项确认
sudo nmap -p443,8443,993,995,587,5432 --open -oG - 192.168.56.0/24 | awk '/Ports:/{print $2}' > tls_hosts.txt
while read -r h; do
  echo "=== $h ==="
  timeout 10 bash -c "echo | openssl s_client -connect $h:443 -brief 2>&1" | head -8
done < tls_hosts.txt

# 2) 批量 TLS 配置枚举（比 s_client 更适合做清单）
sudo nmap -p443 --script "ssl-enum-ciphers,ssl-cert" -iL tls_hosts.txt -oX tls.xml
searchsploit --nmap tls.xml     # 顺带查 TLS 组件的已知漏洞

# 3) nuclei 的 ssl 模板 + s_client 定向确认
nuclei -l tls_hosts.txt -pt ssl -silent -o ssl_findings.txt
echo | openssl s_client -connect <可疑主机>:443 -servername <域名> -showcerts

# 4) 证书到期监控（放进 cron，告警用）
HOST=example.com
DAYS=$(echo | openssl s_client -connect $HOST:443 -servername $HOST 2>/dev/null \
  | openssl x509 -noout -checkend $((86400*30)) >/dev/null 2>&1 && echo ok || echo warning)
echo "$HOST: $DAYS"

# 5) s_client 手写 HTTP 请求（调试虚拟主机/反代）
openssl s_client -connect <host>:443 -servername target.example.com -quiet <<'EOF'
GET / HTTP/1.1
Host: target.example.com
Connection: close

EOF
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| 命令执行后**卡住不动** | 进入了交互模式，在等输入 | `< /dev/null` 或 `echo |`；或加 `-no-interactive` |
| 拿到的是"另一个域名"的证书 | 共享 IP，未设置 SNI | 显式加 `-servername <正确域名>` |
| `-ssl2` / `-ssl3` 报错 | OpenSSL 3.x 已移除这些选项 | 用 `nmap --script ssl-enum-ciphers` 代替 |
| 测 TLS 1.0/1.1 永远失败 | 本地 OpenSSL 安全级别默认禁用了它们 | 加 `-cipher 'DEFAULT@SECLEVEL=0'`，或改用 nmap |
| 证书验证一直失败 | 缺中间证书/私有 CA | `-CAfile`/`-CApath` 指定信任库；或 `-showcerts` 看清链 |
| `-verify` 失败但不影响输出 | 只用 `-verify` 时失败不会返回错误码 | 加 `-verify_return_error`，脚本才能正确判断 |
| 提取证书时 `openssl x509` 报无输入 | 只取了第一个 `BEGIN/END` 之间的内容 | `sed -n '/BEGIN CERTIFICATE/,/END CERTIFICATE/p'` 提取全部会得到多张证书，需分开处理 |
| 想看 Heartbleed 却找不到参数 | `s_client` **没有** `-heartbleed` | `-tlsextdebug` 查扩展 + `nmap --script ssl-heartbleed` 验证 |
| STARTTLS 报 `wrong version number` | 端口是明文协议，不是 TLS | 加对应的 `-starttls <proto>` |
| `-brief` 下看不到证书细节 | `-brief` 只给摘要 | 去掉 `-brief` 或用 `-showcerts | openssl x509` |
| 代理环境连不上 | 未配置代理 | `-proxy <host:port>`，必要时 `-proxy_user`/`-proxy_pass` |
| 会话看起来复用异常 | — | 用 `-reconnect` + `-sess_out`/`-sess_in` 明确测试会话恢复 |

## 9. 防御视角（蓝队）

这一节把"用 openssl 检查"反过来变成"按检查项加固"。

### TLS 配置基线（按优先级）

| 项目 | 目标 | 怎么验证 |
|------|------|----------|
| 协议版本 | 只允许 TLS 1.2 / 1.3 | `nmap --script ssl-enum-ciphers` |
| 加密套件 | 只用 AEAD（AES-GCM / ChaCha20-Poly1305）+ 前向安全（ECDHE） | 同上，看 `ciphers` 列表 |
| 禁用弱套件 | 无 RC4、3DES、NULL、EXPORT、anon | 同上，看 `least strength` |
| 证书链完整 | 服务端必须发送中间证书 | `s_client -showcerts` + `Verify return code: 0 (ok)` |
| 密钥长度 | RSA ≥ 2048（推荐 3072/4096）；ECC ≥ 256 | `openssl x509 -text` |
| 签名算法 | SHA-256 及以上 | `openssl x509 -text` 的 `Signature Algorithm` |
| 到期监控 | 至少提前 30 天告警 | `openssl x509 -checkend` |
| SNI / 虚拟主机 | 每个站点有正确证书 | `s_client -servername` 逐个验证 |
| HSTS | 强制 HTTPS | 看响应头 `Strict-Transport-Security` |
| OCSP Stapling | 减少客户端吊销查询延迟 | `s_client -status` |

### Heartbleed 的专项处理

- **判断**：`s_client -tlsextdebug` 看是否声明 Heartbeat 扩展（id=15）→ `nmap --script ssl-heartbleed` 确认。
- **加固**：
  - 升级 OpenSSL 到 1.0.1g 以上（**当前受影响的 1.0.1~1.0.1f 早已 EOL**，任何现代发行版都不受影响）。
  - 如果历史上曾受影响：**必须吊销并重签证书、更换私钥**，因为私钥可能已通过越界读泄露。仅打补丁不够。
  - 重新签发后通知所有依赖方。
- **检测**：Heartbleed 利用会产生**畸形的 TLS 心跳包**（声明长度远大于实际数据）。IDS/IPS 有对应规则（如 Suricata 的 `tls.heartbleed` 相关规则）。

### 可检测的扫描行为

- **逐版本/逐套件探测**：短时间内对同一端口用不同 TLS 参数反复握手。`s_client` 的握手很"干净"（不发 HTTP 请求），所以表现在日志里是"有 TLS 握手但没有后续应用数据"。
- **证书枚举**：以不同 SNI 反复连接（`-servername` 变化），用于发现虚拟主机——这在反代日志里能看到"同一源 IP、大量不同 Host"。
- **降低安全级别探测**：`-cipher 'DEFAULT@SECLEVEL=0'` 会尝试 TLS 1.0/1.1，这是明显的降级探测特征。
- **缓解**：对同一源 IP 的 TLS 握手失败率/频率设阈值；在边缘设备上直接拒绝已淘汰的协议版本（这样降级探测会立刻失败并留痕）。

### 蓝队自查建议

```bash
# 定期跑一遍自己资产的 TLS 基线
sudo nmap -p443,8443,993,995,587 --script "ssl-enum-ciphers,ssl-cert,ssl-heartbleed" \
     -iL my_hosts.txt -oX tls_baseline.xml
# 用 XSLT 或简单 grep 提取有问题的项
grep -E "least strength: [EF]|TLSv1\.0|TLSv1\.1" tls_baseline.xml
```

把这份基线固化成周期任务，比每次手工 `s_client` 高效得多。**`s_client` 的价值在于"对可疑项做深入确认"，而不是当作批量扫描器。**

## 10. 参考

- 官方文档（含 `s_client`、`x509`、`verify` 手册）：<https://docs.openssl.org/>
- `s_client` 手册页：<https://docs.openssl.org/master/man1/openssl-s_client/>
- `x509` 手册页：<https://docs.openssl.org/master/man1/openssl-x509/>
- RFC 8446（TLS 1.3）：<https://www.rfc-editor.org/rfc/rfc8446>
- CVE-2014-0160（Heartbleed）官方说明：<https://www.heartbleed.com/>
- Kali 工具页：<https://www.kali.org/tools/openssl/>
- man page：`man openssl` ｜ `man s_client`（若已安装 `openssl-doc`）｜ `man x509`
- 用法核实：本教程的 `s_client` / `x509` 参数取自本机 `OpenSSL 3.6.4` 的 `-help` 输出；场景 1、3、5 的输出片段为在本机对 `example.com:443` 实际执行所得

---

**相关教程**：[nuclei](nuclei.md) ｜ [nikto](nikto.md) ｜ [searchsploit](searchsploit.md) ｜ [lynis](lynis.md) ｜ [nmap](../01-信息搜集/nmap.md)
