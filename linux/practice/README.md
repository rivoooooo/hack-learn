# Linux 练习题库 · 使用说明

本目录是 [`../commands/`](../commands/README.md) 的**配套练习**。命令手册解决「这个命令怎么写」，练习解决「遇到问题我能不能想起来用它」。

所有题目遵循同一个结构：

```
真实场景描述  →  准备数据（可复制执行）  →  你的解法  →  参考答案  →  解析
```

> 前置：[`../basics/`](../basics/) 的概念文档。没看过概念直接刷题，容易变成背命令。
> 返回：[`../README.md`](../README.md) 学习路线。

---

## 1. 怎么用

### 推荐的循环

```bash
# ① 造沙盒（只需一次，之后所有题都能直接做）
bash /tmp/linux-practice-setup.sh      # 脚本内容见下面「环境准备」

# ② 进沙盒
cd /tmp/linux-practice

# ③ 看题，先自己写答案，不要点开折叠块

# ④ 自己验证结果对不对（这一步最重要，别跳过）
wc -l result.txt          # 行数对不对
md5sum result.txt         # 和预期哈希是否一致
diff mine.txt answer.txt  # 逐行比对

# ⑤ 再看参考答案，重点对比「思路差异」，不是只看对不对
```

### 三条建议

| 建议 | 原因 |
|------|------|
| **先做后看** | 折叠块里的参考答案一旦看了，这道题就废了 |
| **错了要查** | 答错说明概念有洞，回 `../basics/` 对应章节补，别背答案 |
| **动手改参数** | 把答案里的 `-n1` 改成 `-n2`、把 `-w` 去掉，看输出怎么变，比读十遍文档有用 |

### 怎么判断自己做对了

不要「看着差不多」就算过。用可验证的标准：

```bash
# 1) 比行数
wc -l < 我的输出.txt

# 2) 比哈希（顺序敏感）
md5sum 我的输出.txt

# 3) 比排序后的内容（顺序无关）
sort 我的输出.txt | md5sum
diff <(sort 我的输出.txt) <(sort 标准答案.txt)

# 4) 答案不确定时，换个思路算第二遍，两个结果一致才可信
```

💡 **一题多解是常态**。`awk`/`sed`/`cut` 能互相替代，参考答案给的是「可读性 + 稳妥」的写法，不是唯一解。只要输出一致就是对的。

---

## 2. 难度分级

| 标记 | 含义 | 大概需要 |
|------|------|----------|
| ⭐ | 入门：单个命令、单个选项 | 记住基本语法即可 |
| ⭐⭐ | 熟练：命令组合、选项搭配、管道 2 段以上 | 理解命令的输入输出模型 |
| ⭐⭐⭐ | 进阶：需要先分析再构造、涉及系统原理或多步排查 | 读过 `../basics/` 全部 8 篇 |

其它标记沿用全库约定：

| 标记 | 含义 |
|------|------|
| ⚠️ | **危险操作**，条目标题下会说明后果与安全复现方式 |
| 🔐 | 安全 / 取证 / 提权排查方向 |
| 💡 | 提效技巧 |
| 📦 | 需要额外安装软件包（题里会给出安装命令） |

### ⚠️ 安全红线

题面标 ⚠️ 的命令**只允许在 `/tmp/linux-practice` 或 `~/demo` 里执行**。以下命令在真实系统上会造成不可逆后果：

| 命令 | 后果 |
|------|------|
| `rm -rf 目录` | 目录内容永久消失，不进回收站 |
| `: > 文件` / `truncate -s 0 文件` | 文件内容立即清零，无法撤销 |
| `dd if=/dev/zero of=/dev/sdX` | 整块磁盘数据被覆盖，系统与数据全毁 |
| `mkfs.*` | 格式化分区，原文件系统元数据被重建 |
| `chmod -R 777 /` | 全系统权限失控，SSH 等会直接拒绝工作 |
| `chown -R` 写错路径 | 系统文件属主错乱，服务大面积启动失败 |
| `iptables -F` / `nft flush ruleset` | 清空防火墙规则；远程操作会当场断连 |
| `kill -9 1` | 杀不掉，但会试图杀 init，触发内核 panic 风险 |
| `chmod 000` 目录 | 自己也会被关在门外（root 除外） |

**练习原则**：破坏性操作一律先 `cp -a` 一份到 `/tmp/linux-practice/backup/`，再动手。

---

## 3. 题库索引

