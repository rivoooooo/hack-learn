# pyinstaller

> Utility to bundle a Python application into a single package PyInstaller reads a Python script written by you. It analyzes your code to discover every other module and library your script needs in order to execute. Then it collects copies …

> **功能分类**：通用工具 ｜ **Kali 包**：`pyinstaller` ｜ **官方文档**：<https://www.kali.org/tools/pyinstaller/>

## 1. 安装

```bash
sudo apt update
sudo apt install pyinstaller
```

| 项目 | 内容 |
|------|------|
| 版本 | 6.19.0 |
| 架构 | any |
| 可执行命令 | `pyinstaller`、`pyi-archive_viewer`、`pyi-bindepend`、`pyi-grab_version`、`pyi-makespec`、`pyi-set_version`、`python3-pyinstaller` |
| 依赖 | `python3`、`python3-pyinstaller`、`pyi-archive_viewer` |
| 安装体积 | 104 KB |
| 官网 | <https://pyinstaller.org/en/stable/> |
| 源码仓库 | <https://salsa.debian.org/python-team/packages/pyinstaller> |
| 包追踪 | <https://pkg.kali.org/pkg/pyinstaller> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
pyinstaller -h          # 查看用法
man pyinstaller         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 7 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pyi-archive_viewer`

官方给出的调用示例：`pyi-archive_viewer -h`

```text
root@kali:~# pyi-archive_viewer -h
usage: pyi-archive_viewer [-h] [-l] [-r] [-b] [--log-level LEVEL] pyi_archive
positional arguments:
  pyi_archive        PyInstaller archive to process.
options:
  -h, --help         show this help message and exit
  -l, --list         List the archive contents and exit (default: False).
  -r, --recursive    Recursively print an archive log (default: False).
                     Implies --list.
  -b, --brief        When displaying archive contents, show only file names.
                     (default: False).
  --log-level LEVEL  Amount of detail in build-time console messages. LEVEL
                     may be one of TRACE, DEBUG, INFO, WARN, DEPRECATION,
                     ERROR, FATAL (default: INFO). Also settable via and
                     overrides the PYI_LOG_LEVEL environment variable.
```

### `pyi-bindepend`

官方给出的调用示例：`pyi-bindepend -h`

```text
root@kali:~# pyi-bindepend -h
usage: pyi-bindepend [-h] [--log-level LEVEL]
                     executable-or-dynamic-library [executable-or-dynamic-library ...]
positional arguments:
  executable-or-dynamic-library
                        executables or dynamic libraries for which the
                        dependencies should be shown
options:
  -h, --help            show this help message and exit
  --log-level LEVEL     Amount of detail in build-time console messages. LEVEL
                        may be one of TRACE, DEBUG, INFO, WARN, DEPRECATION,
                        ERROR, FATAL (default: INFO). Also settable via and
                        overrides the PYI_LOG_LEVEL environment variable.
```

### `pyi-grab_version`

官方给出的调用示例：`pyi-grab_version -h`

```text
root@kali:~# pyi-grab_version -h
usage: pyi-grab_version [-h] exe-file [out-filename]
positional arguments:
  exe-file      full pathname of a Windows executable
  out-filename  filename where the grabbed version info will be saved
options:
  -h, --help    show this help message and exit
