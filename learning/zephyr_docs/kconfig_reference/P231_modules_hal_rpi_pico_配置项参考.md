---
id: learning.zephyr-docs.kconfig-reference.page-231
title: "`modules/hal_rpi_pico`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第231章\_`modules/hal_rpi_pico`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/hal_rpi_pico` 的 13 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PICOSDK_USE_ADC"></a>

## 231.1 `CONFIG_PICOSDK_USE_ADC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 pico-sdk 的模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ADC_RPI_PICO
```

**定义位置（Location）**：[`modules/hal_rpi_pico/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_rpi_pico/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_rpi_pico（模块路径 `modules/hal/rpi_pico`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_ADC_RPI_PICO`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_RPI_PICO)。

<a id="CONFIG_PICOSDK_USE_CLAIM"></a>

## 231.2 `CONFIG_PICOSDK_USE_CLAIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 pico-sdk 的资源申领（claim）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_PICOSDK_USE_PIO
CONFIG_PICOSDK_USE_PIO
CONFIG_COUNTER_TIMER_RPI_PICO
CONFIG_DMA_RPI_PICO
CONFIG_ENTROPY_RPI_PICO_RNG
CONFIG_HAZARD3_INTC
CONFIG_UART_RPI_PICO_PIO
CONFIG_SPI_RPI_PICO_PIO
```

**定义位置（Location）**：[`modules/hal_rpi_pico/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_rpi_pico/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_rpi_pico（模块路径 `modules/hal/rpi_pico`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PICOSDK_USE_PIO`](P231_modules_hal_rpi_pico_配置项参考.md#CONFIG_PICOSDK_USE_PIO)、[`CONFIG_COUNTER_TIMER_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_TIMER_RPI_PICO)、[`CONFIG_DMA_RPI_PICO`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_RPI_PICO)、[`CONFIG_ENTROPY_RPI_PICO_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_RPI_PICO_RNG)、[`CONFIG_HAZARD3_INTC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_HAZARD3_INTC)、[`CONFIG_UART_RPI_PICO_PIO`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RPI_PICO_PIO)、[`CONFIG_SPI_RPI_PICO_PIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RPI_PICO_PIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_COUNTER_TIMER_RPI_PICO`。

<a id="CONFIG_PICOSDK_USE_DMA"></a>

## 231.3 `CONFIG_PICOSDK_USE_DMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 pico-sdk 的直接内存访问（DMA）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_DMA_RPI_PICO
CONFIG_MIPI_DBI_RPI_PICO_PIO
```

**定义位置（Location）**：[`modules/hal_rpi_pico/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_rpi_pico/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_rpi_pico（模块路径 `modules/hal/rpi_pico`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_DMA_RPI_PICO`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_RPI_PICO)、[`CONFIG_MIPI_DBI_RPI_PICO_PIO`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI_RPI_PICO_PIO)。

<a id="CONFIG_PICOSDK_USE_FLASH"></a>

## 231.4 `CONFIG_PICOSDK_USE_FLASH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 pico-sdk 的闪存（flash）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_FLASH_RPI_PICO
CONFIG_HWINFO_RPI_PICO
```

**定义位置（Location）**：[`modules/hal_rpi_pico/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_rpi_pico/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_rpi_pico（模块路径 `modules/hal/rpi_pico`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_RPI_PICO`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RPI_PICO)、[`CONFIG_HWINFO_RPI_PICO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_RPI_PICO)。

<a id="CONFIG_PICOSDK_USE_GPIO"></a>

## 231.5 `CONFIG_PICOSDK_USE_GPIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 pico-sdk 的通用输入／输出（GPIO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_PICOSDK_USE_POWMAN
CONFIG_PICOSDK_USE_POWMAN
CONFIG_GPIO_RPI_PICO
CONFIG_PINCTRL_RPI_PICO
```

**定义位置（Location）**：[`modules/hal_rpi_pico/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_rpi_pico/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_rpi_pico（模块路径 `modules/hal/rpi_pico`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PICOSDK_USE_POWMAN`](P231_modules_hal_rpi_pico_配置项参考.md#CONFIG_PICOSDK_USE_POWMAN)、[`CONFIG_GPIO_RPI_PICO`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_RPI_PICO)、[`CONFIG_PINCTRL_RPI_PICO`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL_RPI_PICO)。

<a id="CONFIG_PICOSDK_USE_PIO"></a>

## 231.6 `CONFIG_PICOSDK_USE_PIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 pico-sdk 的可编程输入／输出（PIO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_PICOSDK_USE_CLAIM
```

**被选择（Selected by）**

```text
CONFIG_WS2812_STRIP_RPI_PICO_PIO
CONFIG_MIPI_DBI_RPI_PICO_PIO
CONFIG_PIO_RPI_PICO
CONFIG_UART_RPI_PICO_PIO
CONFIG_SPI_RPI_PICO_PIO
```

**定义位置（Location）**：[`modules/hal_rpi_pico/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_rpi_pico/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_rpi_pico（模块路径 `modules/hal/rpi_pico`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PICOSDK_USE_CLAIM`](P231_modules_hal_rpi_pico_配置项参考.md#CONFIG_PICOSDK_USE_CLAIM)、[`CONFIG_WS2812_STRIP_RPI_PICO_PIO`](P115_drivers_led_strip_配置项参考.md#CONFIG_WS2812_STRIP_RPI_PICO_PIO)、[`CONFIG_MIPI_DBI_RPI_PICO_PIO`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI_RPI_PICO_PIO)、[`CONFIG_PIO_RPI_PICO`](P123_drivers_misc_配置项参考.md#CONFIG_PIO_RPI_PICO)、[`CONFIG_UART_RPI_PICO_PIO`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RPI_PICO_PIO)、[`CONFIG_SPI_RPI_PICO_PIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RPI_PICO_PIO)。

