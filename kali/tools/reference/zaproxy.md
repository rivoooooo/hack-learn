# zaproxy

> Testing tool for finding vulnerabilities in web applications The OWASP Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing tool for finding vulnerabilities in web applications. It is designed to be used by people with a…

> **功能分类**：Web 应用 ｜ **Kali 包**：`zaproxy` ｜ **官方文档**：<https://www.kali.org/tools/zaproxy/>

## 1. 安装

```bash
sudo apt update
sudo apt install zaproxy
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.17.0 |
| 架构 | all |
| 可执行命令 | `zaproxy`、`owasp-zap` |
| 依赖 | `default-jre`、`owasp-zap` |
| 安装体积 | 266.90 MB |
| 官网 | <https://github.com/zaproxy/zaproxy> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/zaproxy> |
| 包追踪 | <https://pkg.kali.org/pkg/zaproxy> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Screenshots
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `owasp-zap`

> 官方示例调用：`owasp-zap -h`

```text
root@kali:~# owasp-zap -h
Found Java version 25.0.4
Available memory: 7941 MB
Using JVM args: -Xmx1985m
Usage:
	zap.sh [Options]
Core options:
	-version                 Reports the ZAP version
	-cmd                     Run inline (exits when command line options complete)
	-daemon                  Starts ZAP in daemon mode, i.e. without a UI
	-config <kvpair>         Overrides the specified key=value pair in the configuration file
	-configfile <path>       Overrides the key=value pairs with those in the specified properties file
	-dir <dir>               Uses the specified directory instead of the default one
	-installdir <dir>        Overrides the code that detects where ZAP has been installed with the specified directory
	-h                       Shows all of the command line options available, including those added by add-ons
	-help                    The same as -h
	-newsession <path>       Creates a new session at the given location
	-session <path>          Opens the given session after starting ZAP
	-lowmem                  Use the database instead of memory as much as possible - this is still experimental
	-experimentaldb          Use the experimental generic database code, which is not surprisingly also still experimental
	-nostdout                Disables the default logging through standard output
	-loglevel <level>        Sets the log level, overriding the values specified in the log4j2.properties file in the home directory
	-sbomzip <path>          Creates a zip file containing all of the available SBOMs
	-suppinfo                Reports support info to the command line and exits
	-silent                  Ensures ZAP does not make any unsolicited requests, including check for updates
Add-on options:
	-graphqlfile <path>       Imports a GraphQL Schema from a File
	-graphqlurl <url>         Imports a GraphQL Schema from a URL
	-graphqlendurl <url>      Sets the Endpoint URL
	-script <script>         Run the specified script from commandline or load in GUI
	-postmanfile <path>          Imports a Postman collection from the specified file name.
	-postmanurl <url>            Imports a Postman collection from the specified URL.
	-postmanendpointurl <url>    The endpoint URL, to override the base URLs present in the Postman collection.
	-notel                   Turns off telemetry calls
	-addoninstall <addOnId>   Installs the add-on with specified ID from the ZAP Marketplace
	-addoninstallall          Install all available add-ons from the ZAP Marketplace
	-addonuninstall <addOnId> Uninstalls the Add-on with specified ID
	-addonupdate              Update all changed add-ons from the ZAP Marketplace
	-addonlist                List all of the installed add-ons
	-quickurl <target url>   The URL to attack, e.g. http://www.example.com
	-quickout <filename>     The file to write the HTML/JSON/MD/XML results to (based on the file extension)
	-quickprogress:          Display progress bars while scanning
	-zapit <target url>      The URL to perform a quick 'reconnaissance' scan on, e.g. http://www.example.com The -cmd option must be specified
	-autorun <source>        Run the automation jobs specified in the file or from the URL
	-autogenmin <filename>   Generate template automation file with the key parameters
	-autogenmax <filename>   Generate template automation file with all parameters
	-autogenconf <filename>  Generate template automation file using the current configuration
	-autocheck <source>      Check the specified automation plan in the file or from the URL
	-certload <path>         Loads the Root CA certificate from the specified file name
	-certpubdump <path>      Dumps the Root CA public certificate into the specified file name, this is suitable for importing into browsers
	-certfulldump <path>     Dumps the Root CA full certificate (including the private key) into the specified file name, this is suitable for importing into ZAP
	-host <host>             Overrides the host of the main proxy, specified in the configuration file
	-port <port>             Overrides the port of the main proxy, specified in the configuration file
	-hud                     Launches a browser configured to proxy through ZAP with the HUD enabled, for use in daemon mode
	-hudurl <url>            Launches a browser as per the -hud option with the specified URL
	-hudbrowser <browser>    Launches a browser as per the -hud option with the specified browser, supported options: Chrome, Firefox by default Firefox
	-openapifile <path>      Imports an OpenAPI definition from the specified file name
	-openapiurl <url>        Imports an OpenAPI definition from the specified URL
	-openapitargeturl <url>  The Target URL, to override the server URL present in the OpenAPI definition. Refer to the help for supported format.
