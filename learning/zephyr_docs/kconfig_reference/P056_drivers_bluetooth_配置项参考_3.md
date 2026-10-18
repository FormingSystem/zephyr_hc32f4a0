---
id: learning.zephyr-docs.kconfig-reference.page-56
title: "`drivers/bluetooth`配置项参考（3/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第56章\_`drivers/bluetooth`配置项参考（3/4）

本章翻译官方 Kconfig 数据库中 `drivers/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ESP32_BT_CTLR_LE_LLCP_PHY_UPDATE"></a>

## 56.1 `CONFIG_ESP32_BT_CTLR_LE_LLCP_PHY_UPDATE`

**提示（Prompt）**：PHY 更新超时时终止（PHY Update Timeout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 低功耗蓝牙链路层控制过程（BLE Link-Layer Control Procedures）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_LE_MASTER"></a>

## 56.2 `CONFIG_ESP32_BT_CTLR_LE_MASTER`

**提示（Prompt）**：低功耗蓝牙主设备角色支持（BLE Master Role Support）

**说明（Help）**

禁用后，不使用可连接广播（Connectable Advertising）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_LE_MAX_ACT"></a>

## 56.3 `CONFIG_ESP32_BT_CTLR_LE_MAX_ACT`

**提示（Prompt）**：BLE 活动实例上限（Activity Instance Limit）

**说明（Help）**

低功耗蓝牙（BLE）活动数量，包括连接（Connection）、扫描（Scanning）、广播（Advertising）和同步（Synchronization）。每个实例约使用 828 字节动态 RAM（DRAM）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_LE_MAX_CONN"></a>

## 56.4 `CONFIG_ESP32_BT_CTLR_LE_MAX_CONN`

**提示（Prompt）**：低功耗蓝牙连接上限（BLE Connection Limit）

**说明（Help）**

并发低功耗蓝牙（BLE）连接的最大数量。每个连接约消耗 1 KB 动态 RAM（DRAM）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 9]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_LE_PING_EN"></a>

## 56.5 `CONFIG_ESP32_BT_CTLR_LE_PING_EN`

**提示（Prompt）**：低功耗蓝牙已认证载荷超时（LE Authenticated Payload Timeout）

**说明（Help）**

启用低功耗蓝牙已认证载荷超时（LE Authenticated Payload Timeout），即 Ping 定时器，以保护链路安全（Link Security）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_LE_PING
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:204`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L204)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_LE_PING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_PING)。

<a id="CONFIG_ESP32_BT_CTLR_LE_SCAN"></a>

## 56.6 `CONFIG_ESP32_BT_CTLR_LE_SCAN`

**提示（Prompt）**：低功耗蓝牙扫描支持（BLE Scanning Support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L233)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_LE_SECURITY_ENABLE"></a>

## 56.7 `CONFIG_ESP32_BT_CTLR_LE_SECURITY_ENABLE`

**提示（Prompt）**：低功耗蓝牙安全支持（BLE Security Support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_LE_ENC
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:237`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L237)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_LE_ENC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_ENC)。

<a id="CONFIG_ESP32_BT_CTLR_LE_STATIC_ACL_TX_BUF_NB"></a>

## 56.8 `CONFIG_ESP32_BT_CTLR_LE_STATIC_ACL_TX_BUF_NB`

**提示（Prompt）**：BLE 静态 ACL 发送缓冲区数量（Static ACL TX Buffers）

**说明（Help）**

低功耗蓝牙（BLE）的 ACL 缓冲区有两种分配方式：持久分配（Persistent Allocation），即控制器初始化时分配，直到控制器反初始化才释放；以及动态分配（Dynamic Allocation），即发送前分配、发送后释放。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 12]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX"></a>

## 56.9 `CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX`

**提示（Prompt）**：蓝牙默认接收天线（Default RX Antenna）

**说明（Help）**

选择用于蓝牙接收（Bluetooth Reception）的天线。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**可选项（Choices）**

```text
CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX_0
CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX_1
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX_0`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX_0)、[`CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX_1`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX_1)。

<a id="CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX_0"></a>

## 56.10 `CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX_0`

**提示（Prompt）**：天线 0（Antenna 0）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 蓝牙默认接收天线（Default RX Antenna）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX)。

<a id="CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX_1"></a>

## 56.11 `CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX_1`

**提示（Prompt）**：天线 1（Antenna 1）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:183`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L183)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 蓝牙默认接收天线（Default RX Antenna）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTLR_RX_ANTENNA_INDEX)。

<a id="CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX"></a>

## 56.12 `CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX`

**提示（Prompt）**：蓝牙默认发射天线（Default TX Antenna）

**说明（Help）**

选择用于蓝牙发送（Bluetooth Transmission）的天线。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**可选项（Choices）**

```text
CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX_0
CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX_1
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX_0`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX_0)、[`CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX_1`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX_1)。

<a id="CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX_0"></a>

## 56.13 `CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX_0`

**提示（Prompt）**：天线 0（Antenna 0）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 蓝牙默认发射天线（Default TX Antenna）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX)。

<a id="CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX_1"></a>

## 56.14 `CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX_1`

**提示（Prompt）**：天线 1（Antenna 1）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 蓝牙默认发射天线（Default TX Antenna）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTLR_TX_ANTENNA_INDEX)。

<a id="CONFIG_ESP32_BT_CTRL_LOW_POWER_CLOCK"></a>

## 56.15 `CONFIG_ESP32_BT_CTRL_LOW_POWER_CLOCK`

**提示（Prompt）**：蓝牙低功耗时钟（Bluetooth Low-Power Clock）

**说明（Help）**

蓝牙调制解调器休眠（Modem Sleep）的低功耗时钟源（Low-Power Clock Source），选项与 ESP-IDF 相同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_CTRL_MODEM_SLEEP_MODE_1 && (CONFIG_SOC_SERIES_ESP32C3 || CONFIG_SOC_SERIES_ESP32S3) && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_ESP32_BT_CTRL_LPCLK_SEL_MAIN_XTAL
```

**可选项（Choices）**

```text
CONFIG_ESP32_BT_CTRL_LPCLK_SEL_MAIN_XTAL
CONFIG_ESP32_BT_CTRL_LPCLK_SEL_EXT_32K_XTAL
CONFIG_ESP32_BT_CTRL_LPCLK_SEL_RTC_SLOW
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:893`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L893)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 调制解调器休眠，ESP32-C3／S3（Modem Sleep） → 蓝牙调制解调器休眠（Bluetooth Modem Sleep） → 蓝牙调制解调器休眠模式 1（Modem Sleep Mode 1）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTRL_MODEM_SLEEP_MODE_1`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTRL_MODEM_SLEEP_MODE_1)、[`CONFIG_SOC_SERIES_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP32_BT_CTRL_LPCLK_SEL_MAIN_XTAL`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTRL_LPCLK_SEL_MAIN_XTAL)、[`CONFIG_ESP32_BT_CTRL_LPCLK_SEL_EXT_32K_XTAL`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTRL_LPCLK_SEL_EXT_32K_XTAL)、[`CONFIG_ESP32_BT_CTRL_LPCLK_SEL_RTC_SLOW`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTRL_LPCLK_SEL_RTC_SLOW)。

