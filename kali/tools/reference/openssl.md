# openssl

> Secure Sockets Layer toolkit - cryptographic utility This package is part of the OpenSSL project’s implementation of the SSL and TLS cryptographic protocols for secure communication over the Internet. It contains the general-purpose comman…

> **功能分类**：信息搜集 ｜ **Kali 包**：`openssl` ｜ **官方文档**：<https://www.kali.org/tools/openssl/>

## 1. 安装

```bash
sudo apt update
sudo apt install openssl
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.6.3 |
| 架构 | any |
| 可执行命令 | `libcrypto3-udeb`、`libssl-dev`、`libssl-doc`、`libssl3-udeb`、`libssl3t64`、`openssl`、`openssl-provider-fips`、`openssl-provider-legacy` |
| 依赖 | `libc6`、`libssl3t64` |
| 安装体积 | 2.47 MB |
| 官网 | <https://openssl-library.org> |
| 源码仓库 | <https://salsa.debian.org/debian/openssl> |
| 包追踪 | <https://pkg.kali.org/pkg/openssl> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libcrypto3-udeb -h          # 查看用法
man libcrypto3-udeb         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 8 个可执行命令，下面是官方页面内嵌的帮助原文。

### `openssl`

官方给出的调用示例：`openssl -h`

```text
root@kali:~# openssl -h
help:
Standard commands
asn1parse         ca                ciphers           cmp
cms               configutl         crl               crl2pkcs7
dgst              dhparam           dsa               dsaparam
ec                ecparam           enc               engine
errstr            fipsinstall       gendsa            genpkey
genrsa            help              info              kdf
list              mac               nseq              ocsp
passwd            pkcs12            pkcs7             pkcs8
pkey              pkeyparam         pkeyutl           prime
rand              rehash            req               rsa
rsautl            s_client          s_server          s_time
sess_id           skeyutl           smime             speed
spkac             srp               storeutl          ts
verify            version           x509
Message Digest commands (see the `dgst' command for more details)
blake2b512        blake2s256        md4               md5
rmd160            sha1              sha224            sha256
sha3-224          sha3-256          sha3-384          sha3-512
sha384            sha512            sha512-224        sha512-256
shake128          shake256          sm3
Cipher commands (see the `enc' command for more details)
aes-128-cbc       aes-128-ecb       aes-192-cbc       aes-192-ecb
aes-256-cbc       aes-256-ecb       aria-128-cbc      aria-128-cfb
aria-128-cfb1     aria-128-cfb8     aria-128-ctr      aria-128-ecb
aria-128-ofb      aria-192-cbc      aria-192-cfb      aria-192-cfb1
aria-192-cfb8     aria-192-ctr      aria-192-ecb      aria-192-ofb
aria-256-cbc      aria-256-cfb      aria-256-cfb1     aria-256-cfb8
aria-256-ctr      aria-256-ecb      aria-256-ofb      base64
bf                bf-cbc            bf-cfb            bf-ecb
bf-ofb            camellia-128-cbc  camellia-128-ecb  camellia-192-cbc
camellia-192-ecb  camellia-256-cbc  camellia-256-ecb  cast
cast-cbc          cast5-cbc         cast5-cfb         cast5-ecb
cast5-ofb         des               des-cbc           des-cfb
des-ecb           des-ede           des-ede-cbc       des-ede-cfb
des-ede-ofb       des-ede3          des-ede3-cbc      des-ede3-cfb
des-ede3-ofb      des-ofb           des3              desx
rc2               rc2-40-cbc        rc2-64-cbc        rc2-cbc
rc2-cfb           rc2-ecb           rc2-ofb           rc4
rc4-40            seed              seed-cbc          seed-cfb
seed-ecb          seed-ofb          sm4-cbc           sm4-cfb
sm4-ctr           sm4-ecb           sm4-ofb           zlib
zstd
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install openssl`，再执行 `libcrypto3-udeb --version` 2>/dev/null || `libcrypto3-udeb -V`
- [ ] **2.** **读官方帮助** —— `libcrypto3-udeb -h`，需要细节时 `man libcrypto3-udeb`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `libcrypto3-udeb -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/openssl/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[openssl](../../tools/tutorials/02-漏洞分析/openssl.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/openssl/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/openssl/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
