# 11 · 系统管理（systemd）

> 概念前置：[`../basics/07-系统启动与systemd.md`](../basics/07-系统启动与systemd.md)。
> 日志与安全审计：[`12-安全与审计.md`](12-安全与审计.md)。
> 返回总索引：[`README.md`](README.md)。

## 本分类命令清单

| 命令 | 一句话 | 跳转 |
|------|--------|------|
| `systemctl` | 服务与单元管理（核心） | [↓](#systemctl--服务与单元管理) |
| `journalctl` | systemd 日志检索 | [↓](#journalctl--检索-systemd-日志) |
| `systemd-analyze` | 启动性能与配置分析 | [↓](#systemd-analyze--启动性能分析) |
| `systemd-run` | 临时运行服务/定时任务 | [↓](#systemd-run--临时运行服务与定时任务) |
| `systemd-cgls` | cgroup 树 | [↓](#systemd-cgls--cgroup-树) |
| `systemd-cgtop` | cgroup 资源占用 | [↓](#systemd-cgtop--cgroup-资源占用) |
| `systemd-tmpfiles` | 临时文件与目录管理 | [↓](#systemd-tmpfiles--临时文件管理) |
| `systemd-cat` | 把输出送进 journal | [↓](#systemd-cat--把输出送入-journal) |
| `loginctl` | 登录会话管理 | [↓](#loginctl--登录会话管理) |
| `hostnamectl` | 主机名与系统标识 | [↓](#hostnamectl--主机名与系统标识) |
| `timedatectl` | 时间与时区 | [↓](#timedatectl--时间与时区) |
| `localectl` | 语言与键盘布局 | [↓](#localectl--语言与键盘布局) |
| `machinectl` | 容器与虚拟机管理 | [↓](#machinectl--容器与虚拟机管理) |
| `resolvectl` | DNS 解析管理 | [↓](#resolvectl--dns-解析管理) |
| `bootctl` | 引导加载器管理 | [↓](#bootctl--引导加载器管理) |
| `systemctl` 关机重启 | 关机/重启/挂起 | [↓](#shutdown--reboot--halt--poweroff--关机与重启) |
| `service` / `chkconfig` | SysV 兼容前端 | [↓](#service--chkconfig--update-rcd--sysv-兼容) |
| `systemd-detect-virt` | 检测虚拟化环境 | [↓](#systemd-detect-virt--检测虚拟化环境) |
| `coredumpctl` | 崩溃转储管理 | [↓](#coredumpctl--崩溃转储管理) |

---

### systemctl — 服务与单元管理

**常用度**：★★★★★ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

#### 语法
```bash
systemctl [选项] 命令 [单元...]
```

#### 生命周期命令
| 命令 | 作用 |
|------|------|
| `start X` | 启动 ⭐ |
| `stop X` | 停止 ⭐ |
| `restart X` | 重启 ⭐ |
| `reload X` | 重载配置（不中断服务，需服务支持） ⭐ |
| `reload-or-restart X` | 优先 reload，不行则 restart ⭐ |
| `try-restart X` | 只在运行中时重启 |
| `enable X` | 开机自启（创建符号链接） ⭐ |
| `disable X` | 取消自启 ⭐ |
| `enable --now X` | **启用并立即启动** ⭐⭐ |
| `mask X` | 屏蔽（比 disable 更强，防止被依赖拉起） ⭐ |
| `unmask X` | 取消屏蔽 |

#### 查询命令
| 命令 | 作用 |
|------|------|
| `status X` | 状态 + 最近日志 ⭐⭐ |
| `is-active X` | 是否运行（输出 `active`/`inactive`/`failed`） ⭐ |
| `is-enabled X` | 是否自启 ⭐ |
| `is-failed X` | 是否失败 |
| `list-units` | 列出已加载单元 ⭐ |
| `list-units --failed` | **只列故障单元** ⭐⭐ |
| `list-unit-files` | 列出所有单元文件 ⭐ |
| `list-unit-files --state=enabled` | 列出已启用的 ⭐ |
| `list-dependencies X` | 依赖树 ⭐ |
| `cat X` | **显示单元文件内容（含 drop-in）** ⭐⭐ |
| `show X` | 显示所有属性（机器可读） ⭐ |
| `show -p 属性 X` | 只看某个属性 ⭐⭐ |
| `list-timers --all` | 列出定时器与下次触发时间 ⭐⭐ |
| `list-sockets` | 列出 socket 单元 |

#### 编辑命令
| 命令 | 作用 |
|------|------|
| `edit X` | **创建 drop-in（推荐）** ⭐⭐ |
| `edit --full X` | 编辑完整单元文件（升级可能被覆盖） |
| `revert X` | 撤销所有本地修改 ⭐ |
| `daemon-reload` | **重新加载单元文件（改完必须做）** ⭐⭐ |
| `daemon-reexec` | 重新执行 systemd 自身（版本升级后） ⭐ |

#### 高频选项
| 选项 | 含义 |
|------|------|
| `--now` | 配合 enable/disable，立即生效 ⭐ |
| `--user` | 操作用户级服务（不需要 root） ⭐ |
| `-H 主机` / `-M 机器` | 远程/容器内操作 ⭐ |
| `--type=service` | 按类型过滤 ⭐ |
| `--state=running` | 按状态过滤 ⭐ |
| `--all` | 包含未加载/未活动的 ⭐ |
| `--no-pager` | 不分页（脚本用） ⭐ |
| `--plain` | 不用颜色与分页 ⭐ |
| `--no-legend` | 不显示表头/说明 ⭐ |
| `--quiet` | 安静 |
| `--failed` | 同 `list-units --failed` |
| `-l` / `--full` | 不截断输出 ⭐ |
| `--value` | 只输出值（脚本用） ⭐⭐ |
| `-p 属性` | 指定属性（`show`） ⭐ |
| `--runtime` | 只改运行时（重启丢失） ⭐ |
| `--force` | 覆盖符号链接冲突 ⚠️ |

#### 实战示例
```bash
# 场景：⭐ 看服务状态（排障第一命令）
$ systemctl status nginx -l --no-pager
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: enabled)
     Active: active (running) since Tue 2026-09-15 09:00:00 CST; 30min ago
       Docs: man:nginx(8)
   Main PID: 1234 (nginx)
      Tasks: 5 (limit: 18930)
     Memory: 12.3M
        CPU: 234ms
     CGroup: /system.slice/nginx.service
             ├─1234 "nginx: master process /usr/sbin/nginx"
             └─1236 "nginx: worker process"

# 场景：⭐ 找所有故障单元
$ systemctl --failed
  UNIT              LOAD   ACTIVE SUB    DESCRIPTION
● myapp.service     loaded failed failed My App

$ sudo journalctl -u myapp --no-pager -n 50         # 看日志找原因

# 场景：⭐ 启用并立即启动（一行搞定）
$ sudo systemctl enable --now nginx redis postgresql

# 场景：⭐ 修改服务配置（用 drop-in，升级不丢）
$ sudo systemctl edit nginx
[Service]
LimitNOFILE=65535
Restart=always
RestartSec=3
$ sudo systemctl daemon-reload
$ sudo systemctl restart nginx
$ systemctl cat nginx | tail -10        # ⭐ 看最终生效的配置

# 场景：⭐ 只输出属性值（脚本用）
$ systemctl show -p MainPID --value nginx
1234
$ systemctl show nginx --value -p ActiveState -p SubState -p MainPID
active
running
1234
$ systemctl is-active --quiet nginx && echo OK || echo FAIL
$ systemctl is-enabled nginx

# 场景：⭐ 列出监听的 socket 单元（安全审计）
$ systemctl list-sockets
LISTEN                          UNIT                        ACTIVATES
/run/systemd/journal/stdout     systemd-journald.socket     systemd-journald.service
0.0.0.0:22                      sshd.socket                 sshd.service
[::]:22                         sshd.socket                 sshd.service

# 场景：⭐ 定时器（cron 的替代）
$ systemctl list-timers --all
NEXT                        LEFT       LAST                        PASSED  UNIT                      ACTIVATES
Tue 2026-09-15 10:00:00 CST 28min left Tue 2026-09-15 09:00:00 CST 31min ago logrotate.timer       logrotate.service
Tue 2026-09-15 12:00:00 CST 2h left    Mon 2026-09-14 12:00:00 CST 22h ago   backup.timer          backup.service

# 场景：⭐ 查看服务的依赖（评估影响）
$ systemctl list-dependencies nginx
$ systemctl list-dependencies --reverse nginx      # ⭐ 谁依赖它
$ systemctl list-dependencies --after nginx        # 启动顺序

# 场景：⭐ 用户级服务（不需要 root）
$ systemctl --user status myapp
$ systemctl --user enable --now myapp
$ systemctl --user daemon-reload
$ loginctl enable-linger alice                     # ⭐ 让用户服务在未登录时也能运行
$ ls ~/.config/systemd/user/

# 场景：⭐ 远程/容器内操作
$ systemctl -H user@remote status nginx
$ systemctl -M mycontainer status nginx            # 容器（machinectl 管理的）
$ systemctl --root=/mnt/sysroot enable nginx       # ⭐ 操作另一个根（救援模式）

# 场景：🔐 排查可疑服务（持久化）⭐⭐
$ systemctl list-unit-files --state=enabled
$ systemctl list-units --type=service --state=running
$ find /etc/systemd/system /usr/lib/systemd/system -name '*.service' -newermt '7 days ago' -ls
$ systemctl list-units --type=service --all --no-legend | awk '$4=="failed" {print}'
$ # ⭐ 检查最近被改动的单元文件
$ systemctl list-unit-files --state=enabled --no-legend | awk '{print $1}' | while read -r u; do
>   f=$(systemctl show -p FragmentPath --value "$u")
>   [ -n "$f" ] && [ -f "$f" ] && stat -c '%y %n' "$f"
> done | sort -r | head -20

# 场景：🔐 屏蔽已知危险的单元（加固）
$ sudo systemctl mask ctrl-alt-del.target           # 禁用 Ctrl+Alt+Del 重启
$ sudo systemctl mask systemd-coredump@.service     # 不收集 core dump（防信息泄露）
$ sudo systemctl mask systemd-ask-password-plymouth.path

# 场景：⭐ 列出被 mask 的单元
$ systemctl list-unit-files --state=masked

# 场景：🔐 检查用户级服务的持久化（攻击者常用）
$ ls -la ~/.config/systemd/user/ /etc/systemd/user/ 2>/dev/null
$ systemctl --user list-unit-files --state=enabled
$ sudo find /home -path '*/.config/systemd/user/*' -name '*.service' 2>/dev/null

# 场景：🧪 服务的资源限制（cgroup）
$ systemctl show -p MemoryMax -p CPUQuota -p TasksMax -p LimitNOFILE nginx
MemoryMax=infinity
CPUQuota=
TasksMax=18930
LimitNOFILE=524288
$ sudo systemctl set-property nginx MemoryMax=512M CPUQuota=50%
$ systemctl show -p MemoryMax -p CPUQuota nginx

# 场景：⭐ 不写单元文件临时跑服务
$ sudo systemd-run --unit=testjob --property=MemoryMax=100M /usr/bin/stress-ng --cpu 2
$ systemctl status testjob
$ sudo systemctl stop testjob
```

#### 输出解读
`systemctl status` 的关键行：

| 行 | 含义 |
|----|------|
| `Loaded:` | 是否加载 + 单元文件路径 + 是否 enabled ⭐ |
| `Active:` | `active (running)` / `inactive (dead)` / `failed` ⭐ |
| `Main PID:` | 主进程 PID ⭐ |
| `Tasks:` | 进程/线程数（含 cgroup 上限） |
| `Memory:` | cgroup 内存占用 |
| `CGroup:` | cgroup 路径 + 进程树 ⭐ |
| `Docs:` | 文档链接 |

**常见状态值**：

| ACTIVE | SUB | 含义 |
|--------|-----|------|
| `active` | `running` | 正常运行 ⭐ |
| `active` | `exited` | 已正常退出（oneshot 类型正常） |
| `inactive` | `dead` | 未运行（正常停止） |
| `failed` | `failed` | **失败** ⭐ |
| `activating` | `start` | 正在启动（可能卡住） |
| `deactivating` | `stop` | 正在停止 |
| `active` | `waiting` | 等待某个事件（socket/path 单元） |

**常见 `status=数字`**：

| 值 | 含义 |
|----|------|
| `status=203/EXEC` | **`ExecStart` 路径不存在或不可执行** ⭐ |
| `status=200/CHDIR` | `WorkingDirectory` 不存在 ⭐ |
| `status=226/NAMESPACE` | 加固项（`ProtectSystem` 等）与程序需求冲突 ⭐ |
| `status=1/FAILURE` | 程序自身报错 |
| `code=killed, signal=TERM` | 被 SIGTERM 终止 |
| `code=killed, signal=SEGV` | **段错误（程序 bug）** ⭐ |
| `code=exited, status=0/SUCCESS` | 正常退出 |

#### 常见坑
- ⚠️⚠️ **改了单元文件（或 drop-in）必须 `daemon-reload`**，否则 systemd 仍用旧配置，出现「我明明改了但没生效」⭐。
- ⚠️ **`systemctl restart` 与 `reload` 的差异**：`reload` 需要服务实现 `ExecReload`（发 SIGHUP 或调专用命令），否则报错 ⭐。
- ⚠️ **`mask` 比 `disable` 强得多**：`disable` 只取消自启（手动仍能启动、能被依赖拉起），`mask` 会链接到 `/dev/null` 使其无法启动 ⭐。
- ⚠️ **`enable` 不启动，`start` 不自启**。要两者都做用 `enable --now` ⭐⭐。
- ⚠️ **`systemctl --user` 与系统级是两套独立的实例**，同名服务可能两处都有 ⭐。
- ⚠️ **用户级服务在用户注销后会停止**，除非 `loginctl enable-linger` ⭐。
- **`list-units` 默认只显示「已加载」的单元**，所有单元要用 `--all`（或 `list-unit-files`）⭐。
- **`list-unit-files` 显示的是「磁盘上的单元文件」**，与「已加载」不同 ⭐。
- **`-H` / `-M` 需要 SSH/D-Bus 支持**，容器里可能不可用 ⭐。
- **systemd 会记录「单元文件被改动」**(`unit file changed on disk`)，要 `daemon-reload` 消除 ⭐。
- **`systemctl stop` 不会阻止其他单元重新拉起它**（除非用 `mask`）⭐。

#### 相关命令
`journalctl` · `systemd-analyze` · `systemd-run` · `machinectl` · `loginctl`

---

### journalctl — 检索 systemd 日志

**常用度**：★★★★★ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

```bash
journalctl [选项] [匹配条件...]
```

#### 高频选项
| 选项 | 含义 |
|------|------|
| `-u 单元` | 按 unit 过滤（可多次） ⭐⭐ |
| `-f` / `--follow` | 实时跟随 ⭐⭐ |
| `-n N` | 最后 N 行 ⭐ |
| `-e` | 跳到末尾 ⭐ |
| `-r` | 倒序（最新在前） ⭐ |
| `-k` | 只内核消息 ⭐ |
| `-b [偏移]` | 本次/上次启动（`-b -1`） ⭐⭐ |
| `--list-boots` | 列出所有启动会话 ⭐ |
| `-p 级别` | 优先级（`err`、`warning`、`info`、`debug`、范围 `warning..err`） ⭐⭐ |
| `-t 标识` | 按 syslog 标识（`-t sudo`、`-t sshd`） ⭐ |
| `--since` / `--until` | 时间范围 ⭐⭐ |
| `-S` / `-U` | `--since` / `--until` 的缩写 ⭐ |
| `_PID=N` / `_UID=N` / `_GID=N` | 按字段匹配 ⭐ |
| `_COMM=名字` / `_EXE=路径` | 按进程名/可执行文件 ⭐ |
| `-o 格式` | 输出格式 ⭐ |
| `--no-pager` | 不分页 ⭐ |
| `-q` | 安静（不显示 `-- Reboot --` 等） |
| `--disk-usage` | 磁盘占用 ⭐ |
| `--vacuum-size=` / `--vacuum-time=` | 清理 ⭐ |
| `--rotate` | 轮转 |
| `--verify` | 校验日志完整性 🔐 ⭐ |
| `--verify-key=KEY` | 用指定密钥校验（FSS） 🔐 ⭐ |
| `-x` | 加解释性提示（含 man 链接） ⭐ |
| `--grep=模式` | 用 PCRE 搜索消息内容 ⭐ |
| `-a` | 完整显示（不省略） |
| `--utc` | UTC 时间 ⭐ |
| `--no-hostname` | 不显示主机名 |
| `-D 目录` / `--directory=` | 用指定日志目录（离线分析） ⭐⭐ |
| `-M 机器` | 容器/虚拟机日志 ⭐ |
| `--merge` | 合并所有可用日志源 |
| `-i` | 显示时用 `less` |
| `--output-fields=` | 指定输出哪些字段 |

**`-o` 输出格式**：

| 格式 | 用途 |
|------|------|
| `short`（默认） | 类 syslog |
| `short-precise` | 微秒精度 ⭐ |
| `short-iso` | ISO 8601 时间 ⭐ |
| `short-unix` | Unix 时间戳 |
| `cat` | 只有消息体 ⭐ |
| `json` / `json-pretty` | JSON（脚本用） ⭐⭐ |
| `verbose` | 所有元数据字段 ⭐ |
| `with-unit` | 含 unit 名 |
| `export` | 二进制导出（可再导入） |

#### 实战示例
```bash
# 场景：⭐ 看某服务的日志（最常用）
$ journalctl -u nginx -n 50 --no-pager
$ journalctl -u nginx -f                        # 实时跟随
$ journalctl -u nginx -u php-fpm -f             # 多个 unit

# 场景：⭐⭐ 综合排障（服务启动失败）
$ systemctl status myapp -l --no-pager
$ journalctl -u myapp -b --no-pager -n 100
$ journalctl -u myapp -b -p err -x --no-pager   # ⭐ 只看错误 + 解释
$ journalctl -u myapp --since "10 min ago" --no-pager

# 场景：⭐⭐ 看上次启动的日志（崩溃后排障）
$ journalctl --list-boots
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
 -2 d1a2b3c4...                      Mon 2026-09-13 20:00:00 CST Tue 2026-09-14 08:00:00 CST
 -1 e5f6a7b8...                      Mon 2026-09-14 22:00:00 CST Tue 2026-09-15 07:30:00 CST
  0 f9a8b7c6...                      Tue 2026-09-15 07:31:00 CST Tue 2026-09-15 09:30:00 CST

$ journalctl -b -1 -p err --no-pager            # ⭐ 上次启动的错误
$ journalctl -b -2 -k --no-pager | tail -30
$ journalctl --since "$(uptime -s)" --no-pager | head -50    # 本次启动以来

# 场景：⭐ 时间范围（跨启动也能查）
$ journalctl --since "2026-09-15 08:00:00" --until "2026-09-15 09:30:00"
$ journalctl -S -30min -U -5min
$ journalctl --since today -p warning
$ journalctl --since yesterday --until now -p err

# 场景：⭐ 只看内核消息
$ journalctl -k -b --no-pager
$ journalctl -k -b -1 -p err                    # 上次启动的内核错误
$ journalctl -k --since "1 hour ago" | grep -iE 'error|fail|panic|oom'

# 场景：⭐ 优先级过滤（8 级）
$ journalctl -p err --no-pager -n 50            # err 及以上
$ journalctl -p warning..err --no-pager -n 50   # 范围
$ journalctl -u nginx -p err -b --no-pager

# 场景：⭐ 按 syslog 标识（非 systemd 服务）
$ journalctl -t sudo --no-pager -n 20
$ journalctl -t sshd --since "1 hour ago" --no-pager
$ journalctl -t kernel -t systemd-udevd --no-pager -n 30

# 场景：⭐ JSON 输出（脚本分析）⭐⭐
$ journalctl -u nginx -o json-pretty -n 3
$ journalctl -u nginx -o json -n 100 | jq -r 'select(.PRIORITY=="3") | "\(.__REALTIME_TIMESTAMP) \(.MESSAGE)"'
$ journalctl -o json -n 1000 | jq -r '.["MESSAGE"]' | grep -c ERROR
$ # ⭐ 提取某服务的错误消息
$ journalctl -u myapp -o json -b | jq -r 'select(.PRIORITY == "4") | .MESSAGE'

# 场景：⭐ 只输出消息体（便于管道）
$ journalctl -u nginx -o cat -n 100 | sort | uniq -c | sort -rn | head
$ journalctl -k -o cat -b | head

# 场景：⭐ 按字段过滤（精确到进程）
$ journalctl _PID=1234 --no-pager
$ journalctl _UID=1000 -n 20 --no-pager
$ journalctl _COMM=sshd --since "1 hour ago"
$ journalctl _EXE=/usr/bin/sudo --no-pager -n 10
$ journalctl /usr/bin/sshd --no-pager -n 10     # ⭐ 按可执行文件路径

# 场景：⭐ 用 PCRE 搜索消息内容
$ journalctl --grep='timeout|refused' -u nginx --no-pager -n 20
$ journalctl --grep='Failed password' -t sshd --no-pager | tail -20

# 场景：⭐ 带解释性提示（含 man 链接）
$ journalctl -xe --no-pager | tail -40
$ journalctl -u myapp -x -b --no-pager

# 场景：⭐ 磁盘占用与清理
$ journalctl --disk-usage
Archived and active journals take up 1.2G in the file system.
$ sudo journalctl --vacuum-size=500M
$ sudo journalctl --vacuum-time=30d
$ sudo journalctl --vacuum-files=10
$ systemctl status systemd-journald
$ grep -E '^(Storage|SystemMaxUse|MaxRetentionSec)' /etc/systemd/journald.conf

# 场景：⭐ 开启持久化日志（默认可能只在内存）
$ sudo mkdir -p /var/log/journal
$ sudo systemd-tmpfiles --create --prefix /var/log/journal
$ sudo systemctl restart systemd-journald
$ ls /var/log/journal/
$ journalctl --list-boots          # ⭐ 有历史说明持久化成功

# 场景：🔐 校验日志完整性（防篡改）⭐⭐
$ journalctl --verify
$ sudo journalctl --verify 2>&1 | tail -20
PASS: /var/log/journal/.../system.journal
# ⭐ 有 FAIL 说明日志文件被改动或损坏

# 场景：🔐 日志的 FSS（Forward Secure Sealing）验证 ⭐
$ journalctl --setup-keys
$ journalctl --verify-key="$(cat /etc/systemd/journald.seal.key)"
$ # ⭐ 需要先在 journald.conf 里开 Seal=yes

# 场景：🔐 离线分析别人的日志（取证）⭐⭐
$ sudo journalctl -D /mnt/evidence/var/log/journal --no-pager
$ sudo journalctl -D /mnt/evidence/var/log/journal --list-boots
$ sudo journalctl -D /mnt/evidence/var/log/journal -b -1 -p err --no-pager | head -50
$ sudo journalctl -D /mnt/evidence/var/log/journal --verify
$ sudo journalctl -D /mnt/evidence/var/log/journal -o json --no-pager > /tmp/evidence.json
$ jq -r '."[MESSAGE]"' /tmp/evidence.json | grep -i 'authentication failure' | head

# 场景：🔐 安全排查常用组合 ⭐⭐
$ # 1. 登录失败（暴力破解）
$ journalctl -u sshd --since "24 hours ago" --no-pager | grep -iE 'failed password|invalid user' | tail -30
$ # 2. sudo 使用
$ journalctl -t sudo --since "24 hours ago" --no-pager | tail -30
$ journalctl _COMM=sudo --since today --no-pager | grep -i 'COMMAND'
$ # 3. 服务崩溃
$ journalctl -b -p err..alert --no-pager
$ # 4. 新建用户/权限变更（需 auditd 或特定服务日志）
$ journalctl -t useradd -t userdel -t usermod --no-pager
$ # 5. systemd 单元被创建/修改
$ journalctl -u systemd --since "24 hours ago" --no-pager | grep -iE 'Created|Started.*service'
$ # 6. 核心转储
$ journalctl -t systemd-coredump --no-pager | tail -20

# 场景：⭐ 导出日志（便于离线分析或取证）
$ sudo journalctl --since "2026-09-15" -o export > /tmp/journal.export
$ sudo journalctl --since "2026-09-15" -o json-pretty > /tmp/journal.json
$ sudo journalctl --since "2026-09-15" > /tmp/journal.txt
$ # 导入 export 格式（用 journalctl -D 不行，要直接读文件）
$ cat /tmp/journal.export | head -20

# 场景：⭐ 合并多源日志（如容器）
$ journalctl --merge -b --no-pager | head -30
$ journalctl -M mycontainer -n 50 --no-pager

# 场景：⭐ UTC 时间（跨时区分析必用）
$ journalctl --utc -u nginx -n 20 --no-pager
$ journalctl --utc -o short-iso -n 5

# 场景：🧪 统计与聚合
$ journalctl -b -p err -o cat --no-pager | sort | uniq -c | sort -rn | head -20
$ journalctl --since today -u nginx -o json | jq -r '.MESSAGE' | awk '{print $NF}' | sort | uniq -c | sort -rn | head

# 场景：🧪 手动写日志（测试）
$ echo "test message" | systemd-cat -t mytest
$ journalctl -t mytest -n 3 --no-pager
$ logger -t mytest2 "from logger"
$ journalctl -t mytest2 -n 2 --no-pager
```

#### 输出解读
默认输出格式：
```
Sep 15 09:30:00 hostname nginx[1234]: 2026/09/15 09:30:00 [error] ...
│                │        │    │       └─ 消息体
│                │        │    └─ PID
│                │        └─ 进程名
│                └─ 主机名
└─ 时间
```

**优先级编号**：

| 编号 | 名称 | 含义 |
|------|------|------|
| 0 | `emerg` | 系统不可用 |
| 1 | `alert` | 需立即处理 |
| 2 | `crit` | 严重 |
| 3 | `err` | 错误 ⭐ |
| 4 | `warning` | 警告 ⭐ |
| 5 | `notice` | 正常但重要 |
| 6 | `info` | 信息 ⭐ |
| 7 | `debug` | 调试 |

**日志存储位置**：

| 路径 | 用途 |
|------|------|
| `/var/log/journal/` | **持久化**日志（重启保留） ⭐ |
| `/run/log/journal/` | 内存日志（重启丢失） ⭐ |
| `/etc/systemd/journald.conf` | 配置 |
| `/var/log/journal/<machine-id>/` | 按机器 ID 分目录（取证时要对 machine-id）⭐ |

#### 常见坑
- ⚠️⚠️ **默认可能不持久化**（只存 `/run`，重启即失）。**重要系统必须开启 `Storage=persistent` 并建 `/var/log/journal`** ⭐⭐。
- ⚠️ **`-p err` 表示「err 及更严重」，不是「恰好 err」**。范围要写 `-p err..err` ⭐。
- ⚠️ **`-u` 只能按 unit 过滤**，非 systemd 服务（如 `sudo`、`sshd` 的某些消息）要用 `-t` 或 `_COMM=`/`_EXE=` ⭐。
- ⚠️ **`-b -1` 是「上一次启动」**，不是「1 小时前」⭐。
- ⚠️ **`journalctl -f` 与 `tail -f` 的差异**：`journalctl -f` 能跟随 unit 过滤与时间过滤，且能处理日志轮转 ⭐。
- ⚠️ **root 可以 `journalctl --rotate && journalctl --vacuum-time=1s` 清掉所有日志**（🔐 攻击者的标准清理动作）⭐。关键日志必须**实时转发到远端**（rsyslog / 远程 journald）。
- ⚠️ **`--verify` 能发现日志文件损坏或被截断**，但**不能发现「整段被删」**（删除是合法的轮转行为）🔐。
- **`journalctl` 不接受管道输入**（要 `journalctl --grep=` 或先导出再处理）⭐。
- **`-o json` 的字段名是下划线大写的**（`_PID`、`MESSAGE`、`PRIORITY`、`__REALTIME_TIMESTAMP`）⭐。
- **`-D` 可以分析挂载的离线日志目录**（取证必备，比 `journalctl -M` 更通用）⭐⭐。
- **`journalctl` 的时间过滤按本地时区**，跨时区用 `--utc` ⭐。

#### 相关命令
`dmesg` · `logger` · `systemd-cat` · `rsyslogd` · `systemctl status` · `journald.conf`

---

### systemd-analyze — 启动性能分析

**常用度**：★★★★☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

```bash
systemd-analyze [命令] [选项]
```

| 命令 | 作用 |
|------|------|
| （无参） | 总启动耗时分解（firmware/loader/kernel/userspace） ⭐ |
| `blame` | **按耗时排序的单元启动列表** ⭐⭐ |
| `critical-chain [单元]` | 关键路径链 ⭐⭐ |
| `time` | 用户空间启动耗时 |
| `plot` | 生成 SVG 启动图 ⭐ |
| `dot` | 生成依赖图（Graphviz） ⭐ |
| `verify [文件]` | **校验单元文件语法** ⭐⭐ |
| `calendar '表达式'` | 校验 `OnCalendar` 表达式 ⭐⭐ |
| `timespan '表达式'` | 校验时间跨度 |
| `security [单元]` | **安全评分（加固建议）** ⭐⭐ |
| `unit-paths` | 显示单元文件搜索路径 ⭐ |
| `exit-status 码` | 解释退出码含义 ⭐ |
| `cat-config 文件` | 显示配置的合并结果 ⭐ |

| 选项 | 含义 |
|------|------|
| `--system` / `--user` | 系统/用户级 ⭐ |
| `--no-pager` | 不分页 ⭐ |
| `--man=no` | 不显示 man 提示 |
| `-H` / `-M` | 远程 / 容器 |
| `--root=` | 指定根目录 |
| `--fuzz=N` | 时间容差 |

#### 实战示例
```bash
# 场景：⭐ 总启动耗时
$ systemd-analyze
Startup finished in 3.201s (firmware) + 1.104s (loader) + 2.883s (kernel) + 4.517s (userspace) = 11.706s
graphical.target reached after 4.412s in userspace.
# ⭐ 若 userspace 慢，用 blame 找原因；若 kernel 慢，看 dmesg

# 场景：⭐⭐ 找出启动慢的单元（最常用）
$ systemd-analyze blame | head -20
4.234s NetworkManager-wait-online.service
1.234s systemd-udev-settle.service
0.876s docker.service
0.543s snapd.service
# ⭐ 前几个通常是「等待网络就绪」「等待设备」类，可以优化或屏蔽

# 场景：⭐⭐ 关键路径（启动链上的时间瓶颈）
$ systemd-analyze critical-chain
the time when unit became active or started is printed after the "@" character.
the time the unit took to start is printed after the "+" character.

graphical.target @4.412s
└─multi-user.target @4.410s
  └─docker.service @3.499s +0.876s
    └─network-online.target @3.487s
      └─NetworkManager-wait-online.service @1.234s +2.234s
        └─NetworkManager.service @1.100s +0.130s
          └─basic.target @1.050s

$ systemd-analyze critical-chain nginx.service     # ⭐ 某个单元的关键链

# 场景：⭐ 生成可视化启动图
$ systemd-analyze plot > /tmp/boot.svg
$ xdg-open /tmp/boot.svg 2>/dev/null || echo "把 /tmp/boot.svg 下载到本地看"
$ systemd-analyze plot --no-pager | head -5

# 场景：⭐ 生成依赖图（需 graphviz）
$ systemd-analyze dot nginx.service | dot -Tsvg > /tmp/nginx-deps.svg
$ systemd-analyze dot --order | dot -Tsvg > /tmp/order.svg

# 场景：⭐⭐ 校验单元文件语法（改完必做）
$ systemd-analyze verify /etc/systemd/system/myapp.service
$ sudo systemd-analyze verify /etc/systemd/system/*.service
# 无输出 = 语法正确；有输出会提示具体问题（依赖不存在、ExecStart 路径错等）

$ # ⭐ 更大的用途：校验整个 systemd 配置
$ sudo systemd-analyze verify /usr/lib/systemd/system/*.service 2>&1 | head -20
$ sudo systemd-analyze verify /etc/fstab 2>&1 | head

# 场景：⭐⭐ 校验 OnCalendar 表达式（写定时器时必做）
$ systemd-analyze calendar 'daily'
  Original form: daily
Normalized form: *-*-* 00:00:00
    Next elapse: Tue 2026-09-15 00:00:00 CST
       (in UTC): Mon 2026-09-14 16:00:00 UTC
       From now: 9h ago

$ systemd-analyze calendar 'Mon..Fri 09:00'
$ systemd-analyze calendar '*-*-* 03:00:00'
$ systemd-analyze calendar '*:0/15'
$ systemd-analyze calendar 'Mon,Wed,Fri *-*-* 02:30:00'
$ systemd-analyze calendar --iterations=5 'daily'     # ⭐ 看接下来 5 次

# 场景：⭐ 校验 timespan 表达式
$ systemd-analyze timespan '2h 30min'
Original: 2h 30min
   μs: 9000000000
Human: 2h 30min

# 场景：⭐⭐ 安全评分（加固检查，非常有价值）
$ systemd-analyze security nginx.service
  NAME                                                        DESCRIPTION                                 EXPOSURE
✓ PrivateTmp=                                                Service has its own private /tmp                 
✓ ProtectSystem=                                             Service has a restricted filesystem view         
✗ PrivateDevices=                                            Service potentially has access to hardware devices
✗ ProtectKernelTunables=                                     ...
✗ NoNewPrivileges=                                           Service may be able to elevate privileges
✗ RestrictAddressFamilies=                                   Service may be able to create sockets of any type
...
→ Overall exposure level for nginx.service: 7.4 OK 🙂
# ⭐ 评分 0（最安全）到 10（最不安全）。可据此加加固项

$ systemd-analyze security --no-pager | tail -5      # 所有单元的总览
$ systemd-analyze security --user                     # 用户级
$ systemd-analyze security --threshold=5              # 只显示超过阈值的

# 场景：⭐ 解析退出码（脚本里的错误码含义）
$ systemd-analyze exit-status 1
1: FAILURE — Generic error code for failures not fitting any other category
$ systemd-analyze exit-status 203
203: EXEC — Failed to invoke the process
$ systemd-analyze exit-status 226
226: NAMESPACE — Failed to set up a namespace

# 场景：⭐ 单元文件的搜索路径（理解「用的是哪个文件」）
$ systemd-analyze unit-paths
/etc/systemd/system.control
/run/systemd/system.control
/run/systemd/transient
/run/systemd/generator.early
/etc/systemd/system
/run/systemd/system
/usr/local/lib/systemd/system
/usr/lib/systemd/system

# 场景：⭐ 看配置的合并结果（含 drop-in）
$ systemd-analyze cat-config systemd/system.conf | head -30
$ systemd-analyze cat-config systemd/journald.conf | grep -vE '^\s*#|^$'
$ systemd-analyze cat-config systemd/resolved.conf

# 场景：🧪 优化启动（诊断后的行动）⭐
$ # 1. 屏蔽不需要的等待服务
$ sudo systemctl mask NetworkManager-wait-online.service     # ⚠️ 若不用网络盘
$ sudo systemctl mask systemd-udev-settle.service
$ # 2. 用 automount 让网络盘按需挂载
$ # 3. 延迟非关键服务（用 After= 而非 Requires=）
$ # 4. 检查 fstab 里有没有不必要的依赖
$ systemd-analyze blame | head -10
```

#### 输出解读
`blame` 的输出：`耗时 单元名`。**耗时是「该单元激活所需的时间」，不是它的运行时长** ⭐。

`critical-chain` 的符号：

| 符号 | 含义 |
|------|------|
| `@时间` | 该单元变为 active 的时刻 ⭐ |
| `+耗时` | 该单元启动花费的时间 ⭐ |
| `└─` | 依赖链的下一环 |

**关键路径的解读方法**：从目标往上找，**`+耗时` 大的那一环就是瓶颈** ⭐。

`security` 的输出：

| 标记 | 含义 |
|------|------|
| `✓` | 该项已加固 ⭐ |
| `✗` | **未加固**（有暴露） ⭐ |
| `-` | 不适用 |

| 评分 | 含义 |
|------|------|
| 0–2 | 很安全 |
| 3–5 | 一般 |
| 6–8 | 暴露较多 ⭐ |
| 9–10 | 极度暴露 ⚠️ |

#### 常见坑
- ⚠️ **`blame` 的总和远大于 `systemd-analyze` 的总时间**（因为单元是并行的）。**看单项耗时，不要看总和** ⭐。
- ⚠️ **`NetworkManager-wait-online.service` 通常是最大的「无意义等待」**（它在等网络真的可用，而大多数服务并不需要）。可屏蔽（若不用网络挂载）⭐⭐。
- ⚠️ **`verify` 需要单元依赖的所有单元都存在**，否则会报「找不到依赖」的假阳性 ⭐。
- ⚠️ **`security` 的评分是启发式的**（按 unit 文件里有没有写加固项），**不代表实际暴露程度**（程序自身可能更不安全）⭐。
- ⚠️ **`calendar` 是校验 `OnCalendar` 的必备工具**（表达式写错会导致定时器不触发，但不报错）⭐⭐。
- **`plot` 与 `dot` 需要额外工具**（`dot` 需 graphviz）⭐。
- **`--user` 要配合 `systemd-analyze --user` 才能看用户级** ⭐。
- **`systemd-analyze` 的时间包含固件与内核阶段**（firmware/loader/kernel），远超 userspace ⭐。

#### 相关命令
`systemctl` · `journalctl` · `systemd-run` · `graphviz`

---

### systemd-run — 临时运行服务与定时任务

**常用度**：★★★★☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有（systemd 236+）

```bash
systemd-run [选项] 命令 [参数...]
```

| 选项 | 含义 |
|------|------|
| `--unit=名字` | 指定单元名 ⭐ |
| `--scope` | **在当前上下文运行（不改环境）** ⭐ |
| `--service`（默认） | 创建临时服务单元 |
| `--user` | 用户级 ⭐ |
| `--pty` | 分配伪终端（交互式） ⭐ |
| `--pipe` | 把命令的 stdio 接到调用者 ⭐ |
| `--wait` | 等待命令结束（返回其退出码） ⭐ |
| `-p 属性=值` | 设置单元属性（资源限制等） ⭐⭐ |
| `--property=` | 同上 |
| `--on-active=时间` | **相对定时器**（`10min`、`1h`） ⭐⭐ |
| `--on-calendar=表达式` | **日历定时器**（`daily`、`Mon 09:00`） ⭐⭐ |
| `--on-boot=时间` | 启动后一段时间 |
| `--timer-property=` | 定时器属性 |
| `-E 变量=值` | 设置环境变量 ⭐ |
| `--working-directory=目录` | 工作目录 ⭐ |
| `-q` | 安静 |
| `-G` | 输出机器可读格式 ⭐ |
| `--collect` | 结束后自动清理单元 ⭐ |
| `--same-dir` | 用当前目录 |
| `-t` | 同 `--pty` |
| `--description=` | 描述 |

#### 实战示例
```bash
# 场景：⭐ 临时跑一个服务（不用写 unit 文件）
$ sudo systemd-run --unit=testjob /usr/bin/stress-ng --cpu 2 --timeout 30s
Running as unit: testjob.service
$ systemctl status testjob
$ sudo journalctl -u testjob -f
$ sudo systemctl stop testjob
$ sudo systemctl reset-failed testjob

# 场景：⭐⭐ 带资源限制运行（cgroup 隔离，非常适合做实验）
$ sudo systemd-run --unit=limited \
>   -p MemoryMax=200M -p CPUQuota=50% -p TasksMax=50 \
>   /usr/bin/stress-ng --vm 1 --vm-bytes 500M --timeout 20s
$ systemctl status limited
$ systemctl show -p MemoryMax -p CPUQuota -p TasksMax limited

$ # ⭐ 观察 OOM（内存限制生效）
$ sudo systemd-run -p MemoryMax=50M --wait /usr/bin/stress-ng --vm 1 --vm-bytes 200M
$ sudo journalctl -u run-* -p err --no-pager | tail -10

# 场景：⭐ 定时任务（替代 at/cron，不需要写 unit）⭐⭐
$ sudo systemd-run --on-active=5min --unit=reminder /usr/bin/wall "5 分钟到"
$ sudo systemd-run --on-active=1h --unit=backup-in-1h /usr/local/bin/backup.sh
$ systemctl list-timers | grep reminder
$ sudo systemctl list-dependencies reminder.timer

# 场景：⭐ 日历定时（持久化到重启后仍有效？不——这是临时的）
$ sudo systemd-run --on-calendar='Mon..Fri 09:00' --unit=weekdaytask /usr/local/bin/task.sh
$ systemd-analyze calendar 'Mon..Fri 09:00'          # ⭐ 先校验表达式
$ systemctl list-timers weekdaytask.timer

# 场景：⭐ 清理临时单元（重要）⭐
$ sudo systemctl stop reminder.timer
$ sudo systemctl reset-failed
$ systemctl list-units --all | grep -E 'run-|testjob|reminder'

# 场景：⭐⭐ 用 --scope 在当前上下文运行（不创建服务）
$ sudo systemd-run --scope -p MemoryMax=100M /usr/bin/stress-ng --cpu 1 --timeout 10s
$ # ⭐ 差异：
$ #   --service（默认）：创建独立服务单元，脱离当前会话
$ #   --scope：在当前会话里运行，作为一个 scope 单元被跟踪

# 场景：⚠️ 用 run 做的事前准备（远程改网络的回滚保险）⭐⭐
$ # 5 分钟后自动重启网络（防把自己锁死）
$ sudo systemd-run --on-active=5min --unit=net-rollback /usr/bin/systemctl restart NetworkManager
$ # ... 改网络配置 ...
$ # 验证没问题后取消
$ sudo systemctl stop net-rollback.timer
$ sudo systemctl reset-failed net-rollback

# 场景：⭐ 用户级 run（不需要 root）
$ systemd-run --user --unit=mytask --wait /usr/bin/sleep 5
$ systemctl --user status mytask
$ systemd-run --user --pty /usr/bin/vim /tmp/test.txt     # 交互式

# 场景：⭐ 交互式命令（--pty）
$ sudo systemd-run --pty --unit=debugshell /bin/bash
$ # 现在是 systemd 管理的 shell（有 cgroup 与资源限制）

# 场景：⭐ 用 --pipe 接入 stdio（脚本里获取输出）
$ sudo systemd-run --pipe --wait /usr/bin/id
$ sudo systemd-run --pipe /usr/bin/echo "hello"

# 场景：⭐ 设置环境变量与工作目录
$ systemd-run --user -E FOO=bar --working-directory=/tmp --wait /usr/bin/env | grep FOO
$ sudo systemd-run -E PATH=/usr/local/bin:/usr/bin --wait /usr/local/bin/mytool

# 场景：⭐ 完整的服务级隔离（把命令当成 hardened 服务跑）⭐⭐
$ sudo systemd-run --unit=sandboxed \
>   -p DynamicUser=yes \
>   -p PrivateTmp=yes -p PrivateDevices=yes \
>   -p ProtectSystem=strict -p ProtectHome=yes \
>   -p NoNewPrivileges=yes -p RestrictAddressFamilies=AF_UNIX \
>   -p MemoryMax=256M -p CPUQuota=25% \
>   --wait /usr/bin/untrusted_binary

$ systemd-analyze security sandboxed.service        # ⭐ 看加固评分

# 场景：🧪 沙箱里跑不可信程序（安全实验）⭐
$ sudo systemd-run --unit=isolate \
>   -p PrivateNetwork=yes -p PrivateTmp=yes \
>   -p ProtectSystem=strict -p ProtectHome=yes \
>   -p DynamicUser=yes -p NoNewPrivileges=yes \
>   --pty /bin/bash
# ⭐ 现在是一个没有网络、只读文件系统的隔离 shell

# 场景：⭐ 给正在运行的命令加限制（先跑，再改）⭐
$ sudo systemd-run --unit=myjob --pty /bin/bash
# 在另一个终端：
$ sudo systemctl set-property myjob MemoryMax=100M CPUQuota=20%
$ systemctl show -p MemoryMax,CPUQuota myjob

# 场景：🔐 排查可疑的 systemd-run 单元（持久化手法之一）⭐
$ systemctl list-units --all --no-legend | grep -E '^run-'
$ systemctl list-timers --all --no-legend | grep -vE 'systemd|logrotate|man-db|fstrim|apt|dnf'
$ ls -la /run/systemd/transient/ 2>/dev/null
$ # ⭐ 攻击者可能用 systemd-run --on-calendar 做持久化（在 /run 里，重启即失，适合短期）
```

#### 输出解读
`systemd-run` 成功时输出：`Running as unit: 单元名.service` ⭐

**`--service` 与 `--scope` 的差异**：

| 方式 | 单元类型 | 环境 | 用途 |
|------|----------|------|------|
| `--service`（默认） | `.service` | 干净环境（不继承当前环境） | 后台服务、资源限制 ⭐ |
| `--scope` | `.scope` | **继承当前环境** | 在会话里跟踪现有进程 ⭐ |

**临时单元的位置**：`/run/systemd/transient/`（**重启即失**） ⭐

#### 常见坑
- ⚠️ **`systemd-run` 创建的单元是临时的**（在 `/run`，重启消失）。要持久化必须写真实的 unit 文件 ⭐。
- ⚠️ **不加 `--wait` 时命令在后台运行**，`systemd-run` 立即返回（退出码是「执行是否成功」，不是命令的退出码）⭐。
- ⚠️ **`--service` 不继承当前环境变量**（PATH 可能是默认的），要看情形用 `-E` 或用 `--scope` ⭐。
- ⚠️ **失败的临时单元会留在 `failed` 状态**，要 `systemctl reset-failed` 清理 ⭐。
- ⚠️ **`--pty` 需要 TTY**，在脚本/CI 里会失败 ⭐。
- **`--on-active=5min` 的时间格式**可以是 `5min`、`1h`、`30s`、`2h30min` ⭐。
- **`-p DynamicUser=yes` 会创建临时用户**（更隔离，但某些程序不兼容）⭐。
- **`systemd-run` 是「快速实验」的利器**，比手写 unit 文件快得多 ⭐⭐。
- **`--collect` 让单元结束后自动清理**（不留 failed 状态）⭐。

#### 相关命令
`systemctl` · `systemd-analyze calendar` · `at` · `crontab` · `systemd.special`

---

### systemd-cgls — cgroup 树

**常用度**：★★★☆☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

```bash
systemd-cgls [选项] [cgroup...]
```

| 选项 | 含义 |
|------|------|
| （无参） | 显示整个 cgroup 树 ⭐ |
| `-a` / `--all` | 显示所有（含空 cgroup） ⭐ |
| `-l N` / `--lines=N` | 限制输出行数 ⭐ |
| `--no-pager` | 不分页 ⭐ |
| `-k` | 显示内核线程 |
| `-u` / `--unit` | 用单元名而非 cgroup 路径 ⭐ |
| `-M 机器` | 容器/虚拟机 ⭐ |
| `--user-unit` | 用户级单元 |
| `--cgroup-id=bool` | 显示 ID |

```bash
# 场景：⭐ 看系统的 cgroup 层次（进程归属）⭐
$ systemd-cgls
Control group /:
-.slice
├─user.slice
│ ├─user-1000.slice
│ │ ├─user@1000.service
│ │ │ ├─app.slice
│ │ │ │ └─...
│ │ │ └─session-2.scope
│ │ │   ├─1234 gnome-terminal-server
│ │ │   └─1236 bash
├─init.scope
│ └─1 /sbin/init
└─system.slice
  ├─systemd-journald.service
  │ └─823 /usr/lib/systemd/systemd-journald
  ├─sshd.service
  │ └─892 sshd: /usr/sbin/sshd -D [listener]
  ├─nginx.service
  │ ├─1234 nginx: master process
  │ └─1236 nginx: worker process
  └─docker.service
    └─2345 /usr/bin/dockerd

# 场景：⭐ 用单元名显示（更易读）
$ systemd-cgls -u --no-pager | head -40
$ systemd-cgls -u nginx.service --no-pager

# 场景：⭐ 看某个单元下的所有进程
$ systemd-cgls /system.slice/nginx.service -l 20 --no-pager
$ systemd-cgls /user.slice -u --no-pager | head -30

# 场景：⭐ 看某个 cgroup 的资源占用
$ systemd-cgls --no-pager | head -60
$ cat /sys/fs/cgroup/system.slice/nginx.service/memory.current
$ cat /sys/fs/cgroup/system.slice/nginx.service/pids.current

# 场景：🔐 用 cgroup 排查「进程藏在哪」⭐⭐
$ # 找某个 PID 属于哪个 cgroup
$ cat /proc/1234/cgroup
0::/system.slice/nginx.service
$ systemctl status nginx | grep CGroup

$ # ⭐ 找不属于任何 systemd 单元的进程（可疑）
$ systemd-cgls --no-pager | grep -E '^\s+[0-9]+' | head -40
$ systemctl list-units --type=service --state=running --no-legend | awk '{print $1}' | head

# 场景：🔐 检查是否有进程逃出了 cgroup（异常）
$ # 正常情况：所有进程都在 system.slice 或 user.slice 下
$ systemd-cgls --no-pager -a | grep -E '^Control group' | head
$ ps -eo pid,cmd --no-headers | while read -r pid rest; do
>   cg=$(cat /proc/"$pid"/cgroup 2>/dev/null | cut -d: -f3)
>   [ -z "$cg" ] && echo "PID $pid 无 cgroup: $rest"
> done | head

# 场景：⭐ 查看容器/虚拟机的 cgroup
$ systemctl status systemd-nspawn@mycontainer
$ systemd-cgls -M mycontainer --no-pager | head -20
$ machinectl list

# 场景：🧪 用 cgroup 限制资源后观察
$ sudo systemd-run --unit=demo -p MemoryMax=100M --pty /bin/bash
# 另一个终端：
$ systemd-cgls /system.slice/demo.service --no-pager
$ cat /sys/fs/cgroup/system.slice/demo.service/memory.max
$ cat /sys/fs/cgroup/system.slice/demo.service/memory.current
$ cat /sys/fs/cgroup/system.slice/demo.service/cpu.max
$ cat /sys/fs/cgroup/system.slice/demo.service/pids.max
$ sudo systemctl stop demo

# 场景：🧪 查看 cgroup v2 的完整层次
$ mount | grep cgroup
cgroup2 on /sys/fs/cgroup type cgroup2 (rw,nosuid,nodev,noexec,relatime,nsdelegate)
$ ls /sys/fs/cgroup/
cgroup.controllers  cgroup.stat  init.scope  system.slice  user.slice
$ cat /sys/fs/cgroup/cgroup.controllers
cpuset cpu io memory hugetlb pids rdma misc
$ cat /sys/fs/cgroup/cgroup.subtree_control

# 场景：🔐 用 cgroup 找「隐藏的进程」（对抗进程隐藏）⭐
$ # ⭐ cgroup 视图与 ps 视图不一致时，说明有进程隐藏
$ ls /sys/fs/cgroup/system.slice/*/cgroup.procs 2>/dev/null | wc -l
$ for f in /sys/fs/cgroup/**/cgroup.procs; do
>   for pid in $(cat "$f" 2>/dev/null); do
>     [ -d "/proc/$pid" ] || echo "PID $pid 在 cgroup 里但 /proc 不可见: $f"
>   done
> done 2>/dev/null | head -20
$ # 反过来：/proc 里有但 cgroup 里没有
$ ps -eo pid --no-headers | while read -r p; do
>   grep -q "$p" /sys/fs/cgroup/**/cgroup.procs 2>/dev/null || echo "PID $p 不在任何 cgroup"
> done | head
```

#### 输出解读
输出是**树状结构**，显示 cgroup 层次与其中的进程：

```
Control group /:
-.slice                          ← 根
├─user.slice                     ← 用户会话
│ ├─user-1000.slice              ← UID 1000
│ │ └─session-2.scope
│ │   ├─1234 bash               ← PID + 命令
│ └─...
└─system.slice                   ← 系统服务
  └─nginx.service
    ├─1234 nginx: master
    └─1236 nginx: worker
```

**cgroup 的路径与进程的对应关系**可以在 `/proc/PID/cgroup` 里看到 ⭐。

#### 常见坑
- ⚠️ **`systemd-cgls` 的输出可能很长**，用 `-l` 限制行数或配 `head` ⭐。
- ⚠️ **cgroup v1 与 v2 的层次结构完全不同**，输出的可读性差异大 ⭐。
- ⚠️ **容器里看到的 cgroup 是命名空间内的视图**（`/sys/fs/cgroup` 挂载的是容器自己的层级）⭐。
- **`-u` 用单元名显示**（更易读），不加则显示 cgroup 路径 ⭐。
- **`systemd-cgls` 不显示资源占用**（那是 `systemd-cgtop` 的活）⭐。
- **`systemd-cgls` 是排查「进程归属哪个服务」的利器**（比 `ps` 更清晰）⭐⭐。
- **cgroup 是容器隔离的基础之一**（另一是 namespace）⭐。

#### 相关命令
`systemd-cgtop` · `/proc/PID/cgroup` · `systemd-run -p` · `systemd.slice`

---

### systemd-cgtop — cgroup 资源占用

**常用度**：★★★☆☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

```bash
systemd-cgtop [选项]
```

| 选项 | 含义 |
|------|------|
| （无参） | 实时显示 cgroup 资源（类 top） ⭐ |
| `-b` / `--batch` | 批处理模式（脚本用） ⭐ |
| `-n N` / `--iterations=N` | 刷新 N 次后退出 ⭐ |
| `-d 延迟` / `--delay=` | 刷新间隔（默认 1s） ⭐ |
| `-p` / `--order=path` | 按路径排序 |
| `--order=cpu` | 按 CPU 排序 ⭐ |
| `--order=memory` | 按内存排序 ⭐ |
| `--order=io` | 按 I/O 排序 ⭐ |
| `-k` | 显示内核线程 |
| `--depth=N` | 层次深度 ⭐ |
| `-M 机器` | 容器/虚拟机 |
| `--slice=名字` | 只看某 slice |
| `--no-pager` | 不分页 |

**交互键**（同 `top`）：`q` 退出、`p` 按路径、`c` 按 CPU、`m` 按内存、`i` 按 I/O、`+`/`-` 调整深度。

```bash
# 场景：⭐ 看哪个服务/容器占用最多资源
$ systemd-cgtop
Control Group                          Tasks   %CPU   Memory  Input/s Output/s
/                                         312   12.3     8.1G       0B     1.2M
system.slice                              180    8.5     5.2G       0B     1.1M
system.slice/docker.service                45    5.1     3.4G       0B     1.0M
system.slice/nginx.service                  5    1.2     12.3M       0B       0B
user.slice                                120    3.8     2.9G       0B     0.1M

# 场景：⭐ 批处理模式（脚本采集）
$ systemd-cgtop -b -n 1 --order=cpu
$ systemd-cgtop -b -n1 --order=memory | head -10
$ systemd-cgtop -b -n1 --order=io --depth=2 | head -10

# 场景：⭐ 按内存排序（找内存大户）
$ systemd-cgtop -b -n1 --order=memory --depth=1
$ systemd-cgtop --order=memory -d 2        # 交互式，2 秒刷新

# 场景：⭐ 只看某个 slice
$ systemd-cgtop --slice=user.slice
$ systemd-cgtop --slice=system.slice --depth=2 -b -n1 | head -15

# 场景：⭐ 看容器的资源占用
$ systemd-cgtop -M mycontainer -b -n1
$ machinectl list
$ # 或直接读 cgroup 文件
$ cat /sys/fs/cgroup/system.slice/docker-*/memory.current 2>/dev/null

# 场景：🔐 排查异常资源消耗（挖矿、反弹 shell）⭐⭐
$ systemd-cgtop -b -n1 --order=cpu | head -10
$ # ⭐ 若看到不明单元占用高 CPU → 立刻查
$ unit=$(systemd-cgtop -b -n1 --order=cpu | awk 'NR==4{print $1}')
$ echo "$unit"
$ systemctl status "$unit" --no-pager -l
$ systemctl cat "$unit"
$ ls -la /etc/systemd/system/ | grep -i "$(basename "$unit" .service)"

# 场景：🧪 用 cgroup 观察限流（CPUQuota 生效）
$ sudo systemd-run --unit=quota-demo -p CPUQuota=25% --pty /bin/bash
# 在 demo shell 里跑 CPU 密集任务
$ yes > /dev/null &
# 另一个终端：
$ systemd-cgtop -b -n3 -d1 | grep quota-demo
Control Group                    Tasks   %CPU   Memory
system.slice/quota-demo.service      3   24.9      2.1M
# ⭐ %CPU 稳定在 25% 左右，说明 CPUQuota 生效
$ sudo systemctl stop quota-demo

# 场景：🧪 观察内存限制与 OOM
$ sudo systemd-run --unit=mem-demo -p MemoryMax=100M --pty /bin/bash
# 在 demo shell 里分配内存
$ systemd-cgtop -b -n3 -d1 | grep mem-demo
$ cat /sys/fs/cgroup/system.slice/mem-demo.service/memory.events
$ sudo journalctl -u mem-demo -p err --no-pager | tail -10
$ sudo systemctl stop mem-demo

# 场景：⭐ 与 top 的差异
$ # top        → 按进程（进程可能跨 cgroup，且看不到 cgroup 聚合）
$ # cgtop      → 按 cgroup（服务/容器/用户会话的聚合视角） ⭐⭐
$ # ⭐ 多进程服务（nginx worker、java 线程）用 cgtop 看总量更准
$ systemd-cgtop -b -n1 --depth=1 --order=memory
$ ps -eo rss,comm --sort=-rss | head -5

# 场景：🔐 对比 cgtop 与实际进程（找隐藏进程）⭐
$ systemd-cgtop -b -n1 --order=cpu | head -5
$ ps -eo pid,pcpu,cmd --sort=-pcpu | head -5
$ # ⭐ 若 cgtop 显示某 cgroup 高 CPU 但 ps 找不到对应进程 → 有隐藏或已退出的进程
```

#### 输出解读
| 列 | 含义 |
|----|------|
| `Control Group` | cgroup 路径（缩进表示层次） ⭐ |
| `Tasks` | 进程/线程数（**> CPU 核数说明有并发**） ⭐ |
| `%CPU` | CPU 使用率 |
| `Memory` | 内存占用（RSS 类） ⭐ |
| `Input/s` / `Output/s` | 块设备 I/O ⭐ |

#### 常见坑
- ⚠️ **`systemd-cgtop` 的 `%CPU` 是相对全部 CPU 的百分比**（与 `top` 不同，后者可能 >100%）⭐。
- ⚠️ **`Tasks` 列是「进程 + 线程」总数**，Java 类应用这个数字会很大 ⭐。
- ⚠️ **`systemd-cgtop` 需要 root**（要读 `/sys/fs/cgroup`）⭐。
- ⚠️ **容器里的视图是容器自己的 cgroup 层次**（看不到宿主的其他容器）⭐。
- **`Memory` 列是 RSS 类统计，不含 page cache**（要看完整内存用 `memory.current`）⭐。
- **`-n1` 加 `-b` 是脚本采集的标准写法** ⭐。
- **`--depth` 控制显示的层次**（默认可能很深、输出很长）⭐。
- **cgroup v2 的 `memory.current` 含 page cache**，与 `cgtop` 的 `Memory` 列可能不一致 ⭐。

#### 相关命令
`systemd-cgls` · `top` · `systemd-run -p` · `systemd.resource-control`

---

### systemd-tmpfiles — 临时文件管理

**常用度**：★★★☆☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

```bash
systemd-tmpfiles [选项] 命令
```

| 命令 | 作用 |
|------|------|
| `--create` | 按配置创建文件/目录 ⭐ |
| `--clean` | 清理过期的文件/目录 ⭐ |
| `--remove` | 删除配置的文件/目录 ⭐ |
| `--create --remove` | 创建 + 删除 |

| 选项 | 含义 |
|------|------|
| `--prefix=路径` | 只处理该前缀下的 ⭐ |
| `--boot` | 只处理标记为「开机时」的 ⭐ |
| `--dry-run` | 只显示会做什么 ⭐⭐ |
| `-v` | 详细 ⭐ |
| `--cat-config` | **显示合并后的配置** ⭐⭐ |
| `--root=目录` | 用指定根目录（离线/chroot） ⭐ |

**配置目录**：`/usr/lib/tmpfiles.d/`、`/etc/tmpfiles.d/`（后者覆盖同名）、`/run/tmpfiles.d/`

**配置文件格式**：
```
类型  路径                        模式  属主  属组  时长  参数
d     /run/lock                   0755  root  root  -     -
d     /tmp                        1777  root  root  -     -
f     /run/motd                   0644  root  root  -     -
L     /var/lock                   -     -     -     -     /run/lock
r     /tmp/oldfile                -     -     -     -
X     /var/log/old                0700  root  root  30d   -
```

| 类型 | 作用 |
|------|------|
| `f` | 创建文件（不存在则创建，存在则不覆盖） ⭐ |
| `F` | 创建或清空文件 ⚠️ |
| `d` | 创建目录 ⭐ |
| `D` | 创建目录或清空内容 ⚠️ |
| `e` | 空目录或清空（保留目录本身） ⭐ |
| `v` | 创建 btrfs 子卷（若不存在） |
| `q` | 创建 btrfs 配额子卷 |
| `Q` | 同上（更高配额级别） |
| `p` / `P` | FIFO 管道 |
| `L` | **符号链接** ⭐ |
| `c` / `b` | 字符/块设备 |
| `C` | 递归复制目录树 |
| `r` | **删除文件/目录** ⭐ |
| `R` | 递归删除 ⚠️ |
| `x` | 排除（不清理） ⭐ |
| `X` | 排除（仅清理时） ⭐ |
| `t` | 设置扩展属性 |
| `a` / `A` | 设置 ACL |
| `z` / `Z` | 设置 SELinux 上下文 ⭐ |
| `h` | 设置文件属性（chattr） |

#### 实战示例
```bash
# 场景：⭐ 看系统当前的 tmpfiles 配置（合并结果）
$ systemd-tmpfiles --cat-config | head -40
# ⭐ 会显示所有配置文件按优先级合并后的内容

$ ls /usr/lib/tmpfiles.d/ | head
$ ls /etc/tmpfiles.d/ 2>/dev/null
$ cat /usr/lib/tmpfiles.d/tmp.conf
# 这是默认的 tmp 清理规则 ⭐

# 场景：⭐ 查看有哪些清理规则
$ grep -E '^\s*(e|X|x|r|R|d|D)\s' /usr/lib/tmpfiles.d/*.conf | head -20
$ systemd-tmpfiles --cat-config | grep -E '^\s*[eDdRr]'

# 场景：⭐ 干跑（看会清理什么）⭐⭐
$ sudo systemd-tmpfiles --clean --dry-run -v
$ sudo systemd-tmpfiles --clean --dry-run --prefix=/tmp -v
$ sudo systemd-tmpfiles --create --dry-run
$ # ⭐ 在生产上改清理策略前必须 dry-run

# 场景：⭐ 手动触发清理
$ sudo systemd-tmpfiles --clean
$ sudo systemd-tmpfiles --clean --prefix=/var/tmp
$ sudo systemd-tmpfiles --create --remove

# 场景：⭐ 只创建某个目录（不改全局）
$ sudo systemd-tmpfiles --create --prefix=/var/log/journal
$ ls -ld /var/log/journal
drwxr-sr-x 2 root systemd-journal 4096 ...
$ # ⭐ 这正是开启 journald 持久化日志的标准做法

# 场景：⭐ 加自己的 tmpfiles 规则
$ sudo tee /etc/tmpfiles.d/myapp.conf <<'EOF'
# 创建应用目录
d /run/myapp 0755 myapp myapp -
d /var/log/myapp 0750 myapp myapp -
d /var/lib/myapp 0700 myapp myapp -

# 开机时清空运行时目录
e /run/myapp 0755 myapp myapp -

# 清理 7 天前的日志
X /var/log/myapp
EOF
$ sudo systemd-tmpfiles --create
$ ls -ld /run/myapp /var/log/myapp /var/lib/myapp
$ sudo systemd-tmpfiles --clean --dry-run --prefix=/var/log/myapp

# 场景：⭐ 清理 /tmp 的策略（重要）
$ cat /usr/lib/tmpfiles.d/tmp.conf
#  This file is part of systemd.
q /tmp 1777 root root 10d
q /var/tmp 1777 root root 30d
# ⭐ q 表示「配额子卷」，时长是清理阈值
$ # 某些发行版用:
$ cat /etc/tmpfiles.d/tmp.conf 2>/dev/null
d /tmp 1777 root root 10d
d /var/tmp 1777 root root 30d

# 场景：⚠️ 用 tmpfiles 定时清理 /tmp（防磁盘满）
$ # ⭐ 注意：systemd-tmpfiles-clean.timer 会自动跑
$ systemctl status systemd-tmpfiles-clean.timer
$ systemctl list-timers systemd-tmpfiles-clean.timer
$ cat /usr/lib/systemd/system/systemd-tmpfiles-clean.timer | grep -E 'OnCalendar|OnBootSec'

# 场景：⭐ 为了安全清空 /tmp（重启时）
$ sudo tee /etc/tmpfiles.d/tmp-secure.conf <<'EOF'
# 重启时清空 /tmp
D! /tmp 1777 root root
D! /var/tmp 1777 root root
EOF
$ # ⭐ `D!` 里的 `!` 表示「只在开机时执行（--boot）」
$ sudo systemd-tmpfiles --boot --create --remove --dry-run

# 场景：🔐 用 tmpfiles 强制安全权限（加固）⭐
$ sudo tee /etc/tmpfiles.d/hardening.conf <<'EOF'
# 关键目录权限加固
z /etc/shadow 0000 root root -
z /etc/gshadow 0000 root root -
z /etc/sudoers 0440 root root -
z /etc/ssh/sshd_config 0600 root root -
z /etc/crontab 0600 root root -
d /var/log/journal 2755 root systemd-journal -
EOF
$ sudo systemd-tmpfiles --create
$ ls -l /etc/shadow /etc/sudoers
$ # ⚠️ 注意：z 设 SELinux 上下文，权限部分要小心别改错导致服务起不来

# 场景：🔐 排查被注入的 tmpfiles 规则（持久化手法）⭐⭐
$ ls -la /etc/tmpfiles.d/ /run/tmpfiles.d/ /usr/lib/tmpfiles.d/ | grep -vE '^total|^d'
$ find /etc/tmpfiles.d /run/tmpfiles.d -newermt '30 days ago' -ls 2>/dev/null
$ systemd-tmpfiles --cat-config | grep -E '^\s*(f|F|w|c|b|L)\s+/' | head -20
$ # ⭐ 关注：
$ #   f/F 创建文件（可能写 crontab、authorized_keys）
$ #   L   创建符号链接（可能劫持路径）
$ #   w   写内容（某些版本支持）
$ #   c/b 创建设备（可能创建危险的设备节点）

# 场景：🧪 离线操作另一个系统（救援模式）⭐
$ sudo systemd-tmpfiles --root=/mnt/sysroot --create
$ sudo systemd-tmpfiles --root=/mnt/sysroot --clean --dry-run

# 场景：🧪 手动清理 /tmp 与 /var/tmp（应急）
$ sudo systemd-tmpfiles --clean --prefix=/tmp --prefix=/var/tmp --dry-run
$ sudo systemd-tmpfiles --clean --prefix=/tmp --prefix=/var/tmp
$ df -h /tmp
```

#### 输出解读
配置行格式：`类型 路径 模式 属主 属组 时长 参数`

| 字段 | 含义 |
|------|------|
| 类型 | `d`/`f`/`r`/`X`…（见上表） ⭐ |
| 路径 | 绝对路径 |
| 模式 | 八进制权限（`-` = 不改） |
| 属主/属组 | 用户名/组名（`-` 或 `root`） |
| 时长 | 清理阈值（`10d`、`30d`、`-` = 不清理） ⭐ |
| 参数 | 类型相关的额外参数（如 `L` 的目标路径） |

**路径前缀的 `!`**：表示「只在 `--boot` 时处理」 ⭐
**路径末尾的 `/`**：表示「递归」 ⭐

#### 常见坑
- ⚠️⚠️ **`systemd-tmpfiles --clean` 会真的删除文件**。**改清理策略前必须 `--dry-run`** ⭐⭐。
- ⚠️ **`/etc/tmpfiles.d/` 里的同名文件会覆盖 `/usr/lib/tmpfiles.d/` 的**（不是合并，是整体替换）⭐。
- ⚠️ **`D`/`D!` 类型会清空目录内容**（`d` 只创建不清理）⚠️。
- ⚠️ **清理的「时长」判断依据是 atime/mtime/ctime 中最新的**（不是只看 mtime）⭐。
- ⚠️ **`/tmp` 在 tmpfs 上时重启自动清空**，`tmpfiles` 的清理规则对它意义不同 ⭐。
- **`systemd-tmpfiles-clean.timer` 会自动运行清理**（默认每天一次 + 开机后 15 分钟）⭐。
- **`--cat-config` 是理解当前生效配置的最佳方式**（比逐个 cat 文件靠谱）⭐⭐。
- **`z`/`Z` 是设 SELinux 上下文**（不是权限），在非 SELinux 系统上是空操作 ⭐。

#### 相关命令
`tmpfiles.d` · `systemd-tmpfiles-clean.timer` · `systemd-run` · `logrotate`

---

### systemd-cat — 把输出送入 journal

**常用度**：★★★☆☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

```bash
systemd-cat [选项] [命令 [参数...]]
命令 | systemd-cat [选项]
```

| 选项 | 含义 |
|------|------|
| `-t 标识` | 设置 syslog 标识（相当于 `logger -t`） ⭐ |
| `-p 优先级` | 设置优先级（`info`/`err`/`debug`…） ⭐ |
| `--level-prefix=bool` | 从输入行解析 `<N>` 前缀作为级别 ⭐ |
| `-u` | 把输出送到指定 unit 的日志 ⭐ |
| `--identifier=` | 同 `-t` |

```bash
# 场景：⭐ 把命令输出写入 journal
$ systemd-cat echo "hello from systemd-cat"
$ journalctl -t cat -n 3 --no-pager
$ # ⭐ 默认标识是 `cat`

# 场景：⭐ 带自定义标识与级别
$ systemd-cat -t mybackup echo "备份开始"
$ systemd-cat -t mybackup -p err echo "备份失败"
$ journalctl -t mybackup --no-pager
Sep 15 09:30:00 host mybackup[1234]: 备份开始

# 场景：⭐ 把整个脚本的输出收集到 journal
$ cat /tmp/job.sh
#!/bin/bash
systemd-cat -t job -p info bash -c '
  echo "任务开始"
  echo "处理中..."
  echo "任务完成"
'
$ journalctl -t job --no-pager

$ # ⭐ 更实用的写法（管道）
$ cat /tmp/task.sh
#!/bin/bash
{
  echo "开始: $(date -Is)"
  rsync -av /data/ /backup/ 2>&1
  echo "结束: $(date -Is), 退出码: $?"
} | systemd-cat -t rsync-backup -p info
$ sudo journalctl -t rsync-backup -f

# 场景：⭐ 在 cron 任务里把输出收集起来（解决 cron 邮件问题）
$ cat /etc/cron.d/backup
30 2 * * * root /usr/local/bin/backup.sh 2>&1 | systemd-cat -t cron-backup
$ # ⭐ 之后用 journalctl 查，不再依赖邮件
$ journalctl -t cron-backup --since today --no-pager

# 场景：⭐ 按行设置级别（前缀 `<N>`）
$ printf '<6>info level\n<3>error level\n' | systemd-cat --level-prefix=true -t leveltest
$ journalctl -t leveltest -o json --no-pager | jq -r '"\(.PRIORITY) \(.MESSAGE)"'
6 info level
3 error level

# 场景：⭐ 送进某个 unit 的日志
$ systemd-cat -u nginx.service echo "外部注入的日志"
$ journalctl -u nginx --no-pager -n 3

# 场景：⭐ 与 logger 的对比
$ logger -t mytag "from logger"
$ journalctl -t mytag -n 2 --no-pager
$ # ⭐ 差异：
$ #   logger   → 发给 syslog socket（可能被 rsyslog 处理/转发）⭐
$ #   systemd-cat → 直接发给 journal，能绑定 unit 与 stdin/stdout 流 ⭐
$ #   ⭐ systemd-cat 能保持「命令的 stdout/stderr 分别标记」

# 场景：⭐ 保留 stdout/stderr 的区别
$ bash -c 'echo out; echo err >&2' | systemd-cat -t streamtest
$ journalctl -t streamtest -o json --no-pager | jq -r '"\(.PRIORITY) \(.MESSAGE)"'
6 out           # stdout 是 info（6）
3 err           # stderr 是 err（3） ⭐

# 场景：🧪 长期运行的守护进程（不写日志文件）
$ cat /tmp/daemon.sh
#!/bin/bash
exec systemd-cat -t mydaemon -p info /usr/local/bin/mydaemon --foreground
$ # ⭐ 但更好的是直接写 systemd unit（StandardOutput=journal）

# 场景：🔐 审计脚本（把操作记录到 journal）⭐
$ cat /tmp/audited-op.sh
#!/bin/bash
log() { systemd-cat -t audit-op -p "$1" echo "$(whoami)@$(hostname): $2"; }
log info "开始执行敏感操作"
log warning "即将删除文件"
rm -v /tmp/testfile 2>&1 | systemd-cat -t audit-op -p warning
log info "操作完成"
$ journalctl -t audit-op --no-pager
$ # ⭐ 日志会进 journal（可被远端转发、可被 --verify 校验）
$ # ⚠️ 但 root 仍能清理 journal（见 journalctl 的坑）

# 场景：⭐ 与 systemd unit 的 StandardOutput 配合
$ cat /etc/systemd/system/myapp.service
[Service]
ExecStart=/usr/local/bin/myapp
StandardOutput=journal
StandardError=journal
SyslogIdentifier=myapp
$ # ⭐ 这才是「服务日志进 journal」的标准方式（不用 systemd-cat）
```

#### 输出解读
`systemd-cat` 会为每条消息设置：

| 字段 | 来源 |
|------|------|
| `SYSLOG_IDENTIFIER` | `-t` 的值（默认 `cat`） ⭐ |
| `PRIORITY` | `-p` 的值，或 `--level-prefix` 从输入解析 ⭐ |
| `_PID` / `_COMM` / `_EXE` | 调用者的信息 ⭐ |
| `MESSAGE` | 实际输出行 ⭐ |

**stdout 与 stderr 的默认级别**：

| 流 | 默认 PRIORITY |
|----|---------------|
| stdout | `6`（info） ⭐ |
| stderr | `3`（err） ⭐ |

#### 常见坑
- ⚠️ **`systemd-cat` 只适用于有 systemd 的系统**（容器里可能没有 journald）⭐。
- ⚠️ **默认标识是 `cat`**，不加 `-t` 会导致日志难以区分 ⭐。
- ⚠️ **`systemd-cat` 不会解决「日志被 root 清理」的问题**（日志还是在 journal 里）🔐。要防篡改需要远端转发 + FSS 签名 ⭐。
- ⚠️ **命令的退出码会被 `systemd-cat` 覆盖**（除非用 `--` 分隔或用 `-u`），要拿原退出码用 `PIPESTATUS` ⭐。
- **`logger` 更通用**（POSIX 风格，几乎所有 Unix 都有），`systemd-cat` 有 unit 绑定与流级别 ⭐。
- **`StandardOutput=journal` 比 `systemd-cat` 更合适**（服务场景）⭐。
- **`--level-prefix` 需要输入行有 `<N>` 前缀**（`<0>`–`<7>`）⭐。
- **`systemd-cat` 会阻塞到命令结束**（它在前台运行）⭐。

#### 相关命令
`journalctl` · `logger` · `systemd.service` 的 `StandardOutput` · `rsyslogd`

---

### loginctl — 登录会话管理

**常用度**：★★★★☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

```bash
loginctl [选项] 命令 [会话/用户...]
```

| 命令 | 作用 |
|------|------|
| `list-sessions` | 列出所有登录会话 ⭐⭐ |
| `list-users` | 列出有会话的用户 ⭐ |
| `session-status [会话]` | 会话详情 ⭐ |
| `user-status [用户]` | 用户详情 ⭐ |
| `show-session 会话` | 会话的机器可读属性 ⭐ |
| `show-user 用户` | 用户的机器可读属性 ⭐ |
| `terminate-session 会话` | 终止会话 ⚠️ |
| `terminate-user 用户` | 终止该用户所有会话 ⚠️ |
| `kill-session 会话` | 向会话内进程发信号 ⚠️ |
| `kill-user 用户` | 向用户所有进程发信号 ⚠️ |
| `activate 会话` | 把会话切到前台 ⭐ |
| `lock-session` / `unlock-session` | 锁定/解锁 ⭐ |
| `lock-sessions` | 锁定所有会话 |
| `flush-devices` | 清理设备分配 |
| `attach 会话` | 把当前终端接入会话 ⭐ |
| `enable-linger 用户` | **允许用户服务在未登录时运行** ⭐⭐ |
| `disable-linger 用户` | 关闭 linger ⭐ |

| 选项 | 含义 |
|------|------|
| `-a` | 显示完整信息 |
| `-p 属性` | 指定属性（`show-*`） ⭐ |
| `--value` | 只输出值 ⭐⭐ |
| `--no-pager` | 不分页 ⭐ |
| `-H` / `-M` | 远程 / 容器 |
| `--no-legend` | 不显示表头 ⭐ |
| `-l` | 不截断 ⭐ |

#### 实战示例
```bash
# 场景：⭐⭐ 查谁在登录（比 who/w 更可靠）
$ loginctl list-sessions
SESSION  UID USER  SEAT  TTY  STATE   IDLE SINCE
      2 1000 alice seat0 tty1 active  no   -
     12 1000 alice -     pts/0 active no   -
     15 1001 bob   -     pts/2 active yes  2min

3 sessions listed.

$ # ⭐ 对比 who：loginctl 能看到更多信息（seat、state、idle）
$ who
$ w

# 场景：⭐ 列出有会话的用户
$ loginctl list-users
 UID USER  LINGER STATE
1000 alice no     active
1001 bob   no     active

# 场景：⭐ 会话详情
$ loginctl session-status
Session 12 logged in as alice.
└─12345 sshd: alice [priv]
  └─12346 sshd: alice@pts/0
    └─12347 -bash
      └─12400 loginctl session-status

Sep 15 09:00:00 host systemd-logind[823]: New session 12 of user alice.
...

$ # ⭐ 未指定会话号时默认是「当前会话」

# 场景：⭐ 用户详情（含会话、linger）
$ loginctl user-status alice
alice (1000)
           Since: Tue 2026-09-15 08:00:00 CST; 1h 30min ago
           State: active
        Sessions: 12 15
          Linger: no
           Slice: user-1000.slice

# 场景：⭐⭐ 机器可读（脚本用）
$ loginctl show-session 12 -p Id -p User -p Type -p Remote -p TTY -p State
Id=12
User=1000
Type=tty
Remote=no
TTY=pts/0
State=active

$ loginctl show-session 12 --value -p Remote -p TTY -p Type
no
pts/0
tty
$ # ⭐ 一句话判断「这是本地还是远程会话」
$ loginctl show-session $(loginctl | awk '/alice/{print $1; exit}') --value -p Remote

# 场景：⭐⭐ 判断哪些登录是远程的（安全审计）
$ for s in $(loginctl list-sessions --no-legend | awk '{print $1}'); do
>   printf '%-8s %-10s remote=%-5s tty=%-10s type=%s\n' \
>     "$s" \
>     "$(loginctl show-session "$s" --value -p User)" \
>     "$(loginctl show-session "$s" --value -p Remote)" \
>     "$(loginctl show-session "$s" --value -p TTY)" \
>     "$(loginctl show-session "$s" --value -p Type)"
> done

# 场景：⭐⭐ enable-linger（用户服务持久化）
$ loginctl show-user alice --value -p Linger
no
$ sudo loginctl enable-linger alice
$ loginctl show-user alice --value -p Linger
yes
$ ls /var/lib/systemd/linger/
alice
$ # ⭐ 现在 alice 的用户级服务会在未登录时也运行（且开机自启）
$ systemctl --user status myapp
$ sudo systemctl status user@1000.service    # ⭐ 用户管理器服务

$ sudo loginctl disable-linger alice

# 场景：⚠️ 终止会话（踢人）
$ sudo loginctl terminate-session 15
$ sudo loginctl terminate-user bob              # ⚠️ 终止 bob 的所有会话
$ sudo loginctl list-sessions

# 场景：⚠️ 向会话内进程发信号
$ sudo loginctl kill-session 15 SIGTERM
$ sudo loginctl kill-user bob SIGKILL

# 场景：⭐ 锁定会话（安全，离开时用）
$ loginctl lock-session                # 锁当前会话
$ loginctl lock-sessions               # 锁所有
$ loginctl unlock-session

# 场景：⭐ 把当前终端接入已有会话（调试/接管）
$ loginctl attach 12
$ # ⭐ 需要 root 或该会话的引用

# 场景：🔐 完整的登录审计脚本 ⭐⭐
$ cat /tmp/login-audit.sh
#!/bin/bash
echo "=== 当前会话 ==="
printf '%-8s %-10s %-8s %-6s %-10s %-8s %s\n' SESSION USER REMOTE TTY TYPE STATE SINCE
for s in $(loginctl list-sessions --no-legend | awk '{print $1}'); do
  printf '%-8s %-10s %-8s %-6s %-10s %-8s %s\n' \
    "$s" \
    "$(loginctl show-session "$s" --value -p Name)" \
    "$(loginctl show-session "$s" --value -p Remote)" \
    "$(loginctl show-session "$s" --value -p TTY)" \
    "$(loginctl show-session "$s" --value -p Type)" \
    "$(loginctl show-session "$s" --value -p State)" \
    "$(loginctl show-session "$s" --value -p Timestamp | head -c 19)"
done

echo
echo "=== 有 linger 的用户（服务在未登录时也跑）==="
loginctl list-users --no-legend | while read -r uid user linger state; do
  [ "$linger" = "yes" ] && echo "$user (UID $uid) linger=yes ⭐"
done

echo
echo "=== 有活跃会话的用户 ==="
loginctl list-users --no-legend | awk '{print $2}'

# 场景：🔐 找异常会话（长时间 idle 的远程会话）⭐
$ loginctl list-sessions --no-legend | while read -r s uid user seat tty state idle since; do
>   remote=$(loginctl show-session "$s" --value -p Remote)
>   [ "$remote" = "yes" ] && printf '⚠️ 远程会话 %s: %s tty=%s state=%s idle=%s\n' "$s" "$user" "$tty" "$state" "$idle"
> done

# 场景：🔐 检查 linger（持久化后门之一）⭐
$ ls -la /var/lib/systemd/linger/ 2>/dev/null
$ cat /var/lib/systemd/linger/* 2>/dev/null
$ # ⭐ 攻击者可能 enable-linger 让用户级服务持久化
$ #   配合 ~/.config/systemd/user/*.service 实现隐蔽持久化

# 场景：🧪 对比 who/w/loginctl 的可见性
$ cat /tmp/session-compare.sh
#!/bin/bash
echo "=== who ==="
who
echo "=== w ==="
w -h
echo "=== loginctl ==="
loginctl list-sessions
echo "=== ps 里的 sshd 会话 ==="
ps -eo pid,user,tty,cmd | grep '[s]shd:'
```

#### 输出解读
`list-sessions` 的列：

| 列 | 含义 |
|----|------|
| `SESSION` | 会话 ID（数字） ⭐ |
| `UID` / `USER` | 用户 |
| `SEAT` | 座位（`seat0` = 本地物理终端） ⭐ |
| `TTY` | 终端（`tty1` 本地，`pts/N` 伪终端 = SSH/终端模拟器） ⭐ |
| `STATE` | `active` / `online` / `closing` |
| `IDLE` | 是否空闲（`no` = 有活动） ⭐ |
| `SINCE` | 空闲起始时刻 |

`show-session` 的关键属性：

| 属性 | 含义 |
|------|------|
| `Remote` | **是否远程会话（`yes`/`no`）** ⭐⭐ |
| `RemoteHost` / `RemoteUser` | 远程主机/用户（如有） ⭐ |
| `Type` | `tty`（本地）/ `x11` / `wayland` / `unspecified` |
| `Class` | `user` / `greeter` / `lock-screen` |
| `TTY` | 终端设备 |
| `Service` | 关联的服务（`sshd.service`） ⭐ |
| `State` | `active` / `online` / `closing` |
| `IdleHint` / `IdleSinceHint` | 空闲提示 ⭐ |
| `Active` / `Timestamp` | 是否活动 / 开始时间 |
| `Display` | 显示（图形会话） |

`show-user` 的关键属性：

| 属性 | 含义 |
|------|------|
| `Linger` | **是否允许离线运行用户服务** ⭐⭐ |
| `State` | `active` / `online` / `lingering` / `closing` ⭐ |
| `Sessions` | 该用户的会话列表 ⭐ |
| `Slice` | cgroup 路径（`user-1000.slice`） |
| `RuntimePath` / `StatePath` | 用户运行时/状态目录 |

#### 常见坑
- ⚠️ **`loginctl` 只显示「systemd-logind 管理的会话」**（本地登录、SSH、图形登录）。**`su`/`sudo -i` 创建的不算新会话** ⭐。
- ⚠️ **会话号在注销后会变**，不要当持久标识 ⭐。
- ⚠️ **`enable-linger` 需 root 或该用户自己有权限** ⭐。
- ⚠️ **`terminate-session` 会立刻杀掉会话内的所有进程**（不优雅，可能丢数据）⚠️。
- ⚠️ **`kill-user` 会杀掉该用户的**所有**进程**（包括后台任务、用户服务）⚠️。
- **容器的会话在宿主看不到**（logind 不在容器里运行）⭐。
- **`Remote=yes` 不一定是 SSH**（也可能是其他远程显示协议），要结合 `Service` 属性判断 ⭐。
- **`loginctl` 比 `who`/`w` 更准确**（`who` 依赖 utmp，会被某些会话类型跳过）⭐⭐。
- **`enable-linger` 是实现「用户级服务开机自启」的唯一方式**（否则用户服务只在登录期间运行）⭐⭐。

#### 相关命令
`who` · `w` · `last` · `systemctl --user` · `systemd-logind` · `pam_systemd`

---

### hostnamectl — 主机名与系统标识

**常用度**：★★★★☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

> 该命令的详细说明见 [`07-系统信息与内核.md`](07-系统信息与内核.md#hostnamectl--主机名与系统标识)。这里补充**系统管理视角**的用法。

```bash
hostnamectl [命令]
```

| 命令 | 作用 |
|------|------|
| （无参） | 系统信息总览（主机名、机箱、虚拟化、OS、内核） ⭐ |
| `set-hostname 名字` | 设置静态主机名 ⭐ |
| `set-hostname 名字 --pretty` | 设置展示名（可含空格） ⭐ |
| `set-icon-name 名字` | 图标名（`computer-vm`、`computer-laptop`） ⭐ |
| `set-chassis 类型` | 机箱类型 ⭐ |
| `set-deployment 环境` | 部署环境（`production`/`staging`） ⭐ |
| `set-location 位置` | 位置（机房/机柜） ⭐ |
| `--static` / `--transient` / `--pretty` | 只看/设置某类主机名 ⭐ |
| `--json=格式` | JSON 输出 ⭐ |

```bash
# 场景：⭐ 系统信息总览（包含发行版与虚拟化）
$ hostnamectl
   Static hostname: web01
         Icon name: computer-vm
           Chassis: vm
        Machine ID: 1234567890abcdef1234567890abcdef
           Boot ID: fedcba0987654321fedcba0987654321
    Virtualization: kvm
  Operating System: Ubuntu 24.04.1 LTS
            Kernel: Linux 7.2.3-arch1-3
      Architecture: x86-64
   Hardware Vendor: QEMU
     Hardware Model: Standard PC _Q35 + ICH9, 2009_
   Firmware Version: 1.16.3-1

# 场景：⭐ 只取值（脚本用）
$ hostnamectl --static
web01
$ hostnamectl --json=short | jq -r '.Hostname'
web01
$ hostnamectl --json=short | jq -r '.Virtualization'
kvm
$ hostnamectl --json=short | jq -r '."Operating System"'

# 场景：⭐ 改主机名（会自动更新 /etc/hostname 与内核）
$ sudo hostnamectl set-hostname web01
$ hostname                      # ⭐ 立即生效
$ cat /etc/hostname             # ⭐ 持久化
$ grep -n "$(hostname)" /etc/hosts   # ⚠️ 记得同步（否则 sudo 变慢）

# 场景：⭐ 部署环境与位置（资产管理）
$ sudo hostnamectl set-deployment production
$ sudo hostnamectl set-location 'DC1-Rack12-U20'
$ hostnamectl | grep -iE 'deployment|location'
$ cat /etc/machine-info

# 场景：🔐 判断是否为虚拟机（安全工作第一步）⭐⭐
$ hostnamectl | grep -i virtualization
    Virtualization: kvm
$ # ⭐ 空 = 物理机；kvm/vmware/docker/lxc/openvz/podman = 虚拟化
$ systemd-detect-virt
$ systemd-detect-virt --vm            # 只在虚拟机里返回 0
$ hostnamectl --json=short | jq -r '.Virtualization'

# 场景：🔐 Machine ID 与克隆检测 ⭐
$ cat /etc/machine-id
1234567890abcdef1234567890abcdef
$ # ⭐ 克隆虚拟机时两台机器会有相同 machine-id → 日志、DHCP、某些软件冲突
$ sudo rm -f /etc/machine-id && sudo systemd-machine-id-setup
$ cat /etc/machine-id

# 场景：🔐 用 Machine ID 定位 journald 日志目录（取证）⭐
$ ls /var/log/journal/
1234567890abcdef1234567890abcdef/
$ SRC=/mnt/evidence
$ ls "$SRC/var/log/journal/"
$ sudo journalctl -D "$SRC/var/log/journal" --list-boots

# 场景：🔐 检查主机名是否可疑（伪装成系统进程的手法）
$ hostnamectl --static
$ # ⭐ 攻击者有时把主机名改成看起来无害的名字，或反之

# 场景：🧪 完整的环境识别脚本 ⭐
$ cat /tmp/env-id.sh
#!/bin/bash
echo "== 主机 =="
hostnamectl --static
echo "== 虚拟化 =="
echo "hostnamectl:  $(hostnamectl --json=short 2>/dev/null | jq -r '.Virtualization // "none"')"
echo "systemd-detect-virt: $(systemd-detect-virt 2>/dev/null || echo none)"
echo "dmidecode:     $(sudo dmidecode -s system-vendor 2>/dev/null || echo '需 root')"
grep -qiE 'hypervisor|kvm|qemu' /proc/cpuinfo && echo "/proc/cpuinfo: 有 hypervisor 标志"
echo "== 容器检测 =="
[ -f /.dockerenv ] && echo "存在 /.dockerenv → Docker 容器"
grep -qE 'docker|containerd' /proc/1/cgroup 2>/dev/null && echo "/proc/1/cgroup 有 docker"
grep -qE 'lxc|kubepods' /proc/1/cgroup 2>/dev/null && echo "/proc/1/cgroup 有 lxc/k8s"
echo "== 系统 =="
cat /etc/os-release | grep PRETTY_NAME
uname -a
```

#### 输出解读
**三类主机名的对比**：

| 类型 | 存储 | 可见性 | 用途 |
|------|------|--------|------|
| `static` | `/etc/hostname` | 内核 + 网络 | **对外标识** ⭐⭐ |
| `transient` | 内核运行时 | 内核 | DHCP/mDNS 临时设置 ⭐ |
| `pretty` | `/etc/machine-info` | 仅展示 | 给人看（可含空格） ⭐ |

优先级：**应用通常读 `static`**；`hostname` 命令读内核的（可能是 transient） ⭐。

#### 常见坑
- ⚠️ **手改 `/etc/hostname` 不生效于当前会话**（要 `hostnamectl set-hostname` 或重启）⭐⭐。
- ⚠️ **改主机名后忘记改 `/etc/hosts`** → `sudo` 会因 DNS 超时变慢、报 `unable to resolve host` ⭐。
- ⚠️ **克隆虚拟机时不重置 `machine-id`** 会导致 DHCP、日志、监控混淆，甚至网络冲突 🔐⭐。
- ⚠️ **`pretty` 主机名不能含换行**（会被拒绝），且**不影响 `hostname` 命令** ⭐。
- **`hostnamectl` 只在 systemd 系统上可用**（Alpine 用 `hostname` 与 `/etc/hostname`）⭐。
- **容器里 `hostnamectl` 通常不可用**（没有 logind/systemd 实例）⭐。
- **`Virtualization` 字段在容器里是 `docker`/`podman`/`lxc`**，在虚拟机里是 `kvm`/`vmware` ⭐。
- **`Hardware Vendor`/`Model` 在虚拟机上显示的是 hypervisor 的伪装值** ⭐。

#### 相关命令
`hostname` · `uname` · `dmidecode` · `systemd-detect-virt` · `/etc/machine-info`

---

### timedatectl — 时间与时区

**常用度**：★★★★☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

> 该命令的完整说明见 [`07-系统信息与内核.md`](07-系统信息与内核.md#timedatectl--时间与时区管理)。这里补充**系统管理视角**的要点。

| 命令 | 作用 |
|------|------|
| `status` / （无参） | 时间与时区状态 ⭐ |
| `set-time '时间'` | 设置时间（**需先关 NTP**） ⚠️ |
| `set-timezone 时区` | 设置时区 ⭐ |
| `list-timezones` | 列出时区 ⭐ |
| `set-ntp true/false` | 启用/禁用 NTP ⭐ |
| `set-local-rtc 0/1` | RTC 用 UTC（`0`）还是本地时间（`1`） ⭐ |
| `timesync-status` | 同步详情 ⭐ |
| `show` | 机器可读 ⭐ |

```bash
# 场景：⭐ 状态（含 NTP 与 RTC 状态）
$ timedatectl
               Local time: Tue 2026-09-15 09:30:00 CST
           Universal time: Tue 2026-09-15 01:30:00 UTC
                 RTC time: Tue 2026-09-15 01:30:00
                Time zone: Asia/Shanghai (CST, +0800)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no

# 场景：⭐ 脚本检查 NTP 同步状态（监控告警）⭐⭐
$ timedatectl show -p NTPSynchronized --value
yes
$ [ "$(timedatectl show -p NTPSynchronized --value)" = "yes" ] || echo "⚠️ 时钟未同步"
$ timedatectl show -p NTP --value
yes

# 场景：⭐ 查看 NTP 同步详情（哪个服务器、偏差多大）
$ timedatectl timesync-status
       Server: 203.0.113.10 (ntp.example.com)
Poll interval: 34min 8s (min: 32s; max 34min 8s)
         Leap: normal
      Version: 4
      Stratum: 2
    Reference: 12345678
    Precision: 1us
    Root delay: 12.345ms
     Root dispersion: 1.234ms
  Packet count: 6
     Frequency: +12.345ppm
         Delay: 12.345ms
      Jitter: 0.123ms
$ timedatectl show-timesync --all | head -20

# 场景：⭐ 改时区（应用环境迁移）
$ sudo timedatectl set-timezone Asia/Shanghai
$ timedatectl list-timezones | grep -iE 'shanghai|tokyo|utc'
$ ls -l /etc/localtime
lrwxrwxrwx ... /etc/localtime -> /usr/share/zoneinfo/Asia/Shanghai

# 场景：⚠️ 设置时间（需先关 NTP）
$ sudo timedatectl set-ntp false
$ sudo timedatectl set-time '2026-09-15 09:30:00'
$ sudo timedatectl set-time '2026-09-15'              # 只改日期
$ sudo timedatectl set-time '09:30:00'                # 只改时间
$ sudo timedatectl set-ntp true

# 场景：⭐ RTC 与 UTC（双系统时间错乱的根源）⭐⭐
$ timedatectl set-local-rtc 0        # ⭐ RTC 存 UTC（推荐）
$ timedatectl set-local-rtc 1        # ⚠️ RTC 存本地时间（Windows 默认）
$ sudo hwclock --systohc --utc       # 把系统时间写入 RTC
$ sudo hwclock --show
$ sudo hwclock --systohc             # 系统时间 → 硬件时钟
$ sudo hwclock --hctosys             # 硬件时钟 → 系统时间

# 场景：🔐 时间偏移的取证意义 ⭐⭐
$ # ⚠️ 如果系统时间被手动改过，日志时间线就不可信
$ # 检查时间同步历史（journald 会记录时间跳变）
$ journalctl --since "7 days ago" --no-pager | grep -iE 'time (jump|change)|synchroniz' | head -20
$ # ⭐ 未同步的系统上，日志时间的交叉验证必须谨慎
$ timedatectl show -p NTPSynchronized --value
$ chronyc tracking 2>/dev/null | head -10
$ ntpq -p 2>/dev/null | head -10

# 场景：🔐 检查 NTP 服务是哪个（timesyncd / chrony / ntpd）⭐
$ systemctl status systemd-timesyncd chronyd ntp ntpsec 2>/dev/null | grep -E '(●|Active:)'
$ # ⚠️ 多个 NTP 服务同时运行会冲突
$ ps -eo pid,cmd | grep -E '[c]hronyd|[n]tpd|[s]ystemd-timesyncd'
$ ss -tunlp | grep ':123'              # NTP 端口

# 场景：🔐 NTP 的安全风险（放大攻击 / 未授权修改时间）
$ # 1. NTP 服务器应限制（ntp.conf 的 restrict 指令）⭐
$ grep -E '^restrict|^server|^pool' /etc/ntp.conf /etc/chrony/chrony.conf 2>/dev/null
$ # 2. 检查是否有 notrap / noquery / nopeer
$ # 3. 时间被篡改会让证书验证、日志、Kerberos 全部失效

# 场景：🧪 完整的时间健康检查脚本 ⭐
$ cat /tmp/time-check.sh
#!/bin/bash
echo "=== 时间状态 ==="
timedatectl
echo
echo "=== NTP 同步 ==="
if [ "$(timedatectl show -p NTPSynchronized --value 2>/dev/null)" != "yes" ]; then
  echo "⚠️ 时钟未同步（NTPSynchronized != yes）"
fi
echo "=== 时间源 ==="
systemctl is-active systemd-timesyncd chronyd ntp 2>/dev/null | paste -sd' '
echo "=== 与公共 NTP 的偏移（粗略）==="
timeout 10 sntp -S 2>/dev/null ntp.example.com 2>/dev/null || echo "无 sntp"
echo "=== RTC ==="
sudo hwclock --show 2>/dev/null
timedatectl show -p LocalRTC --value
```

#### 输出解读
| 字段 | 含义 | 期望值 |
|------|------|--------|
| `System clock synchronized` | NTP 是否已同步 | `yes` ⭐ |
| `NTP service` | NTP 服务状态 | `active` ⭐ |
| `RTC in local TZ` | RTC 是否存本地时间 | **`no`（存 UTC）** ⭐ |
| `Time zone` | 时区 | 与业务一致 |

`timesync-status` 的关键指标：

| 字段 | 含义 | 关注 |
|------|------|------|
| `Stratum` | 层级 | `1` 最准，`2`+ 是转发 ⭐ |
| `Frequency` | 本机时钟漂移率（ppm） | 稳定的小值 ⭐ |
| `Root delay` | 到根时钟的延迟 | 越小越好 |
| `Jitter` | 抖动 | **持续大说明时钟不稳定**（虚拟机常见）⭐ |

#### 常见坑
- ⚠️ **`set-time` 在 NTP 启用时被拒绝**（`Automatic time synchronization is enabled`）。先 `set-ntp false` ⭐。
- ⚠️ **`RTC in local TZ: yes` 是双系统时间错乱的元凶**（Windows 把 RTC 当本地时间）。**统一为 UTC** ⭐。
- ⚠️ **手动改时间会破坏日志的因果顺序**，且会被 NTP 覆盖。**取证时更要避免** 🔐。
- ⚠️ **容器里 `timedatectl` 通常不可用**（报 `Failed to connect to bus`）。容器共享宿主时钟 ⭐。
- ⚠️ **多个 NTP 服务同时运行会冲突**，要禁用其中一个 ⭐。
- **`timedatectl` 是 `systemd-timesyncd` 的前端**，如果用 `chrony`/`ntpd`，`set-ntp` 的语义会不同 ⭐。
- **虚拟机 `Jitter` 大**是因为宿主调度延迟，属正常现象 ⭐。
- **验证时间的方法**：`date -u` 与外部时间源对比（`sntp`、`chronyc tracking`、`curl -sI https://example.com | grep -i '^date'`）⭐。

#### 相关命令
`date` · `hwclock` · `chronyc` · `ntpq` · `systemd-timesyncd` · `systemd-timedated`

---

### localectl — 语言与键盘布局

**常用度**：★★★☆☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

```bash
localectl [命令]
```

| 命令 | 作用 |
|------|------|
| （无参） / `status` | 显示语言、键盘、X11 布局 ⭐ |
| `set-locale 变量=值...` | 设置系统语言 ⭐ |
| `list-locales` | 列出可用语言 ⭐ |
| `set-keymap 布局 [变体]` | 设置控制台键盘 ⭐ |
| `list-keymaps` | 列出控制台键盘布局 ⭐ |
| `list-keymaps --no-pager` | 同上 ⭐ |
| `set-x11-keymap 布局 [型号] [变体] [选项]` | 设置 X11 键盘 ⭐ |
| `list-x11-keymap-layouts` | 列出 X11 布局 ⭐ |
| `list-x11-keymap-variants 布局` | 列出变体 ⭐ |
| `list-x11-keymap-models` | 列出键盘型号 ⭐ |
| `list-x11-keymap-options` | 列出选项 ⭐ |
| `--no-pager` | 不分页 ⭐ |
| `--no-convert` | 不自动转换（键盘↔X11） ⭐ |

```bash
# 场景：⭐ 当前语言与键盘设置
$ localectl
   System Locale: LANG=en_US.UTF-8
       VC Keymap: us
      X11 Layout: us
       X11 Model: pc105
     X11 Variant: -
     X11 Options: -

# 场景：⭐ 改系统语言（持久化）
$ sudo localectl set-locale LANG=en_US.UTF-8
$ sudo localectl set-locale LANG=zh_CN.UTF-8
$ sudo localectl set-locale LANG=zh_CN.UTF-8 LC_TIME=C      # ⭐ 多变量
$ cat /etc/locale.conf
LANG=en_US.UTF-8
$ # ⚠️ 需要对应的 locale 已生成（locale-gen / localedef）
$ locale -a | grep -i 'en_US.utf8'

# 场景：⚠️ 语言未生成时（会显示为问号）
$ sudo localectl set-locale LANG=zh_CN.UTF-8
$ locale
LANG=zh_CN.UTF-8
LC_ALL=
$ # 若中文显示乱码或问号：
$ sudo localedef -i zh_CN -f UTF-8 zh_CN.UTF-8
$ # Debian/Ubuntu:
$ sudo grep -q '^zh_CN.UTF-8' /etc/locale.gen || echo 'zh_CN.UTF-8 UTF-8' | sudo tee -a /etc/locale.gen
$ sudo locale-gen
$ # ⭐ 也可以直接手写 /etc/locale.conf（localectl 只是前端）

# 场景：⭐ 列出可用语言
$ localectl list-locales | head -20
$ localectl list-locales | grep -iE '^zh|^en'
$ localectl list-locales | wc -l

# 场景：⭐ 查看可用键盘布局
$ localectl list-keymaps | head -20
$ localectl list-keymaps | grep -iE '^(us|cn|de|fr)'
$ localectl list-keymaps | wc -l

# 场景：⭐ 设置控制台键盘（TTY 上生效）
$ sudo localectl set-keymap us
$ sudo localectl set-keymap de-latin1
$ # ⭐ set-keymap 会自动同步 X11 布局（除非 --no-convert）

# 场景：⭐ 设置 X11 键盘（图形界面）
$ sudo localectl set-x11-keymap us
$ sudo localectl set-x11-keymap de pc105 nodeadkeys
$ sudo localectl set-x11-keymap us pc105 intl
$ sudo localectl set-x11-keymap '' '' '' caps:swapescape          # ⭐ 只改选项
$ sudo localectl set-x11-keymap fr pc105 '' grp:alt_shift_toggle  # ⭐ 多布局切换键
$ localectl list-x11-keymap-variants us
$ localectl list-x11-keymap-options | grep -iE 'caps|compose'

# 场景：🔐 键盘布局对安全的意义（口令输入）
$ # ⚠️ 若键盘布局设错，输入的口令会与实际不符（尤其符号键位置）
$ # ⭐ 服务器（无图形界面）通常只需要 us
$ # ⭐ 排查「口令明明对却登录不上」时要检查 keymap

# 场景：🔐 让某些按键更安全（禁用 SysRq、Ctrl+Alt+Del）
$ # 相关配置：
$ cat /etc/sysctl.d/*.conf 2>/dev/null | grep kernel.sysrq
$ sudo sysctl -w kernel.sysrq=0                   # 临时禁用 SysRq
$ echo 'kernel.sysrq = 0' | sudo tee /etc/sysctl.d/99-sysrq.conf
$ # ⭐ Ctrl+Alt+Del 的屏蔽用 systemctl mask ctrl-alt-del.target
$ sudo systemctl mask ctrl-alt-del.target

# 场景：⭐ 只改控制台不改 X11
$ sudo localectl --no-convert set-keymap de

# 场景：🧪 检查地区设置的完整状态
$ cat /tmp/locale-check.sh
#!/bin/bash
echo "=== localectl ==="
localectl
echo
echo "=== /etc/locale.conf ==="
cat /etc/locale.conf 2>/dev/null || echo "(不存在)"
echo
echo "=== 进程环境里的 locale ==="
echo "LANG=$LANG  LC_ALL=$LC_ALL"
locale | head -5
echo
echo "=== 可用的相关 locale ==="
locale -a | grep -iE "$(echo "${LANG:-en_US}" | cut -d. -f1)" || echo "(未生成)"
echo
echo "=== /etc/default/locale（Debian 传统）==="
cat /etc/default/locale 2>/dev/null || echo "(不存在)"
echo
echo "=== /etc/vconsole.conf（键盘）==="
cat /etc/vconsole.conf 2>/dev/null || echo "(不存在)"

# 场景：🔐 检查 SSH 转发 locale 警告的根源 ⭐
$ ssh user@server
bash: warning: setlocale: LC_ALL: cannot change locale (en_US.UTF-8)
$ # ⭐ 原因：本地 SSH 转发了 LC_*，但服务器上没有该 locale
$ # 解决 1：在服务器上生成
$ sudo localedef -i en_US -f UTF-8 en_US.UTF-8
$ # 解决 2：客户端不转发
$ ssh -o SendEnv=-LC_ALL user@server
$ grep -E 'SendEnv|AcceptEnv' /etc/ssh/sshd_config ~/.ssh/config
$ # 解决 3：服务器上设一个存在的 locale
$ sudo localectl set-locale LANG=C.UTF-8
```

#### 输出解读
`localectl` 的输出分三块：

| 块 | 字段 | 含义 |
|----|------|------|
| Locale | `System Locale` | `LANG` 等变量 ⭐ |
| VC | `VC Keymap` | 虚拟控制台（TTY）的键盘布局 ⭐ |
| X11 | `X11 Layout` / `Model` / `Variant` / `Options` | 图形界面的键盘布局 ⭐ |

**相关的配置文件**：

| 文件 | 内容 |
|------|------|
| `/etc/locale.conf` | systemd 系统的 locale ⭐ |
| `/etc/default/locale` | Debian/Ubuntu 传统位置 ⭐ |
| `/etc/vconsole.conf` | 控制台键盘（`KEYMAP=`） ⭐ |
| `/etc/X11/xorg.conf.d/00-keyboard.conf` | X11 键盘（localectl 生成） ⭐ |
| `/etc/locale.gen` | Debian/Ubuntu 要生成的 locale 列表 ⭐ |

#### 常见坑
- ⚠️ **`localectl set-locale` 只写配置，不生成 locale**。要用 `localedef` 或 `locale-gen` 生成，否则会出警告与乱码 ⭐。
- ⚠️ **`set-keymap` 默认会同步 X11 布局**（`--no-convert` 可禁用）⭐。
- ⚠️ **改 locale 后已运行的进程不受影响**（要重新登录或重启服务）⭐。
- ⚠️ **`LC_ALL` 会覆盖 `LANG`**，别同时设冲突的值 ⭐。
- ⚠️ **键盘布局设错会导致口令输入错误**（特殊符号位置不同），排查登录问题时值得检查 🔐。
- **容器里 `localectl` 通常不可用**（要手写 `/etc/locale.conf` 或设环境变量）⭐。
- **`C.UTF-8` 是最省事的 locale**（不需要生成，支持 UTF-8）⭐。
- **`localectl` 是 `systemd-localed` 的前端**，配置文件才是真实的 ⭐。

#### 相关命令
`locale` · `locale-gen` · `localedef` · `setxkbmap` · `/etc/locale.conf`

---

### machinectl — 容器与虚拟机管理

**常用度**：★★★☆☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

```bash
machinectl [选项] 命令 [名字...]
```

| 命令 | 作用 |
|------|------|
| `list` | 列出所有机器（容器/虚拟机） ⭐ |
| `status 名字` | 机器详情 ⭐ |
| `show 名字` | 机器可读属性 ⭐ |
| `start 名字` | 启动容器（systemd-nspawn） ⭐ |
| `stop` / `reboot` / `poweroff` | 停止/重启/关机 ⭐ |
| `terminate` | **强制终止** ⚠️ |
| `kill` | 向机器内进程发信号 ⚠️ |
| `login 名字` | **登录到机器（打开 shell）** ⭐⭐ |
| `shell 名字 [命令]` | 在机器里执行命令 ⭐⭐ |
| `enable` / `disable` | 开机自启 ⭐ |
| `clone 源 目标` | 克隆 ⭐ |
| `rename` / `remove` | 重命名 / 删除 ⚠️ |
| `image-list` | 列出可用的镜像 ⭐ |
| `image-pull-tar` | 从 tar 导入镜像 ⭐ |
| `image-pull-raw` | 从磁盘镜像导入 ⭐ |
| `pull-tar URL` | 从 URL 下载 tar 镜像 ⭐ |
| `copy-to` / `copy-from` | 在机器与主机间拷文件 ⭐ |
| `bind 源 目标 名字` | 绑定挂载目录（运行时） ⭐ |
| `bind --read-only` | 只读绑定 ⭐ |
| `list-images` / `image-status` | 镜像管理 ⭐ |
| `show-image` | 镜像详情 |
| `clean` | 清理未使用的镜像 ⭐ |
| `list-transfers` / `cancel-transfer` | 传输管理 |

| 选项 | 含义 |
|------|------|
| `-M 名字` | 指定机器（隐式参数） ⭐ |
| `-H 主机` | 远程（通过 SSH） |
| `--no-pager` | 不分页 ⭐ |
| `-a` | 全部 |
| `--no-legend` | 不显示表头 ⭐ |
| `-q` | 安静 ⭐ |
| `--verify=签名检查` | 镜像签名验证 🔐 ⭐ |

```bash
# 场景：⭐ 列出所有机器（容器/VM）
$ machinectl list
MACHINE     CLASS     SERVICE        OS     VERSION ADDRESSES
mycontainer container systemd-nspawn debian 12      10.0.0.5
winvm       vm        qemu           -      -        -

2 machines listed.

# 场景：⭐ 机器详情（含 cgroup、网络、进程）
$ machinectl status mycontainer
mycontainer
           Since: Tue 2026-09-15 08:00:00 CST; 1h ago
       Leader: 12345 (systemd)
      Service: systemd-nspawn; class container
         Root: /var/lib/machines/mycontainer
          OS: Debian GNU/Linux 12 (bookworm)
        Unit: machine-mycontainer.scope
     Address: 10.0.0.5

# 场景：⭐⭐ 登录到容器 / 在其中执行命令
$ sudo machinectl login mycontainer         # 打开登录会话
$ sudo machinectl shell mycontainer         # 打开 root shell（推荐）⭐
$ sudo machinectl shell mycontainer /usr/bin/uptime
$ sudo machinectl shell mycontainer /bin/bash -c 'systemctl status nginx'
$ # ⭐ shell 比 login 更适合自动化与脚本

# 场景：⭐ 与 systemctl 的配合（机器的操作都能用 systemctl）
$ sudo systemctl start systemd-nspawn@mycontainer
$ sudo systemctl stop systemd-nspawn@mycontainer
$ sudo systemctl status systemd-nspawn@mycontainer
$ sudo systemctl enable systemd-nspawn@mycontainer     # ⭐ 开机自启
$ sudo journalctl -u systemd-nspawn@mycontainer -f

# 场景：⭐ 镜像管理
$ sudo machinectl list-images
NAME      TYPE RO CREATION TIMESTAMP   MODIFICATION TIMESTAMP
debian    dir  no  Mon 2026-09-01 ...  Mon 2026-09-01 ...

$ sudo mkdir -p /var/lib/machines
$ sudo machinectl pull-tar https://example.com/debian-12.tar.gz           # ⚠️ 无验证
$ sudo machinectl pull-tar --verify=signature https://example.com/x.tar.gz # 🔐 验证
$ # ⭐ 从本地 tar 导入
$ sudo machinectl import-tar debian-12.tar.gz mydebian
$ sudo machinectl import-raw debian-12.img mydebian
$ sudo machinectl image-list
$ sudo machinectl clean                    # ⭐ 清理未使用的镜像

# 场景：⭐ 创建容器文件系统（用 debootstrap / dnf）
$ sudo debootstrap --include=systemd,dbus bookworm /var/lib/machines/debian12 \
>   http://deb.debian.org/debian
$ sudo systemd-nspawn -D /var/lib/machines/debian12 --machine=debian12
# 或用从官方镜像：
$ sudo machinectl pull-tar --verify=checksum \
>   https://download.opensuse.org/tumbleweed/appliances/... debian12

# 场景：⭐ 复制文件（主机 ⇄ 机器）⭐
$ sudo machinectl copy-to mycontainer /tmp/config.yml /etc/myapp/config.yml
$ sudo machinectl copy-from mycontainer /var/log/app.log /tmp/app.log
$ # ⭐ 也可用 nsenter + cp，但 machinectl 更简单

# 场景：⭐ 运行时绑定挂载（不重启容器）
$ sudo machinectl bind mycontainer /host/path /container/path
$ sudo machinectl bind --read-only mycontainer /host/data /data     # ⭐ 只读
$ sudo machinectl bind --mkdir mycontainer /host/conf /etc/app       # ⭐ 自动建目录

# 场景：⚠️ 强制操作
$ sudo machinectl terminate mycontainer        # 强制终止（不发 SIGTERM 流程）
$ sudo machinectl kill mycontainer SIGKILL
$ sudo machinectl poweroff mycontainer         # 正常关机
$ sudo machinectl reboot mycontainer

# 场景：⭐ 克隆与重命名
$ sudo machinectl clone mycontainer mycontainer-clone
$ sudo machinectl rename oldname newname
$ sudo machinectl remove mycontainer-clone     # ⚠️ 删除

# 场景：⭐ 在机器里运行 systemctl
$ sudo machinectl shell mycontainer systemctl status nginx
$ sudo systemctl --machine=mycontainer status nginx     # ⭐ 另一种写法
$ sudo systemctl -M mycontainer status nginx            # ⭐ 简写
$ sudo journalctl -M mycontainer -u nginx --no-pager

# 场景：🔐 machinectl 与安全（隔离评估）⭐
$ # 1. 查看容器的启动参数（隔离程度）
$ ps -ef | grep '[s]ystemd-nspawn'
$ systemctl cat systemd-nspawn@mycontainer.service
$ # 2. 检查容器是否用了危险选项
$ grep -oE -- '--(privileged|capability=[^ ]+|bind=[^ ]+|network-(veth|macvlan|ipvlan))' \
>   /etc/systemd/nspawn/*.nspawn 2>/dev/null
$ # ⚠️ --privileged 或大量 capability 会大幅削弱隔离
$ # 3. 进入容器检查隔离边界
$ sudo machinectl shell mycontainer /bin/bash -c 'cat /proc/self/status | grep -E "CapEff|Seccomp"'
$ sudo machinectl shell mycontainer /bin/bash -c 'ls /proc/1/ns/'

# 场景：🔐 从主机检查容器内的进程（不进入容器）
$ sudo systemd-cgls /machine.slice/machine-mycontainer.scope --no-pager | head -30
$ sudo systemd-cgtop -M mycontainer -b -n1
$ sudo journalctl -M mycontainer --no-pager -n 20
$ sudo nsenter -t "$(systemctl show -p MainPID --value machine-mycontainer.scope)" -m -u -i -p -n /bin/bash
$ # ⭐ nsenter 可以直接进入容器的所有命名空间

# 场景：🔐 检查是否有异常的 machine（持久化手法）⭐
$ machinectl list
$ ls -la /var/lib/machines/
$ ls -la /etc/systemd/nspawn/ /usr/lib/systemd/nspawn/
$ systemctl list-unit-files --state=enabled | grep -E 'nspawn|machine'
$ # ⭐ 攻击者可能用 nspawn 容器做持久化隔离环境

# 场景：🧪 完整的容器环境搭建 ⭐
$ cat /tmp/setup-container.sh
#!/bin/bash
set -euo pipefail
name=testenv
root=/var/lib/machines/$name

# 1. 创建根文件系统
sudo mkdir -p "$root"
sudo debootstrap --include=systemd,dbus,iproute2 bookworm "$root" \
  http://deb.debian.org/debian

# 2. 设置 root 口令（容器内）
sudo systemd-nspawn -D "$root" --pipe /bin/bash -c 'echo root:test | chpasswd'

# 3. 配置容器（可选：网络、绑定挂载）
sudo mkdir -p /etc/systemd/nspawn
sudo tee /etc/systemd/nspawn/"$name".nspawn >/dev/null <<'EOF'
[Exec]
Boot=yes
Private=yes

[Network]
VirtualEthernet=yes
Bridge=br0

[Files]
Bind=/host/data:/data
BindReadOnly=/host/conf:/etc/app
EOF

# 4. 启动与验证
sudo machinectl start "$name"
machinectl list
sudo machinectl shell "$name" /usr/bin/uptime
sudo machinectl shell "$name" /bin/bash -c 'ip -br a; ss -tunlp'
sudo machinectl stop "$name"
```

#### 输出解读
`machinectl list` 的列：

| 列 | 含义 |
|----|------|
| `MACHINE` | 机器名 ⭐ |
| `CLASS` | `container`（nspawn）或 `vm`（qemu） ⭐ |
| `SERVICE` | 后端（`systemd-nspawn` / `qemu`） ⭐ |
| `OS` / `VERSION` | 客户机操作系统 ⭐ |
| `ADDRESSES` | 客户机 IP（若可探测） ⭐ |

`machinectl status` 的关键行：

| 行 | 含义 |
|----|------|
| `Leader` | 客户机内 PID 1 的**主机侧 PID** ⭐ |
| `Root` | 客户机根文件系统路径 ⭐ |
| `Unit` | cgroup 单元（`machine-X.scope`） ⭐ |

**与 `machine.slice` 的关系**：所有机器都在 `/machine.slice/` 下，可用 `systemd-cgls` / `systemd-cgtop` 查看 ⭐。

#### 常见坑
- ⚠️ **`machinectl login` 需要容器里有 `logind`**；**`shell` 更通用**（直接在容器里 fork 命令）⭐。
- ⚠️ **`terminate` 会立刻杀掉容器内所有进程**（不优雅），优先用 `poweroff`/`stop` ⭐。
- ⚠️ **`pull-tar` 默认不验证完整性**。要 `--verify=checksum` 或 `--verify=signature` 🔐⭐。
- ⚠️ **nspawn 容器默认共享内核**（不是真正的虚拟机），隔离弱于 VM（不要用来隔离不可信代码）⭐。
- ⚠️ **`--privileged` 或大量 capability 会大幅削弱隔离**（检查 `/etc/systemd/nspawn/*.nspawn`）🔐⭐。
- **`machinectl` 同时也管理 `qemu` 虚拟机**（`systemd-vmspawn`）⭐。
- **容器内 systemd 需要 `systemd` 与 `dbus` 包**（debootstrap 要显式 `--include`）⭐。
- **`-M 名字` 可以让 `systemctl`/`journalctl` 直接操作容器**（比 `machinectl shell` 更方便）⭐⭐。

#### 相关命令
`systemd-nspawn` · `systemd-cgls` · `nsenter` · `docker` · `systemd-vmspawn`

---

### bootctl — 引导加载器管理

**常用度**：★★★☆☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有（UEFI 环境）

```bash
bootctl [选项] 命令
```

| 命令 | 作用 |
|------|------|
| （无参） / `status` | 引导状态（固件、引导器、ESP、条目） ⭐⭐ |
| `list` | 列出所有引导条目（含其他引导器） ⭐ |
| `list-entries` | 只列启动条目 ⭐ |
| `is-installed` | systemd-boot 是否安装（用退出码） ⭐ |
| `install` | 安装 systemd-boot 到 ESP ⭐ |
| `update` | **更新引导器文件**（升级 systemd 后必做） ⭐ |
| `remove` | 卸载 ⚠️ |
| `set-default 条目` | 设置默认启动项 ⭐ |
| `set-oneshot 条目` | 只下次启动用该条目 ⭐ |
| `random-seed` | 设置随机种子 |

| 选项 | 含义 |
|------|------|
| `--esp-path=路径` | ESP 路径（默认自动探测） ⭐ |
| `--boot-path=路径` | 启动分区路径 |
| `--root=路径` | 备用根（离线操作） ⭐⭐ |
| `--no-variables` | 不改 EFI 变量 ⭐ |
| `--graceful` | 已安装时不报错 ⭐ |

```bash
# 场景：⭐⭐ 查看引导状态（排障第一命令）
$ bootctl status
System:
     Firmware: UEFI 2.70 (American Megatrends 5.27)
  Firmware Arch: x64
    Secure Boot: disabled (setup)
   TPM2 Support: yes
   Boot into FW: supported

Current Boot Loader:
      Product: systemd-boot 256.4
     Features: ✓ Boot counting  ✓ Menu timeout control
               ✓ Menu entry editor  ✓ One-shot boot
               ✓ Secure Boot  ✓ TPM2 measured boot

Available Boot Loaders on ESP:
          ESP: /boot/efi (/dev/disk/by-partuuid/abcd-1234)
         File: └─/EFI/systemd/systemd-bootx64.efi (systemd-boot 256.4)
         File: └─/EFI/BOOT/BOOTX64.EFI (systemd-boot 256.4)

Boot Loader Entries:
        title: Arch Linux
           id: arch.conf
       source: /boot/efi/loader/entries/arch.conf
        linux: /vmlinuz-linux
       initrd: /initramfs-linux.img
      options: root=UUID=ab12cd34-... rw quiet

# 场景：⭐ 查看是否用 systemd-boot
$ bootctl is-installed && echo "systemd-boot 已安装"
$ bootctl is-installed --graceful || echo "不是 systemd-boot"
$ [ -d /boot/grub ] && echo "GRUB 存在"
$ efibootmgr -v 2>/dev/null | head

# 场景：⭐ bootctl update（升级 systemd 后必做）⭐⭐
$ sudo bootctl update
$ systemctl status systemd-boot-update.service       # ⭐ 自动更新（systemd 254+）
$ sudo systemctl enable --now systemd-boot-update.service

# 场景：⭐ 设置默认与一次性启动项
$ ls /boot/efi/loader/entries/
arch.conf  arch-fallback.conf  windows.conf
$ sudo bootctl set-default arch-fallback.conf
$ sudo bootctl set-oneshot windows.conf              # ⭐ 只下次启动进 Windows
$ bootctl list | grep -B1 -A2 status

# 场景：⭐ 查看配置文件
$ cat /boot/efi/loader/loader.conf
default  arch.conf
timeout  5
console-mode max
editor   no
$ # ⭐⭐ `editor no` 是重要的安全选项（禁止在引导菜单改内核参数）
$ cat /boot/efi/loader/entries/arch.conf
title   Arch Linux
linux   /vmlinuz-linux
initrd  /initramfs-linux.img
options root=UUID=ab12cd34-... rw quiet

# 场景：🔐 引导加固审计（安全）⭐⭐
$ # 1. Secure Boot 状态
$ bootctl status | grep -i 'secure boot'
    Secure Boot: disabled (setup)
$ # ⭐ disabled 说明未启用（物理接触者可替换引导器与内核）
$ mokutil --sb-state 2>/dev/null
$ # 2. 引导菜单是否可编辑（可改 init=/bin/bash 绕过所有认证）
$ grep -E '^editor' /boot/efi/loader/loader.conf
$ # ⭐ editor yes → 任何人可改内核参数获得 root shell
$ # 3. 是否有引导口令
$ grep -E '^password' /boot/efi/loader/loader.conf
$ grep -EE 'set superusers|password_pbkdf2' /boot/grub/grub.cfg /etc/grub.d/* 2>/dev/null
$ # 4. ESP 的挂载选项与权限
$ mount | grep -i efi
$ findmnt -T /boot/efi -o TARGET,SOURCE,FSTYPE,OPTIONS
$ ls -ld /boot/efi /boot/efi/loader
$ # 5. 内核与 initramfs 的完整性
$ sudo sha256sum /boot/vmlinuz-linux /boot/initramfs-linux.img
$ sudo pacman -Qkk linux 2>/dev/null | grep -i alter
$ sudo rpm -V kernel 2>/dev/null; sudo dpkg -V linux-image-$(uname -r) 2>/dev/null
$ # 6. TPM2 / 测量启动
$ bootctl status | grep -A3 -iE 'tpm|secure boot'
$ systemd-analyze has-tpm2

# 场景：⚠️ 引导器损坏时的修复
$ sudo bootctl install
$ sudo bootctl update
$ ls -la /boot/efi/EFI/systemd/ /boot/efi/EFI/BOOT/
$ efibootmgr -v 2>/dev/null | head -20
$ efibootmgr -o 0000,0001 2>/dev/null                # ⭐ 调整启动顺序

# 场景：🧪 离线修复另一个系统的引导（救援模式）⭐⭐
$ sudo mount /dev/nvme0n1p1 /mnt/boot/efi
$ sudo mount /dev/nvme0n1p2 /mnt
$ sudo mount --rbind /dev /mnt/dev && sudo mount --rbind /proc /mnt/proc && sudo mount --rbind /sys /mnt/sys
$ sudo bootctl --root=/mnt --esp-path=/mnt/boot/efi install
$ sudo bootctl --root=/mnt status | head -10
$ sudo arch-chroot /mnt bootctl update

# 场景：🧪 完整的引导安全检查脚本 ⭐
$ cat /tmp/boot-audit.sh
#!/bin/bash
echo "=== 引导器 ==="
if bootctl is-installed --graceful 2>/dev/null; then
  echo "systemd-boot"
  echo "--- loader.conf ---"
  grep -vE '^\s*#|^$' /boot/efi/loader/loader.conf 2>/dev/null
  echo "--- editor 设置（⚠️ yes = 可绕过认证）---"
  grep -E '^\s*editor' /boot/efi/loader/loader.conf 2>/dev/null || echo "(未设置)"
else
  echo "非 systemd-boot"
  [ -d /boot/grub ] && grub-install --version 2>/dev/null
  grep -E 'set superusers|password_pbkdf2' /boot/grub/grub.cfg 2>/dev/null | head
fi

echo
echo "=== 固件与 Secure Boot ==="
bootctl status 2>/dev/null | grep -E 'Firmware|Secure Boot|TPM2'
mokutil --sb-state 2>/dev/null

echo
echo "=== 引导条目 ==="
bootctl list 2>/dev/null | grep -E 'title:|linux:|options:' | head -20

echo
echo "=== 内核完整性 ==="
sudo sha256sum /boot/vmlinuz-* 2>/dev/null

echo
echo "=== ESP 挂载选项（应有 nosuid,nodev）==="
findmnt -T /boot/efi -o TARGET,SOURCE,FSTYPE,OPTIONS 2>/dev/null

echo
echo "=== EFI 启动顺序 ==="
efibootmgr -v 2>/dev/null | head -15 || echo "(efibootmgr 不可用)"
```

#### 输出解读
`bootctl status` 的关键字段：

| 字段 | 含义 |
|------|------|
| `Firmware` | UEFI 版本与厂商 ⭐ |
| `Secure Boot` | **`enabled` / `disabled (setup)` / `disabled (unsupported)`** 🔐⭐ |
| `TPM2 Support` | TPM2 是否可用 🔐⭐ |
| `Current Boot Loader` | 当前引导器与版本 ⭐ |
| `ESP` | EFI 系统分区路径与设备 ⭐ |
| `Boot Loader Entries` | 条目列表（title/id/linux/initrd/options） ⭐ |
| `status: selected` | 本次启动选中的条目 ⭐ |

**`loader.conf` 的关键选项**：

| 选项 | 含义 | 安全建议 |
|------|------|----------|
| `default` | 默认条目 ⭐ | — |
| `timeout` | 菜单超时（秒） | — |
| `editor` | **是否允许编辑内核参数** | **`no`** 🔐⭐ |
| `console-mode` | 控制台模式 | — |
| `password` | 引导密码 | 设置更安全 |

#### 🔐 引导层的攻击面
| 风险 | 后果 | 防护 |
|------|------|------|
| 物理接触 + Secure Boot 关闭 | 替换引导器/内核 | 启用 Secure Boot ⭐ |
| `editor yes` | 改 `init=/bin/bash` 得 root shell | 设 `editor no` ⭐⭐ |
| 无引导口令 | 选单用户模式绕过 | 设 `password` 或 GRUB superusers ⭐ |
| initramfs 可写 | 植入 hook | 控制 `/boot` 权限 + Secure Boot |
| ESP 挂载选项不当 | SUID/设备文件攻击 | `nosuid,nodev,fmask=0077` ⭐ |

#### 常见坑
- ⚠️⚠️ **`loader.conf` 的 `editor yes` 允许任何人改内核参数获得 root shell**。服务器应设为 `no` 🔐⭐。
- ⚠️ **升级 systemd 后要 `bootctl update`**（或启用 `systemd-boot-update.service`），否则引导器与内核模块版本不匹配 ⭐。
- ⚠️ **`bootctl` 只适用于 systemd-boot**。GRUB 用户用 `grub-install`/`grub-mkconfig`/`efibootmgr` ⭐。
- ⚠️ **操作 ESP 时挂载选项很重要**（`fmask=0077`、`nosuid`、`nodev`）⭐。
- **`bootctl --root=/mnt` 是离线修复的关键**（救援模式必备）⭐⭐。
- **`bootctl list` 会包含其他引导器的条目**（Windows、GRUB chainloader）⭐。
- **`systemd-boot` 只支持 UEFI**（不支持 BIOS/CSM）⭐。
- **ESP 通常挂载在 `/boot/efi` 或 `/efi`**（Arch 现代方案是 `/efi`）⭐。

#### 相关命令
`efibootmgr` · `grub-install` · `grub-mkconfig` · `mokutil` · `sbsigntools` · `systemd-boot`

---

### shutdown / reboot / halt / poweroff — 关机与重启

**常用度**：★★★★★ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：现代系统上由 systemd 提供（`systemctl` 的软链接或前端）

```bash
shutdown [选项] [时间] [消息]
reboot | halt | poweroff [选项]
systemctl poweroff | reboot | halt | suspend | hibernate | hybrid-sleep | suspend-then-hibernate
```

| shutdown 选项 | 含义 |
|---------------|------|
| `-h` | 关机 |
| `-r` | 重启 ⭐ |
| `-c` | **取消已计划的关机** ⭐ |
| `-k` | 只发警告不真关机 ⭐ |
| `-P` | 关机并断电 ⭐ |
| `-H` | 停机但不断电 |
| `-t N` | 延迟 N 秒 |
| `--no-wall` | 不发消息给所有用户 ⭐ |
| `now` | 立即 ⭐ |
| `+N` | N 分钟后 ⭐ |
| `HH:MM` | 指定时刻 ⭐ |

```bash
# 场景：⭐ 立即关机/重启
$ sudo shutdown -h now
$ sudo shutdown -r now
$ sudo systemctl poweroff
$ sudo systemctl reboot
$ sudo poweroff
$ sudo reboot

# 场景：⭐ 定时关机（给用户留时间）⭐
$ sudo shutdown -h +10 "维护，10 分钟后关机"
$ sudo shutdown -r 02:00 "凌晨 2 点重启"
$ wall "5 分钟后关机，请保存工作"                     # ⭐ 手动广播

# 场景：⭐ 取消已计划的关机
$ sudo shutdown -c
$ sudo shutdown -c "维护取消"

# 场景：⭐ 只广播不关机（演练）
$ sudo shutdown -k +5 "测试：5 分钟后会关机（实际不会）"

# 场景：⭐ 挂起与休眠
$ sudo systemctl suspend                    # 挂起到内存（S3） ⭐
$ sudo systemctl hibernate                  # 休眠到磁盘（S4） ⭐
$ sudo systemctl hybrid-sleep               # 混合睡眠
$ sudo systemctl suspend-then-hibernate     # 先挂起后休眠 ⭐
$ cat /sys/power/state
freeze mem disk
$ cat /sys/power/mem_sleep
s2idle [deep]

# 场景：🔐 关机前检查「谁在登录」与「有无抑制器」
$ who; w; loginctl list-sessions
$ systemd-inhibit --list
$ sudo shutdown -r +15 "内核升级，15 分钟后重启"

# 场景：🔐 用 systemd 抑制器保护关键操作 ⭐⭐
$ systemd-inhibit --list
WHO             UID  USER  PID   COMM            WHAT      WHY         MODE
NetworkManager  0    root  823   NetworkManager  sleep     ...         block
unattended-upg  0    root  1234  unattended-upgr shutdown  ...         delay

$ # ⭐ 做备份时阻止关机
$ systemd-inhibit --what=shutdown --who="backup" --why="备份中" --mode=block \
>   /usr/local/bin/backup.sh
$ systemd-inhibit --list | grep backup

$ # ⭐ 若关机被抑制
$ sudo systemctl poweroff
Operation inhibited by "backup" (UID 0, PID 1234, reason "备份中"),
please retry after closing blocking inhibitors.

$ # ⚠️ 强制关机（绕过抑制，可能丢数据）
$ sudo systemctl poweroff -i
$ sudo shutdown -h +0

# 场景：🔐 排查恶意的抑制器（阻止关机 / 干扰运维）⭐
$ systemd-inhibit --list
$ systemd-inhibit --list --mode=block
$ ps -eo pid,user,cmd | grep -i inhibit

# 场景：⭐ 进入救援/紧急模式（不重启的维护状态）
$ sudo systemctl rescue              # 停止多用户服务，只留基础
$ sudo systemctl emergency           # 只挂载根（只读），最简救援
$ sudo systemctl isolate multi-user.target
$ sudo systemctl isolate graphical.target

# 场景：🧪 关机慢的排障 ⭐
$ journalctl -b -1 -p warning --no-pager | tail -30
$ systemd-analyze blame | head
$ # ⭐ 关机慢通常是某服务不响应 SIGTERM（要等 TimeoutStopSec，默认 90s）
$ grep -r 'TimeoutStopSec' /etc/systemd/system/*.d/ /usr/lib/systemd/system/*.service 2>/dev/null | head
$ journalctl -b -1 -u systemd-shutdownd --no-pager | tail -30
$ # ⭐ 找出卡住的服务后加：
$ #   [Service]
$ #   TimeoutStopSec=10
$ #   KillMode=mixed

# 场景：🧪 完整的安全重启脚本 ⭐
$ cat /tmp/safe-reboot.sh
#!/bin/bash
set -euo pipefail
delay=${1:-10}

echo "=== 活跃会话 ==="
loginctl list-sessions --no-pager

echo "=== 抑制器 ==="
systemd-inhibit --list --no-pager || true

echo "=== 失败的服务 ==="
systemctl --failed --no-legend --no-pager || true

echo "=== 磁盘与内存 ==="
df -h / /var 2>/dev/null | tail -n +2
free -h | head -2

sudo shutdown -r "+$delay" "系统将在 $delay 分钟后重启，请保存工作"
echo "已计划 $delay 分钟后重启。取消：sudo shutdown -c"
```

#### 输出解读
`systemctl` 的关机类命令：

| 命令 | 等价 |
|------|------|
| `systemctl poweroff` | `shutdown -h now` + 断电 ⭐ |
| `systemctl reboot` | `shutdown -r now` ⭐ |
| `systemctl halt` | 停机但不断电 ⭐ |
| `systemctl suspend` | 挂起到内存（S3） ⭐ |
| `systemctl hibernate` | 休眠到磁盘（S4） ⭐ |
| `systemctl hybrid-sleep` | 内存 + 磁盘都保存 |
| `systemctl suspend-then-hibernate` | 先挂起，超时后休眠 ⭐ |
| `systemctl rescue` / `emergency` | 救援 / 紧急模式 ⭐ |

`systemd-inhibit --list` 的字段：

| 字段 | 含义 |
|------|------|
| `WHAT` | 被抑制的操作（`shutdown`/`sleep`/`idle`/`handle-power-key`） ⭐ |
| `WHY` | 原因 |
| `MODE` | `block`（阻止）/ `delay`（延迟）/ `block-weak` ⭐ |

#### 常见坑
- ⚠️ **`shutdown` 需要 root**（普通用户报 `Must be root`）⭐。
- ⚠️ **`+N` 是「N 分钟后」，`N`（无加号）是「绝对时刻」**；`shutdown +0` 是立即 ⭐。
- ⚠️ **`-h` 不一定是断电**（可能只 halt），要断电用 `-P` 或 `poweroff` ⭐。
- ⚠️ **`systemctl poweroff -i` 会忽略抑制器**（可能中断备份）⚠️。
- ⚠️ **`shutdown -c` 只能取消「计划中的」关机**，已开始关机流程后无法取消 ⭐。
- ⚠️ **`hibernate` 需要 swap ≥ 内存**（且内核参数正确），否则失败 ⭐。
- **关机慢通常是某服务等超时**（默认 90 秒），用 `journalctl -b -1` 定位 ⭐。
- **`loginctl` 的活跃会话可能阻止重启**（取决于 `KillUserProcesses=`）⭐。
- **`reboot`/`poweroff` 在现代系统上是 `systemctl` 的软链接**（`ls -l /sbin/reboot`）⭐。

#### 相关命令
`systemctl` · `loginctl` · `systemd-inhibit` · `wall` · `last -x reboot`

---

### service / chkconfig / update-rc.d — SysV 兼容

**常用度**：★★★☆☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有（兼容层）

```bash
service 服务名 {start|stop|restart|reload|status}
chkconfig [--list] [--add] [--del] [--level 级别] 服务名 {on|off}
update-rc.d 服务名 {enable|disable|defaults|remove}
ntsysv                                    # 交互式（RHEL 系）
rc-update {add|del} 服务 [级别]            # Alpine / OpenRC
```

**现代系统上它们是到 `systemctl` 的兼容包装**：

| 老命令 | systemd 等价 |
|--------|--------------|
| `service X start` | `systemctl start X.service` ⭐ |
| `service X restart` | `systemctl restart X.service` ⭐ |
| `service X status` | `systemctl status X.service` ⭐ |
| `chkconfig X on` | `systemctl enable X.service` ⭐ |
| `chkconfig X off` | `systemctl disable X.service` ⭐ |
| `update-rc.d X defaults` | `systemctl enable X.service` ⭐ |
| `ntsysv` | `systemctl list-unit-files --state=enabled` |

```bash
# 场景：⭐ 用 service 启动（兼容老脚本）
$ sudo service nginx start
$ sudo service nginx status
$ sudo service nginx restart
$ service --status-all 2>/dev/null
 [ + ]  cron
 [ + ]  nginx
 [ - ]  apache2
$ # ⭐ + 表示运行中，- 表示停止

# 场景：⭐ 用 chkconfig / update-rc.d 设置自启
$ sudo chkconfig --list | head
$ sudo chkconfig nginx on
$ sudo chkconfig --list nginx
$ sudo update-rc.d nginx defaults
$ sudo update-rc.d nginx enable
$ sudo update-rc.d -f nginx remove            # ⚠️ 移除所有链接

# 场景：⭐ 检查本机用的是哪套初始化系统
$ ps -p 1 -o comm=
systemd
$ [ -d /run/systemd/system ] && echo "systemd 运行中"
$ [ -d /run/openrc ] && echo "OpenRC 运行中"
$ cat /proc/1/comm
$ systemctl --version | head -1
$ pidof systemd >/dev/null && echo systemd || echo "非 systemd"

# 场景：⭐ 理解兼容层（为什么 service 能操作 systemd 服务）
$ file "$(command -v service)"
/usr/sbin/service: POSIX shell script, ASCII text executable
$ grep -E 'systemctl|invoke-rc.d' /usr/sbin/service | head -5
$ # ⭐ 是发行版提供的映射脚本

# 场景：🔐 SysV 的持久化位置（攻击者仍会用）⭐⭐
$ ls -la /etc/init.d/
$ ls -la /etc/rc*.d/ | head -30
$ ls -la /etc/rc.local 2>/dev/null
$ cat /etc/rc.local 2>/dev/null
$ # ⭐ rc.local 是经典的持久化位置（systemd 上需启用 rc-local.service）
$ systemctl status rc-local.service 2>/dev/null
$ cat /etc/systemd/system/rc-local.service 2>/dev/null
$ # ⭐ 检查内容是否可疑
$ grep -E 'curl|wget|base64|nc |/dev/tcp|chmod \+x' /etc/rc.local 2>/dev/null

# 场景：🔐 完整的多初始化系统持久化审计 ⭐⭐
$ cat /tmp/persist-audit.sh
#!/bin/bash
echo "=== 1. systemd 单元（enabled）==="
systemctl list-unit-files --state=enabled --no-legend 2>/dev/null | head -40

echo
echo "=== 2. systemd 用户级单元 ==="
for h in /root /home/*; do
  [ -d "$h/.config/systemd/user" ] && {
    echo "--- $h"
    ls -la "$h/.config/systemd/user/" 2>/dev/null
  }
done

echo
echo "=== 3. systemd 定时器 ==="
systemctl list-timers --all --no-legend 2>/dev/null | head -20

echo
echo "=== 4. systemd 临时单元（/run）==="
ls -la /run/systemd/transient/ 2>/dev/null

echo
echo "=== 5. SysV init ==="
ls -la /etc/init.d/ 2>/dev/null | head -20
ls -la /etc/rc*.d/ 2>/dev/null | head -40
cat /etc/rc.local 2>/dev/null

echo
echo "=== 6. OpenRC（如有）==="
rc-update show 2>/dev/null

echo
echo "=== 7. cron ==="
for u in $(cut -d: -f1 /etc/passwd); do
  crontab -l -u "$u" 2>/dev/null | grep -vE '^#|^$' | sed "s/^/[$u] /"
done
ls -la /etc/cron.d/ /etc/cron.{hourly,daily,weekly,monthly}/ 2>/dev/null
cat /etc/crontab 2>/dev/null

echo
echo "=== 8. at 任务 ==="
atq 2>/dev/null

echo
echo "=== 9. tmpfiles.d ==="
ls -la /etc/tmpfiles.d/ /run/tmpfiles.d/ 2>/dev/null

echo
echo "=== 10. shell 启动文件中的可疑内容 ==="
for f in /etc/profile /etc/bash.bashrc /etc/bashrc \
         /root/.bashrc /root/.bash_profile /root/.profile \
         /home/*/.bashrc /home/*/.bash_profile /home/*/.profile; do
  [ -f "$f" ] && grep -HnE 'curl|wget|base64|/dev/tcp|nc -e|socat' "$f" 2>/dev/null
done

# 场景：🧪 把 SysV 脚本转成 systemd 单元 ⭐
$ cat /tmp/mk-unit.sh
#!/bin/bash
svc=$1
init="/etc/init.d/$svc"
[ -f "$init" ] || { echo "找不到 $init"; exit 1; }
desc=$(grep -m1 '# Short-Description:' "$init" | cut -d: -f2- | sed 's/^ *//')
cat <<EOF
[Unit]
Description=${desc:-$svc}
After=network.target

[Service]
Type=forking
ExecStart=$init start
ExecStop=$init stop
ExecReload=$init reload
PIDFile=/run/$svc.pid
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

$ bash /tmp/mk-unit.sh nginx > /tmp/nginx-generic.service
$ cat /tmp/nginx-generic.service
$ systemd-analyze verify /tmp/nginx-generic.service
```

#### 输出解读
`service --status-all` 的输出：

| 标记 | 含义 |
|------|------|
| `[ + ]` | 运行中 ⭐ |
| `[ - ]` | 已停止 |
| `[ ? ]` | 状态未知（脚本没有 status 动作） |

**`/etc/rcN.d/` 的命名规则**：

| 前缀 | 含义 |
|------|------|
| `S` + 数字 | 启动（数字小者先启动） ⭐ |
| `K` + 数字 | 停止（数字小者先停止） ⭐ |
| 链接目标 | `/etc/init.d/X` ⭐ |

运行级别（SysV）：`0` 关机、`1` 单用户、`2`–`5` 多用户、`6` 重启。

#### 常见坑
- ⚠️ **在 systemd 系统上，`service`/`chkconfig` 只是兼容包装**。`service` 通常可用，但 `chkconfig` 可能在 Debian 系不存在（用 `update-rc.d`）⭐。
- ⚠️ **对 systemd 原生服务用 `service` 可能丢失部分功能**（如 `reload` 的行为差异）⭐。
- ⚠️ **`/etc/rc.local` 默认不存在，且 `rc-local.service` 可能未启用**（老脚本依赖它但实际不生效）⭐。
- ⚠️ **`update-rc.d -f remove` 会删掉所有 rcN.d 链接**（不可逆，要重装包）⚠️。
- **容器里可能没有 SysV 兼容层**，且通常不跑 init 系统 ⭐。
- **Alpine 用 OpenRC（`rc-update`/`rc-service`）**，与 SysV 类似但不同 ⭐。
- **审计时必须覆盖所有持久化位置**（见上面的完整脚本）。攻击者常在「不常用的那套机制」里藏东西 🔐⭐。

#### 相关命令
`systemctl` · `rc-update`（OpenRC） · `rc-service` · `insserv` · `runlevel`

---

### systemd-detect-virt — 检测虚拟化环境

**常用度**：★★★★☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

```bash
systemd-detect-virt [选项]
```

| 选项 | 含义 |
|------|------|
| （无参） | 输出虚拟化类型（或 `none`） ⭐⭐ |
| `--vm` | **只在虚拟机里返回 0** ⭐⭐ |
| `--container` | **只在容器里返回 0** ⭐⭐ |
| `--chroot` | 只在 chroot 里返回 0 ⭐ |
| `--private-users` | 在 user namespace 里返回 0 ⭐ |
| `--cvm` | 在机密虚拟机里返回 0 ⭐ |
| `-q` / `--quiet` | 无输出，只用退出码 ⭐ |
| `--list` | 列出所有可识别的类型 ⭐ |

**可识别的类型**：

| 类型 | 含义 |
|------|------|
| `none` | **物理机** ⭐ |
| `kvm` / `vmware` / `microsoft` / `oracle` / `xen` / `bhyve` / `parallels` | 虚拟机 ⭐ |
| `docker` / `podman` / `lxc` / `systemd-nspawn` / `openvz` / `rkt` / `wsl` / `proot` | 容器 ⭐ |
| `chroot` | chroot 环境 ⭐ |
| `qemu` | QEMU 软件模拟（无 KVM 加速） |
| `amazon` / `google` / `zvm` / `acrn` | 云 / 特殊平台 |
| `cvm` | 机密虚拟机（AMD SEV / Intel TDX） |

```bash
# 场景：⭐⭐ 判断是否在虚拟化环境（安全工作第一步）
$ systemd-detect-virt
kvm
$ systemd-detect-virt
docker
$ systemd-detect-virt
none

# 场景：⭐⭐ 脚本里的条件判断
$ if systemd-detect-virt --vm --quiet; then
>   echo "在虚拟机里，可以做快照实验"
> fi
$ if systemd-detect-virt --container --quiet; then
>   echo "在容器里，内核模块操作不可用"
> fi
$ v=$(systemd-detect-virt 2>/dev/null || echo none); echo "类型: $v"

# 场景：⭐ 列出所有可识别的类型
$ systemd-detect-virt --list
qemu kvm amazon google vmware microsoft oracle xen bochs uml openvz
parallels zvm bhyve qnx acrn powerkvm cvm systemd-nspawn docker
podman lxc lxc-libvirt rkt wsl proot pve

# 场景：🔐 交叉验证虚拟化环境（多来源确认）⭐⭐
$ cat /tmp/virt-multi.sh
#!/bin/bash
echo "=== systemd-detect-virt ==="
systemd-detect-virt

echo "=== /proc/cpuinfo ==="
grep -qi 'hypervisor' /proc/cpuinfo && echo "有 hypervisor 标志（虚拟机）" || echo "无"

echo "=== DMI/SMBIOS ==="
sudo dmidecode -s system-vendor 2>/dev/null | head -1
sudo dmidecode -s system-product-name 2>/dev/null | head -1
sudo dmidecode 2>/dev/null | grep -iE 'vmware|virtualbox|qemu|hyper-v|kvm|xen' | head -3

echo "=== 内核模块 ==="
lsmod | grep -E '^(virtio|vmw_|vbox|hyperv|xen)' | head -5

echo "=== PCI 设备 ==="
lspci 2>/dev/null | grep -iE 'vmware|virtio|qemu|virtualbox|hyper-v|red hat' | head -5

echo "=== 容器标志 ==="
[ -f /.dockerenv ] && echo "存在 /.dockerenv（Docker）"
[ -f /run/.containerenv ] && echo "存在 /run/.containerenv（Podman）"
grep -qE 'docker|containerd|kubepods' /proc/1/cgroup 2>/dev/null && echo "/proc/1/cgroup 含 docker/k8s"
tr '\0' '\n' < /proc/1/environ 2>/dev/null | grep -i container | head -3

echo "=== PID 1 ==="
ps -p 1 -o comm=

echo "=== 文件系统 ==="
findmnt -T / -o FSTYPE --value
mount | grep -iE 'overlay|9p|virtiofs' | head -3

echo "=== systemd 视角 ==="
hostnamectl | grep -i virtualization

# 场景：🔐 容器环境评估（逃逸风险）⭐⭐
$ systemd-detect-virt --container --quiet && {
>   echo "=== 容器环境评估 ==="
>   echo "PID 1: $(ps -p 1 -o comm=)"
>   echo "--- cgroup ---"; cat /proc/1/cgroup
>   echo "--- 容器标志 ---"; ls -la /.dockerenv /run/.containerenv 2>/dev/null
>   echo "--- capability ---"; grep -E 'CapEff|Seccomp' /proc/self/status
>   capsh --print 2>/dev/null | head -8
>   echo "--- namespace ---"; ls /proc/self/ns/
>   echo "--- 危险挂载 ---"; mount | grep -E 'docker.sock|/proc|/sys|/dev' | head -10
>   ls -la /var/run/docker.sock /run/docker.sock 2>/dev/null
>   echo "--- 宿主设备可见性 ---"; ls /dev/ | head -20
> }

# 场景：🔐 判断是否在特权容器 ⭐
$ capsh --decode="$(awk '/CapEff/{print $2}' /proc/self/status)" 2>/dev/null | tr ',' '\n' | head -25
$ # ⭐ 有 CAP_SYS_ADMIN / CAP_NET_ADMIN / CAP_SYS_PTRACE 等 → 特权程度高
$ cat /proc/self/status | grep Seccomp
Seccomp:	0            # ⭐ 0 = 未启用 seccomp（隔离更弱）
$ ls /dev/kmsg /dev/mem 2>/dev/null
$ ls /sys/fs/cgroup/ | head

# 场景：🔐 用虚拟化类型决定测试策略 ⭐
$ virt=$(systemd-detect-virt)
$ case "$virt" in
>   kvm|vmware|oracle|microsoft|xen)
>     echo "虚拟机：可测内核模块、快照回滚、嵌套虚拟化" ;;
>   docker|podman|lxc|systemd-nspawn)
>     echo "容器：不能加载内核模块，注意逃逸风险" ;;
>   none)
>     echo "物理机：所有操作要谨慎，没有快照兜底 ⚠️" ;;
>   *)
>     echo "未知类型: $virt" ;;
> esac

# 场景：🧪 检查是否支持嵌套虚拟化（在 VM 里跑 KVM）⭐
$ systemd-detect-virt --vm --quiet && echo "在 VM 中"
$ grep -cE 'vmx|svm' /proc/cpuinfo
$ ls /dev/kvm 2>/dev/null && echo "有 /dev/kvm（支持嵌套虚拟化）"
$ cat /sys/module/kvm_intel/parameters/nested 2>/dev/null
$ cat /sys/module/kvm_amd/parameters/nested 2>/dev/null
$ sudo modprobe kvm_intel nested=1 2>/dev/null && echo "已按需加载"

# 场景：🧪 检查 WSL 环境
$ systemd-detect-virt
wsl
$ grep -i microsoft /proc/version
$ ls /mnt/c 2>/dev/null | head -3
$ cat /etc/wsl.conf 2>/dev/null

# 场景：🧪 检查容器里 systemd 是否可用
$ systemd-detect-virt --container --quiet && {
>   pid1=$(ps -p 1 -o comm=)
>   echo "PID 1 = $pid1"
>   if [ "$pid1" = "systemd" ]; then
>     echo "容器里有 systemd（可用 systemctl）"
>     systemctl is-system-running 2>/dev/null
>   else
>     echo "容器无 systemd（需直接启动进程，或用 --init）"
>   fi
> }
```

#### 输出解读
| 输出 | 含义 |
|------|------|
| `none` | **物理机** ⭐ |
| `kvm` / `vmware` / `microsoft` / `oracle` / `xen` / `bhyve` | 虚拟机（`--vm` 匹配） ⭐ |
| `docker` / `podman` / `lxc` / `systemd-nspawn` / `openvz` / `rkt` / `wsl` / `proot` | 容器（`--container` 匹配） ⭐ |
| `chroot` | chroot（`--chroot` 匹配） ⭐ |
| `qemu` | QEMU 软件模拟（无 KVM 加速） |
| `cvm` | 机密虚拟机（AMD SEV / Intel TDX） |

⚠️ **`systemd-detect-virt` 只看最内层**：在「容器里的虚拟机」中，它返回最内层类型 ⭐。

#### 🔐 虚拟化检测在安全工作中的用途
| 场景 | 用途 |
|------|------|
| 恶意软件分析 | 判断是否在沙箱里（**恶意软件会主动检测并休眠**） 🔐⭐ |
| 渗透测试 | 了解目标环境的隔离边界 |
| 容器逃逸评估 | 确认是容器还是 VM，以及特权程度 🔐⭐ |
| 内核模块操作 | 容器里无法 `modprobe` |
| 快照回滚 | VM 可以随意实验，物理机不行 ⚠️ |
| 加固决策 | 容器与物理机的加固项不同 |

#### 常见坑
- ⚠️ **只看最内层的类型**。要判断「VM 里的容器」需交叉验证（`/proc/1/cgroup` + DMI + 内核模块）⭐。
- ⚠️⚠️ **可以被欺骗**（伪造 DMI、隐藏 `/proc` 标志、修改 hook）。**安全敏感的判断必须多来源交叉验证** 🔐⭐⭐。
- ⚠️ **`--quiet` 时只看退出码**，没有任何输出 ⭐。
- **`--chroot` 与 `--container` 是互斥的判断**（chroot 不是容器）⭐。
- **`--private-users` 判断 user namespace**（容器里常见）⭐。
- **在容器里 `--vm` 通常返回非 0**（它返回最内层类型，即容器）⭐。
- **`cvm` 是「机密虚拟机」**（AMD SEV / Intel TDX）⭐。
- **`systemd-detect-virt` 在无 systemd 的系统上可能不存在**（Alpine 用 `virt-what`）⭐。

#### 相关命令
`hostnamectl` · `dmidecode` · `lspci` · `capsh` · `virt-what` · `/proc/1/cgroup`

---

### coredumpctl — 崩溃转储管理

**常用度**：★★★★☆ ｜ **所属**：系统管理（systemd） ｜ **POSIX/GNU 差异**：Linux 特有

```bash
coredumpctl [选项] 命令 [参数]
```

| 命令 | 作用 |
|------|------|
| `list` | 列出所有转储 ⭐⭐ |
| `info [PID/MATCH]` | 转储详情（含栈回溯） ⭐⭐ |
| `dump [PID/MATCH]` | 导出 core 到 stdout/文件 ⭐ |
| `gdb [PID/MATCH]` | **用 gdb 调试该转储** ⭐⭐⭐ |
| `debug [PID/MATCH]` | 启动调试器（默认 gdb） ⭐ |
| `cat [MATCH]` | 输出到 stdout |
| `sysctl` | 显示内核相关的 sysctl 设置 ⭐ |

| 选项 | 含义 |
|------|------|
| `-1` | **只看最近一个** ⭐ |
| `-n N` | 最近 N 个 ⭐ |
| `--since` / `--until` | 时间范围 ⭐ |
| `-F 字段=值` | 按字段过滤（`_PID=`、`_COMM=`、`_EXE=`、`_UID=`） ⭐ |
| `--reverse` | 倒序 ⭐ |
| `-o 文件` | 输出到文件（`dump`） ⭐ |
| `--no-pager` / `--no-legend` | 不分页 / 不显示表头 ⭐ |
| `--debugger=` | 指定调试器 ⭐ |
| `-D 目录` | 用指定日志目录（离线） ⭐⭐ |
| `--file=文件` | 直接读 core 文件 ⭐ |
| `--json=格式` | JSON 输出 ⭐ |

```bash
# 场景：⭐⭐ 列出所有崩溃转储
$ coredumpctl list
TIME                          PID  UID  GID SIG     COREFILE EXE                          SIZE
Tue 2026-09-15 09:00:00 CST  1234 1000 1000 SIGSEGV present  /usr/bin/myapp              12.3M
Tue 2026-09-14 18:30:00 CST  5678    0    0 SIGABRT present  /usr/lib/jvm/java/bin/java  45.6M
Mon 2026-09-13 12:00:00 CST  9012 1000 1000 SIGSEGV missing  /usr/bin/other                -

$ coredumpctl list -1                       # ⭐ 最近一个
$ coredumpctl list -n 10 --no-pager
$ coredumpctl list --since "1 hour ago"
$ coredumpctl list --since today --reverse

# 场景：⭐⭐ 看转储详情（含栈回溯）
$ coredumpctl info -1
           PID: 1234 (myapp)
           UID: 1000 (alice)
        Signal: 11 (SEGV)
     Timestamp: Tue 2026-09-15 09:00:00 CST (1h ago)
  Command Line: /usr/bin/myapp --config /etc/myapp.conf
    Executable: /usr/bin/myapp
      Coredump: /var/lib/systemd/coredump/core.myapp.1000.abc123...
       Message: Process 1234 (myapp) of user 1000 dumped core.

                Stack trace of thread 1234:
                #0  0x00007f1234567890 raise (libc.so.6 + 0x3d890)
                #1  0x00007f1234569100 abort (libc.so.6 + 0x3e100)
                #2  0x00005555555551a0 main (myapp + 0x11a0)
                #3  0x00007f1234550000 __libc_start_main (libc.so.6 + 0x24000)
# ⭐ 栈回溯是最有价值的部分（直接看到崩在哪）

$ coredumpctl info 1234                     # 按 PID
$ coredumpctl info /usr/bin/myapp           # ⭐ 按可执行文件
$ coredumpctl info -F _COMM=myapp -1        # ⭐ 按字段过滤

# 场景：⭐⭐ 用 gdb 调试转储（最有用的功能）
$ coredumpctl gdb -1
GNU gdb (GDB) 15.1
Core was generated by `/usr/bin/myapp --config /etc/myapp.conf'.
Program terminated with signal SIGSEGV, Segmentation fault.
#0  0x00007f1234567890 in raise () from /lib/x86_64-linux-gnu/libc.so.6
(gdb) bt                                  # 栈回溯 ⭐
(gdb) bt full                             # 含局部变量 ⭐
(gdb) info registers
(gdb) info threads
(gdb) frame 2                             # 切到第 2 帧
(gdb) p variable_name
(gdb) thread apply all bt                 # ⭐ 所有线程的栈
(gdb) quit

$ # ⭐ 非交互式获取栈（脚本用）
$ coredumpctl gdb -1 <<'EOF' 2>/dev/null | sed -n '/#0/,/^$/p'
bt
quit
EOF
$ coredumpctl debug -1                     # 同 gdb
$ coredumpctl debug -1 --debugger=lldb

# 场景：⭐⭐ 导出 core 文件（离线分析 / 交给别人）
$ coredumpctl dump -1 -o /tmp/myapp.core
$ ls -lh /tmp/myapp.core
$ file /tmp/myapp.core
$ gdb /usr/bin/myapp /tmp/myapp.core -ex bt -ex quit       # ⭐ 离线分析
$ coredumpctl --file=/tmp/myapp.core info                  # ⭐ 直接读 core

# 场景：⭐ 只看某个程序的崩溃（排障）
$ coredumpctl list /usr/sbin/nginx --no-pager
$ for f in nginx php-fpm myapp java; do
>   n=$(coredumpctl list "$f" --no-legend 2>/dev/null | wc -l)
>   [ "$n" -gt 0 ] && echo "$f: $n 次崩溃"
> done

# 场景：🔐⭐⭐ 检查崩溃转储是否泄露敏感信息
$ coredumpctl dump -1 -o /tmp/c.core 2>/dev/null
$ strings /tmp/c.core | grep -iE 'password|passwd|secret|token|api[_-]?key|BEGIN.*PRIVATE' | head -10
$ strings /tmp/c.core | grep -E '[A-Za-z0-9+/]{40,}={0,2}' | head -5
$ # ⚠️ core dump 含进程完整内存 → 可能有口令、密钥、会话 token
$ # ⭐ 这就是「为什么生产环境要禁用 core dump」的原因

# 场景：🔐⭐⭐ 禁用 core dump（加固）
$ cat /proc/sys/kernel/core_pattern
|/usr/lib/systemd/systemd-coredump %P %u %g %s %t %c %h
$ ulimit -c
0                                # ⭐ 0 = 已禁用（好）

$ # 1. 用 limits.conf 禁用
$ sudo tee /etc/security/limits.d/99-nocore.conf <<'EOF'
*     soft    core    0
*     hard    core    0
root  soft    core    0
root  hard    core    0
EOF
$ # 2. 用 systemd 全局禁用
$ sudo systemctl mask systemd-coredump@.service systemd-coredump.socket
$ sudo tee /etc/sysctl.d/99-nocoredump.conf <<'EOF'
fs.suid_dumpable = 0
kernel.core_pattern = |/bin/false
EOF
$ sudo sysctl --system
$ # 3. 验证
$ ulimit -c
$ cat /proc/sys/kernel/core_pattern
$ systemctl is-enabled systemd-coredump.socket 2>/dev/null

# 场景：🔐 检查 SUID 程序的核心转储 ⭐
$ cat /proc/sys/fs/suid_dumpable
0                                # ⭐ 0 = 禁止（好）
$ # 1 = 允许（普通文件），2 = 允许（只有 root 可读）
$ # ⚠️ 非 0 时 SUID 程序（如 passwd）崩溃会 dump 出特权内存

# 场景：🔐 排查转储目录的权限与残留 ⭐
$ ls -la /var/lib/systemd/coredump/ | head
$ du -sh /var/lib/systemd/coredump/
$ sudo find /var/lib/systemd/coredump -type f -name 'core.*' -ls 2>/dev/null | head

# 场景：⭐ 清理与保留策略
$ sudo find /var/lib/systemd/coredump -name 'core.*' -mtime +7 -delete
$ cat /etc/systemd/coredump.conf
[Coredump]
Storage=external
Compress=yes
ProcessSizeMax=2G
ExternalSizeMax=2G
JournalSizeMax=767M
$ sudo tee /etc/systemd/coredump.conf.d/limits.conf <<'EOF'
[Coredump]
Storage=none
ProcessSizeMax=0
EOF
$ sudo systemctl daemon-reload && sudo systemctl restart systemd-journald

# 场景：🧪⭐⭐ 完整演示（制造崩溃并分析）
$ # 1. 准备一个会崩溃的程序
$ cat > /tmp/crash.c <<'EOF'
#include <stdio.h>
#include <string.h>
void f2(void) { char *p = NULL; strcpy(p, "boom"); }   /* 空指针写入 */
void f1(void) { f2(); }
int main(int argc, char **argv) {
    printf("starting, secret=SUPERSECRET123\n");
    fflush(stdout);
    if (argc > 1) f1();
    return 0;
}
EOF
$ gcc -g -O0 -o /tmp/crash /tmp/crash.c

$ # 2. 触发崩溃
$ sudo systemctl restart systemd-coredump.socket
$ /tmp/crash go
Segmentation fault (core dumped)

$ # 3. 分析
$ coredumpctl list -1 --no-pager
$ coredumpctl info -1 --no-pager | head -30
$ coredumpctl gdb -1 <<'EOF' 2>/dev/null
bt
info locals
quit
EOF

$ # 4. 检查泄露
$ coredumpctl dump -1 -o /tmp/leak.core 2>/dev/null
$ strings /tmp/leak.core | grep -i SUPERSECRET
$ # ⭐ 会看到 SUPERSECRET123 —— 证明 core dump 会泄露进程内存

$ # 5. 安全清理
$ shred -vfz /tmp/leak.core 2>/dev/null
$ rm -f /tmp/crash /tmp/crash.c

# 场景：🔐 检查系统上是否有意外的 core 文件（信息泄露排查）⭐
$ find / -xdev -type f \( -name 'core' -o -name 'core.*' \) 2>/dev/null | head -20
$ find / -xdev -type f -name 'core*' -size +1M 2>/dev/null | head
$ sudo find /var/lib/systemd/coredump /var/crash /tmp -name 'core*' -ls 2>/dev/null | head
$ # ⭐ 发现 core 文件时的处理流程：
$ #   1. 记录 hash 与来源（取证）
$ #   2. 分析（gdb 栈回溯）
$ #   3. 检查是否含敏感数据
$ #   4. 安全删除（shred）
$ sudo sha256sum /var/lib/systemd/coredump/core.myapp.*
```

#### 输出解读
`coredumpctl list` 的列：

| 列 | 含义 |
|----|------|
| `TIME` | 崩溃时间 ⭐ |
| `PID` / `UID` / `GID` | 进程信息 ⭐ |
| `SIG` | **信号** ⭐ |
| `COREFILE` | `present` / `missing` / `none` / `truncated` ⭐ |
| `EXE` | 可执行文件路径 ⭐ |
| `SIZE` | core 大小 |

**常见崩溃信号**：

| 信号 | 号 | 含义 |
|------|----|------|
| `SIGSEGV` | 11 | 段错误（非法内存访问） ⭐ |
| `SIGABRT` | 6 | 中止（`abort()`、assert 失败、未捕获异常） ⭐ |
| `SIGBUS` | 7 | 总线错误（对齐、mmap 越界） ⭐ |
| `SIGFPE` | 8 | 浮点异常（整数除零） |
| `SIGILL` | 4 | 非法指令 |
| `SIGSYS` | 31 | **非法系统调用（seccomp 拦截）** ⭐ |
| `SIGXFSZ` | 25 | 超过文件大小限制 |

**core 存储位置**：

| `Storage=` | 位置 |
|------------|------|
| `external`（默认） | `/var/lib/systemd/coredump/` ⭐ |
| `journal` | 存在 journal 里 |
| `none` | 不保存 ⭐（加固推荐） |

#### 🔐 安全要点
| 风险 | 说明 |
|------|------|
| **内存泄露** | core 含进程完整内存 → 口令、密钥、token、会话 ⚠️⭐⭐ |
| **SUID 程序** | `fs.suid_dumpable != 0` 时 SUID 程序崩溃会 dump 出特权内存 ⚠️⭐ |
| **磁盘占满** | 反复崩溃的应用会产出大量 core ⚠️ |
| **取证价值** | core 是「崩溃现场」，可看寄存器、栈、内存 ⭐ |
| **恶意利用** | 攻击者触发目标崩溃并用 core 提取密钥（如 `openssl` 的私钥） 🔐⭐ |

**加固清单**：
```bash
$ ulimit -c 0                                        # 当前 shell
$ grep -r core /etc/security/limits*.d/              # limits 配置
$ cat /proc/sys/fs/suid_dumpable                     # 应为 0
$ systemctl is-enabled systemd-coredump.socket       # 建议 mask
$ grep -A5 '^\[Coredump\]' /etc/systemd/coredump.conf
```

#### 常见坑
- ⚠️ **`coredumpctl` 需要 `systemd-coredump` 服务**（且 `core_pattern` 指向它）。用 `apport` 或其他方式时它看不到 ⭐。
- ⚠️ **`COREFILE` 显示 `missing` 说明 core 没保存**（`ulimit -c 0`、`Storage=none` 或空间不足）⭐。
- ⚠️ **`coredumpctl gdb` 需要 `gdb` 已安装**，且**目标程序要有调试符号**（否则栈回溯只有地址）⭐。
- ⚠️ **`Storage=none` 后 `coredumpctl list` 仍显示记录**（来自 journal），但 `COREFILE` 是 `none` ⭐。
- ⚠️ **core dump 可能含敏感数据**，分析完要安全删除（`shred`）🔐⭐。
- **`coredumpctl info` 的栈回溯来自 `libdw`**（不依赖外部 gdb）⭐。
- **要源码级调试需要 `-g` 编译 + debuginfo 包**，`debuginfod` 可自动下载 ⭐⭐：
  ```bash
  $ export DEBUGINFOD_URLS="https://debuginfod.example.com"
  $ coredumpctl debug -1
  ```
- **`coredumpctl dump` 会输出到 stdout**（要 `-o` 写文件）⭐。
- **容器里的 core 处理取决于容器配置**（通常没有 `systemd-coredump`）⭐。

#### 相关命令
`gdb` · `systemd-coredump` · `ulimit -c` · `core_pattern` · `debuginfod` · `abrt`

---

## 本分类自测

1. `myapp.service` 启动失败。写出完整的排查步骤（含 `systemctl`、`journalctl`、`systemd-analyze` 的具体命令）。
2. 修改 `nginx.service` 的文件描述符上限，要求升级时不丢失。写出命令与验证方法。
3. 说明 `systemctl enable`、`start`、`mask` 三者的区别，以及 `enable --now` 的作用。
4. 列出本机所有监听 socket 对应的 systemd 单元，并找出最近 7 天内被修改的单元文件。
5. 用 `systemd-run` 创建一个 5 分钟后执行的定时任务，并说明它是临时的还是持久的。
6. 用 `systemd-analyze security` 找出加固评分最差的前 3 个服务，并列出要加的加固项。
7. 增加 4G 交换文件后开启 journald 持久化日志，并验证能查到上次启动的日志。
8. 检查本机是否有 `enable-linger` 的用户（持久化排查），以及 `/etc/rc.local` 与 `tmpfiles.d` 是否被植入内容。
9. 导出最近一次崩溃的 core 文件，用 gdb 拿到栈回溯，并检查 core 里是否含明文凭据。
10. 说明为什么生产环境应该禁用 core dump，并给出完整的加固命令。

答案见 [`../practice/06-综合场景题.md`](../practice/06-综合场景题.md) 与 [`../practice/04-进程与系统题.md`](../practice/04-进程与系统题.md)。

## 相关文档

- [`../basics/07-系统启动与systemd.md`](../basics/07-系统启动与systemd.md)
- [`07-系统信息与内核.md`](07-系统信息与内核.md)（`journalctl`/`dmesg`/`sysctl`）
- [`12-安全与审计.md`](12-安全与审计.md)（持久化排查）
- [`14-容器与虚拟化.md`](14-容器与虚拟化.md)（`machinectl`/`nsenter`）

