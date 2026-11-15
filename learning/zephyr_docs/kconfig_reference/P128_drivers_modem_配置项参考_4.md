---
id: learning.zephyr-docs.kconfig-reference.page-128
title: "`drivers/modem`配置项参考（4/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第128章\_`drivers/modem`配置项参考（4/4）

本章翻译官方 Kconfig 数据库中 `drivers/modem` 的 99 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600"></a>

## 128.1 `CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600`

**提示（Prompt）**：921600

**说明（Help）**

将调制解调器波特率设为 921600 bps。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_TARGET_BAUDRATE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching） → 目标 UART 波特率（Target Baud Rate）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE)。

<a id="CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_9600"></a>

## 128.2 `CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_9600`

**提示（Prompt）**：9600

**说明（Help）**

将调制解调器波特率设为 9600 bps。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_TARGET_BAUDRATE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching） → 目标 UART 波特率（Target Baud Rate）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE)。

<a id="CONFIG_MODEM_HL78XX_UART_BUFFER_SIZES"></a>

## 128.3 `CONFIG_MODEM_HL78XX_UART_BUFFER_SIZES`

**提示（Prompt）**：UART 接收和发送缓冲区大小，单位为字节。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1568`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1568)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_USER_PIPE_BUFFER_SIZES"></a>

## 128.4 `CONFIG_MODEM_HL78XX_USER_PIPE_BUFFER_SIZES`

**提示（Prompt）**：每个用户管道（User Pipe）使用的缓冲区大小，单位为字节。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1576`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1576)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_USE_ACTIVE_TIME_BASED_POWER_DOWN"></a>

## 128.5 `CONFIG_MODEM_HL78XX_USE_ACTIVE_TIME_BASED_POWER_DOWN`

**提示（Prompt）**：使用 RRC 连接之后的活动时间（Active Time）

**说明（Help）**

建立无线资源控制（RRC）连接后，按类似 PSM 的活动时间 `MODEM_HL78XX_POWER_DOWN_ACTIVE_TIME` 计时，并据此关闭调制解调器电源。只有建立新的 RRC 连接时，才重置此定时器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_POWER_DOWN_MODE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1242`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1242)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes） → 断电模式（Power Down Mode）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_POWER_DOWN_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_POWER_DOWN_MODE)。

<a id="CONFIG_MODEM_HL78XX_USE_DELAY_BASED_POWER_DOWN"></a>

## 128.6 `CONFIG_MODEM_HL78XX_USE_DELAY_BASED_POWER_DOWN`

**提示（Prompt）**：使用最后一次数据活动之后的延迟（Delay after Last Data Activity）

**说明（Help）**

最后一次套接字关闭或数据传输之后，等待 `MODEM_HL78XX_POWER_DOWN_DELAY` 指定的延迟，再关闭调制解调器电源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_POWER_DOWN_MODE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1236`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1236)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes） → 断电模式（Power Down Mode）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_POWER_DOWN_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_POWER_DOWN_MODE)。

<a id="CONFIG_MODEM_HL78XX_WDSI_PROFILE_VALUE"></a>

## 128.7 `CONFIG_MODEM_HL78XX_WDSI_PROFILE_VALUE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏能力值（Hidden Capability Value）：各变体特定的默认 `AT+WDSI` 配置。值 0 表示在运行时通过 `AT+WDSI=?` 查询配置支持情况。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
8191 if CONFIG_MODEM_HL78XX_12
4479 if CONFIG_MODEM_HL78XX_00
0
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_12`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_12)、[`CONFIG_MODEM_HL78XX_00`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_00)。

<a id="CONFIG_MODEM_IFACE_UART"></a>

## 128.8 `CONFIG_MODEM_IFACE_UART`

**提示（Prompt）**：基于 UART 的调制解调器接口（Modem Interface）

**说明（Help）**

要配置并使用此层，应创建 `modem_iface_uart_data` 对象，将其引用与 `modem_context` 对象中的 `modem_iface` 引用、UART 设备名一起传给 `modem_iface_uart_init()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CONTEXT && CONFIG_MODEM
```

**被选择（Selected by）**

```text
CONFIG_MODEM_QUECTEL_BG9X
CONFIG_MODEM_SIM7080
CONFIG_MODEM_ST87MXX
CONFIG_MODEM_UBLOX_SARA
CONFIG_WIFI_ESP_AT
```

**定义位置（Location）**：[`drivers/modem/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器上下文辅助驱动（Modem Context Helper）【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_QUECTEL_BG9X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BG9X)、[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM_ST87MXX`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_ST87MXX)、[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_WIFI_ESP_AT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP_AT)。

<a id="CONFIG_MODEM_IFACE_UART_ASYNC"></a>

## 128.9 `CONFIG_MODEM_IFACE_UART_ASYNC`

**提示（Prompt）**：使用异步 API（Async API）的 UART 调制解调器接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL_SUPPORT_ASYNC && <choice CONFIG_MODEM_IFACE_UART_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_UART_ASYNC_API
```

**定义位置（Location）**：[`drivers/modem/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器上下文辅助驱动（Modem Context Helper）【实验性】 → 基于 UART 的调制解调器接口（Modem Interface） → 调制解调器接口要使用的 UART 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL_SUPPORT_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_MODEM_IFACE_UART_BACKEND`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART_BACKEND)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)。

<a id="CONFIG_MODEM_IFACE_UART_ASYNC_RX_BUFFER_SIZE"></a>

## 128.10 `CONFIG_MODEM_IFACE_UART_ASYNC_RX_BUFFER_SIZE`

**提示（Prompt）**：提供给 UART 驱动的接收缓冲区大小，单位为字节

**说明（Help）**

