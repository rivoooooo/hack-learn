# readpe

> Command-line tools to manipulate Windows PE files readpe is a toolkit designed to analyze Microsoft Windows PE (Portable Executable) binary files. Its tools can parse and compare PE32/PE32+ executable files (EXE, DLL, OCX, etc), and analyz…

> **功能分类**：数字取证 ｜ **Kali 包**：`readpe` ｜ **官方文档**：<https://www.kali.org/tools/readpe/>

## 1. 安装

```bash
sudo apt update
sudo apt install readpe
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.85.1 |
| 架构 | any |
| 可执行命令 | `libpe-dev`、`libpe1t64`、`readpe`、`ofs2rva`、`pedis`、`pehash`、`peldd`、`pepack`、`peres`、`pescan`、`pesec`、`pestr`、`rva2ofs` |
| 依赖 | `libc6`、`libpe1t64`、`libssl3t64`、`ofs2rva` |
| 安装体积 | 1.23 MB |
| 官网 | <https://github.com/mentebinaria/readpe/wiki> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/readpe> |
| 包追踪 | <https://pkg.kali.org/pkg/readpe> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libpe-dev -h          # 查看用法
man libpe-dev         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 13 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ofs2rva`

官方给出的调用示例：`ofs2rva -h`

```text
root@kali:~# ofs2rva -h
Usage: ofs2rva <offset> FILE
Convert raw file offset to RVA
Example: ofs2rva 0x1b9b8 calc.exe
Options:
 -V, --version                          Show version.
 --help                                 Show this help.
```

### `pedis`

官方给出的调用示例：`pedis --help`

```text
root@kali:~# pedis --help
Usage: pedis OPTIONS FILE
Disassemble PE sections and functions (by default, until found a RET or LEAVE instruction)
Example: pedis -r 0x4c4df putty.exe
Options:
 --att                                 Set AT&T assembly syntax (default: Intel).
 -e, --entrypoint                      Disassemble the entire entrypoint function.
 -f, --format <html|text|json|xml|csv> Change output format (default: text).
 -m, --mode <16|32|64>                 Disassembly mode (default: auto).
 -i <number>                           Number of instructions to disassemble.
 -n <number>                           Number of bytes to disassemble
 -o, --offset <offset>                 Disassemble at specified offset, either in decimal or hexadecimal format (prefixed with 0x).
 -r, --rva <rva>                       Disassemble at specified RVA, either in decimal or hexadecimal format (prefixed with 0x).
 -s, --section <section_name>          Disassemble en entire section given.
 -V, --version                         Show version.
 --help                                Show this help.
```

### `pehash`

官方给出的调用示例：`pehash --help`

```text
root@kali:~# pehash --help
Usage: pehash OPTIONS FILE
Calculate hashes of PE pieces
Example: pehash -s '.text' winzip.exe
Options:
 -f, --format <html|text|json|xml|csv> Change output format (default: text).
 -a, --all                             Hash file, sections and headers with md5, sha1, sha256, ssdeep and imphash.
 -c, --content                         Hash only the file content (default).
 -h, --header <dos|coff|optional>      Hash only the header with the specified name.
 -s, --section <section_name>          Hash only the section with the specified name.
 --section-index <section_index>       Hash only the section at the specified index (1..n).
 -V, --version                         Show version.
 --help                                Show this help.
```

### `peldd`

官方给出的调用示例：`peldd --help`

```text
root@kali:~# peldd --help
Usage: peldd FILE
Display PE library dependencies
Example: peldd winzip.exe
Options:
 -f, --format <html|text|json|xml|csv> Change output format (default: text).
 -V, --version                         Show version.
 --help                                Show help.
```

### `pepack`

官方给出的调用示例：`pepack --help`

```text
root@kali:~# pepack --help
Usage: pepack FILE
Search for packers in PE files
Example: pepack putty.exe
Options:
 -d, --database <file>                  Use database file (default: ./userdb.txt).
 -f, --format <html|text|json|xml|csv>  Change output format (default: text).
 -V, --version                          Show version.
 --help                                 Show this help.
```

### `peres`

官方给出的调用示例：`peres -h`

```text
root@kali:~# peres -h
Usage: peres OPTIONS FILE
Show information about resource section and extract it
Example: peres -a putty.exe
Options:
 -a, --all                             Show all information, statistics and extract resources
 -f, --format <html|text|json|xml|csv> Change output format (default: text)
 -i, --info                            Show resources information
 -l, --list                            Show list view
 -s, --statistics                      Show resources statistics
 -x, --extract                         Extract resources
 -X, --named-extract                   Extract resources with path names
 -v, --file-version                    Show File Version from PE resource directory
 -V, --version                         Show version and exit
 --help                                Show this help and exit
```

### `pescan`

官方给出的调用示例：`pescan --help`

```text
root@kali:~# pescan --help
Usage: pescan OPTIONS FILE
Search for suspicious things in PE files
Example: pescan putty.exe
Options:
 -f, --format <html|text|json|xml|csv> Change output format (default: text).
 -v, --verbose                         Show more information about found items.
 -V, --version                         Show version.
 --help                                Show this help.
```

### `pesec`

官方给出的调用示例：`pesec --help`

```text
root@kali:~# pesec --help
Usage: pesec [OPTIONS] FILE
Check for security features in PE files
Example: pesec wordpad.exe
Options:
 -f, --format <html|text|json|xml|csv> Change output format (default: text)
 -c, --certoutform <text|pem>          Specifies the certificate output format (default: text).
 -o, --certout <filename>              Specifies the output filename to write certificates to (default: stdout).
 -V, --version                         Show version.
 --help                                Show this help.
```

### `pestr`

官方给出的调用示例：`pestr --help`

```text
root@kali:~# pestr --help
Usage: pestr OPTIONS FILE
Search for strings in PE files
Example: pestr acrobat.exe
Options:
 -n, --min-length                       Set minimum string length (default: 4).
 -o, --offset                           Show string offset in file.
 -s, --section                          Show string section, if exists.
 -V, --version                          Show version.
 --help                                 Show this help.
```

### `readpe`

官方给出的调用示例：`readpe --help`

```text
root@kali:~# readpe --help
Usage: readpe OPTIONS FILE
Show PE file headers
Example: readpe --header optional winzip.exe
Options:
 -A, --all                             Full output (default).
 -H, --all-headers                     Show all PE headers.
 -S, --all-sections                    Show PE section headers.
 -f, --format <html|text|json|xml|csv> Change output format (default: text).
 -d, --dirs                            Show data directories.
 -h, --header <dos|coff|optional>      Show specific header. It can be used multiple times.
 -i, --imports                         Show imported functions.
 -e, --exports                         Show exported functions.
 -V, --version                         Show version.
 --help                                Show this help.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install readpe`，再执行 `libpe-dev --version` 2>/dev/null || `libpe-dev -V`
- [ ] **2.** **读官方帮助** —— `libpe-dev -h`，需要细节时 `man libpe-dev`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ofs2rva <offset> FILE`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/readpe/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/readpe/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/readpe/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
