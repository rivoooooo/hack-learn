# 10 · ARM 与 NetHunter

> 对应官方章节：<https://www.kali.org/docs/arm/>、<https://www.kali.org/docs/nethunter/>、<https://www.kali.org/docs/nethunter-pro/>
> 本篇覆盖官方文档 **98 篇**（ARM 43 + NetHunter 53 + NetHunter Pro 2），重点精读树莓派、ARM chroot/模拟、NetHunter 架构与安装、Rootless 版、内核移植 6 组。

## 本节速览

| 官方文档 | 中文要点 | 链接 |
|----------|----------|------|
| Kali On ARM（章节首页） | 设备/镜像/内核总览入口 | <https://www.kali.org/docs/arm/> |
| Raspberry Pi 4 | `dd` 写 SD 卡、蓝牙/音频/HDMI 调整 | <https://www.kali.org/docs/arm/raspberry-pi-4/> |
| Using the Raspberry Pi Imager software | 用官方 Imager 图形化写卡 | <https://www.kali.org/docs/arm/using-rpi-imager-to-write-raspberry-pi-images/> |
| Running x86 code on ARM devices | `qemu-user-static` + `binfmt` 跑 x86 程序 | <https://www.kali.org/docs/arm/x86-on-arm/> |
| NetHunter Components | 三大件：自定义内核 / Kali chroot / NetHunter App | <https://www.kali.org/docs/nethunter/nethunter-components/> |
| Installing Kali NetHunter | 解锁→root→自定义恢复→刷 NetHunter | <https://www.kali.org/docs/nethunter/installing-nethunter/> |
| NetHunter Rootless | **不 root、不刷机**，Termux 里跑 NetHunter | <https://www.kali.org/docs/nethunter/nethunter-rootless/> |
| NetHunter Chroot Manager | 下载/备份/恢复/删除 Kali chroot，装 metapackage | <https://www.kali.org/docs/nethunter/nethunter-chroot-manager/> |
| NetHunter Kernel | 查询/下载/刷写设备内核 | <https://www.kali.org/docs/nethunter/nethunter-kernel/> |
| Patching the Kernel | 给内核打注入/WiFi/HID 补丁 | <https://www.kali.org/docs/nethunter/nethunter-kernel-1-patching/> |
| Porting NetHunter to New Devices | 移植到新设备（手工 / kernel builder） | <https://www.kali.org/docs/nethunter/porting-nethunter/> |
| Wireless Cards and NetHunter | 为什么需要外置网卡 | <https://www.kali.org/docs/nethunter/wireless-cards/> |
| Waydroid on NetHunter Pro | 在 NetHunter Pro 上跑 Android 容器 | <https://www.kali.org/docs/nethunter-pro/waydroid/> |

完整 98 篇清单见文末「官方原文索引」。

## 核心知识

### ARM 支持矩阵（43 篇覆盖的设备）

官方 ARM 文档按设备逐篇写，可归为几类：

| 类别 | 代表设备 |
|------|----------|
| 单板机（SBC） | Raspberry Pi 1/2/3/4/400/5、Zero/Zero W/Zero 2 W、Banana Pi/Pro、BeagleBone Black、CubieBoard2/CubieTruck、CuBox/CuBox-i4Pro、ODROID-C0/C1/C1+/C2/U2/U3/XU3、NanoPC-T3、NanoPi NEO Plus2、Radxa Zero（eMMC / sdcard）、RIoTboard、Trimslice、Utilite Pro、Mini-X、Gateworks Newport/Ventana |
| 笔记本 | Pinebook、Pinebook Pro |
| Chromebook | Samsung Chromebook(daisy_snow) / Chromebook 2(peach_pi/pit) / HP Chromebook(daisy_spring)、Acer Tegra Chromebook 13"(Nyan)、ASUS Chromebook Flip(Veyron) |
| 安全硬件 | USB Armory MKI / MKII |
| 特殊用途 | Raspberry Pi-Tail Zero W / Zero 2 W、P4wnP1 A.L.O.A（Zero W 上做 HID 攻击） |

**通用烧写流程**（以树莓派为例，其余板子同理）：

1. 准备 **≥16 GB、Class 10** 的 microSD（官方推荐）。
2. 从 <https://www.kali.org/get-kali/> 下载对应设备的镜像，**并校验 SHA256**。
3. 写卡（⚠️ 会清空目标设备，写错设备名会毁掉你的硬盘）：
   ```bash
   # ⚠️ /dev/sdX 必须替换成你的读卡器设备名，先用 lsblk 确认
   xzcat kali-linux-2026.2-raspberry-pi-armhf.img.xz | sudo dd of=/dev/sdX bs=4M status=progress
   # 或 64 位：
   xzcat kali-linux-2026.2-raspberry-pi-arm64.img.xz | sudo dd of=/dev/sdX bs=4M status=progress
   ```
4. 插卡上电，用默认凭据登录：<https://www.kali.org/docs/introduction/default-credentials/>
5. 首次登录后立即 `sudo kali-tweaks` 改密码/键盘布局。

