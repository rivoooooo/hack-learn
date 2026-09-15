# slimtoolkit

> Optimization of your containers This package contains Slim(toolkit). It was called DockerSlim, and it is now just Slim (SlimToolkit). It is a tool for developers with a number of different commands (build, xray, lint, debug and others) to …

> **功能分类**：通用工具 ｜ **Kali 包**：`slimtoolkit` ｜ **官方文档**：<https://www.kali.org/tools/slimtoolkit/>

## 1. 安装

```bash
sudo apt update
sudo apt install slimtoolkit
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.40.11 |
| 架构 | amd64 |
| 可执行命令 | `slimtoolkit`、`slim-sensor` |
| 依赖 | `docker.io`、`libc6`、`slim-sensor` |
| 安装体积 | 67.39 MB |
| 官网 | <https://github.com/slimtoolkit/slim> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/slimtoolkit> |
| 包追踪 | <https://pkg.kali.org/pkg/slimtoolkit> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
slimtoolkit -h          # 查看用法
man slimtoolkit         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `slim-sensor`

> 官方示例调用：`slim-sensor -h`

```text
root@kali:~# slim-sensor -h
Usage of slim-sensor:
  -a string
    	set path to an executable that'll be invoked at various sensor lifecycle events (post-start, pre-shutdown, etc)
  -appbom
    	get sensor application BOM
  -artifacts-dir string
    	output director for all sensor artifacts (default "/opt/_slim/artifacts")
  -b	get sensor application BOM
  -c string
    	provide a JSONL-encoded file with one ore more sensor commands (standalone mode only) (default "/opt/_slim/commands.json")
  -command-file string
    	provide a JSONL-encoded file with one ore more sensor commands (standalone mode only) (default "/opt/_slim/commands.json")
  -d	enable debug logging
  -debug
    	enable debug logging
  -e string
    	output director for all sensor artifacts (default "/opt/_slim/artifacts")
  -f string
    	set the logging format ('text', or 'json') (default "text")
  -l string
    	set the logging level ('debug', 'info', 'warn', 'error', 'fatal', 'panic') (default "info")
  -lifecycle-hook string
    	set path to an executable that'll be invoked at various sensor lifecycle events (post-start, pre-shutdown, etc)
  -log-file string
    	enable logging redirection to a file (allowing to keep sensor's output separate from the target app's output)
  -log-format string
    	set the logging format ('text', or 'json') (default "text")
  -log-level string
    	set the logging level ('debug', 'info', 'warn', 'error', 'fatal', 'panic') (default "info")
  -m string
    	set the sensor execution mode ('controlled' when sensor expect the driver 'slim' app to manipulate its lifecycle; or 'standalone' when sensor depends on nothing but the target app (default "controlled")
  -mode string
    	set the sensor execution mode ('controlled' when sensor expect the driver 'slim' app to manipulate its lifecycle; or 'standalone' when sensor depends on nothing but the target app (default "controlled")
  -mondel
    	enable monitor data event logging
  -n	enable monitor data event logging
  -o string
    	enable logging redirection to a file (allowing to keep sensor's output separate from the target app's output)
  -s string
    	set the signal to stop the target app (and, eventually, the sensor) (default "TERM")
  -stop-grace-period duration
    	set the time to wait for the graceful termination of the target app (before sensor SIGKILL's it) (default 5s)
  -stop-signal string
    	set the signal to stop the target app (and, eventually, the sensor) (default "TERM")
  -w duration
    	set the time to wait for the graceful termination of the target app (before sensor SIGKILL's it) (default 5s)
```

### `slimtoolkit`

> 官方示例调用：`slimtoolkit -h`

```text
root@kali:~# slimtoolkit -h
Incorrect Usage. flag: help requested
NAME:
   slimtoolkit - inspect, optimize and debug your containers!
USAGE:
   slimtoolkit [global options] command [command options] [arguments...]
VERSION:
   linux/amd64|Transformer|latest|latest|latest
COMMANDS:
   xray, x              Shows what's inside of your container image and reverse engineers its Dockerfile
   lint, l              Analyzes container instructions in Dockerfiles
   build, b             Analyzes, profiles and optimizes your container image auto-generating Seccomp and AppArmor security profiles
   merge, m             Merge two container images (optimized to merge minified images)
   images, i            Get information about container images
   registry, r          Execute registry operations
   vulnerability, vuln  Execute vulnerability related tools and operations
   profile, p           Collects fat image information and generates a fat container report
   version, v           Shows slim and docker version information
   appbom, a            Show application BOM
   help, h              Show help info
   update, u            Updates slim
   install, in          Installs slim
   run, r               Run one or more containers
   debug, dbg           Debug the target container from a debug (side-car) container
   internal.metadata:
     docker-cli-plugin-metadata  Plugin metadata for the docker cli
GLOBAL OPTIONS:
   --report value           command report location (enabled by default; set it to "off" to disable it) (default: "slim.report.json")
   --check-version          check if the current version is outdated (default: true) [$DSLIM_CHECK_VERSION]
   --debug                  enable debug logs (default: false) [$DSLIM_DEBUG]
   --verbose                enable info logs (default: false) [$DSLIM_VERBOSE]
   --quiet                  Quiet CLI execution mode (default: false) [$DSLIM_QUIET]
   --log-level value        set the logging level ('debug', 'info', 'warn' (default), 'error', 'fatal', 'panic') (default: "warn") [$DSLIM_LOG_LEVEL]
   --log value              log file to store logs
   --log-format value       set the format used by logs ('text' (default), or 'json') (default: "text")
   --output-format value    set the output format to use ('text' (default), or 'json') (default: "text")
   --tls                    use TLS (default: true)
   --tls-verify             verify TLS (default: true)
   --tls-cert-path value    path to TLS cert files
   --crt-api-version value  Container runtime API version (default: "1.24") [$DSLIM_CRT_API_VER]
   --host value             Docker host address
   --state-path value       app state base path
   --in-container           app is running in a container (default: false)
   --archive-state value    archive app state to the selected Docker volume (default volume - slim-state). By default, enabled when app is running in a container (disabled otherwise). Set it to "off" to disable explicitly.
   --no-color               disable color output (default: false)
   --version, -v            print the version (default: false)
Updated on: 2025-Dec-09
 Edit this page
sipp
slowhttptest
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install slimtoolkit`，再执行 `slimtoolkit --version` 2>/dev/null || `slimtoolkit -V`
- [ ] **2.** **读官方帮助** —— `slimtoolkit -h`，需要细节时 `man slimtoolkit`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage of slim-sensor:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/slimtoolkit/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/slimtoolkit/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/slimtoolkit/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
