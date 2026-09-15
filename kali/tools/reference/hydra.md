# hydra

> Very fast network logon cracker Hydra is a parallelized login cracker which supports numerous protocols to attack. It is very fast and flexible, and new modules are easy to add. This tool makes it possible for researchers and security cons…

> **功能分类**：信息搜集 ｜ **Kali 包**：`hydra` ｜ **官方文档**：<https://www.kali.org/tools/hydra/>

## 1. 安装

```bash
sudo apt update
sudo apt install hydra
```

| 项目 | 内容 |
|------|------|
| 版本 | 9.7 |
| 架构 | any |
| 可执行命令 | `hydra`、`dpl4hydra`、`hydra-wizard`、`pw-inspector`、`hydra-gtk`、`xhydra` |
| 依赖 | `libapr1t64`、`libbson2-2`、`libc6`、`libfbclient2`、`libfreerdp3-3`、`libgcrypt20`、`libidn12`、`libmariadb3`、`libmemcached11t64`、`libmongoc2-2`、`libpcre2-8-0`、`libpq5` 等 |
| 安装体积 | 978 KB |
| 官网 | <https://github.com/vanhauser-thc/thc-hydra> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/hydra> |
| 包追踪 | <https://pkg.kali.org/pkg/hydra> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Attempt to login as the root user (-l root) using a password list (-P /usr/share/wordlists/metasploit/unix_passwords.txt) with 6 threads (-t 6) on the given SSH server (ssh://192.168.1.123):
root@kali:~# hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt -t 6 ssh://192.168.1.123
Hydra v7.6 (c)2013 by van Hauser/THC & David Maciejak - for legal purposes only

