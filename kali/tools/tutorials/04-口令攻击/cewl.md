# CeWL（网站词汇爬取字典生成器）

> **一句话**：爬取目标网站，把页面上的词、元数据里的作者名、邮箱地址抽取出来，形成「与目标高度相关」的口令与用户名字典。
> **分类**：口令攻击 ｜ **Kali 包**：`cewl` ｜ **官方文档**：<https://github.com/digininja/CeWL>

## 1. 它解决什么问题

口令审计里有一条铁律：**最危险的口令不是 `123456`，而是 `公司名+年份`**。

通用字典（[rockyou](wordlists.md)）能命中大量弱口令，但对「组织特有词汇」几乎没有覆盖。CeWL（Custom Word List generator，**读作 "cool"**）的作用就是补上这块：**用目标自己网站上的词汇，造出针对这个组织的字典**。

| 工具 | 覆盖的候选 | 场景 |
| --- | --- | --- |
| [wordlists](wordlists.md) / [seclists](wordlists.md) | 大众化弱口令 | 第一遍撒网 |
| [crunch](crunch.md) | 结构化组合 | 已知口令规则 |
| **CeWL** | **组织相关词汇**（产品名、地名、标语、员工名） | 前两者都失效时的**关键一手** |

CeWL 还能做第二件事：从 `mailto:` 链接和文件元数据里抽取**邮箱与用户名**，可以直接拿去做用户名列表。

## 2. 工作原理

### 2.1 三步流水线

```
[1] 爬取   →  从起始 URL 出发，按 --depth 递归抓取同站页面
                   ↓
[2] 抽取   →  去掉 HTML 标签，按分隔符切词，过滤长度小于 --min_word_length 的词
                   ↓
[3] 输出   →  去重后的词表（可选：附带词频 --count、邮箱 --email、元数据 --meta）
```

**具体的抽取逻辑**（决定了 CeWL 输出长什么样）：

1. 请求页面 → 得到 HTML。
2. 用正则/解析器**剥掉标签**，只留可见文本。
3. 按「非字母数字」字符切分（连字符、标点、空白都是分隔符）。
4. 过滤：长度 < `-m`（默认 3）的词丢弃。注意 CeWL 默认**只保留纯字母词**——含数字的词（如 `admin2026`）会被切成 `admin`。要保留含数字的词得加 `--with-numbers`。
5. 去重；`-c` 时附带出现次数。
6. `--lowercase` 时全部转小写。

**为什么第一页特别重要**：CeWL 会同时爬取**页面里引用的文档**（PDF、Word、Excel）来提取元数据（`-a` / `--meta`）。这些文件的「作者」「公司」字段常常直接暴露真实用户名格式（如 `zhang.wei`），这是 CeWL 最被低估的能力。

### 2.2 与 FAB（Files Already Bagged）的关系

CeWL 项目还提供一个配套工具 `fab-cewl`（FAB = Files Already Bagged）：

```bash
fab-cewl 文件1.pdf 文件2.docx
```

它专门从**已有文件的元数据**里抽取作者/创建者字段，产出用户名候选。**用法**：先用外部手段（如共享目录、公开文档、搜索引擎）收集一批文件，再用 FAB 提取可能的用户名格式，然后：

- 用户名列表 → 喂给 [hydra](hydra.md)/[medusa](medusa.md)/[ncrack](ncrack.md) 的 `-L`
- 单用户名 + CeWL 词表 → 组合成 `crunch`/`hashcat -a 6` 的组合

### 2.3 为什么它有效

人类选择口令的方式高度依赖**认知可达性（cognitive availability）**：眼前看到的、天天说的词，最容易被选作口令。所以：

- 网站上的**产品名、标语、地名、品牌词**必然是组织内口令的高频素材；
- **员工姓名**（元数据里的作者字段）常被用作口令或用户名；
- 这些词几乎不在 rockyou 里 —— 因为 rockyou 是 2009 年从某网站泄露的英文大众口令。

