# flashrom

> Identify, read, write, erase, and verify BIOS/ROM/flash chips flashrom is a tool for identifying, reading, writing, verifying and erasing flash chips. It’s often used to flash BIOS/EFI/coreboot/firmware/optionROM images in-system using a s…

> **功能分类**：硬件攻击 ｜ **Kali 包**：`flashrom` ｜ **官方文档**：<https://www.kali.org/tools/flashrom/>

## 1. 安装

```bash
sudo apt update
sudo apt install flashrom
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6.0 |
| 架构 | any |
| 可执行命令 | `flashrom`、`libflashrom-dev`、`libflashrom1` |
| 依赖 | `libc6`、`libftdi1-2`、`libjaylink0`、`libpci3`、`libusb-1.0-0` |
| 安装体积 | 1.16 MB |
| 官网 | <http://www.flashrom.org> |
| 源码仓库 | <https://salsa.debian.org/debian/flashrom> |
| 包追踪 | <https://pkg.kali.org/pkg/flashrom> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
flashrom -h          # 查看用法
man flashrom         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `flashrom`

> 官方示例调用：`flashrom -h`

```text
root@kali:~# flashrom -h
flashrom v1.6.0 on Linux 7.1.5+kali-amd64 (x86_64)
flashrom is free software, get the source code at https://flashrom.org
Usage: flashrom [-h|-R|-L|
	-p <programmername>[:<parameters>] [-c <chipname>]
		(--flash-name|--flash-size|
		 [-E|-x|(-r|-w|-v) [<file>]]
		 [(-l <layoutfile>|--ifd| --fmap|--fmap-file <file>) [-i <region>[:<file>]]...]
		 [-n] [-N] [-f])]
	[-V[V[V]]] [-o <logfile>]
 -h | --help                        print this help text
 -R | --version                     print version (release)
 -r | --read [<file>]               read flash and save to <file>
 -w | --write [<file>|-]            write <file> or the content provided
                                    on the standard input to flash
 -v | --verify [<file>|-]           verify flash against <file>
                                    or the content provided on the standard input
 -E | --erase                       erase flash memory
 -V | --verbose                     more verbose output
 -c | --chip <chipname>             probe only for specified flash chip
 -f | --force                       force specific operations (see man page)
 -n | --noverify                    don't auto-verify
 -N | --noverify-all                verify included regions only (cf. -i)
 -x | --extract                     extract regions to files
 -l | --layout <layoutfile>         read ROM layout from <layoutfile>
      --wp-disable                  disable write protection
      --wp-enable                   enable write protection
      --wp-list                     list supported write protection ranges
      --wp-status                   show write protection status
      --wp-range=<start>,<len>      set write protection range (use --wp-range=0,0
                                    to unprotect the entire flash)
      --wp-region <region>          set write protection region
      --flash-name                  read out the detected flash name
      --flash-size                  read out the detected flash size
      --fmap                        read ROM layout from fmap embedded in ROM
      --fmap-file <fmapfile>        read ROM layout from fmap in <fmapfile>
      --ifd                         read layout from an Intel Firmware Descriptor
 -i | --include <region>[:<file>]   only read/write image <region> from layout
                                    (optionally with data from <file>)
      --image <region>[:<file>]     deprecated, please use --include
 -o | --output <logfile>            log output to <logfile>
      --flash-contents <ref-file>   assume flash contents to be <ref-file>
 -L | --list-supported              print supported devices
      --progress                    show progress percentage on the standard output
      --sacrifice-ratio <ratio>     Fraction (as a percentage, 0-50) of an erase block
                                    that may be erased even if unmodified. Larger values
				    may complete programming faster, but may also hurt
				    chip longevity by erasing cells unnecessarily.
				    Default is 0, tradeoff is the speed of programming
                                    operation VS the longevity of the chip. Default is
                                    longevity.
                                    DANGEROUS! It wears your chip faster!
PROGRAMMER SELECTION OPTIONS
 -p | --programmer <name>[:<param>] specify the programmer device. One of
    internal, dummy, nic3com, nicrealtek, gfxnvidia, raiden_debug_spi, drkaiser,
    satasii, asm106x, atavia, it8212, ft2232_spi, serprog, buspirate_spi,
    dediprog, developerbox, rayer_spi, pony_spi, nicintel, nicintel_spi,
    nicintel_eeprom, ogp_spi, satamv, linux_mtd, linux_spi, usbblaster_spi,
    pickit2_spi, ch341a_spi, ch347_spi, digilent_spi, jlink_spi, stlinkv3_spi,
    dirtyjtag_spi, spidriver.
You can specify one of -h, -R, -L, -E, -r, -w, -v or no operation.
If no operation is specified, flashrom will only probe for flash chips.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install flashrom`，再执行 `flashrom --version` 2>/dev/null || `flashrom -V`
- [ ] **2.** **读官方帮助** —— `flashrom -h`，需要细节时 `man flashrom`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: flashrom [-h|-R|-L|`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/flashrom/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/flashrom/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/flashrom/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
