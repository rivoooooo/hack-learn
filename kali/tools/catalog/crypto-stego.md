# 按包速查：密码学与隐写（crypto-stego）

> 共 **6** 个包 · 数据来源 <https://www.kali.org/tools/all-tools/>

返回 [工具总览](../index.md) · [全量清单](all-tools.md) · [按功能分类](../index.md#功能分类导航)

---

### aesfix

Tool for correcting bit errors in an AES key schedule This program illustrates a technique for correcting bit errors in an AES key schedule. It should be used with the output of the aeskeyfind program. It is limited to AES-128 key schedules, and it can only correct unidirectional 1->0 bit errors. For the most part it has been optimized for readability rather than performance.

| 项目 | 内容 |
|------|------|
| 归入分组 | 密码学与隐写 |
| Kali 文档 | <https://www.kali.org/tools/aesfix/> |
| 版本 | 1.0.1 |
| 包 / 命令 | `aesfix` |
| 安装 | `sudo apt install aesfix` |
| 占用空间 | 41 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6`、`aesfix` |
| 官网 | <https://citp.princeton.edu/our-work/memory/code/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/aesfix> |

### aeskeyfind

Tool for locating AES keys in a captured memory image This program illustrates automatic techniques for locating 128-bit and 256-bit AES keys in a captured memory image. The program uses various algorithms and also performs a simple entropy test to filter out blocks that are not keys. It counts the number of repeated bytes and skips blocks that have too many repeats.

| 项目 | 内容 |
|------|------|
| 归入分组 | 密码学与隐写 |
| Kali 文档 | <https://www.kali.org/tools/aeskeyfind/> |
| 版本 | 1.0 |
| 包 / 命令 | `aeskeyfind` |
| 安装 | `sudo apt install aeskeyfind` |
| 占用空间 | 33 KB |
| 依赖 | `libc6`、`aeskeyfind` |
| 官网 | <https://citp.princeton.edu/our-work/memory/code/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/aeskeyfind> |

### ccrypt

Secure encryption and decryption of files and streams ccrypt is a utility for encrypting and decrypting files and streams. It was designed as a replacement for the standard unix crypt utility, which is notorious for using a very weak encryption algorithm. ccrypt is based on the Rijndael cipher, which is the U.S. government’s chosen candidate for the Advanced Encryption Standard (AES, see

| 项目 | 内容 |
|------|------|
| 归入分组 | 密码学与隐写 |
| Kali 文档 | <https://www.kali.org/tools/ccrypt/> |
| 版本 | 1.11 |
| 包 / 命令 | `ccrypt`、`ccat`、`ccdecrypt`、`ccencrypt`、`ccguess`、`elpa-ps-ccrypt` |
| 安装 | `sudo apt install ccrypt` |
| 占用空间 | 180 KB |
| 依赖 | `libc6`、`libcrypt1`、`ccat` |
| 官网 | <https://ccrypt.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/ccrypt> |

### steghide

Steganography hiding tool Steghide is steganography program which hides bits of a data file in some of the least significant bits of another file in such a way that the existence of the data file is not visible and cannot be proven. Steghide is designed to be portable and configurable and features hiding data in bmp, jpeg, wav and au files, blowfish encryption, MD5 hashing of

| 项目 | 内容 |
|------|------|
| 归入分组 | 密码学与隐写 |
| Kali 文档 | <https://www.kali.org/tools/steghide/> |
| 版本 | 0.5.1 |
| 包 / 命令 | `steghide`、`steghide-doc` |
| 安装 | `sudo apt install steghide` |
| 占用空间 | 525 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libjpeg62-turbo`、`libmcrypt4`、`libmhash2`、`libstdc++6`、`zlib1g`、`steghide` |
| 官网 | <https://steghide.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/steghide> |

### stegosuite

Steganography tool to hide information in image files Stegosuite is a graphical steganography tool to easily hide information in image files. It allows the embedding of text messages and multiple files of any type. In addition, the embedded data is encrypted using AES. Currently supported file types are BMP, GIF, JPG and PNG. Stegosuite is written in Java and utilizes the SWT toolkit for its interface.

| 项目 | 内容 |
|------|------|
| 归入分组 | 密码学与隐写 |
| Kali 文档 | <https://www.kali.org/tools/stegosuite/> |
| 版本 | 0.9.0 |
| 包 / 命令 | `stegosuite` |
| 安装 | `sudo apt install stegosuite` |
| 占用空间 | 279 KB |
| 官网 | <https://codeberg.org/tob/stegosuite> |
| 源码 | <https://salsa.debian.org/java-team/stegosuite> |

### stegsnow

Steganography using ASCII files This utility can conceal messages in ASCII text by appending whitespaces to the end of lines. Because spaces and tabs are generally not visible in text viewers, the message is effectively hidden from casual observers. And if the built-in encryption is used, the message cannot be read even if it is detected. About the name: locating trailing whitespace in text is like finding a polar

| 项目 | 内容 |
|------|------|
| 归入分组 | 密码学与隐写 |
| Kali 文档 | <https://www.kali.org/tools/stegsnow/> |
| 版本 | 20130616 |
| 包 / 命令 | `stegsnow` |
| 安装 | `sudo apt install stegsnow` |
| 占用空间 | 56 KB |
| 依赖 | `libc6`、`stegsnow` |
| 官网 | <https://www.darkside.com.au/snow> |
| 源码 | <https://salsa.debian.org/pkg-security-team/stegsnow> |
