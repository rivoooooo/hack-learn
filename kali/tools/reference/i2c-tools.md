# i2c-tools

> Heterogeneous set of I2C tools for Linux This package contains a heterogeneous set of I2C tools for Linux: a bus probing tool, a chip dumper, register-level access helpers, EEPROM decoding scripts, and more.

> **功能分类**：通用工具 ｜ **Kali 包**：`i2c-tools` ｜ **官方文档**：<https://www.kali.org/tools/i2c-tools/>

## 1. 安装

```bash
sudo apt update
sudo apt install i2c-tools
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.4 |
| 架构 | linux-any |
| 可执行命令 | `i2c-tools`、`ddcmon`、`decode-dimms`、`decode-edid`、`decode-vaio`、`i2c-stub-from-dump`、`i2cdetect`、`i2cdump`、`i2cget`、`i2cset`、`i2ctransfer`、`libi2c-dev`、`libi2c0`、`python3-smbus` |
| 依赖 | `libc6`、`libi2c0`、`perl` |
| 安装体积 | 331 KB |
| 官网 | <https://www.kernel.org/pub/software/utils/i2c-tools/> |
| 源码仓库 | <https://salsa.debian.org/aurel32/i2c-tools> |
| 包追踪 | <https://pkg.kali.org/pkg/i2c-tools> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
i2c-tools -h          # 查看用法
man i2c-tools         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 14 个可执行命令，下面是官方页面内嵌的帮助原文。

### `decode-dimms`

> 官方示例调用：`decode-dimms -h`

```text
root@kali:~# decode-dimms -h
Usage: /usr/bin/decode-dimms [-c] [-f [-b]] [-x|-X file [files..]]
       /usr/bin/decode-dimms -h
  -f, --format            Print nice html output
  -b, --bodyonly          Don't print html header
                          (useful for postprocessing the output)
      --side-by-side      Display all DIMMs side-by-side if possible
      --merge-cells       Merge neighbour cells with identical values
                          (side-by-side output only, default)
      --no-merge-cells    Don't merge neighbour cells with identical values
                          (side-by-side output only)
  -c, --checksum          Decode completely even if checksum fails
  -x,                     Read data from hexdump files
  -X,                     Same as -x except treat multibyte hex
                          data as little endian
  -h, --help              Display this usage summary
Hexdumps can be the output from hexdump, hexdump -C, i2cdump, eeprog and
likely many other progams producing hex dumps of one kind or another.  Note
that the default output of "hexdump" will be byte-swapped on little-endian
systems and you must use -X instead of -x, otherwise the dump will not be
parsed correctly.  It is better to use "hexdump -C", which is not ambiguous.
```

### `decode-vaio`

> 官方示例调用：`decode-vaio -h`

```text
root@kali:~# decode-vaio -h
# Sony Vaio EEPROM Decoder version 1.7 by Jean Delvare
Vaio EEPROM not found.  Please make sure that the at24 or eeprom module is loaded.
```

### `i2c-stub-from-dump`

> 官方示例调用：`i2c-stub-from-dump -h`

```text
root@kali:~# i2c-stub-from-dump -h
Usage: i2c-stub-from-dump <addr>[,<addr>,...] <dump file> [<dump file> ...]
```

### `i2cdetect`

> 官方示例调用：`i2cdetect -h`

```text
root@kali:~# i2cdetect -h
Usage: i2cdetect [-y] [-a] [-q|-r] I2CBUS [FIRST LAST]
       i2cdetect -F I2CBUS
       i2cdetect -l
  I2CBUS is an integer or an I2C bus name
  If provided, FIRST and LAST limit the probing range.
```

### `i2cdump`

> 官方示例调用：`i2cdump -h`

```text
root@kali:~# i2cdump -h
Usage: i2cdump [-f] [-y] [-r first-last] [-a] I2CBUS ADDRESS [MODE [BANK [BANKREG]]]
  I2CBUS is an integer or an I2C bus name
  ADDRESS is an integer (0x08 - 0x77, or 0x00 - 0x7f if -a is given)
  MODE is one of:
    b (byte, default)
    w (word)
    W (word on even register addresses)
    i (I2C block)
    c (consecutive byte)
    Append p for SMBus PEC
```

### `i2cget`

> 官方示例调用：`i2cget -h`

```text
root@kali:~# i2cget -h
Usage: i2cget [-f] [-y] [-a] I2CBUS CHIP-ADDRESS [DATA-ADDRESS [MODE [LENGTH]]]
  I2CBUS is an integer or an I2C bus name
  ADDRESS is an integer (0x08 - 0x77, or 0x00 - 0x7f if -a is given)
  MODE is one of:
    b (read byte data, default)
    w (read word data)
    c (write byte/read byte)
    s (read SMBus block data)
    i (read I2C block data)
    Append p for SMBus PEC
  LENGTH is the I2C block data length (between 1 and 32, default 32)
```

### `i2cset`

> 官方示例调用：`i2cset -h`

```text
root@kali:~# i2cset -h
Usage: i2cset [-f] [-y] [-m MASK] [-r] [-a] I2CBUS CHIP-ADDRESS DATA-ADDRESS [VALUE] ... [MODE]
  I2CBUS is an integer or an I2C bus name
  ADDRESS is an integer (0x08 - 0x77, or 0x00 - 0x7f if -a is given)
  MODE is one of:
    c (byte, no value)
    b (byte data, default)
    w (word data)
    i (I2C block data)
    s (SMBus block data)
    Append p for SMBus PEC
```

### `i2ctransfer`

> 官方示例调用：`i2ctransfer -h`

```text
root@kali:~# i2ctransfer -h
Usage: i2ctransfer [OPTIONS] I2CBUS DESC [DATA] [DESC [DATA]]...
  OPTIONS: -a allow even reserved addresses
           -b print read data as binary, disables -v
           -f force access even if address is marked used
           -h this help text
           -v verbose mode
           -V version info
           -y yes to all confirmations
  I2CBUS is an integer or an I2C bus name
  DESC describes the transfer in the form: {r|w}LENGTH[@address]
    1) read/write-flag 2) LENGTH (range 0-65535, or '?')
    3) I2C address (use last one if omitted)
  DATA are LENGTH bytes for a write message. They can be shortened by a suffix:
    = (keep value constant until LENGTH)
    + (increase value by 1 until LENGTH)
    - (decrease value by 1 until LENGTH)
    p (use pseudo random generator until LENGTH with value as seed)
Example (bus 0, read 8 byte at offset 0x64 from EEPROM at 0x50):
  # i2ctransfer 0 w1@0x50 0x64 r8
Example (same EEPROM, at offset 0x42 write 0xff 0xfe ... 0xf0):
  # i2ctransfer 0 w17@0x50 0x42 0xff-
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install i2c-tools`，再执行 `i2c-tools --version` 2>/dev/null || `i2c-tools -V`
- [ ] **2.** **读官方帮助** —— `i2c-tools -h`，需要细节时 `man i2c-tools`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: /usr/bin/decode-dimms [-c] [-f [-b]] [-x|-X file [files..]]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/i2c-tools/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/i2c-tools/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/i2c-tools/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
