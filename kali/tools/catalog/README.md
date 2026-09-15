# 按包速查卡片

本目录收录 Kali 官方文档中的**全部 780 个工具包**，每个包一张卡片。

## 卡片里有什么

描述 · 功能分类 · 版本 · **包名与可执行命令** · 依赖 · 安装命令 · 占用空间 · 官网 · 源码仓库 · Kali 文档链接

## 目录清单

按"包所属的元包分组"分文件：

| 文件 | 分组 | 包数 |
|------|------|------|
| [`all-tools.md`](all-tools.md) | **全量 A–Z 平铺清单** | 780 |
| [`information-gathering.md`](information-gathering.md) | 信息搜集 | 91 |
| [`vulnerability.md`](vulnerability.md) | 漏洞分析 | 38 |
| [`web.md`](web.md) | Web 应用 | — |
| [`passwords.md`](passwords.md) | 口令攻击 | — |
| [`wireless.md`](wireless.md) | 无线攻击 | — |
| [`sniffing-spoofing.md`](sniffing-spoofing.md) | 嗅探与欺骗 | — |
| [`exploitation.md`](exploitation.md) | 漏洞利用 | — |
| [`post-exploitation.md`](post-exploitation.md) | 后渗透 | — |
| [`forensics.md`](forensics.md) | 数字取证 | — |
| [`reverse-engineering.md`](reverse-engineering.md) | 逆向工程 | — |
| [`crypto-stego.md`](crypto-stego.md) | 密码学与隐写 | — |
| [`hardware.md`](hardware.md) | 硬件攻击 | — |
| [`identify.md`](identify.md) | 识别与指纹 | — |
| [`detect.md`](detect.md) | 检测 | — |
| [`protect.md`](protect.md) | 防护 | — |
| [`reporting.md`](reporting.md) | 报告与记录 | — |
| [`respond.md`](respond.md) | 事件响应 | — |
| [`top10.md`](top10.md) | Top 10 常用 | — |
| [`windows-resources.md`](windows-resources.md) | Windows 资源 | — |
| [`utils.md`](utils.md) | 通用工具 | — |

> 具体包数用 `grep -c '^### ' kali/tools/catalog/<文件>.md` 查看；
> 各文件顶部也标注了本组包数。

**为什么会话有些元包没有独立文件**：一个包常同时属于多个元包分组
（例如 `aircrack-ng` 同时属于 `wireless`、`802-11`、`exploitation` 等）。
为避免同一个包在十几个文件里重复出现，卡片只归入**排序最靠前的那一个分组**，
因此像 `802-11`、`bluetooth`、`rfid`、`voip`、`database`、`gpu`、`social-engineering`
这些分组会被邻近的更靠前分组吸收。

想看**跨分组**的完整视角，用另外两种查法：

- 按攻击阶段：[`../by-attack/`](../by-attack/)
- 扁平数据：`data/kali-tools.tsv`（字段含 `package_group` 与 `attack_category`）

---

## 两种分类体系的区别

| 目录 | 组织方式 | 适合 |
|------|----------|------|
| `catalog/`（本目录） | 按**包**（一个包一张卡） | 已知工具名，想查它属于哪个包、有哪些命令、怎么装 |
| [`../by-attack/`](../by-attack/) | 按**攻击阶段**（ATT&CK 风格 16 个分类，501 条命令级条目） | 想按"我现在要做侦察/提权"来找工具 |
| [`../index.md`](../index.md) | 两种查法的总入口 | 第一次来，不知道从哪下手 |

---

## 更快的搜索方式

Markdown 不方便 grep，用扁平数据文件：

```bash
# 按工具名搜
grep -i 'sqlmap' data/kali-tools.tsv

# 按描述搜
grep -i 'kerberos' data/kali-tools.tsv | cut -f1,2

# 按包分组列全部
awk -F'\t' '$3=="passwords" {print $2}' data/kali-tools.tsv

# 按 ATT&CK 分类列全部
awk -F'\t' '$4=="凭据访问" {print $2}' data/kali-tools.tsv
```

字段：`slug` · `name` · `package_group` · `attack_category` · `packages` · `description` · `url`

从包名查可执行命令：

```bash
awk -F'\t' '$1=="nmap" {print $5}' data/kali-tools.tsv | tr ',' '\n'
```

---

## 数据来源与重新生成

- 原始数据：<https://www.kali.org/tools/all-tools/>
- 生成脚本：

```bash
python3 scripts/fetch_kali_tools.py --workers 6   # 抓取（约 1–2 分钟）
python3 scripts/gen_kali_index.py                 # 生成本目录
```

详细说明见 [`scripts/README.md`](../../../scripts/README.md)。
