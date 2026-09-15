# osrframework

> Open Sources Research Framework This package contains a set of libraries developed by i3visio to perform Open Source Intelligence tasks. They include references to a bunch of different applications related to username checking, DNS lookups…

> **功能分类**：识别与指纹 ｜ **Kali 包**：`osrframework` ｜ **官方文档**：<https://www.kali.org/tools/osrframework/>

## 1. 安装

```bash
sudo apt update
sudo apt install osrframework
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.20.5 |
| 架构 | all |
| 可执行命令 | `osrframework`、`alias_generator`、`alias_generator.py`、`checkfy`、`checkfy.py`、`domainfy`、`domainfy.py`、`mailfy`、`mailfy.py`、`osrf`、`osrframework-cli`、`phonefy`、`phonefy.py`、`searchfy`、`searchfy.py`、`usufy`、`usufy.py` |
| 依赖 | `python3`、`python3-bs4`、`python3-cfscrape`、`python3-colorama`、`python3-decorator`、`python3-duckpy`、`python3-emailahoy3`、`python3-networkx`、`python3-oauthlib`、`python3-pyexcel`、`python3-pyexcel-io`、`python3-pyexcel-ods` 等 |
| 安装体积 | 1.51 MB |
| 官网 | <https://pypi.org/project/osrframework/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/osrframework> |
| 包追踪 | <https://pkg.kali.org/pkg/osrframework> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
Check for the -n kalilinux username across all available services:
root@kali:~# usufy.py -n kalilinux

  ___  ____  ____  _____                                            _
 / _ \/ ___||  _ \|  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
| | | \___ \| |_) | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
| |_| |___) |  _ <|  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
 \___/|____/|_| \_\_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_

                Version:      OSRFramework 0.17.2
                Created by:   Felix Brezo and Yaiza Rubio, (i3visio)



usufy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014-2017

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit https://www.gnu.org/licenses/agpl-3.0.txt

2017-10-05 11:20:10.448178  Starting search in 297 platform(s)... Relax!

    Press <Ctrl + C> to stop...

[!] In skype.py, exception caught when checking information in Skype!

2017-10-05 11:20:30.854308  A summary of the results obtained are shown in the following table:

Sheet Name: Profiles recovered (2017-10-5_11h20m).
+-----------------------------------------------------------------+---------------+-------------------+
|                           i3visio_uri                           | i3visio_alias | i3visio_platform  |
+=================================================================+===============+===================+
| https://www.facebook.com/kalilinux                              | kalilinux     | Facebook          |
+-----------------------------------------------------------------+---------------+-------------------+
| http://twitter.com/kalilinux                                    | kalilinux     | Twitter           |
+-----------------------------------------------------------------+---------------+-------------------+
[...]

Search for a given email address.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 17 个可执行命令，下面是官方页面内嵌的帮助原文。

### `usufy.py`

官方给出的调用示例：`usufy.py -n kalilinux`

```text
root@kali:~# usufy.py -n kalilinux
  ___  ____  ____  _____                                            _
 / _ \/ ___||  _ \|  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
| | | \___ \| |_) | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
| |_| |___) |  _ <|  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
 \___/|____/|_| \_\_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_
                Version:      OSRFramework 0.17.2
                Created by:   Felix Brezo and Yaiza Rubio, (i3visio)
usufy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014-2017
This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit https://www.gnu.org/licenses/agpl-3.0.txt
2017-10-05 11:20:10.448178  Starting search in 297 platform(s)... Relax!
    Press <Ctrl + C> to stop...
