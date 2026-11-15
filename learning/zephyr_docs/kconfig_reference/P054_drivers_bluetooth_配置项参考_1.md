---
id: learning.zephyr-docs.kconfig-reference.page-54
title: "`drivers/bluetooth`配置项参考（1/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第54章\_`drivers/bluetooth`配置项参考（1/4）

本章翻译官方 Kconfig 数据库中 `drivers/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_AIROC_AUTOBAUD_MODE"></a>

## 54.1 `CONFIG_AIROC_AUTOBAUD_MODE`

**提示（Prompt）**：自动波特率模式（Autobaud Mode）

**说明（Help）**

使用 AIROC 控制器（Controller）的自动波特率（Autobaud）功能加快固件下载。CYW555xx 等较新的 AIROC 控制器，仅允许在恢复复位（Recovery Reset）之后进入下载模式（Download Mode）上传固件。在下载模式下，最初无法使用厂商专用的波特率命令（Baud Rate Vendor Command）；自动波特率模式则允许直接使用较高波特率。较旧的 AIROC 控制器不需要此模式。更多信息见[AIROC HCI 固件下载官方文档](https://infineon.github.io/btsdk-docs/BT-SDK/AIROC-HCI-Firmware-Download.pdf)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AIROC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:269`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L269)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_AIROC_CUSTOM_FIRMWARE_HCD_BLOB"></a>

## 54.2 `CONFIG_AIROC_CUSTOM_FIRMWARE_HCD_BLOB`

**提示（Prompt）**：用户蓝牙固件 HCD 文件路径（BT Firmware HCD File Path）

**说明（Help）**

自定义或厂商 CYW43xx 模块的蓝牙（BT）固件 HCD 文件路径。可以是绝对路径，也可以是相对于项目目录的路径。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AIROC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:263`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L263)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_AIROC_PART"></a>

## 54.3 `CONFIG_AIROC_PART`

原库同名定义共 2 条；本项为数据库第 396 条记录，各定义分别保留。

**提示（Prompt）**：选择 AIROC 器件（AIROC Part）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AIROC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**可选项（Choices）**

```text
CONFIG_CYW4343W
CONFIG_CYW4373
CONFIG_CYW43012
CONFIG_CYW43438
CONFIG_CYW43439
CONFIG_CYW20829
CONFIG_BT_AIROC_CUSTOM
CONFIG_CYW4343W
CONFIG_CYW4373
CONFIG_CYW43012
CONFIG_CYW43022
CONFIG_CYW43438
CONFIG_CYW43439
CONFIG_CYW55500
CONFIG_CYW55572
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_CYW4343W`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW4343W)、[`CONFIG_CYW4373`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW4373)、[`CONFIG_CYW43012`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW43012)、[`CONFIG_CYW43438`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW43438)、[`CONFIG_CYW43439`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW43439)、[`CONFIG_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW20829)、[`CONFIG_BT_AIROC_CUSTOM`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC_CUSTOM)、[`CONFIG_CYW43022`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW43022)、[`CONFIG_CYW55500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW55500)、[`CONFIG_CYW55572`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW55572)。

<a id="CONFIG_BFLB_BL60X_BLE_M1S1"></a>

## 54.4 `CONFIG_BFLB_BL60X_BLE_M1S1`

**提示（Prompt）**：m1s1：中心设备与外设，各 1 个连接（Central + Peripheral）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL60X_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL60X_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL60X_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL60X_BLE_M8S1"></a>

## 54.5 `CONFIG_BFLB_BL60X_BLE_M8S1`

**提示（Prompt）**：m8s1：8 个中心设备连接与 1 个外设连接（Central + Peripheral）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL60X_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL60X_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL60X_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL60X_BLE_VARIANT"></a>

## 54.6 `CONFIG_BFLB_BL60X_BLE_VARIANT`

**提示（Prompt）**：低功耗蓝牙控制器变体（BLE Controller Variant）

**说明（Help）**

选择低功耗蓝牙（BLE）控制器的二进制变体（Binary Variant）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BFLB_BL60X && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_BFLB_BL60X_BLE_M8S1 if CONFIG_BT_HCI_RAW
CONFIG_BFLB_BL60X_BLE_M8S1 if CONFIG_BT_PERIPHERAL && CONFIG_BT_CENTRAL
CONFIG_BFLB_BL60X_BLE_M1S1 if CONFIG_BT_PERIPHERAL
CONFIG_BFLB_BL60X_BLE_M8S1
```

**可选项（Choices）**

```text
CONFIG_BFLB_BL60X_BLE_M1S1
CONFIG_BFLB_BL60X_BLE_M8S1
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL60X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL60X)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BFLB_BL60X_BLE_M8S1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL60X_BLE_M8S1)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)、[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BFLB_BL60X_BLE_M1S1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL60X_BLE_M1S1)。

<a id="CONFIG_BFLB_BL616CL_BLE_M0B1"></a>

## 54.7 `CONFIG_BFLB_BL616CL_BLE_M0B1`

**提示（Prompt）**：m0b1：仅广播／信标变体（Advertising / Beacon Only）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL616CL_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:377`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L377)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL616CL_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL616CL_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL616CL_BLE_M2S1"></a>

## 54.8 `CONFIG_BFLB_BL616CL_BLE_M2S1`

**提示（Prompt）**：m2s1：中心设备与外设，2 个连接（Central + Peripheral）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL616CL_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:374`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L374)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL616CL_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL616CL_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL616CL_BLE_VARIANT"></a>

## 54.9 `CONFIG_BFLB_BL616CL_BLE_VARIANT`

**提示（Prompt）**：低功耗蓝牙控制器变体（BLE Controller Variant）

**说明（Help）**

选择低功耗蓝牙（BLE）控制器的二进制变体（Binary Variant）。默认值根据已启用的蓝牙角色（Bluetooth Roles）自动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BFLB_BL616CL && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_BFLB_BL616CL_BLE_M2S1 if CONFIG_BT_CENTRAL || CONFIG_BT_PERIPHERAL || CONFIG_BT_OBSERVER
CONFIG_BFLB_BL616CL_BLE_M0B1
```

**可选项（Choices）**

```text
CONFIG_BFLB_BL616CL_BLE_M2S1
CONFIG_BFLB_BL616CL_BLE_M0B1
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:366`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L366)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL616CL`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL616CL)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BFLB_BL616CL_BLE_M2S1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL616CL_BLE_M2S1)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BFLB_BL616CL_BLE_M0B1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL616CL_BLE_M0B1)。

<a id="CONFIG_BFLB_BL61X_BLE_1M0S1"></a>

## 54.10 `CONFIG_BFLB_BL61X_BLE_1M0S1`

**提示（Prompt）**：ble1m0s1bredr0：仅外设，1 个连接（Peripheral Only）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL61X_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:321`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L321)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL61X_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL61X_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL61X_BLE_1M10S1"></a>

## 54.11 `CONFIG_BFLB_BL61X_BLE_1M10S1`

**提示（Prompt）**：ble1m10s1bredr0：外设与中心设备，10 个连接（Peripheral + Central）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL61X_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:324`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L324)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL61X_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL61X_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL61X_BLE_1M2S1BREDR1"></a>

## 54.12 `CONFIG_BFLB_BL61X_BLE_1M2S1BREDR1`

**提示（Prompt）**：ble1m2s1bredr1：外设、中心设备及 BR/EDR，2 个连接（Peripheral + Central + BR/EDR）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL61X_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:327`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L327)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL61X_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL61X_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL61X_BLE_EM_64K"></a>

## 54.13 `CONFIG_BFLB_BL61X_BLE_EM_64K`

**提示（Prompt）**：使用 64 KB 交换内存，BR/EDR 必需（Exchange Memory）

**说明（Help）**

为低功耗蓝牙（BLE）交换内存预留 64 KB 的 WRAM，而不是默认的 32 KB。基本速率／增强数据速率（BR/EDR）变体要求这样配置。开发板设备树源码（DTS）必须包含 `bl61x_em_64kb.dtsi`，而不是 `bl61x_em_32kb.dtsi`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BFLB_BL61X && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BFLB_BL61X_BLE_1M2S1BREDR1
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:342`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L342)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL61X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL61X)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BFLB_BL61X_BLE_1M2S1BREDR1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL61X_BLE_1M2S1BREDR1)。

<a id="CONFIG_BFLB_BL61X_BLE_VARIANT"></a>

## 54.14 `CONFIG_BFLB_BL61X_BLE_VARIANT`

**提示（Prompt）**：低功耗蓝牙控制器变体（BLE Controller Variant）

**说明（Help）**

选择低功耗蓝牙（BLE）控制器的二进制变体（Binary Variant）。默认值根据已启用的蓝牙角色（Bluetooth Roles）自动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BFLB_BL61X && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_BFLB_BL61X_BLE_1M10S1 if CONFIG_BT_HCI_RAW
CONFIG_BFLB_BL61X_BLE_1M2S1BREDR1 if CONFIG_BT_CLASSIC
CONFIG_BFLB_BL61X_BLE_1M10S1 if CONFIG_BT_PERIPHERAL && CONFIG_BT_CENTRAL
CONFIG_BFLB_BL61X_BLE_1M0S1 if CONFIG_BT_PERIPHERAL
CONFIG_BFLB_BL61X_BLE_1M10S1
```

**可选项（Choices）**

