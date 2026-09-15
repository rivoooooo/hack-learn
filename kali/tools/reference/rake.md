# rake

> Ruby make-like utility Rake is a simple ruby build program with capabilities similar to make. Rake has the following features: Rakefiles (rakes version of Makefiles) are completely defined in standard Ruby syntax. No XML files to edit. No …

> **功能分类**：信息搜集 ｜ **Kali 包**：`rake` ｜ **官方文档**：<https://www.kali.org/tools/rake/>

## 1. 安装

```bash
sudo apt update
sudo apt install rake
```

| 项目 | 内容 |
|------|------|
| 版本 | 13.4.2 |
| 架构 | all |
| 可执行命令 | `rake` |
| 依赖 | `ruby` |
| 安装体积 | 208 KB |
| 官网 | <https://github.com/ruby/rake> |
| 源码仓库 | <https://salsa.debian.org/ruby-team/rake> |
| 包追踪 | <https://pkg.kali.org/pkg/rake> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
rake -h          # 查看用法
man rake         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rake`

官方给出的调用示例：`rake -h`

```text
root@kali:~# rake -h
rake [-f rakefile] {options} targets...
Options are ...
        --backtrace=[OUT]            Enable full backtrace.  OUT can be stderr (default) or stdout.
        --comments                   Show commented tasks only
        --job-stats [LEVEL]          Display job statistics. LEVEL=history displays a complete job list
        --rules                      Trace the rules resolution.
        --suppress-backtrace PATTERN Suppress backtrace lines matching regexp PATTERN. Ignored if --trace is on.
    -A, --all                        Show all tasks, even uncommented ones (in combination with -T or -D)
    -B, --build-all                  Build all prerequisites, including those which are up-to-date.
    -C, --directory [DIRECTORY]      Change to DIRECTORY before doing anything.
    -D, --describe [PATTERN]         Describe the tasks (matching optional PATTERN), then exit.
    -e, --execute CODE               Execute some Ruby code and exit.
    -E, --execute-continue CODE      Execute some Ruby code, then continue with normal task processing.
    -f, --rakefile [FILENAME]        Use FILENAME as the rakefile to search for.
    -G, --no-system, --nosystem      Use standard project Rakefile search paths, ignore system wide rakefiles.
    -g, --system                     Using system wide (global) rakefiles (usually '~/.rake/*.rake').
    -I, --libdir LIBDIR              Include LIBDIR in the search path for required modules.
    -j, --jobs [NUMBER]              Specifies the maximum number of tasks to execute in parallel. (default is number of CPU cores + 4)
    -m, --multitask                  Treat all tasks as multitasks.
    -n, --dry-run                    Do a dry run without executing actions.
    -N, --no-search, --nosearch      Do not search parent directories for the Rakefile.
    -P, --prereqs                    Display the tasks and dependencies, then exit.
    -p, --execute-print CODE         Execute some Ruby code, print the result, then exit.
    -q, --quiet                      Do not log messages to standard output.
    -r, --require MODULE             Require MODULE before executing rakefile.
    -R, --rakelibdir RAKELIBDIR,     Auto-import any .rake files in RAKELIBDIR. (default is 'rakelib')
        --rakelib
    -s, --silent                     Like --quiet, but also suppresses the 'in directory' announcement.
    -t, --trace=[OUT]                Turn on invoke/execute tracing, enable full backtrace. OUT can be stderr (default) or stdout.
    -T, --tasks [PATTERN]            Display the tasks (matching optional PATTERN) with descriptions, then exit. -AT combination displays all the tasks, including those without descriptions.
    -v, --verbose                    Log message to standard output.
    -V, --version                    Display the program version.
    -W, --where [PATTERN]            Describe the tasks (matching optional PATTERN), then exit.
    -X, --no-deprecation-warnings    Disable the deprecation warnings.
    -h, -H, --help                   Display this help message.
Updated on: 2026-May-25
 Edit this page
powershell
recoverjpeg
LIGHT
DARK
Links
Home
Download / Get Kali
Blog
OS Documentation
Tool Documentation
System Status
Archived Releases
Partnerships
Platforms
ARM (SBC)
NetHunter (Mobile)
Amazon AWS
Docker
Linode
Microsoft Azure
Microsoft Store (WSL)
Vagrant
Development
Bug Tracker
Continuous Integration
Network Mirror
Package Tracker
GitLab
Community
Discord
Support Forum
PeerTube
Follow Us
Bluesky
Facebook
Instagram
Mastodon
Substack
X
Newsletter
RSS
Policies
Cookie Policy
Privacy Policy
Trademark Policy
© OffSec Services Limited 2026. All rights reserved.
Kali Linux is part of OffSec's Community Projects
Learn more about OffSec's free, open-source penetration testing tools for cybersecurity professionals
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install rake`，再执行 `rake --version` 2>/dev/null || `rake -V`
- [ ] **2.** **读官方帮助** —— `rake -h`，需要细节时 `man rake`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `rake -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rake/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rake/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rake/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
