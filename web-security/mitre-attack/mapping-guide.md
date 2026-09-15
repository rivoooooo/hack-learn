# ATT&CK 映射指南：从测试发现到技术编号

本页解决一个具体问题：**你手上有一堆渗透测试发现（finding），怎么把它们正确地贴上 ATT&CK 技术编号？**

- 阅读前置：[README.md](./README.md)（战术/技术/子技术的概念与 15 个企业战术）
- 抓取依据：<https://attack.mitre.org/>（2026-09-15）

---

## 1. 先想清楚：映射是给谁看的

映射目的不同，"贴到什么粒度"就不同。先定目的，再动手：

| 目的 | 建议粒度 | 说明 |
| --- | --- | --- |
| 检测工程排期 | 子技术（`Txxxx.xxx`） | 越细越好，否则没法写规则 |
| 红队报告 | 技术（`Txxxx`）为主 | 报告读者关心"你干了什么"，不关心实现细节 |
| 管理层热力图 | 技术（`Txxxx`） | 子技术会让图过密，反而看不出趋势 |
| 威胁情报比对 | 子技术 + G/S 编号 | 要和具体组织/工具对齐 |

一个硬性规则：**同一份交付物里的粒度必须统一**。混着用会让热力图分数失去可比性。

---

## 2. 映射的四个步骤

1. **用自然语言描述行为，先不看 ATT&CK。**
   写成"攻击者在 X 主机上，以 Y 权限，通过 Z 方式，达成了 W 结果"。不要一边查表一边描述，否则描述会被你已知的编号带偏。