<a id="CONFIG_ESP32_BT_CTRL_LPCLK_SEL_EXT_32K_XTAL"></a>

## 56.16 `CONFIG_ESP32_BT_CTRL_LPCLK_SEL_EXT_32K_XTAL`

**提示（Prompt）**：外部 32kHz 晶体／振荡器（External Crystal / Oscillator）

**说明（Help）**

外部 32.768 kHz 参考源（External Reference）。仅在开发板提供该时钟源时使用，其作用与 ESP-IDF 的 `BT_CTRL_LPCLK_SEL_EXT_32K_XTAL` 相同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_CTRL_LOW_POWER_CLOCK>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:907`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L907)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 调制解调器休眠，ESP32-C3／S3（Modem Sleep） → 蓝牙调制解调器休眠（Bluetooth Modem Sleep） → 蓝牙调制解调器休眠模式 1（Modem Sleep Mode 1） → 蓝牙低功耗时钟（Bluetooth Low-Power Clock）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTRL_LOW_POWER_CLOCK`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTRL_LOW_POWER_CLOCK)。

<a id="CONFIG_ESP32_BT_CTRL_LPCLK_SEL_MAIN_XTAL"></a>

## 56.17 `CONFIG_ESP32_BT_CTRL_LPCLK_SEL_MAIN_XTAL`

**提示（Prompt）**：主晶体（Main Crystal）

**说明（Help）**

将主晶体（Main Crystal）用作低功耗时钟。可与动态频率调整（DFS）配合使用；结合“轻度休眠期间为主晶体供电”选项，还可以支持系统轻度休眠（Light Sleep）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_CTRL_LOW_POWER_CLOCK>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:900`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L900)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 调制解调器休眠，ESP32-C3／S3（Modem Sleep） → 蓝牙调制解调器休眠（Bluetooth Modem Sleep） → 蓝牙调制解调器休眠模式 1（Modem Sleep Mode 1） → 蓝牙低功耗时钟（Bluetooth Low-Power Clock）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTRL_LOW_POWER_CLOCK`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTRL_LOW_POWER_CLOCK)。

<a id="CONFIG_ESP32_BT_CTRL_LPCLK_SEL_RTC_SLOW"></a>

## 56.18 `CONFIG_ESP32_BT_CTRL_LPCLK_SEL_RTC_SLOW`

**提示（Prompt）**：内部 136kHz RC 振荡器（Internal RC Oscillator）

**说明（Help）**

内部低速 RC（Internal Slow RC）；用于已建立连接的低功耗蓝牙（BLE）时精度较差，与 ESP-IDF 中的注意事项相同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_CTRL_LOW_POWER_CLOCK>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:913`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L913)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 调制解调器休眠，ESP32-C3／S3（Modem Sleep） → 蓝牙调制解调器休眠（Bluetooth Modem Sleep） → 蓝牙调制解调器休眠模式 1（Modem Sleep Mode 1） → 蓝牙低功耗时钟（Bluetooth Low-Power Clock）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTRL_LOW_POWER_CLOCK`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTRL_LOW_POWER_CLOCK)。

<a id="CONFIG_ESP32_BT_CTRL_MAIN_XTAL_PU_DURING_LIGHT_SLEEP"></a>

## 56.19 `CONFIG_ESP32_BT_CTRL_MAIN_XTAL_PU_DURING_LIGHT_SLEEP`

原库同名定义共 2 条；本项为数据库第 5611 条记录，各定义分别保留。

**提示（Prompt）**：轻度休眠期间保持主晶体供电（Keep Main XTAL Powered）

**说明（Help）**

在轻度休眠（Light Sleep）期间保持主晶体振荡器（Main Crystal Oscillator）供电，使低功耗蓝牙（BLE）唤醒时具有稳定时钟。代价是增加休眠电流；仅在 BLE 活动跨越轻度休眠状态切换时启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && (CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:772`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L772)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_CTRL_MAIN_XTAL_PU_DURING_LIGHT_SLEEP--record-5612"></a>

## 56.20 `CONFIG_ESP32_BT_CTRL_MAIN_XTAL_PU_DURING_LIGHT_SLEEP`

原库同名定义共 2 条；本项为数据库第 5612 条记录，各定义分别保留。

**提示（Prompt）**：轻度休眠期间为主晶体供电（Power Up Main XTAL）

**说明（Help）**

选择后，当低功耗时钟使用主晶体（Main XTAL）或外部 32kHz 时，轻度休眠（Light Sleep）期间主晶体保持供电，对应 ESP-IDF 的 `BT_CTRL_MAIN_XTAL_PU_DURING_LIGHT_SLEEP`。使用主晶体而未启用此项时，控制器会设置 `no_light_sleep`，阻止系统轻度休眠。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESP32_BT_CTRL_LPCLK_SEL_MAIN_XTAL || CONFIG_ESP32_BT_CTRL_LPCLK_SEL_EXT_32K_XTAL) && (CONFIG_SOC_SERIES_ESP32C3 || CONFIG_SOC_SERIES_ESP32S3) && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:920`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L920)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 调制解调器休眠，ESP32-C3／S3（Modem Sleep）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTRL_LPCLK_SEL_MAIN_XTAL`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTRL_LPCLK_SEL_MAIN_XTAL)、[`CONFIG_ESP32_BT_CTRL_LPCLK_SEL_EXT_32K_XTAL`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTRL_LPCLK_SEL_EXT_32K_XTAL)、[`CONFIG_SOC_SERIES_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTRL_MODEM_SLEEP"></a>

## 56.21 `CONFIG_ESP32_BT_CTRL_MODEM_SLEEP`

**提示（Prompt）**：蓝牙调制解调器休眠（Bluetooth Modem Sleep）

**说明（Help）**

启用或禁用蓝牙控制器低功耗模式，即调制解调器休眠（Modem Sleep）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C3 || CONFIG_SOC_SERIES_ESP32S3) && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:879`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L879)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 调制解调器休眠，ESP32-C3／S3（Modem Sleep）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTRL_MODEM_SLEEP_MODE_1"></a>

## 56.22 `CONFIG_ESP32_BT_CTRL_MODEM_SLEEP_MODE_1`

**提示（Prompt）**：蓝牙调制解调器休眠模式 1（Modem Sleep Mode 1）

**说明（Help）**

在此模式下，控制器使用专用低功耗时钟（Low-Power Clock），在低功耗蓝牙（BLE）事件之间休眠。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_CTRL_MODEM_SLEEP && (CONFIG_SOC_SERIES_ESP32C3 || CONFIG_SOC_SERIES_ESP32S3) && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:885`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L885)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 调制解调器休眠，ESP32-C3／S3（Modem Sleep） → 蓝牙调制解调器休眠（Bluetooth Modem Sleep）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTRL_MODEM_SLEEP`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_CTRL_MODEM_SLEEP)、[`CONFIG_SOC_SERIES_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT"></a>

