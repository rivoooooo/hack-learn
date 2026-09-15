# apache2

> Apache HTTP Server The Apache HTTP Server Project’s goal is to build a secure, efficient and extensible HTTP server as standards-compliant open source software. The result has long been the number one web server on the Internet. Installing…

> **功能分类**：Web 应用 ｜ **Kali 包**：`apache2` ｜ **官方文档**：<https://www.kali.org/tools/apache2/>

## 1. 安装

```bash
sudo apt update
sudo apt install apache2
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.4.68 |
| 架构 | any |
| 可执行命令 | `apache2`、`a2disconf`、`a2dismod`、`a2dissite`、`a2enconf`、`a2enmod`、`a2ensite`、`a2query`、`apache2ctl`、`apachectl`、`apache2-bin`、`apache2-data`、`apache2-dev`、`apxs`、`apxs2`、`dh_apache2`、`apache2-doc`、`apache2-ssl-dev`、`apache2-suexec-custom`、`apache2-suexec-pristine`、`apache2-utils`、`ab`、`check_forensic`、`checkgid`、`fcgistarter`、`htcacheclean`、`htdbm`、`htdigest`、`htpasswd`、`httxt2dbm`、`logresolve`、`rotatelogs`、`split-logfile` |
| 依赖 | `apache2-bin`、`apache2-data`、`apache2-utils`、`media-types`、`perl`、`procps`、`a2disconf` |
| 安装体积 | 586 KB |
| 官网 | <https://httpd.apache.org/> |
| 源码仓库 | <https://salsa.debian.org/apache-team/apache2> |
| 包追踪 | <https://pkg.kali.org/pkg/apache2> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
apache2 -h          # 查看用法
man apache2         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 33 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man a2disconf`

```text
root@kali:~# man a2disconf
A2ENCONF(8)                 System Manager's Manual                 A2ENCONF(8)
NAME
     a2enconf, a2disconf - enable or disable an apache2 configuration file
SYNOPSIS
     a2enconf [-q|--quiet] [-m|--maintmode] [ configuration ]
     a2disconf [-q|--quiet] [-m|--maintmode] [-p|--purge] [ configuration ]
DESCRIPTION
     This manual page documents briefly the a2enconf and a2disconf commands.
     a2enconf  is a script that enables the specified configuration file within
     the apache2 configuration.  It  does  this  by  creating  symlinks  within
     /etc/apache2/conf-enabled.   Likewise,  a2disconf disables a specific con-
     figuration part by removing those symlinks.  It is not an error to  enable
     a  configuration  which is already enabled, or to disable one which is al-
     ready disabled.
     Note that many configuration file may have a dependency to  specific  mod-
     ules.   Unlike  module dependencies, these are not resolved automatically.
     Configuration fragments stored in the conf-available directory are consid-
     ered non-essential or being installed and manged by  reverse  dependencies
     (e.g. web scripts).
OPTIONS
     -q, --quiet
            Don't show informative messages.
     -m, --maintmode
            Enables  the maintainer mode, that is the program invocation is ef-
            fectuated automatically by a maintainer script. This switch  should
            not be used by end users.
     -p, --purge
            When  disabling a module, purge all traces of the module in the in-
            ternal state data base.
EXIT STATUS
     a2enconf and a2disconf exit  with  status  0  if  all  configurations  are
     processed  successfully,  1  if  errors  occur, 2 if an invalid option was
     used.
EXAMPLES
            a2enconf security
            a2disconf charset
     Enables Apache security directives stored in  the  security  configuration
     files, and disables the charset configuration.
ENVIRONMENT
     The following environment variables may be specified.
     dir_suffix
            Distinguish  different  instances of apache2. Suffixes /etc/apache2
            to build a new APACHE_CONFDIR
     APACHE_CONFDIR
            Override the entire configuraation directory (/etc/apache2$dir_suf-
            fix)
     APACHE_ENVVARS
            Override the default envvars file (/etc/apache2$dir_suffix/envvars)
     APACHE_{MODS,CONF,SITES}_AVAIL
            Override the path to the directory holding the  available  snippets
            for modules, configuration and sites.
     APACHE_{MODS,CONF,SITES}_ENABLED
            Override the path to the directory holding the enabled snippets for
            modules,  configuration and sites. For example, in a multi-instance
            setup,   you   can   set   dir_suffix=-myinstance   and    override
            APACHE_MODS_AVAIL  back  to  /etc/apache2/mods-available  to have a
            single store of snippets for all instances
     APACHE_STATE_DIRECTORY
            Override the path to the state directory (/var/lib/apache2)
FILES
     /etc/apache2/conf-available
            Directory with files giving information on available  configuration
            files.
     /etc/apache2/conf-enabled
            Directory  with  links  to  the files in conf-available for enabled
            configuration files.
SEE ALSO
     apache2ctl(8), a2enmod(8), a2dismod(8), a2ensite(8), a2dissite(8).
AUTHOR
     This manual page was written by Arno Toell <
[email protected]
> for the  De-
     bian  GNU/Linux  distribution,  as it is a Debian-specific script with the
     package.
                                14 February 2012                    A2ENCONF(8)
```

