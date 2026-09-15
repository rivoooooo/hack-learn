# Linux 系统 · 模块总纲

本模块把 Linux 从"会用"带到"能排障、能审计、能加固"。内容分四层，**先读懂原理，再查命令，然后做题，最后在靶场里跑一遍**。

| 层 | 目录 | 作用 | 怎么用 |
|----|------|------|--------|
| 原理 | [`basics/`](basics/) | 8 篇系统概念，讲清"为什么" | 顺序读；读不懂的地方对应命令手册里"常见坑"的原因 |
| 手册 | [`commands/`](commands/README.md) | 14 类 · 335 个命令小节，可查阅 | 当字典用，不要通读；按任务在 `commands/README.md` 的速查表里找 |
| 练习 | [`practice/`](practice/README.md) | 7 个文件 · 155 题（含 15 个综合场景），全部带可直接执行的答案 | 每题先自己敲，再看答案；答案命令可复制到 `/tmp` 验证 |
| 靶场 | [`labs/`](labs/README.md) | 用 Docker / 虚拟机搭练习环境 + 排障实验清单 | 按 `labs/README.md` 起环境，把练习在真机上跑 |

> **刻意不覆盖**：Linux 内核内部实现（调度器、内存管理、驱动、安全模块源码）在 [`../kernel/`](../kernel/README.md)；Kali 工具集的完整清单在 [`../kali/`](../kali/README.md)。本模块只到"用户态 + 可观测边界"为止。

> **标记约定**（全库统一）：
> - `⚠️` 高风险：会丢数据、锁死系统、不可逆
> - `🔐` 安全相关：渗透测试 / 取证 / 加固用法
> - `💡` 提效技巧
> - `🔬` 原理剖析
> - `🧪` 可在 [`labs/`](labs/README.md) 环境中复现
> - `🔗` 延伸链接

> ⚠️ 本模块的攻击性示例（提权、抓密码、持久化排查）仅用于**授权测试、CTF、自有靶场与防御研究**。对未授权系统操作在多数司法辖区（含中国大陆）构成违法。

---

## 目录索引

### basics/ — 系统概念（8 篇）

| # | 文件 | 核心问题 |
|---|------|----------|
| 01 | [文件系统与目录结构](basics/01-文件系统与目录结构.md) | 一切皆文件；FHS 各目录放什么；inode 与硬/软链接；挂载 |
| 02 | [权限与用户体系](basics/02-权限与用户体系.md) | rwx 在文件与目录上的不同含义；SUID/SGID/Sticky；umask；sudo 与 ACL |
| 03 | [进程与信号](basics/03-进程与信号.md) | 进程状态 R/S/D/T/Z；孤儿与僵尸；常用信号；cgroup 与 OOM |
| 04 | [输入输出与管道](basics/04-输入输出与管道.md) | fd 0/1/2；重定向顺序陷阱；管道与子 shell；缓冲；退出码 |
| 05 | [环境变量与 Shell 启动过程](basics/05-环境变量与Shell启动过程.md) | login / 非 login / 非交互各读哪些配置；PATH；cron 的干净环境 |
| 06 | [包管理与软件安装](basics/06-包管理与软件安装.md) | apt/dnf/pacman 三体系；从源码装；供应链风险 |
| 07 | [系统启动与 systemd](basics/07-系统启动与systemd.md) | 固件→GRUB→内核→initramfs→target→getty；unit 与 journald |
| 08 | [网络基础](basics/08-网络基础.md) | 接口与路由；DNS 解析链；TCP 状态；防火墙分层；分层排障法 |

### commands/ — 命令手册（14 类 · 335 个命令小节）