## 56.23 `CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT`

**提示（Prompt）**：BLE 5 功能支持（Feature Support）

**说明（Help）**

支持 Bluetooth 5.0 引入的功能，包括扩展广播（Extended Advertising）、2M 物理层（PHY）和编码物理层（Coded PHY）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_ADV_EXT || CONFIG_BT_CTLR_ADV_PERIODIC || CONFIG_BT_CTLR_PHY_2M || CONFIG_BT_CTLR_PHY_CODED
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:291`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L291)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_ADV_EXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_CTLR_ADV_PERIODIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_PERIODIC)、[`CONFIG_BT_CTLR_PHY_2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_2M)、[`CONFIG_BT_CTLR_PHY_CODED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_CODED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_ACL_BUF_COUNT"></a>

## 56.24 `CONFIG_ESP32_BT_LE_ACL_BUF_COUNT`

**提示（Prompt）**：ACL 缓冲区数量（ACL Buffer Count）

**说明（Help）**

主机控制器接口（HCI）异步连接逻辑传输（ACL）数据缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:447`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L447)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 内存设置（Memory Settings）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_ACL_BUF_SIZE"></a>

## 56.25 `CONFIG_ESP32_BT_LE_ACL_BUF_SIZE`

**提示（Prompt）**：ACL 缓冲区大小（ACL Buffer Size）

**说明（Help）**

每个 HCI ACL 数据包的最大数据大小，不包含 4 字节包头（Header）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
517
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:453`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L453)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 内存设置（Memory Settings）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_ADV_DATA_LENGTH_ZERO_AUX"></a>

## 56.26 `CONFIG_ESP32_BT_LE_ADV_DATA_LENGTH_ZERO_AUX`

**提示（Prompt）**：零长度广播中包含辅助数据包（Auxiliary Packet）

**说明（Help）**

当载荷长度为零时，在不可连接、不可扫描广播（Non-Connectable, Non-Scannable Advertising）中包含辅助协议数据单元（AUX PDU）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_LE_CCA_MODE"></a>

## 56.27 `CONFIG_ESP32_BT_LE_CCA_MODE`

**提示（Prompt）**：低功耗蓝牙空闲信道评估模式（BLE Clear Channel Assessment Mode）

**说明（Help）**

选择低功耗蓝牙（BLE）空闲信道评估（CCA）的行为。信道繁忙时，CCA 会延迟数据包发送，从而影响扫描和连接时序（Timing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_ESP32_BT_LE_CCA_MODE_NONE
```

**可选项（Choices）**

```text
CONFIG_ESP32_BT_LE_CCA_MODE_NONE
CONFIG_ESP32_BT_LE_CCA_MODE_HW
CONFIG_ESP32_BT_LE_CCA_MODE_SW
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP32_BT_LE_CCA_MODE_NONE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CCA_MODE_NONE)、[`CONFIG_ESP32_BT_LE_CCA_MODE_HW`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CCA_MODE_HW)、[`CONFIG_ESP32_BT_LE_CCA_MODE_SW`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CCA_MODE_SW)。

<a id="CONFIG_ESP32_BT_LE_CCA_MODE_HW"></a>

## 56.28 `CONFIG_ESP32_BT_LE_CCA_MODE_HW`

**提示（Prompt）**：硬件空闲信道评估（Hardware CCA）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_LE_CCA_MODE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 低功耗蓝牙空闲信道评估模式（BLE Clear Channel Assessment Mode）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_CCA_MODE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CCA_MODE)。

<a id="CONFIG_ESP32_BT_LE_CCA_MODE_NONE"></a>

## 56.29 `CONFIG_ESP32_BT_LE_CCA_MODE_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_LE_CCA_MODE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 低功耗蓝牙空闲信道评估模式（BLE Clear Channel Assessment Mode）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_CCA_MODE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CCA_MODE)。

<a id="CONFIG_ESP32_BT_LE_CCA_MODE_SW"></a>

## 56.30 `CONFIG_ESP32_BT_LE_CCA_MODE_SW`

**提示（Prompt）**：软件空闲信道评估，实验性（Software CCA, Experimental）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_LE_CCA_MODE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 低功耗蓝牙空闲信道评估模式（BLE Clear Channel Assessment Mode）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_CCA_MODE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CCA_MODE)。

<a id="CONFIG_ESP32_BT_LE_CCA_RSSI_THRESH"></a>

## 56.31 `CONFIG_ESP32_BT_LE_CCA_RSSI_THRESH`

**提示（Prompt）**：CCA 的 RSSI 阈值，以 −1 dBm 为单位（RSSI Threshold）

**说明（Help）**

发送空闲信道评估（TX CCA）的接收信号强度指示（RSSI）阈值，以 −1 dBm 为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_TX_CCA_ENABLED && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
65
```

**取值范围（Ranges）**

```text
[20, 100]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:703`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L703)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 发送空闲信道评估功能（TX CCA Feature）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_TX_CCA_ENABLED`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_TX_CCA_ENABLED)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM"></a>

## 56.32 `CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM`

**提示（Prompt）**：共存场景下编码 PHY 收发时间限制（Coded PHY TX/RX Time Limit）

**说明（Help）**

对编码物理层（Coded PHY）的发送／接收（TX/RX）施加时间限制，以减少 Wi-Fi 干扰。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_SW_COEXIST_ENABLE && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM_DIS
```

**可选项（Choices）**

```text
CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM_EN
CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM_DIS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:591`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L591)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_SW_COEXIST_ENABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP32_SW_COEXIST_ENABLE)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM_DIS`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM_DIS)、[`CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM_EN`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM_EN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM_DIS"></a>

## 56.33 `CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM_DIS`

**提示（Prompt）**：不限制（No Limit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:601`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L601)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 共存场景下编码 PHY 收发时间限制（Coded PHY TX/RX Time Limit）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM)。

<a id="CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM_EN"></a>

## 56.34 `CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM_EN`

**提示（Prompt）**：应用限制（Apply Limit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:598`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L598)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 共存场景下编码 PHY 收发时间限制（Coded PHY TX/RX Time Limit）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_COEX_PHY_CODED_TX_RX_TLIM)。

<a id="CONFIG_ESP32_BT_LE_CONTROLLER_TASK_STACK_SIZE"></a>

## 56.35 `CONFIG_ESP32_BT_LE_CONTROLLER_TASK_STACK_SIZE`

**提示（Prompt）**：控制器任务栈大小（Controller Task Stack Size）

**说明（Help）**

