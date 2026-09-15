# python-defaults

> Package depending on all supported Python2 debugging packages The package currently depends on libpython2.7-dbg, in the future, dependencies on jython (Python2 for a JVM) and ironpython (Python2 for Mono) may be added. This package is a de…

> **功能分类**：通用工具 ｜ **Kali 包**：`python-defaults` ｜ **官方文档**：<https://www.kali.org/tools/python-defaults/>

## 1. 安装

```bash
sudo apt update
sudo apt install libpython-all-dbg
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.7.18 |
| 架构 | any |
| 可执行命令 | `libpython-all-dbg`、`libpython-all-dev`、`libpython2-dbg`、`x86_64-linux-gnu-python2-dbg-config`、`libpython2-dev`、`x86_64-linux-gnu-python2-config`、`libpython2-stdlib`、`python-all`、`python-all-dbg`、`python-all-dev`、`python2`、`pdb2`、`pydoc2`、`pygettext2`、`python2-dbg`、`python2-dbg-config`、`python2-dev`、`python2-config`、`python2-doc`、`python2-minimal`、`pyclean`、`pycompile`、`pyversions` |
| 依赖 | `libpython2-dbg`、`libpython2.7-dbg`、`libpython-all-dev` |
| 安装体积 | 7 KB |
| 官网 | <https://www.python.org/> |
| 源码仓库 | <https://salsa.debian.org/cpython-team/python-defaults> |
| 包追踪 | <https://pkg.kali.org/pkg/python-defaults> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libpython-all-dbg -h          # 查看用法
man libpython-all-dbg         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 23 个可执行命令，下面是官方页面内嵌的帮助原文。

### `x86_64-linux-gnu-python2-dbg-config`

> 官方示例调用：`x86_64-linux-gnu-python2-dbg-config --help`

```text
root@kali:~# x86_64-linux-gnu-python2-dbg-config --help
Usage: /usr/bin/x86_64-linux-gnu-python2-dbg-config --prefix|--exec-prefix|--includes|--libs|--cflags|--ldflags|--extension-suffix|--help|--configdir
```

### `x86_64-linux-gnu-python2-config`

> 官方示例调用：`x86_64-linux-gnu-python2-config --help`

```text
root@kali:~# x86_64-linux-gnu-python2-config --help
Usage: /usr/bin/x86_64-linux-gnu-python2-config --prefix|--exec-prefix|--includes|--libs|--cflags|--ldflags|--extension-suffix|--help|--configdir
```

### `pdb2`

> 官方示例调用：`pdb2 -h`

```text
root@kali:~# pdb2 -h
usage: pdb.py scriptfile [arg] ...
```

### `pydoc2`

> 官方示例调用：`pydoc2 -h`

```text
root@kali:~# pydoc2 -h
pydoc - the Python documentation tool
pydoc2 <name> ...
    Show text documentation on something.  <name> may be the name of a
    Python keyword, topic, function, module, or package, or a dotted
    reference to a class or function within a module or module in a
    package.  If <name> contains a '/', it is used as the path to a
    Python source file to document. If name is 'keywords', 'topics',
    or 'modules', a listing of these things is displayed.
pydoc2 -k <keyword>
    Search for a keyword in the synopsis lines of all available modules.
pydoc2 -p <port>
    Start an HTTP server on the given port on the local machine.  Port
    number 0 can be used to get an arbitrary unused port.
pydoc2 -g
    Pop up a graphical interface for finding and serving documentation.
pydoc2 -w <name> ...
    Write out the HTML documentation for a module to a file in the current
    directory.  If <name> contains a '/', it is treated as a filename; if
    it names a directory, documentation is written for all the contents.
