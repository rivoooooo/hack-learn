# 按包速查：无线攻击（wireless）

> 共 **47** 个包 · 数据来源 <https://www.kali.org/tools/all-tools/>

返回 [工具总览](../index.md) · [全量清单](all-tools.md) · [按功能分类](../index.md#功能分类导航)

---

### aircrack-ng

Wireless WEP/WPA cracking utilities aircrack-ng is an 802.11a/b/g WEP/WPA cracking program that can recover a 40-bit, 104-bit, 256-bit or 512-bit WEP key once enough encrypted packets have been gathered. Also it can attack WPA1/2 networks with some advanced methods or simply by brute force. It implements the standard FMS attack along with some optimizations,

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、漏洞利用、嗅探与欺骗、社会工程、Top 10 常用、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/aircrack-ng/> |
| 版本 | 1.7 |
| 包 / 命令 | `aircrack-ng`、`airbase-ng`、`airdecap-ng`、`airdecloak-ng`、`aireplay-ng`、`airmon-ng`、`airodump-ng`、`airodump-ng-oui-update`、`airolib-ng`、`airserv-ng`、`airtun-ng`、`airventriloquist-ng`、`besside-ng`、`besside-ng-crawler`、`buddy-ng`、`dcrack`、`easside-ng`、`ivstools`、`kstats`、`makeivs-ng`、`packetforge-ng`、`tkiptun-ng`、`wesside-ng`、`wpaclean`、`airgraph-ng`、`airodump-join` |
| 安装 | `sudo apt install aircrack-ng` |
| 占用空间 | 2.47 MB |
| 依赖 | `ethtool`、`hwloc`、`iw`、`libc6`、`libgcc-s1`、`libhwloc15`、`libnl-3-200`、`libnl-genl-3-200`、`libpcap0.8t64`、`libpcre2-8-0`、`libsqlite3-0`、`libssl3t64` 等 |
| 官网 | <https://www.aircrack-ng.org/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/aircrack-ng> |

### airgeddon

Multi-use bash script for Linux systems to audit wireless networks airgeddon is a menu driven 3rd party tools wrapper to audit wireless networks with many features.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/airgeddon/> |
| 版本 | 12.01 |
| 包 / 命令 | `airgeddon` |
| 安装 | `sudo apt install airgeddon` |
| 占用空间 | 5.07 MB |
| 依赖 | `aircrack-ng`、`bash`、`gawk`、`iproute2`、`iw`、`pciutils`、`procps`、`tmux`、`xterm`、`airgeddon` |
| 官网 | <https://github.com/v1s1t0r1sh3r3/airgeddon> |
| 源码 | <https://gitlab.com/kalilinux/packages/airgeddon> |

### asleap

A tool for exploiting Cisco LEAP networks Demonstrates a serious deficiency in proprietary Cisco LEAP networks.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/asleap/> |
| 版本 | 2.3~git20201128.254acab |
| 包 / 命令 | `asleap`、`genkeys` |
| 安装 | `sudo apt install asleap` |
| 占用空间 | 235 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`asleap` |
| 官网 | <https://www.willhackforsushi.com/> |
| 源码 | <https://gitlab.com/kalilinux/packages/asleap> |

### blue-hydra

Bluetooth device discovery service BlueHydra is a Bluetooth device discovery service built on top of the bluez library. BlueHydra makes use of ubertooth where available and attempts to track both classic and low energy (LE) bluetooth devices over time.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 蓝牙、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/blue-hydra/> |
| 版本 | 1.9.21 |
| 包 / 命令 | `blue-hydra`、`blue_hydra`、`rfkill-reset`、`test-discovery` |
| 安装 | `sudo apt install blue-hydra` |
| 占用空间 | 8.98 MB |
| 依赖 | `bluez-test-scripts`、`libc6`、`libruby3.3`、`libsqlite3-0`、`python3`、`ruby`、`blue_hydra` |
| 官网 | <https://github.com/ZeroChaos-/blue_hydra> |
| 源码 | <https://gitlab.com/kalilinux/packages/blue-hydra> |

### bluelog

Bluetooth scanner and logger Bluelog is a Bluetooth scanner designed to tell you how many discoverable devices there are in an area as quickly as possible. It is intended to be used as a site survey tool, identifying the number of possible Bluetooth targets there are in the surrounding environment.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 蓝牙、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/bluelog/> |
| 版本 | 1.1.2 |
| 包 / 命令 | `bluelog` |
| 安装 | `sudo apt install bluelog` |
| 占用空间 | 198 KB |
| 依赖 | `bluez`、`ieee-data`、`libbluetooth-dev`、`libbluetooth3`、`libc6`、`bluelog` |
| 官网 | <http://www.digifail.com/software/bluelog.shtml> |
| 源码 | <https://gitlab.com/kalilinux/packages/bluelog> |

### blueranger

Simple Bash script to locate Bluetooth devices BlueRanger is a simple Bash script which uses Link Quality to locate Bluetooth device radios. It sends l2cap (Bluetooth) pings to create a connection between Bluetooth interfaces, since most devices allow pings without any authentication or

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 蓝牙、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/blueranger/> |
| 版本 | 0.1 |
| 包 / 命令 | `blueranger` |
| 安装 | `sudo apt install blueranger` |
| 占用空间 | 13 KB |
| 依赖 | `bluez`、`blueranger` |
| 官网 | <http://www.hackfromacave.com/projects/blueranger.html> |
| 源码 | <https://gitlab.com/kalilinux/packages/blueranger> |

### bluesnarfer

Bluesnarfing utility A bluetooth bluesnarfing utility

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 蓝牙、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/bluesnarfer/> |
| 版本 | 0.1 |
| 包 / 命令 | `bluesnarfer` |
| 安装 | `sudo apt install bluesnarfer` |
| 占用空间 | 30 KB |
| 依赖 | `bluez`、`libbluetooth3`、`libc6`、`bluesnarfer` |
| 官网 | <http://www.alighieri.org/> |
| 源码 | <https://gitlab.com/kalilinux/packages/bluesnarfer> |

### bluez

bluez Bluetooth tools and daemons This package contains tools and system daemons for using Bluetooth devices. BlueZ is the official Linux Bluetooth protocol stack. It is an Open Source project distributed under GNU General Public License (GPL).

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 蓝牙、RFID / NFC、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/bluez/> |
| 版本 | 5.87 |
| 包 / 命令 | `bluetooth`、`bluez`、`bluemoon`、`bluetoothctl`、`bluetoothd`、`btattach`、`btmgmt`、`btmon`、`ciptool`、`gatttool`、`hciattach`、`hciconfig`、`hcitool`、`hex2hcd`、`l2ping`、`l2test`、`mpris-proxy`、`obexctl`、`rctest`、`rfcomm`、`sdptool`、`bluez-cups`、`bluez-meshd`、`mesh-cfgclient`、`mesh-cfgtest`、`meshctl`、`bluez-obexd`、`bluez-source`、`bluez-test-scripts`、`bluez-test-tools`、`6lowpan-tester`、`b1ee`、`bnep-tester`、`btvirt`、`gap-tester`、`hci-tester`、`hfp`、`ioctl-tester`、`iso-tester`、`isotest`、`l2cap-tester`、`mesh-tester`、`mgmt-tester`、`rfcomm-tester`、`sco-tester`、`smp-tester`、`userchan-tester`、`libbluetooth-dev`、`libbluetooth3` |
| 安装 | `sudo apt install bluez` |
| 占用空间 | 5.20 MB |
| 官网 | <http://www.bluez.org> |
| 源码 | <https://salsa.debian.org/bluetooth-team/bluez> |

### btscanner

Ncurses-based scanner for Bluetooth devices btscanner is a tool designed specifically to extract as much information as possible from a Bluetooth device without the requirement to pair. A detailed information screen extracts HCI and SDP information, and maintains an open connection to monitor the RSSI and link quality. btscanner is based on the BlueZ Bluetooth stack, which is included with

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 蓝牙、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/btscanner/> |
| 版本 | 2.1 |
| 包 / 命令 | `btscanner` |
| 安装 | `sudo apt install btscanner` |
| 占用空间 | 112 KB |
| 依赖 | `ieee-data`、`libbluetooth3`、`libc6`、`libncurses6`、`libtinfo6`、`libxml2-16`、`perl`、`btscanner` |
| 官网 | <https://salsa.debian.org/pkg-security-team/btscanner> |
| 源码 | <https://salsa.debian.org/pkg-security-team/btscanner> |

### bully

Implementation of the WPS brute force attack, written in C Bully is a new implementation of the WPS brute force attack, written in C. It is conceptually identical to other programs, in that it exploits the (now well known) design flaw in the WPS specification. It has several advantages over the original reaver code. These include fewer dependencies, improved memory and cpu performance, correct handling of endianness, and a more robust set of

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/bully/> |
| 版本 | 1.4.00 |
| 包 / 命令 | `bully` |
| 安装 | `sudo apt install bully` |
| 占用空间 | 175 KB |
| 依赖 | `aircrack-ng`、`libc6`、`liblua5.3-0`、`libpcap0.8t64`、`pixiewps`、`bully` |
| 官网 | <https://github.com/kimocoder/bully> |
| 源码 | <https://salsa.debian.org/pkg-security-team/bully> |

### chirp

Configuration tool for amateur radios CHIRP is a free, open-source tool for programming your amateur radio. It supports a large number of manufacturers and models, as well as provides a way to interface with multiple data sources and formats. CHIRP can handle data in the following formats: Comma Separated Values (.csv)

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 软件定义无线电、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/chirp/> |
| 版本 | 20251108 |
| 包 / 命令 | `chirp`、`chirpc`、`chirpw`、`experttune` |
| 安装 | `sudo apt install chirp` |
| 占用空间 | 8.53 MB |
| 依赖 | `python3`、`python3-lark`、`python3-requests`、`python3-serial`、`python3-suds`、`python3-yattag`、`wxpython-tools`、`chirpc` |
| 官网 | <https://chirpmyradio.com/> |
| 源码 | <https://salsa.debian.org/debian-hamradio-team/chirp> |

### cowpatty

Brute-force WPA dictionary attack If you are auditing WPA-PSK or WPA2-PSK networks, you can use this tool to identify weak passphrases that were used to generate the PMK. Supply a libpcap capture file that includes the 4-way handshake, a dictionary file of passphrases to guess with, and the SSID for the network.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/cowpatty/> |
| 版本 | 4.8 |
| 包 / 命令 | `cowpatty`、`genpmk` |
| 安装 | `sudo apt install cowpatty` |
| 占用空间 | 73 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`libssl3t64`、`cowpatty` |
| 官网 | <https://www.willhackforsushi.com/?page_id=50> |
| 源码 | <https://salsa.debian.org/pkg-security-team/cowpatty> |

### eapmd5pass

Tool for extracting and cracking EAP-MD5 EAP-MD5 is a legacy authentication mechanism that does not provide sufficient protection for user authentication credentials. Users who authenticate using EAP-MD5 subject themselves to an offline dictionary attack vulnerability. This tool reads from a live network interface in monitor-mode, or from a stored libpcap capture file, and extracts the portions of the EAP-MD5

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/eapmd5pass/> |
| 版本 | 1.5 |
| 包 / 命令 | `eapmd5pass` |
| 安装 | `sudo apt install eapmd5pass` |
| 占用空间 | 102 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`libssl3t64`、`eapmd5pass` |
| 官网 | <https://www.willhackforsushi.com/?page_id=67> |
| 源码 | <https://gitlab.com/kalilinux/packages/eapmd5pass> |

### ethtool

Display or change Ethernet device settings ethtool can be used to query and change settings such as speed, auto- negotiation and checksum offload on many network devices, especially Ethernet devices.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、漏洞利用、嗅探与欺骗、社会工程、Top 10 常用、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/ethtool/> |
| 版本 | 7.1 |
| 包 / 命令 | `ethtool` |
| 安装 | `sudo apt install ethtool` |
| 占用空间 | 1.06 MB |
| 依赖 | `libc6`、`libmnl0`、`ethtool` |
| 官网 | <https://www.kernel.org/pub/software/network/ethtool/> |
| 源码 | <https://salsa.debian.org/kernel-team/ethtool> |

### fern-wifi-cracker

Automated Wi-Fi cracker This package contains a Wireless security auditing and attack software program written using the Python Programming Language and the Python Qt GUI library, the program is able to crack and recover WEP/WPA/WPS keys and also run other network based attacks on wireless or

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/fern-wifi-cracker/> |
| 版本 | 3.6 |
| 包 / 命令 | `fern-wifi-cracker` |
| 安装 | `sudo apt install fern-wifi-cracker` |
| 占用空间 | 1.13 MB |
| 依赖 | `aircrack-ng`、`macchanger`、`python3`、`python3-pyqt5`、`python3-scapy`、`reaver`、`subversion` |
| 官网 | <https://github.com/savio-code/fern-wifi-cracker> |
| 源码 | <https://gitlab.com/kalilinux/packages/fern-wifi-cracker> |

### freeradius-wpe

FreeRadius Wireless Pawn Edition This package is FreeRadius Wireless Pawn Edition. There are supported and tested EAP Types/Inner Authentication Methods (others may also work): PEAP/PAP (OTP) PEAP/MSCHAPv2

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/freeradius-wpe/> |
| 版本 | 3.2.5 |
| 包 / 命令 | `freeradius-wpe` |
| 安装 | `sudo apt install freeradius-wpe` |
| 占用空间 | 4.69 MB |
| 依赖 | `libc6`、`libcrypt1`、`libct4`、`libgdbm6t64`、`libjson-c5`、`libpam0g`、`libpcap0.8t64`、`libperl5.42`、`libpython3.14`、`libsqlite3-0`、`libssl3t64`、`libsystemd0` 等 |
| 官网 | <https://www.freeradius.org/> |
| 源码 | <https://gitlab.com/kalilinux/packages/freeradius-wpe> |

### gnuradio

GNU Radio Software Radio Toolkit GNU Radio provides signal processing blocks to implement software radios. It can be used with readily-available low-cost external RF hardware to create software-defined radios, or without hardware in a simulation-like environment. It is widely used in hobbyist, academic and commercial environments to support both wireless communications

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | RFID / NFC、软件定义无线电、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/gnuradio/> |
| 版本 | 3.10.12.0 |
| 包 / 命令 | `gnuradio`、`dial_tone`、`display_qt`、`gnuradio-companion`、`gnuradio-config-info`、`gr-ctrlport-monitor`、`gr-perf-monitorx`、`gr_filter_design`、`gr_modtool`、`gr_plot`、`gr_plot_const`、`gr_plot_fft`、`gr_plot_iq`、`gr_plot_psd`、`gr_plot_qt`、`gr_read_file_metadata`、`grcc`、`polar_channel_construction`、`tags_demo`、`uhd_fft`、`uhd_rx_cfile`、`uhd_rx_nogui`、`uhd_siggen`、`uhd_siggen_gui`、`gnuradio-dev`、`gnuradio-doc`、`libgnuradio-analog3.10.12`、`libgnuradio-audio3.10.12`、`libgnuradio-blocks3.10.12`、`libgnuradio-channels3.10.12`、`libgnuradio-digital3.10.12`、`libgnuradio-dtv3.10.12`、`libgnuradio-fec3.10.12`、`libgnuradio-fft3.10.12`、`libgnuradio-filter3.10.12`、`libgnuradio-iio3.10.12`、`libgnuradio-network3.10.12`、`libgnuradio-pdu3.10.12`、`libgnuradio-pmt3.10.12`、`libgnuradio-qtgui3.10.12`、`libgnuradio-runtime3.10.12`、`libgnuradio-soapy3.10.12`、`libgnuradio-trellis3.10.12`、`libgnuradio-uhd3.10.12`、`libgnuradio-video-sdl3.10.12`、`libgnuradio-vocoder3.10.12`、`libgnuradio-wavelet3.10.12`、`libgnuradio-zeromq3.10.12` |
| 安装 | `sudo apt install gnuradio` |
| 占用空间 | 24.31 MB |
| 官网 | <https://www.gnuradio.org/> |
| 源码 | <https://salsa.debian.org/bottoms/pkg-gnuradio> |

### gqrx-sdr

Software defined radio receiver Gqrx works with hardware supported by gr-osmosdr, including Funcube Dongle, RTL-SDR, Airspy, HackRF, BladeRF, RFSpace, USRP and SoapySDR. Gqrx can operate as an AM/FM/SSB receiver with audio output or as an FFT-only instrument. The built-in Gqrx AFSK1200 decoder can decode and display AX.25 packets. There are also various hooks for

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 软件定义无线电、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/gqrx-sdr/> |
| 版本 | 2.17.7 |
| 包 / 命令 | `gqrx-sdr`、`gqrx` |
| 安装 | `sudo apt install gqrx-sdr` |
| 占用空间 | 2.08 MB |
| 依赖 | `libc6`、`libgcc-s1`、`libgnuradio-analog3.10.12`、`libgnuradio-blocks3.10.12`、`libgnuradio-digital3.10.12`、`libgnuradio-fft3.10.12`、`libgnuradio-filter3.10.12`、`libgnuradio-network3.10.12`、`libgnuradio-osmosdr0.2.0t64`、`libgnuradio-pmt3.10.12`、`libgnuradio-runtime3.10.12`、`libpulse0` 等 |
| 官网 | <https://gqrx.dk/> |
| 源码 | <https://salsa.debian.org/bottoms/pkg-gqrx-sdr> |

### gr-air-modes

Gnuradio Mode-S/ADS-B radio A software-defined radio receiver for Mode S transponder signals, including ADS-B reports from equipped aircraft. Multiple output formats are supported: Raw (or minimally processed) output of packet data Parsed text

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 软件定义无线电、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/gr-air-modes/> |
| 版本 | 0.0.20210211 |
| 包 / 命令 | `gr-air-modes`、`modes_rx`、`libgnuradio-air-modes1t64` |
| 安装 | `sudo apt install gr-air-modes` |
| 占用空间 | 421 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libgnuradio-air-modes1t64`、`libgnuradio-runtime3.10.12`、`libstdc++6`、`python3`、`python3` |
| 官网 | <https://github.com/bistromath/gr-air-modes> |
| 源码 | <https://salsa.debian.org/bottoms/pkg-gr-air-modes> |

### gr-iqbal

GNU Radio Blind IQ imbalance estimator and correction The general idea is to suppress symmetrical images caused by IQ imbalance in the RX path of quadrature receivers. It’s composed of two subblocks: “IQ Bal Fix”: This applies the actual correction. to a complex stream. The correction parameters are only magnitude/phase and the

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 软件定义无线电、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/gr-iqbal/> |
| 版本 | 0.38.3 |
| 包 / 命令 | `gr-iqbal`、`libgnuradio-iqbalance3.9.0` |
| 安装 | `sudo apt install gr-iqbal` |
| 占用空间 | 1.27 MB |
| 依赖 | `libc6`、`libgcc-s1`、`libgnuradio-iqbalance3.9.0`、`libgnuradio-runtime3.10.12`、`libpython3.14`、`libstdc++6`、`python3`、`python3` |
| 官网 | <https://git.osmocom.org/gr-iqbal> |
| 源码 | <https://salsa.debian.org/bottoms/pkg-gr-iqbal> |

### gr-osmosdr

GNU Radio blocks from the OsmoSDR project The Osmocom project is a family of projects regarding Open source mobile communications. While primarily being developed for the OsmoSDR hardware, this block as well supports: FUNcube Dongle through gr-funcube

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 软件定义无线电、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/gr-osmosdr/> |
| 版本 | 0.2.6 |
| 包 / 命令 | `gr-osmosdr`、`osmocom_fft`、`osmocom_siggen_nogui`、`gr-osmosdr-doc`、`libgnuradio-osmosdr0.2.0t64` |
| 安装 | `sudo apt install gr-osmosdr` |
| 占用空间 | 770 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libgnuradio-osmosdr0.2.0t64`、`libgnuradio-runtime3.10.12`、`libstdc++6`、`python3`、`python3` |
| 官网 | <https://osmocom.org/projects/gr-osmosdr/wiki> |
| 源码 | <https://salsa.debian.org/bottoms/pkg-gr-osmosdr> |

### hackrf

Software defined radio peripheral - utilities HackRF is an open source Software Defined Radio that can receive and transmit between 30 MHz and 6 GHz. HackRF has a 20 MHz bandwidth. It is a High Speed USB device powered by the USB bus. This package contains a set of command line utilities: hackrf_clock: HackRF clock configuration utility

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 软件定义无线电、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/hackrf/> |
| 版本 | 2026.01.3 |
| 包 / 命令 | `hackrf`、`hackrf_biast`、`hackrf_clock`、`hackrf_cpldjtag`、`hackrf_debug`、`hackrf_info`、`hackrf_operacake`、`hackrf_spiflash`、`hackrf_sweep`、`hackrf_transfer`、`hackrf-doc`、`hackrf-firmware`、`libhackrf-dev`、`libhackrf0` |
| 安装 | `sudo apt install hackrf` |
| 占用空间 | 216 KB |
| 依赖 | `libc6`、`libfftw3-single3`、`libhackrf0`、`hackrf_biast` |
| 官网 | <http://greatscottgadgets.com/hackrf/> |
| 源码 | <https://salsa.debian.org/bottoms/pkg-hackrf> |

### hostapd-wpe

Modified hostapd to facilitate AP impersonation attacks This package contains hostapd modified with hostapd-wpe.patch. It implements IEEE 802.1x Authenticator and Authentication Server impersonation attacks to obtain client credentials, establish connectivity to the client, and launch other attacks where applicable.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/hostapd-wpe/> |
| 版本 | 2.10 |
| 包 / 命令 | `hostapd-wpe`、`hostapd-wpe_cli` |
| 安装 | `sudo apt install hostapd-wpe` |
| 占用空间 | 2.25 MB |
| 依赖 | `libc6`、`libnl-3-200`、`libnl-genl-3-200`、`libsqlite3-0`、`libunsafessl1.0.2` |
| 官网 | <https://github.com/aircrack-ng/aircrack-ng/tree/master/patches/wpe> |
| 源码 | <https://gitlab.com/kalilinux/packages/hostapd-wpe> |

### inspectrum

Tool for visualising captured radio signals inspectrum is a tool for analysing captured signals, primarily from software-defined radio receivers. inspectrum supports the following file types: *.sigmf-meta, *.sigmf-data - Signal Metadata Format (SigMF) recordings *.cf32, *.cfile - Complex 32-bit floating point (GNURadio, osmocom_fft)

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 软件定义无线电、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/inspectrum/> |
| 版本 | 0.4.0 |
| 包 / 命令 | `inspectrum` |
| 安装 | `sudo apt install inspectrum` |
| 占用空间 | 276 KB |
| 依赖 | `libc6`、`libfftw3-single3`、`libgcc-s1`、`libliquid1`、`libqt5core5t64` |
| 官网 | <https://github.com/miek/inspectrum> |
| 源码 | <https://salsa.debian.org/debian-hamradio-team/inspectrum> |

### iw

Tool for configuring Linux wireless devices This package contains the ‘iw’ command line tool which allows one to configure and show information about wireless devices. iw is based on the nl80211 kernel interface and supports the majority of fairly recent hardware. The old tool iwconfig, which uses Wireless Extensions interface, is deprecated and it is strongly recommended to switch to iw and

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、漏洞利用、嗅探与欺骗、社会工程、Top 10 常用、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/iw/> |
| 版本 | 6.17 |
| 包 / 命令 | `iw` |
| 安装 | `sudo apt install iw` |
| 占用空间 | 332 KB |
| 依赖 | `libc6`、`libnl-3-200`、`libnl-genl-3-200`、`iw` |
| 官网 | <https://wireless.wiki.kernel.org/en/users/documentation/iw> |
| 源码 | <https://salsa.debian.org/kernel-team/iw> |

### kalibrate-rtl

Calculate local oscillator frequency offset using GSM base stations Kalibrate, or kal, can scan for GSM base stations in a given frequency band and can use those GSM base stations to calculate the local oscillator frequency offset.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 软件定义无线电、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/kalibrate-rtl/> |
| 版本 | 0.4.1 |
| 包 / 命令 | `kalibrate-rtl`、`kal` |
| 安装 | `sudo apt install kalibrate-rtl` |
| 占用空间 | 62 KB |
| 依赖 | `libc6`、`libfftw3-double3`、`libgcc-s1`、`librtlsdr0`、`libstdc++6`、`rtl-sdr`、`kal` |
| 官网 | <https://github.com/steve-m/kalibrate-rtl> |
| 源码 | <https://gitlab.com/kalilinux/packages/kalibrate-rtl> |

### kismet

Wireless network and device detector (metapackage) Kismet is a wireless network and device detector, sniffer, wardriving tool, and WIDS (wireless intrusion detection) framework. Kismet works with Wi-Fi interfaces, Bluetooth interfaces, some SDR (software defined radio) hardware like the RTLSDR, and other specialized capture hardware.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/kismet/> |
| 版本 | 2025.09.R1 |
| 包 / 命令 | `kismet`、`kismet-capture-antsdr-droneid`、`kismet_cap_antsdr_droneid`、`kismet-capture-bladerf-wiphy`、`kismet_cap_bladerf_wiphy`、`kismet-capture-common`、`kismet-capture-freaklabs-zigbee`、`kismet_cap_freaklabs_zigbee`、`kismet-capture-hak5-wifi-coconut`、`kismet_cap_hak5_wifi_coconut`、`kismet-capture-linux-bluetooth`、`kismet_cap_linux_bluetooth`、`kismet-capture-linux-wifi`、`kismet_cap_linux_wifi`、`kismet-capture-nrf-51822`、`kismet_cap_nrf_51822`、`kismet-capture-nrf-52840`、`kismet_cap_nrf_52840`、`kismet-capture-nrf-mousejack`、`kismet_cap_nrf_mousejack`、`kismet-capture-nxp-kw41z`、`kismet_cap_nxp_kw41z`、`kismet-capture-radiacode-usb`、`kismet_cap_radiacode_usb`、`kismet-capture-rtl433`、`kismet_cap_sdr_rtl433`、`kismet-capture-rtladsb`、`kismet_cap_sdr_rtladsb`、`kismet-capture-rz-killerbee`、`kismet_cap_rz_killerbee`、`kismet-capture-serial-radview`、`kismet_cap_serial_radview`、`kismet-capture-ti-cc-2531`、`kismet_cap_ti_cc_2531`、`kismet-capture-ti-cc-2540`、`kismet_cap_ti_cc_2540`、`kismet-capture-ubertooth-one`、`kismet_cap_ubertooth_one`、`kismet-core`、`kismet_cap_kismetdb`、`kismet_cap_pcapfile`、`kismet_server`、`kismet-logtools`、`kismetdb_clean`、`kismetdb_dump_devices`、`kismetdb_statistics`、`kismetdb_strip_packets`、`kismetdb_to_gpx`、`kismetdb_to_kml`、`kismetdb_to_pcap`、`kismetdb_to_wiglecsv`、`kismet-plugins`、`kismet_discovery`、`kismet_eventbus`、`kismet_proxytest`、`python3-kismetcapturefreaklabszigbee`、`python3-kismetcapturertl433`、`python3-kismetcapturertladsb` |
| 安装 | `sudo apt install kismet` |
| 占用空间 | 23 KB |
| 依赖 | `kismet-capture-antsdr-droneid`、`kismet-capture-freaklabs-zigbee`、`kismet-capture-hak5-wifi-coconut`、`kismet-capture-linux-bluetooth`、`kismet-capture-linux-wifi`、`kismet-capture-nrf-51822`、`kismet-capture-nrf-52840`、`kismet-capture-nrf-mousejack`、`kismet-capture-nxp-kw41z`、`kismet-capture-radiacode-usb`、`kismet-capture-rtl433`、`kismet-capture-rtladsb` 等 |
| 官网 | <https://www.kismetwireless.net/> |
| 源码 | <https://gitlab.com/kalilinux/packages/kismet> |

### macchanger

Utility for manipulating the MAC address of network interfaces GNU MAC Changer is an utility that makes the maniputation of MAC addresses of network interfaces easier. MAC addresses are unique identifiers on networks, they only need to be unique, they can be changed on most network hardware. MAC addresses have started to be abused by unscrupulous marketing firms, government agencies, and others to provide an easy way to track a computer

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、嗅探与欺骗、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/macchanger/> |
| 版本 | 1.7.0 |
| 包 / 命令 | `macchanger` |
| 安装 | `sudo apt install macchanger` |
| 占用空间 | 641 KB |
| 官网 | <https://github.com/alobbs/macchanger> |
| 源码 | <https://salsa.debian.org/debian/macchanger> |

### mdk3

Wireless attack tool for IEEE 802.11 networks MDK is a proof-of-concept tool to exploit common IEEE 802.11 (Wi-Fi) protocol weaknesses. Features: Bruteforce MAC Filters. Bruteforce hidden SSIDs (some small SSID wordlists included).

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/mdk3/> |
| 版本 | 6.0 |
| 包 / 命令 | `mdk3` |
| 安装 | `sudo apt install mdk3` |
| 占用空间 | 174 KB |
| 依赖 | `aircrack-ng`、`libc6`、`mdk3` |
| 官网 | <https://github.com/aircrack-ng/mdk3> |
| 源码 | <https://salsa.debian.org/pkg-security-team/mdk3> |

### mdk4

Wireless attack tool for IEEE 802.11 networks This package contains a proof-of-concept tool to exploit common IEEE 802.11 protocol weaknesses. MDK4 is a new version of MDK3. MDK4 is a Wi-Fi testing tool from E7mer of 360PegasusTeam, ASPj of k2wrlz, it uses the osdep library from the aircrack-ng project to inject frames on several operating systems.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/mdk4/> |
| 版本 | 4.2 |
| 包 / 命令 | `mdk4` |
| 安装 | `sudo apt install mdk4` |
| 占用空间 | 236 KB |
| 依赖 | `aircrack-ng`、`libc6`、`libnl-3-200`、`libnl-genl-3-200`、`libpcap0.8t64`、`mdk4` |
| 官网 | <https://github.com/aircrack-ng/mdk4> |
| 源码 | <https://salsa.debian.org/pkg-security-team/mdk4> |

### multimon-ng

Digital radio transmission decoder The successor to multimon, with support for more modes and improved compatibility with moderns systems. It decodes the following digital transmission modes commonly found on VHF/UHF bands: POCSAG512 POCSAG1200 POCSAG2400 FLEX

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 软件定义无线电、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/multimon-ng/> |
| 版本 | 1.3.1 |
| 包 / 命令 | `multimon-ng` |
| 安装 | `sudo apt install multimon-ng` |
| 占用空间 | 134 KB |
| 依赖 | `libc6`、`libpulse0`、`libx11-6`、`multimon-ng` |
| 官网 | <https://github.com/EliasOenal/multimon-ng/> |
| 源码 | <https://salsa.debian.org/debian-hamradio-team/multimon-ng> |

### net-tools

NET-3 networking toolkit This package includes the important tools for controlling the network subsystem of the Linux kernel. This includes arp, ifconfig, netstat, rarp, nameif and route. Additionally, this package contains utilities relating to particular network hardware types (plipconfig, slattach, mii-tool) and advanced aspects of IP configuration (iptunnel, ipmaddr).

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、数字取证、识别与指纹、后渗透、事件响应、嗅探与欺骗、Top 10 常用、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/net-tools/> |
| 版本 | 2.10 |
| 包 / 命令 | `net-tools`、`arp`、`ifconfig`、`ipmaddr`、`iptunnel`、`mii-tool`、`nameif`、`netstat`、`plipconfig`、`rarp`、`route`、`slattach` |
| 安装 | `sudo apt install net-tools` |
| 占用空间 | 917 KB |
| 依赖 | `libc6`、`libselinux1`、`arp` |
| 官网 | <http://sourceforge.net/projects/net-tools/> |
| 源码 | <https://salsa.debian.org/debian/net-tools> |

### pixiewps

Offline WPS bruteforce tool Pixiewps is a tool written in C used to bruteforce offline the WPS pin exploiting the low or non-existing entropy of some APs (pixie dust attack). It is meant for educational purposes only.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/pixiewps/> |
| 版本 | 1.4.2 |
| 包 / 命令 | `pixiewps` |
| 安装 | `sudo apt install pixiewps` |
| 占用空间 | 118 KB |
| 依赖 | `libc6`、`pixiewps` |
| 官网 | <https://github.com/wiire/pixiewps> |
| 源码 | <https://salsa.debian.org/pkg-security-team/pixiewps> |

### proxmark3

Firmware, flasher, and client for the Proxmark3 This package contains the client and tools for the Proxmark3. It is dedicated to bringing the most out of the new features for Proxmark3 RDV4.0 new hardware and design but it will also support older hardware revisions.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | RFID / NFC、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/proxmark3/> |
| 版本 | 4.21611 |
| 包 / 命令 | `proxmark3`、`proxmark3-common`、`pm3`、`pm3-flash`、`pm3-flash-all`、`pm3-flash-bootrom`、`pm3-flash-fullimage`、`proxmark3-doc`、`proxmark3-firmwares` |
| 安装 | `sudo apt install proxmark3` |
| 占用空间 | 6.70 MB |
| 依赖 | `libbluetooth3`、`libbz2-1.0`、`libc6`、`libgcc-s1`、`libjansson4`、`liblz4-1`、`libpython3.14`、`libqt6core6t64`、`libqt6gui6`、`libqt6widgets6`、`libreadline8t64`、`libssl3t64` 等 |
| 官网 | <https://github.com/RfidResearchGroup/proxmark3> |
| 源码 | <https://gitlab.com/kalilinux/packages/proxmark3> |

### reaver

Brute force attack tool against Wi-Fi Protected Setup PIN number Reaver performs a brute force attack against an access point’s Wi-Fi Protected Setup pin number. Once the WPS pin is found, the WPA PSK can be recovered and alternately the AP’s wireless settings can be reconfigured. This package also provides the Wash executable, an utility for identifying WPS

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/reaver/> |
| 版本 | 1.6.6 |
| 包 / 命令 | `reaver`、`wash` |
| 安装 | `sudo apt install reaver` |
| 占用空间 | 851 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`reaver` |
| 官网 | <https://github.com/t6x/reaver-wps-fork-t6x> |
| 源码 | <https://salsa.debian.org/pkg-security-team/reaver> |

### redfang

Locates non-discoverable bluetooth devices fang is a small proof-of-concept application to find non discoveredable bluetooth devices. This is done by brute forcing the last six (6) bytes of the bluetooth address of the device and doing a read_remote_name().

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 蓝牙、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/redfang/> |
| 版本 | 2.5 |
| 包 / 命令 | `redfang`、`fang` |
| 安装 | `sudo apt install redfang` |
| 占用空间 | 40 KB |
| 依赖 | `libbluetooth3`、`libc6`、`fang` |
| 源码 | <https://gitlab.com/kalilinux/packages/redfang> |

### rfcat

Swiss army knife of sub-GHz radio Rfcat is a sub GHz analysis tool. The goals of the project are to reduce the time for security researchers to create needed tools for analyzing unknown targets, to aid in reverse-engineering of hardware.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/rfcat/> |
| 版本 | 2.0.1 |
| 包 / 命令 | `rfcat`、`rfcat_bootloader`、`rfcat_msfrelay`、`rfcat_server` |
| 安装 | `sudo apt install rfcat` |
| 占用空间 | 443 KB |
| 依赖 | `ipython3`、`python3`、`python3-ipython`、`python3-numpy`、`python3-pyside6.qtcore`、`python3-pyside6.qtgui`、`python3-pyside6.qtwidgets`、`python3-serial`、`python3-usb`、`rfcat` |
| 官网 | <https://github.com/atlas0fd00m/rfcat> |
| 源码 | <https://gitlab.com/kalilinux/packages/rfcat> |

### rfdump

Tool to decode RFID tag data RFDump is a tool to decode RFID tags and show their meta information: tag ID, tag type, manufacturer etc. The user data memory of a tag can be displayed and modified using either a hex or an ASCII editor. In addition, the integrated cookie feature demonstrates how easy it is for a company to abuse RFID technology to spy on their customers.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | RFID / NFC、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/rfdump/> |
| 版本 | 1.6 |
| 包 / 命令 | `rfdump` |
| 安装 | `sudo apt install rfdump` |
| 占用空间 | 251 KB |
| 依赖 | `libc6`、`libexpat1`、`libglib2.0-0t64`、`libgtk-3-0t64`、`rfdump` |
| 官网 | <http://www.rfdump.org/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/rfdump> |

### sakis3g

Tool for establishing 3G connections Sakis3G is a tweaked shell script which is supposed to work out-of-the-box for establishing a 3G connection with any combination of modem or operator. It automagically setups your USB or Bluetooth™ modem, and may even detect operator settings. You should try it when anything else fails.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/sakis3g/> |
| 版本 | 0.2.0e |
| 包 / 命令 | `sakis3g` |
| 安装 | `sudo apt install sakis3g` |
| 占用空间 | 537 KB |
| 依赖 | `bzip2`、`libusb-1.0-0`、`sakis3g` |
| 官网 | <http://www.sakis3g.org> |
| 源码 | <https://gitlab.com/kalilinux/packages/sakis3g> |

### screen

Terminal multiplexer with VT100/ANSI terminal emulation GNU Screen is a terminal multiplexer that runs several separate “screens” on a single physical character-based terminal. Each virtual terminal emulates a DEC VT100 plus several ANSI X3.64 and ISO 2022 functions. Screen sessions can be detached and resumed later on a different terminal. Screen also supports a whole slew of other features, including configurable

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、嗅探与欺骗、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/screen/> |
| 版本 | 5.0.2 |
| 包 / 命令 | `screen`、`screen-udeb` |
| 安装 | `sudo apt install screen` |
| 占用空间 | 1007 KB |
| 依赖 | `debianutils`、`libc6`、`libpam0g`、`libtinfo6`、`ncurses-term` |
| 官网 | <https://savannah.gnu.org/projects/screen> |
| 源码 | <https://salsa.debian.org/debian/screen> |

### spooftooph

Automates spoofing or cloning Bluetooth devices Spooftooph is designed to automate spoofing or cloning Bluetooth device Name, Class, and Address. Cloning this information effectively allows Bluetooth device to hide in plain site. Bluetooth scanning software will only list one of the devices if more than one device in range shares the

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 蓝牙、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/spooftooph/> |
| 版本 | 0.5.2 |
| 包 / 命令 | `spooftooph` |
| 安装 | `sudo apt install spooftooph` |
| 占用空间 | 74 KB |
| 依赖 | `bluez`、`libbluetooth3`、`libc6`、`libncurses6`、`libtinfo6`、`spooftooph` |
| 官网 | <http://www.hackfromacave.com/projects/spooftooph.html> |
| 源码 | <https://gitlab.com/kalilinux/packages/spooftooph> |

### tmux

Terminal multiplexer tmux enables a number of terminals (or windows) to be accessed and controlled from a single terminal like screen. tmux runs as a server-client system. A server is created automatically when necessary and holds a number of sessions, each of which may have a number of windows linked to it. Any number of clients may connect to a session,

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/tmux/> |
| 版本 | 3.7b |
| 包 / 命令 | `tmux` |
| 安装 | `sudo apt install tmux` |
| 占用空间 | 1.35 MB |
| 依赖 | `libc6`、`libevent-core-2.1-7t64`、`libjemalloc2`、`libsystemd0`、`libtinfo6` |
| 官网 | <https://github.com/tmux/tmux/wiki> |
| 源码 | <https://salsa.debian.org/debian/tmux> |

### ubertooth

2.4 GHz wireless development platform for Bluetooth experimentation Project Ubertooth is an open source wireless development platform suitable for Bluetooth experimentation. This package contains everything necessary to use the hardware dongle. Ubertooth is capable of sniffing BLE (Bluetooth Smart) connections and it also has some ability to sniff some data from Basic Rate (BR) Bluetooth Classic

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、蓝牙、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/ubertooth/> |
| 版本 | 2020.12.R1 |
| 包 / 命令 | `libubertooth-dev`、`libubertooth1`、`ubertooth`、`ubertooth-afh`、`ubertooth-btbr`、`ubertooth-btle`、`ubertooth-debug`、`ubertooth-dfu`、`ubertooth-ducky`、`ubertooth-dump`、`ubertooth-ego`、`ubertooth-follow`、`ubertooth-rx`、`ubertooth-scan`、`ubertooth-specan`、`ubertooth-specan-ui`、`ubertooth-util`、`ubertooth-firmware`、`ubertooth-firmware-source` |
| 安装 | `sudo apt install ubertooth` |
| 占用空间 | 333 KB |
| 依赖 | `libbluetooth3`、`libbtbb1`、`libc6`、`libubertooth1`、`libusb-1.0-0`、`python3`、`python3-numpy`、`ubertooth-afh` |
| 官网 | <http://ubertooth.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/debian/ubertooth> |

### uhd

Universal hardware driver for Ettus Research products - headers Host library for the Universal Hardware Driver for Ettus Research products. The supported devices provide analog radio receiver and transmitter hardware along with digital interfaces for getting signals to and from a software defined radio running on the host computer. This package contains the header files for developing with libuhd.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | RFID / NFC、软件定义无线电、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/uhd/> |
| 版本 | 4.9.0.1 |
| 包 / 命令 | `libuhd-dev`、`libuhd4.9.0`、`libuhd4.9.0-dpdk`、`libuhd4.9.0-dpdk-tests`、`python3-uhd`、`uhd-doc`、`uhd-host`、`rfnoc_image_builder`、`rfnoc_modtool`、`uhd_adc_self_cal`、`uhd_cal_rx_iq_balance`、`uhd_cal_tx_dc_offset`、`uhd_cal_tx_iq_balance`、`uhd_config_info`、`uhd_find_devices`、`uhd_image_loader`、`uhd_images_downloader`、`uhd_usrp_probe`、`usrp2_card_burner`、`usrpctl`、`uhd-rfnoc-dev` |
| 安装 | `sudo apt install libuhd-dev` |
| 占用空间 | 1.20 MB |
| 依赖 | `libboost-chrono-dev`、`libboost-date-time-dev`、`libboost-dev`、`libboost-exception-dev`、`libboost-filesystem-dev`、`libboost-program-options-dev`、`libboost-python-dev`、`libboost-regex-dev`、`libboost-serialization-dev`、`libboost-test-dev`、`libboost-thread-dev`、`libuhd4.9.0` 等 |
| 官网 | <https://www.ettus.com/sdr-software/uhd-usrp-hardware-driver/> |
| 源码 | <https://salsa.debian.org/bottoms/pkg-uhd> |

### uhd-images

Various UHD Images Various UHD Images

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 软件定义无线电、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/uhd-images/> |
| 版本 | 4.0.0.0 |
| 包 / 命令 | `uhd-images` |
| 安装 | `sudo apt install uhd-images` |
| 占用空间 | 107.02 MB |
| 官网 | <https://www.ettus.com> |
| 源码 | <https://gitlab.com/kalilinux/packages/uhd-images> |

### wifi-honey

Wi-Fi honeypot In the case of WPA/WPA2, by running airodump-ng along side this you also end up capturing the first two packets of the four way handshake and so can attempt to crack the key with either aircrack-ng or coWPAtty. What this script does is to automate the setup process, it

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、嗅探与欺骗、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/wifi-honey/> |
| 版本 | 1.0 |
| 包 / 命令 | `wifi-honey` |
| 安装 | `sudo apt install wifi-honey` |
| 占用空间 | 16 KB |
| 依赖 | `aircrack-ng`、`screen`、`wifi-honey` |
| 官网 | <https://www.digininja.org/projects/wifi_honey.php> |
| 源码 | <https://gitlab.com/kalilinux/packages/wifi-honey> |

### wifite

Python script to automate wireless auditing using aircrack-ng tools Wifite is a tool to audit WEP or WPA encrypted wireless networks. It uses aircrack-ng, pyrit, reaver, tshark tools to perform the audit. This tool is customizable to be automated with only a few arguments and can be trusted to run without supervision.

| 项目 | 内容 |
|------|------|
| 归入分组 | 无线攻击 |
| 全部所属分组 | 802.11 Wi-Fi、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/wifite/> |
| 版本 | 2.8.2 |
| 包 / 命令 | `wifite` |
| 安装 | `sudo apt install wifite` |
| 占用空间 | 8.01 MB |
| 依赖 | `aircrack-ng`、`ieee-data`、`net-tools`、`python3`、`python3-chardet`、`reaver`、`tshark`、`wifite` |
| 官网 | <https://github.com/kimocoder/wifite2> |
| 源码 | <https://salsa.debian.org/pkg-security-team/wifite> |
