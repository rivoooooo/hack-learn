# detect-it-easy

> Program for determining types of files Detect It Easy (DiE) is a powerful tool for file type identification, popular among malware analysts, cybersecurity experts, and reverse engineers worldwide. Supporting both signature-based and heuris…

> **功能分类**：通用工具 ｜ **Kali 包**：`detect-it-easy` ｜ **官方文档**：<https://www.kali.org/tools/detect-it-easy/>

## 1. 安装

```bash
sudo apt update
sudo apt install detect-it-easy
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.21 |
| 架构 | any |
| 可执行命令 | `detect-it-easy`、`die`、`diec`、`diel` |
| 依赖 | `libc6`、`libgcc-s1`、`libqt5concurrent5t64`、`libqt5core5t64` |
| 安装体积 | 41.40 MB |
| 官网 | <https://github.com/horsicq/Detect-It-Easy> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/detectiteasy> |
| 包追踪 | <https://pkg.kali.org/pkg/detect-it-easy> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
detect-it-easy -h          # 查看用法
man detect-it-easy         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `diec`

官方给出的调用示例：`diec -h`

```text
root@kali:~# diec -h
Usage: diec [options] target
Detect It Easy v3.21
Copyright(C) 2006-2008 Hellsp@wn 2012-2026 hors<
[email protected]
> Web: http://ntinfo.biz
Options:
  -h, --help                   Displays help on commandline options.
  --help-all                   Displays help including Qt specific options.
  -v, --version                Displays version information.
  -r, --recursivescan          Scan directories recursively
  -d, --deepscan               Enable deep scanning for thorough analysis
  -u, --heuristicscan          Enable heuristic scanning methods
  -b, --verbose                Show verbose output with detailed information
  -g, --aggressivecscan        Enable aggressive scanning mode
  -a, --alltypes               Scan all file types
  -f, --format                 Format the output result
  -l, --profiling              Profile signatures during scan
  -M, --messages               Display scan messages and warnings
  -U, --hideunknown            Hide unknown file types from results
  -e, --entropy                Display file entropy information
  -i, --info                   Display file information
  -S, --struct <struct>        Show special file information using specified
                               structure (e.g., 'Hash' or 'Hash#MD5')
  -x, --xml                    Output results in XML format
  -j, --json                   Output results in JSON format
  -c, --csv                    Output results in CSV format
  -t, --tsv                    Output results in TSV format
  -p, --plaintext              Output results as plain text
  -D, --database <path>        Set database path
  -E, --extradatabase <path>   Set extra database path
  -C, --customdatabase <path>  Set custom database path
  -s, --showdatabase           Show database information
  -w, --showstructs            Display all available special structures for the
                               file
  --test <directory>           Test signatures in specified directory
  --addtest <filename>         Add test case with filename, detect string, and
                               directory
Arguments:
  target                       The file or directory to open.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install detect-it-easy`，再执行 `detect-it-easy --version` 2>/dev/null || `detect-it-easy -V`
- [ ] **2.** **读官方帮助** —— `detect-it-easy -h`，需要细节时 `man detect-it-easy`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: diec [options] target`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/detect-it-easy/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/detect-it-easy/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/detect-it-easy/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
