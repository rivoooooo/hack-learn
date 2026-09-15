# proxmark3

> Firmware, flasher, and client for the Proxmark3 This package contains the client and tools for the Proxmark3. It is dedicated to bringing the most out of the new features for Proxmark3 RDV4.0 new hardware and design but it will also suppor…

> **功能分类**：无线攻击 ｜ **Kali 包**：`proxmark3` ｜ **官方文档**：<https://www.kali.org/tools/proxmark3/>

## 1. 安装

```bash
sudo apt update
sudo apt install proxmark3
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.21611 |
| 架构 | any |
| 可执行命令 | `proxmark3`、`proxmark3-common`、`pm3`、`pm3-flash`、`pm3-flash-all`、`pm3-flash-bootrom`、`pm3-flash-fullimage`、`proxmark3-doc`、`proxmark3-firmwares` |
| 依赖 | `libbluetooth3`、`libbz2-1.0`、`libc6`、`libgcc-s1`、`libjansson4`、`liblz4-1`、`libpython3.14`、`libqt6core6t64`、`libqt6gui6`、`libqt6widgets6`、`libreadline8t64`、`libssl3t64` 等 |
| 安装体积 | 6.70 MB |
| 官网 | <https://github.com/RfidResearchGroup/proxmark3> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/proxmark3> |
| 包追踪 | <https://pkg.kali.org/pkg/proxmark3> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
proxmark3 -h          # 查看用法
man proxmark3         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 9 个可执行命令，下面是官方页面内嵌的帮助原文。

### `proxmark3`

> 官方示例调用：`proxmark3 -h`

```text
root@kali:~# proxmark3 -h
syntax: proxmark3 [-h|-t|-m|--fulltext]
        proxmark3 [[-p] <port>] [-b] [-w] [-f] [-d <0|1|2>] [--incognito] [--ncpu <num_cores>] [-c "<command>"]|[-l <lua_script_file>]|[-y <python_script_file>]|[-s <cmd_script_file>] [-i] [-- <arg0> <arg1>...]
        proxmark3 [-p] <port> --flash [--unlock-bootloader] [--image <imagefile>]+ [-w] [-f] [-d <0|1|2>]
Common options:
      -h/--help                           this help
      -v/--version                        print client version
      -p/--port                           serial port to connect to
      -w/--wait                           20sec waiting the serial port to appear in the OS
      -f/--flush                          output will be flushed after every print
      -d/--debug <0|1|2>                  set debugmode
Options in client mode:
      -t/--text                           dump all interactive command list at once
      --fulltext                          dump all interactive command's help at once
      -m/--markdown                       dump all interactive command list at once in markdown syntax
      -b/--baud                           serial port speed (only needed for physical UART, not for USB-CDC or BT)
      --incognito                         do not use history, prefs file nor log files
      --ncpu <num_cores>                  override number of CPU cores
      -c/--command "<command>"          execute one Proxmark3 command (or several separated by ';').
      -l/--lua <lua_script_file>          execute Lua script.
      -y/--py <python_script_file>        execute Python script.
      -s/--script-file <cmd_script_file>  script file with one Proxmark3 command per line
      -i/--interactive                    enter interactive mode after executing the script or the command
      -- <arg0> <arg1>...                 all args following -- are passed to the client command line
Options in flasher mode:
      --flash                             flash Proxmark3, requires at least one --image
      --reboot-to-bootloader              reboot Proxmark3 into bootloader mode
      --unlock-bootloader                 Enable flashing of bootloader area *DANGEROUS* (need --flash)
      --force                             Enable flashing even if firmware seems to not match client version
      --image <imagefile>                 image to flash. Can be specified several times.
Options in memory dump mode:
      --dumpmem <dumpfile>                dumps Proxmark3 flash memory to file
      --dumpaddr <address>                starting address for dump, default 0
      --dumplen <length>                  number of bytes to dump, default 512KB
      --dumpraw                           raw address mode: dump from anywhere, not just flash
Examples:
  to run Proxmark3 client:
      proxmark3 /dev/ttyACM0                       -- runs the pm3 client
      proxmark3 /dev/ttyACM0 -f                    -- flush output every time
      proxmark3 /dev/ttyACM0 -w                    -- wait for serial port
      proxmark3                                    -- runs the pm3 client in OFFLINE mode
  to execute different commands from terminal:
      proxmark3 /dev/ttyACM0 -c "hf mf chk --1k"   -- execute cmd and quit client
      proxmark3 /dev/ttyACM0 -l hf_read            -- execute Lua script `hf_read` and quit client
      proxmark3 /dev/ttyACM0 -s mycmds.txt         -- execute each pm3 cmd in file and quit client
  to flash fullimage and bootloader:
      proxmark3 /dev/ttyACM0 --flash --unlock-bootloader --image bootrom.elf --image fullimage.elf