```text
CONFIG_BFLB_BL61X_BLE_1M0S1
CONFIG_BFLB_BL61X_BLE_1M10S1
CONFIG_BFLB_BL61X_BLE_1M2S1BREDR1
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:310`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L310)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL61X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL61X)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BFLB_BL61X_BLE_1M10S1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL61X_BLE_1M10S1)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)、[`CONFIG_BFLB_BL61X_BLE_1M2S1BREDR1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL61X_BLE_1M2S1BREDR1)、[`CONFIG_BT_CLASSIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CLASSIC)、[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BFLB_BL61X_BLE_1M0S1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL61X_BLE_1M0S1)。

<a id="CONFIG_BFLB_BL70XL_BLE_EM_16K"></a>

## 54.15 `CONFIG_BFLB_BL70XL_BLE_EM_16K`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为低功耗蓝牙（BLE）控制器使用 16KB 交换内存（Exchange Memory）。仅 `m8s1p` 变体，即 8 个连接时需要。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BFLB_BL70XL && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BFLB_BL70XL_BLE_M8S1P
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:270`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L270)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL70XL`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL70XL)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BFLB_BL70XL_BLE_M8S1P`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_M8S1P)。

<a id="CONFIG_BFLB_BL70XL_BLE_M0S1P"></a>

## 54.16 `CONFIG_BFLB_BL70XL_BLE_M0S1P`

**提示（Prompt）**：m0s1p：仅外设，1 个连接（Peripheral Only）

**说明（Help）**

1 个低功耗蓝牙（BLE）连接，仅支持从设备／外设（Slave / Peripheral）。全部控制器代码位于闪存（Flash）中，支持断电休眠（PDS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70XL_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:212`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L212)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70XL_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70XL_BLE_M0S1RP"></a>

## 54.17 `CONFIG_BFLB_BL70XL_BLE_M0S1RP`

**提示（Prompt）**：m0s1rp：仅外设，1 个连接，使用 ROM 代码（Peripheral Only, ROM Code）

**说明（Help）**

1 个低功耗蓝牙（BLE）连接，仅支持从设备／外设（Slave / Peripheral）。部分控制器代码位于 ROM 中，以减少闪存（Flash）占用。要求 A1 芯片版本，支持断电休眠（PDS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BFLB_BL70XL_REV_A1 && <choice CONFIG_BFLB_BL70XL_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70XL_REV_A1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_REV_A1)、[`CONFIG_BFLB_BL70XL_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70XL_BLE_M0S1SP"></a>

## 54.18 `CONFIG_BFLB_BL70XL_BLE_M0S1SP`

**提示（Prompt）**：m0s1sp：外设与观察者，1 个连接（Peripheral + Observer）

**说明（Help）**

1 个低功耗蓝牙（BLE）连接，支持从设备／外设（Slave / Peripheral）及观察者／扫描器（Observer / Scanner）。全部控制器代码位于闪存（Flash）中，支持断电休眠（PDS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70XL_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:225`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L225)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70XL_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70XL_BLE_M0S2P"></a>

## 54.19 `CONFIG_BFLB_BL70XL_BLE_M0S2P`

**提示（Prompt）**：m0s2p：仅外设，2 个连接（Peripheral Only）

**说明（Help）**

2 个低功耗蓝牙（BLE）连接，仅支持从设备／外设（Slave / Peripheral）。全部控制器代码位于闪存（Flash）中，支持断电休眠（PDS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70XL_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:231`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L231)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70XL_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70XL_BLE_M0S4P"></a>

## 54.20 `CONFIG_BFLB_BL70XL_BLE_M0S4P`

**提示（Prompt）**：m0s4p：仅外设，4 个连接（Peripheral Only）

**说明（Help）**

4 个低功耗蓝牙（BLE）连接，仅支持从设备／外设（Slave / Peripheral）。全部控制器代码位于闪存（Flash）中，支持断电休眠（PDS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70XL_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:237`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L237)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70XL_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70XL_BLE_M1S1P"></a>

## 54.21 `CONFIG_BFLB_BL70XL_BLE_M1S1P`

**提示（Prompt）**：m1s1p：所有角色，1 个连接（All Roles）

**说明（Help）**

1 个低功耗蓝牙（BLE）连接，可作为主设备（Master）或从设备（Slave）。全部控制器代码位于闪存（Flash）中，支持断电休眠（PDS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70XL_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:243`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L243)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70XL_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70XL_BLE_M2S1P"></a>

## 54.22 `CONFIG_BFLB_BL70XL_BLE_M2S1P`

**提示（Prompt）**：m2s1p：所有角色，2 个连接（All Roles）

**说明（Help）**

2 个低功耗蓝牙（BLE）连接，可作为主设备（Master）或从设备（Slave）。全部控制器代码位于闪存（Flash）中，支持断电休眠（PDS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70XL_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:249`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L249)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70XL_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70XL_BLE_M4S1P"></a>

## 54.23 `CONFIG_BFLB_BL70XL_BLE_M4S1P`

**提示（Prompt）**：m4s1p：所有角色，4 个连接（All Roles）

**说明（Help）**

4 个低功耗蓝牙（BLE）连接，可作为主设备（Master）或从设备（Slave）。全部控制器代码位于闪存（Flash）中，支持断电休眠（PDS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70XL_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:255`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L255)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70XL_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70XL_BLE_M8S1P"></a>

## 54.24 `CONFIG_BFLB_BL70XL_BLE_M8S1P`

**提示（Prompt）**：m8s1p：所有角色，8 个连接（All Roles）

**说明（Help）**

8 个低功耗蓝牙（BLE）连接，可作为主设备（Master）或从设备（Slave）。全部控制器代码位于闪存（Flash）中，支持断电休眠（PDS）。使用 16KB 交换内存（Exchange Memory），其他变体则使用 8KB。必须在设备树源码（DTS）中通过 `sram0_bt_em16k` 正确配置内存大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70XL_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:261`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L261)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70XL_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70XL_BLE_VARIANT"></a>

## 54.25 `CONFIG_BFLB_BL70XL_BLE_VARIANT`

**提示（Prompt）**：低功耗蓝牙控制器变体（BLE Controller Variant）

**说明（Help）**

选择低功耗蓝牙（BLE）控制器的二进制变体（Binary Variant），决定最大连接数量、支持的角色及功能。命名规则为 `m<master>s<slave>[suffix]`：其中 `m` 表示最大主设备连接数量，`s` 表示最大从设备连接数量；后缀 `p` 表示断电休眠（Power Down Sleep，PDS），`r` 表示 ROM 代码，`s` 表示扫描／观察者（Scan / Observer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BFLB_BL70XL && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_BFLB_BL70XL_BLE_M8S1P if CONFIG_BT_HCI_RAW
CONFIG_BFLB_BL70XL_BLE_M8S1P if CONFIG_BT_CENTRAL && CONFIG_BT_PERIPHERAL
CONFIG_BFLB_BL70XL_BLE_M0S1SP if !CONFIG_BT_CONN && CONFIG_BT_OBSERVER
CONFIG_BFLB_BL70XL_BLE_M0S1SP if CONFIG_BT_PERIPHERAL && CONFIG_BT_OBSERVER && CONFIG_BT_MAX_CONN = 1
CONFIG_BFLB_BL70XL_BLE_M0S1P if CONFIG_BT_PERIPHERAL && CONFIG_BT_MAX_CONN = 1
CONFIG_BFLB_BL70XL_BLE_M1S1P
```

**可选项（Choices）**

```text
CONFIG_BFLB_BL70XL_BLE_M0S1P
CONFIG_BFLB_BL70XL_BLE_M0S1RP
CONFIG_BFLB_BL70XL_BLE_M0S1SP
CONFIG_BFLB_BL70XL_BLE_M0S2P
CONFIG_BFLB_BL70XL_BLE_M0S4P
CONFIG_BFLB_BL70XL_BLE_M1S1P
CONFIG_BFLB_BL70XL_BLE_M2S1P
CONFIG_BFLB_BL70XL_BLE_M4S1P
CONFIG_BFLB_BL70XL_BLE_M8S1P
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:197`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L197)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL70XL`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL70XL)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BFLB_BL70XL_BLE_M8S1P`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_M8S1P)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BFLB_BL70XL_BLE_M0S1SP`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_M0S1SP)、[`CONFIG_BT_CONN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CONN)、[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_MAX_CONN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_CONN)、[`CONFIG_BFLB_BL70XL_BLE_M0S1P`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_M0S1P)、[`CONFIG_BFLB_BL70XL_BLE_M1S1P`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_M1S1P)、[`CONFIG_BFLB_BL70XL_BLE_M0S1RP`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_M0S1RP)、[`CONFIG_BFLB_BL70XL_BLE_M0S2P`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_M0S2P)、[`CONFIG_BFLB_BL70XL_BLE_M0S4P`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_M0S4P)、[`CONFIG_BFLB_BL70XL_BLE_M2S1P`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_M2S1P)、[`CONFIG_BFLB_BL70XL_BLE_M4S1P`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_BLE_M4S1P)。

<a id="CONFIG_BFLB_BL70XL_REV_A0"></a>

## 54.26 `CONFIG_BFLB_BL70XL_REV_A0`

**提示（Prompt）**：A0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70XL_SILICON_REV>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BL70XL 芯片修订版本（Silicon Revision）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70XL_SILICON_REV`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_SILICON_REV)。

<a id="CONFIG_BFLB_BL70XL_REV_A1"></a>

## 54.27 `CONFIG_BFLB_BL70XL_REV_A1`

**提示（Prompt）**：A1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70XL_SILICON_REV>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BL70XL 芯片修订版本（Silicon Revision）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70XL_SILICON_REV`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_SILICON_REV)。

<a id="CONFIG_BFLB_BL70XL_SILICON_REV"></a>

## 54.28 `CONFIG_BFLB_BL70XL_SILICON_REV`

**提示（Prompt）**：BL70XL 芯片修订版本（Silicon Revision）

**说明（Help）**

选择 BL70XL 芯片修订版本（Silicon Revision），决定低功耗蓝牙（BLE）控制器二进制块（Binary Blob）使用的 ROM 数据地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BFLB_BL70XL && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_BFLB_BL70XL_REV_A1
```

