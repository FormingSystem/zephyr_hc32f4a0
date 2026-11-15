---
id: learning.zephyr-docs.kconfig-reference.page-222
title: "`modules/hal_ambiq`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第222章\_`modules/hal_ambiq`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/hal_ambiq` 的 26 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_AMBIQ_COMPONENT_USE_BT"></a>

## 222.1 `CONFIG_AMBIQ_COMPONENT_USE_BT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq 提供的蓝牙组件（Bluetooth component）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_AMBIQ_BT_SUPPORTED
```

**被选择（Selected by）**

```text
CONFIG_BT_AMBIQ_HCI
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.components:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.components#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AMBIQ_BT_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMBIQ_BT_SUPPORTED)、[`CONFIG_BT_AMBIQ_HCI`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AMBIQ_HCI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AMBIQ_BT_SUPPORTED`。

<a id="CONFIG_AMBIQ_HAL"></a>

## 222.2 `CONFIG_AMBIQ_HAL`

**提示（Prompt）**：Ambiq 硬件抽象层（HAL）驱动支持

**说明（Help）**

使用 Ambiq 硬件抽象层（HAL）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_APOLLO2X || CONFIG_SOC_SERIES_APOLLO3X || CONFIG_SOC_SERIES_APOLLO4X || CONFIG_SOC_SERIES_APOLLO5X
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_APOLLO2X
CONFIG_SOC_SERIES_APOLLO3X
CONFIG_SOC_SERIES_APOLLO4X
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_ADC_AMBIQ
CONFIG_AUDIO_DMIC_AMBIQ_PDM
CONFIG_CLOCK_CONTROL_AMBIQ
CONFIG_COUNTER_AMBIQ
CONFIG_FLASH_AMBIQ
CONFIG_GPIO_AMBIQ
CONFIG_HWINFO_AMBIQ
CONFIG_I2C_AMBIQ
CONFIG_I2C_AMBIQ_IOS
CONFIG_I2S_AMBIQ
CONFIG_MSPI_AMBIQ_CONTROLLER
CONFIG_PINCTRL_AMBIQ
CONFIG_PWM_AMBIQ_TIMER
CONFIG_PWM_AMBIQ_CTIMER
CONFIG_RTC_AMBIQ
CONFIG_SDHC_AMBIQ
CONFIG_UART_AMBIQ
CONFIG_SPI_AMBIQ_SPIC
CONFIG_SPI_AMBIQ_SPID
CONFIG_SPI_AMBIQ_BLEIF
CONFIG_AMBIQ_STIMER_TIMER
CONFIG_UDC_AMBIQ
CONFIG_WDT_AMBIQ
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_APOLLO2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO2X)、[`CONFIG_SOC_SERIES_APOLLO3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO3X)、[`CONFIG_SOC_SERIES_APOLLO4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_ADC_AMBIQ`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AMBIQ)、[`CONFIG_AUDIO_DMIC_AMBIQ_PDM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_AMBIQ_PDM)、[`CONFIG_CLOCK_CONTROL_AMBIQ`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_AMBIQ)、[`CONFIG_COUNTER_AMBIQ`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_AMBIQ)、[`CONFIG_FLASH_AMBIQ`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_AMBIQ)、[`CONFIG_GPIO_AMBIQ`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_AMBIQ)、[`CONFIG_HWINFO_AMBIQ`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_AMBIQ)、[`CONFIG_I2C_AMBIQ`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_AMBIQ)、[`CONFIG_I2C_AMBIQ_IOS`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_AMBIQ_IOS)、[`CONFIG_I2S_AMBIQ`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_AMBIQ)、[`CONFIG_MSPI_AMBIQ_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_CONTROLLER)、[`CONFIG_PINCTRL_AMBIQ`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL_AMBIQ)、[`CONFIG_PWM_AMBIQ_TIMER`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_AMBIQ_TIMER)、[`CONFIG_PWM_AMBIQ_CTIMER`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_AMBIQ_CTIMER)、[`CONFIG_RTC_AMBIQ`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_AMBIQ)、[`CONFIG_SDHC_AMBIQ`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_AMBIQ)、[`CONFIG_UART_AMBIQ`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_AMBIQ)、[`CONFIG_SPI_AMBIQ_SPIC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMBIQ_SPIC)、[`CONFIG_SPI_AMBIQ_SPID`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMBIQ_SPID)、[`CONFIG_SPI_AMBIQ_BLEIF`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMBIQ_BLEIF)、[`CONFIG_AMBIQ_STIMER_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_AMBIQ_STIMER_TIMER)、[`CONFIG_UDC_AMBIQ`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ)、[`CONFIG_WDT_AMBIQ`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_AMBIQ)。

<a id="CONFIG_AMBIQ_HAL_USE_ADC"></a>

## 222.3 `CONFIG_AMBIQ_HAL_USE_ADC`

原库同名定义共 3 条；本项为数据库第 410 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_ADC_AMBIQ
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_ADC_AMBIQ`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AMBIQ)。

