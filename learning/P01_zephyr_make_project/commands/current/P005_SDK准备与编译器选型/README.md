# P005_SDK准备与编译器选型：当前命令索引

命令逐块取自[当前正文](../../../P005_SDK准备与编译器选型.md)。先读正文前提，只执行所选环境与路线，不批量执行本目录。

| 操作 | 终端 | 所属讲解 | 内容 |
| --- | --- | --- | --- |
| 001 | bash | 4.2.1_从当前源码确定版本，再选主机与目标 | [完整命令](001-bash.txt) |
| 002 | bash | 4.2.2_GNU 与 Minimal 二选一解压 | [完整命令](002-bash.txt) |
| 003 | bash | 4.2.2_GNU 与 Minimal 二选一解压 | [完整命令](003-bash.txt) |
| 004 | powershell | 4.2.3_Minimal 补 ARM：在线或已有归档二选一 | [完整命令](004-powershell.txt) |
| 005 | bash | 4.2.3_Minimal 补 ARM：在线或已有归档二选一 | [完整命令](005-bash.txt) |
| 006 | bash | 4.2.4_核验安装结果 | [完整命令](006-bash.txt) |
| 007 | powershell | 4.2.5_PowerShell 原生路线安装完整 GNU 包 | [完整命令](007-powershell.txt) |
| 008 | powershell | 4.3.2_可选注册：当前 Windows 用户的自动发现 | [完整命令](008-powershell.txt) |
| 009 | bash | 4.3.3_不注册：环境变量传给当前终端启动的 CMake | [完整命令](009-bash.txt) |
| 010 | bash | 4.3.3_不注册：环境变量传给当前终端启动的 CMake | [完整命令](010-bash.txt) |
| 011 | bash | 4.3.4_不注册：在完整应用配置命令中传入 SDK 根 | [完整命令](011-bash.txt) |
| 012 | bash | 4.4.2_可选路线：保持独立 ARM 目录 | [完整命令](012-bash.txt) |
| 013 | bash | 4.4.2_可选路线：保持独立 ARM 目录 | [完整命令](013-bash.txt) |
| 014 | bash | 4.5_验证工程选用的工具并继续下一阶段 | [完整命令](014-bash.txt) |
| 015 | bash | 4.5.2_转入 west 下载前的 Git 检查 | [完整命令](015-bash.txt) |

## 配套完整操作

下列操作保留已验证实验的目录名，按当前正文前提选择；不能批量执行。与上面的逐块命令相比，它们包含创建文件或恢复必要环境的完整过程。

| 操作 | 说明 |
| --- | --- |
| [sdk-arm-offline.txt](complete/sdk-arm-offline.txt) | Windows UCRT64；Minimal 已解压；ARM 包来自同版 Release。 |
| [sdk-arm-online.txt](complete/sdk-arm-online.txt) | Windows PowerShell；Minimal 已解压，且尚未安装 ARM 工具链。 |
| [sdk-configure.txt](complete/sdk-configure.txt) | Windows UCRT64；完成 P004 主机环境与 P006 模块准备后执行；新构建目录。 |
| [sdk-environment.txt](complete/sdk-environment.txt) | Windows UCRT64；源码根；可选：把 SDK 根交给本窗口启动的 CMake。 |
| [sdk-evidence.txt](complete/sdk-evidence.txt) | Windows UCRT64；源码依赖齐全且 5.3.4 的 CMake 配置成功后，才有这些产物。 |
| [sdk-gnu.txt](complete/sdk-gnu.txt) | Windows UCRT64；下载目录；已取得 GNU 包与同版 sha256.sum。 |
| [sdk-minimal.txt](complete/sdk-minimal.txt) | Windows UCRT64；下载目录；选择 Minimal 才执行。 |
| [sdk-register.txt](complete/sdk-register.txt) | Windows PowerShell；可选：准备当前用户的自动发现入口。 |
| [sdk-standalone.txt](complete/sdk-standalone.txt) | Windows UCRT64；完成 P004—P010；已解压同版独立 ARM 包。 |
| [sdk-verify.txt](complete/sdk-verify.txt) | Windows UCRT64；GNU 或 Minimal + ARM 均用相同目录核验。 |
| [west-git-check.txt](complete/west-git-check.txt) | Windows UCRT64；实验源码根；先激活 P004 创建的 Windows Python 环境。 |