**可选项（Choices）**

```text
CONFIG_BFLB_BL70XL_REV_A0
CONFIG_BFLB_BL70XL_REV_A1
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L182)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL70XL`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL70XL)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BFLB_BL70XL_REV_A1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_REV_A1)、[`CONFIG_BFLB_BL70XL_REV_A0`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70XL_REV_A0)。

<a id="CONFIG_BFLB_BL70X_BLE_EM_16K"></a>

## 54.29 `CONFIG_BFLB_BL70X_BLE_EM_16K`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为低功耗蓝牙（BLE）控制器使用 16KB 交换内存（Exchange Memory）。仅 `m16s1` 变体需要。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BFLB_BL70X && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BFLB_BL70X_BLE_M16S1
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL70X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL70X)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BFLB_BL70X_BLE_M16S1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_M16S1)。

<a id="CONFIG_BFLB_BL70X_BLE_M0S0SP"></a>

## 54.30 `CONFIG_BFLB_BL70X_BLE_M0S0SP`

**提示（Prompt）**：m0s0sp：仅观察者，无连接（Observer Only）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70X_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70X_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70X_BLE_M0S1"></a>

## 54.31 `CONFIG_BFLB_BL70X_BLE_M0S1`

**提示（Prompt）**：m0s1：仅外设，1 个连接，不支持 PDS（Peripheral Only, No PDS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70X_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70X_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70X_BLE_M0S1P"></a>

## 54.32 `CONFIG_BFLB_BL70X_BLE_M0S1P`

**提示（Prompt）**：m0s1p：仅外设，1 个连接（Peripheral Only）

**说明（Help）**

1 个低功耗蓝牙（BLE）连接，仅支持从设备／外设（Slave / Peripheral）。支持断电休眠（PDS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70X_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70X_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70X_BLE_M0S1S"></a>

## 54.33 `CONFIG_BFLB_BL70X_BLE_M0S1S`

**提示（Prompt）**：m0s1s：外设与观察者，1 个连接（Peripheral + Observer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70X_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70X_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70X_BLE_M0S1T10"></a>

## 54.34 `CONFIG_BFLB_BL70X_BLE_M0S1T10`

**提示（Prompt）**：m0s1t10：外设，1 个连接，测试模式（Peripheral, Test Mode）

**说明（Help）**

1 个低功耗蓝牙（BLE）连接，仅支持从设备／外设（Slave / Peripheral）。用于测试／制造模式（Test / Manufacturing Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70X_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70X_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70X_BLE_M16S1"></a>

## 54.35 `CONFIG_BFLB_BL70X_BLE_M16S1`

**提示（Prompt）**：m16s1：所有角色，16 个主设备连接与 1 个从设备连接（All Roles）

**说明（Help）**

16 个中心设备（Central）连接与 1 个外设（Peripheral）连接。使用 16KB 交换内存（Exchange Memory），其他变体则使用 8KB。必须在设备树源码（DTS）中通过 `sram0_bt_em16k` 正确配置内存大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70X_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70X_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70X_BLE_M1S1"></a>

## 54.36 `CONFIG_BFLB_BL70X_BLE_M1S1`

**提示（Prompt）**：m1s1：中心设备与外设，各 1 个连接（Central + Peripheral）

**说明（Help）**

1 个主设备（Master）连接与 1 个从设备（Slave）低功耗蓝牙（BLE）连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BFLB_BL70X_BLE_VARIANT>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 低功耗蓝牙控制器变体（BLE Controller Variant）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_BL70X_BLE_VARIANT`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_VARIANT)。

<a id="CONFIG_BFLB_BL70X_BLE_VARIANT"></a>

## 54.37 `CONFIG_BFLB_BL70X_BLE_VARIANT`

**提示（Prompt）**：低功耗蓝牙控制器变体（BLE Controller Variant）

**说明（Help）**

选择低功耗蓝牙（BLE）控制器的二进制变体（Binary Variant）。默认值根据已启用的蓝牙角色自动选择。命名规则为 `m<master>s<slave>[suffix]`：其中 `m` 表示最大主设备连接数量，`s` 表示最大从设备连接数量；后缀 `p` 表示断电休眠（Power Down Sleep，PDS），`s` 表示扫描／观察者（Scan / Observer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BFLB_BL70X && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_BFLB_BL70X_BLE_M16S1 if CONFIG_BT_HCI_RAW
CONFIG_BFLB_BL70X_BLE_M16S1 if CONFIG_BT_PERIPHERAL && CONFIG_BT_CENTRAL
CONFIG_BFLB_BL70X_BLE_M0S0SP if !CONFIG_BT_CONN && CONFIG_BT_OBSERVER
CONFIG_BFLB_BL70X_BLE_M0S1S if CONFIG_BT_PERIPHERAL && CONFIG_BT_OBSERVER
CONFIG_BFLB_BL70X_BLE_M0S1P if CONFIG_BT_PERIPHERAL
CONFIG_BFLB_BL70X_BLE_M16S1
```

**可选项（Choices）**

```text
CONFIG_BFLB_BL70X_BLE_M0S1P
CONFIG_BFLB_BL70X_BLE_M0S1
CONFIG_BFLB_BL70X_BLE_M0S1S
CONFIG_BFLB_BL70X_BLE_M0S1T10
CONFIG_BFLB_BL70X_BLE_M0S0SP
CONFIG_BFLB_BL70X_BLE_M1S1
CONFIG_BFLB_BL70X_BLE_M16S1
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL70X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL70X)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BFLB_BL70X_BLE_M16S1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_M16S1)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)、[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BFLB_BL70X_BLE_M0S0SP`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_M0S0SP)、[`CONFIG_BT_CONN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CONN)、[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BFLB_BL70X_BLE_M0S1S`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_M0S1S)、[`CONFIG_BFLB_BL70X_BLE_M0S1P`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_M0S1P)、[`CONFIG_BFLB_BL70X_BLE_M0S1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_M0S1)、[`CONFIG_BFLB_BL70X_BLE_M0S1T10`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_M0S1T10)、[`CONFIG_BFLB_BL70X_BLE_M1S1`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BFLB_BL70X_BLE_M1S1)。

<a id="CONFIG_BT_AIROC"></a>

## 54.38 `CONFIG_BT_AIROC`

**提示（Prompt）**：AIROC 蓝牙连接功能（BT Connectivity）

**说明（Help）**

英飞凌（Infineon）的 AIROC™ Wi-Fi 与组合连接产品系列，在单芯片方案中集成 IEEE 802.11a/b/g/n/ac/ax Wi-Fi 和 Bluetooth® 5.2，以支持小尺寸物联网（IoT）设计。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_INFINEON_BT_HCI_UART_ENABLED || DT_HAS_INFINEON_CYW208XX_HCI_ENABLED) && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO if CONFIG_BT_H4
CONFIG_UART_USE_RUNTIME_CONFIGURE if CONFIG_BT_H4
CONFIG_BT_H4_VND_OPEN if CONFIG_BT_H4
CONFIG_BT_HCI_SET_PUBLIC_ADDR
CONFIG_USE_INFINEON_ABSTRACTION_RTOS if CONFIG_BT_CYW208XX
CONFIG_EVENTS if CONFIG_BT_CYW208XX
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:275`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L275)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_BT_H4`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_USE_RUNTIME_CONFIGURE)、[`CONFIG_BT_H4_VND_OPEN`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4_VND_OPEN)、[`CONFIG_BT_HCI_SET_PUBLIC_ADDR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_SET_PUBLIC_ADDR)、[`CONFIG_USE_INFINEON_ABSTRACTION_RTOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_ABSTRACTION_RTOS)、[`CONFIG_BT_CYW208XX`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_CYW208XX)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_BT_AIROC_CUSTOM"></a>

## 54.39 `CONFIG_BT_AIROC_CUSTOM`

**提示（Prompt）**：自定义 AIROC 器件／模块（Custom Device / Module）

**说明（Help）**

选择自定义 AIROC 器件／模块。使用此选项时，用户必须通过 `AIROC_CUSTOM_FIRMWARE_HCD_BLOB` 提供自定义或厂商 AIROC 模块的蓝牙（BT）固件 HCD 文件路径。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AIROC_PART>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)。

<a id="CONFIG_BT_AMBIQ_HCI"></a>

## 54.40 `CONFIG_BT_AMBIQ_HCI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

支持使用 SPI 作为通信协议（Communication Protocol）的 Ambiq 蓝牙片上系统（Bluetooth SoC）。主机控制器接口（HCI）数据包以逐个字节传输的方式发送和接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_BT_HCI_SPI_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_GPIO if CONFIG_SOC_SERIES_APOLLO4X
CONFIG_CLOCK_CONTROL if CONFIG_SOC_SERIES_APOLLO4X
CONFIG_AMBIQ_COMPONENT_USE_BT
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:244`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L244)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_SOC_SERIES_APOLLO4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL)、[`CONFIG_AMBIQ_COMPONENT_USE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_COMPONENT_USE_BT)。

<a id="CONFIG_BT_AMEBA"></a>

## 54.41 `CONFIG_BT_AMEBA`

**提示（Prompt）**：AMEBA 蓝牙 HCI 驱动（BT HCI Driver）

**说明（Help）**

AMEBA 蓝牙 HCI 驱动（BT HCI Driver）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_BT_HCI_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_BEE"></a>

