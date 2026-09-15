# wordlists / SecLists（Kali 字典库）

> **一句话**：Kali 自带的字典集合与目录规范，以及如何安装与使用 SecLists 这个「字典中的字典」。
> **分类**：口令攻击 ｜ **Kali 包**：`wordlists`、`seclists` ｜ **官方文档**：<https://www.kali.org/tools/wordlists/>、<https://github.com/danielmiessler/SecLists>

## 1. 它解决什么问题

前几篇教程（[hydra](hydra.md)、[john](john.md)、[hashcat](hashcat.md)、[crunch](crunch.md)、[cewl](cewl.md)）全都需要一样东西：**候选词列表**。这一篇专门讲「字典从哪来、放在哪、怎么选、怎么装」。

两个包的区别：

| 包 | 内容 | 定位 |
| --- | --- | --- |
| `wordlists` | **`rockyou.txt`** + 一批指向其他工具字典的软链接 | Kali 的「基础字典目录」 |
| `seclists` | 数千个分类字典（用户名、口令、目录、参数、payload…） | 网络安全的「字典合集」 |

**关键事实**：rockyou 是 2009 年一次真实数据泄露事件（RockYou 网站）中的 1400 万条明文口令。它是「大众弱口令」的代表样本，也是所有口令审计的**第一步筛子**——但它**不包含组织特有词汇**，这是 [cewl](cewl.md) 存在的理由。

## 2. 工作原理

### 2.1 为什么字典是口令攻击的核心

口令爆破的效率由两个因子决定：

```
成功率 ≈ (候选集覆盖真实口令的概率) × (在给定时间内能跑完的候选数)
```

通用字典优化的是**第一项**：用人类真实选择口令的统计规律，构造「高命中率、低体积」的候选集。

rockyou 的价值来自它的「真实性」：它是 1400 万个**真人设的**口令。所以按频次排序后，前 1000 个词就能覆盖相当比例的真实账户——这就是为什么安全圈有「Top 1000 口令表」这种产物。

### 2.2 Kali 的 `/usr/share/wordlists/` 目录设计

Kali 不在 `wordlists` 包里塞满字典，而是把它做成**一个集中索引目录**：真正的字典由各自的工具包提供，`wordlists` 包用**软链接**把它们聚合到一起。

```text
/usr/share/wordlists
|-- brutespray -> /usr/share/brutespray/wordlist
|-- dirb -> /usr/share/dirb/wordlists
|-- dirbuster -> /usr/share/dirbuster/wordlists
|-- dnsmap.txt -> /usr/share/dnsmap/wordlist_TLAs.txt
|-- fasttrack.txt -> /usr/share/set/src/fasttrack/wordlist.txt
|-- fern-wifi -> /usr/share/fern-wifi-cracker/extras/wordlists
|-- john.lst -> /usr/share/john/password.lst
|-- legion -> /usr/share/legion/wordlists
|-- metasploit -> /usr/share/metasploit-framework/data/wordlists
|-- nmap.lst -> /usr/share/nmap/nselib/data/passwords.lst
|-- rockyou.txt.gz
|-- seclists -> /usr/share/seclists
|-- sqlmap.txt -> /usr/share/sqlmap/data/txt/wordlist.txt
|-- wfuzz -> /usr/share/wfuzz/wordlist
`-- wifite.txt -> /usr/share/dict/wordlist-probable.txt
```

**设计含义**（很重要）：

- 你**不需要记住每条路径**，只要用 `/usr/share/wordlists/<名字>` 就行。
- 软链接指向的包**卸载后链接会失效**——这就是「明明 `/usr/share/wordlists/dirb` 存在，但里面是空的」的原因。
- `rockyou.txt.gz` 是**唯一的实体文件**，且是**压缩状态**，必须手动解压。

### 2.3 为什么 rockyou 要压缩

- 压缩后 51 MB，解压后 134 MB（`-rw-r--r-- 1 root root 134M Mar 3 2013 rockyou.txt`）。
- 2013 年的镜像体积考虑：不是所有用户都需要它，所以做成「按需解压」。

### 2.4 字典的分类逻辑

字典按**用途**分类，选错类别等于白跑：

| 用途 | 典型字典 | 用在 |
| --- | --- | --- |
| 口令 | `rockyou.txt`、`Passwords/` 下各类 | [hydra](hydra.md)、[medusa](medusa.md)、[hashcat](hashcat.md) 的 `-a 0` |
| 用户名 | `Usernames/` | hydra 的 `-L` |
| Web 目录/文件 | `Discovery/Web-Content/` | 目录爆破（gobuster/ffuf/dirb） |
| DNS 子域 | `Discovery/DNS/` | 子域枚举 |
| 参数名 | `Discovery/Web-Content/burp-parameter-names.txt` | 参数发现 |
| 模糊测试 payload | `Fuzzing/` | 输入验证测试 |
| 敏感数据模式 | `Pattern-Matching/` | 从文本里 grep 敏感信息 |

**最容易犯的错**：拿 `Discovery/Web-Content/` 的目录字典去爆破登录口令。那些词（`index.html`、`admin.php`）**不是口令**。

## 3. 安装与快速上手

```bash
# 基础字典包
sudo apt install wordlists

