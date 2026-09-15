# tcpreplay

> Tool to replay saved tcpdump files at arbitrary speeds Tcpreplay is aimed at testing the performance of a NIDS by replaying real background network traffic in which to hide attacks. Tcpreplay allows you to control the speed at which the tr…

> **功能分类**：嗅探与欺骗 ｜ **Kali 包**：`tcpreplay` ｜ **官方文档**：<https://www.kali.org/tools/tcpreplay/>

## 1. 安装

```bash
sudo apt update
sudo apt install tcpreplay
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.5.4 |
| 架构 | any |
| 可执行命令 | `tcpreplay`、`tcpbridge`、`tcpcapinfo`、`tcpliveplay`、`tcpprep`、`tcpreplay-edit`、`tcprewrite` |
| 依赖 | `libc6`、`libdumbnet1`、`libpcap0.8t64`、`tcpbridge` |
| 安装体积 | 1.99 MB |
| 官网 | <http://tcpreplay.appneta.com/> |
| 源码仓库 | <https://git.in-ulm.de/cbiedl/tcpreplay> |
| 包追踪 | <https://pkg.kali.org/pkg/tcpreplay> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
tcpreplay -h          # 查看用法
man tcpreplay         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 7 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tcpbridge`

> 官方示例调用：`tcpbridge --help`

```text
root@kali:~# tcpbridge --help
tcpbridge (tcpbridge) - Bridge network traffic across two interfaces
Usage:  tcpbridge [ -<flag> [<val>] | --<name>[{=| }<val>] ]...
:
   -r, --portmap=str          Rewrite TCP/UDP ports
				- may appear up to 9999 times
   -s, --seed=num             Randomize src/dst IPv4/v6 addresses w/ given seed
				- prohibits the option 'fuzz-seed'
   -N, --pnat=str             Rewrite IPv4/v6 addresses using pseudo-NAT
				- prohibits the option 'srcipmap'
				- may appear up to 2 times
   -S, --srcipmap=str         Rewrite source IPv4/v6 addresses using pseudo-NAT
				- prohibits the option 'pnat'
   -D, --dstipmap=str         Rewrite destination IPv4/v6 addresses using pseudo-NAT
				- prohibits the option 'pnat'
       --tcp-sequence=num     Change TCP Sequence (and ACK) numbers /w given seed
				- it must be in the range:
				  greater than or equal to 1
   -b, --skipbroadcast        Skip rewriting broadcast/multicast IPv4/v6 addresses
   -C, --fixcsum              Force recalculation of IPv4/TCP/UDP header checksums
       --fixhdrlen            Alter IP/TCP header len to match packet length
   -m, --mtu=num              Override default MTU length (1500 bytes)
				- it must be in the range:
				  1 to 262144
       --mtu-trunc            Truncate packets larger then specified MTU
   -E, --efcs                 Remove Ethernet checksums (FCS) from end of frames
       --ttl=str              Modify the IPv4/v6 TTL/Hop Limit
       --tos=num              Set the IPv4 TOS/DiffServ/ECN byte
				- it must be in the range:
				  0 to 255
       --tclass=num           Set the IPv6 Traffic Class byte
				- it must be in the range:
				  0 to 255
       --flowlabel=num        Set the IPv6 Flow Label
				- it must be in the range:
				  0 to 1048575
   -F, --fixlen=str           Pad or truncate packet data to match header length
       --fuzz-seed=num        Fuzz 1 in X packets.  Edit bytes, length, or emulate packet drop
				- it must be in the range:
				  greater than or equal to 0
       --fuzz-factor=num      Set the Fuzz 1 in X packet ratio (default 1 in 8 packets)
				- requires the option 'fuzz-seed'
				- it must be in the range:
				  greater than or equal to 1
       --skipl2broadcast      Skip rewriting broadcast/multicast Layer 2 addresses
       --dlt=str              Override output DLT encapsulation
       --enet-dmac=str        Override destination ethernet MAC addresses
       --enet-smac=str        Override source ethernet MAC addresses
       --enet-subsmac=str     Substitute MAC addresses
				- may appear up to 9999 times
       --enet-mac-seed=num    Randomize MAC addresses
				- prohibits these options:
				enet-smac
				enet-dmac
				enet-subsmac
       --enet-mac-seed-keep-bytes=num Randomize MAC addresses
				- requires the option 'enet-mac-seed'
				- it must be in the range:
				  1 to 6
       --enet-vlan=str        Specify ethernet 802.1q VLAN tag mode
       --enet-vlan-tag=num    Specify the new ethernet 802.1q VLAN tag value
				- requires the option 'enet-vlan'
				- it must be in the range:
				  0 to 4095
       --enet-vlan-cfi=num    Specify the ethernet 802.1q VLAN CFI value
				- requires the option 'enet-vlan'
				- it must be in the range:
				  0 to 1
       --enet-vlan-pri=num    Specify the ethernet 802.1q VLAN priority
				- requires the option 'enet-vlan'
				- it must be in the range:
				  0 to 7
       --enet-vlan-proto=str  Specify VLAN tag protocol 802.1q or 802.1ad
       --hdlc-control=num     Specify HDLC control value
       --hdlc-address=num     Specify HDLC address
       --user-dlt=num         Set output file DLT type
       --user-dlink=str       Rewrite Data-Link layer with user specified data
				- may appear up to 2 times
   -d, --dbug=num             Enable debugging output
				- it must be in the range:
				  0 to 5
   -i, --intf1=str            Primary interface (listen in uni-directional mode)
   -I, --intf2=str            Secondary interface (send in uni-directional mode)
   -u, --unidir               Send and receive in only one direction
       --listnics             List available network interfaces and exit
   -L, --limit=num            Limit the number of packets to send
				- it must be in the range:
				  greater than or equal to 1
   -M, --mac=str              MAC addresses of local NIC's
				- may appear up to 2 times
   -x, --include=str          Include only packets matching rule
				- prohibits the option 'exclude'
   -X, --exclude=str          Exclude any packet matching this rule
				- prohibits the option 'include'
   -P, --pid                  Print the PID of tcpbridge at startup
   -v, --verbose              Print decoded packets via tcpdump to STDOUT
   -A, --decode=str           Arguments passed to tcpdump decoder
				- requires the option 'verbose'
   -V, --version              Print version information
   -h, --less-help            Display less usage information and exit
   -w, --suppress-warnings    suppress printing warning messages
Version, usage and configuration options:
   -H, --help                 display extended usage information and exit
   -!, --more-help            extended usage information passed thru pager
       --save-opts[=arg]      save the option state to a config file
       --load-opts=str        load options from a config file
				- disabled as '--no-load-opts'
				- may appear multiple times
Options are specified by doubled hyphens and their name or by a single
hyphen and the flag character.
tcpbridge is a tool for selectively bridging network traffic across two
interfaces and optionally modifying the packets in between
The following option preset mechanisms are supported:
 - reading file /usr/bin/.tcpbridgerc
The basic operation of tcpbridge is to be a network bridge between two
subnets.  All packets received on one interface are sent via the other.
Optionally, packets can be edited in a variety of ways according to your
needs.
For more details, please see the Tcpreplay Manual at:
http://tcpreplay.appneta.com
Please send bug reports to:  <
[email protected]
>
```

