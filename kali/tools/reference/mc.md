# mc

> Midnight Commander - a powerful file manager GNU Midnight Commander is a text-mode full-screen file manager. It uses a two panel interface and a subshell for command execution. It includes an internal editor with syntax highlighting and an…

> **功能分类**：通用工具 ｜ **Kali 包**：`mc` ｜ **官方文档**：<https://www.kali.org/tools/mc/>

## 1. 安装

```bash
sudo apt update
sudo apt install mc
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.8.33 |
| 架构 | any |
| 可执行命令 | `mc`、`mcdiff`、`mcedit`、`mcview`、`mc-data` |
| 依赖 | `libc6`、`libext2fs2t64`、`libglib2.0-0t64`、`libgpm2`、`libslang2`、`libssh2-1t64`、`mc-data` |
| 安装体积 | 1.55 MB |
| 官网 | <https://www.midnight-commander.org> |
| 源码仓库 | <https://salsa.debian.org/debian/mc> |
| 包追踪 | <https://pkg.kali.org/pkg/mc> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
mc -h          # 查看用法
man mc         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 5 个可执行命令，下面是官方页面内嵌的帮助原文。

### `mc`

官方给出的调用示例：`mc -h`

```text
root@kali:~# mc -h
Usage:
  mc [OPTION…] [this_dir] [other_panel_dir]
GNU Midnight Commander 4.8.33
Help Options:
  -h, --help               Show help options
  --help-all               Show all help options
  --help-terminal          Terminal options
  --help-color             Color options
Application Options:
  -V, --version            Displays the current version
  -f, --datadir            Print data directory
  -F, --datadir-info       Print extended info about used data directories
  --configure-options      Print configure options
  -P, --printwd=<file>     Print last working directory to specified file
  -U, --subshell           Enables subshell support (default)
  -u, --nosubshell         Disables subshell support
  -l, --ftplog=<file>      Log ftp dialog to specified file
  -v, --view=<file>        Launches the file viewer on a file
  -e, --edit=<file> ...    Edit files
Please send any bug reports (including the output of 'mc -V')
as tickets at www.midnight-commander.org
```

### `mcdiff`

官方给出的调用示例：`mcdiff -h`

```text
root@kali:~# mcdiff -h
Usage:
  mcdiff [OPTION…] file1 file2
GNU Midnight Commander 4.8.33
Help Options:
  -h, --help               Show help options
  --help-all               Show all help options
  --help-terminal          Terminal options
  --help-color             Color options
Application Options:
  -V, --version            Displays the current version
  -f, --datadir            Print data directory
  -F, --datadir-info       Print extended info about used data directories
  --configure-options      Print configure options
  -P, --printwd=<file>     Print last working directory to specified file
  -U, --subshell           Enables subshell support (default)
  -u, --nosubshell         Disables subshell support
  -l, --ftplog=<file>      Log ftp dialog to specified file
  -v, --view=<file>        Launches the file viewer on a file
  -e, --edit=<file> ...    Edit files
Please send any bug reports (including the output of 'mc -V')
as tickets at www.midnight-commander.org
```

### `mcedit`

官方给出的调用示例：`mcedit -h`

```text
root@kali:~# mcedit -h
Usage:
  mcedit [OPTION…] [+lineno] file1[:lineno] [file2[:lineno]...]
GNU Midnight Commander 4.8.33
Help Options:
  -h, --help               Show help options
  --help-all               Show all help options
  --help-terminal          Terminal options
  --help-color             Color options
Application Options:
  -V, --version            Displays the current version
  -f, --datadir            Print data directory
  -F, --datadir-info       Print extended info about used data directories
  --configure-options      Print configure options
  -P, --printwd=<file>     Print last working directory to specified file
  -U, --subshell           Enables subshell support (default)
  -u, --nosubshell         Disables subshell support
  -l, --ftplog=<file>      Log ftp dialog to specified file
  -v, --view=<file>        Launches the file viewer on a file
  -e, --edit=<file> ...    Edit files
Please send any bug reports (including the output of 'mc -V')
as tickets at www.midnight-commander.org
```

### `mcview`

官方给出的调用示例：`mcview -h`

```text
root@kali:~# mcview -h
Usage:
  mcview [OPTION…] file
GNU Midnight Commander 4.8.33
Help Options:
  -h, --help               Show help options
  --help-all               Show all help options
  --help-terminal          Terminal options
  --help-color             Color options
Application Options:
  -V, --version            Displays the current version
  -f, --datadir            Print data directory
  -F, --datadir-info       Print extended info about used data directories
  --configure-options      Print configure options
  -P, --printwd=<file>     Print last working directory to specified file
  -U, --subshell           Enables subshell support (default)
  -u, --nosubshell         Disables subshell support
  -l, --ftplog=<file>      Log ftp dialog to specified file
  -v, --view=<file>        Launches the file viewer on a file
  -e, --edit=<file> ...    Edit files
Please send any bug reports (including the output of 'mc -V')
as tickets at www.midnight-commander.org
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install mc`，再执行 `mc --version` 2>/dev/null || `mc -V`
- [ ] **2.** **读官方帮助** —— `mc -h`，需要细节时 `man mc`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/mc/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/mc/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/mc/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
