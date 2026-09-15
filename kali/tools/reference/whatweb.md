# whatweb

> Next generation web scanner WhatWeb identifies websites. It recognises web technologies including content management systems (CMS), blogging platforms, statistic/analytics packages, JavaScript libraries, web servers, and embedded devices. …

> **功能分类**：信息搜集 ｜ **Kali 包**：`whatweb` ｜ **官方文档**：<https://www.kali.org/tools/whatweb/>

## 1. 安装

```bash
sudo apt update
sudo apt install whatweb
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.6.4 |
| 架构 | all |
| 可执行命令 | `whatweb` |
| 依赖 | `ruby`、`ruby-addressable`、`ruby-ipaddress` |
| 安装体积 | 18.76 MB |
| 官网 | <https://github.com/urbanadventurer/WhatWeb> |
| 包追踪 | <https://pkg.kali.org/pkg/whatweb> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
whatweb -h          # 查看用法
man whatweb         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `whatweb`

官方给出的调用示例：`whatweb -v -a 3 192.168.0.102`

```text
root@kali:~# whatweb -v -a 3 192.168.0.102
WhatWeb report for http://192.168.0.102
Status    : 200 OK
Title     : Toolz TestBed
IP        : 192.168.0.102
Country   : RESERVED, ZZ
Summary   : JQuery, Script, X-UA-Compatible[IE=edge], HTML5, Apache[2.2,2.2.22], HTTPServer[Ubuntu Linux][Apache/2.2.22 (Ubuntu)]
Detected Plugins:
[ Apache ]
  The Apache HTTP Server Project is an effort to develop and
  maintain an open-source HTTP server for modern operating
  systems including UNIX and Windows NT. The goal of this
  project is to provide a secure, efficient and extensible
  server that provides HTTP services in sync with the current
  HTTP standards.
  Version      : 2.2.22 (from HTTP Server Header)
  Version      : 2.2
  Version      : 2.2
  Google Dorks: (3)
  Website     : http://httpd.apache.org/
[ HTML5 ]
  HTML version 5, detected by the doctype declaration
[ HTTPServer ]
  HTTP server header string. This plugin also attempts to
  identify the operating system from the server header.
  OS           : Ubuntu Linux
  String       : Apache/2.2.22 (Ubuntu) (from server string)
[ JQuery ]
  A fast, concise, JavaScript that simplifies how to traverse
  HTML documents, handle events, perform animations, and add
  AJAX.
  Website     : http://jquery.com/
[ Script ]
  This plugin detects instances of script HTML elements and
  returns the script language/type.
[ X-UA-Compatible ]
  This plugin retrieves the X-UA-Compatible value from the
  HTTP header and meta http-equiv tag. - More Info:
  http://msdn.microsoft.com/en-us/library/cc817574.aspx
  String       : IE=edge
HTTP Headers:
  HTTP/1.1 200 OK
  Server: Apache/2.2.22 (Ubuntu)
  Last-Modified: Fri, 02 Feb 2018 15:27:56 GMT
  ETag: "11f-2e38-5643c5b56a8d3"
  Accept-Ranges: bytes
  Vary: Accept-Encoding
  Content-Encoding: gzip
  Content-Length: 3541
  Connection: close
  Content-Type: text/html
