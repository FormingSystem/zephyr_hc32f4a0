---
id: learning.zephyr-docs.kconfig-reference.page-167
title: "`drivers/serial`配置项参考（3/5）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第167章\_`drivers/serial`配置项参考（3/5）

本章翻译官方 Kconfig 数据库中 `drivers/serial` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_UART_2_COUNT_BYTES_WITH_TIMER"></a>

## 167.1 `CONFIG_UART_2_COUNT_BYTES_WITH_TIMER`

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

<a id="CONFIG_UART_2_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 167.2 `CONFIG_UART_2_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_2_NRF_USE_TIMER || CONFIG_UART_2_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE2 && CONFIG_UART_NRFX && CONFIG_SERIAL
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

**配置项引用（Symbol References）**：[`CONFIG_UART_2_NRF_USE_TIMER`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_2_NRF_USE_TIMER)、[`CONFIG_UART_2_NRF_HW_ASYNC`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_2_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE2)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE2`。

<a id="CONFIG_UART_2_ENHANCED_POLL_OUT"></a>

## 167.3 `CONFIG_UART_2_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 2 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE2 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE2 && CONFIG_UART_NRFX && CONFIG_SERIAL
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

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE2)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE2`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_2_INTERRUPT_DRIVEN"></a>

## 167.4 `CONFIG_UART_2_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 2 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE2 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE2)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE2`。

<a id="CONFIG_UART_2_NRF_ASYNC_LOW_POWER"></a>

## 167.5 `CONFIG_UART_2_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE2 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE2 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE2)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE2`。

<a id="CONFIG_UART_2_NRF_HW_ASYNC"></a>

## 167.6 `CONFIG_UART_2_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE2 && !n && CONFIG_HAS_HW_NRF_UARTE2 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE2)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE2`。

<a id="CONFIG_UART_2_NRF_HW_ASYNC_TIMER"></a>

## 167.7 `CONFIG_UART_2_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_2_NRF_USE_TIMER && CONFIG_UART_2_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE2 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_2_NRF_USE_TIMER`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_2_NRF_USE_TIMER)、[`CONFIG_UART_2_NRF_HW_ASYNC`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_2_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE2)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE2`。

<a id="CONFIG_UART_2_NRF_PARITY_BIT"></a>

## 167.8 `CONFIG_UART_2_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE2 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE2)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE2`。

<a id="CONFIG_UART_2_NRF_TX_BUFFER_SIZE"></a>

## 167.9 `CONFIG_UART_2_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE2 && CONFIG_HAS_HW_NRF_UARTE2 && CONFIG_UART_NRFX && CONFIG_SERIAL
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

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE2)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE2`。

<a id="CONFIG_UART_2_NRF_USE_TIMER"></a>

## 167.10 `CONFIG_UART_2_NRF_USE_TIMER`

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

<a id="CONFIG_UART_30_ASYNC"></a>

## 167.11 `CONFIG_UART_30_ASYNC`

**提示（Prompt）**：端口 30 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_30_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE30 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_30_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_30_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE30`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE30)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE30`。

<a id="CONFIG_UART_30_COUNT_BYTES_WITH_TIMER"></a>

## 167.12 `CONFIG_UART_30_COUNT_BYTES_WITH_TIMER`

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

<a id="CONFIG_UART_30_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 167.13 `CONFIG_UART_30_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_30_NRF_USE_TIMER || CONFIG_UART_30_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE30 && CONFIG_UART_NRFX && CONFIG_SERIAL
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

**配置项引用（Symbol References）**：[`CONFIG_UART_30_NRF_USE_TIMER`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_30_NRF_USE_TIMER)、[`CONFIG_UART_30_NRF_HW_ASYNC`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_30_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE30`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE30)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE30`。

<a id="CONFIG_UART_30_ENHANCED_POLL_OUT"></a>

## 167.14 `CONFIG_UART_30_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 30 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE30 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE30 && CONFIG_UART_NRFX && CONFIG_SERIAL
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

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE30`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE30)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE30`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_30_INTERRUPT_DRIVEN"></a>

## 167.15 `CONFIG_UART_30_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 30 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE30 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE30`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE30)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE30`。

<a id="CONFIG_UART_30_NRF_ASYNC_LOW_POWER"></a>

## 167.16 `CONFIG_UART_30_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE30 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE30 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE30`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE30)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE30`。

<a id="CONFIG_UART_30_NRF_HW_ASYNC"></a>

## 167.17 `CONFIG_UART_30_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE30 && !n && CONFIG_HAS_HW_NRF_UARTE30 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE30`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE30)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE30`。

<a id="CONFIG_UART_30_NRF_HW_ASYNC_TIMER"></a>

## 167.18 `CONFIG_UART_30_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_30_NRF_USE_TIMER && CONFIG_UART_30_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE30 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_30_NRF_USE_TIMER`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_30_NRF_USE_TIMER)、[`CONFIG_UART_30_NRF_HW_ASYNC`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_30_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE30`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE30)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE30`。

<a id="CONFIG_UART_30_NRF_PARITY_BIT"></a>

## 167.19 `CONFIG_UART_30_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE30 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE30`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE30)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE30`。

<a id="CONFIG_UART_30_NRF_TX_BUFFER_SIZE"></a>

## 167.20 `CONFIG_UART_30_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE30 && CONFIG_HAS_HW_NRF_UARTE30 && CONFIG_UART_NRFX && CONFIG_SERIAL
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

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE30`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE30)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE30`。

<a id="CONFIG_UART_30_NRF_USE_TIMER"></a>

## 167.21 `CONFIG_UART_30_NRF_USE_TIMER`

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

<a id="CONFIG_UART_3_ASYNC"></a>

## 167.22 `CONFIG_UART_3_ASYNC`

**提示（Prompt）**：端口 3 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_3_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE3 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_3_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_3_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE3)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE3`。

<a id="CONFIG_UART_3_COUNT_BYTES_WITH_TIMER"></a>

## 167.23 `CONFIG_UART_3_COUNT_BYTES_WITH_TIMER`

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

<a id="CONFIG_UART_3_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 167.24 `CONFIG_UART_3_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_3_NRF_USE_TIMER || CONFIG_UART_3_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE3 && CONFIG_UART_NRFX && CONFIG_SERIAL
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

