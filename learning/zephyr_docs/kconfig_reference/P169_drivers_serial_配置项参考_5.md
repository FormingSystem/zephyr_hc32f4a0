---
id: learning.zephyr-docs.kconfig-reference.page-169
title: "`drivers/serial`配置项参考（5/5）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第169章\_`drivers/serial`配置项参考（5/5）

本章翻译官方 Kconfig 数据库中 `drivers/serial` 的 45 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_UART_SIFIVE_PORT_1_RXCNT_IRQ"></a>

## 169.1 `CONFIG_UART_SIFIVE_PORT_1_RXCNT_IRQ`

**提示（Prompt）**：端口 0 接收中断阈值计数（RX Interrupt Threshold Count）

**说明（Help）**

端口 1 触发接收 FIFO（RX FIFO）中断的接收阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_SIFIVE_PORT_1 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/serial/Kconfig.sifive:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.sifive#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → SiFive Freedom 串行驱动（Serial Driver） → SIFIVE 端口 1（Port 1）

**配置项引用（Symbol References）**：[`CONFIG_UART_SIFIVE_PORT_1`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_SIFIVE_PORT_1)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_SIFIVE_PORT_1_TXCNT_IRQ"></a>

## 169.2 `CONFIG_UART_SIFIVE_PORT_1_TXCNT_IRQ`

**提示（Prompt）**：端口 1 发送中断阈值计数（TX Interrupt Threshold Count）

**说明（Help）**

端口 1 触发发送 FIFO（TX FIFO）中断的发送阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_SIFIVE_PORT_1 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/serial/Kconfig.sifive:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.sifive#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → SiFive Freedom 串行驱动（Serial Driver） → SIFIVE 端口 1（Port 1）

**配置项引用（Symbol References）**：[`CONFIG_UART_SIFIVE_PORT_1`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_SIFIVE_PORT_1)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_SILABS_EUSART"></a>

## 169.3 `CONFIG_UART_SILABS_EUSART`

**提示（Prompt）**：Silabs EUSART UART 驱动

**说明（Help）**

启用 EUSART UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_EUSART_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SILABS_SISDK_EUSART
CONFIG_SERIAL_SUPPORT_ASYNC if DT_HAS_SILABS_LDMA_ENABLED
CONFIG_DMA if CONFIG_UART_ASYNC_API
CONFIG_PINCTRL
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.silabs_eusart:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.silabs_eusart#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SILABS_SISDK_EUSART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_EUSART)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_UART_SILABS_EUSART_ASYNC"></a>

## 169.4 `CONFIG_UART_SILABS_EUSART_ASYNC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设为 Y 时，Silabs EUSART 驱动将编译进 UART 异步 API（Async API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_SILABS_LDMA && CONFIG_UART_ASYNC_API && CONFIG_UART_SILABS_EUSART && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.silabs_eusart:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.silabs_eusart#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Silabs EUSART UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_SILABS_LDMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_SILABS_LDMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_SILABS_EUSART`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_SILABS_EUSART)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_SILABS_USART"></a>

## 169.5 `CONFIG_UART_SILABS_USART`

**提示（Prompt）**：Silabs USART UART 驱动

**说明（Help）**

启用 Silicon Labs USART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_USART_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SILABS_SISDK_USART
CONFIG_SERIAL_SUPPORT_ASYNC if DT_HAS_SILABS_LDMA_ENABLED
CONFIG_DMA if CONFIG_UART_ASYNC_API
CONFIG_PINCTRL
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.silabs_usart:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.silabs_usart#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SILABS_SISDK_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_USART)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_UART_SILABS_USART_ASYNC"></a>

## 169.6 `CONFIG_UART_SILABS_USART_ASYNC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设为 Y 时，Silabs USART 驱动将编译进 UART 异步 API（Async API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_SILABS_LDMA && CONFIG_UART_ASYNC_API && CONFIG_UART_SILABS_USART && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.silabs_usart:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.silabs_usart#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Silabs USART UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_SILABS_LDMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_SILABS_LDMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_SILABS_USART`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_SILABS_USART)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_SMARTBOND"></a>

