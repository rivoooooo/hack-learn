# python-faraday

> root@kali:~# python-faraday -h ┏━(Message from Kali developers) ┃ ┃ Please wait for the faraday service to start ┃ ..........

> **功能分类**：报告与记录 ｜ **Kali 包**：`python-faraday` ｜ **官方文档**：<https://www.kali.org/tools/python-faraday/>

## 1. 安装

```bash
sudo apt update
sudo apt install python-faraday
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.22.0 |
| 架构 | all |
| 可执行命令 | `faraday`、`faraday-manage`、`faraday-server`、`faraday-start`、`faraday-stop`、`faraday-worker`、`faraday-worker-gevent`、`python-faraday` |
| 依赖 | `faraday` |
| 安装体积 | 32 KB |
| 官网 | <https://faradaysec.com> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/python-faraday> |
| 包追踪 | <https://pkg.kali.org/pkg/python-faraday> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
Faraday is a GUI application that consists of a ZSH terminal and a sidebar with details about your workspaces and hosts.
When Faraday supports the command you are running, it will automatically detect it and import the results. In the example below, the original nmap command that was entered was nmap -A 192.168.0.7, which Faraday converted on the fly.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 8 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

官方给出的调用示例：`man faraday`

```text
root@kali:~# man faraday
FARADAY(1)                       User Commands                       FARADAY(1)
NAME
     Faraday - Kali script to start and stop faraday-server and faraday-client
SYNOPSIS
     faraday [OPTIONS for faraday-client]
DESCRIPTION
     Kali Faraday's launcher
     It starts the faraday server with starting the Kali python-faraday service
     and the first time it initializes the PostgreSQL database.  The first time
     it  asks  you a new password for the username "faraday" Then it starts the
     faraday client.
     The client and server is closed when the client  windows  is  closed.   It
     also stops the service.
OPTIONS
     See faraday-client manpage or faraday-client -h
SEE ALSO
     /usr/share/doc/python-faraday/README.Debian
Faraday                            June 2019                         FARADAY(1)
```

### `faraday-manage`

官方给出的调用示例：`faraday-manage -h`

```text
root@kali:~# faraday-manage -h
Usage: faraday-manage [OPTIONS] COMMAND [ARGS]...
Options:
  -h, --help  Show this message and exit.
Commands:
  add-custom-field                Custom field wizard
  change-password                 Changes the password of a user
  create-superuser                Create ADMIN user for Faraday application
  create-tables                   Create database tables.
  database-schema                 Create a PNG image with Faraday model...
  delete-custom-field             Custom field delete wizard
  generate-nginx-config           Generate nginx config
  import-vulnerability-templates  Import Vulnerability templates
  ingest                          Import vulnerabilities from one or all...
  initdb                          Create Faraday DB in Postgresql, also...
  list-plugins                    List Available Plugins
  migrate                         Migrates database schema.
  move-references                 Move references from deprecated model...
  openapi-swagger                 Creates Faraday Swagger config file
  rename-user                     Change username
  settings                        Manage settings
  show-urls                       Show all URLs in Faraday Server API
  sql-shell                       Open a SQL Shell connected to...
  sync-hosts-stats                Synchronize vulnerability severity...
```

### `faraday-server`

官方给出的调用示例：`faraday-server -h`

```text
root@kali:~# faraday-server -h
usage: faraday-server [-h] [--debug] [--update_stats] [--port PORT]
                      [--bind_address BIND_ADDRESS] [-v] [--with-workers]
                      [--with-workers-gevent] [--workers-queue WORKERS_QUEUE]
                      [--workers-concurrency WORKERS_CONCURRENCY]
                      [--workers-loglevel WORKERS_LOGLEVEL]
options:
  -h, --help            show this help message and exit
  --debug               run Faraday Server in debug mode
  --update_stats        Updates host and workspace stats of failed commands
  --port PORT           Overides server.ini port configuration
  --bind_address BIND_ADDRESS
                        Overides server.ini bind_address configuration
  -v, --version         show program's version number and exit
  --with-workers        Starts a celery workers
  --with-workers-gevent
                        Run workers in gevent mode
  --workers-queue WORKERS_QUEUE
                        Celery queue
  --workers-concurrency WORKERS_CONCURRENCY
                        Celery concurrency
  --workers-loglevel WORKERS_LOGLEVEL
                        Celery loglevel