2. **定位战术。**问自己：这一步攻击者的**目的**是什么？对照 [README 里的 15 战术表](./README.md#3-企业域-15-个战术tactics全表) 选，通常一步只落一个主战术（少数跨两列）。
3. **在该战术列下找技术。**进入 <https://attack.mitre.org/tactics/TAxxxx/> 或矩阵页，只在该战术列内找，避免跨列乱选。
4. **能下降到子技术就下降。**读子技术定义，如果行为与某个子技术定义吻合就写 `Txxxx.xxx`；多个子技术都部分吻合 → 说明你还没描述清楚，回到第 1 步。

**关键纪律：定义优先于名称。**必须读技术页的正文描述，确认它覆盖的行为与你的发现一致。名字像不代表定义像（见第 4 节的错误案例）。

---

## 3. 三个完整映射示例

### 示例一：钓鱼附件投放宏文档，用户启用宏后上马

**原始发现（第 1 步描述）**

> 2026-08-12 上午，财务部 3 名员工收到伪装成"发票"的 xlsx 附件。员工打开后按提示点击"启用内容"，文件内嵌宏随后执行 PowerShell，从 `hxxp://cdn-static[.]example/upd.ps1` 下载并运行了一个 C2 回连程序。邮件网关未拦截。

**第 2 步：拆成独立行为**

一次攻击链往往对应多个技术，必须**拆开映射**，不要硬塞成一个编号：

| 行为片段 | 战术（目的） | 技术 / 子技术 | 推理过程 |
| --- | --- | --- | --- |
| 发带恶意附件的钓鱼邮件 | 初始访问 TA0001 | **T1566.001** Spearphishing Attachment | 技术 T1566 Phishing 下挂了 4 个子技术，行为是"邮件带**附件**"，对照 T1566.001 名为 Spearphishing Attachment，命中。若发的是纯链接则应选 T1566.002 |
| 用户打开并启用宏 → 代码运行 | 执行 TA0002 | **T1204.002** User Execution: Malicious File | 这里"执行"的触发者是**用户本人**，属于 User Execution 类；因为是文件，落子技术 Malicious File。注意：如果宏是自动执行（无用户交互），则更适合映射到 T1204 之外的路径，需重新描述 |
| 宏调用 PowerShell | 执行 TA0002 | **T1059.001** Command and Scripting Interpreter: PowerShell | 攻击者通过解释器执行命令。平台落在 Windows，子技术选 PowerShell 而非 Shell / Python |
| 从 HTTP 地址下载后续载荷 | 命令与控制 TA0011 | **T1105** Ingress Tool Transfer | 定义是"从外部系统把工具或文件传入受害环境"。注意它属于 C2 战术而非 Execution，因为其目的是**取得工具**以维持后续通信与操作 |
| 程序回连 C2 服务器 | 命令与控制 TA0011 | **T1071.001** Application Layer Protocol: Web Protocols | 回连走 HTTP/HTTPS，属应用层协议；具体子技术是 Web Protocols。若走的是 DNS 隧道则选 T1071.004 |

**产出（写进报告的形式）**

```
F-001 钓鱼附件投放宏文档
ATT&CK: T1566.001 (Initial Access) → T1204.002 (Execution)
        → T1059.001 (Execution) → T1105 (Command and Control)
        → T1071.001 (Command and Control)
```

**推理要点**：一条链路映射出 5 个编号是正常的，不是过度细分。报告里建议按**时间顺序**列出，让读者能还原攻击链。

---

### 示例二：Web 应用 SQL 注入，成功读取数据库并落 webshell

**原始发现（第 1 步描述）**

> `/api/report?id=1` 参数存在报错型 SQL 注入。使用 sqlmap 成功枚举出 12 张表并导出 `users` 表 3.2 万条记录。随后通过 `--os-shell` 在 Web 服务器上以 `www-data` 权限执行命令，写入一句话木马并连接成功，进一步发现该主机可通过 SSH 密钥横向登录内网 4 台应用服务器。

**第 2 步：拆解映射**

| 行为片段 | 战术 | 技术 / 子技术 | 推理过程 |
| --- | --- | --- | --- |
| 探测到 SQL 注入并利用 | 初始访问 TA0001 | **T1190** Exploit Public-Facing Application | 定义是"利用面向公网的应用程序中的弱点获得访问"。SQLi 属于"利用应用弱点"，落 T1190。**不要**因为"注入了"就选 T1059 系列，那是执行段的事 |
| 导出 users 表数据 | 收集 TA0009 / 凭据访问 TA0006 | **T1213** Data from Information Repositories（数据层面）/ 若导出的含口令哈希则加 **T1555** 或 **T1110** 相关 | 导出业务数据 → 收集；导出的是**凭据** → 凭据访问。本例同时命中两者，应写两条 |
| 通过 `--os-shell` 执行系统命令 | 执行 TA0002 | **T1059.004** Command and Scripting Interpreter: Unix Shell | sqlmap 的 os-shell 最终在目标上起的是 Unix shell，命中 T1059.004 |
| 写入一句话木马并连接 | 持久化 TA0003 | **T1505.003** Server Software Component: Web Shell | Web Shell 是 T1505 的子技术，定义完全吻合。**不要**选 T1059，因为持久化才是这一步的目的 |
| 用窃取的 SSH 密钥登录其他主机 | 横向移动 TA0008 | **T1021.004** Remote Services: SSH | 走 SSH 远程服务，子技术为 SSH。若用的是 RDP 则 T1021.001，WinRM 则 T1021.006 |
| 使用窃取的 SSH 私钥 | 凭据访问 TA0006 | **T1552.004** Unsecured Credentials: Private Keys | 注意这里有两个动作：**拿到私钥**（凭据访问 T1552.004）和**用私钥登录**（横向移动 T1021.004）。两者都要写 |

**产出**

```
F-002 公网 API SQL 注入导致数据库泄露与服务器沦陷
T1190  (Initial Access)
T1213  (Collection)          ← 导出业务数据
T1552.004 (Credential Access) ← 取得 SSH 私钥
T1059.004 (Execution)
T1505.003 (Persistence)
T1021.004 (Lateral Movement)
```

**推理要点（本例最容易错的地方）**

- **一个动作可以命中两个战术**：取得私钥既是"凭据访问"也是"横向移动"的前置，别只写一个。
- **手段 ≠ 目的**：`--os-shell` 是手段，目的是"写 Web Shell 维持访问"，所以持久化那条要落在 T1505.003。
- **别把漏洞类型当技术**："SQL 注入"不是一个 ATT&CK 技术；ATT&CK 关心的是**利用公网应用**（T1190）这个行为。SQL 注入的**弱点归类**属于 [CWE-89](../cwe/README.md)，具体的漏洞实例编号属于 CVE，可用 EXP 在 [Exploit-DB](../exploit-db/README.md) 找——三套体系各管一段，不要混。

---

### 示例三：内网已立足后的凭据转储 + 计划任务持久化 + 定时外泄

**原始发现（第 1 步描述）**

> 在已控主机（`WIN-APP-07`，本地管理员）上执行 `procdump` 对 `lsass.exe` 转储内存，用 mimikatz 从转储中取出 2 个域账号的 NTLM 哈希。使用其中一个账号哈希通过 `psexec` 登录域控 `DC01`。为保持访问，在 `WIN-APP-07` 上创建了一个每 15 分钟执行一次的计划任务，任务调用 powershell 从 `\\fileserver\share` 取回加密压缩包并 POST 到 `hxxps://api.example-sync[.]com/v1/upload`。

**第 2 步：拆解映射**

| 行为片段 | 战术 | 技术 / 子技术 | 推理过程 |
| --- | --- | --- | --- |
| 对 lsass 转储内存 | 凭据访问 TA0006 | **T1003.001** OS Credential Dumping: LSASS Memory | T1003 有多个子技术（SAM、LSASS Memory、NTDS、DCSync 等）。行为明确是转 LSASS，选 .001 |
| 从转储中提取哈希 | 凭据访问 TA0006 | **T1003.001**（同一条） | 提取是 LSASS 转储这条技术的一部分，不再单列 |
| 用 NTLM 哈希登录 | 横向移动 TA0008 | **T1550.002** Use Alternate Authentication Material: Pass the Hash | "Pass the Hash" 在 ATT&CK 里归在**横向移动**战术下（T1550 的子技术），不在凭据访问下。这是常见误判点 |
| 借道 psexec 远程执行 | 横向移动 TA0008 | **T1021.002** Remote Services: SMB/Windows Admin Shares | psexec 走 SMB 与管理共享，命中 T1021.002 |
| 创建计划任务 | 持久化 TA0003 | **T1053.005** Scheduled Task | T1053 的子技术按平台/机制分，Windows 计划任务为 .005 |
| 定时从共享取文件 | 收集 TA0009 | **T1039** Data from Network Shared Drive | 从网络共享取数据，符合 T1039 定义 |
| 通过 HTTPS POST 外发 | 外泄 TA0010 | **T1041** Exfiltration Over C2 Channel | 复用已有 C2 通道外泄 → T1041。若走的是独立于 C2 的通道（如仅 HTTPS 直传、与 C2 无关），则应考虑 T1048 系列 |
| 数据打包压缩 | 外泄 TA0010 | **T1560.001** Archive Collected Data: Archive via Utility | 用工具打包压缩，属 T1560 的子技术；如用自定义脚本打包则可能落 T1560.003 |

**产出**

```
F-003 内网凭据转储与持久化外泄
T1003.001 (Credential Access)
T1550.002 (Lateral Movement)
T1021.002 (Lateral Movement)
T1053.005 (Persistence)
T1039     (Collection)
T1560.001 (Collection)     ← 打包压缩，ATT&CK 把它归在 Collection 战术下
T1041     (Exfiltration)
```

**推理要点**

- **T1560 归在"收集"而不是"外泄"**——这是个很容易搞反的位置。判断依据是它回答的是"把数据聚到一起"，不是"把数据送出去"。
- **T1550 归在"横向移动"**而不是"凭据访问"，同理要看战术列归属。
- 每写一个编号，**回到技术页确认它列在哪个战术下**，不要凭印象。

---

## 4. 常见映射错误

### 错误 1：按名字字面匹配

"攻击者用了 PowerShell" → 直接选 T1059.001。但如果 PowerShell 只是被用来做**发现**（如 `Get-ADUser`），那更贴切的是 Discovery 战术下的技术，PowerShell 只是载体。

**纠正**：先定目的（战术），再在战术列内选技术。载体（解释器、语言）只是实现细节。

### 错误 2：把漏洞类型当成 ATT&CK 技术

| 你手上的东西 | 正确归属 | 不归属 |
| --- | --- | --- |
| SQL 注入 | CWE-89（弱点类型）；利用公网应用行为 → ATT&CK T1190 | 不存在名为"SQL Injection"的 ATT&CK 技术 |
| 反序列化 | CWE-502（弱点类型） | 同上 |
| SSRF | CWE-918（弱点类型）；利用行为 → T1190 | 同上 |
| CVE-2021-44228 | CVE 编号 + [Exploit-DB EDB-50592](../exploit-db/README.md) | ATT&CK 不收录 CVE |

**纠正**：ATT&CK 描述**行为**，CWE 描述**弱点**，CVE 描述**实例**。三者是三层，不是同层替代品。

### 错误 3：一步行为硬贴一个编号，丢掉整条链路

把"从钓鱼到外泄"整条链写成 `T1566`。这会毁掉热力图的价值——蓝队看 T1566 会以为只需要加邮件网关规则。

**纠正**：**按行为片段拆开映射**，一段一个编号。

### 错误 4：粒度不一致

同一个报告里有的写 `T1059`、有的写 `T1059.001`。热力图按子技术求和时，父技术的分数会和子技术重复计入。

**纠正**：先定粒度（见第 1 节），全程统一。用 Navigator 时，若必须降到子技术，请用 Aggregate Scores 的 max/sum 规则并明确注明。

### 错误 5：忽略版本差异，尤其是 Defense Evasion

历史资料里 `TA0005` 叫 Defense Evasion。2026-09-15 抓取的官网已把 `TA0005` 改名为 **Stealth（隐蔽）**，并新增 `TA0112 Defense Impairment（防御削弱）`，企业域战术数从 14 变 15。

**纠正**：
- 层文件里用 `versions.attack` 明确声明版本；
- 引用老资料时确认对方用的是哪个版本；
- "关掉杀软/篡改日志/破坏 EDR"这类行为，在新版下要判断是"让行为不被看见"（Stealth）还是"让防守方的机制失效"（Defense Impairment）。

### 错误 6：把"我能做"当成"对手会做"

红队做映射时常只映射自己实现得了的技术，导致覆盖度图反映的是红队能力，不是威胁态势。

**纠正**：先选对手（Threat Group，`Gxxxx`），用 Navigator 的 Search & Multiselect 一次性选中该组织的全部技术，以此为基线。

### 错误 7：只映射技术，不映射平台

T1566 的平台是 `Identity Provider, Linux, Office Suite, SaaS, Windows, macOS`。如果你的环境全是 Linux 且没有办公套件，映射后要说明该技术在本地不适用，否则热力图会出现"覆盖不到但其实不适用"的假缺口。

**纠正**：用 Navigator 的 Platform Filter 过滤出与自身环境相关的技术子集再打分。

---

## 5. 映射质量自查清单

完成一份映射后，逐条过：

- [ ] 每条发现都写了"自然语言行为描述"，且描述里包含**主体、权限、手段、结果**
- [ ] 每条发现拆成了多个行为片段，而不是一整条贴一个编号
- [ ] 每个编号都打开过技术页，确认**定义**吻合（不只是名字像）
- [ ] 每个编号都确认过它**列在哪个战术下**（尤其 T1550、T1560 这类位置反直觉的）
- [ ] 粒度统一（全技术 / 全子技术）
- [ ] 平台与自身环境匹配，不适用的已注明
- [ ] 声明了所依据的 ATT&CK 版本号
- [ ] ATT&CK 编号没有用来替代 CWE / CVE / EXP 编号
- [ ] 一份层文件已导出，能在 Navigator 里复现

---

## 6. 来源 URL

- ATT&CK 官网首页：<https://attack.mitre.org/>
- 企业战术列表（15 个，含 TA0005 Stealth 与 TA0112 Defense Impairment）：<https://attack.mitre.org/tactics/enterprise/>
- 企业矩阵：<https://attack.mitre.org/matrices/enterprise/>
- 技术页示例（编号规则、子技术、平台、Procedure Examples）：<https://attack.mitre.org/techniques/T1566/>
- 入门指南（核心概念与"不该这么用"）：<https://attack.mitre.org/resources/getting-started/>
- 版本历史：<https://attack.mitre.org/resources/versions/>

> 本页引用的技术编号对应的**定义正文**请以 <https://attack.mitre.org/techniques/Txxxx/> 为准。上文未逐条抓取 T1003 / T1059 / T1105 / T1190 / T1204 / T1213 / T1505 / T1550 / T1552 / T1021 / T1053 / T1039 / T1041 / T1560 / T1071 的技术页正文；编号与名称取自 ATT&CK 官网通用编号体系，**动手前请逐个打开技术页核对当前名称与子技术编号**（编号本身稳定，子技术可能有增补）。