[!] In skype.py, exception caught when checking information in Skype!
2017-10-05 11:20:30.854308  A summary of the results obtained are shown in the following table:
Sheet Name: Profiles recovered (2017-10-5_11h20m).
+-----------------------------------------------------------------+---------------+-------------------+
|                           i3visio_uri                           | i3visio_alias | i3visio_platform  |
+=================================================================+===============+===================+
| https://www.facebook.com/kalilinux                              | kalilinux     | Facebook          |
+-----------------------------------------------------------------+---------------+-------------------+
| http://twitter.com/kalilinux                                    | kalilinux     | Twitter           |
+-----------------------------------------------------------------+---------------+-------------------+
[...]
Search for a given email address.
```

### `mailfy.py`

官方给出的调用示例：`mailfy.py -n ltorvalds`

```text
root@kali:~# mailfy.py -n ltorvalds
  ___  ____  ____  _____                                            _
 / _ \/ ___||  _ \|  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
| | | \___ \| |_) | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
| |_| |___) |  _ <|  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
 \___/|____/|_| \_\_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_
                Version:      OSRFramework 0.17.2
                Created by:   Felix Brezo and Yaiza Rubio, (i3visio)
mailfy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2016-2017
This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit https://www.gnu.org/licenses/agpl-3.0.txt
2017-10-05 11:32:49.178753  Starting search in 22 different emails:
[
  "
[email protected]
",
  "
[email protected]
",
  "
[email protected]
",
[...]
Search for a given string across all OSRF services.
root@kali:~$ searchfy.py -q "dookie2000ca"
  ___  ____  ____  _____                                            _
 / _ \/ ___||  _ \|  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
| | | \___ \| |_) | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
| |_| |___) |  _ <|  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
 \___/|____/|_| \_\_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_
                Version:      OSRFramework 0.17.2
                Created by:   Felix Brezo and Yaiza Rubio, (i3visio)
searchfy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014-2017
This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit https://www.gnu.org/licenses/agpl-3.0.txt
2017-10-05 11:38:33.545680  Starting search in different platform(s)... Relax!
    Press <Ctrl + C> to stop...
[!] In skype.py, exception caught when checking information in Skype!
2017-10-05 11:38:36.672623  A summary of the results obtained are listed in the following table:
Sheet Name: Profiles recovered (2017-10-5_11h38m).
+---------------------------------+---------------+------------------+
|           i3visio_uri           | i3visio_alias | i3visio_platform |
+=================================+===============+==================+
| http://github.com/dookie2000ca  | dookie2000ca  | Github           |
+---------------------------------+---------------+------------------+
| http://twitter.com/dookie2000ca | dookie2000ca  | Twitter          |
+---------------------------------+---------------+------------------+
2017-10-05 11:38:36.685354  You can find all the information collected in the following files:
    ./profiles.csv
2017-10-05 11:38:36.685581  Finishing execution...
Total time used:    0:00:03.139901
Average seconds/query:  3.139901 seconds
Did something go wrong? Is a platform reporting false positives? Do you need to
integrate a new one and you don't know how to start? Then, you can always place
an issue in the Github project:
    https://github.com/i3visio/osrframework/issues
Note that otherwise, we won't know about it!
```

### `alias_generator`

官方给出的调用示例：`alias_generator -h`

```text
root@kali:~# alias_generator -h
usage: alias_generator [-n <NAME>] [-s1 <SURNAME_1>] [-s2 <SURNAME_2>]
                       [-c <CITY>] [-C <COUNTRY>] [-y <YEAR>]
                       [-o <path_to_output_file>] [--numbers] [--common-words]
                       [--leet] [--locales]
                       [--extra-words EXTRA_WORDS [EXTRA_WORDS ...]] [-h]
                       [--version]
alias_generator is a tool that tries to create possible aliases based on the
inputs known from a person.
options:
  -n, --name <NAME>     Name of the person.
  -s1, --surname1 <SURNAME_1>
                        First surname.
  -s2, --surname2 <SURNAME_2>
                        Second surname.
  -c, --city <CITY>     A city linked to the profile.
  -C, --country <COUNTRY>
                        A country.
  -y, --year <YEAR>     Birth year.
  -o, --output-file <path_to_output_file>
                        Path to the output file.
