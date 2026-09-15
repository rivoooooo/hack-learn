# pack

> Password analysis and cracking kit PACK was developed in order to aid in a password cracking competition “Crack Me If You Can” that occurred during Defcon 2010. The goal of this toolkit is to aid in preparation for the “better than brutefo…

> **功能分类**：口令攻击 ｜ **Kali 包**：`pack` ｜ **官方文档**：<https://www.kali.org/tools/pack/>

## 1. 安装

```bash
sudo apt update
sudo apt install pack
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0.4 |
| 架构 | all |
| 可执行命令 | `pack`、`dictstat`、`jpackage`、`maskgen`、`pack200`、`policygen`、`rulegen`、`statsgen`、`unpack200` |
| 依赖 | `kali-defaults`、`python3`、`python3-enchant`、`dictstat` |
| 安装体积 | 110 KB |
| 官网 | <https://github.com/Hydraze/pack> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/pack> |
| 包追踪 | <https://pkg.kali.org/pkg/pack> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Generate statistics for passwords with a length of 10 (–minlength=10 –maxlength=10) contained in the rockyou wordlist (rockyou.txt):
root@kali:~# statsgen --minlength=10 --maxlength=10 rockyou.txt
                       _
     StatsGen 0.0.3   | |
      _ __   __ _  ___| | _
     | '_ \ / _` |/ __| |/ /
     | |_) | (_| | (__|   <
     | .__/ \__,_|\___|_|\_\
     | |
     |_| iphelix@thesprawl.org


[*] Analyzing passwords in [rockyou.txt]
[+] Analyzing 14% (2013695/14344391) of passwords
    NOTE: Statistics below is relative to the number of analyzed passwords, not total number of passwords

[*] Length:
[+]                        10: 100% (2013695)

[*] Character-set:
[+]             loweralphanum: 41% (836160)
[+]                   numeric: 23% (478196)
[+]                loweralpha: 20% (416939)
[+]      loweralphaspecialnum: 02% (59911)
[+]         loweralphaspecial: 02% (55761)
[+]             mixedalphanum: 02% (54198)
[+]             upperalphanum: 02% (47430)
[+]                upperalpha: 00% (19723)
[+]                mixedalpha: 00% (15460)
[+]                       all: 00% (9015)
[+]         mixedalphaspecial: 00% (6856)
[+]                specialnum: 00% (6685)
[+]      upperalphaspecialnum: 00% (3698)
[+]         upperalphaspecial: 00% (3459)
[+]                   special: 00% (204)

[*] Password complexity:
[+]                     digit: min(0) max(10)
[+]                     lower: min(0) max(10)
[+]                     upper: min(0) max(10)
[+]                   special: min(0) max(10)

[*] Simple Masks:
[+]               stringdigit: 37% (750938)
[+]                     digit: 23% (478196)
[+]                    string: 22% (452122)
[+]               digitstring: 03% (78963)
[+]                 othermask: 03% (67762)
[+]         stringdigitstring: 02% (59783)
[+]       stringspecialstring: 01% (33173)
[+]        stringspecialdigit: 01% (25293)
[+]             stringspecial: 01% (22207)
[+]          digitstringdigit: 00% (17290)
[+]        stringdigitspecial: 00% (12563)
[+]      specialstringspecial: 00% (3463)
[+]        digitspecialstring: 00% (2406)
[+]             specialstring: 00% (1773)
[+]        digitstringspecial: 00% (1621)
[+]        specialstringdigit: 00% (1468)
[+]        specialdigitstring: 00% (1225)
[+]         digitspecialdigit: 00% (1185)
[+]              digitspecial: 00% (1183)
[+]       specialdigitspecial: 00% (515)
[+]              specialdigit: 00% (362)
[+]                   special: 00% (204)

[*] Advanced Masks:
[+]      ?d?d?d?d?d?d?d?d?d?d: 23% (478196)
[+]      ?l?l?l?l?l?l?l?l?l?l: 20% (416939)
[+]      ?l?l?l?l?l?l?l?l?d?d: 10% (213109)
[+]      ?l?l?l?l?l?l?d?d?d?d: 07% (160592)
[+]      ?l?l?l?l?l?l?l?l?l?d: 06% (129823)
[+]      ?l?l?l?l?l?l?l?d?d?d: 04% (87611)
[+]      ?l?l?l?l?d?d?d?d?d?d: 01% (33277)

policygen Usage Example
Generate Hashcat masks with a length of 8 (–length=8) and containing at least 1 uppercase letter (–minupper 1) and at least 1 digit (–mindigit 1), saving the masks to a file (-o complexity.hcmask):
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 9 个可执行命令，下面是官方页面内嵌的帮助原文。

### `statsgen`

官方给出的调用示例：`statsgen --minlength=10 --maxlength=10 rockyou.txt`

```text
root@kali:~# statsgen --minlength=10 --maxlength=10 rockyou.txt
                       _
     StatsGen 0.0.3   | |
      _ __   __ _  ___| | _
     | '_ \ / _` |/ __| |/ /
     | |_) | (_| | (__|   <
     | .__/ \__,_|\___|_|\_\
     | |
     |_|
[email protected]
[*] Analyzing passwords in [rockyou.txt]
[+] Analyzing 14% (2013695/14344391) of passwords
    NOTE: Statistics below is relative to the number of analyzed passwords, not total number of passwords
[*] Length:
[+]                        10: 100% (2013695)
[*] Character-set:
[+]             loweralphanum: 41% (836160)
[+]                   numeric: 23% (478196)
[+]                loweralpha: 20% (416939)
[+]      loweralphaspecialnum: 02% (59911)
[+]         loweralphaspecial: 02% (55761)
[+]             mixedalphanum: 02% (54198)
[+]             upperalphanum: 02% (47430)
[+]                upperalpha: 00% (19723)
[+]                mixedalpha: 00% (15460)
[+]                       all: 00% (9015)
[+]         mixedalphaspecial: 00% (6856)
[+]                specialnum: 00% (6685)
[+]      upperalphaspecialnum: 00% (3698)
[+]         upperalphaspecial: 00% (3459)
[+]                   special: 00% (204)
[*] Password complexity:
[+]                     digit: min(0) max(10)
[+]                     lower: min(0) max(10)
[+]                     upper: min(0) max(10)
[+]                   special: min(0) max(10)
[*] Simple Masks:
[+]               stringdigit: 37% (750938)
[+]                     digit: 23% (478196)
[+]                    string: 22% (452122)
[+]               digitstring: 03% (78963)
[+]                 othermask: 03% (67762)
[+]         stringdigitstring: 02% (59783)
[+]       stringspecialstring: 01% (33173)
[+]        stringspecialdigit: 01% (25293)
[+]             stringspecial: 01% (22207)
[+]          digitstringdigit: 00% (17290)
[+]        stringdigitspecial: 00% (12563)
[+]      specialstringspecial: 00% (3463)
[+]        digitspecialstring: 00% (2406)
[+]             specialstring: 00% (1773)
[+]        digitstringspecial: 00% (1621)
[+]        specialstringdigit: 00% (1468)
[+]        specialdigitstring: 00% (1225)
[+]         digitspecialdigit: 00% (1185)
[+]              digitspecial: 00% (1183)
[+]       specialdigitspecial: 00% (515)
[+]              specialdigit: 00% (362)
[+]                   special: 00% (204)
[*] Advanced Masks:
[+]      ?d?d?d?d?d?d?d?d?d?d: 23% (478196)
[+]      ?l?l?l?l?l?l?l?l?l?l: 20% (416939)
[+]      ?l?l?l?l?l?l?l?l?d?d: 10% (213109)
[+]      ?l?l?l?l?l?l?d?d?d?d: 07% (160592)
[+]      ?l?l?l?l?l?l?l?l?l?d: 06% (129823)
[+]      ?l?l?l?l?l?l?l?d?d?d: 04% (87611)
[+]      ?l?l?l?l?d?d?d?d?d?d: 01% (33277)
policygen Usage Example
Generate Hashcat masks with a length of 8 (
–length=8
) and containing at least 1 uppercase letter (
–minupper 1
) and at least 1 digit (
–mindigit 1
), saving the masks to a file (
-o complexity.hcmask
):
```

### `policygen`

官方给出的调用示例：`policygen --length=8 --minupper 1 --mindigit 1 -o complexity.hcmask`

```text
root@kali:~# policygen --length=8 --minupper 1 --mindigit 1 -o complexity.hcmask
[*] Password policy:
[+] Password length: 8
[+] Minimum strength: lower: 0, upper: 1, digits: 1, special: 0
[+] Maximum strength: lower: 8, upper: 8, digits: 8, special: 8
[*] Total Masks:  65536 Runtime: [76d|1834h|110078m|6604680s]
[*] Policy Masks: 52670 Runtime: [40d|977h|58659m|3519568s]
```

### `head`

官方给出的调用示例：`head complexity.hcmask`

```text
root@kali:~# head complexity.hcmask
?l?l?l?l?l?l?u?d
?l?l?l?l?l?l?d?u
?l?l?l?l?l?u?l?d
?l?l?l?l?l?u?u?d
?l?l?l?l?l?u?d?l
?l?l?l?l?l?u?d?u
?l?l?l?l?l?u?d?d
?l?l?l?l?l?u?d?s
?l?l?l?l?l?u?s?d
?l?l?l?l?l?d?l?u
```

### `dictstat`

官方给出的调用示例：`dictstat -h`

```text
root@kali:~# dictstat -h
┏━(Message from Kali developers)
┃
┃ The command dictstat is deprecated. Please use statsgen instead.
┃
┗━
```

### `jpackage`

官方给出的调用示例：`jpackage -h`

```text
root@kali:~# jpackage -h
Usage: jpackage <options>
Sample usages:
--------------
    Generate an application package suitable for the host system:
        For a modular application:
            jpackage -n name -p modulePath -m moduleName/className
        For a non-modular application:
            jpackage -i inputDir -n name \
                --main-class className --main-jar myJar.jar
        From a pre-built application image:
            jpackage -n name --app-image appImageDir
    Generate an application image:
        For a modular application:
            jpackage --type app-image -n name -p modulePath \
                -m moduleName/className
        For a non-modular application:
            jpackage --type app-image -i inputDir -n name \
                --main-class className --main-jar myJar.jar
        To provide your own options to jlink, run jlink separately:
            jlink --output appRuntimeImage -p modulePath \
                --add-modules moduleName \
                --no-header-files [<additional jlink options>...]
            jpackage --type app-image -n name \
                -m moduleName/className --runtime-image appRuntimeImage
    Generate a Java runtime package:
        jpackage -n name --runtime-image <runtime-image>
Generic Options:
  @<filename>
          Read options and/or mode from a file
          This option can be used multiple times.
  --type -t <type>
          The type of package to create
          Valid values are: {"app-image", "rpm", "deb"}
          If this option is not specified a platform dependent
          default type will be created.
  --app-version <version>
          Version of the application and/or package
  --copyright <copyright string>
          Copyright for the application
  --description <description string>
          Description of the application
  --help -h
          Print the usage text with a list and description of each valid
          option for the current platform to the output stream, and exit
  --icon <file path>
          Path of the icon of the application package
          (absolute path or relative to the current directory)
  --name -n <name>
          Name of the application and/or package
  --dest -d <destination path>
          Path where generated output file is placed
          (absolute path or relative to the current directory)
          Defaults to the current working directory.
  --temp <directory path>
          Path of a new or empty directory used to create temporary files
          (absolute path or relative to the current directory)
          If specified, the temp dir will not be removed upon the task
          completion and must be removed manually.
          If not specified, a temporary directory will be created and
          removed upon the task completion.
  --vendor <vendor string>
          Vendor of the application
  --verbose
          Enables verbose output
  --version
          Print the product version to the output stream and exit.
Options for creating the runtime image:
  --add-modules <module name>[,<module name>...]
          A comma (",") separated list of modules to add
          This module list, along with the main module (if specified)
          will be passed to jlink as the --add-module argument.
          If not specified, either just the main module (if --module is
          specified), or the default set of modules (if --main-jar is
          specified) are used.
          This option can be used multiple times.
  --module-path -p <module path>...
          A : separated list of paths
          Each path is either a directory of modules or the path to a
          modular jar.
          (Each path is absolute or relative to the current directory.)
          This option can be used multiple times.
  --jlink-options <jlink options>
          A space separated list of options to pass to jlink
          If not specified, defaults to "--strip-native-commands
          --strip-debug --no-man-pages --no-header-files".
          This option can be used multiple times.
  --runtime-image <directory path>
          Path of the predefined runtime image that will be copied into
          the application image
          (absolute path or relative to the current directory)
          If --runtime-image is not specified, jpackage will run jlink to
          create the runtime image using options:
          --strip-debug, --no-header-files, --no-man-pages, and
          --strip-native-commands.
Options for creating the application image:
  --input -i <directory path>
          Path of the input directory that contains the files to be packaged
          (absolute path or relative to the current directory)
          All files in the input directory will be packaged into the
          application image.
  --app-content <additional content>[,<additional content>...]
          A comma separated list of paths to files and/or directories
          to add to the application payload.
          This option can be used more than once.
Options for creating the application launcher(s):
  --add-launcher <launcher name>=<file path>
          Name of launcher, and a path to a Properties file that contains
          a list of key, value pairs
          (absolute path or relative to the current directory)
          The keys "module", "main-jar", "main-class", "description",
          "arguments", "java-options", "app-version", "icon",
          "launcher-as-service",
          "win-console", "win-shortcut", "win-menu",
          "linux-app-category", and "linux-shortcut" can be used.
          These options are added to, or used to overwrite, the original
          command line options to build an additional alternative launcher.
          The main application launcher will be built from the command line
          options. Additional alternative launchers can be built using
          this option, and this option can be used multiple times to
          build multiple additional launchers.
  --arguments <main class arguments>
          Command line arguments to pass to the main class if no command
          line arguments are given to the launcher
          This option can be used multiple times.
  --java-options <java options>
          Options to pass to the Java runtime
          This option can be used multiple times.
  --main-class <class name>
          Qualified name of the application main class to execute
          This option can only be used if --main-jar is specified.
  --main-jar <main jar file>
          The main JAR of the application; containing the main class
          (specified as a path relative to the input path)
          Either --module or --main-jar option can be specified but not
          both.
  --module -m <module name>[/<main class>]
          The main module (and optionally main class) of the application
          This module must be located on the module path.
          When this option is specified, the main module will be linked
          in the Java runtime image.  Either --module or --main-jar
          option can be specified but not both.
Options for creating the application package:
  --about-url <url>
          URL of the application's home page
  --app-image <directory path>
          Location of the predefined application image that is used
          to build an installable package
          (absolute path or relative to the current directory)
  --file-associations <file path>
          Path to a Properties file that contains list of key, value pairs
          (absolute path or relative to the current directory)
          The keys "extension", "mime-type", "icon", and "description"
          can be used to describe the association.
          This option can be used multiple times.
  --install-dir <directory path>
          Absolute path of the installation directory of the application
  --license-file <file path>
          Path to the license file
          (absolute path or relative to the current directory)
  --resource-dir <directory path>
          Path to override jpackage resources
          Icons, template files, and other resources of jpackage can be
          over-ridden by adding replacement resources to this directory.
          (absolute path or relative to the current directory)
  --runtime-image <directory path>
          Path of the predefined runtime image to install
          (absolute path or relative to the current directory)
          Option is required when creating a runtime package.
  --launcher-as-service
          Request to create an installer that will register the main
          application launcher as a background service-type application.
Platform dependent options for creating the application package:
  --linux-package-name <package name>
          Name for Linux package, defaults to the application name
  --linux-deb-maintainer <email address>
          Maintainer for .deb package
  --linux-menu-group <menu-group-name>
          Menu group this application is placed in
  --linux-package-deps <package-dep-string>
          Required packages or capabilities for the application
  --linux-rpm-license-type <type string>
          Type of the license ("License: <value>" of the RPM .spec)
  --linux-app-release <release value>
          Release value of the RPM <name>.spec file or
          Debian revision value of the DEB control file
  --linux-app-category <category value>
          Group value of the RPM <name>.spec file or
          Section value of DEB control file
  --linux-shortcut
          Creates a shortcut for the application.
```

### `maskgen`

官方给出的调用示例：`maskgen -h`

```text
root@kali:~# maskgen -h
Usage: maskgen pass0.masks [pass1.masks ...] [options]
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -t 86400, --targettime=86400
                        Target time of all masks (seconds)
  -o masks.hcmask, --outputmasks=masks.hcmask
                        Save masks to a file
  --showmasks           Show matching masks
  Individual Mask Filter Options:
    --minlength=8       Minimum password length
    --maxlength=8       Maximum password length
    --mintime=3600      Minimum mask runtime (seconds)
    --maxtime=3600      Maximum mask runtime (seconds)
    --mincomplexity=1   Minimum complexity
    --maxcomplexity=100
                        Maximum complexity
    --minoccurrence=1   Minimum occurrence
    --maxoccurrence=100
                        Maximum occurrence
  Mask Sorting Options:
    --optindex          sort by mask optindex (default)
    --occurrence        sort by mask occurrence
    --complexity        sort by mask complexity
  Check mask coverage:
    --checkmasks=?u?l?l?l?l?l?d,?l?l?l?l?l?d?d
                        check mask coverage
    --checkmasksfile=masks.hcmask
                        check mask coverage in a file
  Miscellaneous options:
    --pps=1000000000    Passwords per Second
    -q, --quiet         Don't show headers.
```

### `pack200`

官方给出的调用示例：`pack200 -h`

```text
root@kali:~# pack200 -h
Warning: The pack200 tool is deprecated, and is planned for removal in a future JDK release.
Usage:  pack200 [-opt... | --option=value]... x.pack[.gz] y.jar
Packing Options
  -r, --repack                    repack or normalize a jar, suitable for
                                  signing with jarsigner
  -g, --no-gzip                   output a plain pack file, suitable to be
                                  compressed with a file compression utility
  --gzip                          (default) post compress the pack output
                                  with gzip
  -G, --strip-debug               remove debugging attributes (SourceFile,
                                  LineNumberTable, LocalVariableTable
                                  and LocalVariableTypeTable) while packing
  -O, --no-keep-file-order        do not transmit file ordering information
  --keep-file-order               (default) preserve input file ordering
  -S{N}, --segment-limit={N}      limit segment sizes (default unlimited)
  -E{N}, --effort={N}             packing effort (default N=5)
  -H{h}, --deflate-hint={h}       transmit deflate hint: true, false,
                                  or keep (default)
  -m{V}, --modification-time={V}  transmit modtimes: latest or keep (default)
  -P{F}, --pass-file={F}          transmit the given input element(s) unchanged
  -U{a}, --unknown-attribute={a}  unknown attribute action: error, strip,
                                  or pass (default)
  -C{N}={L}, --class-attribute={N}={L}  (user-defined attribute)
  -F{N}={L}, --field-attribute={N}={L}  (user-defined attribute)
  -M{N}={L}, --method-attribute={N}={L} (user-defined attribute)
  -D{N}={L}, --code-attribute={N}={L}   (user-defined attribute)
  -f{F}, --config-file={F}        read file F for Pack200.Packer properties
  -v, --verbose                   increase program verbosity
  -q, --quiet                     set verbosity to lowest level
  -l{F}, --log-file={F}           output to the given log file,
                                  or '-' for System.out
  -?, -h, --help                  print this help message
  -V, --version                   print program version
  -J{X}                           pass option X to underlying Java VM
Notes:
  The -P, -C, -F, -M, and -D options accumulate.
  Example attribute definition:  -C SourceFile=RUH .
  Config. file properties are defined by the Pack200 API.
  For meaning of -S, -E, -H-, -m, -U values, see Pack200 API.
  Layout definitions (like RUH) are defined by JSR 200.
Repacking mode updates the JAR file with a pack/unpack cycle:
    pack200 [-r|--repack] [-opt | --option=value]... [repackedy.jar] y.jar
Exit Status:
  0 if successful, >0 if an error occurred
Warning: The pack200 tool is deprecated, and is planned for removal in a future JDK release.
```

### `policygen（示例）`

官方给出的调用示例：`policygen -h`

```text
root@kali:~# policygen -h
Usage: policygen [options]
Type --help for more options
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -o masks.hcmask, --outputmasks=masks.hcmask
                        Save masks to a file
  --pps=1000000000      Passwords per Second
  --showmasks           Show matching masks
  --noncompliant        Generate masks for noncompliant passwords
  -q, --quiet           Don't show headers.
  Password Policy:
    Define the minimum (or maximum) password strength policy that you
    would like to test
    --minlength=8       Minimum password length
    --maxlength=8       Maximum password length
    --mindigit=1        Minimum number of digits
    --minlower=1        Minimum number of lower-case characters
    --minupper=1        Minimum number of upper-case characters
    --minspecial=1      Minimum number of special characters
    --maxdigit=3        Maximum number of digits
    --maxlower=3        Maximum number of lower-case characters
    --maxupper=3        Maximum number of upper-case characters
    --maxspecial=3      Maximum number of special characters
```

### `rulegen`

官方给出的调用示例：`rulegen -h`

```text
root@kali:~# rulegen -h
Usage: rulegen [options] passwords.txt
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -b rockyou, --basename=rockyou
                        Output base name. The following files will be
                        generated: basename.words, basename.rules and
                        basename.stats
  -w wiki.dict, --wordlist=wiki.dict
                        Use a custom wordlist for rule analysis.
  -q, --quiet           Don't show headers.
  --threads=THREADS     Parallel threads to use for processing.
  Fine tune source word generation::
    --maxworddist=10    Maximum word edit distance (Levenshtein)
    --maxwords=5        Maximum number of source word candidates to consider
    --morewords         Consider suboptimal source word candidates
    --simplewords       Generate simple source words for given passwords
  Fine tune rule generation::
    --maxrulelen=10     Maximum number of operations in a single rule
    --maxrules=5        Maximum number of rules to consider
    --morerules         Generate suboptimal rules
    --simplerules       Generate simple rules insert,delete,replace
    --bruterules        Bruteforce reversal and rotation rules (slow)
  Fine tune spell checker engine::
    --providers=aspell,myspell
                        Comma-separated list of provider engines
  Debuggin options::
    -v, --verbose       Show verbose information.
    -d, --debug         Debug rules.
    --password          Process the last argument as a password not a file.
    --word=Password     Use a custom word for rule analysis
    --hashcat           Test generated rules with hashcat-cli
```

### `statsgen（示例）`

官方给出的调用示例：`statsgen -h`

```text
root@kali:~# statsgen -h
Usage: statsgen [options] passwords.txt
Type --help for more options
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -o password.masks, --output=password.masks
                        Save masks and stats to a file
  --hiderare            Hide statistics covering less than 1% of the sample
  -q, --quiet           Don't show headers.
  Password Filters:
    --minlength=8       Minimum password length
    --maxlength=8       Maximum password length
    --charset=loweralpha,numeric
                        Password charset filter (comma separated)
    --simplemask=stringdigit,allspecial
                        Password mask filter (comma separated)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install pack`，再执行 `pack --version` 2>/dev/null || `pack -V`
- [ ] **2.** **读官方帮助** —— `pack -h`，需要细节时 `man pack`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: jpackage <options>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/pack/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/pack/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/pack/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
