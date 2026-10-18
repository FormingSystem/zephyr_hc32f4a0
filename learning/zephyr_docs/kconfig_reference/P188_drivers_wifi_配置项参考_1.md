---
id: learning.zephyr-docs.kconfig-reference.page-188
title: "`drivers/wifi`配置项参考（1/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第188章\_`drivers/wifi`配置项参考（1/7）

本章翻译官方 Kconfig 数据库中 `drivers/wifi` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_AIROC_PART"></a>

## 188.1 `CONFIG_AIROC_PART`

原库同名定义共 2 条；本项为数据库第 397 条记录，各定义分别保留。

**提示（Prompt）**：选择 AIROC 器件（AIROC Part）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_AIROC_WIFI_CUSTOM && CONFIG_WIFI_AIROC && CONFIG_WIFI
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

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_AIROC_WIFI_CUSTOM`](P188_drivers_wifi_配置项参考_1.md#CONFIG_AIROC_WIFI_CUSTOM)、[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_CYW4343W`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4343W)、[`CONFIG_CYW4373`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4373)、[`CONFIG_CYW43012`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43012)、[`CONFIG_CYW43438`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43438)、[`CONFIG_CYW43439`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43439)、[`CONFIG_CYW20829`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW20829)、[`CONFIG_BT_AIROC_CUSTOM`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC_CUSTOM)、[`CONFIG_CYW43022`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW43022)、[`CONFIG_CYW55500`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW55500)、[`CONFIG_CYW55572`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW55572)。

<a id="CONFIG_AIROC_WIFI_BUS_SDIO"></a>

## 188.2 `CONFIG_AIROC_WIFI_BUS_SDIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 SDIO 总线支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDHC
CONFIG_SDIO_STACK
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDIO_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDIO_STACK)。

<a id="CONFIG_AIROC_WIFI_BUS_SPI"></a>

## 188.3 `CONFIG_AIROC_WIFI_BUS_SPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 SPI 总线支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_AIROC_WIFI_CUSTOM"></a>

## 188.4 `CONFIG_AIROC_WIFI_CUSTOM`

**提示（Prompt）**：自定义 CYW43xx 器件／模块

**说明（Help）**

选择自定义 CYW43xx 器件／模块。使用此选项时，用户必须为自定义或厂商 CYW43xx 模块提供固件（FW）、CLM 和非易失性 RAM（NVRAM）文件路径。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_AIROC_WIFI_EVENT_TASK_PRIO"></a>

## 188.5 `CONFIG_AIROC_WIFI_EVENT_TASK_PRIO`

**提示（Prompt）**：事件任务优先级（Event Task Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_AIROC_WIFI_EVENT_TASK_STACK_SIZE"></a>

## 188.6 `CONFIG_AIROC_WIFI_EVENT_TASK_STACK_SIZE`

**提示（Prompt）**：事件任务栈大小（Event Task Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_AIROC_WLAN_MFG_FIRMWARE"></a>

## 188.7 `CONFIG_AIROC_WLAN_MFG_FIRMWARE`

**提示（Prompt）**：无线局域网制造固件（WLAN Manufacturing Firmware）

**说明（Help）**

启用无线局域网制造固件（WLAN Manufacturing Firmware）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_AMEBA_WIFI_EVENT_STACK_SIZE"></a>

## 188.8 `CONFIG_AMEBA_WIFI_EVENT_STACK_SIZE`

**提示（Prompt）**：Ameba Wi-Fi 事件线程栈大小

**说明（Help）**

Ameba Wi-Fi 事件处理线程的栈大小。如果出现栈溢出，可增大此值；也可减小此值以节省 RAM。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AMEBA && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/wifi/ameba/Kconfig.ameba:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/ameba/Kconfig.ameba#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Ameba 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AMEBA)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_BT_COEXIST"></a>

## 188.9 `CONFIG_BT_COEXIST`

原库同名定义共 2 条；本项为数据库第 1694 条记录，各定义分别保留。

**提示（Prompt）**：Wi-Fi／蓝牙共存（Wi-Fi/Bluetooth Coexistence）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AMEBA && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/ameba/Kconfig.ameba:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/ameba/Kconfig.ameba#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Ameba 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AMEBA)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_CYW43012"></a>

## 188.10 `CONFIG_CYW43012`

原库同名定义共 2 条；本项为数据库第 4588 条记录，各定义分别保留。

**提示（Prompt）**：CYW43012

**说明（Help）**

启用 Infineon AIROC CYW43012 Wi-Fi 连接功能。器件详情请参阅 [Infineon CYW43012 官方页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/cyw43012/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AIROC_PART>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)。

<a id="CONFIG_CYW43012_MODULE"></a>

## 188.11 `CONFIG_CYW43012_MODULE`

原库同名定义共 2 条；本项为数据库第 4590 条记录，各定义分别保留。

**提示（Prompt）**：选择 CYW43012 模块（Module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW43012 && !CONFIG_AIROC_WIFI_CUSTOM && CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**可选项（Choices）**

```text
CONFIG_CYW43012_MURATA_1LV
CONFIG_CYW43012_MURATA_1LV
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_CYW43012`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43012)、[`CONFIG_AIROC_WIFI_CUSTOM`](P188_drivers_wifi_配置项参考_1.md#CONFIG_AIROC_WIFI_CUSTOM)、[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_CYW43012_MURATA_1LV`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43012_MURATA_1LV)。

<a id="CONFIG_CYW43012_MURATA_1LV"></a>

## 188.12 `CONFIG_CYW43012_MURATA_1LV`

原库同名定义共 2 条；本项为数据库第 4592 条记录，各定义分别保留。

**提示（Prompt）**：MURATA-1LV

**说明（Help）**

村田（Murata）Type 1LV 模块基于英飞凌（Infineon）CYW43012 组合芯片组（Combo Chipset），支持 Wi-Fi® 802.11a/b/g/n 与 Bluetooth® 5.0 基本速率／增强数据速率／低功耗（BR/EDR/LE）。Wi-Fi 物理层（PHY）数据速率最高 72.2 Mbps，蓝牙 PHY 数据速率最高 3 Mbps，也支持 2 Mbps LE PHY。更多信息见[村田 Type 1LV 官方模块页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type1lv)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW43012_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 CYW43012 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_CYW43012_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43012_MODULE)。

<a id="CONFIG_CYW43022"></a>

## 188.13 `CONFIG_CYW43022`

**提示（Prompt）**：CYW43022

**说明（Help）**

启用 Infineon AIROC CYW43022 Wi-Fi 连接功能。器件详情请参阅 [Infineon CYW43022 官方页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-5-802.11ac/cyw43022/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AIROC_PART>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)。

<a id="CONFIG_CYW43022CUB"></a>

## 188.14 `CONFIG_CYW43022CUB`

**提示（Prompt）**：CYW43022CUB

**说明（Help）**

Infineon CYW43022CUB M2 模块。模块详情请参阅 [Infineon CYW43022 官方页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-5-802.11ac/cyw43022/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW43022_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 CYW43022 模块

**配置项引用（Symbol References）**：[`CONFIG_CYW43022_MODULE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW43022_MODULE)。

<a id="CONFIG_CYW43022_MODULE"></a>

## 188.15 `CONFIG_CYW43022_MODULE`

**提示（Prompt）**：选择 CYW43022 模块

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW43022 && !CONFIG_AIROC_WIFI_CUSTOM && CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**可选项（Choices）**

```text
CONFIG_CYW43022CUB
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L160)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_CYW43022`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW43022)、[`CONFIG_AIROC_WIFI_CUSTOM`](P188_drivers_wifi_配置项参考_1.md#CONFIG_AIROC_WIFI_CUSTOM)、[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_CYW43022CUB`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW43022CUB)。

<a id="CONFIG_CYW43438"></a>

## 188.16 `CONFIG_CYW43438`

原库同名定义共 2 条；本项为数据库第 4597 条记录，各定义分别保留。

**提示（Prompt）**：CYW43438

**说明（Help）**

启用 Infineon AIROC CYW43438 Wi-Fi 连接功能。器件详情请参阅 [Infineon CYW43438 官方页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/cyw43438/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AIROC_PART>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)。

<a id="CONFIG_CYW43439"></a>

## 188.17 `CONFIG_CYW43439`

原库同名定义共 2 条；本项为数据库第 4599 条记录，各定义分别保留。

**提示（Prompt）**：CYW43439

**说明（Help）**

启用 Infineon AIROC CYW43439 Wi-Fi 连接功能。器件详情请参阅 [Infineon CYW43439 官方页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/cyw43439/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AIROC_PART>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)。

<a id="CONFIG_CYW43439_MODULE"></a>

## 188.18 `CONFIG_CYW43439_MODULE`

原库同名定义共 2 条；本项为数据库第 4601 条记录，各定义分别保留。

**提示（Prompt）**：选择 CYW43439 模块（Module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW43439 && !CONFIG_AIROC_WIFI_CUSTOM && CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**可选项（Choices）**

