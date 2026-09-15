# Kali Linux 学习模块

Kali Linux 是 Debian 派生的、面向渗透测试与安全审计的发行版，预装 600+ 安全工具，并维护了完整的 [官方工具文档](https://www.kali.org/tools/) 与 [官方使用文档](https://www.kali.org/docs/)。

本模块把这两套官方资料**本地化、结构化**，并补上官方没有的**实操练习**。

---

## 目录结构

```
kali/
├── README.md              本文件：学习总纲
├── docs/                  ① Kali 官方文档精读手册（中文）
│   ├── official-index.md     官方 270 篇文档的全量索引（自动同步）
│   ├── 01-...md              分主题精读笔记（13 篇）
│   └── ...
├── tools/                 ② Kali 工具库
│   ├── index.md              工具总导航（按攻击阶段 + 按包 + 参考文档）
│   ├── by-attack/            按功能分类的工具清单（16 个分类 / 501 条命令）
│   ├── catalog/              按包速查卡片（780 个包全量）
│   ├── reference/            ★ 每个工具包一份参考文档（780 篇：安装 + 官方示例 + 参数原文 + 实践清单）
│   └── tutorials/            重点工具精讲教程（108 篇，含原理与靶场实操）
└── labs/                  ③ 靶场与实验环境
```

**四种查法怎么选**：

| 你想做什么 | 去哪 |
|------------|------|
| 按攻击阶段找工具（先侦察？要提权？） | [`tools/by-attack/`](tools/by-attack/) |
| 按包名看它是什么、装了有什么命令 | [`tools/catalog/`](tools/catalog/) |
| **从零开始用一个工具**（装 → 官方示例 → 参数 → 实践） | [`tools/reference/`](tools/reference/) |
| 把一个重点工具学透（原理 + 靶场实操 + 输出解读） | [`tools/tutorials/`](tools/tutorials/) |

---

## 三条学习路线

### 路线 1：零基础到能打 CTF（建议 4–8 周）
| 阶段 | 内容 | 入口 |
|------|------|------|
| 1 | 装好 Kali（虚拟机即可），熟悉终端与基本命令 | [`docs/02-安装与获取镜像.md`](docs/02-安装与获取镜像.md) |
| 2 | 搞懂 Kali 的包管理、非 root 策略、软件源 | [`docs/05-包管理与软件源.md`](docs/05-包管理与软件源.md) |
| 3 | 网络配置、代理、快照回滚 | [`docs/04-网络配置与代理.md`](docs/04-网络配置与代理.md) |
| 4 | 起靶场（DVWA / Juice Shop / Metasploitable） | [`labs/README.md`](labs/README.md) |
| 5 | 信息搜集 → Web 漏洞 → 简单利用 | [`tools/tutorials/01-信息搜集/`](tools/tutorials/01-信息搜集/) |
| 6 | 打 CTF：把工具串成流程 | [`tools/index.md`](tools/index.md) |

### 路线 2：渗透测试工程师（体系化）
```
侦察(Reconnaissance) → 资源开发 → 初始访问 → 执行 → 持久化 → 提权
→ 防御规避 → 凭据访问 → 发现 → 横向移动 → 收集 → C2 → 数据外泄 → 影响
```
每个阶段对应的 Kali 工具清单在 [`tools/by-attack/`](tools/by-attack/)。流程规范见 [`../web-security/ptes/README.md`](../web-security/ptes/README.md)，技术映射见 [`../web-security/mitre-attack/README.md`](../web-security/mitre-attack/README.md)。

### 路线 3：蓝队 / 取证方向
`tools/by-attack/forensics.md` + [`tools/tutorials/09-数字取证/`](tools/tutorials/09-数字取证/) + [`tools/by-attack/services-and-other-tools.md`](tools/by-attack/services-and-other-tools.md)

---

## 环境准备：选哪种安装方式

| 方式 | 适合 | 优点 | 缺点 | 官方文档 |
|------|------|------|------|----------|
| **虚拟机（VirtualBox/VMware）** | 初学者、日常练习 | 可快照回滚、隔离好、支持几乎所有工具 | 无线与硬件攻击受限 | [virtualization](https://www.kali.org/docs/virtualization/) |
| **Live USB** | 物理机测试、取证 | 不落地、可直接跑硬件工具 | 性能受 U 盘限制 | [usb](https://www.kali.org/docs/usb/) |
| **裸机安装** | 长期使用、需要无线注入 | 性能最好、硬件全支持 | 破坏性操作，需谨慎双系统 | [installation](https://www.kali.org/docs/installation/) |
| **WSL2** | 只想用命令行工具链 | 启动快、与 Windows 互通 | 无 GUI（可配 WSLg）、无无线 | [wsl](https://www.kali.org/docs/wsl/) |
| **Docker** | 快速起单个工具 | 秒级启动、轻量 | 隔离与内核特性受限 | [containers](https://www.kali.org/docs/containers/) |
| **云主机 / 浏览器版** | 临时使用、无本地资源 | 随处可用 | 计费、无内网可达性 | [cloud](https://www.kali.org/docs/cloud/) |

**给初学者的建议**：先在虚拟机里装 Kali（分配 ≥ 4 核 / 8 GB 内存 / 80 GB 磁盘），
并**立刻打一个快照**；所有破坏性实验都在快照之后做，出问题直接回滚。

---

## 必须知道的三件事

### 1. Kali 默认不让你用 root 登录
自 2020.1 起，Kali 安装后创建普通用户（Live/预置镜像默认 `kali` / `kali`），root 账户**没有设置密码**、直接登录被禁用。
需要管理员权限时用 `sudo`，输入的是**当前用户**的密码：

```bash
sudo -i            # 切到 root shell（需要输入当前用户密码）
sudo -l            # 看当前用户能执行哪些 sudo 命令
sudo command ...   # 只给这一条命令提权（推荐）
```

如果想免密（⚠️ 一旦该账号被拿下，等于直接丢 root）：
```bash
sudo apt install -y kali-grant-root && sudo dpkg-reconfigure kali-grant-root
```

🔗 官方说明：<https://www.kali.org/docs/general-use/sudo/> · [本地笔记](docs/03-系统配置与优化.md#1-非-root-策略与-sudo)

### 2. 工具是"元包（metapackage）"组织的
`kali-linux-default`、`kali-linux-large`、`kali-linux-everything` 是元包，
安装它们等于批量安装一批工具；`kali-tools-*` 是按功能拆分的元包。

```bash
apt list --installed 'kali-tools*' 2>/dev/null   # 看装了哪些工具集
sudo apt install -y kali-tools-web               # 只装 Web 相关工具集
```

🔗 官方：<https://www.kali.org/docs/general-use/metapackages/>

### 3. 法律边界
Kali 里的工具本身是合法的通用软件，**但未经授权对他人系统使用即违法**。
- 只测试：自己的设备、自有靶场、明确书面授权的目标、公开允许测试的目标（如 `scanme.nmap.org`）。
- 在中国大陆，相关行为可能触犯《刑法》第 285/286 条与《网络安全法》。
- 练习请用 [`labs/`](labs/README.md) 里的本地靶场。

🔗 官方政策：<https://www.kali.org/docs/policy/>

---

## 本模块文件索引

- [`docs/official-index.md`](docs/official-index.md) —— 官方 270 篇文档全量索引（自动同步）
- [`tools/index.md`](tools/index.md) —— 工具总导航
- [`tools/reference/README.md`](tools/reference/README.md) —— **780 个工具包的参考文档**
- [`tools/tutorials/README.md`](tools/tutorials/README.md) —— 108 篇精讲教程目录
- [`labs/README.md`](labs/README.md) —— 靶场与环境搭建
