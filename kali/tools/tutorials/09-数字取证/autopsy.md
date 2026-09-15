# Autopsy（Sleuth Kit 图形化取证界面）

> **一句话**：给 The Sleuth Kit 的命令行能力套上一个浏览器界面——建案件、加镜像、点几下就能列文件、搜关键字、恢复被删文件、看时间线。
> **分类**：数字取证 / 文件系统分析（图形界面）｜ **Kali 包**：`autopsy`（命令 `autopsy`，**Kali 打包的是经典版「Autopsy Forensic Browser」，浏览器访问，默认端口 9999**）｜ **官方文档**：<https://www.sleuthkit.org/autopsy/> ｜ 命令行引擎：[`sleuthkit.md`](sleuthkit.md)

---

## 1. 它解决什么问题

[`sleuthkit.md`](sleuthkit.md) 里的命令很强，但要记住 `mmls` 的偏移、`fls -r -m` 的参数、`mactime` 的时区……**对不常做取证的人门槛偏高**。

Autopsy 解决的是「**降低使用门槛 + 组织案件材料**」：

| 你要做的事 | TSK 命令行 | Autopsy 图形界面 |
|------------|------------|------------------|
| 建案件、记录案件信息 | 无（自己建目录） | `New Case`，填写案件号/调查员 |
| 加镜像（含分区偏移） | `mmls` 查偏移 → 手工 `-o` | 加镜像时**自动列出分区让你选** |
| 列文件 | `fls -r -l` | 点目录树 |
| 提取文件 | `icat <inode>` | 点文件名 → `Export` |
| 恢复已删除 | `fls -d` + `icat` | 删除文件有**独立视图**（红色标记） |
| 关键字搜索 | 手工串联 TSK + grep | `Keyword Search` 界面 |
| 时间线 | `fls -m` + `mactime -b` | `Timeline` 界面，按时间浏览 |
| 文件类型筛选 | `file` 逐个判断 | `File Type` 按类别浏览 |

对比同类：

| 工具 | 平台 | 说明 |
|------|------|------|
| **Kali 的 `autopsy` 包** | Linux，**Web 界面**（经典版 2.x / Autopsy Forensic Browser） | 轻量、纯 Perl + TSK；功能**有限**（无现代 ingest 模块体系） |
| **Autopsy 4.x**（现代版） | Windows（也有 Linux 安装包） | 真正的主流版本：多线程 ingest 模块、图像/视频缩略图、报告导出，**不通过 Kali 的 `autopsy` 包提供** |
| **TSK 命令行** | 跨平台 | 精确、可脚本化，**是上面两者的底层引擎** |
| **`bulk-extractor`/`foremost`/`scalpel`** | 跨平台 | 不解析文件系统，作为补充，见 [`bulk-extractor.md`](bulk-extractor.md)、[`foremost.md`](foremost.md) |

> **务实建议**：
> - **脚本化/自动化/可复现** → 用 TSK 命令行（[`sleuthkit.md`](sleuthkit.md)）；
> - **一次性浏览、给非技术人员演示** → 用 Kali 的 Autopsy（本文）；
> - **需要完整现代功能**（缩略图、丰富报告、模块化 ingest）→ 装 **Autopsy 4.x**（官方站点下载，注意其许可与平台要求）。

---

## 2. 工作原理

```
① autopsy（Perl 脚本）启动一个内嵌的 HTTP 服务（默认 9999）
        │
② 浏览器访问 http://<host>:9999/autopsy
        │
③ 案件（Case）
     └─ 证据柜（Evidence Locker，默认 /var/lib/autopsy/）
          └─ 主机（Host）← 一台设备一个 Host
               └─ 镜像（Image）← 一个 Host 可加多个镜像/分区
                    └─ 分析视图：
                         File Analysis（基于 fls/icat）
                         Keyword Search（基于 strings/grep/索引）
                         File Type（基于 file/magic 分类）
                         Timeline（基于 fls -m + mactime）
                         Hash Databases（NSRL / 自定义哈希库）
                         Image Details（基于 mmls/fsstat）
                         Deleted Files（fls -d）
        │
④ 所有分析操作最终都调用 TSK 命令 → 结果渲染成 HTML
```

关键设计：

