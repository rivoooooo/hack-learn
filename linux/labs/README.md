# 练习环境 · 靶场与实验

本目录说明**怎么搭一套可以随便折腾的 Linux 练习环境**，以及**有哪些实验可以做**。

> 为什么需要它：本库的练习和命令手册里有大量 `⚠️` 标记的操作（`rm -rf`、`mkfs`、`chmod -R`、`dd`、改 `fstab`…）。这些**绝不能在真机上做**。你需要一个"坏掉了就地重建"的环境。
>
> 所有攻击性实验**仅用于授权测试、CTF、自有靶场与防御研究**。对未授权系统操作在多数司法辖区（含中国大陆）构成违法。

> ⚠️ **破坏性实验的三条硬规矩**（本目录第零节和第 4、5 节都建立在这三条上）：
>
> 1. **只在虚拟机或容器里做**，不要在跑着工作/数据的主机上做。判据：如果你不敢对这台机器执行 `virsh destroy` / `docker rm -f` 后重来，那它就不是练习环境。
> 2. **以下命令会不可逆地毁掉数据，永远不要对着真实设备执行**：
>    - `dd if=... of=/dev/sdX`、`mkfs.*`、`fdisk`/`parted` 写操作 → 抹掉整块盘
>    - `iptables -F` / `nft flush ruleset` → **在远程机器上执行会立刻断掉你的 SSH**（默认策略若是 DROP 就更回不来）
>    - `chmod -R` / `chown -R` 作用于 `/`、`/etc`、`/usr` → 系统级权限事故（见第 4 节实验 5 与 [`../practice/06-综合场景题.md`](../practice/06-综合场景题.md) 场景 11）
>    - `rm -rf $VAR/`（`$VAR` 为空时变成 `rm -rf /`）
>    - `truncate` / `> file` 作用于 `/proc/<PID>/fd/N` 或正在被写的日志 → 内容永久丢失
> 3. **改远程防火墙/网络配置前先留退路**：
>    ```bash
>    # 5 分钟后自动清空规则并放开（给自己留一条命）
>    sudo sh -c 'echo "iptables -F; iptables -P INPUT ACCEPT" | at now + 5 minutes'
>    # 恢复后记得取消：atrm <job编号>
>    ```

---

## 零、一键造沙盒（开始之前先做这一步）

本目录所有实验和 [`../practice/`](../practice/README.md) 的题目都假设有一个**可反复重建**的练习数据目录。

