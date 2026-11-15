---
id: learning.zephyr-docs.kconfig-reference.page-332
title: "`subsys/bluetooth`配置项参考（13/13）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第332章\_`subsys/bluetooth`配置项参考（13/13）

本章翻译官方 Kconfig 数据库中 `subsys/bluetooth` 的 16 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_VOCS_MAX_INSTANCE_COUNT"></a>

## 332.1 `CONFIG_BT_VOCS_MAX_INSTANCE_COUNT`

**提示（Prompt）**：音量偏移控制服务最大实例数（Volume Offset Control Service max instance count）

**说明（Help）**

设置音量偏移控制服务（Volume Offset Control Services）的最大实例数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vocs:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vocs#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VOCS_MAX_OUTPUT_DESCRIPTION_SIZE"></a>

## 332.2 `CONFIG_BT_VOCS_MAX_OUTPUT_DESCRIPTION_SIZE`

**提示（Prompt）**：音量偏移控制服务最大输出描述大小（max output description size）

**说明（Help）**

设置输出描述（output description）的最大大小，单位为八位字节（octets）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_VOCS && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[0, 512]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vocs:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vocs#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VOCS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_WAIT_NOP"></a>

## 332.3 `CONFIG_BT_WAIT_NOP`

**提示（Prompt）**：初始化时等待 NOP 命令完成事件（NOP Command Complete event）

**说明（Help）**

控制器针对 NOP 操作码（opcode）发出命令完成事件（Command Complete event），主机等待此事件，以确认控制器已准备好接收命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L253)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_ZEPHYR_NUS"></a>

## 332.4 `CONFIG_BT_ZEPHYR_NUS`

**提示（Prompt）**：GATT Nordic UART 服务（GATT Nordic UART Service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/nus/Kconfig.nus:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/nus/Kconfig.nus#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ZEPHYR_NUS_AUTO_START_BLUETOOTH"></a>

## 332.5 `CONFIG_BT_ZEPHYR_NUS_AUTO_START_BLUETOOTH`

**提示（Prompt）**：自动启用蓝牙协议栈并启动低功耗广播（Auto-enable Bluetooth stack and start LE advertisements）

**说明（Help）**

自动启用蓝牙协议栈，并开始使用 Nordic UART 服务（NUS）UUID 广播。适用于运行本身不处理蓝牙的应用，例如通过低功耗蓝牙上的 UART 运行非蓝牙示例。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ZEPHYR_NUS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/nus/Kconfig.nus:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/nus/Kconfig.nus#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT Nordic UART 服务（GATT Nordic UART Service）

**配置项引用（Symbol References）**：[`CONFIG_BT_ZEPHYR_NUS`](P332_subsys_bluetooth_配置项参考_13.md#CONFIG_BT_ZEPHYR_NUS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ZEPHYR_NUS_DEFAULT_INSTANCE"></a>

## 332.6 `CONFIG_BT_ZEPHYR_NUS_DEFAULT_INSTANCE`

**提示（Prompt）**：使用默认 NUS 服务实例（Use default NUS Service instance）

**说明（Help）**

启用默认 Nordic UART 服务实例（Nordic UART Service Instance），使 NUS 可像其他服务一样由子系统自身托管。如果用户希望通过 `BT_NUS_INST_DEFINE()` 在外部声明 NUS 实例，同时保留内部实例可能没有益处。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ZEPHYR_NUS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if !CONFIG_UART_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/nus/Kconfig.nus:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/nus/Kconfig.nus#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT Nordic UART 服务（GATT Nordic UART Service）

**配置项引用（Symbol References）**：[`CONFIG_BT_ZEPHYR_NUS`](P332_subsys_bluetooth_配置项参考_13.md#CONFIG_BT_ZEPHYR_NUS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_UART_BT`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN"></a>

## 332.7 `CONFIG_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN`

**提示（Prompt）**：要求加密与身份认证（Encryption and authentication required）[已弃用，DEPRECATED]

**说明（Help）**

此选项已弃用，应改为选择 `BT_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE && CONFIG_BT_GAP_SVC && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service） → 允许远端 GATT 客户端写入 GAP 外观（GAP Appearance）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE)、[`CONFIG_BT_GAP_SVC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GAP_SVC)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_DEVICE_NAME_GATT_WRITABLE_AUTHEN"></a>

## 332.8 `CONFIG_DEVICE_NAME_GATT_WRITABLE_AUTHEN`

**提示（Prompt）**：要求加密与身份认证（Encryption and authentication required）[已弃用，DEPRECATED]

**说明（Help）**

此选项已弃用，应改为选择 `BT_DEVICE_NAME_GATT_WRITABLE_AUTHEN`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DEVICE_NAME_GATT_WRITABLE && CONFIG_BT_GAP_SVC && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service） → 允许远端 GATT 客户端写入设备名称（device name）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_NAME_GATT_WRITABLE`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE)、[`CONFIG_BT_GAP_SVC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GAP_SVC)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_DEVICE_NAME_GATT_WRITABLE_ENCRYPT"></a>

## 332.9 `CONFIG_DEVICE_NAME_GATT_WRITABLE_ENCRYPT`

**提示（Prompt）**：要求加密（Encryption required）[已弃用，DEPRECATED]

**说明（Help）**

