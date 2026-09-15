# qemu

> Extra block backend modules for qemu-system and qemu-utils QEMU is a fast processor emulator: currently the package supports Alpha, ARM, CRIS, i386, LoongArch, M68k (ColdFire), MicroBlaze, MIPS, PowerPC, RISC-V, S390x, SH4, SPARC, x86-64, …

> **功能分类**：硬件攻击 ｜ **Kali 包**：`qemu` ｜ **官方文档**：<https://www.kali.org/tools/qemu/>

## 1. 安装

```bash
sudo apt update
sudo apt install qemu-block-extra
```

| 项目 | 内容 |
|------|------|
| 版本 | 11.1.0 |
| 架构 | linux-any |
| 可执行命令 | `qemu-block-extra`、`qemu-guest-agent`、`qemu-ga`、`qemu-system`、`qemu-system-arm`、`qemu-system-aarch64`、`qemu-system-arm64`、`qemu-system-armel`、`qemu-system-armhf`、`qemu-system-common`、`qemu-pr-helper`、`qemu-vmsr-helper`、`qemu-system-data`、`qemu-system-gui`、`qemu-system-mips`、`qemu-system-mips64`、`qemu-system-mips64el`、`qemu-system-mipsel`、`qemu-system-misc`、`qemu-system-alpha`、`qemu-system-avr`、`qemu-system-hexagon`、`qemu-system-hppa`、`qemu-system-loong64`、`qemu-system-loongarch64`、`qemu-system-m68k`、`qemu-system-microblaze`、`qemu-system-or1k`、`qemu-system-rx`、`qemu-system-sh4`、`qemu-system-sh4eb`、`qemu-system-tricore`、`qemu-system-xtensa`、`qemu-system-xtensaeb`、`qemu-system-modules-opengl`、`qemu-system-modules-spice`、`qemu-system-ppc`、`qemu-system-powerpc`、`qemu-system-ppc64`、`qemu-system-ppc64el`、`qemu-system-ppc64le`、`qemu-system-riscv`、`qemu-system-riscv32`、`qemu-system-riscv64`、`qemu-system-s390x`、`qemu-system-sparc`、`qemu-system-sparc64`、`qemu-system-x86`、`kvm`、`qemu-system-amd64`、`qemu-system-i386`、`qemu-system-x86_64`、`qemu-system-x86_64-microvm`、`qemu-system-xen`、`qemu-user`、`qemu-aarch64`、`qemu-aarch64_be`、`qemu-alpha`、`qemu-amd64`、`qemu-arm`、`qemu-arm64`、`qemu-armeb`、`qemu-armel`、`qemu-armhf`、`qemu-hexagon`、`qemu-hppa`、`qemu-i386`、`qemu-loong64`、`qemu-loongarch64`、`qemu-m68k`、`qemu-microblaze`、`qemu-microblazeel`、`qemu-mips`、`qemu-mips64`、`qemu-mips64el`、`qemu-mipsel`、`qemu-mipsn32`、`qemu-mipsn32el`、`qemu-or1k`、`qemu-powerpc`、`qemu-ppc`、`qemu-ppc64`、`qemu-ppc64el`、`qemu-ppc64le`、`qemu-riscv32`、`qemu-riscv64`、`qemu-s390x`、`qemu-sh4`、`qemu-sh4eb`、`qemu-sparc`、`qemu-sparc32plus`、`qemu-sparc64`、`qemu-x86_64`、`qemu-xtensa`、`qemu-xtensaeb`、`qemu-user-binfmt`、`qemu-utils`、`qemu-img`、`qemu-io`、`qemu-nbd`、`qemu-storage-daemon` |
| 依赖 | `libblkio1`、`libbz2-1.0`、`libc6`、`libcurl4-gnutls`、`libiscsi7`、`libnfs14`、`librados2`、`librbd1`、`libssh-4` |
| 安装体积 | 323 KB |
| 官网 | <http://www.qemu.org/> |
| 源码仓库 | <https://salsa.debian.org/qemu-team/qemu> |
| 包追踪 | <https://pkg.kali.org/pkg/qemu> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
qemu-block-extra -h          # 查看用法
man qemu-block-extra         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 101 个可执行命令，下面是官方页面内嵌的帮助原文。

### `qemu-ga`

> 官方示例调用：`qemu-ga -h`

```text
root@kali:~# qemu-ga -h
Usage: qemu-ga [-m <method> -p <path>] [<options>]
QEMU Guest Agent 11.1.0 (Debian 1:11.1.0+ds-2)
Copyright (c) 2003-2026 Fabrice Bellard and the QEMU Project developers
  -c, --config=PATH configuration file path (default is
                    /etc/qemu/qemu-ga.conf/qemu-ga.conf
                    unless overridden by the QGA_CONF environment variable)
  -m, --method      transport method: one of unix-listen, virtio-serial,
                    isa-serial, or vsock-listen (virtio-serial is the default)
  -p, --path        device/socket path (the default for virtio-serial is:
                    /dev/virtio-ports/org.qemu.guest_agent.0,
                    the default for isa-serial is:
                    /dev/ttyS0).
                    Socket addresses for vsock-listen are written as
                    <cid>:<port>.
  -l, --logfile     set logfile path, logs to stderr by default
  -f, --pidfile     specify pidfile (default is /var/run/qemu-ga.pid)
  -F, --fsfreeze-hook
                    enable fsfreeze hook. Accepts an optional argument that
                    specifies script to run on freeze/thaw. Script will be
                    called with 'freeze'/'thaw' arguments accordingly.
                    (default is /etc/qemu/fsfreeze-hook)
                    If using -F with an argument, do not follow -F with a
                    space.
                    (for example: -F/var/run/fsfreezehook.sh)
  -t, --statedir    specify dir to store state information (absolute paths
                    only, default is /var/run)
  -v, --verbose     log extra debugging information
  -V, --version     print version information and exit
  -d, --daemonize   become a daemon
  -b, --block-rpcs  comma-separated list of RPCs to disable (no spaces,
                    use "--block-rpcs=help" to list available RPCs)
  -a, --allow-rpcs  comma-separated list of RPCs to enable (no spaces,
                    use "--allow-rpcs=help" to list available RPCs)
  -D, --dump-conf   dump a qemu-ga config file based on current config
                    options / command-line parameters to stdout
  -r, --retry-path  attempt re-opening path if it's unavailable or closed
                    due to an error which may be recoverable in the future
                    (virtio-serial driver re-install, serial device hot
                    plug/unplug, etc.)
  -h, --help        display this help and exit
See <https://qemu.org/contribute/report-a-bug> for how to report bugs.
More information on the QEMU project at <https://qemu.org>.
```

### `qemu-system-aarch64`

> 官方示例调用：`qemu-system-aarch64 -h`

```text
root@kali:~# qemu-system-aarch64 -h
QEMU emulator version 11.1.0 (Debian 1:11.1.0+ds-2)
Copyright (c) 2003-2026 Fabrice Bellard and the QEMU Project developers
usage: qemu-system-aarch64 [options] [disk_image]
'disk_image' is a raw hard disk image for IDE hard disk 0
Standard options:
-h or -help     display this help and exit
-version        display version information and exit
-machine [type=]name[,prop=value[,...]]
                selects emulated machine ('-machine help' for list)
                property accel=accel1[:accel2[:...]] selects accelerator
                supported accelerators are kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg (default: tcg)
                vmport=on|off|auto controls emulation of vmport (default: auto)
                dump-guest-core=on|off include guest memory in a core dump (default=on)
                mem-merge=on|off controls memory merge support (default: on)
                aes-key-wrap=on|off controls support for AES key wrapping (default=on)
                dea-key-wrap=on|off controls support for DEA key wrapping (default=on)
                suppress-vmdesc=on|off disables self-describing migration (default=off)
                nvdimm=on|off controls NVDIMM support (default=off)
                confidential-guest-support=<id> specifies confidential guest support object (default=none)
                memory-encryption=<id> (memory-encryption is the alias of confidential-guest-support, recommend to use confidential-guest-support)
                hmat=on|off controls ACPI HMAT support (default=off)
                spcr=on|off controls ACPI SPCR support (default=on)
                aux-ram-share=on|off allocate auxiliary guest RAM as shared (default: off)
                memory-backend='backend-id' specifies explicitly provided backend for main RAM (default=none)
                cxl-fmw.0.targets.0=firsttarget,cxl-fmw.0.targets.1=secondtarget,cxl-fmw.0.size=size[,cxl-fmw.0.interleave-granularity=granularity]
                sgx-epc.0.memdev=memid,sgx-epc.0.node=numaid
                smp-cache.0.cache=cachename,smp-cache.0.topology=topologylevel
-M              as -machine
-cpu cpu        select CPU ('-cpu help' for list)
-accel [accel=]accelerator[,prop=value[,...]]
                select accelerator (kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg; use 'help' for a list)
                igd-passthru=on|off (enable Xen integrated Intel graphics passthrough, default=off)
                kernel-irqchip=on|off|split controls accelerated irqchip support (default=on)
                kvm-shadow-mem=size of KVM shadow MMU in bytes
                one-insn-per-tb=on|off (one guest instruction per TCG translation block)
                split-wx=on|off (enable TCG split w^x mapping)
                tb-size=n (TCG translation block cache size)
                dirty-ring-size=n (KVM dirty ring GFN count, default 0)
                eager-split-size=n (KVM Eager Page Split chunk size, default 0, disabled. ARM only)
                notify-vmexit=run|internal-error|disable,notify-window=n (enable notify VM exit and set notify window, x86 only)
                thread=single|multi (enable multi-threaded TCG)
                device=path (KVM device path, default /dev/kvm)
-smp [[cpus=]n][,maxcpus=maxcpus][,drawers=drawers][,books=books][,sockets=sockets]
               [,dies=dies][,clusters=clusters][,modules=modules][,cores=cores]
               [,threads=threads]
                set the number of initial CPUs to 'n' [default=1]
                maxcpus= maximum number of total CPUs, including
                offline CPUs for hotplug, etc
                drawers= number of drawers on the machine board
                books= number of books in one drawer
                sockets= number of sockets in one book
                dies= number of dies in one socket
                clusters= number of clusters in one die
                modules= number of modules in one cluster
                cores= number of cores in one module
                threads= number of threads in one core
Note: Different machines may have different subsets of the CPU topology
      parameters supported, so the actual meaning of the supported parameters
      will vary accordingly. For example, for a machine type that supports a
      three-level CPU hierarchy of sockets/cores/threads, the parameters will
      sequentially mean as below:
                sockets means the number of sockets on the machine board
                cores means the number of cores in one socket
                threads means the number of threads in one core
      For a particular machine type board, an expected CPU topology hierarchy
      can be defined through the supported sub-option. Unsupported parameters
      can also be provided in addition to the sub-option, but their values
      must be set as 1 in the purpose of correct parsing.
-numa node[,mem=size][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa node[,memdev=id][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa dist,src=source,dst=destination,val=distance
-numa cpu,node-id=node[,socket-id=x][,core-id=y][,thread-id=z]
-numa hmat-lb,initiator=node,target=node,hierarchy=memory|first-level|second-level|third-level,data-type=access-latency|read-latency|write-latency[,latency=lat][,bandwidth=bw]
-numa hmat-cache,node-id=node,size=size,level=level[,associativity=none|direct|complex][,policy=none|write-back|write-through][,line=size]
-add-fd fd=fd,set=set[,opaque=opaque]
                Add 'fd' to fd 'set'
-set group.id.arg=value
                set <arg> parameter for item <id> of type <group>
                i.e. -set drive.$id.file=/path/to/image
-global driver.property=value
-global driver=driver,property=property,value=value
                set a global default for a driver property
-boot [order=drives][,once=drives][,menu=on|off]
      [,splash=sp_name][,splash-time=sp_time][,reboot-timeout=rb_time][,strict=on|off]
                'drives': floppy (a), hard disk (c), CD-ROM (d), network (n)
                'sp_name': the file's name that would be passed to bios as logo picture, if menu=on
                'sp_time': the period that splash picture last if menu=on, unit is ms
                'rb_timeout': the timeout before guest reboot when boot failed, unit is ms
-m [size=]megs[,slots=n,maxmem=size]
                configure guest RAM
                size: initial amount of guest memory
                slots: number of hotplug slots (default: none)
                maxmem: maximum amount of guest memory (default: none)
                Note: Some architectures might enforce a specific granularity
-mem-path FILE  provide backing storage for guest RAM
-mem-prealloc   preallocate guest memory (use with -mem-path)
-k language     use keyboard layout (for example 'fr' for French)
-audio [driver=]driver[,prop=value[,...]]
                specifies default audio backend when `audiodev` is not
                used to create a machine or sound device;                options are the same as for -audiodev
-audio [driver=]driver,model=value[,prop=value[,...]]
                specifies the audio backend and device to use;
                apart from 'model', options are the same as for -audiodev.
                use '-audio model=help' to show possible devices.
-audiodev [driver=]driver,id=id[,prop=value[,...]]
                specifies the audio backend to use
                Use ``-audiodev help`` to list the available drivers
                id= identifier of the backend
                timer-period= timer period in microseconds
                in|out.mixing-engine= use mixing engine to mix streams inside QEMU
                in|out.fixed-settings= use fixed settings for host audio
                in|out.frequency= frequency to use with fixed settings
                in|out.channels= number of channels to use with fixed settings
                in|out.format= sample format to use with fixed settings
                valid values: s8, s16, s32, u8, u16, u32, f32
                in|out.voices= number of voices to use
                in|out.buffer-length= length of buffer in microseconds
-audiodev none,id=id,[,prop=value[,...]]
                dummy driver that discards all output
-audiodev alsa,id=id[,prop=value[,...]]
                in|out.dev= name of the audio device to use
                in|out.period-length= length of period in microseconds
                in|out.try-poll= attempt to use poll mode
                threshold= threshold (in microseconds) when playback starts
-audiodev oss,id=id[,prop=value[,...]]
                in|out.dev= path of the audio device to use
                in|out.buffer-count= number of buffers
                in|out.try-poll= attempt to use poll mode
                try-mmap= try using memory mapped access
                exclusive= open device in exclusive mode
                dsp-policy= set timing policy (0..10), -1 to use fragment mode
-audiodev pa,id=id[,prop=value[,...]]
                server= PulseAudio server address
                in|out.name= source/sink device name
                in|out.latency= desired latency in microseconds
-audiodev pipewire,id=id[,prop=value[,...]]
                in|out.name= source/sink device name
                in|out.stream-name= name of pipewire stream
                in|out.latency= desired latency in microseconds
-audiodev sdl,id=id[,prop=value[,...]]
                in|out.buffer-count= number of buffers
-audiodev spice,id=id[,prop=value[,...]]
-audiodev dbus,id=id[,prop=value[,...]]
-audiodev wav,id=id[,prop=value[,...]]
                path= path of wav file to record
-device driver[,prop=value[,...]]
                add device (based on driver)
                prop=value,... sets driver properties
                use '-device help' to print all possible drivers
                use '-device driver,help' to print all possible properties
-name string1[,process=string2][,debug-threads=on|off]
                set the name of the guest
                string1 sets the window title and string2 the process name
                When debug-threads is enabled, individual threads are given a separate name
                NOTE: The thread names are for debugging and not a stable API.
-uuid %08x-%04x-%04x-%04x-%012x
                specify machine UUID
Block device options:
-fda/-fdb file  use 'file' as floppy disk 0/1 image
-hda/-hdb file  use 'file' as hard disk 0/1 image
-hdc/-hdd file  use 'file' as hard disk 2/3 image
-cdrom file     use 'file' as CD-ROM image
-blockdev [driver=]driver[,node-name=N][,discard=ignore|unmap]
          [,cache.direct=on|off][,cache.no-flush=on|off]
          [,read-only=on|off][,auto-read-only=on|off]
          [,force-share=on|off][,detect-zeroes=on|off|unmap]
          [,driver specific parameters...]
                configure a block backend
-drive [file=file][,if=type][,bus=n][,unit=m][,media=d][,index=i]
       [,cache=writethrough|writeback|none|directsync|unsafe][,format=f]
       [,snapshot=on|off][,rerror=ignore|stop|report]
       [,werror=ignore|stop|report|enospc][,id=name]
       [,aio=threads|native|io_uring]
       [,readonly=on|off][,copy-on-read=on|off]
       [,discard=ignore|unmap][,detect-zeroes=on|off|unmap]
       [[,bps=b]|[[,bps_rd=r][,bps_wr=w]]]
       [[,iops=i]|[[,iops_rd=r][,iops_wr=w]]]
       [[,bps_max=bm]|[[,bps_rd_max=rm][,bps_wr_max=wm]]]
       [[,iops_max=im]|[[,iops_rd_max=irm][,iops_wr_max=iwm]]]
       [[,iops_size=is]]
       [[,group=g]]
                use 'file' as a drive image
-mtdblock file  use 'file' as on-board Flash memory image
-sd file        use 'file' as SecureDigital card image
-snapshot       write to temporary files instead of disk image files
-fsdev local,id=id,path=path,security_model=mapped-xattr|mapped-file|passthrough|none
 [,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,max_xattr=max]
 [[,throttling.bps-total=b]|[[,throttling.bps-read=r][,throttling.bps-write=w]]]
 [[,throttling.iops-total=i]|[[,throttling.iops-read=r][,throttling.iops-write=w]]]
 [[,throttling.bps-total-max=bm]|[[,throttling.bps-read-max=rm][,throttling.bps-write-max=wm]]]
 [[,throttling.iops-total-max=im]|[[,throttling.iops-read-max=irm][,throttling.iops-write-max=iwm]]]
 [[,throttling.iops-size=is]]
-fsdev synth,id=id[,max_xattr=max]
-virtfs local,path=path,mount_tag=tag,security_model=mapped-xattr|mapped-file|passthrough|none
        [,id=id][,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,multidevs=remap|forbid|warn][,max_xattr=max]
-virtfs synth,mount_tag=tag[,id=id][,readonly=on][,max_xattr=max]
-iscsi [user=user][,password=password][,password-secret=secret-id]
       [,header-digest=CRC32C|CR32C-NONE|NONE-CRC32C|NONE]
       [,initiator-name=initiator-iqn][,id=target-iqn]
       [,timeout=timeout]
                iSCSI session parameters
USB convenience options:
-usb            enable on-board USB host controller (if not enabled by default)
-usbdevice name add the host or guest USB device 'name'
Display options:
-display spice-app[,gl=on|off]
-display sdl[,gl=on|core|es|off][,grab-mod=<mod>][,show-cursor=on|off]
            [,window-close=on|off]
-display gtk[,clipboard=on|off][,full-screen=on|off][,gl=on|off]
            [,grab-on-hover=on|off][,show-tabs=on|off][,show-cursor=on|off]
            [,window-close=on|off][,show-menubar=on|off][,zoom-to-fit=on|off]
-display vnc=<display>[,<optargs>]
-display curses[,charset=<encoding>]
-display egl-headless[,rendernode=<file>]
-display dbus[,addr=<dbusaddr>]
             [,gl=on|core|es|off][,rendernode=<file>]
-display none
                select display backend type
                The default display is equivalent to
```