### `tcpcapinfo`

> 官方示例调用：`tcpcapinfo --help`

```text
root@kali:~# tcpcapinfo --help
tcpcapinfo (Tcpreplay Suite) - Pcap file dissector for debugging broken pcap files
Usage:  tcpcapinfo [ -<flag> [<val>] | --<name>[{=| }<val>] ]... <pcap_file(s)>
   -d, --dbug=num             Enable debugging output
				- it must be in the range:
				  0 to 5
   -V, --version              Print version information
   -H, --help                 display extended usage information and exit
   -!, --more-help            extended usage information passed thru pager
Options are specified by doubled hyphens and their name or by a single
hyphen and the flag character.
tcpcapinfo is a tool for decoding the structure of a pcap(3) file with a
focus on finding broken pcap files and determining how two related pcap
files might differ.
tcpcapinfo will first print out the pcap_file_header_t in human readable
form followed by a per-packet summary including the pcap_pkthdr_t and
simple checksum value of the packet.
Please send bug reports to:  <
[email protected]
>
```

### `tcpliveplay`

> 官方示例调用：`tcpliveplay --help`

```text
root@kali:~# tcpliveplay --help
tcpliveplay (tcpliveplay) - Replays network traffic stored in a pcap file on live networks using new TCP connections
Usage:  tcpliveplay [ -<flag> [<val>] | --<name>[{=| }<val>] ]... \
		<eth0/eth1> <file.pcap> <Destination IP [1.2.3.4]> <Destination mac [0a:1b:2c:3d:4e:5f]> <'random' dst port OR specify dport #>
   -d, --dbug=num             Enable debugging output
				- it must be in the range:
				  0 to 5
   -V, --version              Print version information
   -h, --less-help            Display less usage information and exit
   -H, --help                 display extended usage information and exit
   -!, --more-help            extended usage information passed thru pager
       --save-opts[=arg]      save the option state to a config file
       --load-opts=str        load options from a config file
				- disabled as '--no-load-opts'
				- may appear multiple times
Options are specified by doubled hyphens and their name or by a single
hyphen and the flag character.
This program, 'tcpliveplay' replays a captured set of packets using new TCP
connections with the captured TCP payloads against a remote host in order
to do comprehensive vulnerability testing.
The following option preset mechanisms are supported:
 - reading file /usr/bin/.tcpliveplayrc
The basic operation of tcpliveplay is it rewrites the given pcap file in a
scheduled event format and responds with the appropriate packet if the
remote host meets tcp protocal's SEQ/ACK expectation.  Once expectations
are met, then the local packets are sent with the same payload except with
new tcp SEQ & ACK numbers meeting the response from the remote hose.
The input pcap file are rewritten to start at the first encounter of the
SYN packet for correct operation making this packet be the first action in
the event schedule of local host doing the replay.
For more details, please see the Tcpreplay Manual at:
http://tcpreplay.appneta.com
```

