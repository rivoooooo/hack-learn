# tinja

> CLI tool for testing web pages for template injection TInjA is a CLI tool for testing web pages for template injection vulnerabilities and supports 44 of the most relevant template engines for eight different programming languages.

> **功能分类**：通用工具 ｜ **Kali 包**：`tinja` ｜ **官方文档**：<https://www.kali.org/tools/tinja/>

## 1. 安装

```bash
sudo apt update
sudo apt install tinja
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.2.0 |
| 架构 | any |
| 可执行命令 | `tinja` |
| 依赖 | `libc6` |
| 安装体积 | 12.62 MB |
| 官网 | <https://github.com/Hackmanit/TInjA> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/tinja> |
| 包追踪 | <https://pkg.kali.org/pkg/tinja> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
tinja -h          # 查看用法
man tinja         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tinja`

> 官方示例调用：`tinja -h`

```text
root@kali:~# tinja -h
__/\\\\\\\\\\\\\\\__/\\\\\\\\\\\______________________________/\\\\\\\\\____
 _\///////\\\/////__\/////\\\///______________________/\\\___/\\\\\\\\\\\\\__
  _______\/\\\___________\/\\\________________________\///___/\\\/////////\\\_
   _______\/\\\___________\/\\\______/\\/\\\\\\_________/\\\_\/\\\_______\/\\\_
    _______\/\\\___________\/\\\_____\/\\\////\\\_______\/\\\_\/\\\\\\\\\\\\\\\_
     _______\/\\\___________\/\\\_____\/\\\__\//\\\______\/\\\_\/\\\/////////\\\_
      _______\/\\\___________\/\\\_____\/\\\___\/\\\__/\\_\/\\\_\/\\\_______\/\\\_
       _______\/\\\________/\\\\\\\\\\\_\/\\\___\/\\\_\//\\\\\\__\/\\\_______\/\\\_
        _______\///________\///////////__\///____\///___\//////___\///________\///__
the Template INJection Analyzer. (v1.2.0)
Published by Hackmanit under http://www.apache.org/licenses/LICENSE-2.0
Author: Maximilian Hildebrand
Repository: https://github.com/Hackmanit/TInjA
Usage:
  tinja [flags]
  tinja [command]
Available Commands:
  help        Help about any command
  jsonl       Scan using a JSONL file
  raw         Scan using a Raw file
  url         Scan a single or multiple URLs
Flags:
      --config string          set the path for a config file to be read
  -c, --cookie strings         add custom cookie(s)
      --csti                   enable scanning for Client-Side Template Injections using a headless browser
      --escapereport           escape HTML special chars in the JSON report
  -H, --header strings         add custom header(s)
  -h, --help                   help for tinja
      --precedinglength int    how many chars shall be memorized, when getting the preceding chars of a body reflection point (default 30)
      --proxycertpath string   set the path for the certificate of the proxy
      --proxyurl string        set the URL of the proxy
  -r, --ratelimit float        number of requests per seconds. 0 is infinite (default 0)
      --reportpath string      set the path for a report to be generated
      --subsequentlength int   how many chars shall be memorized, when getting the subsequent chars of a body reflection point (default 30)
      --testheaders strings    headers to test. E.g. --testheaders Host,Origin,X-Forwarded-For
      --timeout int            seconds until timeout (default 15)
      --useragentchrome        set chrome as user-agent. Default user-agent is 'TInjA v1.2.0'
  -v, --verbosity int          verbosity of the output. 0 = quiet, 1 = default, 2 = verbose (default 1)
      --version                version for tinja
Use "tinja [command] --help" for more information about a command.
Updated on: 2025-Dec-09
 Edit this page
tiger
traceroute
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install tinja`，再执行 `tinja --version` 2>/dev/null || `tinja -V`
- [ ] **2.** **读官方帮助** —— `tinja -h`，需要细节时 `man tinja`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/tinja/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/tinja/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/tinja/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
