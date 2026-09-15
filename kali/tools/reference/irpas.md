# irpas

> Internetwork Routing Protocol Attack Suite This package contains a collection of programs used for advanced network operations, testing, and debugging. CDP and the route injectors can be useful in a production network. Several other tools …

> **功能分类**：信息搜集 ｜ **Kali 包**：`irpas` ｜ **官方文档**：<https://www.kali.org/tools/irpas/>

## 1. 安装

```bash
sudo apt update
sudo apt install irpas
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.10 |
| 架构 | any |
| 可执行命令 | `irpas`、`ass`、`cdp`、`dfkaa`、`dhcpx`、`file2cable`、`hsrp`、`icmp_redirect`、`igrp`、`inetmask`、`irdp`、`irdpresponder`、`itrace`、`netenum`、`protos`、`tctrace`、`timestamp` |
| 依赖 | `libc6`、`libpcap0.8t64`、`ass` |
| 安装体积 | 406 KB |
| 官网 | <https://web.archive.org/web/20200208113522fw_/http://phenoelit.org/fr/tools.html> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/irpas> |
| 包追踪 | <https://pkg.kali.org/pkg/irpas> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
irpas -h          # 查看用法
man irpas         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 17 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ass`

> 官方示例调用：`ass -h`

```text
root@kali:~# ass -h
ass [-v[v[v]]] -i <interface> [-ApcMs] [-P IER12]
	[-a <autonomous system start> -b <autonomous system stop>]
	[-S <spoofed source IP>] [-D <destination ip>]
	[-T <packets per delay>]
	[-r <filename>]
```

### `cdp`

> 官方示例调用：`cdp -h`

```text
root@kali:~# cdp -h
cdp [-v] -i <interface> -m {0,1} ...
Flood mode (-m 0):
-n <number>	number of packets
-l <number>	length of the device id
-c <char>	character to fill in device id
-r		randomize device id string
Spoof mode (-m 1):
-D <string>	Device id
-P <string>	Port id
-L <string>	Platform
-S <string>	Software
-F <string>	IP address
-C <capabilities>
	these are:
	R - Router, T - Trans Bridge, B - Source Route Bridge
	S - Switch, H - Host, I - IGMP, r - Repeater
```

### `dfkaa`

> 官方示例调用：`dfkaa -h`

```text
root@kali:~# dfkaa -h
dfkaa: invalid option -- 'h'
Usage ... well. Look into the .c
```

### `dhcpx`

> 官方示例调用：`dhcpx -h`

```text
root@kali:~# dhcpx -h
dhcpx [-v[v[v]]] -i <interface> [-A]
	[-D <destination ip>]
	[-t <discovery time in secs>]
	[-u <ARP time in secs>]
```

### `file2cable`

> 官方示例调用：`file2cable -h`

```text
root@kali:~# file2cable -h
file2cable [-v] -i <interface> -f <file>
```

### `hsrp`

> 官方示例调用：`hsrp -h`

```text
root@kali:~# hsrp -h
hsrp -i <interface> -v <virtual IP> -d <router ip> -a <authword>
	-g <group> [-S <source>]
EXAMPLE:
while (true);
  do (./hsrp -d 224.0.0.2 -v192.168.1.22 -a cisco -g 1 -i eth0 ; sleep 3);
done
```

### `icmp_redirect`

> 官方示例调用：`icmp_redirect -h`

```text
root@kali:~# icmp_redirect -h
icmp_redirect [-v[v[v]]] -i <interface>
	[-s <source net>/<source mask>]
	[-d <destination net>/<destination mask>]
	[-G <gateway IP>] [-w <delay>]
	[-S <ip address>]
```

### `igrp`

> 官方示例调用：`igrp -h`

```text
root@kali:~# igrp -h
Usage:
igrp [-v[v[v]]] -i <interface> -f <routes file>
	-a <autonomous system> [-b brute force end]
	[-S <spoofed source IP>] [-D <destination ip>]
```

### `inetmask`

> 官方示例调用：`inetmask -h`

```text
root@kali:~# inetmask -h
inetmask: invalid option -- 'h'
Usage: inetmask -d <destination> -t <timeout>
```

### `irdp`

> 官方示例调用：`irdp -h`

```text
root@kali:~# irdp -h
Usage:
irdp [-v (useless)] -i <interface>
	[-S <spoofed source IP>] [-D <destination ip>]
	[-l <lifetime in sec, default: 1800>] [-p <preference>]
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install irpas`，再执行 `irpas --version` 2>/dev/null || `irpas -V`
- [ ] **2.** **读官方帮助** —— `irpas -h`，需要细节时 `man irpas`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage ... well. Look into the .c`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/irpas/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/irpas/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/irpas/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
