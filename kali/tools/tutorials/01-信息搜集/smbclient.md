# smbclient（SMB/CIFS 共享访问客户端）

> **一句话**：像用 FTP 一样连上 Windows / Samba 共享——列目录、下载、上传，甚至整站打 tar 包。
> **分类**：信息搜集 ｜ **Kali 包**：`smbclient`（Samba 套件的客户端组件，Kali 中由 `samba` / `smbclient` 包提供） ｜ **官方文档**：<https://www.samba.org/>

## 1. 它解决什么问题

前面用 [enum4linux](enum4linux.md) 或 [nmap](nmap.md) 的 `smb-enum-shares` 找到了共享列表。接下来要回答的是：**里面有什么？我能读吗？能写吗？**

`smbclient` 就是干这个的——它是 Samba 套件里的**交互式客户端**，接口和 `ftp` 几乎一样：

```text
smbclient //server/share -U user
smb: \> ls
smb: \> get secrets.txt
smb: \> put payload.bin
```

| 工具 | 定位 |
|------|------|
| **smbclient** | 交互式共享访问、文件上下传、tar 打包、打印队列操作 |
| [enum4linux](enum4linux.md) | 一次性枚举用户/共享/组/口令策略（**会调用 smbclient**） |
| `rpcclient` | 直接发 RPC 调用，做枚举和特定操作 |
| `impacket-smbclient` / `impacket-smbexec` | Python 实现，脚本化与利用更方便 |
| `mount -t cifs` | 把共享挂载成文件系统，适合大量文件操作 |
| `smbmap`（非 Kali 默认） | 自动化列出每个共享的读写权限 |

**核心价值**：smbclient 是"验证"环节的工具——枚举工具告诉你"应该能读"，smbclient 告诉你"确实能读，而且里面有这些文件"。

## 2. 工作原理

```text
   smbclient //192.168.56.101/tmp -N
        │
   ┌────┴───────────────────────────────────────────────┐
   │ ① 名字解析：把 server 名解析成 IP                    │
   │    （-I 直接指定 IP；-R 指定解析顺序）               │
   │ ② 建立 SMB 会话：Negotiate → Session Setup          │
   │    协议版本由 -m 控制（默认取最高，如 SMB3）          │
   │    认证方式：NTLM / Kerberos / 匿名（-N）             │
   │ ③ Tree Connect：连到指定共享                        │
   └────┬───────────────────────────────────────────────┘
        │
   ┌────┴───────────────────────────────────────────────┐
   │ 进入 ftp 风格的交互 Shell                            │
   │   ls / dir        列目录                            │
   │   cd              切换目录                          │
   │   get / mget      下载                              │
   │   put / mput      上传                              │
   │   del / rm        删除                              │
   │   mkdir / rmdir   建/删目录                         │
   │   tar c/x         整目录打包/解包                    │
   │   ...（见第 4 节命令表）                             │
   └────┬───────────────────────────────────────────────┘
        │
   退出：quit / exit，或 Ctrl-D
```

关键机制：

- **服务名格式**：`//server/service`。`server` 是 **NetBIOS 名**，不一定等于 DNS 主机名——这也是为什么 `-I` 指定 IP 很常用。
- **`-L` 是"列共享"而非"进共享"**：`smbclient -L host` 打印共享列表后立即退出，不进入交互。
- **`-N` 抑制口令提示**：匿名访问。注意 man page 特别提醒——**即使服务不需要口令，如果既没给口令也没加 `-N`，客户端也会提示输入口令**（直接回车给空口令）。
- **`-c` 批处理**：把交互命令写在命令行里，适合脚本化（如 `-c "ls;get file;exit"`）。
- **`-T` tar 模式**：可以直接把整个共享打包成本地 tar，不需要先挂载。
- **`--pw-nt-hash`**：用 NT 哈希代替明文口令做认证——这是**传递哈希（Pass-the-Hash）**的经典用法之一（Kali 里还有专门的 `pth-smbclient`）。

## 3. 安装与快速上手