## 54.42 `CONFIG_BT_BEE`

**提示（Prompt）**：瑞昱 Bee 系列蓝牙 HCI 驱动（Realtek BT HCI Driver）

**说明（Help）**

启用瑞昱（Realtek）Bee 片上系统（SoC）的蓝牙主机控制器接口（BT HCI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_BT_HCI_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_BT
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bee:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bee#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_HAL_REALTEK_BEE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_BT`。

<a id="CONFIG_BT_BEE_HCI_H2C_POOL_SIZE"></a>

## 54.43 `CONFIG_BT_BEE_HCI_H2C_POOL_SIZE`

**提示（Prompt）**：HCI 主机到控制器池大小（H2C Pool Size）

**说明（Help）**

HCI H2C 池（Host-to-Controller Pool）用于主机控制器接口（HCI）命令包和异步连接逻辑传输（ACL）数据包。根据低功耗（LE）ACL 数据包最大数量和 HCI 命令包最大数量设置此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BEE && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
3072
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bee:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bee#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 瑞昱 Bee 系列蓝牙 HCI 驱动（Realtek BT HCI Driver）

**配置项引用（Symbol References）**：[`CONFIG_BT_BEE`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BEE)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_BFLB"></a>

## 54.44 `CONFIG_BT_BFLB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

所有博流（Bouffalo Lab）片上低功耗蓝牙（BLE）控制器的共用符号，由各 SoC 专用的主机控制器接口（HCI）驱动配置自动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_HWINFO
```

**被选择（Selected by）**

```text
CONFIG_BT_BFLB_BL60X
CONFIG_BT_BFLB_BL70X
CONFIG_BT_BFLB_BL70XL
CONFIG_BT_BFLB_BL61X
CONFIG_BT_BFLB_BL616CL
CONFIG_BT_BFLB_BL808
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_HWINFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HWINFO)、[`CONFIG_BT_BFLB_BL60X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL60X)、[`CONFIG_BT_BFLB_BL70X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL70X)、[`CONFIG_BT_BFLB_BL70XL`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL70XL)、[`CONFIG_BT_BFLB_BL61X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL61X)、[`CONFIG_BT_BFLB_BL616CL`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL616CL)、[`CONFIG_BT_BFLB_BL808`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL808)。

<a id="CONFIG_BT_BFLB_BL60X"></a>

## 54.45 `CONFIG_BT_BFLB_BL60X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

博流（Bouffalo Lab）BL60X（BL602）片上低功耗蓝牙（BLE）控制器的主机控制器接口（HCI）驱动，使用 `hal_bouffalolab` 模块提供的预编译二进制块（Precompiled Binary Blobs）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BT_HCI_ENABLED && CONFIG_SOC_SERIES_BL60X && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_BFLB
CONFIG_HAS_BT_CTLR
CONFIG_DYNAMIC_INTERRUPTS
CONFIG_FPU_SHARING
CONFIG_BFLB_FREERTOS_SHIM
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_BFLB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)、[`CONFIG_BFLB_FREERTOS_SHIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_FREERTOS_SHIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_BFLB_BL616CL"></a>

## 54.46 `CONFIG_BT_BFLB_BL616CL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

博流（Bouffalo Lab）BL616CL 片上低功耗蓝牙（BLE）控制器的主机控制器接口（HCI）驱动，使用 `hal_bouffalolab` 模块提供的预编译二进制块（Precompiled Binary Blobs）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BT_HCI_ENABLED && CONFIG_SOC_SERIES_BL616CL && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_BFLB
CONFIG_HAS_BT_CTLR
CONFIG_FPU_SHARING
CONFIG_BFLB_BTBLE_PORT_OS_SHIM
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:352`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L352)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_BFLB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)、[`CONFIG_BFLB_BTBLE_PORT_OS_SHIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_BTBLE_PORT_OS_SHIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_BFLB_BL61X"></a>

## 54.47 `CONFIG_BT_BFLB_BL61X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

博流（Bouffalo Lab）BL61X（BL616 / BL618）片上低功耗蓝牙（BLE）控制器的主机控制器接口（HCI）驱动，使用 `hal_bouffalolab` 模块提供的预编译二进制块（Precompiled Binary Blobs）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BT_HCI_ENABLED && CONFIG_SOC_SERIES_BL61X && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_BFLB
CONFIG_HAS_BT_CTLR
CONFIG_FPU_SHARING
CONFIG_BFLB_BTBLE_PORT_OS_SHIM
CONFIG_BFLB_PHYRF
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:295`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L295)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_BFLB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)、[`CONFIG_BFLB_BTBLE_PORT_OS_SHIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_BTBLE_PORT_OS_SHIM)、[`CONFIG_BFLB_PHYRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_PHYRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_BFLB_BL70X"></a>

## 54.48 `CONFIG_BT_BFLB_BL70X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

博流（Bouffalo Lab）BL70X（BL702）片上低功耗蓝牙（BLE）控制器的主机控制器接口（HCI）驱动，使用 `hal_bouffalolab` 模块提供的预编译二进制块（Precompiled Binary Blobs）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BT_HCI_ENABLED && CONFIG_SOC_SERIES_BL70X && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_BFLB
CONFIG_HAS_BT_CTLR
CONFIG_DYNAMIC_INTERRUPTS
CONFIG_FPU_SHARING
CONFIG_BFLB_FREERTOS_SHIM
CONFIG_BFLB_PHYRF
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_BFLB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)、[`CONFIG_BFLB_FREERTOS_SHIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_FREERTOS_SHIM)、[`CONFIG_BFLB_PHYRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_PHYRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_BFLB_BL70XL"></a>

## 54.49 `CONFIG_BT_BFLB_BL70XL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

博流（Bouffalo Lab）BL70XL 片上低功耗蓝牙（BLE）控制器的主机控制器接口（HCI）驱动，使用 `hal_bouffalolab` 模块提供的预编译二进制块（Precompiled Binary Blobs）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BT_HCI_ENABLED && CONFIG_SOC_SERIES_BL70XL && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_BFLB
CONFIG_HAS_BT_CTLR
CONFIG_DYNAMIC_INTERRUPTS
CONFIG_FPU_SHARING
CONFIG_BFLB_BTBLE_PORT_OS_SHIM
CONFIG_BFLB_PHYRF
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_BFLB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)、[`CONFIG_BFLB_BTBLE_PORT_OS_SHIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_BTBLE_PORT_OS_SHIM)、[`CONFIG_BFLB_PHYRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_PHYRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_BFLB_BL808"></a>

## 54.50 `CONFIG_BT_BFLB_BL808`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

博流（Bouffalo Lab）BL808 片上低功耗蓝牙（BLE）控制器的主机控制器接口（HCI）驱动，使用 `hal_bouffalolab` 模块提供的预编译二进制块（Precompiled Binary Blobs）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BT_HCI_ENABLED && CONFIG_SOC_SERIES_BL808 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_BFLB
CONFIG_HAS_BT_CTLR
CONFIG_DYNAMIC_INTERRUPTS
CONFIG_FPU_SHARING
CONFIG_BFLB_AOS_SHIM
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:390`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L390)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_BFLB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)、[`CONFIG_BFLB_AOS_SHIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_AOS_SHIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_BFLB_CTLR_TASK_PRIO"></a>

## 54.51 `CONFIG_BT_BFLB_CTLR_TASK_PRIO`

**提示（Prompt）**：BLE 控制器任务优先级，采用 FreeRTOS 风格（Task Priority）

**说明（Help）**

传给低功耗蓝牙（BLE）控制器初始化函数的优先级。实时操作系统适配层（RTOS Shim Layer）会将其映射为 Zephyr 抢占式优先级（Preemptive Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BFLB && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_BFLB_RX_THREAD_STACK_SIZE"></a>

## 54.52 `CONFIG_BT_BFLB_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：BLE HCI 接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

主机控制器接口（HCI）接收处理线程的栈大小。`recv()` 回调会进入主机协议栈（Host）代码，因此应根据需要调整。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BFLB && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.bflb:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.bflb#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_BLUENRG_ACI"></a>

## 54.53 `CONFIG_BT_BLUENRG_ACI`

**提示（Prompt）**：与 BlueNRG 器件通信的 ACI 消息（ACI Message）

**说明（Help）**

启用兼容 BlueNRG 蓝牙协议栈（Bluetooth Stack）的器件支持。目前驱动支持 ST BLUENRG-MS。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SPI_BLUENRG && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_BT_HCI_SET_PUBLIC_ADDR
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/x_nucleo_bnrg2a1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_bnrg2a1/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/x_nucleo_idb05a1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_idb05a1/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/x_nucleo_wb05kn1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_wb05kn1/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/x_nucleo_wba25a1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_wba25a1/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_SPI_BLUENRG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SPI_BLUENRG)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_HCI_SET_PUBLIC_ADDR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_SET_PUBLIC_ADDR)。

<a id="CONFIG_BT_CTLR_SCAN_BACKOFF_UPPERLIMITMAX"></a>

## 54.54 `CONFIG_BT_CTLR_SCAN_BACKOFF_UPPERLIMITMAX`

**提示（Prompt）**：扫描退避上限值（Scan Backoff Upper Limit）

**说明（Help）**

扫描退避过程（Scan Backoff Procedure）的 `Upperlimitmax` 值，取 2 的幂。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:737`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L737)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_BT_CYW208XX"></a>

## 54.55 `CONFIG_BT_CYW208XX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

