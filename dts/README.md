<!--
SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
SPDX-License-Identifier: Apache-2.0
-->

# HC32 Devicetree 组件

本目录属于仓库内完整 Zephyr 源码树。HC32 当前实现包括：

| 文件 | 描述 |
| --- | --- |
| [`arm/xhsc/hc32f4a0.dtsi`](arm/xhsc/hc32f4a0.dtsi) | Cortex-M4F、NVIC、SysTick、GPIO 端口和 USART1 寄存器节点 |
| [`arm/xhsc/hc32f4a0pitb.dtsi`](arm/xhsc/hc32f4a0pitb.dtsi) | 2 MiB Flash、`0x1FFE0000` 起点的 512 KiB SRAM、LQFP100 GPIO 保留范围 |
| [`bindings/gpio/xhsc,hc32-gpio.yaml`](bindings/gpio/xhsc,hc32-gpio.yaml) | GPIO 端口索引和 GPIO specifier |
| [`bindings/serial/xhsc,hc32-uart.yaml`](bindings/serial/xhsc,hc32-uart.yaml) | UART 端口、TX/RX 引脚和串口格式 |

板级文件位于 `boards/uyup/uyup_rpi_a/`，对应目标
**`uyup_rpi_a/hc32f4a0pitb`**。它声明板载 12 MHz 晶振并以 XTAL 直驱，不启用 PLL，
启用 USART1 PA9/PA10、低有效 PD10/PE15 LED 和 PA3/PE2 按键。

LQFP100 实际引出 PA0..PA15、PB0..PB15、PC0..PC15、PD0..PD15、PE0..PE15、
PH0、PH1 和 PI13。其他槽位全部按 NC 处理，通过 `gpio-reserved-ranges` 排除。
PF/PG、晶振端口 PH 和启动模式端口 PI 在板级 GPIO 配置中保持禁用；PH0/PH1
由时钟初始化配置，不通过通用 GPIO 设备操作。

备份 SRAM 的 4 KiB 不并入默认主 SRAM。Flash `0x400` 的 ICG 由 SoC 链接配置固定，
不作为应用数据区使用。厂商兼容串在 `bindings/vendor-prefixes.txt` 登记。

当前 UART/GPIO 未实现外设中断路由，不在 DTS 中虚构外设事件源与 NVIC 槽号映射。
原理图的通用 STM32 符号不作为 HC32 引脚和实例号依据，实板运行结果仍需另行验收。
