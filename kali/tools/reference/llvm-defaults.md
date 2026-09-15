# llvm-defaults

> C, C++ and Objective-C compiler (LLVM based), clang binary Clang project is a C, C++, Objective C and Objective C++ front-end for the LLVM compiler. Its goal is to offer a replacement to the GNU Compiler Collection (GCC). Clang implements …

> **功能分类**：漏洞分析 ｜ **Kali 包**：`llvm-defaults` ｜ **官方文档**：<https://www.kali.org/tools/llvm-defaults/>

## 1. 安装

```bash
sudo apt update
sudo apt install clang
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.71 |
| 架构 | amd64 |
| 可执行命令 | `clang`、`clang++`、`clang-cl`、`clang-cpp`、`clang-scan-deps`、`clang-format`、`clang-format-diff`、`git-clang-format`、`clang-tidy`、`run-clang-tidy`、`clang-tools`、`amdgpu-arch`、`analyze-build`、`asan_symbolize`、`c-index-test`、`clang-apply-replacements`、`clang-change-namespace`、`clang-check`、`clang-doc`、`clang-extdef-mapping`、`clang-include-cleaner`、`clang-include-fixer`、`clang-installapi`、`clang-linker-wrapper`、`clang-move`、`clang-nvlink-wrapper`、`clang-offload-bundler`、`clang-offload-packager`、`clang-query`、`clang-refactor`、`clang-reorder-fields`、`clang-repl`、`clang-sycl-linker`、`clang-tblgen`、`diagtool`、`find-all-symbols`、`hmaptool`、`hwasan_symbolize`、`intercept-build`、`modularize`、`nvptx-arch`、`offload-arch`、`pp-trace`、`sancov`、`scan-build`、`scan-build-py`、`scan-view`、`clangd`、`flang`、`bbc`、`f18-parse-demo`、`fir-lsp-server`、`fir-opt`、`flang-new`、`tco`、`libbolt-dev`、`libc++-dev`、`libc++-dev-wasm32`、`libc++abi-dev`、`libclang-cpp-dev`、`libclang-dev`、`libclang-rt-dev`、`libclang-rt-dev-wasm32`、`libclang-rt-dev-wasm64`、`libclang-rt-dev-win`、`libflang-dev`、`liblld-dev`、`liblldb-dev`、`libllvm-ocaml-dev`、`libomp-dev`、`libpolly-dev`、`lld`、`ld.lld`、`ld64.lld`、`lld-link`、`wasm-ld`、`lldb`、`lldb-argdumper`、`lldb-dap`、`lldb-instr`、`lldb-server`、`llvm`、`bugpoint`、`dsymutil`、`llc` |
| 依赖 | `clang-21`、`clang` |
| 安装体积 | 22 KB |
| 源码仓库 | <https://salsa.debian.org/pkg-llvm-team/llvm-defaults/> |
| 包追踪 | <https://pkg.kali.org/pkg/llvm-defaults> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
clang -h          # 查看用法
man clang         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 85 个可执行命令，下面是官方页面内嵌的帮助原文。

### `clang`

> 官方示例调用：`clang --help`

```text
root@kali:~# clang --help
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

### `clang++`

> 官方示例调用：`clang++ --help`

```text
root@kali:~# clang++ --help
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

### `clang-cpp`

> 官方示例调用：`clang-cpp --help`

```text
root@kali:~# clang-cpp --help
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

### `clang-scan-deps`

> 官方示例调用：`clang-scan-deps --help`

