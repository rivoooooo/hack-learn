# wsgidav

> root@kali:~# wsgidav -h usage: wsgidav [-h] [-p PORT] [-H HOST] [-r ROOT_PATH] [--auth {anonymous,nt,pam-login}] [--server {cheroot,ext-wsgiutils,gevent,gunicorn,paste,uvicorn,wsgiref}] [--ssl-adapter {builtin,pyopenssl}] [-v | -q] [-c CON…

> **功能分类**：通用工具 ｜ **Kali 包**：`wsgidav` ｜ **官方文档**：<https://www.kali.org/tools/wsgidav/>

## 1. 安装

```bash
sudo apt update
sudo apt install wsgidav
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.3.5 |
| 架构 | all |
| 可执行命令 | `python-wsgidav-doc`、`python3-wsgidav`、`wsgidav` |
| 官网 | <https://github.com/mar10/wsgidav> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/wsgidav> |
| 包追踪 | <https://pkg.kali.org/pkg/wsgidav> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
python-wsgidav-doc -h          # 查看用法
man python-wsgidav-doc         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wsgidav`

> 官方示例调用：`wsgidav -h`

```text
root@kali:~# wsgidav -h
usage: wsgidav [-h] [-p PORT] [-H HOST] [-r ROOT_PATH]
               [--auth {anonymous,nt,pam-login}]
               [--server {cheroot,ext-wsgiutils,gevent,gunicorn,paste,uvicorn,wsgiref}]
               [--ssl-adapter {builtin,pyopenssl}] [-v | -q] [-c CONFIG_FILE |
               --no-config] [--browse] [-V]
Run a WEBDAV server to share file system folders.
Examples:
  Share filesystem folder '/temp' for anonymous access (no config file used):
    wsgidav --port=80 --host=0.0.0.0 --root=/temp --auth=anonymous
  Run using a specific configuration file:
    wsgidav --port=80 --host=0.0.0.0 --config=~/my_wsgidav.yaml
  If no config file is specified, the application will look for a file named
  'wsgidav.yaml' in the current directory.
  See
    https://wsgidav.readthedocs.io/en/latest/user_guide_configure.html
  for some explanation of the configuration file format.
options:
  -h, --help            show this help message and exit
  -p, --port PORT       port to serve on (default: 8080)
  -H, --host HOST       host to serve from (default: localhost). 'localhost' is only accessible from the local computer. Use 0.0.0.0 to make your application public
  -r, --root ROOT_PATH  path to a file system folder to publish for RW as share '/'.
  --auth {anonymous,nt,pam-login}
                        quick configuration of a domain controller when no config file is used
  --server {cheroot,ext-wsgiutils,gevent,gunicorn,paste,uvicorn,wsgiref}
                        type of pre-installed WSGI server to use (default: cheroot).
  --ssl-adapter {builtin,pyopenssl}
                        used by 'cheroot' server if SSL certificates are configured (default: builtin).
  -v, --verbose         increment verbosity by one (default: 3, range: 0..5)
  -q, --quiet           decrement verbosity by one
  -c, --config CONFIG_FILE
                        configuration file (default: ('wsgidav.yaml', 'wsgidav.json') in current directory)
  --no-config           do not try to load default ('wsgidav.yaml', 'wsgidav.json')
  --browse              open browser on start
  -V, --version         print version info and exit (may be combined with --verbose)
Licensed under the MIT license.
See https://github.com/mar10/wsgidav for additional information.
Learn more with
OffSec
Want to learn more about wsgidav? get access to in-depth training and hands-on labs:
PEN-200: 12.3.1. Client-side Attacks: Obtaining Code Execution via Windows Library Files
PEN-200 course
Updated on: 2026-Aug-25
 Edit this page
wpscan
xmount
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install wsgidav`，再执行 `python-wsgidav-doc --version` 2>/dev/null || `python-wsgidav-doc -V`
- [ ] **2.** **读官方帮助** —— `python-wsgidav-doc -h`，需要细节时 `man python-wsgidav-doc`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `python-wsgidav-doc -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wsgidav/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wsgidav/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wsgidav/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
