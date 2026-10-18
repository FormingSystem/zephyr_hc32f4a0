---
id: learning.zephyr-docs.kconfig-reference.page-89
title: "`drivers/ethernet`配置项参考（3/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第89章\_`drivers/ethernet`配置项参考（3/4）

本章翻译官方 Kconfig 数据库中 `drivers/ethernet` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ETH_STM32_HAL_API_V2"></a>

## 89.1 `CONFIG_ETH_STM32_HAL_API_V2`

**提示（Prompt）**：使用官方 STM32Cube 硬件抽象层（HAL）驱动

**说明（Help）**

使用官方 STM32Cube 硬件抽象层（HAL）驱动，代替旧版驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_STM32F4X || CONFIG_SOC_SERIES_STM32F7X || CONFIG_SOC_SERIES_STM32H5X || CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H7RSX || CONFIG_SOC_SERIES_STM32MP13X || CONFIG_SOC_SERIES_STM32N6X) && <choice CONFIG_ETH_STM32_HAL_API_VERSION>
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_ETH_EX if CONFIG_SOC_SERIES_STM32N6X
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver） → STM32Cube HAL 以太网版本（Ethernet Version）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32MP13X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP13X)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_ETH_STM32_HAL_API_VERSION`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_STM32_HAL_API_VERSION)、[`CONFIG_USE_STM32_HAL_ETH_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_ETH_EX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32MP13X`、`CONFIG_SOC_SERIES_STM32N6X`。

<a id="CONFIG_ETH_STM32_HAL_API_VERSION"></a>

## 89.2 `CONFIG_ETH_STM32_HAL_API_VERSION`

**提示（Prompt）**：STM32Cube HAL 以太网版本（Ethernet Version）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**可选项（Choices）**

```text
CONFIG_ETH_STM32_HAL2_API
CONFIG_ETH_STM32_HAL_API_V2
CONFIG_ETH_STM32_HAL_API_V1
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_STM32_HAL2_API`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL2_API)、[`CONFIG_ETH_STM32_HAL_API_V2`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_STM32_HAL_API_V2)、[`CONFIG_ETH_STM32_HAL_API_V1`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL_API_V1)。

<a id="CONFIG_ETH_STM32_HAL_PTP_CLOCK_ADJ_MAX_PCT"></a>

## 89.3 `CONFIG_ETH_STM32_HAL_PTP_CLOCK_ADJ_MAX_PCT`

**提示（Prompt）**：时钟频率调整上限（Clock Frequency Adjustment Upper Bound），以百分比表示

**说明（Help）**

指定精密时间协议（PTP）时钟速率调整的上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK_STM32_HAL && CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
110
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver） → STM32 HAL 精密时间协议时钟驱动支持（PTP Clock Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK_STM32_HAL`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_STM32_HAL)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_STM32_HAL_PTP_CLOCK_ADJ_MIN_PCT"></a>

## 89.4 `CONFIG_ETH_STM32_HAL_PTP_CLOCK_ADJ_MIN_PCT`

**提示（Prompt）**：时钟频率调整下限（Clock Frequency Adjustment Lower Bound），以百分比表示

**说明（Help）**

指定精密时间协议（PTP）时钟速率调整的下限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK_STM32_HAL && CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver） → STM32 HAL 精密时间协议时钟驱动支持（PTP Clock Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK_STM32_HAL`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_STM32_HAL)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_STM32_HAL_PTP_CLOCK_SRC_HZ"></a>

## 89.5 `CONFIG_ETH_STM32_HAL_PTP_CLOCK_SRC_HZ`

**提示（Prompt）**：PTP 定时器时钟源频率（Clock Source Frequency）

**说明（Help）**

设置提供给精密时间协议（PTP）定时器的时钟频率，以 Hz 为单位。数值设置正确时，定时器才能准确计时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK_STM32_HAL && CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
50000000
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver） → STM32 HAL 精密时间协议时钟驱动支持（PTP Clock Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK_STM32_HAL`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_STM32_HAL)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_STM32_HAL_RX_BUF_POOL_COUNT"></a>

## 89.6 `CONFIG_ETH_STM32_HAL_RX_BUF_POOL_COUNT`

**提示（Prompt）**：STM32 HAL 池中的接收缓冲区数量（RX Buffer Count）

**说明（Help）**

为 STM32 HAL 以太网驱动预留的完整大小接收 `net_buf` 数量。此值应大于 `ETH_STM32_HAL_RX_DMA_BUF_COUNT`，以便处理数据包期间仍有空闲缓冲区（Free Buffer）可用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_STM32_HAL2_API && CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_STM32_HAL2_API`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL2_API)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_STM32_HAL_RX_DESC_COUNT"></a>

## 89.7 `CONFIG_ETH_STM32_HAL_RX_DESC_COUNT`

**提示（Prompt）**：接收 DMA 描述符数量（RX DMA Descriptor Count）

**说明（Help）**

STM32H5 HAL 以太网驱动使用的接收 DMA 描述符（RX DMA Descriptor）数量。此设置在整个构建中全局覆盖 STM32Cube 的 `ETH_RX_DESC_CNT` 默认值，使 Zephyr 驱动与 STM32Cube HAL 使用相同的描述符数量。硬件接收时间戳（RX Timestamping）可能在数据包描述符之后使用额外的上下文描述符（Context Descriptor），因此 PTP 配置需要比 STM32Cube 默认值更深的接收描述符环（RX Descriptor Ring）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_STM32_HAL_API_V2 && CONFIG_SOC_SERIES_STM32H5X && CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
8 if CONFIG_PTP_CLOCK_STM32_HAL
4
```

**取值范围（Ranges）**

```text
[4, 64]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_STM32_HAL_API_V2`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_STM32_HAL_API_V2)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PTP_CLOCK_STM32_HAL`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_STM32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32H5X`。

<a id="CONFIG_ETH_STM32_HAL_RX_DMA_BUF_COUNT"></a>

## 89.8 `CONFIG_ETH_STM32_HAL_RX_DMA_BUF_COUNT`

**提示（Prompt）**：接收 DMA 缓冲区数量（RX DMA Buffer Count）

**说明（Help）**

为 STM32 HAL2 以太网驱动分配的接收 DMA 缓冲区（RX DMA Buffer）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_STM32_HAL2_API && CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_STM32_HAL2_API`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL2_API)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_STM32_HAL_RX_THREAD_PREEMPTIVE"></a>

## 89.9 `CONFIG_ETH_STM32_HAL_RX_THREAD_PREEMPTIVE`

**提示（Prompt）**：STM32 以太网接收线程采用抢占式调度（RX Thread Preemptive）【实验性】

**说明（Help）**

采用抢占式线程（Preemptive Thread）时，该线程可被抢占（Preempted）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PREEMPT_ENABLED && CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_NET_TC_THREAD_PREEMPTIVE
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_PREEMPT_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PREEMPT_ENABLED)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_TC_THREAD_PREEMPTIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TC_THREAD_PREEMPTIVE)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PREEMPT_ENABLED`。

<a id="CONFIG_ETH_STM32_HAL_RX_THREAD_PRIO"></a>

## 89.10 `CONFIG_ETH_STM32_HAL_RX_THREAD_PRIO`

**提示（Prompt）**：STM32 以太网接收线程优先级（RX Thread Priority）

**说明（Help）**