### `qemu-system-arm`

> 官方示例调用：`qemu-system-arm -h`

```text
root@kali:~# qemu-system-arm -h
QEMU emulator version 11.1.0 (Debian 1:11.1.0+ds-2)
Copyright (c) 2003-2026 Fabrice Bellard and the QEMU Project developers
usage: qemu-system-arm [options] [disk_image]
'disk_image' is a raw hard disk image for IDE hard disk 0
Standard options:
-h or -help     display this help and exit
-version        display version information and exit
-machine [type=]name[,prop=value[,...]]
                selects emulated machine ('-machine help' for list)
                property accel=accel1[:accel2[:...]] selects accelerator
                supported accelerators are kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg (default: tcg)
                vmport=on|off|auto controls emulation of vmport (default: auto)
                dump-guest-core=on|off include guest memory in a core dump (default=on)
                mem-merge=on|off controls memory merge support (default: on)
                aes-key-wrap=on|off controls support for AES key wrapping (default=on)
                dea-key-wrap=on|off controls support for DEA key wrapping (default=on)
                suppress-vmdesc=on|off disables self-describing migration (default=off)
                nvdimm=on|off controls NVDIMM support (default=off)
                confidential-guest-support=<id> specifies confidential guest support object (default=none)
                memory-encryption=<id> (memory-encryption is the alias of confidential-guest-support, recommend to use confidential-guest-support)
                hmat=on|off controls ACPI HMAT support (default=off)
                spcr=on|off controls ACPI SPCR support (default=on)
                aux-ram-share=on|off allocate auxiliary guest RAM as shared (default: off)
                memory-backend='backend-id' specifies explicitly provided backend for main RAM (default=none)
                cxl-fmw.0.targets.0=firsttarget,cxl-fmw.0.targets.1=secondtarget,cxl-fmw.0.size=size[,cxl-fmw.0.interleave-granularity=granularity]
                sgx-epc.0.memdev=memid,sgx-epc.0.node=numaid
                smp-cache.0.cache=cachename,smp-cache.0.topology=topologylevel
-M              as -machine
-cpu cpu        select CPU ('-cpu help' for list)
-accel [accel=]accelerator[,prop=value[,...]]
                select accelerator (kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg; use 'help' for a list)
                igd-passthru=on|off (enable Xen integrated Intel graphics passthrough, default=off)
                kernel-irqchip=on|off|split controls accelerated irqchip support (default=on)
                kvm-shadow-mem=size of KVM shadow MMU in bytes
                one-insn-per-tb=on|off (one guest instruction per TCG translation block)
                split-wx=on|off (enable TCG split w^x mapping)
                tb-size=n (TCG translation block cache size)
                dirty-ring-size=n (KVM dirty ring GFN count, default 0)
                eager-split-size=n (KVM Eager Page Split chunk size, default 0, disabled. ARM only)
                notify-vmexit=run|internal-error|disable,notify-window=n (enable notify VM exit and set notify window, x86 only)
                thread=single|multi (enable multi-threaded TCG)
                device=path (KVM device path, default /dev/kvm)
-smp [[cpus=]n][,maxcpus=maxcpus][,drawers=drawers][,books=books][,sockets=sockets]
               [,dies=dies][,clusters=clusters][,modules=modules][,cores=cores]
               [,threads=threads]
                set the number of initial CPUs to 'n' [default=1]
                maxcpus= maximum number of total CPUs, including
                offline CPUs for hotplug, etc
                drawers= number of drawers on the machine board
                books= number of books in one drawer
                sockets= number of sockets in one book
                dies= number of dies in one socket
                clusters= number of clusters in one die
                modules= number of modules in one cluster
                cores= number of cores in one module
                threads= number of threads in one core
Note: Different machines may have different subsets of the CPU topology
      parameters supported, so the actual meaning of the supported parameters
      will vary accordingly. For example, for a machine type that supports a
      three-level CPU hierarchy of sockets/cores/threads, the parameters will
      sequentially mean as below:
                sockets means the number of sockets on the machine board
                cores means the number of cores in one socket
                threads means the number of threads in one core
      For a particular machine type board, an expected CPU topology hierarchy
      can be defined through the supported sub-option. Unsupported parameters
      can also be provided in addition to the sub-option, but their values
      must be set as 1 in the purpose of correct parsing.
-numa node[,mem=size][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa node[,memdev=id][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa dist,src=source,dst=destination,val=distance
-numa cpu,node-id=node[,socket-id=x][,core-id=y][,thread-id=z]
-numa hmat-lb,initiator=node,target=node,hierarchy=memory|first-level|second-level|third-level,data-type=access-latency|read-latency|write-latency[,latency=lat][,bandwidth=bw]
-numa hmat-cache,node-id=node,size=size,level=level[,associativity=none|direct|complex][,policy=none|write-back|write-through][,line=size]
-add-fd fd=fd,set=set[,opaque=opaque]
                Add 'fd' to fd 'set'
-set group.id.arg=value
                set <arg> parameter for item <id> of type <group>
                i.e. -set drive.$id.file=/path/to/image
-global driver.property=value
-global driver=driver,property=property,value=value
                set a global default for a driver property
-boot [order=drives][,once=drives][,menu=on|off]
      [,splash=sp_name][,splash-time=sp_time][,reboot-timeout=rb_time][,strict=on|off]
                'drives': floppy (a), hard disk (c), CD-ROM (d), network (n)
                'sp_name': the file's name that would be passed to bios as logo picture, if menu=on
                'sp_time': the period that splash picture last if menu=on, unit is ms
                'rb_timeout': the timeout before guest reboot when boot failed, unit is ms
-m [size=]megs[,slots=n,maxmem=size]
                configure guest RAM
                size: initial amount of guest memory
                slots: number of hotplug slots (default: none)
                maxmem: maximum amount of guest memory (default: none)
                Note: Some architectures might enforce a specific granularity
-mem-path FILE  provide backing storage for guest RAM
-mem-prealloc   preallocate guest memory (use with -mem-path)
-k language     use keyboard layout (for example 'fr' for French)
-audio [driver=]driver[,prop=value[,...]]
                specifies default audio backend when `audiodev` is not
                used to create a machine or sound device;                options are the same as for -audiodev
-audio [driver=]driver,model=value[,prop=value[,...]]
                specifies the audio backend and device to use;
                apart from 'model', options are the same as for -audiodev.
                use '-audio model=help' to show possible devices.
-audiodev [driver=]driver,id=id[,prop=value[,...]]
                specifies the audio backend to use
                Use ``-audiodev help`` to list the available drivers
                id= identifier of the backend
                timer-period= timer period in microseconds
                in|out.mixing-engine= use mixing engine to mix streams inside QEMU
                in|out.fixed-settings= use fixed settings for host audio
                in|out.frequency= frequency to use with fixed settings
                in|out.channels= number of channels to use with fixed settings
                in|out.format= sample format to use with fixed settings
                valid values: s8, s16, s32, u8, u16, u32, f32
                in|out.voices= number of voices to use
                in|out.buffer-length= length of buffer in microseconds
-audiodev none,id=id,[,prop=value[,...]]
                dummy driver that discards all output
-audiodev alsa,id=id[,prop=value[,...]]
                in|out.dev= name of the audio device to use
                in|out.period-length= length of period in microseconds
                in|out.try-poll= attempt to use poll mode
                threshold= threshold (in microseconds) when playback starts
-audiodev oss,id=id[,prop=value[,...]]
                in|out.dev= path of the audio device to use
                in|out.buffer-count= number of buffers
                in|out.try-poll= attempt to use poll mode
                try-mmap= try using memory mapped access
                exclusive= open device in exclusive mode
                dsp-policy= set timing policy (0..10), -1 to use fragment mode
-audiodev pa,id=id[,prop=value[,...]]
                server= PulseAudio server address
                in|out.name= source/sink device name
                in|out.latency= desired latency in microseconds
-audiodev pipewire,id=id[,prop=value[,...]]
                in|out.name= source/sink device name
                in|out.stream-name= name of pipewire stream
                in|out.latency= desired latency in microseconds
-audiodev sdl,id=id[,prop=value[,...]]
                in|out.buffer-count= number of buffers
-audiodev spice,id=id[,prop=value[,...]]
-audiodev dbus,id=id[,prop=value[,...]]
-audiodev wav,id=id[,prop=value[,...]]
                path= path of wav file to record
-device driver[,prop=value[,...]]
                add device (based on driver)
                prop=value,... sets driver properties
                use '-device help' to print all possible drivers
                use '-device driver,help' to print all possible properties
-name string1[,process=string2][,debug-threads=on|off]
                set the name of the guest
                string1 sets the window title and string2 the process name
                When debug-threads is enabled, individual threads are given a separate name
                NOTE: The thread names are for debugging and not a stable API.
-uuid %08x-%04x-%04x-%04x-%012x
                specify machine UUID
Block device options:
-fda/-fdb file  use 'file' as floppy disk 0/1 image
-hda/-hdb file  use 'file' as hard disk 0/1 image
-hdc/-hdd file  use 'file' as hard disk 2/3 image
-cdrom file     use 'file' as CD-ROM image
-blockdev [driver=]driver[,node-name=N][,discard=ignore|unmap]
          [,cache.direct=on|off][,cache.no-flush=on|off]
          [,read-only=on|off][,auto-read-only=on|off]
          [,force-share=on|off][,detect-zeroes=on|off|unmap]
          [,driver specific parameters...]
                configure a block backend
-drive [file=file][,if=type][,bus=n][,unit=m][,media=d][,index=i]
       [,cache=writethrough|writeback|none|directsync|unsafe][,format=f]
       [,snapshot=on|off][,rerror=ignore|stop|report]
       [,werror=ignore|stop|report|enospc][,id=name]
       [,aio=threads|native|io_uring]
       [,readonly=on|off][,copy-on-read=on|off]
       [,discard=ignore|unmap][,detect-zeroes=on|off|unmap]
       [[,bps=b]|[[,bps_rd=r][,bps_wr=w]]]
       [[,iops=i]|[[,iops_rd=r][,iops_wr=w]]]
       [[,bps_max=bm]|[[,bps_rd_max=rm][,bps_wr_max=wm]]]
       [[,iops_max=im]|[[,iops_rd_max=irm][,iops_wr_max=iwm]]]
       [[,iops_size=is]]
       [[,group=g]]
                use 'file' as a drive image
-mtdblock file  use 'file' as on-board Flash memory image
-sd file        use 'file' as SecureDigital card image
-snapshot       write to temporary files instead of disk image files
-fsdev local,id=id,path=path,security_model=mapped-xattr|mapped-file|passthrough|none
 [,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,max_xattr=max]
 [[,throttling.bps-total=b]|[[,throttling.bps-read=r][,throttling.bps-write=w]]]
 [[,throttling.iops-total=i]|[[,throttling.iops-read=r][,throttling.iops-write=w]]]
 [[,throttling.bps-total-max=bm]|[[,throttling.bps-read-max=rm][,throttling.bps-write-max=wm]]]
 [[,throttling.iops-total-max=im]|[[,throttling.iops-read-max=irm][,throttling.iops-write-max=iwm]]]
 [[,throttling.iops-size=is]]
-fsdev synth,id=id[,max_xattr=max]
-virtfs local,path=path,mount_tag=tag,security_model=mapped-xattr|mapped-file|passthrough|none
        [,id=id][,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,multidevs=remap|forbid|warn][,max_xattr=max]
-virtfs synth,mount_tag=tag[,id=id][,readonly=on][,max_xattr=max]
-iscsi [user=user][,password=password][,password-secret=secret-id]
       [,header-digest=CRC32C|CR32C-NONE|NONE-CRC32C|NONE]
       [,initiator-name=initiator-iqn][,id=target-iqn]
       [,timeout=timeout]
                iSCSI session parameters
USB convenience options:
-usb            enable on-board USB host controller (if not enabled by default)
-usbdevice name add the host or guest USB device 'name'
Display options:
-display spice-app[,gl=on|off]
-display sdl[,gl=on|core|es|off][,grab-mod=<mod>][,show-cursor=on|off]
            [,window-close=on|off]
-display gtk[,clipboard=on|off][,full-screen=on|off][,gl=on|off]
            [,grab-on-hover=on|off][,show-tabs=on|off][,show-cursor=on|off]
            [,window-close=on|off][,show-menubar=on|off][,zoom-to-fit=on|off]
-display vnc=<display>[,<optargs>]
-display curses[,charset=<encoding>]
-display egl-headless[,rendernode=<file>]
-display dbus[,addr=<dbusaddr>]
             [,gl=on|core|es|off][,rendernode=<file>]
-display none
                select display backend type
                The default display is equivalent to
```

