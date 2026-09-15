# MITRE ATT&CK 入门：用对手行为语言描述攻防

> 本页所有战术 ID、技术 ID、版本号均抓取自 <https://attack.mitre.org/>（抓取日期：2026-09-15）。
> 版本与编号会随官方更新变化，动手前请先到官网核对。

---

## 1. ATT&CK 是什么

MITRE ATT&CK（Adversarial Tactics, Techniques, and Common Knowledge，对抗战术、技术与常识库）是 MITRE 公司维护的**对手行为知识库**。它不描述漏洞，也不描述某款恶意软件的哈希值，而是把真实世界中观察到的**攻击者行为**按"目的 → 手段 → 具体实现"三层结构化。

ATT&CK 官方给出的四个核心概念（来源：<https://attack.mitre.org/resources/getting-started/>）：

| 概念 | 英文 | 回答的问题 | 例子 |
| --- | --- | --- | --- |
| 战术 | Tactic | 攻击者**为什么**做这件事 | 初始访问（Initial Access） |
| 技术 | Technique | 攻击者**怎么做**到这件事 | 网络钓鱼（Phishing，T1566） |
| 子技术 | Sub-technique | 这件事更**具体**的做法 | 钓鱼附件（Spearphishing Attachment，T1566.001） |
| 过程 | Procedure | 攻击者**具体某次**怎么用的 | APT29 用某模板发带宏的 Word 附件 |

一句话记忆：**战术是"为什么"，技术是"怎么做"，过程是"谁在什么时候怎么做的实例"。**

### ATT&CK 不负责什么