低功耗蓝牙（BLE）控制器任务的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:480`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L480)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS"></a>

## 56.36 `CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS`

**提示（Prompt）**：Mbed TLS 密码学协议栈（Crypto Stack）

**说明（Help）**

使用 Mbed TLS 库执行低功耗蓝牙（BLE）密码学操作（Cryptographic Operations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_SECURITY_ENABLE && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_LE_ENC
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_MBEDTLS_CTR_DRBG_C
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY
CONFIG_PSA_WANT_ECC_SECP_R1_256
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_MBEDTLS_DECLARE_PRIVATE_IDENTIFIERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:527`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L527)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙安全管理器（BLE Security Manager）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_SECURITY_ENABLE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SECURITY_ENABLE)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_LE_ENC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_ENC)、[`CONFIG_PSA_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)、[`CONFIG_MBEDTLS_CTR_DRBG_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CTR_DRBG_C)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ECC_SECP_R1_256)、[`CONFIG_PSA_WANT_ALG_ECDH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_MBEDTLS_DECLARE_PRIVATE_IDENTIFIERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_DECLARE_PRIVATE_IDENTIFIERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_ADV_CH38_39_TX_AVOID_CONFLICT_EN"></a>

## 56.37 `CONFIG_ESP32_BT_LE_CTLR_ADV_CH38_39_TX_AVOID_CONFLICT_EN`

**提示（Prompt）**：避免广播信道 38／39 上的发送冲突（TX Conflicts）

**说明（Help）**

广播信道 38 和 39 与连接事件（Connection Event）重叠时，跳过这些信道上的广播，以减少空中碰撞（On-Air Collision）；代价是广播吞吐量略有下降。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:780`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L780)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_ADV_DATA_LENGTH_ZERO_AUX"></a>

## 56.38 `CONFIG_ESP32_BT_LE_CTLR_ADV_DATA_LENGTH_ZERO_AUX`

**提示（Prompt）**：零长度扩展广播的辅助数据包，实验性（Aux Packet for Zero-Length Extended Advertising）

**说明（Help）**

在零长度、不可连接、不可扫描的扩展广播（Extended Advertising）中包含辅助协议数据单元（AUX PDU）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:754`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L754)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_ADV_EVENT_INC_ON_FULL_TX_EN"></a>

## 56.39 `CONFIG_ESP32_BT_LE_CTLR_ADV_EVENT_INC_ON_FULL_TX_EN`

**提示（Prompt）**：完整发送后递增广播事件计数器（Advertising Event Counter）

**说明（Help）**

仅在完整发送一个协议数据单元（PDU）后，才递增广播事件计数器（Advertising Event Counter），而不是每次尝试发送 PDU 后都递增。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:787`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L787)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_ADV_FAST_TX_EN"></a>

## 56.40 `CONFIG_ESP32_BT_LE_CTLR_ADV_FAST_TX_EN`

**提示（Prompt）**：快速广播发送（Fast Advertising TX）

**说明（Help）**

减小广播信道上的协议数据单元间隔（Inter-PDU Spacing），以提高广播速率。功耗会更高，也可能增加共存（Coexistence）压力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:793`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L793)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_ADV_RAND_CH_IDX_EN"></a>

## 56.41 `CONFIG_ESP32_BT_LE_CTLR_ADV_RAND_CH_IDX_EN`

**提示（Prompt）**：随机化广播信道索引（Advertising Channel Index）

**说明（Help）**

随机化广播信道 37／38／39 的使用顺序，将空中占用时间（Airtime）分散到整个频段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:799`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L799)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_ADV_TX_CONTINUE_WHEN_EXCEED_ITVL_EN"></a>

## 56.42 `CONFIG_ESP32_BT_LE_CTLR_ADV_TX_CONTINUE_WHEN_EXCEED_ITVL_EN`

**提示（Prompt）**：超过间隔后继续发送广播（Continue Advertising TX Past Interval）

**说明（Help）**

配置的时间间隔到期后，继续进行已经开始的广播事件（Advertising Event），而不将其终止。这有助于提高高负载下的可靠性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:805`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L805)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_CHAN_ASS_EN"></a>

## 56.43 `CONFIG_ESP32_BT_LE_CTLR_CHAN_ASS_EN`

**提示（Prompt）**：信道评估，实验性（Channel Assessment）

**说明（Help）**

记录信道质量（Channel Quality）并定期更新信道映射（Channel Map），以提高链路可靠性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:749`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L749)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_CHECK_CONNECT_IND_ACCESS_ADDRESS"></a>

## 56.44 `CONFIG_ESP32_BT_LE_CTLR_CHECK_CONNECT_IND_ACCESS_ADDRESS`

**提示（Prompt）**：CONNECT_IND 中增强的接入地址检查（Enhanced Access Address Check）

**说明（Help）**

严格验证 `CONNECT_IND` 协议数据单元（PDU）中的接入地址（Access Address），以提高安全性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:711`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L711)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_DL_ITVL_PHY_SYNC_EN"></a>

## 56.45 `CONFIG_ESP32_BT_LE_CTLR_DL_ITVL_PHY_SYNC_EN`

**提示（Prompt）**：下行链路间隔与 PHY 同步（Downlink Interval PHY Sync）

**说明（Help）**

将下行链路间隔（Downlink Interval）与连接的物理层（PHY）同步，使频繁切换 PHY 的链路具有更精确的时序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:811`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L811)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_FAST_CONN_DATA_TX_EN"></a>

## 56.46 `CONFIG_ESP32_BT_LE_CTLR_FAST_CONN_DATA_TX_EN`

**提示（Prompt）**：快速连接数据传输（Fast Connection Data Transmission）

**说明（Help）**

发送数据后立即继续发送空协议数据单元（Empty PDU），以维持时序（Timing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:766`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L766)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_LLCP_CHAN_MAP_UPDATE"></a>

## 56.47 `CONFIG_ESP32_BT_LE_CTLR_LLCP_CHAN_MAP_UPDATE`

**提示（Prompt）**：BLE ACL 信道映射更新过程（Channel Map Update Procedure）

**说明（Help）**

启用后，如果信道映射更新过程（Channel Map Update Procedure）发生“生效时刻已过（Instant Passed）”错误 `0x28`，控制器将终止连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:724`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L724)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE ACL 配置（BLE ACL Configurations）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_LLCP_CONN_UPDATE"></a>

## 56.48 `CONFIG_ESP32_BT_LE_CTLR_LLCP_CONN_UPDATE`

**提示（Prompt）**：BLE ACL 连接更新过程（Connection Update Procedure）

**说明（Help）**

启用后，如果连接更新过程（Connection Update Procedure）发生“生效时刻已过（Instant Passed）”错误 `0x28`，控制器将终止连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:718`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L718)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE ACL 配置（BLE ACL Configurations）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_LLCP_PHY_UPDATE"></a>

## 56.49 `CONFIG_ESP32_BT_LE_CTLR_LLCP_PHY_UPDATE`

**提示（Prompt）**：BLE ACL 物理层更新过程（PHY Update Procedure）

**说明（Help）**

启用后，如果物理层更新过程（PHY Update Procedure）发生“生效时刻已过（Instant Passed）”错误 `0x28`，控制器将终止连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:730`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L730)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE ACL 配置（BLE ACL Configurations）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_CTLR_SLV_FAST_RX_CONN_DATA_EN"></a>

## 56.50 `CONFIG_ESP32_BT_LE_CTLR_SLV_FAST_RX_CONN_DATA_EN`

