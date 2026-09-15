# net-tools

> NET-3 networking toolkit This package includes the important tools for controlling the network subsystem of the Linux kernel. This includes arp, ifconfig, netstat, rarp, nameif and route. Additionally, this package contains utilities relat…

> **功能分类**：无线攻击 ｜ **Kali 包**：`net-tools` ｜ **官方文档**：<https://www.kali.org/tools/net-tools/>

## 1. 安装

```bash
sudo apt update
sudo apt install net-tools
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.10 |
| 架构 | any |
| 可执行命令 | `net-tools`、`arp`、`ifconfig`、`ipmaddr`、`iptunnel`、`mii-tool`、`nameif`、`netstat`、`plipconfig`、`rarp`、`route`、`slattach` |
| 依赖 | `libc6`、`libselinux1`、`arp` |
| 安装体积 | 917 KB |
| 官网 | <http://sourceforge.net/projects/net-tools/> |
| 源码仓库 | <https://salsa.debian.org/debian/net-tools> |
| 包追踪 | <https://pkg.kali.org/pkg/net-tools> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
net-tools -h          # 查看用法
man net-tools         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 12 个可执行命令，下面是官方页面内嵌的帮助原文。

### `arp`

> 官方示例调用：`arp -h`

```text
root@kali:~# arp -h
Usage:
  arp [-vn]  [<HW>] [-i <if>] [-a] [<hostname>]             <-Display ARP cache
  arp [-v]          [-i <if>] -d  <host> [pub]               <-Delete ARP entry
  arp [-vnD] [<HW>] [-i <if>] -f  [<filename>]            <-Add entry from file
  arp [-v]   [<HW>] [-i <if>] -s  <host> <hwaddr> [temp]            <-Add entry
  arp [-v]   [<HW>] [-i <if>] -Ds <host> <if> [netmask <nm>] pub          <-''-
        -a                       display (all) hosts in alternative (BSD) style
        -e                       display (all) hosts in default (Linux) style
        -s, --set                set a new ARP entry
        -d, --delete             delete a specified entry
        -v, --verbose            be verbose
        -n, --numeric            don't resolve names
        -i, --device             specify network interface (e.g. eth0)
        -D, --use-device         read <hwaddr> from given device
        -A, -p, --protocol       specify protocol family
        -f, --file               read new entries from file or from /etc/ethers
  <HW>=Use '-H <hw>' to specify hardware address type. Default: ether
  List of possible hardware types (which support ARP):
```

### `ifconfig`

> 官方示例调用：`ifconfig -h`

```text
root@kali:~# ifconfig -h
Usage:
  ifconfig [-a] [-v] [-s] <interface> [[<AF>] <address>]
  [add <address>[/<prefixlen>]]
  [del <address>[/<prefixlen>]]
  [[-]broadcast [<address>]]  [[-]pointopoint [<address>]]
  [netmask <address>]  [dstaddr <address>]  [tunnel <address>]
  [outfill <NN>] [keepalive <NN>]
  [hw <HW> <address>]  [mtu <NN>]
  [[-]trailers]  [[-]arp]  [[-]allmulti]
  [multicast]  [[-]promisc]
  [mem_start <NN>]  [io_addr <NN>]  [irq <NN>]  [media <type>]
  [txqueuelen <NN>]
  [name <newname>]
  [[-]dynamic]
  [up|down] ...
  <HW>=Hardware Type.
  List of possible hardware types:
  <AF>=Address family. Default: inet
  List of possible address families:
```

### `ipmaddr`

> 官方示例调用：`ipmaddr -h`

```text
root@kali:~# ipmaddr -h
Usage: ipmaddr [ add | del ] MULTIADDR dev STRING
       ipmaddr show [ dev STRING ] [ ipv4 | ipv6 | link | all ]
       ipmaddr -V | -version
```

### `iptunnel`

> 官方示例调用：`iptunnel -h`

```text
root@kali:~# iptunnel -h
Usage: iptunnel { add | change | del | show } [ NAME ]
          [ mode { ipip | gre | sit } ] [ remote ADDR ] [ local ADDR ]
          [ [i|o]seq ] [ [i|o]key KEY ] [ [i|o]csum ]
          [ ttl TTL ] [ tos TOS ] [ nopmtudisc ] [ dev PHYS_DEV ]
       iptunnel -V | --version
Where: NAME := STRING
       ADDR := { IP_ADDRESS | any }
       TOS  := { NUMBER | inherit }
       TTL  := { 1..255 | inherit }
       KEY  := { DOTTED_QUAD | NUMBER }
