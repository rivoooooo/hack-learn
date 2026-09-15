# dnsmap

> DNS domain name brute forcing tool dnsmap scans a domain for common subdomains using a built-in or an external wordlist (if specified using -w option). The internal wordlist has around 1000 words in English and Spanish as ns1, firewall ser…

> **功能分类**：信息搜集 ｜ **Kali 包**：`dnsmap` ｜ **官方文档**：<https://www.kali.org/tools/dnsmap/>

## 1. 安装

```bash
sudo apt update
sudo apt install dnsmap
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.36 |
| 架构 | any |
| 可执行命令 | `dnsmap`、`dnsmap-bulk` |
| 依赖 | `libc6` |
| 安装体积 | 259 KB |
| 官网 | <https://github.com/resurrecting-open-source-projects/dnsmap> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/dnsmap> |
| 包追踪 | <https://pkg.kali.org/pkg/dnsmap> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan example.com using a wordlist (-w /usr/share/wordlists/dnsmap.txt):
root@kali:~# dnsmap example.com -w /usr/share/wordlists/dnsmap.txt
dnsmap 0.30 - DNS Network Mapper by pagvac (gnucitizen.org)

[+] searching (sub)domains for example.com using /usr/share/wordlists/dnsmap.txt
[+] using maximum random delay of 10 millisecond(s) between requests

dnsmap-bulk Usage Example
Create a file containing domain names to scan (domains.txt) and pass it to dnsmap-bulk.sh:
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dnsmap`

官方给出的调用示例：`dnsmap example.com -w /usr/share/wordlists/dnsmap.txt`

```text
root@kali:~# dnsmap example.com -w /usr/share/wordlists/dnsmap.txt
dnsmap 0.30 - DNS Network Mapper by pagvac (gnucitizen.org)
[+] searching (sub)domains for example.com using /usr/share/wordlists/dnsmap.txt
[+] using maximum random delay of 10 millisecond(s) between requests
dnsmap-bulk Usage Example
Create a file containing domain names to scan (domains.txt) and pass it to dnsmap-bulk.sh:
```

### `echo`

官方给出的调用示例：`echo "example.com" >> domains.txt`

```text
root@kali:~# echo "example.com" >> domains.txt
```

### `echo（示例）`

官方给出的调用示例：`echo "example.org" >> domains.txt`

```text
root@kali:~# echo "example.org" >> domains.txt
```

### `dnsmap-bulk.sh`

官方给出的调用示例：`dnsmap-bulk.sh domains.txt`

```text
root@kali:~# dnsmap-bulk.sh domains.txt
dnsmap 0.30 - DNS Network Mapper by pagvac (gnucitizen.org)
[+] searching (sub)domains for example.com using built-in wordlist
[+] using maximum random delay of 10 millisecond(s) between requests
```

### `man`

官方给出的调用示例：`man dnsmap`

