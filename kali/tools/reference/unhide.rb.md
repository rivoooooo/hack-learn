# unhide.rb

> Forensics tool to find processes hidden by rootkits Unhide.rb is a forensics tool to find processes hidden by rootkits. It looks for active processes in many different ways. Processes found by some means but not others are considered to be…

> **功能分类**：通用工具 ｜ **Kali 包**：`unhide.rb` ｜ **官方文档**：<https://www.kali.org/tools/unhide.rb/>

## 1. 安装

```bash
sudo apt update
sudo apt install unhide.rb
```

| 项目 | 内容 |
|------|------|
| 版本 | 22 |
| 架构 | all |
| 可执行命令 | `unhide.rb` |
| 依赖 | `procps`、`ruby` |
| 安装体积 | 31 KB |
| 官网 | <https://launchpad.net/unhide.rb> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/unhide.rb> |
| 包追踪 | <https://pkg.kali.org/pkg/unhide.rb> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
unhide.rb -h          # 查看用法
man unhide.rb         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

官方给出的调用示例：`man unhide.rb`

```text
root@kali:~# man unhide.rb
unhide.rb(8)         unhide.rb - Finder of hidden processes        unhide.rb(8)
NAME
     unhide.rb  -  Scans  system  for  hidden  processes  and lists any hits on
     stderr.
SYNOPSIS
     unhide.rb
DESCRIPTION
     Scans the system for hidden processes.
     Progress  messages  are  printed  on  stdout  and  can  be  redirected  to
     /dev/null.
     Error  diagnostics  and  information  about  any hidden processes found is
     printed to stderr.
OPTIONS
     unhide.rb takes no options
EXIT STATUS
     0      No hidden processes found
     1      Something went wrong during scanning
     2      One or more hidden processes were detected
BUGS
     Report bugs to <
[email protected]
> or <https://bugs.launchpad.net/un-
     hide.rb>.
LICENSING
     unhide.rb is  licensed  under  the  GPL-3,  copyright  Johan  Walles  <jo-
[email protected]
>.
SEE ALSO
     rkhunter(8)
     The unhide.rb home page: <http://launchpad.net/unhide.rb>
NOTES
     unhide.rb  is  a Ruby port of unhide.  When it was first written, the Ruby
     port was about 10x faster than the original C program and had much  better
     diagnostics  when  hidden processes were found.   The original unhide pro-
     gram can be found at <http://www.unhide-forensics.info/>.
                                   March 2011                      unhide.rb(8)
Updated on: 2026-May-25
 Edit this page
unhide
vinetto
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install unhide.rb`，再执行 `unhide.rb --version` 2>/dev/null || `unhide.rb -V`
- [ ] **2.** **读官方帮助** —— `unhide.rb -h`，需要细节时 `man unhide.rb`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `unhide.rb -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/unhide.rb/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/unhide.rb/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/unhide.rb/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