**这一条正是蓝队的反面教材**：企业网站上不应该出现「会被用来猜口令的内部词汇」。

## 3. 安装与快速上手

```bash
sudo apt install cewl
cewl -h        # 帮助本身就是一个完整的选项表
```

快速上手：

```bash
# 爬 2 层深、词长 ≥ 5、写到文件
cewl -d 2 -m 5 -w docswords.txt https://example.com

wc -l docswords.txt
# 13 docswords.txt

# 同时抓邮箱
cewl -e -d 2 -m 5 --email_file emails.txt -w words.txt https://example.com
```

**注意**：`-v` 只显示「找到新词」的消息，**字典本体只写到 `-w` 指定的文件里**（或 stdout）。不加 `-w` 时词表会混在提示信息里，不利于后续处理。

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
| --- | --- | --- |
| `<url>` | 起始 URL（必需） | 用你自己的站点或已授权目标 |
| `-d <x>` / `--depth <x>` | 爬取深度，默认 2 | 深度越大越慢；`-d 3` 已是实用上限 |
| `-m <x>` / `--min_word_length <x>` | 最小词长，默认 3 | **建议提到 5**：短词命中率极低，只增加字典体积 |
| `-x <x>` / `--max_word_length <x>` | 最大词长，默认无限 | 排除超长字符串（如 base64 串） |
| `-w <file>` / `--write <file>` | 词表输出文件 | 落地必备 |
| `-o` / `--offsite` | 允许爬取站外链接 | **慎用**：会跑飞，爬遍整个互联网 |
| `--exclude <file>` | 排除路径的文件列表 | 排除 `/logout`、`/delete` 等会改变状态的路径 |
| `--allowed <regex>` | 路径必须匹配此正则才会被跟随 | 限定在特定目录内，如 `--allowed '/blog/.*'` |
| `-u <agent>` / `--ua <agent>` | 自定义 User-Agent | 目标有 UA 限制时 |
| `-n` / `--no-words` | 不输出词表 | **只要邮箱或元数据时用** |
| `-c` / `--count` | 每个词后面附出现次数 | 用来**按词频排序**，优先试高频词 |
| `-v` / `--verbose` | 显示过程信息 | 排错用 |
| `--debug` | 额外调试信息 | — |
| `-e` / `--email` | 抽取邮箱地址 | 拿用户名列表 |
| `--email_file <file>` | 邮箱输出文件 | 与 `-e` 搭配 |
| `-a` / `--meta` | 从文件元数据抽取作者等信息 | **重点功能**：常直接暴露用户名格式 |
| `--meta_file <file>` | 元数据输出文件 | — |
| `--meta-temp-dir <dir>` | exiftool 临时目录，默认 `/tmp` | 大文件时改到大分区 |
| `--lowercase` | 全部转小写 | 大多数口令是小写开头 |
| `--with-numbers` | 保留含数字的词 | 站点有 `admin2026` 这类词时**必须加** |
| `--convert-umlauts` | 转换 ISO-8859-1 变音符（ä→ae 等） | 处理欧洲语言站点 |
| `--auth_type` / `--auth_user` / `--auth_pass` | HTTP 认证（Digest 或 Basic） | 需要登录才能爬的站点 |
| `--proxy_host` / `--proxy_port` / `--proxy_username` / `--proxy_password` | 代理设置（默认端口 8080） | 走代理时 |
| `--header` / `-H` | 自定义请求头，格式 `name:value`，可多次 | 需要特定头才能拿到内容时 |
| `-g <x>` / `--groups <x>` | 同时输出词组组合 | 想要短语时用 |
| `-k` / `--keep` | 保留下载的文件 | 调试用，注意磁盘 |

## 5. 实战演练

**环境声明**：以下示例的爬取目标是**你自己搭建的站点**（本地 DVWA / Juice Shop / 自建博客），或**你已获得书面授权的网站**。**严禁**对任何未授权站点执行爬取+生成字典的组合动作——这在很多司法辖区被视为攻击准备行为。

### 场景 1：基础爬取（与官方示例一致）

