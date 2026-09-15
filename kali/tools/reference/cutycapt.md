# cutycapt

> Utility to capture WebKit’s rendering of a web page CutyCapt is a small cross-platform command-line utility to capture WebKit’s rendering of a web page into a variety of vector and bitmap formats, including SVG, PDF, PS, PNG, JPEG, TIFF, G…

> **功能分类**：Web 应用 ｜ **Kali 包**：`cutycapt` ｜ **官方文档**：<https://www.kali.org/tools/cutycapt/>

## 1. 安装

```bash
sudo apt update
sudo apt install cutycapt
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0 |
| 架构 | any |
| 可执行命令 | `cutycapt` |
| 依赖 | `libc6`、`libgcc-s1`、`libqt5core5t64` |
| 安装体积 | 76 KB |
| 官网 | <https://github.com/Crystalix007/CutyCapt> |
| 源码仓库 | <https://salsa.debian.org/debian/cutycapt> |
| 包追踪 | <https://pkg.kali.org/pkg/cutycapt> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Take a capture of the URL (–url=http://www.kali.org) and save it to disk (–out=kali.png):
root@kali:~# cutycapt --url=http://www.kali.org --out=kali.png
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cutycapt`

官方给出的调用示例：`cutycapt --url=http://www.kali.org --out=kali.png`

```text
root@kali:~# cutycapt --url=http://www.kali.org --out=kali.png
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
```

### `man`

官方给出的调用示例：`man cutycapt`

```text
root@kali:~# man cutycapt
CUTYCAPT(1)                 General Commands Manual                 CUTYCAPT(1)
NAME
     cutycapt - utility to capture WebKit's rendering of a web page
SYNOPSIS
     cutycapt [options] --url=http://www.someurl.com --out=output.png
DESCRIPTION
     This manual page documents briefly the cutycapt command.
     CutyCapt  is  a  small  cross-platform command-line utility to capture We-
     bKit's rendering of a web page into a variety of vector  and  bitmap  for-
     mats, including SVG, PDF, PS, PNG, JPEG, TIFF, GIF, and BMP.
OPTIONS
     A summary of options is included below.
     --help
            Show summary of options.
     --url=<url>
            The URL to capture (http:...|file:...|...)
     --out=<path>
            The target file (.png|pdf|ps|svg|jpeg|...)
     --out-format=<f>
            Like extension in --out, overrides heuristic
     --min-width=<int>
            Minimal width for the image (default: 800)
     --min-height=<int>
            Minimal height for the image (default: 600)
     --max-wait=<ms>
            Don't wait more than (default: 90000, infinite: 0)
     --delay=<ms>
            After successful load, wait (default: 0)
     --user-style-path=<path>
            Location of user style sheet file, if any
     --user-style-string=<css>
            User style rules specified as text
     --header=<name>:<value>
            Request header; repeatable; some can't be set
     --method=<get|post|put>
            Specifies the request method (default: get)
     --body-string=<string>
            Unencoded request body (default: none)
     --body-base64=<base64>
            Base64-encoded request body (default: none)
     --app-name=<name>
            Application name used in User-Agent; default is none
     --app-version=<version>
            Application version used in User-Agent; default is none
     --user-agent=<string>
            Override the User-Agent header Qt would set
     --javascript=<on|off>
            JavaScript execution (default: on)
     --java=<on|off>
            Java execution (default: unknown)
     --plugins=<on|off>
            Plugin execution (default: unknown)
     --private-browsing=<on|off>
            Private browsing (default: unknown)
     --auto-load-images=<on|off>
            Automatic image loading (default: on)
     --js-can-open-windows=<on|off>
            Script can open windows? (default: unknown)
     --js-can-access-clipboard=<on|off>
            Script clipboard privs (default: unknown)
     --print-backgrounds=<on|off>
            Backgrounds in PDF/PS output (default: off)
     --zoom-factor=<float>
            Page zoom factor (default: no zooming)
     --zoom-text-only=<on|off>
            Whether to zoom only the text (default: off)
     --http-proxy=<url>
            Address for HTTP proxy server (default: none)
AUTHOR
     CutyCapt was written by Bjorn Hohrmann <
[email protected]
>.
     This  manual page was written by David Paleino <
[email protected]
>, for the
     Debian project (and may be used by others), and is licensed under the  GNU
     General Public License, version 2 or later.
                                 June 28, 2010                      CUTYCAPT(1)
Updated on: 2026-May-25
 Edit this page
cutecom
detect-it-easy
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cutycapt`，再执行 `cutycapt --version` 2>/dev/null || `cutycapt -V`
- [ ] **2.** **读官方帮助** —— `cutycapt -h`，需要细节时 `man cutycapt`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `cutycapt -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cutycapt/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cutycapt/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cutycapt/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
