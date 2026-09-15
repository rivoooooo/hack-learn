# ubertooth

> 2.4 GHz wireless development platform for Bluetooth experimentation Project Ubertooth is an open source wireless development platform suitable for Bluetooth experimentation. This package contains everything necessary to use the hardware do…

> **功能分类**：无线攻击 ｜ **Kali 包**：`ubertooth` ｜ **官方文档**：<https://www.kali.org/tools/ubertooth/>

## 1. 安装

```bash
sudo apt update
sudo apt install ubertooth
```

| 项目 | 内容 |
|------|------|
| 版本 | 2020.12.R1 |
| 架构 | any |
| 可执行命令 | `libubertooth-dev`、`libubertooth1`、`ubertooth`、`ubertooth-afh`、`ubertooth-btbr`、`ubertooth-btle`、`ubertooth-debug`、`ubertooth-dfu`、`ubertooth-ducky`、`ubertooth-dump`、`ubertooth-ego`、`ubertooth-follow`、`ubertooth-rx`、`ubertooth-scan`、`ubertooth-specan`、`ubertooth-specan-ui`、`ubertooth-util`、`ubertooth-firmware`、`ubertooth-firmware-source` |
| 依赖 | `libbluetooth3`、`libbtbb1`、`libc6`、`libubertooth1`、`libusb-1.0-0`、`python3`、`python3-numpy`、`ubertooth-afh` |
| 安装体积 | 333 KB |
| 官网 | <http://ubertooth.sourceforge.net/> |
| 源码仓库 | <https://salsa.debian.org/debian/ubertooth> |
| 包追踪 | <https://pkg.kali.org/pkg/ubertooth> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libubertooth-dev -h          # 查看用法
man libubertooth-dev         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 19 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ubertooth-afh`

官方给出的调用示例：`ubertooth-afh -h`

```text
root@kali:~# ubertooth-afh -h
ubertooth-afh - passive detection of the AFH channel map
Determine the AFH map for piconet ??:??:22:44:66:88:
    ubertooth-afh -u 22 -l 446688
Main options:
	-l <LAP> LAP of target piconet (3 bytes / 6 hex digits)
	-u <UAP> UAP of target piconet (1 byte / 2 hex digits)
	-m <int> threshold for channel removal (default: 5)
	-r print AFH channel map once every second (default: print on update)
Other options
	-t <seconds> timeout for initial AFH map detection (not required)
	-e maximum access code errors (default: 2, range: 0-4)
	-V print version information
	-U <0-7> set ubertooth device to use
```

### `ubertooth-btle`

官方给出的调用示例：`ubertooth-btle -h`

```text
root@kali:~# ubertooth-btle -h
ubertooth-btle - passive Bluetooth Low Energy monitoring
Usage:
	-h this help
    Major modes:
	-f follow connections
	-n don't follow, only print advertisements
	-p promiscuous: sniff active connections
	-a[address] get/set access address (example: -a8e89bed6)
	-s<address> faux slave mode, using MAC addr (example: -s22:44:66:88:aa:cc)
	-t<address> set connection following target (example: -t22:44:66:88:aa:cc/48)
	-tnone unset connection following target
    Interference (use with -f or -p):
	-i interfere with one connection and return to idle
	-I interfere continuously
    Data source:
	-U<0-7> set ubertooth device to use
    Misc:
	-r<filename> capture packets to PCAPNG file
	-q<filename> capture packets to PCAP file (DLT_BLUETOOTH_LE_LL_WITH_PHDR)
	-c<filename> capture packets to PCAP file (DLT_PPI + DLT_BLUETOOTH_LE_LL)
	-A<index> advertising channel index (default 37)
	-v[01] verify CRC mode, get status or enable/disable
	-x<n> allow n access address offenses (default 32)
If an input file is not specified, an Ubertooth device is used for live capture.
In get/set mode no capture occurs.
```

### `ubertooth-debug`

官方给出的调用示例：`ubertooth-debug -h`

```text
root@kali:~# ubertooth-debug -h
ubertooth-debug - command line utility for debugging Ubertooth One
Usage:
	-h this message
	-r <reg>[,<reg>[,...]] read the contents of CC2400 register(s)
	-r <start>-<end> read a consecutive set of CC2400 register(s)
	-U<0-7> set ubertooth device to use
	-v<0-2> verbosity (default=1)
```

### `ubertooth-dfu`

官方给出的调用示例：`ubertooth-dfu -h`

```text
root@kali:~# ubertooth-dfu -h
ubertooth-dfu - Ubertooth firmware update tool
To update firmware, run:
	ubertooth-dfu -d bluetooth_rxtx.dfu -r
Usage:
	-u <filename> upload - read firmware from device
	-d <filename> download - write DFU file to device
	-r reset Ubertooth after other operations complete
Miscellaneous:
	-s <filename> add DFU suffix to binary firmware file
	-U <0-7> set ubertooth device to use
