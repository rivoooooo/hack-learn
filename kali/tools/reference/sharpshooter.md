# sharpshooter

> Payload Generation Framework SharpShooter is a payload creation framework for the retrieval and execution of arbitrary CSharp source code. SharpShooter is capable of creating payloads in a variety of formats, including HTA, JS, VBS and WSF.

> **功能分类**：通用工具 ｜ **Kali 包**：`sharpshooter` ｜ **官方文档**：<https://www.kali.org/tools/sharpshooter/>

## 1. 安装

```bash
sudo apt update
sudo apt install sharpshooter
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.0 |
| 架构 | all |
| 可执行命令 | `sharpshooter` |
| 依赖 | `python3`、`python3-jsmin` |
| 安装体积 | 538 KB |
| 官网 | <https://github.com/mdsecactivebreach/SharpShooter> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sharpshooter> |
| 包追踪 | <https://pkg.kali.org/pkg/sharpshooter> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sharpshooter -h          # 查看用法
man sharpshooter         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sharpshooter`

> 官方示例调用：`sharpshooter -h`

```text
root@kali:~# sharpshooter -h
       _____ __                    _____ __                __
      / ___// /_  ____ __________ / ___// /_  ____  ____  / /____  _____
      \__ \/ __ \/ __ `/ ___/ __ \\__ \/ __ \/ __ \/ __ \/ __/ _ \/ ___/
     ___/ / / / / /_/ / /  / /_/ /__/ / / / / /_/ / /_/ / /_/  __/ /
    /____/_/ /_/\__,_/_/  / .___/____/_/ /_/\____/\____/\__/\___/_/
                         /_/
     Dominic Chell, @domchell, MDSec ActiveBreach, v2.0
usage: sharpshooter [-h] [--stageless] [--dotnetver <ver>] [--com <com>]
                    [--awl <awl>] [--awlurl <awlurl>] [--payload <format>]
                    [--sandbox <types>] [--amsi <amsi>] [--delivery <type>]
                    [--rawscfile <path>] [--shellcode] [--scfile <path>]
                    [--refs <refs>] [--namespace <ns>] [--entrypoint <ep>]
                    [--web <web>] [--dns <dns>] [--output <output>]
                    [--smuggle] [--template <tpl>]
options:
  -h, --help          show this help message and exit
  --stageless         Create a stageless payload
  --dotnetver <ver>   Target .NET Version: 2 or 4
  --com <com>         COM Staging Technique: outlook, shellbrowserwin, wmi, wscript, xslremote
  --awl <awl>         Application Whitelist Bypass Technique: wmic, regsvr32
  --awlurl <awlurl>   URL to retrieve XSL/SCT payload
  --payload <format>  Payload type: hta, js, jse, vbe, vbs, wsf, macro, slk
  --sandbox <types>   Anti-sandbox techniques:
                      [1] Key to Domain (e.g. 1=CONTOSO)
                      [2] Ensure Domain Joined
                      [3] Check for Sandbox Artifacts
                      [4] Check for Bad MACs
                      [5] Check for Debugging
  --amsi <amsi>       Use amsi bypass technique: amsienable
  --delivery <type>   Delivery method: web, dns, both
  --rawscfile <path>  Path to raw shellcode file for stageless payloads
  --shellcode         Use built in shellcode execution
  --scfile <path>     Path to shellcode file as CSharp byte array
  --refs <refs>       References required to compile custom CSharp,
                      e.g. mscorlib.dll,System.Windows.Forms.dll
  --namespace <ns>    Namespace for custom CSharp,
                      e.g. Foo.bar
  --entrypoint <ep>   Method to execute,
                      e.g. Main
  --web <web>         URI for web delivery
  --dns <dns>         Domain for DNS delivery
  --output <output>   Name of output file (e.g. maldoc)
  --smuggle           Smuggle file inside HTML
  --template <tpl>    Name of template file (e.g. mcafee)
Learn more with
OffSec
Want to learn more about sharpshooter? get access to in-depth training and hands-on labs:
PEN-300: 6.2.6. Phishing with Jscript: SharpShooter
PEN-300 course
Updated on: 2025-Dec-09
 Edit this page
secure-socket-funneling
shed
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sharpshooter`，再执行 `sharpshooter --version` 2>/dev/null || `sharpshooter -V`
- [ ] **2.** **读官方帮助** —— `sharpshooter -h`，需要细节时 `man sharpshooter`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sharpshooter -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sharpshooter/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sharpshooter/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sharpshooter/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