Profile squatting arguments:
  Showing additional configuration options for this program based on the
  original -s option in usufy.py.
  --numbers             Adds numbers at the end of the nicknames.
  --common-words        Adds some famous words at the end of the nicknames.
  --leet                Adds the leet mode to change 'a' by '4', 'e' by '3',
                        etc.
  --locales             Adds ending linked to countries.
  --extra-words EXTRA_WORDS [EXTRA_WORDS ...]
                        Adds new words to the nicknames provided by the user.
About arguments:
  Showing additional information about this program.
  -h, --help            shows this help and exists.
  --version             shows the version of the program and exists.
```

### `alias_generator.py`

官方给出的调用示例：`alias_generator.py -h`

```text
root@kali:~# alias_generator.py -h
usage: alias_generator [-n <NAME>] [-s1 <SURNAME_1>] [-s2 <SURNAME_2>]
                       [-c <CITY>] [-C <COUNTRY>] [-y <YEAR>]
                       [-o <path_to_output_file>] [--numbers] [--common-words]
                       [--leet] [--locales]
                       [--extra-words EXTRA_WORDS [EXTRA_WORDS ...]] [-h]
                       [--version]
alias_generator is a tool that tries to create possible aliases based on the
inputs known from a person.
options:
  -n, --name <NAME>     Name of the person.
  -s1, --surname1 <SURNAME_1>
                        First surname.
  -s2, --surname2 <SURNAME_2>
                        Second surname.
  -c, --city <CITY>     A city linked to the profile.
  -C, --country <COUNTRY>
                        A country.
  -y, --year <YEAR>     Birth year.
  -o, --output-file <path_to_output_file>
                        Path to the output file.
Profile squatting arguments:
  Showing additional configuration options for this program based on the
  original -s option in usufy.py.
  --numbers             Adds numbers at the end of the nicknames.
  --common-words        Adds some famous words at the end of the nicknames.
  --leet                Adds the leet mode to change 'a' by '4', 'e' by '3',
                        etc.
  --locales             Adds ending linked to countries.
  --extra-words EXTRA_WORDS [EXTRA_WORDS ...]
                        Adds new words to the nicknames provided by the user.
About arguments:
  Showing additional information about this program.
  -h, --help            shows this help and exists.
  --version             shows the version of the program and exists.
```

### `checkfy`

官方给出的调用示例：`checkfy -h`

```text
root@kali:~# checkfy -h
usage: checkfy (--license | -n <nicks> [<nicks> ...] | -N <nicks_file>)
               -m <pattern> [-o <path_to_output_folder>] [-t <type>] [--quiet]
               [-h] [--version]
checkfy - Finding potential email addresses based on a list of known aliases
(either provided as arguments or read from a file) and a known pattern.
Default values can be io
Input options (one required):
  --license             shows the GPLv3+ license and exists.
  -n, --nicks <nicks> [<nicks> ...]
                        the list of nicks to be checked in the domains
                        selected.
  -N, --nicks_file <nicks_file>
                        the file with the list of nicks to be checked in the
                        domains selected.
  -m, --email-pattern <pattern>
                        The email pattern that the generated email address
                        SHOULD match. The pattern type can be configured using
                        `--type`.
Other options:
  Configuring other options.
  -o, --output_folder <path_to_output_folder>
                        output folder for the generated files. Default: ./.
  -t, --type <type>     The type of pattern provided. It can be either the
                        style used by Twitter to show the pattern suggestions
                        or a regular expression. Default: regexp.
  --quiet               tells the program not to show anything.
About arguments:
  Showing additional information about this program.
  -h, --help            shows this help and exists.
  --version             shows the version of the program and exists.
Check the README.md file for further details on the usage of this program or
follow us on Twitter in <http://twitter.com/i3visio>.
```

### `checkfy.py`

官方给出的调用示例：`checkfy.py -h`

```text
root@kali:~# checkfy.py -h
usage: checkfy (--license | -n <nicks> [<nicks> ...] | -N <nicks_file>)
               -m <pattern> [-o <path_to_output_folder>] [-t <type>] [--quiet]
               [-h] [--version]
