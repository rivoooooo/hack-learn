# clamav

> Anti-virus utility for Unix - command-line interface Clam AntiVirus is an anti-virus toolkit for Unix. The main purpose of this software is the integration with mail servers (attachment scanning). The package provides a flexible and scalab…

> **功能分类**：防护 ｜ **Kali 包**：`clamav` ｜ **官方文档**：<https://www.kali.org/tools/clamav/>

## 1. 安装

```bash
sudo apt update
sudo apt install clamav
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.4.6 |
| 架构 | any |
| 可执行命令 | `clamav`、`clambc`、`clamscan`、`clamsubmit`、`sigtool`、`clamav-base`、`clamav-daemon`、`clamconf`、`clamd`、`clamdtop`、`clamonacc`、`clamav-doc`、`clamav-docs`、`clamav-freshclam`、`freshclam`、`clamav-milter`、`clamav-testfiles`、`clamdscan`、`libclamav-dev`、`clamav-config`、`libclamav12` |
| 安装体积 | 19.41 MB |
| 官网 | <https://www.clamav.net/> |
| 源码仓库 | <https://salsa.debian.org/clamav-team/clamav> |
| 包追踪 | <https://pkg.kali.org/pkg/clamav> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
clamav -h          # 查看用法
man clamav         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 21 个可执行命令，下面是官方页面内嵌的帮助原文。

### `clambc`

> 官方示例调用：`clambc -h`

```text
root@kali:~# clambc -h
                       Clam AntiVirus: Bytecode Testing Tool 1.4.6
           By The ClamAV Team: https://www.clamav.net/about.html#credits
           (C) 2024 Cisco Systems, Inc.
    clambc <file> [function] [param1 ...]
    --help                 -h         Show this help
    --version              -V         Show version
    --debug                           Show debug
    --force-interpreter    -f         Force using the interpreter instead of the JIT
    --trust-bytecode       -t         Trust loaded bytecode (default yes)
    --info                 -i         Print information about bytecode
    --printsrc             -p         Print bytecode source
    --printbcir            -c         Print IR of bytecode signature
    --input                -c         Input file to run the bytecode on
    --trace <level>        -T         Set bytecode trace level 0..7 (default 7)
    --no-trace-showsource  -s         Don't show source line during tracing
    --statistics=bytecode             Collect and print bytecode execution statistics
    file                              File to test
