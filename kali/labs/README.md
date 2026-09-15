# Kali 靶场与环境搭建

> 所有练习都必须跑在**你自己控制的靶场**里。本文件给出可直接执行的搭法。

---

## 0. 安全与法律红线（先读这一节）

| 事项 | 要求 |
|------|------|
| 只测试你自己的设备 | 你的虚拟机、你的靶机、你的路由器、你的 Wi-Fi |
| 公开允许测试的目标 | 例如 `scanme.nmap.org`（Nmap 官方为演示保留，**有频率限制**） |
| 授权目标 | 必须**书面授权**（SOW），并明确范围与时间窗 |
| 在线靶场 | HTB / THM / PortSwigger 等平台的靶机属于允许测试范围 |
| ⚠️ 绝对不要 | 扫描/攻击 ISP、公司内网、学校网络、公网站点、邻居的 Wi-Fi |

在中国大陆，未经授权侵入他人系统可能触犯《刑法》第 285/286 条及《网络安全法》。
**"只是扫了一下"也可能构成违法**。练习请全部在本地靶场完成。

官方政策：<https://www.kali.org/docs/policy/>

---

## 1. 推荐的整体拓扑

```
                ┌──────────────────────────────┐
                │  宿主机（你的电脑）            │
                │  ┌──────────┐  ┌──────────┐  │
                │  │  Kali VM │  │ 靶机 VM   │  │
                │  │ 攻击机    │  │ 受害者    │  │
                │  └────┬─────┘  └────┬─────┘  │
                │       └──── 仅主机/内部网络 ─┘ │
                └──────────────────────────────┘
                            ↑ 隔离，不接触真实网络
```

**关键原则**：

1. **网络隔离**：Kali 与靶机放在同一个"仅主机（Host-only）"或"内部网络（Internal）"里
2. **不桥接到真实网络**：除非你明确要测试自己的局域网设备
3. **快照先行**：靶机与 Kali 都先打快照，随便折腾
4. **一次一靶**：靶机是易受攻击的系统，**绝不要**让它接触到你的真实网络或公网

| 虚拟网络模式 | 能否出网 | 靶机能否访问宿主 | 建议 |
|--------------|----------|------------------|------|
| Host-only | ❌ | 宿主可访问靶机 | ✅ **推荐**：隔离 + 宿主可控 |
| Internal | ❌ | ❌ | ✅ 最严格隔离 |
| NAT | ✅ | （单向） | 需要联网装包时临时用 |
| Bridged | ✅ | ✅ | ⚠️ **危险**：靶机的漏洞暴露在真实网络上 |

---

## 2. Web 靶场（Docker 一键起）

Kali 里装 Docker 的官方方法见 [../docs/08-容器与虚拟化.md](../docs/08-容器与虚拟化.md)。

```bash
sudo apt update && sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER    # 免 sudo 用 docker（需要重新登录）
```

### 2.1 DVWA（最经典的入门靶场）

覆盖：SQL 注入、XSS、文件包含、文件上传、命令注入、CSRF、暴力破解。
可调难度（Low / Medium / High / Impossible），非常适合对照 WSTG 逐项练。

```bash
docker run --rm -it -p 8080:80 vulnerables/web-dvwa
# 浏览器访问 http://127.0.0.1:8080
# 默认账号：admin / password
# 首次进入先点 "Create / Reset Database"
```

⚠️ 容器里跑 DVWA 时，**不要把 8080 映射到公网可达的地址**。用 `-p 127.0.0.1:8080:80` 限制只监听本机。

### 2.2 OWASP Juice Shop（现代 SPA 靶场）

覆盖：OWASP Top 10 全类别（含 2025 版新增的供应链、异常处理等主题），
有内置的进度条（Score Board），从简单到极难共 100+ 挑战。

```bash
docker run --rm -it -p 3000:3000 bkimminich/juice-shop
# 浏览器访问 http://127.0.0.1:3000
# 无需默认账号；注册一个账号即可开始
```

💡 Juice Shop 是学 OWASP Top 10 的最佳靶场，配套练习见
[../../web-security/owasp/labs.md](../../web-security/owasp/labs.md)。

### 2.3 OWASP WebGoat

