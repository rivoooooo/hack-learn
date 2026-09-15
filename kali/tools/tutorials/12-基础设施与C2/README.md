# 12 · 基础设施与 C2（Infrastructure & Command and Control）

> 本目录是 Kali 工具精讲教程的第 12 篇：**把「能打到」变成「打得稳、藏得住、收得到」**。
> 主干闭环：**载荷生成 → 托管（下载点）→ 前置重定向（隐藏 C2）→ C2 会话管理 → 内网通路 → 记录与清理**。
> 上游：[`../06-漏洞利用/`](../06-漏洞利用/)、[`../08-后渗透/`](../08-后渗透/) ｜ 下游：[`../11-社会工程与报告/`](../11-社会工程与报告/)
> 相关索引：[`../../index.md`](../../index.md) ｜ 分类速查：[`../../catalog/post-exploitation.md`](../../catalog/post-exploitation.md)、[`../../by-attack/command-and-control.md`](../../by-attack/command-and-control.md)、[`../../by-attack/resource-development.md`](../../by-attack/resource-development.md)

---

## 工具清单

| 工具 | 一句话 | 难度 | 教程 |
|------|--------|------|------|
| **sliver** | 现代化 C2：mTLS/HTTPS/DNS 信道、动态编译植入体、内置 socks5/portfwd、多人协作 | ⭐⭐⭐⭐ | [`sliver.md`](sliver.md) |
| **socat** | 万能中继：端口转发、TLS 隧道、TTY 升级、简易重定向器（一条命令） | ⭐⭐⭐ | [`socat.md`](socat.md) |
| **apache2** | 重定向器与 Payload 托管：按 UA/路径/域名条件分流 + 反向代理 + TLS 终结 | ⭐⭐⭐ | [`apache2.md`](apache2.md) |

> **三者的分工**：
> - **sliver** = **控制平面**（植入体、会话、信道、内网代理）
> - **apache2** = **应用层前置**（把 C2 藏在"正常网站"后面，按条件分流）
> - **socat** = **传输层中继**（最简单的端口转发/TLS 隧道/TTY 升级）
>
> **关于工具替换说明**：任务清单里的 **`chisel`** 已在 [`../08-后渗透/chisel.md`](../08-后渗透/chisel.md) 写过，故本目录按其建议改用 **`socat`**；**`nginx` 不在本仓库抓取的 Kali 官方工具清单中**（清单里只有 `apache2`），因此重定向器/托管部分使用 **`apache2`**。

---

## 学习顺序

```
① 先想清楚"为什么需要基础设施"（而不是直接把 C2 暴露出去）
   → 读 sliver.md 第 1 节 + apache2.md 第 1 节

② 最小 C2 闭环（在隔离实验环境）
   sliver.md 场景 1：sliver-server → mtls 监听器 → generate → 会话

③ 内网通路（C2 自带的隧道能力）
   sliver.md 场景 2：socks5 start / portfwd / execute-assembly
   （补充：proxychains4 驱动其它工具 → ../08-后渗透/proxychains4.md）

④ 隐藏与伪装（核心技能）
   apache2.md 场景 2：TLS + mod_rewrite 条件分流 + mod_proxy 反代 + 伪装
   socat.md 场景 1：一条命令做纯端口转发（更简单的替代方案）

⑤ 载荷托管
   apache2.md 场景 1：DocumentRoot + MIME + 伪装 + 日志分析

⑥ 稳定支撑操作（TTY、UDP、串口）
   socat.md 场景 2-3：TTY 升级 / UDP 转发 / TLS 隧道

⑦ 团队与合规
   sliver.md 场景 3：multiplayer / operator / rc 脚本
   全部工具的文末"法律与伦理"：**必须读完再动手**
```

---

## 环境准备

```bash
sudo apt update
sudo apt install -y sliver socat apache2

# 配套（上游/下游章节会用到的）
sudo apt install -y metasploit-framework proxychains4 chisel openssl curl
```

验证：

