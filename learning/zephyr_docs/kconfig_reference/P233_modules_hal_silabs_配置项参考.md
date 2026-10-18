---
id: learning.zephyr-docs.kconfig-reference.page-233
title: "`modules/hal_silabs`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第233章\_`modules/hal_silabs`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/hal_silabs` 的 58 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SILABS_GECKO_ADC"></a>

## 233.1 `CONFIG_SILABS_GECKO_ADC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用模数转换器（Analog to Digital Converter，ADC）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFM32PG12B
CONFIG_ADC_GECKO_ADC
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_SOC_SERIES_EFM32PG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG12B)、[`CONFIG_ADC_GECKO_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_GECKO_ADC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_BURTC"></a>

## 233.2 `CONFIG_SILABS_GECKO_BURTC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用备份实时时间计数器（Back-Up Real Time Counter，BURTC）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_CMU"></a>

## 233.3 `CONFIG_SILABS_GECKO_CMU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用时钟管理单元（Clock Management Unit，CMU）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFM32HG
CONFIG_SOC_SERIES_EFM32TG
CONFIG_SOC_SERIES_EFM32WG
CONFIG_SOC_SERIES_EFM32GG11B
CONFIG_SOC_SERIES_EFM32GG12B
CONFIG_SOC_SERIES_EFM32JG12B
CONFIG_SOC_SERIES_EFM32PG12B
CONFIG_SOC_SERIES_EFM32PG1B
CONFIG_SOC_SERIES_EFR32BG13P
CONFIG_SOC_SERIES_EFR32FG13P
CONFIG_SOC_SERIES_EFR32FG1P
CONFIG_SOC_SERIES_EFR32MG12P
CONFIG_SOC_SERIES_EFR32MG13P
CONFIG_COUNTER_GECKO_RTCC
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_SOC_SERIES_EFM32HG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32HG)、[`CONFIG_SOC_SERIES_EFM32TG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32TG)、[`CONFIG_SOC_SERIES_EFM32WG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32WG)、[`CONFIG_SOC_SERIES_EFM32GG11B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG11B)、[`CONFIG_SOC_SERIES_EFM32GG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG12B)、[`CONFIG_SOC_SERIES_EFM32JG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32JG12B)、[`CONFIG_SOC_SERIES_EFM32PG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG12B)、[`CONFIG_SOC_SERIES_EFM32PG1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG1B)、[`CONFIG_SOC_SERIES_EFR32BG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32BG13P)、[`CONFIG_SOC_SERIES_EFR32FG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG13P)、[`CONFIG_SOC_SERIES_EFR32FG1P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG1P)、[`CONFIG_SOC_SERIES_EFR32MG12P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG12P)、[`CONFIG_SOC_SERIES_EFR32MG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG13P)、[`CONFIG_COUNTER_GECKO_RTCC`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_GECKO_RTCC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_CORE"></a>

## 233.4 `CONFIG_SILABS_GECKO_CORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用核心中断处理（Core interrupt handling，CORE）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_CRYOTIMER"></a>

## 233.5 `CONFIG_SILABS_GECKO_CRYOTIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用超低能耗定时器／计数器（Ultra Low Energy Timer/Counter，CRYOTIMER）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_EMU"></a>

## 233.6 `CONFIG_SILABS_GECKO_EMU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用能量管理单元（Energy Management Unit，EMU）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_SILABS_GECKO_POWER_MANAGER
CONFIG_SILABS_GECKO_POWER_MANAGER
CONFIG_SOC_SERIES_EFM32GG11B
CONFIG_SOC_SERIES_EFM32GG12B
CONFIG_SOC_SERIES_EFM32JG12B
CONFIG_SOC_SERIES_EFM32PG12B
CONFIG_SOC_SERIES_EFM32PG1B
CONFIG_SOC_SERIES_EFR32BG13P
CONFIG_SOC_SERIES_EFR32MG12P
CONFIG_SOC_SERIES_EFR32MG13P
CONFIG_SILABS_GECKO_EMU_DCDC
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_SILABS_GECKO_POWER_MANAGER`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_GECKO_POWER_MANAGER)、[`CONFIG_SOC_SERIES_EFM32GG11B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG11B)、[`CONFIG_SOC_SERIES_EFM32GG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG12B)、[`CONFIG_SOC_SERIES_EFM32JG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32JG12B)、[`CONFIG_SOC_SERIES_EFM32PG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG12B)、[`CONFIG_SOC_SERIES_EFM32PG1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG1B)、[`CONFIG_SOC_SERIES_EFR32BG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32BG13P)、[`CONFIG_SOC_SERIES_EFR32MG12P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG12P)、[`CONFIG_SOC_SERIES_EFR32MG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG13P)、[`CONFIG_SILABS_GECKO_EMU_DCDC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_EMU_DCDC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_EUSART"></a>

## 233.7 `CONFIG_SILABS_GECKO_EUSART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用扩展通用同步／异步收发器（Extended Universal Synchronous Asynchronous Receiver/Transmitter，EUSART）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_GPIO"></a>

## 233.8 `CONFIG_SILABS_GECKO_GPIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用通用输入／输出（General Purpose Input/Output，GPIO）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFM32HG
CONFIG_SOC_SERIES_EFM32TG
CONFIG_SOC_SERIES_EFM32WG
CONFIG_SOC_SERIES_EFM32GG11B
CONFIG_SOC_SERIES_EFM32GG12B
CONFIG_SOC_SERIES_EFM32JG12B
CONFIG_SOC_SERIES_EFM32PG12B
CONFIG_SOC_SERIES_EFM32PG1B
CONFIG_SOC_SERIES_EFR32BG13P
CONFIG_SOC_SERIES_EFR32FG13P
CONFIG_SOC_SERIES_EFR32FG1P
CONFIG_SOC_SERIES_EFR32MG12P
CONFIG_SOC_SERIES_EFR32MG13P
CONFIG_GPIO_GECKO
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_SOC_SERIES_EFM32HG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32HG)、[`CONFIG_SOC_SERIES_EFM32TG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32TG)、[`CONFIG_SOC_SERIES_EFM32WG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32WG)、[`CONFIG_SOC_SERIES_EFM32GG11B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG11B)、[`CONFIG_SOC_SERIES_EFM32GG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG12B)、[`CONFIG_SOC_SERIES_EFM32JG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32JG12B)、[`CONFIG_SOC_SERIES_EFM32PG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG12B)、[`CONFIG_SOC_SERIES_EFM32PG1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG1B)、[`CONFIG_SOC_SERIES_EFR32BG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32BG13P)、[`CONFIG_SOC_SERIES_EFR32FG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG13P)、[`CONFIG_SOC_SERIES_EFR32FG1P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG1P)、[`CONFIG_SOC_SERIES_EFR32MG12P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG12P)、[`CONFIG_SOC_SERIES_EFR32MG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG13P)、[`CONFIG_GPIO_GECKO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_I2C"></a>

## 233.9 `CONFIG_SILABS_GECKO_I2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用芯片间总线接口（Inter-Integrated Circuit Interface，I2C）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_I2C_GECKO
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_I2C_GECKO`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_LETIMER"></a>

## 233.10 `CONFIG_SILABS_GECKO_LETIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用低能耗定时器（Low Energy Timer，LETIMER）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_LEUART"></a>

## 233.11 `CONFIG_SILABS_GECKO_LEUART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用低能耗通用异步收发器（Low Energy Universal Asynchronous Receiver/Transmitter，LEUART）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_LEUART_GECKO
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_LEUART_GECKO`](P165_drivers_serial_配置项参考_1.md#CONFIG_LEUART_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_MSC"></a>

## 233.12 `CONFIG_SILABS_GECKO_MSC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用存储系统控制器（Memory System Controller，MSC）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_GECKO
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_SOC_FLASH_GECKO`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_POWER_MANAGER"></a>

## 233.13 `CONFIG_SILABS_GECKO_POWER_MANAGER`

**提示（Prompt）**：电源管理器服务（Power Manager service）

**说明（Help）**

使用电源管理器（Power Manager）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**主动选择（Selects）**

```text
CONFIG_SILABS_GECKO_EMU
CONFIG_SILABS_GECKO_SLIST
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_SILABS_GECKO_EMU`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_GECKO_EMU)、[`CONFIG_SILABS_GECKO_SLIST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_SLIST)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`、`CONFIG_SILABS_GECKO_SLIST`。

<a id="CONFIG_SILABS_GECKO_PRS"></a>

## 233.14 `CONFIG_SILABS_GECKO_PRS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用外设反射系统（Peripheral Reflex System，PRS）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_SILABS_GECKO_SLEEPTIMER
CONFIG_SILABS_GECKO_SLEEPTIMER
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_SILABS_GECKO_SLEEPTIMER`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_GECKO_SLEEPTIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_RAIL_MULTIPROTOCOL"></a>

## 233.15 `CONFIG_SILABS_GECKO_RAIL_MULTIPROTOCOL`

**提示（Prompt）**：使用 RAIL 多协议库（Multiprotocol library）

**说明（Help）**

启用 Silicon Labs RAIL 多协议库（multiprotocol library），在 Gecko SoC 上提供多个无线协议之间的共存与仲裁（coexistence and arbitration），例如低功耗蓝牙（Bluetooth LE）与专有 2.4 GHz 协议栈之间的协调。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_GECKO_USE_RAIL && CONFIG_HAS_SILABS_GECKO
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_GECKO_USE_RAIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GECKO_USE_RAIL)、[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_RMU"></a>

## 233.16 `CONFIG_SILABS_GECKO_RMU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用复位管理单元（Reset Management Unit，RMU）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_HWINFO_GECKO
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_HWINFO_GECKO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_RTC"></a>

