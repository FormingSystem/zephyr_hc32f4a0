---
id: learning.zephyr-docs.kconfig-reference.page-168
title: "`drivers/serial`配置项参考（4/5）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第168章\_`drivers/serial`配置项参考（4/5）

本章翻译官方 Kconfig 数据库中 `drivers/serial` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_UART_MCHP_SERCOM_G1"></a>

## 168.1 `CONFIG_UART_MCHP_SERCOM_G1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项为 SERCOM 外设的 g1 组启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SERCOM_G1_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_SUPPORT_ASYNC
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_MCHP_UART_G1"></a>

## 168.2 `CONFIG_UART_MCHP_UART_G1`

**提示（Prompt）**：Microchip SAM UART（uart-g1）驱动

**说明（Help）**

此选项为 UART 外设的 g1 组启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_UART_G1_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.mchp:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mchp#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_MCUX"></a>

## 168.3 `CONFIG_UART_MCUX`

**提示（Prompt）**：MCUX UART 驱动

**说明（Help）**

启用 MCUX UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_UART_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.mcux:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mcux#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_MCUX_FLEXCOMM"></a>

## 168.4 `CONFIG_UART_MCUX_FLEXCOMM`

**提示（Prompt）**：MCUX FLEXCOMM UART 驱动

**说明（Help）**

启用 MCUX USART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_USART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_SUPPORT_ASYNC if DT_HAS_NXP_LPC_DMA_ENABLED
CONFIG_PM_POLICY_DEVICE_CONSTRAINTS if CONFIG_PM
CONFIG_DMA if CONFIG_UART_ASYNC_API
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.mcux_flexcomm:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mcux_flexcomm#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_PM_POLICY_DEVICE_CONSTRAINTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_POLICY_DEVICE_CONSTRAINTS)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_MCUX_FLEXCOMM_ISR_SUPPORT"></a>

## 168.5 `CONFIG_UART_MCUX_FLEXCOMM_ISR_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 UART 中断服务程序（Interrupt Service Routine，ISR）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_MCUX_FLEXCOMM && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if CONFIG_UART_INTERRUPT_DRIVEN || CONFIG_UART_ASYNC_API
```

**定义位置（Location）**：[`drivers/serial/Kconfig.mcux_flexcomm:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mcux_flexcomm#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → MCUX FLEXCOMM UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_MCUX_FLEXCOMM`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_MCUX_FLEXCOMM)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)。

<a id="CONFIG_UART_MCUX_IUART"></a>

## 168.6 `CONFIG_UART_MCUX_IUART`

**提示（Prompt）**：MCUX IUART 驱动

**说明（Help）**

启用 MCUX IUART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_IUART_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_SERIAL
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
```

**定义位置（Location）**：[`drivers/serial/Kconfig.mcux_iuart:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mcux_iuart#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_MCUX_LPSCI"></a>

## 168.7 `CONFIG_UART_MCUX_LPSCI`

**提示（Prompt）**：MCUX LPSCI 驱动

**说明（Help）**

启用 MCUX LPSCI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_LPSCI_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.mcux_lpsci:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mcux_lpsci#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_MCUX_LPUART"></a>

## 168.8 `CONFIG_UART_MCUX_LPUART`

**提示（Prompt）**：MCUX LPUART 驱动

**说明（Help）**

启用 MCUX LPUART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPUART_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.mcux_lpuart:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mcux_lpuart#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_MCUX_LPUART_ISR_SUPPORT"></a>

## 168.9 `CONFIG_UART_MCUX_LPUART_ISR_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 UART 中断服务程序（Interrupt Service Routine，ISR）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_MCUX_LPUART && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if CONFIG_UART_INTERRUPT_DRIVEN || CONFIG_PM || CONFIG_UART_ASYNC_API
```

**定义位置（Location）**：[`drivers/serial/Kconfig.mcux_lpuart:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mcux_lpuart#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → MCUX LPUART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_MCUX_LPUART`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_MCUX_LPUART)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)。

<a id="CONFIG_UART_MIV"></a>

## 168.10 `CONFIG_UART_MIV`

**提示（Prompt）**：Mi-V 串行驱动（Serial Driver）

**说明（Help）**

此选项启用 Mi-V 串行驱动（Serial Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_COREUART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.miv:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.miv#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)。

<a id="CONFIG_UART_MSP432P4XX"></a>

## 168.11 `CONFIG_UART_MSP432P4XX`

**提示（Prompt）**：MSP432P4XX UART 驱动

**说明（Help）**

此选项为 `UART_0` 启用 MSP432P4XX UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSP432P4XX_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.msp432p4xx:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.msp432p4xx#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_MSPM0"></a>

## 168.12 `CONFIG_UART_MSPM0`

**提示（Prompt）**：MSPM0 UART 驱动

**说明（Help）**

此选项启用 TI MSPM0 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_USE_MSPM0_DL_UART
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.mspm0:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mspm0#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_USE_MSPM0_DL_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_MSPM0_DL_UART)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_MSPM0_DL_UART`。

<a id="CONFIG_UART_MT8188"></a>

## 168.13 `CONFIG_UART_MT8188`

**提示（Prompt）**：MediaTek MT8188 UART 驱动

**说明（Help）**

为 MediaTek MT8188 启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MEDIATEK_MT8188_UART_ENABLED && CONFIG_SERIAL
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
```

**定义位置（Location）**：[`drivers/serial/Kconfig.mtk:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mtk#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_NATIVE_PTY"></a>

## 168.14 `CONFIG_UART_NATIVE_PTY`

**提示（Prompt）**：用于 native_sim 的伪终端（PTY）UART 驱动

**说明（Help）**

为 POSIX 架构启用基于伪终端（Pseudoterminal，PTY）的 UART 驱动，最多支持两个 UART。对于第一个 UART 端口，可以配置为连接到运行可执行文件的终端，或者连接到为该 UART 单独创建的伪终端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_NATIVE_PTY_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_ASYNC
CONFIG_SERIAL_SUPPORT_INTERRUPT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.native_pty:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.native_pty#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_NATIVE_PTY_0"></a>

## 168.15 `CONFIG_UART_NATIVE_PTY_0`

**提示（Prompt）**：原生伪终端（Native PTY）端口 0 的连接方式

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NATIVE_PTY && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
CONFIG_UART_NATIVE_PTY_0_ON_OWN_PTY
```

**可选项（Choices）**

```text
CONFIG_UART_NATIVE_PTY_0_ON_OWN_PTY
CONFIG_UART_NATIVE_PTY_0_ON_STDINOUT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.native_pty:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.native_pty#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 用于 native_sim 的伪终端（PTY）UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_NATIVE_PTY`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NATIVE_PTY)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_NATIVE_PTY_0_ON_OWN_PTY`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NATIVE_PTY_0_ON_OWN_PTY)、[`CONFIG_UART_NATIVE_PTY_0_ON_STDINOUT`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NATIVE_PTY_0_ON_STDINOUT)。

