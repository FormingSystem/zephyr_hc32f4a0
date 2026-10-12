<!-- SPDX-License-Identifier: Apache-2.0 -->

# P005 Windows 完整操作

对应 [正文](../../P005_Zephyr工程组织与驱动模型_Windows.md)。使用 Windows MSYS2 UCRT64；每个 TXT 是一个可独立恢复目录和必要环境的操作单元。按正文正在进行的阶段选择，不能把整个目录串行执行。只读检查、下载、创建文件和构建分别说明；已有工作区、HAL 与自有文件优先复用。

| 完整操作 | 正文 | 用途 |
| --- | --- | --- |
| [check-baseline-inputs.txt](check-baseline-inputs.txt) | [5.3.3](../../P005_Zephyr工程组织与驱动模型_Windows.md#section-5-3-3) | 只读核对官方 MPS2 baseline 的已有输入 |
| [build-baseline-west.txt](build-baseline-west.txt) | [5.3.3](../../P005_Zephyr工程组织与驱动模型_Windows.md#section-5-3-3) | 用 west 构建官方 hello_world 与 MPS2/AN386 |
| [build-baseline-cmake.txt](build-baseline-cmake.txt) | [5.3.3](../../P005_Zephyr工程组织与驱动模型_Windows.md#section-5-3-3) | 官方 MPS2 baseline 的直接 CMake 分支 |
| [trace-mps2-source.txt](trace-mps2-source.txt) | [5.3.5](../../P005_Zephyr工程组织与驱动模型_Windows.md#section-5-3-5) | 只读定位 MPS2 UART 硬件实现 |
| [read-cmsis-adapter.txt](read-cmsis-adapter.txt) | [5.4.2](../../P005_Zephyr工程组织与驱动模型_Windows.md#section-5-4-2) | 只读查看 board、SoC 与 CMSIS 接入原文件 |
| [inspect-manifest-selection.txt](inspect-manifest-selection.txt) | [5.4.1](../../P005_Zephyr工程组织与驱动模型_Windows.md#section-5-4-1) | 对照完整清单与当前 CMSIS 项目的身份、版本和路径 |
| [trace-baseline-build.txt](trace-baseline-build.txt) | [5.3.7](../../P005_Zephyr工程组织与驱动模型_Windows.md#section-5-3-7) | 反查 MPS2 baseline 的硬件与源文件选择 |
| [check-driver-model-evidence.txt](check-driver-model-evidence.txt) | [5.5](../../P005_Zephyr工程组织与驱动模型_Windows.md#section-5-5) | 只读核对 Kconfig 来源、生成宏与编译命令 |

先核对 P001—P004 的输入，再选择 west 或 CMake baseline 构建入口。反查命令只读取已有输出。CMSDK 源文件读取与 CMSIS 接入规则读取不修改官方源码。
