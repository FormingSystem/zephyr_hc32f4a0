---
id: learning.zephyr-docs.kconfig-reference.page-321
title: "`subsys/bluetooth`配置项参考（2/13）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第321章\_`subsys/bluetooth`配置项参考（2/13）

本章翻译官方 Kconfig 数据库中 `subsys/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_BAP_SHELL_USB_PID"></a>

## 321.1 `CONFIG_BT_BAP_SHELL_USB_PID`

**提示（Prompt）**：USB 设备示例产品 ID（USB device sample Product ID）

**说明（Help）**

USB 设备示例的产品 ID（Product ID）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_LIBLC3 && CONFIG_USBD_AUDIO2_CLASS && CONFIG_BT_SHELL && CONFIG_BT_BAP_STREAM && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x0001
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:309`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L309)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_LIBLC3`](P236_modules_liblc3_配置项参考.md#CONFIG_LIBLC3)、[`CONFIG_USBD_AUDIO2_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_AUDIO2_CLASS)、[`CONFIG_BT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SHELL)、[`CONFIG_BT_BAP_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_STREAM)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_BAP_STREAM`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_SHELL_USB_PRODUCT"></a>

## 321.2 `CONFIG_BT_BAP_SHELL_USB_PRODUCT`

**提示（Prompt）**：USB 设备示例产品字符串（USB device sample product string）

**说明（Help）**

USB 设备示例的产品字符串（product string）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LIBLC3 && CONFIG_USBD_AUDIO2_CLASS && CONFIG_BT_SHELL && CONFIG_BT_BAP_STREAM && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
"Zephyr Audio Shell"
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:297`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L297)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_LIBLC3`](P236_modules_liblc3_配置项参考.md#CONFIG_LIBLC3)、[`CONFIG_USBD_AUDIO2_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_AUDIO2_CLASS)、[`CONFIG_BT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SHELL)、[`CONFIG_BT_BAP_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_STREAM)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_BAP_STREAM`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_SHELL_USB_REMOTE_WAKEUP"></a>

## 321.3 `CONFIG_BT_BAP_SHELL_USB_REMOTE_WAKEUP`

**提示（Prompt）**：USB 设备示例远程唤醒属性（USB device sample Remote Wakeup attribute）

**说明（Help）**

设置示例配置（sample configuration）中的远程唤醒属性（Remote Wakeup attribute）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIBLC3 && CONFIG_USBD_AUDIO2_CLASS && CONFIG_BT_SHELL && CONFIG_BT_BAP_STREAM && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:321`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L321)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_LIBLC3`](P236_modules_liblc3_配置项参考.md#CONFIG_LIBLC3)、[`CONFIG_USBD_AUDIO2_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_AUDIO2_CLASS)、[`CONFIG_BT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SHELL)、[`CONFIG_BT_BAP_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_STREAM)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_BAP_STREAM`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_SHELL_USB_SELF_POWERED"></a>

## 321.4 `CONFIG_BT_BAP_SHELL_USB_SELF_POWERED`

**提示（Prompt）**：USB 设备示例自供电属性（USB device sample Self-powered attribute）

**说明（Help）**

设置示例配置（sample configuration）中的自供电属性（Self-powered attribute）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIBLC3 && CONFIG_USBD_AUDIO2_CLASS && CONFIG_BT_SHELL && CONFIG_BT_BAP_STREAM && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:315`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L315)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_LIBLC3`](P236_modules_liblc3_配置项参考.md#CONFIG_LIBLC3)、[`CONFIG_USBD_AUDIO2_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_AUDIO2_CLASS)、[`CONFIG_BT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SHELL)、[`CONFIG_BT_BAP_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_STREAM)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_BAP_STREAM`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_SHELL_USB_VID"></a>

## 321.5 `CONFIG_BT_BAP_SHELL_USB_VID`

**提示（Prompt）**：USB 设备示例厂商 ID（USB device sample Vendor ID）

**说明（Help）**

USB 设备示例的厂商 ID（Vendor ID）。默认采用 Zephyr Project 的 ID。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_LIBLC3 && CONFIG_USBD_AUDIO2_CLASS && CONFIG_BT_SHELL && CONFIG_BT_BAP_STREAM && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x2fe3
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:303`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L303)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_LIBLC3`](P236_modules_liblc3_配置项参考.md#CONFIG_LIBLC3)、[`CONFIG_USBD_AUDIO2_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_AUDIO2_CLASS)、[`CONFIG_BT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SHELL)、[`CONFIG_BT_BAP_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_STREAM)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_BAP_STREAM`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_UNICAST_CLIENT"></a>

## 321.6 `CONFIG_BT_BAP_UNICAST_CLIENT`

**提示（Prompt）**：蓝牙单播音频客户端支持（Bluetooth Unicast Audio Client Support）

**说明（Help）**

此选项启用使用等时信道（Isochronous channels）的蓝牙单播音频客户端（Bluetooth Unicast Audio Client）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CLIENT && CONFIG_BT_GATT_AUTO_DISCOVER_CCC && CONFIG_BT_GATT_AUTO_UPDATE_MTU && CONFIG_BT_CENTRAL && CONFIG_BT_ISO_CENTRAL && CONFIG_BT_BONDABLE && CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE >= 19 && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_GATT_AUTO_DISCOVER_CCC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_AUTO_DISCOVER_CCC)、[`CONFIG_BT_GATT_AUTO_UPDATE_MTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_AUTO_UPDATE_MTU)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_ISO_CENTRAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_CENTRAL)、[`CONFIG_BT_BONDABLE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BONDABLE)、[`CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SNK_COUNT"></a>

## 321.7 `CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SNK_COUNT`

**提示（Prompt）**：基本音频配置文件 ASE 接收端数量（Basic Audio Profile ASE Sink count）

**说明（Help）**

此选项允许按连接缓存一定数量的基本音频配置文件（Basic Audio Profile）音频流端点接收端实例（Audio Stream Endpoint Sink instances）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_UNICAST_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_CLIENT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SRC_COUNT"></a>

## 321.8 `CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SRC_COUNT`

**提示（Prompt）**：基本音频配置文件 ASE 发送端数量（Basic Audio Profile ASE Source count）

**说明（Help）**

此选项允许按连接缓存一定数量的基本音频配置文件（Basic Audio Profile）音频流端点发送端实例（Audio Stream Endpoint Source instances）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_UNICAST_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_CLIENT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_UNICAST_CLIENT_GROUP_COUNT"></a>

## 321.9 `CONFIG_BT_BAP_UNICAST_CLIENT_GROUP_COUNT`

**提示（Prompt）**：基本音频单播组数量（Basic Audio Unicast Group count）

**说明（Help）**

此选项设置作为单播客户端（unicast client）时支持的已连接音频组（connected audio groups）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_UNICAST_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ISO_MAX_CIG
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_ISO_MAX_CIG]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_CLIENT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_CIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_CIG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_UNICAST_CLIENT_GROUP_STREAM_COUNT"></a>

## 321.10 `CONFIG_BT_BAP_UNICAST_CLIENT_GROUP_STREAM_COUNT`

**提示（Prompt）**：基本音频配置文件单播组的连接等时流数量（Connected Isochronous Stream，CIS count）

**说明（Help）**

