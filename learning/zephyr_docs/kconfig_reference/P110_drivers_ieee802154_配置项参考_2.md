---
id: learning.zephyr-docs.kconfig-reference.page-110
title: "`drivers/ieee802154`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第110章\_`drivers/ieee802154`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `drivers/ieee802154` 的 41 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_IEEE802154_RAW_MODE"></a>

## 110.1 `CONFIG_IEEE802154_RAW_MODE`

**提示（Prompt）**：不带 MAC 协议栈（MAC Stack）的 IEEE 802.15.4 驱动

**说明（Help）**

此选项启用驱动的所谓原始（Raw）模式，即不使用 MAC 协议栈，也不会构建 802.15.4 的网络二层（L2）。仅用于 `wpan_serial` 和 `wpanusb` 示例等非常特定的场景。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_L2_PHY_IEEE802154 && CONFIG_IEEE802154
```

**主动选择（Selects）**

```text
CONFIG_NET_RAW_MODE
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PHY_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PHY_IEEE802154)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)。

<a id="CONFIG_IEEE802154_RDEV"></a>

## 110.2 `CONFIG_IEEE802154_RDEV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

物理层是具备测距能力的设备（Ranging-capable Device，RDEV）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_RF2XX"></a>

## 110.3 `CONFIG_IEEE802154_RF2XX`

**提示（Prompt）**：ATMEL RF2XX 驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_RF2XX_ENABLED && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.rf2xx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.rf2xx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_IEEE802154_RF2XX_INIT_PRIO"></a>

## 110.4 `CONFIG_IEEE802154_RF2XX_INIT_PRIO`

**提示（Prompt）**：RF2X 初始化优先级（Initialization Priority）

**说明（Help）**

设置初始化优先级数值。除非清楚其影响，否则不要随意更改。注意，RF2XX 要求 GPIO 和 SPI 先准备就绪，有时 GPIO 应最先初始化，因为 SPI 也可能需要它。当然，RF2XX 必须在网络协议栈之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_RF2XX && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.rf2xx:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.rf2xx#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ATMEL RF2XX 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_RF2XX`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_RF2XX)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_RF2XX_RX_STACK_SIZE"></a>

## 110.5 `CONFIG_IEEE802154_RF2XX_RX_STACK_SIZE`

**提示（Prompt）**：驱动内部接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

