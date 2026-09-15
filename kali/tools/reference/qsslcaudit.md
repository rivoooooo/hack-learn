# qsslcaudit

> Test SSL/TLS clients how secure they are This tool can be used to determine if an application that uses TLS/SSL for its data transfers does this in a secure way.

> **功能分类**：信息搜集 ｜ **Kali 包**：`qsslcaudit` ｜ **官方文档**：<https://www.kali.org/tools/qsslcaudit/>

## 1. 安装

```bash
sudo apt update
sudo apt install qsslcaudit
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.8.3 |
| 架构 | any |
| 可执行命令 | `qsslcaudit` |
| 依赖 | `libc6`、`libcrypto++8t64`、`libgcc-s1`、`libgnutls30t64`、`libqt5core5t64`、`libqt5network5t64`、`libstdc++6`、`libunsafessl1.0.2` |
| 安装体积 | 1.11 MB |
| 官网 | <https://github.com/gremwell/qsslcaudit> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/qsslcaudit> |
| 包追踪 | <https://pkg.kali.org/pkg/qsslcaudit> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
qsslcaudit -h          # 查看用法
man qsslcaudit         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `qsslcaudit`

> 官方示例调用：`qsslcaudit -h`

```text
root@kali:~# qsslcaudit -h
Usage: qsslcaudit [options]
A tool to test SSL clients behavior
SSL client tests:
	1: (certs) custom certificate trust
	   certificate trust test with user-supplied certificate
	2: (certs) self-signed certificate for target domain trust
	   certificate trust test with self-signed certificate for user-supplied common name
	3: (certs) self-signed certificate for invalid domain trust
	   certificate trust test with self-signed certificate for www.example.com
	4: (certs) custom certificate for target domain trust
	   certificate trust test with user-supplied common name signed by user-supplied certificate
	5: (certs) custom certificate for invalid domain trust
	   certificate trust test with www.example.com common name signed by user-supplied certificate
	6: (certs) certificate for target domain signed by custom CA trust
	   certificate trust test with user-supplied common name signed by user-supplied CA certificate
	7: (certs) certificate for invalid domain signed by custom CA trust
	   certificate trust test with www.example.com common name signed by user-supplied CA certificate
	8: (protos) SSLv2 protocol support
	   test for SSLv2 protocol support
	9: (protos) SSLv3 protocol support
	   test for SSLv3 protocol support
	10: (ciphers) SSLv3 protocol and EXPORT grade ciphers support
	   test for SSLv3 protocol and EXPORT grade ciphers support
	11: (ciphers) SSLv3 protocol and LOW grade ciphers support
	   test for SSLv3 protocol and LOW grade ciphers support
	12: (ciphers) SSLv3 protocol and MEDIUM grade ciphers support
	   test for SSLv3 protocol and MEDIUM grade ciphers support
	13: (protos) TLS 1.0 protocol support
	   test for TLS 1.0 protocol support
	14: (ciphers) TLS 1.0 protocol and EXPORT grade ciphers support
	   test for TLS 1.0 protocol and EXPORT grade ciphers support
	15: (ciphers) TLS 1.0 protocol and LOW grade ciphers support
	   test for TLS 1.0 protocol and LOW grade ciphers support
	16: (ciphers) TLS 1.0 protocol and MEDIUM grade ciphers support
	   test for TLS 1.0 protocol and MEDIUM grade ciphers support
	17: (ciphers) TLS 1.1 protocol and EXPORT grade ciphers support
	   test for TLS 1.1 protocol and EXPORT grade ciphers support
	18: (ciphers) TLS 1.1 protocol and LOW grade ciphers support
	   test for TLS 1.1 protocol and LOW grade ciphers support
	19: (ciphers) TLS 1.1 protocol and MEDIUM grade ciphers support
	   test for TLS 1.1 protocol and MEDIUM grade ciphers support
	20: (ciphers) TLS 1.2 protocol and EXPORT grade ciphers support
	   test for TLS 1.2 protocol and EXPORT grade ciphers support
	21: (ciphers) TLS 1.2 protocol and LOW grade ciphers support
	   test for TLS 1.2 protocol and LOW grade ciphers support
	22: (ciphers) TLS 1.2 protocol and MEDIUM grade ciphers support
	   test for TLS 1.2 protocol and MEDIUM grade ciphers support
	23: (ciphers) DTLS 1.0 protocol and EXPORT grade ciphers support
	   test for DTLS 1.0 protocol and EXPORT grade ciphers support
	24: (ciphers) DTLS 1.0 protocol and LOW grade ciphers support
	   test for DTLS 1.0 protocol and LOW grade ciphers support
	25: (ciphers) DTLS 1.0 protocol and MEDIUM grade ciphers support
	   test for DTLS 1.0 protocol and MEDIUM grade ciphers support
	26: (ciphers) DTLS 1.2 protocol and EXPORT grade ciphers support
	   test for DTLS 1.2 protocol and EXPORT grade ciphers support
	27: (ciphers) DTLS 1.2 protocol and LOW grade ciphers support
	   test for DTLS 1.2 protocol and LOW grade ciphers support
	28: (ciphers) DTLS 1.2 protocol and MEDIUM grade ciphers support
	   test for DTLS 1.2 protocol and MEDIUM grade ciphers support
	29: (certs) CVE-2020-0601 ECC cert trust
	   test for trusting certificate signed by private key with custom curve
