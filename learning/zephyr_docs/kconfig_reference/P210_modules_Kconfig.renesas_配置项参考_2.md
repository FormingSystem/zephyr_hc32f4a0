---
id: learning.zephyr-docs.kconfig-reference.page-210
title: "`modules/Kconfig.renesas`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第210章\_`modules/Kconfig.renesas`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.renesas` 的 5 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_USE_RZ_FSP_SCIF_UART"></a>

## 210.1 `CONFIG_USE_RZ_FSP_SCIF_UART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP SCIF UART 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_UART_RENESAS_RZ_SCIF
```

**定义位置（Location）**：[`modules/Kconfig.renesas:377`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L377)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_UART_RENESAS_RZ_SCIF`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RENESAS_RZ_SCIF)。

<a id="CONFIG_USE_RZ_FSP_SCI_UART"></a>

## 210.2 `CONFIG_USE_RZ_FSP_SCI_UART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP SCI UART 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_UART_RENESAS_RZ_SCI
CONFIG_UART_RENESAS_RZ_SCI_B
```

**定义位置（Location）**：[`modules/Kconfig.renesas:442`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L442)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_UART_RENESAS_RZ_SCI`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RENESAS_RZ_SCI)、[`CONFIG_UART_RENESAS_RZ_SCI_B`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RENESAS_RZ_SCI_B)。

<a id="CONFIG_USE_RZ_FSP_SPI"></a>

## 210.3 `CONFIG_USE_RZ_FSP_SPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP 串行外设接口（SPI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_SPI_RENESAS_RZ
```

**定义位置（Location）**：[`modules/Kconfig.renesas:457`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L457)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_SPI_RENESAS_RZ`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ)。

<a id="CONFIG_USE_RZ_FSP_SPI_B"></a>

## 210.4 `CONFIG_USE_RZ_FSP_SPI_B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP SPI B 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_SPI_RENESAS_RZ_SPI_B
```

**定义位置（Location）**：[`modules/Kconfig.renesas:462`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L462)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_SPI_RENESAS_RZ_SPI_B`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_SPI_B)。

<a id="CONFIG_USE_RZ_FSP_WDT"></a>

## 210.5 `CONFIG_USE_RZ_FSP_WDT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP 看门狗定时器（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_WDT_RENESAS_RZ
```

**定义位置（Location）**：[`modules/Kconfig.renesas:467`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L467)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_WDT_RENESAS_RZ`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RENESAS_RZ)。

<!-- kconfig-navigation -->

[上一章](P209_modules_Kconfig.renesas_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P211_modules_Kconfig.simplelink_配置项参考.md)
