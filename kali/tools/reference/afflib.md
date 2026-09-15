# afflib

> Advanced Forensics Format Library (utilities) The Advanced Forensic Format (AFF) is on-disk format for storing computer forensic information. Critical features of AFF include: AFF allows you to store both computer forensic data and associa…

> **功能分类**：数字取证 ｜ **Kali 包**：`afflib` ｜ **官方文档**：<https://www.kali.org/tools/afflib/>

## 1. 安装

```bash
sudo apt update
sudo apt install afflib-tools
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.7.22 |
| 架构 | any |
| 可执行命令 | `afflib-tools`、`affcat`、`affcompare`、`affconvert`、`affcopy`、`affcrypto`、`affdiskprint`、`affinfo`、`affix`、`affrecover`、`affsegment`、`affsign`、`affstats`、`affuse`、`affverify`、`affxml`、`libafflib-dev`、`libafflib0t64` |
| 依赖 | `libafflib0t64`、`libc6`、`libexpat1`、`libfuse3-4`、`libgcc-s1`、`libssl3t64`、`libstdc++6`、`affcat` |
| 安装体积 | 624 KB |
| 官网 | <https://github.com/sshock/AFFLIBv3> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/afflib> |
| 包追踪 | <https://pkg.kali.org/pkg/afflib> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
afflib-tools -h          # 查看用法
man afflib-tools         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 18 个可执行命令，下面是官方页面内嵌的帮助原文。

### `affcat`

> 官方示例调用：`affcat -h`

```text
root@kali:~# affcat -h
affcat version 3.7.22
usage: affcat [options] infile [... more infiles]
options:
    -s name --- Just output segment name
    -p ###  --- just output data page number ###
    -S ###  --- Just output data sector ### (assumes 512-byte sectors). Sector #0 is first
    -q      --- quiet; don't print to STDERR if a page is skipped
    -n      --- noisy; tell when pages are skipped.
    -l      --- List all of the segment names
    -L      --- List segment names, lengths, and args
    -d      --- debug. Print the page numbers to stderr as data goes to stdout
    -b      --- Output BADFALG for bad blocks (default is NULLs)
    -v      --- Just print the version number and exit.
    -r offset:count --- seek to offset and output count characters in each file; may be repeated
```

### `affcompare`

> 官方示例调用：`affcompare -h`

```text
root@kali:~# affcompare -h
affcompare version 3.7.22
usage: affcompare [options] file1 file2
       compares file1 with file2
or     affcompare [options] -r dir1 dir2
       compares similarly-named files in dir1 and dir2