### `qemu-system-arm64`

> 官方示例调用：`qemu-system-arm64 -h`

```text
root@kali:~# qemu-system-arm64 -h
QEMU emulator version 11.1.0 (Debian 1:11.1.0+ds-2)
Copyright (c) 2003-2026 Fabrice Bellard and the QEMU Project developers
usage: qemu-system-arm64 [options] [disk_image]
'disk_image' is a raw hard disk image for IDE hard disk 0
Standard options:
-h or -help     display this help and exit
-version        display version information and exit
-machine [type=]name[,prop=value[,...]]
                selects emulated machine ('-machine help' for list)
                property accel=accel1[:accel2[:...]] selects accelerator
                supported accelerators are kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg (default: tcg)
                vmport=on|off|auto controls emulation of vmport (default: auto)
                dump-guest-core=on|off include guest memory in a core dump (default=on)
                mem-merge=on|off controls memory merge support (default: on)
                aes-key-wrap=on|off controls support for AES key wrapping (default=on)
                dea-key-wrap=on|off controls support for DEA key wrapping (default=on)
                suppress-vmdesc=on|off disables self-describing migration (default=off)
                nvdimm=on|off controls NVDIMM support (default=off)
                confidential-guest-support=<id> specifies confidential guest support object (default=none)
                memory-encryption=<id> (memory-encryption is the alias of confidential-guest-support, recommend to use confidential-guest-support)
                hmat=on|off controls ACPI HMAT support (default=off)
                spcr=on|off controls ACPI SPCR support (default=on)
                aux-ram-share=on|off allocate auxiliary guest RAM as shared (default: off)
                memory-backend='backend-id' specifies explicitly provided backend for main RAM (default=none)
                cxl-fmw.0.targets.0=firsttarget,cxl-fmw.0.targets.1=secondtarget,cxl-fmw.0.size=size[,cxl-fmw.0.interleave-granularity=granularity]
                sgx-epc.0.memdev=memid,sgx-epc.0.node=numaid
                smp-cache.0.cache=cachename,smp-cache.0.topology=topologylevel
-M              as -machine
-cpu cpu        select CPU ('-cpu help' for list)
-accel [accel=]accelerator[,prop=value[,...]]
                select accelerator (kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg; use 'help' for a list)
                igd-passthru=on|off (enable Xen integrated Intel graphics passthrough, default=off)
                kernel-irqchip=on|off|split controls accelerated irqchip support (default=on)
                kvm-shadow-mem=size of KVM shadow MMU in bytes
                one-insn-per-tb=on|off (one guest instruction per TCG translation block)
                split-wx=on|off (enable TCG split w^x mapping)
                tb-size=n (TCG translation block cache size)
                dirty-ring-size=n (KVM dirty ring GFN count, default 0)
                eager-split-size=n (KVM Eager Page Split chunk size, default 0, disabled. ARM only)
                notify-vmexit=run|internal-error|disable,notify-window=n (enable notify VM exit and set notify window, x86 only)
                thread=single|multi (enable multi-threaded TCG)
                device=path (KVM device path, default /dev/kvm)
-smp [[cpus=]n][,maxcpus=maxcpus][,drawers=drawers][,books=books][,sockets=sockets]
               [,dies=dies][,clusters=clusters][,modules=modules][,cores=cores]
               [,threads=threads]
                set the number of initial CPUs to 'n' [default=1]
                maxcpus= maximum number of total CPUs, including
                offline CPUs for hotplug, etc
                drawers= number of drawers on the machine board
                books= number of books in one drawer
                sockets= number of sockets in one book
                dies= number of dies in one socket
                clusters= number of clusters in one die
                modules= number of modules in one cluster
                cores= number of cores in one module
                threads= number of threads in one core
Note: Different machines may have different subsets of the CPU topology
      parameters supported, so the actual meaning of the supported parameters
      will vary accordingly. For example, for a machine type that supports a
      three-level CPU hierarchy of sockets/cores/threads, the parameters will
      sequentially mean as below:
                sockets means the number of sockets on the machine board
                cores means the number of cores in one socket
                threads means the number of threads in one core
      For a particular machine type board, an expected CPU topology hierarchy
      can be defined through the supported sub-option. Unsupported parameters
      can also be provided in addition to the sub-option, but their values
      must be set as 1 in the purpose of correct parsing.
-numa node[,mem=size][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa node[,memdev=id][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa dist,src=source,dst=destination,val=distance
-numa cpu,node-id=node[,socket-id=x][,core-id=y][,thread-id=z]
-numa hmat-lb,initiator=node,target=node,hierarchy=memory|first-level|second-level|third-level,data-type=access-latency|read-latency|write-latency[,latency=lat][,bandwidth=bw]
-numa hmat-cache,node-id=node,size=size,level=level[,associativity=none|direct|complex][,policy=none|write-back|write-through][,line=size]
-add-fd fd=fd,set=set[,opaque=opaque]
                Add 'fd' to fd 'set'
-set group.id.arg=value
                set <arg> parameter for item <id> of type <group>
                i.e. -set drive.$id.file=/path/to/image
-global driver.property=value
-global driver=driver,property=property,value=value
                set a global default for a driver property
-boot [order=drives][,once=drives][,menu=on|off]
      [,splash=sp_name][,splash-time=sp_time][,reboot-timeout=rb_time][,strict=on|off]
                'drives': floppy (a), hard disk (c), CD-ROM (d), network (n)
                'sp_name': the file's name that would be passed to bios as logo picture, if menu=on
                'sp_time': the period that splash picture last if menu=on, unit is ms
                'rb_timeout': the timeout before guest reboot when boot failed, unit is ms
-m [size=]megs[,slots=n,maxmem=size]
                configure guest RAM
                size: initial amount of guest memory
                slots: number of hotplug slots (default: none)
                maxmem: maximum amount of guest memory (default: none)
                Note: Some architectures might enforce a specific granularity
-mem-path FILE  provide backing storage for guest RAM
-mem-prealloc   preallocate guest memory (use with -mem-path)
-k language     use keyboard layout (for example 'fr' for French)
-audio [driver=]driver[,prop=value[,...]]
                specifies default audio backend when `audiodev` is not
                used to create a machine or sound device;                options are the same as for -audiodev
-audio [driver=]driver,model=value[,prop=value[,...]]
                specifies the audio backend and device to use;
                apart from 'model', options are the same as for -audiodev.
                use '-audio model=help' to show possible devices.
-audiodev [driver=]driver,id=id[,prop=value[,...]]
                specifies the audio backend to use
                Use ``-audiodev help`` to list the available drivers
                id= identifier of the backend
                timer-period= timer period in microseconds
                in|out.mixing-engine= use mixing engine to mix streams inside QEMU
                in|out.fixed-settings= use fixed settings for host audio
                in|out.frequency= frequency to use with fixed settings
                in|out.channels= number of channels to use with fixed settings
                in|out.format= sample format to use with fixed settings
                valid values: s8, s16, s32, u8, u16, u32, f32
                in|out.voices= number of voices to use
                in|out.buffer-length= length of buffer in microseconds
-audiodev none,id=id,[,prop=value[,...]]
                dummy driver that discards all output
-audiodev alsa,id=id[,prop=value[,...]]
                in|out.dev= name of the audio device to use
                in|out.period-length= length of period in microseconds
                in|out.try-poll= attempt to use poll mode
                threshold= threshold (in microseconds) when playback starts
-audiodev oss,id=id[,prop=value[,...]]
                in|out.dev= path of the audio device to use
                in|out.buffer-count= number of buffers
                in|out.try-poll= attempt to use poll mode
                try-mmap= try using memory mapped access
                exclusive= open device in exclusive mode
                dsp-policy= set timing policy (0..10), -1 to use fragment mode
-audiodev pa,id=id[,prop=value[,...]]
                server= PulseAudio server address
                in|out.name= source/sink device name
                in|out.latency= desired latency in microseconds
-audiodev pipewire,id=id[,prop=value[,...]]
                in|out.name= source/sink device name
                in|out.stream-name= name of pipewire stream
                in|out.latency= desired latency in microseconds
-audiodev sdl,id=id[,prop=value[,...]]
                in|out.buffer-count= number of buffers
-audiodev spice,id=id[,prop=value[,...]]
-audiodev dbus,id=id[,prop=value[,...]]
-audiodev wav,id=id[,prop=value[,...]]
                path= path of wav file to record
-device driver[,prop=value[,...]]
                add device (based on driver)
                prop=value,... sets driver properties
                use '-device help' to print all possible drivers
                use '-device driver,help' to print all possible properties
-name string1[,process=string2][,debug-threads=on|off]
                set the name of the guest
                string1 sets the window title and string2 the process name
                When debug-threads is enabled, individual threads are given a separate name
                NOTE: The thread names are for debugging and not a stable API.
-uuid %08x-%04x-%04x-%04x-%012x
                specify machine UUID
Block device options:
-fda/-fdb file  use 'file' as floppy disk 0/1 image
-hda/-hdb file  use 'file' as hard disk 0/1 image
-hdc/-hdd file  use 'file' as hard disk 2/3 image
-cdrom file     use 'file' as CD-ROM image
-blockdev [driver=]driver[,node-name=N][,discard=ignore|unmap]
          [,cache.direct=on|off][,cache.no-flush=on|off]
          [,read-only=on|off][,auto-read-only=on|off]
          [,force-share=on|off][,detect-zeroes=on|off|unmap]
          [,driver specific parameters...]
                configure a block backend
-drive [file=file][,if=type][,bus=n][,unit=m][,media=d][,index=i]
       [,cache=writethrough|writeback|none|directsync|unsafe][,format=f]
       [,snapshot=on|off][,rerror=ignore|stop|report]
       [,werror=ignore|stop|report|enospc][,id=name]
       [,aio=threads|native|io_uring]
       [,readonly=on|off][,copy-on-read=on|off]
       [,discard=ignore|unmap][,detect-zeroes=on|off|unmap]
       [[,bps=b]|[[,bps_rd=r][,bps_wr=w]]]
       [[,iops=i]|[[,iops_rd=r][,iops_wr=w]]]
       [[,bps_max=bm]|[[,bps_rd_max=rm][,bps_wr_max=wm]]]
       [[,iops_max=im]|[[,iops_rd_max=irm][,iops_wr_max=iwm]]]
       [[,iops_size=is]]
       [[,group=g]]
                use 'file' as a drive image
-mtdblock file  use 'file' as on-board Flash memory image
-sd file        use 'file' as SecureDigital card image
-snapshot       write to temporary files instead of disk image files
-fsdev local,id=id,path=path,security_model=mapped-xattr|mapped-file|passthrough|none
 [,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,max_xattr=max]
 [[,throttling.bps-total=b]|[[,throttling.bps-read=r][,throttling.bps-write=w]]]
 [[,throttling.iops-total=i]|[[,throttling.iops-read=r][,throttling.iops-write=w]]]
 [[,throttling.bps-total-max=bm]|[[,throttling.bps-read-max=rm][,throttling.bps-write-max=wm]]]
 [[,throttling.iops-total-max=im]|[[,throttling.iops-read-max=irm][,throttling.iops-write-max=iwm]]]
 [[,throttling.iops-size=is]]
-fsdev synth,id=id[,max_xattr=max]
-virtfs local,path=path,mount_tag=tag,security_model=mapped-xattr|mapped-file|passthrough|none
        [,id=id][,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,multidevs=remap|forbid|warn][,max_xattr=max]
-virtfs synth,mount_tag=tag[,id=id][,readonly=on][,max_xattr=max]
-iscsi [user=user][,password=password][,password-secret=secret-id]
       [,header-digest=CRC32C|CR32C-NONE|NONE-CRC32C|NONE]
       [,initiator-name=initiator-iqn][,id=target-iqn]
       [,timeout=timeout]
                iSCSI session parameters
USB convenience options:
-usb            enable on-board USB host controller (if not enabled by default)
-usbdevice name add the host or guest USB device 'name'
Display options:
-display spice-app[,gl=on|off]
-display sdl[,gl=on|core|es|off][,grab-mod=<mod>][,show-cursor=on|off]
            [,window-close=on|off]
-display gtk[,clipboard=on|off][,full-screen=on|off][,gl=on|off]
            [,grab-on-hover=on|off][,show-tabs=on|off][,show-cursor=on|off]
            [,window-close=on|off][,show-menubar=on|off][,zoom-to-fit=on|off]
-display vnc=<display>[,<optargs>]
-display curses[,charset=<encoding>]
-display egl-headless[,rendernode=<file>]
-display dbus[,addr=<dbusaddr>]
             [,gl=on|core|es|off][,rendernode=<file>]
-display none
                select display backend type
                The default display is equivalent to
```