此选项用于配置处理传入以太网数据包的接收线程（RX Thread）的优先级。可通过 `NET_TC_THREAD_PREEMPTIVE` 在抢占式调度（Preemptive Scheduling）与协作式调度（Cooperative Scheduling）之间切换。抢占式调度可使网络流量处理的响应更及时，尤其在高负载情况下。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_STM32_HAL_RX_THREAD_STACK_SIZE"></a>

## 89.11 `CONFIG_ETH_STM32_HAL_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

接收线程栈大小（RX Thread Stack Size）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_STM32_HAL_TX_ASYNC"></a>

## 89.12 `CONFIG_ETH_STM32_HAL_TX_ASYNC`

**提示（Prompt）**：使用异步发送模式（TX Async Mode）

**说明（Help）**

启用发送异步模式（TX Asynchronous Mode），以提高吞吐性能（Throughput Performance）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_STM32_HAL_API_V2 && CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_STM32_HAL_API_V2`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_STM32_HAL_API_V2)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_STM32_HAL_TX_MAX_BUF"></a>

## 89.13 `CONFIG_ETH_STM32_HAL_TX_MAX_BUF`

**提示（Prompt）**：每个以太网数据包的最大发送缓冲区数量（Maximum TX Buffers Per Packet）

**说明（Help）**

每个以太网数据包（Ethernet Packet）的最大发送缓冲区（TX Buffer，即分片）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_STM32_HAL2_API && CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_STM32_HAL2_API`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL2_API)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_STM32_HAL_USE_DTCM_FOR_DMA_BUFFER"></a>

## 89.14 `CONFIG_ETH_STM32_HAL_USE_DTCM_FOR_DMA_BUFFER`

**提示（Prompt）**：使用 DTCM 存放 DMA 缓冲区（DMA Buffers）

**说明（Help）**

启用此选项时，用于 DMA 传输的缓冲区从 SRAM 移到数据紧耦合内存（Data Tightly Coupled Memory，DTCM）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_STM32F7X && CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F7X`。

<a id="CONFIG_ETH_STM32_HW_CHECKSUM"></a>

## 89.15 `CONFIG_ETH_STM32_HW_CHECKSUM`

**提示（Prompt）**：使用发送和接收硬件校验和（TX and RX Hardware Checksum）

**说明（Help）**

启用接收和发送校验和卸载（Checksum Offload），以提高吞吐性能（Throughput Performance）。有关此功能的更多信息，参见参考手册（Reference Manual）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_STM32H5X && CONFIG_NET_CHECKSUM_OFFLOAD && CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_NET_CHECKSUM_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32H5X`。

<a id="CONFIG_ETH_STM32_MULTICAST_FILTER"></a>

## 89.16 `CONFIG_ETH_STM32_MULTICAST_FILTER`

**提示（Prompt）**：组播哈希过滤支持（Multicast Hash Filter Support）

**说明（Help）**

在 MAC 中启用组播哈希过滤（Multicast Hash Filtering）支持。启用后，以太网 MAC 对组播目标 MAC 地址计算哈希值（Hash），据此进行非精确过滤（Imperfect Filtering）。仅接收其计算出的哈希值对应位已在组播表中置位的组播，其余组播均由 MAC 丢弃。禁用时，MAC 接收全部组播。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:183`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L183)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_SY1XX"></a>

## 89.17 `CONFIG_ETH_SY1XX`

**提示（Prompt）**：Sensry SY1XX 以太网驱动（Ethernet Driver）

**说明（Help）**

启用 Sensry SY1XX 以太网 MAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSRY_SY1XX_MAC_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.sy1xx_mac:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.sy1xx_mac#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ETH_VIRTIO_NET"></a>

## 89.18 `CONFIG_ETH_VIRTIO_NET`

**提示（Prompt）**：VIRTIO 网络半虚拟化设备驱动（Networking Paravirtualization Device Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VIRTIO_NET_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_VIRTIO
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.virtio_net:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.virtio_net#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_VIRTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIRTIO)。

<a id="CONFIG_ETH_VIRTIO_NET_RX_BUFFERS"></a>

## 89.19 `CONFIG_ETH_VIRTIO_NET_RX_BUFFERS`

**提示（Prompt）**：VIRTIO 网络设备接收缓冲区（Receive Buffers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_VIRTIO_NET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.virtio_net:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.virtio_net#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → VIRTIO 网络半虚拟化设备驱动（Networking Paravirtualization Device Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_VIRTIO_NET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_VIRTIO_NET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_W5100S"></a>

## 89.20 `CONFIG_ETH_W5100S`

**提示（Prompt）**：W5100S 以太网控制器（Ethernet Controller）

**说明（Help）**

具有 SPI 接口的 W5100S 独立以太网控制器（Stand-Alone Ethernet Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WIZNET_W5100S_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_WIZNET
CONFIG_ETH_WIZNET_CORE
CONFIG_SPI
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/ethernet/wiznet/Kconfig.w5100s:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/wiznet/Kconfig.w5100s#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_WIZNET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WIZNET)、[`CONFIG_ETH_WIZNET_CORE`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WIZNET_CORE)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_ETH_W5500"></a>

## 89.21 `CONFIG_ETH_W5500`

**提示（Prompt）**：W5500 以太网控制器（Ethernet Controller）

**说明（Help）**

具有 SPI 接口的 W5500 独立以太网控制器（Stand-Alone Ethernet Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WIZNET_W5500_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_WIZNET
CONFIG_ETH_WIZNET_CORE
CONFIG_SPI
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/ethernet/wiznet/Kconfig.w5500:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/wiznet/Kconfig.w5500#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_WIZNET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WIZNET)、[`CONFIG_ETH_WIZNET_CORE`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WIZNET_CORE)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_ETH_W6100"></a>

## 89.22 `CONFIG_ETH_W6100`

**提示（Prompt）**：W6100 以太网控制器（Ethernet Controller）

**说明（Help）**

具有 SPI 接口的 W6100 独立以太网控制器（Stand-Alone Ethernet Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WIZNET_W6100_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_WIZNET
CONFIG_ETH_WIZNET_CORE
CONFIG_SPI
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/ethernet/wiznet/Kconfig.w6100:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/wiznet/Kconfig.w6100#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_WIZNET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WIZNET)、[`CONFIG_ETH_WIZNET_CORE`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WIZNET_CORE)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_ETH_W6300"></a>

## 89.23 `CONFIG_ETH_W6300`

**提示（Prompt）**：W6300 以太网控制器（Ethernet Controller）

**说明（Help）**

具有 SPI 接口的 W6300 独立以太网控制器（Stand-Alone Ethernet Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WIZNET_W6300_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_WIZNET
CONFIG_SPI
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/ethernet/wiznet/Kconfig.w6300:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/wiznet/Kconfig.w6300#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_WIZNET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WIZNET)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_ETH_WCH"></a>

## 89.24 `CONFIG_ETH_WCH`

**提示（Prompt）**：沁恒（WCH）以太网驱动（Ethernet Driver）

**说明（Help）**

启用沁恒（WCH）以太网驱动。它适用于全部 CH32V307 和 CH32V317 微控制器（MCU）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_ETHERNET_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.wch:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.wch#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_WCH_HAL_RX_THREAD_PRIO"></a>

## 89.25 `CONFIG_ETH_WCH_HAL_RX_THREAD_PRIO`

**提示（Prompt）**：WCH 以太网接收线程优先级（RX Thread Priority）

**说明（Help）**

此选项用于配置处理传入以太网数据包的接收线程（RX Thread）的优先级。可通过 `NET_TC_THREAD_PREEMPTIVE` 在抢占式调度（Preemptive Scheduling）与协作式调度（Cooperative Scheduling）之间切换。抢占式调度可使网络流量处理的响应更及时，尤其在高负载情况下。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_WCH && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.wch:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.wch#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 沁恒（WCH）以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_WCH`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WCH)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_WCH_HAL_RX_THREAD_STACK_SIZE"></a>