```text
CONFIG_CYW43439_MURATA_1YN
CONFIG_CYW43439_MURATA_1YN
CONFIG_CYW43439_STERLING_LWBPLUS
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:220`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L220)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_CYW43439`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43439)、[`CONFIG_AIROC_WIFI_CUSTOM`](P188_drivers_wifi_配置项参考_1.md#CONFIG_AIROC_WIFI_CUSTOM)、[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_CYW43439_MURATA_1YN`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43439_MURATA_1YN)、[`CONFIG_CYW43439_STERLING_LWBPLUS`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW43439_STERLING_LWBPLUS)。

<a id="CONFIG_CYW43439_MURATA_1YN"></a>

## 188.19 `CONFIG_CYW43439_MURATA_1YN`

原库同名定义共 2 条；本项为数据库第 4603 条记录，各定义分别保留。

**提示（Prompt）**：MURATA_1YN

**说明（Help）**

村田（Murata）Type 1YN 模块基于英飞凌（Infineon）CYW43439 组合芯片组（Combo Chipset），支持 Wi-Fi® 802.11b/g/n 与 Bluetooth® 5.2 基本速率／增强数据速率／低功耗（BR/EDR/LE）。Wi-Fi 物理层（PHY）数据速率最高 65 Mbps，蓝牙 PHY 数据速率最高 3 Mbps。更多信息见[村田 Type 1YN 官方模块页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type1yn)。

译注：此处 Bluetooth 5.2 保留自 Zephyr 官方配置数据库。2026-10-17 核验所引村田 Type 1YN 官方页面时，其 Description 和 Specs 写为 Bluetooth 5.1；两份来源存在版本差异，不能把本条译文当作独立确认的硬件版本规格。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW43439_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:224`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L224)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 CYW43439 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_CYW43439_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43439_MODULE)。

<a id="CONFIG_CYW43439_STERLING_LWBPLUS"></a>

## 188.20 `CONFIG_CYW43439_STERLING_LWBPLUS`

**提示（Prompt）**：STERLING-LWBplus

**说明（Help）**

Ezurio Sterling-LWB+ Wi-Fi 4 与蓝牙 5.2 模块。模块详情请参阅 [Ezurio Sterling-LWB+ 官方页面](https://www.ezurio.com/wireless-modules/wifi-modules-bluetooth/sterling-lwb-wifi-4-and-bluetooth-52-modules)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW43439_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L235)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 CYW43439 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_CYW43439_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43439_MODULE)。

<a id="CONFIG_CYW4343W"></a>

## 188.21 `CONFIG_CYW4343W`

原库同名定义共 2 条；本项为数据库第 4606 条记录，各定义分别保留。

**提示（Prompt）**：CYW4343W

**说明（Help）**

启用 Infineon AIROC CYW4343W Wi-Fi 连接功能。器件详情请参阅 [Infineon CYW4343W 官方页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/cyw4343w/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AIROC_PART>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)。

<a id="CONFIG_CYW4343W_MODULE"></a>

## 188.22 `CONFIG_CYW4343W_MODULE`

原库同名定义共 2 条；本项为数据库第 4608 条记录，各定义分别保留。

**提示（Prompt）**：选择 CYW4343W 模块（Module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW4343W && !CONFIG_AIROC_WIFI_CUSTOM && CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**可选项（Choices）**

```text
CONFIG_CYW4343W_MURATA_1DX
CONFIG_CYW4343W_MURATA_1DX
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_CYW4343W`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4343W)、[`CONFIG_AIROC_WIFI_CUSTOM`](P188_drivers_wifi_配置项参考_1.md#CONFIG_AIROC_WIFI_CUSTOM)、[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_CYW4343W_MURATA_1DX`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4343W_MURATA_1DX)。

<a id="CONFIG_CYW4343W_MURATA_1DX"></a>

## 188.23 `CONFIG_CYW4343W_MURATA_1DX`

原库同名定义共 2 条；本项为数据库第 4610 条记录，各定义分别保留。

**提示（Prompt）**：MURATA-1DX

**说明（Help）**

村田（Murata）Type 1DX 模块基于英飞凌（Infineon）CYW4343W 组合芯片组（Combo Chipset），支持 Wi-Fi® 802.11b/g/n 与 Bluetooth® 5.1 基本速率／增强数据速率／低功耗（BR/EDR/LE）。Wi-Fi 物理层（PHY）数据速率最高 65 Mbps，蓝牙 PHY 数据速率最高 3 Mbps。更多信息见[村田 Type 1DX 官方模块页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type1dx)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW4343W_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 CYW4343W 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_CYW4343W_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4343W_MODULE)。

<a id="CONFIG_CYW4373"></a>

## 188.24 `CONFIG_CYW4373`

原库同名定义共 2 条；本项为数据库第 4612 条记录，各定义分别保留。

**提示（Prompt）**：CYW4373

**说明（Help）**

启用 Infineon AIROC CYW4373 Wi-Fi 连接功能。器件详情请参阅 [Infineon CYW4373 官方页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/cyw4373/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AIROC_PART>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)。

<a id="CONFIG_CYW4373_MODULE"></a>

## 188.25 `CONFIG_CYW4373_MODULE`

原库同名定义共 2 条；本项为数据库第 4614 条记录，各定义分别保留。

**提示（Prompt）**：选择 CYW4373 模块（Module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW4373 && !CONFIG_AIROC_WIFI_CUSTOM && CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**可选项（Choices）**

```text
CONFIG_CYW4373_STERLING_LWB5PLUS
CONFIG_CYW4373_MURATA_2AE
CONFIG_CYW4373_MURATA_2BC
CONFIG_CYW4373_STERLING_LWB5PLUS
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_CYW4373`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4373)、[`CONFIG_AIROC_WIFI_CUSTOM`](P188_drivers_wifi_配置项参考_1.md#CONFIG_AIROC_WIFI_CUSTOM)、[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_CYW4373_STERLING_LWB5PLUS`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4373_STERLING_LWB5PLUS)、[`CONFIG_CYW4373_MURATA_2AE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW4373_MURATA_2AE)、[`CONFIG_CYW4373_MURATA_2BC`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW4373_MURATA_2BC)。

<a id="CONFIG_CYW4373_MURATA_2AE"></a>

## 188.26 `CONFIG_CYW4373_MURATA_2AE`

**提示（Prompt）**：CYW4373_MURATA_2AE

**说明（Help）**

基于 Infineon CYW4373 组合芯片组（Combo Chipset）的 Murata Type 2AE 模块。模块详情请参阅 [Murata Type 2AE 官方页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2ae)。

译注：Zephyr 本快照写作 CYW4373；核对时 Murata 页面标为 CYW4373E。此处保留 Zephyr 原文型号，未据厂商现页改写配置定义。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW4373_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 CYW4373 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_CYW4373_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4373_MODULE)。

<a id="CONFIG_CYW4373_MURATA_2BC"></a>

## 188.27 `CONFIG_CYW4373_MURATA_2BC`

**提示（Prompt）**：CYW4373_MURATA_2BC

**说明（Help）**

基于 Infineon CYW4373 组合芯片组（Combo Chipset）的 Murata Type 2BC 模块。模块详情请参阅 [Murata Type 2BC 官方页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2bc)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW4373_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 CYW4373 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_CYW4373_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4373_MODULE)。

<a id="CONFIG_CYW4373_STERLING_LWB5PLUS"></a>

## 188.28 `CONFIG_CYW4373_STERLING_LWB5PLUS`

原库同名定义共 2 条；本项为数据库第 4618 条记录，各定义分别保留。

**提示（Prompt）**：STERLING-LWB5plus

**说明（Help）**

Ezurio Sterling LWB5+ 802.11ac／蓝牙 5.0 M.2 载板（Carrier Board），采用 E 型键位（E-Type Key），配备 SDIO/UART。模块详情请参阅 [Ezurio Sterling LWB5+ 官方页面](https://www.ezurio.com/wireless-modules/wifi-modules-bluetooth/sterling-lwb5-plus-wifi-5-bluetooth-5-module)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW4373_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:210`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L210)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 CYW4373 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_CYW4373_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4373_MODULE)。

<a id="CONFIG_CYW55500"></a>

## 188.29 `CONFIG_CYW55500`

**提示（Prompt）**：CYW55500

**说明（Help）**

启用 Infineon AIROC CYW55500 Wi-Fi 连接功能。原文提供的详细信息链接为 [Infineon CYW55511 官方页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-6-6e-802.11ax/cyw55511/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AIROC_PART>
```

**主动选择（Selects）**

```text
CONFIG_AIROC_WIFI6 if CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)、[`CONFIG_AIROC_WIFI6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AIROC_WIFI6)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_AIROC_WIFI6`。

<a id="CONFIG_CYW55500_MODULE"></a>

## 188.30 `CONFIG_CYW55500_MODULE`

原库同名定义共 2 条；本项为数据库第 4621 条记录，各定义分别保留。

**提示（Prompt）**：选择 CYW55500 模块

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW55500 && !CONFIG_AIROC_WIFI_CUSTOM && CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**可选项（Choices）**

```text
CONFIG_CYW55513IUBG_SM
CONFIG_CYW55513_MURATA_2FY
CONFIG_CYW955513SDM2WLIPA_SM
CONFIG_CYW55513IUBG_SM
CONFIG_CYW55513_MURATA_2FY_SM
CONFIG_CYW55513_MOD_PSE84_SOM
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:244`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L244)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_CYW55500`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW55500)、[`CONFIG_AIROC_WIFI_CUSTOM`](P188_drivers_wifi_配置项参考_1.md#CONFIG_AIROC_WIFI_CUSTOM)、[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_CYW55513IUBG_SM`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW55513IUBG_SM)、[`CONFIG_CYW55513_MURATA_2FY`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW55513_MURATA_2FY)、[`CONFIG_CYW955513SDM2WLIPA_SM`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW955513SDM2WLIPA_SM)、[`CONFIG_CYW55513_MURATA_2FY_SM`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW55513_MURATA_2FY_SM)、[`CONFIG_CYW55513_MOD_PSE84_SOM`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW55513_MOD_PSE84_SOM)。

