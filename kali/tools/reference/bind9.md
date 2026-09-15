# bind9

> Internet Domain Name Server The Berkeley Internet Name Domain (BIND 9) implements an Internet domain name server. BIND 9 is the most widely-used name server software on the Internet, and is supported by the Internet Software Consortium, ww…

> **功能分类**：通用工具 ｜ **Kali 包**：`bind9` ｜ **官方文档**：<https://www.kali.org/tools/bind9/>

## 1. 安装

```bash
sudo apt update
sudo apt install bind9
```

| 项目 | 内容 |
|------|------|
| 版本 | 9.20.27 |
| 架构 | any |
| 可执行命令 | `bind9`、`arpaname`、`ddns-confgen`、`dnssec-importkey`、`named`、`named-journalprint`、`named-nzd2nzf`、`named-rrchecker`、`nsec3hash`、`tsig-keygen`、`bind9-dev`、`bind9-dnsutils`、`delv`、`dig`、`dnstap-read`、`mdig`、`nslookup`、`nsupdate`、`bind9-doc`、`bind9-host`、`host`、`bind9-libs`、`bind9-utils`、`dnssec-cds`、`dnssec-dsfromkey`、`dnssec-keyfromlabel`、`dnssec-keygen`、`dnssec-ksr`、`dnssec-revoke`、`dnssec-settime`、`dnssec-signzone`、`dnssec-verify`、`named-checkconf`、`named-checkzone`、`named-compilezone`、`rndc`、`rndc-confgen` |
| 依赖 | `adduser`、`bind9-libs`、`bind9-utils` |
| 安装体积 | 904 KB |
| 官网 | <https://www.isc.org/downloads/bind/> |
| 源码仓库 | <https://salsa.debian.org/dns-team/bind9> |
| 包追踪 | <https://pkg.kali.org/pkg/bind9> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
bind9 -h          # 查看用法
man bind9         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 37 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

官方给出的调用示例：`man arpaname`

```text
root@kali:~# man arpaname
ARPANAME(1)                          BIND 9                         ARPANAME(1)
NAME
     arpaname - translate IP addresses to the corresponding ARPA names
SYNOPSIS
     arpaname {ipaddress ...}
DESCRIPTION
     arpaname  translates  IP  addresses  (IPv4  and IPv6) to the corresponding
     IN-ADDR.ARPA or IP6.ARPA names.
SEE ALSO
     BIND 9 Administrator Reference Manual.
Author
     Internet Systems Consortium
Copyright
     2026, Internet Systems Consortium
9.20.27-2-Debian                   2026-08-05                       ARPANAME(1)
```

### `ddns-confgen`

官方给出的调用示例：`ddns-confgen -h`

```text
root@kali:~# ddns-confgen -h
Usage:
 ddns-confgen [-a alg] [-k keyname] [-q] [-s name | -z zone]
  -a alg:        algorithm (default hmac-sha256)
  -k keyname:    name of the key as it will be used in named.conf
  -s name:       domain name to be updated using the created key
  -z zone:       name of the zone as it will be used in named.conf
  -q:            quiet mode: print the key, with no explanatory text
```

### `dnssec-importkey`

官方给出的调用示例：`dnssec-importkey -h`

```text
root@kali:~# dnssec-importkey -h
Usage:
    dnssec-importkey options [-K dir] keyfile
    dnssec-importkey options -f file [keyname]
Version: 9.20.27-2-Debian
Options:
    -f file: read key from zone file
    -K <directory>: directory in which to store the key files
    -L ttl:             set default key TTL
    -v <verbose level>
    -V: print version information
    -h: print usage and exit
Timing options:
    -P date/[+-]offset/none: set/unset key publication date
    -P sync date/[+-]offset/none: set/unset CDS and CDNSKEY publication date
    -D date/[+-]offset/none: set/unset key deletion date
    -D sync date/[+-]offset/none: set/unset CDS and CDNSKEY deletion date
```

### `named`

官方给出的调用示例：`named -h`

```text
root@kali:~# named -h
usage: named [-4|-6] [-c conffile] [-d debuglevel] [-D comment] [-E engine]
             [-f|-g] [-L logfile] [-n number_of_cpus] [-p port] [-s]
             [-S sockets] [-t chrootdir] [-u username] [-U listeners]
             [-m {usage|trace|record}]
             [-M fill|nofill]
usage: named [-v|-V|-C]
named: unknown option '-h'
```

### `named-journalprint`

官方给出的调用示例：`named-journalprint -h`

```text
root@kali:~# named-journalprint -h
named-journalprint: illegal option -- h
Usage: named-journalprint [-dux] journal
```

### `man（示例）`

