# 07 · 加密磁盘与 LUKS

> 对应官方章节：<https://www.kali.org/docs/installation/> 与 <https://www.kali.org/docs/usb/>
> 本篇覆盖官方文档 20 篇，重点精读「安装时全盘加密」「Live USB 加密持久化」「全加密独立 USB 安装」3 篇。

## 本节速览

| 官方文档 | 中文要点 | 链接 |
|----------|----------|------|
| Installing Kali Linux | 单系统安装 + **Encrypted LVM（LUKS 全盘加密）** | <https://www.kali.org/docs/installation/hard-disk-install/> |
| Adding Encrypted Persistence to a Kali Linux Live USB Drive | Live USB 上做 **LUKS 加密持久化分区** | <https://www.kali.org/docs/usb/usb-persistence-encryption/> |
| Adding Persistence to a Kali Linux Live USB Drive | 非加密的普通持久化（对照） | <https://www.kali.org/docs/usb/usb-persistence/> |
| Standalone Kali Linux 2021.4 Installation on a USB Drive, Fully Encrypted | 整块 U 盘完全加密的独立系统 | <https://www.kali.org/docs/usb/usb-standalone-encrypted/> |
| Making a Kali Bootable USB Drive (Linux) | `dd` 写盘与 Etcher 写盘 | <https://www.kali.org/docs/usb/live-usb-install-with-linux/> |
| Updating Kali Linux on USB | 持久化 USB 的更新方式 | <https://www.kali.org/docs/usb/updating-kali-on-usb/> |
| Verifying USB Write | 写盘后校验内容与校验和 | <https://www.kali.org/docs/usb/verify-usb-write/> |
| BTRFS Install (Kali Unkaputtbar) | BTRFS 快照做「时间回滚」 | <https://www.kali.org/docs/installation/btrfs/> |
| Dual Booting Kali with Windows / Linux / macOS | 三种双系统共存 | <https://www.kali.org/docs/installation/dual-boot-kali-with-windows/> |
| Deploying Kali over Network PXE Install | 网络无人值守安装（可预置加密） | <https://www.kali.org/docs/installation/network-pxe/> |

完整 20 篇清单见文末「官方原文索引」。

## 核心知识

### 为什么要全盘加密（FDE）

笔记本电脑、U 盘、树莓派 SD 卡极易丢失。渗透测试人员设备里往往存着**客户网络拓扑、抓包、凭据、报告草稿**。没有 FDE，只要拆下硬盘挂到另一台机器上，数据就是明文。Kali 官方文档在 USB 加密持久化页里给了一个非常明确的态度：**「作为渗透测试者，我们经常带着敏感数据出差，所以尽量全盘加密」**。

### LUKS 原理

LUKS（Linux Unified Key Setup）是 Linux 上事实标准的磁盘加密格式，由 `cryptsetup` 管理。理解它要抓住三层结构：

```text
┌──────────────────────────────────────────┐
│ LUKS Header（明文，固定大小，可单独备份） │
│  ├─ LUKS1: 通常 2 MiB                     │
│  ├─ LUKS2: 默认约 16 MiB                  │
│  ├─ Cipher / Mode / Hash 元数据           │
│  └─ Key Slots（8 个，LUKS1；LUKS2 支持更多）│
│      每个 slot = KDF 后的密钥 + 加密的      │
│      主密钥（master key）密文               │
└──────────────────────────────────────────┘
┌──────────────────────────────────────────┐
│ Payload（真正的数据区，被 master key 加密） │
└──────────────────────────────────────────┘
```

关键概念：

- **Master key（主密钥）**：真正加密数据的密钥，随机生成，**永远不会以明文落盘**。它被每个 key slot 各自加密一份。
- **Key slot（密钥槽）**：每个槽存一份「被 KDF 处理过的口令 → 加密后的 master key」。所以**换密码不重加密数据**，只是重写某个 slot（`luksChangeKey`）。
- **PBKDF（口令派生函数）**：把人类口令拉伸成密钥。
  - **LUKS1 默认 `pbkdf2`**。
  - **LUKS2 默认 `argon2id`**（本机 `cryptsetup 2.8.7` 实测：`Default PBKDF for LUKS2: argon2id, Iteration time: 2000, Memory required: 1048576kB, Parallel threads: 4`）。
  - argon2id 是**内存硬**函数，强烈抵抗 GPU/ASIC 爆破——这是 LUKS2 相对 LUKS1 最大的安全提升。