# 查看目录结构（官方提供的自文档命令）
wordlists -h

# 解压 rockyou
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# 验证
wc -l /usr/share/wordlists/rockyou.txt
# 14344392 /usr/share/wordlists/rockyou.txt
ls -lah /usr/share/wordlists/rockyou.txt
# -rw-r--r-- 1 root root 134M Mar  3  2013 /usr/share/wordlists/rockyou.txt
```

安装 SecLists：

```bash
sudo apt install seclists
ls /usr/share/seclists/
```

**官方仓库方式的 SecLists**（需要最新版本时）：

```bash
sudo git clone --depth 1 https://github.com/danielmiessler/SecLists.git /usr/share/seclists
# 或者只取需要的目录以节省空间
```

**SecLists 体积**：完整仓库约 1~2 GB 量级（包含大量 fuzz 与 payload 文件）。**装之前先确认磁盘空间**：

```bash
df -h /usr/share
```

## 4. 核心参数详解（按字典选择维度组织）

`wordlists` 本身只有一个 `-h`（打印目录树），没有其他参数。因此这里给出**选择字典的决策表**——这比记参数更重要。

| 维度 | 选项 | 建议 |
| --- | --- | --- |
| **用途** | 口令 / 用户名 / 目录 / 子域 / 参数 / payload | **先想清楚要做什么**，再进对应目录 |
| **体积** | Top 100 / Top 1000 / Top 10k / 全量 | 在线爆破只能用小体积（前两者）；离线破解可上全量 |
| **语言** | 英文 / 中文 / 多语言 | 中文目标用 `seclists/Passwords/` 下的中文相关文件，或自建 |
| **场景** | 通用弱口令 / 默认口令 / Wi-Fi PSK | `dpl4hydra`（默认口令）、`wifite.txt`（Wi-Fi 常见 PSK） |
| **规格** | 是否含用户名 / 是否为 `user:pass` 组合 | `-L`/`-P` 需要分开的文件，`-C` 需要组合文件 |

### 常用字典速查表

| 路径 | 内容 | 典型用途 |
| --- | --- | --- |
| `/usr/share/wordlists/rockyou.txt` | 1400 万条真实泄露口令 | 口令爆破第一遍 |
| `/usr/share/wordlists/john.lst` | John 自带口令表 | 小字典快速试 |
| `/usr/share/wordlists/nmap.lst` | Nmap 服务口令表 | 服务默认口令 |
| `/usr/share/wordlists/metasploit/` | Metasploit 的口令/用户名库 | 多种协议默认口令 |
| `/usr/share/wordlists/sqlmap.txt` | SQLMap 口令表 | 数据库爆破 |
| `/usr/share/wordlists/wifite.txt` | Wi-Fi 常见 PSK | WPA 握手包破解 |
| `/usr/share/wordlists/dirb/` | Web 目录/文件字典 | 目录爆破 |
| `/usr/share/wordlists/dirbuster/` | 分级目录字典（小/中/大） | 目录爆破 |
| `/usr/share/wordlists/dnsmap.txt` | 顶级域名字典 | 子域枚举 |
| `/usr/share/seclists/Passwords/` | 各类口令表 | 口令爆破 |
| `/usr/share/seclists/Usernames/` | 用户名表 | hydra `-L` |
| `/usr/share/seclists/Discovery/Web-Content/` | Web 路径字典 | 目录爆破 |
| `/usr/share/seclists/Discovery/DNS/` | DNS 子域字典 | 子域枚举 |

### SecLists 目录结构

```text
/usr/share/seclists/
├── Discovery/          # 发现类：Web-Content、DNS、SNMP、Infrastructure …
├── Fuzzing/            # 模糊测试 payload（SQLi、XSS、XXE、LDAP …）
├── Passwords/          # 口令字典（含 Leaked-Databases、Common-Credentials …）
├── Pattern-Matching/   # 敏感信息正则模式
├── Payloads/           # 各类 payload
├── Usernames/          # 用户名
├── Miscellaneous/      # 杂项
└── Web-Shells/         # WebShell
```

**几个高价值子目录**：

| 路径 | 说明 |
| --- | --- |
| `Passwords/Common-Credentials/` | Top 100/1000/10000 口令表，**在线爆破首选** |
| `Passwords/Leaked-Databases/` | 各种泄露库（含 rockyou 变体） |
| `Usernames/Names/` | 常见名字 |
| `Usernames/top-usernames-shortlist.txt` | 短用户名列表 |
| `Discovery/Web-Content/directory-list-2.3-medium.txt` | 目录爆破经典字典 |
| `Discovery/Web-Content/raft-*-directories.txt` | RAFT 系列，覆盖度好 |
| `Discovery/DNS/subdomains-top1million-5000.txt` | 子域枚举（小体积版） |

**探测命令**：

```bash
# 找所有 Top 口令表
ls -lh /usr/share/seclists/Passwords/Common-Credentials/ | head -20

