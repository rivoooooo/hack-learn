# Linux 命令手册 · 总索引

本目录是 Linux 常用命令的**可查阅手册**。每个命令按统一结构编写：语法 → 高频选项 → 实战示例 → 输出解读 → 常见坑 → 相关命令。

> 标记约定：
> - `⚠️` 高风险操作（会丢数据 / 锁死系统 / 不可逆）
> - `🔐` 渗透测试与安全取证常用用法
> - `💡` 提效技巧
> - `🧪` 可在 [`../labs/README.md`](../labs/README.md) 环境中复现

> 阅读前提：先读 [`../basics/`](../basics/) 的概念文档，否则「常见坑」里的原理看不懂。

---

## 分类索引

| # | 分类 | 文件 | 命令数 | 覆盖内容 |
|---|------|------|--------|----------|
| 01 | 文件与目录 | [`01-文件与目录.md`](01-文件与目录.md) | 22 | 浏览、创建、复制、移动、链接、元数据 |
| 02 | 文本处理 | [`02-文本处理.md`](02-文本处理.md) | 30 | 查看、切割、排序、`sed`/`awk`/`grep` 三剑客 |
| 03 | 权限与用户 | [`03-权限与用户.md`](03-权限与用户.md) | 30 | `chmod`、`sudo`、用户组、ACL、文件属性 |
| 04 | 进程与作业 | [`04-进程与作业.md`](04-进程与作业.md) | 30 | 进程查看、信号、后台作业、调试 |
| 05 | 磁盘与文件系统 | [`05-磁盘与文件系统.md`](05-磁盘与文件系统.md) | 23 | 容量、挂载、分区、格式化、`dd` |
| 06 | 网络 | [`06-网络.md`](06-网络.md) | 33 | 接口、路由、DNS、传输、抓包、防火墙 |
| 07 | 系统信息与内核 | [`07-系统信息与内核.md`](07-系统信息与内核.md) | 27 | 硬件、内核模块、参数、性能计数 |
| 08 | 包管理 | [`08-包管理.md`](08-包管理.md) | 23 | Debian/RPM/Arch 三体系 + 语言级包管理器 |
| 09 | 归档与压缩 | [`09-归档与压缩.md`](09-归档与压缩.md) | 14 | `tar`、`gzip`、`xz`、`zstd`、`zip` |
| 10 | 搜索与查找 | [`10-搜索与查找.md`](10-搜索与查找.md) | 18 | `find`、`locate`、`man`、`xargs`、`fd`/`fzf` |
| 11 | 系统管理 (systemd) | [`11-系统管理-systemd.md`](11-系统管理-systemd.md) | 18 | unit、日志、定时器、开关机 |
| 12 | 安全与审计 | [`12-安全与审计.md`](12-安全与审计.md) | 28 | 校验和、GPG、auditd、SELinux/AppArmor、扫描器 |
| 13 | 开发与调试 | [`13-开发与调试.md`](13-开发与调试.md) | 20 | 编译、调试、二进制分析、git、jq |
| 14 | 容器与虚拟化 | [`14-容器与虚拟化.md`](14-容器与虚拟化.md) | 19 | Docker/K8s、namespace、虚拟机 |

**合计 335 个命令小节**（含跨分类重复出现的命令）。用 `grep -c '^### ' linux/commands/*.md` 可复核（该结果 342 包含本索引文件模板中的 7 行示例标题）。

---

## 按任务找命令（速查）

### 我想知道「这个文件是什么」

| 需求 | 命令 |
|------|------|
| 看类型 | `file` · `stat -c '%F'` |
| 看完整元数据 | `stat` |
| 看大小分布 | `du -sh *` · `ncdu` |
| 看是哪个包装的 | `dpkg -S` / `rpm -qf` / `pacman -Qo` |
| 看有无被改过 | `dpkg -V` / `rpm -V` / `pacman -Qkk` |
| 看扩展属性 | `lsattr` · `getfattr` · `getfacl` |

### 我想处理文本

| 需求 | 命令 |
|------|------|
| 按列取 | `cut -d, -f3` · `awk '{print $3}'` |
| 过滤行 | `grep` · `awk '/pat/'` |
| 替换 | `sed -i 's/a/b/g'` |
| 排序去重 | `sort -u` · `sort \| uniq -c` |
| 统计 | `wc -l` · `awk '{s+=$1} END{print s}'` |
| 合并文件 | `paste` · `join` · `comm` |
| 比较 | `diff -u` · `comm` |
| 大文件浏览 | `less +F` · `tail -f` |

### 我想找文件

