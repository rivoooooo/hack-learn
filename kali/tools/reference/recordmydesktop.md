# recordmydesktop

> Captures audio-video data of a Linux desktop session The application produces an ogg-encapsulated theora-vorbis file. recordMyDesktop tries to be as unobstrusive as possible by proccessing only regions of the screen that have changed

> **功能分类**：报告与记录 ｜ **Kali 包**：`recordmydesktop` ｜ **官方文档**：<https://www.kali.org/tools/recordmydesktop/>

## 1. 安装

```bash
sudo apt update
sudo apt install recordmydesktop
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.4.0 |
| 架构 | any |
| 可执行命令 | `recordmydesktop` |
| 依赖 | `libasound2t64`、`libc6` |
| 安装体积 | 126 KB |
| 官网 | <https://enselic.github.io/recordmydesktop/> |
| 源码仓库 | <https://salsa.debian.org/debian/recordmydesktop> |
| 包追踪 | <https://pkg.kali.org/pkg/recordmydesktop> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
recordmydesktop -h          # 查看用法
man recordmydesktop         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `recordmydesktop`

> 官方示例调用：`recordmydesktop -h`

```text
root@kali:~# recordmydesktop -h
Usage: recordmydesktop [OPTIONS]^filename
Generic Options
  -h, --help                              Print this help and exit.
      --version                           Print program version and exit.
      --print-config                      Print info about options selected
                                          during compilation and exit.
Image Options
      --windowid=id_of_window             id of window to be recorded.
      --display=DISPLAY                   Display to connect to.
  -x, --x=N>=0                            Offset in x direction.
  -y, --y=N>=0                            Offset in y direction.
      --width=N>0                         Width of recorded window.
      --height=N>0                        Height of recorded window.
      --dummy-cursor=color                Color of the dummy cursor
                                          [black|white]
      --no-cursor                         Disable drawing of the cursor.
      --no-shared                         Disable usage of MIT-shared memory
                                          extension(Not Recommended!).
      --full-shots                        Take full screenshot at every
                                          frame(Not recomended!).
      --follow-mouse                      Makes the capture area follow the
                                          mouse cursor. Autoenables
                                          --full-shots.
      --quick-subsampling                 Do subsampling of the chroma planes
                                          by discarding, not averaging.
      --fps=N(number>0.0)                 A positive number denoting desired
                                          framerate.
Sound Options
      --channels=N                        A positive number denoting desired
                                          sound channels in recording.
      --freq=N                            A positive number denoting desired
                                          sound frequency.
      --buffer-size=N                     A positive number denoting the
                                          desired sound buffer size (in
                                          frames,when using ALSA or OSS)
      --ring-buffer-size=N                A float number denoting the desired
                                          ring buffer size (in seconds,when
                                          using JACK only).
      --device=SOUND_DEVICE               Sound device(default default).
      --use-jack=port1 port2... portn     Record audio from the specified list
                                          of space-separated jack ports.
      --no-sound                          Do not record sound.
Encoding Options
      --on-the-fly-encoding               Encode the audio-video data, while
                                          recording.
      --v_quality=n                       A number from 0 to 63 for desired
                                          encoded video quality(default 63).
      --v_bitrate=n                       A number from 0 to 200000000 for
                                          desired encoded video
                                          bitrate(default 0).
      --s_quality=n                       Desired audio quality(-1 to 10).
Misc Options
      --rescue=path_to_data               Encode data from a previous,
                                          crashed, session.
      --no-wm-check                       Do not try to detect the window
                                          manager(and set options according to
                                          it)
      --no-frame                          Don not show the frame that
                                          visualizes the recorded area.
      --pause-shortcut=MOD+KEY            Shortcut that will be used for
                                          (un)pausing (default Control+Mod1+p).
      --stop-shortcut=MOD+KEY             Shortcut that will be used to stop
                                          the recording (default
                                          Control+Mod1+s).
      --compress-cache                    Image data are cached with light
                                          compression.
      --workdir=DIR                       Location where a temporary directory
                                          will be created to hold project
                                          files(default $HOME).
      --delay=n[H|h|M|m]                  Number of secs(default),minutes or
                                          hours before capture starts(number
                                          can be float)
      --overwrite                         If there is already a file with the
                                          same name, delete it (default is to
                                          add a number postfix to the new one).
  -o, --output=filename                   Name of recorded video(default
                                          out.ogv).
	If no other options are specified, filename can be given without the -o switch.
Updated on: 2026-Aug-25
 Edit this page
readpe
regripper
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install recordmydesktop`，再执行 `recordmydesktop --version` 2>/dev/null || `recordmydesktop -V`
- [ ] **2.** **读官方帮助** —— `recordmydesktop -h`，需要细节时 `man recordmydesktop`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: recordmydesktop [OPTIONS]^filename`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/recordmydesktop/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/recordmydesktop/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/recordmydesktop/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
