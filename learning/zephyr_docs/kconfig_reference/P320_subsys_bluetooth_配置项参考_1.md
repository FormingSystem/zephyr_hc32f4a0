---
id: learning.zephyr-docs.kconfig-reference.page-320
title: "`subsys/bluetooth`配置项参考（1/13）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第320章\_`subsys/bluetooth`配置项参考（1/13）

本章翻译官方 Kconfig 数据库中 `subsys/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT"></a>

## 320.1 `CONFIG_BT`

原库同名定义共 2 条；本项为数据库第 1288 条记录，各定义分别保留。

**提示（Prompt）**：蓝牙（Bluetooth）

**说明（Help）**

此选项启用蓝牙（Bluetooth）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SMP
```

**主动选择（Selects）**

```text
CONFIG_NET_BUF
```

**被选择（Selected by）**

```text
CONFIG_USB_DEVICE_BLUETOOTH
CONFIG_USBD_BT_HCI
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_ieee802154/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_ieee802154/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_NET_BUF`](P198_lib_配置项参考_2.md#CONFIG_NET_BUF)、[`CONFIG_USB_DEVICE_BLUETOOTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_BLUETOOTH)、[`CONFIG_USBD_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_BT_HCI)。

<a id="CONFIG_BT_A2DP"></a>

## 320.2 `CONFIG_BT_A2DP`

**提示（Prompt）**：蓝牙高级音频分发配置文件（Bluetooth A2DP Profile）[实验性，EXPERIMENTAL]

**说明（Help）**

此选项启用高级音频分发配置文件（A2DP profile）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_AVDTP
CONFIG_EXPERIMENTAL
```

**弱选择（Implies）**

```text
CONFIG_LIBSBC
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:471`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L471)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AVDTP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVDTP)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_LIBSBC`](P237_modules_libsbc_配置项参考.md#CONFIG_LIBSBC)。

<a id="CONFIG_BT_A2DP_CODEC_MAX_IE_LEN"></a>

## 320.3 `CONFIG_BT_A2DP_CODEC_MAX_IE_LEN`

**提示（Prompt）**：A2DP 编解码器信息元素最大大小（Maximum size of A2DP codec IE）

**说明（Help）**

此选项设置 A2DP 编解码器信息元素（codec IE）的最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_A2DP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[4, 253]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:509`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L509)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_A2DP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_A2DP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_A2DP_SINK"></a>

## 320.4 `CONFIG_BT_A2DP_SINK`

**提示（Prompt）**：蓝牙 A2DP 配置文件接收端功能（Bluetooth A2DP Profile Sink Function）

**说明（Help）**

此选项启用 A2DP 配置文件的接收端功能（sink function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_A2DP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:504`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L504)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_A2DP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_A2DP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_A2DP_SOURCE"></a>

## 320.5 `CONFIG_BT_A2DP_SOURCE`

**提示（Prompt）**：蓝牙 A2DP 配置文件发送端功能（Bluetooth A2DP Profile Source Function）

**说明（Help）**

此选项启用 A2DP 配置文件的发送端功能（source function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_A2DP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:499`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L499)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_A2DP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_A2DP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_ACCEPT_CONN_AS_CENTRAL"></a>

## 320.6 `CONFIG_BT_ACCEPT_CONN_AS_CENTRAL`

**提示（Prompt）**：以中心设备角色接受新到来的 ACL 连接请求（central role）

**说明（Help）**

默认情况下，设备以外设角色（peripheral role）接受 ACL 连接请求。启用此选项后，设备将以中心设备角色（central role）接受 ACL 连接请求。通常，HCI 命令 `Accept Connection Request` 成功后，会生成 HCI 角色变更事件（Role Change event）。此 Kconfig 选项仅在调用 `bt_br_set_discoverable` 启用可连接模式（connectable mode）、且回调参数为 `NULL` 时生效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_AICS"></a>

## 320.7 `CONFIG_BT_AICS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项启用音频输入控制服务（Audio Input Control Service，AICS）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_DYNAMIC_DB && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_AICS_MAX_INSTANCE_COUNT > 0
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.aics:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.aics#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_DYNAMIC_DB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AICS_MAX_INSTANCE_COUNT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AICS_MAX_INSTANCE_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AICS_CLIENT"></a>

## 320.8 `CONFIG_BT_AICS_CLIENT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项启用音频输入控制服务（Audio Input Control Service，AICS）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_AICS_CLIENT_MAX_INSTANCE_COUNT > 0
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.aics:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.aics#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AICS_CLIENT_MAX_INSTANCE_COUNT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AICS_CLIENT_MAX_INSTANCE_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AICS_CLIENT_MAX_INSTANCE_COUNT"></a>

## 320.9 `CONFIG_BT_AICS_CLIENT_MAX_INSTANCE_COUNT`

**提示（Prompt）**：音频输入控制服务客户端最大实例数（Audio Input Control Service client max instance count）

**说明（Help）**

此选项设置音频输入控制服务（Audio Input Control Services）的最大实例数。

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

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.aics:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.aics#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AICS_MAX_INPUT_DESCRIPTION_SIZE"></a>

## 320.10 `CONFIG_BT_AICS_MAX_INPUT_DESCRIPTION_SIZE`

**提示（Prompt）**：音频输入控制服务最大输入描述大小（Audio Input Control Service max input description size）

**说明（Help）**

此选项设置输入描述（input description）的最大大小，单位为八位字节（octets）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AICS && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[0, 512]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.aics:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.aics#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AICS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AICS_MAX_INSTANCE_COUNT"></a>

## 320.11 `CONFIG_BT_AICS_MAX_INSTANCE_COUNT`

**提示（Prompt）**：音频输入控制服务最大实例数（Audio Input Control Service max instance count）

**说明（Help）**

此选项设置音频输入控制服务（Audio Input Control Services）的最大实例数。

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

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.aics:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.aics#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS"></a>

## 320.12 `CONFIG_BT_ANS`