此选项设置驱动内部接收线程的栈大小。默认值应足够使用；如果实际过小，可通过此选项方便地调整。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_RF2XX && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
800
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.rf2xx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.rf2xx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ATMEL RF2XX 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_RF2XX`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_RF2XX)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_SELECTIVE_TXCHANNEL"></a>

## 110.6 `CONFIG_IEEE802154_SELECTIVE_TXCHANNEL`

**提示（Prompt）**：支持选择性设置发送信道（Selective TX Channel）

**说明（Help）**

启用对每个定时发送请求分别设置发送信道的支持。只有启用此 Kconfig 选项时，驱动才可以（MAY）具备 `IEEE802154_HW_SELECTIVE_TXCHANNEL` 能力。如果禁用此选项，驱动必须不（MUST NOT）具备该能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_SILABS_EFR32"></a>

## 110.7 `CONFIG_IEEE802154_SILABS_EFR32`

**提示（Prompt）**：Silabs EFR32 IEEE 802.15.4 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_EFR32_IEEE802154_ENABLED && (CONFIG_ZEPHYR_HAL_SILABS_MODULE_BLOBS || CONFIG_BUILD_ONLY_NO_BLOBS) && CONFIG_SOC_VENDOR_SILABS_HAS_RADIO && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SOC_GECKO_USE_RAIL
CONFIG_PSA_CRYPTO
CONFIG_SILABS_SISDK_PROTOCOL_CRYPTO
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.silabs_efr32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.silabs_efr32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_SILABS_MODULE_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_SILABS_MODULE_BLOBS)、[`CONFIG_BUILD_ONLY_NO_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_ONLY_NO_BLOBS)、[`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VENDOR_SILABS_HAS_RADIO)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_SOC_GECKO_USE_RAIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GECKO_USE_RAIL)、[`CONFIG_PSA_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)、[`CONFIG_SILABS_SISDK_PROTOCOL_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_PROTOCOL_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_SILABS_MODULE_BLOBS`、`CONFIG_SILABS_SISDK_PROTOCOL_CRYPTO`。

<a id="CONFIG_IEEE802154_SILABS_EFR32_BG_RX_PRIORITY"></a>

## 110.8 `CONFIG_IEEE802154_SILABS_EFR32_BG_RX_PRIORITY`

**提示（Prompt）**：后台接收调度器优先级（Background RX Scheduler Priority）

**说明（Help）**

EFR32 802.15.4 后台接收调度时隙使用的优先级。后台接收是设备未发送时的被动接收状态。在 RAIL 多协议调度器（Multiprotocol Scheduler）中，数值越大，优先级越低，因此默认值 255 使后台接收成为优先级最低的活动。仅与多协议构建相关，例如 BLE 与 802.15.4 并行运行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_SILABS_EFR32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.silabs_efr32:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.silabs_efr32#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Silabs EFR32 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_SILABS_EFR32`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_SILABS_EFR32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_SILABS_EFR32_INIT_PRIO"></a>

## 110.9 `CONFIG_IEEE802154_SILABS_EFR32_INIT_PRIO`

**提示（Prompt）**：Silabs EFR32 IEEE 802.15.4 初始化优先级

**说明（Help）**

设置初始化优先级（Initialization Priority）数值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_SILABS_EFR32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.silabs_efr32:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.silabs_efr32#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Silabs EFR32 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_SILABS_EFR32`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_SILABS_EFR32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_SILABS_EFR32_SRC_MATCH_EXT_MAX"></a>

## 110.10 `CONFIG_IEEE802154_SILABS_EFR32_SRC_MATCH_EXT_MAX`

**提示（Prompt）**：源匹配扩展地址表大小（Source-match Extended-address Table Size）

**说明（Help）**

驱动的软件源匹配表中可跟踪的扩展地址最大数量。参见 `IEEE802154_SILABS_EFR32_SRC_MATCH_SHORT_MAX`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_SILABS_EFR32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
CONFIG_OPENTHREAD_MAX_CHILDREN if CONFIG_NET_L2_OPENTHREAD
16
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.silabs_efr32:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.silabs_efr32#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Silabs EFR32 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_SILABS_EFR32`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_SILABS_EFR32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_OPENTHREAD_MAX_CHILDREN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MAX_CHILDREN)、[`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)。

<a id="CONFIG_IEEE802154_SILABS_EFR32_SRC_MATCH_SHORT_MAX"></a>

## 110.11 `CONFIG_IEEE802154_SILABS_EFR32_SRC_MATCH_SHORT_MAX`

**提示（Prompt）**：源匹配短地址表大小（Source-match Short-address Table Size）

**说明（Help）**

驱动的软件源匹配表中可跟踪的短地址最大数量，用于决定发出的确认帧（ACK）中的帧待处理（Frame Pending）位。在 OpenThread 构建中，默认值为 `OPENTHREAD_MAX_CHILDREN`，使路由器能够跟踪每个休眠子节点的 Frame Pending 状态。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_SILABS_EFR32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
CONFIG_OPENTHREAD_MAX_CHILDREN if CONFIG_NET_L2_OPENTHREAD
16
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.silabs_efr32:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.silabs_efr32#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Silabs EFR32 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_SILABS_EFR32`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_SILABS_EFR32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_OPENTHREAD_MAX_CHILDREN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MAX_CHILDREN)、[`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)。

<a id="CONFIG_IEEE802154_SILABS_EFR32_TX_PRIORITY_MIN"></a>

## 110.12 `CONFIG_IEEE802154_SILABS_EFR32_TX_PRIORITY_MIN`

**提示（Prompt）**：发送调度器优先级（TX Scheduler Priority，初始）

**说明（Help）**

在 RAIL 多协议调度器中，802.15.4 首次发送尝试所使用的优先级。数值越小，优先级越高。仅与多协议构建相关，例如 BLE 与 802.15.4 并行运行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_SILABS_EFR32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.silabs_efr32:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.silabs_efr32#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Silabs EFR32 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_SILABS_EFR32`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_SILABS_EFR32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_STM32WBA"></a>

## 110.13 `CONFIG_IEEE802154_STM32WBA`

**提示（Prompt）**：STM32WBA 系列 IEEE 802.15.4 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32WBA_IEEE802154_ENABLED && (CONFIG_ZEPHYR_HAL_STM32_MODULE_BLOBS || CONFIG_BUILD_ONLY_NO_BLOBS) && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.stm32wba:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.stm32wba#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_STM32_MODULE_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_STM32_MODULE_BLOBS)、[`CONFIG_BUILD_ONLY_NO_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_ONLY_NO_BLOBS)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_STM32_MODULE_BLOBS`。

<a id="CONFIG_IEEE802154_STM32WBA_CSMA_CA_ENABLED"></a>

## 110.14 `CONFIG_IEEE802154_STM32WBA_CSMA_CA_ENABLED`

**提示（Prompt）**：CSMA-CA 配置

**说明（Help）**

此选项启用载波侦听多路访问／冲突避免（CSMA-CA）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_STM32WBA && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.stm32wba:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.stm32wba#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → STM32WBA 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_STM32WBA`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_STM32WBA)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_STM32WBA_DELAY_TRX_ACC"></a>

## 110.15 `CONFIG_IEEE802154_STM32WBA_DELAY_TRX_ACC`

**提示（Prompt）**：延迟操作的时钟精度（Clock Accuracy）

**说明（Help）**

用于调度无线电延迟操作（延迟发送或延迟接收）的时钟精度，单位为百万分之一（ppm）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_STM32WBA && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.stm32wba:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.stm32wba#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → STM32WBA 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_STM32WBA`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_STM32WBA)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_STM32WBA_INIT_PRIO"></a>

## 110.16 `CONFIG_IEEE802154_STM32WBA_INIT_PRIO`

**提示（Prompt）**：STM32WBA IEEE 802.15.4 初始化优先级

**说明（Help）**

设置初始化优先级数值。除非清楚其影响，否则不要随意更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_STM32WBA && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.stm32wba:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.stm32wba#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → STM32WBA 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_STM32WBA`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_STM32WBA)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_STM32WBA_LOG_RX_FAILURES"></a>

## 110.17 `CONFIG_IEEE802154_STM32WBA_LOG_RX_FAILURES`

**提示（Prompt）**：帧接收失败日志（Frame Reception Failure Logging）

**说明（Help）**

某些情况下，内部原因可能导致帧接收失败。这些情况以通用错误码向上传递。此选项启用帧接收失败原因的日志记录，有助于分析网络流量，但在高压力环境中也会产生大量日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_STM32WBA && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.stm32wba:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.stm32wba#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → STM32WBA 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_STM32WBA`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_STM32WBA)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_STM32WBA_RX_BUFFERS"></a>

## 110.18 `CONFIG_IEEE802154_STM32WBA_RX_BUFFERS`

**提示（Prompt）**：STM32WBA 802.15.4 接收缓冲区（Receive Buffers）

**说明（Help）**

802.15.4 驱动序列化主机（Serialization Host）接收队列中的缓冲区数量。若预期处于噪声较多的环境、要处理许多终端设备，且有足够的 RAM 分配缓冲区，可增大此值。增大此值后，可能还需要更新 `IEEE802154_STM32WBA_RX_STACK_SIZE`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_STM32WBA && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[16, 128]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.stm32wba:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.stm32wba#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → STM32WBA 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_STM32WBA`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_STM32WBA)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_STM32WBA_RX_STACK_SIZE"></a>

## 110.19 `CONFIG_IEEE802154_STM32WBA_RX_STACK_SIZE`

**提示（Prompt）**：驱动接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

此选项设置驱动内部接收线程的栈大小。默认值应足够使用；如果实际过小，请按需调整。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_STM32WBA && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
800
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.stm32wba:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.stm32wba#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → STM32WBA 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_STM32WBA`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_STM32WBA)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_TELINK_B91"></a>

## 110.20 `CONFIG_IEEE802154_TELINK_B91`

**提示（Prompt）**：Telink B91 射频（RF）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TELINK_B91_ZB_ENABLED && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.b91:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.b91#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_UPIPE"></a>

## 110.21 `CONFIG_IEEE802154_UPIPE`

**提示（Prompt）**：用于 QEMU 的 UART PIPE 模拟无线电驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BOARD_QEMU_X86 || CONFIG_BOARD_QEMU_CORTEX_M3) && DT_HAS_ZEPHYR_IEEE802154_UART_PIPE_ENABLED && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UART_PIPE
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.uart_pipe:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.uart_pipe#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_BOARD_QEMU_X86`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_QEMU_X86)、[`CONFIG_BOARD_QEMU_CORTEX_M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_QEMU_CORTEX_M3)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_UART_PIPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_PIPE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_QEMU_X86`、`CONFIG_BOARD_QEMU_CORTEX_M3`。

