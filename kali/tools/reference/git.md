# git

> Fast, scalable, distributed revision control system Git is popular version control system designed to handle very large projects with speed and efficiency; it is used for many high profile open source projects, most notably the Linux kerne…

> **功能分类**：信息搜集 ｜ **Kali 包**：`git` ｜ **官方文档**：<https://www.kali.org/tools/git/>

## 1. 安装

```bash
sudo apt update
sudo apt install git
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.53.0 |
| 架构 | any |
| 可执行命令 | `git`、`git-receive-pack`、`git-shell`、`git-upload-archive`、`git-upload-pack`、`scalar`、`git-all`、`git-cvs`、`git-cvsserver`、`git-doc`、`git-email`、`git-gui`、`git-man`、`git-svn`、`gitk`、`gitweb` |
| 依赖 | `git-man`、`libc6`、`libcurl3t64-gnutls`、`liberror-perl`、`libexpat1`、`libpcre2-8-0`、`perl`、`zlib1g` |
| 安装体积 | 49.77 MB |
| 官网 | <https://git-scm.com/> |
| 源码仓库 | <https://repo.or.cz/w/git/debian.git/> |
| 包追踪 | <https://pkg.kali.org/pkg/git> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
git -h          # 查看用法
man git         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 16 个可执行命令，下面是官方页面内嵌的帮助原文。

### `git`

官方给出的调用示例：`git -h`

```text
root@kali:~# git -h
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--no-lazy-fetch]
           [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]
           [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>]
           <command> [<args>]
These are common Git commands used in various situations:
start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one
work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   restore    Restore working tree files
   rm         Remove files from the working tree and from the index
examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   diff       Show changes between commits, commit and working tree, etc
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status
grow, mark and tweak your common history
   backfill   Download missing objects in a partial clone
   branch     List, create, or delete branches
   commit     Record changes to the repository
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   reset      Set `HEAD` or the index to a known state
   switch     Switch branches
   tag        Create, list, delete or verify tags
collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects
'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
```

### `git-receive-pack`

官方给出的调用示例：`git-receive-pack --help`

```text
root@kali:~# git-receive-pack --help
GIT-RECEIVE-PACK(1)                Git Manual               GIT-RECEIVE-PACK(1)
NAME
     git-receive-pack - Receive what is pushed into the repository
SYNOPSIS
     git receive-pack <git-dir>
DESCRIPTION
     Invoked  by  git send-pack and updates the repository with the information
     fed from the remote end.
     This command is usually not invoked directly by the end user. The  UI  for
     the  protocol  is on the git send-pack side, and the program pair is meant
     to be used to push updates to a remote repository.  For  pull  operations,
     see git-fetch-pack(1).
     The  command  allows  for  the  creation  and fast-forwarding of sha1 refs
     (heads/tags) on the remote end (strictly speaking, it  is  the  local  end
     git-receive-pack  runs,  but  to  the user who is sitting at the send-pack
     end, it is updating the remote. Confused?)
     There are other real-world examples of using update and post-update  hooks
     found in the Documentation/howto directory.
     git-receive-pack  honours  the  receive.denyNonFastForwards config option,
     which tells it if updates to a ref  should  be  denied  if  they  are  not
     fast-forwards.
     A  number of other receive.* config options are available to tweak its be-
     havior, see git-config(1).
OPTIONS
     <git-dir>
         The repository to sync into.
     --http-backend-info-refs
         Used  by  git-http-backend(1)  to  serve  up   $GIT_URL/info/refs?ser-
         vice=git-receive-pack  requests.  See --http-backend-info-refs in git-
         upload-pack(1).
     --skip-connectivity-check
         Bypasses the connectivity checks that validate the  existence  of  all
         objects in the transitive closure of reachable objects. This option is
         intended  for server operators that want to implement their own object
         connectivity validation outside of Git. This is useful in  such  cases
         where  the  server-side  knows additional information about how Git is
         being used and thus can rely on certain guarantees to more efficiently
         compute object connectivity that Git itself cannot make. Usage of this
         option without a reliable external mechanism to ensure full  reachable
         object  connectivity risks corrupting the repository and should not be
         used in the general case.