Hydra (http://www.thc.org/thc-hydra) starting at 2014-05-19 07:53:33
[DATA] 6 tasks, 1 server, 1003 login tries (l:1/p:1003), ~167 tries per task
[DATA] attacking service ssh on port 22

pw-inspector Usage Example
Read in a list of passwords (-i /usr/share/wordlists/nmap.lst) and save to a file (-o /root/passes.txt), selecting passwords of a minimum length of 6 (-m 6) and a maximum length of 10 (-M 10):
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 6 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hydra`

官方给出的调用示例：`hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt -t 6 ssh://192.168.1.123`

```text
root@kali:~# hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt -t 6 ssh://192.168.1.123
Hydra v7.6 (c)2013 by van Hauser/THC & David Maciejak - for legal purposes only
Hydra (http://www.thc.org/thc-hydra) starting at 2014-05-19 07:53:33
[DATA] 6 tasks, 1 server, 1003 login tries (l:1/p:1003), ~167 tries per task
[DATA] attacking service ssh on port 22
pw-inspector Usage Example
Read in a list of passwords (
-i /usr/share/wordlists/nmap.lst
) and save to a file (
-o /root/passes.txt
), selecting passwords of a minimum length of 6 (
-m 6
) and a maximum length of 10 (
-M 10
):
```

### `pw-inspector`

官方给出的调用示例：`pw-inspector -i /usr/share/wordlists/nmap.lst -o /root/passes.txt -m 6 -M 10`

```text
root@kali:~# pw-inspector -i /usr/share/wordlists/nmap.lst -o /root/passes.txt -m 6 -M 10
```

### `wc`

官方给出的调用示例：`wc -l /usr/share/wordlists/nmap.lst`

```text
root@kali:~# wc -l /usr/share/wordlists/nmap.lst
5086 /usr/share/wordlists/nmap.lst
```

### `wc（示例）`

官方给出的调用示例：`wc -l /root/passes.txt`

```text
root@kali:~# wc -l /root/passes.txt
4490 /root/passes.txt
```

### `dpl4hydra`

官方给出的调用示例：`dpl4hydra -h`

```text
root@kali:~# dpl4hydra -h
dpl4hydra v0.9.9 (c) 2012 by Roland Kessler (@rokessler)
Syntax: dpl4hydra [help] | [refresh] | [BRAND] | [all]
This script depends on a local (d)efault (p)assword (l)ist called
/root/.dpl4hydra/dpl4hydra_full.csv. If it is not available, regenerate it with
'dpl4hydra refresh'. Source of the default password list is
http://open-sez.me
Options:
  help        Help: Show this message
  refresh     Refresh list: Download the full (d)efault (p)assword (l)ist
              and generate a new local /root/.dpl4hydra/dpl4hydra_full.csv file. Takes time!
  BRAND       Generates a (d)efault (p)assword (l)ist from the local file
              /root/.dpl4hydra/dpl4hydra_full.csv, limiting the output to BRAND systems, using
              the format username:password (as required by THC hydra).
              The output file is called dpl4hydra_BRAND.lst.
  all         Dump list of all systems credentials into dpl4hydra_all.lst.
Example:
# dpl4hydra linksys
File dpl4hydra_linksys.lst was created with 20 entries.
# hydra -C ./dpl4hydra_linksys.lst -t 1 192.168.1.1 http-get /index.asp
```

### `hydra（示例）`

官方给出的调用示例：`hydra -h`

```text
root@kali:~# hydra -h
Hydra v9.7 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).
Syntax: hydra [[[-l LOGIN|-L FILE] [-p PASS|-P FILE]] | [-C FILE]] [-e nsr] [-o FILE] [-t TASKS] [-M FILE [-T TASKS]] [-w TIME] [-W TIME] [-f] [-s PORT] [-x MIN:MAX:CHARSET] [-c TIME] [-ISOuvVd46] [-m MODULE_OPT] [service://server[:PORT][/OPT]]
Options:
  -R        restore a previous aborted/crashed session
  -I        ignore an existing restore file (don't wait 10 seconds)
  -S        perform an SSL connect
  -s PORT   if the service is on a different default port, define it here
  -l LOGIN or -L FILE  login with LOGIN name, or load several logins from FILE
  -p PASS  or -P FILE  try password PASS, or load several passwords from FILE
  -x MIN:MAX:CHARSET  password bruteforce generation, type "-x -h" to get help
  -y        disable use of symbols in bruteforce, see above
  -r        use a non-random shuffling method for option -x
  -e nsr    try "n" null password, "s" login as pass and/or "r" reversed login
  -u        loop around users, not passwords (effective! implied with -x)
  -C FILE   colon separated "login:pass" format, instead of -L/-P options
  -M FILE   list of servers to attack, one entry per line, ':' to specify port
  -D XofY   Divide wordlist into Y segments and use the Xth segment.
  -o FILE   write found login/password pairs to FILE instead of stdout
  -b FORMAT specify the format for the -o FILE: text(default), json, jsonv1
  -f / -F   exit when a login/pass pair is found (-M: -f per host, -F global)
  -t TASKS  run TASKS number of connects in parallel per target (default: 16)
  -T TASKS  run TASKS connects in parallel overall (for -M, default: 64)
  -w / -W TIME  wait time for a response (32) / between connects per thread (0)
  -c TIME   wait time per login attempt over all threads (enforces -t 1)
  -4 / -6   use IPv4 (default) / IPv6 addresses (put always in [] also in -M)
  -v / -V / -d  verbose mode / show login+pass for each attempt / debug mode
  -O        use old SSL v2 and v3
  -K        do not redo failed attempts (good for -M mass scanning)
  -q        do not print messages about connection errors
  -U        service module usage details
  -m OPT    options specific for a module, see -U output for information
  -h        more command line options (COMPLETE HELP)
  server    the target: DNS, IP or 192.168.0.0/24 (this OR the -M option)
  service   the service to crack (see below for supported protocols)
  OPT       some service modules support additional input (-U for module help)
Supported services: adam6500 asterisk cisco cisco-enable cobaltstrike cvs firebird ftp[s] http[s]-{head|get|post} http[s]-{get|post}-form http-proxy http-proxy-urlenum icq imap[s] irc ldap2[s] ldap3[-{cram|digest}md5][s] memcached mongodb mssql mysql nntp oracle-listener oracle-sid pcanywhere pcnfs pop3[s] postgres radmin2 rdp redis rexec rlogin rpcap rsh rtsp s7-300 sip smb smb2 smtp[s] smtp-enum snmp socks5 ssh sshkey svn teamspeak telnet[s] vmauthd vnc xmpp
Hydra is a tool to guess/crack valid login/password pairs.
Licensed under AGPL v3.0. The newest version is always available at;
https://github.com/vanhauser-thc/thc-hydra
Please don't use in military or secret service organizations, or for illegal
purposes. (This is a wish and non-binding - most such people do not care about
laws and ethics anyway - and tell themselves they are one of the good ones.)
These services were not compiled in: afp ncp oracle sapr3.
Use HYDRA_PROXY_HTTP or HYDRA_PROXY environment variables for a proxy setup.
E.g. % export HYDRA_PROXY=socks5://l:
[email protected]
:9150 (or: socks4:// connect://)
     % export HYDRA_PROXY=connect_and_socks_proxylist.txt  (up to 64 entries)
     % export HYDRA_PROXY_HTTP=http://login:pass@proxy:8080
     % export HYDRA_PROXY_HTTP=proxylist.txt  (up to 64 entries)
Examples:
  hydra -l user -P passlist.txt ftp://192.168.0.1
  hydra -L userlist.txt -p defaultpw imap://192.168.0.1/PLAIN
  hydra -C defaults.txt -6 pop3s://[2001:db8::1]:143/TLS:DIGEST-MD5
  hydra -l admin -p password ftp://[192.168.0.0/24]/
  hydra -L logins.txt -P pws.txt -M targets.txt ssh
```

### `man`

官方给出的调用示例：`man hydra-wizard`

```text
root@kali:~# man hydra-wizard
HYDRA-WIZARD(1)             General Commands Manual             HYDRA-WIZARD(1)
NAME
     HYDRA-WIZARD - Wizard to use hydra from command line
DESCRIPTION
     This  script guide users to use hydra, with a simple wizard that will make
     the necessary questions to launch hydra from command line a fast and  eas-
     ily
     1. The wizard ask for the service to attack
     2. The target to attack
     3. The username o file with the username what use to attack
     4. The password o file with the passwords what use to attack
     5. The wizard ask if you want to test for passwords same as login, null or
     reverse login
     6. The wizard ask for the port number to attack
     Finally,  the wizard show the resume information of attack, and ask if you
     want launch attack
SEE ALSO
     hydra(1), dpl4hydra(1),
AUTHOR
     hydra-wizard was written by Shivang Desai <
[email protected]
>.
     This manual page was written by  Daniel  Echeverry  <
[email protected]
>,
     for the Debian project (and may be used by others).
                                   19/01/2014                   HYDRA-WIZARD(1)
```

### `pw-inspector（示例）`

官方给出的调用示例：`pw-inspector -h`

```text
root@kali:~# pw-inspector -h
PW-Inspector v0.2 (c) 2005 by van Hauser / THC
[email protected]
 [https://github.com/vanhauser-thc/thc-hydra]
Syntax: pw-inspector [-i FILE] [-o FILE] [-m MINLEN] [-M MAXLEN] [-c MINSETS] -l -u -n -p -s
Options:
  -i FILE    file to read passwords from (default: stdin)
  -o FILE    file to write valid passwords to (default: stdout)
  -m MINLEN  minimum length of a valid password
  -M MAXLEN  maximum length of a valid password
  -c MINSETS the minimum number of sets required (default: all given)
Sets:
  -l         lowcase characters (a,b,c,d, etc.)
  -u         upcase characters (A,B,C,D, etc.)
  -n         numbers (1,2,3,4, etc.)
  -p         printable characters (which are not -l/-u/-n, e.g. $,!,/,(,*, etc.)
  -s         special characters - all others not within the sets above
PW-Inspector reads passwords in and prints those which meet the requirements.
The return code is the number of valid passwords found, 0 if none was found.
Use for security: check passwords, if 0 is returned, reject password choice.
Use for hacking: trim your dictionary file to the pw requirements of the target.
Usage only allowed for legal purposes.
```

### `man（示例）`

官方给出的调用示例：`man xhydra`

```text
root@kali:~# man xhydra
XHYDRA(1)                   General Commands Manual                   XHYDRA(1)
NAME
     xhydra - Gtk+3 frontend for thc-hydra
SYNOPSIS
     Execute xhydra in a terminal to start the application.
DESCRIPTION
     Hydra is a parallelized login cracker which supports numerous protocols to
     attack.  New modules are easy to add, beside that, it is flexible and very
     fast.
     xhydra is the graphical fronend for the hydra(1) tool.
SEE ALSO
     hydra(1), pw-inspector(1).
AUTHOR
     hydra was written by van Hauser <
[email protected]
>
     This manual page was written by  Daniel  Echeverry  <
[email protected]
>,
     for the Debian project (and may be used by others).
                                   02/02/2012                         XHYDRA(1)
Learn more with
OffSec
Want to learn more about hydra? get access to in-depth training and hands-on labs:
PEN-200: 16. Password Attacks
Intermediate Secure Software Development II: 8. Credential Attacks for Developers
Monitoring, Intrusion Detection and Analysis Skill Path: 3.2.2. Introduction to Splunk: Detect an SSH Password Guessing Attack
Linux Admin Skill Path: 3.2.1. Linux Privilege Escalation: Inspecting User Trails
Password Attacks Skill Path
SOC Analyst Tools Skill Path: 2.2.2. Introduction to Splunk: Detect an SSH Password Guessing Attack
MITRE D3FEND - Detect: 6.1.3. Windows Server Side Attacks: Brute Force Logins
MITRE D3FEND - Harden: 10. Credential Attacks for Developers
MITRE ATT&CK - Credential Access (TA0006): 1.1. Password Attacks: Attacking Network Services Logins
PEN-200 course
Updated on: 2026-Jun-17
 Edit this page
finalrecon
kerberoast
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install hydra`，再执行 `hydra --version` 2>/dev/null || `hydra -V`
- [ ] **2.** **读官方帮助** —— `hydra -h`，需要细节时 `man hydra`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage only allowed for legal purposes.`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hydra/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[hydra](../../tools/tutorials/04-口令攻击/hydra.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hydra/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hydra/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
