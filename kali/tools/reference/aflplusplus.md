# aflplusplus

> Instrumentation-driven fuzzer for binary formats American fuzzy lop is a fuzzer that employs compile-time instrumentation and genetic algorithms to automatically discover clean, interesting test cases that trigger new internal states in th…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`aflplusplus` ｜ **官方文档**：<https://www.kali.org/tools/aflplusplus/>

## 1. 安装

```bash
sudo apt update
sudo apt install afl++
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.02c |
| 架构 | any |
| 可执行命令 | `afl++`、`afl-addseeds`、`afl-analyze`、`afl-c++`、`afl-cc`、`afl-clang`、`afl-clang++`、`afl-clang-fast`、`afl-clang-fast++`、`afl-clang-lto`、`afl-clang-lto++`、`afl-cmin`、`afl-cmin.awk`、`afl-cmin.bash`、`afl-cmin.py`、`afl-fuzz`、`afl-g++`、`afl-g++-fast`、`afl-gcc`、`afl-gcc-fast`、`afl-gotcpu`、`afl-health`、`afl-ld-lto`、`afl-lto`、`afl-lto++`、`afl-network-client`、`afl-network-server`、`afl-persistent-config`、`afl-plot`、`afl-showmap`、`afl-system-config`、`afl-tmin`、`afl-whatsup`、`afl++-doc` |
| 依赖 | `build-essential`、`clang`、`clang-21`、`libc6`、`libgcc-s1`、`libpython3.14`、`libstdc++6`、`procps`、`python3`、`zlib1g`、`afl-addseeds` |
| 安装体积 | 4.41 MB |
| 官网 | <https://github.com/AFLplusplus/AFLplusplus> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/aflplusplus> |
| 包追踪 | <https://pkg.kali.org/pkg/aflplusplus> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
afl++ -h          # 查看用法
man afl++         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 34 个可执行命令，下面是官方页面内嵌的帮助原文。

### `afl-addseeds`

官方给出的调用示例：`afl-addseeds -h`

```text
root@kali:~# afl-addseeds -h
afl-addseeds by Marc Heuse
Syntax: afl-addseeds -o afl-out-dir [-i seed_file_or_dir] seed_file_or_seed_dir seed_file_or_seed_dir ...
Options:
  -o afl-out-dir       the output directory being used in the fuzzing campaign
  -i seed_file_or_dir  file or directory of files to add
Adds new seeds to an existing AFL++ fuzzing campaign.
```

### `afl-analyze`

官方给出的调用示例：`afl-analyze --help`

```text
root@kali:~# afl-analyze --help
afl-analyze++5.02c by Michal Zalewski
afl-analyze: invalid option -- '-'
afl-analyze [ options ] -- /path/to/target_app [ ... ]
Required parameters:
  -i file       - input test case to be analyzed by the tool
Execution control settings:
  -f file       - input file read by the tested program (stdin)
  -t msec       - timeout for each run (1000 ms)
  -m megs       - memory limit for child process (0 MB)
  -O            - use binary-only instrumentation (FRIDA mode)
  -Q            - use binary-only instrumentation (QEMU mode)
  -U            - use unicorn-based instrumentation (Unicorn mode)
  -W            - use qemu-based instrumentation with Wine (Wine mode)
  -X            - use Nyx mode
Analysis settings:
  -e            - look for edge coverage only, ignore hit counts
For additional tips, please consult docs/README.md.
Environment variables used:
TMPDIR: directory to use for temporary input files
ASAN_OPTIONS: custom settings for ASAN
              (must contain abort_on_error=1 and symbolize=0)
MSAN_OPTIONS: custom settings for MSAN
              (must contain exitcode=86 and symbolize=0)
AFL_ANALYZE_HEX: print file offsets in hexadecimal instead of decimal
AFL_KILL_SIGNAL: Signal ID delivered to child processes on timeout, etc.
                 (default: SIGKILL)
AFL_FORK_SERVER_KILL_SIGNAL: Kill signal for the fork server on termination
                             (default: SIGTERM). If unset and AFL_KILL_SIGNAL is
                             set, that value will be used.
AFL_MAP_SIZE: the shared memory size for that target. must be >= the size
              the target was compiled for
AFL_PRELOAD: LD_PRELOAD / DYLD_INSERT_LIBRARIES settings for target
AFL_INPUT_PLACEHOLDER: custom placeholder for input file (default: @@)
AFL_SKIP_BIN_CHECK: skip checking the location of and the target
```

### `afl-c++`

官方给出的调用示例：`afl-c++ --help`

```text
root@kali:~# afl-c++ --help
OVERVIEW: clang LLVM compiler
USAGE: clang [options] file...
OPTIONS:
  -###                    Print (but do not run) the commands to run for this compilation
  --analyzer-output <value>
                          Static analyzer report output format (html|plist|plist-multi-file|plist-html|sarif|sarif-html|text).
  --analyze               Run the static analyzer
  -B <prefix>             Search $prefix$file for executables, libraries, and data files. If $prefix is a directory, search $prefix/$file
  -b <arg>                Pass -b <arg> to the linker on AIX
  -CC                     Include comments from within macros in preprocessed output
  -cl-denorms-are-zero    OpenCL only. Allow denormals to be flushed to zero.
  -cl-ext=<value>         OpenCL only. Enable or disable OpenCL extensions/optional features. The argument is a comma-separated sequence of one or more extension names, each prefixed by '+' or '-'.
  -cl-fast-relaxed-math   OpenCL only. Sets -cl-finite-math-only and -cl-unsafe-math-optimizations, and defines __FAST_RELAXED_MATH__.
  -cl-finite-math-only    OpenCL only. Allow floating-point optimizations that assume arguments and results are not NaNs or +-Inf.
  -cl-fp32-correctly-rounded-divide-sqrt
                          OpenCL only. Specify that single precision floating-point divide and sqrt used in the program source are correctly rounded.
  -cl-kernel-arg-info     OpenCL only. Generate kernel argument metadata.
  -cl-mad-enable          OpenCL only. Allow use of less precise MAD computations in the generated binary.
  -cl-no-signed-zeros     OpenCL only. Allow use of less precise no signed zeros computations in the generated binary.
  -cl-no-stdinc           OpenCL only. Disables all standard includes containing non-native compiler types and functions.
  -cl-opt-disable         OpenCL only. This option disables all optimizations. By default optimizations are enabled.
  -cl-single-precision-constant
                          OpenCL only. Treat double precision floating-point constant as single precision constant.
  -cl-std=<value>         OpenCL language standard to compile for.
  -cl-strict-aliasing     OpenCL only. This option is added for compatibility with OpenCL 1.0.
  -cl-uniform-work-group-size
                          OpenCL only. Defines that the global work-size be a multiple of the work-group size specified to clEnqueueNDRangeKernel
  -cl-unsafe-math-optimizations
                          OpenCL only. Allow unsafe floating-point optimizations.  Also implies -cl-no-signed-zeros and -cl-mad-enable.
  -clangir-disable-passes Disable CIR transformations pipeline
  -clangir-disable-verifier
                          ClangIR: Disable MLIR module verifier
  --config=<file>         Specify configuration file
  --cuda-compile-host-device
                          Compile CUDA code for both host and device (default). Has no effect on non-CUDA compilations.
  --cuda-device-only      Compile CUDA code for device only
  --cuda-feature=<value>  Manually specify the CUDA feature to use
  --cuda-host-only        Compile CUDA code for host only. Has no effect on non-CUDA compilations.
  --cuda-include-ptx=<value>
                          Include PTX for the following GPU architecture (e.g. sm_35) or 'all'. May be specified more than once.
  --cuda-noopt-device-debug
                          Enable device-side debug info generation. Disables ptxas optimizations.
  --cuda-path-ignore-env  Ignore environment variables to detect CUDA installation
  --cuda-path=<value>     CUDA installation path
  -cuid=<value>           An ID for compilation unit, which should be the same for the same compilation unit but different for different compilation units. It is used to externalize device-side static variables for single source offloading languages CUDA and HIP so that they can be accessed by the host code of the same compilation unit.
  -cxx-isystem <directory>
                          Add directory to the C++ SYSTEM include search path
  -C                      Include comments in preprocessed output
  -c                      Only run preprocess, compile, and assemble steps
  -darwin-target-variant-triple <value>
                          Specify the darwin target variant triple
  -darwin-target-variant <value>
                          Generate code for an additional runtime variant of the deployment target
  -dD                     Print macro definitions in -E mode in addition to normal output
  -dependency-dot <value> Filename to write DOT-formatted header dependencies to
  -dependency-file <value>
                          Filename (or -) to write dependency output to
  -dI                     Print include directives in -E mode in addition to normal output
  -dM                     Print macro definitions in -E mode instead of normal output
  -dsym-dir <dir>         Directory to output dSYM's (if any) to
  -dumpdir <dumppfx>      Use <dumpfpx> as a prefix to form auxiliary and dump file names
  -dumpmachine            Display the compiler's target processor
  -dumpversion            Display the version of the compiler
  -D <macro>=<value>      Define <macro> to <value> (or 1 if <value> omitted)
  --embed-dir=<dir>       Add directory to embed search path
  -emit-ast               Emit Clang AST files for source inputs
  -emit-cir               Build ASTs and then lower to ClangIR
  --emit-extension-symbol-graphs
                          Generate additional symbol graphs for extended modules.
  -emit-interface-stubs   Generate Interface Stub Files.
  -emit-llvm              Use the LLVM representation for assembler and object files
  -emit-merged-ifs        Generate Interface Stub Files, emit merged text not binary.
  --emit-static-lib       Enable linker job to emit a static library.
  -emit-symbol-graph      Generate Extract API information as a side effect of compilation.
  --end-no-unused-arguments
                          Start emitting warnings for unused driver arguments
  --extract-api-ignores=<value>
                          Comma separated list of files containing a new line separated list of API symbols to ignore when extracting API information.
  -extract-api            Extract API information
  -E                      Only run the preprocessor
  -faapcs-bitfield-load   Follows the AAPCS standard that all volatile bit-field write generates at least one load. (ARM only).
  -faapcs-bitfield-width  Follow the AAPCS standard requirement stating that volatile bit-field width is dictated by the field container type. (ARM only).
  -faarch64-jump-table-hardening
                          Use hardened lowering for jump-table dispatch
  -faddrsig               Emit an address-significance table
  -falign-loops=<N>       N must be a power of two. Align loops to the boundary
  -faligned-allocation    Enable C++17 aligned allocation functions
  -fallow-editor-placeholders
                          Treat editor placeholders as valid source code
  -fallow-runtime-check-skip-hot-cutoff=<value>
                          Exclude __builtin_allow_runtime_check for the top hottest code responsible for the given fraction of PGO counters (0.0 [default] = skip none; 1.0 = skip all). Argument format: <value>
  -faltivec-src-compat=<value>
                          Source-level compatibility for Altivec vectors (for PowerPC targets). This includes results of vector comparison (scalar for 'xl', vector for 'gcc') as well as behavior when initializing with a scalar (splatting for 'xl', element zero only for 'gcc'). For 'mixed', the compatibility is as 'gcc' for 'vector bool/vector pixel' and as 'xl' for other types. Current default is 'mixed'.
  -fansi-escape-codes     Use ANSI escape codes for diagnostics
  -fapinotes-modules      Enable module-based external API notes support
  -fapinotes-swift-version=<version>
                          Specify the Swift version to use when filtering API notes
  -fapinotes              Enable external API notes support
  -fapple-kext            Use Apple's kernel extensions ABI
  -fapple-link-rtlib      Force linking the clang builtins runtime library
  -fapple-pragma-pack     Enable Apple gcc-compatible #pragma pack handling
  -fapplication-extension Restrict code to those available for App Extensions
  -fapprox-func           Allow certain math function calls to be replaced with an approximately equivalent calculation
  -fassume-nothrow-exception-dtor
                          Assume that exception objects' destructors are non-throwing
  -fasync-exceptions      Enable EH Asynchronous exceptions
  -fatomic-fine-grained-memory
                          May have atomic operations on fine-grained memory
  -fatomic-ignore-denormal-mode
                          Allow atomic operations to ignore denormal mode
  -fatomic-remote-memory  May have atomic operations on remote memory
  -fauto-import           MinGW specific. Enable code generation support for automatic dllimport, and enable support for it in the linker. Enabled by default.
  -fbasic-block-address-map
                          Emit the basic block address map section.
  -fbasic-block-sections=<value>
                          Place each function's basic blocks in unique sections (ELF Only)
  -fbinutils-version=<major.minor>
                          Produced object files can use all ELF features supported by this binutils version and newer. If -fno-integrated-as is specified, the generated assembly will consider GNU as support. 'none' means that all ELF features can be used, regardless of binutils support. Defaults to 2.26.
  -fblocks                Enable the 'blocks' language feature
  -fborland-extensions    Accept non-standard constructs supported by the Borland compiler
  -fbuild-session-file=<file>
                          Use the last modification time of <file> as the build session timestamp
  -fbuild-session-timestamp=<time since Epoch in seconds>
                          Time when the current build session started
  -fbuiltin-module-map    Load the clang builtins module map file.
  -fc++-abi=<value>       C++ ABI to use. This will override the target C++ ABI.
  -fc++-static-destructors=<value>
                          Controls which variables C++ static destructors are registered for
  -fcall-saved-x10        Make the x10 register call-saved (AArch64 only)
  -fcall-saved-x11        Make the x11 register call-saved (AArch64 only)
  -fcall-saved-x12        Make the x12 register call-saved (AArch64 only)
  -fcall-saved-x13        Make the x13 register call-saved (AArch64 only)
  -fcall-saved-x14        Make the x14 register call-saved (AArch64 only)
  -fcall-saved-x15        Make the x15 register call-saved (AArch64 only)
  -fcall-saved-x18        Make the x18 register call-saved (AArch64 only)
  -fcall-saved-x8         Make the x8 register call-saved (AArch64 only)
  -fcall-saved-x9         Make the x9 register call-saved (AArch64 only)
  -fcaret-diagnostics-max-lines=<value>
                          Set the maximum number of source lines to show in a caret diagnostic (0 = no limit).
  -fcf-protection=<value> Instrument control-flow architecture protection
  -fcf-protection         Enable cf-protection in 'full' mode
  -fchar8_t               Enable C++ builtin type char8_t
  -fcheck-new             Do not assume C++ operator new may not return NULL
  -fclang-abi-compat=<version>
                          Attempt to match the ABI of Clang <version>
  -fclangir               Use the ClangIR pipeline to compile
  -fcodegen-data-generate=<path>
                          Emit codegen data into the object file. LLD for MachO (currently) merges them into the specified <path>.
  -fcodegen-data-generate Emit codegen data into the object file. LLD for MachO (currently) merges them into default.cgdata.
  -fcodegen-data-use=<path>
                          Use codegen data read from the specified <path>.
  -fcodegen-data-use      Use codegen data read from default.cgdata to optimize the binary
  -fcolor-diagnostics     Enable colors in diagnostics
  -fcomment-block-commands=<arg>
                          Treat each comma separated argument in <arg> as a documentation comment block command
  -fcommon                Place uninitialized global variables in a common block
  -fcomplete-member-pointers
                          Require member pointer base types to be complete if they would be significant under the Microsoft ABI
  -fcomplex-arithmetic=<value>
                          Controls the calculation methods of complex number multiplication and division.
  -fconstexpr-backtrace-limit=<value>
                          Set the maximum number of entries to print in a constexpr evaluation backtrace (0 = no limit)
  -fconstexpr-depth=<value>
                          Set the maximum depth of recursive constexpr function calls
  -fconstexpr-steps=<value>
                          Set the maximum number of steps in constexpr function evaluation
  -fconvergent-functions  Assume all functions may be convergent.
  -fcoro-aligned-allocation
                          Prefer aligned allocation for C++ Coroutines
  -fcoroutines            Enable support for the C++ Coroutines
  -fcoverage-compilation-dir=<value>
                          The compilation directory to embed in the coverage mapping.
  -fcoverage-mapping      Generate coverage mapping to enable code coverage analysis
  -fcoverage-mcdc         Enable MC/DC criteria when generating code coverage
  -fcoverage-prefix-map=<old>=<new>
                          remap file source paths <old> to <new> in coverage mapping. If there are multiple options, prefix replacement is applied in reverse order starting from the last one
  -fcrash-diagnostics-dir=<dir>
                          Put crash-report files in <dir>
  -fcrash-diagnostics=<value>
                          Set level of crash diagnostic reporting, (option: off, compiler, all)
  -fcrash-diagnostics     Enable crash diagnostic reporting (default)
  -fcs-profile-generate=<directory>
                          Generate instrumented code to collect context sensitive execution counts into <directory>/default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcs-profile-generate   Generate instrumented code to collect context sensitive execution counts into default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcuda-short-ptr        Use 32-bit pointers for accessing const/local/shared address spaces
  -fcx-fortran-rules      Range reduction is enabled for complex arithmetic operations.
  -fcx-limited-range      Basic algebraic expansions of complex arithmetic operations involving are enabled.
  -fcxx-exceptions        Enable C++ exceptions
  -fcxx-modules           Enable modules for C++
  -fdata-sections         Place each data in its own section
  -fdebug-compilation-dir=<value>
                          The compilation directory to embed in the debug info
  -fdebug-default-version=<value>
                          Default DWARF version to use, if a -g option caused DWARF debug info to be produced
  -fdebug-info-for-profiling
                          Emit extra debug info to make sample profile more accurate
  -fdebug-macro           Emit macro debug information
  -fdebug-prefix-map=<old>=<new>
                          For paths in debug info, remap directory <old> to <new>. If multiple options match a path, the last option wins
  -fdebug-ranges-base-address
                          Use DWARF base address selection entries in .debug_ranges
  -fdebug-types-section   Place debug types in their own section (ELF Only)
  -fdeclspec              Allow __declspec as a keyword
  -fdefine-target-os-macros
                          Enable predefined target OS macros
  -fdelayed-template-parsing
                          Parse templated function definitions at the end of the translation unit
  -fdelete-null-pointer-checks
                          Treat usage of null pointers as undefined behavior (default)
  -fdiagnostics-absolute-paths
                          Print absolute paths in diagnostics
  -fdiagnostics-color=<value>
                          When to use colors in diagnostics
  -fdiagnostics-hotness-threshold=<value>
                          Prevent optimization remarks from being output if they do not have at least this profile count. Use 'auto' to apply the threshold from profile summary
  -fdiagnostics-misexpect-tolerance=<value>
                          Prevent misexpect diagnostics from being output if the profile counts are within N% of the expected.
  -fdiagnostics-parseable-fixits
                          Print fix-its in machine parseable form
