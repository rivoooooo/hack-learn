# gitleaks

> Protect and discover secrets using Gitleaks 🔑 (program) Gitleaks is a SAST tool for detecting and preventing hardcoded

> **功能分类**：通用工具 ｜ **Kali 包**：`gitleaks` ｜ **官方文档**：<https://www.kali.org/tools/gitleaks/>

## 1. 安装

```bash
sudo apt update
sudo apt install gitleaks
```

| 项目 | 内容 |
|------|------|
| 版本 | 8.26.0 |
| 架构 | any |
| 可执行命令 | `gitleaks`、`golang-github-gitleaks-gitleaks-dev` |
| 依赖 | `libc6` |
| 安装体积 | 9.88 MB |
| 官网 | <https://github.com/gitleaks/gitleaks> |
| 源码仓库 | <https://salsa.debian.org/go-team/packages/gitleaks> |
| 包追踪 | <https://pkg.kali.org/pkg/gitleaks> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gitleaks -h          # 查看用法
man gitleaks         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `gitleaks`

官方给出的调用示例：`gitleaks -h`

```text
root@kali:~# gitleaks -h
Gitleaks scans code, past or present, for secrets
Usage:
  gitleaks [command]
Available Commands:
  completion  Generate the autocompletion script for the specified shell
  dir         scan directories or files for secrets
  git         scan git repositories for secrets
  help        Help about any command
  stdin       detect secrets from stdin
  version     display gitleaks version
Flags:
  -b, --baseline-path string          path to baseline with issues that can be ignored
  -c, --config string                 config file path
                                      order of precedence:
                                      1. --config/-c
                                      2. env var GITLEAKS_CONFIG
                                      3. env var GITLEAKS_CONFIG_TOML with the file content
                                      4. (target path)/.gitleaks.toml
                                      If none of the four options are used, then gitleaks will use the default config
      --enable-rule strings           only enable specific rules by id
      --exit-code int                 exit code when leaks have been encountered (default 1)
  -i, --gitleaks-ignore-path string   path to .gitleaksignore file or folder containing one (default ".")
  -h, --help                          help for gitleaks
      --ignore-gitleaks-allow         ignore gitleaks:allow comments
  -l, --log-level string              log level (trace, debug, info, warn, error, fatal) (default "info")
      --max-decode-depth int          allow recursive decoding up to this depth (default "0", no decoding is done)
      --max-target-megabytes int      files larger than this will be skipped
      --no-banner                     suppress banner
      --no-color                      turn off color for verbose output
      --redact uint[=100]             redact secrets from logs and stdout. To redact only parts of the secret just apply a percent value from 0..100. For example --redact=20 (default 100%)
  -f, --report-format string          output format (json, csv, junit, sarif, template)
  -r, --report-path string            report file
      --report-template string        template file used to generate the report (implies --report-format=template)
  -v, --verbose                       show verbose output from scan
      --version                       version for gitleaks
Use "gitleaks [command] --help" for more information about a command.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install gitleaks`，再执行 `gitleaks --version` 2>/dev/null || `gitleaks -V`
- [ ] **2.** **读官方帮助** —— `gitleaks -h`，需要细节时 `man gitleaks`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gitleaks/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gitleaks/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gitleaks/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
