# tnscmd10g

> Tool to prod the oracle tnslsnr process A tool to prod the oracle tnslsnr process on port 1521/tcp.

> **功能分类**：Web 应用 ｜ **Kali 包**：`tnscmd10g` ｜ **官方文档**：<https://www.kali.org/tools/tnscmd10g/>

## 1. 安装

```bash
sudo apt update
sudo apt install tnscmd10g
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3 |
| 架构 | all |
| 可执行命令 | `tnscmd10g` |
| 依赖 | `libio-socket-ip-perl`、`perl` |
| 安装体积 | 18 KB |
| 官网 | <http://www.red-database-security.com/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/tnscmd10g> |
| 包追踪 | <https://pkg.kali.org/pkg/tnscmd10g> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Retrieve the version (version) from the target server (-h 192.168.1.205):
root@kali:~# tnscmd10g version -h 192.168.1.205
sending (CONNECT_DATA=(COMMAND=version)) to 192.168.1.205:1521
writing 90 bytes
reading
.M.......6.........-. ..........(DESCRIPTION=(TMP=)(VSNNUM=153092352)(ERR=0)).7........TNSLSNR for 32-bit Windows: Version 9.2.0.1.0 - Production..TNS for 32-bit Windows: Version 9.2.0.1.0 - Production..Windows NT Named Pipes NT Protocol Adapter for 32-bit Windows: Version 9.2.0.1.0 - Production..Windows NT TCP/IP NT Protocol Adapter for 32-bit Windows: Version 9.2.0.1.0 - Production,,.........@
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tnscmd10g`

官方给出的调用示例：`tnscmd10g version -h 192.168.1.205`

```text
root@kali:~# tnscmd10g version -h 192.168.1.205
sending (CONNECT_DATA=(COMMAND=version)) to 192.168.1.205:1521
writing 90 bytes
reading
.M.......6.........-. ..........(DESCRIPTION=(TMP=)(VSNNUM=153092352)(ERR=0)).7........TNSLSNR for 32-bit Windows: Version 9.2.0.1.0 - Production..TNS for 32-bit Windows: Version 9.2.0.1.0 - Production..Windows NT Named Pipes NT Protocol Adapter for 32-bit Windows: Version 9.2.0.1.0 - Production..Windows NT TCP/IP NT Protocol Adapter for 32-bit Windows: Version 9.2.0.1.0 - Production,,.........@
```

### `tnscmd10g（示例）`

官方给出的调用示例：`tnscmd10g -h`

```text
root@kali:~# tnscmd10g -h
usage: /usr/bin/tnscmd10g [command] -h hostname
       where 'command' is something like ping, version, status, etc.
       (default is ping)
       [-p port] - alternate TCP port to use (default is 1521)
       [--logfile logfile] - write raw packets to specified logfile
       [--indent] - indent & outdent on parens
       [--10G] - make it work against 10G
       [--rawcmd command] - build your own CONNECT_DATA string
       [--cmdsize bytes] - fake TNS command size (reveals packet leakage)
Updated on: 2026-Mar-02
 Edit this page
thc-ssl-dos
truecrack
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install tnscmd10g`，再执行 `tnscmd10g --version` 2>/dev/null || `tnscmd10g -V`
- [ ] **2.** **读官方帮助** —— `tnscmd10g -h`，需要细节时 `man tnscmd10g`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `tnscmd10g -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/tnscmd10g/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/tnscmd10g/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/tnscmd10g/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
