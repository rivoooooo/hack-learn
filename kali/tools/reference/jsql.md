# jsql

> root@kali:~# jsql -h 2026-09-14 06:41:06,177 ERROR [main] jsql.MainApp (MainApp.java:30) - Headless runtime not supported, use default Java runtime instead

> **功能分类**：Web 应用 ｜ **Kali 包**：`jsql` ｜ **官方文档**：<https://www.kali.org/tools/jsql/>

## 1. 安装

```bash
sudo apt update
sudo apt install jsql
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.115 |
| 架构 | all |
| 可执行命令 | `jsql-injection`、`jsql` |
| 官网 | <https://github.com/ron190/jsql-injection> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/jsql> |
| 包追踪 | <https://pkg.kali.org/pkg/jsql> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Description
jSQL Injection is a lightweight application used to find database information from a server.
It’s free, open source and cross-platform and it works with Java from version 11 to 20.
The source code is available on Github: https://github.com/ron190/jsql-injection
Features

Automatic injection of 33 database engines: Access, Altibase, C-treeACE, CockroachDB, CUBRID, DB2, Derby, Exasol, Firebird, FrontBase, H2, Hana, HSQLDB, Informix, Ingres, InterSystems-IRIS, MaxDB, Mckoi, MemSQL, MimerSQL, MonetDB, MySQL, Neo4j, Netezza, NuoDB, Oracle, PostgreSQL, Presto, SQLite, SQL Server, Sybase, Teradata and Vertica
Multiple injection strategies: Normal, Stacked, Error, Blind and Time
Parallel bitwise Boolean Blind and Time strategies
Various injection processes: Default, Zip, Dios
Database fingerprint: Basic error, Order By error, Boolean single query
Script sandboxes for SQL and tampering
Inject multiple targets
Read and write files using injection
Create and display Web shell and SQL shell
Bruteforce password hash
Search for admin pages
Hash, encode and decode text
Authenticate using Basic, Digest, NTLM and Kerberos
Proxy connection on HTTP, SOCKS4 and SOCKS5

Continuous integration
This software is developed using open source libraries like Spring, Spock and Hibernate and is tested using continuous integration platform Github Actions.
Non regression tests are run against dockerized and in memory databases and GUI is tested on VNC screen on the CI platform, then quality checks are stored on code quality platform.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `jsql`

> 官方示例调用：`jsql -h`

```text
root@kali:~# jsql -h
2026-09-14 06:41:06,177 ERROR [main] jsql.MainApp (MainApp.java:30) - Headless runtime not supported, use default Java runtime instead
```

### `jsql-injection`

> 官方示例调用：`jsql-injection -h`

```text
root@kali:~# jsql-injection -h
2026-09-14 06:41:07,816 ERROR [main] jsql.MainApp (MainApp.java:30) - Headless runtime not supported, use default Java runtime instead
Updated on: 2026-Aug-25
 Edit this page
john
juice-shop
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install jsql`，再执行 `jsql-injection --version` 2>/dev/null || `jsql-injection -V`
- [ ] **2.** **读官方帮助** —— `jsql-injection -h`，需要细节时 `man jsql-injection`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `jsql-injection -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/jsql/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/initial-access.md`](../../tools/by-attack/initial-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/jsql/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/jsql/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