Options:
  -h, --help                      Displays help on commandline options.
  --help-all                      Displays help including Qt specific options.
  -v, --version                   Displays version information.
  -l, --listen-address <0.0.0.0>  listen on <address>
  -p, --listen-port <8443>        bind to <port>
  --user-cn <example.com>         common name (CN) to suggest to client
  --server <https://example.com>  grab certificate information from <server>
  --user-cert <~/host.cert>       path to file containing custom certificate
                                  (or chain of certificates)
  --user-key <~/host.key>         path to file containing custom private key
  --user-ca-cert <~/ca.cert>      path to file containing custom certificate
                                  usable as CA
  --user-ca-key <~/ca.key>        path to file containing custom private key
                                  for CA certificate
  --selected-tests <1,3,5>        comma-separated list of tests (id) to execute
  --forward <127.0.0.1:6666>      forward connection to upstream proxy
  --show-ciphers                  show ciphers provided by loaded openssl
                                  library
  --starttls <ftp|smtp|xmpp>      exchange specific STARTTLS messages before
                                  starting secure connection
  --loop-tests                    infinitely repeat selected tests (use Ctrl-C
                                  to kill the tool)
  -w, --wait-data-timeout <5000>  wait for incoming data <ms> milliseconds
                                  before emitting error
  --output-xml <qsslcaudit.xml>   save results in XML
  --pid-file </tmp/qs.pid>        create a pidfile once initialized
  --dtls                          use DTLS protocol over UDP
  --double-first-test             execute the first test two times and ignore
                                  its client fingerprint
Updated on: 2025-Dec-09
 Edit this page
python-ldapdomaindump
rarcrack
LIGHT
DARK
Links
Home
Download / Get Kali
Blog
OS Documentation
Tool Documentation
System Status
Archived Releases
Partnerships
Platforms
ARM (SBC)
NetHunter (Mobile)
Amazon AWS
Docker
Linode
Microsoft Azure
Microsoft Store (WSL)
Vagrant
Development
Bug Tracker
Continuous Integration
Network Mirror
Package Tracker
GitLab
Community
Discord
Support Forum
PeerTube
Follow Us
Bluesky
Facebook
Instagram
Mastodon
Substack
X
Newsletter
RSS
Policies
Cookie Policy
Privacy Policy
Trademark Policy
© OffSec Services Limited 2026. All rights reserved.
Kali Linux is part of OffSec's Community Projects
Learn more about OffSec's free, open-source penetration testing tools for cybersecurity professionals
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install qsslcaudit`，再执行 `qsslcaudit --version` 2>/dev/null || `qsslcaudit -V`
- [ ] **2.** **读官方帮助** —— `qsslcaudit -h`，需要细节时 `man qsslcaudit`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: qsslcaudit [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/qsslcaudit/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/qsslcaudit/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/qsslcaudit/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