覆盖：以"课程 + 练习"形式讲漏洞原理，含 WebWolf 辅助工具（用于 SSRF、XSS 等需要外部服务的场景）。

```bash
docker run --rm -it -p 8080:8080 -p 9090:9090 webgoat/webgoat
# 主站 http://127.0.0.1:8080/WebGoat
# 辅助 http://127.0.0.1:9090/WebWolf
```

### 2.4 bWAPP

覆盖：100+ 漏洞，覆盖面极广，适合查漏补缺。

```bash
docker run --rm -it -p 8081:80 raesene/bwapp
# 访问 http://127.0.0.1:8081/bWAPP/install.php 完成初始化
# 默认账号：bee / bug
```

> 💡 Docker 镜像名与端口可能随上游更新变化，起不来时以 Docker Hub 页面为准。

---

## 3. 主机靶场（练 nmap / 密码攻击 / 提权）

### 3.1 Metasploitable2（经典 Linux 靶机）

一台**故意做得很脆弱**的 Ubuntu 虚拟机，开了大量带漏洞的服务。

```bash
docker run --rm -it tleemcjr/metasploitable2
```

⚠️ 该容器适合练**网络扫描与服务识别**。若要完整练习（含 HTTP、SMB、后门等全部服务），
更推荐官方 OVA 虚拟机镜像，可从 VulnHub 或 SourceForge 获取后导入 VirtualBox/VMware。

