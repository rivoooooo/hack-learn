# mdbtools

> JET / MS Access database (MDB) tools These are various tools for manipulating JET / MS Access database (MDB) files: utils - provides command line utilities to list tables, export schema, and data, show file versions, and other useful stuff…

> **功能分类**：数字取证 ｜ **Kali 包**：`mdbtools` ｜ **官方文档**：<https://www.kali.org/tools/mdbtools/>

## 1. 安装

```bash
sudo apt update
sudo apt install mdbtools
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0.1 |
| 架构 | any |
| 可执行命令 | `libmdb3t64`、`libmdbsql3t64`、`mdbtools`、`mdb-array`、`mdb-count`、`mdb-export`、`mdb-header`、`mdb-hexdump`、`mdb-import`、`mdb-json`、`mdb-parsecsv`、`mdb-prop`、`mdb-queries`、`mdb-schema`、`mdb-sql`、`mdb-tables`、`mdb-ver`、`mdbtools-dev`、`mdbtools-doc`、`odbc-mdbtools` |
| 依赖 | `libc6`、`libglib2.0-0t64`、`libmdb3t64`、`libmdbsql3t64`、`libreadline8t64`、`mdb-array` |
| 安装体积 | 268 KB |
| 官网 | <https://github.com/mdbtools/mdbtools> |
| 源码仓库 | <https://salsa.debian.org/debian/mdbtools> |
| 包追踪 | <https://pkg.kali.org/pkg/mdbtools> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libmdb3t64 -h          # 查看用法
man libmdb3t64         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 20 个可执行命令，下面是官方页面内嵌的帮助原文。

### `mdb-array`

官方给出的调用示例：`mdb-array -h`

```text
root@kali:~# mdb-array -h
mdb-array is deprecated and will disappear in a future version of mdbtools.
Please drop us a line if you have any use of it.
See https://github.com/mdbtools/mdbtools/issues/197
Usage: mdb-array <file> <table>
```

### `mdb-count`

官方给出的调用示例：`mdb-count -h`

```text
root@kali:~# mdb-count -h
Usage:
  mdb-count [OPTION…] <file> <table> - print the number of records in an Access database
Help Options:
  -h, --help       Show help options
Application Options:
  --version        Show mdbtools version and exit
```

### `mdb-export`

官方给出的调用示例：`mdb-export -h`

```text
root@kali:~# mdb-export -h
Usage:
  mdb-export [OPTION…] <file> <table> - export data from MDB file
Help Options:
  -h, --help                        Show help options
Application Options:
  -H, --no-header                   Suppress header row.
  -d, --delimiter=char              Specify an alternative column delimiter. Default is comma.
  -R, --row-delimiter=char          Specify a row delimiter
  -Q, --no-quote                    Don't wrap text-like fields in quotes.
  -q, --quote=char                  Use <char> to wrap text-like fields. Default is double quote.
  -X, --escape=format               Use <char> to escape quoted characters within a field. Default is doubling.
  -e, --escape-invisible            Use C-style escaping for return (\r), tab (\t), line-feed (\n), and back-slash (\\) characters. Default is to leave as they are.
  -I, --insert=backend              INSERT statements (instead of CSV)
  -N, --namespace=namespace         Prefix identifiers with namespace
  -S, --batch-size=int              Size of insert batches on supported platforms.
  -D, --date-format=format          Set the date format (see strftime(3) for details)
  -T, --datetime-format=format      Set the date/time format (see strftime(3) for details)
  -0, --null=char                   Use <char> to represent a NULL value
  -b, --bin=strip|raw|octal|hex     Binary export mode
  -B, --boolean-words               Use TRUE/FALSE in Boolean fields (default is 0/1)
  --version                         Show mdbtools version and exit
```

### `man`

官方给出的调用示例：`man mdb-header`

```text
root@kali:~# man mdb-header
mdb-header(1)        Executable programs or shell commands        mdb-header(1)
NAME
     mdb-header - Write header file from an MDB database
SYNOPSIS
     mdb-header [database]
DESCRIPTION
     mdb-header is a utility program distributed with MDB Tools.
     It will dump the names and types of the tables and columns in an MDB data-
     base in a C header format.
     It will create three files - types.h and dumptypes.[ch]
ENVIRONMENT
     MDB_JET3_CHARSET
            Defines  the charset of the input JET3 (access 97) file. Default is
            CP1252. See iconv(1).
     MDBICONV
            Defines the output charset. Default is UTF-8.  mdbtools  must  have
            been compiled with iconv.
     MDBOPTS
            Colon-separated list of options:
            *  debug_like
            *  debug_write
            *  debug_usage
            *  debug_ole
            *  debug_row
            *  debug_props
            *  debug_all is a shortcut for all debug_* options
            *  no_memo (deprecated; has no effect)
            *  use_index (experimental; requires libmswstr)