**提示（Prompt）**：外设延迟期间快速接收 PDU（Fast Peripheral PDU Reception）

**说明（Help）**

允许外设角色（Peripheral Role）在外设延迟（Peripheral Latency）生效期间更快接收连接数据协议数据单元（PDU），代价是电流消耗略有增加。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:817`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L817)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_ENABLE_PERIODIC_ADV"></a>

## 56.51 `CONFIG_ESP32_BT_LE_ENABLE_PERIODIC_ADV`

**提示（Prompt）**：周期性广播支持（Periodic Advertising Support）

**说明（Help）**

启用周期性广播（Periodic Advertising），以同步广播事件（Broadcast Events）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_EXT_ADV && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_ADV_PERIODIC
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:338`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L338)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 5 功能支持（Feature Support） → 扩展广播支持（Extended Advertising Support）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_EXT_ADV`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_EXT_ADV)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_ADV_PERIODIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_PERIODIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_EXT_ADV"></a>

## 56.52 `CONFIG_ESP32_BT_LE_EXT_ADV`

**提示（Prompt）**：扩展广播支持（Extended Advertising Support）

**说明（Help）**

支持 Bluetooth 5.0 的扩展广播（Extended Advertising）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_ADV_EXT
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:313`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L313)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 5 功能支持（Feature Support）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_ADV_EXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_EXT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_EXT_ADV_MAX_SIZE"></a>

## 56.53 `CONFIG_ESP32_BT_LE_EXT_ADV_MAX_SIZE`

**提示（Prompt）**：最大扩展广播数据长度（Extended Advertising Data Length）

**说明（Help）**

扩展广播数据（Extended Advertising Data）的最大长度，不超过 1650 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_EXT_ADV && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
1650
```

**取值范围（Ranges）**

```text
[0, 1650]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:331`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L331)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 5 功能支持（Feature Support） → 扩展广播支持（Extended Advertising Support）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_EXT_ADV`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_EXT_ADV)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_HCI_EVT_BUF_SIZE"></a>

## 56.54 `CONFIG_ESP32_BT_LE_HCI_EVT_BUF_SIZE`

**提示（Prompt）**：HCI 事件缓冲区大小（Event Buffer Size）

**说明（Help）**

每个主机控制器接口（HCI）事件缓冲区的大小；使用扩展广播（Extended Advertising）时应设为 257 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
257 if CONFIG_ESP32_BT_LE_EXT_ADV
70
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:459`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L459)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 内存设置（Memory Settings）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP32_BT_LE_EXT_ADV`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_EXT_ADV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_HCI_EVT_HI_BUF_COUNT"></a>

## 56.55 `CONFIG_ESP32_BT_LE_HCI_EVT_HI_BUF_COUNT`

**提示（Prompt）**：高优先级 HCI 事件缓冲区数量（High-Priority Event Buffers）

**说明（Help）**

高优先级主机控制器接口（HCI）事件缓冲区数量，不包括广播报告（Advertising Report）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:466`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L466)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 内存设置（Memory Settings）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_HCI_EVT_LO_BUF_COUNT"></a>

## 56.56 `CONFIG_ESP32_BT_LE_HCI_EVT_LO_BUF_COUNT`

**提示（Prompt）**：低优先级 HCI 事件缓冲区数量（Low-Priority Event Buffers）

**说明（Help）**

用于广播报告（Advertising Report）的低优先级主机控制器接口（HCI）事件缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:472`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L472)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 内存设置（Memory Settings）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_HCI_INTERFACE"></a>

## 56.57 `CONFIG_ESP32_BT_LE_HCI_INTERFACE`

**提示（Prompt）**：主机控制器接口模式（HCI Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_ESP32_BT_LE_HCI_INTERFACE_USE_RAM
```

**可选项（Choices）**

```text
CONFIG_ESP32_BT_LE_HCI_INTERFACE_USE_RAM
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:278`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L278)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 乐鑫 HCI 配置（Espressif HCI Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP32_BT_LE_HCI_INTERFACE_USE_RAM`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_HCI_INTERFACE_USE_RAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_HCI_INTERFACE_USE_RAM"></a>

## 56.58 `CONFIG_ESP32_BT_LE_HCI_INTERFACE_USE_RAM`

**提示（Prompt）**：虚拟主机控制器接口（VHCI）

**说明（Help）**

使用基于 RAM 的主机控制器接口（HCI）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_LE_HCI_INTERFACE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:282`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L282)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 乐鑫 HCI 配置（Espressif HCI Configuration） → 主机控制器接口模式（HCI Mode）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_HCI_INTERFACE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_HCI_INTERFACE)。

<a id="CONFIG_ESP32_BT_LE_LL_CFG_FEAT_LE_2M_PHY"></a>

## 56.59 `CONFIG_ESP32_BT_LE_LL_CFG_FEAT_LE_2M_PHY`

**提示（Prompt）**：2M 物理层支持（2M PHY Support）

**说明（Help）**

允许低功耗蓝牙（BLE）连接使用 2M 物理层（PHY），以获得更高数据速率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_PHY_2M
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:299`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L299)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 5 功能支持（Feature Support）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_PHY_2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_2M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_LL_CFG_FEAT_LE_CODED_PHY"></a>

## 56.60 `CONFIG_ESP32_BT_LE_LL_CFG_FEAT_LE_CODED_PHY`

**提示（Prompt）**：编码物理层支持（Coded PHY Support）

**说明（Help）**

启用编码物理层（LE Coded PHY），用于扩大低功耗蓝牙（BLE）连接的通信范围。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_PHY_CODED
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:306`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L306)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 5 功能支持（Feature Support）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_PHY_CODED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_CODED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_LL_CFG_FEAT_LE_ENCRYPTION"></a>

## 56.61 `CONFIG_ESP32_BT_LE_LL_CFG_FEAT_LE_ENCRYPTION`

**提示（Prompt）**：低功耗蓝牙加密（LE Encryption）

**说明（Help）**

支持低功耗蓝牙（BLE）连接的链路层加密（Link-Layer Encryption）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_SECURITY_ENABLE && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_LE_ENC
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:520`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L520)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙安全管理器（BLE Security Manager）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_SECURITY_ENABLE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SECURITY_ENABLE)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_LE_ENC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_ENC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_LL_DUP_SCAN_LIST_COUNT"></a>

## 56.62 `CONFIG_ESP32_BT_LE_LL_DUP_SCAN_LIST_COUNT`

**提示（Prompt）**：重复扫描列表条目数量（Duplicate Scan List Count）

**说明（Help）**

重复扫描列表（Duplicate Scan List）的最大条目数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[5, 100]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:551`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L551)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_LL_PEER_SCA"></a>

## 56.63 `CONFIG_ESP32_BT_LE_LL_PEER_SCA`

**提示（Prompt）**：固定的对端休眠时钟精度值（Constant Peer Sleep Clock Accuracy）

**说明（Help）**

设置对端设备的休眠时钟精度（Sleep Clock Accuracy）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_LL_PEER_SCA_SET_ENABLE && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10000]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:572`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L572)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 使用固定的对端休眠时钟精度（Constant Peer SCA）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_LL_PEER_SCA_SET_ENABLE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_LL_PEER_SCA_SET_ENABLE)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_LL_PEER_SCA_SET_ENABLE"></a>

