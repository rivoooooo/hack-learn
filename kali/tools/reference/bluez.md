# bluez

> bluez Bluetooth tools and daemons This package contains tools and system daemons for using Bluetooth devices. BlueZ is the official Linux Bluetooth protocol stack. It is an Open Source project distributed under GNU General Public License (…

> **功能分类**：无线攻击 ｜ **Kali 包**：`bluez` ｜ **官方文档**：<https://www.kali.org/tools/bluez/>

## 1. 安装

```bash
sudo apt update
sudo apt install bluez
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.87 |
| 架构 | linux-any |
| 可执行命令 | `bluetooth`、`bluez`、`bluemoon`、`bluetoothctl`、`bluetoothd`、`btattach`、`btmgmt`、`btmon`、`ciptool`、`gatttool`、`hciattach`、`hciconfig`、`hcitool`、`hex2hcd`、`l2ping`、`l2test`、`mpris-proxy`、`obexctl`、`rctest`、`rfcomm`、`sdptool`、`bluez-cups`、`bluez-meshd`、`mesh-cfgclient`、`mesh-cfgtest`、`meshctl`、`bluez-obexd`、`bluez-source`、`bluez-test-scripts`、`bluez-test-tools`、`6lowpan-tester`、`b1ee`、`bnep-tester`、`btvirt`、`gap-tester`、`hci-tester`、`hfp`、`ioctl-tester`、`iso-tester`、`isotest`、`l2cap-tester`、`mesh-tester`、`mgmt-tester`、`rfcomm-tester`、`sco-tester`、`smp-tester`、`userchan-tester`、`libbluetooth-dev`、`libbluetooth3` |
| 安装体积 | 5.20 MB |
| 官网 | <http://www.bluez.org> |
| 源码仓库 | <https://salsa.debian.org/bluetooth-team/bluez> |
| 包追踪 | <https://pkg.kali.org/pkg/bluez> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
bluetooth -h          # 查看用法
man bluetooth         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 49 个可执行命令，下面是官方页面内嵌的帮助原文。

### `bluemoon`

官方给出的调用示例：`bluemoon -h`

```text
root@kali:~# bluemoon -h
bluemoon - Bluemoon configuration utility
Usage:
	bluemoon [options]
Options:
	-A, --bdaddr [addr]    Set Bluetooth address
	-F, --firmware [file]  Load firmware
	-C, --check <file>     Check firmware image
	-R, --reset            Reset controller
	-B, --coldboot         Cold boot controller
	-E, --exception        Trigger exception
	-i, --index <num>      Use specified controller
	-h, --help             Show help options
```

### `bluetoothctl`

官方给出的调用示例：`bluetoothctl -h`

```text
root@kali:~# bluetoothctl -h
bluetoothctl ver 5.87
Usage:
	bluetoothctl [--options] [commands]
Options:
	--agent 	Register agent handler: <capability>
	--endpoints 	Register Media endpoints
	--monitor 	Enable monitor output
	--timeout 	Timeout in seconds for non-interactive mode
	--version 	Display version
	--init-script 	Init script file
	--help 		Display help
Commands:
	list		List available controllers
	show		Controller information
	select		Select default controller
	devices		List available devices, with an optional property as the filter
	system-alias	Set controller alias
	reset-alias	Reset controller alias
	power		Set controller power
	pairable	Set controller pairable mode
	discoverable	Set controller discoverable mode
	discoverable-timeout	Set discoverable timeout
	agent		Enable/disable agent with given capability
	default-agent	Set agent as the default one
	advertise	Enable/disable advertising with given type
	set-alias	Set device alias
	scan		Scan for devices
	info		Device/Set information
	pair		Pair with device
	cancel-pairing	Cancel pairing with device
	trust		Trust device
	untrust		Untrust device
	block		Block device
	unblock		Unblock device
	remove		Remove device
	connect		Connect a device and all its profiles or optionally connect a single profile only
	disconnect	Disconnect a device or optionally disconnect a single profile only
	wake		Get/Set wake support
	bearer		Get/Set preferred bearer
	advertise.:
		uuids		Set/Get advertise uuids
		solicit		Set/Get advertise solicit uuids
		service		Set/Get advertise service data
		manufacturer	Set/Get advertise manufacturer data
		data		Set/Get advertise data
		public-broadcast	Set/Get BLE Audio Public Broadcast Announcement
		sr-uuids	Set/Get scan response uuids
		sr-solicit	Set/Get scan response solicit uuids
		sr-service	Set/Get scan response service data
		sr-manufacturer	Set/Get scan response manufacturer data
		sr-data		Set/Get scan response data
		discoverable	Set/Get advertise discoverable
		discoverable-timeout	Set/Get advertise discoverable timeout
		tx-power	Show/Enable/Disable TX power to be advertised
		name		Configure local name to be advertised
		appearance	Configure custom appearance to be advertised
		duration	Set/Get advertise duration
		timeout		Set/Get advertise timeout
		secondary	Set/Get advertise secondary channel
		interval	Set/Get advertise interval range
		rsi		Show/Enable/Disable RSI to be advertised
		instance	Show advertisement instance number
		clear		Clear advertise config
	monitor.:
		set-rssi-threshold	Set RSSI threshold parameter
		set-rssi-timeout	Set RSSI timeout parameter
		set-rssi-sampling-period	Set RSSI sampling period parameter
		add-or-pattern	Register 'or pattern' type monitor with the specified RSSI parameters
		get-pattern	Get advertisement monitor
		remove-pattern	Remove advertisement monitor
		get-supported-info	Get advertisement manager supported features and supported monitor types
		print-usage	Print the command usage
	scan.:
		uuids		Set/Get UUIDs filter
		rssi		Set/Get RSSI filter, and clears pathloss
		pathloss	Set/Get Pathloss filter, and clears RSSI
		transport	Set/Get transport filter
		duplicate-data	Set/Get duplicate data filter
		discoverable	Set/Get discoverable filter
		pattern		Set/Get pattern filter
		auto-connect	Set/Get auto-connect filter
		clear		Clears discovery filter.
	gatt.:
		list-attributes	List attributes
		select-attribute	Select attribute
		attribute-info	Select attribute
		read		Read attribute value
		write		Write attribute value
		acquire-write	Acquire Write file descriptor
		release-write	Release Write file descriptor
		acquire-notify	Acquire Notify file descriptor
		release-notify	Release Notify file descriptor
		notify		Notify attribute value
		clone		Clone a device or attribute
		register-application	Register profile to connect
		unregister-application	Unregister profile
		register-service	Register application service.
		unregister-service	Unregister application service
		register-includes	Register as Included service in.
		unregister-includes	Unregister Included service.
		register-characteristic	Register application characteristic
		unregister-characteristic	Unregister application characteristic
		register-descriptor	Register application descriptor
		unregister-descriptor	Unregister application descriptor
	le.:
		list		List available le devices
		show		LE bearer information
		connect		Connect le on a device
		disconnect	Disconnect le on a device
	bredr.:
		list		List available bredr devices
		show		BREDR bearer information
		connect		Connect bredr on a device
		disconnect	Disconnect bredr on a device
	admin.:
		allow		Allow service UUIDs and block rest of them
	player.:
		list		List available players
		show		Player information
		select		Select default player
		play		Start playback
		pause		Pause playback
		stop		Stop playback
		next		Jump to next item
		previous	Jump to previous item
		fast-forward	Fast forward playback
		rewind		Rewind playback
		equalizer	Enable/Disable equalizer
		repeat		Set repeat mode
		shuffle		Set shuffle mode
		scan		Set scan mode
		change-folder	Change current folder
		list-items	List items of current folder
		search		Search items containing string
		queue		Add item to playlist queue
		show-item	Show item information
	endpoint.:
		list		List available endpoints
		show		Endpoint information
		register	Register Endpoint
		unregister	Register Endpoint
		config		Configure Endpoint
		presets		List or add presets
	transport.:
		list		List available transports
		show		Transport information
		acquire		Acquire Transport
		release		Release Transport
		send		Send contents of a file
		receive		Get/Set file to receive
		volume		Get/Set transport volume
		select		Select Transport
		unselect	Unselect Transport
		metadata	Get/Set Transport Metadata
		desync		Desynchronize Transport
	mgmt.:
		select		Select a different index
		revision	Get the MGMT Revision
		commands	List supported commands
		config		Show configuration info
		info		Show controller info
		extinfo		Show extended controller info
		auto-power	Power all available features
		power		Toggle powered state
		discov		Toggle discoverable state
		connectable	Toggle connectable state
		fast-conn	Toggle fast connectable state
		bondable	Toggle bondable state
		pairable	Toggle bondable state
		linksec		Toggle link level security
		ssp		Toggle SSP mode
		sc		Toggle SC support
		hs		Toggle HS support
		le		Toggle LE support
		advertising	Toggle LE advertising
		bredr		Toggle BR/EDR support
		privacy		Toggle privacy support
		class		Set device major/minor class
		disconnect	Disconnect device
		con		List connections
		find		Discover nearby devices
		find-service	Discover nearby service
		stop-find	Stop discovery
		name		Set local name
		pair		Pair with a remote device
		cancelpair	Cancel pairing
		unpair		Unpair device
		keys		Load Link Keys
		ltks		Load Long Term Keys
		irks		Load Identity Resolving Keys
		block		Block Device
		unblock		Unblock Device
		add-uuid	Add UUID
		rm-uuid		Remove UUID
		clr-uuids	Clear UUIDs
		local-oob	Local OOB data
		remote-oob	Remote OOB data
		did		Set Device ID
		static-addr	Set static address
		public-addr	Set public address
		ext-config	External configuration
		debug-keys	Toggle debug keys
		conn-info	Get connection information
		io-cap		Set IO Capability
		scan-params	Set Scan Parameters
		get-clock	Get Clock Information
		add-device	Add Device
		del-device	Remove Device
		clr-devices	Clear Devices
		bredr-oob	Local OOB data (BR/EDR)
		le-oob		Local OOB data (LE)
		advinfo		Show advertising features
		advsize		Show advertising size info
		add-adv		Add advertising instance
		rm-adv		Remove advertising instance
		clr-adv		Clear advertising instances
		add-ext-adv-params	Add extended advertising params
		add-ext-adv-data	Add extended advertising data
		appearance	Set appearance
```

### `bluetoothd`

官方给出的调用示例：`bluetoothd -h`

```text
root@kali:~# bluetoothd -h
Usage:
  bluetoothd [OPTION…]
Help Options:
  -h, --help                  Show help options
Application Options:
  -d, --debug=DEBUG           Specify debug options to enable
  -p, --plugin=NAME,..,       Specify plugins to load
  -P, --noplugin=NAME,...     Specify plugins not to load
  -f, --configfile=FILE       Specify an explicit path to the config file
  -C, --compat                Provide deprecated command line interfaces
  -E, --experimental          Enable experimental D-Bus interfaces
  -T, --testing               Enable testing D-Bus interfaces
  -K, --kernel                Enable kernel experimental features
  -n, --nodetach              Run with logging in foreground
  -v, --version               Show version information and exit
```

### `btattach`

官方给出的调用示例：`btattach -h`

```text
root@kali:~# btattach -h
btattach - Bluetooth serial utility
Usage:
	btattach [options]
options:
	-B, --bredr <device>   Attach Primary controller
	-A, --amp <device>     Attach AMP controller
	-P, --protocol <proto> Specify protocol type
	-S, --speed <baudrate> Specify which baudrate to use
	-N, --noflowctl        Disable flow control
	-h, --help             Show help options
```

### `btmgmt`

官方给出的调用示例：`btmgmt -h`

```text
root@kali:~# btmgmt -h
btmgmt ver 5.87
Usage:
	btmgmt [--options] [commands]
Options:
	--index 	Specify adapter index
	--monitor 	Enable monitor output
	--timeout 	Timeout in seconds for non-interactive mode
	--version 	Display version
	--init-script 	Init script file
	--help 		Display help
Commands:
	select		Select a different index
	revision	Get the MGMT Revision
	commands	List supported commands
	config		Show configuration info
	info		Show controller info
	extinfo		Show extended controller info
	auto-power	Power all available features
	power		Toggle powered state
	discov		Toggle discoverable state
	connectable	Toggle connectable state
	fast-conn	Toggle fast connectable state
	bondable	Toggle bondable state
	pairable	Toggle bondable state
	linksec		Toggle link level security
	ssp		Toggle SSP mode
	sc		Toggle SC support
	hs		Toggle HS support
	le		Toggle LE support
	advertising	Toggle LE advertising
	bredr		Toggle BR/EDR support
	privacy		Toggle privacy support
	class		Set device major/minor class
	disconnect	Disconnect device
	con		List connections
	find		Discover nearby devices
	find-service	Discover nearby service
	stop-find	Stop discovery
	name		Set local name
	pair		Pair with a remote device
	cancelpair	Cancel pairing
	unpair		Unpair device
	keys		Load Link Keys
	ltks		Load Long Term Keys
	irks		Load Identity Resolving Keys
	block		Block Device
	unblock		Unblock Device
	add-uuid	Add UUID
	rm-uuid		Remove UUID
	clr-uuids	Clear UUIDs
	local-oob	Local OOB data
	remote-oob	Remote OOB data
	did		Set Device ID
	static-addr	Set static address
	public-addr	Set public address
	ext-config	External configuration
	debug-keys	Toggle debug keys
	conn-info	Get connection information
	io-cap		Set IO Capability
	scan-params	Set Scan Parameters
	get-clock	Get Clock Information
	add-device	Add Device
	del-device	Remove Device
	clr-devices	Clear Devices
	bredr-oob	Local OOB data (BR/EDR)
	le-oob		Local OOB data (LE)
	advinfo		Show advertising features
	advsize		Show advertising size info
	add-adv		Add advertising instance
	rm-adv		Remove advertising instance
	clr-adv		Clear advertising instances
	add-ext-adv-params	Add extended advertising params
	add-ext-adv-data	Add extended advertising data
	appearance	Set appearance
	phy		Get/Set PHY Configuration
	wbs		Toggle Wideband-Speech support
	secinfo		Show security information
	expinfo		Show experimental features
	exp-debug	Set debug feature
	exp-privacy	Set LL privacy feature
	exp-quality	Set bluetooth quality report feature
	exp-offload	Toggle codec support
	exp-iso		Toggle ISO support
	read-sysconfig	Read System Configuration
	set-sysconfig	Set System Configuration
	get-flags	Get device flags
	set-flags	Set device flags
	hci-cmd		Send HCI Command and wait for Event
	monitor.:
		features	Show advertisement monitor features
		remove		Remove advertisement monitor
		add-pattern	Add advertisement monitor pattern
		add-pattern-rssi	Add advertisement monitor pattern with RSSI options
```

### `btmon`

官方给出的调用示例：`btmon -h`

```text
root@kali:~# btmon -h
btmon - Bluetooth monitor
Usage:
	btmon [options]
options:
	-r, --read <file>      Read traces in btsnoop format
	-w, --write <file>     Save traces in btsnoop format
	-a, --analyze <file>   Analyze traces in btsnoop format
	                       If gnuplot is installed on the
	                       system it will also attempt to plot
	                       packet latency graph.
	-s, --server <socket>  Start monitor server socket
	-p, --priority <level> Show only priority or lower
	-i, --index <num>      Show only specified controller
	-d, --tty <tty>        Read data from TTY
	-B, --tty-speed <rate> Set TTY speed (default 115200)
	-V, --vendor <compid>  Set default company identifier
	-M, --mgmt             Open channel for mgmt events
	-K, --kernel           Open kmsg for kernel messages
	-t, --time             Show time instead of time offset
	-T, --date             Show time and date information
	-S, --sco              Dump SCO traffic
	-A, --a2dp             Dump A2DP stream traffic
	-I, --iso              Dump ISO traffic
	-E, --ellisys [ip]     Send Ellisys HCI Injection
	-P, --no-pager         Disable pager usage
	-J  --jlink <device>,[<serialno>],[<interface>],[<speed>]
	                       Read data from RTT
	-R  --rtt [<address>],[<area>],[<name>]
	                       RTT control block parameters
	-C, --columns [width]  Output width if not a terminal
	-c, --color [mode]     Output color: auto/always/never
	-h, --help             Show help options
```

### `ciptool`

官方给出的调用示例：`ciptool -h`

```text
root@kali:~# ciptool -h
ciptool - Bluetooth Common ISDN Access Profile (CIP)
Usage:
	ciptool [options] [command]
Options:
	-i [hciX|bdaddr]   Local HCI device or BD Address
	-h, --help         Display help
Commands:
	show               	Show remote connections
	search             	Search for a remote device
	connect  <bdaddr>  	Connect a remote device
	release  [bdaddr]  	Disconnect the remote device
	loopback <bdaddr>  	Loopback test of a device
```

### `gatttool`

官方给出的调用示例：`gatttool -h`

```text
root@kali:~# gatttool -h
Usage:
  gatttool [OPTION…]
Help Options:
  -h, --help                                Show help options
  --help-all                                Show all help options
  --help-gatt                               Show all GATT commands
  --help-params                             Show all Primary Services/Characteristics arguments
  --help-char-read-write                    Show all Characteristics Value/Descriptor Read/Write arguments
Application Options:
  -i, --adapter=hciX                        Specify local adapter interface
  -b, --device=MAC                          Specify remote Bluetooth address
  -t, --addr-type=[public | random]         Set LE address type. Default: public
  -m, --mtu=MTU                             Specify the MTU size
  -p, --psm=PSM                             Specify the PSM for GATT/ATT over BR/EDR
  -l, --sec-level=[low | medium | high]     Set security level. Default: low
  -I, --interactive                         Use interactive mode
```

### `hciattach`

官方给出的调用示例：`hciattach -h`

```text
root@kali:~# hciattach -h
hciattach - HCI UART driver initialization utility
Usage:
	hciattach [-n] [-p] [-b] [-r] [-t timeout] [-s initial_speed] <tty> <type | id> [speed] [flow|noflow] [sleep|nosleep] [bdaddr]
	hciattach -l
```

### `hciconfig`

官方给出的调用示例：`hciconfig -h`

```text
root@kali:~# hciconfig -h
hciconfig - HCI device configuration utility
Usage:
	hciconfig
	hciconfig [-a] hciX [command ...]
Commands:
	up                 	Open and initialize HCI device
	down               	Close HCI device
	reset              	Reset HCI device
	rstat              	Reset statistic counters
	auth               	Enable Authentication
	noauth             	Disable Authentication
	encrypt            	Enable Encryption
	noencrypt          	Disable Encryption
	piscan             	Enable Page and Inquiry scan
	noscan             	Disable scan
	iscan              	Enable Inquiry scan
	pscan              	Enable Page scan
	ptype      [type]  	Get/Set default packet type
	lm         [mode]  	Get/Set default link mode
	lp         [policy]	Get/Set default link policy
	name       [name]  	Get/Set local name
	class      [class] 	Get/Set class of device
	voice      [voice] 	Get/Set voice setting
	iac        [iac]   	Get/Set inquiry access code
	inqtpl     [level] 	Get/Set inquiry transmit power level
	inqmode    [mode]  	Get/Set inquiry mode
	inqdata    [data]  	Get/Set inquiry data
	inqtype    [type]  	Get/Set inquiry scan type
	inqparms   [win:int]	Get/Set inquiry scan window and interval
	pageparms  [win:int]	Get/Set page scan window and interval
	pageto     [to]    	Get/Set page timeout
	afhmode    [mode]  	Get/Set AFH mode
	sspmode    [mode]  	Get/Set Simple Pairing Mode
	aclmtu     <mtu:pkt>	Set ACL MTU and number of packets
	scomtu     <mtu:pkt>	Set SCO MTU and number of packets
	delkey     <bdaddr>	Delete link key from the device
	oobdata            	Get local OOB data
	commands           	Display supported commands
	features           	Display device features
	version            	Display version information
	revision           	Display revision information
	block      <bdaddr>	Add a device to the reject list
	unblock    <bdaddr>	Remove a device from the reject list
	lerandaddr <bdaddr>	Set LE Random Address
	leadv      [type]  	Enable LE advertising
			0 - Connectable undirected advertising (default)
			3 - Non connectable undirected advertising
	noleadv            	Disable LE advertising
	lestates           	Display the supported LE states
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install bluez`，再执行 `bluetooth --version` 2>/dev/null || `bluetooth -V`
- [ ] **2.** **读官方帮助** —— `bluetooth -h`，需要细节时 `man bluetooth`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/bluez/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/bluez/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/bluez/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
