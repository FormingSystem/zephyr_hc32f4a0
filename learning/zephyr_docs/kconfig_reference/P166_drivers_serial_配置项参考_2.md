---
id: learning.zephyr-docs.kconfig-reference.page-166
title: "`drivers/serial`配置项参考（2/5）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第166章\_`drivers/serial`配置项参考（2/5）

本章翻译官方 Kconfig 数据库中 `drivers/serial` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_UART_135_ASYNC"></a>

## 166.1 `CONFIG_UART_135_ASYNC`

**提示（Prompt）**：端口 135 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_135_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE135 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_135_INTERRUPT_DRIVEN`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_135_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE135`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE135)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE135`。

<a id="CONFIG_UART_135_COUNT_BYTES_WITH_TIMER"></a>

## 166.2 `CONFIG_UART_135_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_135_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 166.3 `CONFIG_UART_135_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_135_NRF_USE_TIMER || CONFIG_UART_135_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE135 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_135_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_135_NRF_USE_TIMER)、[`CONFIG_UART_135_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_135_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE135`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE135)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE135`。

<a id="CONFIG_UART_135_ENHANCED_POLL_OUT"></a>

## 166.4 `CONFIG_UART_135_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 135 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE135 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE135 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE135`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE135)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE135`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_135_INTERRUPT_DRIVEN"></a>

## 166.5 `CONFIG_UART_135_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 135 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE135 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE135`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE135)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE135`。

<a id="CONFIG_UART_135_NRF_ASYNC_LOW_POWER"></a>

## 166.6 `CONFIG_UART_135_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE135 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE135 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE135`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE135)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE135`。

<a id="CONFIG_UART_135_NRF_HW_ASYNC"></a>

## 166.7 `CONFIG_UART_135_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE135 && !n && CONFIG_HAS_HW_NRF_UARTE135 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE135`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE135)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE135`。

<a id="CONFIG_UART_135_NRF_HW_ASYNC_TIMER"></a>

## 166.8 `CONFIG_UART_135_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_135_NRF_USE_TIMER && CONFIG_UART_135_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE135 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_135_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_135_NRF_USE_TIMER)、[`CONFIG_UART_135_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_135_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE135`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE135)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE135`。

<a id="CONFIG_UART_135_NRF_PARITY_BIT"></a>

## 166.9 `CONFIG_UART_135_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE135 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE135`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE135)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE135`。

<a id="CONFIG_UART_135_NRF_TX_BUFFER_SIZE"></a>

## 166.10 `CONFIG_UART_135_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE135 && CONFIG_HAS_HW_NRF_UARTE135 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE135`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE135)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE135`。

<a id="CONFIG_UART_135_NRF_USE_TIMER"></a>

## 166.11 `CONFIG_UART_135_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_136_ASYNC"></a>

## 166.12 `CONFIG_UART_136_ASYNC`

**提示（Prompt）**：端口 136 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_136_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE136 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_136_INTERRUPT_DRIVEN`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_136_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE136)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE136`。

<a id="CONFIG_UART_136_COUNT_BYTES_WITH_TIMER"></a>

## 166.13 `CONFIG_UART_136_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_136_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 166.14 `CONFIG_UART_136_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_136_NRF_USE_TIMER || CONFIG_UART_136_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE136 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_136_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_136_NRF_USE_TIMER)、[`CONFIG_UART_136_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_136_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE136)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE136`。

<a id="CONFIG_UART_136_ENHANCED_POLL_OUT"></a>

## 166.15 `CONFIG_UART_136_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 136 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE136 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE136 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE136)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE136`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_136_INTERRUPT_DRIVEN"></a>

## 166.16 `CONFIG_UART_136_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 136 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE136 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE136)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE136`。

<a id="CONFIG_UART_136_NRF_ASYNC_LOW_POWER"></a>

## 166.17 `CONFIG_UART_136_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE136 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE136 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE136)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE136`。

<a id="CONFIG_UART_136_NRF_HW_ASYNC"></a>

## 166.18 `CONFIG_UART_136_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE136 && !n && CONFIG_HAS_HW_NRF_UARTE136 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE136)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE136`。

<a id="CONFIG_UART_136_NRF_HW_ASYNC_TIMER"></a>