```text
root@kali:~# man dnsmap
dnsmap(1)      scan for subdomains using bruteforcing techniques      dnsmap(1)
NAME
     dnsmap - scan for subdomains using bruteforcing techniques
SYNOPSIS
     dnsmap <target-domain> [options]
DESCRIPTION
     dnsmap  scans a domain for common subdomains using a built-in or an exter-
     nal wordlist (if specified with -w  option).  The  internal  wordlist  has
     around  1000  words in English and Spanish as ns1, firewall, servicios and
     smtp. So will be possible search for smtp.example.com  inside  example.com
     automatically.   Results can be saved in CSV and human-readable format for
     further processing. dnsmap does NOT require root privileges to be run, and
     should NOT be run with such privileges for security reasons.
     dnsmap was originally released back in 2006 and was inspired by  the  fic-
     tional  story  "The Thief No One Saw" by Paul Craig, which can be found in
     the book "Stealing the Network - How to 0wn the Box".
     dnsmap is mainly meant to be used by  pentesters  during  the  information
     gathering/enumeration phase of infrastructure security assessments. During
     the  enumeration  stage,  the security consultant would typically discover
     the target company's IP netblocks, domain names, phone numbers, etc.
     Subdomain bruteforcing is another technique that should  be  used  in  the
     enumeration stage, as it's especially useful when other domain enumeration
     techniques  such  as zone transfers don't work (is rare to see zone trans-
     fers being publicly allowed these days by the way).
     Fun things that can happen:
            1.  Finding interesting remote access  servers  (e.g.:  https://ex-
                tranet.example.com).
            2.  Finding   badly  configured  and/or  unpatched  servers  (e.g.:
                test.example.com).
            3.  Finding new domain names which will allow you to map  non-obvi-
                ous/hard-to-find  netblocks  of  your target organization (reg-
                istry lookups - aka whois is your friend).
            4.  Sometimes you find that some bruteforced subdomains resolve  to
                internal  IP  addresses (RFC 1918).  This is great as sometimes
                they are real up-to-date "A" records which means that  it  *is*
                possible to enumerate internal servers of a target organization
                from  the Internet by only using standard DNS resolving (as op-
                posed to zone transfers for instance).
            5.  Discover embedded devices configured using Dynamic DNS services
                (e.g.: IP Cameras). This method is an  alternative  to  finding
                devices via Google hacking techniques.
OPTIONS
     -w <wordlist-file>
            Use  an  external wordlist instead of the built-in one. You can use
            programs as crunch or cupp to generate personalized wordlists.
     -r <regular-results-file>
            Save results to a plain text file. If a file name  isn't  supplied,
            dnsmap  will  create  an unique filename which includes the current
            timestamp. e.g.:  dnsmap_example_com_br_2019_11_15_214812.txt.  So,
            you can provide a directory name only, as -r /tmp.
     -c <csv-results-file>
            Save  results  in  CSV  format in a file. If a file name isn't pro-
            vided,   dnsmap   will    create    something    as    dnsmap_exam-
            ple_com_br_2019_11_15_220114.csv.  This is a similar behaviour from
            -r option.
     -d <delay-millisecs>
            Limit of random delay in milliseconds between  successive  queries.
            Delay value is a maximum random value. e.g. if you enter 1000, each
            DNS  request  will  be delayed a *maximum* of 1 second. By default,
            dnsmap uses a value of 10 milliseconds of maximum delay between DNS
            lookups. It is recommended to use the -d  (delay  in  milliseconds)
            option  in cases where dnsmap is interfering with your online expe-
            rience. i.e.: killing your bandwidth. If used, delay  must  be  be-
            tween 1 and 300000 milliseconds (5 minutes).
     -i <ips-to-ignore>
            IP  addresses to ignore in the results (useful if you get obtaining
            false positives). Use commas without spaces to separate the IP  ad-
            dresses.  The  maximum  number  of  IPs  to  filter  is 5. Example:
            203.0.113.10,198.51.199.65
INTERNAL WORDLIST
     The built-in wordlist is defined in src/dnsmap.h file. If needed, see  the
     file to know all words.
EXAMPLES
     Subdomain bruteforcing using dnsmap's built-in wordlist:
         $ dnsmap example.com
     Subdomain bruteforcing using a user-supplied wordlist:
         $ dnsmap example.com -w wordlist.txt
     Subdomain  bruteforcing using the built-in wordlist and saving the results
     to /tmp/ :
         $ dnsmap example.com -r /tmp
     Example of subdomain bruteforcing using the built-in wordlist, saving  the
     results to /tmp/, and waiting a random maximum of 300 milliseconds between
     each request:
         $ dnsmap example.com -r /tmp/ -d 300
     Subdomain  bruteforcing  with 0.8 seconds delay, saving results in regular
     and CSV format, filtering 2 user-provided IP  and  using  a  user-supplied
     wordlist:
         $ dnsmap example.com -d 800 -r /tmp/ -c /tmp/ -i 10.55.206.154,10.55.24.100 -w ./wordlist_TLAs.txt
BUGS
     Currently,  dnsmap  does  not yet support parallel scanning and hence take
     quite a long time.
     New  bugs  should  be  reported  at  https://github.com/resurrecting-open-
     source-projects/dnsmap/issues
SEE ALSO
     crunch(1), cupp(1), dnsmap-bulk(1)
AUTHOR
     dnsmap  was  originally written by "pagvac" in 2006. Currently it is main-
     tained by volunteers, inside dnsmap project, at  https://github.com/resur-
     recting-open-source-projects/dnsmap/
     This manpage was written by Joao Eriberto Mota Filho.
dnsmap-0.36                       25 Feb 2021                         dnsmap(1)
```

### `man（示例）`

官方给出的调用示例：`man dnsmap-bulk`

```text
root@kali:~# man dnsmap-bulk
dnsmap-bulk(1)               mass scan using dnsmap              dnsmap-bulk(1)
NAME
     dnsmap-bulk - mass scan using dnsmap
SYNOPSIS
     dnsmap-bulk <domains-file> [results-path]
DESCRIPTION
     dnsmap-bulk  is used to bruteforce several target domains in bulk fashion.
     In other words, is possible get a list of domains from a file to scan mul-
     tiple targets using dnsmap as backend.
     WARNING: using dnsmap-bulk, dnsmap will always use  the  default  options,
     i.e. built-in wordlist, delay = 10 ms, never ignoring IPs.
OPTIONS
     domain-file
            A file with domains to be scanned, one per line.
     results-path
            A  path where the results will be saved. dnsmap will use the -r op-
            tion to name files and will be created a file for each domain. This
            item is optional and if not supplied, dnsmap won't create files.
EXAMPLE
     For bruteforcing a list of target domains in a bulk  fashion,  saving  all
     results inside a directory:
         $ dnsmap-bulk domains.txt /tmp/results/
SEE ALSO
     dnsmap(1)
AUTHOR
     dnsmap-bulk  was  originally  written by "pagvac" in 2006. Currently it is
     maintained    by     volunteers,     inside     dnsmap     project,     at
     https://github.com/resurrecting-open-source-projects/dnsmap/
     This manpage was written by Joao Eriberto Mota Filho.
dnsmap-bulk-0.1                   18 Nov 2019                    dnsmap-bulk(1)
Updated on: 2026-May-25
 Edit this page
dirb
edb-debugger
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dnsmap`，再执行 `dnsmap --version` 2>/dev/null || `dnsmap -V`
- [ ] **2.** **读官方帮助** —— `dnsmap -h`，需要细节时 `man dnsmap`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `dnsmap -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dnsmap/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dnsmap/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dnsmap/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
