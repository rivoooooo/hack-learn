# opentaxii

> TAXII server implementation from EclecticIQ This package contains a robust Python implementation of TAXII Services that delivers rich feature set and friendly pythonic API built on top of well designed application. OpenTAXII is guaranteed …

> **功能分类**：通用工具 ｜ **Kali 包**：`opentaxii` ｜ **官方文档**：<https://www.kali.org/tools/opentaxii/>

## 1. 安装

```bash
sudo apt update
sudo apt install opentaxii
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.9.3 |
| 架构 | all |
| 可执行命令 | `opentaxii`、`opentaxii-add-api-root`、`opentaxii-add-collection`、`opentaxii-create-account`、`opentaxii-delete-blocks`、`opentaxii-job-cleanup`、`opentaxii-run-dev`、`opentaxii-sync-data`、`opentaxii-update-account`、`opentaxii-doc` |
| 依赖 | `python3`、`python3-blinker`、`python3-flask`、`python3-jwt`、`python3-libtaxii`、`python3-lxml`、`python3-marshmallow`、`python3-mypy-extensions`、`python3-pytz`、`python3-six`、`python3-sqlalchemy`、`python3-stix2` 等 |
| 安装体积 | 347 KB |
| 官网 | <https://github.com/eclecticiq/OpenTAXII> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/opentaxii> |
| 包追踪 | <https://pkg.kali.org/pkg/opentaxii> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
opentaxii -h          # 查看用法
man opentaxii         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 10 个可执行命令，下面是官方页面内嵌的帮助原文。

### `opentaxii-add-api-root`

官方给出的调用示例：`opentaxii-add-api-root -h`

```text
root@kali:~# opentaxii-add-api-root -h
usage: opentaxii-add-api-root [-h] -t TITLE [-d DESCRIPTION] [--default]
Add a new taxii2 ApiRoot object.
options:
  -h, --help            show this help message and exit
  -t, --title TITLE     Title of the api root
  -d, --description DESCRIPTION
                        Description of the api root (default: None)
  --default             Set as default api root (default: False)
```

### `opentaxii-add-collection`

官方给出的调用示例：`opentaxii-add-collection -h`

```text
root@kali:~# opentaxii-add-collection -h
usage: opentaxii-add-collection [-h] -r {} -t TITLE [-d DESCRIPTION]
                                [-a ALIAS] [--public] [--public-write]
Add a new taxii2 Collection object.
options:
  -h, --help            show this help message and exit
  -r, --rootid {}       Api root id of the collection
  -t, --title TITLE     Title of the collection
  -d, --description DESCRIPTION
                        Description of the collection (default: None)
  -a, --alias ALIAS     alias of the collection (default: None)
  --public              allow public read access (default: False)
  --public-write        allow public write access (default: False)
```

### `opentaxii-create-account`

官方给出的调用示例：`opentaxii-create-account -h`

```text
root@kali:~# opentaxii-create-account -h
usage: opentaxii-create-account [-h] -u USERNAME -p PASSWORD [-a]
Create Account via OpenTAXII Auth API
options:
  -h, --help            show this help message and exit
  -u, --username USERNAME
  -p, --password PASSWORD
  -a, --admin           grant admin access (default: False)
```

### `opentaxii-delete-blocks`

官方给出的调用示例：`opentaxii-delete-blocks -h`

```text
root@kali:~# opentaxii-delete-blocks -h
usage: opentaxii-delete-blocks [-h] -c COLLECTION [-m] --begin BEGIN
                               [--end END]
Delete content blocks from specified collections with timestamp labels
matching defined time window
options:
  -h, --help            show this help message and exit
  -c, --collection COLLECTION
                        Collection to remove content blocks from
  -m, --with-messages   delete inbox messages associated with deleted content
                        blocks (default: False)
  --begin BEGIN         exclusive beginning of time window as ISO8601
                        formatted date
  --end END             inclusive ending of time window as ISO8601 formatted
                        date (default: None)
```

### `opentaxii-job-cleanup`

官方给出的调用示例：`opentaxii-job-cleanup -h`

```text
root@kali:~# opentaxii-job-cleanup -h
No job to remove
```

### `opentaxii-run-dev`

官方给出的调用示例：`opentaxii-run-dev -h`

```text
root@kali:~# opentaxii-run-dev -h
 * Serving Flask app 'opentaxii.middleware'
 * Debug mode: on
```

### `opentaxii-sync-data`

官方给出的调用示例：`opentaxii-sync-data -h`

```text
root@kali:~# opentaxii-sync-data -h
usage: opentaxii-sync-data [-h] [-f] config
Create services/collections/accounts
positional arguments:
  config              YAML file with data configuration
options:
  -h, --help          show this help message and exit
  -f, --force-delete  force deletion of collections and their content blocks
                      if collection is not defined in configuration file
                      (default: False)
```

### `opentaxii-update-account`

官方给出的调用示例：`opentaxii-update-account -h`

```text
root@kali:~# opentaxii-update-account -h
usage: opentaxii-update-account [-h] -u USERNAME -f {password,admin} -v VALUE
Update Account via OpenTAXII Auth API
options:
  -h, --help            show this help message and exit
  -u, --username USERNAME
  -f, --field {password,admin}
  -v, --value VALUE
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install opentaxii`，再执行 `opentaxii --version` 2>/dev/null || `opentaxii -V`
- [ ] **2.** **读官方帮助** —— `opentaxii -h`，需要细节时 `man opentaxii`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `opentaxii -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/opentaxii/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/opentaxii/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/opentaxii/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