```text
root@kali:~# clang-scan-deps --help
OVERVIEW: clang-scan-deps
USAGE: clang-scan-deps [options]
OPTIONS:
  -compilation-database=<value>
                          Compilation database
  -dependency-target=<value>
                          The names of dependency targets for the dependency file
  -deprecated-driver-command
                          use a single driver command to build the tu (deprecated)
  -eager-load-pcm         Load PCM files eagerly (instead of lazily on import)
  -emit-visible-modules   emit visible modules in primary output
  -format=<value>         The output format for the dependencies
  --help                  Display this help
  -j <value>              Number of worker threads to use (default: use all concurrent threads)
  -mode=<value>           The preprocessing mode used to compute the dependencies
  -module-files-dir=<value>
                          The build directory for modules. Defaults to the value of '-fmodules-cache-path=' from command lines for implicit modules
  -module-name=<value>    the module of which the dependencies are to be computed
  -optimize-args=<value>  Which command-line arguments of modules to optimize
  -o <value>              Destination of the primary output
  -print-timing           Print timing information
  -resource-dir-recipe=<value>
                          How to produce missing '-resource-dir' argument
  -round-trip-args        verify that command-line arguments are canonical by parsing and re-serializing
  -tu-buffer-path=<value> The path to the translation unit for depscan. Not compatible with -module-name
  --version               Display the version
  -v                      Use verbose output
```

### `clang-format`

> 官方示例调用：`clang-format --help`

```text
root@kali:~# clang-format --help
OVERVIEW: A tool to format C/C++/Java/JavaScript/JSON/Objective-C/Protobuf/C# code.
If no arguments are specified, it formats the code from standard input
and writes the result to the standard output.
If <file>s are given, it reformats the files. If -i is specified
together with <file>s, the files are edited in-place. Otherwise, the
result is written to the standard output.
USAGE: clang-format [options] [@<file>] [<file> ...]
OPTIONS:
Clang-format options:
  --Werror                       - If set, changes formatting warnings to errors
  --Wno-error=<value>            - If set, don't error out on the specified warning type.
    =unknown                     -   If set, unknown format options are only warned about.
                                     This can be used to enable formatting, even if the
                                     configuration contains unknown (newer) options.
                                     Use with caution, as this might lead to dramatically
                                     differing format depending on an option being
                                     supported or not.
  --assume-filename=<string>     - Set filename used to determine the language and to find
                                   .clang-format file.
                                   Only used when reading from stdin.
                                   If this is not passed, the .clang-format file is searched
                                   relative to the current working directory when reading stdin.
                                   Unrecognized filenames are treated as C++.
                                   supported:
                                     CSharp: .cs
                                     Java: .java
                                     JavaScript: .js .mjs .cjs .ts
                                     Json: .json .ipynb
                                     Objective-C: .m .mm
                                     Proto: .proto .protodevel
                                     TableGen: .td
                                     TextProto: .txtpb .textpb .pb.txt .textproto .asciipb
                                     Verilog: .sv .svh .v .vh
  --cursor=<uint>                - The position of the cursor when invoking
                                   clang-format from an editor integration
  --dry-run                      - If set, do not actually make the formatting changes
  --dump-config                  - Dump configuration options to stdout and exit.
                                   Can be used with -style option.
  --fail-on-incomplete-format    - If set, fail with exit code 1 on incomplete format.
  --fallback-style=<string>      - The name of the predefined style used as a
                                   fallback in case clang-format is invoked with
                                   -style=file, but can not find the .clang-format
                                   file to use. Defaults to 'LLVM'.
                                   Use -fallback-style=none to skip formatting.
  --ferror-limit=<uint>          - Set the maximum number of clang-format errors to emit
                                   before stopping (0 = no limit).
                                   Used only with --dry-run or -n
  --files=<filename>             - A file containing a list of files to process, one per line.
  -i                             - Inplace edit <file>s, if specified.
  --length=<uint>                - Format a range of this length (in bytes).
                                   Multiple ranges can be formatted by specifying
                                   several -offset and -length pairs.
                                   When only a single -offset is specified without
                                   -length, clang-format will format up to the end
                                   of the file.
                                   Can only be used with one input file.
  --lines=<string>               - <start line>:<end line> - format a range of
                                   lines (both 1-based).
                                   Multiple ranges can be formatted by specifying
                                   several -lines arguments.
                                   Can't be used with -offset and -length.
                                   Can only be used with one input file.
  -n                             - Alias for --dry-run
  --offset=<uint>                - Format a range starting at this byte offset.
                                   Multiple ranges can be formatted by specifying
                                   several -offset and -length pairs.
                                   Can only be used with one input file.
  --output-replacements-xml      - Output replacements as XML.
  --qualifier-alignment=<string> - If set, overrides the qualifier alignment style
                                   determined by the QualifierAlignment style flag
  --sort-includes                - If set, overrides the include sorting behavior
                                   determined by the SortIncludes style flag
  --style=<string>               - Set coding style. <string> can be:
                                   1. A preset: LLVM, GNU, Google, Chromium, Microsoft,
                                      Mozilla, WebKit.
                                   2. 'file' to load style configuration from a
                                      .clang-format file in one of the parent directories
                                      of the source file (for stdin, see --assume-filename).
                                      If no .clang-format file is found, falls back to
                                      --fallback-style.
                                      --style=file is the default.
                                   3. 'file:<format_file_path>' to explicitly specify
                                      the configuration file.
                                   4. "{key: value, ...}" to set specific parameters, e.g.:
                                      --style="{BasedOnStyle: llvm, IndentWidth: 8}"
  --verbose                      - If set, shows the list of processed files
Generic Options:
  --help                         - Display available options (--help-hidden for more)
  --help-list                    - Display list of available options (--help-list-hidden for more)
  --version                      - Display the version of this program
```