PRE-RECEIVE HOOK
     Before any ref is updated, if $GIT_DIR/hooks/pre-receive file  exists  and
     is  executable,  it  will be invoked once with no parameters. The standard
     input of the hook will be one line per ref to be updated:
         sha1-old SP sha1-new SP refname LF
     The refname value is relative to $GIT_DIR; e.g. for the master  head  this
     is  "refs/heads/master".  The  two sha1 values before each refname are the
     object names for the refname before and after the update. Refs to be  cre-
     ated will have sha1-old equal to 0{40}, while refs to be deleted will have
     sha1-new  equal  to 0{40}, otherwise sha1-old and sha1-new should be valid
     objects in the repository.
     When accepting a signed push (see git-push(1)), the signed  push  certifi-
     cate  is stored in a blob and an environment variable GIT_PUSH_CERT can be
     consulted for its object name. See the description  of  post-receive  hook
     for an example. In addition, the certificate is verified using GPG and the
     result is exported with the following environment variables:
     GIT_PUSH_CERT_SIGNER
         The  name  and  the e-mail address of the owner of the key that signed
         the push certificate.
     GIT_PUSH_CERT_KEY
         The GPG key ID of the key that signed the push certificate.
     GIT_PUSH_CERT_STATUS
         The status of GPG verification of the push certificate, using the same
         mnemonic as used in %G? format of git log family of commands (see git-
         log(1)).
     GIT_PUSH_CERT_NONCE
         The nonce string the process asked the signer to include in  the  push
         certificate.  If this does not match the value recorded on the "nonce"
         header in the push certificate, it may indicate that  the  certificate
         is  a valid one that is being replayed from a separate "git push" ses-
         sion.
     GIT_PUSH_CERT_NONCE_STATUS
         UNSOLICITED
             "git push --signed" sent a nonce when we did not ask  it  to  send
             one.
         MISSING
             "git push --signed" did not send any nonce header.
         BAD
             "git push --signed" sent a bogus nonce.
         OK
             "git push --signed" sent the nonce we asked it to send.
         SLOP
             "git  push  --signed" sent a nonce different from what we asked it
             to   send    now,    but    in    a    previous    session.    See
             GIT_PUSH_CERT_NONCE_SLOP environment variable.
     GIT_PUSH_CERT_NONCE_SLOP
         "git  push  --signed"  sent a nonce different from what we asked it to
         send now, but in a different session whose starting time is  different
         by  this  many  seconds from the current session. Only meaningful when
         GIT_PUSH_CERT_NONCE_STATUS says SLOP. Also read about receive.certNon-
         ceSlop variable in git-config(1).
     This hook is called before any refname is updated and before any fast-for-
     ward checks are performed.
     If the pre-receive hook exits with a non-zero exit status no updates  will
     be  performed, and the update, post-receive and post-update hooks will not
     be invoked either. This can be useful to quickly bail out if the update is
     not to be supported.
     See the notes on the quarantine environment below.
UPDATE HOOK
     Before each ref is updated, if $GIT_DIR/hooks/update file  exists  and  is
     executable, it is invoked once per ref, with three parameters:
         $GIT_DIR/hooks/update refname sha1-old sha1-new
     The  refname  parameter  is relative to $GIT_DIR; e.g. for the master head
     this is "refs/heads/master". The two sha1 arguments are the  object  names
     for  the refname before and after the update. Note that the hook is called
     before the refname is updated, so either sha1-old is 0{40} (meaning  there
     is no such ref yet), or it should match what is recorded in refname.
     The hook should exit with non-zero status if it wants to disallow updating
     the named ref. Otherwise it should exit with zero.
     Successful execution (a zero exit status) of this hook does not ensure the
     ref will actually be updated, it is only a prerequisite. As such it is not
     a  good  idea  to send notices (e.g. email) from this hook. Consider using
     the post-receive hook instead.