Note (Linux):
if the flasher gets stuck in 'Waiting for Proxmark3 to reappear on <DEVICE>',
you need to blacklist Proxmark3 for modem-manager - see documentation for more details:
* https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/md/Installation_Instructions/ModemManager-Must-Be-Discarded.md
More info on flashing procedure from the official Proxmark3 wiki:
* https://github.com/Proxmark/proxmark3/wiki/Gentoo%20Linux
* https://github.com/Proxmark/proxmark3/wiki/Ubuntu%20Linux
* https://github.com/Proxmark/proxmark3/wiki/OSX
```

### `pm3`

> 官方示例调用：`pm3 -h`

```text
root@kali:~# pm3 -h
Quick helper script for proxmark3 client when working with a Proxmark3 device
Description:
    The usage is the same as for the proxmark3 client, with the following differences:
     * the correct port name will be automatically guessed;
     * the script will wait for a Proxmark3 to be connected (same as option -w of the client).
    You can also specify a first option -n N to access the Nth Proxmark3 connected.
    To see a list of available ports, use --list.
Usage:
    pm3 [-n <N>] [<any other proxmark3 client option>]
    pm3 [--list] [-h|--help] [-hh|--helpclient]
    pm3 [-o|--offline]
Arguments:
    -h/--help        this help
    -hh/--helpclient proxmark3 client help (the script will forward these options)
    --list           list all detected com ports
    -n <N>           connect device referred to the N:th number on the --list output
    -o/--offline     shortcut to use directly the proxmark3 client without guessing ports
Samples:
    ./pm3                       -- Auto detect/ select com port in the following order BT, USB/CDC, BT DONGLE
    ./pm3 -p /dev/ttyACM0       -- connect to port /dev/ttyACM0
    ./pm3 -n 2                  -- use second item from the --list output
    ./pm3 -c 'lf search' -i     -- run command and stay in client once completed
```

### `pm3-flash`

> 官方示例调用：`pm3-flash -h`

```text
root@kali:~# pm3-flash -h
Quick helper script for flashing a Proxmark3 device via USB
Description:
    The usage is similar to the old proxmark3-flasher binary, except that the correct port name will be automatically guessed.
    You can also specify a first option -n N to access the Nth Proxmark3 connected on USB.
    If this doesn't work, you'll have to use manually the proxmark3 client, see "/usr/bin/proxmark3 -h".
    To see a list of available ports, use --list.
Usage:
    pm3-flash [-n <N>] [-b] image.elf [image.elf...]
    pm3-flash --list
Options:
    -b         Enable flashing of bootloader area (DANGEROUS)
Example:
     pm3-flash -b bootrom.elf fullimage.elf
```

### `pm3-flash-all`

> 官方示例调用：`pm3-flash-all -h`

```text
root@kali:~# pm3-flash-all -h
Quick helper script for flashing a Proxmark3 device via USB
Description:
    The correct port name will be automatically guessed and the stock bootloader and firmware image will be flashed.
    You can also specify a first option -n N to access the Nth Proxmark3 connected on USB.
    If this doesn't work, you'll have to use manually the proxmark3 client, see "/usr/bin/proxmark3 -h".
    To see a list of available ports, use --list.
Usage:
    pm3-flash-all [-n <N>]
    pm3-flash-all --list
```

### `pm3-flash-bootrom`

> 官方示例调用：`pm3-flash-bootrom -h`

```text
root@kali:~# pm3-flash-bootrom -h
Quick helper script for flashing a Proxmark3 device via USB
Description:
    The correct port name will be automatically guessed and the stock bootloader will be flashed.
    You can also specify a first option -n N to access the Nth Proxmark3 connected on USB.
    If this doesn't work, you'll have to use manually the proxmark3 client, see "/usr/bin/proxmark3 -h".
    To see a list of available ports, use --list.
Usage:
    pm3-flash-bootrom [-n <N>]
    pm3-flash-bootrom --list
```

### `pm3-flash-fullimage`

> 官方示例调用：`pm3-flash-fullimage -h`

```text
root@kali:~# pm3-flash-fullimage -h
Quick helper script for flashing a Proxmark3 device via USB
Description:
    The correct port name will be automatically guessed and the stock firmware image will be flashed.
    You can also specify a first option -n N to access the Nth Proxmark3 connected on USB.
    If this doesn't work, you'll have to use manually the proxmark3 client, see "/usr/bin/proxmark3 -h".
    To see a list of available ports, use --list.
Usage:
    pm3-flash-fullimage [-n <N>]
    pm3-flash-fullimage --list
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install proxmark3`，再执行 `proxmark3 --version` 2>/dev/null || `proxmark3 -V`
- [ ] **2.** **读官方帮助** —— `proxmark3 -h`，需要细节时 `man proxmark3`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/proxmark3/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/proxmark3/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/proxmark3/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
