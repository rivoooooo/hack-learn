# php-defaults

> Server-side, HTML-embedded scripting language (Apache 2 module) (default) This package provides the PHP module for the Apache 2 webserver. PHP (recursive acronym for PHP: Hypertext Preprocessor) is a widely-used open source general-purpose…

> **功能分类**：Web 应用 ｜ **Kali 包**：`php-defaults` ｜ **官方文档**：<https://www.kali.org/tools/php-defaults/>

## 1. 安装

```bash
sudo apt update
sudo apt install libapache2-mod-php
```

| 项目 | 内容 |
|------|------|
| 版本 | 99 |
| 架构 | all |
| 可执行命令 | `libapache2-mod-php`、`libphp-embed`、`php`、`php-all-dev`、`php-bcmath`、`php-bz2`、`php-cgi`、`php-cgi.default`、`php-cli`、`phar.default`、`phar.phar.default`、`php.default`、`php-common`、`phpdismod`、`phpenmod`、`phpquery`、`php-curl`、`php-dev`、`php-config.default`、`phpize.default`、`php-enchant`、`php-fpm`、`php-gd`、`php-gmp`、`php-interbase`、`php-intl`、`php-json`、`php-ldap`、`php-mbstring`、`php-mysql`、`php-odbc`、`php-pgsql`、`php-phpdbg`、`phpdbg.default`、`php-readline`、`php-snmp`、`php-soap`、`php-sqlite3`、`php-sybase`、`php-tidy`、`php-xml`、`php-zip` |
| 依赖 | `libapache2-mod-php8.4`、`libphp-embed` |
| 安装体积 | 15 KB |
| 源码仓库 | <https://salsa.debian.org/php-team/php-defaults> |
| 包追踪 | <https://pkg.kali.org/pkg/php-defaults> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libapache2-mod-php -h          # 查看用法
man libapache2-mod-php         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 42 个可执行命令，下面是官方页面内嵌的帮助原文。

### `php-cgi.default`

官方给出的调用示例：`php-cgi.default -h`

```text
root@kali:~# php-cgi.default -h
Usage: php-cgi [-q] [-h] [-s] [-v] [-i] [-f <file>]
       php-cgi <file> [args...]
  -a               Run interactively
  -b <address:port>|<port> Bind Path for external FASTCGI Server mode
  -C               Do not chdir to the script's directory
  -c <path>|<file> Look for php.ini file in this directory
  -n               No php.ini file will be used
  -d foo[=bar]     Define INI entry foo with value 'bar'
  -e               Generate extended information for debugger/profiler
  -f <file>        Parse <file>.  Implies `-q'
  -h               This help
  -i               PHP information
  -l               Syntax check only (lint)
  -m               Show compiled in modules
  -q               Quiet-mode.  Suppress HTTP Header output.
  -s               Display colour syntax highlighted source.
  -v               Version number
  -w               Display source with stripped comments and whitespace.
  -z <file>        Load Zend extension <file>.
  -T <count>       Measure execution time of script repeated <count> times.
```

### `man`

官方给出的调用示例：`man phar.default`

```text
root@kali:~# man phar.default
PHAR(1)                          User Commands                          PHAR(1)
NAME
     phar, phar.phar - PHAR (PHP archive) command line tool
SYNOPSIS
     phar <command> [options] ...
DESCRIPTION
     The  PHAR file format provides a way to put entire PHP applications into a
     single file called a "phar" (PHP Archive) for easy  distribution  and  in-
     stallation.
     With the phar command you can create, update or extract PHP archives.
     Commands:  add  compress  delete extract help help-list info list meta-del
     meta-get meta-set pack sign stub-get stub-set tree version
add command
     Add entries to a PHAR package.
     Required arguments:
     -f file        Specifies the phar file to work on.
     ...            Any number of input files and directories. If -i is in  use
                    then  ONLY  files and matching the given regular expression
                    are being packed. If -x is given then files  matching  that
                    regular expression are NOT being packed.
     Optional arguments:
     -a alias       Provide an alias name for the phar file.
     -c algo        Compression algorithm (see COMPRESSION )
     -i regex       Specifies a regular expression for input files.
     -l level       Number  of  preceding subdirectories to strip from file en-
                    tries
     -x regex       Regular expression for input files to exclude.
compress command
     Compress or uncompress all files or a selected entry.
     Required arguments:
     -c algo        Compression algorithm (see COMPRESSION )
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -e entry       Name of entry to work on (must include PHAR internal direc-
                    tory name if any).
