# gr-air-modes

> Gnuradio Mode-S/ADS-B radio A software-defined radio receiver for Mode S transponder signals, including ADS-B reports from equipped aircraft. Multiple output formats are supported: Raw (or minimally processed) output of packet data Parsed …

> **功能分类**：无线攻击 ｜ **Kali 包**：`gr-air-modes` ｜ **官方文档**：<https://www.kali.org/tools/gr-air-modes/>

## 1. 安装

```bash
sudo apt update
sudo apt install gr-air-modes
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0.20210211 |
| 架构 | any |
| 可执行命令 | `gr-air-modes`、`modes_rx`、`libgnuradio-air-modes1t64` |
| 依赖 | `libc6`、`libgcc-s1`、`libgnuradio-air-modes1t64`、`libgnuradio-runtime3.10.12`、`libstdc++6`、`python3`、`python3` |
| 安装体积 | 421 KB |
| 官网 | <https://github.com/bistromath/gr-air-modes> |
| 源码仓库 | <https://salsa.debian.org/bottoms/pkg-gr-air-modes> |
| 包追踪 | <https://pkg.kali.org/pkg/gr-air-modes> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gr-air-modes -h          # 查看用法
man gr-air-modes         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `modes_rx`

官方给出的调用示例：`modes_rx -h`

```text
root@kali:~# modes_rx -h
gr-air-modes warning: numpy+scipy not installed, FlightGear interface not supported
Usage: modes_rx: [options]
Options:
  -h, --help            show this help message and exit
  -l LOCATION, --location=LOCATION
                        GPS coordinates of receiving station in format
                        xx.xxxxx,xx.xxxxx
  -a REMOTE, --remote=REMOTE
                        specify additional servers from which to take data in
                        format tcp://x.x.x.x:y,tcp://....
  -n, --no-print        disable printing decoded packets to stdout
  -K KML, --kml=KML     filename for Google Earth KML output
  -P, --sbs1            open an SBS-1-compatible server on port 30003
  -m MULTIPLAYER, --multiplayer=MULTIPLAYER
                        FlightGear server to send aircraft data, in format
                        host:port
  Receiver setup options:
    -s SOURCE, --source=SOURCE
                        Choose source: uhd, osmocom, <filename>, or <ip:port>
                        [default=uhd]
    -t PORT, --tcp=PORT
                        Open a TCP server on this port to publish reports
    -R SUBDEV, --subdev=SUBDEV
                        select USRP Rx side A or B
    -A ANTENNA, --antenna=ANTENNA
                        select which antenna to use on daughterboard
    -D ARGS, --args=ARGS
                        arguments to pass to radio constructor
    -f FREQ, --freq=FREQ
                        set receive frequency in Hz [default=1090000000.0]
    -g dB, --gain=dB    set RF gain
    -r RATE, --rate=RATE
                        set sample rate [default=4000000.0]
    -T THRESHOLD, --threshold=THRESHOLD
                        set pulse detection threshold above noise in dB
                        [default=7.0]
    -p, --pmf           Use pulse matched filtering [default=True]
    -d, --dcblock       Use a DC blocking filter (best for HackRF Jawbreaker)
                        [default=False]
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install gr-air-modes`，再执行 `gr-air-modes --version` 2>/dev/null || `gr-air-modes -V`
- [ ] **2.** **读官方帮助** —— `gr-air-modes -h`，需要细节时 `man gr-air-modes`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: modes_rx: [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gr-air-modes/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gr-air-modes/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gr-air-modes/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