**配置项引用（Symbol References）**：[`CONFIG_UART_3_NRF_USE_TIMER`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_3_NRF_USE_TIMER)、[`CONFIG_UART_3_NRF_HW_ASYNC`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_3_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE3)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE3`。

<a id="CONFIG_UART_3_ENHANCED_POLL_OUT"></a>

## 167.25 `CONFIG_UART_3_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 3 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE3 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE3 && CONFIG_UART_NRFX && CONFIG_SERIAL
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

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE3)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE3`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_3_INTERRUPT_DRIVEN"></a>

## 167.26 `CONFIG_UART_3_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 3 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE3 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE3)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE3`。

<a id="CONFIG_UART_3_NRF_ASYNC_LOW_POWER"></a>

## 167.27 `CONFIG_UART_3_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE3 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE3 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE3)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE3`。

<a id="CONFIG_UART_3_NRF_HW_ASYNC"></a>

## 167.28 `CONFIG_UART_3_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE3 && !n && CONFIG_HAS_HW_NRF_UARTE3 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE3)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE3`。

<a id="CONFIG_UART_3_NRF_HW_ASYNC_TIMER"></a>

## 167.29 `CONFIG_UART_3_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_3_NRF_USE_TIMER && CONFIG_UART_3_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE3 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_3_NRF_USE_TIMER`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_3_NRF_USE_TIMER)、[`CONFIG_UART_3_NRF_HW_ASYNC`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_3_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE3)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE3`。

<a id="CONFIG_UART_3_NRF_PARITY_BIT"></a>

## 167.30 `CONFIG_UART_3_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE3 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE3)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE3`。

<a id="CONFIG_UART_3_NRF_TX_BUFFER_SIZE"></a>

## 167.31 `CONFIG_UART_3_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE3 && CONFIG_HAS_HW_NRF_UARTE3 && CONFIG_UART_NRFX && CONFIG_SERIAL
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

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE3)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE3`。

<a id="CONFIG_UART_3_NRF_USE_TIMER"></a>

## 167.32 `CONFIG_UART_3_NRF_USE_TIMER`

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

<a id="CONFIG_UART_AESC"></a>

## 167.33 `CONFIG_UART_AESC`

**提示（Prompt）**：Aesc Silicon UART 驱动

**说明（Help）**

启用 Aesc Silicon UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AESC_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.aesc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.aesc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_ALTERA"></a>

## 167.34 `CONFIG_UART_ALTERA`

**提示（Prompt）**：ALTERA UART 驱动

**说明（Help）**

启用 Altera UART 驱动，该 UART 可集成到 Intel NiosV CPU 设计中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ALTR_UART_ENABLED && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.altera:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.altera#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_ALTERA_EOP"></a>

## 167.35 `CONFIG_UART_ALTERA_EOP`

**提示（Prompt）**：ALTERA UART 包结束（End of Packet）功能

**说明（Help）**

使用驱动命令 `CMD_ENABLE_EOP` 和 `CMD_DISABLE_EOP` 控制此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ALTERA && CONFIG_UART_DRV_CMD && CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.altera:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.altera#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → ALTERA UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ALTERA`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ALTERA)、[`CONFIG_UART_DRV_CMD`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_DRV_CMD)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_ALTERA_JTAG"></a>

## 167.36 `CONFIG_UART_ALTERA_JTAG`

**提示（Prompt）**：NiosV JTAG UART 驱动

**说明（Help）**

启用 Altera JTAG UART 驱动，此 UART 内置于许多 NiosV CPU 设计中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ALTR_JTAG_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.altera_jtag:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.altera_jtag#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)。

<a id="CONFIG_UART_ALTERA_JTAG_SUPPORT_INTERRUPT"></a>

## 167.37 `CONFIG_UART_ALTERA_JTAG_SUPPORT_INTERRUPT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

这是辅助配置项（Helper Config）。禁用 `UART_ALTERA_JTAG_HAL` 时，Altera JTAG UART 驱动将支持中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ALTERA_JTAG && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_SUPPORT_INTERRUPT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.altera_jtag:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.altera_jtag#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → NiosV JTAG UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ALTERA_JTAG`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ALTERA_JTAG)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_ALTERA_LINE_CTRL_WORKAROUND"></a>

## 167.38 `CONFIG_UART_ALTERA_LINE_CTRL_WORKAROUND`

**提示（Prompt）**：ALTERA UART 流控制变通方案（Flow Control Workaround）

**说明（Help）**

启用前，请先尝试优化中断服务程序（ISR），使其更快取走接收数据。启用后，发送器会等待允许发送（CTS）信号的上升沿再发送。接收器在收到一个字节后立即撤销请求发送（RTS）信号，待该字节被取走后重新置为有效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ALTERA && CONFIG_UART_LINE_CTRL && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.altera:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.altera#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → ALTERA UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ALTERA`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ALTERA)、[`CONFIG_UART_LINE_CTRL`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_LINE_CTRL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_AMBIQ"></a>

## 167.39 `CONFIG_UART_AMBIQ`

**提示（Prompt）**：AMBIQ UART 驱动

**说明（Help）**

启用 AMBIQ UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_UART_ENABLED && (CONFIG_SOC_SERIES_APOLLO5X || CONFIG_SOC_SERIES_APOLLO4X) && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_SUPPORT_ASYNC if CONFIG_SOC_SERIES_APOLLO5X
CONFIG_PINCTRL
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_UART
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ambiq:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ambiq#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_SERIES_APOLLO4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_UART)。

<a id="CONFIG_UART_AMBIQ_HANDLE_CACHE"></a>

## 167.40 `CONFIG_UART_AMBIQ_HANDLE_CACHE`

**提示（Prompt）**：在 UART 驱动中启用缓存处理（Cache Handling）

**说明（Help）**

如果上层已处理缓存（Cache），则禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE && CONFIG_UART_AMBIQ && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ambiq:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ambiq#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → AMBIQ UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_UART_AMBIQ`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_AMBIQ)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_AMEBA_LOGUART"></a>