| # | 分类 | 命令数 | 典型命令 |
|---|------|--------|----------|
| 01 | [文件与目录](commands/01-文件与目录.md) | 22 | `ls` `cp` `mv` `find` 之外的日常：`stat` `ln` `install` `shred` |
| 02 | [文本处理](commands/02-文本处理.md) | 30 | `sed` `awk` `grep` `sort` `cut` `jq`（jq 见 13 类） |
| 03 | [权限与用户](commands/03-权限与用户.md) | 30 | `chmod` `chown` `sudo` `setfacl` `chattr` `useradd` |
| 04 | [进程与作业](commands/04-进程与作业.md) | 30 | `ps` `top` `pgrep` `kill` `nohup` `lsof` `strace` |
| 05 | [磁盘与文件系统](commands/05-磁盘与文件系统.md) | 23 | `df` `du` `lsblk` `mount` `fdisk` `mkfs` `dd` |
| 06 | [网络](commands/06-网络.md) | 33 | `ip` `ss` `dig` `curl` `ssh` `rsync` `tcpdump` `nft` |
| 07 | [系统信息与内核](commands/07-系统信息与内核.md) | 27 | `uname` `lsmod` `dmesg` `sysctl` `vmstat` `iostat` `lspci` |
| 08 | [包管理](commands/08-包管理.md) | 23 | `apt` `dpkg` `dnf` `rpm` `pacman` `pip` `npm` `cargo` |
| 09 | [归档与压缩](commands/09-归档与压缩.md) | 14 | `tar` `gzip` `xz` `zstd` `zip` `cpio` `ar` |
| 10 | [搜索与查找](commands/10-搜索与查找.md) | 18 | `find` `locate` `fd` `fzf` `rg` `xargs` `man` `tldr` |
| 11 | [系统管理 (systemd)](commands/11-系统管理-systemd.md) | 18 | `systemctl` `journalctl` `systemd-analyze` `loginctl` `coredumpctl` |
| 12 | [安全与审计](commands/12-安全与审计.md) | 28 | `sha256sum` `gpg` `auditctl` `ausearch` `semanage` `nmap` `john` |
| 13 | [开发与调试](commands/13-开发与调试.md) | 20 | `gcc` `gdb` `objdump` `readelf` `perf` `valgrind` `git` `jq` |
| 14 | [容器与虚拟化](commands/14-容器与虚拟化.md) | 19 | `docker` `podman` `kubectl` `unshare` `nsenter` `qemu-img` |

### practice/ — 练习（7 个文件 · 155 题，含 15 个综合场景）

| # | 文件 | 题量 | 覆盖 |
|---|------|------|------|
| 01 | [基础题](practice/01-基础题.md) | 30 | 目录导航与路径、文件操作、通配与转义、别名与历史、手册 |
| 02 | [文本处理题](practice/02-文本处理题.md) | 25 | `grep`/`sed`/`awk`/`sort`/`uniq` 组合 |
| 03 | [权限与用户题](practice/03-权限与用户题.md) | 20 | 权限位、ACL、SUID、用户与 sudo |
| 04 | [进程与系统题](practice/04-进程与系统题.md) | 20 | 进程定位、信号、资源、日志、systemd |
| 05 | [网络题](practice/05-网络题.md) | 20 | 连接、DNS、端口、抓包、防火墙 |
| 06 | [综合场景题](practice/06-综合场景题.md) | 15 | 真实运维/排障/安全场景，含完整处置流程 |
| 07 | [速查挑战](practice/07-速查挑战.md) | 25 | 一条命令解决的问题，限时挑战 |

### labs/ — 靶场与环境

| 文件 | 内容 |
|------|------|
| [labs/README.md](labs/README.md) | Docker / 虚拟机 / Vagrant 三种练习环境搭建 + 排障实验清单 + 安全实验清单 |

---

## 三条学习路线

### 路线 A · 日常使用与运维（零基础起步）

```
basics/01 文件系统 → basics/02 权限 → commands/01 文件与目录 → commands/02 文本处理
  → practice/01 基础题（做满 30 题）
  → basics/04 输入输出与管道 → commands/10 搜索与查找 → practice/02 文本处理题
  → basics/06 包管理 → commands/08 包管理 → labs/README 起一个 Docker 环境
  → basics/07 启动与 systemd → commands/11 systemd → practice/04 进程与系统题
```