- **LUKS1 vs LUKS2**：
  - LUKS2 header 冗余（有备份头），**抗单点损坏**；LUKS1 头一坏，数据基本报废。
  - LUKS2 用了 JSON 元数据，支持 argon2id、token（可对接 FIDO2/TPM）。
  - LUKS2 支持 `luksHeaderBackup` 只备份必要部分；LUKS1 头很小可整块备份。
  - 新装 Kali 默认就是 **LUKS2**（`cryptsetup` 2.x 起 `luksFormat` 默认 LUKS2）。

### Kali 里 LUKS 出现的两个场景

1. **安装时全盘加密**：安装器菜单选 `Guided - use entire disk and set up encrypted LVM`。安装器会先做一遍**安全擦除（secure wipe，随盘大小可能耗时数小时，可跳过）**，再让你输两遍口令。
2. **Live USB 加密持久化**：手动在 U 盘空余空间建第三个分区 → `cryptsetup luksFormat` → 写 `persistence.conf`。

这两条路径互不相同：**场景 1 加密的是系统盘，场景 2 只加密「持久化数据分区」**（Live 系统本身仍是明文的 squashfs）。

## 关键文档精读

### Installing Kali Linux（安装时全盘加密）

- **它解决什么问题**：在裸机或 VM 上装一个单系统、全盘加密的 Kali。
- **操作步骤**（安装器交互，无命令行）：
  1. UEFI 里 **关闭 Secure Boot**——Kali 内核未签名，Secure Boot 不认。
  2. 启动安装镜像 → 选 `Graphical install` 或 `Install`。
  3. 语言 / 地区 / 键盘 → 网络（DHCP 会自动探测）→ 主机名 → 普通用户账号（全名 + 用户名 + 强密码）。
  4. **磁盘分区**：干净的盘会看到 4 个选项，选
     **`Guided - use entire disk and set up encrypted LVM`**
     （想双系统就选 `Guided - use the largest continuous free space`；想精细控制选 `Manual`）。
  5. 选目标磁盘 → 选择「All files in one partition」（不确定时的推荐项）。
  6. 最后确认磁盘配置（**这一步之后改动不可逆**）。
  7. **Encrypted LVM**：Kali 开始安全擦除磁盘，然后要求输入 **LVM 口令（要输两遍）**。
     - ⚠️ 官方明确警告：口令太弱会有 weak passphrase 提示。
     - ⚠️ 安全擦除**可能耗时数小时**（取决于盘容量与速度）；官方说「如果你愿意冒险，可以跳过」。
  8. 代理信息 → 选择要装的 metapackages（默认即可）→ 确认安装 GRUB → **选择 GRUB 装到哪块盘（默认不会帮你选任何盘！）**。
  9. 重启进入系统。**之后每次开机都要先输这个口令**。
- **验证方式**：
  ```bash
  lsblk                                  # 应能看到 crypt 分区 + LVM 的 kali--vg-* 逻辑卷
  ls /dev/mapper/                        # 出现 crypt / 卷组名
  sudo cryptsetup luksDump /dev/sda3      # 替换成你的 LUKS 分区；看 Version / Cipher / Keyslots
  df -h /                                 # 根分区应是 LVM 逻辑卷（/dev/mapper/kali--vg-root）
  ```
- **坑**：
  - **GRUB 默认不预选磁盘**，漏选会导致装完无法引导。
  - 官方文档示例里的口令叫「LVM password」，它其实就是 **LUKS passphrase**。
  - 装完**忘记口令 = 数据永久不可恢复**。LUKS 没有后门、没有厂商恢复流程。
  - Secure Boot 与 Kali 未签名内核冲突——这是安装失败的头号原因之一（见 [11-故障排查](11-故障排查.md)）。

### Adding Encrypted Persistence to a Kali Linux Live USB Drive

- **它解决什么问题**：U 盘起 Live Kali，但希望重启后能**保留文件/配置/测试结果**，且这些数据是加密的。
- **前置**：已按 `live-usb-install-with-linux` 把 ISO 写进 U 盘；有 root 或 `sudo`。
- **⚠️ 前置警告**：官方专门强调 `sdX` 是**占位符**，`/dev/sdX` 不会覆盖任何真实设备（防止文档被照抄误伤）。实际执行必须换成你自己的设备名（用 `lsblk` 确认），**写错设备名会摧毁那块盘上的数据**。