### `qemu-system-armel`

> 官方示例调用：`qemu-system-armel -h`

```text
root@kali:~# qemu-system-armel -h
QEMU emulator version 11.1.0 (Debian 1:11.1.0+ds-2)
Copyright (c) 2003-2026 Fabrice Bellard and the QEMU Project developers
usage: qemu-system-armel [options] [disk_image]
'disk_image' is a raw hard disk image for IDE hard disk 0
Standard options:
-h or -help     display this help and exit
-version        display version information and exit
-machine [type=]name[,prop=value[,...]]
                selects emulated machine ('-machine help' for list)
                property accel=accel1[:accel2[:...]] selects accelerator
                supported accelerators are kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg (default: tcg)
                vmport=on|off|auto controls emulation of vmport (default: auto)
                dump-guest-core=on|off include guest memory in a core dump (default=on)
                mem-merge=on|off controls memory merge support (default: on)
                aes-key-wrap=on|off controls support for AES key wrapping (default=on)
                dea-key-wrap=on|off controls support for DEA key wrapping (default=on)
                suppress-vmdesc=on|off disables self-describing migration (default=off)
                nvdimm=on|off controls NVDIMM support (default=off)
                confidential-guest-support=<id> specifies confidential guest support object (default=none)
                memory-encryption=<id> (memory-encryption is the alias of confidential-guest-support, recommend to use confidential-guest-support)
                hmat=on|off controls ACPI HMAT support (default=off)
                spcr=on|off controls ACPI SPCR support (default=on)
                aux-ram-share=on|off allocate auxiliary guest RAM as shared (default: off)
                memory-backend='backend-id' specifies explicitly provided backend for main RAM (default=none)
                cxl-fmw.0.targets.0=firsttarget,cxl-fmw.0.targets.1=secondtarget,cxl-fmw.0.size=size[,cxl-fmw.0.interleave-granularity=granularity]
                sgx-epc.0.memdev=memid,sgx-epc.0.node=numaid
                smp-cache.0.cache=cachename,smp-cache.0.topology=topologylevel
-M              as -machine
-cpu cpu        select CPU ('-cpu help' for list)
-accel [accel=]accelerator[,prop=value[,...]]
                select accelerator (kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg; use 'help' for a list)
                igd-passthru=on|off (enable Xen integrated Intel graphics passthrough, default=off)
                kernel-irqchip=on|off|split controls accelerated irqchip support (default=on)
                kvm-shadow-mem=size of KVM shadow MMU in bytes
                one-insn-per-tb=on|off (one guest instruction per TCG translation block)
                split-wx=on|off (enable TCG split w^x mapping)
                tb-size=n (TCG translation block cache size)
                dirty-ring-size=n (KVM dirty ring GFN count, default 0)
                eager-split-size=n (KVM Eager Page Split chunk size, default 0, disabled. ARM only)
                notify-vmexit=run|internal-error|disable,notify-window=n (enable notify VM exit and set notify window, x86 only)
                thread=single|multi (enable multi-threaded TCG)
                device=path (KVM device path, default /dev/kvm)
-smp [[cpus=]n][,maxcpus=maxcpus][,drawers=drawers][,books=books][,sockets=sockets]
               [,dies=dies][,clusters=clusters][,modules=modules][,cores=cores]
               [,threads=threads]
                set the number of initial CPUs to 'n' [default=1]
                maxcpus= maximum number of total CPUs, including
                offline CPUs for hotplug, etc
                drawers= number of drawers on the machine board
                books= number of books in one drawer
                sockets= number of sockets in one book
                dies= number of dies in one socket
                clusters= number of clusters in one die
                modules= number of modules in one cluster
                cores= number of cores in one module
                threads= number of threads in one core
Note: Different machines may have different subsets of the CPU topology
      parameters supported, so the actual meaning of the supported parameters
      will vary accordingly. For example, for a machine type that supports a
      three-level CPU hierarchy of sockets/cores/threads, the parameters will
      sequentially mean as below:
                sockets means the number of sockets on the machine board
                cores means the number of cores in one socket
                threads means the number of threads in one core
      For a particular machine type board, an expected CPU topology hierarchy
      can be defined through the supported sub-option. Unsupported parameters
      can also be provided in addition to the sub-option, but their values
      must be set as 1 in the purpose of correct parsing.
-numa node[,mem=size][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa node[,memdev=id][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa dist,src=source,dst=destination,val=distance
-numa cpu,node-id=node[,socket-id=x][,core-id=y][,thread-id=z]
-numa hmat-lb,initiator=node,target=node,hierarchy=memory|first-level|second-level|third-level,data-type=access-latency|read-latency|write-latency[,latency=lat][,bandwidth=bw]
-numa hmat-cache,node-id=node,size=size,level=level[,associativity=none|direct|complex][,policy=none|write-back|write-through][,line=size]
-add-fd fd=fd,set=set[,opaque=opaque]
                Add 'fd' to fd 'set'
-set group.id.arg=value
                set <arg> parameter for item <id> of type <group>
                i.e. -set drive.$id.file=/path/to/image
-global driver.property=value
-global driver=driver,property=property,value=value
                set a global default for a driver property
-boot [order=drives][,once=drives][,menu=on|off]
      [,splash=sp_name][,splash-time=sp_time][,reboot-timeout=rb_time][,strict=on|off]
                'drives': floppy (a), hard disk (c), CD-ROM (d), network (n)
                'sp_name': the file's name that would be passed to bios as logo picture, if menu=on
                'sp_time': the period that splash picture last if menu=on, unit is ms
                'rb_timeout': the timeout before guest reboot when boot failed, unit is ms
-m [size=]megs[,slots=n,maxmem=size]
                configure guest RAM
                size: initial amount of guest memory
                slots: number of hotplug slots (default: none)
                maxmem: maximum amount of guest memory (default: none)
                Note: Some architectures might enforce a specific granularity
-mem-path FILE  provide backing storage for guest RAM
-mem-prealloc   preallocate guest memory (use with -mem-path)
-k language     use keyboard layout (for example 'fr' for French)
-audio [driver=]driver[,prop=value[,...]]
                specifies default audio backend when `audiodev` is not
                used to create a machine or sound device;                options are the same as for -audiodev
-audio [driver=]driver,model=value[,prop=value[,...]]
                specifies the audio backend and device to use;
                apart from 'model', options are the same as for -audiodev.
                use '-audio model=help' to show possible devices.
-audiodev [driver=]driver,id=id[,prop=value[,...]]
                specifies the audio backend to use
                Use ``-audiodev help`` to list the available drivers
                id= identifier of the backend
                timer-period= timer period in microseconds
                in|out.mixing-engine= use mixing engine to mix streams inside QEMU
                in|out.fixed-settings= use fixed settings for host audio
                in|out.frequency= frequency to use with fixed settings
                in|out.channels= number of channels to use with fixed settings
                in|out.format= sample format to use with fixed settings
                valid values: s8, s16, s32, u8, u16, u32, f32
                in|out.voices= number of voices to use
                in|out.buffer-length= length of buffer in microseconds
-audiodev none,id=id,[,prop=value[,...]]
                dummy driver that discards all output
-audiodev alsa,id=id[,prop=value[,...]]
                in|out.dev= name of the audio device to use
                in|out.period-length= length of period in microseconds
                in|out.try-poll= attempt to use poll mode
                threshold= threshold (in microseconds) when playback starts
-audiodev oss,id=id[,prop=value[,...]]
                in|out.dev= path of the audio device to use
                in|out.buffer-count= number of buffers
                in|out.try-poll= attempt to use poll mode
                try-mmap= try using memory mapped access
                exclusive= open device in exclusive mode
                dsp-policy= set timing policy (0..10), -1 to use fragment mode
-audiodev pa,id=id[,prop=value[,...]]
                server= PulseAudio server address
                in|out.name= source/sink device name
                in|out.latency= desired latency in microseconds
-audiodev pipewire,id=id[,prop=value[,...]]
                in|out.name= source/sink device name
                in|out.stream-name= name of pipewire stream
                in|out.latency= desired latency in microseconds
-audiodev sdl,id=id[,prop=value[,...]]
                in|out.buffer-count= number of buffers
-audiodev spice,id=id[,prop=value[,...]]
-audiodev dbus,id=id[,prop=value[,...]]
-audiodev wav,id=id[,prop=value[,...]]
                path= path of wav file to record
-device driver[,prop=value[,...]]
                add device (based on driver)
                prop=value,... sets driver properties
                use '-device help' to print all possible drivers
                use '-device driver,help' to print all possible properties
-name string1[,process=string2][,debug-threads=on|off]
                set the name of the guest
                string1 sets the window title and string2 the process name
                When debug-threads is enabled, individual threads are given a separate name
                NOTE: The thread names are for debugging and not a stable API.
-uuid %08x-%04x-%04x-%04x-%012x
                specify machine UUID
Block device options:
-fda/-fdb file  use 'file' as floppy disk 0/1 image
-hda/-hdb file  use 'file' as hard disk 0/1 image
-hdc/-hdd file  use 'file' as hard disk 2/3 image
-cdrom file     use 'file' as CD-ROM image
-blockdev [driver=]driver[,node-name=N][,discard=ignore|unmap]
          [,cache.direct=on|off][,cache.no-flush=on|off]
          [,read-only=on|off][,auto-read-only=on|off]
          [,force-share=on|off][,detect-zeroes=on|off|unmap]
          [,driver specific parameters...]
                configure a block backend
-drive [file=file][,if=type][,bus=n][,unit=m][,media=d][,index=i]
       [,cache=writethrough|writeback|none|directsync|unsafe][,format=f]
       [,snapshot=on|off][,rerror=ignore|stop|report]
       [,werror=ignore|stop|report|enospc][,id=name]
       [,aio=threads|native|io_uring]
       [,readonly=on|off][,copy-on-read=on|off]
       [,discard=ignore|unmap][,detect-zeroes=on|off|unmap]
       [[,bps=b]|[[,bps_rd=r][,bps_wr=w]]]
       [[,iops=i]|[[,iops_rd=r][,iops_wr=w]]]
       [[,bps_max=bm]|[[,bps_rd_max=rm][,bps_wr_max=wm]]]
       [[,iops_max=im]|[[,iops_rd_max=irm][,iops_wr_max=iwm]]]
       [[,iops_size=is]]
       [[,group=g]]
                use 'file' as a drive image
-mtdblock file  use 'file' as on-board Flash memory image
-sd file        use 'file' as SecureDigital card image
-snapshot       write to temporary files instead of disk image files
-fsdev local,id=id,path=path,security_model=mapped-xattr|mapped-file|passthrough|none
 [,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,max_xattr=max]
 [[,throttling.bps-total=b]|[[,throttling.bps-read=r][,throttling.bps-write=w]]]
 [[,throttling.iops-total=i]|[[,throttling.iops-read=r][,throttling.iops-write=w]]]
 [[,throttling.bps-total-max=bm]|[[,throttling.bps-read-max=rm][,throttling.bps-write-max=wm]]]
 [[,throttling.iops-total-max=im]|[[,throttling.iops-read-max=irm][,throttling.iops-write-max=iwm]]]
 [[,throttling.iops-size=is]]
-fsdev synth,id=id[,max_xattr=max]
-virtfs local,path=path,mount_tag=tag,security_model=mapped-xattr|mapped-file|passthrough|none
        [,id=id][,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,multidevs=remap|forbid|warn][,max_xattr=max]
-virtfs synth,mount_tag=tag[,id=id][,readonly=on][,max_xattr=max]
-iscsi [user=user][,password=password][,password-secret=secret-id]
       [,header-digest=CRC32C|CR32C-NONE|NONE-CRC32C|NONE]
       [,initiator-name=initiator-iqn][,id=target-iqn]
       [,timeout=timeout]
                iSCSI session parameters
USB convenience options:
-usb            enable on-board USB host controller (if not enabled by default)
-usbdevice name add the host or guest USB device 'name'
Display options:
-display spice-app[,gl=on|off]
-display sdl[,gl=on|core|es|off][,grab-mod=<mod>][,show-cursor=on|off]
            [,window-close=on|off]
-display gtk[,clipboard=on|off][,full-screen=on|off][,gl=on|off]
            [,grab-on-hover=on|off][,show-tabs=on|off][,show-cursor=on|off]
            [,window-close=on|off][,show-menubar=on|off][,zoom-to-fit=on|off]
-display vnc=<display>[,<optargs>]
-display curses[,charset=<encoding>]
-display egl-headless[,rendernode=<file>]
-display dbus[,addr=<dbusaddr>]
             [,gl=on|core|es|off][,rendernode=<file>]
-display none
                select display backend type
                The default display is equivalent to
```

