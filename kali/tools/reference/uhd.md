# uhd

> Universal hardware driver for Ettus Research products - headers Host library for the Universal Hardware Driver for Ettus Research products. The supported devices provide analog radio receiver and transmitter hardware along with digital int…

> **功能分类**：无线攻击 ｜ **Kali 包**：`uhd` ｜ **官方文档**：<https://www.kali.org/tools/uhd/>

## 1. 安装

```bash
sudo apt update
sudo apt install libuhd-dev
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.9.0.1 |
| 架构 | any |
| 可执行命令 | `libuhd-dev`、`libuhd4.9.0`、`libuhd4.9.0-dpdk`、`libuhd4.9.0-dpdk-tests`、`python3-uhd`、`uhd-doc`、`uhd-host`、`rfnoc_image_builder`、`rfnoc_modtool`、`uhd_adc_self_cal`、`uhd_cal_rx_iq_balance`、`uhd_cal_tx_dc_offset`、`uhd_cal_tx_iq_balance`、`uhd_config_info`、`uhd_find_devices`、`uhd_image_loader`、`uhd_images_downloader`、`uhd_usrp_probe`、`usrp2_card_burner`、`usrpctl`、`uhd-rfnoc-dev` |
| 依赖 | `libboost-chrono-dev`、`libboost-date-time-dev`、`libboost-dev`、`libboost-exception-dev`、`libboost-filesystem-dev`、`libboost-program-options-dev`、`libboost-python-dev`、`libboost-regex-dev`、`libboost-serialization-dev`、`libboost-test-dev`、`libboost-thread-dev`、`libuhd4.9.0` 等 |
| 安装体积 | 1.20 MB |
| 官网 | <https://www.ettus.com/sdr-software/uhd-usrp-hardware-driver/> |
| 源码仓库 | <https://salsa.debian.org/bottoms/pkg-uhd> |
| 包追踪 | <https://pkg.kali.org/pkg/uhd> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libuhd-dev -h          # 查看用法
man libuhd-dev         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 21 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rfnoc_image_builder`

> 官方示例调用：`rfnoc_image_builder -h`