增大此值，可减少接收大数据包所需的 UART 中断次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_IFACE_UART_ASYNC && CONFIG_MODEM_IFACE_UART && CONFIG_MODEM_CONTEXT && CONFIG_MODEM
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/modem/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器上下文辅助驱动（Modem Context Helper）【实验性】 → 基于 UART 的调制解调器接口（Modem Interface）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_IFACE_UART_ASYNC`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART_ASYNC)、[`CONFIG_MODEM_IFACE_UART`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART)、[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_IFACE_UART_ASYNC_RX_NUM_BUFFERS"></a>

## 128.11 `CONFIG_MODEM_IFACE_UART_ASYNC_RX_NUM_BUFFERS`

**提示（Prompt）**：UART 驱动可用的接收缓冲区数量

**说明（Help）**

为避免缓冲区耗尽（Buffer Starvation），此值需要是使用该驱动的 UART 调制解调器数量的两倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_IFACE_UART_ASYNC && CONFIG_MODEM_IFACE_UART && CONFIG_MODEM_CONTEXT && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/modem/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器上下文辅助驱动（Modem Context Helper）【实验性】 → 基于 UART 的调制解调器接口（Modem Interface）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_IFACE_UART_ASYNC`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART_ASYNC)、[`CONFIG_MODEM_IFACE_UART`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART)、[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_IFACE_UART_ASYNC_RX_TIMEOUT_US"></a>

## 128.12 `CONFIG_MODEM_IFACE_UART_ASYNC_RX_TIMEOUT_US`

**提示（Prompt）**：未收到更多数据后刷新接收缓冲区的超时（RX Buffer Flush Timeout）

**说明（Help）**

使用较高波特率时，减小此值有助于提高数据吞吐量。原文说明，115200 波特下 4 字节对应 278 μs。减得过小可能产生杂散中断（Spurious Interrupt），保持过大则可能降低吞吐量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_IFACE_UART_ASYNC && CONFIG_MODEM_IFACE_UART && CONFIG_MODEM_CONTEXT && CONFIG_MODEM
```

**默认值（Defaults）**

```text
278
```

**定义位置（Location）**：[`drivers/modem/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器上下文辅助驱动（Modem Context Helper）【实验性】 → 基于 UART 的调制解调器接口（Modem Interface）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_IFACE_UART_ASYNC`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART_ASYNC)、[`CONFIG_MODEM_IFACE_UART`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART)、[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_IFACE_UART_BACKEND"></a>

## 128.13 `CONFIG_MODEM_IFACE_UART_BACKEND`

**提示（Prompt）**：调制解调器接口要使用的 UART 后端（Backend）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_IFACE_UART && CONFIG_MODEM_CONTEXT && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_IFACE_UART_INTERRUPT
```

**可选项（Choices）**

```text
CONFIG_MODEM_IFACE_UART_INTERRUPT
CONFIG_MODEM_IFACE_UART_ASYNC
```

**定义位置（Location）**：[`drivers/modem/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器上下文辅助驱动（Modem Context Helper）【实验性】 → 基于 UART 的调制解调器接口（Modem Interface）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_IFACE_UART`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART)、[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_IFACE_UART_INTERRUPT`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART_INTERRUPT)、[`CONFIG_MODEM_IFACE_UART_ASYNC`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART_ASYNC)。

<a id="CONFIG_MODEM_IFACE_UART_INTERRUPT"></a>

## 128.14 `CONFIG_MODEM_IFACE_UART_INTERRUPT`

**提示（Prompt）**：使用中断 API（Interrupt API）的 UART 调制解调器接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL_SUPPORT_INTERRUPT && <choice CONFIG_MODEM_IFACE_UART_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`drivers/modem/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器上下文辅助驱动（Modem Context Helper）【实验性】 → 基于 UART 的调制解调器接口（Modem Interface） → 调制解调器接口要使用的 UART 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_MODEM_IFACE_UART_BACKEND`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART_BACKEND)、[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_MODEM_MIN_ALLOWED_SIGNAL_QUALITY"></a>

## 128.15 `CONFIG_MODEM_MIN_ALLOWED_SIGNAL_QUALITY`

**提示（Prompt）**：允许的最低参考信号接收质量（RSRQ），单位为 dB

**说明（Help）**

HL78xx 辅助 API 接受的最低参考信号接收质量（Reference Signal Received Quality，RSRQ）阈值，值越低越差。较宽松的默认值 −20 dB 保持现有行为，除非应用选择更严格的门限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
-20
```

**取值范围（Ranges）**

```text
[-20, 0]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1433`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1433)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_MIN_ALLOWED_SIGNAL_STRENGTH"></a>

## 128.16 `CONFIG_MODEM_MIN_ALLOWED_SIGNAL_STRENGTH`

**提示（Prompt）**：允许的最低参考信号接收功率（RSRP），单位为 dBm

**说明（Help）**

从单个参考信号接收到的平均功率，典型范围约为 −44 dBm（好）至 −140 dBm（差）。原文注明，低于 −115 dBm 的信号不可用／不可靠。以下为原文所附的强度级别片段，依次表示优秀、良好、中等小区信号、小区边缘信号和较差信号；标识、类型、比较方向及范围中的空格均按原文保留：

```text
EXCELLENT_SIGNAL_STRENGTH
bool ">= -80(dBm)"
  default -80
  range - 80 0
GOOD_SIGNAL_STRENGTH
bool ">= -90(dBm)"
  default -90
  range - 90 0
MID_CELL_SIGNAL_STRENGTH
bool ">= -100(dBm)"
  default -100
  range - 100 0
CELL_EDGE_SIGNAL_STRENGTH
bool "<= -100(dBm)"
  default -110
  range - 110 0
POOR_SIGNAL_STRENGTH
bool ">= -140(dBm)"
  default -140
  range - 140 0
```

译注：这是官方帮助中附带的原始片段，不把其中 `bool` 与数值范围的组合当作经过语法校正的可用 Kconfig。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
-140
```

**取值范围（Ranges）**

```text
[-140, 0]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1404`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1404)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_MIN_ALLOWED_SINR"></a>

## 128.17 `CONFIG_MODEM_MIN_ALLOWED_SINR`

**提示（Prompt）**：允许的最低信干噪比（SINR），单位为 dB

**说明（Help）**

HL78xx 辅助 API 接受的最低信号与干扰加噪声比（Signal-to-Interference-plus-Noise Ratio，SINR）阈值，值越高越好。较宽松的默认值 −20 dB 保持现有行为，除非应用选择更严格的门限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
-20
```

**取值范围（Ranges）**

```text
[-20, 40]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1443`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1443)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BC66"></a>

## 128.18 `CONFIG_MODEM_QUECTEL_BC66`

**提示（Prompt）**：Quectel BC66

**说明（Help）**

启用 Quectel BC66 调制解调器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if DT_HAS_QUECTEL_BC66_ENABLED
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BC660K"></a>

## 128.19 `CONFIG_MODEM_QUECTEL_BC660K`

**提示（Prompt）**：Quectel BC660K-GL

**说明（Help）**

启用 Quectel BC660K-GL 调制解调器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if DT_HAS_QUECTEL_BC660K_ENABLED
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BC66X"></a>

## 128.20 `CONFIG_MODEM_QUECTEL_BC66X`

**提示（Prompt）**：Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**说明（Help）**