此选项设置每个单播组（unicast group）支持的最大 CIS 数量。由于 BAP 流（streams）是单向的，两个 BAP 流可以共用一个 CIS，因此每组 BAP 音频流数量最多可达该值的两倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAP_UNICAST_CLIENT_GROUP_COUNT > 0 && CONFIG_BT_BAP_UNICAST_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
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

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_CLIENT_GROUP_COUNT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_CLIENT_GROUP_COUNT)、[`CONFIG_BT_BAP_UNICAST_CLIENT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_CHAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_CHAN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAP_UNICAST_SERVER"></a>

## 321.11 `CONFIG_BT_BAP_UNICAST_SERVER`

**提示（Prompt）**：蓝牙单播音频服务器支持（Bluetooth Unicast Audio Server Support）

**说明（Help）**

此选项启用使用等时信道（Isochronous channels）的蓝牙单播音频服务器（Bluetooth Unicast Audio Server）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_DYNAMIC_DB && CONFIG_BT_PERIPHERAL && CONFIG_BT_ISO_PERIPHERAL && CONFIG_BT_ASCS && CONFIG_BT_BONDABLE && CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE >= 19 && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_PAC_SNK if CONFIG_BT_ASCS_ASE_SNK
CONFIG_BT_PAC_SRC if CONFIG_BT_ASCS_ASE_SRC
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.bap:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.bap#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_DYNAMIC_DB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_ISO_PERIPHERAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_PERIPHERAL)、[`CONFIG_BT_ASCS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ASCS)、[`CONFIG_BT_BONDABLE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BONDABLE)、[`CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PAC_SNK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PAC_SNK)、[`CONFIG_BT_ASCS_ASE_SNK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ASCS_ASE_SNK)、[`CONFIG_BT_PAC_SRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PAC_SRC)、[`CONFIG_BT_ASCS_ASE_SRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ASCS_ASE_SRC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_ASCS_ASE_SNK`、`CONFIG_BT_ASCS_ASE_SRC`。

<a id="CONFIG_BT_BAS"></a>

## 321.12 `CONFIG_BT_BAS`

**提示（Prompt）**：GATT 电池服务（GATT Battery service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/bas/Kconfig.bas:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/bas/Kconfig.bas#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAS_BCS"></a>

## 321.13 `CONFIG_BT_BAS_BCS`

**提示（Prompt）**：电池临界状态（Battery Critical Status）

**说明（Help）**

启用此选项以包含电池临界状态特征（Battery Critical Status Characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAS_BLS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/bas/Kconfig.bas:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/bas/Kconfig.bas#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 电池电量状态（Battery Level Status）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAS_BLS`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAS_BLS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAS_BLS"></a>

## 321.14 `CONFIG_BT_BAS_BLS`

**提示（Prompt）**：电池电量状态（Battery Level Status）

**说明（Help）**

启用此选项以包含电池电量状态特征（Battery Level Status Characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/bas/Kconfig.bas:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/bas/Kconfig.bas#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAS_BLS_ADDITIONAL_STATUS_PRESENT"></a>

## 321.15 `CONFIG_BT_BAS_BLS_ADDITIONAL_STATUS_PRESENT`

**提示（Prompt）**：提供附加电池状态（Additional Battery Status Present）

**说明（Help）**

如果提供附加电池状态信息（Additional Battery Status information），则启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAS_BLS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/bas/Kconfig.bas:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/bas/Kconfig.bas#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 电池电量状态（Battery Level Status）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAS_BLS`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAS_BLS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAS_BLS_BATTERY_LEVEL_PRESENT"></a>

## 321.16 `CONFIG_BT_BAS_BLS_BATTERY_LEVEL_PRESENT`

**提示（Prompt）**：提供电池电量（Battery Level Present）

**说明（Help）**

如果提供电池电量（Battery Level），则启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAS_BLS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/bas/Kconfig.bas:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/bas/Kconfig.bas#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 电池电量状态（Battery Level Status）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAS_BLS`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAS_BLS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BAS_BLS_IDENTIFIER_PRESENT"></a>

## 321.17 `CONFIG_BT_BAS_BLS_IDENTIFIER_PRESENT`

**提示（Prompt）**：提供电池电量标识符（Battery Level Identifier Present）

**说明（Help）**

如果提供电池电量标识符（Battery Level Identifier），则启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BAS_BLS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/bas/Kconfig.bas:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/bas/Kconfig.bas#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 电池电量状态（Battery Level Status）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAS_BLS`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAS_BLS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BIP"></a>

## 321.18 `CONFIG_BT_BIP`

**提示（Prompt）**：蓝牙基本成像配置文件（Bluetooth BIP Profile）[实验性，EXPERIMENTAL]

**说明（Help）**

此选项启用基本成像配置文件（BIP profile）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_GOEP
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_BT_AVRCP_TG_COVER_ART
CONFIG_BT_AVRCP_CT_COVER_ART
CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE_PROPERTIES
CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE
CONFIG_BT_AVRCP_CT_COVER_ART_GET_LINKED_THUMBNAIL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:769`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L769)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_GOEP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GOEP)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_AVRCP_TG_COVER_ART`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_TG_COVER_ART)、[`CONFIG_BT_AVRCP_CT_COVER_ART`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CT_COVER_ART)、[`CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE_PROPERTIES`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE_PROPERTIES)、[`CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE)、[`CONFIG_BT_AVRCP_CT_COVER_ART_GET_LINKED_THUMBNAIL`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_CT_COVER_ART_GET_LINKED_THUMBNAIL)。

<a id="CONFIG_BT_BONDABLE"></a>

## 321.19 `CONFIG_BT_BONDABLE`

**提示（Prompt）**：可绑定模式（Bondable Mode）

**说明（Help）**

此选项规定任意 ACL 连接的绑定标志（bonding flag）默认值。选项为真时，默认绑定标志为真；否则默认标志为假。建立连接后，如果启用了按连接设置绑定标志（the bonding flag per-connection）的配置 `BT_BONDABLE_PER_CONNECTION`，还可以调用 `bt_conn_set_bondable()` 修改该连接的绑定标志。请参阅 `BT_BONDABLE_PER_CONNECTION` 配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:733`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L733)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BONDABLE_PER_CONNECTION"></a>

## 321.20 `CONFIG_BT_BONDABLE_PER_CONNECTION`

**提示（Prompt）**：按连接设置／清除绑定标志（Set/clear the bonding flag per-connection）

**说明（Help）**

启用 `bt_conn_set_bondable` API 函数支持；该函数用于按连接设置／清除绑定标志（bonding flag）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:753`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L753)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BONDING_REQUIRED"></a>

## 321.21 `CONFIG_BT_BONDING_REQUIRED`

**提示（Prompt）**：始终要求绑定（Always require bonding）

**说明（Help）**

启用此选项后，远端设备必须始终在配对请求（pairing request）中设置可绑定标志（bondable flag）。任何其他形式的请求都会被拒绝。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BONDABLE && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:745`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L745)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support） → 可绑定模式（Bondable Mode）

**配置项引用（Symbol References）**：[`CONFIG_BT_BONDABLE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BONDABLE)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BROADCASTER"></a>

## 321.22 `CONFIG_BT_BROADCASTER`

**提示（Prompt）**：广播者角色支持（Broadcaster Role support）

**说明（Help）**

选择此项以支持低功耗蓝牙广播者角色（LE Broadcaster role）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if !CONFIG_BT_OBSERVER
```

**被选择（Selected by）**

```text
CONFIG_BT_PERIPHERAL
CONFIG_BT_ISO_BROADCASTER
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_ISO_BROADCASTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_BROADCASTER)。

<a id="CONFIG_BT_BR_MIN_ENC_KEY_SIZE"></a>

## 321.23 `CONFIG_BT_BR_MIN_ENC_KEY_SIZE`

**提示（Prompt）**：接受的最小加密密钥长度，单位为八位字节（Minimum encryption key size accepted in octets）

**说明（Help）**

此选项设置经典蓝牙（classic）配对期间接受的最小加密密钥长度（encryption key size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_SMP_MIN_ENC_KEY_SIZE
```

**取值范围（Ranges）**

```text
[7, 16]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SMP_MIN_ENC_KEY_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP_MIN_ENC_KEY_SIZE)。

<a id="CONFIG_BT_BUF_ACL_RX_COUNT_EXTRA"></a>

## 321.24 `CONFIG_BT_BUF_ACL_RX_COUNT_EXTRA`

**提示（Prompt）**：额外的入站 ACL 数据缓冲区数量（Number of extra incoming ACL data buffers）

**说明（Help）**

从控制器（Controller）发送到主机（Host）的额外入站 ACL 数据缓冲区数量。默认情况下，为支持 L2CAP 重组（recombination），入站 ACL 数据缓冲区总数等于 `CONFIG_BT_MAX_CONN + 1`。主机中的 L2CAP 重组会为每条连接保留第一个接收缓冲区（Rx buffer），并让所有连接共用一个 Rx 缓冲区，以接收来自控制器的分片（fragment）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MAX_CONN if CONFIG_BT_CONN
0
```

**取值范围（Ranges）**

```text
[1, 65535] if CONFIG_BT_CONN
[0, 0]
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙缓冲区配置（Bluetooth buffer configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MAX_CONN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_CONN)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)。

<a id="CONFIG_BT_BUF_ACL_RX_SIZE"></a>

## 321.25 `CONFIG_BT_BUF_ACL_RX_SIZE`

**提示（Prompt）**：入站数据支持的最大 ACL 大小（Maximum supported ACL size for incoming data）

**说明（Help）**

从控制器（Controller）发送到主机（Host）的数据包所支持的最大 ACL 大小，不包含 HCI ACL 头（header）。

在主机与控制器合并构建（combined Host and Controller build）中，两者都采用该值设置缓冲区大小，因此不严格要求控制器到主机的流控（Controller to Host flow control）。

在仅主机构建（Host only build）中，如果启用了控制器到主机的流控，主机会在 `Host Buffer Size` 命令中设置此值，告知控制器其可发送的最大 ACL 数据大小。如果未启用此流控，控制器可假定主机接收和处理 ACL 数据的速度高于控制器生成数据的速度。

在仅控制器构建（Controller only build）中，此值决定控制器发送给主机的最大 ACL 大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
676 if CONFIG_BT_CLASSIC && CONFIG_BT_HID_HOST
265 if CONFIG_BT_CLASSIC && CONFIG_BT_GOEP
200 if CONFIG_BT_CLASSIC
70 if CONFIG_BT_EATT
69 if CONFIG_BT_SMP
37 if CONFIG_BT_MESH_GATT
27
```

**取值范围（Ranges）**

```text
[676, 65535] if CONFIG_BT_CLASSIC && CONFIG_BT_HID_HOST
[264, 65535] if CONFIG_BT_CLASSIC && CONFIG_BT_GOEP
[70, 65535] if CONFIG_BT_EATT
[69, 65535] if CONFIG_BT_SMP
[27, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙缓冲区配置（Bluetooth buffer configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HID_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HID_HOST)、[`CONFIG_BT_GOEP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GOEP)、[`CONFIG_BT_EATT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_EATT)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_MESH_GATT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_GATT`。

<a id="CONFIG_BT_BUF_ACL_TX_COUNT"></a>

## 321.26 `CONFIG_BT_BUF_ACL_TX_COUNT`

**提示（Prompt）**：出站 ACL 数据缓冲区数量（Number of outgoing ACL data buffers）

**说明（Help）**

从主机（Host）发送到控制器（Controller）的出站 ACL 数据缓冲区数量。它决定主机能够在控制器中排队的数据包最大数量；达到上限后，主机须等待控制器通过已完成数据包数量事件（Number of Completed Packets event）通知其可以继续排队。所有连接共享这些缓冲区，由主机决定如何在各连接间分配。控制器会在 HCI `LE Read Buffer Size` 命令响应中返回该值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
7 if CONFIG_BT_HCI_RAW
4 if CONFIG_BT_MESH_GATT
3
```

**取值范围（Ranges）**

```text
[1, 255]
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/mchp_rnbd451_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/mchp_rnbd451_bt/Kconfig.defconfig)。

