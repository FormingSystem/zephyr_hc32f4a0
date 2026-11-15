---
id: learning.zephyr-docs.kconfig-reference.page-57
title: "`drivers/bluetooth`配置项参考（4/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第57章\_`drivers/bluetooth`配置项参考（4/4）

本章翻译官方 Kconfig 数据库中 `drivers/bluetooth` 的 16 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ESP_BT_HEAP_SYSTEM"></a>

## 57.1 `CONFIG_ESP_BT_HEAP_SYSTEM`

**提示（Prompt）**：内核内存池堆，k_malloc（Kernel Memory Pool Heap）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_BT_HEAP>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 蓝牙堆类型（Bluetooth Heap Type）

**配置项引用（Symbol References）**：[`CONFIG_ESP_BT_HEAP`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP_BT_HEAP)。

<a id="CONFIG_HCI_NXP_ANT_DIVERSITY"></a>

## 57.2 `CONFIG_HCI_NXP_ANT_DIVERSITY`

**提示（Prompt）**：天线分集配置（Antenna Diversity Configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HCI_NXP_SET_CAL_DATA_ANNEX100 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_HCI_NXP_ANT_DIVERSITY_ANT1
```

**可选项（Choices）**

```text
CONFIG_HCI_NXP_ANT_DIVERSITY_ANT1
CONFIG_HCI_NXP_ANT_DIVERSITY_ANT2
CONFIG_HCI_NXP_ANT_DIVERSITY_ANT3
CONFIG_HCI_NXP_ANT_DIVERSITY_ANT4
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HCI_NXP_SET_CAL_DATA_ANNEX100`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_HCI_NXP_SET_CAL_DATA_ANNEX100)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_HCI_NXP_ANT_DIVERSITY_ANT1`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_HCI_NXP_ANT_DIVERSITY_ANT1)、[`CONFIG_HCI_NXP_ANT_DIVERSITY_ANT2`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_HCI_NXP_ANT_DIVERSITY_ANT2)、[`CONFIG_HCI_NXP_ANT_DIVERSITY_ANT3`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_HCI_NXP_ANT_DIVERSITY_ANT3)、[`CONFIG_HCI_NXP_ANT_DIVERSITY_ANT4`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_HCI_NXP_ANT_DIVERSITY_ANT4)。

<a id="CONFIG_HCI_NXP_ANT_DIVERSITY_ANT1"></a>

## 57.3 `CONFIG_HCI_NXP_ANT_DIVERSITY_ANT1`

**提示（Prompt）**：ANT1 天线分集，与 annex100 共用（Antenna Diversity）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HCI_NXP_ANT_DIVERSITY>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 天线分集配置（Antenna Diversity Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HCI_NXP_ANT_DIVERSITY`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_HCI_NXP_ANT_DIVERSITY)。

<a id="CONFIG_HCI_NXP_ANT_DIVERSITY_ANT2"></a>

## 57.4 `CONFIG_HCI_NXP_ANT_DIVERSITY_ANT2`

**提示（Prompt）**：ANT2 天线分集，配合外部 FEM，仅用于 BLE（Antenna Diversity with External FEM）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HCI_NXP_ANT_DIVERSITY>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 天线分集配置（Antenna Diversity Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HCI_NXP_ANT_DIVERSITY`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_HCI_NXP_ANT_DIVERSITY)。

<a id="CONFIG_HCI_NXP_ANT_DIVERSITY_ANT3"></a>

## 57.5 `CONFIG_HCI_NXP_ANT_DIVERSITY_ANT3`

**提示（Prompt）**：ANT3 天线分集，配合 annex100（Antenna Diversity）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HCI_NXP_ANT_DIVERSITY>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 天线分集配置（Antenna Diversity Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HCI_NXP_ANT_DIVERSITY`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_HCI_NXP_ANT_DIVERSITY)。

<a id="CONFIG_HCI_NXP_ANT_DIVERSITY_ANT4"></a>

## 57.6 `CONFIG_HCI_NXP_ANT_DIVERSITY_ANT4`

**提示（Prompt）**：ANT4 天线分集，配合 annex100（Antenna Diversity）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HCI_NXP_ANT_DIVERSITY>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 天线分集配置（Antenna Diversity Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HCI_NXP_ANT_DIVERSITY`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_HCI_NXP_ANT_DIVERSITY)。

<a id="CONFIG_HCI_NXP_CONFIG_IR"></a>

## 57.7 `CONFIG_HCI_NXP_CONFIG_IR`

**提示（Prompt）**：蓝牙控制器独立复位配置（Independent Reset Configuration）

**说明（Help）**

启用后，主机（Host）在主机控制器接口（HCI）初始化期间，向蓝牙控制器发送 iR 配置的厂商专用命令（Vendor Command）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4_NXP_CTLR && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4_NXP_CTLR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4_NXP_CTLR)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_HCI_NXP_ENABLE_AUTO_SLEEP"></a>

