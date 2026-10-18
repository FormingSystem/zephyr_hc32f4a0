---
id: learning.zephyr-docs.kconfig-reference.page-325
title: "`subsys/bluetooth`配置项参考（6/13）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第325章\_`subsys/bluetooth`配置项参考（6/13）

本章翻译官方 Kconfig 数据库中 `subsys/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_NONE"></a>

## 325.1 `CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_NONE`

**提示（Prompt）**：无要求（No requirements）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_SECURITY>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service） → 允许远端 GATT 客户端写入 GAP 外观（GAP Appearance） → 安全要求（Security requirements）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_SECURITY`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_SECURITY)。

<a id="CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_SECURITY"></a>

## 325.2 `CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_SECURITY`

**提示（Prompt）**：安全要求（Security requirements）

**说明（Help）**

选择远端 GATT 客户端写入设备外观（device appearance）时所需的安全要求（security requirements）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE && CONFIG_BT_GAP_SVC && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN if CONFIG_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN
CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN
```

**可选项（Choices）**

```text
CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_NONE
CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_ENCRYPT
CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service） → 允许远端 GATT 客户端写入 GAP 外观（GAP Appearance）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE)、[`CONFIG_BT_GAP_SVC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GAP_SVC)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN)、[`CONFIG_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN)、[`CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_NONE`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_NONE)、[`CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_ENCRYPT`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_ENCRYPT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DEVICE_NAME"></a>

## 325.3 `CONFIG_BT_DEVICE_NAME`

**提示（Prompt）**：蓝牙设备名称（Bluetooth device name）

**说明（Help）**

蓝牙设备名称（Bluetooth device name），最长 `248` 字节，不含 `NULL` 终止符。允许为空字符串。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
"Zephyr"
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:951`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L951)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DEVICE_NAME_DYNAMIC"></a>

## 325.4 `CONFIG_BT_DEVICE_NAME_DYNAMIC`

**提示（Prompt）**：允许在运行时设置蓝牙设备名称（Bluetooth device name at runtime）

**说明（Help）**

启用后，允许在运行时配置蓝牙设备名称（Bluetooth device name）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:936`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L936)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DEVICE_NAME_GATT_WRITABLE"></a>

## 325.5 `CONFIG_BT_DEVICE_NAME_GATT_WRITABLE`

**提示（Prompt）**：允许远端 GATT 客户端写入设备名称（device name）

**说明（Help）**

启用后，远端 GATT 客户端可以写入设备名称 GAP 特征（device name GAP characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DEVICE_NAME_DYNAMIC && CONFIG_BT_GAP_SVC && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_NAME_DYNAMIC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_NAME_DYNAMIC)、[`CONFIG_BT_GAP_SVC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GAP_SVC)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_AUTHEN"></a>

## 325.6 `CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_AUTHEN`

**提示（Prompt）**：要求加密与身份认证（Encryption and authentication required）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_SECURITY>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service） → 允许远端 GATT 客户端写入设备名称（device name） → 安全要求（Security requirements）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_SECURITY`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_SECURITY)。

<a id="CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_ENCRYPT"></a>

## 325.7 `CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_ENCRYPT`

**提示（Prompt）**：要求加密（Encryption required）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_SECURITY>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service） → 允许远端 GATT 客户端写入设备名称（device name） → 安全要求（Security requirements）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_SECURITY`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_SECURITY)。

<a id="CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_NONE"></a>

## 325.8 `CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_NONE`

**提示（Prompt）**：无要求（No requirements）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_SECURITY>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service） → 允许远端 GATT 客户端写入设备名称（device name） → 安全要求（Security requirements）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_SECURITY`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_SECURITY)。

<a id="CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_SECURITY"></a>

## 325.9 `CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_SECURITY`

**提示（Prompt）**：安全要求（Security requirements）

**说明（Help）**

选择远端 GATT 客户端写入设备名称（device name）时所需的安全要求（security requirements）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DEVICE_NAME_GATT_WRITABLE && CONFIG_BT_GAP_SVC && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_NONE if CONFIG_DEVICE_NAME_GATT_WRITABLE_NONE
CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_AUTHEN if CONFIG_DEVICE_NAME_GATT_WRITABLE_AUTHEN
CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_ENCRYPT if CONFIG_DEVICE_NAME_GATT_WRITABLE_ENCRYPT
CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_ENCRYPT
```

**可选项（Choices）**

```text
CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_NONE
CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_ENCRYPT
CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_AUTHEN
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service） → 允许远端 GATT 客户端写入设备名称（device name）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_NAME_GATT_WRITABLE`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE)、[`CONFIG_BT_GAP_SVC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GAP_SVC)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_NONE`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_NONE)、[`CONFIG_DEVICE_NAME_GATT_WRITABLE_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_NAME_GATT_WRITABLE_NONE)、[`CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_AUTHEN`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_AUTHEN)、[`CONFIG_DEVICE_NAME_GATT_WRITABLE_AUTHEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_NAME_GATT_WRITABLE_AUTHEN)、[`CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_ENCRYPT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_ENCRYPT)、[`CONFIG_DEVICE_NAME_GATT_WRITABLE_ENCRYPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_NAME_GATT_WRITABLE_ENCRYPT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DEVICE_NAME_MAX"></a>

## 325.10 `CONFIG_BT_DEVICE_NAME_MAX`

**提示（Prompt）**：设备名称最大大小，单位为字节（Maximum size for device name）

**说明（Help）**

蓝牙设备名称（Bluetooth device name）的存储大小。最多可为 `248` 字节，不含 `NULL` 终止符。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DEVICE_NAME_DYNAMIC && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
28
```

**取值范围（Ranges）**

```text
[2, 248]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:942`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L942)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 允许在运行时设置蓝牙设备名称（Bluetooth device name at runtime）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_NAME_DYNAMIC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DEVICE_NAME_DYNAMIC)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DEVICE_PRODUCT_ID"></a>

## 325.11 `CONFIG_BT_DEVICE_PRODUCT_ID`

**提示（Prompt）**：蓝牙设备产品 ID（Bluetooth Device Product ID）

**说明（Help）**

此选项设置设备产品 ID（device product id）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DID && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x0000
```

**取值范围（Ranges）**

```text
[0x0000, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:647`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L647)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙设备识别配置文件（Bluetooth DID Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_DID`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DID)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_DEVICE_VENDOR_ID"></a>

## 325.12 `CONFIG_BT_DEVICE_VENDOR_ID`

**提示（Prompt）**：蓝牙设备厂商 ID（Bluetooth Device Vendor ID）

**说明（Help）**

此选项设置设备厂商 ID（device vendor id）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DID && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x0000
```

**取值范围（Ranges）**

```text
[0x0000, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:640`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L640)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙设备识别配置文件（Bluetooth DID Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_DID`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DID)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_DEVICE_VERSION"></a>

## 325.13 `CONFIG_BT_DEVICE_VERSION`

**提示（Prompt）**：蓝牙设备版本（Bluetooth Device Version）

**说明（Help）**

此选项设置设备版本（device version）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DID && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x0000
```

**取值范围（Ranges）**

```text
[0x0000, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:654`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L654)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙设备识别配置文件（Bluetooth DID Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_DID`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DID)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_DF"></a>

## 325.14 `CONFIG_BT_DF`

**提示（Prompt）**：测向支持（Direction Finding support）[实验性，EXPERIMENTAL]

**说明（Help）**