**镜像默认内容**：树莓派 4 等主流板子的镜像是 **ARM 原生安装**，**默认含 `kali-linux-default` metapackage**（与桌面版类似）。

官方构建脚本：<https://gitlab.com/kalilinux/build-scripts/kali-arm>，树莓派用 `raspberry-pi.sh`（32 位）或 `raspberry-pi-64-bit.sh`（64 位）。

### ARM 上的工具可用性：为什么要跑 x86 代码

很多渗透工具（尤其是**闭源二进制**、只有 x86_64 构建的商用工具）在 ARM 上没有原生版本。Kali 官方给了 `qemu-user-static` + `binfmt-support` 方案：

```bash
sudo apt update
sudo apt install -y qemu-user-static binfmt-support
sudo dpkg --add-architecture amd64
sudo apt update
sudo apt install libc6:amd64
```

配好后，**x86_64 二进制会被内核自动交给 qemu 用户态模拟执行**。官方举的例子是在 ARM 上跑 PowerShell：装完组件后 `pwsh` 从 `exec format error` 变成正常启动。

手动指定执行：
```bash
qemu-x86_64-static my_x86_code
```

⚠️ 官方提醒：`qemu-user-static` 当前版本**可能让部分程序行为异常**，Kali 放了打过补丁的版本；若文档流程跑不通，可从 snapshot.debian.org 下载指定版本手工安装（具体 URL 见官方页面）。

**性能认知**：用户态模拟只翻译系统调用/指令，**比原生慢一个数量级**，且依赖库缺失时程序还是会挂——需要按需补 `libc6:amd64` 之类的多架构库。

### NetHunter 三大件（官方 Components 页）

```text
┌─────────────────────────────────────────────────────┐
│  NetHunter ROM Overlay（刷进 Android 的 zip）        │
│  ├─ ① Custom Android Kernel  自定义内核              │
│  │    · HID（把手机当键盘/鼠标）                      │
│  │    · OTG 无线支持                                 │
│  │    · CDROM 模拟                                   │
│  │    · 部分设备：外置 SDR/蓝牙、y-cable 充电         │
│  │    · Multirom 支持（KEXEC 补丁）                   │
│  │    · 对外置无线设备的额外补丁                      │
│  ├─ ② Kali Linux chroot                             │
│  │    · minimal（100+ MB，裸系统）                   │
│  │    · full（约 600 MB，与 App 完整集成）            │
│  └─ ③ NetHunter Android Application                 │
│       · 管理 chroot 的 GUI                           │
│       · 开机服务、配置复制到 sdcard                   │
│       · MANA / MPC / VNC / DuckHunter / HID 等入口    │
│       · 自定义命令构建器                              │
└─────────────────────────────────────────────────────┘
```

### NetHunter 的版本形态

| 形态 | 前提 | 能力 |
|------|------|------|
| **NetHunter（原版）** | 解锁 bootloader + root + 自定义 recovery（TWRP）+ 自定义内核 | 全功能：HID、BadUSB、外置网卡注入、恶意外接设备等 |
| **NetHunter Lite** | 已 root 的设备（无定制内核） | 功能受限，硬件类特性缺失 |
| **NetHunter Rootless** | **完全不用 root、不刷机、不影响保修** | Termux + proot 里跑 Kali，纯用户态能力 |

### ⚠️ NetHunter 的法律与授权边界

NetHunter 的模块（EvilTwin、Wifipumpkin3、HID/BadUSB、WPS 攻击、CARsenal 汽车攻击）几乎全部是**针对第三方系统/网络/设备**的攻击工具。使用前必须确认：

- 你有**书面授权**（渗透测试合同、SOW）；
- 或目标**完全是你自己的设备**（自己的车、自己的手机、自己的 AP）；
- EvilTwin / Wifipumpkin3 **会主动诱骗他人输入凭据**，即使在自己网络里，也**可能影响路过的无关设备**。

细节见 [13-政策法规与社区](13-政策法规与社区.md)。

## 关键文档精读

### Raspberry Pi 4（代表所有 SBC 的通用流程）

- **它解决什么问题**：在 Pi 4 上跑 Kali。
- **硬件**：四核 1.5 GHz，2/4/8 GB RAM（按型号），系统跑在 microSD 上。
- **操作步骤**：见上文「通用烧写流程」。
- **验证方式**：
  ```bash
  uname -a                 # 应看到 aarch64 或 armv7l
  nproc; free -h
  grep -c . /proc/cpuinfo  # 核对核心数
  ```
- **官方 Tips（这些是实际会踩的坑）**：
  ```bash
  # 1. Pi 4 的蓝牙需要先起 uart helper 服务
  sudo systemctl enable --now hciuart.service
  sudo systemctl enable --now bluetooth.service

  # 2. 默认音频走 HDMI，3.5mm 耳机孔无声 → 切换到耳机输出
  sudo amixer -c 0 set numid=3 1

  # 3. 接了 LCD HAT 后无显示 → 尝试移除 Xorg 配置片段
  sudo mv -v /etc/X11/Xorg.conf.d/99-vc4.conf ~
  ```