### `man a2dismod`

> 官方示例调用：`man a2dismod`

```text
root@kali:~# man a2dismod
A2ENMOD(8)                  System Manager's Manual                  A2ENMOD(8)
NAME
     a2enmod, a2dismod - enable or disable an apache2 module
SYNOPSIS
     a2enmod [-q|--quiet] [-m|--maintmode] [ module ]
     a2dismod  [-q|--quiet] [-f|--force] [-m|--maintmode] [-p|--purge] [ module
     ]
DESCRIPTION
     This manual page documents briefly the a2enmod and a2dismod commands.
     a2enmod is a script that enables the specified module within  the  apache2
     configuration.     It    does    this    by   creating   symlinks   within
     /etc/apache2/mods-enabled.  Likewise, a2dismod disables a module by remov-
     ing those symlinks.  It is not an error to enable a module  which  is  al-
     ready enabled, or to disable one which is already disabled.
     Note  that  many  modules have, in addition to a .load file, an associated
     .conf file.  Enabling the module puts the configuration directives in  the
     .conf file as directives into the main server context of apache2.
OPTIONS
     -q, --quiet
            Don't show informative messages.
     -f, --force
            When disabling a module, also cascade disables all modules that de-
            pends on it.
     -m, --maintmode
            Enables  the maintainer mode, that is the program invocation is ef-
            fectuated automatically by a maintainer script. This switch  should
            not be used by end users.
     -p, --purge
            When  disabling a module, purge all traces of the module in the in-
            ternal state data base.
EXIT STATUS
     a2enmod and a2dismod exit with status 0 if all modules are processed  suc-
     cessfully, 1 if errors occur, 2 if an invalid option was used.
EXAMPLES
            a2enmod imagemap
            a2dismod mime_magic
     Enables the mod_imagemap module, and disables the mod_mime_magic module.
ENVIRONMENT
     The following environment variables may be specified.
     dir_suffix
            Distinguish  different  instances of apache2. Suffixes /etc/apache2
            to build a new APACHE_CONFDIR
     APACHE_CONFDIR
            Override the entire configuraation directory (/etc/apache2$dir_suf-
            fix)
     APACHE_ENVVARS
            Override the default envvars file (/etc/apache2$dir_suffix/envvars)
     APACHE_{MODS,CONF,SITES}_AVAIL
            Override the path to the directory holding the  available  snippets
            for modules, configuration and sites.
     APACHE_{MODS,CONF,SITES}_ENABLED
            Override the path to the directory holding the enabled snippets for
            modules,  configuration and sites. For example, in a multi-instance
            setup,   you   can   set   dir_suffix=-myinstance   and    override
            APACHE_MODS_AVAIL  back  to  /etc/apache2/mods-available  to have a
            single store of snippets for all instances
     APACHE_STATE_DIRECTORY
            Override the path to the state directory (/var/lib/apache2)
FILES
     /etc/apache2/mods-available
            Directory with files giving information on available modules.
     /etc/apache2/mods-enabled
            Directory with links to the files  in  mods-available  for  enabled
            modules.
SEE ALSO
     apache2ctl(8), a2enconf(8), a2disconf(8), a2ensite(8), a2dissite(8).
AUTHOR
     This  manual  page  was written by Daniel Stone <
[email protected]
> for the
     Debian GNU/Linux distribution, as it is a Debian-specific script with  the
     package.
                                12 October 2006                      A2ENMOD(8)
```

