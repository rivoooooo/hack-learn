# ATT&CK 实验：导入层文件与模拟 APT 的 TTP 覆盖度分析

本页是两个可复现的动手练习。全部操作**无需安装任何软件**，只需浏览器；进阶部分可选装本地实例。

- 阅读前置：[README.md](./README.md) ｜ [mapping-guide.md](./mapping-guide.md)
- 工具：ATT&CK Navigator <https://mitre-attack.github.io/attack-navigator/>
- 依据：<https://attack.mitre.org/>、<https://github.com/mitre-attack/attack-navigator>（抓取日期 2026-09-15）

> 所有练习均使用**公开的 ATT&CK 知识库数据**和**虚构的本地环境**，不涉及对任何真实系统的测试。

---

## 实验 0（可选）：把 Navigator 部署到本地

只在层文件含敏感信息时需要。官方在线实例是纯客户端应用，层文件不上传服务器，但官方仍建议敏感内容本地部署。

**前置要求**（核取自 <https://github.com/mitre-attack/attack-navigator>）：Node.js v22、Angular CLI v19。

```bash
git clone https://github.com/mitre-attack/attack-navigator.git
cd attack-navigator/nav-app
npm install
ng serve
# 浏览器打开 http://localhost:4200
```

或用 Docker 跑开发容器：

```bash
cd attack-navigator/nav-app
docker build -f Dockerfile.dev -t nav-app-dev .
docker run -p 4200:4200 nav-app-dev
```

离线运行还需要把 ATT&CK 数据文件放到本地，并修改 `nav-app/src/assets/config.json` 的 `versions` 配置指向本地文件，例如：

```json
"versions": {
  "enabled": true,
  "entries": [
    {
      "name": "Local Enterprise STIX Data",
      "version": "19",
      "domains": [
        {
          "name": "Enterprise",
          "identifier": "enterprise-attack",
          "data": ["assets/enterprise-attack.json"]
        }
      ]
    }
  ]
}
```

生产构建：

```bash
ng build --configuration production
# 产物在 nav-app/dist/browser/
```

---

## 实验 1：创建层 → 导出 JSON → 重新导入

**目标**：跑通"层"的完整生命周期，理解层文件就是一份 JSON。

### 步骤