```bash
sudo apt install smbclient
smbclient --version
smbclient --help | head -30
```

最小可用命令：

```bash
# 1) 列出目标上的共享
smbclient -N -L //192.168.56.101

# 2) 匿名进入某个共享，然后 ls
smbclient -N //192.168.56.101/tmp
#  smb: \> ls

# 3) 用凭据访问
smbclient //192.168.56.101/share -U 'user%Password123'
```

## 4. 核心参数详解

### 连接与目标

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `//server/service` | 服务名（位置参数） | server 是 NetBIOS 名 |
| `-I, --ip-address=IP` | 直接指定目标 IP，忽略名字解析 | **NBT 名和 DNS 名不一致时必用** |
| `-p, --port=PORT` | 目标端口（默认 139） | 现代系统常用 445：`-p 445` |
| `-m, --max-protocol=PROTO` | 最高 SMB 协议：`SMB3`（默认）/`SMB2`/`NT1` | 连老设备用 `NT1`（SMB1）；连启用了加密的 Win2012+ 需 `SMB3` |
| `-R, --name-resolve=ORDER` | 名字解析顺序 | 排查"连不上" |
| `-n, --netbiosname=NAME` | 本端 NetBIOS 名 | 少见 |
| `--netbios-scope=SCOPE` | NetBIOS 作用域 | 少见 |
| `-W, --workgroup=WG` | 指定工作组/域 | 与 `-U` 搭配 |
| `--realm=REALM` | Kerberos 域 | Kerberos 认证时 |
| `-t, --timeout=SEC` | 每个 SMB 请求超时（默认 20 秒） | 超时时调大 |
| `-E, --stderr` | 消息写 stderr 而非 stdout | 脚本里想把数据与提示分开 |
| `-B, --browse` | 用 DNS 浏览 SMB 服务器 | — |
| `-b, --send-buffer=BYTES` | 收发缓冲区（0=用服务器建议值，最大 16776960） | 一般用默认（0）最快 |

### 认证

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-U, --user=[DOMAIN/]USERNAME[%PASSWORD]` | 用户名，可用 `%` 附口令 | **推荐 `-U 'DOMAIN/user%pass'`** |
| `-N, --no-pass` | 不提示口令（匿名） | 探测匿名访问 |
| `--password=STRING` | 单独给口令 | 不想写在 `-U` 里时 |
| `--pw-nt-hash` | 口令参数按 NT 哈希解析 | **传递哈希**场景 |
| `-A, --authentication-file=FILE` | 从文件读凭据 | 避免口令出现在命令行/历史里 |
| `-P, --machine-pass` | 用本机机器账户 | 域内机器账户利用 |
| `--use-kerberos=desired\|required\|off` | Kerberos 认证策略 | 域环境 |
| `--use-krb5-ccache=CCACHE` | 用 Kerberos 票据缓存 | 拿到票据后免密访问 |
| `--use-winbind-ccache` | 用 winbind 的 ccache | — |
| `--simple-bind-dn=DN` | 简单绑定 DN | LDAP 场景 |
| `--client-protection=sign\|encrypt\|off` | SMB 签名/加密策略 | 需要强制签名时用 `sign` |

### 列表与批处理

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-L, --list=HOST` | 列出主机上的共享后退出 | 最常用 |
| `-g, --grepable` | 与 `-L` 配合，输出便于 grep/cut 解析 | **脚本化必用** |
| `-c, --command=STRING` | 执行分号分隔的命令后退出 | 非交互式自动化 |
| `-D, --directory=DIR` | 起始目录（与 `-T` 配合） | tar 备份/恢复时 |
| `-T, --tar=<c\|x>IXFvgbNan` | tar 模式（详见下） | 整共享打包 |
| `-M, --message=HOST` | 用 WinPopup 协议发消息 | 历史用法 |
| `-q, --quiet` | 静默 | 脚本化 |
| `-d, --debuglevel=LEVEL` | 调试等级 | 排错（`-d 3`、`-d 10`） |
| `-s, --configfile=FILE` | 指定 smb.conf | 少见 |
| `--option=name=value` | 覆盖 smb.conf 参数 | 临时调整行为 |
| `-V, --version` / `-?`/`--usage`/`--help` | 版本/帮助 | — |

