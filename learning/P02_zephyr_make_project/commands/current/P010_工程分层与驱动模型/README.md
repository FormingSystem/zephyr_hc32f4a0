# P010_工程分层与驱动模型：当前命令索引

按[本章两种构建入口的准备条件](../../../P010_工程分层与驱动模型.md#section-10-1-1)设置终端后，选择 [west 工作区构建](001-bash.txt)或[本地归档的 CMake 配置与构建](complete/build-an386-local-cmake.txt)。两条命令路线均从 Zephyr 源码根选取 `samples/hello_world`。

| 操作 | 终端 | 所属讲解 | 内容 |
| --- | --- | --- | --- |
| 001 | UCRT64 | [10.1.1_为 hello_world 选择开发板](../../../P010_工程分层与驱动模型.md#section-10-1-1) | [完整命令](001-bash.txt) |
| 002 | bash | [10.3.3_构建 AN386 控制台示例](../../../reference/MPS2串口构建与驱动源码实验.md#section-10-3-3) | [完整命令](002-bash.txt) |
| 003 | bash | [10.3.3_构建 AN386 控制台示例](../../../reference/MPS2串口构建与驱动源码实验.md#section-10-3-3) | [完整命令](003-bash.txt) |
| 004 | bash | [10.3.3_构建 AN386 控制台示例](../../../reference/MPS2串口构建与驱动源码实验.md#section-10-3-3) | [完整命令](004-bash.txt) |
| 005 | bash | [10.3.7_反查同一次构建的记录](../../../reference/MPS2串口构建与驱动源码实验.md#section-10-3-7) | [完整命令](005-bash.txt) |
| 006 | bash | [10.4.1_清单管理源码，构建记录证明使用](../../../reference/MPS2串口构建与驱动源码实验.md#section-10-4-1) | [完整命令](006-bash.txt) |
| 007 | bash | [串口驱动的配置来源与编译记录](../../../reference/MPS2串口构建与驱动源码实验.md#section-10-5) | [完整命令](007-bash.txt) |

## 配套完整操作

下列操作保留已验证实验的目录名，按当前正文前提选择；不能批量执行。与上面的逐块命令相比，它们包含创建文件或恢复必要环境的完整过程。

| 操作 | 说明 |
| --- | --- |
| [locate-target-files.txt](complete/locate-target-files.txt) | P010 10.1.1：从目标名定位板、SoC 与架构选择 |
| [build-baseline-cmake.txt](complete/build-baseline-cmake.txt) | P010 10.3.3：官方 MPS2 baseline 的直接 CMake 分支 |
| [build-baseline-west.txt](complete/build-baseline-west.txt) | P010 10.3.3：用 west 构建官方 hello_world 与 MPS2/AN386 |
| [check-baseline-inputs.txt](complete/check-baseline-inputs.txt) | P010 10.3.3：只读核对官方 MPS2 baseline 的已有输入 |
| [check-driver-model-evidence.txt](complete/check-driver-model-evidence.txt) | P010 10.5：只读核对 Kconfig 来源、生成宏与编译命令 |
| [inspect-manifest-selection.txt](complete/inspect-manifest-selection.txt) | P010 10.4.1：只读对照完整清单与 CMSIS 的实际项目身份 |
| [read-cmsis-adapter.txt](complete/read-cmsis-adapter.txt) | P010 10.4.2：只读查看 board、SoC 与 CMSIS 接入原文件 |
| [trace-baseline-build.txt](complete/trace-baseline-build.txt) | P010 10.3.7：反查 MPS2 baseline 的硬件与源文件选择 |
| [trace-mps2-source.txt](complete/trace-mps2-source.txt) | P010 10.3.5：只读定位 MPS2 UART 硬件实现 |