POST-RECEIVE HOOK
     After all refs were updated (or attempted to be updated), if any  ref  up-
     date was successful, and if $GIT_DIR/hooks/post-receive file exists and is
     executable, it will be invoked once with no parameters. The standard input
     of the hook will be one line for each successfully updated ref:
         sha1-old SP sha1-new SP refname LF
     The  refname  value is relative to $GIT_DIR; e.g. for the master head this
     is "refs/heads/master". The two sha1 values before each  refname  are  the
     object  names  for the refname before and after the update. Refs that were
     created will have sha1-old equal to 0{40}, while refs  that  were  deleted
     will  have sha1-new equal to 0{40}, otherwise sha1-old and sha1-new should
     be valid objects in the repository.
     The GIT_PUSH_CERT* environment variables can  be  inspected,  just  as  in
     pre-receive hook, after accepting a signed push.
     Using  this  hook,  it is easy to generate mails describing the updates to
     the repository. This example script sends one mail message per ref listing
     the commits pushed to the repository, and logs the  push  certificates  of
     signed pushes with good signatures to a logger service:
         #!/bin/sh
         # mail out commit update information.
         while read oval nval ref
         do
                 if expr "$oval" : '0*$' >/dev/null
                 then
                         echo "Created a new ref, with the following commits:"
                         git rev-list --pretty "$nval"
                 else
                         echo "New commits:"
                         git rev-list --pretty "$nval" "^$oval"
                 fi |
                 mail -s "Changes to ref $ref" commit-list@mydomain
         done
         # log signed push certificate, if any
         if test -n "${GIT_PUSH_CERT-}" && test ${GIT_PUSH_CERT_STATUS} = G
         then
                 (
                         echo expected nonce is ${GIT_PUSH_NONCE}
                         git cat-file blob ${GIT_PUSH_CERT}
                 ) | mail -s "push certificate from $GIT_PUSH_CERT_SIGNER" push-log@mydomain
         fi
         exit 0
     The  exit  code  from  this hook invocation is ignored, however a non-zero
     exit code will generate an error message.
     Note that it is possible for refname to not have sha1-new when  this  hook
     runs.  This can easily occur if another user modifies the ref after it was
     updated by git-receive-pack, but before the hook was able to evaluate  it.
     It  is  recommended  that  hooks  rely on sha1-new rather than the current
     value of refname.
POST-UPDATE HOOK
     After all other processing, if at  least  one  ref  was  updated,  and  if
     $GIT_DIR/hooks/post-update file exists and is executable, then post-update
     will  be  called with the list of refs that have been updated. This can be
     used to implement any repository wide cleanup tasks.
     The exit code from this hook invocation is ignored; the  only  thing  left
     for git-receive-pack to do at that point is to exit itself anyway.
     This  hook  can be used, for example, to run git update-server-info if the
     repository is packed and is served via a dumb transport.
         #!/bin/sh
         exec git update-server-info
QUARANTINE ENVIRONMENT
     When receive-pack takes in objects,  they  are  placed  into  a  temporary
     "quarantine"  directory within the $GIT_DIR/objects directory and migrated
     into the main object store only after the pre-receive hook has  completed.
     If  the  push  fails  before  then, the temporary directory is removed en-
     tirely.
     This has a few user-visible effects and caveats:
      1. Pushes which fail due to problems with the incoming pack, missing  ob-
         jects, or due to the pre-receive hook will not leave any on-disk data.
         This is usually helpful to prevent repeated failed pushes from filling
         up your disk, but can make debugging more challenging.
       2. Any  objects  created  by the pre-receive hook will be created in the
         quarantine directory (and migrated only if it succeeds).
      3. The pre-receive hook MUST NOT update any refs to point to  quarantined
         objects.  Other  programs accessing the repository will not be able to
         see the objects (and if the pre-receive hook fails, those  refs  would
         become corrupted). For safety, any ref updates from within pre-receive
         are automatically rejected.
SEE ALSO
     git-send-pack(1), gitnamespaces(7)
GIT
     Part of the git(1) suite
Git 2.53.0                         03/01/2026               GIT-RECEIVE-PACK(1)
```

### `git-shell`

官方给出的调用示例：`git-shell -h`

```text
root@kali:~# git-shell -h
fatal: Run with no arguments or with -c cmd
```

### `git-upload-archive`

官方给出的调用示例：`git-upload-archive --help`

```text
root@kali:~# git-upload-archive --help
GIT-UPLOAD-ARCHIVE(1)              Git Manual             GIT-UPLOAD-ARCHIVE(1)
NAME
     git-upload-archive - Send archive back to git-archive
SYNOPSIS
     git upload-archive <repository>
DESCRIPTION
     Invoked by git archive --remote and sends a generated archive to the other
     end over the Git protocol.
     This  command  is usually not invoked directly by the end user. The UI for
     the protocol is on the git archive side, and the program pair is meant  to
     be used to get an archive from a remote repository.