| 需求 | 命令 |
|------|------|
| 按名字 | `find / -name '*.conf'` |
| 按时间 | `find . -mtime -1` · `-newermt` |
| 按大小 | `find . -size +100M` |
| 按权限 | `find . -perm -4000` 🔐 |
| 按属主 | `find . -user alice` · `-nouser` |
| 内容搜索 | `grep -r` · `rg` |
| 快速定位 | `locate` · `fd` |
| 该命令是哪来的 | `type -a` · `command -v` · `whereis` |

### 我想知道系统在干什么

| 需求 | 命令 |
|------|------|
| CPU/内存 | `top` · `htop` · `free -h` · `vmstat 1` |
| 磁盘 I/O | `iostat -xz 1` · `iotop` |
| 网络连接 | `ss -tunap` · `ss -s` |
| 端口占用 | `ss -tunlp` · `lsof -i :80` · `fuser` |
| 进程树 | `pstree -p` · `ps -ef --forest` |
| 卡在哪 | `strace -p PID` · `cat /proc/PID/wchan` |
| 日志 | `journalctl -u X -f` · `dmesg -T -w` |
| 启动慢 | `systemd-analyze blame` |

### 我想改配置

| 需求 | 命令 |
|------|------|
| 内核参数 | `sysctl -w`（持久化写 `/etc/sysctl.d/`） |
| 服务 | `systemctl edit X`（drop-in，不要直接改） |
| 环境变量 | `/etc/profile.d/*.sh` · `~/.bashrc` |
| 网络（临时） | `ip addr add` · `ip route add` |
| 网络（持久） | `nmcli` · `/etc/netplan/` · `/etc/systemd/network/` |
| 定时 | `systemd timer` · `crontab -e` |
| 挂载 | `/etc/fstab`（改完必须 `mount -a` 验证） |

### 我在做安全排查 🔐

| 需求 | 命令 |
|------|------|
| SUID 文件 | `find / -xdev -perm -4000 -type f` |
| 可写系统目录 | `find / -xdev -type d -perm -0002` |
| 异常 UID 0 | `awk -F: '$3==0' /etc/passwd` |
| 空密码账号 | `awk -F: '$2==""' /etc/shadow` |
| 监听端口 | `ss -tunlp` |
| 已建立连接 | `ss -tunap state established` |
| 无实体的进程 | `ls -l /proc/*/exe \| grep deleted` |
| 持久化位置 | `crontab -l` · `systemctl list-timers --all` · `~/.bashrc` |
| 登录记录 | `last` · `lastb` · `lastlog` · `journalctl -u sshd` |
| 命令审计 | `ausearch -m EXECVE` |
| 完整性校验 | `sha256sum` · `dpkg -V` · `aide` |
| 后门扫描 | `chkrootkit` · `rkhunter` · `lynis` |

---

## 命令文档的统一模板

````markdown
### 命令名 — 一句话作用

**常用度**：★★★★★ ｜ **所属**：分类 ｜ **POSIX/GNU 差异**：有则说明

#### 语法
```bash
命令名 [选项] 参数
```

#### 高频选项
| 选项 | 含义 | 示例 |
|------|------|------|

#### 实战示例
```bash
# 场景：xxx
$ 命令 ...
输出示意
```

#### 输出解读
（关键字段含义）

#### 常见坑
- ...

#### 相关命令
`a` · `b`
````

---

## 配套练习

| 练习 | 文件 | 题量 |
|------|------|------|
| 基础 | [`../practice/01-基础题.md`](../practice/01-基础题.md) | 30 |
| 文本处理 | [`../practice/02-文本处理题.md`](../practice/02-文本处理题.md) | 25 |
| 权限与用户 | [`../practice/03-权限与用户题.md`](../practice/03-权限与用户题.md) | 20 |
| 进程与系统 | [`../practice/04-进程与系统题.md`](../practice/04-进程与系统题.md) | 20 |
| 网络 | [`../practice/05-网络题.md`](../practice/05-网络题.md) | 20 |
| 综合场景 | [`../practice/06-综合场景题.md`](../practice/06-综合场景题.md) | 15 |
| 速查挑战 | [`../practice/07-速查挑战.md`](../practice/07-速查挑战.md) | 25 |

**合计 155 题**，全部带可直接复制执行的参考答案。

## 外部权威手册

| 资源 | 说明 |
|------|------|
| `man 7 man-pages` | man 手册的分类说明 |
| https://www.gnu.org/software/coreutils/manual/ | GNU coreutils 官方手册 |
| https://man7.org/linux/man-pages/ | Linux man 页面在线版 |
| https://explainshell.com/ | 输入命令，逐参数解释 |
| https://github.com/koalaman/shellcheck | shell 脚本静态检查 |
| https://tldr.sh/ | 命令的常用示例速查（比 man 易读） |