# 找特定关键字
find /usr/share/seclists -iname '*wpa*' -o -iname '*wifi*' | head

# 看目录树概览
find /usr/share/seclists -maxdepth 2 -type d | sort | head -40
```

## 5. 实战演练

**环境声明**：所有演示均针对**你自己的机器 / 隔离靶场 / 自建靶机**。**严禁对未授权目标使用**。

### 场景 1：解压 rockyou 并核对（每个人的第一步）

```bash
# 1) 看包裹里的样子
ls -lh /usr/share/wordlists/rockyou.txt.gz
# -rw-r--r-- 1 root root 51M Mar  3  2013 /usr/share/wordlists/rockyou.txt.gz

# 2) 解压（gunzip 会删除 .gz，只留 .txt）
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# 3) 核对
wc -l /usr/share/wordlists/rockyou.txt
# 14344392 /usr/share/wordlists/rockyou.txt

ls -lah /usr/share/wordlists/rockyou.txt
# -rw-r--r-- 1 root root 134M Mar  3  2013 /usr/share/wordlists/rockyou.txt
```

**如果你想保留 `.gz`**（例如为了省空间，只在需要时流式解压）：

```bash
# 方式一：用 zcat 流式喂给工具（不落盘）
zcat /usr/share/wordlists/rockyou.txt.gz | hashcat -m 0 -a 0 hashes.txt

# 方式二：解压到别处，保留原压缩包
gunzip -c /usr/share/wordlists/rockyou.txt.gz > ~/rockyou.txt

# 方式三：用 gzip -k 保留原文件
sudo gzip -dk /usr/share/wordlists/rockyou.txt.gz
```

**注意 `-k`**：默认 `gunzip` 会**删除** `.gz` 文件。若不想要这个行为，用 `gzip -dk` 或 `gunzip -c` 重定向。

### 场景 2：把 rockyou 变成「可用的分层字典」

直接拿 1400 万条去在线爆破是不现实的（见 [hydra](hydra.md) 的速度计算）。正确做法是**分层**：

```bash
# 1) 取前 1000 条（rockyou 已按常见程度大致排序）
head -1000 /usr/share/wordlists/rockyou.txt > ~/top1000.txt