checkfy - Finding potential email addresses based on a list of known aliases
(either provided as arguments or read from a file) and a known pattern.
Default values can be io
Input options (one required):
  --license             shows the GPLv3+ license and exists.
  -n, --nicks <nicks> [<nicks> ...]
                        the list of nicks to be checked in the domains
                        selected.
  -N, --nicks_file <nicks_file>
                        the file with the list of nicks to be checked in the
                        domains selected.
  -m, --email-pattern <pattern>
                        The email pattern that the generated email address
                        SHOULD match. The pattern type can be configured using
                        `--type`.
Other options:
  Configuring other options.
  -o, --output_folder <path_to_output_folder>
                        output folder for the generated files. Default: ./.
  -t, --type <type>     The type of pattern provided. It can be either the
                        style used by Twitter to show the pattern suggestions
                        or a regular expression. Default: regexp.
  --quiet               tells the program not to show anything.
About arguments:
  Showing additional information about this program.
  -h, --help            shows this help and exists.
  --version             shows the version of the program and exists.
Check the README.md file for further details on the usage of this program or
follow us on Twitter in <http://twitter.com/i3visio>.
```

### `domainfy`

官方给出的调用示例：`domainfy -h`

```text
root@kali:~# domainfy -h
usage: domainfy (-n <nicks> [<nicks> ...] | -N <nicks_file> | --license)
                [-e <sum_ext> [<sum_ext> ...]] [-o <path_to_output_folder>]
                [-t <tld_type> [<tld_type> ...]]
                [-u <new_tld> [<new_tld> ...]] [-x <domain> [<domain> ...]]
                [-F <alternative_header_file>] [-T <num_threads>] [--quiet]
                [--whois] [-h] [--version]
domainfy - Checking the existence of domains that resolev to an IP address.
Input options (one required):
  -n, --nicks <nicks> [<nicks> ...]
                        the list of nicks to be checked in the domains
                        selected.
  -N, --nicks_file <nicks_file>
                        the file with the list of nicks to be checked in the
                        domains selected.
  --license             shows the GPLv3+ license and exists.
Processing arguments:
  Configuring the way in which mailfy will process the identified profiles.
  -e, --extension <sum_ext> [<sum_ext> ...]
                        output extension for the summary files. Default: xls.
  -o, --output-folder <path_to_output_folder>
                        output folder for the generated documents. While if
                        the paths does not exist, usufy.py will try to create;
                        if this argument is not provided, usufy will NOT write
                        any down any data. Check permissions if something goes
                        wrong.
  -t, --tlds <tld_type> [<tld_type> ...]
                        list of TLD types where the nick will be looked for.
  -u, --user-defined <new_tld> [<new_tld> ...]
                        additional TLD that will be searched.
  -x, --exclude <domain> [<domain> ...]
                        select the domains to be avoided. The format should
                        include the initial '.'.
  -F, --file-header <alternative_header_file>
                        header for the output filenames to be generated. If
                        None was provided the following will be used:
                        profiles.<extension>.
  -T, --threads <num_threads>
                        write down the number of threads to be used (default
                        16). If 0, the maximum number possible will be used,
                        which may make the system feel unstable.
  --quiet               tells the program not to show anything.
  --whois               tells the program to launch whois queries.
About arguments:
  Showing additional information about this program.
  -h, --help            shows this help and exists.
  --version             shows the version of the program and exists.
Check the README.md file for further details on the usage of this program or
follow us on Twitter in <http://twitter.com/i3visio>.
```

### `domainfy.py`

官方给出的调用示例：`domainfy.py -h`

```text
root@kali:~# domainfy.py -h
usage: domainfy (-n <nicks> [<nicks> ...] | -N <nicks_file> | --license)
                [-e <sum_ext> [<sum_ext> ...]] [-o <path_to_output_folder>]
                [-t <tld_type> [<tld_type> ...]]
                [-u <new_tld> [<new_tld> ...]] [-x <domain> [<domain> ...]]
                [-F <alternative_header_file>] [-T <num_threads>] [--quiet]
                [--whois] [-h] [--version]