## 56.64 `CONFIG_ESP32_BT_LE_LL_PEER_SCA_SET_ENABLE`

**提示（Prompt）**：使用固定的对端休眠时钟精度（Constant Peer SCA）

**说明（Help）**

启用固定的对端休眠时钟精度（SCA）设置；当对端设备的 SCA 大于 500 ppm 时使用。启用后，控制器始终将 `ESP32_BT_LE_LL_PEER_SCA` 用作对端 SCA，计算接收窗口扩展（Window Widening），而不使用从对端收到的值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:565`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L565)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_LL_RESOLV_LIST_SIZE"></a>

## 56.65 `CONFIG_ESP32_BT_LE_LL_RESOLV_LIST_SIZE`

**提示（Prompt）**：BLE 地址解析列表大小（Resolving List Size）

**说明（Help）**

链路层地址解析列表（Link-Layer Resolving List）的条目数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:486`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L486)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_LL_SCA"></a>

## 56.66 `CONFIG_ESP32_BT_LE_LL_SCA`

**提示（Prompt）**：BLE 休眠时钟精度，单位为 ppm（Sleep Clock Accuracy）

**说明（Help）**

休眠时钟精度（Sleep Clock Accuracy），以百万分之一（Parts Per Million，ppm）为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
60
```

**取值范围（Ranges）**

```text
[0, 500]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:558`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L558)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_LP_CLK_SRC"></a>

## 56.67 `CONFIG_ESP32_BT_LE_LP_CLK_SRC`

**提示（Prompt）**：低功耗蓝牙低功耗时钟源（BLE Low-Power Clock Source）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_ESP32_BT_LE_LP_CLK_SRC_MAIN_XTAL
```

**可选项（Choices）**

```text
CONFIG_ESP32_BT_LE_LP_CLK_SRC_MAIN_XTAL
CONFIG_ESP32_BT_LE_LP_CLK_SRC_DEFAULT
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:620`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L620)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP32_BT_LE_LP_CLK_SRC_MAIN_XTAL`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_LP_CLK_SRC_MAIN_XTAL)、[`CONFIG_ESP32_BT_LE_LP_CLK_SRC_DEFAULT`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_LP_CLK_SRC_DEFAULT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_LP_CLK_SRC_DEFAULT"></a>

## 56.68 `CONFIG_ESP32_BT_LE_LP_CLK_SRC_DEFAULT`

**提示（Prompt）**：系统 RTC 低速时钟（RTC Slow Clock）

**说明（Help）**

使用系统实时时钟（RTC）的低速时钟源；由于精度较低，仅支持传统广播／扫描（Legacy ADV / SCAN）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_LE_LP_CLK_SRC>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:629`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L629)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙低功耗时钟源（BLE Low-Power Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_LP_CLK_SRC`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_LP_CLK_SRC)。

<a id="CONFIG_ESP32_BT_LE_LP_CLK_SRC_MAIN_XTAL"></a>

## 56.69 `CONFIG_ESP32_BT_LE_LP_CLK_SRC_MAIN_XTAL`

**提示（Prompt）**：将主晶体用作 RTC 时钟（Main XTAL as RTC Clock）

**说明（Help）**

没有外部 32.768 kHz 晶体时，使用主晶体（Main XTAL）作为实时时钟（RTC）的时钟源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_LE_LP_CLK_SRC>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:624`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L624)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙低功耗时钟源（BLE Low-Power Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_LP_CLK_SRC`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_LP_CLK_SRC)。

<a id="CONFIG_ESP32_BT_LE_MAX_CONNECTIONS"></a>

## 56.70 `CONFIG_ESP32_BT_LE_MAX_CONNECTIONS`

**提示（Prompt）**：最大并发连接数量（Max Concurrent Connections）

**说明（Help）**

低功耗蓝牙（BLE）的最大连接数量。每个连接约使用 1 KB 动态 RAM（DRAM）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
2 if CONFIG_SOC_SERIES_ESP32C2
3 if CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2
```

**取值范围（Ranges）**

```text
[1, 2] if CONFIG_SOC_SERIES_ESP32C2
[1, 35] if CONFIG_SOC_SERIES_ESP32H2
[1, 70] if CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:580`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L580)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_MAX_EXT_ADV_INSTANCES"></a>

## 56.71 `CONFIG_ESP32_BT_LE_MAX_EXT_ADV_INSTANCES`

**提示（Prompt）**：最大扩展广播实例数量（Extended Advertising Instances）

**说明（Help）**

扩展广播实例（Extended Advertising Instance）的数量，至少为 1。每个实例约使用 0.5 KB 动态 RAM（DRAM）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_EXT_ADV && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_BT_EXT_ADV_MAX_ADV_SET if CONFIG_BT_EXT_ADV
4 if CONFIG_BT_HCI_RAW
1
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:322`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L322)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 5 功能支持（Feature Support） → 扩展广播支持（Extended Advertising Support）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_EXT_ADV`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_EXT_ADV)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_EXT_ADV_MAX_ADV_SET`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV_MAX_ADV_SET)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_MAX_PERIODIC_ADVERTISER_LIST"></a>

## 56.72 `CONFIG_ESP32_BT_LE_MAX_PERIODIC_ADVERTISER_LIST`

**提示（Prompt）**：周期性广播发布者列表的最大条目数量（Periodic Advertiser List Entries）

**说明（Help）**

周期性广播发布者列表（Periodic Advertiser List）的数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:367`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L367)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 5 功能支持（Feature Support）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_MAX_PERIODIC_SYNCS"></a>

## 56.73 `CONFIG_ESP32_BT_LE_MAX_PERIODIC_SYNCS`

**提示（Prompt）**：最大周期性广播同步数量（Periodic Advertising Syncs）

**说明（Help）**

周期性广播同步连接（Periodic Advertising Sync Connection）的数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_BT_PER_ADV_SYNC_MAX if CONFIG_BT_PER_ADV_SYNC
3 if CONFIG_BT_HCI_RAW && CONFIG_SOC_SERIES_ESP32C2
8 if CONFIG_BT_HCI_RAW
1 if CONFIG_ESP32_BT_LE_ENABLE_PERIODIC_ADV
0
```

**取值范围（Ranges）**

```text
[0, 3] if CONFIG_SOC_SERIES_ESP32C2
[0, 8] if CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:353`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L353)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 5 功能支持（Feature Support）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_PER_ADV_SYNC_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC_MAX)、[`CONFIG_BT_PER_ADV_SYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)、[`CONFIG_ESP32_BT_LE_ENABLE_PERIODIC_ADV`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_ENABLE_PERIODIC_ADV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_MSYS_1_BLOCK_COUNT"></a>

## 56.74 `CONFIG_ESP32_BT_LE_MSYS_1_BLOCK_COUNT`

**提示（Prompt）**：MSYS_1 块数量（Block Count）

**说明（Help）**

MSYS_1 池中用于准备写入（Prepare Write）和响应（Response）的块数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
12
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:415`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L415)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 内存设置（Memory Settings）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_MSYS_1_BLOCK_SIZE"></a>

## 56.75 `CONFIG_ESP32_BT_LE_MSYS_1_BLOCK_SIZE`

**提示（Prompt）**：MSYS_1 块大小（Block Size）

**说明（Help）**

MSYS_1 池中每个块（Block）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:421`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L421)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 内存设置（Memory Settings）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_MSYS_2_BLOCK_COUNT"></a>

