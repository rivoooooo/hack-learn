# python-virtualenv

> Python virtual environment creator virtualenv is a tool to create isolated Python environments, each invokable with its own Python executable. Each instance can have different sets of modules, installable via pip. Virtual Python instances …

> **功能分类**：通用工具 ｜ **Kali 包**：`python-virtualenv` ｜ **官方文档**：<https://www.kali.org/tools/python-virtualenv/>

## 1. 安装

```bash
sudo apt update
sudo apt install python3-virtualenv
```

| 项目 | 内容 |
|------|------|
| 版本 | 21.5.1 |
| 架构 | all |
| 可执行命令 | `python3-virtualenv`、`virtualenv` |
| 依赖 | `python3`、`python3-discovery`、`python3-distlib`、`python3-filelock`、`python3-pip-whl`、`python3-platformdirs`、`python3-setuptools-whl`、`virtualenv` |
| 安装体积 | 374 KB |
| 官网 | <https://virtualenv.pypa.io/> |
| 源码仓库 | <https://salsa.debian.org/python-team/packages/python-virtualenv> |
| 包追踪 | <https://pkg.kali.org/pkg/python-virtualenv> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
python3-virtualenv -h          # 查看用法
man python3-virtualenv         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `virtualenv`

官方给出的调用示例：`virtualenv -h`

```text
root@kali:~# virtualenv -h
usage: virtualenv [--version] [--with-traceback] [-v | -q]
                  [--read-only-app-data] [--app-data APP_DATA]
                  [--reset-app-data] [--upgrade-embed-wheels]
                  [--discovery {builtin}] [-p py] [--try-first-with py_exe]
                  [--creator {builtin,cpython3-posix,venv}]
                  [--seeder {app-data,pip}] [--no-seed]
                  [--activators comma_sep_list] [--clear] [--no-vcs-ignore]
                  [--system-site-packages] [--symlinks | --copies]
                  [--no-download | --download] [--extra-search-dir d [d ...]]
                  [--pip version] [--setuptools version] [--no-pip]
                  [--no-setuptools] [--no-periodic-update] [--symlink-app-data]
                  [--prompt prompt] [-h]
                  dest
options:
  --version                     display the version of the virtualenv package
                                and its location, then exit
  --with-traceback              on failure also display the stacktrace internals
                                of virtualenv (default: False)
  --read-only-app-data          use app data folder in read-only mode (write
                                operations will fail with error) (default:
                                False)
  --app-data APP_DATA           a data folder used as cache by the virtualenv
                                (default: /root/.cache/virtualenv)
  --reset-app-data              start with empty app data folder (default:
                                False)
  --upgrade-embed-wheels        trigger a manual update of the embedded wheels
                                (default: False)
  -h, --help                    show this help message and exit
verbosity:
  verbosity = verbose - quiet, default INFO, mapping => CRITICAL=0, ERROR=1,
  WARNING=2, INFO=3, DEBUG=4, NOTSET=5
  -v, --verbose                 increase verbosity (default: 2)
  -q, --quiet                   decrease verbosity (default: 0)
discovery:
  discover and provide a target interpreter
  --discovery {builtin}         interpreter discovery method (default: builtin)
  -p, --python py               interpreter based on what to create environment
                                (path/identifier/version-specifier) - by default
                                use the interpreter where the tool is installed
                                - first found wins. Version specifiers (e.g.,
                                >=3.12, ~=3.11.0, ==3.10) are also supported
                                (default: [])
  --try-first-with py_exe       try first these interpreters before starting the
                                discovery (default: [])
creator:
  options for creator builtin
  --creator {builtin,cpython3-posix,venv}
                                create environment via (builtin =
                                cpython3-posix) (default: builtin)
  dest                          directory to create virtualenv at
  --clear                       remove the destination directory if exist before
                                starting (will overwrite files otherwise)
                                (default: False)
  --no-vcs-ignore               don't create VCS ignore directive in the
                                destination directory (default: False)
  --system-site-packages        give the virtual environment access to the
                                system site-packages dir (default: False)
  --symlinks                    try to use symlinks rather than copies, when
                                symlinks are not the default for the platform
                                (default: True)
  --copies, --always-copy       try to use copies rather than symlinks, even
                                when symlinks are the default for the platform
                                (default: False)
seeder:
  options for seeder app-data
  --seeder {app-data,pip}       seed packages install method (default: app-data)
  --no-seed, --without-pip      do not install seed packages (default: False)
  --no-download, --never-download
                                pass to disable download of the latest
                                pip/setuptools/wheel from PyPI (default: True)
  --download                    pass to enable download of the latest
                                pip/setuptools/wheel from PyPI (default: False)
  --extra-search-dir d [d ...]  a path containing wheels to extend the internal
                                wheel list (can be set 1+ times) (default: [])
  --pip version                 version of pip to install as seed: embed,
                                bundle, none or exact version (default: bundle)
  --setuptools version          version of setuptools to install as seed: embed,
                                bundle, none or exact version (default: none)
  --no-pip                      do not install pip (default: False)
  --no-setuptools               do not install setuptools (default: False)
  --no-periodic-update          disable the periodic (once every 14 days) update
                                of the embedded wheels (default: True)
  --symlink-app-data            symlink the python packages from the app-data
                                folder (requires seed pip>=19.3) (default:
                                False)
activators:
  options for activation scripts
  --activators comma_sep_list   activators to generate - default is all
                                supported (default: bash,cshell,fish,nushell,pow
                                ershell,python,xonsh)
  --prompt prompt               provides an alternative prompt prefix for this
                                environment (value of . means name of the
                                current working directory) (default: None)
config file /root/.config/virtualenv/virtualenv.ini missing (change via env var
VIRTUALENV_CONFIG_FILE)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install python3-virtualenv`，再执行 `python3-virtualenv --version` 2>/dev/null || `python3-virtualenv -V`
- [ ] **2.** **读官方帮助** —— `python3-virtualenv -h`，需要细节时 `man python3-virtualenv`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `python3-virtualenv -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/python-virtualenv/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/python-virtualenv/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/python-virtualenv/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