## 89.26 `CONFIG_ETH_WCH_HAL_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

接收线程栈大小（RX Thread Stack Size）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_WCH && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.wch:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.wch#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 沁恒（WCH）以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_WCH`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WCH)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_WCH_HW_CHECKSUM"></a>

## 89.27 `CONFIG_ETH_WCH_HW_CHECKSUM`

**提示（Prompt）**：使用发送和接收硬件校验和（TX and RX Hardware Checksum）

**说明（Help）**

启用接收和发送校验和卸载（Checksum Offload），以提高吞吐性能（Throughput Performance）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_WCH && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.wch:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.wch#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 沁恒（WCH）以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_WCH`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WCH)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_WCH_MULTICAST_FILTER"></a>

## 89.28 `CONFIG_ETH_WCH_MULTICAST_FILTER`

**提示（Prompt）**：组播哈希过滤支持（Multicast Hash Filter Support）

**说明（Help）**

在 MAC 中启用组播哈希过滤（Multicast Hash Filtering）支持。启用后，以太网 MAC 对组播目标 MAC 地址计算哈希值（Hash），据此进行非精确过滤（Imperfect Filtering）。仅接收其计算出的哈希值对应位已在组播表中置位的组播，其余组播均由 MAC 丢弃。禁用时，MAC 接收全部组播。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_WCH && CONFIG_ETH_DRIVER
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.wch:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.wch#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 沁恒（WCH）以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_WCH`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WCH)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_ETH_WIZNET"></a>

## 89.29 `CONFIG_ETH_WIZNET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

构建中包含了一个 WIZnet 独立以太网控制器（Stand-Alone Ethernet Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_ETH_W5100S
CONFIG_ETH_W5500
CONFIG_ETH_W6100
CONFIG_ETH_W6300
```

**定义位置（Location）**：[`drivers/ethernet/wiznet/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/wiznet/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_W5100S`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W5100S)、[`CONFIG_ETH_W5500`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W5500)、[`CONFIG_ETH_W6100`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W6100)、[`CONFIG_ETH_W6300`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W6300)。

<a id="CONFIG_ETH_WIZNET_CORE"></a>

## 89.30 `CONFIG_ETH_WIZNET_CORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

WIZnet 独立以太网控制器共用的 MACRAW 核心（Shared MACRAW Core）。W6300 自带相应实现，因此不使用此共享核心。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_WIZNET && CONFIG_ETH_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_ETH_W5100S
CONFIG_ETH_W5500
CONFIG_ETH_W6100
```

**定义位置（Location）**：[`drivers/ethernet/wiznet/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/wiznet/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_WIZNET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WIZNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_W5100S`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W5100S)、[`CONFIG_ETH_W5500`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W5500)、[`CONFIG_ETH_W6100`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W6100)。

<a id="CONFIG_ETH_WIZNET_MONITOR_PERIOD"></a>

## 89.31 `CONFIG_ETH_WIZNET_MONITOR_PERIOD`

**提示（Prompt）**：监控任务执行周期（Monitor Task Execution Period）

**说明（Help）**

监控任务（Monitor Task）的执行周期，以毫秒为单位。该任务定期运行，用于检测链路状态（Link Status）的变化，并将变化报告给操作系统（Operating System）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_WIZNET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/ethernet/wiznet/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/wiznet/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_WIZNET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WIZNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_WIZNET_POLL_PERIOD"></a>

## 89.32 `CONFIG_ETH_WIZNET_POLL_PERIOD`

**提示（Prompt）**：轮询周期（Polling Period），以毫秒为单位

**说明（Help）**

以轮询模式（Polling Mode）运行时，检查接收数据（RX Data）和链路状态（Link Status）的间隔，以毫秒为单位。此模式适用于设备树（Devicetree）中未定义 `int-gpios` 的情况。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_WIZNET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/ethernet/wiznet/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/wiznet/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_WIZNET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WIZNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_WIZNET_RX_THREAD_PRIO"></a>

## 89.33 `CONFIG_ETH_WIZNET_RX_THREAD_PRIO`

**提示（Prompt）**：内部传入数据包处理线程（Incoming Packet Handler）的优先级

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_WIZNET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/wiznet/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/wiznet/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_WIZNET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WIZNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_WIZNET_RX_THREAD_STACK_SIZE"></a>

## 89.34 `CONFIG_ETH_WIZNET_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：内部传入数据包处理线程的栈大小（Stack Size）

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程所用的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_WIZNET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/ethernet/wiznet/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/wiznet/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_WIZNET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WIZNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_WIZNET_TIMEOUT"></a>

## 89.35 `CONFIG_ETH_WIZNET_TIMEOUT`

**提示（Prompt）**：IP 缓冲区超时时间（IP Buffer Timeout）

**说明（Help）**

给定超时时间，以毫秒为单位。驱动等待从 IP 协议栈（IP Stack）获得内存缓冲区的最长时间，超过后丢弃以太网帧（Ethernet Frame）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_WIZNET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/ethernet/wiznet/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/wiznet/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_WIZNET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WIZNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_XGMAC_MAX_QUEUES"></a>

## 89.36 `CONFIG_ETH_XGMAC_MAX_QUEUES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

XGMAC IP 支持的硬件队列数量（Hardware Queue Count）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DWC_XGMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/ethernet/dwc_xgmac/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → DWC XGMAC 配置（Configuration） → Synopsys DesignWareCore XGMAC 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_XGMAC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_XILINX_AXIENET"></a>

## 89.37 `CONFIG_ETH_XILINX_AXIENET`

**提示（Prompt）**：Xilinx AXI 以太网驱动（Ethernet Driver）

**说明（Help）**

启用 Xilinx 1G / 2.5G AXI 以太网（Ethernet）驱动，此类硬件常见于 FPGA。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_AXI_ETHERNET_1_00_A_ENABLED && CONFIG_DMA_XILINX_AXI_DMA && CONFIG_NET_BUF_FIXED_DATA_SIZE && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.xilinx_axienet:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.xilinx_axienet#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DMA_XILINX_AXI_DMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XILINX_AXI_DMA)、[`CONFIG_NET_BUF_FIXED_DATA_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF_FIXED_DATA_SIZE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)。

<a id="CONFIG_ETH_XILINX_AXIENET_BUFFER_NUM_RX"></a>

## 89.38 `CONFIG_ETH_XILINX_AXIENET_BUFFER_NUM_RX`

**提示（Prompt）**：用于并发接收（Concurrent Reception，RX）的缓冲区数量。

**说明（Help）**

Xilinx AXI 以太网驱动为接收分配的缓冲区（Buffer）数量。它限制同时在途的传输（In-Flight Transmission）数量，不得超过 AXI DMA 中可用的接收缓冲区（RX Buffer）数量。不过，如果系统有多个 AXI DMA 用于不同用途，可能需要减少并发传输数量以节约资源。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_XILINX_AXIENET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_DMA_XILINX_AXI_DMA_SG_DESCRIPTOR_NUM_RX
```

**取值范围（Ranges）**

```text
[2, CONFIG_DMA_XILINX_AXI_DMA_SG_DESCRIPTOR_NUM_RX]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.xilinx_axienet:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.xilinx_axienet#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Xilinx AXI 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_XILINX_AXIENET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XILINX_AXIENET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_DMA_XILINX_AXI_DMA_SG_DESCRIPTOR_NUM_RX`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XILINX_AXI_DMA_SG_DESCRIPTOR_NUM_RX)。

