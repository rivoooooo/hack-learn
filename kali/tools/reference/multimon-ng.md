# multimon-ng

> Digital radio transmission decoder The successor to multimon, with support for more modes and improved compatibility with moderns systems. It decodes the following digital transmission modes commonly found on VHF/UHF bands: POCSAG512 POCSA…

> **功能分类**：无线攻击 ｜ **Kali 包**：`multimon-ng` ｜ **官方文档**：<https://www.kali.org/tools/multimon-ng/>

## 1. 安装

```bash
sudo apt update
sudo apt install multimon-ng
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3.1 |
| 架构 | any |
| 可执行命令 | `multimon-ng` |
| 依赖 | `libc6`、`libpulse0`、`libx11-6` |
| 安装体积 | 134 KB |
| 官网 | <https://github.com/EliasOenal/multimon-ng/> |
| 源码仓库 | <https://salsa.debian.org/debian-hamradio-team/multimon-ng> |
| 包追踪 | <https://pkg.kali.org/pkg/multimon-ng> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Take raw input from rtl_fm (-t raw), add the POCSAG512, POCSAG1200, POCSAG2400, and SCOPE modules (-a POCSAG512 -a POCSAG1200 -a POCSAG2400 -a SCOPE), decode in alpha mode (-f alpha), reading from stdin (/dev/stdin):
root@kali:~# rtl_fm -f 149.614M -s 22050 -p -19 | multimon-ng -t raw -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -a SCOPE -f alpha /dev/stdin
multimon-ng  (C) 1996/1997 by Tom Sailer HB9JNX/AE4WA
             (C) 2012/2013 by Elias Oenal
available demodulators: POCSAG512 POCSAG1200 POCSAG2400 EAS UFSK1200 CLIPFSK AFSK1200 AFSK2400 AFSK2400_2 AFSK2400_3 HAPN4800 FSK9600 DTMF ZVEI1 ZVEI2 ZVEI3 DZVEI PZVEI EEA EIA CCIR SCOPE
Enabled demodulators: POCSAG512 POCSAG1200 POCSAG2400 SCOPE
Found 1 device(s):
  0:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: ezcap USB 2.0 DVB-T/DAB/FM dongle
Found Rafael Micro R820T tuner
Oversampling input by: 46x.
Oversampling output by: 1x.
Buffer size: 8.08ms
Tuned to 149867575 Hz.
Sampling at 1014300 Hz.
Output at 22050 Hz.
Exact sample rate is: 1014300.020041 Hz
Tuner gain set to automatic.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rtl_fm`

官方给出的调用示例：`rtl_fm -f 149.614M -s 22050 -p -19 | multimon-ng -t raw -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -a SCOPE -f alpha /dev/stdin`

```text
root@kali:~# rtl_fm -f 149.614M -s 22050 -p -19 | multimon-ng -t raw -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -a SCOPE -f alpha /dev/stdin
multimon-ng  (C) 1996/1997 by Tom Sailer HB9JNX/AE4WA
             (C) 2012/2013 by Elias Oenal
available demodulators: POCSAG512 POCSAG1200 POCSAG2400 EAS UFSK1200 CLIPFSK AFSK1200 AFSK2400 AFSK2400_2 AFSK2400_3 HAPN4800 FSK9600 DTMF ZVEI1 ZVEI2 ZVEI3 DZVEI PZVEI EEA EIA CCIR SCOPE
Enabled demodulators: POCSAG512 POCSAG1200 POCSAG2400 SCOPE
Found 1 device(s):
  0:  Realtek, RTL2838UHIDIR, SN: 00000001
Using device 0: ezcap USB 2.0 DVB-T/DAB/FM dongle
Found Rafael Micro R820T tuner
Oversampling input by: 46x.
Oversampling output by: 1x.
Buffer size: 8.08ms
Tuned to 149867575 Hz.
Sampling at 1014300 Hz.
Output at 22050 Hz.
Exact sample rate is: 1014300.020041 Hz
Tuner gain set to automatic.
```

### `multimon-ng`

