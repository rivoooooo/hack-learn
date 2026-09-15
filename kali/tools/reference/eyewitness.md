# eyewitness

> Rapid web application triage tool EyeWitness is designed to take screenshots of websites, provide some server header info, and identify default credentials if possible. Inspiration came from Tim Tomes’s PeepingTom Script. EyeWitness is des…

> **功能分类**：信息搜集 ｜ **Kali 包**：`eyewitness` ｜ **官方文档**：<https://www.kali.org/tools/eyewitness/>

## 1. 安装

```bash
sudo apt update
sudo apt install eyewitness
```

| 项目 | 内容 |
|------|------|
| 版本 | 20230525.1 |
| 架构 | amd64 |
| 可执行命令 | `eyewitness`、`geckodriver` |
| 安装体积 | 5.78 MB |
| 官网 | <https://www.christophertruncer.com/eyewitness-triage-tool/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/eyewitness> |
| 包追踪 | <https://pkg.kali.org/pkg/eyewitness> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
Take a screenshot of each of the websites listed in the provided file using headless mode:
root@kali:~# cat urls.txt
https://www.kali.org
https://www.kali.org/docs
https://www.kali.org/tools
https://www.exploit-db.com
https://www.offsec.com

root@kali:~# eyewitness -f /root/urls.txt -d screens --headless

################################################################################
#                                  EyeWitness                                  #
################################################################################

Starting Web Requests (5 Hosts)
Attempting to screenshot https://www.kali.org
Attempting to screenshot https://www.kali.org/docs
Attempting to screenshot https://www.kali.org/tools
Attempting to screenshot https://www.exploit-db.com
Attempting to screenshot https://www.offsec.com
Finished in 14.1417660713 seconds