<a id="CONFIG_ETH_XILINX_AXIENET_BUFFER_NUM_TX"></a>

## 89.39 `CONFIG_ETH_XILINX_AXIENET_BUFFER_NUM_TX`

**提示（Prompt）**：用于并发发送（Concurrent Transmission，TX）的缓冲区数量。

**说明（Help）**

Xilinx AXI 以太网驱动为发送分配的缓冲区（Buffer）数量。它限制同时在途的传输（In-Flight Transmission）数量，不得超过 AXI DMA 中可用的发送缓冲区（TX Buffer）数量。不过，如果系统有多个 AXI DMA 用于不同用途，可能需要减少并发传输数量以节约资源。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_XILINX_AXIENET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_DMA_XILINX_AXI_DMA_SG_DESCRIPTOR_NUM_TX
```

**取值范围（Ranges）**

```text
[2, CONFIG_DMA_XILINX_AXI_DMA_SG_DESCRIPTOR_NUM_TX]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.xilinx_axienet:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.xilinx_axienet#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Xilinx AXI 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_XILINX_AXIENET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XILINX_AXIENET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_DMA_XILINX_AXI_DMA_SG_DESCRIPTOR_NUM_TX`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XILINX_AXI_DMA_SG_DESCRIPTOR_NUM_TX)。

<a id="CONFIG_ETH_XILINX_AXI_ETHERNET_LITE"></a>

## 89.40 `CONFIG_ETH_XILINX_AXI_ETHERNET_LITE`

**提示（Prompt）**：Xilinx AXI Ethernet Lite 驱动

**说明（Help）**

启用 Xilinx AXI Ethernet Lite MAC 驱动，此类硬件常见于 Xilinx FPGA 和 SoC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_XLNX_XPS_ETHERNETLITE_3_00_A_MAC_ENABLED || DT_HAS_XLNX_XPS_ETHERNETLITE_1_00_A_MAC_ENABLED) && CONFIG_LITTLE_ENDIAN && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.xilinx_axi_ethernet_lite:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.xilinx_axi_ethernet_lite#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LITTLE_ENDIAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LITTLE_ENDIAN)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LITTLE_ENDIAN`。

<a id="CONFIG_ETH_XILINX_AXI_ETHERNET_LITE_TIMER_PERIOD"></a>

## 89.41 `CONFIG_ETH_XILINX_AXI_ETHERNET_LITE_TIMER_PERIOD`

**提示（Prompt）**：Xilinx AXI Ethernet Lite 定时器周期（Timer Period），以毫秒为单位

**说明（Help）**

AXI Ethernet Lite 中周期性接收定时任务（Periodic RX Timer Task）的周期。在完全没有可用中断请求（IRQ），或者中断控制器不能可靠处理中断的情况下有用。设为 `0` 可禁用此功能。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_XILINX_AXI_ETHERNET_LITE && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.xilinx_axi_ethernet_lite:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.xilinx_axi_ethernet_lite#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Xilinx AXI Ethernet Lite 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_XILINX_AXI_ETHERNET_LITE`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XILINX_AXI_ETHERNET_LITE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_XLNX_GEM"></a>

## 89.42 `CONFIG_ETH_XLNX_GEM`

**提示（Prompt）**：Xilinx GEM 以太网驱动（Ethernet Driver）

**说明（Help）**

启用 Xilinx GEM 以太网（Ethernet）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_GEM_ENABLED && (!CONFIG_QEMU_TARGET || (CONFIG_QEMU_TARGET && CONFIG_NET_QEMU_ETHERNET)) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_CACHE_MANAGEMENT if CONFIG_DCACHE
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
CONFIG_ETH_NIC_MODEL_ONBOARD
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.xlnx_gem:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.xlnx_gem#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_TARGET)、[`CONFIG_NET_QEMU_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QEMU_ETHERNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_ETH_NIC_MODEL_ONBOARD`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NIC_MODEL_ONBOARD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_XMC4XXX"></a>

## 89.43 `CONFIG_ETH_XMC4XXX`

**提示（Prompt）**：XMC4XXX 以太网驱动（Ethernet Driver）

**说明（Help）**

启用 XMC4XXX 以太网（Ethernet）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_ETHERNET_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.xmc4xxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.xmc4xxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)。

<a id="CONFIG_ETH_XMC4XXX_NUM_RX_DMA_DESCRIPTORS"></a>

## 89.44 `CONFIG_ETH_XMC4XXX_NUM_RX_DMA_DESCRIPTORS`

**提示（Prompt）**：接收 DMA 描述符数量（RX DMA Descriptor Count）

**说明（Help）**

接收 DMA 描述符（RX DMA Descriptor）的数量。每个描述符存储一个数据分片（Data Fragment）的内存地址和大小。数据分片从接收网络缓冲区（`CONFIG_NET_BUF_RX_COUNT`）预先分配。收到帧时，无需复制数据即可将其转发到网络协议栈（Network Stack）；描述符中的缓冲区随后替换为新预先分配的缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_XMC4XXX && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
12
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.xmc4xxx:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.xmc4xxx#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → XMC4XXX 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_XMC4XXX`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XMC4XXX)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_XMC4XXX_NUM_TX_DMA_DESCRIPTORS"></a>

## 89.45 `CONFIG_ETH_XMC4XXX_NUM_TX_DMA_DESCRIPTORS`

**提示（Prompt）**：发送 DMA 描述符数量（TX DMA Descriptor Count）

**说明（Help）**

发送 DMA 描述符（TX DMA Descriptor）的数量。每个描述符存储一个数据分片（Data Fragment）的内存地址和大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_XMC4XXX && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.xmc4xxx:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.xmc4xxx#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → XMC4XXX 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_XMC4XXX`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XMC4XXX)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_XMC4XXX_TX_FRAME_POOL_SIZE"></a>

## 89.46 `CONFIG_ETH_XMC4XXX_TX_FRAME_POOL_SIZE`

**提示（Prompt）**：池中的发送帧数量（TX Frame Count in Pool）

**说明（Help）**

驱动中可以缓冲的发送帧（TX Frame）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_XMC4XXX && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.xmc4xxx:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.xmc4xxx#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → XMC4XXX 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_XMC4XXX`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XMC4XXX)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_XMC4XXX_VLAN_HW_FILTER"></a>

## 89.47 `CONFIG_ETH_XMC4XXX_VLAN_HW_FILTER`

**提示（Prompt）**：通过硬件过滤虚拟局域网帧（Hardware Filter VLAN Frames）

**说明（Help）**

在硬件中执行虚拟局域网帧过滤（VLAN Frame Filtering）。仅接收标签已通过 `vlan_setup()` 调用配置的以太网帧。只能针对一个 VLAN 标签过滤；如果多次调用 `vlan_setup()`，则使用最后配置的标签进行过滤。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_VLAN && CONFIG_ETH_XMC4XXX && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_NET_VLAN_COUNT = 1
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.xmc4xxx:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.xmc4xxx#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → XMC4XXX 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_NET_VLAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_VLAN)、[`CONFIG_ETH_XMC4XXX`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XMC4XXX)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_VLAN_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_VLAN_COUNT)。