EXIT STATUS
     mdb-header exits with error code 1 if there was anunsupported type.
FUTURE DIRECTIONS
     mdb-header is deprecated. Soon, it will no longer be distributed.
     It  is the feeling of developers that it is not used, as C code generation
     is now usually replaced by more generic approaches, including libmdb calls
     and odbc.
     However,  should  you  find  this  tool  useful,  drop  us   a   line   at
     https://github.com/mdbtools/mdbtools/issues/197  and  we'll consider main-
     taining it.
SEE ALSO
     mdb-array(1) mdb-count(1) mdb-export(1) mdb-hexdump(1) mdb-import(1)  mdb-
     json(1)  mdb-parsecsv(1)  mdb-prop(1)  mdb-queries(1)  mdb-schema(1)  mdb-
     sql(1) mdb-tables(1) mdb-ver(1)
AUTHORS
     The mdb-header utility was written by Brian Bruns.
BUGS
     Only a few types are currently supported.
MDBTools 1.0.1                   29 April 2026                    mdb-header(1)
```

### `man（示例）`

官方给出的调用示例：`man mdb-hexdump`

```text
root@kali:~# man mdb-hexdump
mdb-hexdump(1)       Executable programs or shell commands       mdb-hexdump(1)
NAME
     mdb-hexdump - Hexdump utility from MDB Tools
SYNOPSIS
     mdb-hexdump file [pagenumber]
DESCRIPTION
     mdb-hexdump is a utility program distributed with MDB Tools.
     mdb-hexdump makes a hex dump of a binary file (such as an mdb file).
ENVIRONMENT
     MDB_JET3_CHARSET
            Defines  the charset of the input JET3 (access 97) file. Default is
            CP1252. See iconv(1).
     MDBICONV
            Defines the output charset. Default is UTF-8.  mdbtools  must  have
            been compiled with iconv.
     MDBOPTS
            Colon-separated list of options:
            *  debug_like
            *  debug_write
            *  debug_usage
            *  debug_ole
            *  debug_row
            *  debug_props
            *  debug_all is a shortcut for all debug_* options
            *  no_memo (deprecated; has no effect)
            *  use_index (experimental; requires libmswstr)
SEE ALSO
     mdb-array(1)  mdb-count(1)  mdb-export(1) mdb-header(1) mdb-import(1) mdb-
     json(1)  mdb-parsecsv(1)  mdb-prop(1)  mdb-queries(1)  mdb-schema(1)  mdb-
     sql(1) mdb-tables(1) mdb-ver(1)
AUTHORS
     The mdb-hexdump utility was written by Brian Bruns.
MDBTools 1.0.1                   29 April 2026                   mdb-hexdump(1)
```

### `man（示例）`

官方给出的调用示例：`man mdb-import`

```text
root@kali:~# man mdb-import
mdb-import(1)        Executable programs or shell commands        mdb-import(1)
NAME
     mdb-import - Import CSV data into an MDB database.
SYNOPSIS
     mdb-import [-H lines] [-d char] database table csvfile
     mdb-import -h|--help
     mdb-import --version
DESCRIPTION
     mdb-import is a utility program distributed with MDB Tools.
     It reads a CSV (comma separated value) file and add the data into table of
     database.
OPTIONS
     -H, --header lines
            Skip lines of CSV header.
     -d, --delimiter char
            Specify an alternative column delimiter. Default is , (comma).
     --version
            Print the mdbtools version and exit
NOTES
ENVIRONMENT
     MDB_JET3_CHARSET
            Defines  the  charset  of  the  JET3  (access  97) file. Default is
            CP1252. See iconv(1).
     MDBICONV
            Defines the input charset to use  for  the  SQL  file.  Default  is
            UTF-8. mdbtools must have been compiled with iconv.
     MDBOPTS
            Colon-separated list of options:
            *  debug_like
            *  debug_write
            *  debug_usage
            *  debug_ole
            *  debug_row
            *  debug_props
            *  debug_all is a shortcut for all debug_* options
            *  no_memo (deprecated; has no effect)
            *  use_index (experimental; requires libmswstr)
SEE ALSO
     mdb-array(1)  mdb-count(1) mdb-export(1) mdb-header(1) mdb-hexdump(1) mdb-
     json(1)  mdb-parsecsv(1)  mdb-prop(1)  mdb-queries(1)  mdb-schema(1)  mdb-
     sql(1) mdb-tables(1) mdb-ver(1)