<a id="CONFIG_UART_NATIVE_PTY_0_ON_OWN_PTY"></a>

## 168.16 `CONFIG_UART_NATIVE_PTY_0_ON_OWN_PTY`

**提示（Prompt）**：将第一个 PTY UART 连接到其专用伪终端

**说明（Help）**

将此 UART 连接到其专用伪终端（Pseudoterminal）。对于需要使用 Zephyr 命令行（Shell）的用户，这是推荐选项。它也不会与可能使用调用方命令行标准输入／输出的其他原生后端冲突。注意，可通过命令行覆盖此设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_NATIVE_PTY_0>
```

**定义位置（Location）**：[`drivers/serial/Kconfig.native_pty:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.native_pty#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 用于 native_sim 的伪终端（PTY）UART 驱动 → 原生伪终端（Native PTY）端口 0 的连接方式

**配置项引用（Symbol References）**：[`CONFIG_UART_NATIVE_PTY_0`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NATIVE_PTY_0)。

<a id="CONFIG_UART_NATIVE_PTY_0_ON_STDINOUT"></a>

## 168.17 `CONFIG_UART_NATIVE_PTY_0_ON_STDINOUT`

**提示（Prompt）**：将第一个 PTY UART 连接到调用方命令行的 stdin/stdout

**说明（Help）**

将第一个 UART 实例连接到启动原生可执行文件的命令行／终端的标准输入和标准输出（stdin/stdout）。这足以满足自动化测试，或从文件／管道输入数据的需求。

注意：此设置适用于最先实例化的 PTY 实例。如果有多个实例，并希望指定哪个实例使用 stdin/stdout，应改用命令行选项，或对应实例设备树（DT）的 `on-stdinout` 属性。终端中还会打印其他非 UART 消息。不建议将此选项用于交互式命令行：默认终端配置不适合 Zephyr Shell 的交互使用，自动补全、历史记录搜索等功能可能表现异常。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_NATIVE_PTY_0>
```

**定义位置（Location）**：[`drivers/serial/Kconfig.native_pty:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.native_pty#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 用于 native_sim 的伪终端（PTY）UART 驱动 → 原生伪终端（Native PTY）端口 0 的连接方式

**配置项引用（Symbol References）**：[`CONFIG_UART_NATIVE_PTY_0`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NATIVE_PTY_0)。

<a id="CONFIG_UART_NATIVE_PTY_AUTOATTACH_DEFAULT_CMD"></a>

## 168.18 `CONFIG_UART_NATIVE_PTY_AUTOATTACH_DEFAULT_CMD`

**提示（Prompt）**：将 PTY UART 连接到新终端的默认命令

**说明（Help）**

如果使用 `--attach_uart` 命令行选项运行原生可执行文件，此设置指定用于将新终端连接到第一个 UART 的默认命令。该命令必须包含且只能包含一个 `%s`，作为伪终端设备名的占位符，例如 `/dev/pts/35`。

仅当 `UART_0` 通过 `UART_NATIVE_PTY_0_ON_OWN_PTY` 配置为使用专用 PTY 时，此选项才适用。第二个 UART 不受此选项影响。使用 GNOME 时，可使用以下命令字符串：

```sh
gnome-terminal -- screen %s
```

译注：`/dev/pts/35` 是原文中的 Linux 伪终端设备路径示例，不是仓库绝对路径。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NATIVE_PTY && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
"xterm -e screen %s &"
```

**定义位置（Location）**：[`drivers/serial/Kconfig.native_pty:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.native_pty#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 用于 native_sim 的伪终端（PTY）UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_NATIVE_PTY`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NATIVE_PTY)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_NATIVE_PTY_RX_POLL_PERIOD_US"></a>

## 168.19 `CONFIG_UART_NATIVE_PTY_RX_POLL_PERIOD_US`

**提示（Prompt）**：异步接收（RX）线程轮询 PTY 的周期，单位为微秒

**说明（Help）**

异步 API 通过轮询伪终端（PTY）的线程模拟实现。线程未发现数据时，会休眠此处指定的时长，因此接收字节在驱动察觉之前的最长等待时间由此决定。减小此值会增加主机 CPU 使用率，但可降低延迟。注意，无论此值如何设置，休眠至少持续两个时钟节拍（Tick，由 `CONFIG_SYS_CLOCK_TICKS_PER_SEC` 决定）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_UART_NATIVE_PTY && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
10000
```

**取值范围（Ranges）**

```text
[1, 1000000]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.native_pty:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.native_pty#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 用于 native_sim 的伪终端（PTY）UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NATIVE_PTY`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NATIVE_PTY)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_NATIVE_TTY"></a>

## 168.20 `CONFIG_UART_NATIVE_TTY`

