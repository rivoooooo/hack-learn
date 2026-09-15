# 09 · WSL 与云环境

> 对应官方章节：<https://www.kali.org/docs/wsl/> 与 <https://www.kali.org/docs/cloud/>
> 本篇覆盖官方文档 9 篇，重点精读 WSL 安装、Win-KeX 四模式、AWS/Azure/Linode/DigitalOcean 4 篇。

## 本节速览

| 官方文档 | 中文要点 | 链接 |
|----------|----------|------|
| Kali WSL | WSL 1/2、2025 新分发架构、四种安装方式 | <https://www.kali.org/docs/wsl/wsl-preparations/> |
| Win-KeX | 总入口：Window / Seamless / Enhanced Session 三模式 | <https://www.kali.org/docs/wsl/win-kex/> |
| Win-KeX Window Mode | 独立窗口，基于 TigerVNC | <https://www.kali.org/docs/wsl/win-kex-win/> |
| Win-KeX Seamless Mode | 与 Windows 桌面共存的无缝模式 | <https://www.kali.org/docs/wsl/win-kex-sl/> |
| Win-KeX Enhanced Session Mode | RDP/xrdp，**ARM 设备唯一支持的模式** | <https://www.kali.org/docs/wsl/win-kex-esm/> |
| AWS | EC2 里跑 Kali（AMI + SSH） | <https://www.kali.org/docs/cloud/aws/> |
| Azure | Azure VM 市场镜像选 Kali | <https://www.kali.org/docs/cloud/azure/> |
| Linode | 「Kali as a Distribution」与 Marketplace 两种 | <https://www.kali.org/docs/cloud/linode/> |
| Digital Ocean | 自制 netboot 镜像 + Custom Image 上传 | <https://www.kali.org/docs/cloud/digitalocean/> |

完整 9 篇清单见文末「官方原文索引」。

## 核心知识

### WSL 1 与 WSL 2 的本质差别

- **WSL 1**：用一层「翻译层」把 Linux 系统调用翻译成 Windows 调用，类似 WINE。**共享 Windows 文件系统性能好**，但内核特性缺失。
- **WSL 2**：跑一个**真正的 Linux 内核**（在 WSL 管理的 Hyper-V 轻量 VM 里）。兼容性接近原生，但**跨 `/mnt/c/` 访问 Windows 文件很慢**。
- **官方明确推荐 WSL 2**，也是新安装的默认。

**为什么这对 Kali 特别重要**：WSL 2 才有完整内核，才谈得上 `iptables`、`tun/tap`、部分内核模块相关行为；WSL 1 上很多渗透工具直接不可用。但**两者都不能做无线注入**——WSL 没有真实网卡。

### 2025 年的 WSL 新分发架构

自 **2024 年 11 月**起，WSL 支持**用 tar 压缩的 rootfs 导入**。这让 Kali 有了新的分发方式：

```powershell
wsl --update --pre-release
wsl --install kali-linux
```

也可以直接从 Kali 镜像站下载 `.wsl` 文件：<https://kali.download/wsl-images/current/>

### Win-KeX 是什么

Win-KeX（Kali Desktop Experience for Windows）给 WSL 2 里的 Kali 提供 GUI 桌面。特性（官方列举）：

- 三种模式：Window / Seamless / Enhanced Session
- **声音支持**（PipeWire/PulseAudio）
- **共享剪贴板**（Kali ↔ Windows 复制粘贴）
- root 与非特权会话都可
- **多会话并发**（root 窗口 + 普通窗口 + seamless 同时开）
- 与 **WSLg** 完全兼容

### 云上 Kali 的形态

| 云商 | 提供方式 | SSH 用户 |
|------|----------|----------|
| AWS | 官方 **AMI**（Marketplace 里选 Kali） | `kali` |
| Azure | **Azure 市场镜像**（2022.3 起回归） | 创建时自定 |
| Linode | ① 发行版下拉选 Kali（= bare-bones + `kali-linux-core`）② Marketplace 一键部署 | `root` 或自定 |
| DigitalOcean | **没有官方镜像**，要自己用 netboot ISO 造盘再上传 Custom Image | `kali`（必须用 SSH key） |

### ⚠️ 云主机与法务（务必读）

云主机有**公网 IP**，且**平台会记录你的一切流量**。用云主机对外网做扫描/爆破，等于用实名账单去实施未授权入侵，后果是：