```

### `zaproxy`

> 官方示例调用：`zaproxy -h`

```text
root@kali:~# zaproxy -h
Found Java version 25.0.4
Available memory: 7941 MB
Using JVM args: -Xmx1985m
Usage:
	zap.sh [Options]
Core options:
	-version                 Reports the ZAP version
	-cmd                     Run inline (exits when command line options complete)
	-daemon                  Starts ZAP in daemon mode, i.e. without a UI
	-config <kvpair>         Overrides the specified key=value pair in the configuration file
	-configfile <path>       Overrides the key=value pairs with those in the specified properties file
	-dir <dir>               Uses the specified directory instead of the default one
	-installdir <dir>        Overrides the code that detects where ZAP has been installed with the specified directory
	-h                       Shows all of the command line options available, including those added by add-ons
	-help                    The same as -h
	-newsession <path>       Creates a new session at the given location
	-session <path>          Opens the given session after starting ZAP
	-lowmem                  Use the database instead of memory as much as possible - this is still experimental
	-experimentaldb          Use the experimental generic database code, which is not surprisingly also still experimental
	-nostdout                Disables the default logging through standard output
	-loglevel <level>        Sets the log level, overriding the values specified in the log4j2.properties file in the home directory
	-sbomzip <path>          Creates a zip file containing all of the available SBOMs
	-suppinfo                Reports support info to the command line and exits
	-silent                  Ensures ZAP does not make any unsolicited requests, including check for updates
Add-on options:
	-openapifile <path>      Imports an OpenAPI definition from the specified file name
	-openapiurl <url>        Imports an OpenAPI definition from the specified URL
	-openapitargeturl <url>  The Target URL, to override the server URL present in the OpenAPI definition. Refer to the help for supported format.
	-hud                     Launches a browser configured to proxy through ZAP with the HUD enabled, for use in daemon mode
	-hudurl <url>            Launches a browser as per the -hud option with the specified URL
	-hudbrowser <browser>    Launches a browser as per the -hud option with the specified browser, supported options: Chrome, Firefox by default Firefox
	-certload <path>         Loads the Root CA certificate from the specified file name
	-certpubdump <path>      Dumps the Root CA public certificate into the specified file name, this is suitable for importing into browsers
	-certfulldump <path>     Dumps the Root CA full certificate (including the private key) into the specified file name, this is suitable for importing into ZAP
	-host <host>             Overrides the host of the main proxy, specified in the configuration file
	-port <port>             Overrides the port of the main proxy, specified in the configuration file
	-addoninstall <addOnId>   Installs the add-on with specified ID from the ZAP Marketplace
	-addoninstallall          Install all available add-ons from the ZAP Marketplace
	-addonuninstall <addOnId> Uninstalls the Add-on with specified ID
	-addonupdate              Update all changed add-ons from the ZAP Marketplace
	-addonlist                List all of the installed add-ons
	-notel                   Turns off telemetry calls
	-postmanfile <path>          Imports a Postman collection from the specified file name.
	-postmanurl <url>            Imports a Postman collection from the specified URL.
	-postmanendpointurl <url>    The endpoint URL, to override the base URLs present in the Postman collection.
	-quickurl <target url>   The URL to attack, e.g. http://www.example.com
	-quickout <filename>     The file to write the HTML/JSON/MD/XML results to (based on the file extension)
	-quickprogress:          Display progress bars while scanning
	-zapit <target url>      The URL to perform a quick 'reconnaissance' scan on, e.g. http://www.example.com The -cmd option must be specified
	-autorun <source>        Run the automation jobs specified in the file or from the URL
	-autogenmin <filename>   Generate template automation file with the key parameters
	-autogenmax <filename>   Generate template automation file with all parameters
	-autogenconf <filename>  Generate template automation file using the current configuration
	-autocheck <source>      Check the specified automation plan in the file or from the URL
	-script <script>         Run the specified script from commandline or load in GUI
	-graphqlfile <path>       Imports a GraphQL Schema from a File
	-graphqlurl <url>         Imports a GraphQL Schema from a URL
	-graphqlendurl <url>      Sets the Endpoint URL
Updated on: 2026-Aug-25
 Edit this page
yersinia
zsh
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install zaproxy`，再执行 `zaproxy --version` 2>/dev/null || `zaproxy -V`
- [ ] **2.** **读官方帮助** —— `zaproxy -h`，需要细节时 `man zaproxy`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/zaproxy/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[zaproxy](../../tools/tutorials/03-Web应用/zaproxy.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/zaproxy/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/zaproxy/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
