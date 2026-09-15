# brutespray

> Bruteforcing from various scanner output Brutespray has been re-written in Golang, eliminating the requirement for additional tools. This enhanced version is more extensive and operates at a significantly faster pace than its Python counte…

> **功能分类**：通用工具 ｜ **Kali 包**：`brutespray` ｜ **官方文档**：<https://www.kali.org/tools/brutespray/>

## 1. 安装

```bash
sudo apt update
sudo apt install brutespray
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.2.2 |
| 架构 | any |
| 可执行命令 | `brutespray` |
| 依赖 | `libc6` |
| 安装体积 | 24.46 MB |
| 官网 | <https://github.com/x90skysn3k/brutespray> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/brutespray> |
| 包追踪 | <https://pkg.kali.org/pkg/brutespray> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
Attack all services in nas.gnmap with a specific user list (unix_users.txt) and password list (password.lst):
root@kali:~# brutespray --file nas.gnmap -U /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/metasploit/password.lst --threads 3 --hosts 1

                              #@                           @/
                           @@@                               @@@
                        %@@@                                   @@@.
                      @@@@@                                     @@@@%
                     @@@@@                                       @@@@@
                    @@@@@@@                  @                  @@@@@@@
                    @(@@@@@@@%            @@@@@@@            &@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                     @@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@
                       @@@( @@@@@#@@@@@@@@@*@@@,@@@@@@@@@@@@@@@  @@@
                           @@@@@@ .@@@/@@@@@@@@@@@@@/@@@@ @@@@@@
                                  @@@   @@@@@@@@@@@   @@@
                                 @@@@*  ,@@@@@@@@@(  ,@@@@
                                 @@@@@@@@@@@@@@@@@@@@@@@@@
                                  @@@.@@@@@@@@@@@@@@@ @@@
                                    @@@@@@ @@@@@ @@@@@@
                                       @@@@@@@@@@@@@
                                       @@   @@@   @@
                                       @@ @@@@@@@ @@
                                         @@% @  @@



        ██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗██████╗ ██████╗  █████╗ ██╗   ██╗
        ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
        ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ███████╗██████╔╝██████╔╝███████║ ╚████╔╝
        ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ╚════██║██╔═══╝ ██╔══██╗██╔══██║  ╚██╔╝
        ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗███████║██║     ██║  ██║██║  ██║   ██║
        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝



 brutespray.py v1.5.2
 Created by: Shane Young/@x90skysn3k && Jacob Robles/@shellfail
 Inspired by: Leon Johnson/@sho-luv
 Credit to Medusa: JoMo-Kun / Foofus Networks <jmk@foofus.net>

Starting to brute, please make sure to use the right amount of threads(-t) and parallel hosts(-T)...  \

Brute-Forcing...
Medusa v2.2 [http://www.foofus.net] (C) JoMo-Kun / Foofus Networks <jmk@foofus.net>

ACCOUNT CHECK: [mysql] Host: 192.168.86.4 (1 of 1, 0 complete) User: 4Dgifts (1 of 111, 0 complete) Password: !@#$%^& (1 of 88396 complete)
ACCOUNT CHECK: [mysql] Host: 192.168.86.4 (1 of 1, 0 complete) User: 4Dgifts (1 of 111, 0 complete) Password: !@#$% (2 of 88396 complete)
ACCOUNT CHECK: [mysql] Host: 192.168.86.4 (1 of 1, 0 complete) User: 4Dgifts (1 of 111, 0 complete) Password: !@#$%^ (3 of 88396 complete)
[...]

Interactive mode, brute forcing the FTP service only.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `brutespray`

> 官方示例调用：`brutespray --file nas.gnmap -U /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/metasploit/password.lst --threads 3 --hosts 1`

```text
root@kali:~# brutespray --file nas.gnmap -U /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/metasploit/password.lst --threads 3 --hosts 1
                              #@                           @/
                           @@@                               @@@
                        %@@@                                   @@@.
                      @@@@@                                     @@@@%
                     @@@@@                                       @@@@@
                    @@@@@@@                  @                  @@@@@@@
                    @(@@@@@@@%            @@@@@@@            &@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                     @@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@
                       @@@( @@@@@#@@@@@@@@@*@@@,@@@@@@@@@@@@@@@  @@@
                           @@@@@@ .@@@/@@@@@@@@@@@@@/@@@@ @@@@@@
                                  @@@   @@@@@@@@@@@   @@@
                                 @@@@*  ,@@@@@@@@@(  ,@@@@
                                 @@@@@@@@@@@@@@@@@@@@@@@@@
                                  @@@.@@@@@@@@@@@@@@@ @@@
                                    @@@@@@ @@@@@ @@@@@@
                                       @@@@@@@@@@@@@
                                       @@   @@@   @@
                                       @@ @@@@@@@ @@
                                         @@% @  @@
        ██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗██████╗ ██████╗  █████╗ ██╗   ██╗
        ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
        ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ███████╗██████╔╝██████╔╝███████║ ╚████╔╝
        ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ╚════██║██╔═══╝ ██╔══██╗██╔══██║  ╚██╔╝
        ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗███████║██║     ██║  ██║██║  ██║   ██║
        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
 brutespray.py v1.5.2
 Created by: Shane Young/@x90skysn3k && Jacob Robles/@shellfail
 Inspired by: Leon Johnson/@sho-luv
 Credit to Medusa: JoMo-Kun / Foofus Networks <
[email protected]
>
Starting to brute, please make sure to use the right amount of threads(-t) and parallel hosts(-T)...  \
Brute-Forcing...
Medusa v2.2 [http://www.foofus.net] (C) JoMo-Kun / Foofus Networks <
[email protected]
>
ACCOUNT CHECK: [mysql] Host: 192.168.86.4 (1 of 1, 0 complete) User: 4Dgifts (1 of 111, 0 complete) Password: !@#$%^& (1 of 88396 complete)
ACCOUNT CHECK: [mysql] Host: 192.168.86.4 (1 of 1, 0 complete) User: 4Dgifts (1 of 111, 0 complete) Password: !@#$% (2 of 88396 complete)
ACCOUNT CHECK: [mysql] Host: 192.168.86.4 (1 of 1, 0 complete) User: 4Dgifts (1 of 111, 0 complete) Password: !@#$%^ (3 of 88396 complete)
[...]
Interactive mode, brute forcing the FTP service only.
```

### `brutespray -i -f nas.gnmap`

> 官方示例调用：`brutespray -i -f nas.gnmap`

```text
root@kali:~# brutespray -i -f nas.gnmap
                              #@                           @/
                           @@@                               @@@
                        %@@@                                   @@@.
                      @@@@@                                     @@@@%
                     @@@@@                                       @@@@@
                    @@@@@@@                  @                  @@@@@@@
                    @(@@@@@@@%            @@@@@@@            &@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                     @@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@
                       @@@( @@@@@#@@@@@@@@@*@@@,@@@@@@@@@@@@@@@  @@@
                           @@@@@@ .@@@/@@@@@@@@@@@@@/@@@@ @@@@@@
                                  @@@   @@@@@@@@@@@   @@@
                                 @@@@*  ,@@@@@@@@@(  ,@@@@
                                 @@@@@@@@@@@@@@@@@@@@@@@@@
                                  @@@.@@@@@@@@@@@@@@@ @@@
                                    @@@@@@ @@@@@ @@@@@@
                                       @@@@@@@@@@@@@
                                       @@   @@@   @@
                                       @@ @@@@@@@ @@
                                         @@% @  @@
        ██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗██████╗ ██████╗  █████╗ ██╗   ██╗
        ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
        ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ███████╗██████╔╝██████╔╝███████║ ╚████╔╝
        ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ╚════██║██╔═══╝ ██╔══██╗██╔══██║  ╚██╔╝
        ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗███████║██║     ██║  ██║██║  ██║   ██║
        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
 brutespray.py v1.5.2
 Created by: Shane Young/@x90skysn3k && Jacob Robles/@shellfail
 Inspired by: Leon Johnson/@sho-luv
 Credit to Medusa: JoMo-Kun / Foofus Networks <
[email protected]
>
Loading File: /
Welcome to interactive mode!
WARNING: Leaving an option blank will leave it empty and refer to default
Available services to brute-force:
Service: ftp on port 21 with 1 hosts
Service: ssh on port 22 with 1 hosts
Service: mysql on port 3306 with 1 hosts
Enter services you want to brute - default all (ssh,ftp,etc): ftp
Enter the number of parallel threads (default is 2): 4
Enter the number of parallel hosts to scan per service (default is 1): 1
Would you like to specify a wordlist? (y/n): y
Enter a userlist you would like to use: /usr/share/wordlists/metasploit/unix_users.txt
Enter a passlist you would like to use: /usr/share/wordlists/metasploit/password.lst
Would to specify a single username or password (y/n): n
Starting to brute, please make sure to use the right amount of threads(-t) and parallel hosts(-T)...  \
Brute-Forcing...
```

### `brutespray -h`

> 官方示例调用：`brutespray -h`

```text
root@kali:~# brutespray -h
Usage of brutespray:
  -C string
    	Specify a combo wordlist deiminated by ':', example: user1:password
  -H string
    	Target in the format service://host:port, CIDR ranges supported,
    	 default port will be used if not specified
  -P	Print found hosts parsed from provided host and file arguments
  -S	List all supported services
  -T int
    	Number of hosts to bruteforce at the same time (default 5)
  -f string
    	File to parse; Supported: Nmap, Nessus, Nexpose, Lists, etc
  -o string
    	Directory containing successful attempts (default "brutespray-output")
  -p string
    	Password or password file to use for bruteforce
  -q	Suppress the banner
  -r int
    	Amount of times to retry after receiving connection failed (default 3)
  -s string
    	Service type: ssh, ftp, smtp, etc; Default all (default "all")
  -t int
    	Number of threads to use (default 10)
  -u string
    	Username or user list to bruteforce
  -w duration
    	Set timeout of bruteforce attempts (default 5s)
Updated on: 2025-Dec-09
 Edit this page
bruteshark
bully
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install brutespray`，再执行 `brutespray --version` 2>/dev/null || `brutespray -V`
- [ ] **2.** **读官方帮助** —— `brutespray -h`，需要细节时 `man brutespray`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage of brutespray:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/brutespray/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/brutespray/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/brutespray/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