```

### `afl-cc`

官方给出的调用示例：`afl-cc --help`

```text
root@kali:~# afl-cc --help
OVERVIEW: clang LLVM compiler
USAGE: clang [options] file...
OPTIONS:
  -###                    Print (but do not run) the commands to run for this compilation
  --analyzer-output <value>
                          Static analyzer report output format (html|plist|plist-multi-file|plist-html|sarif|sarif-html|text).
  --analyze               Run the static analyzer
  -B <prefix>             Search $prefix$file for executables, libraries, and data files. If $prefix is a directory, search $prefix/$file
  -b <arg>                Pass -b <arg> to the linker on AIX
  -CC                     Include comments from within macros in preprocessed output
  -cl-denorms-are-zero    OpenCL only. Allow denormals to be flushed to zero.
  -cl-ext=<value>         OpenCL only. Enable or disable OpenCL extensions/optional features. The argument is a comma-separated sequence of one or more extension names, each prefixed by '+' or '-'.
  -cl-fast-relaxed-math   OpenCL only. Sets -cl-finite-math-only and -cl-unsafe-math-optimizations, and defines __FAST_RELAXED_MATH__.
  -cl-finite-math-only    OpenCL only. Allow floating-point optimizations that assume arguments and results are not NaNs or +-Inf.
  -cl-fp32-correctly-rounded-divide-sqrt
                          OpenCL only. Specify that single precision floating-point divide and sqrt used in the program source are correctly rounded.
  -cl-kernel-arg-info     OpenCL only. Generate kernel argument metadata.
  -cl-mad-enable          OpenCL only. Allow use of less precise MAD computations in the generated binary.
  -cl-no-signed-zeros     OpenCL only. Allow use of less precise no signed zeros computations in the generated binary.
  -cl-no-stdinc           OpenCL only. Disables all standard includes containing non-native compiler types and functions.
  -cl-opt-disable         OpenCL only. This option disables all optimizations. By default optimizations are enabled.
  -cl-single-precision-constant
                          OpenCL only. Treat double precision floating-point constant as single precision constant.
  -cl-std=<value>         OpenCL language standard to compile for.
  -cl-strict-aliasing     OpenCL only. This option is added for compatibility with OpenCL 1.0.
  -cl-uniform-work-group-size
                          OpenCL only. Defines that the global work-size be a multiple of the work-group size specified to clEnqueueNDRangeKernel
  -cl-unsafe-math-optimizations
                          OpenCL only. Allow unsafe floating-point optimizations.  Also implies -cl-no-signed-zeros and -cl-mad-enable.
  -clangir-disable-passes Disable CIR transformations pipeline
  -clangir-disable-verifier
                          ClangIR: Disable MLIR module verifier
  --config=<file>         Specify configuration file
  --cuda-compile-host-device
                          Compile CUDA code for both host and device (default). Has no effect on non-CUDA compilations.
  --cuda-device-only      Compile CUDA code for device only
  --cuda-feature=<value>  Manually specify the CUDA feature to use
  --cuda-host-only        Compile CUDA code for host only. Has no effect on non-CUDA compilations.
  --cuda-include-ptx=<value>
                          Include PTX for the following GPU architecture (e.g. sm_35) or 'all'. May be specified more than once.
  --cuda-noopt-device-debug
                          Enable device-side debug info generation. Disables ptxas optimizations.
  --cuda-path-ignore-env  Ignore environment variables to detect CUDA installation
  --cuda-path=<value>     CUDA installation path
  -cuid=<value>           An ID for compilation unit, which should be the same for the same compilation unit but different for different compilation units. It is used to externalize device-side static variables for single source offloading languages CUDA and HIP so that they can be accessed by the host code of the same compilation unit.
  -cxx-isystem <directory>
                          Add directory to the C++ SYSTEM include search path
  -C                      Include comments in preprocessed output
  -c                      Only run preprocess, compile, and assemble steps
  -darwin-target-variant-triple <value>
                          Specify the darwin target variant triple
  -darwin-target-variant <value>
                          Generate code for an additional runtime variant of the deployment target
  -dD                     Print macro definitions in -E mode in addition to normal output
  -dependency-dot <value> Filename to write DOT-formatted header dependencies to
  -dependency-file <value>
                          Filename (or -) to write dependency output to
  -dI                     Print include directives in -E mode in addition to normal output
  -dM                     Print macro definitions in -E mode instead of normal output
  -dsym-dir <dir>         Directory to output dSYM's (if any) to
  -dumpdir <dumppfx>      Use <dumpfpx> as a prefix to form auxiliary and dump file names
  -dumpmachine            Display the compiler's target processor
  -dumpversion            Display the version of the compiler
  -D <macro>=<value>      Define <macro> to <value> (or 1 if <value> omitted)
  --embed-dir=<dir>       Add directory to embed search path
  -emit-ast               Emit Clang AST files for source inputs
  -emit-cir               Build ASTs and then lower to ClangIR
  --emit-extension-symbol-graphs
                          Generate additional symbol graphs for extended modules.
  -emit-interface-stubs   Generate Interface Stub Files.
  -emit-llvm              Use the LLVM representation for assembler and object files
  -emit-merged-ifs        Generate Interface Stub Files, emit merged text not binary.
  --emit-static-lib       Enable linker job to emit a static library.
  -emit-symbol-graph      Generate Extract API information as a side effect of compilation.
  --end-no-unused-arguments
                          Start emitting warnings for unused driver arguments
  --extract-api-ignores=<value>
                          Comma separated list of files containing a new line separated list of API symbols to ignore when extracting API information.
  -extract-api            Extract API information
  -E                      Only run the preprocessor
  -faapcs-bitfield-load   Follows the AAPCS standard that all volatile bit-field write generates at least one load. (ARM only).
  -faapcs-bitfield-width  Follow the AAPCS standard requirement stating that volatile bit-field width is dictated by the field container type. (ARM only).
  -faarch64-jump-table-hardening
                          Use hardened lowering for jump-table dispatch
  -faddrsig               Emit an address-significance table
  -falign-loops=<N>       N must be a power of two. Align loops to the boundary
  -faligned-allocation    Enable C++17 aligned allocation functions
  -fallow-editor-placeholders
                          Treat editor placeholders as valid source code
  -fallow-runtime-check-skip-hot-cutoff=<value>
                          Exclude __builtin_allow_runtime_check for the top hottest code responsible for the given fraction of PGO counters (0.0 [default] = skip none; 1.0 = skip all). Argument format: <value>
  -faltivec-src-compat=<value>
                          Source-level compatibility for Altivec vectors (for PowerPC targets). This includes results of vector comparison (scalar for 'xl', vector for 'gcc') as well as behavior when initializing with a scalar (splatting for 'xl', element zero only for 'gcc'). For 'mixed', the compatibility is as 'gcc' for 'vector bool/vector pixel' and as 'xl' for other types. Current default is 'mixed'.
  -fansi-escape-codes     Use ANSI escape codes for diagnostics
  -fapinotes-modules      Enable module-based external API notes support
  -fapinotes-swift-version=<version>
                          Specify the Swift version to use when filtering API notes
  -fapinotes              Enable external API notes support
  -fapple-kext            Use Apple's kernel extensions ABI
  -fapple-link-rtlib      Force linking the clang builtins runtime library
  -fapple-pragma-pack     Enable Apple gcc-compatible #pragma pack handling
  -fapplication-extension Restrict code to those available for App Extensions
  -fapprox-func           Allow certain math function calls to be replaced with an approximately equivalent calculation
  -fassume-nothrow-exception-dtor
                          Assume that exception objects' destructors are non-throwing
  -fasync-exceptions      Enable EH Asynchronous exceptions
  -fatomic-fine-grained-memory
                          May have atomic operations on fine-grained memory
  -fatomic-ignore-denormal-mode
                          Allow atomic operations to ignore denormal mode
  -fatomic-remote-memory  May have atomic operations on remote memory
  -fauto-import           MinGW specific. Enable code generation support for automatic dllimport, and enable support for it in the linker. Enabled by default.
  -fbasic-block-address-map
                          Emit the basic block address map section.
  -fbasic-block-sections=<value>
                          Place each function's basic blocks in unique sections (ELF Only)
  -fbinutils-version=<major.minor>
                          Produced object files can use all ELF features supported by this binutils version and newer. If -fno-integrated-as is specified, the generated assembly will consider GNU as support. 'none' means that all ELF features can be used, regardless of binutils support. Defaults to 2.26.
  -fblocks                Enable the 'blocks' language feature
  -fborland-extensions    Accept non-standard constructs supported by the Borland compiler
  -fbuild-session-file=<file>
                          Use the last modification time of <file> as the build session timestamp
  -fbuild-session-timestamp=<time since Epoch in seconds>
                          Time when the current build session started
  -fbuiltin-module-map    Load the clang builtins module map file.
  -fc++-abi=<value>       C++ ABI to use. This will override the target C++ ABI.
  -fc++-static-destructors=<value>
                          Controls which variables C++ static destructors are registered for
  -fcall-saved-x10        Make the x10 register call-saved (AArch64 only)
  -fcall-saved-x11        Make the x11 register call-saved (AArch64 only)
  -fcall-saved-x12        Make the x12 register call-saved (AArch64 only)
  -fcall-saved-x13        Make the x13 register call-saved (AArch64 only)
  -fcall-saved-x14        Make the x14 register call-saved (AArch64 only)
  -fcall-saved-x15        Make the x15 register call-saved (AArch64 only)
  -fcall-saved-x18        Make the x18 register call-saved (AArch64 only)
  -fcall-saved-x8         Make the x8 register call-saved (AArch64 only)
  -fcall-saved-x9         Make the x9 register call-saved (AArch64 only)
  -fcaret-diagnostics-max-lines=<value>
                          Set the maximum number of source lines to show in a caret diagnostic (0 = no limit).
  -fcf-protection=<value> Instrument control-flow architecture protection
  -fcf-protection         Enable cf-protection in 'full' mode
  -fchar8_t               Enable C++ builtin type char8_t
  -fcheck-new             Do not assume C++ operator new may not return NULL
  -fclang-abi-compat=<version>
                          Attempt to match the ABI of Clang <version>
  -fclangir               Use the ClangIR pipeline to compile
  -fcodegen-data-generate=<path>
                          Emit codegen data into the object file. LLD for MachO (currently) merges them into the specified <path>.
  -fcodegen-data-generate Emit codegen data into the object file. LLD for MachO (currently) merges them into default.cgdata.
  -fcodegen-data-use=<path>
                          Use codegen data read from the specified <path>.
  -fcodegen-data-use      Use codegen data read from default.cgdata to optimize the binary
  -fcolor-diagnostics     Enable colors in diagnostics
  -fcomment-block-commands=<arg>
                          Treat each comma separated argument in <arg> as a documentation comment block command
  -fcommon                Place uninitialized global variables in a common block
  -fcomplete-member-pointers
                          Require member pointer base types to be complete if they would be significant under the Microsoft ABI
  -fcomplex-arithmetic=<value>
                          Controls the calculation methods of complex number multiplication and division.
  -fconstexpr-backtrace-limit=<value>
                          Set the maximum number of entries to print in a constexpr evaluation backtrace (0 = no limit)
  -fconstexpr-depth=<value>
                          Set the maximum depth of recursive constexpr function calls
  -fconstexpr-steps=<value>
                          Set the maximum number of steps in constexpr function evaluation
  -fconvergent-functions  Assume all functions may be convergent.
  -fcoro-aligned-allocation
                          Prefer aligned allocation for C++ Coroutines
  -fcoroutines            Enable support for the C++ Coroutines
  -fcoverage-compilation-dir=<value>
                          The compilation directory to embed in the coverage mapping.
  -fcoverage-mapping      Generate coverage mapping to enable code coverage analysis
  -fcoverage-mcdc         Enable MC/DC criteria when generating code coverage
  -fcoverage-prefix-map=<old>=<new>
                          remap file source paths <old> to <new> in coverage mapping. If there are multiple options, prefix replacement is applied in reverse order starting from the last one
  -fcrash-diagnostics-dir=<dir>
                          Put crash-report files in <dir>
  -fcrash-diagnostics=<value>
                          Set level of crash diagnostic reporting, (option: off, compiler, all)
  -fcrash-diagnostics     Enable crash diagnostic reporting (default)
  -fcs-profile-generate=<directory>
                          Generate instrumented code to collect context sensitive execution counts into <directory>/default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcs-profile-generate   Generate instrumented code to collect context sensitive execution counts into default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcuda-short-ptr        Use 32-bit pointers for accessing const/local/shared address spaces
  -fcx-fortran-rules      Range reduction is enabled for complex arithmetic operations.
  -fcx-limited-range      Basic algebraic expansions of complex arithmetic operations involving are enabled.
  -fcxx-exceptions        Enable C++ exceptions
  -fcxx-modules           Enable modules for C++
  -fdata-sections         Place each data in its own section
  -fdebug-compilation-dir=<value>
                          The compilation directory to embed in the debug info
  -fdebug-default-version=<value>
                          Default DWARF version to use, if a -g option caused DWARF debug info to be produced
  -fdebug-info-for-profiling
                          Emit extra debug info to make sample profile more accurate
  -fdebug-macro           Emit macro debug information
  -fdebug-prefix-map=<old>=<new>
                          For paths in debug info, remap directory <old> to <new>. If multiple options match a path, the last option wins
  -fdebug-ranges-base-address
                          Use DWARF base address selection entries in .debug_ranges
  -fdebug-types-section   Place debug types in their own section (ELF Only)
  -fdeclspec              Allow __declspec as a keyword
  -fdefine-target-os-macros
                          Enable predefined target OS macros
  -fdelayed-template-parsing
                          Parse templated function definitions at the end of the translation unit
  -fdelete-null-pointer-checks
                          Treat usage of null pointers as undefined behavior (default)
  -fdiagnostics-absolute-paths
                          Print absolute paths in diagnostics
  -fdiagnostics-color=<value>
                          When to use colors in diagnostics
  -fdiagnostics-hotness-threshold=<value>
                          Prevent optimization remarks from being output if they do not have at least this profile count. Use 'auto' to apply the threshold from profile summary
  -fdiagnostics-misexpect-tolerance=<value>
                          Prevent misexpect diagnostics from being output if the profile counts are within N% of the expected.
  -fdiagnostics-parseable-fixits
                          Print fix-its in machine parseable form