### `qemu-system-armhf`

> 官方示例调用：`qemu-system-armhf -h`

```text
root@kali:~# qemu-system-armhf -h
QEMU emulator version 11.1.0 (Debian 1:11.1.0+ds-2)
Copyright (c) 2003-2026 Fabrice Bellard and the QEMU Project developers
usage: qemu-system-armhf [options] [disk_image]
'disk_image' is a raw hard disk image for IDE hard disk 0
Standard options:
-h or -help     display this help and exit
-version        display version information and exit
-machine [type=]name[,prop=value[,...]]
                selects emulated machine ('-machine help' for list)
                property accel=accel1[:accel2[:...]] selects accelerator
                supported accelerators are kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg (default: tcg)
                vmport=on|off|auto controls emulation of vmport (default: auto)
                dump-guest-core=on|off include guest memory in a core dump (default=on)
                mem-merge=on|off controls memory merge support (default: on)
                aes-key-wrap=on|off controls support for AES key wrapping (default=on)
                dea-key-wrap=on|off controls support for DEA key wrapping (default=on)
                suppress-vmdesc=on|off disables self-describing migration (default=off)
                nvdimm=on|off controls NVDIMM support (default=off)
                confidential-guest-support=<id> specifies confidential guest support object (default=none)
                memory-encryption=<id> (memory-encryption is the alias of confidential-guest-support, recommend to use confidential-guest-support)
                hmat=on|off controls ACPI HMAT support (default=off)
                spcr=on|off controls ACPI SPCR support (default=on)
                aux-ram-share=on|off allocate auxiliary guest RAM as shared (default: off)
                memory-backend='backend-id' specifies explicitly provided backend for main RAM (default=none)
                cxl-fmw.0.targets.0=firsttarget,cxl-fmw.0.targets.1=secondtarget,cxl-fmw.0.size=size[,cxl-fmw.0.interleave-granularity=granularity]
                sgx-epc.0.memdev=memid,sgx-epc.0.node=numaid
                smp-cache.0.cache=cachename,smp-cache.0.topology=topologylevel
-M              as -machine
-cpu cpu        select CPU ('-cpu help' for list)
-accel [accel=]accelerator[,prop=value[,...]]
                select accelerator (kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg; use 'help' for a list)
                igd-passthru=on|off (enable Xen integrated Intel graphics passthrough, default=off)
                kernel-irqchip=on|off|split controls accelerated irqchip support (default=on)
                kvm-shadow-mem=size of KVM shadow MMU in bytes
                one-insn-per-tb=on|off (one guest instruction per TCG translation block)
                split-wx=on|off (enable TCG split w^x mapping)
                tb-size=n (TCG translation block cache size)
                dirty-ring-size=n (KVM dirty ring GFN count, default 0)
                eager-split-size=n (KVM Eager Page Split chunk size, default 0, disabled. ARM only)
                notify-vmexit=run|internal-error|disable,notify-window=n (enable notify VM exit and set notify window, x86 only)
                thread=single|multi (enable multi-threaded TCG)
                device=path (KVM device path, default /dev/kvm)
-smp [[cpus=]n][,maxcpus=maxcpus][,drawers=drawers][,books=books][,sockets=sockets]
               [,dies=dies][,clusters=clusters][,modules=modules][,cores=cores]
               [,threads=threads]
                set the number of initial CPUs to 'n' [default=1]
                maxcpus= maximum number of total CPUs, including
                offline CPUs for hotplug, etc
                drawers= number of drawers on the machine board
                books= number of books in one drawer
                sockets= number of sockets in one book
                dies= number of dies in one socket
                clusters= number of clusters in one die
                modules= number of modules in one cluster
                cores= number of cores in one module
                threads= number of threads in one core
Note: Different machines may have different subsets of the CPU topology
      parameters supported, so the actual meaning of the supported parameters
      will vary accordingly. For example, for a machine type that supports a
      three-level CPU hierarchy of sockets/cores/threads, the parameters will
      sequentially mean as below:
                sockets means the number of sockets on the machine board
                cores means the number of cores in one socket
                threads means the number of threads in one core
      For a particular machine type board, an expected CPU topology hierarchy
      can be defined through the supported sub-option. Unsupported parameters
      can also be provided in addition to the sub-option, but their values
      must be set as 1 in the purpose of correct parsing.
-numa node[,mem=size][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa node[,memdev=id][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa dist,src=source,dst=destination,val=distance
-numa cpu,node-id=node[,socket-id=x][,core-id=y][,thread-id=z]
-numa hmat-lb,initiator=node,target=node,hierarchy=memory|first-level|second-level|third-level,data-type=access-latency|read-latency|write-latency[,latency=lat][,bandwidth=bw]
-numa hmat-cache,node-id=node,size=size,level=level[,associativity=none|direct|complex][,policy=none|write-back|write-through][,line=size]
-add-fd fd=fd,set=set[,opaque=opaque]
                Add 'fd' to fd 'set'
-set group.id.arg=value
                set <arg> parameter for item <id> of type <group>
                i.e. -set drive.$id.file=/path/to/image
-global driver.property=value
-global driver=driver,property=property,value=value
                set a global default for a driver property
-boot [order=drives][,once=drives][,menu=on|off]
      [,splash=sp_name][,splash-time=sp_time][,reboot-timeout=rb_time][,strict=on|off]
                'drives': floppy (a), hard disk (c), CD-ROM (d), network (n)
                'sp_name': the file's name that would be passed to bios as logo picture, if menu=on
                'sp_time': the period that splash picture last if menu=on, unit is ms
                'rb_timeout': the timeout before guest reboot when boot failed, unit is ms
-m [size=]megs[,slots=n,maxmem=size]
                configure guest RAM
                size: initial amount of guest memory
                slots: number of hotplug slots (default: none)
                maxmem: maximum amount of guest memory (default: none)
                Note: Some architectures might enforce a specific granularity
-mem-path FILE  provide backing storage for guest RAM
-mem-prealloc   preallocate guest memory (use with -mem-path)
-k language     use keyboard layout (for example 'fr' for French)
-audio [driver=]driver[,prop=value[,...]]
                specifies default audio backend when `audiodev` is not
                used to create a machine or sound device;                options are the same as for -audiodev
-audio [driver=]driver,model=value[,prop=value[,...]]
                specifies the audio backend and device to use;
                apart from 'model', options are the same as for -audiodev.
                use '-audio model=help' to show possible devices.
-audiodev [driver=]driver,id=id[,prop=value[,...]]
                specifies the audio backend to use
                Use ``-audiodev help`` to list the available drivers
                id= identifier of the backend
                timer-period= timer period in microseconds
                in|out.mixing-engine= use mixing engine to mix streams inside QEMU
                in|out.fixed-settings= use fixed settings for host audio
                in|out.frequency= frequency to use with fixed settings
                in|out.channels= number of channels to use with fixed settings
                in|out.format= sample format to use with fixed settings
                valid values: s8, s16, s32, u8, u16, u32, f32
                in|out.voices= number of voices to use
                in|out.buffer-length= length of buffer in microseconds
-audiodev none,id=id,[,prop=value[,...]]
                dummy driver that discards all output
-audiodev alsa,id=id[,prop=value[,...]]
                in|out.dev= name of the audio device to use
                in|out.period-length= length of period in microseconds
                in|out.try-poll= attempt to use poll mode
                threshold= threshold (in microseconds) when playback starts
-audiodev oss,id=id[,prop=value[,...]]
                in|out.dev= path of the audio device to use
                in|out.buffer-count= number of buffers
                in|out.try-poll= attempt to use poll mode
                try-mmap= try using memory mapped access
                exclusive= open device in exclusive mode
                dsp-policy= set timing policy (0..10), -1 to use fragment mode
-audiodev pa,id=id[,prop=value[,...]]
                server= PulseAudio server address
                in|out.name= source/sink device name
                in|out.latency= desired latency in microseconds
-audiodev pipewire,id=id[,prop=value[,...]]
                in|out.name= source/sink device name
                in|out.stream-name= name of pipewire stream
                in|out.latency= desired latency in microseconds
-audiodev sdl,id=id[,prop=value[,...]]
                in|out.buffer-count= number of buffers
-audiodev spice,id=id[,prop=value[,...]]
-audiodev dbus,id=id[,prop=value[,...]]
-audiodev wav,id=id[,prop=value[,...]]
                path= path of wav file to record
-device driver[,prop=value[,...]]
                add device (based on driver)
                prop=value,... sets driver properties
                use '-device help' to print all possible drivers
                use '-device driver,help' to print all possible properties
-name string1[,process=string2][,debug-threads=on|off]
                set the name of the guest
                string1 sets the window title and string2 the process name
                When debug-threads is enabled, individual threads are given a separate name
                NOTE: The thread names are for debugging and not a stable API.
-uuid %08x-%04x-%04x-%04x-%012x
                specify machine UUID
Block device options:
-fda/-fdb file  use 'file' as floppy disk 0/1 image
-hda/-hdb file  use 'file' as hard disk 0/1 image
-hdc/-hdd file  use 'file' as hard disk 2/3 image
-cdrom file     use 'file' as CD-ROM image
-blockdev [driver=]driver[,node-name=N][,discard=ignore|unmap]
          [,cache.direct=on|off][,cache.no-flush=on|off]
          [,read-only=on|off][,auto-read-only=on|off]
          [,force-share=on|off][,detect-zeroes=on|off|unmap]
          [,driver specific parameters...]
                configure a block backend
-drive [file=file][,if=type][,bus=n][,unit=m][,media=d][,index=i]
       [,cache=writethrough|writeback|none|directsync|unsafe][,format=f]
       [,snapshot=on|off][,rerror=ignore|stop|report]
       [,werror=ignore|stop|report|enospc][,id=name]
       [,aio=threads|native|io_uring]
       [,readonly=on|off][,copy-on-read=on|off]
       [,discard=ignore|unmap][,detect-zeroes=on|off|unmap]
       [[,bps=b]|[[,bps_rd=r][,bps_wr=w]]]
       [[,iops=i]|[[,iops_rd=r][,iops_wr=w]]]
       [[,bps_max=bm]|[[,bps_rd_max=rm][,bps_wr_max=wm]]]
       [[,iops_max=im]|[[,iops_rd_max=irm][,iops_wr_max=iwm]]]
       [[,iops_size=is]]
       [[,group=g]]
                use 'file' as a drive image
-mtdblock file  use 'file' as on-board Flash memory image
-sd file        use 'file' as SecureDigital card image
-snapshot       write to temporary files instead of disk image files
-fsdev local,id=id,path=path,security_model=mapped-xattr|mapped-file|passthrough|none
 [,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,max_xattr=max]
 [[,throttling.bps-total=b]|[[,throttling.bps-read=r][,throttling.bps-write=w]]]
 [[,throttling.iops-total=i]|[[,throttling.iops-read=r][,throttling.iops-write=w]]]
 [[,throttling.bps-total-max=bm]|[[,throttling.bps-read-max=rm][,throttling.bps-write-max=wm]]]
 [[,throttling.iops-total-max=im]|[[,throttling.iops-read-max=irm][,throttling.iops-write-max=iwm]]]
 [[,throttling.iops-size=is]]
-fsdev synth,id=id[,max_xattr=max]
-virtfs local,path=path,mount_tag=tag,security_model=mapped-xattr|mapped-file|passthrough|none
        [,id=id][,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,multidevs=remap|forbid|warn][,max_xattr=max]
-virtfs synth,mount_tag=tag[,id=id][,readonly=on][,max_xattr=max]
-iscsi [user=user][,password=password][,password-secret=secret-id]
       [,header-digest=CRC32C|CR32C-NONE|NONE-CRC32C|NONE]
       [,initiator-name=initiator-iqn][,id=target-iqn]
       [,timeout=timeout]
                iSCSI session parameters
USB convenience options:
-usb            enable on-board USB host controller (if not enabled by default)
-usbdevice name add the host or guest USB device 'name'
Display options:
-display spice-app[,gl=on|off]
-display sdl[,gl=on|core|es|off][,grab-mod=<mod>][,show-cursor=on|off]
            [,window-close=on|off]
-display gtk[,clipboard=on|off][,full-screen=on|off][,gl=on|off]
            [,grab-on-hover=on|off][,show-tabs=on|off][,show-cursor=on|off]
            [,window-close=on|off][,show-menubar=on|off][,zoom-to-fit=on|off]
-display vnc=<display>[,<optargs>]
-display curses[,charset=<encoding>]
-display egl-headless[,rendernode=<file>]
-display dbus[,addr=<dbusaddr>]
             [,gl=on|core|es|off][,rendernode=<file>]
-display none
                select display backend type
                The default display is equivalent to
```