```

### ``

```text
root@kali:~#
```

### `whatweb（示例）`

官方给出的调用示例：`whatweb -h`

```text
root@kali:~# whatweb -h
.$$$     $.                                   .$$$     $.
$$$$     $$. .$$$  $$$ .$$$$$$.  .$$$$$$$$$$. $$$$     $$. .$$$$$$$. .$$$$$$.
$ $$     $$$ $ $$  $$$ $ $$$$$$. $$$$$ $$$$$$ $ $$     $$$ $ $$   $$ $ $$$$$$.
$ `$     $$$ $ `$  $$$ $ `$  $$$ $$' $ `$ `$$ $ `$     $$$ $ `$      $ `$  $$$'
$. $     $$$ $. $$$$$$ $. $$$$$$ `$  $. $  :' $. $     $$$ $. $$$$   $. $$$$$.
$::$  .  $$$ $::$  $$$ $::$  $$$     $::$     $::$  .  $$$ $::$      $::$  $$$$
$;;$ $$$ $$$ $;;$  $$$ $;;$  $$$     $;;$     $;;$ $$$ $$$ $;;$      $;;$  $$$$
$$$$$$ $$$$$ $$$$  $$$ $$$$  $$$     $$$$     $$$$$$ $$$$$ $$$$$$$$$ $$$$$$$$$'
WhatWeb - Next generation web scanner version 0.6.4.
Developed by Andrew Horton (urbanadventurer) and Brendan Coles (bcoles).
Homepage: https://morningstarsecurity.com/research/whatweb
Usage: whatweb [options] <URLs>
TARGET SELECTION:
  <TARGETs>			Enter URLs, hostnames, IP addresses, filenames or
  				IP ranges in CIDR, x.x.x-x, or x.x.x.x-x.x.x.x
  				format.
  --input-file=FILE, -i		Read targets from a file. You can pipe
				hostnames or URLs directly with -i /dev/stdin.
TARGET MODIFICATION:
  --url-prefix			Add a prefix to target URLs.
  --url-suffix			Add a suffix to target URLs.
  --url-pattern			Insert the targets into a URL.
				e.g. example.com/%insert%/robots.txt
AGGRESSION:
The aggression level controls the trade-off between speed/stealth and
reliability.
  --aggression, -a=LEVEL	Set the aggression level. Default: 1.
  1. Stealthy			Makes one HTTP request per target and also
  				follows redirects.
  3. Aggressive			If a level 1 plugin is matched, additional
  				requests will be made.
  4. Heavy			Makes a lot of HTTP requests per target. URLs
  				from all plugins are attempted.
HTTP OPTIONS:
  --user-agent, -U=AGENT	Identify as AGENT instead of WhatWeb/0.6.4.
  --header, -H			Add an HTTP header. eg "Foo:Bar". Specifying a
				default header will replace it. Specifying an
				empty value, e.g. "User-Agent:" will remove it.
  --follow-redirect=WHEN	Control when to follow redirects. WHEN may be
				`never', `http-only', `meta-only', `same-site',
				or `always'. Default: always.
  --max-redirects=NUM		Maximum number of redirects. Default: 10.
AUTHENTICATION:
  --user, -u=<user:password>	HTTP basic authentication.
  --cookie, -c=COOKIES		Use cookies, e.g. 'name=value; name2=value2'.
  --cookie-jar=FILE		Read cookies from a file and save cookies to the
				same file. Creates the file if it doesn't exist.
  --no-cookies			Disable automatic cookie handling (improves performance with high thread counts).
PROXY:
  --proxy			<hostname[:port]> Set proxy hostname and port.
				Default: 8080.
  --proxy-user			<username:password> Set proxy user and password.
PLUGINS:
  --list-plugins, -l		List all plugins.
  --info-plugins, -I=[SEARCH]	List all plugins with detailed information.
				Optionally search with keywords in a comma
				delimited list.
  --search-plugins=STRING	Search plugins for a keyword.
  --plugins, -p=LIST		Select plugins. LIST is a comma delimited set
				of selected plugins. Default is all.
				Each element can be a directory, file or plugin
				name and can optionally have a modifier, +/-.
				Examples: +/tmp/moo.rb,+/tmp/foo.rb
				title,md5,+./plugins-disabled/
				./plugins-disabled,-md5
				-p + is a shortcut for -p +plugins-disabled.
  --grep, -g=STRING|REGEXP	Search for STRING or a Regular Expression. Shows
				only the results that match.
				Examples: --grep "hello"
				--grep "/he[l]*o/"
  --custom-plugin=DEFINITION	Define a custom plugin named Custom-Plugin,
				Examples: ":text=>'powered by abc'"
				":version=>/powered[ ]?by ab[0-9]/"
				":ghdb=>'intitle:abc \"powered by abc\"'"
				":md5=>'8666257030b94d3bdb46e05945f60b42'"
				"{:text=>'powered by abc'}"
  --dorks=PLUGIN		List Google dorks for the selected plugin.
OUTPUT:
  --verbose, -v			Verbose output includes plugin descriptions.
				Use twice for debugging.
  --colour,--color=WHEN		control whether colour is used. WHEN may be
				`never', `always', or `auto'.
  --quiet, -q			Do not display brief logging to STDOUT.
  --no-errors			Suppress error messages.
LOGGING:
  --log-brief=FILE		Log brief, one-line output.
  --log-verbose=FILE		Log verbose output.
  --log-errors=FILE		Log errors.
  --log-xml=FILE		Log XML format.
  --log-json=FILE		Log JSON format.
  --log-sql=FILE		Log SQL INSERT statements.
  --log-sql-create=FILE		Create SQL database tables.
  --log-json-verbose=FILE	Log JSON Verbose format.
  --log-magictree=FILE		Log MagicTree XML format.
  --log-object=FILE		Log Ruby object inspection format.
  --log-mongo-database		Name of the MongoDB database.
  --log-mongo-collection	Name of the MongoDB collection.
				Default: whatweb.
  --log-mongo-host		MongoDB hostname or IP address.
				Default: 0.0.0.0.
  --log-mongo-username		MongoDB username. Default: nil.
  --log-mongo-password		MongoDB password. Default: nil.
  --log-elastic-index		Name of the index to store results. Default: whatweb
  --log-elastic-host		Host:port of the elastic http interface. Default: 127.0.0.1:9200
PERFORMANCE & STABILITY:
  --max-threads, -t		Number of simultaneous threads. Default: 25.
  --open-timeout		Time in seconds. Default: 15.
  --read-timeout		Time in seconds. Default: 30.
  --wait=SECONDS		Wait SECONDS between connections.
				This is useful when using a single thread.
  --output-sync			Force immediate output flushing for real-time
				monitoring (slower with high thread counts).
  --output-buffer-size=SIZE	Set output buffer size. 0=unbuffered,
				default=auto based on thread count.
HELP & MISCELLANEOUS:
  --short-help			Short usage help.
  --help, -h			Complete usage help.
  --debug			Raise errors in plugins.
  --version			Display version information.
EXAMPLE USAGE:
* Scan example.com.
  ./whatweb example.com
* Scan reddit.com slashdot.org with verbose plugin descriptions.
  ./whatweb -v reddit.com slashdot.org
* An aggressive scan of wired.com detects the exact version of WordPress.
  ./whatweb -a 3 www.wired.com
* Scan the local network quickly and suppress errors.
  whatweb --no-errors 192.168.0.0/24
* Scan the local network for https websites.
  whatweb --no-errors --url-prefix https:// 192.168.0.0/24
* Scan for crossdomain policies in the Alexa Top 1000.
  ./whatweb -i plugin-development/alexa-top-100.txt \
  --url-suffix /crossdomain.xml -p crossdomain_xml
Learn more with
OffSec
Want to learn more about whatweb? get access to in-depth training and hands-on labs:
PEN-200: 27.1.2. Assembling the Pieces: WEBSRV1
PEN-200 course
Updated on: 2026-May-25
 Edit this page
whatmask
wig
LIGHT
DARK
Links
Home
Download / Get Kali
Blog
OS Documentation
Tool Documentation
System Status
Archived Releases
Partnerships
Platforms
ARM (SBC)
NetHunter (Mobile)
Amazon AWS
Docker
Linode
Microsoft Azure
Microsoft Store (WSL)
Vagrant
Development
Bug Tracker
Continuous Integration
Network Mirror
Package Tracker
GitLab
Community
Discord
Support Forum
PeerTube
Follow Us
Bluesky
Facebook
Instagram
Mastodon
Substack
X
Newsletter
RSS
Policies
Cookie Policy
Privacy Policy
Trademark Policy
© OffSec Services Limited 2026. All rights reserved.
Kali Linux is part of OffSec's Community Projects
Learn more about OffSec's free, open-source penetration testing tools for cybersecurity professionals
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install whatweb`，再执行 `whatweb --version` 2>/dev/null || `whatweb -V`
- [ ] **2.** **读官方帮助** —— `whatweb -h`，需要细节时 `man whatweb`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: whatweb [options] <URLs>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/whatweb/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[whatweb](../../tools/tutorials/01-信息搜集/whatweb.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/whatweb/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/whatweb/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
