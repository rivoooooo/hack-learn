# unblob

> Accurate, fast, and easy-to-use extraction suite (Python 3) This package contains an accurate, fast, and easy-to-use extraction suite. It parses unknown binary blobs for more than 30 different archive, compression, and file-system formats,…

> **功能分类**：通用工具 ｜ **Kali 包**：`unblob` ｜ **官方文档**：<https://www.kali.org/tools/unblob/>

## 1. 安装

```bash
sudo apt update
sudo apt install unblob
```

| 项目 | 内容 |
|------|------|
| 版本 | 26.6.4 |
| 架构 | amd64 |
| 可执行命令 | `unblob` |
| 依赖 | `libc6`、`libgcc-s1`、`python3`、`python3-arpy`、`python3-attr`、`python3-click`、`python3-cryptography`、`python3-dissect.cstruct`、`python3-jefferson`、`python3-lark`、`python3-lief`、`python3-lz4` 等 |
| 安装体积 | 1.20 MB |
| 官网 | <https://unblob.org/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/unblob> |
| 包追踪 | <https://pkg.kali.org/pkg/unblob> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
unblob -h          # 查看用法
man unblob         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `unblob`

官方给出的调用示例：`unblob -h`

```text
root@kali:~# unblob -h
Usage: unblob [OPTIONS] FILE
  A tool for getting information out of any kind of binary blob.
  You also need these extractor commands to be able to extract the supported
  file types: 7z, debugfs, fsck.erofs, jefferson, lz4, lziprecover, lzop,
  partclone.restore, sasquatch, sasquatch-v4be, simg2img,
  ubireader_extract_files, ubireader_extract_images, unar, zstd
  NOTE: Some older extractors might not be compatible.
Options:
  -e, --extract-dir DIRECTORY     Extract the files to this directory. Will be
                                  created if doesn't exist.
  -f, --force                     Force extraction even if outputs already
                                  exist (they are removed).
  -d, --depth INTEGER RANGE       Recursion depth. How deep should we extract
                                  containers.  [default: 10; x>=1]
  -n, --randomness-depth INTEGER RANGE
                                  Entropy calculation depth. How deep should
                                  we calculate randomness for unknown files? 1
                                  means input files only, 0 turns it off.
                                  [default: 1; x>=0]
  -P, --plugins-path PATH         Load plugins from the provided path.
  -S, --skip-magic TEXT           Skip processing files with given magic
                                  prefix. The provided values are appended to
                                  unblob's own skip magic list unless --clear-
                                  skip-magic is provided. [default: BFLT,
                                  Erlang BEAM file, GIF, GNU message catalog,
                                  HP Printer Job Language, JPEG, Java module
                                  image, MPEG, MS Windows icon resource,
                                  Macromedia Flash data, Microsoft Excel,
                                  Microsoft PowerPoint, Microsoft Word,
                                  OpenDocument, PDF document, PNG, SQLite,
                                  TrueType Font data, Web Open Font Format,
                                  Windows Embedded CE binary image, Xilinx BIT
                                  data, compiled Java class, magic binary
                                  file, python]
  --skip-extension TEXT           Skip processing files with given extension
                                  [default: .rlib]
  --clear-skip-magics             Clear unblob's own skip magic list.
  -p, --process-num INTEGER RANGE
                                  Number of worker processes to process files
                                  parallelly.  [default: 6; x>=1]
  --report PATH                   File to store metadata generated during the
                                  extraction process (in JSON format).
  --log PATH                      File to save logs (in text format). Defaults
                                  to unblob.log.
  -s, --skip-extraction           Only carve chunks and skip further
                                  extraction
  --no-sandbox                    Disable Landlock sandboxing (useful for
                                  breakpoint-based debugging).
  -k, --keep-extracted-chunks     Keep extracted chunks
  --delete-extracted-files TEXT   Delete fully extracted intermediate files
                                  (whole-file chunks only). Use
                                  'selected:<handler1,handler2>' (comma-
                                  separated) to restrict deletions to specific
                                  handlers.  [default: none]
  --carve-suffix TEXT             Carve directory name is source file + this
                                  suffix. NOTE: carving is skipped when the
                                  whole file is of a known type  [default:
                                  _extract]
  --extract-suffix TEXT           Extraction directory name is source file +
                                  this suffix  [default: _extract]
  -v, --verbose                   Verbosity level, counting, maximum level: 3
                                  (use: -v, -vv, -vvv)
  --show-external-dependencies    Shows commands needs to be available for
                                  unblob to work properly
  --build-handlers-doc TEXT       Build handlers markdown documentation
  --version                       Shows unblob version
  -h, --help                      Show this message and exit.
Updated on: 2026-Aug-25
 Edit this page
unar
unix-privesc-check
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install unblob`，再执行 `unblob --version` 2>/dev/null || `unblob -V`
- [ ] **2.** **读官方帮助** —— `unblob -h`，需要细节时 `man unblob`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: unblob [OPTIONS] FILE`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/unblob/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/unblob/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/unblob/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
