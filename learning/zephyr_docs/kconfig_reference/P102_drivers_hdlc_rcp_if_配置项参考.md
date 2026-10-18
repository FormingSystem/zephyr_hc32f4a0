---
id: learning.zephyr-docs.kconfig-reference.page-102
title: "`drivers/hdlc_rcp_if`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第102章\_`drivers/hdlc_rcp_if`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/hdlc_rcp_if` 的 11 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HDLC_RCP_IF"></a>

## 102.1 `CONFIG_HDLC_RCP_IF`

**提示（Prompt）**：Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_OPENTHREAD && !CONFIG_OPENTHREAD_COPROCESSOR
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_ieee802154/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_ieee802154/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/openthread_rcp_arduino/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/openthread_rcp_arduino/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/hdlc_rcp_if/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hdlc_rcp_if/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)、[`CONFIG_OPENTHREAD_COPROCESSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_COPROCESSOR)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_HDLC_RCP_IF_DRV_NAME"></a>

## 102.2 `CONFIG_HDLC_RCP_IF_DRV_NAME`

**提示（Prompt）**：HDLC RCP 接口驱动名称（Interface Driver Name）

**说明（Help）**

此选项设置驱动名称（Driver Name）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_HDLC_RCP_IF
```

**默认值（Defaults）**

```text
"hdlc_rcp_if"
```

**定义位置（Location）**：[`drivers/hdlc_rcp_if/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hdlc_rcp_if/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF)。

<a id="CONFIG_HDLC_RCP_IF_NXP"></a>

## 102.3 `CONFIG_HDLC_RCP_IF_NXP`

**提示（Prompt）**：用于 Zephyr OpenThread 无线电协处理器主机（RCP Host）的 NXP HDLC 接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_HDLC_RCP_IF_ENABLED && CONFIG_HDLC_RCP_IF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/hdlc_rcp_if/Kconfig.nxp:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hdlc_rcp_if/Kconfig.nxp#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF)。

<a id="CONFIG_HDLC_RCP_IF_SPI"></a>

## 102.4 `CONFIG_HDLC_RCP_IF_SPI`

**提示（Prompt）**：用于 Zephyr OpenThread 无线电协处理器主机（RCP Host）的 SPI HDLC 接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SPI_HDLC_RCP_IF_ENABLED && CONFIG_SPI && CONFIG_HDLC_RCP_IF
```

**默认值（Defaults）**

```text
y
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_ieee802154/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_ieee802154/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/hdlc_rcp_if/Kconfig.spi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hdlc_rcp_if/Kconfig.spi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_HDLC_RCP_IF`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF)。

<a id="CONFIG_HDLC_RCP_IF_SPI_ALIGN_ALLOWANCE"></a>

## 102.5 `CONFIG_HDLC_RCP_IF_SPI_ALIGN_ALLOWANCE`

**提示（Prompt）**：HDLC RCP 接口 SPI 接收对齐余量（RX Alignment Allowance）

**说明（Help）**

指定可从 SDI 帧开头裁除的 `0xFF` 字节的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HDLC_RCP_IF_SPI && CONFIG_HDLC_RCP_IF
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 16]
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_ieee802154/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_ieee802154/Kconfig.defconfig)。

```text
16
```

**定义位置（Location）**：[`drivers/hdlc_rcp_if/Kconfig.spi:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hdlc_rcp_if/Kconfig.spi#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口 → 用于 Zephyr OpenThread 无线电协处理器主机（RCP Host）的 SPI HDLC 接口

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF_SPI`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF_SPI)、[`CONFIG_HDLC_RCP_IF`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF)。

<a id="CONFIG_HDLC_RCP_IF_SPI_DEFERRED_INIT"></a>

## 102.6 `CONFIG_HDLC_RCP_IF_SPI_DEFERRED_INIT`

**提示（Prompt）**：将 SPI RCP 接口启动推迟到显式请求时（Deferred Start）

**说明（Help）**