[*] Done! Report written in the /usr/share/eyewitness/screens folder!
Would you like to open the report now? [Y/n] Y
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cat`

> 官方示例调用：`cat urls.txt`

```text
root@kali:~# cat urls.txt
https://www.kali.org
https://www.kali.org/docs
https://www.kali.org/tools
https://www.exploit-db.com
https://www.offsec.com
```

### `eyewitness`

> 官方示例调用：`eyewitness -f /root/urls.txt -d screens --headless`

```text
root@kali:~# eyewitness -f /root/urls.txt -d screens --headless
################################################################################
#                                  EyeWitness                                  #
################################################################################
Starting Web Requests (5 Hosts)
Attempting to screenshot https://www.kali.org
Attempting to screenshot https://www.kali.org/docs
Attempting to screenshot https://www.kali.org/tools
Attempting to screenshot https://www.exploit-db.com
Attempting to screenshot https://www.offsec.com
Finished in 14.1417660713 seconds
[*] Done! Report written in the /usr/share/eyewitness/screens folder!
Would you like to open the report now? [Y/n] Y
```

### `eyewitness -h`

> 官方示例调用：`eyewitness -h`

```text
root@kali:~# eyewitness -h
################################################################################
#                                  EyeWitness                                  #
################################################################################
#           Red Siege Information Security - https://www.redsiege.com           #
################################################################################
usage: EyeWitness.py [--web] [-f Filename] [-x Filename.xml]
                     [--single Single URL] [--no-dns] [--timeout Timeout]
                     [--jitter # of Seconds] [--delay # of Seconds]
                     [--threads # of Threads]
                     [--max-retries Max retries on a timeout]
                     [-d Directory Name] [--results Hosts Per Page]
                     [--no-prompt] [--user-agent User Agent]
                     [--difference Difference Threshold]
                     [--proxy-ip 127.0.0.1] [--proxy-port 8080]
                     [--proxy-type socks5] [--show-selenium] [--resolve]
                     [--add-http-ports ADD_HTTP_PORTS]
                     [--add-https-ports ADD_HTTPS_PORTS]
                     [--only-ports ONLY_PORTS] [--prepend-https]
                     [--selenium-log-path SELENIUM_LOG_PATH]
                     [--cookies key1=value1,key2=value2] [--resume ew.db]
EyeWitness is a tool used to capture screenshots from a list of URLs
Protocols:
  --web                 HTTP Screenshot using Selenium
Input Options:
  -f Filename           Line-separated file containing URLs to capture
  -x Filename.xml       Nmap XML or .Nessus file
  --single Single URL   Single URL/Host to capture
  --no-dns              Skip DNS resolution when connecting to websites
Timing Options:
  --timeout Timeout     Maximum number of seconds to wait while requesting a
                        web page (Default: 7)
  --jitter # of Seconds
                        Randomize URLs and add a random delay between requests
  --delay # of Seconds  Delay between the opening of the navigator and taking
                        the screenshot
  --threads # of Threads
                        Number of threads to use while using file based input
  --max-retries Max retries on a timeout
                        Max retries on timeouts
Report Output Options:
  -d Directory Name     Directory name for report output
  --results Hosts Per Page
                        Number of Hosts per page of report
  --no-prompt           Don't prompt to open the report
Web Options:
  --user-agent User Agent
                        User Agent to use for all requests
  --difference Difference Threshold
                        Difference threshold when determining if user agent
                        requests are close "enough" (Default: 50)
  --proxy-ip 127.0.0.1  IP of web proxy to go through
  --proxy-port 8080     Port of web proxy to go through
  --proxy-type socks5   Proxy type (socks5/http)
  --show-selenium       Show display for selenium
  --resolve             Resolve IP/Hostname for targets
  --add-http-ports ADD_HTTP_PORTS
                        Comma-separated additional port(s) to assume are http
                        (e.g. '8018,8028')
  --add-https-ports ADD_HTTPS_PORTS
                        Comma-separated additional port(s) to assume are https
                        (e.g. '8018,8028')
  --only-ports ONLY_PORTS
                        Comma-separated list of exclusive ports to use (e.g.
                        '80,8080')
  --prepend-https       Prepend http:// and https:// to URLs without either
  --selenium-log-path SELENIUM_LOG_PATH
                        Selenium geckodriver log path
  --cookies key1=value1,key2=value2
                        Additional cookies to add to the request
Resume Options:
  --resume ew.db        Path to db file if you want to resume
```

### `geckodriver`

> 官方示例调用：`geckodriver -h`

```text
root@kali:~# geckodriver -h
geckodriver 0.33.0 (a80e5fd61076 2023-04-02 18:31 +0000)
WebDriver implementation for Firefox
USAGE:
    geckodriver [OPTIONS]
OPTIONS:
        --allow-hosts <ALLOW_HOSTS>...
            List of hostnames to allow. By default the value of --host is allowed, and in addition
            if that's a well known local address, other variations on well known local addresses are
            allowed. If --allow-hosts is provided only exactly those hosts are allowed.
        --allow-origins <ALLOW_ORIGINS>...
            List of request origins to allow. These must be formatted as scheme://host:port. By
            default any request with an origin header is rejected. If --allow-origins is provided
            then only exactly those origins are allowed.
        --android-storage <ANDROID_STORAGE>
            Selects storage location to be used for test data (deprecated). [possible values: auto,
            app, internal, sdcard]
    -b, --binary <BINARY>
            Path to the Firefox binary
        --connect-existing
            Connect to an existing Firefox instance
    -h, --help
            Prints this message
        --host <HOST>
            Host IP to use for WebDriver server [default: 127.0.0.1]
        --jsdebugger
            Attach browser toolbox debugger for Firefox
        --log <LEVEL>
            Set Gecko log level [possible values: fatal, error, warn, info, config, debug, trace]
        --log-no-truncate
            Disable truncation of long log lines
        --marionette-host <HOST>
            Host to use to connect to Gecko [default: 127.0.0.1]
        --marionette-port <PORT>
            Port to use to connect to Gecko [default: system-allocated port]
    -p, --port <PORT>
            Port to use for WebDriver server [default: 4444]
        --profile-root <PROFILE_ROOT>
            Directory in which to create profiles. Defaults to the system temporary directory.
    -v
            Log level verbosity (-v for debug and -vv for trace level)
    -V, --version
            Prints version and copying information
        --websocket-port <PORT>
            Port to use to connect to WebDriver BiDi [default: 9222]
Updated on: 2025-Dec-09
 Edit this page
extundelete
faraday-agent-dispatcher
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install eyewitness`，再执行 `eyewitness --version` 2>/dev/null || `eyewitness -V`
- [ ] **2.** **读官方帮助** —— `eyewitness -h`，需要细节时 `man eyewitness`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `eyewitness -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/eyewitness/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/eyewitness/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/eyewitness/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
