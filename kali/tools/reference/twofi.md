# twofi

> Twitter words of interest When attempting to crack passwords custom word lists are very useful additions to standard dictionaries. An interesting idea originally released on the “7 Habits of Highly Effective Hackers” blog was to use Twitte…

> **功能分类**：信息搜集 ｜ **Kali 包**：`twofi` ｜ **官方文档**：<https://www.kali.org/tools/twofi/>

## 1. 安装

```bash
sudo apt update
sudo apt install twofi
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.0 |
| 架构 | all |
| 可执行命令 | `twofi` |
| 依赖 | `ruby`、`ruby-twitter` |
| 安装体积 | 38 KB |
| 官网 | <https://www.digininja.org/projects/twofi.php> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/twofi> |
| 包追踪 | <https://pkg.kali.org/pkg/twofi> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Video
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `twofi`

官方给出的调用示例：`twofi -h`

```text
root@kali:~# twofi -h
twoif 2.0-beta Robin Wood (
[email protected]
) (www.digininja.org)
twoif - Twitter Words of Interest
Usage: twoif [OPTIONS]
	--help, -h: show help
	--config <file>: config file, default is twofi.yml
	--count, -c: include the count with the words
	--min_word_length, -m: minimum word length
	--term_file, -T <file>: a file containing a list of terms
	--terms, -t: comma separated search terms
		quote words containing spaces, no space after commas
	--user_file, -U <file>: a file containing a list of users
	--users, -u: comma separated usernames
		quote words containing spaces, no space after commas
	--verbose, -v: verbose
Updated on: 2026-May-25
 Edit this page
trufflehog
unhide
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install twofi`，再执行 `twofi --version` 2>/dev/null || `twofi -V`
- [ ] **2.** **读官方帮助** —— `twofi -h`，需要细节时 `man twofi`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: twoif [OPTIONS]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/twofi/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/twofi/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/twofi/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