## 167.41 `CONFIG_UART_AMEBA_LOGUART`

**提示（Prompt）**：Ameba LOGUART 驱动

**说明（Help）**

此选项为 Realtek Ameba 片上系统（SoC）启用 LOGUART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_LOGUART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.ameba_loguart:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ameba_loguart#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)。

<a id="CONFIG_UART_APBUART"></a>

## 167.42 `CONFIG_UART_APBUART`

**提示（Prompt）**：ABPUART 串行驱动（Serial Driver）

**说明（Help）**

此选项为 LEON 处理器启用 APBUART 驱动。

译注：标题原文拼作 ABPUART，帮助原文拼作 APBUART；此处保留差异。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GAISLER_APBUART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.apbuart:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.apbuart#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_ASCLIN"></a>

## 167.43 `CONFIG_UART_ASCLIN`

**提示（Prompt）**：ASCLIN 串行驱动（Serial Driver）

**说明（Help）**

此选项为 AURIX 处理器启用 ASCLIN 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_ASCLIN_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.infineon_aurix:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.infineon_aurix#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)。

<a id="CONFIG_UART_ASYNC_API"></a>

## 167.44 `CONFIG_UART_ASYNC_API`

**提示（Prompt）**：异步 UART API（Asynchronous UART API）

**说明（Help）**

此选项启用异步 UART API（Asynchronous UART API）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL_SUPPORT_ASYNC && CONFIG_SERIAL
```

**被选择（Selected by）**

```text
CONFIG_DEBUG_NRF_ETR_SHELL
CONFIG_WS2812_STRIP_UART
CONFIG_MODEM_IFACE_UART_ASYNC
```

**定义位置（Location）**：[`drivers/serial/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEBUG_NRF_ETR_SHELL`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_SHELL)、[`CONFIG_WS2812_STRIP_UART`](P115_drivers_led_strip_配置项参考.md#CONFIG_WS2812_STRIP_UART)、[`CONFIG_MODEM_IFACE_UART_ASYNC`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART_ASYNC)。

<a id="CONFIG_UART_ASYNC_RX_HELPER"></a>

## 167.45 `CONFIG_UART_ASYNC_RX_HELPER`

**提示（Prompt）**：UART 异步接收辅助模块（Asynchronous Reception Helper）

**说明（Help）**

此模块通过异步 UART API（Asynchronous UART API）处理变长数据接收，适用于接收数据延迟处理的场景。模块采用多个接收缓冲区实现零拷贝（Zero-copy）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**被选择（Selected by）**

```text
CONFIG_DEBUG_NRF_ETR_SHELL
CONFIG_UART_ASYNC_TO_INT_DRIVEN_API
CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC
```

**定义位置（Location）**：[`drivers/serial/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEBUG_NRF_ETR_SHELL`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_SHELL)、[`CONFIG_UART_ASYNC_TO_INT_DRIVEN_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_TO_INT_DRIVEN_API)、[`CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC)。

<a id="CONFIG_UART_ASYNC_TO_INT_DRIVEN_API"></a>

## 167.46 `CONFIG_UART_ASYNC_TO_INT_DRIVEN_API`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

异步到中断驱动适配层（Asynchronous to Interrupt-driven Adaptation Layer）。启用后，仅实现异步 API 的设备，也可通过通用适配层提供的中断驱动 API 使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_UART_ASYNC_RX_HELPER
```

**定义位置（Location）**：[`drivers/serial/Kconfig:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_ASYNC_RX_HELPER`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_RX_HELPER)。

<a id="CONFIG_UART_ASYNC_TO_INT_DRIVEN_RX_TIMEOUT"></a>

## 167.47 `CONFIG_UART_ASYNC_TO_INT_DRIVEN_RX_TIMEOUT`

**提示（Prompt）**：接收器超时（原文单位：bauds）

**说明（Help）**

接收器不活动超时时间（Receiver Inactivity Timeout），用于计算以微秒为单位的超时时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_TO_INT_DRIVEN_API && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/serial/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_TO_INT_DRIVEN_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_TO_INT_DRIVEN_API)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_ASYNC_TX_CACHE_SIZE"></a>

## 167.48 `CONFIG_UART_ASYNC_TX_CACHE_SIZE`

**提示（Prompt）**：发送（TX）缓存缓冲区大小

**说明（Help）**

对于 UARTE，当提供的发送缓冲区不位于 RAM 中时，使用发送（TX）缓存缓冲区；因为 UARTE 外设中的 EasyDMA 只能从 RAM 传输数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_BEE"></a>

## 167.49 `CONFIG_UART_BEE`

**提示（Prompt）**：Realtek Bee 系列 UART 驱动

**说明（Help）**

此选项为 Realtek Bee 片上系统（SoC）启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_UART
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_PINCTRL
CONFIG_SERIAL_SUPPORT_ASYNC if DT_HAS_REALTEK_BEE_DMA_ENABLED
CONFIG_DMA if CONFIG_UART_ASYNC_API
```

**定义位置（Location）**：[`drivers/serial/Kconfig.bee:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.bee#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_HAL_REALTEK_BEE_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_UART)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_UART`。

<a id="CONFIG_UART_BFLB"></a>

## 167.50 `CONFIG_UART_BFLB`

**提示（Prompt）**：Bouffalo Lab 串行驱动（Serial Driver）

**说明（Help）**

此选项为 Bouffalo Lab 片上系统（SoC）系列启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.bflb:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.bflb#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_BITBANG"></a>

## 167.51 `CONFIG_UART_BITBANG`

**提示（Prompt）**：软件模拟 UART 控制器（Bitbang UART Controller）驱动

**说明（Help）**

启用软件模拟 UART 控制器（Bitbang UART Controller）。驱动依靠计数器中断生成／采样 UART 帧。中断周期的准确性本身无法得到保证，并会受到应用程序其他活动的影响。波特率较低时，可观察到的相对偏差通常较小。还建议使用奇偶校验（Parity）和／或其他错误检测机制，以检测传输错误。此驱动旨在提供额外的 UART 接口，以及／或者支持部分平台硬件 UART 外设未支持的模式。集成此驱动的应用应了解上述限制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_UART_BITBANG_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_COUNTER
CONFIG_SERIAL_HAS_POST_KERNEL_INIT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.bitbang:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.bitbang#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_SERIAL_HAS_POST_KERNEL_INIT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_POST_KERNEL_INIT)。

