# guymager

> Forensic imaging tool based on Qt The forensic imager contained in this package, guymager, was designed to support different image file formats, to be most user-friendly and to run really fast. It has a high speed multi-threaded engine usi…

> **功能分类**：数字取证 ｜ **Kali 包**：`guymager` ｜ **官方文档**：<https://www.kali.org/tools/guymager/>

## 1. 安装

```bash
sudo apt update
sudo apt install guymager
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.8.13 |
| 架构 | any |
| 可执行命令 | `guymager` |
| 依赖 | `hdparm`、`libc6`、`libewf2`、`libgcc-s1`、`libguytools2t64` |
| 安装体积 | 1.02 MB |
| 官网 | <https://guymager.sourceforge.net/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/guymager> |
| 包追踪 | <https://pkg.kali.org/pkg/guymager> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Screenshots
guymager
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

官方给出的调用示例：`man guymager`

```text
root@kali:~# man guymager
guymager(1)                 General Commands Manual                 guymager(1)
0.8.13-1" "guymager manual pages"
NAME
     guymager - a forensic acquisition program
SYNOPSIS
     guymager [log=log_file] [cfg=configuration_file] [options]
DESCRIPTION
     Guymager  is  a Qt-based forensic imager. It is capable of producing image
     files in EWF, AFF and dd format. Its main strenghs are the easy  user  in-
     terface, the high imaging speed and the extended acquisition info file.
     The internal structure is based on separate threads for reading, hash cal-
     culation (MD5 and SHA256), writing and includes a parallelised compression
     engine,  thus making full usage of multi-processor and hyper-threading ma-
     chines.
     Guymager should be run with root privileges, as other users  do  not  have
     access to physical devices normally.
OPTIONS
     log=log_file
            By  default,  guymager  uses /var/log/guymager.log as its log file.
            This option allows for specifying a different file.
     cfg=configuration_file
            The default configuration file is /etc/guymager/guymager.cfg.  This
            option  allows  for specifying a different file. Guymager creates a
            template configuration file when the  option  -cfg=template.cfg  is
            given.
     All  other  configuration  options  may  be  specified on the command line
     and/or in the configuration file. See /etc/guymager/guymager.cfg for a de-
     scription of all possible options. In case an option is specified  in  the
     configuration file and on the command line, the command line dominates.
EXIT CODES
     Guymager normally returns an exit code of 0. Exit code 1 means that Guy-
     mager terminated because the AutoExit function became active. All other
     exit codes are related to internal Guymager or Qt errors.
EXAMPLES
     Write all log entries to ./my.log:
            guymager log=my.log
     Create a template configuration file
            guymager cfg=template.cfg
     Read the configuration from my.cfg and use 4 threads for parallelised com-
     pression:
            guymager cfg=my.cfg CompressionThreads=4
     See /etc/guymager/guymager.cfg for details about option CompressionThreads
     and all other options as well.
AUTHOR
     Guy Voncken (develop (at) faert.net)
version 0.8.13-3                   2026-02-28                       guymager(1)
Updated on: 2026-May-25
 Edit this page
grokevt
hackrf
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install guymager`，再执行 `guymager --version` 2>/dev/null || `guymager -V`
- [ ] **2.** **读官方帮助** —— `guymager -h`，需要细节时 `man guymager`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `guymager -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/guymager/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/guymager/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/guymager/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
