---
id: learning.zephyr-docs.kconfig-reference.page-68
title: "`drivers/counter`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第68章\_`drivers/counter`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `drivers/counter` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ACE_V1X_ART_COUNTER"></a>

## 68.1 `CONFIG_ACE_V1X_ART_COUNTER`

**提示（Prompt）**：ACE V1X 的 DSP ART 实际时间时钟（Wall Clock）

**说明（Help）**

ACE V1X 使用的 DSP ART 实际时间时钟（Wall Clock）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ACE_ART_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER_SUPPORTS_64BITS_TICKS
CONFIG_COUNTER_64BITS_TICKS
```

**定义位置（Location）**：[`drivers/counter/Kconfig.ace:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.ace#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_SUPPORTS_64BITS_TICKS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_64BITS_TICKS)、[`CONFIG_COUNTER_64BITS_TICKS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_64BITS_TICKS)。

<a id="CONFIG_ACE_V1X_RTC_COUNTER"></a>

## 68.2 `CONFIG_ACE_V1X_RTC_COUNTER`

**提示（Prompt）**：ACE V1X 的 DSP RTC 实际时间时钟（Wall Clock）

**说明（Help）**

ACE V1X 使用的 DSP RTC 实际时间时钟（Wall Clock）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ACE_RTC_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER_SUPPORTS_64BITS_TICKS
CONFIG_COUNTER_64BITS_TICKS
```

**定义位置（Location）**：[`drivers/counter/Kconfig.ace:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.ace#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_SUPPORTS_64BITS_TICKS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_64BITS_TICKS)、[`CONFIG_COUNTER_64BITS_TICKS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_64BITS_TICKS)。

<a id="CONFIG_COUNTER"></a>

## 68.3 `CONFIG_COUNTER`

**提示（Prompt）**：计数器驱动（Counter Drivers）

**说明（Help）**

