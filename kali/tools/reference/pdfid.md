# pdfid

> Scans PDF files for certain PDF keywords This tool is not a PDF parser, but it will scan a file to look for certain PDF keywords, allowing you to identify PDF documents that contain (for example) JavaScript or execute an action when opened…

> **功能分类**：数字取证 ｜ **Kali 包**：`pdfid` ｜ **官方文档**：<https://www.kali.org/tools/pdfid/>

## 1. 安装

```bash
sudo apt update
sudo apt install pdfid
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.2.10 |
| 架构 | all |
| 可执行命令 | `pdfid` |
| 依赖 | `python3`、`python3-pyzipper`、`python3-simplejson` |
| 安装体积 | 106 KB |
| 官网 | <https://blog.didierstevens.com/programs/pdf-tools/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/pdfid> |
| 包追踪 | <https://pkg.kali.org/pkg/pdfid> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# pdfid /usr/share/doc/texmf/fonts/lm/lm-info.pdf
PDFiD 0.0.12 /usr/share/doc/texmf/fonts/lm/lm-info.pdf
 PDF Header: %PDF-1.4
 obj                  526
 endobj               526
 stream               151
 endstream            151
 xref                   1
 trailer                1
 startxref              1
 /Page                 26
 /Encrypt               0
 /ObjStm                0
 /JS                    0
 /JavaScript            0
 /AA                    0
 /OpenAction            0
 /AcroForm              0
 /JBIG2Decode           0
 /RichMedia             0
 /Launch                0
 /EmbeddedFile          0
 /Colors > 2^24         0
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pdfid`

> 官方示例调用：`pdfid /usr/share/doc/texmf/fonts/lm/lm-info.pdf`

```text
root@kali:~# pdfid /usr/share/doc/texmf/fonts/lm/lm-info.pdf
PDFiD 0.0.12 /usr/share/doc/texmf/fonts/lm/lm-info.pdf
 PDF Header: %PDF-1.4
 obj                  526
 endobj               526
 stream               151
 endstream            151
 xref                   1
 trailer                1
 startxref              1
 /Page                 26
 /Encrypt               0
 /ObjStm                0
 /JS                    0
 /JavaScript            0
 /AA                    0
 /OpenAction            0
 /AcroForm              0
 /JBIG2Decode           0
 /RichMedia             0
 /Launch                0
 /EmbeddedFile          0
 /Colors > 2^24         0
```

### `pdfid -h`

> 官方示例调用：`pdfid -h`

```text
root@kali:~# pdfid -h
Usage: pdfid [options] [pdf-file|zip-file|url|@file] ...
Tool to test a PDF file
Arguments:
pdf-file and zip-file can be a single file, several files, and/or @file
@file: run PDFiD on each file listed in the text file specified
wildcards are supported
Source code put in the public domain by Didier Stevens, no Copyright
Use at your own risk
https://DidierStevens.com
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -s, --scan            scan the given directory
  -a, --all             display all the names
  -e, --extra           display extra data, like dates
  -f, --force           force the scan of the file, even without proper %PDF
                        header
  -d, --disarm          disable JavaScript and auto launch
  -p PLUGINS, --plugins=PLUGINS
                        plugins to load (separate plugins with a comma , ;
                        @file supported)
  -c, --csv             output csv data when using plugins
  -m MINIMUMSCORE, --minimumscore=MINIMUMSCORE
                        minimum score for plugin results output
  -v, --verbose         verbose (will also raise catched exceptions)
  -S SELECT, --select=SELECT
                        selection expression
  -n, --nozero          supress output for counts equal to zero
  -o OUTPUT, --output=OUTPUT
                        output to log file
  --pluginoptions=PLUGINOPTIONS
                        options for the plugin
  -l, --literalfilenames
                        take filenames literally, no wildcard matching
  --recursedir          Recurse directories (wildcards and here files (@...)
                        allowed)
Learn more with
OffSec
Want to learn more about pdfid? get access to in-depth training and hands-on labs:
MITRE D3FEND - Detect: 3.2.2. Basic Static Malware Analysis: Inspecting PDF Documents
Updated on: 2025-Dec-09
 Edit this page
pdfcrack
perl-cisco-copyconfig
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install pdfid`，再执行 `pdfid --version` 2>/dev/null || `pdfid -V`
- [ ] **2.** **读官方帮助** —— `pdfid -h`，需要细节时 `man pdfid`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: pdfid [options] [pdf-file|zip-file|url|@file] ...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/pdfid/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/pdfid/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/pdfid/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