<a id="CONFIG_UART_BRIDGE"></a>

## 167.52 `CONFIG_UART_BRIDGE`

**提示（Prompt）**：UART 桥接（UART Bridge）

**说明（Help）**

启用 UART 桥接（UART Bridge）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_UART_BRIDGE_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`drivers/serial/Kconfig.bridge:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.bridge#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_UART_BRIDGE_BUF_SIZE"></a>

## 167.53 `CONFIG_UART_BRIDGE_BUF_SIZE`

**提示（Prompt）**：UART 桥接缓冲区大小

**说明（Help）**

桥接环形缓冲区（Ring Buffer）的大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_BRIDGE && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/serial/Kconfig.bridge:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.bridge#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → UART 桥接（UART Bridge）

**配置项引用（Symbol References）**：[`CONFIG_UART_BRIDGE`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_BRIDGE)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_BT"></a>

## 167.54 `CONFIG_UART_BT`

**提示（Prompt）**：基于 NUS 低功耗蓝牙的 UART［实验性，EXPERIMENTAL］

**说明（Help）**

启用基于 NUS 的蓝牙 UART 驱动，通过 Nordic UART 服务（Nordic UART Service，NUS），在低功耗蓝牙（Bluetooth LE）GATT 上传送串行数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ZEPHYR_NUS && DT_HAS_ZEPHYR_NUS_UART_ENABLED && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_UART_INTERRUPT_DRIVEN
CONFIG_EXPERIMENTAL
CONFIG_SERIAL_SUPPORT_INTERRUPT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.bt:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.bt#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_ZEPHYR_NUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ZEPHYR_NUS)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_BT_WORKQUEUE_PRIORITY"></a>

## 167.55 `CONFIG_UART_BT_WORKQUEUE_PRIORITY`

**提示（Prompt）**：UART NUS 工作队列优先级（Work-queue Priority）

**说明（Help）**

根据应用场景选择 UART NUS 工作队列（Work-queue）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_BT && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
CONFIG_MAIN_THREAD_PRIORITY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.bt:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.bt#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 基于 NUS 低功耗蓝牙的 UART［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UART_BT`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_BT)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_MAIN_THREAD_PRIORITY`](P001_kernel_配置项参考_1.md#CONFIG_MAIN_THREAD_PRIORITY)。

<a id="CONFIG_UART_BT_WORKQUEUE_STACK_SIZE"></a>

## 167.56 `CONFIG_UART_BT_WORKQUEUE_STACK_SIZE`

**提示（Prompt）**：UART NUS 工作队列栈大小（Work-queue Stack Size）

**说明（Help）**

根据应用场景设置 UART NUS 工作队列（Work-queue）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_BT && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/serial/Kconfig.bt:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.bt#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 基于 NUS 低功耗蓝牙的 UART［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UART_BT`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_BT)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_CC13XX_CC26XX"></a>

## 167.57 `CONFIG_UART_CC13XX_CC26XX`

**提示（Prompt）**：TI SimpleLink CC13xx / CC26xx UART 驱动

**说明（Help）**

启用 TI SimpleLink CC13xx / CC26xx UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC13XX_CC26XX_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.cc13xx_cc26xx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.cc13xx_cc26xx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_CC23X0"></a>

## 167.58 `CONFIG_UART_CC23X0`

**提示（Prompt）**：TI SimpleLink CC23x0 UART 驱动

**说明（Help）**

启用 TI SimpleLink CC23x0 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC23X0_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.cc23x0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.cc23x0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_CC23X0_DMA_DRIVEN"></a>

## 167.59 `CONFIG_UART_CC23X0_DMA_DRIVEN`

**提示（Prompt）**：TI CC23X0 UART 设备的直接内存访问（DMA）支持

**说明（Help）**

直接内存访问（DMA）驱动模式将数据传输任务从 CPU 卸载到 DMA。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_CC23X0 && CONFIG_UART_ASYNC_API && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/serial/Kconfig.cc23x0:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.cc23x0#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → TI SimpleLink CC23x0 UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_CC23X0`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_CC23X0)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_UART_CC32XX"></a>

## 167.60 `CONFIG_UART_CC32XX`

**提示（Prompt）**：CC32XX UART 驱动

**说明（Help）**

此选项为 `UART_0` 启用 CC32XX UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC32XX_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.cc32xx:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.cc32xx#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_CDNS"></a>

## 167.61 `CONFIG_UART_CDNS`

**提示（Prompt）**：Cadence UART IP6528 串行驱动

**说明（Help）**

此选项启用 Cadence UART IP6528 串行驱动（Serial Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CDNS_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.cdns:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.cdns#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_CMSDK_APB"></a>

## 167.62 `CONFIG_UART_CMSDK_APB`

**提示（Prompt）**：ARM CMSDK APB UART 驱动

**说明（Help）**

此选项启用 ARM CMSDK APB UART 的 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_CMSDK_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.cmsdk_apb:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.cmsdk_apb#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_DRV_CMD"></a>

## 167.63 `CONFIG_UART_DRV_CMD`

**提示（Prompt）**：驱动命令 API（Driver Commands API）

**说明（Help）**

启用向驱动发送额外命令的 API，使驱动能够提供硬件特定功能（Hardware-specific Functions）。如果不确定，请选择 N。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_EFINIX_SAPPIHIRE"></a>

## 167.64 `CONFIG_UART_EFINIX_SAPPIHIRE`

**提示（Prompt）**：EFINIX_SAPPIHIRE 串行驱动（Serial Driver）

**说明（Help）**

此选项启用 Efinix Sapphire 串行驱动（Serial Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_EFINIX_SAPPHIRE_UART0_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.efinix_sapphire:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.efinix_sapphire#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)。

<a id="CONFIG_UART_EM32"></a>

## 167.65 `CONFIG_UART_EM32`

