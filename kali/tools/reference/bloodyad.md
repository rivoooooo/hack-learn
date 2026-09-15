# bloodyad

> Active Directory privilege escalation framework bloodyAD can perform specific LDAP calls to a domain controller in order to perform AD privesc. It supports authentication using cleartext passwords, pass-the-hash, pass-the-ticket or certifi…

> **功能分类**：通用工具 ｜ **Kali 包**：`bloodyad` ｜ **官方文档**：<https://www.kali.org/tools/bloodyad/>

## 1. 安装

```bash
sudo apt update
sudo apt install bloodyad
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.5.5 |
| 架构 | amd64 |
| 可执行命令 | `bloodyad` |
| 依赖 | `python3` |
| 安装体积 | 54.80 MB |
| 官网 | <https://github.com/CravateRouge/bloodyAD> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/bloodyAD> |
| 包追踪 | <https://pkg.kali.org/pkg/bloodyad> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
bloodyad -h          # 查看用法
man bloodyad         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `bloodyad`

> 官方示例调用：`bloodyad -h`

```text
root@kali:~# bloodyad -h
usage: bloodyad [-h] [-d DOMAIN] [-u USERNAME] [-p PASSWORD]
                [-k [KERBEROS ...]] [-f {b64,hex,aes,rc4,default}]
                [-c [CERTIFICATE]] [-s] -H HOST [-i DC_IP] [--dns DNS]
                [-t TIMEOUT] [--gc] [-v {QUIET,INFO,DEBUG,TRACE}] [--json]
                {add,get,msldap,remove,set} ...
AD Privesc Swiss Army Knife
options:
  -h, --help            show this help message and exit
  -d, --domain DOMAIN   Domain used for NTLM authentication
  -u, --username USERNAME
                        Username used for NTLM authentication
  -p, --password PASSWORD
                        password or LMHASH:NTHASH for NTLM authentication,
                        password or AES/RC4 key for kerberos, password for
                        certificate (Do not specify to trigger integrated
                        windows authentication)
  -k, --kerberos [KERBEROS ...]
                        Enable Kerberos authentication. If '-p' is provided it
                        will try to query a TGT with it. You can also provide
                        a list of one or more optional keywords as '-k
                        kdc=192.168.100.1 kdcc=192.168.150.1
                        realmc=foreign.realm.corp
                        <keyfile_type>=/home/silver/Admin.ccache',
                        <keyfile_type> being ccache, kirbi or keytab, 'kdc'
                        being the kerberos server for the keyfile provided and
                        'realmc' and 'kdcc' for cross realm (the realm of the
                        '--host' provided)
  -f, --format {b64,hex,aes,rc4,default}
                        Specify format for '--password' or '-k <keyfile>'
  -c, --certificate [CERTIFICATE]
                        Schannel authentication or krb pkinit if -k also
                        provided, e.g: "path/to/key:path/to/cert" (Use Windows
                        Certstore with krb if left empty)
  -s, --secure          Use LDAP/GC over TLS (LDAPS/GCS). Use -ss for simple
                        bind and -sss to remove all channel binding/signing
                        (useful for debug).
  -H, --host HOST       Hostname or IP of the DC (ex: my.dc.local or
                        172.16.1.3)
  -i, --dc-ip DC_IP     IP of the DC (useful if you provided a --host which
                        can't resolve)
  --dns DNS             IP of the DNS to resolve AD names (useful for inter-
                        domain functions)
  -t, --timeout TIMEOUT
                        Connection timeout in seconds
  --gc                  Connect to Global Catalog (GC)
  -v, --verbose {QUIET,INFO,DEBUG,TRACE}
                        Adjust output verbosity
  --json                Output results in JSON format
Commands:
  {add,get,msldap,remove,set}
    add                 [ADD] function category
    get                 [GET] function category
    msldap              [MSLDAP] function category
    remove              [REMOVE] function category
    set                 [SET] function category
Updated on: 2026-Aug-25
 Edit this page
bloodhound
blue-hydra
LIGHT
DARK
Links
Home
Download / Get Kali
Blog
OS Documentation
Tool Documentation
System Status
Archived Releases
Partnerships
Platforms
ARM (SBC)
NetHunter (Mobile)
Amazon AWS
Docker
Linode
Microsoft Azure
Microsoft Store (WSL)
Vagrant
Development
Bug Tracker
Continuous Integration
Network Mirror
Package Tracker
GitLab
Community
Discord
Support Forum
PeerTube
Follow Us
Bluesky
Facebook
Instagram
Mastodon
Substack
X
Newsletter
RSS
Policies
Cookie Policy
Privacy Policy
Trademark Policy
© OffSec Services Limited 2026. All rights reserved.
Kali Linux is part of OffSec's Community Projects
Learn more about OffSec's free, open-source penetration testing tools for cybersecurity professionals
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install bloodyad`，再执行 `bloodyad --version` 2>/dev/null || `bloodyad -V`
- [ ] **2.** **读官方帮助** —— `bloodyad -h`，需要细节时 `man bloodyad`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `bloodyad -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/bloodyad/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/privilege-escalation.md`](../../tools/by-attack/privilege-escalation.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/bloodyad/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/bloodyad/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