英飞凌 CYW208XX HCI 蓝牙接口（Infineon HCI Bluetooth Interface）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_CYW208XX_HCI_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_HCI_SET_PUBLIC_ADDR
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:236`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L236)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_HCI_SET_PUBLIC_ADDR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_SET_PUBLIC_ADDR)。

<a id="CONFIG_BT_CYW555XX"></a>

## 54.56 `CONFIG_BT_CYW555XX`

**提示（Prompt）**：CYW555XX 蓝牙支持（Bluetooth Support）

**说明（Help）**

基于 CYW555XX 的设计所共用的蓝牙配置，包括村田（Murata）2FY 模块和分立芯片实现（Discrete Chip Implementations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AIROC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_CYW55513_MURATA_2FY || CONFIG_CYW55513IUBG_SM
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_CYW55513_MURATA_2FY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW55513_MURATA_2FY)、[`CONFIG_CYW55513IUBG_SM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW55513IUBG_SM)。

<a id="CONFIG_BT_DA1453X"></a>

## 54.57 `CONFIG_BT_DA1453X`

**提示（Prompt）**：DA1453x 主机控制器接口驱动（HCI Driver）

**说明（Help）**

用于与运行在 DA1453x 微控制器（MCU）上的控制器通信的蓝牙主机控制器接口（Bluetooth HCI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_BT_HCI_DA1453X_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_BT_DA1469X"></a>

## 54.58 `CONFIG_BT_DA1469X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于与 DA1469x 微控制器（MCU）上的 CMAC 内核通信的蓝牙主机控制器接口（Bluetooth HCI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_BT_HCI_DA1469X_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:220`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L220)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_DRIVERS"></a>

## 54.59 `CONFIG_BT_DRIVERS`

**提示（Prompt）**：蓝牙驱动（Bluetooth Drivers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_DRIVER_QUIRK_NO_AUTO_DLE"></a>

## 54.60 `CONFIG_BT_DRIVER_QUIRK_NO_AUTO_DLE`

**提示（Prompt）**：主机自动发起数据长度更新的兼容处理（Data Length Update Quirk）

**说明（Help）**

启用以下兼容处理（Quirk）：当默认数据长度参数与初始参数不同，而控制器不会自动发起数据长度更新过程（Data Length Update Procedure）时，由蓝牙主机协议栈（BT Host Stack）为新连接自动发起该过程。连接的低功耗蓝牙（BLE）控制器为 Zephyr 开源控制器时，必须启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUTO_DATA_LEN_UPDATE && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HCI_IPC || CONFIG_BT_ESP32
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:297`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L297)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUTO_DATA_LEN_UPDATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUTO_DATA_LEN_UPDATE)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_HCI_IPC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_IPC)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)。

<a id="CONFIG_BT_DRV_RX_STACK_SIZE"></a>

## 54.61 `CONFIG_BT_DRV_RX_STACK_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

主机控制器接口（HCI）驱动接收线程（RX Thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
640 if CONFIG_BT_SPI || CONFIG_BT_AMBIQ_HCI
CONFIG_BT_RX_STACK_SIZE if CONFIG_BT_H4
CONFIG_BT_STM32_IPM_RX_STACK_SIZE if CONFIG_BT_STM32_IPM
CONFIG_HCI_NXP_RX_STACK_SIZE if CONFIG_HCI_NXP_RX_THREAD
1024 if CONFIG_BT_SF32LB
1024 if CONFIG_BT_BFLB
512
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:358`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L358)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SPI)、[`CONFIG_BT_AMBIQ_HCI`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AMBIQ_HCI)、[`CONFIG_BT_RX_STACK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RX_STACK_SIZE)、[`CONFIG_BT_H4`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4)、[`CONFIG_BT_STM32_IPM_RX_STACK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_STM32_IPM_RX_STACK_SIZE)、[`CONFIG_BT_STM32_IPM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_STM32_IPM)、[`CONFIG_HCI_NXP_RX_STACK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HCI_NXP_RX_STACK_SIZE)、[`CONFIG_HCI_NXP_RX_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HCI_NXP_RX_THREAD)、[`CONFIG_BT_SF32LB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_SF32LB)、[`CONFIG_BT_BFLB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB)。

<a id="CONFIG_BT_DRV_TX_STACK_SIZE"></a>

## 54.62 `CONFIG_BT_DRV_TX_STACK_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

主机控制器接口（HCI）驱动发送线程（TX Thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:352`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L352)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_ESP32"></a>

## 54.63 `CONFIG_BT_ESP32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

乐鑫 HCI 蓝牙接口（Espressif HCI Bluetooth Interface）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_BT_HCI_ENABLED && (CONFIG_ZEPHYR_HAL_ESPRESSIF_MODULE_BLOBS || CONFIG_BUILD_ONLY_NO_BLOBS) && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_BT_CTLR
CONFIG_BT_CTLR_LE_ENC_SUPPORT
CONFIG_BT_CTLR_PRIVACY_SUPPORT
CONFIG_BT_CTLR_EXT_SCAN_FP_SUPPORT
CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT
CONFIG_BT_CTLR_CONN_RSSI_SUPPORT
CONFIG_BT_CTLR_ADV_EXT_SUPPORT if !CONFIG_SOC_SERIES_ESP32
CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT if !CONFIG_SOC_SERIES_ESP32
CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT if !CONFIG_SOC_SERIES_ESP32
CONFIG_BT_CTLR_PHY_2M_SUPPORT if !CONFIG_SOC_SERIES_ESP32
CONFIG_BT_CTLR_PHY_CODED_SUPPORT if !CONFIG_SOC_SERIES_ESP32
CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT if !CONFIG_SOC_SERIES_ESP32
CONFIG_BT_CTLR_ADV_PERIODIC_SUPPORT if !CONFIG_SOC_SERIES_ESP32
CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT if !CONFIG_SOC_SERIES_ESP32
CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT if !CONFIG_SOC_SERIES_ESP32
CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT if !CONFIG_SOC_SERIES_ESP32
CONFIG_BT_CTLR_ADV_PERIODIC_RSP_SUPPORT if CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2
CONFIG_BT_CTLR_LE_POWER_CONTROL_SUPPORT if CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2
CONFIG_BT_CTLR_SUBRATING_SUPPORT if CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ESPRESSIF_MODULE_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ESPRESSIF_MODULE_BLOBS)、[`CONFIG_BUILD_ONLY_NO_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_ONLY_NO_BLOBS)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_LE_ENC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_ENC_SUPPORT)、[`CONFIG_BT_CTLR_PRIVACY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PRIVACY_SUPPORT)、[`CONFIG_BT_CTLR_EXT_SCAN_FP_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_EXT_SCAN_FP_SUPPORT)、[`CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT)、[`CONFIG_BT_CTLR_CONN_RSSI_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_RSSI_SUPPORT)、[`CONFIG_BT_CTLR_ADV_EXT_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_EXT_SUPPORT)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT)、[`CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT)、[`CONFIG_BT_CTLR_PHY_2M_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_2M_SUPPORT)、[`CONFIG_BT_CTLR_PHY_CODED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_CODED_SUPPORT)、[`CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT)、[`CONFIG_BT_CTLR_ADV_PERIODIC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_PERIODIC_SUPPORT)、[`CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT)、[`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT)、[`CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT)、[`CONFIG_BT_CTLR_ADV_PERIODIC_RSP_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_PERIODIC_RSP_SUPPORT)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_CTLR_LE_POWER_CONTROL_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_POWER_CONTROL_SUPPORT)、[`CONFIG_BT_CTLR_SUBRATING_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SUBRATING_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ESPRESSIF_MODULE_BLOBS`、`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_LE_ENC_SUPPORT`、`CONFIG_BT_CTLR_PRIVACY_SUPPORT`、`CONFIG_BT_CTLR_EXT_SCAN_FP_SUPPORT`、`CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT`、`CONFIG_BT_CTLR_CONN_RSSI_SUPPORT`、`CONFIG_BT_CTLR_ADV_EXT_SUPPORT`、`CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT`、`CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT`、`CONFIG_BT_CTLR_PHY_2M_SUPPORT`、`CONFIG_BT_CTLR_PHY_CODED_SUPPORT`、`CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT`、`CONFIG_BT_CTLR_ADV_PERIODIC_SUPPORT`、`CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT`、`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT`、`CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT`、`CONFIG_BT_CTLR_ADV_PERIODIC_RSP_SUPPORT`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_BT_CTLR_LE_POWER_CONTROL_SUPPORT`、`CONFIG_BT_CTLR_SUBRATING_SUPPORT`。

<a id="CONFIG_BT_FW_EXPECTED_VERSION_MAJOR"></a>

## 54.64 `CONFIG_BT_FW_EXPECTED_VERSION_MAJOR`

**提示（Prompt）**：预期的 STM32WB 无线固件主版本号（Major Version）

**说明（Help）**

预期的 STM32WB 无线固件主版本号（Major Version）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_STM32_IPM_FW_INFO_CHECK && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.stm32:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.stm32#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → STM32WB 无线固件运行时检查（Runtime Check）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32_IPM_FW_INFO_CHECK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_STM32_IPM_FW_INFO_CHECK)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_FW_EXPECTED_VERSION_MINOR"></a>

## 54.65 `CONFIG_BT_FW_EXPECTED_VERSION_MINOR`

**提示（Prompt）**：预期的 STM32WB 无线固件次版本号（Minor Version）

**说明（Help）**

预期的 STM32WB 无线固件次版本号（Minor Version）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_STM32_IPM_FW_INFO_CHECK && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.stm32:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.stm32#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → STM32WB 无线固件运行时检查（Runtime Check）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32_IPM_FW_INFO_CHECK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_STM32_IPM_FW_INFO_CHECK)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_FW_EXPECTED_VERSION_SUB"></a>

## 54.66 `CONFIG_BT_FW_EXPECTED_VERSION_SUB`

**提示（Prompt）**：预期的 STM32WB 无线固件子版本号（Sub Version）

**说明（Help）**

预期的 STM32WB 无线固件子版本号（Sub Version）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_STM32_IPM_FW_INFO_CHECK && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.stm32:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.stm32#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → STM32WB 无线固件运行时检查（Runtime Check）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32_IPM_FW_INFO_CHECK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_STM32_IPM_FW_INFO_CHECK)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_H4"></a>

## 54.67 `CONFIG_BT_H4`

**提示（Prompt）**：H:4 通用异步收发器（UART）

**说明（Help）**

蓝牙 H:4 UART 驱动，要求具备硬件流量控制线（Hardware Flow Control Lines）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_BT_HCI_UART_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_UART
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_ieee802154/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_ieee802154/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_UART)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_UART`。

<a id="CONFIG_BT_H4_NXP_CTLR"></a>

## 54.68 `CONFIG_BT_H4_NXP_CTLR`

**提示（Prompt）**：恩智浦蓝牙控制器（NXP Bluetooth Controller）

**说明（Help）**

启用恩智浦蓝牙控制器（NXP Bluetooth Controller）支持。更多产品信息见[恩智浦无线连接产品页面](https://www.nxp.com/products/wireless-connectivity/wi-fi-plus-bluetooth-plus-802-15-4:WIFI-BLUETOOTH)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4 && DT_HAS_NXP_BT_HCI_UART_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_CRC
CONFIG_BT_H4_VND_OPEN
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_ieee802154/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_ieee802154/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:370`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L370)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)、[`CONFIG_BT_H4_VND_OPEN`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4_VND_OPEN)。