### `man a2dissite`

> 官方示例调用：`man a2dissite`

```text
root@kali:~# man a2dissite
A2ENSITE(8)                 System Manager's Manual                 A2ENSITE(8)
NAME
     a2ensite, a2dissite - enable or disable an apache2 site / virtual host
SYNOPSIS
     a2ensite [-q|--quiet] [-m|--maintmode] [ site ]
     a2dissite [-q|--quiet] [-m|--maintmode] [-p|--purge] [ site ]
DESCRIPTION
     This manual page documents briefly the a2ensite and a2dissite commands.
     a2ensite  is  a  script  that enables the specified site (which contains a
     <VirtualHost> block) within the apache2 configuration.  It  does  this  by
     creating  symlinks within /etc/apache2/sites-enabled.  Likewise, a2dissite
     disables a site by removing those symlinks.  It is not an error to  enable
     a  site  which is already enabled, or to disable one which is already dis-
     abled.
     Apache treats the very first virtual host enabled specially as  every  re-
     quest not matching any actual directive is being redirected there. Thus it
     should  be  called 000-default in order to sort before the remaining hosts
     to be loaded first.
OPTIONS
     -q, --quiet
            Don't show informative messages.
     -m, --maintmode
            Enables the maintainer mode, that is the program invocation is  ef-
            fectuated  automatically by a maintainer script. This switch should
            not be used by end users.
     -p, --purge
            When disabling a module, purge all traces of the module in the  in-
            ternal state data base.
EXIT STATUS
     a2ensite  and a2dissite exit with status 0 if all sites are processed suc-
     cessfully, 1 if errors occur, 2 if an invalid option was used.
EXAMPLES
            a2dissite 000-default
     Disables the default site.
ENVIRONMENT
     The following environment variables may be specified.
     dir_suffix
            Distinguish different instances of apache2.  Suffixes  /etc/apache2
            to build a new APACHE_CONFDIR
     APACHE_CONFDIR
            Override the entire configuraation directory (/etc/apache2$dir_suf-
            fix)
     APACHE_ENVVARS
            Override the default envvars file (/etc/apache2$dir_suffix/envvars)
     APACHE_{MODS,CONF,SITES}_AVAIL
            Override  the  path to the directory holding the available snippets
            for modules, configuration and sites.
     APACHE_{MODS,CONF,SITES}_ENABLED
            Override the path to the directory holding the enabled snippets for
            modules, configuration and sites. For example, in a  multi-instance
            setup,    you   can   set   dir_suffix=-myinstance   and   override
            APACHE_MODS_AVAIL back to  /etc/apache2/mods-available  to  have  a
            single store of snippets for all instances
     APACHE_STATE_DIRECTORY
            Override the path to the state directory (/var/lib/apache2)
FILES
     /etc/apache2/sites-available
            Directory with files giving information on available sites.
     /etc/apache2/sites-enabled
            Directory  with  links  to the files in sites-available for enabled
            sites.
SEE ALSO
     apache2ctl(8), a2enmod(8), a2dismod(8), a2enconf(8), a2disconf(8).
AUTHOR
     This manual page was written by Stefan Fritsch <
[email protected]
>  (based  on
     the a2enmod manual page by Daniel Stone <
[email protected]
>) for the Debian
     GNU/Linux distribution.
                                  8 June 2007                       A2ENSITE(8)
```

### `man a2enconf`