Quectel BC66 / BC660K-GL NB-IoT 调制解调器驱动。使用 Zephyr 调制解调器子系统的 `modem_chat` 与 `modem_backend_uart` 交换 AT 命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM && CONFIG_MODEM_CHAT && CONFIG_MODEM_BACKEND_UART && CONFIG_MODEM_PIPE && CONFIG_NETWORKING && CONFIG_NET_OFFLOAD && CONFIG_NET_SOCKETS_OFFLOAD && CONFIG_GPIO && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_CHAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CHAT)、[`CONFIG_MODEM_BACKEND_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_PIPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_PIPE)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_OFFLOAD)、[`CONFIG_NET_SOCKETS_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_APN_PROFILES"></a>

## 128.21 `CONFIG_MODEM_QUECTEL_BC66X_APN_PROFILES`

**提示（Prompt）**：自动检测 APN 时搜索的配置文件列表（Profiles）

**说明（Help）**

设置以逗号分隔的配置文件列表，每项包含以下内容：

```text
<apn>=<ICCID_1> ... <ICCID_n>
```

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"tim=893901, 1nce=8988228"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_CHAT_BUF_SIZE"></a>

## 128.22 `CONFIG_MODEM_QUECTEL_BC66X_CHAT_BUF_SIZE`

**提示（Prompt）**：AT 会话接收缓冲区大小（AT Chat RX Buffer Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_DNS_ADDRESS_1"></a>

## 128.23 `CONFIG_MODEM_QUECTEL_BC66X_DNS_ADDRESS_1`

**提示（Prompt）**：主 DNS 服务器地址（Primary DNS Server Address）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"8.8.8.8"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_DNS_ADDRESS_2"></a>

## 128.24 `CONFIG_MODEM_QUECTEL_BC66X_DNS_ADDRESS_2`

**提示（Prompt）**：备用 DNS 服务器地址（Secondary DNS Server Address）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"1.1.1.1"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_DNS_TIMEOUT"></a>

## 128.25 `CONFIG_MODEM_QUECTEL_BC66X_DNS_TIMEOUT`

**提示（Prompt）**：DNS 解析超时，单位为秒

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
15
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_INIT_PRIORITY"></a>

## 128.26 `CONFIG_MODEM_QUECTEL_BC66X_INIT_PRIORITY`

**提示（Prompt）**：Quectel BC66x 调制解调器驱动初始化优先级

**说明（Help）**

此优先级必须小于 `MODEM_QUECTEL_BC66X_NET_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
75
```

**取值范围（Ranges）**

```text
[0, 99]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_NET_INIT_PRIORITY"></a>

## 128.27 `CONFIG_MODEM_QUECTEL_BC66X_NET_INIT_PRIORITY`

**提示（Prompt）**：网络设备初始化优先级（Net Device Init Priority）

**说明（Help）**

此优先级必须大于 `MODEM_QUECTEL_BC66X_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
80
```

**取值范围（Ranges）**

```text
[0, 99]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_UART_RX_BUF_SIZE"></a>

## 128.28 `CONFIG_MODEM_QUECTEL_BC66X_UART_RX_BUF_SIZE`

**提示（Prompt）**：UART 接收环形缓冲区大小（RX Ring Buffer Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_UART_TX_BUF_SIZE"></a>

## 128.29 `CONFIG_MODEM_QUECTEL_BC66X_UART_TX_BUF_SIZE`

**提示（Prompt）**：UART 发送缓冲区大小（TX Buffer Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_WORKQ_PRIORITY"></a>

## 128.30 `CONFIG_MODEM_QUECTEL_BC66X_WORKQ_PRIORITY`

**提示（Prompt）**：工作队列（Workq）优先级；注意，初始化工作也在此队列调度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_WORKQ_STACK_SIZE"></a>

## 128.31 `CONFIG_MODEM_QUECTEL_BC66X_WORKQ_STACK_SIZE`

**提示（Prompt）**：延后工作线程（Deferred Work Thread）栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BG9X"></a>

## 128.32 `CONFIG_MODEM_QUECTEL_BG9X`

**提示（Prompt）**：Quectel 调制解调器驱动

**说明（Help）**

Quectel BG9x LTE-CatM1/NB-IoT 卸载式（Offload）调制解调器驱动。需要卸载驱动时应使用它。仅在用户需要 PSM/eDRX 节能模式时，此模式才是首选；其他情况下，原文推荐通用蜂窝调制解调器（Cellular Modem）方案。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_MODEM_CONTEXT
CONFIG_MODEM_CMD_HANDLER
CONFIG_MODEM_IFACE_UART
CONFIG_MODEM_SOCKET
CONFIG_NET_SOCKETS_OFFLOAD
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM_CMD_HANDLER`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CMD_HANDLER)、[`CONFIG_MODEM_IFACE_UART`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART)、[`CONFIG_MODEM_SOCKET`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SOCKET)、[`CONFIG_NET_SOCKETS_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD)。

<a id="CONFIG_MODEM_QUECTEL_BG9X_APN"></a>

## 128.33 `CONFIG_MODEM_QUECTEL_BG9X_APN`

**提示（Prompt）**：用于建立网络连接的接入点名称（APN）

**说明（Help）**

此设置用于为网络连接上下文设置接入点名称（APN）。它取决于网络提供商，可能需要更改。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BG9X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"internet"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BG9X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BG9X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BG9X_INIT_PRIORITY"></a>

## 128.34 `CONFIG_MODEM_QUECTEL_BG9X_INIT_PRIORITY`

**提示（Prompt）**：Quectel BG9X 驱动初始化优先级

**说明（Help）**

Quectel BG9X 设备驱动的初始化优先级。除非清楚其影响，否则不要随意更改。注意，数值需要低于网络协议栈的初始化优先级，使它能在网络子系统之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BG9X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BG9X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BG9X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BG9X_PASSWORD"></a>

## 128.35 `CONFIG_MODEM_QUECTEL_BG9X_PASSWORD`

**提示（Prompt）**：用于建立网络连接的密码（Password）

**说明（Help）**

此设置用于为网络连接上下文设置密码。它取决于网络提供商，可能需要更改。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BG9X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BG9X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BG9X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BG9X_RX_STACK_SIZE"></a>

## 128.36 `CONFIG_MODEM_QUECTEL_BG9X_RX_STACK_SIZE`

**提示（Prompt）**：Quectel BG9X 调制解调器驱动接收线程栈大小

**说明（Help）**

此栈由 Quectel BG9X 接收（RX）线程使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BG9X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1028
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BG9X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BG9X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BG9X_RX_WORKQ_STACK_SIZE"></a>

## 128.37 `CONFIG_MODEM_QUECTEL_BG9X_RX_WORKQ_STACK_SIZE`

**提示（Prompt）**：Quectel BG9X 调制解调器驱动工作队列栈大小

**说明（Help）**

工作队列（Work Queue）使用此栈，将 `net_pkt` 数据交给网络协议栈的其他部分，使接收线程能继续处理数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BG9X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BG9X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BG9X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BG9X_UNSOL_RDY"></a>

## 128.38 `CONFIG_MODEM_QUECTEL_BG9X_UNSOL_RDY`

**提示（Prompt）**：预期调制解调器发出的主动响应字符串（Unsolicited Response String）

**说明（Help）**

此字符串用于确定调制解调器已上电，并准备好接受 AT 命令。如果该值与调制解调器响应不匹配，初始化会因超时而失败。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BG9X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"RDY"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BG9X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BG9X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_QUECTEL_BG9X_USERNAME"></a>

## 128.39 `CONFIG_MODEM_QUECTEL_BG9X_USERNAME`

**提示（Prompt）**：用于建立网络连接的用户名（Username）

**说明（Help）**

此设置用于为网络连接上下文设置用户名。它取决于网络提供商，可能需要更改。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BG9X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bg9x/Kconfig.quectel-bg9x#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BG9X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BG9X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_RECEIVER"></a>

## 128.40 `CONFIG_MODEM_RECEIVER`

**提示（Prompt）**：调制解调器接收辅助驱动（Receiver Helper Driver）

**说明（Help）**

