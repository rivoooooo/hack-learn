# powershell

> PowerShell is an automation and configuration management platform. It consists of a cross-platform command-line shell and associated scripting language.

> **功能分类**：通用工具 ｜ **Kali 包**：`powershell` ｜ **官方文档**：<https://www.kali.org/tools/powershell/>

## 1. 安装

```bash
sudo apt update
sudo apt install powershell
```

| 项目 | 内容 |
|------|------|
| 版本 | 7.6.2 |
| 架构 | amd64 |
| 可执行命令 | `powershell`、`pwsh` |
| 依赖 | `libc6`、`libgcc1`、`libgssapi-krb5-2` |
| 安装体积 | 188.65 MB |
| 官网 | <https://microsoft.com/powershell> |
| 包追踪 | <https://pkg.kali.org/pkg/powershell> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
powershell -h          # 查看用法
man powershell         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pwsh`

官方给出的调用示例：`pwsh -h`

```text
root@kali:~# pwsh -h
Usage: pwsh[.exe] [-Login] [[-File] <filePath> [args]]
                  [-Command { - | <script-block> [-args <arg-array>]
                                | <string> [<CommandParameters>] } ]
                  [-CommandWithArgs <string> [<CommandParameters>]
                  [-ConfigurationName <string>] [-ConfigurationFile <filePath>]
                  [-CustomPipeName <string>] [-EncodedCommand <Base64EncodedCommand>]
                  [-ExecutionPolicy <ExecutionPolicy>] [-InputFormat {Text | XML}]
                  [-Interactive] [-MTA] [-NoExit] [-NoLogo] [-NonInteractive] [-NoProfile]
                  [-NoProfileLoadTime] [-OutputFormat {Text | XML}]
                  [-SettingsFile <filePath>] [-SSHServerMode] [-STA]
                  [-Version] [-WindowStyle <style>]
                  [-WorkingDirectory <directoryPath>]
       pwsh[.exe] -h | -Help | -? | /?
PowerShell Online Help https://aka.ms/powershell-docs
All parameters are case-insensitive.
-File | -f
    If the value of File is "-", the command text is read from standard input.
    Running "pwsh -File -" without redirected standard input starts a regular
    session. This is the same as not specifying the File parameter at all.
    This is the default parameter if no parameters are present but values are
    present in the command line. The specified script runs in the local scope
    ("dot-sourced"), so that the functions and variables that the script
    creates are available in the current session. Enter the script file path
    and any parameters. File must be the last parameter in the command, because
    all characters typed after the File parameter name are interpreted as the
    script file path followed by the script parameters.
    Typically, the switch parameters of a script are either included or
    omitted. For example, the following command uses the All parameter of the
    Get-Script.ps1 script file: "-File .\Get-Script.ps1 -All"
    In rare cases, you might need to provide a BOOLEAN value for a switch
    parameter. To provide a BOOLEAN value for a switch parameter in the value
    of the FILE parameter, Use the parameter normally followed immediately by a
    colon and the boolean value, such as the following:
    "-File .\Get-Script.ps1 -All:$False".
    Parameters passed to the script are passed as literal strings, after
    interpretation by the current shell. For example, if you are in cmd.exe and
    want to pass an environment variable value, you would use the cmd.exe
    syntax: "pwsh -File .\test.ps1 -TestParam %windir%"
    In contrast, running "pwsh -File .\test.ps1 -TestParam $env:windir" in
    cmd.exe results in the script receiving the literal string "$env:windir"
    because it has no special meaning to the current cmd.exe shell. The
    "$env:windir" style of environment variable reference can be used inside a
    Command parameter, since there it is interpreted as PowerShell code.
    Similarly, if you want to execute the same command from a Batch script,
    you would use "%~dp0" instead of ".\" or "$PSScriptRoot" to represent the current
    execution directory: "pwsh -File %~dp0test.ps1 -TestParam %windir%". If you
    instead used ".\test.ps1", PowerShell would throw an error because it cannot
    find the literal path ".\test.ps1".
    When the script file invoked terminates with an exit command, the process
    exit code is set to the numeric argument used with the exit command. With
    normal termination, the exit code is always 0.
    Similar to -Command, when a script-terminating error occurs, the exit code
    is set to 1. However, unlike with -Command, when the execution is
    interrupted with Ctrl-C the exit code is 0.
-Command | -c
    Executes the specified commands (and any parameters) as though they were
    typed at the PowerShell command prompt, and then exits, unless the NoExit
    parameter is specified.
    The value of Command can be "-", a script block, or a string. If the value
    of Command is "-", the command text is read from standard input.
    The Command parameter only accepts a script block for execution when it can
    recognize the value passed to Command as a ScriptBlock type. This is only
    possible when running pwsh from another PowerShell host. The ScriptBlock
    type may be contained in an existing variable, returned from an expression,
    or parsed by the PowerShell host as a literal script block enclosed in
    curly braces "{}", before being passed to pwsh.
        pwsh -Command {Get-WinEvent -LogName security}
    In cmd.exe, there is no such thing as a script block (or ScriptBlock type),
    so the value passed to Command will always be a string. You can write a
    script block inside the string, but instead of being executed it will
    behave exactly as though you typed it at a typical PowerShell prompt,
    printing the contents of the script block back out to you.
    A string passed to Command is still executed as PowerShell script, so the
    script block curly braces are often not required in the first place when
    running from cmd.exe. To execute an inline script block defined inside a
    string, the call operator "&" can be used:
        pwsh -Command "& {Get-WinEvent -LogName security}"
    If the value of Command is a string, Command must be the last parameter for
    pwsh, because all arguments following it are interpreted as part of the
    command to execute.
    When called from within an existing PowerShell session, the results are
    returned to the parent shell as deserialized XML objects, not live objects.
    For other shells, the results are returned as strings.
    If the value of Command is "-", the command text is read from standard
    input. You must redirect standard input when using the Command parameter
    with standard input. For example:
        @'
        "in"
        "hi" |
        % { "$_ there" }
        "out"
        '@ | powershell -NoProfile -Command -
    This example produces the following output:
        in
        hi there
        out
    The process exit code is determined by status of the last (executed)
    command within the script block. The exit code is 0 when $? is $true or 1
    when $? is $false. If the last command is an external program or a
    PowerShell script that explicitly sets an exit code other than 0 or 1, that
    exit code is converted to 1 for process exit code. To preserve the specific
    exit code, add exit $LASTEXITCODE to your command string or script block.
    Similarly, the value 1 is returned when a script-terminating
    (runspace-terminating) error, such as a throw or -ErrorAction Stop, occurs
    or when execution is interrupted with Ctrl-C.
-CommandWithArgs | -cwa
    [Experimental]
    Executes a PowerShell command with arguments.  Unlike `-Command`, this
    parameter populates the `$args built-in variable which can be used by the
    command.
    The first string is the command and subsequent strings delimited by whitespace
    are the arguments.
    For example:
        pwsh -CommandWithArgs '$args | % { "arg: $_" }' arg1 arg2
    This example produces the following output:
        arg: arg1
        arg: arg2
-ConfigurationName | -config
    Specifies a configuration endpoint in which PowerShell is run. This can be
    any endpoint registered on the local machine including the default
    PowerShell remoting endpoints or a custom endpoint having specific user
    role capabilities.
    Example: "pwsh -ConfigurationName AdminRoles"
-ConfigurationFile
    Specifies a session configuration (.pssc) file path. The configuration
    contained in the configuration file will be applied to the PowerShell
    session.
    Example: "pwsh -ConfigurationFile "C:\ProgramData\PowerShell\MyConfig.pssc"
-CustomPipeName
    Specifies the name to use for an additional IPC server (named pipe) used
    for debugging and other cross-process communication. This offers a
    predictable mechanism for connecting to other PowerShell instances.
    Typically used with the CustomPipeName parameter on "Enter-PSHostProcess".
    This parameter was introduced in PowerShell 6.2.
    For example:
        # PowerShell instance 1
        pwsh -CustomPipeName mydebugpipe
        # PowerShell instance 2
        Enter-PSHostProcess -CustomPipeName mydebugpipe
-EncodedCommand | -e | -ec
    Accepts a Base64-encoded string version of a command. Use this parameter to
    submit commands to PowerShell that require complex, nested quoting. The
    Base64 representation must be a UTF-16 encoded string.
    For example:
        $command = 'dir "c:\program files" '
        $bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
        $encodedCommand = [Convert]::ToBase64String($bytes)
        pwsh -encodedcommand $encodedCommand
-ExecutionPolicy | -ex | -ep
    Sets the default execution policy for the current session and saves it in
    the $env:PSExecutionPolicyPreference environment variable. This parameter
    does not change the persistently configured execution policies.
    This parameter only applies to Windows computers. The
    $env:PSExecutionPolicyPreference environment variable does not exist on
    non-Windows platforms.
-InputFormat | -inp | -if
    Describes the format of data sent to PowerShell. Valid values are "Text"
    (text strings) or "XML" (serialized CLIXML format).
-Interactive | -i
    Present an interactive prompt to the user. Inverse for NonInteractive
    parameter.
-Login | -l
    On Linux and macOS, starts PowerShell as a login shell, using /bin/sh to
    execute login profiles such as /etc/profile and ~/.profile. On Windows,
    this switch does nothing.
    [!IMPORTANT] This parameter must come first to start PowerShell as a login
    shell. The parameter is ignored if passed in any other position.
    To set up pwsh as the login shell on UNIX-like operating systems:
    - Verify that the full absolute path to pwsh is listed under /etc/shells
      - This path is usually something like /usr/bin/pwsh on Linux or
        /usr/local/bin/pwsh on macOS
      - With some installation methods, this entry will be added
        automatically at installation time
      - If pwsh is not present in /etc/shells, use an editor to append the
        path to pwsh on the last line. This requires elevated privileges to
        edit.
    - Use the chsh utility to set your current user's shell to pwsh:
        chsh -s /usr/bin/pwsh
    [!WARNING] Setting pwsh as the login shell is currently not supported on
    Windows Subsystem for Linux (WSL), and attempting to set pwsh as the
    login shell there may lead to being unable to start WSL interactively.
-MTA
    Start PowerShell using a multi-threaded apartment. This switch is only
    available on Windows.
-NoExit | -noe
    Does not exit after running startup commands.
    Example: "pwsh -NoExit -Command Get-Date"
-NoLogo | -nol
    Hides the banner text at startup of interactive sessions.
-NonInteractive | -noni
    This switch is used to create sessions that shouldn't require user input.
    This is useful for scripts that run in scheduled tasks or CI/CD pipelines.
    Any attempts to use interactive features, like 'Read-Host' or confirmation
    prompts, result in statement terminating errors rather than hanging.
-NoProfile | -nop
    Does not load the PowerShell profiles.
-NoProfileLoadTime
    Hides the PowerShell profile load time text shown at startup when the load
    time exceeds 500 milliseconds.
-OutputFormat | -o | -of
    Determines how output from PowerShell is formatted. Valid values are "Text"
    (text strings) or "XML" (serialized CLIXML format).
    Example: "pwsh -o XML -c Get-Date"
    When called within a PowerShell session, you get deserialized objects as
    output rather plain strings. When called from other shells, the output is
    string data formatted as CLIXML text.
-SettingsFile | -settings
    Overrides the system-wide "powershell.config.json" settings file for the
    session. By default, system-wide settings are read from the
    "powershell.config.json" in the "$PSHOME" directory.
    Note that these settings are not used by the endpoint specified by the
    "-ConfigurationName" argument.
    Example: "pwsh -SettingsFile c:\myproject\powershell.config.json"
-SSHServerMode | -sshs
    Used in sshd_config for running PowerShell as an SSH subsystem. It is not
    intended or supported for any other use.
-STA
    Start PowerShell using a single-threaded apartment. This is the default.
    This switch is only available on Windows.
```

### `pwsh（示例）`

官方给出的调用示例：`pwsh -h`

```text
root@kali:~# pwsh -h
Usage: pwsh[.exe] [-Login] [[-File] <filePath> [args]]
                  [-Command { - | <script-block> [-args <arg-array>]
                                | <string> [<CommandParameters>] } ]
                  [-CommandWithArgs <string> [<CommandParameters>]
                  [-ConfigurationName <string>] [-ConfigurationFile <filePath>]
                  [-CustomPipeName <string>] [-EncodedCommand <Base64EncodedCommand>]
                  [-ExecutionPolicy <ExecutionPolicy>] [-InputFormat {Text | XML}]
                  [-Interactive] [-MTA] [-NoExit] [-NoLogo] [-NonInteractive] [-NoProfile]
                  [-NoProfileLoadTime] [-OutputFormat {Text | XML}]
                  [-SettingsFile <filePath>] [-SSHServerMode] [-STA]
                  [-Version] [-WindowStyle <style>]
                  [-WorkingDirectory <directoryPath>]
       pwsh[.exe] -h | -Help | -? | /?
PowerShell Online Help https://aka.ms/powershell-docs
All parameters are case-insensitive.
-File | -f
    If the value of File is "-", the command text is read from standard input.
    Running "pwsh -File -" without redirected standard input starts a regular
    session. This is the same as not specifying the File parameter at all.
    This is the default parameter if no parameters are present but values are
    present in the command line. The specified script runs in the local scope
    ("dot-sourced"), so that the functions and variables that the script
    creates are available in the current session. Enter the script file path
    and any parameters. File must be the last parameter in the command, because
    all characters typed after the File parameter name are interpreted as the
    script file path followed by the script parameters.
    Typically, the switch parameters of a script are either included or
    omitted. For example, the following command uses the All parameter of the
    Get-Script.ps1 script file: "-File .\Get-Script.ps1 -All"
    In rare cases, you might need to provide a BOOLEAN value for a switch
    parameter. To provide a BOOLEAN value for a switch parameter in the value
    of the FILE parameter, Use the parameter normally followed immediately by a
    colon and the boolean value, such as the following:
    "-File .\Get-Script.ps1 -All:$False".
    Parameters passed to the script are passed as literal strings, after
    interpretation by the current shell. For example, if you are in cmd.exe and
    want to pass an environment variable value, you would use the cmd.exe
    syntax: "pwsh -File .\test.ps1 -TestParam %windir%"
    In contrast, running "pwsh -File .\test.ps1 -TestParam $env:windir" in
    cmd.exe results in the script receiving the literal string "$env:windir"
    because it has no special meaning to the current cmd.exe shell. The
    "$env:windir" style of environment variable reference can be used inside a
    Command parameter, since there it is interpreted as PowerShell code.
    Similarly, if you want to execute the same command from a Batch script,
    you would use "%~dp0" instead of ".\" or "$PSScriptRoot" to represent the current
    execution directory: "pwsh -File %~dp0test.ps1 -TestParam %windir%". If you
    instead used ".\test.ps1", PowerShell would throw an error because it cannot
    find the literal path ".\test.ps1".
    When the script file invoked terminates with an exit command, the process
    exit code is set to the numeric argument used with the exit command. With
    normal termination, the exit code is always 0.
    Similar to -Command, when a script-terminating error occurs, the exit code
    is set to 1. However, unlike with -Command, when the execution is
    interrupted with Ctrl-C the exit code is 0.
-Command | -c
    Executes the specified commands (and any parameters) as though they were
    typed at the PowerShell command prompt, and then exits, unless the NoExit
    parameter is specified.
    The value of Command can be "-", a script block, or a string. If the value
    of Command is "-", the command text is read from standard input.
    The Command parameter only accepts a script block for execution when it can
    recognize the value passed to Command as a ScriptBlock type. This is only
    possible when running pwsh from another PowerShell host. The ScriptBlock
    type may be contained in an existing variable, returned from an expression,
    or parsed by the PowerShell host as a literal script block enclosed in
    curly braces "{}", before being passed to pwsh.
        pwsh -Command {Get-WinEvent -LogName security}
    In cmd.exe, there is no such thing as a script block (or ScriptBlock type),
    so the value passed to Command will always be a string. You can write a
    script block inside the string, but instead of being executed it will
    behave exactly as though you typed it at a typical PowerShell prompt,
    printing the contents of the script block back out to you.
    A string passed to Command is still executed as PowerShell script, so the
    script block curly braces are often not required in the first place when
    running from cmd.exe. To execute an inline script block defined inside a
    string, the call operator "&" can be used:
        pwsh -Command "& {Get-WinEvent -LogName security}"
    If the value of Command is a string, Command must be the last parameter for
    pwsh, because all arguments following it are interpreted as part of the
    command to execute.
    When called from within an existing PowerShell session, the results are
    returned to the parent shell as deserialized XML objects, not live objects.
    For other shells, the results are returned as strings.
    If the value of Command is "-", the command text is read from standard
    input. You must redirect standard input when using the Command parameter
    with standard input. For example:
        @'
        "in"
        "hi" |
        % { "$_ there" }
        "out"
        '@ | powershell -NoProfile -Command -
    This example produces the following output:
        in
        hi there
        out
    The process exit code is determined by status of the last (executed)
    command within the script block. The exit code is 0 when $? is $true or 1
    when $? is $false. If the last command is an external program or a
    PowerShell script that explicitly sets an exit code other than 0 or 1, that
    exit code is converted to 1 for process exit code. To preserve the specific
    exit code, add exit $LASTEXITCODE to your command string or script block.
    Similarly, the value 1 is returned when a script-terminating
    (runspace-terminating) error, such as a throw or -ErrorAction Stop, occurs
    or when execution is interrupted with Ctrl-C.
-CommandWithArgs | -cwa
    [Experimental]
    Executes a PowerShell command with arguments.  Unlike `-Command`, this
    parameter populates the `$args built-in variable which can be used by the
    command.
    The first string is the command and subsequent strings delimited by whitespace
    are the arguments.
    For example:
        pwsh -CommandWithArgs '$args | % { "arg: $_" }' arg1 arg2
    This example produces the following output:
        arg: arg1
        arg: arg2
-ConfigurationName | -config
    Specifies a configuration endpoint in which PowerShell is run. This can be
    any endpoint registered on the local machine including the default
    PowerShell remoting endpoints or a custom endpoint having specific user
    role capabilities.
    Example: "pwsh -ConfigurationName AdminRoles"
-ConfigurationFile
    Specifies a session configuration (.pssc) file path. The configuration
    contained in the configuration file will be applied to the PowerShell
    session.
    Example: "pwsh -ConfigurationFile "C:\ProgramData\PowerShell\MyConfig.pssc"
-CustomPipeName
    Specifies the name to use for an additional IPC server (named pipe) used
    for debugging and other cross-process communication. This offers a
    predictable mechanism for connecting to other PowerShell instances.
    Typically used with the CustomPipeName parameter on "Enter-PSHostProcess".
    This parameter was introduced in PowerShell 6.2.
    For example:
        # PowerShell instance 1
        pwsh -CustomPipeName mydebugpipe
        # PowerShell instance 2
        Enter-PSHostProcess -CustomPipeName mydebugpipe
-EncodedCommand | -e | -ec
    Accepts a Base64-encoded string version of a command. Use this parameter to
    submit commands to PowerShell that require complex, nested quoting. The
    Base64 representation must be a UTF-16 encoded string.
    For example:
        $command = 'dir "c:\program files" '
        $bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
        $encodedCommand = [Convert]::ToBase64String($bytes)
        pwsh -encodedcommand $encodedCommand
-ExecutionPolicy | -ex | -ep
    Sets the default execution policy for the current session and saves it in
    the $env:PSExecutionPolicyPreference environment variable. This parameter
    does not change the persistently configured execution policies.
    This parameter only applies to Windows computers. The
    $env:PSExecutionPolicyPreference environment variable does not exist on
    non-Windows platforms.
-InputFormat | -inp | -if
    Describes the format of data sent to PowerShell. Valid values are "Text"
    (text strings) or "XML" (serialized CLIXML format).
-Interactive | -i
    Present an interactive prompt to the user. Inverse for NonInteractive
    parameter.
-Login | -l
    On Linux and macOS, starts PowerShell as a login shell, using /bin/sh to
    execute login profiles such as /etc/profile and ~/.profile. On Windows,
    this switch does nothing.
    [!IMPORTANT] This parameter must come first to start PowerShell as a login
    shell. The parameter is ignored if passed in any other position.
    To set up pwsh as the login shell on UNIX-like operating systems:
    - Verify that the full absolute path to pwsh is listed under /etc/shells
      - This path is usually something like /usr/bin/pwsh on Linux or
        /usr/local/bin/pwsh on macOS
      - With some installation methods, this entry will be added
        automatically at installation time
      - If pwsh is not present in /etc/shells, use an editor to append the
        path to pwsh on the last line. This requires elevated privileges to
        edit.
    - Use the chsh utility to set your current user's shell to pwsh:
        chsh -s /usr/bin/pwsh
    [!WARNING] Setting pwsh as the login shell is currently not supported on
    Windows Subsystem for Linux (WSL), and attempting to set pwsh as the
    login shell there may lead to being unable to start WSL interactively.
-MTA
    Start PowerShell using a multi-threaded apartment. This switch is only
    available on Windows.
-NoExit | -noe
    Does not exit after running startup commands.
    Example: "pwsh -NoExit -Command Get-Date"
-NoLogo | -nol
    Hides the banner text at startup of interactive sessions.
-NonInteractive | -noni
    This switch is used to create sessions that shouldn't require user input.
    This is useful for scripts that run in scheduled tasks or CI/CD pipelines.
    Any attempts to use interactive features, like 'Read-Host' or confirmation
    prompts, result in statement terminating errors rather than hanging.
-NoProfile | -nop
    Does not load the PowerShell profiles.
-NoProfileLoadTime
    Hides the PowerShell profile load time text shown at startup when the load
    time exceeds 500 milliseconds.
-OutputFormat | -o | -of
    Determines how output from PowerShell is formatted. Valid values are "Text"
    (text strings) or "XML" (serialized CLIXML format).
    Example: "pwsh -o XML -c Get-Date"
    When called within a PowerShell session, you get deserialized objects as
    output rather plain strings. When called from other shells, the output is
    string data formatted as CLIXML text.
-SettingsFile | -settings
    Overrides the system-wide "powershell.config.json" settings file for the
    session. By default, system-wide settings are read from the
    "powershell.config.json" in the "$PSHOME" directory.
    Note that these settings are not used by the endpoint specified by the
    "-ConfigurationName" argument.
    Example: "pwsh -SettingsFile c:\myproject\powershell.config.json"
-SSHServerMode | -sshs
    Used in sshd_config for running PowerShell as an SSH subsystem. It is not
    intended or supported for any other use.
-STA
    Start PowerShell using a single-threaded apartment. This is the default.
    This switch is only available on Windows.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install powershell`，再执行 `powershell --version` 2>/dev/null || `powershell -V`
- [ ] **2.** **读官方帮助** —— `powershell -h`，需要细节时 `man powershell`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: pwsh[.exe] [-Login] [[-File] <filePath> [args]]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/powershell/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[powershell-empire](../../tools/tutorials/08-后渗透/powershell-empire.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/powershell/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/powershell/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