## 166.19 `CONFIG_UART_136_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_136_NRF_USE_TIMER && CONFIG_UART_136_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE136 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_136_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_136_NRF_USE_TIMER)、[`CONFIG_UART_136_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_136_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE136)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE136`。

<a id="CONFIG_UART_136_NRF_PARITY_BIT"></a>

## 166.20 `CONFIG_UART_136_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE136 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE136)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE136`。

<a id="CONFIG_UART_136_NRF_TX_BUFFER_SIZE"></a>

## 166.21 `CONFIG_UART_136_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE136 && CONFIG_HAS_HW_NRF_UARTE136 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE136)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE136`。

<a id="CONFIG_UART_136_NRF_USE_TIMER"></a>

## 166.22 `CONFIG_UART_136_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_137_ASYNC"></a>

## 166.23 `CONFIG_UART_137_ASYNC`

**提示（Prompt）**：端口 137 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_137_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE137 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_137_INTERRUPT_DRIVEN`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_137_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE137`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE137)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE137`。

<a id="CONFIG_UART_137_COUNT_BYTES_WITH_TIMER"></a>

## 166.24 `CONFIG_UART_137_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_137_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 166.25 `CONFIG_UART_137_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_137_NRF_USE_TIMER || CONFIG_UART_137_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE137 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_137_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_137_NRF_USE_TIMER)、[`CONFIG_UART_137_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_137_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE137`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE137)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE137`。

<a id="CONFIG_UART_137_ENHANCED_POLL_OUT"></a>

## 166.26 `CONFIG_UART_137_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 137 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE137 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE137 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE137`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE137)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE137`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_137_INTERRUPT_DRIVEN"></a>

## 166.27 `CONFIG_UART_137_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 137 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE137 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE137`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE137)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE137`。

<a id="CONFIG_UART_137_NRF_ASYNC_LOW_POWER"></a>

## 166.28 `CONFIG_UART_137_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE137 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE137 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE137`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE137)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE137`。

<a id="CONFIG_UART_137_NRF_HW_ASYNC"></a>

## 166.29 `CONFIG_UART_137_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE137 && !n && CONFIG_HAS_HW_NRF_UARTE137 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE137`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE137)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE137`。

<a id="CONFIG_UART_137_NRF_HW_ASYNC_TIMER"></a>

## 166.30 `CONFIG_UART_137_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_137_NRF_USE_TIMER && CONFIG_UART_137_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE137 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_137_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_137_NRF_USE_TIMER)、[`CONFIG_UART_137_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_137_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE137`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE137)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE137`。

<a id="CONFIG_UART_137_NRF_PARITY_BIT"></a>

## 166.31 `CONFIG_UART_137_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE137 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE137`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE137)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE137`。

<a id="CONFIG_UART_137_NRF_TX_BUFFER_SIZE"></a>

## 166.32 `CONFIG_UART_137_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE137 && CONFIG_HAS_HW_NRF_UARTE137 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE137`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE137)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE137`。

<a id="CONFIG_UART_137_NRF_USE_TIMER"></a>

## 166.33 `CONFIG_UART_137_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_1_ASYNC"></a>

## 166.34 `CONFIG_UART_1_ASYNC`

**提示（Prompt）**：端口 1 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_1_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE1 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_1_INTERRUPT_DRIVEN`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_1_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE1)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE1`。

<a id="CONFIG_UART_1_COUNT_BYTES_WITH_TIMER"></a>

## 166.35 `CONFIG_UART_1_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_1_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 166.36 `CONFIG_UART_1_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_1_NRF_USE_TIMER || CONFIG_UART_1_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE1 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_1_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_1_NRF_USE_TIMER)、[`CONFIG_UART_1_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_1_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE1)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE1`。

<a id="CONFIG_UART_1_ENHANCED_POLL_OUT"></a>

## 166.37 `CONFIG_UART_1_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 1 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE1 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE1 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE1)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE1`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_1_INTERRUPT_DRIVEN"></a>

## 166.38 `CONFIG_UART_1_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 1 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE1 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE1)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE1`。

<a id="CONFIG_UART_1_NRF_ASYNC_LOW_POWER"></a>

## 166.39 `CONFIG_UART_1_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE1 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE1 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE1)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE1`。