```text
12
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙缓冲区配置（Bluetooth buffer configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)、[`CONFIG_BT_MESH_GATT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_GATT`。

<a id="CONFIG_BT_BUF_ACL_TX_SIZE"></a>

## 321.27 `CONFIG_BT_BUF_ACL_TX_SIZE`

**提示（Prompt）**：出站数据支持的最大 ACL 大小（Maximum supported ACL size for outgoing data）

**说明（Help）**

从主机（Host）发送到控制器（Controller）的数据包所支持的最大 ACL 大小，不包含 HCI ACL 头（header）。在合并构建（combined build）中，主机和控制器均设置此值。在仅主机构建（Host-only build）中，主机读取控制器支持的最大 ACL 大小，并采用双方支持值中的较小值。

主机支持发送大于 ACL 大小的 L2CAP 协议数据单元（PDUs），并将这些 L2CAP PDU 分片为 ACL 数据包。控制器会在 HCI `LE Read Buffer Size` 命令响应中返回该值。

如果该大小大于实际有效的链路层传输大小（Link Layer transmission size），控制器会在通过空中接口发送数据包之前进行分片。如果该值小于实际有效的链路层传输大小，则会限制链路层的最大传输大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
37 if CONFIG_BT_MESH_GATT
27
```

**取值范围（Ranges）**

```text
[27, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙缓冲区配置（Bluetooth buffer configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_GATT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_GATT`。

<a id="CONFIG_BT_BUF_CMD_TX_COUNT"></a>

## 321.28 `CONFIG_BT_BUF_CMD_TX_COUNT`

**提示（Prompt）**：HCI 命令缓冲区数量（Number of HCI command buffers）

**说明（Help）**

可供主机（Host）发送 HCI 命令使用的缓冲区数量。HCI 控制器（Controllers）可能不支持 `Num_HCI_Command_Packets > 1`；因此，当未启用控制器到主机的数据流控（`BT_HCI_ACL_FLOW_CONTROL`）、读取远端版本信息（`BT_REMOTE_VERSION`）、自动发起 PHY 更新（`BT_AUTO_PHY_CENTRAL` 和 `BT_AUTO_PHY_PERIPHERAL` 选择项）或自动发起数据长度更新（`BT_AUTO_DATA_LEN_UPDATE`）时，默认数量为 `1`。

普通 HCI 命令遵循 HCI 命令流控（command flow control），使用 HCI 命令完成与状态事件返回的 `Num_HCI_Command_Packets`。`Host Number of Completed Packets` 命令不遵循普通 HCI 命令的流控；控制器侧以 `K_NO_WAIT` 分配 HCI 命令缓冲区的 HCI 驱动可能最终耗尽命令缓冲区。

在仅主机构建或主机加控制器合并构建中启用控制器到主机的数据流控时，会综合考虑已启用的自动发起过程（auto-initiated procedures）来调整内部的 `BT_BUF_CMD_TX_COUNT`，同时遵循普通 HCI 命令流控，使其能够向控制器发送 `Ncmd` 个普通 HCI 命令，以及 `BT_BUF_ACL_RX_COUNT` 个 `Host Number of Completed Packets` 命令。

在仅控制器构建中支持控制器到主机的数据流控时，内部 `BT_BUF_CMD_TX_COUNT` 调整为 `(BT_BUF_RX_COUNT + Ncmd)`；其中 `Ncmd` 为控制器实现所支持的最大 `Num_HCI_Command_Packets`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(!CONFIG_BT_HCI_RAW || !CONFIG_HAS_BT_CTLR || !CONFIG_BT_HCI_ACL_FLOW_CONTROL) && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2 if CONFIG_BT_MESH
1
```

**取值范围（Ranges）**

```text
[2, 64] if CONFIG_BT_MESH
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙缓冲区配置（Bluetooth buffer configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI_ACL_FLOW_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_ACL_FLOW_CONTROL)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_BUF_CMD_TX_SIZE"></a>

## 321.29 `CONFIG_BT_BUF_CMD_TX_SIZE`

**提示（Prompt）**：支持的最大 HCI 命令缓冲区长度（Maximum support HCI Command buffer length）

**说明（Help）**

每个 HCI 命令缓冲区（Command buffer）的最大数据大小，不包含 HCI 命令头（Command header）。主机和控制器都用此值确定包含 HCI 命令的缓冲区大小。应根据该配置下预期会发送的 HCI 命令设置。如果无法确定可能使用的 HCI 命令子集，应设为最大值 `255`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
255 if CONFIG_BT_EXT_ADV || CONFIG_BT_CLASSIC || CONFIG_BT_ISO_CENTRAL || CONFIG_BT_CHANNEL_SOUNDING
83 if !CONFIG_BT_EXT_ADV && !CONFIG_BT_CLASSIC && CONFIG_BT_CTLR_DF && CONFIG_BT_CTLR_DF_CONN_CTE_REQ && !CONFIG_SOC_COMPATIBLE_NRF
65
```

**取值范围（Ranges）**

```text
[65, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙缓冲区配置（Bluetooth buffer configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_ISO_CENTRAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_CENTRAL)、[`CONFIG_BT_CHANNEL_SOUNDING`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CHANNEL_SOUNDING)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_BT_CTLR_DF_CONN_CTE_REQ`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CONN_CTE_REQ)、[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF`。

<a id="CONFIG_BT_BUF_EVT_DISCARDABLE_COUNT"></a>

## 321.30 `CONFIG_BT_BUF_EVT_DISCARDABLE_COUNT`

**提示（Prompt）**：可丢弃 HCI 事件缓冲区数量（Number of discardable HCI Event buffers）

**说明（Help）**

专用缓冲池（buffer pool）中的缓冲区数量，用于 HCI 驱动认为可丢弃（discardable）的事件，例如广播报告（Advertising Reports）。使用这种缓冲池的好处是：即使此类事件大量涌入，也不会阻塞其他关键事件的缓冲区分配，某些情况下甚至可以消除死锁（deadlocks）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
20 if CONFIG_BT_MESH
3
```

**取值范围（Ranges）**

```text
[1, 255]
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/mchp_rnbd451_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/mchp_rnbd451_bt/Kconfig.defconfig)。

```text
12
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BUF_EVT_DISCARDABLE_SIZE"></a>

## 321.31 `CONFIG_BT_BUF_EVT_DISCARDABLE_SIZE`

**提示（Prompt）**：支持的最大可丢弃 HCI 事件缓冲区长度（Maximum supported discardable HCI Event buffer length）

**说明（Help）**

专用可丢弃事件缓冲池（discardable event buffer pool）所支持的最大 HCI 事件大小，不包含 HCI 事件头（Event header）。最小大小依据广播报告（Advertising Report）确定。将此缓冲区大小设为不同于 `BT_BUF_EVT_RX_SIZE` 的值，可以节省内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
255 if CONFIG_BT_CLASSIC
43 if !CONFIG_BT_EXT_ADV
58 if CONFIG_BT_EXT_ADV && CONFIG_BT_MESH
CONFIG_BT_BUF_EVT_RX_SIZE if CONFIG_BT_EXT_ADV
```

**取值范围（Ranges）**

```text
[43, 255] if !CONFIG_BT_EXT_ADV
[58, 255] if CONFIG_BT_EXT_ADV
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_MESH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH)、[`CONFIG_BT_BUF_EVT_RX_SIZE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BUF_EVT_RX_SIZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_BUF_EVT_RX_COUNT"></a>

## 321.32 `CONFIG_BT_BUF_EVT_RX_COUNT`

**提示（Prompt）**：HCI 事件缓冲区数量（Number of HCI Event buffers）

**说明（Help）**

可用于接收控制器（Controller）传入 HCI 事件（events）的缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
20 if CONFIG_BT_MESH && !(CONFIG_BT_BUF_EVT_DISCARDABLE_COUNT > 0)
10
```

**取值范围（Ranges）**

```text
[2, 255]
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/mchp_rnbd451_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/mchp_rnbd451_bt/Kconfig.defconfig)。