启用计数器（Counter）与定时器（Timer）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_ALARM_COUNTER
CONFIG_OPENTHREAD_ALARM_COUNTER
CONFIG_DALI_PWM
CONFIG_DISPLAY_CHARLIEPLEX_LED_MATRIX
CONFIG_IEEE802154_MCXW
CONFIG_RTC_COUNTER
CONFIG_UART_BITBANG
CONFIG_GPIO_STEPPER_COUNTER_TIMING
CONFIG_WDT_COUNTER
CONFIG_WDT_ANDES_ATCWDT200
CONFIG_TEST_BUSY_SIM
```

**定义位置（Location）**：[`drivers/counter/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_ALARM_COUNTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_ALARM_COUNTER)、[`CONFIG_DALI_PWM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DALI_PWM)、[`CONFIG_DISPLAY_CHARLIEPLEX_LED_MATRIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DISPLAY_CHARLIEPLEX_LED_MATRIX)、[`CONFIG_IEEE802154_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IEEE802154_MCXW)、[`CONFIG_RTC_COUNTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_COUNTER)、[`CONFIG_UART_BITBANG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_BITBANG)、[`CONFIG_GPIO_STEPPER_COUNTER_TIMING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_STEPPER_COUNTER_TIMING)、[`CONFIG_WDT_COUNTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_COUNTER)、[`CONFIG_WDT_ANDES_ATCWDT200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_ANDES_ATCWDT200)、[`CONFIG_TEST_BUSY_SIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_BUSY_SIM)。

<a id="CONFIG_COUNTER_64BITS_FREQ"></a>

## 68.4 `CONFIG_COUNTER_64BITS_FREQ`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果计数器（Counter）驱动应使用 64 位值表示频率，则选择此项。通常由频率大于 4,294,967,295 Hz 的驱动设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER
```

**定义位置（Location）**：[`drivers/counter/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_64BITS_TICKS"></a>

## 68.5 `CONFIG_COUNTER_64BITS_TICKS`

**提示（Prompt）**：支持超过 32 位计数刻度的 API（Ticks Longer than 32 Bits）

**说明（Help）**

启用使用 64 位类型定义（Typedef）处理超过 32 位的计数刻度（Tick）的 API。驱动需自行实现所需函数，以提供相应支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_SUPPORTS_64BITS_TICKS && CONFIG_COUNTER
```

**被选择（Selected by）**

```text
CONFIG_ACE_V1X_ART_COUNTER
CONFIG_ACE_V1X_RTC_COUNTER
CONFIG_COUNTER_RTC_STM32_SUBSECONDS
```

**定义位置（Location）**：[`drivers/counter/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_SUPPORTS_64BITS_TICKS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_64BITS_TICKS)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_ACE_V1X_ART_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_ACE_V1X_ART_COUNTER)、[`CONFIG_ACE_V1X_RTC_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_ACE_V1X_RTC_COUNTER)、[`CONFIG_COUNTER_RTC_STM32_SUBSECONDS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_RTC_STM32_SUBSECONDS)。

<a id="CONFIG_COUNTER_AMBIQ"></a>

## 68.6 `CONFIG_COUNTER_AMBIQ`

**提示（Prompt）**：Ambiq 计数器驱动（Counter Driver）

**说明（Help）**

启用 Ambiq 器件的计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_TIMER
```

**定义位置（Location）**：[`drivers/counter/Kconfig.ambiq:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.ambiq#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_TIMER)。

<a id="CONFIG_COUNTER_ANDES_ATCPIT100"></a>

## 68.7 `CONFIG_COUNTER_ANDES_ATCPIT100`

**提示（Prompt）**：Andes ATCPIT100 周期中断定时器驱动（PIT Driver）

**说明（Help）**

启用 Andes ATCPIT100 周期中断定时器（PIT）控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_ATCPIT100_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.andes_atcpit100:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.andes_atcpit100#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_BEE_RTC"></a>

## 68.8 `CONFIG_COUNTER_BEE_RTC`

**提示（Prompt）**：瑞昱 Bee 系列 RTC 计数器驱动（Realtek Counter RTC Driver）

**说明（Help）**

启用瑞昱（Realtek）Bee 片上系统（SoC）的实时时钟计数器（Counter RTC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_COUNTER_RTC_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_RTC
```

**定义位置（Location）**：[`drivers/counter/Kconfig.bee_rtc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.bee_rtc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_HAL_REALTEK_BEE_RTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_RTC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_RTC`。

<a id="CONFIG_COUNTER_BEE_TIMER"></a>

## 68.9 `CONFIG_COUNTER_BEE_TIMER`

**提示（Prompt）**：瑞昱 Bee 系列定时器计数器驱动（Realtek Counter Timer Driver）

**说明（Help）**

启用瑞昱（Realtek）Bee 片上系统（SoC）的定时器计数器（Counter Timer）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_COUNTER_TIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_TIM if DT_HAS_REALTEK_BEE_BASIC_TIMER_ENABLED
CONFIG_HAL_REALTEK_BEE_ENHTIM if DT_HAS_REALTEK_BEE_ENHANCED_TIMER_ENABLED
```

**定义位置（Location）**：[`drivers/counter/Kconfig.bee_timer:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.bee_timer#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_HAL_REALTEK_BEE_TIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_TIM)、[`CONFIG_HAL_REALTEK_BEE_ENHTIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_ENHTIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_TIM`、`CONFIG_HAL_REALTEK_BEE_ENHTIM`。

<a id="CONFIG_COUNTER_BFLB_RTC"></a>

## 68.10 `CONFIG_COUNTER_BFLB_RTC`

**提示（Prompt）**：博流 RTC 计数器驱动（Bouffalo Lab RTC Counter Driver）

**说明（Help）**

启用博流（Bouffalo Lab）片上系统（SoC）的实时时钟计数器（RTC Counter）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_RTC_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.bflb:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.bflb#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_BFLB_TIMER"></a>

## 68.11 `CONFIG_COUNTER_BFLB_TIMER`

**提示（Prompt）**：博流定时器计数器驱动（Bouffalo Lab Timer Counter Driver）

**说明（Help）**

启用博流（Bouffalo Lab）片上系统（SoC）的通用定时器计数器（General-Purpose Timer Counter）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_TIMER_CHANNEL_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_BFLB_TIMER_HAS_CNT_CLR"></a>

## 68.12 `CONFIG_COUNTER_BFLB_TIMER_HAS_CNT_CLR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统（SoC）的 `TCER` 寄存器具有计数器清零位（Counter Clear Bits），支持硬件复位计数器。未设置此项时，驱动在自由运行模式（Free-Run Mode）下跟踪软件周期偏移（Software Cycle Offset），模拟计数器复位。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_BFLB_TIMER && CONFIG_COUNTER
```

**定义位置（Location）**：[`drivers/counter/Kconfig.bflb:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.bflb#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → 博流定时器计数器驱动（Bouffalo Lab Timer Counter Driver）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_BFLB_TIMER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_BFLB_TIMER)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_CALIBRATION"></a>

## 68.13 `CONFIG_COUNTER_CALIBRATION`

**提示（Prompt）**：计数器驱动校准支持（Counter Driver Calibration Support）

**说明（Help）**

启用计数器时钟校准（Counter Clock Calibration）支持。校准量以十亿分之一（Parts Per Billion，ppb）表示，正值使计数器加快，负值使其减慢。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER
```

**被选择（Selected by）**

```text
CONFIG_RTC_COUNTER
```

**定义位置（Location）**：[`drivers/counter/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_RTC_COUNTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_COUNTER)。

<a id="CONFIG_COUNTER_CAPTURE"></a>

## 68.14 `CONFIG_COUNTER_CAPTURE`

**提示（Prompt）**：计数器捕获（Counter Capture）［实验性，EXPERIMENTAL］

**说明（Help）**

启用计数器捕获（Counter Capture）支持。该功能可对外部事件进行硬件时间戳记录（Hardware Timestamping），并在事件发生时产生软件中断（Software Interrupt）。并非所有计数器驱动都支持此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_SUPPORTS_CAPTURE && CONFIG_COUNTER
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/counter/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_SUPPORTS_CAPTURE`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_CAPTURE)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_COUNTER_CC23X0_LGPT"></a>

## 68.15 `CONFIG_COUNTER_CC23X0_LGPT`

**提示（Prompt）**：基于 LGPT 定时器的 CC23x0 计数器驱动（Counter Driver）

**说明（Help）**

启用 CC23x0 基于 LGPT 定时器（Timer）的计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC23X0_LGPT_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.cc23x0_lgpt:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.cc23x0_lgpt#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_CC23X0_RTC"></a>

## 68.16 `CONFIG_COUNTER_CC23X0_RTC`

**提示（Prompt）**：基于 RTC 定时器的 CC23x0 计数器驱动（Counter Driver）

**说明（Help）**

启用 CC23x0 基于实时时钟（RTC）定时器的计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC23X0_RTC_ENABLED && CONFIG_CC23X0_SYSTIM_TIMER && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER_SUPPORTS_64BITS_TICKS
```

**定义位置（Location）**：[`drivers/counter/Kconfig.cc23x0_rtc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.cc23x0_rtc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CC23X0_SYSTIM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_CC23X0_SYSTIM_TIMER)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_SUPPORTS_64BITS_TICKS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_64BITS_TICKS)。

<a id="CONFIG_COUNTER_CMOS"></a>

## 68.17 `CONFIG_COUNTER_CMOS`

**提示（Prompt）**：x86 CMOS／RTC 时钟的计数器驱动（Counter Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MOTOROLA_MC146818_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y if !CONFIG_RTC
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/counter/Kconfig.cmos:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.cmos#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_RTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_COUNTER_CRSAS_MA2"></a>

## 68.18 `CONFIG_COUNTER_CRSAS_MA2`

**提示（Prompt）**：ARM CRSAS-MA2 系统计数器驱动（System Counter Driver）

**说明（Help）**

启用 ARM CRSAS-MA2，即 Corstone 参考系统架构规范 Ma2（Corstone Reference System Architecture Specification Ma2），的系统计数器（System Counter）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_CRSAS_MA2_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_CRSAS_MA2_TIMER
```

**定义位置（Location）**：[`drivers/counter/Kconfig.crsas_ma2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.crsas_ma2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_CRSAS_MA2_TIMER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_CRSAS_MA2_TIMER)。

<a id="CONFIG_COUNTER_CRSAS_MA2_TIMER"></a>

## 68.19 `CONFIG_COUNTER_CRSAS_MA2_TIMER`

**提示（Prompt）**：ARM CRSAS-MA2 系统定时器驱动（System Timer Driver）

**说明（Help）**

启用 ARM CRSAS-MA2，即 Corstone 参考系统架构规范 Ma2（Corstone Reference System Architecture Specification Ma2），的系统定时器（System Timer）支持。注意，尽管 ARM 将其命名为定时器，其工作方式实际上更接近 Zephyr 计数器（Counter）接口提供的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_CRSAS_MA2_TIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER_CRSAS_MA2
```

**定义位置（Location）**：[`drivers/counter/Kconfig.crsas_ma2:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.crsas_ma2#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_CRSAS_MA2`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_CRSAS_MA2)。

<a id="CONFIG_COUNTER_GECKO_RTCC"></a>

## 68.20 `CONFIG_COUNTER_GECKO_RTCC`

**提示（Prompt）**：Silicon Labs Gecko RTCC 计数器驱动（Counter Driver）

**说明（Help）**

启用 Silicon Labs Gecko 芯片基于 RTCC 模块的计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GECKO_RTCC_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_GECKO_CMU
CONFIG_SILABS_GECKO_RTCC
```

**定义位置（Location）**：[`drivers/counter/Kconfig.silabs:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.silabs#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_SILABS_GECKO_CMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_CMU)、[`CONFIG_SILABS_GECKO_RTCC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_RTCC)。

<a id="CONFIG_COUNTER_GECKO_STIMER"></a>

## 68.21 `CONFIG_COUNTER_GECKO_STIMER`

**提示（Prompt）**：Silicon Labs Gecko 休眠定时器计数器驱动（Sleep Timer Counter Driver）

**说明（Help）**

启用 Silicon Labs Gecko 芯片休眠定时器（Sleep Timer）模块的计数器（Counter）驱动。

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
CONFIG_SILABS_GECKO_SLEEPTIMER
CONFIG_SILABS_SISDK_SLEEPTIMER
```

**定义位置（Location）**：[`drivers/counter/Kconfig.silabs:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.silabs#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SILABS_GECKO_SLEEPTIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_SLEEPTIMER)、[`CONFIG_SILABS_SISDK_SLEEPTIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_SLEEPTIMER)。

<a id="CONFIG_COUNTER_IMX_EPIT"></a>

## 68.22 `CONFIG_COUNTER_IMX_EPIT`

**提示（Prompt）**：i.MX EPIT 驱动（Driver）

**说明（Help）**

启用 i.MX EPIT 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_EPIT_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.imx_epit:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.imx_epit#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_INFINEON_CAT1"></a>

## 68.23 `CONFIG_COUNTER_INFINEON_CAT1`

**提示（Prompt）**：英飞凌 CAT1 计数器驱动（Infineon Counter Driver）

**说明（Help）**

启用英飞凌（Infineon）CAT1 系列的计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_TIMER
```

**定义位置（Location）**：[`drivers/counter/Kconfig.infineon:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.infineon#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_USE_INFINEON_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_TIMER)。

<a id="CONFIG_COUNTER_INFINEON_TCPWM"></a>

## 68.24 `CONFIG_COUNTER_INFINEON_TCPWM`

**提示（Prompt）**：英飞凌 TCPWM 计数器驱动（Infineon Counter Driver）

**说明（Help）**

启用英飞凌（Infineon）器件的 TCPWM 计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_TCPWM_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_TIMER
```

**定义位置（Location）**：[`drivers/counter/Kconfig.infineon_tcpwm:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.infineon_tcpwm#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_USE_INFINEON_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_TIMER)。

<a id="CONFIG_COUNTER_INIT_PRIORITY"></a>

## 68.25 `CONFIG_COUNTER_INIT_PRIORITY`

**提示（Prompt）**：计数器初始化优先级（Counter Init Priority）

**说明（Help）**

计数器（Counter）驱动设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/counter/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_COUNTER_ITE_IT51XXX"></a>

## 68.26 `CONFIG_COUNTER_ITE_IT51XXX`

**提示（Prompt）**：ITE IT51XXX 计数器驱动（Counter Driver）

**说明（Help）**

启用 ITE IT51XXX 的计数器（Counter）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.ite_it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.ite_it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_ITE_IT8XXX2"></a>

## 68.27 `CONFIG_COUNTER_ITE_IT8XXX2`

**提示（Prompt）**：ITE IT8XXX2 定时器驱动（Timer Driver）

**说明（Help）**

启用 ITE IT8XXX2 的计数器（Counter）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.ite_it8xxx2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.ite_it8xxx2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCHP_G1_TCC"></a>

## 68.28 `CONFIG_COUNTER_MCHP_G1_TCC`

**提示（Prompt）**：Microchip TCC G1 计数器驱动（Counter Driver）

**说明（Help）**

启用 Microchip 定时器（Timer）外设的计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_TCC_G1_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCHP_RTC_G1"></a>

## 68.29 `CONFIG_COUNTER_MCHP_RTC_G1`

**提示（Prompt）**：Microchip RTC G1 计数器驱动（Counter Driver）

**说明（Help）**

启用 Microchip 定时器（Timer）外设的计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_RTC_G1_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mchp:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mchp#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCHP_SAM_PIT64B"></a>

## 68.30 `CONFIG_COUNTER_MCHP_SAM_PIT64B`

**提示（Prompt）**：Microchip SAM PIT64B 计数器（Counter）

**说明（Help）**

启用 Microchip PIT64B 计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SAM_PIT64B_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mchp_sam_pit64b:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mchp_sam_pit64b#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCHP_TC_G1"></a>

## 68.31 `CONFIG_COUNTER_MCHP_TC_G1`

**提示（Prompt）**：Microchip TC G1 计数器驱动（Counter Driver）

**说明（Help）**

启用 Microchip 定时器（Timer）外设的计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_TC_G1_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mchp:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mchp#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCHP_TC_G2"></a>

## 68.32 `CONFIG_COUNTER_MCHP_TC_G2`

**提示（Prompt）**：Microchip 第 2 代定时器计数器驱动（Timer Counter g2 Driver）

**说明（Help）**

启用 Microchip 第 2 代定时器计数器（Timer Counter g2）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_TC_G2_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mchp:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mchp#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_CTIMER"></a>

## 68.33 `CONFIG_COUNTER_MCUX_CTIMER`

**提示（Prompt）**：MCUX CTIMER 驱动（Driver）

**说明（Help）**

启用 MCUX CTIMER 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_CTIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER_SUPPORTS_CAPTURE
CONFIG_MUX if CONFIG_COUNTER_CAPTURE
CONFIG_PINCTRL if CONFIG_COUNTER_CAPTURE
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_ctimer:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_ctimer#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_SUPPORTS_CAPTURE`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_CAPTURE)、[`CONFIG_MUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MUX)、[`CONFIG_COUNTER_CAPTURE`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_CAPTURE)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_COUNTER_MCUX_CTIMER_RESERVE_CHANNEL_FOR_SETTOP"></a>

## 68.34 `CONFIG_COUNTER_MCUX_CTIMER_RESERVE_CHANNEL_FOR_SETTOP`

**提示（Prompt）**：预留一个 CTimer 通道用于设置计数上限值（Top Value）

**说明（Help）**

预留一个 CTimer 通道，用于设置计数上限值（Top Value）。不预留时，上限值只能设为计数器可表示的最大值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_MCUX_CTIMER && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_ctimer:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_ctimer#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → MCUX CTIMER 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_MCUX_CTIMER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_MCUX_CTIMER)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_FTM"></a>

## 68.35 `CONFIG_COUNTER_MCUX_FTM`

**提示（Prompt）**：MCUX FTM 驱动（Driver）

**说明（Help）**

启用 MCUX 灵活定时器（FlexTimer，FTM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FTM_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_ftm:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_ftm#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_GPT"></a>

## 68.36 `CONFIG_COUNTER_MCUX_GPT`

**提示（Prompt）**：MCUX GPT 驱动（Driver）

**说明（Help）**

启用 MCUX 通用定时器（General Purpose Timer，GPT）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_GPT_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_KERNEL_DIRECT_MAP if CONFIG_MMU
CONFIG_COUNTER_SUPPORTS_CAPTURE
CONFIG_PINCTRL if CONFIG_COUNTER_CAPTURE
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_gpt:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_gpt#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_KERNEL_DIRECT_MAP`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_DIRECT_MAP)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_COUNTER_SUPPORTS_CAPTURE`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_CAPTURE)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_COUNTER_CAPTURE`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_CAPTURE)。

<a id="CONFIG_COUNTER_MCUX_LPC_RTC"></a>

## 68.37 `CONFIG_COUNTER_MCUX_LPC_RTC`

**提示（Prompt）**：MCUX LPC RTC 驱动（Driver）

**说明（Help）**

启用 LPC 实时时钟（RTC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NXP_LPC_RTC_ENABLED || DT_HAS_NXP_LPC_RTC_HIGHRES_ENABLED) && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_lpc_rtc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_lpc_rtc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_LPC_RTC_1HZ"></a>

## 68.38 `CONFIG_COUNTER_MCUX_LPC_RTC_1HZ`

**提示（Prompt）**：MCUX LPC RTC 1Hz 计数器驱动（Counter Driver）

**说明（Help）**

启用 LPC 1Hz 计数器（Counter）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_RTC_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_lpc_rtc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_lpc_rtc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_LPC_RTC_HIGHRES"></a>

## 68.39 `CONFIG_COUNTER_MCUX_LPC_RTC_HIGHRES`

**提示（Prompt）**：MCUX LPC RTC 高分辨率计数器驱动（High Resolution Counter Driver）

**说明（Help）**

启用 LPC 实时时钟（RTC）的高分辨率计数器（High Resolution Counter）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_RTC_HIGHRES_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_lpc_rtc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_lpc_rtc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_LPIT"></a>

## 68.40 `CONFIG_COUNTER_MCUX_LPIT`

**提示（Prompt）**：恩智浦 LPIT 驱动（NXP Driver）

**说明（Help）**

启用恩智浦（NXP）低功耗周期中断定时器（Low Power Periodic Interrupt Timer，LPIT）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPIT_CHANNEL_ENABLED && DT_HAS_NXP_LPIT_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_lpit:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_lpit#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_LPTMR"></a>

## 68.41 `CONFIG_COUNTER_MCUX_LPTMR`

**提示（Prompt）**：MCUX LPTMR 驱动（Driver）

**说明（Help）**

启用 MCUX 低功耗定时器（Low Power Timer，LPTMR）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPTMR_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_lptmr:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_lptmr#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_LPTMR_ALARM"></a>

## 68.42 `CONFIG_COUNTER_MCUX_LPTMR_ALARM`

**提示（Prompt）**：LPTMR 告警支持（Alarm Support）

**说明（Help）**

低功耗定时器（LPTMR）是许多恩智浦（NXP）微控制器（MCU）常用的唤醒源（Wake-Up Source），也可作为 Cortex-M 系统滴答定时器（SysTick）的配套低功耗定时器。启用单次告警（Single-Shot Alarm）需要重新配置硬件比较寄存器 `COMPARE` / `CMR`，而周期性计数上限回调（TOP Callback）也使用同一资源。

受此硬件限制，本 Kconfig 选项决定是否启用告警支持：

- 启用告警支持时，驱动不允许运行时设置 TOP；尝试设置会返回 `-ENOTSUP`。
- 禁用告警支持时，驱动不允许运行时设置或取消 ALARM；尝试这些操作会返回 `-ENOTSUP`。

应根据应用需求选择。此定时器被选为系统定时器的低功耗配套定时器时，默认启用告警，因为配套定时器通过单次告警启动；没有此功能，系统定时器便无法补偿在低功耗状态中经过的时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_MCUX_LPTMR && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y if CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER && n
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_lptmr:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_lptmr#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → MCUX LPTMR 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_MCUX_LPTMR`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_MCUX_LPTMR)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_QTMR"></a>

## 68.43 `CONFIG_COUNTER_MCUX_QTMR`

**提示（Prompt）**：MCUX QTMR 驱动（Driver）

**说明（Help）**

启用 MCUX 四路定时器（Quad Timer，QTMR）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_TMR_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER_SUPPORTS_CAPTURE
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_qtmr:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_qtmr#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_SUPPORTS_CAPTURE`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_CAPTURE)。

<a id="CONFIG_COUNTER_MCUX_RTC"></a>

## 68.44 `CONFIG_COUNTER_MCUX_RTC`

**提示（Prompt）**：MCUX RTC 驱动（Driver）

**说明（Help）**

启用 MCU 实时时钟（RTC）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_RTC_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_rtc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_rtc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_RTC_JDP"></a>

## 68.45 `CONFIG_COUNTER_MCUX_RTC_JDP`

**提示（Prompt）**：MCUX RTC JDP 驱动（Driver）

**说明（Help）**

启用 MCU RTC JDP 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_RTC_JDP_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_rtc_jdp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_rtc_jdp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_SNVS"></a>

## 68.46 `CONFIG_COUNTER_MCUX_SNVS`

**提示（Prompt）**：i.MX SNVS RTC 驱动（Driver）

**说明（Help）**

启用 i.MX SNVS 高／低功耗时钟（High / Low Power Clock）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_SNVS_RTC_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_snvs:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_snvs#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_SNVS_SRTC"></a>

## 68.47 `CONFIG_COUNTER_MCUX_SNVS_SRTC`

**提示（Prompt）**：i.MX SNVS 安全 RTC 低功耗支持（SRTC Low Power Support）

**说明（Help）**

启用 SNVS 中低功耗安全实时时钟（SRTC）的同步（Synchronisation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_MCUX_SNVS && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_snvs:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_snvs#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → i.MX SNVS RTC 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_MCUX_SNVS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_MCUX_SNVS)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_STM"></a>

## 68.48 `CONFIG_COUNTER_MCUX_STM`

**提示（Prompt）**：MCUX STM 驱动（Driver）

**说明（Help）**

启用 MCUX 系统定时器模块（System Timer Module，STM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_STM_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_stm:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_stm#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_SYSCTR"></a>

## 68.49 `CONFIG_COUNTER_MCUX_SYSCTR`

**提示（Prompt）**：MCUX 系统计数器驱动（System Counter，SYS_CTR）

**说明（Help）**

启用恩智浦（NXP）系统计数器（System Counter，SYS_CTR）支持。SYS_CTR 是 56 位自由运行递增计数器（Free-Running Up-Counter），为多个处理器内核提供共享时基（Shared Time Base）。它支持两个比较帧（Compare Frame），每个都能产生中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SYSCTR_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_sysctr:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_sysctr#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_TPM"></a>

## 68.50 `CONFIG_COUNTER_MCUX_TPM`

**提示（Prompt）**：MCUX TPM 计数器驱动（Counter Driver）

**说明（Help）**

启用 MCUX 定时器 PWM 模块（Timer PWM Module，TPM）的计数器（Counter）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_TPM_TIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER_SUPPORTS_CAPTURE
CONFIG_PINCTRL if CONFIG_COUNTER_CAPTURE
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_tpm:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_tpm#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_SUPPORTS_CAPTURE`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_CAPTURE)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_COUNTER_CAPTURE`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_CAPTURE)。

<a id="CONFIG_COUNTER_MCUX_TSTMR"></a>

## 68.51 `CONFIG_COUNTER_MCUX_TSTMR`

**提示（Prompt）**：MCUX 时间戳定时器驱动（Time Stamp Timer，TSTMR）

**说明（Help）**

启用恩智浦（NXP）时间戳定时器（TSTMR）支持。TSTMR 是 56 位自由运行递增计数器（Free-Running Up-Counter），其频率由具体片上系统（SoC）决定，参阅设备树（Devicetree）的 `clock-frequency` 属性。它不提供比较（Compare）、告警（Alarm）、上限值（Top Value）或中断功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_TSTMR_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER_SUPPORTS_64BITS_TICKS
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_tstmr:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_tstmr#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_SUPPORTS_64BITS_TICKS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_64BITS_TICKS)。

<a id="CONFIG_COUNTER_MCUX_TSTMR_SYSCTR_BACKEND"></a>

## 68.52 `CONFIG_COUNTER_MCUX_TSTMR_SYSCTR_BACKEND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在同时启用了 `nxp,sysctr` 节点的片上系统（SoC）上构建 TSTMR 驱动时，自动选择此项。这类 SoC 的 TSTMR 是共享 `SYS_CTR` 硬件的只读视图（Read-Only View），因此驱动需要访问 `SYS_CTR_CONTROL` 寄存器，以启用计数器并使其稳定。

未设置此符号时，例如 MCXW 或 i.MX8ULP 上不具有 SYS_CTR 的独立 TSTMR，相关寄存器访问代码会被完全排除在编译结果之外。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_MCUX_TSTMR && DT_HAS_NXP_SYSCTR_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_tstmr:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_tstmr#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → MCUX 时间戳定时器驱动（Time Stamp Timer，TSTMR）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_MCUX_TSTMR`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_MCUX_TSTMR)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_WAKE_TIMER"></a>

## 68.53 `CONFIG_COUNTER_MCUX_WAKE_TIMER`

**提示（Prompt）**：MCUX 唤醒定时器驱动（Wake Timer Driver）

**说明（Help）**

启用 MCUX 唤醒定时器（Wake Timer）支持。它是采用 1 kHz 时钟的 32 位递减计数器（Down-Counter），可从低功耗模式唤醒芯片。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_WAKE_TIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_wake_timer:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_wake_timer#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MCUX_WAKE_TIMER_ALARM"></a>

## 68.54 `CONFIG_COUNTER_MCUX_WAKE_TIMER_ALARM`

**提示（Prompt）**：唤醒定时器告警支持（Wake Timer Alarm Support）

**说明（Help）**

唤醒定时器（Wake Timer）只有一个计数／重装寄存器（Count / Reload Register），因此周期性计数上限回调（TOP Callback）与单次告警（Single-Shot ALARM）需要使用同一硬件资源。受此限制，本 Kconfig 选项决定运行时可用的功能。

启用告警支持时，驱动仅支持相对单次告警（Relative Single-Shot Alarm）；绝对告警（Absolute Alarm）和设置 TOP 操作均返回 `-ENOTSUP`。禁用告警支持时，驱动不允许运行时设置或取消 ALARM，尝试这些操作会返回 `-ENOTSUP`。应根据应用需求选择配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_MCUX_WAKE_TIMER && CONFIG_COUNTER
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcux_wake_timer:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcux_wake_timer#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → MCUX 唤醒定时器驱动（Wake Timer Driver）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_MCUX_WAKE_TIMER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_MCUX_WAKE_TIMER)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MICROCHIP_MCP7940N"></a>

## 68.55 `CONFIG_COUNTER_MICROCHIP_MCP7940N`

**提示（Prompt）**：Microchip MCP7940N 实时时钟（RTC）

**说明（Help）**

启用基于 Microchip MCP7940N I2C 器件的实时时钟（RTC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MCP7940N_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mcp7940n:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mcp7940n#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_COUNTER_MICROCRYSTAL_RV3032_INIT_PRIORITY"></a>

## 68.56 `CONFIG_COUNTER_MICROCRYSTAL_RV3032_INIT_PRIORITY`

**提示（Prompt）**：rc3032c7 计数器初始化优先级（Counter Init Priority）

**说明（Help）**

Micro Crystal RV3032C7 计数器（Counter）驱动的初始化优先级。

译注：上游标题写为 `rc3032c7`，帮助正文写为 `rv3032c7`，此处保留两处原始标识并说明差异。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_RV3032 && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/counter/Kconfig.rv3032_counter:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.rv3032_counter#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → RV3032 计数器驱动（Counter Driver）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_RV3032`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_RV3032)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_MSPM0_TIMER"></a>

## 68.57 `CONFIG_COUNTER_MSPM0_TIMER`

**提示（Prompt）**：TI MSPM0 MCU 系列计数器驱动（Counter Driver）

**说明（Help）**

启用 TI MSPM0 微控制器（MCU）系列的计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_TIMER_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_MSPM0_DL_TIMER
```

**定义位置（Location）**：[`drivers/counter/Kconfig.mspm0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.mspm0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_USE_MSPM0_DL_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_MSPM0_DL_TIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_MSPM0_DL_TIMER`。

<a id="CONFIG_COUNTER_NATIVE_SIM"></a>

## 68.58 `CONFIG_COUNTER_NATIVE_SIM`

**提示（Prompt）**：使用 COUNTER_0 的计数器（Counter）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_NATIVE_SIM_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER_SUPPORTS_CAPTURE
```

**定义位置（Location）**：[`drivers/counter/Kconfig.native_sim:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.native_sim#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_SUPPORTS_CAPTURE`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_CAPTURE)。

<a id="CONFIG_COUNTER_NATIVE_SIM_FREQUENCY"></a>

## 68.59 `CONFIG_COUNTER_NATIVE_SIM_FREQUENCY`

**提示（Prompt）**：native_sim 计数器频率，单位为 Hz（Counter Frequency）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_NATIVE_SIM && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/counter/Kconfig.native_sim:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.native_sim#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → 使用 COUNTER_0 的计数器（Counter）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_NATIVE_SIM`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_NATIVE_SIM)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_NATIVE_SIM_NBR_CHANNELS"></a>

## 68.60 `CONFIG_COUNTER_NATIVE_SIM_NBR_CHANNELS`

**提示（Prompt）**：native_sim 计数器通道数量（Number of Channels）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_NATIVE_SIM && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/counter/Kconfig.native_sim:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.native_sim#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → 使用 COUNTER_0 的计数器（Counter）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_NATIVE_SIM`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_NATIVE_SIM)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_NEORV32_GPTMR"></a>

## 68.61 `CONFIG_COUNTER_NEORV32_GPTMR`

**提示（Prompt）**：NEORV32 GPTMR 驱动（Driver）

**说明（Help）**

启用 NEORV32 通用定时器（General Purpose Timer，GPTMR）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NEORV32_GPTMR_ENABLED && CONFIG_SYSCON && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.neorv32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.neorv32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_NPCX_LCT"></a>

## 68.62 `CONFIG_COUNTER_NPCX_LCT`

**提示（Prompt）**：NPCX 长倒计时定时器模块驱动（Long Countdown Timer Module Driver）

**说明（Help）**

启用 NPCX 长倒计时定时器模块（Long Countdown Timer Module，LCT）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NUVOTON_NPCX_LCT_V1_ENABLED || DT_HAS_NUVOTON_NPCX_LCT_V2_ENABLED || DT_HAS_NUVOTON_NPCK_LCT_ENABLED) && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER_NPCX_NPCXN_V1 if DT_HAS_NUVOTON_NPCX_LCT_V1_ENABLED
CONFIG_COUNTER_NPCX_NPCXN_V2 if DT_HAS_NUVOTON_NPCX_LCT_V2_ENABLED
CONFIG_COUNTER_NPCX_NPCKN if DT_HAS_NUVOTON_NPCK_LCT_ENABLED
```

**定义位置（Location）**：[`drivers/counter/Kconfig.npcx:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.npcx#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_NPCX_NPCXN_V1`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_NPCX_NPCXN_V1)、[`CONFIG_COUNTER_NPCX_NPCXN_V2`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_NPCX_NPCXN_V2)、[`CONFIG_COUNTER_NPCX_NPCKN`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_NPCX_NPCKN)。

<a id="CONFIG_COUNTER_NPCX_NPCKN"></a>

## 68.63 `CONFIG_COUNTER_NPCX_NPCKN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 NPCKn 变体启用长倒计时定时器（LCT）版本 1 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_NPCX_LCT
```

**定义位置（Location）**：[`drivers/counter/Kconfig.npcx:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.npcx#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_NPCX_LCT`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_NPCX_LCT)。

<a id="CONFIG_COUNTER_NPCX_NPCXN_V1"></a>

## 68.64 `CONFIG_COUNTER_NPCX_NPCXN_V1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 NPCXn 变体启用长倒计时定时器（LCT）版本 1 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_NPCX_LCT
```

**定义位置（Location）**：[`drivers/counter/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_NPCX_LCT`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_NPCX_LCT)。

<a id="CONFIG_COUNTER_NPCX_NPCXN_V2"></a>

## 68.65 `CONFIG_COUNTER_NPCX_NPCXN_V2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 NPCXn 变体启用长倒计时定时器（LCT）版本 2 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_NPCX_LCT
```

**定义位置（Location）**：[`drivers/counter/Kconfig.npcx:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.npcx#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_NPCX_LCT`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_NPCX_LCT)。

<a id="CONFIG_COUNTER_NXP_IRTC"></a>

## 68.66 `CONFIG_COUNTER_NXP_IRTC`

**提示（Prompt）**：恩智浦 IRTC 唤醒定时器计数器驱动（NXP Wake Timer Counter Driver）

**说明（Help）**

启用恩智浦（NXP）IRTC 唤醒定时器（Wake Timer）的计数器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IRTC_WAKE_TIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.nxp_irtc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.nxp_irtc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_NXP_MRT"></a>

## 68.67 `CONFIG_COUNTER_NXP_MRT`

**提示（Prompt）**：恩智浦 MRT 驱动（NXP Driver）

**说明（Help）**

启用恩智浦（NXP）多速率定时器（Multirate Timer，MRT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MRT_CHANNEL_ENABLED && DT_HAS_NXP_MRT_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RESET
```

**定义位置（Location）**：[`drivers/counter/Kconfig.nxp_mrt:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.nxp_mrt#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)。

<a id="CONFIG_COUNTER_NXP_PIT"></a>

## 68.68 `CONFIG_COUNTER_NXP_PIT`

**提示（Prompt）**：恩智浦 PIT 驱动（NXP Driver）

**说明（Help）**

启用恩智浦（NXP）周期中断定时器（Periodic Interrupt Timer，PIT）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PIT_CHANNEL_ENABLED && DT_HAS_NXP_PIT_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.nxp_pit:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.nxp_pit#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_NXP_S32_SYS_TIMER"></a>

## 68.69 `CONFIG_COUNTER_NXP_S32_SYS_TIMER`

**提示（Prompt）**：恩智浦 S32 系统定时器模块驱动（NXP System Timer Module Driver）

**说明（Help）**

启用恩智浦（NXP）S32 系统定时器模块（STM）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_SYS_TIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/counter/Kconfig.nxp_s32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.nxp_s32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_COUNTER_RA_AGT"></a>

## 68.70 `CONFIG_COUNTER_RA_AGT`

**提示（Prompt）**：瑞萨 RA AGT 驱动（Renesas Driver）

**说明（Help）**

启用瑞萨（Renesas）低功耗异步通用定时器（Low Power Asynchronous General Purpose Timer，AGT）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_AGT_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_AGT
```

**定义位置（Location）**：[`drivers/counter/Kconfig.renesas_ra:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.renesas_ra#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_USE_RA_FSP_AGT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_AGT)。

<a id="CONFIG_COUNTER_REALTEK_RTS5912"></a>

## 68.71 `CONFIG_COUNTER_REALTEK_RTS5912`

**提示（Prompt）**：瑞昱 RTS5912 系列计数器驱动（Realtek Counter Driver）

**说明（Help）**

启用瑞昱（Realtek）RTS5912 微控制器（MCU）系列的计数器（Counter）驱动，将 MCU 中的基本定时器（Basic Timer）暴露为设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_TIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.rts5912:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.rts5912#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_REALTEK_RTS5912_SLWTMR"></a>

## 68.72 `CONFIG_COUNTER_REALTEK_RTS5912_SLWTMR`

**提示（Prompt）**：瑞昱 RTS5912 系列低速定时器计数器驱动（Realtek Slow Timer Counter Driver）

**说明（Help）**

启用瑞昱（Realtek）RTS5912 微控制器（MCU）系列的计数器（Counter）驱动，将 MCU 中的低速定时器（Slow Timer）暴露为设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_SLWTIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.rts5912_slwtmr:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.rts5912_slwtmr#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_RENESAS_RA_ULPT"></a>

## 68.73 `CONFIG_COUNTER_RENESAS_RA_ULPT`

**提示（Prompt）**：瑞萨 RA ULPT 驱动（Renesas Driver）

**说明（Help）**

启用瑞萨（Renesas）RA 超低功耗定时器（Ultra-Low-Power Timer，ULPT）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_ULPT_COUNTER_ENABLED && !CONFIG_RENESAS_RA_ULPT_TIMER && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_ULPT
```

**定义位置（Location）**：[`drivers/counter/Kconfig.renesas_ra:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.renesas_ra#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RENESAS_RA_ULPT_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RENESAS_RA_ULPT_TIMER)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_USE_RA_FSP_ULPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_ULPT)。

<a id="CONFIG_COUNTER_RENESAS_RZA2M_OSTM"></a>

## 68.74 `CONFIG_COUNTER_RENESAS_RZA2M_OSTM`

**提示（Prompt）**：瑞萨 RZA2M OS 定时器计数器驱动（Renesas OSTM Counter Driver）

**说明（Help）**

启用瑞萨（Renesas）RZA2M 操作系统定时器（OS Timer，OSTM）的计数器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZA2M_OSTM_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.renesas_rz:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.renesas_rz#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_RENESAS_RZ_CMTW"></a>

## 68.75 `CONFIG_COUNTER_RENESAS_RZ_CMTW`

**提示（Prompt）**：瑞萨 RZ 比较匹配定时器 W 计数器驱动（Renesas CMTW Counter Driver）

**说明（Help）**

启用瑞萨（Renesas）RZ 比较匹配定时器 W（Compare Match Timer W，CMTW）的计数器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_CMTW_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_CMTW
```

**定义位置（Location）**：[`drivers/counter/Kconfig.renesas_rz:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.renesas_rz#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_USE_RZ_FSP_CMTW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_CMTW)。

<a id="CONFIG_COUNTER_RENESAS_RZ_GTM"></a>

## 68.76 `CONFIG_COUNTER_RENESAS_RZ_GTM`

**提示（Prompt）**：瑞萨 RZ 通用定时器计数器驱动（Renesas GTM Counter Driver）

**说明（Help）**

启用瑞萨（Renesas）RZ 通用定时器（General Timer，GTM）的计数器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_GTM_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_GTM
```

**定义位置（Location）**：[`drivers/counter/Kconfig.renesas_rz:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.renesas_rz#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_USE_RZ_FSP_GTM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_GTM)。

<a id="CONFIG_COUNTER_RPI_PICO_PIT"></a>

## 68.77 `CONFIG_COUNTER_RPI_PICO_PIT`

**提示（Prompt）**：树莓派 Pico PIT 驱动（RPI Pico PIT Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_PIT_CHANNEL_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PICOSDK_USE_PWM
```

**定义位置（Location）**：[`drivers/counter/Kconfig.rpi_pico_pit:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.rpi_pico_pit#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_PICOSDK_USE_PWM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_PWM)。

<a id="CONFIG_COUNTER_RTC_ESP32"></a>

## 68.78 `CONFIG_COUNTER_RTC_ESP32`

**提示（Prompt）**：基于 RTC 定时器的 ESP32 计数器驱动（Counter Driver）

**说明（Help）**

为 ESP32 系列器件启用基于乐鑫（Espressif）RTC 定时器的计数器（Counter）驱动 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_RTC_TIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.esp32_rtc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.esp32_rtc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_RTC_MAX32"></a>

## 68.79 `CONFIG_COUNTER_RTC_MAX32`

**提示（Prompt）**：MAX32xxx RTC 计数器驱动（Counter RTC Driver）

**说明（Help）**

启用 MAX32 微控制器（MCU）的实时时钟计数器（Counter RTC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_RTC_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.max32_rtc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.max32_rtc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_RTC_STM32"></a>

## 68.80 `CONFIG_COUNTER_RTC_STM32`

**提示（Prompt）**：STM32 RTC 计数器驱动（Counter RTC Driver）

**说明（Help）**

为 STM32 片上系统（SoC）构建实时时钟（RTC）驱动。已在 STM32 C0、F0、F2、F3、F4、F7、G0、G4、H7、L1、L4、L5、U5 系列上测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_RTC_ENABLED && !CONFIG_SOC_SERIES_STM32WB0X && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y if !CONFIG_RTC
```

**定义位置（Location）**：[`drivers/counter/Kconfig.stm32_rtc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.stm32_rtc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_RTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32WB0X`。

<a id="CONFIG_COUNTER_RTC_STM32_SAVE_VALUE_BETWEEN_RESETS"></a>

## 68.81 `CONFIG_COUNTER_RTC_STM32_SAVE_VALUE_BETWEEN_RESETS`

**提示（Prompt）**：跨复位保留 RTC 时间值（Preserve RTC Time）

**说明（Help）**

每次复位后保留计数器值（Counter Value）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_RTC_STM32 && CONFIG_COUNTER
```

**定义位置（Location）**：[`drivers/counter/Kconfig.stm32_rtc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.stm32_rtc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → STM32 RTC 计数器驱动（Counter RTC Driver）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_RTC_STM32`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_RTC_STM32)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_RTC_STM32_SUBSECONDS"></a>

## 68.82 `CONFIG_COUNTER_RTC_STM32_SUBSECONDS`

**提示（Prompt）**：使用亚秒计数作为基本时间刻度（Subseconds as Basic Tick）

**说明（Help）**

使用亚秒计数（Subseconds）作为基本时间刻度（Time Tick），以提高计数器分辨率（Resolution）。其频率是 RTC 源时钟频率除以 2，即经过第一级异步预分频器（Asynchronous Prescaler）后的时钟。此配置会增加功耗。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_STM32F1X && CONFIG_COUNTER_RTC_STM32 && CONFIG_COUNTER
```

**主动选择（Selects）**

```text
CONFIG_COUNTER_SUPPORTS_64BITS_TICKS
CONFIG_COUNTER_64BITS_TICKS
```

**定义位置（Location）**：[`drivers/counter/Kconfig.stm32_rtc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.stm32_rtc#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → STM32 RTC 计数器驱动（Counter RTC Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_COUNTER_RTC_STM32`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_RTC_STM32)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_SUPPORTS_64BITS_TICKS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_64BITS_TICKS)、[`CONFIG_COUNTER_64BITS_TICKS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_64BITS_TICKS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F1X`。

<a id="CONFIG_COUNTER_RV3028"></a>

## 68.83 `CONFIG_COUNTER_RV3028`

**提示（Prompt）**：Micro Crystal RV3028 计数器驱动（Counter Driver）

**说明（Help）**

启用 Micro Crystal RV3028 的计数器／定时器子驱动（Counter / Timer Child Driver），通过计数器 API 提供硬件定时器功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCRYSTAL_RV3028_COUNTER_ENABLED && DT_HAS_MICROCRYSTAL_RV3028_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/counter/Kconfig.rv3028_counter:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.rv3028_counter#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_COUNTER_RV3032"></a>

## 68.84 `CONFIG_COUNTER_RV3032`

**提示（Prompt）**：RV3032 计数器驱动（Counter Driver）

**说明（Help）**

启用虚拟计数器驱动（Dummy Counter Driver）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCRYSTAL_RV3032_COUNTER_ENABLED && DT_HAS_MICROCRYSTAL_RV3032_MFD_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/counter/Kconfig.rv3032_counter:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.rv3032_counter#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_COUNTER_SAM0_TC32"></a>

## 68.85 `CONFIG_COUNTER_SAM0_TC32`

**提示（Prompt）**：SAM0 系列 32 位基本定时器驱动（Basic Timer Driver）

**说明（Help）**

以 32 位宽模式启用 SAM0 系列定时器计数器（Timer Counter，TC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_TC32_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/counter/Kconfig.sam0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.sam0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_COUNTER_SAM_TC"></a>

## 68.86 `CONFIG_COUNTER_SAM_TC`

**提示（Prompt）**：Atmel SAM MCU 系列计数器 TC 驱动（Counter Driver）

**说明（Help）**

启用 Atmel SAM 微控制器（MCU）系列的计数器（TC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_TC_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/counter/Kconfig.sam:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.sam#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_COUNTER_SHELL"></a>

## 68.87 `CONFIG_COUNTER_SHELL`

**提示（Prompt）**：计数器命令行（Counter Shell）

**说明（Help）**

启用计数器（Counter）和定时器（Timer）的命令行（Shell）命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_COUNTER
```

**定义位置（Location）**：[`drivers/counter/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_SILABS_BURTC"></a>

## 68.88 `CONFIG_COUNTER_SILABS_BURTC`

**提示（Prompt）**：Silicon Labs 备份定时器计数器驱动（BURTC Counter Driver）

**说明（Help）**

启用 Silicon Labs 芯片备份实时时钟计数器（Backup Real Time Counter）模块的计数器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_BURTC_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_BURTC
```

**定义位置（Location）**：[`drivers/counter/Kconfig.silabs:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.silabs#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_SILABS_SISDK_BURTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_BURTC)。

<a id="CONFIG_COUNTER_SILABS_BURTC_ALARM"></a>

## 68.89 `CONFIG_COUNTER_SILABS_BURTC_ALARM`

**提示（Prompt）**：BURTC 告警支持（Alarm Support）

**说明（Help）**

备份实时时钟计数器（BURTC）是许多 Silicon Labs 微控制器（MCU）常用的唤醒源（Wake-Up Source），也可作为 Cortex-M 系统滴答定时器（SysTick）的配套低功耗定时器。启用单次告警（Single-Shot Alarm）需要重新配置硬件比较寄存器 `COMP`，而周期性计数上限回调（TOP Callback）也使用同一资源。

受此硬件限制，本 Kconfig 选项决定是否启用告警支持：启用时，驱动不允许运行时设置 TOP，尝试设置会返回 `-ENOTSUP`；禁用时，不允许运行时设置或取消 ALARM，尝试这些操作会返回 `-ENOTSUP`。应根据应用需求选择配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_SILABS_BURTC && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.silabs:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.silabs#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → Silicon Labs 备份定时器计数器驱动（BURTC Counter Driver）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_SILABS_BURTC`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SILABS_BURTC)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_SILABS_PROTIMER"></a>

## 68.90 `CONFIG_COUNTER_SILABS_PROTIMER`

**提示（Prompt）**：Silicon Labs PROTIMER 计数器驱动（Counter Driver）

**说明（Help）**

启用 Silicon Labs PROTIMER 外设的计数器（Counter）驱动，该外设用作 RAIL 定时器。启用 `BUILD_ONLY_NO_BLOBS` 时，例如某些 Twister 构建，使用不具备实际功能的桩（Stub），驱动无法在设备上工作。

使用 RAIL 二进制块（Blob）构建时，必须启用 `SOC_GECKO_USE_RAIL`，且 RAIL 必须先完成初始化。PROTIMER 位于无线电模块（Radio Block）中，其时钟直到 RAIL 初始化时才启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_FAMILY_SILABS_S2 || CONFIG_SOC_FAMILY_SILABS_S3) && DT_HAS_SILABS_PROTIMER_ENABLED && (CONFIG_BUILD_ONLY_NO_BLOBS || (CONFIG_ZEPHYR_HAL_SILABS_MODULE_BLOBS && CONFIG_SOC_GECKO_USE_RAIL)) && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.silabs:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.silabs#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)、[`CONFIG_BUILD_ONLY_NO_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_ONLY_NO_BLOBS)、[`CONFIG_ZEPHYR_HAL_SILABS_MODULE_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_SILABS_MODULE_BLOBS)、[`CONFIG_SOC_GECKO_USE_RAIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GECKO_USE_RAIL)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`、`CONFIG_SOC_FAMILY_SILABS_S3`、`CONFIG_ZEPHYR_HAL_SILABS_MODULE_BLOBS`。

<a id="CONFIG_COUNTER_SILABS_TIMER"></a>

## 68.91 `CONFIG_COUNTER_SILABS_TIMER`

**提示（Prompt）**：Silicon Labs Series 2 TIMER 计数器驱动（Counter Driver）

**说明（Help）**

启用基于 Silicon Labs TIMER 外设的计数器（Counter）驱动。该驱动在 Silicon Labs Series 2 片上系统（SoC）上使用 TIMER，支持带比较匹配告警（Compare-Match Alarm）的计数器模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_TIMER_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_TIMER
```

**定义位置（Location）**：[`drivers/counter/Kconfig.silabs:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.silabs#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_SILABS_SISDK_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_TIMER)。

<a id="CONFIG_COUNTER_SMARTBOND_TIMER"></a>

## 68.92 `CONFIG_COUNTER_SMARTBOND_TIMER`

**提示（Prompt）**：瑞萨 SmartBond™ 计数器驱动（Renesas Counter Driver）

**说明（Help）**

启用瑞萨（Renesas）SmartBond™ 处理器系列的计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_TIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_SMARTBOND
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/counter/Kconfig.smartbond_timer:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.smartbond_timer#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_CLOCK_CONTROL_SMARTBOND`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_SMARTBOND)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_COUNTER_SNPS_DW"></a>

## 68.93 `CONFIG_COUNTER_SNPS_DW`

**提示（Prompt）**：新思科技 DesignWare 定时器驱动（Synopsys Timer Driver）

**说明（Help）**

启用定时器（Timer）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DW_TIMERS_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.dw:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.dw#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_SUPPORTS_64BITS_TICKS"></a>

## 68.94 `CONFIG_COUNTER_SUPPORTS_64BITS_TICKS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果计数器（Counter）驱动支持使用 64 位表示计数刻度（Tick），则选择此项。通常由需要超过 32 位限制的扩展计数范围的驱动设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER
```

**被选择（Selected by）**

```text
CONFIG_ACE_V1X_ART_COUNTER
CONFIG_ACE_V1X_RTC_COUNTER
CONFIG_COUNTER_CC23X0_RTC
CONFIG_COUNTER_TMR_ESP32
CONFIG_COUNTER_MCUX_TSTMR
CONFIG_COUNTER_RTC_STM32_SUBSECONDS
```

**定义位置（Location）**：[`drivers/counter/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_ACE_V1X_ART_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_ACE_V1X_ART_COUNTER)、[`CONFIG_ACE_V1X_RTC_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_ACE_V1X_RTC_COUNTER)、[`CONFIG_COUNTER_CC23X0_RTC`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_CC23X0_RTC)、[`CONFIG_COUNTER_TMR_ESP32`](P069_drivers_counter_配置项参考_2.md#CONFIG_COUNTER_TMR_ESP32)、[`CONFIG_COUNTER_MCUX_TSTMR`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_MCUX_TSTMR)、[`CONFIG_COUNTER_RTC_STM32_SUBSECONDS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_RTC_STM32_SUBSECONDS)。

<a id="CONFIG_COUNTER_SUPPORTS_CAPTURE"></a>

## 68.95 `CONFIG_COUNTER_SUPPORTS_CAPTURE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果计数器（Counter）驱动支持计数器捕获（Counter Capture）API，则选择此项。应由驱动设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_TMR_ESP32
CONFIG_COUNTER_MCUX_CTIMER
CONFIG_COUNTER_MCUX_GPT
CONFIG_COUNTER_MCUX_QTMR
CONFIG_COUNTER_MCUX_TPM
CONFIG_COUNTER_NATIVE_SIM
CONFIG_COUNTER_TIMER_STM32
```

**定义位置（Location）**：[`drivers/counter/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_TMR_ESP32`](P069_drivers_counter_配置项参考_2.md#CONFIG_COUNTER_TMR_ESP32)、[`CONFIG_COUNTER_MCUX_CTIMER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_MCUX_CTIMER)、[`CONFIG_COUNTER_MCUX_GPT`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_MCUX_GPT)、[`CONFIG_COUNTER_MCUX_QTMR`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_MCUX_QTMR)、[`CONFIG_COUNTER_MCUX_TPM`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_MCUX_TPM)、[`CONFIG_COUNTER_NATIVE_SIM`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_NATIVE_SIM)、[`CONFIG_COUNTER_TIMER_STM32`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_TIMER_STM32)。

<a id="CONFIG_COUNTER_TIMER_GD32"></a>

## 68.96 `CONFIG_COUNTER_TIMER_GD32`

**提示（Prompt）**：GD32 定时器计数器驱动（Timer Counter Driver）

**说明（Help）**

启用 GD32 系列器件的定时器计数器（Counter Timer）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_TIMER_ENABLED && !CONFIG_SOC_SERIES_GD32VF103 && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_GD32_TIMER
```

**定义位置（Location）**：[`drivers/counter/Kconfig.gd32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.gd32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_USE_GD32_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_GD32_TIMER)。

