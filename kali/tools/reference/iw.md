# iw

> Tool for configuring Linux wireless devices This package contains the ‘iw’ command line tool which allows one to configure and show information about wireless devices. iw is based on the nl80211 kernel interface and supports the majority o…

> **功能分类**：无线攻击 ｜ **Kali 包**：`iw` ｜ **官方文档**：<https://www.kali.org/tools/iw/>

## 1. 安装

```bash
sudo apt update
sudo apt install iw
```

| 项目 | 内容 |
|------|------|
| 版本 | 6.17 |
| 架构 | linux-any |
| 可执行命令 | `iw` |
| 依赖 | `libc6`、`libnl-3-200`、`libnl-genl-3-200` |
| 安装体积 | 332 KB |
| 官网 | <https://wireless.wiki.kernel.org/en/users/documentation/iw> |
| 源码仓库 | <https://salsa.debian.org/kernel-team/iw> |
| 包追踪 | <https://pkg.kali.org/pkg/iw> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
iw -h          # 查看用法
man iw         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `iw`

> 官方示例调用：`iw -h`

```text
root@kali:~# iw -h
Usage:	iw [options] command
Options:
	--debug		enable netlink debugging
	--version	show version (6.17)
Commands:
	dev <devname> ap stop
		Stop AP functionality
	dev <devname> ap start <SSID> <SSID> <freq> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz|160MHz|320MHz] [punct <bitmap>] <beacon interval in TU> <DTIM period> [hidden-ssid|zeroed-ssid] head <beacon head in hexadecimal> [tail <beacon tail in hexadecimal>] [inactivity-time <inactivity time in seconds>] [key0:abcde d:1:6162636465]
	dev <devname> ap start <SSID> <control freq> [5|10|20|40|80|80+80|160|320] [<center1_freq> [<center2_freq>]] [punct <bitmap>] <beacon interval in TU> <DTIM period> [hidden-ssid|zeroed-ssid] head <beacon head in hexadecimal> [tail <beacon tail in hexadecimal>] [inactivity-time <inactivity time in seconds>] [key0:abcde d:1:6162636465]
		Start an AP. Note that this usually requires hostapd or similar.
	phy <phyname> coalesce show
		Show coalesce status.
	phy <phyname> coalesce disable
		Disable coalesce.
	phy <phyname> coalesce enable <config-file>
		Enable coalesce with given configuration.
		The configuration file contains coalesce rules:
		  delay=<delay>
		  condition=<condition>
		  patterns=<[offset1+]<pattern1>,<[offset2+]<pattern2>,...>
		  delay=<delay>
		  condition=<condition>
		  patterns=<[offset1+]<pattern1>,<[offset2+]<pattern2>,...>
		  ...
		delay: maximum coalescing delay in msec.
		condition: 1/0 i.e. 'not match'/'match' the patterns
		patterns: each pattern is given as a bytestring with '-' in
		places where any byte may be present, e.g. 00:11:22:-:44 will
		match 00:11:22:33:44 and 00:11:22:33:ff:44 etc. Offset and
		pattern should be separated by '+', e.g. 18+43:34:00:12 will
		match '43:34:00:12' after 18 bytes of offset in Rx packet.
	dev <devname> auth <SSID> <bssid> <type:open|shared> <freq in MHz> [key 0:abcde d:1:6162636465]
		Authenticate with the given network.
	dev <devname> connect [-w] <SSID> [<freq in MHz>] [<bssid>] [auth open|shared] [key 0:abcde d:1:6162636465] [mfp:req/opt/no]
		Join the network with the given SSID (and frequency, BSSID).
		With -w, wait for the connect to finish or fail.
	dev <devname> disconnect
		Disconnect from the current network.
	dev <devname> cqm rssi <threshold|off> [<hysteresis>]
		Set connection quality monitor RSSI threshold.
	event [-t|-T|-r] [-f]
		Monitor events from the kernel.
		-t - print timestamp
		-T - print absolute, human-readable timestamp
		-r - print relative timestamp
		-f - print full frame for auth/assoc etc.
	dev <devname> ftm start_responder [lci=<lci buffer in hex>] [civic=<civic buffer in hex>]
		Start an FTM responder. Needs a running ap interface
	dev <devname> ftm get_stats
		Get FTM responder statistics.
	phy <phyname> hwsim wakequeues
	phy <phyname> hwsim stopqueues
	phy <phyname> hwsim setps <value>
	phy <phyname> hwsim getps
	dev <devname> ibss join <SSID> <freq in MHz> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz] [fixed-freq] [<fixed bssid>] [beacon-interval <TU>] [basic-rates <rate in Mbps,rate2,...>] [mcast-rate <rate in Mbps>] [key d:0:abcde]
		Join the IBSS cell with the given SSID, if it doesn't exist create
		it on the given frequency. When fixed frequency is requested, don't
		join/create a cell on a different frequency. When a fixed BSSID is
		requested use that BSSID and do not adopt another cell's BSSID even
		if it has higher TSF and the same SSID. If an IBSS is created, create
		it with the specified basic-rates, multicast-rate and beacon-interval.
	dev <devname> ibss leave
		Leave the current IBSS cell.
	features
	commands
		list all known commands and their decimal & hex value
	phy
	list
		List all wireless devices and their capabilities.
	phy <phyname> info
		Show capabilities for the specified wireless device.
	dev <devname> switch channel <channel> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz] [beacons <count>] [block-tx]
	dev <devname> switch freq <freq> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz] [beacons <count>] [block-tx]
	dev <devname> switch freq <control freq> [5|10|20|40|80|80+80|160] [<center1_freq> [<center2_freq>]] [beacons <count>] [block-tx]
		Switch the operating channel by sending a channel switch announcement (CSA).
	dev
		List all network interfaces for wireless hardware.
	dev <devname> info
		Show information for this interface.
	dev <devname> del
		Remove this virtual interface
	dev <devname> interface add <name> type <type> [mesh_id <meshid>] [4addr on|off] [flags <flag>*] [addr <mac-addr>]
	phy <phyname> interface add <name> type <type> [mesh_id <meshid>] [4addr on|off] [flags <flag>*] [addr <mac-addr>]
		Add a new virtual interface with the given configuration.
		Valid interface types are: managed, ibss, monitor, mesh, wds.
		The flags are only used for monitor interfaces, valid flags are:
		none:     no special flags
		fcsfail:  show frames with FCS errors
		control:  show control frames
		otherbss: show frames from other BSSes
		cook:     use cooked mode
		active:   use active mode (ACK incoming unicast packets)
		mumimo-groupid <GROUP_ID>: use MUMIMO according to a group id
		mumimo-follow-mac <MAC_ADDRESS>: use MUMIMO according to a MAC address
		The mesh_id is used only for mesh mode.
	help [command]
		Print usage for all or a specific command, e.g.
		"help wowlan" or "help wowlan enable".
	dev <devname> key get <key index> <MAC address>
		Retrieve a key and key sequence.
	dev <devname> link
		Print information about the current connection, if any.
	dev <devname> measurement ftm_request <config-file> [timeout=<seconds>] [randomise[=<addr>/<mask>]]
		Send an FTM request to the targets supplied in the config file.
		Each line in the file represents a target, with the following format:
		<addr> bw=<[20|40|80|80+80|160]> cf=<center_freq> [cf1=<center_freq1>] [cf2=<center_freq2>] [ftms_per_burst=<samples per burst>] [ap-tsf] [asap] [bursts_exp=<num of bursts exponent>] [burst_period=<burst period>] [retries=<num of retries>] [burst_duration=<burst duration>] [preamble=<legacy,ht,vht,dmg>] [lci] [civic] [tb] [non_tb]
	dev <devname> mesh_param dump
		List all supported mesh parameters
	dev <devname> mesh leave
		Leave a mesh.
	dev <devname> mesh join <mesh ID> [[freq <freq in MHz> <NOHT|HT20|HT40+|HT40-|80MHz>] [basic-rates <rate in Mbps,rate2,...>]], [mcast-rate <rate in Mbps>] [beacon-interval <time in TUs>] [dtim-period <value>] [vendor_sync on|off] [<param>=<value>]*
		Join a mesh with the given mesh ID with frequency, basic-rates,
		mcast-rate and mesh parameters. Basic-rates are applied only if
		frequency is provided.
	dev <devname> mgmt dump frame <type as hex ab> <pattern as hex ab:cd:..> [frame <type> <pattern>]* [count <frames>]
		Register for receiving certain mgmt frames and print them.
		Frames are selected by their type and pattern containing
		the first several bytes of the frame that should match.
		Example: iw dev wlan0 mgmt dump frame 40 00 frame 40 01:02 count 10
	dev <devname> mpath dump
		List known mesh paths.
	dev <devname> mpath set <destination MAC address> next_hop <next hop MAC address>
		Set an existing mesh path's next hop.
	dev <devname> mpath new <destination MAC address> next_hop <next hop MAC address>
		Create a new mesh path (instead of relying on automatic discovery).
	dev <devname> mpath del <MAC address>
		Remove the mesh path to the given node.
	dev <devname> mpath get <MAC address>
		Get information on mesh path to the given node.
	dev <devname> mpath probe <destination MAC address> frame <frame>
		Inject ethernet frame to given peer overriding the next hop
		lookup from mpath table.
		.Example: iw dev wlan0 mpath probe xx:xx:xx:xx:xx:xx frame 01:xx:xx:00
	dev <devname> mpp dump
		List known mesh proxy paths.
	dev <devname> mpp get <MAC address>
		Get information on mesh proxy path to the given node.
	wdev <idx> nan add_func type <publish|subscribe|followup> [active] [solicited] [unsolicited] [bcast] [close_range] name <name> [info <info>] [flw_up_id <id> flw_up_req_id <id> flw_up_dest <mac>] [ttl <ttl>] [srf <include|exclude> <bf|list> [bf_idx] [bf_len] <mac1;mac2...>] [rx_filter <str1:str2...>] [tx_filter <str1:str2...>]
	wdev <idx> nan rm_func cookie <cookie>
	wdev <idx> nan config [pref <pref>] [bands [2GHz] [5GHz]]
	wdev <idx> nan stop
	wdev <idx> nan start pref <pref> [bands [2GHz] [5GHz]]
	dev <devname> ocb leave
		Leave the OCB mode network.
	dev <devname> ocb join <freq in MHz> <5MHz|10MHz>
		Join the OCB mode network.
	dev <devname> offchannel <freq> <duration>
		Leave operating channel and go to the given channel for a while.
	wdev <idx> p2p stop
	wdev <idx> p2p start
	dev <devname> cac channel <channel> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz|160MHz|320MHz] [punct <bitmap>]
	dev <devname> cac freq <freq> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz|160MHz|320MHz] [punct <bitmap>]
	dev <devname> cac freq <control freq> [5|10|20|40|80|80+80|160|320] [<center1_freq> [<center2_freq>]] [punct <bitmap>]
	dev <devname> cac background channel <channel> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz|160MHz|320MHz] [punct <bitmap>]
	dev <devname> cac background freq <freq> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz|160MHz|320MHz] [punct <bitmap>]
	dev <devname> cac background freq <control freq> [5|10|20|40|80|80+80|160|320] [<center1_freq> [<center2_freq>]] [punct <bitmap>]
		Start background channel availability check (CAC) looking to look for
		radars on the given channel.
	dev <devname> cac trigger channel <channel> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz|160MHz|320MHz] [punct <bitmap>]
	dev <devname> cac trigger freq <freq> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz|160MHz|320MHz] [punct <bitmap>]
	dev <devname> cac trigger freq <control freq> [5|10|20|40|80|80+80|160|320] [<center1_freq> [<center2_freq>]] [punct <bitmap>]
		Start or trigger a channel availability check (CAC) looking to look for
		radars on the given channel.
	phy <phyname> channels
		Show available channels.
	reg reload
		Reload the kernel's regulatory database.
	phy <phyname> reg get
		Print out the devices' current regulatory domain information.
	reg get
		Print out the kernel's current regulatory domain information.
	reg set <ISO/IEC 3166-1 alpha2>
		Notify the kernel about the current regulatory domain.
	dev <devname> roc start <freq> <time in ms>
	dev <devname> scan [-u] [freq <freq>*] [duration <dur>] [ies <hex as 00:11:..>] [meshid <meshid>] [lowpri,flush,ap-force,duration-mandatory] [randomise[=<addr>/<mask>]] [ssid <ssid>*|passive]
		Scan on the given frequencies and probe for the given SSIDs
		(or wildcard if not given) unless passive scanning is requested.
		If -u is specified print unknown data in the scan results.
		Specified (vendor) IEs must be well-formed.
	dev <devname> scan sched_stop
		Stop an ongoing scheduled scan.
	dev <devname> scan sched_start [interval <in_msecs> | scan_plans [<interval_secs:iterations>*] <interval_secs>] [delay <in_secs>] [freqs <freq>+] [matches [ssid <ssid>]+]] [active [ssid <ssid>]+|passive] [randomise[=<addr>/<mask>]] [coloc] [flush]
		Start a scheduled scan at the specified interval on the given frequencies
		with probing for the given SSIDs (or wildcard if not given) unless passive
		scanning is requested.  If matches are specified, only matching results
		will be returned.
	dev <devname> scan abort
		Abort ongoing scan
	dev <devname> scan trigger [freq <freq>*] [duration <dur>] [ies <hex as 00:11:..>] [meshid <meshid>] [lowpri,flush,ap-force,duration-mandatory,coloc] [randomise[=<addr>/<mask>]] [ssid <ssid>*|passive]
		Trigger a scan on the given frequencies with probing for the given
		SSIDs (or wildcard if not given) unless passive scanning is requested.
		Duration(in TUs), if specified, will be used to set dwell times.
	dev <devname> scan dump [-u]
		Dump the current scan results. If -u is specified, print unknown
		data in scan results.
	dev <devname> set bitrates [legacy-<2.4|5> <legacy rate in Mbps>*] [ht-mcs-<2.4|5> <MCS index>*] [vht-mcs-<2.4|5> [he-mcs-<2.4|5|6> <NSS:MCSx,MCSy... | NSS:MCSx-MCSy>*] [sgi-2.4|lgi-2.4] [sgi-5|lgi-5] [he-gi-<2.4|5|6> <0.8|1.6|3.2>] [he-ltf-<2.4|5|6> <1|2|4>]
		Sets up the specified rate masks.
		Not passing any arguments would clear the existing mask (if any).
	dev <devname> set epcs <enable|disable>
		Enable/Disable EPCS support
	dev <devname> set tidconf [peer <MAC address>] tids <mask> [override] [sretry <num>] [lretry <num>] [ampdu [on|off]] [amsdu [on|off]] [noack [on|off]] [rtscts [on|off]][bitrates <type [auto|fixed|limit]> [legacy-<2.4|5> <legacy rate in Mbps>*] [ht-mcs-<2.4|5> <MCS index>*] [vht-mcs-<2.4|5> <NSS:MCSx,MCSy... | NSS:MCSx-MCSy>*] [sgi-2.4|lgi-2.4] [sgi-5|lgi-5]]
		Setup per-node TID specific configuration for TIDs selected by bitmask.
		If MAC address is not specified, then supplied TID configuration
		applied to all the peers.
		Examples:
		  $ iw dev wlan0 set tidconf tids 0x1 ampdu off
		  $ iw dev wlan0 set tidconf tids 0x5 ampdu off amsdu off rtscts on
		  $ iw dev wlan0 set tidconf tids 0x3 override ampdu on noack on rtscts on
		  $ iw dev wlan0 set tidconf peer xx:xx:xx:xx:xx:xx tids 0x1 ampdu off tids 0x3 amsdu off rtscts on
		  $ iw dev wlan0 set tidconf peer xx:xx:xx:xx:xx:xx tids 0x2 bitrates auto
		  $ iw dev wlan0 set tidconf peer xx:xx:xx:xx:xx:xx tids 0x2 bitrates limit vht-mcs-5 4:9
	dev <devname> set mcast_rate <rate in Mbps>
		Set the multicast bitrate.
	dev <devname> set peer <MAC address>
		Set interface WDS peer.
	dev <devname> set noack_map <map>
		Set the NoAck map for the TIDs. (0x0009 = BE, 0x0006 = BK, 0x0030 = VI, 0x00C0 = VO)
	dev <devname> set 4addr <on|off>
		Set interface 4addr (WDS) mode.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install iw`，再执行 `iw --version` 2>/dev/null || `iw -V`
- [ ] **2.** **读官方帮助** —— `iw -h`，需要细节时 `man iw`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:	iw [options] command`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/iw/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/iw/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/iw/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
