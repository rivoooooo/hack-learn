# gsocket

> Allows two machines on different networks to communicate with each other Abandon the thought of IP Addresses and Port Numbers. Instead start thinking that two programs should be able to communicate with each other as long as they know the …

> **功能分类**：通用工具 ｜ **Kali 包**：`gsocket` ｜ **官方文档**：<https://www.kali.org/tools/gsocket/>

## 1. 安装

```bash
sudo apt update
sudo apt install gsocket
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.4.43 |
| 架构 | any |
| 可执行命令 | `gsocket`、`blitz`、`gs-mount`、`gs-netcat`、`gs-sftp` |
| 依赖 | `libc6`、`libssl3t64`、`blitz` |
| 安装体积 | 286 KB |
| 官网 | <https://github.com/hackerschoice/gsocket> |
| 源码仓库 | <https://salsa.debian.org/debian/gsocket> |
| 包追踪 | <https://pkg.kali.org/pkg/gsocket> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gsocket -h          # 查看用法
man gsocket         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 5 个可执行命令，下面是官方页面内嵌的帮助原文。

### `blitz`

官方给出的调用示例：`blitz -h`

```text
root@kali:~# blitz -h
blitz [-k file] [-s password] [-l] [FILES ...]
   -l           Server Mode.
   -s <secret>  Secret (e.g. password).
   -k <file>    Read Secret from file.
   -f <list>	Read list of file names from FILE [or - for stdin]
   -o RSOPT=val Options passed to rsync.
 Example:
    $ blitz -s MySecret -l             # Server
    $ blitz -s MySecret *.dat          # Client
...limiting transfer rate to 10kB/sec
    $ blitz -s MySecret -o 'RSOPT=--bwlimit=10 -v' /etc/*.conf *.dat
...reading the file list from standard-in
    $ cd /etc
    $ find . -name '*.mp3' | blitz -s MySecret -f -
...limit the amount of path information by inserting a dot and slash
    $ blitz -s MySecret ~/tools/./upx/mp3
See 'man gs-netcat' and 'man rsync' for more options.
```

### `gs-mount`

官方给出的调用示例：`gs-mount -h`

```text
root@kali:~# gs-mount -h
gs-mount [-k file] [-s password] [-l] [mount point]
   -l           Server Mode.
   -R           Server in read-only mode.
   -s <secret>  Secret (e.g. password).
   -k <file>    Read Secret from file.
Example:
    $ gs-mount -s MySecret -l             # Server
    $ gs-mount -s MySecret                # Client
See 'gs-netcat -h' for more options.
```

### `gs-netcat`

官方给出的调用示例：`gs-netcat -h`

```text
root@kali:~# gs-netcat -h
gs-netcat [-skrlgvqwCTLtSDuim] [-s secret] [-e cmd] [-p port] [-d ip]
Version 1.4.42, Aug 15 2026 17:28:47 [OpenSSL 3.6.3 9 Jun 2026]
  -s <secret>  Secret (e.g. password).
  -k <file>    Read Secret from file.
  -r           Receive-only. Terminate when no more data.
  -I           Ignore EOF on stdin.
  -l           Listening server [default: client]
  -g           Generate a Secret (random)
  -v           Verbose. -vv more verbose. -vvv insanely verbose
  -q           Quiet. No log output
  -w           Wait for server to become available [client only]
  -C           Disable encryption
  -T           Use TOR or any Socks proxy (See gs-netcat(1))
  -L <file>    Logfile
  -t           Check if peer is listening (do not connect)
  -S           Act as a SOCKS server [needs -l]
  -D           Daemon & Watchdog mode [background]
  -d <IP>      IPv4 address for port forwarding
  -p <port>    Port to listen on or forward to
  -u           Use UDP [requires -p]
  -i           Interactive login shell (TTY) [Ctrl-e q to terminate]
  -e <cmd>     Execute command [e.g. "bash -il" or "id"]
  -m           Display man page
Example to forward traffic from port 2222 to 192.168.6.7:22:
    $ gs-netcat -l -d 192.168.6.7 -p 22     # Server
    $ gs-netcat -p 2222                     # Client
Example to act as a SOCKS proxy
    $ gs-netcat -l -S                       # Server
    $ gs-netcat -p 1080                     # Client
Example file transfer:
    $ gs-netcat -l -r >warez.tar.gz         # Server
    $ gs-netcat <warez.tar.gz               # Client
Example for a reverse shell:
    $ gs-netcat -l -i                       # Server
    $ gs-netcat -i                          # Client
```

### `gs-sftp`

官方给出的调用示例：`gs-sftp -h`

```text
root@kali:~# gs-sftp -h
gs-sftp [-k file] [-s password] [-l]
   -l           Server Mode.
   -R           Server in read-only mode.
   -s <secret>  Secret (e.g. password).
   -k <file>    Read Secret from file.
Example:
    $ gs-sftp -s MySecret -l             # Server
    $ gs-sftp -s MySecret                # Client
See 'gs-netcat -h' for more options.
```

### `gsocket`

官方给出的调用示例：`gsocket -h`

```text
root@kali:~# gsocket -h
gsocket [-k file] [-s password] <programm> <parameters>
   -s <secret>  Secret (e.g. password).
   -k <file>    Read Secret from file.
   -p <ports>   Range of listening ports to redirect [default=all]
   -T           Use TOR.
Example:
    $ gsocket -s MySecret /usr/bin/sshd -d         # Server
    $ gsocket -s MySecret ssh root@gsocket         # Client
See 'gs-netcat -h' for more options.
Updated on: 2026-Aug-25
 Edit this page
gr-iqbal
gvm
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install gsocket`，再执行 `gsocket --version` 2>/dev/null || `gsocket -V`
- [ ] **2.** **读官方帮助** —— `gsocket -h`，需要细节时 `man gsocket`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `gsocket -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gsocket/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gsocket/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gsocket/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
