---
id: learning.zephyr-docs.kconfig-reference.page-245
title: "`modules/nrf_wifi`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第245章\_`modules/nrf_wifi`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/nrf_wifi` 的 8 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NRF70_BUSLIB"></a>

## 245.1 `CONFIG_NRF70_BUSLIB`

**提示（Prompt）**：NRF70 总线库（NRF70 Bus Library）

**说明（Help）**

为 nRF7002 Wi-Fi 扩展板（shield）启用 NRF70 总线库（Bus Library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_WIFI_NRF70
```

**定义位置（Location）**：[`modules/nrf_wifi/bus/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nrf_wifi/bus/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NRF70)。

<a id="CONFIG_NRF70_IOVDD_REGULATOR"></a>

## 245.2 `CONFIG_NRF70_IOVDD_REGULATOR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当 IOVDD 由稳压器（regulator）而非专用 GPIO 供电时选择此项，以便构建驱动调用的稳压器 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_BUSLIB
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_REGULATOR
```

**定义位置（Location）**：[`modules/nrf_wifi/bus/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nrf_wifi/bus/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录） → NRF70 总线库（NRF70 Bus Library）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_BUSLIB`](P245_modules_nrf_wifi_配置项参考.md#CONFIG_NRF70_BUSLIB)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_NRF70_LOG_VERBOSE"></a>

## 245.3 `CONFIG_NRF70_LOG_VERBOSE`

原库同名定义共 2 条；本项为数据库第 13647 条记录，各定义分别保留。

**提示（Prompt）**：控制日志信息的详细程度（Verbosity）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_BUSLIB
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/nrf_wifi/bus/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nrf_wifi/bus/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录） → NRF70 总线库（NRF70 Bus Library）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_BUSLIB`](P245_modules_nrf_wifi_配置项参考.md#CONFIG_NRF70_BUSLIB)。

<a id="CONFIG_NRF70_SPI_PM_CLAIM_WHILE_ACTIVE"></a>

## 245.4 `CONFIG_NRF70_SPI_PM_CLAIM_WHILE_ACTIVE`

**提示（Prompt）**：nRF70 通电期间保持 SPI 总线处于活动状态（ACTIVE）

**说明（Help）**

启用设备运行时电源管理（PM device runtime）时，每次总线事务都请求并释放 SPI 总线，会降低数据吞吐量。启用此选项可在接口通电期间保持总线处于活动状态（active state）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE_RUNTIME && CONFIG_NRF70_ON_SPI && CONFIG_NRF70_BUSLIB
```

**定义位置（Location）**：[`modules/nrf_wifi/bus/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nrf_wifi/bus/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录） → NRF70 总线库（NRF70 Bus Library）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_NRF70_ON_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF70_ON_SPI)、[`CONFIG_NRF70_BUSLIB`](P245_modules_nrf_wifi_配置项参考.md#CONFIG_NRF70_BUSLIB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRF70_ON_SPI`。

<a id="CONFIG_NRF70_SUPPLY"></a>

## 245.5 `CONFIG_NRF70_SUPPLY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当此驱动以任一种方式开关 nRF70 供电电源轨（supply rail）时选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_BUSLIB
```

**默认值（Defaults）**

```text
CONFIG_NRF70_SUPPLY_GPIO || CONFIG_NRF70_VIN_SUPPLY
```

**定义位置（Location）**：[`modules/nrf_wifi/bus/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nrf_wifi/bus/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录） → NRF70 总线库（NRF70 Bus Library）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_BUSLIB`](P245_modules_nrf_wifi_配置项参考.md#CONFIG_NRF70_BUSLIB)、[`CONFIG_NRF70_SUPPLY_GPIO`](P245_modules_nrf_wifi_配置项参考.md#CONFIG_NRF70_SUPPLY_GPIO)、[`CONFIG_NRF70_VIN_SUPPLY`](P245_modules_nrf_wifi_配置项参考.md#CONFIG_NRF70_VIN_SUPPLY)。

<a id="CONFIG_NRF70_SUPPLY_GPIO"></a>

## 245.6 `CONFIG_NRF70_SUPPLY_GPIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当 nRF70 供电电源轨（supply rail）通过 GPIO 开关时选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_BUSLIB
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`modules/nrf_wifi/bus/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nrf_wifi/bus/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录） → NRF70 总线库（NRF70 Bus Library）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_BUSLIB`](P245_modules_nrf_wifi_配置项参考.md#CONFIG_NRF70_BUSLIB)。

<a id="CONFIG_NRF70_VIN_SUPPLY"></a>

## 245.7 `CONFIG_NRF70_VIN_SUPPLY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当 nRF70 供电电源轨（supply rail）由稳压器（regulator）供电时选择此项，以便构建驱动调用的稳压器 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_BUSLIB
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_REGULATOR
```

**定义位置（Location）**：[`modules/nrf_wifi/bus/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nrf_wifi/bus/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录） → NRF70 总线库（NRF70 Bus Library）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_BUSLIB`](P245_modules_nrf_wifi_配置项参考.md#CONFIG_NRF70_BUSLIB)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_ZVFS_OPEN_ADD_SIZE_NRF70_ENABLE_DUAL_VIF"></a>

## 245.8 `CONFIG_ZVFS_OPEN_ADD_SIZE_NRF70_ENABLE_DUAL_VIF`

**提示（Prompt）**：nrf wifi 驱动所需的套接字描述符数量（socket descriptors）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_ENABLE_DUAL_VIF
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`modules/nrf_wifi/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/nrf_wifi/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_ENABLE_DUAL_VIF`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_ENABLE_DUAL_VIF)。

<!-- kconfig-navigation -->

[上一章](P244_modules_nanopb_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P246_modules_openthread_配置项参考_1.md)
