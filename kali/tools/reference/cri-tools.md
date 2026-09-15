# cri-tools

> Command line tool used for creating OCI images This package contains a series of debugging and validation tools for Kubelet CRI, which includes: crictl: CLI for kubelet CRI. critest: validation test suites for kubelet CRI.

> **功能分类**：通用工具 ｜ **Kali 包**：`cri-tools` ｜ **官方文档**：<https://www.kali.org/tools/cri-tools/>

## 1. 安装

```bash
sudo apt update
sudo apt install cri-tools
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.36.0 |
| 架构 | any |
| 可执行命令 | `cri-tools`、`crictl`、`critest` |
| 安装体积 | 53.62 MB |
| 官网 | <https://github.com/kubernetes-sigs/cri-tools> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/cri-tools> |
| 包追踪 | <https://pkg.kali.org/pkg/cri-tools> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
cri-tools -h          # 查看用法
man cri-tools         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `crictl`

> 官方示例调用：`crictl -h`

```text
root@kali:~# crictl -h
NAME:
   crictl - client for CRI
USAGE:
   crictl [global options] command [command options]
COMMANDS:
   attach                 Attach to a running container
   checkpoint             Checkpoint one or more running containers
   completion             Output shell completion code
   config                 Get, set and list crictl configuration options
   create                 Create a new container
   events, event          Stream the events of containers
   exec                   Run a command in a running container
   imagefsinfo            Return image filesystem info
   images, image, img     List images
   info                   Display information of the container runtime
   inspect                Display the status of one or more containers
   inspecti               Return the status of one or more images
   inspectp               Display the status of one or more pods
   logs                   Fetch the logs of a container
   metricdescs            List metric descriptors. Returns information about the metrics available through the CRI.
   metricsp               List pod metrics. Metrics are unstructured key/value pairs gathered by CRI meant to replace cAdvisor's /metrics/cadvisor endpoint.
   pods                   List pods
   port-forward           Forward local port to a pod
   ps                     List containers
   pull                   Pull an image from a registry
   rm                     Remove one or more containers
   rmi                    Remove one or more images
   rmp                    Remove one or more pods
   run                    Run a new container inside a sandbox
   runp                   Run a new pod
   runtime-config         Retrieve the container runtime configuration
   start                  Start one or more created containers
   stats                  List container(s) resource usage statistics
   statsp                 List pod statistics. Stats represent a structured API that will fulfill the Kubelet's /stats/summary endpoint.
   stop                   Stop one or more running containers
   stopp                  Stop one or more running pods
   update                 Update one or more running containers
   update-runtime-config  Update the runtime configuration
   version                Display runtime version information
   help, h                Shows a list of commands or help for one command
