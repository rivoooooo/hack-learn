# 07 · 系统启动与 systemd

> 命令手册：[`../commands/11-系统管理-systemd.md`](../commands/11-系统管理-systemd.md)、[`../commands/07-系统信息与内核.md`](../commands/07-系统信息与内核.md)。

---

## 1. 从加电到登录的完整链路

```
① 固件 POST（加电自检）
   传统 BIOS / 现代 UEFI
   ↓
② 引导加载程序 bootloader
   UEFI 直接加载 EFI 程序：/boot/efi/EFI/<distro>/grubx64.efi
   BIOS 读 MBR 的 boot.img → core.img
   二者最终都进入 GRUB 2
   ↓
③ GRUB 2
   读 /boot/grub/grub.cfg（不要手改，由 grub-mkconfig 生成）
   展示菜单 → 加载内核 vmlinuz 与 initramfs
   内核命令行参数来自 GRUB_CMDLINE_LINUX
   ↓
④ 内核初始化
   解压自身、探测硬件、挂载 initramfs 作为临时根
   执行 /init
   ↓
⑤ initramfs
   加载真实根文件系统所需的驱动（存储控制器、LVM、LUKS、RAID）
   找到并挂载真实根 → switch_root → 执行 /sbin/init
   ↓
⑥ init（PID 1）
   现代发行版 = systemd（也可能已切换为独立的 systemd 二进制）
   ↓
⑦ systemd 按默认 target 启动 unit
   ↓
⑧ getty / display-manager 提供登录
   ↓
⑨ PAM 验证 → 启动用户登录 shell（见 05-环境变量与Shell启动过程.md）
```

### 各阶段对应的排查命令

| 阶段 | 排查方式 |
|------|----------|
| 固件 | `sudo dmidecode -t bios`、UEFI 下 `efibootmgr -v` |
| GRUB | 启动菜单按 `e` 编辑，`Ctrl+X` 启动；`grub-mkconfig` 重新生成 |
| 内核命令行 | `cat /proc/cmdline` |
| initramfs | `lsinitcpio -l`（Arch）、`lsinitramfs`（Debian） |
| systemd | `systemd-analyze blame`、`systemctl --failed` |

```bash
# 查看当前内核启动参数
$ cat /proc/cmdline
BOOT_IMAGE=/vmlinuz-linux root=UUID=abcd-1234 rw loglevel=3 quiet

# 分析启动耗时
$ systemd-analyze
Startup finished in 3.201s (firmware) + 1.104s (loader) + 2.883s (kernel) + 4.517s (userspace) = 11.706s
$ systemd-analyze blame | head -10
$ systemd-analyze critical-chain

# 看某次启动的日志
$ journalctl -b              # 本次
$ journalctl -b -1           # 上次（崩溃后必看）⭐
$ journalctl --list-boots    # 所有启动记录
```

⚠️ **系统起不来时的三大救急手段**：

1. GRUB 菜单按 `e`，在内核命令行末尾加 `systemd.unit=rescue.target`（或 `emergency.target`）、`single`、`init=/bin/bash`。
2. 加 `rd.break` 停在 initramfs。
3. 用 Live USB 挂载原系统，`chroot` 进去修。

在 GRUB 里编辑的**只是本次生效**，修好后要写进 `/etc/default/grub` 并重新生成。

---

## 2. systemd 的核心理念

systemd 用 **unit（单元）** 描述一切可管理对象，按后缀分类型：

| 后缀 | 类型 | 说明 |
|------|------|------|
| `.service` | 服务 | 最常用，一个守护进程 |
| `.socket` | 套接字 | 按需启动（socket activation） |
| `.timer` | 定时器 | 替代 cron |
| `.target` | 目标 | 一组 unit 的集合，类似「运行级别」 |
| `.mount` | 挂载点 | 来自 `/etc/fstab` 的挂载，名称是路径转义 |
| `.automount` | 自动挂载 | 按需挂载 |
| `.device` | 设备 | 由 udev 生成 |
| `.path` | 路径监视 | 文件变化时触发 |
| `.slice` | 资源切片 | cgroup 分组 |
| `.scope` | 外部进程组 | 由 systemd 外部创建 |
| `.swap` | 交换分区 | — |

### 关键关系