此选项已弃用，应改为选择 `BT_DEVICE_NAME_GATT_WRITABLE_ENCRYPT`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DEVICE_NAME_GATT_WRITABLE && CONFIG_BT_GAP_SVC && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service） → 允许远端 GATT 客户端写入设备名称（device name）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_NAME_GATT_WRITABLE`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE)、[`CONFIG_BT_GAP_SVC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GAP_SVC)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_DEVICE_NAME_GATT_WRITABLE_NONE"></a>

## 332.10 `CONFIG_DEVICE_NAME_GATT_WRITABLE_NONE`

**提示（Prompt）**：无要求（No requirements）[已弃用，DEPRECATED]

**说明（Help）**

此选项已弃用，应改为选择 `BT_DEVICE_NAME_GATT_WRITABLE_NONE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DEVICE_NAME_GATT_WRITABLE && CONFIG_BT_GAP_SVC && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service） → 允许远端 GATT 客户端写入设备名称（device name）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_NAME_GATT_WRITABLE`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE)、[`CONFIG_BT_GAP_SVC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GAP_SVC)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_MCTL"></a>

## 332.11 `CONFIG_MCTL`

**提示（Prompt）**：媒体播放器控制支持（media player control）

**说明（Help）**

启用对本地和远端媒体播放器（media players）的控制支持。要控制本地媒体播放器，必须先启用本地媒体播放器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mctl:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mctl#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_MCTL_LOCAL_PLAYER_CONTROL"></a>

## 332.12 `CONFIG_MCTL_LOCAL_PLAYER_CONTROL`

**提示（Prompt）**：本地媒体播放器控制支持（control of local media player）

**说明（Help）**

启用对本地媒体播放器（local media player）的控制支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCTL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mctl:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mctl#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器控制支持（media player control）

**配置项引用（Symbol References）**：[`CONFIG_MCTL`](P332_subsys_bluetooth_配置项参考_13.md#CONFIG_MCTL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_MCTL_LOCAL_PLAYER_LOCAL_CONTROL"></a>

## 332.13 `CONFIG_MCTL_LOCAL_PLAYER_LOCAL_CONTROL`

**提示（Prompt）**：本地控制本地媒体播放器的支持（local control of local media player）

**说明（Help）**

允许本地应用控制本地媒体播放器（local media players）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCTL_LOCAL_PLAYER_CONTROL && CONFIG_MCTL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mctl:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mctl#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器控制支持（media player control） → 本地媒体播放器控制支持（control of local media player）

**配置项引用（Symbol References）**：[`CONFIG_MCTL_LOCAL_PLAYER_CONTROL`](P332_subsys_bluetooth_配置项参考_13.md#CONFIG_MCTL_LOCAL_PLAYER_CONTROL)、[`CONFIG_MCTL`](P332_subsys_bluetooth_配置项参考_13.md#CONFIG_MCTL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_MCTL_LOCAL_PLAYER_REMOTE_CONTROL"></a>

## 332.14 `CONFIG_MCTL_LOCAL_PLAYER_REMOTE_CONTROL`

**提示（Prompt）**：远程控制本地媒体播放器的支持（remote control of local media players）

**说明（Help）**

启用远程控制本地媒体播放器（local media players）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCTL_LOCAL_PLAYER_CONTROL && CONFIG_MCTL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mctl:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mctl#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器控制支持（media player control） → 本地媒体播放器控制支持（control of local media player）

**配置项引用（Symbol References）**：[`CONFIG_MCTL_LOCAL_PLAYER_CONTROL`](P332_subsys_bluetooth_配置项参考_13.md#CONFIG_MCTL_LOCAL_PLAYER_CONTROL)、[`CONFIG_MCTL`](P332_subsys_bluetooth_配置项参考_13.md#CONFIG_MCTL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_MCTL_REMOTE_PLAYER_CONTROL"></a>

## 332.15 `CONFIG_MCTL_REMOTE_PLAYER_CONTROL`

**提示（Prompt）**：远端媒体播放器控制支持（control of remote media player）

**说明（Help）**

启用对远端媒体播放器（remote media player）的控制支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_MCTL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mctl:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mctl#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器控制支持（media player control）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_MCTL`](P332_subsys_bluetooth_配置项参考_13.md#CONFIG_MCTL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_MCTL_REMOTE_PLAYER_CONTROL_OBJECTS"></a>

## 332.16 `CONFIG_MCTL_REMOTE_PLAYER_CONTROL_OBJECTS`

**提示（Prompt）**：访问远端播放器对象的支持（accessing objects on remote player）

**说明（Help）**

允许访问远端媒体播放器上的对象（objects），例如曲目、组和搜索结果（tracks, groups, search results）等。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCTL_REMOTE_PLAYER_CONTROL && CONFIG_BT_MCC_OTS && CONFIG_MCTL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mctl:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mctl#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器控制支持（media player control） → 远端媒体播放器控制支持（control of remote media player）

**配置项引用（Symbol References）**：[`CONFIG_MCTL_REMOTE_PLAYER_CONTROL`](P332_subsys_bluetooth_配置项参考_13.md#CONFIG_MCTL_REMOTE_PLAYER_CONTROL)、[`CONFIG_BT_MCC_OTS`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_OTS)、[`CONFIG_MCTL`](P332_subsys_bluetooth_配置项参考_13.md#CONFIG_MCTL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<!-- kconfig-navigation -->

[上一章](P331_subsys_bluetooth_配置项参考_12.md) · [返回大纲](大纲.md) · [下一章](P333_subsys_canbus_配置项参考.md)