```

### `afl-clang`

官方给出的调用示例：`afl-clang --help`

```text
root@kali:~# afl-clang --help
OVERVIEW: clang LLVM compiler
USAGE: clang [options] file...
OPTIONS:
  -###                    Print (but do not run) the commands to run for this compilation
  --analyzer-output <value>
                          Static analyzer report output format (html|plist|plist-multi-file|plist-html|sarif|sarif-html|text).
  --analyze               Run the static analyzer
  -B <prefix>             Search $prefix$file for executables, libraries, and data files. If $prefix is a directory, search $prefix/$file
  -b <arg>                Pass -b <arg> to the linker on AIX
  -CC                     Include comments from within macros in preprocessed output
  -cl-denorms-are-zero    OpenCL only. Allow denormals to be flushed to zero.
  -cl-ext=<value>         OpenCL only. Enable or disable OpenCL extensions/optional features. The argument is a comma-separated sequence of one or more extension names, each prefixed by '+' or '-'.
  -cl-fast-relaxed-math   OpenCL only. Sets -cl-finite-math-only and -cl-unsafe-math-optimizations, and defines __FAST_RELAXED_MATH__.
  -cl-finite-math-only    OpenCL only. Allow floating-point optimizations that assume arguments and results are not NaNs or +-Inf.
  -cl-fp32-correctly-rounded-divide-sqrt
                          OpenCL only. Specify that single precision floating-point divide and sqrt used in the program source are correctly rounded.
  -cl-kernel-arg-info     OpenCL only. Generate kernel argument metadata.
  -cl-mad-enable          OpenCL only. Allow use of less precise MAD computations in the generated binary.
  -cl-no-signed-zeros     OpenCL only. Allow use of less precise no signed zeros computations in the generated binary.
  -cl-no-stdinc           OpenCL only. Disables all standard includes containing non-native compiler types and functions.
  -cl-opt-disable         OpenCL only. This option disables all optimizations. By default optimizations are enabled.
  -cl-single-precision-constant
                          OpenCL only. Treat double precision floating-point constant as single precision constant.
  -cl-std=<value>         OpenCL language standard to compile for.
  -cl-strict-aliasing     OpenCL only. This option is added for compatibility with OpenCL 1.0.
  -cl-uniform-work-group-size
                          OpenCL only. Defines that the global work-size be a multiple of the work-group size specified to clEnqueueNDRangeKernel
  -cl-unsafe-math-optimizations
                          OpenCL only. Allow unsafe floating-point optimizations.  Also implies -cl-no-signed-zeros and -cl-mad-enable.
  -clangir-disable-passes Disable CIR transformations pipeline
  -clangir-disable-verifier
                          ClangIR: Disable MLIR module verifier
  --config=<file>         Specify configuration file
  --cuda-compile-host-device
                          Compile CUDA code for both host and device (default). Has no effect on non-CUDA compilations.
  --cuda-device-only      Compile CUDA code for device only
  --cuda-feature=<value>  Manually specify the CUDA feature to use
  --cuda-host-only        Compile CUDA code for host only. Has no effect on non-CUDA compilations.
  --cuda-include-ptx=<value>
                          Include PTX for the following GPU architecture (e.g. sm_35) or 'all'. May be specified more than once.
  --cuda-noopt-device-debug
                          Enable device-side debug info generation. Disables ptxas optimizations.
  --cuda-path-ignore-env  Ignore environment variables to detect CUDA installation
  --cuda-path=<value>     CUDA installation path
  -cuid=<value>           An ID for compilation unit, which should be the same for the same compilation unit but different for different compilation units. It is used to externalize device-side static variables for single source offloading languages CUDA and HIP so that they can be accessed by the host code of the same compilation unit.
  -cxx-isystem <directory>
                          Add directory to the C++ SYSTEM include search path
  -C                      Include comments in preprocessed output
  -c                      Only run preprocess, compile, and assemble steps
  -darwin-target-variant-triple <value>
                          Specify the darwin target variant triple
  -darwin-target-variant <value>
                          Generate code for an additional runtime variant of the deployment target
  -dD                     Print macro definitions in -E mode in addition to normal output
  -dependency-dot <value> Filename to write DOT-formatted header dependencies to
  -dependency-file <value>
                          Filename (or -) to write dependency output to
  -dI                     Print include directives in -E mode in addition to normal output
  -dM                     Print macro definitions in -E mode instead of normal output
  -dsym-dir <dir>         Directory to output dSYM's (if any) to
  -dumpdir <dumppfx>      Use <dumpfpx> as a prefix to form auxiliary and dump file names
  -dumpmachine            Display the compiler's target processor
  -dumpversion            Display the version of the compiler
  -D <macro>=<value>      Define <macro> to <value> (or 1 if <value> omitted)
  --embed-dir=<dir>       Add directory to embed search path
  -emit-ast               Emit Clang AST files for source inputs
  -emit-cir               Build ASTs and then lower to ClangIR
  --emit-extension-symbol-graphs
                          Generate additional symbol graphs for extended modules.
  -emit-interface-stubs   Generate Interface Stub Files.
  -emit-llvm              Use the LLVM representation for assembler and object files
  -emit-merged-ifs        Generate Interface Stub Files, emit merged text not binary.
  --emit-static-lib       Enable linker job to emit a static library.
  -emit-symbol-graph      Generate Extract API information as a side effect of compilation.
  --end-no-unused-arguments
                          Start emitting warnings for unused driver arguments
  --extract-api-ignores=<value>
                          Comma separated list of files containing a new line separated list of API symbols to ignore when extracting API information.
  -extract-api            Extract API information
  -E                      Only run the preprocessor
  -faapcs-bitfield-load   Follows the AAPCS standard that all volatile bit-field write generates at least one load. (ARM only).
  -faapcs-bitfield-width  Follow the AAPCS standard requirement stating that volatile bit-field width is dictated by the field container type. (ARM only).
  -faarch64-jump-table-hardening
                          Use hardened lowering for jump-table dispatch
  -faddrsig               Emit an address-significance table
  -falign-loops=<N>       N must be a power of two. Align loops to the boundary
  -faligned-allocation    Enable C++17 aligned allocation functions
  -fallow-editor-placeholders
                          Treat editor placeholders as valid source code
  -fallow-runtime-check-skip-hot-cutoff=<value>
                          Exclude __builtin_allow_runtime_check for the top hottest code responsible for the given fraction of PGO counters (0.0 [default] = skip none; 1.0 = skip all). Argument format: <value>
  -faltivec-src-compat=<value>
                          Source-level compatibility for Altivec vectors (for PowerPC targets). This includes results of vector comparison (scalar for 'xl', vector for 'gcc') as well as behavior when initializing with a scalar (splatting for 'xl', element zero only for 'gcc'). For 'mixed', the compatibility is as 'gcc' for 'vector bool/vector pixel' and as 'xl' for other types. Current default is 'mixed'.
  -fansi-escape-codes     Use ANSI escape codes for diagnostics
  -fapinotes-modules      Enable module-based external API notes support
  -fapinotes-swift-version=<version>
                          Specify the Swift version to use when filtering API notes
  -fapinotes              Enable external API notes support
  -fapple-kext            Use Apple's kernel extensions ABI
  -fapple-link-rtlib      Force linking the clang builtins runtime library
  -fapple-pragma-pack     Enable Apple gcc-compatible #pragma pack handling
  -fapplication-extension Restrict code to those available for App Extensions
  -fapprox-func           Allow certain math function calls to be replaced with an approximately equivalent calculation
  -fassume-nothrow-exception-dtor
                          Assume that exception objects' destructors are non-throwing
  -fasync-exceptions      Enable EH Asynchronous exceptions
  -fatomic-fine-grained-memory
                          May have atomic operations on fine-grained memory
  -fatomic-ignore-denormal-mode
                          Allow atomic operations to ignore denormal mode
  -fatomic-remote-memory  May have atomic operations on remote memory
  -fauto-import           MinGW specific. Enable code generation support for automatic dllimport, and enable support for it in the linker. Enabled by default.
  -fbasic-block-address-map
                          Emit the basic block address map section.
  -fbasic-block-sections=<value>
                          Place each function's basic blocks in unique sections (ELF Only)
  -fbinutils-version=<major.minor>
                          Produced object files can use all ELF features supported by this binutils version and newer. If -fno-integrated-as is specified, the generated assembly will consider GNU as support. 'none' means that all ELF features can be used, regardless of binutils support. Defaults to 2.26.
  -fblocks                Enable the 'blocks' language feature
  -fborland-extensions    Accept non-standard constructs supported by the Borland compiler
  -fbuild-session-file=<file>
                          Use the last modification time of <file> as the build session timestamp
  -fbuild-session-timestamp=<time since Epoch in seconds>
                          Time when the current build session started
  -fbuiltin-module-map    Load the clang builtins module map file.
  -fc++-abi=<value>       C++ ABI to use. This will override the target C++ ABI.
  -fc++-static-destructors=<value>
                          Controls which variables C++ static destructors are registered for
  -fcall-saved-x10        Make the x10 register call-saved (AArch64 only)
  -fcall-saved-x11        Make the x11 register call-saved (AArch64 only)
  -fcall-saved-x12        Make the x12 register call-saved (AArch64 only)
  -fcall-saved-x13        Make the x13 register call-saved (AArch64 only)
  -fcall-saved-x14        Make the x14 register call-saved (AArch64 only)
  -fcall-saved-x15        Make the x15 register call-saved (AArch64 only)
  -fcall-saved-x18        Make the x18 register call-saved (AArch64 only)
  -fcall-saved-x8         Make the x8 register call-saved (AArch64 only)
  -fcall-saved-x9         Make the x9 register call-saved (AArch64 only)
  -fcaret-diagnostics-max-lines=<value>
                          Set the maximum number of source lines to show in a caret diagnostic (0 = no limit).
  -fcf-protection=<value> Instrument control-flow architecture protection
  -fcf-protection         Enable cf-protection in 'full' mode
  -fchar8_t               Enable C++ builtin type char8_t
  -fcheck-new             Do not assume C++ operator new may not return NULL
  -fclang-abi-compat=<version>
                          Attempt to match the ABI of Clang <version>
  -fclangir               Use the ClangIR pipeline to compile
  -fcodegen-data-generate=<path>
                          Emit codegen data into the object file. LLD for MachO (currently) merges them into the specified <path>.
  -fcodegen-data-generate Emit codegen data into the object file. LLD for MachO (currently) merges them into default.cgdata.
  -fcodegen-data-use=<path>
                          Use codegen data read from the specified <path>.
  -fcodegen-data-use      Use codegen data read from default.cgdata to optimize the binary
  -fcolor-diagnostics     Enable colors in diagnostics
  -fcomment-block-commands=<arg>
                          Treat each comma separated argument in <arg> as a documentation comment block command
  -fcommon                Place uninitialized global variables in a common block
  -fcomplete-member-pointers
                          Require member pointer base types to be complete if they would be significant under the Microsoft ABI
  -fcomplex-arithmetic=<value>
                          Controls the calculation methods of complex number multiplication and division.
  -fconstexpr-backtrace-limit=<value>
                          Set the maximum number of entries to print in a constexpr evaluation backtrace (0 = no limit)
  -fconstexpr-depth=<value>
                          Set the maximum depth of recursive constexpr function calls
  -fconstexpr-steps=<value>
                          Set the maximum number of steps in constexpr function evaluation
  -fconvergent-functions  Assume all functions may be convergent.
  -fcoro-aligned-allocation
                          Prefer aligned allocation for C++ Coroutines
  -fcoroutines            Enable support for the C++ Coroutines
  -fcoverage-compilation-dir=<value>
                          The compilation directory to embed in the coverage mapping.
  -fcoverage-mapping      Generate coverage mapping to enable code coverage analysis
  -fcoverage-mcdc         Enable MC/DC criteria when generating code coverage
  -fcoverage-prefix-map=<old>=<new>
                          remap file source paths <old> to <new> in coverage mapping. If there are multiple options, prefix replacement is applied in reverse order starting from the last one
  -fcrash-diagnostics-dir=<dir>
                          Put crash-report files in <dir>
  -fcrash-diagnostics=<value>
                          Set level of crash diagnostic reporting, (option: off, compiler, all)
  -fcrash-diagnostics     Enable crash diagnostic reporting (default)
  -fcs-profile-generate=<directory>
                          Generate instrumented code to collect context sensitive execution counts into <directory>/default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcs-profile-generate   Generate instrumented code to collect context sensitive execution counts into default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcuda-short-ptr        Use 32-bit pointers for accessing const/local/shared address spaces
  -fcx-fortran-rules      Range reduction is enabled for complex arithmetic operations.
  -fcx-limited-range      Basic algebraic expansions of complex arithmetic operations involving are enabled.
  -fcxx-exceptions        Enable C++ exceptions
  -fcxx-modules           Enable modules for C++
  -fdata-sections         Place each data in its own section
  -fdebug-compilation-dir=<value>
                          The compilation directory to embed in the debug info
  -fdebug-default-version=<value>
                          Default DWARF version to use, if a -g option caused DWARF debug info to be produced
  -fdebug-info-for-profiling
                          Emit extra debug info to make sample profile more accurate
  -fdebug-macro           Emit macro debug information
  -fdebug-prefix-map=<old>=<new>
                          For paths in debug info, remap directory <old> to <new>. If multiple options match a path, the last option wins
  -fdebug-ranges-base-address
                          Use DWARF base address selection entries in .debug_ranges
  -fdebug-types-section   Place debug types in their own section (ELF Only)
  -fdeclspec              Allow __declspec as a keyword
  -fdefine-target-os-macros
                          Enable predefined target OS macros
  -fdelayed-template-parsing
                          Parse templated function definitions at the end of the translation unit
  -fdelete-null-pointer-checks
                          Treat usage of null pointers as undefined behavior (default)
  -fdiagnostics-absolute-paths
                          Print absolute paths in diagnostics
  -fdiagnostics-color=<value>
                          When to use colors in diagnostics
  -fdiagnostics-hotness-threshold=<value>
                          Prevent optimization remarks from being output if they do not have at least this profile count. Use 'auto' to apply the threshold from profile summary
  -fdiagnostics-misexpect-tolerance=<value>
                          Prevent misexpect diagnostics from being output if the profile counts are within N% of the expected.
  -fdiagnostics-parseable-fixits
                          Print fix-its in machine parseable form