<a id="CONFIG_ETH_XMC_DWC_ETHER_1000"></a>

## 89.48 `CONFIG_ETH_XMC_DWC_ETHER_1000`

**提示（Prompt）**：用于基于 DWC 以太网 MAC 的 XMC4XXX 的驱动

**说明（Help）**

为 XMC4XXX SoC 启用 Synopsys DesignWare MAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ETH_XMC4XXX && CONFIG_SOC_FAMILY_INFINEON_XMC && DT_HAS_INFINEON_XMC4XXX_ETHERNET_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_DWC_ETHER_1000_CORE
CONFIG_PINCTRL
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_XMC4XXX`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XMC4XXX)、[`CONFIG_SOC_FAMILY_INFINEON_XMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_XMC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_XMC`。

<a id="CONFIG_MDIO"></a>

## 89.49 `CONFIG_MDIO`

**提示（Prompt）**：管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**说明（Help）**

启用 MDIO 驱动配置（Driver Configuration）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ETH_SMSC91X
CONFIG_PHY_TJA11XX
CONFIG_PHY_TJA1103
CONFIG_PHY_DM8806
CONFIG_PHY_MICROCHIP_T1S
CONFIG_PHY_GENERIC_MII
CONFIG_PHY_ADIN1140
CONFIG_PHY_ADIN2111
CONFIG_PHY_MICROCHIP_KSZ8081
CONFIG_PHY_MICROCHIP_KSZ9131
CONFIG_PHY_MICROCHIP_LAN8742
CONFIG_PHY_MICROCHIP_VSC8541
CONFIG_PHY_TI_DP83825
CONFIG_PHY_TI_DP83867
CONFIG_PHY_REALTEK_RTL8211F
CONFIG_PHY_QUALCOMM_AR8031
CONFIG_PHY_MAXLINEAR_GPY111
CONFIG_PHY_MOTORCOMM_YT8521
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_SMSC91X`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_SMSC91X)、[`CONFIG_PHY_TJA11XX`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_TJA11XX)、[`CONFIG_PHY_TJA1103`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_TJA1103)、[`CONFIG_PHY_DM8806`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806)、[`CONFIG_PHY_MICROCHIP_T1S`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_MICROCHIP_T1S)、[`CONFIG_PHY_GENERIC_MII`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_GENERIC_MII)、[`CONFIG_PHY_ADIN1140`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_ADIN1140)、[`CONFIG_PHY_ADIN2111`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_ADIN2111)、[`CONFIG_PHY_MICROCHIP_KSZ8081`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_MICROCHIP_KSZ8081)、[`CONFIG_PHY_MICROCHIP_KSZ9131`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_MICROCHIP_KSZ9131)、[`CONFIG_PHY_MICROCHIP_LAN8742`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_MICROCHIP_LAN8742)、[`CONFIG_PHY_MICROCHIP_VSC8541`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_MICROCHIP_VSC8541)、[`CONFIG_PHY_TI_DP83825`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_TI_DP83825)、[`CONFIG_PHY_TI_DP83867`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_TI_DP83867)、[`CONFIG_PHY_REALTEK_RTL8211F`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_REALTEK_RTL8211F)、[`CONFIG_PHY_QUALCOMM_AR8031`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_QUALCOMM_AR8031)、[`CONFIG_PHY_MAXLINEAR_GPY111`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_MAXLINEAR_GPY111)、[`CONFIG_PHY_MOTORCOMM_YT8521`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_MOTORCOMM_YT8521)。

<a id="CONFIG_MDIO_ADIN1140"></a>

## 89.50 `CONFIG_MDIO_ADIN1140`

**提示（Prompt）**：ADIN1140 MDIO 驱动

**说明（Help）**

启用 ADIN1140 MDIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADIN1140_MDIO_ENABLED && CONFIG_ETH_ADIN1140 && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.adin1140:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.adin1140#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_ADIN1140`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ADIN1140)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_ADIN2111"></a>

## 89.51 `CONFIG_MDIO_ADIN2111`

**提示（Prompt）**：ADIN2111 MDIO 驱动

**说明（Help）**

启用 ADIN2111 MDIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADIN2111_MDIO_ENABLED && CONFIG_ETH_ADIN2111 && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.adin2111:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.adin2111#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_ADIN2111`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ADIN2111)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_ATMEL_SAM"></a>

## 89.52 `CONFIG_MDIO_ATMEL_SAM`

**提示（Prompt）**：Atmel SAM MDIO 驱动

**说明（Help）**

启用 Atmel SAM 微控制器（MCU）系列的 MDIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_SAM_GMAC && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.sam:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.sam#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_SAM_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_SAM_GMAC)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_BCMGENET"></a>

## 89.53 `CONFIG_MDIO_BCMGENET`

**提示（Prompt）**：Broadcom GENET MDIO 驱动

**说明（Help）**

启用 Broadcom GENET MDIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_GENET_MDIO_ENABLED && CONFIG_ETH_BCMGENET && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.bcmgenet:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.bcmgenet#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_BCMGENET`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_BCMGENET)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_DWCXGMAC"></a>

## 89.54 `CONFIG_MDIO_DWCXGMAC`

**提示（Prompt）**：Synopsys MDIO 驱动

**说明（Help）**

启用 Synopsys DWC XGMAC MDIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DWC_XGMAC && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.dwcxgmac:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.dwcxgmac#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_XGMAC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_DWCXGMAC_STATUS_BUSY_CHECK_TIMEOUT"></a>

## 89.55 `CONFIG_MDIO_DWCXGMAC_STATUS_BUSY_CHECK_TIMEOUT`

**提示（Prompt）**：检查软件复位状态（Software Reset Status）的超时时间，以微秒为单位

**说明（Help）**

此选项指定 MDIO 初始化期间检查软件复位状态（Software Reset Status）的超时时间，以微秒（µs）为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDIO_DWCXGMAC && CONFIG_MDIO
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.dwcxgmac:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.dwcxgmac#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → Synopsys MDIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO_DWCXGMAC`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO_DWCXGMAC)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_DWMAC"></a>

## 89.56 `CONFIG_MDIO_DWMAC`

**提示（Prompt）**：Synopsys DesignWare MAC MDIO 驱动

**说明（Help）**