<a id="CONFIG_BT_H4_NXP_CTLR_WAIT_HDR_SIG_TIMEOUT"></a>

## 54.69 `CONFIG_BT_H4_NXP_CTLR_WAIT_HDR_SIG_TIMEOUT`

**提示（Prompt）**：等待 HDR 签名的超时时间（HDR Signature Timeout）

**说明（Help）**

等待 HDR 签名（Signature）的超时时间，单位为毫秒。

译注：上游将 Signature 拼写为 Signure，此处按签名含义翻译。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4_NXP_CTLR && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
2500
```

**取值范围（Ranges）**

```text
[1000, 60000]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:385`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L385)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 恩智浦蓝牙控制器（NXP Bluetooth Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4_NXP_CTLR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4_NXP_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_H4_NXP_CTLR_WAIT_TIME_AFTER_BAUDRATE_UPDATE"></a>

## 54.70 `CONFIG_BT_H4_NXP_CTLR_WAIT_TIME_AFTER_BAUDRATE_UPDATE`

**提示（Prompt）**：控制器波特率更新后的等待时间（Baud Rate Update Wait）

**说明（Help）**

控制器波特率（Baud Rate）更新后的等待时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4_NXP_CTLR && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
500
```

**取值范围（Ranges）**

```text
[500, 5000]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:399`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L399)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 恩智浦蓝牙控制器（NXP Bluetooth Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4_NXP_CTLR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4_NXP_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_H4_NXP_CTLR_WAIT_TIME_AFTER_UPLOAD"></a>

## 54.71 `CONFIG_BT_H4_NXP_CTLR_WAIT_TIME_AFTER_UPLOAD`

**提示（Prompt）**：固件上传后的等待时间（Firmware Upload Wait）

**说明（Help）**

固件（Firmware）上传后的等待时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4_NXP_CTLR && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[1000, 5000]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:392`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L392)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 恩智浦蓝牙控制器（NXP Bluetooth Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4_NXP_CTLR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4_NXP_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_H4_VND_OPEN"></a>

## 54.72 `CONFIG_BT_H4_VND_OPEN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由实现 `bt_h4_vnd_open()` 的 H:4 厂商扩展（Vendor Extension）选择。H:4 驱动在打开传输通道（Transport）时调用该函数，使扩展能够利用锁步辅助机制（Lockstep Helper），通过主机控制器接口（HCI）配置控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**被选择（Selected by）**

```text
CONFIG_BT_AIROC
CONFIG_BT_H4_NXP_CTLR
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → H:4 通用异步收发器（UART）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_H4_NXP_CTLR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4_NXP_CTLR)。

<a id="CONFIG_BT_H5"></a>

## 54.73 `CONFIG_BT_H5`

**提示（Prompt）**：H:5 UART［实验性，EXPERIMENTAL］

**说明（Help）**

蓝牙三线（H:5）UART 驱动，实现主机控制器接口三线 UART 传输层（HCI Three-Wire UART Transport Layer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_BT_HCI_3WIRE_UART_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_UART
CONFIG_EXPERIMENTAL
CONFIG_BT_SYSTEM_WORKQUEUE_COOP
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_UART)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_SYSTEM_WORKQUEUE_COOP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SYSTEM_WORKQUEUE_COOP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_UART`。

<a id="CONFIG_BT_HCI_ESP_HOSTED_MCU"></a>

## 54.74 `CONFIG_BT_HCI_ESP_HOSTED_MCU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

蓝牙主机控制器接口（Bluetooth HCI）驱动，用于外部乐鑫（Espressif）协处理器上的控制器，该协处理器运行 `esp-hosted-mcu` 固件。通过共用的 `esp-hosted-mcu` 传输通道，即 SPI 或 SDIO，以 HCI H4 帧访问控制器；这也是 Wi-Fi 使用的同一条链路。

协处理器是独立器件，因此蓝牙能力由该器件决定，而不由当前主机决定。ESP32-C2、C3、C5、C6、H2 或 S3 协处理器提供 Bluetooth 5.0 低功耗（LE）控制器；ESP32 提供 Bluetooth 4.2 LE 和基本速率／增强数据速率（BR/EDR），但不支持扩展广播（Extended Advertising）。应按实际使用的协处理器选择主机特性（Host Features）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP_HOSTED_MCU_BT_HCI_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ESP_HOSTED_MCU
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:950`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L950)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP_HOSTED_MCU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_HOSTED_MCU)。

<a id="CONFIG_BT_HCI_ESP_HOSTED_MCU_RX_PRIO"></a>

## 54.75 `CONFIG_BT_HCI_ESP_HOSTED_MCU_RX_PRIO`

**提示（Prompt）**：esp-hosted-mcu HCI 接收线程协作式优先级（Cooperative Priority）

**说明（Help）**

esp-hosted-mcu 主机控制器接口（HCI）接收线程的协作式优先级（Cooperative Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_ESP_HOSTED_MCU && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:995`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L995)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_ESP_HOSTED_MCU`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_ESP_HOSTED_MCU)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_HCI_ESP_HOSTED_MCU_RX_STACK_SIZE"></a>

## 54.76 `CONFIG_BT_HCI_ESP_HOSTED_MCU_RX_STACK_SIZE`

**提示（Prompt）**：esp-hosted-mcu HCI 接收线程栈大小（Receive Thread Stack Size）

**说明（Help）**

重建并递送已接收主机控制器接口（HCI）帧的线程栈大小。将递送工作移出共用的 `esp-hosted-mcu` 接收线程，以免等待主机缓冲区池（Host Buffer Pool）时阻塞 Wi-Fi 路径。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_ESP_HOSTED_MCU && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:987`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L987)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_ESP_HOSTED_MCU`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_ESP_HOSTED_MCU)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_HCI_INIT_PRIORITY"></a>

## 54.77 `CONFIG_BT_HCI_INIT_PRIORITY`

**提示（Prompt）**：蓝牙 HCI 初始化优先级（BT HCI Init Priority）

**说明（Help）**

蓝牙主机控制器接口（BT HCI）驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
75 if CONFIG_BT_AMBIQ_HCI
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:263`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L263)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_AMBIQ_HCI`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AMBIQ_HCI)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_BT_HCI_IPC"></a>

## 54.78 `CONFIG_BT_HCI_IPC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用处理器间通信（IPC）子系统与另一颗 CPU 通信的蓝牙主机控制器接口（Bluetooth HCI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_BT_HCI_IPC_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_HAS_HCI_VS
CONFIG_IPC_SERVICE
CONFIG_MBOX
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_HAS_HCI_VS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HAS_HCI_VS)、[`CONFIG_IPC_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPC_SERVICE)、[`CONFIG_MBOX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBOX)。

<a id="CONFIG_BT_HCI_IPC_ENDPOINT_BOUND_TIMEOUT_MS"></a>

## 54.79 `CONFIG_BT_HCI_IPC_ENDPOINT_BOUND_TIMEOUT_MS`

**提示（Prompt）**：HCI IPC 绑定超时，单位为毫秒（Binding Timeout）

**说明（Help）**

主机控制器接口（HCI）等待处理器间通信（IPC）端点完成绑定（Binding）的超时时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_IPC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
2000
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_IPC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_IPC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_HCI_IPC_SEND_RETRY_COUNT"></a>

## 54.80 `CONFIG_BT_HCI_IPC_SEND_RETRY_COUNT`

**提示（Prompt）**：HCI IPC 发送重试次数（Send Retry Count）

**说明（Help）**

通过处理器间通信（IPC）发送消息的重试次数。通过 IPC 发送消息失败时，即 `ipc_service_send` 返回 `-ENOMEM` 时进行重试。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_IPC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_IPC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_IPC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_HCI_IPC_SEND_RETRY_DELAY_US"></a>

## 54.81 `CONFIG_BT_HCI_IPC_SEND_RETRY_DELAY_US`

