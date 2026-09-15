# ipv6toolkit

> IPv6 assessment and troubleshooting tools Included tools: addr6: An IPv6 address analysis and manipulation tool. flow6: A tool to perform a security asseessment of the IPv6 Flow Label. frag6: A tool to perform IPv6 fragmentation-based atta…

> **功能分类**：通用工具 ｜ **Kali 包**：`ipv6toolkit` ｜ **官方文档**：<https://www.kali.org/tools/ipv6toolkit/>

## 1. 安装

```bash
sudo apt update
sudo apt install ipv6toolkit
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.2 |
| 架构 | any |
| 可执行命令 | `ipv6toolkit`、`addr6`、`blackhole6`、`flow6`、`frag6`、`icmp6`、`jumbo6`、`messi`、`mldq6`、`na6`、`ni6`、`ns6`、`path6`、`ra6`、`rd6`、`rs6`、`scan6`、`script6`、`tcp6`、`udp6` |
| 依赖 | `ieee-data`、`libc6`、`libpcap0.8t64`、`addr6` |
| 安装体积 | 3.49 MB |
| 官网 | <https://www.si6networks.com/tools/ipv6toolkit/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ipv6toolkit> |
| 包追踪 | <https://pkg.kali.org/pkg/ipv6toolkit> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ipv6toolkit -h          # 查看用法
man ipv6toolkit         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 20 个可执行命令，下面是官方页面内嵌的帮助原文。

### `addr6`

> 官方示例调用：`addr6 -h`

```text
root@kali:~# addr6 -h
SI6 Networks' IPv6 Toolkit 2.2
addr6: An IPv6 address analysis and conversion tool
usage: addr6 (-i | -a) [-c | -d | -r | -s | -q] [-v] [-h]
OPTIONS:
  --address, -a             IPv6 address to be decoded
  --gen-addr, -A            Generate a randmized address for the specified prefix
  --stdin, -i               Read IPv6 addresses from stdin (standard input)
  --print-fixed, -f         Print addresses in expanded/fixed format
  --print-canonic, -c       Print IPv6 addresses in canonic form
  --print-reverse, -r       Print reversed IPv6 address
  --print-decode, -d        Decode IPv6 addresses
  --print-stats, -s         Print statistics about IPv6 addresses
  --print-response, -R      Print result of address filters
  --print-pattern, -x       Analyze addresses pattern
  --print-uni-preflen, -P   Print unique prefixes of a specified length
  --block-dup, -q           Discard duplicate IPv6 addresses
  --block-dup-preflen, -p   Discard duplicate prefixes of specified length
  --accept, -j              Accept IPv6 addresses from specified IPv6 prefix
  --accept-type, -b         Accept IPv6 addresses of specified type
  --accept-scope, -k        Accept IPv6 addresses of specified scope
  --accept-utype, -w        Accept IPv6 unicast addresses of specified type
  --accept-iid, -g          Accept IPv6 addresses with IIDs of specified type
  --block, -J               Block IPv6 addresses from specified IPv6 prefix
  --block-type, -B          Block IPv6 addresses of specified type
  --block-scope, -K         Block IPv6 addresses of specified scope
  --block-utype, -W         Block IPv6 unicast addresses of specified type
  --block-iid, -G           Block IPv6 addresses with IIDs of specified type
  --verbose, -v             Be verbose
  --help, -h                Print help for the addr6 tool
 Programmed by Fernando Gont for SI6 Networks <https://www.si6networks.com>
 Please send any bug reports to <
[email protected]
>
```

### `man`

> 官方示例调用：`man blackhole6`

```text
root@kali:~# man blackhole6
BLACKHOLE6(1)               General Commands Manual               BLACKHOLE6(1)
NAME
     blackhole6 - A tool to find IPv6 blackholes
SYNOPSIS
     blackhole6 DESTINATION [PARAMETERS]
