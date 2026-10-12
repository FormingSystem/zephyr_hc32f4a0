---
id: zephyr-p006-command-index
title: P006 Windows 命令索引
kind: reference
status: evolving
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# P006 Windows 完整操作

对应 [正文](../../P006_HC32与外部源码模块接入_Windows.md)。使用 Windows MSYS2 UCRT64；每个 TXT 是一个可独立恢复目录和必要环境的操作单元。按正文正在进行的阶段选择，不能把整个目录串行执行。只读检查、下载、创建文件和构建分别说明；已有工作区、HAL 与自有文件优先复用。

| 完整操作 | 正文 | 用途 |
| --- | --- | --- |
| [query-hal-project.txt](query-hal-project.txt) | [6.3](../../P006_HC32与外部源码模块接入_Windows.md#section-6-3) | 只读确认当前清单是否声明 hal_xhsc |
| [download-hal-fixed.txt](download-hal-fixed.txt) | [6.3](../../P006_HC32与外部源码模块接入_Windows.md#section-6-3) | 没有可复用 HAL 时下载固定修订 |
| [check-hal-files.txt](check-hal-files.txt) | [6.3](../../P006_HC32与外部源码模块接入_Windows.md#section-6-3) | 选择已有 HAL 根并核对模块入口及器件文件 |
| [verify-hal-revision.txt](verify-hal-revision.txt) | [6.3](../../P006_HC32与外部源码模块接入_Windows.md#section-6-3) | 选择实际 HAL 根并核对 Git 或原归档版本依据 |
| [fetch-hal-if-missing.txt](fetch-hal-if-missing.txt) | [6.3.1](../../P006_HC32与外部源码模块接入_Windows.md#section-6-3-1) | 检查两个常用目录后才下载 HAL 的分支 |
| [discover-default-modules.txt](discover-default-modules.txt) | [6.5.5](../../P006_HC32与外部源码模块接入_Windows.md#section-6-5-5) | 读取默认 west 项目的模块发现结果 |
| [discover-extra-hal.txt](discover-extra-hal.txt) | [6.5.5](../../P006_HC32与外部源码模块接入_Windows.md#section-6-5-5) | 在已核验 HAL 后检查额外模块发现 |
| [copy-hc32-port.txt](copy-hc32-port.txt) | [6.6.1](../../P006_HC32与外部源码模块接入_Windows.md#section-6-6-1) | 复制教材适配为工作副本，不覆盖现有目录 |
| [build-hc32-west.txt](build-hc32-west.txt) | [6.6.4](../../P006_HC32与外部源码模块接入_Windows.md#section-6-6-4) | HC32 全部前提就绪后用 west 构建 |
| [build-hc32-cmake.txt](build-hc32-cmake.txt) | [6.6.4](../../P006_HC32与外部源码模块接入_Windows.md#section-6-6-4) | 相同 HC32 输入的直接 CMake 构建 |
| [build-hc32-manual-modules.txt](build-hc32-manual-modules.txt) | [6.6.4](../../P006_HC32与外部源码模块接入_Windows.md#section-6-6-4) | HC32 显式 CMSIS、HAL 与适配模块列表 |
| [create-greeting-component.txt](create-greeting-component.txt) | [6.7.1](../../P006_HC32与外部源码模块接入_Windows.md#section-6-7-1) | 创建普通组件，已有目标不覆盖 |
| [create-component-application.txt](create-component-application.txt) | [6.7.5](../../P006_HC32与外部源码模块接入_Windows.md#section-6-7-5) | 创建调用组件的独立应用，已有目标不覆盖 |
| [build-component-on.txt](build-component-on.txt) | [6.7.7](../../P006_HC32与外部源码模块接入_Windows.md#section-6-7-7) | 构建启用 app_greeting 的应用 |
| [check-component-on.txt](check-component-on.txt) | [6.7.9](../../P006_HC32与外部源码模块接入_Windows.md#section-6-7-9) | 检查组件开启时的发现、配置、源码和 ELF |
| [build-component-off.txt](build-component-off.txt) | [6.7.10](../../P006_HC32与外部源码模块接入_Windows.md#section-6-7-10) | 保留开启版，独立构建关闭组件的应用 |
| [check-component-off.txt](check-component-off.txt) | [6.7.10](../../P006_HC32与外部源码模块接入_Windows.md#section-6-7-10) | 检查组件仍被发现而源文件已关闭 |
| [build-component-manual-modules.txt](build-component-manual-modules.txt) | [6.7.11](../../P006_HC32与外部源码模块接入_Windows.md#section-6-7-11) | 显式提供完整模块列表的 CMake 分支 |

HAL 两种首次获取块二选一，已有目录不重复克隆。copy-hc32-port 先检查目标不存在；HC32 三种构建入口均要求该工作副本、HAL、CMSIS 与 SDK 已齐全。普通组件先创建模块和应用，再构建开启/关闭版本，最后才选择手管完整模块列表分支。