### `qemu-pr-helper`

> 官方示例调用：`qemu-pr-helper -h`

```text
root@kali:~# qemu-pr-helper -h
Usage: qemu-pr-helper [OPTIONS] FILE
Persistent Reservation helper program for QEMU
  -h, --help                display this help and exit
  -V, --version             output version information and exit
  -d, --daemon              run in the background
  -f, --pidfile=PATH        PID file when running as a daemon
                            (default '/var/run/qemu-pr-helper.pid')
  -k, --socket=PATH         path to the unix socket
                            (default '/var/run/qemu-pr-helper.sock')
  -T, --trace [[enable=]<pattern>][,events=<file>][,file=<file>]
                            specify tracing options
  -u, --user=USER           user to drop privileges to
  -g, --group=GROUP         group to drop privileges to
See <https://qemu.org/contribute/report-a-bug> for how to report bugs.
More information on the QEMU project at <https://qemu.org>.
```

### `qemu-system-mips`

> 官方示例调用：`qemu-system-mips -h`

```text
root@kali:~# qemu-system-mips -h
QEMU emulator version 11.1.0 (Debian 1:11.1.0+ds-2)
Copyright (c) 2003-2026 Fabrice Bellard and the QEMU Project developers
usage: qemu-system-mips [options] [disk_image]
'disk_image' is a raw hard disk image for IDE hard disk 0
Standard options:
-h or -help     display this help and exit
-version        display version information and exit
-machine [type=]name[,prop=value[,...]]
                selects emulated machine ('-machine help' for list)
                property accel=accel1[:accel2[:...]] selects accelerator
                supported accelerators are kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg (default: tcg)
                vmport=on|off|auto controls emulation of vmport (default: auto)
                dump-guest-core=on|off include guest memory in a core dump (default=on)
                mem-merge=on|off controls memory merge support (default: on)
                aes-key-wrap=on|off controls support for AES key wrapping (default=on)
                dea-key-wrap=on|off controls support for DEA key wrapping (default=on)
                suppress-vmdesc=on|off disables self-describing migration (default=off)
                nvdimm=on|off controls NVDIMM support (default=off)
                confidential-guest-support=<id> specifies confidential guest support object (default=none)
                memory-encryption=<id> (memory-encryption is the alias of confidential-guest-support, recommend to use confidential-guest-support)
                hmat=on|off controls ACPI HMAT support (default=off)
                spcr=on|off controls ACPI SPCR support (default=on)
                aux-ram-share=on|off allocate auxiliary guest RAM as shared (default: off)
                memory-backend='backend-id' specifies explicitly provided backend for main RAM (default=none)
                cxl-fmw.0.targets.0=firsttarget,cxl-fmw.0.targets.1=secondtarget,cxl-fmw.0.size=size[,cxl-fmw.0.interleave-granularity=granularity]
                sgx-epc.0.memdev=memid,sgx-epc.0.node=numaid
                smp-cache.0.cache=cachename,smp-cache.0.topology=topologylevel
-M              as -machine
-cpu cpu        select CPU ('-cpu help' for list)
-accel [accel=]accelerator[,prop=value[,...]]
                select accelerator (kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg; use 'help' for a list)
                igd-passthru=on|off (enable Xen integrated Intel graphics passthrough, default=off)
                kernel-irqchip=on|off|split controls accelerated irqchip support (default=on)
                kvm-shadow-mem=size of KVM shadow MMU in bytes
                one-insn-per-tb=on|off (one guest instruction per TCG translation block)
                split-wx=on|off (enable TCG split w^x mapping)
                tb-size=n (TCG translation block cache size)
                dirty-ring-size=n (KVM dirty ring GFN count, default 0)
                eager-split-size=n (KVM Eager Page Split chunk size, default 0, disabled. ARM only)
                notify-vmexit=run|internal-error|disable,notify-window=n (enable notify VM exit and set notify window, x86 only)
                thread=single|multi (enable multi-threaded TCG)
                device=path (KVM device path, default /dev/kvm)
-smp [[cpus=]n][,maxcpus=maxcpus][,drawers=drawers][,books=books][,sockets=sockets]
               [,dies=dies][,clusters=clusters][,modules=modules][,cores=cores]
               [,threads=threads]
                set the number of initial CPUs to 'n' [default=1]
                maxcpus= maximum number of total CPUs, including
                offline CPUs for hotplug, etc
                drawers= number of drawers on the machine board
                books= number of books in one drawer
                sockets= number of sockets in one book
                dies= number of dies in one socket
                clusters= number of clusters in one die
                modules= number of modules in one cluster
                cores= number of cores in one module
                threads= number of threads in one core
Note: Different machines may have different subsets of the CPU topology
      parameters supported, so the actual meaning of the supported parameters
      will vary accordingly. For example, for a machine type that supports a
      three-level CPU hierarchy of sockets/cores/threads, the parameters will
      sequentially mean as below:
                sockets means the number of sockets on the machine board
                cores means the number of cores in one socket
                threads means the number of threads in one core
      For a particular machine type board, an expected CPU topology hierarchy
      can be defined through the supported sub-option. Unsupported parameters
      can also be provided in addition to the sub-option, but their values
      must be set as 1 in the purpose of correct parsing.
-numa node[,mem=size][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa node[,memdev=id][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa dist,src=source,dst=destination,val=distance
-numa cpu,node-id=node[,socket-id=x][,core-id=y][,thread-id=z]
-numa hmat-lb,initiator=node,target=node,hierarchy=memory|first-level|second-level|third-level,data-type=access-latency|read-latency|write-latency[,latency=lat][,bandwidth=bw]
-numa hmat-cache,node-id=node,size=size,level=level[,associativity=none|direct|complex][,policy=none|write-back|write-through][,line=size]
-add-fd fd=fd,set=set[,opaque=opaque]
                Add 'fd' to fd 'set'
-set group.id.arg=value
                set <arg> parameter for item <id> of type <group>
                i.e. -set drive.$id.file=/path/to/image
-global driver.property=value
-global driver=driver,property=property,value=value
                set a global default for a driver property
-boot [order=drives][,once=drives][,menu=on|off]
      [,splash=sp_name][,splash-time=sp_time][,reboot-timeout=rb_time][,strict=on|off]
                'drives': floppy (a), hard disk (c), CD-ROM (d), network (n)
                'sp_name': the file's name that would be passed to bios as logo picture, if menu=on
                'sp_time': the period that splash picture last if menu=on, unit is ms
                'rb_timeout': the timeout before guest reboot when boot failed, unit is ms
-m [size=]megs[,slots=n,maxmem=size]
                configure guest RAM
                size: initial amount of guest memory
                slots: number of hotplug slots (default: none)
                maxmem: maximum amount of guest memory (default: none)
                Note: Some architectures might enforce a specific granularity
-mem-path FILE  provide backing storage for guest RAM
-mem-prealloc   preallocate guest memory (use with -mem-path)
-k language     use keyboard layout (for example 'fr' for French)
-audio [driver=]driver[,prop=value[,...]]
                specifies default audio backend when `audiodev` is not
                used to create a machine or sound device;                options are the same as for -audiodev
-audio [driver=]driver,model=value[,prop=value[,...]]
                specifies the audio backend and device to use;
                apart from 'model', options are the same as for -audiodev.
                use '-audio model=help' to show possible devices.
-audiodev [driver=]driver,id=id[,prop=value[,...]]
                specifies the audio backend to use
                Use ``-audiodev help`` to list the available drivers
                id= identifier of the backend
                timer-period= timer period in microseconds
                in|out.mixing-engine= use mixing engine to mix streams inside QEMU
                in|out.fixed-settings= use fixed settings for host audio
                in|out.frequency= frequency to use with fixed settings
                in|out.channels= number of channels to use with fixed settings
                in|out.format= sample format to use with fixed settings
                valid values: s8, s16, s32, u8, u16, u32, f32
                in|out.voices= number of voices to use
                in|out.buffer-length= length of buffer in microseconds
-audiodev none,id=id,[,prop=value[,...]]
                dummy driver that discards all output
-audiodev alsa,id=id[,prop=value[,...]]
                in|out.dev= name of the audio device to use
                in|out.period-length= length of period in microseconds
                in|out.try-poll= attempt to use poll mode
                threshold= threshold (in microseconds) when playback starts
-audiodev oss,id=id[,prop=value[,...]]
                in|out.dev= path of the audio device to use
                in|out.buffer-count= number of buffers
                in|out.try-poll= attempt to use poll mode
                try-mmap= try using memory mapped access
                exclusive= open device in exclusive mode
                dsp-policy= set timing policy (0..10), -1 to use fragment mode
-audiodev pa,id=id[,prop=value[,...]]
                server= PulseAudio server address
                in|out.name= source/sink device name
                in|out.latency= desired latency in microseconds
-audiodev pipewire,id=id[,prop=value[,...]]
                in|out.name= source/sink device name
                in|out.stream-name= name of pipewire stream
                in|out.latency= desired latency in microseconds
-audiodev sdl,id=id[,prop=value[,...]]
                in|out.buffer-count= number of buffers
-audiodev spice,id=id[,prop=value[,...]]
-audiodev dbus,id=id[,prop=value[,...]]
-audiodev wav,id=id[,prop=value[,...]]
                path= path of wav file to record
-device driver[,prop=value[,...]]
                add device (based on driver)
                prop=value,... sets driver properties
                use '-device help' to print all possible drivers
                use '-device driver,help' to print all possible properties
-name string1[,process=string2][,debug-threads=on|off]
                set the name of the guest
                string1 sets the window title and string2 the process name
                When debug-threads is enabled, individual threads are given a separate name
                NOTE: The thread names are for debugging and not a stable API.
-uuid %08x-%04x-%04x-%04x-%012x
                specify machine UUID
Block device options:
-fda/-fdb file  use 'file' as floppy disk 0/1 image
-hda/-hdb file  use 'file' as hard disk 0/1 image
-hdc/-hdd file  use 'file' as hard disk 2/3 image
-cdrom file     use 'file' as CD-ROM image
-blockdev [driver=]driver[,node-name=N][,discard=ignore|unmap]
          [,cache.direct=on|off][,cache.no-flush=on|off]
          [,read-only=on|off][,auto-read-only=on|off]
          [,force-share=on|off][,detect-zeroes=on|off|unmap]
          [,driver specific parameters...]
                configure a block backend
-drive [file=file][,if=type][,bus=n][,unit=m][,media=d][,index=i]
       [,cache=writethrough|writeback|none|directsync|unsafe][,format=f]
       [,snapshot=on|off][,rerror=ignore|stop|report]
       [,werror=ignore|stop|report|enospc][,id=name]
       [,aio=threads|native|io_uring]
       [,readonly=on|off][,copy-on-read=on|off]
       [,discard=ignore|unmap][,detect-zeroes=on|off|unmap]
       [[,bps=b]|[[,bps_rd=r][,bps_wr=w]]]
       [[,iops=i]|[[,iops_rd=r][,iops_wr=w]]]
       [[,bps_max=bm]|[[,bps_rd_max=rm][,bps_wr_max=wm]]]
       [[,iops_max=im]|[[,iops_rd_max=irm][,iops_wr_max=iwm]]]
       [[,iops_size=is]]
       [[,group=g]]
                use 'file' as a drive image
-mtdblock file  use 'file' as on-board Flash memory image
-sd file        use 'file' as SecureDigital card image
-snapshot       write to temporary files instead of disk image files
-fsdev local,id=id,path=path,security_model=mapped-xattr|mapped-file|passthrough|none
 [,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,max_xattr=max]
 [[,throttling.bps-total=b]|[[,throttling.bps-read=r][,throttling.bps-write=w]]]
 [[,throttling.iops-total=i]|[[,throttling.iops-read=r][,throttling.iops-write=w]]]
 [[,throttling.bps-total-max=bm]|[[,throttling.bps-read-max=rm][,throttling.bps-write-max=wm]]]
 [[,throttling.iops-total-max=im]|[[,throttling.iops-read-max=irm][,throttling.iops-write-max=iwm]]]
 [[,throttling.iops-size=is]]
-fsdev synth,id=id[,max_xattr=max]
-virtfs local,path=path,mount_tag=tag,security_model=mapped-xattr|mapped-file|passthrough|none
        [,id=id][,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,multidevs=remap|forbid|warn][,max_xattr=max]
-virtfs synth,mount_tag=tag[,id=id][,readonly=on][,max_xattr=max]
-iscsi [user=user][,password=password][,password-secret=secret-id]
       [,header-digest=CRC32C|CR32C-NONE|NONE-CRC32C|NONE]
       [,initiator-name=initiator-iqn][,id=target-iqn]
       [,timeout=timeout]
                iSCSI session parameters
USB convenience options:
-usb            enable on-board USB host controller (if not enabled by default)
-usbdevice name add the host or guest USB device 'name'
Display options:
-display spice-app[,gl=on|off]
-display sdl[,gl=on|core|es|off][,grab-mod=<mod>][,show-cursor=on|off]
            [,window-close=on|off]
-display gtk[,clipboard=on|off][,full-screen=on|off][,gl=on|off]
            [,grab-on-hover=on|off][,show-tabs=on|off][,show-cursor=on|off]
            [,window-close=on|off][,show-menubar=on|off][,zoom-to-fit=on|off]
-display vnc=<display>[,<optargs>]
-display curses[,charset=<encoding>]
-display egl-headless[,rendernode=<file>]
-display dbus[,addr=<dbusaddr>]
             [,gl=on|core|es|off][,rendernode=<file>]
-display none
                select display backend type
                The default display is equivalent to
```

