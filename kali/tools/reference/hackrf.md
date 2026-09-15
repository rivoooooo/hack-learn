# hackrf

> Software defined radio peripheral - utilities HackRF is an open source Software Defined Radio that can receive and transmit between 30 MHz and 6 GHz. HackRF has a 20 MHz bandwidth. It is a High Speed USB device powered by the USB bus. This…

> **功能分类**：无线攻击 ｜ **Kali 包**：`hackrf` ｜ **官方文档**：<https://www.kali.org/tools/hackrf/>

## 1. 安装

```bash
sudo apt update
sudo apt install hackrf
```

| 项目 | 内容 |
|------|------|
| 版本 | 2026.01.3 |
| 架构 | any |
| 可执行命令 | `hackrf`、`hackrf_biast`、`hackrf_clock`、`hackrf_cpldjtag`、`hackrf_debug`、`hackrf_info`、`hackrf_operacake`、`hackrf_spiflash`、`hackrf_sweep`、`hackrf_transfer`、`hackrf-doc`、`hackrf-firmware`、`libhackrf-dev`、`libhackrf0` |
| 依赖 | `libc6`、`libfftw3-single3`、`libhackrf0`、`hackrf_biast` |
| 安装体积 | 216 KB |
| 官网 | <http://greatscottgadgets.com/hackrf/> |
| 源码仓库 | <https://salsa.debian.org/bottoms/pkg-hackrf> |
| 包追踪 | <https://pkg.kali.org/pkg/hackrf> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
hackrf -h          # 查看用法
man hackrf         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 14 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hackrf_biast`

> 官方示例调用：`hackrf_biast --help`

```text
root@kali:~# hackrf_biast --help
hackrf_biast: invalid option -- '-'
hackrf_biast - enable/disable antenna power on the HackRF for compatibility
               with software that does not support this function
Usage:
  -h         Display this help
  -R         Reset all bias tee settings to device default.  When combined
             with -r/-t/-o, those settings will take precedence.
  [-b mode]  1=Enable bias tee immediately, 0=disable immediately
  [-r mode]  Set default bias tee power when device enters RX mode
  [-t mode]  Set default bias tee power when device enters TX mode
  [-o mode]  Set default bias tee power when device enters OFF mode
  [-d serial_number]  Specify serial number of HackRF device to configure
The -r/-t/-o options support the following mode settings:
  leave		do nothing when entering mode
  on		enable bias tee when entering mode
  off		disable bias tee when entering mode
```

### `hackrf_clock`

> 官方示例调用：`hackrf_clock -h`

```text
root@kali:~# hackrf_clock -h
hackrf_clock - HackRF clock configuration utility
Usage:
	-h, --help: this help
	-r, --read <clock_num>: read settings for clock_num
	-a, --all: read settings for all clocks
	-i, --clkin: get CLKIN status
	-o, --clkout <clkout_enable>: enable/disable CLKOUT
	-1, --p1 <signal>: select the HackRF Pro P1 SMA connector signal (default: clkin)
	one of: clkin, trigger_in, trigger_out, p22_clkin, pps_out, aux_clk1, aux_clk2, off
	-2, --p2 <signal>: select the signal for the HackRF Pro P2 SMA connector (default: clkout)
	one of: clkout, trigger_in, trigger_out
	-d, --device <serial_number>: Serial number of desired HackRF.
Examples:
	hackrf_clock -r 3 : prints settings for CLKOUT
```

### `hackrf_cpldjtag`

> 官方示例调用：`hackrf_cpldjtag -h`

```text
root@kali:~# hackrf_cpldjtag -h
Usage:
	-h, --help: this help
	-x, --xsvf <filename>: XSVF file to be written to CPLD.
	-d, --device <serialnumber>: Serial number of device, if multiple devices
