<!--
SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
SPDX-License-Identifier: Apache-2.0
-->

# 工程文档与 Zephyr 学习资料

`project-docs/` 用于维护本工程的介绍、开发说明、移植记录，以及后续整理的 Zephyr 学习笔记和资料索引。
仓库的 `doc/` 保存 Zephyr 上游文档源码。

| 文档 | 内容 |
| --- | --- |
| [工程概览](../README.md) | 项目目标、开发入口与源码目录 |
| [组件架构](architecture.md) | 工程组织、启动过程、驱动与调试边界 |
| [开发与调试](development.md) | 环境准备、构建、VS Code 和板卡调试 |
| [硬件依据](hardware.md) | 芯片资源、引脚、时钟与板载 DAP 操作 |
| [移植状态](porting-status.md) | 已实现能力、验证结果与后续工作 |
| [源码基线](source-baseline.md) | Zephyr、CMSIS 和厂商 HAL 的来源节点与导入范围 |

后续工程介绍和 Zephyr 专题资料可在本目录新增 Markdown 文件，并在此维护入口。
学习资料注明适用版本与来源；涉及本板硬件的事实引用[硬件依据](hardware.md)，验证结果更新到[移植状态](porting-status.md)。
