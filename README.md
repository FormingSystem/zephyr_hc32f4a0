<!--
SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
SPDX-License-Identifier: Apache-2.0
-->

# zephyr_hc32f4a0

文档仓库与从零实验的分工、逐步形成完整工程的目标，以及尚未确定的更新需求，见[两个目录的职责](project-docs/workspace-roles.md)。

本仓库用于维护和推送 Zephyr 学习文档、PPT、环境资料与移植记录。`learning/` 面向读者从零复现，实验统一在 `G:\zephyr_practice\zephyr-main` 中进行；文档保存目录不是实验执行目录。

仓库保留完整 Zephyr 源码及已经完成的 HC32F4A0 移植实现，作为早期移植参考和对照组：从零复现出现问题时可对照定位，也可比较新增、修改的文件来理解移植范围。G 盘实验工程将随着实验逐步形成与本仓库一致的目录、板级适配、工具和文档组织，支持两边对照和适配。对照的目标是工程形态和功能逐步一致，不预设两边源码版本或 Git 历史已经相同。具体构建和实板验证证据仍按下述状态记录区分。
内核、架构、驱动框架、设备树、构建系统，以及 CMSIS_6 和华大 HAL 源码都在本仓库内；
工程使用自己的 Git 历史。源码来源和版本见 [源码基线](project-docs/source-baseline.md)。

当前已实现 HC32 SoC、板级设备树、GPIO、轮询 USART1 与 USBFS CDC ACM，默认构建目标为
`uyup_rpi_a/hc32f4a0pitb`。实装晶振仍为 12 MHz，当前板级使用 PLLH 生成 48 MHz 系统及 USB 时钟；
12 MHz 直驱是早期 GPIO/UART 教学阶段。USB1 日志构建和 COM 使用见 [USB 控制台示例](samples/usb_console/README.md)；`printf` / `scanf` 交互见 [USB 标准输入输出示例](samples/usb_stdio/README.md)。
编译结果与实板验证状态分别记录在 [移植状态](project-docs/porting-status.md)。

## 阅读文档与使用移植参照

从零实验先读[学习中心](learning/README.md)和[实验准备](learning/P000_实验准备.md)。以下入口介绍保留的移植实现与环境资料，供维护和故障对照使用。

了解这份参照工程时，先读[从哪里开始学习](project-docs/learning/开始学习.md)，按阅读顺序完成第一次软件实验。

第一次接触本工程，可以先按[四篇入门介绍](project-docs/README.md)的顺序认识工程、运行过程、构建和芯片移植。
随后沿[Zephyr 学习与实验路线](project-docs/learning/README.md)逐篇深入；完整蓝图规划了 14 组、88 个专题，
分别说明前置知识、实验目标与平台条件。第一组 T01—T06 已完成正文与相应实验，
从[版本与证据](project-docs/learning/evidence/README.md)开始，具体结果见[第一组验收记录](project-docs/learning/第一组验收记录.md)。

打开本仓库的 [VS Code 工作区](zephyr_hc32f4a0.code-workspace)。工作区只有本仓库一个根目录，
可以直接查看和修改 Zephyr 全部源码及 HC32 组件。工程任务通过根目录 `.venv` 和 Python 入口配置环境。

Python 环境隔离与 west 的专题入门、常用命令及本地实验见 [工具学习中心](learning/README.md)，
主线采用 UCRT64 Bash。项目自身的用法分别见 [Python 环境](project-docs/python/venv/README.md)
和 [west 的项目边界](project-docs/west/README.md)。

从 Windows 终端安装、国内换源和源码下载开始，可读[Zephyr 下载与工程准备](learning/P01_zephyr_make_project/大纲.md)，配有可编辑教学课件。

新机器先按[下载与安装说明](project-docs/environment.md)取得本工程、安装主机工具和 SDK，再建立根目录 `.venv`。
Windows 读者可在工程根运行 `setup-windows.cmd`，选择中英文、安装目录与镜像后自动准备工具；
教学前的完整 MSYS2 备份、教学后恢复及环境变量回退见[Windows 一键环境](project-docs/windows-bootstrap.md)。
已有开发环境时，在仓库根目录的 UCRT64 Bash 执行：

```bash
source .venv/Scripts/activate
python scripts/configure_west.py
python scripts/project_env.py doctor
python scripts/project_env.py check
python scripts/project_env.py build
```

`build` 直接使用本仓库的 CMake 构建系统与内置模块，不要求外部 west 工作区。
HC32 固件输出到 `build/bringup/zephyr/`，编译数据库为 `build/bringup/compile_commands.json`。
QEMU 软件回归使用独立目标：

```bash
python scripts/project_env.py test
```

该测试运行 `mps2/an386`，用于软件回归；HC32 实板下载和运行另行验证。

west 使用 [project-west.yml](project-west.yml)，详细配置见[项目 west](project-docs/west/README.md)。
新 GitHub 仓库给别人克隆时，提交源码、依赖说明和初始化脚本，由对方安装工具，见[发布与重建](project-docs/distribution.md)。
新增源文件/模块、VS Code 单步调试与板级适配的实验入口见[学习中心](learning/README.md)。
完整日常命令、调试与板卡操作见 [开发文档](project-docs/development.md)。

## 目录

| 位置 | 内容 |
| --- | --- |
| `kernel/`、`arch/`、`include/`、`subsys/`、`cmake/` | Zephyr 内核、架构、接口、子系统和构建源码 |
| `modules/hal/cmsis_6/`、`modules/hal/xhsc/` | 当前 ARM/HC32 构建使用的完整模块源码快照 |
| `soc/xhsc/hc32f4a0/` | HC32 启动、12 MHz 晶振时钟、ICG 布局与 DDL 集成 |
| `boards/uyup/`、`dts/arm/xhsc/` | UYUP 板卡、HC32 SoC 及存储/引脚描述 |
| `drivers/` | Zephyr 驱动框架与本工程 GPIO/USART 实现 |
| `samples/bringup/` | 控制台与 GPIO 心跳示例 |
| `samples/learning/`、`tests/learning/` | 编译观察、对象边界与断言等课程实验 |
| [`scripts/learning/`](scripts/learning/README.md) | 学习应用构建、模拟运行与证据记录入口 |
| `debug/` | 10 MHz SWD 配置、SRAM 地址修正及离线检查 |
| `scripts/`、`tests/tooling/` | 环境入口、工程命令和工具回归 |
| [`project-docs/`](project-docs/README.md) | 工程介绍、移植记录和 Zephyr 学习资料 |
| [`learning/`](learning/README.md) | 环境工具知识、构建调试与板级配置的可运行实验 |
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