domainfy - Checking the existence of domains that resolev to an IP address.
Input options (one required):
  -n, --nicks <nicks> [<nicks> ...]
                        the list of nicks to be checked in the domains
                        selected.
  -N, --nicks_file <nicks_file>
                        the file with the list of nicks to be checked in the
                        domains selected.
  --license             shows the GPLv3+ license and exists.
Processing arguments:
  Configuring the way in which mailfy will process the identified profiles.
  -e, --extension <sum_ext> [<sum_ext> ...]
                        output extension for the summary files. Default: xls.
  -o, --output-folder <path_to_output_folder>
                        output folder for the generated documents. While if
                        the paths does not exist, usufy.py will try to create;
                        if this argument is not provided, usufy will NOT write
                        any down any data. Check permissions if something goes
                        wrong.
  -t, --tlds <tld_type> [<tld_type> ...]
                        list of TLD types where the nick will be looked for.
  -u, --user-defined <new_tld> [<new_tld> ...]
                        additional TLD that will be searched.
  -x, --exclude <domain> [<domain> ...]
                        select the domains to be avoided. The format should
                        include the initial '.'.
  -F, --file-header <alternative_header_file>
                        header for the output filenames to be generated. If
                        None was provided the following will be used:
                        profiles.<extension>.
  -T, --threads <num_threads>
                        write down the number of threads to be used (default
                        16). If 0, the maximum number possible will be used,
                        which may make the system feel unstable.
  --quiet               tells the program not to show anything.
  --whois               tells the program to launch whois queries.
About arguments:
  Showing additional information about this program.
  -h, --help            shows this help and exists.
  --version             shows the version of the program and exists.
Check the README.md file for further details on the usage of this program or
follow us on Twitter in <http://twitter.com/i3visio>.
```

### `mailfy`

官方给出的调用示例：`mailfy -h`

```text
root@kali:~# mailfy -h
usage: mailfy (--license | -m <emails> [<emails> ...] | -M <emails_file> |
              -n <nicks> [<nicks> ...] | -N <nicks_file> |
              --create-emails <nicks_file>) [-e <sum_ext> [<sum_ext> ...]]
              [-d <candidate_domains> [<candidate_domains> ...]]
              [-o <path_to_output_folder>] [-p <platform> [<platform> ...]]
              [-x <domain> [<domain> ...]] [-F <alternative_header_file>]
              [-T <num_threads>] [--quiet] [-h] [--version]
mailfy - Checking the existence of a given mail.
Input options (one required):
  --license             shows the GPLv3+ license and exists.
  -m, --emails <emails> [<emails> ...]
                        the list of emails to be checked.
  -M, --emails-file <emails_file>
                        the file with the list of emails.
  -n, --nicks <nicks> [<nicks> ...]
                        the list of nicks to be checked in the domains
                        selected.
  -N, --nicks-file <nicks_file>
                        the file with the list of nicks to be checked in the
                        domains selected.
  --create-emails <nicks_file>
                        the file with the list of nicks to be created in the
                        domains selected.