## 169.7 `CONFIG_UART_SMARTBOND`

**提示（Prompt）**：Renesas SmartBond™ UART 驱动

**说明（Help）**

为 Renesas SmartBond™ DA1469x 系列微控制器（MCU）启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_UART_INTERRUPT_DRIVEN if CONFIG_PM_DEVICE
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.smartbond:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.smartbond#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_STELLARIS"></a>

## 169.8 `CONFIG_UART_STELLARIS`

**提示（Prompt）**：Stellaris 串行驱动（Serial Driver）

**说明（Help）**

此选项启用 Stellaris 串行驱动（Serial Driver），可用于 Texas Instruments LM3S6965 开发板上的串行硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_STELLARIS_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.stellaris:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.stellaris#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_STELLARIS_PORT_0"></a>

## 169.9 `CONFIG_UART_STELLARIS_PORT_0`

**提示（Prompt）**：Stellaris UART 端口 0

**说明（Help）**

指示驱动在启动时根据下面的其他配置选项，配置 UART 端口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_STELLARIS && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.stellaris:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.stellaris#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Stellaris 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_STELLARIS`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_STELLARIS)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_STELLARIS_PORT_1"></a>

## 169.10 `CONFIG_UART_STELLARIS_PORT_1`

**提示（Prompt）**：Stellaris UART 端口 1

**说明（Help）**

指示驱动在启动时根据下面的其他配置选项，配置 UART 端口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_STELLARIS && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.stellaris:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.stellaris#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Stellaris 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_STELLARIS`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_STELLARIS)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_STELLARIS_PORT_2"></a>

## 169.11 `CONFIG_UART_STELLARIS_PORT_2`

**提示（Prompt）**：Stellaris UART 端口 2

**说明（Help）**

指示驱动在启动时根据下面的其他配置选项，配置 UART 端口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_STELLARIS && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.stellaris:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.stellaris#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Stellaris 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_STELLARIS`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_STELLARIS)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_STM32"></a>

## 169.12 `CONFIG_UART_STM32`

**提示（Prompt）**：STM32 MCU 串行驱动

**说明（Help）**

此选项为 STM32 系列处理器启用 UART 驱动。如果需要在 STM32 微控制器（MCU）上使用串口，请选择 Y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_SUPPORT_ASYNC if DT_HAS_ST_STM32_DMA_V1_ENABLED || DT_HAS_ST_STM32_DMA_V2_ENABLED || DT_HAS_ST_STM32_DMA_V2BIS_ENABLED || DT_HAS_ST_STM32U5_DMA_ENABLED
CONFIG_DMA if CONFIG_UART_ASYNC_API
CONFIG_RESET
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.stm32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.stm32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_STM32U5_ERRATA_DMAT"></a>

## 169.13 `CONFIG_UART_STM32U5_ERRATA_DMAT`

**提示（Prompt）**：特定器件 DMAT 勘误的变通方案（Workaround）

**说明（Help）**

处理“置位／清除 DMAT 位后 USART 不产生 DMA 请求”的勘误（Erratum）。相关勘误文档位置如下：