- **操作步骤（官方 0x01–0x07，命令逐条照抄）**：

  **0x01 把 ISO 写进 U 盘**（如果你还没写）：
  ```bash
  # ⚠️ /dev/sdX 必须换成真实设备名；写错会清掉目标盘全部数据
  sudo dd if=kali-linux-2026.2-live-amd64.iso of=/dev/sdX conv=fsync bs=4M
  sudo parted /dev/sdX print
  ```
  `parted` 输出会显示两个分区：`1`（约 4.9 GB，`boot, hidden`）和 `2`（约 4 MB）。

  **0x02 在空余空间建一个持久化分区**：
  ```bash
  sudo fdisk /dev/sdX <<< $(printf "p\nn\np\n\n\n\np\nw")
  lsblk /dev/sdX      # 新的第三个分区应为 /dev/sdX3
  ```

  **0x03 用 LUKS 加密这个分区**：
  ```bash
  # ⚠️ 会不可逆地覆盖 /dev/sdX3 上的数据
  sudo cryptsetup --verbose --verify-passphrase luksFormat /dev/sdX3
  ```
  输出会警告 `This will overwrite data on /dev/sdX3 irrevocably.`，必须**全大写输入 `YES`**。

  **0x04 打开（解锁）加密分区**：
  ```bash
  sudo cryptsetup luksOpen /dev/sdX3 my_usb
  ```

  **0x05 建文件系统并打上 `persistence` 标签**（标签名必须是 `persistence`，Live 启动项靠它找分区）：
  ```bash
  sudo mkfs.ext4 -L persistence /dev/mapper/my_usb
  ```

  **0x06 挂载并写 `persistence.conf`**：
  ```bash
  sudo mkdir -pv /mnt/my_usb
  sudo mount -v /dev/mapper/my_usb /mnt/my_usb
  echo "/ union" | sudo tee /mnt/my_usb/persistence.conf
  sudo umount -v /mnt/my_usb
  ```
  `/ union` 的含义：把整个 `/` 联合挂载（union）到持久化层，即**全盘变动都保留**。

  **0x07 关闭加密分区**：
  ```bash
  sudo cryptsetup luksClose /dev/mapper/my_usb
  reboot
  ```
- **验证方式**：
  - 重启时选择引导菜单里的 **`Live USB Encrypted Persistence`** 项（不是普通 `Live`）。
  - 起来后建个文件 `touch /root/persist-test`，重启再看文件是否还在。
  - `sudo cryptsetup luksDump /dev/sdX3` 应显示 LUKS2 header 与 1 个已用 keyslot。
- **坑**：
  - **必须从「Encrypted Persistence」这项启动**，从普通 Live 启动是看不到持久化的。
  - `mkfs.ext4 -L persistence` 的标签**写错就彻底不生效**，且不会报错。
  - `fdisk` 那串 heredoc 里的空行顺序很关键，跑之前先 `lsblk` 备份当前分区表。

### 紧急自毁（Nuke Password）与 LUKS header 备份

官方在 USB 加密持久化文档末尾附了一整套「旅行时被胁迫怎么办」的方案。这是**高风险操作**，完整流程如下：

```bash
# 1. 安装 nuke password 工具
sudo apt install -y cryptsetup-nuke-password
sudo dpkg-reconfigure cryptsetup-nuke-password
# nuke 口令的哈希被存进 initrd，对所有开机可解锁的加密分区生效

# 2. 备份 LUKS keyslot 并加密备份文件
# ⚠️ 这一步是「救命稻草」，务必在真的用 nuke 之前做
sudo cryptsetup luksHeaderBackup --header-backup-file luksheader.back /dev/sdX3
sudo openssl enc -e -aes-256-cbc -in luksheader.back -out luksheader.back.enc
ls -lh luksheader.back*        # 本例约 16 MB / 17 MB
file luksheader.back*          # 确认 .enc 是 "openssl enc'd data"

# 3. 安全擦除明文 header
sudo shred -v luksheader.back

# 4. 使用时：在开机口令提示处输入 nuke password（而不是真口令）
#    这会让加密数据变得不可用

# 5. 恢复：解密备份 + 还原 header
sudo openssl enc -d -aes-256-cbc -in luksheader.back.enc -out luksheader.back
sudo cryptsetup luksHeaderRestore --header-backup-file luksheader.back /dev/sdc3
#    会警告 "Device /dev/sdc3 already contains LUKS2 header. Replacing header will destroy existing keyslots."
```

