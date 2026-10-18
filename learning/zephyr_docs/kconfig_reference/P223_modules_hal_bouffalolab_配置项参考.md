---
id: learning.zephyr-docs.kconfig-reference.page-223
title: "`modules/hal_bouffalolab`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第223章\_`modules/hal_bouffalolab`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/hal_bouffalolab` 的 8 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BFLB_AOS_SHIM"></a>

## 223.1 `CONFIG_BFLB_AOS_SHIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

BL808 片上低功耗蓝牙控制器二进制固件（BLE controller blob）的操作系统适配层（OS shim），实现 `aos_*`、`bl_irq_*` 和平台函数（platform functions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BT_BFLB_BL808
```

**定义位置（Location）**：[`modules/hal_bouffalolab/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_bouffalolab/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_bouffalolab（模块路径 `modules/hal/bouffalolab`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL808`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL808)。

<a id="CONFIG_BFLB_BL602_OS_SHIM"></a>

## 223.2 `CONFIG_BFLB_BL602_OS_SHIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将 `bl_ops_funcs` 操作系统抽象表（OS abstraction table）移植到 Zephyr。BL602 wifi4 二进制固件（firmware blob）通过该表使用所有实时操作系统原语（RTOS primitives），包括堆、互斥锁、信号量、任务、定时器、IRQ、消息队列和事件组。由 BL60x Wi-Fi 驱动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_WIFI_BFLB_WIFI4
```

**定义位置（Location）**：[`modules/hal_bouffalolab/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_bouffalolab/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_bouffalolab（模块路径 `modules/hal/bouffalolab`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB_WIFI4`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI4)。

<a id="CONFIG_BFLB_BTBLE_PORT_OS_SHIM"></a>

## 223.3 `CONFIG_BFLB_BTBLE_PORT_OS_SHIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`btblecontroller` 二进制固件（binary blob）的 Zephyr RTOS 移植，实现 BL702L／BL616 的 `btblecontroller_*` 操作系统抽象（OS abstraction）。由使用 `btblecontroller` API 的 SoC 专用低功耗蓝牙（BLE）驱动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BT_BFLB_BL70XL
CONFIG_BT_BFLB_BL61X
CONFIG_BT_BFLB_BL616CL
```

**定义位置（Location）**：[`modules/hal_bouffalolab/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_bouffalolab/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_bouffalolab（模块路径 `modules/hal/bouffalolab`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL70XL`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL70XL)、[`CONFIG_BT_BFLB_BL61X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL61X)、[`CONFIG_BT_BFLB_BL616CL`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL616CL)。

<a id="CONFIG_BFLB_BTBLE_TASK_PRIO"></a>

## 223.4 `CONFIG_BFLB_BTBLE_TASK_PRIO`

**提示（Prompt）**：低功耗蓝牙控制器任务（BLE controller task）优先级

**说明（Help）**

通过 FreeRTOS 适配层（shim）的 `uxTaskPriorityGet()` 函数，向 BLE 控制器二进制固件（controller blob）报告的优先级级别。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BFLB_FREERTOS_SHIM
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`modules/hal_bouffalolab/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_bouffalolab/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_bouffalolab（模块路径 `modules/hal/bouffalolab`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_FREERTOS_SHIM`](P223_modules_hal_bouffalolab_配置项参考.md#CONFIG_BFLB_FREERTOS_SHIM)。

<a id="CONFIG_BFLB_FREERTOS_SHIM"></a>

## 223.5 `CONFIG_BFLB_FREERTOS_SHIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

博流（Bouffalo Lab）低功耗蓝牙控制器二进制固件（BLE controller blobs）的 FreeRTOS 到 Zephyr 适配层（shim）。由需要它的 SoC 专用 BLE 驱动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BT_BFLB_BL60X
CONFIG_BT_BFLB_BL70X
```

**定义位置（Location）**：[`modules/hal_bouffalolab/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_bouffalolab/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_bouffalolab（模块路径 `modules/hal/bouffalolab`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL60X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL60X)、[`CONFIG_BT_BFLB_BL70X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL70X)。

<a id="CONFIG_BFLB_PHYRF"></a>

## 223.6 `CONFIG_BFLB_PHYRF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

链接正在构建的 SoC 的共享物理层／射频二进制库（PHY/RF binary blob），例如 BL61x 上的 `libbl616_phyrf.a`。由博流（Bouffalo Lab）BLE、Wi-Fi 和 IEEE 802.15.4 驱动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BT_BFLB_BL70X
CONFIG_BT_BFLB_BL70XL
CONFIG_BT_BFLB_BL61X
CONFIG_IEEE802154_BFLB
CONFIG_WIFI_BFLB
```

**定义位置（Location）**：[`modules/hal_bouffalolab/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_bouffalolab/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_bouffalolab（模块路径 `modules/hal/bouffalolab`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL70X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL70X)、[`CONFIG_BT_BFLB_BL70XL`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL70XL)、[`CONFIG_BT_BFLB_BL61X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL61X)、[`CONFIG_IEEE802154_BFLB`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_BFLB)、[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)。

<a id="CONFIG_BFLB_SHIM_HEAP_SIZE"></a>

## 223.7 `CONFIG_BFLB_SHIM_HEAP_SIZE`

**提示（Prompt）**：低功耗蓝牙适配层堆大小（BLE shim heap size）

**说明（Help）**

BLE 控制器适配层（shim layer）用于线程、栈和队列的专用内存池（dedicated memory pool）大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BFLB_FREERTOS_SHIM || CONFIG_BFLB_BTBLE_PORT_OS_SHIM || CONFIG_BFLB_AOS_SHIM
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`modules/hal_bouffalolab/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_bouffalolab/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_bouffalolab（模块路径 `modules/hal/bouffalolab`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_BFLB_FREERTOS_SHIM`](P223_modules_hal_bouffalolab_配置项参考.md#CONFIG_BFLB_FREERTOS_SHIM)、[`CONFIG_BFLB_BTBLE_PORT_OS_SHIM`](P223_modules_hal_bouffalolab_配置项参考.md#CONFIG_BFLB_BTBLE_PORT_OS_SHIM)、[`CONFIG_BFLB_AOS_SHIM`](P223_modules_hal_bouffalolab_配置项参考.md#CONFIG_BFLB_AOS_SHIM)。

<a id="CONFIG_BFLB_WL80211_SHIM"></a>

## 223.8 `CONFIG_BFLB_WL80211_SHIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Wi-Fi 二进制固件（blob）的 WL80211 认证客户端桥接（supplicant bridge）和 RTOS 移植适配层（port shim）。提供 MACSW 二进制固件所需的 `wl80211_supplicant_*` 入口和操作系统抽象（OS abstractions）。由 BL61x Wi-Fi 驱动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_WIFI_BFLB_WIFI6
```

**定义位置（Location）**：[`modules/hal_bouffalolab/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_bouffalolab/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_bouffalolab（模块路径 `modules/hal/bouffalolab`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB_WIFI6`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI6)。

<!-- kconfig-navigation -->

[上一章](P222_modules_hal_ambiq_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P224_modules_hal_ethos_u_配置项参考.md)
