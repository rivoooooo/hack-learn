# 05 · 环境变量与 Shell 启动过程

> 命令手册：[`../commands/10-搜索与查找.md`](../commands/10-搜索与查找.md)（`type`、`command`、`which`）。
> 相关：[`04-输入输出与管道.md`](04-输入输出与管道.md)。

---

## 1. 环境变量基础

变量分两种作用域：

| 类型 | 说明 | 子进程可见 |
|------|------|-----------|
| shell 变量 | 只在当前 shell 内 | ❌ |
| 环境变量 | 用 `export` 导出 | ✅ |

```bash
$ NAME="alice"            # shell 变量
$ export NAME             # 升级为环境变量
$ export NAME="alice"     # 一条搞定
$ unset NAME              # 删除

$ env                     # 打印所有环境变量
$ printenv PATH           # 打印单个
$ set                     # 打印所有变量（含 shell 变量和函数）
$ declare -p PATH         # 显示类型与值
```

### 验证作用域

```bash
$ A=1
$ export B=2
$ bash -c 'echo "A=$A B=$B"'
A= B=2                    # A 不可见，B 可见
```

### 常用内置变量

| 变量 | 含义 |
|------|------|
| `$HOME` | 家目录 |
| `$USER` / `$LOGNAME` | 用户名 |
| `$SHELL` | 登录 shell 路径 |
| `$PATH` | 命令搜索路径 |
| `$PWD` / `$OLDPWD` | 当前 / 上一个目录 |
| `$PS1` | 主提示符 |
| `$IFS` | 字段分隔符，默认空格+Tab+换行 |
| `$LANG` / `$LC_ALL` | 语言与字符集 |
| `$TZ` | 时区 |
| `$EDITOR` / `$VISUAL` | 默认编辑器，被很多工具读取 |
| `$RANDOM` | 0–32767 随机数 |
| `$$` | 当前 shell 的 PID |
| `$!` | 最近一个后台进程的 PID |
| `$?` | 上条命令退出码 |
| `$#` `$@` `$*` `$0` `$1` | 脚本参数（见第 6 节） |

```bash
$ echo $RANDOM
27481
$ echo $$; echo $PPID
```

---

## 2. PATH：命令是怎么被找到的

```bash
$ echo "$PATH" | tr ':' '\n'
/usr/local/sbin
/usr/local/bin
/usr/bin
/usr/bin/site_perl
/usr/bin/vendor_perl
/usr/bin/core_perl
```

查找规则：

1. 若输入含 `/`（如 `./script.sh`、`/bin/ls`），**直接按路径执行**，不走 PATH。
2. 否则按 PATH 中**从左到右**的顺序查第一个匹配的可执行文件。
3. 全都没有 → `bash: cmd: command not found`（退出码 127）。
4. 找到但没有执行权限 → `Permission denied`（退出码 126）。

```bash
# 看某个命令最终用的是哪个
$ type -a ls
ls is aliased to `ls --color=auto'
ls is /usr/bin/ls