```text
root@kali:~# rfnoc_image_builder -h
usage: rfnoc_image_builder [-h] (-y YAML_CONFIG | -r GRC_CONFIG) [-C BASE_DIR]
                           [-F FPGA_DIR] [-B BUILD_DIR] [-O BUILD_OUTPUT_DIR]
                           [-E BUILD_IP_DIR] [-o IMAGE_CORE_OUTPUT]
                           [-x ROUTER_HEX_OUTPUT] [-I INCLUDE_DIR]
                           [-b GRC_BLOCKS] [-l LOG_LEVEL] [-R] [-G] [-W]
                           [-S SECURE_CORE] [-K SECURE_KEY] [-d DEVICE]
                           [-n IMAGE_CORE_NAME]
                           [-t {E310_SG1,E310_SG1_IDLE,E310_SG3,E310_SG3_IDLE,E320_1G,E320_XG,E320_AA,N310_WX,N310_HG,N310_XG,N310_HA,N310_XA,N310_AA,N300_WX,N300_HG,N300_XG,N300_HA,N300_XA,N300_AA,N320_WX,N320_HG,N320_XG,N320_XQ,N320_AQ,N320_AA,X310_1G,X310_HG,X310_XG,X310_HA,X310_XA,X300_1G,X300_HG,X300_XG,X300_HA,X300_XA,X410,X440}]
                           [-g] [-Y] [--CHECK] [-s] [-P] [-j JOBS] [-c]
                           [-p VIVADO_PATH] [-H] [-D]
                           [--color {never,auto,always}]
Build UHD image using RFNoC blocks
options:
  -h, --help            show this help message and exit
  -y, --yaml-config YAML_CONFIG
                        Path to yml configuration file
  -r, --grc-config GRC_CONFIG
                        Path to grc file to generate config from
  -C, --base-dir BASE_DIR
                        Path to the base directory. Defaults to the current
                        directory.
  -F, --fpga-dir FPGA_DIR
                        Path to directory for the FPGA source tree. Defaults
                        to the FPGA source tree of the current repo.
  -B, --build-dir BUILD_DIR
                        Path to directory where the image core and and build
                        artifacts will be generated. Defaults to
                        "build-<image-core-name>" in the base directory.
  -O, --build-output-dir BUILD_OUTPUT_DIR
                        Path to directory for final FPGA build outputs.
                        Defaults to "build" in the base directory.
  -E, --build-ip-dir BUILD_IP_DIR
                        Path to directory for IP build artifacts. Defaults to
                        "build-ip" in the base directory.
  -o, --image-core-output IMAGE_CORE_OUTPUT
                        DEPRECATED! This has been replaced by --build-dir.
  -x, --router-hex-output ROUTER_HEX_OUTPUT
                        DEPRECATED! This option will be ignored.
  -I, --include-dir INCLUDE_DIR
                        Path to directory of the RFNoC Out-of-Tree module
  -b, --grc-blocks GRC_BLOCKS
                        Path to directory of GRC block descriptions (needed
                        for --grc-config only)
  -l, --log-level LOG_LEVEL
                        Adjust log level
  -R, --reuse           Reuse existing files (do not regenerate image core).
  -G, --generate-only   Just generate files without building the FPGA
  -W, --ignore-warnings
                        Run build even when there are warnings in the build
                        process
  -S, --secure-core SECURE_CORE
                        Build a secure image core instead of a bitfile. This
                        argument provides the name of the generated YAML.
  -K, --secure-key SECURE_KEY
                        Path to encryption key file to use for secure core.
  -d, --device DEVICE   Device to be programmed [x300, x310, e310, e320, n300,
                        n310, n320, x410, x440]. Needs to be specified either
                        here, or in the configuration file.
  -n, --image-core-name, --image_core_name IMAGE_CORE_NAME
                        Name to use for the RFNoC image core. Defaults to name
                        of the image core YML file, without the extension.
  -t, --target {E310_SG1,E310_SG1_IDLE,E310_SG3,E310_SG3_IDLE,E320_1G,E320_XG,E320_AA,N310_WX,N310_HG,N310_XG,N310_HA,N310_XA,N310_AA,N300_WX,N300_HG,N300_XG,N300_HA,N300_XA,N300_AA,N320_WX,N320_HG,N320_XG,N320_XQ,N320_AQ,N320_AA,X310_1G,X310_HG,X310_XG,X310_HA,X310_XA,X300_1G,X300_HG,X300_XG,X300_HA,X300_XA,X410,X440}
                        Build target (e.g. X310_HG, N320_XG, ...). Needs to be
                        specified either here, on the configuration file.
  -g, --GUI             Open Vivado GUI during the FPGA building process
  -Y, --SYNTH           Stop the FPGA build process after Synthesis
  --CHECK               Run elaboration only to check HDL syntax
  -s, --save-project    Save Vivado project to disk
  -P, --ip-only         Build only the required IPs
  -j, --jobs JOBS       Number of parallel jobs to use with make
  -c, --clean-all       Cleans the IP before a new build
  -p, --vivado-path VIVADO_PATH
                        Path to the base install for Xilinx Vivado if not in
                        default location (e.g., /tools/Xilinx/Vivado).
  -H, --no-hash         Do not include source YAML hash in the generated
                        source code.
  -D, --no-date         Do not include date or time in the generated source
                        code.
  --color {never,auto,always}
                        Enable colorful output. When set to 'auto' will only
                        show color output in TTY environments (e.g.,
                        interactive shells)
```

### `rfnoc_modtool`

> 官方示例调用：`rfnoc_modtool -h`

