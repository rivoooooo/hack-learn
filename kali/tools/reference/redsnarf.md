# redsnarf

> Pentesting tool for retrieving credentials from Windows workstations This package contains a pentesting / redteaming tool by Ed Williams for retrieving hashes and credentials from Windows workstations, servers and domain controllers using …

> **功能分类**：通用工具 ｜ **Kali 包**：`redsnarf` ｜ **官方文档**：<https://www.kali.org/tools/redsnarf/>

## 1. 安装

```bash
sudo apt update
sudo apt install redsnarf
```

| 项目 | 内容 |
|------|------|
| 版本 | 0~git20170822 |
| 架构 | all |
| 可执行命令 | `redsnarf` |
| 依赖 | `creddump7`、`passing-the-hash`、`python3-docopt`、`python3-impacket`、`python3-ipy`、`python3-ldap`、`python3-libnmap`、`python3-netaddr`、`python3-pycryptodome`、`python3-pyuserinput`、`python3-smb`、`python3-termcolor` 等 |
| 安装体积 | 12.00 MB |
| 官网 | <https://github.com/nccgroup/redsnarf> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/redsnarf> |
| 包追踪 | <https://pkg.kali.org/pkg/redsnarf> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
redsnarf -h          # 查看用法
man redsnarf         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `redsnarf`

官方给出的调用示例：`redsnarf -h`

