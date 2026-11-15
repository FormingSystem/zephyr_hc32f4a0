---
id: learning.zephyr-docs.kconfig-reference.page-75
title: "`drivers/debug`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第75章\_`drivers/debug`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/debug` 的 30 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DEBUG_CORESIGHT_NRF"></a>

## 75.1 `CONFIG_DEBUG_CORESIGHT_NRF`

**提示（Prompt）**：CoreSight 跟踪（Trace）支持

**说明（Help）**

支持测试与调试域（Test and Debug Domain）中的 CoreSight 外设，以提供 ARM CoreSight 系统跟踪宏单元（System Trace Macrocell，STM）跟踪功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_CORESIGHT_NRF_ENABLED && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_IRONSIDE_SE_CALL
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_IRONSIDE_SE_CALL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IRONSIDE_SE_CALL)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_ATBFUNNEL_HOLD_TIME"></a>

## 75.2 `CONFIG_DEBUG_CORESIGHT_NRF_ATBFUNNEL_HOLD_TIME`

**提示（Prompt）**：ATBFUNNEL：事务保持时间（Transaction Hold Time）

**说明（Help）**

在漏斗（Funnel）主端口上输出的、来自同一从端口的事务（Transaction）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_CORESIGHT_NRF && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 15]
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L203)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_CORESIGHT_NRF)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_ATB_TRACE_ID_STM_GLOBAL"></a>

## 75.3 `CONFIG_DEBUG_CORESIGHT_NRF_ATB_TRACE_ID_STM_GLOBAL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

STM 使用的全局跟踪标识符（Global Trace ID）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_CORESIGHT_NRF && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
0x40
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_CORESIGHT_NRF)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_STM_HWEVENTS"></a>

## 75.4 `CONFIG_DEBUG_CORESIGHT_NRF_STM_HWEVENTS`

**提示（Prompt）**：STM：启用硬件事件（Hardware Events）

**说明（Help）**

启用 STM 中硬件事件（Hardware Events）的输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_CORESIGHT_NRF && CONFIG_DEBUG_DRIVER
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:183`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L183)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_CORESIGHT_NRF)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_STM_SYNC_BYTE_COUNT"></a>

## 75.5 `CONFIG_DEBUG_CORESIGHT_NRF_STM_SYNC_BYTE_COUNT`

**提示（Prompt）**：STM：每 N 字节发送一个同步包（Synchronization Packet）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_CORESIGHT_NRF && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[0, 4095]
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_CORESIGHT_NRF)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_TPIU_FFCR_TRIG"></a>

## 75.6 `CONFIG_DEBUG_CORESIGHT_NRF_TPIU_FFCR_TRIG`

**提示（Prompt）**：TPIU：使用刷新请求触发（Flush Request Trigger）

**说明（Help）**

使用 CTI 通道 1 触发 TPIU 的刷新请求（Flush Request）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_CORESIGHT_NRF && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:188`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L188)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_CORESIGHT_NRF)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_TPIU_PORTSIZE"></a>

## 75.7 `CONFIG_DEBUG_CORESIGHT_NRF_TPIU_PORTSIZE`

**提示（Prompt）**：TPIU：当前 TPIU 端口的位宽

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_CORESIGHT_NRF && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L198)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_CORESIGHT_NRF)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_TPIU_SYNC_FRAME_COUNT"></a>

## 75.8 `CONFIG_DEBUG_CORESIGHT_NRF_TPIU_SYNC_FRAME_COUNT`

**提示（Prompt）**：TPIU：每 N 帧发送一个同步包（Synchronization Packet）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_CORESIGHT_NRF && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_CORESIGHT_NRF)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_TSGEN_CLK_DIV"></a>

## 75.9 `CONFIG_DEBUG_CORESIGHT_NRF_TSGEN_CLK_DIV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

生成跟踪时间戳（Trace Timestamp）所用的时钟分频系数（Clock Division Factor）。时间戳计数器的时钟频率不应低于系统中最快处理器时钟频率的 10%，因此其时钟采用八分频。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_CORESIGHT_NRF && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_CORESIGHT_NRF)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_DRIVER"></a>

## 75.10 `CONFIG_DEBUG_DRIVER`

**提示（Prompt）**：调试驱动（Debug Drivers）

**说明（Help）**