<a id="CONFIG_IEEE802154_UPIPE_HW_FILTER"></a>

## 110.22 `CONFIG_IEEE802154_UPIPE_HW_FILTER`

**提示（Prompt）**：硬件过滤（Hardware Filtering）

**说明（Help）**

此选项保证驱动只处理发给自己的帧。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_UPIPE && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.uart_pipe:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.uart_pipe#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → 用于 QEMU 的 UART PIPE 模拟无线电驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_UPIPE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_UPIPE)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_UPIPE_MAC4"></a>

## 110.23 `CONFIG_IEEE802154_UPIPE_MAC4`

**提示（Prompt）**：MAC 地址第 4 字节（Byte 4）

**说明（Help）**

这是介质访问控制（MAC）地址的第 4 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_UPIPE_RANDOM_MAC && CONFIG_IEEE802154_UPIPE && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.uart_pipe:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.uart_pipe#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → 用于 QEMU 的 UART PIPE 模拟无线电驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_UPIPE_RANDOM_MAC`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_UPIPE_RANDOM_MAC)、[`CONFIG_IEEE802154_UPIPE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_UPIPE)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_UPIPE_MAC5"></a>

## 110.24 `CONFIG_IEEE802154_UPIPE_MAC5`

**提示（Prompt）**：MAC 地址第 5 字节（Byte 5）