**`-T` tar 的次级标志**：

| 标志 | 含义 |
|------|------|
| `c` | 创建归档到本地（后接 tar 文件名、设备或 `-` 表示 stdout）；与 `x` 互斥 |
| `x` | 从本地 tar 恢复到共享；与 `c` 互斥 |
| `n` | 与 `c` 连用：只做 dry-run，不真正写文件 |
| `I` | 包含指定文件/目录（指定文件名时的默认行为） |
| `X` | 排除指定文件/目录 |
| `F` | 后接一个文件，文件里列出要包含的文件/目录 |
| `b` | 块大小（`blocksize*512` 字节） |
| `g` | 增量：只备份设置了 archive 位的文件（仅 `c`） |
| `v` | 详细输出 |
| `r` | 使用通配符匹配（已废弃） |
| `N` | 只备份比指定文件更新的文件（仅 `c`） |
| `a` | 备份后重置 archive 位（与 `g`、`c` 配合） |

> 注意：用 `-T` 输出到 stdout（`-`）时必须设 `-d0`，否则日志会污染 tar 文件。

### 交互模式命令

| 命令 | 作用 |
|------|------|
| `ls <mask>` / `dir <mask>` | 列目录（支持通配符） |
| `cd <dir>` / `lcd [dir]` | 切换远程目录 / 本地目录 |
| `pwd` | 显示远程当前目录 |
| `get <remote> [local]` | 下载单个文件 |
| `mget <mask>` | 批量下载 |
| `put <local> [remote]` | 上传单个文件 |
| `mput <mask>` | 批量上传 |
| `del <mask>` / `rm <mask>` | 删除文件 |
| `mkdir` / `md` / `rmdir` / `rd` | 建/删目录 |
| `deltree <mask>` | 递归删除目录 |
| `rename <old> <new> [-f]` | 重命名 |
| `chmod <file> <octal>` / `chown <file> <uid> <gid>` | 权限/属主（需服务器支持） |
| `stat <file>` | 文件属性 |
| `allinfo <file>` | 所有属性信息 |
| `du <filename>` | 磁盘使用 |
| `more <file>` / `less` | 查看文件内容 |
| `tar <c\|x>[IXbgNa]` | 交互式 tar |
| `mask <mask>` | 设置递归操作的通配符 |
| `recurse ON\|OFF` | 开关递归（配 `mget`/`mput` 用） |
| `prompt ON\|OFF` | 开关批量操作的逐项确认 |
| `lcd` / `!<cmd>` | 本地目录 / 执行本地命令 |
| `timeout <sec>` | 设置操作超时 |
| `iosize <bytes>` | 设置 IO 缓冲区 |
| `print <file>` / `queue` / `cancel <jobid>` | 打印相关 |
| `help [cmd]` | 帮助 |
| `quit` / `exit` | 退出 |

## 5. 实战演练

**环境**：本地实验室。

- 靶机 A：Metasploitable2（`192.168.56.101`），有匿名可写的 `tmp` 共享，非常适合练习。
- 靶机 B（可选）：一台配置了域账号的 Windows 实验虚拟机。
- 攻击机：Kali（`192.168.56.10`）。

> 只在授权环境操作。对他人的共享做写入、删除属于破坏性行为。

### 场景 1：列出共享（先看有什么）

```bash
smbclient -N -L //192.168.56.101
```

预期输出片段：

```text
	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	tmp             Disk      oh noes!
	opt             Disk
	IPC$            IPC       IPC Service (metasploitable server (Samba 3.0.20-Debian))
	ADMIN$          IPC       IPC Service (metasploitable server (Samba 3.0.20-Debian))

	Server               Comment
	---------            -------
	METASPLOITABLE       metasploitable server (Samba 3.0.20-Debian)

	Workgroup            Master
	---------            -------
	WORKGROUP            METASPLOITABLE
```