delete command
     Delete entry from a PHAR archive
     Required arguments:
     -e entry       Name of entry to work on (must include PHAR internal direc-
                    tory name if any).
     -f file        Specifies the phar file to work on.
extract command
     Extract a PHAR package to a directory.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -i regex       Specifies a regular expression for input files.
     -x regex       Regular expression for input files to exclude.
     ...            Directory to extract to (defaults to '.').
help command
     This help or help for a selected command.
     Optional arguments:
     ...            Optional command to retrieve help for.
help-list command
     Lists available commands.
info command
     Get information about a PHAR package.
     By using -k it is possible to return a single value.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -k index       Subscription index to work on.
list command
     List contents of a PHAR archive.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -i regex       Specifies a regular expression for input files.
     -x regex       Regular expression for input files to exclude.
meta-del command
     Delete meta information of a PHAR entry or a PHAR package.
     If -k is given then the metadata is expected to be an array and the  given
     index is being deleted.
     If something was deleted the return value is 0 otherwise it is 1.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -e entry       Name of entry to work on (must include PHAR internal direc-
                    tory name if any).
     -k index       Subscription index to work on.
meta-get command
     Get meta information of a PHAR entry or a PHAR package in serialized from.
     If  no  output  file is specified for meta data then stdout is being used.
     You can also specify a particular index using -k. In that case  the  meta-
     data  is  expected  to be an array and the value of the given index is re-
     turned using echo rather than using serialize. If that index does not  ex-
     ist or no meta data is present then the return value is 1.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -e entry       Name of entry to work on (must include PHAR internal direc-
                    tory name if any).
     -k index       Subscription index to work on.
meta-set command
     Set meta data of a PHAR entry or a PHAR package using serialized input. If
     no input file is specified for meta data then stdin is being used. You can
     also specify a particular index using -k. In that case the metadata is ex-
     pected  to  be an array and the value of the given index is being set.  If
     the metadata is not present or empty a new array will be created.  If  the
     metadata  is present and a flat value then the return value is 1. Also us-
     ing -k the input is been taken directly rather then being serialized.
     Required arguments:
     -f file        Specifies the phar file to work on.
     -m meta        Meta data to store with entry (serialized php data).
     Optional arguments:
     -e entry       Name of entry to work on (must include PHAR internal direc-
                    tory name if any).
     -k index       Subscription index to work on.
