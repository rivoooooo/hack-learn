# sipp

> Traffic generator for the SIP protocol SIPp is a free Open Source test tool / traffic generator for the SIP protocol. It includes a few basic SipStone user agent scenarios (UAC and UAS) and establishes and releases multiple calls with the …

> **功能分类**：漏洞分析 ｜ **Kali 包**：`sipp` ｜ **官方文档**：<https://www.kali.org/tools/sipp/>

## 1. 安装

```bash
sudo apt update
sudo apt install sipp
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.3 |
| 架构 | any |
| 可执行命令 | `sipp` |
| 依赖 | `libc6`、`libgcc-s1`、`libncurses6`、`libpcap0.8t64`、`libstdc++6`、`libtinfo6` |
| 安装体积 | 735 KB |
| 官网 | <https://sipp.sourceforge.net/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sipp> |
| 包追踪 | <https://pkg.kali.org/pkg/sipp> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Run sipp using the embedded server (-sn uas) scenario:
root@kali:~# sipp -sn uas
Warning: open file limit > FD_SETSIZE; limiting max. # of open files to FD_SETSIZE = 1024
------------------------------ Scenario Screen -------- [1-9]: Change Screen --
  Port   Total-time  Total-calls  Transport
  5060      11.94 s            0  UDP

  0 new calls during 0.926 s period      1 ms scheduler resolution
  0 calls                                Peak was 0 calls, after 0 s
  0 Running, 2 Paused, 2 Woken up
  0 dead call msg (discarded)
  3 open sockets

                                 Messages  Retrans   Timeout   Unexpected-Msg
  ----------> INVITE             0         0         0         0

  <---------- 180                0         0
  <---------- 200                0         0         0
  ----------> ACK         E-RTD1 0         0         0         0

  ----------> BYE                0         0         0         0
  <---------- 200                0         0
  [   4000ms] Pause              0                             0
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sipp`

> 官方示例调用：`sipp -sn uas`

```text
root@kali:~# sipp -sn uas
Warning: open file limit > FD_SETSIZE; limiting max. # of open files to FD_SETSIZE = 1024
------------------------------ Scenario Screen -------- [1-9]: Change Screen --
  Port   Total-time  Total-calls  Transport
  5060      11.94 s            0  UDP
  0 new calls during 0.926 s period      1 ms scheduler resolution
  0 calls                                Peak was 0 calls, after 0 s
  0 Running, 2 Paused, 2 Woken up
  0 dead call msg (discarded)
  3 open sockets
                                 Messages  Retrans   Timeout   Unexpected-Msg
  ----------> INVITE             0         0         0         0
  <---------- 180                0         0
  <---------- 200                0         0         0
  ----------> ACK         E-RTD1 0         0         0         0
  ----------> BYE                0         0         0         0
  <---------- 200                0         0
  [   4000ms] Pause              0                             0
```

### `sipp -h`

> 官方示例调用：`sipp -h`