<a id="CONFIG_UART_1_NRF_HW_ASYNC"></a>

## 166.40 `CONFIG_UART_1_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE1 && !n && CONFIG_HAS_HW_NRF_UARTE1 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE1)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE1`。

<a id="CONFIG_UART_1_NRF_HW_ASYNC_TIMER"></a>

## 166.41 `CONFIG_UART_1_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_1_NRF_USE_TIMER && CONFIG_UART_1_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE1 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_1_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_1_NRF_USE_TIMER)、[`CONFIG_UART_1_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_1_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE1)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE1`。

<a id="CONFIG_UART_1_NRF_PARITY_BIT"></a>

## 166.42 `CONFIG_UART_1_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE1 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE1)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE1`。

<a id="CONFIG_UART_1_NRF_TX_BUFFER_SIZE"></a>

## 166.43 `CONFIG_UART_1_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE1 && CONFIG_HAS_HW_NRF_UARTE1 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE1)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE1`。

<a id="CONFIG_UART_1_NRF_USE_TIMER"></a>

## 166.44 `CONFIG_UART_1_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_20_ASYNC"></a>

## 166.45 `CONFIG_UART_20_ASYNC`

**提示（Prompt）**：端口 20 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_20_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE20 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_20_INTERRUPT_DRIVEN`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_20_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE20)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE20`。

<a id="CONFIG_UART_20_COUNT_BYTES_WITH_TIMER"></a>

## 166.46 `CONFIG_UART_20_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_20_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 166.47 `CONFIG_UART_20_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_20_NRF_USE_TIMER || CONFIG_UART_20_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE20 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_20_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_20_NRF_USE_TIMER)、[`CONFIG_UART_20_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_20_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE20)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE20`。

<a id="CONFIG_UART_20_ENHANCED_POLL_OUT"></a>

## 166.48 `CONFIG_UART_20_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 20 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE20 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE20 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE20)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE20`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_20_INTERRUPT_DRIVEN"></a>

## 166.49 `CONFIG_UART_20_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 20 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE20 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE20)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE20`。

<a id="CONFIG_UART_20_NRF_ASYNC_LOW_POWER"></a>

## 166.50 `CONFIG_UART_20_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE20 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE20 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE20)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE20`。

<a id="CONFIG_UART_20_NRF_HW_ASYNC"></a>

## 166.51 `CONFIG_UART_20_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE20 && !n && CONFIG_HAS_HW_NRF_UARTE20 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE20)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE20`。

<a id="CONFIG_UART_20_NRF_HW_ASYNC_TIMER"></a>

## 166.52 `CONFIG_UART_20_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_20_NRF_USE_TIMER && CONFIG_UART_20_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE20 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_20_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_20_NRF_USE_TIMER)、[`CONFIG_UART_20_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_20_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE20)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE20`。

<a id="CONFIG_UART_20_NRF_PARITY_BIT"></a>

## 166.53 `CONFIG_UART_20_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE20 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE20)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE20`。

<a id="CONFIG_UART_20_NRF_TX_BUFFER_SIZE"></a>

## 166.54 `CONFIG_UART_20_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE20 && CONFIG_HAS_HW_NRF_UARTE20 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE20)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE20`。

<a id="CONFIG_UART_20_NRF_USE_TIMER"></a>

## 166.55 `CONFIG_UART_20_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_21_ASYNC"></a>

## 166.56 `CONFIG_UART_21_ASYNC`

**提示（Prompt）**：端口 21 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_21_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE21 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_21_INTERRUPT_DRIVEN`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_21_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE21)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE21`。

<a id="CONFIG_UART_21_COUNT_BYTES_WITH_TIMER"></a>

## 166.57 `CONFIG_UART_21_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_21_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 166.58 `CONFIG_UART_21_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_21_NRF_USE_TIMER || CONFIG_UART_21_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE21 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_21_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_21_NRF_USE_TIMER)、[`CONFIG_UART_21_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_21_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE21)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE21`。

<a id="CONFIG_UART_21_ENHANCED_POLL_OUT"></a>

## 166.59 `CONFIG_UART_21_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 21 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE21 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE21 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE21)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE21`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_21_INTERRUPT_DRIVEN"></a>

