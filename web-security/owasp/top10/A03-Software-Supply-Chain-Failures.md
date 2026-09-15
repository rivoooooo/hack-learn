# A03:2025 软件供应链失效（Software Supply Chain Failures）

> 官方详情页：<https://top10.owasp.org/2025/A03_2025-Software_Supply_Chain_Failures/>
> 排名：**第 3 位**（2021 版为第 6 位的"易受攻击和过时的组件"，**上升 3 位并大幅扩展范围**）
> CWE 数量：6 个（官方正文亦提及 5 个核心 CWE）｜平均发生率：**5.72%（全榜最高）**｜相关 CVE：仅 11 条

## 一句话理解

软件供应链失效是指**你信任的代码、工具、依赖、构建与分发环节被污染或腐化**，从而让攻击者的代码"搭便车"进入你的生产环境——它不只是"用了有漏洞的库"，而是整条"从源码到制品"的链条都算在内。

## 风险原理

只要你的应用里有一行代码不是你写的，你就把一部分信任交给了外部。供应链失效的本质是**信任边界失控**。

2025 版把范围从 2021 版的"易受攻击和过时的组件（Vulnerable and Outdated Components）"扩展为：

1. **依赖层面**：直接依赖、传递依赖（transitive dependency）、嵌套依赖，未跟踪版本、未做漏洞扫描。
2. **构建层面**：CI/CD 流水线、构建工具、构建脚本被篡改；构建环境密钥泄露。
3. **分发层面**：制品仓库、容器镜像仓库、CDN 上的产物被替换；无签名、无来源证明。
4. **开发工具层面**：IDE、IDE 插件、开发工作站被攻陷（现在的攻击者把开发者本人当目标）。
5. **流程层面**：无变更管理、无职责分离，一个人可以从写代码一路推到生产而无人复核。

官方给出的"高风险信号"包括：不跟踪组件版本、组件已停止维护、不定期扫描、供应链任何环节没有变更追踪、供应链系统没有职责分离、从不信任来源引入组件、补丁按季度而非按风险及时修复、更新后不测试兼容性、CI/CD 安全性弱于它构建的系统。

ASCII 数据流图（供应链攻击面）：

```
[上游开源包] --(1)投毒--> [包仓库 npm/PyPI/Maven]
                                |
                                v
[开发者工作站] --(2)IDE插件/依赖安装--> [代码仓库]
                                |
                                v
                        [CI/CD 构建流水线] --(3)构建脚本篡改 / 密钥窃取
                                |
                                v
                        [制品仓库 / 容器镜像] --(4)镜像替换 / 无签名
                                |
                                v
                          [生产环境]  <-- 攻击者代码在此执行
```

## 典型场景与真实案例模式

> 以下案例均为 **OWASP 官方 A03 页面正文引用的真实事件**，此处仅转述，未自行补充细节。

- **可信厂商被植入恶意代码，随升级分发（案例模式：供应商入侵）。** 官方引用 2019 年 SolarWinds 事件，导致约 18,000 个组织受影响；以及 2025 年一起钱包软件供应链攻击，恶意代码仅在特定条件下触发（只在目标钱包被使用时执行）。
- **自传播的包管理器蠕虫（案例模式：npm 生态投毒）。** 官方引用 2025 年的 `Shai-Hulud` 攻击，被称为首个成功的自传播 npm 蠕虫：攻击者发布热门包的恶意版本，借 `post-install` 脚本窃取并外传敏感数据到公开 GitHub 仓库；同时检测受害者环境中的 npm token，用它自动给可访问的包发布恶意版本，波及 500 多个包版本后才被 npm 遏止。官方强调：**开发者本人已成为供应链攻击的首要目标**。
- **组件自身漏洞导致大规模入侵（案例模式：常见依赖的 RCE）。** 官方引用 CVE-2017-5638（Struts 2 远程代码执行）与 CVE-2021-44228（"Log4Shell"，Apache Log4j 远程代码执行零日）。
- **传递依赖翻车。** 项目只锁定了直接依赖，但某传递依赖被替换/投毒，构建时被拉入。
- **构建产物不可追溯。** 制品没有 SBOM、没有签名、没有来源证明（provenance），出现问题无法定位"这批镜像到底用了哪个版本"。
- **CI/CD 是更弱的一环。** 流水线能读到生产密钥，却只有比生产系统更弱的访问控制，成为攻击者的跳板。

## 怎么测

对应 WSTG 测试项（供应链难以黑盒测出，需结合代码/流程审计）：

- [WSTG-INFO-10](../wstg/checklist.md) 测绘应用架构（识别依赖与技术栈）
- [WSTG-INFO-08](../wstg/checklist.md) 指纹识别 Web 应用框架
- [WSTG-CONF-02](../wstg/checklist.md) 应用平台配置
- [WSTG-CONF-11](../wstg/checklist.md) 云存储（制品/备份泄露）

