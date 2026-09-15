# ruby-pedump

> Dump win32 PE executable files with a pure ruby This package contains a script to dump headers, sections, extract resources of win32 PE exe,dll,etc

> **功能分类**：通用工具 ｜ **Kali 包**：`ruby-pedump` ｜ **官方文档**：<https://www.kali.org/tools/ruby-pedump/>

## 1. 安装

```bash
sudo apt update
sudo apt install ruby-pedump
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.6.5 |
| 架构 | all |
| 可执行命令 | `ruby-pedump`、`pedump-ruby` |
| 依赖 | `ruby`、`ruby-awesome-print`、`ruby-iostruct`、`ruby-multipart-post`、`ruby-rainbow`、`ruby-zhexdump`、`pedump-ruby` |
| 安装体积 | 2.41 MB |
| 官网 | <http://github.com/zed-0xff/pedump> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ruby-pedump> |
| 包追踪 | <https://pkg.kali.org/pkg/ruby-pedump> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ruby-pedump -h          # 查看用法
man ruby-pedump         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pedump-ruby`

官方给出的调用示例：`pedump-ruby -h`

```text
root@kali:~# pedump-ruby -h
Usage: pedump [options]
        --version                    Print version information and exit
    -v, --verbose                    Run verbosely
                                     (can be used multiple times)
    -q, --quiet                      Silent any warnings
                                     (can be used multiple times)
    -F, --force                      Try to dump by all means
                                     (can cause exceptions & heavy wounds)
    -f, --format FORMAT              Output format: bin,c,dump,hex,inspect,json,table,yaml
                                     (default: table)
        --mz
        --dos-stub
        --rich
        --pe
        --ne
        --te
        --data-directory
    -S, --sections
        --tls
        --security
    -s, --strings
    -R, --resources
        --resource-directory
    -I, --imports
    -E, --exports
    -V, --version-info
        --packer
        --deep                       packer deep scan, significantly slower
    -P, --packer-only                packer/compiler detect only,
                                     mimics 'file' command output
    -r, --recursive                  recurse dirs in packer detect
        --all                        Dump all but resource-directory (default)
        --extract ID                 Extract a resource/section/data_dir
                                     ID: datadir:EXPORT     - datadir by type
                                     ID: resource:0x98478   - resource by offset
                                     ID: resource:ICON/#1   - resource by type & name
                                     ID: section:.text      - section by name
                                     ID: section:rva/0x1000 - section by RVA
                                     ID: section:raw/0x400  - section by RAW_PTR
        --va2file VA                 Convert RVA to file offset
    -W, --web                        Uploads files to a https://pedump.me
                                     for a nice HTML tables with image previews,
                                     candies & stuff
    -C, --console                    opens IRB console with specified file loaded
Updated on: 2025-Dec-09
 Edit this page
rubeus
s3scanner
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ruby-pedump`，再执行 `ruby-pedump --version` 2>/dev/null || `ruby-pedump -V`
- [ ] **2.** **读官方帮助** —— `ruby-pedump -h`，需要细节时 `man ruby-pedump`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: pedump [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ruby-pedump/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ruby-pedump/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ruby-pedump/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