解读：`-N` 匿名 + `-L` 列表，这是 SMB 侦察的第一步。`tmp` 的注释 `oh noes!` 是 Metasploitable2 的彩蛋。`ADMIN$`/`IPC$` 以 `$` 结尾属于**隐藏共享**——用 `-L` 能看到，但 `net view` 之类看不到。

**脚本友好版本**：

```bash
smbclient -N -L //192.168.56.101 -g | grep -i 'Disk' | cut -d'|' -f2
```

预期输出：

```text
print$
tmp
opt
```

### 场景 2：匿名进入共享并下载文件

```bash
smbclient -N //192.168.56.101/tmp
```

```text
smb: \> ls
  .                                   D        0  Mon May 20 10:00:00 2024
  ..                                  D        0  Mon May 20 10:00:00 2024
  9999.jsvc_up                        A        0  Mon May 20 10:00:00 2024

		12970256 blocks of size 1024. 6323260 blocks available

smb: \> get 9999.jsvc_up
getting file \9999.jsvc_up of size 0 as 9999.jsvc_up (0.0 KiloBytes/sec)
smb: \> quit
```

用 `-c` 一行完成：

```bash
smbclient -N //192.168.56.101/tmp -c "ls; get 9999.jsvc_up; exit"
```

解读：`-c` 把交互命令串成一行，是最常用的自动化形式。`A` 表示普通文件（archive 属性），`D` 表示目录。**匿名可读 = 信息泄露；匿名可写 = 高危**。

### 场景 3：用凭据访问 + 递归批量下载

```bash
# 用 域/用户%口令 的形式
smbclient //192.168.56.101/opt -U 'WORKGROUP/user%Password123'
```

```text
smb: \> recurse ON
smb: \> prompt OFF
smb: \> ls
smb: \> mget *
smb: \> quit
```

解读：
- `recurse ON` 让 `mget`/`mput` 递归子目录。
- `prompt OFF` 关闭每个文件的确认提示（否则会一个个问 Y/N）。
- 这是"把整个共享拖到本地"的标准组合，做数据收集时非常常用。

**注意**：口令写在命令行会进入 shell history 和进程列表。更安全的做法是：

```bash
# 用认证文件（-A），文件权限设为 600
cat > /tmp/cred <<'EOF'
username = user
password = Password123
domain = WORKGROUP
EOF
chmod 600 /tmp/cred
smbclient //192.168.56.101/opt -A /tmp/cred
```

### 场景 4（进阶）：tar 整共享打包 + 传递哈希

```bash
# 把整个共享打包成一个本地 tar（不经过挂载）
smbclient //192.168.56.101/tmp -N -Tc backup_tmp.tar
tar tf backup_tmp.tar | head

# 只打包某个子目录
smbclient //192.168.56.101/opt -N -Tc opt_users.tar users/docs

# 恢复（-TX 排除指定目录）
# smbclient //host/share "" -N -TXx restore.tar users/docs

# 传递哈希：用 NT 哈希代替口令（授权测试场景）
smbclient //192.168.56.101/share -U 'user' --pw-nt-hash \
  'aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0'
```

解读：
- `-Tc` 的 `c` 是"创建归档"，输出到 `backup_tmp.tar`。**这是绕过挂载、快速取走大量数据的高效方式**。
- `--pw-nt-hash` 是**传递哈希**（Pass-the-Hash）的入口。Kali 里还有 `pth-smbclient`（来自 `passing-the-hash` 包）专门做这件事——这也说明**为什么 Windows 侧必须禁止 NTLM、启用 SMB 签名**。

### 场景 5：协议版本与排错式连接

```bash
# 老设备只支持 SMB1
smbclient -N -L //192.168.56.101 -m NT1

# 指定 445 端口
smbclient -N -L //192.168.56.101 -p 445

# 名字解析失败时直接给 IP
smbclient -N -L //192.168.56.101 -I 192.168.56.101

# 打开调试看握手细节
smbclient -N -L //192.168.56.101 -d 3
```