1. 打开 <https://mitre-attack.github.io/attack-navigator/>。
2. 点 "**Create New Layer**" → 选 Enterprise 域、当前 ATT&CK 版本。
3. 记下页面右上角显示的 ATT&CK 版本号（写作时官网 current 为 **v19.2**，你的实操可能已更新）。
4. 点右上角 "**?**" 打开应用内帮助，找到 "Create New Layer" 与 "Open Existing Layer" 两节，对照本页 [README 第 7 节](./README.md#7-用-attck-navigator-做覆盖度热力图) 阅读。
5. 点战术表头 "**Initial Access**"，全选该列。
6. 点 "**Scoring Techniques**"（柱状图图标），给全部选中项打分 `1`。
7. 点 "**Color Setup**"（调色板图标）：
   - 把 "low value" 设为 `0`，并把 0 对应的颜色设为**透明**；
   - 把 "high value" 设为 `1`，1 对应颜色设为 `#66ff00`（绿色）。
   - 预期效果：只有打分为 1 的格子是绿色，其余保持无底色。
8. 右键任意一个已选技术 → 选 "**add to selection**" 或 "**remove from selection**"，观察选中集合的变化。
9. 点 "**Adding Comments to Techniques**"（对话气泡图标），给任意一个技术写注释 "lab1 手工标注"。预期：该单元格出现**黄色下划线**，鼠标悬停显示注释。
10. 点 "**save layer**"（下载图标）→ "**download single layer as json**"。
11. 用文本编辑器打开下载的 JSON，**记录以下字段的实际取值**：

    | 字段 | 你看到的实际值 |
    | --- | --- |
    | `name` | |
    | `versions.attack` | |
    | `versions.navigator` | |
    | `domain` | |
    | `gradient.minValue` / `maxValue` | |
    | `techniques` 数组长度 | |
    | 第 1 个 `techniques` 元素的全部键 | |

12. 手工编辑这份 JSON：把 `name` 改成 `我的第一个层`，在 `techniques` 数组里**手工新增**一条：

    ```json
    { "techniqueID": "T1071.001", "score": 1, "color": "", "comment": "手工新增，验证 JSON 可编辑" }
    ```

13. 回 Navigator，新开一个标签页 → "**Open Existing Layer**" 面板 → "**Upload from local**" → 选择你改过的 JSON。
14. 确认：层名变成 `我的第一个层`，且 `T1071.001`（Command and Control 列）已被选中并着色。

### 验收标准

- [ ] 能说清 `domain` 字段的作用（决定贴在哪个矩阵上）
- [ ] 能解释为什么 `unscored` 与 `score: 0` 在渐变上表现不同
- [ ] 手工改过的 JSON 能被成功导入并正确渲染
- [ ] 能说出 `versions.attack` 为什么必须写（提示：见 [mapping-guide 错误 5](./mapping-guide.md#错误-5忽略版本差异尤其是-defense-evasion)）

### 思考题

如果你把 `domain` 从 `enterprise-attack` 改成 `mobile-attack`，`T1566.001` 还会显示吗？为什么？（提示：T1566 是 Enterprise 域的技术，Mobile 域编号体系不同，见 [README 第 2 节](./README.md#2-三个技术域technology-domains)。）

---

## 实验 2：模拟 APT 的 TTP 覆盖度分析

**目标**：以真实攻击组织的公开 TTP 为基线，对一份虚构的企业环境做覆盖度评估，产出热力图与缺口清单。

### 虚构环境（作为你的"被保护对象"）

| 项 | 描述 |
| --- | --- |
| 组织 | ACME 制造有限公司（虚构） |
| 终端 | 1,200 台 Windows 11 办公终端、80 台 Windows Server 2022、40 台 Ubuntu 22.04 |
| 身份 | 微软 Entra ID（云身份提供商）+ 本地 AD 双轨 |
| 邮件 | Microsoft 365 邮件 + 第三方邮件网关 |
| 边界 | 下一代防火墙 + 公网 Web 应用 3 个（Java / .NET / Nginx+PHP） |
| 现有检测能力 | EDR（全终端）、DNS 日志、防火墙日志、Entra ID 登录取证日志、Sysmon（仅服务器） |
| **没有** | 邮件附件沙箱、内存扫描、网络流量元数据（NDR）、云工作负载日志 |

### 第 1 步：选对手，生成"威胁基线层"

1. 在 Navigator 里新建一个层，命名为 `基线-对手TTP`。
2. 点 "**Search & Multiselect Interface**"（放大镜图标）。
3. 在搜索框里填入一个真实攻击组织的 PUBLIC 名称（例如 `MuddyWater`、`Kimsuky`、`APT29` 均是 ATT&CK 中收录的组织；本项目练习**任选一个**并在报告里注明你选了谁）。
4. 在搜索结果下方的 "**Threat Groups**" 列表里找到该组织，点它的 "**select**" 按钮。
   - 预期：矩阵中该组织用过的**全部技术被一次性选中**。记录这个数量 `N_baseline`。
5. 用 "**Adding Comments to Techniques**" 给每个必选技术加一句 "APT-基线"。
6. 点 "**save layer**" → "**download single layer as json**"，文件名存为 `baseline.json`。

> **记录**：你选的对手 = ____________；基线技术数 `N_baseline` = ______

### 第 2 步：做环境适用性过滤

7. 点 "**Filtering**"（漏斗图标）→ **Platform Filter**：
   - 反选 `Linux` 与 `macOS`（环境中 Linux 占比小，本练习先只看 Windows 侧）；
   - 保留 `Windows`、`Office Suite`、`Identity Provider`、`SaaS`、`IaaS`、`Network Devices`。
8. 对过滤后**仍然留在视图里**的技术，逐个判断在 ACME 环境中是否**适用**：
   - 不适用（例：要求 IaaS 云工作负载日志而 ACME 没有）→ 右键 "**remove from selection**"，并在 comment 里写 "不适用：无该平台资产"。
   - 适用 → 保留选中。
9. 记录过滤后数量 `N_applicable` = ______。

### 第 3 步：做检测覆盖度打分（这是核心工作）

10. 新建第二个层，命名 `覆盖度-现状`（用 "**Create New Layer**"，不要覆盖上一个层；Navigator 支持同时打开多个层）。
11. 在 `覆盖度-现状` 层里，按第 2 步得到的技术集合逐个选中并打分。**打分规则**（三档，写进层描述里）：

    | 分数 | 含义 | 判断依据 |
    | --- | --- | --- |
    | `0` | 无遥测 | 该技术执行后，现有日志源里**不会留下任何记录** |
    | `1` | 有遥测，无规则 | 日志里有痕迹，但没有专门检测规则，靠人肉翻日志 |
    | `2` | 有规则，未验证有效性 | 已写检测规则并上生产，但从未用真实 TTP 验证过 |
    | `3` | 有规则且验证有效 | 红队/Purple 演练中实际触发并确认告警可达 |

12. 每个技术的 comment 必须写清**依赖哪个日志源**。示例：

    ```
    T1053.005 / score 1 / comment: "Windows 安全日志 4698 有记录，但未建检测规则；Sysmon 未覆盖办公终端"
    T1003.001 / score 0 / comment: "无内存扫描能力，EDR 未开启 LSASS 访问告警"
    ```

13. 点 "**Color Setup**"：
    - "low value" = `0`（透明）、"high value" = `3`（深绿）；
    - 叠加一层视觉区分：对 `score = 0` 的技术，用 "**Assigning Manual Colors**" 手工涂成**红色**（手动色会覆盖渐变派生色，这正是我们想要的：红色醒目地标出"完全看不见"）。
14. 点 "**Adding Metadata**"（元数据图标），给每个技术加两个键值对：`owner`（负责团队）和 `due`（整改截止日期）。

### 第 4 步：白纸测试（Peer Review）

15. 找一位同事，**只给他 `覆盖度-现状` 层**（不给你的 comment），让他自己给 5 个技术重新打分。
16. 比对分歧。分歧点通常暴露"日志源是否存在"这类事实性认知差异——这类分歧最有价值。
17. 记录分歧数量 `N_dispute` = ______。

### 第 5 步：出图与产出

18. 点 "**render layer to SVG**"（相机图标）：
    - "**Configuring Image Size**"：宽 `11`、高 `17`、header 高 `1`（单位用 "**toggle measurement unit**" 切到 `in`）；
    - "**Display Settings**" 勾选：Show header、Show about、Show domain、Show legend、Show filters；
    - sub-techniques 选 "**show expanded**"（子技术要展开，否则看不清缺口）；
    - 点 "**download svg**"。
    - 若用 Edge 下载得到 `.txt`，改名为 `.svg`。
19. 出正式 PDF 前，点工具栏图钉图标**关掉粘性工具栏**，再用浏览器打印 → 存为 PDF，避免矩阵被截断。
20. 另外导出 Excel 便于排期：菜单里选 "**export single layer to excel**"。

### 第 6 步：写分析结论

按以下结构产出（这正是 [PTES 报告模板](../ptes/templates.md) 里"发现"章节可用的素材）：

```
一、基线
选择的对手：__________（ATT&CK 中的 G 编号：______）
基线技术数 N_baseline：______
环境过滤后适用技术数 N_applicable：______

二、覆盖度现状
score 3（验证有效）：____ 条，占比 ____%
score 2（有规则未验证）：____ 条，占比 ____%
score 1（有遥测无规则）：____ 条，占比 ____%
score 0（完全无遥测）：____ 条，占比 ____%

三、Top 5 最高风险缺口（按"对手常用度 × 我方不可见度"排序）
1. 技术编号 / 名称 / 为什么是缺口 / 需要补什么日志源或规则 / 责任团队 / 截止日
2. ...
3. ...
4. ...
5. ...

四、结论的三条限制（必写）
1. 本评估只覆盖了与所选对手相关的技术子集，不代表全量威胁覆盖；
2. score 2 的条目未经真实演练验证，实际有效性存疑；
3. ATT&CK 版本为 v____，与本报告不兼容的旧版映射需重新核对。
```

### 验收标准

- [ ] 产出 `baseline.json` 与 `覆盖度-现状` 层共两个可导入的 JSON 文件
- [ ] 每个技术都有 comment 说明依赖的日志源
- [ ] 有一张展开子技术的 SVG 热力图
- [ ] 有一份含 `N_baseline`、`N_applicable`、`N_dispute` 的结论
- [ ] 结论里写了第 6 步要求的三条限制

### 自检：三个"官方明令不要做"

本实验**故意不要求**你做到以下三件事，请你判断自己的产出有没有犯：

1. 你是否试图覆盖 100% 的技术？（官方：不应追求 100% 覆盖，只挑与环境相关的）
2. 你是否因为一个技术"某一种实现方式被覆盖了"就打了满分？（官方：不要中一个就喊 Bingo，一个技术往往有多种实现）
3. 你是否只映射了矩阵里已有的技术，而忽略了自己环境里观察到但 ATT&CK 尚未收录的行为？（官方：矩阵只记录已被观察到的真实行为）

对照来源：<https://attack.mitre.org/resources/getting-started/>

---

## 实验 3（进阶）：用脚本生成层文件

**目标**：理解层文件是机器可生成的，可以接进 CI。

参照 Navigator 仓库 `layers` 目录里的格式规范与示例脚本，写一个最小脚本，把一份 CSV 转成层 JSON。

输入 `coverage.csv`：

```csv
techniqueID,score,comment
T1566.001,1,邮件网关可拦但无沙箱
T1059.001,1,仅有进程创建日志
T1071.001,0,无 DNS 与流量元数据
T1078.004,2,Entra ID 已有规则未验证
```

期望输出 `coverage.json`：

```json
{
  "name": "ACME 自动生成覆盖度",
  "versions": { "attack": "19", "navigator": "5.1.0", "layer": "4.5" },
  "domain": "enterprise-attack",
  "description": "由 CI 每周生成",
  "gradient": { "colors": ["#ffffff", "#66ff00"], "minValue": 0, "maxValue": 3 },
  "techniques": [
    { "techniqueID": "T1566.001", "score": 1, "comment": "邮件网关可拦但无沙箱" },
    { "techniqueID": "T1059.001", "score": 1, "comment": "仅有进程创建日志" },
    { "techniqueID": "T1071.001", "score": 0, "comment": "无 DNS 与流量元数据" },
    { "techniqueID": "T1078.004", "score": 2, "comment": "Entra ID 已有规则未验证" }
  ]
}
```

**验收**：生成的 JSON 能被 Navigator 的 "**Open Existing Layer**" → "**Upload from local**" 正确加载，4 个格子按分数着色。

**进阶问题**：`versions.attack` 该填 `"19"` 还是 `"19.2"`？——**导出你自己的层文件，看 Navigator 实际写的是什么**，以实际导出为准。这是本练习最重要的方法：**不要猜字段，导出一次就有权威答案。**

---

## 常见问题排查

| 现象 | 原因 | 处理 |
| --- | --- | --- |
| 上传层文件后报错 | JSON 语法错误（多逗号、缺引号） | 用 JSON 校验工具过一遍 |
| 技术全部错位或消失 | `domain` 或 `versions.attack` 不匹配 | 核对 `domain` 与 ATT&CK 版本 |
| 打了分但格子不上色 | 分数超出 gradient 的 min/max，或颜色设成了透明 | 检查 "Color Setup" 的 low/high value |
| 格子有颜色但和我预期相反 | 手动色覆盖了渐变 | 在颜色面板顶部选 "**no color**" 清除手动色 |
| 下载的图片打不开 | Edge 下载成 `.txt` | 改名为 `.svg` |
| 打印出来的矩阵被截断 | 粘性工具栏占用空间 | 先点图钉图标关掉粘性工具栏 |
| 不能新建更多层 | 已达 10 层上限 | 关掉不用的层 |
| 子技术看不到 | 子技术被折叠 | 点 "**expand sub-techniques**" |

---

## 来源 URL

- ATT&CK Navigator 在线实例：<https://mitre-attack.github.io/attack-navigator/>
- ATT&CK Navigator 仓库（安装、层格式、USAGE 文档）：<https://github.com/mitre-attack/attack-navigator>
- ATT&CK 入门指南（核心概念、四类用法、"不该这么用"三条）：<https://attack.mitre.org/resources/getting-started/>
- 企业矩阵：<https://attack.mitre.org/matrices/enterprise/>
- 企业战术列表：<https://attack.mitre.org/tactics/enterprise/>
- 版本历史：<https://attack.mitre.org/resources/versions/>

> ⚠️ 待核实项：本页示例中 `versions.navigator` 值 `5.1.0` 与 `versions.layer` 值 `4.5` 是**格式示例**，未从官网逐一核实当前版本号。请在实验第 1 步用 "**download single layer as json**" 导出一次真实层文件，以导出结果中的实际版本号为准替换。