启用调试驱动（Debug Drivers）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/debug/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_DEBUG_DRIVER_INIT_PRIORITY"></a>

## 75.11 `CONFIG_DEBUG_DRIVER_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

调试驱动（Debug Drivers）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/debug/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_DEBUG_NRF_ETR"></a>

## 75.12 `CONFIG_DEBUG_NRF_ETR`

**提示（Prompt）**：CoreSight ETR 处理模块（使用 Nordic TBM）

**说明（Help）**

此模块处理 ETR 环形缓冲区（Circular Buffer）中存储的数据，例如 STM 日志数据。通过 Nordic Semiconductor SoC 专用的跟踪缓冲区监视器（Trace Buffer Monitor，TBM）外设跟踪缓冲区的忙碌程度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_TBM
```

**弱选择（Implies）**

```text
CONFIG_UART_ASYNC_API
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_TBM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_TBM)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)。

<a id="CONFIG_DEBUG_NRF_ETR_BACKEND_RTT"></a>

## 75.13 `CONFIG_DEBUG_NRF_ETR_BACKEND_RTT`

**提示（Prompt）**：RTT 后端（Backend）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**主动选择（Selects）**

```text
CONFIG_USE_SEGGER_RTT
CONFIG_SEGGER_RTT_CUSTOM_LOCKING
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)、[`CONFIG_USE_SEGGER_RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_SEGGER_RTT)、[`CONFIG_SEGGER_RTT_CUSTOM_LOCKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_RTT_CUSTOM_LOCKING)。

<a id="CONFIG_DEBUG_NRF_ETR_BACKEND_RTT_BUFFER"></a>

## 75.14 `CONFIG_DEBUG_NRF_ETR_BACKEND_RTT_BUFFER`

**提示（Prompt）**：用于日志输出（Logger Output）的缓冲区编号。

**说明（Help）**

选择用于日志输出（Logger Output）的上行缓冲区（Up-Buffer）索引；默认使用终端上行缓冲区及其设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR_BACKEND_RTT && CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS]
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM） → RTT 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR_BACKEND_RTT`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_BACKEND_RTT)、[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)、[`CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS)。

<a id="CONFIG_DEBUG_NRF_ETR_BACKEND_RTT_BUFFER_SIZE"></a>

## 75.15 `CONFIG_DEBUG_NRF_ETR_BACKEND_RTT_BUFFER_SIZE`

**提示（Prompt）**：为日志输出（Logger Output）预留的上行缓冲区（Up-Buffer）大小。

**说明（Help）**

指定用于日志输出（Logger Output）的上行缓冲区（Up-Buffer）预留大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR_BACKEND_RTT_BUFFER > 0 && CONFIG_DEBUG_NRF_ETR_BACKEND_RTT && CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM） → RTT 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR_BACKEND_RTT_BUFFER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_BACKEND_RTT_BUFFER)、[`CONFIG_DEBUG_NRF_ETR_BACKEND_RTT`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_BACKEND_RTT)、[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_NRF_ETR_BACKEND_RTT_RETRY_CNT"></a>

## 75.16 `CONFIG_DEBUG_NRF_ETR_BACKEND_RTT_RETRY_CNT`

**提示（Prompt）**：重试次数（Number of Retries）

**说明（Help）**

在丢弃数据并认定 RTT 会话（Session）未活动之前，进行发送（TX）重试的次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR_BACKEND_RTT && CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM） → RTT 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR_BACKEND_RTT`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_BACKEND_RTT)、[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_NRF_ETR_BACKEND_RTT_RETRY_DELAY_MS"></a>

## 75.17 `CONFIG_DEBUG_NRF_ETR_BACKEND_RTT_RETRY_DELAY_MS`

**提示（Prompt）**：发送重试间隔，单位为毫秒（TX Retry Delay）

**说明（Help）**

两次发送重试（TX Retry）之间的休眠时间。实时传输（RTT）会话期间，主机定期拉取数据，周期从 1–2 毫秒起；RTT 流量增加时，包括主机到设备的流量，该周期可能增加。流量较大时可能丢失数据，需要增大延迟或重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR_BACKEND_RTT && CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM） → RTT 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR_BACKEND_RTT`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_BACKEND_RTT)、[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_NRF_ETR_BACKEND_UART"></a>

## 75.18 `CONFIG_DEBUG_NRF_ETR_BACKEND_UART`

**提示（Prompt）**：UART 后端（backend）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_NRF_ETR_BACKOFF"></a>

## 75.19 `CONFIG_DEBUG_NRF_ETR_BACKOFF`

**提示（Prompt）**：线程退避时间（Thread Backoff Time），单位为毫秒

**说明（Help）**

决定尝试转储（Dump）数据的频率。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_NRF_ETR_DEBUG"></a>

## 75.20 `CONFIG_DEBUG_NRF_ETR_DEBUG`

**提示（Prompt）**：调试模式（Debug Mode）

**说明（Help）**

在调试模式（Debug Mode）下，打印经 STPv2 解码的数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_PRINTK && CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**主动选择（Selects）**

```text
CONFIG_MIPI_STP_DECODER
CONFIG_CS_TRACE_DEFMT
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM）

**配置项引用（Symbol References）**：[`CONFIG_LOG_PRINTK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_PRINTK)、[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)、[`CONFIG_MIPI_STP_DECODER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_STP_DECODER)、[`CONFIG_CS_TRACE_DEFMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CS_TRACE_DEFMT)。

<a id="CONFIG_DEBUG_NRF_ETR_DECODE"></a>

## 75.21 `CONFIG_DEBUG_NRF_ETR_DECODE`

**提示（Prompt）**：解码 ETR 内容（Decode ETR Content）

**说明（Help）**

在此模式下，对 CoreSight STM 日志前端（Logging Frontend）存储的日志消息进行解码，并以人可读的形式打印。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_LOG_FRONTEND_STMESP_FSC
```

**主动选择（Selects）**

```text
CONFIG_MIPI_STP_DECODER
CONFIG_CS_TRACE_DEFMT
CONFIG_LOG_FRONTEND_STMESP_DEMUX
CONFIG_LOG_OUTPUT
```

**弱选择（Implies）**

```text
CONFIG_LOG_BACKEND_SHOW_COLOR
CONFIG_CBPRINTF_FP_SUPPORT
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)、[`CONFIG_LOG_FRONTEND_STMESP_FSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_FRONTEND_STMESP_FSC)、[`CONFIG_MIPI_STP_DECODER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_STP_DECODER)、[`CONFIG_CS_TRACE_DEFMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CS_TRACE_DEFMT)、[`CONFIG_LOG_FRONTEND_STMESP_DEMUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_FRONTEND_STMESP_DEMUX)、[`CONFIG_LOG_OUTPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_OUTPUT)、[`CONFIG_LOG_BACKEND_SHOW_COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BACKEND_SHOW_COLOR)、[`CONFIG_CBPRINTF_FP_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CBPRINTF_FP_SUPPORT)。

<a id="CONFIG_DEBUG_NRF_ETR_DECODE_DROP_PERIOD"></a>

## 75.22 `CONFIG_DEBUG_NRF_ETR_DECODE_DROP_PERIOD`

**提示（Prompt）**：消息丢弃通知周期（Dropped Messages Notification Period）

**说明（Help）**

检查是否发生消息丢弃的周期，以毫秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_NRF_ETR_FLUSH_TIMEOUT"></a>

## 75.23 `CONFIG_DEBUG_NRF_ETR_FLUSH_TIMEOUT`

**提示（Prompt）**：刷新期间的退避时间（Backoff Time During Flushing），单位为毫秒

**说明（Help）**

线程触发 ETR 数据刷新（Flushing）后，会定期检查是否仍有待处理的 ETR 数据。此选项指定线程唤醒并执行检查的周期，以毫秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_NRF_ETR_SHELL"></a>

## 75.24 `CONFIG_DEBUG_NRF_ETR_SHELL`

**提示（Prompt）**：使用命令行（Shell）

**说明（Help）**

启用支持 CoreSight STM 日志的命令行（Shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR_DECODE && CONFIG_DEBUG_NRF_ETR_BACKEND_UART && CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_SHELL
```

**主动选择（Selects）**

```text
CONFIG_UART_ASYNC_API
CONFIG_UART_ASYNC_RX_HELPER
CONFIG_SHELL_LOG_BACKEND_CUSTOM
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR_DECODE`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_DECODE)、[`CONFIG_DEBUG_NRF_ETR_BACKEND_UART`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_BACKEND_UART)、[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_ASYNC_RX_HELPER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_RX_HELPER)、[`CONFIG_SHELL_LOG_BACKEND_CUSTOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_LOG_BACKEND_CUSTOM)。