```

### `afl-clang++`

官方给出的调用示例：`afl-clang++ --help`

```text
root@kali:~# afl-clang++ --help
OVERVIEW: clang LLVM compiler
USAGE: clang [options] file...
OPTIONS:
  -###                    Print (but do not run) the commands to run for this compilation
  --analyzer-output <value>
                          Static analyzer report output format (html|plist|plist-multi-file|plist-html|sarif|sarif-html|text).
  --analyze               Run the static analyzer
  -B <prefix>             Search $prefix$file for executables, libraries, and data files. If $prefix is a directory, search $prefix/$file
  -b <arg>                Pass -b <arg> to the linker on AIX
  -CC                     Include comments from within macros in preprocessed output
  -cl-denorms-are-zero    OpenCL only. Allow denormals to be flushed to zero.
  -cl-ext=<value>         OpenCL only. Enable or disable OpenCL extensions/optional features. The argument is a comma-separated sequence of one or more extension names, each prefixed by '+' or '-'.
  -cl-fast-relaxed-math   OpenCL only. Sets -cl-finite-math-only and -cl-unsafe-math-optimizations, and defines __FAST_RELAXED_MATH__.
  -cl-finite-math-only    OpenCL only. Allow floating-point optimizations that assume arguments and results are not NaNs or +-Inf.
  -cl-fp32-correctly-rounded-divide-sqrt
                          OpenCL only. Specify that single precision floating-point divide and sqrt used in the program source are correctly rounded.
  -cl-kernel-arg-info     OpenCL only. Generate kernel argument metadata.
  -cl-mad-enable          OpenCL only. Allow use of less precise MAD computations in the generated binary.
  -cl-no-signed-zeros     OpenCL only. Allow use of less precise no signed zeros computations in the generated binary.
  -cl-no-stdinc           OpenCL only. Disables all standard includes containing non-native compiler types and functions.
  -cl-opt-disable         OpenCL only. This option disables all optimizations. By default optimizations are enabled.
  -cl-single-precision-constant
                          OpenCL only. Treat double precision floating-point constant as single precision constant.
  -cl-std=<value>         OpenCL language standard to compile for.
  -cl-strict-aliasing     OpenCL only. This option is added for compatibility with OpenCL 1.0.
  -cl-uniform-work-group-size
                          OpenCL only. Defines that the global work-size be a multiple of the work-group size specified to clEnqueueNDRangeKernel
  -cl-unsafe-math-optimizations
                          OpenCL only. Allow unsafe floating-point optimizations.  Also implies -cl-no-signed-zeros and -cl-mad-enable.
  -clangir-disable-passes Disable CIR transformations pipeline
  -clangir-disable-verifier
                          ClangIR: Disable MLIR module verifier
  --config=<file>         Specify configuration file
  --cuda-compile-host-device
                          Compile CUDA code for both host and device (default). Has no effect on non-CUDA compilations.
  --cuda-device-only      Compile CUDA code for device only
  --cuda-feature=<value>  Manually specify the CUDA feature to use
  --cuda-host-only        Compile CUDA code for host only. Has no effect on non-CUDA compilations.
  --cuda-include-ptx=<value>
                          Include PTX for the following GPU architecture (e.g. sm_35) or 'all'. May be specified more than once.
  --cuda-noopt-device-debug
                          Enable device-side debug info generation. Disables ptxas optimizations.
  --cuda-path-ignore-env  Ignore environment variables to detect CUDA installation
  --cuda-path=<value>     CUDA installation path
  -cuid=<value>           An ID for compilation unit, which should be the same for the same compilation unit but different for different compilation units. It is used to externalize device-side static variables for single source offloading languages CUDA and HIP so that they can be accessed by the host code of the same compilation unit.
  -cxx-isystem <directory>
                          Add directory to the C++ SYSTEM include search path
  -C                      Include comments in preprocessed output
  -c                      Only run preprocess, compile, and assemble steps
  -darwin-target-variant-triple <value>
                          Specify the darwin target variant triple
  -darwin-target-variant <value>
                          Generate code for an additional runtime variant of the deployment target
  -dD                     Print macro definitions in -E mode in addition to normal output
  -dependency-dot <value> Filename to write DOT-formatted header dependencies to
  -dependency-file <value>
                          Filename (or -) to write dependency output to
  -dI                     Print include directives in -E mode in addition to normal output
  -dM                     Print macro definitions in -E mode instead of normal output
  -dsym-dir <dir>         Directory to output dSYM's (if any) to
  -dumpdir <dumppfx>      Use <dumpfpx> as a prefix to form auxiliary and dump file names
  -dumpmachine            Display the compiler's target processor
  -dumpversion            Display the version of the compiler
  -D <macro>=<value>      Define <macro> to <value> (or 1 if <value> omitted)
  --embed-dir=<dir>       Add directory to embed search path
  -emit-ast               Emit Clang AST files for source inputs
  -emit-cir               Build ASTs and then lower to ClangIR
  --emit-extension-symbol-graphs
                          Generate additional symbol graphs for extended modules.
  -emit-interface-stubs   Generate Interface Stub Files.
  -emit-llvm              Use the LLVM representation for assembler and object files
  -emit-merged-ifs        Generate Interface Stub Files, emit merged text not binary.
  --emit-static-lib       Enable linker job to emit a static library.
  -emit-symbol-graph      Generate Extract API information as a side effect of compilation.
  --end-no-unused-arguments
                          Start emitting warnings for unused driver arguments
  --extract-api-ignores=<value>
                          Comma separated list of files containing a new line separated list of API symbols to ignore when extracting API information.
  -extract-api            Extract API information
  -E                      Only run the preprocessor
  -faapcs-bitfield-load   Follows the AAPCS standard that all volatile bit-field write generates at least one load. (ARM only).
  -faapcs-bitfield-width  Follow the AAPCS standard requirement stating that volatile bit-field width is dictated by the field container type. (ARM only).
  -faarch64-jump-table-hardening
                          Use hardened lowering for jump-table dispatch
  -faddrsig               Emit an address-significance table
  -falign-loops=<N>       N must be a power of two. Align loops to the boundary
  -faligned-allocation    Enable C++17 aligned allocation functions
  -fallow-editor-placeholders
                          Treat editor placeholders as valid source code
  -fallow-runtime-check-skip-hot-cutoff=<value>
                          Exclude __builtin_allow_runtime_check for the top hottest code responsible for the given fraction of PGO counters (0.0 [default] = skip none; 1.0 = skip all). Argument format: <value>
  -faltivec-src-compat=<value>
                          Source-level compatibility for Altivec vectors (for PowerPC targets). This includes results of vector comparison (scalar for 'xl', vector for 'gcc') as well as behavior when initializing with a scalar (splatting for 'xl', element zero only for 'gcc'). For 'mixed', the compatibility is as 'gcc' for 'vector bool/vector pixel' and as 'xl' for other types. Current default is 'mixed'.
  -fansi-escape-codes     Use ANSI escape codes for diagnostics
  -fapinotes-modules      Enable module-based external API notes support
  -fapinotes-swift-version=<version>
                          Specify the Swift version to use when filtering API notes
  -fapinotes              Enable external API notes support
  -fapple-kext            Use Apple's kernel extensions ABI
  -fapple-link-rtlib      Force linking the clang builtins runtime library
  -fapple-pragma-pack     Enable Apple gcc-compatible #pragma pack handling
  -fapplication-extension Restrict code to those available for App Extensions
  -fapprox-func           Allow certain math function calls to be replaced with an approximately equivalent calculation
  -fassume-nothrow-exception-dtor
                          Assume that exception objects' destructors are non-throwing
  -fasync-exceptions      Enable EH Asynchronous exceptions
  -fatomic-fine-grained-memory
                          May have atomic operations on fine-grained memory
  -fatomic-ignore-denormal-mode
                          Allow atomic operations to ignore denormal mode
  -fatomic-remote-memory  May have atomic operations on remote memory
  -fauto-import           MinGW specific. Enable code generation support for automatic dllimport, and enable support for it in the linker. Enabled by default.
  -fbasic-block-address-map
                          Emit the basic block address map section.
  -fbasic-block-sections=<value>
                          Place each function's basic blocks in unique sections (ELF Only)
  -fbinutils-version=<major.minor>
                          Produced object files can use all ELF features supported by this binutils version and newer. If -fno-integrated-as is specified, the generated assembly will consider GNU as support. 'none' means that all ELF features can be used, regardless of binutils support. Defaults to 2.26.
  -fblocks                Enable the 'blocks' language feature
  -fborland-extensions    Accept non-standard constructs supported by the Borland compiler
  -fbuild-session-file=<file>
                          Use the last modification time of <file> as the build session timestamp
  -fbuild-session-timestamp=<time since Epoch in seconds>
                          Time when the current build session started
  -fbuiltin-module-map    Load the clang builtins module map file.
  -fc++-abi=<value>       C++ ABI to use. This will override the target C++ ABI.
  -fc++-static-destructors=<value>
                          Controls which variables C++ static destructors are registered for
  -fcall-saved-x10        Make the x10 register call-saved (AArch64 only)
  -fcall-saved-x11        Make the x11 register call-saved (AArch64 only)
  -fcall-saved-x12        Make the x12 register call-saved (AArch64 only)
  -fcall-saved-x13        Make the x13 register call-saved (AArch64 only)
  -fcall-saved-x14        Make the x14 register call-saved (AArch64 only)
  -fcall-saved-x15        Make the x15 register call-saved (AArch64 only)
  -fcall-saved-x18        Make the x18 register call-saved (AArch64 only)
  -fcall-saved-x8         Make the x8 register call-saved (AArch64 only)
  -fcall-saved-x9         Make the x9 register call-saved (AArch64 only)
  -fcaret-diagnostics-max-lines=<value>
                          Set the maximum number of source lines to show in a caret diagnostic (0 = no limit).
  -fcf-protection=<value> Instrument control-flow architecture protection
  -fcf-protection         Enable cf-protection in 'full' mode
  -fchar8_t               Enable C++ builtin type char8_t
  -fcheck-new             Do not assume C++ operator new may not return NULL
  -fclang-abi-compat=<version>
                          Attempt to match the ABI of Clang <version>
  -fclangir               Use the ClangIR pipeline to compile
  -fcodegen-data-generate=<path>
                          Emit codegen data into the object file. LLD for MachO (currently) merges them into the specified <path>.
  -fcodegen-data-generate Emit codegen data into the object file. LLD for MachO (currently) merges them into default.cgdata.
  -fcodegen-data-use=<path>
                          Use codegen data read from the specified <path>.
  -fcodegen-data-use      Use codegen data read from default.cgdata to optimize the binary
  -fcolor-diagnostics     Enable colors in diagnostics
  -fcomment-block-commands=<arg>
                          Treat each comma separated argument in <arg> as a documentation comment block command
  -fcommon                Place uninitialized global variables in a common block
  -fcomplete-member-pointers
                          Require member pointer base types to be complete if they would be significant under the Microsoft ABI
  -fcomplex-arithmetic=<value>
                          Controls the calculation methods of complex number multiplication and division.
  -fconstexpr-backtrace-limit=<value>
                          Set the maximum number of entries to print in a constexpr evaluation backtrace (0 = no limit)
  -fconstexpr-depth=<value>
                          Set the maximum depth of recursive constexpr function calls
  -fconstexpr-steps=<value>
                          Set the maximum number of steps in constexpr function evaluation
  -fconvergent-functions  Assume all functions may be convergent.
  -fcoro-aligned-allocation
                          Prefer aligned allocation for C++ Coroutines
  -fcoroutines            Enable support for the C++ Coroutines
  -fcoverage-compilation-dir=<value>
                          The compilation directory to embed in the coverage mapping.
  -fcoverage-mapping      Generate coverage mapping to enable code coverage analysis
  -fcoverage-mcdc         Enable MC/DC criteria when generating code coverage
  -fcoverage-prefix-map=<old>=<new>
                          remap file source paths <old> to <new> in coverage mapping. If there are multiple options, prefix replacement is applied in reverse order starting from the last one
  -fcrash-diagnostics-dir=<dir>
                          Put crash-report files in <dir>
  -fcrash-diagnostics=<value>
                          Set level of crash diagnostic reporting, (option: off, compiler, all)
  -fcrash-diagnostics     Enable crash diagnostic reporting (default)
  -fcs-profile-generate=<directory>
                          Generate instrumented code to collect context sensitive execution counts into <directory>/default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcs-profile-generate   Generate instrumented code to collect context sensitive execution counts into default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcuda-short-ptr        Use 32-bit pointers for accessing const/local/shared address spaces
  -fcx-fortran-rules      Range reduction is enabled for complex arithmetic operations.
  -fcx-limited-range      Basic algebraic expansions of complex arithmetic operations involving are enabled.
  -fcxx-exceptions        Enable C++ exceptions
  -fcxx-modules           Enable modules for C++
  -fdata-sections         Place each data in its own section
  -fdebug-compilation-dir=<value>
                          The compilation directory to embed in the debug info
  -fdebug-default-version=<value>
                          Default DWARF version to use, if a -g option caused DWARF debug info to be produced
  -fdebug-info-for-profiling
                          Emit extra debug info to make sample profile more accurate
  -fdebug-macro           Emit macro debug information
  -fdebug-prefix-map=<old>=<new>
                          For paths in debug info, remap directory <old> to <new>. If multiple options match a path, the last option wins
  -fdebug-ranges-base-address
                          Use DWARF base address selection entries in .debug_ranges
  -fdebug-types-section   Place debug types in their own section (ELF Only)
  -fdeclspec              Allow __declspec as a keyword
  -fdefine-target-os-macros
                          Enable predefined target OS macros
  -fdelayed-template-parsing
                          Parse templated function definitions at the end of the translation unit
  -fdelete-null-pointer-checks
                          Treat usage of null pointers as undefined behavior (default)
  -fdiagnostics-absolute-paths
                          Print absolute paths in diagnostics
  -fdiagnostics-color=<value>
                          When to use colors in diagnostics
  -fdiagnostics-hotness-threshold=<value>
                          Prevent optimization remarks from being output if they do not have at least this profile count. Use 'auto' to apply the threshold from profile summary
  -fdiagnostics-misexpect-tolerance=<value>
                          Prevent misexpect diagnostics from being output if the profile counts are within N% of the expected.
  -fdiagnostics-parseable-fixits
                          Print fix-its in machine parseable form