```bash
cewl -d 2 -m 5 -w docswords.txt https://example.com
```

**预期输出**

```
CeWL 5.4.3 (Arkanoid) Robin Wood (robin@digi.ninja) (https://digi.ninja/)
```

```bash
wc -l docswords.txt
# 13 docswords.txt

sort -u docswords.txt | head
```

**解读**：

- CeWL 的默认输出量比想象中小得多（官方示例只有 13 个词）。这是正常的——**它给的是高信号词，不是大字典**。
- 因此正确的用法是**把 CeWL 的输出与其他字典合并或加规则**：

```bash
cat docswords.txt /usr/share/wordlists/rockyou.txt | sort -u > combined.txt
# 或对 CeWL 词加变形规则，放大命中率
```

### 场景 2：只提取邮箱与元数据（拿用户名列表）

```bash
cewl -n -e --email_file ~/emails.txt -a --meta_file ~/meta.txt \
     -d 2 -v https://your-lab-site.local
```

| 参数 | 效果 |
| --- | --- |
| `-n` | **不输出词表**（只要邮箱和元数据） |
| `-e --email_file` | 抽 `mailto:` 链接里的邮箱 |
| `-a --meta_file` | 从 PDF/Office 文档的元数据里抽作者、公司 |

**查看结果**

```bash
head ~/emails.txt
# zhang.wei@example.com
# li.na@example.com

sort -u ~/meta.txt | head
# 张三
# 李四
# Example Corp
```

**下一步（关键）**：从邮箱推断出**用户名格式**。

```bash
# 常见的三种格式
sed 's/@.*//' ~/emails.txt | head         # zhang.wei
sed 's/@.*//' ~/emails.txt | sed 's/\.//'  # zhangwei
```

把三种格式都生成出来，交给 [hydra](hydra.md) 的 `-L`：

```bash
{
  sed 's/@.*//' ~/emails.txt
  sed 's/@.*//' ~/emails.txt | tr -d '.'
  sed 's/@.*//' ~/emails.txt | cut -d. -f1
} | sort -u > ~/usernames.txt
```

**这是 CeWL 最有价值的使用方式**——**用户名格式**往往比口令本身更难猜。

### 场景 3：处理登录后才能访问的站点

```bash
cewl --auth_type basic \
     --auth_user myuser --auth_pass mypass \
     -d 2 -m 5 --with-numbers --lowercase \
     --exclude ~/exclude-paths.txt \
     -w ~/authed-words.txt \
     http://your-lab-site.local/members/
```

**`--exclude` 文件示例**（避免爬到会执行操作、退出登录的路径）：

```text
/logout
/delete
/admin/remove
/api/v1/delete
```

**务必先写 `--exclude`**：CeWL 会跟随链接，如果站点有「删除」类的 GET 链接，会真的执行删除动作。

### 场景 4：用词频排序，优先试高频词

```bash
cewl -c -d 2 -m 5 -w ~/counted.txt https://your-lab-site.local

# 按出现次数从高到低排序（输出格式：词, 次数）
sort -t, -k2 -nr ~/counted.txt | head -20
```

**解读**：出现频率高 = 这个词是这个组织的「核心词汇」 = 更可能被用作口令素材。**先跑前 200 个高频词**往往比跑 100 万条通用字典更有效。

### 场景 5：FAB —— 从已有文件提取用户名

```bash
# 对你收集到的（你自己的 / 公开的）文档做元数据抽取
fab-cewl ~/docs/*.pdf ~/docs/*.docx
```

**预期输出**：作者名、公司名列表。这些直接就是用户名候选。

再结合 [crunch](crunch.md) 做组合：

```bash
# 用户名 + 4 位数字
crunch 0 0 -q ~/meta-words.txt --stdout 2>/dev/null | head
```

## 6. 输出解读

