# hack-learn · 网络安全与系统学习库

一个按模块组织的中文学习库：**Kali Linux**、**Web 与安全标准**、**Linux 系统**、**Linux 内核**。
每个模块包含三类内容——**知识文档**（讲清楚）、**命令/工具手册**（查得到）、**练习与靶场**（动手做）。

> ⚠️ 本库所有攻击性内容仅用于**授权测试、CTF 竞赛、自有靶场与防御研究**。
> 未经授权对他人系统进行扫描或入侵在多数司法辖区（含中国大陆）构成违法。

---

## 模块导航

| 模块 | 目录 | 规模 | 从哪开始 |
|------|------|------|----------|
| **Kali Linux** | [`kali/`](kali/README.md) | **780 个工具包**（每个一份参考文档）· 501 条命令条目 · 16 个功能分类 · 270 篇官方文档精读（13 篇）· 108 篇精讲教程 | [kali/README.md](kali/README.md) |
| **Web 与安全标准** | [`web-security/`](web-security/README.md) | OWASP Top 10 **2025** + WSTG · ATT&CK · PTES · Exploit-DB · CWE Top 25 **2025** · NIST SP 800 | [web-security/README.md](web-security/README.md) |
| **Linux 系统** | [`linux/`](linux/README.md) | 8 篇基础 · **335 个命令**（14 类）· **155 道练习** + 15 个排障场景 | [linux/README.md](linux/README.md) |
| **Linux 内核** | [`kernel/`](kernel/README.md) | 7 篇内核文档 · 本地内核源码（Linux 7.3.0-rc3）· 20 个实验 | [kernel/README.md](kernel/README.md) |
| **工具与数据** | [`scripts/`](scripts/README.md) · [`data/`](data/) | 10 个数据同步 / 索引生成 / 校验脚本 · 结构化数据 | [scripts/README.md](scripts/README.md) |

### Kali Linux 模块内部结构

```
kali/
├── docs/          官方文档精读（13 篇）+ 全量官方索引（270 篇）
├── tools/
│   ├── index.md       工具总导航（按攻击阶段 / 按包 两种查法）
│   ├── by-attack/     16 个功能分类的工具清单（ATT&CK 战术风格）
│   ├── catalog/       780 个包的速查卡片
│   ├── reference/     780 个包各一份参考文档（安装/官方示例/参数原文/实践清单）
│   └── tutorials/     108 篇重点工具精讲教程（含靶场实操）
└── labs/          靶场搭建（DVWA / Juice Shop / Metasploitable / GOAD …）
```

---

## 三条学习路线

### 路线 A · Web 安全工程师
```
linux/basics（文件/权限/网络）
  → web-security/owasp（Top 10 2025 漏洞原理）
  → web-security/wstg（测试方法论与清单）
  → kali/labs（起 DVWA / Juice Shop 靶场）
  → kali/tools/tutorials/03-Web应用（sqlmap / ffuf / burp 等）
  → web-security/cwe（把发现归类到弱点）
  → web-security/nist（用 SP 800-115 规范评估流程）
```

### 路线 B · 渗透测试 / 红队
```
kali/README（安装与环境）
  → kali/tools/by-attack（按攻击阶段认识工具）
  → web-security/ptes（流程规范与交付物模板）
  → web-security/mitre-attack（把动作映射到 TTP）
  → web-security/exploit-db（检索与使用公开 EXP）
  → kali/labs（靶场串联成完整演练）
```

### 路线 C · 系统 / 内核方向
```
linux/commands（工具链与系统调用）
  → kernel/README（源码结构、构建、调试）
  → kernel/docs/03-内核模块开发
  → kernel/src/linux（源码阅读，配 kernel/docs/02 的阅读方法）
```

---

## 快速开始