⚠️⚠️ **风险提示**：

- **把 nuke password 输成开机口令 = 自我销毁**。且这一步发生在启动早期，输错了就没有第二次机会。
- **没有 header 备份，nuke 之后数据永久无法恢复**。备份必须加密后**离线存放在另一台设备**上。
- `luksHeaderRestore` 会**销毁现有 keyslots**，会覆盖你在 nuke 之后新加的密钥。
- 这只是应对物理胁迫的技术手段，**不能替代法律合规与数据分级**。

### Standalone Kali Linux on USB Drive, Fully Encrypted

- **它解决什么问题**：做一块**整盘全加密的独立 Kali 系统 U 盘**，插到任何机器上启动都是一个完整的加密 Kali（不同于 Live + 持久化）。
- **它与「Live + 加密持久化」的区别**：
  - Live 持久化：系统本体是明文 squashfs，只有数据分区加密。
  - 独立全加密：**整个系统盘（含 `/boot` 之外的根文件系统）都在 LUKS 里**，本质是「把 Kali 装进 U 盘并开 Encrypted LVM」。
- **概要（官方 Outline）**：准备 → 用 Kali 裸机安装器 → 用 Xubuntu 20.04 LTS 安装器做引导体操 → 对目标 U 盘分区 → 装 Kali → 配置安装器 → 分区 → Btrfs 调整 → 文件系统表（fstab）→ 实际安装 → 生成 initramfs → 收尾 → 创建引导装载器 → 使用与联网 → 硬件限制 → 自定义内核编译 → 密码学备注。
- ⚠️ **这是一篇长流程、强耦合的实践记录，涉及大量手工分区与 bootloader 操作**。命令细节必须以官方原文为准：
  <https://www.kali.org/docs/usb/usb-standalone-encrypted/>
- **坑**：USB 接口的速度决定体验（USB 3.0 起步）；某些机器的固件对「从 U 盘引导加密根」支持不好；文中还提到「硬件限制」与「需要自行编译内核」的情况。

## 实操清单

- [ ] 写盘前先 `lsblk` 记录目标设备名，确认不是系统盘
- [ ] 安装 Kali 时选择 `Guided - use entire disk and set up encrypted LVM`
- [ ] 安装完立刻 `sudo cryptsetup luksDump <设备>`，把 **LUKS header 备份**存到离线介质
- [ ] `sudo cryptsetup luksHeaderBackup --header-backup-file luksheader.back <设备>`
- [ ] 记录 UUID：`sudo blkid <设备>` 与 `sudo cryptsetup luksUUID <设备>`
- [ ] 检查 `/etc/crypttab` 里加密卷的条目（系统盘加密时由安装器自动生成）
- [ ] 做一次「口令输错」演练：确认系统不会误挂载明文
- [ ] 若用 nuke password：**先做并在离线机上验证 header 备份可还原**
- [ ] 定期验证备份：`sudo cryptsetup isLuks <设备>`、`file luksheader.back.enc`

## 排错

| 现象 | 原因 | 解决 |
|------|------|------|
| 安装时看不到「encrypted LVM」选项 | 用的是 Live 镜像而非 Installer 镜像 | 下载标记为 **Installer** 的镜像 |
| 装完开机卡在 `GRUB rescue>` | GRUB 未正确安装或装错盘 | 用 Live USB 启动 + `grub-install` 修复；参见 [11-故障排查](11-故障排查.md) |
| 开机提示 `cryptsetup: cryptsetup failed, bad password or options?` | 口令错 / 键盘布局不一致 / initramfs 与 header 不匹配 | 切换 TTY 或在 GRUB 下用 `init=/bin/sh` 调试；确认键盘布局 |
| `luksOpen` 报 `Device /dev/sdX3 is not a valid LUKS device` | 设备名错，或分区未 `luksFormat` | `sudo cryptsetup isLuks /dev/sdX3` 验证 |
| `mkfs.ext4 -L persistence` 做完但重启没生效 | 标签不是 `persistence`，或启动了普通 Live 项 | 重新 `mkfs.ext4 -L persistence`；引导菜单选 Encrypted Persistence |
| `luksHeaderRestore` 后仍有旧 keyslot | restore 覆盖 header，但 slot 内容以备份为准 | 正常现象；如需清理用 `cryptsetup luksKillSlot` |
| 忘记口令 | LUKS 无后门 | **无解**，只能靠事先备份的 header + 已知口令，或从其他备份恢复数据 |

