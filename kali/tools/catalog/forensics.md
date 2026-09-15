# 按包速查：数字取证（forensics）

> 共 **89** 个包 · 数据来源 <https://www.kali.org/tools/all-tools/>

返回 [工具总览](../index.md) · [全量清单](all-tools.md) · [按功能分类](../index.md#功能分类导航)

---

### 7zip

7-Zip file archiver with a high compression ratio 7-Zip is a file archiver with a high compression ratio. The main features of 7-Zip are: High compression ratio in 7z format with LZMA and LZMA2 compression Supported formats: Packing / unpacking: 7z, XZ, BZIP2, GZIP, TAR, ZIP and WIM

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应、逆向工程 |
| Kali 文档 | <https://www.kali.org/tools/7zip/> |
| 版本 | 26.02 |
| 包 / 命令 | `7zip`、`7z`、`7za`、`7zr`、`p7zip`、`7zip-standalone`、`7zz` |
| 安装 | `sudo apt install 7zip` |
| 占用空间 | 6.99 MB |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6`、`7z` |
| 官网 | <https://www.7-zip.org/> |
| 源码 | <https://salsa.debian.org/debian/7zip> |

### afflib

Advanced Forensics Format Library (utilities) The Advanced Forensic Format (AFF) is on-disk format for storing computer forensic information. Critical features of AFF include: AFF allows you to store both computer forensic data and associated metadata in one or more files. AFF allows files to be digital signed, to provide for

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/afflib/> |
| 版本 | 3.7.22 |
| 包 / 命令 | `afflib-tools`、`affcat`、`affcompare`、`affconvert`、`affcopy`、`affcrypto`、`affdiskprint`、`affinfo`、`affix`、`affrecover`、`affsegment`、`affsign`、`affstats`、`affuse`、`affverify`、`affxml`、`libafflib-dev`、`libafflib0t64` |
| 安装 | `sudo apt install afflib-tools` |
| 占用空间 | 624 KB |
| 依赖 | `libafflib0t64`、`libc6`、`libexpat1`、`libfuse3-4`、`libgcc-s1`、`libssl3t64`、`libstdc++6`、`affcat` |
| 官网 | <https://github.com/sshock/AFFLIBv3> |
| 源码 | <https://salsa.debian.org/pkg-security-team/afflib> |

### apktool

Tool for reverse engineering Android apk files A tool for reverse engineering 3rd party, closed, binary Android apps. It can decode resources to nearly original form and rebuild them after making some modifications; it makes possible to debug smali code step by step. Also it makes working with an app easier because of project-like file structure and automation of some repetitive tasks like building apk.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应、逆向工程 |
| Kali 文档 | <https://www.kali.org/tools/apktool/> |
| 版本 | 2.7.0 |
| 包 / 命令 | `apktool` |
| 安装 | `sudo apt install apktool` |
| 占用空间 | 269 KB |
| 依赖 | `aapt`、`android-framework-res` |
| 官网 | <https://ibotpeaches.github.io/Apktool/> |
| 源码 | <https://salsa.debian.org/android-tools-team/apktool> |

### autopsy

Graphical interface to SleuthKit The Autopsy Forensic Browser is a graphical interface to the command line digital forensic analysis tools in The Sleuth Kit. Together, The Sleuth Kit and Autopsy provide many of the same features as commercial digital forensics tools for the analysis of Windows and UNIX file systems (NTFS, FAT, FFS, EXT2FS, and EXT3FS).

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/autopsy/> |
| 版本 | 2.24 |
| 包 / 命令 | `autopsy` |
| 安装 | `sudo apt install autopsy` |
| 占用空间 | 1.00 MB |
| 依赖 | `binutils`、`perl`、`sleuthkit`、`autopsy` |
| 官网 | <https://www.sleuthkit.org/autopsy/> |
| 源码 | <https://salsa.debian.org/debian/autopsy> |

### binwalk

Tool library for analyzing binary blobs and executable code Binwalk is a tool for searching a given binary image for embedded files and executable code. Specifically, it is designed for identifying files and code embedded inside of firmware images. Binwalk uses the libmagic library, so it is compatible with magic signatures created for the Unix file utility.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、硬件攻击、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/binwalk/> |
| 版本 | 2.4.3 |
| 包 / 命令 | `binwalk`、`python3-binwalk` |
| 安装 | `sudo apt install binwalk` |
| 占用空间 | 17 KB |
| 依赖 | `python3`、`python3-binwalk`、`binwalk` |
| 官网 | <https://github.com/ReFirmLabs/binwalk> |
| 源码 | <https://salsa.debian.org/pkg-security-team/binwalk> |

### binwalk3

Tool library for analyzing binary blobs and executable code Binwalk is a tool for identifying, and optionally extracting, files and data that have been embedded inside of other files. While its primary focus is firmware analysis, it supports a wide variety of file and data types. Through entropy analysis, it can even help to identify unknown compression or

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、硬件攻击、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/binwalk3/> |
| 版本 | 3.1.0 |
| 包 / 命令 | `binwalk3`、`librust-binwalk-dev` |
| 安装 | `sudo apt install binwalk3` |
| 占用空间 | 3.88 MB |
| 依赖 | `libc6`、`libfontconfig1`、`libfreetype6`、`libgcc-s1`、`liblzma5`、`sasquatch`、`binwalk3` |
| 官网 | <https://github.com/ReFirmLabs/binwalk> |
| 源码 | <https://gitlab.com/kalilinux/packages/binwalk3> |

### bulk-extractor

Extracts information without parsing filesystem bulk_extractor is a C++ program that scans a disk image, a file, or a directory of files and extracts useful information without parsing the file system or file system structures. The results are stored in feature files that can be easily inspected, parsed, or processed with automated tools. bulk_extractor also creates

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/bulk-extractor/> |
| 版本 | 2.1.1 |
| 包 / 命令 | `bulk-extractor`、`bulk_extractor` |
| 安装 | `sudo apt install bulk-extractor` |
| 占用空间 | 15.82 MB |
| 依赖 | `libc6`、`libewf2`、`libexpat1`、`libgcc-s1`、`libgcrypt20`、`libre2-11-absl20260526`、`libstdc++6`、`zlib1g`、`bulk_extractor` |
| 官网 | <https://github.com/simsong/bulk_extractor> |
| 源码 | <https://gitlab.com/kalilinux/packages/bulk-extractor> |

### bytecode-viewer

Java 8+ Jar & Android APK Reverse Engineering Suite This package contains Bytecode Viewer (BCV). It is an Advanced Lightweight Java Bytecode Viewer, GUI Java Decompiler, GUI Bytecode Editor, GUI Smali, GUI Baksmali, GUI APK Editor, GUI Dex Editor, GUI APK Decompiler, GUI DEX Decompiler, GUI Procyon Java Decompiler, GUI Krakatau, GUI CFR Java Decompiler, GUI FernFlower Java Decompiler, GUI DEX2Jar, GUI Jar2DEX, GUI

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应、逆向工程 |
| Kali 文档 | <https://www.kali.org/tools/bytecode-viewer/> |
| 版本 | 2.13.2 |
| 包 / 命令 | `bytecode-viewer` |
| 安装 | `sudo apt install bytecode-viewer` |
| 占用空间 | 66.93 MB |
| 依赖 | `default-jre`、`java-wrappers`、`bytecode-viewer` |
| 官网 | <https://github.com/Konloch/bytecode-viewer> |
| 源码 | <https://gitlab.com/kalilinux/packages/bytecode-viewer> |

### cabextract

Microsoft Cabinet file unpacker Cabextract is a program which unpacks cabinet (.cab) files, which are a form of archive Microsoft uses to distribute their software and things like Windows Font Packs.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/cabextract/> |
| 版本 | 1.11 |
| 包 / 命令 | `cabextract` |
| 安装 | `sudo apt install cabextract` |
| 占用空间 | 83 KB |
| 依赖 | `libc6`、`libmspack0t64`、`cabextract` |

### capstone

Lightweight multi-architecture disassembly framework - command line tool Capstone is a lightweight multi-platform, multi-architecture disassembly framework. This package contains cstool, a command-line tool to disassemble hexadecimal strings.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、硬件攻击、事件响应、逆向工程 |
| Kali 文档 | <https://www.kali.org/tools/capstone/> |
| 版本 | 5.0.9 |
| 包 / 命令 | `capstone-tool`、`cstool`、`libcapstone-dev`、`libcapstone5`、`python3-capstone` |
| 安装 | `sudo apt install capstone-tool` |
| 占用空间 | 8.97 MB |
| 依赖 | `libc6`、`cstool` |
| 官网 | <https://www.capstone-engine.org/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/capstone> |

### chkrootkit

Rootkit detector The chkrootkit security scanner searches for signs that the system is infected with a ‘rootkit’. Rootkits are a form of malware that seek to exploit security flaws to grant unauthorised access to a computer or its services, generally for malicious purposes. chkrootkit can identify signs of over 70 different rootkits (see the

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/chkrootkit/> |
| 版本 | 0.59 |
| 包 / 命令 | `chkrootkit`、`chklastlog`、`chkrootkit-daily`、`chkwtmp` |
| 安装 | `sudo apt install chkrootkit` |
| 占用空间 | 988 KB |
| 依赖 | `binutils` |
| 官网 | <https://www.chkrootkit.org/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/chkrootkit> |

### dc3dd

Patched version of GNU dd with forensic features dc3dd is a patched version of GNU dd with added features for computer forensics: on the fly hashing (md5, sha-1, sha-256, and sha-512); possibility to write errors to a file; group errors in the error log;

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/dc3dd/> |
| 版本 | 7.3.1 |
| 包 / 命令 | `dc3dd` |
| 安装 | `sudo apt install dc3dd` |
| 占用空间 | 478 KB |
| 依赖 | `libc6`、`dc3dd` |
| 官网 | <https://sourceforge.net/projects/dc3dd/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/dc3dd> |

### dcfldd

Enhanced version of dd for forensics and security dcfldd was initially developed at Department of Defense Computer Forensics Lab (DCFL). This tool is based on the dd program with the following additional features: Hashing on-the-fly: dcfldd can hash the input data as it is being transferred, helping to ensure data integrity.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/dcfldd/> |
| 版本 | 1.9.3 |
| 包 / 命令 | `dcfldd` |
| 安装 | `sudo apt install dcfldd` |
| 占用空间 | 113 KB |
| 依赖 | `libc6`、`dcfldd` |
| 官网 | <https://github.com/resurrecting-open-source-projects/dcfldd> |
| 源码 | <https://salsa.debian.org/debian/dcfldd> |

### ddrescue

Data recovery and protection tool When your disk has crashed and you try to copy it over to another one, standard Unix tools like cp, cat, and dd will abort on every I/O error, dd_rescue does not. It optimizes copying by using large blocks as long as no errors occur and falls back to smaller blocks. It supports reverse direction copying

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、数据恢复、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/ddrescue/> |
| 版本 | 1.99.13 |
| 包 / 命令 | `ddrescue`、`dd_rescue` |
| 安装 | `sudo apt install ddrescue` |
| 占用空间 | 411 KB |
| 依赖 | `libc6`、`liblzo2-2`、`libssl3t64`、`dd_rescue` |
| 官网 | <http://www.garloff.de/kurt/linux/ddrescue/> |
| 源码 | <https://gitlab.com/kalilinux/packages/ddrescue> |

### dfdatetime

Digital Forensics date and time library for Python 3 dfDateTime, or Digital Forensics date and time, provides date and time objects to preserve accuracy and precision.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/dfdatetime/> |
| 版本 | 20260730 |
| 包 / 命令 | `python3-dfdatetime` |
| 安装 | `sudo apt install python3-dfdatetime` |
| 占用空间 | 269 KB |
| 依赖 | `python3` |
| 官网 | <https://github.com/log2timeline/dfdatetime> |
| 源码 | <https://salsa.debian.org/pkg-security-team/dfdatetime> |

### dfvfs

Digital Forensics Virtual File System The Digital Forensics Virtual File System, provides read-only access to file-system objects from various storage media types and file formats. The goal of dfVFS is to provide a generic interface for accessing file-system objects, for which it uses several back-ends that provide the actual implementation of the various storage media

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/dfvfs/> |
| 版本 | 20251019 |
| 包 / 命令 | `python3-dfvfs` |
| 安装 | `sudo apt install python3-dfvfs` |
| 占用空间 | 1.15 MB |
| 依赖 | `python3`、`python3-cffi-backend`、`python3-cryptography`、`python3-dfdatetime`、`python3-dtfabric`、`python3-fsapfs`、`python3-idna`、`python3-libbde`、`python3-libewf`、`python3-libfsext`、`python3-libfshfs`、`python3-libfsntfs` 等 |
| 官网 | <https://github.com/log2timeline/dfvfs> |
| 源码 | <https://salsa.debian.org/pkg-security-team/dfvfs> |

### dfwinreg

Digital Forensics Windows Registry library for Python 3 dfWinReg, or Digital Forensics Windows Registry, provides read-only access to Windows Registry objects. The goal of dfWinReg is to provide a generic interface for accessing Windows Registry objects that resembles the Registry key hierarchy as seen on a live Windows system.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/dfwinreg/> |
| 版本 | 20260411 |
| 包 / 命令 | `python3-dfwinreg` |
| 安装 | `sudo apt install python3-dfwinreg` |
| 占用空间 | 1.05 MB |
| 依赖 | `libjs-jquery`、`libjs-sphinxdoc`、`python3`、`python3-dfdatetime`、`python3-dtfabric`、`python3-libregf`、`python3-yaml`、`sphinx-rtd-theme-common` |
| 官网 | <https://github.com/log2timeline/dfwinreg> |
| 源码 | <https://salsa.debian.org/pkg-security-team/dfwinreg> |

### distorm3

Powerful disassembler library for x86/AMD64 binary streams (runtime) diStorm3 is a binary stream disassembler library project. With diStorm3, no more parsing strings is needed. diStorm3 is really a decomposer, which means it takes an instruction and returns a binary structure which describes it rather than static text. This is great for advanced binary code analysis.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/distorm3/> |
| 版本 | 3.5.2b |
| 包 / 命令 | `libdistorm3-3`、`libdistorm3-dev`、`python3-distorm3` |
| 安装 | `sudo apt install libdistorm3-3` |
| 占用空间 | 89 KB |
| 依赖 | `libc6`、`libdistorm3-dev` |
| 官网 | <https://github.com/gdabah/distorm> |
| 源码 | <https://salsa.debian.org/debian/distorm3> |

### dumpzilla

Mozilla browser forensic tool Dumpzilla application is developed in Python 3.x and has as purpose extract all forensic interesting information of Firefox, Iceweasel and Seamonkey browsers to be analyzed. Due to its Python 3.x development, might not work properly in old Python versions, mainly with certain characters. Works under Unix and Windows 32/64 bits systems. Works in command line interface, so information

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/dumpzilla/> |
| 版本 | 20210311 |
| 包 / 命令 | `dumpzilla` |
| 安装 | `sudo apt install dumpzilla` |
| 占用空间 | 136 KB |
| 依赖 | `libnss3`、`python3`、`python3-lz4`、`python3-magic-ahupp`、`dumpzilla` |
| 官网 | <http://www.dumpzilla.org/> |
| 源码 | <https://gitlab.com/kalilinux/packages/dumpzilla> |

### edb-debugger

Cross platform x86/x86-64 debugger edb is a graphical cross platform x86/x86-64 debugger. It was inspired by Ollydbg, but aims to function on x86 and x86-64 as well as multiple OS’s. Linux is the only officially supported platform at the moment, but FreeBSD, OpenBSD, OSX and Windows ports are underway with varying

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应、逆向工程 |
| Kali 文档 | <https://www.kali.org/tools/edb-debugger/> |
| 版本 | 1.3.0 |
| 包 / 命令 | `edb-debugger`、`edb`、`edb-debugger-plugins` |
| 安装 | `sudo apt install edb-debugger` |
| 占用空间 | 1.68 MB |
| 依赖 | `edb-debugger-plugins`、`libc6`、`libcapstone5`、`libcgraph8`、`libdouble-conversion3`、`libgcc-s1`、`libgvc7`、`libqt5core5t64` |
| 官网 | <https://github.com/eteran/edb-debugger> |
| 源码 | <https://salsa.debian.org/debian/edb-debugger> |

### exifprobe

Read metadata from digital pictures Exifprobe reads image files produced by digital cameras (including several so-called “raw” file formats) and reports the structure of the files and the auxiliary data and metadata contained within them. In addition to TIFF, JPEG and EXIF, the program understands several formats which may contain “raw” camera data, including MRW, CIFF/CRW,

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/exifprobe/> |
| 版本 | 2.0.1 |
| 包 / 命令 | `exifprobe`、`exifgrep` |
| 安装 | `sudo apt install exifprobe` |
| 占用空间 | 506 KB |
| 依赖 | `libc6`、`exifgrep` |
| 官网 | <https://github.com/hfiguiere/exifprobe> |
| 源码 | <https://salsa.debian.org/pkg-security-team/exifprobe> |

### exiv2

EXIF/IPTC/XMP metadata manipulation tool Exiv2 is a C++ library and a command line utility to manage image metadata. It provides fast and easy read and write access to the Exif, IPTC and XMP metadata of images in various formats Exiv2 command line utility to: print Exif, IPTC and XMP image metadata in different formats:

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/exiv2/> |
| 版本 | 0.28.9 |
| 包 / 命令 | `exiv2`、`libexiv2-28`、`libexiv2-data`、`libexiv2-dev`、`libexiv2-doc` |
| 安装 | `sudo apt install exiv2` |
| 占用空间 | 436 KB |
| 依赖 | `libc6`、`libexiv2-28`、`libgcc-s1`、`libstdc++6`、`exiv2` |
| 官网 | <https://www.exiv2.org/> |
| 源码 | <https://salsa.debian.org/qt-kde-team/3rdparty/exiv2> |

### ext3grep

Tool to help recover deleted files on ext3 filesystems ext3grep is a simple tool intended to aid anyone who accidentally deletes a file on an ext3 filesystem, only to find that they wanted it shortly thereafter. This package is useful in forensics investigations.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、数据恢复、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/ext3grep/> |
| 版本 | 0.10.2 |
| 包 / 命令 | `ext3grep` |
| 安装 | `sudo apt install ext3grep` |
| 占用空间 | 299 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6`、`ext3grep` |
| 源码 | <https://salsa.debian.org/pkg-security-team/ext3grep> |

### ext4magic

Recover deleted files from ext3 or ext4 partitions ext4magic is a file carver (or file carving). It can be used when recovering from disasters or in digital forensics activities. The deletion of files in ext3/4 filesystems can not be easily reversed. Zero out of the block references in the inodes makes that impossible. Experiences with other programs have proved that is possible restore sufficient information

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/ext4magic/> |
| 版本 | 0.3.2 |
| 包 / 命令 | `ext4magic` |
| 安装 | `sudo apt install ext4magic` |
| 占用空间 | 235 KB |
| 依赖 | `libblkid1`、`libbz2-1.0`、`libc6`、`libext2fs2t64`、`libmagic1t64`、`libuuid1`、`zlib1g`、`ext4magic` |
| 官网 | <http://ext4magic.sf.net/ext4magic_en.html> |
| 源码 | <https://salsa.debian.org/pkg-security-team/ext4magic> |

### extundelete

Utility to recover deleted files from ext3/ext4 partition extundelete uses the information stored in the partition’s journal to attempt to recover a file that has been deleted. There is no guarantee that any particular file will be able to be undeleted.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、数据恢复、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/extundelete/> |
| 版本 | 0.2.4 |
| 包 / 命令 | `extundelete` |
| 安装 | `sudo apt install extundelete` |
| 占用空间 | 152 KB |
| 依赖 | `libc6`、`libcom-err2`、`libext2fs2t64`、`libgcc-s1`、`libstdc++6`、`extundelete` |
| 官网 | <http://extundelete.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/extundelete> |

### firmware-mod-kit

Deconstruct and reconstruct firmware images The Firmware Mod Kit allows for easy deconstruction and reconstruction of firmware images for various embedded devices. While it primarily targets Linux based routers, it should be compatible with most firmware that makes use of common firmware formats and file systems such as TRX/uImage and SquashFS/CramFS.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/firmware-mod-kit/> |
| 版本 | 0.99 |
| 包 / 命令 | `firmware-mod-kit` |
| 安装 | `sudo apt install firmware-mod-kit` |
| 占用空间 | 52.89 MB |
| 依赖 | `git`、`liblzma-dev`、`python3-magic`、`zlib1g-dev` |
| 官网 | <https://github.com/rampageX/firmware-mod-kit> |
| 源码 | <https://gitlab.com/kalilinux/packages/firmware-mod-kit> |

### foremost

Forensic program to recover lost files Foremost is a forensic program to recover lost files based on their headers, footers, and internal data structures. Foremost can work on image files, such as those generated by dd, Safeback, Encase, etc, or directly on a drive. The headers and footers can be specified by a configuration file or you can use

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/foremost/> |
| 版本 | 1.5.7 |
| 包 / 命令 | `foremost` |
| 安装 | `sudo apt install foremost` |
| 占用空间 | 101 KB |
| 依赖 | `libc6`、`foremost` |
| 官网 | <https://sourceforge.net/projects/foremost/> |
| 源码 | <https://salsa.debian.org/rul/foremost/tree/debian/sid> |

### forensic-artifacts

Knowledge base of forensic artifacts (data files) A free, community-sourced, machine-readable knowledge base of forensic artifacts that the world can use both as an information source and within other tools. This package installs the data files alone, without the Python toolkit.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/forensic-artifacts/> |
| 版本 | 20230928 |
| 包 / 命令 | `forensic-artifacts`、`python3-artifacts` |
| 安装 | `sudo apt install forensic-artifacts` |
| 占用空间 | 425 KB |
| 依赖 | `forensic-artifacts`、`python3`、`python3-pip`、`python3-yaml` |
| 官网 | <https://github.com/ForensicArtifacts/artifacts> |
| 源码 | <https://salsa.debian.org/pkg-security-team/forensic-artifacts> |

### forensics-colorize

Show differences between files using color graphics forensics-colorize is a set of tools to visually compare large files, as filesystem images, creating graphics of them. It is intuitive because the produced graphics provide a quick and perfect sense about the percentage of changes between two files. Comparing large textual files using a simple diff can produce a very big

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/forensics-colorize/> |
| 版本 | 1.1 |
| 包 / 命令 | `forensics-colorize`、`colorize`、`filecompare` |
| 安装 | `sudo apt install forensics-colorize` |
| 占用空间 | 2.05 MB |
| 依赖 | `libc6`、`colorize` |
| 官网 | <https://github.com/jessek/colorize> |
| 源码 | <https://salsa.debian.org/pkg-security-team/forensics-colorize> |

### galleta

Internet Explorer cookie forensic analysis tool Galleta is a forensics tool that examines the content of cookie files produced by Microsoft Internet Explorer (MSIE). It parses the file and outputs a field separated that can be loaded in a spreadsheet.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/galleta/> |
| 版本 | 1.0 |
| 包 / 命令 | `galleta` |
| 安装 | `sudo apt install galleta` |
| 占用空间 | 31 KB |
| 依赖 | `libc6`、`galleta` |
| 官网 | <https://odessa.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/galleta> |

### gdb

GNU Debugger GDB is a source-level debugger, capable of breaking programs at any specific line, displaying variable values, and determining where errors occurred. Currently, gdb supports C, C++, D, Objective-C, Fortran, Java, OpenCL C, Pascal, assembly, Modula-2, Go, and Ada. A must-have for any serious programmer.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/gdb/> |
| 版本 | 17.2 |
| 包 / 命令 | `gdb`、`gcore`、`gdb-add-index`、`gdbtui`、`gstack`、`gdb-minimal`、`gdb-multiarch`、`gdb-source`、`gdbserver` |
| 安装 | `sudo apt install gdb` |
| 占用空间 | 12.16 MB |
| 依赖 | `libc6`、`libdebuginfod1t64`、`libexpat1`、`libgcc-s1`、`libgmp10`、`libipt2`、`liblzma5`、`libmpfr6`、`libncursesw6`、`libpython3.14`、`libreadline8t64`、`libsource-highlight4t64` 等 |
| 官网 | <https://www.gnu.org/s/gdb/> |
| 源码 | <https://salsa.debian.org/gdb-team/gdb> |

### gpart

Guess PC disk partition table, find lost partitions Gpart is a tool which tries to guess the primary partition table of a PC-type disk in case the primary partition table in sector 0 is damaged, incorrect or deleted. It is also good at finding and listing the types, locations, and sizes of inadvertently-deleted partitions, both primary and logical. It gives you the

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/gpart/> |
| 版本 | 0.3 |
| 包 / 命令 | `gpart` |
| 安装 | `sudo apt install gpart` |
| 占用空间 | 76 KB |
| 依赖 | `libc6`、`gpart` |
| 官网 | <https://github.com/baruch/gpart> |
| 源码 | <https://salsa.debian.org/pkg-security-team/gpart> |

### gparted

GNOME partition editor GParted uses libparted to detect and manipulate devices and partition tables while several (optional) filesystem tools provide support for filesystems not included in libparted.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/gparted/> |
| 版本 | 1.8.0 |
| 包 / 命令 | `gparted`、`gparted-common` |
| 安装 | `sudo apt install gparted` |
| 占用空间 | 2.25 MB |
| 依赖 | `gparted-common`、`libatkmm-1.6-1v5`、`libc6`、`libcairomm-1.0-1v5`、`libgcc-s1`、`libglib2.0-0t64`、`libglibmm-2.4-1t64`、`libgtk-3-0t64`、`libgtkmm-3.0-1t64`、`libpangomm-1.4-1v5`、`libparted-fs-resize0t64`、`libparted2t64` 等 |
| 官网 | <https://gparted.org> |
| 源码 | <https://salsa.debian.org/debian/gparted> |

### grokevt

Scripts for reading Microsoft Windows event log files GrokEVT is a collection of scripts built for reading Microsoft Windows NT/2000/XP/2003 event log files. Currently the scripts work together on one or more mounted Microsoft Windows partitions to extract all information needed (registry entries, message templates, and log files) to convert the logs to a human-readable format.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 检测、数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/grokevt/> |
| 版本 | 0.5.0 |
| 包 / 命令 | `grokevt`、`grokevt-addlog`、`grokevt-builddb`、`grokevt-dumpmsgs`、`grokevt-findlogs`、`grokevt-parselog`、`grokevt-ripdll` |
| 安装 | `sudo apt install grokevt` |
| 占用空间 | 122 KB |
| 依赖 | `python3`、`python3-pyregfi`、`reglookup`、`grokevt-addlog` |
| 官网 | <http://projects.sentinelchicken.org/grokevt/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/grokevt> |

### guymager

Forensic imaging tool based on Qt The forensic imager contained in this package, guymager, was designed to support different image file formats, to be most user-friendly and to run really fast. It has a high speed multi-threaded engine using parallel compression for best performance on multi-processor and hyper-threading machines.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/guymager/> |
| 版本 | 0.8.13 |
| 包 / 命令 | `guymager` |
| 安装 | `sudo apt install guymager` |
| 占用空间 | 1.02 MB |
| 依赖 | `hdparm`、`libc6`、`libewf2`、`libgcc-s1`、`libguytools2t64` |
| 官网 | <https://guymager.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/guymager> |

### hashdeep

Recursively compute hashsums or piecewise hashings hashdeep is a set of tools to compute MD5, SHA1, SHA256, tiger and whirlpool hashsums of arbitrary number of files recursively. The main hashdeep features are: It can compare those hashsums with a list of known hashes; The tools can display those that match the list or those that

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/hashdeep/> |
| 版本 | 4.4 |
| 包 / 命令 | `hashdeep`、`md5deep`、`sha1deep`、`sha256deep`、`tigerdeep`、`whirlpooldeep` |
| 安装 | `sudo apt install hashdeep` |
| 占用空间 | 1.57 MB |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6`、`hashdeep` |
| 官网 | <https://md5deep.sourceforge.net> |
| 源码 | <https://salsa.debian.org/pkg-security-team/hashdeep> |

### hivex

Utilities for reading and writing Windows Registry hives libhivex is a self-contained library for reading and writing Windows Registry “hive” binary files. This package contains a few command line programs that utilize libhivex.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/hivex/> |
| 版本 | 1.3.24 |
| 包 / 命令 | `libhivex-bin`、`hivexget`、`hivexml`、`hivexsh`、`libhivex-dev`、`libhivex-ocaml`、`libhivex-ocaml-dev`、`libhivex0`、`libwin-hivex-perl`、`hivexregedit`、`python3-hivex`、`ruby-hivex` |
| 安装 | `sudo apt install libhivex-bin` |
| 占用空间 | 244 KB |
| 依赖 | `libc6`、`libhivex0`、`libreadline8t64`、`libxml2-16`、`hivexget` |
| 官网 | <http://libguestfs.org/> |
| 源码 | <https://salsa.debian.org/libvirt-team/hivex> |

### inetsim

Software suite for simulating common internet services INetSim is a software suite for simulating common internet services in a lab environment, e.g. for analyzing the network behaviour of unknown malware samples. INetSim supports simulation of the following services: HTTP, SMTP, POP3, DNS, FTP, NTP, TFTP, IRC, Ident, Finger, Syslog,

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/inetsim/> |
| 版本 | 1.3.2 |
| 包 / 命令 | `inetsim` |
| 安装 | `sudo apt install inetsim` |
| 占用空间 | 1.07 MB |
| 依赖 | `libdigest-sha-perl`、`libipc-shareable-perl`、`libnet-dns-perl`、`libnet-server-perl`、`openssl`、`perl` |
| 官网 | <https://www.inetsim.org/index.html> |
| 源码 | <https://salsa.debian.org/pkg-security-team/inetsim> |

### jadx

Dex to Java decompiler This package contains a Dex to Java decompiler. It contains a command line and GUI tools for produce Java source code from Android Dex and Apk files. Main features: - decompile Dalvik bytecode to java classes from APK, dex, aar and zip files - decode AndroidManifest.xml and other resources from resources.arsc

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应、逆向工程 |
| Kali 文档 | <https://www.kali.org/tools/jadx/> |
| 版本 | 1.5.6 |
| 包 / 命令 | `jadx`、`jadx-gui` |
| 安装 | `sudo apt install jadx` |
| 占用空间 | 74.63 MB |
| 依赖 | `default-jre`、`jadx` |
| 官网 | <https://github.com/skylot/jadx> |
| 源码 | <https://gitlab.com/kalilinux/packages/jadx> |

### javasnoop

Intercept Java applications locally Normally, without access to the original source code, testing the security of a Java client is unpredictable at best and unrealistic at worst. With access the original source, you can run a simple Java program and attach a debugger to it remotely, stepping through code and changing

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应、逆向工程 |
| Kali 文档 | <https://www.kali.org/tools/javasnoop/> |
| 版本 | 1.1 |
| 包 / 命令 | `javasnoop` |
| 安装 | `sudo apt install javasnoop` |
| 占用空间 | 13.14 MB |
| 依赖 | `default-jdk`、`javasnoop` |
| 源码 | <https://gitlab.com/kalilinux/packages/javasnoop> |

### libewf

Collection of tools for reading and writing EWF files Libewf is a library with support for reading and writing the Expert Witness Compression Format (EWF). This library allows you to read media information of EWF files in the SMART (EWF-S01) format and the EnCase (EWF-E01) format. It supports files created by EnCase 1 to 6, linen and FTK Imager. The libewf is useful for forensics

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/libewf/> |
| 版本 | 20140816 |
| 包 / 命令 | `ewf-tools`、`ewfacquire`、`ewfacquirestream`、`ewfdebug`、`ewfexport`、`ewfinfo`、`ewfmount`、`ewfrecover`、`ewfverify`、`libewf-dev`、`libewf2`、`python3-libewf` |
| 安装 | `sudo apt install ewf-tools` |
| 占用空间 | 6.64 MB |
| 依赖 | `libc6`、`libewf2`、`libfuse3-4`、`libssl3t64`、`ewfacquire` |
| 官网 | <https://github.com/libyal/libewf-legacy> |
| 源码 | <https://salsa.debian.org/pkg-security-team/libewf> |

### libpst

Library for reading Microsoft Outlook PST files (development files) Library for accessing data from Microsoft Outlook PST files. This package include the files needed for developing with libpst, including the headers, static library and documentation.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/libpst/> |
| 版本 | 0.6.76 |
| 包 / 命令 | `libpst-dev`、`libpst4t64`、`pst-utils`、`lspst`、`nick2ldif`、`pst2dii`、`pst2ldif`、`readpst` |
| 安装 | `sudo apt install libpst-dev` |
| 占用空间 | 2.58 MB |
| 依赖 | `libpst4t64`、`libpst4t64` |
| 官网 | <https://www.five-ten-sg.com/libpst/> |
| 源码 | <https://salsa.debian.org/debian/libpst> |

### libsmali-java

Assembler/disassembler for Android’s dex format smali/baksmali is an assembler/disassembler for the dex format used by dalvik, Android’s Java VM implementation. The syntax is loosely based on Jasmin’s/dedexer’s syntax and supports the full functionality of the dex format like annotations, debug info and line info.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应、逆向工程 |
| Kali 文档 | <https://www.kali.org/tools/libsmali-java/> |
| 版本 | 2.5.2.git2771eae |
| 包 / 命令 | `libsmali-java`、`baksmali`、`smali` |
| 安装 | `sudo apt install libsmali-java` |
| 占用空间 | 1.57 MB |
| 依赖 | `java-wrappers`、`libantlr3-runtime-java`、`libguava-java`、`libjcommander-java`、`baksmali` |
| 官网 | <https://github.com/JesusFreke/smali> |
| 源码 | <https://salsa.debian.org/android-tools-team/libsmali-java> |

### lvm2

Linux Logical Volume Manager This is LVM2, the rewrite of The Linux Logical Volume Manager. LVM supports enterprise level volume management of disk and disk subsystems by grouping arbitrary disks into volume groups. The total capacity of volume groups can be allocated to logical volumes, which are accessed as regular block devices.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、防护、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/lvm2/> |
| 版本 | 2.03.31 |
| 包 / 命令 | `dmeventd`、`dmsetup`、`blkdeactivate`、`dmstats`、`dmsetup-udeb`、`libdevmapper-dev`、`libdevmapper-event1.02.1`、`libdevmapper1.02.1`、`libdevmapper1.02.1-udeb`、`liblvm2-dev`、`liblvm2cmd2.03`、`lvm2`、`fsadm`、`lvchange`、`lvconvert`、`lvcreate`、`lvdisplay`、`lvextend`、`lvm`、`lvmconfig`、`lvmdiskscan`、`lvmdump`、`lvmpolld`、`lvmsadc`、`lvmsar`、`lvreduce`、`lvremove`、`lvrename`、`lvresize`、`lvs`、`lvscan`、`pvchange`、`pvck`、`pvcreate`、`pvdisplay`、`pvmove`、`pvremove`、`pvresize`、`pvs`、`pvscan`、`vgcfgbackup`、`vgcfgrestore`、`vgchange`、`vgck`、`vgconvert`、`vgcreate`、`vgdisplay`、`vgexport`、`vgextend`、`vgimport`、`vgimportclone`、`vgmerge`、`vgmknodes`、`vgreduce`、`vgremove`、`vgrename`、`vgs`、`vgscan`、`vgsplit`、`lvm2-dbusd`、`lvmdbusd`、`lvm2-lockd`、`lvmlockctl`、`lvmlockd`、`lvm2-udeb` |
| 安装 | `sudo apt install lvm2` |
| 占用空间 | 3.96 MB |
| 依赖 | `dmeventd`、`dmsetup`、`libaio1t64`、`libblkid1`、`libc6`、`libdevmapper-event1.02.1`、`libedit2`、`libselinux1`、`libsystemd0`、`libudev1`、`fsadm` |
| 官网 | <https://sourceware.org/lvm2/> |
| 源码 | <https://salsa.debian.org/lvm-team/lvm2> |

### mac-robber

Collects data about allocated files in mounted filesystems mac-robber is a digital investigation tool (digital forensics) that collects metadata from allocated files in a mounted filesystem. This is useful during incident response when analyzing a live system or when analyzing a dead system in a lab. The data can be used by the mactime tool in The Sleuth Kit (TSK or SleuthKit only) to make a timeline of file activity. The mac-robber

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/mac-robber/> |
| 版本 | 1.02 |
| 包 / 命令 | `mac-robber` |
| 安装 | `sudo apt install mac-robber` |
| 占用空间 | 35 KB |
| 依赖 | `libc6`、`mac-robber` |
| 官网 | <https://www.sleuthkit.org/mac-robber> |
| 源码 | <https://salsa.debian.org/pkg-security-team/mac-robber> |

### magicrescue

Recover files by looking for magic bytes Magic Rescue scans a block device for file types it knows how to recover and calls an external program to extract them. It looks at “magic bytes” (file patterns) in file contents, so it can be used both as an undelete utility and for recovering a corrupted drive or partition. As long as the file data is there, it will find it.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/magicrescue/> |
| 版本 | 1.1.10 |
| 包 / 命令 | `magicrescue`、`dupemap`、`magicsort` |
| 安装 | `sudo apt install magicrescue` |
| 占用空间 | 257 KB |
| 依赖 | `dcraw`、`flac`、`libc6`、`libgdbm-compat4t64`、`libjpeg-turbo-progs`、`mpg123`、`sqlite3`、`unzip`、`zip`、`dupemap` |
| 官网 | <https://github.com/jbj/magicrescue> |
| 源码 | <https://salsa.debian.org/pkg-security-team/magicrescue> |

### mdbtools

JET / MS Access database (MDB) tools These are various tools for manipulating JET / MS Access database (MDB) files: utils - provides command line utilities to list tables, export schema, and data, show file versions, and other useful stuff. mdb-sql - a command line SQL tool that allows one to type SQL queries and get results.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数据库、数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/mdbtools/> |
| 版本 | 1.0.1 |
| 包 / 命令 | `libmdb3t64`、`libmdbsql3t64`、`mdbtools`、`mdb-array`、`mdb-count`、`mdb-export`、`mdb-header`、`mdb-hexdump`、`mdb-import`、`mdb-json`、`mdb-parsecsv`、`mdb-prop`、`mdb-queries`、`mdb-schema`、`mdb-sql`、`mdb-tables`、`mdb-ver`、`mdbtools-dev`、`mdbtools-doc`、`odbc-mdbtools` |
| 安装 | `sudo apt install mdbtools` |
| 占用空间 | 268 KB |
| 依赖 | `libc6`、`libglib2.0-0t64`、`libmdb3t64`、`libmdbsql3t64`、`libreadline8t64`、`mdb-array` |
| 官网 | <https://github.com/mdbtools/mdbtools> |
| 源码 | <https://salsa.debian.org/debian/mdbtools> |

### memdump

Utility to dump memory contents to standard output Program which dumps system memory to the standard output stream, skipping over holes in memory maps. By default, the program dumps the contents of physical memory. This program will not work if CONFIG_STRICT_DEVMEM is enabled in kernel. Since 2.6 version, several kernels are enabling this option by default.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/memdump/> |
| 版本 | 1.01 |
| 包 / 命令 | `memdump` |
| 安装 | `sudo apt install memdump` |
| 占用空间 | 44 KB |
| 依赖 | `libc6`、`memdump` |
| 官网 | <http://www.porcupine.org/forensics/tct.html> |
| 源码 | <https://salsa.debian.org/pkg-security-team/memdump> |

### metacam

Extract EXIF information from digital camera files EXIF (Exchangeable Image File Format) is a standard for storing interchange information in image files, especially those using JPEG compression. Most digital cameras, including mobile phones, now use the EXIF format. The format is part of the DCF standard created by JEIDA to encourage the interoperability between imaging devices. In addition to the standard EXIF

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/metacam/> |
| 版本 | 1.2 |
| 包 / 命令 | `metacam` |
| 安装 | `sudo apt install metacam` |
| 占用空间 | 142 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6`、`metacam` |
| 官网 | <http://www.cheeseplant.org/~daniel/pages/metacam.html> |
| 源码 | <https://salsa.debian.org/pkg-security-team/metacam> |

### missidentify

Find win32 applications Miss Identify (missidentify) is a program to find MS Windows type win32 applications. By default, it displays the filename of any executable that does not have an extension, as exe, dll, com, sys, cpl, hxs, hxi, olb, rll or tlb. It can also display all the executables regardless the extension. Miss Identify is useful in forensics investigations.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/missidentify/> |
| 版本 | 1.0 |
| 包 / 命令 | `missidentify` |
| 安装 | `sudo apt install missidentify` |
| 占用空间 | 47 KB |
| 依赖 | `libc6`、`missidentify` |
| 官网 | <https://missidentify.sf.net> |
| 源码 | <https://salsa.debian.org/pkg-security-team/missidentify> |

### myrescue

Rescue data from damaged disks myrescue is a program to rescue the still-readable data from a damaged harddisk, CD-ROM, DVD, flash drives, etc. It is similar in purpose to dd_rescue (or ddrescue), but it tries to quickly get out of damaged areas to first handle the not yet damaged part of the disk and return later.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、数据恢复、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/myrescue/> |
| 版本 | 0.9.8 |
| 包 / 命令 | `myrescue`、`myrescue-bitmap2ppm`、`myrescue-stat` |
| 安装 | `sudo apt install myrescue` |
| 占用空间 | 81 KB |
| 依赖 | `libc6`、`myrescue` |
| 官网 | <https://myrescue.sf.net> |
| 源码 | <https://salsa.debian.org/pkg-security-team/myrescue> |

### nasty

Tool which helps you to recover your GPG passphrase Nasty is a program that helps you to recover the passphrase of your PGP or GPG-key in case you forget or lost it. The following features will make things easier: set minimum/maximum length of the passphrase incremental mode, random mode or reads a file for guessing

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/nasty/> |
| 版本 | 0.6 |
| 包 / 命令 | `nasty` |
| 安装 | `sudo apt install nasty` |
| 占用空间 | 42 KB |
| 依赖 | `libc6`、`libgpgme45`、`nasty` |
| 官网 | <https://github.com/folkertvanheusden/nasty> |
| 源码 | <https://salsa.debian.org/pkg-security-team/nasty> |

### ollydbg

32-bit assembler level analysing debugger OllyDbg is a 32-bit assembler level analysing debugger for Microsoft Windows. Emphasis on binary code analysis makes it particularly useful in cases where source is unavailable.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应、逆向工程、Windows 资源 |
| Kali 文档 | <https://www.kali.org/tools/ollydbg/> |
| 版本 | 1.10 |
| 包 / 命令 | `ollydbg` |
| 安装 | `sudo apt install ollydbg` |
| 占用空间 | 2.50 MB |
| 依赖 | `kali-defaults`、`wine`、`ollydbg` |
| 官网 | <http://www.ollydbg.de/> |
| 源码 | <https://gitlab.com/kalilinux/packages/ollydbg> |

### parted

Disk partition manipulator GNU Parted is a program that allows you to create, destroy, resize, move, and copy disk partitions. This is useful for creating space for new operating systems, reorganizing disk usage, and copying data to new hard disks. This package contains the binary and manual page. Further

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/parted/> |
| 版本 | 3.7 |
| 包 / 命令 | `libparted-dev`、`libparted-fs-resize0-udeb`、`libparted-fs-resize0t64`、`libparted-i18n`、`libparted2-udeb`、`libparted2t64`、`parted`、`partprobe`、`parted-doc`、`parted-udeb` |
| 安装 | `sudo apt install parted` |
| 占用空间 | 122 KB |
| 依赖 | `libc6`、`libparted2t64`、`libreadline8t64`、`libtinfo6`、`libuuid1`、`parted` |
| 官网 | <https://www.gnu.org/software/parted> |
| 源码 | <https://salsa.debian.org/parted-team/parted> |

### pasco

Internet Explorer cache forensic analysis tool Pasco is a forensic tool that examines the content of cache files (index.dat) produced by Microsoft Internet Explorer. It parses the file and outputs a field separated that can be loaded in a spreadsheet. This package is useful in forensics investigations.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/pasco/> |
| 版本 | 20040505 |
| 包 / 命令 | `pasco` |
| 安装 | `sudo apt install pasco` |
| 占用空间 | 34 KB |
| 依赖 | `libc6`、`pasco` |
| 官网 | <https://sf.net/projects/odessa> |
| 源码 | <https://salsa.debian.org/pkg-security-team/pasco> |

### pdf-parser

Parses PDF files to identify fundamental elements This tool will parse a PDF document to identify the fundamental elements used in the analyzed file. It will not render a PDF document.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/pdf-parser/> |
| 版本 | 0.7.14 |
| 包 / 命令 | `pdf-parser` |
| 安装 | `sudo apt install pdf-parser` |
| 占用空间 | 87 KB |
| 依赖 | `python3`、`python3-pyzipper`、`zlib1g`、`pdf-parser` |
| 官网 | <https://blog.didierstevens.com/programs/pdf-tools/> |
| 源码 | <https://gitlab.com/kalilinux/packages/pdf-parser> |

### pdfid

Scans PDF files for certain PDF keywords This tool is not a PDF parser, but it will scan a file to look for certain PDF keywords, allowing you to identify PDF documents that contain (for example) JavaScript or execute an action when opened. PDFiD will also handle name obfuscation.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/pdfid/> |
| 版本 | 0.2.10 |
| 包 / 命令 | `pdfid` |
| 安装 | `sudo apt install pdfid` |
| 占用空间 | 106 KB |
| 依赖 | `python3`、`python3-pyzipper`、`python3-simplejson`、`pdfid` |
| 官网 | <https://blog.didierstevens.com/programs/pdf-tools/> |
| 源码 | <https://gitlab.com/kalilinux/packages/pdfid> |

### plaso

Super timeline all the things – metapackage This is a metapackage that depends on the Python 3 package of the Plaso libraries and scripts.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/plaso/> |
| 版本 | 20260119 |
| 包 / 命令 | `plaso`、`python3-plaso`、`plaso-image_export`、`plaso-log2timeline`、`plaso-pinfo`、`plaso-psort`、`plaso-psteal` |
| 安装 | `sudo apt install plaso` |
| 占用空间 | 39 KB |
| 依赖 | `python3-plaso`、`python3-plaso` |
| 官网 | <https://github.com/log2timeline/plaso> |
| 源码 | <https://salsa.debian.org/pkg-security-team/plaso> |

### python-pip

Python package installer pip is the Python package installer. It integrates with virtualenv, doesn’t do partial installs, can save package state for replaying, can install from non-egg sources, and can install from version control repositories. This is the Python 3 version of the package.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/python-pip/> |
| 版本 | 26.1.2 |
| 包 / 命令 | `python3-pip`、`pip`、`pip3`、`python3-pip-whl` |
| 安装 | `sudo apt install python3-pip` |
| 占用空间 | 9.65 MB |
| 依赖 | `ca-certificates`、`python3`、`python3-wheel`、`pip` |
| 官网 | <https://pip.pypa.io/en/stable/> |
| 源码 | <https://salsa.debian.org/python-team/packages/python-pip> |

### radare2

Free and advanced command line hexadecimal editor The project aims to create a complete, portable, multi-architecture, unix-like toolchain for reverse engineering. It is composed by an hexadecimal editor (radare) with a wrapped IO layer supporting multiple backends for local/remote files, debugger (OS X, BSD, Linux, W32), stream analyzer, assembler/disassembler (rasm)

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、硬件攻击、事件响应、逆向工程 |
| Kali 文档 | <https://www.kali.org/tools/radare2/> |
| 版本 | 6.0.4 |
| 包 / 命令 | `libradare2-6.0.0t64`、`libradare2-common`、`libradare2-dev`、`radare2`、`r2`、`r2agent`、`r2pm`、`r2r`、`r2sdb`、`rabin2`、`radiff2`、`rafind2`、`ragg2`、`rahash2`、`rapatch2`、`rarun2`、`rasign2`、`rasm2`、`ravc2`、`rax2` |
| 安装 | `sudo apt install radare2` |
| 占用空间 | 3.58 MB |
| 依赖 | `libc6`、`libradare2-6.0.0t64`、`r2` |
| 官网 | <https://www.radare.org> |
| 源码 | <https://salsa.debian.org/pkg-security-team/radare2> |

### readpe

Command-line tools to manipulate Windows PE files readpe is a toolkit designed to analyze Microsoft Windows PE (Portable Executable) binary files. Its tools can parse and compare PE32/PE32+ executable files (EXE, DLL, OCX, etc), and analyze them in search of suspicious characteristics. It can be used to get information from those executable files, such as

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/readpe/> |
| 版本 | 0.85.1 |
| 包 / 命令 | `libpe-dev`、`libpe1t64`、`readpe`、`ofs2rva`、`pedis`、`pehash`、`peldd`、`pepack`、`peres`、`pescan`、`pesec`、`pestr`、`rva2ofs` |
| 安装 | `sudo apt install readpe` |
| 占用空间 | 1.23 MB |
| 依赖 | `libc6`、`libpe1t64`、`libssl3t64`、`ofs2rva` |
| 官网 | <https://github.com/mentebinaria/readpe/wiki> |
| 源码 | <https://salsa.debian.org/pkg-security-team/readpe> |

### recoverdm

Recover files on disks with damaged sectors recoverdm recover disks with bad sectors. You can recover files as well complete devices. In case it finds sectors which simply cannot be recovered, it writes an empty sector to the output file and continues. When recovering a CD or a DVD and the program cannot read the sector in “normal mode”, then the program will try to read the sector in “RAW mode”

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、数据恢复、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/recoverdm/> |
| 版本 | 0.20 |
| 包 / 命令 | `recoverdm`、`mergebad` |
| 安装 | `sudo apt install recoverdm` |
| 占用空间 | 64 KB |
| 依赖 | `libc6`、`mergebad` |
| 官网 | <https://www.vanheusden.com/recoverdm> |
| 源码 | <https://salsa.debian.org/pkg-security-team/recoverdm> |

### recoverjpeg

Recover JFIF (JPEG) pictures and MOV movies recoverjpeg tries to recover JFIF (JPEG) pictures and MOV movies from a peripheral. This may be useful if you mistakenly overwrite a partition or if a device such as a digital camera memory card is bogus. This package provides these executables: recoverjpeg, recovermov, remove-duplicates and sort-pictures. The remove-duplicates is useful to

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、数据恢复、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/recoverjpeg/> |
| 版本 | 2.6.3 |
| 包 / 命令 | `recoverjpeg`、`recovermov`、`remove-duplicates`、`sort-pictures` |
| 安装 | `sudo apt install recoverjpeg` |
| 占用空间 | 65 KB |
| 依赖 | `exif`、`imagemagick`、`libc6`、`libgcc-s1`、`libstdc++6`、`python3`、`recoverjpeg` |
| 官网 | <https://www.rfc1149.net/devel/recoverjpeg> |
| 源码 | <https://salsa.debian.org/pkg-security-team/recoverjpeg> |

### reglookup

Utility to analysis for Windows NT-based registry RegLookup is a system to direct analysis of Windows NT-based registry files providing command line tools, a C API, and a Python module for accessing registry data structures. The project has a focus on providing tools for digital forensics investigations (though is useful for many purposes), and includes algorithms for retrieving deleted data structures

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 检测、数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/reglookup/> |
| 版本 | 1.0.1 |
| 包 / 命令 | `libregfi-dev`、`libregfi1t64`、`python3-pyregfi`、`reglookup`、`reglookup-recover`、`reglookup-timeline`、`reglookup-doc` |
| 安装 | `sudo apt install reglookup` |
| 占用空间 | 87 KB |
| 依赖 | `libc6`、`libregfi1t64`、`libtalloc2`、`reglookup` |
| 官网 | <https://web.archive.org/web/20240804024044/http://projects.sentinelchicken.org/reglookup/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/reglookup> |

### regripper

Perform forensic analysis of registry hives Regripper’s CLI tool can be used to surgically extract, translate, and display information (both data and metadata) from Registry-formatted files via plugins in the form of Perl-scripts. It allows the analyst to select a hive-file to parse and a plugin or a profile, which is a list of plugins to run against the given hive. The results go to STDOUT and

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应、Windows 资源 |
| Kali 文档 | <https://www.kali.org/tools/regripper/> |
| 版本 | 3.0~git20260527.ec96dd4 |
| 包 / 命令 | `regripper` |
| 安装 | `sudo apt install regripper` |
| 占用空间 | 1.11 MB |
| 依赖 | `libparse-win32registry-perl`、`perl`、`regripper` |
| 官网 | <https://github.com/keydet89/RegRipper3.0> |
| 源码 | <https://salsa.debian.org/pkg-security-team/regripper> |

### rephrase

Specialized passphrase recovery tool for GnuPG If you can nearly remember your GnuPG passphrase - but not quite - then Rephrase may be able to help. Tell Rephrase the parts of the passphrase you know, and any number of alternatives for the parts you’re not sure about; and Rephrase will try all the alternatives, in all possible combinations, and tell you which combination (if any) gives you the correct passphrase.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/rephrase/> |
| 版本 | 0.2 |
| 包 / 命令 | `rephrase` |
| 安装 | `sudo apt install rephrase` |
| 占用空间 | 43 KB |
| 依赖 | `gnupg`、`libc6`、`rephrase` |
| 官网 | <https://www.roguedaemon.net/rephrase/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/rephrase> |

### rifiuti

MS Windows recycle bin analysis tool Rifiuti is a tool to examine the INFO2 files. The INFO2 file gives meta information about the files found in the MS Windows recycle bin. This package is useful in forensics investigations.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/rifiuti/> |
| 版本 | 20040505 |
| 包 / 命令 | `rifiuti` |
| 安装 | `sudo apt install rifiuti` |
| 占用空间 | 30 KB |
| 依赖 | `libc6`、`rifiuti` |
| 官网 | <https://sf.net/projects/odessa> |
| 源码 | <https://salsa.debian.org/pkg-security-team/rifiuti> |

### rifiuti2

Replacement for rifiuti, a MS Windows recycle bin analysis tool Rifiuti2 analyses recycle bin files from Windows. Analysis of Windows recycle bin is usually carried out during Windows computer forensics. Rifiuti2 can extract file deletion time, original path and size of deleted files and whether the deleted files have been moved out from the recycle bin since they are trashed.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/rifiuti2/> |
| 版本 | 0.8.2 |
| 包 / 命令 | `rifiuti2`、`rifiuti-vista` |
| 安装 | `sudo apt install rifiuti2` |
| 占用空间 | 134 KB |
| 依赖 | `libc6`、`libglib2.0-0t64`、`rifiuti-vista` |
| 官网 | <https://abelcheung.github.io/rifiuti2> |
| 源码 | <https://salsa.debian.org/pkg-security-team/rifiuti2> |

### rizin

Reverse engineering framework and command-line toolset Rizin is a fork of the radare2 reverse engineering framework with a focus on usability, working features and code cleanliness. Rizin is portable and it can be used to analyze binaries, disassemble code, debug programs, as a forensics tool, as a scriptable command-line hexadecimal editor able to open disk files, and much more!

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、硬件攻击、事件响应、逆向工程 |
| Kali 文档 | <https://www.kali.org/tools/rizin/> |
| 版本 | 0.9.1 |
| 包 / 命令 | `librizin-common`、`librizin-dev`、`librizin0`、`rizin`、`rz-ar`、`rz-asm`、`rz-ax`、`rz-bin`、`rz-diff`、`rz-find`、`rz-gg`、`rz-hash`、`rz-run`、`rz-sign`、`rz-test` |
| 安装 | `sudo apt install rizin` |
| 占用空间 | 334 KB |
| 依赖 | `libc6`、`librizin0`、`rizin` |
| 官网 | <https://rizin.re/> |
| 源码 | <https://gitlab.com/kalilinux/packages/rizin> |

### rizin-cutter

Reverse engineering platform powered by rizin Cutter is a free and open-source reverse engineering platform powered by rizin. It aims at being an advanced and customizable reverse engineering platform while keeping the user experience in mind. Cutter is created by reverse engineers for reverse engineers.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、硬件攻击、事件响应、逆向工程 |
| Kali 文档 | <https://www.kali.org/tools/rizin-cutter/> |
| 版本 | 2.5.0 |
| 包 / 命令 | `librizin-cutter-dev`、`rizin-cutter`、`cutter` |
| 安装 | `sudo apt install rizin-cutter` |
| 占用空间 | 10.61 MB |
| 依赖 | `libc6`、`libcgraph8`、`libgcc-s1`、`libgvc7`、`libkf6syntaxhighlighting6`、`libpyside6-py3-6.10`、`libpython3.14`、`libqt6core5compat6`、`libqt6core6t64`、`libqt6gui6`、`libqt6network6`、`libqt6opengl6` 等 |
| 官网 | <https://cutter.re> |
| 源码 | <https://gitlab.com/kalilinux/packages/rizin-cutter> |

### rkhunter

Rootkit, backdoor, sniffer and exploit scanner Rootkit Hunter scans systems for known and unknown rootkits, backdoors, sniffers and exploits. It checks for: SHA256 hash changes; files commonly created by rootkits;

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/rkhunter/> |
| 版本 | 1.4.6 |
| 包 / 命令 | `rkhunter` |
| 安装 | `sudo apt install rkhunter` |
| 占用空间 | 1.05 MB |
| 依赖 | `binutils` |
| 官网 | <https://rkhunter.sourceforge.net> |
| 源码 | <https://salsa.debian.org/pkg-security-team/rkhunter> |

### rsakeyfind

Locates BER-encoded RSA private keys in memory images rsakeyfind is a tool that locates BER-encoded RSA private keys in MEMORY-IMAGE. If a MODULUS-FILE is specified, it will locate private and public keys matching the hex-encoded modulus read from this file. This package is useful to several activities, as forensics investigations.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/rsakeyfind/> |
| 版本 | 1.0 |
| 包 / 命令 | `rsakeyfind` |
| 安装 | `sudo apt install rsakeyfind` |
| 占用空间 | 34 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6`、`rsakeyfind` |
| 官网 | <https://citp.princeton.edu/our-work/memory/code/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/rsakeyfind> |

### rz-ghidra

Ghidra decompiler and sleigh disassembler for rizin This is an integration of the Ghidra decompiler and Sleigh Disassembler for rizin. It is solely based on the decompiler part of Ghidra, which is written entirely in C++, so Ghidra itself is not required at all and the plugin can be built self-contained.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、硬件攻击、事件响应、逆向工程 |
| Kali 文档 | <https://www.kali.org/tools/rz-ghidra/> |
| 版本 | 0.9.0 |
| 包 / 命令 | `rz-ghidra` |
| 安装 | `sudo apt install rz-ghidra` |
| 占用空间 | 18.67 MB |
| 依赖 | `libc6`、`libgcc-s1`、`libqt6core6t64`、`librizin0`、`libstdc++6`、`zlib1g` |
| 官网 | <https://github.com/rizinorg/rz-ghidra> |
| 源码 | <https://gitlab.com/kalilinux/packages/rz-ghidra> |

### safecopy

Data recovery tool for problematic or damaged media Safecopy tries to get as much data from SOURCE as possible, even resorting to device specific low level operations if applicable. This is achieved by identifying problematic or damaged areas, skipping over them and continuing reading afterwards. The corresponding area in the destination file is either skipped (on initial creation that means padded with zeros) or deliberately

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/safecopy/> |
| 版本 | 1.7 |
| 包 / 命令 | `safecopy` |
| 安装 | `sudo apt install safecopy` |
| 占用空间 | 97 KB |
| 依赖 | `libc6`、`safecopy` |
| 官网 | <http://safecopy.sf.net> |
| 源码 | <https://salsa.debian.org/pkg-security-team/safecopy> |

### scalpel

Fast filesystem-independent file recovery scalpel is a fast file carver that reads a database of header and footer definitions and extracts matching files from a set of image files or raw device files. scalpel is filesystem-independent and will carve files from FAT16, FAT32, exFAT, NTFS, Ext2, Ext3, Ext4, JFS, XFS, ReiserFS, raw partitions, etc.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/scalpel/> |
| 版本 | 1.60 |
| 包 / 命令 | `scalpel` |
| 安装 | `sudo apt install scalpel` |
| 占用空间 | 89 KB |
| 依赖 | `libc6`、`scalpel` |
| 官网 | <https://github.com/nolaforensix/scalpel-1.60> |
| 源码 | <https://salsa.debian.org/pkg-security-team/scalpel> |

### scrounge-ntfs

Data recovery program for NTFS filesystems Scrounge NTFS is a data recovery program for NTFS filesystems. It reads each block of the hard disk and try to rebuild the original filesystem tree into a directory. This package is useful in forensics investigations.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、数据恢复、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/scrounge-ntfs/> |
| 版本 | 0.9 |
| 包 / 命令 | `scrounge-ntfs` |
| 安装 | `sudo apt install scrounge-ntfs` |
| 占用空间 | 49 KB |
| 依赖 | `libc6`、`scrounge-ntfs` |
| 官网 | <http://thewalter.net/stef/software/scrounge/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/scrounge-ntfs> |

### sleuthkit

Tools for forensics analysis on volume and filesystem data The Sleuth Kit, also known as TSK, is a collection of UNIX-based command line file and volume system forensic analysis tools. The filesystem tools allow you to examine filesystems of a suspect computer in a non-intrusive fashion. Because the tools do not rely on the operating system to process the filesystems, deleted and hidden content is shown.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/sleuthkit/> |
| 版本 | 4.14.0 |
| 包 / 命令 | `libsleuthkit-java`、`libsleuthkit-jni`、`libtsk-dev`、`libtsk23`、`sleuthkit`、`blkcalc`、`blkcat`、`blkls`、`blkstat`、`fcat`、`ffind`、`fiwalk`、`fls`、`fsstat`、`hfind`、`icat`、`ifind`、`ils`、`img_cat`、`img_stat`、`istat`、`jcat`、`jls`、`jpeg_extract`、`mactime`、`mmcat`、`mmls`、`mmstat`、`pstat`、`sigfind`、`sorter`、`srch_strings`、`tsk_comparedir`、`tsk_gettimes`、`tsk_imageinfo`、`tsk_loaddb`、`tsk_recover`、`usnjls` |
| 安装 | `sudo apt install sleuthkit` |
| 占用空间 | 1.09 MB |
| 依赖 | `file`、`libafflib0t64`、`libbfio1`、`libc6`、`libdate-manip-perl`、`libewf2`、`libgcc-s1`、`libstdc++6`、`libtsk23`、`libvhdi1`、`libvmdk1`、`libvslvm1t64` 等 |
| 官网 | <https://www.sleuthkit.org/sleuthkit> |
| 源码 | <https://gitlab.com/kalilinux/packages/sleuthkit> |

### ssdeep

Recursive piecewise hashing tool ssdeep is a tool for recursive computing and matching of Context Triggered Piecewise Hashing (aka Fuzzy Hashing). Fuzzy hashing is a method for comparing similar but not identical files. This tool can be used to compare files like regular hashing does (like md5sum or sha1sum) but it will find similar files with little differences.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/ssdeep/> |
| 版本 | 2.14.1 |
| 包 / 命令 | `libfuzzy-dev`、`libfuzzy2`、`ssdeep` |
| 安装 | `sudo apt install ssdeep` |
| 占用空间 | 83 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6`、`ssdeep` |
| 官网 | <https://github.com/ssdeep-project/ssdeep> |
| 源码 | <https://salsa.debian.org/pkg-security-team/ssdeep> |

### tcpick

TCP stream sniffer and connection tracker This libpcap-based textmode sniffer can: track, reassemble and reorder TCP streams save the captured flows in different files or display them in the terminal display all the stream on the terminal with different display modes like hexdump, hexdump + ascii, only printable characters, raw mode, colorized

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/tcpick/> |
| 版本 | 0.2.1 |
| 包 / 命令 | `tcpick` |
| 安装 | `sudo apt install tcpick` |
| 占用空间 | 88 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`tcpick` |
| 官网 | <http://tcpick.sourceforge.net> |
| 源码 | <https://salsa.debian.org/pkg-security-team/tcpick> |

### unar

Unarchiver for a variety of file formats The Unarchiver is an archive unpacker program with support for the popular zip, RAR, 7z, tar, gzip, bzip2, LZMA, XZ, CAB, MSI, NSIS, EXE, ISO, BIN, and split file formats, as well as the old Stuffit, Stuffit X, DiskDouble, Compact Pro, Packit, cpio, compress (.Z), ARJ, ARC, PAK, ACE, ZOO, LZH, ADF, DMS, LZX, PowerPacker, LBR, Squeeze, Crunch, and other old formats.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/unar/> |
| 版本 | 1.10.8 |
| 包 / 命令 | `unar`、`lsar` |
| 安装 | `sudo apt install unar` |
| 占用空间 | 5.85 MB |
| 依赖 | `gnustep-base-runtime`、`libbz2-1.0`、`libc6`、`libgcc-s1`、`libgnustep-base1.31`、`libicu78`、`libobjc4`、`libstdc++6`、`libwavpack1`、`zlib1g`、`lsar` |
| 官网 | <https://theunarchiver.com/command-line> |
| 源码 | <https://salsa.debian.org/gnustep-team/unar> |

### undbx

Tool to extract, recover and undelete e-mail messages from .dbx files UnDBX is a tool to extract, recover and undelete e-mail messages from MS Outlook Express .dbx files (or similar e-mail programs in MS Windows). Corrupted .dbx files can be parsed to try to recover messages from it. It can also try to undelete messages, not only from Deleted Items but also from fragments of deleted messages that were not overwritten.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、数据恢复、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/undbx/> |
| 版本 | 0.21 |
| 包 / 命令 | `undbx` |
| 安装 | `sudo apt install undbx` |
| 占用空间 | 61 KB |
| 依赖 | `libc6`、`undbx` |
| 官网 | <https://github.com/ZungBang/undbx> |
| 源码 | <https://salsa.debian.org/pkg-security-team/undbx> |

### unhide

Forensic tool to find hidden processes and ports Unhide is a forensic tool to find processes and TCP/UDP ports hidden by rootkits, Linux kernel modules or by other techniques. It includes two utilities: unhide and unhide-tcp. unhide detects hidden processes using the following six techniques: Compare /proc vs /bin/ps output

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/unhide/> |
| 版本 | 20240510 |
| 包 / 命令 | `unhide`、`unhide-linux`、`unhide-posix`、`unhide-tcp`、`unhide_rb`、`unhide-gui` |
| 安装 | `sudo apt install unhide` |
| 占用空间 | 172 KB |
| 依赖 | `iproute2`、`libc6`、`lsof`、`procps`、`psmisc`、`unhide` |
| 官网 | <https://www.unhide-forensics.info> |
| 源码 | <https://salsa.debian.org/pkg-security-team/unhide> |

### unrar-nonfree

Extract files from rar archives root@kali:~# man unrar-nonfree UNRAR(1)                          RAR archiver                         UNRAR(1) NAME unrar - extract files from rar archives SYNOPSIS

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/unrar-nonfree/> |
| 版本 | 7.2.7 |
| 包 / 命令 | `libunrar-dev`、`libunrar-headers`、`libunrar5t64`、`unrar`、`unrar-nonfree` |
| 安装 | `sudo apt install unrar-nonfree` |
| 官网 | <https://www.rarlab.com/> |
| 源码 | <https://github.com/debian-calibre/unrar-nonfree> |

### vinetto

Forensics tool to examine Thumbs.db files vinetto is a console program to extract thumbnail pictures and their metadata from Thumbs.db files, that are generated under Microsoft Windows. vinetto can help *nix-based forensics investigators to: easily preview thumbnails of deleted pictures on Windows systems; obtain information (dates, path, …) about deleted pictures.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/vinetto/> |
| 版本 | 0.9.15 |
| 包 / 命令 | `vinetto` |
| 安装 | `sudo apt install vinetto` |
| 占用空间 | 234 KB |
| 依赖 | `python3`、`python3-pil`、`vinetto` |
| 官网 | <https://github.com/AtesComp/Vinetto> |
| 源码 | <https://salsa.debian.org/pkg-security-team/vinetto> |

### wce

Windows Credentials Editor Windows Credentials Editor (WCE) v1.3beta allows you to: NTLM authentication: List logon sessions and add, change, list and delete associated credentials (e.g.: LM/NT hashes) Perform pass-the-hash on Windows natively

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应、Windows 资源 |
| Kali 文档 | <https://www.kali.org/tools/wce/> |
| 版本 | 1.42 |
| 包 / 命令 | `wce` |
| 安装 | `sudo apt install wce` |
| 占用空间 | 940 KB |
| 依赖 | `kali-defaults`、`wce` |
| 官网 | <http://www.ampliasecurity.com/research.html> |
| 源码 | <https://gitlab.com/kalilinux/packages/wce> |

### winregfs

Windows registry FUSE filesystem Winregfs is a FUSE-based filesystem driver that enables accessing of Windows registry hive files as ordinary filesystems. Registry hive file editing can be performed with ordinary shell scripts and command-line tools once mounted. fsck.winregfs scans a Windows registry hive file for problems that indicate the hive has been damaged by hardware or software issues, reading recursively

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/winregfs/> |
| 版本 | 0.8 |
| 包 / 命令 | `winregfs`、`fsck.winregfs`、`mount.winregfs` |
| 安装 | `sudo apt install winregfs` |
| 占用空间 | 106 KB |
| 依赖 | `libc6`、`libfuse3-4`、`fsck.winregfs` |
| 官网 | <https://codeberg.org/jbruchon/winregfs> |
| 源码 | <https://salsa.debian.org/pkg-security-team/winregfs> |

### xmount

Tool for crossmounting between disk image formats xmount allows you to convert on-the-fly between multiple input and output harddisk image formats. xmount creates a virtual file system using FUSE (Filesystem in Userspace) that contains a virtual representation of the input image. The virtual representation can be in raw DD, Apple’s Disk Image format

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/xmount/> |
| 版本 | 1.3.1 |
| 包 / 命令 | `xmount` |
| 安装 | `sudo apt install xmount` |
| 占用空间 | 337 KB |
| 依赖 | `libafflib0t64`、`libc6`、`libewf2`、`libfuse3-4`、`zlib1g`、`xmount` |
| 官网 | <https://www.sits.lu/xmount> |
| 源码 | <https://salsa.debian.org/pkg-security-team/xmount> |

### xplico

Network Forensic Analysis Tool (NFAT) The goal of Xplico is extract from an internet traffic capture the applications data contained. For example, from a pcap file Xplico extracts each email (POP, IMAP, and SMTP protocols), all HTTP contents, each VoIP call (SIP, MGCP, H323), FTP, TFTP, and so on. Xplico is not a network protocol analyzer.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/xplico/> |
| 版本 | 1.2.2 |
| 包 / 命令 | `xplico`、`mfbc`、`mfile`、`mpaltalk`、`mwmail`、`trigcap`、`xplico-webui`、`xplico-webui-start`、`xplico-webui-stop` |
| 安装 | `sudo apt install xplico` |
| 占用空间 | 10.08 MB |
| 依赖 | `apache2`、`binfmt-support`、`kali-defaults`、`lame`、`libapache2-mod-php`、`libc6`、`libjson-c5`、`libmariadb3`、`libmaxminddb0`、`libndpi4.2t64`、`libpcap0.8t64`、`libpq5` 等 |
| 官网 | <https://www.xplico.org> |
| 源码 | <https://gitlab.com/kalilinux/packages/xplico> |

### yara

Pattern matching swiss knife for malware researchers YARA is a tool aimed at helping malware researchers to identify and classify malware samples. With YARA, it is possible to create descriptions of malware families based on textual or binary patterns contained in samples of those families. Each description consists of a set of strings and a Boolean expression which determines its logic.

| 项目 | 内容 |
|------|------|
| 归入分组 | 数字取证 |
| 全部所属分组 | 数字取证、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/yara/> |
| 版本 | 4.5.8 |
| 包 / 命令 | `libyara-dev`、`libyara10`、`yara`、`yarac`、`yara-doc` |
| 安装 | `sudo apt install yara` |
| 占用空间 | 637 KB |
| 依赖 | `libc6`、`libjansson4`、`libmagic1t64`、`libssl3t64`、`libyara10`、`yara` |
| 官网 | <https://virustotal.github.io/yara/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/yara> |