**提示（Prompt）**：与主机串口交互的 UART 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_NATIVE_TTY_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NATIVE_USE_NSI_ERRNO
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_HAS_POST_KERNEL_INIT if CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`drivers/serial/Kconfig.native_tty:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.native_tty#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NATIVE_USE_NSI_ERRNO`](P033_arch_posix_配置项参考.md#CONFIG_NATIVE_USE_NSI_ERRNO)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_HAS_POST_KERNEL_INIT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_POST_KERNEL_INIT)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_UART_NEORV32"></a>

## 168.21 `CONFIG_UART_NEORV32`

**提示（Prompt）**：NEORV32 UART

**说明（Help）**

此选项启用 NEORV32 的 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NEORV32_UART_ENABLED && CONFIG_SYSCON && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.neorv32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.neorv32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_NPCX"></a>

## 168.22 `CONFIG_UART_NPCX`

**提示（Prompt）**：Nuvoton NPCX 嵌入式控制器（EC）串行驱动

**说明（Help）**

此选项为 NPCX 系列处理器启用 UART 驱动。如果需要在 NPCX 微控制器（MCU）上使用串口，请选择 Y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.npcx:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.npcx#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_NPCX_FIFO_EX"></a>

## 168.23 `CONFIG_UART_NPCX_FIFO_EX`

**提示（Prompt）**：扩展 NPCX UART FIFO 驱动支持

**说明（Help）**

此选项为 NPCKN 处理器变体启用扩展 UART FIFO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if DT_HAS_NUVOTON_NPCX_UART_NPCKN_ENABLED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.npcx:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.npcx#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_NPCX_USE_MDMA"></a>

## 168.24 `CONFIG_UART_NPCX_USE_MDMA`

**提示（Prompt）**：Nuvoton NPCX 嵌入式控制器（EC）串行驱动 DMA 支持

**说明（Help）**

启用 NPCX UART 直接内存访问（DMA）模式支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NPCX && "0x0" != 0 && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_SUPPORT_ASYNC
```

**定义位置（Location）**：[`drivers/serial/Kconfig.npcx:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.npcx#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Nuvoton NPCX 嵌入式控制器（EC）串行驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_NPCX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NPCX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)。

<a id="CONFIG_UART_NRFX"></a>

## 168.25 `CONFIG_UART_NRFX`

**提示（Prompt）**：nRF UART nrfx 驱动

**说明（Help）**

为 nRF 微控制器（MCU）系列启用 nrfx UART 驱动支持。实例 ID 相同的外设不能同时使用，例如 `UART_0` 和 `UARTE_0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NORDIC_NRF_UART_ENABLED || DT_HAS_NORDIC_NRF_UARTE_ENABLED) && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_SUPPORT_ASYNC
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_NRFX_UARTE_BOUNCE_BUF_LEN"></a>

## 168.26 `CONFIG_UART_NRFX_UARTE_BOUNCE_BUF_LEN`

**提示（Prompt）**：接收中转缓冲区（RX Bounce Buffer）大小

**说明（Help）**

采用中转缓冲区（Bounce Buffer）变通方案时使用的缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[64, 1024]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_NRFX_UARTE_BOUNCE_BUF_SWAP_LATENCY"></a>

## 168.27 `CONFIG_UART_NRFX_UARTE_BOUNCE_BUF_SWAP_LATENCY`

**提示（Prompt）**：接收中转缓冲区切换提前量（RX Bounce Buffer Swap Latency），单位为微秒

**说明（Help）**

此选项决定驱动在当前中转缓冲区（Bounce Buffer）填满之前多早尝试切换缓冲区。时间必须足够长，以确保缓冲区后方的空间不被覆写。值过大会导致更频繁的缓冲区切换，影响性能。设置时应考虑潜在的中断处理延迟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
300
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_NRFX_UARTE_DIRECT_ISR"></a>

## 168.28 `CONFIG_UART_NRFX_UARTE_DIRECT_ISR`

**提示（Prompt）**：使用直接中断服务程序（Direct ISR）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_MULTITHREADING
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)。

<a id="CONFIG_UART_NRFX_UARTE_ENHANCED_RX"></a>

## 168.29 `CONFIG_UART_NRFX_UARTE_ENHANCED_RX`

**提示（Prompt）**：增强接收处理（Enhanced RX Handling）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用，因为除非使用 TIMER 外设统计接收（RX）字节数，否则此模式已成为默认模式。该接收处理模式在超时时切换缓冲区，相比另外两种模式——原默认模式和硬件辅助模式（Hardware-assisted Mode）——进行了改进。原默认模式在中断未及时处理时可能错误统计字节数；硬件辅助模式则需要一个 TIMER 外设实例和一个 PPI 通道，才能准确统计字节数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_UART_NRFX_UARTE_HFXO_ON_ACTIVE"></a>

## 168.30 `CONFIG_UART_NRFX_UARTE_HFXO_ON_ACTIVE`

**提示（Prompt）**：外设活动期间请求高频晶体振荡器（HFXO）

**说明（Help）**

在 UART 外设活动期间，请求启用高频晶体振荡器（HFXO）。与高频内部振荡器（HFINT）相比，这可提高比特率的准确性；代价是如果 HFXO 尚未运行，启用外设时会产生约 700 µs 的启动延迟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NRFX_UARTE && !CONFIG_SOC_NRF54H20 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_NRFX_UARTE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX_UARTE)、[`CONFIG_SOC_NRF54H20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UART_NRFX_UARTE`。

<a id="CONFIG_UART_NRFX_UARTE_NO_IRQ"></a>

## 168.31 `CONFIG_UART_NRFX_UARTE_NO_IRQ`

**提示（Prompt）**：无中断轮询（Polling without Interrupt）

**说明（Help）**

启用时完全不使用中断处理程序；如果不使用接收器，执行 `uart_poll_out` 后即可进入最低功耗状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NRFX_UARTE && !CONFIG_UART_ASYNC_API && !CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_NRFX_UARTE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX_UARTE)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UART_NRFX_UARTE`。

<a id="CONFIG_UART_NS16550"></a>

## 168.32 `CONFIG_UART_NS16550`

**提示（Prompt）**：NS16550 串行驱动（Serial Driver）

**说明（Help）**

此选项启用 NS16550 串行驱动（Serial Driver），可用于 x86 开发板上的串行硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NS16550_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT if n
CONFIG_PINCTRL if n
CONFIG_PCIE if n
CONFIG_DYNAMIC_INTERRUPTS if CONFIG_UART_INTERRUPT_DRIVEN && n
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_UART_NS16550_ACCESS_WORD_ONLY"></a>

## 168.33 `CONFIG_UART_NS16550_ACCESS_WORD_ONLY`

**提示（Prompt）**：NS16550 仅允许字访问（Word Access）

**说明（Help）**

某些情况下，例如 ARC HS Development Kit，NS16550（DesignWare UART）的外设空间仅允许字访问（Word Access），字节访问（Byte Access）会引发异常。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NS16550 && CONFIG_SERIAL
```

**被选择（Selected by）**

```text
CONFIG_SOC_SR100
CONFIG_SOC_SERIES_AM62X_M4
CONFIG_SOC_SERIES_AM64X_M4
CONFIG_SOC_SERIES_AM64X_R5
CONFIG_SOC_SERIES_J721E_R5
CONFIG_SOC_SERIES_J722S_R5
CONFIG_UART_NS16550_BCM283X_AUX
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_NS16550`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_AM62X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_M4)、[`CONFIG_SOC_SERIES_AM64X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_M4)、[`CONFIG_SOC_SERIES_AM64X_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_R5)、[`CONFIG_SOC_SERIES_J721E_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J721E_R5)、[`CONFIG_SOC_SERIES_J722S_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J722S_R5)、[`CONFIG_UART_NS16550_BCM283X_AUX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550_BCM283X_AUX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SR100`。

<a id="CONFIG_UART_NS16550_BCM283X_AUX"></a>

## 168.34 `CONFIG_UART_NS16550_BCM283X_AUX`

**提示（Prompt）**：支持 Broadcom BCM283x SoC 专用的 NS16550 变体

**说明（Help）**

启用此配置后，通过开启厂商专用扩展寄存器集（Vendor-specific Extended Register Set），可使用 Broadcom BCM283x 片上系统（SoC）的辅助 UART 端口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_BCM283X_AUX_UART_ENABLED && CONFIG_UART_NS16550 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UART_NS16550_ACCESS_WORD_ONLY
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_NS16550`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_NS16550_ACCESS_WORD_ONLY`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550_ACCESS_WORD_ONLY)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_NS16550_DRV_CMD"></a>

## 168.35 `CONFIG_UART_NS16550_DRV_CMD`

**提示（Prompt）**：驱动命令（Driver Commands）

**说明（Help）**

启用应用向驱动发送命令的 API。如果不确定，请选择 N。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_DRV_CMD && CONFIG_UART_NS16550 && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_DRV_CMD`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_DRV_CMD)、[`CONFIG_UART_NS16550`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_NS16550_DW8250_DW_APB"></a>

## 168.36 `CONFIG_UART_NS16550_DW8250_DW_APB`

**提示（Prompt）**：Synopsys DesignWare 8250

**说明（Help）**

启用 Synopsys DesignWare 8250 UART 控制器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DW_APB_UART_ENABLED && CONFIG_UART_NS16550 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_NS16550`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_NS16550_INTEL_LPSS_DMA"></a>

## 168.37 `CONFIG_UART_NS16550_INTEL_LPSS_DMA`

**提示（Prompt）**：NS16550 的 INTEL LPSS 支持

**说明（Help）**

允许异步操作（Async Operations）使用 INTEL LPSS 内部直接内存访问（DMA）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NS16550 && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_SUPPORT_ASYNC
CONFIG_DMA if CONFIG_UART_ASYNC_API
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_NS16550`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)。