### `tcpprep`

> 官方示例调用：`tcpprep --help`

```text
root@kali:~# tcpprep --help
tcpprep (tcpprep) - Create a tcpreplay cache cache file from a pcap file.
Usage:  tcpprep [ -<flag> [<val>] | --<name>[{=| }<val>] ]...
   -d, --dbug=num             Enable debugging output
				- it must be in the range:
				  0 to 5
   -a, --auto=str             Auto-split mode
				- prohibits these options:
				cidr
				port
				regex
				mac
   -c, --cidr=str             CIDR-split mode
				- prohibits these options:
				auto
				port
				regex
				mac
   -r, --regex=str            Regex-split mode
				- prohibits these options:
				auto
				port
				cidr
				mac
   -p, --port                 Port-split mode
				- prohibits these options:
				auto
				regex
				cidr
				mac
   -e, --mac=str              Source MAC split mode
				- prohibits these options:
				auto
				regex
				cidr
				port
       --reverse              Matches to be client instead of server
   -C, --comment=str          Embedded cache file comment
       --no-arg-comment       Do not embed any cache file comment
   -x, --include=str          Include only packets matching rule
				- prohibits the option 'exclude'
   -X, --exclude=str          Exclude any packet matching this rule
				- prohibits the option 'include'
   -o, --cachefile=str        Output cache file
   -i, --pcap=str             Input pcap file to process
   -P, --print-comment=str    Print embedded comment in the specified cache file
   -I, --print-info=str       Print basic info from the specified cache file
   -S, --print-stats=str      Print statistical information about the specified cache file
   -s, --services=str         Load services file for server ports
				- requires the option 'port'
   -N, --nonip                Send non-IP traffic out server interface
   -R, --ratio=str            Ratio of client to server packets
				- requires the option 'auto'
   -m, --minmask=num          Minimum network mask length in auto mode
				- requires the option 'auto'
				- it must be in the range:
				  0 to 32
   -M, --maxmask=num          Maximum network mask length in auto mode
				- requires the option 'auto'
				- it must be in the range:
				  0 to 32
   -v, --verbose              Print decoded packets via tcpdump to STDOUT
   -A, --decode=str           Arguments passed to tcpdump decoder
				- requires the option 'verbose'
   -V, --version              Print version information
   -h, --less-help            Display less usage information and exit
   -w, --suppress-warnings    suppress printing warning messages
   -H, --help                 display extended usage information and exit
   -!, --more-help            extended usage information passed thru pager
       --save-opts[=arg]      save the option state to a config file
       --load-opts=str        load options from a config file
				- disabled as '--no-load-opts'
				- may appear multiple times
Options are specified by doubled hyphens and their name or by a single
hyphen and the flag character.
tcpprep is a 'pcap(3)' file pre-processor which creates a cache file which
provides "rules" for 'tcprewrite(1)' and 'tcpreplay(1)' on how to process
and send packets.
The following option preset mechanisms are supported:
 - reading file /usr/bin/.tcppreprc
The basic operation of tcpreplay is to resend all packets from the input
file(s) out a single file.  Tcpprep processes a pcap file and applies a set
of user-specified rules to create a cache file which tells tcpreplay
whether or not to send each packet and which interface the packet should be
sent out of.
For more details, please see the Tcpreplay Manual at:
http://tcpreplay.appneta.com
Please send bug reports to:  <
[email protected]
>
```