The printed output may be saved to a file, edited and used as the input for a
version resource on any of the executable targets in a PyInstaller .spec file.
```

### `pyi-makespec`

官方给出的调用示例：`pyi-makespec -h`

```text
root@kali:~# pyi-makespec -h
usage: pyi-makespec [-h] [-D] [-F] [--specpath DIR] [-n NAME]
                    [--contents-directory CONTENTS_DIRECTORY]
                    [--add-data SOURCE:DEST] [--add-binary SOURCE:DEST]
                    [-p DIR] [--hidden-import MODULENAME]
                    [--collect-submodules MODULENAME]
                    [--collect-data MODULENAME]
                    [--collect-binaries MODULENAME] [--collect-all MODULENAME]
                    [--copy-metadata PACKAGENAME]
                    [--recursive-copy-metadata PACKAGENAME]
                    [--additional-hooks-dir HOOKSPATH]
                    [--runtime-hook RUNTIME_HOOKS] [--exclude-module EXCLUDES]
                    [--splash IMAGE_FILE]
                    [-d {all,imports,bootloader,noarchive}] [--optimize LEVEL]
                    [--python-option PYTHON_OPTION] [-s] [--noupx]
                    [--upx-exclude FILE] [-c] [-w]
                    [--hide-console {hide-early,minimize-late,minimize-early,hide-late}]
                    [-i <FILE.ico or FILE.exe,ID or FILE.icns or Image or "NONE">]
                    [--disable-windowed-traceback] [--version-file FILE]
                    [--manifest <FILE or XML>] [-m <FILE or XML>]
                    [-r RESOURCE] [--uac-admin] [--uac-uiaccess]
                    [--argv-emulation]
                    [--osx-bundle-identifier BUNDLE_IDENTIFIER]
                    [--target-architecture ARCH]
                    [--codesign-identity IDENTITY]
                    [--osx-entitlements-file FILENAME] [--runtime-tmpdir PATH]
                    [--bootloader-ignore-signals] [--log-level LEVEL]
                    scriptname [scriptname ...]
positional arguments:
  scriptname
options:
  -h, --help            show this help message and exit
  --log-level LEVEL     Amount of detail in build-time console messages. LEVEL
                        may be one of TRACE, DEBUG, INFO, WARN, DEPRECATION,
                        ERROR, FATAL (default: INFO). Also settable via and
                        overrides the PYI_LOG_LEVEL environment variable.
