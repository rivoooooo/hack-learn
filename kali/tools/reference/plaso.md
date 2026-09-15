# plaso

> Super timeline all the things – metapackage This is a metapackage that depends on the Python 3 package of the Plaso libraries and scripts.

> **功能分类**：数字取证 ｜ **Kali 包**：`plaso` ｜ **官方文档**：<https://www.kali.org/tools/plaso/>

## 1. 安装

```bash
sudo apt update
sudo apt install plaso
```

| 项目 | 内容 |
|------|------|
| 版本 | 20260119 |
| 架构 | all |
| 可执行命令 | `plaso`、`python3-plaso`、`plaso-image_export`、`plaso-log2timeline`、`plaso-pinfo`、`plaso-psort`、`plaso-psteal` |
| 依赖 | `python3-plaso`、`python3-plaso` |
| 安装体积 | 39 KB |
| 官网 | <https://github.com/log2timeline/plaso> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/plaso> |
| 包追踪 | <https://pkg.kali.org/pkg/plaso> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
plaso -h          # 查看用法
man plaso         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 7 个可执行命令，下面是官方页面内嵌的帮助原文。

### `plaso-image_export`

官方给出的调用示例：`plaso-image_export -h`

```text
root@kali:~# plaso-image_export -h
usage: plaso-image_export [-h] [--troubles] [-V] [-d] [-q] [-u]
                          [--artifact_definitions PATH]
                          [--custom_artifact_definitions PATH] [--data PATH]
                          [--process_memory_limit SIZE] [--vfs_back_end TYPE]
                          [--logfile FILENAME] [--partitions PARTITIONS]
                          [--volumes VOLUMES] [--no_vss] [--vss_only]
                          [--vss_stores VSS_STORES] [--credential TYPE:DATA]
                          [--artifact_filters ARTIFACT_FILTERS]
                          [--artifact_filters_file PATH]
                          [--date-filter TYPE_START_END] [-f FILE_FILTER]
                          [-x EXTENSIONS] [--names NAMES]
                          [--signatures IDENTIFIERS] [--enable_artifacts_map]
                          [-w PATH] [--include_duplicates] [--no_hashes]
                          [IMAGE]
This is a simple collector designed to export files inside an image, both within a regular RAW image as well as inside a VSS. The tool uses a collection filter that uses the same syntax as a targeted plaso filter.
positional arguments:
  IMAGE                 The full path to the image file that we are about to
                        extract files from, it should be a raw image or
                        another image that Plaso supports.
options:
  -h, --help            Show this help message and exit.
  --troubles            Show troubleshooting information.
  -V, --version         Show the version information.
  -d, --debug           Enable debug output.
  -q, --quiet           Disable informational output.
  -u, --unattended      Enable unattended mode and do not ask the user for
                        additional input when needed, but terminate with an
                        error instead.
  --artifact_definitions, --artifact-definitions PATH
                        Path to a directory or file containing artifact
                        definitions, which are .yaml files. Artifact
                        definitions can be used to describe and quickly
                        collect data of interest, such as specific files or
                        Windows Registry keys.
  --custom_artifact_definitions, --custom-artifact-definitions PATH
                        Path to a directory or file containing custom artifact
                        definitions, which are .yaml files. Artifact
                        definitions can be used to describe and quickly
                        collect data of interest, such as specific files or
                        Windows Registry keys.
  --data PATH           Path to a directory containing the data files.
  --process_memory_limit, --process-memory-limit SIZE
                        Maximum amount of memory (data segment) a process is
                        allowed to allocate in bytes, where 0 represents no
                        limit. The default limit is 4294967296 (4 GiB). This
                        applies to both the main (foreman) process and the
                        worker processes. This limit is enforced by the
                        operating system and will supersede the worker memory
                        limit (--worker_memory_limit).
  --vfs_back_end, --vfs-back-end TYPE
                        The preferred dfVFS back-end: "auto", "fsext",
                        "fsfat", "fshfs", "fsntfs", "tsk" or "vsgpt".
  --logfile, --log_file, --log-file FILENAME
                        Path of the file in which to store log messages, by
                        default this file will be named: "image_export-
                        YYYYMMDDThhmmss.log.gz". Note that the file will be
                        gzip compressed if the extension is ".gz".
  --partitions, --partition PARTITIONS
                        Define partitions to be processed. A range of
                        partitions can be defined as: "3..5". Multiple
                        partitions can be defined as: "1,3,5" (a list of comma
                        separated values). Ranges and lists can also be
                        combined as: "1,3..5". The first partition is 1. All
                        partitions can be specified with: "all".
  --volumes, --volume VOLUMES
                        Define volumes to be processed. A range of volumes can
                        be defined as: "3..5". Multiple volumes can be defined
                        as: "1,3,5" (a list of comma separated values). Ranges
                        and lists can also be combined as: "1,3..5". The first
                        volume is 1. All volumes can be specified with: "all".
  --no_vss, --no-vss    Do not scan for Volume Shadow Snapshots (VSS). This
                        means that Volume Shadow Snapshots (VSS) are not
                        processed. WARNING: this option is deprecated use
                        --vss_stores=none instead.
  --vss_only, --vss-only
                        Do not process the current volume if Volume Shadow
                        Snapshots (VSS) have been selected.
  --vss_stores, --vss-stores VSS_STORES
                        Define Volume Shadow Snapshots (VSS) (or stores) that
                        need to be processed. A range of snapshots can be
                        defined as: "3..5". Multiple snapshots can be defined
                        as: "1,3,5" (a list of comma separated values). Ranges
                        and lists can also be combined as: "1,3..5". The first
                        snapshot is 1. All snapshots can be defined as: "all"
                        and no snapshots as: "none".
  --credential TYPE:DATA
                        Define a credentials that can be used to unlock
                        encrypted volumes e.g. BitLocker. The credential is
                        defined as type:data e.g. "password:BDE-test".
                        Supported credential types are: key_data, password,
                        recovery_password, startup_key. Binary key data is
                        expected to be passed in BASE-16 encoding
                        (hexadecimal). WARNING credentials passed via command
                        line arguments can end up in logs, so use this option
                        with care.
  --artifact_filters, --artifact-filters ARTIFACT_FILTERS
                        Names of forensic artifact definitions, provided on
                        the command command line (comma separated). Forensic
                        artifacts are stored in .yaml files that are directly
                        pulled from the artifact definitions project. You can
                        also specify a custom artifacts yaml file (see
                        --custom_artifact_definitions). Artifact definitions
                        can be used to describe and quickly collect data of
                        interest, such as specific files or Windows Registry
                        keys.
  --artifact_filters_file, --artifact-filters_file PATH
                        Names of forensic artifact definitions, provided in a
                        file with one artifact name per line. Forensic
                        artifacts are stored in .yaml files that are directly
                        pulled from the artifact definitions project. You can
                        also specify a custom artifacts yaml file (see
                        --custom_artifact_definitions). Artifact definitions
                        can be used to describe and quickly collect data of
                        interest, such as specific files or Windows Registry
                        keys.
  --date-filter, --date_filter TYPE_START_END
                        Filter based on file entry date and time ranges. This
                        parameter is formatted as
                        "TIME_VALUE,START_DATE_TIME,END_DATE_TIME" where
                        TIME_VALUE defines which file entry timestamp the
                        filter applies to e.g. atime, ctime, crtime, bkup,
                        etc. START_DATE_TIME and END_DATE_TIME define
                        respectively the start and end of the date time range.
                        A date time range requires at minimum start or end to
                        time of the boundary and END defines the end time.
                        Both timestamps be set. The date time values are
                        formatted as: YYYY-MM-DD hh:mm:ss.######[+-]##:##
                        Where # are numeric digits ranging from 0 to 9 and the
                        seconds fraction can be either 3 or 6 digits. The time
                        of day, seconds fraction and time zone offset are
                        optional. The default time zone is UTC. E.g. "atime,
                        2013-01-01 23:12:14, 2013-02-23". This parameter can
                        be repeated as needed to add additional date
                        boundaries, e.g. once for atime, once for crtime, etc.
  -f, --filter-file, --filter_file, --file-filter, --file_filter FILE_FILTER
                        List of files to include for targeted collection of
                        files to parse, one line per file path, setup is
                        /path|file - where each element can contain either a
                        variable set in the preprocessing stage or a regular
                        expression.
  -x, --extensions EXTENSIONS
                        Filter on file name extensions. This option accepts
                        multiple multiple comma separated values e.g.
                        "csv,docx,pst".
  --names NAMES         Filter on file names. This option accepts a comma
                        separated string denoting all file names, e.g. -x
                        "NTUSER.DAT,UsrClass.dat".
  --signatures IDENTIFIERS
                        Filter on file format signature identifiers. This
                        option accepts multiple comma separated values e.g.
                        "esedb,lnk". Use "list" to show an overview of the
                        supported file format signatures.
  --enable_artifacts_map
                        Output a JSON file mapping extracted files/directories
                        to artifact definitions.
  -w, --write PATH      The directory in which extracted files should be
                        stored.
  --include_duplicates, --include-duplicates
                        By default a digest hash (SHA-256) is calculated for
                        each file (data stream). These hashes are compared to
                        the previously exported files and duplicates are
                        skipped. Use this option to include duplicate files in
                        the export.
  --no_hashes, --no-hashes
                        Do not generate the hashes.json file
And that is how you export files, plaso style.
```