SECURITY
     In  order  to  protect  the privacy of objects that have been removed from
     history but may not yet have been pruned, git-upload-archive avoids  serv-
     ing archives for commits and trees that are not reachable from the reposi-
     tory's  refs. However, because calculating object reachability is computa-
     tionally expensive, git-upload-archive  implements  a  stricter  but  eas-
     ier-to-check set of rules:
       1. Clients may request a commit or tree that is pointed to directly by a
         ref. E.g., git archive --remote=origin v1.0.
      2. Clients may request a sub-tree within  a  commit  or  tree  using  the
         ref:path syntax. E.g., git archive --remote=origin v1.0:Documentation.
       3. Clients may not use other sha1 expressions, even if the end result is
         reachable. E.g., neither a relative commit like master^ nor a  literal
         sha1  like  abcd1234  is allowed, even if the result is reachable from
         the refs.
     Note that rule 3 disallows many cases that do not have any privacy  impli-
     cations.  These rules are subject to change in future versions of git, and
     the server accessed by git archive --remote may or may  not  follow  these
     exact rules.
     If  the  config option uploadArchive.allowUnreachable is true, these rules
     are ignored, and clients may use arbitrary sha1 expressions. This is  use-
     ful  if  you  do  not care about the privacy of unreachable objects, or if
     your  object  database  is  already  publicly  available  for  access  via
     non-smart-http.
OPTIONS
     <repository>
         The repository to get a tar archive from.
GIT
     Part of the git(1) suite
Git 2.53.0                         03/01/2026             GIT-UPLOAD-ARCHIVE(1)
```

### `git-upload-pack`

官方给出的调用示例：`git-upload-pack --help`

```text
root@kali:~# git-upload-pack --help
GIT-UPLOAD-PACK(1)                 Git Manual                GIT-UPLOAD-PACK(1)
NAME
     git-upload-pack - Send objects packed back to git-fetch-pack
SYNOPSIS
     git-upload-pack [--[no-]strict] [--timeout=<n>] [--stateless-rpc]
                       [--advertise-refs] <directory>
DESCRIPTION
     Invoked  by git fetch-pack, learns what objects the other side is missing,
     and sends them after packing.
     This command is usually not invoked directly by the end user. The  UI  for
     the  protocol is on the git fetch-pack side, and the program pair is meant
     to be used to pull updates from a remote repository. For push  operations,
     see git send-pack.
OPTIONS
     --strict, --no-strict
         Do not try <directory>/.git/ if <directory> is not a Git directory.
     --timeout=<n>
         Interrupt transfer after <n> seconds of inactivity.
     --stateless-rpc
         Perform  only  a  single  read-write cycle with stdin and stdout. This
         fits with the HTTP POST request processing model where a  program  may
         read the request, write a response, and must exit.
     --http-backend-info-refs
         Used   by  git-http-backend(1)  to  serve  up  $GIT_URL/info/refs?ser-
         vice=git-upload-pack requests. See  "Smart  Clients"  in  gitprotocol-
         http(5)  and  "HTTP Transport" in the gitprotocol-v2(5) documentation.
         Also understood by git-receive-pack(1).
     <directory>
         The repository to sync from.
ENVIRONMENT
     GIT_PROTOCOL
         Internal variable used for handshaking the wire protocol.  Server  ad-
         mins  may  need to configure some transports to allow this variable to
         be passed. See the discussion in git(1).
     GIT_NO_LAZY_FETCH
         When cloning or fetching from a partial repository (i.e.,  one  itself
         cloned  with  --filter), the server-side upload-pack may need to fetch
         extra objects from its upstream in order to complete the  request.  By
         default, upload-pack will refuse to perform such a lazy fetch, because
         git  fetch  may  run arbitrary commands specified in configuration and
         hooks of the source repository (and upload-pack tries to  be  safe  to
         run even in untrusted .git directories).
         This   is   implemented  by  having  upload-pack  internally  set  the
         GIT_NO_LAZY_FETCH variable to 1. If you want to override  it  (because
         you are fetching from a partial clone, and you are sure you trust it),
         you can explicitly set GIT_NO_LAZY_FETCH to 0.
SECURITY
     Most  Git  commands  should not be run in an untrusted .git directory (see
     the section SECURITY in git(1)). upload-pack tries to avoid any  dangerous
     configuration options or hooks from the repository it's serving, making it
     safe  to  clone  an  untrusted directory and run commands on the resulting
     clone.
     For an extra level of safety, you may be able to run upload-pack as an al-
     ternate user. The details will be platform dependent, but on many  systems
     you can run:
         git clone --no-local --upload-pack='sudo -u nobody git-upload-pack' ...