<a id="CONFIG_CYW55513IUBG_SM"></a>

## 188.31 `CONFIG_CYW55513IUBG_SM`

原库同名定义共 2 条；本项为数据库第 4623 条记录，各定义分别保留。

**提示（Prompt）**：CYW55513IUBG_SM

**说明（Help）**

Infineon CYW55513IUBG（SM）模块

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW55500_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L253)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 CYW55500 模块

**配置项引用（Symbol References）**：[`CONFIG_CYW55500_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW55500_MODULE)。

<a id="CONFIG_CYW55513_MOD_PSE84_SOM"></a>

## 188.32 `CONFIG_CYW55513_MOD_PSE84_SOM`

**提示（Prompt）**：CYW55513_MOD_PSE84_SOM

**说明（Help）**

Infineon CYW55513_MOD_PSE84_SOM（SM）模块

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW55500_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:263`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L263)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 CYW55500 模块

**配置项引用（Symbol References）**：[`CONFIG_CYW55500_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW55500_MODULE)。

<a id="CONFIG_CYW55513_MURATA_2FY_SM"></a>

## 188.33 `CONFIG_CYW55513_MURATA_2FY_SM`

**提示（Prompt）**：CYW55513 MURATA-2FY（SM）

**说明（Help）**

Murata LBEE5HY2FY（Type 2FY）模块中的 Infineon CYW55513（SM）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW55500_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:258`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L258)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 CYW55500 模块

**配置项引用（Symbol References）**：[`CONFIG_CYW55500_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW55500_MODULE)。

<a id="CONFIG_CYW55572"></a>

## 188.34 `CONFIG_CYW55572`

**提示（Prompt）**：CYW55572

**说明（Help）**

启用 Infineon AIROC CYW55572 Wi-Fi 连接功能。器件详情请参阅 [Infineon CYW55572 官方页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-6-6e-802.11ax/cyw55572/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AIROC_PART>
```

**主动选择（Selects）**

```text
CONFIG_AIROC_WIFI6
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)、[`CONFIG_AIROC_WIFI6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AIROC_WIFI6)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_AIROC_WIFI6`。

<a id="CONFIG_CYW55572_MODULE"></a>

## 188.35 `CONFIG_CYW55572_MODULE`

**提示（Prompt）**：选择 CYW55572 模块

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW55572 && !CONFIG_AIROC_WIFI_CUSTOM && CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**可选项（Choices）**

```text
CONFIG_CYW955573M2IPA1_SM
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:270`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L270)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_CYW55572`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW55572)、[`CONFIG_AIROC_WIFI_CUSTOM`](P188_drivers_wifi_配置项参考_1.md#CONFIG_AIROC_WIFI_CUSTOM)、[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_CYW955573M2IPA1_SM`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW955573M2IPA1_SM)。

<a id="CONFIG_CYW955513SDM2WLIPA_SM"></a>

## 188.36 `CONFIG_CYW955513SDM2WLIPA_SM`

**提示（Prompt）**：CYW955513SDM2WLIPA_SM

**说明（Help）**

Infineon CYW955513SDM2WLIPA（SM）模块

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW55500_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:248`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L248)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 CYW55500 模块

**配置项引用（Symbol References）**：[`CONFIG_CYW55500_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW55500_MODULE)。

<a id="CONFIG_CYW955573M2IPA1_SM"></a>

## 188.37 `CONFIG_CYW955573M2IPA1_SM`

**提示（Prompt）**：CYW955573M2IPA1_SM

**说明（Help）**

Infineon CYW955573M2IPA1（SM）模块

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW55572_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:274`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L274)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持 → 选择 CYW55572 模块

**配置项引用（Symbol References）**：[`CONFIG_CYW55572_MODULE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW55572_MODULE)。

<a id="CONFIG_ESP32_WIFI_11KV_SUPPORT"></a>

## 188.38 `CONFIG_ESP32_WIFI_11KV_SUPPORT`

**提示（Prompt）**：802.11k 和 802.11v 支持

**说明（Help）**

构建 Espressif 认证客户端（Supplicant）中的 802.11k 无线资源测量（Radio Resource Measurement）和 802.11v 无线网络管理（Wireless Network Management）代码。此选项是总开关；`ESP32_WIFI_RRM_SUPPORT` 和 `ESP32_WIFI_WNM_SUPPORT` 随之启用，也可分别关闭。漫游策略（Roaming Policy）仍由应用决定：驱动声明支持的能力，并通过 Wi-Fi 管理 API 提供 11k/11v 操作，但不会自行决定切换接入点（AP）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_WIFI_NM_WPA_SUPPLICANT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:823`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L823)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_11R_SUPPORT"></a>

## 188.39 `CONFIG_ESP32_WIFI_11R_SUPPORT`

**提示（Prompt）**：802.11r 快速基本服务集转换（Fast BSS Transition）

**说明（Help）**

构建 Espressif 认证客户端（Supplicant）的快速基本服务集转换（Fast BSS Transition，FT）代码。802.11r 将密钥协商包含在认证交换中，缩短重新关联过程，使漫游无需执行完整的四次握手（Four-way Handshake）。

站点（Station）仅在连接请求设置 `ft_used` 时声明 FT 能力，因此启用此选项只是将快速 BSS 转换代码加入镜像，不改变默认关联行为。启用 `ESP32_WIFI_ENTERPRISE` 时，此选项默认开启，因为在此选项出现之前，企业模式已遵循 `ft_used` 设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_WIFI_NM_WPA_SUPPLICANT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_ESP32_WIFI_ENTERPRISE
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:967`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L967)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)。

<a id="CONFIG_ESP32_WIFI_AMPDU_RX_ENABLED"></a>

## 188.40 `CONFIG_ESP32_WIFI_AMPDU_RX_ENABLED`

**提示（Prompt）**：Wi-Fi 聚合 MAC 协议数据单元接收（A-MPDU RX）

**说明（Help）**

启用聚合 MAC 协议数据单元接收（A-MPDU RX）功能。原文说明，它以处理速度为代价，改善传输错误检查及整体网络性能；设备工作于拥挤无线环境时有帮助。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:273`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L273)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_AMPDU_TX_ENABLED"></a>

## 188.41 `CONFIG_ESP32_WIFI_AMPDU_TX_ENABLED`

**提示（Prompt）**：Wi-Fi 聚合 MAC 协议数据单元发送（A-MPDU TX）

**说明（Help）**

启用聚合 MAC 协议数据单元发送（A-MPDU TX）功能。原文说明，它以处理速度为代价，改善传输错误检查及整体网络性能；设备工作于拥挤无线环境时有帮助。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L253)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_AMSDU_TX_ENABLED"></a>

## 188.42 `CONFIG_ESP32_WIFI_AMSDU_TX_ENABLED`

**提示（Prompt）**：Wi-Fi 聚合 MAC 服务数据单元发送（A-MSDU TX）

**说明（Help）**

启用聚合 MAC 服务数据单元发送（A-MSDU TX）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_SPIRAM && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:296`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L296)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_ESP_SPIRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_SPIRAM)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_AP_STA_MODE"></a>

## 188.43 `CONFIG_ESP32_WIFI_AP_STA_MODE`

**提示（Prompt）**：启用站点／接入点共存模式（Station/AP Coexistence Mode）

**说明（Help）**

站点／接入点共存模式（Station/AP Coexistence Mode）允许 ESP32 同时作为站点和接入点工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_USAGE_MODE_STA_AP
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_WIFI_USAGE_MODE_STA_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USAGE_MODE_STA_AP)。

<a id="CONFIG_ESP32_WIFI_BSS_MAX_IDLE_SUPPORT"></a>

## 188.44 `CONFIG_ESP32_WIFI_BSS_MAX_IDLE_SUPPORT`