```

### `afl-clang-fast`

官方给出的调用示例：`afl-clang-fast --help`

```text
root@kali:~# afl-clang-fast --help
OVERVIEW: clang LLVM compiler
USAGE: clang [options] file...
OPTIONS:
  -###                    Print (but do not run) the commands to run for this compilation
  --analyzer-output <value>
                          Static analyzer report output format (html|plist|plist-multi-file|plist-html|sarif|sarif-html|text).
  --analyze               Run the static analyzer
  -B <prefix>             Search $prefix$file for executables, libraries, and data files. If $prefix is a directory, search $prefix/$file
  -b <arg>                Pass -b <arg> to the linker on AIX
  -CC                     Include comments from within macros in preprocessed output
  -cl-denorms-are-zero    OpenCL only. Allow denormals to be flushed to zero.
  -cl-ext=<value>         OpenCL only. Enable or disable OpenCL extensions/optional features. The argument is a comma-separated sequence of one or more extension names, each prefixed by '+' or '-'.
  -cl-fast-relaxed-math   OpenCL only. Sets -cl-finite-math-only and -cl-unsafe-math-optimizations, and defines __FAST_RELAXED_MATH__.
  -cl-finite-math-only    OpenCL only. Allow floating-point optimizations that assume arguments and results are not NaNs or +-Inf.
  -cl-fp32-correctly-rounded-divide-sqrt
                          OpenCL only. Specify that single precision floating-point divide and sqrt used in the program source are correctly rounded.
  -cl-kernel-arg-info     OpenCL only. Generate kernel argument metadata.
  -cl-mad-enable          OpenCL only. Allow use of less precise MAD computations in the generated binary.
  -cl-no-signed-zeros     OpenCL only. Allow use of less precise no signed zeros computations in the generated binary.
  -cl-no-stdinc           OpenCL only. Disables all standard includes containing non-native compiler types and functions.
  -cl-opt-disable         OpenCL only. This option disables all optimizations. By default optimizations are enabled.
  -cl-single-precision-constant
                          OpenCL only. Treat double precision floating-point constant as single precision constant.
  -cl-std=<value>         OpenCL language standard to compile for.
  -cl-strict-aliasing     OpenCL only. This option is added for compatibility with OpenCL 1.0.
  -cl-uniform-work-group-size
                          OpenCL only. Defines that the global work-size be a multiple of the work-group size specified to clEnqueueNDRangeKernel
  -cl-unsafe-math-optimizations
                          OpenCL only. Allow unsafe floating-point optimizations.  Also implies -cl-no-signed-zeros and -cl-mad-enable.
  -clangir-disable-passes Disable CIR transformations pipeline
  -clangir-disable-verifier
                          ClangIR: Disable MLIR module verifier
  --config=<file>         Specify configuration file
  --cuda-compile-host-device
                          Compile CUDA code for both host and device (default). Has no effect on non-CUDA compilations.
  --cuda-device-only      Compile CUDA code for device only
  --cuda-feature=<value>  Manually specify the CUDA feature to use
  --cuda-host-only        Compile CUDA code for host only. Has no effect on non-CUDA compilations.
  --cuda-include-ptx=<value>
                          Include PTX for the following GPU architecture (e.g. sm_35) or 'all'. May be specified more than once.
  --cuda-noopt-device-debug
                          Enable device-side debug info generation. Disables ptxas optimizations.
  --cuda-path-ignore-env  Ignore environment variables to detect CUDA installation
  --cuda-path=<value>     CUDA installation path
  -cuid=<value>           An ID for compilation unit, which should be the same for the same compilation unit but different for different compilation units. It is used to externalize device-side static variables for single source offloading languages CUDA and HIP so that they can be accessed by the host code of the same compilation unit.
  -cxx-isystem <directory>
                          Add directory to the C++ SYSTEM include search path
  -C                      Include comments in preprocessed output
  -c                      Only run preprocess, compile, and assemble steps
  -darwin-target-variant-triple <value>
                          Specify the darwin target variant triple
  -darwin-target-variant <value>
                          Generate code for an additional runtime variant of the deployment target
  -dD                     Print macro definitions in -E mode in addition to normal output
  -dependency-dot <value> Filename to write DOT-formatted header dependencies to
  -dependency-file <value>
                          Filename (or -) to write dependency output to
  -dI                     Print include directives in -E mode in addition to normal output
  -dM                     Print macro definitions in -E mode instead of normal output
  -dsym-dir <dir>         Directory to output dSYM's (if any) to
  -dumpdir <dumppfx>      Use <dumpfpx> as a prefix to form auxiliary and dump file names
  -dumpmachine            Display the compiler's target processor
  -dumpversion            Display the version of the compiler
  -D <macro>=<value>      Define <macro> to <value> (or 1 if <value> omitted)
  --embed-dir=<dir>       Add directory to embed search path
  -emit-ast               Emit Clang AST files for source inputs
  -emit-cir               Build ASTs and then lower to ClangIR
  --emit-extension-symbol-graphs
                          Generate additional symbol graphs for extended modules.
  -emit-interface-stubs   Generate Interface Stub Files.
  -emit-llvm              Use the LLVM representation for assembler and object files
  -emit-merged-ifs        Generate Interface Stub Files, emit merged text not binary.
  --emit-static-lib       Enable linker job to emit a static library.
  -emit-symbol-graph      Generate Extract API information as a side effect of compilation.
  --end-no-unused-arguments
                          Start emitting warnings for unused driver arguments
  --extract-api-ignores=<value>
                          Comma separated list of files containing a new line separated list of API symbols to ignore when extracting API information.
  -extract-api            Extract API information
  -E                      Only run the preprocessor
  -faapcs-bitfield-load   Follows the AAPCS standard that all volatile bit-field write generates at least one load. (ARM only).
  -faapcs-bitfield-width  Follow the AAPCS standard requirement stating that volatile bit-field width is dictated by the field container type. (ARM only).
  -faarch64-jump-table-hardening
                          Use hardened lowering for jump-table dispatch
  -faddrsig               Emit an address-significance table
  -falign-loops=<N>       N must be a power of two. Align loops to the boundary
  -faligned-allocation    Enable C++17 aligned allocation functions
  -fallow-editor-placeholders
                          Treat editor placeholders as valid source code
  -fallow-runtime-check-skip-hot-cutoff=<value>
                          Exclude __builtin_allow_runtime_check for the top hottest code responsible for the given fraction of PGO counters (0.0 [default] = skip none; 1.0 = skip all). Argument format: <value>
  -faltivec-src-compat=<value>
                          Source-level compatibility for Altivec vectors (for PowerPC targets). This includes results of vector comparison (scalar for 'xl', vector for 'gcc') as well as behavior when initializing with a scalar (splatting for 'xl', element zero only for 'gcc'). For 'mixed', the compatibility is as 'gcc' for 'vector bool/vector pixel' and as 'xl' for other types. Current default is 'mixed'.
  -fansi-escape-codes     Use ANSI escape codes for diagnostics
  -fapinotes-modules      Enable module-based external API notes support
  -fapinotes-swift-version=<version>
                          Specify the Swift version to use when filtering API notes
  -fapinotes              Enable external API notes support
  -fapple-kext            Use Apple's kernel extensions ABI
  -fapple-link-rtlib      Force linking the clang builtins runtime library
  -fapple-pragma-pack     Enable Apple gcc-compatible #pragma pack handling
  -fapplication-extension Restrict code to those available for App Extensions
  -fapprox-func           Allow certain math function calls to be replaced with an approximately equivalent calculation
  -fassume-nothrow-exception-dtor
                          Assume that exception objects' destructors are non-throwing
  -fasync-exceptions      Enable EH Asynchronous exceptions
  -fatomic-fine-grained-memory
                          May have atomic operations on fine-grained memory
  -fatomic-ignore-denormal-mode
                          Allow atomic operations to ignore denormal mode
  -fatomic-remote-memory  May have atomic operations on remote memory
  -fauto-import           MinGW specific. Enable code generation support for automatic dllimport, and enable support for it in the linker. Enabled by default.
  -fbasic-block-address-map
                          Emit the basic block address map section.
  -fbasic-block-sections=<value>
                          Place each function's basic blocks in unique sections (ELF Only)
  -fbinutils-version=<major.minor>
                          Produced object files can use all ELF features supported by this binutils version and newer. If -fno-integrated-as is specified, the generated assembly will consider GNU as support. 'none' means that all ELF features can be used, regardless of binutils support. Defaults to 2.26.
  -fblocks                Enable the 'blocks' language feature
  -fborland-extensions    Accept non-standard constructs supported by the Borland compiler
  -fbuild-session-file=<file>
                          Use the last modification time of <file> as the build session timestamp
  -fbuild-session-timestamp=<time since Epoch in seconds>
                          Time when the current build session started
  -fbuiltin-module-map    Load the clang builtins module map file.
  -fc++-abi=<value>       C++ ABI to use. This will override the target C++ ABI.
  -fc++-static-destructors=<value>
                          Controls which variables C++ static destructors are registered for
  -fcall-saved-x10        Make the x10 register call-saved (AArch64 only)
  -fcall-saved-x11        Make the x11 register call-saved (AArch64 only)
  -fcall-saved-x12        Make the x12 register call-saved (AArch64 only)
  -fcall-saved-x13        Make the x13 register call-saved (AArch64 only)
  -fcall-saved-x14        Make the x14 register call-saved (AArch64 only)
  -fcall-saved-x15        Make the x15 register call-saved (AArch64 only)
  -fcall-saved-x18        Make the x18 register call-saved (AArch64 only)
  -fcall-saved-x8         Make the x8 register call-saved (AArch64 only)
  -fcall-saved-x9         Make the x9 register call-saved (AArch64 only)
  -fcaret-diagnostics-max-lines=<value>
                          Set the maximum number of source lines to show in a caret diagnostic (0 = no limit).
  -fcf-protection=<value> Instrument control-flow architecture protection
  -fcf-protection         Enable cf-protection in 'full' mode
  -fchar8_t               Enable C++ builtin type char8_t
  -fcheck-new             Do not assume C++ operator new may not return NULL
  -fclang-abi-compat=<version>
                          Attempt to match the ABI of Clang <version>
  -fclangir               Use the ClangIR pipeline to compile
  -fcodegen-data-generate=<path>
                          Emit codegen data into the object file. LLD for MachO (currently) merges them into the specified <path>.
  -fcodegen-data-generate Emit codegen data into the object file. LLD for MachO (currently) merges them into default.cgdata.
  -fcodegen-data-use=<path>
                          Use codegen data read from the specified <path>.
  -fcodegen-data-use      Use codegen data read from default.cgdata to optimize the binary
  -fcolor-diagnostics     Enable colors in diagnostics
  -fcomment-block-commands=<arg>
                          Treat each comma separated argument in <arg> as a documentation comment block command
  -fcommon                Place uninitialized global variables in a common block
  -fcomplete-member-pointers
                          Require member pointer base types to be complete if they would be significant under the Microsoft ABI
  -fcomplex-arithmetic=<value>
                          Controls the calculation methods of complex number multiplication and division.
  -fconstexpr-backtrace-limit=<value>
                          Set the maximum number of entries to print in a constexpr evaluation backtrace (0 = no limit)
  -fconstexpr-depth=<value>
                          Set the maximum depth of recursive constexpr function calls
  -fconstexpr-steps=<value>
                          Set the maximum number of steps in constexpr function evaluation
  -fconvergent-functions  Assume all functions may be convergent.
  -fcoro-aligned-allocation
                          Prefer aligned allocation for C++ Coroutines
  -fcoroutines            Enable support for the C++ Coroutines
  -fcoverage-compilation-dir=<value>
                          The compilation directory to embed in the coverage mapping.
  -fcoverage-mapping      Generate coverage mapping to enable code coverage analysis
  -fcoverage-mcdc         Enable MC/DC criteria when generating code coverage
  -fcoverage-prefix-map=<old>=<new>
                          remap file source paths <old> to <new> in coverage mapping. If there are multiple options, prefix replacement is applied in reverse order starting from the last one
  -fcrash-diagnostics-dir=<dir>
                          Put crash-report files in <dir>
  -fcrash-diagnostics=<value>
                          Set level of crash diagnostic reporting, (option: off, compiler, all)
  -fcrash-diagnostics     Enable crash diagnostic reporting (default)
  -fcs-profile-generate=<directory>
                          Generate instrumented code to collect context sensitive execution counts into <directory>/default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcs-profile-generate   Generate instrumented code to collect context sensitive execution counts into default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcuda-short-ptr        Use 32-bit pointers for accessing const/local/shared address spaces
  -fcx-fortran-rules      Range reduction is enabled for complex arithmetic operations.
  -fcx-limited-range      Basic algebraic expansions of complex arithmetic operations involving are enabled.
  -fcxx-exceptions        Enable C++ exceptions
  -fcxx-modules           Enable modules for C++
  -fdata-sections         Place each data in its own section
  -fdebug-compilation-dir=<value>
                          The compilation directory to embed in the debug info
  -fdebug-default-version=<value>
                          Default DWARF version to use, if a -g option caused DWARF debug info to be produced
  -fdebug-info-for-profiling
                          Emit extra debug info to make sample profile more accurate
  -fdebug-macro           Emit macro debug information
  -fdebug-prefix-map=<old>=<new>
                          For paths in debug info, remap directory <old> to <new>. If multiple options match a path, the last option wins
  -fdebug-ranges-base-address
                          Use DWARF base address selection entries in .debug_ranges
  -fdebug-types-section   Place debug types in their own section (ELF Only)
  -fdeclspec              Allow __declspec as a keyword
  -fdefine-target-os-macros
                          Enable predefined target OS macros
  -fdelayed-template-parsing
                          Parse templated function definitions at the end of the translation unit
  -fdelete-null-pointer-checks
                          Treat usage of null pointers as undefined behavior (default)
  -fdiagnostics-absolute-paths
                          Print absolute paths in diagnostics
  -fdiagnostics-color=<value>
                          When to use colors in diagnostics
  -fdiagnostics-hotness-threshold=<value>
                          Prevent optimization remarks from being output if they do not have at least this profile count. Use 'auto' to apply the threshold from profile summary
  -fdiagnostics-misexpect-tolerance=<value>
                          Prevent misexpect diagnostics from being output if the profile counts are within N% of the expected.
  -fdiagnostics-parseable-fixits
                          Print fix-its in machine parseable form
