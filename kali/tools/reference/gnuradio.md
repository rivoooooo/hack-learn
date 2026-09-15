# gnuradio

> GNU Radio Software Radio Toolkit GNU Radio provides signal processing blocks to implement software radios. It can be used with readily-available low-cost external RF hardware to create software-defined radios, or without hardware in a simu…

> **功能分类**：无线攻击 ｜ **Kali 包**：`gnuradio` ｜ **官方文档**：<https://www.kali.org/tools/gnuradio/>

## 1. 安装

```bash
sudo apt update
sudo apt install gnuradio
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.10.12.0 |
| 架构 | any |
| 可执行命令 | `gnuradio`、`dial_tone`、`display_qt`、`gnuradio-companion`、`gnuradio-config-info`、`gr-ctrlport-monitor`、`gr-perf-monitorx`、`gr_filter_design`、`gr_modtool`、`gr_plot`、`gr_plot_const`、`gr_plot_fft`、`gr_plot_iq`、`gr_plot_psd`、`gr_plot_qt`、`gr_read_file_metadata`、`grcc`、`polar_channel_construction`、`tags_demo`、`uhd_fft`、`uhd_rx_cfile`、`uhd_rx_nogui`、`uhd_siggen`、`uhd_siggen_gui`、`gnuradio-dev`、`gnuradio-doc`、`libgnuradio-analog3.10.12`、`libgnuradio-audio3.10.12`、`libgnuradio-blocks3.10.12`、`libgnuradio-channels3.10.12`、`libgnuradio-digital3.10.12`、`libgnuradio-dtv3.10.12`、`libgnuradio-fec3.10.12`、`libgnuradio-fft3.10.12`、`libgnuradio-filter3.10.12`、`libgnuradio-iio3.10.12`、`libgnuradio-network3.10.12`、`libgnuradio-pdu3.10.12`、`libgnuradio-pmt3.10.12`、`libgnuradio-qtgui3.10.12`、`libgnuradio-runtime3.10.12`、`libgnuradio-soapy3.10.12`、`libgnuradio-trellis3.10.12`、`libgnuradio-uhd3.10.12`、`libgnuradio-video-sdl3.10.12`、`libgnuradio-vocoder3.10.12`、`libgnuradio-wavelet3.10.12`、`libgnuradio-zeromq3.10.12` |
| 安装体积 | 24.31 MB |
| 官网 | <https://www.gnuradio.org/> |
| 源码仓库 | <https://salsa.debian.org/bottoms/pkg-gnuradio> |
| 包追踪 | <https://pkg.kali.org/pkg/gnuradio> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gnuradio -h          # 查看用法
man gnuradio         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 48 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man dial_tone`

```text
root@kali:~# man dial_tone
DIAL_TONE(1)                     User Commands                     DIAL_TONE(1)
NAME
     dial_tone - dial tone example
DESCRIPTION
     GnuRadio Dial Tone example
OPTIONS
     None
     Play a Dial Tone on the sound card output device.
SEE ALSO
     The  c++  gnuradio  example  programs are in /usr/bin. There are also many
     Python and GnuRadio Companion examples in /usr/share/gnuradio/examples/...
     tags_demo(1)      uhd_rx_cfile(1)      uhd_rx_nogui(1)       uhd_siggen(1)
     uhd_siggen_gui(1)
DIAL_TONE 3.10.12.0                2026-06-29                      DIAL_TONE(1)
```

### `man display_qt`

> 官方示例调用：`man display_qt`

```text
root@kali:~# man display_qt
DISPLAY_QT(1)                    User Commands                    DISPLAY_QT(1)
NAME
     display_qt - a Gnu Radio Example gr-qtgui
DESCRIPTION
     Display a GUI using QT of a sine wave in noise.
     Example  program  instantiates  a  GNU  Radio flow graph using a sine wave
     source, a noise source, and gr-qtgui blocks. This new (in version  3.7.10)
     example shows how to build a C++ only QT based application.
SEE ALSO
     http://gnuradio.squarespace.com/examples/tag/qt
display_qt 3.10.12.0               2026-06-29                     DISPLAY_QT(1)
```

### `gnuradio-companion`

> 官方示例调用：`gnuradio-companion -h`

```text
root@kali:~# gnuradio-companion -h
usage: gnuradio-companion [-h] [--log {debug,info,warning,error,critical}]
                          [--qt | --gtk]
                          [flow_graphs ...]
GNU Radio Companion (3.10.12.0) - This program is part of GNU Radio. GRC comes
with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to
redistribute it.
positional arguments:
  flow_graphs
options:
  -h, --help            show this help message and exit
  --log {debug,info,warning,error,critical}
Framework:
  --qt                  GNU Radio Companion (QT)
  --gtk                 GNU Radio Companion (GTK)
```

### `gnuradio-config-info`

> 官方示例调用：`gnuradio-config-info -h`