- **Evidence Locker（证据柜）**：所有案件数据的根目录，**新增证据不能写入既往案件**（保持历史不可变）。
- **Case → Host → Image 三层模型**：一个案件可以有多个设备（Host），每个设备可以有多个镜像（Image），每个镜像可以是整盘或单个分区。
- **镜像添加方式**：本地磁盘/分区、镜像文件（raw/dd）、**分区偏移**（可自动识别分区）。
- **只读原则**：Autopsy 只读取镜像，不写回原始证据。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install autopsy
command -v autopsy
```

```console
root@kali:~# autopsy -h
Invalid flag: -h


usage: /usr/bin/autopsy [-c] [-C] [-d evid_locker] [-i device filesystem mnt] [-p port] [remoteaddr]
  -c: force a cookie in the URL
  -C: force NO cookie in the URL
  -d dir: specify the evidence locker directory
  -i device filesystem mnt: Specify info for live analysis
  -p port: specify the server port (default: 9999)
  remoteaddr: specify the host with the browser (default: localhost)
```

> **注意**：`autopsy -h` 会打印 `Invalid flag: -h`——它**没有 `-h` 参数**，用法直接打在错误信息里（上面的输出就是用 `-h` 触发的）。

启动：

```bash
# 默认端口 9999，证据柜 /var/lib/autopsy
sudo autopsy
```

```console
============================================================================
Autopsy Forensic Browser
http://www.sleuthkit.org/autopsy/
ver 2.24

Evidence Locker: /var/lib/autopsy
Start Time: Sat Sep 15 10:00:00 2024
Remote Host: localhost
Local Port: 9999
Open an HTML browser on the remote host and paste this URL in it:

  http://localhost:9999/autopsy

Keep this process running and use <ctrl-c> to exit
```

浏览器打开 `http://localhost:9999/autopsy`（远程使用则把浏览器指向 Kali 的 IP，并注意 `remoteaddr` 参数与防火墙）。

指定证据柜位置（推荐放在有空间的数据盘）：

```bash
sudo mkdir -p /evidence/autopsy
sudo autopsy -d /evidence/autopsy -p 9999
```

---

## 4. 核心参数详解

### 4.1 命令行参数（真实参数，来自 `autopsy -h`）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-p <port>` | HTTP 服务端口 | 默认 **9999**；冲突时改（如 `-p 8888`） |
| `-d <dir>` | **证据柜目录** | 放到空间足够的数据盘（镜像动辄数十 GB） |
| `-c` | 强制在 URL 中使用 Cookie | 多用户/多会话时避免串会话 |
| `-C` | 强制**不**使用 Cookie | 老浏览器兼容 |
| `-i <device> <filesystem> <mnt>` | **实时分析（live analysis）**：把已挂载设备当作证据 | 应急响应中分析当前系统（**会改变系统状态，取证严谨性下降，慎用**） |
| `<remoteaddr>` | 允许访问的主机名/IP | 默认 `localhost`；远程访问需显式指定 |
| `-h` | **不存在**（会报 Invalid flag 并打印用法） | 用无参数运行或直接看上面的用法行 |

### 4.2 界面核心操作（等价于哪些 TSK 命令）

| 界面功能 | 作用 | 底层等价命令 |
|----------|------|--------------|
| `New Case` | 建案件（案件号、调查员、描述） | 建目录结构 |
| `Add Host` | 添加设备 | —— |
| `Add Image` | 添加镜像（本地磁盘/镜像文件；**可选分区偏移**） | `mmls` 查偏移 |
| `Image Details` | 镜像与分区信息 | `mmls`、`fsstat`、`img_stat` |
| `File Analysis` | 目录树浏览、查看元数据、导出文件 | `fls`、`istat`、`icat` |
| `Deleted Files`（视图内标记） | 已删除条目 | `fls -d` |
| `File Type` | 按类型（图片/文档/可执行…）浏览 | `file` + `fls` |
| `Keyword Search` | 关键字搜索（可建索引） | `grep`/`strings` 遍历 |
| `Timeline` | 按时间浏览全部文件活动 | `fls -m` + `mactime` |
| `Hash Databases` | 与 NSRL 等哈希库比对（筛掉已知文件 / 标记已知恶意文件） | `hfind` |
| `Notes` / `Case Journal` | 记录调查笔记 | —— |
| `Report`（有限） | 导出 HTML 报告 | —— |

