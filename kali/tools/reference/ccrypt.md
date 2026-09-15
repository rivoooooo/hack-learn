# ccrypt

> Secure encryption and decryption of files and streams ccrypt is a utility for encrypting and decrypting files and streams. It was designed as a replacement for the standard unix crypt utility, which is notorious for using a very weak encry…

> **功能分类**：密码学与隐写 ｜ **Kali 包**：`ccrypt` ｜ **官方文档**：<https://www.kali.org/tools/ccrypt/>

## 1. 安装

```bash
sudo apt update
sudo apt install ccrypt
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.11 |
| 架构 | any |
| 可执行命令 | `ccrypt`、`ccat`、`ccdecrypt`、`ccencrypt`、`ccguess`、`elpa-ps-ccrypt` |
| 依赖 | `libc6`、`libcrypt1`、`ccat` |
| 安装体积 | 180 KB |
| 官网 | <https://ccrypt.sourceforge.net/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/ccrypt> |
| 包追踪 | <https://pkg.kali.org/pkg/ccrypt> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ccrypt -h          # 查看用法
man ccrypt         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 6 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ccat`

官方给出的调用示例：`ccat -h`

```text
root@kali:~# ccat -h
ccrypt 1.11. Secure encryption and decryption of files and streams.
Usage: ccrypt [mode] [options] [file...]
       ccencrypt [options] [file...]
       ccdecrypt [options] [file...]
       ccat [options] file...
Modes:
    -e, --encrypt         encrypt
    -d, --decrypt         decrypt
    -c, --cat             cat; decrypt files to stdout
    -x, --keychange       change key
    -u, --unixcrypt       decrypt old unix crypt files
Options:
    -h, --help            print this help message and exit
    -V, --version         print version info and exit
    -L, --license         print license info and exit
    -v, --verbose         print progress information to stderr
    -q, --quiet           run quietly; suppress warnings
    -f, --force           overwrite existing files without asking
    -m, --mismatch        allow decryption with non-matching key
    -E, --envvar var      read keyword from environment variable (unsafe)
    -K, --key key         give keyword on command line (unsafe)
    -k, --keyfile file    read keyword(s) as first line(s) from file
    -P, --prompt prompt   use this prompt instead of default
    -S, --suffix .suf     use suffix .suf instead of default .cpt
    -s, --strictsuffix    refuse to encrypt files which already have suffix
    -F, --envvar2 var     as -E for second keyword (for keychange mode)
    -H, --key2 key        as -K for second keyword (for keychange mode)
    -Q, --prompt2 prompt  as -P for second keyword (for keychange mode)
    -t, --timid           prompt twice for encryption keys (default)
    -b, --brave           prompt only once for encryption keys
    -y, --keyref file     encryption key must match this encrypted file
    -r, --recursive       recurse through directories
    -R, --rec-symlinks    follow symbolic links as subdirectories
    -l, --symlinks        dereference symbolic links
    -T, --tmpfiles        use temporary files instead of overwriting (unsafe)
    --                    end of options, filenames follow
```

### `ccdecrypt`

官方给出的调用示例：`ccdecrypt -h`

```text
root@kali:~# ccdecrypt -h
ccrypt 1.11. Secure encryption and decryption of files and streams.
Usage: ccrypt [mode] [options] [file...]
       ccencrypt [options] [file...]
       ccdecrypt [options] [file...]
       ccat [options] file...
Modes:
    -e, --encrypt         encrypt
    -d, --decrypt         decrypt
    -c, --cat             cat; decrypt files to stdout
    -x, --keychange       change key
    -u, --unixcrypt       decrypt old unix crypt files
Options:
    -h, --help            print this help message and exit
    -V, --version         print version info and exit
    -L, --license         print license info and exit
    -v, --verbose         print progress information to stderr
    -q, --quiet           run quietly; suppress warnings
    -f, --force           overwrite existing files without asking
    -m, --mismatch        allow decryption with non-matching key
    -E, --envvar var      read keyword from environment variable (unsafe)
    -K, --key key         give keyword on command line (unsafe)
    -k, --keyfile file    read keyword(s) as first line(s) from file
    -P, --prompt prompt   use this prompt instead of default
    -S, --suffix .suf     use suffix .suf instead of default .cpt
    -s, --strictsuffix    refuse to encrypt files which already have suffix
    -F, --envvar2 var     as -E for second keyword (for keychange mode)
    -H, --key2 key        as -K for second keyword (for keychange mode)
    -Q, --prompt2 prompt  as -P for second keyword (for keychange mode)
    -t, --timid           prompt twice for encryption keys (default)
    -b, --brave           prompt only once for encryption keys
    -y, --keyref file     encryption key must match this encrypted file
    -r, --recursive       recurse through directories
    -R, --rec-symlinks    follow symbolic links as subdirectories
    -l, --symlinks        dereference symbolic links
    -T, --tmpfiles        use temporary files instead of overwriting (unsafe)
    --                    end of options, filenames follow
```