- 云商会立刻封号并可能配合调查；
- 流量日志、账单记录会成为完整的证据链；
- 在多数司法辖区，未授权访问他人系统是**刑事犯罪**。

**合法用途**：只扫描/攻击**你自己在云上开的靶机**（同一 VPC 内自己的实例），或**持有书面授权（SOW/授权书）**的目标。详见 [13-政策法规与社区](13-政策法规与社区.md)。

## 关键文档精读

### Kali WSL（wsl-preparations）

- **它解决什么问题**：从零在 Windows 上装一个 Kali WSL。
- **Windows 版本门槛（官方给出）**：
  | 目标 | 最低 Build | 最低 Version |
  |------|-----------|--------------|
  | WSL 1 | `16215` | `1703`（2017-06） |
  | WSL 2 (x64) | `18362.1049` | `1903`（19H1） |
  | WSL 2 (x64) 推荐 | `19041` | `2004`（20H1，2020-05） |
  | WSL 2 (ARM64) | `19041` | `2004` |
  检查方式：`Win + R` → 输入 `winver`，看 **OS Build** 后面的数字。
- **推荐路径（官方 Quick Method）**——管理员命令提示符：
  ```powershell
  dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
  dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all
  ```
  重启 → 装 WSL 2 内核 <https://aka.ms/wsl2kernel> → 重启 → 然后：
  ```powershell
  wsl --set-default-version 2
  ```
  再从 Microsoft Store 安装 **Kali Linux**，首次运行 `kali` 创建用户。
  已有 Kali WSL 1 升级到 2：
  ```powershell
  wsl --set-version kali-linux 2
  wsl --list --verbose
  ```
- **最省事路径（helper-script）**——管理员命令提示符一条命令搞定 WSL + Kali：
  ```powershell
  wsl --install --distribution kali-linux
  ```
  ⚠️ 需要 Windows 10 `20H1`（Build `19041`）或更高。**Windows 10 未打 2022 年 11 月补丁时，此法会装上过旧的 Kali 2019.2**——那就改用 Microsoft Store 重装。
- **导入 rootfs（进阶）**：
  ```powershell
  wsl --import kali-wsl wsl-test .\kali-linux-rolling-wsl-rootfs-amd64.tar.gz
  wsl --distribution kali-wsl
  ```
- **Store + PowerShell 直达下载**：
  ```powershell
  Invoke-WebRequest -Uri https://aka.ms/wsl-kali-linux-new -OutFile .\kali-linux.AppxBundle -UseBasicParsing -TimeoutSec 1800
  Add-AppxPackage .\kali-linux.AppxBundle
  ```
- **运行 Kali WSL 的 5 种方式**：命令提示符 `kali`、`wsl --distribution kali-linux`、`wsl`（设为默认后）、开始菜单 `Kali Linux`、Windows Terminal。
- **⚠️ 别用覆盖安装来切换安装方式**，官方明说：先 `wsl --unregister kali-linux`。
- **验证方式**：
  ```powershell
  wsl --status
  wsl --version       # 仅较新 WSL 版本可用
  wsl --update
  ```
  进入 Kali 后：
  ```bash
  uname -a      # 应看到 "...-microsoft-standard-WSL2"
  id            # 应看到 sudo / adm 等组
  grep VERSION= /etc/*release
  ```

### Win-KeX（总入口）

- **前置**：Kali in WSL 2 + Windows Terminal。
- **安装**：
  ```bash
  sudo apt update
  sudo apt install -y kali-win-kex
  ```
- **三种模式的启动命令**（官方原文）：
  | 模式 | 在 Kali WSL 内 | 在 Windows 命令提示符 |
  |------|----------------|----------------------|
  | Window | `kex --win -s` | `wsl -d kali-linux kex --win -s` |
  | Enhanced Session | `kex --esm --ip -s` | `wsl -d kali-linux kex --esm --ip -s` |
  | Seamless | `kex --sl -s` | `wsl -d kali-linux kex --sl -s` |
  （`-s` 即 `--sound`，开启声音）
- **可选：装全量工具**
  ```bash
  sudo apt install -y kali-linux-large
  ```