### `plaso-log2timeline`

官方给出的调用示例：`plaso-log2timeline -h`

```text
root@kali:~# plaso-log2timeline -h
usage: plaso-log2timeline [-h] [--troubles] [-V] [--artifact_definitions PATH]
                          [--custom_artifact_definitions PATH] [--data PATH]
                          [--archives TYPES]
                          [--artifact_filters ARTIFACT_FILTERS]
                          [--artifact_filters_file PATH]
                          [--extract_winreg_binary] [--preferred_year YEAR]
                          [--skip_compressed_streams] [-f FILE_FILTER]
                          [--hasher_file_size_limit SIZE]
                          [--hashers HASHER_LIST]
                          [--parsers PARSER_FILTER_EXPRESSION]
                          [--yara_rules PATH] [--partitions PARTITIONS]
                          [--volumes VOLUMES] [--codepage CODEPAGE]
                          [--language LANGUAGE_TAG]
                          [--no_extract_winevt_resources] [-z TIME_ZONE]
                          [--no_vss] [--vss_only] [--vss_stores VSS_STORES]
                          [--credential TYPE:DATA] [-d] [-q] [-u] [--info]
                          [--use_markdown] [--no_dependencies_check]
                          [--logfile FILENAME] [--status_view TYPE]
                          [--status_view_file PATH]
                          [--status_view_interval SECONDS]
                          [--buffer_size BUFFER_SIZE]
                          [--queue_size QUEUE_SIZE] [--single_process]
                          [--process_memory_limit SIZE]
                          [--temporary_directory DIRECTORY]
                          [--vfs_back_end TYPE] [--worker_memory_limit SIZE]
                          [--worker_timeout MINUTES] [--workers WORKERS]
                          [--sigsegv_handler] [--profilers PROFILERS_LIST]
                          [--profiling_directory DIRECTORY]
                          [--profiling_sample_rate SAMPLE_RATE]
                          [--storage_file PATH] [--storage_format FORMAT]
                          [--task_storage_format FORMAT]
                          [SOURCE]
log2timeline is a command line tool to extract events from individual
files, recursing a directory (e.g. mount point) or storage media
image or device.
More information can be gathered from here:
    https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html
positional arguments:
  SOURCE                Path to a source device, file or directory. If the
                        source is a supported storage media device or image
                        file, archive file or a directory, the files within
                        are processed recursively.
options:
  -h, --help            Show this help message and exit.
  --troubles            Show troubleshooting information.
  -V, --version         Show the version information.
data location arguments:
  --artifact_definitions, --artifact-definitions PATH
                        Path to a directory or file containing artifact
                        definitions, which are .yaml files. Artifact
                        definitions can be used to describe and quickly
                        collect data of interest, such as specific files or
                        Windows Registry keys.
  --custom_artifact_definitions, --custom-artifact-definitions PATH
                        Path to a directory or file containing custom artifact
                        definitions, which are .yaml files. Artifact
                        definitions can be used to describe and quickly
                        collect data of interest, such as specific files or
                        Windows Registry keys.
  --data PATH           Path to a directory containing the data files.
extraction arguments:
  --archives TYPES      Define a list of archive and storage media image types
                        for which to process embedded file entries, such as
                        TAR (archive.tar) or ZIP (archive.zip). This is a
                        comma separated list where each entry is the name of
                        an archive type, such as "tar,zip". "all" indicates
                        that all archive types should be enabled. "none"
                        disables processing file entries embedded in archives.
                        Use "--archives list" to list the available archive
                        types. WARNING: this can make processing significantly
                        slower.
  --artifact_filters, --artifact-filters ARTIFACT_FILTERS
                        Names of forensic artifact definitions, provided on
                        the command command line (comma separated). Forensic
                        artifacts are stored in .yaml files that are directly
                        pulled from the artifact definitions project. You can
                        also specify a custom artifacts yaml file (see
                        --custom_artifact_definitions). Artifact definitions
                        can be used to describe and quickly collect data of
                        interest, such as specific files or Windows Registry
                        keys.
  --artifact_filters_file, --artifact-filters_file PATH
                        Names of forensic artifact definitions, provided in a
                        file with one artifact name per line. Forensic
                        artifacts are stored in .yaml files that are directly
                        pulled from the artifact definitions project. You can
                        also specify a custom artifacts yaml file (see
                        --custom_artifact_definitions). Artifact definitions
                        can be used to describe and quickly collect data of
                        interest, such as specific files or Windows Registry
                        keys.
  --extract_winreg_binary, --extract-winreg-binary
                        Extract binary Windows Registry values. WARNING: This
                        can make processing significantly slower.
  --preferred_year, --preferred-year YEAR
                        When a format's timestamp does not include a year,
                        e.g. syslog, use this as the initial year instead of
                        attempting auto-detection.
  --skip_compressed_streams, --skip-compressed-streams
                        Skip processing file content within compressed
                        streams, such as syslog.gz and syslog.bz2.
  -f, --filter-file, --filter_file, --file-filter, --file_filter FILE_FILTER
                        List of files to include for targeted collection of
                        files to parse, one line per file path, setup is
                        /path|file - where each element can contain either a
                        variable set in the preprocessing stage or a regular
                        expression.
  --hasher_file_size_limit, --hasher-file-size-limit SIZE
                        Define the maximum file size in bytes that hashers
                        should process. Any larger file will be skipped. A
                        size of 0 represents no limit.
  --hashers HASHER_LIST
                        Define a list of hashers to use by the tool. This is a
                        comma separated list where each entry is the name of a
                        hasher, such as "md5,sha256". "all" indicates that all
                        hashers should be enabled. "none" disables all
                        hashers. Use "--hashers list" or "--info" to list the
                        available hashers.
  --parsers PARSER_FILTER_EXPRESSION
                        Define which presets, parsers and/or plugins to use,
                        or show possible values. The expression is a comma
                        separated string where each element is a preset,
                        parser or plugin name. Each element can be prepended
                        with an exclamation mark to exclude the item. Matching
                        is case insensitive. Examples: "linux,!bash_history"
                        enables the linux preset, without the bash_history
                        parser. "sqlite,!sqlite/chrome_history" enables all
                        sqlite plugins except for chrome_history".
                        "win7,syslog" enables the win7 preset, as well as the
                        syslog parser. Use "--parsers list" or "--info" to
                        list available presets, parsers and plugins.
  --yara_rules, --yara-rules PATH
                        Path to a file containing Yara rules definitions.
  --partitions, --partition PARTITIONS
                        Define partitions to be processed. A range of
                        partitions can be defined as: "3..5". Multiple
                        partitions can be defined as: "1,3,5" (a list of comma
                        separated values). Ranges and lists can also be
                        combined as: "1,3..5". The first partition is 1. All
                        partitions can be specified with: "all".
  --volumes, --volume VOLUMES
                        Define volumes to be processed. A range of volumes can
                        be defined as: "3..5". Multiple volumes can be defined
                        as: "1,3,5" (a list of comma separated values). Ranges
                        and lists can also be combined as: "1,3..5". The first
                        volume is 1. All volumes can be specified with: "all".
  --codepage CODEPAGE   The preferred codepage, which is used for decoding
                        single-byte or multi-byte character extracted strings.
  --language LANGUAGE_TAG
                        The preferred language, which is used for extracting
                        and formatting Windows EventLog message strings. Use "
                        --language list" to see a list of supported language
                        tags. The en-US (LCID 0x0409) language is used as
                        fallback if preprocessing could not determine the
                        system language or no language information is
                        available in the winevt-rc.db database.
  --no_extract_winevt_resources, --no-extract-winevt-resources
                        Do not extract Windows EventLog resources such as
                        event message template strings. By default Windows
                        EventLog resources will be extracted when a Windows
                        EventLog parser is enabled.
  -z, --zone, --timezone TIME_ZONE
                        preferred time zone of extracted date and time values
                        that are stored without a time zone indicator. The
                        time zone is determined based on the source data where
                        possible otherwise it will default to UTC. Use "list"
                        to see a list of available time zones.
  --no_vss, --no-vss    Do not scan for Volume Shadow Snapshots (VSS). This
                        means that Volume Shadow Snapshots (VSS) are not
                        processed. WARNING: this option is deprecated use
                        --vss_stores=none instead.
  --vss_only, --vss-only
                        Do not process the current volume if Volume Shadow
                        Snapshots (VSS) have been selected.
  --vss_stores, --vss-stores VSS_STORES
                        Define Volume Shadow Snapshots (VSS) (or stores) that
                        need to be processed. A range of snapshots can be
                        defined as: "3..5". Multiple snapshots can be defined
                        as: "1,3,5" (a list of comma separated values). Ranges
                        and lists can also be combined as: "1,3..5". The first
                        snapshot is 1. All snapshots can be defined as: "all"
                        and no snapshots as: "none".
  --credential TYPE:DATA
                        Define a credentials that can be used to unlock
                        encrypted volumes e.g. BitLocker. The credential is
                        defined as type:data e.g. "password:BDE-test".
                        Supported credential types are: key_data, password,
                        recovery_password, startup_key. Binary key data is
                        expected to be passed in BASE-16 encoding
                        (hexadecimal). WARNING credentials passed via command
                        line arguments can end up in logs, so use this option
                        with care.
informational arguments:
  -d, --debug           Enable debug output.
  -q, --quiet           Disable informational output.
  -u, --unattended      Enable unattended mode and do not ask the user for
                        additional input when needed, but terminate with an
                        error instead.
  --info                Print out information about supported plugins and
                        parsers.
  --use_markdown, --use-markdown
                        Output lists in Markdown format use in combination
                        with "--hashers list", "--parsers list" or "--timezone
                        list"
  --no_dependencies_check, --no-dependencies-check
                        Disable the dependencies check.
  --logfile, --log_file, --log-file FILENAME
                        Path of the file in which to store log messages, by
                        default this file will be named: "log2timeline-
                        YYYYMMDDThhmmss.log.gz". Note that the file will be
                        gzip compressed if the extension is ".gz".
  --status_view, --status-view TYPE
                        The processing status view mode: "file", "linear",
                        "none" or "window".
  --status_view_file, --status-view-file PATH
                        The name of the status view file.
  --status_view_interval, --status-view-interval SECONDS
                        Number of seconds to update the status view.
processing arguments:
```