## 166.60 `CONFIG_UART_21_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 21 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE21 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE21)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE21`。

<a id="CONFIG_UART_21_NRF_ASYNC_LOW_POWER"></a>

## 166.61 `CONFIG_UART_21_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE21 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE21 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE21)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE21`。

<a id="CONFIG_UART_21_NRF_HW_ASYNC"></a>

## 166.62 `CONFIG_UART_21_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE21 && !n && CONFIG_HAS_HW_NRF_UARTE21 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE21)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE21`。

<a id="CONFIG_UART_21_NRF_HW_ASYNC_TIMER"></a>

## 166.63 `CONFIG_UART_21_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_21_NRF_USE_TIMER && CONFIG_UART_21_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE21 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_21_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_21_NRF_USE_TIMER)、[`CONFIG_UART_21_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_21_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE21)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE21`。

<a id="CONFIG_UART_21_NRF_PARITY_BIT"></a>

## 166.64 `CONFIG_UART_21_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE21 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE21)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE21`。

<a id="CONFIG_UART_21_NRF_TX_BUFFER_SIZE"></a>

## 166.65 `CONFIG_UART_21_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE21 && CONFIG_HAS_HW_NRF_UARTE21 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE21)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE21`。

<a id="CONFIG_UART_21_NRF_USE_TIMER"></a>

## 166.66 `CONFIG_UART_21_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_22_ASYNC"></a>

## 166.67 `CONFIG_UART_22_ASYNC`

**提示（Prompt）**：端口 22 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_22_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE22 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_22_INTERRUPT_DRIVEN`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_22_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE22)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE22`。

<a id="CONFIG_UART_22_COUNT_BYTES_WITH_TIMER"></a>

## 166.68 `CONFIG_UART_22_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_22_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 166.69 `CONFIG_UART_22_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_22_NRF_USE_TIMER || CONFIG_UART_22_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE22 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_22_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_22_NRF_USE_TIMER)、[`CONFIG_UART_22_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_22_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE22)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE22`。

<a id="CONFIG_UART_22_ENHANCED_POLL_OUT"></a>

## 166.70 `CONFIG_UART_22_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 22 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE22 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE22 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE22)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE22`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_22_INTERRUPT_DRIVEN"></a>

## 166.71 `CONFIG_UART_22_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 22 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE22 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE22)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE22`。

<a id="CONFIG_UART_22_NRF_ASYNC_LOW_POWER"></a>

## 166.72 `CONFIG_UART_22_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE22 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE22 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE22)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE22`。

<a id="CONFIG_UART_22_NRF_HW_ASYNC"></a>

## 166.73 `CONFIG_UART_22_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE22 && !n && CONFIG_HAS_HW_NRF_UARTE22 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE22)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE22`。

<a id="CONFIG_UART_22_NRF_HW_ASYNC_TIMER"></a>

## 166.74 `CONFIG_UART_22_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_22_NRF_USE_TIMER && CONFIG_UART_22_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE22 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_22_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_22_NRF_USE_TIMER)、[`CONFIG_UART_22_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_22_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE22)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE22`。

<a id="CONFIG_UART_22_NRF_PARITY_BIT"></a>

## 166.75 `CONFIG_UART_22_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE22 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE22)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE22`。

<a id="CONFIG_UART_22_NRF_TX_BUFFER_SIZE"></a>

## 166.76 `CONFIG_UART_22_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE22 && CONFIG_HAS_HW_NRF_UARTE22 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE22)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE22`。

<a id="CONFIG_UART_22_NRF_USE_TIMER"></a>

## 166.77 `CONFIG_UART_22_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_23_ASYNC"></a>

## 166.78 `CONFIG_UART_23_ASYNC`

**提示（Prompt）**：端口 23 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_23_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE23 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_23_INTERRUPT_DRIVEN`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_23_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE23)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE23`。

<a id="CONFIG_UART_23_COUNT_BYTES_WITH_TIMER"></a>

## 166.79 `CONFIG_UART_23_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_23_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 166.80 `CONFIG_UART_23_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_23_NRF_USE_TIMER || CONFIG_UART_23_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE23 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_23_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_23_NRF_USE_TIMER)、[`CONFIG_UART_23_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_23_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE23)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE23`。