| 指令 | 含义 |
|------|------|
| `Requires=` | 强依赖，被依赖者失败则本单元失败 |
| `Wants=` | 弱依赖，失败不影响本单元（**更常用**） |
| `After=` / `Before=` | 只定义顺序，不定义依赖 |
| `PartOf=` | 随目标单元一起启停 |
| `Conflicts=` | 互斥 |
| `BindsTo=` | 比 Requires 更强，对方停止则本单元也停 |

💡 **`After=` 和 `Requires=` 是两件不同的事**。想「等网络起来再启动」应该写 `After=network-online.target` + `Wants=network-online.target`；只写 `Requires=` 不保证顺序。

---

## 3. Unit 文件

### 搜索路径（优先级从高到低）

```
/etc/systemd/system/           # 管理员创建的，最高优先级
/run/systemd/system/           # 运行时生成
/usr/lib/systemd/system/       # 发行版/包管理器安装的
```

```bash
# 确认某 unit 实际用的是哪个文件
$ systemctl cat nginx
$ systemctl show -p FragmentPath nginx
```

### 一个完整的 service

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Application Server
Documentation=man:myapp(8) https://example.com/docs
After=network-online.target
Wants=network-online.target
RequiresMountsFor=/srv/myapp

[Service]
Type=simple
User=myapp
Group=myapp
WorkingDirectory=/srv/myapp
Environment=NODE_ENV=production
EnvironmentFile=-/etc/myapp/env
ExecStartPre=/usr/bin/myapp --check-config
ExecStart=/usr/bin/myapp --foreground
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5s
TimeoutStopSec=30
StandardOutput=journal
StandardError=journal
SyslogIdentifier=myapp

# 资源限制
MemoryMax=1G
CPUQuota=150%
TasksMax=256
LimitNOFILE=65535

# 加固
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/srv/myapp/data
ProtectKernelTunables=true
ProtectControlGroups=true
RestrictSUIDSGID=true
SystemCallFilter=@system-service
CapabilityBoundingSet=CAP_NET_BIND_SERVICE

[Install]
WantedBy=multi-user.target
```

### `Type=` 的选择

| Type | 行为 | 适用 |
|------|------|------|
| `simple`（默认） | `ExecStart` 一启动就算 ok | 前台运行的守护进程 |
| `exec` | 等 `execve()` 成功才算 ok | 比 simple 更准确，推荐 |
| `forking` | 进程 fork 并父进程退出后算 ok | 传统「自己后台化」的守护进程 |
| `oneshot` | 执行完退出才算成功 | 一次性任务（配 `RemainAfterExit=yes`） |
| `notify` | 等进程用 `sd_notify()` 报告就绪 | 支持 systemd 通知的服务 |
| `dbus` | 等获取 D-Bus 名称 | D-Bus 服务 |
| `idle` | 等其他任务完成 | 输出串行化 |

⚠️ **Type 写错是最常见的「服务反复重启」原因**：把 `simple` 用在会自己 daemonize 的程序上，systemd 会以为主进程退出了，反复重启。

### `Restart=` 策略

| 值 | 何时重启 |
|----|----------|
| `no`（默认） | 从不 |
| `on-failure` | 非零退出码、被信号杀、超时 ⭐ 最常用 |
| `always` | 任何退出（含正常退出） |
| `on-abnormal` | 被信号或超时 |
| `on-watchdog` | 看门狗超时 |

配合 `RestartSec=` 防止疯狂重启。防止无限重启循环可用 `StartLimitBurst=` / `StartLimitIntervalSec=`（在 `[Unit]` 段）。

### `[Install]` 段

只在 `systemctl enable` 时被读取，决定「被 enable 时创建什么符号链接」。

```bash
# 改完 unit 文件必须做这个
$ sudo systemctl daemon-reload
```

⚠️ **`daemon-reload` 是绝对的必做项**。改了 unit 文件不 reload，systemd 仍用旧配置，会出现「我明明改了但没生效」的诡异现象。

---

## 4. 常用 systemctl 操作

```bash
# 生命周期
$ sudo systemctl start nginx
$ sudo systemctl stop nginx
$ sudo systemctl restart nginx
$ sudo systemctl reload nginx          # 重载配置（不中断连接，需服务支持）
$ sudo systemctl reload-or-restart nginx
$ sudo systemctl try-restart nginx

# 开机自启
$ sudo systemctl enable nginx          # 创建符号链接
$ sudo systemctl disable nginx
$ sudo systemctl enable --now nginx    # 启用并立即启动 ⭐
$ systemctl is-enabled nginx