此驱动允许调制解调器驱动通过 UART 使用自定义协议通信。它不检查接收数据，收到的协议数据的所有处理都由应用通过提供的工作方法（Work Method）负责。与管道 UART 驱动不同，此驱动在另一工作队列中执行回调，并通过 `k_pipe` 结构传递数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL_SUPPORT_INTERRUPT && CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_UART_INTERRUPT_DRIVEN
```

**被选择（Selected by）**

```text
CONFIG_MODEM_HL7800
CONFIG_MODEM_ST87MXX
CONFIG_MODEM_WNCM14A2A
```

**定义位置（Location）**：[`drivers/modem/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM_ST87MXX`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_ST87MXX)、[`CONFIG_MODEM_WNCM14A2A`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_WNCM14A2A)。

<a id="CONFIG_MODEM_RECEIVER_MAX_CONTEXTS"></a>

## 128.41 `CONFIG_MODEM_RECEIVER_MAX_CONTEXTS`

**提示（Prompt）**：调制解调器接收上下文最大数量（Maximum Receiver Contexts）

**说明（Help）**

要处理的调制解调器接收上下文最大数量。多数情况下应保持为 1。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_RECEIVER && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`drivers/modem/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器接收辅助驱动（Receiver Helper Driver）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_RECEIVER`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_RECEIVER)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_SHELL"></a>

## 128.42 `CONFIG_MODEM_SHELL`

**提示（Prompt）**：调制解调器 Shell 实用工具（Utilities）

**说明（Help）**

激活提供调制解调器实用功能的 Shell 模块，例如向调制解调器 UART 发送命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_SHELL
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

**定义位置（Location）**：[`drivers/modem/Kconfig:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L170)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)。

<a id="CONFIG_MODEM_SIM7080"></a>

## 128.43 `CONFIG_MODEM_SIM7080`

**提示（Prompt）**：SIM7080 驱动

**说明（Help）**

启用 SIM7080 调制解调器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_MODEM_CONTEXT
CONFIG_MODEM_CMD_HANDLER
CONFIG_MODEM_IFACE_UART
CONFIG_MODEM_SOCKET
CONFIG_NET_OFFLOAD
CONFIG_NET_SOCKETS_OFFLOAD
```

**弱选择（Implies）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM_CMD_HANDLER`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CMD_HANDLER)、[`CONFIG_MODEM_IFACE_UART`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART)、[`CONFIG_MODEM_SOCKET`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SOCKET)、[`CONFIG_NET_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_OFFLOAD)、[`CONFIG_NET_SOCKETS_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_APN"></a>

## 128.44 `CONFIG_MODEM_SIMCOM_SIM7080_APN`

**提示（Prompt）**：用于建立网络连接的接入点名称（APN）

**说明（Help）**

此设置用于为网络连接上下文设置接入点名称（APN）。它取决于网络提供商，可能需要更改。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_SIM7080 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"internet"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_BAUDRATE"></a>

## 128.45 `CONFIG_MODEM_SIMCOM_SIM7080_BAUDRATE`

**提示（Prompt）**：调制解调器 UART 波特率（Baud Rate）

**说明（Help）**

将此值设置为 UART 使用的波特率。首次启动时，调制解调器配置为自动波特率（Autobaud）；之后驱动会将其配置为固定波特率，以加快启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_SIM7080 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
115200
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_BOOT_TYPE_CONSTRAINED"></a>

## 128.46 `CONFIG_MODEM_SIMCOM_SIM7080_BOOT_TYPE_CONSTRAINED`

**提示（Prompt）**：受限启动（Constrained Boot）

**说明（Help）**

检查调制解调器能否工作，然后关闭电源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动 → 调制解调器启动类型（Modem Boot Type）

<a id="CONFIG_MODEM_SIMCOM_SIM7080_BOOT_TYPE_NORMAL"></a>

## 128.47 `CONFIG_MODEM_SIMCOM_SIM7080_BOOT_TYPE_NORMAL`

**提示（Prompt）**：正常启动（Normal Boot）

**说明（Help）**

启动调制解调器并附着到网络（Attach to Network）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动 → 调制解调器启动类型（Modem Boot Type）

<a id="CONFIG_MODEM_SIMCOM_SIM7080_DNS_DEFAULT_RECOUNT"></a>

## 128.48 `CONFIG_MODEM_SIMCOM_SIM7080_DNS_DEFAULT_RECOUNT`

**提示（Prompt）**：DNS 查询重试次数（Retry Count）

**说明（Help）**

DNS 查询的重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_SIM7080 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_DNS_DEFAULT_TIMEOUT"></a>

## 128.49 `CONFIG_MODEM_SIMCOM_SIM7080_DNS_DEFAULT_TIMEOUT`

**提示（Prompt）**：DNS 查询超时（Timeout）

**说明（Help）**

DNS 查询的超时时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_SIM7080 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
20000
```

**取值范围（Ranges）**

```text
[0, 60000]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_INIT_PRIORITY"></a>

## 128.50 `CONFIG_MODEM_SIMCOM_SIM7080_INIT_PRIORITY`

**提示（Prompt）**：SIMCom SIM7080 驱动初始化优先级

**说明（Help）**

SIMCom SIM7080 驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_SIM7080 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_LTE_BANDS_M1"></a>

## 128.51 `CONFIG_MODEM_SIMCOM_SIM7080_LTE_BANDS_M1`

**提示（Prompt）**：CAT-M1 默认 LTE 频段

**说明（Help）**

调制解调器可用于 CAT-M1 的信道位图（Bitmap），参见枚举 `sim7080_lte_chan`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_SIM7080 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
0x8820
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_LTE_BANDS_NB1"></a>

## 128.52 `CONFIG_MODEM_SIMCOM_SIM7080_LTE_BANDS_NB1`

**提示（Prompt）**：NB-IoT 默认 LTE 频段

**说明（Help）**

调制解调器可用于 NB-IoT 的信道位图（Bitmap），参见枚举 `sim7080_lte_chan`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_SIM7080 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
0x8820
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_RAT"></a>

## 128.53 `CONFIG_MODEM_SIMCOM_SIM7080_RAT`

**提示（Prompt）**：默认无线接入技术模式（Radio Access Technology Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_SIM7080 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_SIMCOM_SIM7080_RAT_NB1
```

**可选项（Choices）**

```text
CONFIG_MODEM_SIMCOM_SIM7080_RAT_NB1
CONFIG_MODEM_SIMCOM_SIM7080_RAT_M1
CONFIG_MODEM_SIMCOM_SIM7080_RAT_LTE_AUTO
CONFIG_MODEM_SIMCOM_SIM7080_RAT_GSM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_SIMCOM_SIM7080_RAT_NB1`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIMCOM_SIM7080_RAT_NB1)、[`CONFIG_MODEM_SIMCOM_SIM7080_RAT_M1`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIMCOM_SIM7080_RAT_M1)、[`CONFIG_MODEM_SIMCOM_SIM7080_RAT_LTE_AUTO`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIMCOM_SIM7080_RAT_LTE_AUTO)、[`CONFIG_MODEM_SIMCOM_SIM7080_RAT_GSM`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIMCOM_SIM7080_RAT_GSM)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_RAT_GSM"></a>

## 128.54 `CONFIG_MODEM_SIMCOM_SIM7080_RAT_GSM`

**提示（Prompt）**：全球移动通信系统（GSM）

**说明（Help）**

启用全球移动通信系统（GSM）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_SIMCOM_SIM7080_RAT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动 → 默认无线接入技术模式（Radio Access Technology Mode）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIMCOM_SIM7080_RAT`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIMCOM_SIM7080_RAT)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_RAT_LTE_AUTO"></a>