# 2) 取前 1 万条
head -10000 /usr/share/wordlists/rockyou.txt > ~/top10k.txt

# 3) 只保留符合目标口令策略的（长度 8-12，含大小写和数字）
pw-inspector -i /usr/share/wordlists/rockyou.txt \
             -m 8 -M 12 -l -u -n \
             -o ~/filtered.txt 2>/dev/null || \
  grep -P '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,12}$' /usr/share/wordlists/rockyou.txt > ~/filtered.txt

wc -l ~/top1000.txt ~/top10k.txt ~/filtered.txt
```

`pw-inspector` 来自 `hydra` 包，专门用来**按目标口令策略裁剪字典**——这能显著提升小体积字典的命中率。

**分层使用的策略**：

```text
第 1 层：top1000.txt        → 在线爆破（几十秒内跑完）
第 2 层：top10k.txt         → 在线爆破（几分钟）
第 3 层：filtered / 全量     → 离线破解（hashcat，见 04-口令攻击/hashcat.md）
```

### 场景 3：安装 SecLists 并挑出「对的」字典

```bash
# 1) 先看空间
df -h /usr/share

# 2) 安装
sudo apt install seclists

# 3) 确认目录结构
ls /usr/share/seclists/
# Discovery  Fuzzing  Miscellaneous  Passwords  Pattern-Matching  Payloads  Usernames  Web-Shells

# 4) 找在线爆破用的「小而精」口令表
ls -lh /usr/share/seclists/Passwords/Common-Credentials/ | head
```

**预期输出（节选）**

```
-rw-r--r-- 1 root root  294 Jan  1 00:00 10-million-password-list-top-100.txt
-rw-r--r-- 1 root root 2.8K Jan  1 00:00 10-million-password-list-top-1000.txt
-rw-r--r-- 1 root root 2.0K Jan  1 00:00 top-passwords-shortlist.txt
...
```

**选型对照**：

| 场景 | 用哪个 |
| --- | --- |
| 在线爆破（[hydra](hydra.md) 等） | `top-100.txt`、`top-1000.txt`、`top-passwords-shortlist.txt` |
| 离线破解（[hashcat](hashcat.md)） | `10-million-password-list-top-1000000.txt` 或 rockyou |
| 用户名（多账号审计） | `Usernames/top-usernames-shortlist.txt` |
| Web 目录爆破 | `Discovery/Web-Content/directory-list-2.3-medium.txt` |
| 子域枚举 | `Discovery/DNS/subdomains-top1million-5000.txt` |

```bash
# 5) 与 hydra 串联
hydra -L /usr/share/seclists/Usernames/top-usernames-shortlist.txt \
      -P /usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-1000.txt \
      -t 4 -f \
      ssh://192.168.56.10
```

### 场景 4：自建与合并字典（把各类来源统一管理）

```bash
mkdir -p ~/wordlists-local

# 合并 + 去重 + 排序（按字母，方便 lookups）
cat /usr/share/wordlists/rockyou.txt \
    /usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt \
| sort -u > ~/wordlists-local/merged.txt

wc -l ~/wordlists-local/merged.txt

# 追加自建内容（CeWL 的输出、crunch 输出、组织相关词）
cat ~/site-words.txt >> ~/wordlists-local/merged.txt
sort -u -o ~/wordlists-local/merged.txt ~/wordlists-local/merged.txt

# 记录来源与日期（审计留痕）
cat > ~/wordlists-local/README.md <<'EOF'
# 本地字典集合
- merged.txt：rockyou + top-1M 合并去重
- 生成时间：2026-09-15
- 用途：仅用于自有靶场口令强度自查
EOF
```

### 场景 5：处理编码与非英文口令

```bash
# 检测字典编码
file /usr/share/wordlists/rockyou.txt
# UTF-8 Unicode text