```bash
for t in sliver-server sliver-client socat apache2 apache2ctl a2enmod openssl; do
  printf '%-16s %s\n' "$t" "$(command -v $t || echo MISSING)"
done

# socat 是否支持 OpenSSL（TLS 隧道的前提）
socat -V | grep -i openssl

# Apache 模块与端口
sudo a2enmod rewrite proxy proxy_http ssl headers 2>/dev/null
sudo apache2ctl -M 2>/dev/null | grep -E 'rewrite|proxy|ssl|headers'
sudo ss -lntp | grep -E ':80|:443'
```

### 环境准备清单（自检）

| 检查项 | 命令 | 期望 |
|--------|------|------|
| C2 可启动 | `sudo sliver-server` | 出现 Sliver 控制台提示符 |
| socat 支持 TLS | `socat -V \| grep -i openssl` | 有输出 |
| Apache 可用 | `curl -s http://127.0.0.1/` | 返回默认页 |
| 80/443 空闲 | `sudo ss -lntp \| grep -E ':80\|:443'` | 无冲突（或你知道谁占用） |
| 有可用域名/证书（真实演练） | `certbot` 已装 | 能签发 Let's Encrypt |
| **网络完全隔离** | `ip route` / 虚拟机网络设置 | 只有 Host-Only / 独立虚拟网络 |
| **有可回滚快照** | 虚拟机快照 | **实验前打快照**（这是纪律） |

### 练习环境（**必须隔离**）

```
┌──────────── 独立虚拟网络（Host-Only / Internal）────────────┐
│  [ Kali 攻击机 ]  192.168.56.5                              │
│      · sliver-server（C2 服务端）                            │
│      · apache2（重定向器 / 载荷托管）                         │
│      · socat（端口转发 / TTY）                               │
│                                                              │
│  [ 靶机 A ] 192.168.56.50  自建 Windows 虚拟机（未打补丁）     │
│  [ 靶机 B ] 192.168.56.10  Linux 跳板机（双网卡）             │
│  [ 内网 ]   10.10.20.0/24  只有跳板机能到达                    │
└──────────────────────────────────────────────────────────────┘
```

**必须做到**：
- 攻击机与靶机**都在你自己的控制下**；
- 网络**与互联网/生产网隔离**（避免误伤与法律风险）；
- **实验前打快照，结束后回滚**；
- **不要在真实域名/证书上做演练**，除非这确实是授权演练的基础设施。

---

## 工具选择速查

| 你的需求 | 首选 | 备选 |
|----------|------|------|
| 需要 C2（植入体/会话/信道管理） | **sliver** | `../08-后渗透/powershell-empire.md`、Metasploit |
| 需要隐藏 C2（前置重定向器） | **apache2**（按条件分流 + 反代） | **socat**（纯端口转发） |
| 需要托管载荷 | **apache2** | `python3 -m http.server`（临时、无伪装） |
| 需要把内网端口搬到本地 | **socat** 或 C2 自带的 `portfwd` | `chisel`、`ssh -L` |
| 需要 SOCKS 代理内网 | C2 自带 `socks5` | `chisel R:socks` + `proxychains4` |
| 需要多层网段 / UDP / ICMP | `../08-后渗透/ligolo-ng.md` | 多个 socat 串联（繁琐） |
| 需要把哑 shell 升级成真 TTY | **socat**（`PTY,raw,echo=0`） | `python3 -c 'import pty...'` |
| 需要 TLS 加密隧道 | **socat**（`OPENSSL-LISTEN`） | Apache + 反向代理 |
| 需要团队协作 | **sliver**（multiplayer） | —— |

---

## 核心概念速查

| 概念 | 一句话 | 详见 |
|------|--------|------|
| **C2** | Command and Control：控制被控主机的通道 | [`sliver.md`](sliver.md) 第 2 节 |
| **Implant** | 目标上运行的客户端（植入体） | [`sliver.md`](sliver.md) |
| **Session vs Beacon** | 长连接交互 vs 定时回连（抖动） | [`sliver.md`](sliver.md) |
| **Listener** | 服务端监听（mTLS/HTTPS/DNS/WireGuard） | [`sliver.md`](sliver.md) |
| **mTLS** | 双向证书验证（Sliver 默认，抗中间人） | [`sliver.md`](sliver.md) |
| **重定向器（Redirector）** | 前置服务器，只把"像植入体"的流量转给 C2 | [`apache2.md`](apache2.md)、[`socat.md`](socat.md) |
| **条件分流** | 按 UA/路径/Host 决定"转发 or 返回正常站点" | [`apache2.md`](apache2.md) 场景 2 |
| **TLS 指纹（JA3/JA4）** | 由 TLS 握手参数生成的客户端指纹（蓝队的重要线索） | [`sliver.md`](sliver.md) 第 9 节 |
| **TTY 升级** | 把哑 shell 变成可交互终端（Tab/`vi`/`top`） | [`socat.md`](socat.md) 场景 2 |
| **范围限制（`Require ip` / `range=`）** | **授权测试的合规底线**：只服务授权来源 | [`apache2.md`](apache2.md)、[`socat.md`](socat.md) |

