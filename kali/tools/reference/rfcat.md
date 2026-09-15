# rfcat

> Swiss army knife of sub-GHz radio Rfcat is a sub GHz analysis tool. The goals of the project are to reduce the time for security researchers to create needed tools for analyzing unknown targets, to aid in reverse-engineering of hardware.

> **功能分类**：无线攻击 ｜ **Kali 包**：`rfcat` ｜ **官方文档**：<https://www.kali.org/tools/rfcat/>

## 1. 安装

```bash
sudo apt update
sudo apt install rfcat
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.0.1 |
| 架构 | any |
| 可执行命令 | `rfcat`、`rfcat_bootloader`、`rfcat_msfrelay`、`rfcat_server` |
| 依赖 | `ipython3`、`python3`、`python3-ipython`、`python3-numpy`、`python3-pyside6.qtcore`、`python3-pyside6.qtgui`、`python3-pyside6.qtwidgets`、`python3-serial`、`python3-usb` |
| 安装体积 | 443 KB |
| 官网 | <https://github.com/atlas0fd00m/rfcat> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/rfcat> |
| 包追踪 | <https://pkg.kali.org/pkg/rfcat> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
rfcat -h          # 查看用法
man rfcat         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rfcat`

> 官方示例调用：`rfcat -h`

```text
root@kali:~# rfcat -h
usage: rfcat [-h] [-r] [-i INDEX] [-s] [-f CENTFREQ] [-c INC] [-n SPECCHANS]
             [--bootloader] [--force] [-S]
options:
  -h, --help            show this help message and exit
  -r, --research        Interactive Python and the "d" instance to talk to
                        your dongle. melikey longtime.
  -i, --index INDEX
  -s, --specan          start spectrum analyzer
  -f, --centfreq CENTFREQ
  -c, --inc INC
  -n, --specchans SPECCHANS
  --bootloader          trigger the bootloader (use in order to flash the
                        dongle)
  --force               use this to make sure you want to set bootloader mode
                        (you *must* flash after setting --bootloader)
  -S, --safemode        TROUBLESHOOTING ONLY, used with -r
```

### `rfcat_bootloader`

> 官方示例调用：`rfcat_bootloader -h`

```text
root@kali:~# rfcat_bootloader -h
CC Bootloader Download Utility
Usage:  /usr/bin/rfcat_bootloader serial_port command
Commands:
  download <hex_file>
    Download hex_file to the device.
  run
    Run the user code.
  reset
    The bootloader will not erase pages that have previously been written to
    before writing new data to that page. This allows for random access writes
    but prevents you from overwriting downloaded code unless the device is
    power cycled. This command will reset the bootloader's record of what
    pages have been written to, allowing you to overwrite without power
    cycling.
  erase_all
    Erases the entire user flash area.
  erase <n>
    Erases page n of the flash memory (organised into 1024 byte pages). The
    bootloader occupies the first few pages and the rest are reserved for user
    code. Attempting to erase a bootloader page will have no effect. To
    determine which page the user code starts on please check the
    USER_CODE_BASE setting in main.h.
  read <start_addr> <len> [hex_file]
    Reads len bytes from flash memory starting from start_addr and optionally
    write to hex_file. start_addr and len should be specified in hexadecimal
    (e.g. 0x1234).
  verify <hex_file>
    Verify hex_file matches device flash memory.
```

### `rfcat_msfrelay`

> 官方示例调用：`rfcat_msfrelay -h`

```text
root@kali:~# rfcat_msfrelay -h
usage: rfcat_msfrelay [-h] [-i INDEX] [-u USER] [-p PASSWORD] [-P PORT]
                      [--noauth] [--localonly]
options:
  -h, --help            show this help message and exit
  -i, --index INDEX
  -u, --user USER       HTTP Username
  -p, --password PASSWORD
                        HTTP Password
  -P, --Port PORT
  --noauth              Do not require authentication
  --localonly           Listen on localhost only
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install rfcat`，再执行 `rfcat --version` 2>/dev/null || `rfcat -V`
- [ ] **2.** **读官方帮助** —— `rfcat -h`，需要细节时 `man rfcat`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:  /usr/bin/rfcat_bootloader serial_port command`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rfcat/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rfcat/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rfcat/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
