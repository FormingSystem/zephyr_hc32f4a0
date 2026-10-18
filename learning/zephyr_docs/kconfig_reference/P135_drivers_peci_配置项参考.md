---
id: learning.zephyr-docs.kconfig-reference.page-135
title: "`drivers/peci`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第135章\_`drivers/peci`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/peci` 的 8 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ESPI_PECI"></a>

## 135.1 `CONFIG_ESPI_PECI`

**提示（Prompt）**：支持通过 eSPI 传输 PECI

**说明（Help）**

嵌入式控制器（EC）支持使用带外（OOB）消息，通过 eSPI 传输平台环境控制接口（PECI）数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ESPI_PECI_ENABLED && CONFIG_ESPI_OOB_CHANNEL && CONFIG_PECI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/peci/Kconfig.espi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/peci/Kconfig.espi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_OOB_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_OOB_CHANNEL)、[`CONFIG_PECI`](P135_drivers_peci_配置项参考.md#CONFIG_PECI)。

<a id="CONFIG_ESPI_PECI_SHELL"></a>

## 135.2 `CONFIG_ESPI_PECI_SHELL`

**提示（Prompt）**：支持 PECI over eSPI 命令行（Shell）

**说明（Help）**

EC 支持通过 eSPI 使用 PECI 的控制台命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PECI && CONFIG_PECI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/peci/Kconfig.espi:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/peci/Kconfig.espi#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动 → 支持通过 eSPI 传输 PECI

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PECI`](P135_drivers_peci_配置项参考.md#CONFIG_ESPI_PECI)、[`CONFIG_PECI`](P135_drivers_peci_配置项参考.md#CONFIG_PECI)。

<a id="CONFIG_PECI"></a>

## 135.3 `CONFIG_PECI`

**提示（Prompt）**：平台环境控制接口（Platform Environment Control Interface，PECI）驱动

**说明（Help）**

在系统配置中纳入 PECI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/peci/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/peci/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_PECI_INIT_PRIORITY"></a>

## 135.4 `CONFIG_PECI_INIT_PRIORITY`

**提示（Prompt）**：PECI 驱动初始化优先级

**说明（Help）**

PECI 设备驱动的初始化优先级。原文说明，目前没有关键组件依赖此优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PECI
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`drivers/peci/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/peci/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动

**配置项引用（Symbol References）**：[`CONFIG_PECI`](P135_drivers_peci_配置项参考.md#CONFIG_PECI)。

<a id="CONFIG_PECI_INTERRUPT_DRIVEN"></a>

## 135.5 `CONFIG_PECI_INTERRUPT_DRIVEN`

**提示（Prompt）**：PECI 驱动中断支持（Interrupt Support）

**说明（Help）**

由各 PECI 驱动启用此选项，表示驱动及硬件支持中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PECI
```

**被选择（Selected by）**

```text
CONFIG_PECI_ITE_IT8XXX2
CONFIG_PECI_NPCX
```

**定义位置（Location）**：[`drivers/peci/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/peci/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动

**配置项引用（Symbol References）**：[`CONFIG_PECI`](P135_drivers_peci_配置项参考.md#CONFIG_PECI)、[`CONFIG_PECI_ITE_IT8XXX2`](P135_drivers_peci_配置项参考.md#CONFIG_PECI_ITE_IT8XXX2)、[`CONFIG_PECI_NPCX`](P135_drivers_peci_配置项参考.md#CONFIG_PECI_NPCX)。

<a id="CONFIG_PECI_ITE_IT8XXX2"></a>

## 135.6 `CONFIG_PECI_ITE_IT8XXX2`

**提示（Prompt）**：ITE IT8XXX2 PECI 驱动

**说明（Help）**

启用 ITE IT8XXX2 PECI IO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_PECI_ENABLED && CONFIG_PECI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PECI_INTERRUPT_DRIVEN
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/peci/Kconfig.it8xxx2:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/peci/Kconfig.it8xxx2#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动

**配置项引用（Symbol References）**：[`CONFIG_PECI`](P135_drivers_peci_配置项参考.md#CONFIG_PECI)、[`CONFIG_PECI_INTERRUPT_DRIVEN`](P135_drivers_peci_配置项参考.md#CONFIG_PECI_INTERRUPT_DRIVEN)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PECI_NPCX"></a>

## 135.7 `CONFIG_PECI_NPCX`

**提示（Prompt）**：NPCX PECI 驱动

**说明（Help）**

启用 NPCX PECI IO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_PECI_ENABLED && CONFIG_PECI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PECI_INTERRUPT_DRIVEN
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/peci/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/peci/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动

**配置项引用（Symbol References）**：[`CONFIG_PECI`](P135_drivers_peci_配置项参考.md#CONFIG_PECI)、[`CONFIG_PECI_INTERRUPT_DRIVEN`](P135_drivers_peci_配置项参考.md#CONFIG_PECI_INTERRUPT_DRIVEN)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PECI_XEC"></a>

## 135.8 `CONFIG_PECI_XEC`

**提示（Prompt）**：XEC Microchip PECI 驱动

**说明（Help）**

启用 Microchip XEC PECI IO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_PECI_ENABLED && CONFIG_PECI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/peci/Kconfig.xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/peci/Kconfig.xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动

**配置项引用（Symbol References）**：[`CONFIG_PECI`](P135_drivers_peci_配置项参考.md#CONFIG_PECI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<!-- kconfig-navigation -->

[上一章](P134_drivers_pcie_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P136_drivers_pinctrl_配置项参考.md)