$ command -v ls          # 只输出路径/别名定义，脚本友好
$ which -a python3       # 注意 which 不认识别名和函数
```

### 追加与前置

```bash
$ export PATH="$PATH:$HOME/.local/bin"       # 追加（最低优先）
$ export PATH="$HOME/.local/bin:$PATH"       # 前置（最高优先，可覆盖系统命令）
$ export PATH="${PATH%%:*}"                  # 删除第一项
```

⚠️ 前置 PATH 是**经典的提权与劫持通道**：如果 root 的 PATH 里有普通用户可写的目录，攻击者放一个同名 `ls` 即可在 root 执行它时获得 root 权限。排查用 sudo 时的环境：

```bash
$ sudo sudo -V | grep 'environment'     # 看是否启用 secure_path
$ sudo cat /etc/sudoers | grep secure_path
```

`secure_path` 会让 sudo 使用固定 PATH，是重要的加固项。

### 同名命令冲突排查

```bash
$ type -a grep           # 列出所有来源（别名、函数、内建、外部）
$ alias | grep grep
$ declare -f grep        # 是否被定义成了函数
```

优先级：**别名 → 函数 → 内建 → PATH 中的外部命令**。

```bash
$ command ls             # 跳过别名和函数，直接用外部命令
$ \ls                    # 反斜杠转义，跳过别名
$ builtin cd /tmp        # 显式调用 shell 内建
```

---

## 3. Shell 启动类型

这是理解「为什么我的环境变量在某些场景不生效」的关键。

| 类型 | 触发方式 | 判断方法 |
|------|----------|----------|
| **登录 shell** (login) | `ssh user@host`、`su -`、`login`、tty 登录 | `echo $0` 以 `-` 开头 |
| **交互式非登录** (interactive non-login) | 从图形终端开新 tab、`bash` | `echo $-` 含 `i` |
| **非交互** (non-interactive) | `bash script.sh`、`bash -c '...'`、cron | 都不含 |

```bash
# 判断当前 shell 类型
$ shopt -q login_shell && echo "login shell" || echo "non-login shell"
$ case $- in *i*) echo "interactive";; *) echo "non-interactive";; esac
```

### bash 的配置文件加载顺序

| 场景 | 加载的文件 |
|------|-----------|
| 交互式**登录** shell | `/etc/profile` → 然后按顺序取 **第一个存在**的：`~/.bash_profile`、`~/.bash_login`、`~/.profile` |
| 交互式**非登录** shell | `/etc/bash.bashrc`（部分发行版） → `~/.bashrc` |
| **非交互** shell（脚本） | **都不加载**（除非 `BASH_ENV` 指定） |
| 登录 shell 退出时 | `~/.bash_logout` |

⚠️ **「加载第一个存在的」是关键陷阱**：如果你同时有 `~/.bash_profile` 和 `~/.profile`，后者**永远不会被读**。

标准做法是让 `~/.bash_profile` 主动 source `.bashrc`：

```bash
# ~/.bash_profile
[ -f ~/.bashrc ] && . ~/.bashrc
```

`/etc/profile` 通常还会遍历 `/etc/profile.d/*.sh`，这是发行版放置系统级环境变量的地方。

### 完整加载流程（bash）

```
登录 shell:
  /etc/profile
    ├── /etc/profile.d/*.sh
    └── ...
  ~/.bash_profile   （/ ~/.bash_login / ~/.profile，取第一个存在）
    └── source ~/.bashrc
          └── /etc/bashrc 或 /etc/bash.bashrc（视发行版）

交互式非登录 shell:
  ~/.bashrc
```

### 检查到底是谁设置了某变量

```bash
$ grep -rn 'MY_VAR' /etc/profile /etc/profile.d/ ~/.bashrc ~/.bash_profile ~/.profile 2>/dev/null
$ bash -x -l -c exit 2>&1 | grep MY_VAR       # 跟踪登录时执行了什么
```

⚠️ **cron 与 systemd 服务的环境极其干净**：不加载 profile/bashrc，PATH 常只有 `/usr/bin:/bin`。脚本里用绝对路径，或显式设置 PATH。这解释了「手动跑正常，定时任务报 command not found」。

```bash
# cron 任务里的稳妥写法
$ crontab -l
PATH=/usr/local/bin:/usr/bin:/bin
30 2 * * * /usr/bin/flock -n /tmp/x.lock /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1
```

---

## 4. 持久化配置放哪

| 文件 | 作用域 | 建议放什么 |
|------|--------|-----------|
| `/etc/environment` | 所有用户（PAM 读取，**非 shell 脚本**） | 简单的 `KEY=value`，不能写 `export`、不能用 `$VAR` 引用 |
| `/etc/profile` | 所有用户登录 shell | 系统级 PATH |
| `/etc/profile.d/*.sh` | 所有用户登录 shell | ⭐ 推荐的系统级扩展位置 |
| `/etc/bash.bashrc` | Debian/Ubuntu 交互式 | 系统级 alias |
| `~/.profile` | 当前用户登录 | 用户级环境变量 |
| `~/.bashrc` | 当前用户交互式 | ⭐ alias、函数、PS1 |
| `~/.bash_profile` | 当前用户登录 | 只 source `.bashrc` |
| `~/.bash_logout` | 退出登录 | 清理 |

```bash
# 加一个系统级环境变量（推荐方式）
$ echo 'export EDITOR=nvim' | sudo tee /etc/profile.d/editor.sh
$ sudo chmod 644 /etc/profile.d/editor.sh
```

⚠️ `/etc/environment` 里写 `export FOO=bar` **不生效**，它由 PAM 的 `pam_env` 解析，只认 `KEY=value` 且不支持 shell 语法。

---

## 5. alias 与函数

### alias

```bash
$ alias ll='ls -alF --color=auto'
$ alias gs='git status -sb'
$ alias ..='cd ..'
$ alias grep='grep --color=auto'
$ unalias ll
$ alias                  # 列出所有别名
```

⚠️ **alias 只在交互式 shell 生效**（`~/.bashrc`），且**不继承给子进程**。脚本里用 alias 必须在 `non-interactive` 场景显式 `shopt -s expand_aliases`，且别名要求命令在定义之后解析。**脚本里请用函数。**

⚠️ alias 无法处理需要参数的逻辑（`alias ll='ls -l $1'` 是错的），需要用函数。

### 函数

```bash
# 定义
mkcd() { mkdir -p "$1" && cd "$1"; }

# 带多行
port() {
  ss -tunlp 2>/dev/null | awk -v p=":$1" '$5 ~ p {print $NF}'
}

# 查看
$ declare -f mkcd
$ type mkcd
```

💡 实用函数（放进 `~/.bashrc`）：

```bash
# 提取各种压缩包
extract() {
  case "$1" in
    *.tar.bz2) tar xjf "$1" ;;
    *.tar.gz)  tar xzf "$1" ;;
    *.tar.xz)  tar xJf "$1" ;;
    *.tar.zst) tar --zstd -xf "$1" ;;
    *.zip)     unzip "$1" ;;
    *.7z)      7z x "$1" ;;
    *)         echo "unknown: $1" >&2 && return 1 ;;
  esac
}

# 显示 PATH 每项是否有该命令
whichall() { for d in ${PATH//:/ }; do [ -x "$d/$1" ] && echo "$d/$1"; done; }
```

### 什么时候必须用函数而不是 alias

| 需求 | alias | 函数 |
|------|-------|------|
| 固定替换前缀 | ✅ | ✅ |
| 需要参数 | ❌ | ✅ |
| 需要条件/循环 | ❌ | ✅ |
| 在脚本中使用 | ❌ | ✅ |

---

## 6. 脚本参数与环境传递

```bash
#!/usr/bin/env bash
echo "脚本名: $0"
echo "参数个数: $#"
echo "全部参数: $@"
echo "第一个: ${1:-默认值}"
```

| 写法 | 含义 |
|------|------|
| `$0` | 脚本名 |
| `$1`..`$9`, `${10}` | 位置参数（≥10 必须加花括号） |
| `$#` | 参数个数 |
| `$@` | 全部参数，**每个是独立词**（`"$@"` 保留引号语义，最常用） |
| `$*` | 全部参数，合并成一个词（按 IFS 连接） |
| `$?` | 上条命令退出码 |
| `$$` | 当前 shell PID |
| `$!` | 最近后台进程 PID |
| `${VAR:-default}` | 未设置或为空时用默认值 |
| `${VAR:=default}` | 未设置则赋值 |
| `${VAR:?msg}` | 未设置则报错退出 |
| `${VAR:offset:length}` | 子串 |
| `${VAR#prefix}` / `${VAR##prefix}` | 从头部删最短 / 最长匹配 |
| `${VAR%suffix}` / `${VAR%%suffix}` | 从尾部删最短 / 最长匹配 |
| `${VAR/old/new}` | 替换第一处 |
| `${VAR//old/new}` | 替换全部 |
| `${VAR^^}` / `${VAR,,}` | 全大写 / 全小写（bash 4+） |

```bash
$ f=/a/b/c.tar.gz
$ echo "${f##*/}"      # c.tar.gz     （文件名）
$ echo "${f%/*}"       # /a/b         （目录）
$ echo "${f%.tar.gz}"  # /a/b/c
$ echo "${f##*.}"      # gz           （扩展名）
```

### 向子进程传环境

```bash
$ FOO=bar command              # 只对该命令生效
$ env -u PATH command          # 删除某变量后执行
$ env -i /bin/bash             # 完全干净的环境
$ sudo -E command              # 保留当前环境（默认 sudo 会重置）
$ sudo FOO=bar command         # sudo 下设置变量（推荐）
```

⚠️ `sudo FOO=bar cmd` 依赖 `env_reset`/`env_keep` 配置；并非所有变量都能通过。稳妥写法：`sudo env FOO=bar cmd`。

### bash 与 POSIX sh 的差异

| 特性 | bash | POSIX sh |
|------|------|----------|
| `[[ ]]` | ✅ | ❌（只有 `[ ]`） |
| 数组 | ✅ | ❌ |
| `<<<` here-string | ✅ | ❌ |
| 进程替换 `<()` | ✅ | ❌ |
| `local` | ✅ | ❌ |
| `$RANDOM` | ✅ | ❌ |
| 字符串 `^^`/`,,` | ✅ | ❌ |

shebang 写 `#!/bin/sh` 的脚本在很多系统上实际跑的是 dash（Debian）或 bash（RHEL）。要可移植就用 `[ ]` 和 POSIX 语法；要功能就用 `#!/usr/bin/env bash`。