**提示（Prompt）**：ELAN EM32 串行驱动（Serial Driver）

**说明（Help）**

此选项启用 ELAN EM32 串行驱动（Serial Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_EM32F967 && DT_HAS_ELAN_EM32_UART_ENABLED && CONFIG_CLOCK_CONTROL_EM32_APB && CONFIG_GPIO_EM32 && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.em32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.em32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_EM32F967`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EM32F967)、[`CONFIG_CLOCK_CONTROL_EM32_APB`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_EM32_APB)、[`CONFIG_GPIO_EM32`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_EM32)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_EM32_INIT_PRIORITY"></a>

## 167.66 `CONFIG_UART_EM32_INIT_PRIORITY`

**提示（Prompt）**：EM32 UART 初始化优先级（Initialization Priority）

**说明（Help）**

EM32 UART 驱动的初始化优先级。由于 UART 依赖 GPIO、时钟和引脚控制（Pinctrl）驱动，此值必须大于 `GPIO_EM32_INIT_PRIORITY` 和 `CLOCK_CONTROL_EM32_APB_INIT_PRIORITY`。UART 用作控制台（Console）时，该值还必须小于 `CONSOLE_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_EM32 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
56
```

**定义位置（Location）**：[`drivers/serial/Kconfig.em32:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.em32#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → ELAN EM32 串行驱动（Serial Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_EM32`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_EM32)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_EMUL"></a>

## 167.67 `CONFIG_UART_EMUL`

**提示（Prompt）**：仿真 UART 驱动（Emulated UART Driver）［实验性，EXPERIMENTAL］

**说明（Help）**

启用仿真 UART 驱动（Emulated UART Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_UART_EMUL_ENABLED && CONFIG_EMUL && CONFIG_SERIAL
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
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.emul:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.emul#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_UART_EMUL_DEVICE_INIT_PRIORITY"></a>

## 167.68 `CONFIG_UART_EMUL_DEVICE_INIT_PRIORITY`

**提示（Prompt）**：UART 仿真设备初始化优先级

**说明（Help）**

UART 总线上仿真驱动的初始化优先级（Init Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_EMUL && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/serial/Kconfig.emul:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.emul#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 仿真 UART 驱动（Emulated UART Driver）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UART_EMUL`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_EMUL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_EMUL_WORK_Q_PRIORITY"></a>

## 167.69 `CONFIG_UART_EMUL_WORK_Q_PRIORITY`

**提示（Prompt）**：UART 仿真器工作队列线程优先级

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_EMUL && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/serial/Kconfig.emul:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.emul#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 仿真 UART 驱动（Emulated UART Driver）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UART_EMUL`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_EMUL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_EMUL_WORK_Q_STACK_SIZE"></a>

## 167.70 `CONFIG_UART_EMUL_WORK_Q_STACK_SIZE`

**提示（Prompt）**：UART 仿真器工作队列栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_EMUL && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/serial/Kconfig.emul:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.emul#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 仿真 UART 驱动（Emulated UART Driver）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UART_EMUL`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_EMUL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_ENE_KB106X"></a>

## 167.71 `CONFIG_UART_ENE_KB106X`

**提示（Prompt）**：ENE KB106X 串行驱动（Serial Driver）

**说明（Help）**

此选项启用 KB106X 串行驱动（Serial Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB106X_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.ene:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ene#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_ENE_KB1200"></a>

## 167.72 `CONFIG_UART_ENE_KB1200`

**提示（Prompt）**：ENE KB1200 串行驱动（Serial Driver）

**说明（Help）**

此选项启用 KB1200 串行驱动（Serial Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB1200_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.ene:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.ene#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_ESP32"></a>

## 167.73 `CONFIG_UART_ESP32`

**提示（Prompt）**：ESP32 UART 驱动

**说明（Help）**

启用 ESP32 UART。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_SUPPORT_ASYNC if CONFIG_SOC_SERIES_ESP32C3 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2 || CONFIG_SOC_SERIES_ESP32S3
CONFIG_GPIO_ESP32
```

**定义位置（Location）**：[`drivers/serial/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_SOC_SERIES_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_GPIO_ESP32`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_UART_ESP32_RX_FIFO_THRESH"></a>

## 167.74 `CONFIG_UART_ESP32_RX_FIFO_THRESH`

**提示（Prompt）**：ESP32 UART 接收 FIFO 阈值（RX FIFO Threshold）

**说明（Help）**

配置 ESP32 UART 驱动的接收 FIFO 阈值（RX FIFO Threshold）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ESP32 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
0x16
```

**取值范围（Ranges）**

```text
[1, 127]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.esp32:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.esp32#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_ESP32`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ESP32)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_ESP32_TX_FIFO_THRESH"></a>

## 167.75 `CONFIG_UART_ESP32_TX_FIFO_THRESH`

**提示（Prompt）**：ESP32 UART 发送 FIFO 阈值（TX FIFO Threshold）

**说明（Help）**

配置 ESP32 UART 驱动的发送 FIFO 阈值（TX FIFO Threshold）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ESP32 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
0x1
```

**取值范围（Ranges）**

```text
[1, 127]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.esp32:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.esp32#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_ESP32`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ESP32)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_EXCLUSIVE_API_CALLBACKS"></a>

## 167.76 `CONFIG_UART_EXCLUSIVE_API_CALLBACKS`

**提示（Prompt）**：多个 API 使用互斥回调（Exclusive Callbacks）

**说明（Help）**

当多组 API 均支持回调时，启用此选项会使同一时间只有一组 API 的回调处于有效状态。为某组 API 设置新回调，将移除其他 API 组的回调。例如，调用 `uart_callback_set()` 会禁用先前通过 `uart_irq_callback_set()` 设置的回调。除非完全理解其影响，并承诺出现问题时不因此提交缺陷报告，否则请选择 Y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → UART 中断支持（Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_FOCALTECH"></a>

## 167.77 `CONFIG_UART_FOCALTECH`

**提示（Prompt）**：FocalTech FT9001 MCU 串行驱动

**说明（Help）**