**提示（Prompt）**：GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL]

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UTF8 && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_UTF8`](P199_lib_配置项参考_3.md#CONFIG_UTF8)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_NALRT_CAT_CALL"></a>

## 320.13 `CONFIG_BT_ANS_NALRT_CAT_CALL`

**提示（Prompt）**：支持来电（Call）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 新警报类别（New Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_NALRT_CAT_EMAIL"></a>

## 320.14 `CONFIG_BT_ANS_NALRT_CAT_EMAIL`

**提示（Prompt）**：支持电子邮件（Email）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 新警报类别（New Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_NALRT_CAT_HIGH_PRI_ALERT"></a>

## 320.15 `CONFIG_BT_ANS_NALRT_CAT_HIGH_PRI_ALERT`

**提示（Prompt）**：支持高优先级警报（High Priority Alert）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 新警报类别（New Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_NALRT_CAT_INSTANT_MESSAGE"></a>

## 320.16 `CONFIG_BT_ANS_NALRT_CAT_INSTANT_MESSAGE`

**提示（Prompt）**：支持即时消息（Instant Message）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 新警报类别（New Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_NALRT_CAT_MISSED_CALL"></a>

## 320.17 `CONFIG_BT_ANS_NALRT_CAT_MISSED_CALL`

**提示（Prompt）**：支持未接来电（Missed Call）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 新警报类别（New Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_NALRT_CAT_NEWS"></a>

## 320.18 `CONFIG_BT_ANS_NALRT_CAT_NEWS`

**提示（Prompt）**：支持新闻（News）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 新警报类别（New Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_NALRT_CAT_SCHEDULE"></a>

## 320.19 `CONFIG_BT_ANS_NALRT_CAT_SCHEDULE`

**提示（Prompt）**：支持日程（Schedule）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 新警报类别（New Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_NALRT_CAT_SIMPLE_ALERT"></a>

## 320.20 `CONFIG_BT_ANS_NALRT_CAT_SIMPLE_ALERT`

**提示（Prompt）**：支持简单警报（Simple Alert）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 新警报类别（New Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_NALRT_CAT_SMS_MMS"></a>

## 320.21 `CONFIG_BT_ANS_NALRT_CAT_SMS_MMS`

**提示（Prompt）**：支持短信／彩信（SMS/MMS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 新警报类别（New Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_NALRT_CAT_VOICE_MAIL"></a>

## 320.22 `CONFIG_BT_ANS_NALRT_CAT_VOICE_MAIL`

**提示（Prompt）**：支持语音邮件（Voice Mail）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 新警报类别（New Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_UNALRT_CAT_CALL"></a>

## 320.23 `CONFIG_BT_ANS_UNALRT_CAT_CALL`

**提示（Prompt）**：支持来电（Call）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 未读警报类别（Unread Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_UNALRT_CAT_EMAIL"></a>

## 320.24 `CONFIG_BT_ANS_UNALRT_CAT_EMAIL`

**提示（Prompt）**：支持电子邮件（Email）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 未读警报类别（Unread Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_UNALRT_CAT_HIGH_PRI_ALERT"></a>

## 320.25 `CONFIG_BT_ANS_UNALRT_CAT_HIGH_PRI_ALERT`

**提示（Prompt）**：支持高优先级警报（High Priority Alert）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 未读警报类别（Unread Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_UNALRT_CAT_INSTANT_MESSAGE"></a>

## 320.26 `CONFIG_BT_ANS_UNALRT_CAT_INSTANT_MESSAGE`

**提示（Prompt）**：支持即时消息（Instant Message）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 未读警报类别（Unread Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_UNALRT_CAT_MISSED_CALL"></a>

## 320.27 `CONFIG_BT_ANS_UNALRT_CAT_MISSED_CALL`

**提示（Prompt）**：支持未接来电（Missed Call）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 未读警报类别（Unread Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_UNALRT_CAT_NEWS"></a>

## 320.28 `CONFIG_BT_ANS_UNALRT_CAT_NEWS`

**提示（Prompt）**：支持新闻（News）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 未读警报类别（Unread Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_UNALRT_CAT_SCHEDULE"></a>

## 320.29 `CONFIG_BT_ANS_UNALRT_CAT_SCHEDULE`

**提示（Prompt）**：支持日程（Schedule）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 未读警报类别（Unread Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_UNALRT_CAT_SIMPLE_ALERT"></a>

## 320.30 `CONFIG_BT_ANS_UNALRT_CAT_SIMPLE_ALERT`

**提示（Prompt）**：支持简单警报（Simple Alert）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 未读警报类别（Unread Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_UNALRT_CAT_SMS_MMS"></a>

## 320.31 `CONFIG_BT_ANS_UNALRT_CAT_SMS_MMS`

**提示（Prompt）**：支持短信／彩信（SMS/MMS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 未读警报类别（Unread Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_UNALRT_CAT_VOICE_MAIL"></a>

## 320.32 `CONFIG_BT_ANS_UNALRT_CAT_VOICE_MAIL`

**提示（Prompt）**：支持语音邮件（Voice Mail）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.ans:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.ans#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 未读警报类别（Unread Alert Categories）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_APP_PASSKEY"></a>

## 320.33 `CONFIG_BT_APP_PASSKEY`

**提示（Prompt）**：允许应用为配对提供通行密钥（passkeys for pairing）

**说明（Help）**

启用此选项后，应用能够通过 `app_passkey()` 回调提供配对通行密钥（passkeys for pairing）。如果应用不提供通行密钥，主机（Host）会随机生成一个。警告：应用有责任确保使用随机且唯一的密钥（random and unique keys）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:714`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L714)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ASCS"></a>

## 320.34 `CONFIG_BT_ASCS`

**提示（Prompt）**：音频流控制服务支持（Audio Stream Control Service Support）

**说明（Help）**

此选项启用音频流控制服务（Audio Stream Control Service，ASCS）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE >= 19 && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.ascs:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.ascs#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ASCS_ASE_BUF_TIMEOUT"></a>

## 320.35 `CONFIG_BT_ASCS_ASE_BUF_TIMEOUT`

**提示（Prompt）**：并发访问 ASE 长读取缓冲区的处理超时，单位为毫秒（long read ASE buffer）

**说明（Help）**

