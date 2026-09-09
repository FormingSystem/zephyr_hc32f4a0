<!--
SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
SPDX-License-Identifier: Apache-2.0
-->

# Zephyr 驱动组件

本目录由模块根目录的 CMake 和 Kconfig 接入。当前没有 HC32 驱动实现；
示例使用所选 Zephyr 平台已有的控制台和 GPIO 驱动。

驱动按 Zephyr 外设类别组织，例如 `gpio/`、`serial/`、`clock_control/`、
`pinctrl/` 和 `interrupt_controller/`。每个已实现类别独立提供 CMake/Kconfig，
其 devicetree binding 放在 `dts/bindings/`，不在应用中直接调用板商整套 BSP。

HC32 DDL 依赖由外部 `hal_xhsc` 模块提供。未来驱动使用所需的
`HC32_LL_*` 配置选择源文件，SoC 集成负责 `HAS_HC32_DDL` 等配置；
当前没有启用该 HAL 或复制供应商代码。

首次实板驱动顺序为安全时钟、管脚复用、GPIO、USART1 控制台与中断路由。
板载晶振为 12 MHz，未引出管脚按 NC 处理。时钟、Flash 等待周期和总线分频
必须完成核对后再接入 PLL。
