# tcpick

> TCP stream sniffer and connection tracker This libpcap-based textmode sniffer can: track, reassemble and reorder TCP streams save the captured flows in different files or display them in the terminal display all the stream on the terminal …

> **功能分类**：数字取证 ｜ **Kali 包**：`tcpick` ｜ **官方文档**：<https://www.kali.org/tools/tcpick/>

## 1. 安装

```bash
sudo apt update
sudo apt install tcpick
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.2.1 |
| 架构 | any |
| 可执行命令 | `tcpick` |
| 依赖 | `libc6`、`libpcap0.8t64` |
| 安装体积 | 88 KB |
| 官网 | <http://tcpick.sourceforge.net> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/tcpick> |
| 包追踪 | <https://pkg.kali.org/pkg/tcpick> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
tcpick -h          # 查看用法
man tcpick         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tcpick`

官方给出的调用示例：`tcpick --help`

```text
root@kali:~# tcpick --help
	tcpick 0.2.1 is a sniffer tool written using libpcap.
tcpick can keep track of tcp connection, sniff all tcp streams
and store them to files, to show you what is happening on a network interface
Usage: tcpick [ -a ] [ -n ] [ -C ]
       [ -i interface ]
       [ -yH ] [ -yP ] [ -yR ] [ -yU ] [ -yx ] [ -yX ]
       [ -bH ] [ -bP ] [ -bR ] [ -bU ] [ -bx ] [ -bX ]
       [ -wH ] [ -wP ] [ -wR ] [ -wU ]
       [ -v  [ verbosity ]]
       [ -S ] [ -h ] [ --separator ]
       [  "filter" ] [ -r  file ]
       [ --help ] [ --version ]
Example: tcpick -i ppp0 -yP -C -h "not port 22"
for an updated list of options see tcpick(1) manpage
to see version and license information try `tcpick --version'
or read the `COPYING' file, released with the package
tcpick homepage: http://tcpick.sourceforge.net
mailing-list address:
	<
[email protected]
>
Archive:
	http://sourceforge.net/mailarchive/forum.php?forum=tcpick-project
Subscribe:
	http://lists.sourceforge.net/lists/listinfo/tcpick-project
thank you for using tcpick!
Updated on: 2025-Dec-09
 Edit this page
tcpflow
teamsploit
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install tcpick`，再执行 `tcpick --version` 2>/dev/null || `tcpick -V`
- [ ] **2.** **读官方帮助** —— `tcpick -h`，需要细节时 `man tcpick`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: tcpick [ -a ] [ -n ] [ -C ]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/tcpick/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/tcpick/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/tcpick/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
