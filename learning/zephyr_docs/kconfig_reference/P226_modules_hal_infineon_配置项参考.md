---
id: learning.zephyr-docs.kconfig-reference.page-226
title: "`modules/hal_infineon`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第226章\_`modules/hal_infineon`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/hal_infineon` 的 32 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_USE_INFINEON_ABSTRACTION_RTOS"></a>

## 226.1 `CONFIG_USE_INFINEON_ABSTRACTION_RTOS`

**提示（Prompt）**：实时操作系统抽象组件（Abstraction RTOS component），支持 Zephyr

**说明（Help）**

启用支持 Zephyr 的实时操作系统抽象组件（Abstraction RTOS component）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**被选择（Selected by）**

```text
CONFIG_PSOC_EDGE_M55_SRF_SUPPORT
CONFIG_BT_AIROC
CONFIG_WIFI_AIROC
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_PSOC_EDGE_M55_SRF_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSOC_EDGE_M55_SRF_SUPPORT)、[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_WIFI_AIROC`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AIROC)。

<a id="CONFIG_USE_INFINEON_ADC"></a>

## 226.2 `CONFIG_USE_INFINEON_ADC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用模数转换器（Analog-to-Digital Converter，ADC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_ADC_INFINEON_CAT1
CONFIG_ADC_INFINEON_SAR
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_ADC_INFINEON_CAT1`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_INFINEON_CAT1)、[`CONFIG_ADC_INFINEON_SAR`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_INFINEON_SAR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_AUTANALOG_SAR_ADC"></a>

## 226.3 `CONFIG_USE_INFINEON_AUTANALOG_SAR_ADC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用 AutAnalog 逐次逼近型模数转换器（SAR ADC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_MFD_INFINEON_AUTANALOG
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_MFD_INFINEON_AUTANALOG`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_AUTANALOG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_DMA"></a>

## 226.4 `CONFIG_USE_INFINEON_DMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用直接内存访问（DMA）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_ADC_INFINEON_CAT1
CONFIG_DMA_INFINEON_CAT1_HAL
CONFIG_DMA_INFINEON_CAT1_PDL
CONFIG_DMA_INFINEON
CONFIG_INFINEON_CAT1_QSPI_FLASH
CONFIG_UART_INFINEON_CAT1_PDL
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_ADC_INFINEON_CAT1`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_INFINEON_CAT1)、[`CONFIG_DMA_INFINEON_CAT1_HAL`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INFINEON_CAT1_HAL)、[`CONFIG_DMA_INFINEON_CAT1_PDL`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INFINEON_CAT1_PDL)、[`CONFIG_DMA_INFINEON`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INFINEON)、[`CONFIG_INFINEON_CAT1_QSPI_FLASH`](P093_drivers_flash_配置项参考_2.md#CONFIG_INFINEON_CAT1_QSPI_FLASH)、[`CONFIG_UART_INFINEON_CAT1_PDL`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INFINEON_CAT1_PDL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_FLASH"></a>

## 226.5 `CONFIG_USE_INFINEON_FLASH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用闪存（Flash）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_FLASH_INFINEON_CAT1
CONFIG_FLASH_INFINEON_PDL
CONFIG_INFINEON_CAT1_QSPI_FLASH
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_FLASH_INFINEON_CAT1`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INFINEON_CAT1)、[`CONFIG_FLASH_INFINEON_PDL`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INFINEON_PDL)、[`CONFIG_INFINEON_CAT1_QSPI_FLASH`](P093_drivers_flash_配置项参考_2.md#CONFIG_INFINEON_CAT1_QSPI_FLASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_FLASH_RRAM"></a>

## 226.6 `CONFIG_USE_INFINEON_FLASH_RRAM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用原文称为 Flash RRAM 的存储模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_FLASH_INFINEON_RRAM
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_FLASH_INFINEON_RRAM`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INFINEON_RRAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_HPPASS_ANALOG"></a>

## 226.7 `CONFIG_USE_INFINEON_HPPASS_ANALOG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用英飞凌（Infineon）HPPASS 模拟功能（Analog）外设驱动库（PDL）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_HPPASS_SAR_ADC"></a>