### `clang-format-diff`

> 官方示例调用：`clang-format-diff -h`

```text
root@kali:~# clang-format-diff -h
usage: clang-format-diff [-h] [-i] [-p NUM] [-regex PATTERN] [-iregex PATTERN]
                         [-sort-includes] [-v] [-style STYLE]
                         [-fallback-style FALLBACK_STYLE] [-binary BINARY]
This script reads input from a unified diff and reformats all the changed
lines. This is useful to reformat all the lines touched by a specific patch.
Example usage for git/svn users:
  git diff -U0 --no-color --relative HEAD^ | clang-format-diff -p1 -i
  svn diff --diff-cmd=diff -x-U0 | clang-format-diff -i
It should be noted that the filename contained in the diff is used unmodified
to determine the source file to update. Users calling this script directly
should be careful to ensure that the path in the diff is correct relative to the
current working directory.
options:
  -h, --help            show this help message and exit
  -i                    apply edits to files instead of displaying a diff
  -p NUM                strip the smallest prefix containing P slashes
  -regex PATTERN        custom pattern selecting file paths to reformat (case
                        sensitive, overrides -iregex)
  -iregex PATTERN       custom pattern selecting file paths to reformat (case
                        insensitive, overridden by -regex)
  -sort-includes        let clang-format sort include blocks
  -v, --verbose         be more verbose, ineffective without -i
  -style STYLE          formatting style to apply (LLVM, GNU, Google,
                        Chromium, Microsoft, Mozilla, WebKit)
  -fallback-style FALLBACK_STYLE
                        The name of the predefined style used as afallback in
                        case clang-format is invoked with-style=file, but can
                        not find the .clang-formatfile to use.
  -binary BINARY        location of binary to use for clang-format
```

### `git-clang-format`

> 官方示例调用：`git-clang-format -h`