## 128.55 `CONFIG_MODEM_SIMCOM_SIM7080_RAT_LTE_AUTO`

**提示（Prompt）**：自动选择 NB-IoT 或 Cat-M1

**说明（Help）**

启用自动 LTE 技术选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_SIMCOM_SIM7080_RAT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动 → 默认无线接入技术模式（Radio Access Technology Mode）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIMCOM_SIM7080_RAT`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIMCOM_SIM7080_RAT)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_RAT_M1"></a>

## 128.56 `CONFIG_MODEM_SIMCOM_SIM7080_RAT_M1`

**提示（Prompt）**：Cat-M1

**说明（Help）**

启用 Cat-M1 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_SIMCOM_SIM7080_RAT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动 → 默认无线接入技术模式（Radio Access Technology Mode）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIMCOM_SIM7080_RAT`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIMCOM_SIM7080_RAT)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_RAT_NB1"></a>

## 128.57 `CONFIG_MODEM_SIMCOM_SIM7080_RAT_NB1`

**提示（Prompt）**：窄带物联网（NB-IoT）

**说明（Help）**

启用 LTE NB-IoT 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_SIMCOM_SIM7080_RAT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动 → 默认无线接入技术模式（Radio Access Technology Mode）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIMCOM_SIM7080_RAT`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIMCOM_SIM7080_RAT)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_RX_STACK_SIZE"></a>

## 128.58 `CONFIG_MODEM_SIMCOM_SIM7080_RX_STACK_SIZE`

**提示（Prompt）**：SIMCom SIM7080 调制解调器驱动接收线程栈大小

**说明（Help）**

此栈由 SIMCom SIM7080 接收（RX）线程使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_SIM7080 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1028
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_RX_WORKQ_STACK_SIZE"></a>

## 128.59 `CONFIG_MODEM_SIMCOM_SIM7080_RX_WORKQ_STACK_SIZE`

**提示（Prompt）**：SIMCom SIM7080 调制解调器驱动工作队列栈大小

**说明（Help）**

此栈由工作队列（Work Queue）使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_SIM7080 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_SOCKETS_SOCKOPT_TLS"></a>

## 128.60 `CONFIG_MODEM_SIMCOM_SIM7080_SOCKETS_SOCKOPT_TLS`

**提示（Prompt）**：套接字的传输层安全（TLS）支持

**说明（Help）**

此选项为 SIM7080 调制解调器上的套接字启用传输层安全（Transport Layer Security，TLS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_SIM7080 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_SIMCOM_SIM7080_TLS_BUFFER_SIZE"></a>

## 128.61 `CONFIG_MODEM_SIMCOM_SIM7080_TLS_BUFFER_SIZE`

**提示（Prompt）**：TLS 证书复制缓冲区大小（Certificate Copy Buffer Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_SIMCOM_SIM7080_SOCKETS_SOCKOPT_TLS && CONFIG_MODEM_SIM7080 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/simcom/sim7080/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/simcom/sim7080/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → SIM7080 驱动 → 套接字的传输层安全（TLS）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SIMCOM_SIM7080_SOCKETS_SOCKOPT_TLS`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIMCOM_SIM7080_SOCKETS_SOCKOPT_TLS)、[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_SIM_NUMBERS"></a>

## 128.62 `CONFIG_MODEM_SIM_NUMBERS`

**提示（Prompt）**：向 SIM 查询 IMSI 和 ICCID

**说明（Help）**

向 SIM 卡查询国际移动用户识别码（IMSI）和集成电路卡标识符（ICCID）。如果应用不使用 SIM，可禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/Kconfig:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_SOCKET"></a>

## 128.63 `CONFIG_MODEM_SOCKET`

**提示（Prompt）**：通用调制解调器套接字支持层（Socket Support Layer）

**说明（Help）**

此层提供跟踪调制解调器“套接字”整个生命周期的大部分基础功能，覆盖最初的卸载 API 调用直至命令处理程序回调层。要配置并使用此层，应创建带套接字数据的 `modem_socket_config` 对象，将其引用传给 `modem_socket_init()`。注意，调制解调器套接字使用运行时从 `fdtable` 预留并分配的文件描述符（File Descriptor），其最大数量由 Kconfig 选项 `ZVFS_OPEN_MAX` 设置。调制解调器套接字与启用时的 `POSIX_API` 会共享这些描述符，因此务必相应调整该值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_MODEM
```

**被选择（Selected by）**

```text
CONFIG_MODEM_HL78XX
CONFIG_MODEM_QUECTEL_BG9X
CONFIG_MODEM_SIM7080
CONFIG_MODEM_ST87MXX
CONFIG_MODEM_UBLOX_SARA
```

**定义位置（Location）**：[`drivers/modem/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM_QUECTEL_BG9X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BG9X)、[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM_ST87MXX`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_ST87MXX)、[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)。

<a id="CONFIG_MODEM_SOCKET_PACKET_COUNT"></a>

## 128.64 `CONFIG_MODEM_SOCKET_PACKET_COUNT`

**提示（Prompt）**：每个套接字保存的数据包大小最大数量

**说明（Help）**

调制解调器指示还有数据可接收时，相应数值会组织为“数据包”（Packet）。此设置限制套接字可跟踪的数据包大小条目最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_SOCKET && CONFIG_MODEM
```

**默认值（Defaults）**

```text
6
```

**定义位置（Location）**：[`drivers/modem/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用调制解调器套接字支持层（Socket Support Layer）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SOCKET`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SOCKET)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_ST87MXX"></a>

## 128.65 `CONFIG_MODEM_ST87MXX`

**提示（Prompt）**：ST87MXX 调制解调器驱动

**说明（Help）**

启用 ST87M01 NB-IoT 调制解调器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_MODEM_CMD_HANDLER
CONFIG_MODEM_CONTEXT
CONFIG_MODEM_IFACE_UART
CONFIG_MODEM_RECEIVER
CONFIG_MODEM_SOCKET
CONFIG_NET_OFFLOAD
CONFIG_NET_SOCKETS_OFFLOAD
```

**弱选择（Implies）**

```text
CONFIG_GPIO
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/st87mxx/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st87mxx/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/st87mxx/Kconfig.st87mxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/st87mxx/Kconfig.st87mxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_CMD_HANDLER`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CMD_HANDLER)、[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM_IFACE_UART`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART)、[`CONFIG_MODEM_RECEIVER`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_RECEIVER)、[`CONFIG_MODEM_SOCKET`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SOCKET)、[`CONFIG_NET_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_OFFLOAD)、[`CONFIG_NET_SOCKETS_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_MODEM_ST87MXX_INIT_PRIORITY"></a>

## 128.66 `CONFIG_MODEM_ST87MXX_INIT_PRIORITY`

**提示（Prompt）**：ST87M01 驱动初始化优先级

**说明（Help）**

ST87M01 设备驱动的初始化优先级。除非清楚其影响，否则不要随意更改。注意，数值需要低于网络协议栈的初始化优先级，使它能在网络子系统之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_ST87MXX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/st87mxx/Kconfig.st87mxx:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/st87mxx/Kconfig.st87mxx#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → ST87MXX 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_ST87MXX`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_ST87MXX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_ST87MXX_MAX_RX_DATA_LENGTH"></a>

## 128.67 `CONFIG_MODEM_ST87MXX_MAX_RX_DATA_LENGTH`

**提示（Prompt）**：ST87M01 调制解调器接收缓冲区大小

**说明（Help）**

此缓冲区由 ST87M01 接收（RX）AT 命令逻辑使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_ST87MXX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/st87mxx/Kconfig.st87mxx:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/st87mxx/Kconfig.st87mxx#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → ST87MXX 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_ST87MXX`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_ST87MXX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_ST87MXX_MAX_TX_DATA_LENGTH"></a>

## 128.68 `CONFIG_MODEM_ST87MXX_MAX_TX_DATA_LENGTH`

**提示（Prompt）**：ST87M01 调制解调器发送缓冲区大小

**说明（Help）**

此缓冲区由 ST87M01 发送（TX）AT 命令逻辑使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_ST87MXX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/st87mxx/Kconfig.st87mxx:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/st87mxx/Kconfig.st87mxx#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → ST87MXX 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_ST87MXX`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_ST87MXX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_ST87MXX_RX_STACK_SIZE"></a>

## 128.69 `CONFIG_MODEM_ST87MXX_RX_STACK_SIZE`

**提示（Prompt）**：ST87M01 调制解调器驱动接收线程栈大小

**说明（Help）**

此栈由 ST87M01 接收线程使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_ST87MXX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/st87mxx/Kconfig.st87mxx:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/st87mxx/Kconfig.st87mxx#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → ST87MXX 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_ST87MXX`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_ST87MXX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_UBLOX_SARA"></a>

## 128.70 `CONFIG_MODEM_UBLOX_SARA`

**提示（Prompt）**：u-blox SARA 调制解调器驱动

**说明（Help）**

选择此设置，以启用 u-blox SARA-R4 LTE-CatM1/NB-IoT 调制解调器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_MODEM_CONTEXT
CONFIG_MODEM_CMD_HANDLER
CONFIG_MODEM_IFACE_UART
CONFIG_MODEM_SOCKET
CONFIG_NET_OFFLOAD
CONFIG_NET_SOCKETS_OFFLOAD
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/sparkfun_sara_r4/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/sparkfun_sara_r4/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM_CMD_HANDLER`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CMD_HANDLER)、[`CONFIG_MODEM_IFACE_UART`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART)、[`CONFIG_MODEM_SOCKET`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SOCKET)、[`CONFIG_NET_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_OFFLOAD)、[`CONFIG_NET_SOCKETS_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD)。

<a id="CONFIG_MODEM_UBLOX_SARA_AUTODETECT_APN"></a>

## 128.71 `CONFIG_MODEM_UBLOX_SARA_AUTODETECT_APN`

**提示（Prompt）**：自动检测接入点名称（APN）

**说明（Help）**

启用基于 IMSI 自动检测 APN。检测失败时，使用已配置的 APN。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_UBLOX_SARA && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_UBLOX_SARA_AUTODETECT_APN_PROFILES"></a>

## 128.72 `CONFIG_MODEM_UBLOX_SARA_AUTODETECT_APN_PROFILES`

**提示（Prompt）**：自动检测 APN 时搜索的配置文件列表（Profiles）

**说明（Help）**

设置以逗号分隔的配置文件列表，每项包含以下内容：

```text
<apn>=<IMSI_1> ... <IMSI_n>
```

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_UBLOX_SARA && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"hologram=23450, wm=20601 29505 29509 23450 53703 90143"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_UBLOX_SARA_AUTODETECT_VARIANT"></a>

## 128.73 `CONFIG_MODEM_UBLOX_SARA_AUTODETECT_VARIANT`

**提示（Prompt）**：自动检测（Detect Automatically）

**说明（Help）**

启用自动检测调制解调器变体（SARA-R4 或 SARA-U2）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_UBLOX_SARA_VARIANT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动 → u-blox SARA 变体选择（Variant Selection）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA_VARIANT`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA_VARIANT)。