```

### `faraday-start`

官方给出的调用示例：`faraday-start -h`

```text
root@kali:~# faraday-start -h
┏━(Message from Kali developers)
┃
┃ Please wait for the faraday service to start
┃ ..........
```

### `faraday-stop`

官方给出的调用示例：`faraday-stop -h`

```text
root@kali:~# faraday-stop -h
┏━(Message from Kali developers)
┃
┃ Service status:
┃   * faraday.service - Faraday Server
┃        Loaded: loaded (/usr/lib/systemd/system/faraday.service; 5:185mdisabled; preset: 5:185mdisabled)
┃        Active: inactive (dead)
┃          Docs: file:/usr/share/doc/faraday/README.Debian
┃
┃   Jun 17 21:03:39 kali faraday-server[15272]: [2026-06-17 21:03:39,451] INFO in app: Checking celery configuration ...
┃   Jun 17 21:03:39 kali faraday-server[15272]: 2026-06-17T21:03:39+0000 - faraday.server.app - INFO {MainThread} [pid:15272] [app.py:657 - register_extensions()]  Checking celery configuration ...
┃   Jun 17 21:03:39 kali faraday-server[15272]: 2026-06-17T21:03:39+0000 - faraday.server.threads.crontab - INFO {CrontabThread} [pid:15272] [crontab.py:53 - run()]  Crontab Thread [Start]
┃   Jun 17 21:03:39 kali faraday-server[15272]: 2026-06-17T21:03:39+0000 - celery.backends.redis - ERROR {MainThread} [pid:15272] [redis.py:435 - on_connection_error()]  Connection to Redis lost: Retry (0/20) now.
┃   Jun 17 21:03:39 kali faraday-server[15272]: 2026-06-17T21:03:39+0000 - celery.backends.redis - ERROR {MainThread} [pid:15272] [redis.py:435 - on_connection_error()]  Connection to Redis lost: Retry (1/20) in 1.00 second.
┃   Jun 17 21:03:40 kali faraday-server[15272]: 2026-06-17T21:03:40+0000 - celery.backends.redis - ERROR {MainThread} [pid:15272] [redis.py:435 - on_connection_error()]  Connection to Redis lost: Retry (2/20) in 1.00 second.
┃   Jun 17 21:03:41 kali faraday-server[15272]: 2026-06-17T21:03:41+0000 - celery.backends.redis - ERROR {MainThread} [pid:15272] [redis.py:435 - on_connection_error()]  Connection to Redis lost: Retry (3/20) in 1.00 second.
┃   Jun 17 21:03:42 kali faraday-server[15272]: 2026-06-17T21:03:42+0000 - celery.backends.redis - ERROR {MainThread} [pid:15272] [redis.py:435 - on_connection_error()]  Connection to Redis lost: Retry (4/20) in 1.00 second.
┃   Jun 17 21:03:42 kali systemd[1]: faraday.service: Deactivated successfully.
┃   Jun 17 21:03:42 kali systemd[1]: faraday.service: Consumed 1.473s CPU time over 4.985s wall clock time, 145M memory peak.
┃
┗━
```

### `faraday-worker`

官方给出的调用示例：`faraday-worker -h`

```text
root@kali:~# faraday-worker -h
usage: faraday-worker [-h] [--queue QUEUE] [--concurrency CONCURRENCY]
                      [--loglevel LOGLEVEL]
options:
  -h, --help            show this help message and exit
  --queue QUEUE         Celery queue
  --concurrency CONCURRENCY
                        Celery concurrency
  --loglevel LOGLEVEL   Celery log level
```

### `faraday-worker-gevent`

官方给出的调用示例：`faraday-worker-gevent -h`

```text
root@kali:~# faraday-worker-gevent -h
usage: faraday-worker-gevent [-h] [--queue QUEUE] [--concurrency CONCURRENCY]
                             [--loglevel LOGLEVEL]
options:
  -h, --help            show this help message and exit
  --queue QUEUE         Celery queue
  --concurrency CONCURRENCY
                        Celery concurrency
  --loglevel LOGLEVEL   Celery log level
```

### `python-faraday`

官方给出的调用示例：`python-faraday -h`

```text
root@kali:~# python-faraday -h
┏━(Message from Kali developers)
┃
┃ Please wait for the faraday service to start
┃ ..........
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install python-faraday`，再执行 `faraday --version` 2>/dev/null || `faraday -V`
- [ ] **2.** **读官方帮助** —— `faraday -h`，需要细节时 `man faraday`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: faraday-manage [OPTIONS] COMMAND [ARGS]...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/python-faraday/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/python-faraday/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/python-faraday/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
