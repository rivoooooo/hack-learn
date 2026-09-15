# 按包速查：信息搜集（information-gathering）

> 共 **91** 个包 · 数据来源 <https://www.kali.org/tools/all-tools/>

返回 [工具总览](../index.md) · [全量清单](all-tools.md) · [按功能分类](../index.md#功能分类导航)

---

### 0trace

Traceroute tool that can run within an existing TCP connection The package is traceroute tool that can be run within an existing, open TCP connection, therefore bypassing some types of stateful packet filters with ease.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/0trace/> |
| 版本 | 0.01 |
| 包 / 命令 | `0trace`、`0trace.sh`、`sendprobe`、`usleep` |
| 安装 | `sudo apt install 0trace` |
| 占用空间 | 43 KB |
| 依赖 | `libc6`、`tcpdump`、`0trace.sh` |
| 官网 | <https://lcamtuf.coredump.cx> |
| 源码 | <https://gitlab.com/kalilinux/packages/0trace> |

### arping

Sends IP and/or ARP pings (to the MAC address) The arping utility sends ARP and/or ICMP requests to the specified host and displays the replies. The host may be specified by its hostname, its IP address, or its MAC address.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/arping/> |
| 版本 | 2.29 |
| 包 / 命令 | `arping` |
| 安装 | `sudo apt install arping` |
| 占用空间 | 97 KB |
| 依赖 | `libc6`、`libnet9`、`libpcap0.8t64`、`libseccomp2`、`arping` |
| 官网 | <https://www.habets.pp.se/synscan/programs.php?prog=arping> |
| 源码 | <https://salsa.debian.org/debian/arping> |

### braa

Mass SNMP scanner Braa is a mass snmp scanner. The intended usage of such a tool is of course making SNMP queries - but unlike snmpget or snmpwalk from net-snmp, it is able to query dozens or hundreds of hosts simultaneously, and in a single process. Thus, it consumes very few system resources and does the scanning VERY fast. Braa implements its OWN snmp stack, so it does NOT need any SNMP libraries

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/braa/> |
| 版本 | 0.90.1 |
| 包 / 命令 | `braa` |
| 安装 | `sudo apt install braa` |
| 占用空间 | 66 KB |
| 依赖 | `libc6`、`braa` |
| 官网 | <https://github.com/mteg/braa> |
| 源码 | <https://salsa.debian.org/pkg-security-team/braa> |

### curl

Command line tool for transferring data with URL syntax curl is a command line tool for transferring data with URL syntax, supporting DICT, FILE, FTP, FTPS, GOPHER, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMTP, SMTPS, TELNET and TFTP. curl supports SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP form based upload, proxies, cookies, user+password authentication (Basic, Digest,

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 802.11 Wi-Fi、蓝牙、数据库、检测、漏洞利用、数字取证、模糊测试、硬件攻击 等 26 个 |
| Kali 文档 | <https://www.kali.org/tools/curl/> |
| 版本 | 8.21.0 |
| 包 / 命令 | `curl`、`wcurl`、`libcurl3t64-gnutls`、`libcurl4-doc`、`libcurl4-gnutls`、`libcurl4-gnutls-dev`、`curl-config`、`libcurl4-openssl-dev`、`libcurl4t64` |
| 安装 | `sudo apt install curl` |
| 占用空间 | 512 KB |
| 依赖 | `libc6`、`libcurl4t64`、`zlib1g`、`curl` |
| 官网 | <https://curl.se/> |
| 源码 | <https://salsa.debian.org/debian/curl> |

### dirbuster

Web server directory brute-forcer DirBuster is a multi threaded java application designed to brute force directories and files names on web/application servers. Often is the case now of what looks like a web server in a state of default installation is actually not, and has pages and applications hidden within. DirBuster

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/dirbuster/> |
| 版本 | 1.0 |
| 包 / 命令 | `dirbuster` |
| 安装 | `sudo apt install dirbuster` |
| 占用空间 | 10.75 MB |
| 依赖 | `default-jre`、`dirbuster` |
| 官网 | <https://www.owasp.org/index.php/Category:OWASP_DirBuster_Project> |
| 源码 | <https://gitlab.com/kalilinux/packages/dirbuster> |

### dmitry

Deepmagic Information Gathering Tool DMitry is a UNIX/(GNU)Linux command line application written in C. DMitry can find possible subdomains, email addresses, uptime information, perform tcp port scan, whois lookups, and more.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/dmitry/> |
| 版本 | 1.3a |
| 包 / 命令 | `dmitry` |
| 安装 | `sudo apt install dmitry` |
| 占用空间 | 50 KB |
| 依赖 | `libc6`、`dmitry` |
| 官网 | <https://mor-pah.net/software/dmitry-deepmagic-information-gathering-tool/> |
| 源码 | <https://salsa.debian.org/debian/dmitry> |

### dnsenum

Tool to enumerate domain DNS information Dnsenum is a multithreaded perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks. The main purpose of Dnsenum is to gather as much information as possible about a domain. The program currently performs the following operations: Get the host’s addresses (A record).

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/dnsenum/> |
| 版本 | 1.3.2 |
| 包 / 命令 | `dnsenum` |
| 安装 | `sudo apt install dnsenum` |
| 占用空间 | 87 KB |
| 依赖 | `libhtml-parser-perl`、`libnet-dns-perl`、`libnet-ip-perl`、`libnet-netmask-perl`、`libnet-whois-ip-perl`、`libstring-random-perl`、`libwww-mechanize-perl`、`libxml-writer-perl`、`perl`、`dnsenum` |
| 官网 | <https://github.com/SparrowOchon/dnsenum2> |
| 源码 | <https://salsa.debian.org/pkg-security-team/dnsenum> |

### dnsmap

DNS domain name brute forcing tool dnsmap scans a domain for common subdomains using a built-in or an external wordlist (if specified using -w option). The internal wordlist has around 1000 words in English and Spanish as ns1, firewall servicios and smtp. So will be possible search for smtp.example.com inside example.com automatically. Results can be saved in CSV and human-readable format for further processing. dnsmap

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/dnsmap/> |
| 版本 | 0.36 |
| 包 / 命令 | `dnsmap`、`dnsmap-bulk` |
| 安装 | `sudo apt install dnsmap` |
| 占用空间 | 259 KB |
| 依赖 | `libc6`、`dnsmap` |
| 官网 | <https://github.com/resurrecting-open-source-projects/dnsmap> |
| 源码 | <https://salsa.debian.org/pkg-security-team/dnsmap> |

### dnsrecon

Powerful DNS enumeration script DNSRecon is a Python script that provides the ability to perform: Check all NS Records for Zone Transfers. Enumerate General DNS Records for a given Domain (MX, SOA, NS, A, AAAA, SPF and TXT). Perform common SRV Record Enumeration.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/dnsrecon/> |
| 版本 | 1.6.0 |
| 包 / 命令 | `dnsrecon` |
| 安装 | `sudo apt install dnsrecon` |
| 占用空间 | 1.51 MB |
| 依赖 | `python3`、`python3-dnspython`、`python3-fastapi`、`python3-httpx`、`python3-loguru`、`python3-netaddr`、`python3-slowapi`、`python3-stamina`、`dnsrecon` |
| 官网 | <https://github.com/darkoperator/dnsrecon> |
| 源码 | <https://salsa.debian.org/pkg-security-team/dnsrecon> |

### dnstracer

Trace DNS queries to the source dnstracer determines where a given Domain Name Server (DNS) gets its information from for a given hostname, and follows the chain of DNS servers back to the authoritative answer.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/dnstracer/> |
| 版本 | 1.10 |
| 包 / 命令 | `dnstracer` |
| 安装 | `sudo apt install dnstracer` |
| 占用空间 | 63 KB |
| 依赖 | `libc6`、`dnstracer` |
| 官网 | <http://www.mavetju.org/unix/dnstracer.php> |
| 源码 | <https://salsa.debian.org/creekorful/dnstracer> |

### dnswalk

Checks dns zone information using nameserver lookups dnswalk is a DNS debugger. It performs zone transfers of specified domains, and checks the database in numerous ways for internal consistency, as well as accuracy.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/dnswalk/> |
| 版本 | 2.0.2.dfsg.1 |
| 包 / 命令 | `dnswalk` |
| 安装 | `sudo apt install dnswalk` |
| 占用空间 | 46 KB |
| 依赖 | `libnet-dns-perl`、`perl`、`dnswalk` |
| 官网 | <https://github.com/davebarr/dnswalk> |
| 源码 | <https://salsa.debian.org/debian/dnswalk> |

### enum4linux

Enumerates info from Windows and Samba systems Enum4linux is a tool for enumerating information from Windows and Samba systems. It attempts to offer similar functionality to enum.exe formerly available from www.bindview.com .

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/enum4linux/> |
| 版本 | 0.9.1 |
| 包 / 命令 | `enum4linux` |
| 安装 | `sudo apt install enum4linux` |
| 占用空间 | 58 KB |
| 依赖 | `ldap-utils`、`perl`、`polenum`、`samba`、`smbclient`、`enum4linux` |
| 官网 | <https://labs.portcullis.co.uk/tools/enum4linux/> |
| 源码 | <https://gitlab.com/kalilinux/packages/enum4linux> |

### eyewitness

Rapid web application triage tool EyeWitness is designed to take screenshots of websites, provide some server header info, and identify default credentials if possible. Inspiration came from Tim Tomes’s PeepingTom Script. EyeWitness is designed to run on Kali Linux. It will auto detect the file you give it with the -f flag as either being a text file with URLs on each new

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、报告与记录、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/eyewitness/> |
| 版本 | 20230525.1 |
| 包 / 命令 | `eyewitness`、`geckodriver` |
| 安装 | `sudo apt install eyewitness` |
| 占用空间 | 5.78 MB |
| 官网 | <https://www.christophertruncer.com/eyewitness-triage-tool/> |
| 源码 | <https://gitlab.com/kalilinux/packages/eyewitness> |

### feroxbuster

Fast, simple, recursive content discovery tool written in Rust feroxbuster is a tool designed to perform Forced Browsing. Forced browsing is an attack where the aim is to enumerate and access resources that are not referenced by the web application, but are still accessible by an attacker. feroxbuster uses brute force combined with a wordlist to search

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/feroxbuster/> |
| 版本 | 2.13.1 |
| 包 / 命令 | `feroxbuster` |
| 安装 | `sudo apt install feroxbuster` |
| 占用空间 | 12.27 MB |
| 依赖 | `fonts-noto-color-emoji`、`libc6`、`libgcc-s1`、`feroxbuster` |
| 官网 | <https://github.com/epi052/feroxbuster> |
| 源码 | <https://gitlab.com/kalilinux/packages/feroxbuster> |

### fierce

Domain DNS scanner Fierce is a semi-lightweight scanner that helps locate non-contiguous IP space and hostnames against specified domains. It’s really meant as a pre-cursor to nmap, unicornscan, nessus, nikto, etc, since all of those require that you already know what IP space you are looking for. This does not perform exploitation and does not scan the whole internet

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/fierce/> |
| 版本 | 1.6.0 |
| 包 / 命令 | `fierce` |
| 安装 | `sudo apt install fierce` |
| 占用空间 | 242 KB |
| 依赖 | `python3`、`python3-dnspython`、`fierce` |
| 官网 | <https://github.com/mschwager/fierce> |
| 源码 | <https://salsa.debian.org/pkg-security-team/fierce> |

### firewalk

Active reconnaissance network security tool Firewalk is an active reconnaissance network security tool that attempts to determine what layer 4 protocols a given IP forwarding device will pass. It works by sending out TCP or UDP packets with a TTL one hop greater than the targeted gateway. If the gateway allows the traffic, it will forward the packets to the next hop where they will expire and elicit an ICMP_TIME_EXCEEDED

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/firewalk/> |
| 版本 | 5.0 |
| 包 / 命令 | `firewalk` |
| 安装 | `sudo apt install firewalk` |
| 占用空间 | 51 KB |
| 依赖 | `libc6`、`libdumbnet1`、`libnet9`、`libpcap0.8t64`、`firewalk` |
| 官网 | <http://packetfactory.openwall.net/projects/firewalk/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/firewalk> |

### fping

Sends ICMP ECHO_REQUEST packets to network hosts fping is a ping like program which uses the Internet Control Message Protocol (ICMP) echo request to determine if a target host is responding. fping differs from ping in that you can specify any number of targets on the command line, or specify a file containing the lists of targets to ping. Instead of sending to one target until it times out or replies, fping will send out a

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/fping/> |
| 版本 | 5.1 |
| 包 / 命令 | `fping`、`fping6` |
| 安装 | `sudo apt install fping` |
| 占用空间 | 93 KB |
| 依赖 | `libc6`、`libcap2-bin`、`netbase`、`fping` |
| 官网 | <https://www.fping.org/> |
| 源码 | <https://salsa.debian.org/debian/fping> |

### fragrouter

IDS evasion toolkit Fragrouter is a network intrusion detection evasion toolkit.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/fragrouter/> |
| 版本 | 1.7 |
| 包 / 命令 | `fragrouter` |
| 安装 | `sudo apt install fragrouter` |
| 占用空间 | 72 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`fragrouter` |
| 官网 | <http://www.anzen.com/research/nidsbench/fragrouter.html> |
| 源码 | <https://gitlab.com/kalilinux/packages/fragrouter> |

### freerdp3

FreeRDP proxy server FreeRDP is a libre client/server implementation of the Remote Desktop Protocol (RDP). This package contains the proxy server that can be used as man in the middle proxy for RDP connections.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、口令攻击、Top 10 常用、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/freerdp3/> |
| 版本 | 3.31.1 |
| 包 / 命令 | `freerdp-proxy`、`freerdp-proxy-modules`、`freerdp-sdl`、`sdl-freerdp`、`freerdp-shadow-x11`、`freerdp-shadow-cli`、`freerdp-wayland`、`wlfreerdp`、`freerdp-x11`、`xfreerdp`、`freerdp3-dev`、`freerdp3-proxy`、`freerdp-proxy3`、`freerdp3-proxy-modules`、`freerdp3-sdl`、`sdl-freerdp3`、`freerdp3-shadow-x11`、`freerdp-shadow-cli3`、`freerdp3-wayland`、`wlfreerdp3`、`freerdp3-x11`、`xfreerdp3`、`libfreerdp-client3-3`、`libfreerdp-server-proxy3-3`、`libfreerdp-server3-3`、`libfreerdp-shadow-subsystem3-3`、`libfreerdp-shadow3-3`、`libfreerdp3-3`、`libwinpr-tools3-3`、`libwinpr3-3`、`libwinpr3-dev`、`winpr-utils`、`winpr-hash`、`winpr-makecert`、`winpr3-utils`、`winpr-hash3`、`winpr-makecert3` |
| 安装 | `sudo apt install freerdp-proxy` |
| 占用空间 | 30 KB |
| 依赖 | `libc6`、`libfreerdp-server-proxy3-3`、`libfreerdp3-3`、`libwinpr3-3`、`freerdp-proxy` |
| 官网 | <https://www.freerdp.com/> |
| 源码 | <https://salsa.debian.org/debian-remote-team/freerdp3> |

### ftester

Tool for testing firewalls and Intrusion Detection System (IDS) The Firewall Tester (FTester) is a tool designed for testing firewall filtering policies and Intrusion Detection System (IDS) capabilities. Features: firewall testing IDS testing

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/ftester/> |
| 版本 | 1.0 |
| 包 / 命令 | `ftester`、`freport`、`ftest`、`ftestd` |
| 安装 | `sudo apt install ftester` |
| 占用空间 | 91 KB |
| 依赖 | `libnet-pcap-perl`、`libnet-rawip-perl`、`libnetpacket-perl`、`perl`、`freport` |
| 官网 | <https://dev.inversepath.com/ftester/> |
| 源码 | <https://gitlab.com/kalilinux/packages/ftester> |

### git

Fast, scalable, distributed revision control system Git is popular version control system designed to handle very large projects with speed and efficiency; it is used for many high profile open source projects, most notably the Linux kernel. Git falls in the category of distributed source code management tools. Every Git working directory is a full-fledged repository with full

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 漏洞利用、数字取证、识别与指纹、信息搜集、后渗透、报告与记录、事件响应、逆向工程 等 12 个 |
| Kali 文档 | <https://www.kali.org/tools/git/> |
| 版本 | 2.53.0 |
| 包 / 命令 | `git`、`git-receive-pack`、`git-shell`、`git-upload-archive`、`git-upload-pack`、`scalar`、`git-all`、`git-cvs`、`git-cvsserver`、`git-doc`、`git-email`、`git-gui`、`git-man`、`git-svn`、`gitk`、`gitweb` |
| 安装 | `sudo apt install git` |
| 占用空间 | 49.77 MB |
| 依赖 | `git-man`、`libc6`、`libcurl3t64-gnutls`、`liberror-perl`、`libexpat1`、`libpcre2-8-0`、`perl`、`zlib1g`、`git` |
| 官网 | <https://git-scm.com/> |
| 源码 | <https://repo.or.cz/w/git/debian.git/> |

### glibc

GNU C Library: Documentation Contains the complete GNU C Library ChangeLog. The GNU C Library Reference manual has been moved into glibc-doc-reference for licensing reasons.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 802.11 Wi-Fi、蓝牙、密码学与隐写、数据库、检测、漏洞利用、数字取证、模糊测试 等 29 个 |
| Kali 文档 | <https://www.kali.org/tools/glibc/> |
| 版本 | 2.43 |
| 包 / 命令 | `glibc-doc`、`glibc-source`、`libc-bin`、`getconf`、`getent`、`iconv`、`iconvconfig`、`ld.so`、`ldconfig`、`ldd`、`locale`、`localedef`、`pldd`、`tzselect`、`zdump`、`zic`、`libc-dev-bin`、`gencat`、`libc-devtools`、`memusage`、`memusagestat`、`mtrace`、`sotruss`、`sprof`、`libc-gconv-modules-extra`、`libc-l10n`、`libc0.3`、`libc0.3-dbg`、`libc0.3-dev`、`libc0.3-udeb`、`libc6`、`libc6-amd64`、`libc6-dbg`、`libc6-dev`、`libc6-dev-amd64`、`libc6-dev-i386`、`libc6-dev-mips32`、`libc6-dev-mips64`、`libc6-dev-mipsn32`、`libc6-dev-powerpc`、`libc6-dev-ppc64`、`libc6-dev-sparc`、`libc6-dev-sparc64`、`libc6-dev-x32`、`libc6-i386`、`libc6-mips32`、`libc6-mips64`、`libc6-mipsn32`、`libc6-powerpc`、`libc6-ppc64`、`libc6-sparc`、`libc6-sparc64`、`libc6-udeb`、`libc6-x32`、`libc6.1`、`libc6.1-dbg`、`libc6.1-dev`、`libc6.1-udeb`、`locales`、`locale-gen`、`update-locale`、`validlocale`、`locales-all`、`nscd` |
| 安装 | `sudo apt install glibc-doc` |
| 占用空间 | 3.83 MB |
| 依赖 | `libc6`、`getconf` |
| 官网 | <https://www.gnu.org/software/libc/libc.html> |
| 源码 | <https://salsa.debian.org/glibc-team/glibc> |

### hping3

Active Network Smashing Tool hping3 is a network tool able to send custom ICMP/UDP/TCP packets and to display target replies like ping does with ICMP replies. It handles fragmentation and arbitrary packet body and size, and can be used to transfer files under supported protocols. Using hping3, you can test firewall rules, perform (spoofed) port scanning, test network

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/hping3/> |
| 版本 | 3.a2.ds2 |
| 包 / 命令 | `hping3` |
| 安装 | `sudo apt install hping3` |
| 占用空间 | 255 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`libtcl8.6`、`hping3` |
| 官网 | <http://www.hping.org/> |
| 源码 | <https://salsa.debian.org/debian/hping3> |

### httpx-toolkit

Fast and multi-purpose HTTP toolkit This package contains the httpX toolkit developed by ProjectDiscovery. It’s a fast and multi-purpose HTTP toolkit allow to run multiple probers using retryablehttp library, it is designed to maintain the result reliability with increased threads. Features

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/httpx-toolkit/> |
| 版本 | 1.9.0 |
| 包 / 命令 | `httpx-toolkit` |
| 安装 | `sudo apt install httpx-toolkit` |
| 占用空间 | 54.22 MB |
| 依赖 | `libc6`、`httpx-toolkit` |
| 官网 | <https://github.com/projectdiscovery/httpx> |
| 源码 | <https://gitlab.com/kalilinux/packages/httpx-toolkit> |

### hydra

Very fast network logon cracker Hydra is a parallelized login cracker which supports numerous protocols to attack. It is very fast and flexible, and new modules are easy to add. This tool makes it possible for researchers and security consultants to show how easy it would be to gain unauthorized access to a system remotely.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、口令攻击、Top 10 常用、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/hydra/> |
| 版本 | 9.7 |
| 包 / 命令 | `hydra`、`dpl4hydra`、`hydra-wizard`、`pw-inspector`、`hydra-gtk`、`xhydra` |
| 安装 | `sudo apt install hydra` |
| 占用空间 | 978 KB |
| 依赖 | `libapr1t64`、`libbson2-2`、`libc6`、`libfbclient2`、`libfreerdp3-3`、`libgcrypt20`、`libidn12`、`libmariadb3`、`libmemcached11t64`、`libmongoc2-2`、`libpcre2-8-0`、`libpq5` 等 |
| 官网 | <https://github.com/vanhauser-thc/thc-hydra> |
| 源码 | <https://salsa.debian.org/pkg-security-team/hydra> |

### ike-scan

Discover and fingerprint IKE hosts (IPsec VPN Servers) ike-scan discovers IKE hosts and can also fingerprint them using the retransmission backoff pattern. ike-scan does two things: a) Discovery: Determine which hosts are running IKE. This is done by displaying those hosts which respond to the IKE requests

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/ike-scan/> |
| 版本 | 1.9.5 |
| 包 / 命令 | `ike-scan`、`psk-crack` |
| 安装 | `sudo apt install ike-scan` |
| 占用空间 | 4.17 MB |
| 依赖 | `libc6`、`libssl3t64`、`ike-scan` |
| 官网 | <https://github.com/royhills/ike-scan> |
| 源码 | <https://salsa.debian.org/pkg-security-team/ike-scan> |

### impacket

Python3 module to easily build and dissect network protocols Impacket is a collection of Python3 classes focused on providing access to network packets. Impacket allows Python3 developers to craft and decode network packets in simple and consistent manner. It includes support for low-level protocols such as IP, UDP and TCP, as well as higher-level protocols such as NMB and SMB.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 漏洞利用、数字取证、信息搜集、口令攻击、事件响应、社会工程、Top 10 常用、漏洞分析 等 9 个 |
| Kali 文档 | <https://www.kali.org/tools/impacket/> |
| 版本 | 0.13.0 |
| 包 / 命令 | `python3-impacket`、`impacket-netview`、`impacket-rpcdump`、`impacket-samrdump`、`impacket-secretsdump`、`impacket-wmiexec` |
| 安装 | `sudo apt install python3-impacket` |
| 占用空间 | 7.31 MB |
| 依赖 | `python3`、`python3-charset-normalizer`、`python3-flask`、`python3-ldap3`、`python3-ldapdomaindump`、`python3-openssl`、`python3-pyasn1`、`python3-pyasn1-modules`、`python3-pycryptodome`、`python3-six`、`impacket-netview` |
| 官网 | <https://github.com/SecureAuthCorp/impacket> |
| 源码 | <https://salsa.debian.org/python-team/packages/impacket> |

### impacket-scripts

Links to useful impacket scripts examples This package contains links to useful impacket scripts. It’s a separate package to keep impacket package from Debian and have the useful scripts in the path for Kali.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、事件响应、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/impacket-scripts/> |
| 版本 | 1.1 |
| 包 / 命令 | `impacket-scripts` |
| 安装 | `sudo apt install impacket-scripts` |
| 占用空间 | 65 KB |
| 依赖 | `python3-dnspython`、`python3-dsinternals`、`python3-impacket`、`python3-ldap3`、`python3-ldapdomaindump`、`python3-pcapy` |
| 源码 | <https://gitlab.com/kalilinux/packages/impacket-scripts> |

### intrace

Traceroute-like application piggybacking on existing TCP connections InTrace is a traceroute-like application that enables users to enumerate IP hops exploiting existing TCP connections, both initiated from local network (local system) or from remote hosts. It could be useful for network reconnaissance and firewall bypassing.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/intrace/> |
| 版本 | 1.6 |
| 包 / 命令 | `intrace` |
| 安装 | `sudo apt install intrace` |
| 占用空间 | 52 KB |
| 依赖 | `libc6`、`intrace` |
| 官网 | <https://github.com/robertswiecki/intrace> |
| 源码 | <https://gitlab.com/kalilinux/packages/intrace> |

### irpas

Internetwork Routing Protocol Attack Suite This package contains a collection of programs used for advanced network operations, testing, and debugging. CDP and the route injectors can be useful in a production network. Several other tools are useful for security and firewall testing. Finally some tools such as netenum are useful for general admin

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/irpas/> |
| 版本 | 0.10 |
| 包 / 命令 | `irpas`、`ass`、`cdp`、`dfkaa`、`dhcpx`、`file2cable`、`hsrp`、`icmp_redirect`、`igrp`、`inetmask`、`irdp`、`irdpresponder`、`itrace`、`netenum`、`protos`、`tctrace`、`timestamp` |
| 安装 | `sudo apt install irpas` |
| 占用空间 | 406 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`ass` |
| 官网 | <https://web.archive.org/web/20200208113522fw_/http://phenoelit.org/fr/tools.html> |
| 源码 | <https://salsa.debian.org/pkg-security-team/irpas> |

### john

Active password cracking tool John the Ripper is a tool designed to help systems administrators to find weak (easy to guess or crack through brute force) passwords, and even automatically mail users warning them about it, if it is desired. Besides several crypt(3) password hash types most commonly found on various Unix flavors, supported out of the box are Kerberos AFS and

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 漏洞利用、识别与指纹、信息搜集、口令攻击、后渗透、逆向工程、社会工程、Top 10 常用 等 10 个 |
| Kali 文档 | <https://www.kali.org/tools/john/> |
| 版本 | 1.9.0 |
| 包 / 命令 | `john` |
| 安装 | `sudo apt install john` |
| 占用空间 | 78.67 MB |
| 依赖 | `john-data`、`libc6`、`libcrypt1`、`libgmp10`、`libgomp1`、`libpcap0.8t64`、`libssl3t64`、`zlib1g` |
| 官网 | <https://github.com/openwall/john> |
| 源码 | <https://gitlab.com/kalilinux/packages/john> |

### kali-defaults

Kali default settings This package implements various default settings within Kali. The size of this package (including its dependencies) should be rather limited because it is included in all Kali images, even minimalistic ones such as container images. This package is meant to be installed during bootstrap stage, so it shouldn’t

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 数据库、漏洞利用、数字取证、识别与指纹、信息搜集、口令攻击、后渗透、报告与记录 等 14 个 |
| Kali 文档 | <https://www.kali.org/tools/kali-defaults/> |
| 版本 | 2026.3.2 |
| 包 / 命令 | `kali-defaults`、`kali-check-apt-sources`、`kali-deprecated`、`kali-motd`、`kali-service-start`、`kali-service-stop`、`kali-setup`、`kali-treecd`、`kali-winexec`、`kali-defaults-desktop` |
| 安装 | `sudo apt install kali-defaults` |
| 占用空间 | 375 KB |
| 官网 | <https://www.kali.org> |
| 源码 | <https://gitlab.com/kalilinux/packages/kali-defaults> |

### lbd

Load balancer detector Checks if a given domain uses load-balancing.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/lbd/> |
| 版本 | 0.4 |
| 包 / 命令 | `lbd` |
| 安装 | `sudo apt install lbd` |
| 占用空间 | 15 KB |
| 官网 | <http://ge.mine.nu/code/> |
| 源码 | <https://gitlab.com/kalilinux/packages/lbd> |

### legion

Semi-automated network penetration testing tool This package contains an open source, easy-to-use, super-extensible and semi-automated network penetration testing tool that aids in discovery, reconnaissance and exploitation of information systems. Legion is a fork of SECFORCE’s Sparta.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/legion/> |
| 版本 | 0.7.0 |
| 包 / 命令 | `legion` |
| 安装 | `sudo apt install legion` |
| 占用空间 | 7.51 MB |
| 依赖 | `dirbuster`、`dnsmap`、`enum4linux` |
| 官网 | <https://github.com/Hackman238/legion> |
| 源码 | <https://gitlab.com/kalilinux/packages/legion> |

### maltego

Open source intelligence and forensics application Maltego is an open source intelligence and forensics application. It will offer you timous mining and gathering of information as well as the representation of this information in a easy to understand format. This package replaces previous packages matlegoce and casefile.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 识别与指纹、信息搜集、报告与记录、社会工程、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/maltego/> |
| 版本 | 4.12.1 |
| 包 / 命令 | `maltego` |
| 安装 | `sudo apt install maltego` |
| 占用空间 | 301.19 MB |
| 依赖 | `openjdk-11-jdk-headless`、`openjdk-11-jre`、`maltego` |
| 官网 | <https://www.maltego.com> |
| 源码 | <https://gitlab.com/kalilinux/packages/maltego> |

### masscan

TCP port scanner MASSCAN is TCP port scanner which transmits SYN packets asynchronously and produces results similar to nmap, the most famous port scanner. Internally, it operates more like scanrand, unicornscan, and ZMap, using asynchronous transmission.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/masscan/> |
| 版本 | 1.3.2 |
| 包 / 命令 | `masscan` |
| 安装 | `sudo apt install masscan` |
| 占用空间 | 516 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`masscan` |
| 官网 | <https://github.com/robertdavidgraham/masscan> |
| 源码 | <https://salsa.debian.org/pkg-security-team/masscan> |

### medusa

Fast, parallel, modular, login brute-forcer for network services Medusa is intended to be a speedy, massively parallel, modular, login brute-forcer. The goal is to support as many services which allow remote authentication as possible. The author considers following items as some of the key features of this application: * Thread-based parallel testing. Brute-force testing can be

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、口令攻击、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/medusa/> |
| 版本 | 2.3 |
| 包 / 命令 | `medusa` |
| 安装 | `sudo apt install medusa` |
| 占用空间 | 843 KB |
| 依赖 | `libc6`、`libfreerdp-client3-3`、`libfreerdp3-3`、`libpq5`、`libsmb2-6`、`libssh2-1t64`、`libssl3t64`、`libsvn1`、`medusa` |
| 官网 | <http://foofus.net/?page_id=51> |
| 源码 | <https://salsa.debian.org/pkg-security-team/medusa> |

### metagoofil

Tool designed for extracting metadata of public documents Metagoofil is an information gathering tool designed for extracting metadata of public documents (pdf,doc,xls,ppt,docx,pptx,xlsx) belonging to a target company. Metagoofil will perform a search in Google to identify and download the documents to local disk.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、报告与记录 |
| Kali 文档 | <https://www.kali.org/tools/metagoofil/> |
| 版本 | 1.2.0 |
| 包 / 命令 | `metagoofil` |
| 安装 | `sudo apt install metagoofil` |
| 占用空间 | 126 KB |
| 依赖 | `python3`、`python3-googlesearch`、`python3-requests`、`metagoofil` |
| 官网 | <https://github.com/opsdisk/metagoofil> |
| 源码 | <https://gitlab.com/kalilinux/packages/metagoofil> |

### metasploit-framework

Framework for exploit development and vulnerability research The Metasploit Framework is an open source platform that supports vulnerability research, exploit development, and the creation of custom security tools.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 漏洞利用、识别与指纹、信息搜集、后渗透、逆向工程、社会工程、Top 10 常用、漏洞分析 等 9 个 |
| Kali 文档 | <https://www.kali.org/tools/metasploit-framework/> |
| 版本 | 6.5.3 |
| 包 / 命令 | `metasploit-framework`、`msf-egghunter`、`msf-exe2vba`、`msf-exe2vbs`、`msf-find_badchars`、`msf-halflm_second`、`msf-hmac_sha1_crack`、`msf-java_deserializer`、`msf-jsobfu`、`msf-makeiplist`、`msf-md5_lookup`、`msf-metasm_shell`、`msf-msf_irb_shell`、`msf-nasm_shell`、`msf-pattern_create`、`msf-pattern_offset`、`msf-pdf2xdp`、`msf-virustotal`、`msfconsole`、`msfd`、`msfdb`、`msfrpc`、`msfrpcd`、`msfupdate`、`msfvenom` |
| 安装 | `sudo apt install metasploit-framework` |
| 占用空间 | 598.76 MB |
| 依赖 | `bundler`、`curl`、`gcc-mingw-w64-i686-win32`、`gcc-mingw-w64-x86-64-win32`、`git`、`john`、`libc6`、`libffi8`、`libgcc-s1`、`liblzma5`、`libpcap0.8t64`、`libruby3.3` 等 |
| 官网 | <https://www.metasploit.com/> |
| 源码 | <https://gitlab.com/kalilinux/packages/metasploit-framework> |

### mitmproxy

SSL-capable man-in-the-middle HTTP proxy mitmproxy is an interactive man-in-the-middle proxy for HTTP and HTTPS. It provides a console interface that allows traffic flows to be inspected and edited on the fly. Also shipped is mitmdump, the command-line version of mitmproxy, with the same functionality but without the frills. Think tcpdump for

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 识别与指纹、信息搜集、嗅探与欺骗、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/mitmproxy/> |
| 版本 | 12.2.3 |
| 包 / 命令 | `mitmproxy`、`mitmdump`、`mitmweb` |
| 安装 | `sudo apt install mitmproxy` |
| 占用空间 | 4.96 MB |
| 依赖 | `dpkg`、`fonts-font-awesome`、`python3`、`python3-aioquic`、`python3-argon2`、`python3-asgiref`、`python3-bcrypt`、`python3-brotli`、`python3-certifi`、`python3-cryptography`、`python3-flask`、`python3-h11` 等 |
| 官网 | <https://mitmproxy.org> |
| 源码 | <https://gitlab.com/kalilinux/packages/mitmproxy> |

### mysql-defaults

MySQL database development files (metapackage) MySQL is a fast, stable and true multi-user, multi-threaded SQL database server. SQL (Structured Query Language) is the most popular database query language in the world. The main goals of MySQL are speed, robustness and ease of use. This package depends on the default implementation of the client development

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 漏洞利用、数字取证、信息搜集、口令攻击、事件响应、社会工程、Top 10 常用、漏洞分析 等 9 个 |
| Kali 文档 | <https://www.kali.org/tools/mysql-defaults/> |
| 版本 | 1.1.1 |
| 包 / 命令 | `default-libmysqlclient-dev`、`default-mysql-client`、`default-mysql-client-core`、`default-mysql-server`、`default-mysql-server-core`、`mysql-common` |
| 安装 | `sudo apt install default-libmysqlclient-dev` |
| 占用空间 | 10 KB |
| 依赖 | `libmariadb-dev-compat`、`default-mysql-client` |
| 源码 | <https://salsa.debian.org/mariadb-team/mysql/-/tree/mysql-defaults/debian/master> |

### nasm

General-purpose x86 assembler Netwide Assembler. NASM will currently output flat-form binary files, a.out, COFF and ELF Unix object files, and Microsoft 16-bit DOS and Win32 object files. Also included is NDISASM, a prototype x86 binary-file disassembler which uses the same instruction table as NASM.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 漏洞利用、数字取证、识别与指纹、信息搜集、后渗透、事件响应、逆向工程、社会工程 等 11 个 |
| Kali 文档 | <https://www.kali.org/tools/nasm/> |
| 版本 | 3.01 |
| 包 / 命令 | `nasm`、`ndisasm` |
| 安装 | `sudo apt install nasm` |
| 占用空间 | 3.67 MB |
| 依赖 | `libc6`、`nasm` |
| 官网 | <https://www.nasm.us/> |
| 源码 | <https://salsa.debian.org/debian/nasm> |

### nbtscan

Scan networks searching for NetBIOS information NBTscan is a program for scanning IP networks for NetBIOS name information. It sends NetBIOS status query to each address in supplied range and lists received information in human readable form. For each responded host it lists IP address, NetBIOS computer name, logged-in user name and MAC address (such as Ethernet).

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/nbtscan/> |
| 版本 | 1.7.2 |
| 包 / 命令 | `nbtscan` |
| 安装 | `sudo apt install nbtscan` |
| 占用空间 | 57 KB |
| 依赖 | `libc6`、`nbtscan` |
| 官网 | <https://github.com/resurrecting-open-source-projects/nbtscan> |
| 源码 | <https://salsa.debian.org/pkg-security-team/nbtscan> |

### net-snmp

SNMP (Simple Network Management Protocol) trap library The Simple Network Management Protocol (SNMP) provides a framework for the exchange of management information between agents (servers) and clients. The Net-SNMP trap library contains functions for receiving SNMP trap and inform messages.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、防护、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/net-snmp/> |
| 版本 | 5.9.5.2 |
| 包 / 命令 | `libnetsnmptrapd45`、`libsnmp-base`、`libsnmp-dev`、`mib2c`、`mib2c-update`、`net-snmp-config`、`libsnmp-perl`、`libsnmp45`、`snmp`、`agentxtrap`、`encode_keychange`、`fixproc`、`snmp-bridge-mib`、`snmpbulkget`、`snmpbulkwalk`、`snmpcheck`、`snmpconf`、`snmpdelta`、`snmpdf`、`snmpget`、`snmpgetnext`、`snmpinform`、`snmpnetstat`、`snmpping`、`snmpps`、`snmpset`、`snmpstatus`、`snmptable`、`snmptest`、`snmptls`、`snmptranslate`、`snmptrap`、`snmpusm`、`snmpvacm`、`snmpwalk`、`snmpd`、`net-snmp-create-v3-user`、`snmptrapd`、`traptoemail`、`tkmib` |
| 安装 | `sudo apt install libnetsnmptrapd45` |
| 占用空间 | 74 KB |
| 依赖 | `libc6`、`libmariadb3`、`libsnmp-base`、`libsnmp45`、`libsnmp-base` |
| 官网 | <https://net-snmp.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/debian/net-snmp> |

### netbase

Basic TCP/IP networking system This package provides the necessary infrastructure for basic TCP/IP based networking. In particular, it supplies common name-to-number mappings in /etc/services, /etc/rpc, /etc/protocols and /etc/ethertypes.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 802.11 Wi-Fi、蓝牙、数据库、漏洞利用、数字取证、模糊测试、硬件攻击、识别与指纹 等 25 个 |
| Kali 文档 | <https://www.kali.org/tools/netbase/> |
| 版本 | 6.5 |
| 包 / 命令 | `netbase` |
| 安装 | `sudo apt install netbase` |
| 占用空间 | 35 KB |
| 源码 | <https://salsa.debian.org/md/netbase> |

### netcat

TCP/IP swiss army knife A simple Unix utility which reads and writes data across network connections using TCP or UDP protocol. It is designed to be a reliable “back-end” tool that can be used directly or easily driven by other programs and scripts. At the same time it is a feature-rich network debugging and exploration tool, since it can create almost any kind

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/netcat/> |
| 版本 | 1.10 |
| 包 / 命令 | `netcat-traditional`、`nc.traditional` |
| 安装 | `sudo apt install netcat-traditional` |
| 占用空间 | 139 KB |
| 依赖 | `libc6`、`nc.traditional` |
| 官网 | <http://www.stearns.org/nc/> |
| 源码 | <https://salsa.debian.org/debian/netcat> |

### netdiscover

Active/passive network address scanner using ARP requests Netdiscover is an active/passive address reconnaissance tool, mainly developed for those wireless networks without dhcp server, when you are wardriving. It can be also used on hub/switched networks. Built on top of libnet and libpcap, it can passively detect online hosts, or search for them, by actively sending ARP requests.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/netdiscover/> |
| 版本 | 0.21 |
| 包 / 命令 | `netdiscover` |
| 安装 | `sudo apt install netdiscover` |
| 占用空间 | 3.08 MB |
| 依赖 | `libc6`、`libpcap0.8t64`、`netdiscover` |
| 官网 | <https://github.com/netdiscover-scanner/netdiscover> |
| 源码 | <https://salsa.debian.org/debian/netdiscover> |

### netmask

Helps determine network masks This is a tiny program handy if you work with firewalls or routers occasionally (possibly using this as a helper for shell scripts). It can determine the smallest set of network masks to specify a range of hosts. It can also convert between common IP netmask and address formats.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/netmask/> |
| 版本 | 2.5.0 |
| 包 / 命令 | `netmask` |
| 安装 | `sudo apt install netmask` |
| 占用空间 | 74 KB |
| 依赖 | `libc6`、`netmask` |
| 官网 | <https://github.com/tlby/netmask> |
| 源码 | <https://salsa.debian.org/debian/netmask> |

### nfs-utils

Header files and docs for libnfsidmap Contains the header files and documentation for libnfsidmap for use in developing applications that use the libnfsidmap library. libnfsidmap provides functions to map between NFSv4 names (which are of the form user@domain) and local uid’s and gid’s.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/nfs-utils/> |
| 版本 | 2.9.2 |
| 包 / 命令 | `libnfsidmap-dev`、`libnfsidmap1`、`nfs-common`、`mount.nfs`、`mount.nfs4`、`mountstats`、`nfsconf`、`nfsidmap`、`nfsiostat`、`nfsstat`、`rpc.gssd`、`rpc.idmapd`、`rpc.statd`、`rpc.svcgssd`、`rpcctl`、`rpcdebug`、`showmount`、`sm-notify`、`start-statd`、`umount.nfs`、`umount.nfs4`、`nfs-kernel-server`、`exportfs`、`fsidd`、`nfsdcld`、`nfsdclddb`、`nfsdclnts`、`nfsdctl`、`nfsref`、`rpc.mountd`、`rpc.nfsd` |
| 安装 | `sudo apt install libnfsidmap-dev` |
| 占用空间 | 110 KB |
| 依赖 | `libnfsidmap1`、`libnfsidmap1` |
| 官网 | <https://linux-nfs.org/> |
| 源码 | <https://salsa.debian.org/kernel-team/nfs-utils> |

### nikto

Web server security scanner Nikto is a pluggable web server and CGI scanner written in Perl, using rfp’s LibWhisker to perform fast security or informational checks. Features: Easily updatable CSV-format checks database Output reports in plain text or HTML

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/nikto/> |
| 版本 | 2.6.1 |
| 包 / 命令 | `nikto`、`replay` |
| 安装 | `sudo apt install nikto` |
| 占用空间 | 2.15 MB |
| 依赖 | `libdigest-perl-md5-perl`、`libio-socket-ssl-perl`、`libjson-perl`、`libjson-pp-perl`、`libnet-ssleay-perl`、`libwhisker2-perl`、`libxml-libxml-perl`、`libxml-writer-perl`、`perl`、`nikto` |
| 官网 | <https://github.com/sullo/nikto> |
| 源码 | <https://gitlab.com/kalilinux/packages/nikto> |

### nmap

The Network Mapper Nmap is a utility for network exploration or security auditing. It supports ping scanning (determine which hosts are up), many port scanning techniques, version detection (determine service protocols and application versions listening behind ports), and TCP/IP fingerprinting (remote host OS or device identification). Nmap also

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 漏洞利用、识别与指纹、信息搜集、后渗透、逆向工程、社会工程、Top 10 常用、VoIP 等 10 个 |
| Kali 文档 | <https://www.kali.org/tools/nmap/> |
| 版本 | 7.99 |
| 包 / 命令 | `ncat`、`ndiff`、`nmap`、`nping`、`nmap-common`、`zenmap` |
| 安装 | `sudo apt install nmap` |
| 占用空间 | 4.70 MB |
| 依赖 | `libc6`、`libgcc-s1`、`liblinear4`、`liblua5.4-0`、`libpcap0.8t64`、`libpcre2-8-0`、`libssh2-1t64`、`libssl3t64`、`libstdc++6`、`nmap-common`、`zlib1g`、`nmap` |
| 官网 | <https://nmap.org/> |
| 源码 | <https://gitlab.com/kalilinux/packages/nmap> |

### nuclei

Fast and customizable vulnerability scanner based on simple YAML based DSL This package contains a fast tool for configurable targeted scanning based on templates offering massive extensibility and ease of use. Nuclei is used to send requests across targets based on a template leading to zero false positives and providing fast scanning on large number of hosts. Nuclei offers scanning for a variety of protocols

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/nuclei/> |
| 版本 | 3.11.1 |
| 包 / 命令 | `nuclei` |
| 安装 | `sudo apt install nuclei` |
| 占用空间 | 136.31 MB |
| 官网 | <https://github.com/projectdiscovery/nuclei> |
| 源码 | <https://gitlab.com/kalilinux/packages/nuclei> |

### onesixtyone

Fast and simple SNMP scanner onesixtyone is a simple SNMP scanner which sends SNMP requests for the sysDescr value asynchronously with user-adjustable sending times and then logs the responses which gives the description of the software running on the device. Running onesixtyone on a class B network (switched 100Mbs with 1Gbs

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/onesixtyone/> |
| 版本 | 0.3.4 |
| 包 / 命令 | `onesixtyone` |
| 安装 | `sudo apt install onesixtyone` |
| 占用空间 | 177 KB |
| 依赖 | `libc6`、`onesixtyone` |
| 官网 | <https://github.com/trailofbits/onesixtyone> |
| 源码 | <https://salsa.debian.org/pkg-security-team/onesixtyone> |

### openssl

Secure Sockets Layer toolkit - cryptographic utility This package is part of the OpenSSL project’s implementation of the SSL and TLS cryptographic protocols for secure communication over the Internet. It contains the general-purpose command line binary /usr/bin/openssl, useful for cryptographic operations such as:

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 802.11 Wi-Fi、蓝牙、密码学与隐写、数据库、检测、漏洞利用、数字取证、模糊测试 等 28 个 |
| Kali 文档 | <https://www.kali.org/tools/openssl/> |
| 版本 | 3.6.3 |
| 包 / 命令 | `libcrypto3-udeb`、`libssl-dev`、`libssl-doc`、`libssl3-udeb`、`libssl3t64`、`openssl`、`openssl-provider-fips`、`openssl-provider-legacy` |
| 安装 | `sudo apt install openssl` |
| 占用空间 | 2.47 MB |
| 依赖 | `libc6`、`libssl3t64`、`openssl` |
| 官网 | <https://openssl-library.org> |
| 源码 | <https://salsa.debian.org/debian/openssl> |

### p0f

Passive OS fingerprinting tool p0f performs passive OS detection based on SYN packets. Unlike nmap and queso, p0f does recognition without sending any data. Additionally, it is able to determine the distance to the remote host, and can be used to determine the structure of a foreign or local network. When running on the gateway of a network it is able

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/p0f/> |
| 版本 | 3.09b |
| 包 / 命令 | `p0f` |
| 安装 | `sudo apt install p0f` |
| 占用空间 | 218 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`p0f` |
| 官网 | <https://lcamtuf.coredump.cx/p0f3/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/p0f> |

### polenum

Extracts the password policy from a Windows system polenum is a Python script which uses the Impacket Library from CORE Security Technologies to extract the password policy information from a windows machine. This allows a non-windows (Linux, Mac OSX, BSD etc..) user to query the password policy of a remote windows box without the need to have access to a windows machine.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 数字取证、信息搜集、口令攻击、事件响应、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/polenum/> |
| 版本 | 1.7 |
| 包 / 命令 | `polenum` |
| 安装 | `sudo apt install polenum` |
| 占用空间 | 26 KB |
| 依赖 | `python3`、`python3-impacket`、`polenum` |
| 官网 | <https://github.com/Wh1t3Fox/polenum/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/polenum> |

### procps

/proc file system utilities This package provides command line and full screen utilities for browsing procfs, a “pseudo” file system dynamically generated by the kernel to provide information about the status of entries in its process table (such as whether the process is running, stopped, or a “zombie”). It contains free, kill, pkill, pgrep, pmap, ps, pwdx, skill, slabtop,

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 802.11 Wi-Fi、密码学与隐写、数据库、漏洞利用、数字取证、模糊测试、识别与指纹、信息搜集 等 23 个 |
| Kali 文档 | <https://www.kali.org/tools/procps/> |
| 版本 | 4.0.6 |
| 包 / 命令 | `libproc2-1`、`libproc2-dev`、`procps`、`free`、`hugetop`、`kill`、`pgrep`、`pidwait`、`pkill`、`pmap`、`ps`、`pwdx`、`skill`、`slabtop`、`snice`、`sysctl`、`tload`、`top`、`uptime`、`vmstat`、`w`、`watch` |
| 安装 | `sudo apt install procps` |
| 占用空间 | 2.60 MB |
| 依赖 | `libc6`、`libncursesw6`、`libproc2-1`、`libsystemd0`、`libtinfo6`、`free` |
| 官网 | <https://gitlab.com/procps-ng/procps> |
| 源码 | <https://salsa.debian.org/debian/procps> |

### python-ldapdomaindump

Active Directory information dumper via LDAP (Python 3) This package contains an Active Directory information dumper via LDAP. In an Active Directory domain, a lot of interesting information can be retrieved via LDAP by any authenticated user (or machine). This makes LDAP an interesting protocol for gathering information in the recon phase of a pentest of an internal network. A problem is that data from LDAP often is not available in

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 漏洞利用、数字取证、信息搜集、口令攻击、事件响应、社会工程、Top 10 常用、漏洞分析 等 9 个 |
| Kali 文档 | <https://www.kali.org/tools/python-ldapdomaindump/> |
| 版本 | 0.9.4 |
| 包 / 命令 | `python3-ldapdomaindump`、`ldapdomaindump`、`ldd2bloodhound`、`ldd2pretty` |
| 安装 | `sudo apt install python3-ldapdomaindump` |
| 占用空间 | 84 KB |
| 依赖 | `python3`、`python3-dnspython`、`python3-ldap3`、`ldapdomaindump` |
| 官网 | <https://github.com/dirkjanm/ldapdomaindump> |
| 源码 | <https://salsa.debian.org/python-team/packages/python-ldapdomaindump> |

### qsslcaudit

Test SSL/TLS clients how secure they are This tool can be used to determine if an application that uses TLS/SSL for its data transfers does this in a secure way.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/qsslcaudit/> |
| 版本 | 0.8.3 |
| 包 / 命令 | `qsslcaudit` |
| 安装 | `sudo apt install qsslcaudit` |
| 占用空间 | 1.11 MB |
| 依赖 | `libc6`、`libcrypto++8t64`、`libgcc-s1`、`libgnutls30t64`、`libqt5core5t64`、`libqt5network5t64`、`libstdc++6`、`libunsafessl1.0.2`、`qsslcaudit` |
| 官网 | <https://github.com/gremwell/qsslcaudit> |
| 源码 | <https://gitlab.com/kalilinux/packages/qsslcaudit> |

### rake

Ruby make-like utility Rake is a simple ruby build program with capabilities similar to make. Rake has the following features: Rakefiles (rakes version of Makefiles) are completely defined in standard Ruby syntax. No XML files to edit. No quirky Makefile syntax to worry about (is that a tab or a space?)

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 蓝牙、漏洞利用、识别与指纹、信息搜集、口令攻击、后渗透、报告与记录、逆向工程 等 13 个 |
| Kali 文档 | <https://www.kali.org/tools/rake/> |
| 版本 | 13.4.2 |
| 包 / 命令 | `rake` |
| 安装 | `sudo apt install rake` |
| 占用空间 | 208 KB |
| 依赖 | `ruby`、`rake` |
| 官网 | <https://github.com/ruby/rake> |
| 源码 | <https://salsa.debian.org/ruby-team/rake> |

### rdesktop

RDP client for Windows NT/2000 Terminal Server and Windows Servers rdesktop is an open source client for Windows NT/2000 Terminal Server and Windows Server 2003/2008. Capable of natively speaking its Remote Desktop Protocol (RDP) in order to present the user’s Windows desktop. Unlike Citrix ICA, no server extensions are required. Rdesktop is in need of a new upstream maintainter. Please see the home page

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/rdesktop/> |
| 版本 | 1.9.0 |
| 包 / 命令 | `rdesktop` |
| 安装 | `sudo apt install rdesktop` |
| 占用空间 | 692 KB |
| 依赖 | `libasound2t64`、`libc6`、`libgmp10`、`libgnutls30t64`、`libgssapi-krb5-2`、`libhogweed6t64`、`libnettle8t64`、`libpcsclite1`、`libtasn1-6`、`libx11-6`、`libxcursor1`、`libxrandr2` 等 |
| 官网 | <https://www.rdesktop.org/> |
| 源码 | <https://salsa.debian.org/debian/rdesktop> |

### recon-ng

Web Reconnaissance framework written in Python Recon-ng is a full-featured Web Reconnaissance framework written in Python. Complete with independent modules, database interaction, built in convenience functions, interactive help, and command completion, Recon-ng provides a powerful environment in which open source web-based reconnaissance can be conducted quickly and thoroughly.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/recon-ng/> |
| 版本 | 5.1.2 |
| 包 / 命令 | `recon-ng`、`recon-cli`、`recon-web` |
| 安装 | `sudo apt install recon-ng` |
| 占用空间 | 271 KB |
| 依赖 | `libjs-jquery`、`libjs-skeleton`、`node-normalize.css`、`python3`、`python3-dicttoxml`、`python3-dnspython`、`python3-flasgger`、`python3-flask`、`python3-flask-restful`、`python3-lxml`、`python3-mechanize`、`python3-redis` 等 |
| 官网 | <https://github.com/lanmaster53/recon-ng> |
| 源码 | <https://salsa.debian.org/pkg-security-team/recon-ng> |

### requests

Elegant and simple HTTP library for Python (Documentation) Requests allow you to send HTTP/1.1 requests. You can add headers, form data, multipart files, and parameters with simple Python dictionaries, and access the response data in the same way. It’s powered by httplib and urllib3, but it does all the hard work and crazy hacks for you. Features

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 漏洞利用、数字取证、识别与指纹、信息搜集、报告与记录、事件响应、软件定义无线电、社会工程 等 12 个 |
| Kali 文档 | <https://www.kali.org/tools/requests/> |
| 版本 | 2.32.5 |
| 包 / 命令 | `python-requests-doc`、`python3-requests` |
| 安装 | `sudo apt install python-requests-doc` |
| 占用空间 | 1.50 MB |
| 依赖 | `libjs-sphinxdoc`、`python3-requests` |
| 官网 | <https://requests.readthedocs.io/> |
| 源码 | <https://salsa.debian.org/python-team/packages/requests> |

### samba

SMB/CIFS file, print, and login server for Unix Samba is an implementation of the SMB/CIFS protocol for Unix systems, providing support for cross-platform file and printer sharing with Microsoft Windows, OS X, and other Unix systems. Samba can also function as an Active Directory or NT4-style domain controller, and can integrate with Active Directory realms or NT4 domains as a member server.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 802.11 Wi-Fi、检测、数字取证、信息搜集、口令攻击、事件响应、Top 10 常用、漏洞分析 等 10 个 |
| Kali 文档 | <https://www.kali.org/tools/samba/> |
| 版本 | 4.24.6 |
| 包 / 命令 | `ctdb`、`ctdb_diagnostics`、`ctdbd`、`ltdbtool`、`onnode`、`ping_pong`、`ldb-tools`、`ldbadd`、`ldbdel`、`ldbedit`、`ldbmodify`、`ldbrename`、`ldbsearch`、`libldb-dev`、`libldb2`、`libnss-winbind`、`libpam-winbind`、`libsmbclient`、`libsmbclient-dev`、`libsmbclient0`、`libtalloc-dev`、`libtalloc2`、`libtdb-dev`、`libtdb1`、`libtevent-dev`、`libtevent0`、`libtevent0t64`、`libwbclient-dev`、`libwbclient0`、`python3-ldb`、`python3-samba`、`samba-gpupdate`、`samba-tool`、`python3-talloc`、`python3-tdb`、`registry-tools`、`regdiff`、`regpatch`、`regshell`、`regtree`、`samba`、`eventlogadm`、`mvxattr`、`nmbd` |
| 安装 | `sudo apt install samba` |
| 占用空间 | 5.01 MB |
| 依赖 | `libbsd0`、`libc6`、`libcups2t64`、`libdbus-1-3`、`libgnutls30t64`、`libldap2`、`libldb2`、`libndr6`、`libpopt0`、`libtalloc2`、`libtdb1`、`libtevent0t64` 等 |
| 官网 | <https://www.samba.org> |
| 源码 | <https://salsa.debian.org/samba-team/samba> |

### scapy

Interactive packet manipulation tool root@kali:~# scapy -h Usage: scapy.py [-c new_startup_file] [-p new_prestart_file] [-C] [-P] [-H] Args: -H: header-less start -C: do not read startup file

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 802.11 Wi-Fi、信息搜集、口令攻击、嗅探与欺骗、VoIP、漏洞分析、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/scapy/> |
| 版本 | 2.7.0 |
| 包 / 命令 | `python3-scapy`、`scapy`、`scapy3` |
| 安装 | `sudo apt install scapy` |
| 官网 | <https://scapy.net/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/scapy> |

### smbmap

Handy SMB enumeration tool SMBMap allows users to enumerate samba share drives across an entire domain. List share drives, drive permissions, share contents, upload/download functionality, file name auto-download pattern matching, and even execute remote commands. This tool was designed with pen testing in mind, and is intended to simplify searching for potentially sensitive data across large

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/smbmap/> |
| 版本 | 1.10.7 |
| 包 / 命令 | `smbmap` |
| 安装 | `sudo apt install smbmap` |
| 占用空间 | 134 KB |
| 依赖 | `python3`、`python3-impacket`、`python3-pyasn1`、`python3-termcolor`、`smbmap` |
| 官网 | <https://github.com/ShawnDEvans/smbmap> |
| 源码 | <https://salsa.debian.org/pkg-security-team/smbmap> |

### smtp-user-enum

Username guessing tool for the SMTP service Username guessing tool primarily for use against the default Solaris SMTP service. Can use either EXPN, VRFY or RCPT TO.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/smtp-user-enum/> |
| 版本 | 1.2 |
| 包 / 命令 | `smtp-user-enum` |
| 安装 | `sudo apt install smtp-user-enum` |
| 占用空间 | 98 KB |
| 依赖 | `libio-socket-ip-perl`、`libsocket-perl`、`perl`、`smtp-user-enum` |
| 官网 | <http://pentestmonkey.net/tools/user-enumeration/smtp-user-enum> |
| 源码 | <https://gitlab.com/kalilinux/packages/smtp-user-enum> |

### snmpcheck

SNMP service enumeration tool Like to snmpwalk, snmpcheck allows you to enumerate the SNMP devices and places the output in a very human readable friendly format. It could be useful for penetration testing or systems monitoring.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/snmpcheck/> |
| 版本 | 1.9 |
| 包 / 命令 | `snmpcheck`、`snmp-check` |
| 安装 | `sudo apt install snmpcheck` |
| 占用空间 | 46 KB |
| 依赖 | `libnet-snmp-perl`、`libnumber-bytes-human-perl`、`perl`、`ruby`、`ruby-snmp`、`snmp-check` |
| 官网 | <http://www.nothink.org/codes/snmpcheck/index.php> |
| 源码 | <https://gitlab.com/kalilinux/packages/snmpcheck> |

### sqlmap

Automatic SQL injection tool sqlmap goal is to detect and take advantage of SQL injection vulnerabilities in web applications. Once it detects one or more SQL injections on the target host, the user can choose among a variety of options to perform an extensive back-end database management system fingerprint, retrieve DBMS session user and database, enumerate users,

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 数据库、漏洞利用、信息搜集、Top 10 常用、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/sqlmap/> |
| 版本 | 1.10.8 |
| 包 / 命令 | `sqlmap`、`sqlmapapi` |
| 安装 | `sudo apt install sqlmap` |
| 占用空间 | 12.69 MB |
| 依赖 | `python3`、`python3-magic`、`sqlmap` |
| 官网 | <https://sqlmap.org/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/sqlmap> |

### ssldump

SSLv3/TLS network protocol analyzer This program will dump the traffic on a network and analyze it for SSLv3/TLS network traffic, typically used to secure TCP connections. When it identifies this traffic, it decodes the results. When provided with the appropriate keying material, it will also decrypt the connections and display the application data traffic.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/ssldump/> |
| 版本 | 1.9 |
| 包 / 命令 | `ssldump` |
| 安装 | `sudo apt install ssldump` |
| 占用空间 | 193 KB |
| 依赖 | `libc6`、`libjson-c5`、`libnet9`、`libpcap0.8t64`、`libssl3t64`、`ssldump` |
| 官网 | <https://github.com/adulau/ssldump> |
| 源码 | <https://salsa.debian.org/pkg-security-team/ssldump> |

### sslh

Applicative protocol multiplexer sslh lets one accept HTTPS, SSH, OpenVPN, tinc and XMPP connections on the same port. This makes it possible to connect to any of these servers on port 443 (e.g. from inside a corporate firewall, which almost never block port 443) while still serving HTTPS on that port.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、后渗透、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/sslh/> |
| 版本 | 2.3.1 |
| 包 / 命令 | `sslh`、`sslh-ev`、`sslh-select` |
| 安装 | `sudo apt install sslh` |
| 占用空间 | 844 KB |
| 依赖 | `adduser` |
| 官网 | <http://www.rutschle.net/tech/sslh/README.html> |
| 源码 | <https://salsa.debian.org/debian/sslh.git> |

### sslscan

Tests SSL/TLS enabled services to discover supported cipher suites This tool allow queries SSL/TLS services (such as HTTPS) and reports the protocol versions, cipher suites, key exchanges, signature algorithms, and certificates in use. This helps the user understand which parameters are weak from a security standpoint. sslscan can also output results into an XML file for easy consumption by

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/sslscan/> |
| 版本 | 2.1.5 |
| 包 / 命令 | `sslscan` |
| 安装 | `sudo apt install sslscan` |
| 占用空间 | 178 KB |
| 依赖 | `libc6`、`libssl3t64`、`sslscan` |
| 官网 | <https://github.com/rbsec/sslscan> |
| 源码 | <https://salsa.debian.org/debian/sslscan> |

### sslyze

Fast and full-featured SSL scanner SSLyze is a Python tool that can analyze the SSL configuration of a server by connecting to it. It is designed to be fast and comprehensive, and should help organizations and testers identify misconfigurations affecting their SSL servers.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/sslyze/> |
| 版本 | 6.3.1 |
| 包 / 命令 | `sslyze` |
| 安装 | `sudo apt install sslyze` |
| 占用空间 | 2.19 MB |
| 依赖 | `libjs-sphinxdoc`、`python3`、`python3-cryptography`、`python3-nassl`、`python3-pkg-resources`、`python3-pydantic`、`python3-tls-parser`、`python3-typing-extensions`、`sslyze` |
| 官网 | <https://github.com/nabla-c0d3/sslyze> |
| 源码 | <https://gitlab.com/kalilinux/packages/sslyze> |

### subversion

Advanced version control system Apache Subversion, also known as svn, is a centralised version control system. Version control systems allow many individuals (who may be distributed geographically) to collaborate on a set of files (source code, websites, etc). Subversion began with a CVS paradigm and supports all the major features of CVS, but has evolved to support

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 802.11 Wi-Fi、信息搜集、口令攻击、Top 10 常用、漏洞分析、Web 应用、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/subversion/> |
| 版本 | 1.14.5 |
| 包 / 命令 | `libapache2-mod-svn`、`libsvn-dev`、`libsvn-doc`、`libsvn-java`、`libsvn-perl`、`libsvn1`、`python3-subversion`、`ruby-svn`、`subversion`、`svn`、`svnadmin`、`svnauthz`、`svnauthz-validate`、`svnbench`、`svndumpfilter`、`svnfsfs`、`svnlook`、`svnmucc`、`svnrdump`、`svnserve`、`svnsync`、`svnversion`、`subversion-tools`、`fsfs-access-map`、`fsfs-stats`、`svn-backup-dumps`、`svn-bisect`、`svn-clean`、`svn-hot-backup`、`svn-mergeinfo-normalizer`、`svn-populate-node-origins-index`、`svn-vendor`、`svn_apply_autoprops`、`svn_load_dirs`、`svnraisetreeconflict`、`svnwrap` |
| 安装 | `sudo apt install subversion` |
| 占用空间 | 4.73 MB |
| 依赖 | `libapr1t64`、`libaprutil1t64`、`libc6`、`libsvn1`、`svn` |
| 官网 | <http://subversion.apache.org/> |
| 源码 | <https://salsa.debian.org/jamessan/subversion> |

### sudo

Provide limited super user privileges to specific users Sudo is a program designed to allow a sysadmin to give limited root privileges to users and log root activity. The basic philosophy is to give as few privileges as possible but still allow people to get their work done.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 识别与指纹、信息搜集、口令攻击、后渗透、报告与记录、社会工程、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/sudo/> |
| 版本 | 1.9.17p2 |
| 包 / 命令 | `libnss-sudo`、`sudo`、`cvtsudoers`、`sudo_logsrvd`、`sudo_sendlog`、`sudoedit`、`sudoreplay`、`visudo`、`sudo-ldap` |
| 安装 | `sudo apt install sudo` |
| 占用空间 | 6.61 MB |
| 依赖 | `libapparmor1`、`libaudit1`、`libc6`、`libpam-modules`、`libpam0g`、`libselinux1`、`libssl3t64` |
| 官网 | <https://www.sudo.ws/> |
| 源码 | <https://salsa.debian.org/sudo-team/sudo> |

### swaks

SMTP command-line test tool swaks (Swiss Army Knife SMTP) is a command-line tool written in Perl for testing SMTP setups; it supports STARTTLS and SMTP AUTH (PLAIN, LOGIN, CRAM-MD5, SPA, and DIGEST-MD5). swaks allows one to stop the SMTP dialog at any stage, e.g to check RCPT TO: without actually sending a mail.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/swaks/> |
| 版本 | 20240103.0 |
| 包 / 命令 | `swaks` |
| 安装 | `sudo apt install swaks` |
| 占用空间 | 312 KB |
| 依赖 | `perl`、`swaks` |
| 官网 | <https://www.jetmore.org/john/code/swaks/> |
| 源码 | <https://salsa.debian.org/debian/swaks> |

### tcpdump

Command-line network traffic analyzer This program allows you to dump the traffic on a network. tcpdump is able to examine IPv4, ICMPv4, IPv6, ICMPv6, UDP, TCP, SNMP, AFS BGP, RIP, PIM, DVMRP, IGMP, SMB, OSPF, NFS and many other packet types. It can be used to print out the headers of packets on a network

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 数字取证、信息搜集、事件响应、嗅探与欺骗 |
| Kali 文档 | <https://www.kali.org/tools/tcpdump/> |
| 版本 | 4.99.6 |
| 包 / 命令 | `tcpdump` |
| 安装 | `sudo apt install tcpdump` |
| 占用空间 | 1.31 MB |
| 依赖 | `libc6`、`libpcap0.8t64`、`libssl3t64` |
| 官网 | <https://www.tcpdump.org/> |
| 源码 | <https://salsa.debian.org/debian/tcpdump> |

### thc-ipv6

The Hacker Choice’s IPv6 Attack Toolkit Attack toolkit for testing IPv6 and ICMPv6 protocol weaknesses. Some of the tools included: alive6: an effective alive scanning. denial6: try a collection of denial-of-service tests against a target.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/thc-ipv6/> |
| 版本 | 3.8 |
| 包 / 命令 | `thc-ipv6`、`atk6-address6`、`atk6-alive6`、`atk6-connect6`、`atk6-connsplit6`、`atk6-covert_send6`、`atk6-covert_send6d`、`atk6-denial6`、`atk6-detect-new-ip6`、`atk6-detect_sniffer6`、`atk6-dnsdict6`、`atk6-dnsrevenum6`、`atk6-dnssecwalk`、`atk6-dos-new-ip6`、`atk6-dump_dhcp6`、`atk6-dump_router6`、`atk6-exploit6`、`atk6-extract_hosts6`、`atk6-extract_networks6`、`atk6-fake_advertise6`、`atk6-fake_dhcps6`、`atk6-fake_dns6d`、`atk6-fake_dnsupdate6`、`atk6-fake_mipv6`、`atk6-fake_mld26`、`atk6-fake_mld6`、`atk6-fake_mldrouter6`、`atk6-fake_pim6`、`atk6-fake_router26`、`atk6-fake_router6`、`atk6-fake_solicitate6`、`atk6-firewall6`、`atk6-flood_advertise6`、`atk6-flood_dhcpc6`、`atk6-flood_mld26`、`atk6-flood_mld6`、`atk6-flood_mldrouter6`、`atk6-flood_redir6`、`atk6-flood_router26`、`atk6-flood_router6`、`atk6-flood_rs6`、`atk6-flood_solicitate6`、`atk6-flood_unreach6`、`atk6-four2six`、`atk6-fragmentation6`、`atk6-fragrouter6`、`atk6-fuzz_dhcpc6`、`atk6-fuzz_dhcps6`、`atk6-fuzz_ip6`、`atk6-implementation6`、`atk6-implementation6d`、`atk6-inject_alive6`、`atk6-inverse_lookup6`、`atk6-kill_router6`、`atk6-ndpexhaust26`、`atk6-ndpexhaust6`、`atk6-node_query6`、`atk6-parasite6`、`atk6-passive_discovery6`、`atk6-randicmp6`、`atk6-redir6`、`atk6-redirsniff6`、`atk6-rsmurf6`、`atk6-sendpees6`、`atk6-sendpeesmp6`、`atk6-smurf6`、`atk6-thcping6`、`atk6-thcsyn6`、`atk6-toobig6`、`atk6-toobigsniff6`、`atk6-trace6` |
| 安装 | `sudo apt install thc-ipv6` |
| 占用空间 | 3.68 MB |
| 依赖 | `libc6`、`libnetfilter-queue1`、`libpcap0.8t64`、`libssl3t64`、`atk6-address6` |
| 官网 | <http://www.thc.org/thc-ipv6/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/thc-ipv6> |

### theharvester

Tool for gathering e-mail accounts and subdomain names from public sources The package contains a tool for gathering subdomain names, e-mail addresses, virtual hosts, open ports/ banners, and employee names from different public sources (search engines, pgp key servers).

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/theharvester/> |
| 版本 | 4.11.1 |
| 包 / 命令 | `theharvester` |
| 安装 | `sudo apt install theharvester` |
| 占用空间 | 2.26 MB |
| 依赖 | `kali-defaults`、`python3`、`python3-aiodns`、`python3-aiofiles`、`python3-aiohttp`、`python3-aiohttp-socks`、`python3-aiomultiprocess`、`python3-aiosqlite`、`python3-bs4`、`python3-censys`、`python3-certifi`、`python3-dateutil` 等 |
| 官网 | <https://github.com/laramies/theHarvester> |
| 源码 | <https://gitlab.com/kalilinux/packages/theharvester> |

### tlssled

Evaluates the security of a target SSL/TLS (HTTPS) server TLSSLed is a Linux shell script whose purpose is to evaluate the security of a target SSL/TLS (HTTPS) web server implementation. It is based on sslscan, a thorough SSL/TLS scanner that is based on the openssl library, and on the “openssl s_client” command line tool. The current tests

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/tlssled/> |
| 版本 | 1.3 |
| 包 / 命令 | `tlssled` |
| 安装 | `sudo apt install tlssled` |
| 占用空间 | 38 KB |
| 依赖 | `openssl`、`sslscan`、`tlssled` |
| 官网 | <http://www.taddong.com/en/lab.html> |
| 源码 | <https://gitlab.com/kalilinux/packages/tlssled> |

### twofi

Twitter words of interest When attempting to crack passwords custom word lists are very useful additions to standard dictionaries. An interesting idea originally released on the “7 Habits of Highly Effective Hackers” blog was to use Twitter to help generate those lists based on searches for keywords related

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/twofi/> |
| 版本 | 2.0 |
| 包 / 命令 | `twofi` |
| 安装 | `sudo apt install twofi` |
| 占用空间 | 38 KB |
| 依赖 | `ruby`、`ruby-twitter`、`twofi` |
| 官网 | <https://www.digininja.org/projects/twofi.php> |
| 源码 | <https://gitlab.com/kalilinux/packages/twofi> |

### tzdata

Time zone and daylight-saving time data This package contains data required for the implementation of standard local time for many representative locations around the globe. It is updated periodically to reflect changes made by political bodies to time zone boundaries, UTC offsets, and daylight-saving rules.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 802.11 Wi-Fi、蓝牙、漏洞利用、数字取证、模糊测试、硬件攻击、识别与指纹、信息搜集 等 23 个 |
| Kali 文档 | <https://www.kali.org/tools/tzdata/> |
| 版本 | 2026c |
| 包 / 命令 | `tzdata`、`tzdata-legacy` |
| 安装 | `sudo apt install tzdata` |
| 占用空间 | 1.32 MB |
| 官网 | <https://www.iana.org/time-zones> |
| 源码 | <https://salsa.debian.org/glibc-team/tzdata> |

### unicornscan

Userland distributed TCP/IP stack Unicornscan is a new information gathering and correlation engine built for and by members of the security research and testing communities. It was designed to provide an engine that is Scalable, Accurate, Flexible, and Efficient. It is released for the community to use under the terms of the GPL license. Benefits:

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/unicornscan/> |
| 版本 | 0.4.7 |
| 包 / 命令 | `unicornscan`、`fantaip`、`unibrow`、`unicfgtst`、`us` |
| 安装 | `sudo apt install unicornscan` |
| 占用空间 | 3.61 MB |
| 依赖 | `flex`、`libc6`、`libpcap0.8t64`、`fantaip` |
| 官网 | <http://www.unicornscan.org/> |
| 源码 | <https://gitlab.com/kalilinux/packages/unicornscan> |

### urlcrazy

Domain typo generator Generate and test domain typos and variations to detect and perform typo squatting, URL hijacking, phishing, and corporate espionage.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| Kali 文档 | <https://www.kali.org/tools/urlcrazy/> |
| 版本 | 0.8.2 |
| 包 / 命令 | `urlcrazy` |
| 安装 | `sudo apt install urlcrazy` |
| 占用空间 | 1.31 MB |
| 依赖 | `ruby`、`ruby-async`、`ruby-async-dns`、`ruby-async-http`、`ruby-colorize`、`ruby-httpclient`、`rubygems`、`urlcrazy` |
| 官网 | <https://www.morningstarsecurity.com/research/urlcrazy> |
| 源码 | <https://gitlab.com/kalilinux/packages/urlcrazy> |

### util-linux

Miscellaneous system utilities This package contains a number of important utilities, most of which are oriented towards maintenance of your system. Some of the more important utilities included in this package allow you to view kernel messages, create new filesystems, view block device information, interface with real time clock, etc.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 802.11 Wi-Fi、蓝牙、密码学与隐写、数据库、检测、漏洞利用、数字取证、模糊测试 等 28 个 |
| Kali 文档 | <https://www.kali.org/tools/util-linux/> |
| 版本 | 2.42.2 |
| 包 / 命令 | `bsdextrautils`、`col`、`colcrt`、`colrm`、`column`、`hd`、`hexdump`、`look`、`rev`、`ul`、`bsdutils`、`renice`、`script`、`scriptlive`、`scriptreplay`、`wall`、`eject`、`eject-udeb`、`fdisk`、`cfdisk`、`sfdisk`、`fdisk-udeb`、`lastlog2`、`libblkid-dev`、`libblkid1`、`libblkid1-udeb`、`libfdisk-dev`、`libfdisk1`、`libfdisk1-udeb`、`liblastlog2-2`、`liblastlog2-dev`、`libmount-dev`、`libmount1`、`libmount1-udeb`、`libpam-lastlog2`、`libsmartcols-dev`、`libsmartcols1`、`libsmartcols1-udeb`、`libuuid1`、`libuuid1-udeb`、`login`、`nologin`、`mount`、`losetup`、`swapoff`、`swapon`、`umount`、`rfkill`、`util-linux`、`agetty`、`blkdiscard`、`blkid`、`blockdev`、`choom`、`chrt`、`dmesg`、`fallocate`、`findfs`、`findmnt`、`flock`、`fsck`、`fsfreeze`、`fstrim`、`getopt`、`getty`、`hardlink`、`i386`、`ionice`、`ipcmk`、`ipcrm`、`ipcs`、`linux32`、`linux64`、`logger`、`lsblk`、`lscpu`、`lsipc`、`lslocks`、`lsns`、`mcookie`、`mkfs`、`mkswap`、`more`、`mountpoint`、`namei`、`nsenter`、`partx`、`prlimit`、`readprofile`、`rtcwake`、`runuser`、`setarch`、`setpriv`、`setsid`、`setterm`、`su`、`sulogin`、`swaplabel`、`taskset`、`uclampset`、`unshare`、`whereis`、`wipefs`、`x86_64`、`zramctl`、`util-linux-extra`、`addpart`、`bits`、`blkpr`、`blkzone`、`chcpu`、`chmem`、`copyfilerange`、`coresched`、`ctrlaltdel`、`delpart`、`enosys`、`exch`、`fadvise`、`fincore`、`fsck.cramfs`、`fsck.minix`、`getino`、`hwclock`、`isosize`、`ldattach`、`lsclocks`、`lsfd`、`lsirq`、`lslogins`、`lsmem`、`mkfs.bfs`、`mkfs.cramfs`、`mkfs.minix`、`newgrp`、`pipesz`、`pivot_root`、`rename.ul`、`resizepart`、`sg`、`switch_root`、`waitpid`、`wdctl`、`util-linux-locales`、`util-linux-udeb`、`uuid-dev`、`uuid-runtime`、`uuidd`、`uuidgen`、`uuidparse` |
| 安装 | `sudo apt install util-linux` |
| 占用空间 | 4.54 MB |
| 依赖 | `libblkid1`、`libc6`、`libcap-ng0`、`libcrypt1`、`libmount1`、`libpam-modules`、`libpam-runtime`、`libpam0g`、`libselinux1`、`libsmartcols1`、`libsystemd0`、`libtinfo6` 等 |
| 官网 | <https://github.com/util-linux/util-linux> |
| 源码 | <https://salsa.debian.org/debian/util-linux> |

### wafw00f

Identify and fingerprint Web Application Firewall products This package identifies and fingerprints Web Application Firewall (WAF) products using the following logic: Sends a normal HTTP request and analyses the response; this identifies a

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/wafw00f/> |
| 版本 | 2.4.2 |
| 包 / 命令 | `wafw00f` |
| 安装 | `sudo apt install wafw00f` |
| 占用空间 | 265 KB |
| 依赖 | `python3`、`python3-requests`、`wafw00f` |
| 官网 | <https://github.com/EnableSecurity/wafw00f> |
| 源码 | <https://salsa.debian.org/pkg-security-team/wafw00f> |

### wapiti

Web application vulnerability scanner Wapiti allows you to audit the security of your web applications. It performs “black-box” scans, i.e. it does not study the source code of the application but will scan the web pages of the deployed web applications, looking for scripts and forms where it can inject data. Once it gets this list, Wapiti acts like a fuzzer, injecting payloads to see

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 识别与指纹、信息搜集、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/wapiti/> |
| 版本 | 3.2.10 |
| 包 / 命令 | `wapiti`、`wapiti-getcookie` |
| 安装 | `sudo apt install wapiti` |
| 占用空间 | 3.26 MB |
| 依赖 | `mitmproxy`、`python3`、`python3-aiosqlite`、`python3-browser-cookie3`、`python3-bs4`、`python3-dnspython`、`python3-httpcore`、`python3-httpx`、`python3-httpx-ntlm`、`python3-mako`、`python3-packaging`、`python3-playwright` 等 |
| 官网 | <https://wapiti.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/wapiti> |

### wget

Retrieves files from the web Wget is a network utility to retrieve files from the web using HTTP(S) and FTP, the two most widely used internet protocols. It works non-interactively, so it will work in the background, after having logged off. The program supports recursive retrieval of web-authoring pages as well as FTP

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 802.11 Wi-Fi、蓝牙、漏洞利用、识别与指纹、信息搜集、后渗透、报告与记录、逆向工程 等 13 个 |
| Kali 文档 | <https://www.kali.org/tools/wget/> |
| 版本 | 1.25.0 |
| 包 / 命令 | `wget`、`wget-udeb` |
| 安装 | `sudo apt install wget` |
| 占用空间 | 3.69 MB |
| 依赖 | `libc6`、`libgnutls30t64`、`libidn2-0`、`libnettle8t64`、`libpcre2-8-0`、`libpsl5t64`、`libuuid1`、`zlib1g`、`wget` |
| 官网 | <https://www.gnu.org/software/wget/> |
| 源码 | <https://salsa.debian.org/debian/wget> |

### whatweb

Next generation web scanner WhatWeb identifies websites. It recognises web technologies including content management systems (CMS), blogging platforms, statistic/analytics packages, JavaScript libraries, web servers, and embedded devices. WhatWeb has over 900 plugins, each to recognise something different. It also identifies version numbers, email addresses, account IDs,

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/whatweb/> |
| 版本 | 0.6.4 |
| 包 / 命令 | `whatweb` |
| 安装 | `sudo apt install whatweb` |
| 占用空间 | 18.76 MB |
| 依赖 | `ruby`、`ruby-addressable`、`ruby-ipaddress`、`whatweb` |
| 官网 | <https://github.com/urbanadventurer/WhatWeb> |

### wordlists

Contains the rockyou wordlist This package contains the rockyou.txt wordlist and has an installation size of 134 MB.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、口令攻击、漏洞分析 |
| Kali 文档 | <https://www.kali.org/tools/wordlists/> |
| 版本 | 2026.2.0 |
| 包 / 命令 | `wordlists` |
| 安装 | `sudo apt install wordlists` |
| 占用空间 | 50.90 MB |
| 依赖 | `kali-defaults`、`sudo`、`wordlists` |
| 官网 | <https://www.kali.org> |
| 源码 | <https://gitlab.com/kalilinux/packages/wordlists> |

### wpscan

Black box WordPress vulnerability scanner WPScan scans remote WordPress installations to find security issues.

| 项目 | 内容 |
|------|------|
| 归入分组 | 信息搜集 |
| 全部所属分组 | 信息搜集、漏洞分析、Web 应用 |
| Kali 文档 | <https://www.kali.org/tools/wpscan/> |
| 版本 | 4.1.0 |
| 包 / 命令 | `wpscan` |
| 安装 | `sudo apt install wpscan` |
| 占用空间 | 695 KB |
| 依赖 | `curl`、`ruby`、`ruby-activesupport`、`ruby-addressable`、`ruby-cms-scanner`、`ruby-ethon`、`ruby-ferrum`、`ruby-fiddle`、`ruby-get-process-mem`、`ruby-nokogiri`、`ruby-ostruct`、`ruby-progressbar` 等 |
| 官网 | <https://wpscan.com/wordpress-security-scanner> |
| 源码 | <https://gitlab.com/kalilinux/packages/wpscan> |