| 文件 | 题量 | 覆盖知识点 | 主要难度 |
|------|------|-----------|----------|
| [`01-基础题.md`](01-基础题.md) | 30 | `pwd`/`cd`/`ls -la`/`realpath`、`cp -a`/`mv`/`rm`/`mkdir -p`/`touch`/`ln`、`cat`/`less`/`head`/`tail -f`、通配符与引号、`alias`/`history`、`man`/`apropos` | ⭐–⭐⭐ |
| [`02-文本处理题.md`](02-文本处理题.md) | 25 | `grep` 正则与 `-r/-v/-c/-o/-E/-A/-B`、`sed` 替换删除行范围与 `-i` 备份、`awk` 字段条件统计、`cut`/`sort`/`uniq -c`/`tr`/`wc`、日志分析管道 | ⭐–⭐⭐⭐ |
| [`03-权限与用户题.md`](03-权限与用户题.md) | 20 | `chmod` 符号/数字/粘滞位、`chown`/`chgrp`、`umask`、SUID/SGID 查找、`setfacl`/`getfacl`、`sudo`/`visudo`、`useradd`/`usermod`/`passwd`、`id`/`who`/`w`/`last`（含 🔐 4 题） | ⭐–⭐⭐⭐ |
| [`04-进程与系统题.md`](04-进程与系统题.md) | 20 | `ps aux`/`-ef`/`--sort`/`-o`、`top`、`pgrep`/`pkill`/`kill` 信号、`jobs`/`bg`/`fg`/`nohup`/`disown`、`nice`/`renice`、`lsof` 找端口占用、`strace` 入门、`systemctl`/`journalctl` | ⭐–⭐⭐⭐ |
| [`05-网络题.md`](05-网络题.md) | 20 | `ip addr/route/link`、`ss -tulnp`、`ping`/`traceroute`/`mtr`、`dig`/`nslookup`/`host`、`curl`/`wget`、`nc`、`tcpdump`、`nft`/`iptables`（含 🔐 5 题） | ⭐–⭐⭐⭐ |
| [`06-综合场景题.md`](06-综合场景题.md) | 15 | 磁盘满、SSH 连不上、load 高 CPU 低、`203/EXEC`、cron 环境、OOM、入侵取证、误删文件抢救、403 权限、时间错乱、批量权限事故、I/O 错误 D 状态、journald 占满磁盘、容器 `CrashLoopBackOff`、多服务资源争抢 | ⭐⭐⭐ |
| [`07-速查挑战.md`](07-速查挑战.md) | 25 | 「用一条命令完成 X」，覆盖 `find`/`awk`/`sed`/`sort`/`tar`/`ps`/`ss` 的高频组合 | ⭐⭐–⭐⭐⭐ |

**合计 155 题。**

建议顺序：`01 → 02 → 03 → 04 → 05 → 06 → 07`。`06` 和 `07` 是综合应用，前面的题没做完直接上会很难受。

---

## 4. 环境准备

### 4.1 一键造沙盒

把下面整段复制到终端执行（或存成 `/tmp/linux-practice-setup.sh` 再 `bash` 它）。它会在 `/tmp/linux-practice` 下造出一整套练习数据，**本目录所有题目都能直接做**。