# 状态
$ systemctl status nginx               # 状态 + 最近日志
$ systemctl is-active nginx
$ systemctl is-failed nginx
$ systemctl list-units --failed        # 找故障单元 ⭐
$ systemctl list-units --type=service --state=running
$ systemctl list-unit-files --state=enabled
$ systemctl list-dependencies nginx    # 依赖树

# 屏蔽（比 disable 更强，防止被其他单元拉起）
$ sudo systemctl mask nginx
$ sudo systemctl unmask nginx

# 用户级服务（不需要 root）
$ systemctl --user status myapp
$ systemctl --user enable --now myapp
$ loginctl enable-linger alice         # 允许用户服务在未登录时运行 ⭐

# 不写 unit 文件直接跑一个服务（临时/测试）
$ sudo systemd-run --unit=test --property=MemoryMax=100M /usr/bin/stress-ng
$ systemd-run --user --on-active=5m /usr/bin/notify-send "5 分钟后提醒"
```

### 修改现有 unit 而不覆盖原文件

```bash
# 方式一：drop-in（推荐，升级不丢失）
$ sudo systemctl edit nginx            # 生成 /etc/systemd/system/nginx.service.d/override.conf
[Service]
LimitNOFILE=65535
$ sudo systemctl daemon-reload && sudo systemctl restart nginx

# 方式二：整体替换（升级时可能被覆盖）
$ sudo systemctl edit --full nginx
```

💡 **永远优先用 drop-in**。直接改 `/usr/lib/systemd/system/nginx.service` 会在包升级时被覆盖，且 `systemctl status` 会提示 "unit file changed on disk"。

---

## 5. target：运行级别的替代

| target | 大致等价旧运行级 | 说明 |
|--------|------------------|------|
| `poweroff.target` | 0 | 关机 |
| `rescue.target` | 1 | 单用户，基础文件系统，需 root 密码 |
| `multi-user.target` | 3 | 多用户命令行（**服务器默认**） |
| `graphical.target` | 5 | 图形界面（**桌面默认**） |
| `reboot.target` | 6 | 重启 |
| `emergency.target` | S | 只挂载根（只读），最简救援 |
| `default.target` | — | 指向实际默认 target 的符号链接 |

```bash
# 查看当前 target
$ systemctl get-default

# 切换（本次生效）
$ sudo systemctl isolate multi-user.target
$ sudo systemctl isolate rescue.target

# 改默认
$ sudo systemctl set-default multi-user.target

# 关机/重启（等价于 systemctl start reboot.target）
$ sudo systemctl reboot
$ sudo systemctl poweroff
$ sudo systemctl halt
```

`shutdown` / `reboot` / `poweroff` / `halt` 现在都是 systemd 的符号链接或包装。

```bash
$ sudo shutdown -h now         # 立刻关机
$ sudo shutdown -h +10         # 10 分钟后
$ sudo shutdown -r 02:00       # 定时重启
$ sudo shutdown -c             # 取消定时
$ sudo shutdown -h +5 "维护公告"   # 给所有登录用户发消息
$ sudo wall "5 分钟后重启"      # 广播消息
```

---

## 6. journalctl：日志检索

systemd 的日志服务 **journald** 收集内核、服务、用户会话日志，默认存在 `/var/log/journal/`（持久）或 `/run/log/journal/`（内存，重启丢失）。

```bash
# 基础
$ journalctl                       # 全部
$ journalctl -e                    # 跳到末尾
$ journalctl -f                    # 实时跟随（类似 tail -f）⭐
$ journalctl -n 50                 # 最后 50 行
$ journalctl -r                    # 倒序（最新在前）

# 时间过滤
$ journalctl --since "1 hour ago"
$ journalctl --since today
$ journalctl --since "2026-09-01" --until "2026-09-02 12:00"
$ journalctl -S -30min             # -S = --since，-U = --until

# 来源过滤
$ journalctl -u nginx              # 单个 unit ⭐
$ journalctl -u nginx -u php-fpm   # 多个 unit
$ journalctl -t sudo               # 按 syslog identifier
$ journalctl -k                    # 只内核消息（等于 dmesg）
$ journalctl _PID=1234             # 按字段
$ journalctl _UID=1000
$ journalctl /usr/bin/sshd         # 按可执行文件路径 ⭐

# 优先级
$ journalctl -p err                # err 及以上
$ journalctl -p warning..err       # 范围
$ journalctl -u nginx -p err -b