**阶段验收**：给定一台陌生机器，能在 10 分钟内说清"它跑着什么、磁盘满没满、谁在占端口"。

### 路线 B · 系统排障 / SRE 方向

```
basics/03 进程与信号 + basics/08 网络基础
  → commands/04 进程与作业（重点：lsof / strace / ps 各字段）
  → commands/05 磁盘与文件系统（重点：df 满但 du 小、inode 耗尽）
  → commands/07 系统信息与内核（重点：vmstat / iostat / mpstat 三件套）
  → commands/11 系统管理（journalctl 过滤、systemd-analyze blame）
  → commands/13 开发与调试（重点：perf / valgrind / gdb core dump）
  → practice/04 + practice/06 综合场景题
  → labs/README 的「排障实验清单」逐个做
```

**阶段验收**：能对"服务起不来 / 系统变慢 / 磁盘满 / 网络不通"四类故障给出**有依据的排查顺序**，而不是逐个试。

### 路线 C · 安全与取证方向 🔐

```
basics/02 权限与用户体系（SUID、sudoers、ACL 的滥用面）
  → commands/03 权限与用户 + commands/12 安全与审计
  → commands/12 重点：auditd 规则与溯源、SELinux/AppArmor、文件完整性基线
  → commands/04 进程与作业（🔐 可疑进程排查）
  → commands/14 容器与虚拟化（容器逃逸面、namespace）
  → practice/03 + practice/06 里带 🔐 标记的题
  → labs/README 的「安全实验清单」
  → 进入 kali/ 与 web-security/ 模块
```

**阶段验收**：给一台"疑似被入侵"的机器，能列出**先取证后清理**的顺序，并说清每条命令会不会破坏证据。

---

## 怎么用本模块

**当字典查**：直接进 [`commands/README.md`](commands/README.md)，用"按任务找命令"的速查表定位，再点进分类文件看某个命令的完整说明。

**当教程读**：按 [`basics/`](basics/) 的编号顺序读，每读完一篇就去做 `practice/` 里对应主题的题。`basics/` 每篇末尾都有自检清单。

**当实验做**：`labs/README.md` 提供 Docker 一行起环境、虚拟机拓扑、以及"故意搞坏"的排障实验。命令手册里带 `🧪` 的示例都能在这里复现。

**三条纪律**：
1. 命令**自己敲一遍**，不要只读。`man` 里的选项看一次不如手打一次。
2. 涉及 `⚠️` 的命令，先在 `/tmp` 或虚拟机里试，理解后果再用到真实路径。
3. 答案里的命令是**一种**解法，不是唯一解。若你的写法输出一致，就是对的。

---

## 环境说明

本模块的示例在以下环境验证过语法：

- Arch 系（Omarchy，kernel 7.2）：`pacman` / `systemd` / `nftables` 相关示例**本机实测**
- Debian 系（Ubuntu 22.04+）：`apt` / `dpkg` 相关示例按官方文档编写，语法与 `man` 一致
- RHEL 系（CentOS Stream 9 / Rocky）：`dnf` / `rpm` / `firewalld` 相关示例同上

> 💡 不同发行版的**选项差异**（尤其是 `ps`、`sed -i`、`tar` 的 GNU/BSD 差异）在每个命令的「常见坑」里单独标注。若报 `invalid option`，先看那一节。

## 相关模块

| 想去哪 | 入口 |
|--------|------|
| Linux 内核内部实现 | [`../kernel/README.md`](../kernel/README.md) |
| Kali 工具与靶场 | [`../kali/README.md`](../kali/README.md) |
| OWASP / WSTG / ATT&CK 等安全标准 | [`../web-security/README.md`](../web-security/README.md) |
| 官方数据同步脚本 | [`../scripts/README.md`](../scripts/README.md) |
| 回到全库首页 | [`../README.md`](../README.md) |
