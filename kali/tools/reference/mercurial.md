# mercurial

> Easy-to-use, scalable distributed version control system Mercurial is a fast, lightweight Source Control Management system designed for efficient handling of very large distributed projects. Its features include: O(1) delta-compressed file…

> **功能分类**：通用工具 ｜ **Kali 包**：`mercurial` ｜ **官方文档**：<https://www.kali.org/tools/mercurial/>

## 1. 安装

```bash
sudo apt update
sudo apt install mercurial
```

| 项目 | 内容 |
|------|------|
| 版本 | 7.2.3 |
| 架构 | any |
| 可执行命令 | `mercurial`、`chg`、`hg`、`mercurial-common`、`hg-ssh` |
| 依赖 | `libc6`、`mercurial-common`、`python3`、`python3`、`ucf`、`chg` |
| 安装体积 | 2.51 MB |
| 官网 | <https://www.mercurial-scm.org/> |
| 源码仓库 | <https://salsa.debian.org/python-team/packages/mercurial> |
| 包追踪 | <https://pkg.kali.org/pkg/mercurial> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
mercurial -h          # 查看用法
man mercurial         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 5 个可执行命令，下面是官方页面内嵌的帮助原文。

### `chg`

官方给出的调用示例：`chg -h`

```text
root@kali:~# chg -h
Mercurial Distributed SCM
list of commands:
Repository creation:
 clone         make a copy of an existing repository
 init          create a new repository in the given directory
Remote repository management:
 incoming      show new changesets found in source
 outgoing      show changesets not found in the destination
 paths         show aliases for remote repositories
 pull          pull changes from the specified source
 push          push changes to the specified destination
 serve         start stand-alone webserver
Change creation:
 commit        commit the specified files or all outstanding changes
Change manipulation:
 backout       reverse effect of earlier changeset
 graft         copy changes from other branches onto the current branch
 merge         merge another revision into working directory
Change organization:
 bookmarks     create a new bookmark or list existing bookmarks
 branch        set or show the current branch name
 branches      list repository named branches
 phase         set or show the current phase name
 tag           add one or more tags for the current or given revision
 tags          list repository tags
File content management:
 annotate      show changeset information by line for each file
 cat           output the current or given revision of files
 copy          mark files as copied for the next commit
 diff          diff repository (or selected files)
 grep          search for a pattern in specified files
Change navigation:
 bisect        subdivision search of changesets
 heads         show branch heads
 identify      identify the working directory or specified revision
 log           show revision history of entire repository or files
Working directory management:
 add           add the specified files on the next commit
 addremove     add all new files, delete all missing files
 files         list tracked files
 forget        forget the specified files on the next commit
 purge         removes files not tracked by Mercurial
 remove        remove the specified files on the next commit
 rename        rename files; equivalent of copy + remove
 resolve       redo merges or set/view the merge status of files
 revert        restore files to their checkout state
 root          print the root (top) of the current working directory
 shelve        save and set aside changes from the working directory
 status        show changed files in the working directory
 summary       summarize working directory state
 unshelve      restore a shelved change to the working directory
 update        update working directory (or switch revisions)
Change import/export:
 archive       create an unversioned archive of a repository revision
 bundle        create a bundle file
 export        dump the header and diffs for one or more changesets
 import        import an ordered set of patches
 unbundle      apply one or more bundle files
Repository maintenance:
 admin::verify
               verify the integrity of the repository
 manifest      output the current or given revision of the project manifest
 recover       roll back an interrupted transaction
 verify        verify the integrity of the repository
Help:
 config        show combined config settings from all hgrc files
 help          show help for a given topic or a help overview
 version       output version and copyright information
additional help topics:
Mercurial identifiers:
 filesets      Specifying File Sets
 hgignore      Syntax for Mercurial Ignore Files
 patterns      File Name Patterns
 revisions     Specifying Revisions
 urls          URL Paths
Mercurial output:
 color         Colorizing Outputs
 dates         Date Formats
 diffs         Diff Formats
 templating    Template Usage
Mercurial configuration:
 config        Configuration Files
 environment   Environment Variables
 extensions    Using Additional Features
 flags         Command-line flags
 hgweb         Configuring hgweb
 merge-tools   Merge Tools
 pager         Pager Support
 rust          Rust in Mercurial
Concepts:
 bundlespec    Bundle File Formats
 evolution     Safely rewriting history (EXPERIMENTAL)
 glossary      Glossary
 phases        Working with Phases
 subrepos      Subrepositories
Miscellaneous:
 deprecated    Deprecated Features
 internals     Technical implementation topics
 scripting     Using Mercurial from scripts and automation
(use 'hg help -v' to show built-in aliases and global options)
```

