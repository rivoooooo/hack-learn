# sshuttle

> Transparent proxy server for VPN over SSH Sshuttle makes it possible to access remote networks using SSH. It creates a transparent proxy server, using iptables, that will forward all the traffic through an SSH tunnel to a remote copy of ss…

> **功能分类**：通用工具 ｜ **Kali 包**：`sshuttle` ｜ **官方文档**：<https://www.kali.org/tools/sshuttle/>

## 1. 安装

```bash
sudo apt update
sudo apt install sshuttle
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3.2 |
| 架构 | all |
| 可执行命令 | `sshuttle` |
| 安装体积 | 861 KB |
| 官网 | <https://github.com/sshuttle/sshuttle> |
| 源码仓库 | <https://salsa.debian.org/debian/sshuttle> |
| 包追踪 | <https://pkg.kali.org/pkg/sshuttle> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sshuttle -h          # 查看用法
man sshuttle         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sshuttle`

官方给出的调用示例：`sshuttle -h`

```text
root@kali:~# sshuttle -h
usage: sshuttle [-l [ip:]port] -r [user@]sshserver[:port] <subnets...>
positional arguments:
  IP/MASK[:PORT[-PORT]]...
                        capture and forward traffic to these subnets
                        (whitespace separated)
options:
  -h, --help            show this help message and exit
  -l, --listen [IP:]PORT
                        transproxy to this ip address and port number
  -H, --auto-hosts      continuously scan for remote hostnames and update
                        local /etc/hosts as they are found
  -N, --auto-nets       automatically determine subnets to route
  --dns                 capture local DNS requests and forward to the remote
                        DNS server
  --ns-hosts IP[,IP]    capture and forward DNS requests made to the following
                        servers (comma separated)
  --to-ns IP[:PORT]     the DNS server to forward requests to; defaults to
                        servers in /etc/resolv.conf on remote side if not
                        given.
  --method TYPE         auto, nft, nat, tproxy, pf, ipfw
  --python PATH         path to python interpreter on the remote server
  -r, --remote [USERNAME[:PASSWORD]@]ADDR[:PORT]
                        ssh hostname (and optional username and password) of
                        remote sshuttle server
  -x, --exclude IP/MASK[:PORT[-PORT]]
                        exclude this subnet (can be used more than once)
  -X, --exclude-from PATH
                        exclude the subnets in a file (whitespace separated)
  -v, --verbose         increase debug message verbosity (can be used more
                        than once)
  -V, --version         print the sshuttle version number and exit
  -e, --ssh-cmd CMD     the command to use to connect to the remote [ssh]
  --no-cmd-delimiter    do not add a double dash before the python command
  --remote-shell PROGRAM
                        alternate remote shell program instead of defacto
                        posix shell. For Windows targets it would be either
                        `cmd` or `powershell` unless something like git-bash
                        is in use.
  --seed-hosts HOSTNAME[,HOSTNAME]
                        comma-separated list of hostnames for initial scan
                        (may be used with or without --auto-hosts)
  --no-latency-control  sacrifice latency to improve bandwidth benchmarks
  --latency-buffer-size SIZE
                        size of latency control buffer
  --wrap NUM            restart counting channel numbers after this number
                        (for testing)
  --disable-ipv6        disable IPv6 support
  -D, --daemon          run in the background as a daemon
  -s, --subnets PATH    file where the subnets are stored, instead of on the
                        command line
  --syslog              send log messages to syslog (default if you use
                        --daemon)
  --pidfile PATH        pidfile name (only if using --daemon) [./sshuttle.pid]
  --user USER           apply all the rules only to this linux user
  --group GROUP         apply all the rules only to this linux group
  --firewall            (internal use only)
  --hostwatch           (internal use only)
  --sudoers-no-modify   Prints a sudo configuration to STDOUT which allows a
                        user to run sshuttle without a password. This option
                        is INSECURE because, with some cleverness, it also
                        allows the user to run any command as root without a
                        password. The output also includes a suggested method
                        for you to install the configuration.
  --sudoers-user SUDOERS_USER
                        Set the user name or group with %group_name for
                        passwordless operation. Default is the current user.
                        Only works with the --sudoers-no-modify option.
  --no-sudo-pythonpath  do not set PYTHONPATH when invoking sudo
  -t, --tmark [MARK]    tproxy optional traffic mark with provided MARK value
                        in hexadecimal (default '0x01')
  --namespace NAMESPACE
                        Run inside of a net namespace with the given name.
  --namespace-pid NAMESPACE_PID
                        Run inside the net namespace used by the process with
                        the given pid.
Learn more with
OffSec
Want to learn more about sshuttle? get access to in-depth training and hands-on labs:
PEN-200: 19.3.5. Port Redirection and SSH Tunneling: Using sshuttle
PEN-200 course
Updated on: 2025-Dec-09
 Edit this page
sqlsus
sslstrip
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sshuttle`，再执行 `sshuttle --version` 2>/dev/null || `sshuttle -V`
- [ ] **2.** **读官方帮助** —— `sshuttle -h`，需要细节时 `man sshuttle`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sshuttle -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sshuttle/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sshuttle/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sshuttle/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