如果另一个线程正在访问音频流端点（ASE）状态，ASCS 实现会先等待；此值指定其在拒绝 ASE 读取或丢弃通知（notification）前等待的最大毫秒数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ASCS && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
50
```

**取值范围（Ranges）**

```text
[0, 1000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.ascs:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.ascs#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音频流控制服务支持（Audio Stream Control Service Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_ASCS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ASCS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ASCS_ISO_DISCONNECT_DELAY"></a>

## 320.36 `CONFIG_BT_ASCS_ISO_DISCONNECT_DELAY`

**提示（Prompt）**：流停止后 ASCS 断开 ISO 连接前的延迟，单位为毫秒（ASCS ISO disconnect delay）

**说明（Help）**

对于已经停止的流（stream），ASCS 在断开其等时连接（ISO）前等待的毫秒数。由于这本应由单播客户端（Unicast Client）负责，因此加入该延迟；这是为确保 ISO 信道（channel）能够正确断开而提供的兜底机制（failsafe）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ASCS && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
500
```

**取值范围（Ranges）**

```text
[0, 5000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.ascs:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.ascs#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音频流控制服务支持（Audio Stream Control Service Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_ASCS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ASCS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ASCS_MAX_ACTIVE_ASES"></a>

## 320.37 `CONFIG_BT_ASCS_MAX_ACTIVE_ASES`

**提示（Prompt）**：同时支持的 ASE 会话数（Number of simultaneously supported ASE sessions）

**说明（Help）**

同时支持的活动音频流端点（active ASEs）数量，具体指同一时刻允许处于非空闲状态（non-idle state）的 ASE 数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ASCS && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ISO_MAX_CHAN
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.ascs:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.ascs#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音频流控制服务支持（Audio Stream Control Service Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_ASCS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ASCS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_CHAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_CHAN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT"></a>

## 320.38 `CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT`

**提示（Prompt）**：音频流端点接收端特征最大数量（Audio Stream Endpoint Sink Characteristics）

**说明（Help）**

ASE 接收端特征（ASE Sink characteristic）表示一个音频流端点（ASE）的状态，该端点与单播音频流（unicast Audio Stream）的一个传输方向相关联。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ASCS && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.ascs:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.ascs#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音频流控制服务支持（Audio Stream Control Service Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_ASCS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ASCS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ASCS_MAX_ASE_SRC_COUNT"></a>

## 320.39 `CONFIG_BT_ASCS_MAX_ASE_SRC_COUNT`

**提示（Prompt）**：音频流端点发送端特征最大数量（Audio Stream Endpoint Source Characteristics）

**说明（Help）**

ASE 发送端特征（ASE Source characteristic）表示一个音频流端点（ASE）的状态，该端点与单播音频流（unicast Audio Stream）的一个传输方向相关联。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ASCS && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.ascs:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.ascs#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音频流控制服务支持（Audio Stream Control Service Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_ASCS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ASCS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ASSERT"></a>

## 320.40 `CONFIG_BT_ASSERT`

**提示（Prompt）**：自定义蓝牙断言实现（Custom Bluetooth assert implementation）

**说明（Help）**

在禁用 `CONFIG_ASSERT` 时，使用自定义蓝牙断言实现（Bluetooth assert implementation），代替内核范围的 `__ASSERT()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:268`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L268)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_ASSERT_PANIC"></a>

## 320.41 `CONFIG_BT_ASSERT_PANIC`

**提示（Prompt）**：使用 `k_panic()` 代替 `k_oops()`

**说明（Help）**

启用 `CONFIG_BT_ASSERT` 时，此选项使代码在断言（assertion）触发时调用 `k_panic()`，而非 `k_oops()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ASSERT && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:284`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L284)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 自定义蓝牙断言实现（Custom Bluetooth assert implementation）

**配置项引用（Symbol References）**：[`CONFIG_BT_ASSERT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ASSERT)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_ASSERT_VERBOSE"></a>

## 320.42 `CONFIG_BT_ASSERT_VERBOSE`

**提示（Prompt）**：使用 `BT_ASSERT` 时打印断言字符串（assert string）

**说明（Help）**

启用 `CONFIG_BT_ASSERT` 时，此选项允许使用 `printk()` 将断言原因（cause of the assert）打印到控制台（console）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ASSERT && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:277`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L277)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 自定义蓝牙断言实现（Custom Bluetooth assert implementation）

**配置项引用（Symbol References）**：[`CONFIG_BT_ASSERT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ASSERT)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_ATT_ERR_TO_STR"></a>

## 320.43 `CONFIG_BT_ATT_ERR_TO_STR`

**提示（Prompt）**：以字符串打印 ATT 错误码（ATT error codes as strings）[实验性，EXPERIMENTAL]

**说明（Help）**

此配置允许以字符串形式打印 ATT 错误码（ATT error codes）。详情参见 `bt_att_err_to_str()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ATT_PREPARE_COUNT"></a>

## 320.44 `CONFIG_BT_ATT_PREPARE_COUNT`

**提示（Prompt）**：ATT 准备写入缓冲区数量（Number of ATT prepare write buffers）

**说明（Help）**

可供 ATT 准备写入（prepare write）使用的缓冲区数量。设为 `0` 会禁用 GATT 长写入／可靠写入（long/reliable writes）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ATT_RETRY_ON_SEC_ERR"></a>

## 320.45 `CONFIG_BT_ATT_RETRY_ON_SEC_ERR`

**提示（Prompt）**：出现安全错误时自动提高安全级别并重试（Automatic security elevation and retry）

**说明（Help）**

如果 ATT 请求因安全级别不足（insufficient security）而失败，主机（host）会尝试提高安全级别（security level）并重试该 ATT 请求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ATT_TX_COUNT"></a>

## 320.46 `CONFIG_BT_ATT_TX_COUNT`

**提示（Prompt）**：ATT 缓冲区数量（Number of ATT buffers）

**说明（Help）**

这些缓冲区仅用于通过 ATT 发送各种数据：请求（requests）、响应（responses）、指示（indications）、确认（confirmations）和通知（notifications）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BUF_ACL_TX_COUNT
3
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BUF_ACL_TX_COUNT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BUF_ACL_TX_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AUDIO"></a>

## 320.47 `CONFIG_BT_AUDIO`

**提示（Prompt）**：蓝牙音频支持（Bluetooth Audio support）

**说明（Help）**

此选项启用蓝牙音频（Bluetooth Audio）支持。具体可用功能可能依赖协议栈中已启用的其他功能，例如广播（Broadcast）所需的周期性广播（Periodic Advertisement），以及单播（Unicast）所需的 L2CAP 动态信道（Dynamic Channel）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UTF8 && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_UTF8`](P199_lib_配置项参考_3.md#CONFIG_UTF8)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AUDIO_CODEC_CAP_MAX_DATA_SIZE"></a>

## 320.48 `CONFIG_BT_AUDIO_CODEC_CAP_MAX_DATA_SIZE`

**提示（Prompt）**：编解码器能力数据大小（Codec Capabilities Data Size）

**说明（Help）**

为编解码器专用能力数据（Codec Specific Capabilities data）支持的八位字节（octets）数。默认值 `19` 与 LC3 编解码器所需字段相匹配。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
19
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AUDIO_CODEC_CAP_MAX_METADATA_SIZE"></a>

## 320.49 `CONFIG_BT_AUDIO_CODEC_CAP_MAX_METADATA_SIZE`

**提示（Prompt）**：编解码器能力元数据大小（Codec Capabilities Metadata Size）

**说明（Help）**

为编解码器专用能力元数据（Codec Specific Capabilities metadata）支持的八位字节（octets）数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE"></a>

## 320.50 `CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE`

**提示（Prompt）**：编解码器专用配置数据大小（Codec Specific Configuration Data Size）

**说明（Help）**

为编解码器专用配置数据（Codec Specific Configuration data）支持的八位字节（octets）数。默认值 `19` 与 LC3 编解码器所需字段相匹配。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
19
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE"></a>

## 320.51 `CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE`

**提示（Prompt）**：编解码器专用配置元数据大小（Codec Specific Configuration Metadata Size）

**说明（Help）**

为编解码器专用配置元数据（Codec Specific Configuration metadata）支持的八位字节（octets）数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AUDIO_NOTIFY_RETRY_DELAY"></a>

## 320.52 `CONFIG_BT_AUDIO_NOTIFY_RETRY_DELAY`

**提示（Prompt）**：通知发送重试前的延迟，以 1.25 ms 为单位（notification sending retry delay）

**说明（Help）**

当通知（notification）因没有可用发送缓冲区（TX buffers）而发送失败时，此选项设置协议栈再次尝试发送前的等待时间，以 `1.25 ms` 为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[6, 3200]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AUDIO_RX"></a>

## 320.53 `CONFIG_BT_AUDIO_RX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示协议栈已配置为支持接收音频（receiving audio），例如作为单播音频流接收端（unicast Audio Stream sink）或广播接收端（Broadcast Sink）。此内部选项自动推导，不供直接设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ASCS_ASE_SNK || CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SRC || CONFIG_BT_BAP_BROADCAST_SINK
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ASCS_ASE_SNK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ASCS_ASE_SNK)、[`CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SRC)、[`CONFIG_BT_BAP_BROADCAST_SINK`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_ASCS_ASE_SNK`、`CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SRC`。

<a id="CONFIG_BT_AUDIO_TX"></a>

## 320.54 `CONFIG_BT_AUDIO_TX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示协议栈已配置为支持发送音频（transmitting audio），例如作为单播音频流发送端（unicast Audio Stream source）或广播发送端（Broadcast Source）。此内部选项自动推导，不供直接设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ASCS_ASE_SRC || CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SNK || CONFIG_BT_BAP_BROADCAST_SOURCE
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ASCS_ASE_SRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ASCS_ASE_SRC)、[`CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SNK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SNK)、[`CONFIG_BT_BAP_BROADCAST_SOURCE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SOURCE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_ASCS_ASE_SRC`、`CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SNK`。

<a id="CONFIG_BT_AUTO_DATA_LEN_UPDATE"></a>

## 320.55 `CONFIG_BT_AUTO_DATA_LEN_UPDATE`

**提示（Prompt）**：自动发起数据长度更新过程（Data Length Update procedure）

**说明（Help）**

在连接建立时发起数据长度更新过程（Data Length Update Procedure）。如果希望保留对此过程的支持，但由远端设备自行决定何时发起，或者希望手动发起，则禁用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DATA_LEN_UPDATE && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if !CONFIG_BT_USER_DATA_LEN_UPDATE
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:405`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L405)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_DATA_LEN_UPDATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DATA_LEN_UPDATE)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_USER_DATA_LEN_UPDATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_USER_DATA_LEN_UPDATE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AUTO_PHY_CENTRAL"></a>