<a id="CONFIG_UART_23_ENHANCED_POLL_OUT"></a>

## 166.81 `CONFIG_UART_23_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 23 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE23 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE23 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE23)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE23`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_23_INTERRUPT_DRIVEN"></a>

## 166.82 `CONFIG_UART_23_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 23 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE23 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE23)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE23`。

<a id="CONFIG_UART_23_NRF_ASYNC_LOW_POWER"></a>

## 166.83 `CONFIG_UART_23_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE23 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE23 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE23)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE23`。

<a id="CONFIG_UART_23_NRF_HW_ASYNC"></a>

## 166.84 `CONFIG_UART_23_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE23 && !n && CONFIG_HAS_HW_NRF_UARTE23 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE23)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE23`。

<a id="CONFIG_UART_23_NRF_HW_ASYNC_TIMER"></a>

## 166.85 `CONFIG_UART_23_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_23_NRF_USE_TIMER && CONFIG_UART_23_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE23 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_23_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_23_NRF_USE_TIMER)、[`CONFIG_UART_23_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_23_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE23)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE23`。

<a id="CONFIG_UART_23_NRF_PARITY_BIT"></a>

## 166.86 `CONFIG_UART_23_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE23 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE23)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE23`。

<a id="CONFIG_UART_23_NRF_TX_BUFFER_SIZE"></a>

## 166.87 `CONFIG_UART_23_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE23 && CONFIG_HAS_HW_NRF_UARTE23 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE23)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE23`。

<a id="CONFIG_UART_23_NRF_USE_TIMER"></a>

## 166.88 `CONFIG_UART_23_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_24_ASYNC"></a>

## 166.89 `CONFIG_UART_24_ASYNC`

**提示（Prompt）**：端口 24 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_24_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE24 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_24_INTERRUPT_DRIVEN`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_24_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE24)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE24`。

<a id="CONFIG_UART_24_COUNT_BYTES_WITH_TIMER"></a>

## 166.90 `CONFIG_UART_24_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_24_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 166.91 `CONFIG_UART_24_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_24_NRF_USE_TIMER || CONFIG_UART_24_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE24 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_24_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_24_NRF_USE_TIMER)、[`CONFIG_UART_24_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_24_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE24)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE24`。

<a id="CONFIG_UART_24_ENHANCED_POLL_OUT"></a>

## 166.92 `CONFIG_UART_24_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 24 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE24 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE24 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE24)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE24`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_24_INTERRUPT_DRIVEN"></a>

## 166.93 `CONFIG_UART_24_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 24 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE24 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE24)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE24`。

<a id="CONFIG_UART_24_NRF_ASYNC_LOW_POWER"></a>

## 166.94 `CONFIG_UART_24_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE24 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE24 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE24)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE24`。

<a id="CONFIG_UART_24_NRF_HW_ASYNC"></a>

## 166.95 `CONFIG_UART_24_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE24 && !n && CONFIG_HAS_HW_NRF_UARTE24 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE24)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE24`。

<a id="CONFIG_UART_24_NRF_HW_ASYNC_TIMER"></a>

## 166.96 `CONFIG_UART_24_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_24_NRF_USE_TIMER && CONFIG_UART_24_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE24 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_24_NRF_USE_TIMER`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_24_NRF_USE_TIMER)、[`CONFIG_UART_24_NRF_HW_ASYNC`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_24_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE24)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE24`。

<a id="CONFIG_UART_24_NRF_PARITY_BIT"></a>

## 166.97 `CONFIG_UART_24_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE24 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE24)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE24`。

<a id="CONFIG_UART_24_NRF_TX_BUFFER_SIZE"></a>

## 166.98 `CONFIG_UART_24_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE24 && CONFIG_HAS_HW_NRF_UARTE24 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE24)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE24`。

<a id="CONFIG_UART_24_NRF_USE_TIMER"></a>

## 166.99 `CONFIG_UART_24_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_2_ASYNC"></a>

## 166.100 `CONFIG_UART_2_ASYNC`

**提示（Prompt）**：端口 2 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_2_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE2 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_2_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_2_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE2)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE2`。

<!-- kconfig-navigation -->

[上一章](P165_drivers_serial_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P167_drivers_serial_配置项参考_3.md)