启用蓝牙 5.1 测向（Direction Finding）支持，允许获取天线信息、配置恒定音调扩展（Constant Tone Extension，CTE）、发送 CTE，以及对传入 CTE 采样。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_DF_SUPPORT) && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:982`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L982)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_DF_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_SUPPORT)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_DF_SUPPORT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DF_CONNECTIONLESS_CTE_RX"></a>

## 325.15 `CONFIG_BT_DF_CONNECTIONLESS_CTE_RX`

**提示（Prompt）**：无连接模式下的 CTE 接收支持（CTE reception in connectionless mode）

**说明（Help）**

启用无连接模式（connectionless mode）下恒定音调扩展（Constant Tone Extension，CTE）的接收与采样支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT) && CONFIG_BT_DF && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:993`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L993)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 测向支持（Direction Finding support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT)、[`CONFIG_BT_DF`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DF_CONNECTIONLESS_CTE_TX"></a>

## 325.16 `CONFIG_BT_DF_CONNECTIONLESS_CTE_TX`

**提示（Prompt）**：无连接模式下的 CTE 发送支持（CTE transmission in connectionless mode）

**说明（Help）**

启用无连接模式（connectionless mode）下恒定音调扩展（Constant Tone Extension，CTE）的发送支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT) && CONFIG_BT_DF && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1000`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1000)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 测向支持（Direction Finding support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT)、[`CONFIG_BT_DF`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DF_CONNECTION_CTE_REQ"></a>

## 325.17 `CONFIG_BT_DF_CONNECTION_CTE_REQ`

**提示（Prompt）**：连接模式下的 CTE 请求过程支持（CTE request procedure in connection mode）

**说明（Help）**

启用连接模式（connection mode）下的恒定音调扩展（Constant Tone Extension，CTE）请求支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DF_CONNECTION_CTE_RX && CONFIG_BT_DF && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1021`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1021)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 测向支持（Direction Finding support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_DF_CONNECTION_CTE_RX`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF_CONNECTION_CTE_RX)、[`CONFIG_BT_DF`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DF_CONNECTION_CTE_RSP"></a>

## 325.18 `CONFIG_BT_DF_CONNECTION_CTE_RSP`

**提示（Prompt）**：连接模式下的 CTE 请求过程支持（CTE request procedure in connection mode）

**说明（Help）**

启用连接模式（connection mode）下的恒定音调扩展（Constant Tone Extension，CTE）请求支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DF_CONNECTION_CTE_TX && CONFIG_BT_DF && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1028`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1028)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 测向支持（Direction Finding support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_DF_CONNECTION_CTE_TX`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF_CONNECTION_CTE_TX)、[`CONFIG_BT_DF`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DF_CONNECTION_CTE_RX"></a>

## 325.19 `CONFIG_BT_DF_CONNECTION_CTE_RX`

**提示（Prompt）**：连接模式下的 CTE 接收支持（CTE reception in connection mode）

**说明（Help）**

启用连接模式（connection mode）下恒定音调扩展（Constant Tone Extension，CTE）的接收与采样支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT) && CONFIG_BT_DF && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1007`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1007)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 测向支持（Direction Finding support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT)、[`CONFIG_BT_DF`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DF_CONNECTION_CTE_TX"></a>

## 325.20 `CONFIG_BT_DF_CONNECTION_CTE_TX`

**提示（Prompt）**：连接模式下的 CTE 发送支持（CTE transmission in connection mode）

**说明（Help）**

启用连接模式（connection mode）下恒定音调扩展（Constant Tone Extension，CTE）的发送支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT) && CONFIG_BT_DF && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1014`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1014)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 测向支持（Direction Finding support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT)、[`CONFIG_BT_DF`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DF_CTE_RX_AOA"></a>

## 325.21 `CONFIG_BT_DF_CTE_RX_AOA`

**提示（Prompt）**：CTE 接收期间的天线切换功能，AoA（antenna switching during CTE reception）

**说明（Help）**

启用接收恒定音调扩展（CTE）期间的天线切换（antenna switching）支持，也称为到达角模式（Angle of Arrival，AoA）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_DF_CONNECTIONLESS_CTE_RX || CONFIG_BT_DF_CONNECTION_CTE_RX) && CONFIG_BT_DF && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1035`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1035)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 测向支持（Direction Finding support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_DF_CONNECTIONLESS_CTE_RX`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF_CONNECTIONLESS_CTE_RX)、[`CONFIG_BT_DF_CONNECTION_CTE_RX`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF_CONNECTION_CTE_RX)、[`CONFIG_BT_DF`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DF_CTE_TX_AOD"></a>

## 325.22 `CONFIG_BT_DF_CTE_TX_AOD`

**提示（Prompt）**：CTE 发送期间的天线切换功能，AoD（antenna switching during CTE transmission）

**说明（Help）**

启用发送恒定音调扩展（CTE）期间的天线切换（antenna switching）支持，也称为出发角模式（Angle of Departure，AoD）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_DF_CONNECTIONLESS_CTE_TX || CONFIG_BT_DF_CONNECTION_CTE_TX) && CONFIG_BT_DF && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1043`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1043)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 测向支持（Direction Finding support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_DF_CONNECTIONLESS_CTE_TX`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF_CONNECTIONLESS_CTE_TX)、[`CONFIG_BT_DF_CONNECTION_CTE_TX`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF_CONNECTION_CTE_TX)、[`CONFIG_BT_DF`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DF_VS_CL_IQ_REPORT_16_BITS_IQ_SAMPLES"></a>

## 325.23 `CONFIG_BT_DF_VS_CL_IQ_REPORT_16_BITS_IQ_SAMPLES`

**提示（Prompt）**：在无连接 IQ 报告中使用 16 位有符号整数 IQ 样本（16 bits signed integer IQ samples）

**说明（Help）**

测向（Direction Finding）的无连接 IQ 报告（connectionless IQ reports）提供一组在 CTE 采样期间采集的 IQ 样本。蓝牙 5.3 核心规范将 IQ 样本定义为 8 位有符号整数，参见 Vol 4, Part E section 7.7.65.21。此选项启用主机端厂商专用扩展（vendor specific Host extension），处理样本采用 16 位有符号整数格式的无连接 IQ 报告。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DF_CONNECTIONLESS_CTE_RX && CONFIG_BT_HCI_VS && CONFIG_BT_DF && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1051`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1051)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 测向支持（Direction Finding support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_DF_CONNECTIONLESS_CTE_RX`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF_CONNECTIONLESS_CTE_RX)、[`CONFIG_BT_HCI_VS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI_VS)、[`CONFIG_BT_DF`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DF_VS_CONN_IQ_REPORT_16_BITS_IQ_SAMPLES"></a>

## 325.24 `CONFIG_BT_DF_VS_CONN_IQ_REPORT_16_BITS_IQ_SAMPLES`

**提示（Prompt）**：在连接 IQ 报告中使用 16 位有符号整数 IQ 样本（16 bits signed integer IQ samples）

**说明（Help）**

测向（Direction Finding）的连接 IQ 报告（connection IQ reports）提供一组在 CTE 采样期间采集的 IQ 样本。蓝牙 5.3 核心规范将 IQ 样本定义为 8 位有符号整数，参见 Vol 4, Part E section 7.7.65.22。此选项启用主机端厂商专用扩展（vendor specific Host extension），处理样本采用 16 位有符号整数格式的连接 IQ 报告。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DF_CONNECTION_CTE_RX && CONFIG_BT_HCI_VS && CONFIG_BT_DF && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1061`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1061)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 测向支持（Direction Finding support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_DF_CONNECTION_CTE_RX`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF_CONNECTION_CTE_RX)、[`CONFIG_BT_HCI_VS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI_VS)、[`CONFIG_BT_DF`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DID"></a>

## 325.25 `CONFIG_BT_DID`

**提示（Prompt）**：蓝牙设备识别配置文件（Bluetooth DID Profile）[实验性，EXPERIMENTAL]

**说明（Help）**

此选项启用设备识别配置文件（DID profile）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_BT_HID_DEVICE
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:633`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L633)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_HID_DEVICE`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HID_DEVICE)。

<a id="CONFIG_BT_DIS"></a>

## 325.26 `CONFIG_BT_DIS`

**提示（Prompt）**：GATT 设备信息服务（GATT Device Information service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_FW_REV"></a>

## 325.27 `CONFIG_BT_DIS_FW_REV`

**提示（Prompt）**：DIS 固件修订版本特征（DIS Firmware Revision characteristic）

**说明（Help）**

在设备信息服务（Device Information Service）中启用固件修订版本特征（Firmware Revision characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_FW_REV_STR"></a>

## 325.28 `CONFIG_BT_DIS_FW_REV_STR`

**提示（Prompt）**：固件修订版本（Firmware revision）

**说明（Help）**

在设备信息服务（Device Information Service）中启用固件修订版本特征（firmware revision characteristic）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_FW_REV && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
"" if "" != ""
"0.0.0+0"
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → DIS 固件修订版本特征（DIS Firmware Revision characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_FW_REV`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_FW_REV)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_HW_REV"></a>