> 官方示例调用：`man a2enconf`

```text
root@kali:~# man a2enconf
A2ENCONF(8)                 System Manager's Manual                 A2ENCONF(8)
NAME
     a2enconf, a2disconf - enable or disable an apache2 configuration file
SYNOPSIS
     a2enconf [-q|--quiet] [-m|--maintmode] [ configuration ]
     a2disconf [-q|--quiet] [-m|--maintmode] [-p|--purge] [ configuration ]
DESCRIPTION
     This manual page documents briefly the a2enconf and a2disconf commands.
     a2enconf  is a script that enables the specified configuration file within
     the apache2 configuration.  It  does  this  by  creating  symlinks  within
     /etc/apache2/conf-enabled.   Likewise,  a2disconf disables a specific con-
     figuration part by removing those symlinks.  It is not an error to  enable
     a  configuration  which is already enabled, or to disable one which is al-
     ready disabled.
     Note that many configuration file may have a dependency to  specific  mod-
     ules.   Unlike  module dependencies, these are not resolved automatically.
     Configuration fragments stored in the conf-available directory are consid-
     ered non-essential or being installed and manged by  reverse  dependencies
     (e.g. web scripts).
OPTIONS
     -q, --quiet
            Don't show informative messages.
     -m, --maintmode
            Enables  the maintainer mode, that is the program invocation is ef-
            fectuated automatically by a maintainer script. This switch  should
            not be used by end users.
     -p, --purge
            When  disabling a module, purge all traces of the module in the in-
            ternal state data base.
EXIT STATUS
     a2enconf and a2disconf exit  with  status  0  if  all  configurations  are
     processed  successfully,  1  if  errors  occur, 2 if an invalid option was
     used.
EXAMPLES
            a2enconf security
            a2disconf charset
     Enables Apache security directives stored in  the  security  configuration
     files, and disables the charset configuration.
ENVIRONMENT
     The following environment variables may be specified.
     dir_suffix
            Distinguish  different  instances of apache2. Suffixes /etc/apache2
            to build a new APACHE_CONFDIR
     APACHE_CONFDIR
            Override the entire configuraation directory (/etc/apache2$dir_suf-
            fix)
     APACHE_ENVVARS
            Override the default envvars file (/etc/apache2$dir_suffix/envvars)
     APACHE_{MODS,CONF,SITES}_AVAIL
            Override the path to the directory holding the  available  snippets
            for modules, configuration and sites.
     APACHE_{MODS,CONF,SITES}_ENABLED
            Override the path to the directory holding the enabled snippets for
            modules,  configuration and sites. For example, in a multi-instance
            setup,   you   can   set   dir_suffix=-myinstance   and    override
            APACHE_MODS_AVAIL  back  to  /etc/apache2/mods-available  to have a
            single store of snippets for all instances
     APACHE_STATE_DIRECTORY
            Override the path to the state directory (/var/lib/apache2)
FILES
     /etc/apache2/conf-available
            Directory with files giving information on available  configuration
            files.
     /etc/apache2/conf-enabled
            Directory  with  links  to  the files in conf-available for enabled
            configuration files.
SEE ALSO
     apache2ctl(8), a2enmod(8), a2dismod(8), a2ensite(8), a2dissite(8).
AUTHOR
     This manual page was written by Arno Toell <
[email protected]
> for the  De-
     bian  GNU/Linux  distribution,  as it is a Debian-specific script with the
     package.
                                14 February 2012                    A2ENCONF(8)
```

### `man a2enmod`

> 官方示例调用：`man a2enmod`