<a id="CONFIG_UART_NS16550_ITE_HIGH_SPEED_BAUDRATE"></a>

## 168.38 `CONFIG_UART_NS16550_ITE_HIGH_SPEED_BAUDRATE`

**提示（Prompt）**：IT8XXX2 专用波特率配置（Baud Rate Configuration）

**说明（Help）**

启用 IT8XXX2 专用波特率配置，适用于高速波特率配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NS16550 && CONFIG_SERIAL
```

**被选择（Selected by）**

```text
CONFIG_UART_ITE_IT51XXX
CONFIG_UART_ITE_IT8XXX2
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_NS16550`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_ITE_IT51XXX`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ITE_IT51XXX)、[`CONFIG_UART_ITE_IT8XXX2`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ITE_IT8XXX2)。

<a id="CONFIG_UART_NS16550_LINE_CTRL"></a>

## 168.39 `CONFIG_UART_NS16550_LINE_CTRL`

**提示（Prompt）**：面向应用的串行线路控制（Serial Line Control）

**说明（Help）**

启用应用控制串行线路的 API，例如允许发送（CTS）和请求发送（RTS）。如果不确定，请选择 N。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_LINE_CTRL && CONFIG_UART_NS16550 && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_LINE_CTRL`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_LINE_CTRL)、[`CONFIG_UART_NS16550`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_NS16550_TI_K3"></a>

## 168.40 `CONFIG_UART_NS16550_TI_K3`

**提示（Prompt）**：支持 TI K3 SoC 专用的 NS16550 变体

**说明（Help）**

启用此配置后，通过开启厂商专用扩展寄存器集（Vendor-specific Extended Register Set），可使用 Texas Instruments K3 片上系统（SoC）的 UART 端口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NS16550 && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_NS16550`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_NS16550_VARIANT"></a>

## 168.41 `CONFIG_UART_NS16550_VARIANT`

**提示（Prompt）**：UART 变体（Variant）

**说明（Help）**

选择 UART 设备变体（Device Variant）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NS16550 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
CONFIG_UART_NS16550_VARIANT_NS16550
```

**可选项（Choices）**

```text
CONFIG_UART_NS16550_VARIANT_NS16550
CONFIG_UART_NS16550_VARIANT_NS16450
CONFIG_UART_NS16550_VARIANT_NS16750
CONFIG_UART_NS16550_VARIANT_NS16950
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_NS16550`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_NS16550_VARIANT_NS16550`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550_VARIANT_NS16550)、[`CONFIG_UART_NS16550_VARIANT_NS16450`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550_VARIANT_NS16450)、[`CONFIG_UART_NS16550_VARIANT_NS16750`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550_VARIANT_NS16750)、[`CONFIG_UART_NS16550_VARIANT_NS16950`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550_VARIANT_NS16950)。

<a id="CONFIG_UART_NS16550_VARIANT_NS16450"></a>

## 168.42 `CONFIG_UART_NS16550_VARIANT_NS16450`

**提示（Prompt）**：UART 16450（无 FIFO）

**说明（Help）**

使控制器在不使用 FIFO 的 16450 模式下运行。对于 FIFO 模式接收中断的触发阈值（Trigger Level）和字符超时（Character Timeout）无法正常工作的硬件，应选择此模式；16450 模式改为每收到一个字符就触发接收数据可用中断（Received Data Available Interrupt）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_NS16550_VARIANT>
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver） → UART 变体（Variant）

**配置项引用（Symbol References）**：[`CONFIG_UART_NS16550_VARIANT`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550_VARIANT)。

<a id="CONFIG_UART_NS16550_VARIANT_NS16550"></a>

## 168.43 `CONFIG_UART_NS16550_VARIANT_NS16550`

**提示（Prompt）**：UART 16550（16 字节 FIFO）

**说明（Help）**

如果 UART 控制器为 16550，则启用 16 字节 FIFO 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_NS16550_VARIANT>
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver） → UART 变体（Variant）

**配置项引用（Symbol References）**：[`CONFIG_UART_NS16550_VARIANT`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550_VARIANT)。

<a id="CONFIG_UART_NS16550_VARIANT_NS16750"></a>

## 168.44 `CONFIG_UART_NS16550_VARIANT_NS16750`

**提示（Prompt）**：UART 16750（64 字节 FIFO 和自动流控制）

**说明（Help）**

如果 UART 控制器为 16750，则启用 64 字节 FIFO 和自动硬件流控制（Automatic Hardware Flow Control）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_NS16550_VARIANT>
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver） → UART 变体（Variant）

**配置项引用（Symbol References）**：[`CONFIG_UART_NS16550_VARIANT`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550_VARIANT)。

<a id="CONFIG_UART_NS16550_VARIANT_NS16950"></a>

## 168.45 `CONFIG_UART_NS16550_VARIANT_NS16950`

**提示（Prompt）**：UART 16950（128 字节 FIFO 和自动流控制）

**说明（Help）**

启用 128 字节 FIFO 和自动硬件流控制（Automatic Hardware Flow Control）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_NS16550_VARIANT>
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver） → UART 变体（Variant）

**配置项引用（Symbol References）**：[`CONFIG_UART_NS16550_VARIANT`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550_VARIANT)。

<a id="CONFIG_UART_NS16550_WA_ISR_REENABLE_INTERRUPT"></a>

## 168.46 `CONFIG_UART_NS16550_WA_ISR_REENABLE_INTERRUPT`

**提示（Prompt）**：在中断服务程序（ISR）结束时切换 IER，重新启用中断

**说明（Help）**

某些配置下，例如边沿触发中断（Edge-triggered Interrupt），中断服务程序（ISR）执行期间发生新的可中断事件，但由于 IIR 持续保持中断有效，主机中断控制器无法察觉新事件。

