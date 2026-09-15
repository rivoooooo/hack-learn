# kali-meta

> Metapackage with dependencies common to all Kali’s desktops This metapackage depends on Kali packages that should be installed on all desktop installations of Kali Linux. This metapackage is a dependency of all kali-desktop-* packages.

> **功能分类**：通用工具 ｜ **Kali 包**：`kali-meta` ｜ **官方文档**：<https://www.kali.org/tools/kali-meta/>

## 1. 安装

```bash
sudo apt update
sudo apt install kali-desktop-core
```

| 项目 | 内容 |
|------|------|
| 版本 | 2026.3.8 |
| 架构 | any |
| 可执行命令 | `kali-desktop-core`、`kali-desktop-e17`、`kali-desktop-gnome`、`kali-desktop-i3`、`kali-desktop-i3-gaps`、`kali-desktop-kde`、`kali-desktop-live`、`kali-desktop-lxde`、`kali-desktop-mate`、`kali-desktop-xfce`、`kali-linux-arm`、`kali-linux-core`、`kali-linux-default`、`kali-linux-everything`、`kali-linux-firmware`、`kali-linux-firmware-graphics`、`kali-linux-headless`、`kali-linux-labs`、`kali-linux-large`、`kali-linux-nethunter`、`kali-linux-wsl`、`kali-nethunter-core`、`kali-nethunter-full`、`kali-nethunter-nano`、`kali-sbc-allwinner`、`kali-sbc-amlogic`、`kali-sbc-qualcomm`、`kali-sbc-raspberrypi`、`kali-sbc-rockchip`、`kali-system-cli`、`kali-system-core`、`kali-system-gui`、`kali-tools-802-11`、`kali-tools-bluetooth`、`kali-tools-crypto-stego`、`kali-tools-database`、`kali-tools-detect`、`kali-tools-exploitation`、`kali-tools-forensics`、`kali-tools-fuzzing`、`kali-tools-gpu`、`kali-tools-hardware`、`kali-tools-identify`、`kali-tools-information-gathering`、`kali-tools-passwords`、`kali-tools-post-exploitation`、`kali-tools-protect`、`kali-tools-recover`、`kali-tools-reporting`、`kali-tools-respond`、`kali-tools-reverse-engineering`、`kali-tools-rfid`、`kali-tools-sdr`、`kali-tools-sniffing-spoofing`、`kali-tools-social-engineering`、`kali-tools-top10`、`kali-tools-voip`、`kali-tools-vulnerability`、`kali-tools-web`、`kali-tools-windows-resources`、`kali-tools-wireless` |
| 依赖 | `dbus-user-session`、`dbus-x11` |
| 安装体积 | 13 KB |
| 官网 | <https://www.kali.org> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/kali-meta> |
| 包追踪 | <https://pkg.kali.org/pkg/kali-meta> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
kali-desktop-core -h          # 查看用法
man kali-desktop-core         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

> 官方页面未内嵌该工具的 help 原文，请在本机执行：

```bash
kali-desktop-core -h
kali-desktop-e17 -h
kali-desktop-gnome -h
kali-desktop-i3 -h
kali-desktop-i3-gaps -h
kali-desktop-kde -h
kali-desktop-live -h
kali-desktop-lxde -h
kali-desktop-mate -h
kali-desktop-xfce -h
kali-linux-arm -h
kali-linux-core -h
kali-linux-default -h
kali-linux-everything -h
kali-linux-firmware -h
kali-linux-firmware-graphics -h
kali-linux-headless -h
kali-linux-labs -h
kali-linux-large -h
kali-linux-nethunter -h
kali-linux-wsl -h
kali-nethunter-core -h
kali-nethunter-full -h
kali-nethunter-nano -h
kali-sbc-allwinner -h
kali-sbc-amlogic -h
kali-sbc-qualcomm -h
kali-sbc-raspberrypi -h
kali-sbc-rockchip -h
kali-system-cli -h
kali-system-core -h
kali-system-gui -h
kali-tools-802-11 -h
kali-tools-bluetooth -h
kali-tools-crypto-stego -h
kali-tools-database -h
kali-tools-detect -h
kali-tools-exploitation -h
kali-tools-forensics -h
kali-tools-fuzzing -h
kali-tools-gpu -h
kali-tools-hardware -h
kali-tools-identify -h
kali-tools-information-gathering -h
kali-tools-passwords -h
kali-tools-post-exploitation -h
kali-tools-protect -h
kali-tools-recover -h
kali-tools-reporting -h
kali-tools-respond -h
kali-tools-reverse-engineering -h
kali-tools-rfid -h
kali-tools-sdr -h
kali-tools-sniffing-spoofing -h
kali-tools-social-engineering -h
kali-tools-top10 -h
kali-tools-voip -h
kali-tools-vulnerability -h
kali-tools-web -h
kali-tools-windows-resources -h
kali-tools-wireless -h
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install kali-desktop-core`，再执行 `kali-desktop-core --version` 2>/dev/null || `kali-desktop-core -V`
- [ ] **2.** **读官方帮助** —— `kali-desktop-core -h`，需要细节时 `man kali-desktop-core`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `kali-desktop-core -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/kali-meta/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/kali-meta/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/kali-meta/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
