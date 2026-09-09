<!--
SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
SPDX-License-Identifier: Apache-2.0
-->

# 板级组件

此目录已通过 `zephyr/module.yml` 注册为外部 board root。
当前没有可构建的 HC32 板级目标，也没有用于冒充实板支持的 `board.yml`。
`mps2/an386` 验证的是模块加载、工具链和示例运行。

目标板为 UYUP-RPI-A-2.5，芯片为 HC32F4A0PITB / LQFP100，
2 MiB Flash、512 KiB 系统 SRAM，板载主晶振为 **12 MHz**。
未引出管脚按 NC 处理。USART1 的 TX/RX 使用 PA9/PA10；
PD10 蓝灯与 PE15 绿灯均为低有效。

未来按当前 Zephyr hardware model v2 建立板目录，包含 `board.yml`、
`Kconfig.<board>`、DTS、defconfig 和 pyOCD runner 配置。
对应 SoC 和基础驱动可构建后再发布板目标；调试、下载和实板验证另行记录。

板载 CMSIS-DAP 默认为 2.x / WinUSB，支持 10 MHz SWD，
一根 USB 线提供调试与串口输出。使用外部调试器前停用板载 DAP：
关电、按住复位、开电、松开复位；完整操作两次，橙灯不闪表示已停用。