例如，回调先处理接收（RX），再处理发送（TX）。如果发送处理结束前又收到一个字符，产生接收中断时发送中断仍然有效，主机中断控制器可能无法察觉这一新事件。因此，必要时在 ISR 末尾切换 IER，使中断重新置为有效，从而促使主机中断控制器再次调用 ISR。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_UART_NS16550 && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver） → NS16550 变通方案（Workarounds）

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_UART_NS16550`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_NS16550_WA_TX_FIFO_EMPTY_INTERRUPT"></a>

## 168.47 `CONFIG_UART_NS16550_WA_TX_FIFO_EMPTY_INTERRUPT`

**提示（Prompt）**：发送 FIFO 已空时直接调用回调

**说明（Help）**

调用 `uart_ns16550_irq_tx_enable()` 以等待发送 FIFO（TX FIFO）就绪中断时，只有当前状态非空才会触发该中断。因此，如果当前状态已经为空，需要直接调用回调函数来解决此问题。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_UART_NS16550 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SOC_EGIS_ET171
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ns16550:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ns16550#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NS16550 串行驱动（Serial Driver） → NS16550 变通方案（Workarounds）

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_UART_NS16550`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SHELL_BACKEND_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)。

<a id="CONFIG_UART_NUMAKER"></a>

## 168.48 `CONFIG_UART_NUMAKER`

**提示（Prompt）**：Nuvoton NUMAKER MCU 串行驱动

**说明（Help）**

此选项为 Nuvoton Numaker 系列处理器启用 UART 驱动。如果需要在 Nuvoton Numaker 微控制器（MCU）上使用串口，请选择 Y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_HAS_NUMAKER_UART
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_HAS_NUMAKER_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_UART)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_NUMICRO"></a>

## 168.49 `CONFIG_UART_NUMICRO`

**提示（Prompt）**：NUVOTON MCU 串行驱动

**说明（Help）**

此选项为 Nuvoton Numicro 系列处理器启用 UART 驱动。需要在 Nuvoton 微控制器（MCU）上使用串口时，请选择 Y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMICRO_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_HAS_NUMICRO_UART
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.numicro:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.numicro#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_HAS_NUMICRO_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMICRO_UART)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_NXP_LPUART_ASYNC_API_SUPPORT"></a>

## 168.50 `CONFIG_UART_NXP_LPUART_ASYNC_API_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过是否为 LPUART 启用 `dmas`，表明其是否支持异步 API（Async API）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_MCUX_LPUART && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_SUPPORT_ASYNC
CONFIG_DMA if CONFIG_UART_ASYNC_API
CONFIG_CACHE_MANAGEMENT if CONFIG_UART_ASYNC_API && CONFIG_DCACHE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.mcux_lpuart:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mcux_lpuart#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → MCUX LPUART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_MCUX_LPUART`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_MCUX_LPUART)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)。

<a id="CONFIG_UART_NXP_S32_LINFLEXD"></a>

## 168.51 `CONFIG_UART_NXP_S32_LINFLEXD`

**提示（Prompt）**：NXP S32 系列处理器的 LINFlexD UART 驱动

**说明（Help）**

为 NXP S32 系列处理器启用 LINFlexD UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_LINFLEXD_ENABLED && CONFIG_SERIAL
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
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nxp_s32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nxp_s32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_UART_NXP_S32_POLL_IN_TIMEOUT"></a>

## 168.52 `CONFIG_UART_NXP_S32_POLL_IN_TIMEOUT`

**提示（Prompt）**：阻塞模式下接收一个字节的最长时间

**说明（Help）**

阻塞模式（Blocking Mode）下接收一个字节的最长时间，单位为微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NXP_S32_LINFLEXD && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nxp_s32:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nxp_s32#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NXP S32 系列处理器的 LINFlexD UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_NXP_S32_LINFLEXD`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NXP_S32_LINFLEXD)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_NXP_S32_POLL_OUT_TIMEOUT"></a>

## 168.53 `CONFIG_UART_NXP_S32_POLL_OUT_TIMEOUT`

**提示（Prompt）**：阻塞模式下传输一个字节的最长时间

**说明（Help）**

阻塞模式（Blocking Mode）下传输一个字节的最长时间，单位为微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_NXP_S32_LINFLEXD && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nxp_s32:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nxp_s32#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NXP S32 系列处理器的 LINFlexD UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_NXP_S32_LINFLEXD`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NXP_S32_LINFLEXD)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_OPENTITAN"></a>

## 168.54 `CONFIG_UART_OPENTITAN`

**提示（Prompt）**：OpenTitan UART

**说明（Help）**

启用 OpenTitan UART 串行驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LOWRISC_OPENTITAN_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.opentitan:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.opentitan#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)。

<a id="CONFIG_UART_PIPE"></a>

## 168.55 `CONFIG_UART_PIPE`

**提示（Prompt）**：管道 UART（Pipe UART）驱动

**说明（Help）**

启用管道 UART（Pipe UART）驱动，使应用能够通过 UART 使用自定义协议通信。与控制台 UART 驱动不同，此驱动不检查接收数据；接收协议数据的所有处理都由应用提供的回调负责。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_UART_INTERRUPT_DRIVEN
```

**被选择（Selected by）**

```text
CONFIG_IEEE802154_UPIPE
CONFIG_SLIP
CONFIG_NET_SLIP_TAP
```

**定义位置（Location）**：[`drivers/serial/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_IEEE802154_UPIPE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_UPIPE)、[`CONFIG_SLIP`](P131_drivers_net_配置项参考.md#CONFIG_SLIP)、[`CONFIG_NET_SLIP_TAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SLIP_TAP)。

<a id="CONFIG_UART_PL011"></a>

## 168.56 `CONFIG_UART_PL011`

**提示（Prompt）**：ARM PL011 UART 驱动

**说明（Help）**

此选项为 PL011 启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ARM_PL011_ENABLED || DT_HAS_ARM_SBSA_UART_ENABLED) && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_PINCTRL if n
```

**定义位置（Location）**：[`drivers/serial/Kconfig.pl011:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.pl011#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_PL011_SBSA"></a>

## 168.57 `CONFIG_UART_PL011_SBSA`

**提示（Prompt）**：SBSA UART

**说明（Help）**

为 PL011 驱动启用 SBSA 模式。SBSA 的原文全称为 Server Based System Architecture（基于服务器的系统架构）。该规范的定义之一是简化的 UART 接口，它是 PL011 接口的子集。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_PL011 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if DT_HAS_ARM_SBSA_UART_ENABLED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.pl011:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.pl011#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → ARM PL011 UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_PL011`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_PL011)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_PSOC6"></a>

## 168.58 `CONFIG_UART_PSOC6`

**提示（Prompt）**：PSOC 6 MCU SCB 串行驱动

**说明（Help）**

此选项为 PSOC 6 片上系统（SoC）系列启用 SCB[UART] 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CYPRESS_PSOC6_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_USE_INFINEON_UART
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.psoc6:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.psoc6#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_USE_INFINEON_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_UART)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_QUICKLOGIC_USBSERIALPORT_S3B"></a>

## 168.59 `CONFIG_UART_QUICKLOGIC_USBSERIALPORT_S3B`

**提示（Prompt）**：QuickLogic USBserialport_S3B 串行驱动