```text
root@kali:~# rfnoc_modtool -h
usage: rfnoc_modtool [-h] [-C DIRECTORY] [-l LOG_LEVEL]
                     {add-grc,create,add-gr-block,add-gr-oot,make-yaml,add} ...
RFNoC Modtool: The tool to create and manipulate RFNoC OOT modules.
positional arguments:
  {add-grc,create,add-gr-block,add-gr-oot,make-yaml,add}
    add-grc             Add GNU Radio GRC bindings for an existing block in
                        this RFNoC OOT module. This command may be called
                        within an existing RFNoC OOT module directory, if
                        within it there exists a GNU Radio OOT module. It will
                        add GRC bindings for a given block. Note: Must be
                        called from within a valid RFNoC OOT module directory.
                        Use -C to specify the module directory if necessary.
    create              Create a new RFNoC OOT module
    add-gr-block        Add a GNU Radio block for an existing block in this
                        RFNoC OOT module. This command may be called within an
                        existing RFNoC OOT module directory, if within it
                        there exists a GNU Radio OOT module. It will add a C++
                        block implementation for an RFNoC block. Note: Must be
                        called from within a valid RFNoC OOT module directory.
                        Use -C to specify the module directory if necessary.
                        Note: This command will call into `gr_modtool` under
                        the hood, so make sure it is installed and available
                        in your PATH.
    add-gr-oot          Add GNU Radio OOT Module. Note: Must be called from
                        within a valid RFNoC OOT module directory. Use -C to
                        specify the module directory if necessary. Requires an
                        installation of GNU Radio. This command will use
                        gr_modtool to generate a new OOT module.
    make-yaml           YAML Creation Wizard -- Generate an RFNoC block YAML
                        descriptor file based on user input. Note: Must be
                        called from within a valid RFNoC OOT module directory.
                        Use -C to specify the module directory if necessary.
    add                 Add a new block to an RFNoC OOT module based on a
                        descriptor file. Note: Must be called from within a
                        valid RFNoC OOT module directory. Use -C to specify
                        the module directory if necessary.
options:
  -h, --help            show this help message and exit
  -C, --directory DIRECTORY
                        Change to this directory before running the command
  -l, --log-level LOG_LEVEL
                        Set the log level (default: INFO)
```

### `uhd_adc_self_cal`

> 官方示例调用：`uhd_adc_self_cal --help`

```text
root@kali:~# uhd_adc_self_cal --help
UHD ADC self calibration Allowed options:
  --help                help message
  --version             print the version string and exit
  --args arg            device address args
```

### `uhd_cal_rx_iq_balance`

> 官方示例调用：`uhd_cal_rx_iq_balance --help`

```text
root@kali:~# uhd_cal_rx_iq_balance --help
USRP Generate RX IQ Balance Calibration Table Allowed options:
  --help                                help message
  --verbose                             enable some verbose
  --args arg                            Device address args [default = ""]
  --subdev arg                          Subdevice specification (default: first
                                        subdevice, often 'A')
  --tx_wave_ampl arg (=0.69999999999999996)
                                        Transmit wave amplitude
  --tx_offset arg (=934400)             TX LO offset from the RX LO in Hz
  --tx_gain arg                         Tx gain in dB (do not specify for
                                        default)
  --freq_start arg                      Frequency start in Hz (do not specify
                                        for default)
  --freq_stop arg                       Frequency stop in Hz (do not specify
                                        for default)
  --freq_step arg (=7300000)            Step size for LO sweep in Hz
  --nsamps arg                          Samples per data capture
  --precision arg (=0.0001)             Correction precision (default=0.0001)
This application measures leakage between RX and TX on a transceiver daughterboard to self-calibrate.
Note: Not all daughterboards support this feature. Refer to the UHD manual for details.
```

### `uhd_cal_tx_dc_offset`

> 官方示例调用：`uhd_cal_tx_dc_offset --help`