## 325.29 `CONFIG_BT_DIS_HW_REV`

**提示（Prompt）**：DIS 硬件修订版本特征（DIS Hardware Revision characteristic）

**说明（Help）**

在设备信息服务（Device Information Service）中启用硬件修订版本特征（Hardware Revision characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_HW_REV_STR"></a>

## 325.30 `CONFIG_BT_DIS_HW_REV_STR`

**提示（Prompt）**：硬件修订版本（Hardware revision）

**说明（Help）**

在设备信息服务（Device Information Service）中启用硬件修订版本特征（hardware revision characteristic）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_HW_REV && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → DIS 硬件修订版本特征（DIS Hardware Revision characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_HW_REV`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_HW_REV)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_IEEE_RCDL"></a>

## 325.31 `CONFIG_BT_DIS_IEEE_RCDL`

**提示（Prompt）**：DIS IEEE 11073-20601 法规认证数据列表特征（Regulatory Certification Data List characteristic）

**说明（Help）**

在设备信息服务（Device Information Service）中启用 IEEE 11073-20601 法规认证数据列表特征（Regulatory Certification Data List characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_IEEE_RCDL_STR"></a>

## 325.32 `CONFIG_BT_DIS_IEEE_RCDL_STR`

**提示（Prompt）**：IEEE 11073-20601 法规认证数据列表（Regulatory Certification Data List）

**说明（Help）**

设备信息服务（Device Information Service）中 IEEE 11073-20601 法规认证数据列表特征（Regulatory Certification Data List characteristic）的字符串内容。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_IEEE_RCDL && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → DIS IEEE 11073-20601 法规认证数据列表特征（Regulatory Certification Data List characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_IEEE_RCDL`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_IEEE_RCDL)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_MANUF_NAME"></a>

## 325.33 `CONFIG_BT_DIS_MANUF_NAME`

**提示（Prompt）**：制造商名称特征（Manufacturer name characteristic）

**说明（Help）**

在设备信息服务（Device Information Service）中启用制造商名称特征（manufacturer name characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_MANUF_NAME_STR"></a>

## 325.34 `CONFIG_BT_DIS_MANUF_NAME_STR`

**提示（Prompt）**：制造商名称（Manufacturer name）

**说明（Help）**

配置制造商名称字符串（manufacturer name string），可以通过设备信息服务（Device Information Service）中的制造商名称特征读取。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_MANUF_NAME && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
"Manufacturer"
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → 制造商名称特征（Manufacturer name characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_MANUF_NAME`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_MANUF_NAME)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_MODEL_NUMBER"></a>

## 325.35 `CONFIG_BT_DIS_MODEL_NUMBER`

**提示（Prompt）**：型号特征（Model number characteristic）

**说明（Help）**

在设备信息服务（Device Information Service）中启用型号特征（model number characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_MODEL_NUMBER_STR"></a>

## 325.36 `CONFIG_BT_DIS_MODEL_NUMBER_STR`

**提示（Prompt）**：型号（Model number）

**说明（Help）**

配置型号字符串（model number string），可以通过设备信息服务（Device Information Service）中的型号特征读取。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_MODEL_NUMBER && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_SOC
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → 型号特征（Model number characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_MODEL_NUMBER`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_MODEL_NUMBER)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SOC`](P257_soc_Kconfig.v2_配置项参考.md#CONFIG_SOC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_PNP"></a>

## 325.37 `CONFIG_BT_DIS_PNP`

**提示（Prompt）**：即插即用标识特征（PnP_ID characteristic）

**说明（Help）**

在设备信息服务（Device Information Service）中启用 `PnP_ID` 特征（characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_PNP_PID"></a>

## 325.38 `CONFIG_BT_DIS_PNP_PID`

**提示（Prompt）**：产品 ID（Product ID）

**说明（Help）**

产品 ID 字段（Product ID field）用于区分由厂商 ID 字段（Vendor ID field）所标识的厂商制造的不同产品。产品 ID 字段值由厂商自行管理。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_PNP && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xFFFF]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → 即插即用标识特征（PnP_ID characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_PNP`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_PNP)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_PNP_VER"></a>

## 325.39 `CONFIG_BT_DIS_PNP_VER`

**提示（Prompt）**：产品版本（Product Version）

**说明（Help）**

产品版本字段（Product Version field）使用二进制编码的十进制数（Binary-Coded Decimal，BCD）表示设备发布版本号。该值由厂商分配，定义厂商 ID（Vendor ID）与产品 ID（Product ID）所标识产品的版本，用于区分具有相同厂商 ID 和产品 ID 的不同产品版本。

对于版本 `JJ.M.N`，字段值为 `0xJJMN`：`JJ` 为主版本号（major version number），`M` 为次版本号（minor version number），`N` 为次次版本号（sub-minor version number）。例如，`2.1.3` 表示为 `0x0213`，`2.0.0` 表示为 `0x0200`。

设备发生向上兼容的更改（upward-compatible changes）时，建议递增次版本号；发生不兼容更改时，建议递增主版本号；修复缺陷（bug fixes）时递增次次版本号。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_PNP && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 0xFFFF]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → 即插即用标识特征（PnP_ID characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_PNP`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_PNP)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_PNP_VID"></a>

## 325.40 `CONFIG_BT_DIS_PNP_VID`

**提示（Prompt）**：厂商标识符（Vendor ID）。

**说明（Help）**

厂商 ID 字段（Vendor ID field）用于唯一标识设备厂商。它与厂商 ID 来源字段（Vendor ID Source field）配合使用，后者确定由哪个组织分配该 ID 值。

注意：蓝牙技术联盟（Bluetooth Special Interest Group，Bluetooth SIG）分配 Device ID Vendor ID，USB 开发者论坛（USB Implementers Forum，USB-IF）分配 Vendor ID，两者均可用于此字段。设备提供方应从 USB-IF 获取厂商 ID，或从 Bluetooth SIG 获取公司标识符（Company Identifier）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_PNP && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xFFFF]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → 即插即用标识特征（PnP_ID characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_PNP`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_PNP)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_PNP_VID_SRC"></a>

## 325.41 `CONFIG_BT_DIS_PNP_VID_SRC`

**提示（Prompt）**：厂商 ID 来源（Vendor ID source）

**说明（Help）**

