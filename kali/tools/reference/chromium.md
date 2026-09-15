# chromium

> Web browser Web browser that aims to build a safer, faster, and more stable internet browsing experience. This package contains the web browser component.

> **功能分类**：通用工具 ｜ **Kali 包**：`chromium` ｜ **官方文档**：<https://www.kali.org/tools/chromium/>

## 1. 安装

```bash
sudo apt update
sudo apt install chromium
```

| 项目 | 内容 |
|------|------|
| 版本 | 150.0.7871.181 |
| 架构 | i386 |
| 可执行命令 | `chromium`、`chromium-common`、`chromium-driver`、`chromedriver`、`chromium-headless-shell`、`chromium-l10n`、`chromium-sandbox`、`chromium-shell` |
| 依赖 | `chromium-common`、`libasound2t64`、`libatk-bridge2.0-0t64`、`libatk1.0-0t64`、`libatspi2.0-0t64`、`libc6`、`libcairo2`、`libcups2t64`、`libdav1d7`、`libdbus-1-3`、`libdouble-conversion3`、`libexpat1` 等 |
| 安装体积 | 300.51 MB |
| 官网 | <http://www.chromium.org/Home> |
| 源码仓库 | <https://salsa.debian.org/chromium-team/chromium> |
| 包追踪 | <https://pkg.kali.org/pkg/chromium> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
chromium -h          # 查看用法
man chromium         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 8 个可执行命令，下面是官方页面内嵌的帮助原文。

### `chromium`

> 官方示例调用：`chromium -h`

```text
root@kali:~# chromium -h
chromium [-h|--help] [-g|--debug] [--temp-profile] [options] [URL]
        -g or --debug              Start within /usr/bin/gdb
        -h or --help               This help screen
        --temp-profile             Start with a new and temporary profile
        --enable-remote-extensions Allow extensions from remote sites
 Other supported options are:
     @@MENUNAME  has hundreds of undocumented command-line flags that are added
     and removed at the whim of the developers.  Here, we  document  relatively
     stable flags.
     -h or --help
            Show help output.
     -g or --debug
            Start a debugging session within /usr/bin/gdb.
     --temp-profile
            Use  a throw-away/temporary profile for this session.  This creates
            an entirely new user profile temporarily.  It is not  the  same  as
            incognito mode.
     --enable-remote-extensions
            Allow installation and updates of remote extensions.
     --user-data-dir=DIR
            Specifies the directory that user data (your "profile") is kept in.
            Defaults  to $HOME/.config/@@PACKAGE .  Separate instances of @@ME-
            NUNAME must use separate user data  directories;  repeated  invoca-
            tions  of @@PACKAGE will reuse an existing process for a given user
            data directory.
     --incognito
            Open in incognito mode.
     --new-window
            If PATH or URL is given, open it in a new window.
     --proxy-server=host:port
            Specify the HTTP/SOCKS4/SOCKS5 proxy server to  use  for  requests.
            This overrides any environment variables or settings picked via the
            options  dialog.  An individual proxy server is specified using the
            format:
              [<proxy-scheme>://]<proxy-host>[:<proxy-port>]
            Where <proxy-scheme> is the protocol of the proxy  server,  and  is
            one of:
              "http", "socks", "socks4", "socks5".
            If  the <proxy-scheme> is omitted, it defaults to "http". Also note
            that "socks" is equivalent to "socks5".
            Examples:
              --proxy-server="foopy:99"
                  Use the HTTP proxy "foopy:99" to load all URLs.
              --proxy-server="socks://foobar:1080"
                  Use the SOCKS v5 proxy "foobar:1080" to load all URLs.
              --proxy-server="socks4://foobar:1080"
                  Use the SOCKS v4 proxy "foobar:1080" to load all URLs.
              --proxy-server="socks5://foobar:66"
                  Use the SOCKS v5 proxy "foobar:66" to load all URLs.
            It is also possible to specify a separate proxy server for  differ-
            ent  URL  types, by prefixing the proxy server specifier with a URL
            specifier:
            Example:
              --proxy-server="https=proxy1:80;http=socks4://baz:1080"
                  Load https://* URLs using the  HTTP  proxy  "proxy1:80".  And
            load http://*
                  URLs using the SOCKS v4 proxy "baz:1080".
     --no-proxy-server
            Disables  the proxy server.  Overrides any environment variables or
            settings picked via the options dialog.
     --proxy-auto-detect
            Autodetect proxy configuration.  Overrides  any  environment  vari-
            ables or settings picked via the options dialog.
     --proxy-pac-url=URL
            Specify  proxy  autoconfiguration  URL.   Overrides any environment
            variables or settings picked via the options dialog.
     --password-store=<basic|gnome|kwallet>
            Set the password store to use.  The default is to automatically de-
            tect based on the desktop environment.  basic selects the built in,
            unencrypted password store.  gnome selects Gnome keyring.   kwallet
            selects  (KDE)  KWallet.   (Note that KWallet may not work reliably
            outside KDE.)
     --version
            Show version information.
     As a GTK+ app, @@MENUNAME also obeys  GTK+  command-line  flags,  such  as
     --display.  See the GTK documentation for more:
            <http://library.gnome.org/devel/gtk/stable/gtk-running.html>
            <http://library.gnome.org/devel/gtk/stable/gtk-x11.html>
 See 'man chromium' for more details
```

### `chromedriver`

> 官方示例调用：`chromedriver -h`

```text
root@kali:~# chromedriver -h
Usage: chromedriver [OPTIONS]
Options
  --port=PORT                     port to listen on
  --adb-port=PORT                 adb server port
  --log-path=FILE                 write server log to file instead of stderr, increases log level to INFO
  --log-level=LEVEL               set log level: ALL, DEBUG, INFO, WARNING, SEVERE, OFF
  --verbose                       log verbosely (equivalent to --log-level=ALL)
  --silent                        log nothing (equivalent to --log-level=OFF)
  --append-log                    append log file instead of rewriting
  --replayable                    (experimental) log verbosely and don't truncate long strings so that the log can be replayed.
  --version                       print the version number and exit
  --url-base                      base URL path prefix for commands, e.g. wd/url
  --readable-timestamp            add readable timestamps to log
  --enable-chrome-logs            show logs from the browser (overrides other logging options)
  --bidi-mapper-path=PATH         custom bidi mapper path
  --disable-dev-shm-usage         do not use /dev/shm (add this switch if seeing errors related to shared memory)
  --ignore-explicit-port          (experimental) ignore the port specified explicitly, find a free port instead
  --allowed-ips=LIST              comma-separated allowlist of remote IP addresses which are allowed to connect to ChromeDriver
  --allowed-origins=LIST          comma-separated allowlist of request origins which are allowed to connect to ChromeDriver. Using `*` to allow any host origin is dangerous!
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install chromium`，再执行 `chromium --version` 2>/dev/null || `chromium -V`
- [ ] **2.** **读官方帮助** —— `chromium -h`，需要细节时 `man chromium`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: chromedriver [OPTIONS]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/chromium/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/chromium/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/chromium/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