```text
root@kali:~# uhd_cal_tx_dc_offset --help
USRP Generate TX DC Offset Calibration Table Allowed options:
  --help                                help message
  --verbose                             enable some verbose
  --args arg                            device address args [default = ""]
  --subdev arg                          Subdevice specification (default: first
                                        subdevice, often 'A')
  --tx_wave_freq arg (=507123)          Transmit wave frequency in Hz
  --tx_wave_ampl arg (=0.69999999999999996)
                                        Transmit wave amplitude
  --tx_gain arg                         Tx gain in dB (do not specify for
                                        default)
  --rx_offset arg (=934400)             RX LO offset from the TX LO in Hz
  --freq_start arg                      Frequency start in Hz (do not specify
                                        for default)
  --freq_stop arg                       Frequency stop in Hz (do not specify
                                        for default)
  --freq_step arg (=7300000)            Step size for LO sweep in Hz
  --nsamps arg                          Samples per data capture
  --precision arg (=0.0001)             Correction precision (default=0.0001)
This application measures leakage between RX and TX on a transceiver daughterboard to self-calibrate.
Note: Not all daughterboards support this feature. Refer to the UHD manual for details.
```

### `uhd_cal_tx_iq_balance`

> 官方示例调用：`uhd_cal_tx_iq_balance --help`

```text
root@kali:~# uhd_cal_tx_iq_balance --help
USRP Generate TX IQ Balance Calibration Table Allowed options:
  --help                                help message
  --verbose                             enable some verbose
  --args arg                            device address args [default = ""]
  --subdev arg                          Subdevice specification (default: first
                                        subdevice, often 'A')
  --tx_wave_freq arg (=507123)          Transmit wave frequency in Hz
  --tx_wave_ampl arg (=0.69999999999999996)
                                        Transmit wave amplitude
  --tx_gain arg                         Tx gain in dB (do not specify for
                                        default)
  --rx_offset arg (=934400)             RX LO offset from the TX LO in Hz
  --freq_start arg                      Frequency start in Hz (do not specify
                                        for default)
  --freq_stop arg                       Frequency stop in Hz (do not specify
                                        for default)
  --freq_step arg (=7300000)            Step size for LO sweep in Hz
  --nsamps arg                          Samples per data capture
  --precision arg (=0.0001)             Correction precision (default=0.0001)
This application measures leakage between RX and TX on a transceiver daughterboard to self-calibrate.
Note: Not all daughterboards support this feature. Refer to the UHD manual for details.
```

### `uhd_config_info`

> 官方示例调用：`uhd_config_info --help`

```text
root@kali:~# uhd_config_info --help
UHD Config Info - Allowed Options:
  --build-date          Print build date
  --c-compiler          Print C compiler
  --cxx-compiler        Print C++ compiler
  --c-flags             Print C compiler flags
  --cxx-flags           Print C++ compiler flags
  --enabled-components  Print built-time enabled components
  --install-prefix      Print install prefix
  --boost-version       Print Boost version
  --dpdk-version        Print DPDK version
  --libusb-version      Print libusb version
  --pkg-path            Print pkg path
  --pkg-data-path       Print package data path
  --lib-path            Print library path
  --images-dir          Print images dir
  --abi-version         Print ABI version string
  --print-all           Print everything
  --version             Print this UHD build's version
  --help                Print help message
```

### `uhd_find_devices`

> 官方示例调用：`uhd_find_devices --help`

```text
root@kali:~# uhd_find_devices --help
UHD Find Devices Allowed options:
  --help                help message
  --args arg            device address args
```

### `uhd_image_loader`

> 官方示例调用：`uhd_image_loader --help`

```text
root@kali:~# uhd_image_loader --help
UHD Image Loader
Load firmware and/or FPGA images onto an Ettus Research device.
Allowed options:
  --help                help message
  --args arg            Device args, optional loader args
  --fw-path arg         Firmware path (uses default if none specified)
  --fpga-path arg       FPGA path (uses default if none specified)
  --out-path arg        Output path/filename of the downloaded FPGA .bit file
  --no-fw               Don't burn firmware
  --no-fpga             Don't Burn FPGA
  --download            Download an image to a bit/bin file
```

### `uhd_images_downloader`

> 官方示例调用：`uhd_images_downloader -h`