- **无头（headless）联网**：在第一分区放 `wpa_supplicant.conf`：
  ```bash
  wpa_passphrase YOURNETWORK > wpa_supplicant.conf
  ```
  ⚠️ 若把密码直接写在命令行里，**会留在 shell 历史里**。

### Using the Raspberry Pi Imager software

- **它解决什么问题**：不想用 `dd` 命令行，改用图形化写卡工具。
- **要点**：Raspberry Pi Imager 内置了 Kali 的镜像下载项，选好设备与镜像后一键写卡，省掉手工 `xzcat | dd`。
- **坑**：Imager 内置的镜像版本可能滞后于 Kali 官网最新版；追求最新版还是从 <https://www.kali.org/get-kali/> 下载后手动写。
- **详细步骤以官方为准**：<https://www.kali.org/docs/arm/using-rpi-imager-to-write-raspberry-pi-images/>

### Running x86 code on ARM devices

- **它解决什么问题**：ARM 上跑只有 x86_64 构建的闭源工具。
- **操作步骤**：见上文「为什么要跑 x86 代码」的命令块。
- **验证方式**：
  ```bash
  file /path/to/binary           # 显示 x86-64 或 aarch64
  pwsh                           # 官方示例：装 qemu 前报 exec format error，装后正常
  ls /proc/sys/fs/binfmt_misc/   # 应能看到 qemu-x86_64 条目
  ```
- **坑**：需要额外多架构库时得手动 `dpkg --add-architecture amd64` + 装对应 `:amd64` 包；模拟执行**明显慢**。

### NetHunter Components

- **它解决什么问题**：理解 NetHunter 由什么组成、各自负责什么。
- **要点**：见上文架构图。**chroot 分 minimal（100+ MB）与 full（约 600 MB）**——大多数用户要 full。
- **验证方式**：在 NetHunter App 里看 chroot 状态；`NetHunter Chroot Manager` 面板能列出/管理 chroot。

### Installing Kali NetHunter（原版，需刷机）