**提示（Prompt）**：基本服务集最大空闲（BSS Max Idle）支持

**说明（Help）**

在 Espressif Wi-Fi 驱动中启用基本服务集最大空闲（BSS Max Idle）功能的能力声明。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_ENTERPRISE && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:815`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L815)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → WPA2/WPA3 企业模式（Enterprise）站点支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_CACHE_TX_BUFFER_NUM"></a>

## 188.45 `CONFIG_ESP32_WIFI_CACHE_TX_BUFFER_NUM`

**提示（Prompt）**：Wi-Fi 缓存发送（Cache TX）缓冲区最大数量

**说明（Help）**

设置 Wi-Fi 缓存发送（TX）缓冲区数量。对于来自上层，例如 lwIP，的每个发送包，Wi-Fi 驱动需要分配静态发送缓冲区，并复制上层包。如果无法分配静态发送缓冲区，驱动将上层包缓存到专用缓冲队列中。此选项配置该缓存发送队列的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_SPIRAM && CONFIG_ESP_WIFI_HEAP_SPIRAM && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[16, 128]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:171`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L171)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_ESP_SPIRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_SPIRAM)、[`CONFIG_ESP_WIFI_HEAP_SPIRAM`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP_WIFI_HEAP_SPIRAM)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_CSI_ENABLED"></a>

## 188.46 `CONFIG_ESP32_WIFI_CSI_ENABLED`

**提示（Prompt）**：Wi-Fi 信道状态信息（Channel State Information，CSI）

**说明（Help）**

启用信道状态信息（CSI）功能。CSI 大约占用 `CONFIG_ESP32_WIFI_STATIC_RX_BUFFER_NUM` KB RAM。不使用 CSI 时，最好禁用此功能以节省内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:245`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L245)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_DEBUG_PRINT"></a>

## 188.47 `CONFIG_ESP32_WIFI_DEBUG_PRINT`

**提示（Prompt）**：打印 WPA 认证客户端（Supplicant）的调试消息

**说明（Help）**

启用 WPA 认证客户端（Supplicant）日志输出。根据工程日志等级，内容可能包括握手信息和密钥的十六进制转储（Hex Dump）。启用后，构建产物大小可能增加约 60 kb，具体取决于工程日志等级；这里保留原文的单位写法。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:1029`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L1029)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_DYNAMIC_RX_BUFFER_NUM"></a>

## 188.48 `CONFIG_ESP32_WIFI_DYNAMIC_RX_BUFFER_NUM`

**提示（Prompt）**：Wi-Fi 动态接收（Dynamic RX）缓冲区最大数量

**说明（Help）**

设置 Wi-Fi 动态接收（RX）缓冲区数量。0 表示不限制分配数量，前提是有足够的空闲 RAM。每个动态接收缓冲区的大小取决于收到的数据帧大小。Wi-Fi 驱动将每个接收帧复制到接收缓冲区，再交给上层 TCP/IP 协议栈；上层成功接收数据帧后，释放该动态缓冲区。

缓冲区从 `ESP_WIFI_HEAP` 选定的 Wi-Fi 适配器堆分配。堆耗尽时，将丢弃收到的帧。某些应用中，Wi-Fi 数据帧到达速度可能高于应用处理速度；若接收缓冲区数量不受限制，即设为 0，可能耗尽内存。若设置动态接收缓冲区上限，其值至少应等于静态接收缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[0, 128]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_DYNAMIC_RX_MGMT_BUFFER"></a>

## 188.49 `CONFIG_ESP32_WIFI_DYNAMIC_RX_MGMT_BUFFER`

**提示（Prompt）**：动态（Dynamic）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_WIFI_MGMT_RX_BUFFER>
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:225`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L225)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → Wi-Fi 接收管理帧（RX MGMT）缓冲区类型

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_MGMT_RX_BUFFER`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MGMT_RX_BUFFER)。

<a id="CONFIG_ESP32_WIFI_DYNAMIC_TX_BUFFER"></a>

## 188.50 `CONFIG_ESP32_WIFI_DYNAMIC_TX_BUFFER`

**提示（Prompt）**：动态（Dynamic）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_WIFI_TX_BUFFER>
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → Wi-Fi 发送（TX）缓冲区类型

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_TX_BUFFER`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_TX_BUFFER)。

<a id="CONFIG_ESP32_WIFI_DYNAMIC_TX_BUFFER_NUM"></a>

## 188.51 `CONFIG_ESP32_WIFI_DYNAMIC_TX_BUFFER_NUM`

**提示（Prompt）**：Wi-Fi 动态发送（Dynamic TX）缓冲区最大数量

**说明（Help）**

设置 Wi-Fi 动态发送（TX）缓冲区数量。每个缓冲区大小不固定，取决于待发送数据帧大小。对于来自上层 TCP/IP 协议栈的每个发送帧，Wi-Fi 驱动都会将其复制到发送缓冲区。某些应用，尤其 UDP 应用，可能以高于 Wi-Fi 层发送速度的速率提交帧，导致发送缓冲区耗尽。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_DYNAMIC_TX_BUFFER && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 128]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_DYNAMIC_TX_BUFFER`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_DYNAMIC_TX_BUFFER)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_ENABLE_SAE_H2E"></a>

## 188.52 `CONFIG_ESP32_WIFI_ENABLE_SAE_H2E`

**提示（Prompt）**：SAE 哈希到元素（Hash-to-Element，H2E）

**说明（Help）**

为 SAE 密码派生（Password Derivation）启用哈希到元素（Hash-to-Element，H2E）方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:1000`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L1000)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → WPA3 个人模式（WPA3-Personal）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_ENABLE_SAE_PK"></a>

## 188.53 `CONFIG_ESP32_WIFI_ENABLE_SAE_PK`

**提示（Prompt）**：SAE 公钥扩展（SAE-PK）

**说明（Help）**

启用 SAE 公钥扩展（SAE-PK）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_ENABLE_SAE_H2E && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:1007`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L1007)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → WPA3 个人模式（WPA3-Personal） → SAE 哈希到元素（Hash-to-Element，H2E）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_ENABLE_SAE_H2E`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENABLE_SAE_H2E)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_ENABLE_WPA3_OWE_STA"></a>

## 188.54 `CONFIG_ESP32_WIFI_ENABLE_WPA3_OWE_STA`

**提示（Prompt）**：机会式无线加密站点（OWE STA）

**说明（Help）**

允许设备与符合条件的接入点（AP）建立机会式无线加密（OWE）连接。注意，ESP32 当前仅在站点（STA）模式下支持 OWE。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:992`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L992)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → WPA3 个人模式（WPA3-Personal）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE"></a>

## 188.55 `CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE`

**提示（Prompt）**：WPA3 个人模式（WPA3-Personal）

**说明（Help）**

允许设备建立 WPA3 个人模式（WPA3-Personal）连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:984`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L984)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)。

<a id="CONFIG_ESP32_WIFI_ENHANCED_LIGHT_SLEEP"></a>

## 188.56 `CONFIG_ESP32_WIFI_ENHANCED_LIGHT_SLEEP`

**提示（Prompt）**：Wi-Fi 调制解调器自动接收信标（Beacon）［实验性，EXPERIMENTAL］

**说明（Help）**

在轻度睡眠（Light Sleep）期间，由 Wi-Fi 调制解调器自动接收信标帧（Beacon Frame），使用电源管理单元（PMU）调制解调器状态唤醒。这将 CPU 唤醒工作从 RTC 定时器交给 PMU 调制解调器状态机。

实验性限制：已知某些配置下断开连接时会导致系统挂起。若需要可靠的保持连接轻度睡眠，请使用普通 `MAC_BB_PD` 轻度睡眠，不启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MAC_BB_PD && CONFIG_SOC_ESP32_PM_SUPPORT_BEACON_WAKEUP && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:669`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L669)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_MAC_BB_PD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAC_BB_PD)、[`CONFIG_SOC_ESP32_PM_SUPPORT_BEACON_WAKEUP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_PM_SUPPORT_BEACON_WAKEUP)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32_PM_SUPPORT_BEACON_WAKEUP`。

<a id="CONFIG_ESP32_WIFI_ENTERPRISE"></a>

## 188.57 `CONFIG_ESP32_WIFI_ENTERPRISE`

**提示（Prompt）**：WPA2/WPA3 企业模式（Enterprise）站点支持

**说明（Help）**

允许 ESP32 Wi-Fi 站点驱动通过 Espressif EAP 认证客户端（Supplicant），连接 WPA2 企业模式（WPA2-Enterprise）和 WPA3 企业模式（WPA3-Enterprise）网络。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_WIFI_CERTIFICATE_LIB
CONFIG_MBEDTLS
CONFIG_MBEDTLS_PEM_PARSE_C
CONFIG_MBEDTLS_SSL_EXTENDED_MASTER_SECRET
CONFIG_MBEDTLS_SSL_KEYING_MATERIAL_EXPORT
CONFIG_MBEDTLS_SSL_SERVER_NAME_INDICATION
CONFIG_MBEDTLS_X509_CRL_PARSE_C
CONFIG_MBEDTLS_X509_CRT_PARSE_C
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:751`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L751)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_WIFI_CERTIFICATE_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CERTIFICATE_LIB)、[`CONFIG_MBEDTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_PEM_PARSE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PEM_PARSE_C)、[`CONFIG_MBEDTLS_SSL_EXTENDED_MASTER_SECRET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_EXTENDED_MASTER_SECRET)、[`CONFIG_MBEDTLS_SSL_KEYING_MATERIAL_EXPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_KEYING_MATERIAL_EXPORT)、[`CONFIG_MBEDTLS_SSL_SERVER_NAME_INDICATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_SERVER_NAME_INDICATION)、[`CONFIG_MBEDTLS_X509_CRL_PARSE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_X509_CRL_PARSE_C)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)。