# 从 GBK 转换到 UTF-8
iconv -f GBK -t UTF-8 cn-dict-gbk.txt > cn-dict-utf8.txt

# 去除无效字节（容错转换）
iconv -f UTF-8 -t UTF-8 -c in.txt > out.txt

# 找出含非 ASCII 的行
grep -P '[^\x00-\x7F]' /usr/share/wordlists/rockyou.txt | head
```

**对 hashcat**：用 `--encoding-from` / `--encoding-to` 显式指定，比手工转换更保险。

## 6. 输出解读

`wordlists -h` 的输出（见第 2.2 节）就是**目录清单**：

| 行样式 | 含义 |
| --- | --- |
| `/usr/share/wordlists/` 开头的一行 | 目录根 |
| `名字 -> /真实/路径` | **软链接**指向真实字典 |
| `名字`（无箭头） | **实体文件** |

**判断一个字典是否可用**：

```bash
# 1) 链接是否还有效
ls -lL /usr/share/wordlists/dirb/ 2>&1 | head -3
# 若报 No such file or directory → 对应的包没装

# 2) 文件是否非空
find /usr/share/wordlists -type f -size 0 2>/dev/null | head

# 3) 行数
wc -l /usr/share/wordlists/rockyou.txt
```

## 7. 与其他工具配合

字典是**所有口令攻击工具的公共输入**：

```text
/usr/share/wordlists/rockyou.txt
        ├─→ hydra -P          在线爆破
        ├─→ medusa -P         多目标在线爆破
        ├─→ ncrack -P         大规模在线审计
        ├─→ john --wordlist   离线破解
        ├─→ hashcat -a 0      离线 GPU 破解
        └─→ aircrack-ng -w    WPA 握手包破解

pw-inspector（hydra 包）  →  按目标策略裁剪字典
dpl4hydra（hydra 包）     →  厂商默认口令表
cewl                      →  组织相关词表
crunch                    →  结构化字典
CeWL 输出 + rockyou 合并  →  最强定向字典
```

**组合策略示例**：

```bash
# 在线先小后大
hydra -l admin -P ~/top1000.txt -f ssh://target           # 先几十秒
hydra -l admin -P ~/top10k.txt  -f ssh://target           # 再几分钟

# 离线全量
hashcat -m 1000 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt -O
hashcat -m 1000 -a 0 hashes.txt ~/wordlists-local/merged.txt -r rules/best64.rule
```

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| `hydra … -P /usr/share/wordlists/rockyou.txt` 报文件不存在 | **没解压**，只有 `rockyou.txt.gz` | `sudo gunzip /usr/share/wordlists/rockyou.txt.gz` |
| 工具读字典时输出乱码 / 0 命中 | 直接把 `.gz` 当文本读了 | 解压，或用 `zcat` 管道 |
| `/usr/share/wordlists/dirb` 存在但为空 | 软链接指向的包（`dirb`）没装 | `sudo apt install dirb` |
| 找不到 `seclists` | 未安装 | `sudo apt install seclists` |
| `gunzip` 后 `.gz` 消失了 | gunzip 默认删除源文件 | 用 `gzip -dk` 或 `gunzip -c > file` |
| 字典太大，在线爆破跑不完 | 用错了层 | 在线用 top-1000/top-10k；全量留给离线 [hashcat](hashcat.md) |
| 用目录字典爆破了登录口 | 字典**类别选错** | 登录口令用 `Passwords/`，目录用 `Discovery/Web-Content/` |
| 中文口令全都试不出来 | 字典是英文 | 找中文口令表；检查编码（`iconv`）；hashcat 用 `--encoding-from` |
| 磁盘满 | SecLists 体积大 | `df -h`；只 clone 需要的目录；`apt clean` |
| 合并字典里有重复导致浪费时间 | 未去重 | `sort -u` |
| rockyou 里也跑不出正确口令 | rockyou 是 2009 年的样本，且是英文为主 | 用 [cewl](cewl.md) 造组织相关字典 + [crunch](crunch.md) 加结构 + hashcat 规则变形 |

## 9. 防御视角（蓝队）

字典本身是「**已知泄露口令的集合**」，这让蓝队的工作变得非常直接：

| 措施 | 做法 |
| --- | --- |
| **拒绝已泄露口令** | 注册/改密时对候选口令做黑名单检查：`grep -Fxq "$newpass" /usr/share/wordlists/rockyou.txt`（实际部署用哈希索引或 HIBP k-Anonymity API 更好） |
| **拒绝高频口令** | 至少拒绝 Top 1000 / Top 10k：`grep -Fxq "$pw" seclists/Passwords/Common-Credentials/10-million-password-list-top-1000.txt` |
| **拒绝组织相关词汇** | 把公司名、产品名、品牌词加入黑名单（这也正对应 [cewl](cewl.md) 的攻击面） |
| **降低在线爆破成功率** | MFA + 失败锁定 + 速率限制 + 验证码 |
| **降低离线破解成功率** | bcrypt/scrypt/Argon2 + 长口令（≥ 12，管理员 ≥ 16） |
| **定期自查** | 用同样的字典审计自己（**需先获得内部授权**），发现弱口令立即整改 |

### 一个可落地的口令校验脚本思路

```bash
#!/usr/bin/env bash
# 说明：仅用于自有系统的口令策略校验。需要 root 权限读取字典。
set -euo pipefail
PW="$1"
BLACKLISTS=(
  /usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-1000.txt
  /usr/share/wordlists/rockyou.txt
)
if [ "${#PW}" -lt 12 ]; then echo "拒绝：长度小于 12"; exit 1; fi
for f in "${BLACKLISTS[@]}"; do
  [ -r "$f" ] || continue
  if grep -Fxq -- "$PW" "$f"; then echo "拒绝：出现在已知泄露口令库中"; exit 1; fi