厂商 ID 来源字段（Vendor ID Source field）指明分配厂商 ID 字段值的组织。可用值如下：

- `1`：Bluetooth SIG，该厂商 ID 由蓝牙技术联盟分配。
- `2`：USB IF，该厂商 ID 由 USB 开发者论坛分配。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_PNP && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → 即插即用标识特征（PnP_ID characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_PNP`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_PNP)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_SERIAL_NUMBER"></a>

## 325.42 `CONFIG_BT_DIS_SERIAL_NUMBER`

**提示（Prompt）**：DIS 序列号特征（DIS Serial number characteristic）

**说明（Help）**

在设备信息服务（Device Information Service）中启用序列号特征（Serial Number characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_SERIAL_NUMBER_STR"></a>

## 325.43 `CONFIG_BT_DIS_SERIAL_NUMBER_STR`

**提示（Prompt）**：序列号（Serial Number）

**说明（Help）**

在设备信息服务（Device Information Service）中启用序列号特征（Serial Number characteristic）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_SERIAL_NUMBER && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → DIS 序列号特征（DIS Serial number characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_SERIAL_NUMBER`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_SERIAL_NUMBER)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_SETTINGS"></a>

## 325.44 `CONFIG_BT_DIS_SETTINGS`

**提示（Prompt）**：设备信息服务中的设置功能使用（Settings usage in Device Information Service）

**说明（Help）**

允许在设备信息服务（Device Information Service）中使用设置功能（Settings）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_SETTINGS
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_STR_MAX"></a>

## 325.45 `CONFIG_BT_DIS_STR_MAX`

**提示（Prompt）**：DIS 字符串最大大小，单位为字节（Maximum size for DIS strings）

**说明（Help）**

蓝牙设备信息服务（DIS）字符串的存储大小，最多可为 `248` 字节，不含 `NULL` 终止符。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_SETTINGS && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
21
```

**取值范围（Ranges）**

```text
[2, 248]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → 设备信息服务中的设置功能使用（Settings usage in Device Information Service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_SETTINGS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_SETTINGS)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_SW_REV"></a>

## 325.46 `CONFIG_BT_DIS_SW_REV`

**提示（Prompt）**：DIS 软件修订版本特征（DIS Software Revision characteristic）

**说明（Help）**

在设备信息服务（Device Information Service）中启用软件修订版本特征（Software Revision characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_SW_REV_STR"></a>

## 325.47 `CONFIG_BT_DIS_SW_REV_STR`

**提示（Prompt）**：软件修订版本（Software revision）

**说明（Help）**

在设备信息服务（Device Information Service）中启用软件修订版本特征（software revision characteristic）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_SW_REV && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → DIS 软件修订版本特征（DIS Software Revision characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_SW_REV`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_SW_REV)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_SYSTEM_ID"></a>

## 325.48 `CONFIG_BT_DIS_SYSTEM_ID`

**提示（Prompt）**：DIS 系统 ID 特征（DIS System ID characteristic）[实验性，EXPERIMENTAL]

**说明（Help）**

在设备信息服务（Device Information Service）中启用系统 ID 特征（System ID characteristic）。此特征表示实现该服务的系统的扩展唯一标识符（Extended Unique Identifier，EUI）。该 64 位结构是一个 EUI-64，由组织唯一标识符（Organizationally Unique Identifier，OUI）与制造商定义的标识符拼接而成。传输时先发送 40 位标识符，再发送 24 位 OUI，两者均采用小端格式（little-endian format）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_SYSTEM_ID_IDENTIFIER"></a>

## 325.49 `CONFIG_BT_DIS_SYSTEM_ID_IDENTIFIER`

**提示（Prompt）**：制造商定义的唯一标识符（Manufacturer-defined unique identifier）

**说明（Help）**

制造商定义的唯一标识符（manufacturer-defined unique identifier）长度为 `40` 位。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_SYSTEM_ID && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xFFFFFFFFFF]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → DIS 系统 ID 特征（DIS System ID characteristic）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_SYSTEM_ID`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_SYSTEM_ID)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_SYSTEM_ID_OUI"></a>

## 325.50 `CONFIG_BT_DIS_SYSTEM_ID_OUI`

**提示（Prompt）**：制造商的组织唯一标识符（Organizationally Unique Identifier，OUI）

**说明（Help）**

OUI 是由 IEEE 注册机构（IEEE Registration Authority）签发的 `24` 位数值。设备信息服务（Device Information Service）中的系统 ID 特征（System ID characteristic）应包含组织唯一标识符（OUI），后接由制造商定义、对该设备唯一的标识符。

译注：本条描述字段的组成次序；实际传输的字节顺序另见 `System ID` 特征说明，其中明确写为先发送 40 位标识符，再发送 24 位 OUI，均为小端。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_SYSTEM_ID && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xFFFFFF]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:205`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L205)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → DIS 系统 ID 特征（DIS System ID characteristic）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_SYSTEM_ID`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_SYSTEM_ID)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_UDI"></a>

## 325.51 `CONFIG_BT_DIS_UDI`

**提示（Prompt）**：DIS 医疗设备 UDI 特征（DIS UDI for Medical Devices characteristic）

**说明（Help）**

在设备信息服务（Device Information Service）中启用医疗设备唯一标识（UDI for Medical Devices）特征。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_UDI_AUTHORITY_STR"></a>

## 325.52 `CONFIG_BT_DIS_UDI_AUTHORITY_STR`

**提示（Prompt）**：UDI 主管机构（UDI Authority）

**说明（Help）**

表示区域 UDI 主管机构（UDI Authority）的对象标识符（OID），例如美国 FDA。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_UDI && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L186)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → DIS 医疗设备 UDI 特征（DIS UDI for Medical Devices characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_UDI`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_UDI)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_UDI_DI_STR"></a>

## 325.53 `CONFIG_BT_DIS_UDI_DI_STR`

**提示（Prompt）**：UDI 设备标识（UDI Device Identifier）

**说明（Help）**

UDI 的固定部分，用于标识标签责任方（labeler）以及设备的特定版本或型号。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_UDI && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → DIS 医疗设备 UDI 特征（DIS UDI for Medical Devices characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_UDI`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_UDI)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_UDI_ISSUER_STR"></a>

## 325.54 `CONFIG_BT_DIS_UDI_ISSUER_STR`

**提示（Prompt）**：UDI 签发机构（UDI Issuer）

**说明（Help）**

表示 UDI 签发组织（UDI Issuing Organization）的对象标识符（OID），例如 GS1。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_UDI && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → DIS 医疗设备 UDI 特征（DIS UDI for Medical Devices characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_UDI`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_UDI)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DIS_UDI_LABEL_STR"></a>

## 325.55 `CONFIG_BT_DIS_UDI_LABEL_STR`

**提示（Prompt）**：UDI 标签（UDI Label）

**说明（Help）**

字符串值，与受认可的 UDI 签发机构（UDI Issuer）为产品分配的、人类可读形式（human readable form）的 UDI 一致。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DIS_UDI && CONFIG_BT_DIS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.dis:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.dis#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 设备信息服务（GATT Device Information service） → DIS 医疗设备 UDI 特征（DIS UDI for Medical Devices characteristic）

**配置项引用（Symbol References）**：[`CONFIG_BT_DIS_UDI`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_UDI)、[`CONFIG_BT_DIS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_EAD"></a>

## 325.56 `CONFIG_BT_EAD`

**提示（Prompt）**：加密广播数据（Encrypted Advertising Data）

**说明（Help）**