宿主机上先查它拿到的 IP：

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 容器ID
# 或者进 Kali 扫网段
sudo nmap -sn 192.168.56.0/24
```

默认凭据（渗透练习的经典考点）：`msfadmin` / `msfadmin`。

### 3.2 Metasploitable3

更现代、更"企业味"的靶机，有 Windows 与 Linux 两个版本，
覆盖更多真实 CVE 与域环境场景。构建较复杂，需要 Vagrant/Packer。

🔗 官方仓库：<https://github.com/rapid7/metasploitable3>

### 3.3 VulnHub

免费下载的大量单体靶机（OVA/虚拟机镜像），每题都是一次完整的夺旗。

🔗 <https://www.vulnhub.com/>

用法：下载 OVA → 导入 VirtualBox → 改为 Host-only 网络 → 从 Kali 扫描它。

⚠️ 有些靶机镜像很老（内核、服务、Python 版本），起不来是常态，不必纠结。

### 3.4 活动目录靶场（进阶）

| 项目 | 说明 |
|------|------|
| **GOAD** (Game of Active Directory) | 用 Vagrant/Terraform 一键起一个含多台机器、多个漏洞的 AD 环境，是练 AD 攻击的最佳开源方案 |
| **DetectionLab** | 偏蓝队：带日志与检测的 AD 环境 |
| **BadBlood** | 给现有 AD 灌入大量测试对象，用于练 BloodHound 分析 |

相关工具教程见 [../tools/tutorials/08-后渗透/](../tools/tutorials/08-后渗透/)。

---

## 4. 在线靶场（无需本地资源）

| 平台 | 特点 | 免费额度 |
|------|------|----------|
| **PortSwigger Web Security Academy** | 由 Burp Suite 官方出品，Web 漏洞**最系统**的免费课程 + 靶场，按漏洞类型分章节 | 完全免费 |
| **Hack The Box** | 含退役靶机（免费）、Pro Labs（AD 环境，付费） | 有免费靶机 |
| **TryHackMe** | 引导式学习路径，适合入门 | 有免费房间 |
| **PentesterLab** | 以"代码审计 + 漏洞复现"为特色 | 部分免费 |
| **OverTheWire** | 命令行/基础类挑战（Bandit 非常适合补 Linux 基础） | 免费 |

💡 **推荐组合**：
- 补 Linux 基础 → OverTheWire Bandit（配合 [../../linux/practice/](../../linux/practice/)）
- 学 Web 漏洞 → PortSwigger Academy + Juice Shop
- 练完整渗透流程 → TryHackMe 路径 → HTB 退役机
- 练 AD → GOAD 或 HTB Pro Labs

---

## 5. 环境管理最佳实践

### 5.1 快照策略

```text
装好 Kali（干净状态）        → 快照 #1  base
装完常用工具、配好网络        → 快照 #2  ready
每次做破坏性实验前            → 快照 #N  实验名
实验炸了                      → 回滚到 #2
```

VirtualBox 命令行：

```bash
VBoxManage snapshot "Kali" take "ready"
VBoxManage snapshot "Kali" list
VBoxManage snapshot "Kali" restore "ready"
```

⚠️ 快照会占用磁盘（差异磁盘），别攒几十个。

### 5.2 网络配置检查清单

```bash
# 在 Kali 里执行
ip -br addr                                  # 我的地址
ip route                                     # 我的网关
sudo nmap -sn 192.168.56.0/24                # 同网段有哪些机器（换成你的网段）
```

- [ ] Kali 与靶机在**同一网段**
- [ ] Kali **不能**直接访问公网（或至少靶机不能）
- [ ] 靶机**不能**访问真实局域网
- [ ] 已记录靶机 IP
- [ ] 已对两台机器打快照

### 5.3 让工具知道你的代理

如果靶场跑在远程（如云上），记得：

```bash
# 排除靶网段，避免被代理劫持
export no_proxy="127.0.0.1,localhost,192.168.56.0/24,10.10.10.0/24"
```

细节见 [../docs/04-网络配置与代理.md](../docs/04-网络配置与代理.md)。

---

## 6. 按学习阶段的靶场路线

| 阶段 | 目标 | 靶场 | 配套教程 |
|------|------|------|----------|
| 1 | 会用基本命令、能扫到主机 | Metasploitable2 + `nmap` | [../tools/tutorials/01-信息搜集/](../tools/tutorials/01-信息搜集/) |
| 2 | 能识别 Web 漏洞 | DVWA（逐项切换难度） | [WSTG 清单](../../web-security/owasp/wstg/checklist.md) |
| 3 | 能利用 Web 漏洞 | Juice Shop + PortSwigger Academy | [../../web-security/owasp/](../../web-security/owasp/) |
| 4 | 能打完整靶机拿 shell | VulnHub 单机靶场 | [../tools/tutorials/06-漏洞利用/](../tools/tutorials/06-漏洞利用/) |
| 5 | 能提权 | VulnHub 中高难度靶机 | [../tools/tutorials/08-后渗透/](../tools/tutorials/08-后渗透/) |
| 6 | 能打内网/AD | GOAD、HTB Pro Labs | [../../web-security/mitre-attack/](../../web-security/mitre-attack/) |
| 7 | 能做专业交付 | 任意靶场 + 报告 | [../../web-security/ptes/templates.md](../../web-security/ptes/templates.md) |

---

## 7. 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| Kali 扫不到靶机 | 不在同一虚拟网络 | 两台机器改成同一 Host-only 网络，检查 `ip addr` |
| Docker 容器里的靶机扫不到 | 容器在 NAT 网桥里 | 用 `docker inspect` 查容器 IP，或改用 `--network host`（⚠️ 降低隔离性） |
| 靶机启动后是黑屏/进不去 | 镜像太老或显卡不兼容 | 换 VBoxVGA 显卡、关 3D 加速、或直接换靶机 |
| 装了工具但命令找不到 | 没装对应包 | `apt list --installed 'kali-tools-*'`，或见 [../docs/05-包管理与软件源.md](../docs/05-包管理与软件源.md) |
| 容器起来后马上退出 | 镜像需要交互式终端 | 加 `-it` |
| 端口冲突 | 宿主已占用同端口 | 改映射端口，如 `-p 18080:80` |

---

## 8. 练习

1. **起全套靶场**：用 Docker 同时跑 DVWA、Juice Shop、WebGoat，记录各自端口，写出访问清单。
2. **网络隔离验证**：从 Kali 用 `nmap -sn` 扫出靶机，再从宿主机确认靶机**无法**访问外网。
   ```bash
   # 在靶机容器里
   ping -c 2 1.1.1.1        # 应该不通（取决于网络配置）
   ```
3. **快照演练**：在 Kali 里 `sudo rm -rf /etc/apt/sources.list.d/`（故意破坏），然后从快照回滚，验证恢复成功。
4. **写一份测试范围表**：参照 [../../web-security/ptes/templates.md](../../web-security/ptes/templates.md)，
   为你自己的实验环境写一份包含目标 IP、允许的测试动作、时间窗、联系人的授权记录。