## 233.17 `CONFIG_SILABS_GECKO_RTC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用实时时间计数器（Real Time Counter，RTC）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_RTCC"></a>

## 233.18 `CONFIG_SILABS_GECKO_RTCC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用实时时间计数器与日历（Real Time Counter and Calendar，RTCC）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_GECKO_RTCC
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_COUNTER_GECKO_RTCC`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_GECKO_RTCC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_SLEEPTIMER"></a>

## 233.19 `CONFIG_SILABS_GECKO_SLEEPTIMER`

**提示（Prompt）**：休眠定时器服务（Sleeptimer service）

**说明（Help）**

使用休眠定时器（Sleeptimer）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**主动选择（Selects）**

```text
CONFIG_SILABS_GECKO_PRS
CONFIG_SILABS_GECKO_RTCC if n
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_SILABS_GECKO_PRS`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_GECKO_PRS)、[`CONFIG_SILABS_GECKO_RTCC`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_GECKO_RTCC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_TIMER"></a>

## 233.20 `CONFIG_SILABS_GECKO_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用定时器／计数器（Timer/Counter，TIMER）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_PWM_GECKO
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_PWM_GECKO`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_TRNG"></a>

## 233.21 `CONFIG_SILABS_GECKO_TRNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 具有真随机数生成器（True Random Number Generator，TRNG）模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFM32GG11B
CONFIG_SOC_SERIES_EFM32GG12B
CONFIG_SOC_SERIES_EFM32JG12B
CONFIG_SOC_SERIES_EFM32PG12B
CONFIG_SOC_SERIES_EFR32MG12P
CONFIG_SOC_SERIES_EFR32MG13P
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_SOC_SERIES_EFM32GG11B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG11B)、[`CONFIG_SOC_SERIES_EFM32GG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG12B)、[`CONFIG_SOC_SERIES_EFM32JG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32JG12B)、[`CONFIG_SOC_SERIES_EFM32PG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG12B)、[`CONFIG_SOC_SERIES_EFR32MG12P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG12P)、[`CONFIG_SOC_SERIES_EFR32MG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG13P)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_USART"></a>

## 233.22 `CONFIG_SILABS_GECKO_USART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用通用同步／异步收发器（Universal Synchronous Asynchronous Receiver/Transmitter，USART）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_UART_GECKO
CONFIG_SPI_SILABS_USART
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_UART_GECKO`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_GECKO)、[`CONFIG_SPI_SILABS_USART`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_SILABS_USART)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_GECKO_WDOG"></a>

## 233.23 `CONFIG_SILABS_GECKO_WDOG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用看门狗定时器（Watchdog Timer，WDOG）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_GECKO
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFM32HG
CONFIG_WDT_GECKO
```

**定义位置（Location）**：[`modules/hal_silabs/gecko/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/gecko/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → Gecko SDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_GECKO)、[`CONFIG_SOC_SERIES_EFM32HG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32HG)、[`CONFIG_WDT_GECKO`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_GECKO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_GECKO`。

<a id="CONFIG_SILABS_SISDK_ACMP"></a>

## 233.24 `CONFIG_SILABS_SISDK_ACMP`

**提示（Prompt）**：模拟比较器（ACMP）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_COMPARATOR_SILABS_ACMP
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_COMPARATOR_SILABS_ACMP`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_SILABS_ACMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_ADC"></a>

## 233.25 `CONFIG_SILABS_SISDK_ADC`

**提示（Prompt）**：模数转换器（ADC）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_ADC_SILABS_ADC
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_ADC_SILABS_ADC`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_SILABS_ADC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_BURTC"></a>

## 233.26 `CONFIG_SILABS_SISDK_BURTC`

**提示（Prompt）**：备份实时时间计数器（BURTC）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_SILABS_BURTC
CONFIG_GECKO_BURTC_TIMER
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_COUNTER_SILABS_BURTC`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SILABS_BURTC)、[`CONFIG_GECKO_BURTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_GECKO_BURTC_TIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_CLOCK_MANAGER"></a>

## 233.27 `CONFIG_SILABS_SISDK_CLOCK_MANAGER`

**提示（Prompt）**：时钟管理器服务（Clock Manager service）

**说明（Help）**

使用时钟管理器（Clock Manager）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_SE if CONFIG_SOC_FAMILY_SILABS_S3
CONFIG_SILABS_SISDK_SYSCFG if CONFIG_SOC_FAMILY_SILABS_S3
CONFIG_SILABS_SISDK_SYSTEM if CONFIG_SOC_FAMILY_SILABS_S3
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG21
CONFIG_SOC_FAMILY_SILABS_S2_XG22
CONFIG_SOC_FAMILY_SILABS_S2_XG23
CONFIG_SOC_FAMILY_SILABS_S2_XG24
CONFIG_SOC_FAMILY_SILABS_S2_XG26
CONFIG_SOC_FAMILY_SILABS_S2_XG27
CONFIG_SOC_FAMILY_SILABS_S2_XG28
CONFIG_SOC_FAMILY_SILABS_S2_XG29
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
CONFIG_CLOCK_CONTROL_SILABS_SERIES
CONFIG_CLOCK_CONTROL_SILABS_SERIES_OUTPUT
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SILABS_SISDK_SE`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_SE)、[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)、[`CONFIG_SILABS_SISDK_SYSCFG`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_SYSCFG)、[`CONFIG_SILABS_SISDK_SYSTEM`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_SYSTEM)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_CLOCK_CONTROL_SILABS_SERIES`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_SILABS_SERIES)、[`CONFIG_CLOCK_CONTROL_SILABS_SERIES_OUTPUT`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_SILABS_SERIES_OUTPUT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`、`CONFIG_SOC_FAMILY_SILABS_S3`。

<a id="CONFIG_SILABS_SISDK_CORE"></a>

## 233.28 `CONFIG_SILABS_SISDK_CORE`

**提示（Prompt）**：核心（CORE）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG21
CONFIG_SOC_FAMILY_SILABS_S2_XG22
CONFIG_SOC_FAMILY_SILABS_S2_XG23
CONFIG_SOC_FAMILY_SILABS_S2_XG24
CONFIG_SOC_FAMILY_SILABS_S2_XG26
CONFIG_SOC_FAMILY_SILABS_S2_XG27
CONFIG_SOC_FAMILY_SILABS_S2_XG28
CONFIG_SOC_FAMILY_SILABS_S2_XG29
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_CRYPTO"></a>

## 233.29 `CONFIG_SILABS_SISDK_CRYPTO`

**提示（Prompt）**：密码驱动（Crypto driver）

**说明（Help）**

使用密码驱动（crypto driver）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SERIES3_CRYPTO_ENABLED && CONFIG_HAS_SILABS_SISDK
```

**主动选择（Selects）**

```text
CONFIG_CSPRNG_NEEDED
```

**被选择（Selected by）**

```text
CONFIG_SILABS_SISDK_PSA_CRYPTO_HOST
CONFIG_SILABS_SISDK_PROTOCOL_CRYPTO
CONFIG_SILABS_SISDK_PSA_CRYPTO_HOST
CONFIG_SILABS_SISDK_PROTOCOL_CRYPTO
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_CSPRNG_NEEDED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CSPRNG_NEEDED)、[`CONFIG_SILABS_SISDK_PSA_CRYPTO_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_PSA_CRYPTO_HOST)、[`CONFIG_SILABS_SISDK_PROTOCOL_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_PROTOCOL_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`、`CONFIG_SILABS_SISDK_PSA_CRYPTO_HOST`、`CONFIG_SILABS_SISDK_PROTOCOL_CRYPTO`。

<a id="CONFIG_SILABS_SISDK_DEVICE_INIT"></a>

## 233.30 `CONFIG_SILABS_SISDK_DEVICE_INIT`

**提示（Prompt）**：设备初始化服务（Device Init service）

**说明（Help）**

使用 Silicon Labs HAL 中 `device_init` 服务提供的设备初始化例程（device initialization routines）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_EMU
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG21
CONFIG_SOC_FAMILY_SILABS_S2_XG22
CONFIG_SOC_FAMILY_SILABS_S2_XG23
CONFIG_SOC_FAMILY_SILABS_S2_XG24
CONFIG_SOC_FAMILY_SILABS_S2_XG26
CONFIG_SOC_FAMILY_SILABS_S2_XG27
CONFIG_SOC_FAMILY_SILABS_S2_XG28
CONFIG_SOC_FAMILY_SILABS_S2_XG29
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SILABS_SISDK_EMU`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_EMU)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG29)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_EMU"></a>

## 233.31 `CONFIG_SILABS_SISDK_EMU`

**提示（Prompt）**：能量管理单元（EMU）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_SILABS_SISDK_DEVICE_INIT
CONFIG_SILABS_SISDK_POWER_MANAGER
CONFIG_SILABS_SISDK_DEVICE_INIT
CONFIG_SILABS_SISDK_POWER_MANAGER
CONFIG_HWINFO_SILABS_S3
CONFIG_TEMP_SILABS_EMU
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SILABS_SISDK_DEVICE_INIT`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_DEVICE_INIT)、[`CONFIG_SILABS_SISDK_POWER_MANAGER`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_POWER_MANAGER)、[`CONFIG_HWINFO_SILABS_S3`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_SILABS_S3)、[`CONFIG_TEMP_SILABS_EMU`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_SILABS_EMU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_EUSART"></a>

## 233.32 `CONFIG_SILABS_SISDK_EUSART`

**提示（Prompt）**：扩展通用同步／异步收发器（EUSART）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_PRS
```

**被选择（Selected by）**

```text
CONFIG_UART_SILABS_EUSART
CONFIG_SPI_SILABS_EUSART
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SILABS_SISDK_PRS`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_PRS)、[`CONFIG_UART_SILABS_EUSART`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_SILABS_EUSART)、[`CONFIG_SPI_SILABS_EUSART`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_SILABS_EUSART)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_GPCRC"></a>

## 233.33 `CONFIG_SILABS_SISDK_GPCRC`

**提示（Prompt）**：通用循环冗余校验（GPCRC）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_CRC_DRIVER_SILABS_GPCRC
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_CRC_DRIVER_SILABS_GPCRC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SILABS_GPCRC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_GPIO"></a>

## 233.34 `CONFIG_SILABS_SISDK_GPIO`

**提示（Prompt）**：通用输入／输出（GPIO）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG21
CONFIG_SOC_FAMILY_SILABS_S2_XG22
CONFIG_SOC_FAMILY_SILABS_S2_XG23
CONFIG_SOC_FAMILY_SILABS_S2_XG24
CONFIG_SOC_FAMILY_SILABS_S2_XG26
CONFIG_SOC_FAMILY_SILABS_S2_XG27
CONFIG_SOC_FAMILY_SILABS_S2_XG28
CONFIG_SOC_FAMILY_SILABS_S2_XG29
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
CONFIG_GPIO_SILABS
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_GPIO_SILABS`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SILABS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_HFXO_MANAGER"></a>

## 233.35 `CONFIG_SILABS_SISDK_HFXO_MANAGER`

**提示（Prompt）**：高频晶体振荡器管理器服务（HFXO Manager service）

**说明（Help）**

使用高频晶体振荡器管理器（HFXO Manager）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_I2C"></a>

## 233.36 `CONFIG_SILABS_SISDK_I2C`

**提示（Prompt）**：I2C 的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_I2C_SILABS
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_I2C_SILABS`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_SILABS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_IADC"></a>

## 233.37 `CONFIG_SILABS_SISDK_IADC`

**提示（Prompt）**：IADC 的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_SYSTEM
```

**被选择（Selected by）**

```text
CONFIG_ADC_SILABS_IADC
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SILABS_SISDK_SYSTEM`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_SYSTEM)、[`CONFIG_ADC_SILABS_IADC`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_SILABS_IADC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_LDMA"></a>

## 233.38 `CONFIG_SILABS_SISDK_LDMA`

**提示（Prompt）**：链接式直接内存访问（LDMA）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_SLIST
```

**被选择（Selected by）**

```text
CONFIG_SOC_GECKO_USE_RAIL
CONFIG_DMA_SILABS_LDMA
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SILABS_SISDK_SLIST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_SLIST)、[`CONFIG_SOC_GECKO_USE_RAIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GECKO_USE_RAIL)、[`CONFIG_DMA_SILABS_LDMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_SILABS_LDMA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`、`CONFIG_SILABS_SISDK_SLIST`。

<a id="CONFIG_SILABS_SISDK_LETIMER"></a>

## 233.39 `CONFIG_SILABS_SISDK_LETIMER`

**提示（Prompt）**：低能耗定时器（LETIMER）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_PWM_SILABS_LETIMER
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_PWM_SILABS_LETIMER`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_SILABS_LETIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_MSC"></a>

## 233.40 `CONFIG_SILABS_SISDK_MSC`

**提示（Prompt）**：存储系统控制器（MSC）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_SILABS_S2
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SOC_FLASH_SILABS_S2`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SILABS_S2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_POWER_MANAGER"></a>

## 233.41 `CONFIG_SILABS_SISDK_POWER_MANAGER`

**提示（Prompt）**：电源管理器服务（Power Manager service）

**说明（Help）**

使用电源管理器（Power Manager）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_EMU if CONFIG_SOC_FAMILY_SILABS_S2
CONFIG_SILABS_SISDK_SLIST
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SILABS_SISDK_EMU`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_EMU)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SILABS_SISDK_SLIST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_SLIST)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`、`CONFIG_SOC_FAMILY_SILABS_S2`、`CONFIG_SILABS_SISDK_SLIST`。

<a id="CONFIG_SILABS_SISDK_PRS"></a>

## 233.42 `CONFIG_SILABS_SISDK_PRS`

**提示（Prompt）**：外设反射系统（PRS）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_SILABS_SISDK_EUSART
CONFIG_SILABS_SISDK_SLEEPTIMER
CONFIG_SILABS_SISDK_EUSART
CONFIG_SILABS_SISDK_SLEEPTIMER
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SILABS_SISDK_EUSART`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_EUSART)、[`CONFIG_SILABS_SISDK_SLEEPTIMER`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_SLEEPTIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_PSA_CRYPTO"></a>

## 233.43 `CONFIG_SILABS_SISDK_PSA_CRYPTO`

**提示（Prompt）**：支持硬件加速（hardware acceleration）的 TF-PSA-Crypto 驱动

**说明（Help）**

使用支持硬件加速密码操作（hardware-accelerated crypto operations）的驱动分发实现（driver dispatch implementation）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_C && CONFIG_HAS_SILABS_SISDK
```

**默认值（Defaults）**

```text
y if n || n
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_SE
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SILABS_SISDK_SE`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_SE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_RAIL_MULTIPROTOCOL"></a>

## 233.44 `CONFIG_SILABS_SISDK_RAIL_MULTIPROTOCOL`

**提示（Prompt）**：使用 RAIL 多协议库（Multiprotocol library）

**说明（Help）**

启用 Silicon Labs RAIL 多协议库（multiprotocol library），在 Gecko SoC 上提供多个无线协议之间的共存与仲裁（coexistence and arbitration），例如低功耗蓝牙（Bluetooth LE）与专有 2.4 GHz 协议栈之间的协调。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_GECKO_USE_RAIL && CONFIG_HAS_SILABS_SISDK
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_GECKO_USE_RAIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GECKO_USE_RAIL)、[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_RAIL_PA_CURVE_HEADER"></a>

## 233.45 `CONFIG_SILABS_SISDK_RAIL_PA_CURVE_HEADER`

**提示（Prompt）**：RAIL 功率放大器自定义曲线头文件（PA custom curve header file）

**说明（Help）**

功率放大器（PA）初始化使用的自定义 PA 曲线头文件名称。如何创建自定义 PA 曲线（custom PA curve），请参阅 AN1127。此头文件必须位于包含路径（include path）中。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**默认值（Defaults）**

```text
"pa_curves_efr32.h"
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_RAIL_PA_CURVE_TYPES_HEADER"></a>

## 233.46 `CONFIG_SILABS_SISDK_RAIL_PA_CURVE_TYPES_HEADER`

**提示（Prompt）**：RAIL 功率放大器曲线类型头文件（PA curve types header file）

**说明（Help）**

功率放大器（PA）初始化使用的自定义 PA 曲线类型头文件名称。如何创建自定义 PA 曲线（custom PA curve），请参阅 AN1127。此头文件必须位于包含路径（include path）中。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**默认值（Defaults）**

```text
"pa_curve_types_efr32.h"
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_RAIL_PA_ENABLE_CALIBRATION"></a>

## 233.47 `CONFIG_SILABS_SISDK_RAIL_PA_ENABLE_CALIBRATION`

**提示（Prompt）**：RAIL 功率放大器（PA）：应用出厂校准偏移（factory calibration offset）

**说明（Help）**

通过应用出厂校准（factory calibration），确保不同芯片之间的 PA 功率保持一致。此选项默认启用，并推荐所有 Series 2 设备启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_RMU"></a>

## 233.48 `CONFIG_SILABS_SISDK_RMU`

**提示（Prompt）**：复位管理单元（RMU）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_HWINFO_SILABS_S2
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_HWINFO_SILABS_S2`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_SILABS_S2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_RTCC"></a>

## 233.49 `CONFIG_SILABS_SISDK_RTCC`

**提示（Prompt）**：实时时间计数器与日历（RTCC）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_SE"></a>

## 233.50 `CONFIG_SILABS_SISDK_SE`

**提示（Prompt）**：安全引擎（Secure Engine，SE）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_SILABS_SISDK_CLOCK_MANAGER
CONFIG_SILABS_SISDK_PSA_CRYPTO
CONFIG_SILABS_SISDK_CLOCK_MANAGER
CONFIG_SILABS_SISDK_PSA_CRYPTO
CONFIG_ENTROPY_GECKO_SE
CONFIG_SOC_FLASH_SILABS_S3_EXTMEM
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SILABS_SISDK_CLOCK_MANAGER`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_CLOCK_MANAGER)、[`CONFIG_SILABS_SISDK_PSA_CRYPTO`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_PSA_CRYPTO)、[`CONFIG_ENTROPY_GECKO_SE`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GECKO_SE)、[`CONFIG_SOC_FLASH_SILABS_S3_EXTMEM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SILABS_S3_EXTMEM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_SLEEPTIMER"></a>

## 233.51 `CONFIG_SILABS_SISDK_SLEEPTIMER`

原库同名定义共 2 条；本项为数据库第 17178 条记录，各定义分别保留。

**提示（Prompt）**：休眠定时器服务（Sleeptimer service）

**说明（Help）**

使用休眠定时器（Sleeptimer）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_PRS
CONFIG_SILABS_SISDK_RTCC if n
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SILABS_SISDK_PRS`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_PRS)、[`CONFIG_SILABS_SISDK_RTCC`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_RTCC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_SLEEPTIMER--record-17179"></a>

## 233.52 `CONFIG_SILABS_SISDK_SLEEPTIMER`

原库同名定义共 2 条；本项为数据库第 17179 条记录，各定义分别保留。

**提示（Prompt）**：休眠定时器服务（Sleeptimer service）

**说明（Help）**

使用休眠定时器（Sleeptimer）HAL 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_WISECONNECT
```

**主动选择（Selects）**

```text
CONFIG_SRAM_VECTOR_TABLE
CONFIG_CODE_DATA_RELOCATION_SRAM
```

**定义位置（Location）**：[`modules/hal_silabs/wiseconnect/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/wiseconnect/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → WiSeConnect 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_WISECONNECT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_WISECONNECT)、[`CONFIG_SRAM_VECTOR_TABLE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_VECTOR_TABLE)、[`CONFIG_CODE_DATA_RELOCATION_SRAM`](P029_arch_arm_配置项参考_1.md#CONFIG_CODE_DATA_RELOCATION_SRAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_WISECONNECT`。

<a id="CONFIG_SILABS_SISDK_SYSCFG"></a>

## 233.53 `CONFIG_SILABS_SISDK_SYSCFG`

**提示（Prompt）**：系统配置（SYSCFG）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_SILABS_SISDK_CLOCK_MANAGER
CONFIG_SILABS_SISDK_CLOCK_MANAGER
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SILABS_SISDK_CLOCK_MANAGER`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_CLOCK_MANAGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_SYSTEM"></a>

## 233.54 `CONFIG_SILABS_SISDK_SYSTEM`

**提示（Prompt）**：系统设备信息（SYSTEM，device info）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_SILABS_SISDK_IADC
CONFIG_SILABS_SISDK_CLOCK_MANAGER
CONFIG_SILABS_SISDK_IADC
CONFIG_SILABS_SISDK_CLOCK_MANAGER
CONFIG_HWINFO_SILABS_S3
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SILABS_SISDK_IADC`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_IADC)、[`CONFIG_SILABS_SISDK_CLOCK_MANAGER`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_CLOCK_MANAGER)、[`CONFIG_HWINFO_SILABS_S3`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_SILABS_S3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_TIMER"></a>

## 233.55 `CONFIG_SILABS_SISDK_TIMER`

**提示（Prompt）**：定时器（TIMER）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_SOC_GECKO_USE_RAIL
CONFIG_COUNTER_SILABS_TIMER
CONFIG_PWM_SILABS_TIMER
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_SOC_GECKO_USE_RAIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GECKO_USE_RAIL)、[`CONFIG_COUNTER_SILABS_TIMER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SILABS_TIMER)、[`CONFIG_PWM_SILABS_TIMER`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_SILABS_TIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_USART"></a>

## 233.56 `CONFIG_SILABS_SISDK_USART`

**提示（Prompt）**：通用同步／异步收发器（USART）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_UART_SILABS_USART
CONFIG_SPI_SILABS_USART
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_UART_SILABS_USART`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_SILABS_USART)、[`CONFIG_SPI_SILABS_USART`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_SILABS_USART)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_VDAC"></a>

## 233.57 `CONFIG_SILABS_SISDK_VDAC`

**提示（Prompt）**：电压数模转换器（VDAC）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_DAC_SILABS_VDAC
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_DAC_SILABS_VDAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_SILABS_VDAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<a id="CONFIG_SILABS_SISDK_WDOG"></a>

## 233.58 `CONFIG_SILABS_SISDK_WDOG`

**提示（Prompt）**：看门狗（WDOG）的外设硬件抽象层（Peripheral HAL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SILABS_SISDK
```

**被选择（Selected by）**

```text
CONFIG_WDT_GECKO
CONFIG_WDT_SILABS_WDOG
```

**定义位置（Location）**：[`modules/hal_silabs/simplicity_sdk/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_silabs/simplicity_sdk/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_silabs（模块路径 `modules/hal/silabs`，相对于 west 工作区顶层目录） → SiSDK 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SILABS_SISDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SILABS_SISDK)、[`CONFIG_WDT_GECKO`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_GECKO)、[`CONFIG_WDT_SILABS_WDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_SILABS_WDOG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SILABS_SISDK`。

<!-- kconfig-navigation -->

[上一章](P232_modules_hal_sifli_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P234_modules_hal_tdk_配置项参考.md)