**说明（Help）**

这是介质访问控制（MAC）地址的第 5 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_UPIPE_RANDOM_MAC && CONFIG_IEEE802154_UPIPE && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.uart_pipe:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.uart_pipe#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → 用于 QEMU 的 UART PIPE 模拟无线电驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_UPIPE_RANDOM_MAC`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_UPIPE_RANDOM_MAC)、[`CONFIG_IEEE802154_UPIPE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_UPIPE)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_UPIPE_MAC6"></a>

## 110.25 `CONFIG_IEEE802154_UPIPE_MAC6`

**提示（Prompt）**：MAC 地址第 6 字节（Byte 6）

**说明（Help）**

这是介质访问控制（MAC）地址的第 6 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_UPIPE_RANDOM_MAC && CONFIG_IEEE802154_UPIPE && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.uart_pipe:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.uart_pipe#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → 用于 QEMU 的 UART PIPE 模拟无线电驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_UPIPE_RANDOM_MAC`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_UPIPE_RANDOM_MAC)、[`CONFIG_IEEE802154_UPIPE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_UPIPE)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_UPIPE_MAC7"></a>

## 110.26 `CONFIG_IEEE802154_UPIPE_MAC7`

**提示（Prompt）**：MAC 地址第 7 字节（Byte 7）

**说明（Help）**

这是介质访问控制（MAC）地址的第 7 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_UPIPE_RANDOM_MAC && CONFIG_IEEE802154_UPIPE && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.uart_pipe:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.uart_pipe#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → 用于 QEMU 的 UART PIPE 模拟无线电驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_UPIPE_RANDOM_MAC`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_UPIPE_RANDOM_MAC)、[`CONFIG_IEEE802154_UPIPE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_UPIPE)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_UPIPE_RANDOM_MAC"></a>

## 110.27 `CONFIG_IEEE802154_UPIPE_RANDOM_MAC`

**提示（Prompt）**：随机 MAC 地址（Random MAC Address）

**说明（Help）**

动态生成随机 MAC 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_UPIPE && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.uart_pipe:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.uart_pipe#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → 用于 QEMU 的 UART PIPE 模拟无线电驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_UPIPE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_UPIPE)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_VENDOR_OUI"></a>

## 110.28 `CONFIG_IEEE802154_VENDOR_OUI`

**提示（Prompt）**：厂商组织唯一标识符（Organizationally Unique Identifier，OUI）

**说明（Help）**

自定义厂商 OUI，构成 MAC 地址的最高 24 位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_VENDOR_OUI_ENABLE && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → 支持设置厂商组织唯一标识符（OUI）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_VENDOR_OUI_ENABLE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_VENDOR_OUI_ENABLE)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_VENDOR_OUI_ENABLE"></a>

## 110.29 `CONFIG_IEEE802154_VENDOR_OUI_ENABLE`

**提示（Prompt）**：支持设置厂商组织唯一标识符（OUI）

**说明（Help）**

此选项启用通过 `IEEE802154_VENDOR_OUI` 设置自定义厂商 OUI。启用后，用户必须设置 `IEEE802154_VENDOR_OUI`，因为它没有默认值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_KW41_DBG_TRACE"></a>

## 110.30 `CONFIG_KW41_DBG_TRACE`

**提示（Prompt）**：简化的事件调试跟踪（Debug Tracing）

**说明（Help）**

