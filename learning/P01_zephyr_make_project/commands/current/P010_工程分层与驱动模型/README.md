# P010_工程分层与驱动模型：当前命令索引

命令逐块取自[当前正文](../../../P010_工程分层与驱动模型.md)。先读对应小节，只执行所选分支。

| 操作 | 终端 | 所属讲解 | 内容 |
| --- | --- | --- | --- |
| 001 | bash | 9.1.1_先找声明文件，不把目标名当作目录 | [完整命令](001-bash.txt) |
| 002 | bash | 9.3.3_沿用官方应用，明确本教程选择 AN386 | [完整命令](002-bash.txt) |
| 003 | bash | 9.3.3_沿用官方应用，明确本教程选择 AN386 | [完整命令](003-bash.txt) |
| 004 | bash | 9.3.3_沿用官方应用，明确本教程选择 AN386 | [完整命令](004-bash.txt) |
| 005 | bash | 9.3.7_反查同一次构建的记录 | [完整命令](005-bash.txt) |
| 006 | bash | 9.4.1_清单管理源码，构建记录证明使用 | [完整命令](006-bash.txt) |
| 007 | bash | 9.5_把配置来源、选源与设备调用放回同一条链 | [完整命令](007-bash.txt) |

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
