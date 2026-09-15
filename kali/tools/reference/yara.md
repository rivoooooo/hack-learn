# yara

> Pattern matching swiss knife for malware researchers YARA is a tool aimed at helping malware researchers to identify and classify malware samples. With YARA, it is possible to create descriptions of malware families based on textual or bin…

> **功能分类**：数字取证 ｜ **Kali 包**：`yara` ｜ **官方文档**：<https://www.kali.org/tools/yara/>

## 1. 安装

```bash
sudo apt update
sudo apt install yara
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.5.8 |
| 架构 | any |
| 可执行命令 | `libyara-dev`、`libyara10`、`yara`、`yarac`、`yara-doc` |
| 依赖 | `libc6`、`libjansson4`、`libmagic1t64`、`libssl3t64`、`libyara10` |
| 安装体积 | 637 KB |
| 官网 | <https://virustotal.github.io/yara/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/yara> |
| 包追踪 | <https://pkg.kali.org/pkg/yara> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libyara-dev -h          # 查看用法
man libyara-dev         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 5 个可执行命令，下面是官方页面内嵌的帮助原文。

### `yara`

> 官方示例调用：`yara -h`

```text
root@kali:~# yara -h
YARA 4.5.8, the pattern matching swiss army knife.
Usage: yara [OPTION]... [NAMESPACE:]RULES_FILE... FILE | DIR | PID
Mandatory arguments to long options are mandatory for short options too.
       --atom-quality-table=FILE           path to a file with the atom quality table
  -C,  --compiled-rules                    load compiled rules
  -c,  --count                             print only number of matches
  -E,  --strict-escape                     warn on unknown escape sequences
  -d,  --define=VAR=VALUE                  define external variable
  -q,  --disable-console-logs              disable printing console log messages
       --fail-on-warnings                  fail on warnings
  -f,  --fast-scan                         fast matching mode
  -h,  --help                              show this help and exit
  -i,  --identifier=IDENTIFIER             print only rules named IDENTIFIER
       --max-process-memory-chunk=NUMBER   set maximum chunk size while reading process memory (default=1073741824)
  -l,  --max-rules=NUMBER                  abort scanning after matching a NUMBER of rules
       --max-strings-per-rule=NUMBER       set maximum number of strings per rule (default=10000)
  -x,  --module-data=MODULE=FILE           pass FILE's content as extra data to MODULE
  -n,  --negate                            print only not satisfied rules (negate)
  -N,  --no-follow-symlinks                do not follow symlinks when scanning
  -w,  --no-warnings                       disable warnings
  -m,  --print-meta                        print metadata
  -D,  --print-module-data                 print module data
  -M,  --module-names                      show module names
  -e,  --print-namespace                   print rules' namespace
  -S,  --print-stats                       print rules' statistics
  -s,  --print-strings                     print matching strings
  -L,  --print-string-length               print length of matched strings
  -X,  --print-xor-key                     print xor key and plaintext of matched strings
  -g,  --print-tags                        print tags
  -r,  --recursive                         recursively search directories
       --scan-list                         scan files listed in FILE, one per line
  -z,  --skip-larger=NUMBER                skip files larger than the given size when scanning a directory
  -k,  --stack-size=SLOTS                  set maximum stack size (default=16384)
  -t,  --tag=TAG                           print only rules tagged as TAG
  -p,  --threads=NUMBER                    use the specified NUMBER of threads to scan a directory
  -a,  --timeout=SECONDS                   abort scanning after the given number of SECONDS
  -v,  --version                           show version information
Send bug reports and suggestions to:
[email protected]
.
```

### `yarac`

> 官方示例调用：`yarac -h`

```text
root@kali:~# yarac -h
Usage: yarac [OPTION]... [NAMESPACE:]SOURCE_FILE... OUTPUT_FILE
       --atom-quality-table=FILE        path to a file with the atom quality table
  -d,  --define=VAR=VALUE               define external variable
       --fail-on-warnings               fail on warnings
  -h,  --help                           show this help and exit
  -E,  --strict-escape                  warn on unknown escape sequences
       --max-strings-per-rule=NUMBER    set maximum number of strings per rule (default=10000)
  -w,  --no-warnings                    disable warnings
  -v,  --version                        show version information
Send bug reports and suggestions to:
[email protected]
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install yara`，再执行 `libyara-dev --version` 2>/dev/null || `libyara-dev -V`
- [ ] **2.** **读官方帮助** —— `libyara-dev -h`，需要细节时 `man libyara-dev`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: yara [OPTION]... [NAMESPACE:]RULES_FILE... FILE | DIR | PID`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/yara/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[yara](../../tools/tutorials/02-漏洞分析/yara.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/yara/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/yara/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
