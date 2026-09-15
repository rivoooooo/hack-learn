# oletools

> Analyze MS OLE2 files and MS Office documents Tools to analyze Microsoft OLE2 files (also called Structured Storage, Compound File Binary Format or Compound Document File Format), such as Microsoft Office 97-2003 documents, MSI files or Ou…

> **功能分类**：通用工具 ｜ **Kali 包**：`oletools` ｜ **官方文档**：<https://www.kali.org/tools/oletools/>

## 1. 安装

```bash
sudo apt update
sudo apt install oletools
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.60.2 |
| 架构 | all |
| 可执行命令 | `oletools`、`ezhexviewer`、`ftguess`、`mraptor`、`msodde`、`olebrowse`、`oledir`、`olefile`、`oleid`、`olemap`、`olemeta`、`oleobj`、`oletimes`、`olevba`、`pyxswf`、`rtfobj` |
| 依赖 | `python3`、`python3-colorclass`、`python3-easygui`、`python3-msoffcrypto-tool`、`python3-olefile`、`python3-pcodedmp`、`python3-pyparsing`、`ezhexviewer`、`ftguess` |
| 安装体积 | 1.90 MB |
| 官网 | <https://github.com/decalage2/oletools> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/oletools> |
| 包追踪 | <https://pkg.kali.org/pkg/oletools> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
oletools -h          # 查看用法
man oletools         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 16 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ftguess`

> 官方示例调用：`ftguess -h`

```text
root@kali:~# ftguess -h
ftguess 0.60.2 on Python 3.14.6 - http://decalage.info/python/oletools
THIS IS WORK IN PROGRESS - Check updates regularly!
Please report any issue at https://github.com/decalage2/oletools/issues
Usage: ftguess [options] <filename> [filename2 ...]
Options:
  -h, --help            show this help message and exit
  -r                    find files recursively in subdirectories.
  -z ZIP_PASSWORD, --zip=ZIP_PASSWORD
                        if the file is a zip archive, open first file from it,
                        using the provided password
  -f ZIP_FNAME, --zipfname=ZIP_FNAME
                        if the file is a zip archive, file(s) to be opened
                        within the zip. Wildcards * and ? are supported.
                        (default:*)
  -l LOGLEVEL, --loglevel=LOGLEVEL
                        logging level debug/info/warning/error/critical
                        (default=warning)
```

### `mraptor`

> 官方示例调用：`mraptor -h`

```text
root@kali:~# mraptor -h
Usage: mraptor [options] <filename> [filename2 ...]
Options:
  -h, --help            show this help message and exit
  -r                    find files recursively in subdirectories.
  -z ZIP_PASSWORD, --zip=ZIP_PASSWORD
                        if the file is a zip archive, open all files from it,
                        using the provided password (requires Python 2.6+)
  -f ZIP_FNAME, --zipfname=ZIP_FNAME
                        if the file is a zip archive, file(s) to be opened
                        within the zip. Wildcards * and ? are supported.
                        (default:*)
  -l LOGLEVEL, --loglevel=LOGLEVEL
                        logging level debug/info/warning/error/critical
                        (default=warning)
  -m, --matches         Show matched strings.
```

### `msodde`

> 官方示例调用：`msodde -h`

```text
root@kali:~# msodde -h
usage: msodde [-h] [-j] [--nounquote] [-l LOGLEVEL] [-p PASSWORD] [-d] [-f]
              [-a]
              FILE
A python tool to detect and extract DDE links in MS Office files
positional arguments:
  FILE                  path of the file to be analyzed
options:
  -h, --help            show this help message and exit
  -j, --json            Output in json format. Do not use with -ldebug
  --nounquote           don't unquote values
  -l, --loglevel LOGLEVEL
                        logging level debug/info/warning/error/critical
                        (default=warning)
  -p, --password PASSWORD
                        if encrypted office files are encountered, try
                        decryption with this password. May be repeated.
Filter which OpenXML field commands are returned:
  Only applies to OpenXML (e.g. docx) and rtf, not to OLE (e.g. .doc). These
  options are mutually exclusive, last option found on command line
  overwrites earlier ones.
  -d, --dde-only        Return only DDE and DDEAUTO fields
  -f, --filter          Return all fields except harmless ones
  -a, --all-fields      Return all fields, irrespective of their contents
```

### `oledir`

> 官方示例调用：`oledir -h`

```text
root@kali:~# oledir -h
Usage: oledir [options] <filename> [filename2 ...]
Options:
  -h, --help            show this help message and exit
  -r                    find files recursively in subdirectories.
  -z ZIP_PASSWORD, --zip=ZIP_PASSWORD
                        if the file is a zip archive, open all files from it,
                        using the provided password (requires Python 2.6+)
  -f ZIP_FNAME, --zipfname=ZIP_FNAME
                        if the file is a zip archive, file(s) to be opened
                        within the zip. Wildcards * and ? are supported.
                        (default:*)
```

### `olefile`

> 官方示例调用：`olefile -h`

