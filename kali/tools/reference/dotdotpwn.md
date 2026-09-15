# dotdotpwn

> Directory Traversal Fuzzer. DotDotPwn is a very flexible intelligent fuzzer to discover traversal directory vulnerabilities in software such as HTTP/FTP/TFTP servers, Web platforms such as CMSs, ERPs, Blogs, etc.

> **功能分类**：Web 应用 ｜ **Kali 包**：`dotdotpwn` ｜ **官方文档**：<https://www.kali.org/tools/dotdotpwn/>

## 1. 安装

```bash
sudo apt update
sudo apt install dotdotpwn
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.0.2 |
| 架构 | any |
| 可执行命令 | `dotdotpwn` |
| 依赖 | `libnet-tftp-perl`、`libwww-perl`、`perl` |
| 安装体积 | 236 KB |
| 官网 | <https://dotdotpwn.blogspot.ca> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/dotdotpwn> |
| 包追踪 | <https://pkg.kali.org/pkg/dotdotpwn> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Use the HTTP scan module (-m http) against a host (-h 192.168.1.1) , using the GET method (-M GET):
root@kali:~# dotdotpwn.pl -m http -h 192.168.1.1 -M GET
#################################################################################
#                                                                               #
#  CubilFelino                                                       Chatsubo   #
#  Security Research Lab              and            [(in)Security Dark] Labs   #
#  chr1x.sectester.net                             chatsubo-labs.blogspot.com   #
#                                                                               #
#                               pr0udly present:                                #
#                                                                               #
#  ________            __  ________            __  __________                   #
#  \______ \    ____ _/  |_\______ \    ____ _/  |_\______   \__  _  __ ____    #
#   |    |  \  /  _ \\   __\|    |  \  /  _ \\   __\|     ___/\ \/ \/ //    \   #
#   |    `   \(  <_> )|  |  |    `   \(  <_> )|  |  |    |     \     /|   |  \  #
#  /_______  / \____/ |__| /_______  / \____/ |__|  |____|      \/\_/ |___|  /  #
#          \/                      \/                                      \/   #
#                               - DotDotPwn v3.0 -                              #
#                         The Directory Traversal Fuzzer                        #
#                         http://dotdotpwn.sectester.net                        #
#                            dotdotpwn@sectester.net                            #
#                                                                               #
#                               by chr1x & nitr0us                              #
#################################################################################

[+] Report name: Reports/192.168.1.1_05-20-2014_08-41.txt

[========== TARGET INFORMATION ==========]
[+] Hostname: 192.168.1.1
[+] Protocol: http
[+] Port: 80

[=========== TRAVERSAL ENGINE ===========]
[+] Creating Traversal patterns (mix of dots and slashes)
[+] Multiplying 6 times the traversal patterns (-d switch)
[+] Creating the Special Traversal patterns
[+] Translating (back)slashes in the filenames
[+] Adapting the filenames according to the OS type detected (generic)
[+] Including Special sufixes
[+] Traversal Engine DONE ! - Total traversal tests created: 19680

[=========== TESTING RESULTS ============]
[+] Ready to launch 3.33 traversals per second
[+] Press Enter to start the testing (You can stop it pressing Ctrl + C)
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dotdotpwn.pl`

> 官方示例调用：`dotdotpwn.pl -m http -h 192.168.1.1 -M GET`

```text
root@kali:~# dotdotpwn.pl -m http -h 192.168.1.1 -M GET
#################################################################################
#                                                                               #
#  CubilFelino                                                       Chatsubo   #
#  Security Research Lab              and            [(in)Security Dark] Labs   #
#  chr1x.sectester.net                             chatsubo-labs.blogspot.com   #
#                                                                               #
#                               pr0udly present:                                #
#                                                                               #
#  ________            __  ________            __  __________                   #
#  \______ \    ____ _/  |_\______ \    ____ _/  |_\______   \__  _  __ ____    #
#   |    |  \  /  _ \\   __\|    |  \  /  _ \\   __\|     ___/\ \/ \/ //    \   #
#   |    `   \(  <_> )|  |  |    `   \(  <_> )|  |  |    |     \     /|   |  \  #
#  /_______  / \____/ |__| /_______  / \____/ |__|  |____|      \/\_/ |___|  /  #
#          \/                      \/                                      \/   #
#                               - DotDotPwn v3.0 -                              #
#                         The Directory Traversal Fuzzer                        #
#                         http://dotdotpwn.sectester.net                        #
#
[email protected]
                            #
#                                                                               #
#                               by chr1x & nitr0us                              #
#################################################################################
[+] Report name: Reports/192.168.1.1_05-20-2014_08-41.txt
[========== TARGET INFORMATION ==========]
[+] Hostname: 192.168.1.1
[+] Protocol: http
[+] Port: 80
[=========== TRAVERSAL ENGINE ===========]
[+] Creating Traversal patterns (mix of dots and slashes)
[+] Multiplying 6 times the traversal patterns (-d switch)
[+] Creating the Special Traversal patterns
[+] Translating (back)slashes in the filenames
[+] Adapting the filenames according to the OS type detected (generic)
[+] Including Special sufixes
[+] Traversal Engine DONE ! - Total traversal tests created: 19680
[=========== TESTING RESULTS ============]
[+] Ready to launch 3.33 traversals per second
[+] Press Enter to start the testing (You can stop it pressing Ctrl + C)
```

