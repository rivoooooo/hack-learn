# 04 · 口令攻击（Password Attacks）

本目录覆盖 Kali 中与口令攻击（Credential Access / Password Cracking / Brute Force / Password Profiling & Wordlists）相关的工具教程。

**核心心智模型**：先分清**在线爆破**与**离线破解**——这决定了工具选择、字典策略和速度预期。

```text
                    在线爆破（走网络，慢）
                    hydra / medusa / ncrack / patator
                              ↓ 拿到入口
                    dump 出哈希（unshadow / secretsdump / zip2john …）
                              ↓
                    离线破解（本地算力，快几个数量级）
                    john / hashcat / ophcrack
```

## 工具清单

| 工具 | 一句话 | 难度 | 教程 |
| --- | --- | --- | --- |
| `wordlists` / `seclists` | Kali 字典库位置、rockyou 解压、SecLists 目录结构 | ★ | [wordlists.md](wordlists.md) |
| `hash-identifier` | 从长度与字符集推断哈希类型 | ★ | [hash-identifier.md](hash-identifier.md) |
| `hydra` | 在线登录爆破，50+ 协议，上手最快 | ★★ | [hydra.md](hydra.md) |
| `medusa` | 多主机 × 多用户 × 多口令的并行登录爆破 | ★★ | [medusa.md](medusa.md) |
| `ncrack` | Nmap 风格的认证爆破，带时序模板与断点续跑 | ★★ | [ncrack.md](ncrack.md) |
| `patator` | 模块化万能爆破：登录、枚举、模糊测试 | ★★★ | [patator.md](patator.md) |
| `crunch` | 按字符集/模式/长度规则生成定向字典 | ★★ | [crunch.md](crunch.md) |
| `cewl` | 爬站生成组织相关词表与用户名字典 | ★★ | [cewl.md](cewl.md) |
| `john` | 离线哈希破解，上百个 `*2john` 格式转换器 | ★★ | [john.md](john.md) |
| `hashcat` | GPU 加速离线破解，300+ 哈希算法 | ★★★ | [hashcat.md](hashcat.md) |
| `ophcrack` | 用彩虹表秒破解 Windows LM/NTLM 弱口令 | ★★ | [ophcrack.md](ophcrack.md) |

## 学习顺序

**第 1 步 · 打地基（先搞懂「弹药」和「目标」）**

1. [wordlists.md](wordlists.md) —— 字典从哪来。不做这一步，后面所有工具都没法跑。
2. [hash-identifier.md](hash-identifier.md) —— 拿到哈希先看清它是什么。

**第 2 步 · 在线爆破（最快见效）**

3. [hydra.md](hydra.md) —— 从 SSH 单目标开始，掌握 `-l/-P/-e/-f` 这套最小配置。
4. [crunch.md](crunch.md) —— 学完 hydra 会立刻需要「定向字典」，此时学 crunch 最合适。
5. [cewl.md](cewl.md) —— 把「定向」从「字符结构」扩展到「组织词汇」。
6. [medusa.md](medusa.md) —— 目标从 1 台扩展到 1 个网段。
7. [ncrack.md](ncrack.md) —— 需要精细时序控制与 Nmap 联动时。
8. [patator.md](patator.md) —— 遇到非标准认证流程时的终极武器。

**第 3 步 · 离线破解（真正的效率战场）**

9. [john.md](john.md) —— 先掌握「提取 → 破解」这套流程与攻击模式。
10. [hashcat.md](hashcat.md) —— 把 john 的活交给 GPU 跑，速度提升几个数量级。
11. [ophcrack.md](ophcrack.md) —— 理解彩虹表这一条完全不同的技术路线。

**第 4 步 · 串起来**

回到本 README 开头的流程图，把「在线拿入口 → dump 哈希 → 离线扩大战果」跑通一遍。

## 环境准备

### 硬件