SEE ALSO
     gitnamespaces(7)
GIT
     Part of the git(1) suite
Git 2.53.0                         03/01/2026                GIT-UPLOAD-PACK(1)
```

### `scalar`

官方给出的调用示例：`scalar -h`

```text
root@kali:~# scalar -h
usage: scalar [-C <directory>] [-c <key>=<value>] <command> [<options>]
Commands:
	clone
	list
	register
	unregister
	run
	reconfigure
	delete
	help
	version
	diagnose
```

### `git-cvsserver`

官方给出的调用示例：`git-cvsserver --help`

```text
root@kali:~# git-cvsserver --help
Unknown option: help
usage: git cvsserver [options] [pserver|server] [<directory> ...]
    --base-path <path>  : Prepend to requested CVSROOT
                          Can be read from GIT_CVSSERVER_BASE_PATH
    --strict-paths      : Don't allow recursing into subdirectories
    --export-all        : Don't check for gitcvs.enabled in config
    --version, -V       : Print version information and exit
    -h, -H              : Print usage information and exit
<directory> ... is a list of allowed directories. If no directories
are given, all are allowed. This is an additional restriction, gitcvs
access still needs to be enabled by the gitcvs.enabled config option.
Alternately, one directory may be specified in GIT_CVSSERVER_ROOT.
```

### `man`

官方给出的调用示例：`man gitk`

```text
root@kali:~# man gitk
GITK(1)                            Git Manual                           GITK(1)
NAME
     gitk - The Git repository browser
SYNOPSIS
     gitk [<options>] [<revision-range>] [--] [<path>...]
DESCRIPTION
     Displays  changes  in  a repository or a selected set of commits. This in-
     cludes visualizing the commit graph, showing information related  to  each
     commit, and the files in the trees of each revision.