---

## 7. 常见「环境不生效」排查流程

```
1. 变量存在吗？
   echo "$VAR"；env | grep VAR

2. 在哪个 shell 里缺失？
   shopt -q login_shell && echo login || echo nonlogin
   echo $-        # 有 i 吗

3. 该 shell 类型加载了哪些文件？
   ls -la ~/.bash_profile ~/.bash_login ~/.profile ~/.bashrc

4. 是不是被覆盖了？
   grep -rn 'PATH' /etc/profile.d/ ~/.bashrc ~/.bash_profile

5. 子进程为什么看不到？
   是否 export？

6. 是 sudo / cron / systemd 场景吗？
   它们的默认环境是干净的，必须显式设置。
```

---

## 8. 自查清单

- [ ] 能说出 bash 登录 shell 与交互式非登录 shell 各自加载哪些文件
- [ ] 知道 `~/.bash_profile` 会屏蔽 `~/.profile`
- [ ] 知道脚本（非交互）不加载任何 rc 文件
- [ ] 知道 cron 与 systemd 服务的环境非常干净
- [ ] 会用 `type -a` 排查命令被别名/函数覆盖
- [ ] 知道 alias 只在交互式 shell 生效，脚本里要用函数
- [ ] 会写 `${f##*/}`、`${f%.*}` 这类参数展开
- [ ] 知道 `/etc/environment` 不支持 shell 语法

## 相关文档

- [`06-包管理与软件安装.md`](06-包管理与软件安装.md) — PATH 与安装位置的关系
- [`../commands/10-搜索与查找.md`](../commands/10-搜索与查找.md) — `type` / `which` / `whereis`