```text
root@kali:~# man a2enmod
A2ENMOD(8)                  System Manager's Manual                  A2ENMOD(8)
NAME
     a2enmod, a2dismod - enable or disable an apache2 module
SYNOPSIS
     a2enmod [-q|--quiet] [-m|--maintmode] [ module ]
     a2dismod  [-q|--quiet] [-f|--force] [-m|--maintmode] [-p|--purge] [ module
     ]
DESCRIPTION
     This manual page documents briefly the a2enmod and a2dismod commands.
     a2enmod is a script that enables the specified module within  the  apache2
     configuration.     It    does    this    by   creating   symlinks   within
     /etc/apache2/mods-enabled.  Likewise, a2dismod disables a module by remov-
     ing those symlinks.  It is not an error to enable a module  which  is  al-
     ready enabled, or to disable one which is already disabled.
     Note  that  many  modules have, in addition to a .load file, an associated
     .conf file.  Enabling the module puts the configuration directives in  the
     .conf file as directives into the main server context of apache2.
OPTIONS
     -q, --quiet
            Don't show informative messages.
     -f, --force
            When disabling a module, also cascade disables all modules that de-
            pends on it.
     -m, --maintmode
            Enables  the maintainer mode, that is the program invocation is ef-
            fectuated automatically by a maintainer script. This switch  should
            not be used by end users.
     -p, --purge
            When  disabling a module, purge all traces of the module in the in-
            ternal state data base.
EXIT STATUS
     a2enmod and a2dismod exit with status 0 if all modules are processed  suc-
     cessfully, 1 if errors occur, 2 if an invalid option was used.
EXAMPLES
            a2enmod imagemap
            a2dismod mime_magic
     Enables the mod_imagemap module, and disables the mod_mime_magic module.
ENVIRONMENT
     The following environment variables may be specified.
     dir_suffix
            Distinguish  different  instances of apache2. Suffixes /etc/apache2
            to build a new APACHE_CONFDIR
     APACHE_CONFDIR
            Override the entire configuraation directory (/etc/apache2$dir_suf-
            fix)
     APACHE_ENVVARS
            Override the default envvars file (/etc/apache2$dir_suffix/envvars)
     APACHE_{MODS,CONF,SITES}_AVAIL
            Override the path to the directory holding the  available  snippets
            for modules, configuration and sites.
     APACHE_{MODS,CONF,SITES}_ENABLED
            Override the path to the directory holding the enabled snippets for
            modules,  configuration and sites. For example, in a multi-instance
            setup,   you   can   set   dir_suffix=-myinstance   and    override
            APACHE_MODS_AVAIL  back  to  /etc/apache2/mods-available  to have a
            single store of snippets for all instances
     APACHE_STATE_DIRECTORY
            Override the path to the state directory (/var/lib/apache2)
FILES
     /etc/apache2/mods-available
            Directory with files giving information on available modules.
     /etc/apache2/mods-enabled
            Directory with links to the files  in  mods-available  for  enabled
            modules.
SEE ALSO
     apache2ctl(8), a2enconf(8), a2disconf(8), a2ensite(8), a2dissite(8).
AUTHOR
     This  manual  page  was written by Daniel Stone <
[email protected]
> for the
     Debian GNU/Linux distribution, as it is a Debian-specific script with  the
     package.
                                12 October 2006                      A2ENMOD(8)
```

### `man a2ensite`

> 官方示例调用：`man a2ensite`