### `qemu-system-mips64`

> 官方示例调用：`qemu-system-mips64 -h`

```text
root@kali:~# qemu-system-mips64 -h
QEMU emulator version 11.1.0 (Debian 1:11.1.0+ds-2)
Copyright (c) 2003-2026 Fabrice Bellard and the QEMU Project developers
usage: qemu-system-mips64 [options] [disk_image]
'disk_image' is a raw hard disk image for IDE hard disk 0
Standard options:
-h or -help     display this help and exit
-version        display version information and exit
-machine [type=]name[,prop=value[,...]]
                selects emulated machine ('-machine help' for list)
                property accel=accel1[:accel2[:...]] selects accelerator
                supported accelerators are kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg (default: tcg)
                vmport=on|off|auto controls emulation of vmport (default: auto)
                dump-guest-core=on|off include guest memory in a core dump (default=on)
                mem-merge=on|off controls memory merge support (default: on)
                aes-key-wrap=on|off controls support for AES key wrapping (default=on)
                dea-key-wrap=on|off controls support for DEA key wrapping (default=on)
                suppress-vmdesc=on|off disables self-describing migration (default=off)
                nvdimm=on|off controls NVDIMM support (default=off)
                confidential-guest-support=<id> specifies confidential guest support object (default=none)
                memory-encryption=<id> (memory-encryption is the alias of confidential-guest-support, recommend to use confidential-guest-support)
                hmat=on|off controls ACPI HMAT support (default=off)
                spcr=on|off controls ACPI SPCR support (default=on)
                aux-ram-share=on|off allocate auxiliary guest RAM as shared (default: off)
                memory-backend='backend-id' specifies explicitly provided backend for main RAM (default=none)
                cxl-fmw.0.targets.0=firsttarget,cxl-fmw.0.targets.1=secondtarget,cxl-fmw.0.size=size[,cxl-fmw.0.interleave-granularity=granularity]
                sgx-epc.0.memdev=memid,sgx-epc.0.node=numaid
                smp-cache.0.cache=cachename,smp-cache.0.topology=topologylevel
-M              as -machine
-cpu cpu        select CPU ('-cpu help' for list)
-accel [accel=]accelerator[,prop=value[,...]]
                select accelerator (kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg; use 'help' for a list)
                igd-passthru=on|off (enable Xen integrated Intel graphics passthrough, default=off)
                kernel-irqchip=on|off|split controls accelerated irqchip support (default=on)
                kvm-shadow-mem=size of KVM shadow MMU in bytes
                one-insn-per-tb=on|off (one guest instruction per TCG translation block)
                split-wx=on|off (enable TCG split w^x mapping)
                tb-size=n (TCG translation block cache size)
                dirty-ring-size=n (KVM dirty ring GFN count, default 0)
                eager-split-size=n (KVM Eager Page Split chunk size, default 0, disabled. ARM only)
                notify-vmexit=run|internal-error|disable,notify-window=n (enable notify VM exit and set notify window, x86 only)
                thread=single|multi (enable multi-threaded TCG)
                device=path (KVM device path, default /dev/kvm)
-smp [[cpus=]n][,maxcpus=maxcpus][,drawers=drawers][,books=books][,sockets=sockets]
               [,dies=dies][,clusters=clusters][,modules=modules][,cores=cores]
               [,threads=threads]
                set the number of initial CPUs to 'n' [default=1]
                maxcpus= maximum number of total CPUs, including
                offline CPUs for hotplug, etc
                drawers= number of drawers on the machine board
                books= number of books in one drawer
                sockets= number of sockets in one book
                dies= number of dies in one socket
                clusters= number of clusters in one die
                modules= number of modules in one cluster
                cores= number of cores in one module
                threads= number of threads in one core
Note: Different machines may have different subsets of the CPU topology
      parameters supported, so the actual meaning of the supported parameters
      will vary accordingly. For example, for a machine type that supports a
      three-level CPU hierarchy of sockets/cores/threads, the parameters will
      sequentially mean as below:
                sockets means the number of sockets on the machine board
                cores means the number of cores in one socket
                threads means the number of threads in one core
      For a particular machine type board, an expected CPU topology hierarchy
      can be defined through the supported sub-option. Unsupported parameters
      can also be provided in addition to the sub-option, but their values
      must be set as 1 in the purpose of correct parsing.
-numa node[,mem=size][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa node[,memdev=id][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa dist,src=source,dst=destination,val=distance
-numa cpu,node-id=node[,socket-id=x][,core-id=y][,thread-id=z]
-numa hmat-lb,initiator=node,target=node,hierarchy=memory|first-level|second-level|third-level,data-type=access-latency|read-latency|write-latency[,latency=lat][,bandwidth=bw]
-numa hmat-cache,node-id=node,size=size,level=level[,associativity=none|direct|complex][,policy=none|write-back|write-through][,line=size]
-add-fd fd=fd,set=set[,opaque=opaque]
                Add 'fd' to fd 'set'
-set group.id.arg=value
                set <arg> parameter for item <id> of type <group>
                i.e. -set drive.$id.file=/path/to/image
-global driver.property=value
-global driver=driver,property=property,value=value
                set a global default for a driver property
-boot [order=drives][,once=drives][,menu=on|off]
      [,splash=sp_name][,splash-time=sp_time][,reboot-timeout=rb_time][,strict=on|off]
                'drives': floppy (a), hard disk (c), CD-ROM (d), network (n)
                'sp_name': the file's name that would be passed to bios as logo picture, if menu=on
                'sp_time': the period that splash picture last if menu=on, unit is ms
                'rb_timeout': the timeout before guest reboot when boot failed, unit is ms
-m [size=]megs[,slots=n,maxmem=size]
                configure guest RAM
                size: initial amount of guest memory
                slots: number of hotplug slots (default: none)
                maxmem: maximum amount of guest memory (default: none)
                Note: Some architectures might enforce a specific granularity
-mem-path FILE  provide backing storage for guest RAM
-mem-prealloc   preallocate guest memory (use with -mem-path)
-k language     use keyboard layout (for example 'fr' for French)
-audio [driver=]driver[,prop=value[,...]]
                specifies default audio backend when `audiodev` is not
                used to create a machine or sound device;                options are the same as for -audiodev
-audio [driver=]driver,model=value[,prop=value[,...]]
                specifies the audio backend and device to use;
                apart from 'model', options are the same as for -audiodev.
                use '-audio model=help' to show possible devices.
-audiodev [driver=]driver,id=id[,prop=value[,...]]
                specifies the audio backend to use
                Use ``-audiodev help`` to list the available drivers
                id= identifier of the backend
                timer-period= timer period in microseconds
                in|out.mixing-engine= use mixing engine to mix streams inside QEMU
                in|out.fixed-settings= use fixed settings for host audio
                in|out.frequency= frequency to use with fixed settings
                in|out.channels= number of channels to use with fixed settings
                in|out.format= sample format to use with fixed settings
                valid values: s8, s16, s32, u8, u16, u32, f32
                in|out.voices= number of voices to use
                in|out.buffer-length= length of buffer in microseconds
-audiodev none,id=id,[,prop=value[,...]]
                dummy driver that discards all output
-audiodev alsa,id=id[,prop=value[,...]]
                in|out.dev= name of the audio device to use
                in|out.period-length= length of period in microseconds
                in|out.try-poll= attempt to use poll mode
                threshold= threshold (in microseconds) when playback starts
-audiodev oss,id=id[,prop=value[,...]]
                in|out.dev= path of the audio device to use
                in|out.buffer-count= number of buffers
                in|out.try-poll= attempt to use poll mode
                try-mmap= try using memory mapped access
                exclusive= open device in exclusive mode
                dsp-policy= set timing policy (0..10), -1 to use fragment mode
-audiodev pa,id=id[,prop=value[,...]]
                server= PulseAudio server address
                in|out.name= source/sink device name
                in|out.latency= desired latency in microseconds
-audiodev pipewire,id=id[,prop=value[,...]]
                in|out.name= source/sink device name
                in|out.stream-name= name of pipewire stream
                in|out.latency= desired latency in microseconds
-audiodev sdl,id=id[,prop=value[,...]]
                in|out.buffer-count= number of buffers
-audiodev spice,id=id[,prop=value[,...]]
-audiodev dbus,id=id[,prop=value[,...]]
-audiodev wav,id=id[,prop=value[,...]]
                path= path of wav file to record
-device driver[,prop=value[,...]]
                add device (based on driver)
                prop=value,... sets driver properties
                use '-device help' to print all possible drivers
                use '-device driver,help' to print all possible properties
-name string1[,process=string2][,debug-threads=on|off]
                set the name of the guest
                string1 sets the window title and string2 the process name
                When debug-threads is enabled, individual threads are given a separate name
                NOTE: The thread names are for debugging and not a stable API.
-uuid %08x-%04x-%04x-%04x-%012x
                specify machine UUID
Block device options:
-fda/-fdb file  use 'file' as floppy disk 0/1 image
-hda/-hdb file  use 'file' as hard disk 0/1 image
-hdc/-hdd file  use 'file' as hard disk 2/3 image
-cdrom file     use 'file' as CD-ROM image
-blockdev [driver=]driver[,node-name=N][,discard=ignore|unmap]
          [,cache.direct=on|off][,cache.no-flush=on|off]
          [,read-only=on|off][,auto-read-only=on|off]
          [,force-share=on|off][,detect-zeroes=on|off|unmap]
          [,driver specific parameters...]
                configure a block backend
-drive [file=file][,if=type][,bus=n][,unit=m][,media=d][,index=i]
       [,cache=writethrough|writeback|none|directsync|unsafe][,format=f]
       [,snapshot=on|off][,rerror=ignore|stop|report]
       [,werror=ignore|stop|report|enospc][,id=name]
       [,aio=threads|native|io_uring]
       [,readonly=on|off][,copy-on-read=on|off]
       [,discard=ignore|unmap][,detect-zeroes=on|off|unmap]
       [[,bps=b]|[[,bps_rd=r][,bps_wr=w]]]
       [[,iops=i]|[[,iops_rd=r][,iops_wr=w]]]
       [[,bps_max=bm]|[[,bps_rd_max=rm][,bps_wr_max=wm]]]
       [[,iops_max=im]|[[,iops_rd_max=irm][,iops_wr_max=iwm]]]
       [[,iops_size=is]]
       [[,group=g]]
                use 'file' as a drive image
-mtdblock file  use 'file' as on-board Flash memory image
-sd file        use 'file' as SecureDigital card image
-snapshot       write to temporary files instead of disk image files
-fsdev local,id=id,path=path,security_model=mapped-xattr|mapped-file|passthrough|none
 [,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,max_xattr=max]
 [[,throttling.bps-total=b]|[[,throttling.bps-read=r][,throttling.bps-write=w]]]
 [[,throttling.iops-total=i]|[[,throttling.iops-read=r][,throttling.iops-write=w]]]
 [[,throttling.bps-total-max=bm]|[[,throttling.bps-read-max=rm][,throttling.bps-write-max=wm]]]
 [[,throttling.iops-total-max=im]|[[,throttling.iops-read-max=irm][,throttling.iops-write-max=iwm]]]
 [[,throttling.iops-size=is]]
-fsdev synth,id=id[,max_xattr=max]
-virtfs local,path=path,mount_tag=tag,security_model=mapped-xattr|mapped-file|passthrough|none
        [,id=id][,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,multidevs=remap|forbid|warn][,max_xattr=max]
-virtfs synth,mount_tag=tag[,id=id][,readonly=on][,max_xattr=max]
-iscsi [user=user][,password=password][,password-secret=secret-id]
       [,header-digest=CRC32C|CR32C-NONE|NONE-CRC32C|NONE]
       [,initiator-name=initiator-iqn][,id=target-iqn]
       [,timeout=timeout]
                iSCSI session parameters
USB convenience options:
-usb            enable on-board USB host controller (if not enabled by default)
-usbdevice name add the host or guest USB device 'name'
Display options:
-display spice-app[,gl=on|off]
-display sdl[,gl=on|core|es|off][,grab-mod=<mod>][,show-cursor=on|off]
            [,window-close=on|off]
-display gtk[,clipboard=on|off][,full-screen=on|off][,gl=on|off]
            [,grab-on-hover=on|off][,show-tabs=on|off][,show-cursor=on|off]
            [,window-close=on|off][,show-menubar=on|off][,zoom-to-fit=on|off]
-display vnc=<display>[,<optargs>]
-display curses[,charset=<encoding>]
-display egl-headless[,rendernode=<file>]
-display dbus[,addr=<dbusaddr>]
             [,gl=on|core|es|off][,rendernode=<file>]
-display none
                select display backend type
                The default display is equivalent to
```

