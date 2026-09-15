# zonedb

> Public Zone Database (program) This package provides a free, open-source database ( http://opendatacommons.org/licenses/odbl/1.0/ ) containing a list and associated metadata of public DNS zones

> **功能分类**：通用工具 ｜ **Kali 包**：`zonedb` ｜ **官方文档**：<https://www.kali.org/tools/zonedb/>

## 1. 安装

```bash
sudo apt update
sudo apt install zonedb
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0.3170 |
| 架构 | any |
| 可执行命令 | `golang-github-zonedb-zonedb-dev`、`zonedb` |
| 依赖 | `libc6` |
| 安装体积 | 14.86 MB |
| 官网 | <https://github.com/zonedb/zonedb> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/zonedb> |
| 包追踪 | <https://pkg.kali.org/pkg/zonedb> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
golang-github-zonedb-zonedb-dev -h          # 查看用法
man golang-github-zonedb-zonedb-dev         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `zonedb`

官方给出的调用示例：`zonedb -h`

```text
root@kali:~# zonedb -h
Usage: zonedb [arguments] <command>
Available arguments:
  -add-languages string
    	add BCP 47 language tags to zones (comma-delimited)
  -add-locations string
    	add locations to zones (comma-delimited)
  -add-rdap-url string
    	add RDAP URL to zones
  -add-tags string
    	add tags to zones (comma-delimited)
  -c int
    	number of concurrent connections (default 32)
  -dir string
    	data directory (location of zones.txt and metadata dir) (default "/var/lib/zonedb")
  -exclude-tags string
    	exclude working zones with tags (comma-delimited)
  -generate-go
    	generate Go source code to specified directory
  -grep string
    	filter working zones by regular expression across all metadata
  -guess-languages
    	guess BCP 47 languages for zones
  -list
    	list working zones
  -list-locations
    	list locations in working zones
  -list-tags
    	list tags in working zones
  -list-wildcards
    	list zones with wildcarded DNS
  -ps
    	check against Public Suffix List
  -remove-locations string
    	remove locations from zones (comma-delimited)
  -remove-tags string
    	remove tags from zones (comma-delimited)
  -set-info-url string
    	set zone(s) info URLs
  -tags string
    	filter working zones by tags (comma-delimited)
  -tlds
    	work on top-level domains only
  -update
    	update all (root zone, whois, IANA data, IDN tables)
  -update-iana
    	query IANA for metadata
  -update-idn
    	query IANA for IDN tables
  -update-info-url
    	update zone(s) info URLs
  -update-ns
    	update name servers
  -update-rdap
    	query IANA for RDAP URLs
  -update-root
    	retrieve updates to the root zone file
  -update-ruby-whois
    	query Ruby Whois for whois servers
  -update-whois
    	query whois-servers.net for whois servers
  -update-wildcards
    	update wildcard IPs
  -v	enable verbose logging
  -verify-ns
    	verify name servers
  -verify-whois
    	verify whois servers
  -w	write zones.txt and metadata
  -x string
    	filter working zones by regular expression
  -zones string
    	select specific working zones (comma-delimited)
Updated on: 2025-Dec-09
 Edit this page
zerofree
zsh-autosuggestions
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install zonedb`，再执行 `golang-github-zonedb-zonedb-dev --version` 2>/dev/null || `golang-github-zonedb-zonedb-dev -V`
- [ ] **2.** **读官方帮助** —— `golang-github-zonedb-zonedb-dev -h`，需要细节时 `man golang-github-zonedb-zonedb-dev`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: zonedb [arguments] <command>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/zonedb/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/zonedb/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/zonedb/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
