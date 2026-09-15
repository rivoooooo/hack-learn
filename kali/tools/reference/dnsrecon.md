# dnsrecon

> Powerful DNS enumeration script DNSRecon is a Python script that provides the ability to perform: Check all NS Records for Zone Transfers. Enumerate General DNS Records for a given Domain (MX, SOA, NS, A, AAAA, SPF and TXT). Perform common…

> **功能分类**：信息搜集 ｜ **Kali 包**：`dnsrecon` ｜ **官方文档**：<https://www.kali.org/tools/dnsrecon/>

## 1. 安装

```bash
sudo apt update
sudo apt install dnsrecon
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6.0 |
| 架构 | all |
| 可执行命令 | `dnsrecon` |
| 依赖 | `python3`、`python3-dnspython`、`python3-fastapi`、`python3-httpx`、`python3-loguru`、`python3-netaddr`、`python3-slowapi`、`python3-stamina` |
| 安装体积 | 1.51 MB |
| 官网 | <https://github.com/darkoperator/dnsrecon> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/dnsrecon> |
| 包追踪 | <https://pkg.kali.org/pkg/dnsrecon> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan a domain (-d example.com), use a dictionary to brute force hostnames (-D /usr/share/wordlists/dnsmap.txt), do a standard scan (-t std), and save the output to a file (–xml dnsrecon.xml):
root@kali:~# dnsrecon -d example.com -D /usr/share/wordlists/dnsmap.txt -t std --xml dnsrecon.xml
[*] Performing General Enumeration of Domain:example.com
[*] DNSSEC is configured for example.com
[*] DNSKEYs:
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dnsrecon`

> 官方示例调用：`dnsrecon -d example.com -D /usr/share/wordlists/dnsmap.txt -t std --xml dnsrecon.xml`

```text
root@kali:~# dnsrecon -d example.com -D /usr/share/wordlists/dnsmap.txt -t std --xml dnsrecon.xml
[*] Performing General Enumeration of Domain:example.com
[*] DNSSEC is configured for example.com
[*] DNSKEYs:
```

### `dnsrecon -h`

> 官方示例调用：`dnsrecon -h`

```text
root@kali:~# dnsrecon -h
usage: dnsrecon [-h] [-d DOMAIN] [-iL INPUT_LIST] [-n NS_SERVER] [-r RANGE]
                [-D DICTIONARY] [-f] [-a] [-s] [-b] [-y] [-k] [-w] [--shodan]
                [--shodan-active] [--shodan-key SHODAN_KEY] [-z]
                [--threads THREADS] [--lifetime LIFETIME]
                [--loglevel {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--tcp]
                [--db DB] [-x XML] [-c CSV] [-j JSON] [--iw]
                [--disable_check_nxdomain] [--disable_check_recursion]
                [--disable_recurs] [--disable_check_bindversion] [-V] [-v]
                [-t TYPE]
options:
  -h, --help            show this help message and exit
  -d, --domain DOMAIN   Target domain.
  -iL, --input-list INPUT_LIST
                        File containing a list of domains to perform DNS enumeration on, one per line.
  -n, --name_server NS_SERVER
                        Domain server to use. If none is given, the SOA of the target will be used. Multiple servers can be specified using a comma separated list.
  -r, --range RANGE     IP range for reverse lookup brute force in formats (first-last) or in (range/bitmask).
  -D, --dictionary DICTIONARY
                        Dictionary file of subdomain and hostnames to use for brute force.
  -f                    Filter out of brute force domain lookup, records that resolve to the wildcard defined IP address when saving records.
  -a                    Perform AXFR with standard enumeration.
  -s                    Perform a reverse lookup of IPv4 ranges in the SPF record with standard enumeration.
  -b                    Perform Bing enumeration with standard enumeration.
  -y                    Perform Yandex enumeration with standard enumeration.
  -k                    Perform crt.sh enumeration with standard enumeration.
  -w                    Perform deep whois record analysis and reverse lookup of IP ranges found through Whois when doing a standard enumeration.
  --shodan              Use Shodan to query netblocks discovered via SPF (-s) and/or Whois (-w) during standard enumeration.
  --shodan-active       Actively validate Shodan-discovered names by resolving them and confirming they still match the queried netblock.
  --shodan-key SHODAN_KEY
                        Shodan API key. If omitted, SHODAN_API_KEY environment variable is used.
  -z                    Performs a DNSSEC zone walk with standard enumeration.
  --threads THREADS     Number of threads to use in reverse lookups, forward lookups, brute force and SRV record enumeration.
  --lifetime LIFETIME   Time to wait for a server to respond to a query. default is 3.0
  --loglevel {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Log level to use. default is INFO
  --tcp                 Use TCP protocol to make queries.
  --db DB               SQLite 3 file to save found records.
  -x, --xml XML         XML file to save found records.
  -c, --csv CSV         Save output to a comma separated value file.
  -j, --json JSON       save output to a JSON file.
  --iw                  Continue brute forcing a domain even if a wildcard record is discovered.
  --disable_check_nxdomain
                        Disables check for NXDOMAIN hijacking on name servers.
  --disable_check_recursion
                        Disables check for recursion on name servers
  --disable_recurs      Disable recursion desired flag in queries.
  --disable_check_bindversion
                        Disables check for BIND version on name servers
  -V, --version         DNSrecon version
  -v, --verbose         Enable verbosity
  -t, --type TYPE       Type of enumeration to perform.
                        Possible types:
                            std:      SOA, NS, A, AAAA, MX and SRV.
                            rvl:      Reverse lookup of a given CIDR or IP range.
                            brt:      Brute force domains and hosts using a given dictionary.
                            srv:      SRV records.
                            axfr:     Test all NS servers for a zone transfer.
                            bing:     Perform Bing search for subdomains and hosts.
                            yand:     Perform Yandex search for subdomains and hosts.
                            crt:      Perform crt.sh search for subdomains and hosts.
                            caa:      CAA records.
                            snoop:    Perform cache snooping against all NS servers for a given domain, testing
                                      all with file containing the domains, file given with -D option.
                            tld:      Remove the TLD of given domain and test against all TLDs registered in IANA.
                            zonewalk: Perform a DNSSEC zone walk using NSEC records.
Learn more with
OffSec
Want to learn more about dnsrecon? get access to in-depth training and hands-on labs:
PEN-200: 6.4.1. Information Gathering: DNS Enumeration
PEN-200 course
Updated on: 2026-Aug-25
 Edit this page
dnscat2
dnstracer
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dnsrecon`，再执行 `dnsrecon --version` 2>/dev/null || `dnsrecon -V`
- [ ] **2.** **读官方帮助** —— `dnsrecon -h`，需要细节时 `man dnsrecon`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `dnsrecon -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dnsrecon/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[dnsrecon](../../tools/tutorials/01-信息搜集/dnsrecon.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dnsrecon/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dnsrecon/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