启用加密广播数据支持库（Encrypted Advertising Data library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_HOST_CCM
```

**定义位置（Location）**：[`subsys/bluetooth/lib/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/lib/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HOST_CCM`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HOST_CCM)。

<a id="CONFIG_BT_EATT"></a>

## 325.57 `CONFIG_BT_EATT`

**提示（Prompt）**：增强 ATT 承载支持（Enhanced ATT Bearers support）[实验性，EXPERIMENTAL]

**说明（Help）**

此选项启用增强 ATT 承载（Enhanced ATT bearers）支持。启用后，可连接额外的 L2CAP 信道作为承载，从而允许多个尚未完成的请求（outstanding requests）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_L2CAP_ECRED && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_BT_GATT_READ_MULT_VAR_LEN
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_ECRED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_ECRED)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_GATT_READ_MULT_VAR_LEN`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_GATT_READ_MULT_VAR_LEN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_EATT_AUTO_CONNECT"></a>

## 325.58 `CONFIG_BT_EATT_AUTO_CONNECT`

**提示（Prompt）**：链路建立时自动连接 EATT 承载（Automatically connect EATT bearers）

**说明（Help）**

与对端建立连接时，设备会尝试连接 `BT_EATT_MAX` 个增强 ATT 承载（enhanced ATT bearers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_EATT && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options） → 增强 ATT 承载支持（Enhanced ATT Bearers support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_EATT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_EATT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_EATT_MAX"></a>

## 325.59 `CONFIG_BT_EATT_MAX`

**提示（Prompt）**：增强 ATT 承载最大数量（Maximum number of Enhanced ATT bearers）

**说明（Help）**

可用的增强 ATT 承载（Enhanced ATT bearers）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_EATT && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options） → 增强 ATT 承载支持（Enhanced ATT Bearers support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_EATT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_EATT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ECC"></a>

## 325.60 `CONFIG_BT_ECC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设置此选项后，将提供内部 API，通过长工作队列（long work queue）或系统工作队列（system work queue）执行椭圆曲线 Diffie-Hellman（ECDH）操作，例如用于低功耗蓝牙安全连接（LE Secure Connections）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**被选择（Selected by）**

```text
CONFIG_BT_SMP
```

**弱选择（Implies）**

```text
CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED if CONFIG_MBEDTLS_PSA_CRYPTO_C
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1073`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1073)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED)、[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ETS"></a>

## 325.61 `CONFIG_BT_ETS`

**提示（Prompt）**：GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL]

**说明（Help）**

启用蓝牙经过时间服务（Elapsed Time Service，ETS）。该服务为以下任一类嵌入式设备提供时间服务：

- 跟踪绝对时间（absolute time），即日内时间、UTC 或本地时间的设备。
- 维护 tick 计数器（tick counter），用于相对时间测量的设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ETS_CLOCK_CAP_DST_AUTO"></a>

## 325.62 `CONFIG_BT_ETS_CLOCK_CAP_DST_AUTO`

**提示（Prompt）**：时钟自主应用夏令时规则（Clock autonomously applies DST rules）

**说明（Help）**

如果时钟能自主应用夏令时（Daylight Saving Time，DST）规则，则启用此项。启用后，时钟能力（Clock Capabilities）的位 `0` 置位，表示设备无需外部干预即可自动完成夏令时切换调整。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY && CONFIG_BT_ETS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY)、[`CONFIG_BT_ETS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ETS_CLOCK_CAP_TZ_AUTO"></a>

## 325.63 `CONFIG_BT_ETS_CLOCK_CAP_TZ_AUTO`

**提示（Prompt）**：时钟自主管理时区变化（Clock autonomously manages timezone changes）

**说明（Help）**

如果时钟能自主管理时区变化（timezone changes），则启用此项。启用后，时钟能力（Clock Capabilities）的位 `1` 置位，表示设备无需外部干预即可自动适应时区变化，例如旅行时。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY && CONFIG_BT_ETS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:188`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L188)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY)、[`CONFIG_BT_ETS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ETS_CURRENT_ELAPSED_TIME_WRITABLE"></a>

## 325.64 `CONFIG_BT_ETS_CURRENT_ELAPSED_TIME_WRITABLE`

**提示（Prompt）**：允许客户端写入时间（Allow clients to write time）

**说明（Help）**

启用当前经过时间特征（Current Elapsed Time characteristic）的写权限。启用后：

- 客户端可通过写入该特征设置或调整时间。
- 应用必须实现 `write_elapsed_time` 回调。
- 写入值会依据受支持的标志（flags）进行验证。
- 写入成功后，向其他客户端发送指示（indication）。
- 设置“当前时间线”（Current timeline）位，表示采用新的时间参考。

客户端需要同步设备时间时，使用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ETS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ETS_HELPER_API"></a>

## 325.65 `CONFIG_BT_ETS_HELPER_API`

**提示（Prompt）**：Unix 时间转换辅助 API（Helper API for Unix time conversion）

**说明（Help）**

启用在 ETS 时间格式与 Unix 毫秒时间之间转换的辅助函数（helper functions），Unix 纪元（epoch）为 `1970-01-01 00:00:00 UTC`：

- `bt_ets_time_to_unix_ms()`：ETS 格式转换为 Unix 毫秒（UTC）。
- `bt_ets_time_from_unix_ms()`：Unix 毫秒（UTC）转换为 ETS 格式。

这些函数处理纪元转换（2000 与 1970）、分辨率缩放（resolution scaling）及时区转换（timezone conversion）。

要求如下：

- UTC 模式：直接转换，无需时区偏移。
- 本地模式（Local mode）：需要时区／夏令时偏移（TZ/DST offset）以在 UTC 与本地时间之间转换。

此选项要求启用 UTC 模式或 TZ/DST 偏移支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_ETS_SUPPORT_UTC || CONFIG_BT_ETS_SUPPORT_TZ_DST) && CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY && CONFIG_BT_ETS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_SUPPORT_UTC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_SUPPORT_UTC)、[`CONFIG_BT_ETS_SUPPORT_TZ_DST`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_SUPPORT_TZ_DST)、[`CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY)、[`CONFIG_BT_ETS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ETS_RESOLUTION_100_MS"></a>

## 325.66 `CONFIG_BT_ETS_RESOLUTION_100_MS`

**提示（Prompt）**：100 毫秒（100 milliseconds）

**说明（Help）**

时间值每 `100` 毫秒（`0.1` 秒）递增一次。最大范围约为 `892551` 年。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_TIME_RESOLUTION>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 时间分辨率（Time resolution）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_TIME_RESOLUTION`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_TIME_RESOLUTION)。

<a id="CONFIG_BT_ETS_RESOLUTION_100_US"></a>

## 325.67 `CONFIG_BT_ETS_RESOLUTION_100_US`

**提示（Prompt）**：100 微秒（100 microseconds）

**说明（Help）**

时间值每 `100` 微秒（`0.0001` 秒）递增一次。最大范围约为 `892` 年。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_TIME_RESOLUTION>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 时间分辨率（Time resolution）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_TIME_RESOLUTION`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_TIME_RESOLUTION)。

<a id="CONFIG_BT_ETS_RESOLUTION_1_MS"></a>

## 325.68 `CONFIG_BT_ETS_RESOLUTION_1_MS`

**提示（Prompt）**：1 毫秒（1 millisecond）

**说明（Help）**

时间值每 `1` 毫秒（`0.001` 秒）递增一次。最大范围约为 `8,920` 年。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_TIME_RESOLUTION>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 时间分辨率（Time resolution）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_TIME_RESOLUTION`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_TIME_RESOLUTION)。

<a id="CONFIG_BT_ETS_RESOLUTION_1_SEC"></a>

## 325.69 `CONFIG_BT_ETS_RESOLUTION_1_SEC`