**提示（Prompt）**：HCI IPC 发送重试延迟，单位为微秒（Send Retry Delay）

**说明（Help）**

通过处理器间通信（IPC）发送消息时，两次重试之间的延迟，单位为微秒。如果单个时钟节拍（Tick）的时长，由 `CONFIG_SYS_CLOCK_TICKS_PER_SEC` 决定，大于重试延迟，则使用 `k_busy_wait` 函数。应谨慎设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_IPC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
75
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_IPC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_IPC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_HCI_NXP_IR_ENABLE_PDN_TOGGLE"></a>

## 54.82 `CONFIG_BT_HCI_NXP_IR_ENABLE_PDN_TOGGLE`

**提示（Prompt）**：独立复位时切换 PDN 断电引脚（Power Down Pin Toggle）

**说明（Help）**

启用后，在蓝牙芯片组独立复位（Independent Reset，IR）期间切换断电引脚（Power Down，PDN）。切换 PDN 会同时复位蓝牙和 Wi-Fi CPU。禁用后，执行 IR 时不切换 PDN，使复位仅影响蓝牙 CPU。在必须避免复位 Wi-Fi CPU 的共存（Coexistence，COEX）场景中，应禁用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HCI_NXP_CONFIG_IR && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 蓝牙控制器独立复位配置（Independent Reset Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HCI_NXP_CONFIG_IR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HCI_NXP_CONFIG_IR)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_HCI_SETUP"></a>

## 54.83 `CONFIG_BT_HCI_SETUP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用主机控制器接口（HCI）厂商专用初始化函数（Vendor-Specific Setup）［已弃用，DEPRECATED］。如果蓝牙控制器（BT Controller）要求在蓝牙主机（BT Host）执行复位序列之前，先执行厂商专用命令序列完成初始化，则必须启用此选项。通常不应通过 `menuconfig` 或配置文件修改它；应由实现了 Setup 函数的厂商专用 HCI 扩展启用。

弃用说明：驱动应改为在 `open()` 中，通过自己的传输通道（Transport）执行厂商专用初始化。参阅 4.5 迁移指南（Migration Guide）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:335`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L335)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_BT_HCI_SET_PUBLIC_ADDR"></a>

## 54.84 `CONFIG_BT_HCI_SET_PUBLIC_ADDR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将控制器的公共地址（Public Address）传给主机控制器接口（HCI）驱动。对于支持通过厂商专用命令（Vendor-Specific Command）设置公共身份标识（Public Identity）的控制器，应由其驱动启用此选项。

从 HCI 传输通道打开时起，驱动即可通过 `bt_hci_get_public_addr()` 获取地址，因此能在 `open()` 期间设置地址。如果驱动改为在 HCI 驱动 API 的 `setup()` 函数中应用地址，该函数通过 `public_addr` 字段接收地址，则驱动还应选择 `BT_HCI_SETUP`。当应用未设置公共地址时，无论使用哪种方式，驱动得到的都是 `BT_ADDR_ANY`，而不是 `BT_ADDR_NONE`。

应用侧应在调用 `bt_enable()` 之前，通过首次调用 `bt_id_create()` 设置公共地址。

此选项描述的是驱动的一项能力：驱动通过控制器支持的方式将地址应用到控制器，例如经传输通道发送厂商专用 HCI 命令。地址仅保存在本地驱动中。通用传输驱动（Generic Transport Driver）不会将地址转发到通道远端，也不会选择此选项；这种情况下，若控制器支持，主机将通过 `HCI_VS_Write_BD_ADDR` 命令设置地址，参阅 `BT_HCI_VS`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**被选择（Selected by）**

```text
CONFIG_BT_BLUENRG_ACI
CONFIG_BT_STM32WBA
CONFIG_BT_CYW208XX
CONFIG_BT_AIROC
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:310`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L310)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_BLUENRG_ACI`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BLUENRG_ACI)、[`CONFIG_BT_STM32WBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_STM32WBA)、[`CONFIG_BT_CYW208XX`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_CYW208XX)、[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)。

<a id="CONFIG_BT_HCI_UART_INFINEON"></a>

## 54.85 `CONFIG_BT_HCI_UART_INFINEON`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用面向 AIROC 连接芯片的英飞凌 HCI UART 驱动（Infineon HCI UART Driver）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AIROC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_BT_AIROC && CONFIG_BT_H4
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_H4`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4)。

<a id="CONFIG_BT_NXP"></a>

## 54.86 `CONFIG_BT_NXP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

恩智浦 HCI 蓝牙接口（NXP HCI Bluetooth Interface）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_HCI_BLE_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC if CONFIG_BT_HCI_SET_PUBLIC_ADDR
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:228`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L228)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)、[`CONFIG_BT_HCI_SET_PUBLIC_ADDR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_SET_PUBLIC_ADDR)。

<a id="CONFIG_BT_NXP_CTRL_BSP_RTS_PULSE_MS"></a>

## 54.87 `CONFIG_BT_NXP_CTRL_BSP_RTS_PULSE_MS`

**提示（Prompt）**：BSP 唤醒触发的 RTS 脉冲持续时间，单位为毫秒（RTS Pulse Duration）

**说明（Help）**

用于从启动休眠状态（Boot-Sleep State）唤醒蓝牙 CPU 的 RTS 低电平脉冲持续时间，单位为毫秒。此值由蓝牙 CPU 引导加载程序（Bootloader）的唤醒检测窗口（Wakeup Detection Window）决定。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_NXP_CTRL_BSP_TRIGGER && ((CONFIG_BT_NXP_NW612 && CONFIG_NXP_IW61X) || (CONFIG_BT_NXP_IW416 && CONFIG_NXP_IW416) || (CONFIG_BT_NXP_IW610 && CONFIG_NXP_IW610)) && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 50]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 用于唤醒启用 BSP 的 NXP 蓝牙 CPU 的触发机制（Wakeup Trigger）

**配置项引用（Symbol References）**：[`CONFIG_BT_NXP_CTRL_BSP_TRIGGER`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_CTRL_BSP_TRIGGER)、[`CONFIG_BT_NXP_NW612`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_NW612)、[`CONFIG_NXP_IW61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW61X)、[`CONFIG_BT_NXP_IW416`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_IW416)、[`CONFIG_NXP_IW416`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW416)、[`CONFIG_BT_NXP_IW610`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_IW610)、[`CONFIG_NXP_IW610`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW610)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_NXP_CTRL_BSP_TRIGGER"></a>

## 54.88 `CONFIG_BT_NXP_CTRL_BSP_TRIGGER`

**提示（Prompt）**：用于唤醒启用 BSP 的 NXP 蓝牙 CPU 的触发机制（Wakeup Trigger）

**说明（Help）**

为恩智浦（NXP）蓝牙 IW416 / NW612 / IW610 固件启用启动—休眠—补丁（Boot-Sleep-Patch，BSP）唤醒触发。在 Wi-Fi 与蓝牙并行下载固件（FW）时，如果固件启用了 BSP，那么一旦 Wi-Fi CPU，即 CPU1，加载有效固件后，就会让蓝牙 CPU，即 CPU2，进入休眠，导致蓝牙引导加载程序（Bootloader）停止发送用于固件加载的签名字节（Signature Bytes）。

为唤醒蓝牙 CPU，主机 HCI 驱动开始向蓝牙 CPU 加载固件之前，需要对蓝牙 HCI UART 的 RTS 线执行原文所称的“撤销有效状态（De-asserted）”，并将其从高电平切换到低电平。

译注：此处保留上游对 RTS 状态与高到低转换的表述；实际电平极性应结合具体硬件接口确认。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
((CONFIG_BT_NXP_NW612 && CONFIG_NXP_IW61X) || (CONFIG_BT_NXP_IW416 && CONFIG_NXP_IW416) || (CONFIG_BT_NXP_IW610 && CONFIG_NXP_IW610)) && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UART_LINE_CTRL
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_NXP_NW612`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_NW612)、[`CONFIG_NXP_IW61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW61X)、[`CONFIG_BT_NXP_IW416`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_IW416)、[`CONFIG_NXP_IW416`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW416)、[`CONFIG_BT_NXP_IW610`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_IW610)、[`CONFIG_NXP_IW610`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW610)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_UART_LINE_CTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_LINE_CTRL)。

<a id="CONFIG_BT_NXP_CTRL_BSP_WAIT_TIMEOUT"></a>

## 54.89 `CONFIG_BT_NXP_CTRL_BSP_WAIT_TIMEOUT`

**提示（Prompt）**：等待蓝牙 CPU 进入 BSP 休眠的超时，单位为毫秒（BSP Sleep Timeout）

**说明（Help）**

发送唤醒触发（Wakeup Trigger）之前，等待蓝牙 CPU 进入启动—休眠—补丁（Boot-Sleep-Patch）状态的最长时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_NXP_CTRL_BSP_TRIGGER && ((CONFIG_BT_NXP_NW612 && CONFIG_NXP_IW61X) || (CONFIG_BT_NXP_IW416 && CONFIG_NXP_IW416) || (CONFIG_BT_NXP_IW610 && CONFIG_NXP_IW610)) && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
10000
```

**取值范围（Ranges）**

```text
[1000, 20000]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:215`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L215)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 用于唤醒启用 BSP 的 NXP 蓝牙 CPU 的触发机制（Wakeup Trigger）