- **它解决什么问题**：在受支持设备上安装完整 NetHunter。
- **官方支持的规模**：**超过 99 款设备**，Android 版本从 **4.4 KitKat 到 15**。
- **操作步骤（官方 5+1 步）**：
  1. **确认设备支持**：先看 [预构建镜像列表](https://nethunter.kali.org/images.html)；不在列表但[设备内核受支持](https://nethunter.kali.org/device-kernels.html) → 自己按「Building NetHunter」构建；完全不支持 → 只能退到 **NetHunter Lite**。
     官方还提供**通用 ARM64 安装包**：
     - Full：`kali-nethunter-20YY.X-generic-arm64-kalifs-full.zip`
     - Minimal：`kali-nethunter-20YY.X-generic-arm64-kalifs-minimal.zip`
     下载地址：<https://kali.download/nethunter-images/current/>（另有 armhf/i386/amd64）
  2. **开启开发者模式**：设置 → 关于 → 连点 **Build number 7 次** → 回到设置 → **Developer options** → 打开 **Advanced Reboot** 与 **Android Debugging**。
  3. **解锁 bootloader、root、装自定义 recovery**：
     - 官方首选 recovery 是 **TWRP**；
     - 官方首选 root 方案是 **Magisk**；
     - ⚠️ **这一步因设备与 Android 版本而异**，官方把你导向 XDA 论坛，自己找对应机型的教程。
  4. **（Android 9/10/11 必做）刷 Universal DM-Verity & ForceEncrypt Disabler 并格式化 data 分区**。
     - ⚠️ 官方说明原因：**Magisk 不支持加密 data 分区上的 user context 变更**，不刷会导致 SSH 连 Kali rootfs 时报 `Required key not available`。
  5. **刷 NetHunter 镜像**（二选一）：
     - **Recovery 方式**：把 zip 传到手机 → 重启进 recovery → 刷 zip → 重启 → 打开 NetHunter App 完成初始化。
     - **Magisk 模块方式（官方标注为「新的、推荐的方法」）**：用**同一个 zip** 在 Magisk 里当模块安装；**安装时保持屏幕常亮**（锁屏时 Android 可能杀掉 App）；然后重启。
     - 附带说明（Android 10/11）：刷完要**从 NetHunter Store 更新 NetHunter App**，绕开 scoped storage 限制。
- **验证方式**：
  - NetHunter App 能打开，chroot 能启动；
  - 官方有专门的「Testing Checklist」：<https://www.kali.org/docs/nethunter/testing-checklist/>（检查能否启动、应用是否装上、Android VNC / BlueNMEA / DriveDroid / Hacker's Keyboard / RF Analyzer / Terminal Emulator、以及 设置→关于手机→内核版本 是否正确）。
- **坑**：**步骤 3 是最大的不确定性来源**——官方明说各机型差别很大。刷机**会清空数据**，先备份。

### NetHunter Rootless（零风险入门路径）

- **它解决什么问题**：**在完全不 root、不刷机的 Android 上**体验 NetHunter，不丢保修。
- **前置**：一台**原厂未修改**的 Android（不需要 root，不需要自定义 recovery）。
- **操作步骤（官方原文）**：
  1. 从 <https://store.nethunter.com/> 安装 **NetHunter-Store** App。
  2. 在 Store 里安装 **Termux**、**NetHunter-KeX client**、**Hacker's keyboard**。
     - 官方备注：装完 Store 里按钮可能不会变成「installed」，无视它；Termux 首次启动可能卡在 installing，敲回车即可。
  3. 打开 Termux：
     ```bash
     termux-setup-storage
     pkg install wget
     wget -O install-nethunter-termux https://offs.ec/2MceZWr
     chmod +x install-nethunter-termux
     ./install-nethunter-termux
     ```
- **使用命令（官方表格）**：
  | 命令 | 作用 |
  |------|------|
  | `nethunter` | 进入 NetHunter 命令行 |
  | `nethunter kex passwd` | 设置 KeX 密码（首次使用前） |
  | `nethunter kex &` | 启动桌面体验（KeX）用户会话 |
  | `nethunter kex stop` | 停止 KeX |
  | `nethunter -r` | 以 root 进入 NetHunter CLI |
  | `nethunter -r kex passwd` | 设置 root 的 KeX 密码 |
  | `nethunter -r kex &` | 以 root 启动 KeX |
  | `nethunter -r kex kill` | 杀掉所有 KeX 会话 |
  > `nethunter` 可缩写为 `nh`。
- **验证方式**：开 KeX 客户端，输入密码连接；官方建议在 KeX 客户端「Advanced Settings」里设自定义分辨率提升观感。
- **坑（官方 Tips，逐条重要）**：
  1. 装完第一件事：`sudo apt update && sudo apt full-upgrade -y`；空间够再 `sudo apt install -y kali-linux-default`。
  2. 大部分工具能用，但**部分受限**——例如 **Metasploit 能用但没有数据库支持**。
  3. **`top` 之类的工具在未 root 手机上跑不了**。
  4. **非 root 用户在 chroot 内仍有 root 权限**（proot 的特性），**心里要有数**。
  5. Galaxy 手机可能不允许非 root 用户用 sudo，改用 `su -c`。
  6. 备份 rootfs（先停掉所有 nethunter 会话，在 Termux 里）：
     ```bash
     tar -cJf kali-arm64.tar.xz kali-arm64 && mv kali-arm64.tar.xz storage/downloads
     ```
     老设备把 `arm64` 换成 `armhf`。

### NetHunter Chroot Manager

- **它解决什么问题**：在 NetHunter App 里管理 Kali chroot 与 metapackage。
- **功能**：下载并安装 chroot（若尚不存在）、**备份/恢复 chroot**、**删除 chroot**、按需安装 **Kali metapackage**。
- **官方建议**：**`kali-nethunter` metapackage 已包含运行 NetHunter 所需的一切**；只在确实需要时再加别的 metapackage，尤其手机存储紧张时。
- **验证方式**：Chroot Manager 面板里能列出当前 chroot 及其大小；`df -h` 看剩余空间。

### NetHunter Kernel / Patching the Kernel

- **它解决什么问题**：查/下载/刷设备内核；或给内核打补丁以获得注入与 HID 能力。
- **要点**：
  - NetHunter 网页端可查设备是否有可用内核并直接下载刷写；设备**不支持运行时刷写**的话，用同一个 zip 在 recovery 里刷（借助 magisk 的 magic-flash）。
  - 打补丁（官方原文）：**默认会应用 WiFi 注入补丁与新增 WiFi 驱动的补丁**；**4.x 以下的内核还需要 HID 键盘/鼠标补丁**。
- **坑**：**内核与 Android 版本、设备型号强绑定**，刷错内核会变砖。官方以 Google Nexus 6P 为例讲解，但强调「思路一样」，实际要替换成你的设备。

### Porting NetHunter to New Devices

- **它解决什么问题**：你的设备不在受支持列表里，自己移植。
- **两条路**：
  - **手工移植**：<https://www.kali.org/docs/nethunter/porting-nethunter/>
  - **用 kernel builder**：<https://www.kali.org/docs/nethunter/porting-nethunter-kernel-builder/>
- **内核配置的官方分册**（按功能拆分，逐篇读）：
  - General / Network / Wifi / SDR / USB(3.x) / USB(4.x) / NFS / CAN
- **坑**：这是**开发者级任务**，需要熟悉 Android 内核源码树、`defconfig`、交叉编译工具链，且**极易把设备刷成砖**。

### Wireless Cards and NetHunter

- **它解决什么问题**：解释为什么手机做无线渗透必须插外置网卡。
- **核心结论（官方原文大意）**：**除少数现代 Snapdragon SOC 上的高通芯片外，Android 设备在大多数机型上不支持 monitor mode**；少数机型（Nexus 5、Nexus 7 (2012)、Nexus 6P 等）可通过**改固件 + 改内核**支持。
- **实践含义**：
  - 想正经做无线渗透，买一块**支持注入的 USB 无线网卡** + OTG 线；
  - **部分设备（如 POCO F1）需要带外部供电的 OTG 线**；
  - 内核必须支持该网卡驱动与注入补丁，否则插上也没用。
- **验证方式**：
  ```bash
  iw dev                       # 是否列出外置网卡
  airmon-ng                    # 看芯片组是否被识别
  airmon-ng check kill         # 官方反复强调：进 monitor 前必须先跑这条
  ```
  （官方无线排查页原话：**90% 的无线问题是因为没读 aircrack-ng 文档、没先跑 `airmon-ng check kill`**。）

### NetHunter 应用内的攻击模块（简介，命令以 App 操作为主）

| 模块 | 作用（来自官方摘要） |
|------|----------------------|
| **HID Keyboard Attacks** | 把设备+OTG 线变成预编程键盘，直接打字执行命令（过去只有 Teensy 类硬件能做） |
| **DuckHunter** | 把 USB Rubber Ducky 脚本转成 NetHunter HID 攻击格式 |
| **BadUSB Attack** | Black Hat USA 2014 那套 BadUSB 实现；开启后设备变成网卡，把目标 PC 流量引出 |
| **USB-Arsenal** | USB 攻击控制中心，启停 USB gadget 模式；支持挂载 `.iso`/`.img` 做 mass storage |
| **Bluetooth-Arsenal** | 蓝牙攻击控制中心：启停服务、启用接口、扫描可发现设备（含 Carwhisperer、Bad Bluetooth） |
| **CARsenal** | 汽车安全工具集；**需要内核启用 CAN 支持**；含 CAN-USB、ICSim、UDSim、MSF 等 |
| **EvilTwin** | 抓目标网络握手 → 起同名恶意 AP + 强制门户钓鱼（用握手校验） |
| **WifiPumpkin3** | 恶意 AP 与 MitM；可带/不带 captive portal；可自定义 SSID/信道；部分设备支持虚拟 `wlan1` |
| **WPS Attacks** | 跑 WPS 攻击；**无需外置网卡**，OneShot 支持 Pixie Dust、在线爆破、PBC、PIN 预测（用 wpa_supplicant，**不需要 monitor mode**） |
| **Wardriving** | 把 Android GPS + 外置射频（WiFi/蓝牙/RTL-SDR/漏洞扫描器）汇入 **Kismet**，生成实时地理标记 RF 热力图 |
| **KeX / KeX Manager** | 桌面体验：连本地 VNC（默认 `localhost:1:5900`，即 5901）；可 HDMI 或投屏接显示器 |
| **MAC Changer** | 改网卡 MAC：随机或手填 `00:11:22:AA:BB:CC` 格式 |
| **Nmap Scan** | Nmap 常用选项的 GUI 封装 |
| **Metasploit Payload Generator** | 基于 g0tmi1k 的 MSFvenom Payload Creator（MFSPC） |
| **SearchSploit** | 搜 Exploit-DB，可在线查看或本地编辑 |
| **Social Engineer Toolkit** | 生成/自定义 3 套钓鱼邮件模板，存进 SET 的 templates 目录 |
| **Kali Services** | 启停 chroot 内服务（SSH、Apache、OpenVPN…），并可设为开机自启 |
| **Custom Commands** | 自定义命令按钮（例如把 Wifite 做成一个按钮） |
| **Modules** | 手工加载内核模块；多数内核把驱动编译为 builtin，此页才用不到 |
| **Settings** | 自定义开机动画、备份/恢复 `nh_files`、改 SELinux 状态、终端样式 |
| **Terminal** | 三种终端：chroot 内 Kali 终端、Android 终端、Android root 终端 |
| **Home Screen** | 显示内外网 IP、HID 接口可用性 |
| **Audio** | 让 KeX 会话支持音频 |

> 以上均为官方 App 内操作（点按式），**没有需要照抄的命令行步骤**，具体交互以各官方页面为准。

### NetHunter Pro

- **NetHunter Pro** 是跑在**专用移动设备**（如 PinePhone 类）上的形态，与「Android 手机刷 NetHunter」不同。
- 两篇官方文档：
  - **Enable OTG in SDM845（OnePlus 6/6T、POCO F1）**：需要用 `abootimg`、`device-tree-compiler` 改 dtb：
    ```bash
    sudo apt install -y abootimg device-tree-compiler
    ```
    ⚠️ 官方特别提醒：**部分设备（如 POCO F1）需要带外部供电的 OTG 线**，必须接外接电源。
  - **Waydroid on NetHunter Pro**：Waydroid 是开源项目，用**容器**在 Linux 上跑 Android，从而让 Android App 与 Linux App 在同一设备上共存。

## 实操清单

### ARM 单板机

- [ ] `lsblk` 确认读卡器设备名，**不要写错 `dd of=`**
- [ ] 从官网下载镜像并校验 SHA256，与 `SHA256SUMS` 对照
- [ ] `xzcat ...img.xz | sudo dd of=/dev/sdX bs=4M status=progress`
- [ ] 首次登录后立刻 `sudo kali-tweaks` 改默认密码
- [ ] Pi 4 蓝牙：`sudo systemctl enable --now hciuart.service bluetooth.service`
- [ ] Pi 4 音频：`sudo amixer -c 0 set numid=3 1`
- [ ] 需要 x86 程序：装 `qemu-user-static binfmt-support`，必要时加 amd64 架构
- [ ] 自定义镜像：读 `kali-arm` 仓库 README，用 `raspberry-pi.sh` / `raspberry-pi-64-bit.sh`

### NetHunter

- [ ] **先判断走哪条路**：受支持机型刷完整版 / 只 root 装机 Lite / 什么都不懂先玩 Rootless
- [ ] 完整版：备份数据 → 开发者模式 → TWRP + Magisk → （Android 9–11）刷 DM-Verity/ForceEncrypt Disabler 并格式化 data → 刷 NetHunter zip 或做 Magisk 模块
- [ ] 刷完从 NetHunter Store **更新 App**
- [ ] Rootless：Store 装 NetHunter-Store → Termux/KeX client/Hacker's Keyboard → `termux-setup-storage` → `wget` 脚本 → 运行
- [ ] Rootless 首件事：`sudo apt update && sudo apt full-upgrade -y`
- [ ] Rootless 备份：`tar -cJf kali-arm64.tar.xz kali-arm64 && mv kali-arm64.tar.xz storage/downloads`
- [ ] 无线渗透：准备支持注入的 USB 网卡 + （可能需供电的）OTG 线
- [ ] 任何注入操作前先 `airmon-ng check kill`
- [ ] 按官方 Testing Checklist 逐项验收新设备

## 排错

| 现象 | 原因 | 解决 |
|------|------|------|
| SD 卡插上不启动 | 镜像与板子型号不匹配 / 卡质量差 | 用对应型号的镜像；换 Class 10 卡；重新 `dd` 并在写完后 `sync` |
| Pi 4 蓝牙不可用 | 缺 `hciuart.service` | `sudo systemctl enable --now hciuart.service bluetooth.service` |
| Pi 4 3.5mm 耳机无声 | 默认走 HDMI | `sudo amixer -c 0 set numid=3 1` |
| 接 LCD HAT 后无显示 | Xorg 配置片段冲突 | `sudo mv -v /etc/X11/Xorg.conf.d/99-vc4.conf ~` 后重启 |
| ARM 上运行 x86 程序报 `exec format error` | 未装 qemu 用户态模拟 / binfmt 未注册 | `sudo apt install -y qemu-user-static binfmt-support` |
| 用户态模拟的程序行为异常 | `qemu-user-static` 已知问题 | 按官方页面从 snapshot.debian.org 装指定版本 |
| NetHunter 刷完 SSH 连 rootfs 报 `Required key not available` | data 分区加密，Magisk 不支持 user context 变更 | （Android 9–11）刷 DM-Verity/ForceEncrypt Disabler 并**格式化 data** |
| NetHunter Magisk 模块安装中断 | 锁屏时 Android 杀掉 App | 保持屏幕常亮重装 |
| NetHunter 里外置网卡不被识别 | 内核无该驱动 / OTG 供电不足 | 换受支持网卡；换**带外部供电的 OTG 线**（POCO F1 明确需要） |
| 注入失败、aireplay 无反应 | 网卡或驱动不支持注入 / 未先停网络管理器 | `airmon-ng check kill`；参考 [11-故障排查](11-故障排查.md) |
| Rootless 里 `top` 跑不了 | 未 root 的 Android 限制 | 已知限制，用别的方式看进程 |
| Rootless 里 Metasploit 无数据库 | proot 环境下受限 | 已知限制，接受或用完整版 NetHunter |
| KeX 连不上 | 未设密码 / 端口被占 | `nethunter kex passwd`；`nethunter -r kex kill` 清会话后重来 |

## 官方原文索引

- [Banana Pi](https://www.kali.org/docs/arm/banana-pi/)
- [Banana Pro](https://www.kali.org/docs/arm/banana-pro/)
- [BeagleBone Black](https://www.kali.org/docs/arm/beaglebone-black/)
- [Samsung Chromebook (daisy_snow) & Samsung Chromebook 2 (peach_pi / peach_pit) & HP Chromebook (daisy_spring)](https://www.kali.org/docs/arm/chromebook-exynos/)
- [Acer Tegra Chromebook 13" (Nyan)](https://www.kali.org/docs/arm/chromebook-nyan/)
- [ASUS Chromebook Flip (Veyron)](https://www.kali.org/docs/arm/chromebook-veyron/)
- [CubieBoard2](https://www.kali.org/docs/arm/cubieboard2/)
- [CubieTruck (CubieBoard3)](https://www.kali.org/docs/arm/cubietruck/)
- [CuBox](https://www.kali.org/docs/arm/cubox/)
- [CuBox-i4Pro](https://www.kali.org/docs/arm/cubox-i4pro/)
- [Gateworks Newport](https://www.kali.org/docs/arm/gateworks-newport/)
- [Gateworks Ventana](https://www.kali.org/docs/arm/gateworks-ventana/)
- [Mini-X](https://www.kali.org/docs/arm/mini-x/)
- [NanoPC-T3](https://www.kali.org/docs/arm/nanopc-t/)
- [NanoPi NEO Plus2](https://www.kali.org/docs/arm/nanopi-neo-plus2/)
- [ODROID-C0/C1/C1+](https://www.kali.org/docs/arm/odroid-c/)
- [ODROID-C2](https://www.kali.org/docs/arm/odroid-c2/)
- [ODROID-U2/U3](https://www.kali.org/docs/arm/odroid-u/)
- [ODROID-XU3](https://www.kali.org/docs/arm/odroid-xu3/)
- [Pinebook](https://www.kali.org/docs/arm/pinebook/)
- [Pinebook Pro](https://www.kali.org/docs/arm/pinebook-pro/)
- [Radxa Zero (eMMC)](https://www.kali.org/docs/arm/radxa-zero-emmc/)
- [Radxa Zero (sdcard)](https://www.kali.org/docs/arm/radxa-zero-sdcard/)
- [Raspberry Pi 1 (Original)](https://www.kali.org/docs/arm/raspberry-pi/)
- [Raspberry Pi 2](https://www.kali.org/docs/arm/raspberry-pi-2/)
- [Raspberry Pi 3](https://www.kali.org/docs/arm/raspberry-pi-3/)
- [Raspberry Pi 4](https://www.kali.org/docs/arm/raspberry-pi-4/)
- [Raspberry Pi 400](https://www.kali.org/docs/arm/raspberry-pi-400/)
- [Raspberry Pi 5](https://www.kali.org/docs/arm/raspberry-pi-5/)
- [Raspberry Pi 2 v1.2](https://www.kali.org/docs/arm/raspberry-pi-64-bit/)
- [Raspberry Pi Zero](https://www.kali.org/docs/arm/raspberry-pi-zero/)
- [Raspberry Pi Zero 2 W](https://www.kali.org/docs/arm/raspberry-pi-zero-2-w/)
- [Raspberry Pi-Tail Zero 2 W](https://www.kali.org/docs/arm/raspberry-pi-zero-2-w-pi-tail/)
- [Raspberry Pi Zero W](https://www.kali.org/docs/arm/raspberry-pi-zero-w/)
- [Raspberry Pi Zero W P4wnP1 A.L.O.A](https://www.kali.org/docs/arm/raspberry-pi-zero-w-p4wnp1-aloa/)
- [Raspberry Pi-Tail Zero W](https://www.kali.org/docs/arm/raspberry-pi-zero-w-pi-tail/)
- [RIoTboard](https://www.kali.org/docs/arm/riotboard/)
- [Trimslice](https://www.kali.org/docs/arm/trimslice/)
- [USB Armory MKI](https://www.kali.org/docs/arm/usb-armory-mki/)
- [USB Armory MKII](https://www.kali.org/docs/arm/usb-armory-mkii/)
- [Using the Raspberry Pi Imager software to write Kali Raspberry Pi Images](https://www.kali.org/docs/arm/using-rpi-imager-to-write-raspberry-pi-images/)
- [Utilite Pro](https://www.kali.org/docs/arm/utilite-pro/)
- [Running x86 code on ARM devices](https://www.kali.org/docs/arm/x86-on-arm/)
- [Building NetHunter](https://www.kali.org/docs/nethunter/building-nethunter/)
- [Installing Kali NetHunter](https://www.kali.org/docs/nethunter/installing-nethunter/)
- [Installing NetHunter on the Gemini PDA](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-gemini-pda/)
- [Installing NetHunter on the OnePlus 5T](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-oneplus-5t/)
- [Installing NetHunter on the OnePlus 7](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-oneplus-7/)
- [Installing NetHunter on the OnePlus One](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-oneplus-one/)
- [Installing NetHunter on the Samsung Galaxy S10](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-samsung-galaxy-s10/)
- [Installing NetHunter on the TicWatch Pro](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-ticwatch-pro/)
- [Installing NetHunter on the TicWatch Pro 3](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-ticwatch-pro-3/)
- [Installing NetHunter on the Xiaomi Mi A2](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-xiaomi-mi-a2/)
- [Installing NetHunter on the Xiaomi Mi A3](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-xiaomi-mi-a3/)
- [NetHunter Audio](https://www.kali.org/docs/nethunter/nethunter-audio/)
- [NetHunter BadUSB Attack](https://www.kali.org/docs/nethunter/nethunter-badusb/)
- [NetHunter Bluetooth-Arsenal](https://www.kali.org/docs/nethunter/nethunter-btarsenal/)
- [NetHunter CARsenal](https://www.kali.org/docs/nethunter/nethunter-carsenal/)
- [NetHunter Chroot Manager](https://www.kali.org/docs/nethunter/nethunter-chroot-manager/)
- [NetHunter Components](https://www.kali.org/docs/nethunter/nethunter-components/)
- [NetHunter Custom Commands](https://www.kali.org/docs/nethunter/nethunter-custom-commands/)
- [NetHunter DuckHunter Attacks](https://www.kali.org/docs/nethunter/nethunter-duckhunter/)
- [NetHunter EvilTwin](https://www.kali.org/docs/nethunter/nethunter-eviltwin/)
- [NetHunter HID Keyboard Attacks](https://www.kali.org/docs/nethunter/nethunter-hid-attacks/)
- [NetHunter Home Screen](https://www.kali.org/docs/nethunter/nethunter-home-screen/)
- [NetHunter Kali Services](https://www.kali.org/docs/nethunter/nethunter-kali-services/)
- [NetHunter Kernel](https://www.kali.org/docs/nethunter/nethunter-kernel/)
- [Patching the Kernel](https://www.kali.org/docs/nethunter/nethunter-kernel-1-patching/)
- [Configuring the Kernel - General](https://www.kali.org/docs/nethunter/nethunter-kernel-2-config-1/)
- [Configuring the Kernel - Network](https://www.kali.org/docs/nethunter/nethunter-kernel-3-config-2/)
- [Configuring the Kernel - Wifi](https://www.kali.org/docs/nethunter/nethunter-kernel-4-config-3/)
- [Configuring the Kernel - SDR](https://www.kali.org/docs/nethunter/nethunter-kernel-5-config-4/)
- [Configuring the 3.x Kernel - USB](https://www.kali.org/docs/nethunter/nethunter-kernel-6-config-5/)
- [Configuring the 4.x Kernel - USB](https://www.kali.org/docs/nethunter/nethunter-kernel-7-config-6/)
- [Adding your device](https://www.kali.org/docs/nethunter/nethunter-kernel-8-adding-your-device/)
- [Configuring the Kernel - NFS](https://www.kali.org/docs/nethunter/nethunter-kernel-8-config-7/)
- [Configuring the Kernel - CAN](https://www.kali.org/docs/nethunter/nethunter-kernel-9-config-8/)
- [NetHunter Application - KeX](https://www.kali.org/docs/nethunter/nethunter-kex/)
- [NetHunter KeX Manager](https://www.kali.org/docs/nethunter/nethunter-kex-manager/)
- [NetHunter MAC Changer](https://www.kali.org/docs/nethunter/nethunter-mac-changer/)
- [NetHunter Modules](https://www.kali.org/docs/nethunter/nethunter-modules/)
- [NetHunter Metasploit Payload Generator](https://www.kali.org/docs/nethunter/nethunter-mpg/)
- [NetHunter Nmap Scan](https://www.kali.org/docs/nethunter/nethunter-nmap/)
- [NetHunter Rootless](https://www.kali.org/docs/nethunter/nethunter-rootless/)
- [NetHunter Exploit Database SearchSploit](https://www.kali.org/docs/nethunter/nethunter-searchsploit/)
- [NetHunter Social Engineer Toolkit](https://www.kali.org/docs/nethunter/nethunter-set/)
- [NetHunter Settings](https://www.kali.org/docs/nethunter/nethunter-settings/)
- [NetHunter Application - Terminal](https://www.kali.org/docs/nethunter/nethunter-terminal/)
- [NetHunter USB-Arsenal](https://www.kali.org/docs/nethunter/nethunter-usbarsenal/)
- [NetHunter Wardriving](https://www.kali.org/docs/nethunter/nethunter-wardriving/)
- [NetHunter WifiPumpkin](https://www.kali.org/docs/nethunter/nethunter-wifipumpkin/)
- [NetHunter WPS Attacks](https://www.kali.org/docs/nethunter/nethunter-wps/)
- [Porting NetHunter to New Devices manually](https://www.kali.org/docs/nethunter/porting-nethunter/)
- [Porting NetHunter to New Devices with kernel builder](https://www.kali.org/docs/nethunter/porting-nethunter-kernel-builder/)
- [Testing Checklist](https://www.kali.org/docs/nethunter/testing-checklist/)
- [Wireless Cards and NetHunter](https://www.kali.org/docs/nethunter/wireless-cards/)
- [NetHunter Pro - Enable OTG in SDM845 (OnePlus6/6T and POCO F1)](https://www.kali.org/docs/nethunter-pro/enable-otg-sdm845/)
- [Waydroid on NetHunter Pro](https://www.kali.org/docs/nethunter-pro/waydroid/)