**提示（Prompt）**：1 秒（1 second）

**说明（Help）**

时间值每 `1` 秒递增一次。最大范围约为 `8925512` 年。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_TIME_RESOLUTION>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 时间分辨率（Time resolution）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_TIME_RESOLUTION`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_TIME_RESOLUTION)。

<a id="CONFIG_BT_ETS_SUPPORT_LOCAL_TIME"></a>

## 325.70 `CONFIG_BT_ETS_SUPPORT_LOCAL_TIME`

**提示（Prompt）**：本地时间（Local time）

**说明（Help）**

时间值（Time Value）表示本地时间（Local time），已经应用时区／夏令时调整。位 `1 = 0`，表示本地时间。

可选择启用下方的时区／夏令时偏移（TZ/DST offset），指明该本地时间所代表的时区，使接收方能按以下原始公式将本地时间转换回 UTC：

```text
UTC time = Local time - TZ/DST Offset × 15 minutes
```

即：UTC 时间 = 本地时间 − 时区／夏令时偏移量 × 15 分钟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_TIME_TYPE>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 时间参考（Time reference）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_TIME_TYPE`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_TIME_TYPE)。

<a id="CONFIG_BT_ETS_SUPPORT_TICK_COUNTER"></a>

## 325.71 `CONFIG_BT_ETS_SUPPORT_TICK_COUNTER`

**提示（Prompt）**：Tick 计数器，相对时间（Tick counter, relative time）

**说明（Help）**

使用计数器／tick 值报告相对时间（relative time）。时间值（Time Value）表示经过的时间单位数，单位由分辨率决定。计数起点取决于具体实现。此模式不适用时区及 UTC／本地时间设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_TIME_MODE>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 时间模式（Time mode）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_TIME_MODE`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_TIME_MODE)。

<a id="CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY"></a>

## 325.72 `CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY`

**提示（Prompt）**：日内时间，绝对时间（Time of day, absolute time）

**说明（Help）**

报告自 ETS 纪元 `2000-01-01 00:00:00` 起的绝对时间（absolute time）。时间值（Time Value）表示自该纪元以来的时间单位数量，单位由分辨率决定。支持 UTC 或带时区偏移的本地时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_TIME_MODE>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 时间模式（Time mode）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_TIME_MODE`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_TIME_MODE)。

<a id="CONFIG_BT_ETS_SUPPORT_TZ_DST"></a>

## 325.73 `CONFIG_BT_ETS_SUPPORT_TZ_DST`

**提示（Prompt）**：包含时区／夏令时偏移（Include timezone/DST offset）

**说明（Help）**

在特征（characteristic）中包含时区／夏令时偏移字段（TZ/DST offset），即位 `4 = 1`。偏移相对于 UTC 指定，以 `15` 分钟为一个增量。

UTC 与本地时间两种模式均可使用该偏移：

- UTC 模式：偏移作为信息供客户端计算本地时间。

```text
Local time = UTC time + TZ/DST Offset × 15 minutes
```

即：本地时间 = UTC 时间 + 时区／夏令时偏移量 × 15 分钟。

- 本地模式（Local mode）：偏移指明本地时间所代表的时区。

```text
UTC time = Local time - TZ/DST Offset × 15 minutes
```

即：UTC 时间 = 本地时间 − 时区／夏令时偏移量 × 15 分钟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY && CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY && CONFIG_BT_ETS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY)、[`CONFIG_BT_ETS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ETS_SUPPORT_UTC"></a>

## 325.74 `CONFIG_BT_ETS_SUPPORT_UTC`

**提示（Prompt）**：协调世界时（UTC，Coordinated Universal Time）

**说明（Help）**

时间值（Time Value）表示 UTC 时间。位 `1 = 1`，表示 UTC。

可选择启用下方的时区／夏令时偏移（TZ/DST offset），使客户端能按以下原始公式计算本地时间：

```text
Local time = UTC time + TZ/DST Offset × 15 minutes
```

即：本地时间 = UTC 时间 + 时区／夏令时偏移量 × 15 分钟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_TIME_TYPE>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 时间参考（Time reference）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_TIME_TYPE`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_TIME_TYPE)。

<a id="CONFIG_BT_ETS_TIME_MODE"></a>

## 325.75 `CONFIG_BT_ETS_TIME_MODE`

**提示（Prompt）**：时间模式（Time mode）

**说明（Help）**

选择时间表示模式（time representation mode），由标志字段（flags field）的位 `0` 表示：

- 日内时间（Time of Day）：报告自 `2000-01-01 00:00:00` 起的绝对时间，适用于具有实时时钟（real-time clocks）或时间同步功能的设备。
- Tick 计数器（Tick Counter）：报告相对时间，即经过的 tick／计数值，适用于无需绝对时间参考的简单事件计时。计数器起点取决于具体实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ETS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY
```

**可选项（Choices）**

```text
CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY
CONFIG_BT_ETS_SUPPORT_TICK_COUNTER
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY)、[`CONFIG_BT_ETS_SUPPORT_TICK_COUNTER`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_SUPPORT_TICK_COUNTER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ETS_TIME_RESOLUTION"></a>

## 325.76 `CONFIG_BT_ETS_TIME_RESOLUTION`

**提示（Prompt）**：时间分辨率（Time resolution）

**说明（Help）**

时间值字段（Time Value field）的时间分辨率，由标志（flags）的位 `2–3` 表示。它决定时间值递增的频率。更高分辨率提供更细的粒度，但会缩小可表示的最大时间范围。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ETS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ETS_RESOLUTION_1_SEC
```

**可选项（Choices）**

```text
CONFIG_BT_ETS_RESOLUTION_1_SEC
CONFIG_BT_ETS_RESOLUTION_100_MS
CONFIG_BT_ETS_RESOLUTION_1_MS
CONFIG_BT_ETS_RESOLUTION_100_US
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ETS_RESOLUTION_1_SEC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_RESOLUTION_1_SEC)、[`CONFIG_BT_ETS_RESOLUTION_100_MS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_RESOLUTION_100_MS)、[`CONFIG_BT_ETS_RESOLUTION_1_MS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_RESOLUTION_1_MS)、[`CONFIG_BT_ETS_RESOLUTION_100_US`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_RESOLUTION_100_US)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ETS_TIME_TYPE"></a>

## 325.77 `CONFIG_BT_ETS_TIME_TYPE`

**提示（Prompt）**：时间参考（Time reference）

**说明（Help）**

选择时间参考类型（time reference type），由标志字段（flags field）的位 `1` 表示：

- 本地时间（Local Time，位 `1 = 0`）：时间值采用已经调整好的本地时间，无需时区偏移即可表示当地时间。
- UTC（位 `1 = 1`）：时间值采用协调世界时（Coordinated Universal Time），可选择包含时区偏移，以便客户端计算本地时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY && CONFIG_BT_ETS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ETS_SUPPORT_LOCAL_TIME
```

**可选项（Choices）**

```text
CONFIG_BT_ETS_SUPPORT_LOCAL_TIME
CONFIG_BT_ETS_SUPPORT_UTC
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ets:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ets#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_SUPPORT_TIME_OF_DAY)、[`CONFIG_BT_ETS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ETS_SUPPORT_LOCAL_TIME`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_SUPPORT_LOCAL_TIME)、[`CONFIG_BT_ETS_SUPPORT_UTC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS_SUPPORT_UTC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_EXT_ADV"></a>

## 325.78 `CONFIG_BT_EXT_ADV`

原库同名定义共 2 条；本项为数据库第 2208 条记录，各定义分别保留。