## 320.56 `CONFIG_BT_AUTO_PHY_CENTRAL`

**提示（Prompt）**：中心设备角色的自动 PHY 更新（Auto PHY update for central role）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CENTRAL && CONFIG_BT_PHY_UPDATE && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_AUTO_PHY_CENTRAL_2M
```

**可选项（Choices）**

```text
CONFIG_BT_AUTO_PHY_CENTRAL_NONE
CONFIG_BT_AUTO_PHY_CENTRAL_1M
CONFIG_BT_AUTO_PHY_CENTRAL_2M
CONFIG_BT_AUTO_PHY_CENTRAL_CODED
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:369`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L369)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_PHY_UPDATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PHY_UPDATE)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AUTO_PHY_CENTRAL_2M`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_CENTRAL_2M)、[`CONFIG_BT_AUTO_PHY_CENTRAL_NONE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_CENTRAL_NONE)、[`CONFIG_BT_AUTO_PHY_CENTRAL_1M`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_CENTRAL_1M)、[`CONFIG_BT_AUTO_PHY_CENTRAL_CODED`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_CENTRAL_CODED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AUTO_PHY_CENTRAL_1M"></a>

## 320.57 `CONFIG_BT_AUTO_PHY_CENTRAL_1M`

**提示（Prompt）**：1M 物理层（1M PHY）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUTO_PHY_CENTRAL>
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:377`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L377)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 中心设备角色的自动 PHY 更新（Auto PHY update for central role）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUTO_PHY_CENTRAL`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_CENTRAL)。

<a id="CONFIG_BT_AUTO_PHY_CENTRAL_2M"></a>

## 320.58 `CONFIG_BT_AUTO_PHY_CENTRAL_2M`

**提示（Prompt）**：2M 物理层（2M PHY）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUTO_PHY_CENTRAL>
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:380`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L380)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 中心设备角色的自动 PHY 更新（Auto PHY update for central role）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUTO_PHY_CENTRAL`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_CENTRAL)。

<a id="CONFIG_BT_AUTO_PHY_CENTRAL_CODED"></a>

## 320.59 `CONFIG_BT_AUTO_PHY_CENTRAL_CODED`

**提示（Prompt）**：编码物理层（Coded PHY）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUTO_PHY_CENTRAL>
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:383`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L383)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 中心设备角色的自动 PHY 更新（Auto PHY update for central role）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUTO_PHY_CENTRAL`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_CENTRAL)。

<a id="CONFIG_BT_AUTO_PHY_CENTRAL_NONE"></a>

## 320.60 `CONFIG_BT_AUTO_PHY_CENTRAL_NONE`

**提示（Prompt）**：无物理层偏好（No PHY preference）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUTO_PHY_CENTRAL>
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:374`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L374)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 中心设备角色的自动 PHY 更新（Auto PHY update for central role）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUTO_PHY_CENTRAL`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_CENTRAL)。

<a id="CONFIG_BT_AUTO_PHY_PERIPHERAL"></a>

## 320.61 `CONFIG_BT_AUTO_PHY_PERIPHERAL`

**提示（Prompt）**：外设角色的自动 PHY 更新（Auto PHY update for peripheral role）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PERIPHERAL && CONFIG_BT_PHY_UPDATE && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_AUTO_PHY_PERIPHERAL_NONE
```

**可选项（Choices）**

```text
CONFIG_BT_AUTO_PHY_PERIPHERAL_NONE
CONFIG_BT_AUTO_PHY_PERIPHERAL_1M
CONFIG_BT_AUTO_PHY_PERIPHERAL_2M
CONFIG_BT_AUTO_PHY_PERIPHERAL_CODED
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:350`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L350)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_PHY_UPDATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PHY_UPDATE)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AUTO_PHY_PERIPHERAL_NONE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_PERIPHERAL_NONE)、[`CONFIG_BT_AUTO_PHY_PERIPHERAL_1M`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_PERIPHERAL_1M)、[`CONFIG_BT_AUTO_PHY_PERIPHERAL_2M`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_PERIPHERAL_2M)、[`CONFIG_BT_AUTO_PHY_PERIPHERAL_CODED`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_PERIPHERAL_CODED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AUTO_PHY_PERIPHERAL_1M"></a>

## 320.62 `CONFIG_BT_AUTO_PHY_PERIPHERAL_1M`

**提示（Prompt）**：1M 物理层（1M PHY）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUTO_PHY_PERIPHERAL>
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:358`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L358)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 外设角色的自动 PHY 更新（Auto PHY update for peripheral role）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUTO_PHY_PERIPHERAL`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_PERIPHERAL)。