<a id="CONFIG_COUNTER_TIMER_MAX32"></a>

## 68.97 `CONFIG_COUNTER_TIMER_MAX32`

**提示（Prompt）**：MAX32xxx 计数器驱动（Counter Driver）

**说明（Help）**

启用 MAX32 微控制器（MCU）的计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/counter/Kconfig.max32_timer:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.max32_timer#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_COUNTER_TIMER_STM32"></a>

## 68.98 `CONFIG_COUNTER_TIMER_STM32`

**提示（Prompt）**：STM32 计数器驱动（Counter Driver）

**说明（Help）**

启用 STM32 处理器系列的计数器（Counter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RESET
CONFIG_PINCTRL if CONFIG_COUNTER_CAPTURE
CONFIG_COUNTER_SUPPORTS_CAPTURE
```

**定义位置（Location）**：[`drivers/counter/Kconfig.stm32_timer:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.stm32_timer#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_COUNTER_CAPTURE`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_CAPTURE)、[`CONFIG_COUNTER_SUPPORTS_CAPTURE`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_CAPTURE)。

<a id="CONFIG_COUNTER_TI_K3_RTC"></a>

## 68.99 `CONFIG_COUNTER_TI_K3_RTC`

**提示（Prompt）**：TI K3 片上系统的 RTC 计数器驱动（RTC Counter Driver）

**说明（Help）**

启用 TI K3 片上系统（SoC）的实时时钟（RTC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_K3_RTC_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.k3_rtc_counter:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.k3_rtc_counter#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_TMR_AMEBA"></a>

## 68.100 `CONFIG_COUNTER_TMR_AMEBA`

**提示（Prompt）**：基于基本定时器的 AMEBA 计数器驱动（Basic-Timer Counter Driver）

**说明（Help）**

为 AMEBA 系列器件启用基于瑞昱（Realtek）基本定时器（Basic Timer）的计数器（Counter）驱动 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.ameba_tmr:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.ameba_tmr#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<!-- kconfig-navigation -->

[上一章](P067_drivers_coredump_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P069_drivers_counter_配置项参考_2.md)