| 输出 / 文件 | 内容 | 怎么用 |
| --- | --- | --- |
| `-w` 指定的文件 | 去重后的词表，每行一个词 | 合并进主字典，或直接喂破解器 |
| `-c` 时的格式 | `单词, 出现次数` | `sort -t, -k2 -nr` 排序 |
| `-e --email_file` | 邮箱地址 | `sed 's/@.*//'` 推断用户名格式 |
| `-a --meta_file` | 文件元数据里的作者/公司 | 用户名与口令素材 |
| `-v` 的屏幕输出 | 「Found …」之类的过程信息 | **不是词表**，别误当结果 |
| 退出码 0 + 文件非空 | 成功 | — |

**判断成功**：`-w` 文件行数 > 0。

**下一步转化**：

```text
词表 + 词频排序  →  取高频前 N  →  加规则（hashcat -r） →  定向爆破
邮箱 → 去域名 → 三种用户名格式 → -L 用户名列表
元数据作者名 → FAB → 用户名候选
```

## 7. 与其他工具配合

```text
[CeWL 爬站]  ─┬→ 词表（-w）      ─→ hashcat -a 0 -r rules/best64.rule
              ├→ 词频（-c）      ─→ 取高频 N 个优先跑
              ├→ 邮箱（-e）      ─→ 推断用户名格式 ─→ hydra -L
              └→ 元数据（-a）    ─→ FAB ─→ 用户名候选
```

**典型链路 1：网站相关口令**

```bash
cewl -d 2 -m 5 -c -w ~/site-words.txt https://your-lab-site.local
sort -t, -k2 -nr ~/site-words.txt | head -200 | cut -d, -f1 > ~/top200.txt
hashcat -m 0 -a 0 hashes.txt ~/top200.txt -r rules/best64.rule
```

**典型链路 2：用 CeWL 词做组合（`hashcat -a 6/7`）**

```bash
# 词 + 4 位数字后缀
hashcat -m 0 -a 6 hashes.txt ~/site-words-raw.txt '?d?d?d?d'
# 年份前缀 + 词
hashcat -m 0 -a 7 hashes.txt '?d?d?d?d' ~/site-words-raw.txt
```

**典型链路 3：与 [crunch](crunch.md) 配合**

```bash
# 用 CeWL 获取到的词做全排列
crunch 1 1 -q ~/site-words-raw.txt | hashcat -m 0 -a 0 hashes.txt
```

**典型链路 4：无线场景**

Wi-Fi 口令常常就是「公司名/产品名 + 数字」。CeWL 词表 + `?d?d?d?d` 掩码对 WPA 握手包（`hashcat -m 22000`）的效果远好于纯 rockyou。

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
| --- | --- | --- |
| 输出文件是空的 | 只加了 `-v` 忘了 `-w`；或站点是 JS 渲染的（CeWL 不执行 JS） | 加 `-w`；对 SPA 站点先用别的工具拿到静态 HTML |
| 词表里有大量短词/无意义词 | `-m` 默认只有 3，且未过滤 | `-m 5` 或更高；`-x` 限制最大长度 |
| 含数字的词全被切掉了 | 默认只保留纯字母词 | 加 `--with-numbers` |
| 爬到站外去了，跑了很久 | 加了 `-o`，或站点有大量外链 | 去掉 `-o`；用 `--allowed '/blog/.*'` 限定范围 |
| 站点被「退出登录」「删除」了 | 未加 `--exclude`，CeWL 跟随了有副作用的 GET 链接 | **爬之前先列 `--exclude`**；对生产站点一律先只爬 `--depth 1` 观察 |
| 遇到登录墙 | 站点需要认证 | `--auth_type` + `--auth_user`/`--auth_pass`；或带有会话的 `-H 'Cookie: ...'` |
| `--meta` 报 exiftool 相关错误 | 缺少 `libimage-exiftool-perl`；或临时目录满 | `sudo apt install libimage-exiftool-perl`；`--meta-temp-dir /var/tmp` |
| 被 WAF/限流封了 | 请求过快 | 降低 `-d`；走代理 `--proxy_host`；**这不是要绕过防护，而是要意识到对方在告警** |
| 词表太大跑不完 | 直接用了全量词表 | 用 `-c` 按词频排序取前 N 个 |
| 中文字符不生效 | CeWL 的词切分基于非字母数字分隔符，对中文分词无效 | 中文站点效果有限；用 `--convert-umlauts` 也无帮助。中文口令建议靠 crunch 手工构造 |