解读：遇到 `NT_STATUS_...` 之类错误时，`-d 3`（或更高）会打印协议握手细节，能快速判断是"认证失败"、"协议不匹配"还是"网络不可达"。

## 6. 输出解读

### `-L` 共享列表

| 字段 | 含义 | 下一步 |
|------|------|--------|
| `Sharename` | 共享名，`$` 结尾为隐藏共享 | 隐藏共享往往是管理/备份用途，优先关注 |
| `Type: Disk` | 磁盘共享 | 可读写的目标 |
| `Type: IPC` | 进程间通信（`IPC$`、`ADMIN$`） | 不能直接列文件，但可用于 RPC |
| `Type: Printer` | 打印共享 | 打印队列信息 |
| `Comment` | 注释 | 有时直接泄露用途（如 `backup`、`hr files`） |
| `Workgroup` / `Master` | 工作组与主浏览器 | 域环境线索 |

### 交互 `ls` 输出

| 列 | 含义 |
|----|------|
| `D` / `A` | 目录（Directory）/ 归档属性（Archive） |
| 大小 | 字节数 |
| 时间 | 修改时间 |
| `blocks of size 1024` | 该共享所在卷的剩余空间统计 |

### 常见 `NT_STATUS` 与含义

| 状态码 | 含义 | 应对 |
|--------|------|------|
| `NT_STATUS_ACCESS_DENIED` | 权限不足 | 换账号；检查共享 ACL |
| `NT_STATUS_LOGON_FAILURE` | 凭据错误 | 核对 `-U` 格式（`DOMAIN/user%pass`） |
| `NT_STATUS_BAD_NETWORK_NAME` | 共享名不存在 | `-L` 重新确认共享名 |
| `NT_STATUS_CONNECTION_REFUSED` | 端口未开放 | 试 `-p 445`；确认 139/445 是否可达 |
| `NT_STATUS_IO_TIMEOUT` | 超时 | `-t 60` 加大超时 |
| `NT_STATUS_INVALID_PARAMETER` + 协议相关 | 协议版本不匹配 | `-m NT1` 或 `-m SMB3` |
| `session setup failed: NT_STATUS_...` | 会话建立失败 | 加 `-d 3` 看细节 |

## 7. 与其他工具配合