OPTIONS
     To  control which revisions to show, gitk supports most options applicable
     to the git rev-list command. It also supports a few options applicable  to
     the  git diff-* commands to control how the changes each commit introduces
     are shown. Finally, it supports some gitk-specific options.
     gitk generally only understands options with arguments in the  stuck  form
     (see gitcli(7)) due to limitations in the command-line parser.
   rev-list options and arguments
     This manual page describes only the most frequently used options. See git-
     rev-list(1) for a complete list.
     --all
         Show all refs (branches, tags, etc.).
     --branches[=<pattern>], --tags[=<pattern>], --remotes[=<pattern>]
         Pretend  as  if  all  the  branches (tags, remote branches, resp.) are
         listed on the command line as <commit>. If <pattern> is  given,  limit
         refs  to  ones matching given shell glob. If pattern lacks ?, *, or [,
         /* at the end is implied.
     --since=<date>
         Show commits more recent than a specific date.
     --until=<date>
         Show commits older than a specific date.
     --date-order
         Sort commits by date when possible.
     --merge
         After an attempt to merge stops with conflicts, show  the  commits  on
         the  history  between  two branches (i.e. the HEAD and the MERGE_HEAD)
         that modify the conflicted files and do not exist on all the heads be-
         ing merged.
     --left-right
         Mark which side of a symmetric difference a commit is reachable  from.
         Commits from the left side are prefixed with a < symbol and those from
         the right with a > symbol.
     --full-history
         When  filtering  history  with <path>..., does not prune some history.
         (See "History simplification" in git-log(1) for a more detailed expla-
         nation.)
     --simplify-merges
         Additional option to --full-history to  remove  some  needless  merges
         from  the  resulting  history,  as  there are no selected commits con-
         tributing to this merge. (See "History simplification"  in  git-log(1)
         for a more detailed explanation.)
     --ancestry-path
         When  given  a  range of commits to display (e.g.  commit1..commit2 or
         commit2 ^commit1), only display commits that exist directly on the an-
         cestry chain between the commit1 and commit2, i.e.  commits  that  are
         both  descendants  of commit1, and ancestors of commit2. (See "History
         simplification" in git-log(1) for a more detailed explanation.)
     -L<start>,<end>:<file>, -L:<funcname>:<file>
         Trace the evolution of the line range given by  <start>,<end>,  or  by
         the  function  name  regex  <funcname>, within the <file>. You may not
         give any pathspec limiters. This is currently limited to a walk start-
         ing from a single revision, i.e., you may only give zero or one  posi-
         tive  revision  arguments,  and <start> and <end> (or <funcname>) must
         exist in the starting revision. You can specify this option more  than
         once.   Implies   --patch.   Patch  output  can  be  suppressed  using
         --no-patch, but other diff formats (namely --raw, --numstat,  --short-
         stat,  --dirstat,  --summary, --name-only, --name-status, --check) are
         not currently implemented.
         <start> and <end> can take one of these forms:
         *   <number>
             If <start> or <end> is a number, it  specifies  an  absolute  line
             number (lines count from 1).
         *   /<regex>/
             This  form  will  use  the  first  line  matching  the given POSIX
             <regex>. If <start> is a regex, it will search from the end of the
             previous -L range, if any, otherwise from the start  of  file.  If
             <start>  is  ^/<regex>/, it will search from the start of file. If
             <end> is a regex, it will search starting at  the  line  given  by
             <start>.
         *   +<offset> or -<offset>
             This  is  only  valid for <end> and will specify a number of lines
             before or after the line given by <start>.
         If :<funcname> is given in place of <start> and <end>, it is a regular
         expression that denotes the range from the first  funcname  line  that
         matches  <funcname>,  up  to  the  next  funcname  line.   :<funcname>
         searches from the end of the previous -L range, if any, otherwise from
         the start of file.  ^:<funcname> searches from the start of file.  The
         function  names  are  determined in the same way as git diff works out
         patch hunk headers (see Defining a custom  hunk-header  in  gitattrib-
         utes(5)).
     <revision range>
         Limit  the  revisions  to  show.  This can be either a single revision
         meaning show from the given revision and back, or it can be a range in
         the form "<from>..<to>" to show all revisions between <from> and  back
         to  <to>. Note, more advanced revision selection can be applied. For a
         more complete list of ways to spell object names, see gitrevisions(7).
     <path>...
         Limit commits to the ones touching files in the given paths. Note,  to
         avoid  ambiguity  with  respect to revision names use "--" to separate
         the paths from any preceding options.
   gitk-specific options
     --argscmd=<command>
         Command to be run each time gitk has to determine the  revision  range
         to  show.  The  command  is expected to print on its standard output a
         list of additional revisions to be shown, one per line. Use  this  in-
         stead  of  explicitly specifying a <revision-range> if the set of com-
         mits to show may vary between refreshes.
     --select-commit=<ref>
         Select the specified commit after loading the graph. Default  behavior
         is equivalent to specifying --select-commit=HEAD.
EXAMPLES
     gitk v2.6.12.. include/scsi drivers/scsi
         Show  the  changes  since version v2.6.12 that changed any file in the
         include/scsi or drivers/scsi subdirectories
     gitk --since="2 weeks ago" -- gitk
         Show the changes during the last two weeks to the file gitk. The  "--"
         is necessary to avoid confusion with the branch named gitk
     gitk --max-count=100 --all -- Makefile
         Show  at  most  100 changes made to the file Makefile. Instead of only
         looking for changes in the current branch look in all branches.
FILES
     User configuration and preferences are stored at:
     *   $XDG_CONFIG_HOME/git/gitk if it exists, otherwise
     *   $HOME/.gitk if it exists
     If neither of the above exist then  $XDG_CONFIG_HOME/git/gitk  is  created
     and  used  by  default.  If  $XDG_CONFIG_HOME  is  not  set it defaults to
     $HOME/.config in all cases.
HISTORY
     Gitk was the first graphical repository browser, written by Paul Mackerras
     in Tcl/Tk.
     gitk is actually maintained as an independent project, but stable versions
     are distributed as part of the Git suite for the convenience of end users.
     gitk-git/ comes from Johannes Sixt's gitk project:
         https://github.com/j6t/gitk
SEE ALSO
     qgit(1)
         A repository browser written in C++ using Qt.
     tig(1)
         A minimal repository browser and Git tool output  highlighter  written
         in C using Ncurses.
GIT
     Part of the git(1) suite
Git 2.53.0                         03/01/2026                           GITK(1)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install git`，再执行 `git --version` 2>/dev/null || `git -V`
- [ ] **2.** **读官方帮助** —— `git -h`，需要细节时 `man git`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `git -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/git/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/git/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/git/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