```bash
#!/usr/bin/env bash
# 一键造出 Linux 练习沙盒：/tmp/linux-practice
# 用法：bash linux-practice-setup.sh
set -e

ROOT=/tmp/linux-practice
rm -rf "$ROOT"
mkdir -p "$ROOT"/{projects/{src,docs,logs},data,backup,shared,secret,archive/old,bin,"my dir"}

# 1) 1000 行 Nginx 风格访问日志（含 IP / 路径 / 状态码 / 字节数）
python3 - <<'PY'
import random
random.seed(42)
ips   = ["10.0.0.11","10.0.0.12","10.0.0.13","192.168.1.5",
         "192.168.1.7","203.0.113.9","203.0.113.10"]
paths = ["/index.html","/login","/api/v1/user","/static/app.js",
         "/admin","/images/logo.png","/api/v1/order","/health"]
methods = ["GET"]*7 + ["POST"]*3
codes   = ["200"]*12 + ["404"]*4 + ["500","403","301"]
lines = []
for i in range(1, 1001):
    # ⚠️ 取随机数的【顺序】决定了最终数据。必须按 ip → 路径 → 方法 → 状态码 → 字节数 依次取，
    #    这样才能和 02-文本处理题.md 里写的预期输出（404=231、200=607…）逐位对上。
    ip  = random.choice(ips)
    pa  = random.choice(paths)
    me  = random.choice(methods)
    co  = random.choice(codes)
    sz  = random.randint(120, 98000)
    lines.append('{ip} - - [15/Sep/2026:{h:02d}:{m:02d}:{s:02d} +0800] '
                 '"{me} {pa} HTTP/1.1" {co} {sz}'.format(
        ip=ip, h=i % 24, m=(i*7) % 60, s=(i*13) % 60,
        me=me, pa=pa, co=co, sz=sz))
open("/tmp/linux-practice/data/access.log","w").write("\n".join(lines)+"\n")
PY

# 2) 结构化数据
cat > "$ROOT/data/sales.csv" <<'EOF'
id,name,dept,amount,date
1,Alice,研发,1200.50,2026-01-03
2,Bob,运维,880.00,2026-01-03
3,Carol,研发,1500.75,2026-01-04
4,Dave,市场,300.25,2026-01-04
5,Eve,运维,2200.00,2026-01-05
6,Frank,研发,450.10,2026-01-05
7,Grace,市场,990.90,2026-01-06
8,Heidi,运维,1780.00,2026-01-06
EOF
printf 'apple 30\nbanana 12\napple 5\ncherry 100\nbanana 8\napple 2\n' > "$ROOT/data/fruit.txt"
printf 'name,size\nreport.pdf,2048\nphoto.jpg,4096\nnotes.txt,12\n'   > "$ROOT/data/files.csv"

# 3) 含空格 / 中文 / 特殊字符的文件名（练转义与引号）
echo "hello world"  > "$ROOT/my dir/hello world.txt"
echo "中文内容 test" > "$ROOT/my dir/中文文件.txt"
echo 'a*b?c'        > "$ROOT/data/特殊*字符.txt"

# 4) 配置文件（app.conf.new 是它的「改后版本」，用于 diff/sed）
cat > "$ROOT/projects/src/app.conf" <<'EOF'
# app config
listen = 0.0.0.0
port   = 8080
debug  = true
workers = 4
log_level = info
EOF
sed -e 's/8080/8081/' -e 's/debug  = true/debug  = false/' \
    "$ROOT/projects/src/app.conf" > "$ROOT/projects/src/app.conf.new"

# 5) 硬链接 / 软链接 / 断链
echo "target content" > "$ROOT/data/original.txt"
ln    "$ROOT/data/original.txt" "$ROOT/data/hardlink.txt"
ln -s "$ROOT/data/original.txt" "$ROOT/data/softlink.txt"
ln -s /nonexistent/path         "$ROOT/data/broken_link"
ln -sf "$ROOT/projects/logs/app.log" "$ROOT/data/current.log"

# 6) 权限异常样本（练 find -perm 审计）
printf '#!/bin/bash\necho pwned\n' > "$ROOT/bin/suid-demo"
chmod 4755 "$ROOT/bin/suid-demo"          # SUID 可执行
echo "top secret" > "$ROOT/secret/readme.txt"
chmod 666 "$ROOT/secret/readme.txt"       # 所有人可写
echo "world writable dir" > "$ROOT/shared/open.txt"
chmod 777 "$ROOT/shared"                  # 所有人可写目录

# 7) 大文件（练 du / find -size / ls -S）
truncate -s 5M "$ROOT/data/big5M.bin"
head -c 150000 /dev/urandom | base64 > "$ROOT/archive/big-text.txt"

# 8) 2000 行应用日志（练 grep -c / journalctl 类比）
python3 - <<'PY'
with open("/tmp/linux-practice/projects/logs/app.log","w") as f:
    for i in range(1, 2001):
        lvl = "ERROR" if i % 50 == 0 else ("WARN" if i % 10 == 0 else "INFO")
        f.write(f"2026-09-15 10:{i%60:02d}:{(i*3)%60:02d} [{lvl}] "
                f"worker-{i%4} request={i} msg=processing item {i}\n")
PY

# 9) 二进制样本（练 file / strings / sha256sum）
cp /bin/ls "$ROOT/bin/ls-copy"

# 10) 不同修改时间的归档源（练 find -mtime / -newermt）
for i in 1 2 3; do echo "old file $i" > "$ROOT/archive/old/f$i.txt"; done
touch -d '30 days ago' "$ROOT/archive/old/f1.txt"
touch -d '10 days ago' "$ROOT/archive/old/f2.txt"

# 11) 备份样本（与 sales.csv 内容完全相同，用于练 diff / md5sum）
cp "$ROOT/data/sales.csv" "$ROOT/backup/sales.csv.bak"

echo "✅ 沙盒已生成：$ROOT"
find "$ROOT" -maxdepth 2 | sort
```