```text
root@kali:~# man a2ensite
A2ENSITE(8)                 System Manager's Manual                 A2ENSITE(8)
NAME
     a2ensite, a2dissite - enable or disable an apache2 site / virtual host
SYNOPSIS
     a2ensite [-q|--quiet] [-m|--maintmode] [ site ]
     a2dissite [-q|--quiet] [-m|--maintmode] [-p|--purge] [ site ]
DESCRIPTION
     This manual page documents briefly the a2ensite and a2dissite commands.
     a2ensite  is  a  script  that enables the specified site (which contains a
     <VirtualHost> block) within the apache2 configuration.  It  does  this  by
     creating  symlinks within /etc/apache2/sites-enabled.  Likewise, a2dissite
     disables a site by removing those symlinks.  It is not an error to  enable
     a  site  which is already enabled, or to disable one which is already dis-
     abled.
     Apache treats the very first virtual host enabled specially as  every  re-
     quest not matching any actual directive is being redirected there. Thus it
     should  be  called 000-default in order to sort before the remaining hosts
     to be loaded first.
OPTIONS
     -q, --quiet
            Don't show informative messages.
     -m, --maintmode
            Enables the maintainer mode, that is the program invocation is  ef-
            fectuated  automatically by a maintainer script. This switch should
            not be used by end users.
     -p, --purge
            When disabling a module, purge all traces of the module in the  in-
            ternal state data base.
EXIT STATUS
     a2ensite  and a2dissite exit with status 0 if all sites are processed suc-
     cessfully, 1 if errors occur, 2 if an invalid option was used.
EXAMPLES
            a2dissite 000-default
     Disables the default site.
ENVIRONMENT
     The following environment variables may be specified.
     dir_suffix
            Distinguish different instances of apache2.  Suffixes  /etc/apache2
            to build a new APACHE_CONFDIR
     APACHE_CONFDIR
            Override the entire configuraation directory (/etc/apache2$dir_suf-
            fix)
     APACHE_ENVVARS
            Override the default envvars file (/etc/apache2$dir_suffix/envvars)
     APACHE_{MODS,CONF,SITES}_AVAIL
            Override  the  path to the directory holding the available snippets
            for modules, configuration and sites.
     APACHE_{MODS,CONF,SITES}_ENABLED
            Override the path to the directory holding the enabled snippets for
            modules, configuration and sites. For example, in a  multi-instance
            setup,    you   can   set   dir_suffix=-myinstance   and   override
            APACHE_MODS_AVAIL back to  /etc/apache2/mods-available  to  have  a
            single store of snippets for all instances
     APACHE_STATE_DIRECTORY
            Override the path to the state directory (/var/lib/apache2)
FILES
     /etc/apache2/sites-available
            Directory with files giving information on available sites.
     /etc/apache2/sites-enabled
            Directory  with  links  to the files in sites-available for enabled
            sites.
SEE ALSO
     apache2ctl(8), a2enmod(8), a2dismod(8), a2enconf(8), a2disconf(8).
AUTHOR
     This manual page was written by Stefan Fritsch <
[email protected]
>  (based  on
     the a2enmod manual page by Daniel Stone <
[email protected]
>) for the Debian
     GNU/Linux distribution.
                                  8 June 2007                       A2ENSITE(8)
```

### `a2query`

> 官方示例调用：`a2query --help`

```text
root@kali:~# a2query --help
/usr/sbin/a2query version [unknown] calling Getopt::Std::getopts (version 1.14 [paranoid]),
running under Perl version 5.42.2.
Usage: a2query [-OPTIONS [-MORE_OPTIONS]] [--] [PROGRAM_ARG1 ...]
The following single-character options are accepted:
	With arguments: -m -s -c
	Boolean (without arguments): -h -a -v -M -d -q
Options may be merged together.  -- stops processing of options.
Space is not required between options and their arguments.
For more details run
	perldoc -F /usr/sbin/a2query
  [Now continuing due to backward compatibility and excessive paranoia.
   See 'perldoc Getopt::Std' about $Getopt::Std::STANDARD_HELP_VERSION.]
```

### `apache2ctl`

> 官方示例调用：`apache2ctl -h`

```text
root@kali:~# apache2ctl -h
Usage: /usr/sbin/apache2 [-D name] [-d directory] [-f file]
                         [-C "directive"] [-c "directive"]
                         [-k start|restart|graceful|graceful-stop|stop]
                         [-v] [-V] [-h] [-l] [-L] [-t] [-T] [-S] [-X]
Options:
  -D name            : define a name for use in <IfDefine name> directives
  -d directory       : specify an alternate initial ServerRoot
  -f file            : specify an alternate ServerConfigFile
  -C "directive"     : process directive before reading config files
  -c "directive"     : process directive after reading config files
  -e level           : show startup errors of level (see LogLevel)
  -E file            : log startup errors to file
  -v                 : show version number
  -V                 : show compile settings
  -h                 : list available command line options (this page)
  -l                 : list compiled in modules
  -L                 : list available configuration directives
  -t -D DUMP_VHOSTS  : show parsed vhost settings
  -t -D DUMP_RUN_CFG : show parsed run settings
  -S                 : a synonym for -t -D DUMP_VHOSTS -D DUMP_RUN_CFG
  -t -D DUMP_MODULES : show all loaded modules
  -M                 : a synonym for -t -D DUMP_MODULES
  -t -D DUMP_INCLUDES: show all included configuration files
  -t                 : run syntax check for config files
  -T                 : start without DocumentRoot(s) check
  -X                 : debug mode (only one worker, do not detach)
```