<a id="CONFIG_ESP32_WIFI_ENTERPRISE_MBEDTLS_TLS_CLIENT"></a>

## 188.58 `CONFIG_ESP32_WIFI_ENTERPRISE_MBEDTLS_TLS_CLIENT`

**提示（Prompt）**：WPA 企业模式（WPA-Enterprise）使用 Mbed TLS TLS 客户端

**说明（Help）**

使用 Espressif 认证客户端（Supplicant）的 Mbed TLS TLS 后端执行 EAP TLS 握手。这也是 Espressif 企业 Wi-Fi 示例使用的后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_ENTERPRISE && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:770`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L770)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → WPA2/WPA3 企业模式（Enterprise）站点支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_EVENT_QUEUE_SIZE"></a>

## 188.59 `CONFIG_ESP32_WIFI_EVENT_QUEUE_SIZE`

**提示（Prompt）**：Wi-Fi 事件队列深度（Event Queue Depth）

**说明（Help）**

Wi-Fi 库任务与事件任务之间可缓冲的已投递事件数量。每个队列条目都内嵌一份事件载荷（Event Payload）副本，因此 RAM 开销等于队列深度乘以条目大小。事件在事件任务上异步交付，不在库任务上直接执行，从而将处理程序的工作移出库任务。

Mesh 需要这种机制：它从事件处理程序启动网络协议栈，包括 DHCP 服务器、网络地址转换（NAT）和路由。这些工作既超出库任务栈的承载范围，也不应阻塞库任务。每次投递携带调用方指定的超时时间。库投递大多数事件时不等待，所以队列满时会丢弃这些事件，并记录错误级日志。可能填满队列的事件包括 SoftAP 客户端频繁加入／退出，以及 Mesh 路由更新；后续事件或重新选择父节点（Re-parent）可取代先前事件。队列容量用于吸收这类突发。

不能丢失事件的调用方会等待，但事件任务自身例外：它负责消费此队列，因此绝不会等待该队列腾出空间。如果站点或 SoftAP 状态转换事件因此丢失，驱动状态会停留在旧值，直到下一次状态转换；因此，队列深度足以容纳数倍于一次突发的状态事件。由于处理程序只更新状态并发出网络管理事件，通常只有事件任务完全得不到调度时才会达到此上限。

这种情况下，仍可通过 `NET_REQUEST_WIFI_IFACE_STATUS` 读取驱动状态。通知进一步传给应用时，网络管理层还有独立的反压（Backpressure）机制，参见 `NET_MGMT_EVENT_QUEUE_SIZE` 和 `NET_MGMT_EVENT_QUEUE_TIMEOUT`。如果观察到事件丢失，可增加队列深度，代价是占用更多 RAM。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:388`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L388)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_EVENT_TASK_PRIORITY"></a>

## 188.60 `CONFIG_ESP32_WIFI_EVENT_TASK_PRIORITY`

**提示（Prompt）**：Wi-Fi 事件任务优先级

**说明（Help）**

Wi-Fi 事件任务的抢占式优先级（Preemptible Priority）。应使其高于应用线程，以及时处理连接和断开状态变化。必须确认状态变化后才能继续的调用方，应通过事件同步，而不要依赖此任务抢占自身。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:370`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L370)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_EVENT_TASK_STACK_SIZE"></a>

## 188.61 `CONFIG_ESP32_WIFI_EVENT_TASK_STACK_SIZE`

**提示（Prompt）**：Wi-Fi 事件任务栈大小

**说明（Help）**

运行 Wi-Fi 和 Mesh 事件处理程序的事件任务栈大小。Wi-Fi 库从自身任务投递事件，处理程序则在此专用任务中运行，避免处理程序使库任务栈溢出或阻塞库任务。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:361`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L361)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_EXTRA_IRAM_OPT"></a>

## 188.62 `CONFIG_ESP32_WIFI_EXTRA_IRAM_OPT`

**提示（Prompt）**：Wi-Fi 额外指令 RAM（EXTRA IRAM）速度优化

**说明（Help）**

将更多频繁调用的 Wi-Fi 库函数放入指令 RAM（IRAM）。禁用此选项可节省超过 5 Kbytes 的 IRAM，但会降低 Wi-Fi 吞吐量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_ESP32_WIFI_HE_SUPPORT
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:316`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L316)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_SOC_ESP32_WIFI_HE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_WIFI_HE_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32_WIFI_HE_SUPPORT`。

<a id="CONFIG_ESP32_WIFI_FTM_ENABLE"></a>

## 188.63 `CONFIG_ESP32_WIFI_FTM_ENABLE`

**提示（Prompt）**：Wi-Fi 精细时间测量（FTM）

**说明（Help）**

启用精细时间测量（Fine Timing Measurement，FTM）功能，用于计算 Wi-Fi 往返时间（Round-Trip-Time，RTT）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C3 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3) && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:477`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L477)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`。

<a id="CONFIG_ESP32_WIFI_FTM_INITIATOR_SUPPORT"></a>

## 188.64 `CONFIG_ESP32_WIFI_FTM_INITIATOR_SUPPORT`

**提示（Prompt）**：FTM 发起方（Initiator）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_FTM_ENABLE && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:485`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L485)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → Wi-Fi 精细时间测量（FTM）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_FTM_ENABLE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_FTM_ENABLE)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_FTM_RESPONDER_SUPPORT"></a>

## 188.65 `CONFIG_ESP32_WIFI_FTM_RESPONDER_SUPPORT`

**提示（Prompt）**：FTM 响应方（Responder）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_FTM_ENABLE && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:490`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L490)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → Wi-Fi 精细时间测量（FTM）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_FTM_ENABLE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_FTM_ENABLE)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_GCMP_SUPPORT"></a>

## 188.66 `CONFIG_ESP32_WIFI_GCMP_SUPPORT`

**提示（Prompt）**：GCMP 密码套件（Cipher）支持

**说明（Help）**

在 Espressif 认证客户端（Supplicant）中启用 GCMP 密码套件支持。WPA3 企业模式（WPA3-Enterprise）需要此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_ENTERPRISE && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ESP32_WIFI_SUITE_B
CONFIG_ESP32_WIFI_SUITE_B_192
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:779`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L779)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → WPA2/WPA3 企业模式（Enterprise）站点支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP32_WIFI_SUITE_B`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_SUITE_B)、[`CONFIG_ESP32_WIFI_SUITE_B_192`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_SUITE_B_192)。

<a id="CONFIG_ESP32_WIFI_GMAC_SUPPORT"></a>

## 188.67 `CONFIG_ESP32_WIFI_GMAC_SUPPORT`

**提示（Prompt）**：GMAC 密码套件（Cipher）支持

**说明（Help）**

在 Espressif 认证客户端（Supplicant）中启用 GMAC 支持。WPA3 企业模式 Suite-B（WPA3-Enterprise Suite-B）需要此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_ENTERPRISE && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ESP32_WIFI_SUITE_B
CONFIG_ESP32_WIFI_SUITE_B_192
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:787`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L787)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → WPA2/WPA3 企业模式（Enterprise）站点支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP32_WIFI_SUITE_B`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_SUITE_B)、[`CONFIG_ESP32_WIFI_SUITE_B_192`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_SUITE_B_192)。

<a id="CONFIG_ESP32_WIFI_IRAM_OPT"></a>

## 188.68 `CONFIG_ESP32_WIFI_IRAM_OPT`

**提示（Prompt）**：Wi-Fi 指令 RAM（IRAM）速度优化

**说明（Help）**

将频繁调用的 Wi-Fi 库函数放入指令 RAM（IRAM）。禁用此选项可节省超过 10 Kbytes 的 IRAM，但会降低 Wi-Fi 吞吐量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:309`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L309)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_LOW_RSSI_THRESHOLD"></a>

## 188.69 `CONFIG_ESP32_WIFI_LOW_RSSI_THRESHOLD`

**提示（Prompt）**：触发信号变化事件的信号强度（dBm）

**说明（Help）**

已连接接入点（AP）的信号强度阈值，单位为 dBm；低于此值时产生信号变化事件（Signal Change Event）。接近 -30 的值会在链路仍然良好时报告事件，导致大量事件产生。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_SIGNAL_CHANGE_EVENT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
-70
```