done
echo "通过"
```

**为什么不直接用 grep**：1400 万行逐行 grep 太慢。生产环境应把黑名单预计算成哈希集合（如 Bloom filter 或数据库索引），或用 HIBP 的 k-Anonymity 接口（只发送口令 SHA-1 的前 5 位）。

### 检测：攻击者正在用字典爆破

| 信号 | 说明 |
| --- | --- |
| 登录失败序列**按常见口令顺序**推进 | 例如失败的用户名/口令尝试呈现出 Top-N 列表的**固定次序**——这是字典攻击的强特征 |
| 同一 IP 对多个账号的失败 | 口令喷洒，见 [hydra](hydra.md) 蓝队章节 |
| 失败请求的 User-Agent / 时序固定 | 自动化工具的典型特征 |

**蓝队核心结论**：

> rockyou 的存在意味着**任何出现在它里面的口令都等于没有口令**。所以口令策略的第一条就是「拒绝已泄露口令」——这比「必须含大小写数字」这类复杂度规则有效得多。

## 10. 参考

- Kali wordlists 工具页：<https://www.kali.org/tools/wordlists/>
- Kali seclists 工具页：<https://www.kali.org/tools/seclists/>
- SecLists 官方仓库：<https://github.com/danielmiessler/SecLists>
- 本机命令：`wordlists -h`（打印目录树）、`man wordlists`
- 相关：[hydra](hydra.md)（`pw-inspector`、`dpl4hydra` 同包）、[hashcat](hashcat.md)、[john](john.md)、[crunch](crunch.md)、[cewl](cewl.md)

## ⚠️ 法律与伦理

字典本身是公开数据，**持有和阅读字典完全合法**。但《中华人民共和国网络安全法》第二十七条禁止任何「危害网络安全」的活动；《刑法》第二百八十五条对「非法侵入计算机信息系统」「非法获取计算机信息系统数据」有明确刑事责任。**把字典用于对未授权目标的口令破解，即构成上述违法/犯罪行为。**

特别提醒：

- 不要把公司/客户的口令字典带离授权范围；
- 不要用「公开泄露的口令库」去撞库任何真实服务（「撞库」在多数司法辖区明确违法）；
- **本教程仅适用于**：自有系统的口令强度自查、有书面授权的渗透测试、CTF 靶场、教学演示。