# 启动会话
$ journalctl -b                    # 本次启动
$ journalctl -b -1                 # 上次启动 ⭐
$ journalctl --list-boots

# 输出格式
$ journalctl -o json-pretty        # JSON，给脚本用 ⭐
$ journalctl -o short-precise      # 微秒精度
$ journalctl -o cat                # 只有消息体
$ journalctl -x                    # 加解释性提示（含 man 链接）⭐
$ journalctl -o verbose            # 全部元数据字段

# 磁盘占用与清理
$ journalctl --disk-usage
$ sudo journalctl --vacuum-size=500M
$ sudo journalctl --vacuum-time=30d
```

### 优先级编号

| 编号 | 名称 | 含义 |
|------|------|------|
| 0 | emerg | 系统不可用 |
| 1 | alert | 需立即处理 |
| 2 | crit | 严重 |
| 3 | err | 错误 |
| 4 | warning | 警告 |
| 5 | notice | 正常但重要 |
| 6 | info | 信息 |
| 7 | debug | 调试 |

### 持久化日志

默认在部分发行版上只存内存。开启持久化：

```bash
$ sudo mkdir -p /var/log/journal
$ sudo systemd-tmpfiles --create --prefix /var/log/journal
$ sudo systemctl restart systemd-journald
# 或在 /etc/systemd/journald.conf 里设 Storage=persistent
```

🔐 **应急响应中 journalctl 的价值**：

```bash
# 谁在什么时候登录过
$ journalctl -u sshd --since "7 days ago" | grep -i 'accepted\|failed'

# 某用户的 sudo 操作
$ journalctl _UID=1000 -t sudo

# 服务崩溃前的最后消息
$ journalctl -u myapp -b -1 -n 100

# 谁执行了某命令（需 auditd，见 12-安全与审计.md）
$ ausearch -x /usr/bin/curl -ts today
```

⚠️ **journald 默认不记录所有命令执行**，它记录的是服务/内核/会话事件。要审计命令执行必须装 **auditd**（`-a exit,always -F arch=b64 -S execve`）或开启 bash 的 `PROMPT_COMMAND` 记录。

⚠️ 攻击者拿 root 后可以 `journalctl --rotate && journalctl --vacuum-time=1s` 清掉日志。所以**关键日志必须实时转发到远端**（rsyslog / journald 的 `ForwardToSyslog`）。

---

## 7. 定时任务：timer 替代 cron

### systemd timer

```ini
# /etc/systemd/system/backup.timer
[Unit]
Description=Daily backup

[Timer]
OnCalendar=daily
Persistent=true
RandomizedDelaySec=1h