| 项 | 说明 |
| --- | --- |
| CPU | 8 核以上体验更好（john `--fork`、ophcrack `-n`） |
| **GPU** | **hashcat 的核心**。NVIDIA 最好（CUDA 生态完善），AMD 需 ROCm/HIP。集显也能跑但慢 |
| 磁盘 | 字典 + 彩虹表可能占几十 GB。SecLists 1~2 GB，Ophcrack 免费表数 GB |
| 内存 | hashcat 大字典/大掩码会吃显存；Ophcrack `-p 3` 会吃内存 |

**GPU 环境检查**：

```bash
hashcat -I                    # 看有没有识别到设备
hashcat -b -m 0               # 跑一次基准测试，确认能真正用上 GPU
```

如果 `-I` 里没有 GPU，需要装显卡驱动 + OpenCL 运行时：

```bash
# NVIDIA
sudo apt install nvidia-driver nvidia-opencl-icd
# AMD
sudo apt install mesa-opencl-icd
# 纯 CPU（慢，但可用）
sudo apt install pocl-opencl-icd
```

### 工具安装

```bash
sudo apt install hydra medusa ncrack patator crunch cewl \
                 john hashcat hash-identifier ophcrack ophcrack-cli \
                 wordlists seclists
```

**必做的一件事** —— 解压 rockyou：

```bash
sudo gunzip /usr/share/wordlists/rockyou.txt.gz
wc -l /usr/share/wordlists/rockyou.txt     # 14344392
```

没有这一步，你的 hydra/john/hashcat 命令全都会报「字典不存在」。

### 靶机与练习环境

**法律前提**：以下所有环境都是**你自己搭建的**，或在**明确授权的 CTF 平台**上使用。**绝不对任何未授权目标使用本目录的任何工具。**

| 靶场 | 适合练什么 | 获取方式 |
| --- | --- | --- |
| **Metasploitable 2** | SSH/FTP/MySQL 弱口令，`/etc/shadow` 提取 | 官方 ISO，导入 VirtualBox |
| **Metasploitable 3** | Windows 侧：SMB、WinRM、SAM 哈希 | Vagrant |
| **DVWA** | HTTP 表单爆破（[hydra](hydra.md) `http-post-form`）、口令策略实验 | Docker 一键部署 |
| **OWASP Juice Shop** | 现代 Web 登录、JWT | Docker / npm |
| **VulnHub 系列** | 综合靶机，含口令攻击环节 | 官方镜像 |
| **HackTheBox / TryHackMe** | 有授权的在线靶场 | 需注册，遵守平台规则 |
| **自建 Windows 虚拟机** | SAM 导出、Ophcrack 彩虹表演示 | 自己安装，自己设口令 |
| **自建 Kali 攻击机** | 所有工具的演练平台 | 官方 ISO |

**推荐的最小组合（够练完本目录所有内容）**：

```text
VirtualBox Host-Only 网络 192.168.56.0/24
├── Kali Linux（攻击机）
├── Metasploitable 2（Linux 目标，练 hydra/medusa/ncrack/john）
└── Windows 10 虚拟机（练 ophcrack / NTLM）
    └── 自己创建测试账户，口令设为弱口令（如 pass123 / password / qwerty12345）
```

**部署示例（DVWA，用于练 hydra 的 HTTP 表单爆破）**：

```bash
docker run --rm -it -p 80:80 vulnerables/web-dvwa
# 浏览器访问 http://127.0.0.1 并完成 setup，安全等级设为 low
```

### 字典准备

```bash
# 1) 解压 rockyou（必做）
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# 2) 建立分层字典（在线用小、离线的用大）
head -1000  /usr/share/wordlists/rockyou.txt > ~/top1000.txt
head -10000 /usr/share/wordlists/rockyou.txt > ~/top10k.txt

# 3) 安装 SecLists
sudo apt install seclists
ls /usr/share/seclists/Passwords/Common-Credentials/ | head

# 4) 确认目录结构
wordlists -h
```