### `tcpreplay`

> 官方示例调用：`tcpreplay --help`

```text
root@kali:~# tcpreplay --help
tcpreplay (tcpreplay) - Replay network traffic stored in pcap files
Usage:  tcpreplay [ -<flag> [<val>] | --<name>[{=| }<val>] ]... \
		<pcap_file(s)> | <pcap_dir(s)>
   -d, --dbug=num             Enable debugging output
				- it must be in the range:
				  0 to 5
   -q, --quiet                Quiet mode
   -T, --timer=str            Select packet timing mode: select, ioport, gtod, nano
       --maxsleep=num         Sleep for no more then X milliseconds between packets
   -v, --verbose              Print decoded packets via tcpdump to STDOUT
   -A, --decode=str           Arguments passed to tcpdump decoder
				- requires the option 'verbose'
   -K, --preload-pcap         Preloads packets into RAM before sending
   -c, --cachefile=str        Split traffic via a tcpprep cache file
				- requires the option 'intf2'
				-- and prohibits the option 'dualfile'
   -2, --dualfile             Replay two files at a time from a network tap
				- requires the option 'intf2'
				-- and prohibits the option 'cachefile'
   -i, --intf1=str            Client to server/RX/primary traffic output interface
   -I, --intf2=str            Server to client/TX/secondary traffic output interface
   -w, --write=str            Pcap file to receive traffic outputs
				- prohibits the option 'intf2'
				- an alternate for 'intf1'
       --include=str          Send only selected packet numbers
				- prohibits the option 'exclude'
       --exclude=str          Send all but selected packet numbers
				- prohibits the option 'include'
       --listnics             List available network interfaces and exit
   -l, --loop=num             Loop through the capture file X times
				- it must be in the range:
				  greater than or equal to 0
       --loopdelay-ms=num     Delay between loops in milliseconds
				- requires the option 'loop'
				-- and prohibits the option 'loopdelay-ns'
				- it must be in the range:
				  greater than or equal to 0
       --loopdelay-ns=num     Delay between loops in nanoseconds
				- requires the option 'loop'
				-- and prohibits the option 'loopdelay-ms'
				- it must be in the range:
				  greater than or equal to 0
       --pktlen               Override the snaplen and use the actual packet len
   -L, --limit=num            Limit the number of packets to send
				- it must be in the range:
				  greater than or equal to 1
       --duration=num         Limit the number of seconds to send
				- it must be in the range:
				  greater than or equal to 1
   -x, --multiplier=str       Modify replay speed to a given multiple
				- prohibits these options:
				pps
				mbps
				oneatatime
				topspeed
   -p, --pps=str              Replay packets at a given packets/sec
				- prohibits these options:
				multiplier
				mbps
				oneatatime
				topspeed
   -M, --mbps=str             Replay packets at a given Mbps
				- prohibits these options:
				multiplier
				pps
				oneatatime
				topspeed
   -t, --topspeed             Replay packets as fast as possible
				- prohibits these options:
				mbps
				multiplier
				pps
				oneatatime
   -o, --oneatatime           Replay one packet at a time for each user input
				- prohibits these options:
				mbps
				pps
				multiplier
				topspeed
       --pps-multi=num        Number of packets to send for each time interval
				- requires the option 'pps'
				- it must be in the range:
				  greater than or equal to 1
       --unique-ip            Modify IP addresses each loop iteration to generate unique flows
				- requires the option 'loop'
       --unique-ip-loops=str  Number of times to loop before assigning new unique ip
				- requires the option 'unique-ip'
       --no-flow-stats        Suppress printing and tracking flow count, rates and expirations
       --flow-expiry=num      Number of inactive seconds before a flow is considered expired
				- prohibits the option 'no-flow-stats'
				- it must be in the range:
				  greater than or equal to 0
   -P, --pid                  Print the PID of tcpreplay at startup
       --stats=num            Print statistics every X seconds, or every loop if '0'
				- it must be in the range:
				  greater than or equal to 0
   -W, --suppress-warnings    suppress printing warning messages
   -V, --version              Print version information
   -h, --less-help            Display less usage information and exit
   -H, --help                 display extended usage information and exit
   -!, --more-help            extended usage information passed thru pager
       --save-opts[=arg]      save the option state to a config file
       --load-opts=str        load options from a config file
				- disabled as '--no-load-opts'
				- may appear multiple times
Options are specified by doubled hyphens and their name or by a single
hyphen and the flag character.
tcpreplay is a tool for replaying network traffic from files saved with
tcpdump or other tools which write pcap(3) files.
The following option preset mechanisms are supported:
 - reading file /usr/bin/.tcpreplayrc
The basic operation of tcpreplay is to resend all packets from the input
file(s) at the speed at which they were recorded, or a specified data rate,
up to as fast as the hardware is capable.
Optionally, the traffic can be split between two interfaces, written to
files, filtered and edited in various ways, providing the means to test
firewalls, NIDS and other network devices.
For more details, please see the Tcpreplay Manual at:
http://tcpreplay.appneta.com
Please send bug reports to:  <
[email protected]
>
```