为将 MDIO 控制器作为 MAC 子节点（Child Node）公开的 Synopsys DesignWare MAC 设备启用 MDIO 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DWMAC_MDIO_ENABLED && (CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL if n
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.dwmac:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.dwmac#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MDIO_DWMAC_BUSY_CHECK_TIMEOUT"></a>

## 89.57 `CONFIG_MDIO_DWMAC_BUSY_CHECK_TIMEOUT`

**提示（Prompt）**：MDIO 忙等待超时（Busy-Wait Timeout），以微秒为单位

**说明（Help）**

等待 MDIO 事务（Transaction）完成时使用的超时时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDIO_DWMAC && CONFIG_MDIO
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.dwmac:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.dwmac#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → Synopsys DesignWare MAC MDIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO_DWMAC`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO_DWMAC)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_ESP32"></a>

## 89.58 `CONFIG_MDIO_ESP32`

**提示（Prompt）**：ESP32 MDIO 驱动

**说明（Help）**

启用 ESP32 微控制器（MCU）系列的 MDIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32P4) && DT_HAS_SNPS_DWMAC_MDIO_ENABLED && !CONFIG_MDIO_DWMAC && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_MDIO_DWMAC`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO_DWMAC)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_MDIO_GPIO"></a>

## 89.59 `CONFIG_MDIO_GPIO`

**提示（Prompt）**：GPIO 位模拟 MDIO 控制器驱动（Bitbang MDIO Controller Driver）

**说明（Help）**

启用通过 GPIO 引脚进行软件驱动（位模拟，Bit Banging）的 MDIO 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_MDIO_GPIO_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.gpio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.gpio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_INFINEON_XMC4XXX"></a>

## 89.60 `CONFIG_MDIO_INFINEON_XMC4XXX`

**提示（Prompt）**：Infineon XMC4XXX MDIO 驱动

**说明（Help）**

启用英飞凌（Infineon）XMC4XXX MDIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_XMC4XXX && DT_HAS_SNPS_DWMAC_MDIO_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.xmc4xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.xmc4xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_XMC4XXX`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XMC4XXX)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MDIO_INIT_PRIORITY"></a>

## 89.61 `CONFIG_MDIO_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

MDIO 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDIO
```

**默认值（Defaults）**

```text
CONFIG_ETH_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_ETH_INIT_PRIORITY`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_INIT_PRIORITY)。

<a id="CONFIG_MDIO_INTEL_BUSY_CHECK_TIMEOUT"></a>

## 89.62 `CONFIG_MDIO_INTEL_BUSY_CHECK_TIMEOUT`

**提示（Prompt）**：`MDIO_INTEL_IGC` 忙等待超时（Busy-Wait Timeout）

**说明（Help）**

此超时时间以微秒为单位，指定等待 MDIO 读或写周期（Read or Write Cycle）完成的时长。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDIO_INTEL_IGC && CONFIG_MDIO
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.intel_igc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.intel_igc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → Intel IGC MDIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO_INTEL_IGC`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO_INTEL_IGC)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_INTEL_IGC"></a>

## 89.63 `CONFIG_MDIO_INTEL_IGC`

**提示（Prompt）**：Intel IGC MDIO 驱动

**说明（Help）**

启用 Intel IGC MDIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_IGC_MDIO_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.intel_igc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.intel_igc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_LAN865X"></a>

## 89.64 `CONFIG_MDIO_LAN865X`

**提示（Prompt）**：LAN865X MDIO 驱动

**说明（Help）**

启用 LAN865X MDIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_LAN865X_MDIO_ENABLED && CONFIG_ETH_LAN865X && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.lan865x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.lan865x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_LAN865X`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_LAN865X)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_LITEX_LITEETH"></a>

## 89.65 `CONFIG_MDIO_LITEX_LITEETH`

**提示（Prompt）**：LiteX LiteEth MDIO 控制器驱动（Controller Driver）

**说明（Help）**

启用 LiteX LiteEth 控制器提供的 MDIO 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_LITEETH_MDIO_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.litex:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.litex#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_MCHP_GMAC_G1"></a>

## 89.66 `CONFIG_MDIO_MCHP_GMAC_G1`

**提示（Prompt）**：Microchip MDIO 驱动

**说明（Help）**

启用 Microchip 微控制器（MCU）系列的 MDIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_GMAC_G1_MDIO_ENABLED && CONFIG_ETH_MCHP_GMAC_G1 && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_MCHP_GMAC_G1`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_MCHP_GMAC_G1)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_NXP_ENET"></a>

## 89.67 `CONFIG_MDIO_NXP_ENET`

**提示（Prompt）**：NXP ENET MDIO 驱动

**说明（Help）**

启用 NXP ENET MDIO 驱动。如果与 ENET 配合使用的全部以太网物理层器件（PHY）都不通过 MDIO 总线管理，可手动禁用此 Kconfig 选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_ENET_MDIO_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.nxp_enet:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.nxp_enet#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MDIO_NXP_ENET_QOS"></a>

## 89.68 `CONFIG_MDIO_NXP_ENET_QOS`

**提示（Prompt）**：NXP ENET QoS MDIO 驱动

**说明（Help）**

启用 NXP ENET 服务质量（Quality of Service，QoS）MDIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET_QOS && DT_HAS_SNPS_DWMAC_MDIO_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.nxp_enet_qos:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.nxp_enet_qos#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET_QOS)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_NXP_ENET_QOS_RECHECK_COUNT"></a>

## 89.69 `CONFIG_MDIO_NXP_ENET_QOS_RECHECK_COUNT`

**提示（Prompt）**：重新检查 MDIO 事务状态的次数（Transaction Status Recheck Count）

**说明（Help）**

超时之前，驱动应重新检查 MDIO 总线事务状态（Transaction Status）的次数。超时时间为：

```text
CONFIG_MDIO_NXP_ENET_QOS_RECHECK_TIME * CONFIG_MDIO_NXP_ENET_QOS_RECHECK_COUNT
```

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDIO_NXP_ENET_QOS && CONFIG_MDIO
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.nxp_enet_qos:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.nxp_enet_qos#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → NXP ENET QoS MDIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO_NXP_ENET_QOS`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO_NXP_ENET_QOS)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_NXP_ENET_QOS_RECHECK_TIME"></a>

## 89.70 `CONFIG_MDIO_NXP_ENET_QOS_RECHECK_TIME`

**提示（Prompt）**：事务状态检查间隔（Transaction Status Recheck Interval），以微秒为单位

**说明（Help）**

驱动在两次 MDIO 事务状态（Transaction Status）检查之间忙等待（Busy Wait）的时长，以微秒为单位。超时时间为：

```text
CONFIG_MDIO_NXP_ENET_QOS_RECHECK_TIME * CONFIG_MDIO_NXP_ENET_QOS_RECHECK_COUNT
```

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDIO_NXP_ENET_QOS && CONFIG_MDIO
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.nxp_enet_qos:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.nxp_enet_qos#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → NXP ENET QoS MDIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO_NXP_ENET_QOS`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO_NXP_ENET_QOS)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_NXP_ENET_TIMEOUT"></a>

## 89.71 `CONFIG_MDIO_NXP_ENET_TIMEOUT`

**提示（Prompt）**：NXP ENET MDIO 超时时间（Timeout Time）

**说明（Help）**

将尚未完成的 MDIO 事务（Transaction）判定为超时之前允许经过的时间，以微秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDIO_NXP_ENET && CONFIG_MDIO
```

**默认值（Defaults）**

```text
250
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.nxp_enet:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.nxp_enet#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → NXP ENET MDIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO_NXP_ENET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO_NXP_ENET)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_NXP_IMX_NETC"></a>

## 89.72 `CONFIG_MDIO_NXP_IMX_NETC`

**提示（Prompt）**：NXP i.MX NETC 外部 MDIO 驱动（External MDIO Driver）

**说明（Help）**

为 NXP i.MX SoC 启用 NETC 外部 MDIO 控制器驱动（External MDIO Controller Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_NETC_EMDIO_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.nxp_imx_netc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.nxp_imx_netc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_NXP_S32_GMAC"></a>

## 89.73 `CONFIG_MDIO_NXP_S32_GMAC`

**提示（Prompt）**：NXP S32 GMAC MDIO 驱动

**说明（Help）**