### `qemu-system-mips64el`

> 官方示例调用：`qemu-system-mips64el -h`

```text
root@kali:~# qemu-system-mips64el -h
QEMU emulator version 11.1.0 (Debian 1:11.1.0+ds-2)
Copyright (c) 2003-2026 Fabrice Bellard and the QEMU Project developers
usage: qemu-system-mips64el [options] [disk_image]
'disk_image' is a raw hard disk image for IDE hard disk 0
Standard options:
-h or -help     display this help and exit
-version        display version information and exit
-machine [type=]name[,prop=value[,...]]
                selects emulated machine ('-machine help' for list)
                property accel=accel1[:accel2[:...]] selects accelerator
                supported accelerators are kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg (default: tcg)
                vmport=on|off|auto controls emulation of vmport (default: auto)
                dump-guest-core=on|off include guest memory in a core dump (default=on)
                mem-merge=on|off controls memory merge support (default: on)
                aes-key-wrap=on|off controls support for AES key wrapping (default=on)
                dea-key-wrap=on|off controls support for DEA key wrapping (default=on)
                suppress-vmdesc=on|off disables self-describing migration (default=off)
                nvdimm=on|off controls NVDIMM support (default=off)
                confidential-guest-support=<id> specifies confidential guest support object (default=none)
                memory-encryption=<id> (memory-encryption is the alias of confidential-guest-support, recommend to use confidential-guest-support)
                hmat=on|off controls ACPI HMAT support (default=off)
                spcr=on|off controls ACPI SPCR support (default=on)
                aux-ram-share=on|off allocate auxiliary guest RAM as shared (default: off)
                memory-backend='backend-id' specifies explicitly provided backend for main RAM (default=none)
                cxl-fmw.0.targets.0=firsttarget,cxl-fmw.0.targets.1=secondtarget,cxl-fmw.0.size=size[,cxl-fmw.0.interleave-granularity=granularity]
                sgx-epc.0.memdev=memid,sgx-epc.0.node=numaid
                smp-cache.0.cache=cachename,smp-cache.0.topology=topologylevel
-M              as -machine
-cpu cpu        select CPU ('-cpu help' for list)
-accel [accel=]accelerator[,prop=value[,...]]
                select accelerator (kvm, xen, hvf, nitro, nvmm, whpx, mshv or tcg; use 'help' for a list)
                igd-passthru=on|off (enable Xen integrated Intel graphics passthrough, default=off)
                kernel-irqchip=on|off|split controls accelerated irqchip support (default=on)
                kvm-shadow-mem=size of KVM shadow MMU in bytes
                one-insn-per-tb=on|off (one guest instruction per TCG translation block)
                split-wx=on|off (enable TCG split w^x mapping)
                tb-size=n (TCG translation block cache size)
                dirty-ring-size=n (KVM dirty ring GFN count, default 0)
                eager-split-size=n (KVM Eager Page Split chunk size, default 0, disabled. ARM only)
                notify-vmexit=run|internal-error|disable,notify-window=n (enable notify VM exit and set notify window, x86 only)
                thread=single|multi (enable multi-threaded TCG)
                device=path (KVM device path, default /dev/kvm)
-smp [[cpus=]n][,maxcpus=maxcpus][,drawers=drawers][,books=books][,sockets=sockets]
               [,dies=dies][,clusters=clusters][,modules=modules][,cores=cores]
               [,threads=threads]
                set the number of initial CPUs to 'n' [default=1]
                maxcpus= maximum number of total CPUs, including
                offline CPUs for hotplug, etc
                drawers= number of drawers on the machine board
                books= number of books in one drawer
                sockets= number of sockets in one book
                dies= number of dies in one socket
                clusters= number of clusters in one die
                modules= number of modules in one cluster
                cores= number of cores in one module
                threads= number of threads in one core
Note: Different machines may have different subsets of the CPU topology
      parameters supported, so the actual meaning of the supported parameters
      will vary accordingly. For example, for a machine type that supports a
      three-level CPU hierarchy of sockets/cores/threads, the parameters will
      sequentially mean as below:
                sockets means the number of sockets on the machine board
                cores means the number of cores in one socket
                threads means the number of threads in one core
      For a particular machine type board, an expected CPU topology hierarchy
      can be defined through the supported sub-option. Unsupported parameters
      can also be provided in addition to the sub-option, but their values
      must be set as 1 in the purpose of correct parsing.
-numa node[,mem=size][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa node[,memdev=id][,cpus=firstcpu[-lastcpu]][,nodeid=node][,initiator=node]
-numa dist,src=source,dst=destination,val=distance
-numa cpu,node-id=node[,socket-id=x][,core-id=y][,thread-id=z]
-numa hmat-lb,initiator=node,target=node,hierarchy=memory|first-level|second-level|third-level,data-type=access-latency|read-latency|write-latency[,latency=lat][,bandwidth=bw]
-numa hmat-cache,node-id=node,size=size,level=level[,associativity=none|direct|complex][,policy=none|write-back|write-through][,line=size]
-add-fd fd=fd,set=set[,opaque=opaque]
                Add 'fd' to fd 'set'
-set group.id.arg=value
                set <arg> parameter for item <id> of type <group>
                i.e. -set drive.$id.file=/path/to/image
-global driver.property=value
-global driver=driver,property=property,value=value
                set a global default for a driver property
-boot [order=drives][,once=drives][,menu=on|off]
      [,splash=sp_name][,splash-time=sp_time][,reboot-timeout=rb_time][,strict=on|off]
                'drives': floppy (a), hard disk (c), CD-ROM (d), network (n)
                'sp_name': the file's name that would be passed to bios as logo picture, if menu=on
                'sp_time': the period that splash picture last if menu=on, unit is ms
                'rb_timeout': the timeout before guest reboot when boot failed, unit is ms
-m [size=]megs[,slots=n,maxmem=size]
                configure guest RAM
                size: initial amount of guest memory
                slots: number of hotplug slots (default: none)
                maxmem: maximum amount of guest memory (default: none)
                Note: Some architectures might enforce a specific granularity
-mem-path FILE  provide backing storage for guest RAM
-mem-prealloc   preallocate guest memory (use with -mem-path)
-k language     use keyboard layout (for example 'fr' for French)
-audio [driver=]driver[,prop=value[,...]]
                specifies default audio backend when `audiodev` is not
                used to create a machine or sound device;                options are the same as for -audiodev
-audio [driver=]driver,model=value[,prop=value[,...]]
                specifies the audio backend and device to use;
                apart from 'model', options are the same as for -audiodev.
                use '-audio model=help' to show possible devices.
-audiodev [driver=]driver,id=id[,prop=value[,...]]
                specifies the audio backend to use
                Use ``-audiodev help`` to list the available drivers
                id= identifier of the backend
                timer-period= timer period in microseconds
                in|out.mixing-engine= use mixing engine to mix streams inside QEMU
                in|out.fixed-settings= use fixed settings for host audio
                in|out.frequency= frequency to use with fixed settings
                in|out.channels= number of channels to use with fixed settings
                in|out.format= sample format to use with fixed settings
                valid values: s8, s16, s32, u8, u16, u32, f32
                in|out.voices= number of voices to use
                in|out.buffer-length= length of buffer in microseconds
-audiodev none,id=id,[,prop=value[,...]]
                dummy driver that discards all output
-audiodev alsa,id=id[,prop=value[,...]]
                in|out.dev= name of the audio device to use
                in|out.period-length= length of period in microseconds
                in|out.try-poll= attempt to use poll mode
                threshold= threshold (in microseconds) when playback starts
-audiodev oss,id=id[,prop=value[,...]]
                in|out.dev= path of the audio device to use
                in|out.buffer-count= number of buffers
                in|out.try-poll= attempt to use poll mode
                try-mmap= try using memory mapped access
                exclusive= open device in exclusive mode
                dsp-policy= set timing policy (0..10), -1 to use fragment mode
-audiodev pa,id=id[,prop=value[,...]]
                server= PulseAudio server address
                in|out.name= source/sink device name
                in|out.latency= desired latency in microseconds
-audiodev pipewire,id=id[,prop=value[,...]]
                in|out.name= source/sink device name
                in|out.stream-name= name of pipewire stream
                in|out.latency= desired latency in microseconds
-audiodev sdl,id=id[,prop=value[,...]]
                in|out.buffer-count= number of buffers
-audiodev spice,id=id[,prop=value[,...]]
-audiodev dbus,id=id[,prop=value[,...]]
-audiodev wav,id=id[,prop=value[,...]]
                path= path of wav file to record
-device driver[,prop=value[,...]]
                add device (based on driver)
                prop=value,... sets driver properties
                use '-device help' to print all possible drivers
                use '-device driver,help' to print all possible properties
-name string1[,process=string2][,debug-threads=on|off]
                set the name of the guest
                string1 sets the window title and string2 the process name
                When debug-threads is enabled, individual threads are given a separate name
                NOTE: The thread names are for debugging and not a stable API.
-uuid %08x-%04x-%04x-%04x-%012x
                specify machine UUID
Block device options:
-fda/-fdb file  use 'file' as floppy disk 0/1 image
-hda/-hdb file  use 'file' as hard disk 0/1 image
-hdc/-hdd file  use 'file' as hard disk 2/3 image
-cdrom file     use 'file' as CD-ROM image
-blockdev [driver=]driver[,node-name=N][,discard=ignore|unmap]
          [,cache.direct=on|off][,cache.no-flush=on|off]
          [,read-only=on|off][,auto-read-only=on|off]
          [,force-share=on|off][,detect-zeroes=on|off|unmap]
          [,driver specific parameters...]
                configure a block backend
-drive [file=file][,if=type][,bus=n][,unit=m][,media=d][,index=i]
       [,cache=writethrough|writeback|none|directsync|unsafe][,format=f]
       [,snapshot=on|off][,rerror=ignore|stop|report]
       [,werror=ignore|stop|report|enospc][,id=name]
       [,aio=threads|native|io_uring]
       [,readonly=on|off][,copy-on-read=on|off]
       [,discard=ignore|unmap][,detect-zeroes=on|off|unmap]
       [[,bps=b]|[[,bps_rd=r][,bps_wr=w]]]
       [[,iops=i]|[[,iops_rd=r][,iops_wr=w]]]
       [[,bps_max=bm]|[[,bps_rd_max=rm][,bps_wr_max=wm]]]
       [[,iops_max=im]|[[,iops_rd_max=irm][,iops_wr_max=iwm]]]
       [[,iops_size=is]]
       [[,group=g]]
                use 'file' as a drive image
-mtdblock file  use 'file' as on-board Flash memory image
-sd file        use 'file' as SecureDigital card image
-snapshot       write to temporary files instead of disk image files
-fsdev local,id=id,path=path,security_model=mapped-xattr|mapped-file|passthrough|none
 [,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,max_xattr=max]
 [[,throttling.bps-total=b]|[[,throttling.bps-read=r][,throttling.bps-write=w]]]
 [[,throttling.iops-total=i]|[[,throttling.iops-read=r][,throttling.iops-write=w]]]
 [[,throttling.bps-total-max=bm]|[[,throttling.bps-read-max=rm][,throttling.bps-write-max=wm]]]
 [[,throttling.iops-total-max=im]|[[,throttling.iops-read-max=irm][,throttling.iops-write-max=iwm]]]
 [[,throttling.iops-size=is]]
-fsdev synth,id=id[,max_xattr=max]
-virtfs local,path=path,mount_tag=tag,security_model=mapped-xattr|mapped-file|passthrough|none
        [,id=id][,writeout=immediate][,readonly=on][,fmode=fmode][,dmode=dmode][,multidevs=remap|forbid|warn][,max_xattr=max]
-virtfs synth,mount_tag=tag[,id=id][,readonly=on][,max_xattr=max]
-iscsi [user=user][,password=password][,password-secret=secret-id]
       [,header-digest=CRC32C|CR32C-NONE|NONE-CRC32C|NONE]
       [,initiator-name=initiator-iqn][,id=target-iqn]
       [,timeout=timeout]
                iSCSI session parameters
USB convenience options:
-usb            enable on-board USB host controller (if not enabled by default)
-usbdevice name add the host or guest USB device 'name'
Display options:
-display spice-app[,gl=on|off]
-display sdl[,gl=on|core|es|off][,grab-mod=<mod>][,show-cursor=on|off]
            [,window-close=on|off]
-display gtk[,clipboard=on|off][,full-screen=on|off][,gl=on|off]
            [,grab-on-hover=on|off][,show-tabs=on|off][,show-cursor=on|off]
            [,window-close=on|off][,show-menubar=on|off][,zoom-to-fit=on|off]
-display vnc=<display>[,<optargs>]
-display curses[,charset=<encoding>]
-display egl-headless[,rendernode=<file>]
-display dbus[,addr=<dbusaddr>]
             [,gl=on|core|es|off][,rendernode=<file>]
-display none
                select display backend type
                The default display is equivalent to
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install qemu-block-extra`，再执行 `qemu-block-extra --version` 2>/dev/null || `qemu-block-extra -V`
- [ ] **2.** **读官方帮助** —— `qemu-block-extra -h`，需要细节时 `man qemu-block-extra`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: qemu-ga [-m <method> -p <path>] [<options>]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/qemu/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/qemu/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/qemu/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