Processing arguments:
  Configuring the way in which mailfy will process the identified profiles.
  -e, --extension <sum_ext> [<sum_ext> ...]
                        output extension for the summary files. Default: csv.
  -d, --domains <candidate_domains> [<candidate_domains> ...]
                        list of domains where the nick will be looked for.
  -o, --output-folder <path_to_output_folder>
                        output folder for the generated documents. While if
                        the paths does not exist, usufy.py will try to create;
                        if this argument is not provided, usufy will NOT write
                        any down any data. Check permissions if something goes
                        wrong.
  -p, --platforms <platform> [<platform> ...]
                        select the platforms where you want to perform the
                        search amongst the following: ['all', 'infojobs',
                        'instagram', 'keyserverubuntu', 'okcupid']. More than
                        one option can be selected.
  -x, --exclude <domain> [<domain> ...]
                        select the domains to be excluded from the search.
  -F, --file-header <alternative_header_file>
                        Header for the output filenames to be generated. If
                        None was provided the following will be used:
                        profiles.<extension>.
  -T, --threads <num_threads>
                        write down the number of threads to be used (default
                        16). If 0, the maximum number possible will be used,
                        which may make the system feel unstable.
  --quiet               tells the program not to show anything.
About arguments:
  Showing additional information about this program.
  -h, --help            shows this help and exists.
  --version             shows the version of the program and exists.
Check the README.md file for further details on the usage of this program or
follow us on Twitter in <http://twitter.com/i3visio>.
```

### `mailfy.py（示例）`

官方给出的调用示例：`mailfy.py -h`

```text
root@kali:~# mailfy.py -h
usage: mailfy (--license | -m <emails> [<emails> ...] | -M <emails_file> |
              -n <nicks> [<nicks> ...] | -N <nicks_file> |
              --create-emails <nicks_file>) [-e <sum_ext> [<sum_ext> ...]]
              [-d <candidate_domains> [<candidate_domains> ...]]
              [-o <path_to_output_folder>] [-p <platform> [<platform> ...]]
              [-x <domain> [<domain> ...]] [-F <alternative_header_file>]
              [-T <num_threads>] [--quiet] [-h] [--version]
mailfy - Checking the existence of a given mail.
Input options (one required):
  --license             shows the GPLv3+ license and exists.
  -m, --emails <emails> [<emails> ...]
                        the list of emails to be checked.
  -M, --emails-file <emails_file>
                        the file with the list of emails.
  -n, --nicks <nicks> [<nicks> ...]
                        the list of nicks to be checked in the domains
                        selected.
  -N, --nicks-file <nicks_file>
                        the file with the list of nicks to be checked in the
                        domains selected.
  --create-emails <nicks_file>
                        the file with the list of nicks to be created in the
                        domains selected.
Processing arguments:
  Configuring the way in which mailfy will process the identified profiles.
  -e, --extension <sum_ext> [<sum_ext> ...]
                        output extension for the summary files. Default: csv.
  -d, --domains <candidate_domains> [<candidate_domains> ...]
                        list of domains where the nick will be looked for.
  -o, --output-folder <path_to_output_folder>
                        output folder for the generated documents. While if
                        the paths does not exist, usufy.py will try to create;
                        if this argument is not provided, usufy will NOT write
                        any down any data. Check permissions if something goes
                        wrong.
  -p, --platforms <platform> [<platform> ...]
                        select the platforms where you want to perform the
                        search amongst the following: ['all', 'infojobs',
                        'instagram', 'keyserverubuntu', 'okcupid']. More than
                        one option can be selected.
  -x, --exclude <domain> [<domain> ...]
                        select the domains to be excluded from the search.
  -F, --file-header <alternative_header_file>
                        Header for the output filenames to be generated. If
                        None was provided the following will be used:
                        profiles.<extension>.
  -T, --threads <num_threads>
                        write down the number of threads to be used (default
                        16). If 0, the maximum number possible will be used,
                        which may make the system feel unstable.
  --quiet               tells the program not to show anything.
About arguments:
  Showing additional information about this program.
  -h, --help            shows this help and exists.
  --version             shows the version of the program and exists.
Check the README.md file for further details on the usage of this program or
follow us on Twitter in <http://twitter.com/i3visio>.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install osrframework`，再执行 `osrframework --version` 2>/dev/null || `osrframework -V`
- [ ] **2.** **读官方帮助** —— `osrframework -h`，需要细节时 `man osrframework`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `osrframework -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/osrframework/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/osrframework/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/osrframework/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