- STM32H503xx：ES0561 修订版 4，第 2.11.2 和 2.12.1 节。
- STM32H523xx/H533xx：ES0621 修订版 2，第 2.14.2 和 2.15.1 节。
- STM32H562xx/H563xx/H573xx：ES0565 修订版 7，第 2.16.2 和 2.17.1 节。
- STM32U575xx/U585xx：ES0499 修订版 10，第 2.21.2 和 2.22.1 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_STM32U5_ERRATA_DMAT_AFFECTED && CONFIG_UART_STM32 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
CONFIG_UART_STM32U5_ERRATA_DMAT_NOCLEAR if !CONFIG_PM
CONFIG_UART_STM32U5_ERRATA_DMAT_LOWPOWER
```

**可选项（Choices）**

```text
CONFIG_UART_STM32U5_ERRATA_DMAT_LOWPOWER
CONFIG_UART_STM32U5_ERRATA_DMAT_NOCLEAR
```

**定义位置（Location）**：[`drivers/serial/Kconfig.stm32:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.stm32#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → STM32 MCU 串行驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_STM32U5_ERRATA_DMAT_AFFECTED`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_STM32U5_ERRATA_DMAT_AFFECTED)、[`CONFIG_UART_STM32`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_STM32)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_STM32U5_ERRATA_DMAT_NOCLEAR`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_STM32U5_ERRATA_DMAT_NOCLEAR)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_UART_STM32U5_ERRATA_DMAT_LOWPOWER`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_STM32U5_ERRATA_DMAT_LOWPOWER)。

<a id="CONFIG_UART_STM32U5_ERRATA_DMAT_AFFECTED"></a>

## 169.14 `CONFIG_UART_STM32U5_ERRATA_DMAT_AFFECTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

受 DMAT 勘误（Errata）影响。请参阅 `UART_STM32U5_ERRATA_DMAT`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_STM32H503XX || CONFIG_SOC_STM32H523XX || CONFIG_SOC_STM32H533XX || CONFIG_SOC_STM32H562XX || CONFIG_SOC_STM32H563XX || CONFIG_SOC_STM32H573XX || CONFIG_SOC_STM32U575XX || CONFIG_SOC_STM32U585XX) && CONFIG_UART_STM32 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.stm32:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.stm32#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → STM32 MCU 串行驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_STM32H503XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H503XX)、[`CONFIG_SOC_STM32H523XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H523XX)、[`CONFIG_SOC_STM32H533XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H533XX)、[`CONFIG_SOC_STM32H562XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H562XX)、[`CONFIG_SOC_STM32H563XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H563XX)、[`CONFIG_SOC_STM32H573XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H573XX)、[`CONFIG_SOC_STM32U575XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32U575XX)、[`CONFIG_SOC_STM32U585XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32U585XX)、[`CONFIG_UART_STM32`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_STM32)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_STM32H503XX`、`CONFIG_SOC_STM32H523XX`、`CONFIG_SOC_STM32H533XX`、`CONFIG_SOC_STM32H562XX`、`CONFIG_SOC_STM32H563XX`、`CONFIG_SOC_STM32H573XX`、`CONFIG_SOC_STM32U575XX`、`CONFIG_SOC_STM32U585XX`。

<a id="CONFIG_UART_STM32U5_ERRATA_DMAT_LOWPOWER"></a>

## 169.15 `CONFIG_UART_STM32U5_ERRATA_DMAT_LOWPOWER`

**提示（Prompt）**：通过轮询发送首字节

**说明（Help）**

此选项通过软件轮询（Software Polling）发送第一个字节，缓冲区剩余部分通过直接内存访问（DMA）发送，适用于 STOP 低功耗模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_STM32U5_ERRATA_DMAT>
```

**定义位置（Location）**：[`drivers/serial/Kconfig.stm32:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.stm32#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → STM32 MCU 串行驱动 → 特定器件 DMAT 勘误的变通方案（Workaround）

**配置项引用（Symbol References）**：[`CONFIG_UART_STM32U5_ERRATA_DMAT`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_STM32U5_ERRATA_DMAT)。

<a id="CONFIG_UART_STM32U5_ERRATA_DMAT_NOCLEAR"></a>

## 169.16 `CONFIG_UART_STM32U5_ERRATA_DMAT_NOCLEAR`

**提示（Prompt）**：不清除 DMAT

**说明（Help）**

此选项使 DMAT 位保持置位，在 STOP 低功耗模式下可能增加功耗。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_POWEROFF && <choice CONFIG_UART_STM32U5_ERRATA_DMAT>
```

**定义位置（Location）**：[`drivers/serial/Kconfig.stm32:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.stm32#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → STM32 MCU 串行驱动 → 特定器件 DMAT 勘误的变通方案（Workaround）