- **Windows Terminal 快捷方式**（写进 WT 的 `settings.json`）：
  ```json
  {
      "guid": "{55ca431a-3a87-5fb3-83cd-11ececc031d2}",
      "hidden": false,
      "name": "Win-KeX",
      "commandline": "wsl -d kali-linux kex --wtstart -s",
  }
  ```
  换 `--sl --wtstart` 或 `--esm --wtstart` 即可切换模式。
- **坑**：`kali-win-kex` 装完后如果 `kex` 命令找不到，检查是否在正确的 WSL 分发里执行。

### Win-KeX Enhanced Session Mode（ESM）

- **它解决什么问题**：用 **xrdp 服务 + Windows 原生 RDP 客户端**渲染桌面。**这是 ARM 设备上唯一支持的模式**。
- **操作步骤**：
  ```bash
  # 普通用户
  kex --esm --sound
  # 或（ARM 设备必须加 --ip，见下）
  kex --esm --ip --sound
  # root 会话
  sudo kex --esm
  ```
- **ARM 上的已知 Bug（官方原文）**：Windows on ARM 用 `localhost` 连容器会**大量丢包**，必须加 `--ip`；代价是**每次重启都要重新输 ESM 密码**（凭据按会话名存储，重启后会话名变了）。
- **改 RDP 密码**：
  ```bash
  kex --esm --passwd
  sudo kex --esm --passwd     # root 会话
  ```
- **会话管理**：
  ```bash
  kex --esm --start-client    # 重新连上后台会话
  kex --esm --stop            # 停止
  ```
  关闭 RDP 客户端窗口 = 断开但保留后台会话。
- **坑**：ESM 比 `--win` / `--sl` **更慢**（像素密度更高），但 HiDPI 屏上更清晰。

### Win-KeX Seamless Mode（SL）

- **它解决什么问题**：在 Windows 桌面顶部放一条 Kali 面板，从面板启动的 Kali 应用**直接和 Windows 应用共享桌面**，没有独立窗口边框。
- **操作步骤**：
  ```bash
  kex --sl -s
  ```
- **坑**：多屏时面板可能只出现在主屏；需要 `--wtstart` 才能从 Windows Terminal 启。

### AWS

- **它解决什么问题**：在 EC2 上开一台 Kali。
- **背景（重要且常被忽略）**：官方明说，Kali 的 AWS AMI **为了「不为难用户」，允许任何有 IAM/EC2 串口控制台访问权的人拿到 root shell**。要收紧就改 `/etc/systemd/system/serial-getty@.service.d/autologin.conf`：
  ```ini
  # 默认（自动以 root 登录串口）
  [Service]
  ExecStart=
  ExecStart=-/sbin/agetty --autologin root -o '-p -f -- \\u' --keep-baud 115200,38400,9600 --noclear %I $TERM
  ```
  ```ini
  # 收紧后（不自登录）
  [Service]
  ExecStart=
  ExecStart=-/sbin/agetty -o '-p -- \\u' --keep-baud 115200,38400,9600 --noclear %I $TERM
  ```
- **操作步骤**：登录 AWS → Services → Compute → **EC2** → 左侧 **AMI Catalog** → **AWS Marketplace AMIs** → 搜 `kali` → 选官方镜像 → **创建新的 key pair（务必下载私钥）** → 把存储改成 standard 省成本 → Launch instance。
- **连接**：
  ```bash
  ssh -i "keys.pem" kali@<实例IP>
  # 需要时改密码
  sudo passwd kali
  ```
- **装工具**：
  ```bash
  sudo apt update && sudo apt install -y kali-linux-headless
  ```
- **上 GUI 的两条路**：`ssh -X` 单个图形程序转发，或装 RDP 脚本后隧道：
  ```bash
  ssh -N -L 3390:127.0.0.1:3390 <用户名>@<实例IP>
  # 然后用任意远程桌面客户端连 127.0.0.1:3390
  ```
- **装 NVIDIA 驱动（GPU 破解）**：先更新 + 装 cloud 内核头文件，再装驱动：
  ```bash
  sudo apt update
  sudo apt full-upgrade -y
  sudo apt install -y linux-headers-5.7.0-kali3-cloud-amd64   # 换成你自己的 cloud 内核版本
  sudo reboot -f
  # 重连后
  sudo apt install -y nvidia-driver nvidia-cuda-toolkit
  sudo reboot -f
  ```
  > ⚠️ 上面的内核版本号是官方示例（旧版本），实际要按你的 `uname -r` 调整。以官方文档为准：<https://www.kali.org/docs/cloud/aws/>
