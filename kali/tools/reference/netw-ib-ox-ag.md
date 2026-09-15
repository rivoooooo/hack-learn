# netw-ib-ox-ag

> Graphical frontend for netwox Netwag is a graphical front end for netwox which contains more than 200 tools. Netwag permits one to easily: search amongst tools proposed in netwox construct command line run tools

> **功能分类**：通用工具 ｜ **Kali 包**：`netw-ib-ox-ag` ｜ **官方文档**：<https://www.kali.org/tools/netw-ib-ox-ag/>

## 1. 安装

```bash
sudo apt update
sudo apt install netwag
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.39.0 |
| 架构 | any |
| 可执行命令 | `netwag`、`netwag-doc`、`netwox`、`netwox-doc` |
| 依赖 | `netwox`、`tk` |
| 安装体积 | 328 KB |
| 官网 | <http://ntwox.sourceforge.net/> |
| 源码仓库 | <https://salsa.debian.org/debian/netw-ib-ox-ag> |
| 包追踪 | <https://pkg.kali.org/pkg/netw-ib-ox-ag> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
netwag -h          # 查看用法
man netwag         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `netwag`

官方给出的调用示例：`netwag -h`

```text
root@kali:~# netwag -h
application-specific initialization failed: Command-specific options:
 -sync:     Use synchronous mode for display server
 -colormap: Colormap for main window
 -display:  Display to use
 -geometry: Initial geometry for window
 -name:     Name to use for application
 -visual:   Visual for main window
 -use:      Id of window in which to embed application
 --:        Marks the end of the options
 -help:     Print summary of command-line options and abort
Error in startup script: can't read "tk_version": no such variable
    while executing
"netwag_glo_check_version "Tk" $tk_version 8"
    (file "/usr/bin/netwag" line 236)
```

### `man`

官方给出的调用示例：`man netwox`

```text
root@kali:~# man netwox
NETWOX(1)                   General Commands Manual                   NETWOX(1)
NAME
     netwox - examples/tools of the network library netwib
VERSION
     The version installed on this system is 5.39.0.
IMPORTANT
     Manpage   do   not   contain  a  lot  of  information.  Rather  read  net-
     wox-5.39.0-doc_html.tgz.
SYNOPSIS
     netwox number [ parameters... ]
     netwox number --help
     netwox number --help2
     netwox
PRESENTATION
     Toolbox netwox helps to find and solve network problems.
     It provides 223 tools :
      - udp/tcp clients/servers
      - spoofing
      - sniffing
      - address conversion
      - etc.
     Netwox is mainly oriented towards network administrators and security  au-
     ditors.
     Some tools are only a simplified implementation, while others are very so-
     phisticated.
     Netwox is available under the GNU GPL license.
DESCRIPTION
     number
            number of the tool to use
     parameters
            parameters  for  the  chosen  tool  number.  Parameter --help shows
            help.  Parameter --help2 shows description.
     When using netwox without number and  parameters,  it  enters  interactive
     help  mode.  In this mode, the user has to select a category by pressing a
     key. Then by choosing a tool number, its corresponding usage is displayed.
     Note: netwag is easier than interactive help mode.
EXAMPLES
     netwox 23 --help
            display simple help for tool number 23
     netwox 23 --help2
            display full description of tool 23. It also display  its  descrip-
            tion.
     netwox 23
            run tool 23
     netwox 23 --extended
            run tool 23 with --extended parameter
     netwox 23 -e
            run tool 23 with -e parameter (synonym for --extended)
     All   the   tools  are  not  described  in  this  manpage.   Reading  net-
     wox-5.39.0-doc_html.tgz is recommended.
SEE ALSO
     netwib(3) netwag(1)
                                   08/07/2012                         NETWOX(1)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install netwag`，再执行 `netwag --version` 2>/dev/null || `netwag -V`
- [ ] **2.** **读官方帮助** —— `netwag -h`，需要细节时 `man netwag`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `netwag -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/netw-ib-ox-ag/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/netw-ib-ox-ag/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/netw-ib-ox-ag/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
