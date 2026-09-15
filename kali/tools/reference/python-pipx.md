# python-pipx

> Execute binaries from Python packages in isolated environments pipx allows you to… Run the latest version of a CLI application from a package in a temporary virtual environment, leaving your system untouched after it finishes. Install pack…

> **功能分类**：通用工具 ｜ **Kali 包**：`python-pipx` ｜ **官方文档**：<https://www.kali.org/tools/python-pipx/>

## 1. 安装

```bash
sudo apt update
sudo apt install pipx
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.15.0 |
| 架构 | all |
| 可执行命令 | `pipx` |
| 依赖 | `python3`、`python3-argcomplete`、`python3-packaging`、`python3-platformdirs`、`python3-userpath`、`python3-venv`、`pipx` |
| 安装体积 | 4.30 MB |
| 官网 | <https://github.com/pypa/pipx> |
| 源码仓库 | <https://salsa.debian.org/python-team/packages/python-pipx> |
| 包追踪 | <https://pkg.kali.org/pkg/python-pipx> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
pipx -h          # 查看用法
man pipx         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pipx`

官方给出的调用示例：`pipx -h`

```text
root@kali:~# pipx -h
usage: pipx [-h] [--version]
            {install,install-all,uninject,inject,pin,unpin,upgrade,upgrade-all,upgrade-shared,uninstall,uninstall-all,reinstall,reinstall-all,list,interpreter,run,runpip,ensurepath,environment,completions,help} ...
Install and execute apps from Python packages.
Binaries can either be installed globally into isolated Virtual Environments
or run directly in a temporary Virtual Environment.
Virtual Environment location is /root/.local/share/pipx/venvs.
Symlinks to apps are placed in /root/.local/bin.
Symlinks to manual pages are placed in /root/.local/share/man.
optional environment variables:
  PIPX_HOME              Overrides default pipx location. Virtual Environments
                        will be installed to $PIPX_HOME/venvs.
  PIPX_GLOBAL_HOME       Used instead of PIPX_HOME when the `--global` option
                        is given.
  PIPX_BIN_DIR           Overrides location of app installations. Apps are
                        symlinked or copied here.
  PIPX_GLOBAL_BIN_DIR    Used instead of PIPX_BIN_DIR when the `--global`
                        option is given.
  PIPX_MAN_DIR           Overrides location of manual pages installations.
                        Manual pages are symlinked or copied here.
  PIPX_GLOBAL_MAN_DIR    Used instead of PIPX_MAN_DIR when the `--global`
                        option is given.
  PIPX_DEFAULT_PYTHON    Overrides default python used for commands.
  PIPX_DEFAULT_BACKEND   Overrides which backend (`pip` or `uv`) is used for
                        new venvs.
  PIPX_DISABLE_SHARED_LIBS_AUTO_UPGRADE
                        Skips automatic shared library upgrades.
  PIPX_USE_EMOJI         Overrides emoji behavior. Default value varies based
                        on platform.
  PIPX_HOME_ALLOW_SPACE  Overrides default warning on spaces in the home path
options:
  -h, --help            show this help message and exit
  --version             Print version and exit
subcommands:
  Get help for commands with pipx COMMAND --help
  {install,install-all,uninject,inject,pin,unpin,upgrade,upgrade-all,upgrade-shared,uninstall,uninstall-all,reinstall,reinstall-all,list,interpreter,run,runpip,ensurepath,environment,completions,help}
    install             Install a package
    install-all         Install all packages
    uninject            Uninstall injected packages from an existing Virtual
                        Environment
    inject              Install packages into an existing Virtual Environment
    pin                 Pin the specified package to prevent it from being
                        upgraded
    unpin               Unpin the specified package
    upgrade             Upgrade a package
    upgrade-all         Upgrade all packages. Runs `pip install -U <pkgname>`
                        for each package.
    upgrade-shared      Upgrade shared libraries.
    uninstall           Uninstall a package
    uninstall-all       Uninstall all packages
    reinstall           Reinstall a package
    reinstall-all       Reinstall all packages
    list                List installed packages
    interpreter         Interact with interpreters managed by pipx
    run                 Download the latest version of a package to a
                        temporary virtual environment, then run an app from
                        it. Also compatible with local `__pypackages__`
                        directory (experimental).
    runpip              Run pip in an existing pipx-managed Virtual
                        Environment
    ensurepath          Ensure directories necessary for pipx operation are in
                        your PATH environment variable.
    environment         Print a list of environment variables and paths used
                        by pipx.
    completions         Print instructions on enabling shell completions for
                        pipx
    help                Show help for pipx or a command
Updated on: 2026-Aug-25
 Edit this page
python-pip
python-virtualenv
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install pipx`，再执行 `pipx --version` 2>/dev/null || `pipx -V`
- [ ] **2.** **读官方帮助** —— `pipx -h`，需要细节时 `man pipx`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `pipx -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/python-pipx/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/python-pipx/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/python-pipx/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