```text
root@kali:~# gnuradio-config-info -h
Program options: gnuradio-config-info [options]:
  -h [ --help ]         print help message
  --print-all           print all information
  --prefix              print GNU Radio installation prefix
  --sysconfdir          print GNU Radio system configuration directory
  --prefsdir            print GNU Radio preferences directory
  --userprefsdir        print GNU Radio user preferences directory
  --persistentdir       print GNU Radio persistent state directory
  --prefs               print GNU Radio preferences
  --builddate           print GNU Radio build date (RFC2822 format)
  --enabled-components  print GNU Radio build time enabled components
  --cc                  print GNU Radio C compiler version
  --cxx                 print GNU Radio C++ compiler version
  --cflags              print GNU Radio CFLAGS
  -v [ --version ]      print GNU Radio version
  --pybind              print pybind11 version used in this build
```

### `gr-ctrlport-monitor`

> 官方示例调用：`gr-ctrlport-monitor -h`

```text
root@kali:~# gr-ctrlport-monitor -h
usage: gr-ctrlport-monitor [-h] [host] port
GNU Radio Control Port Monitor
positional arguments:
  host        host name or IP
  port        port
options:
  -h, --help  show this help message and exit
```

### `gr-perf-monitorx`

> 官方示例调用：`gr-perf-monitorx -h`

```text
root@kali:~# gr-perf-monitorx -h
usage: gr-perf-monitorx [-h] [host] port
GNU Radio Performance Monitor
positional arguments:
  host        host name or IP
  port        port
options:
  -h, --help  show this help message and exit
```

### `gr_filter_design`

> 官方示例调用：`gr_filter_design -h`

```text
root@kali:~# gr_filter_design -h
Usage: gr_filter_design: [options] (input_filename)
Options:
  -h, --help  show this help message and exit
```

### `gr_modtool`

> 官方示例调用：`gr_modtool --help`

```text
root@kali:~# gr_modtool --help
Usage: gr_modtool [OPTIONS] COMMAND [ARGS]...
  A tool for editing GNU Radio out-of-tree modules.
Options:
  --help  Show this message and exit.
Commands:
  add       Adds a block to the out-of-tree module.
  bind      Generate Python bindings for GR block
  disable   Disable selected block in module.
  help      Display help for gr_modtool (equivalent to `gr_modtool --help`).
  info      Return information about a given module
  makeyaml  Generate YAML files for GRC block bindings.
  newmod    Create new empty module, use add to add blocks.
  rename    Rename a block inside a module.
  rm        Remove a block from a module.
  update    Update the grc bindings for a block
  Manipulate the source code tree of a GNU Radio module. Call without options
  to run specified command interactively
```

### `gr_plot`

> 官方示例调用：`gr_plot -h`

```text
root@kali:~# gr_plot -h
usage: gr_plot [-h]
               [-d {complex64,float32,uint32,int32,uint16,int16,uint8,int8}]
               [-B BLOCK] [-s START] [-R SAMPLE_RATE]
               FILE [FILE ...]
Takes a GNU Radio binary file and displays the samples versus time. You can
set the block size to specify how many points to read in at a time and the
start position in the file. By default, the system assumes a sample rate of 1,
so in time, each sample is plotted versus the sample number. To set a true
time axis, set the sample rate (-R or --sample-rate) to the sample rate used
when capturing the samples.
positional arguments:
  FILE                  Input file with samples
options:
  -h, --help            show this help message and exit
  -d, --data-type {complex64,float32,uint32,int32,uint16,int16,uint8,int8}
                        Specify the data type [default='complex64']
  -B, --block BLOCK     Specify the block size [default=1000]
  -s, --start START     Specify where to start in the file [default=0]
  -R, --sample-rate SAMPLE_RATE
                        Set the sampler rate of the data [default=1.0]
```

### `gr_plot_const`

> 官方示例调用：`gr_plot_const -h`

```text
root@kali:~# gr_plot_const -h
usage: gr_plot_const [-h] [-B BLOCK] [-s START] [-R SAMPLE_RATE] FILE
Takes a GNU Radio complex binary file and displays the I&Q data versus time
and the constellation plot (I vs. Q). You can set the block size to specify
how many points to read in at a time and the start position in the file. By
default, the system assumes a sample rate of 1, so in time, each sample is
plotted versus the sample number. To set a true time axis, set the sample rate
(-R or --sample-rate) to the sample rate used when capturing the samples.
positional arguments:
  FILE                  Input file with complex samples
options:
  -h, --help            show this help message and exit
  -B, --block BLOCK     Specify the block size [default=1000]
  -s, --start START     Specify where to start in the file [default=0]
  -R, --sample-rate SAMPLE_RATE
                        Set the sampler rate of the data [default=1.0]
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install gnuradio`，再执行 `gnuradio --version` 2>/dev/null || `gnuradio -V`
- [ ] **2.** **读官方帮助** —— `gnuradio -h`，需要细节时 `man gnuradio`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: gr_filter_design: [options] (input_filename)`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gnuradio/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gnuradio/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gnuradio/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