**取值范围（Ranges）**

```text
[-99, -30]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:929`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L929)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → AP 信号减弱时报告信号变化事件

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_SIGNAL_CHANGE_EVENT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_SIGNAL_CHANGE_EVENT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_LOW_RSSI_THRESHOLD_STEP"></a>

## 188.70 `CONFIG_ESP32_WIFI_LOW_RSSI_THRESHOLD_STEP`

**提示（Prompt）**：每次事件后降低阈值的幅度（dB）

**说明（Help）**

Wi-Fi 库只报告一次越过阈值的情况，之后需要重新启用监测（Arm）。如果链路持续较弱，仍以相同阈值重新启用，会重复产生相同事件，因此每次都将阈值降低此处指定的幅度。库仅报告信号变差的情况，所以当当前监测阈值低于配置值时，驱动会采样已连接的接入点，并在信号恢复后将阈值复原。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_SIGNAL_CHANGE_EVENT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 20]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:939`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L939)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → AP 信号减弱时报告信号变化事件

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_SIGNAL_CHANGE_EVENT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_SIGNAL_CHANGE_EVENT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_MAX_THREAD_PRIORITY"></a>

## 188.71 `CONFIG_ESP32_WIFI_MAX_THREAD_PRIORITY`

**提示（Prompt）**：工作队列线程最大优先级

**说明（Help）**

用于处理驱动工作队列条目的线程的最大优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:346`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L346)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO"></a>

## 188.72 `CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`

**提示（Prompt）**：使用 Mbed TLS 密码学 API（Crypto APIs）

**说明（Help）**

使用支持硬件加速（Hardware Acceleration）的 Mbed TLS 密码学 API（Crypto APIs）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_DECLARE_PRIVATE_IDENTIFIERS
CONFIG_MBEDTLS_MD_C
CONFIG_MBEDTLS_PK_PARSE_C
CONFIG_MBEDTLS_PK_WRITE_C
CONFIG_MBEDTLS_PKCS5_C
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_ALG_CBC_NO_PADDING
CONFIG_PSA_WANT_ALG_CMAC
CONFIG_PSA_WANT_ALG_CTR
CONFIG_PSA_WANT_ALG_ECB_NO_PADDING
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ALG_ECDSA
CONFIG_PSA_WANT_ALG_HMAC
CONFIG_PSA_WANT_ALG_PBKDF2_HMAC
CONFIG_PSA_WANT_ALG_SHA_1
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_ECC_SECP_R1_256
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY
```

**被选择（Selected by）**

```text
CONFIG_ESP32_WIFI_ENTERPRISE
CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:725`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L725)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_MBEDTLS_DECLARE_PRIVATE_IDENTIFIERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_DECLARE_PRIVATE_IDENTIFIERS)、[`CONFIG_MBEDTLS_MD_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_MD_C)、[`CONFIG_MBEDTLS_PK_PARSE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PK_PARSE_C)、[`CONFIG_MBEDTLS_PK_WRITE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PK_WRITE_C)、[`CONFIG_MBEDTLS_PKCS5_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PKCS5_C)、[`CONFIG_PSA_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_ALG_CBC_NO_PADDING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_CBC_NO_PADDING)、[`CONFIG_PSA_WANT_ALG_CMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_CMAC)、[`CONFIG_PSA_WANT_ALG_CTR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_CTR)、[`CONFIG_PSA_WANT_ALG_ECB_NO_PADDING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_ECB_NO_PADDING)、[`CONFIG_PSA_WANT_ALG_ECDH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_ECDSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_ECDSA)、[`CONFIG_PSA_WANT_ALG_HMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_HMAC)、[`CONFIG_PSA_WANT_ALG_PBKDF2_HMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_PBKDF2_HMAC)、[`CONFIG_PSA_WANT_ALG_SHA_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA_1)、[`CONFIG_PSA_WANT_ALG_SHA_256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ECC_SECP_R1_256)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY)、[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)、[`CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC`。

<a id="CONFIG_ESP32_WIFI_MBO_SUPPORT"></a>

## 188.73 `CONFIG_ESP32_WIFI_MBO_SUPPORT`

**提示（Prompt）**：多频段操作（Multi Band Operation，MBO）

**说明（Help）**

启用 Wi-Fi 灵活多频段（Agile Multiband，MBO）支持。MBO 基于 802.11k 和 802.11v，因此必须同时启用两者；扫描缓存（Scan Cache）也会随之启用。此处尚不能报告非首选信道（Non-preferred Channels），因为该功能依赖的扫描入口在 Zephyr 移植中只是桩实现（Stub）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_RRM_SUPPORT && CONFIG_ESP32_WIFI_WNM_SUPPORT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_ESP32_WIFI_SCAN_CACHE
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:874`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L874)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_RRM_SUPPORT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_RRM_SUPPORT)、[`CONFIG_ESP32_WIFI_WNM_SUPPORT`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_WNM_SUPPORT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP32_WIFI_SCAN_CACHE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_SCAN_CACHE)。

<a id="CONFIG_ESP32_WIFI_MGMT_RX_BUFFER"></a>

## 188.74 `CONFIG_ESP32_WIFI_MGMT_RX_BUFFER`

**提示（Prompt）**：Wi-Fi 接收管理帧（RX MGMT）缓冲区类型

**说明（Help）**

选择 Wi-Fi 接收管理帧（RX MGMT）缓冲区类型：

- 静态（Static）：Wi-Fi 初始化时分配，反初始化时释放。每个静态 RX MGMT 缓冲区大小固定，约为 500 字节。
- 动态（Dynamic）：收到管理数据帧时按需分配每个缓冲区；Wi-Fi 驱动处理完该管理帧后释放缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_ESP32_WIFI_STATIC_RX_MGMT_BUFFER
```

**可选项（Choices）**

```text
CONFIG_ESP32_WIFI_STATIC_RX_MGMT_BUFFER
CONFIG_ESP32_WIFI_DYNAMIC_RX_MGMT_BUFFER
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:210`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L210)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP32_WIFI_STATIC_RX_MGMT_BUFFER`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_STATIC_RX_MGMT_BUFFER)、[`CONFIG_ESP32_WIFI_DYNAMIC_RX_MGMT_BUFFER`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_DYNAMIC_RX_MGMT_BUFFER)。

<a id="CONFIG_ESP32_WIFI_MGMT_SBUF_NUM"></a>

## 188.75 `CONFIG_ESP32_WIFI_MGMT_SBUF_NUM`

**提示（Prompt）**：Wi-Fi 管理短缓冲区（Management Short Buffer）数量

**说明（Help）**

设置 Wi-Fi 管理短缓冲区（Management Short Buffer）的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[6, 32]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:302`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L302)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_NET_ALLOC_SPIRAM"></a>

## 188.76 `CONFIG_ESP32_WIFI_NET_ALLOC_SPIRAM`

**提示（Prompt）**：在 SPI RAM（SPIRAM）中分配 Wi-Fi 和网络协议栈内存

**说明（Help）**

在 SPI RAM（SPIRAM）中分配 Wi-Fi 和网络（NET）协议栈内存，为应用栈释放更多可用 RAM 空间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_SPIRAM && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_ESP_SPIRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_SPIRAM)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_ROAM_TIMEOUT_MS"></a>

## 188.77 `CONFIG_ESP32_WIFI_ROAM_TIMEOUT_MS`

**提示（Prompt）**：允许基本服务集（BSS）转换完成的时间，单位为毫秒

**说明（Help）**

基本服务集转换（BSS Transition）期间，站点在关联到目标接入点之前没有可用 AP；如果始终未关联成功，Wi-Fi 库不会报告结果。等待此处指定的时间后放弃，并报告链路丢失，避免停滞的转换使接口仍显示为启用状态，实际却没有连接。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_WNM_SUPPORT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
10000
```

**取值范围（Ranges）**

```text
[1000, 60000]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:899`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L899)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_WNM_SUPPORT`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_WNM_SUPPORT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_RRM_SUPPORT"></a>

## 188.78 `CONFIG_ESP32_WIFI_RRM_SUPPORT`

**提示（Prompt）**：802.11k 无线资源测量（Radio Resource Measurement）

**说明（Help）**

无线测量允许站点观测并报告无线环境。只实现对网络辅助漫游（Network-assisted Roaming）有用的测量：信标报告（Beacon Report）、链路测量（Link Measurement）和邻居报告（Neighbor Report）。启用后，站点在关联时声明无线资源测量（RRM）能力；AP 在回复邻居报告请求前会检查此能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_11KV_SUPPORT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:836`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L836)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → 802.11k 和 802.11v 支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_11KV_SUPPORT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_11KV_SUPPORT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_RSSI_RECOVER_INTERVAL_MS"></a>

## 188.79 `CONFIG_ESP32_WIFI_RSSI_RECOVER_INTERVAL_MS`

**提示（Prompt）**：链路较弱时的信号采样间隔，单位为毫秒

**说明（Help）**

当当前启用的监测阈值低于配置值、正在等待信号恢复时，对已连接接入点进行采样的间隔。Wi-Fi 库仅报告信号变差，因此必须轮询检测恢复。每次采样都需要调用 Wi-Fi 库；较短间隔可更早发现链路恢复，但会增加节能站点的唤醒次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_SIGNAL_CHANGE_EVENT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5000
```