**配置项引用（Symbol References）**：[`CONFIG_POWEROFF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POWEROFF)、[`CONFIG_UART_STM32U5_ERRATA_DMAT`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_STM32U5_ERRATA_DMAT)。

<a id="CONFIG_UART_STM32_ABNORMAL_RTS_ERRATUM_WORKAROUND"></a>

## 169.17 `CONFIG_UART_STM32_ABNORMAL_RTS_ERRATUM_WORKAROUND`

**提示（Prompt）**：协议违规后 nRTS 异常拉低问题的变通方案

**说明（Help）**

在启用硬件流控制（`hw-flow-control`）的 STM32 UART 外设上，通过 GPIO 启用软件请求发送（RTS）流控制。在保留硬件允许发送（CTS）功能的同时，由软件管理 RTS，从而规避受影响 STM32 器件上“协议违规后 nRTS 异常拉低”的勘误（Erratum）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_STM32 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/serial/Kconfig.stm32:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.stm32#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → STM32 MCU 串行驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_STM32`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_STM32)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_UART_SY1XX"></a>

## 169.18 `CONFIG_UART_SY1XX`

**提示（Prompt）**：Sensry SY1xx 驱动

**说明（Help）**

Sensry SY1xx 系列 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSRY_SY1XX_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.sy1xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.sy1xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_TELINK_B91"></a>

## 169.19 `CONFIG_UART_TELINK_B91`

**提示（Prompt）**：Telink B91 UART 驱动

**说明（Help）**

此选项启用 B91 串行驱动（Serial Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TELINK_B91_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.b91:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.b91#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_TIVA_C"></a>

## 169.20 `CONFIG_UART_TIVA_C`

**提示（Prompt）**：TI Tiva C 系列 UART 驱动

**说明（Help）**

为 TI Tiva C 系列微控制器（TM4C123G、TM4C129x）启用 UART 驱动，使用 TivaWare 硬件抽象层（HAL）的 `driverlib/uart.c` 进行配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TIVA_C_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_USE_TIVAWARE_UART
CONFIG_USE_TIVAWARE_SYSCTL
CONFIG_USE_TIVAWARE_GPIO
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.tiva_c:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.tiva_c#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_USE_TIVAWARE_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_TIVAWARE_UART)、[`CONFIG_USE_TIVAWARE_SYSCTL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_TIVAWARE_SYSCTL)、[`CONFIG_USE_TIVAWARE_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_TIVAWARE_GPIO)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_TIVAWARE_UART`、`CONFIG_USE_TIVAWARE_SYSCTL`、`CONFIG_USE_TIVAWARE_GPIO`。

<a id="CONFIG_UART_TX_CACHE_LEN"></a>

## 169.21 `CONFIG_UART_TX_CACHE_LEN`

**提示（Prompt）**：发送（TX）缓存缓冲区大小

**说明（Help）**

源缓冲区不位于可供 DMA 访问的区域时，所使用的 UART 发送缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_MAX32 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[8, 64]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.max32:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.max32#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → MAX32 MCU 串行驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_MAX32`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_MAX32)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_USE_RUNTIME_CONFIGURE"></a>

## 169.22 `CONFIG_UART_USE_RUNTIME_CONFIGURE`

**提示（Prompt）**：UART 控制器运行时配置（Runtime Configuration）

**说明（Help）**