<a id="CONFIG_BT_AUTO_PHY_PERIPHERAL_2M"></a>

## 320.63 `CONFIG_BT_AUTO_PHY_PERIPHERAL_2M`

**提示（Prompt）**：2M 物理层（2M PHY）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUTO_PHY_PERIPHERAL>
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:361`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L361)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 外设角色的自动 PHY 更新（Auto PHY update for peripheral role）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUTO_PHY_PERIPHERAL`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_PERIPHERAL)。

<a id="CONFIG_BT_AUTO_PHY_PERIPHERAL_CODED"></a>

## 320.64 `CONFIG_BT_AUTO_PHY_PERIPHERAL_CODED`

**提示（Prompt）**：编码物理层（Coded PHY）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUTO_PHY_PERIPHERAL>
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:364`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L364)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 外设角色的自动 PHY 更新（Auto PHY update for peripheral role）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUTO_PHY_PERIPHERAL`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_PERIPHERAL)。

<a id="CONFIG_BT_AUTO_PHY_PERIPHERAL_NONE"></a>

## 320.65 `CONFIG_BT_AUTO_PHY_PERIPHERAL_NONE`

**提示（Prompt）**：无物理层偏好（No PHY preference）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUTO_PHY_PERIPHERAL>
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:355`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L355)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 外设角色的自动 PHY 更新（Auto PHY update for peripheral role）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUTO_PHY_PERIPHERAL`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_PHY_PERIPHERAL)。

<a id="CONFIG_BT_AVCTP"></a>

## 320.66 `CONFIG_BT_AVCTP`

**提示（Prompt）**：蓝牙音视频控制传输协议支持（Bluetooth AVCTP protocol support）[实验性，EXPERIMENTAL]

**说明（Help）**

此选项启用蓝牙音视频控制传输协议（AVCTP）支持。

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
CONFIG_BT_AVRCP
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:523`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L523)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_AVRCP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP)。

<a id="CONFIG_BT_AVDTP"></a>

## 320.67 `CONFIG_BT_AVDTP`

**提示（Prompt）**：蓝牙音视频分发传输协议支持（Bluetooth AVDTP protocol support）[实验性，EXPERIMENTAL]

**说明（Help）**

此选项启用蓝牙音视频分发传输协议（AVDTP）支持。

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
CONFIG_BT_A2DP
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:465`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L465)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_A2DP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_A2DP)。

<a id="CONFIG_BT_AVDTP_RTP_VERSION"></a>

## 320.68 `CONFIG_BT_AVDTP_RTP_VERSION`

**提示（Prompt）**：蓝牙 AVDTP 的 RTP 版本（Bluetooth AVDTP RTP version）

**说明（Help）**

此选项设置 AVDTP 使用的实时传输协议（RTP）版本。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AVDTP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:481`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L481)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_AVDTP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVDTP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_AVDTP_SIGNAL_SDU_MAX"></a>

## 320.69 `CONFIG_BT_AVDTP_SIGNAL_SDU_MAX`

**提示（Prompt）**：AVDTP 信令 SDU 最大大小（Maximum size of AVDTP signaling SDU）

**说明（Help）**

此选项设置 AVDTP 信令服务数据单元（signaling SDU）的最大大小。默认值为 `512` 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AVDTP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[48, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:487`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L487)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_AVDTP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVDTP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_AVRCP"></a>

## 320.70 `CONFIG_BT_AVRCP`

**提示（Prompt）**：蓝牙音视频遥控配置文件（Bluetooth AVRCP Profile）[实验性，EXPERIMENTAL]

**说明（Help）**

此选项启用音视频遥控配置文件（AVRCP profile）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_AVCTP
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:529`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L529)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AVCTP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVCTP)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_BT_AVRCP_BROWSING"></a>

## 320.71 `CONFIG_BT_AVRCP_BROWSING`

**提示（Prompt）**：蓝牙 AVRCP 浏览信道支持（Bluetooth AVRCP Browsing channel support）[实验性，EXPERIMENTAL]

**说明（Help）**

此选项启用蓝牙 BR/EDR 上的 AVRCP 浏览信道（Browsing channel）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AVRCP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_BT_L2CAP_ENH_RET
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:559`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L559)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙音视频遥控配置文件（Bluetooth AVRCP Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_L2CAP_ENH_RET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_ENH_RET)。

<a id="CONFIG_BT_AVRCP_BROWSING_L2CAP_MTU"></a>

## 320.72 `CONFIG_BT_AVRCP_BROWSING_L2CAP_MTU`

**提示（Prompt）**：AVRCP 浏览信道的 L2CAP MTU（L2CAP MTU for AVRCP Browsing Channel）

**说明（Help）**

AVCTP 浏览信道（Browsing Channel）的 L2CAP 最大传输单元（MTU）最大大小。接收 MTU（RX MTU）会被截减，为 ACL 数据及类型开销和 L2CAP 协议数据单元头（PDU header）留出空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AVRCP_BROWSING && CONFIG_BT_AVRCP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
339
```

**取值范围（Ranges）**

```text
[339, 4096]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:569`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L569)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙音视频遥控配置文件（Bluetooth AVRCP Profile）[实验性，EXPERIMENTAL] → 蓝牙 AVRCP 浏览信道支持（Bluetooth AVRCP Browsing channel support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP_BROWSING`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_BROWSING)、[`CONFIG_BT_AVRCP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_AVRCP_CONTROLLER"></a>

## 320.73 `CONFIG_BT_AVRCP_CONTROLLER`

**提示（Prompt）**：蓝牙 AVRCP 配置文件控制器功能（Bluetooth AVRCP Profile Controller Function）

**说明（Help）**

此选项启用 AVRCP 配置文件的控制器功能（controller function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AVRCP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:543`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L543)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙音视频遥控配置文件（Bluetooth AVRCP Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_AVRCP_CT_COVER_ART"></a>

