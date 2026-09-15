# zim

> Graphical text editor based on wiki technologies Zim is a graphical text editor used to maintain a collection of wiki pages. Each page can contain links to other pages, simple formatting and inline images. Pages are stored in a folder stru…

> **功能分类**：通用工具 ｜ **Kali 包**：`zim` ｜ **官方文档**：<https://www.kali.org/tools/zim/>

## 1. 安装

```bash
sudo apt update
sudo apt install zim
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.76.3 |
| 架构 | all |
| 可执行命令 | `zim` |
| 依赖 | `gir1.2-gtk-3.0`、`python3`、`python3-gi`、`python3-xdg`、`xdg-utils` |
| 安装体积 | 5.22 MB |
| 官网 | <https://zim-wiki.org> |
| 源码仓库 | <https://salsa.debian.org/debian/zim> |
| 包追踪 | <https://pkg.kali.org/pkg/zim> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
zim -h          # 查看用法
man zim         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

官方给出的调用示例：`man zim`

```text
root@kali:~# man zim
ZIM(1)                           User Commands                           ZIM(1)
NAME
     zim - A Desktop Wiki Editor
SYNOPSIS
     usage: zim [OPTIONS] [NOTEBOOK [PAGE_LINK]]
        or: zim --gui [OPTIONS] [NOTEBOOK [PAGE_LINK]]
        or: zim --server [OPTIONS] [NOTEBOOK]
        or: zim --export [OPTIONS] NOTEBOOK [PAGE]
        or: zim --import [OPTIONS] NOTEBOOK PAGE FILES
        or: zim --search [OPTIONS] NOTEBOOK QUERY
        or: zim --index  [OPTIONS] NOTEBOOK
        or: zim --plugin PLUGIN [ARGUMENTS]
        or: zim --manual [OPTIONS] [PAGE_LINK]
        or: zim --help
     NOTEBOOK  can  be  a  local file path, a local file URI or a notebook name
     PAGE is be a fully specified page name PAGE_LINK is a fully specified page
     name optionally extended with an anchor ID
DESCRIPTION
     Zim is a graphical text editor used  to  maintain  a  collection  of  wiki
     pages.  Each page can contain links to other pages, simple formatting, and
     images. Pages are stored in a folder structure, like in an  outliner,  and
     can  have  attachments.   Creating  a  new page is as easy as linking to a
     nonexistent page. All data is stored in plain text files with wiki format-
     ting. Various plugins provide additional functionality, like a  task  list
     manager, an equation editor, a tray icon, and support for version control.
     Zim can be used to:
     *      Keep an archive of notes
     *      Keep a daily or weekly journal
     *      Take notes during meetings or lectures
     *      Organize task lists
     *      Draft blog entries and emails
     *      Do brainstorming
OPTIONS
     General Options:
       --gui             run the editor (this is the default)
       --server          run the web server
       --export          export to a different format
       --import          import one or more files into a notebook
       --search          run a search query on a notebook
       --index           build an index for a notebook
       --plugin          call a specific plugin function
       --manual          open the user manual
       -V, --verbose     print information to terminal
       -D, --debug       print debug messages
       -v, --version     print version and exit
       -h, --help        print this text
     GUI Options:
       --list            show the list with notebooks instead of
                         opening the default notebook
       --geometry        window size and position as WxH+X+Y
       --fullscreen      start in fullscreen mode
       --non-unique       start  a  new  process, do not connect to an existing
     process
       --standalone      start a new process per notebook, implies --non-unique
     Server Options:
       --port            port to use (defaults to 8080)
       --template        name or filepath of the template to use
       --private         serve only to localhost
       --gui             run the gui wrapper for the server
     Export Options:
       -o, --output      output directory (mandatory option)
       --format          format to use (defaults to 'html')
       --template        name or filepath of the template to use
       --root-url        url to use for the document root
       --index-page      index page name
       -r, --recursive   when exporting a page, also export sub-pages
       -s, --singlefile  export all pages to a single output file
       -O, --overwrite   force overwriting existing file(s)
     Import Options:
       --format          format to read (defaults to 'wiki')
       --assubpage       import files as sub-pages of PATH,  this  is  implicit
     true
                         when  PATH  ends with a ":" or when multiple files are
     given
     Search Options:
       -s, --with-scores print score for each page, sort by score
     Index Options:
       -f, --flush       flush the index first and force re-building
     Try 'zim --manual' for more help.
AUTHOR
     Jaap Karssenberg <
[email protected]
>
SEE ALSO
     The full documentation for zim is maintained as a zim notebook.  The  com-
     mand
            zim --manual
     should give you access to the complete manual.
     The website for zim can be found at https://www.zim-wiki.org
zim 0.76.3                         March 2026                            ZIM(1)
Updated on: 2026-May-25
 Edit this page
xclip
binwalk3
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install zim`，再执行 `zim --version` 2>/dev/null || `zim -V`
- [ ] **2.** **读官方帮助** —— `zim -h`，需要细节时 `man zim`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `zim -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/zim/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/zim/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/zim/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