[Install]
WantedBy=timers.target
```

```ini
# /etc/systemd/system/backup.service
[Unit]
Description=Daily backup job

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup.sh
```

```bash
$ sudo systemctl enable --now backup.timer
$ systemctl list-timers --all          # 查看所有定时器与下次触发时间 ⭐
```

`OnCalendar` 语法：

| 写法 | 含义 |
|------|------|
| `daily` | 每天 00:00 |
| `weekly` | 每周一 00:00 |
| `*-*-* 03:00:00` | 每天 3 点 |
| `Mon..Fri 09:00` | 工作日 9 点 |
| `*:0/15` | 每 15 分钟 |
| `OnBootSec=5min` | 启动后 5 分钟 |
| `OnUnitActiveSec=1h` | 上次运行后 1 小时 |

```bash
# 验证表达式是否合法，并看接下来 5 次触发时间
$ systemd-analyze calendar 'Mon..Fri 09:00'
```

### timer vs cron

| 维度 | cron | systemd timer |
|------|------|---------------|
| 错过的任务 | ❌ 直接跳过 | ✅ `Persistent=true` 会补跑 |
| 日志 | 邮件（常失效） | 自动进 journal ⭐ |
| 依赖其他服务 | ❌ | ✅ `After=` |
| 资源限制 | ❌ | ✅ cgroup |
| 随机延迟 | 需自己写 | ✅ `RandomizedDelaySec` |
| 精确到秒 | ❌ 最小 1 分钟 | ✅ |
| 学习成本 | 低 | 中 |

### cron 关键点

```bash
$ crontab -e            # 编辑当前用户
$ crontab -l            # 列出
$ sudo crontab -e -u alice   # 编辑指定用户（root）
$ crontab -r            # ⚠️ 删除全部，没有确认！高危误操作
```

```
# ┌─ 分 (0-59)
# │ ┌─ 时 (0-23)
# │ │ ┌─ 日 (1-31)
# │ │ │ ┌─ 月 (1-12)
# │ │ │ │ ┌─ 周 (0-7，0 和 7 都是周日)
# * * * * * command
```

| 特殊写法 | 含义 |
|----------|------|
| `@reboot` | 启动时 |
| `@daily` / `@midnight` | 每天 0 点 |
| `@weekly` / `@monthly` / `@yearly` | — |
| `*/5` | 每 5 单位 |
| `1-5` | 范围 |
| `1,15` | 列举 |

系统级 cron 目录：`/etc/cron.d/`、`/etc/cron.{hourly,daily,weekly,monthly}/`、`/etc/crontab`（比用户 crontab 多一个「用户」字段）。

```bash
# 排查 cron 不执行
$ journalctl -u cron -u crond -n 50      # 有没有被调度
$ grep CRON /var/log/syslog              # Debian
$ sudo grep cron /var/log/cron           # RHEL
$ sudo grep CRON /var/log/cron.log       # 部分发行版
```

⚠️ **cron 环境极简**：PATH 常只有 `/usr/bin:/bin`，不加载 `.bashrc`。脚本里用绝对路径，或在 `crontab` 顶部设 `PATH=`。永忘不掉的第一大 cron 坑。

🔐 **cron 是持久化后门的热门位置**，排查要点：

```bash
$ for u in $(cut -d: -f1 /etc/passwd); do echo "== $u"; sudo crontab -l -u "$u" 2>/dev/null; done
$ ls -la /etc/cron.* /var/spool/cron/* 2>/dev/null
$ cat /etc/cron.d/* /etc/crontab
$ cat /etc/at.allow /etc/at.deny 2>/dev/null
$ sudo systemctl list-timers --all
$ ls -la /etc/systemd/system/*.timer /usr/lib/systemd/system/*.timer
```

---

## 8. 常见启动故障诊断流程

```bash
# 1. 有故障单元吗
$ systemctl --failed

# 2. 看该单元的完整状态与最近日志
$ systemctl status <unit> -l --no-pager
$ journalctl -u <unit> -b --no-pager

# 3. 为什么启动慢
$ systemd-analyze blame | head -20

# 4. 卡在哪个依赖
$ systemd-analyze critical-chain <unit>

# 5. 手动前台运行，看真实错误（绕过 systemd 的环境差异）
$ sudo -u <user> /usr/bin/<binary> --foreground

# 6. 检查 unit 语法
$ systemd-analyze verify /etc/systemd/system/myapp.service
```

| 症状 | 常见原因 |
|------|----------|
| `Failed to start ...: Unit not found` | unit 名拼错、未 `daemon-reload`、未 `enable` |
| 启动后立即退出、反复重启 | `Type=` 写错、程序自己 fork 了、工作目录/环境变量缺失 |
| `status=203/EXEC` | `ExecStart` 路径不存在或不可执行 |
| `status=200/CHDIR` | `WorkingDirectory` 不存在 |
| `status=226/NAMESPACE` | 加固项（`ProtectSystem` 等）与程序实际需求冲突 |
| `code=exited, status=1/FAILURE` | 程序自身错误，看应用日志 |
| 手动能跑，systemd 不能 | 环境变量/绝对路径/用户权限差异 ⭐ 最常见 |

---

## 9. 自查清单

- [ ] 能背出启动链路：固件 → bootloader → 内核 → initramfs → init → target
- [ ] 知道 unit 文件三个搜索路径的优先级
- [ ] 知道 `daemon-reload` 什么时候必须做
- [ ] 知道 `simple` / `forking` / `oneshot` / `notify` 的差异
- [ ] 知道 `After=` 不等于 `Requires=`
- [ ] 会用 `systemctl edit` 做 drop-in 而不是直接改系统文件
- [ ] 会用 `journalctl -u X -b -1 -p err` 组合定位上次启动的错误
- [ ] 知道 cron 环境极简、`crontab -r` 无确认
- [ ] 知道 root 可以清 journal，所以关键日志要远端转发

## 相关文档

- [`../commands/11-系统管理-systemd.md`](../commands/11-系统管理-systemd.md)
- [`../commands/12-安全与审计.md`](../commands/12-安全与审计.md)
- [`../practice/06-综合场景题.md`](../practice/06-综合场景题.md)
