# 按包速查：硬件攻击（hardware）

> 共 **5** 个包 · 数据来源 <https://www.kali.org/tools/all-tools/>

返回 [工具总览](../index.md) · [全量清单](all-tools.md) · [按功能分类](../index.md#功能分类导航)

---

### cutecom

Graphical serial terminal, like minicom Cutecom is a graphical serial terminal, like minicom. It is aimed mainly at hardware developers or other people who need a terminal to talk to their devices. It features lineoriented interface instead of character-oriented, xmodem, ymodem, zmodem support (requires the lrzsz package) and hexadecimal input and output among

| 项目 | 内容 |
|------|------|
| 归入分组 | 硬件攻击 |
| Kali 文档 | <https://www.kali.org/tools/cutecom/> |
| 版本 | 0.51.0 |
| 包 / 命令 | `cutecom` |
| 安装 | `sudo apt install cutecom` |
| 占用空间 | 739 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libqt5core5t64` |
| 官网 | <https://gitlab.com/cutecom/cutecom> |

### flashrom

Identify, read, write, erase, and verify BIOS/ROM/flash chips flashrom is a tool for identifying, reading, writing, verifying and erasing flash chips. It’s often used to flash BIOS/EFI/coreboot/firmware/optionROM images in-system using a supported mainboard, but it also supports flashing of network cards (NICs), SATA controller cards, and other external devices which can program flash chips.

| 项目 | 内容 |
|------|------|
| 归入分组 | 硬件攻击 |
| Kali 文档 | <https://www.kali.org/tools/flashrom/> |
| 版本 | 1.6.0 |
| 包 / 命令 | `flashrom`、`libflashrom-dev`、`libflashrom1` |
| 安装 | `sudo apt install flashrom` |
| 占用空间 | 1.16 MB |
| 依赖 | `libc6`、`libftdi1-2`、`libjaylink0`、`libpci3`、`libusb-1.0-0`、`flashrom` |
| 官网 | <http://www.flashrom.org> |
| 源码 | <https://salsa.debian.org/debian/flashrom> |

### minicom

Menu-driven serial communication program Minicom is a text-mode serial communications program modelled on the MS-DOS program Telix. It drives modems and serial consoles through a full-screen, menu-driven interface and emulates ANSI and VT102 terminals. A dialling directory with auto-redial, a scripting language for automating log-ins and other exchanges, capture-to-file logging, remappable key

| 项目 | 内容 |
|------|------|
| 归入分组 | 硬件攻击 |
| Kali 文档 | <https://www.kali.org/tools/minicom/> |
| 版本 | 2.11.1 |
| 包 / 命令 | `minicom`、`ascii-xfr`、`runscript`、`xminicom` |
| 安装 | `sudo apt install minicom` |
| 占用空间 | 1.10 MB |
| 依赖 | `libc6`、`libtinfo6`、`ascii-xfr` |
| 官网 | <https://salsa.debian.org/minicom-team/minicom> |

### openocd

Open on-chip JTAG/SWD debug solution for embedded target devices OpenOCD aims to provide debugging, in-system programming and boundary-scan testing for embedded target devices. The debugger uses an IEEE 1149-1 compliant JTAG TAP bus master to access on-chip debug functionality available on ARM based microcontrollers or system-on-chip solutions. For MIPS systems the EJTAG interface is supported.

| 项目 | 内容 |
|------|------|
| 归入分组 | 硬件攻击 |
| Kali 文档 | <https://www.kali.org/tools/openocd/> |
| 版本 | 0.12.0 |
| 包 / 命令 | `openocd` |
| 安装 | `sudo apt install openocd` |
| 占用空间 | 8.97 MB |
| 依赖 | `libc6`、`libcapstone5`、`libftdi1-2`、`libhidapi-hidraw0`、`libjaylink0`、`libjim0.84`、`libusb-1.0-0`、`openocd` |
| 官网 | <http://openocd.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/electronics-team/openocd> |

### qemu

Extra block backend modules for qemu-system and qemu-utils QEMU is a fast processor emulator: currently the package supports Alpha, ARM, CRIS, i386, LoongArch, M68k (ColdFire), MicroBlaze, MIPS, PowerPC, RISC-V, S390x, SH4, SPARC, x86-64, Xtensa and other emulations. By using dynamic translation it achieves reasonable speed while being easy to port on new host CPUs.

| 项目 | 内容 |
|------|------|
| 归入分组 | 硬件攻击 |
| Kali 文档 | <https://www.kali.org/tools/qemu/> |
| 版本 | 11.1.0 |
| 包 / 命令 | `qemu-block-extra`、`qemu-guest-agent`、`qemu-ga`、`qemu-system`、`qemu-system-arm`、`qemu-system-aarch64`、`qemu-system-arm64`、`qemu-system-armel`、`qemu-system-armhf`、`qemu-system-common`、`qemu-pr-helper`、`qemu-vmsr-helper`、`qemu-system-data`、`qemu-system-gui`、`qemu-system-mips`、`qemu-system-mips64`、`qemu-system-mips64el`、`qemu-system-mipsel`、`qemu-system-misc`、`qemu-system-alpha`、`qemu-system-avr`、`qemu-system-hexagon`、`qemu-system-hppa`、`qemu-system-loong64`、`qemu-system-loongarch64`、`qemu-system-m68k`、`qemu-system-microblaze`、`qemu-system-or1k`、`qemu-system-rx`、`qemu-system-sh4`、`qemu-system-sh4eb`、`qemu-system-tricore`、`qemu-system-xtensa`、`qemu-system-xtensaeb`、`qemu-system-modules-opengl`、`qemu-system-modules-spice`、`qemu-system-ppc`、`qemu-system-powerpc`、`qemu-system-ppc64`、`qemu-system-ppc64el`、`qemu-system-ppc64le`、`qemu-system-riscv`、`qemu-system-riscv32`、`qemu-system-riscv64`、`qemu-system-s390x`、`qemu-system-sparc`、`qemu-system-sparc64`、`qemu-system-x86`、`kvm`、`qemu-system-amd64`、`qemu-system-i386`、`qemu-system-x86_64`、`qemu-system-x86_64-microvm`、`qemu-system-xen`、`qemu-user`、`qemu-aarch64`、`qemu-aarch64_be`、`qemu-alpha`、`qemu-amd64`、`qemu-arm`、`qemu-arm64`、`qemu-armeb`、`qemu-armel`、`qemu-armhf`、`qemu-hexagon`、`qemu-hppa`、`qemu-i386`、`qemu-loong64`、`qemu-loongarch64`、`qemu-m68k`、`qemu-microblaze`、`qemu-microblazeel`、`qemu-mips`、`qemu-mips64`、`qemu-mips64el`、`qemu-mipsel`、`qemu-mipsn32`、`qemu-mipsn32el`、`qemu-or1k`、`qemu-powerpc`、`qemu-ppc`、`qemu-ppc64`、`qemu-ppc64el`、`qemu-ppc64le`、`qemu-riscv32`、`qemu-riscv64`、`qemu-s390x`、`qemu-sh4`、`qemu-sh4eb`、`qemu-sparc`、`qemu-sparc32plus`、`qemu-sparc64`、`qemu-x86_64`、`qemu-xtensa`、`qemu-xtensaeb`、`qemu-user-binfmt`、`qemu-utils`、`qemu-img`、`qemu-io`、`qemu-nbd`、`qemu-storage-daemon` |
| 安装 | `sudo apt install qemu-block-extra` |
| 占用空间 | 323 KB |
| 依赖 | `libblkio1`、`libbz2-1.0`、`libc6`、`libcurl4-gnutls`、`libiscsi7`、`libnfs14`、`librados2`、`librbd1`、`libssh-4` |
| 官网 | <http://www.qemu.org/> |
| 源码 | <https://salsa.debian.org/qemu-team/qemu> |