启用 UART 控制器运行时配置（Runtime Configuration），允许应用调用 `uart_configure()` 在运行时配置 UART 控制器，并调用 `uart_config_get()` 取得配置。如果禁用，UART 控制器将依赖驱动的初始化函数进行正确配置。如果不确定，请选择 Y。对于不需要运行时 UART 配置的应用，可以禁用此选项以减小资源占用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_BT_AIROC
CONFIG_ETH_CH9120
CONFIG_GNSS_U_BLOX_M10
CONFIG_GNSS_U_BLOX_M8
CONFIG_I2C_SC18IM704
CONFIG_INPUT_CRSF
CONFIG_INPUT_SBUS
CONFIG_MODEM_CELLULAR
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE
CONFIG_A01NYUB
CONFIG_UART_LPC84X
CONFIG_W1_ZEPHYR_SERIAL
CONFIG_GDBSTUB
```

**被弱选择（Implied by）**

```text
CONFIG_WIFI_ESP_AT
CONFIG_OSDP
CONFIG_MODBUS_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_ETH_CH9120`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_CH9120)、[`CONFIG_GNSS_U_BLOX_M10`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10)、[`CONFIG_GNSS_U_BLOX_M8`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M8)、[`CONFIG_I2C_SC18IM704`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_SC18IM704)、[`CONFIG_INPUT_CRSF`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CRSF)、[`CONFIG_INPUT_SBUS`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_SBUS)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM_HL78XX_AUTO_BAUDRATE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTO_BAUDRATE)、[`CONFIG_A01NYUB`](P149_drivers_sensor_配置项参考_1.md#CONFIG_A01NYUB)、[`CONFIG_UART_LPC84X`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_LPC84X)、[`CONFIG_W1_ZEPHYR_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_W1_ZEPHYR_SERIAL)、[`CONFIG_GDBSTUB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GDBSTUB)、[`CONFIG_WIFI_ESP_AT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP_AT)、[`CONFIG_OSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OSDP)、[`CONFIG_MODBUS_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODBUS_SERIAL)。

<a id="CONFIG_UART_VIRTIO_CONSOLE"></a>

## 169.23 `CONFIG_UART_VIRTIO_CONSOLE`

**提示（Prompt）**：VIRTIO 控制台半虚拟化设备驱动（Paravirtualization Device Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VIRTIO_CONSOLE_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_VIRTIO
CONFIG_SERIAL_HAS_POST_KERNEL_INIT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.virtio_console:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.virtio_console#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_VIRTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIRTIO)、[`CONFIG_SERIAL_HAS_POST_KERNEL_INIT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_POST_KERNEL_INIT)。

<a id="CONFIG_UART_VIRTIO_CONSOLE_F_MULTIPORT"></a>

## 169.24 `CONFIG_UART_VIRTIO_CONSOLE_F_MULTIPORT`

**提示（Prompt）**：支持多个 VIRTIO 控制台端口

**说明（Help）**

VIRTIO 控制台设备可同时支持多个输入／输出端口（I/O Ports），QEMU 中最多为 31 个。选择此选项以启用该功能；否则，只使用一个端口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_VIRTIO_CONSOLE && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/serial/Kconfig.virtio_console:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.virtio_console#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → VIRTIO 控制台半虚拟化设备驱动（Paravirtualization Device Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_VIRTIO_CONSOLE`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_VIRTIO_CONSOLE)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_VIRTIO_CONSOLE_NAME_BUFSIZE"></a>

## 169.25 `CONFIG_UART_VIRTIO_CONSOLE_NAME_BUFSIZE`

**提示（Prompt）**：VIRTIO 控制台端口名称最大长度

**说明（Help）**

可以为端口指定便于阅读的名称，并在日志中打印这些名称。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_VIRTIO_CONSOLE && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
0 if CONFIG_UART_LOG_LEVEL < 3
16
```

**定义位置（Location）**：[`drivers/serial/Kconfig.virtio_console:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.virtio_console#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → VIRTIO 控制台半虚拟化设备驱动（Paravirtualization Device Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_VIRTIO_CONSOLE`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_VIRTIO_CONSOLE)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_LOG_LEVEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_LOG_LEVEL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UART_LOG_LEVEL`。

<a id="CONFIG_UART_VIRTIO_CONSOLE_RX_BUFSIZE"></a>

## 169.26 `CONFIG_UART_VIRTIO_CONSOLE_RX_BUFSIZE`