官方给出的调用示例：`multimon-ng --help`

```text
root@kali:~# multimon-ng --help
multimon-ng: unrecognized option '--help'
multimon-ng 1.3.1
  (C) 1996/1997 by Tom Sailer HB9JNX/AE4WA
  (C) 2012-2024 by Elias Oenal
Available demodulators: POCSAG512 POCSAG1200 POCSAG2400 FLEX FLEX_NEXT EAS UFSK1200 CLIPFSK FMSFSK AFSK1200 AFSK2400 AFSK2400_2 AFSK2400_3 HAPN4800 FSK9600 DTMF ZVEI1 ZVEI2 ZVEI3 DZVEI PZVEI EEA EIA CCIR MORSE_CW DUMPCSV X10 SCOPE
Usage: multimon-ng [file] [file] [file] ...
  If no [file] is given, input will be read from your default sound
  hardware. A filename of "-" denotes standard input.
  -t <type>  : Input file type (any other type than raw requires sox)
  -a <demod> : Add demodulator
  -s <demod> : Subtract demodulator
  -c         : Remove all demodulators (must be added with -a <demod>)
  -q         : Quiet
  -v <level> : Level of verbosity (e.g. '-v 3')
               For POCSAG and MORSE_CW '-v1' prints decoding statistics.
  -h         : This help
  -A         : APRS mode (TNC2 text output)
  -m         : Mute SoX warnings
  -r         : Call SoX in repeatable mode (e.g. fixed random seed for dithering)
  -n         : Don't flush stdout, increases performance.
  -j         : FMS: Just output hex data and CRC, no parsing.
  -e         : POCSAG: Hide empty messages.
  -u         : POCSAG: Heuristically prune unlikely decodes.
  -i         : POCSAG: Inverts the input samples. Try this if decoding fails.
  -p         : POCSAG: Show partially received messages.
  -f <mode>  : POCSAG: Overrides standards and forces decoding of data as <mode>
                       (<mode> can be 'numeric', 'alpha', 'skyper' or 'auto')
  -b <level> : POCSAG: BCH bit error correction level. Set 0 to disable, default is 2.
                       Lower levels increase performance and lower false positives.
  -C <cs>    : POCSAG: Set Charset.
  -o         : CW: Set threshold for dit detection (default: 500)
  -d         : CW: Dit length in ms (default: 50)
  -g         : CW: Gap length in ms (default: 50)
  -x         : CW: Disable auto threshold detection
  -y         : CW: Disable auto timing detection
  --timestamp: Add a time stamp in front of every printed line
  --label    : Add a label to the front of every printed line
   Raw input requires one channel, 16 bit, signed integer (platform-native)
   samples at the demodulator's input sampling rate, which is
   usually 22050 Hz. Raw input is assumed and required if piped input is used.
Updated on: 2026-Mar-02
 Edit this page
multimac
nipper-ng
LIGHT
DARK
Links
Home
Download / Get Kali
Blog
OS Documentation
Tool Documentation
System Status
Archived Releases
Partnerships
Platforms
ARM (SBC)
NetHunter (Mobile)
Amazon AWS
Docker
Linode
Microsoft Azure
Microsoft Store (WSL)
Vagrant
Development
Bug Tracker
Continuous Integration
Network Mirror
Package Tracker
GitLab
Community
Discord
Support Forum
PeerTube
Follow Us
Bluesky
Facebook
Instagram
Mastodon
Substack
X
Newsletter
RSS
Policies
Cookie Policy
Privacy Policy
Trademark Policy
© OffSec Services Limited 2026. All rights reserved.
Kali Linux is part of OffSec's Community Projects
Learn more about OffSec's free, open-source penetration testing tools for cybersecurity professionals
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install multimon-ng`，再执行 `multimon-ng --version` 2>/dev/null || `multimon-ng -V`
- [ ] **2.** **读官方帮助** —— `multimon-ng -h`，需要细节时 `man multimon-ng`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: multimon-ng [file] [file] [file] ...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/multimon-ng/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/multimon-ng/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/multimon-ng/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