```bash
# 1) nmap 找 445 -> smbclient 列共享 -> 逐个共享看内容
sudo nmap -p139,445 --open -oG - 192.168.56.0/24 | awk '/445\/open/{print $2}' > smb_hosts.txt
while read ip; do
  echo "===== $ip ====="
  smbclient -N -L "//$ip" -g 2>/dev/null | grep -i 'Disk' | cut -d'|' -f2 | while read sh; do
    echo "--- $sh ---"
    smbclient -N "//$ip/$sh" -c "ls" 2>/dev/null | head -5
  done
done < smb_hosts.txt

# 2) enum4linux 枚举 -> smbclient 验证
enum4linux -S 192.168.56.101 | grep -i disk
smbclient -N //192.168.56.101/tmp -c "ls"

# 3) smbclient 下载 -> 本地分析
smbclient //192.168.56.101/opt -N -Tc opt.tar
mkdir opt && tar xf opt.tar -C opt/
grep -rin "password\|secret\|key" opt/ 2>/dev/null | head -20

# 4) smbclient -> rpcclient（需要 RPC 时）
rpcclient -N -U '' 192.168.56.101 -c "enumdomusers"
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| 提示要输入口令（明明匿名可访问） | 没给口令也没加 `-N` | 加 `-N`，或在口令提示处直接回车 |
| `protocol negotiation failed: NT_STATUS_...` | 协议版本不匹配 | `-m NT1`（老设备）或 `-m SMB3`（需加密的现代服务器） |
| `NT_STATUS_BAD_NETWORK_NAME` | 共享名写错 / 是隐藏共享但拼写不对 | `-L -g` 重新确认；注意 `$` 要保留 |
| 连 445 端口时默认走了 139 | 默认端口是 139 | 加 `-p 445` |
| Server 名解析不到 | NetBIOS 名 ≠ DNS 名 | 用 `-I <IP>` |
| `mget *` 一个个问 Y/N | 默认 `prompt ON` | `prompt OFF`（配合 `recurse ON`） |
| `mget` 不下载子目录 | 默认不递归 | `recurse ON` |
| 上传/删除报 `ACCESS_DENIED` | 共享是只读 | 换共享，或确认写权限（用 [enum4linux](enum4linux.md) `-A` 慎查） |
| 口令出现在 `ps` / history | 明文写在命令行 | 用 `-A credfile` 认证文件；或 `--password` 从环境变量读 |
| `-Tc -` 输出到 stdout 后 tar 解不开 | 日志混进了 tar 流 | 加 `-d0` 把日志级别降到最低 |
| Kerberos 环境连不上 | 未走 Kerberos | `--use-kerberos=required` + `--use-krb5-ccache=...` |
| 传输很慢 | `-b` 缓冲区设得太小 | 保持默认 `0`（由服务器决定，能流水线化） |
| 容器/受限环境无法用 | 需要网络与端口访问 | 检查 139/445 是否被本地防火墙拦截 |

## 9. 防御视角（蓝队）

- **smbclient 本身是合法客户端**，检测重点在**行为模式**：
  - **匿名枚举**：`IPC$` 匿名连接 + 随后的 `srvsvc`/`lsarpc` 调用。Windows 安全日志能看到匿名登录（事件 ID 4624，登录类型 3，匿名）。
  - **大量共享遍历**：同一账号在短时间内 `Tree Connect` 到大量共享名，典型的"扫共享"模式。
  - **批量下载**：短时间内从同一共享读取大量文件，注意与正常业务流量的基线对比。
- **最有效的加固**：
  1. **禁用匿名访问**：`restrict anonymous = 2`（Samba）／组策略关闭匿名枚举。
  2. **禁用 SMBv1**：`server min protocol = SMB2`（Samba）／Windows 移除 SMB1 功能。SMB1 是绝大多数 SMB 攻击的土壤。
  3. **禁用 NTLM，只留 Kerberos**：直接废掉传递哈希（`--pw-nt-hash`）和大量中继攻击。
  4. **强制 SMB 签名**：`server signing = mandatory`（Samba）／`Microsoft network server: Digitally sign communications (always)`。这对**中间人/中继**是关键防线。
  5. **最小共享权限**：共享不要给 `Everyone`；用 NTFS + 共享双 ACL；不要有匿名可写共享。
  6. **隐藏共享不是安全措施**：`$` 结尾的共享照样能被 `-L -g` 列出来。
- **检测规则建议**：
  - 对 `NT_STATUS_ACCESS_DENIED` / `LOGON_FAILURE` 的数量做阈值告警（口令喷洒/枚举）。
  - 对单个源 IP 在一段时间内访问"多个不同共享名"的行为告警。
  - 对共享内的**大批量读取**（尤其是非工作时间）做数据外泄检测。
- **审计**：定期用 smbclient 自己扫自己的共享（在授权范围内）——"匿名能读到什么"应该是一个明确的、周期性验证的指标。

## 10. 参考

- Samba 官方文档（smbclient 章节）：<https://www.samba.org/samba/docs/current/man-html/smbclient.1.html>
- Samba 项目主页：<https://www.samba.org/>
- Kali 工具页（包归属 `samba`）：<https://www.kali.org/tools/samba/>
- man page：`man smbclient`（含完整交互命令表与 `NT_STATUS` 说明）
- 用法核实：本教程参数取自 `smbclient 4.24.6` 的 man page，并用本机 `/usr/bin/smbclient --version` 验证

---

**相关教程**：[enum4linux](enum4linux.md) ｜ [nbtscan](nbtscan.md) ｜ [nmap](nmap.md) ｜ [searchsploit](../02-漏洞分析/searchsploit.md) ｜ [whatweb](whatweb.md)