```text
root@kali:~# git-clang-format -h
usage: git clang-format [OPTIONS] [<commit>] [<commit>|--staged] [--] [<file>...]
If zero or one commits are given, run clang-format on all lines that differ
between the working directory and <commit>, which defaults to HEAD.  Changes are
only applied to the working directory, or in the stage/index.
Examples:
  To format staged changes, i.e everything that's been `git add`ed:
    git clang-format
  To also format everything touched in the most recent commit:
    git clang-format HEAD~1
  If you're on a branch off main, to format everything touched on your branch:
    git clang-format main
If two commits are given (requires --diff), run clang-format on all lines in the
second <commit> that differ from the first <commit>.
The following git-config settings set the default of the corresponding option:
  clangFormat.binary
  clangFormat.commit
  clangFormat.extensions
  clangFormat.style
positional arguments:
  <commit>              revision from which to compute the diff
  <file>...             if specified, only consider differences in these files
options:
  -h, --help            show this help message and exit
  --binary BINARY       path to clang-format
  --commit COMMIT       default commit to use if none is specified
  --diff                print a diff instead of applying the changes
  --diffstat            print a diffstat instead of applying the changes
  --extensions EXTENSIONS
                        comma-separated list of file extensions to format,
                        excluding the period and case-insensitive
  -f, --force           allow changes to unstaged files
  -p, --patch           select hunks interactively
  -q, --quiet           print less information
  --staged, --cached    format lines in the stage instead of the working dir
  --style STYLE         passed to clang-format
  -v, --verbose         print extra information
  --diff_from_common_commit
                        diff from the last common commit for commits in
                        separate branches rather than the exact point of the
                        commits
```

### `clang-tidy`

> 官方示例调用：`clang-tidy -h`