**Caution**: You should NEVER run bytecode signatures from untrusted sources.
Doing so may result in arbitrary code execution.
```

### `clamscan`

> 官方示例调用：`clamscan -h`

```text
root@kali:~# clamscan -h
                       Clam AntiVirus: Scanner 1.4.6
           By The ClamAV Team: https://www.clamav.net/about.html#credits
           (C) 2024 Cisco Systems, Inc.
    clamscan [options] [file/directory/-]
    --help                -h             Show this help
    --version             -V             Print version number
    --verbose             -v             Be verbose
    --archive-verbose     -a             Show filenames inside scanned archives
    --debug                              Enable libclamav's debug messages
    --quiet                              Only output error messages
    --stdout                             Write to stdout instead of stderr. Does not affect 'debug' messages.
    --no-summary                         Disable summary at end of scanning
    --infected            -i             Only print infected files
    --suppress-ok-results -o             Skip printing OK files
    --bell                               Sound bell on virus detection
    --tempdir=DIRECTORY                  Create temporary files in DIRECTORY
    --leave-temps[=yes/no(*)]            Do not remove temporary files
    --force-to-disk[=yes/no(*)]          Create temporary files for nested file scans that would otherwise be in-memory only
    --gen-json[=yes/no(*)]               Generate JSON metadata for the scanned file(s). For testing & development use ONLY.
                                         JSON will be printed if --debug is enabled.
                                         A JSON file will dropped to the temp directory if --leave-temps is enabled.
    --database=FILE/DIR   -d FILE/DIR    Load virus database from FILE or load all supported db files from DIR
    --official-db-only[=yes/no(*)]       Only load official signatures
    --fail-if-cvd-older-than=days        Return with a nonzero error code if virus database outdated.
    --log=FILE            -l FILE        Save scan report to FILE
    --recursive[=yes/no(*)]  -r          Scan subdirectories recursively
    --allmatch[=yes/no(*)]   -z          Continue scanning within file after finding a match
    --cross-fs[=yes(*)/no]               Scan files and directories on other filesystems
    --follow-dir-symlinks[=0/1(*)/2]     Follow directory symlinks (0 = never, 1 = direct, 2 = always)
    --follow-file-symlinks[=0/1(*)/2]    Follow file symlinks (0 = never, 1 = direct, 2 = always)
    --file-list=FILE      -f FILE        Scan files from FILE
    --remove[=yes/no(*)]                 Remove infected files. Be careful!
    --move=DIRECTORY                     Move infected files into DIRECTORY
    --copy=DIRECTORY                     Copy infected files into DIRECTORY
    --exclude=REGEX                      Don't scan file names matching REGEX
    --exclude-dir=REGEX                  Don't scan directories matching REGEX
    --include=REGEX                      Only scan file names matching REGEX
    --include-dir=REGEX                  Only scan directories matching REGEX
    --bytecode[=yes(*)/no]               Load bytecode from the database
    --bytecode-unsigned[=yes/no(*)]      Load unsigned bytecode
                                         **Caution**: You should NEVER run bytecode signatures from untrusted sources.
                                         Doing so may result in arbitrary code execution.
    --bytecode-timeout=N                 Set bytecode timeout (in milliseconds)
    --statistics[=none(*)/bytecode/pcre] Collect and print execution statistics
    --detect-pua[=yes/no(*)]             Detect Possibly Unwanted Applications
    --exclude-pua=CAT                    Skip PUA sigs of category CAT
    --include-pua=CAT                    Load PUA sigs of category CAT
    --detect-structured[=yes/no(*)]      Detect structured data (SSN, Credit Card)
    --structured-ssn-format=X            SSN format (0=normal,1=stripped,2=both)
    --structured-ssn-count=N             Min SSN count to generate a detect
    --structured-cc-count=N              Min CC count to generate a detect
    --structured-cc-mode=X               CC mode (0=credit debit and private label, 1=credit cards only
    --scan-mail[=yes(*)/no]              Scan mail files
    --phishing-sigs[=yes(*)/no]          Enable email signature-based phishing detection
    --phishing-scan-urls[=yes(*)/no]     Enable URL signature-based phishing detection
    --heuristic-alerts[=yes(*)/no]       Heuristic alerts
    --heuristic-scan-precedence[=yes/no(*)] Stop scanning as soon as a heuristic match is found
    --normalize[=yes(*)/no]              Normalize html, script, and text files. Use normalize=no for yara compatibility
    --scan-pe[=yes(*)/no]                Scan PE files
    --scan-elf[=yes(*)/no]               Scan ELF files
    --scan-ole2[=yes(*)/no]              Scan OLE2 containers
    --scan-pdf[=yes(*)/no]               Scan PDF files
    --scan-swf[=yes(*)/no]               Scan SWF files
    --scan-html[=yes(*)/no]              Scan HTML files
    --scan-xmldocs[=yes(*)/no]           Scan xml-based document files
    --scan-hwp3[=yes(*)/no]              Scan HWP3 files
    --scan-onenote[=yes(*)/no]           Scan OneNote files
    --scan-archive[=yes(*)/no]           Scan archive files (supported by libclamav)
    --scan-image[=yes(*)/no]             Scan image (graphics) files
    --scan-image-fuzzy-hash[=yes(*)/no]  Detect files by calculating image (graphics) fuzzy hashes
    --alert-broken[=yes/no(*)]           Alert on broken executable files (PE & ELF)
    --alert-broken-media[=yes/no(*)]     Alert on broken graphics files (JPEG, TIFF, PNG, GIF)
    --alert-encrypted[=yes/no(*)]        Alert on encrypted archives and documents
    --alert-encrypted-archive[=yes/no(*)] Alert on encrypted archives
    --alert-encrypted-doc[=yes/no(*)]    Alert on encrypted documents
    --alert-macros[=yes/no(*)]           Alert on OLE2 files containing VBA macros
    --alert-exceeds-max[=yes/no(*)]      Alert on files that exceed max file size, max scan size, or max recursion limit
    --alert-phishing-ssl[=yes/no(*)]     Alert on emails containing SSL mismatches in URLs
    --alert-phishing-cloak[=yes/no(*)]   Alert on emails containing cloaked URLs
    --alert-partition-intersection[=yes/no(*)] Alert on raw DMG image files containing partition intersections
    --nocerts                            Disable authenticode certificate chain verification in PE files
    --dumpcerts                          Dump authenticode certificate chain in PE files
    --max-scantime=#n                    Scan time longer than this will be skipped and assumed clean (milliseconds)
    --max-filesize=#n                    Files larger than this will be skipped and assumed clean
    --max-scansize=#n                    The maximum amount of data to scan for each container file (**)
    --max-files=#n                       The maximum number of files to scan for each container file (**)
    --max-recursion=#n                   Maximum archive recursion level for container file (**)
    --max-dir-recursion=#n               Maximum directory recursion level
    --max-embeddedpe=#n                  Maximum size file to check for embedded PE
    --max-htmlnormalize=#n               Maximum size of HTML file to normalize
    --max-htmlnotags=#n                  Maximum size of normalized HTML file to scan
    --max-scriptnormalize=#n             Maximum size of script file to normalize
    --max-ziptypercg=#n                  Maximum size zip to type reanalyze
    --max-partitions=#n                  Maximum number of partitions in disk image to be scanned
    --max-iconspe=#n                     Maximum number of icons in PE file to be scanned
    --max-rechwp3=#n                     Maximum recursive calls to HWP3 parsing function
    --pcre-match-limit=#n                Maximum calls to the PCRE match function.
    --pcre-recmatch-limit=#n             Maximum recursive calls to the PCRE match function.
    --pcre-max-filesize=#n               Maximum size file to perform PCRE subsig matching.
    --disable-cache                      Disable caching and cache checks for hash sums of scanned files.
Pass in - as the filename for stdin.
(*) Default scan settings
(**) Certain files (e.g. documents, archives, etc.) may in turn contain other
   files inside. The above options ensure safe processing of this kind of data.
```

### `clamsubmit`

> 官方示例调用：`clamsubmit -h`

```text
root@kali:~# clamsubmit -h
                       Clam AntiVirus: Malware and False Positive Reporting Tool 1.4.6
           By The ClamAV Team: https://www.clamav.net/about.html#credits
           (C) 2024 Cisco Systems, Inc.
    clamsubmit -hHinpVvd?
    -h or -?                  Show this help
    -v                        Show version
    -e [EMAIL]                Your email address (required)
    -n [FILE/-]               Submit a false negative (FN)
    -N [NAME]                 Your name contained in quotation marks (required)
    -p [FILE/-]               Submit a false positive (FP)
    -V [VIRUS]                Detected virus name (required with -p)
    -d                        Enable debug output
You must specify -n or -p. Both are mutually exclusive. Pass in - as the filename for stdin.
```

### `sigtool`

> 官方示例调用：`sigtool -h`

```text
root@kali:~# sigtool -h
                      Clam AntiVirus: Signature Tool 1.4.6
           By The ClamAV Team: https://www.clamav.net/about.html#credits
           (C) 2024 Cisco Systems, Inc.
    sigtool [options]
    --help                 -h              Show this help
    --version              -V              Print version number and exit
    --quiet                                Be quiet, output only error messages
    --debug                                Enable debug messages
    --stdout                               Write to stdout instead of stderr. Does not affect 'debug' messages.
    --hex-dump                             Convert data from stdin to a hex
                                           string and print it on stdout
    --md5 [FILES]                          Generate MD5 checksum from stdin
                                           or MD5 sigs for FILES
    --sha1 [FILES]                         Generate SHA1 checksum from stdin
                                           or SHA1 sigs for FILES
    --sha256 [FILES]                       Generate SHA256 checksum from stdin
                                           or SHA256 sigs for FILES
    --mdb [FILES]                          Generate .mdb (section hash) sigs
    --imp [FILES]                          Generate .imp (import table hash) sigs
    --fuzzy-img FILE(S)                    Generate image fuzzy hash for each file
    --html-normalise=FILE                  Create normalised parts of HTML file
    --ascii-normalise=FILE                 Create normalised text file from ascii source
    --utf16-decode=FILE                    Decode UTF16 encoded files
    --info=FILE            -i FILE         Print database information
    --build=NAME [cvd] -b NAME             Build a CVD file
    --max-bad-sigs=NUMBER                  Maximum number of mismatched signatures
                                           When building a CVD. Default: 3000
    --flevel=FLEVEL                        Specify a custom flevel.
                                           Default: 216
    --cvd-version=NUMBER                   Specify the version number to use for
                                           the build. Default is to use the value+1
                                           from the current CVD in --datadir.
                                           If no datafile is found the default
                                           behaviour is to prompt for a version
                                           number, this switch will prevent the
                                           prompt.  NOTE: If a CVD is found in the
                                           --datadir its version+1 is used and
                                           this value is ignored.
    --no-cdiff                             Don't generate .cdiff file
    --unsigned                             Create unsigned database file (.cud)
    --hybrid                               Create a hybrid (standard and bytecode) database file
    --print-certs=FILE                     Print Authenticode details from a PE
    --server=ADDR                          ClamAV Signing Service address
    --datadir=DIR                          Use DIR as default database directory
    --unpack=FILE          -u FILE         Unpack a CVD/CLD file
    --unpack-current=SHORTNAME             Unpack local CVD/CLD into cwd
    --list-sigs[=FILE]     -l[FILE]        List signature names
    --find-sigs=REGEX      -fREGEX         Find signatures matching REGEX
    --decode-sigs                          Decode signatures from stdin
    --test-sigs=DATABASE TARGET_FILE       Test signatures from DATABASE against
                                           TARGET_FILE
    --vba=FILE                             Extract VBA/Word6 macro code
    --vba-hex=FILE                         Extract Word6 macro code with hex values
    --diff=OLD NEW         -d OLD NEW      Create diff for OLD and NEW CVDs
    --compare=OLD NEW      -c OLD NEW      Show diff between OLD and NEW files in
                                           cdiff format
    --run-cdiff=FILE       -r FILE         Execute update script FILE in cwd
    --verify-cdiff=DIFF CVD/CLD            Verify DIFF against CVD/CLD
    --tempdir=DIRECTORY                    Create temporary files in DIRECTORY
    --leave-temps[=yes/no(*)]              Do not remove temporary files
```

### `clamconf`

> 官方示例调用：`clamconf -h`

```text
root@kali:~# clamconf -h
                       Clam AntiVirus: Configuration Tool 1.4.6
           By The ClamAV Team: https://www.clamav.net/about.html#credits
           (C) 2024 Cisco Systems, Inc.
    --help                 -h         Show this help
    --version              -V         Show version
    --config-dir=DIR       -c DIR     Read configuration files from DIR
    --non-default          -n         Only display non-default settings
    --generate-config=NAME -g NAME    Generate example config file
```

### `clamd`

> 官方示例调用：`clamd -h`

```text
root@kali:~# clamd -h
                      Clam AntiVirus: Daemon 1.4.6
           By The ClamAV Team: https://www.clamav.net/about.html#credits
           (C) 2024 Cisco Systems, Inc.
    clamd [options]
    --help                   -h             Show this help
    --version                -V             Show version number
    --foreground             -F             Run in foreground; do not daemonize
    --debug                                 Enable debug mode
    --log=FILE               -l FILE        Log into FILE
    --config-file=FILE       -c FILE        Read configuration from FILE
    --fail-if-cvd-older-than=days           Return with a nonzero error code if virus database outdated
    --datadir=DIRECTORY                     Load signatures from DIRECTORY
    --pid=FILE               -p FILE        Write the daemon's pid to FILE
Pass in - as the filename for stdin.
```

### `clamdtop`

> 官方示例调用：`clamdtop -h`

```text
root@kali:~# clamdtop -h
                       Clam AntiVirus: Monitoring Tool 1.4.6
           By The ClamAV Team: https://www.clamav.net/about.html#credits
           (C) 2024 Cisco Systems, Inc.
    clamdtop [-hVc] [host[:port] /path/to/clamd.sock ...]
    --help                 -h         Show this help
    --version              -V         Show version
    --config-file=FILE     -c FILE    Read clamd's configuration files from FILE
    --defaultcolors        -d         Use default terminal colors
    host[:port]                       Connect to clamd on host at port (default 3310)
    /path/to/clamd.sock               Connect to clamd over a local socket
```

### `clamonacc`

> 官方示例调用：`clamonacc -h`

```text
root@kali:~# clamonacc -h
           ClamAV: On Access Scanning Application and Client 1.4.6
           By The ClamAV Team: https://www.clamav.net/about.html#credits
           (C) 2024 Cisco Systems, Inc.
    clamonacc [options] [file/directory/-]
    --help                 -h          Show this help
    --version              -V          Print version number and exit
    --verbose              -v          Be verbose
    --log=FILE             -l FILE     Save scanning output to FILE
    --foreground           -F          Output to foreground and do not daemonize
    --watch-list=FILE      -W FILE     Watch directories from FILE
    --exclude-list=FILE    -e FILE     Exclude directories from FILE
    --ping                 -p A[:I]    Ping clamd up to [A] times at optional interval [I] until it responds.
    --wait                 -w          Wait up to 30 seconds for clamd to start. Optionally use alongside --ping to set attempts [A] and interval [I] to check clamd.
    --remove                           Remove infected files. Be careful!
    --move=DIRECTORY                   Move infected files into DIRECTORY
    --copy=DIRECTORY                   Copy infected files into DIRECTORY
    --config-file=FILE     -c FILE     Read configuration from FILE
    --allmatch             -z          Continue scanning within file after finding a match.
    --fdpass                           Pass filedescriptor to clamd (useful if clamd is running as a different user)
    --stream                           Force streaming files to clamd (for debugging and unit testing)
```

### `freshclam`

> 官方示例调用：`freshclam -h`

```text
root@kali:~# freshclam -h
                      Clam AntiVirus: Database Updater 1.4.6
           By The ClamAV Team: https://www.clamav.net/about.html#credits
           (C) 2024 Cisco Systems, Inc.
    freshclam [options]
    --help               -h              Show this help
    --version            -V              Print version number and exit
    --verbose            -v              Be verbose
    --debug                              Enable debug messages
    --quiet                              Only output error messages
    --no-warnings                        Don't print and log warnings
    --stdout                             Write to stdout instead of stderr.
                                         Does not affect 'debug' messages.
    --show-progress                      Show download progress percentage
    --config-file=FILE                   Read configuration from FILE.
    --log=FILE           -l FILE         Log into FILE
    --daemon             -d              Run in daemon mode
    --pid=FILE           -p FILE         Write the daemon's pid to FILE
    --foreground         -F              Don't fork into background (for use in daemon mode).
    --user=USER          -u USER         Run as USER
    --no-dns                             Force old non-DNS verification method
    --checks=#n          -c #n           Number of checks per day, 1 <= n <= 50
    --datadir=DIRECTORY                  Download new databases into DIRECTORY
                                         NOTE: DIRECTORY must already exist, be an absolute path, and                                         be writeable by freshclam and readable by clamd/clamscan.    --daemon-notify[=/path/clamd.conf]   Send RELOAD command to clamd
    --local-address=IP   -a IP           Bind to IP for HTTP downloads
    --on-update-execute=COMMAND          Execute COMMAND after successful update.
                                         Use EXIT_1 to return 1 after successful database update.
    --on-error-execute=COMMAND           Execute COMMAND if errors occurred
    --on-outdated-execute=COMMAND        Execute COMMAND when software is outdated
    --update-db=DBNAME                   Only update database DBNAME
Environment Variables:
  CURL_CA_BUNDLE                         May be set to the path of a file (bundle)
                                         containing one or more CA certificates.
                                         This will override the default openssl
                                         certificate path.
  FRESHCLAM_CLIENT_CERT                  May be set to the path of a file (PEM)
                                         containing the client certificate.
                                         This may be used for client authentication
                                         to a private mirror.
  FRESHCLAM_CLIENT_KEY                   May be set to the path of a file (PEM)
                                         containing the client private key.
                                         This is required if FRESHCLAM_CLIENT_CERT is set.
  FRESHCLAM_CLIENT_KEY_PASSWD            May be set to a password for the client key PEM file.
                                         This is required if FRESHCLAM_CLIENT_KEY is
                                         set and the PEM file is password protected.
```

### `clamav-milter`

> 官方示例调用：`clamav-milter -h`

```text
root@kali:~# clamav-milter -h
                       Clam AntiVirus: Milter Mail Scanner 1.4.6
           By The ClamAV Team: https://www.clamav.net/about.html#credits
           (C) 2024 Cisco Systems, Inc.
    clamav-milter [-c <config-file>]
    --help                   -h             Show this help
    --version                -V             Show version
    --config-file <file>     -c             Read configuration from file
    --pid=FILE               -p FILE        Write the daemon's pid to FILE
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install clamav`，再执行 `clamav --version` 2>/dev/null || `clamav -V`
- [ ] **2.** **读官方帮助** —— `clamav -h`，需要细节时 `man clamav`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `clamav -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/clamav/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/clamav/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/clamav/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