```

### `hackrf_debug`

> 官方示例调用：`hackrf_debug -h`

```text
root@kali:~# hackrf_debug -h
Usage:
	-h, --help: this help
	-n, --register <n>: set register number for read/write operations
	-r, --read: read register specified by last -n argument, or all registers
	-w, --write <v>: write register specified by last -n argument with value <v>
	-c, --config: print SI5351C multisynth configuration information
	-d, --device <s>: specify a particular device by serial number
	-m, --max283x: target MAX283x
	-s, --si5351c: target SI5351C
	-f, --rffc5072: target RFFC5072
	-g, --gateware: target gateware registers
	-P, --fpga <n>: load the n-th bitstream to the FPGA
	-1, --p1 <n>: P1 control
	-2, --p2 <n>: P2 control
	-C, --clkin <0/1>: CLKIN control (0 for P1_CLKIN, 1 for P22_CLKIN)
	-N, --narrowband <0/1>: narrowband filter disable/enable
	-S, --state: display M0 state
	-T, --tx-underrun-limit <n>: set TX underrun limit in bytes (0 for no limit)
	-R, --rx-overrun-limit <n>: set RX overrun limit in bytes (0 for no limit)
	-u, --ui <1/0>: enable/disable UI
	-l, --leds <state>: configure LED state (0 for all off, 1 for default)
	-t, --selftest: read self-test report
	-o, --rtc-osc: test 32.768kHz RTC oscillator
	-a, --adc <channel>: read value from an ADC channel. Add 0x80 for alternate pin
Examples:
	hackrf_debug --si5351c -n 0 -r     # reads from si5351c register 0
	hackrf_debug --si5351c -c          # displays si5351c multisynth configuration
	hackrf_debug --rffc5072 -r         # reads all rffc5072 registers
	hackrf_debug --max283x -n 10 -w 22 # writes max283x register 10 with 22 decimal
	hackrf_debug --state               # displays M0 state
```

### `man`

> 官方示例调用：`man hackrf_info`

```text
root@kali:~# man hackrf_info
hackrf_info(1)                   User Commands                   hackrf_info(1)
NAME
     hackrf_info - probe device and show configuration
DESCRIPTION
     The  HackRF  project  started  by Michael Ossmann and Jared Boone to build
     software radio peripheral using Free Software and  Free  Hardware  design.
     Care was taken to only use electronic components with published documenta-
     tion  (no  NDAs!)  and to avoid software libraries without open source li-
     censes.
     Jawbreaker is the first complete HackRF platform, a wideband software  ra-
     dio transceiver with a USB interface.
     This application lets the user probe the device and show configuration.
SYNOPSIS
     hackrf_info
OPTIONS
     none
SEE ALSO
     Great Scott Gadgets HackRF web page: http://greatscottgadgets.com/hackrf/
     Other hackrf programs:
     hackrf_cpldjtag(1),  hackrf_debug(1),  hackrf_info(1), hackrf_spiflash(1),
     hackrf_transfer(1)
AUTHOR
     This manual page was written by Maitland Bottoms for  the  Debian  project
     (but may be used by others).
COPYRIGHT
     Copyright (c) 2013 A. Maitland Bottoms <
[email protected]
>
     This  program  is  free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the Free
     Software Foundation, either version 2 of the License, or (at your  option)
     any later version.
     This  program is distributed in the hope that it will be useful, but WITH-
     OUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY  or
     FITNESS  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
     more details.
HACKRF                             2013.07.1                     hackrf_info(1)
```

### `hackrf_operacake`

> 官方示例调用：`hackrf_operacake -h`

```text
root@kali:~# hackrf_operacake -h
Usage:
	-h, --help: this help
	-d, --device <n>: specify a particular device by serial number
	-o, --address <n>: specify a particular Opera Cake by address [default: 0]
	-m, --mode <mode>: specify switching mode [options: manual, frequency, time]
	-a <port>: set port connected to port A0
	-b <port>: set port connected to port B0
	-f <port:min:max>: automatically assign <port> for range <min:max> in MHz. This argument can be repeated to specify a list of ports.
	-t <port:dwell>: in time mode, dwell on <port> for <dwell> samples. Specify only <port> to use the default dwell time (with -w). This argument can be repeated to specify a list of ports.
	-w <n>: set default dwell time in samples for time mode
	-l, --list: list available Opera Cake boards
	-g, --gpio_test: test GPIO functionality of an Opera Cake