## 320.74 `CONFIG_BT_AVRCP_CT_COVER_ART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项启用蓝牙 BR/EDR 上 AVRCP 控制器角色（controller role）的封面图（Cover Art）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AVRCP_CONTROLLER && CONFIG_BT_AVRCP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_BT_BIP
```

**被选择（Selected by）**

```text
CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE_PROPERTIES
CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE
CONFIG_BT_AVRCP_CT_COVER_ART_GET_LINKED_THUMBNAIL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:592`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L592)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙音视频遥控配置文件（Bluetooth AVRCP Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP_CONTROLLER`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CONTROLLER)、[`CONFIG_BT_AVRCP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_BIP`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BIP)、[`CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE_PROPERTIES`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE_PROPERTIES)、[`CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE)、[`CONFIG_BT_AVRCP_CT_COVER_ART_GET_LINKED_THUMBNAIL`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CT_COVER_ART_GET_LINKED_THUMBNAIL)。

<a id="CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE"></a>

## 320.75 `CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE`

**提示（Prompt）**：蓝牙 AVRCP 控制器封面图获取图像支持（Cover Art Get Image）[实验性，EXPERIMENTAL]

**说明（Help）**

此选项启用蓝牙 BR/EDR 上 AVRCP 控制器角色（Controller role）的封面图获取图像（Cover Art Get Image）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AVRCP_CONTROLLER && CONFIG_BT_AVRCP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_BT_BIP
CONFIG_BT_AVRCP_CT_COVER_ART
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:611`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L611)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙音视频遥控配置文件（Bluetooth AVRCP Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP_CONTROLLER`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CONTROLLER)、[`CONFIG_BT_AVRCP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_BIP`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BIP)、[`CONFIG_BT_AVRCP_CT_COVER_ART`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CT_COVER_ART)。

<a id="CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE_PROPERTIES"></a>

## 320.76 `CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE_PROPERTIES`

**提示（Prompt）**：蓝牙 AVRCP 控制器封面图获取图像属性支持（Cover Art Get Image Properties）[实验性，EXPERIMENTAL]

**说明（Help）**

此选项启用蓝牙 BR/EDR 上 AVRCP 控制器角色（Controller role）的封面图获取图像属性（Cover Art Get Image Properties）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AVRCP_CONTROLLER && CONFIG_BT_AVRCP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_BT_BIP
CONFIG_BT_AVRCP_CT_COVER_ART
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:601`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L601)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙音视频遥控配置文件（Bluetooth AVRCP Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP_CONTROLLER`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CONTROLLER)、[`CONFIG_BT_AVRCP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_BIP`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BIP)、[`CONFIG_BT_AVRCP_CT_COVER_ART`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CT_COVER_ART)。

<a id="CONFIG_BT_AVRCP_CT_COVER_ART_GET_LINKED_THUMBNAIL"></a>

## 320.77 `CONFIG_BT_AVRCP_CT_COVER_ART_GET_LINKED_THUMBNAIL`

**提示（Prompt）**：蓝牙 AVRCP 控制器封面图获取关联缩略图支持（Cover Art Get Linked Thumbnail）[实验性，EXPERIMENTAL]

**说明（Help）**

此选项启用蓝牙 BR/EDR 上 AVRCP 控制器角色（Controller role）的封面图获取关联缩略图（Cover Art Get Linked Thumbnail）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AVRCP_CONTROLLER && CONFIG_BT_AVRCP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_BT_BIP
CONFIG_BT_AVRCP_CT_COVER_ART
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:621`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L621)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙音视频遥控配置文件（Bluetooth AVRCP Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP_CONTROLLER`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CONTROLLER)、[`CONFIG_BT_AVRCP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_BIP`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BIP)、[`CONFIG_BT_AVRCP_CT_COVER_ART`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CT_COVER_ART)。

<a id="CONFIG_BT_AVRCP_TARGET"></a>

## 320.78 `CONFIG_BT_AVRCP_TARGET`

**提示（Prompt）**：蓝牙 AVRCP 配置文件目标端功能（Bluetooth AVRCP Profile Target Function）

**说明（Help）**

此选项启用 AVRCP 配置文件的目标端功能（target function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AVRCP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:538`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L538)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙音视频遥控配置文件（Bluetooth AVRCP Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_AVRCP_TG_COVER_ART"></a>

## 320.79 `CONFIG_BT_AVRCP_TG_COVER_ART`

**提示（Prompt）**：蓝牙 AVRCP 目标端封面图支持（Bluetooth AVRCP Target Cover Art support）[实验性，EXPERIMENTAL]

**说明（Help）**

此选项启用蓝牙 BR/EDR 上 AVRCP 目标端角色（Target role）的封面图（Cover Art）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AVRCP_TARGET && CONFIG_BT_AVRCP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_BT_BIP
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:583`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L583)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙音视频遥控配置文件（Bluetooth AVRCP Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP_TARGET`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_TARGET)、[`CONFIG_BT_AVRCP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_BIP`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BIP)。

<a id="CONFIG_BT_AVRCP_VD_RX_SIZE"></a>

## 320.80 `CONFIG_BT_AVRCP_VD_RX_SIZE`

**提示（Prompt）**：AVRCP 厂商相关接收数据缓冲区大小（AVRCP Vendor Dependent RX data buffer Size）

**说明（Help）**

AVRCP 厂商相关接收数据缓冲区（Vendor Dependent RX data buffer）的大小，单位为字节。此缓冲区用于重组从控制器设备（CT device）收到的、经过分片的 AVRCP 厂商相关命令与响应（Vendor Dependent commands and responses）。如果远端 CT 发送较大的厂商专用协议数据单元（Vendor-specific PDUs），或经常发生分片，可考虑增大该值，以免消息处理不完整。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AVRCP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1024
```

**取值范围（Ranges）**

```text
[512, 32767]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:548`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L548)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙音视频遥控配置文件（Bluetooth AVRCP Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_BACKGROUND_SCAN_INTERVAL"></a>

## 320.81 `CONFIG_BT_BACKGROUND_SCAN_INTERVAL`

**提示（Prompt）**：后台扫描间隔，以 0.625 ms 为单位（background scanning interval）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2048
```

**取值范围（Ranges）**

```text
[4, 16384]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:869`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L869)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BACKGROUND_SCAN_WINDOW"></a>

## 320.82 `CONFIG_BT_BACKGROUND_SCAN_WINDOW`