```text
13
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙缓冲区配置（Bluetooth buffer configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH)、[`CONFIG_BT_BUF_EVT_DISCARDABLE_COUNT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BUF_EVT_DISCARDABLE_COUNT)。

<a id="CONFIG_BT_BUF_EVT_RX_SIZE"></a>

## 321.33 `CONFIG_BT_BUF_EVT_RX_SIZE`

**提示（Prompt）**：支持的最大 HCI 事件缓冲区长度（Maximum supported HCI Event buffer length）

**说明（Help）**

支持的最大 HCI 事件缓冲区（event buffer）大小，不包含 HCI 事件头（Event header）。主机和控制器都用此值确定包含 HCI 事件的缓冲区大小。应根据该配置下预期可能生成的 HCI 事件设置。如果无法确定可能出现的 HCI 事件子集，应设为最大值 `255`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
255 if (CONFIG_BT_EXT_ADV && CONFIG_BT_OBSERVER) || CONFIG_BT_PER_ADV_SYNC || CONFIG_BT_DF_CONNECTION_CTE_RX || CONFIG_BT_CLASSIC || CONFIG_BT_CHANNEL_SOUNDING || CONFIG_BT_LE_EXTENDED_FEAT_SET
68
```

**取值范围（Ranges）**

```text
[68, 255]
[78, 255] if CONFIG_BT_CHANNEL_SOUNDING
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙缓冲区配置（Bluetooth buffer configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_PER_ADV_SYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC)、[`CONFIG_BT_DF_CONNECTION_CTE_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DF_CONNECTION_CTE_RX)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_CHANNEL_SOUNDING`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CHANNEL_SOUNDING)、[`CONFIG_BT_LE_EXTENDED_FEAT_SET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LE_EXTENDED_FEAT_SET)。

<a id="CONFIG_BT_BUF_SYNC_EVT_POOL_COUNT"></a>

## 321.34 `CONFIG_BT_BUF_SYNC_EVT_POOL_COUNT`

**提示（Prompt）**：同步事件缓冲池数量（Sync event buffer pool count）

**说明（Help）**

此选项允许厂商根据应用需求配置同步事件缓冲区（sync event buffers）的数量。同步事件缓冲池数量的默认值为 `1`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1175)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_CAP_ACCEPTOR"></a>

## 321.35 `CONFIG_BT_CAP_ACCEPTOR`

**提示（Prompt）**：通用音频配置文件接受方角色支持（Common Audio Profile Acceptor Role Support）

**说明（Help）**

启用后将启用 CAP 接受方角色（Acceptor role），并实例化通用音频服务（Common Audio Service，CAS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_BAP_UNICAST_SERVER || (CONFIG_BT_BAP_BROADCAST_SINK && CONFIG_BT_BAP_SCAN_DELEGATOR)) && CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE >= 4 && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.cap:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.cap#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_SERVER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_SERVER)、[`CONFIG_BT_BAP_BROADCAST_SINK`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SINK)、[`CONFIG_BT_BAP_SCAN_DELEGATOR`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_SCAN_DELEGATOR)、[`CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CAP_ACCEPTOR_SET_MEMBER"></a>

## 321.36 `CONFIG_BT_CAP_ACCEPTOR_SET_MEMBER`

**提示（Prompt）**：通用音频配置文件接受方角色的集合成员支持（Common Audio Profile Acceptor Role Set Member support）

**说明（Help）**

启用后，CAP 接受方（acceptor）可作为集合成员（set member）。此时需要手动注册 CAS 服务，并会占用一个已分配的 CSIS 实例（`BT_CSIP_SET_MEMBER_MAX_INSTANCE_COUNT`）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CAP_ACCEPTOR && CONFIG_BT_CSIP_SET_MEMBER && CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT && CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT && CONFIG_BT_GATT_DYNAMIC_DB && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.cap:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.cap#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 通用音频配置文件接受方角色支持（Common Audio Profile Acceptor Role Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_ACCEPTOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CAP_ACCEPTOR)、[`CONFIG_BT_CSIP_SET_MEMBER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER)、[`CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT)、[`CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT)、[`CONFIG_BT_GATT_DYNAMIC_DB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CAP_COMMANDER"></a>

## 321.37 `CONFIG_BT_CAP_COMMANDER`

**提示（Prompt）**：通用音频配置文件发起方角色支持（Common Audio Profile Initiator Role Support）

**说明（Help）**

启用后将启用 CAP 发起方角色（Initiator role）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
((CONFIG_BT_BAP_BROADCAST_ASSISTANT && CONFIG_BT_BAP_SCAN_DELEGATOR && CONFIG_BT_CSIP_SET_COORDINATOR) || (CONFIG_BT_BAP_SCAN_DELEGATOR && CONFIG_BT_CSIP_SET_COORDINATOR) || (CONFIG_BT_VCP_VOL_CTLR && CONFIG_BT_CSIP_SET_COORDINATOR) || (CONFIG_BT_MICP_MIC_CTLR && CONFIG_BT_CSIP_SET_COORDINATOR) || CONFIG_BT_TBS_CLIENT || CONFIG_BT_MCC) && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.cap:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.cap#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_ASSISTANT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT)、[`CONFIG_BT_BAP_SCAN_DELEGATOR`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_SCAN_DELEGATOR)、[`CONFIG_BT_CSIP_SET_COORDINATOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_COORDINATOR)、[`CONFIG_BT_VCP_VOL_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_VCP_VOL_CTLR)、[`CONFIG_BT_MICP_MIC_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MICP_MIC_CTLR)、[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_MCC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CAP_HANDOVER"></a>

## 321.38 `CONFIG_BT_CAP_HANDOVER`

**提示（Prompt）**：通用音频配置文件切换过程（Common Audio Profile Handover Procedures）

**说明（Help）**

启用 CAP 切换过程（Handover procedures）支持，允许设备在某个使用场景中切换广播（broadcast）和单播（unicast）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CAP_COMMANDER && CONFIG_BT_CAP_INITIATOR && CONFIG_BT_BAP_BROADCAST_ASSISTANT && CONFIG_BT_BAP_BROADCAST_SOURCE && CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SNK_COUNT > 0 && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.cap:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.cap#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 通用音频配置文件发起方角色支持（Common Audio Profile Initiator Role Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMANDER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CAP_COMMANDER)、[`CONFIG_BT_CAP_INITIATOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CAP_INITIATOR)、[`CONFIG_BT_BAP_BROADCAST_ASSISTANT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT)、[`CONFIG_BT_BAP_BROADCAST_SOURCE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SOURCE)、[`CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SNK_COUNT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SNK_COUNT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CAP_INITIATOR"></a>

## 321.39 `CONFIG_BT_CAP_INITIATOR`

**提示（Prompt）**：通用音频配置文件发起方角色支持（Common Audio Profile Initiator Role Support）

**说明（Help）**

启用后将启用 CAP 发起方角色（Initiator role）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
((CONFIG_BT_BAP_UNICAST_CLIENT && CONFIG_BT_CSIP_SET_COORDINATOR) || CONFIG_BT_BAP_BROADCAST_SOURCE) && CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE >= 4 && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.cap:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.cap#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_CLIENT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_CLIENT)、[`CONFIG_BT_CSIP_SET_COORDINATOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_COORDINATOR)、[`CONFIG_BT_BAP_BROADCAST_SOURCE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SOURCE)、[`CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CCP_CALL_CONTROL_CLIENT"></a>

## 321.40 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT`

**提示（Prompt）**：呼叫控制配置文件客户端支持（Call Control Profile Client Support）

**说明（Help）**

此选项启用呼叫控制配置文件客户端（Call Control Profile Client）支持；该客户端使用电话承载服务（Telephone Bearer Service，TBS）客户端控制远端设备上的呼叫（calls）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_EXT_ADV && CONFIG_BT_TBS_CLIENT && CONFIG_BT_BONDABLE && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.ccp:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.ccp#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_BONDABLE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BONDABLE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CCP_CALL_CONTROL_CLIENT_BEARER_COUNT"></a>

## 321.41 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_BEARER_COUNT`

**提示（Prompt）**：电话承载数量（Telephone bearer count）

**说明（Help）**

CCP 呼叫控制客户端（Call Control Client）支持的电话承载（telephone bearers）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CCP_CALL_CONTROL_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255] if CONFIG_BT_TBS_CLIENT_TBS
[1, 1]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.ccp:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.ccp#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件客户端支持（Call Control Profile Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_TBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_TBS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CCP_CALL_CONTROL_CLIENT_CB_USER_DATA"></a>

## 321.42 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_CB_USER_DATA`

**提示（Prompt）**：呼叫控制配置文件客户端回调中的 user_data 支持（user_data in callbacks）

**说明（Help）**

此选项启用呼叫控制配置文件客户端（Call Control Profile Client）回调中的 `user_data` 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CCP_CALL_CONTROL_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.ccp:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.ccp#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件客户端支持（Call Control Profile Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CCP_CALL_CONTROL_SERVER"></a>