### 常用 cryptsetup 命令速查（本机 `cryptsetup 2.8.7 --help` 实查）

```bash
cryptsetup luksFormat <设备> [<密钥文件>]     # 格式化 LUKS 设备
cryptsetup luksOpen <设备> <名字>            # 解锁并在 /dev/mapper/<名字> 暴露
cryptsetup luksClose <名字>                  # 关闭
cryptsetup luksDump <设备>                   # 查看 header：版本/算法/keyslot
cryptsetup luksUUID <设备>                   # 打印 LUKS UUID
cryptsetup isLuks <设备>                     # 判断是否为 LUKS 设备
cryptsetup luksAddKey <设备> [<新密钥文件>]   # 新增口令
cryptsetup luksChangeKey <设备>              # 修改口令（不重加密数据）
cryptsetup luksRemoveKey <设备> <密钥文件>    # 移除某个口令
cryptsetup luksKillSlot <设备> <槽号>        # 抹掉某个 keyslot
cryptsetup luksConvertKey <设备>             # 把密钥转换到新的 PBKDF 参数
cryptsetup luksHeaderBackup <设备> --header-backup-file <文件>
cryptsetup luksHeaderRestore <设备> --header-backup-file <文件>
cryptsetup luksSuspend / luksResume <设备>   # 挂起/恢复（挂起会清空密钥）
cryptsetup convert <设备>                    # LUKS1 <-> LUKS2 互转
cryptsetup config <设备>                     # 设置 LUKS2 持久配置项
cryptsetup encrypt / decrypt <设备>          # 原地加/解密 LUKS2（新式）
cryptsetup token <add|remove|import|export> <设备>   # LUKS2 token
```

> 以上 action 名称来自本机 `cryptsetup --help` 的 action 列表，可离线复核。

## 官方原文索引

- [Bare-bones Kali](https://www.kali.org/docs/installation/barebone-kali/)
- [BTRFS Install (Kali Unkaputtbar)](https://www.kali.org/docs/installation/btrfs/)
- [Dual Booting Kali with Linux](https://www.kali.org/docs/installation/dual-boot-kali-with-linux/)
- [Dual Booting Kali with macOS/OS X](https://www.kali.org/docs/installation/dual-boot-kali-with-mac/)
- [Dual Booting Kali with Windows](https://www.kali.org/docs/installation/dual-boot-kali-with-windows/)
- [Installing Kali Linux](https://www.kali.org/docs/installation/hard-disk-install/)
- [Installing Kali on Mac Hardware](https://www.kali.org/docs/installation/hard-disk-install-on-mac/)
- [Kali Installation Sizes](https://www.kali.org/docs/installation/installation-sizes/)
- [Installing old i386 images](https://www.kali.org/docs/installation/installing-old-i386/)
- [Deploying Kali over Network PXE Install](https://www.kali.org/docs/installation/network-pxe/)
- [USB Boot in VMware](https://www.kali.org/docs/usb/boot-usb-in-a-vm/)
- [USB Boot in VirtualBox](https://www.kali.org/docs/usb/boot-usb-in-virtualbox/)
- [Making a Kali Bootable USB Drive (Linux)](https://www.kali.org/docs/usb/live-usb-install-with-linux/)
- [Making a Kali Bootable USB Drive (macOS/OS X)](https://www.kali.org/docs/usb/live-usb-install-with-mac/)
- [Making a Kali Bootable USB Drive on Windows](https://www.kali.org/docs/usb/live-usb-install-with-windows/)
- [Updating Kali Linux on USB](https://www.kali.org/docs/usb/updating-kali-on-usb/)
- [Adding Persistence to a Kali Linux Live USB Drive](https://www.kali.org/docs/usb/usb-persistence/)
- [Adding Encrypted Persistence to a Kali Linux Live USB Drive](https://www.kali.org/docs/usb/usb-persistence-encryption/)
- [Standalone Kali Linux 2021.4 Installation on a USB Drive, Fully Encrypted](https://www.kali.org/docs/usb/usb-standalone-encrypted/)
- [Verifying USB Write](https://www.kali.org/docs/usb/verify-usb-write/)