## 56.76 `CONFIG_ESP32_BT_LE_MSYS_2_BLOCK_COUNT`

**提示（Prompt）**：MSYS_2 块数量（Block Count）

**说明（Help）**

MSYS_2 池中的块（Block）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
24
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:427`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L427)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 内存设置（Memory Settings）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_MSYS_2_BLOCK_SIZE"></a>

## 56.77 `CONFIG_ESP32_BT_LE_MSYS_2_BLOCK_SIZE`

**提示（Prompt）**：MSYS_2 块大小（Block Size）

**说明（Help）**

MSYS_2 池中每个块（Block）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
320
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:433`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L433)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 内存设置（Memory Settings）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_MSYS_BUF_FROM_HEAP"></a>

## 56.78 `CONFIG_ESP32_BT_LE_MSYS_BUF_FROM_HEAP`

**提示（Prompt）**：从堆分配 MSYS mbuf（Mbuf from Heap）

**说明（Help）**

设置后，从堆（Heap）分配 MSYS 内存缓冲（mbuf），而不是从内存池（Mempool）分配。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6) && CONFIG_ESP32_BT_LE_MSYS_INIT_IN_CONTROLLER && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:439`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L439)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 内存设置（Memory Settings）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_ESP32_BT_LE_MSYS_INIT_IN_CONTROLLER`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_MSYS_INIT_IN_CONTROLLER)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_MSYS_INIT_IN_CONTROLLER"></a>

## 56.79 `CONFIG_ESP32_BT_LE_MSYS_INIT_IN_CONTROLLER`

**提示（Prompt）**：在控制器中初始化 MSYS mbuf（Init in Controller）

**说明（Help）**

在控制器（Controller）内部分配 MSYS 内存缓冲（mbuf），而不是在主机（Host）中分配。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:690`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L690)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32C2`。

<a id="CONFIG_ESP32_BT_LE_PERIODIC_ADV_SYNC_TRANSFER"></a>

## 56.80 `CONFIG_ESP32_BT_LE_PERIODIC_ADV_SYNC_TRANSFER`

**提示（Prompt）**：周期性同步事件传递（Periodic Sync Event Transfer）

**说明（Help）**

允许控制器（Controller）向主机（Host）传递周期性同步事件（Periodic Sync Event）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_ENABLE_PERIODIC_ADV && CONFIG_ESP32_BT_LE_EXT_ADV && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER || CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:344`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L344)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 5 功能支持（Feature Support） → 扩展广播支持（Extended Advertising Support） → 周期性广播支持（Periodic Advertising Support）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_ENABLE_PERIODIC_ADV`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_ENABLE_PERIODIC_ADV)、[`CONFIG_ESP32_BT_LE_EXT_ADV`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_EXT_ADV)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER)、[`CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_PERIODIC_ADV_WITH_RESPONSE_ENABLED"></a>

## 56.81 `CONFIG_ESP32_BT_LE_PERIODIC_ADV_WITH_RESPONSE_ENABLED`

**提示（Prompt）**：带响应周期性广播，BLE 5.4（Periodic Advertising with Responses，PAwR）

**说明（Help）**

启用 Bluetooth 5.4 带响应周期性广播（Periodic Advertising with Responses），在周期性广播序列（Periodic Advertising Train）中实现双向通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_ESP32_BT_LE_ENABLE_PERIODIC_ADV && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_ADV_PERIODIC_RSP
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:403`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L403)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_ESP32_BT_LE_ENABLE_PERIODIC_ADV`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_ENABLE_PERIODIC_ADV)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_ADV_PERIODIC_RSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_PERIODIC_RSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32C2`。

<a id="CONFIG_ESP32_BT_LE_POWER_CONTROL_ENABLED"></a>

## 56.82 `CONFIG_ESP32_BT_LE_POWER_CONTROL_ENABLED`

**提示（Prompt）**：控制器 BLE 功率控制（Controller BLE Power Control）

**说明（Help）**

允许控制器根据链路质量（Link Quality）调整发射功率（Transmit Power）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_LE_POWER_CONTROL
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:375`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L375)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 5 功能支持（Feature Support）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_LE_POWER_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_POWER_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32C2`。

<a id="CONFIG_ESP32_BT_LE_RXBUF_OPT_ENABLED"></a>

## 56.83 `CONFIG_ESP32_BT_LE_RXBUF_OPT_ENABLED`

**提示（Prompt）**：接收缓冲区优化（RX Buffer Optimization）

**说明（Help）**

优化接收缓冲区（RX Buffer）分配，以减少主机内存用量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:760`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L760)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_SCAN_DUPL"></a>

## 56.84 `CONFIG_ESP32_BT_LE_SCAN_DUPL`

**提示（Prompt）**：BLE 扫描重复过滤（Scan Duplicate Filtering）

**说明（Help）**

启用扫描过滤器（Scanning Filter），避免重复报告相同广播（Duplicate Advertisement）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:644`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L644)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32C2`。

<a id="CONFIG_ESP32_BT_LE_SCAN_DUPL_CACHE_REFRESH_PERIOD"></a>

## 56.85 `CONFIG_ESP32_BT_LE_SCAN_DUPL_CACHE_REFRESH_PERIOD`

**提示（Prompt）**：重复缓存刷新周期，单位为秒（Duplicate Cache Refresh Period）

**说明（Help）**

清除重复扫描缓存（Duplicate Scan Cache）的时间间隔，单位为秒。设为 0 时禁用周期性清除。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_SCAN_DUPL && (CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 1000]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:682`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L682)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 扫描重复过滤（Scan Duplicate Filtering）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_SCAN_DUPL`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SCAN_DUPL)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32C2`。

<a id="CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE"></a>

## 56.86 `CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE`

**提示（Prompt）**：扫描重复过滤类型（Scan Duplicate Filter Type）

**说明（Help）**