**取值范围（Ranges）**

```text
[1000, 60000]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:952`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L952)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → AP 信号减弱时报告信号变化事件

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_SIGNAL_CHANGE_EVENT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_SIGNAL_CHANGE_EVENT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_RX_BA_WIN"></a>

## 188.80 `CONFIG_ESP32_WIFI_RX_BA_WIN`

**提示（Prompt）**：Wi-Fi A-MPDU 接收块确认（RX BA）窗口大小

**说明（Help）**

设置 Wi-Fi 块确认接收窗口（Block Ack RX Window）的大小。通常更大的值意味着更高吞吐量、更好兼容性，但也占用更多内存。除非有特殊原因，例如使用 iperf 测试最大 UDP 接收吞吐量，否则通常不应修改默认值。

在屏蔽箱（Shieldbox）内进行 iperf 测试时，推荐值为 9 至 12。如果使用伪静态 RAM（PSRAM），且 Wi-Fi 内存优先从 PSRAM 分配，则默认值和最小值都应为 16，以获得更好的吞吐量，以及与站点和 AP 的兼容性。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_AMPDU_RX_ENABLED && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[2, 32]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:281`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L281)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → Wi-Fi 聚合 MAC 协议数据单元接收（A-MPDU RX）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_AMPDU_RX_ENABLED`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_AMPDU_RX_ENABLED)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_RX_IRAM_OPT"></a>

## 188.81 `CONFIG_ESP32_WIFI_RX_IRAM_OPT`

**提示（Prompt）**：Wi-Fi 接收（RX）指令 RAM（IRAM）速度优化

**说明（Help）**

将频繁调用的 Wi-Fi 库接收（RX）函数放入指令 RAM（IRAM）。禁用此选项可节省超过 17 Kbytes 的 IRAM，但会降低 Wi-Fi 性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:324`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L324)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_RX_MGMT_BUF_NUM_DEF"></a>

## 188.82 `CONFIG_ESP32_WIFI_RX_MGMT_BUF_NUM_DEF`

**提示（Prompt）**：Wi-Fi 接收管理帧（RX MGMT）缓冲区最大数量

**说明（Help）**

设置 Wi-Fi `RX_MGMT` 缓冲区数量。动态和静态管理缓冲区使用相同的数量设置。为避免内存碎片（Memory Fragmentation），应优先将管理缓冲区类型设为静态。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L235)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_SCAN_CACHE"></a>

## 188.83 `CONFIG_ESP32_WIFI_SCAN_CACHE`

**提示（Prompt）**：在缓存中保留扫描结果（Scan Results）

**说明（Help）**

保留扫描结果，以便从缓存回复信标报告（Beacon Report）。未启用时，扫描结束后立即清除结果，每次报告都需要重新扫描。Zephyr 移植目前尚不能访问这些缓存结果，因此现阶段只为认证客户端（Supplicant）自身保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_RRM_SUPPORT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**被选择（Selected by）**

```text
CONFIG_ESP32_WIFI_MBO_SUPPORT
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:863`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L863)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_RRM_SUPPORT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_RRM_SUPPORT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP32_WIFI_MBO_SUPPORT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBO_SUPPORT)。

<a id="CONFIG_ESP32_WIFI_SIGNAL_CHANGE_EVENT"></a>

## 188.84 `CONFIG_ESP32_WIFI_SIGNAL_CHANGE_EVENT`

**提示（Prompt）**：AP 信号减弱时报告信号变化事件

**说明（Help）**

监测已连接接入点（AP）的接收信号强度指示（RSSI），低于配置阈值时产生 `NET_EVENT_WIFI_SIGNAL_CHANGE`。该事件仅用于报告，不会因此自动启动扫描、基本服务集转换查询（BSS Transition Query）或重新关联（Reassociation）。应用可据此决定是否调用 11k 和 11v 操作。

Wi-Fi 命令行（Shell）仅在启用 `WIFI_NM_WPA_SUPPLICANT_ROAMING` 时响应此事件并注册 `NET_REQUEST_WIFI_START_ROAMING`。该选项属于 wpa_supplicant 网络管理器，而当前这些选项排除了该管理器，因此应用需要自行提供事件处理程序。AP 通过 BSS 转换请求发起的转换与此事件相互独立，只要启用了无线网络管理（WNM）支持，就会执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESP32_WIFI_RRM_SUPPORT || CONFIG_ESP32_WIFI_WNM_SUPPORT) && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:911`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L911)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_RRM_SUPPORT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_RRM_SUPPORT)、[`CONFIG_ESP32_WIFI_WNM_SUPPORT`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_WNM_SUPPORT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_SKIP_DHCP_ON_ROAMING"></a>

## 188.85 `CONFIG_ESP32_WIFI_SKIP_DHCP_ON_ROAMING`

**提示（Prompt）**：漫游到另一个 AP 时保留 IP 配置

**说明（Help）**

基本服务集转换（BSS Transition）使站点在同一网络的 AP 之间移动。启用时，接口在切换期间保持启用，并保留地址；两个 AP 位于同一子网时，即二层漫游（L2 Roaming），这样处理是正确的。如果 AP 位于不同子网，应禁用此选项，使漫游被报告为断开连接，并重新请求地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_WNM_SUPPORT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:886`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L886)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_WNM_SUPPORT`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_WNM_SUPPORT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT"></a>

## 188.86 `CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT`

**提示（Prompt）**：信标丢失时的 Wi-Fi 睡眠优化

**说明（Help）**

启用信标丢失（Beacon Loss）时的 Wi-Fi 睡眠优化，在 Wi-Fi 模块检测到信标丢失后立即进入睡眠模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MAC_BB_PD && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:682`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L682)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_MAC_BB_PD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAC_BB_PD)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_SLP_BEACON_LOST_THRESHOLD"></a>

## 188.87 `CONFIG_ESP32_WIFI_SLP_BEACON_LOST_THRESHOLD`

**提示（Prompt）**：允许连续丢失信标的最大数量

**说明（Help）**

允许连续丢失信标（Beacon）的最大数量。连续丢失数量大于指定阈值时，Wi-Fi 保持接收（RX）状态。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 8]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:698`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L698)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → 信标丢失时的 Wi-Fi 睡眠优化

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_SLP_BEACON_LOST_TIMEOUT"></a>

## 188.88 `CONFIG_ESP32_WIFI_SLP_BEACON_LOST_TIMEOUT`

**提示（Prompt）**：信标丢失超时（Beacon Loss Timeout）

**说明（Help）**

信标丢失时，在关闭射频物理层（RF PHY）之前等待的超时时间。单位为 1024 微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[5, 100]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:689`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L689)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → 信标丢失时的 Wi-Fi 睡眠优化

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_SLP_DEFAULT_MAX_ACTIVE_TIME"></a>

## 188.89 `CONFIG_ESP32_WIFI_SLP_DEFAULT_MAX_ACTIVE_TIME`

**提示（Prompt）**：最大保活时间（Maximum Keep Alive Time）

**说明（Help）**

仅适用于 `WIFI_PS_MIN_MODEM` 或 `WIFI_PS_MAX_MODEM` 下的站点。如果在 `ESP_WIFI_SLP_DEFAULT_MAX_ACTIVE_TIME` 内没有发送任何包，则发送一个空数据包（Null Data Packet），以维持与 AP 的连接。单位为秒。

译注：此处标识符按原文保留为 `ESP_WIFI_SLP_DEFAULT_MAX_ACTIVE_TIME`，未根据标题擅自更名。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[10, 60]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:458`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L458)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_SLP_DEFAULT_MIN_ACTIVE_TIME"></a>

## 188.90 `CONFIG_ESP32_WIFI_SLP_DEFAULT_MIN_ACTIVE_TIME`

**提示（Prompt）**：最短活动时间（Minimum Active Time）

**说明（Help）**

仅适用于 `WIFI_PS_MIN_MODEM` 或 `WIFI_PS_MAX_MODEM` 下的站点。站点进入活动状态后，至少工作 `ESP_WIFI_SLP_DEFAULT_MIN_ACTIVE_TIME`。如果期间接收或发送了数据包，将重新计时；即使时间已到，只要站点仍有包待接收或发送，也会重新计时。单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
50
```

**取值范围（Ranges）**

```text
[8, 60]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:448`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L448)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_SLP_DEFAULT_WAIT_BROADCAST_DATA_TIME"></a>

## 188.91 `CONFIG_ESP32_WIFI_SLP_DEFAULT_WAIT_BROADCAST_DATA_TIME`

**提示（Prompt）**：等待广播数据的最短时间

**说明（Help）**

仅适用于 `WIFI_PS_MIN_MODEM` 或 `WIFI_PS_MAX_MODEM` 下的站点。站点通过信标得知 AP 将发送广播包时，会先等待 `ESP_WIFI_SLP_DEFAULT_WAIT_BROADCAST_DATA_TIME`，再进入睡眠流程。如果收到设置了更多数据位（More Data Bit）的广播包，将重新计时。单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
15
```