## 226.8 `CONFIG_USE_INFINEON_HPPASS_SAR_ADC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用英飞凌（Infineon）HPPASS 逐次逼近型模数转换器（SAR ADC）外设驱动库（PDL）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_ADC_INFINEON_HPPASS_SAR
CONFIG_MFD_INFINEON_HPPASS
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_ADC_INFINEON_HPPASS_SAR`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_INFINEON_HPPASS_SAR)、[`CONFIG_MFD_INFINEON_HPPASS`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_HPPASS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_I2C"></a>

## 226.9 `CONFIG_USE_INFINEON_I2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用芯片间总线接口（Inter-Integrated Circuit Interface，I2C）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_I2C_INFINEON_CAT1_HAL
CONFIG_I2C_INFINEON_CAT1_PDL
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_I2C_INFINEON_CAT1_HAL`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_INFINEON_CAT1_HAL)、[`CONFIG_I2C_INFINEON_CAT1_PDL`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_INFINEON_CAT1_PDL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_I2S"></a>

## 226.10 `CONFIG_USE_INFINEON_I2S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用芯片间音频接口（Inter-Integrated Sound Interface，I2S）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_I2S_INFINEON
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_I2S_INFINEON`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_INFINEON)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_I3C"></a>

## 226.11 `CONFIG_USE_INFINEON_I3C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用改进型芯片间总线接口（Improved Inter-Integrated Circuit Interface，I3C）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_LEGACY_HAL"></a>