<a id="CONFIG_DEBUG_NRF_ETR_SHELL_ASYNC_RX_BUFFER_COUNT"></a>

## 75.25 `CONFIG_DEBUG_NRF_ETR_SHELL_ASYNC_RX_BUFFER_COUNT`

**提示（Prompt）**：接收缓冲区（RX Buffer）数量

**说明（Help）**

接收缓冲区（RX Buffer）的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR_SHELL && CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[2, 64]
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM） → 使用命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR_SHELL`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_SHELL)、[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_NRF_ETR_SHELL_ASYNC_RX_BUFFER_SIZE"></a>

## 75.26 `CONFIG_DEBUG_NRF_ETR_SHELL_ASYNC_RX_BUFFER_SIZE`

**提示（Prompt）**：接收缓冲区（RX Buffer）大小

**说明（Help）**

单个接收缓冲区（RX Buffer）的大小。它与缓冲区数量共同决定可容纳接收数据的空间。如果命令行（Shell）输入较慢，可以减小此值；如果会将长消息直接粘贴到命令提示符处，则可能需要增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR_SHELL && CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM） → 使用命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR_SHELL`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_SHELL)、[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_NRF_ETR_SHELL_PROMPT"></a>

## 75.27 `CONFIG_DEBUG_NRF_ETR_SHELL_PROMPT`

**提示（Prompt）**：显示的提示符名称（Prompt Name）

**说明（Help）**

支持 CoreSight STM 日志的 UART 命令行（Shell）所显示的提示符名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR_SHELL && CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
"uart:~$ "
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM） → 使用命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR_SHELL`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_SHELL)、[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<a id="CONFIG_DEBUG_NRF_ETR_STACK_SIZE"></a>

## 75.28 `CONFIG_DEBUG_NRF_ETR_STACK_SIZE`

**提示（Prompt）**：ETR 线程栈（Thread Stack）大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
2048 if CONFIG_DEBUG_NRF_ETR_DECODE || CONFIG_DEBUG_NRF_ETR_DEBUG
1024
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)、[`CONFIG_DEBUG_NRF_ETR_DECODE`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_DECODE)、[`CONFIG_DEBUG_NRF_ETR_DEBUG`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_DEBUG)。

<a id="CONFIG_DEBUG_NRF_ETR_SYNC_PERIOD"></a>

## 75.29 `CONFIG_DEBUG_NRF_ETR_SYNC_PERIOD`

**提示（Prompt）**：自定义同步帧（Custom Synchronization Frame）周期

**说明（Help）**

为帮助主机工具在解码 ETR 内容时找到同步位置，可以定期发送同步模式（Synchronization Pattern）：16 个值为 `0xFF` 的字节。此帧在 CoreSight 格式化器帧（Formatter Frame）之间发送。设为 `0` 可禁用此功能。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_NRF_ETR && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
0 if CONFIG_DEBUG_NRF_ETR_DECODE
0 if CONFIG_DEBUG_NRF_ETR_DEBUG
16
```

**定义位置（Location）**：[`drivers/debug/Kconfig.nrf:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.nrf#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight ETR 处理模块（使用 Nordic TBM）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)、[`CONFIG_DEBUG_NRF_ETR_DECODE`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_DECODE)、[`CONFIG_DEBUG_NRF_ETR_DEBUG`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_DEBUG)。

<a id="CONFIG_DEBUG_SILABS_PTI"></a>

## 75.30 `CONFIG_DEBUG_SILABS_PTI`

**提示（Prompt）**：Silicon Labs 数据包跟踪接口（Packet Trace Interface）

**说明（Help）**

启用数据包跟踪接口（Packet Trace Interface），提供查看已发送和已接收无线数据包的机制，用于网络嗅探（Network Sniffing）或调试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_PTI_ENABLED && CONFIG_PINCTRL && CONFIG_SOC_GECKO_USE_RAIL && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/debug/Kconfig.silabs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/Kconfig.silabs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers）

**配置项引用（Symbol References）**：[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_SOC_GECKO_USE_RAIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GECKO_USE_RAIL)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)。

<!-- kconfig-navigation -->

[上一章](P074_drivers_dali_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P076_drivers_disk_配置项参考.md)