---

## 与其它章节的衔接

| 你手上的东西 | 去哪里 |
|--------------|--------|
| 拿到了一个执行能力（命令执行/shell/WinRM） | [`sliver.md`](sliver.md)（建立 C2 会话） |
| 需要一个稳定的载荷下载点 | [`apache2.md`](apache2.md) 场景 1 |
| 想把 C2 藏起来 | [`apache2.md`](apache2.md) 场景 2、[`socat.md`](socat.md) 场景 1 |
| 需要访问内网 | [`sliver.md`](sliver.md) 场景 2、[`../08-后渗透/proxychains4.md`](../08-后渗透/proxychains4.md) |
| 需要 UDP/多层网段 | [`../08-后渗透/ligolo-ng.md`](../08-后渗透/ligolo-ng.md) |
| 拿到哑 shell 想升级 | [`socat.md`](socat.md) 场景 2 |
| 想用其它 C2 对比 | [`../08-后渗透/powershell-empire.md`](../08-后渗透/powershell-empire.md)、[`../06-漏洞利用/metasploit-framework.md`](../06-漏洞利用/metasploit-framework.md) |
| 需要社工投递这些载荷 | [`../11-社会工程与报告/gophish.md`](../11-社会工程与报告/gophish.md)、[`../11-社会工程与报告/set.md`](../11-社会工程与报告/set.md) |
| 需要记录与报告 | [`../11-社会工程与报告/cherrytree.md`](../11-社会工程与报告/cherrytree.md)、[`../11-社会工程与报告/dradis.md`](../11-社会工程与报告/dradis.md) |

---

## ⚠️ 法律与伦理（**本目录风险最高，请完整阅读**）

本目录的工具用来**建立并隐藏对被控主机的控制通道**。在未授权环境下使用，可能触犯：

- 《刑法》**第 285 条**：非法侵入计算机信息系统罪、非法获取计算机信息系统数据罪、**非法控制计算机信息系统罪**（C2 的典型行为恰好是"非法控制"）；
- 《刑法》**第 286 条**：破坏计算机信息系统罪；
- 《网络安全法》第 27 条（禁止非法侵入、干扰、破坏；禁止提供用于此类活动的程序与工具）；
- 《数据安全法》《个人信息保护法》（主机信息、凭据、文件均可能涉及）。

**七条硬性要求（缺一不可）**：

1. **书面授权必须明确覆盖"C2 植入 / 基础设施搭建"** —— 很多渗透授权书默认不包含，必须单独确认；
2. **在完全隔离的实验环境学习**：自己的攻击机 + 自己的靶机 + Host-Only 网络 + **实验前快照、实验后回滚**；
3. **绝不把 C2 服务端暴露公网**（这既会让他人利用你的设施，也会显著加重你的法律责任）；
4. **必须做范围限制**：`Require ip`（Apache）、`range=`（socat），确保只服务授权来源——**这既是合规底线，也是保护自己**；
5. **CA/证书/操作员配置是最高机密**：加密保管、不明文传输、不进入公开仓库；
6. **测试结束必须拆除**：停止监听器、删除植入体、清理持久化项、`a2dissite` + 删配置、删载荷，并保留清理记录（**日志是证据，须按约定保存后销毁**）；
7. **不做"顺手用一下"**：任何超出授权范围的动作都不是测试，而是犯罪。

> **判断标准**：如果你的实验环境能连到互联网上的任意主机，或者你的靶机不是你自己的——**那就不要执行本目录的任何命令**。