### `apachectl`

> 官方示例调用：`apachectl -h`

```text
root@kali:~# apachectl -h
Usage: /usr/sbin/apache2 [-D name] [-d directory] [-f file]
                         [-C "directive"] [-c "directive"]
                         [-k start|restart|graceful|graceful-stop|stop]
                         [-v] [-V] [-h] [-l] [-L] [-t] [-T] [-S] [-X]
Options:
  -D name            : define a name for use in <IfDefine name> directives
  -d directory       : specify an alternate initial ServerRoot
  -f file            : specify an alternate ServerConfigFile
  -C "directive"     : process directive before reading config files
  -c "directive"     : process directive after reading config files
  -e level           : show startup errors of level (see LogLevel)
  -E file            : log startup errors to file
  -v                 : show version number
  -V                 : show compile settings
  -h                 : list available command line options (this page)
  -l                 : list compiled in modules
  -L                 : list available configuration directives
  -t -D DUMP_VHOSTS  : show parsed vhost settings
  -t -D DUMP_RUN_CFG : show parsed run settings
  -S                 : a synonym for -t -D DUMP_VHOSTS -D DUMP_RUN_CFG
  -t -D DUMP_MODULES : show all loaded modules
  -M                 : a synonym for -t -D DUMP_MODULES
  -t -D DUMP_INCLUDES: show all included configuration files
  -t                 : run syntax check for config files
  -T                 : start without DocumentRoot(s) check
  -X                 : debug mode (only one worker, do not detach)
```

### `apache2`

> 官方示例调用：`apache2 -h`

```text
root@kali:~# apache2 -h
Usage: apache2 [-D name] [-d directory] [-f file]
               [-C "directive"] [-c "directive"]
               [-k start|restart|graceful|graceful-stop|stop]
               [-v] [-V] [-h] [-l] [-L] [-t] [-T] [-S] [-X]
Options:
  -D name            : define a name for use in <IfDefine name> directives
  -d directory       : specify an alternate initial ServerRoot
  -f file            : specify an alternate ServerConfigFile
  -C "directive"     : process directive before reading config files
  -c "directive"     : process directive after reading config files
  -e level           : show startup errors of level (see LogLevel)
  -E file            : log startup errors to file
  -v                 : show version number
  -V                 : show compile settings
  -h                 : list available command line options (this page)
  -l                 : list compiled in modules
  -L                 : list available configuration directives
  -t -D DUMP_VHOSTS  : show parsed vhost settings
  -t -D DUMP_RUN_CFG : show parsed run settings
  -S                 : a synonym for -t -D DUMP_VHOSTS -D DUMP_RUN_CFG
  -t -D DUMP_MODULES : show all loaded modules
  -M                 : a synonym for -t -D DUMP_MODULES
  -t -D DUMP_INCLUDES: show all included configuration files
  -t                 : run syntax check for config files
  -T                 : start without DocumentRoot(s) check
  -X                 : debug mode (only one worker, do not detach)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install apache2`，再执行 `apache2 --version` 2>/dev/null || `apache2 -V`
- [ ] **2.** **读官方帮助** —— `apache2 -h`，需要细节时 `man apache2`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: a2query [-OPTIONS [-MORE_OPTIONS]] [--] [PROGRAM_ARG1 ...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/apache2/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[apache2](../../tools/tutorials/12-基础设施与C2/apache2.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/apache2/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/apache2/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