<a id="CONFIG_AMBIQ_HAL_USE_ADC--record-411"></a>

## 222.4 `CONFIG_AMBIQ_HAL_USE_ADC`

原库同名定义共 3 条；本项为数据库第 411 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_ADC_AMBIQ
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_ADC_AMBIQ`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AMBIQ)。

<a id="CONFIG_AMBIQ_HAL_USE_ADC--record-412"></a>

## 222.5 `CONFIG_AMBIQ_HAL_USE_ADC`

原库同名定义共 3 条；本项为数据库第 412 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_ADC_AMBIQ
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_ADC_AMBIQ`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AMBIQ)。

<a id="CONFIG_AMBIQ_HAL_USE_BLEIF"></a>

## 222.6 `CONFIG_AMBIQ_HAL_USE_BLEIF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的蓝牙低功耗接口（BLEIF）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_SPI_AMBIQ_BLEIF
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_SPI_AMBIQ_BLEIF`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMBIQ_BLEIF)。

<a id="CONFIG_AMBIQ_HAL_USE_DCU"></a>

## 222.7 `CONFIG_AMBIQ_HAL_USE_DCU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq 提供的 DCU 硬件抽象层（HAL）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)。

<a id="CONFIG_AMBIQ_HAL_USE_DSI"></a>

## 222.8 `CONFIG_AMBIQ_HAL_USE_DSI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的显示串行接口（DSI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)。

<a id="CONFIG_AMBIQ_HAL_USE_GPIO"></a>

## 222.9 `CONFIG_AMBIQ_HAL_USE_GPIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的通用输入／输出（GPIO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_GPIO_AMBIQ
CONFIG_PINCTRL_AMBIQ
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_GPIO_AMBIQ`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_AMBIQ)、[`CONFIG_PINCTRL_AMBIQ`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL_AMBIQ)。

<a id="CONFIG_AMBIQ_HAL_USE_HWINFO"></a>

## 222.10 `CONFIG_AMBIQ_HAL_USE_HWINFO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_HWINFO_AMBIQ
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_HWINFO_AMBIQ`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_AMBIQ)。

<a id="CONFIG_AMBIQ_HAL_USE_I2C"></a>

## 222.11 `CONFIG_AMBIQ_HAL_USE_I2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的 I2C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_I2C_AMBIQ
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_I2C_AMBIQ`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_AMBIQ)。

<a id="CONFIG_AMBIQ_HAL_USE_I2S"></a>

## 222.12 `CONFIG_AMBIQ_HAL_USE_I2S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的芯片间音频接口（I2S）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_I2S_AMBIQ
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_I2S_AMBIQ`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_AMBIQ)。

<a id="CONFIG_AMBIQ_HAL_USE_IOS_I2C"></a>

## 222.13 `CONFIG_AMBIQ_HAL_USE_IOS_I2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的 I2C 目标端（Target）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_I2C_AMBIQ_IOS
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_I2C_AMBIQ_IOS`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_AMBIQ_IOS)。

<a id="CONFIG_AMBIQ_HAL_USE_ITM"></a>

## 222.14 `CONFIG_AMBIQ_HAL_USE_ITM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq 提供的插桩跟踪宏单元（ITM）硬件抽象层（HAL）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)。

<a id="CONFIG_AMBIQ_HAL_USE_MSPI"></a>

## 222.15 `CONFIG_AMBIQ_HAL_USE_MSPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的 MSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_MSPI_AMBIQ_CONTROLLER
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_MSPI_AMBIQ_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_CONTROLLER)。

<a id="CONFIG_AMBIQ_HAL_USE_PDM"></a>