## 321.43 `CONFIG_BT_CCP_CALL_CONTROL_SERVER`

**提示（Prompt）**：呼叫控制配置文件呼叫控制服务器支持（Call Control Profile Call Control Server Support）

**说明（Help）**

此选项启用呼叫控制配置文件呼叫控制服务器（Call Control Profile Call Control Server）支持；该服务器使用电话承载服务（Telephone Bearer Service，TBS）保存并控制设备上的呼叫（calls）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_EXT_ADV && CONFIG_BT_TBS && CONFIG_BT_BONDABLE && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.ccp:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.ccp#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_TBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS)、[`CONFIG_BT_BONDABLE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BONDABLE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CCP_CALL_CONTROL_SERVER_BEARER_COUNT"></a>

## 321.44 `CONFIG_BT_CCP_CALL_CONTROL_SERVER_BEARER_COUNT`

**提示（Prompt）**：电话承载数量（Telephone bearer count）

**说明（Help）**

CCP 呼叫控制服务器（Call Control Server）支持的电话承载（telephone bearers）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CCP_CALL_CONTROL_SERVER && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.ccp:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.ccp#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件呼叫控制服务器支持（Call Control Profile Call Control Server Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_SERVER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CCP_CALL_CONTROL_SERVER_PROVIDER_NAME_MAX_LENGTH"></a>

## 321.45 `CONFIG_BT_CCP_CALL_CONTROL_SERVER_PROVIDER_NAME_MAX_LENGTH`

**提示（Prompt）**：承载提供方名称的最大长度，不含空终止符（bearer provider name, excluding null terminator）

**说明（Help）**

设置承载提供方名称（bearer provider name）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CCP_CALL_CONTROL_SERVER && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_TBS_MAX_PROVIDER_NAME_LENGTH
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_TBS_MAX_PROVIDER_NAME_LENGTH]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.ccp:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.ccp#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件呼叫控制服务器支持（Call Control Profile Call Control Server Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_SERVER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_MAX_PROVIDER_NAME_LENGTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_MAX_PROVIDER_NAME_LENGTH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CCP_CALL_CONTROL_SERVER_URI_SCHEMES_MAX_LENGTH"></a>

## 321.46 `CONFIG_BT_CCP_CALL_CONTROL_SERVER_URI_SCHEMES_MAX_LENGTH`

**提示（Prompt）**：承载 URI 方案支持列表的最大长度，不含空终止符（bearer URI schemes support list）

**说明（Help）**

设置承载 URI 方案支持列表（bearer URI schemes support list）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CCP_CALL_CONTROL_SERVER && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_TBS_MAX_SCHEME_LIST_LENGTH
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_TBS_MAX_SCHEME_LIST_LENGTH]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.ccp:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.ccp#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件呼叫控制服务器支持（Call Control Profile Call Control Server Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_SERVER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_MAX_SCHEME_LIST_LENGTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_MAX_SCHEME_LIST_LENGTH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CENTRAL"></a>

## 321.47 `CONFIG_BT_CENTRAL`

原库同名定义共 2 条；本项为数据库第 1686 条记录，各定义分别保留。

**提示（Prompt）**：中心设备角色支持（Central Role support）

**说明（Help）**

选择此项以支持低功耗蓝牙中心设备角色（LE Central role）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HCI_RAW
```

**主动选择（Selects）**

```text
CONFIG_BT_OBSERVER
CONFIG_BT_CONN
```

**被选择（Selected by）**

```text
CONFIG_BT_CLASSIC
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)、[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)。

<a id="CONFIG_BT_CHANNEL_SOUNDING"></a>

## 321.48 `CONFIG_BT_CHANNEL_SOUNDING`

**提示（Prompt）**：信道探测（Channel Sounding）[实验性，EXPERIMENTAL]

**说明（Help）**

启用蓝牙 6.0 信道探测（Bluetooth 6.0 Channel Sounding）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_CHANNEL_SOUNDING_SUPPORT) && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:231`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L231)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_CHANNEL_SOUNDING_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CHANNEL_SOUNDING_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_CHANNEL_SOUNDING_SUPPORT`。

<a id="CONFIG_BT_CHANNEL_SOUNDING_REASSEMBLY_BUFFER_CNT"></a>

## 321.49 `CONFIG_BT_CHANNEL_SOUNDING_REASSEMBLY_BUFFER_CNT`

**提示（Prompt）**：子事件结果重组缓冲区数量（Subevent result reassembly buffer count）

**说明（Help）**

控制信道探测（CS）子事件结果重组缓冲区（reassembly buffers）的数量。每个运行中的 CS 过程（procedure）分配一个缓冲区，并发 CS 过程数量受此值限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CHANNEL_SOUNDING && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_MAX_CONN]
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:255`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L255)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 信道探测（Channel Sounding）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CHANNEL_SOUNDING`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CHANNEL_SOUNDING)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MAX_CONN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_CONN)。

<a id="CONFIG_BT_CHANNEL_SOUNDING_REASSEMBLY_BUFFER_SIZE"></a>

## 321.50 `CONFIG_BT_CHANNEL_SOUNDING_REASSEMBLY_BUFFER_SIZE`

**提示（Prompt）**：子事件结果重组缓冲区大小（Subevent result reassembly buffer size）

**说明（Help）**

当一个信道探测（CS）子事件的结果无法放入单个 HCI 事件时，结果会拆分到多个事件中，随后重组为完整的 CS 子事件。此配置设置重组缓冲区（reassembly buffer）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CHANNEL_SOUNDING && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
5600
```

**取值范围（Ranges）**

```text
[239, 5600]
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:245`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L245)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 信道探测（Channel Sounding）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CHANNEL_SOUNDING`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CHANNEL_SOUNDING)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_CHANNEL_SOUNDING_TEST"></a>

## 321.51 `CONFIG_BT_CHANNEL_SOUNDING_TEST`

**提示（Prompt）**：信道探测测试（Channel Sounding Test）[实验性，EXPERIMENTAL]

**说明（Help）**

启用信道探测测试模式（Channel Sounding test mode）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CHANNEL_SOUNDING && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:238`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L238)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 信道探测（Channel Sounding）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CHANNEL_SOUNDING`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CHANNEL_SOUNDING)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_BT_CLASSIC"></a>

## 321.52 `CONFIG_BT_CLASSIC`

**提示（Prompt）**：蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**说明（Help）**

此选项启用蓝牙基本速率／增强数据速率（Bluetooth BR/EDR）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_PERIPHERAL
CONFIG_BT_CENTRAL
CONFIG_BT_SMP
CONFIG_BT_L2CAP_DYNAMIC_CHANNEL
CONFIG_CRC
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_L2CAP_DYNAMIC_CHANNEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_DYNAMIC_CHANNEL)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_COD"></a>

## 321.53 `CONFIG_BT_COD`

**提示（Prompt）**：蓝牙设备类别（Bluetooth Class of Device，CoD）

**说明（Help）**

此选项设置设备类别（class of device）。可用值列表请参阅 [Bluetooth 分配编号（Assigned Numbers）](https://www.bluetooth.com/specifications/assigned-numbers)。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:684`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L684)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_COMPANY_ID"></a>

## 321.54 `CONFIG_BT_COMPANY_ID`

**提示（Prompt）**：公司标识符（Company Id）

**说明（Help）**

设置此设备的蓝牙公司标识符（Bluetooth Company Identifier）。此选项默认使用 Linux 基金会（The Linux Foundation）的公司标识符 `0x05F1`，芯片厂商和硬件制造商也可设置自己的值。注意：控制器的公司标识符由 `BT_CTLR_COMPANY_ID` 控制。完整列表见 [Bluetooth Company Identifiers](https://www.bluetooth.com/specifications/assigned-numbers/company-identifiers)。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT
```

**默认值（Defaults）**

```text
0x05F1
```

**取值范围（Ranges）**

```text
[0x0000, 0xFFFF]
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:439`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L439)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_CONN"></a>

## 321.55 `CONFIG_BT_CONN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示已启用低功耗蓝牙连接（Bluetooth LE connections，ACL）支持。此内部选项由需要连接的角色自动选择，例如 `BT_PERIPHERAL` 和 `BT_CENTRAL`，不供直接设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_PERIPHERAL
CONFIG_BT_CENTRAL
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)。

<a id="CONFIG_BT_CONN_CHECK_NULL_BEFORE_CREATE"></a>

## 321.56 `CONFIG_BT_CONN_CHECK_NULL_BEFORE_CREATE`

**提示（Prompt）**：创建连接时检查 `*conn` 是否为 `NULL`（connection pointer check）

**说明（Help）**

启用此选项可确保：若 `*conn` 未初始化为 `NULL`，`bt_conn_le_create` 和 `bt_conn_le_create_synced` 将返回错误。建议启用它，以捕获应用在未释放引用的情况下复用活动连接对象（active connection object）指针的编程错误。如果不释放引用，连接对象会一直存活，可能造成不可预测的行为。

译注：原文使用 `dereferencing`，此处结合连接对象生命周期指释放其持有的引用，而不是普通的指针取值操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:329`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L329)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CONN_DISABLE_SECURITY"></a>

## 321.57 `CONFIG_BT_CONN_DISABLE_SECURITY`

**提示（Prompt）**：禁用安全检查（Disable security）

**说明（Help）**

此选项禁用入站请求的安全检查（security checks），以便测试访问通常需要加密／身份认证（encryption/authentication）才能访问的 GATT 属性（attributes）和 L2CAP 信道（channels）。警告：此选项允许任何人窃听空中传输流量（on-air traffic）。强烈不建议在生产环境使用此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TESTING && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1147)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙测试（Bluetooth Testing）

**配置项引用（Symbol References）**：[`CONFIG_BT_TESTING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TESTING)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_CONN_DYNAMIC_CALLBACKS"></a>