**说明（Help）**

此选项启用 QuickLogic USBserialport_S3B 串行驱动（Serial Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_QUICKLOGIC_USBSERIALPORT_S3B_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.ql_usbserialport_s3b:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ql_usbserialport_s3b#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_RA8_SCI_B"></a>

## 168.60 `CONFIG_UART_RA8_SCI_B`

**提示（Prompt）**：Renesas RA SCI_B UART

**说明（Help）**

启用 Renesas RA SCI_B UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA8_UART_SCI_B_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_SUPPORT_ASYNC
CONFIG_USE_RA_FSP_SCI_B_UART
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_ra8:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_ra8#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_USE_RA_FSP_SCI_B_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SCI_B_UART)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_RA8_SCI_B_UART_DMAC"></a>

## 168.61 `CONFIG_UART_RA8_SCI_B_UART_DMAC`

**提示（Prompt）**：Renesas RA SCI_B UART DMAC

**说明（Help）**

为 RA 系列的 SCI-B UART 驱动启用直接内存访问控制器（Direct Memory Access Controller，DMAC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_RA8_SCI_B && CONFIG_UART_ASYNC_API && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DMA
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_ra8:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_ra8#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Renesas RA SCI_B UART

**配置项引用（Symbol References）**：[`CONFIG_UART_RA8_SCI_B`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RA8_SCI_B)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_USE_RA_FSP_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DMA)。

<a id="CONFIG_UART_RA8_SCI_B_UART_DTC"></a>

## 168.62 `CONFIG_UART_RA8_SCI_B_UART_DTC`

**提示（Prompt）**：Renesas RA SCI_B UART DTC

**说明（Help）**

为 RA 系列的 SCI-B UART 驱动启用数据传输控制器（Data Transfer Controller，DTC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_RA8_SCI_B && CONFIG_UART_ASYNC_API && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
n || n
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DTC
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_ra8:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_ra8#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Renesas RA SCI_B UART

**配置项引用（Symbol References）**：[`CONFIG_UART_RA8_SCI_B`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RA8_SCI_B)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_USE_RA_FSP_DTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DTC)。

<a id="CONFIG_UART_RA_SCI_B_UART_FIFO_ENABLE"></a>

## 168.63 `CONFIG_UART_RA_SCI_B_UART_FIFO_ENABLE`

**提示（Prompt）**：启用 RA SCI_B UART FIFO

**说明（Help）**

启用 RA SCI_B FIFO。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_RA8_SCI_B && (CONFIG_UART_INTERRUPT_DRIVEN || CONFIG_UART_ASYNC_API) && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if CONFIG_UART_INTERRUPT_DRIVEN
n if CONFIG_UART_ASYNC_API
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_ra8:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_ra8#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Renesas RA SCI_B UART

**配置项引用（Symbol References）**：[`CONFIG_UART_RA8_SCI_B`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RA8_SCI_B)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_RA_SCI_UART_FIFO_ENABLE"></a>

## 168.64 `CONFIG_UART_RA_SCI_UART_FIFO_ENABLE`

**提示（Prompt）**：启用 RA SCI UART FIFO

**说明（Help）**

启用 RA SCI FIFO。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_SCI_RA && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_ra:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_ra#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Renesas RA SCI UART

**配置项引用（Symbol References）**：[`CONFIG_UART_SCI_RA`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_SCI_RA)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_RCAR"></a>

## 168.65 `CONFIG_UART_RCAR`

**提示（Prompt）**：Renesas R-Car UART 驱动

**说明（Help）**

启用 Renesas R-Car UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_RENESAS_RCAR_SCIF_ENABLED || DT_HAS_RENESAS_RCAR_HSCIF_ENABLED) && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.rcar:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.rcar#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_RENESAS_RA_SAU"></a>

## 168.66 `CONFIG_UART_RENESAS_RA_SAU`

**提示（Prompt）**：Renesas RA SAU UART 驱动

**说明（Help）**

启用 Renesas RA SAU UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_UART_SAU_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_USE_RA_FSP_SAU_UART
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_ra:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_ra#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_USE_RA_FSP_SAU_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SAU_UART)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_RENESAS_RX"></a>

## 168.67 `CONFIG_UART_RENESAS_RX`

**提示（Prompt）**：Renesas RX 系列 UART 驱动

**说明（Help）**