### `plaso-pinfo`

官方给出的调用示例：`plaso-pinfo -h`

```text
root@kali:~# plaso-pinfo -h
usage: plaso-pinfo [-h] [--troubles] [-V] [--logfile FILENAME]
                   [--process_memory_limit SIZE] [--compare STORAGE_FILE]
                   [--output_format FORMAT] [--hash TYPE] [--report TYPE]
                   [--sections SECTIONS_LIST] [-v] [-w OUTPUTFILE]
                   [PATH]
Shows information about a Plaso storage file, for example how it was collected, what information was extracted from a source, etc.
positional arguments:
  PATH                  Path to a storage file.
options:
  -h, --help            Show this help message and exit.
  --troubles            Show troubleshooting information.
  -V, --version         Show the version information.
  --logfile, --log_file, --log-file FILENAME
                        Path of the file in which to store log messages, by
                        default this file will be named: "pinfo-
                        YYYYMMDDThhmmss.log.gz". Note that the file will be
                        gzip compressed if the extension is ".gz".
  --process_memory_limit, --process-memory-limit SIZE
                        Maximum amount of memory (data segment) a process is
                        allowed to allocate in bytes, where 0 represents no
                        limit. The default limit is 4294967296 (4 GiB). This
                        applies to both the main (foreman) process and the
                        worker processes. This limit is enforced by the
                        operating system and will supersede the worker memory
                        limit (--worker_memory_limit).
  --compare STORAGE_FILE
                        The path of the storage file to compare against.
  --output_format, --output-format FORMAT
                        Format of the output, the default is: text. Supported
                        options: json, markdown, text.
  --hash TYPE           Type of hash to output in file_hashes report.
                        Supported options: md5, sha1, sha256
  --report TYPE         Report on specific information. Supported options:
                        browser_search, chrome_extension,
                        environment_variables, file_hashes, list, none,
                        windows_services, winevt_providers
  --sections SECTIONS_LIST
                        List of sections to output. This is a comma separated
                        list where each entry is the name of a section. Use "
                        --sections list" to list the available sections and "
                        --sections all" to show all available sections.
  -v, --verbose         Print verbose output.
  -w, --write OUTPUTFILE
                        Output filename.
```