### 4.2 沙盒里有什么

```
/tmp/linux-practice/
├── data/
│   ├── access.log        1000 行访问日志（IP/路径/状态码/字节）
│   ├── sales.csv         8 行 CSV（id,name,dept,amount,date）
│   ├── fruit.txt         "名称 数量" 两列，含重复项
│   ├── files.csv         name,size
│   ├── original.txt      ← hardlink.txt 与 softlink.txt 的源
│   ├── hardlink.txt      与 original.txt 同一 inode
│   ├── softlink.txt      符号链接 → original.txt
│   ├── current.log       符号链接 → ../projects/logs/app.log
│   ├── broken_link       断链（指向 /nonexistent/path）
│   ├── big5M.bin         5 MiB 空洞文件
│   └── 特殊*字符.txt      文件名含 glob 字符
├── projects/
│   ├── src/app.conf      + app.conf.new（改后版本）
│   ├── logs/app.log      2000 行日志（INFO/WARN/ERROR）
│   └── docs/             空目录
├── archive/
│   ├── old/f1.txt        30 天前修改
│   ├── old/f2.txt        10 天前修改
│   ├── old/f3.txt        刚创建
│   └── big-text.txt
├── backup/sales.csv.bak  与 data/sales.csv 内容相同
├── bin/
│   ├── suid-demo         4755 可执行（无实际提权能力）
│   └── ls-copy           /bin/ls 的副本
├── shared/               777 目录
├── secret/readme.txt     666 文件
└── my dir/
    ├── hello world.txt   名含空格
    └── 中文文件.txt       中文名
```

### 4.3 需要真实 root 的题目怎么办

本目录里标注了「环境限制」的题（涉及 `useradd`、`chown`、`sudoers`、`iptables`、`tcpdump`、`mount` 等）需要 root 或额外软件包。两种做法：

```bash
# 方式一：用容器，随便折腾不心疼
docker run --rm -it debian:stable bash

# 方式二：本机装缺的软件包（按发行版选一行）
sudo apt install lsof tcpdump netcat-openbsd dnsutils strace mtr-tiny   # Debian/Ubuntu
sudo pacman -S lsof tcpdump openbsd-netcat bind strace mtr              # Arch
sudo dnf install lsof tcpdump nc bind-utils strace mtr                  # RHEL 系
```

装不了也没关系：这些题都给了**同等效果的替代命令**（例如用 `/proc/PID/fd` 代替 `lsof`、用 `bash /dev/tcp` 代替 `nc`、用 `getent hosts` 代替 `dig`）。

### 4.4 网络练习的范围限制

[`05-网络题.md`](05-网络题.md) 全部围绕 `127.0.0.1`、本机服务（如 `python3 -m http.server`）与 RFC 5737 文档用网段（`192.0.2.0/24`）展开。

**不要**对本机以外的主机做端口扫描、抓包、泛洪或 DNS 查询。扫描他人主机在绝大多数司法辖区违法，也会触发 IDS 告警。

---

## 5. 常见问题

| 问题 | 原因 / 解法 |
|------|-------------|
| `Permission denied` 但我是文件属主 | 目录缺 `x` 位，看目录权限不是文件权限 |
| `rm` 提示 `Argument list too long` | 用 `find ... -delete` 或 `find ... -print0 \| xargs -0 rm` |
| `grep` 找不到明明存在的字符串 | 二进制文件被跳过（加 `-a`）、或正则里有未转义的 `.`/`*` |
| `awk` 统计结果是整数丢了小数 | `printf "%.2f"` 才保留小数位 |
| `sort` 后 `uniq -c` 计数是散的 | `uniq` 只合并**相邻**重复行，必须先 `sort` |
| 时间类输出和 `ls` 对不上 | `find -mtime` 以 24 小时为单位、按**整数天**截断，不是精确时刻；用 `-newermt` 更准 |
| 沙盒被我玩坏了 | 重新跑 4.1 的脚本即可，它会 `rm -rf` 重建 |

---

## 相关

- [`../README.md`](../README.md) — Linux 模块学习路线（三条路线 + 检查清单）
- [`../basics/`](../basics/) — 8 篇概念文档，做题卡住先看这里
- [`../commands/README.md`](../commands/README.md) — 330 个命令手册总索引 + 按任务速查
- [`../labs/README.md`](../labs/README.md) — 虚拟机 / 容器实验环境
- [`../../kali/tools/tutorials/`](../../kali/tools/tutorials/) — 渗透测试实操教程