启用 Renesas RX 系列 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_UART_SCI_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_SUPPORT_ASYNC
CONFIG_USE_RX_RDP_SCI_UART
CONFIG_RENESAS_RX_DTC if CONFIG_UART_ASYNC_API
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_rx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_rx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_USE_RX_RDP_SCI_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RX_RDP_SCI_UART)、[`CONFIG_RENESAS_RX_DTC`](P123_drivers_misc_配置项参考.md#CONFIG_RENESAS_RX_DTC)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_RENESAS_RX_QEMU"></a>

## 168.68 `CONFIG_UART_RENESAS_RX_QEMU`

**提示（Prompt）**：Renesas RX 系列 UART 驱动

**说明（Help）**

启用 Renesas RX 系列 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_UART_SCI_QEMU_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_rx_qemu:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_rx_qemu#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)。

<a id="CONFIG_UART_RENESAS_RX_SCI_B"></a>

## 168.69 `CONFIG_UART_RENESAS_RX_SCI_B`

**提示（Prompt）**：Renesas RX 系列 UART 驱动

**说明（Help）**

启用 Renesas RX 系列基于 SCI B 硬件的 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_UART_SCI_B_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_USE_RX_FSP_SCI_B_UART
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_rx:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_rx#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_USE_RX_FSP_SCI_B_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RX_FSP_SCI_B_UART)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_RENESAS_RZA2M_SCIF"></a>

## 168.70 `CONFIG_UART_RENESAS_RZA2M_SCIF`

**提示（Prompt）**：Renesas A2M SCIF UART 驱动

**说明（Help）**

启用 Renesas SCIF UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZA2M_SCIF_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_rz:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_rz#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_RENESAS_RZG_INIT_DELAY_MS"></a>

## 168.71 `CONFIG_UART_RENESAS_RZG_INIT_DELAY_MS`

**提示（Prompt）**：UART 初始化延迟，单位为毫秒

**说明（Help）**

此选项引入延迟，在 M33 初始化 UART 之前，先等待 A55 完成其设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_RENESAS_RZ_SCIF && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
8000
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_rz:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_rz#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_RENESAS_RZ_SCIF`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RENESAS_RZ_SCIF)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_RENESAS_RZ_SCI"></a>

## 168.72 `CONFIG_UART_RENESAS_RZ_SCI`

**提示（Prompt）**：Renesas RZ SCI UART

**说明（Help）**

启用 Renesas RZ SCI UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_SCI_UART_ENABLED && CONFIG_SERIAL
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
CONFIG_USE_RZ_FSP_SCI_UART
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_rz:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_rz#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_USE_RZ_FSP_SCI_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_SCI_UART)。

<a id="CONFIG_UART_RENESAS_RZ_SCIF"></a>

## 168.73 `CONFIG_UART_RENESAS_RZ_SCIF`

**提示（Prompt）**：Renesas RZ SCIF UART

**说明（Help）**

启用 Renesas RZ SCIF UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_SCIF_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_USE_RZ_FSP_SCIF_UART
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_rz:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_rz#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_USE_RZ_FSP_SCIF_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_SCIF_UART)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_RENESAS_RZ_SCI_B"></a>

## 168.74 `CONFIG_UART_RENESAS_RZ_SCI_B`

**提示（Prompt）**：Renesas RZ SCI-B UART

**说明（Help）**

启用 Renesas RZ SCI-B UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_SCI_B_UART_ENABLED && CONFIG_SERIAL
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
CONFIG_USE_RZ_FSP_SCI_UART
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_rz:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_rz#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_USE_RZ_FSP_SCI_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_SCI_UART)。

<a id="CONFIG_UART_RPI_PICO_PIO"></a>

## 168.75 `CONFIG_UART_RPI_PICO_PIO`

**提示（Prompt）**：Raspberry Pi 可编程输入输出（PIO）UART 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_UART_PIO_ENABLED && CONFIG_RESET && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_PICOSDK_USE_PIO
CONFIG_PICOSDK_USE_CLAIM
CONFIG_PINCTRL
CONFIG_SERIAL_HAS_POST_KERNEL_INIT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_PICOSDK_USE_PIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_PIO)、[`CONFIG_PICOSDK_USE_CLAIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_CLAIM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_HAS_POST_KERNEL_INIT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_POST_KERNEL_INIT)。

<a id="CONFIG_UART_RPMSG"></a>

## 168.76 `CONFIG_UART_RPMSG`

**提示（Prompt）**：使用远程处理器消息（RPMSG）UART

**说明（Help）**

启用基于远程处理器消息（RPMSG）的 UART。应用通过 `remoteproc` 加载到协处理器（Co-processor）时，可使用此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSG_SERVICE && DT_HAS_RPMSG_UART_ENABLED && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_POST_KERNEL_INIT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.rpmsg:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.rpmsg#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RPMSG_SERVICE)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_POST_KERNEL_INIT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_POST_KERNEL_INIT)。

<a id="CONFIG_UART_RPMSG_RX_BUF_SIZE"></a>

## 168.77 `CONFIG_UART_RPMSG_RX_BUF_SIZE`

**提示（Prompt）**：内部接收（RX）缓冲区大小

**说明（Help）**

此选项用于设置接收缓冲区（Receive Buffer）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_RPMSG && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/serial/Kconfig.rpmsg:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.rpmsg#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 使用远程处理器消息（RPMSG）UART

**配置项引用（Symbol References）**：[`CONFIG_UART_RPMSG`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RPMSG)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_RTS5912"></a>

## 168.78 `CONFIG_UART_RTS5912`

**提示（Prompt）**：Realtek RTS5912 嵌入式控制器（EC）的 UART 驱动

**说明（Help）**

此选项启用 RTS5912 UART 封装驱动（Wrapper Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RTS5912 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if DT_HAS_REALTEK_RTS5912_UART_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.realtek_rts5912:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.realtek_rts5912#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_UART_RTS5912_INIT_PRIORITY"></a>

## 168.79 `CONFIG_UART_RTS5912_INIT_PRIORITY`

**提示（Prompt）**：RTS5912 UART 封装初始化优先级（Wrapper Init Priority）

**说明（Help）**

Realtek RTS5912 UART 封装驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_RTS5912 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
51
```

**定义位置（Location）**：[`drivers/serial/Kconfig.realtek_rts5912:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.realtek_rts5912#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Realtek RTS5912 嵌入式控制器（EC）的 UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_RTS5912`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RTS5912)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_RTT"></a>

## 168.80 `CONFIG_UART_RTT`

**提示（Prompt）**：UART RTT 驱动

**说明（Help）**

此选项允许将实时传输（RTT）通道作为 UART 设备访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SEGGER_RTT_UART_ENABLED && CONFIG_USE_SEGGER_RTT && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SEGGER_RTT_CUSTOM_LOCKING
CONFIG_SERIAL_SUPPORT_ASYNC
```

**定义位置（Location）**：[`drivers/serial/Kconfig.rtt:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.rtt#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_SEGGER_RTT)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SEGGER_RTT_CUSTOM_LOCKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_RTT_CUSTOM_LOCKING)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)。

<a id="CONFIG_UART_RTT_0"></a>

## 168.81 `CONFIG_UART_RTT_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在默认 RTT 通道 0 上启用 UART。默认通道必须配置为非阻塞跳过模式（Non-blocking Skip Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS >= 1 && CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS >= 1 && CONFIG_SEGGER_RTT_MODE_NO_BLOCK_SKIP && CONFIG_UART_RTT && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_UART_RTT_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.rtt:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.rtt#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → UART RTT 驱动

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS)、[`CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS)、[`CONFIG_SEGGER_RTT_MODE_NO_BLOCK_SKIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_RTT_MODE_NO_BLOCK_SKIP)、[`CONFIG_UART_RTT`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RTT)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_UART_RTT_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RTT_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UART_RTT_DRIVER`。

<a id="CONFIG_UART_RTT_1"></a>

## 168.82 `CONFIG_UART_RTT_1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在 RTT 通道 1 上启用 UART

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS >= 2 && CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS >= 2 && CONFIG_UART_RTT && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_UART_RTT_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.rtt:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.rtt#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → UART RTT 驱动

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS)、[`CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS)、[`CONFIG_UART_RTT`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RTT)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_UART_RTT_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RTT_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UART_RTT_DRIVER`。

<a id="CONFIG_UART_RTT_2"></a>

## 168.83 `CONFIG_UART_RTT_2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在 RTT 通道 2 上启用 UART

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS >= 3 && CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS >= 3 && CONFIG_UART_RTT && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_UART_RTT_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.rtt:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.rtt#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → UART RTT 驱动

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS)、[`CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS)、[`CONFIG_UART_RTT`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RTT)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_UART_RTT_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RTT_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UART_RTT_DRIVER`。

<a id="CONFIG_UART_RTT_3"></a>

## 168.84 `CONFIG_UART_RTT_3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在 RTT 通道 3 上启用 UART

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS >= 4 && CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS >= 4 && CONFIG_UART_RTT && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_UART_RTT_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.rtt:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.rtt#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → UART RTT 驱动

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS)、[`CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS)、[`CONFIG_UART_RTT`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RTT)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_UART_RTT_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RTT_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UART_RTT_DRIVER`。

<a id="CONFIG_UART_RV32M1_LPUART"></a>

## 168.85 `CONFIG_UART_RV32M1_LPUART`

**提示（Prompt）**：RV32M1 LPUART 驱动

**说明（Help）**

启用 RV32M1 LPUART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OPENISA_RV32M1_LPUART_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.rv32m1_lpuart:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.rv32m1_lpuart#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_RZT2M"></a>

## 168.86 `CONFIG_UART_RZT2M`

**提示（Prompt）**：Renesas RZ/T2M UART 驱动

**说明（Help）**

启用 Renesas RZ/T2M UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZT2M_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.rzt2m:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.rzt2m#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_SAM"></a>

## 168.87 `CONFIG_UART_SAM`

**提示（Prompt）**：Atmel SAM MCU 系列 UART 驱动

**说明（Help）**

此选项为 Atmel SAM 微控制器（MCU）启用 UARTx 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_UART_ENABLED && CONFIG_SERIAL
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
```

**定义位置（Location）**：[`drivers/serial/Kconfig.uart_sam:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.uart_sam#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_SAM0"></a>

## 168.88 `CONFIG_UART_SAM0`

**提示（Prompt）**：Atmel SAM0 系列 SERCOM USART 驱动

**说明（Help）**

此选项为 Atmel SAM0 微控制器（MCU）启用 SERCOMx USART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_UART_ENABLED && CONFIG_SERIAL
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
CONFIG_SERIAL_SUPPORT_ASYNC if DT_HAS_ATMEL_SAM0_DMAC_ENABLED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.sam0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.sam0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)。