What to generate:
  -D, --onedir          Create a one-folder bundle containing an executable
                        (default)
  -F, --onefile         Create a one-file bundled executable.
  --specpath DIR        Folder to store the generated spec file (default:
                        current directory)
  -n, --name NAME       Name to assign to the bundled app and spec file
                        (default: first script's basename)
  --contents-directory CONTENTS_DIRECTORY
                        For onedir builds only, specify the name of the
                        directory in which all supporting files (i.e.
                        everything except the executable itself) will be
                        placed in. Use "." to re-enable old onedir layout
                        without contents directory.
What to bundle, where to search:
  --add-data SOURCE:DEST
                        Additional data files or directories containing data
                        files to be added to the application. The argument
                        value should be in form of "source:dest_dir", where
                        source is the path to file (or directory) to be
                        collected, dest_dir is the destination directory
                        relative to the top-level application directory, and
                        both paths are separated by a colon (:). To put a file
                        in the top-level application directory, use . as a
                        dest_dir. This option can be used multiple times.
  --add-binary SOURCE:DEST
                        Additional binary files to be added to the executable.
                        See the ``--add-data`` option for the format. This
                        option can be used multiple times.
  -p, --paths DIR       A path to search for imports (like using PYTHONPATH).
                        Multiple paths are allowed, separated by ``':'``, or
                        use this option multiple times. Equivalent to
                        supplying the ``pathex`` argument in the spec file.
  --hidden-import, --hiddenimport MODULENAME
                        Name an import not visible in the code of the
                        script(s). This option can be used multiple times.
  --collect-submodules MODULENAME
                        Collect all submodules from the specified package or
                        module. This option can be used multiple times.
  --collect-data, --collect-datas MODULENAME
                        Collect all data from the specified package or module.
                        This option can be used multiple times.
  --collect-binaries MODULENAME
                        Collect all binaries from the specified package or
                        module. This option can be used multiple times.
  --collect-all MODULENAME
                        Collect all submodules, data files, and binaries from
                        the specified package or module. This option can be
                        used multiple times.
  --copy-metadata PACKAGENAME
                        Copy metadata for the specified package. This option
                        can be used multiple times.
  --recursive-copy-metadata PACKAGENAME
                        Copy metadata for the specified package and all its
                        dependencies. This option can be used multiple times.
  --additional-hooks-dir HOOKSPATH
                        An additional path to search for hooks. This option
                        can be used multiple times.
  --runtime-hook RUNTIME_HOOKS
                        Path to a custom runtime hook file. A runtime hook is
                        code that is bundled with the executable and is
                        executed before any other code or module to set up
                        special features of the runtime environment. This
                        option can be used multiple times.
  --exclude-module EXCLUDES
                        Optional module or package (the Python name, not the
                        path name) that will be ignored (as though it was not
                        found). This option can be used multiple times.
  --splash IMAGE_FILE   (EXPERIMENTAL) Add an splash screen with the image
                        IMAGE_FILE to the application. The splash screen can
                        display progress updates while unpacking.
How to generate:
  -d, --debug {all,imports,bootloader,noarchive}
                        R|Provide assistance with debugging a frozen
                        application. This argument may be provided multiple
                        times to select several of the following options. -
                        all: All three of the following options. - imports:
                        specify the -v option to the underlying Python
                        interpreter, causing it to print a message each time a
                        module is initialized, showing the place (filename or
                        built-in module) from which it is loaded. See
                        https://docs.python.org/3/using/cmdline.html#id4. -
                        bootloader: tell the bootloader to issue progress
                        messages while initializing and starting the bundled
                        app. Used to diagnose problems with missing imports. -
                        noarchive: instead of storing all frozen Python source
                        files as an archive inside the resulting executable,
                        store them as files in the resulting output directory.
  --optimize LEVEL      Bytecode optimization level used for collected python
                        modules and scripts. For details, see the section
                        “Bytecode Optimization Level” in PyInstaller manual.
  --python-option PYTHON_OPTION
                        Specify a command-line option to pass to the Python
                        interpreter at runtime. Currently supports "v"
                        (equivalent to "--debug imports"), "u", "W <warning
                        control>", "X <xoption>", and "hash_seed=<value>". For
                        details, see the section "Specifying Python
                        Interpreter Options" in PyInstaller manual.
  -s, --strip           Apply a symbol-table strip to the executable and
                        shared libs (not recommended for Windows)
  --noupx               Do not use UPX even if it is available (works
                        differently between Windows and *nix)
  --upx-exclude FILE    Prevent a binary from being compressed when using upx.
                        This is typically used if upx corrupts certain
                        binaries during compression. FILE is the filename of
                        the binary without path. This option can be used
                        multiple times.
Windows and macOS specific options:
  -c, --console, --nowindowed
                        Open a console window for standard i/o (default). On
                        Windows this option has no effect if the first script
                        is a '.pyw' file.
  -w, --windowed, --noconsole
                        Windows and macOS: do not provide a console window for
                        standard i/o. On macOS this also triggers building a
                        macOS .app bundle. On Windows this option is
                        automatically set if the first script is a '.pyw'
                        file. This option is ignored on *NIX systems.
  --hide-console {hide-early,minimize-late,minimize-early,hide-late}
                        Windows only: in console-enabled executable, have
                        bootloader automatically hide or minimize the console
                        window if the program owns the console window (i.e.,
                        was not launched from an existing console window).
  -i, --icon <FILE.ico or FILE.exe,ID or FILE.icns or Image or "NONE">
                        FILE.ico: apply the icon to a Windows executable.
                        FILE.exe,ID: extract the icon with ID from an exe.
                        FILE.icns: apply the icon to the .app bundle on macOS.
                        If an image file is entered that isn't in the platform
                        format (ico on Windows, icns on Mac), PyInstaller
                        tries to use Pillow to translate the icon into the
                        correct format (if Pillow is installed). Use "NONE" to
                        not apply any icon, thereby making the OS show some
                        default (default: apply PyInstaller's icon). This
                        option can be used multiple times.
  --disable-windowed-traceback
                        Disable traceback dump of unhandled exception in
                        windowed (noconsole) mode (Windows and macOS only),
                        and instead display a message that this feature is
                        disabled.
Windows specific options:
  --version-file FILE   Add a version resource from FILE to the exe.
  --manifest <FILE or XML>
                        Add manifest FILE or XML to the exe.
  -m <FILE or XML>      Deprecated shorthand for --manifest.
  -r, --resource RESOURCE
                        Add or update a resource to a Windows executable. The
                        RESOURCE is one to four items,
                        FILE[,TYPE[,NAME[,LANGUAGE]]]. FILE can be a data file
                        or an exe/dll. For data files, at least TYPE and NAME
                        must be specified. LANGUAGE defaults to 0 or may be
                        specified as wildcard * to update all resources of the
                        given TYPE and NAME. For exe/dll files, all resources
                        from FILE will be added/updated to the final
                        executable if TYPE, NAME and LANGUAGE are omitted or
                        specified as wildcard *. This option can be used
                        multiple times.
  --uac-admin           Using this option creates a Manifest that will request
                        elevation upon application start.
  --uac-uiaccess        Using this option allows an elevated application to
                        work with Remote Desktop.
macOS specific options:
  --argv-emulation      Enable argv emulation for macOS app bundles. If
                        enabled, the initial open document/URL event is
                        processed by the bootloader and the passed file paths
                        or URLs are appended to sys.argv.
  --osx-bundle-identifier BUNDLE_IDENTIFIER
                        macOS .app bundle identifier is used as the default
                        unique program name for code signing purposes. The
                        usual form is a hierarchical name in reverse DNS
                        notation. For example:
                        com.mycompany.department.appname (default: first
                        script's basename)
  --target-architecture, --target-arch ARCH
                        Target architecture (macOS only; valid values: x86_64,
                        arm64, universal2). Enables switching between
                        universal2 and single-arch version of frozen
                        application (provided python installation supports the
                        target architecture). If not target architecture is
                        not specified, the current running architecture is
                        targeted.
  --codesign-identity IDENTITY
                        Code signing identity (macOS only). Use the provided
                        identity to sign collected binaries and generated
                        executable. If signing identity is not provided, ad-
```

### `pyi-set_version`

官方给出的调用示例：`pyi-set_version -h`

```text
root@kali:~# pyi-set_version -h
usage: pyi-set_version [-h] info-file exe-file
positional arguments:
  info-file   text file containing version info
  exe-file    full pathname of a Windows executable
options:
  -h, --help  show this help message and exit
```

### `pyinstaller`

官方给出的调用示例：`pyinstaller -h`

```text
root@kali:~# pyinstaller -h
usage: pyinstaller [-h] [-v] [-D] [-F] [--specpath DIR] [-n NAME]
                   [--contents-directory CONTENTS_DIRECTORY]
                   [--add-data SOURCE:DEST] [--add-binary SOURCE:DEST]
                   [-p DIR] [--hidden-import MODULENAME]
                   [--collect-submodules MODULENAME]
                   [--collect-data MODULENAME] [--collect-binaries MODULENAME]
                   [--collect-all MODULENAME] [--copy-metadata PACKAGENAME]
                   [--recursive-copy-metadata PACKAGENAME]
                   [--additional-hooks-dir HOOKSPATH]
                   [--runtime-hook RUNTIME_HOOKS] [--exclude-module EXCLUDES]
                   [--splash IMAGE_FILE]
                   [-d {all,imports,bootloader,noarchive}] [--optimize LEVEL]
                   [--python-option PYTHON_OPTION] [-s] [--noupx]
                   [--upx-exclude FILE] [-c] [-w]
                   [--hide-console {hide-late,minimize-early,hide-early,minimize-late}]
                   [-i <FILE.ico or FILE.exe,ID or FILE.icns or Image or "NONE">]
                   [--disable-windowed-traceback] [--version-file FILE]
                   [--manifest <FILE or XML>] [-m <FILE or XML>] [-r RESOURCE]
                   [--uac-admin] [--uac-uiaccess] [--argv-emulation]
                   [--osx-bundle-identifier BUNDLE_IDENTIFIER]
                   [--target-architecture ARCH] [--codesign-identity IDENTITY]
                   [--osx-entitlements-file FILENAME] [--runtime-tmpdir PATH]
                   [--bootloader-ignore-signals] [--distpath DIR]
                   [--workpath WORKPATH] [-y] [--upx-dir UPX_DIR] [--clean]
                   [--log-level LEVEL]
                   scriptname [scriptname ...]
positional arguments:
  scriptname            Name of scriptfiles to be processed or exactly one
                        .spec file. If a .spec file is specified, most options
                        are unnecessary and are ignored.
options:
  -h, --help            show this help message and exit
  -v, --version         Show program version info and exit.
  --distpath DIR        Where to put the bundled app (default: ./dist)
  --workpath WORKPATH   Where to put all the temporary work files, .log, .pyz
                        and etc. (default: ./build)
  -y, --noconfirm       Replace output directory (default:
                        SPECPATH/dist/SPECNAME) without asking for
                        confirmation
  --upx-dir UPX_DIR     Path to UPX utility (default: search the execution
                        path)
  --clean               Clean PyInstaller cache and remove temporary files
                        before building.
  --log-level LEVEL     Amount of detail in build-time console messages. LEVEL
                        may be one of TRACE, DEBUG, INFO, WARN, DEPRECATION,
                        ERROR, FATAL (default: INFO). Also settable via and
                        overrides the PYI_LOG_LEVEL environment variable.
What to generate:
  -D, --onedir          Create a one-folder bundle containing an executable
                        (default)
  -F, --onefile         Create a one-file bundled executable.
  --specpath DIR        Folder to store the generated spec file (default:
                        current directory)
  -n, --name NAME       Name to assign to the bundled app and spec file
                        (default: first script's basename)
  --contents-directory CONTENTS_DIRECTORY
                        For onedir builds only, specify the name of the
                        directory in which all supporting files (i.e.
                        everything except the executable itself) will be
                        placed in. Use "." to re-enable old onedir layout
                        without contents directory.
What to bundle, where to search:
  --add-data SOURCE:DEST
                        Additional data files or directories containing data
                        files to be added to the application. The argument
                        value should be in form of "source:dest_dir", where
                        source is the path to file (or directory) to be
                        collected, dest_dir is the destination directory
                        relative to the top-level application directory, and
                        both paths are separated by a colon (:). To put a file
                        in the top-level application directory, use . as a
                        dest_dir. This option can be used multiple times.
  --add-binary SOURCE:DEST
                        Additional binary files to be added to the executable.
                        See the ``--add-data`` option for the format. This
                        option can be used multiple times.
  -p, --paths DIR       A path to search for imports (like using PYTHONPATH).
                        Multiple paths are allowed, separated by ``':'``, or
                        use this option multiple times. Equivalent to
                        supplying the ``pathex`` argument in the spec file.
  --hidden-import, --hiddenimport MODULENAME
                        Name an import not visible in the code of the
                        script(s). This option can be used multiple times.
  --collect-submodules MODULENAME
                        Collect all submodules from the specified package or
                        module. This option can be used multiple times.
  --collect-data, --collect-datas MODULENAME
                        Collect all data from the specified package or module.
                        This option can be used multiple times.
  --collect-binaries MODULENAME
                        Collect all binaries from the specified package or
                        module. This option can be used multiple times.
  --collect-all MODULENAME
                        Collect all submodules, data files, and binaries from
                        the specified package or module. This option can be
                        used multiple times.
  --copy-metadata PACKAGENAME
                        Copy metadata for the specified package. This option
                        can be used multiple times.
  --recursive-copy-metadata PACKAGENAME
                        Copy metadata for the specified package and all its
                        dependencies. This option can be used multiple times.
  --additional-hooks-dir HOOKSPATH
                        An additional path to search for hooks. This option
                        can be used multiple times.
  --runtime-hook RUNTIME_HOOKS
                        Path to a custom runtime hook file. A runtime hook is
                        code that is bundled with the executable and is
                        executed before any other code or module to set up
                        special features of the runtime environment. This
                        option can be used multiple times.
  --exclude-module EXCLUDES
                        Optional module or package (the Python name, not the
                        path name) that will be ignored (as though it was not
                        found). This option can be used multiple times.
  --splash IMAGE_FILE   (EXPERIMENTAL) Add an splash screen with the image
                        IMAGE_FILE to the application. The splash screen can
                        display progress updates while unpacking.
How to generate:
  -d, --debug {all,imports,bootloader,noarchive}
                        Provide assistance with debugging a frozen
                        application. This argument may be provided multiple
                        times to select several of the following options.
                        - all: All three of the following options.
                        - imports: specify the -v option to the underlying
                          Python interpreter, causing it to print a message
                          each time a module is initialized, showing the
                          place (filename or built-in module) from which it
                          is loaded. See
                          https://docs.python.org/3/using/cmdline.html#id4.
                        - bootloader: tell the bootloader to issue progress
                          messages while initializing and starting the
                          bundled app. Used to diagnose problems with
                          missing imports.
                        - noarchive: instead of storing all frozen Python
                          source files as an archive inside the resulting
                          executable, store them as files in the resulting
                          output directory.
  --optimize LEVEL      Bytecode optimization level used for collected python
                        modules and scripts. For details, see the section
                        “Bytecode Optimization Level” in PyInstaller manual.
  --python-option PYTHON_OPTION
                        Specify a command-line option to pass to the Python
                        interpreter at runtime. Currently supports "v"
                        (equivalent to "--debug imports"), "u", "W <warning
                        control>", "X <xoption>", and "hash_seed=<value>". For
                        details, see the section "Specifying Python
                        Interpreter Options" in PyInstaller manual.
  -s, --strip           Apply a symbol-table strip to the executable and
                        shared libs (not recommended for Windows)
  --noupx               Do not use UPX even if it is available (works
                        differently between Windows and *nix)
  --upx-exclude FILE    Prevent a binary from being compressed when using upx.
                        This is typically used if upx corrupts certain
                        binaries during compression. FILE is the filename of
                        the binary without path. This option can be used
                        multiple times.
Windows and macOS specific options:
  -c, --console, --nowindowed
                        Open a console window for standard i/o (default). On
                        Windows this option has no effect if the first script
                        is a '.pyw' file.
  -w, --windowed, --noconsole
                        Windows and macOS: do not provide a console window for
                        standard i/o. On macOS this also triggers building a
                        macOS .app bundle. On Windows this option is
                        automatically set if the first script is a '.pyw'
                        file. This option is ignored on *NIX systems.
  --hide-console {hide-late,minimize-early,hide-early,minimize-late}
                        Windows only: in console-enabled executable, have
                        bootloader automatically hide or minimize the console
                        window if the program owns the console window (i.e.,
                        was not launched from an existing console window).
  -i, --icon <FILE.ico or FILE.exe,ID or FILE.icns or Image or "NONE">
                        FILE.ico: apply the icon to a Windows executable.
                        FILE.exe,ID: extract the icon with ID from an exe.
                        FILE.icns: apply the icon to the .app bundle on macOS.
                        If an image file is entered that isn't in the platform
                        format (ico on Windows, icns on Mac), PyInstaller
                        tries to use Pillow to translate the icon into the
                        correct format (if Pillow is installed). Use "NONE" to
                        not apply any icon, thereby making the OS show some
                        default (default: apply PyInstaller's icon). This
                        option can be used multiple times.
  --disable-windowed-traceback
                        Disable traceback dump of unhandled exception in
                        windowed (noconsole) mode (Windows and macOS only),
                        and instead display a message that this feature is
                        disabled.
Windows specific options:
  --version-file FILE   Add a version resource from FILE to the exe.
  --manifest <FILE or XML>
                        Add manifest FILE or XML to the exe.
  -m <FILE or XML>      Deprecated shorthand for --manifest.
  -r, --resource RESOURCE
                        Add or update a resource to a Windows executable. The
                        RESOURCE is one to four items,
                        FILE[,TYPE[,NAME[,LANGUAGE]]]. FILE can be a data file
                        or an exe/dll. For data files, at least TYPE and NAME
                        must be specified. LANGUAGE defaults to 0 or may be
                        specified as wildcard * to update all resources of the
                        given TYPE and NAME. For exe/dll files, all resources
                        from FILE will be added/updated to the final
                        executable if TYPE, NAME and LANGUAGE are omitted or
                        specified as wildcard *. This option can be used
                        multiple times.
  --uac-admin           Using this option creates a Manifest that will request
                        elevation upon application start.
  --uac-uiaccess        Using this option allows an elevated application to
                        work with Remote Desktop.
macOS specific options:
  --argv-emulation      Enable argv emulation for macOS app bundles. If
                        enabled, the initial open document/URL event is
                        processed by the bootloader and the passed file paths
                        or URLs are appended to sys.argv.
  --osx-bundle-identifier BUNDLE_IDENTIFIER
                        macOS .app bundle identifier is used as the default
                        unique program name for code signing purposes. The
                        usual form is a hierarchical name in reverse DNS
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install pyinstaller`，再执行 `pyinstaller --version` 2>/dev/null || `pyinstaller -V`
- [ ] **2.** **读官方帮助** —— `pyinstaller -h`，需要细节时 `man pyinstaller`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `pyinstaller -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/pyinstaller/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/pyinstaller/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/pyinstaller/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