**取值范围（Ranges）**

```text
[10, 30]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:467`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L467)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_SLP_IRAM_OPT"></a>

## 188.92 `CONFIG_ESP32_WIFI_SLP_IRAM_OPT`

**提示（Prompt）**：Wi-Fi 睡眠（SLP）指令 RAM（IRAM）速度优化

**说明（Help）**

将 Wi-Fi 库中被调用的目标信标传输时间（TBTT）处理函数和信标接收函数放入指令 RAM（IRAM）。部分函数既可通过 `ESP32_WIFI_IRAM_OPT` 和 `ESP32_WIFI_RX_IRAM_OPT` 放入 IRAM，也可通过此选项放入。

- 已启用 `ESP32_WIFI_IRAM_OPT` 时，额外使用 7.3 KB IRAM。
- 仅启用 `ESP32_WIFI_RX_IRAM_OPT` 时，额外使用 1.3 KB。
- 两者均未启用时，额外使用 7.4 KB。

此选项可降低 Wi-Fi 节能模式（Power-save Mode）的平均电流。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_ESP32_WIFI_HE_SUPPORT && !CONFIG_BUILD_ONLY_NO_BLOBS
```

**主动选择（Selects）**

```text
CONFIG_SOC_ESP32_PM_SLP_DEFAULT_PARAMS_OPT if CONFIG_PM && CONFIG_TICKLESS_KERNEL
CONFIG_ESP32_PM_SLP_IRAM_OPT if CONFIG_PM && CONFIG_TICKLESS_KERNEL
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:331`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L331)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_SOC_ESP32_WIFI_HE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_WIFI_HE_SUPPORT)、[`CONFIG_BUILD_ONLY_NO_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_ONLY_NO_BLOBS)、[`CONFIG_SOC_ESP32_PM_SLP_DEFAULT_PARAMS_OPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_PM_SLP_DEFAULT_PARAMS_OPT)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_ESP32_PM_SLP_IRAM_OPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP32_PM_SLP_IRAM_OPT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32_WIFI_HE_SUPPORT`、`CONFIG_SOC_ESP32_PM_SLP_DEFAULT_PARAMS_OPT`。

<a id="CONFIG_ESP32_WIFI_SLP_PHY_OFF_DELTA_TIMEOUT_TIME"></a>

## 188.93 `CONFIG_ESP32_WIFI_SLP_PHY_OFF_DELTA_TIMEOUT_TIME`

**提示（Prompt）**：关闭射频物理层（RF PHY）的超时增量

**说明（Help）**

关闭射频物理层（RF PHY）的超时增量。信标丢失时，下一次关闭 RF PHY 的时刻将延后此配置指定的时长。单位为 1024 微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT && CONFIG_SOC_ESP32_WIFI_SUPPORT_VARIABLE_BEACON_WINDOW && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 8]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:716`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L716)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → 信标丢失时的 Wi-Fi 睡眠优化

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT)、[`CONFIG_SOC_ESP32_WIFI_SUPPORT_VARIABLE_BEACON_WINDOW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_WIFI_SUPPORT_VARIABLE_BEACON_WINDOW)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32_WIFI_SUPPORT_VARIABLE_BEACON_WINDOW`。

<a id="CONFIG_ESP32_WIFI_SLP_PHY_ON_DELTA_EARLY_TIME"></a>

## 188.94 `CONFIG_ESP32_WIFI_SLP_PHY_ON_DELTA_EARLY_TIME`

**提示（Prompt）**：开启射频物理层（RF PHY）的提前时间增量

**说明（Help）**

开启射频物理层（RF PHY）的提前时间增量。信标丢失时，下一次开启 RF PHY 的时刻将提前此配置指定的时长。单位为 32 微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT && CONFIG_SOC_ESP32_WIFI_SUPPORT_VARIABLE_BEACON_WINDOW && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 100]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:707`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L707)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → 信标丢失时的 Wi-Fi 睡眠优化

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_SLP_BEACON_LOST_OPT)、[`CONFIG_SOC_ESP32_WIFI_SUPPORT_VARIABLE_BEACON_WINDOW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_WIFI_SUPPORT_VARIABLE_BEACON_WINDOW)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32_WIFI_SUPPORT_VARIABLE_BEACON_WINDOW`。

<a id="CONFIG_ESP32_WIFI_SOFTAP_SAE_SUPPORT"></a>

## 188.95 `CONFIG_ESP32_WIFI_SOFTAP_SAE_SUPPORT`

**提示（Prompt）**：WPA3-SAE 软件接入点（SoftAP）支持

**说明（Help）**

在软件接入点（SoftAP）模式下启用 WPA3-SAE 认证。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE && CONFIG_ESP32_WIFI_SOFTAP_SUPPORT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:1014`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L1014)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → WPA3 个人模式（WPA3-Personal）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE)、[`CONFIG_ESP32_WIFI_SOFTAP_SUPPORT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_SOFTAP_SUPPORT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_SOFTAP_SUPPORT"></a>

## 188.96 `CONFIG_ESP32_WIFI_SOFTAP_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，用于在 WPA 认证客户端（Supplicant）和射频（RF）库中启用 Wi-Fi 软件接入点（SoftAP）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_WIFI_ESP32_MESH
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:495`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L495)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_WIFI_ESP32_MESH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32_MESH)。

<a id="CONFIG_ESP32_WIFI_STATIC_RX_BUFFER_NUM"></a>

## 188.97 `CONFIG_ESP32_WIFI_STATIC_RX_BUFFER_NUM`

**提示（Prompt）**：Wi-Fi 静态接收（Static RX）缓冲区最大数量

**说明（Help）**

设置 Wi-Fi 静态接收（RX）缓冲区数量。每个缓冲区约占 1.6 KB RAM。静态接收缓冲区在调用 `esp_wifi_init` 时分配，直到调用 `esp_wifi_deinit` 才释放。它们始终从系统堆（System Heap）分配，即使选择了 `ESP_WIFI_HEAP_SPIRAM` 也是如此。

Wi-Fi 硬件使用这些缓冲区接收所有 802.11 帧。增加数量可能提高吞吐量，但会增大内存占用。启用 `ESP32_WIFI_AMPDU_RX_ENABLED` 时，建议此值大于或等于 `ESP32_WIFI_RX_BA_WIN`，以获得更好的吞吐量，以及与站点和 AP 的兼容性。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[2, 25]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_STATIC_RX_MGMT_BUFFER"></a>

## 188.98 `CONFIG_ESP32_WIFI_STATIC_RX_MGMT_BUFFER`

**提示（Prompt）**：静态（Static）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_WIFI_MGMT_RX_BUFFER>
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → Wi-Fi 接收管理帧（RX MGMT）缓冲区类型

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_MGMT_RX_BUFFER`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MGMT_RX_BUFFER)。

<a id="CONFIG_ESP32_WIFI_STATIC_TX_BUFFER"></a>

## 188.99 `CONFIG_ESP32_WIFI_STATIC_TX_BUFFER`

**提示（Prompt）**：静态（Static）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_WIFI_TX_BUFFER>
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → Wi-Fi 发送（TX）缓冲区类型

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_TX_BUFFER`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_TX_BUFFER)。

<a id="CONFIG_ESP32_WIFI_STATIC_TX_BUFFER_NUM"></a>

## 188.100 `CONFIG_ESP32_WIFI_STATIC_TX_BUFFER_NUM`

**提示（Prompt）**：Wi-Fi 静态发送（Static TX）缓冲区最大数量

**说明（Help）**

设置 Wi-Fi 静态发送（TX）缓冲区数量。每个缓冲区约占 1.6 KB RAM。原文接着说明，静态接收（RX）缓冲区在调用 `esp_wifi_init()` 时分配，直到调用 `esp_wifi_deinit()` 才释放。对于来自上层 TCP/IP 协议栈的每个发送数据帧，Wi-Fi 驱动都会将其复制到发送缓冲区。某些应用，尤其 UDP 应用，可能以高于 Wi-Fi 层发送速度的速率提交帧，导致发送缓冲区耗尽。

译注：本项标题和主要说明讨论 TX 缓冲区，但分配／释放句使用了 RX；此处保留原文差异。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_STATIC_TX_BUFFER && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_STATIC_TX_BUFFER`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_STATIC_TX_BUFFER)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<!-- kconfig-navigation -->

[上一章](P187_drivers_watchdog_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P189_drivers_wifi_配置项参考_2.md)