### `dotdotpwn`

> 官方示例调用：`dotdotpwn -h`

```text
root@kali:~# dotdotpwn -h
#################################################################################
#                                                                               #
#  CubilFelino                                                       Chatsubo   #
#  Security Research Lab              and            [(in)Security Dark] Labs   #
#  chr1x.sectester.net                             chatsubo-labs.blogspot.com   #
#                                                                               #
#                               pr0udly present:                                #
#                                                                               #
#  ________            __  ________            __  __________                   #
#  \______ \    ____ _/  |_\______ \    ____ _/  |_\______   \__  _  __ ____    #
#   |    |  \  /  _ \\   __\|    |  \  /  _ \\   __\|     ___/\ \/ \/ //    \   #
#   |    `   \(  <_> )|  |  |    `   \(  <_> )|  |  |    |     \     /|   |  \  #
#  /_______  / \____/ |__| /_______  / \____/ |__|  |____|      \/\_/ |___|  /  #
#          \/                      \/                                      \/   #
#                              - DotDotPwn v3.0.2 -                             #
#                         The Directory Traversal Fuzzer                        #
#                         http://dotdotpwn.sectester.net                        #
#
[email protected]
                            #
#                                                                               #
#                               by chr1x & nitr0us                              #
#################################################################################
Usage: ./dotdotpwn.pl -m <module> -h <host> [OPTIONS]
	Available options:
	-m	Module [http | http-url | ftp | tftp | payload | stdout]
	-h	Hostname
	-O	Operating System detection for intelligent fuzzing (nmap)
	-o	Operating System type if known ("windows", "unix" or "generic")
	-s	Service version detection (banner grabber)
	-d	Depth of traversals (e.g. deepness 3 equals to ../../../; default: 6)
	-f	Specific filename (e.g. /etc/motd; default: according to OS detected, defaults in TraversalEngine.pm)
	-E	Add @Extra_files in TraversalEngine.pm (e.g. web.config, httpd.conf, etc.)
	-S	Use SSL for HTTP and Payload module (not needed for http-url, use a https:// url instead)
	-u	URL with the part to be fuzzed marked as TRAVERSAL (e.g. http://foo:8080/id.php?x=TRAVERSAL&y=31337)
	-k	Text pattern to match in the response (http-url & payload modules - e.g. "root:" if trying /etc/passwd)
	-p	Filename with the payload to be sent and the part to be fuzzed marked with the TRAVERSAL keyword
	-x	Port to connect (default: HTTP=80; FTP=21; TFTP=69)
	-t	Time in milliseconds between each test (default: 300 (.3 second))
	-X	Use the Bisection Algorithm to detect the exact deepness once a vulnerability has been found
	-e	File extension appended at the end of each fuzz string (e.g. ".php", ".jpg", ".inc")
	-U	Username (default: 'anonymous')
	-P	Password (default: '
[email protected]
')
	-M	HTTP Method to use when using the 'http' module [GET | POST | HEAD | COPY | MOVE] (default: GET)
	-r	Report filename (default: 'HOST_MM-DD-YYYY_HOUR-MIN.txt')
	-b	Break after the first vulnerability is found
	-q	Quiet mode (doesn't print each attempt)
	-C	Continue if no data was received from host
Updated on: 2025-Dec-09
 Edit this page
doona
dploot
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dotdotpwn`，再执行 `dotdotpwn --version` 2>/dev/null || `dotdotpwn -V`
- [ ] **2.** **读官方帮助** —— `dotdotpwn -h`，需要细节时 `man dotdotpwn`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ./dotdotpwn.pl -m <module> -h <host> [OPTIONS]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dotdotpwn/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dotdotpwn/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dotdotpwn/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