DESCRIPTION
     blackhole6 is a tool to isolate IPv6 blackholes.
     SCRIPTS
     get-mx
     This script takes no further arguments, and operates as follows:
         + The tool reads domain names from standard-input (oner per line),
           and obtains the MX for the corresponding domain.
         + Lines where the first non-blank character is the numeral sign (#)
           are consdered to contain comments, and hence are ignored.
         + The format of the resulting output is:
           # DOMAIN_NAME (CANONIC_NAME)
           MX_RECORD_1
           MX_RECORD_2
     get-ns
     This script takes no further arguments, and operates as follows:
         + The tool reads domain names from standard-input (oner per line),
           and obtains the NS records for the corresponding domain.
         + Lines where the first non-blank character is the numeral sign (#)
           are consdered to contain comments, and hence are ignored.
         + The format of the resulting output is:
           # DOMAIN_NAME (CANONIC_NAME)
           MX_RECORD_1
           MX_RECORD_2
     trace-do8-tcp trace-do8-icmp trace-do256-tcp trace-do256-icmp
     These  scripts  are meant to obtain information about where in the network
     packets employing IPv6 Extension Headers are being dropped. They test  the
     path with IPv6 packets containing TCP or ICMPv6 payloads and a Destination
     Options  Header of 8 or 256 bytes. Based on the obtained results, the tool
     can infer what is the system causing the packet drops.
     trace-hbh8-tcp trace-hbh8-icmp trace-hbh256-tcp trace-hbh256-icmp
     These scripts are meant to obtain information about where in  the  network
     packets  employing IPv6 Extension Headers are being dropped. They test the
     path with IPv6 packets containing TCP or ICMPv6 payloads and a  Hop-by-Hop
     Options  Header of 8 or 256 bytes. Based on the obtained results, the tool
     can infer what is the system causing the packet drops.
     trace-fh256-tcp trace-fh256-icmp
     These scripts are meant to obtain information about where in  the  network
     packets  employing IPv6 Extension Headers are being dropped. They test the
     path with IPv6 packets containing TCP or ICMPv6 payloads resulting in IPv6
     fragments of around 256 bytes. Based on the obtained results, the tool can
     infer what is the system causing the packet drops.
     trace-do8-tcp-stdin  trace-do8-icmp-stdin   trace-do256-tcp-stdin   trace-
     do256-icmp-stdin
     These  scripts  are meant to obtain information about where in the network
     packets employing IPv6 Extension Headers are being dropped. They test  the
     path with IPv6 packets containing TCP or ICMPv6 payloads and a Destination
     Options  Header of 8 or 256 bytes. Based on the obtained results, the tool
     can infer what is the system causing the packet drops.  These  tools  read
     one  IPv6  address per line form standard input and, for each of those ad-
     dresses, information is printed with the following syntax:
     trace-hbh8-tcp-stdin trace-hbh8-icmp-stdin  trace-hbh256-tcp-stdin  trace-
     hbh256-icmp-stdin
     These  scripts  are meant to obtain information about where in the network
     packets employing IPv6 Extension Headers are being dropped. They test  the
     path  with IPv6 packets containing TCP or ICMPv6 payloads and a Hop-by-Hop
     Options Header of 8 or 256 bytes. Based on the obtained results, the  tool
     can  infer  what  is the system causing the packet drops. These tools read
     one IPv6 address per line form standard input and, for each of  those  ad-
     dresses, information is printed with the following syntax:
     trace-fh256-tcp-stdin trace-fh256-icmp-stdin
     These  scripts  are meant to obtain information about where in the network
     packets employing IPv6 Extension Headers are being dropped. They test  the
     path with IPv6 packets containing TCP or ICMPv6 payloads resulting in IPv6
     fragments of around 256 bytes. Based on the obtained results, the tool can
     infer  what  is  the system causing the packet drops. These tools read one
     IPv6 address per line form standard input  and,  for  each  of  those  ad-
     dresses, information is printed with the following syntax:
     -h, --help
            Print help information for the scan6 tool.
EXAMPLES
     The following sections illustrate typical use cases of the script6 tool.
     Example #1
     # scan6 -i eth0 -L -e -v
     Perform  host  scanning on the local network ("-L" option) using interface
     "eth0" ("-i" option). Use both ICMPv6 echo requests and unrecognized  IPv6
     options  of type 10xxxxxx (default). Print link-link layer addresses along
     with IPv6 addresses ("-e" option). Be verbose ("-v" option).
     Example #2
     #  scan6   -d   2001:db8::/64   --tgt-virtual-machines   all   --ipv4-host
     10.10.10.0/24
     Scan  for  virtual  machines  (both  VirtualBox  and vmware) in the prefix
     2001:db8::/64. The additional information about the IPv4  prefix  employed
     by the host system is leveraged to reduce the search space.
     Example #3
     #   scan6   -d   2001:db8::/64   --tgt-ipv4-embedded  ipv4-32  --ipv4-host
     10.10.10.0/24
     Scan for IPv6 addresses of the network 2001:db8::/64 that embed  the  IPv4
     prefix 10.10.10.0/24 (with the 32-bit encoding).
     Example #4
     # scan6 -d 2001:db8:0-500:0-1000
     Scan for IPv6 addresses of the network 2001:db8::/64, varying the two low-
     est order 16-bit words of the addresses in the range 0-500 and 0-1000, re-
     spectively.
     Example #5
     # scan6 -d fc00::/64 --tgt-vendor 'Dell Inc' -p tcp
     Scan  for  network devices manufactured by 'Dell Inc' in the target prefix
     fc00::/64. The tool will employ TCP segments as the probe packets  (rather
     than the default ICMPv6 echo requests).
     Example #6
     # scan6 -i eth0 -L -S 66:55:44:33:22:11 -p unrec -P global -v
     Use the "eth0" interface ("-i" option) to perform host-scanning on the lo-
     cal  network  ("-L"  option).  The  Ethernet  Source  Address  is  set  to
     "66:55:44:33:22:11" ("-S" option). The probe packets will be IPv6  packets
     with  unrecognized  options  of type 10xxxxxx ("-p" option). The tool will
     only print IPv6 global addresses ("-P" option). The tool will be verbose.
     Example #7
     # scan6 -d 2001:db8::/64 -w KNOWN_IIDS
     Perform an address scan of a  set  of  known  hosts  listed  in  the  file
     KNOWN_IIDS,  at remote network 2001:db8::/64. The target addresses are ob-
     taining by concatenating the network prefix 2001:db8::/64 with the  inter-
     face IDs of each of the addresses fund in the file KNOWN_IIDS.
     Example #8
     # scan6 -i eth0 -L -P global --print-unique -e
     Use the "eth0" interface ("-i" option) to perform host-scanning on the lo-
     cal  network  ("-L" option). Print only global unicast addresses ("-P" op-
     tion), and at most one IPv6 address per Ethernet address ("--print-unique"
     option). Ethernet addresses will be printed along with the  corresponiding
     IPv6 address ("-e" option).
     Example #9
     # scan6 -m knownprefixes.txt -w knowniids.txt -l -z 60 -t -v
     Build  the  list  of  targets from the IPv6 prefixes contained in the file
     'knownprefixes.txt' and the Interface IDs (IIDs)  contained  in  the  file
     'knowniids.txt'. Poll the targets periodically ("-l" option), and sleep 60
     seconds  after  each  iteration ("-z" option). Print a timestamp along the
     IPv6 address of each alive node ("-t" option). Be verbose ("-v" option).
AUTHOR
     The script6 tool and the corresponding manual pages were produced by  Fer-
     nando  Gont  <
[email protected]
>  for SI6 Networks <http://www.si6net-
     works.com>.
COPYRIGHT
     Copyright (c) 2014-2015 Fernando Gont.
     Permission is granted to copy, distribute and/or modify this document  un-
     der  the  terms  of the GNU Free Documentation License, Version 1.3 or any
     later version published by the Free Software Foundation; with no Invariant
     Sections, no Front-Cover Texts, and no Back-Cover Texts.  A  copy  of  the
     license is available at <http://www.gnu.org/licenses/fdl.html>.
                                                                  BLACKHOLE6(1)
```

### `flow6`

> 官方示例调用：`flow6 -h`

```text
root@kali:~# flow6 -h
SI6 Networks' IPv6 Toolkit 2.2
flow6: Security assessment tool for the IPv6 Flow Label field
usage: flow6 -d DST_ADDR [-i INTERFACE] [-S LINK_SRC_ADDR] [-D LINK-DST-ADDR]
       [-s SRC_ADDR[/LEN]] [-A HOP_LIMIT] [-P PROTOCOL] [-p PORT]
       [-W] [-v] [-h]
OPTIONS:
  --interface, -i           Network interface
  --link-src-addr, -S       Link-layer Destination Address
  --link-dst-addr, -D       Link-layer Source Address
  --src-addr, -s            IPv6 Source Address
  --dst-addr, -d            IPv6 Destination Address
  --hop-limit, -A           IPv6 Hop Limit
  --protocol, -P            IPv6 Payload protocol (valid: TCP, UDP)
  --dst-port, -p            Transport Protocol Destination Port
  --flow-label-policy, -W   Assess the Flow Label generation policy
  --help, -h                Print help for the flow6 tool
  --verbose, -v             Be verbose
Programmed by Fernando Gont on behalf of SI6 Networks <https://www.si6networks.com>
Please send any bug reports to <
[email protected]
>
```

### `frag6`

> 官方示例调用：`frag6 -h`

```text
root@kali:~# frag6 -h
SI6 Networks' IPv6 Toolkit 2.2
frag6: A security assessment tool for attack vectors based on IPv6 fragments
usage: frag6 -d DST_ADDR [-i INTERFACE] [-S LINK_SRC_ADDR] [-D LINK-DST-ADDR]
       [-s SRC_ADDR[/LEN]] [-A HOP_LIMIT] [-u DST_OPT_HDR_SIZE]
       [-U DST_OPT_U_HDR_SIZE] [-H HBH_OPT_HDR_SIZE] [-P FRAG_SIZE]
       [-O FRAG_TYPE] [-o FRAG_OFFSET] [-I FRAG_ID] [-T] [-n]
       [-p | -W | -X | -F N_FRAGS] [-l] [-z SECONDS] [-v] [-h]
OPTIONS:
  --interface, -i           Network interface
  --link-src-addr, -S       Link-layer Destination Address
  --link-dst-addr, -D       Link-layer Source Address
  --src-addr, -s            IPv6 Source Address
  --dst-addr, -d            IPv6 Destination Address
  --hop-limit, -A           IPv6 Hop Limit
  --dst-opt-hdr, -u         Destination Options Header (Fragmentable Part)
  --dst-opt-u-hdr, -U       Destination Options Header (Unfragmentable Part)
  --hbh-opt-hdr, -H         Hop by Hop Options Header
  --frag-size, -P           IPv6 fragment payload size
  --frag-type, -O           IPv6 Fragment Type {first, last, middle, atomic}
  --frag-offset, -o         IPv6 Fragment Offset
  --frag-id, -I             IPv6 Fragment Identification
  --no-timestamp, -T        Do not include a timestamp in the payload
  --no-responses, -n        Do not print responses to transmitted packets
  --frag-reass-policy, -p   Assess fragment reassembly policy
  --frag-id-policy, -W      Assess the Fragment ID generation policy
  --pod-attack, -X          Perform a 'Ping of Death' attack
  --flood-frags, -F         Flood target with IPv6 fragments
  --loop, -l                Send IPv6 fragments periodically
  --sleep, -z               Pause between sending IPv6 fragments
  --verbose, -v             Be verbose
  --help, -h                Print help for the frag6 tool
Programmed by Fernando Gont for SI6 Networks <https://www.si6networks.com>
Please send any bug reports to <
[email protected]
>
```

### `icmp6`

> 官方示例调用：`icmp6 -h`

```text
root@kali:~# icmp6 -h
SI6 Networks' IPv6 Toolkit 2.2
icmp6: Security assessment tool for attack vectors based on ICMPv6 error messages
usage: icmp6 [-i INTERFACE] [-s SRC_ADDR[/LEN]] [-d DST_ADDR]
       [-S LINK_SRC_ADDR] [-D LINK-DST-ADDR] [-c HOP_LIMIT] [-y FRAG_SIZE]
       [-u DST_OPT_HDR_SIZE] [-U DST_OPT_U_HDR_SIZE] [-H HBH_OPT_HDR_SIZE]
       [-t TYPE[:CODE] | -e CODE | -A CODE -V CODE -R CODE] [-r TARGET_ADDR]
       [-x PEER_ADDR] [-c HOP_LIMIT] [-m MTU] [-O POINTER] [-p PAYLOAD_TYPE]
       [-P PAYLOAD_SIZE] [-n] [-a SRC_PORTL[:SRC_PORTH]]
       [-o DST_PORTL[:DST_PORTH]] [-X TCP_FLAGS] [-q TCP_SEQ] [-Q TCP_ACK]
       [-V TCP_URP] [-w TCP_WIN] [-M] [-j PREFIX[/LEN]] [-k PREFIX[/LEN]]
       [-J LINK_ADDR] [-K LINK_ADDR] [-b PREFIX[/LEN]] [-g PREFIX[/LEN]]
       [-B LINK_ADDR] [-G LINK_ADDR] [-f] [-L | -l] [-z] [-v] [-h]
OPTIONS:
  --interface, -i             Network interface
  --src-addr, -s              IPv6 Source Address
  --dst-addr, -d              IPv6 Destination Address
  --hop-limit, -c             IPv6 Hop Limit
  --frag-hdr. -y              Fragment Header
  --dst-opt-hdr, -u           Destination Options Header (Fragmentable Part)
  --dst-opt-u-hdr, -U         Destination Options Header (Unfragmentable Part)
  --hbh-opt-hdr, -H           Hop by Hop Options Header
  --link-src-addr, -S         Link-layer Destination Address
  --link-dst-addr, -D         Link-layer Source Address
  --icmp6, -t                 ICMPv6 Type:Code
  --icmp6-dest-unreach, -e    ICMPv6 Destination Unreachable
  --icmp6-packet-too-big, -E  ICMPv6 Packet Too Big
  --icmp6-time-exceeded, -A   ICMPv6 Time Exceeeded
  --icmp6-param-problem, -R   ICMPv6 Parameter Problem
  --mtu, -m                   Next-Hop MTU (ICMPv6 Packet Too Big)
  --pointer, -O               Pointer (ICMPv6 Parameter Problem
  --payload-type, -p          Redirected Header Payload Type
  --payload-size, -P          Redirected Header Payload Size
  --no-payload, -n            Do not include a Redirected Header Option
  --ipv6-hlim, -C             ICMPv6 Payload's Hop Limit
  --target-addr, -r           ICMPv6 Payload's IPv6 Source Address
  --peer-addr, -x             ICMPv6 Payload's IPv6 Destination Address
  --target-port, -o           ICMPv6 Payload's Source Port
  --peer-port, -a             ICMPv6 Payload's Destination Port
  --tcp-flags, -X             ICMPv6 Payload's TCP Flags
  --tcp-seq, -q               ICMPv6 Payload's TCP SEQ Number
  --tcp-ack, -Q               ICMPv6 Payload's TCP ACK Number
  --tcp-urg, -V               ICMPv6 Payload's TCP URG Pointer
  --tcp-win, -w               ICMPv6 Payload's TCP Window
  --resp-mcast, -M            Respond to Multicast Packets
  --block-src, -j             Block IPv6 Source Address prefix
  --block-dst, -k             Block IPv6 Destination Address prefix
  --block-link-src, -J        Block Ethernet Source Address
  --block-link-dst, -K        Block Ethernet Destination Address
  --accept-src, -b            Accept IPv6 Source Address prefix
  --accept-dst, -g            Accept IPv6 Destination Address prefix
  --accept-link-src, -B       Accept Ethernet Source Address
  --accept-link-dst, -G       Accept Ethernet Destination Address
  --sanity-filters, -f        Add sanity filters
  --listen, -L                Listen to incoming traffic
  --loop, -l                  Send periodic ICMPv6 error messages
  --sleep, -z                 Pause between sending ICMPv6 error messages
  --help, -h                  Print help for the icmp6 tool
  --verbose, -v               Be verbose
 Programmed by Fernando Gont for SI6 Networks <https://www.si6networks.com>
 Please send any bug reports to <
[email protected]
>
```

### `jumbo6`

> 官方示例调用：`jumbo6 -h`

```text
root@kali:~# jumbo6 -h
SI6 Networks' IPv6 Toolkit 2.2
jumbo6: Security assessment tool for attack vectors based on IPv6 jumbo packets
usage: jumbo6 -d DST_ADDR [-i INTERFACE] [-S LINK_SRC_ADDR] [-D LINK-DST-ADDR]
       [-s SRC_ADDR[/LEN]] [-A HOP_LIMIT] [-H HBH_OPT_HDR_SIZE]
       [-U DST_OPT_U_HDR_SIZE] [-y FRAG_SIZE] [-u DST_OPT_HDR_SIZE]
       [-q IPV6_LENGTH] [-Q JUMBO_LENGTH] [-P PAYLOAD_SIZE] [-j PREFIX[/LEN]]
       [-k PREFIX[/LEN]] [-J LINK_ADDR] [-K LINK_ADDR] [-b PREFIX[/LEN]]
       [-g PREFIX[/LEN]] [-B LINK_ADDR] [-G LINK_ADDR] [-L | -l] [-z SECONDS]
       [-v] [-h]
OPTIONS:
  --interface, -i           Network interface
  --link-src-addr, -S       Link-layer Destination Address
  --link-dst-addr, -D       Link-layer Source Address
  --src-addr, -s            IPv6 Source Address
  --dst-addr, -d            IPv6 Destination Address
  --hop-limit, -A           IPv6 Hop Limit
  --frag-hdr. -y            Fragment Header
  --dst-opt-hdr, -u         Destination Options Header (Fragmentable Part)
  --dst-opt-u-hdr, -U       Destination Options Header (Unfragmentable Part)
  --hbh-opt-hdr, -H         Hop by Hop Options Header
  --ipv6-length, -q         IPv6 Payload Length
  --jumbo-length, -Q        Jumbo Payload Length
  --payload-size, -P        ICMPv6 payload size
  --loop, -l                Send periodic Jumbo messages
  --sleep, -z               Pause between sending Redirect messages
  --listen, -L              Listen to incoming packets
  --verbose, -v             Be verbose
  --help, -h                Print help for the jumbo6 tool
Programmed by Fernando Gont on behalf of SI6 Networks <https://www.si6networks.com>
Please send any bug reports to <
[email protected]
>
```

### `mldq6`

> 官方示例调用：`mldq6 -h`

```text
root@kali:~# mldq6 -h
SI6 Networks' IPv6 Toolkit 2.2
mldq6: Security assessment tool for attack vectors based on MLD Query messages
usage: mldq6 -i INTERFACE [-s SRC_ADDR[/LEN]] [-d DST_ADDR] [-A HOP_LIMIT] [-y FRAG_SIZE] [-u DST_OPT_HDR_SIZE] [-U DST_OPT_U_HDR_SIZE] [-H HBH_OPT_HDR_SIZE] [-S LINK_SRC_ADDR] [-D LINK-DST-ADDR] [-E LINK_ADDR] [-e] [-m MLD_ADDR] [-r MLD_RESP_DELAY ] [-F N_SOURCES] [-z SECONDS] [-l] [-v] [-h]
OPTIONS:
  --interface, -i            Network interface
  --src-addr, -s             IPv6 Source Address
  --dst-addr, -d             IPv6 Destination Address
  --hop-limit, -A            IPv6 Hop Limit
  --frag-hdr. -y             Fragment Header
  --dst-opt-hdr, -u          Destination Options Header (Fragmentable Part)
  --dst-opt-u-hdr, -U        Destination Options Header (Unfragmentable Part)
  --hbh-opt-hdr, -H          Hop by Hop Options Header
  --link-src-addr, -S        Link-layer Destination Address
  --link-dst-addr, -D        Link-layer Source Address
  --src-link-opt, -E         Source link-layer address option
  --add-slla-opt, -e         Add Source link-layer address option
  --mld-addr, -m             MLD Query Multicast Address
  --mld-resp-delay, -r       MLD Query Maximum Response Delay [ms]
  --flood-sources, -F        Number of Source Addresses to forge randomly
  --loop, -l                 Send MLD Query periodically
  --sleep, -z                Pause between peiodic MLD Queries [sec]
  --help, -h                 Print help for the mldq6 tool
  --verbose, -v              Be verbose
Programmed by Fernando Gont for SI6 Networks <https://www.si6networks.com>
Please send any bug reports to <
[email protected]
>
```

### `na6`

> 官方示例调用：`na6 -h`

```text
root@kali:~# na6 -h
SI6 Networks' IPv6 Toolkit 2.2
na6: Security Assessment tool for attack vectors based on NA messages
usage: na6 -i INTERFACE [-s SRC_ADDR[/LEN]] [-d DST_ADDR] [-S LINK_SRC_ADDR] [-y FRAG_SIZE] [-u DST_OPT_HDR_SIZE] [-U DST_OPT_U_HDR_SIZE] [-H HBH_OPT_HDR_SIZE] [-D LINK-DST-ADDR] [-t TARGET_ADDR[/LEN]] [-r] [-c] [-o] [-E LINK_ADDR] [-e] [-j PREFIX[/LEN]] [-k PREFIX[/LEN]] [-J LINK_ADDR] [-K LINK_ADDR] [-w PREFIX[/LEN]] [-b PREFIX[/LEN]] [-g PREFIX[/LEN]] [-B LINK_ADDR] [-G LINK_ADDR] [-W PREFIX[/LEN]] [-F N_SOURCES] [-T N_TARGETS] [-L | -l] [-z] [-v] [-V] [-h]
OPTIONS:
  --interface, -i            Network interface
  --src-addr, -s             IPv6 Source Address
  --dst-addr, -d             IPv6 Destination Address
  --frag-hdr. -y             Fragment Header
  --dst-opt-hdr, -u          Destination Options Header (Fragmentable Part)
  --dst-opt-u-hdr, -U        Destination Options Header (Unfragmentable Part)
  --hbh-opt-hdr, -H          Hop by Hop Options Header
  --link-src-addr, -S        Link-layer Destination Address
  --link-dst-addr, -D        Link-layer Source Address
  --target, -t               ND IPv6 Target Address
  --target-lla-opt, -E       Source link-layer address option
  --add-tlla-opt, -e         Add Source link-layer address option
  --router, -r               Set the 'Router Flag'
  --solicited, -c            Set the 'Solicited' flag
  --override, -o             Set the 'Override' flag
  --block-src, -j            Block IPv6 Source Address prefix
  --block-dst, -k            Block IPv6 Destination Address prefix
  --block-link-src, -J       Block Ethernet Source Address
  --block-link-dst, -K       Block Ethernet Destination Address
  --block-target, -w         Block ND Target IPv6 prefix
  --accept-src, -b           Accept IPv6 Source Address prefix
  --accept-dst, -g           Accept IPv6 Destination Address prefix
  --accept-link-src, -B      Accept Ethernet Source Address
  --accept-link-dst, -G      Accept Ethernet Destination Address
  --accept-target, -W        Accept ND Target IPv6 prefix
  --flood-targets, -T        Flood with NA's for multiple Target Addresses
  --flood-sources, -F        Number of Source Addresses to forge randomly
  --listen, -L               Listen to Neighbor Solicitation messages
  --loop, -l                 Send periodic Neighbor Advertisements
  --sleep, -z                Pause between sending NA messages
  --help, -h                 Print help for the na6 tool
  --verbose, -v              Be verbose
Programmed by Fernando Gont for SI6 Networks <https://www.si6networks.com>
Please send any bug reports to <
[email protected]
>
```

### `ni6`

> 官方示例调用：`ni6 -h`

```text
root@kali:~# ni6 -h
SI6 Networks' IPv6 Toolkit 2.2
ni6: Security assessment tool for attack vectors based on ICMPv6 NI messages
usage:
 ni6 [-i INTERFACE] [-S LINK_SRC_ADDR | -R] [-D LINK-DST-ADDR]
     [-s SRC_ADDR[/LEN] | -r] [-d DST_ADDR] [-c HOP_LIMIT] [-y FRAG_SIZE]
     [-u DST_OPT_HDR_SIZE] [-U DST_OPT_U_HDR_SIZE] [-H HBH_OPT_HDR_SIZE]
     [-P SIZE | -6 IPV6_ADDR | -4 IPV4_ADDR | -n NAME | -N LEN | -x LEN -o TYPE]
     [-Z SIZE] [-e] [-C ICMP6_CODE] [-q NI_QTYPE] [-X NI_FLAGS]
     [-P SIZE | -w IPV6_ADDR | -W IPV4_ADDR | -a NAME | -A LEN | -Q LEN -O TYPE]
     [-E] [-j PREFIX[/LEN]] [-k PREFIX[/LEN]] [-J LINK_ADDR]
     [-K LINK_ADDR] [-b PREFIX[/LEN]] [-g PREFIX[/LEN]] [-B LINK_ADDR]
     [-G LINK_ADDR] [-L | -l] [-z] [-v] [-h]
OPTIONS:
  --interface, -i            Network interface
  --link-src-addr, -S        Link-layer Destination Address
  --link-dst-addr, -D        Link-layer Source Address
  --src-addr, -s             IPv6 Source Address
  --dst-addr, -d             IPv6 Destination Address
  --hop-limit, -c            IPv6 Hop Limit
  --frag-hdr. -y             Fragment Header
  --dst-opt-hdr, -u          Destination Options Header (Fragmentable Part)
  --dst-opt-u-hdr, -U        Destination Options Header (Unfragmentable Part)
  --hbh-opt-hdr, -H          Hop by Hop Options Header
  --payload-size, -P         ICMPv6 NI payload size
  --subject-ipv6. -6         Subject IPv6 Address
  --subject-ipv4, -4         Subject IPv4 address
  --subject-name, -n         Subject Name
  --subject-fname, -N        Forge Subject Name of specific length
  --subject-ename, -x        For (malformed) Subject name of specified length
  --subject-nloop, -o        Subject is a Name with a DNS compression loop
  --max-label-size, -Z       Maximum DNS label size (defaults to 63)
  --sname-slabel, -e         Subject Name is a single-label name
  --code, -C                 ICMPv6 code
  --qtype, -q                ICMPv6 NI Qtype
  --flags, -X                ICMPv6 NI flags
  --data-ipv6, -w            Data IPv6 Address
  --data-ipv4, W             Data IPv4 Address
  --data-name, -a            Data Name
  --data-fname, -A           Forge Data Name of specific length
  --data-ename, -Q           For (malformed) Data Name of specified length
  --data-nloop, -O           Data is a Name with a DNS compression loop
  --dname-slabel, -E         Subject Name is a single-label name
  --block-src, -j            Block IPv6 Source Address prefix
  --block-dst, -k            Block IPv6 Destination Address prefix
  --block-link-src, -J       Block Ethernet Source Address
  --block-link-dst, -K       Block Ethernet Destination Address
  --accept-src, -b           Accept IPv6 Source Address prefix
  --accept-dst, -g           Accept IPv6 Destination Address prefix
  --accept-link-src, -B      Accept Ethernet Source Address
  --accept-link-dst, -G      Accept Ethernet Destination Address
  --forge-src-addr, -r       Forge IPv6 Source Address
  --forge-link-src-addr, -R  Forge link-layer Source Address
  --loop, -l                 Send periodic ICMPv6 error messages
  --sleep, -z                Pause between sending ICMPv6 messages
  --listen, -L               Listen to incoming traffic
  --help, -h                 Print help for the ni6 tool
  --verbose, -v              Be verbose
 Programmed by Fernando Gont for SI6 Networks <https://www.si6networks.com>
 Please send any bug reports to <
[email protected]
>
```

### `ns6`

> 官方示例调用：`ns6 -h`

```text
root@kali:~# ns6 -h
SI6 Networks' IPv6 Toolkit 2.2
ns6: Security assessment tool for attack vectors based on NS messages
usage: ns6 -i INTERFACE [-s SRC_ADDR[/LEN]] [-d DST_ADDR] [-y FRAG_SIZE] [-u DST_OPT_HDR_SIZE] [-U DST_OPT_U_HDR_SIZE] [-H HBH_OPT_HDR_SIZE] [-S LINK_SRC_ADDR] [-D LINK-DST-ADDR] [-E LINK_ADDR] [-e] [-t TARGET_ADDR[/LEN]] [-F N_SOURCES] [-T N_TARGETS] [-z SECONDS] [-l] [-v] [-h]
OPTIONS:
  --interface, -i            Network interface
  --src-addr, -s             IPv6 Source Address
  --dst-addr, -d             IPv6 Destination Address
  --frag-hdr. -y             Fragment Header
  --dst-opt-hdr, -u          Destination Options Header (Fragmentable Part)
  --dst-opt-u-hdr, -U        Destination Options Header (Unfragmentable Part)
  --hbh-opt-hdr, -H          Hop by Hop Options Header
  --link-src-addr, -S        Link-layer Destination Address
  --link-dst-addr, -D        Link-layer Source Address
  --target-address, -t       ND Target Address
  --source-lla-opt, -E       Source link-layer address option
  --add-slla-opt, -e         Add Source link-layer address option
  --flood-sources, -F        Number of Source Addresses to forge randomly
  --flood-targets, -T        Flood with NA's for multiple Target Addresses
  --loop, -l                 Send Neighbor Solicitations periodically
  --sleep, -z                Pause between peiodic Neighbor Solicitations
  --help, -h                 Print help for the ns6 tool
  --verbose, -v              Be verbose
Programmed by Fernando Gont for SI6 Networks <https://www.si6networks.com>
Please send any bug reports to <
[email protected]
>
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install ipv6toolkit`，再执行 `ipv6toolkit --version` 2>/dev/null || `ipv6toolkit -V`
- [ ] **2.** **读官方帮助** —— `ipv6toolkit -h`，需要细节时 `man ipv6toolkit`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `ipv6toolkit -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ipv6toolkit/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ipv6toolkit/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ipv6toolkit/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