```

### `afl-clang-fast++`

官方给出的调用示例：`afl-clang-fast++ --help`

```text
root@kali:~# afl-clang-fast++ --help
OVERVIEW: clang LLVM compiler
USAGE: clang [options] file...
OPTIONS:
  -###                    Print (but do not run) the commands to run for this compilation
  --analyzer-output <value>
                          Static analyzer report output format (html|plist|plist-multi-file|plist-html|sarif|sarif-html|text).
  --analyze               Run the static analyzer
  -B <prefix>             Search $prefix$file for executables, libraries, and data files. If $prefix is a directory, search $prefix/$file
  -b <arg>                Pass -b <arg> to the linker on AIX
  -CC                     Include comments from within macros in preprocessed output
  -cl-denorms-are-zero    OpenCL only. Allow denormals to be flushed to zero.
  -cl-ext=<value>         OpenCL only. Enable or disable OpenCL extensions/optional features. The argument is a comma-separated sequence of one or more extension names, each prefixed by '+' or '-'.
  -cl-fast-relaxed-math   OpenCL only. Sets -cl-finite-math-only and -cl-unsafe-math-optimizations, and defines __FAST_RELAXED_MATH__.
  -cl-finite-math-only    OpenCL only. Allow floating-point optimizations that assume arguments and results are not NaNs or +-Inf.
  -cl-fp32-correctly-rounded-divide-sqrt
                          OpenCL only. Specify that single precision floating-point divide and sqrt used in the program source are correctly rounded.
  -cl-kernel-arg-info     OpenCL only. Generate kernel argument metadata.
  -cl-mad-enable          OpenCL only. Allow use of less precise MAD computations in the generated binary.
  -cl-no-signed-zeros     OpenCL only. Allow use of less precise no signed zeros computations in the generated binary.
  -cl-no-stdinc           OpenCL only. Disables all standard includes containing non-native compiler types and functions.
  -cl-opt-disable         OpenCL only. This option disables all optimizations. By default optimizations are enabled.
  -cl-single-precision-constant
                          OpenCL only. Treat double precision floating-point constant as single precision constant.
  -cl-std=<value>         OpenCL language standard to compile for.
  -cl-strict-aliasing     OpenCL only. This option is added for compatibility with OpenCL 1.0.
  -cl-uniform-work-group-size
                          OpenCL only. Defines that the global work-size be a multiple of the work-group size specified to clEnqueueNDRangeKernel
  -cl-unsafe-math-optimizations
                          OpenCL only. Allow unsafe floating-point optimizations.  Also implies -cl-no-signed-zeros and -cl-mad-enable.
  -clangir-disable-passes Disable CIR transformations pipeline
  -clangir-disable-verifier
                          ClangIR: Disable MLIR module verifier
  --config=<file>         Specify configuration file
  --cuda-compile-host-device
                          Compile CUDA code for both host and device (default). Has no effect on non-CUDA compilations.
  --cuda-device-only      Compile CUDA code for device only
  --cuda-feature=<value>  Manually specify the CUDA feature to use
  --cuda-host-only        Compile CUDA code for host only. Has no effect on non-CUDA compilations.
  --cuda-include-ptx=<value>
                          Include PTX for the following GPU architecture (e.g. sm_35) or 'all'. May be specified more than once.
  --cuda-noopt-device-debug
                          Enable device-side debug info generation. Disables ptxas optimizations.
  --cuda-path-ignore-env  Ignore environment variables to detect CUDA installation
  --cuda-path=<value>     CUDA installation path
  -cuid=<value>           An ID for compilation unit, which should be the same for the same compilation unit but different for different compilation units. It is used to externalize device-side static variables for single source offloading languages CUDA and HIP so that they can be accessed by the host code of the same compilation unit.
  -cxx-isystem <directory>
                          Add directory to the C++ SYSTEM include search path
  -C                      Include comments in preprocessed output
  -c                      Only run preprocess, compile, and assemble steps
  -darwin-target-variant-triple <value>
                          Specify the darwin target variant triple
  -darwin-target-variant <value>
                          Generate code for an additional runtime variant of the deployment target
  -dD                     Print macro definitions in -E mode in addition to normal output
  -dependency-dot <value> Filename to write DOT-formatted header dependencies to
  -dependency-file <value>
                          Filename (or -) to write dependency output to
  -dI                     Print include directives in -E mode in addition to normal output
  -dM                     Print macro definitions in -E mode instead of normal output
  -dsym-dir <dir>         Directory to output dSYM's (if any) to
  -dumpdir <dumppfx>      Use <dumpfpx> as a prefix to form auxiliary and dump file names
  -dumpmachine            Display the compiler's target processor
  -dumpversion            Display the version of the compiler
  -D <macro>=<value>      Define <macro> to <value> (or 1 if <value> omitted)
  --embed-dir=<dir>       Add directory to embed search path
  -emit-ast               Emit Clang AST files for source inputs
  -emit-cir               Build ASTs and then lower to ClangIR
  --emit-extension-symbol-graphs
                          Generate additional symbol graphs for extended modules.
  -emit-interface-stubs   Generate Interface Stub Files.
  -emit-llvm              Use the LLVM representation for assembler and object files
  -emit-merged-ifs        Generate Interface Stub Files, emit merged text not binary.
  --emit-static-lib       Enable linker job to emit a static library.
  -emit-symbol-graph      Generate Extract API information as a side effect of compilation.
  --end-no-unused-arguments
                          Start emitting warnings for unused driver arguments
  --extract-api-ignores=<value>
                          Comma separated list of files containing a new line separated list of API symbols to ignore when extracting API information.
  -extract-api            Extract API information
  -E                      Only run the preprocessor
  -faapcs-bitfield-load   Follows the AAPCS standard that all volatile bit-field write generates at least one load. (ARM only).
  -faapcs-bitfield-width  Follow the AAPCS standard requirement stating that volatile bit-field width is dictated by the field container type. (ARM only).
  -faarch64-jump-table-hardening
                          Use hardened lowering for jump-table dispatch
  -faddrsig               Emit an address-significance table
  -falign-loops=<N>       N must be a power of two. Align loops to the boundary
  -faligned-allocation    Enable C++17 aligned allocation functions
  -fallow-editor-placeholders
                          Treat editor placeholders as valid source code
  -fallow-runtime-check-skip-hot-cutoff=<value>
                          Exclude __builtin_allow_runtime_check for the top hottest code responsible for the given fraction of PGO counters (0.0 [default] = skip none; 1.0 = skip all). Argument format: <value>
  -faltivec-src-compat=<value>
                          Source-level compatibility for Altivec vectors (for PowerPC targets). This includes results of vector comparison (scalar for 'xl', vector for 'gcc') as well as behavior when initializing with a scalar (splatting for 'xl', element zero only for 'gcc'). For 'mixed', the compatibility is as 'gcc' for 'vector bool/vector pixel' and as 'xl' for other types. Current default is 'mixed'.
  -fansi-escape-codes     Use ANSI escape codes for diagnostics
  -fapinotes-modules      Enable module-based external API notes support
  -fapinotes-swift-version=<version>
                          Specify the Swift version to use when filtering API notes
  -fapinotes              Enable external API notes support
  -fapple-kext            Use Apple's kernel extensions ABI
  -fapple-link-rtlib      Force linking the clang builtins runtime library
  -fapple-pragma-pack     Enable Apple gcc-compatible #pragma pack handling
  -fapplication-extension Restrict code to those available for App Extensions
  -fapprox-func           Allow certain math function calls to be replaced with an approximately equivalent calculation
  -fassume-nothrow-exception-dtor
                          Assume that exception objects' destructors are non-throwing
  -fasync-exceptions      Enable EH Asynchronous exceptions
  -fatomic-fine-grained-memory
                          May have atomic operations on fine-grained memory
  -fatomic-ignore-denormal-mode
                          Allow atomic operations to ignore denormal mode
  -fatomic-remote-memory  May have atomic operations on remote memory
  -fauto-import           MinGW specific. Enable code generation support for automatic dllimport, and enable support for it in the linker. Enabled by default.
  -fbasic-block-address-map
                          Emit the basic block address map section.
  -fbasic-block-sections=<value>
                          Place each function's basic blocks in unique sections (ELF Only)
  -fbinutils-version=<major.minor>
                          Produced object files can use all ELF features supported by this binutils version and newer. If -fno-integrated-as is specified, the generated assembly will consider GNU as support. 'none' means that all ELF features can be used, regardless of binutils support. Defaults to 2.26.
  -fblocks                Enable the 'blocks' language feature
  -fborland-extensions    Accept non-standard constructs supported by the Borland compiler
  -fbuild-session-file=<file>
                          Use the last modification time of <file> as the build session timestamp
  -fbuild-session-timestamp=<time since Epoch in seconds>
                          Time when the current build session started
  -fbuiltin-module-map    Load the clang builtins module map file.
  -fc++-abi=<value>       C++ ABI to use. This will override the target C++ ABI.
  -fc++-static-destructors=<value>
                          Controls which variables C++ static destructors are registered for
  -fcall-saved-x10        Make the x10 register call-saved (AArch64 only)
  -fcall-saved-x11        Make the x11 register call-saved (AArch64 only)
  -fcall-saved-x12        Make the x12 register call-saved (AArch64 only)
  -fcall-saved-x13        Make the x13 register call-saved (AArch64 only)
  -fcall-saved-x14        Make the x14 register call-saved (AArch64 only)
  -fcall-saved-x15        Make the x15 register call-saved (AArch64 only)
  -fcall-saved-x18        Make the x18 register call-saved (AArch64 only)
  -fcall-saved-x8         Make the x8 register call-saved (AArch64 only)
  -fcall-saved-x9         Make the x9 register call-saved (AArch64 only)
  -fcaret-diagnostics-max-lines=<value>
                          Set the maximum number of source lines to show in a caret diagnostic (0 = no limit).
  -fcf-protection=<value> Instrument control-flow architecture protection
  -fcf-protection         Enable cf-protection in 'full' mode
  -fchar8_t               Enable C++ builtin type char8_t
  -fcheck-new             Do not assume C++ operator new may not return NULL
  -fclang-abi-compat=<version>
                          Attempt to match the ABI of Clang <version>
  -fclangir               Use the ClangIR pipeline to compile
  -fcodegen-data-generate=<path>
                          Emit codegen data into the object file. LLD for MachO (currently) merges them into the specified <path>.
  -fcodegen-data-generate Emit codegen data into the object file. LLD for MachO (currently) merges them into default.cgdata.
  -fcodegen-data-use=<path>
                          Use codegen data read from the specified <path>.
  -fcodegen-data-use      Use codegen data read from default.cgdata to optimize the binary
  -fcolor-diagnostics     Enable colors in diagnostics
  -fcomment-block-commands=<arg>
                          Treat each comma separated argument in <arg> as a documentation comment block command
  -fcommon                Place uninitialized global variables in a common block
  -fcomplete-member-pointers
                          Require member pointer base types to be complete if they would be significant under the Microsoft ABI
  -fcomplex-arithmetic=<value>
                          Controls the calculation methods of complex number multiplication and division.
  -fconstexpr-backtrace-limit=<value>
                          Set the maximum number of entries to print in a constexpr evaluation backtrace (0 = no limit)
  -fconstexpr-depth=<value>
                          Set the maximum depth of recursive constexpr function calls
  -fconstexpr-steps=<value>
                          Set the maximum number of steps in constexpr function evaluation
  -fconvergent-functions  Assume all functions may be convergent.
  -fcoro-aligned-allocation
                          Prefer aligned allocation for C++ Coroutines
  -fcoroutines            Enable support for the C++ Coroutines
  -fcoverage-compilation-dir=<value>
                          The compilation directory to embed in the coverage mapping.
  -fcoverage-mapping      Generate coverage mapping to enable code coverage analysis
  -fcoverage-mcdc         Enable MC/DC criteria when generating code coverage
  -fcoverage-prefix-map=<old>=<new>
                          remap file source paths <old> to <new> in coverage mapping. If there are multiple options, prefix replacement is applied in reverse order starting from the last one
  -fcrash-diagnostics-dir=<dir>
                          Put crash-report files in <dir>
  -fcrash-diagnostics=<value>
                          Set level of crash diagnostic reporting, (option: off, compiler, all)
  -fcrash-diagnostics     Enable crash diagnostic reporting (default)
  -fcs-profile-generate=<directory>
                          Generate instrumented code to collect context sensitive execution counts into <directory>/default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcs-profile-generate   Generate instrumented code to collect context sensitive execution counts into default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcuda-short-ptr        Use 32-bit pointers for accessing const/local/shared address spaces
  -fcx-fortran-rules      Range reduction is enabled for complex arithmetic operations.
  -fcx-limited-range      Basic algebraic expansions of complex arithmetic operations involving are enabled.
  -fcxx-exceptions        Enable C++ exceptions
  -fcxx-modules           Enable modules for C++
  -fdata-sections         Place each data in its own section
  -fdebug-compilation-dir=<value>
                          The compilation directory to embed in the debug info
  -fdebug-default-version=<value>
                          Default DWARF version to use, if a -g option caused DWARF debug info to be produced
  -fdebug-info-for-profiling
                          Emit extra debug info to make sample profile more accurate
  -fdebug-macro           Emit macro debug information
  -fdebug-prefix-map=<old>=<new>
                          For paths in debug info, remap directory <old> to <new>. If multiple options match a path, the last option wins
  -fdebug-ranges-base-address
                          Use DWARF base address selection entries in .debug_ranges
  -fdebug-types-section   Place debug types in their own section (ELF Only)
  -fdeclspec              Allow __declspec as a keyword
  -fdefine-target-os-macros
                          Enable predefined target OS macros
  -fdelayed-template-parsing
                          Parse templated function definitions at the end of the translation unit
  -fdelete-null-pointer-checks
                          Treat usage of null pointers as undefined behavior (default)
  -fdiagnostics-absolute-paths
                          Print absolute paths in diagnostics
  -fdiagnostics-color=<value>
                          When to use colors in diagnostics
  -fdiagnostics-hotness-threshold=<value>
                          Prevent optimization remarks from being output if they do not have at least this profile count. Use 'auto' to apply the threshold from profile summary
  -fdiagnostics-misexpect-tolerance=<value>
                          Prevent misexpect diagnostics from being output if the profile counts are within N% of the expected.
  -fdiagnostics-parseable-fixits
                          Print fix-its in machine parseable form