## 57.8 `CONFIG_HCI_NXP_ENABLE_AUTO_SLEEP`

**提示（Prompt）**：BLE 控制器自动休眠模式（Controller Auto Sleep Mode）

**说明（Help）**

启用后，在主机控制器接口（HCI）初始化期间配置并启用控制器自动休眠模式（Auto Sleep Mode）。自动休眠表示控制器自行管理其低功耗状态（Low-Power State）。此功能可以节电，但向控制器发送 HCI 消息时会增加一定延迟，因为主机（Host）需要先唤醒控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_HCI_NXP_RX_MSG_QUEUE_SIZE"></a>

## 57.9 `CONFIG_HCI_NXP_RX_MSG_QUEUE_SIZE`

**提示（Prompt）**：HCI 接收消息队列大小（RX Message Queue Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HCI_NXP_RX_THREAD && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 在专用线程中处理接收缓冲区（Dedicated RX Processing Thread）

**配置项引用（Symbol References）**：[`CONFIG_HCI_NXP_RX_THREAD`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_HCI_NXP_RX_THREAD)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_HCI_NXP_RX_STACK_SIZE"></a>

## 57.10 `CONFIG_HCI_NXP_RX_STACK_SIZE`

**提示（Prompt）**：HCI 接收栈大小（RX Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HCI_NXP_RX_THREAD && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 在专用线程中处理接收缓冲区（Dedicated RX Processing Thread）

**配置项引用（Symbol References）**：[`CONFIG_HCI_NXP_RX_THREAD`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_HCI_NXP_RX_THREAD)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_HCI_NXP_RX_THREAD"></a>

## 57.11 `CONFIG_HCI_NXP_RX_THREAD`

**提示（Prompt）**：在专用线程中处理接收缓冲区（Dedicated RX Processing Thread）

**说明（Help）**

某些平台在中断服务例程（ISR）上下文中接收主机控制器接口（HCI）的接收缓冲区。启用后，由 ISR 将 HCI 接收消息入队，再由专用线程（Dedicated Thread）处理该消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_HCI_NXP_SET_CAL_DATA"></a>

## 57.12 `CONFIG_HCI_NXP_SET_CAL_DATA`

**提示（Prompt）**：蓝牙控制器校准数据（Controller Calibration Data）

**说明（Help）**

启用后，主机（Host）在主机控制器接口（HCI）初始化期间向蓝牙控制器发送校准数据（Calibration Data）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_NXP_NW612 || CONFIG_BT_NXP_IW416
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_NXP_NW612`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_NW612)、[`CONFIG_BT_NXP_IW416`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_IW416)。

<a id="CONFIG_HCI_NXP_SET_CAL_DATA_ANNEX100"></a>

## 57.13 `CONFIG_HCI_NXP_SET_CAL_DATA_ANNEX100`

**提示（Prompt）**：蓝牙控制器校准数据附录 100（Calibration Data Annex 100）

**说明（Help）**

启用后，主机（Host）在主机控制器接口（HCI）初始化期间向蓝牙控制器发送校准数据附录 100（Calibration Data Annex 100）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HCI_NXP_SET_CAL_DATA && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_NXP_NW612 || CONFIG_BT_NXP_IW416
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 蓝牙控制器校准数据（Controller Calibration Data）

**配置项引用（Symbol References）**：[`CONFIG_HCI_NXP_SET_CAL_DATA`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_HCI_NXP_SET_CAL_DATA)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_NXP_NW612`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_NW612)、[`CONFIG_BT_NXP_IW416`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_IW416)。

<a id="CONFIG_HCI_NXP_TRIGGER_IR_ON_BT_INIT"></a>

## 57.14 `CONFIG_HCI_NXP_TRIGGER_IR_ON_BT_INIT`

**提示（Prompt）**：蓝牙初始化时触发独立复位（IR Triggered on BT Init）

**说明（Help）**

启用后，在蓝牙禁用之后再次初始化蓝牙时，主机（Host）向蓝牙控制器发送触发 iR 的厂商专用命令（Vendor Command）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4_NXP_CTLR && CONFIG_BT_HCI_HOST && CONFIG_HCI_NXP_CONFIG_IR && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 蓝牙控制器独立复位配置（Independent Reset Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4_NXP_CTLR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4_NXP_CTLR)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_HCI_NXP_CONFIG_IR`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_HCI_NXP_CONFIG_IR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_BFLB_BT"></a>

## 57.15 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_BFLB_BT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为低功耗蓝牙（BLE）控制器使用预留的额外堆内存（Heap Memory），例如任务栈、消息队列等。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BFLB && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_ESP_BT"></a>

## 57.16 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_ESP_BT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为蓝牙驱动使用预留的额外堆大小（Additional Heap Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
50000 if CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2
25600
0
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<!-- kconfig-navigation -->

[上一章](P056_drivers_bluetooth_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P058_drivers_buzzer_配置项参考.md)