**提示（Prompt）**：VIRTIO 控制台接收缓冲区长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_VIRTIO_CONSOLE && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/serial/Kconfig.virtio_console:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.virtio_console#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → VIRTIO 控制台半虚拟化设备驱动（Paravirtualization Device Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_VIRTIO_CONSOLE`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_VIRTIO_CONSOLE)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_VIRTIO_CONSOLE_RX_CONTROL_BUFSIZE"></a>

## 169.27 `CONFIG_UART_VIRTIO_CONSOLE_RX_CONTROL_BUFSIZE`

**提示（Prompt）**：VIRTIO 控制台控制消息接收缓冲区长度

**说明（Help）**

设置控制消息接收缓冲区及其对应虚拟队列（Virtqueue）的大小。请注意，控制消息可能连续快速发送；此值过小时，某些消息可能始终无法接收。如果多端口功能出现问题，可尝试增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_VIRTIO_CONSOLE_F_MULTIPORT && CONFIG_UART_VIRTIO_CONSOLE && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/serial/Kconfig.virtio_console:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.virtio_console#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → VIRTIO 控制台半虚拟化设备驱动（Paravirtualization Device Driver） → 支持多个 VIRTIO 控制台端口

**配置项引用（Symbol References）**：[`CONFIG_UART_VIRTIO_CONSOLE_F_MULTIPORT`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_VIRTIO_CONSOLE_F_MULTIPORT)、[`CONFIG_UART_VIRTIO_CONSOLE`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_VIRTIO_CONSOLE)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_VIRTIO_CONSOLE_TX_BUFSIZE"></a>

## 169.28 `CONFIG_UART_VIRTIO_CONSOLE_TX_BUFSIZE`

**提示（Prompt）**：VIRTIO 控制台发送缓冲区长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_VIRTIO_CONSOLE && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/serial/Kconfig.virtio_console:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.virtio_console#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → VIRTIO 控制台半虚拟化设备驱动（Paravirtualization Device Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_VIRTIO_CONSOLE`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_VIRTIO_CONSOLE)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_VIRTIO_CONSOLE_TX_CONTROL_BUFSIZE"></a>

## 169.29 `CONFIG_UART_VIRTIO_CONSOLE_TX_CONTROL_BUFSIZE`

**提示（Prompt）**：VIRTIO 控制台控制消息发送缓冲区长度

**说明（Help）**

设置控制消息发送缓冲区及其对应虚拟队列（Virtqueue）的大小。请注意，控制消息可能连续快速发送；此值过小时，缓冲区可能迅速填满。如果多端口功能出现问题，可尝试增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_VIRTIO_CONSOLE_F_MULTIPORT && CONFIG_UART_VIRTIO_CONSOLE && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/serial/Kconfig.virtio_console:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.virtio_console#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → VIRTIO 控制台半虚拟化设备驱动（Paravirtualization Device Driver） → 支持多个 VIRTIO 控制台端口

**配置项引用（Symbol References）**：[`CONFIG_UART_VIRTIO_CONSOLE_F_MULTIPORT`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_VIRTIO_CONSOLE_F_MULTIPORT)、[`CONFIG_UART_VIRTIO_CONSOLE`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_VIRTIO_CONSOLE)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_WCH_CH5XX"></a>

## 169.30 `CONFIG_UART_WCH_CH5XX`

**提示（Prompt）**：WCH CH5xx UART 驱动

**说明（Help）**

此选项为 CH5xx 片上系统（SoC）系列启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_CH5XX_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.wch_ch5xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.wch_ch5xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_WCH_USART"></a>

## 169.31 `CONFIG_UART_WCH_USART`

**提示（Prompt）**：CH32V00x USART 驱动

**说明（Help）**

此选项为 CH32V00x 片上系统（SoC）系列启用 USART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_USART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.wch_usart:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.wch_usart#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_WCH_USART_RESET"></a>

## 169.32 `CONFIG_UART_WCH_USART_RESET`