```

### `pygettext2`

> 官方示例调用：`pygettext2 -h`

```text
root@kali:~# pygettext2 -h
pygettext -- Python equivalent of xgettext(1)
Many systems (Solaris, Linux, Gnu) provide extensive tools that ease the
internationalization of C programs. Most of these tools are independent of
the programming language and can be used from within Python programs.
Martin von Loewis' work[1] helps considerably in this regard.
There's one problem though; xgettext is the program that scans source code
looking for message strings, but it groks only C (or C++). Python
introduces a few wrinkles, such as dual quoting characters, triple quoted
strings, and raw strings. xgettext understands none of this.
Enter pygettext, which uses Python's standard tokenize module to scan
Python source code, generating .pot files identical to what GNU xgettext[2]
generates for C and C++ code. From there, the standard GNU tools can be
used.
A word about marking Python strings as candidates for translation. GNU
xgettext recognizes the following keywords: gettext, dgettext, dcgettext,
and gettext_noop. But those can be a lot of text to include all over your
code. C and C++ have a trick: they use the C preprocessor. Most
internationalized C source includes a #define for gettext() to _() so that
what has to be written in the source is much less. Thus these are both
translatable strings:
    gettext("Translatable String")
    _("Translatable String")
Python of course has no preprocessor so this doesn't work so well.  Thus,
pygettext searches only for _() by default, but see the -k/--keyword flag
below for how to augment this.
 [1] http://www.python.org/workshops/1997-10/proceedings/loewis.html
 [2] http://www.gnu.org/software/gettext/gettext.html