**提示（Prompt）**：扩展广播与扫描支持（Extended Advertising and Scanning support）

**说明（Help）**

选择此项以启用扩展广播 API（Extended Advertising API）支持，包括多个广播集合（advertising sets）、扩展广播数据以及低功耗蓝牙编码物理层（LE Coded PHY）上的广播；也允许扫描器接收扩展广播数据，包括通过 LE Coded PHY 传输的广播数据。此外，允许通过 LE Coded PHY 建立连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_ADV_EXT_SUPPORT) && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_MESH
```

**被选择（Selected by）**

```text
CONFIG_BT_ISO_BROADCAST
CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL
```

**被弱选择（Implied by）**

```text
CONFIG_BT_CSIP_SET_MEMBER
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig.adv:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig.adv#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_ADV_EXT_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_EXT_SUPPORT)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH)、[`CONFIG_BT_ISO_BROADCAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_BROADCAST)、[`CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL)、[`CONFIG_BT_CSIP_SET_MEMBER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_ADV_EXT_SUPPORT`、`CONFIG_BT_ISO_BROADCAST`。

<a id="CONFIG_BT_EXT_ADV_CODING_SELECTION"></a>

## 325.79 `CONFIG_BT_EXT_ADV_CODING_SELECTION`

**提示（Prompt）**：广播编码选择支持（Advertising Coding Selection support）

**说明（Help）**

选择此项以启用广播编码选择 API（Advertising Coding Selection API）支持，使主机（Host）在使用扩展广播（Extended Advertising）时能够声明对编码方案（coding scheme）的严格要求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_PHY_CODED) && CONFIG_BT_EXT_ADV && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig.adv:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig.adv#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 扩展广播与扫描支持（Extended Advertising and Scanning support）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_PHY_CODED`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_PHY_CODED)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_EXT_ADV_LEGACY_SUPPORT"></a>

## 325.80 `CONFIG_BT_EXT_ADV_LEGACY_SUPPORT`

**提示（Prompt）**：支持通过传统命令启动广播（starting advertising through legacy commands）

**说明（Help）**

选择此项以允许使用传统广播 HCI 命令（Legacy Advertising HCI commands）。控制器能力未知时，应使用此选项。如果不启用，控制器就必须支持扩展广播功能（extended advertising feature）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_EXT_ADV && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig.adv:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig.adv#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 扩展广播与扫描支持（Extended Advertising and Scanning support）

**配置项引用（Symbol References）**：[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_EXT_ADV_MAX_ADV_SET"></a>

## 325.81 `CONFIG_BT_EXT_ADV_MAX_ADV_SET`

原库同名定义共 2 条；本项为数据库第 2212 条记录，各定义分别保留。

**提示（Prompt）**：最大同时广播集合数（Maximum number of simultaneous advertising sets）

**说明（Help）**

支持同时存在的蓝牙广播集合（Bluetooth advertising sets）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_EXT_ADV && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig.adv:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig.adv#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 扩展广播与扫描支持（Extended Advertising and Scanning support）

**配置项引用（Symbol References）**：[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_EXT_ADV_REASSEMBLY_TIMEOUT"></a>

## 325.82 `CONFIG_BT_EXT_ADV_REASSEMBLY_TIMEOUT`

**提示（Prompt）**：扩展广播重组超时（Extended advertising reassembly timeout）

**说明（Help）**

重组扩展广播报告（extended advertising reports）的超时，单位为毫秒。如果重组正在进行，但在超时内没有收到更多数据，该链（chain）会被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_EXT_ADV && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[100, 10000]
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig.adv:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig.adv#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 扩展广播与扫描支持（Extended Advertising and Scanning support）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_EXT_SCAN_BUF_SIZE"></a>

## 325.83 `CONFIG_BT_EXT_SCAN_BUF_SIZE`

**提示（Prompt）**：最大广播报告大小（Maximum advertisement report size）

**说明（Help）**

广播报告（advertisement report）的最大大小，单位为八位字节（octets）。如果控制器提供的广播内容超过此缓冲区大小，其余数据会被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_EXT_ADV && CONFIG_BT_OBSERVER && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
229
```

**取值范围（Ranges）**

```text
[1, 1650]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:878`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L878)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_FILTER_ACCEPT_LIST"></a>

## 325.84 `CONFIG_BT_FILTER_ACCEPT_LIST`

**提示（Prompt）**：过滤接纳列表支持（Filter accept list support）

**说明（Help）**

此选项启用过滤接纳列表 API（filter accept list API），利用低功耗蓝牙控制器的过滤能力。过滤接纳列表是全局列表，扫描器（scanner）和广播者（advertiser）共用同一份列表，列表使用期间不可修改。

广播者可过滤哪些对端能够连接或请求扫描响应数据（scan response data）；扫描器可过滤哪些广播者会触发广播报告（advertising reports）；系统可自动为已接纳的对端建立连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:273`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L273)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_FRAME_SPACE_UPDATE"></a>

## 325.85 `CONFIG_BT_FRAME_SPACE_UPDATE`

**提示（Prompt）**：帧间隔更新（Frame Space Update）

**说明（Help）**

启用蓝牙 6.0 帧间隔更新（Frame Space Update）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_FRAME_SPACE_UPDATE_SUPPORT) && CONFIG_BT_CONN && CONFIG_BT_LE_EXTENDED_FEAT_SET && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:225`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L225)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_FRAME_SPACE_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_FRAME_SPACE_UPDATE_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LE_EXTENDED_FEAT_SET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LE_EXTENDED_FEAT_SET)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_FRAME_SPACE_UPDATE_SUPPORT`。

<a id="CONFIG_BT_GAP_AUTO_UPDATE_CONN_PARAMS"></a>

## 325.86 `CONFIG_BT_GAP_AUTO_UPDATE_CONN_PARAMS`

**提示（Prompt）**：自动更新连接参数（Automatic Update of Connection Parameters）

**说明（Help）**

启用后，设备作为外设建立连接满 GAP 推荐的 `5` 秒后，可自动发送连接参数更新请求（connection parameters update request）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PERIPHERAL && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:224`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L224)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS"></a>

## 325.87 `CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS`

**提示（Prompt）**：配置外设首选连接参数（Configure peripheral preferred connection parameters）

**说明（Help）**

允许配置外设首选连接参数（peripheral preferred connection parameters）。启用后会在 GAP 中添加 PPCP 特征（characteristic）。禁用时，由应用设置期望的连接参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PERIPHERAL && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L233)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GAP_SVC"></a>

## 325.88 `CONFIG_BT_GAP_SVC`

**提示（Prompt）**：GATT 通用访问服务（GATT Generic Access Service）

**说明（Help）**

启用默认的 GATT 通用访问服务（Generic Access Service）。此服务默认启用，提供基本 GAP 功能。如果禁用，应用负责提供自己的 GAP 服务实现，否则系统不符合蓝牙资格认证要求（Bluetooth qualification compliant）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_AUTHORIZATION_CUSTOM"></a>

## 325.89 `CONFIG_BT_GATT_AUTHORIZATION_CUSTOM`

**提示（Prompt）**：GATT 操作的自定义授权（Custom authorization of GATT operations）

**说明（Help）**

允许用户定义应用专用的 GATT 操作授权逻辑（authorization logic），通过 `bt_gatt_authorization_cb_register` API 注册。详情参见 API 文档。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:274`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L274)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_AUTO_DISCOVER_CCC"></a>

## 325.90 `CONFIG_BT_GATT_AUTO_DISCOVER_CCC`

**提示（Prompt）**：支持自动发现特征的 CCC 句柄（automatic discovery of CCC handles）

**说明（Help）**