```text
root@kali:~# sipp -h
Usage:
  sipp remote_host[:remote_port] [options]
  Available options:
   -v               : Display version and copyright information.
   -aa              : Enable automatic 200 OK answer for INFO, UPDATE and
                      NOTIFY messages.
   -auth_uri        : Force the value of the URI for authentication.
                      By default, the URI is composed of
                      remote_ip:remote_port.
   -au              : Set authorization username for authentication challenges.
                      Default is taken from -s argument
   -ap              : Set the password for authentication challenges. Default
                      is 'password'
   -base_cseq       : Start value of [cseq] for each call.
   -bg              : Launch SIPp in background mode.
   -bind_local      : Bind socket to local IP address, i.e. the local IP
                      address is used as the source IP address.  If SIPp runs
                      in server mode it will only listen on the local IP
                      address instead of all IP addresses.
   -buff_size       : Set the send and receive buffer size.
   -calldebug_file  : Set the name of the call debug file.
   -calldebug_overwrite: Overwrite the call debug file (default true).
   -cid_str         : Call ID string (default %u-%p@%s).  %u=call_number,
                      %s=ip_address, %p=process_number, %%=% (in any order).
   -ci              : Set the local control IP address
   -cp              : Set the local control port number. Default is 8888.
   -d               : Controls the length of calls. More precisely, this
                      controls the duration of 'pause' instructions in the
                      scenario, if they do not have a 'milliseconds' section.
                      Default value is 0 and default unit is milliseconds.
   -deadcall_wait   : How long the Call-ID and final status of calls should be
                      kept to improve message and error logs (default unit is
                      ms).
   -default_behaviors: Set the default behaviors that SIPp will use.  Possbile
                      values are:
                      - all	Use all default behaviors
                      - none	Use no default behaviors
                      - bye	Send byes for aborted calls
                      - abortunexp	Abort calls on unexpected messages
                      - pingreply	Reply to ping requests
                      If a behavior is prefaced with a -, then it is turned
                      off.  Example: all,-bye
   -error_file      : Set the name of the error log file.
   -error_overwrite : Overwrite the error log file (default true).
   -f               : Set the statistics report frequency on screen. Default is
                      1 and default unit is seconds.
   -fd              : Set the statistics dump log report frequency. Default is
                      60 and default unit is seconds.
   -i               : Set the local IP address for 'Contact:','Via:', and
                      'From:' headers. Default is primary host IP address.
   -inf             : Inject values from an external CSV file during calls into
                      the scenarios.
                      First line of this file say whether the data is to be
                      read in sequence (SEQUENTIAL), random (RANDOM), or user
                      (USER) order.
                      Each line corresponds to one call and has one or more
                      ';' delimited data fields. Those fields can be referred
                      as [field0], [field1], ... in the xml scenario file.
                      Several CSV files can be used simultaneously (syntax:
                      -inf f1.csv -inf f2.csv ...)
   -infindex        : file field
                      Create an index of file using field.  For example -inf
                      users.csv -infindex users.csv 0 creates an index on the
                      first key.
   -ip_field        : Set which field from the injection file contains the IP
                      address from which the client will send its messages.
                      If this option is omitted and the '-t ui' option is
                      present, then field 0 is assumed.
                      Use this option together with '-t ui'
   -l               : Set the maximum number of simultaneous calls. Once this
                      limit is reached, traffic is decreased until the number
                      of open calls goes down. Default:
                        (3 * call_duration (s) * rate).
   -log_file        : Set the name of the log actions log file.
   -log_overwrite   : Overwrite the log actions log file (default true).
   -lost            : Set the number of packets to lose by default (scenario
                      specifications override this value).
   -rtcheck         : Select the retransmisison detection method: full
                      (default) or loose.
   -m               : Stop the test and exit when 'calls' calls are processed
   -mi              : Set the local media IP address (default: local primary
                      host IP address)
   -master          : 3pcc extended mode: indicates the master number
   -max_recv_loops  : Set the maximum number of messages received read per
                      cycle. Increase this value for high traffic level.  The
                      default value is 1000.
   -max_sched_loops : Set the maximum number of calsl run per event loop.
                      Increase this value for high traffic level.  The default
                      value is 1000.
   -max_reconnect   : Set the the maximum number of reconnection.
   -max_retrans     : Maximum number of UDP retransmissions before call ends on
                      timeout.  Default is 5 for INVITE transactions and 7 for
                      others.
   -max_invite_retrans: Maximum number of UDP retransmissions for invite
                      transactions before call ends on timeout.
   -max_non_invite_retrans: Maximum number of UDP retransmissions for non-invite
                      transactions before call ends on timeout.
   -max_log_size    : What is the limit for error and message log file sizes.
   -max_socket      : Set the max number of sockets to open simultaneously.
                      This option is significant if you use one socket per
                      call. Once this limit is reached, traffic is distributed
                      over the sockets already opened. Default value is 50000
   -mb              : Set the RTP echo buffer size (default: 2048).
   -message_file    : Set the name of the message log file.
   -message_overwrite: Overwrite the message log file (default true).
   -mp              : Set the local RTP echo port number. Default is 6000.
   -nd              : No Default. Disable all default behavior of SIPp which
                      are the following:
                      - On UDP retransmission timeout, abort the call by
                        sending a BYE or a CANCEL
                      - On receive timeout with no ontimeout attribute, abort
                        the call by sending a BYE or a CANCEL
                      - On unexpected BYE send a 200 OK and close the call
                      - On unexpected CANCEL send a 200 OK and close the call
                      - On unexpected PING send a 200 OK and continue the call
                      - On any other unexpected message, abort the call by
                        sending a BYE or a CANCEL
   -nr              : Disable retransmission in UDP mode.
   -nostdin         : Disable stdin.
   -p               : Set the local port number.  Default is a random free port
                      chosen by the system.
   -pause_msg_ign   : Ignore the messages received during a pause defined in
                      the scenario
   -periodic_rtd    : Reset response time partition counters each logging
                      interval.
   -plugin          : Load a plugin.
   -r               : Set the call rate (in calls per seconds).  This value can
                      bechanged during test by pressing '+','_','*' or '/'.
                      Default is 10.
                      pressing '+' key to increase call rate by 1 *
                      rate_scale,
                      pressing '-' key to decrease call rate by 1 *
                      rate_scale,
                      pressing '*' key to increase call rate by 10 *
                      rate_scale,
                      pressing '/' key to decrease call rate by 10 *
                      rate_scale.
                      If the -rp option is used, the call rate is calculated
                      with the period in ms given by the user.
   -rp              : Specify the rate period for the call rate.  Default is 1
                      second and default unit is milliseconds.  This allows
                      you to have n calls every m milliseconds (by using -r n
                      -rp m).
                      Example: -r 7 -rp 2000 ==> 7 calls every 2 seconds.
                               -r 10 -rp 5s => 10 calls every 5 seconds.
   -rate_scale      : Control the units for the '+', '-', '*', and '/' keys.
   -rate_increase   : Specify the rate increase every -fd units (default is
                      seconds).  This allows you to increase the load for each
                      independent logging period.
                      Example: -rate_increase 10 -fd 10s
                        ==> increase calls by 10 every 10 seconds.
   -rate_max        : If -rate_increase is set, then quit after the rate
                      reaches this value.
                      Example: -rate_increase 10 -rate_max 100
                        ==> increase calls by 10 until 100 cps is hit.
   -no_rate_quit    : If -rate_increase is set, do not quit after the rate
                      reaches -rate_max.
   -recv_timeout    : Global receive timeout. Default unit is milliseconds. If
                      the expected message is not received, the call times out
                      and is aborted.
   -send_timeout    : Global send timeout. Default unit is milliseconds. If a
                      message is not sent (due to congestion), the call times
                      out and is aborted.
   -sleep           : How long to sleep for at startup. Default unit is
                      seconds.
   -reconnect_close : Should calls be closed on reconnect?
   -reconnect_sleep : How long (in milliseconds) to sleep between the close and
                      reconnect?
   -ringbuffer_files: How many error/message files should be kept after
                      rotation?
   -ringbuffer_size : How large should error/message files be before they get
                      rotated?
   -rsa             : Set the remote sending address to host:port for sending
                      the messages.
   -rtp_echo        : Enable RTP echo. RTP/UDP packets received on port defined
                      by -mp are echoed to their sender.
                      RTP/UDP packets coming on this port + 2 are also echoed
                      to their sender (used for sound and video echo).
   -rtt_freq        : freq is mandatory. Dump response times every freq calls
                      in the log file defined by -trace_rtt. Default value is
                      200.
   -s               : Set the username part of the resquest URI. Default is
                      'service'.
   -sd              : Dumps a default scenario (embeded in the sipp executable)
   -sf              : Loads an alternate xml scenario file.  To learn more
                      about XML scenario syntax, use the -sd option to dump
                      embedded scenarios. They contain all the necessary help.
   -shortmessage_file: Set the name of the short message log file.
   -shortmessage_overwrite: Overwrite the short message log file (default true).
   -oocsf           : Load out-of-call scenario.
   -oocsn           : Load out-of-call scenario.
   -skip_rlimit     : Do not perform rlimit tuning of file descriptor limits.
                      Default: false.
   -slave           : 3pcc extended mode: indicates the slave number
   -slave_cfg       : 3pcc extended mode: indicates the file where the master
                      and slave addresses are stored
   -sn              : Use a default scenario (embedded in the sipp executable).
                      If this option is omitted, the Standard SipStone UAC
                      scenario is loaded.
                      Available values in this version:
                      - 'uac'      : Standard SipStone UAC (default).
                      - 'uas'      : Simple UAS responder.
                      - 'regexp'   : Standard SipStone UAC - with regexp and
                        variables.
                      - 'branchc'  : Branching and conditional branching in
                        scenarios - client.
                      - 'branchs'  : Branching and conditional branching in
                        scenarios - server.
                      Default 3pcc scenarios (see -3pcc option):
                      - '3pcc-C-A' : Controller A side (must be started after
                        all other 3pcc scenarios)
                      - '3pcc-C-B' : Controller B side.
                      - '3pcc-A'   : A side.
                      - '3pcc-B'   : B side.
   -stat_delimiter  : Set the delimiter for the statistics file
   -stf             : Set the file name to use to dump statistics
   -t               : Set the transport mode:
                      - u1: UDP with one socket (default),
                      - un: UDP with one socket per call,
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install sipp`，再执行 `sipp --version` 2>/dev/null || `sipp -V`
- [ ] **2.** **读官方帮助** —— `sipp -h`，需要细节时 `man sipp`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sipp/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sipp/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sipp/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