## 9. 防御视角（蓝队）

**CeWL 的存在本身就是一条情报**：攻击者会从你的公开内容里找素材。所以蓝队的对策分两半：

### 9.1 减少「可被收集的素材」

| 泄露点 | 缓解 |
| --- | --- |
| 网页上的产品名/内部项目名/标语 | 公开站点只保留对外品牌词；内部项目名不上公网 |
| 文档元数据里的作者与公司 | **发布前清除元数据**（Office：文件→信息→检查文档→删除文档属性和个人信息；PDF：`exiftool -all= file.pdf`） |
| `mailto:` 邮箱暴露内部命名规则 | 使用统一对外邮箱（如 `info@`），内部邮箱名规则不对外可推断 |
| 目录索引、备份文件、`.git` 泄露 | 关闭目录列表；扫描并清理备份与版本库 |

**自动化清理元数据的示例**（在发布流程中使用）：

```bash
# 对一批待发布文件清除元数据
exiftool -all= -overwrite_original ./public-docs/*
```

### 9.2 让收集到的词无法用于爆破

| 攻击者的做法 | 对策 |
| --- | --- |
| 用词表 + 数字后缀 | 口令策略禁止「词典词 + 数字」这类结构；强制最小熵 |
| 用邮箱格式推断用户名 | 用户名与邮箱解耦；登录失败响应统一（不泄露用户是否存在） |
| 用高频词优先爆破 | **降低在线尝试速率**：失败计数 + 锁定 + MFA + 验证码 |
| 用词表做 WPA 破解 | WPA3-SAE；强随机 PSK |

### 9.3 检测

| 行为 | 检测信号 |
| --- | --- |
| CeWL 爬取 | 单源 IP 在短时间内拉取大量页面 + **顺序模式明显**（按链接深度推进）；UA 常为默认或自定义；可能不加载图片/CSS |
| 爬取伴随的 404 洪泛 | 路径字典式请求，`--allowed` 不匹配时的大量 404 |
| 后续的登录爆破 | 见 [hydra](hydra.md) / [medusa](medusa.md) 的蓝队章节 |

**WAF 规则思路**：

```text
if requests_per_minute(src_ip) > 100 and distinct_paths(src_ip, 5m) > 50
   and user_agent matches "CeWL"
then rate-limit or block, log as recon
```

**蓝队核心结论**：

> 你无法阻止攻击者爬取公开内容，但你可以（1）**不把内部词汇放到公网**，（2）**清除文件元数据**，（3）**让即使拿到词表也无法有效爆破**（MFA + 慢哈希 + 锁定策略）。

## 10. 参考

- 官方仓库：<https://github.com/digininja/CeWL>
- Kali 工具页：<https://www.kali.org/tools/cewl/>
- 本机手册：`man cewl`、`cewl -h`、`man fab-cewl`
- 相关：[crunch](crunch.md)、[wordlists](wordlists.md)、[hashcat](hashcat.md)、[hydra](hydra.md)

## ⚠️ 法律与伦理

- **爬取**本身可能违反目标网站的《服务条款》，并可能触犯《中华人民共和国刑法》第二百八十五条第二款「非法获取计算机信息系统数据罪」；
- **将爬取结果用于口令破解**，则进一步落入「非法侵入计算机信息系统罪」或「非法获取计算机信息系统数据罪」；
- 若站点明确禁止自动化访问（`robots.txt`、TLS 证书、登录墙），绕过这些限制可能构成《网络安全法》第二十七条禁止的行为。

**本教程仅适用于**：爬取你自己拥有的站点、有书面授权的渗透测试目标、自建靶场。**绝不**对任何未授权站点执行本文命令——即使在判断某站点「是否可爬」时，也已经越线。
