---
id: learning.zephyr-docs.kconfig-reference.page-13
title: "`<module:hal_realtek>/ameba`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第13章\_`<module:hal_realtek>/ameba`配置项参考

本章翻译官方 Kconfig 数据库中 `<module:hal_realtek>/ameba` 的 33 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT"></a>

## 13.1 `CONFIG_BT`

原库同名定义共 2 条；本项为数据库第 1287 条记录，各定义分别保留。

**提示（Prompt）**：启用蓝牙（Bluetooth，BT）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_REALTEK_AMEBA_ZEPHYR_BT && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
y
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

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/bluetooth/Kconfig:14`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Ameba Zephyr 蓝牙（BT）

**配置项引用（Symbol References）**：[`CONFIG_REALTEK_AMEBA_ZEPHYR_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_BT)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_USB_DEVICE_BLUETOOTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_BLUETOOTH)、[`CONFIG_USBD_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_BT_HCI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_BT_CENTRAL"></a>

## 13.2 `CONFIG_BT_CENTRAL`

原库同名定义共 2 条；本项为数据库第 1685 条记录，各定义分别保留。

**提示（Prompt）**：启用蓝牙中心设备（BT Central）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_REALTEK_AMEBA_ZEPHYR_BT && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_BT_CLASSIC
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/bluetooth/Kconfig:30`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Ameba Zephyr 蓝牙（BT）

**配置项引用（Symbol References）**：[`CONFIG_REALTEK_AMEBA_ZEPHYR_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_BT)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_BT_CLASSIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CLASSIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_BT_COEXIST"></a>

## 13.3 `CONFIG_BT_COEXIST`

原库同名定义共 2 条；本项为数据库第 1693 条记录，各定义分别保留。

**提示（Prompt）**：启用共存（Coexistence）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_SERIES_AMEBAD
```

**主动选择（Selects）**

```text
CONFIG_COEXIST_HOST if !CONFIG_SINGLE_CORE_WIFI
CONFIG_ZEPHYR_SDK
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:6`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`）

**配置项引用（Symbol References）**：[`CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_COEXIST_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COEXIST_HOST)、[`CONFIG_SINGLE_CORE_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SINGLE_CORE_WIFI)、[`CONFIG_ZEPHYR_SDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_SDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_COEXIST_HOST`、`CONFIG_SINGLE_CORE_WIFI`、`CONFIG_ZEPHYR_SDK`。

<a id="CONFIG_BT_EXT_ADV"></a>

## 13.4 `CONFIG_BT_EXT_ADV`

原库同名定义共 2 条；本项为数据库第 2207 条记录，各定义分别保留。

**提示（Prompt）**：启用蓝牙扩展广播（BT Extended Advertising）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_REALTEK_AMEBA_ZEPHYR_BT && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
n
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

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/bluetooth/Kconfig:44`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Ameba Zephyr 蓝牙（BT）

**配置项引用（Symbol References）**：[`CONFIG_REALTEK_AMEBA_ZEPHYR_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_BT)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_BT_ISO_BROADCAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_BROADCAST)、[`CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL)、[`CONFIG_BT_CSIP_SET_MEMBER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_BT_ISO_BROADCAST`。

<a id="CONFIG_BT_EXT_ADV_MAX_ADV_SET"></a>

## 13.5 `CONFIG_BT_EXT_ADV_MAX_ADV_SET`

原库同名定义共 2 条；本项为数据库第 2211 条记录，各定义分别保留。

**提示（Prompt）**：最大广播集数量（Max Advertising Sets）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_EXT_ADV && CONFIG_REALTEK_AMEBA_ZEPHYR_BT && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/bluetooth/Kconfig:49`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Ameba Zephyr 蓝牙（BT） → 启用蓝牙扩展广播（BT Extended Advertising）

**配置项引用（Symbol References）**：[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_REALTEK_AMEBA_ZEPHYR_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_BT)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_BT_PERIPHERAL"></a>

## 13.6 `CONFIG_BT_PERIPHERAL`

原库同名定义共 2 条；本项为数据库第 3117 条记录，各定义分别保留。

**提示（Prompt）**：启用蓝牙外设（BT Peripheral）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_REALTEK_AMEBA_ZEPHYR_BT && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_BT_CLASSIC
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/bluetooth/Kconfig:26`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Ameba Zephyr 蓝牙（BT）

**配置项引用（Symbol References）**：[`CONFIG_REALTEK_AMEBA_ZEPHYR_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_BT)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_BT_CLASSIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CLASSIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_BT_PRIVACY"></a>

## 13.7 `CONFIG_BT_PRIVACY`

原库同名定义共 2 条；本项为数据库第 3134 条记录，各定义分别保留。

**提示（Prompt）**：启用蓝牙隐私（BT Privacy）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_REALTEK_AMEBA_ZEPHYR_BT && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/bluetooth/Kconfig:40`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Ameba Zephyr 蓝牙（BT）

**配置项引用（Symbol References）**：[`CONFIG_REALTEK_AMEBA_ZEPHYR_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_BT)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_COEXIST_EXT"></a>

## 13.8 `CONFIG_COEXIST_EXT`

**提示（Prompt）**：启用外部共存（External Coexistence）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_COEXIST && !CONFIG_SOC_SERIES_AMEBAD && CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_COEX_EXT_CHIP_SUPPORT
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:23`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`）

**配置项引用（Symbol References）**：[`CONFIG_BT_COEXIST`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_COEXIST)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_COEX_EXT_CHIP_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COEX_EXT_CHIP_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_COEX_EXT_CHIP_SUPPORT`。

<a id="CONFIG_COEX_EXT_GNT_POLAR"></a>

## 13.9 `CONFIG_COEX_EXT_GNT_POLAR`

**提示（Prompt）**：授权信号极性（Grant Polarity）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COEXIST_EXT && CONFIG_BT_COEXIST && !CONFIG_SOC_SERIES_AMEBAD && CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
CONFIG_EXT_GNT_POLAR_LOW
```

**可选项（Choices）**

```text
CONFIG_EXT_GNT_POLAR_LOW
CONFIG_EXT_GNT_POLAR_HIGH
CONFIG_EXT_GNT_POLAR_LOW
CONFIG_EXT_GNT_POLAR_HIGH
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:72`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持

**配置项引用（Symbol References）**：[`CONFIG_COEXIST_EXT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEXIST_EXT)、[`CONFIG_BT_COEXIST`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_COEXIST)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_EXT_GNT_POLAR_LOW`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_GNT_POLAR_LOW)、[`CONFIG_EXT_GNT_POLAR_HIGH`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_GNT_POLAR_HIGH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_COEX_EXT_PRIORITY_MODE"></a>

## 13.10 `CONFIG_COEX_EXT_PRIORITY_MODE`

**提示（Prompt）**：优先级模式（Priority Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COEXIST_EXT && CONFIG_BT_COEXIST && !CONFIG_SOC_SERIES_AMEBAD && CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
CONFIG_EXT_PRIORITY_DIRECTIONAL
```

**可选项（Choices）**

```text
CONFIG_EXT_PRIORITY_DIRECTIONAL
CONFIG_EXT_PRIORITY_STATIC
CONFIG_EXT_PRIORITY_DIRECTIONAL
CONFIG_EXT_PRIORITY_STATIC
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:50`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持

**配置项引用（Symbol References）**：[`CONFIG_COEXIST_EXT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEXIST_EXT)、[`CONFIG_BT_COEXIST`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_COEXIST)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_EXT_PRIORITY_DIRECTIONAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_PRIORITY_DIRECTIONAL)、[`CONFIG_EXT_PRIORITY_STATIC`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_PRIORITY_STATIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_COEX_EXT_PROTOCOL"></a>

## 13.11 `CONFIG_COEX_EXT_PROTOCOL`

**提示（Prompt）**：外部协议（External Protocol）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COEXIST_EXT && CONFIG_BT_COEXIST && !CONFIG_SOC_SERIES_AMEBAD && CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
CONFIG_EXT_PROTOCOL_WPAN
```

**可选项（Choices）**

```text
CONFIG_EXT_PROTOCOL_WPAN
CONFIG_EXT_PROTOCOL_BT
CONFIG_EXT_PROTOCOL_BT_WPAN
CONFIG_EXT_PROTOCOL_WPAN
CONFIG_EXT_PROTOCOL_BT
CONFIG_EXT_PROTOCOL_BT_WPAN
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:38`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持

**配置项引用（Symbol References）**：[`CONFIG_COEXIST_EXT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEXIST_EXT)、[`CONFIG_BT_COEXIST`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_COEXIST)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_EXT_PROTOCOL_WPAN`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_PROTOCOL_WPAN)、[`CONFIG_EXT_PROTOCOL_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_PROTOCOL_BT)、[`CONFIG_EXT_PROTOCOL_BT_WPAN`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_PROTOCOL_BT_WPAN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_COEX_EXT_PTA_MODE"></a>

## 13.12 `CONFIG_COEX_EXT_PTA_MODE`

**提示（Prompt）**：分组业务仲裁模式（PTA Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COEXIST_EXT && CONFIG_BT_COEXIST && !CONFIG_SOC_SERIES_AMEBAD && CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
CONFIG_EXT_PTA_MODE_SIMPLE
```

**可选项（Choices）**

```text
CONFIG_EXT_PTA_MODE_SIMPLE
CONFIG_EXT_PTA_MODE_MULTIPLE
CONFIG_EXT_PTA_MODE_SIMPLE
CONFIG_EXT_PTA_MODE_MULTIPLE
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:28`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持

**配置项引用（Symbol References）**：[`CONFIG_COEXIST_EXT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEXIST_EXT)、[`CONFIG_BT_COEXIST`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_COEXIST)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_EXT_PTA_MODE_SIMPLE`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_PTA_MODE_SIMPLE)、[`CONFIG_EXT_PTA_MODE_MULTIPLE`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_PTA_MODE_MULTIPLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_COEX_EXT_REQUEST_POLAR"></a>

## 13.13 `CONFIG_COEX_EXT_REQUEST_POLAR`

**提示（Prompt）**：请求信号极性（Request Polarity）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COEXIST_EXT && CONFIG_BT_COEXIST && !CONFIG_SOC_SERIES_AMEBAD && CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
CONFIG_EXT_REQUEST_POLAR_HIGH
```

**可选项（Choices）**

```text
CONFIG_EXT_REQUEST_POLAR_HIGH
CONFIG_EXT_REQUEST_POLAR_LOW
CONFIG_EXT_REQUEST_POLAR_HIGH
CONFIG_EXT_REQUEST_POLAR_LOW
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:61`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持

**配置项引用（Symbol References）**：[`CONFIG_COEXIST_EXT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEXIST_EXT)、[`CONFIG_BT_COEXIST`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_COEXIST)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_EXT_REQUEST_POLAR_HIGH`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_REQUEST_POLAR_HIGH)、[`CONFIG_EXT_REQUEST_POLAR_LOW`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_REQUEST_POLAR_LOW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_EXT_GNT_POLAR_HIGH"></a>

## 13.14 `CONFIG_EXT_GNT_POLAR_HIGH`

**提示（Prompt）**：授权信号高电平有效（Grant Active High）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EXT_PTA_MODE_SIMPLE && <choice CONFIG_COEX_EXT_GNT_POLAR>
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:78`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持 → 授权信号极性（Grant Polarity）

**配置项引用（Symbol References）**：[`CONFIG_EXT_PTA_MODE_SIMPLE`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_PTA_MODE_SIMPLE)、[`CONFIG_COEX_EXT_GNT_POLAR`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEX_EXT_GNT_POLAR)。

<a id="CONFIG_EXT_GNT_POLAR_LOW"></a>

## 13.15 `CONFIG_EXT_GNT_POLAR_LOW`

**提示（Prompt）**：授权信号低电平有效（Grant Active Low）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COEX_EXT_GNT_POLAR>
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:76`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持 → 授权信号极性（Grant Polarity）

**配置项引用（Symbol References）**：[`CONFIG_COEX_EXT_GNT_POLAR`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEX_EXT_GNT_POLAR)。

<a id="CONFIG_EXT_PRIORITY_DIRECTIONAL"></a>

## 13.16 `CONFIG_EXT_PRIORITY_DIRECTIONAL`

**提示（Prompt）**：有方向（Directional）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COEX_EXT_PRIORITY_MODE>
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:54`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持 → 优先级模式（Priority Mode）

**配置项引用（Symbol References）**：[`CONFIG_COEX_EXT_PRIORITY_MODE`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEX_EXT_PRIORITY_MODE)。

<a id="CONFIG_EXT_PRIORITY_STATIC"></a>

## 13.17 `CONFIG_EXT_PRIORITY_STATIC`

**提示（Prompt）**：静态（Static）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EXT_PTA_MODE_SIMPLE && <choice CONFIG_COEX_EXT_PRIORITY_MODE>
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:56`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持 → 优先级模式（Priority Mode）

**配置项引用（Symbol References）**：[`CONFIG_EXT_PTA_MODE_SIMPLE`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_PTA_MODE_SIMPLE)、[`CONFIG_COEX_EXT_PRIORITY_MODE`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEX_EXT_PRIORITY_MODE)。

<a id="CONFIG_EXT_PRI_DET_TIME"></a>

## 13.18 `CONFIG_EXT_PRI_DET_TIME`

**提示（Prompt）**：优先级检测时间（Priority Detection Time）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COEXIST_EXT && CONFIG_BT_COEXIST && !CONFIG_SOC_SERIES_AMEBAD && CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 254]
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:83`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持

**配置项引用（Symbol References）**：[`CONFIG_COEXIST_EXT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEXIST_EXT)、[`CONFIG_BT_COEXIST`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_COEXIST)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_EXT_PROTOCOL_BT"></a>

## 13.19 `CONFIG_EXT_PROTOCOL_BT`

**提示（Prompt）**：外部蓝牙（External BT）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COEX_EXT_PROTOCOL>
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:44`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持 → 外部协议（External Protocol）

**配置项引用（Symbol References）**：[`CONFIG_COEX_EXT_PROTOCOL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEX_EXT_PROTOCOL)。

<a id="CONFIG_EXT_PROTOCOL_BT_WPAN"></a>

## 13.20 `CONFIG_EXT_PROTOCOL_BT_WPAN`

**提示（Prompt）**：外部蓝牙与无线个人区域网（External BT & WPAN）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COEX_EXT_PROTOCOL>
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:46`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持 → 外部协议（External Protocol）

**配置项引用（Symbol References）**：[`CONFIG_COEX_EXT_PROTOCOL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEX_EXT_PROTOCOL)。

<a id="CONFIG_EXT_PROTOCOL_WPAN"></a>

## 13.21 `CONFIG_EXT_PROTOCOL_WPAN`

**提示（Prompt）**：外部无线个人区域网（External WPAN）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COEX_EXT_PROTOCOL>
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:42`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持 → 外部协议（External Protocol）

**配置项引用（Symbol References）**：[`CONFIG_COEX_EXT_PROTOCOL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEX_EXT_PROTOCOL)。

<a id="CONFIG_EXT_PTA_MODE_MULTIPLE"></a>

## 13.22 `CONFIG_EXT_PTA_MODE_MULTIPLE`

**提示（Prompt）**：PTA 多路模式（Multiple Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COEX_EXT_PTA_MODE>
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:34`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持 → 分组业务仲裁模式（PTA Mode）

**配置项引用（Symbol References）**：[`CONFIG_COEX_EXT_PTA_MODE`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEX_EXT_PTA_MODE)。

<a id="CONFIG_EXT_PTA_MODE_SIMPLE"></a>

## 13.23 `CONFIG_EXT_PTA_MODE_SIMPLE`

**提示（Prompt）**：PTA 简单模式（Simple Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COEX_EXT_PTA_MODE>
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:32`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持 → 分组业务仲裁模式（PTA Mode）

**配置项引用（Symbol References）**：[`CONFIG_COEX_EXT_PTA_MODE`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEX_EXT_PTA_MODE)。

<a id="CONFIG_EXT_PTA_PIN_GNT"></a>

## 13.24 `CONFIG_EXT_PTA_PIN_GNT`

**提示（Prompt）**：PTA 授权引脚（Grant Pin）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_COEXIST_EXT && CONFIG_BT_COEXIST && !CONFIG_SOC_SERIES_AMEBAD && CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
"PB_1" if CONFIG_SOC_SERIES_AMEBADPLUS
"PA_19" if CONFIG_SOC_SERIES_AMEBAG2
"PA_27" if CONFIG_SOC_SERIES_AMEBAD
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:112`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持

**配置项引用（Symbol References）**：[`CONFIG_COEXIST_EXT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEXIST_EXT)、[`CONFIG_BT_COEXIST`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_COEXIST)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_SERIES_AMEBAG2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAG2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_SERIES_AMEBAG2`。

<a id="CONFIG_EXT_PTA_PIN_PRI"></a>

## 13.25 `CONFIG_EXT_PTA_PIN_PRI`

**提示（Prompt）**：PTA 优先级引脚（Priority Pin）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_COEXIST_EXT && CONFIG_BT_COEXIST && !CONFIG_SOC_SERIES_AMEBAD && CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
"PB_2" if CONFIG_SOC_SERIES_AMEBADPLUS
"PA_18" if CONFIG_SOC_SERIES_AMEBAG2
"PB_1" if CONFIG_SOC_SERIES_AMEBAD
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:105`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持

**配置项引用（Symbol References）**：[`CONFIG_COEXIST_EXT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEXIST_EXT)、[`CONFIG_BT_COEXIST`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_COEXIST)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_SERIES_AMEBAG2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAG2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_SERIES_AMEBAG2`。

<a id="CONFIG_EXT_PTA_PIN_REQ"></a>

## 13.26 `CONFIG_EXT_PTA_PIN_REQ`

**提示（Prompt）**：PTA 请求引脚（Request Pin）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_COEXIST_EXT && CONFIG_BT_COEXIST && !CONFIG_SOC_SERIES_AMEBAD && CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
"PB_0" if CONFIG_SOC_SERIES_AMEBADPLUS
"PA_21" if CONFIG_SOC_SERIES_AMEBAG2
"PA_26" if CONFIG_SOC_SERIES_AMEBAD
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:98`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持

**配置项引用（Symbol References）**：[`CONFIG_COEXIST_EXT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEXIST_EXT)、[`CONFIG_BT_COEXIST`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_COEXIST)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_SERIES_AMEBAG2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAG2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_SERIES_AMEBAG2`。

<a id="CONFIG_EXT_REQUEST_POLAR_HIGH"></a>

## 13.27 `CONFIG_EXT_REQUEST_POLAR_HIGH`

**提示（Prompt）**：请求信号高电平有效（Request Active High）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COEX_EXT_REQUEST_POLAR>
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:65`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持 → 请求信号极性（Request Polarity）

**配置项引用（Symbol References）**：[`CONFIG_COEX_EXT_REQUEST_POLAR`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEX_EXT_REQUEST_POLAR)。

<a id="CONFIG_EXT_REQUEST_POLAR_LOW"></a>

## 13.28 `CONFIG_EXT_REQUEST_POLAR_LOW`

**提示（Prompt）**：请求信号低电平有效（Request Active Low）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EXT_PTA_MODE_SIMPLE && <choice CONFIG_COEX_EXT_REQUEST_POLAR>
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:67`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持 → 请求信号极性（Request Polarity）

**配置项引用（Symbol References）**：[`CONFIG_EXT_PTA_MODE_SIMPLE`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_EXT_PTA_MODE_SIMPLE)、[`CONFIG_COEX_EXT_REQUEST_POLAR`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEX_EXT_REQUEST_POLAR)。

<a id="CONFIG_EXT_TRX_DET_TIME"></a>

## 13.29 `CONFIG_EXT_TRX_DET_TIME`

**提示（Prompt）**：收发检测时间（TRX Detection Time）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COEXIST_EXT && CONFIG_BT_COEXIST && !CONFIG_SOC_SERIES_AMEBAD && CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[0, 254]
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/rtk_coex/Kconfig:90`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → 启用外部共存（External Coexistence）支持

**配置项引用（Symbol References）**：[`CONFIG_COEXIST_EXT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_COEXIST_EXT)、[`CONFIG_BT_COEXIST`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_COEXIST)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_REALTEK_AMEBA_HAL_LIB"></a>

## 13.30 `CONFIG_REALTEK_AMEBA_HAL_LIB`

**提示（Prompt）**：Realtek Ameba 硬件抽象层库（HAL Library）

**说明（Help）**

此选项启用 Realtek Ameba 硬件抽象层库（HAL Library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/Kconfig:6`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_REALTEK_AMEBA_ZEPHYR_BT"></a>

## 13.31 `CONFIG_REALTEK_AMEBA_ZEPHYR_BT`

**提示（Prompt）**：Realtek Ameba Zephyr 蓝牙（BT）

**说明（Help）**

此选项启用 Realtek Ameba 蓝牙（BT）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ZEPHYR_MBEDTLS_MODULE
CONFIG_SHARED_INTERRUPTS
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/bluetooth/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_ZEPHYR_MBEDTLS_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_MBEDTLS_MODULE)、[`CONFIG_SHARED_INTERRUPTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHARED_INTERRUPTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_ZEPHYR_MBEDTLS_MODULE`。

<a id="CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI"></a>

## 13.32 `CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`

**提示（Prompt）**：Realtek Ameba Zephyr Wi-Fi

**说明（Help）**

此选项启用 Realtek Ameba Wi-Fi。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/wifi/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_WLAN"></a>

## 13.33 `CONFIG_WLAN`

**提示（Prompt）**：启用 Wi-Fi

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI && CONFIG_SOC_FAMILY_REALTEK_AMEBA && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:hal_realtek>/ameba/common/wifi/Kconfig:11`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Ameba Zephyr Wi-Fi

**配置项引用（Symbol References）**：[`CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_WIFI)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<!-- kconfig-navigation -->

[上一章](P012_module_hal_nxp_mcux_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P014_module_hal_realtek_bee_配置项参考.md)