为 NXP S32 SoC 启用 GMAC MDIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_GMAC && DT_HAS_SNPS_DWMAC_MDIO_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.nxp_s32_gmac:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.nxp_s32_gmac#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_MDIO_NXP_S32_NETC"></a>

## 89.74 `CONFIG_MDIO_NXP_S32_NETC`

**提示（Prompt）**：NXP S32 NETC 外部 MDIO 驱动（External MDIO Driver）

**说明（Help）**

为 NXP S32 SoC 启用 NETC 外部 MDIO 控制器驱动（External MDIO Controller Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_NETC_EMDIO_ENABLED && CONFIG_ETH_NXP_S32_NETC && DT_HAS_NXP_S32_NETC_PSI_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.nxp_s32_netc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.nxp_s32_netc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_MDIO_NXP_S32_TIMEOUT"></a>

## 89.75 `CONFIG_MDIO_NXP_S32_TIMEOUT`

**提示（Prompt）**：读写操作超时（Read/Write Operation Timeout），以毫秒为单位

**说明（Help）**

通过 MDIO 执行读写操作（Read/Write Operation）的超时时间，以毫秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDIO_NXP_S32_GMAC && CONFIG_MDIO
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.nxp_s32_gmac:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.nxp_s32_gmac#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → NXP S32 GMAC MDIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO_NXP_S32_GMAC`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO_NXP_S32_GMAC)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_RENESAS_RA"></a>

## 89.76 `CONFIG_MDIO_RENESAS_RA`

**提示（Prompt）**：瑞萨（RENESAS）MDIO 控制器驱动（Controller Driver）

**说明（Help）**

启用瑞萨（RENESAS）MDIO 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_MDIO_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_USE_RA_FSP_ETHER_PHY
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_USE_RA_FSP_ETHER_PHY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_ETHER_PHY)。

<a id="CONFIG_MDIO_RENESAS_RA_RMAC"></a>

## 89.77 `CONFIG_MDIO_RENESAS_RA_RMAC`

**提示（Prompt）**：瑞萨（RENESAS）MDIO RMAC 控制器驱动（Controller Driver）

**说明（Help）**

启用瑞萨（RENESAS）MDIO RMAC 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_MDIO_RMAC_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.renesas_ra:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.renesas_ra#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MDIO_SENSRY_SY1XX"></a>

## 89.78 `CONFIG_MDIO_SENSRY_SY1XX`

**提示（Prompt）**：Sensry SY1XX MDIO 驱动

**说明（Help）**

启用 Sensry SY1xx SoC 系列的 MDIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSRY_SY1XX_MDIO_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.sy1xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.sy1xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MDIO_SHELL"></a>

## 89.79 `CONFIG_MDIO_SHELL`

**提示（Prompt）**：MDIO 命令行（Shell）

**说明（Help）**

启用 MDIO 命令行（Shell）。目前支持扫描（Scanning）和设备读写（Device Read/Write）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_MDIO
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_ST_STM32_HAL"></a>

## 89.80 `CONFIG_MDIO_ST_STM32_HAL`

**提示（Prompt）**：STM32 MDIO 控制器驱动（Controller Driver）

**说明（Help）**

启用 STM32 MDIO 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DWMAC_MDIO_ENABLED && CONFIG_ETH_STM32_HAL && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.stm32_hal:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.stm32_hal#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MDIO_WCH"></a>

## 89.81 `CONFIG_MDIO_WCH`

**提示（Prompt）**：沁恒（WCH）MDIO 控制器驱动（Controller Driver）

**说明（Help）**

启用沁恒（WCH）MDIO 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_CH32V && DT_HAS_SNPS_DWMAC_MDIO_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.wch:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.wch#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_CH32V`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CH32V)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_CH32V`。

<a id="CONFIG_MDIO_XILINX_AXI_ENET"></a>

## 89.82 `CONFIG_MDIO_XILINX_AXI_ENET`

**提示（Prompt）**：Xilinx AXI Ethernet MDIO 驱动

**说明（Help）**

启用 Xilinx AXI Ethernet MDIO 总线驱动（Bus Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_AXI_ETHERNET_1_00_A_MDIO_ENABLED && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.xilinx_axienet:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.xilinx_axienet#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_XILINX_AXI_ETHERNET_LITE"></a>

## 89.83 `CONFIG_MDIO_XILINX_AXI_ETHERNET_LITE`

**提示（Prompt）**：Xilinx AXI Ethernet Lite MDIO 驱动

**说明（Help）**

启用 Xilinx AXI Ethernet Lite MDIO 总线驱动（Bus Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_XLNX_XPS_ETHERNETLITE_3_00_A_MDIO_ENABLED || DT_HAS_XLNX_XPS_ETHERNETLITE_1_00_A_MDIO_ENABLED) && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.xilinx_axi_ethernet_lite:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.xilinx_axi_ethernet_lite#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_XLNX_GEM"></a>

## 89.84 `CONFIG_MDIO_XLNX_GEM`

**提示（Prompt）**：Xilinx GEM MDIO 控制器驱动（Controller Driver）

**说明（Help）**

启用 Xilinx GEM MDIO 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_GEM_MDIO_ENABLED && CONFIG_ETH_XLNX_GEM && CONFIG_MDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.xlnx_gem:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.xlnx_gem#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_XLNX_GEM`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XLNX_GEM)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_MDIO_XLNX_GEM_IDLE_TIMEOUT_US"></a>

## 89.85 `CONFIG_MDIO_XLNX_GEM_IDLE_TIMEOUT_US`

**提示（Prompt）**：MDIO 空闲等待超时（Idle Wait Timeout）

**说明（Help）**

读或写操作之前或之后，等待 GEM MDIO 总线进入空闲状态（Idle）的超时时间，以微秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDIO_XLNX_GEM && CONFIG_MDIO
```

**默认值（Defaults）**

```text
1000000
```

**定义位置（Location）**：[`drivers/ethernet/mdio/Kconfig.xlnx_gem:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/Kconfig.xlnx_gem#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → Xilinx GEM MDIO 控制器驱动（Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_MDIO_XLNX_GEM`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO_XLNX_GEM)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_PHY_ADIN1140"></a>

## 89.86 `CONFIG_PHY_ADIN1140`

**提示（Prompt）**：ADIN1140 物理层（PHY）驱动

**说明（Help）**