<a id="CONFIG_UART_SAM0_ASYNC"></a>

## 168.89 `CONFIG_UART_SAM0_ASYNC`

**提示（Prompt）**：Atmel SAM0 系列的异步 UART（Async UART）支持。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_SAM0 && CONFIG_UART_SAM0 && CONFIG_UART_ASYNC_API && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.sam0:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.sam0#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Atmel SAM0 系列 SERCOM USART 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_SAM0`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_SAM0)、[`CONFIG_UART_SAM0`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_SAM0)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_SCI_RA"></a>

## 168.90 `CONFIG_UART_SCI_RA`

**提示（Prompt）**：Renesas RA SCI UART

**说明（Help）**

启用 Renesas RA SCI UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_SCI_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_SUPPORT_ASYNC
CONFIG_USE_RA_FSP_SCI_UART
CONFIG_USE_RA_FSP_DTC if CONFIG_UART_ASYNC_API
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.renesas_ra:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.renesas_ra#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_USE_RA_FSP_SCI_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SCI_UART)、[`CONFIG_USE_RA_FSP_DTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DTC)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_SEDI"></a>

## 168.91 `CONFIG_UART_SEDI`

**提示（Prompt）**：Intel SEDI UART 驱动

**说明（Help）**

此选项启用 Intel SEDI UART 驱动。该驱动是一个轻量适配驱动（Shim Driver），构建于 `hal-intel` 模块中的 SEDI 裸机 UART 驱动（Bare Metal UART Driver）之上。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_SEDI_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.sedi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.sedi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_SF32LB"></a>

## 168.92 `CONFIG_UART_SF32LB`

**提示（Prompt）**：SiFli SF32LB UART 驱动

**说明（Help）**

此选项启用 SiFli SF32LB UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_USART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_SUPPORT_ASYNC if DT_HAS_SIFLI_SF32LB_DMAC_ENABLED
CONFIG_DMA if CONFIG_UART_ASYNC_API
CONFIG_PINCTRL
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_UART_SHAKTI"></a>

## 168.93 `CONFIG_UART_SHAKTI`

**提示（Prompt）**：Shakti UART 驱动

**说明（Help）**

启用 Shakti UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SHAKTI_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.shakti:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.shakti#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_SHELL"></a>

## 168.94 `CONFIG_UART_SHELL`

**提示（Prompt）**：UART 命令行命令（Shell Commands）

**说明（Help）**

UART 命令行命令（Shell Commands）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig:160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L160)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_SI32_USART"></a>

## 168.95 `CONFIG_UART_SI32_USART`

**提示（Prompt）**：SI32 USART MCU 串行驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SI32_USART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.si32:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.si32#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_SIFIVE"></a>

## 168.96 `CONFIG_UART_SIFIVE`

**提示（Prompt）**：SiFive Freedom 串行驱动（Serial Driver）

**说明（Help）**

此选项启用 SiFive Freedom 串行驱动（Serial Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFIVE_UART0_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_PINCTRL if CONFIG_SOC_SERIES_FE300
```

**定义位置（Location）**：[`drivers/serial/Kconfig.sifive:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.sifive#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SOC_SERIES_FE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FE300)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_FE300`。

<a id="CONFIG_UART_SIFIVE_PORT_0"></a>

## 168.97 `CONFIG_UART_SIFIVE_PORT_0`

**提示（Prompt）**：SIFIVE 端口 0（Port 0）

**说明（Help）**

指示驱动在启动时根据下面的其他配置选项，配置 UART 端口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_SIFIVE && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.sifive:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.sifive#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → SiFive Freedom 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_SIFIVE`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_SIFIVE)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_SIFIVE_PORT_0_RXCNT_IRQ"></a>

## 168.98 `CONFIG_UART_SIFIVE_PORT_0_RXCNT_IRQ`

**提示（Prompt）**：端口 0 接收中断阈值计数（RX Interrupt Threshold Count）

**说明（Help）**

端口 0 触发接收 FIFO（RX FIFO）中断的接收阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_SIFIVE_PORT_0 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/serial/Kconfig.sifive:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.sifive#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → SiFive Freedom 串行驱动（Serial Driver） → SIFIVE 端口 0（Port 0）

**配置项引用（Symbol References）**：[`CONFIG_UART_SIFIVE_PORT_0`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_SIFIVE_PORT_0)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_SIFIVE_PORT_0_TXCNT_IRQ"></a>

## 168.99 `CONFIG_UART_SIFIVE_PORT_0_TXCNT_IRQ`

**提示（Prompt）**：端口 0 发送中断阈值计数（TX Interrupt Threshold Count）

**说明（Help）**

端口 0 触发发送 FIFO（TX FIFO）中断的发送阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_SIFIVE_PORT_0 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/serial/Kconfig.sifive:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.sifive#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → SiFive Freedom 串行驱动（Serial Driver） → SIFIVE 端口 0（Port 0）

**配置项引用（Symbol References）**：[`CONFIG_UART_SIFIVE_PORT_0`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_SIFIVE_PORT_0)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_SIFIVE_PORT_1"></a>

## 168.100 `CONFIG_UART_SIFIVE_PORT_1`

**提示（Prompt）**：SIFIVE 端口 1（Port 1）

**说明（Help）**

指示驱动在启动时根据下面的其他配置选项，配置 UART 端口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_SIFIVE && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.sifive:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.sifive#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → SiFive Freedom 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_SIFIVE`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_SIFIVE)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<!-- kconfig-navigation -->

[上一章](P167_drivers_serial_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P169_drivers_serial_配置项参考_5.md)