<a id="CONFIG_MODEM_UBLOX_SARA_R4"></a>

## 128.74 `CONFIG_MODEM_UBLOX_SARA_R4`

**提示（Prompt）**：u-blox SARA-R4

**说明（Help）**

启用 SARA-R4 调制解调器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_UBLOX_SARA_VARIANT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动 → u-blox SARA 变体选择（Variant Selection）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA_VARIANT`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA_VARIANT)。

<a id="CONFIG_MODEM_UBLOX_SARA_R4_APN"></a>

## 128.75 `CONFIG_MODEM_UBLOX_SARA_R4_APN`

**提示（Prompt）**：用于建立网络连接的接入点名称（APN）

**说明（Help）**

此设置用于 `AT+CGDCONT` 命令，为网络连接上下文设置 APN 名称。它取决于网络提供商，可能需要更改。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_UBLOX_SARA && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"hologram"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_UBLOX_SARA_R4_INIT_PRIORITY"></a>

## 128.76 `CONFIG_MODEM_UBLOX_SARA_R4_INIT_PRIORITY`

**提示（Prompt）**：u-blox SARA-R4 驱动初始化优先级

**说明（Help）**

u-blox SARA-R4 设备驱动的初始化优先级。除非清楚其影响，否则不要随意更改。注意，数值需要低于网络协议栈的初始化优先级，使它能在网络子系统之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_UBLOX_SARA && CONFIG_MODEM
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_UBLOX_SARA_R4_MANUAL_MCCMNO"></a>

## 128.77 `CONFIG_MODEM_UBLOX_SARA_R4_MANUAL_MCCMNO`

**提示（Prompt）**：用于建立网络连接的 MCC/MNO

**说明（Help）**

此设置用于 `AT+COPS` 命令，为网络连接上下文设置 MCC/MNO。它取决于网络提供商，未选择自动模式时可能需要更改。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_UBLOX_SARA && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_UBLOX_SARA_R4_NET_STATUS"></a>

## 128.78 `CONFIG_MODEM_UBLOX_SARA_R4_NET_STATUS`

**提示（Prompt）**：网络状态指示（Network Status Indication）支持

**说明（Help）**

选择此设置，以使用调制解调器的一个 GPIO 引脚作为网络指示。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_UBLOX_SARA && CONFIG_MODEM
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/sparkfun_sara_r4/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/sparkfun_sara_r4/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_UBLOX_SARA_R4_NET_STATUS_PIN"></a>

## 128.79 `CONFIG_MODEM_UBLOX_SARA_R4_NET_STATUS_PIN`

**提示（Prompt）**：网络状态指示 GPIO ID

**说明（Help）**

此设置用于将调制解调器的一个 GPIO 引脚配置为网络状态指示。GPIO ID 及其与引脚编号的映射，请参见手册。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_UBLOX_SARA_R4_NET_STATUS && CONFIG_MODEM_UBLOX_SARA && CONFIG_MODEM
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动 → 网络状态指示（Network Status Indication）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA_R4_NET_STATUS`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA_R4_NET_STATUS)、[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_UBLOX_SARA_R4_RX_STACK_SIZE"></a>

## 128.80 `CONFIG_MODEM_UBLOX_SARA_R4_RX_STACK_SIZE`

**提示（Prompt）**：u-blox SARA-R4 调制解调器驱动接收线程栈大小

**说明（Help）**

此栈由 u-blox SARA-R4 接收（RX）线程使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_UBLOX_SARA && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1028
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_UBLOX_SARA_R4_RX_WORKQ_STACK_SIZE"></a>

## 128.81 `CONFIG_MODEM_UBLOX_SARA_R4_RX_WORKQ_STACK_SIZE`

**提示（Prompt）**：u-blox SARA-R4 调制解调器驱动工作队列栈大小

**说明（Help）**

工作队列（Work Queue）使用此栈，将 `net_pkt` 数据交给网络协议栈的其他部分，使接收线程能继续处理数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_UBLOX_SARA && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_UBLOX_SARA_RSSI_WORK"></a>

## 128.82 `CONFIG_MODEM_UBLOX_SARA_RSSI_WORK`

**提示（Prompt）**：RSSI 轮询工作项（Polling Work）

**说明（Help）**

将 u-blox SARA-R4 设备配置为轮询接收信号强度指示（RSSI）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_UBLOX_SARA && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_UBLOX_SARA_RSSI_WORK_PERIOD"></a>

## 128.83 `CONFIG_MODEM_UBLOX_SARA_RSSI_WORK_PERIOD`

**提示（Prompt）**：配置 RSSI 工作项轮询频率（Polling Frequency）

**说明（Help）**

此设置用于配置 RSSI 轮询周期。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_UBLOX_SARA_RSSI_WORK && CONFIG_MODEM_UBLOX_SARA && CONFIG_MODEM
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动 → RSSI 轮询工作项（Polling Work）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA_RSSI_WORK`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA_RSSI_WORK)、[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_UBLOX_SARA_U2"></a>

## 128.84 `CONFIG_MODEM_UBLOX_SARA_U2`

**提示（Prompt）**：u-blox SARA-U2

**说明（Help）**

启用 SARA-U2 调制解调器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_UBLOX_SARA_VARIANT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动 → u-blox SARA 变体选择（Variant Selection）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA_VARIANT`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA_VARIANT)。

