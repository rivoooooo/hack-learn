# curl

> Command line tool for transferring data with URL syntax curl is a command line tool for transferring data with URL syntax, supporting DICT, FILE, FTP, FTPS, GOPHER, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP,…

> **功能分类**：信息搜集 ｜ **Kali 包**：`curl` ｜ **官方文档**：<https://www.kali.org/tools/curl/>

## 1. 安装

```bash
sudo apt update
sudo apt install curl
```

| 项目 | 内容 |
|------|------|
| 版本 | 8.21.0 |
| 架构 | any |
| 可执行命令 | `curl`、`wcurl`、`libcurl3t64-gnutls`、`libcurl4-doc`、`libcurl4-gnutls`、`libcurl4-gnutls-dev`、`curl-config`、`libcurl4-openssl-dev`、`libcurl4t64` |
| 依赖 | `libc6`、`libcurl4t64`、`zlib1g` |
| 安装体积 | 512 KB |
| 官网 | <https://curl.se/> |
| 源码仓库 | <https://salsa.debian.org/debian/curl> |
| 包追踪 | <https://pkg.kali.org/pkg/curl> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
curl -h          # 查看用法
man curl         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 9 个可执行命令，下面是官方页面内嵌的帮助原文。

### `curl`

官方给出的调用示例：`curl -h`

```text
root@kali:~# curl -h
Usage: curl [options...] <url>
 -d, --data <data>            HTTP POST data
 -f, --fail                   Fail fast with no output on HTTP errors
 -I, --head                   Show document info only
 -H, --header <header/@file>  Pass custom header(s) to server
 -h, --help <subject>         Get help for commands
 -o, --output <file>          Write to file instead of stdout
 -O, --remote-name            Write output to file named as remote file
 -i, --show-headers           Show response headers in output
 -s, --silent                 Silent mode
 -T, --upload-file <file>     Transfer local FILE to destination
 -u, --user <user:password>   Server user and password
 -A, --user-agent <name>      Send User-Agent <name> to server
 -v, --verbose                Make the operation more talkative
 -V, --version                Show version number and quit
This is not the full help; this menu is split into categories.
Use "--help category" to get an overview of all categories, which are:
auth, connection, curl, deprecated, dns, file, ftp, global, http, imap, ldap,
output, pop3, post, proxy, scp, sftp, smtp, ssh, telnet, tftp, timeout, tls,
upload, verbose.
Use "--help all" to list all options
Use "--help [option]" to view documentation for a given option
```

### `wcurl`

官方给出的调用示例：`wcurl -h`

```text
root@kali:~# wcurl -h
wcurl -- a simple wrapper around curl to easily download files.
Usage: wcurl <URL>...
       wcurl [--curl-options <CURL_OPTIONS>]... [--no-decode-filename] [-o|-O|--output <PATH>] [--dry-run] [--] <URL>...
       wcurl [--curl-options=<CURL_OPTIONS>]... [--no-decode-filename] [--output=<PATH>] [--dry-run] [--] <URL>...
       wcurl -h|--help
       wcurl -V|--version
Options:
  --curl-options <CURL_OPTIONS>: Specify extra options to be passed when invoking curl. May be
                                 specified more than once.
  -o, -O, --output <PATH>: Use the provided output path instead of getting it from the URL. If
                           multiple URLs are provided, resulting files share the same name with a
                           number appended to the end (curl >= 7.83.0). If this option is provided
                           multiple times, only the last value is considered.
  --no-decode-filename: Do not percent-decode the output filename, even if the percent-encoding in
                        the URL was done by wcurl, e.g.: The URL contained whitespace.
  --dry-run: Do not actually execute curl, only print what would be invoked.
  -V, --version: Print version information.
  -h, --help: Print this usage message.
  <CURL_OPTIONS>: Any option supported by curl can be set here. This is not used by wcurl; it is
                 instead forwarded to the curl invocation.
  <URL>: URL to be downloaded. Anything that is not a parameter is considered
         an URL. Whitespace is percent-encoded and the URL is passed to curl, which
         then performs the parsing. May be specified more than once.
```

### `curl-config`

官方给出的调用示例：`curl-config --help`

```text
root@kali:~# curl-config --help
Usage: curl-config [OPTION]
Available values for OPTION include:
  --built-shared        says 'yes' if libcurl was built shared
  --ca                  CA bundle install path
  --cc                  compiler
  --cflags              preprocessor and compiler flags
  --checkfor [version]  check for (lib)curl of the specified version
  --configure           the arguments given to configure when building curl
  --features            newline separated list of enabled features
  --help                display this help and exit
  --libs                library linking information
  --prefix              curl install prefix
  --protocols           newline separated list of enabled protocols
  --ssl-backends        output the SSL backends libcurl was built to support
  --static-libs         static libcurl library linking information
  --version             output version information
  --vernum              output version as a hexadecimal number
```

### `curl-config（示例）`

官方给出的调用示例：`curl-config --help`

```text
root@kali:~# curl-config --help
Usage: curl-config [OPTION]
Available values for OPTION include:
  --built-shared        says 'yes' if libcurl was built shared
  --ca                  CA bundle install path
  --cc                  compiler
  --cflags              preprocessor and compiler flags
  --checkfor [version]  check for (lib)curl of the specified version
  --configure           the arguments given to configure when building curl
  --features            newline separated list of enabled features
  --help                display this help and exit
  --libs                library linking information
  --prefix              curl install prefix
  --protocols           newline separated list of enabled protocols
  --ssl-backends        output the SSL backends libcurl was built to support
  --static-libs         static libcurl library linking information
  --version             output version information
  --vernum              output version as a hexadecimal number
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install curl`，再执行 `curl --version` 2>/dev/null || `curl -V`
- [ ] **2.** **读官方帮助** —— `curl -h`，需要细节时 `man curl`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: curl [options...] <url>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/curl/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/curl/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/curl/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