**提示（Prompt）**：使用前复位 USART 外设

**说明（Help）**

使用前通过复位子系统（Reset Subsystem）复位 USART 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RESET && CONFIG_UART_WCH_USART && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.wch_usart:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.wch_usart#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → CH32V00x USART 驱动

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)、[`CONFIG_UART_WCH_USART`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_WCH_USART)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_WIDE_DATA"></a>

## 169.33 `CONFIG_UART_WIDE_DATA`

**提示（Prompt）**：支持超过 8 位数据的 API

**说明（Help）**

启用处理超过 8 位数据的 API。各个驱动负责实现正确支持此功能所需的函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_XEC"></a>

## 169.34 `CONFIG_UART_XEC`

**提示（Prompt）**：Microchip XEC 系列 UART 驱动

**说明（Help）**

此选项为 Microchip XEC 微控制器（MCU）启用 UARTx 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_XEC_LINE_CTRL"></a>

## 169.35 `CONFIG_UART_XEC_LINE_CTRL`

**提示（Prompt）**：面向应用的串行线路控制（Serial Line Control）

**说明（Help）**

启用应用控制串行线路的 API，例如允许发送（CTS）和请求发送（RTS）。如果不确定，请选择 N。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_LINE_CTRL && CONFIG_UART_XEC && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.xec:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.xec#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Microchip XEC 系列 UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_LINE_CTRL`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_LINE_CTRL)、[`CONFIG_UART_XEC`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_XEC)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_XEN_HVC"></a>

## 169.36 `CONFIG_UART_XEN_HVC`

**提示（Prompt）**：Xen 虚拟机监控器 DomU 控制台 UART 驱动

**说明（Help）**

启用基于 Xen 环形缓冲区（Ring Buffer）的虚拟机监控器（Hypervisor）控制台驱动，用于将 Zephyr 作为非特权域（Unprivileged Domain）运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XEN_HVC_UART_ENABLED && CONFIG_XEN && !CONFIG_XEN_DOM0 && !CONFIG_XEN_DOM0LESS && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_XEN_EVENTS if CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`drivers/serial/Kconfig.xen:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.xen#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)、[`CONFIG_XEN_DOM0`](P031_arch_arm64_配置项参考.md#CONFIG_XEN_DOM0)、[`CONFIG_XEN_DOM0LESS`](P031_arch_arm64_配置项参考.md#CONFIG_XEN_DOM0LESS)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_XEN_EVENTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN_EVENTS)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_UART_XEN_HVC_CONSOLEIO"></a>

## 169.37 `CONFIG_UART_XEN_HVC_CONSOLEIO`

**提示（Prompt）**：Xen 虚拟机监控器 consoleio UART 驱动

**说明（Help）**

启用 Xen 虚拟机监控器（Hypervisor）控制台驱动，用于将 Zephyr 作为特权域（Privileged Domain，Dom0）运行，或在无 Dom0（Dom0less）配置中作为 DomU 运行。Dom0less 配置没有特权域，因此没有控制台守护进程（Console Daemon）；Xen 通过 `consoleio` 接口管理所有域的输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XEN_HVC_CONSOLEIO_ENABLED && (CONFIG_XEN_DOM0 || CONFIG_XEN_DOM0LESS) && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.xen:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.xen#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_XEN_DOM0`](P031_arch_arm64_配置项参考.md#CONFIG_XEN_DOM0)、[`CONFIG_XEN_DOM0LESS`](P031_arch_arm64_配置项参考.md#CONFIG_XEN_DOM0LESS)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)。

<a id="CONFIG_UART_XLNX_PS"></a>

## 169.38 `CONFIG_UART_XLNX_PS`

**提示（Prompt）**：Xilinx Zynq 7000/ZynqMP 串行驱动

**说明（Help）**

此选项为 Xilinx 多处理器片上系统（MPSoC）平台启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_XUARTPS_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.xlnx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.xlnx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_XLNX_UARTLITE"></a>

## 169.39 `CONFIG_UART_XLNX_UARTLITE`

**提示（Prompt）**：Xilinx UART Lite

**说明（Help）**

此选项为 Xilinx UART Lite IP 启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_XPS_UARTLITE_1_00_A_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.xlnx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.xlnx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_XMC4XXX"></a>

## 169.40 `CONFIG_UART_XMC4XXX`

**提示（Prompt）**：XMC4XX UART 驱动

**说明（Help）**

此选项启用 XMC4XX UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_SUPPORT_ASYNC if DT_HAS_INFINEON_XMC4XXX_DMA_ENABLED
CONFIG_DMA if CONFIG_UART_ASYNC_API
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.xmc4xxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.xmc4xxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_XMC4XXX_RX_FIFO_INT_TRIGGER"></a>

## 169.41 `CONFIG_UART_XMC4XXX_RX_FIFO_INT_TRIGGER`

**提示（Prompt）**：持续触发 FIFO 接收（RX）中断

**说明（Help）**

启用此选项后，只要接收 FIFO 中仍有数据，中断就会持续触发。否则，仅在收到第一个字节时触发一次中断；必须完全清空接收 FIFO，才会再次触发中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_XMC4XXX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/serial/Kconfig.xmc4xxx:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.xmc4xxx#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → XMC4XX UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_XMC4XXX`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_XMC4XXX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_USART_GD32"></a>

## 169.42 `CONFIG_USART_GD32`

**提示（Prompt）**：GD32 串行驱动（Serial Driver）

**说明（Help）**

此选项为 GD32 片上系统（SoC）系列启用 USART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_USART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_USE_GD32_USART
```

**定义位置（Location）**：[`drivers/serial/Kconfig.gd32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.gd32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_USE_GD32_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_GD32_USART)。

