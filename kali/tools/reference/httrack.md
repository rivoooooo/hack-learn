# httrack

> Copy websites to your computer (Offline browser) HTTrack is an offline browser utility, allowing you to download a World Wide website from the Internet to a local directory, building recursively all directories, getting html, images, and o…

> **功能分类**：Web 应用 ｜ **Kali 包**：`httrack` ｜ **官方文档**：<https://www.kali.org/tools/httrack/>

## 1. 安装

```bash
sudo apt update
sudo apt install httrack
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.50.1 |
| 架构 | any |
| 可执行命令 | `httrack`、`httrack-doc`、`libhttrack-dev`、`libhttrack3`、`proxytrack`、`webhttrack`、`htsserver`、`webhttrack-common` |
| 依赖 | `libc6`、`libhttrack3` |
| 安装体积 | 98 KB |
| 官网 | <https://www.httrack.com> |
| 源码仓库 | <https://github.com/xroche/httrack> |
| 包追踪 | <https://pkg.kali.org/pkg/httrack> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
httrack -h          # 查看用法
man httrack         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 8 个可执行命令，下面是官方页面内嵌的帮助原文。

### `httrack`

> 官方示例调用：`httrack -h`

```text
root@kali:~# httrack -h
HTTrack version 3.50-1
	usage: httrack <URLs> [-option] [+<URL_FILTER>] [-<URL_FILTER>] [+<mime:MIME_FILTER>] [-<mime:MIME_FILTER>]
	with options listed below: (* is the default value)
General options:
  O  path for mirror/logfiles+cache (-O path_mirror[,path_cache_and_logfiles]) (--path <param>)
Action options:
  w *mirror web sites (--mirror)
  W  mirror web sites, semi-automatic (asks questions) (--mirror-wizard)
  g  just get files (saved in the current directory) (--get-files)
  i  continue an interrupted mirror using the cache (--continue)
  Y   mirror ALL links located in the first level pages (mirror links) (--mirrorlinks)