HISTORY
     mdb-import first appeared in MDB Tools 0.7.
AUTHORS
     The mdb-import utility was written by Brian Bruns.
BUGS
     mdb-import  does  not  enforce  any  kind  of checks. You can violate con-
     straints.
MDBTools 1.0.1                   29 April 2026                    mdb-import(1)
```

### `mdb-json`

官方给出的调用示例：`mdb-json -h`

```text
root@kali:~# mdb-json -h
Usage:
  mdb-json [OPTION…] <file> <table> - export data from Access file to JSON
Help Options:
  -h, --help                       Show help options
Application Options:
  -D, --date-format=format         Set the date format (see strftime(3) for details)
  -T, --datetime-format=format     Set the date/time format (see strftime(3) for details)
  -U, --no-unprintable             Change unprintable characters to spaces (otherwise escaped as \u00XX)
  --version                        Show mdbtools version and exit
```

### `man（示例）`

官方给出的调用示例：`man mdb-parsecsv`

```text
root@kali:~# man mdb-parsecsv
mdb-parsecsv(1)      Executable programs or shell commands      mdb-parsecsv(1)
NAME
     mdb-parsecsv - Convert CSV table dump into C file.
SYNOPSIS
     mdb-parsecsv file
DESCRIPTION
     mdb-parsecsv is a utility program distributed with MDB Tools.
     mdb-parsecsv  takes a CSV file representing a database table, and converts
     it into a C array.
NOTES
     If the first argument does not exist as a file, mdb-parsecsv will look for
     the same filename with '.txt' appended.
     The file extension is stripped, and the output written to  the  base  name
     plus a '.c' extension.
ENVIRONMENT
     MDB_JET3_CHARSET
            Defines  the charset of the input JET3 (access 97) file. Default is
            CP1252. See iconv(1).
     MDBICONV
            Defines the output charset to use for  the  SQL  file.  Default  is
            UTF-8. mdbtools must have been compiled with iconv.
     MDBOPTS
            Colon-separated list of options:
            *  debug_like
            *  debug_write
            *  debug_usage
            *  debug_ole
            *  debug_row
            *  debug_props
            *  debug_all is a shortcut for all debug_* options
            *  no_memo (deprecated; has no effect)
            *  use_index (experimental; requires libmswstr)
FUTURE DIRECTIONS
     mdb-parsecsv is deprecated. Soon, it will no longer be distributed.
     It  is the feeling of developers that it is not used, as C code generation
     is now usually replaced by more generic approaches, including libmdb calls
     and odbc.
     However,  should  you  find  this  tool  useful,  drop  us   a   line   at
     https://github.com/mdbtools/mdbtools/issues/197  and  we'll consider main-
     taining it.
SEE ALSO
     mdb-array(1) mdb-count(1) mdb-export(1) mdb-header(1) mdb-hexdump(1)  mdb-
     import(1)  mdb-json(1) mdb-prop(1) mdb-queries(1) mdb-schema(1) mdb-sql(1)
     mdb-tables(1) mdb-ver(1)
AUTHORS
     The mdb-parsecsv utility was written by Brian Bruns.
MDBTools 1.0.1                   29 April 2026                  mdb-parsecsv(1)
```

### `mdb-prop`

官方给出的调用示例：`mdb-prop -h`

```text
root@kali:~# mdb-prop -h
Usage:
  mdb-prop [OPTION…] <file> <object name> [<prop col>] - display properties of an object in an Access database
Help Options:
  -h, --help       Show help options
Application Options:
  --version        Show mdbtools version and exit
```

### `mdb-queries`

官方给出的调用示例：`mdb-queries -h`

```text
root@kali:~# mdb-queries -h
Usage:
  mdb-queries [OPTION…] <file> <query name> - list or export queries from an Access database
Help Options:
  -h, --help                Show help options
Application Options:
  -L, --list                List queries in the database (default if no query name is passed)
  -1, --newline             Use newline as the delimiter (used in conjunction with listing)
  -d, --delimiter=delim     Specify delimiter to use
  --version                 Show mdbtools version and exit
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install mdbtools`，再执行 `libmdb3t64 --version` 2>/dev/null || `libmdb3t64 -V`
- [ ] **2.** **读官方帮助** —— `libmdb3t64 -h`，需要细节时 `man libmdb3t64`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: mdb-array <file> <table>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/mdbtools/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/mdbtools/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/mdbtools/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