<a id="CONFIG_PICOSDK_USE_POWMAN"></a>

## 231.7 `CONFIG_PICOSDK_USE_POWMAN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 pico-sdk 的电源管理器（power manager，POWMAN）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_PICOSDK_USE_GPIO
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RP2350
```

**定义位置（Location）**：[`modules/hal_rpi_pico/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_rpi_pico/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_rpi_pico（模块路径 `modules/hal/rpi_pico`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PICOSDK_USE_GPIO`](P231_modules_hal_rpi_pico_配置项参考.md#CONFIG_PICOSDK_USE_GPIO)、[`CONFIG_SOC_SERIES_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2350)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RP2350`。

<a id="CONFIG_PICOSDK_USE_PWM"></a>

## 231.8 `CONFIG_PICOSDK_USE_PWM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 pico-sdk 的脉宽调制（PWM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_COUNTER_RPI_PICO_PIT
CONFIG_PWM_RPI_PICO
```

**定义位置（Location）**：[`modules/hal_rpi_pico/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_rpi_pico/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_rpi_pico（模块路径 `modules/hal/rpi_pico`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_RPI_PICO_PIT`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_RPI_PICO_PIT)、[`CONFIG_PWM_RPI_PICO`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_RPI_PICO)。

<a id="CONFIG_PICOSDK_USE_RAND"></a>

## 231.9 `CONFIG_PICOSDK_USE_RAND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 pico-sdk 的随机数（rand）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ENTROPY_RPI_PICO_RNG
```

**定义位置（Location）**：[`modules/hal_rpi_pico/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_rpi_pico/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_rpi_pico（模块路径 `modules/hal/rpi_pico`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_RPI_PICO_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_RPI_PICO_RNG)。

<a id="CONFIG_PICOSDK_USE_RTC"></a>

## 231.10 `CONFIG_PICOSDK_USE_RTC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 pico-sdk 的实时时钟（RTC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_RTC_RPI_PICO
```

**定义位置（Location）**：[`modules/hal_rpi_pico/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_rpi_pico/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_rpi_pico（模块路径 `modules/hal/rpi_pico`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_RTC_RPI_PICO`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_RPI_PICO)。

<a id="CONFIG_PICOSDK_USE_SHA256"></a>

## 231.11 `CONFIG_PICOSDK_USE_SHA256`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 pico-sdk 的 SHA-256 驱动和实用工具（utilities）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CRYPTO_RPI_PICO_SHA256
```

**定义位置（Location）**：[`modules/hal_rpi_pico/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_rpi_pico/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_rpi_pico（模块路径 `modules/hal/rpi_pico`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_RPI_PICO_SHA256`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_RPI_PICO_SHA256)。

<a id="CONFIG_PICOSDK_USE_TIMER"></a>

## 231.12 `CONFIG_PICOSDK_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 pico-sdk 的定时器（TIMER）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_COUNTER_TIMER_RPI_PICO
CONFIG_ENTROPY_RPI_PICO_RNG
```

**定义位置（Location）**：[`modules/hal_rpi_pico/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_rpi_pico/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_rpi_pico（模块路径 `modules/hal/rpi_pico`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_TIMER_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_TIMER_RPI_PICO)、[`CONFIG_ENTROPY_RPI_PICO_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_RPI_PICO_RNG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_COUNTER_TIMER_RPI_PICO`。

<a id="CONFIG_PICOSDK_USE_UART"></a>

## 231.13 `CONFIG_PICOSDK_USE_UART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 pico-sdk 的通用异步收发器（UART）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`modules/hal_rpi_pico/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_rpi_pico/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_rpi_pico（模块路径 `modules/hal/rpi_pico`，相对于 west 工作区顶层目录）

<!-- kconfig-navigation -->

[上一章](P230_modules_hal_realtek_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P232_modules_hal_sifli_配置项参考.md)
