# wgetpaste

> Command-line interface to various online pastebin services This package contains a script that automates pasting to a number of pastebin services.

> **功能分类**：通用工具 ｜ **Kali 包**：`wgetpaste` ｜ **官方文档**：<https://www.kali.org/tools/wgetpaste/>

## 1. 安装

```bash
sudo apt update
sudo apt install wgetpaste
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.30 |
| 架构 | all |
| 可执行命令 | `wgetpaste` |
| 依赖 | `wget` |
| 安装体积 | 49 KB |
| 官网 | <http://wgetpaste.zlin.dk/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/wgetpaste> |
| 包追踪 | <https://pkg.kali.org/pkg/wgetpaste> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
wgetpaste -h          # 查看用法
man wgetpaste         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wgetpaste`

官方给出的调用示例：`wgetpaste -h`

```text
root@kali:~# wgetpaste -h
Usage: /usr/bin/wgetpaste [options] [file[s]]
Options:
    -l, --language LANG           set language (defaults to "Plain Text")
    -d, --description DESCRIPTION set description (defaults to "stdin" or filename)
    -n, --nick NICK               set nick (defaults to your username)
    -s, --service SERVICE         set service to use (defaults to "dpaste")
    -e, --expiration EXPIRATION   set when it should expire (defaults to "30 days")
    -S, --list-services           list supported pastebin services
    -L, --list-languages          list languages supported by the specified service
    -E, --list-expiration         list expiration setting supported by the specified service
    -u, --tinyurl URL             convert input url to tinyurl
    -c, --command COMMAND         paste COMMAND and the output of COMMAND
    -i, --info                    append the output of `emerge --info`
    -I, --info-only               paste the output of `emerge --info` only
    -x, --xcut                    read input from clipboard (requires x11-misc/xclip)
    -X, --xpaste                  write resulting url to the X primary selection buffer (requires x11-misc/xclip)
    -C, --xclippaste              write resulting url to the X clipboard selection buffer (requires x11-misc/xclip)
    -r, --raw                     show url for the raw paste (no syntax highlighting or html)
    -t, --tee                     use tee to show what is being pasted
    -v, --verbose                 show wget stderr output if no url is received
        --completions             emit output suitable for shell completions (only affects --list-*)
        --debug                   be *very* verbose (implies -v)
    -h, --help                    show this help
    -g, --ignore-configs          ignore /etc/wgetpaste.conf, ~/.wgetpaste.conf etc.
        --version                 show version information
Defaults (DEFAULT_{NICK,LANGUAGE,EXPIRATION}[_${SERVICE}] and DEFAULT_SERVICE)
can be overridden globally in /etc/wgetpaste.conf or /etc/wgetpaste.d/*.conf or
per user in any of ~/.wgetpaste.conf or ~/.wgetpaste.d/*.conf.
An additional http header can be passed by setting HEADER_${SERVICE} in any of the
configuration files mentioned above. For example, authenticating with github gist:
HEADER_gists="Authorization: token 1234abc56789...", or with gitlab snippets:
HEADER_snippets="PRIVATE-TOKEN: 1234abc56789..."
You can also set PUBLIC_gists='false' if you want to default to secret instead of
public github gists. In the case of gitlab, you can set VISIBILITY_snippets= to
'public', 'private' or 'internal'"
To change your gitlab server, you can override the default API URL setting
URL_snippets='https://gitlab.[server].com/api/v4/snippets'
Updated on: 2025-Dec-09
 Edit this page
weevely
wifipumpkin3
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install wgetpaste`，再执行 `wgetpaste --version` 2>/dev/null || `wgetpaste -V`
- [ ] **2.** **读官方帮助** —— `wgetpaste -h`，需要细节时 `man wgetpaste`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: /usr/bin/wgetpaste [options] [file[s]]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wgetpaste/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wgetpaste/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wgetpaste/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
