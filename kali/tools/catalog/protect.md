# 按包速查：防护（protect）

> 共 **4** 个包 · 数据来源 <https://www.kali.org/tools/all-tools/>

返回 [工具总览](../index.md) · [全量清单](all-tools.md) · [按功能分类](../index.md#功能分类导航)

---

### clamav

Anti-virus utility for Unix - command-line interface Clam AntiVirus is an anti-virus toolkit for Unix. The main purpose of this software is the integration with mail servers (attachment scanning). The package provides a flexible and scalable multi-threaded daemon in the clamav-daemon package, a command-line scanner in the clamav package, and a tool for automatic updating via

| 项目 | 内容 |
|------|------|
| 归入分组 | 防护 |
| Kali 文档 | <https://www.kali.org/tools/clamav/> |
| 版本 | 1.4.6 |
| 包 / 命令 | `clamav`、`clambc`、`clamscan`、`clamsubmit`、`sigtool`、`clamav-base`、`clamav-daemon`、`clamconf`、`clamd`、`clamdtop`、`clamonacc`、`clamav-doc`、`clamav-docs`、`clamav-freshclam`、`freshclam`、`clamav-milter`、`clamav-testfiles`、`clamdscan`、`libclamav-dev`、`clamav-config`、`libclamav12` |
| 安装 | `sudo apt install clamav` |
| 占用空间 | 19.41 MB |
| 官网 | <https://www.clamav.net/> |
| 源码 | <https://salsa.debian.org/clamav-team/clamav> |

### cryptsetup

Disk encryption support - startup scripts Cryptsetup provides an interface for configuring encryption on block devices (such as /home or swap partitions), using the Linux kernel device mapper target dm-crypt. It features integrated Linux Unified Key Setup (LUKS) support. Cryptsetup is backwards compatible with the on-disk format of cryptoloop,

| 项目 | 内容 |
|------|------|
| 归入分组 | 防护 |
| Kali 文档 | <https://www.kali.org/tools/cryptsetup/> |
| 版本 | 2.8.7 |
| 包 / 命令 | `cryptsetup`、`cryptdisks_start`、`cryptdisks_stop`、`luksformat`、`cryptsetup-bin`、`integritysetup`、`veritysetup`、`cryptsetup-initramfs`、`cryptsetup-ssh`、`cryptsetup-suspend`、`cryptsetup-udeb`、`libcryptsetup-dev`、`libcryptsetup12`、`libcryptsetup12-udeb` |
| 安装 | `sudo apt install cryptsetup` |
| 占用空间 | 465 KB |
| 依赖 | `cryptsetup-bin` |
| 官网 | <https://gitlab.com/cryptsetup/cryptsetup> |
| 源码 | <https://salsa.debian.org/cryptsetup-team/cryptsetup> |

### cryptsetup-nuke-password

Erase the LUKS keys with a special password on the unlock prompt Installing this package lets you configure a special “nuke password” that can be used to destroy the encryption keys required to unlock the encrypted partitions. This password can be entered in the usual early-boot prompt asking the passphrase to unlock the encrypted partition(s). This provides a relatively stealth way to make your data unreadable in

| 项目 | 内容 |
|------|------|
| 归入分组 | 防护 |
| Kali 文档 | <https://www.kali.org/tools/cryptsetup-nuke-password/> |
| 版本 | 9 |
| 包 / 命令 | `cryptsetup-nuke-password` |
| 安装 | `sudo apt install cryptsetup-nuke-password` |
| 占用空间 | 69 KB |
| 依赖 | `cryptsetup` |
| 官网 | <https://salsa.debian.org/pkg-security-team/cryptsetup-nuke-password> |
| 源码 | <https://salsa.debian.org/pkg-security-team/cryptsetup-nuke-password> |

### fwbuilder

Firewall administration tool GUI Firewall Builder consists of an object-oriented GUI and a set of policy compilers for various firewall platforms. In Firewall Builder, firewall policy is a set of rules, each rule consists of abstract objects which represent real network objects and services (hosts, routers, firewalls, networks, protocols). Firewall Builder helps the user maintain a database

| 项目 | 内容 |
|------|------|
| 归入分组 | 防护 |
| Kali 文档 | <https://www.kali.org/tools/fwbuilder/> |
| 版本 | 5.3.7 |
| 包 / 命令 | `fwbuilder`、`fwb_compile_all`、`fwb_iosacl`、`fwb_ipf`、`fwb_ipfw`、`fwb_ipt`、`fwb_pf`、`fwb_pix`、`fwb_procurve_acl`、`fwbedit`、`fwbuilder-common`、`fwbuilder-doc` |
| 安装 | `sudo apt install fwbuilder` |
| 占用空间 | 39.82 MB |
| 依赖 | `fwbuilder-common`、`libc6`、`libgcc-s1`、`libqt5core5t64` |
| 官网 | <https://github.com/fwbuilder/fwbuilder/> |
| 源码 | <https://salsa.debian.org/debian/fwbuilder> |