**配置项引用（Symbol References）**：[`CONFIG_BT_NXP_CTRL_BSP_TRIGGER`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_CTRL_BSP_TRIGGER)、[`CONFIG_BT_NXP_NW612`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_NW612)、[`CONFIG_NXP_IW61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW61X)、[`CONFIG_BT_NXP_IW416`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_IW416)、[`CONFIG_NXP_IW416`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW416)、[`CONFIG_BT_NXP_IW610`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_IW610)、[`CONFIG_NXP_IW610`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW610)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_NXP_CTRL_HDR_SIG_INTERVAL"></a>

## 54.90 `CONFIG_BT_NXP_CTRL_HDR_SIG_INTERVAL`

**提示（Prompt）**：轮询启用 BSP 的 NXP 蓝牙 CPU 的 HDR 签名间隔（HDR Signature Polling Interval）

**说明（Help）**

轮询启用 BSP 的恩智浦（NXP）蓝牙 CPU 的 HDR 签名字节（Signature Bytes）的间隔，单位为毫秒。蓝牙引导加载程序（Bootloader）在唤醒状态下大约每 500ms 发送一次签名字节。此值应略大于签名发送周期，使超时能够可靠地表明蓝牙 CPU 已进入 BSP 休眠。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_NXP_CTRL_BSP_TRIGGER && ((CONFIG_BT_NXP_NW612 && CONFIG_NXP_IW61X) || (CONFIG_BT_NXP_IW416 && CONFIG_NXP_IW416) || (CONFIG_BT_NXP_IW610 && CONFIG_NXP_IW610)) && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
505
```

**取值范围（Ranges）**

```text
[501, 510]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L203)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 用于唤醒启用 BSP 的 NXP 蓝牙 CPU 的触发机制（Wakeup Trigger）

**配置项引用（Symbol References）**：[`CONFIG_BT_NXP_CTRL_BSP_TRIGGER`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_CTRL_BSP_TRIGGER)、[`CONFIG_BT_NXP_NW612`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_NW612)、[`CONFIG_NXP_IW61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW61X)、[`CONFIG_BT_NXP_IW416`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_IW416)、[`CONFIG_NXP_IW416`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW416)、[`CONFIG_BT_NXP_IW610`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_IW610)、[`CONFIG_NXP_IW610`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW610)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_NXP_CTRL_WAKE_ON_BT"></a>

## 54.91 `CONFIG_BT_NXP_CTRL_WAKE_ON_BT`

**提示（Prompt）**：配置 NXP 控制器的 BT／BLE 唤醒（Wake on BT / BLE）

**说明（Help）**

启用或禁用恩智浦（NXP）蓝牙 IW416 / NW612 / IW610 片上系统（SoC）的蓝牙唤醒 I/O 触发（BT Wakeup IO Trigger）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_NXP_CTRL_WAKE_ON_BT_LED_BLINK"></a>

## 54.92 `CONFIG_BT_NXP_CTRL_WAKE_ON_BT_LED_BLINK`

**提示（Prompt）**：检测到蓝牙唤醒 I/O 活动时让 LED0 闪烁（LED0 Activity Indication）

**说明（Help）**

启用 LED 闪烁，在蓝牙唤醒（Wake-on-BT）触发时指示蓝牙活动。要求在设备树（Devicetree）中定义 `led0` 别名（Alias）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BT_SYSTEM_WORKQUEUE_COOP
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_SYSTEM_WORKQUEUE_COOP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SYSTEM_WORKQUEUE_COOP)。

<a id="CONFIG_BT_NXP_IW416"></a>

## 54.93 `CONFIG_BT_NXP_IW416`

**提示（Prompt）**：恩智浦 IW416 芯片组（NXP Chipset）

**说明（Help）**

恩智浦（NXP）IW416 芯片组支持 Wi-Fi 4 与 Bluetooth 5.2。模块详情见[IW416 官方产品页面](https://www.nxp.com/products/wireless-connectivity/wi-fi-plus-bluetooth-plus-802-15-4/2-4-5-ghz-dual-band-1x1-wi-fi-4-802-11n-plus-bluetooth-5-2-solution:IW416)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_NXP_MODULE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L156)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 恩智浦蓝牙模块（NXP Bluetooth Module）

**配置项引用（Symbol References）**：[`CONFIG_BT_NXP_MODULE`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_MODULE)。

<a id="CONFIG_BT_NXP_IW610"></a>

## 54.94 `CONFIG_BT_NXP_IW610`

**提示（Prompt）**：恩智浦 IW610 芯片组的 IW610 固件（Firmware）

**说明（Help）**

恩智浦（NXP）IW610 芯片组支持 Wi-Fi™ 802.11a/b/g/n/ac/ax HE20、Bluetooth® 5.4 低功耗（Low Energy）和 802.15.4。模块详情见[IW610 官方产品页面](https://www.nxp.com/products/wireless-connectivity/wi-fi-plus-bluetooth-plus-802-15-4/2-4-5ghz-dual-band-1x1-wi-fi-6-plus-bluetooth-low-energy-5-4-plus-802-15-4-tri-radio-solution:IW610)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_NXP_MODULE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 恩智浦蓝牙模块（NXP Bluetooth Module）

**配置项引用（Symbol References）**：[`CONFIG_BT_NXP_MODULE`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_MODULE)。

<a id="CONFIG_BT_NXP_MODULE"></a>

## 54.95 `CONFIG_BT_NXP_MODULE`

**提示（Prompt）**：恩智浦蓝牙模块（NXP Bluetooth Module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4_NXP_CTLR && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_BT_NXP_NW612
```

**可选项（Choices）**

```text
CONFIG_BT_NXP_NW612
CONFIG_BT_NXP_IW416
CONFIG_BT_NXP_IW610
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_arduino_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_arduino_wifi_bt/Kconfig.defconfig)。

```text
CONFIG_BT_NXP_IW416
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
CONFIG_BT_NXP_IW416
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
CONFIG_BT_NXP_NW612
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
CONFIG_BT_NXP_IW610
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4_NXP_CTLR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4_NXP_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_NXP_NW612`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_NW612)、[`CONFIG_BT_NXP_IW416`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_IW416)、[`CONFIG_BT_NXP_IW610`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_IW610)。

<a id="CONFIG_BT_NXP_NW612"></a>

## 54.96 `CONFIG_BT_NXP_NW612`

**提示（Prompt）**：恩智浦 IW612 芯片组的 NW612 固件（Firmware）

**说明（Help）**

恩智浦（NXP）IW612 芯片组支持 Wi-Fi 802.11a/b/g/n/ac/ax、Bluetooth 5.4 基本速率／增强数据速率／低功耗（BR/EDR/LE）及原文所写的 `IEEE802.1.5.4`。Wi-Fi 数据速率最高 601 Mbps，蓝牙数据速率最高 2 Mbps。支持波特率为 3M 的四线 UART，即 `4-wire UART@3M baud`，也支持用于音频的脉冲编码调制（PCM）。模块详情见[IW612 官方产品页面](https://www.nxp.com/products/wireless-connectivity/wi-fi-plus-bluetooth-plus-802-15-4/2-4-5-ghz-dual-band-1x1-wi-fi-6-802-11ax-plus-bluetooth-5-4-plus-802-15-4-tri-radio-solution:IW612)。

译注：上游此处的 `IEEE802.1.5.4` 写法与产品链接中的 `802-15-4` 不一致，原始文本还以问号显示部分商标符号。此处保留标准编号的原始写法并说明差异。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_NXP_MODULE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.nxp:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.nxp#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 恩智浦蓝牙模块（NXP Bluetooth Module）

**配置项引用（Symbol References）**：[`CONFIG_BT_NXP_MODULE`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_MODULE)。

<a id="CONFIG_BT_PSOC6_BLESS"></a>

## 54.97 `CONFIG_BT_PSOC6_BLESS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

PSOC 6 BLESS 驱动，带有以单 CPU 模式（Single CPU Mode）运行的低功耗蓝牙（BLE）控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_BLESS_HCI_ENABLED && CONFIG_ZEPHYR_HAL_INFINEON_MODULE_BLOBS && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_INFINEON_MODULE_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_INFINEON_MODULE_BLOBS)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_INFINEON_MODULE_BLOBS`。

<a id="CONFIG_BT_PSOC6_BLESS_MAX_RX_PAYLOAD"></a>

## 54.98 `CONFIG_BT_PSOC6_BLESS_MAX_RX_PAYLOAD`

**提示（Prompt）**：最大接收载荷大小（Max RX Payload Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PSOC6_BLESS && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
27
```

**取值范围（Ranges）**

```text
[27, 251]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:299`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L299)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_PSOC6_BLESS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_PSOC6_BLESS)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_PSOC6_BLESS_MAX_TX_PAYLOAD"></a>

## 54.99 `CONFIG_BT_PSOC6_BLESS_MAX_TX_PAYLOAD`

**提示（Prompt）**：最大发送载荷大小（Max TX Payload Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PSOC6_BLESS && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
27
```

**取值范围（Ranges）**

```text
[27, 251]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:294`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L294)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_PSOC6_BLESS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_PSOC6_BLESS)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SF32LB"></a>

## 54.100 `CONFIG_BT_SF32LB`

**提示（Prompt）**：思澈蓝牙控制器（SiFli Bluetooth Controller）

**说明（Help）**

在思澈（SiFli）SF32LB 芯片组上通过处理器间通信邮箱（IPC Mailbox）传输蓝牙主机控制器接口（Bluetooth HCI）数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_MAILBOX_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_SIFLI_IPC_QUEUE
CONFIG_USE_SIFLI_HAL
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:408`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L408)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_USE_SIFLI_IPC_QUEUE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_SIFLI_IPC_QUEUE)、[`CONFIG_USE_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_SIFLI_HAL)。

<!-- kconfig-navigation -->

[上一章](P053_drivers_biometrics_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P055_drivers_bluetooth_配置项参考_2.md)