```

### `afl-clang-lto`

官方给出的调用示例：`afl-clang-lto --help`

```text
root@kali:~# afl-clang-lto --help
OVERVIEW: clang LLVM compiler
USAGE: clang [options] file...
OPTIONS:
  -###                    Print (but do not run) the commands to run for this compilation
  --analyzer-output <value>
                          Static analyzer report output format (html|plist|plist-multi-file|plist-html|sarif|sarif-html|text).
  --analyze               Run the static analyzer
  -B <prefix>             Search $prefix$file for executables, libraries, and data files. If $prefix is a directory, search $prefix/$file
  -b <arg>                Pass -b <arg> to the linker on AIX
  -CC                     Include comments from within macros in preprocessed output
  -cl-denorms-are-zero    OpenCL only. Allow denormals to be flushed to zero.
  -cl-ext=<value>         OpenCL only. Enable or disable OpenCL extensions/optional features. The argument is a comma-separated sequence of one or more extension names, each prefixed by '+' or '-'.
  -cl-fast-relaxed-math   OpenCL only. Sets -cl-finite-math-only and -cl-unsafe-math-optimizations, and defines __FAST_RELAXED_MATH__.
  -cl-finite-math-only    OpenCL only. Allow floating-point optimizations that assume arguments and results are not NaNs or +-Inf.
  -cl-fp32-correctly-rounded-divide-sqrt
                          OpenCL only. Specify that single precision floating-point divide and sqrt used in the program source are correctly rounded.
  -cl-kernel-arg-info     OpenCL only. Generate kernel argument metadata.
  -cl-mad-enable          OpenCL only. Allow use of less precise MAD computations in the generated binary.
  -cl-no-signed-zeros     OpenCL only. Allow use of less precise no signed zeros computations in the generated binary.
  -cl-no-stdinc           OpenCL only. Disables all standard includes containing non-native compiler types and functions.
  -cl-opt-disable         OpenCL only. This option disables all optimizations. By default optimizations are enabled.
  -cl-single-precision-constant
                          OpenCL only. Treat double precision floating-point constant as single precision constant.
  -cl-std=<value>         OpenCL language standard to compile for.
  -cl-strict-aliasing     OpenCL only. This option is added for compatibility with OpenCL 1.0.
  -cl-uniform-work-group-size
                          OpenCL only. Defines that the global work-size be a multiple of the work-group size specified to clEnqueueNDRangeKernel
  -cl-unsafe-math-optimizations
                          OpenCL only. Allow unsafe floating-point optimizations.  Also implies -cl-no-signed-zeros and -cl-mad-enable.
  -clangir-disable-passes Disable CIR transformations pipeline
  -clangir-disable-verifier
                          ClangIR: Disable MLIR module verifier
  --config=<file>         Specify configuration file
  --cuda-compile-host-device
                          Compile CUDA code for both host and device (default). Has no effect on non-CUDA compilations.
  --cuda-device-only      Compile CUDA code for device only
  --cuda-feature=<value>  Manually specify the CUDA feature to use
  --cuda-host-only        Compile CUDA code for host only. Has no effect on non-CUDA compilations.
  --cuda-include-ptx=<value>
                          Include PTX for the following GPU architecture (e.g. sm_35) or 'all'. May be specified more than once.
  --cuda-noopt-device-debug
                          Enable device-side debug info generation. Disables ptxas optimizations.
  --cuda-path-ignore-env  Ignore environment variables to detect CUDA installation
  --cuda-path=<value>     CUDA installation path
  -cuid=<value>           An ID for compilation unit, which should be the same for the same compilation unit but different for different compilation units. It is used to externalize device-side static variables for single source offloading languages CUDA and HIP so that they can be accessed by the host code of the same compilation unit.
  -cxx-isystem <directory>
                          Add directory to the C++ SYSTEM include search path
  -C                      Include comments in preprocessed output
  -c                      Only run preprocess, compile, and assemble steps
  -darwin-target-variant-triple <value>
                          Specify the darwin target variant triple
  -darwin-target-variant <value>
                          Generate code for an additional runtime variant of the deployment target
  -dD                     Print macro definitions in -E mode in addition to normal output
  -dependency-dot <value> Filename to write DOT-formatted header dependencies to
  -dependency-file <value>
                          Filename (or -) to write dependency output to
  -dI                     Print include directives in -E mode in addition to normal output
  -dM                     Print macro definitions in -E mode instead of normal output
  -dsym-dir <dir>         Directory to output dSYM's (if any) to
  -dumpdir <dumppfx>      Use <dumpfpx> as a prefix to form auxiliary and dump file names
  -dumpmachine            Display the compiler's target processor
  -dumpversion            Display the version of the compiler
  -D <macro>=<value>      Define <macro> to <value> (or 1 if <value> omitted)
  --embed-dir=<dir>       Add directory to embed search path
  -emit-ast               Emit Clang AST files for source inputs
  -emit-cir               Build ASTs and then lower to ClangIR
  --emit-extension-symbol-graphs
                          Generate additional symbol graphs for extended modules.
  -emit-interface-stubs   Generate Interface Stub Files.
  -emit-llvm              Use the LLVM representation for assembler and object files
  -emit-merged-ifs        Generate Interface Stub Files, emit merged text not binary.
  --emit-static-lib       Enable linker job to emit a static library.
  -emit-symbol-graph      Generate Extract API information as a side effect of compilation.
  --end-no-unused-arguments
                          Start emitting warnings for unused driver arguments
  --extract-api-ignores=<value>
                          Comma separated list of files containing a new line separated list of API symbols to ignore when extracting API information.
  -extract-api            Extract API information
  -E                      Only run the preprocessor
  -faapcs-bitfield-load   Follows the AAPCS standard that all volatile bit-field write generates at least one load. (ARM only).
  -faapcs-bitfield-width  Follow the AAPCS standard requirement stating that volatile bit-field width is dictated by the field container type. (ARM only).
  -faarch64-jump-table-hardening
                          Use hardened lowering for jump-table dispatch
  -faddrsig               Emit an address-significance table
  -falign-loops=<N>       N must be a power of two. Align loops to the boundary
  -faligned-allocation    Enable C++17 aligned allocation functions
  -fallow-editor-placeholders
                          Treat editor placeholders as valid source code
  -fallow-runtime-check-skip-hot-cutoff=<value>
                          Exclude __builtin_allow_runtime_check for the top hottest code responsible for the given fraction of PGO counters (0.0 [default] = skip none; 1.0 = skip all). Argument format: <value>
  -faltivec-src-compat=<value>
                          Source-level compatibility for Altivec vectors (for PowerPC targets). This includes results of vector comparison (scalar for 'xl', vector for 'gcc') as well as behavior when initializing with a scalar (splatting for 'xl', element zero only for 'gcc'). For 'mixed', the compatibility is as 'gcc' for 'vector bool/vector pixel' and as 'xl' for other types. Current default is 'mixed'.
  -fansi-escape-codes     Use ANSI escape codes for diagnostics
  -fapinotes-modules      Enable module-based external API notes support
  -fapinotes-swift-version=<version>
                          Specify the Swift version to use when filtering API notes
  -fapinotes              Enable external API notes support
  -fapple-kext            Use Apple's kernel extensions ABI
  -fapple-link-rtlib      Force linking the clang builtins runtime library
  -fapple-pragma-pack     Enable Apple gcc-compatible #pragma pack handling
  -fapplication-extension Restrict code to those available for App Extensions
  -fapprox-func           Allow certain math function calls to be replaced with an approximately equivalent calculation
  -fassume-nothrow-exception-dtor
                          Assume that exception objects' destructors are non-throwing
  -fasync-exceptions      Enable EH Asynchronous exceptions
  -fatomic-fine-grained-memory
                          May have atomic operations on fine-grained memory
  -fatomic-ignore-denormal-mode
                          Allow atomic operations to ignore denormal mode
  -fatomic-remote-memory  May have atomic operations on remote memory
  -fauto-import           MinGW specific. Enable code generation support for automatic dllimport, and enable support for it in the linker. Enabled by default.
  -fbasic-block-address-map
                          Emit the basic block address map section.
  -fbasic-block-sections=<value>
                          Place each function's basic blocks in unique sections (ELF Only)
  -fbinutils-version=<major.minor>
                          Produced object files can use all ELF features supported by this binutils version and newer. If -fno-integrated-as is specified, the generated assembly will consider GNU as support. 'none' means that all ELF features can be used, regardless of binutils support. Defaults to 2.26.
  -fblocks                Enable the 'blocks' language feature
  -fborland-extensions    Accept non-standard constructs supported by the Borland compiler
  -fbuild-session-file=<file>
                          Use the last modification time of <file> as the build session timestamp
  -fbuild-session-timestamp=<time since Epoch in seconds>
                          Time when the current build session started
  -fbuiltin-module-map    Load the clang builtins module map file.
  -fc++-abi=<value>       C++ ABI to use. This will override the target C++ ABI.
  -fc++-static-destructors=<value>
                          Controls which variables C++ static destructors are registered for
  -fcall-saved-x10        Make the x10 register call-saved (AArch64 only)
  -fcall-saved-x11        Make the x11 register call-saved (AArch64 only)
  -fcall-saved-x12        Make the x12 register call-saved (AArch64 only)
  -fcall-saved-x13        Make the x13 register call-saved (AArch64 only)
  -fcall-saved-x14        Make the x14 register call-saved (AArch64 only)
  -fcall-saved-x15        Make the x15 register call-saved (AArch64 only)
  -fcall-saved-x18        Make the x18 register call-saved (AArch64 only)
  -fcall-saved-x8         Make the x8 register call-saved (AArch64 only)
  -fcall-saved-x9         Make the x9 register call-saved (AArch64 only)
  -fcaret-diagnostics-max-lines=<value>
                          Set the maximum number of source lines to show in a caret diagnostic (0 = no limit).
  -fcf-protection=<value> Instrument control-flow architecture protection
  -fcf-protection         Enable cf-protection in 'full' mode
  -fchar8_t               Enable C++ builtin type char8_t
  -fcheck-new             Do not assume C++ operator new may not return NULL
  -fclang-abi-compat=<version>
                          Attempt to match the ABI of Clang <version>
  -fclangir               Use the ClangIR pipeline to compile
  -fcodegen-data-generate=<path>
                          Emit codegen data into the object file. LLD for MachO (currently) merges them into the specified <path>.
  -fcodegen-data-generate Emit codegen data into the object file. LLD for MachO (currently) merges them into default.cgdata.
  -fcodegen-data-use=<path>
                          Use codegen data read from the specified <path>.
  -fcodegen-data-use      Use codegen data read from default.cgdata to optimize the binary
  -fcolor-diagnostics     Enable colors in diagnostics
  -fcomment-block-commands=<arg>
                          Treat each comma separated argument in <arg> as a documentation comment block command
  -fcommon                Place uninitialized global variables in a common block
  -fcomplete-member-pointers
                          Require member pointer base types to be complete if they would be significant under the Microsoft ABI
  -fcomplex-arithmetic=<value>
                          Controls the calculation methods of complex number multiplication and division.
  -fconstexpr-backtrace-limit=<value>
                          Set the maximum number of entries to print in a constexpr evaluation backtrace (0 = no limit)
  -fconstexpr-depth=<value>
                          Set the maximum depth of recursive constexpr function calls
  -fconstexpr-steps=<value>
                          Set the maximum number of steps in constexpr function evaluation
  -fconvergent-functions  Assume all functions may be convergent.
  -fcoro-aligned-allocation
                          Prefer aligned allocation for C++ Coroutines
  -fcoroutines            Enable support for the C++ Coroutines
  -fcoverage-compilation-dir=<value>
                          The compilation directory to embed in the coverage mapping.
  -fcoverage-mapping      Generate coverage mapping to enable code coverage analysis
  -fcoverage-mcdc         Enable MC/DC criteria when generating code coverage
  -fcoverage-prefix-map=<old>=<new>
                          remap file source paths <old> to <new> in coverage mapping. If there are multiple options, prefix replacement is applied in reverse order starting from the last one
  -fcrash-diagnostics-dir=<dir>
                          Put crash-report files in <dir>
  -fcrash-diagnostics=<value>
                          Set level of crash diagnostic reporting, (option: off, compiler, all)
  -fcrash-diagnostics     Enable crash diagnostic reporting (default)
  -fcs-profile-generate=<directory>
                          Generate instrumented code to collect context sensitive execution counts into <directory>/default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcs-profile-generate   Generate instrumented code to collect context sensitive execution counts into default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcuda-short-ptr        Use 32-bit pointers for accessing const/local/shared address spaces
  -fcx-fortran-rules      Range reduction is enabled for complex arithmetic operations.
  -fcx-limited-range      Basic algebraic expansions of complex arithmetic operations involving are enabled.
  -fcxx-exceptions        Enable C++ exceptions
  -fcxx-modules           Enable modules for C++
  -fdata-sections         Place each data in its own section
  -fdebug-compilation-dir=<value>
                          The compilation directory to embed in the debug info
  -fdebug-default-version=<value>
                          Default DWARF version to use, if a -g option caused DWARF debug info to be produced
  -fdebug-info-for-profiling
                          Emit extra debug info to make sample profile more accurate
  -fdebug-macro           Emit macro debug information
  -fdebug-prefix-map=<old>=<new>
                          For paths in debug info, remap directory <old> to <new>. If multiple options match a path, the last option wins
  -fdebug-ranges-base-address
                          Use DWARF base address selection entries in .debug_ranges
  -fdebug-types-section   Place debug types in their own section (ELF Only)
  -fdeclspec              Allow __declspec as a keyword
  -fdefine-target-os-macros
                          Enable predefined target OS macros
  -fdelayed-template-parsing
                          Parse templated function definitions at the end of the translation unit
  -fdelete-null-pointer-checks
                          Treat usage of null pointers as undefined behavior (default)
  -fdiagnostics-absolute-paths
                          Print absolute paths in diagnostics
  -fdiagnostics-color=<value>
                          When to use colors in diagnostics
  -fdiagnostics-hotness-threshold=<value>
                          Prevent optimization remarks from being output if they do not have at least this profile count. Use 'auto' to apply the threshold from profile summary
  -fdiagnostics-misexpect-tolerance=<value>
                          Prevent misexpect diagnostics from being output if the profile counts are within N% of the expected.
  -fdiagnostics-parseable-fixits
                          Print fix-its in machine parseable form
