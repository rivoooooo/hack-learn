# openssh

> Secure shell (SSH) client, for secure access to remote machines This is the portable version of OpenSSH, a free implementation of the Secure Shell protocol as specified by the IETF secsh working group. Ssh (Secure Shell) is a program for l…

> **功能分类**：通用工具 ｜ **Kali 包**：`openssh` ｜ **官方文档**：<https://www.kali.org/tools/openssh/>

## 1. 安装

```bash
sudo apt update
sudo apt install openssh-client
```

| 项目 | 内容 |
|------|------|
| 版本 | 10.4p1 |
| 架构 | any |
| 可执行命令 | `openssh-client`、`scp`、`sftp`、`ssh`、`ssh-add`、`ssh-agent`、`ssh-argv0`、`ssh-copy-id`、`ssh-keyscan`、`openssh-client-udeb`、`openssh-common`、`ssh-keygen`、`openssh-server`、`sshd`、`openssh-server-udeb`、`openssh-sftp-server`、`openssh-tests`、`ssh-askpass-gnome` |
| 依赖 | `libc6`、`libedit2`、`libselinux1`、`libssl3t64`、`openssh-common` |
| 安装体积 | 3.50 MB |
| 官网 | <https://www.openssh.com/> |
| 源码仓库 | <https://salsa.debian.org/ssh-team/openssh> |
| 包追踪 | <https://pkg.kali.org/pkg/openssh> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
openssh-client -h          # 查看用法
man openssh-client         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 18 个可执行命令，下面是官方页面内嵌的帮助原文。

### `scp`

官方给出的调用示例：`scp -h`

```text
root@kali:~# scp -h
scp: unknown option -- h
usage: scp [-346ABCOpqRrsTv] [-c cipher] [-D sftp_server_path] [-F ssh_config]
           [-i identity_file] [-J destination] [-l limit] [-o ssh_option]
           [-P port] [-S program] [-X sftp_option] source ... target
```

### `scp（示例）`

官方给出的调用示例：`scp -h`

```text
root@kali:~# scp -h
scp: unknown option -- h
usage: scp [-346ABCOpqRrsTv] [-c cipher] [-D sftp_server_path] [-F ssh_config]
           [-i identity_file] [-J destination] [-l limit] [-o ssh_option]
           [-P port] [-S program] [-X sftp_option] source ... target
```

### `sftp`

官方给出的调用示例：`sftp --help`

```text
root@kali:~# sftp --help
unknown option -- -
usage: sftp [-46AaCfNpqrv] [-B buffer_size] [-b batchfile] [-c cipher]
          [-D sftp_server_command] [-F ssh_config] [-i identity_file]
          [-J destination] [-l limit] [-o ssh_option] [-P port]
          [-R num_requests] [-S program] [-s subsystem | sftp_server]
          [-X sftp_option] destination
```

### `sftp（示例）`

官方给出的调用示例：`sftp --help`

```text
root@kali:~# sftp --help
unknown option -- -
usage: sftp [-46AaCfNpqrv] [-B buffer_size] [-b batchfile] [-c cipher]
          [-D sftp_server_command] [-F ssh_config] [-i identity_file]
          [-J destination] [-l limit] [-o ssh_option] [-P port]
          [-R num_requests] [-S program] [-s subsystem | sftp_server]
          [-X sftp_option] destination
```

### `ssh`

官方给出的调用示例：`ssh -h`

```text
root@kali:~# ssh -h
unknown option -- h
usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface] [-b bind_address]
           [-c cipher_spec] [-D [bind_address:]port] [-E log_file]
           [-e escape_char] [-F configfile] [-I pkcs11] [-i identity_file]
           [-J destination] [-L address] [-l login_name] [-m mac_spec]
           [-O ctl_cmd] [-o option] [-P tag] [-p port] [-R address]
           [-S ctl_path] [-W host:port] [-w local_tun[:remote_tun]]
           destination [command [argument ...]]
       ssh [-Q query_option]
```

### `ssh（示例）`

官方给出的调用示例：`ssh -h`

```text
root@kali:~# ssh -h
unknown option -- h
usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface] [-b bind_address]
           [-c cipher_spec] [-D [bind_address:]port] [-E log_file]
           [-e escape_char] [-F configfile] [-I pkcs11] [-i identity_file]
           [-J destination] [-L address] [-l login_name] [-m mac_spec]
           [-O ctl_cmd] [-o option] [-P tag] [-p port] [-R address]
           [-S ctl_path] [-W host:port] [-w local_tun[:remote_tun]]
           destination [command [argument ...]]
       ssh [-Q query_option]
```

### `ssh-add`

官方给出的调用示例：`ssh-add -h`

```text
root@kali:~# ssh-add -h
option requires an argument -- h
usage: ssh-add [-CcDdKkLlqvXx] [-E fingerprint_hash] [-H hostkey_file]
               [-h destination_constraint] [-S provider] [-t life]
               [file ...]
       ssh-add -s pkcs11 [-Cv] [certificate ...]
       ssh-add -e pkcs11
       ssh-add -T pubkey ...
```

### `ssh-add（示例）`

官方给出的调用示例：`ssh-add -h`

```text
root@kali:~# ssh-add -h
option requires an argument -- h
usage: ssh-add [-CcDdKkLlqvXx] [-E fingerprint_hash] [-H hostkey_file]
               [-h destination_constraint] [-S provider] [-t life]
               [file ...]
       ssh-add -s pkcs11 [-Cv] [certificate ...]
       ssh-add -e pkcs11
       ssh-add -T pubkey ...
```

### `ssh-agent`

官方给出的调用示例：`ssh-agent -h`

```text
root@kali:~# ssh-agent -h
unknown option -- h
usage: ssh-agent [-c | -s] [-DdTU] [-a bind_address] [-E fingerprint_hash]
                 [-O option] [-P allowed_providers] [-t life]
       ssh-agent [-TU] [-a bind_address] [-E fingerprint_hash] [-O option]
                 [-P allowed_providers] [-t life] command [arg ...]
       ssh-agent [-c | -s] -k
       ssh-agent -u
       ssh-agent -V
```

### `ssh-agent（示例）`

官方给出的调用示例：`ssh-agent -h`

```text
root@kali:~# ssh-agent -h
unknown option -- h
usage: ssh-agent [-c | -s] [-DdTU] [-a bind_address] [-E fingerprint_hash]
                 [-O option] [-P allowed_providers] [-t life]
       ssh-agent [-TU] [-a bind_address] [-E fingerprint_hash] [-O option]
                 [-P allowed_providers] [-t life] command [arg ...]
       ssh-agent [-c | -s] -k
       ssh-agent -u
       ssh-agent -V
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install openssh-client`，再执行 `openssh-client --version` 2>/dev/null || `openssh-client -V`
- [ ] **2.** **读官方帮助** —— `openssh-client -h`，需要细节时 `man openssh-client`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `openssh-client -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/openssh/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/openssh/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/openssh/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