## 321.58 `CONFIG_BT_CONN_DYNAMIC_CALLBACKS`

**提示（Prompt）**：动态连接回调（Dynamic connection callbacks）

**说明（Help）**

启用动态连接回调（dynamic connection callbacks）支持，将 `bt_conn_cb_register()` 链接进来。禁用此配置是安全的，但使用该 API 及相关 API 的代码将无法链接。注意：通过 `BT_CONN_CB_DEFINE()` 进行的静态注册（static registration）始终可用，不依赖此配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_CONN_FRAG_COUNT"></a>

## 321.59 `CONFIG_BT_CONN_FRAG_COUNT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设置同时处于传输中（in flight）的数据包最大数量的内部 Kconfig 选项。它应等于连接数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MAX_CONN if CONFIG_BT_CONN
CONFIG_BT_ISO_MAX_CHAN if CONFIG_BT_ISO
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L307)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MAX_CONN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_CONN)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_ISO_MAX_CHAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_CHAN)、[`CONFIG_BT_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_ISO`。

<a id="CONFIG_BT_CONN_PARAM_ANY"></a>

## 321.60 `CONFIG_BT_CONN_PARAM_ANY`

**提示（Prompt）**：接受任意连接参数值（Accept any values for connection parameters）

**说明（Help）**

某些控制器支持规范规定范围之外的连接参数（connection parameters）。启用此选项后，应用可以为所有连接参数设置任意值。主机（Host）不会对任何连接参数执行边界或一致性检查，包括最小／最大连接间隔（conn interval min and max）、延迟（latency）和超时（timeout）。但主机仍会使用最小与最大连接间隔的数值比较，验证连接是否已采用期望的参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:317`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L317)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CONN_PARAM_RETRY_COUNT"></a>

## 321.61 `CONFIG_BT_CONN_PARAM_RETRY_COUNT`

**提示（Prompt）**：外设连接参数更新重试次数（Peripheral connection parameter update retry attempts）

**说明（Help）**

此值表示连接参数更新（connection parameter update）的重试次数，用于达到外设（Peripheral）的 GATT 特征（characteristics）中设定的首选值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:849`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L849)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CONN_PARAM_RETRY_TIMEOUT"></a>

## 321.62 `CONFIG_BT_CONN_PARAM_RETRY_TIMEOUT`

**提示（Prompt）**：外设连接参数更新重试超时，单位为毫秒（Peripheral connection parameter update retry timeout）

**说明（Help）**

此值是外设（peripheral device）在再次尝试请求首选连接参数（preferred connection parameters）之前等待的超时时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
5000
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:858`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L858)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CONN_PARAM_UPDATE_TIMEOUT"></a>

## 321.63 `CONFIG_BT_CONN_PARAM_UPDATE_TIMEOUT`

**提示（Prompt）**：外设连接参数更新超时，单位为毫秒（Peripheral connection parameter update timeout）

**说明（Help）**

此值是外设（peripheral device）在连接建立后、开始首次连接参数更新过程（connection parameters update procedure）之前等待的超时时间。所请求的连接参数采用应用设置的参数；如果配置了外设首选连接参数（peripheral preferred connection parameters），则采用这些参数。默认值为 `5` 秒，以符合蓝牙核心规范（Bluetooth Core specification）：Core 4.2 Vol 3, Part C, 9.3.12.2 规定，外设不应在连接建立后的 5 秒内执行连接参数更新过程。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
5000
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:833`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L833)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CONN_TX"></a>

## 321.64 `CONFIG_BT_CONN_TX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ACL 或广播 ISO（broadcast ISO）时为真的隐藏配置

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CONN || CONFIG_BT_ISO_TX
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_ISO_TX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_TX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_ISO_TX`。

<a id="CONFIG_BT_CONN_TX_NOTIFY_WQ"></a>

## 321.65 `CONFIG_BT_CONN_TX_NOTIFY_WQ`

**提示（Prompt）**：使用独立工作队列处理连接 TX 通知（connection TX notify processing）[实验性，EXPERIMENTAL]

**说明（Help）**

使用独立工作队列（separate workqueue）代替系统工作队列来执行 `bt_conn_tx_notify` 处理。此选项可使蓝牙协议栈减少对系统工作队列（system workqueue）的依赖。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN_TX && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN_TX`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN_TX)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_BT_CONN_TX_NOTIFY_WQ_INIT_PRIORITY"></a>

## 321.66 `CONFIG_BT_CONN_TX_NOTIFY_WQ_INIT_PRIORITY`

**提示（Prompt）**：连接 TX 通知处理工作队列的初始化优先级（Init priority）

**说明（Help）**

连接发送通知处理工作队列（connection TX notify processing workqueue）在系统初始化的 `POST_KERNEL` 级别初始化。此 Kconfig 选项控制该级别内的初始化优先级（initialization priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN_TX_NOTIFY_WQ && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 使用独立工作队列处理连接 TX 通知（connection TX notify processing）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN_TX_NOTIFY_WQ`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN_TX_NOTIFY_WQ)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_CONN_TX_NOTIFY_WQ_PRIO"></a>

## 321.67 `CONFIG_BT_CONN_TX_NOTIFY_WQ_PRIO`

**提示（Prompt）**：连接 TX 通知处理工作队列的协作式优先级（Cooperative priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN_TX_NOTIFY_WQ && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 使用独立工作队列处理连接 TX 通知（connection TX notify processing）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN_TX_NOTIFY_WQ`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN_TX_NOTIFY_WQ)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_CONN_TX_NOTIFY_WQ_STACK_SIZE"></a>

## 321.68 `CONFIG_BT_CONN_TX_NOTIFY_WQ_STACK_SIZE`

**提示（Prompt）**：连接 TX 通知处理工作队列的栈大小（Stack size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN_TX_NOTIFY_WQ && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 使用独立工作队列处理连接 TX 通知（connection TX notify processing）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN_TX_NOTIFY_WQ`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN_TX_NOTIFY_WQ)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE`](P002_kernel_配置项参考_2.md#CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE)。

<a id="CONFIG_BT_CONN_TX_USER_DATA_SIZE"></a>

## 321.69 `CONFIG_BT_CONN_TX_USER_DATA_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

协议栈使用所必需的 `user_data` 大小，主要用于传递回调（callbacks）。参见 `conn_internal.h` 中的 `struct closure`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
32 if CONFIG_64BIT
16
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:299`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L299)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CREATE_CONN_TIMEOUT"></a>

## 321.70 `CONFIG_BT_CREATE_CONN_TIMEOUT`

**提示（Prompt）**：待完成 LE Create Connection 命令的超时，单位为秒（pending LE Create Connection timeout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 655]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:828`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L828)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CRYPTO"></a>