启用 ADIN1140 物理层（PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADIN1140_PHY_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
CONFIG_ETH_PHY_API_PLCA
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_ETH_PHY_API_PLCA`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_API_PLCA)。

<a id="CONFIG_PHY_ADIN2111"></a>

## 89.87 `CONFIG_PHY_ADIN2111`

**提示（Prompt）**：ADIN2111 物理层（PHY）驱动

**说明（Help）**

启用 ADIN2111 物理层（PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ADI_ADIN2111_PHY_ENABLED || DT_HAS_ADI_ADIN1100_PHY_ENABLED) && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_PHY_AUTONEG_TIMEOUT_MS"></a>

## 89.88 `CONFIG_PHY_AUTONEG_TIMEOUT_MS`

**提示（Prompt）**：自动协商超时值（Auto-Negotiation Timeout），以毫秒为单位

**说明（Help）**

自动协商序列（Auto-Negotiation Sequence）在被判定为失败之前允许持续的最长时间，以毫秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
4000
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_PHY_DM8806"></a>

## 89.89 `CONFIG_PHY_DM8806`

**提示（Prompt）**：Davicom DM8806 物理层（PHY）驱动

**说明（Help）**

启用 Davicom DM8806 物理层（PHY）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_DAVICOM_DM8806_PHY_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.dm8806:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.dm8806#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_PHY_DM8806_ENERGY_EFFICIENT_MODE"></a>

## 89.90 `CONFIG_PHY_DM8806_ENERGY_EFFICIENT_MODE`

**提示（Prompt）**：节能模式（Energy Efficient Mode）

**说明（Help）**

DM8806 默认启用节能模式（Energy Efficient Mode）。曾观察到启用此模式时网络会随机失效，因此此配置符号默认禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PHY_DM8806 && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.dm8806:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.dm8806#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → Davicom DM8806 物理层（PHY）驱动

**配置项引用（Symbol References）**：[`CONFIG_PHY_DM8806`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806)、[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_PHY_DM8806_SMI_BUS_CHECK"></a>

## 89.91 `CONFIG_PHY_DM8806_SMI_BUS_CHECK`

**提示（Prompt）**：主机 SMI 总线错误检查功能（Bus Error Check）

**说明（Help）**

此功能用于防止板级噪声（Board-Level Noise）干扰主机 SMI 总线。写入过程中，原文描述为：“寄存器中写入的值会被应用，直到写入正确的校验和（Checksum）。”读取过程中，将硬件计算的校验和与软件计算的校验和比较，以检测所接收数据是否正确。

> 译注：写入部分原句使用 `will be applied until` 描述生效时序，措辞容易产生歧义；这里保留原句，没有将其自行改写为“校验通过后才生效”。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PHY_DM8806 && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.dm8806:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.dm8806#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → Davicom DM8806 物理层（PHY）驱动

**配置项引用（Symbol References）**：[`CONFIG_PHY_DM8806`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806)、[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_PHY_DM8806_SMI_BUS_CHECK_REPETITION"></a>

## 89.92 `CONFIG_PHY_DM8806_SMI_BUS_CHECK_REPETITION`

**提示（Prompt）**：SMI 总线传输重试次数（Transmission Repetitions）

**说明（Help）**

读取或写入期间循环冗余校验（CRC）失败时，重复 SMI 总线传输的次数。达到此次数后，读取消息被丢弃，不再传递给系统。写入过程的原文描述为：“寄存器中写入的值会被应用，直到将正确的校验和（Checksum）写入 PHY 寄存器。”

> 译注：此处原句也使用 `will be applied until`；保留其表述，不自行补入原文没有写出的生效时序保证。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PHY_DM8806_SMI_BUS_CHECK && CONFIG_PHY_DM8806 && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.dm8806:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.dm8806#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → Davicom DM8806 物理层（PHY）驱动 → 主机 SMI 总线错误检查功能（Bus Error Check）

**配置项引用（Symbol References）**：[`CONFIG_PHY_DM8806_SMI_BUS_CHECK`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806_SMI_BUS_CHECK)、[`CONFIG_PHY_DM8806`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806)、[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_PHY_DM8806_THREAD_PRIORITY"></a>

## 89.93 `CONFIG_PHY_DM8806_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PHY_DM8806_TRIGGER_GLOBAL_THREAD && CONFIG_PHY_DM8806 && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
13
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.dm8806:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.dm8806#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → Davicom DM8806 物理层（PHY）驱动

**配置项引用（Symbol References）**：[`CONFIG_PHY_DM8806_TRIGGER_GLOBAL_THREAD`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806_TRIGGER_GLOBAL_THREAD)、[`CONFIG_PHY_DM8806`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806)、[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_PHY_DM8806_THREAD_STACK_SIZE"></a>

## 89.94 `CONFIG_PHY_DM8806_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PHY_DM8806_TRIGGER_GLOBAL_THREAD && CONFIG_PHY_DM8806 && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.dm8806:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.dm8806#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → Davicom DM8806 物理层（PHY）驱动

**配置项引用（Symbol References）**：[`CONFIG_PHY_DM8806_TRIGGER_GLOBAL_THREAD`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806_TRIGGER_GLOBAL_THREAD)、[`CONFIG_PHY_DM8806`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806)、[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_PHY_DM8806_TRIGGER_GLOBAL_THREAD"></a>

## 89.95 `CONFIG_PHY_DM8806_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_PHY_DM8806_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_PHY_DM8806_TRIGGER
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.dm8806:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.dm8806#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → Davicom DM8806 物理层（PHY）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_PHY_DM8806_TRIGGER_MODE`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806_TRIGGER_MODE)、[`CONFIG_PHY_DM8806_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PHY_DM8806_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PHY_DM8806_TRIGGER`。

<a id="CONFIG_PHY_DM8806_TRIGGER_MODE"></a>

## 89.96 `CONFIG_PHY_DM8806_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PHY_DM8806 && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_PHY_DM8806_TRIGGER_GLOBAL_THREAD
```

**可选项（Choices）**

```text
CONFIG_PHY_DM8806_TRIGGER_NONE
CONFIG_PHY_DM8806_TRIGGER_GLOBAL_THREAD
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.dm8806:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.dm8806#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → Davicom DM8806 物理层（PHY）驱动

**配置项引用（Symbol References）**：[`CONFIG_PHY_DM8806`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806)、[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PHY_DM8806_TRIGGER_GLOBAL_THREAD`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806_TRIGGER_GLOBAL_THREAD)、[`CONFIG_PHY_DM8806_TRIGGER_NONE`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806_TRIGGER_NONE)。

<a id="CONFIG_PHY_DM8806_TRIGGER_NONE"></a>

## 89.97 `CONFIG_PHY_DM8806_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PHY_DM8806_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.dm8806:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.dm8806#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → Davicom DM8806 物理层（PHY）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_PHY_DM8806_TRIGGER_MODE`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_DM8806_TRIGGER_MODE)。

<a id="CONFIG_PHY_GENERIC_FIXED_LINK"></a>

## 89.98 `CONFIG_PHY_GENERIC_FIXED_LINK`

**提示（Prompt）**：具有固定链路的通用 MII PHY 驱动（Generic MII PHY with Fixed Link）

**说明（Help）**

这是具有固定链路（Fixed Link）的通用 MII PHY 接口，不通过 MDIO 总线与物理层器件（PHY）通信。当以太网驱动要求存在 PHY，但没有可用于配置 PHY 的接口时，可将它用作占位（Placeholder）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ETHERNET_PHY_FIXED_LINK_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_PHY_GENERIC_MII"></a>

## 89.99 `CONFIG_PHY_GENERIC_MII`

**提示（Prompt）**：通用 MII PHY 驱动（Generic MII PHY Driver）

**说明（Help）**

这是通过 MDIO 总线与物理层器件（PHY）通信的通用 MII PHY 接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ETHERNET_PHY_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_PHY_INIT_PRIORITY"></a>

## 89.100 `CONFIG_PHY_INIT_PRIORITY`

**提示（Prompt）**：以太网物理层驱动初始化优先级（Ethernet PHY Driver Init Priority）

**说明（Help）**

以太网物理层（PHY）设备驱动的初始化优先级（Initialization Priority）。除非了解修改的影响，否则不要更改此值。优先级数值必须小于网络协议栈（Network Stack）的对应数值，以便驱动在网络子系统之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_ETH_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_INIT_PRIORITY`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_INIT_PRIORITY)。

<!-- kconfig-navigation -->

[上一章](P088_drivers_ethernet_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P090_drivers_ethernet_配置项参考_4.md)