### `hg`

官方给出的调用示例：`hg -h`

```text
root@kali:~# hg -h
Mercurial Distributed SCM
list of commands:
Repository creation:
 clone         make a copy of an existing repository
 init          create a new repository in the given directory
Remote repository management:
 incoming      show new changesets found in source
 outgoing      show changesets not found in the destination
 paths         show aliases for remote repositories
 pull          pull changes from the specified source
 push          push changes to the specified destination
 serve         start stand-alone webserver
Change creation:
 commit        commit the specified files or all outstanding changes
Change manipulation:
 backout       reverse effect of earlier changeset
 graft         copy changes from other branches onto the current branch
 merge         merge another revision into working directory
Change organization:
 bookmarks     create a new bookmark or list existing bookmarks
 branch        set or show the current branch name
 branches      list repository named branches
 phase         set or show the current phase name
 tag           add one or more tags for the current or given revision
 tags          list repository tags
File content management:
 annotate      show changeset information by line for each file
 cat           output the current or given revision of files
 copy          mark files as copied for the next commit
 diff          diff repository (or selected files)
 grep          search for a pattern in specified files
Change navigation:
 bisect        subdivision search of changesets
 heads         show branch heads
 identify      identify the working directory or specified revision
 log           show revision history of entire repository or files
Working directory management:
 add           add the specified files on the next commit
 addremove     add all new files, delete all missing files
 files         list tracked files
 forget        forget the specified files on the next commit
 purge         removes files not tracked by Mercurial
 remove        remove the specified files on the next commit
 rename        rename files; equivalent of copy + remove
 resolve       redo merges or set/view the merge status of files
 revert        restore files to their checkout state
 root          print the root (top) of the current working directory
 shelve        save and set aside changes from the working directory
 status        show changed files in the working directory
 summary       summarize working directory state
 unshelve      restore a shelved change to the working directory
 update        update working directory (or switch revisions)
Change import/export:
 archive       create an unversioned archive of a repository revision
 bundle        create a bundle file
 export        dump the header and diffs for one or more changesets
 import        import an ordered set of patches
 unbundle      apply one or more bundle files
Repository maintenance:
 admin::verify
               verify the integrity of the repository
 manifest      output the current or given revision of the project manifest
 recover       roll back an interrupted transaction
 verify        verify the integrity of the repository
Help:
 config        show combined config settings from all hgrc files
 help          show help for a given topic or a help overview
 version       output version and copyright information
additional help topics:
Mercurial identifiers:
 filesets      Specifying File Sets
 hgignore      Syntax for Mercurial Ignore Files
 patterns      File Name Patterns
 revisions     Specifying Revisions
 urls          URL Paths
Mercurial output:
 color         Colorizing Outputs
 dates         Date Formats
 diffs         Diff Formats
 templating    Template Usage
Mercurial configuration:
 config        Configuration Files
 environment   Environment Variables
 extensions    Using Additional Features
 flags         Command-line flags
 hgweb         Configuring hgweb
 merge-tools   Merge Tools
 pager         Pager Support
 rust          Rust in Mercurial
Concepts:
 bundlespec    Bundle File Formats
 evolution     Safely rewriting history (EXPERIMENTAL)
 glossary      Glossary
 phases        Working with Phases
 subrepos      Subrepositories
Miscellaneous:
 deprecated    Deprecated Features
 internals     Technical implementation topics
 scripting     Using Mercurial from scripts and automation
(use 'hg help -v' to show built-in aliases and global options)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install mercurial`，再执行 `mercurial --version` 2>/dev/null || `mercurial -V`
- [ ] **2.** **读官方帮助** —— `mercurial -h`，需要细节时 `man mercurial`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `mercurial -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/mercurial/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/mercurial/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/mercurial/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
