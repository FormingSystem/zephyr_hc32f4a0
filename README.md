<!--
SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
SPDX-License-Identifier: Apache-2.0
-->

# zephyr_hc32f4a0

这是包含完整 Zephyr 源码的 HC32F4A0PITB / UYUP-RPI-A-2.5 开发仓库。
内核、架构、驱动框架、设备树、构建系统，以及 CMSIS_6 和华大 HAL 源码都在本仓库内；
工程使用自己的 Git 历史。源码来源和版本见 [源码基线](project-docs/source-baseline.md)。

当前已实现 HC32 SoC、板级设备树、GPIO 与轮询 USART1 控制台，默认构建目标为
`uyup_rpi_a/hc32f4a0pitb`。首版使用板载 12 MHz 晶振直接驱动系统时钟，不启用 PLL。
编译结果与实板验证状态分别记录在 [移植状态](project-docs/porting-status.md)。

## 开始开发

第一次接触本工程，可以先按[四篇入门介绍](project-docs/README.md)的顺序认识工程、运行过程、构建和芯片移植。

打开本仓库的 [VS Code 工作区](zephyr_hc32f4a0.code-workspace)。工作区只有本仓库一个根目录，
可以直接查看和修改 Zephyr 全部源码及 HC32 组件。新终端和工程任务会加载本仓库环境。

已有开发环境时，在仓库根目录执行：

```powershell
. ./scripts/Enter-Environment.ps1
python scripts/git_setup.py
python scripts/project.py doctor
python scripts/project.py check
python scripts/project.py build
```

`build` 直接使用本仓库的 CMake 构建系统与内置模块，不要求外部 west 工作区。
HC32 固件输出到 `build/bringup/zephyr/`，编译数据库为 `build/bringup/compile_commands.json`。
QEMU 软件回归使用独立目标：

```powershell
python scripts/project.py test
```

该测试运行 `mps2/an386`，用于软件回归；HC32 实板下载和运行另行验证。

新机器先准备 Zephyr SDK 和主机工具，再运行 `scripts/Setup-Environment.ps1 -SdkRoot <SDK目录>`。
该脚本创建仓库内 `.venv`、安装工程与 Zephyr 基础 Python 依赖，并保存本机 SDK 配置。
完整命令、调试与板卡操作见 [开发文档](project-docs/development.md)。

## 目录

| 位置 | 内容 |
| --- | --- |
| `kernel/`、`arch/`、`include/`、`subsys/`、`cmake/` | Zephyr 内核、架构、接口、子系统和构建源码 |
| `modules/hal/cmsis_6/`、`modules/hal/xhsc/` | 当前 ARM/HC32 构建使用的完整模块源码快照 |
| `soc/xhsc/hc32f4a0/` | HC32 启动、12 MHz 晶振时钟、ICG 布局与 DDL 集成 |
| `boards/uyup/`、`dts/arm/xhsc/` | UYUP 板卡、HC32 SoC 及存储/引脚描述 |
| `drivers/` | Zephyr 驱动框架与本工程 GPIO/USART 实现 |
| `samples/bringup/` | 控制台与 GPIO 心跳示例 |
| `debug/` | 10 MHz SWD 配置、SRAM 地址修正及离线检查 |
| `scripts/`、`tests/tooling/` | 环境入口、工程命令和工具回归 |
| [`project-docs/`](project-docs/README.md) | 工程介绍、移植记录和 Zephyr 学习资料 |
| `governance/` | Git 协作框架 |
| `doc/` | Zephyr 上游文档源码 |

本机 SDK、虚拟环境、`.local/` 和 `build/` 不提交。导入源码保留原许可证；自研实现采用
Apache-2.0，治理框架的来源和许可见 [框架来源](governance/architecture/framework_provenance.md)。

- [工程文档与学习资料](project-docs/README.md)
- [组件架构](project-docs/architecture.md)
- [硬件事实与操作](project-docs/hardware.md)
- [开发与调试](project-docs/development.md)
- [移植状态](project-docs/porting-status.md)
- [Git 规范](governance/conventions/git_guide.md)
