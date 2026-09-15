# snaffler-ng

> SMB share credential and sensitive data scanner Impacket port of Snaffler, a post-exploitation tool that discovers readable SMB shares, walks directory trees, and identifies credentials and sensitive data on Windows file systems. Features …

> **功能分类**：通用工具 ｜ **Kali 包**：`snaffler-ng` ｜ **官方文档**：<https://www.kali.org/tools/snaffler-ng/>

## 1. 安装

```bash
sudo apt update
sudo apt install snaffler-ng
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.5.13 |
| 架构 | all |
| 可执行命令 | `snaffler-ng`、`snaffler` |
| 依赖 | `python3`、`python3-cryptography`、`python3-impacket`、`python3-rich`、`python3-tomlkit`、`python3-typer`、`snaffler` |
| 安装体积 | 1.85 MB |
| 官网 | <https://github.com/totekuh/snaffler-ng> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/snaffler-ng> |
| 包追踪 | <https://pkg.kali.org/pkg/snaffler-ng> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
snaffler-ng -h          # 查看用法
man snaffler-ng         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `snaffler`

官方给出的调用示例：`snaffler --help`

```text
root@kali:~# snaffler --help
 Usage: snaffler [OPTIONS] COMMAND [ARGS]...
 Snaffler Linux – Find credentials and sensitive data on Windows SMB shares
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --version  -V        Show version and exit                                   │
│ --help               Show this message and exit.                             │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Authentication ─────────────────────────────────────────────────────────────╮
│ --username    -u      TEXT  Username for authentication                      │
│ --password    -p      TEXT  Password for authentication (NTLM)               │
│ --hash                TEXT  NT hash for Pass-the-Hash authentication         │
│ --kerberos    -k            Use Kerberos authentication (requires -d and     │
│                             hostnames as targets)                            │
│ --use-kcache                Use Kerberos credentials from ccache             │
│                             (KRB5CCNAME)                                     │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Targeting ──────────────────────────────────────────────────────────────────╮
│ --domain                      -d      TEXT     AD domain for LDAP discovery, │
│                                                or Kerberos realm (e.g.       │
│                                                CORP.LOCAL)                   │
│ --unc                                 TEXT     Direct UNC path(s) to scan    │
│                                                (disables computer/share      │
│                                                discovery)                    │
│ --local-fs                            TEXT     Local directory path(s) to    │
│                                                scan (no SMB, scans local     │
│                                                filesystem)                   │
│ --ftp                                 TEXT     FTP target URL(s) to scan     │
│                                                (e.g. ftp://10.0.0.5/data or  │
│                                                bare 10.0.0.5)                │
│ --ftp-file                            PATH     File containing FTP targets   │
│                                                (one per line, same format as │
│                                                --ftp)                        │
│ --ftp-tls                                      Use FTPS (FTP over TLS) for   │
│                                                --ftp targets                 │
│ --computer                    -c      TEXT     Target computer(s) by         │
│                                                hostname, IP, CIDR            │
│                                                (10.0.0.0/24), or range       │
│                                                (10.0.0.1-50)                 │
│ --computer-file                       PATH     File containing computer      │
│                                                names (one per line)          │
│ --shares-only                 -a               Only enumerate shares, skip   │
│                                                filesystem walking            │
│ --no-check-writable                            Skip the per-share            │
│                                                write-access probe (RW        │
│                                                detection is on by default)   │
│ --check-writable                               Force-enable the per-share    │
│                                                write-access probe (overrides │
│                                                a config check_writable =     │
│                                                false)                        │
│ --rescan-unreadable                            Re-test previously unreadable │
│                                                shares from state DB with     │
│                                                current creds                 │
│ --domain-users                                 Discover interesting AD users │
│                                                and match their names in file │
│                                                contents (requires -d)        │
│ --user-match                          TEXT     Keyword filter for            │
│                                                interesting usernames         │
│                                                (repeatable, default:         │
│                                                sql,svc,service,...)          │
│ --user-min-len                        INTEGER  Minimum username length for   │
│                                                dynamic user rules            │
│                                                [default: 6]                  │
│ --grab                                         Bulk download mode: read file │
│                                                paths from stdin, download to │
│                                                -m dir (no scanning)          │
│ --include-disabled                             Include disabled and stale    │
│                                                (4+ months inactive) computer │
│                                                accounts                      │
│ --stdin                                        Read NXC SMB --shares output  │
│                                                from stdin and use as UNC     │
│                                                targets                       │
│ --share                               TEXT     Only scan shares matching     │
│                                                glob pattern                  │
│                                                (case-insensitive,            │
│                                                repeatable)                   │
│ --exclude-share                       TEXT     Skip shares matching glob     │
│                                                pattern (case-insensitive,    │
│                                                repeatable)                   │
│ --exclude-unc,--exclude-path          TEXT     Skip paths matching glob      │
│                                                pattern (case-insensitive,    │
│                                                repeatable). Works with both  │
│                                                UNC and local paths.          │
│ --exclusions                          PATH     File of hostnames/IPs to skip │
│                                                (one per line)                │
│ --max-hosts                           INTEGER  Stop after scanning N hosts   │
│                                                (applied after exclusions)    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Network ────────────────────────────────────────────────────────────────────╮
│ --dc-host                TEXT     Domain controller hostname, FQDN or IP     │
│                                   (required for Kerberos LDAP)               │
│ --timeout                INTEGER  SMB connection timeout in seconds          │
│                                   (default: 5)                               │
│                                   [default: 5]                               │
│ --socks                  TEXT     SOCKS proxy for pivoting (e.g.             │
│                                   socks5://127.0.0.1:1080)                   │
│ --nameserver,--ns        TEXT     Custom DNS server for hostname resolution  │
│                                   (e.g. DC IP)                               │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Output ─────────────────────────────────────────────────────────────────────╮
│ --output     -o      PATH               Write results to file                │
│ --log-level          [debug|info|data]  Log verbosity: debug | info | data   │
│                                         (data = findings only)               │
│                                         [default: info]                      │
│ --log-type   -t      [plain|json|tsv]   Output format (auto-detected from -o │
│                                         extension if omitted)                │
│ --no-banner  -q                         Disable startup banner               │
│ --no-color                              Disable colored output               │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Scanning ───────────────────────────────────────────────────────────────────╮
│ --min-interest    -b      INTEGER RANGE [0<=x<=3]  Minimum interest level to │
│                                                    report (0=all, 3=high     │
│                                                    only)                     │
│                                                    [default: 0]              │
│ --max-read-bytes  -r      INTEGER                  Maximum bytes to read     │
│                                                    from a file for content   │
│                                                    scanning (default: 2 MB)  │
│                                                    [default: 2097152]        │
│ --max-file-bytes  -l      INTEGER                  Maximum file size allowed │
│                                                    for scanning and          │
│                                                    downloading (default: 10  │
│                                                    MB)                       │
│                                                    [default: 10485760]       │
│ --snaffle-path    -m      PATH                     Directory to copy         │
│                                                    interesting files into    │
│ --context         -j      INTEGER                  Bytes of context around   │
│                                                    matched strings (default: │
│                                                    200)                      │
│                                                    [default: 200]            │
│ --max-depth               INTEGER                  Maximum directory         │
│                                                    recursion depth (0 =      │
│                                                    share root only)          │
│ --fast                                             Skip known time-waster    │
│                                                    directories and           │
│                                                    interleave share walking  │
│ --match                   TEXT                     Only output findings      │
│                                                    matching this regex       │
│                                                    (applied to path, rule,   │
│                                                    match, context)           │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Advanced ───────────────────────────────────────────────────────────────────╮
│ --max-threads            -x      INTEGER  Maximum total worker threads       │
│                                           (default: 60)                      │
│                                           [default: 60]                      │
│ --dns-threads                    INTEGER  Concurrent threads for DNS + port  │
│                                           445 reachability probes (default:  │
│                                           100)                               │
│                                           [default: 100]                     │
│ --max-threads-per-share          INTEGER  Max concurrent tree-walk threads   │
│                                           per share (0 = unlimited, --fast   │
│                                           auto-sets)                         │
│                                           [default: 0]                       │
│ --config                 -z      PATH     Path to TOML configuration file    │
│ --rule-dir               -R      PATH     Directory containing custom TOML   │
│                                           rule files                         │
│ --stealth                                 OPSEC mode: pad LDAP queries with  │
│                                           random attributes to break IDS     │
│                                           signatures                         │
│ --state                          PATH     Path to state database (default:   │
│                                           ./snaffler.db). Auto-resumes if DB │
│                                           exists.                            │
│ --fresh                                   Ignore existing state DB and start │
│                                           a clean scan                       │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Web Dashboard ──────────────────────────────────────────────────────────────╮
│ --web                      Enable live web dashboard (requires: pip install  │
│                            snaffler-ng[web])                                 │
│ --web-port        INTEGER  Port for web dashboard (default: 8080)            │
│                            [default: 8080]                                   │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ results  Display stats and findings from a scan database                     │
╰──────────────────────────────────────────────────────────────────────────────╯
Updated on: 2026-Sep-03
 Edit this page
rustscan
7zip
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
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install snaffler-ng`，再执行 `snaffler-ng --version` 2>/dev/null || `snaffler-ng -V`
- [ ] **2.** **读官方帮助** —— `snaffler-ng -h`，需要细节时 `man snaffler-ng`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: snaffler [OPTIONS] COMMAND [ARGS]...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/snaffler-ng/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/snaffler-ng/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/snaffler-ng/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