```

### `mii-tool`

> 官方示例调用：`mii-tool -h`

```text
root@kali:~# mii-tool -h
mii-tool: invalid option -- 'h'
usage: mii-tool [-VvRrwl] [-A media,... | -F media] [-p addr] <interface ...>
       -V, --version               display version information
       -v, --verbose               more verbose output
       -R, --reset                 reset MII to poweron state
       -r, --restart               restart autonegotiation
       -w, --watch                 monitor for link status changes
       -l, --log                   with -w, write events to syslog
       -A, --advertise=media,...   advertise only specified media
       -F, --force=media           force specified media technology
       -p, --phy=addr              set PHY (MII address) to report
media: 1000baseTx-HD, 1000baseTx-FD,
       100baseT4, 100baseTx-FD, 100baseTx-HD,
       10baseT-FD, 10baseT-HD,
       (to advertise both HD and FD) 1000baseTx, 100baseTx, 10baseT
```

### `nameif`

> 官方示例调用：`nameif -h`

```text
root@kali:~# nameif -h
usage: nameif [-c configurationfile] [-s] {ifname macaddress}
```

### `netstat`

> 官方示例调用：`netstat -h`

```text
root@kali:~# netstat -h
usage: netstat [-vWeenNcCF] [<Af>] -r         netstat {-V|--version|-h|--help}
       netstat [-vWnNcaeol] [<Socket> ...]
       netstat { [-vWeenNac] -i | [-cnNe] -M | -s [-6tuw] }
        -r, --route              display routing table
        -i, --interfaces         display interface table
        -g, --groups             display multicast group memberships
        -s, --statistics         display networking statistics (like SNMP)
        -M, --masquerade         display masqueraded connections
        -v, --verbose            be verbose
        -W, --wide               don't truncate IP addresses
        -n, --numeric            don't resolve names
        --numeric-hosts          don't resolve host names
        --numeric-ports          don't resolve port names
        --numeric-users          don't resolve user names
        -N, --symbolic           resolve hardware names
        -e, --extend             display other/more information
        -p, --programs           display PID/Program name for sockets
        -o, --timers             display timers
        -c, --continuous         continuous listing
        -l, --listening          display listening server sockets
        -a, --all                display all sockets (default: connected)
        -F, --fib                display Forwarding Information Base (default)
        -C, --cache              display routing cache instead of FIB
        -Z, --context            display SELinux security context for sockets
  <Socket>={-t|--tcp} {-u|--udp} {-U|--udplite} {-S|--sctp} {-w|--raw}
           {-x|--unix} --ax25 --ipx --netrom
  <AF>=Use '-6|-4' or '-A <af>' or '--<af>'; default: inet
  List of possible address families (which support routing):
```

### `plipconfig`

> 官方示例调用：`plipconfig -h`

```text
root@kali:~# plipconfig -h
Usage: plipconfig interface [nibble NN] [trigger NN]
       plipconfig -V | --version
       plipconfig -h | --help
```

### `rarp`

> 官方示例调用：`rarp -h`

```text
root@kali:~# rarp -h
Usage: rarp -a                               list entries in cache.
       rarp -d <hostname>                    delete entry from cache.
       rarp [<HW>] -s <hostname> <hwaddr>    add entry to cache.
       rarp -f                               add entries from /etc/ethers.
       rarp -V                               display program version.
  <HW>=Use '-H <hw>' to specify hardware address type. Default: ether
  List of possible hardware types (which support ARP):
```

### `route`

> 官方示例调用：`route -h`

```text
root@kali:~# route -h
Usage: route [-nNvee] [-FC] [<AF>]           List kernel routing tables
       route [-v] [-FC] {add|del|flush} ...  Modify routing table for AF.
       route {-h|--help} [<AF>]              Detailed usage syntax for specified AF.
       route {-V|--version}                  Display version/author and exit.
        -v, --verbose            be verbose
        -n, --numeric            don't resolve names
        -e, --extend             display other/more information
        -F, --fib                display Forwarding Information Base (default)
        -C, --cache              display routing cache instead of FIB
  <AF>=Use -4, -6, '-A <af>' or '--<af>'; default: inet
  List of possible address families (which support routing):
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install net-tools`，再执行 `net-tools --version` 2>/dev/null || `net-tools -V`
- [ ] **2.** **读官方帮助** —— `net-tools -h`，需要细节时 `man net-tools`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/net-tools/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[arp-scan](../../tools/tutorials/01-信息搜集/arp-scan.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/net-tools/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/net-tools/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