为 FocalTech FT9001 片上系统（SoC）启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FOCALTECH_FT9001_USART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_RESET
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.focaltech:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.focaltech#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_UART_GECKO"></a>

## 167.78 `CONFIG_UART_GECKO`

**提示（Prompt）**：Gecko UART/USART 驱动

**说明（Help）**

启用 Gecko UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_SILABS_GECKO_UART_ENABLED || DT_HAS_SILABS_GECKO_USART_ENABLED) && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SILABS_GECKO_USART
CONFIG_PINCTRL if CONFIG_SOC_FAMILY_SILABS_S1
```

**定义位置（Location）**：[`drivers/serial/Kconfig.gecko:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.gecko#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SILABS_GECKO_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_USART)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`。

<a id="CONFIG_UART_HOSTLINK"></a>

## 167.79 `CONFIG_UART_HOSTLINK`

**提示（Prompt）**：ARC HOSTLINK UART 驱动

**说明（Help）**

此选项允许将 HOSTLINK 通道作为 UART 设备访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC && DT_HAS_SNPS_HOSTLINK_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.hostlink:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.hostlink#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)。

<a id="CONFIG_UART_IMX"></a>

## 167.80 `CONFIG_UART_IMX`

**提示（Prompt）**：NXP i.MX7 系列处理器 UART 驱动

**说明（Help）**

此选项为 NXP i.MX7 系列处理器启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.imx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.imx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_INFINEON_CAT1_HAL"></a>

## 167.81 `CONFIG_UART_INFINEON_CAT1_HAL`

**提示（Prompt）**：Infineon CAT1 UART 驱动

**说明（Help）**

此选项为 Infineon CAT1 系列启用基于旧版硬件抽象层（Legacy HAL）的 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_UART_ENABLED && CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_SUPPORT_ASYNC if !(CONFIG_SOC_FAMILY_INFINEON_CAT1C || CONFIG_SOC_CY8C6244LQI_S4D92)
CONFIG_USE_INFINEON_UART
CONFIG_PINCTRL
CONFIG_DMA if CONFIG_UART_ASYNC_API
```

**定义位置（Location）**：[`drivers/serial/Kconfig.infineon:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.infineon#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_SOC_FAMILY_INFINEON_CAT1C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1C)、[`CONFIG_SOC_CY8C6244LQI_S4D92`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CY8C6244LQI_S4D92)、[`CONFIG_USE_INFINEON_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_UART)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1C`、`CONFIG_SOC_CY8C6244LQI_S4D92`。

<a id="CONFIG_UART_INFINEON_CAT1_PDL"></a>

## 167.82 `CONFIG_UART_INFINEON_CAT1_PDL`

**提示（Prompt）**：Infineon CAT1 UART 驱动（PDL）

**说明（Help）**

此选项为 Infineon CAT1 系列启用基于外设驱动库（PDL）的 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_UART_ENABLED && !CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SERIAL_SUPPORT_ASYNC if !CONFIG_SOC_FAMILY_INFINEON_CAT1C
CONFIG_USE_INFINEON_UART
CONFIG_PINCTRL
CONFIG_DMA if CONFIG_UART_ASYNC_API
CONFIG_USE_INFINEON_DMA if CONFIG_UART_ASYNC_API
```

**定义位置（Location）**：[`drivers/serial/Kconfig.infineon:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.infineon#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_SOC_FAMILY_INFINEON_CAT1C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1C)、[`CONFIG_USE_INFINEON_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_UART)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_USE_INFINEON_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_DMA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1C`。

<a id="CONFIG_UART_INFINEON_PDL_MP_FIELD_QUIRK"></a>

## 167.83 `CONFIG_UART_INFINEON_PDL_MP_FIELD_QUIRK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

对于 PDL 已修正 SCB UART 配置字段名称 `enableMultiProcessorMode` 的片上系统（SoC），启用此选项。旧版 PDL 将其误拼为 `enableMutliProcessorMode`；驱动根据此符号选择字段名。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_DIE_PSC3M6 || CONFIG_SOC_SERIES_PSE84
```

**定义位置（Location）**：[`drivers/serial/Kconfig.infineon:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.infineon#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SOC_DIE_PSC3M6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_DIE_PSC3M6)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_DIE_PSC3M6`、`CONFIG_SOC_SERIES_PSE84`。

<a id="CONFIG_UART_INTEL_LW"></a>

## 167.84 `CONFIG_UART_INTEL_LW`

**提示（Prompt）**：Intel 轻量级 UART（Lightweight UART）驱动

**说明（Help）**

启用 Intel 轻量级 UART（Lightweight UART）驱动，该 UART 可集成到 Intel NiosV CPU 设计中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_LW_UART_ENABLED && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.intel_lw:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.intel_lw#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_INTEL_LW_AUTO_LINE_CTRL_POLL"></a>

## 167.85 `CONFIG_UART_INTEL_LW_AUTO_LINE_CTRL_POLL`

**提示（Prompt）**：轮询输出时自动设置请求发送（RTS）信号

**说明（Help）**

轮询输出一个字符前将请求发送（RTS）信号置为有效，字符输出完成后撤销 RTS。注意，此方式不适合轮询输出多个字符。请在轮询输出前，使用 `uart_drv_cmd` 和 `CMD_POLL_ASSERT_RTS` 命令；轮询结束后，使用 `CMD_POLL_DEASSERT_RTS` 恢复正常操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_LINE_CTRL && CONFIG_UART_INTEL_LW && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.intel_lw:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.intel_lw#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Intel 轻量级 UART（Lightweight UART）驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_LINE_CTRL`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_LINE_CTRL)、[`CONFIG_UART_INTEL_LW`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTEL_LW)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_INTEL_LW_EOP"></a>

## 167.86 `CONFIG_UART_INTEL_LW_EOP`

**提示（Prompt）**：包含包结束寄存器（End of Packet Register）

**说明（Help）**

使用驱动命令 `CMD_ENABLE_EOP` 和 `CMD_DISABLE_EOP` 控制此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_DRV_CMD && CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_UART_INTEL_LW && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.intel_lw:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.intel_lw#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → Intel 轻量级 UART（Lightweight UART）驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_DRV_CMD`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_DRV_CMD)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_UART_INTEL_LW`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTEL_LW)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_INTERRUPT_DRIVEN"></a>