### `plaso-psort`

官方给出的调用示例：`plaso-psort -h`

```text
root@kali:~# plaso-psort -h
usage: plaso-psort [-h] [--troubles] [-V] [--analysis PLUGIN_LIST]
                   [--process_memory_limit SIZE]
                   [--temporary_directory DIRECTORY]
                   [--worker_memory_limit SIZE] [--worker_timeout MINUTES]
                   [--logfile FILENAME] [-d] [-q] [-u] [--status_view TYPE]
                   [--status_view_file PATH] [--status_view_interval SECONDS]
                   [--slice DATE_TIME] [--slice_size SLICE_SIZE] [--slicer]
                   [--data PATH] [-a] [--language LANGUAGE_TAG]
                   [--additional_fields ADDITIONAL_FIELDS]
                   [--custom_fields CUSTOM_FIELDS]
                   [--custom_formatter_definitions PATH] [--dynamic_time]
                   [--output_time_zone TIME_ZONE] [-o FORMAT] [-w OUTPUT_FILE]
                   [--fields FIELDS] [--profilers PROFILERS_LIST]
                   [--profiling_directory DIRECTORY]
                   [--profiling_sample_rate SAMPLE_RATE]
                   [PATH] [FILTER]
Application to read, filter and process output from a Plaso storage file.
positional arguments:
  PATH                  Path to a storage file.
options:
  -h, --help            Show this help message and exit.
  --troubles            Show troubleshooting information.
  -V, --version         Show the version information.
Analysis Arguments:
  --analysis PLUGIN_LIST
                        A comma separated list of analysis plugin names to be
                        loaded or "--analysis list" to see a list of available
                        plugins.
Processing:
  --process_memory_limit, --process-memory-limit SIZE
                        Maximum amount of memory (data segment) a process is
                        allowed to allocate in bytes, where 0 represents no
                        limit. The default limit is 4294967296 (4 GiB). This
                        applies to both the main (foreman) process and the
                        worker processes. This limit is enforced by the
                        operating system and will supersede the worker memory
                        limit (--worker_memory_limit).
  --temporary_directory, --temporary-directory DIRECTORY
                        Path to the directory that should be used to store
                        temporary files created during processing.
  --worker_memory_limit, --worker-memory-limit SIZE
                        Maximum amount of memory (data segment and shared
                        memory) a worker process is allowed to consume in
                        bytes, where 0 represents no limit. The default limit
                        is 2147483648 (2 GiB). If a worker process exceeds
                        this limit it is killed by the main (foreman) process.
  --worker_timeout, --worker-timeout MINUTES
                        Number of minutes before a worker process that is not
                        providing status updates is considered inactive. The
                        default timeout is 15.0 minutes. If a worker process
                        exceeds this timeout it is killed by the main
                        (foreman) process.
Informational Arguments:
  --logfile, --log_file, --log-file FILENAME
                        Path of the file in which to store log messages, by
                        default this file will be named: "psort-
                        YYYYMMDDThhmmss.log.gz". Note that the file will be
                        gzip compressed if the extension is ".gz".
  -d, --debug           Enable debug output.
  -q, --quiet           Disable informational output.
  -u, --unattended      Enable unattended mode and do not ask the user for
                        additional input when needed, but terminate with an
                        error instead.
  --status_view, --status-view TYPE
                        The processing status view mode: "file", "linear",
                        "none" or "window".
  --status_view_file, --status-view-file PATH
                        The name of the status view file.
  --status_view_interval, --status-view-interval SECONDS
                        Number of seconds to update the status view.
Filter Arguments:
  --slice DATE_TIME     Date and time to create a time slice around. This
                        parameter, if defined, will display all events that
                        happened X minutes before and after the defined date,
                        where X is controlled by the --slice_size option,
                        which is 5 minutes by default. The date and time must
                        be specified in ISO 8601 format including time zone
                        offset, for example: 20200619T20:09:23+02:00.
  --slice_size, --slice-size SLICE_SIZE
                        Defines the slice size. In the case of a regular time
                        slice it defines the number of minutes the slice size
                        should be. In the case of the --slicer it determines
                        the number of events before and after a filter match
                        has been made that will be included in the result set.
                        The default value is 5. See --slice or --slicer for
                        more details about this option.
  --slicer              Create a time slice around every filter match. This
                        parameter, if defined will save all X events before
                        and after a filter match has been made. X is defined
                        by the --slice_size parameter.
  FILTER                A filter that can be used to filter the dataset before
                        it is written into storage. More information about the
                        filters and how to use them can be found here: https:/
                        /plaso.readthedocs.io/en/latest/sources/user/Event-
                        filters.html
Input Arguments:
  --data PATH           Path to a directory containing the data files.
Output Arguments:
  -a, --include_all, --include-all
                        By default the psort removes duplicate entries from
                        the output. This parameter changes that behavior so
                        all events are included.
  --language LANGUAGE_TAG
                        The preferred language, which is used for extracting
                        and formatting Windows EventLog message strings. Use "
                        --language list" to see a list of supported language
                        tags. The en-US (LCID 0x0409) language is used as
                        fallback if preprocessing could not determine the
                        system language or no language information is
                        available in the winevt-rc.db database.
  --additional_fields, --additional-fields ADDITIONAL_FIELDS
                        Defines additional fields to be included in the output
                        besides the default fields. Multiple additional field
                        names can be defined as a list of comma separated
                        values. Output formats that support additional fields
                        are: dynamic, opensearch and xlsx.
  --custom_fields, --custom-fields CUSTOM_FIELDS
                        Defines custom fields to be included in the output
                        besides the default fields. A custom field is defined
                        as "name:value". Multiple custom field names can be
                        defined as list of comma separated values. Note that
                        regular fields will are favoured above custom fields
                        with same name. Output formats that support this are:
                        dynamic, opensearch and xlsx.
  --custom_formatter_definitions, --custom-formatter-definitions PATH
                        Path to a file containing custom event formatter
                        definitions, which is a .yaml file. Custom event
                        formatter definitions can be used to customize event
                        messages and override the built-in event formatter
                        definitions.
  --dynamic_time, --dynamic-time
                        Indicate that the output should use dynamic time.
                        Output formats that support dynamic time are: dynamic
  --output_time_zone, --output-time-zone TIME_ZONE
                        time zone of date and time values written to the
                        output, if supported by the output format. Use "list"
                        to see a list of available time zones. Output formats
                        that support an output time zone are: dynamic and
                        l2t_csv.
Output Format Arguments:
  -o, --output_format, --output-format FORMAT
                        The output format. Use "-o list" to see a list of
                        available output formats.
  -w, --write OUTPUT_FILE
                        Output filename.
  --fields FIELDS       Defines which fields should be included in the output.
profiling arguments:
  --profilers PROFILERS_LIST
                        List of profilers to use by the tool. This is a comma
                        separated list where each entry is the name of a
                        profiler. Use "--profilers list" to list the available
                        profilers.
  --profiling_directory, --profiling-directory DIRECTORY
                        Path to the directory that should be used to store the
                        profiling sample files. By default the sample files
                        are stored in the current working directory.
  --profiling_sample_rate, --profiling-sample-rate SAMPLE_RATE
                        Profiling sample rate (defaults to a sample every 1000
                        files).
```