```

### `afl-clang-lto++`

官方给出的调用示例：`afl-clang-lto++ --help`

```text
root@kali:~# afl-clang-lto++ --help
OVERVIEW: clang LLVM compiler
USAGE: clang [options] file...
OPTIONS:
  -###                    Print (but do not run) the commands to run for this compilation
  --analyzer-output <value>
                          Static analyzer report output format (html|plist|plist-multi-file|plist-html|sarif|sarif-html|text).
  --analyze               Run the static analyzer
  -B <prefix>             Search $prefix$file for executables, libraries, and data files. If $prefix is a directory, search $prefix/$file
  -b <arg>                Pass -b <arg> to the linker on AIX
  -CC                     Include comments from within macros in preprocessed output
  -cl-denorms-are-zero    OpenCL only. Allow denormals to be flushed to zero.
  -cl-ext=<value>         OpenCL only. Enable or disable OpenCL extensions/optional features. The argument is a comma-separated sequence of one or more extension names, each prefixed by '+' or '-'.
  -cl-fast-relaxed-math   OpenCL only. Sets -cl-finite-math-only and -cl-unsafe-math-optimizations, and defines __FAST_RELAXED_MATH__.
  -cl-finite-math-only    OpenCL only. Allow floating-point optimizations that assume arguments and results are not NaNs or +-Inf.
  -cl-fp32-correctly-rounded-divide-sqrt
                          OpenCL only. Specify that single precision floating-point divide and sqrt used in the program source are correctly rounded.
  -cl-kernel-arg-info     OpenCL only. Generate kernel argument metadata.
  -cl-mad-enable          OpenCL only. Allow use of less precise MAD computations in the generated binary.
  -cl-no-signed-zeros     OpenCL only. Allow use of less precise no signed zeros computations in the generated binary.
  -cl-no-stdinc           OpenCL only. Disables all standard includes containing non-native compiler types and functions.
  -cl-opt-disable         OpenCL only. This option disables all optimizations. By default optimizations are enabled.
  -cl-single-precision-constant
                          OpenCL only. Treat double precision floating-point constant as single precision constant.
  -cl-std=<value>         OpenCL language standard to compile for.
  -cl-strict-aliasing     OpenCL only. This option is added for compatibility with OpenCL 1.0.
  -cl-uniform-work-group-size
                          OpenCL only. Defines that the global work-size be a multiple of the work-group size specified to clEnqueueNDRangeKernel
  -cl-unsafe-math-optimizations
                          OpenCL only. Allow unsafe floating-point optimizations.  Also implies -cl-no-signed-zeros and -cl-mad-enable.
  -clangir-disable-passes Disable CIR transformations pipeline
  -clangir-disable-verifier
                          ClangIR: Disable MLIR module verifier
  --config=<file>         Specify configuration file
  --cuda-compile-host-device
                          Compile CUDA code for both host and device (default). Has no effect on non-CUDA compilations.
  --cuda-device-only      Compile CUDA code for device only
  --cuda-feature=<value>  Manually specify the CUDA feature to use
  --cuda-host-only        Compile CUDA code for host only. Has no effect on non-CUDA compilations.
  --cuda-include-ptx=<value>
                          Include PTX for the following GPU architecture (e.g. sm_35) or 'all'. May be specified more than once.
  --cuda-noopt-device-debug
                          Enable device-side debug info generation. Disables ptxas optimizations.
  --cuda-path-ignore-env  Ignore environment variables to detect CUDA installation
  --cuda-path=<value>     CUDA installation path
  -cuid=<value>           An ID for compilation unit, which should be the same for the same compilation unit but different for different compilation units. It is used to externalize device-side static variables for single source offloading languages CUDA and HIP so that they can be accessed by the host code of the same compilation unit.
  -cxx-isystem <directory>
                          Add directory to the C++ SYSTEM include search path
  -C                      Include comments in preprocessed output
  -c                      Only run preprocess, compile, and assemble steps
  -darwin-target-variant-triple <value>
                          Specify the darwin target variant triple
  -darwin-target-variant <value>
                          Generate code for an additional runtime variant of the deployment target
  -dD                     Print macro definitions in -E mode in addition to normal output
  -dependency-dot <value> Filename to write DOT-formatted header dependencies to
  -dependency-file <value>
                          Filename (or -) to write dependency output to
  -dI                     Print include directives in -E mode in addition to normal output
  -dM                     Print macro definitions in -E mode instead of normal output
  -dsym-dir <dir>         Directory to output dSYM's (if any) to
  -dumpdir <dumppfx>      Use <dumpfpx> as a prefix to form auxiliary and dump file names
  -dumpmachine            Display the compiler's target processor
  -dumpversion            Display the version of the compiler
  -D <macro>=<value>      Define <macro> to <value> (or 1 if <value> omitted)
  --embed-dir=<dir>       Add directory to embed search path
  -emit-ast               Emit Clang AST files for source inputs
  -emit-cir               Build ASTs and then lower to ClangIR
  --emit-extension-symbol-graphs
                          Generate additional symbol graphs for extended modules.
  -emit-interface-stubs   Generate Interface Stub Files.
  -emit-llvm              Use the LLVM representation for assembler and object files
  -emit-merged-ifs        Generate Interface Stub Files, emit merged text not binary.
  --emit-static-lib       Enable linker job to emit a static library.
  -emit-symbol-graph      Generate Extract API information as a side effect of compilation.
  --end-no-unused-arguments
                          Start emitting warnings for unused driver arguments
  --extract-api-ignores=<value>
                          Comma separated list of files containing a new line separated list of API symbols to ignore when extracting API information.
  -extract-api            Extract API information
  -E                      Only run the preprocessor
  -faapcs-bitfield-load   Follows the AAPCS standard that all volatile bit-field write generates at least one load. (ARM only).
  -faapcs-bitfield-width  Follow the AAPCS standard requirement stating that volatile bit-field width is dictated by the field container type. (ARM only).
  -faarch64-jump-table-hardening
                          Use hardened lowering for jump-table dispatch
  -faddrsig               Emit an address-significance table
  -falign-loops=<N>       N must be a power of two. Align loops to the boundary
  -faligned-allocation    Enable C++17 aligned allocation functions
  -fallow-editor-placeholders
                          Treat editor placeholders as valid source code
  -fallow-runtime-check-skip-hot-cutoff=<value>
                          Exclude __builtin_allow_runtime_check for the top hottest code responsible for the given fraction of PGO counters (0.0 [default] = skip none; 1.0 = skip all). Argument format: <value>
  -faltivec-src-compat=<value>
                          Source-level compatibility for Altivec vectors (for PowerPC targets). This includes results of vector comparison (scalar for 'xl', vector for 'gcc') as well as behavior when initializing with a scalar (splatting for 'xl', element zero only for 'gcc'). For 'mixed', the compatibility is as 'gcc' for 'vector bool/vector pixel' and as 'xl' for other types. Current default is 'mixed'.
  -fansi-escape-codes     Use ANSI escape codes for diagnostics
  -fapinotes-modules      Enable module-based external API notes support
  -fapinotes-swift-version=<version>
                          Specify the Swift version to use when filtering API notes
  -fapinotes              Enable external API notes support
  -fapple-kext            Use Apple's kernel extensions ABI
  -fapple-link-rtlib      Force linking the clang builtins runtime library
  -fapple-pragma-pack     Enable Apple gcc-compatible #pragma pack handling
  -fapplication-extension Restrict code to those available for App Extensions
  -fapprox-func           Allow certain math function calls to be replaced with an approximately equivalent calculation
  -fassume-nothrow-exception-dtor
                          Assume that exception objects' destructors are non-throwing
  -fasync-exceptions      Enable EH Asynchronous exceptions
  -fatomic-fine-grained-memory
                          May have atomic operations on fine-grained memory
  -fatomic-ignore-denormal-mode
                          Allow atomic operations to ignore denormal mode
  -fatomic-remote-memory  May have atomic operations on remote memory
  -fauto-import           MinGW specific. Enable code generation support for automatic dllimport, and enable support for it in the linker. Enabled by default.
  -fbasic-block-address-map
                          Emit the basic block address map section.
  -fbasic-block-sections=<value>
                          Place each function's basic blocks in unique sections (ELF Only)
  -fbinutils-version=<major.minor>
                          Produced object files can use all ELF features supported by this binutils version and newer. If -fno-integrated-as is specified, the generated assembly will consider GNU as support. 'none' means that all ELF features can be used, regardless of binutils support. Defaults to 2.26.
  -fblocks                Enable the 'blocks' language feature
  -fborland-extensions    Accept non-standard constructs supported by the Borland compiler
  -fbuild-session-file=<file>
                          Use the last modification time of <file> as the build session timestamp
  -fbuild-session-timestamp=<time since Epoch in seconds>
                          Time when the current build session started
  -fbuiltin-module-map    Load the clang builtins module map file.
  -fc++-abi=<value>       C++ ABI to use. This will override the target C++ ABI.
  -fc++-static-destructors=<value>
                          Controls which variables C++ static destructors are registered for
  -fcall-saved-x10        Make the x10 register call-saved (AArch64 only)
  -fcall-saved-x11        Make the x11 register call-saved (AArch64 only)
  -fcall-saved-x12        Make the x12 register call-saved (AArch64 only)
  -fcall-saved-x13        Make the x13 register call-saved (AArch64 only)
  -fcall-saved-x14        Make the x14 register call-saved (AArch64 only)
  -fcall-saved-x15        Make the x15 register call-saved (AArch64 only)
  -fcall-saved-x18        Make the x18 register call-saved (AArch64 only)
  -fcall-saved-x8         Make the x8 register call-saved (AArch64 only)
  -fcall-saved-x9         Make the x9 register call-saved (AArch64 only)
  -fcaret-diagnostics-max-lines=<value>
                          Set the maximum number of source lines to show in a caret diagnostic (0 = no limit).
  -fcf-protection=<value> Instrument control-flow architecture protection
  -fcf-protection         Enable cf-protection in 'full' mode
  -fchar8_t               Enable C++ builtin type char8_t
  -fcheck-new             Do not assume C++ operator new may not return NULL
  -fclang-abi-compat=<version>
                          Attempt to match the ABI of Clang <version>
  -fclangir               Use the ClangIR pipeline to compile
  -fcodegen-data-generate=<path>
                          Emit codegen data into the object file. LLD for MachO (currently) merges them into the specified <path>.
  -fcodegen-data-generate Emit codegen data into the object file. LLD for MachO (currently) merges them into default.cgdata.
  -fcodegen-data-use=<path>
                          Use codegen data read from the specified <path>.
  -fcodegen-data-use      Use codegen data read from default.cgdata to optimize the binary
  -fcolor-diagnostics     Enable colors in diagnostics
  -fcomment-block-commands=<arg>
                          Treat each comma separated argument in <arg> as a documentation comment block command
  -fcommon                Place uninitialized global variables in a common block
  -fcomplete-member-pointers
                          Require member pointer base types to be complete if they would be significant under the Microsoft ABI
  -fcomplex-arithmetic=<value>
                          Controls the calculation methods of complex number multiplication and division.
  -fconstexpr-backtrace-limit=<value>
                          Set the maximum number of entries to print in a constexpr evaluation backtrace (0 = no limit)
  -fconstexpr-depth=<value>
                          Set the maximum depth of recursive constexpr function calls
  -fconstexpr-steps=<value>
                          Set the maximum number of steps in constexpr function evaluation
  -fconvergent-functions  Assume all functions may be convergent.
  -fcoro-aligned-allocation
                          Prefer aligned allocation for C++ Coroutines
  -fcoroutines            Enable support for the C++ Coroutines
  -fcoverage-compilation-dir=<value>
                          The compilation directory to embed in the coverage mapping.
  -fcoverage-mapping      Generate coverage mapping to enable code coverage analysis
  -fcoverage-mcdc         Enable MC/DC criteria when generating code coverage
  -fcoverage-prefix-map=<old>=<new>
                          remap file source paths <old> to <new> in coverage mapping. If there are multiple options, prefix replacement is applied in reverse order starting from the last one
  -fcrash-diagnostics-dir=<dir>
                          Put crash-report files in <dir>
  -fcrash-diagnostics=<value>
                          Set level of crash diagnostic reporting, (option: off, compiler, all)
  -fcrash-diagnostics     Enable crash diagnostic reporting (default)
  -fcs-profile-generate=<directory>
                          Generate instrumented code to collect context sensitive execution counts into <directory>/default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcs-profile-generate   Generate instrumented code to collect context sensitive execution counts into default.profraw (overridden by LLVM_PROFILE_FILE env var)
  -fcuda-short-ptr        Use 32-bit pointers for accessing const/local/shared address spaces
  -fcx-fortran-rules      Range reduction is enabled for complex arithmetic operations.
  -fcx-limited-range      Basic algebraic expansions of complex arithmetic operations involving are enabled.
  -fcxx-exceptions        Enable C++ exceptions
  -fcxx-modules           Enable modules for C++
  -fdata-sections         Place each data in its own section
  -fdebug-compilation-dir=<value>
                          The compilation directory to embed in the debug info
  -fdebug-default-version=<value>
                          Default DWARF version to use, if a -g option caused DWARF debug info to be produced
  -fdebug-info-for-profiling
                          Emit extra debug info to make sample profile more accurate
  -fdebug-macro           Emit macro debug information
  -fdebug-prefix-map=<old>=<new>
                          For paths in debug info, remap directory <old> to <new>. If multiple options match a path, the last option wins
  -fdebug-ranges-base-address
                          Use DWARF base address selection entries in .debug_ranges
  -fdebug-types-section   Place debug types in their own section (ELF Only)
  -fdeclspec              Allow __declspec as a keyword
  -fdefine-target-os-macros
                          Enable predefined target OS macros
  -fdelayed-template-parsing
                          Parse templated function definitions at the end of the translation unit
  -fdelete-null-pointer-checks
                          Treat usage of null pointers as undefined behavior (default)
  -fdiagnostics-absolute-paths
                          Print absolute paths in diagnostics
  -fdiagnostics-color=<value>
                          When to use colors in diagnostics
  -fdiagnostics-hotness-threshold=<value>
                          Prevent optimization remarks from being output if they do not have at least this profile count. Use 'auto' to apply the threshold from profile summary
  -fdiagnostics-misexpect-tolerance=<value>
                          Prevent misexpect diagnostics from being output if the profile counts are within N% of the expected.
  -fdiagnostics-parseable-fixits
                          Print fix-its in machine parseable form
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install afl++`，再执行 `afl++ --version` 2>/dev/null || `afl++ -V`
- [ ] **2.** **读官方帮助** —— `afl++ -h`，需要细节时 `man afl++`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `afl++ -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/aflplusplus/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/aflplusplus/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/aflplusplus/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
