# gr-osmosdr

> GNU Radio blocks from the OsmoSDR project The Osmocom project is a family of projects regarding Open source mobile communications. While primarily being developed for the OsmoSDR hardware, this block as well supports: FUNcube Dongle throug…

> **功能分类**：无线攻击 ｜ **Kali 包**：`gr-osmosdr` ｜ **官方文档**：<https://www.kali.org/tools/gr-osmosdr/>

## 1. 安装

```bash
sudo apt update
sudo apt install gr-osmosdr
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.2.6 |
| 架构 | any |
| 可执行命令 | `gr-osmosdr`、`osmocom_fft`、`osmocom_siggen_nogui`、`gr-osmosdr-doc`、`libgnuradio-osmosdr0.2.0t64` |
| 依赖 | `libc6`、`libgcc-s1`、`libgnuradio-osmosdr0.2.0t64`、`libgnuradio-runtime3.10.12`、`libstdc++6`、`python3`、`python3` |
| 安装体积 | 770 KB |
| 官网 | <https://osmocom.org/projects/gr-osmosdr/wiki> |
| 源码仓库 | <https://salsa.debian.org/bottoms/pkg-gr-osmosdr> |
| 包追踪 | <https://pkg.kali.org/pkg/gr-osmosdr> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gr-osmosdr -h          # 查看用法
man gr-osmosdr         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 5 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man osmocom_fft`

```text
root@kali:~# man osmocom_fft
osmocom_fft(1)                   User Commands                   osmocom_fft(1)
NAME
     osmocom_fft - Spectrum Browser
SYNOPSIS
     osmocom_fft [options]
DESCRIPTION
     Spectrum Browser
OPTIONS
     -h, --help
            show this help message and exit
     -a ARGS, --args=ARGS
            Device args, [default=]
     -A ANTENNA, --antenna=ANTENNA
            Select RX antenna where appropriate
     -s SAMP_RATE, --samp-rate=SAMP_RATE
            Set sample rate (bandwidth), minimum by default
     -f FREQ, --center-freq=FREQ
            Set frequency to FREQ
     -c FREQ_CORR, --freq-corr=FREQ_CORR
            Set frequency correction (ppm)
     -g GAIN, --gain=GAIN
            Set gain in dB (default is midpoint)
     -W, --waterfall
            Enable waterfall display
     -S, --oscilloscope
            Enable oscilloscope display
     --avg-alpha=AVG_ALPHA
            Set fftsink averaging factor, default=[0.1]
     --averaging
            Enable fftsink averaging, default=[False]
     --ref-scale=REF_SCALE
            Set dBFS=0dB input value, default=[1.0]
     --fft-size=FFT_SIZE
            Set number of FFT bins [default=1024]
     --fft-rate=FFT_RATE
            Set FFT update rate, [default=30]
     -v, --verbose
            Use verbose console output [default=False]
SEE ALSO
     The  full  documentation for linux; is maintained as a Texinfo manual.  If
     the info and linux; programs are properly installed at your site, the com-
     mand
            info linux;
     should give you access to the complete manual.
Device specification
     You can specify the source or sink device using a comma  separated  string
     of  argument=value  pairs.  The always-up-to-date block documentation with
     examples is available right here.
FCD Source
     Argument
            Notes
     fcd=<device-index>
            0-based device identifier, optional
     device=hw:2
            overrides the audio device
     type=2
            selects the dongle type, 1 for Classic, 2 for Pro+
     The "device" argument overrides the audio device used  by  the  underlying
     driver to access the dongle's IQ sample stream.
     The "type" argument selects the dongle type, 1 for Classic, 2 for Pro+.
OsmoSDR Source
     Argument
            Notes
     osmosdr=<device-index>
            0-based device identifier
     buffers=<number-of-buffers>
            Default is 32
     buflen=<length-of-buffer>
            Default is 256kB, must be multiple of 512
RTL-SDR Source
     Argument
            Notes
     rtl=<device-index>
            0-based device identifier OR serial number
     rtl_xtal=<frequency>
            Frequency (Hz) used for the RTL chip, accepts eng notation
     tuner_xtal=<frequency>
            Frequency (Hz) used for the tuner chip, accepts eng notation
     buffers=<number-of-buffers>
            Default is 32
     buflen=<length-of-buffer>
            Default is 256kB, must be multiple of 512
     direct_samp=0|1|2
            Enable  direct  sampling mode on the RTL chip. 0: Disable, 1: use I
            channel, 2: use Q channel
     offset_tune=0|1
            Enable offset tune mode for E4000 tuners
     NOTE: use rtl_eeprom -s to program your own serial number to the device
     NOTE: if you don't specify rtl_xtal/tuner_xtal, the underlying driver will
     use 28.0MHz
RTL-SDR TCP Source
     Argument
            Notes
     rtl_tcp=<hostname>:<port>
            hostname defaults to "localhost", port to "1234"
     psize=<payload-size>
            Default is 16384 bytes
     direct_samp=0|1|2
            Enable direct sampling mode on the RTL chip  0=Off,  1=I-ADC  input
            enabled, 2=Q-ADC input enabled
     offset_tune=0|1
            Enable offset tune mode for E4000 tuners
Miri Source
     Argument
            Notes
     miri=<device-index>
            0-based device identifier
     buffers=<number-of-buffers>
            Default is 32
UHD Source / Sink
     Argument Notes
     uhd    Use this argument without a value
     nchan=<channel-count>
            For  multichannel  USRP  configurations use the subdev parameter to
            specify stream mapping
     subdev=<subdev-spec>
            Examples: "A:0", "B:0", "A:0 B:0" when nchan=2. Refer original  et-
            tus documentation on this
     lo_offset=<frequency>
            Offset frequency in Hz, must be within daughterboard bandwidth. Ac-
            cepts eng notation
     Additional  argument/value  pairs will be passed to the underlying driver,
     for more information see specifying the subdevice and common device  iden-
     tifiers in the Ettus documentation.
bladeRF Source / Sink
     Argument
            Notes
     bladerf[=0]
            0-based device identifier (optional)
     fw='/path/to/the/firmware.img'
            program MCU firmware from given file. usually not needed. power cy-
            cle required.
     fpga='/path/to/the/bitstream.rbf'
            load  FPGA bitstream from given file. required only at first run at
            the moment.
     feature=oversample|default
            controls bladeRF hardware features (default: default)
     sample_format=16bit|16bit_packed|8bit
            specifies the sample format to use (default: 16bit)
HackRF Source / Sink
     Argument
            Notes
     hackrf
            Use this argument without a value
     buffers=<number-of-buffers>
            Default is 32
     Only the first device found may be used at the moment because of libhackrf
     limitation.
     Transmit support has been verified  by  using  the  crc-mmbTools  DAB  sdr
     transmitter.
IQ File Source
     Argument
            Notes
     file=<path-to-file-name>
     freq=<frequency>
            Center frequency in Hz, accepts eng notation
     rate=<sampling-rate>
            Mandatory, in samples/s, accepts eng notation
     repeat=true|false
            Default is true
     throttle=true|false
            Throttle flow of samples, default is true
EXAMPLES
     osmocom_fft -a rtl=0 -v -f 100e6 -s 2.4e6 -g 15
     osmocom_fft -a hackrf -v
     osmocom_fft -a uhd -v
SEE ALSO
     osmocom_siggen(1) osmocom_siggen_nogui(1) osmocom_spectrum_sense(1)
OSMOCOM                           October 2013                   osmocom_fft(1)
```

