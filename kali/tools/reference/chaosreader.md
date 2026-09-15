# chaosreader

> Trace network sessions and export it to html format Chaosreader traces TCP/UDP/others sessions and fetches application data from snoop or tcpdump logs (or other libpcap compatible programs). This is a type of “any-snarf” program, as it wil…

> **功能分类**：通用工具 ｜ **Kali 包**：`chaosreader` ｜ **官方文档**：<https://www.kali.org/tools/chaosreader/>

## 1. 安装

```bash
sudo apt update
sudo apt install chaosreader
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.96 |
| 架构 | all |
| 可执行命令 | `chaosreader` |
| 依赖 | `libnet-dns-perl`、`perl` |
| 安装体积 | 230 KB |
| 官网 | <https://www.brendangregg.com/chaosreader.html> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/chaosreader> |
| 包追踪 | <https://pkg.kali.org/pkg/chaosreader> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
chaosreader -h          # 查看用法
man chaosreader         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `chaosreader`

> 官方示例调用：`chaosreader --help`

```text
root@kali:~# chaosreader --help
Version 0.95i, 14-Apr-2014
USAGE: chaosreader [-adehiknqrvxAHIRTUXY] [-D dir]
                   [-b port[,...]] [-B port[,...]]
                   [-j IPaddr[,...]] [-J IPaddr[,...]]
                   [-l port[,...]] [-L port[,...]] [-m bytes[k]]
                   [-M bytes[k]] [-o "time"|"size"|"type"|"ip"]
                   [-p port[,...]] [-P port[,...]]
                   infile [infile2 ...]
       chaosreader -s [mins] | -S [mins[,count]]
	           [-z] [-f 'filter']
   chaosreader           # Create application session files, indexes
   -a, --application     # Create application session files (default)
   -d, --preferdns       # Show DNS names instead of IP addresses
   -e, --everything      # Create HTML 2-way & hex files for everything
   -h                    # Print a brief help
   --help                # Print verbose help (this) and version
   --help2               # Print massive help
   -i, --info            # Create info file
   -q, --quiet           # Quiet, no output to screen
   -r, --raw             # Create raw files
   -v, --verbose         # Verbose - Create ALL files .. (except -e)
   -x, --index           # Create index files (default)
   -A, --noapplication   # Exclude application session files
   -H, --hex             # Include hex dumps (slow)
   -I, --noinfo          # Exclude info files
   -R, --noraw           # Exclude raw files
   -T, --notcp           # Exclude TCP traffic
   -U, --noudp           # Exclude UDP traffic
   -Y, --noicmp          # Exclude ICMP traffic
   -X, --noindex         # Exclude index files
   -k, --keydata         # Create extra files for keystroke analysis
   -n, --names           # Include hostnames in hyperlinked HTTPlog (HTML)
   -D dir    --dir dir        # Output all files to this directory
   -b 25,79  --playtcp 25,79  # replay these TCP ports as well (playback)
   -B 36,42  --playudp 36,42  # replay these UDP ports as well (playback)
   -l 7,79   --htmltcp 7,79   # Create HTML for these TCP ports as well
   -L 7,123  --htmludp 7,123  # Create HTML for these UDP ports as well
   -m 1k     --min 1k         # Min size of connection to save ("k" for Kb)
   -M 1024k  --max 1k         # Max size of connection to save ("k" for Kb)
   -o size   --sort size      # sort Order: time/size/type/ip (Default time)
   -p 21,23  --port 21,23     # Only examine these ports (TCP & UDP)
   -P 80,81  --noport 80,81   # Exclude these ports (TCP & UDP)
   -s 5      --runonce 5      # Standalone. Run tcpdump/snoop for 5 mins.
   -S 5,10   --runmany 5,10   # Standalone, many. 10 samples of 5 mins each.
   -S 5      --runmany 5      # Standalone, endless. 5 min samples forever.
   -z        --runredo        # Standalone, redo. Rereads last run's logs.
   -j 10.1.2.1  --ipaddr 10.1.2.1    # Only examine these IPs
   -J 10.1.2.1  --noipaddr 10.1.2.1  # Exclude these IPs
   -f 'port 7'  --filter 'port 7'    # With standalone, use this dump filter.
eg1,
     tcpdump -s9000 -w output1          # create tcpdump capture file
     chaosreader output1                # extract recognised sessions, or,
     chaosreader -ve output1            # gimme everything, or,
     chaosreader -p 20,21,23 output1    # only ftp and telnet...
eg2,
     snoop -o output1                   # create snoop capture file instead
     chaosreader output1                # extract recognised sessions...
eg3,
     chaosreader -S 2,5		# Standalone, sniff network 5 times for 2 mins
				# each. View index.html for progress (or .text)
Updated on: 2026-Mar-02
 Edit this page
cadaver
cilium-cli
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install chaosreader`，再执行 `chaosreader --version` 2>/dev/null || `chaosreader -V`
- [ ] **2.** **读官方帮助** —— `chaosreader -h`，需要细节时 `man chaosreader`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `chaosreader -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/chaosreader/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/chaosreader/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/chaosreader/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