## 167.87 `CONFIG_UART_INTERRUPT_DRIVEN`

**提示（Prompt）**：UART 中断支持（Interrupt Support）

**说明（Help）**

此选项启用 UART 中断支持，以允许控制台输入和其他基于 UART 的驱动工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL_SUPPORT_INTERRUPT && CONFIG_SERIAL
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_COPROCESSOR
CONFIG_OPENTHREAD_COPROCESSOR
CONFIG_BIOMETRICS_GT5X
CONFIG_BIOMETRICS_ZFM_X0
CONFIG_BT_UART
CONFIG_CONSOLE_HANDLER
CONFIG_UART_MCUMGR
CONFIG_ETH_CH9120
CONFIG_INPUT_CH9350L
CONFIG_MODEM_RECEIVER
CONFIG_MODEM_IFACE_UART_INTERRUPT
CONFIG_SLIP
CONFIG_UART_BRIDGE
CONFIG_UART_BT
CONFIG_UART_SMARTBOND
CONFIG_BT_DEBUG_MONITOR_UART_INTERRUPT_DRIVEN
CONFIG_CONSOLE_GETCHAR
CONFIG_GNSS_RTK_SERIAL
CONFIG_INSTRUMENTATION
CONFIG_NET_SLIP_TAP
CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN
CONFIG_TRACING_HANDLE_HOST_CMD
CONFIG_USB_CDC_ACM
CONFIG_USBD_CDC_ACM_CLASS
```

**被弱选择（Implied by）**

```text
CONFIG_OSDP
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/sparkfun_sara_r4/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/sparkfun_sara_r4/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/st87mxx/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st87mxx/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/wnc_m14a2a/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/wnc_m14a2a/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/x_nucleo_gnss1a1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_gnss1a1/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_OPENTHREAD_COPROCESSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_COPROCESSOR)、[`CONFIG_BIOMETRICS_GT5X`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS_GT5X)、[`CONFIG_BIOMETRICS_ZFM_X0`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS_ZFM_X0)、[`CONFIG_BT_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_UART)、[`CONFIG_CONSOLE_HANDLER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HANDLER)、[`CONFIG_UART_MCUMGR`](P066_drivers_console_配置项参考.md#CONFIG_UART_MCUMGR)、[`CONFIG_ETH_CH9120`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_CH9120)、[`CONFIG_INPUT_CH9350L`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CH9350L)、[`CONFIG_MODEM_RECEIVER`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_RECEIVER)、[`CONFIG_MODEM_IFACE_UART_INTERRUPT`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART_INTERRUPT)、[`CONFIG_SLIP`](P131_drivers_net_配置项参考.md#CONFIG_SLIP)、[`CONFIG_UART_BRIDGE`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_BRIDGE)、[`CONFIG_UART_BT`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_BT)、[`CONFIG_UART_SMARTBOND`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_SMARTBOND)、[`CONFIG_BT_DEBUG_MONITOR_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEBUG_MONITOR_UART_INTERRUPT_DRIVEN)、[`CONFIG_CONSOLE_GETCHAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CONSOLE_GETCHAR)、[`CONFIG_GNSS_RTK_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GNSS_RTK_SERIAL)、[`CONFIG_INSTRUMENTATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION)、[`CONFIG_NET_SLIP_TAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SLIP_TAP)、[`CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN)、[`CONFIG_TRACING_HANDLE_HOST_CMD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING_HANDLE_HOST_CMD)、[`CONFIG_USB_CDC_ACM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_CDC_ACM)、[`CONFIG_USBD_CDC_ACM_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_CDC_ACM_CLASS)、[`CONFIG_OSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_UART`。

<a id="CONFIG_UART_ITE_IT51XXX"></a>

## 167.88 `CONFIG_UART_ITE_IT51XXX`

**提示（Prompt）**：ITE IT51XXX UART 驱动

**说明（Help）**

IT51XXX 使用共享的 `ns16550.c` 驱动。此封装主要注册一个中断，使嵌入式控制器（EC）从休眠（Doze）或深度休眠（Deep Doze）模式唤醒，恢复活动状态（Active State）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UART_NS16550_ITE_HIGH_SPEED_BAUDRATE
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_NS16550_ITE_HIGH_SPEED_BAUDRATE`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550_ITE_HIGH_SPEED_BAUDRATE)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_ITE_IT8XXX2"></a>

## 167.89 `CONFIG_UART_ITE_IT8XXX2`

**提示（Prompt）**：ITE IT8XXX2 UART 驱动

**说明（Help）**

IT8XXX2 使用共享的 `ns16550.c` 驱动，该驱动不提供电源管理回调，因此另行创建驱动以处理 IT8XXX2 特定的 UART 功能。除了使用 `pm_action_cb`，还需在 `uart_it8xxx2_init` 中进行一些设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UART_NS16550_ITE_HIGH_SPEED_BAUDRATE
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.it8xxx2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.it8xxx2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_NS16550_ITE_HIGH_SPEED_BAUDRATE`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NS16550_ITE_HIGH_SPEED_BAUDRATE)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_ITE_IT8XXX2_INIT_PRIORITY"></a>

## 167.90 `CONFIG_UART_ITE_IT8XXX2_INIT_PRIORITY`

**提示（Prompt）**：ITE IT8XXX2 UART 封装初始化优先级（Wrapper Init Priority）

**说明（Help）**

ITE IT8XXX2 上 UART 封装驱动的初始化优先级。必须安排在对应的 ns16550 设备（`CONFIG_SERIAL_INIT_PRIORITY`）之后初始化；原文称其优先级应更低。

译注：此处“更低”指初始化次序更靠后，不应理解为优先级数值更小；本项默认数值为 51。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ITE_IT8XXX2 && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
51
```

**定义位置（Location）**：[`drivers/serial/Kconfig.it8xxx2:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.it8xxx2#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → ITE IT8XXX2 UART 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ITE_IT8XXX2`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ITE_IT8XXX2)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_LINE_CTRL"></a>