```text
root@kali:~# clang-tidy -h
USAGE: clang-tidy [options] <source0> [... <sourceN>]
OPTIONS:
Generic Options:
  --help                           - Display available options (--help-hidden for more)
  --help-list                      - Display list of available options (--help-list-hidden for more)
  --version                        - Display the version of this program
clang-tidy options:
  --allow-no-checks                - Allow empty enabled checks. This suppresses
                                     the "no checks enabled" error when disabling
                                     all of the checks.
  --checks=<string>                - Comma-separated list of globs with optional '-'
                                     prefix. Globs are processed in order of
                                     appearance in the list. Globs without '-'
                                     prefix add checks with matching names to the
                                     set, globs with the '-' prefix remove checks
                                     with matching names from the set of enabled
                                     checks. This option's value is appended to the
                                     value of the 'Checks' option in .clang-tidy
                                     file, if any.
  --config=<string>                - Specifies a configuration in YAML/JSON format:
                                       -config="{Checks: '*',
                                                 CheckOptions: {x: y}}"
                                     When the value is empty, clang-tidy will
                                     attempt to find a file named .clang-tidy for
                                     each source file in its parent directories.
  --config-file=<string>           - Specify the path of .clang-tidy or custom config file:
                                      e.g. --config-file=/some/path/myTidyConfigFile
                                     This option internally works exactly the same way as
                                      --config option after reading specified config file.
                                     Use either --config-file or --config, not both.
  --dump-config                    - Dumps configuration in the YAML format to
                                     stdout. This option can be used along with a
                                     file name (and '--' if the file is outside of a
                                     project with configured compilation database).
                                     The configuration used for this file will be
                                     printed.
                                     Use along with -checks=* to include
                                     configuration of all checks.
  --enable-check-profile           - Enable per-check timing profiles, and print a
                                     report to stderr.
  --enable-module-headers-parsing  - Enables preprocessor-level module header parsing
                                     for C++20 and above, empowering specific checks
                                     to detect macro definitions within modules. This
                                     feature may cause performance and parsing issues
                                     and is therefore considered experimental.
  --exclude-header-filter=<string> - Regular expression matching the names of the
                                     headers to exclude diagnostics from. Diagnostics
                                     from the main file of each translation unit are
                                     always displayed.
                                     Must be used together with --header-filter.
                                     Can be used together with -line-filter.
                                     This option overrides the 'ExcludeHeaderFilterRegex'
                                     option in .clang-tidy file, if any.
  --explain-config                 - For each enabled check explains, where it is
                                     enabled, i.e. in clang-tidy binary, command
                                     line or a specific configuration file.
  --export-fixes=<filename>        - YAML file to store suggested fixes in. The
                                     stored fixes can be applied to the input source
                                     code with clang-apply-replacements.
  --extra-arg=<string>             - Additional argument to append to the compiler command line
  --extra-arg-before=<string>      - Additional argument to prepend to the compiler command line
  --fix                            - Apply suggested fixes. Without -fix-errors
                                     clang-tidy will bail out if any compilation
                                     errors were found.
  --fix-errors                     - Apply suggested fixes even if compilation
                                     errors were found. If compiler errors have
                                     attached fix-its, clang-tidy will apply them as
                                     well.
  --fix-notes                      - If a warning has no fix, but a single fix can
                                     be found through an associated diagnostic note,
                                     apply the fix.
                                     Specifying this flag will implicitly enable the
                                     '--fix' flag.
  --format-style=<string>          - Style for formatting code around applied fixes:
                                       - 'none' (default) turns off formatting
                                       - 'file' (literally 'file', not a placeholder)
                                         uses .clang-format file in the closest parent
                                         directory
                                       - '{ <json> }' specifies options inline, e.g.
                                         -format-style='{BasedOnStyle: llvm, IndentWidth: 8}'
                                       - 'llvm', 'google', 'webkit', 'mozilla'
                                     See clang-format documentation for the up-to-date
                                     information about formatting styles and options.
                                     This option overrides the 'FormatStyle` option in
                                     .clang-tidy file, if any.
  --header-filter=<string>         - Regular expression matching the names of the
                                     headers to output diagnostics from. Diagnostics
                                     from the main file of each translation unit are
                                     always displayed.
                                     Can be used together with -line-filter.
                                     This option overrides the 'HeaderFilterRegex'
                                     option in .clang-tidy file, if any.
  --line-filter=<string>           - List of files with line ranges to filter the
                                     warnings. Can be used together with
                                     -header-filter. The format of the list is a
                                     JSON array of objects:
                                       [
                                         {"name":"file1.cpp","lines":[[1,3],[5,7]]},
                                         {"name":"file2.h"}
                                       ]
  --list-checks                    - List all enabled checks and exit. Use with
                                     -checks=* to list all available checks.
  --load=<pluginfilename>          - Load the specified plugin
  -p <string>                      - Build path
  --quiet                          - Run clang-tidy in quiet mode. This suppresses
                                     printing statistics about ignored warnings and
                                     warnings treated as errors if the respective
                                     options are specified.
  --store-check-profile=<prefix>   - By default reports are printed in tabulated
                                     format to stderr. When this option is passed,
                                     these per-TU profiles are instead stored as JSON.
  --system-headers                 - Display the errors from system headers.
                                     This option overrides the 'SystemHeaders' option
                                     in .clang-tidy file, if any.
  --use-color                      - Use colors in diagnostics. If not set, colors
                                     will be used if the terminal connected to
                                     standard output supports colors.
                                     This option overrides the 'UseColor' option in
                                     .clang-tidy file, if any.
  --verify-config                  - Check the config files to ensure each check and
                                     option is recognized without running any checks.
  --vfsoverlay=<filename>          - Overlay the virtual filesystem described by file
                                     over the real file system.
  --warnings-as-errors=<string>    - Upgrades warnings to errors. Same format as
                                     '-checks'.
                                     This option's value is appended to the value of
                                     the 'WarningsAsErrors' option in .clang-tidy
                                     file, if any.
-p <build-path> is used to read a compile command database.
	For example, it can be a CMake build directory in which a file named
	compile_commands.json exists (use -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
	CMake option to get this output). When no build path is specified,
	a search for compile_commands.json will be attempted through all
	parent paths of the first input file . See:
	https://clang.llvm.org/docs/HowToSetupToolingForLLVM.html for an
	example of setting up Clang Tooling on a source tree.