## 321.71 `CONFIG_BT_CRYPTO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项启用蓝牙密码工具箱（Bluetooth Cryptographic Toolbox）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_ALG_CMAC
CONFIG_PSA_WANT_ALG_ECB_NO_PADDING
```

**被选择（Selected by）**

```text
CONFIG_BT_SMP
CONFIG_BT_CTLR_BROADCAST_ISO_ENC
```

**弱选择（Implies）**

```text
CONFIG_MBEDTLS_AES_ROM_TABLES if CONFIG_MBEDTLS_PSA_CRYPTO_C
```

**定义位置（Location）**：[`subsys/bluetooth/crypto/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/crypto/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_ALG_CMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CMAC)、[`CONFIG_PSA_WANT_ALG_ECB_NO_PADDING`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECB_NO_PADDING)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CTLR_BROADCAST_ISO_ENC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_BROADCAST_ISO_ENC)、[`CONFIG_MBEDTLS_AES_ROM_TABLES`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_AES_ROM_TABLES)、[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_BROADCAST_ISO_ENC`。

<a id="CONFIG_BT_CSIP_SET_COORDINATOR"></a>

## 321.72 `CONFIG_BT_CSIP_SET_COORDINATOR`

**提示（Prompt）**：协调集合识别配置文件集合协调器支持（Coordinated Set Identification Profile Set Coordinator Support）

**说明（Help）**

此选项启用协调集合识别配置文件（Coordinated Set Identification Profile）的集合协调器（Set Coordinator）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CLIENT && CONFIG_BT_GATT_AUTO_DISCOVER_CCC && CONFIG_BT_SMP && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.csip:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.csip#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_GATT_AUTO_DISCOVER_CCC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_AUTO_DISCOVER_CCC)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CSIP_SET_COORDINATOR_ENC_SIRK_SUPPORT"></a>

## 321.73 `CONFIG_BT_CSIP_SET_COORDINATOR_ENC_SIRK_SUPPORT`

**提示（Prompt）**：加密 SIRK 支持（Support for encrypted SIRK）

**说明（Help）**

启用集合身份解析密钥（SIRK）的加密支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CSIP_SET_COORDINATOR && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.csip:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.csip#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 协调集合识别配置文件集合协调器支持（Coordinated Set Identification Profile Set Coordinator Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_COORDINATOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_COORDINATOR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES"></a>

## 321.74 `CONFIG_BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES`

**提示（Prompt）**：协调集合识别服务数量（Coordinated Set Identification Service Count）

**说明（Help）**

设置服务实例（service instances）的数量，对应对端设备可能归属的不同集合（sets）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CSIP_SET_COORDINATOR && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 3]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.csip:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.csip#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 协调集合识别配置文件集合协调器支持（Coordinated Set Identification Profile Set Coordinator Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_COORDINATOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_COORDINATOR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CSIP_SET_COORDINATOR_TEST_SAMPLE_DATA"></a>

## 321.75 `CONFIG_BT_CSIP_SET_COORDINATOR_TEST_SAMPLE_DATA`

**提示（Prompt）**：协调集合识别服务测试样例数据（Coordinated Set Identification Service Test Sample Data）

**说明（Help）**

启用 CSIS 规范定义的样例数据（sample data），使用样例 `SIRK`、`prand` 和 `LTK`。警告：此选项允许客户端使用样例数据定位成员并解密 SIRK，因此无法用于未采用这些样例数据的集合成员（set members）。不应在生产构建（production builds）中使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CSIP_SET_COORDINATOR && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.csip:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.csip#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 协调集合识别配置文件集合协调器支持（Coordinated Set Identification Profile Set Coordinator Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_COORDINATOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_COORDINATOR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CSIP_SET_MEMBER"></a>

## 321.76 `CONFIG_BT_CSIP_SET_MEMBER`

**提示（Prompt）**：协调集合识别配置文件集合成员支持（Coordinated Set Identification Profile Set Member support）

**说明（Help）**

此选项启用协调集合识别配置文件（Coordinated Set Identification Profile）的集合成员角色（Set Member role）以及协调集合识别服务（Coordinated Set Identification Service）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_DYNAMIC_DB && CONFIG_BT_SMP && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**弱选择（Implies）**

```text
CONFIG_BT_EXT_ADV if CONFIG_BT_PRIVACY
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.csip:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.csip#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_DYNAMIC_DB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_PRIVACY`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PRIVACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CSIP_SET_MEMBER_ENC_SIRK_SUPPORT"></a>

## 321.77 `CONFIG_BT_CSIP_SET_MEMBER_ENC_SIRK_SUPPORT`

**提示（Prompt）**：加密 SIRK 支持（Support for encrypted SIRK）

**说明（Help）**

启用集合身份解析密钥（SIRK）的加密支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CSIP_SET_MEMBER && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.csip:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.csip#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 协调集合识别配置文件集合成员支持（Coordinated Set Identification Profile Set Member support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT"></a>

## 321.78 `CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT`

**提示（Prompt）**：集合成员锁支持（Support for Set Member Lock）

**说明（Help）**

此选项启用集合成员锁（Set Member Locks）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CSIP_SET_MEMBER && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.csip:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.csip#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 协调集合识别配置文件集合成员支持（Coordinated Set Identification Profile Set Member support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CSIP_SET_MEMBER_MAX_INSTANCE_COUNT"></a>

## 321.79 `CONFIG_BT_CSIP_SET_MEMBER_MAX_INSTANCE_COUNT`

**提示（Prompt）**：协调集合识别配置文件最大服务实例数（Coordinated Set Identification Profile max service instance count）

**说明（Help）**

此选项设置协调集合识别服务（Coordinated Set Identification Services）的最大实例数。如果将该服务声明为主服务（primary service），则只能有一个实例。启用 `BT_CAP_ACCEPTOR_SET_MEMBER` 会占用一个已分配实例。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CSIP_SET_MEMBER && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.csip:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.csip#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 协调集合识别配置文件集合成员支持（Coordinated Set Identification Profile Set Member support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT"></a>

## 321.80 `CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT`

**提示（Prompt）**：集合成员顺序等级支持（Support for Set Member Rank）

**说明（Help）**

此选项启用集合成员顺序等级（Set Member Ranks）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CSIP_SET_MEMBER && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.csip:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.csip#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 协调集合识别配置文件集合成员支持（Coordinated Set Identification Profile Set Member support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CSIP_SET_MEMBER_SIRK_NOTIFIABLE"></a>

## 321.81 `CONFIG_BT_CSIP_SET_MEMBER_SIRK_NOTIFIABLE`

**提示（Prompt）**：SIRK 变更通知支持（SIRK notifiable Support）

**说明（Help）**

此选项允许在集合身份解析密钥（SIRK）变更时通知客户端（clients）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CSIP_SET_MEMBER && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.csip:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.csip#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 协调集合识别配置文件集合成员支持（Coordinated Set Identification Profile Set Member support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CSIP_SET_MEMBER_SIZE_NOTIFIABLE"></a>

## 321.82 `CONFIG_BT_CSIP_SET_MEMBER_SIZE_NOTIFIABLE`

**提示（Prompt）**：集合大小变更通知支持（Set Size notifiable support）

**说明（Help）**

此选项允许在集合大小（Set Size）变更时通知客户端（clients）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT && CONFIG_BT_CSIP_SET_MEMBER && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.csip:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.csip#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 协调集合识别配置文件集合成员支持（Coordinated Set Identification Profile Set Member support） → 协调集合大小支持（Support for Coordinated Set Size）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT)、[`CONFIG_BT_CSIP_SET_MEMBER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT"></a>

## 321.83 `CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT`

**提示（Prompt）**：协调集合大小支持（Support for Coordinated Set Size）

**说明（Help）**

启用协调集合大小（Coordinated Set Sizes）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CSIP_SET_MEMBER && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.csip:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.csip#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 协调集合识别配置文件集合成员支持（Coordinated Set Identification Profile Set Member support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CSIP_SET_MEMBER_TEST_SAMPLE_DATA"></a>

## 321.84 `CONFIG_BT_CSIP_SET_MEMBER_TEST_SAMPLE_DATA`

**提示（Prompt）**：协调集合识别服务测试样例数据（Coordinated Set Identification Service Test Sample Data）

**说明（Help）**

启用 CSIS 规范为 SIRK 定义的样例数据（sample data），使用样例 `SIRK`、`prand` 和 `LTK`。警告：此选项允许任何人使用公开的样例数据跟踪 SIRK，并在 SIRK 加密时将其解密。不应在生产构建（production builds）中使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CSIP_SET_MEMBER && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.csip:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.csip#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 协调集合识别配置文件集合成员支持（Coordinated Set Identification Profile Set Member support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CTLR_ADVANCED_FEATURES"></a>

## 321.85 `CONFIG_BT_CTLR_ADVANCED_FEATURES`

**提示（Prompt）**：显示高级功能（Show advanced features）

**说明（Help）**

使控制器开发者（controller developers）能够看到高级功能（advanced features）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:352`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L352)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_ADI_IN_SCAN_RSP"></a>

## 321.86 `CONFIG_BT_CTLR_ADV_ADI_IN_SCAN_RSP`

**提示（Prompt）**：在 AUX_SCAN_RSP PDU 中包含 ADI（Include ADI）

**说明（Help）**

启用 `AUX_SCAN_RSP` 协议数据单元（PDU）中的 ADI 字段（field）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:536`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L536)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_AUX_PDU_BACK2BACK"></a>

## 321.87 `CONFIG_BT_CTLR_ADV_AUX_PDU_BACK2BACK`

**提示（Prompt）**：扩展广播序列的背靠背发送（Back-to-back transmission of extended advertising trains）

**说明（Help）**

允许在扩展广播序列（extended advertising train）中发送 `AUX_CHAIN_IND`，各 `AUX_CHAIN_IND` 依次背靠背（back-to-back）发送。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_ADV_DATA_CHAIN
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_ADV_AUX_PDU_LINK
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:428`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L428)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ADV_DATA_CHAIN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_DATA_CHAIN)、[`CONFIG_BT_CTLR_ADV_AUX_PDU_LINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_AUX_PDU_LINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_ADV_AUX_PDU_LINK`。

<a id="CONFIG_BT_CTLR_ADV_AUX_PDU_BACK2BACK_AFS"></a>

## 321.88 `CONFIG_BT_CTLR_ADV_AUX_PDU_BACK2BACK_AFS`

**提示（Prompt）**：扩展广播序列背靠背发送的辅助帧间隔（AUX Frame Space）

**说明（Help）**

指定扩展广播序列（extended advertising trains）背靠背发送所用的辅助帧间隔（AUX Frame Space），时间单位为微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_AUX_PDU_BACK2BACK && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
300
```

