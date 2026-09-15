# 11 · 社会工程与报告（Social Engineering & Reporting）

> 本目录是 Kali 工具精讲教程的第 11 篇：**面向「人」的攻击面**，以及**把测试结果变成可交付物**。
> 两条线：
> - **社工线**：诱饵设计 → 投递 → 度量（[`set.md`](set.md)、[`gophish.md`](gophish.md)）
> - **报告线**：过程记录 → 汇总协作 → 按模板交付（[`cherrytree.md`](cherrytree.md)、[`dradis.md`](dradis.md)）
> 上游：[`../08-后渗透/`](../08-后渗透/)、[`../09-数字取证/`](../09-数字取证/)、[`../10-逆向工程/`](../10-逆向工程/)
> 相关索引：[`../../index.md`](../../index.md) ｜ 分类速查：[`../../catalog/reporting.md`](../../catalog/reporting.md)

---

## 工具清单

| 工具 | 一句话 | 难度 | 教程 |
|------|--------|------|------|
| **set** | Social-Engineer Toolkit：交互式社工工具箱（克隆站点收凭据、邮件钓鱼、介质攻击…） | ⭐⭐⭐ | [`set.md`](set.md) |
| **gophish** | 钓鱼演练平台：模板/名单/时间线/**事件级度量**/报表/API | ⭐⭐ | [`gophish.md`](gophish.md) |
| **cherrytree** | 层级笔记：树形结构记录过程与草稿，导出 HTML/PDF/Markdown | ⭐ | [`cherrytree.md`](cherrytree.md) |
| **dradis** | 协作式报告平台：**导入扫描器输出** + Issue 库 + Evidence + 模板出报告 | ⭐⭐⭐ | [`dradis.md`](dradis.md) |

> **选型速查**：
> - 想要**一次性演示社工手法** → SET
> - 想做**可度量、可合规的企业演练** → **Gophish**
> - **一个人**记过程 → **CherryTree**
> - **团队**协作 + 正式报告 → **Dradis**

> **关于工具替换说明**：任务清单里提到的 `mailsniper`、`faraday` **不在本仓库抓取的 Kali 官方工具清单中**，因此未收录。报告线由确实存在于清单的 `cherrytree` 与 `dradis` 承担；钓鱼线由 `set` 与 `gophish`（两者都在清单中）承担。

---

## 学习顺序

```
【社工线】
① 先看清「法律与授权」：set.md 文末 + gophish.md 文末（**必读，先读**）
② 在自建靶站上验证手法：set.md 场景 1–2（克隆 + 收凭据）
③ 把手法做成可度量演练：gophish.md 场景 1（SMTP → 页面 → 模板 → Campaign）
④ 企业流程与指标：gophish.md 场景 2（授权→设计→预演→执行→澄清→复盘→清理）
⑤ 蓝队视角：gophish.md 第 9 节（MFA / DMARC / 上报率）

【报告线】
① 建立记录习惯：cherrytree.md 场景 1（树形结构 + 授权要点置顶）
② 用模板写漏洞条目：cherrytree.md 场景 2（标题→等级→资产→描述→复现→证据→影响→修复→参考）
③ 脱敏/加密/导出：cherrytree.md 场景 3
④ 团队协作 + 正式报告：dradis.md 场景 1–3（导入 Nmap → Issue/Evidence → 模板导出）
```

**PDCA 循环（把两条线连起来）**：

```
演练      Gophish / SET  →  度量指标（点击率/提交率/上报率）
   ▲                                  │
   │                                  ▼
改进  ◄──  报告（CherryTree 草稿 → Dradis 交付）  ◄──  防护加固（MFA/DMARC/培训）
```

---

## 环境准备

```bash
sudo apt update
sudo apt install -y set gophish cherrytree dradis

# 社工线依赖（SET 用 Apache/PHP 托管页面；msf 生成载荷）
sudo apt install -y apache2 libapache2-mod-php metasploit-framework

# 报告线依赖（Dradis 是 Rails 应用，依赖较多但 apt 会拉齐）
command -v setoolkit gophish-start cherrytree dradis-start
```

验证：