此值取决于调试需求。它生成经过编码的事件跟踪记录，而不进入调试日志路径，以避免影响运行代码的时序。之后通过调试器对缓冲区进行分析。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_KW41Z && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.kw41z:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.kw41z#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP KW41Z 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_KW41Z`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_KW41Z)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_MCR20A_CLK_OUT_16MHZ"></a>

## 110.31 `CONFIG_MCR20A_CLK_OUT_16MHZ`

**提示（Prompt）**：16 MHz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcr20a:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcr20a#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCR20A 驱动支持 → CLK_OUT 频率（Frequency）

<a id="CONFIG_MCR20A_CLK_OUT_1MHZ"></a>

## 110.32 `CONFIG_MCR20A_CLK_OUT_1MHZ`

**提示（Prompt）**：1 MHz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcr20a:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcr20a#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCR20A 驱动支持 → CLK_OUT 频率（Frequency）

<a id="CONFIG_MCR20A_CLK_OUT_250KHZ"></a>

## 110.33 `CONFIG_MCR20A_CLK_OUT_250KHZ`

**提示（Prompt）**：带宽（Bandwidth）：250 kHz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcr20a:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcr20a#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCR20A 驱动支持 → CLK_OUT 频率（Frequency）

<a id="CONFIG_MCR20A_CLK_OUT_32768HZ"></a>

## 110.34 `CONFIG_MCR20A_CLK_OUT_32768HZ`

**提示（Prompt）**：32768 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcr20a:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcr20a#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCR20A 驱动支持 → CLK_OUT 频率（Frequency）

<a id="CONFIG_MCR20A_CLK_OUT_32MHZ"></a>

## 110.35 `CONFIG_MCR20A_CLK_OUT_32MHZ`

**提示（Prompt）**：32 MHz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcr20a:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcr20a#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCR20A 驱动支持 → CLK_OUT 频率（Frequency）

<a id="CONFIG_MCR20A_CLK_OUT_4MHZ"></a>

## 110.36 `CONFIG_MCR20A_CLK_OUT_4MHZ`

**提示（Prompt）**：4 MHz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcr20a:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcr20a#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCR20A 驱动支持 → CLK_OUT 频率（Frequency）

<a id="CONFIG_MCR20A_CLK_OUT_62500HZ"></a>

## 110.37 `CONFIG_MCR20A_CLK_OUT_62500HZ`

**提示（Prompt）**：62500 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcr20a:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcr20a#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCR20A 驱动支持 → CLK_OUT 频率（Frequency）

<a id="CONFIG_MCR20A_CLK_OUT_8MHZ"></a>

## 110.38 `CONFIG_MCR20A_CLK_OUT_8MHZ`

**提示（Prompt）**：8 MHz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcr20a:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcr20a#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCR20A 驱动支持 → CLK_OUT 频率（Frequency）

<a id="CONFIG_MCR20A_CLK_OUT_DISABLED"></a>

## 110.39 `CONFIG_MCR20A_CLK_OUT_DISABLED`

**提示（Prompt）**：禁用（Disabled）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcr20a:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcr20a#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCR20A 驱动支持 → CLK_OUT 频率（Frequency）

<a id="CONFIG_MCR20A_IS_PART_OF_KW2XD_SIP"></a>

## 110.40 `CONFIG_MCR20A_IS_PART_OF_KW2XD_SIP`

**提示（Prompt）**：MCR20A 设备属于 KW2xD 系统级封装（SiP）的一部分

**说明（Help）**

设置此选项后，驱动不执行硬件复位，也不设置 `CLK_OUT` 频率；这些设置改为在 SoC 初始化期间完成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_MCR20A && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcr20a:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcr20a#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCR20A 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_MCR20A`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_MCR20A)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_NET_L2_CUSTOM_IEEE802154_STM32WBA"></a>

## 110.41 `CONFIG_NET_L2_CUSTOM_IEEE802154_STM32WBA`

**提示（Prompt）**：使用 ST MAC 作为二层（L2）

**说明（Help）**

自定义 STM32WBA 系列 IEEE 802.15.4 二层（L2）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_CUSTOM_IEEE802154 && CONFIG_IEEE802154_STM32WBA && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.stm32wba:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.stm32wba#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → STM32WBA 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_CUSTOM_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_CUSTOM_IEEE802154)、[`CONFIG_IEEE802154_STM32WBA`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_STM32WBA)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<!-- kconfig-navigation -->

[上一章](P109_drivers_ieee802154_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P111_drivers_input_配置项参考_1.md)