当应用不知道客户端特征配置（CCC）句柄时，此选项允许 GATT 发起发现过程以查找该句柄。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CLIENT && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_OTS_CLIENT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:210`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L210)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_OTS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OTS_CLIENT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_AUTO_READ_CENTRAL_ADDR_RES"></a>

## 325.91 `CONFIG_BT_GATT_AUTO_READ_CENTRAL_ADDR_RES`

**提示（Prompt）**：自动读取对端的中心设备地址解析支持（Central Address Resolution support）

**说明（Help）**

按照核心规范 GAP 章节的建议，对已绑定对端（bonded peer）的中心设备地址解析特征（Central Address Resolution characteristic）读取一次，并在绑定关系存续期间记住结果。如果已知对端不支持地址解析，随后使用 `BT_LE_ADV_OPT_DIR_ADDR_RPA` 向其进行定向广播（directed advertising）就会失败，因为该对端不可能收到这种广播。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CLIENT && CONFIG_BT_PERIPHERAL && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_AUTO_RESUBSCRIBE"></a>

## 325.92 `CONFIG_BT_GATT_AUTO_RESUBSCRIBE`

**提示（Prompt）**：自动重新订阅特征（Automatic re-subscription to characteristics）

**说明（Help）**

兼容性处理（Quirk）：重新建立已绑定连接（bonded connection）时，假定远端忘记了 CCC 值，并重新设置。对于不希望采用此行为的某个订阅，可设置 `BT_GATT_SUBSCRIBE_FLAG_NO_RESUB` 标志。这也意味着重连时，应用会收到一次并非由其主动请求触发的 `subscribe` 回调。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CLIENT && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_BT_GATT_AUTO_SEC_REQ
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_GATT_AUTO_SEC_REQ`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_AUTO_SEC_REQ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_AUTO_SEC_REQ"></a>

## 325.93 `CONFIG_BT_GATT_AUTO_SEC_REQ`

**提示（Prompt）**：作为外设自动请求重新建立安全状态（Automatic security re-establishment request as a peripheral）

**说明（Help）**

每次重新连接 GATT 客户端时，如果存在需要安全保护且可通知或可指示的特征（notifiable or indicatable characteristics），此选项会自动请求重新建立安全状态（security re-establishment）。该配置只适用于外设角色（peripheral role），外设会为此发送安全请求（Security Request）。

禁用时，除非中心设备先完成该操作，否则应用必须在向需要安全保护的特征发送任何通知或指示之前，调用 `bt_conn_set_security()` 重新建立安全状态。引入此选项是为了避免与某些商用中心设备的互操作性问题：这些设备对重连后立即收到安全请求的情况反应不佳。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**被弱选择（Implied by）**

```text
CONFIG_BT_GATT_AUTO_RESUBSCRIBE
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_GATT_AUTO_RESUBSCRIBE`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_AUTO_RESUBSCRIBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_AUTO_UPDATE_MTU"></a>

## 325.94 `CONFIG_BT_GATT_AUTO_UPDATE_MTU`

**提示（Prompt）**：连接时自动发送 ATT MTU 交换请求（ATT MTU exchange request）

**说明（Help）**

启用后，允许自动发送 ATT 最大传输单元（MTU）交换请求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CLIENT && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L217)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_CACHING"></a>

## 325.95 `CONFIG_BT_GATT_CACHING`

**提示（Prompt）**：GATT 缓存支持（GATT Caching support）

**说明（Help）**

启用 GATT 缓存（Caching）支持。启用后，协议栈注册客户端支持功能（Client Supported Features）及数据库哈希（Database Hash）特征，客户端可用它们检测 GATT 数据库是否发生变化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_SERVICE_CHANGED && CONFIG_PSA_CRYPTO && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_ALG_CMAC
CONFIG_PSA_WANT_ALG_ECB_NO_PADDING
```

**弱选择（Implies）**

```text
CONFIG_MBEDTLS_AES_ROM_TABLES if CONFIG_MBEDTLS_PSA_CRYPTO_C
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options） → GATT 服务变更支持（GATT Service Changed support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_SERVICE_CHANGED`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_GATT_SERVICE_CHANGED)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_ALG_CMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CMAC)、[`CONFIG_PSA_WANT_ALG_ECB_NO_PADDING`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECB_NO_PADDING)、[`CONFIG_MBEDTLS_AES_ROM_TABLES`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_AES_ROM_TABLES)、[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_CLIENT"></a>

## 325.96 `CONFIG_BT_GATT_CLIENT`

**提示（Prompt）**：GATT 客户端支持（GATT client support）

**说明（Help）**

此选项启用 GATT 客户端角色（Client role）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_MESH_PB_GATT_CLIENT
CONFIG_BT_MESH_PROXY_CLIENT
CONFIG_BT_IAS_CLIENT
CONFIG_BT_OTS_CLIENT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L190)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_PB_GATT_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PB_GATT_CLIENT)、[`CONFIG_BT_MESH_PROXY_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROXY_CLIENT)、[`CONFIG_BT_IAS_CLIENT`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_IAS_CLIENT)、[`CONFIG_BT_OTS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OTS_CLIENT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_DYNAMIC_DB"></a>

## 325.97 `CONFIG_BT_GATT_DYNAMIC_DB`

**提示（Prompt）**：GATT 动态数据库支持（GATT dynamic database support）

**说明（Help）**

允许在运行时注册／注销服务（registering/unregistering services）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_SERVICE_CHANGED && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_MESH_GATT_SERVER
CONFIG_BT_OTS
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options） → GATT 服务变更支持（GATT Service Changed support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_SERVICE_CHANGED`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_GATT_SERVICE_CHANGED)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_GATT_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT_SERVER)、[`CONFIG_BT_OTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_GATT_SERVER`。

<a id="CONFIG_BT_GATT_ENFORCE_CHANGE_UNAWARE"></a>

## 325.98 `CONFIG_BT_GATT_ENFORCE_CHANGE_UNAWARE`

**提示（Prompt）**：GATT 强制遵守未获知变更状态（GATT Enforce change-unaware state）

**说明（Help）**

启用后，会阻止向客户端发送通知和指示（notifications and indications），以遵守蓝牙 5.1 规范的要求：服务器不得向这种客户端发送通知或指示，直到客户端获知变更（change-aware）。如果服务无法处理突然出现的 `-EAGAIN` 错误，则不应使用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CACHING && CONFIG_BT_GATT_CACHING && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options） → GATT 服务变更支持（GATT Service Changed support） → GATT 缓存支持（GATT Caching support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CACHING`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CACHING)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_ENFORCE_SUBSCRIPTION"></a>

## 325.99 `CONFIG_BT_GATT_ENFORCE_SUBSCRIPTION`

**提示（Prompt）**：GATT 强制要求特征订阅（GATT Enforce characteristic subscription）

**说明（Help）**

启用后，如果设备未订阅指定特征（characteristic），服务器就会阻止向它发送该特征的通知和指示（notifications and indications）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L182)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_GAP_SVC_VALIDATE"></a>

## 325.100 `CONFIG_BT_GATT_GAP_SVC_VALIDATE`

**提示（Prompt）**：GATT GAP 服务验证（GATT GAP Service validation）

**说明（Help）**

验证 GATT 数据库中是否恰好存在一个 GAP 服务（GAP service），帮助调试可能导致蓝牙实现不符合标准的 GAP 服务相关问题。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:282`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L282)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<!-- kconfig-navigation -->

[上一章](P324_subsys_bluetooth_配置项参考_5.md) · [返回大纲](大纲.md) · [下一章](P326_subsys_bluetooth_配置项参考_7.md)