<source0> ... specify the paths of source files. These paths are
	looked up in the compile command database. If the path of a file is
	absolute, it needs to point into CMake's source tree. If the path is
	relative, the current working directory needs to be in the CMake
	source tree and the file must be in a subdirectory of the current
	working directory. "./" prefixes in the relative files will be
	automatically removed, but the rest of a relative path must be a
	suffix of a path in the compile command database.
Parameters files:
  A large number of options or source files can be passed as parameter files
  by use '@parameter-file' in the command line.
Configuration files:
  clang-tidy attempts to read configuration for each source file from a
  .clang-tidy file located in the closest parent directory of the source
  file. The .clang-tidy file is specified in YAML format. If any configuration
  options have a corresponding command-line option, command-line option takes
  precedence.
  The following configuration options may be used in a .clang-tidy file:
  CheckOptions                 - List of key-value pairs defining check-specific
                                 options. Example:
                                   CheckOptions:
                                     some-check.SomeOption: 'some value'
  Checks                       - Same as '--checks'. Additionally, the list of
                                 globs can be specified as a list instead of a
                                 string.
  ExcludeHeaderFilterRegex     - Same as '--exclude-header-filter'.
  ExtraArgs                    - Same as '--extra-arg'.
  ExtraArgsBefore              - Same as '--extra-arg-before'.
  FormatStyle                  - Same as '--format-style'.
  HeaderFileExtensions         - File extensions to consider to determine if a
                                 given diagnostic is located in a header file.
  HeaderFilterRegex            - Same as '--header-filter'.
  ImplementationFileExtensions - File extensions to consider to determine if a
                                 given diagnostic is located in an
                                 implementation file.
  InheritParentConfig          - If this option is true in a config file, the
                                 configuration file in the parent directory
                                 (if any exists) will be taken and the current
                                 config file will be applied on top of the
                                 parent one.
  SystemHeaders                - Same as '--system-headers'.
  UseColor                     - Same as '--use-color'.
  User                         - Specifies the name or e-mail of the user
                                 running clang-tidy. This option is used, for
                                 example, to place the correct user name in
                                 TODO() comments in the relevant check.
  WarningsAsErrors             - Same as '--warnings-as-errors'.
  The effective configuration can be inspected using --dump-config:
    $ clang-tidy --dump-config
    ---
    Checks:                       '-*,some-check'
    WarningsAsErrors:             ''
    HeaderFileExtensions:         ['', 'h','hh','hpp','hxx']
    ImplementationFileExtensions: ['c','cc','cpp','cxx']
    HeaderFilterRegex:            ''
    FormatStyle:                  none
    InheritParentConfig:          true
    User:                         user
    CheckOptions:
      some-check.SomeOption: 'some value'
    ...
```

### `run-clang-tidy`

> 官方示例调用：`run-clang-tidy -h`

```text
root@kali:~# run-clang-tidy -h
usage: run-clang-tidy [-h] [-allow-enabling-alpha-checkers]
                      [-clang-tidy-binary PATH]
                      [-clang-apply-replacements-binary PATH] [-checks CHECKS]
                      [-config CONFIG | -config-file CONFIG_FILE]
                      [-exclude-header-filter EXCLUDE_HEADER_FILTER]
                      [-header-filter HEADER_FILTER]
                      [-source-filter SOURCE_FILTER]
                      [-line-filter LINE_FILTER]
                      [-export-fixes file_or_directory] [-j J] [-fix]
                      [-format] [-style STYLE] [-use-color [USE_COLOR]]
                      [-p BUILD_PATH] [-extra-arg EXTRA_ARG]
                      [-extra-arg-before EXTRA_ARG_BEFORE] [-quiet]
                      [-load PLUGINS] [-warnings-as-errors WARNINGS_AS_ERRORS]
                      [-allow-no-checks]
                      [files ...]
Runs clang-tidy over all files in a compilation database. Requires clang-tidy
and clang-apply-replacements in $PATH or in your build directory.
positional arguments:
  files                 Files to be processed (regex on path).