官方给出的调用示例：`man named-nzd2nzf`

```text
root@kali:~# man named-nzd2nzf
NAMED-NZD2NZF(1)                     BIND 9                    NAMED-NZD2NZF(1)
NAME
     named-nzd2nzf - convert an NZD database to NZF text format
SYNOPSIS
     named-nzd2nzf {filename}
DESCRIPTION
     named-nzd2nzf  converts  an  NZD  database  to NZF format and prints it to
     standard output. This can be used to review  the  configuration  of  zones
     that   were  added  to  named  <#std-iscman-named>  via  rndc  addzone  <#
     cmdoption-rndc-arg-addzone>. It can also be used to restore the  old  file
     format when rolling back from a newer version of BIND to an older version.
ARGUMENTS
     filename
            This is the name of the .nzd file whose contents should be printed.
SEE ALSO
     BIND 9 Administrator Reference Manual.
Author
     Internet Systems Consortium
Copyright
     2026, Internet Systems Consortium
9.20.27-2-Debian                   2026-08-05                  NAMED-NZD2NZF(1)
```

### `named-rrchecker`

官方给出的调用示例：`named-rrchecker --help`

```text
root@kali:~# named-rrchecker --help
named-rrchecker: illegal option -- -
usage: named-rrchecker [-o origin] [-hpCPTu]
	-h: print this help message
	-o origin: set origin to be used when interpreting the record
	-p: print the record in canonical format
	-C: list the supported class names
	-P: list the supported private type names
	-T: list the supported standard type names
	-u: print the record in unknown record format
```

### `nsec3hash`

官方给出的调用示例：`nsec3hash -h`

```text
root@kali:~# nsec3hash -h
nsec3hash: illegal option -- h
Usage: nsec3hash salt algorithm iterations domain
       nsec3hash -r algorithm flags iterations salt domain
```

### `tsig-keygen`

官方给出的调用示例：`tsig-keygen -h`

```text
root@kali:~# tsig-keygen -h
Usage:
 tsig-keygen [-a alg] [keyname]
  -a alg:        algorithm (default hmac-sha256)
```

### `delv`

官方给出的调用示例：`delv -h`

```text
root@kali:~# delv -h
Usage:  delv [@server] {q-opt} {d-opt} [domain] [q-type] [q-class]
Where:  domain	  is in the Domain Name System
        q-class  is one of (in,hs,ch,...) [default: in]
        q-type   is one of (a,any,mx,ns,soa,hinfo,axfr,txt,...) [default:a]
        q-opt    is one of:
                 -4                  (use IPv4 query transport only)
                 -6                  (use IPv6 query transport only)
                 -a anchor-file      (specify root trust anchor)
                 -b address[#port]   (bind to source address/port)
                 -c class            (option included for compatibility;
                 -d level            (set debugging level)
                 -h                  (print help and exit)
                 -i                  (disable DNSSEC validation)
                 -m                  (enable memory usage debugging)
                 -p port             (specify port number)
                 -q name             (specify query name)
                 -t type             (specify query type)
                                      only IN is supported)
                 -v                  (print version and exit)
                 -x dot-notation     (shortcut for reverse lookups)
        d-opt    is of the form +keyword[=value], where keyword is:
                 +[no]all            (Set or clear all display flags)
                 +[no]class          (Control display of class)
                 +[no]comments       (Control display of comment lines)
                 +[no]crypto         (Control display of cryptographic
                                      fields in records)
                 +[no]dlv            (Obsolete)
                 +[no]dnssec         (Display DNSSEC records)
                 +[no]mtrace         (Trace messages received)
                 +[no]ns             (Run internal name server)
                 +[no]multiline      (Print records in an expanded format)
                 +[no]qmin[=mode]    (QNAME minimization: relaxed or strict)
                 +[no]root           (DNSSEC validation trust anchor)
                 +[no]rrcomments     (Control display of per-record comments)
                 +[no]rtrace         (Trace resolver fetches)
                 +[no]short          (Short form answer)
                 +[no]split=##       (Split hex/base64 fields into chunks)
                 +[no]strace         (Trace messages sent)
                 +[no]tcp            (TCP mode)
                 +[no]ttl            (Control display of ttls in records)
                 +[no]trust          (Control display of trust level)
                 +[no]unknownformat  (Print RDATA in RFC 3597 "unknown" format)
                 +[no]vtrace         (Trace validation process)
                 +[no]yaml           (Present the results as YAML)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install bind9`，再执行 `bind9 --version` 2>/dev/null || `bind9 -V`
- [ ] **2.** **读官方帮助** —— `bind9 -h`，需要细节时 `man bind9`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/bind9/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/bind9/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/bind9/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