## 222.16 `CONFIG_AMBIQ_HAL_USE_PDM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的脉冲密度调制（PDM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_AUDIO_DMIC_AMBIQ_PDM
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_AUDIO_DMIC_AMBIQ_PDM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_AMBIQ_PDM)。

<a id="CONFIG_AMBIQ_HAL_USE_SDIO"></a>

## 222.17 `CONFIG_AMBIQ_HAL_USE_SDIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的安全数字输入／输出（SDIO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_SDHC_AMBIQ
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_SDHC_AMBIQ`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_AMBIQ)。

<a id="CONFIG_AMBIQ_HAL_USE_SPIC"></a>

## 222.18 `CONFIG_AMBIQ_HAL_USE_SPIC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的 SPI 控制器（Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_SPI_AMBIQ_SPIC
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_SPI_AMBIQ_SPIC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMBIQ_SPIC)。

<a id="CONFIG_AMBIQ_HAL_USE_SPID"></a>

## 222.19 `CONFIG_AMBIQ_HAL_USE_SPID`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的 SPI 设备端（Device）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_SPI_AMBIQ_SPID
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_SPI_AMBIQ_SPID`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMBIQ_SPID)。

<a id="CONFIG_AMBIQ_HAL_USE_STIMER"></a>

## 222.20 `CONFIG_AMBIQ_HAL_USE_STIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的系统定时器（STIMER）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_AMBIQ_STIMER_TIMER
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_STIMER_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_AMBIQ_STIMER_TIMER)。

<a id="CONFIG_AMBIQ_HAL_USE_TIMER"></a>

## 222.21 `CONFIG_AMBIQ_HAL_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的定时器（TIMER）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_ADC_AMBIQ
CONFIG_COUNTER_AMBIQ
CONFIG_PWM_AMBIQ_TIMER
CONFIG_PWM_AMBIQ_CTIMER
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_ADC_AMBIQ`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AMBIQ)、[`CONFIG_COUNTER_AMBIQ`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_AMBIQ)、[`CONFIG_PWM_AMBIQ_TIMER`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_AMBIQ_TIMER)、[`CONFIG_PWM_AMBIQ_CTIMER`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_AMBIQ_CTIMER)。

<a id="CONFIG_AMBIQ_HAL_USE_TPIU"></a>

## 222.22 `CONFIG_AMBIQ_HAL_USE_TPIU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq 提供的跟踪端口接口单元（TPIU）硬件抽象层（HAL）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)。

<a id="CONFIG_AMBIQ_HAL_USE_UART"></a>

## 222.23 `CONFIG_AMBIQ_HAL_USE_UART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的通用异步收发器（UART）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_UART_AMBIQ
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_UART_AMBIQ`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_AMBIQ)。

<a id="CONFIG_AMBIQ_HAL_USE_USB"></a>

## 222.24 `CONFIG_AMBIQ_HAL_USE_USB`

原库同名定义共 2 条；本项为数据库第 431 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的通用串行总线（USB）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_UDC_AMBIQ
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_UDC_AMBIQ`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ)。

<a id="CONFIG_AMBIQ_HAL_USE_USB--record-432"></a>

## 222.25 `CONFIG_AMBIQ_HAL_USE_USB`

原库同名定义共 2 条；本项为数据库第 432 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的通用串行总线（USB）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_UDC_AMBIQ
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_UDC_AMBIQ`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ)。

<a id="CONFIG_AMBIQ_HAL_USE_WDT"></a>

## 222.26 `CONFIG_AMBIQ_HAL_USE_WDT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 Ambiq HAL 的看门狗定时器（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMBIQ_HAL
```

**被选择（Selected by）**

```text
CONFIG_WDT_AMBIQ
```

**定义位置（Location）**：[`modules/hal_ambiq/Kconfig.hal:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ambiq/Kconfig.hal#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ambiq（模块路径 `modules/hal/ambiq`，相对于 west 工作区顶层目录） → Ambiq 硬件抽象层（HAL）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_AMBIQ_HAL`](P222_modules_hal_ambiq_配置项参考.md#CONFIG_AMBIQ_HAL)、[`CONFIG_WDT_AMBIQ`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_AMBIQ)。

<!-- kconfig-navigation -->

[上一章](P221_modules_cmsis_6_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P223_modules_hal_bouffalolab_配置项参考.md)