### `tcpreplay-edit`

> 官方示例调用：`tcpreplay-edit --help`

```text
root@kali:~# tcpreplay-edit --help
tcpreplay (tcpreplay) - Replay network traffic stored in pcap files
Usage:  tcpreplay-edit [ -<flag> [<val>] | --<name>[{=| }<val>] ]... \
		<pcap_file(s)> | <pcap_dir(s)>
:
   -r, --portmap=str          Rewrite TCP/UDP ports
				- may appear up to 9999 times
   -s, --seed=num             Randomize src/dst IPv4/v6 addresses w/ given seed
				- prohibits the option 'fuzz-seed'
   -N, --pnat=str             Rewrite IPv4/v6 addresses using pseudo-NAT
				- prohibits the option 'srcipmap'
				- may appear up to 2 times
   -S, --srcipmap=str         Rewrite source IPv4/v6 addresses using pseudo-NAT
				- prohibits the option 'pnat'
   -D, --dstipmap=str         Rewrite destination IPv4/v6 addresses using pseudo-NAT
				- prohibits the option 'pnat'
   -e, --endpoints=str        Rewrite IP addresses to be between two endpoints
				- requires the option 'cachefile'
       --tcp-sequence=num     Change TCP Sequence (and ACK) numbers /w given seed
				- it must be in the range:
				  greater than or equal to 1
   -b, --skipbroadcast        Skip rewriting broadcast/multicast IPv4/v6 addresses
   -C, --fixcsum              Force recalculation of IPv4/TCP/UDP header checksums
       --fixhdrlen            Alter IP/TCP header len to match packet length
   -m, --mtu=num              Override default MTU length (1500 bytes)
				- it must be in the range:
				  1 to 262144
       --mtu-trunc            Truncate packets larger then specified MTU
   -E, --efcs                 Remove Ethernet checksums (FCS) from end of frames
       --ttl=str              Modify the IPv4/v6 TTL/Hop Limit
       --tos=num              Set the IPv4 TOS/DiffServ/ECN byte
				- it must be in the range:
				  0 to 255
       --tclass=num           Set the IPv6 Traffic Class byte
				- it must be in the range:
				  0 to 255
       --flowlabel=num        Set the IPv6 Flow Label
				- it must be in the range:
				  0 to 1048575
   -F, --fixlen=str           Pad or truncate packet data to match header length
       --fuzz-seed=num        Fuzz 1 in X packets.  Edit bytes, length, or emulate packet drop
				- it must be in the range:
				  greater than or equal to 0
       --fuzz-factor=num      Set the Fuzz 1 in X packet ratio (default 1 in 8 packets)
				- requires the option 'fuzz-seed'
				- it must be in the range:
				  greater than or equal to 1
       --skipl2broadcast      Skip rewriting broadcast/multicast Layer 2 addresses
       --dlt=str              Override output DLT encapsulation
       --enet-dmac=str        Override destination ethernet MAC addresses
       --enet-smac=str        Override source ethernet MAC addresses
       --enet-subsmac=str     Substitute MAC addresses
				- may appear up to 9999 times
       --enet-mac-seed=num    Randomize MAC addresses
				- prohibits these options:
				enet-smac
				enet-dmac
				enet-subsmac
       --enet-mac-seed-keep-bytes=num Randomize MAC addresses
				- requires the option 'enet-mac-seed'
				- it must be in the range:
				  1 to 6
       --enet-vlan=str        Specify ethernet 802.1q VLAN tag mode
       --enet-vlan-tag=num    Specify the new ethernet 802.1q VLAN tag value
				- requires the option 'enet-vlan'
				- it must be in the range:
				  0 to 4095
       --enet-vlan-cfi=num    Specify the ethernet 802.1q VLAN CFI value
				- requires the option 'enet-vlan'
				- it must be in the range:
				  0 to 1
       --enet-vlan-pri=num    Specify the ethernet 802.1q VLAN priority
				- requires the option 'enet-vlan'
				- it must be in the range:
				  0 to 7
       --enet-vlan-proto=str  Specify VLAN tag protocol 802.1q or 802.1ad
       --hdlc-control=num     Specify HDLC control value
       --hdlc-address=num     Specify HDLC address
       --user-dlt=num         Set output file DLT type
       --user-dlink=str       Rewrite Data-Link layer with user specified data
				- may appear up to 2 times
   -d, --dbug=num             Enable debugging output
				- it must be in the range:
				  0 to 5
   -q, --quiet                Quiet mode
   -T, --timer=str            Select packet timing mode: select, ioport, gtod, nano
       --maxsleep=num         Sleep for no more then X milliseconds between packets
   -v, --verbose              Print decoded packets via tcpdump to STDOUT
   -A, --decode=str           Arguments passed to tcpdump decoder
				- requires the option 'verbose'
   -K, --preload-pcap         Preloads packets into RAM before sending
   -c, --cachefile=str        Split traffic via a tcpprep cache file
				- requires the option 'intf2'
				-- and prohibits the option 'dualfile'
   -2, --dualfile             Replay two files at a time from a network tap
				- requires the option 'intf2'
				-- and prohibits the option 'cachefile'
   -i, --intf1=str            Client to server/RX/primary traffic output interface
   -I, --intf2=str            Server to client/TX/secondary traffic output interface
   -w, --write=str            Pcap file to receive traffic outputs
				- prohibits the option 'intf2'
				- an alternate for 'intf1'
       --include=str          Send only selected packet numbers
				- prohibits the option 'exclude'
       --exclude=str          Send all but selected packet numbers
				- prohibits the option 'include'
       --listnics             List available network interfaces and exit
   -l, --loop=num             Loop through the capture file X times
				- it must be in the range:
				  greater than or equal to 0
       --loopdelay-ms=num     Delay between loops in milliseconds
				- requires the option 'loop'
				-- and prohibits the option 'loopdelay-ns'
				- it must be in the range:
				  greater than or equal to 0
       --loopdelay-ns=num     Delay between loops in nanoseconds
				- requires the option 'loop'
				-- and prohibits the option 'loopdelay-ms'
				- it must be in the range:
				  greater than or equal to 0
       --pktlen               Override the snaplen and use the actual packet len
   -L, --limit=num            Limit the number of packets to send
				- it must be in the range:
				  greater than or equal to 1
       --duration=num         Limit the number of seconds to send
				- it must be in the range:
				  greater than or equal to 1
   -x, --multiplier=str       Modify replay speed to a given multiple
				- prohibits these options:
				pps
				mbps
				oneatatime
				topspeed
   -p, --pps=str              Replay packets at a given packets/sec
				- prohibits these options:
				multiplier
				mbps
				oneatatime
				topspeed
   -M, --mbps=str             Replay packets at a given Mbps
				- prohibits these options:
				multiplier
				pps
				oneatatime
				topspeed
   -t, --topspeed             Replay packets as fast as possible
				- prohibits these options:
				mbps
				multiplier
				pps
				oneatatime
   -o, --oneatatime           Replay one packet at a time for each user input
				- prohibits these options:
				mbps
				pps
				multiplier
				topspeed
       --pps-multi=num        Number of packets to send for each time interval
				- requires the option 'pps'
				- it must be in the range:
				  greater than or equal to 1
       --unique-ip            Modify IP addresses each loop iteration to generate unique flows
				- requires the option 'loop'
				-- and prohibits these options:
				seed
				fuzz-seed
       --unique-ip-loops=str  Number of times to loop before assigning new unique ip
				- requires the option 'unique-ip'
       --no-flow-stats        Suppress printing and tracking flow count, rates and expirations
       --flow-expiry=num      Number of inactive seconds before a flow is considered expired
				- prohibits the option 'no-flow-stats'
				- it must be in the range:
				  greater than or equal to 0
   -P, --pid                  Print the PID of tcpreplay at startup
       --stats=num            Print statistics every X seconds, or every loop if '0'
				- it must be in the range:
				  greater than or equal to 0
   -W, --suppress-warnings    suppress printing warning messages
   -V, --version              Print version information
   -h, --less-help            Display less usage information and exit
Version, usage and configuration options:
   -H, --help                 display extended usage information and exit
   -!, --more-help            extended usage information passed thru pager
       --save-opts[=arg]      save the option state to a config file
       --load-opts=str        load options from a config file
				- disabled as '--no-load-opts'
				- may appear multiple times
Options are specified by doubled hyphens and their name or by a single
hyphen and the flag character.
tcpreplay is a tool for replaying network traffic from files saved with
tcpdump or other tools which write pcap(3) files.
The following option preset mechanisms are supported:
 - reading file /usr/bin/.tcpreplayrc
The basic operation of tcpreplay is to resend all packets from the input
file(s) at the speed at which they were recorded, or a specified data rate,
up to as fast as the hardware is capable.
Optionally, the traffic can be split between two interfaces, written to
files, filtered and edited in various ways, providing the means to test
firewalls, NIDS and other network devices.
For more details, please see the Tcpreplay Manual at:
http://tcpreplay.appneta.com
Please send bug reports to:  <
[email protected]
>
```