## 167.91 `CONFIG_UART_LINE_CTRL`

**提示（Prompt）**：串行线路控制 API（Serial Line Control API）

**说明（Help）**

启用应用控制串行线路的 API，例如控制波特率（Baud Rate）、允许发送（CTS）和请求发送（RTS）。具体实现由各个驱动决定。如果不确定，请选择 N。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**被选择（Selected by）**

```text
CONFIG_BT_NXP_CTRL_BSP_TRIGGER
```

**定义位置（Location）**：[`drivers/serial/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_BT_NXP_CTRL_BSP_TRIGGER`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_CTRL_BSP_TRIGGER)。

<a id="CONFIG_UART_LITEX"></a>

## 167.92 `CONFIG_UART_LITEX`

**提示（Prompt）**：LiteX 串行驱动（Serial Driver）

**说明（Help）**

此选项启用 LiteX UART 串行驱动（Serial Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.litex:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.litex#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_UART_LPC11U6X"></a>

## 167.93 `CONFIG_UART_LPC11U6X`

**提示（Prompt）**：LPC11U6X 串行驱动（Serial Driver）

**说明（Help）**

为 LPC11U6X 系列启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC11U6X_UART_ENABLED && CONFIG_SERIAL
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

**定义位置（Location）**：[`drivers/serial/Kconfig.lpc11u6x:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.lpc11u6x#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_LPC84X"></a>

## 167.94 `CONFIG_UART_LPC84X`

**提示（Prompt）**：LPC84x UART 驱动

**说明（Help）**

启用 LPC84x UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC84X_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_UART_USE_RUNTIME_CONFIGURE
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.lpc84x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.lpc84x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_USE_RUNTIME_CONFIGURE)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UART_MAX32"></a>

## 167.95 `CONFIG_UART_MAX32`

**提示（Prompt）**：MAX32 MCU 串行驱动

**说明（Help）**

此选项为 MAX32 系列处理器启用 UART 驱动。如果需要在 MAX32 微控制器（MCU）上使用串口，请选择 Y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_UART_ENABLED && CONFIG_SERIAL
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
CONFIG_SERIAL_SUPPORT_ASYNC if DT_HAS_ADI_MAX32_DMA_ENABLED && !CONFIG_SOC_FAMILY_MAX32_RV32
CONFIG_DMA if CONFIG_UART_ASYNC_API
```

**定义位置（Location）**：[`drivers/serial/Kconfig.max32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.max32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_SOC_FAMILY_MAX32_RV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_RV32)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32_RV32`。

<a id="CONFIG_UART_MAX32_TX_AE_WORKAROUND"></a>

## 167.96 `CONFIG_UART_MAX32_TX_AE_WORKAROUND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项启用一个小型变通方案（Workaround），处理少量数据发送时几乎为空中断（Almost-empty Interrupt）不触发的问题。此选项已弃用，相关平台应改用更完整的中断变通方案。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_MAX32 && CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.max32:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.max32#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → MAX32 MCU 串行驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_MAX32`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_MAX32)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_UART_MAX32_TX_IRQ_WORKAROUND"></a>

## 167.97 `CONFIG_UART_MAX32_TX_IRQ_WORKAROUND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

针对部分 MAX32 微控制器（MCU）的变通方案（Workaround）；这些器件存在勘误，发送 FIFO 半空／几乎为空（TX Half/Almost Empty）标志无法稳定地触发中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_MAX32 && CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_MAX32690 || CONFIG_SOC_MAX32655 || CONFIG_SOC_MAX32657 || CONFIG_SOC_MAX32666 || CONFIG_SOC_MAX32670 || CONFIG_SOC_MAX32672 || CONFIG_SOC_MAX32675
```

**定义位置（Location）**：[`drivers/serial/Kconfig.max32:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.max32#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → MAX32 MCU 串行驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_MAX32`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_MAX32)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SOC_MAX32690`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MAX32690)、[`CONFIG_SOC_MAX32655`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MAX32655)、[`CONFIG_SOC_MAX32657`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MAX32657)、[`CONFIG_SOC_MAX32666`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MAX32666)、[`CONFIG_SOC_MAX32670`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MAX32670)、[`CONFIG_SOC_MAX32672`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MAX32672)、[`CONFIG_SOC_MAX32675`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MAX32675)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MAX32690`、`CONFIG_SOC_MAX32655`、`CONFIG_SOC_MAX32657`、`CONFIG_SOC_MAX32666`、`CONFIG_SOC_MAX32670`、`CONFIG_SOC_MAX32672`、`CONFIG_SOC_MAX32675`。

<a id="CONFIG_UART_MAX32_TX_IRQ_WORKAROUND_POLL_US"></a>

## 167.98 `CONFIG_UART_MAX32_TX_IRQ_WORKAROUND_POLL_US`

**提示（Prompt）**：检查发送（TX）完成的间隔

**说明（Help）**

检查发送 FIFO（TX FIFO）状态的定时器间隔，适用于发送半空／几乎为空中断有时无法触发的平台。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_MAX32_TX_IRQ_WORKAROUND && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/serial/Kconfig.max32:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.max32#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → MAX32 MCU 串行驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_MAX32_TX_IRQ_WORKAROUND`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_MAX32_TX_IRQ_WORKAROUND)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UART_MCHP_ASYNC"></a>

## 167.99 `CONFIG_UART_MCHP_ASYNC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为具有 `dmas` 属性的 UART 实例启用异步／直接内存访问（Async/DMA）支持。没有 `dmas` 属性的实例在执行异步操作时将返回 `-ENOTSUP`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.mchp:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mchp#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

<a id="CONFIG_UART_MCHP_DBGU_G1"></a>

## 167.100 `CONFIG_UART_MCHP_DBGU_G1`

**提示（Prompt）**：Microchip SAM 调试单元（Debug Unit，DBGU）驱动

**说明（Help）**

此选项为 DBGU 外设的 g1 组启用 UART 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_DBGU_G1_UART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.mchp:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.mchp#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)。

<!-- kconfig-navigation -->

[上一章](P166_drivers_serial_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P168_drivers_serial_配置项参考_4.md)