**提示（Prompt）**：后台扫描窗口，以 0.625 ms 为单位（background scanning window）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
18
```

**取值范围（Ranges）**

```text
[4, 16384]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:873`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L873)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_BASS_MAX_SUBGROUPS"></a>

## 320.83 `CONFIG_BT_BAP_BASS_MAX_SUBGROUPS`

**提示（Prompt）**：BASS 接收状态支持的最大子组数（maximum number of subgroups）

**说明（Help）**

此选项设置支持的最大子组（subgroups）数。受广播数据（advertising data）限制，所有子组的总大小最大为 `249`。一个子组的最小大小为 `10` 个八位字节（octets）。因此，一个 BASE 实际最多可包含 `24` 个子组。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 24]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_BROADCAST_ASSISTANT"></a>

## 320.84 `CONFIG_BT_BAP_BROADCAST_ASSISTANT`

**提示（Prompt）**：基本音频配置文件广播助手角色支持（Basic Audio Profile Broadcast Assistant role support）

**说明（Help）**

此选项启用广播助手角色（Broadcast Assistant role）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_EXT_ADV && CONFIG_BT_PER_ADV_SYNC && CONFIG_BT_ISO_SYNC_RECEIVER && CONFIG_BT_GATT_CLIENT && CONFIG_BT_GATT_AUTO_DISCOVER_CCC && CONFIG_BT_GATT_AUTO_UPDATE_MTU && CONFIG_BT_OBSERVER && CONFIG_BT_BONDABLE && CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE >= 19 && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:241`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L241)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_PER_ADV_SYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC)、[`CONFIG_BT_ISO_SYNC_RECEIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_SYNC_RECEIVER)、[`CONFIG_BT_GATT_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_GATT_AUTO_DISCOVER_CCC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_AUTO_DISCOVER_CCC)、[`CONFIG_BT_GATT_AUTO_UPDATE_MTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_AUTO_UPDATE_MTU)、[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_BONDABLE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BONDABLE)、[`CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_BROADCAST_ASSISTANT_RECV_STATE_COUNT"></a>

## 320.85 `CONFIG_BT_BAP_BROADCAST_ASSISTANT_RECV_STATE_COUNT`

**提示（Prompt）**：广播助手最大接收状态数量（Broadcast Assistant Max Receive State Count）

**说明（Help）**

设置会被发现并可供使用的接收状态特征（receive state characteristics）的最大数量。每个特征都可保存用于同步到周期性广播（periodic advertising）或广播等时流（broadcast isochronous stream）的信息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_BROADCAST_ASSISTANT && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:257`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L257)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 基本音频配置文件广播助手角色支持（Basic Audio Profile Broadcast Assistant role support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_ASSISTANT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_BROADCAST_SINK"></a>

## 320.86 `CONFIG_BT_BAP_BROADCAST_SINK`

**提示（Prompt）**：蓝牙广播接收端音频支持（Bluetooth Broadcast Sink Audio Support）

**说明（Help）**

此选项启用使用等时信道（Isochronous channels）的蓝牙广播接收端音频（Bluetooth Broadcast Sink Audio）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ISO_SYNC_RECEIVER && CONFIG_BT_PAC_SNK && CONFIG_BT_PERIPHERAL && CONFIG_BT_BAP_SCAN_DELEGATOR && CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE >= 19 && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_SYNC_RECEIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_SYNC_RECEIVER)、[`CONFIG_BT_PAC_SNK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PAC_SNK)、[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_BAP_SCAN_DELEGATOR`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_SCAN_DELEGATOR)、[`CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_BROADCAST_SNK_COUNT"></a>

## 320.87 `CONFIG_BT_BAP_BROADCAST_SNK_COUNT`

**提示（Prompt）**：基本音频广播接收端数量（Basic Audio Broadcaster Sink count）

**说明（Help）**

此选项设置支持的广播接收端（broadcast sinks）数量。一个广播接收端可接收多个流（streams），每个接收端最多为 `BT_BAP_BROADCAST_SNK_STREAM_COUNT` 个。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_BROADCAST_SINK && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, CONFIG_BT_ISO_MAX_BIG]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙广播接收端音频支持（Bluetooth Broadcast Sink Audio Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SINK`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SINK)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_BIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_BIG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_BROADCAST_SNK_STREAM_COUNT"></a>

## 320.88 `CONFIG_BT_BAP_BROADCAST_SNK_STREAM_COUNT`

**提示（Prompt）**：基本音频广播接收端流数量（Basic Audio Broadcast Sink Stream count）

**说明（Help）**

此选项设置每个广播接收端（broadcast sink）支持的最大流（streams）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_BROADCAST_SNK_COUNT > 0 && CONFIG_BT_BAP_BROADCAST_SINK && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_ISO_MAX_CHAN] if CONFIG_BT_ISO_MAX_CHAN < 31
[1, 31]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙广播接收端音频支持（Bluetooth Broadcast Sink Audio Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SNK_COUNT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SNK_COUNT)、[`CONFIG_BT_BAP_BROADCAST_SINK`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SINK)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_CHAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_CHAN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_BROADCAST_SNK_SUBGROUP_COUNT"></a>

## 320.89 `CONFIG_BT_BAP_BROADCAST_SNK_SUBGROUP_COUNT`

**提示（Prompt）**：基本音频配置文件广播接收端子组数量（Basic Audio Profile Broadcast Sink subgroup count）

**说明（Help）**

此选项设置每个广播接收端（broadcast sink）支持的最大子组（subgroups）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_BROADCAST_SINK && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BAP_BASS_MAX_SUBGROUPS
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_BAP_BASS_MAX_SUBGROUPS]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙广播接收端音频支持（Bluetooth Broadcast Sink Audio Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SINK`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SINK)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BAP_BASS_MAX_SUBGROUPS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BASS_MAX_SUBGROUPS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_BROADCAST_SOURCE"></a>

## 320.90 `CONFIG_BT_BAP_BROADCAST_SOURCE`

**提示（Prompt）**：蓝牙广播发送端音频支持（Bluetooth Broadcast Source Audio Support）

**说明（Help）**

此选项启用使用等时信道（Isochronous channels）的蓝牙广播发送端音频（Bluetooth Broadcast Source Audio）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ISO_BROADCASTER && CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE >= 19 && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_BROADCASTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_BROADCASTER)、[`CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_BROADCAST_SRC_COUNT"></a>

## 320.91 `CONFIG_BT_BAP_BROADCAST_SRC_COUNT`

**提示（Prompt）**：基本音频广播发送端数量（Basic Audio Broadcaster source count）

**说明（Help）**

此选项设置支持的广播发送端（broadcast sources）数量。一个广播发送端可发送多个流（streams），每个发送端最多为 `BT_BAP_BROADCAST_SRC_STREAM_COUNT` 个。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_BROADCAST_SOURCE && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_ISO_MAX_BIG]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙广播发送端音频支持（Bluetooth Broadcast Source Audio Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SOURCE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SOURCE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_BIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_BIG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_BROADCAST_SRC_STREAM_COUNT"></a>

## 320.92 `CONFIG_BT_BAP_BROADCAST_SRC_STREAM_COUNT`

**提示（Prompt）**：基本音频广播发送端流数量（Basic Audio Broadcast Source Stream count）

**说明（Help）**

此选项设置每个广播发送端（broadcast source）支持的最大流（streams）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_BROADCAST_SOURCE && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_ISO_MAX_CHAN] if CONFIG_BT_ISO_MAX_CHAN < 31
[1, 31]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙广播发送端音频支持（Bluetooth Broadcast Source Audio Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SOURCE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SOURCE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_CHAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_CHAN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_BROADCAST_SRC_SUBGROUP_COUNT"></a>

## 320.93 `CONFIG_BT_BAP_BROADCAST_SRC_SUBGROUP_COUNT`

**提示（Prompt）**：基本音频广播发送端子组数量（Basic Audio Broadcast Source subgroup count）

**说明（Help）**

此选项设置每个广播发送端（broadcast source）支持的最大子组（subgroups）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_BROADCAST_SOURCE && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_ISO_MAX_CHAN] if CONFIG_BT_ISO_MAX_CHAN < 31
[1, 31]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙广播发送端音频支持（Bluetooth Broadcast Source Audio Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SOURCE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SOURCE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_CHAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_CHAN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_DEBUG_STREAM_DATA"></a>

## 320.94 `CONFIG_BT_BAP_DEBUG_STREAM_DATA`

**提示（Prompt）**：蓝牙音频流数据调试（Bluetooth Audio Stream data debug）

**说明（Help）**

此选项为蓝牙音频功能启用蓝牙音频流数据调试日志（Bluetooth Audio Stream data debug logs），记录所有接收和发送的音频数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_STREAM_LOG_LEVEL_DBG && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:268`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L268)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_STREAM_LOG_LEVEL_DBG)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_DEBUG_STREAM_SEQ_NUM"></a>