```text
root@kali:~# uhd_images_downloader -h
usage: uhd_images_downloader [-h] [-t TYPES] [-i INSTALL_LOCATION]
                             [-m MANIFEST_LOCATION] [-I INVENTORY_LOCATION]
                             [-l] [--url-only] [--buffer-size BUFFER_SIZE]
                             [--download-limit DOWNLOAD_LIMIT]
                             [--http-proxy HTTP_PROXY] [-b BASE_URL] [-k] [-T]
                             [-y] [-n] [--refetch] [-V] [-q] [-v]
Download image files required for USRPs. Usage: The `uhd_images_downloader`
should work, "out of the box", with no command line arguments. Assuming your
computer has an internet connection to [files.ettus.com], simply run the
utility every time you update UHD, and the installed images for your devices
should always be up to date. Images will be downloaded on a per-target basis.
That is, there are image packages for a desired device and configuration.
Users can specify which image packages they would plan to use. To see a list
of available targets, run `uhd_images_downloader --list-targets`. The left
column of the printout will be a list of available image archives. From there,
you can construct a regular expression which matches to the targets you wish
to download. For example, in order to download all image packages related to
the X300 product line, users may run `uhd_images_downloader --types x3.*`. The
`uhd_images_downloader` uses a manifest to look-up the URLs of image packages
to download. Downloaded images are recorded in an inventory file that lives in
the images install location. This allows the downloader to skip images that
were previously downloaded, and haven't changed since. Manifests are built
into the downloader, but can also be accessed at uhd/images/manifest.txt.
Inventory files are JSON files called `inventory.json`, by default. It is
possible to specify the inventory file in command line arguments, but we don't
recommend using this functionality unless you're really sure you need it.
options:
  -h, --help            show this help message and exit
  -t, --types TYPES     RegEx to select image sets from the manifest file.
                        (default: None)
  -i, --install-location INSTALL_LOCATION
                        Set custom install location for images (default: None)
  -m, --manifest-location MANIFEST_LOCATION
                        Set custom location for the manifest file (default:
                        None)
  -I, --inventory-location INVENTORY_LOCATION
                        Set custom location for the inventory file (default:
                        None)
  -l, --list-targets    Print targets in the manifest file to stdout, and
                        exit. To get relative paths only, specify an empty
                        base URL (-b ''). (default: False)
  --url-only            With -l, only print the URLs, nothing else. (default:
                        False)
  --buffer-size BUFFER_SIZE
                        Set download buffer size (default: 8192)
  --download-limit DOWNLOAD_LIMIT
                        Set threshold for download limits. Any download larger
                        than this will require approval, either interactively,
                        or by providing --yes. (default: 1073741824)
  --http-proxy HTTP_PROXY
                        Specify HTTP(S) proxy in the format
                        http[s]://user:
[email protected]
:port If this this option
                        is not given, the environment variables
                        HTTP_PROXY/HTTPS_PROXY can also be used to specify a
                        proxy. (default: None)
  -b, --base-url BASE_URL
                        Set base URL for images download location. Defaults to
                        $UHD_IMAGES_URL if set, or
                        https://files.ettus.com/binaries/cache/ otherwise.
                        (default: None)
  -k, --keep            Keep the downloaded images archives in the image
                        directory (default: False)
  -T, --test            Verify the downloaded archives before extracting them
                        (default: False)
  -y, --yes             Answer all questions with 'yes' (for scripting
                        purposes). (default: False)
  -n, --dry-run         Print selected target without actually downloading
                        them. (default: False)
  --refetch             Ignore the inventory file and download all images.
                        (default: False)
  -V, --version         show program's version number and exit
  -q, --quiet           Decrease verbosity level (default: 0)
  -v, --verbose         Increase verbosity level (default: 0)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install libuhd-dev`，再执行 `libuhd-dev --version` 2>/dev/null || `libuhd-dev -V`
- [ ] **2.** **读官方帮助** —— `libuhd-dev -h`，需要细节时 `man libuhd-dev`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `libuhd-dev -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/uhd/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/uhd/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/uhd/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
