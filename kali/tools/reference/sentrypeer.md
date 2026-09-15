# sentrypeer

> SIP peer to peer honeypot for VoIP SentryPeer is a distributed list of bad IP addresses and phone numbers collected via a SIP Honeypot. SentryPeer is a fraud detection tool. It lets bad actors try to make phone calls and saves the IP addre…

> **功能分类**：检测 ｜ **Kali 包**：`sentrypeer` ｜ **官方文档**：<https://www.kali.org/tools/sentrypeer/>

## 1. 安装

```bash
sudo apt update
sudo apt install sentrypeer
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.0.4 |
| 架构 | amd64 |
| 可执行命令 | `sentrypeer` |
| 依赖 | `adduser`、`libc6`、`libcurl4t64`、`libgcc-s1`、`libjansson4`、`libmicrohttpd12t64`、`libosip2-15t64`、`libpcre2-8-0`、`libsqlite3-0`、`libuuid1` |
| 安装体积 | 5.32 MB |
| 官网 | <https://sentrypeer.org> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sentrypeer> |
| 包追踪 | <https://pkg.kali.org/pkg/sentrypeer> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sentrypeer -h          # 查看用法
man sentrypeer         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sentrypeer`

官方给出的调用示例：`sentrypeer -h`

```text
root@kali:~# sentrypeer -h
Protect your SIP Servers from bad actors at https://sentrypeer.com
Usage: sentrypeer [OPTIONS]
Options:
  -f <DB_FILE>                 Set 'sentrypeer.db' location or use SENTRYPEER_DB_FILE env
  -j                           Enable json logging or use SENTRYPEER_JSON_LOG env
  -p                           Enable Peer to Peer mode or use SENTRYPEER_PEER_TO_PEER env
  -b <BOOTSTRAP_NODE>          Set Peer to Peer bootstrap node or use SENTRYPEER_BOOTSTRAP_NODE env
  -i <CLIENT_ID>               Set OAuth 2 client ID or use SENTRYPEER_OAUTH2_CLIENT_ID env to get a Bearer token for WebHook
  -c <CLIENT_SECRET>           Set OAuth 2 client secret or use SENTRYPEER_OAUTH2_CLIENT_SECRET env to get a Bearer token for WebHook
  -a                           Enable RESTful API mode or use SENTRYPEER_API env
  -w <WEBHOOK_URL>             Set WebHook URL for bad actor json POSTs or use SENTRYPEER_WEBHOOK_URL env
  -r                           Enable SIP responsive mode or use SENTRYPEER_SIP_RESPONSIVE env
  -R                           Disable SIP mode completely or use SENTRYPEER_SIP_DISABLE env
  -l <JSON_LOG_FILE>           Set JSON logfile (default './sentrypeer_json.log') location or use SENTRYPEER_JSON_LOG_FILE env
  -N                           Disable Rust powered TCP, UDP and TLS or use SENTRYPEER_TLS_DISABLE env
  -t <TLS_CERT_FILE>           Set TLS cert location (default './cert.pem') or use SENTRYPEER_CERT env
  -k <TLS_KEY_FILE>            Set TLS key location (default './key.pem') or use SENTRYPEER_KEY env
  -z <TLS_LISTEN_ADDRESS>      Set TLS listen address (default '0.0.0.0:5061') or use SENTRYPEER_TLS_LISTEN_ADDRESS env
  -s                           Enable syslog logging or use SENTRYPEER_SYSLOG env
  -v                           Enable verbose logging or use SENTRYPEER_VERBOSE env
  -d                           Enable debug mode or use SENTRYPEER_DEBUG env
  -h, --help                   Print help
  -V, --version                Print version
Updated on: 2026-Mar-02
 Edit this page
sendemail
sickle-pdk
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sentrypeer`，再执行 `sentrypeer --version` 2>/dev/null || `sentrypeer -V`
- [ ] **2.** **读官方帮助** —— `sentrypeer -h`，需要细节时 `man sentrypeer`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sentrypeer [OPTIONS]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sentrypeer/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sentrypeer/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sentrypeer/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