**权威版本在 [`../practice/README.md` 的 4.1 节 `一键造沙盒`](../practice/README.md#41-一键造沙盒)** —— 那段脚本会生成 `/tmp/linux-practice`，包含：目录树、1000 行访问日志、CSV、含空格/中文/glob 字符的文件名、硬链接/软链接/断链、`4755` 与 `666`/`777` 权限异常样本、5 MiB 空洞大文件、2000 行应用日志、二进制样本、不同 mtime 的归档源。先跑它，再回来做实验。

下面是**只给本目录实验用**的补充脚本：造出排障类实验需要但练习沙盒里没有的东西（填满的分区镜像、海量小文件、可填满的日志、被删除但仍被占用的文件）。

```bash
#!/usr/bin/env bash
# /tmp/linux-lab-setup.sh —— 为本目录的排障实验准备素材
# 用法：bash /tmp/linux-lab-setup.sh
set -euo pipefail

LAB=/tmp/linux-lab
rm -rf "$LAB"
mkdir -p "$LAB"/{img,logs,inode,occupy,secret,backup}

# 1) 一块 64 MiB 的"假硬盘"（用于实验 8 分区、实验 11 制造磁盘满）
truncate -s 64M "$LAB/img/fakedisk.img"

# 2) 一个会被填满的分区镜像（挂载后 dw 会到 100%）
dd if=/dev/urandom of="$LAB/img/fill-50M.bin" bs=1M count=50 status=none

# 3) 海量小文件（用于实验 12 制造 inode 耗尽 —— 需要 root 挂载小 inode 的文件系统才够快，
#    这里先生成 5 万个用于观察 inode 增长）
mkdir -p "$LAB/inode/many"
for i in $(seq 1 500); do
  mkdir -p "$LAB/inode/many/d$i"
  for j in $(seq 1 100); do : > "$LAB/inode/many/d$i/f$j"; done
done
echo "小文件数: $(find "$LAB/inode/many" -type f | wc -l)"

# 4) 会被"疯狂写"的日志（用于实验 11 制造磁盘满 / 实验 15 观察 IO）
head -c 20M /dev/urandom | base64 > "$LAB/logs/noisy.log"

# 5) 被删除但仍被进程占用的文件（用于实验 13）
#    先只生成内容；实验 13 里用 python 打开它再 rm 掉
head -c 30M /dev/urandom | base64 > "$LAB/occupy/ghost.log"

# 6) 权限异常样本（用于实验 5 与安全实验 3 的 find -perm 审计）
: > "$LAB/secret/notes.txt";      chmod 666 "$LAB/secret/notes.txt"   # 世界可写文件
mkdir -p "$LAB/secret/open";      chmod 777 "$LAB/secret/open"        # 世界可写目录
cp /bin/true "$LAB/secret/suid";  chmod 4755 "$LAB/secret/suid"       # SUID 可执行（无实际提权能力）
: > "$LAB/secret/sgid";           chmod 2755 "$LAB/secret/sgid"       # SGID

# 7) 软/硬链接与断链（用于实验 5、10）
echo "original" > "$LAB/backup/orig.txt"
ln    "$LAB/backup/orig.txt" "$LAB/backup/hard.txt"
ln -s "$LAB/backup/orig.txt" "$LAB/backup/soft.txt"
ln -s /nonexistent/nowhere   "$LAB/backup/broken"

echo "✅ 实验素材已生成：$LAB"
find "$LAB" -maxdepth 2 -printf '%y %10s  %p\n' | sort -k3 | head -30
```

**重置（每次做完破坏性实验后跑一遍）**：

```bash
rm -rf /tmp/linux-lab && bash /tmp/linux-lab-setup.sh
```

> 💡 **要点：所有素材都放在 `/tmp` 下的一个目录里**。这样"恢复干净状态"就是一条 `rm -rf` + 重跑脚本，而不是去找哪里被改坏了。这也是虚拟机快照之外的第二种低成本回滚手段。
>
> ⚠️ **不要把素材目录设成 `/`、`/var`、`~/` 这类有真实数据的位置**。上面脚本里的 `rm -rf "$LAB"` 会在每次运行时删掉整个 `$LAB` —— 如果 `$LAB` 拼成了 `/var`，那就是灾难。脚本里已经用 `set -u` 防止变量为空，但**你自己改脚本时要保证 `$LAB` 一定被赋值**。

---

## 一、三种环境的选择

| 方案 | 启动成本 | 隔离强度 | 适合做什么 | 不适合 |
|------|----------|----------|------------|--------|
| **Docker / Podman 容器** | 秒级 | 中（共享内核） | 文件/权限/文本/进程/网络命令练习 | 内核模块、systemd、启动过程、分区 |
| **虚拟机（KVM / VirtualBox / VMware）** | 分钟级 | **高（独立内核）** | **全部**内容，含 systemd、磁盘、启动、快照回滚 | 资源占用大 |
| **Vagrant / 一键脚本** | 分钟级 | 高 | 多机拓扑（互 ping、SSH 互连、攻击/防守） | 需要装 VirtualBox/libvirt |

**推荐组合**：

- **日常刷命令** → Docker（一个 `debian:stable` 或 `rockylinux:9` 容器）
- **做「排障」类实验**（本目录第 4 节） → 虚拟机（因为要动系统级配置，且需要快照回滚）
- **做「安全」实验**（本目录第 5 节） → 虚拟机（需要 `auditd`、SELinux/AppArmor、`chattr` 等内核级能力）
- **做「多机」实验**（网络、SSH、渗透） → Vagrant 或两台虚拟机 + 内部网络
- **无论做哪一种** → 先跑第零节的「一键造沙盒」，把所有素材放在一个可 `rm -rf` 重建的目录里

---

## 二、方案 A：Docker 容器（最快上手）

### 2.1 起一个可以随便折腾的容器

```bash
# 一次性（用完即弃）
docker run --rm -it --name lab debian:12 bash

# 长期使用（带持久化目录，重启后数据还在）
mkdir -p ~/linux-lab/data
docker run -it --name linux-lab \
  --hostname lab \
  -v ~/linux-lab/data:/data \
  debian:12 bash
```

| 参数 | 作用 |
|------|------|
| `--rm` | 退出后自动删除容器（`⚠️ 数据全丢`，练习用） |
| `-it` | 交互式 + 分配 TTY（**两个都要**，否则没有提示符） |
| `--name` | 起个名字，方便 `exec` 进去 |
| `--hostname lab` | 设置主机名（`hostname`、`/etc/hostname` 才有内容可练） |
| `-v 宿主:容器` | 挂载目录（**练习数据放这里，容器删了也不丢**） |

> ⚠️ **不要用 `--rm` 之外还指望"重启后数据还在"**。容器可写层随容器删除而消失。要持久化就用 `-v`。

### 2.2 选择发行版（练包管理用）

```bash
docker pull debian:12              # apt / dpkg
docker pull ubuntu:24.04           # apt / dpkg
docker pull rockylinux:9           # dnf / rpm / firewalld / SELinux
docker pull almalinux:9            # dnf / rpm
docker pull fedora:41              # dnf / rpm
docker pull archlinux:latest       # pacman
docker pull alpine:3.20            # apk（极小，busybox 工具集）
docker pull kalilinux/kali-rolling # 🔐 Kali 工具集（apt，镜像很大）
```

```bash
# 用哪个发行版练哪个包管理
docker run --rm -it debian:12 bash -c 'apt update && apt install -y curl && dpkg -l curl'
docker run --rm -it rockylinux:9 bash -c 'dnf install -y curl && rpm -q curl'
docker run --rm -it archlinux:latest bash -c 'pacman -Sy --noconfirm curl && pacman -Qo /usr/bin/curl'
```

**怎么选镜像**（按用途，不按"哪个更流行"）：

| 镜像 | 大小 | 适合练什么 | 不建议练什么 |
|------|------|------------|--------------|
| `debian:stable` | ~120 MB | **通用首选**。`apt`/`dpkg`、`systemd`（装完就能起）、`find`/文本三剑客、POSIX shell 行为 | 需要 `dnf`/`rpm` 的内容 |
| `ubuntu:24.04` | ~80 MB | 与 `debian` 类似，但更新更快、文档更多；练 `netplan`、`ufw`、`snap` | 同上；`snapd` 在容器里默认起不来 |
| `alpine:3.20` | **~8 MB** | 快速验证"某个命令在最小系统里有没有"；练 `apk`、BusyBox 工具集差异 | ⚠️ **不要拿它当通用练习环境**：`coreutils` 是 BusyBox 版，`sed`/`tar`/`ps` 的参数与 GNU 版**不同**，你在 Alpine 上学到的写法在 Debian/RHEL 上常常不生效，反之亦然 |
| `rockylinux:9` / `almalinux:9` | ~180 MB | `dnf`/`rpm`、**SELinux**（唯一能在容器里较真实体验的）、`firewalld`、RHEL 系路径与配置文件 | —— |
| `archlinux:latest` | ~150 MB | `pacman`、滚动发行版行为、`systemd` 较新特性 | 稳定长期环境 |
| `kalilinux/kali-rolling` | ~1 GB+ | 🔐 渗透工具集（`nmap`/`hydra`/`john` 等），做 [`../commands/12-安全与审计.md`](../commands/12-安全与审计.md) 的练习 | 资源受限的机器 |

**两个通用建议**：

1. **先用 `debian:stable`**。它的 `coreutils`、`sed`、`tar`、`procps` 都是 GNU 版，与 `man` 手册和本库示例一致，能把"工具差异"这个变量排除掉。
2. **需要 root 权限的题用 `--privileged` 或按需 `--cap-add`**，不要为了省事一律 `--privileged`：
   ```bash
   # 只给网络相关能力（练 nft/iptables/tcpdump 够用）
   docker run --rm -it --cap-add=NET_ADMIN --cap-add=NET_RAW debian:stable bash
   # 需要挂 loop 设备/改挂载（练 fdisk/mkfs/mount）
   docker run --rm -it --cap-add=SYS_ADMIN --device=/dev/loop-control debian:stable bash
   ```

### 2.3 常用的容器形态

**需要 systemd 的容器**（练 `systemctl` / `journalctl`）：

```bash
docker run -it --name systemd-lab \
  --privileged \
  --cgroupns=host \
  -v /sys/fs/cgroup:/sys/fs/cgroup:rw \
  rockylinux:9 \
  /usr/sbin/init
```

| 参数 | 为什么需要 |
|------|------------|
| `--privileged` | systemd 要挂载 cgroup、管理设备；**⚠️ 这等于给容器几乎全部的宿主权限** 🔐 |
| `--cgroupns=host` | 让容器看到宿主的 cgroup 层级（cgroup v2 下的必需项） |
| `-v /sys/fs/cgroup:rw` | systemd 需要**写** cgroup |
| `/usr/sbin/init` | 用 systemd 当 PID 1（覆盖镜像默认的 CMD） |

> ⚠️ **`--privileged` 是容器逃逸的标准路径**：容器里的 root 可以 `mount` 宿主磁盘、加载内核模块、`nsenter` 进宿主命名空间。**只在练习机上这么用**，绝不要在生产环境跑 privileged 容器。
>
> 更安全的替代：用 `--cap-add` 只给需要的 capability（`SYS_ADMIN`、`NET_ADMIN`），而不是 `--privileged`。

**多机网络（练 `ping` / `ss` / `ssh` / 抓包）**：

```bash
# 建一个自定义网络（默认 bridge 网络不支持按名字解析）
docker network create --subnet 172.28.0.0/24 labnet

docker run -d --name host1 --network labnet --ip 172.28.0.1 --hostname host1 rockylinux:9 sleep infinity
docker run -d --name host2 --network labnet --ip 172.28.0.2 --hostname host2 rockylinux:9 sleep infinity

# 进 host1 测到 host2 的连通性
docker exec -it host1 bash
# 容器内：
#   ip -br addr          → 看到 172.28.0.1
#   ping -c3 host2       → 可用名字（自定义网络提供 DNS）
#   ss -tunlp
```

**加一个能抓包的容器**（练 `tcpdump`）：

```bash
docker run -d --name sniff --network labnet --cap-add=NET_ADMIN --cap-add=NET_RAW \
  --hostname sniff nicolaka/netshoot sleep infinity
docker exec -it sniff bash
# 容器内：
#   tcpdump -i eth0 -nn 'tcp port 80'
#   ss -tunap
#   ip -br addr
#   dig, mtr, iperf3, nmap, curl 都有（netshoot 镜像自带一整套网络工具）
```

> 💡 **`nicolaka/netshoot` 是"网络排障工具全家桶"镜像**，含 `tcpdump`、`tshark`、`nmap`、`mtr`、`dig`、`iperf3`、`socat`、`conntrack`、`bpftrace` 等几十个工具。没有网络工具的环境里，`docker run --net=container:<目标容器> nicolaka/netshoot` 就能"借"它的网络命名空间来排障。

**练"服务起来就退出"（场景 14）**：

```bash
docker run --rm -d --name exitdemo nginx:latest
sleep 2 && docker ps -a --filter name=exitdemo    # 看看它在不在
# 对比：
docker run --rm -d --name okdemo nginx:latest nginx -g 'daemon off;'
```

### 2.4 容器里练不了什么

| 内容 | 为什么 | 替代 |
|------|--------|------|
| 内核模块（`lsmod`、`modprobe`） | 共享宿主内核，无权限加载 | 虚拟机 |
| 磁盘分区（`fdisk`、`mkfs`） | 不能用宿主块设备（除 loop 文件） | 用 **loop 文件当磁盘**（见下） |
| 系统启动过程（GRUB、initramfs） | 容器没有独立的启动链 | 虚拟机（或 `systemd-nspawn` 部分可做） |
| `fstab` 挂载 | 容器内 `mount` 受限（除 `--privileged`） | `--privileged` + loop 文件，或虚拟机 |
| cgroup v2 的完整功能 | 容器自身的 cgroup 受宿主限制 | 虚拟机 |
| SELinux / AppArmor 完整策略 | 容器里的策略是被裁剪的 | 虚拟机（Rocky/Alma） |

**在容器里练分区（用 loop 文件当"硬盘"）** —— 这是个很实用的技巧：

```bash
# 在**宿主**上创建一块"假硬盘"
dd if=/dev/zero of=~/linux-lab/disk.img bs=1M count=200      # 200MB

# 起一个带特权 + 内核能力的容器（loop 设备需要）
docker run -it --rm --privileged -v ~/linux-lab:/lab debian:12 bash

# 容器内：
#   ls -l /lab/disk.img
#   losetup -fP /lab/disk.img                # 关联成 loop 设备（自动分区）
#   losetup -a
#   fdisk /dev/loop0                         # 练 fdisk！（全在假盘上，安全）
#   mkfs.ext4 /dev/loop0p1
#   mkdir -p /mnt/test && mount /dev/loop0p1 /mnt/test
#   df -h /mnt/test
#   umount /mnt/test && losetup -d /dev/loop0
```

> 💡 **这个套路能安全地练几乎所有磁盘命令**（`fdisk`/`parted`/`mkfs`/`mount`/`fsck`/`resize2fs`），因为操作对象是一个文件而不是真磁盘。**练完删掉 `disk.img` 就行，没有任何风险。**
>
> ⚠️ 但需要 `--privileged` 或 `--cap-add=SYS_ADMIN` + `--device=/dev/loop-control`。同时**必须仔细检查 `/lab/disk.img` 的路径** —— `losetup`/`dd` 写错设备名是真会毁盘的。

---

## 三、方案 B：虚拟机

### 3.0 装 Debian / Ubuntu Server 的要点（VMware / VirtualBox / KVM 通用）

排障类实验（`fstab`、systemd、磁盘、网络）**必须用虚拟机**，因为要在独立内核里改系统级配置并且需要快照回滚。下面是装 Debian 12 / Ubuntu Server 24.04 时的推荐参数。

**内存**

| 用途 | 建议 | 说明 |
|------|------|------|
| 只练命令与排障 | **2 GB** | Server 版无桌面，1 GB 也能跑，但跑 `dnf`/`apt` 升级时容易 OOM |
| 要跑数据库/多个服务 | 4 GB | 做第 4 节实验 6（OOM）时留出观察空间 |
| 想做 OOM 实验 | 1 GB + swap 512 MB | 内存小才容易触发，但**别用 512 MB**，`apt` 都可能失败 |

> 💡 内存越小越容易复现"内存不足 / OOM"类问题，但也越容易在装包时莫名失败。**建议建两台**：一台 2 GB 当日常，一台 1 GB 专门做资源耗尽实验。

**磁盘**

| 项 | 建议 | 理由 |
|----|------|------|
| 容量 | **20 GB** | 够装 `build-essential`、`docker`、`postgresql` 等，且能给快照留空间 |
| 格式 | **qcow2（KVM）/ VDI（VirtualBox，动态分配）** | 稀疏分配，实际占用远小于声明值 |
| 分区方案 | **LVM**（Ubuntu Server 安装器默认就是） | ⭐ 关键：LVM 让你能**在线扩容**且方便做快照；做实验时不至于因为分区满了就重装 |
| 单独分区 | 建议 `/home`、`/var` 独立 | `/var/log` 写满时不会拖垮 `/`（便于重现第 4 节实验 1、实验 16 的场景） |
| 交换分区 | 内存的 1~2 倍，或 2 GB | 做内存实验需要 |

> ⚠️ **不要选"整块盘"自动分区加 `ext4` 无 LVM**，否则事后想扩容非常麻烦。Ubuntu Server 安装器里选 **"Use an entire disk + Set up this disk as an LVM group"**。

**网络模式**

| 模式 | VM 出网 | 宿主能访问 VM | 局域网能访问 VM | 用在什么时候 |
|------|---------|---------------|-----------------|--------------|
| **NAT**（默认） | ✅ | 需端口转发 | ❌ | **日常练习首选**，最安全 |
| **Host-only / 私有网络** | ❌ | ✅ | ❌ | 做网络实验、多机互连；配合 NAT 双网卡即可既出网又隔离 |
| **Bridged（桥接）** | ✅ | ✅ | ✅ | ⚠️ **只有在明确需要时才用**；含漏洞的靶机**绝对不能**用它 |
| **Internal（VirtualBox）** | ❌ | ❌ | ❌ | 纯 VM 之间通信，做隔离拓扑 |

**推荐配置：两张网卡**

```
网卡1: NAT        → 用于 apt/dnf 装包、访问外网
网卡2: Host-only  → 192.168.56.0/24，用于宿主 SSH 进 VM、做网络实验
```

**安装时的几个勾选项**

| 选项 | 建议 | 理由 |
|------|------|------|
| OpenSSH server | **勾上** | 装完就能从宿主 `ssh` 进去，不用在 VM 窗口里敲字（操作体验差别巨大） |
| 标准系统工具（standard system utilities） | 勾上 | 含 `man`、`ps` 等，不勾会缺一堆基础命令 |
| 桌面环境 | **不勾** | Server 版就够；省内存，且更接近真实服务器 |
| 自动更新 | 根据需要 | 做"包管理"实验时建议**关掉**，否则 `apt` 会被后台更新占用锁 |
| 快照 | **装完立刻打一个** | `virsh snapshot-create-as` / VirtualBox `snapshot take clean`，之后随便折腾 |

**装完先做的 5 件事**（建立基线）

```bash
# 1) 确认能连网、能解析、能装包
ip -br addr && ping -c2 1.1.1.1 && getent hosts deb.debian.org

# 2) 打快照（KVM）
virsh snapshot-create-as debian-lab clean "装完基线"

# 3) 记录一份"干净状态"的基线，之后做实验时能对比
sudo find /etc /usr/bin /usr/sbin -printf '%m %u:%g %p\n' 2>/dev/null | sort > ~/baseline_perms.txt
sudo find / -xdev -type f -perm -4000 -print 2>/dev/null | sort > ~/baseline_suid.txt

# 4) 装上后面实验要用的工具（一次装齐，避免实验中途被锁）
sudo apt install -y lsof strace sysstat tcpdump nftables auditd \
                    psmisc procps iproute2 dnsutils netcat-openbsd mtr-tiny tree
sudo systemctl enable --now sysstat        # 让 sar 开始采样，实验 14 要用历史数据

# 5) 关掉那些会"自己动"的服务，避免干扰实验
sudo systemctl disable --now apt-daily.timer apt-daily-upgrade.timer unattended-upgrades 2>/dev/null || true
sudo systemctl disable --now systemd-timesyncd   # ⚠️ 只在做时间实验（实验 10）时关，平时要开着
```

**容器里练 `systemctl` 的坑**（为什么排障实验必须用虚拟机）

Docker 容器默认**没有 init 系统**，`systemctl` 会直接报错：

```bash
$ docker run --rm -it debian:stable systemctl status
System has not been booted with systemd as init system (PID 1). Can't operate.
```

要让它工作，需要同时满足三个条件（`--privileged` + host cgroup 命名空间 + 可读写 cgroup 挂载），并显式用 init 当 PID 1：

```bash
docker run -it --name systemd-lab \
  --privileged \
  --cgroupns=host \
  -v /sys/fs/cgroup:/sys/fs/cgroup:rw \
  debian:stable \
  /sbin/init
```

即便这样也有三个限制：

| 限制 | 后果 | 替代做法 |
|------|------|----------|
| `--privileged` 给了容器**几乎全部宿主权限** | 🔐 这本身就是容器逃逸路径，只在练习机上用 | 只在专用练习机/VM 里跑 privileged 容器 |
| 无法测试启动过程（GRUB、initramfs、`rescue.target`） | 「启动失败排障」做不了 | 必须用虚拟机（实验 2） |
| cgroup 层级受宿主约束 | 资源限制实验的数值不真实 | 用虚拟机，或 `systemd-run -p MemoryMax=` 做局部实验 |

**所以在容器里排障时，用这些替代验证方式**（不依赖 systemd）：

```bash
# 想看"服务是否在跑" → 直接看进程与监听，而不是 systemctl status
ps -eo pid,user,args | grep -v grep | grep <服务名>
ss -tlnp

# 想看日志 → 直接读日志文件，而不是 journalctl
tail -n 50 /var/log/syslog        # Debian/Ubuntu
tail -n 50 /var/log/nginx/error.log

# 想管服务 → 直接起前台进程
/usr/sbin/nginx -g 'daemon off;' &

# 想看资源限制 → 读 cgroup 文件
cat /sys/fs/cgroup/system.slice/<unit>/memory.max
```

> 💡 结论：**文件/权限/文本/进程/网络命令 → 容器足够；systemd / 启动 / 磁盘 / 资源限制 → 必须虚拟机。**

### 3.1 KVM + libvirt（Linux 宿主，性能最好）

```bash
# Arch / Omarchy
sudo pacman -S qemu-full libvirt virt-manager virt-install dnsmasq bridge-utils

# Debian/Ubuntu
sudo apt install qemu-kvm libvirt-daemon-system virtinst virt-manager bridge-utils

sudo systemctl enable --now libvirtd
sudo usermod -aG libvirt,kvm "$USER"        # ⚠️ 必须重新登录才生效

# 验证
$ virt-host-validate
QEMU: Checking for hardware virtualization                         : PASS
QEMU: Checking if device /dev/kvm exists                           : PASS
```

**创建虚拟机**（用 `virt-install` 一条命令）：

```bash
# 下载一个 cloud image（比装 ISO 快得多）
mkdir -p ~/vms/images && cd ~/vms/images
curl -fSLO https://cloud.rockylinux.org/rocky/images/Rocky-9-GenericCloud-Base.latest.x86_64.qcow2

# 准备好 cloud-init 配置（设置用户、密码、SSH key）
cat > ~/vms/cloud-init.yaml <<'EOF'
#cloud-config
users:
  - name: lab
    sudo: ALL=(ALL) NOPASSWD:ALL
    ssh_authorized_keys:
      - <把你的公钥粘这里>
    lock_passwd: false
ssh_pwauth: true
chpasswd:
  list: |
    lab:lab123
  expire: false
EOF

# 把 cloud-init 打进一个种子 ISO
sudo pacman -S cdrtools 2>/dev/null || sudo apt install genisoimage
genisoimage -output ~/vms/seed.iso -volid cidata -joliet -rock ~/vms/cloud-init.yaml

# 建虚拟机
qemu-img create -f qcow2 -b ~/vms/images/Rocky-9-GenericCloud-Base.latest.x86_64.qcow2 \
  -F qcow2 ~/vms/rocky9-lab.qcow2 20G

sudo virt-install \
  --name rocky9-lab \
  --memory 2048 --vcpus 2 \
  --disk path=$HOME/vms/rocky9-lab.qcow2,format=qcow2 \
  --disk path=$HOME/vms/seed.iso,device=cdrom \
  --network network=default,model=virtio \
  --graphics none --console pty,target_type=serial \
  --import --os-variant rocky9
```

**日常管理**：

```bash
$ virsh list --all
$ virsh start rocky9-lab
$ virsh console rocky9-lab                 # Ctrl+] 退出控制台
$ virsh domifaddr rocky9-lab               # 查 VM 拿到的 IP（SSH 进去）
$ ssh lab@<VM-IP>
$ virsh snapshot-create-as rocky9-lab clean "干净基线"
$ virsh snapshot-revert rocky9-lab clean   # ⭐ 随时回滚到干净状态
$ virsh destroy rocky9-lab                 # ⚠️ 拔电式关机
```

> ⭐ **快照是虚拟机最大的价值**。做破坏性实验前：
> ```bash
> $ virsh snapshot-create-as rocky9-lab before-experiment
> # 实验（可以随便搞坏）
> $ virsh snapshot-revert rocky9-lab before-experiment
> ```

### 3.2 VirtualBox（跨平台，图形界面友好）

```bash
# 无头服务器上的典型流程
VBoxManage createvm --name lab --ostype RedHat_64 --register
VBoxManage modifyvm lab --memory 2048 --cpus 2 \
  --nic1 nat --natpf1 "ssh,tcp,,2222,,22" \
  --nic2 hostonly --hostonlyadapter2 vboxnet0
VBoxManage storagectl lab --name SATA --add sata --controller IntelAhci
VBoxManage createmedium disk --filename ~/VirtualBox/lab.vdi --size 20480
VBoxManage storageattach lab --storagectl SATA --port 0 --device 0 --type hdd --medium ~/VirtualBox/lab.vdi
VBoxManage storagectl lab --name IDE --add ide
VBoxManage storageattach lab --storagectl IDE --port 1 --device 0 --type dvddrive --medium /path/to.iso
VBoxManage startvm lab --type headless
VBoxManage snapshot lab take clean
VBoxManage snapshot lab restore clean
```

> ⚠️ **虚拟机网络模式的选择在安全实验里很关键** 🔐：
>
> | 模式 | VM 能否出网 | 局域网能否访问 VM | 适用 |
> |------|-------------|-------------------|------|
> | `NAT` | ✅ | ❌（要端口转发） | 日常练习，**最安全** |
> | `Host-only` | ❌ | ❌（只有宿主能访问） | **含漏洞的靶机，必须用这个** |
> | `Bridged` | ✅ | ✅（**和你的笔记本同一广播域**） | ⚠️ 危险，靶机绝不能用 |
> | `Internal`（VBox） | ❌ | ❌（只有 VM 之间） | 多机隔离实验 |
>
> **把含漏洞的靶机接 `Bridged`，等于把它直接暴露在办公网里。** 这是真实事故。

### 3.3 Vagrant（一条命令拉起多机拓扑）

```bash
mkdir -p ~/vms/vagrant-lab && cd ~/vms/vagrant-lab
vagrant init -m generic/rocky9
```

编辑 `Vagrantfile`：

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "generic/rocky9"
  config.vm.synced_folder ".", "/vagrant", disabled: true

  # 三台机器 + 一张内部网络，用于练"互 ping / ssh / 抓包 / 防火墙"
  {
    "web"  => { ip: "192.168.56.11", mem: 1024 },
    "db"   => { ip: "192.168.56.12", mem: 1024 },
    "attacker" => { ip: "192.168.56.99", mem: 512 }
  }.each do |name, cfg|
    config.vm.define name do |node|
      node.vm.hostname = name
      # 第一张网卡 NAT（用于 apt/dnf 装包），第二张 host-only（实验网）
      node.vm.network "private_network", ip: cfg[:ip]
      node.vm.provider "virtualbox" do |vb|
        vb.memory = cfg[:mem]
        vb.cpus   = 1
      end
    end
  end
end
```

```bash
$ vagrant up
$ vagrant status
$ vagrant ssh web
$ vagrant halt
$ vagrant snapshot save clean
$ vagrant snapshot restore clean
$ vagrant destroy -f          # ⚠️ 删掉所有机器与磁盘
```

> ⚠️ Vagrant 的 box 用的是**公开的不安全私钥**（用户名/密码都是 `vagrant`）。这套环境**绝不能暴露到公网**。

### 3.4 distrobox（在宿主里跑另一个发行版，最轻量）

```bash
# 适合"我只想试某个发行版才有的包/命令"
distrobox create --name rocky --image rockylinux:9
distrobox enter rocky
# 容器内：dnf install -y httpd && rpm -q httpd
distrobox rm rocky
```

见 [`../commands/14-容器与虚拟化.md`](../commands/14-容器与虚拟化.md) 的 `distrobox` 小节（含它不是沙箱的注意事项 🔐）。

---

## 四、排障实验清单（把系统"故意搞坏"）

**每个实验都遵循同样的四步**：

```
1. 建快照 / 记录基线
2. 制造故障
3. 只用命令行诊断（不看本库答案，自己推）
4. 恢复（或回滚快照），并写下"我是怎么找到的"
```

> ⭐ **第 3 步是关键**：故障是你自己造的，所以你知道答案。**请假装不知道**，从"现象"出发按分层流程推。这句话是本清单唯一的价值。

### 4.0 清单总表（15 个排障实验）

| # | 目标（要复现什么） | 步骤要点 | 验证方式（做对了会看到什么） |
|---|--------------------|----------|------------------------------|
| 1 | **磁盘满，但 `du` 算出来很小** | `truncate` 造大文件 → 用 python 打开并 `rm` 掉它 | `df -h` 显示 100%，而 `du -sh` 只几 MB；`lsof +L1` 列出带 `(deleted)` 的条目 |
| 2 | **`fstab` 写错 → 开机进紧急模式** | 加一条 UUID 不存在的挂载 → 重启 | 启动卡在 `emergency mode`；`mount -o remount,rw /` 后改回并重启才能进系统 |
| 3 | **服务起不来（各类 EXEC 失败）** | 写 3 个坏 unit（路径不存在 / 无执行位 / `WorkingDirectory` 不存在） | `systemctl status` 显示 `203/EXEC`、`200/CHDIR`；`systemd-analyze verify` 报语法问题 |
| 4 | **cron 任务手工能跑、定时失败** | 写一个依赖 `PATH` 的脚本放进 crontab | `env > /tmp/cron_env.txt` 显示 cron 的 `PATH` 只有 `/usr/bin:/bin`；日志里 `command not found` |
| 5 | **权限混乱，`403` 却"文件看着正常"** | 去掉 Web 根目录的 `x` 位；另造 4755 / 666 / 777 样本 | `namei -l` 一眼看出哪一级缺 `x`；`find -perm -4000` / `-perm -0002` 能审计出异常样本 |
| 6 | **内存泄漏 → OOM 被内核杀掉** | 跑泄漏脚本并用 `systemd-run -p MemoryMax=200M` 限制 | `dmesg`/`journalctl -k` 出现 `Killed process`；`memory.events` 的 `oom_kill` 递增 |
| 7 | **CPU 或 IO 打满 → `load` 飙升** | 造 N 个满核进程（CPU 实验）或 `dd oflag=direct`（IO 实验） | `uptime` 的 load ≈ 核数倍数；CPU 实验 `%us` 高，IO 实验 `vmstat` 的 `b` 与 `wa` 高、`/proc/pressure/io` 的 `full` 上升 |
| 8 | **分区/格式化/扩容（零风险版）** | 用 loop 文件当硬盘：`losetup -fP` → `parted` → `mkfs` → `mount` → `resize2fs` | `lsblk` 看到 loop 设备与分区；扩容后 `df -h` 的容量真的变大 |
| 9 | **网络不通（分层定位）** | 两个容器 + 三种故障：服务停了 / 只绑 `127.0.0.1` / INPUT `DROP` | `Connection refused` vs `Connection timed out` 的区别；服务端 `tcpdump` 能看到/看不到 SYN |
| 10 | **时间错乱** | `timedatectl set-ntp false` 后把时间设到过去 | `curl -v https://...` 报 `certificate is not yet valid`；`journalctl` 时间戳异常 |
| 11 | **磁盘被写满（真实写满，不是空洞文件）** | 在挂载的 loop 分区上 `dd` 写满，或让日志疯狂增长 | `df -h` 到 100%；写操作报 `No space left on device`；`find` 找 `-size +100M` 能定位杀手 |
| 12 | **inode 耗尽（有空间但建不了文件）** | 挂一个小 inode 数的文件系统并创建海量空文件 | `df -h` 还有余量，但 `df -i` 显示 `IUse% 100%`；`touch` 报 `No space left on device` |
| 13 | **误删文件但空间没释放（不重启进程救回）** | 进程打开文件 → `rm` 文件 → 从 fd 恢复 | `lsof +L1` 或 `/proc/PID/fd` 找到 `(deleted)`；`cp /proc/PID/fd/N` 恢复后 `reload` 释放空间 |
| 14 | **启动很慢，定位是谁拖的** | 注入一个 `After=network-online.target` 的慢服务 / 用 `systemd-analyze blame` 看现状 | `systemd-analyze blame` 排出耗时榜；`critical-chain` 指出真正的阻塞环节 |
| 15 | **抓包与防火墙规则** | `tcpdump -i lo` 抓本机回环流量；用 `nft` 建规则并观察生效 | `tcpdump` 能抓到 `127.0.0.1` 上的 HTTP 明文；`nft list ruleset` 能看到规则与计数器增长 |

**每题标准动作**：`建快照/记基线 → 制造故障 → 只看现象诊断 → 恢复 → 写三行记录`（见第 6 节）。


### 实验 1 · 磁盘满但 `du` 很小

```bash
# 制造
dd if=/dev/zero of=/var/tmp/bigfile bs=1M count=500
tail -f /dev/null > /dev/null &     # 占位
python3 -c "
import time
f = open('/var/tmp/ghost.log','w')
for i in range(200000): f.write('x'*100 + '\n')
f.flush()
"
rm /var/tmp/ghost.log                # 删掉但 python 还开着 fd
rm /var/tmp/bigfile                  # 这个是正常删除，空间会释放

# 现象：df 显示磁盘满，du 找不到大文件
df -h /var && sudo du -sh /var/tmp

# 你要用的命令
sudo lsof +L1
sudo ls -l /proc/*/fd/* 2>/dev/null | grep deleted
sudo truncate -s 0 /proc/<PID>/fd/<N>

# 对照答案
# → ../practice/06-综合场景题.md 场景 1
```

### 实验 2 · `fstab` 写错导致系统进紧急模式

```bash
# ⚠️ 必须在能回滚的虚拟机里做
sudo cp /etc/fstab /etc/fstab.bak
echo "UUID=00000000-0000-0000-0000-000000000000 /mnt/broken ext4 defaults 0 2" | sudo tee -a /etc/fstab
sudo reboot
# 现象：启动卡在 "emergency mode" / "You are in emergency mode"

# 恢复（在紧急模式里，根分区通常已只读挂载）
mount -o remount,rw /
cp /etc/fstab.bak /etc/fstab
systemctl reboot

# 或者：在启动参数里加 systemd.unit=rescue.target 进救援模式后修
```

**学到的东西**：`/etc/fstab` 的错误会让系统**起不来**（因为本地文件系统挂载是 `local-fs.target` 的强依赖）。所以——

```bash
# 改完 fstab 必须验证！
sudo mount -a          # 有任何报错就说明 fstab 有问题，立即修
findmnt --verify       # 更严格的结构校验
```

> ⭐ **`sudo mount -a` 是改 fstab 后的强制动作**。它按 fstab 重新挂载所有条目，有错立刻报出来 —— 在重启前发现，比重启后进不了系统好得多。

### 实验 3 · 服务起不来（`203/EXEC` / `200/CHDIR` / 依赖缺失）

```bash
# 制造三种不同的失败
sudo tee /etc/systemd/system/bad1.service <<'EOF'
[Unit]
Description=Bad ExecStart
[Service]
ExecStart=/opt/nonexistent/start.sh
[Install]
WantedBy=multi-user.target
EOF

sudo tee /etc/systemd/system/bad2.service <<'EOF'
[Service]
WorkingDirectory=/opt/does-not-exist
ExecStart=/bin/sleep 3600
EOF

sudo systemctl daemon-reload
sudo systemctl start bad1 bad2

# 现象与诊断
systemctl status bad1       # 203/EXEC → 找不到可执行文件
systemctl status bad2       # 200/CHDIR → WorkingDirectory 不存在
journalctl -u bad1 -n 20 --no-pager
systemd-analyze verify /etc/systemd/system/bad1.service

# 对照答案
# → ../practice/06-综合场景题.md 场景 4
```

### 实验 4 · cron 任务失败（环境差异）

```bash
# 制造：写一个依赖 PATH 的脚本
sudo tee /opt/crontest.sh <<'EOF'
#!/bin/bash
echo "PATH=$PATH"
echo "SHELL=$SHELL"
which curl || echo "curl not found"
curl -sS -o /dev/null -w '%{http_code}\n' https://example.com
EOF
sudo chmod +x /opt/crontest.sh

# 手工跑（成功）
/opt/crontest.sh

# 放进 cron（失败）
crontab -e
# * * * * * /opt/crontest.sh > /tmp/crontest.log 2>&1

# 等一分钟，看日志
sleep 70 && cat /tmp/crontest.log

# 你要用的命令
env > /tmp/cron_env.txt         # 在 crontab 里跑，对比环境
journalctl -u cron -n 30 --no-pager

# 修复
# → 在 crontab 顶部加 PATH= / SHELL=，或脚本里显式 export PATH
```

### 实验 5 · 权限事故（403 与"文件看着正常"）

```bash
# 起一个 web 服务
sudo dnf install -y httpd && sudo systemctl start httpd
sudo sh -c 'echo "hello" > /var/www/html/index.html'

# 制造：把目录的 x 位去掉（只保留 r）
sudo chmod 644 /var/www/html
curl -sS -o /dev/null -w '%{http_code}\n' http://localhost/    # → 403

# 你要用的命令
sudo -u apache namei -l /var/www/html/index.html       # ⭐ 一眼看出哪一级缺 x
ls -ld /var/www/html
sudo -u apache cat /var/www/html/index.html            # 验证能不能读

# 修复（目录 755，文件 644）
sudo find /var/www/html -type d -exec chmod 755 {} +
sudo find /var/www/html -type f -exec chmod 644 {} +

# 对照答案
# → ../practice/06-综合场景题.md 场景 9
```

### 实验 6 · 内存泄漏 / OOM

```bash
# 制造（故意泄漏内存的 Python 脚本）
cat > /tmp/leak.py <<'EOF'
import time
leak = []
while True:
    leak.append('x' * 1_000_000)     # 每秒泄漏 1MB
    time.sleep(0.1)
EOF

# 限制可用内存，快速触发 OOM（用 systemd-run 起临时服务）
sudo systemd-run --unit=leaker --property=MemoryMax=200M --property=MemorySwapMax=0 \
  python3 /tmp/leak.py

# 观察（另一个终端）
watch -n 1 'systemctl status leaker --no-pager | head -20'
cat /sys/fs/cgroup/system.slice/leaker.service/memory.current
cat /sys/fs/cgroup/system.slice/leaker.service/memory.events
journalctl -k | grep -i oom | tail
coredumpctl list leaker 2>/dev/null

# 清理
sudo systemctl stop leaker

# 对照答案
# → ../practice/06-综合场景题.md 场景 6
```

### 实验 7 · 磁盘 IO 打满导致 load 飙升

```bash
# 制造：用带 sync 的 dd 压磁盘（会同时压 IO 和 dirty page）
sudo dd if=/dev/zero of=/var/tmp/io_stress bs=1M count=20000 oflag=direct &

# 观察（另一个终端）
uptime                          # load 上升
vmstat 1 5                      # 看 b 列（blocked）和 wa
iostat -xz 1 5                  # 看 await / aqu-sz（需 sysstat）
cat /proc/pressure/io           # ⭐ PSI，最直接的"IO 停顿"指标
ps -eo stat,pid,wchan:24,comm | awk '$1 ~ /^D/'
sudo iotop -oP 2>/dev/null || sudo pidstat -d 1

# 清理
sudo kill %1    # ⚠️ 如果 kill 不掉，说明在 D 状态 → 等它写完
rm -f /var/tmp/io_stress

# 对照答案
# → ../practice/06-综合场景题.md 场景 3
```

### 实验 8 · 分区与文件系统（loop 文件安全版）

```bash
# 用 loop 文件当"硬盘"，全程零风险
dd if=/dev/zero of=/tmp/fakedisk.img bs=1M count=200

# 关联成块设备
sudo losetup -fP /tmp/fakedisk.img
sudo losetup -a
LOOP=$(losetup -j /tmp/fakedisk.img | cut -d: -f1)
echo "loop 设备: $LOOP"

# 分区（非交互）
sudo parted -s "$LOOP" mklabel gpt
sudo parted -s "$LOOP" mkpart primary ext4 1MiB 100MiB
sudo partprobe "$LOOP" 2>/dev/null
sudo lsblk "$LOOP"

# 格式化与挂载
sudo mkfs.ext4 "${LOOP}p1"
sudo mkdir -p /mnt/fake && sudo mount "${LOOP}p1" /mnt/fake
df -h /mnt/fake
sudo tune2fs -l "${LOOP}p1" | head -20

# 练扩容（先 dump 再扩）
sudo umount /mnt/fake
sudo parted -s "$LOOP" resizepart 1 150MiB
sudo e2fsck -f "${LOOP}p1"
sudo resize2fs "${LOOP}p1"
sudo mount "${LOOP}p1" /mnt/fake && df -h /mnt/fake

# 清理
sudo umount /mnt/fake
sudo losetup -d "$LOOP"
rm /tmp/fakedisk.img
```

### 实验 9 · 网络不通（分层排查）

```bash
# 需要两台机器（两个容器或两台 VM）
# 在"服务端"起一个 web 服务
docker run -d --name srv --network labnet --ip 172.28.0.10 nginx:alpine

# 在"客户端"制造不同的问题并观察现象
docker exec -it host1 bash

# 情况 A：服务没起来
docker stop srv
# 客户端：nc -zvw3 172.28.0.10 80   → Connection refused

# 情况 B：监听地址不对（只绑 127.0.0.1）
# 客户端：→ Connection refused，但服务在跑

# 情况 C：防火墙 DROP
docker exec srv sh -c 'apk add --no-cache iptables && iptables -A INPUT -p tcp --dport 80 -j DROP'
# 客户端：nc -zvw3 172.28.0.10 80   → Connection timed out  ⭐ 和 refused 的区别

# 你要用的命令（在服务端）
ss -tlnp
tcpdump -i eth0 -nn 'tcp port 80 and tcp[tcpflags] & tcp-syn != 0'
iptables -L -n -v

# 对照答案
# → ../practice/05-网络题.md 题 20
```

### 实验 10 · 时间错乱

```bash
# ⚠️ 在虚拟机里做！会影响宿主的时间感知
sudo timedatectl set-ntp false
sudo timedatectl set-time '2020-01-01 00:00:00'

# 观察后果
date
curl -v https://example.com 2>&1 | grep -i 'certificate'
curl -v https://example.com 2>&1 | grep -i 'not yet valid'
journalctl -n 5 --no-pager            # 日志时间戳变奇怪
make 2>&1 | head -3                   # 如果有代码目录，会报"时间在未来"

# 修复
sudo timedatectl set-ntp true
sudo chronyc makestep 2>/dev/null || sudo systemctl restart systemd-timesyncd
timedatectl
date -u

# 对照答案
# → ../practice/06-综合场景题.md 场景 10
```

### 实验 11 · 真实写满一个分区（不是空洞文件）

**目标**：复现"磁盘真的没有空间了"，并区分它与"空洞文件占位"的差别。

<details><summary>步骤与验证</summary>

```bash
# ⚠️ 只在一块 loop 假盘上做，不要写宿主的真实分区
truncate -s 64M /tmp/linux-lab/img/fakedisk.img
LOOP=$(sudo losetup -f --show /tmp/linux-lab/img/fakedisk.img)   # -f 取空闲、--show 打印设备名
sudo mkfs.ext4 -q "$LOOP"
sudo mkdir -p /mnt/fill && sudo mount "$LOOP" /mnt/fill

# 制造：一直写到没空间
sudo dd if=/dev/zero of=/mnt/fill/filler bs=1M count=200
# 预期报错：dd: error writing '/mnt/fill/filler': No space left on device

# 现象
df -h /mnt/fill                 # Use% = 100%
df -i /mnt/fill                 # inode 还够（和实验 12 区分）
sudo du -sh /mnt/fill           # du 这次能算出来（和实验 1 区分）

# 再试一次写
sudo touch /mnt/fill/x          # 报 No space left on device
```

**验证方式**：`df -h` 到 100%，`touch` 报错；而 `lsof +L1` **没有**输出（说明不是"已删除但仍被占用"那种假满）。

**顺带对比三个"满了"的区别**：

| 现象 | `df -h` | `df -i` | `du` | `lsof +L1` |
|------|---------|---------|------|------------|
| 真的写满（本实验） | 100% | 正常 | ≈ 分区大小 | 无 |
| 文件被删但仍被占用（实验 1） | 100% | 正常 | 远小于分区 | **有** |
| inode 耗尽（实验 12） | 有余量 | **100%** | ≈ 分区大小 | 无 |

**清理**：

```bash
sudo umount /mnt/fill && sudo losetup -d "$LOOP" && rm -f /tmp/linux-lab/img/fakedisk.img
```

</details>

### 实验 12 · inode 耗尽（有空间却建不了文件）

**目标**：复现"`df -h` 有余量，但 `touch` 报 `No space left on device`"这一极具误导性的故障。

<details><summary>步骤与验证</summary>

```bash
# 关键：mkfs 时把 inode 数设得很小（-N 指定 inode 总数），空间却给足
truncate -s 64M /tmp/linux-lab/img/inode.img
LOOP=$(sudo losetup -f --show /tmp/linux-lab/img/inode.img)
sudo mkfs.ext4 -q -N 512 "$LOOP"        # 只给 512 个 inode！
sudo mkdir -p /mnt/inode && sudo mount "$LOOP" /mnt/inode

# 制造：建超过 512 个文件
sudo bash -c 'cd /mnt/inode && for i in $(seq 1 600); do : > f$i 2>/dev/null || break; done'

# 诊断
df -h /mnt/inode          # ⭐ 还有几十 MB 空闲！
df -i /mnt/inode          # ⭐ IUse% = 100%
df -i /mnt/inode | awk 'NR==2{printf "inode: 已用 %s / 共 %s\n", $3, $2}'
sudo touch /mnt/inode/x
# touch: cannot touch '/mnt/inode/x': No space left on device   ← 空间还有，但 inode 没了
```

**验证方式**：`df -h` 显示有余量、`df -i` 显示 `IUse% 100%`、`touch` 报 `No space left on device`。三者同时成立才算复现成功。

**真实场景里怎么找"谁造的几百万个小文件"**：

```bash
# 按目录统计文件数，找出"小文件海"
sudo find / -xdev -type f 2>/dev/null | sed 's#/[^/]*$##' | sort | uniq -c | sort -rn | head -20
# 常见元凶
sudo find /var/spool/postfix/maildrop -type f 2>/dev/null | wc -l   # cron 输出堆积（因为没重定向）
sudo find /var/lib/php/sessions -type f 2>/dev/null | wc -l
ls -l /tmp | wc -l
```

> 💡 **`sed 's#/[^/]*$##'` 是取"文件所在目录"的省事写法**：把最后一个 `/` 之后的内容删掉。比 `dirname` 快得多（没有进程开销）。

**清理**：

```bash
sudo umount /mnt/inode && sudo losetup -d "$LOOP" && rm -f /tmp/linux-lab/img/inode.img
```

</details>

### 实验 13 · 误删了一个正在被写入的文件，用 `/proc` 救回来

**目标**：复现"`rm` 之后空间没释放"，并从文件描述符把内容完整捞出来，最后让进程重新打开日志。

<details><summary>步骤与验证</summary>

```bash
# 1) 让一个进程打开文件并持续写入（用 python 保持 fd）
python3 - <<'PY' &
open('/tmp/linux-lab/occupy/ghost.log', 'w').close()   # 先确保文件存在
f = open('/tmp/linux-lab/occupy/ghost.log', 'a')
import time
while True:
    f.write('x' * 4096 + '\n'); f.flush(); time.sleep(0.2)
PY
WRITER=$!
echo "写入进程 PID = $WRITER"
sleep 1

# 2) 记下删除前的大小
ls -l /tmp/linux-lab/occupy/ghost.log

# 3) ⚠️ 删掉它（模拟手滑）
rm /tmp/linux-lab/occupy/ghost.log
ls /tmp/linux-lab/occupy/ghost.log      # 已经不存在

# 4) 它还在长 —— 看 fd
sudo lsof +L1 | grep ghost
# mysqld/python3  12345 rivo  3w  REG  8,1  1234567  0  12345 /tmp/.../ghost.log (deleted)
ls -l /proc/$WRITER/fd | grep deleted
PID=$(sudo lsof -t +L1 | head -1)      # 或直接用 $WRITER

# 5) 从 fd 恢复内容（cp 会新建一个文件）
sudo cp "/proc/$WRITER/fd/3" /tmp/linux-lab/occupy/ghost.restored
sudo chown "$(id -u):$(id -g)" /tmp/linux-lab/occupy/ghost.restored
wc -l /tmp/linux-lab/occupy/ghost.restored
tail -2 /tmp/linux-lab/occupy/ghost.restored

# 6) 让进程重开文件（这里直接杀掉写入进程，因为它是我们自己起的）
kill "$WRITER"; wait "$WRITER" 2>/dev/null
ls -l /proc/$WRITER 2>&1 | head -1     # 已消失，fd 随之释放
```

**验证方式**：
1. `rm` 之后 `lsof +L1`（或 `ls -l /proc/<PID>/fd | grep deleted`）能列出带 `(deleted)` 的条目 —— 证明"空间没释放"的原因。
2. `cp /proc/<PID>/fd/N` 得到的文件**行数与删除前一致**（`wc -l` 对比）—— 证明内容被完整救回。
3. 进程退出/重开后，`lsof +L1` 不再有该条目。

> ⚠️ **真实场景里不要 `kill` 生产进程**。正确做法是给它发 `reload` 类信号让它重开日志：
> ```bash
> sudo kill -USR1 <PID>     # 很多守护进程用它"重开日志文件"
> sudo kill -HUP  <PID>     # 另一批用它做 reload
> sudo systemctl reload <服务>   # 最稳的写法（由 unit 决定发什么信号）
> ```
> 或者只清空不恢复：`sudo truncate -s 0 /proc/<PID>/fd/N`（**数据永久丢失**，先确认内容不重要）。

**根因**：日志轮转（logrotate）如果**缺少 `postrotate` 段**，程序会继续往旧 inode 写，空间永远不释放。这就是为什么 `logrotate` 配置必须让程序重新打开日志。

</details>

### 实验 14 · 用 `systemd-analyze` 找出拖慢启动的服务

**目标**：读懂 `blame` 与 `critical-chain`，区分"自己慢"和"在等别人"。

<details><summary>步骤与验证</summary>

```bash
# 1) 先看现在的启动耗时构成
systemd-analyze
# Startup finished in 3.214s (firmware) + 2.847s (loader) + 4.123s (kernel) + 35.602s (userspace) = 45.786s
#                                       ↑ 固件      ↑ GRUB      ↑ 内核        ↑ 用户态 ← 通常是这里

# 2) 按"服务自己花的时间"排序
systemd-analyze blame | head -15
systemd-analyze blame --no-pager | head -20

# 3) ⭐ 找出真正的关键路径（谁是阻塞链上的元凶）
systemd-analyze critical-chain
# graphical.target @35.421s
# └─multi-user.target @35.420s
#   └─docker.service @34.102s +1.205s
#     └─network-online.target @34.080s
#       └─NetworkManager-wait-online.service @1.978s +32.100s   ← 从第 2 秒等到第 34 秒
```

**制造一个"慢服务"来观察**：

```bash
# 写一个启动就睡 20 秒的服务，并挂在 network-online.target 之后
sudo tee /etc/systemd/system/slowdemo.service >/dev/null <<'EOF'
[Unit]
Description=Slow demo service
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/bin/sleep 20
RemainAfterExit=yes
EOF

sudo systemctl enable slowdemo.service
sudo systemctl daemon-reload      # ⭐ 改了 unit 必须 reload
```

**验证方式**：
- 重启后 `systemd-analyze blame` 的第一名变成 `slowdemo.service`，耗时 ≈ 20s；
- `systemd-analyze critical-chain` 里 `slowdemo.service` 出现在**缩进链**上（说明它阻塞了 `multi-user.target`），而不只是排在 blame 榜首。

**读 `critical-chain` 的三个要点**：

| 符号 | 含义 |
|------|------|
| 缩进 | 依赖关系（越靠右越底层，是被依赖者） |
| `@Xs` | 该 unit **开始**的时刻（从启动算起） |
| `+Ys` | 该 unit **自己**花的时间 |

> ⚠️ **`blame` 榜首 ≠ 元凶**。一个"等待型"服务（比如等 DHCP）可能耗时很长，但它**不在关键路径上**，关掉它对启动速度毫无影响。**必须看 `critical-chain`** 才能知道关哪个有用。

**其它有用的分析命令**：

```bash
systemd-analyze plot > /tmp/boot.svg          # 可视化时间线（浏览器打开）
systemd-analyze dot | dot -Tsvg > /tmp/dep.svg # 依赖图
systemd-analyze verify /etc/systemd/system/slowdemo.service
journalctl -b -o short-monotonic | head -60    # 用"启动后多少秒"显示日志时间
systemd-analyze security slowdemo.service      # 这个 unit 的加固评分（越低越好）
```

**清理**：

```bash
sudo systemctl disable --now slowdemo.service
sudo rm /etc/systemd/system/slowdemo.service
sudo systemctl daemon-reload
```

</details>

### 实验 15 · 抓包与防火墙规则（本机回环，零外网影响）

**目标**：用 `tcpdump` 抓到本机回环上的明文 HTTP，用 `nft` 观察规则与计数器；理解"包在哪一层被拦"。

<details><summary>步骤与验证</summary>

**第一部分：抓回环流量**

```bash
# 终端 A：抓 lo 上的 8000 端口（-nn 不做名称解析，-A 显示 ASCII 内容）
sudo tcpdump -i lo -nn -A 'tcp port 8000'

# 终端 B：起一个本地 HTTP 服务并发一个请求
python3 -m http.server 8000 --bind 127.0.0.1 &
curl -sS http://127.0.0.1:8000/ -o /dev/null
curl -sS -X POST http://127.0.0.1:8000/ -d 'secret=hunter2'

# 终端 A 应看到完整的三次握手 + 请求头 + 响应头，POST 的请求体也是明文
```

**验证方式**：终端 A 里能看到 `GET / HTTP/1.1`、`Host: 127.0.0.1:8000`、`POST / ...`、`secret=hunter2` —— 证明 **HTTP 明文在回环上可被本机任何有权限的用户抓到**（这就是为什么"localhost 上的明文传输"也不等于安全 🔐）。

**第二部分：nft 规则与计数器**

```bash
# 看现有规则（现代内核用 nftables）
sudo nft list ruleset

# 建一张最简表 + 链，只在 input 上放行本机回环、丢弃 8000 端口的新连接
sudo nft add table inet labdemo
sudo nft add chain inet labdemo input '{ type filter hook input priority 0; policy accept; }'
sudo nft add rule inet labdemo input iif lo accept
sudo nft add rule inet labdemo input tcp dport 8000 counter drop

# 观察命中计数
sudo nft list ruleset | sed -n '/labdemo/,$p'

# 从**另一台机器/容器**访问这台机器的 8000（应被丢弃）
#   → 客户端：Connection timed out（不是 refused！）
# 而本机访问不受影响（iif lo accept 在前）
curl -sS -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8000/
```

**验证方式**：
- `nft list ruleset` 里 `tcp dport 8000 counter drop` 的 `packets` / `bytes` **计数在增长**（每被拦一次就 +1）；
- 外部访问 `timeout`、本机访问正常 —— 印证 [`../practice/05-网络题.md`](../practice/05-网络题.md) 题 20 里"`refused` vs `timeout`"的判据。

**清理**（⚠️ 一条命令删掉整张表）：

```bash
sudo nft delete table inet labdemo
kill %1 2>/dev/null         # 关掉 python http.server
```

> ⚠️ **`nft flush ruleset` 会清掉这台机器上所有防火墙规则**。如果在远程机器上执行，且默认策略是 DROP，你会**立刻断线且回不来**。永远只在本地控制台或可回滚的虚拟机里做。
>
> 🔐 抓包得到的 pcap 里是**明文数据**（密码、Cookie、token）。按敏感文件处理：`chmod 600`，用完删掉。
>
> ⚠️ 抓包/规则实验只对**自己的机器**做。对他人网络抓包在多数司法辖区违法。

</details>

---

## 五、安全实验清单 🔐

### 5.0 清单总表（7 个安全实验）

| # | 目标 | 步骤要点 | 验证方式 |
|---|------|----------|----------|
| 1 | **建立文件完整性基线，并发现篡改** | `aideinit` 生成基线 → 手工改一个受管文件 + 造一个 SUID → `aide --check` | `aide --check` 报出被改的文件与新出现的 SUID；与 `find -perm -4000` 的结果能对上 |
| 2 | **用 `auditd` 还原"谁在什么时候改了什么"** | 对 `/etc/passwd` 加 `-w ... -p wa -k` 规则 → `useradd` 造变更 → `ausearch -k` | `ausearch -k passwd_change` 里有记录；**`auid` 字段**能指回真实登录用户（即使当时是 root） |
| 3 | **提权面审计（SUID / sudo / 可写文件 / PATH）** | 按 7 项清单逐条扫 | `find -perm -4000` 列出 SUID；`sudo -l` 显示可执行命令；可写 PATH 目录被标出 ⚠️ |
| 4 | **持久化位置全清单** | 逐项检查 cron / systemd / `authorized_keys` / shell rc / `ld.so.preload` / 内核模块 / `chattr +i` / 账号 | 每一项都有明确输出；**自己造的测试后门能被这一轮检查发现** |
| 5 | **可疑进程与网络连接排查** | 从 `/tmp` 起一个进程 + 看对外连接 | `ls -l /proc/*/exe \| grep -E '/tmp\|deleted\|memfd'` 能命中；`ss -tunap` 能列出异常外连 |
| 6 | **日志与登录痕迹分析（含篡改检测）** | 造失败登录 → `lastb`/`lastlog`/`journalctl` → 检查日志文件 mtime 与大小 | `lastb` 有失败记录；`stat` 显示 wtmp/btmp 的大小与时间；能指出"日志被清空"的特征（大小骤降但 mtime 很新） |
| 7 | **容器安全审计** | 遍历 `docker inspect` 检查 `Privileged` / `PidMode` / 挂载 `docker.sock` / `0.0.0.0` 端口 | 能列出每个容器的特权与挂载；能指出哪个容器等于"有宿主 root" 🔐 |

> ⚠️ **全部只在你自己完全控制的靶机/靶场里做。** 对未授权系统进行扫描或攻击在多数司法辖区（含中国大陆）构成违法。
>
> ⚠️ **靶机必须用 Host-only / Internal 网络**，绝不能接 Bridged 或公网。

### 安全实验 1 · 建立文件完整性基线并发现篡改

```bash
# 在干净状态建基线
sudo dnf install -y aide
sudo aideinit
sudo cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db

# 制造"篡改"（模拟攻击者改文件）
echo 'evil' | sudo tee -a /etc/profile > /dev/null
sudo cp /usr/bin/ls /usr/bin/ls.bak && sudo chmod 4755 /usr/bin/ls.bak   # 造一个 SUID

# 检测
sudo aide --check | head -40
sudo find / -xdev -type f -perm -4000 2>/dev/null | sort
sudo awk -F: '$3==0' /etc/passwd

# 恢复
sudo cp /var/lib/aide/aide.db /tmp/ 2>/dev/null
sudo rm /usr/bin/ls.bak
sudo sed -i '/evil/d' /etc/profile
```

### 安全实验 2 · auditd 记录并还原"谁改了什么" 🔐

```bash
sudo systemctl enable --now auditd

# 监控关键文件
sudo auditctl -w /etc/passwd -p wa -k passwd_change
sudo auditctl -w /etc/sudoers -p wa -k sudoers_change

# 制造变更
sudo useradd -m testuser

# 查询
sudo ausearch -k passwd_change | tail -30
sudo ausearch -m ADD_USER -ts recent
sudo aureport --auth --summary
sudo aureport -u --summary

# 关键点：看 auid（审计用户 ID）—— 即使切到 root，auid 仍是登录用户
sudo ausearch -k passwd_change -i | grep -E 'auid|uid|comm'

# 锁定规则（防止攻击者改规则）
sudo auditctl -e 2
sudo auditctl -s | grep enabled       # 应为 2
sudo auditctl -e 1                    # 解锁
```

### 安全实验 3 · 提权面审计（SUID / sudo / 可写文件）🔐

```bash
# 1. SUID / SGID
sudo find / -xdev -type f \( -perm -4000 -o -perm -2000 \) -exec ls -l {} + 2>/dev/null

# 2. 全局可写的系统文件与目录
sudo find / -xdev -type f -perm -0002 2>/dev/null | head -20
sudo find / -xdev -type d -perm -0002 ! -path '/tmp*' ! -path '/var/tmp*' 2>/dev/null

# 3. 无属主文件（可能残留了删除用户遗留的提权点）
sudo find / -xdev \( -nouser -o -nogroup \) -ls 2>/dev/null | head -20

# 4. sudo 规则里的"能执行任意程序"的授权
sudo -l
sudo grep -rE 'NOPASSWD|ALL\s*=\s*\(ALL' /etc/sudoers /etc/sudoers.d/ 2>/dev/null

# 5. 可写的 PATH 目录（PATH 劫持）
echo "$PATH" | tr ':' '\n' | while read -r d; do
  [ -w "$d" ] && echo "⚠️ 可写: $d"
done

# 6. 系统里非 root 拥有但带 SUID 的文件（最可疑）
sudo find / -xdev -type f -perm -4000 ! -user root -ls 2>/dev/null

# 7. 计划任务
sudo systemctl list-timers --all --no-pager
for u in $(cut -d: -f1 /etc/passwd); do sudo crontab -l -u "$u" 2>/dev/null; done
```

### 安全实验 4 · 持久化位置全清单 🔐

```bash
# 逐项检查（每一项都是攻击者验证过的"能活下来"的位置）
echo "=== 1. cron ==="
sudo ls -la /etc/cron.{d,daily,hourly,weekly,monthly}/ /var/spool/cron/ 2>/dev/null
sudo cat /etc/crontab 2>/dev/null

echo "=== 2. systemd units ==="
sudo find /etc/systemd /usr/lib/systemd -newermt '-30 days' -name '*.service' -o -name '*.timer' 2>/dev/null | head
systemctl list-unit-files --state=enabled --no-pager | head -30

echo "=== 3. SSH keys ==="
sudo find / -xdev -name authorized_keys -exec ls -l {} + 2>/dev/null
sudo cat /root/.ssh/authorized_keys 2>/dev/null

echo "=== 4. shell 启动文件 ==="
grep -rn 'curl\|wget\|base64\|/tmp\|/dev/shm' ~/.bashrc ~/.bash_profile ~/.profile /etc/profile /etc/profile.d/ 2>/dev/null | head -20

echo "=== 5. ld.so.preload ==="
cat /etc/ld.so.preload 2>/dev/null
echo "LD_PRELOAD=$LD_PRELOAD"

echo "=== 6. 内核模块 ==="
lsmod | head -20
sudo find /lib/modules -newermt '-30 days' -name '*.ko*' 2>/dev/null | head

echo "=== 7. 不可变文件 ==="
sudo lsattr -R /etc /tmp /var/tmp 2>/dev/null | grep -v '^----' | head -20

echo "=== 8. 账号 ==="
awk -F: '$3==0' /etc/passwd
sudo awk -F: '$2==""' /etc/shadow
getent group sudo wheel docker admin | cut -d: -f1,4
```

### 安全实验 5 · 可疑进程与网络连接排查 🔐

```bash
# 先造一个"可疑进程"（无害演示）
cp /bin/sleep /tmp/.hidden && /tmp/.hidden 600 &     # 从 /tmp 运行的进程

# 排查
echo "=== 1. 从临时目录运行的进程 ==="
sudo ls -l /proc/*/cwd 2>/dev/null | grep -E '/tmp|/dev/shm'
sudo ls -l /proc/*/exe 2>/dev/null | grep -E '/tmp|/dev/shm|deleted|memfd'

echo "=== 2. 对外连接 ==="
sudo ss -tunap state established | grep -vE '127\.0\.0\.1|\[::1\]'

echo "=== 3. 反常的参数（长命令行、编码过的） ==="
ps -eo pid,user,args | awk '{ if (length($0) > 200) print }'

echo "=== 4. 环境变量里的可疑地址 ==="
for p in $(pgrep -f .); do
  sudo tr '\0' '\n' < "/proc/$p/environ" 2>/dev/null | grep -qiE 'http://|https://|/bin/(sh|bash)' && \
    { echo "--- PID $p ---"; sudo tr '\0' '\n' < "/proc/$p/environ" | grep -iE 'http|shell'; }
done

# 清理
kill %1 2>/dev/null; rm -f /tmp/.hidden
```

### 安全实验 6 · 日志与登录痕迹分析 🔐

```bash
# 造一些失败登录
for i in $(seq 1 10); do ssh -o BatchMode=yes -o ConnectTimeout=1 nonexistent@localhost true 2>/dev/null; done

# 分析
sudo lastb -n 20                        # 失败登录（btmp）
sudo last -n 20                         # 成功登录（wtmp）
sudo lastlog | grep -v 'Never'
sudo journalctl -u sshd --since '-1 hour' | grep -iE 'failed|invalid|accepted' | tail -30
sudo grep -c 'Failed password' /var/log/secure 2>/dev/null || sudo grep -c 'Failed password' /var/log/auth.log 2>/dev/null

# ⭐ 检查日志是否被篡改（文件大小/时间是关键线索）
sudo ls -l /var/log/wtmp /var/log/btmp /var/log/lastlog
sudo stat -c '%n 大小=%s  修改=%y' /var/log/wtmp /var/log/btmp

# auditd 视角
sudo ausearch -m USER_LOGIN,USER_AUTH -ts today | tail -40
sudo aureport --auth --summary
sudo aureport --login --summary
```

### 安全实验 7 · 容器安全审计 🔐

```bash
# 审计本机容器的危险配置
docker ps -a --format '{{.Names}}' | while read -r c; do
  echo "=== $c ==="
  docker inspect "$c" --format '  Privileged={{.HostConfig.Privileged}}'
  docker inspect "$c" --format '  PidMode={{.HostConfig.PidMode}} NetworkMode={{.HostConfig.NetworkMode}}'
  docker inspect "$c" --format '  CapAdd={{.HostConfig.CapAdd}}'
  docker inspect "$c" --format '  User={{.Config.User}}'
  docker inspect "$c" --format '{{range .Mounts}}  Mount: {{.Source}} -> {{.Destination}} rw={{.RW}}{{"\n"}}{{end}}'
done

# 找挂载了 docker.sock 的容器（等于容器里有宿主 root）
docker ps -q | xargs -r docker inspect --format '{{.Name}} {{range .Mounts}}{{.Source}} {{end}}' \
  | grep 'docker.sock'

# 找对外暴露的端口
docker ps --format '{{.Names}}\t{{.Ports}}' | grep '0.0.0.0'
```

---

## 六、建立你的实验记录

每次实验后写三行（放在 `~/linux-lab/notes.md`）：

```markdown
## 2026-09-15 · 实验 1 磁盘满但 du 小
- 现象：df 显示 / 100%，du -sh /var/tmp 只 2M
- 怎么找到的：先跑 lsof +L1，看到 python 持有已删除的 ghost.log（1.2G）
- 学到的：rm 不释放空间是因为 fd 还开着；下次先 `lsof +L1` 再考虑 restart
```

**为什么必须写**：三个月后你只会记得"我做过这个实验"，不会记得"我是怎么找到的"。**排查能力体现在过程，不是结论。**

**记录的三个必备项**：

| 项 | 为什么 |
|----|--------|
| **现象** | 训练"从症状出发"而不是"凭记忆匹配" |
| **怎么找到的**（命令序列） | 这才是可复用的部分 |
| **一句话结论** | 便于回顾，也便于讲给别人 |

---

## 七、快速重置环境

**Docker**：

```bash
# 删掉练习容器
docker rm -f linux-lab systemd-lab host1 host2 sniff srv 2>/dev/null
# 删掉练习网络
docker network rm labnet
# 删掉练习镜像（可选，省空间）
docker image prune -a
# ⚠️ 想全部重置（会删掉你所有容器与镜像）
# docker system prune -a --volumes
```

**KVM / libvirt**：

```bash
# 回滚到快照（最快）
virsh snapshot-revert rocky9-lab clean

# 彻底重建
virsh destroy rocky9-lab
virsh undefine rocky9-lab --remove-all-storage
# 再跑一遍 virt-install
```

**Vagrant**：

```bash
vagrant destroy -f && vagrant up      # ⚠️ destroy 会删所有机器磁盘
```

**检查有没有留下"脏"东西**：

```bash
docker ps -a
docker volume ls
virsh list --all
ip -br link | grep -E 'virbr|docker|vbox'
ls -la /tmp/*.img /var/tmp/*.img 2>/dev/null
```

---

## 八、相关文档

| 去哪 | 说明 |
|------|------|
| [`../basics/`](../basics/) | 原理文档（做实验遇到不懂的机制时读） |
| [`../commands/README.md`](../commands/README.md) | 命令手册，按任务查 |
| [`../practice/README.md`](../practice/README.md) | 练习题库（155 题）+ **第 4.1 节是一键造沙盒脚本的权威版本** |
| [`../practice/README.md#41-一键造沙盒`](../practice/README.md#41-一键造沙盒) | 直接跳转到沙盒脚本 |
| [`../practice/06-综合场景题.md`](../practice/06-综合场景题.md) | 本目录大部分排障实验的"标准答案"（15 个场景） |
| [`../practice/05-网络题.md`](../practice/05-网络题.md) | 实验 9 / 实验 15 的配套习题（含题 20 分层排障） |
| [`../commands/14-容器与虚拟化.md`](../commands/14-容器与虚拟化.md) | 容器/虚拟机命令细节与安全风险 |
| [`../commands/12-安全与审计.md`](../commands/12-安全与审计.md) | 第 5 节安全实验用到的命令细节（auditd / aide / SELinux） |
| [`../../kali/`](../../kali/) | Kali 模块的靶场搭建（DVWA / Juice Shop / Metasploitable 等） |
| [`../README.md`](../README.md) | 回到 Linux 模块总纲 |