### `osmocom_siggen_nogui`

> 官方示例调用：`osmocom_siggen_nogui -h`

```text
root@kali:~# osmocom_siggen_nogui -h
Usage: osmocom_siggen_nogui: [options]
Options:
  -h, --help            show this help message and exit
  -a ARGS, --args=ARGS  Device args, [default=]
  -A ANTENNA, --antenna=ANTENNA
                        Select Rx Antenna where appropriate
  --clock-source=CLOCK_SOURCE
                        Set the clock source; typically 'internal',
                        'external', 'external_1pps', 'mimo' or 'gpsdo'
  -s SAMP_RATE, --samp-rate=SAMP_RATE
                        Set sample rate (bandwidth), minimum by default
  -g GAIN, --gain=GAIN  Set gain in dB (default is midpoint)
  -G GAINS, --gains=GAINS
                        Set named gain in dB, name:gain,name:gain,...
  -f FREQ, --tx-freq=FREQ
                        Set carrier frequency to FREQ [default=mid-point]
  -c FREQ_CORR, --freq-corr=FREQ_CORR
                        Set carrier frequency correction [default=0]
  -x WAVEFORM_FREQ, --waveform-freq=WAVEFORM_FREQ
                        Set baseband waveform frequency to FREQ [default=0]
  -y WAVEFORM2_FREQ, --waveform2-freq=WAVEFORM2_FREQ
                        Set 2nd waveform frequency to FREQ [default=none]
  --sine                Generate a carrier modulated by a complex sine wave
  --const               Generate a constant carrier
  --offset=OFFSET       Set waveform phase offset to OFFSET [default=0]
  --gaussian            Generate Gaussian random output
  --uniform             Generate Uniform random output
  --2tone               Generate Two Tone signal for IMD testing
  --sweep               Generate a swept sine wave
  --gsm                 Generate GMSK modulated GSM Burst Sequence
  --amplitude=AMPL      Set output amplitude to AMPL (0.1-1.0) [default=0.3]
  -v, --verbose         Use verbose console output [default=False]
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install gr-osmosdr`，再执行 `gr-osmosdr --version` 2>/dev/null || `gr-osmosdr -V`
- [ ] **2.** **读官方帮助** —— `gr-osmosdr -h`，需要细节时 `man gr-osmosdr`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: osmocom_siggen_nogui: [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gr-osmosdr/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gr-osmosdr/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gr-osmosdr/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