### `tcprewrite`

> 官方示例调用：`tcprewrite --help`

```text
root@kali:~# tcprewrite --help
tcprewrite (tcprewrite) - Rewrite the packets in a pcap file.
Usage:  tcprewrite [ -<flag> [<val>] | --<name>[{=| }<val>] ]...
:
   -r, --portmap=str          Rewrite TCP/UDP ports
				- may appear up to 9999 times
   -s, --seed=num             Randomize src/dst IPv4/v6 addresses w/ given seed
				- prohibits the option 'fuzz-seed'
   -N, --pnat=str             Rewrite IPv4/v6 addresses using pseudo-NAT
				- prohibits the option 'srcipmap'
				- may appear up to 2 times
   -S, --srcipmap=str         Rewrite source IPv4/v6 addresses using pseudo-NAT
				- prohibits the option 'pnat'
   -D, --dstipmap=str         Rewrite destination IPv4/v6 addresses using pseudo-NAT
				- prohibits the option 'pnat'
   -e, --endpoints=str        Rewrite IP addresses to be between two endpoints
				- requires the option 'cachefile'
       --tcp-sequence=num     Change TCP Sequence (and ACK) numbers /w given seed
				- it must be in the range:
				  greater than or equal to 1
   -b, --skipbroadcast        Skip rewriting broadcast/multicast IPv4/v6 addresses
   -C, --fixcsum              Force recalculation of IPv4/TCP/UDP header checksums
       --fixhdrlen            Alter IP/TCP header len to match packet length
   -m, --mtu=num              Override default MTU length (1500 bytes)
				- it must be in the range:
				  1 to 262144
       --mtu-trunc            Truncate packets larger then specified MTU
   -E, --efcs                 Remove Ethernet checksums (FCS) from end of frames
       --ttl=str              Modify the IPv4/v6 TTL/Hop Limit
       --tos=num              Set the IPv4 TOS/DiffServ/ECN byte
				- it must be in the range:
				  0 to 255
       --tclass=num           Set the IPv6 Traffic Class byte
				- it must be in the range:
				  0 to 255
       --flowlabel=num        Set the IPv6 Flow Label
				- it must be in the range:
				  0 to 1048575
   -F, --fixlen=str           Pad or truncate packet data to match header length
       --fuzz-seed=num        Fuzz 1 in X packets.  Edit bytes, length, or emulate packet drop
				- it must be in the range:
				  greater than or equal to 0
       --fuzz-factor=num      Set the Fuzz 1 in X packet ratio (default 1 in 8 packets)
				- requires the option 'fuzz-seed'
				- it must be in the range:
				  greater than or equal to 1
       --skipl2broadcast      Skip rewriting broadcast/multicast Layer 2 addresses
       --dlt=str              Override output DLT encapsulation
       --enet-dmac=str        Override destination ethernet MAC addresses
       --enet-smac=str        Override source ethernet MAC addresses
       --enet-subsmac=str     Substitute MAC addresses
				- may appear up to 9999 times
       --enet-mac-seed=num    Randomize MAC addresses
				- prohibits these options:
				enet-smac
				enet-dmac
				enet-subsmac
       --enet-mac-seed-keep-bytes=num Randomize MAC addresses
				- requires the option 'enet-mac-seed'
				- it must be in the range:
				  1 to 6
       --enet-vlan=str        Specify ethernet 802.1q VLAN tag mode
       --enet-vlan-tag=num    Specify the new ethernet 802.1q VLAN tag value
				- requires the option 'enet-vlan'
				- it must be in the range:
				  0 to 4095
       --enet-vlan-cfi=num    Specify the ethernet 802.1q VLAN CFI value
				- requires the option 'enet-vlan'
				- it must be in the range:
				  0 to 1
       --enet-vlan-pri=num    Specify the ethernet 802.1q VLAN priority
				- requires the option 'enet-vlan'
				- it must be in the range:
				  0 to 7
       --enet-vlan-proto=str  Specify VLAN tag protocol 802.1q or 802.1ad
       --hdlc-control=num     Specify HDLC control value
       --hdlc-address=num     Specify HDLC address
       --user-dlt=num         Set output file DLT type
       --user-dlink=str       Rewrite Data-Link layer with user specified data
				- may appear up to 2 times
   -d, --dbug=num             Enable debugging output
				- it must be in the range:
				  0 to 5
   -i, --infile=str           Input pcap file to be processed
   -o, --outfile=str          Output pcap file
   -c, --cachefile=str        Split traffic via tcpprep cache file
   -v, --verbose              Print decoded packets via tcpdump to STDOUT
   -A, --decode=str           Arguments passed to tcpdump decoder
				- requires the option 'verbose'
       --fragroute=str        Parse fragroute configuration file
       --fragdir=str          Which flows to apply fragroute to: c2s, s2c, both
				- requires the option 'cachefile'
       --skip-soft-errors     Skip writing packets with soft errors
   -V, --version              Print version information
   -h, --less-help            Display less usage information and exit
   -w, --suppress-warnings    suppress printing warning messages
Version, usage and configuration options:
   -H, --help                 display extended usage information and exit
   -!, --more-help            extended usage information passed thru pager
       --save-opts[=arg]      save the option state to a config file
       --load-opts=str        load options from a config file
				- disabled as '--no-load-opts'
				- may appear multiple times
Options are specified by doubled hyphens and their name or by a single
hyphen and the flag character.
The following option preset mechanisms are supported:
 - reading file /usr/bin/.tcprewriterc
Tcprewrite is a tool to rewrite packets stored in 'pcap(3)' file format,
such as created by tools such as 'tcpdump(1)' and 'wireshark(1)'.  Once a
pcap file has had it's packets rewritten, they can be replayed back out on
the network using 'tcpreplay(1)'.
tcprewrite currently supports reading the following DLT types:
'DLT_C_HDLC' aka Cisco HDLC
'DLT_EN10MB' aka Ethernet
'DLT_LINUX_SLL' aka Linux Cooked Socket
'DLT_LINUX_SLL2' aka Linux Cooked Socket v2
'DLT_RAW' aka RAW IP
'DLT_NULL' aka BSD Loopback
'DLT_LOOP' aka OpenBSD Loopback
'DLT_IEEE802_11' aka 802.11a/b/g
'DLT_IEEE802_11_RADIO' aka 802.11a/b/g with Radiotap headers
'DLT_JUNIPER_ETHER' aka Juniper Encapsulated Ethernet
'DLT_PPP_SERIAL' aka PPP over Serial
Please see the --dlt option for supported DLT types for writing.
The packet editing features of tcprewrite which distinguish between
"client" and "server" traffic requires a tcpprep(1) cache file.
For more details, please see the Tcpreplay Manual at:
http://tcpreplay.appneta.com
Please send bug reports to:  <
[email protected]
>
Updated on: 2026-Aug-25
 Edit this page
tcpdump
testdisk
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install tcpreplay`，再执行 `tcpreplay --version` 2>/dev/null || `tcpreplay -V`
- [ ] **2.** **读官方帮助** —— `tcpreplay -h`，需要细节时 `man tcpreplay`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:  tcpbridge [ -<flag> [<val>] | --<name>[{=| }<val>] ]...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/tcpreplay/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/tcpreplay/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/tcpreplay/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