```text
root@kali:~# olefile -h
Usage: olefile [options] <filename> [filename2 ...]
Options:
  -h, --help            show this help message and exit
  -c                    check all streams (for debugging purposes)
  -p                    extract all user-defined propertires
  -d                    debug mode, shortcut for -l debug (displays a lot of
                        debug information, for developers only)
  -l LOGLEVEL, --loglevel=LOGLEVEL
                        logging level debug/info/warning/error/critical
                        (default=warning)
```

### `oleid`

> 官方示例调用：`oleid -h`

```text
root@kali:~# oleid -h
oleid 0.60.1 - http://decalage.info/oletools
THIS IS WORK IN PROGRESS - Check updates regularly!
Please report any issue at https://github.com/decalage2/oletools/issues
usage: oleid [-h] [FILE ...]
oleid.py oleid is a script to analyze OLE files such as MS Office documents
(e.g. Word, Excel), to detect specific characteristics that could potentially
indicate that the file is suspicious or malicious, in terms of security (e.g.
malware). For example it can detect VBA macros, embedded Flash objects,
fragmentation. The results is displayed as ascii table (but could be returned
or printed in other formats like CSV, XML or JSON in future). oleid project
website: http://www.decalage.info/python/oleid oleid is part of the python-
oletools package: http://www.decalage.info/python/oletools
positional arguments:
  FILE        Name of files to process
options:
  -h, --help  show this help message and exit
```

### `olemap`

> 官方示例调用：`olemap -h`

```text
root@kali:~# olemap -h
Usage: olemap [options] <filename> [filename2 ...]
Options:
  -h, --help            show this help message and exit
  -r                    find files recursively in subdirectories.
  -z ZIP_PASSWORD, --zip=ZIP_PASSWORD
                        if the file is a zip archive, open all files from it,
                        using the provided password (requires Python 2.6+)
  -f ZIP_FNAME, --zipfname=ZIP_FNAME
                        if the file is a zip archive, file(s) to be opened
                        within the zip. Wildcards * and ? are supported.
                        (default:*)
  --header              Display the OLE header (default: yes)
  --fat                 Display the FAT (default: no)
  --minifat             Display the MiniFAT (default: no)
  -x, --exdata          Display a hex dump of extra data at end of file
```

### `olemeta`

> 官方示例调用：`olemeta -h`

```text
root@kali:~# olemeta -h
olemeta 0.54 - http://decalage.info/python/oletools
THIS IS WORK IN PROGRESS - Check updates regularly!
Please report any issue at https://github.com/decalage2/oletools/issues
Usage: olemeta [options] <filename> [filename2 ...]
Options:
  -h, --help            show this help message and exit
  -r                    find files recursively in subdirectories.
  -z ZIP_PASSWORD, --zip=ZIP_PASSWORD
                        if the file is a zip archive, open all files from it,
                        using the provided password (requires Python 2.6+)
  -f ZIP_FNAME, --zipfname=ZIP_FNAME
                        if the file is a zip archive, file(s) to be opened
                        within the zip. Wildcards * and ? are supported.
                        (default:*)
```

### `oleobj`

> 官方示例调用：`oleobj -h`

```text
root@kali:~# oleobj -h
oleobj 0.60.1 - http://decalage.info/oletools
THIS IS WORK IN PROGRESS - Check updates regularly!
Please report any issue at https://github.com/decalage2/oletools/issues
usage: usage: oleobj [options] <filename> [filename2 ...]
positional arguments:
  FILE                  Office files to parse (same as -i)
options:
  -h, --help            show this help message and exit
  -r                    find files recursively in subdirectories.
  -d OUTPUT_DIR         use specified directory to output files.
  -z, --zip ZIP_PASSWORD
                        if the file is a zip archive, open first file from it,
                        using the provided password (requires Python 2.6+)
  -f, --zipfname ZIP_FNAME
                        if the file is a zip archive, file(s) to be opened
                        within the zip. Wildcards * and ? are supported.
                        (default:*)
  -l, --loglevel LOGLEVEL
                        logging level debug/info/warning/error/critical
                        (default=warning)
  -i, --more-input FILE
                        Additional file to parse (same as positional
                        arguments)
  -v, --verbose         verbose mode, set logging to DEBUG (overwrites -l)
```

### `oletimes`

> 官方示例调用：`oletimes -h`

```text
root@kali:~# oletimes -h
oletimes 0.54 - http://decalage.info/python/oletools
THIS IS WORK IN PROGRESS - Check updates regularly!
Please report any issue at https://github.com/decalage2/oletools/issues
Usage: oletimes [options] <filename> [filename2 ...]
Options:
  -h, --help            show this help message and exit
  -r                    find files recursively in subdirectories.
  -z ZIP_PASSWORD, --zip=ZIP_PASSWORD
                        if the file is a zip archive, open all files from it,
                        using the provided password (requires Python 2.6+)
  -f ZIP_FNAME, --zipfname=ZIP_FNAME
                        if the file is a zip archive, file(s) to be opened
                        within the zip. Wildcards * and ? are supported.
                        (default:*)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install oletools`，再执行 `oletools --version` 2>/dev/null || `oletools -V`
- [ ] **2.** **读官方帮助** —— `oletools -h`，需要细节时 `man oletools`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ftguess [options] <filename> [filename2 ...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/oletools/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/oletools/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/oletools/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