<a id="CONFIG_USART_SAM"></a>

## 169.43 `CONFIG_USART_SAM`

**提示（Prompt）**：Atmel SAM MCU 系列 USART 驱动

**说明（Help）**

此选项为 Atmel SAM 微控制器（MCU）启用 USARTx 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_USART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_MFD if CONFIG_SOC_SERIES_SAMA7G5
```

**定义位置（Location）**：[`drivers/serial/Kconfig.usart_sam:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.usart_sam#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_SOC_SERIES_SAMA7G5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMA7G5)。

<a id="CONFIG_XEN_EARLY_CONSOLEIO"></a>

## 169.44 `CONFIG_XEN_EARLY_CONSOLEIO`

**提示（Prompt）**：通过 Xen console_io 接口提供早期 printk/stdout

**说明（Help）**

启用为标准输出（stdout）和 `printk` 设置 `console_io` 符号钩子（Symbol Hook）。日志输出将在 `PRE_KERNEL_1` 阶段可用。要求 Xen 使用 `CONFIG_DEBUG` 标志编译。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_XEN_HVC && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.xen:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.xen#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_XEN_HVC`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_XEN_HVC)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_XEN_HVC_INIT_PRIORITY"></a>

## 169.45 `CONFIG_XEN_HVC_INIT_PRIORITY`

**提示（Prompt）**：Xen 虚拟机监控器控制台初始化优先级

**说明（Help）**

设置 Xen 虚拟机监控器控制台（HVC）的初始化优先级。HVC 应在 UART 控制台驱动之前初始化，并在 `PRE_KERNEL_1` 阶段完成初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_XEN_HVC || CONFIG_UART_XEN_HVC_CONSOLEIO) && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
55
```

**定义位置（Location）**：[`drivers/serial/Kconfig.xen:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.xen#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_XEN_HVC`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_XEN_HVC)、[`CONFIG_UART_XEN_HVC_CONSOLEIO`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_XEN_HVC_CONSOLEIO)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<!-- kconfig-navigation -->

[上一章](P168_drivers_serial_配置项参考_4.md) · [返回大纲](大纲.md) · [下一章](P170_drivers_sip_svc_配置项参考.md)