**取值范围（Ranges）**

```text
[300, 1000]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:436`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L436)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 扩展广播序列的背靠背发送（Back-to-back transmission of extended advertising trains）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_AUX_PDU_BACK2BACK`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_AUX_PDU_BACK2BACK)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_AUX_SET"></a>

## 321.89 `CONFIG_BT_CTLR_ADV_AUX_SET`

**提示（Prompt）**：低功耗蓝牙扩展广播辅助集合（LE Extended Advertising Auxiliary Sets）

**说明（Help）**

支持的广播辅助信道集合（advertising auxiliary channel sets）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CTLR_ADV_SET
```

**取值范围（Ranges）**

```text
[0, CONFIG_BT_CTLR_ADV_SET]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:258`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L258)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ADV_SET`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_SET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_AUX_SLOT_WINDOW_DRIFT"></a>

## 321.90 `CONFIG_BT_CTLR_ADV_AUX_SLOT_WINDOW_DRIFT`

**提示（Prompt）**：在时隙窗口内移动扩展广播辅助 PDU（Drift Extended Advertising Auxiliary PDUs）

**说明（Help）**

在时隙窗口（slot window）内移动扩展广播辅助协议数据单元（Extended Advertising Auxiliary PDUs），避免与其他周期性调度的状态／角色（states/roles）重叠；将这些 PDU 安排在原本会重叠的状态／角色之前或之后。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TICKER_EXT && CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_SYNC_ISO || CONFIG_BT_CTLR_CONN_ISO
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:481`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L481)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_TICKER_EXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_EXT)、[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_SYNC_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_CONN_ISO`。

<a id="CONFIG_BT_CTLR_ADV_AUX_SYNC_OFFSET"></a>

## 321.91 `CONFIG_BT_CTLR_ADV_AUX_SYNC_OFFSET`

**提示（Prompt）**：AUX_ADV_IND 与 AUX_SYNC_IND 之间的预定义偏移（Pre-defined offset）

**说明（Help）**

当扩展广播（Extended Advertising）与周期性广播（Periodic Advertising）所用广播间隔相同或互为倍数时，定义 `AUX_ADV_IND` 和 `AUX_SYNC_IND` 之间的偏移（offset）。注意，为获得相同或成倍数的广播间隔，周期性广播间隔应比扩展广播间隔多 `10` 毫秒；这是因为 `AUX_ADV_IND` PDU 按周期性事件调度，其周期等于扩展广播间隔加 `10` 毫秒的广播随机延迟（Advertising Random Delay）。偏移单位为微秒，实验性的最大允许值为 `4` 秒。

译注：上述间隔关系按原文保留；其比较基准包括调度时加入的广播随机延迟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_PERIODIC && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4000000]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:504`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L504)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_PERIODIC`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_PERIODIC)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_DATA_BUF_MAX"></a>

## 321.92 `CONFIG_BT_CTLR_ADV_DATA_BUF_MAX`

**提示（Prompt）**：广播数据最大缓冲数量（Advertising Data Maximum Buffers）

**说明（Help）**

所有已启用广播集合（advertising sets）之间，能够缓存的广播数据有效载荷（Advertising Data payload）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2 if CONFIG_BT_CTLR_ADV_PERIODIC
1
```

**取值范围（Ranges）**

```text
[1, 64] if CONFIG_BT_CTLR_ADV_EXT
[1, 1] if !CONFIG_BT_CTLR_ADV_EXT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:276`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L276)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ADV_PERIODIC`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_PERIODIC)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_DATA_CHAIN"></a>

## 321.93 `CONFIG_BT_CTLR_ADV_DATA_CHAIN`

**提示（Prompt）**：广播数据链式连接（Advertising Data chaining）[实验性，EXPERIMENTAL]

**说明（Help）**

启用扩展广播（Extended Advertising，非可连接）和周期性广播（Periodic Advertising）的广播数据链式连接（Advertising Data chaining）支持，使广播数据长度最多可达 `1650` 字节。

该功能仍处于实验和开发阶段，尚未实现广播数据（AD Data）的重新组合。如果某个链 PDU 的 AD 数据需要溢出到新的链 PDU，可能返回 `BT_HCI_ERR_PACKET_TOO_LONG`。具体而言，末尾 PDU 因需要加入辅助指针字段（Aux Pointer field）而可能出现 AD 数据溢出；若这些溢出字节与下一个 AD 数据分片的总长度超过 `255` 字节，就需要额外的链 PDU。该处理尚未实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:400`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L400)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_DATA_LEN_MAX"></a>

## 321.94 `CONFIG_BT_CTLR_ADV_DATA_LEN_MAX`

**提示（Prompt）**：最大广播数据长度（Maximum Advertising Data Length）

**说明（Help）**

最大扩展广播数据长度（Maximum Extended Advertising Data Length）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**取值范围（Ranges）**

```text
[31, 191] if CONFIG_BT_LL_SW_SPLIT && !CONFIG_BT_CTLR_ADV_DATA_CHAIN
[31, 1650]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:769`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L769)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_ADV_DATA_CHAIN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_DATA_CHAIN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_ENABLE_STRICT"></a>

## 321.95 `CONFIG_BT_CTLR_ADV_ENABLE_STRICT`

**提示（Prompt）**：严格执行广播启用／禁用规则（Enforce Strict Advertising Enable/Disable）

**说明（Help）**

在启用已启用的广播或禁用已禁用的广播时，强制返回 HCI 命令不允许错误（Command Disallowed）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:609`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L609)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_EXT"></a>

## 321.96 `CONFIG_BT_CTLR_ADV_EXT`

**提示（Prompt）**：低功耗蓝牙广播扩展（LE Advertising Extensions）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.0 低功耗蓝牙广播扩展（LE Advertising Extensions）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_EXT_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_EXT_ADV
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_CHAN_SEL_2 if CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_BROADCASTER
CONFIG_BT_CTLR_SCAN_REQ_NOTIFY if CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_BROADCASTER
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:737`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L737)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_EXT_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_EXT_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_CTLR_CHAN_SEL_2`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CHAN_SEL_2)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CTLR_SCAN_REQ_NOTIFY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SCAN_REQ_NOTIFY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_ADV_EXT_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_EXT_CODING_SELECTION"></a>

## 321.97 `CONFIG_BT_CTLR_ADV_EXT_CODING_SELECTION`

**提示（Prompt）**：广播编码选择支持（Advertising Coding Selection support）

**说明（Help）**

在控制器（Controller）中启用蓝牙 6.0 广播编码选择（Advertising Coding Selection）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_PHY_CODED && CONFIG_BT_CTLR_ADV_EXT_CODING_SELECTION_SUPPORT && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_EXT_ADV_CODING_SELECTION
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_SET_HOST_FEATURE if CONFIG_BT_OBSERVER
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:795`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L795)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_PHY_CODED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_CODED)、[`CONFIG_BT_CTLR_ADV_EXT_CODING_SELECTION_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_EXT_CODING_SELECTION_SUPPORT)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_EXT_ADV_CODING_SELECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_EXT_ADV_CODING_SELECTION)、[`CONFIG_BT_CTLR_SET_HOST_FEATURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SET_HOST_FEATURE)、[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_ADV_EXT_CODING_SELECTION_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_EXT_PDU_EXTRA_DATA_MEMORY"></a>

## 321.98 `CONFIG_BT_CTLR_ADV_EXT_PDU_EXTRA_DATA_MEMORY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为广播 PDU 存储增加额外内存。该内存作为通用存储区（general purpose storage），保存应从上层链路层（ULL）发送给下层链路层（LLL）的数据。其内容与 PDU 内存内容保持同步。例如，额外数据内存用于保存配置无线电外设（Radio peripheral）发送恒定音调扩展（CTE）的参数。这些配置数据必须与扩展广播头（extended advertising header）中的 `CTEInfo` 字段同步，该广播头属于 PDU 数据的一部分。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_DF_ADV_CTE_TX
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:522`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L522)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_DF_ADV_CTE_TX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_ADV_CTE_TX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_EXT_RX_PDU_LEN_MAX"></a>

## 321.99 `CONFIG_BT_CTLR_ADV_EXT_RX_PDU_LEN_MAX`

**提示（Prompt）**：广播扩展接收 PDU 最大长度（Maximum Advertising Extensions Receive PDU Length）

**说明（Help）**

广播扩展（Advertising Extensions）接收协议数据单元（PDU）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_CTLR_ADV_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[255, 255] if CONFIG_BT_HCI_RAW
[31, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:236`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L236)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_INDICATION"></a>

## 321.100 `CONFIG_BT_CTLR_ADV_INDICATION`

**提示（Prompt）**：广播指示（Advertisement indications）

**说明（Help）**

生成用于指示空中广播活动（on air advertisement events）的事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1207)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<!-- kconfig-navigation -->

[上一章](P320_subsys_bluetooth_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P322_subsys_bluetooth_配置项参考_3.md)