<a id="CONFIG_MODEM_UBLOX_SARA_VARIANT"></a>

## 128.85 `CONFIG_MODEM_UBLOX_SARA_VARIANT`

**提示（Prompt）**：u-blox SARA 变体选择（Variant Selection）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_UBLOX_SARA && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_UBLOX_SARA_R4
```

**可选项（Choices）**

```text
CONFIG_MODEM_UBLOX_SARA_R4
CONFIG_MODEM_UBLOX_SARA_U2
CONFIG_MODEM_UBLOX_SARA_AUTODETECT_VARIANT
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/sparkfun_sara_r4/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/sparkfun_sara_r4/Kconfig.defconfig)。

```text
CONFIG_MODEM_UBLOX_SARA_R4
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/ublox-sara/Kconfig.ublox-sara-r4#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → u-blox SARA 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_UBLOX_SARA_R4`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA_R4)、[`CONFIG_MODEM_UBLOX_SARA_U2`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA_U2)、[`CONFIG_MODEM_UBLOX_SARA_AUTODETECT_VARIANT`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA_AUTODETECT_VARIANT)。

<a id="CONFIG_MODEM_WNCM14A2A"></a>

## 128.86 `CONFIG_MODEM_WNCM14A2A`

**提示（Prompt）**：Wistron LTE-M 调制解调器驱动

**说明（Help）**

选择此设置，以启用 Wistron WNC-M14A2A LTE-M 调制解调器驱动。注意：原文说明，当前引脚设置仅适用于 FRDM K64F 扩展板（Shield）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_MODEM_RECEIVER
CONFIG_NET_OFFLOAD
```

**弱选择（Implies）**

```text
CONFIG_GPIO
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/wnc_m14a2a/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/wnc_m14a2a/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/wncm14a2a/Kconfig.wncm14a2a:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/wncm14a2a/Kconfig.wncm14a2a#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_RECEIVER`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_RECEIVER)、[`CONFIG_NET_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_OFFLOAD)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_MODEM_WNCM14A2A_APN_NAME"></a>

## 128.87 `CONFIG_MODEM_WNCM14A2A_APN_NAME`

**提示（Prompt）**：用于建立网络连接的接入点名称（APN）

**说明（Help）**

此设置用于 `AT%PDNSET` 命令，为网络连接上下文设置 APN 名称。通常无需更改此值。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_WNCM14A2A && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"m2m.com.attz"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/wncm14a2a/Kconfig.wncm14a2a:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/wncm14a2a/Kconfig.wncm14a2a#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Wistron LTE-M 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_WNCM14A2A`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_WNCM14A2A)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_WNCM14A2A_INIT_PRIORITY"></a>

## 128.88 `CONFIG_MODEM_WNCM14A2A_INIT_PRIORITY`

**提示（Prompt）**：WNC-M14A2A 驱动初始化优先级

**说明（Help）**

WNC-M14A2A 设备驱动的初始化优先级。除非清楚其影响，否则不要随意更改。注意，数值需要低于网络协议栈的初始化优先级，使它能在网络子系统之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_WNCM14A2A && CONFIG_MODEM
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/wncm14a2a/Kconfig.wncm14a2a:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/wncm14a2a/Kconfig.wncm14a2a#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Wistron LTE-M 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_WNCM14A2A`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_WNCM14A2A)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_WNCM14A2A_RX_STACK_SIZE"></a>

## 128.89 `CONFIG_MODEM_WNCM14A2A_RX_STACK_SIZE`

**提示（Prompt）**：WNC-M14A2A 调制解调器驱动接收线程栈大小

**说明（Help）**

此栈由 WNCM14A2A 接收（RX）线程使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_WNCM14A2A && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1028
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/wncm14a2a/Kconfig.wncm14a2a:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/wncm14a2a/Kconfig.wncm14a2a#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Wistron LTE-M 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_WNCM14A2A`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_WNCM14A2A)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_WNCM14A2A_RX_WORKQ_STACK_SIZE"></a>

## 128.90 `CONFIG_MODEM_WNCM14A2A_RX_WORKQ_STACK_SIZE`

**提示（Prompt）**：WNC-M14A2A 调制解调器驱动工作队列栈大小

**说明（Help）**

工作队列（Work Queue）使用此栈，将 `net_pkt` 数据交给网络协议栈的其他部分，使接收线程能继续处理数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_WNCM14A2A && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/wncm14a2a/Kconfig.wncm14a2a:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/wncm14a2a/Kconfig.wncm14a2a#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Wistron LTE-M 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_WNCM14A2A`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_WNCM14A2A)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_NTN_DYNAMIC_POSREQ_UPDATE"></a>