**手工与工具测试步骤**

1. **识别前端依赖版本。** 查看页面引用的 JS/CSS 库与版本，比对已知漏洞库。
   ```bash
   # 浏览器插件类工具（如 Wappalyzer）识别技术栈，或用发包观察静态资源特征
   curl -s https://target/ | grep -oE '<script[^>]+src="[^"]+"'
   ```
   对识别到的 JS 库用 Retire.js 检查：
   ```bash
   npx retire --path ./static --outputformat json
   ```
2. **检查源码映射与包清单是否暴露。**
   ```bash
   curl -s -o /dev/null -w '%{http_code}\n' https://target/static/js/main.js.map
   curl -s -o /dev/null -w '%{http_code}\n' https://target/package.json
   ```
3. **服务端依赖核查。** 若能获得源码或镜像，跑软件成分分析（SCA）：
   ```bash
   # Java / Maven
   mvn org.owasp:dependency-check-maven:check
   # Node
   npm audit --json
   # 容器镜像
   trivy image <image:tag>
   ```
4. **核查 SBOM 是否存在。** 询问/索取 CycloneDX 或 SPDX 格式 SBOM；若无 SBOM，本身就是一个发现项。
5. **审计构建与分发流程。** 检查：制品是否签名？镜像是否有 provenance？CI 是否允许任意人修改流水线？密钥是否可被构建脚本读取？是否可跳过复核直接发布？
6. **检查子域名接管风险。** 供应的 CDN/第三方服务若已下线但仍被 DNS 指向，攻击者可接管并投毒前端资源。
   ```bash
   dig +short CNAME cdn.target.com
   # 若指向已失效的第三方服务（如已注销的云资源），则存在接管风险
   ```
7. **检查自动更新机制。** 客户端/设备固件更新是否验签？更新服务器是否可被劫持？

## 代码示例

### 易受攻击的实践（任意语言，配置/流程层面）

```dockerfile
# 危险 1：使用可变标签 latest，无法复现、无法追溯
FROM node:latest

# 危险 2：以 root 运行，且直接从网络管道执行脚本（供应链投毒高危）
USER root
RUN curl -fsSL https://example.com/install.sh | bash

# 危险 3：未锁定依赖版本，每次构建拉到的可能不是同一份代码
COPY package.json ./
RUN npm install        # 而非 npm ci
```

```yaml
# 危险 4：CI 流水线允许任意分支写入，且权限过大
on: [pull_request]
permissions: write-all          # PR 即可读写仓库与 secrets
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@main          # 未锁定到 commit SHA
        with:
          ref: ${{ github.event.pull_request.head.sha }}
      - run: npm run build && npm publish    # PR 内容可直接发布
```

### 修复后的实践

```dockerfile
# 修复 1：使用不可变的基础镜像 digest，锁定到具体版本
FROM node:24.10.0-bookworm@sha256:<完整digest>

# 修复 2：非 root 运行
RUN groupadd -r app && useradd -r -g app app
USER app

# 修复 3：锁定依赖，用 npm ci 严格按 lockfile 安装，并校验完整性
COPY package.json package-lock.json ./
RUN npm ci --ignore-scripts          # 必要时禁用 postinstall 脚本
```

```yaml
# 修复 4：最小权限 + 锁定第三方 Action 到 commit SHA + 环境隔离 + 发布需人工审批
on:
  push:
    branches: [main]
permissions:
  contents: read                     # 默认只读，需要时按步授权
jobs:
  build:
    runs-on: ubuntu-latest
    environment: production-release  # 受保护环境，发布需审批
    steps:
      - uses: actions/checkout@<40位commit SHA>   # 锁定版本，不用 @main
      - run: npm ci --ignore-scripts
      - run: npm run build
      - name: Generate SBOM
        run: npx @cyclonedx/cyclonedx-npm --output-file sbom.json
      - name: Sign artifact
        run: cosign sign-blob --yes dist/app.tar.gz
```

> 修复思路总结：**锁定（pin）+ 验证（verify）+ 最小权限（least privilege）+ 可追溯（traceable）**。

## 防御清单