**选字典的铁律**：

| 场景 | 用多大的字典 |
| --- | --- |
| 在线爆破（hydra/medusa/ncrack/patator） | Top 100 ~ Top 10k。**20 万条以上的字典在线跑不完** |
| 离线破解（john/hashcat） | rockyou 全量、SecLists、自建合并字典 |
| 有结构情报 | 用 [crunch](crunch.md) 定向生成 |
| 有组织情报 | 用 [cewl](cewl.md) 爬取 |

## 速度的现实预期

写进报告的数字必须来自**你自己的基准测试**：

```bash
# CPU 侧
john --test=5 --format=sha512crypt
john --test=5 --format=bcrypt

# GPU 侧
hashcat -b -m 0        # MD5
hashcat -b -m 1000     # NTLM
hashcat -b -m 1800     # sha512crypt
hashcat -b -m 3200     # bcrypt
```

**不同算法的差距是数量级级别的**，这条规则决定了一切策略：

| 算法 | 相对速度 | 策略含义 |
| --- | --- | --- |
| MD5 / NTLM（无盐、快） | 极快 | 大字典随便跑 |
| SHA-1 / SHA-256 | 快 | 字典 + 规则 |
| md5crypt / sha512crypt | 慢千倍量级 | **只跑小字典**（Top 10k + 规则） |
| bcrypt / scrypt / Argon2 | 慢多个数量级 | **只跑 Top 1000 + 精确规则**，大字典不现实 |

**在线爆破的现实**：

```
预计耗时 = 字典行数 × 每个用户 × 用户名数 ÷ 每秒尝试次数
局域网 SSH 每秒几十~几百次；跨公网低一个数量级
```

先算这个数，再决定用多大的字典——**不要跑一晚上才发现字典选大了**。

## 法律与伦理（必读）

本目录所有工具都**只能用于**：

- ✅ 你自己拥有的系统、网络、账号
- ✅ 有**书面授权**（SOW / ROE）的渗透测试与合规审计
- ✅ CTF 竞赛靶场
- ✅ 为学习搭建的隔离实验环境

**严禁用于**：

- ❌ 任何未授权的主机、网络、账号、服务
- ❌ 「撞库」任何真实服务（多数司法辖区明确违法）
- ❌ 破解他人提供的、来源不明的哈希
- ❌ 超出授权范围的一台设备、一个端口、一次尝试

**相关法律责任**（中国大陆）：

| 法律 | 条款 | 行为 |
| --- | --- | --- |
| 《刑法》 | 第二百八十五条第一款 | 非法侵入国家事务、国防建设、尖端科学技术领域的计算机信息系统 |
| 《刑法》 | 第二百八十五条第二款 | 非法获取计算机信息系统数据、非法控制计算机信息系统 |
| 《刑法》 | 第二百八十六条 | 破坏计算机信息系统 |
| 《网络安全法》 | 第二十七条 | 禁止任何危害网络安全的活动 |
| 《数据安全法》 | 相关条款 | 数据处理活动的合规要求 |

可判处有期徒刑。**授权以书面为准，超出范围即违法**。

## 相关目录

- [05 · 无线攻击](../05-无线攻击/README.md) —— WPA 握手包抓取与破解（与 [hashcat](hashcat.md) `-m 22000` 衔接）
- [07 · 嗅探与欺骗](../07-嗅探与欺骗/README.md) —— [responder](../07-嗅探与欺骗/responder.md) 抓 NetNTLM 哈希后交给 [hashcat](hashcat.md) `-m 5600`

## 参考

- Kali 工具分类总览：<https://www.kali.org/tools/>
- Kali 元包（metapackages）：<https://www.kali.org/docs/general-use/metapackages/>
- 本仓库工具清单来源：`data/kali-tools.tsv`、`data/kali-tools.json`
