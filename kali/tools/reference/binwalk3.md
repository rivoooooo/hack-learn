# binwalk3

> Tool library for analyzing binary blobs and executable code Binwalk is a tool for identifying, and optionally extracting, files and data that have been embedded inside of other files. While its primary focus is firmware analysis, it suppor…

> **功能分类**：数字取证 ｜ **Kali 包**：`binwalk3` ｜ **官方文档**：<https://www.kali.org/tools/binwalk3/>

## 1. 安装

```bash
sudo apt update
sudo apt install binwalk3
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.1.0 |
| 架构 | arm64 |
| 可执行命令 | `binwalk3`、`librust-binwalk-dev` |
| 依赖 | `libc6`、`libfontconfig1`、`libfreetype6`、`libgcc-s1`、`liblzma5`、`sasquatch` |
| 安装体积 | 3.88 MB |
| 官网 | <https://github.com/ReFirmLabs/binwalk> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/binwalk3> |
| 包追踪 | <https://pkg.kali.org/pkg/binwalk3> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
binwalk3 -h          # 查看用法
man binwalk3         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `binwalk3`

官方给出的调用示例：`binwalk3 -h`

```text
root@kali:~# binwalk3 -h
Analyzes data for embedded file types
Usage: binwalk3 [OPTIONS] [FILE_NAME]
Arguments:
  [FILE_NAME]  Path to the file to analyze
Options:
  -L, --list                   List supported signatures and extractors
  -q, --quiet                  Supress output to stdout
  -v, --verbose                During recursive extraction display *all* results
  -e, --extract                Automatically extract known file types
  -M, --matryoshka             Recursively scan extracted files
  -a, --search-all             Search for all signatures at all offsets
  -E, --entropy                Plot the entropy of the specified file
  -l, --log <LOG>              Log JSON results to a file
  -t, --threads <THREADS>      Manually specify the number of threads to use
  -x, --exclude <EXCLUDE>...   Do no scan for these signatures
  -y, --include <INCLUDE>...   Only scan for these signatures
  -C, --directory <DIRECTORY>  Extract files/folders to a custom directory [default: extractions]
  -h, --help                   Print help
  -V, --version                Print version
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install binwalk3`，再执行 `binwalk3 --version` 2>/dev/null || `binwalk3 -V`
- [ ] **2.** **读官方帮助** —— `binwalk3 -h`，需要细节时 `man binwalk3`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: binwalk3 [OPTIONS] [FILE_NAME]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/binwalk3/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[binwalk](../../tools/tutorials/09-数字取证/binwalk.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/binwalk3/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/binwalk3/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