## 226.12 `CONFIG_USE_INFINEON_LEGACY_HAL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用旧版硬件抽象层驱动（Legacy HAL driver），而不是基于外设驱动库（PDL）的驱动。这样，在完全迁移到 PDL 之前，设备仍可使用基于 HAL 的驱动。全部设备完成迁移后，将移除旧版 HAL 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_PSOC6
CONFIG_SOC_FAMILY_PSOC6_LEGACY
CONFIG_SOC_SERIES_XMC7200
CONFIG_SOC_SERIES_CYW20829
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_SOC_FAMILY_PSOC6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6)、[`CONFIG_SOC_SERIES_XMC7200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC7200)、[`CONFIG_SOC_SERIES_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYW20829)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`、`CONFIG_SOC_FAMILY_PSOC6`、`CONFIG_SOC_SERIES_XMC7200`、`CONFIG_SOC_SERIES_CYW20829`。

<a id="CONFIG_USE_INFINEON_LPCOMP"></a>

## 226.13 `CONFIG_USE_INFINEON_LPCOMP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用低功耗比较器（Low Power Comparator，LPComp）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_COMPARATOR_INFINEON_LPCOMP
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_COMPARATOR_INFINEON_LPCOMP`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_INFINEON_LPCOMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_LPTIMER"></a>

## 226.14 `CONFIG_USE_INFINEON_LPTIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用低功耗定时器（Low-Power Timer，LPTimer）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_SOC_PSE84_LPM_TIMER
CONFIG_SOC_PSC3_LPM_TIMER
CONFIG_INFINEON_LP_TIMER_HAL
CONFIG_INFINEON_LP_TIMER_PDL
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_SOC_PSE84_LPM_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PSE84_LPM_TIMER)、[`CONFIG_SOC_PSC3_LPM_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PSC3_LPM_TIMER)、[`CONFIG_INFINEON_LP_TIMER_HAL`](P007_drivers_timer_配置项参考_1.md#CONFIG_INFINEON_LP_TIMER_HAL)、[`CONFIG_INFINEON_LP_TIMER_PDL`](P007_drivers_timer_配置项参考_1.md#CONFIG_INFINEON_LP_TIMER_PDL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_MXCRYPTOLITE_AES"></a>

## 226.15 `CONFIG_USE_INFINEON_MXCRYPTOLITE_AES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用英飞凌（Infineon）MXCRYPTOLITE PDL 的 AES-128 硬件加速器源码（hardware accelerator sources），支持 ECB／CBC／CTR／CCM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_MXCRYPTOLITE_SHA256"></a>

## 226.16 `CONFIG_USE_INFINEON_MXCRYPTOLITE_SHA256`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用英飞凌（Infineon）MXCRYPTOLITE PDL 的 SHA-256 硬件加速器源码（hardware accelerator sources）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_MXCRYPTOLITE_TRNG"></a>

## 226.17 `CONFIG_USE_INFINEON_MXCRYPTOLITE_TRNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用英飞凌（Infineon）MXCRYPTOLITE PDL 的真随机数生成器（TRNG）硬件加速器源码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_ENTROPY_INFINEON_MXCRYPTOLITE_TRNG
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_ENTROPY_INFINEON_MXCRYPTOLITE_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_INFINEON_MXCRYPTOLITE_TRNG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_MXCRYPTO_AES"></a>

## 226.18 `CONFIG_USE_INFINEON_MXCRYPTO_AES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用英飞凌（Infineon）MXCRYPTO PDL 的 AES 硬件加速器源码（hardware accelerator sources），支持 ECB／CBC／CTR／CCM／GCM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_MXCRYPTO_CORE
```

**被选择（Selected by）**

```text
CONFIG_CRYPTO_INFINEON_MXCRYPTO
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_USE_INFINEON_MXCRYPTO_CORE`](P226_modules_hal_infineon_配置项参考.md#CONFIG_USE_INFINEON_MXCRYPTO_CORE)、[`CONFIG_CRYPTO_INFINEON_MXCRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_INFINEON_MXCRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_MXCRYPTO_CORE"></a>

## 226.19 `CONFIG_USE_INFINEON_MXCRYPTO_CORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用英飞凌（Infineon）MXCRYPTO PDL 核心源码（core sources），由 TRNG、AES、SHA 加速器及启用该硬件块的多功能设备（MFD）驱动共同使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_USE_INFINEON_MXCRYPTO_TRNG
CONFIG_USE_INFINEON_MXCRYPTO_AES
CONFIG_USE_INFINEON_MXCRYPTO_SHA
CONFIG_USE_INFINEON_MXCRYPTO_TRNG
CONFIG_USE_INFINEON_MXCRYPTO_AES
CONFIG_USE_INFINEON_MXCRYPTO_SHA
CONFIG_MFD_INFINEON_MXCRYPTO
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_USE_INFINEON_MXCRYPTO_TRNG`](P226_modules_hal_infineon_配置项参考.md#CONFIG_USE_INFINEON_MXCRYPTO_TRNG)、[`CONFIG_USE_INFINEON_MXCRYPTO_AES`](P226_modules_hal_infineon_配置项参考.md#CONFIG_USE_INFINEON_MXCRYPTO_AES)、[`CONFIG_USE_INFINEON_MXCRYPTO_SHA`](P226_modules_hal_infineon_配置项参考.md#CONFIG_USE_INFINEON_MXCRYPTO_SHA)、[`CONFIG_MFD_INFINEON_MXCRYPTO`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_MXCRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_MXCRYPTO_SHA"></a>

## 226.20 `CONFIG_USE_INFINEON_MXCRYPTO_SHA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用英飞凌（Infineon）MXCRYPTO PDL 的 SHA 硬件加速器源码（hardware accelerator sources），支持 SHA-224／256／384／512。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_MXCRYPTO_CORE
```

**被选择（Selected by）**

```text
CONFIG_CRYPTO_INFINEON_MXCRYPTO
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_USE_INFINEON_MXCRYPTO_CORE`](P226_modules_hal_infineon_配置项参考.md#CONFIG_USE_INFINEON_MXCRYPTO_CORE)、[`CONFIG_CRYPTO_INFINEON_MXCRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_INFINEON_MXCRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_MXCRYPTO_TRNG"></a>

## 226.21 `CONFIG_USE_INFINEON_MXCRYPTO_TRNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用英飞凌（Infineon）MXCRYPTO PDL 的真随机数生成器（TRNG）硬件加速器源码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_MXCRYPTO_CORE
```

**被选择（Selected by）**

```text
CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_USE_INFINEON_MXCRYPTO_CORE`](P226_modules_hal_infineon_配置项参考.md#CONFIG_USE_INFINEON_MXCRYPTO_CORE)、[`CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_PDM_PCM"></a>

## 226.22 `CONFIG_USE_INFINEON_PDM_PCM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用脉冲密度／脉冲编码调制（PDM-PCM）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_AUDIO_DMIC_INFINEON
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_AUDIO_DMIC_INFINEON`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_INFINEON)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_PWM"></a>

## 226.23 `CONFIG_USE_INFINEON_PWM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用脉宽调制器（Pulse Width Modulator，PWM）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_PWM_INFINEON_TCPWM
CONFIG_PWM_INFINEON_TCPWM_PSOC4
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_PWM_INFINEON_TCPWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_INFINEON_TCPWM)、[`CONFIG_PWM_INFINEON_TCPWM_PSOC4`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_INFINEON_TCPWM_PSOC4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_RTC"></a>

## 226.24 `CONFIG_USE_INFINEON_RTC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用实时时钟（Real-Time Clock，RTC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_RTC_INFINEON_CAT1
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_RTC_INFINEON_CAT1`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_INFINEON_CAT1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_SDHC"></a>

## 226.25 `CONFIG_USE_INFINEON_SDHC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用安全数字主机控制器（SDHC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_SDIO"></a>

## 226.26 `CONFIG_USE_INFINEON_SDIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用安全数字输入／输出接口（Secure Digital Input/Output interface，SDIO）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_SDHC_INFINEON_CAT1_PDL
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_SDHC_INFINEON_CAT1_PDL`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_INFINEON_CAT1_PDL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_SMIF"></a>

## 226.27 `CONFIG_USE_INFINEON_SMIF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用串行存储接口（SMIF）HAL 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_INFINEON_CAT1_QSPI_FLASH
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_INFINEON_CAT1_QSPI_FLASH`](P093_drivers_flash_配置项参考_2.md#CONFIG_INFINEON_CAT1_QSPI_FLASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_SPI"></a>

## 226.28 `CONFIG_USE_INFINEON_SPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用串行外设接口（Serial Peripheral Interface，SPI）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_SPI_INFINEON_HAL
CONFIG_SPI_INFINEON_PDL
CONFIG_SPI_PSOC6
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_SPI_INFINEON_HAL`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_INFINEON_HAL)、[`CONFIG_SPI_INFINEON_PDL`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_INFINEON_PDL)、[`CONFIG_SPI_PSOC6`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_PSOC6)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_TIMER"></a>

## 226.29 `CONFIG_USE_INFINEON_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用定时器／计数器（Timer/Counter）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_INFINEON_CAT1
CONFIG_COUNTER_INFINEON_TCPWM
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_COUNTER_INFINEON_CAT1`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_INFINEON_CAT1)、[`CONFIG_COUNTER_INFINEON_TCPWM`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_INFINEON_TCPWM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_TRNG"></a>

## 226.30 `CONFIG_USE_INFINEON_TRNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用真随机数生成器（True Random Number Generator，TRNG）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_UART"></a>

## 226.31 `CONFIG_USE_INFINEON_UART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_UART_INFINEON_CAT1_HAL
CONFIG_UART_INFINEON_CAT1_PDL
CONFIG_UART_PSOC6
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_UART_INFINEON_CAT1_HAL`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INFINEON_CAT1_HAL)、[`CONFIG_UART_INFINEON_CAT1_PDL`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INFINEON_CAT1_PDL)、[`CONFIG_UART_PSOC6`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_PSOC6)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_USE_INFINEON_WDT"></a>

## 226.32 `CONFIG_USE_INFINEON_WDT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为英飞凌（Infineon）设备启用看门狗定时器（WATCHDOG TIMER，WDT）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 || CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_PSOC6_LEGACY || CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_PSOC4100TP
CONFIG_WDT_INFINEON_CAT1
```

**定义位置（Location）**：[`modules/hal_infineon/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_infineon/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_infineon（模块路径 `modules/hal/infineon`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_SOC_SERIES_PSOC4100TP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100TP)、[`CONFIG_WDT_INFINEON_CAT1`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_INFINEON_CAT1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<!-- kconfig-navigation -->

[上一章](P225_modules_hal_gigadevice_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P227_modules_hal_nordic_配置项参考_1.md)
