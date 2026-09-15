# swaks

> SMTP command-line test tool swaks (Swiss Army Knife SMTP) is a command-line tool written in Perl for testing SMTP setups; it supports STARTTLS and SMTP AUTH (PLAIN, LOGIN, CRAM-MD5, SPA, and DIGEST-MD5). swaks allows one to stop the SMTP d…

> **功能分类**：信息搜集 ｜ **Kali 包**：`swaks` ｜ **官方文档**：<https://www.kali.org/tools/swaks/>

## 1. 安装

```bash
sudo apt update
sudo apt install swaks
```

| 项目 | 内容 |
|------|------|
| 版本 | 20240103.0 |
| 架构 | all |
| 可执行命令 | `swaks` |
| 依赖 | `perl` |
| 安装体积 | 312 KB |
| 官网 | <https://www.jetmore.org/john/code/swaks/> |
| 源码仓库 | <https://salsa.debian.org/debian/swaks> |
| 包追踪 | <https://pkg.kali.org/pkg/swaks> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
swaks -h          # 查看用法
man swaks         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `swaks`

官方给出的调用示例：`swaks --help`

```text
root@kali:~# swaks --help
SWAKS(1)                             SWAKS                             SWAKS(1)
NAME
     Swaks - Swiss Army Knife SMTP, the all-purpose SMTP transaction tester
DESCRIPTION
     Swaks'  primary  design goal is to be a flexible, scriptable, transaction-
     oriented SMTP test tool.  It handles SMTP features and extensions such  as
     TLS, authentication, and pipelining; multiple version of the SMTP protocol
     including  SMTP, ESMTP, and LMTP; and multiple transport methods including
     UNIX-domain  sockets,  internet-domain  sockets,  and  pipes  to   spawned
     processes.   Options can be specified in environment variables, configura-
     tion files, and the command line allowing maximum configurability and ease
     of use for operators and scripters.
QUICK START
     Deliver  a  standard  test  email  to
[email protected]
  on  port  25   of
     test-server.example.net:
      swaks --to
[email protected]
 --server test-server.example.net
     Deliver  a  standard test email, requiring CRAM-MD5 authentication as user
[email protected]
.  An "X-Test" header will be added to the email body.   The
     authentication password will be prompted for if it cannot be obtained from
     your .netrc file.
      swaks --to
[email protected]
 --from
[email protected]
 --auth CRAM-MD5 --auth-user
[email protected]
 --header-X-Test "test email"
     Test a virus scanner using EICAR in an attachment.  Don't show the message
     DATA part.:
      swaks -t
[email protected]
 --attach - --server test-server.example.com --suppress-data </path/to/eicar.txt
     Test a spam scanner using GTUBE in the body of an email, routed via the MX
     records for example.com:
      swaks --to
[email protected]
 --body @/path/to/gtube/file
     Deliver  a standard test email to
[email protected]
 using the LMTP protocol
     via a UNIX domain socket file
      swaks --to
[email protected]
 --socket /var/lda.sock --protocol LMTP
     Report all the recipients in a text file that are non-verifiable on a test
     server:
      for E in `cat /path/to/email/file`
      do
          swaks --to $E --server test-server.example.com --quit-after RCPT --hide-all
          [ $? -ne 0 ] && echo $E
      done
TERMS AND CONVENTIONS
     This document tries to be consistent and specific in its use of  the  fol-
     lowing terms to reduce confusion.
     Target
         The target of a transaction is the thing that Swaks connects to.  This
         generic  term  is used throughout the documentation because most other
         terms improperly imply something about the transport being used.
     Transport
         The transport is the underlying method used to connect to the target.
     Transaction
         A transaction is the opening of a connection over  a  transport  to  a
         target and using a messaging protocol to attempt to deliver a message.
     Protocol
         The  protocol is the application language used to communicate with the
         target.  This document uses SMTP to speak  generically  of  all  three
         supported  protocols  unless it states that it is speaking of the spe-
         cific 'SMTP' protocol and excluding the others.
     Message
         SMTP protocols exist to transfer  messages,  a  set  of  bytes  in  an
         agreed-upon format that has a sender and a recipient.
     Envelope
         A message's envelope contains the "true" sender and receiver of a mes-
         sage.   It  can also be referred to as its components, envelope-sender
         and envelope-recipients.  It is important to note that a messages  en-
         velope does not have to match its "To:" and "From:" headers.
     DATAThe  DATA portion of an SMTP transaction is the actual message that is
         being transported.  It consists of both the message's headers and  its
         body.  DATA and body are sometimes used synonymously, but they are al-
         ways two distinct things in this document.
     Headers
         A message's headers are defined as all the lines in the message's DATA
         section  before  the first blank line.  They contain information about
         the email that will be displayed  to  the  recipient  such  as  "To:",
         "From:",  "Subject:",  etc.   In  this document headers will always be
         written with a capitalized first letter and a trailing colon.
     BodyA message's body is the portion of  its  DATA  section  following  the
         first blank line.
     Option
         An  option  is a flag which changes Swaks' behavior.  Always called an
         option  regardless   of   how   it   is   provided.    For   instance,
         "--no-data-fixup" is an option.
     Argument
         When  an option takes addition data beside the option itself, that ad-
         ditional data is called an argument. In "--quit-after  <stop-point>'",
         "<stop-point>" is the argument to the "--quit-after" option.
     <literal-string>
         When used in the definition of an option, text that is inside of angle
         brackets  ("<>")  indicates  a  descriptive label for a value that the
         user should provide.  For instance, "--quit-after <stop-point>"  indi-
         cates  that  "<stop-point>" should be replaced with a valid stop-point
         value.
     [<optional-value>]
         When used in the definition of an option, text inside of square brack-
         ets ([]) indicates that the value is optional and can be omitted.  For
         instance, "--to [<recipient>]" indicates that the "--to" option can be
         used with or without a specified "<recipient>".
OPTION PROCESSING
     To prevent potential confusion in this document a flag to Swaks is  always
     referred to as an "option".  If the option takes additional data, that ad-
     ditional  data  is referred to as an argument to the option.  For example,
     "--from
[email protected]
" might be provided to Swaks on the command  line,
     with "--from" being the option and "
[email protected]
" being "--from"'s ar-
     gument.
     Options  and  arguments  are the only way to provide information to Swaks.
     If Swaks finds data during option processing that is neither an option nor
     an  option's  argument,  it  will  error  and  exit.   For  instance,   if
     "--no-data-fixup  1"  were found on the command line, this would result in
     an error because "--no-data-fixup" does not take an argument and therefore
     Swaks would not know what to do with 1.
     Options can be given to Swaks in three ways.  They can be specified  in  a
     configuration  file,  in  environment  variables, and on the command line.
     Depending on the specific option and whether an argument is given  to  it,
     Swaks may prompt the user for the argument.
     When  Swaks evaluates its options, it first looks for a configuration file
     (either in a default location or  specified  with  "--config").   Then  it
     evaluates  any  options  in  environment variables.  Finally, it evaluates
     command line options.  At each round of processing, any options  set  ear-
     lier  will  be  overridden.  Additionally, any option can be prefixed with
     "no-" to cause Swaks to forget that the variable had previously  been  set
     (either in an earlier round, or earlier in the same round).  This capabil-
     ity  is  necessary because many options treat defined-but-no-argument dif-
     ferently than not-defined.
     As a general rule, if the same option is given  multiple  time,  the  last
     time  it  is given is the one that will be used.  This applies to both in-
     tra-method (if  "--from
[email protected]
  --from
[email protected]
"  is
     given,  "
[email protected]
"  will  be  used)  and  inter-method  (if "from
[email protected]
" is given in  a  config  file  and  "--from  user2@exam-
     ple.com" is given on the command line, "
[email protected]
" will be used)
     Each  option  definition ends with a parenthetical synopsis of how the op-
     tion behaves.  The following codes can be used
     Arg-None, Arg-Optional, Arg-Required
         These three codes are mutually exclusive and describe whether  or  not
         the option takes an argument.  Note that this does not necessarily de-
         scribe  whether the argument is required to be specified directly, but
         rather whether an argument  is  required  eventually.   For  instance,
         "--to"  is  labeled as Arg-Required, but it is legal to specify "--to"
         on the command line without an argument.  This is  because  Swaks  can
         prompt for the required argument if it is not directly provided.
     From-Prompt
         An  option labeled with From-Prompt will prompt the user interactively
         for the argument if none is provided.
     From-File
         An option labeled with From-File will handle  arguments  as  files  in
         certain situations.
         If  the initial argument is "-", the final argument is the contents of
         "STDIN".  Multiple options can all specify "STDIN", but the same  con-
         tent will be used for each of them.
         If  the  initial  argument  is prefixed with "@", the argument will be
         treated as a path to a file.  The file will be opened and the contents
         will be used as the final argument.  If the contents of the file can't
         be read, Swaks will exit.  To specify a literal string value  starting
         with  an "@", use two "@" symbols.  The first will be stripped.  It is
         not possible to include an unqualified file which starts with  an  "@"
         sign  (like "--attach @file.txt" or "--attach @@file.txt"), but if you
         include a path to the file which splits up the  two  "@"  signs,  that
         will work (eg "--attach @./@file.txt" will include the contents of the
         file @file.txt).
     Sensitive
         If an option marked Sensitive attempts to prompt the user for an argu-
         ment  and  the "--protect-prompt" option is set, Swaks will attempt to
         mask the user input from being echoed on the terminal.  Swaks tries to
         mask the input in several ways, but if none of them work program  flow
         will continue with unmasked input.
     Deprecated
         An  option  labeled Deprecated has been officially deprecated and will
         be removed in a future release.  See  the  "DEPRECATIONS"  section  of
         this documentation for details about the deprecations.
     The  exact  mechanism and format for using each of the types is listed be-
     low.
     CONFIGURATION FILES
         A configuration file can be used to set  commonly-used  or  abnormally
         verbose   options.    By   default,   Swaks   looks   in   order   for
         $SWAKS_HOME/.swaksrc, $HOME/.swaksrc, and $LOGDIR/.swaksrc.  If one of
         those is found to exist (and "--config" has not been used)  that  file
         is used as the configuration file.
         Additionally,  a  configuration  file in a non-default location can be
         specified using "--config".  If this is set and not given an  argument
         Swaks will not use any configuration file, including any default file.
         If  "--config" points to a readable file, it is used as the configura-
         tion file, overriding any default that may exist.  If it points  to  a
         non-readable file an error will be shown and Swaks will exit.
         A  set of "portable" defaults can also be created by adding options to
         the end of the Swaks program file.  As distributed, the last  line  of
         Swaks  should  be  "__END__".  Any lines added after "__END__" will be
         treated as the contents of a configuration file.  This allows a set of
         user preferences to be automatically copied from server to server in a
         single file.
         If configuration files  have  not  been  explicitly  turned  off,  the
         "__END__"  config  is  always read.  Only one other configuration file
         will ever be used per single invocation of  Swaks,  even  if  multiple
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install swaks`，再执行 `swaks --version` 2>/dev/null || `swaks -V`
- [ ] **2.** **读官方帮助** —— `swaks -h`，需要细节时 `man swaks`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `swaks -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/swaks/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/swaks/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/swaks/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