> **时区提醒**：Autopsy 的时间线显示依赖服务端时区设置。**在报告里必须写明时区基准**（与 [`sleuthkit.md`](sleuthkit.md) 的 `-z` 要求一致）。

---

## 5. 实战演练

> **环境声明**：全部使用**自建实验镜像**（生成方法见 [`dcfldd.md` 场景 1](dcfldd.md#场景-1造一个作案现场先有可练的镜像)）或**公开发布的取证样本**（NIST CFReDS）。**禁止**对未经授权的设备做镜像获取或分析。
> 下面用 `/evidence/disk.img`（含一个已删除的 `secret.txt`）贯穿演示。

### 场景 1：启动 + 建案件 + 加镜像（把界面跑起来）

```bash
# ① 准备证据柜与镜像
sudo mkdir -p /evidence/autopsy
ls -lh /evidence/disk.img
```

```console
-rw-r--r-- 1 root root 256M Sep 15 09:30 /evidence/disk.img
```

```bash
# ② 启动 Autopsy
sudo autopsy -d /evidence/autopsy -p 9999
```

```console
Autopsy Forensic Browser ver 2.24
Evidence Locker: /evidence/autopsy
Local Port: 9999
  http://localhost:9999/autopsy
```

```bash
# ③ 确认服务在监听（另开一个终端）
ss -lntp | grep 9999
```

```console
LISTEN 0  128  127.0.0.1:9999  0.0.0.0:*  users:(("perl",pid=20431,fd=3))
```

浏览器打开 `http://localhost:9999/autopsy`，按顺序操作：

```
[CASE GALLERY] → New Case
    Case Name:  lab-2024-01
    Description: 磁盘取证练习（自建镜像）
    Investigator: analyst01
        ↓
[CASE] → Add Host
    Host Name:  lab-vm-01
    Description: 自建实验虚拟机
        ↓
[HOST] → Add Image
    Image Type:  Image File
    Location:    /evidence/disk.img
    ↓（Autopsy 会列出分区）
    选择：Linux filesystem (Start: 2048 sectors)
        ↓
[IMAGE] → 出现分析菜单
```

**解读**：Autopsy 会**自动读分区表并列出分区**，让你选一个——这一步在命令行里对应「先 `mmls` 看 `Start`，再每次加 `-o 2048`」。**这就是界面的价值：少记参数、少犯错**。

> **注意**：`Add Image` 里不要选错分区（例如把整盘当分区）。若选错，会看到「无法识别文件系统」。

### 场景 2：按「取证问题清单」走一遍界面

进入 `File Analysis` 后，按下面的**问题顺序**操作（这是取证分析的通用顺序，比乱点有效得多）：

**问题 1：这台机器上原有什么文件？**

```
File Analysis → 目录树
    根目录 /
      ├─ lost+found
      ├─ secret.txt        （正常文件）
      ├─ photo.jpg
      └─ report.pdf
```

对应命令：`fls -o 2048 /evidence/disk.img`。

**问题 2：有没有被删除的文件？**

```
File Analysis → 显示设置中勾选 Show Deleted Files
     或者：Image Details → Deleted Files 视图
```

```console
deleted_secret.txt   (deleted)   inode 15
```

对应命令：`fls -d -r -o 2048`。

**问题 3：这个文件是什么时候创建/删除的？**

点击 `deleted_secret.txt` → 查看元数据：

```console
Name: deleted_secret.txt
Inode: 15
Mode: rrw-r--r--
Size: 128
UID/GID: 0/0
Accessed: 2024-09-14 10:13:00
File Modified: 2024-09-14 10:13:00
Inode Modified: 2024-09-14 10:13:05
Deleted: 2024-09-14 10:13:05
```

对应命令：`istat -o 2048 /evidence/disk.img 15`。**`Deleted:` 时间是本次分析最重要的证据。**

**问题 4：能把内容拿出来吗？**

```
选中文件 → Export / Save As → 选择本地目录
```

```bash
# 导出的文件会出现在你指定的目录
ls -l /evidence/autopsy/lab-2024-01/lab-vm-01/.../
cat <导出的文件>
```

```console
employee_id=1024
salary=185000
```

对应命令：`icat -o 2048 /evidence/disk.img 15 > out.txt`。

**问题 5：全盘有没有「工资」「密码」之类的关键字？**

```
Keyword Search → 输入关键字 → 选择镜像 → Search
```

```console
Keyword 'salary' found in:
  /deleted_secret.txt (inode 15)   offset 14
```

对应命令：`blkls -A -o 2048 image | strings | grep -i salary`。

> **注意**：关键字搜索会**遍历未分配空间**（否则搜不到已删除内容），因此**耗时较长**——大镜像上先做定向搜索（限定文件类型/目录）。

**问题 6：整体时间线长什么样？**

```
Timeline → 选择日期/时间段 → 按 时间 排序
```

```console
2024-09-14 10:12:03  m...  /secret.txt
2024-09-14 10:12:41  m...  /photo.jpg
2024-09-14 10:13:00  m...  /deleted_secret.txt
2024-09-14 10:13:05  .a.b  /deleted_secret.txt (deleted)
```

对应命令：`fls -r -m / -o 2048 image > bodyfile` + `mactime -b bodyfile`。

**把上面 6 个问题的答案写进报告，就是一份完整的取证分析结论。**

### 场景 3：与命令行交叉验证 + 哈希库过滤

**为什么必须交叉验证**：GUI 会隐藏细节（例如时间字段的顺序、`-f` 未指定时的自动探测结果）。**报告要经得起复核**。

```bash
# ① GUI 里看到的删除文件，命令行复核一遍
fls -d -r -l -o 2048 /evidence/disk.img | grep -i deleted
```

```console
r/r * 15:	deleted_secret.txt	2024-09-14 10:13:00 (CST)	...	128	0	0
```

```bash
# ② GUI 导出的文件与 icat 的内容比对
icat -o 2048 /evidence/disk.img 15 > /tmp/cli_extract.txt
md5sum /tmp/cli_extract.txt "<GUI 导出的文件>"
```

**解读**：两者哈希一致 → 「GUI 与命令行两条独立路径得到同一结果」，**这在报告里是可信度加分项**。

**Hash Databases（筛掉已知无害文件）**：

```
Hash Databases → Add Database
    NSRL（官方哈希库，需自行准备）
        ↓
File Analysis → 标记为 "Known Good" 的文件被过滤/置灰
```

对应命令：`hfind -i nsrl-md5 <hashdb> <hashfile>`。**作用**：一份 500GB 的镜像里可能有 90% 是操作系统自带文件，用哈希库过滤后，**你只需要看剩下的 10%**。

```bash
# ③ 与雕刻工具互补：GUI 里「找不到」的文件，去未分配空间雕
blkls -A -o 2048 /evidence/disk.img > /evidence/unallocated.bin
foremost -t jpg,pdf,doc,txt -i /evidence/unallocated.bin -o /evidence/carved
ls /evidence/carved/*/
```

```console
/evidence/carved/jpg/  /evidence/carved/pdf/  /evidence/carved/txt/  audit.txt
```

见 [`foremost.md`](foremost.md)、[`scalpel.md`](scalpel.md)、[`bulk-extractor.md`](bulk-extractor.md)。

**收尾（重要）**：

```bash
# 停止 Autopsy
# 在启动它的终端按 Ctrl-C

# 记录你的操作（保管链）
cat >> /evidence/chain_of_custody.txt <<'EOF'
2024-09-15 09:30  获取镜像 /evidence/disk.img（dcfldd, sha256 见 disk.sha256）
2024-09-15 10:00  启动 Autopsy（-d /evidence/autopsy -p 9999），建案件 lab-2024-01
2024-09-15 10:35  导出文件 3 个至 /evidence/export/
2024-09-15 10:50  生成时间线并交叉验证（fls/mactime）
2024-09-15 11:00  停止 Autopsy
EOF
```

---

## 6. 输出解读

| 界面元素 | 含义 | 报告里怎么写 |
|----------|------|--------------|
| `(deleted)` 标记 | 该条目已删除 | 「文件 X 于 <时间> 被删除」 |
| `Deleted: <time>` | ext4 记录的删除时间 | 可作为精确的「删除动作时间」 |
| `Allocated` / `Not Allocated` | inode 是否仍被使用 | `Not Allocated` + `links=0` = 已删除 |
| `Size` vs 导出文件大小 | 逻辑大小 vs 实际取回 | 不一致 → 数据被覆盖/截断，需说明 |
| MAC 四个时间 | 修改/访问/变更/创建 | **必须写清时区**，并区分「动作时间」与「元数据变更时间」 |
| `File Type` 分类 | 按真实类型（`file` 判定） | 可发现「扩展名与真实类型不符」这种反取证手法 |
| `Keyword Search` 命中位置 | 文件名 + inode + 偏移 | 偏移可用于在 `blkcat` 中定位原始块 |
| `Known Good` 标记 | 命中 NSRL 哈希库 | 用于说明「已排除操作系统自带文件」 |
| Timeline 里的空白窗口 | 某段时间无活动 | 可能是**系统关机**，也可能是**日志/痕迹被清理**——需交叉验证 |
| `Timeline` 出现未来时间 | 时钟被篡改 | 重要发现：反取证迹象 |

**成功判据**：GUI 结论能在命令行上复现（`fls`/`istat`/`icat` 结果一致），且时间线在时区明确的前提下自洽。

---

## 7. 与其他工具配合

```
镜像（dcfldd / ddrescue / E01）
        │
        ├─► autopsy（GUI：案件管理 + 导航 + 初筛）   ← 本文
        │        └─ 复杂/批量/需复现的部分 → 回到命令行
        │
        ├─► sleuthkit（命令行：精确解析、脚本化、可复现）   sleuthkit.md
        │        ├─ mmls / fsstat        → 结构
        │        ├─ fls / istat / icat    → 文件与元数据
        │        └─ fls -m + mactime      → 时间线
        │
        ├─► blkls -A → foremost / scalpel（雕刻兜底）        foremost.md / scalpel.md
        ├─► bulk-extractor（不依赖文件系统的特征与凭据搜索）  bulk-extractor.md
        ├─► binwalk（固件/嵌入数据）                        binwalk.md
        └─► exiftool（恢复出的图片/文档元数据）              exiftool.md
                                │
                                ▼
                     报告：时间线 + 证据清单 + 哈希校验值
```

- 引擎与命令行细节：[`sleuthkit.md`](sleuthkit.md)
- 镜像获取：[`dcfldd.md`](dcfldd.md)
- 未分配空间与特征：[`bulk-extractor.md`](bulk-extractor.md)
- 雕刻：[`foremost.md`](foremost.md)、[`scalpel.md`](scalpel.md)
- 元数据：[`exiftool.md`](exiftool.md)、固件：[`binwalk.md`](binwalk.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `Invalid flag: -h` | **Autopsy 没有 `-h`** | 无参数运行，或看错误信息里的 usage |
| 端口 9999 被占用 | 已有实例在跑 | `ss -lntp \| grep 9999`；改 `-p 8888` 或杀掉旧进程 |
| 浏览器打不开（远程） | 默认只绑 `localhost` | 用 `autopsy <你的IP>` 指定 remoteaddr，并放行防火墙（**仅内网**） |
| `Add Image` 后报「无法识别文件系统」 | 选错了分区（选了整盘或元数据区） | 重新添加，选择 `Start` 为分区起始的那个 |
| 看不到已删除文件 | 界面未开启显示删除项 | 在视图里勾选 `Show Deleted Files`，或用 `Deleted Files` 视图 |
| 关键字搜索搜不到已删除内容 | 只搜了已分配区域 | 确保搜索范围包含未分配空间；或离线用 `blkcat` 定向验证 |
| 时间线时间不对 | **时区**问题 | 确认服务端时区并在报告写明；命令行用 `-z` 明确指定 |
| 分析大镜像极慢 | GUI 串行处理 + 关键字搜索全盘 | 先做定向分析；重活交给命令行脚本（可并行） |
| 无法加载镜像 | 格式不支持（E01/AFF） | Kali 经典版对 E01 支持有限；用 `ewfmount`/`libewf` 转换或改用 TSK 的 `-i ewf` |
| 界面报 Perl 错误 | 缺失 Perl 模块/权限 | 装 `libhtml-*` 类依赖（`apt -f install`）；确认用 `sudo` 启动 |
| 证据柜写满 | 镜像与恢复文件堆在同一分区 | `-d` 指到空间足够的盘；分析结果目录单独规划 |
| 恢复出的文件是空的 | 数据块被覆盖 | 转向 `blkls -A` 导出未分配空间 + `foremost`/`scalpel` 雕刻 |
| 想让报告更完整 | 经典版报告能力弱 | 用命令行生成时间线 CSV/HTML；或改用 Autopsy 4.x |

---

## 9. 防御视角（蓝队 / 应急响应）

Autopsy 在蓝队的主要用途是**事件响应取证的「组织层」**：把镜像、案件、笔记、结论组织在一起，便于复核与交付。

| 场景 | Autopsy 的用法 | 关键动作 |
|------|----------------|----------|
| 入侵事件取证 | 建案件 → 加镜像 → `File Analysis` 找异常文件 | 与发布清单/基线比对 |
| 找 webshell / 攻击工具 | `File Type` 筛可执行/脚本 + Timeline 看新增时间 | 结合 Web 日志时间对齐 |
| 找被删除的攻击工具 | `Deleted Files` 视图 + 导出 | 攻击者删除的 EXP/隧道工具常可恢复 |
| 验证日志被清理 | 查看 `/var/log` 大小与修改时间 | size 变小/条目缺失 = 反取证证据 |
| 数据外带取证 | `Keyword Search` 找压缩包/敏感关键字 | 与 DLP/网络日志交叉验证 |
| 员工离职/合规调查 | 定向搜索关键字（**须有制度依据与授权**） | 仅限授权范围，避免浏览无关隐私 |
| 培训与演练 | 用自建镜像做「案件」，让团队成员独立复现结论 | 强化流程与纪律 |

**蓝队实操建议**：

1. **把「案件目录规范」定下来**（案件号/镜像/导出/时间线/报告/保管链文档），Autopsy 的证据柜就是这套规范的一部分；
2. **GUI 初筛 + 命令行固化结论**：任何写进报告的结论，都能用一条 `fls`/`istat`/`icat` 命令复现；
3. **记录操作时间线**（谁在什么时候做了什么），这本身就是保管链的核心；
4. **不要在分析的机器上处理与案件无关的数据**，分析机建议专用并加密磁盘；
5. **优先做时间线**：先搞清楚「什么时候发生了什么」，再深挖「怎么发生的」。

---

## 10. 参考

- Autopsy 官网：<https://www.sleuthkit.org/autopsy/>
- The Sleuth Kit 官网（Autopsy 的底层引擎）：<https://www.sleuthkit.org/sleuthkit/>
- Kali 工具页：<https://www.kali.org/tools/autopsy/>
- TSK Wiki（命令行细节，报告复核必读）：<https://wiki.sleuthkit.org/>
- NIST CFReDS 公开取证镜像：<https://cfreds.nist.gov/>
- 本地命令：`autopsy`（无参数查看用法）、`autopsy -d <dir> -p <port>`

## ⚠️ 法律与伦理

Autopsy 让**浏览他人磁盘内容变得极其容易**——这正是它的风险所在。未经授权获取或查看他人设备数据，可能触犯：

- 《刑法》第 285 条（非法获取计算机信息系统数据）、第 253 条之一（侵犯公民个人信息罪）；
- 《网络安全法》《数据安全法》《个人信息保护法》（企业内部调查同样受约束）。

**必须遵守**：

1. 有**设备所有者或司法机关的书面授权**；企业内部调查需有制度依据并履行告知程序；
2. **最小必要**：只分析与事件相关的范围，避免浏览与案件无关的私密内容；
3. **只读分析**：绝不修改原始镜像；工作副本单独存放；
4. **访问留痕**：记录谁在什么时间访问了哪些内容（分析过程也要有保管链）；
5. **加密存储 + 限时销毁**：结案后按约定安全销毁副本；
6. **报告脱敏**：不包含真实个人信息、凭据与私密内容。

本教程请仅在**自建实验镜像**或 **NIST CFReDS 公开样本**上练习。
