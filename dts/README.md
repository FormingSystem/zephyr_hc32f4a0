<!--
SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
SPDX-License-Identifier: Apache-2.0
-->

# Devicetree 组件

此目录已通过模块设置注册为外部 DTS root。当前没有 HC32 DTS、binding 或
管脚复用定义；示例读取所选 Zephyr 平台本身的 devicetree。

未来 SoC 描述放在 `dts/arm/xhsc/`，驱动绑定按外设类别放在
`dts/bindings/`。板级 DTS 定义 12 MHz 主晶振、实际连接的 UART、LED 和按键，
不把 UYUP 原理图的通用 STM32 符号当作 HC32 外设或管脚定义。

芯片未引出的功能按 NC 处理，不创建可用的 pinctrl 状态。
SoC 描述区分 2 MiB Flash、从 `0x1FFE0000` 开始的 512 KiB 系统 SRAM、
独立 4 KiB 备份 SRAM。新厂商兼容串接入时同时落实 vendor prefix 与 binding。
