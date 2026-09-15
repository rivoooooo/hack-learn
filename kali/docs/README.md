# Kali 官方文档精读手册

本目录把 Kali 官方文档（<https://www.kali.org/docs/>，共 **270 篇**）按主题重组成
13 篇中文精读笔记，并附一份自动同步的**全量官方索引**。

---

## 两份东西的区别

| 文件 | 内容 | 什么时候看 |
|------|------|-----------|
| `NN-*.md`（13 篇） | **中文精读**：把官方文档的核心内容提炼、翻译、串成体系，补上实操与踩坑经验 | 想系统学一个主题时 |
| [official-index.md](official-index.md) | **官方全量索引**：270 篇官方文档的标题、链接、内文大纲、摘要（脚本自动同步） | 知道某个具体话题、想找原文时 |

---

## 13 篇索引

| # | 主题 | 覆盖内容 | 官方章节 |
|---|------|----------|----------|
| 01 | [Kali 介绍与版本](01-Kali介绍与版本.md) | Kali 是什么、三个关键设计决定、该不该用、镜像类型怎么选、默认凭据、分支 | [introduction](https://www.kali.org/docs/introduction/) |
| 02 | [安装与获取镜像](02-安装与获取镜像.md) | 硬件需求、**GPG 校验镜像**、安装流程、分区与 LUKS、双系统、最小化/PXE/BTRFS | [installation](https://www.kali.org/docs/installation/) |
| 03 | [系统配置与优化](03-系统配置与优化.md) | 非 root 策略与 sudo、启用 root、元包体系、换桌面环境、X11/Wayland、HiDPI、RDP | [general-use](https://www.kali.org/docs/general-use/) |
| 04 | [网络配置与代理](04-网络配置与代理.md) | 网络分层排查、SSH/Samba 兼容策略、代理与隧道、远程访问、无线驱动排查 | [general-use](https://www.kali.org/docs/general-use/) · [troubleshooting](https://www.kali.org/docs/troubleshooting/) |
| 05 | [包管理与软件源](05-包管理与软件源.md) | `kali.sources` 新格式、7 个分支、更新时机、APT 报错修复、pipx、Flatpak/Snap | [general-use](https://www.kali.org/docs/general-use/) · [tools](https://www.kali.org/docs/tools/) |
| 06 | [内核与硬件驱动](06-内核与硬件驱动.md) | Kali 定制内核、驱动排查、显卡驱动、无线网卡、Secure Boot | general-use · troubleshooting |
| 07 | [加密磁盘与 LUKS](07-加密磁盘与LUKS.md) | LUKS 原理、全盘加密、USB 持久化加密、`cryptsetup` 全套命令、恢复 | installation · usb |
| 08 | [容器与虚拟化](08-容器与虚拟化.md) | Docker/Podman/LXC、虚拟机跑 Kali、云镜像、容器化渗透的限制 | [containers](https://www.kali.org/docs/containers/) · [virtualization](https://www.kali.org/docs/virtualization/) |
| 09 | [WSL 与云环境](09-WSL与云环境.md) | WSL2 安装、Win-KeX 四种模式、AWS/Azure/Linode/DO 部署 | [wsl](https://www.kali.org/docs/wsl/) · [cloud](https://www.kali.org/docs/cloud/) |
| 10 | [ARM 与 NetHunter](10-ARM与NetHunter.md) | 树莓派烧写、ARM 支持矩阵、NetHunter 架构与安装类型 | [arm](https://www.kali.org/docs/arm/) · [nethunter](https://www.kali.org/docs/nethunter/) |
| 11 | [故障排查](11-故障排查.md) | 按"现象 → 排查 → 解决"组织：安装、引导、显卡、声音、APT、无线、下载 | [troubleshooting](https://www.kali.org/docs/troubleshooting/) |
| 12 | [开发与打包](12-开发与打包.md) | Debian 打包、`debian/` 目录、构建工具链、Kali 与 Debian 的关系、提交工具 | [development](https://www.kali.org/docs/development/) |
| 13 | [政策法规与社区](13-政策法规与社区.md) | 用户政策、渗透工具政策、网络服务政策、商标、法律边界、社区渠道 | [policy](https://www.kali.org/docs/policy/) · [community](https://www.kali.org/docs/community/) |

---

## 建议阅读顺序

### 第一次装 Kali（按顺序读）
```
01 → 02 → 05 → 03 → 04
介绍  安装  包管理  配置  网络
```

### 已经有 Kali，想解决具体问题
直接查 [official-index.md](official-index.md) 里的关键词，
或按主题跳到对应篇目。

### 想深入系统层
```
06 内核与驱动 → 07 加密磁盘 → 08 容器与虚拟化 → 12 开发与打包
```

---

## 官方文档的章节分布

| 章节 | 篇数 | 本手册对应 |
|------|------|-----------|
| introduction | 12 | 01 |
| installation | 10 | 02 |
| general-use | 30 | 03 · 04 · 05 · 06 |
| tools | 7 | 05 |
| virtualization | 22 | 08 |
| containers | 5 | 08 |
| cloud | 4 | 09 |
| wsl | 5 | 09 |
| usb | 10 | 07 |
| arm | 43 | 10 |
| nethunter | 53 | 10 |
| nethunter-pro | 2 | 10 |
| development | 21 | 12 |
| troubleshooting | 12 | 11 |
| policy | 10 | 13 |
| community | 8 | 13 |
| （根文档） | 16 | 散见各篇 |

> 数据由 `scripts/fetch_kali_docs.py` 从官网 sitemap 同步，可用
> `python3 scripts/fetch_kali_docs.py` 刷新。

---

## 相关

- [Kali 工具库](../tools/index.md) —— 780 个工具包与 500+ 条命令级索引
- [工具精讲教程](../tools/tutorials/README.md) —— 重点工具的实操教程
- [靶场搭建](../labs/README.md) —— 练习环境
