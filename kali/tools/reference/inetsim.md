# inetsim

> Software suite for simulating common internet services INetSim is a software suite for simulating common internet services in a lab environment, e.g. for analyzing the network behaviour of unknown malware samples. INetSim supports simulati…

> **功能分类**：数字取证 ｜ **Kali 包**：`inetsim` ｜ **官方文档**：<https://www.kali.org/tools/inetsim/>

## 1. 安装

```bash
sudo apt update
sudo apt install inetsim
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3.2 |
| 架构 | all |
| 可执行命令 | `inetsim` |
| 依赖 | `libdigest-sha-perl`、`libipc-shareable-perl`、`libnet-dns-perl`、`libnet-server-perl`、`openssl`、`perl` |
| 安装体积 | 1.07 MB |
| 官网 | <https://www.inetsim.org/index.html> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/inetsim> |
| 包追踪 | <https://pkg.kali.org/pkg/inetsim> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
inetsim -h          # 查看用法
man inetsim         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `inetsim`

官方给出的调用示例：`inetsim --help`

```text
root@kali:~# inetsim --help
INetSim 1.3.2 (2020-05-19) by Matthias Eckert & Thomas Hungenberg
Usage: /usr/bin/inetsim [options]
Available options:
  --help                         Print this help message.
  --version                      Show version information.
  --config=<filename>            Configuration file to use.
  --log-dir=<directory>          Directory logfiles are written to.
  --data-dir=<directory>         Directory containing service data.
  --report-dir=<directory>       Directory reports are written to.
  --bind-address=<IP address>    Default IP address to bind services to.
                                 Overrides configuration option 'default_bind_address'.
  --max-childs=<num>             Default maximum number of child processes per service.
                                 Overrides configuration option 'default_max_childs'.
  --user=<username>              Default user to run services.
                                 Overrides configuration option 'default_run_as_user'.
  --faketime-init-delta=<secs>   Initial faketime delta (seconds).
                                 Overrides configuration option 'faketime_init_delta'.
  --faketime-auto-delay=<secs>   Delay for auto incrementing faketime (seconds).
                                 Overrides configuration option 'faketime_auto_delay'.
  --faketime-auto-incr=<secs>    Delta for auto incrementing faketime (seconds).
                                 Overrides configuration option 'faketime_auto_increment'.
  --session=<id>                 Session id to use. Defaults to main process id.
  --pidfile=<filename>           Pid file to use. Defaults to '/run/inetsim.pid'.
Updated on: 2026-Aug-25
 Edit this page
i2c-tools
inspectrum
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install inetsim`，再执行 `inetsim --version` 2>/dev/null || `inetsim -V`
- [ ] **2.** **读官方帮助** —— `inetsim -h`，需要细节时 `man inetsim`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: /usr/bin/inetsim [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/inetsim/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/inetsim/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/inetsim/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