选择重复扫描结果（Duplicate Scan Results）的过滤方法。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_SCAN_DUPL && (CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DEVICE
```

**可选项（Choices）**

```text
CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DEVICE
CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DATA
CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DATA_DEVICE
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:650`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L650)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 扫描重复过滤（Scan Duplicate Filtering）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_SCAN_DUPL`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SCAN_DUPL)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DEVICE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DEVICE)、[`CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DATA`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DATA)、[`CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DATA_DEVICE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DATA_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32C2`。

<a id="CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DATA"></a>

## 56.87 `CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DATA`

**提示（Prompt）**：按广播数据过滤（By Advertising Data）

**说明（Help）**

仅按广播数据（Advertising Data）过滤重复项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:662`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L662)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 扫描重复过滤（Scan Duplicate Filtering） → 扫描重复过滤类型（Scan Duplicate Filter Type）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE)。

<a id="CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DATA_DEVICE"></a>

## 56.88 `CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DATA_DEVICE`

**提示（Prompt）**：按地址和数据过滤（By Address and Data）

**说明（Help）**

同时按设备地址（Device Address）和广播数据（Advertising Data）过滤重复项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:667`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L667)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 扫描重复过滤（Scan Duplicate Filtering） → 扫描重复过滤类型（Scan Duplicate Filter Type）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE)。

<a id="CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DEVICE"></a>

## 56.89 `CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE_DEVICE`

**提示（Prompt）**：按设备地址过滤（By Device Address）

**说明（Help）**

仅按设备地址（Device Address）过滤重复项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:657`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L657)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 扫描重复过滤（Scan Duplicate Filtering） → 扫描重复过滤类型（Scan Duplicate Filter Type）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SCAN_DUPL_TYPE)。

<a id="CONFIG_ESP32_BT_LE_SECURITY_ENABLE"></a>

## 56.90 `CONFIG_ESP32_BT_LE_SECURITY_ENABLE`

**提示（Prompt）**：低功耗蓝牙安全管理器（BLE Security Manager）

**说明（Help）**

启用安全管理器（Security Manager）功能，以进行低功耗蓝牙（BLE）配对（Pairing）和加密（Encryption）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CRYPTO && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_LE_ENC
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:493`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L493)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CRYPTO)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_LE_ENC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_ENC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_SLEEP_CLOCK_ACCURACY_INDEX_EFF"></a>

## 56.91 `CONFIG_ESP32_BT_LE_SLEEP_CLOCK_ACCURACY_INDEX_EFF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

低功耗蓝牙（BLE）休眠时钟精度（SCA）索引，其中 1 对应 151–250 ppm。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_LE_SLEEP_ENABLE"></a>

## 56.92 `CONFIG_ESP32_BT_LE_SLEEP_ENABLE`

**提示（Prompt）**：低功耗蓝牙休眠模式（BLE Sleep Mode）

**说明（Help）**

允许控制器在空闲期间进入低功耗休眠（Low-Power Sleep）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && CONFIG_TICKLESS_KERNEL && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MAC_BB_PD if CONFIG_SOC_SERIES_ESP32C6
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:612`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L612)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_MAC_BB_PD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAC_BB_PD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_SM_LEGACY"></a>

## 56.93 `CONFIG_ESP32_BT_LE_SM_LEGACY`

**提示（Prompt）**：传统配对（Legacy Pairing）

**说明（Help）**

使用传统配对过程（Legacy Pairing Procedure），即 Bluetooth 4.2 之前的方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_SECURITY_ENABLE && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_SMP && !CONFIG_BT_SMP_SC_PAIR_ONLY
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:500`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L500)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙安全管理器（BLE Security Manager）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_SECURITY_ENABLE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SECURITY_ENABLE)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_SMP_SC_PAIR_ONLY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP_SC_PAIR_ONLY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_SM_SC"></a>

## 56.94 `CONFIG_ESP32_BT_LE_SM_SC`

**提示（Prompt）**：低功耗安全连接（Secure Connections，LE SC）

**说明（Help）**

使用安全连接配对（Secure Connections Pairing），适用于 Bluetooth 4.2 及更新版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_SECURITY_ENABLE && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_SMP
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:507`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L507)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙安全管理器（BLE Security Manager）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_SECURITY_ENABLE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SECURITY_ENABLE)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_SM_SC_DEBUG_KEYS"></a>

## 56.95 `CONFIG_ESP32_BT_LE_SM_SC_DEBUG_KEYS`

**提示（Prompt）**：预定义的 DH 密钥对（Predefined DH Key Pair）

**说明（Help）**

为 Diffie–Hellman（DH）密钥交换使用预定义调试密钥（Debug Keys），仅用于测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_SECURITY_ENABLE && CONFIG_ESP32_BT_LE_SM_SC && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:514`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L514)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙安全管理器（BLE Security Manager） → 低功耗安全连接（Secure Connections，LE SC）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_SECURITY_ENABLE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SECURITY_ENABLE)、[`CONFIG_ESP32_BT_LE_SM_SC`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SM_SC)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_SUBRATE_ENABLED"></a>

## 56.96 `CONFIG_ESP32_BT_LE_SUBRATE_ENABLED`

**提示（Prompt）**：连接子速率，原文标为 BLE 5.2（Connection Subrating）

**说明（Help）**

启用原文标注为 Bluetooth 5.2 的连接子速率（Connection Subrating），根据与对端协商的子速率因子（Subrate Factor）跳过连接事件，以降低已建立链路的功耗。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_SUBRATING
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:384`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L384)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 5 功能支持（Feature Support）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_50_FEATURE_SUPPORT)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_CTLR_SUBRATING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SUBRATING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32C2`。

<a id="CONFIG_ESP32_BT_LE_TX_CCA_ENABLED"></a>

## 56.97 `CONFIG_ESP32_BT_LE_TX_CCA_ENABLED`

**提示（Prompt）**：发送空闲信道评估功能（TX CCA Feature）

**说明（Help）**

当接收信号强度指示（RSSI）超过空闲信道评估（CCA）阈值时，取消数据包发送。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:698`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L698)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_USE_ESP_TIMER"></a>

## 56.98 `CONFIG_ESP32_BT_LE_USE_ESP_TIMER`

**提示（Prompt）**：使用 esp-timer 执行定时回调（Callouts）

**说明（Help）**

使用高优先级 `esp-timer` 执行控制器定时回调（Controller Callouts）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:636`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L636)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_LE_WHITELIST_SIZE"></a>

## 56.99 `CONFIG_ESP32_BT_LE_WHITELIST_SIZE`

**提示（Prompt）**：BLE 白名单大小（Whitelist Size）

**说明（Help）**

低功耗蓝牙（BLE）白名单（Whitelist）的条目数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
12
```

**取值范围（Ranges）**

```text
[1, 31]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:544`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L544)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP_BT_HEAP"></a>

## 56.100 `CONFIG_ESP_BT_HEAP`

**提示（Prompt）**：蓝牙堆类型（Bluetooth Heap Type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_ESP_BT_HEAP_SYSTEM
```

**可选项（Choices）**

```text
CONFIG_ESP_BT_HEAP_SYSTEM
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP_BT_HEAP_SYSTEM`](P057_drivers_bluetooth_配置项参考_4.md#CONFIG_ESP_BT_HEAP_SYSTEM)。

<!-- kconfig-navigation -->

[上一章](P055_drivers_bluetooth_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P057_drivers_bluetooth_配置项参考_4.md)
