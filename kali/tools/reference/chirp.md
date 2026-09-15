# chirp

> Configuration tool for amateur radios CHIRP is a free, open-source tool for programming your amateur radio. It supports a large number of manufacturers and models, as well as provides a way to interface with multiple data sources and forma…

> **功能分类**：无线攻击 ｜ **Kali 包**：`chirp` ｜ **官方文档**：<https://www.kali.org/tools/chirp/>

## 1. 安装

```bash
sudo apt update
sudo apt install chirp
```

| 项目 | 内容 |
|------|------|
| 版本 | 20251108 |
| 架构 | all |
| 可执行命令 | `chirp`、`chirpc`、`chirpw`、`experttune` |
| 依赖 | `python3`、`python3-lark`、`python3-requests`、`python3-serial`、`python3-suds`、`python3-yattag`、`wxpython-tools`、`chirpc` |
| 安装体积 | 8.53 MB |
| 官网 | <https://chirpmyradio.com/> |
| 源码仓库 | <https://salsa.debian.org/debian-hamradio-team/chirp> |
| 包追踪 | <https://pkg.kali.org/pkg/chirp> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
chirp -h          # 查看用法
man chirp         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `chirpc`

> 官方示例调用：`chirpc -h`

```text
root@kali:~# chirpc -h
usage: chirpc [-h] [--version] [-s SERIAL] [--list-settings] [-i] [--list-mem]
              [--list-special-mem] [--raw] [--get-mem] [--copy-mem]
              [--clear-mem] [--set-mem-name SET_MEM_NAME]
              [--set-mem-freq SET_MEM_FREQ] [--set-mem-tencon]
              [--set-mem-tencoff] [--set-mem-tsqlon] [--set-mem-tsqloff]
              [--set-mem-dtcson] [--set-mem-dtcsoff]
              [--set-mem-tenc SET_MEM_TENC] [--set-mem-tsql SET_MEM_TSQL]
              [--set-mem-dtcs SET_MEM_DTCS]
              [--set-mem-dtcspol SET_MEM_DTCSPOL] [--set-mem-dup SET_MEM_DUP]
              [--set-mem-offset SET_MEM_OFFSET] [--set-mem-mode SET_MEM_MODE]
              [-r RADIO] [--list-radios] [--mmap MMAP] [--download-mmap]
              [--upload-mmap] [-q] [-v] [--log LOG_FILE]
              [--log-level LOG_LEVEL]
              [arg ...]
positional arguments:
  arg                   Some commands require additional arguments
options:
  -h, --help            show this help message and exit
  --version             Print version and exit
  -s, --serial SERIAL   Serial port (default: mmap)
  --list-settings       List settings
  -i, --id              Request radio ID string
  -r, --radio RADIO     Radio model (see --list-radios)
  --list-radios         List radio models
  --mmap MMAP           Radio memory map file location
  --download-mmap       Download memory map from radio
  --upload-mmap         Upload memory map to radio
  -q, --quiet           Decrease verbosity
  -v, --verbose         Increase verbosity
  --log LOG_FILE        Log messages to a file
  --log-level LOG_LEVEL
                        Log file verbosity (critical, error, warn, info,
                        debug). Defaults to 'debug'.
Memory/Channel Options:
  --list-mem            List all memory locations
  --list-special-mem    List all special memory locations
  --raw                 Dump raw memory location
  --get-mem             Get and print memory location
  --copy-mem            Copy memory location
  --clear-mem           Clear memory location
  --set-mem-name SET_MEM_NAME
                        Set memory name
  --set-mem-freq SET_MEM_FREQ
                        Set memory frequency
  --set-mem-tencon      Set tone encode enabled flag
  --set-mem-tencoff     Set tone decode disabled flag
  --set-mem-tsqlon      Set tone squelch enabled flag
  --set-mem-tsqloff     Set tone squelch disabled flag
  --set-mem-dtcson      Set DTCS enabled flag
  --set-mem-dtcsoff     Set DTCS disabled flag
  --set-mem-tenc SET_MEM_TENC
                        Set memory encode tone
  --set-mem-tsql SET_MEM_TSQL
                        Set memory squelch tone
  --set-mem-dtcs SET_MEM_DTCS
                        Set memory DTCS code
  --set-mem-dtcspol SET_MEM_DTCSPOL
                        Set memory DTCS polarity (NN, NR, RN, RR)
  --set-mem-dup SET_MEM_DUP
                        Set memory duplex (+,-, or blank)
  --set-mem-offset SET_MEM_OFFSET
                        Set memory duplex offset (in MHz)
  --set-mem-mode SET_MEM_MODE
                        Set mode (WFM,FM,NFM,AM,NAM,DV,USB,LSB,CW,RTTY,DIG,PKT
                        ,NCW,NCWR,CWR,P25,Auto,RTTYR,FSK,FSKR,DMR,DN)
```