or     affcompare [options] -s file1 file2...
       Reports if file was successfully copied to Amazon S3
       checking only for existence, not reading back the bytes.
       (Because all writes to S3 are validated by the MD5 of the object
fast options:
(These compare segments but not their contents.)
       -p        --- report about the results of preening
       -e        --- Just report about existence (use with -r)
       -s        --- Just see if all of the segments are present, but don't
                     validate the contents. (Primarily for use with Amazon S3)
other options:
       -V        --- just print the version number and exit
       -v        --- Verbose; each file as it is compared.
       -q        --- Quiet. No output except for errors
       -a        --- print what's the same (all)
       -b        --- print the numbers of differing sectors
       -c        --- print the contents of differing sectors
       -m        --- Just report about the data (ignore metadata)
       -P ###    --- Just examine the differences on page ###
Options documented above:
       -r dir1 dir2 --- recursively compare what's in dir1 with dir2, and
                       report what's in dir1 that's not in dir2
       -s        --- Check to see if named files are on Amazon S3
  affcompare file1.aff file2.aff           --- compare file1.aff and file2.aff
  affcompare f1.aff f2.aff dir1/           --- compare f1.aff with dir1/f1.aff and f2.aff with dir2/f2.aff
                                              note: dir1/ must end with a slash.
  affcompare -b img file.aff               --- compare file.aff and file.img
  affcompare -b img file1.aff file2.aff... --- compare file1.aff, file1.img, etc.
  affcompare -re dir1 dir2                --- report AFF files in dir1 but not in dir2
  affcompare -rse dir1 s3:///             --- report AFF files in dir1 but not on S3 (low bandwidth)
  affcompare -rs dir1 s3:///              --- report AFF files in dir1 but incomplete on on S3 (more bandwidth)
```

### `affconvert`

> 官方示例调用：`affconvert -h`

```text
root@kali:~# affconvert -h
affconvert version 3.7.22
usage:   affconvert [options] file1 [... files]
Please, see more info in manpage.
```

### `affcopy`

> 官方示例调用：`affcopy -h`

```text
root@kali:~# affcopy -h
affcopy version 3.7.22
usage: affcopy [options] file1 file
                    Copies file1 to file2
       affcopy [options] file1 file2 file3 ... dir
                    Copies file1.. into dir
       affcopy [options] file1 file2 file3 ... dir1 dir2...
                    Copies file1.. into dirs1, dir2, ...
By default, all page MACs are verified on read and all segments
are verified after write.
Options:
   -v = verbose: print each file as it is copied
   -vv = very verbose: print each segment as it is copied
   -d = print debugging information as well
   -x = don't verify hashes on reads
   -y = don't verify writes
   -Xn = recompress pages (preen) with zlib level n
   -L  = recompress pages (preen) with LZMA (smaller but slower)
   -h = help; print this message.
   -V = print the program version and exit.
   -z = zap; copy even if the destination exists.
   -m = just copy the missing segments
Signature Options:
   -k filename.key   = specify private key for signing
   -c filename.cer   = specify a X.509 certificate that matches the private key
                       (by default, the file is assumed to be the same one
                       provided with the -k option.)
   -n  = read notes to accompany the copy from standard in.
Encryption Options:   Specify passphrase encryption for filename.aff with:
      file://:passphrase@/filename.aff
Examples:
       affcopy  file.aff   file://:mypassword@/file-encrypted.aff   - encrypt file.aff
       affcopy -vy -X9 *.aff s3:///     Copy all files in current
                               directory to S3 default bucket with X9 compression
```

### `affcrypto`

> 官方示例调用：`affcrypto -h`

```text
root@kali:~# affcrypto -h
affcrypto version 3.7.22
usage: affcrypto [options] filename.aff [filename2.aff ... ]
   prints if each file is encrypted or not.
options:
    -x      --- output in XML
    -j      --- Just print the number of encrypted segments
    -J      --- Just print the number of unencrypted segments
Data conversion options:
    -e      --- encrypt the unencrypted non-signature segments
    -d      --- decrypt the encrypted non-signature segments
    -r      --- change passphrase (take old and new from stdin)
    -O old  --- specify old passphrase
    -N new  --- specify new passphrase
    -K mykey.key  -- specifies a private keyfile for unsealing (may not be repeated)
    -C mycert.crt -- specifies a certificate file for sealing (may be repeated)
    -S      --- add symmetric encryptiong (passphrase) to AFFILE encrypted with public key
                    (requires a private key and a specified passphrase).
    -A      --- add asymmetric encryption to a AFFILE encrypted with a passphrase
                    (requires a certificate file spcified with the -C option
Password Cracking Options:
    -p passphrase --- checks to see if passphrase is the passphrase of the file
                exit code is 0 if it is, -1 if it is not
    -k      --- attempt to crack passwords by reading a list of passwords from ~/.affpassphrase
    -f file --- Crack passwords but read them from file.
Debugging:
    -V      --- Just print the version number and exit.
    -D      --- debug; print out each key as it is tried
    -l      --- List the installed hash and encryption algorithms
Note: This program ignores the environment variables:
AFFLIB_PASSPHRASE
AFFLIB_PASSPHRASE_FILE
AFFLIB_PASSPHRASE_FD
AFFLIB_DECRYPTING_PRIVATE_KEYFILE
```

### `affdiskprint`

> 官方示例调用：`affdiskprint -h`

```text
root@kali:~# affdiskprint -h
affdiskprint version 3.7.22
usage: affdiskprint [options] infile
   -x XML     =   Verify the diskprint
   -V         =   Just print the version number and exit.
   -h         =   Print this help.
```

### `affinfo`

> 官方示例调用：`affinfo -h`

```text
root@kali:~# affinfo -h
affinfo version 3.7.22
usage: affinfo [options] infile
   -a = print ALL segments (normally data segments are suppressed)
   -b = print how many bad blocks in each segment (implies -a)
   -i = identify the files, don't do info on them.
   -w = wide output; print more than 1 line if necessary.
   -s segment =   Just print information about 'segment'.
                    (may be repeated)
   -m = validate MD5 hash of entire image
   -S = validate SHA1 hash of entire image
   -v = validate the hash of each page (if present)
   -y = don't print segments of lengths 16 and 20 as hex)
   -p<passphrase> = Specify <passphrase> to decrypt file
   -l = Just print the segment names and exit
   -V = Just print the version number and exit.
Preview Options:
   -X = no data preview; just print the segment names
   -x = print binary values in hex (default is ASCII)
Misc:
   -d = debug
   -A = if infile is a device, print the number of sectors
        and sector size to stdout in XML. Otherwise error
Compilation:
    LZMA compression: Enabled
    QEMU enabled
    FUSE enabled
    Amazon S3 enabled
    HAVE_LIBEXPAT
```

### `affix`

> 官方示例调用：`affix -h`

```text
root@kali:~# affix -h
usage: affix [options] file1 [...]
  -y = Actually modify the files; normally just reports the problems
  -v = Just print the version number and exit.
```

### `affrecover`

> 官方示例调用：`affrecover -h`

```text
root@kali:~# affrecover -h
usage: affrecover filename
```

### `affsegment`

> 官方示例调用：`affsegment -h`

```text
root@kali:~# affsegment -h
affsegment version 3.7.22
usage: affsegment [options] file1.aff [file2.aff ...]
options:
    -c              Create AFF files if they do not exist
    -ssegval        Sets the value of a segment; may be repeated
    -psegname       Prints the contents of the segment name for each file
    -V              Just print the version number and exit.
    -dname          Delete segment 'name'
    -h, -?          Print this message
    -Q              interpert 8-byte segments as a 64-bit value
    -A              Print the 32-bit arg, not the segment value
    -x              Print the segment as a hex string
Values for segval:
Setting the segment values:
    -sname=-        Take the new value of segment 'name' from stdin
    -sname=val      Sets segment 'name' to be 'val'
    -sname=<val     Sets segment 'name' to be contents of file 'val'
Setting the segment args:
    -sname/arg       Sets segment 'name' arg to be 'arg'  (may be repeated)
Setting both the segment value and the arg:
    -sname/arg=val   Sets both arg and val for segment 'name'
    -sname/arg=<file Sets the arg and take contents from file 'file'
    -sname/arg=-     Sets the arg of segment 'name' and take the contents from stdin
Note: All deletions are done first, then all updates. Don't specify the
same segment twice on one command line.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install afflib-tools`，再执行 `afflib-tools --version` 2>/dev/null || `afflib-tools -V`
- [ ] **2.** **读官方帮助** —— `afflib-tools -h`，需要细节时 `man afflib-tools`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `afflib-tools -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/afflib/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/afflib/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/afflib/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