### `ccencrypt`

官方给出的调用示例：`ccencrypt -h`

```text
root@kali:~# ccencrypt -h
ccrypt 1.11. Secure encryption and decryption of files and streams.
Usage: ccrypt [mode] [options] [file...]
       ccencrypt [options] [file...]
       ccdecrypt [options] [file...]
       ccat [options] file...
Modes:
    -e, --encrypt         encrypt
    -d, --decrypt         decrypt
    -c, --cat             cat; decrypt files to stdout
    -x, --keychange       change key
    -u, --unixcrypt       decrypt old unix crypt files
Options:
    -h, --help            print this help message and exit
    -V, --version         print version info and exit
    -L, --license         print license info and exit
    -v, --verbose         print progress information to stderr
    -q, --quiet           run quietly; suppress warnings
    -f, --force           overwrite existing files without asking
    -m, --mismatch        allow decryption with non-matching key
    -E, --envvar var      read keyword from environment variable (unsafe)
    -K, --key key         give keyword on command line (unsafe)
    -k, --keyfile file    read keyword(s) as first line(s) from file
    -P, --prompt prompt   use this prompt instead of default
    -S, --suffix .suf     use suffix .suf instead of default .cpt
    -s, --strictsuffix    refuse to encrypt files which already have suffix
    -F, --envvar2 var     as -E for second keyword (for keychange mode)
    -H, --key2 key        as -K for second keyword (for keychange mode)
    -Q, --prompt2 prompt  as -P for second keyword (for keychange mode)
    -t, --timid           prompt twice for encryption keys (default)
    -b, --brave           prompt only once for encryption keys
    -y, --keyref file     encryption key must match this encrypted file
    -r, --recursive       recurse through directories
    -R, --rec-symlinks    follow symbolic links as subdirectories
    -l, --symlinks        dereference symbolic links
    -T, --tmpfiles        use temporary files instead of overwriting (unsafe)
    --                    end of options, filenames follow
```

### `ccguess`

官方给出的调用示例：`ccguess -h`

```text
root@kali:~# ccguess -h
ccguess 1.11. Search for ccrypt encryption keys.
Usage: ccguess [options] file...
Options:
    -h, --help              print this help message and exit
    -V, --version           print version info and exit
    -L, --license           print license info and exit
    -K, --key <key>         specify approximate key
    -d, --depth             try up to this many changes to key (default: 5)
    -c, --continue          keep trying more keys after first match
    -n, --non-printable     allow non-printable characters in keys
    -t, --chartable <chars> characters to use in passwords (default: printable)
Arguments:
    file...               files to read encrypted data from, or '-' for stdin
```

### `ccrypt`

官方给出的调用示例：`ccrypt -h`

```text
root@kali:~# ccrypt -h
ccrypt 1.11. Secure encryption and decryption of files and streams.
Usage: ccrypt [mode] [options] [file...]
       ccencrypt [options] [file...]
       ccdecrypt [options] [file...]
       ccat [options] file...
Modes:
    -e, --encrypt         encrypt
    -d, --decrypt         decrypt
    -c, --cat             cat; decrypt files to stdout
    -x, --keychange       change key
    -u, --unixcrypt       decrypt old unix crypt files
Options:
    -h, --help            print this help message and exit
    -V, --version         print version info and exit
    -L, --license         print license info and exit
    -v, --verbose         print progress information to stderr
    -q, --quiet           run quietly; suppress warnings
    -f, --force           overwrite existing files without asking
    -m, --mismatch        allow decryption with non-matching key
    -E, --envvar var      read keyword from environment variable (unsafe)
    -K, --key key         give keyword on command line (unsafe)
    -k, --keyfile file    read keyword(s) as first line(s) from file
    -P, --prompt prompt   use this prompt instead of default
    -S, --suffix .suf     use suffix .suf instead of default .cpt
    -s, --strictsuffix    refuse to encrypt files which already have suffix
    -F, --envvar2 var     as -E for second keyword (for keychange mode)
    -H, --key2 key        as -K for second keyword (for keychange mode)
    -Q, --prompt2 prompt  as -P for second keyword (for keychange mode)
    -t, --timid           prompt twice for encryption keys (default)
    -b, --brave           prompt only once for encryption keys
    -y, --keyref file     encryption key must match this encrypted file
    -r, --recursive       recurse through directories
    -R, --rec-symlinks    follow symbolic links as subdirectories
    -l, --symlinks        dereference symbolic links
    -T, --tmpfiles        use temporary files instead of overwriting (unsafe)
    --                    end of options, filenames follow
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install ccrypt`，再执行 `ccrypt --version` 2>/dev/null || `ccrypt -V`
- [ ] **2.** **读官方帮助** —— `ccrypt -h`，需要细节时 `man ccrypt`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ccrypt [mode] [options] [file...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ccrypt/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ccrypt/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ccrypt/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