```

### `hackrf_spiflash`

> 官方示例调用：`hackrf_spiflash -h`

```text
root@kali:~# hackrf_spiflash -h
Usage:
	-h, --help: this help
	-a, --address <n>: starting address (default: 0)
	-l, --length <n>: number of bytes to read (default: all)
	-r, --read <filename>: Read data into file.
	-w, --write <filename>: Write data from file.
	-i, --no-check: Skip check for firmware compatibility with target device.
	-d, --device <serialnumber>: Serial number of device, if multiple devices
	-s, --status: Read SPI flash status registers before other operations.
	-c, --clear: Clear SPI flash status registers before other operations.
	-R, --reset: Reset HackRF after other operations.
	-v, --verbose: Verbose output.
```

### `hackrf_sweep`

> 官方示例调用：`hackrf_sweep --help`

```text
root@kali:~# hackrf_sweep --help
hackrf_sweep: invalid option -- '-'
Usage:
	[-h] # this help
	[-d serial_number] # Serial number of desired HackRF
	[-a amp_enable] # RX RF amplifier 1=Enable, 0=Disable
	[-f freq_min:freq_max] # minimum and maximum frequencies in MHz
	[-p antenna_enable] # Antenna port power, 1=Enable, 0=Disable
	[-l gain_db] # RX LNA (IF) gain, 0-40dB, 8dB steps
	[-g gain_db] # RX VGA (baseband) gain, 0-62dB, 2dB steps
	[-w bin_width] # FFT bin width (frequency resolution) in Hz, 2445-5000000
	[-W wisdom_file] # Use FFTW wisdom file (will be created if necessary)
	[-P estimate|measure|patient|exhaustive] # FFTW plan type, default is 'measure'
	[-1] # one shot mode
	[-N num_sweeps] # Number of sweeps to perform
	[-B] # binary output
	[-I] # binary inverse FFT output
	[-n] # keep the same timestamp within a sweep
	-r filename # output file
Output fields:
	date, time, hz_low, hz_high, hz_bin_width, num_samples, dB, dB, . . .
```

### `hackrf_transfer`

> 官方示例调用：`hackrf_transfer -h`

```text
root@kali:~# hackrf_transfer -h
Usage:
	-h # this help
	[-d serial_number] # Serial number of desired HackRF.
	-r <filename> # Receive data into file (use '-' for stdout).
	-t <filename> # Transmit data from file (use '-' for stdin).
	-w # Receive data into file with WAV header and automatic name.
	   # This is for SDR# compatibility and may not work with other software.
	[-f freq_hz] # Frequency in Hz [1MHz to 6000MHz supported, 0MHz to 7250MHz forceable].
	[-i if_freq_hz] # Intermediate Frequency (IF) in Hz [2170MHz to 2740MHz supported, 2000MHz to 3000MHz forceable].
	[-o lo_freq_hz] # Front-end Local Oscillator (LO) frequency in Hz [84MHz to 5400MHz].
	[-m image_reject] # Image rejection filter selection, 0=bypass, 1=low pass, 2=high pass.
	[-a amp_enable] # RX/TX RF amplifier 1=Enable, 0=Disable.
	[-p antenna_enable] # Antenna port power, 1=Enable, 0=Disable.
	[-l gain_db] # RX LNA (IF) gain, 0-40dB, 8dB steps
	[-g gain_db] # RX VGA (baseband) gain, 0-62dB, 2dB steps
	[-x gain_db] # TX VGA (IF) gain, 0-47dB, 1dB steps
	[-s sample_rate_hz] # Sample rate in Hz (2-20MHz supported, default 10MHz).
	[-F force] # Force use of parameters outside supported ranges.
	[-n num_samples] # Number of samples to transfer (default is unlimited).
	[-S buf_size] # Enable receive streaming with buffer size buf_size.
	[-B] # Print buffer statistics during transfer
	[-c amplitude] # CW signal source mode, amplitude 0-127 (DC value to DAC).
	[-R] # Repeat TX mode (default is off)
	[-b baseband_filter_bw_hz] # Set baseband filter bandwidth in Hz.
	Possible values: 1.75/2.5/3.5/5/5.5/6/7/8/9/10/12/14/15/20/24/28MHz, default <= 0.75 * sample_rate_hz.
	[-C ppm] # Set Internal crystal clock error in ppm.
	[-H] # Synchronize RX/TX to external trigger input.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install hackrf`，再执行 `hackrf --version` 2>/dev/null || `hackrf -V`
- [ ] **2.** **读官方帮助** —— `hackrf -h`，需要细节时 `man hackrf`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hackrf/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hackrf/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hackrf/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
