# 01 · Kali 介绍与版本选择

> 对应官方章节：<https://www.kali.org/docs/introduction/>（12 篇）
> 本篇回答三个问题：Kali 是什么、该不该用它、该下哪个镜像。

---

## 本节速览

| 官方文档 | 中文要点 |
|----------|----------|
| [What is Kali Linux?](https://www.kali.org/docs/introduction/what-is-kali-linux/) | 定位、特性、与 BackTrack 的渊源 |
| [Should I Use Kali Linux?](https://www.kali.org/docs/introduction/should-i-use-kali-linux/) | 三个关键设计差异；**谁不该用 Kali** |
| [Which Image Should I Download?](https://www.kali.org/docs/introduction/what-image-to-download/) | Installer / NetInstaller / Live / Everything 的区别 |
| [Kali Linux Image Overview](https://www.kali.org/docs/introduction/kali-linux-image-overview/) | 全平台镜像矩阵（安装 / 虚拟机 / 云 / 容器 / USB / ARM / 移动端） |
| [Kali's Default Credentials](https://www.kali.org/docs/introduction/default-credentials/) | 系统与各工具的默认账号密码 |
| [Kali Linux History](https://www.kali.org/docs/introduction/kali-linux-history/) | BackTrack → Kali 的演进 |

---

## 1. Kali 是什么

Kali Linux 是一个开源的、基于 Debian 的发行版，用于**渗透测试与安全审计**。前身是 BackTrack Linux。

官方的自我定位很明确（[原文](https://www.kali.org/docs/introduction/what-is-kali-linux/)）：

> 这个发行版有数百个工具、配置和脚本，带有面向行业的定制修改，
> 让用户能专注于计算机取证、逆向工程、漏洞检测等任务，而不必处理无关的杂事。
>
> **本站所有文档都假定读者已具备 Linux 操作系统的先验知识与熟练度。**

关键特性（官方列举，逐条翻译并补充实践含义）：

| 官方特性 | 实践含义 |
|----------|----------|
| 永远免费 | 没有商业版限制 |
| 开源 Git 树 | 所有包的源码可获取、可重打包 |
| 遵循 FHS 文件系统层次标准 | 二进制在 `bin/`、库在 `lib/`、配置在 `/etc`，与普通 Linux 一致 |
| 广泛的硬件支持，尤其无线设备 | 支持大量 USB 无线网卡（注入能力） |
| **打过注入补丁的自定义内核** | 无线审计要用的注入（injection）能力来自这里 |
| 在安全环境中开发 | 提交者受信任、变更走安全协议 |
| GPG 签名的包与仓库 | 每个包由提交者签名，仓库再签一次 |
| 多语言支持 | 工具本身多为英文，但系统可中文化 |
| 完全可定制 | 从桌面到内核都能改 |

---

## 2. 三个最关键的设计决定

这一节是**理解 Kali 一切"怪异行为"的钥匙**（源自 [Should I Use Kali Linux?](https://www.kali.org/docs/introduction/should-i-use-kali-linux/)）：

### ① 默认禁用网络服务
Kali 内置了 systemd 钩子（hooks），**安装任何服务包都不会让它开机自启**。
蓝牙等服务还被直接加入 blocklist。

```bash
# 查看哪些服务被禁用/屏蔽
systemctl list-unit-files --state=disabled | head -30
systemctl status bluetooth     # 通常是 inactive
```

💡 这意味着你 `apt install apache2` 之后不要惊讶"怎么访问不了"，需要手动 `systemctl start apache2`。
这也是安全设计：避免一台测试机在不知情的情况下对外暴露一堆服务。

### ② 自定义内核（打了无线注入补丁）
上游内核 + 注入补丁。这是 Kali 相比 Ubuntu/Debian 做无线测试时的核心优势。

🔬 相关细节见 [06-内核与硬件驱动.md](06-内核与硬件驱动.md)。

### ③ 极小的可信上游仓库集合
Kali 只从极少数上游源取包。官方原文措辞很重：

> 很多新用户会忍不住往 `kali.sources`（或旧版 `sources.list`）里加仓库，
> 但这么做有**非常严重**的风险会让你的 Kali 安装彻底损坏。
>
> **完全不支持** `apt-add-repository`、LaunchPad、PPA。
> 想在 Kali 桌面上装 Steam 是一个不会有好结果的实验。

⚠️ **结论：不要把 Ubuntu 的 PPA 加进 Kali。** 需要某软件时：
1. 先查 Kali 仓库有没有：`apt-cache search 关键词`
2. 没有就找 Debian 的对应包
3. 再不行用 Flatpak / Snap 隔离安装（见 [05 篇](05-包管理与软件源.md#6-flatpak-与-snap)）
4. 最后才考虑源码编译，并且**编译到 `/usr/local` 或 `~/.local`**，不要覆盖系统包

---

## 3. 该不该用 Kali？

官方的态度比很多人想象的**保守**（[原文](https://www.kali.org/docs/introduction/should-i-use-kali-linux/)）：

> Kali 是专为**专业渗透测试人员和安全专家**打造的发行版，
> 如果你不熟悉 Linux，或者你在找一个通用的 Linux 桌面发行版用来做开发、网页设计、打游戏，
> **它不是推荐的选择**。
>
> 即使对经验丰富的 Linux 用户，Kali 也可能带来一些挑战。
> 它虽然是开源项目，但出于安全原因，它不是一个"完全开放"的开源项目。

| 你的情况 | 建议 |
|----------|------|
| 完全不懂 Linux，想学安全 | 先用 Ubuntu/Debian 或本库的 [`../../linux/`](../../linux/README.md) 打好基础 |
| 会用 Linux，想学渗透测试 | ✅ Kali 虚拟机 + 靶场，合适 |
| 想要日常开发/办公/游戏的主力系统 | ❌ 用 Debian/Ubuntu/Fedora，需要工具时用容器或虚拟机 |
| 做安全审计/CTF/红队 | ✅ Kali 是标准配置之一 |
| 只想"玩一下" | Live 镜像 + 虚拟机快照，不要裸机安装 |

💡 一个被低估的方案：**主力用普通 Linux，Kali 跑在 Docker 里**。
```bash
docker run --rm -it kalilinux/kali-rolling /bin/bash
```
单工具场景（只想用 `nmap`、`sqlmap`）这样最省事。

---

## 4. 镜像类型怎么选

来自 [Which Image Should I Download?](https://www.kali.org/docs/introduction/what-image-to-download/)。官网对 x86-64 提供三类镜像，外加 Everything 风味：

| 镜像类型 | 是否含本地包 | 能否 Live 启动 | 能否选桌面环境 | 适合谁 |
|----------|--------------|----------------|----------------|--------|
| **Installer** | ✅ 含 top10 / default / large 元包 | ❌ 只能安装 | ✅ | **默认推荐，没想法就选它** |
| **NetInstaller** | ❌ 安装时联网下载 | ❌ 只能安装 | ✅ | 想每次安装都拿最新包，或标准安装镜像太大下不动 |
| **Live** | 只含基础工具 | ✅ 可以直接从 U 盘跑 | ❌ 装出来是默认配置 | 想先试用 / 临时环境 / 制作启动盘 |
| **Everything** | ✅ 几乎全部工具 | 分 Live 版和 Installer 版 | — | 完全离线的场景（**> 9 GB，仅 BitTorrent 提供**） |

官方原话：

> 如果拿不定主意，就用 **Installer** 镜像。
> 我们建议保持安装时的默认选择，装完之后再按需补充包。
> **Xfce 是默认桌面环境**，同时会安装 `kali-linux-top10` 和 `kali-linux-default` 两个工具集。

安装时的桌面环境与元包选择：

| 选项 | 说明 |
|------|------|
| Desktop Environment | 默认 Xfce。另有 GNOME / KDE Plasma / MATE / LXDE 等 |
| 不选桌面环境 | 变成 **headless**（无图形界面）——服务器/云主机场景这样选 |
| 元包 | 默认 `kali-linux-top10` + `kali-linux-default`；可加 `kali-linux-large` |

💡 在虚拟机上练手，选 Installer + Xfce + default 就够了，装完约 15–20 GB。

---

## 5. 平台与镜像总览

[Image Overview](https://www.kali.org/docs/introduction/kali-linux-image-overview/) 把全部获取方式列成矩阵。按大类：

| 大类 | 典型方式 | 本库对应文档 |
|------|----------|--------------|
| 安装（Installations） | 单系统、macOS/Windows 双系统、装到 USB、BTRFS、PXE 网络安装 | [02 篇](02-安装与获取镜像.md) |
| 虚拟机 | VMware / VirtualBox / Hyper-V / QEMU / Vagrant / Proxmox / WSL | [08 篇](08-容器与虚拟化.md) |
| 云 | AWS / Azure / Digital Ocean / Linode | [09 篇](09-WSL与云环境.md) |
| 容器 | Docker / Podman / LXC / LXD / Proxmox | [08 篇](08-容器与虚拟化.md) |
| USB | Live 启动、持久化、加密持久化 | [07 篇](07-加密磁盘与LUKS.md) |
| ARM 单板机 | 树莓派全系、Banana Pi、BeagleBone、ODROID、Pinebook 等 | [10 篇](10-ARM与NetHunter.md) |
| 移动端 | NetHunter（Rootless / Lite / 完整） | [10 篇](10-ARM与NetHunter.md) |

---

## 6. 默认凭据

自 **2020.1** 起 Kali 改为**非 root 用户策略**（[原文](https://www.kali.org/docs/introduction/default-credentials/)）：

| 场景 | 用户名 | 密码 |
|------|--------|------|
| Live 启动 / 预置镜像（虚拟机、ARM） | `kali` | `kali` |
| amd64 安装镜像 | 安装过程中由你创建 | 你设定的 |
| Vagrant 镜像 | `vagrant` | `vagrant` |
| Amazon EC2 | `kali` | 用 SSH 密钥登录 |

**部分工具自带硬编码默认凭据**（⚠️ 这也是渗透测试中的常见突破口）：

| 工具 | 用户名 | 密码 | 配置文件 / 初始化程序 |
|------|--------|------|----------------------|
| BeEF-XSS | `beef` | `beef` | `/etc/beef-xss/config.yaml` |
| MySQL | `root` | *（空）* | `mysql_secure_installation` |
| OpenVAS | `admin` | 安装时生成 | `openvas-setup` |
| Metasploit Framework (PostgreSQL) | `postgres` | `postgres` | `/usr/share/metasploit-framework/config/database.yml` |
| PowerShell-Empire / Starkiller | `empireadmin` | `password123` | — |

💡 **第一件事就该改掉这些默认密码**，尤其是把 Kali 暴露在局域网时。
反向思考：这些默认值正是实战中"弱口令"的经典案例。

---

## 7. 版本与分支

Kali 不需要记复杂版本号（不像 Ubuntu 有 20.04/22.04 这种 LTS 概念），它是**滚动更新（rolling release）**。

| 分支 | 含义 | 用途 |
|------|------|------|
| `kali-rolling` | 默认分支，持续更新 | 日常使用 |
| `kali-last-snapshot` | 上一次发布时的快照 | 需要稳定、可复现的环境 |
| `kali-bleeding-edge` | 未发布的最新特性与修复 | 想提前尝鲜、帮助测试 |
| `kali-dev` | 开发分支 | 开发者和打包人员 |

```bash
# 查看当前版本
cat /etc/os-release
# 或
kali-version 2>/dev/null || cat /etc/debian_version
```

🔗 详见 [Kali Branches](https://www.kali.org/docs/general-use/kali-branches/) 与 [05-包管理与软件源.md](05-包管理与软件源.md#2-分支怎么选)。

---

## 🧪 练习

1. 在虚拟机里装好 Kali（Installer + Xfce + default），记录安装用了多久、占了多少磁盘。
   ```bash
   df -h /
   ```
2. 找出系统里所有被禁用的服务，并解释为什么 Kali 要默认禁用它们。
   ```bash
   systemctl list-unit-files --state=disabled | wc -l
   systemctl list-unit-files --state=masked | head
   ```
3. 尝试 `apt install apache2`，然后回答：为什么装完之后 `http://localhost` 访问不通？怎么让它跑起来？
4. 用 `docker run --rm -it kalilinux/kali-rolling /bin/bash` 起一个容器，对比容器里的 Kali 和虚拟机里的 Kali 有哪些差异（提示：内核、服务、网络）。

---

## 官方原文索引

本节覆盖 introduction 章节全部 12 篇：

- [Kali's Default Credentials](https://www.kali.org/docs/introduction/default-credentials/)
- [Download Kali Linux Images Securely](https://www.kali.org/docs/introduction/download-images-securely/)
- [Downloading Kali Linux](https://www.kali.org/docs/introduction/download-official-kali-linux-images/)
- [Kali Linux History](https://www.kali.org/docs/introduction/kali-linux-history/)
- [Kali Linux Image Overview](https://www.kali.org/docs/introduction/kali-linux-image-overview/)
- [Kali NetHunter History](https://www.kali.org/docs/introduction/kali-nethunter-history/)
- [Kali ARM History](https://www.kali.org/docs/introduction/kali-on-arm-a-bit-of-history/)
- [Kali Undercover](https://www.kali.org/docs/introduction/kali-undercover/)
- [Kali Press Release](https://www.kali.org/docs/introduction/press-release/)
- [Should I Use Kali Linux?](https://www.kali.org/docs/introduction/should-i-use-kali-linux/)
- [Which Image Should I Download?](https://www.kali.org/docs/introduction/what-image-to-download/)
- [What is Kali Linux?](https://www.kali.org/docs/introduction/what-is-kali-linux/)

全部 270 篇官方文档的完整索引见 [official-index.md](official-index.md)。