```text
root@kali:~# redsnarf -h
    ______           .____________                     _____
\______   \ ____   __| _/   _____/ ____ _____ ________/ ____\\
 |       _// __ \ / __ |\_____  \ /    \\__  \\_  __ \   __\\
 |    |   \  ___// /_/ |/        \   |  \/ __ \|  | \/|  |
 |____|_  /\___  >____ /_______  /___|  (____  /__|   |__|
        \/     \/     \/       \/     \/     \/
[email protected]
                                                  @redsnarf
E D Williams - NCCGroup
usage: ./redsnarf -H ip=192.168.0.1 -u administrator -p Password1 [-h] [-H HOST] [-u USERNAME] [-p PASSWORD] [-d DOMAIN_NAME] [-cC CREDPATH]
                                                                  [-cM MERGEPF] [-cO OUTPUTPATH] [-cQ QUICK_VALIDATE] [-cS SKIPLSACACHE]
                                                                  [-uA AUTO_COMPLETE] [-uC CLEAR_EVENT] [-uCP CUSTOM_POWERSHELL] [-uCIDR CIDR]
                                                                  [-uD DROPSHELL] [-uE EMPIRE_LAUNCHER] [-uFT FILE_TRANSCRIBE] [-uG C_PASSWORD]
                                                                  [-uMC MCAFEE_SITES] [-uJ JOHN_TO_PIPAL] [-uJW SENDTOJOHN] [-uJS SENDSPNTOJOHN]
                                                                  [-uL LOCKDESKTOP] [-uLP LIVEIPS] [-uM MSSQLSHELL] [-uMT METERPRETER_REVHTTPS]
                                                                  [-uO DELEGATED_PRIVS] [-uP POLICIESSCRIPTS_DUMP] [-uR MULTI_RDP] [-uRP RDP_CONNECT]
                                                                  [-uRS SNARF_SHELL] [-uS GET_SPN] [-uSS SPLIT_SPN] [-uSCF SCF_CREATOR]
                                                                  [-uSG SESSION_GOPHER] [-uU UNATTEND] [-uX XCOMMAND] [-uXS XSCRIPT]
                                                                  [-uW WIFI_CREDENTIALS] [-uWU WINDOWS_UPDATES] [-hI DRSUAPI] [-hN NTDS_UTIL]
                                                                  [-hQ QLDAP] [-hS CREDSFILE] [-hP PASS_ON_BLANK] [-hK MIMIKITTENZ] [-hL LSASS_DUMP]
                                                                  [-hM MASSMIMI_DUMP] [-hR STEALTH_MIMI] [-hT GOLDEN_TICKET] [-hW WIN_SCP]
                                                                  [-eA SERVICE_ACCOUNTS] [-eD USER_DESC] [-eL FIND_USER] [-eO OFIND_USER]
                                                                  [-eP PASSWORD_POLICY] [--protocols [PROTOCOLS ...]] [-eR RECORDDESKTOP]
                                                                  [-eS SCREENSHOT] [-eT SYSTEM_TASKLIST] [-rA EDQ_AUTOLOGON] [-rB EDQ_BACKDOOR]
                                                                  [-rC EDQ_SCFORCEOPTION] [-rF FAT] [-rL LAT] [-rM EDQ_SINGLESESSIONPERUSER]
                                                                  [-rN EDQ_NLA] [-rR EDQ_RDP] [-rS EDQ_ALLOWTGTSESSIONKEY] [-rT EDQ_TRDP]
                                                                  [-rU EDQ_UAC] [-rW EDQ_WDIGEST]
RedSnarf Version 0.5p: Offers a rich set of features to help Pentest Servers and Workstations
options:
  -h, --help        show this help message and exit
  -H, --host HOST   Specify a hostname -H ip= / range -H range= / targets file -H file= to grab hashes from
  -u, --username USERNAME
                    Enter a username
  -p, --password PASSWORD
                    Enter a password or hash
  -d, --domain_name DOMAIN_NAME
                    <Optional> Enter domain name
Configurational:
  -cC, --credpath CREDPATH
                    <Optional> Enter path to creddump7 default /usr/share/creddump7/
  -cM, --mergepf MERGEPF
                    <Optional> Enter output path and filename to merge multiple pwdump files default /tmp/merged.txt
  -cO, --outputpath OUTPUTPATH
                    <Optional> Enter output path default /tmp/
  -cQ, --quick_validate QUICK_VALIDATE
                    <Optional> Quickly Validate Credentials
  -cS, --skiplsacache SKIPLSACACHE
                    <Optional> Enter y to skip dumping lsa and cache and go straight to hashes!!
Utilities:
  -uA, --auto_complete AUTO_COMPLETE
                    <Optional> Copy autocomplete file to /etc/bash_completion.d
  -uC, --clear_event CLEAR_EVENT
                    <Optional> Clear event log - application, security, setup or system
  -uCP, --custom_powershell CUSTOM_POWERSHELL
                    <Optional> Run Custom Powershell Scripts found in the RedSnarf folder
  -uCIDR, --cidr CIDR
                    <Optional> Convert CIDR representation to ip, hostmask, broadcast
  -uD, --dropshell DROPSHELL
                    <Optional> Enter y to Open up a shell on the remote machine
  -uE, --empire_launcher EMPIRE_LAUNCHER
                    <Optional> Start Empire Launcher
  -uFT, --file_transcribe FILE_TRANSCRIBE
                    <Optional> Converts a file to base64 then sends via SendKeys
  -uG, --c_password C_PASSWORD
                    <Optional> Decrypt GPP Cpassword
  -uMC, --mcafee_sites MCAFEE_SITES
                    <Optional> Decrypt Mcafee Sites Password
  -uJ, --john_to_pipal JOHN_TO_PIPAL
                    <Optional> Send passwords cracked with JtR to Pipal for Auditing
  -uJW, --sendtojohn SENDTOJOHN
                    <Optional> Enter path to NT Hash file to send to JtR
  -uJS, --sendspntojohn SENDSPNTOJOHN
                    <Optional> Enter path of SPN Hash file to send to JtR Jumbo
  -uL, --lockdesktop LOCKDESKTOP
                    <Optional> Lock remote users Desktop
  -uLP, --liveips LIVEIPS
                    <Optional> Ping scan to generate a list of live IP's
  -uM, --mssqlshell MSSQLSHELL
                    <Optional> Start MSSQL Shell use WIN for Windows Auth, DB for MSSQL Auth
  -uMT, --meterpreter_revhttps METERPRETER_REVHTTPS
                    <Optional> Launch Reverse Meterpreter HTTPS
  -uO, --delegated_privs DELEGATED_PRIVS
                    <Optional> Delegated Privilege Checker
  -uP, --policiesscripts_dump POLICIESSCRIPTS_DUMP
                    <Optional> Enter y to Dump Policies and Scripts folder from a Domain Controller
  -uR, --multi_rdp MULTI_RDP
                    <Optional> Enable Multi-RDP with Mimikatz
  -uRP, --rdp_connect RDP_CONNECT
                    <Optional> Connect to existing RDP sessions without password
  -uRS, --snarf_shell SNARF_SHELL
                    <Optional> Start Reverse Listening Snarf Shell
  -uS, --get_spn GET_SPN
                    <Optional> Get SPN's from DC
  -uSS, --split_spn SPLIT_SPN
                    <Optional> Split SPN File
  -uSCF, --scf_creator SCF_CREATOR
                    <Optional> Create an SCF file for some SMB hash capturing fun
  -uSG, --session_gopher SESSION_GOPHER
                    <Optional> Run Session Gopher on Remote Machine
  -uU, --unattend UNATTEND
                    <Optional> Enter y to look for and grep unattended installation files
  -uX, --xcommand XCOMMAND
                    <Optional> Run custom command
  -uXS, --xscript XSCRIPT
                    <Optional> Run custom script
  -uW, --wifi_credentials WIFI_CREDENTIALS
                    <Optional> Grab Wifi Credentials
  -uWU, --windows_updates WINDOWS_UPDATES
                    <Optional> Get Windows Update Status
Hash related:
  -hI, --drsuapi DRSUAPI
                    <Optional> Extract NTDS.dit hashes using drsuapi method - accepts machine name as username
  -hN, --ntds_util NTDS_UTIL
                    <Optional> Extract NTDS.dit using NTDSUtil
  -hQ, --qldap QLDAP
                    <Optional> In conjunction with the -i and -n option - Query LDAP for Account Status when dumping Domain Hashes
  -hS, --credsfile CREDSFILE
                    Spray multiple hashes at a target range
  -hP, --pass_on_blank PASS_ON_BLANK
                    Password to use when only username found in Creds File
  -hK, --mimikittenz MIMIKITTENZ
                    <Optional> Run Mimikittenz
  -hL, --lsass_dump LSASS_DUMP
                    <Optional> Dump lsass for offline use with mimikatz
  -hM, --massmimi_dump MASSMIMI_DUMP
                    <Optional> Mimikatz Dump Credentaisl from the remote machine(s)
  -hR, --stealth_mimi STEALTH_MIMI
                    <Optional> stealth version of mass-mimikatz
  -hT, --golden_ticket GOLDEN_TICKET
                    <Optional> Create a Golden Ticket
  -hW, --win_scp WIN_SCP
                    <Optional> Check for, and decrypt WinSCP hashes
Enumeration related:
  -eA, --service_accounts SERVICE_ACCOUNTS
                    <Optional> Enum service accounts, if any
  -eD, --user_desc USER_DESC
                    <Optional> Save AD User Description Field to file, check for password
  -eL, --find_user FIND_USER
                    <Optional> Find user - Live
  -eO, --ofind_user OFIND_USER
                    <Optional> Find user - Offline
  -eP, --password_policy PASSWORD_POLICY
                    <Optional> Display Password Policy
  --protocols [PROTOCOLS ...]
                    ['139/SMB', '445/SMB']
  -eR, --recorddesktop RECORDDESKTOP
                    <Optional> Record a desktop using Windows Problem Steps Recorder
  -eS, --screenshot SCREENSHOT
                    <Optional> Take a screenshot of remote machine desktop
  -eT, --system_tasklist SYSTEM_TASKLIST
                    <Optional> Display NT AUTHORITY\SYSTEM Tasklist
Registry related:
  -rA, --edq_autologon EDQ_AUTOLOGON
                    <Optional> (e)nable/(d)isable/(q)uery AutoLogon Registry Setting
  -rB, --edq_backdoor EDQ_BACKDOOR
                    <Optional> (e)nable/(d)isable/(q)uery Backdoor Registry Setting
  -rC, --edq_scforceoption EDQ_SCFORCEOPTION
                    <Optional> (e)nable/(d)isable/(q)uery Smart Card scforceoption Registry Setting
  -rF, --fat FAT    <Optional> Write batch file for turning on/off FilterAdministratorToken Policy
  -rL, --lat LAT    <Optional> Write batch file for turning on/off Local Account Token Filter Policy
  -rM, --edq_SingleSessionPerUser EDQ_SINGLESESSIONPERUSER
                    <Optional> (E)nable/(D)isable/(Q)uery RDP SingleSessionPerUser Registry Setting
  -rN, --edq_nla EDQ_NLA
                    <Optional> (e)nable/(d)isable/(q)uery NLA Status
  -rR, --edq_rdp EDQ_RDP
                    <Optional> (e)nable/(d)isable/(q)uery RDP Status
  -rS, --edq_allowtgtsessionkey EDQ_ALLOWTGTSESSIONKEY
                    <Optional> (E)nable/(D)isable/(Q)uery allowtgtsessionkey Registry Setting
  -rT, --edq_trdp EDQ_TRDP
                    <Optional> (e)nable/(d)isable/(q)uery Tunnel RDP out of port 443
  -rU, --edq_uac EDQ_UAC
                    <Optional> (e)nable/(d)isable/(q)uery UAC Registry Setting
  -rW, --edq_wdigest EDQ_WDIGEST
                    <Optional> (e)nable/(d)isable/(q)uery Wdigest UseLogonCredential Registry Setting
Updated on: 2025-Dec-09
 Edit this page
recoverdm
redsocks
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
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install redsnarf`，再执行 `redsnarf --version` 2>/dev/null || `redsnarf -V`
- [ ] **2.** **读官方帮助** —— `redsnarf -h`，需要细节时 `man redsnarf`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `redsnarf -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/redsnarf/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/redsnarf/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/redsnarf/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