- **坑**：AWS 控制台 UI 经常改版，官方文档自己也提示可能过时。

### Azure

- **它解决什么问题**：在 Azure 上开 Kali VM。Kali 自 **2022.3** 起回归 Azure。
- **操作步骤**：创建 Azure 账号 → 「Virtual machines」→ **Create** → **Azure virtual machine**：
  - **Resource group**：新建或选现有；
  - **Image**：选 **See all images** → 搜 `Kali` → 选唯一那个；
  - **Basics**：填用户名与 Key pair 名；
  - **Disks**：**默认没有磁盘挂上**，需要 `Create and attach a new disk`，保留默认值即可；
  - 走到 **Review + create** → Create → 部署完成后 **Go to resource** → **Connect → SSH**。
- **连接前**：按页面提示改私钥权限（`chmod 400`）。
- **坑**：`Disks` 那一步是新手最容易漏的——不挂盘就没有可用存储。

### Linode

- **两种方式**：
  1. **Kali as a Distribution**：在发行版下拉里选 Kali Linux，得到的是 [bare-bones Kali](https://www.kali.org/docs/installation/barebone-kali/)（**只装 `kali-linux-core`**）。**成本最低，适合只跑几个工具**。注意 **Root Password** 一栏决定 SSH 密码（除非你再选 public key）。
  2. **Kali from the Marketplace**：从 Marketplace 一键部署，会按你选的选项装若干 metapackage，并**自动配好 VNC 访问**。装得快但脚本执行要等一会儿。
- **事后补装默认工具**：
  ```bash
  sudo apt update && sudo apt install kali-linux-default -y
  ```
- **坑**：Marketplace 的 metapackage 选项会**显著影响资源占用**，按需勾选，别无脑全选。

### Digital Ocean

- **它解决什么问题**：DigitalOcean **没有官方 Kali 镜像**，但支持 **Custom Image**，所以可以自己造。
- **思路**：本地用 **netboot mini.iso** 装一个**最小化、无桌面**的 Kali → 装 `cloud-init` / `openssh-server` → 清理 → 导出 `.vmdk` → 压缩上传 → 起 droplet。
- **操作步骤（官方原文命令）**：
  ```bash
  # 1. 取 netboot ISO（文本安装器）
  #    http://http.kali.org/kali/dists/kali-rolling/main/installer-amd64/current/images/netboot/mini.iso
  #    （图形安装器在 netboot/gtk/ 下）

  # 2. 本地建 VM：OS 选最新 Debian 64-bit，磁盘 20 GB，单文件、动态分配
  #    安装时手动分区：全部文件一个分区、不要 swap
  #    软件选择里只勾 "standard system utilities"

  # 3. 装完重启，更新系统
  sudo apt update
  sudo apt full-upgrade -y

  # 4. 装 cloud-init 并指定数据源
  sudo apt install -y cloud-init
  sudo sh -c "echo 'datasource_list: [ ConfigDrive, DigitalOcean, NoCloud, None ]' > /etc/cloud/cloud.cfg.d/99_digitalocean.cfg"
  sudo systemctl enable cloud-init --now

  # 5. 准备 SSH（自定义镜像必须用 SSH key）
  sudo apt install -y openssh-server
  sudo systemctl enable ssh.service --now
  passwd -d root                 # 删除 root 密码
  mkdir -p /root/.ssh/

  # 6. 清理
  apt autoremove
  apt autoclean
  rm -rf /var/log/*
  history -c
  poweroff

  # 7. 本地压缩磁盘文件（在 VM 目录里）
  bzip2 kali.vmdk
  ```
  然后在 DigitalOcean 控制台 **Manage → Images → Custom Images** 上传，命名为 Kali、标记为 Debian、选区域。之后对该镜像选 **More → Start a droplet**，**必须绑定 SSH key**。
- **连接**：
  ```bash
  ssh -i MY_KEY kali@<IP>
  ```
- **代价（官方明说）**：**磁盘大小直接决定账单**。磁盘建 40 GB 就无法用 $5/月档（该档最大 25 GB），被迫上 $10/月。另外**自定义镜像只能在它上传的那个区域启动**（当前限制）。
- **坑**：上传的镜像占空间，DO 按磁盘用量计费；忘了在网络安装阶段加镜像源会导致 `apt update` 不走镜像（可用 [06-内核与硬件驱动](06-内核与硬件驱动.md) 的源配置修）。

## 实操清单

### WSL

- [ ] `winver` 确认 Build 是否满足 WSL 2 要求
- [ ] 管理员 PowerShell/Dism 开启 `VirtualMachinePlatform` 与 `Microsoft-Windows-Subsystem-Linux`
- [ ] `wsl --set-default-version 2`，确认 `wsl --list --verbose` 里 VERSION 为 2
- [ ] 装 Kali：`wsl --install --distribution kali-linux` 或 Microsoft Store
- [ ] `wsl --unregister kali-linux` 只在**真要重装**时用（会删掉整个发行版数据）
- [ ] 装 Win-KeX：`sudo apt install -y kali-win-kex`
- [ ] 三种模式各启动一次：`kex --win -s` / `kex --esm --ip -s` / `kex --sl -s`
- [ ] 验证剪贴板互通、声音是否正常

### 云

- [ ] 明确**授权范围**：只对自己实例/书面授权目标操作
- [ ] AWS/Azure：创建时下载并保存好 SSH 私钥（丢了只能重建实例）
- [ ] 首次登录后立刻 `sudo passwd kali` / 加 public key
- [ ] 装工具：`sudo apt update && sudo apt install -y kali-linux-headless`
- [ ] 云主机设好安全组/防火墙，**别把 SSH 22 端口开放给 0.0.0.0/0**
- [ ] GPU 机型：先装 cloud 内核头文件再装 `nvidia-driver nvidia-cuda-toolkit`
- [ ] 不用时 `poweroff` 或销毁实例，避免持续计费

## 排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `'wsl' is not recognized as an internal or external command` | Windows 10 版本低于 20H1，无 WSL helper-script | 用 Dism/PowerShell 手动开启功能，或升级 Windows |
| `wsl --install` 装出来是 Kali 2019.2 | Windows 10 未打 2022-11 补丁 | 从 Microsoft Store 重新安装 Kali |
| WSL 2 起不来 | BIOS/UEFI 未开虚拟化，或 `VirtualMachinePlatform` 未启用 | 开 VT-x/AMD-V；`Get-WindowsOptionalFeature -Online \| Where-Object {$_.FeatureName -eq "VirtualMachinePlatform"}` |
| 在 VM 里装 WSL 2 失败 | 未开嵌套虚拟化 | 宿主开启 nested virtualization |
| Win-KeX ARM 上卡顿/丢包 | Windows on ARM 的 `localhost` bug | 加 `--ip`，接受每次重启重输密码 |
| `kex` 提示需要密码但没设置 | 首次启动需设 RDP 密码 | `kex --esm --passwd` |
| AWS 连不上、权限拒绝 | 私钥权限过宽，或用户不是 `kali` | `chmod 400 keys.pem`；AWS/Azure 用户是 `kali`，Linode 可能是 `root` |
| 云主机 `apt update` 很慢 | 未走就近镜像 | 参考 [06-内核与硬件驱动](06-内核与硬件驱动.md) 的镜像与源配置 |
| DigitalOcean droplet 起不来 | 磁盘超出所选套餐上限 | 重建更小的磁盘镜像（例如 20 GB），或上更贵的套餐 |
| GPU 机型 `nvidia-smi` 报错 | 内核头文件与 kernel 不匹配 | 装 `linux-headers-$(uname -r)` 对应版本后再装驱动 |

## 官方原文索引

- [Win-KeX](https://www.kali.org/docs/wsl/win-kex/)
- [Win-KeX Enhanced Session Mode](https://www.kali.org/docs/wsl/win-kex-esm/)
- [Win-KeX Seamless Mode](https://www.kali.org/docs/wsl/win-kex-sl/)
- [Win-KeX Window Mode](https://www.kali.org/docs/wsl/win-kex-win/)
- [Kali WSL](https://www.kali.org/docs/wsl/wsl-preparations/)
- [AWS](https://www.kali.org/docs/cloud/aws/)
- [Azure](https://www.kali.org/docs/cloud/azure/)
- [Digital Ocean](https://www.kali.org/docs/cloud/digitalocean/)
- [Linode](https://www.kali.org/docs/cloud/linode/)