启用后，阻止 `net_if_post_init()` 在启动时自动启用 OpenThread 接口，并将 SPI 中断使能（Interrupt Arming）推迟到调用 `hdlc_api.deferred_init()` 时。这适用于异步加载无线电协处理器（RCP）固件的情况，例如在 SPI 活动之前，通过蓝牙 UART H4 上传 IW61X 固件。固件就绪后，可调用 `hdlc_api.deferred_init()`，使能 SPI 中断请求（IRQ）并启用网络接口。禁用此项时，在初始化期间使能 SPI IRQ，并自动启用接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HDLC_RCP_IF_SPI && CONFIG_HDLC_RCP_IF_SPI && CONFIG_HDLC_RCP_IF
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_ieee802154/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_ieee802154/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/hdlc_rcp_if/Kconfig.spi:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hdlc_rcp_if/Kconfig.spi#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口 → 用于 Zephyr OpenThread 无线电协处理器主机（RCP Host）的 SPI HDLC 接口

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF_SPI`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF_SPI)、[`CONFIG_HDLC_RCP_IF`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF)。

<a id="CONFIG_HDLC_RCP_IF_SPI_MAX_FRAME_SIZE"></a>

## 102.7 `CONFIG_HDLC_RCP_IF_SPI_MAX_FRAME_SIZE`

**提示（Prompt）**：HDLC RCP 接口 SPI 最大帧大小（Maximum Frame Size）

**说明（Help）**

OpenThread HDLC 主机 SPI 的最大帧大小（Maximum Frame Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HDLC_RCP_IF_SPI && CONFIG_HDLC_RCP_IF
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/hdlc_rcp_if/Kconfig.spi:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hdlc_rcp_if/Kconfig.spi#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口 → 用于 Zephyr OpenThread 无线电协处理器主机（RCP Host）的 SPI HDLC 接口

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF_SPI`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF_SPI)、[`CONFIG_HDLC_RCP_IF`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF)。

<a id="CONFIG_HDLC_RCP_IF_SPI_SMALL_PACKET_SIZE"></a>

## 102.8 `CONFIG_HDLC_RCP_IF_SPI_SMALL_PACKET_SIZE`

**提示（Prompt）**：HDLC RCP 接口 SPI 小数据包大小（Small Packet Size）

**说明（Help）**

指定单次事务（Transaction）中可接收的最小数据包大小。更大的数据包需要多次事务。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HDLC_RCP_IF_SPI && CONFIG_HDLC_RCP_IF
```

**默认值（Defaults）**

```text
32
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_ieee802154/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_ieee802154/Kconfig.defconfig)。

```text
48
```

**定义位置（Location）**：[`drivers/hdlc_rcp_if/Kconfig.spi:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hdlc_rcp_if/Kconfig.spi#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口 → 用于 Zephyr OpenThread 无线电协处理器主机（RCP Host）的 SPI HDLC 接口

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF_SPI`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF_SPI)、[`CONFIG_HDLC_RCP_IF`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF)。

<a id="CONFIG_HDLC_RCP_IF_UART"></a>

## 102.9 `CONFIG_HDLC_RCP_IF_UART`

**提示（Prompt）**：用于 Zephyr OpenThread 无线电协处理器主机（RCP Host）的 UART HDLC 接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_UART_HDLC_RCP_IF_ENABLED && CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HDLC_RCP_IF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/hdlc_rcp_if/Kconfig.uart:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hdlc_rcp_if/Kconfig.uart#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HDLC_RCP_IF`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF)。

<a id="CONFIG_OPENTHREAD_HDLC_RCP_IF_UART_RX_RING_BUFFER_SIZE"></a>

## 102.10 `CONFIG_OPENTHREAD_HDLC_RCP_IF_UART_RX_RING_BUFFER_SIZE`

**提示（Prompt）**：设置 HDLC RCP 接口 UART 接收环形缓冲区大小（RX Ring Buffer Size）

**说明（Help）**

OpenThread HDLC 主机 UART 的接收缓冲区大小（RX Buffer Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HDLC_RCP_IF
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/hdlc_rcp_if/Kconfig.uart:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hdlc_rcp_if/Kconfig.uart#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF)。

<a id="CONFIG_OPENTHREAD_HDLC_RCP_IF_UART_TX_RING_BUFFER_SIZE"></a>

## 102.11 `CONFIG_OPENTHREAD_HDLC_RCP_IF_UART_TX_RING_BUFFER_SIZE`

**提示（Prompt）**：设置 HDLC RCP 接口 UART 发送环形缓冲区大小（TX Ring Buffer Size）

**说明（Help）**

OpenThread HDLC 主机 UART 的发送缓冲区大小（TX Buffer Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HDLC_RCP_IF
```

**默认值（Defaults）**

```text
1344
```

**定义位置（Location）**：[`drivers/hdlc_rcp_if/Kconfig.uart:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hdlc_rcp_if/Kconfig.uart#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF)。

<!-- kconfig-navigation -->

[上一章](P101_drivers_haptics_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P103_drivers_hwinfo_配置项参考.md)