Proxy options:
  P  proxy use (-P [socks5://|connect://][user:pass@]proxy:port) (--proxy <param>)
 %f *use proxy for ftp (f0 don't use) (--httpproxy-ftp[=0])
 %b  use this local hostname to make/send requests (-%b hostname) (--bind <param>)
Limits options:
  rN set the mirror depth to N (* r9999) (--depth[=N])
 %eN set the external links depth to N (* %e0) (--ext-depth[=N])
  mN maximum file length for a non-html file (--max-files[=N])
  mN,N2 maximum file length for non html (N) and html (N2)
  MN maximum overall size that can be uploaded/scanned (--max-size[=N])
  EN maximum mirror time in seconds (60=1 minute, 3600=1 hour) (--max-time[=N])
  AN maximum transfer rate in bytes/seconds (1000=1KB/s max) (--max-rate[=N])
 %cN maximum number of connections/seconds (*%c5) (--connection-per-second[=N])
 %G  random pause of MIN[:MAX] seconds between files (e.g. %G5:10) (--pause <param>)
  GN pause transfer if N bytes reached, and wait until lock file is deleted (--max-pause[=N])
Flow control:
  cN number of multiple connections (*c4) (--sockets[=N])
  TN timeout, number of seconds after a non-responding link is shutdown; also bounds host name resolution (--timeout[=N])
  RN number of retries, in case of timeout or non-fatal errors (*R1) (--retries[=N])
  JN traffic jam control, minimum transfert rate (bytes/seconds) tolerated for a link (--min-rate[=N])
  HN host is abandoned if: 0=never, 1=timeout, 2=slow, 3=timeout or slow (--host-control[=N])
Links options:
 %P *extended parsing, attempt to parse all links, even in unknown tags or Javascript (%P0 don't use) (--extended-parsing[=0])
  n  get non-html files 'near' an html file (ex: an image located outside) (--near)
  t  test all URLs (even forbidden ones) (--test)
 %L <file> add all URL located in this text file (one URL per line) (--list <param>)
 %S <file> add all scan rules located in this text file (one scan rule per line) (--urllist <param>)
 %m  seed the crawl from the site's sitemap (robots.txt Sitemap:, then /sitemap.xml); --sitemap-url URL names one explicitly. A sitemap you name, or one the site declares, is fetched even under robots.txt Disallow; only the guessed /sitemap.xml obeys it. The URLs found still pass every filter and scope rule (--sitemap)
Build options:
  NN structure type (0 *original structure, 1+: see below) (--structure[=N])
     or user defined structure (-N "%h%p/%n%q.%t", --structure or --user-structure)
     --structure takes one preset or template: -N1L0 clusters more short options, --structure=1L0 is refused
 %N  delayed type check, don't make any link test but wait for files download to start instead (experimental) (%N0 don't use, %N1 use for unknown extensions, * %N2 always use) (--delayed-type-check[=N])
 %D  cached delayed type check, don't wait for remote type during updates, to speedup them (%D0 wait, * %D1 don't wait) (--cached-delayed-type-check[=0])
 %M  generate a RFC MIME-encapsulated full-archive (.mht) (--mime-html[=0])
 %Z  after the mirror, rewrite each saved page with its stylesheets, scripts, images and fonts inlined as data: URIs, so any page opens by double-click anywhere (links between pages stay relative; audio and video stay links); --single-file-max-size N caps each asset (default 10485760 bytes). %M is the better container where a Chromium-family browser is a given: one archive, no base64 tax on text, a shared asset stored once (--single-file[=0])
 %t  keep the original file extension, don't rewrite it from the MIME type (%t0 rewrite)
  LN long names (L1 *long names / L0 8-3 conversion / L2 ISO9660 compatible) (--long-names[=N])
  KN keep original links (e.g. http://www.adr/link) (K0 *relative link, K absolute links, K4 original links, K3 absolute URI links, K5 transparent proxy link) (--keep-links[=N])
  x  replace external html links by error pages (--replace-external)
 %x  do not include any password for external password protected websites (%x0 include) (--disable-passwords[=0])
 %q *include query string for local files (useless, for information purpose only) (%q0 don't include) (--include-query-string[=0])
 %g  strip query keys for dedup ([host/pattern=]key1,key2,...) (--strip-query <param>)
 %C  fold other hostnames of one site onto it ([scheme://]alias[,...]=[scheme://]host) (--host-alias <param>)
  o *save the server's error pages (404..) (o0 discard them) (--generate-errors[=N])
  X *purge old files after update (X0 keep delete) (--purge-old[=0])
 %p  preserve html files 'as is' (identical to '-K4 -%F ""') (--preserve)
 %T  links conversion to UTF-8 (--utf8-conversion[=0])
Spider options:
  bN accept cookies in cookies.txt (0=do not accept,* 1=accept) (--cookies[=N])
 %K  load extra cookies from a Netscape cookies.txt (--cookies-file <param>)
 %Y  explain which filter rule accepts or rejects a URL, then exit (--why <param>)
  u  check document type if unknown (cgi,asp..) (u0 don't check, * u1 check but /, u2 check always) (--check-type[=N])
  j *parse scripts (j0 don't parse, bitmask: |1 parse default, |4 don't parse .js |8 don't be aggressive) (--parse-java[=N])
  sN follow robots.txt and meta robots tags (0=never,1=sometimes,* 2=always, 3=always (even strict rules)) (--robots[=N])
 %h  force HTTP/1.0 requests (reduce update features, only for old servers or proxies) (--http-10[=0])
 %k  use keep-alive if possible, greately reducing latency for small files and test requests (%k0 don't use) (--keep-alive[=0])
 %z  do not request compressed content (%z0 request) (--disable-compression[=0])
 %B  tolerant requests (accept bogus responses on some servers, but not standard!) (--tolerant[=0])
 %s  update hacks: various hacks to limit re-transfers when updating (identical size, bogus response..) (--updatehack[=0])
 %u  url hacks: various hacks to limit duplicate URLs (strip //, www.foo.com==foo.com..) (--urlhack[=0])
     opt out of one url-hack part: --keep-www-prefix (www.foo.com<>foo.com), --keep-double-slashes (//), --keep-query-order (?b&a)
 %A  assume that a type (cgi,asp..) is always linked with a mime type (-%A php3,cgi=text/html;dat,bin=application/x-zip) (--assume <param>)
     shortcut: '--assume standard' is equivalent to -%A php2 php3 php4 php cgi asp jsp pl cfm nsf=text/html
     can also be used to force a specific file type: --assume foo.cgi=text/html
 @iN internet protocol (0=both ipv6+ipv4, 4=ipv4 only, 6=ipv6 only) (--protocol[=N])
 %w  disable a specific external mime module (-%w httrack-plugin) (--disable-module <param>)
Browser ID:
  F  user-agent field sent in HTTP headers (-F "user-agent name") (--user-agent <param>)
 %R  default referer field sent in HTTP headers (--referer <param>)
 %E  from email address sent in HTTP headers (--from <param>)
 %F  footer string in Html code (-%F "Mirrored from {url} on {date}"; fields {addr} {path} {url} {date} {lastmodified} {version} {mime} {charset} {status} {size}, or legacy %s) (--footer <param>)
 %l  preferred language (-%l "fr, en, jp, *" (--language <param>)
 %a  accepted formats (-%a "text/html,image/png;q=0.9,*/*;q=0.1" (--accept <param>)
 %X  additional HTTP header line (-%X "X-Magic: 42" (--headers <param>)
Log, index, cache
  C  create/use a cache for updates and retries (C0 no cache,C1 cache is prioritary,* C2 test update before) (--cache[=N])
  k  store all files in cache (not useful if files on disk) (--store-all-in-cache)
 %r  write an ISO-28500 WARC/1.1 archive; --warc-file NAME sets the output name, --warc-max-size N rotates segments past N bytes, --warc-cdx also writes a sorted CDXJ index, --wacz packages it all as a WACZ file (--warc)
 %d  write hts-changes.json listing what this crawl left new, changed, unchanged and gone compared to the previous mirror (--changes[=0])
 %n  do not re-download locally erased files (--do-not-recatch[=0])
 %v  display on screen filenames downloaded (in realtime) - * %v1 short version - %v2 full animation (--display[=N])
  Q  no log - quiet mode (--do-not-log)
  q  no questions - quiet mode (--quiet)
  z  log - extra infos (--extra-log)
  Z  log - debug (--debug-log)
  v  log on screen (--verbose)
  f *log in files (--file-log)
  f2 one single log file (--single-log)
  I *make an index (I0 don't make) (--index[=0])
 %i  make a top index for a project folder (* %i0 don't make) (--build-top-index[=0])
 %I  make an searchable index for this mirror (* %I0 don't make) (--search-index[=N])
Expert options:
  pN priority mode: (* p3) (--priority[=N])
      p0 just scan, don't save anything (for checking links)
      p1 save only html files
      p2 save only non html files
     *p3 save all files
      p7 get html files before, then treat other files
  S  stay on the same directory (--stay-on-same-dir)
  D *can only go down into subdirs (--can-go-down)
  U  can only go to upper directories (--can-go-up)
  B  can both go up&down into the directory structure (--can-go-up-and-down)
  a *stay on the same address (--stay-on-same-address)
  d  stay on the same principal domain (--stay-on-same-domain)
  l  stay on the same TLD (eg: .com) (--stay-on-same-tld)
  e  go everywhere on the web (--go-everywhere)
 %H  debug HTTP headers in logfile (--debug-headers)
Guru options: (do NOT use if possible)
 #test  list engine self-tests (run one with -#test=NAME [args])
 #C  cache list (-#C '*.com/spider*.gif' (--debug-cache <param>)
 #R  cache repair (damaged cache) (--repair-cache)
 #d  debug parser (--debug-parsing)
 #E  extract new.zip cache meta-data in meta.zip
 #f  always flush log files (--advanced-flushlogs)
 #FN maximum number of filters (--advanced-maxfilters[=N])
 #h  version info (--version)
 #K  scan stdin (debug) (--debug-scanstdin)
 #L  maximum number of links (-#L1000000) (--advanced-maxlinks[=N])
 #p  display ugly progress information (--advanced-progressinfo)
 #P  catch URL (--catch-url)
 #T  generate transfer ops. log every minutes (--debug-xfrstats)
 #u  wait time (--advanced-wait[=N])
 #Z  generate transfer rate statistics every minutes (--debug-ratestats)
Dangerous options: (do NOT use unless you exactly know what you are doing)
 %!  bypass built-in security limits aimed to avoid bandwidth abuses (bandwidth, simultaneous connections) (--disable-security-limits[=0])
     IMPORTANT NOTE: DANGEROUS OPTION, ONLY SUITABLE FOR EXPERTS
                     USE IT WITH EXTREME CARE
Command-line specific options:
  V execute system command after each files ($0 is the filename: -V "rm \$0") (--userdef-cmd <param>)
 %W use an external library function as a wrapper (-%W myfoo.so[,myparameters]) (--callback <param>)
  y  go to background when suspended (y0 don't) (--background-on-suspend[=0])
Details: Option N
  N0 Site-structure (default)
  N1 HTML in web/, images/other files in web/images/
  N2 HTML in web/HTML, images/other in web/images
  N3 HTML in web/,  images/other in web/
  N4 HTML in web/, images/other in web/xxx, where xxx is the file extension (all gif will be placed onto web/gif, for example)
  N5 Images/other in web/xxx and HTML in web/HTML
  N99 All files in web/, with random names (gadget !)
  N100 Site-structure, without www.domain.xxx/
  N101 Identical to N1 except that "web" is replaced by the site's name
  N102 Identical to N2 except that "web" is replaced by the site's name
  N103 Identical to N3 except that "web" is replaced by the site's name
  N104 Identical to N4 except that "web" is replaced by the site's name
  N105 Identical to N5 except that "web" is replaced by the site's name
  N199 Identical to N99 except that "web" is replaced by the site's name
  N1001 Identical to N1 except that there is no "web" directory
  N1002 Identical to N2 except that there is no "web" directory
  N1003 Identical to N3 except that there is no "web" directory (option set for g option)
  N1004 Identical to N4 except that there is no "web" directory
  N1005 Identical to N5 except that there is no "web" directory
  N1099 Identical to N99 except that there is no "web" directory
Details: User-defined option N
  '%n' Name of file without file type (ex: image)
  '%N' Name of file, including file type (ex: image.gif)
  '%t' File type (ex: gif)
  '%p' Path [without ending /] (ex: /someimages)
  '%h' Host name (ex: www.example.com)
  '%M' URL MD5 (128 bits, 32 ascii bytes)
  '%Q' query string MD5 (128 bits, 32 ascii bytes)
  '%k' full query string
  '%r' protocol name (ex: http)
  '%q' small query string MD5 (16 bits, 4 ascii bytes)
     '%s?' Short name version (ex: %sN)
  '%[param]' param variable in query string
  '%[param:before:after:empty:notfound]' advanced variable extraction
Details: User-defined option N and advanced variable extraction
   %[param:before:after:empty:notfound]
   param : parameter name
   before : string to prepend if the parameter was found
   after : string to append if the parameter was found
   notfound : string replacement if the parameter could not be found
   empty : string replacement if the parameter was empty
   all fields, except the first one (the parameter name), can be empty
Details: Option K
  K0  foo.cgi?q=45  ->  foo4B54.html?q=45 (relative URI, default)
  K                 ->  http://www.example.com/folder/foo.cgi?q=45 (absolute URL) (--keep-links[=N])
  K3                ->  /folder/foo.cgi?q=45 (absolute URI)
  K4                ->  foo.cgi?q=45 (original URL)
  K5                ->  http://www.example.com/folder/foo4B54.html?q=45 (transparent proxy URL)
Shortcuts:
--mirror      <URLs> *make a mirror of site(s) (default)
--get         <URLs>  get the files indicated, do not seek other URLs (-qg)
--list   <text file>  add all URL located in this text file (-%L)
--mirrorlinks <URLs>  mirror all links in 1st level pages (-Y)
--testlinks   <URLs>  test links in pages (-r1p0C0I0t)
--spider      <URLs>  spider site(s), to test links: reports Errors & Warnings (-p0C0I0t)
--testsite    <URLs>  identical to --spider
--skeleton    <URLs>  make a mirror, but gets only html files (-p1)
--update              update a mirror, without confirmation (-iC2)
--continue            continue a mirror, without confirmation (-iC1)
--catchurl            create a temporary proxy to capture an URL or a form post URL
--clean               erase cache & log files
--http10              force http/1.0 requests (-%h)
Details: Option %W: External callbacks prototypes
see htsdefines.h
example: httrack www.example.com/bob/
means:   mirror site www.example.com/bob/ and only this site
example: httrack www.example.com/bob/ other.example.com/mike/ +*.com/*.jpg -mime:application/*
means:   mirror the two sites together (with shared links) and accept any .jpg files on .com sites
example: httrack www.example.com/bob/bobby.html +* -r6
means get all files starting from bobby.html, with 6 link-depth, and possibility of going everywhere on the web
example: httrack www.example.com/bob/bobby.html --spider -P proxy.example.com:8080
runs the spider on www.example.com/bob/bobby.html using a proxy
example: httrack --update
updates a mirror in the current folder
example: httrack
```

### `proxytrack`

> 官方示例调用：`proxytrack -h`

```text
root@kali:~# proxytrack -h
proxy mode:
usage: proxytrack <proxy-addr:proxy-port> <ICP-addr:ICP-port> [ ( <new.zip path> | <new.ndx path> | <archive.arc path> | --list <file-list> ) ..]
	example:proxytrack proxy:8080 localhost:3130 /home/archives/www-archive-01.zip /home/old-archives/www-archive-02.ndx
convert mode:
usage: proxytrack --convert <archive-output-path> [ ( <new.zip path> | <new.ndx path> | <archive.arc path> | --list <file-list> ) ..]
	example:proxytrack proxy:8080 localhost:3130 /home/archives/www-archive-01.zip /home/old-archives/www-archive-02.ndx
```

### `man`

> 官方示例调用：`man htsserver`

```text
root@kali:~# man htsserver
htsserver(1)                General Commands Manual                htsserver(1)
NAME
     htsserver - offline browser server : copy websites to a local directory
SYNOPSIS
     htsserver [ path/ ] [ keyword value [ keyword value .. ] ]
DESCRIPTION
     htsserver  this  program is a web frontend server to httrack(1).  , a web-
     site copier, used by webhttrack(1).
EXAMPLES
     htsserver /usr/share/httrack/ path $HOME/websites lang 1
             then, browse http://localhost:8080/
FILES
     /etc/httrack.conf
            The system wide configuration file.
ENVIRONMENT
     HOME   Is being used if you defined in  /etc/httrack.conf  the  line  path
            ~/websites/#
DIAGNOSTICS
     Errors/Warnings are reported to hts-log.txt located in the destination di-
     rectory.
BUGS
     Please  reports bugs to <
[email protected]
>.  Include a complete, self-con-
     tained example that will allow the bug to be  reproduced,  and  say  which
     version  of  (web)httrack  you  are using. Do not forget to detail options
     used, OS version, and any other information you deem necessary.
COPYRIGHT
     Copyright (C) 1998-2026 Xavier Roche and other contributors
     This program is free software: you can redistribute it  and/or  modify  it
     under the terms of the GNU General Public License as published by the Free
     Software  Foundation, either version 3 of the License, or (at your option)
     any later version.
     This program is distributed in the hope that it will be useful, but  WITH-
     OUT  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
     FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License  for
     more details.
     You  should  have  received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
AVAILABILITY
     The  most  recent released  version  of  (web)httrack  can  be  found  at:
     https://www.httrack.com
AUTHOR
     Xavier Roche <
[email protected]
>
SEE ALSO
     The  HTML documentation (available online at https://www.httrack.com/html/
     ) contains more detailed information. Please also refer to the httrack FAQ
     (available online at https://www.httrack.com/html/faq.html )
httrack website copier              Mar 2003                       htsserver(1)
```

### `webhttrack`

> 官方示例调用：`webhttrack -h`

```text
root@kali:~# webhttrack -h
** Warning: use the webhttrack frontend if available
usage: /usr/bin/htsserver [--port <port>] [--bind <address>: default 127.0.0.1] [--ppid parent-pid] [--ping-timeout <seconds>] <path-to-html-root-dir> [key value [key value]..]
example: /usr/bin/htsserver /usr/share/httrack/
/usr/bin/webhttrack(285774): Could not spawn htsserver
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install httrack`，再执行 `httrack --version` 2>/dev/null || `httrack -V`
- [ ] **2.** **读官方帮助** —— `httrack -h`，需要细节时 `man httrack`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `httrack -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/httrack/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/collection.md`](../../tools/by-attack/collection.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/httrack/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/httrack/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