- 不负责给漏洞编号 → 那是 [CVE](https://www.cve.org/) 和 [CWE](../cwe/README.md) 的事。
- 不负责定义测试流程 → 那是 [PTES](../ptes/README.md) 的事。
- 不负责提供可用 EXP → 那是 [Exploit-DB](../exploit-db/README.md) 的事。
- 不负责给出控制项清单 → 那是 [NIST SP 800-53](../nist/README.md) 的事。

---

## 2. 三个技术域（Technology Domains）

ATT&CK 按"对手在什么生态里活动"分成三套独立的知识库，各有自己的矩阵（Matrix）：

| 域 | 英文 | 覆盖对象 | 当前战术数 | 矩阵地址 |
| --- | --- | --- | --- | --- |
| 企业 | Enterprise | 传统企业网络、云、容器、SaaS、身份系统 | **15** | <https://attack.mitre.org/matrices/enterprise/> |
| 移动 | Mobile | Android / iOS 移动终端 | **12** | <https://attack.mitre.org/matrices/mobile/> |
| 工控 | ICS | 工业控制系统（SCADA / PLC / 工程工作站） | **12** | <https://attack.mitre.org/matrices/ics/> |

要点：

- 三套矩阵**编号不互通**。同一个"初始访问"，Enterprise 是 `TA0001`，Mobile 是 `TA0027`，ICS 是 `TA0108`。写报告时必须标明域，否则 `TA0108` 在企业语境里是无意义编号。
- 每个域内部还有"平台（Platform）"维度。例如 T1566 的平台包含 Identity Provider、Linux、Office Suite、SaaS、Windows、macOS。
- 技术/子技术可以跨平台、跨战术复用。同一个技术出现在多个战术列里，是正常现象，不是数据错误。

---

## 3. 企业域 15 个战术（Tactics）全表

来源：<https://attack.mitre.org/tactics/enterprise/>（Enterprise Tactics: 15）

| # | 战术 ID | 英文名 | 中文名 | 攻击者目标 |
| --- | --- | --- | --- | --- |
| 1 | TA0043 | Reconnaissance | 侦察 | 收集可用于规划后续行动的信息 |
| 2 | TA0042 | Resource Development | 资源开发 | 建立可支撑行动的各类资源（账号、基础设施、工具） |
| 3 | TA0001 | Initial Access | 初始访问 | 进入你的网络 |
| 4 | TA0002 | Execution | 执行 | 运行恶意代码 |
| 5 | TA0003 | Persistence | 持久化 | 维持已获得的立足点 |
| 6 | TA0004 | Privilege Escalation | 权限提升 | 获取更高层级的权限 |
| 7 | TA0005 | Stealth | 隐蔽 | 隐藏和掩盖自身行为，让行为看起来像正常活动 |
| 8 | TA0112 | Defense Impairment | 防御削弱 | 破坏安全机制、检测流水线与工具，使防守方看不到或无法信任正在发生的事 |
| 9 | TA0006 | Credential Access | 凭据访问 | 窃取账号名与口令 |
| 10 | TA0007 | Discovery | 发现 | 摸清你的环境 |
| 11 | TA0008 | Lateral Movement | 横向移动 | 在环境中横向穿行 |
| 12 | TA0009 | Collection | 收集 | 汇聚对其目标有价值的数据 |
| 13 | TA0011 | Command and Control | 命令与控制 | 与被控系统通信以控制它们 |
| 14 | TA0010 | Exfiltration | 外泄 | 窃取数据 |
| 15 | TA0040 | Impact | 影响 | 操纵、中断或破坏系统与数据 |

> ⚠️ **版本易变点（务必注意）**：历史上企业域长期是 **14** 个战术，其中包含 `TA0005 Defense Evasion`（防御规避）。在 2026-09-15 抓取时官网已改为：
> - `TA0005` 的名称变为 **Stealth（隐蔽）**；
> - 新增 **`TA0112 Defense Impairment`（防御削弱）**，把"破坏安全机制本身"从"规避检测"里拆分出来，因此战术总数变为 **15**。
>
> 很多老教程、老工具默认仍是 14 个战术 + Defense Evasion。做映射或写热力图时先统一版本，否则会出现"同一份层文件在不同版本下错位"。

---

## 4. 移动域 12 个战术

来源：<https://attack.mitre.org/tactics/mobile/>（Mobile Tactics: 12）

| 战术 ID | 英文名 | 中文名 |
| --- | --- | --- |
| TA0027 | Initial Access | 初始访问 |
| TA0041 | Execution | 执行 |
| TA0028 | Persistence | 持久化 |
| TA0029 | Privilege Escalation | 权限提升 |
| TA0030 | Defense Evasion | 防御规避 |
| TA0031 | Credential Access | 凭据访问 |
| TA0032 | Discovery | 发现 |
| TA0033 | Lateral Movement | 横向移动 |
| TA0035 | Collection | 收集 |
| TA0037 | Command and Control | 命令与控制 |
| TA0036 | Exfiltration | 外泄 |
| TA0034 | Impact | 影响 |

注意：移动域**没有** Reconnaissance、Resource Development、Defense Impairment，且仍保留 `Defense Evasion` 这一名称。三域命名并不完全对齐，跨域引用时不要假设名称一致。

## 5. 工控域 12 个战术

来源：<https://attack.mitre.org/tactics/ics/>（ICS Tactics: 12）

| 战术 ID | 英文名 | 中文名 |
| --- | --- | --- |
| TA0108 | Initial Access | 初始访问 |
| TA0104 | Execution | 执行 |
| TA0110 | Persistence | 持久化 |
| TA0111 | Privilege Escalation | 权限提升 |
| TA0103 | Evasion | 规避 |
| TA0102 | Discovery | 发现 |
| TA0109 | Lateral Movement | 横向移动 |
| TA0100 | Collection | 收集 |
| TA0101 | Command and Control | 命令与控制 |
| TA0107 | Inhibit Response Function | 抑制响应功能 |
| TA0106 | Impair Process Control | 破坏过程控制 |
| TA0105 | Impact | 影响 |

工控域独有的 `Inhibit Response Function` 与 `Impair Process Control` 两个战术，是 IT 域没有的——它们对应"让安全仪表系统 / 联锁失效"这类物理后果，是做 OT 安全评估时的重点。

---

## 6. 技术编号规则 `Txxxx` 与 `Txxxx.xxx`

- **技术**：`T` + 四位数字，例如 `T1566`（Phishing / 网络钓鱼）。
- **子技术**：父技术编号 + `.` + 三位数字，例如 `T1566.001`。
- 编号**一旦分配即永久稳定**，改名不改号。因此编号可以安全地写进报告、告警规则和数据库主键。
- 已废弃的技术编号会标记为 deprecated 并保留，不会回收给新内容。

以 T1566 为例（来源：<https://attack.mitre.org/techniques/T1566/>）：

```
T1566            网络钓鱼（Phishing）
├── T1566.001    Spearphishing Attachment（钓鱼附件）
├── T1566.002    Spearphishing Link（钓鱼链接）
├── T1566.003    Spearphishing via Service（通过第三方服务钓鱼）
└── T1566.004    Spearphishing Voice（语音钓鱼 / vishing）
```

该技术页在抓取时显示：ID `T1566`、Tactic `Initial Access`、Platforms `Identity Provider, Linux, Office Suite, SaaS, Windows, macOS`、Version `2.7`、Created `02 March 2020`、Last Modified `12 May 2026`。技术页的 "Procedure Examples" 段会列出哪些攻击组织（G 编号）或恶意软件（S 编号）用过它，这是做威胁建模时最直接的证据来源。

另外两个编号族：

- **G 编号**：攻击组织（Groups），如 `G0094 Kimsuky`、`G0069 MuddyWater`。
- **S 编号**：软件（Software），包括恶意软件与攻击者工具，如 `S1073 Royal`。

### ATT&CK 版本

抓取时当前版本为 **ATT&CK v19.2（2026-04-28 起为 current）**，来源 <https://attack.mitre.org/resources/versions/>。版本号采用 `major.minor`：major 版本随正式发布递增（含新内容），minor 版本用于拼写与数据修正。

近几个版本：

| 版本 | 生效区间 |
| --- | --- |
| v19.2 | 2026-04-28 起（current） |
| v18.1 | 2025-10-28 ～ 2026-04-27 |
| v17.1 | 2025-04-22 ～ 2025-10-27 |
| v16.1 | 2024-10-31 ～ 2025-04-21 |
| v15.1 | 2024-04-23 ～ 2024-10-30 |

Navigator 支持 ATT&CK v4 及以后的版本，更早的数据模型已不兼容。

---

## 7. 用 ATT&CK Navigator 做覆盖度热力图

ATT&CK Navigator（<https://mitre-attack.github.io/attack-navigator/>）是一个纯客户端 Web 应用，用来给矩阵单元格上色、打分、加注释，核心概念是**层（Layer）**——一份对 ATT&CK 知识库的自定义视图，可导出成 JSON 文件互相传递。

> 隐私提示：GitHub Pages 上的官方实例不会上传层文件（纯客户端），但如果层文件含敏感内容，官方建议自行本地部署实例。

### 完整操作步骤

**第 1 步：创建层**

1. 打开 <https://mitre-attack.github.io/attack-navigator/>。
2. 点 "**Create New Layer**" 下拉。
   - 快速按钮使用当前 ATT&CK 版本；
   - 选 "**More Options**" 可指定历史版本，或指定自定义 collection / STIX bundle 的 URL（该 bundle 必须含 Matrix 对象才能显示）。
3. 同时最多可打开 **10 个**活动层。

**第 2 步：只留下你关心的技术（过滤）**

- 用 **Platform Filter**（漏斗图标）反选平台。例如取消勾选 Windows 和 macOS，只看 Linux 相关技术。
- 过滤器之间是**逻辑或**叠加。
- 配合 "**hide disabled techniques**"（眼睛划掉图标），可把不关心的技术整块从视图中去掉。

**第 3 步：批量选中技术**

- 鼠标左键单击选中；`Ctrl` / `Command` / `Shift` + 左键加入或移出当前选择。
- 右键技术单元格会弹出上下文菜单，含：`select`、`add to selection`、`remove from selection`、`invert selection`、`select all`、`deselect all`、`select annotated`、`select unannotated`、`select all techniques in tactic`、`deselect all techniques in tactic`。
- 点战术表头可直接全选该列（受"selection behavior"设置影响）。
- 两个行为开关先设好再动手：
  - "**Select techniques across tactics**"：多战术技术是"全选"还是"只选当前列"。
  - "**Select sub-techniques with parent**"：选父技术时是否连带子技术。
- 批量勾选推荐用 "**Search & Multiselect Interface**"（放大镜图标）：
  - 文本搜索可限定搜索字段（name / ATT&CK ID / description / data sources）；
  - 列表分四类：**Techniques / Threat Groups / Software / Mitigations**；
  - 选中一个 Threat Group 会一次性选中该组织用过的**全部技术**——这是做"某 APT 的 TTP 覆盖度"最快的方法；
  - 选中一个 Mitigation 会一次性选中它所能缓解的全部技术；
  - "**select all**" / "**deselect all**" 作用于当前搜索结果。

**第 4 步：打分（热力图的数值来源）**

1. 先选中一个或多个技术（技术类控件只在有选中项时可用）。
2. 点 "**Scoring Techniques**"（柱状图图标）填入数值。多选会一起赋同一分数。
3. 默认状态是 "**unscored**"。记住：**unscored ≠ 0 分**，未打分的单元格不会被渐变上色，会保持无底色。

**第 5 步：配置渐变，把分数变成颜色**

1. 点 "**Color Setup**"（调色板图标）。
2. 在 "**Scoring Gradient**" 中设置 "low value" 与 "high value"，分数在这两点之间**线性映射**到颜色。
   - 官方示例：红→绿渐变，low=0、high=50 时，分数 25 落在正中间（黄色）。
   - 超出上下限的分数会被**截断（clamp）**到端点色。
3. 常用两套配置：
   - **二值覆盖度**（会/不会）：low value = 0 设为**透明**，high value = 1 设为某个实色。这样只有"覆盖到的"技术显色。
   - **频次热力图**（告警数量）：low = 0、high = 该周期内最高告警数。
4. 同一菜单里可设 "**Tactic Row Background**"（战术行底色），需勾选 show 才显示，mini 布局下不显示。
5. 手动色（"**Assigning Manual Colors**"，油漆桶图标）会**覆盖**渐变派生色；要恢复渐变，在颜色面板顶部选 "**no color**"。

**第 6 步：加注释，让图能自解释**

- "**Adding Comments to Techniques**"（对话气泡图标）→ 悬停可见，单元格出现**黄色下划线**。
- "**Assigning Links to Techniques**"（链环图标）→ 标签 + URL（URL 必须带协议前缀如 `https://`），单元格出现**蓝色下划线**，右键菜单里可见。
- "**Adding Metadata to Techniques**"（元数据图标）→ 键值对，悬停可见。
- "**Clearing Annotations on Techniques**"（清除图标）→ 一次性清掉所选技术的注释、链接、元数据、颜色、分数与启停状态。

**第 7 步：导出与分发**

- **JSON**：点 "**save layer**"（下载图标）→
  - "**download single layer as json**"：导出当前层；
  - "**download all layers as json**"：导出全部打开的层。
  - 导出内容含：被自定义过的技术配置、渐变设置、过滤器、层名称、层描述、视图配置。
- **导入**：新标签页打开 "**Open Existing Layer**" 面板 → "**Upload from local**" 选择 JSON；或直接用 "**load from URL**"。
- **Excel**：菜单里有 "**export single layer to excel**" 与 "**export all layers to excel**"（每个层一个 sheet），会带上颜色、启停状态、战术行底色、排序、过滤与隐藏状态。
- **图片**：点 "**render layer to SVG**"（相机图标）→ 在弹出的窗口里点 "**download svg**"。
  - 窗口内可调："**toggle measurement unit**"（in / cm / px）、"**Configuring Image Size**"（宽、高、header 高度）、"**Configuring Text**"（serif / sans-serif / monospace）、"**Customizing the Legend**"（可 undock 后调 X/Y/宽/高）、"**Display Settings**"（show header / about / domain / filters / legend，sub-techniques 选 show all / expanded / none，cell border）。
  - 官方文档只提供 SVG 导出，**没有独立的 PNG 按钮**；要 PNG 需自行转换，或走打印 / 存 PDF 路径。
  - 用 Edge 下载时文件可能带 `.txt` 后缀，改名为 `.svg` 即可。

**第 8 步：出图前的小技巧**

- 浏览器打印前先**关掉粘性工具栏**（图钉图标 "show/hide sticky toolbar"），否则矩阵会被截断。
- 排序有四种模式：字母升 / 字母降 / 数值升 / 数值降（数值排序时未打分按 0 处理）。
- 子技术折叠控制："**expand sub-techniques**"、"**expand annotated sub-techniques**"、"**collapse sub-techniques**"。
- 布局（Matrix Configuration 下拉）：**Side Layout** / **Flat Layout** / **Mini Layout**。Mini 布局去掉文字、只显方块，子技术收进带框的小格，"禁用"显示为 `x`，"有注释"显示为 `i`。
- "**show names**" 默认开，"**show IDs**" 默认关。出正式图时建议两个都开，方便对照。
- 聚合分数（Aggregate Scores）可把技术与子技术用 average / min / max / sum 合并，另有 "show/hide aggregate scores" 与 "count unscored techniques as 0"。

### 层文件（layer JSON）长什么样

Navigator 的层文件是纯 JSON，关键字段如下（结构参见仓库 `layers` 目录的格式规范）：

```json
{
  "name": "ACME 2026 Q3 检测覆盖度",
  "versions": { "attack": "19", "navigator": "5.1.0", "layer": "4.5" },
  "domain": "enterprise-attack",
  "description": "基于 EDR 与 DNS 日志的检测覆盖情况，2026-09-15",
  "gradient": {
    "colors": ["#ffffff", "#66ff00"],
    "minValue": 0,
    "maxValue": 1
  },
  "techniques": [
    { "techniqueID": "T1566.001", "score": 1, "comment": "邮件网关可拦，EDR 无遥测" },
    { "techniqueID": "T1059.001", "score": 0, "comment": "仅有进程创建日志，未建规则" }
  ]
}
```

要点：`domain` 决定这份层贴在哪个矩阵上；`techniqueID` 必须是合法编号；`score` 与 `gradient` 配合出颜色；`comment` 在图上表现为黄下划线。**手工生成层文件是可行的**，CI 里跑脚本自动产出层 JSON 再给人看图，是很常见的落地方式。

---

## 8. 红队、蓝队、Purple Team 三种用法

ATT&CK 官方列出的四类主要用法是：检测与分析（Detections and Analytics）、威胁情报（Threat Intelligence）、对手模拟与红队（Adversary Emulation and Red Teaming）、评估与工程（Assessment and Engineering）。下面按团队角色归并成三种落地方式。

### 红队 / 对手模拟

- **目标**：不是"拿到域管"，而是"按某个真实对手的 TTP 走一遍"，验证防守方能不能看见。
- **做法**：先在 Threat Groups 里选一个与自身行业匹配的组织（例如金融行业选 `G0069 MuddyWater`），用 Navigator 的 Search & Multiselect 一次性选中它用过的全部技术，导出成层文件，这就是**模拟范围基线**。然后逐条挑选可落地的技术去执行。
- **产物**：一份"计划执行的 TTP 清单"层文件 + 每次执行的时间戳与命令记录。
- **常见误区**：只挑自己会做的技术，导致模拟结果不反映真实威胁；正确做法是先定对手，再决定要补哪些能力。

### 蓝队 / 检测工程

- **目标**：回答"这个技术如果我被用了，我看得见吗？"
- **做法**：以技术为粒度建检测覆盖度层。每个技术打 0/1 或按告警量打频次分，配 `comment` 说明**数据源是什么、为什么覆盖不到**。数据源可对照技术页里的 "Data Sources" 与 Detection Strategies 段。
- **产物**：覆盖度热力图（给管理层）+ 缺口清单（给工程排期）。
- **常见误区**：把"日志里有这条记录"等同于"检测到"。有遥测不等于有规则，有规则不等于有人看。建议分三个分数维度或用 metadata 区分"遥测 / 规则 / 告警处置"。

### Purple Team / 评估与工程

- **目标**：把红队的执行结果和蓝队的覆盖度对齐，找出"以为自己能测到、实际测不到"的落差。
- **做法**（一次典型演练）：
  1. 选定对手 TTP 子集，红蓝双方各自出一份层文件（红 = 计划+已执行，蓝 = 自评覆盖度）。
  2. 在同一 Navigator 实例里同时打开两份层（最多 10 层），逐技术比对。
  3. 对每一处不一致（红队说打了，蓝队说没告警）现场排查：是数据没采、规则没写，还是规则写了没生效。
  4. 把结论写回第三份"改进后目标态"层文件，作为下一轮验收基线。
- **产物**：三份层文件 + 一份落差表。
- **常见误区**：追 100% 覆盖。官方明确说 **不要追求 100% 覆盖**，每个组织面对的唯一威胁不同，不是所有战术技术都适用，应优先覆盖最相关的；也**不要"中了 Bingo"**——发现一种实现方式就涂绿，同一个技术攻击者往往有多种实现方式。

### 官方给出的三种"不该这么用"

来源：<https://attack.mitre.org/resources/getting-started/>

1. **不要试图达成 100% 覆盖**——优先挑与你相关的。
2. **不要中一个就喊 Bingo**——一个技术有多种实现方式，要持续找其他实现路径。
3. **不要被矩阵框死**——矩阵只记录"已被观察到的真实行为"，攻击者还会用尚未被记录的行为。要结合自有情报源、记录自己观察到的技术，也别只盯行为，及时的情报指标同样能抓到人。

---

## 9. 延伸阅读

- [mapping-guide.md](./mapping-guide.md)：把一次测试的发现映射到 ATT&CK 技术编号，含 3 个完整示例与常见错误。
- [labs.md](./labs.md)：练习——导入层文件、做一次模拟 APT 的 TTP 覆盖度分析。
- 上级模块：[../README.md](../README.md)
- 相邻标准：[OWASP / WSTG](../owasp/README.md) ｜ [PTES](../ptes/README.md) ｜ [Exploit-DB](../exploit-db/README.md) ｜ [CWE](../cwe/README.md) ｜ [NIST SP 800](../nist/README.md)

## 10. 来源 URL

- ATT&CK 官网首页：<https://attack.mitre.org/>
- 企业战术列表：<https://attack.mitre.org/tactics/enterprise/>
- 移动战术列表：<https://attack.mitre.org/tactics/mobile/>
- 工控战术列表：<https://attack.mitre.org/tactics/ics/>
- 企业矩阵：<https://attack.mitre.org/matrices/enterprise/>
- 入门指南（核心概念、四类用法、三种"不该这么用"）：<https://attack.mitre.org/resources/getting-started/>
- 版本历史：<https://attack.mitre.org/resources/versions/>
- 技术页示例 T1566 Phishing：<https://attack.mitre.org/techniques/T1566/>
- ATT&CK Navigator 在线实例：<https://mitre-attack.github.io/attack-navigator/>
- ATT&CK Navigator 仓库与 USAGE 文档：<https://github.com/mitre-attack/attack-navigator>