GLOBAL OPTIONS:
   --config value, -c value                   Location of the client config file. If not specified and the default does not exist, the program's directory is searched as well (default: "/etc/crictl.yaml") [$CRI_CONFIG_FILE]
   --debug, -D                                Enable debug mode (default: false)
   --enable-tracing                           Enable OpenTelemetry tracing. (default: false)
   --image-endpoint value, -i value           Endpoint of CRI image manager service (default: uses 'runtime-endpoint' setting) [$IMAGE_SERVICE_ENDPOINT]
   --profile-cpu value                        Write a pprof CPU profile to the provided path.
   --profile-mem value                        Write a pprof memory profile to the provided path.
   --runtime-endpoint value, -r value         Endpoint of CRI container runtime service (default: uses in order the first successful one of [unix:///run/containerd/containerd.sock unix:///run/crio/crio.sock unix:///var/run/cri-dockerd.sock]). Default is now deprecated and the endpoint should be set instead. [$CONTAINER_RUNTIME_ENDPOINT]
   --timeout value, -t value                  Timeout of connecting to the server in seconds (e.g. 2s, 20s.). 0 or less is set to default (default: 2s)
   --tracing-endpoint value                   Address to which the gRPC tracing collector will send spans to. (default: "127.0.0.1:4317")
   --tracing-sampling-rate-per-million value  Number of samples to collect per million OpenTelemetry spans. Set to 1000000 or -1 to always sample. (default: -1)
   --help, -h                                 show help
```

### `critest`

> 官方示例调用：`critest -h`

```text
root@kali:~# critest -h
WARN[0000] Config "/etc/crictl.yaml" does not exist, trying next: "/home/kali/kali-www/bin/kali-tools/tool-output/crictl.yaml"
Controlling Test Order
  --ginkgo.seed [int] (default: randomly generated by Ginkgo)
    The seed used to randomize the spec suite.
  --ginkgo.randomize-all
    If set, ginkgo will randomize all specs together.  By default, ginkgo only
    randomizes the top level Describe, Context and When containers.
Controlling Test Parallelism
These are set by the Ginkgo CLI, do not set them manually via go test.
Use ginkgo -p or ginkgo -procs=N instead.
  --ginkgo.parallel.process [int] (default: 1)
    This worker process's (one-indexed) process number.  For running specs in
    parallel.
  --ginkgo.parallel.total [int] (default: 1)
    The total number of worker processes.  For running specs in parallel.
  --ginkgo.parallel.host [string] (default: set by Ginkgo CLI)
    The address for the server that will synchronize the processes.
Filtering Tests
  --ginkgo.label-filter [expression]
    If set, ginkgo will only run specs with labels that match the label-filter.
    The passed-in expression can include boolean operations (!, &&, ||, ','),
    groupings via '()', and regular expressions '/regexp/'.  e.g. '(cat || dog)
    && !fruit'
  --ginkgo.sem-ver-filter [version]
    If set, ginkgo will only run specs with semantic version constraints that
    are satisfied by the provided version. e.g. '2.1.0'
  --ginkgo.focus [string]
    If set, ginkgo will only run specs that match this regular expression. Can
    be specified multiple times, values are ORed.
  --ginkgo.skip [string]
    If set, ginkgo will only run specs that do not match this regular
    expression. Can be specified multiple times, values are ORed.
  --ginkgo.focus-file [file (regexp) | file:line | file:lineA-lineB | file:line,line,line]
    If set, ginkgo will only run specs in matching files. Can be specified
    multiple times, values are ORed.
  --ginkgo.skip-file [file (regexp) | file:line | file:lineA-lineB | file:line,line,line]
    If set, ginkgo will skip specs in matching files. Can be specified multiple
    times, values are ORed.
Failure Handling
  --ginkgo.fail-on-pending
    If set, ginkgo will mark the test suite as failed if any specs are pending.
  --ginkgo.fail-fast
    If set, ginkgo will stop running a test suite after a failure occurs.
  --ginkgo.flake-attempts [int] (default: 0 - failed tests are not retried)
    Make up to this many attempts to run each spec. If any of the attempts
    succeed, the suite will not be failed.
  --ginkgo.fail-on-empty
    If set, ginkgo will mark the test suite as failed if no specs are run.
Controlling Output Formatting
  --ginkgo.no-color
    If set, suppress color output in default reporter.  You can also set the
    environment variable GINKGO_NO_COLOR=TRUE
  --ginkgo.v
    If set, emits more output including GinkgoWriter contents.
  --ginkgo.vv
    If set, emits with maximal verbosity - includes skipped and pending tests.
  --ginkgo.succinct
    If set, default reporter prints out a very succinct report
  --ginkgo.trace
    If set, default reporter prints out the full stack trace when a failure
    occurs
  --ginkgo.show-node-events
    If set, default reporter prints node > Enter and < Exit events when specs
    fail
  --ginkgo.github-output
    If set, default reporter prints easier to manage output in Github Actions.
  --ginkgo.silence-skips
    If set, default reporter will not print out skipped tests.
  --ginkgo.force-newlines
    If set, default reporter will ensure a newline appears after each test.
  --ginkgo.json-report [filename.json]
    If set, Ginkgo will generate a JSON-formatted test report at the specified
    location.
  --ginkgo.gojson-report [filename.json]
    If set, Ginkgo will generate a Go JSON-formatted test report at the
    specified location.
  --ginkgo.junit-report [filename.xml]
    If set, Ginkgo will generate a conformant junit test report in the specified
    file.
  --ginkgo.teamcity-report [filename]
    If set, Ginkgo will generate a Teamcity-formatted test report at the
    specified location.
Debugging Tests
In addition to these flags, Ginkgo supports a few debugging environment
variables.  To change the parallel server protocol set GINKGO_PARALLEL_PROTOCOL
to HTTP.  To avoid pruning callstacks set GINKGO_PRUNE_STACK to FALSE.
  --ginkgo.dry-run
    If set, ginkgo will walk the test hierarchy without actually running
    anything.  Best paired with -v.
  --ginkgo.poll-progress-after [duration] (default: 0)
    Emit node progress reports periodically if node hasn't completed after this
    duration.
  --ginkgo.poll-progress-interval [duration] (default: 10s)
    The rate at which to emit node progress reports after poll-progress-after
    has elapsed.
  --ginkgo.source-root [string]
    The location to look for source code when generating progress reports.  You
    can pass multiple --source-root flags.
  --ginkgo.timeout [duration] (default: 1h)
    Test suite fails if it does not complete within the specified timeout.
  --ginkgo.grace-period [duration] (default: 30s)
    When interrupted, Ginkgo will wait for GracePeriod for the current running
    node to exit before moving on to the next one.
  --ginkgo.output-interceptor-mode [dup, swap, or none]
    If set, ginkgo will use the specified output interception strategy when
    running in parallel.  Defaults to dup on unix and swap on windows.
Go test flags
  -benchmark
    	Run benchmarks instead of validation tests
  -benchmarking-output-dir string
    	Optional path to a directory in which benchmarking data should be placed.
  -benchmarking-params-file string
    	Optional path to a YAML file specifying benchmarking configuration options.
  -config string
    	Location of the client config file. If not specified and the default does not exist, the program's directory is searched as well
  -image-endpoint string
    	Image service socket for client to connect.
  -image-service-timeout duration
    	Timeout when trying to connect to image service.
  -parallel int
    	The number of parallel test nodes to run (default 1)
  -registry-prefix string
    	A possible registry prefix added to all images, like 'localhost:5000'
  -report-dir string
    	Path to the directory where the JUnit XML reports should be saved. Default is empty, which doesn't generate these reports.
  -report-prefix string
    	Optional prefix for JUnit XML reports. Default is empty, which doesn't prepend anything to the default name.
  -runtime-endpoint string
    	Runtime service socket for client to connect.
  -runtime-handler string
    	Runtime handler to use in the test.
  -runtime-service-timeout duration
    	Timeout when trying to connect to a runtime service.
  -test-images-file string
    	Optional path to a YAML file containing references to custom container images to be used in tests.
  -test.artifacts
    	store test artifacts in test.,outputdir
  -test.bench regexp
    	run only benchmarks matching regexp
  -test.benchmem
    	print memory allocations for benchmarks
  -test.benchtime d
    	run each benchmark for duration d or N times if `d` is of the form Nx
  -test.blockprofile file
    	write a goroutine blocking profile to file
  -test.blockprofilerate rate
    	set blocking profile rate (see runtime.SetBlockProfileRate)
  -test.count n
    	run tests and benchmarks n times
  -test.coverprofile file
    	write a coverage profile to file
  -test.cpu list
    	comma-separated list of cpu counts to run each test with
  -test.cpuprofile file
    	write a cpu profile to file
  -test.failfast
    	do not start new tests after the first test failure
  -test.fullpath
    	show full file names in error messages
  -test.fuzz regexp
    	run the fuzz test matching regexp
  -test.fuzzcachedir string
    	directory where interesting fuzzing inputs are stored (for use only by cmd/go)
  -test.fuzzminimizetime value
    	time to spend minimizing a value after finding a failing input
  -test.fuzztime value
    	time to spend fuzzing; default is to run indefinitely
  -test.fuzzworker
    	coordinate with the parent process to fuzz random values (for use only by cmd/go)
  -test.gocoverdir string
    	write coverage intermediate files to this directory
  -test.list regexp
    	list tests, examples, and benchmarks matching regexp then exit
  -test.memprofile file
    	write an allocation profile to file
  -test.memprofilerate rate
    	set memory allocation profiling rate (see runtime.MemProfileRate)
  -test.mutexprofile string
    	write a mutex contention profile to the named file after execution
  -test.mutexprofilefraction int
    	if >= 0, calls runtime.SetMutexProfileFraction()
  -test.outputdir dir
    	write profiles to dir
  -test.paniconexit0
    	panic on call to os.Exit(0)
  -test.parallel n
    	run at most n tests in parallel
  -test.run regexp
    	run only tests and examples matching regexp
  -test.short
    	run smaller test suite to save time
  -test.shuffle string
    	randomize the execution order of tests and benchmarks
  -test.skip regexp
    	do not list or run tests matching regexp
  -test.testlogfile file
    	write test action log to file (for use only by cmd/go)
  -test.timeout d
    	panic test binary after duration d (default 0, timeout disabled)
  -test.trace file
    	write an execution trace to file
  -test.v
    	verbose: print additional output
  -version
    	Display version of critest
  -websocket-attach
    	Use websocket connections over SPDY for attach streaming tests.
  -websocket-exec
    	Use websocket connections over SPDY for exec streaming tests.
  -websocket-portforward
    	Use websocket connections over SPDY for portforward streaming tests.
Updated on: 2026-Aug-25
 Edit this page
crackmapexec
cryptsetup
LIGHT
DARK
Links
Home
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install cri-tools`，再执行 `cri-tools --version` 2>/dev/null || `cri-tools -V`
- [ ] **2.** **读官方帮助** —— `cri-tools -h`，需要细节时 `man cri-tools`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `cri-tools -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cri-tools/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cri-tools/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cri-tools/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