### `plaso-psteal`

官方给出的调用示例：`plaso-psteal -h`

```text
root@kali:~# plaso-psteal -h
usage: plaso-psteal [-h] [--troubles] [-V] [--artifact_definitions PATH]
                    [--custom_artifact_definitions PATH] [--data PATH]
                    [--archives TYPES] [--extract_winreg_binary]
                    [--preferred_year YEAR] [--skip_compressed_streams]
                    [--hasher_file_size_limit SIZE] [--hashers HASHER_LIST]
                    [--parsers PARSER_FILTER_EXPRESSION] [--storage_file PATH]
                    [--partitions PARTITIONS] [--volumes VOLUMES]
                    [--codepage CODEPAGE] [--language LANGUAGE_TAG]
                    [--no_extract_winevt_resources] [-z TIME_ZONE] [--no_vss]
                    [--vss_only] [--vss_stores VSS_STORES]
                    [--credential TYPE:DATA] [-d] [-q] [-u]
                    [--no_dependencies_check] [--status_view TYPE]
                    [--status_view_file PATH] [--status_view_interval SECONDS]
                    [--source SOURCE] [--additional_fields ADDITIONAL_FIELDS]
                    [--custom_fields CUSTOM_FIELDS]
                    [--custom_formatter_definitions PATH] [--dynamic_time]
                    [--output_time_zone TIME_ZONE] [-o FORMAT]
                    [-w OUTPUT_FILE] [--fields FIELDS]
                    [--buffer_size BUFFER_SIZE] [--queue_size QUEUE_SIZE]
                    [--single_process] [--process_memory_limit SIZE]
                    [--temporary_directory DIRECTORY] [--vfs_back_end TYPE]
                    [--worker_memory_limit SIZE] [--worker_timeout MINUTES]
                    [--workers WORKERS]
psteal is a command line tool to extract events from individual
files, recursing a directory (e.g. mount point) or storage media
image or device. The output events will be stored in a storage file.
This tool will then read the output and process the events into a CSV
file.
More information can be gathered from here:
    https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html
options:
  -h, --help            Show this help message and exit.
  --troubles            Show troubleshooting information.
  -V, --version         Show the version information.
data location arguments:
  --artifact_definitions, --artifact-definitions PATH
                        Path to a directory or file containing artifact
                        definitions, which are .yaml files. Artifact
                        definitions can be used to describe and quickly
                        collect data of interest, such as specific files or
                        Windows Registry keys.
  --custom_artifact_definitions, --custom-artifact-definitions PATH
                        Path to a directory or file containing custom artifact
                        definitions, which are .yaml files. Artifact
                        definitions can be used to describe and quickly
                        collect data of interest, such as specific files or
                        Windows Registry keys.
  --data PATH           Path to a directory containing the data files.
extraction arguments:
  --archives TYPES      Define a list of archive and storage media image types
                        for which to process embedded file entries, such as
                        TAR (archive.tar) or ZIP (archive.zip). This is a
                        comma separated list where each entry is the name of
                        an archive type, such as "tar,zip". "all" indicates
                        that all archive types should be enabled. "none"
                        disables processing file entries embedded in archives.
                        Use "--archives list" to list the available archive
                        types. WARNING: this can make processing significantly
                        slower.
  --extract_winreg_binary, --extract-winreg-binary
                        Extract binary Windows Registry values. WARNING: This
                        can make processing significantly slower.
  --preferred_year, --preferred-year YEAR
                        When a format's timestamp does not include a year,
                        e.g. syslog, use this as the initial year instead of
                        attempting auto-detection.
  --skip_compressed_streams, --skip-compressed-streams
                        Skip processing file content within compressed
                        streams, such as syslog.gz and syslog.bz2.
  --hasher_file_size_limit, --hasher-file-size-limit SIZE
                        Define the maximum file size in bytes that hashers
                        should process. Any larger file will be skipped. A
                        size of 0 represents no limit.
  --hashers HASHER_LIST
                        Define a list of hashers to use by the tool. This is a
                        comma separated list where each entry is the name of a
                        hasher, such as "md5,sha256". "all" indicates that all
                        hashers should be enabled. "none" disables all
                        hashers. Use "--hashers list" or "--info" to list the
                        available hashers.
  --parsers PARSER_FILTER_EXPRESSION
                        Define which presets, parsers and/or plugins to use,
                        or show possible values. The expression is a comma
                        separated string where each element is a preset,
                        parser or plugin name. Each element can be prepended
                        with an exclamation mark to exclude the item. Matching
                        is case insensitive. Examples: "linux,!bash_history"
                        enables the linux preset, without the bash_history
                        parser. "sqlite,!sqlite/chrome_history" enables all
                        sqlite plugins except for chrome_history".
                        "win7,syslog" enables the win7 preset, as well as the
                        syslog parser. Use "--parsers list" or "--info" to
                        list available presets, parsers and plugins.
  --storage_file, --storage-file PATH
                        The path of the storage file. If not specified, one
                        will be made in the form <timestamp>-<source>.plaso
  --partitions, --partition PARTITIONS
                        Define partitions to be processed. A range of
                        partitions can be defined as: "3..5". Multiple
                        partitions can be defined as: "1,3,5" (a list of comma
                        separated values). Ranges and lists can also be
                        combined as: "1,3..5". The first partition is 1. All
                        partitions can be specified with: "all".
  --volumes, --volume VOLUMES
                        Define volumes to be processed. A range of volumes can
                        be defined as: "3..5". Multiple volumes can be defined
                        as: "1,3,5" (a list of comma separated values). Ranges
                        and lists can also be combined as: "1,3..5". The first
                        volume is 1. All volumes can be specified with: "all".
  --codepage CODEPAGE   The preferred codepage, which is used for decoding
                        single-byte or multi-byte character extracted strings.
  --language LANGUAGE_TAG
                        The preferred language, which is used for extracting
                        and formatting Windows EventLog message strings. Use "
                        --language list" to see a list of supported language
                        tags. The en-US (LCID 0x0409) language is used as
                        fallback if preprocessing could not determine the
                        system language or no language information is
                        available in the winevt-rc.db database.
  --no_extract_winevt_resources, --no-extract-winevt-resources
                        Do not extract Windows EventLog resources such as
                        event message template strings. By default Windows
                        EventLog resources will be extracted when a Windows
                        EventLog parser is enabled.
  -z, --zone, --timezone TIME_ZONE
                        preferred time zone of extracted date and time values
                        that are stored without a time zone indicator. The
                        time zone is determined based on the source data where
                        possible otherwise it will default to UTC. Use "list"
                        to see a list of available time zones.
  --no_vss, --no-vss    Do not scan for Volume Shadow Snapshots (VSS). This
                        means that Volume Shadow Snapshots (VSS) are not
                        processed. WARNING: this option is deprecated use
                        --vss_stores=none instead.
  --vss_only, --vss-only
                        Do not process the current volume if Volume Shadow
                        Snapshots (VSS) have been selected.
  --vss_stores, --vss-stores VSS_STORES
                        Define Volume Shadow Snapshots (VSS) (or stores) that
                        need to be processed. A range of snapshots can be
                        defined as: "3..5". Multiple snapshots can be defined
                        as: "1,3,5" (a list of comma separated values). Ranges
                        and lists can also be combined as: "1,3..5". The first
                        snapshot is 1. All snapshots can be defined as: "all"
                        and no snapshots as: "none".
  --credential TYPE:DATA
                        Define a credentials that can be used to unlock
                        encrypted volumes e.g. BitLocker. The credential is
                        defined as type:data e.g. "password:BDE-test".
                        Supported credential types are: key_data, password,
                        recovery_password, startup_key. Binary key data is
                        expected to be passed in BASE-16 encoding
                        (hexadecimal). WARNING credentials passed via command
                        line arguments can end up in logs, so use this option
                        with care.
informational arguments:
  -d, --debug           Enable debug output.
  -q, --quiet           Disable informational output.
  -u, --unattended      Enable unattended mode and do not ask the user for
                        additional input when needed, but terminate with an
                        error instead.
  --no_dependencies_check, --no-dependencies-check
                        Disable the dependencies check.
  --status_view, --status-view TYPE
                        The processing status view mode: "file", "linear",
                        "none" or "window".
  --status_view_file, --status-view-file PATH
                        The name of the status view file.
  --status_view_interval, --status-view-interval SECONDS
                        Number of seconds to update the status view.
input arguments:
  --source SOURCE       The source to process
output arguments:
  --additional_fields, --additional-fields ADDITIONAL_FIELDS
                        Defines additional fields to be included in the output
                        besides the default fields. Multiple additional field
                        names can be defined as a list of comma separated
                        values. Output formats that support additional fields
                        are: dynamic, opensearch and xlsx.
  --custom_fields, --custom-fields CUSTOM_FIELDS
                        Defines custom fields to be included in the output
                        besides the default fields. A custom field is defined
                        as "name:value". Multiple custom field names can be
                        defined as list of comma separated values. Note that
                        regular fields will are favoured above custom fields
                        with same name. Output formats that support this are:
                        dynamic, opensearch and xlsx.
  --custom_formatter_definitions, --custom-formatter-definitions PATH
                        Path to a file containing custom event formatter
                        definitions, which is a .yaml file. Custom event
                        formatter definitions can be used to customize event
                        messages and override the built-in event formatter
                        definitions.
  --dynamic_time, --dynamic-time
                        Indicate that the output should use dynamic time.
                        Output formats that support dynamic time are: dynamic
  --output_time_zone, --output-time-zone TIME_ZONE
                        time zone of date and time values written to the
                        output, if supported by the output format. Use "list"
                        to see a list of available time zones. Output formats
                        that support an output time zone are: dynamic and
                        l2t_csv.
output format arguments:
  -o, --output_format, --output-format FORMAT
                        The output format. Use "-o list" to see a list of
                        available output formats.
  -w, --write OUTPUT_FILE
                        Output filename.
  --fields FIELDS       Defines which fields should be included in the output.
processing arguments:
  --buffer_size, --buffer-size, --bs BUFFER_SIZE
                        The buffer size for the output (defaults to 196MiB).
  --queue_size, --queue-size QUEUE_SIZE
                        The maximum number of queued items per worker
                        (defaults to 125000)
  --single_process, --single-process
                        Indicate that the tool should run in a single process.
  --process_memory_limit, --process-memory-limit SIZE
                        Maximum amount of memory (data segment) a process is
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install plaso`，再执行 `plaso --version` 2>/dev/null || `plaso -V`
- [ ] **2.** **读官方帮助** —— `plaso -h`，需要细节时 `man plaso`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `plaso -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/plaso/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/plaso/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/plaso/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