### `chirpw`

> 官方示例调用：`chirpw -h`

```text
root@kali:~# chirpw -h
usage: chirpw [-h] [--module module] [--version] [--profile]
              [--onlydriver ONLYDRIVER [ONLYDRIVER ...]] [--inspect]
              [--page PAGE]
              [--action {upload,download,query_rr,query_mg,query_rb,query_dm,new}]
              [--restore] [--force-language FORCE_LANGUAGE]
              [--config-dir CONFIG_DIR] [--no-linux-gdk-backend]
              [--install-desktop-app | --no-install-desktop-app] [-q] [-v]
              [--log LOG_FILE] [--log-level LOG_LEVEL]
              [file ...]
positional arguments:
  file                  File to open
options:
  -h, --help            show this help message and exit
  --module module       Load module on startup
  --version             Print version and exit
  --profile             Enable profiling
  --onlydriver ONLYDRIVER [ONLYDRIVER ...]
                        Include this driver while loading
  --inspect             Show wxPython inspector
  --page PAGE           Select this page of the default editor at start
  --action {upload,download,query_rr,query_mg,query_rb,query_dm,new}
                        Start UI action immediately
  --restore             Restore previous tabs
  --force-language FORCE_LANGUAGE
                        Force locale to this ISO language code
  --config-dir CONFIG_DIR
                        Use this alternate directory for config and other
                        profile data
  --no-linux-gdk-backend
                        Do not force GDK_BACKEND=x11
  --install-desktop-app
                        Install a desktop icon even if it was previously
                        refused
  --no-install-desktop-app
                        Do not prompt to install a desktop icon
  -q, --quiet           Decrease verbosity
  -v, --verbose         Increase verbosity
  --log LOG_FILE        Log messages to a file
  --log-level LOG_LEVEL
                        Log file verbosity (critical, error, warn, info,
                        debug). Defaults to 'debug'.
```

### `experttune`

> 官方示例调用：`experttune -h`

```text
root@kali:~# experttune -h
usage: experttune [-h] [--bands BANDS] [--call CALL]
                  [--next {interactive,auto}] [--debug]
                  {7200,7300,7610,Demo} port
A simple tool to automate running through the required frequencies to tune an
SPE Expert linear.
positional arguments:
  {7200,7300,7610,Demo}
                        Radio model
  port                  Serial port for CAT control
options:
  -h, --help            show this help message and exit
  --bands BANDS         Comma-separated list of bands to tune (160, 80, etc)
  --call CALL           Callsign for CW ID after each step
  --next {interactive,auto}
                        Next step strategy
  --debug               Enable verbose debugging
Updated on: 2025-Dec-09
 Edit this page
changeme
cisco-torch
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install chirp`，再执行 `chirp --version` 2>/dev/null || `chirp -V`
- [ ] **2.** **读官方帮助** —— `chirp -h`，需要细节时 `man chirp`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `chirp -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/chirp/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/chirp/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/chirp/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
