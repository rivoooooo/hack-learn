# rustscan

> Modern Port Scanner The Modern Port Scanner. Find ports quickly (3 seconds at its fastest). Run scripts through our scripting engine (Python, Lua, Shell supported). Scans all 65k ports in 3 seconds. Full scripting engine support. Automatic…

> **功能分类**：通用工具 ｜ **Kali 包**：`rustscan` ｜ **官方文档**：<https://www.kali.org/tools/rustscan/>

## 1. 安装

```bash
sudo apt update
sudo apt install rustscan
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.4.1 |
| 架构 | any |
| 可执行命令 | `rustscan` |
| 依赖 | `libc6`、`libgcc-s1` |
| 安装体积 | 4.50 MB |
| 官网 | <https://github.com/bee-san/RustScan> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/rustscan> |
| 包追踪 | <https://pkg.kali.org/pkg/rustscan> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
rustscan -h          # 查看用法
man rustscan         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rustscan`

> 官方示例调用：`rustscan -h`

```text
root@kali:~# rustscan -h
rustscan 2.3.0
Fast Port Scanner built in Rust. WARNING Do not use this program against
sensitive infrastructure since the specified server may not be able to handle
this many socket connections at once. - Discord  <http://discord.skerritt.blog>
- GitHub <https://github.com/RustScan/RustScan>
USAGE:
    rustscan [OPTIONS] [-- <COMMAND>...]
OPTIONS:
  -a, --addresses <ADDRESSES>
          A comma-delimited list or newline-delimited file of separated CIDRs,
          IPs, or hosts to be scanned
  -p, --ports <PORTS>
          A list of comma separated ports to be scanned. Example: 80,443,8080
  -r, --range <RANGE>
          A range of ports with format start-end. Example: 1-1000
  -n, --no-config
          Whether to ignore the configuration file or not
      --no-banner
          Hide the banner
  -c, --config-path <CONFIG_PATH>
          Custom path to config file
  -g, --greppable
          Greppable mode. Only output the ports. No Nmap. Useful for grep or
          outputting to a file
      --accessible
          Accessible mode. Turns off features which negatively affect screen
          readers
      --resolver <RESOLVER>
          A comma-delimited list or file of DNS resolvers
  -b, --batch-size <BATCH_SIZE>
          The batch size for port scanning, it increases or slows the speed of
          scanning. Depends on the open file limit of your OS.  If you do 65535
          it will do every port at the same time. Although, your OS may not
          support this [default: 4500]
  -t, --timeout <TIMEOUT>
          The timeout in milliseconds before a port is assumed to be closed
          [default: 1500]
      --tries <TRIES>
          The number of tries before a port is assumed to be closed. If set to
          0, rustscan will correct it to 1 [default: 1]
  -u, --ulimit <ULIMIT>
          Automatically ups the ULIMIT with the value you provided
      --scan-order <SCAN_ORDER>
          The order of scanning to be performed. The "serial" option will scan
          ports in ascending order while the "random" option will scan ports
          randomly [default: serial] [possible values: serial, random]
      --scripts <SCRIPTS>
          Level of scripting required for the run [default: default] [possible
          values: none, default, custom]
      --top
          Use the top 1000 ports
  -e, --exclude-ports <EXCLUDE_PORTS>
          A list of comma separated ports to be excluded from scanning. Example:
          80,443,8080
  -x, --exclude-addresses <EXCLUDE_ADDRESSES>
          A list of comma separated CIDRs, IPs, or hosts to be excluded from
          scanning
      --udp
          UDP scanning mode, finds UDP ports that send back responses
  -h, --help
          Print help
  -V, --version
          Print version
Updated on: 2026-Sep-03
 Edit this page
katana
snaffler-ng
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install rustscan`，再执行 `rustscan --version` 2>/dev/null || `rustscan -V`
- [ ] **2.** **读官方帮助** —— `rustscan -h`，需要细节时 `man rustscan`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `rustscan -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rustscan/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rustscan/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rustscan/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
