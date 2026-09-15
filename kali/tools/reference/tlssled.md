# tlssled

> Evaluates the security of a target SSL/TLS (HTTPS) server TLSSLed is a Linux shell script whose purpose is to evaluate the security of a target SSL/TLS (HTTPS) web server implementation. It is based on sslscan, a thorough SSL/TLS scanner t…

> **功能分类**：信息搜集 ｜ **Kali 包**：`tlssled` ｜ **官方文档**：<https://www.kali.org/tools/tlssled/>

## 1. 安装

```bash
sudo apt update
sudo apt install tlssled
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3 |
| 架构 | all |
| 可执行命令 | `tlssled` |
| 依赖 | `openssl`、`sslscan` |
| 安装体积 | 38 KB |
| 官网 | <http://www.taddong.com/en/lab.html> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/tlssled> |
| 包追踪 | <https://pkg.kali.org/pkg/tlssled> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Check SSL/TLS on the host (192.168.1.1) and port (443):
root@kali:~# tlssled 192.168.1.1 443
------------------------------------------------------
 TLSSLed - (1.3) based on sslscan and openssl
                 by Raul Siles (www.taddong.com)
------------------------------------------------------
    openssl version: OpenSSL 1.0.1e 11 Feb 2013
    sslscan version 1.8.2
------------------------------------------------------
------------------------------------------------------

[*] Analyzing SSL/TLS on 192.168.1.1:443 ...
    [.] Output directory: TLSSLed_1.3_192.168.1.1_443_20140513-165131 ...

[*] Checking if the target service speaks SSL/TLS...
    [.] The target service 192.168.1.1:443 seems to speak SSL/TLS...

    [.] Using SSL/TLS protocol version:
        (empty means I'm using the default openssl protocol version(s))

[*] Running sslscan on 192.168.1.1:443 ...

    [-] Testing for SSLv2 ...

    [-] Testing for the NULL cipher ...
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tlssled`

> 官方示例调用：`tlssled 192.168.1.1 443`

```text
root@kali:~# tlssled 192.168.1.1 443
------------------------------------------------------
 TLSSLed - (1.3) based on sslscan and openssl
                 by Raul Siles (www.taddong.com)
------------------------------------------------------
    openssl version: OpenSSL 1.0.1e 11 Feb 2013
    sslscan version 1.8.2
------------------------------------------------------
------------------------------------------------------
[*] Analyzing SSL/TLS on 192.168.1.1:443 ...
    [.] Output directory: TLSSLed_1.3_192.168.1.1_443_20140513-165131 ...
[*] Checking if the target service speaks SSL/TLS...
    [.] The target service 192.168.1.1:443 seems to speak SSL/TLS...
    [.] Using SSL/TLS protocol version:
        (empty means I'm using the default openssl protocol version(s))
[*] Running sslscan on 192.168.1.1:443 ...
    [-] Testing for SSLv2 ...
    [-] Testing for the NULL cipher ...
```

### `tlssled -h`

> 官方示例调用：`tlssled -h`

```text
root@kali:~# tlssled -h
------------------------------------------------------
 TLSSLed - (1.3) based on sslscan and openssl
                 by Raul Siles (www.taddong.com)
------------------------------------------------------
    openssl version: OpenSSL 3.6.3 9 Jun 2026 (Library: OpenSSL 3.6.3 9 Jun 2026)
------------------------------------------------------
------------------------------------------------------
[!] Usage: /usr/bin/tlssled <hostname or IP_address> <port>
Updated on: 2026-Aug-25
 Edit this page
theharvester
tmux
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install tlssled`，再执行 `tlssled --version` 2>/dev/null || `tlssled -V`
- [ ] **2.** **读官方帮助** —— `tlssled -h`，需要细节时 `man tlssled`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `tlssled -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/tlssled/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/tlssled/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/tlssled/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