- [ ] 集中生成并管理 **SBOM**（软件物料清单），覆盖直接与传递依赖。
- [ ] 用工具持续清点版本：OWASP Dependency-Track、OWASP Dependency-Check、retire.js、Trivy、Grype。
- [ ] 持续监控 CVE / NVD / OSV 等漏洞源，并订阅相关组件安全公告。
- [ ] 移除未使用的依赖、功能、组件、文件与文档，缩小攻击面。
- [ ] 只从官方（可信）来源获取组件，优先使用**已签名**的包。
- [ ] 明确选择依赖版本，仅在确有需要时升级；不盲目追 `latest`。
- [ ] 定期更新 CI/CD、IDE 与所有开发工具。
- [ ] 用**分阶段发布/金丝雀发布**替代"全量同时更新"，防止上游被污染时全军覆没。
- [ ] 对 CI/CD 设置、代码仓库、沙箱、IDE、SBOM 工具、制品、日志系统、第三方集成建立**变更管理/追踪**。
- [ ] 加固代码仓库（分支保护、禁止提交密钥、备份）、开发工作站（补丁、MFA、监控）、构建服务器（职责分离、访问控制、签名构建、环境级密钥、防篡改日志）、制品（来源证明、签名、时间戳、晋升而非重复构建）。
- [ ] 基础设施即代码（IaC）与普通代码同等管理（走 PR 与版本控制）。
- [ ] 参考 [Vulnerable Dependency Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html)、[Dependency Graph SBOM Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Dependency_Graph_SBOM_Cheat_Sheet.html)、[Software Supply Chain Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html)。

## 常见坑

- **坑 1：只扫直接依赖。** 真正的风险常在传递依赖里。必须覆盖完整依赖树。
- **坑 2：只看 CVE 数量。** A03 的 CVE 数量全榜最少（11 条），但**平均利用分与影响分最高**。数据少是因为"难测"，不代表风险低。
- **坑 3：SBOM 生成了却没人用。** SBOM 的价值在于"出事时能 5 分钟内定位受影响版本"，而不是交付一份文件。
- **坑 4：依赖锁文件存在但 CI 里用 `npm install`。** `install` 会重新解析版本，必须用 `npm ci`（严格按 lockfile）。
- **坑 5：信任 `postinstall` 脚本。** 包管理器蠕虫正是靠安装脚本执行代码。对不受信任或不需要构建的依赖应禁用安装脚本。
- **坑 6：把"装了 SCA 扫描器"当作完成。** 扫描结果需要有人分诊、定 SLA、跟踪修复，否则只是告警堆积。
- **坑 7：一次性升级所有系统。** 上游被污染时，同时升级等于同时中招，必须分批/金丝雀。
- **坑 8：忽视开发工作站。** 开发者机器通常不被视为"生产资产"，但它持有源码与发布凭据，是最有价值的目标。

## 自测题

**1. A03 的平均发生率是全榜最高的 5.72%，但相关 CVE 只有 11 条。如何解释这个矛盾？**

<details><summary>答案</summary>

因为供应链失效极难通过常规黑盒测试与 CVE 记录体系捕捉：污染可能只在特定条件触发、构建期攻击不产生运行时告警、上游投毒未必分配 CVE。同时该类别 CVE 的平均利用分与影响分最高，说明一旦被利用，后果最严重。数据少 = 可见性差，不等于风险低。
</details>

**2. 为什么 `curl https://example.com/install.sh | bash` 在 CI 里特别危险？**

<details><summary>答案</summary>

它把"远程可变内容"直接作为构建机上的可执行代码运行，且通常在拥有密钥、可写入制品仓库的 CI 环境中。攻击者只需污染该 URL 指向的脚本，即可以 CI 的身份执行任意操作，并进一步污染所有下游产物。修复：固定版本与校验和，或将脚本纳入仓库并走审查。
</details>

**3. 团队只锁定了 `package.json` 的直接依赖，但没有提交 lockfile。风险是什么？**

<details><summary>答案</summary>

传递依赖版本在每次安装时可能被重新解析到不同版本，构建不可复现，攻击者可通过污染某个传递依赖的补丁版本在任意一次构建时引入恶意代码。修复：提交 lockfile，并在 CI 中用 `npm ci` 严格安装。
</details>

**4. 什么是"发布制品晋升（promote）而非重复构建"，为什么重要？**

<details><summary>答案</summary>

指同一个经过测试与签名的制品被逐环境提升（测试→预发→生产），而不是每个环境重新构建一次。这样能保证生产运行的正是被测过、被签过的那份制品，避免"构建环境被污染导致生产制品与测试制品不一致"。也便于用来源证明（provenance）追溯。
</details>

**5. 公司把一个已注销的第三方 CDN 域名仍保留在 DNS 中。这属于 A03 还是别的？危害是什么？**

<details><summary>答案</summary>

属于供应链失效（对应 WSTG-CONF-10 子域名接管）。若第三方服务已释放该资源，攻击者可注册/接管该域名，从而控制所有引用该 CDN 的前端资源加载，实现全站脚本注入或流量劫持。修复：清理失效 DNS 记录，并对所有第三方依赖做生命周期监控。
</details>

## 来源

- <https://top10.owasp.org/2025/A03_2025-Software_Supply_Chain_Failures/>
- <https://top10.owasp.org/2025/0x00_2025-Introduction/>
- <https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html>
- <https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html>