## 320.95 `CONFIG_BT_BAP_DEBUG_STREAM_SEQ_NUM`

**提示（Prompt）**：蓝牙音频流序列号调试（Bluetooth Audio Stream sequence number debug）

**说明（Help）**

此选项为蓝牙音频功能启用蓝牙音频流序列号调试日志（Bluetooth Audio Stream sequence number debugging logs）。如果应用提供了不符合预期的序列号（sequence numbers），会产生警告。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_STREAM_LOG_LEVEL >= CONFIG_BT_BAP_STREAM_LOG_LEVEL_WRN && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:282`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L282)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_STREAM_LOG_LEVEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_STREAM_LOG_LEVEL)、[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_WRN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_STREAM_LOG_LEVEL_WRN)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_BAP_STREAM_LOG_LEVEL`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_SCAN_DELEGATOR"></a>

## 320.96 `CONFIG_BT_BAP_SCAN_DELEGATOR`

**提示（Prompt）**：基本音频配置文件扫描委托方角色支持（Basic Audio Profile Scan Delegator role support）

**说明（Help）**

此选项启用扫描委托方角色（Scan Delegator role）及广播音频扫描服务（Broadcast Audio Scan Service，BASS）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_EXT_ADV && CONFIG_BT_PER_ADV_SYNC && CONFIG_BT_ISO_SYNC_RECEIVER && CONFIG_BT_OBSERVER && CONFIG_BT_GATT_DYNAMIC_DB && CONFIG_BT_BONDABLE && CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE >= 19 && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_PER_ADV_SYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC)、[`CONFIG_BT_ISO_SYNC_RECEIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_SYNC_RECEIVER)、[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_GATT_DYNAMIC_DB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_BT_BONDABLE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BONDABLE)、[`CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_SCAN_DELEGATOR_BUF_TIMEOUT"></a>

## 320.97 `CONFIG_BT_BAP_SCAN_DELEGATOR_BUF_TIMEOUT`

**提示（Prompt）**：并发访问 ASE 长读取缓冲区的处理超时，单位为毫秒（long read ASE buffer）

**说明（Help）**

如果另一个线程正在访问扫描委托方状态（scan delegator state），扫描委托方实现会先等待；此值指定其在拒绝读取或丢弃通知（notification）前等待的最大毫秒数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_SCAN_DELEGATOR && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
50
```

**取值范围（Ranges）**

```text
[0, 1000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:230`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L230)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 基本音频配置文件扫描委托方角色支持（Basic Audio Profile Scan Delegator role support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_SCAN_DELEGATOR`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_SCAN_DELEGATOR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_SCAN_DELEGATOR_RECV_STATE_COUNT"></a>

## 320.98 `CONFIG_BT_BAP_SCAN_DELEGATOR_RECV_STATE_COUNT`

**提示（Prompt）**：扫描委托方接收状态数量（Scan Delegator Receive State Count）

**说明（Help）**

设置服务器上的接收状态特征（receive state characteristics）数量。每个特征都可保存用于同步到周期性广播（periodic advertising）或广播等时流（broadcast isochronous stream）的信息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_SCAN_DELEGATOR && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 3]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 基本音频配置文件扫描委托方角色支持（Basic Audio Profile Scan Delegator role support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_SCAN_DELEGATOR`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_SCAN_DELEGATOR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_SHELL_USB_20_EXTENSION_DESC"></a>

## 320.99 `CONFIG_BT_BAP_SHELL_USB_20_EXTENSION_DESC`

**提示（Prompt）**：使用默认 USB 2.0 扩展描述符（default USB 2.0 Extension Descriptor）

**说明（Help）**

将 `bcdUSB` 值设为 `0201`，并使用默认 USB 2.0 扩展描述符（Extension Descriptor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_BOS_SUPPORT && CONFIG_LIBLC3 && CONFIG_USBD_AUDIO2_CLASS && CONFIG_BT_SHELL && CONFIG_BT_BAP_STREAM && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:333`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L333)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_USBD_BOS_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_BOS_SUPPORT)、[`CONFIG_LIBLC3`](P236_modules_liblc3_配置项参考.md#CONFIG_LIBLC3)、[`CONFIG_USBD_AUDIO2_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_AUDIO2_CLASS)、[`CONFIG_BT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SHELL)、[`CONFIG_BT_BAP_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_STREAM)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_BAP_STREAM`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_SHELL_USB_MAX_POWER"></a>

## 320.100 `CONFIG_BT_BAP_SHELL_USB_MAX_POWER`

**提示（Prompt）**：USB 设备示例的 bMaxPower 值（USB device sample bMaxPower value）

**说明（Help）**

示例配置（sample configuration）中的 `bMaxPower` 值，以 `2 mA` 为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIBLC3 && CONFIG_USBD_AUDIO2_CLASS && CONFIG_BT_SHELL && CONFIG_BT_BAP_STREAM && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
125
```

**取值范围（Ranges）**

```text
[0, 250]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:326`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L326)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_LIBLC3`](P236_modules_liblc3_配置项参考.md#CONFIG_LIBLC3)、[`CONFIG_USBD_AUDIO2_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_AUDIO2_CLASS)、[`CONFIG_BT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SHELL)、[`CONFIG_BT_BAP_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_STREAM)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_BAP_STREAM`、`CONFIG_BT_HCI_HOST`。

<!-- kconfig-navigation -->

[上一章](P319_subsys_bindesc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P321_subsys_bluetooth_配置项参考_2.md)