options:
  -h, --help            show this help message and exit
  -allow-enabling-alpha-checkers
                        Allow alpha checkers from clang-analyzer.
  -clang-tidy-binary PATH
                        Path to clang-tidy binary.
  -clang-apply-replacements-binary PATH
                        Path to clang-apply-replacements binary.
  -checks CHECKS        Checks filter, when not specified, use clang-tidy
                        default.
  -config CONFIG        Specifies a configuration in YAML/JSON format:
                        -config="{Checks: '*', CheckOptions: {x: y}}" When the
                        value is empty, clang-tidy will attempt to find a file
                        named .clang-tidy for each source file in its parent
                        directories.
  -config-file CONFIG_FILE
                        Specify the path of .clang-tidy or custom config file:
                        e.g. -config-file=/some/path/myTidyConfigFile. This
                        option internally works exactly the same way as
                        -config option after reading specified config file.
                        Use either -config-file or -config, not both.
  -exclude-header-filter EXCLUDE_HEADER_FILTER
                        Regular expression matching the names of the headers
                        to exclude diagnostics from. Diagnostics from the main
                        file of each translation unit are always displayed.
  -header-filter HEADER_FILTER
                        Regular expression matching the names of the headers
                        to output diagnostics from. Diagnostics from the main
                        file of each translation unit are always displayed.
  -source-filter SOURCE_FILTER
                        Regular expression matching the names of the source
                        files from compilation database to output diagnostics
                        from.
  -line-filter LINE_FILTER
                        List of files with line ranges to filter the warnings.
  -export-fixes file_or_directory
                        A directory or a yaml file to store suggested fixes
                        in, which can be applied with clang-apply-
                        replacements. If the parameter is a directory, the
                        fixes of each compilation unit are stored in
                        individual yaml files in the directory.
  -j J                  Number of tidy instances to be run in parallel.
  -fix                  apply fix-its.
  -format               Reformat code after applying fixes.
  -style STYLE          The style of reformat code after applying fixes.
  -use-color [USE_COLOR]
                        Use colors in diagnostics, overriding clang-tidy's
                        default behavior. This option overrides the 'UseColor'
                        option in .clang-tidy file, if any.
  -p BUILD_PATH         Path used to read a compile command database.
  -extra-arg EXTRA_ARG  Additional argument to append to the compiler command
                        line.
  -extra-arg-before EXTRA_ARG_BEFORE
                        Additional argument to prepend to the compiler command
                        line.
  -quiet                Run clang-tidy in quiet mode.
  -load PLUGINS         Load the specified plugin in clang-tidy.
  -warnings-as-errors WARNINGS_AS_ERRORS
                        Upgrades warnings to errors. Same format as '-checks'.
  -allow-no-checks      Allow empty enabled checks.
```

### `amdgpu-arch`

> 官方示例调用：`amdgpu-arch --help`

```text
root@kali:~# amdgpu-arch --help
OVERVIEW: A tool to detect the presence of offloading devices on the system.
The tool will output each detected GPU architecture separated by a
newline character. If multiple GPUs of the same architecture are found
a string will be printed for each
USAGE: amdgpu-arch [options]
OPTIONS:
Generic Options:
  --help         - Display available options (--help-hidden for more)
  --help-list    - Display list of available options (--help-list-hidden for more)
  --version      - Display the version of this program
offload-arch options:
  --only=<value> - Restrict to vendor:
    =all         -   Print all GPUs (default)
    =amdgpu      -   Only print AMD GPUs
    =nvptx       -   Only print NVIDIA GPUs
  --verbose      - Enable verbose output
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install clang`，再执行 `clang --version` 2>/dev/null || `clang -V`
- [ ] **2.** **读官方帮助** —— `clang -h`，需要细节时 `man clang`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `clang -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/llvm-defaults/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/llvm-defaults/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/llvm-defaults/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
