# ethtool

> Display or change Ethernet device settings ethtool can be used to query and change settings such as speed, auto- negotiation and checksum offload on many network devices, especially Ethernet devices.

> **功能分类**：无线攻击 ｜ **Kali 包**：`ethtool` ｜ **官方文档**：<https://www.kali.org/tools/ethtool/>

## 1. 安装

```bash
sudo apt update
sudo apt install ethtool
```

| 项目 | 内容 |
|------|------|
| 版本 | 7.1 |
| 架构 | linux-any |
| 可执行命令 | `ethtool` |
| 依赖 | `libc6`、`libmnl0` |
| 安装体积 | 1.06 MB |
| 官网 | <https://www.kernel.org/pub/software/network/ethtool/> |
| 源码仓库 | <https://salsa.debian.org/kernel-team/ethtool> |
| 包追踪 | <https://pkg.kali.org/pkg/ethtool> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ethtool -h          # 查看用法
man ethtool         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ethtool`

> 官方示例调用：`ethtool -h`

```text
root@kali:~# ethtool -h
ethtool version 7.1
Usage:
        ethtool [ FLAGS ]  DEVNAME	Display standard information about device
        ethtool [ FLAGS ] -s|--change DEVNAME	Change generic options
		[ speed %d ]
		[ lanes %d ]
		[ duplex half|full ]
		[ port tp|aui|bnc|mii|fibre|da ]
		[ mdix auto|on|off ]
		[ autoneg on|off ]
		[ advertise %x[/%x] | mode on|off ... [--] ]
		[ phyad %d ]
		[ xcvr internal|external ]
		[ wol %d[/%d] | p|u|m|b|a|g|s|f|d... ]
		[ sopass %x:%x:%x:%x:%x:%x ]
		[ msglvl %d[/%d] | type on|off ... [--] ]
		[ master-slave preferred-master|preferred-slave|forced-master|forced-slave ]
        ethtool [ FLAGS ] -a|--show-pause DEVNAME	Show pause options
		[ --src aggregate | emac | pmac ]
        ethtool [ FLAGS ] -A|--pause DEVNAME	Set pause options
		[ autoneg on|off ]
		[ rx on|off ]
		[ tx on|off ]
        ethtool [ FLAGS ] -c|--show-coalesce DEVNAME	Show coalesce options
        ethtool [ FLAGS ] -C|--coalesce DEVNAME	Set coalesce options
		[adaptive-rx on|off]
		[adaptive-tx on|off]
		[rx-usecs N]
		[rx-frames N]
		[rx-usecs-irq N]
		[rx-frames-irq N]
		[tx-usecs N]
		[tx-frames N]
		[tx-usecs-irq N]
		[tx-frames-irq N]
		[stats-block-usecs N]
		[pkt-rate-low N]
		[rx-usecs-low N]
		[rx-frames-low N]
		[tx-usecs-low N]
		[tx-frames-low N]
		[pkt-rate-high N]
		[rx-usecs-high N]
		[rx-frames-high N]
		[tx-usecs-high N]
		[tx-frames-high N]
		[sample-interval N]
		[cqe-mode-rx on|off]
		[cqe-mode-tx on|off]
		[tx-aggr-max-bytes N]
		[tx-aggr-max-frames N]
		[tx-aggr-time-usecs N]
		[rx-cqe-frames N]
		[rx-cqe-nsecs N]
        ethtool [ FLAGS ] -g|--show-ring DEVNAME	Query RX/TX ring parameters
        ethtool [ FLAGS ] -G|--set-ring DEVNAME	Set RX/TX ring parameters
		[ rx N ]
		[ rx-mini N ]
		[ rx-jumbo N ]
		[ tx N ]
		[ rx-buf-len N ]
		[ tcp-data-split auto|on|off ]
		[ cqe-size N ]
		[ tx-push on|off ]
		[ rx-push on|off ]
		[ tx-push-buf-len N]
		[ hds-thresh N ]
        ethtool [ FLAGS ] -k|--show-features|--show-offload DEVNAME	Get state of protocol offload and other features
        ethtool [ FLAGS ] -K|--features|--offload DEVNAME	Set protocol offload and other features
		FEATURE on|off ...
        ethtool [ FLAGS ] -i|--driver DEVNAME	Show driver information
        ethtool [ FLAGS ] -d|--register-dump DEVNAME	Do a register dump
		[ raw on|off ]
		[ file FILENAME ]
        ethtool [ FLAGS ] -e|--eeprom-dump DEVNAME	Do a EEPROM dump
		[ raw on|off ]
		[ offset N ]
		[ length N ]
        ethtool [ FLAGS ] -E|--change-eeprom DEVNAME	Change bytes in device EEPROM
		[ magic N ]
		[ offset N ]
		[ length N ]
		[ value N ]
        ethtool [ FLAGS ] -r|--negotiate DEVNAME	Restart N-WAY negotiation
        ethtool [ FLAGS ] -p|--identify DEVNAME	Show visible port identification (e.g. blinking)
		[ TIME-IN-SECONDS ]
        ethtool [ FLAGS ] -t|--test DEVNAME	Execute adapter self test
		[ online | offline | external_lb ]
        ethtool [ FLAGS ] -S|--statistics DEVNAME	Show adapter statistics
		[ --all-groups | --groups [eth-phy] [eth-mac] [eth-ctrl] [rmon] ]
		[ --src aggregate | emac | pmac ]
        ethtool [ FLAGS ] --phy-statistics DEVNAME	Show phy statistics
        ethtool [ FLAGS ] -n|-u|--show-nfc|--show-ntuple DEVNAME	Show Rx network flow classification options or rules
		[ rx-flow-hash tcp4|udp4|ah4|esp4|sctp4|gtpc4|gtpc4t|gtpu4|gtpu4e|gtpu4u|gtpu4d|tcp6|udp6|ah6|esp6|sctp6|gtpc6|gtpc6t|gtpu6|gtpu6e|gtpu6u|gtpu6d [context %d] |
		  rule %d ]
        ethtool [ FLAGS ] -N|-U|--config-nfc|--config-ntuple DEVNAME	Configure Rx network flow classification options or rules
		rx-flow-hash tcp4|udp4|ah4|esp4|sctp4|gtpc4|gtpc4t|gtpu4|gtpu4e|gtpu4u|gtpu4d|tcp6|udp6|ah6|esp6|sctp6|gtpc6|gtpc6t|gtpu6|gtpu6e|gtpu6u|gtpu6d m|v|t|s|d|f|n|r|e|l... [context %d] |
		flow-type ether|ip4|tcp4|udp4|sctp4|ah4|esp4|ip6|tcp6|udp6|ah6|esp6|sctp6
			[ src %x:%x:%x:%x:%x:%x [m %x:%x:%x:%x:%x:%x] ]
			[ dst %x:%x:%x:%x:%x:%x [m %x:%x:%x:%x:%x:%x] ]
			[ proto %d [m %x] ]
			[ src-ip IP-ADDRESS [m IP-ADDRESS] ]
			[ dst-ip IP-ADDRESS [m IP-ADDRESS] ]
			[ tos %d [m %x] ]
			[ tclass %d [m %x] ]
			[ l4proto %d [m %x] ]
			[ src-port %d [m %x] ]
			[ dst-port %d [m %x] ]
			[ spi %d [m %x] ]
			[ vlan-etype %x [m %x] ]
			[ vlan %x [m %x] ]
			[ user-def %x [m %x] ]
			[ dst-mac %x:%x:%x:%x:%x:%x [m %x:%x:%x:%x:%x:%x] ]
			[ action %d ] | [ vf %d queue %d ]
			[ context %d ]
			[ loc %d ] |
		delete %d
        ethtool [ FLAGS ] -T|--show-time-stamping DEVNAME	Show time stamping capabilities
		[ index N qualifier precise|approx ]
        ethtool [ FLAGS ] --get-hwtimestamp-cfg DEVNAME	Get selected hardware time stamping
        ethtool [ FLAGS ] --set-hwtimestamp-cfg DEVNAME	Select hardware time stamping
		[ index N qualifier precise|approx ]
		[ tx TX-TYPE ] [ rx-filter RX-FILTER ]
        ethtool [ FLAGS ] -x|--show-rxfh-indir|--show-rxfh DEVNAME	Show Rx flow hash indirection table and/or RSS hash key
		[ context %d ]
        ethtool [ FLAGS ] -X|--set-rxfh-indir|--rxfh DEVNAME	Set Rx flow hash indirection table and/or RSS hash key
		[ context %d|new ]
		[ equal N | weight W0 W1 ... | default ]
		[ hkey %x:%x:%x:%x:%x:.... ]
		[ hfunc FUNC ]
		[ xfrm symmetric-xor | symmetric-or-xor | none ]
		[ delete ]
        ethtool [ FLAGS ] -f|--flash DEVNAME	Flash firmware image from the specified file to a region on the device
		FILENAME [ REGION-NUMBER-TO-FLASH ]
        ethtool [ FLAGS ] -P|--show-permaddr DEVNAME	Show permanent hardware address
        ethtool [ FLAGS ] -w|--get-dump DEVNAME	Get dump flag, data
		[ data FILENAME ]
        ethtool [ FLAGS ] -W|--set-dump DEVNAME	Set dump flag of the device
		N
        ethtool [ FLAGS ] -l|--show-channels DEVNAME	Query Channels
        ethtool [ FLAGS ] -L|--set-channels DEVNAME	Set Channels
		[ rx N ]
		[ tx N ]
		[ other N ]
		[ combined N ]
        ethtool [ FLAGS ] --show-priv-flags DEVNAME	Query private flags
        ethtool [ FLAGS ] --set-priv-flags DEVNAME	Set private flags
		FLAG on|off ...
        ethtool [ FLAGS ] -m|--dump-module-eeprom|--module-info DEVNAME	Query/Decode Module EEPROM information and optical diagnostics if available
		[ raw on|off ]
		[ hex on|off ]
		[ pages on|off ]
		[ offset N ]
		[ length N ]
		[ page N ]
		[ bank N ]
		[ i2c N ]
        ethtool [ FLAGS ] --show-eee DEVNAME	Show EEE settings
        ethtool [ FLAGS ] --set-eee DEVNAME	Set EEE settings
		[ eee on|off ]
		[ advertise %x ]
		[ tx-lpi on|off ]
		[ tx-timer %d ]
        ethtool [ FLAGS ] --set-phy-tunable DEVNAME	Set PHY tunable
		[ downshift on|off [count N] ]
		[ fast-link-down on|off [msecs N] ]
		[ energy-detect-power-down on|off [msecs N] ]
        ethtool [ FLAGS ] --get-phy-tunable DEVNAME	Get PHY tunable
		[ downshift ]
		[ fast-link-down ]
		[ energy-detect-power-down ]
        ethtool [ FLAGS ] --get-tunable DEVNAME	Get tunable
		[ rx-copybreak ]
		[ tx-copybreak ]
		[ tx-buf-size ]
		[ pfc-prevention-tout ]
        ethtool [ FLAGS ] --set-tunable DEVNAME	Set tunable
		[ rx-copybreak N ]
		[ tx-copybreak N ]
		[ tx-buf-size N ]
		[ pfc-prevention-tout N ]
        ethtool [ FLAGS ] --reset DEVNAME	Reset components
		[ flags %x ]
		[ mgmt ]
		[ mgmt-shared ]
		[ irq ]
		[ irq-shared ]
		[ dma ]
		[ dma-shared ]
		[ filter ]
		[ filter-shared ]
		[ offload ]
		[ offload-shared ]
		[ mac ]
		[ mac-shared ]
		[ phy ]
		[ phy-shared ]
		[ ram ]
		[ ram-shared ]
		[ ap ]
		[ ap-shared ]
		[ dedicated ]
		[ all ]
        ethtool [ FLAGS ] --show-fec DEVNAME	Show FEC settings
        ethtool [ FLAGS ] --set-fec DEVNAME	Set FEC settings
		[ encoding auto|off|rs|baser|llrs [...] ]
        ethtool [ FLAGS ] -Q|--per-queue DEVNAME	Apply per-queue command.
The supported sub commands include --show-coalesce, --coalesce		[queue_mask %x] SUB_COMMAND
        ethtool [ FLAGS ] [ --phy PHY ] --cable-test DEVNAME	Perform a cable test
        ethtool [ FLAGS ] [ --phy PHY ] --cable-test-tdr DEVNAME	Print cable test time domain reflectrometery data
		[ first N ]
		[ last N ]
		[ step N ]
		[ pair N ]
        ethtool [ FLAGS ] --show-tunnels DEVNAME	Show NIC tunnel offload information
        ethtool [ FLAGS ] --show-module DEVNAME	Show transceiver module settings
        ethtool [ FLAGS ] --set-module DEVNAME	Set transceiver module settings
		[ power-mode-policy high|auto ]
        ethtool [ FLAGS ] [ --phy PHY ] --get-plca-cfg DEVNAME	Get PLCA configuration
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install ethtool`，再执行 `ethtool --version` 2>/dev/null || `ethtool -V`
- [ ] **2.** **读官方帮助** —— `ethtool -h`，需要细节时 `man ethtool`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ethtool/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ethtool/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ethtool/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