NOTE: pygettext attempts to be option and feature compatible with GNU
xgettext where ever possible. However some options are still missing or are
not fully implemented. Also, xgettext's use of command line switches with
option arguments is broken, and in these cases, pygettext just defines
additional switches.
Usage: pygettext [options] inputfile ...
Options:
    -a
    --extract-all
        Extract all strings.
    -d name
    --default-domain=name
        Rename the default output file from messages.pot to name.pot.
    -E
    --escape
        Replace non-ASCII characters with octal escape sequences.
    -D
    --docstrings
        Extract module, class, method, and function docstrings.  These do
        not need to be wrapped in _() markers, and in fact cannot be for
        Python to consider them docstrings. (See also the -X option).
    -h
    --help
        Print this help message and exit.
    -k word
    --keyword=word
        Keywords to look for in addition to the default set, which are:
        _
        You can have multiple -k flags on the command line.
    -K
    --no-default-keywords
        Disable the default set of keywords (see above).  Any keywords
        explicitly added with the -k/--keyword option are still recognized.
    --no-location
        Do not write filename/lineno location comments.
    -n
    --add-location
        Write filename/lineno location comments indicating where each
        extracted string is found in the source.  These lines appear before
        each msgid.  The style of comments is controlled by the -S/--style
        option.  This is the default.
    -o filename
    --output=filename
        Rename the default output file from messages.pot to filename.  If
        filename is `-' then the output is sent to standard out.
    -p dir
    --output-dir=dir
        Output files will be placed in directory dir.
    -S stylename
    --style stylename
        Specify which style to use for location comments.  Two styles are
        supported:
        Solaris  # File: filename, line: line-number
        GNU      #: filename:line
        The style name is case insensitive.  GNU style is the default.
    -v
    --verbose
        Print the names of the files being processed.
    -V
    --version
        Print the version of pygettext and exit.
    -w columns
    --width=columns
        Set width of output to columns.
    -x filename
    --exclude-file=filename
        Specify a file that contains a list of strings that are not be
        extracted from the input files.  Each string to be excluded must
        appear on a line by itself in the file.
    -X filename
    --no-docstrings=filename
        Specify a file that contains a list of files (one per line) that
        should not have their docstrings extracted.  This is only useful in
        conjunction with the -D option above.
If `inputfile' is -, standard input is read.
```

### `python2-dbg`

> 官方示例调用：`python2-dbg -h`

```text
root@kali:~# python2-dbg -h
usage: python2-dbg [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-b     : issue warnings about comparing bytearray with unicode
         (-bb: issue errors)
-B     : don't write .py[co] files on import; also PYTHONDONTWRITEBYTECODE=x
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser; also PYTHONDEBUG=x
-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
-h     : print this help message and exit (also --help)
-i     : inspect interactively after running script; forces a prompt even
         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
-m mod : run library module as a script (terminates option list)
-O     : optimize generated bytecode slightly; also PYTHONOPTIMIZE=x
-OO    : remove doc-strings in addition to the -O optimizations
-R     : use a pseudo-random salt to make hash() values of various types be
         unpredictable between separate invocations of the interpreter, as
         a defense against denial-of-service attacks
-Q arg : division options: -Qold (default), -Qwarn, -Qwarnall, -Qnew
-s     : don't add user site directory to sys.path; also PYTHONNOUSERSITE
-S     : don't imply 'import site' on initialization
-t     : issue warnings about inconsistent tab usage (-tt: issue errors)
-u     : unbuffered binary stdout and stderr; also PYTHONUNBUFFERED=x
         see man page for details on internal buffering relating to '-u'
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
-W arg : warning control; arg is action:message:category:module:lineno
         also PYTHONWARNINGS=arg
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
-3     : warn about Python 3.x incompatibilities that 2to3 cannot trivially fix
file   : program read from script file
-      : program read from stdin (default; interactive mode if a tty)
arg ...: arguments passed to program in sys.argv[1:]
Other environment variables:
PYTHONSTARTUP: file executed on interactive startup (no default)
PYTHONPATH   : ':'-separated list of directories prefixed to the
               default module search path.  The result is sys.path.
PYTHONHOME   : alternate <prefix> directory (or <prefix>:<exec_prefix>).
               The default module search path uses <prefix>/pythonX.X.
PYTHONCASEOK : ignore case in 'import' statements (Windows).
PYTHONIOENCODING: Encoding[:errors] used for stdin/stdout/stderr.
PYTHONHASHSEED: if this variable is set to 'random', the effect is the same
   as specifying the -R option: a random value is used to seed the hashes of
   str, bytes and datetime objects.  It can also be set to an integer
   in the range [0,4294967295] to get hash values with a predictable seed.
```

### `python2-dbg-config`

> 官方示例调用：`python2-dbg-config --help`

```text
root@kali:~# python2-dbg-config --help
Usage: /usr/bin/python2-dbg-config --prefix|--exec-prefix|--includes|--libs|--cflags|--ldflags|--extension-suffix|--help|--configdir
```

### `python2-config`

> 官方示例调用：`python2-config --help`

```text
root@kali:~# python2-config --help
Usage: /usr/bin/python2-config --prefix|--exec-prefix|--includes|--libs|--cflags|--ldflags|--extension-suffix|--help|--configdir
```

### `pyclean`

> 官方示例调用：`pyclean -h`

```text
root@kali:~# pyclean -h
Usage: pyclean [-p PACKAGE] [DIR_OR_FILE]
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -v, --verbose         turn verbose more one
  -q, --quiet           be quiet
  -p PACKAGE, --package=PACKAGE
                        specify Debian package name to clean
```

### `pycompile`

> 官方示例调用：`pycompile -h`

```text
root@kali:~# pycompile -h
Usage: pycompile [-V [X.Y][-][A.B]] DIR_OR_FILE [-X REGEXPR]
       pycompile -p PACKAGE
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -v, --verbose         turn verbose mode on
  -q, --quiet           be quiet
  -f, --force           force rebuild even if timestamps are up-to-date
  -O                    byte-compile to .pyo files
  -p PACKAGE, --package=PACKAGE
                        specify Debian package name whose files should be
                        bytecompiled
  -V VRANGE             force private modules to be bytecompiled with Python
                        version from given range, regardless of the default
                        Python version in the system. If there are no other
                        options, bytecompile all public modules for installed
                        Python versions that match given range.  VERSION_RANGE
                        examples: '2.5' (version 2.5 only), '2.5-' (version
                        2.5 or newer), '2.5-2.7' (version 2.5 or 2.6), '-3.0'
                        (all supported 2.X versions)
  -X REGEXPR, --exclude=REGEXPR
                        exclude items that match given REGEXPR. You may use
                        this option multiple times to build up a list of
                        things to exclude.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install libpython-all-dbg`，再执行 `libpython-all-dbg --version` 2>/dev/null || `libpython-all-dbg -V`
- [ ] **2.** **读官方帮助** —— `libpython-all-dbg -h`，需要细节时 `man libpython-all-dbg`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: /usr/bin/x86_64-linux-gnu-python2-dbg-config --prefix|--exec-prefix|--includes|--libs|--cflags|--ldflags|--extension-suffix|--help|--configdir`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/python-defaults/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/python-defaults/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/python-defaults/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