```bash
# SET
sudo systemctl start apache2 && sudo ss -lntp | grep ':80 '
sudo setoolkit    # 首次需同意 ToS（输入 y），看到主菜单即正常（Ctrl+C 退出）

# Gophish
sudo gophish-start
curl -sk -o /dev/null -w 'gophish admin: %{http_code}\n' https://127.0.0.1:3333
sudo gophish-stop

# CherryTree（需要有图形环境）
cherrytree --version

# Dradis
sudo dradis-start
sleep 20 && curl -s -o /dev/null -w 'dradis: %{http_code}\n' http://127.0.0.1:3000
sudo dradis-stop
```

### 环境准备清单（自检）

| 检查项 | 命令/动作 | 期望 |
|--------|-----------|------|
| 80/443 端口空闲 | `sudo ss -lntp \| grep -E ':80 \|:443 '` | 无占用（或你知道谁占用） |
| 本机可达 IP 明确 | `ip -4 addr \| grep inet` | 记录下**目标可达的那个 IP** |
| Apache 可用 | `sudo systemctl status apache2 --no-pager` | active |
| msf 可用 | `command -v msfvenom msfconsole` | 有输出 |
| Gophish 管理口可访问 | `curl -sk https://127.0.0.1:3333` | 返回页面（证书告警属正常） |
| CherryTree 有图形环境 | `echo $DISPLAY` | 非空（或本机 GUI 使用） |
| Dradis 起来了 | `curl -s http://127.0.0.1:3000` | 返回页面 |
| **有自建靶站/靶机** | 自建登录页或 DVWA（Docker） | 可访问 |

### 练习素材（**必须合法**）

| 素材 | 获取方式 | 适合练什么 |
|------|----------|------------|
| **自建登录页** | 自己写一个 HTML 表单（见 [`set.md`](set.md) 场景 1、[`gophish.md`](gophish.md) 场景 1） | 站点克隆、Landing Page、凭据收集 |
| **自建 SMTP** | MailHog/Mailpit（Docker）、或自建 postfix | 演练邮件投递与统计 |
| **自有/演练域名** | 自己注册的域名（如 `drill.example.com`） | SPF/DKIM/DMARC、真实证书 |
| **自建靶站** | DVWA / Juice Shop（Docker） | 社工 + Web 场景串联 |
| **自建靶机** | 自建 Windows/Linux 虚拟机（Host-Only） | 记录与报告演练 |

---

## ⚠️ 法律与伦理（**本目录的红线，比任何工具用法都重要**）

社工攻击直接针对**人**，法律风险在所有 Kali 工具里最高。

**可能触犯的法律**：

- 《刑法》**第 285 条**：非法侵入计算机信息系统罪、非法获取计算机信息系统数据罪、**非法控制计算机信息系统罪**；
- 《刑法》**第 253 条之一**：**侵犯公民个人信息罪**（账号口令、员工邮箱、行为数据均属个人信息）；
- 《刑法》**第 252 条**：侵犯通信自由罪（收发/阅读他人邮件）；
- 《网络安全法》第 27 条、《数据安全法》、《个人信息保护法》。

**社工演练的四条硬性前提（缺一不可）**：

1. **管理层书面批准 + 制度依据**：员工手册/信息安全政策中必须明确"组织可能开展安全意识演练"；
2. **明确范围与时间窗**：演练名单、时间、目标要有书面记录；
3. **只针对已批准的名单**；**建议关闭"记录口令"选项**（只统计提交行为）；
4. **演练后立即澄清 + 清理数据 + 报告脱敏**。

**报告线的要求**：

1. 只记录**有授权**的内容；把**授权范围与时间窗写在记录顶部**；
2. **记录时就脱敏**（口令/hash/姓名/无关个人数据）；
3. 笔记与项目数据**加密存储**、限时保存、到期销毁；
4. Dradis 等平台**只在内网部署**，独立账号，绝不暴露公网。

> **一句话**：社工与报告的每一个环节，都要能回答一个问题——**「如果客户/监管/法庭问我凭什么这么做，我拿得出什么？」** 拿不出，就不要做。