## 128.91 `CONFIG_NTN_DYNAMIC_POSREQ_UPDATE`

**提示（Prompt）**：动态模式下收到 POSREQ 时要求更新位置（Position Update）

**说明（Help）**

启用后，在动态模式中收到主动指示 `+KNTNEV: 'POSREQ'` 后，必须先更新用户设备（UE）位置，才能执行任何对外网络操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_NBNTN_POSITIONING && CONFIG_MODEM_HL78XX_NTN_SUPPORT && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → NB-IoT 非地面网络（NTN）位置配置

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_NBNTN_POSITIONING`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NBNTN_POSITIONING)、[`CONFIG_MODEM_HL78XX_NTN_SUPPORT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NTN_SUPPORT)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_NTN_MANUAL_ALTITUDE"></a>

## 128.92 `CONFIG_NTN_MANUAL_ALTITUDE`

**提示（Prompt）**：手动高度（Manual Altitude），单位为米

**说明（Help）**

手动输入的位置高度，以距地球表面的米数表示，范围为 `-5000.0`～`40000000.0`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NTN_POSITION_SOURCE_MANUAL && CONFIG_NTN_POSITION_SOURCE_MANUAL && CONFIG_MODEM_HL78XX_NBNTN_POSITIONING && CONFIG_MODEM_HL78XX_NTN_SUPPORT && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"0.0"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1125)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → NB-IoT 非地面网络（NTN）位置配置

**配置项引用（Symbol References）**：[`CONFIG_NTN_POSITION_SOURCE_MANUAL`](P128_drivers_modem_配置项参考_4.md#CONFIG_NTN_POSITION_SOURCE_MANUAL)、[`CONFIG_MODEM_HL78XX_NBNTN_POSITIONING`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NBNTN_POSITIONING)、[`CONFIG_MODEM_HL78XX_NTN_SUPPORT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NTN_SUPPORT)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_NTN_MANUAL_LATITUDE"></a>

## 128.93 `CONFIG_NTN_MANUAL_LATITUDE`

**提示（Prompt）**：手动纬度（Manual Latitude），单位为度

**说明（Help）**

手动输入的位置纬度，单位为度。北纬为正，南纬为负；采用 WGS84，范围为 `-90.0`～`90.0`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NTN_POSITION_SOURCE_MANUAL && CONFIG_NTN_POSITION_SOURCE_MANUAL && CONFIG_MODEM_HL78XX_NBNTN_POSITIONING && CONFIG_MODEM_HL78XX_NTN_SUPPORT && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"0.0"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1111)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → NB-IoT 非地面网络（NTN）位置配置

**配置项引用（Symbol References）**：[`CONFIG_NTN_POSITION_SOURCE_MANUAL`](P128_drivers_modem_配置项参考_4.md#CONFIG_NTN_POSITION_SOURCE_MANUAL)、[`CONFIG_MODEM_HL78XX_NBNTN_POSITIONING`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NBNTN_POSITIONING)、[`CONFIG_MODEM_HL78XX_NTN_SUPPORT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NTN_SUPPORT)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_NTN_MANUAL_LONGITUDE"></a>

## 128.94 `CONFIG_NTN_MANUAL_LONGITUDE`

**提示（Prompt）**：手动经度（Manual Longitude），单位为度

**说明（Help）**

手动输入的位置经度，单位为度。东经为正，西经为负；采用 WGS84，范围为 `-180.0`～`180.0`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NTN_POSITION_SOURCE_MANUAL && CONFIG_NTN_POSITION_SOURCE_MANUAL && CONFIG_MODEM_HL78XX_NBNTN_POSITIONING && CONFIG_MODEM_HL78XX_NTN_SUPPORT && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"0.0"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1118)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → NB-IoT 非地面网络（NTN）位置配置

**配置项引用（Symbol References）**：[`CONFIG_NTN_POSITION_SOURCE_MANUAL`](P128_drivers_modem_配置项参考_4.md#CONFIG_NTN_POSITION_SOURCE_MANUAL)、[`CONFIG_MODEM_HL78XX_NBNTN_POSITIONING`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NBNTN_POSITIONING)、[`CONFIG_MODEM_HL78XX_NTN_SUPPORT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NTN_SUPPORT)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_NTN_MOBILITY_TYPE_DYNAMIC"></a>

## 128.95 `CONFIG_NTN_MOBILITY_TYPE_DYNAMIC`

**提示（Prompt）**：DYNAMIC：动态位置（Moving Position）

**说明（Help）**

位置可能变化，每次网络操作都需要更新。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1087`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1087)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → NB-IoT 非地面网络（NTN）位置配置 → 移动性类型（Mobility Type）

<a id="CONFIG_NTN_MOBILITY_TYPE_STATIC"></a>

## 128.96 `CONFIG_NTN_MOBILITY_TYPE_STATIC`

**提示（Prompt）**：STATIC：固定位置（Fixed Position）

**说明（Help）**

位置保持固定，即在初次定位结果的 600 米范围内。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1082`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1082)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → NB-IoT 非地面网络（NTN）位置配置 → 移动性类型（Mobility Type）

<a id="CONFIG_NTN_POSITION_SOURCE_IGNSS"></a>

## 128.97 `CONFIG_NTN_POSITION_SOURCE_IGNSS`

**提示（Prompt）**：IGNSS：内部 GNSS（Internal GNSS）

**说明（Help）**

使用 HL781x 内部 GNSS 自动获取位置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1062`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1062)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → NB-IoT 非地面网络（NTN）位置配置 → 位置来源（Position Source）

<a id="CONFIG_NTN_POSITION_SOURCE_MANUAL"></a>

## 128.98 `CONFIG_NTN_POSITION_SOURCE_MANUAL`

**提示（Prompt）**：MANUAL：手动输入（Manual Entry）

**说明（Help）**

使用 `+KNTNCMD` AT 命令手动输入用户设备（UE）位置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1067`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1067)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → NB-IoT 非地面网络（NTN）位置配置 → 位置来源（Position Source）

<a id="CONFIG_NTN_STATIC_THRESHOLD"></a>

## 128.99 `CONFIG_NTN_STATIC_THRESHOLD`

**提示（Prompt）**：静态模式阈值（Static Mode Threshold），单位为米

**说明（Help）**

用于判定静态／动态模式的当前位置与初次定位结果之间的距离。如果位置变化超过此阈值，原文建议使用动态模式。此项仅用于文档／参考。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_NBNTN_POSITIONING && CONFIG_MODEM_HL78XX_NTN_SUPPORT && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
600
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1094`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1094)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → NB-IoT 非地面网络（NTN）位置配置

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_NBNTN_POSITIONING`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NBNTN_POSITIONING)、[`CONFIG_MODEM_HL78XX_NTN_SUPPORT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NTN_SUPPORT)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<!-- kconfig-navigation -->

[上一章](P127_drivers_modem_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P129_drivers_mspi_配置项参考.md)