pack command
     Pack files into a PHAR archive.
     When using -s <stub>, then the stub file is being excluded from  the  list
     of  input  files/dirs.To  create  an  archive  that  contains  PEAR  class
     PHP_Archive then point -p argument to PHP/Archive.php.
     Required arguments:
     -f file        Specifies the phar file to work on.
     ...            Any number of input files and directories. If -i is in  use
                    then  ONLY  files and matching the given regular expression
                    are being packed. If -x is given then files  matching  that
                    regular expression are NOT being packed.
     Optional arguments:
     -a alias       Provide an alias name for the phar file.
     -b bang        Hash-bang  line to start the archive (e.g. #!/usr/bin/php).
                    The hash mark itself '#!' and the newline character are op-
                    tional.
     -c algo        Compression algorithm (see COMPRESSION )
     -h hash        Selects the hash algorithm (see HASH )
     -i regex       Specifies a regular expression for input files.
     -l level       Number of preceding subdirectories to strip from  file  en-
                    tries
     -p loader      Location   of   PHP_Archive  class  file  (pear  list-files
                    PHP_Archive).You can use '0' or '1' to locate it  automati-
                    cally  using the mentioned pear command. When using '0' the
                    command does not error out when the class  file  cannot  be
                    located. This switch also adds some code around the stub so
                    that  class  PHP_Archive  gets registered as phar:// stream
                    wrapper if necessary. And finally this switch will add  the
                    file phar.inc from this package and load it to ensure class
                    Phar is present.
     -s stub        Select the stub file.
     -x regex       Regular expression for input files to exclude.
     -y key         Private key for OpenSSL signing.
sign command
     Set signature hash algorithm.
     Required arguments:
     -f file        Specifies the phar file to work on.
     -h hash        Selects the hash algorithm (see HASH )
     Optional arguments:
     -y key         Private key for OpenSSL signing.
stub-get command
     Get  the  stub of a PHAR file. If no output file is specified as stub then
     stdout is being used.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -s stub        Select the stub file.
stub-set command
     Set the stub of a PHAR file. If no input file is specified  as  stub  then
     stdin is being used.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -b bang        Hash-bang  line to start the archive (e.g. #!/usr/bin/php).
                    The hash mark itself '#!' and the newline character are op-
                    tional.
     -p loader      Location  of  PHP_Archive  class  file   (pear   list-files
                    PHP_Archive).You  can use '0' or '1' to locate it automati-
                    cally using the mentioned pear command. When using '0'  the
                    command  does  not  error out when the class file cannot be
                    located. This switch also adds some code around the stub so
                    that class PHP_Archive gets registered  as  phar://  stream
                    wrapper  if necessary. And finally this switch will add the
                    file phar.inc from this package and load it to ensure class
                    Phar is present.
     -s stub        Select the stub file.
tree command
     Get a directory tree for a PHAR archive.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -i regex       Specifies a regular expression for input files.
     -x regex       Regular expression for input files to exclude.
version command
     Get information about the PHAR environment and the tool version.
COMPRESSION
     Algorithms:
     0              No compression
     none           No compression
     auto           Automatically select compression algorithm
     gz             GZip compression
     gzip           GZip compression
     bz2            BZip2 compression
     bzip2          BZip2 compression
HASH
     Algorithms:
     md5            MD5
     sha1           SHA1
     sha256         SHA256
     sha512         SHA512
     openssl        OpenSSL using SHA-1
     openssl_sha256
                    OpenSSL using SHA-256
     openssl_sha512
                    OpenSSL using SHA-512
SEE ALSO
     For a more or less complete description of PHAR look here:
     https://www.php.net/phar
BUGS
     You can view the list of known bugs or report any new bug you found at:
     https://github.com/php/php-src/issues
AUTHORS
     The PHP Group: Thies C. Arntzen, Stig Bakken, Andi  Gutmans,  Rasmus  Ler-
     dorf,  Sam  Ruby,  Sascha  Schumann,  Zeev  Suraski,  Jim Winstead, Andrei
     Zmievski.
     Work for the PHP archive was done by Gregory Beaver, Marcus Boerger.
     A List of active developers can be found here:
     https://www.php.net/credits.php
     And last but not least PHP was developed with the help of a huge amount of
     contributors all around the world.
VERSION INFORMATION
```

### `man（示例）`

官方给出的调用示例：`man phar.phar.default`

```text
root@kali:~# man phar.phar.default
PHAR(1)                          User Commands                          PHAR(1)
NAME
     phar, phar.phar - PHAR (PHP archive) command line tool
SYNOPSIS
     phar <command> [options] ...
DESCRIPTION
     The  PHAR file format provides a way to put entire PHP applications into a
     single file called a "phar" (PHP Archive) for easy  distribution  and  in-
     stallation.
     With the phar command you can create, update or extract PHP archives.
     Commands:  add  compress  delete extract help help-list info list meta-del
     meta-get meta-set pack sign stub-get stub-set tree version
add command
     Add entries to a PHAR package.
     Required arguments:
     -f file        Specifies the phar file to work on.
     ...            Any number of input files and directories. If -i is in  use
                    then  ONLY  files and matching the given regular expression
                    are being packed. If -x is given then files  matching  that
                    regular expression are NOT being packed.
     Optional arguments:
     -a alias       Provide an alias name for the phar file.
     -c algo        Compression algorithm (see COMPRESSION )
     -i regex       Specifies a regular expression for input files.
     -l level       Number  of  preceding subdirectories to strip from file en-
                    tries
     -x regex       Regular expression for input files to exclude.
compress command
     Compress or uncompress all files or a selected entry.
     Required arguments:
     -c algo        Compression algorithm (see COMPRESSION )
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -e entry       Name of entry to work on (must include PHAR internal direc-
                    tory name if any).
delete command
     Delete entry from a PHAR archive
     Required arguments:
     -e entry       Name of entry to work on (must include PHAR internal direc-
                    tory name if any).
     -f file        Specifies the phar file to work on.
extract command
     Extract a PHAR package to a directory.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -i regex       Specifies a regular expression for input files.
     -x regex       Regular expression for input files to exclude.
     ...            Directory to extract to (defaults to '.').
help command
     This help or help for a selected command.
     Optional arguments:
     ...            Optional command to retrieve help for.
help-list command
     Lists available commands.
info command
     Get information about a PHAR package.
     By using -k it is possible to return a single value.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -k index       Subscription index to work on.
list command
     List contents of a PHAR archive.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -i regex       Specifies a regular expression for input files.
     -x regex       Regular expression for input files to exclude.
meta-del command
     Delete meta information of a PHAR entry or a PHAR package.
     If -k is given then the metadata is expected to be an array and the  given
     index is being deleted.
     If something was deleted the return value is 0 otherwise it is 1.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -e entry       Name of entry to work on (must include PHAR internal direc-
                    tory name if any).
     -k index       Subscription index to work on.
meta-get command
     Get meta information of a PHAR entry or a PHAR package in serialized from.
     If  no  output  file is specified for meta data then stdout is being used.
     You can also specify a particular index using -k. In that case  the  meta-
     data  is  expected  to be an array and the value of the given index is re-
     turned using echo rather than using serialize. If that index does not  ex-
     ist or no meta data is present then the return value is 1.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -e entry       Name of entry to work on (must include PHAR internal direc-
                    tory name if any).
     -k index       Subscription index to work on.
meta-set command
     Set meta data of a PHAR entry or a PHAR package using serialized input. If
     no input file is specified for meta data then stdin is being used. You can
     also specify a particular index using -k. In that case the metadata is ex-
     pected  to  be an array and the value of the given index is being set.  If
     the metadata is not present or empty a new array will be created.  If  the
     metadata  is present and a flat value then the return value is 1. Also us-
     ing -k the input is been taken directly rather then being serialized.
     Required arguments:
     -f file        Specifies the phar file to work on.
     -m meta        Meta data to store with entry (serialized php data).
     Optional arguments:
     -e entry       Name of entry to work on (must include PHAR internal direc-
                    tory name if any).
     -k index       Subscription index to work on.
pack command
     Pack files into a PHAR archive.
     When using -s <stub>, then the stub file is being excluded from  the  list
     of  input  files/dirs.To  create  an  archive  that  contains  PEAR  class
     PHP_Archive then point -p argument to PHP/Archive.php.
     Required arguments:
     -f file        Specifies the phar file to work on.
     ...            Any number of input files and directories. If -i is in  use
                    then  ONLY  files and matching the given regular expression
                    are being packed. If -x is given then files  matching  that
                    regular expression are NOT being packed.
     Optional arguments:
     -a alias       Provide an alias name for the phar file.
     -b bang        Hash-bang  line to start the archive (e.g. #!/usr/bin/php).
                    The hash mark itself '#!' and the newline character are op-
                    tional.
     -c algo        Compression algorithm (see COMPRESSION )
     -h hash        Selects the hash algorithm (see HASH )
     -i regex       Specifies a regular expression for input files.
     -l level       Number of preceding subdirectories to strip from  file  en-
                    tries
     -p loader      Location   of   PHP_Archive  class  file  (pear  list-files
                    PHP_Archive).You can use '0' or '1' to locate it  automati-
                    cally  using the mentioned pear command. When using '0' the
                    command does not error out when the class  file  cannot  be
                    located. This switch also adds some code around the stub so
                    that  class  PHP_Archive  gets registered as phar:// stream
                    wrapper if necessary. And finally this switch will add  the
                    file phar.inc from this package and load it to ensure class
                    Phar is present.
     -s stub        Select the stub file.
     -x regex       Regular expression for input files to exclude.
     -y key         Private key for OpenSSL signing.
sign command
     Set signature hash algorithm.
     Required arguments:
     -f file        Specifies the phar file to work on.
     -h hash        Selects the hash algorithm (see HASH )
     Optional arguments:
     -y key         Private key for OpenSSL signing.
stub-get command
     Get  the  stub of a PHAR file. If no output file is specified as stub then
     stdout is being used.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -s stub        Select the stub file.
stub-set command
     Set the stub of a PHAR file. If no input file is specified  as  stub  then
     stdin is being used.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -b bang        Hash-bang  line to start the archive (e.g. #!/usr/bin/php).
                    The hash mark itself '#!' and the newline character are op-
                    tional.
     -p loader      Location  of  PHP_Archive  class  file   (pear   list-files
                    PHP_Archive).You  can use '0' or '1' to locate it automati-
                    cally using the mentioned pear command. When using '0'  the
                    command  does  not  error out when the class file cannot be
                    located. This switch also adds some code around the stub so
                    that class PHP_Archive gets registered  as  phar://  stream
                    wrapper  if necessary. And finally this switch will add the
                    file phar.inc from this package and load it to ensure class
                    Phar is present.
     -s stub        Select the stub file.
tree command
     Get a directory tree for a PHAR archive.
     Required arguments:
     -f file        Specifies the phar file to work on.
     Optional arguments:
     -i regex       Specifies a regular expression for input files.
     -x regex       Regular expression for input files to exclude.
version command
     Get information about the PHAR environment and the tool version.
COMPRESSION
     Algorithms:
     0              No compression
     none           No compression
     auto           Automatically select compression algorithm
     gz             GZip compression
     gzip           GZip compression
     bz2            BZip2 compression
     bzip2          BZip2 compression
HASH
     Algorithms:
     md5            MD5
     sha1           SHA1
     sha256         SHA256
     sha512         SHA512
     openssl        OpenSSL using SHA-1
     openssl_sha256
                    OpenSSL using SHA-256
     openssl_sha512
                    OpenSSL using SHA-512
SEE ALSO
     For a more or less complete description of PHAR look here:
     https://www.php.net/phar
BUGS
     You can view the list of known bugs or report any new bug you found at:
     https://github.com/php/php-src/issues
AUTHORS
     The PHP Group: Thies C. Arntzen, Stig Bakken, Andi  Gutmans,  Rasmus  Ler-
     dorf,  Sam  Ruby,  Sascha  Schumann,  Zeev  Suraski,  Jim Winstead, Andrei
     Zmievski.
     Work for the PHP archive was done by Gregory Beaver, Marcus Boerger.
     A List of active developers can be found here:
     https://www.php.net/credits.php
     And last but not least PHP was developed with the help of a huge amount of
     contributors all around the world.
VERSION INFORMATION
```

### `php.default`

官方给出的调用示例：`php.default -h`

```text
root@kali:~# php.default -h
Usage: php [options] [-f] <file> [--] [args...]
   php [options] -r <code> [--] [args...]
   php [options] [-B <begin_code>] -R <code> [-E <end_code>] [--] [args...]
   php [options] [-B <begin_code>] -F <file> [-E <end_code>] [--] [args...]
   php [options] -S <addr>:<port> [-t docroot] [router]
   php [options] -- [args...]
   php [options] -a
  -a               Run as interactive shell (requires readline extension)
  -c <path>|<file> Look for php.ini file in this directory
  -n               No configuration (ini) files will be used
  -d foo[=bar]     Define INI entry foo with value 'bar'
  -e               Generate extended information for debugger/profiler
  -f <file>        Parse and execute <file>.
  -h               This help
  -i               PHP information
  -l               Syntax check only (lint)
  -m               Show compiled in modules
  -r <code>        Run PHP <code> without using script tags <?..?>
  -B <begin_code>  Run PHP <begin_code> before processing input lines
  -R <code>        Run PHP <code> for every input line
  -F <file>        Parse and execute <file> for every input line
  -E <end_code>    Run PHP <end_code> after processing all input lines
  -H               Hide any passed arguments from external tools.
  -S <addr>:<port> Run with built-in web server.
  -t <docroot>     Specify document root <docroot> for built-in web server.
  -s               Output HTML syntax highlighted source.
  -v               Version number
  -w               Output source with stripped comments and whitespace.
  -z <file>        Load Zend extension <file>.
  args...          Arguments passed to script. Use -- args when first argument
                   starts with - or script is read from stdin
  --ini            Show configuration file names
  --rf <name>      Show information about function <name>.
  --rc <name>      Show information about class <name>.
  --re <name>      Show information about extension <name>.
  --rz <name>      Show information about Zend extension <name>.
  --ri <name>      Show configuration for extension <name>.
```

### `phpdismod`

官方给出的调用示例：`phpdismod -h`

```text
root@kali:~# phpdismod -h
usage: phpdismod [ -v ALL|php_version ] [ -s ALL|sapi_name ] module_name [ module_name_2 ]
```

### `phpenmod`

官方给出的调用示例：`phpenmod -h`

```text
root@kali:~# phpenmod -h
usage: phpenmod [ -v ALL|php_version ] [ -s ALL|sapi_name ] module_name [ module_name_2 ]
```

### `phpquery`

官方给出的调用示例：`phpquery -h`

```text
root@kali:~# phpquery -h
usage: phpquery [ -d ] [ -q ] -v version_name -s sapi_name [ -m module_name ] [ -M ] [ -S ] [ -V ]
```

### `php-config.default`

官方给出的调用示例：`php-config.default -h`

```text
root@kali:~# php-config.default -h
Usage: /usr/bin/php-config.default [OPTION]
Options:
  --prefix            [/usr]
  --includes          [-I/usr/include/php/20240924 -I/usr/include/php/20240924/main -I/usr/include/php/20240924/TSRM -I/usr/include/php/20240924/Zend -I/usr/include/php/20240924/ext -I/usr/include/php/20240924/ext/date/lib ]
  --ldflags           [-L/usr/lib/php/20240924 ]
  --libs              [  -lm  -lxml2 -lssl -lcrypto -lpcre2-8 -lz -lsodium -largon2 -lrt -ldl]
  --extension-dir     [/usr/lib/php/20240924]
  --include-dir       [/usr/include/php/20240924]
  --lib-dir           [${prefix}/lib/php]
  --lib-embed         []
  --man-dir           [/usr/share/man]
  --php-binary        [/usr/bin/php8.4]
  --php-sapis         [apache2handler cgi cli fpm ]
  --phpapi            [20240924]
  --ini-path          [/etc/php/8.4/cli]
  --ini-dir           [/etc/php/8.4/cli/conf.d]
  --configure-options [--includedir=/usr/include --mandir=/usr/share/man --infodir=/usr/share/info --disable-option-checking --disable-silent-rules --libdir=/usr/lib/x86_64-linux-gnu --libexecdir=/usr/lib/x86_64-linux-gnu --disable-maintainer-mode --disable-dependency-tracking --prefix=/usr --enable-cli --disable-cgi --disable-phpdbg --with-config-file-path=/etc/php/8.4/cli --with-config-file-scan-dir=/etc/php/8.4/cli/conf.d --build=x86_64-linux-gnu --host=x86_64-linux-gnu --config-cache --cache-file=/tmp/buildd/nonexistent/config.cache --libdir=${prefix}/lib/php --libexecdir=${prefix}/lib/php --datadir=${prefix}/share/php/8.4 --program-suffix=8.4 --sysconfdir=/etc --localstatedir=/var --mandir=/usr/share/man --disable-all --disable-debug --disable-rpath --disable-static --disable-dtrace --with-pic --with-layout=GNU --without-pear --enable-filter --with-openssl --with-password-argon2=/usr --with-external-pcre --enable-hash --with-mhash=/usr --with-libxml --enable-session --with-sodium --with-system-tzdata --with-zlib=/usr --with-zlib-dir=/usr --enable-pcntl --with-libedit=shared,/usr build_alias=x86_64-linux-gnu host_alias=x86_64-linux-gnu CFLAGS=-g -O2 -Werror=implicit-function-declaration -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -fcf-protection -Wall -pedantic -fsigned-char -fno-strict-aliasing -DTELEMETRY_PACKAGE=]
  --version           [8.4.24]
  --vernum            [80424]
```

### `phpize.default`

官方给出的调用示例：`phpize.default --help`

```text
root@kali:~# phpize.default --help
Usage: /usr/bin/phpize.default [--clean|--help|--version|-v]
```

### `phpdbg.default`

官方给出的调用示例：`phpdbg.default -h`

```text
root@kali:~# phpdbg.default -h
phpdbg is a lightweight, powerful and easy to use debugging platform for PHP
It supports the following commands:
Information
  list      list PHP source
  info      displays information on the debug session
  print     show opcodes
  frame     select a stack frame and print a stack frame summary
  generator show active generators or select a generator frame
  back      shows the current backtrace
  help      provide help on a topic
Starting and Stopping Execution
  exec      set execution context
  stdin     set executing script from stdin
  run       attempt execution
  step      continue execution until other line is reached
  continue  continue execution
  until     continue execution up to the given location
  next      continue execution up to the given location and halt on the first
line after it
  finish    continue up to end of the current execution frame
  leave     continue up to end of the current execution frame and halt after
the calling instruction
  break     set a breakpoint at the specified target
  watch     set a watchpoint on $variable
  clear     clear one or all breakpoints
  clean     clean the execution environment
Miscellaneous
  set       set the phpdbg configuration
  source    execute a phpdbginit script
  register  register a phpdbginit function as a command alias
  sh        shell a command
  ev        evaluate some code
  quit      exit phpdbg
Type help <command> or (help alias) to get detailed help on any of the above
commands, for example help list or h l.  Note that help will also match
---Type <return> to continue or q <return> to quit---
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install libapache2-mod-php`，再执行 `libapache2-mod-php --version` 2>/dev/null || `libapache2-mod-php -V`
- [ ] **2.** **读官方帮助** —— `libapache2-mod-php -h`，需要细节时 `man libapache2-mod-php`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: php-cgi [-q] [-h] [-s] [-v] [-i] [-f <file>]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/php-defaults/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/php-defaults/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/php-defaults/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