```bash
# 1. 看 Kali 工具怎么查（四种查法：按攻击阶段 / 按包 / 参考文档 / 精讲教程）
less kali/tools/index.md

# 1b. 想直接开始用某个工具（780 个包都有参考文档）
less kali/tools/reference/nmap.md

# 2. 搜一个工具（TSV 比 Markdown 好搜）
grep -i 'sqlmap' data/kali-tools.tsv

# 3. 刷新官方数据（可选，仓库里已包含抓好的数据）
python3 scripts/fetch_kali_tools.py --workers 6   # 780 个工具页面
python3 scripts/fetch_kali_categories.py          # 16 个功能分类
python3 scripts/fetch_kali_docs.py --workers 6    # 270 篇官方文档
python3 scripts/gen_kali_index.py                 # 重新生成索引

# 4. 校验文档链接
python3 scripts/check_links.py --anchors

# 5. 拉取内核源码（若 kernel/src/linux 不存在）
bash scripts/fetch_linux_kernel.sh
```

只依赖 **Python 3 标准库**，不需要 pip 安装任何东西。

---

## 内容是怎么保证准确的

本库不靠"凭记忆抄写"，而是：

| 手段 | 做法 |
|------|------|
| **官方数据同步** | Kali 工具元数据、功能分类树、官方文档大纲全部由 `scripts/` 下的脚本从官网抓取，可随时复现 |
| **附源链接** | 每篇文档都列出实际访问过的官方 URL，可回源核对 |
| **本地实测** | 内核篇的版本号、文件路径、函数行号均在本机源码树上实测（如 Linux 7.3.0-rc3） |
| **链接校验** | `scripts/check_links.py` 校验全库相对链接与锚点，防止文档漂移 |
| **不确定就标注** | 无法核实的编号、参数、章节会显式标注 `⚠️ 待核实`，不做推测 |

---

## 文档约定

统一模板，方便横向跳转与查漏：

- **工具/命令文档**：它解决什么问题 → 工作原理 → 语法与参数 → 实战演练 → 输出解读 → 常见坑 → 防御视角
- **练习**：目标 → 环境 → 步骤 → 验证 → 挑战题
- **风险标记**：

| 标记 | 含义 |
|------|------|
| ⚠️ | 高风险操作或法律红线（如 `dd` 写盘、`luksFormat`、`PermitRootLogin yes`） |
| 💡 | 提效技巧或容易被忽略的用法 |
| 🔬 | 原理层深入（为什么是这样） |
| 🧪 | 实验与练习 |
| 🔐 | 与安全测试/取证相关的用法 |
| 🔗 | 外部权威链接 |

---

## 外部权威资源

| 名称 | 说明 | 地址 |
|------|------|------|
| Kali 工具文档 | 全量工具说明 | <https://www.kali.org/tools/> |
| Kali 官方文档 | 安装、配置、使用 | <https://www.kali.org/docs/> |
| OWASP Top 10 | Web 应用十大风险（当前 **2025** 版） | <https://owasp.org/Top10/2025/> |
| OWASP WSTG | Web 安全测试指南 | <https://owasp.org/www-project-web-security-testing-guide/> |
| MITRE ATT&CK | 攻防战术与技术知识库（企业域 **15** 个战术） | <https://attack.mitre.org/> |
| CWE | 软件弱点分类字典（Top 25 当前 **2025** 版） | <https://cwe.mitre.org/> |
| NIST SP 800 | 美国 NIST 安全规范（如 SP 800-115 测试评估指南） | <https://csrc.nist.gov/publications/sp800> |
| Exploit Database | 公开 PoC / Exploit 库 | <https://www.exploit-db.com/> |
| PTES | 渗透测试执行标准（7 阶段） | <http://www.pentest-standard.org/> |
| Linux 内核 | 主线源码与官方文档 | <https://www.kernel.org/> · <https://docs.kernel.org/> |

---

## 免责声明

本仓库内容用于安全学习、授权渗透测试与防御建设。
使用者须自行确保对目标拥有合法授权。作者不对任何滥用行为承担责任。

法律风险提示见 [kali/docs/13-政策法规与社区.md](kali/docs/13-政策法规与社区.md) 与
[web-security/ptes/](web-security/ptes/) 中的授权书（SOW）模板。