```

### `ubertooth-ducky`

官方给出的调用示例：`ubertooth-ducky -h`

```text
root@kali:~# ubertooth-ducky -h
ubertooth-ducky - make an Uberducky quack like a USB Rubber Ducky
Usage:
	-q [uuid] quack!
	-b signal Uberducky to enter bootloader
	-A <index> advertising channel index (default: 38)
	-a <BD ADDR> Bluetooth address (default: random)
	-h this help
For more information on Uberducky, visit:
https://github.com/mikeryan/uberducky
```

### `ubertooth-dump`

官方给出的调用示例：`ubertooth-dump -h`

```text
root@kali:~# ubertooth-dump -h
ubertooth-dump - output a continuous stream of received bits
Usage:
	-h this help
	-b only dump received bitstream (GnuRadio style)
	-c classic modulation
	-l LE modulation
	-U<0-7> set ubertooth device to use
	-d filename
This program sends binary data to stdout.  You probably don't want to
run it from a terminal without redirecting the output.
```

### `ubertooth-ego`

官方给出的调用示例：`ubertooth-ego -h`

```text
root@kali:~# ubertooth-ego -h
ubertooth-ego - Yuneec E-GO skateboard sniffing
Usage:
	-h this help
    Major modes:
	-f follow connections
	-r continuous rx on a single channel
	-i interfere
    Options:
	-c <2402-2480> set channel in MHz (for continuous rx)
	-l <1-48> capture length (default: 18)
	-a <access_code> access code (default: 630f9ffe)
```

### `ubertooth-follow`

官方给出的调用示例：`ubertooth-follow -h`

```text
root@kali:~# ubertooth-follow -h
ubertooth-follow - active(bluez) CLK discovery and follow for a particular UAP/LAP
Usage:
	-h this help
	-l<LAP> (in hexadecimal)
	-u<UAP> (in hexadecimal)
	-U<0-7> set ubertooth device to use
	-r<filename> capture packets to PCAPNG file
	-q<filename> capture packets to PCAP file
	-e max_ac_errors
	-d filename
	-a Enable AFH
	-b Bluetooth device (hci0)
	-w USB delay in 625us timeslots (default:5)
LAP and UAP are both required, if not given they are read from the local device, in some cases this may give the incorrect address.
```

### `ubertooth-rx`

官方给出的调用示例：`ubertooth-rx -h`

```text
root@kali:~# ubertooth-rx -h
ubertooth-rx - passive Classic Bluetooth discovery/decode
Example usage:
	ubertooth-rx -- sniff for all LAPs
	ubertooth-rx -l <lap> -- calculate UAP for a given LAP
	ubertooth-rx -l <lap> -u <uap> -- calculate clock and follow piconet
	ubertooth-rx -z -t 20 -- survey mode: discover all LAPs+UAPs for 20 seconds
Major modes:
	-l <LAP> to decode (6 hex) - if not specified sniff all LAPs
	-u <UAP> to decode (2 hex) - if not specified calculate UAP (requires LAP)
	-z Survey mode - discover and list piconets (implies -s, interrupt with ctrl-C)
	-i <filename> input file - if not specified use Ubertooth for live capture
Configuration:
	-c <BT Channel> set a fixed bluetooth channel [Default: 39]
	-e max_ac_errors (default: 2, range: 0-4)
	-t <SECONDS> sniff timeout - 0 means no timeout [Default: 0]
Output options:
	-r<filename> capture packets to PcapNG file
	-q<filename> capture packets to PCAP file
	-d<filename> dump packets to binary file
Miscellaneous:
	-V print version information
	-U <0-7> set ubertooth device to use
```

### `ubertooth-scan`

官方给出的调用示例：`ubertooth-scan -h`

```text
root@kali:~# ubertooth-scan -h
ubertooth-scan - active(Bluez) device scan and inquiry supported by Ubertooth
This tool uses a normal Bluetooth dongle to perform Inquiry Scans and
Extended Inquiry scans of Bluetooth devices. It uses Ubertooth to
discover undiscoverable devices and can use BlueZ to scan for
discoverable devices.
Usage:
    ubertooth-scan
        Use Ubertooth to discover devices and perform Inquiry Scan.
    ubertooth-scan -s -x
        Use BlueZ and Ubertooth to discover devices and perform Inquiry Scan
        and Extended Inquiry Scan.
Options:
	-s hci Scan - use BlueZ to scan for discoverable devices
	-x eXtended scan - retrieve additional information about target devices
	-t scan Time (seconds) - length of time to sniff packets. [Default: 20s]
	-e max_ac_errors (default: 2, range: 0-4)
	-b Bluetooth device (hci0)
	-U<0-7> set Ubertooth device to use
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install ubertooth`，再执行 `libubertooth-dev --version` 2>/dev/null || `libubertooth-dev -V`
- [ ] **2.** **读官方帮助** —— `libubertooth-dev -h`，需要细节时 `man libubertooth-dev`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ubertooth/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ubertooth/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ubertooth/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
