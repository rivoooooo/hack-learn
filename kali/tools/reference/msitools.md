# msitools

> Windows Installer file manipulation tool msitools contains a number of programs to create, inspect and extract Windows Installer (.msi) files. The following tools are included: msiinfo: inspects MSI packages msibuild: builds MSI packages

> **功能分类**：通用工具 ｜ **Kali 包**：`msitools` ｜ **官方文档**：<https://www.kali.org/tools/msitools/>

## 1. 安装

```bash
sudo apt update
sudo apt install msitools
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.106 |
| 架构 | any |
| 可执行命令 | `gir1.2-libmsi-1.0`、`libmsi-1.0-0`、`libmsi-dev`、`msitools`、`msibuild`、`msidiff`、`msidump`、`msiextract`、`msiinfo`、`wixl`、`wixl-heat`、`wixl-data` |
| 依赖 | `libc6`、`libgcab-1.0-0`、`libglib2.0-0t64`、`libmsi-1.0-0`、`msibuild` |
| 安装体积 | 306 KB |
| 官网 | <https://wiki.gnome.org/msitools> |
| 源码仓库 | <https://salsa.debian.org/debian/msitools> |
| 包追踪 | <https://pkg.kali.org/pkg/msitools> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gir1.2-libmsi-1.0 -h          # 查看用法
man gir1.2-libmsi-1.0         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 12 个可执行命令，下面是官方页面内嵌的帮助原文。

### `msibuild`

> 官方示例调用：`msibuild -h`

```text
root@kali:~# msibuild -h
Usage: msibuild MSIFILE [OPTION]...
Options:
  -s name [author] [template] [uuid] Set summary information.
  -q query         Execute SQL query/queries.
  -i table1.idt    Import one table into the database.
  -a stream file   Add 'stream' to storage with contents of 'file'.
Existing tables or streams will be overwritten. If package.msi does not exist a new file
will be created with an empty database.
```

### `msidiff`

> 官方示例调用：`msidiff -h`

```text
root@kali:~# msidiff -h
msidiff diffs contents of two MSI files.
Usage: msidiff [OPTION]... [DIFF-OPTIONS] FROM-MSI TO-MSI
Options:
  -t, --tables     Diff MSI tables as text.  This is the default.
  -l, --list       Diff lists of files.
  -L, --long-list  Diff long lists (akin to 'find -ls') of files.
  -h, --help       Print help message and exit.
  -v, --version    Print version information and exit.
  diff-options     Options passed to diff(1).  The first repeated argument of
                   the above or the first argument starting with a '-' but not
                   one of the above starts diff-options, the first one not
                   starting with it ends them.  Default: -Nup for contents
                   (in addition to -r which will always be passed), -U0 for
                   others.
More than one of -t, -l or -L may be specified.
Report bugs to <https://gitlab.gnome.org/GNOME/msitools/issues>.
```

### `msidump`

> 官方示例调用：`msidump -h`

```text
root@kali:~# msidump -h
msidump dumps MSI tables as idt text and streams
Usage: msidump [OPTION]... MSI-FILE
Options:
  -t, --tables         Dump tables.  This is the default.
  -s, --streams        Dump streams
  -S, --signature      Dump asn1parse of digital signature.
  -d, --directory DIR  Dump to given directory DIR
  -h, --help           Print help message and exit.
  -v, --version        Print version information and exit.
More than one of -t, -s or -S may be specified.
Report bugs to <https://gitlab.gnome.org/GNOME/msitools/issues>.
```

### `msiextract`

> 官方示例调用：`msiextract -h`

```text
root@kali:~# msiextract -h
Usage:
  msiextract [OPTION…] MSI_FILE... - a msi files extracting tool
Help Options:
  -h, --help          Show help options
Application Options:
  --version           Display version number
  -C, --directory     Extract to directory
  -l, --list          List files only
```

### `msiinfo`

> 官方示例调用：`msiinfo -h`

```text
root@kali:~# msiinfo -h
Usage: msiinfo SUBCOMMAND COMMAND-OPTIONS...
Options:
  -h, --help        Show program usage
  -v, --version     Display program version
Available subcommands:
  help              Show program or subcommand usage
  streams           List streams in a .msi file
  tables            List tables in a .msi file
  extract           Extract a binary stream from an .msi file
  export            Export a table in text form from an .msi file
  suminfo           Print summary information
```

### `wixl`

> 官方示例调用：`wixl -h`

```text
root@kali:~# wixl -h
Usage:
  wixl [OPTION…] INPUT_FILE1 [INPUT_FILE2]... - a msi building tool
Help Options:
  -h, --help                          Show help options
Application Options:
  --version                           Display version number
  -v, --verbose                       Verbose output
  -o, --output                        Output file
  -D, --define                        Define variable
  -a, --arch                          Target architecture
  -I, --includedir                    Include directory
  --extdir                            System extension directory
  --wxidir                            System include directory
  -E, --only-preproc                  Stop after the preprocessing stage
  --ext                               Specify an extension
```

### `wixl-heat`

> 官方示例调用：`wixl-heat -h`

```text
root@kali:~# wixl-heat -h
Usage:
  wixl-heat [OPTION…]
Help Options:
  -h, --help            Show help options
Application Options:
  --directory-ref       Directory Ref
  --component-group     Component Group
  --var                 Variable for source dir
  -p, --prefix          Prefix
  -x, --exclude         Exclude prefix
  --win64               Add Win64 Component
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install msitools`，再执行 `gir1.2-libmsi-1.0 --version` 2>/dev/null || `gir1.2-libmsi-1.0 -V`
- [ ] **2.** **读官方帮助** —— `gir1.2-libmsi-1.0 -h`，需要细节时 `man gir1.2-libmsi-1.0`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: msibuild MSIFILE [OPTION]...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/msitools/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/msitools/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/msitools/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
