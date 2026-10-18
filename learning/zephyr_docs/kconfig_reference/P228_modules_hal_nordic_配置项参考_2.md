---
id: learning.zephyr-docs.kconfig-reference.page-228
title: "`modules/hal_nordic`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第228章\_`modules/hal_nordic`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `modules/hal_nordic` 的 84 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NRFX_QSPI_LOG"></a>

## 228.1 `CONFIG_NRFX_QSPI_LOG`

**提示（Prompt）**：四线串行外设接口（QSPI）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_QSPI && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_QSPI`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_QSPI)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_RNG"></a>

## 228.2 `CONFIG_NRFX_RNG`

**提示（Prompt）**：随机数生成器（RNG）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L203)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

<a id="CONFIG_NRFX_RNG_LOG"></a>

## 228.3 `CONFIG_NRFX_RNG_LOG`

**提示（Prompt）**：随机数生成器（RNG）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_RNG && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_RNG`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_RNG)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_RRAMC"></a>

## 228.4 `CONFIG_NRFX_RRAMC`

**提示（Prompt）**：RRAMC 驱动（driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_NRF_RRAM
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)。

<a id="CONFIG_NRFX_RTC"></a>

## 228.5 `CONFIG_NRFX_RTC`

**提示（Prompt）**：实时时钟（RTC）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_RTC_LOG"></a>

## 228.6 `CONFIG_NRFX_RTC_LOG`

**提示（Prompt）**：实时时钟（RTC）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_RTC && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_RTC`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_RTC)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_SAADC"></a>

## 228.7 `CONFIG_NRFX_SAADC`

**提示（Prompt）**：逐次逼近模数转换器（SAADC）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n && !CONFIG_SOC_SERIES_NRF51 && CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_ADC_NRFX_SAADC
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_ADC_NRFX_SAADC`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NRFX_SAADC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_SAADC_LOG"></a>

## 228.8 `CONFIG_NRFX_SAADC_LOG`

**提示（Prompt）**：逐次逼近模数转换器（SAADC）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_SAADC && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_SAADC`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_SAADC)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_SPI"></a>

## 228.9 `CONFIG_NRFX_SPI`

**提示（Prompt）**：串行外设接口（SPI）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_SPI_NRFX_SPI
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_SPI_NRFX_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NRFX_SPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_SPI_NRFX_SPI`。

<a id="CONFIG_NRFX_SPIM"></a>

## 228.10 `CONFIG_NRFX_SPIM`

**提示（Prompt）**：SPI 主端（SPIM）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_SPI_NRFX_SPIM
CONFIG_SPI_NRFX_SPIM_RTIO
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NRFX_SPIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NRFX_SPIM)、[`CONFIG_SPI_NRFX_SPIM_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NRFX_SPIM_RTIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SPI_NRFX_SPIM`、`CONFIG_SPI_NRFX_SPIM_RTIO`。

<a id="CONFIG_NRFX_SPIM_LOG"></a>

## 228.11 `CONFIG_NRFX_SPIM_LOG`

**提示（Prompt）**：SPI 主端（SPIM）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_SPIM && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_SPIM`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_SPIM)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_SPIS"></a>

## 228.12 `CONFIG_NRFX_SPIS`

**提示（Prompt）**：SPI 从端（SPIS）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_SPI_NRFX_SPIS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:225`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L225)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NRFX_SPIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NRFX_SPIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SPI_NRFX_SPIS`。

<a id="CONFIG_NRFX_SPIS_LOG"></a>

## 228.13 `CONFIG_NRFX_SPIS_LOG`

**提示（Prompt）**：SPI 从端（SPIS）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_SPIS && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_SPIS`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_SPIS)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_SPI_LOG"></a>

## 228.14 `CONFIG_NRFX_SPI_LOG`

**提示（Prompt）**：串行外设接口（SPI）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_SPI && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_SPI`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_SPI)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_SYSTICK"></a>

## 228.15 `CONFIG_NRFX_SYSTICK`

**提示（Prompt）**：系统滴答（SYSTICK）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M_HAS_SYSTICK && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M_HAS_SYSTICK`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_SYSTICK)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_SYSTICK_LOG"></a>

## 228.16 `CONFIG_NRFX_SYSTICK_LOG`

**提示（Prompt）**：系统滴答（SYSTICK）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_SYSTICK && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_SYSTICK`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_SYSTICK)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_TBM"></a>

## 228.17 `CONFIG_NRFX_TBM`

**提示（Prompt）**：TBM 驱动（driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L233)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

<a id="CONFIG_NRFX_TDM"></a>

## 228.18 `CONFIG_NRFX_TDM`

**提示（Prompt）**：时分复用（TDM）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:237`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L237)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_TEMP"></a>

## 228.19 `CONFIG_NRFX_TEMP`

**提示（Prompt）**：温度（TEMP）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:240`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L240)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

<a id="CONFIG_NRFX_TEMP_LOG"></a>

## 228.20 `CONFIG_NRFX_TEMP_LOG`

**提示（Prompt）**：温度（TEMP）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_TEMP && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_TEMP`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_TEMP)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_TIMER"></a>

## 228.21 `CONFIG_NRFX_TIMER`

**提示（Prompt）**：定时器（TIMER）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:244`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L244)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_TIMER_LOG"></a>

## 228.22 `CONFIG_NRFX_TIMER_LOG`

**提示（Prompt）**：定时器（TIMER）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_TIMER && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_TIMER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_TIMER)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_TWI"></a>

## 228.23 `CONFIG_NRFX_TWI`

**提示（Prompt）**：双线接口（TWI）外设的 NRFX 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_I2C_NRFX_TWI
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:247`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L247)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_I2C_NRFX_TWI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_NRFX_TWI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_I2C_NRFX_TWI`。

<a id="CONFIG_NRFX_TWIM"></a>

## 228.24 `CONFIG_NRFX_TWIM`

**提示（Prompt）**：双线接口主端（TWIM）外设的 NRFX 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_I2C_NRFX_TWIM
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_I2C_NRFX_TWIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_NRFX_TWIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_I2C_NRFX_TWIM`。

<a id="CONFIG_NRFX_TWIM_LOG"></a>

## 228.25 `CONFIG_NRFX_TWIM_LOG`

**提示（Prompt）**：双线接口主端（TWIM）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_TWIM && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_TWIM`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_TWIM)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_TWIS"></a>

## 228.26 `CONFIG_NRFX_TWIS`

**提示（Prompt）**：双线接口从端（TWIS）外设的 NRFX 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_I2C_NRFX_TWIS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L253)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_I2C_NRFX_TWIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_NRFX_TWIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_I2C_NRFX_TWIS`。

<a id="CONFIG_NRFX_TWIS_LOG"></a>

## 228.27 `CONFIG_NRFX_TWIS_LOG`

**提示（Prompt）**：双线接口从端（TWIS）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_TWIS && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_TWIS`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_TWIS)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_TWI_LOG"></a>

## 228.28 `CONFIG_NRFX_TWI_LOG`

**提示（Prompt）**：双线接口（TWI）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_TWI && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_TWI`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_TWI)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_UART"></a>

## 228.29 `CONFIG_NRFX_UART`

**提示（Prompt）**：通用异步收发器（UART）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_UARTE"></a>

## 228.30 `CONFIG_NRFX_UARTE`

**提示（Prompt）**：UARTE 驱动（driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:259`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L259)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_UARTE_CONFIG_RX_CACHE_ENABLED"></a>

## 228.31 `CONFIG_NRFX_UARTE_CONFIG_RX_CACHE_ENABLED`

**提示（Prompt）**：UARTE 接收缓存支持（RX caching support）

**说明（Help）**

当平台限制接收器可写入的数据地址时，可以启用此功能。启用后，DMA 传输使用驱动内部缓冲区（cache buffers），随后将数据复制到用户缓冲区（user buffer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_UARTE && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:274`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L274)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → UARTE 驱动（driver）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_UARTE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_UARTE)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_UARTE_CONFIG_SKIP_GPIO_CONFIG"></a>

## 228.32 `CONFIG_NRFX_UARTE_CONFIG_SKIP_GPIO_CONFIG`

**提示（Prompt）**：UARTE 通用输入／输出配置支持（GPIO configuration support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_UARTE && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:262`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L262)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → UARTE 驱动（driver）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_UARTE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_UARTE)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_UARTE_CONFIG_SKIP_PSEL_CONFIG"></a>

## 228.33 `CONFIG_NRFX_UARTE_CONFIG_SKIP_PSEL_CONFIG`

**提示（Prompt）**：UARTE 引脚选择配置支持（PSEL configuration support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_UARTE && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:266`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L266)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → UARTE 驱动（driver）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_UARTE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_UARTE)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_UARTE_CONFIG_TX_LINK"></a>

## 228.34 `CONFIG_NRFX_UARTE_CONFIG_TX_LINK`

**提示（Prompt）**：UARTE 发送传输链接支持（TX transfer linking support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_UARTE && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:270`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L270)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → UARTE 驱动（driver）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_UARTE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_UARTE)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_UARTE_LOG"></a>

## 228.35 `CONFIG_NRFX_UARTE_LOG`

**提示（Prompt）**：UARTE 驱动日志（driver logging）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_UARTE && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_UARTE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_UARTE)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_UART_LOG"></a>

## 228.36 `CONFIG_NRFX_UART_LOG`

**提示（Prompt）**：通用异步收发器（UART）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_UART && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_UART`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_UART)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_USBREG"></a>

## 228.37 `CONFIG_NRFX_USBREG`

**提示（Prompt）**：USBREG 驱动（driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:282`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L282)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

<a id="CONFIG_NRFX_USBREG_LOG"></a>

## 228.38 `CONFIG_NRFX_USBREG_LOG`

**提示（Prompt）**：USBREG 驱动日志（driver logging）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_USBREG && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_USBREG`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_USBREG)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_WDT"></a>

## 228.39 `CONFIG_NRFX_WDT`

**提示（Prompt）**：看门狗定时器（WDT）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_WDT_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:286`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L286)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_WDT_NRFX`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_WDT_LOG"></a>

## 228.40 `CONFIG_NRFX_WDT_LOG`

**提示（Prompt）**：看门狗定时器（WDT）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_WDT && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_WDT`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_WDT)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRF_802154_ASSERT_CHOICE"></a>

## 228.41 `CONFIG_NRF_802154_ASSERT_CHOICE`

**提示（Prompt）**：nRF 802.15.4 断言实现（assert implementation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_RADIO_DRIVER || CONFIG_NRF_802154_SERIALIZATION) && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_NRF_802154_ASSERT_ZEPHYR_MINIMAL
```

**可选项（Choices）**

```text
CONFIG_NRF_802154_ASSERT_ZEPHYR_MINIMAL
CONFIG_NRF_802154_ASSERT_ZEPHYR
CONFIG_NRF_802154_ASSERT_ZEPHYR_MINIMAL
CONFIG_NRF_802154_ASSERT_ZEPHYR
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L234)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_NRF_802154_ASSERT_ZEPHYR_MINIMAL`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_ASSERT_ZEPHYR_MINIMAL)、[`CONFIG_NRF_802154_ASSERT_ZEPHYR`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_ASSERT_ZEPHYR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_ASSERT_ZEPHYR"></a>

## 228.42 `CONFIG_NRF_802154_ASSERT_ZEPHYR`

**提示（Prompt）**：将 nRF 802.15.4 无线电驱动断言用作 Zephyr 标准 `__ASERT_NO_MSG`（原文拼写）

**说明（Help）**

nRF 802.15.4 无线电驱动（Radio Driver）的运行时检查完全依赖 `__ASSERT_NO_MSG` 宏的配置，包括完全关闭运行时检查的能力。

译注：对应提示原文写作 `__ASERT_NO_MSG`，本段帮助写作 `__ASSERT_NO_MSG`，两者拼写不同；此处保留来源差异。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_802154_ASSERT_CHOICE>
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:248`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L248)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → nRF 802.15.4 断言实现（assert implementation）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_ASSERT_CHOICE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_ASSERT_CHOICE)。

<a id="CONFIG_NRF_802154_ASSERT_ZEPHYR_MINIMAL"></a>

## 228.43 `CONFIG_NRF_802154_ASSERT_ZEPHYR_MINIMAL`

**提示（Prompt）**：nRF 802.15.4 最小断言（minimal assertions）

**说明（Help）**

即使内核级 `CONFIG_ASSERT` 已禁用，仍对 nRF 802.15.4 无线电驱动（Radio Driver）的运行提供最小运行时检查。异常情况下调用 `nrf_802154_assert_handler()`。为节省镜像内存，不提供文件名和行号调试信息。`nrf_802154_assert_handler` 的默认实现调用 `k_panic`／`k_oops`，并允许进一步调整行为；也可自行提供该函数的实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_802154_ASSERT_CHOICE>
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:238`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L238)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → nRF 802.15.4 断言实现（assert implementation）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_ASSERT_CHOICE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_ASSERT_CHOICE)。

<a id="CONFIG_NRF_802154_CARRIER_FUNCTIONS"></a>

## 228.44 `CONFIG_NRF_802154_CARRIER_FUNCTIONS`

**提示（Prompt）**：nRF 802.15.4 载波功能（carrier functions）

**说明（Help）**

启用调制载波（modulated carrier）和连续载波（continuous carrier）等功能。如果在多核 SoC 上修改此项，远端对应配置必须设为完全相同的值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_RADIO_DRIVER || CONFIG_NRF_802154_SERIALIZATION) && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_OPENTHREAD_DIAG || CONFIG_IEEE802154_CARRIER_FUNCTIONS
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_OPENTHREAD_DIAG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_DIAG)、[`CONFIG_IEEE802154_CARRIER_FUNCTIONS`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CARRIER_FUNCTIONS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_CCA_CORR_LIMIT"></a>

## 228.45 `CONFIG_NRF_802154_CCA_CORR_LIMIT`

**提示（Prompt）**：nRF IEEE 802.15.4 空闲信道评估相关器计数限制（CCA Correlator limit）

**说明（Help）**

超过相关器阈值（correlator threshold）的出现次数限制。非零时，启用基于相关器的信号检测（correlator-based signal detection）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_RADIO_DRIVER || CONFIG_NRF_802154_SERIALIZATION) && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_CCA_CORR_THRESHOLD"></a>

## 228.46 `CONFIG_NRF_802154_CCA_CORR_THRESHOLD`

**提示（Prompt）**：nRF IEEE 802.15.4 空闲信道评估相关器阈值（CCA Correlator threshold）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_RADIO_DRIVER || CONFIG_NRF_802154_SERIALIZATION) && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
45
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_CCA_ED_THRESHOLD_DBM"></a>

## 228.47 `CONFIG_NRF_802154_CCA_ED_THRESHOLD_DBM`

**提示（Prompt）**：nRF IEEE 802.15.4 空闲信道评估能量检测阈值（CCA Energy Detection threshold），单位为 dBm

**说明（Help）**

如果在给定信道检测到的能量超过此值，则认为该信道忙（busy）。单位为 dBm。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_RADIO_DRIVER || CONFIG_NRF_802154_SERIALIZATION) && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
-75
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_CCA_MODE"></a>

## 228.48 `CONFIG_NRF_802154_CCA_MODE`

**提示（Prompt）**：nRF IEEE 802.15.4 空闲信道评估模式（CCA mode）

**说明（Help）**

空闲信道评估模式（CCA mode）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_RADIO_DRIVER || CONFIG_NRF_802154_SERIALIZATION) && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_NRF_802154_CCA_MODE_ED
```

**可选项（Choices）**

```text
CONFIG_NRF_802154_CCA_MODE_ED
CONFIG_NRF_802154_CCA_MODE_CARRIER
CONFIG_NRF_802154_CCA_MODE_CARRIER_AND_ED
CONFIG_NRF_802154_CCA_MODE_CARRIER_OR_ED
CONFIG_NRF_802154_CCA_MODE_ED
CONFIG_NRF_802154_CCA_MODE_CARRIER
CONFIG_NRF_802154_CCA_MODE_CARRIER_AND_ED
CONFIG_NRF_802154_CCA_MODE_CARRIER_OR_ED
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_NRF_802154_CCA_MODE_ED`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_CCA_MODE_ED)、[`CONFIG_NRF_802154_CCA_MODE_CARRIER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_CCA_MODE_CARRIER)、[`CONFIG_NRF_802154_CCA_MODE_CARRIER_AND_ED`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_CCA_MODE_CARRIER_AND_ED)、[`CONFIG_NRF_802154_CCA_MODE_CARRIER_OR_ED`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_CCA_MODE_CARRIER_OR_ED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_CCA_MODE_CARRIER"></a>

## 228.49 `CONFIG_NRF_802154_CCA_MODE_CARRIER`

**提示（Prompt）**：检测到载波（Carrier Seen）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_802154_CCA_MODE>
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → nRF IEEE 802.15.4 空闲信道评估模式（CCA mode）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_CCA_MODE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_CCA_MODE)。

<a id="CONFIG_NRF_802154_CCA_MODE_CARRIER_AND_ED"></a>

## 228.50 `CONFIG_NRF_802154_CCA_MODE_CARRIER_AND_ED`

**提示（Prompt）**：能量高于阈值且检测到载波（Energy Above Threshold AND Carrier Seen）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_802154_CCA_MODE>
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → nRF IEEE 802.15.4 空闲信道评估模式（CCA mode）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_CCA_MODE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_CCA_MODE)。

<a id="CONFIG_NRF_802154_CCA_MODE_CARRIER_OR_ED"></a>

## 228.51 `CONFIG_NRF_802154_CCA_MODE_CARRIER_OR_ED`

**提示（Prompt）**：能量高于阈值或检测到载波（Energy Above Threshold OR Carrier Seen）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_802154_CCA_MODE>
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → nRF IEEE 802.15.4 空闲信道评估模式（CCA mode）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_CCA_MODE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_CCA_MODE)。

<a id="CONFIG_NRF_802154_CCA_MODE_ED"></a>

## 228.52 `CONFIG_NRF_802154_CCA_MODE_ED`

**提示（Prompt）**：能量高于阈值（Energy Above Threshold）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_802154_CCA_MODE>
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → nRF IEEE 802.15.4 空闲信道评估模式（CCA mode）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_CCA_MODE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_CCA_MODE)。

<a id="CONFIG_NRF_802154_CONSTLAT_CONTROL"></a>

## 228.53 `CONFIG_NRF_802154_CONSTLAT_CONTROL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

允许 nRF 802.15.4 无线电驱动（radio driver）管理恒定延迟状态（constant latency state）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF54L && CONFIG_NRF_802154_SL_OPENSOURCE && CONFIG_NRF_802154_RADIO_DRIVER && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRF_SYS_EVENT
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → NRF IEEE 802.15.4 无线电驱动（radio driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_NRF_802154_SL_OPENSOURCE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SL_OPENSOURCE)、[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_NRF_SYS_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_SYS_EVENT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_ENCRYPTION"></a>

## 228.54 `CONFIG_NRF_802154_ENCRYPTION`

**提示（Prompt）**：nRF 802.15.4 AES-CCM* 认证与加密（authentication & encryption）

**说明（Help）**

启用对发出帧和确认帧（Acks）进行加密与认证（encryption and authentication）的模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_CRYPTO_NRF_ECB && (CONFIG_NRF_802154_RADIO_DRIVER || CONFIG_NRF_802154_SERIALIZATION) && CONFIG_HAS_NORDIC_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_NRF_802154_IE_WRITER
CONFIG_NRF_802154_SECURITY_WRITER
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L203)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_NRF_ECB`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_NRF_ECB)、[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_NRF_802154_IE_WRITER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_IE_WRITER)、[`CONFIG_NRF_802154_SECURITY_WRITER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SECURITY_WRITER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_IE_WRITER"></a>

## 228.55 `CONFIG_NRF_802154_IE_WRITER`

**提示（Prompt）**：信息元素写入器（Information element writer）

**说明（Help）**

对某些信息元素（Information Element）类型启用数据注入（data injection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_RADIO_DRIVER || CONFIG_NRF_802154_SERIALIZATION) && CONFIG_HAS_NORDIC_DRIVERS
```

**被选择（Selected by）**

```text
CONFIG_NRF_802154_ENCRYPTION
CONFIG_NRF_802154_ENCRYPTION
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_NRF_802154_ENCRYPTION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_ENCRYPTION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_MULTIPROTOCOL_SUPPORT"></a>

## 228.56 `CONFIG_NRF_802154_MULTIPROTOCOL_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在动态多协议应用（dynamic multiprotocol applications）中，必须由仲裁器（arbiter）分配无线电外设的访问权。为使驱动支持这种仲裁，必须启用此项；否则，驱动假定无线电外设访问权无限期授予自身。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_802154_RADIO_DRIVER && CONFIG_HAS_NORDIC_DRIVERS
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → NRF IEEE 802.15.4 无线电驱动（radio driver）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_PENDING_EXTENDED_ADDRESSES"></a>

## 228.57 `CONFIG_NRF_802154_PENDING_EXTENDED_ADDRESSES`

**提示（Prompt）**：nRF 802.15.4 待处理数据的扩展地址（pending extended addresses）

**说明（Help）**

用于保存有待处理数据（pending data）的节点扩展地址（extended addresses）的槽位数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_RADIO_DRIVER || CONFIG_NRF_802154_SERIALIZATION) && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:197`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L197)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_PENDING_SHORT_ADDRESSES"></a>

## 228.58 `CONFIG_NRF_802154_PENDING_SHORT_ADDRESSES`

**提示（Prompt）**：nRF 802.15.4 待处理数据的短地址（pending short addresses）

**说明（Help）**

用于保存有待处理数据（pending data）的节点短地址（short addresses）的槽位数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_RADIO_DRIVER || CONFIG_NRF_802154_SERIALIZATION) && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L191)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_RADIO_DRIVER"></a>

## 228.59 `CONFIG_NRF_802154_RADIO_DRIVER`

**提示（Prompt）**：NRF IEEE 802.15.4 无线电驱动（radio driver）

**说明（Help）**

在 Zephyr 中启用 nRF IEEE 802.15.4 无线电驱动（radio driver）。注意：除无线电外设本身外，此驱动还占用若干其他外设，完整列表见 `hal_nordic` 仓库中的 `drivers/nrf_radio_802154/nrf_802154_peripherals.h`。驱动定义了中断请求配置抽象层（IRQ configuration abstraction layer）API，其 Zephyr 专用实现使用动态中断（dynamic interrupts），因此会无条件选择 `DYNAMIC_INTERRUPTS`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_RADIO_IEEE802154 && !n && CONFIG_HAS_NORDIC_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_DYNAMIC_INTERRUPTS
CONFIG_ENTROPY_GENERATOR
CONFIG_CLOCK_CONTROL
```

**被选择（Selected by）**

```text
CONFIG_NRF_802154_SER_RADIO
CONFIG_NRF_802154_SER_RADIO
CONFIG_IEEE802154_NRF5
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_RADIO_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_RADIO_IEEE802154)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_NRF_802154_SER_RADIO`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SER_RADIO)、[`CONFIG_IEEE802154_NRF5`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_RADIO_IEEE802154`、`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_RX_BUFFERS"></a>

## 228.60 `CONFIG_NRF_802154_RX_BUFFERS`

**提示（Prompt）**：nRF 802.15.4 接收缓冲区（receive buffers）

**说明（Help）**

nRF 802.15.4 驱动序列化主机（serialization host）的接收队列缓冲区数量。修改此值时，远端对应配置必须设为完全相同的值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_RADIO_DRIVER || CONFIG_NRF_802154_SERIALIZATION) && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_SECURITY_KEY_STORAGE_SIZE"></a>

## 228.61 `CONFIG_NRF_802154_SECURITY_KEY_STORAGE_SIZE`

**提示（Prompt）**：nRF 802.15.4 安全密钥存储容量（security key storage size）

**说明（Help）**

nRF 802.15.4 无线电驱动（Radio Driver）可同时保存的加密密钥（encryption keys）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_RADIO_DRIVER || CONFIG_NRF_802154_SERIALIZATION) && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_SECURITY_WRITER"></a>

## 228.62 `CONFIG_NRF_802154_SECURITY_WRITER`

**提示（Prompt）**：安全帧计数器写入器（Security frame counter writer）

**说明（Help）**

启用安全帧计数器（security frame counter）注入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_RADIO_DRIVER || CONFIG_NRF_802154_SERIALIZATION) && CONFIG_HAS_NORDIC_DRIVERS
```

**被选择（Selected by）**

```text
CONFIG_NRF_802154_ENCRYPTION
CONFIG_NRF_802154_ENCRYPTION
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_NRF_802154_ENCRYPTION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_ENCRYPTION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_SERIALIZATION"></a>

## 228.63 `CONFIG_NRF_802154_SERIALIZATION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此辅助符号（helper symbol）表示 nRF 802.15.4 序列化（serialization）可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NORDIC_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_IPC_SERVICE
CONFIG_MBOX
```

**被选择（Selected by）**

```text
CONFIG_NRF_802154_SER_HOST
CONFIG_NRF_802154_SER_RADIO
CONFIG_NRF_802154_SER_HOST
CONFIG_NRF_802154_SER_RADIO
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_IPC_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPC_SERVICE)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_NRF_802154_SER_HOST`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SER_HOST)、[`CONFIG_NRF_802154_SER_RADIO`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SER_RADIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_SER_DEFAULT_RESPONSE_TIMEOUT"></a>

## 228.64 `CONFIG_NRF_802154_SER_DEFAULT_RESPONSE_TIMEOUT`

**提示（Prompt）**：默认 Spinel 序列化响应超时（serialization response timeout），单位为毫秒

**说明（Help）**

指定 Spinel 状态响应（status response）的默认超时，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_SER_HOST || CONFIG_NRF_802154_SER_RADIO) && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → nRF 802.15.4 序列化（serialization）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_SER_HOST`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SER_HOST)、[`CONFIG_NRF_802154_SER_RADIO`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SER_RADIO)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_SER_HOST"></a>

## 228.65 `CONFIG_NRF_802154_SER_HOST`

**提示（Prompt）**：nRF IEEE 802.15.4 驱动序列化主机（serialization host）

**说明（Help）**

启用 nRF IEEE 802.15.4 驱动序列化（serialization）。当本核心没有可用无线电，而无线电服务由序列化后端（serialization backend）提供时，使用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NRF_802154_RADIO_DRIVER && !CONFIG_HAS_HW_NRF_RADIO_IEEE802154 && CONFIG_HAS_NORDIC_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_IEEE802154_NRF5_EXT_IRQ_MGMT if CONFIG_IEEE802154_NRF5
CONFIG_NRF_802154_SERIALIZATION
```

**被选择（Selected by）**

```text
CONFIG_IEEE802154_NRF5
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_HAS_HW_NRF_RADIO_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_RADIO_IEEE802154)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_IEEE802154_NRF5_EXT_IRQ_MGMT`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5_EXT_IRQ_MGMT)、[`CONFIG_IEEE802154_NRF5`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_RADIO_IEEE802154`、`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_SER_LOG"></a>

## 228.66 `CONFIG_NRF_802154_SER_LOG`

**提示（Prompt）**：802.15.4 序列化日志（serialization logs）

**说明（Help）**

启用 802.15.4 序列化模块（serialization module）的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NRF_802154_SER_HOST || CONFIG_NRF_802154_SER_RADIO) && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → nRF 802.15.4 序列化（serialization）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_SER_HOST`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SER_HOST)、[`CONFIG_NRF_802154_SER_RADIO`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SER_RADIO)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_SER_RADIO"></a>

## 228.67 `CONFIG_NRF_802154_SER_RADIO`

**提示（Prompt）**：nRF IEEE 802.15.4 驱动序列化无线电端（serialization radio）

**说明（Help）**

启用 nRF IEEE 802.15.4 驱动序列化（serialization）。当本核心具备无线电，并通过序列化后端（serialization backend）向外提供无线电服务时，使用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_RADIO_IEEE802154 && !CONFIG_IEEE802154_NRF5 && CONFIG_HAS_NORDIC_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_NRF_802154_RADIO_DRIVER
CONFIG_NRF_802154_SERIALIZATION
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_RADIO_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_RADIO_IEEE802154)、[`CONFIG_IEEE802154_NRF5`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_RADIO_IEEE802154`、`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_SER_RADIO_INIT_PRIO"></a>

## 228.68 `CONFIG_NRF_802154_SER_RADIO_INIT_PRIO`

**提示（Prompt）**：nRF52 IEEE 802.15.4 序列化初始化优先级（serialization initialization priority）

**说明（Help）**

设置初始化优先级数值。除非清楚其影响，否则不要随意更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_802154_SER_RADIO && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
53
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → nRF IEEE 802.15.4 驱动序列化无线电端（serialization radio）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_SER_RADIO`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SER_RADIO)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_SL_OPENSOURCE"></a>

## 228.69 `CONFIG_NRF_802154_SL_OPENSOURCE`

**提示（Prompt）**：开源（Open source）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_802154_SL_TYPE>
```

**主动选择（Selects）**

```text
CONFIG_SENSOR if CONFIG_NRF_802154_TEMPERATURE_UPDATE
CONFIG_TEMP_NRF5 if CONFIG_NRF_802154_TEMPERATURE_UPDATE
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → NRF IEEE 802.15.4 无线电驱动（radio driver） → nRF IEEE 802.15.4 服务层类型（Service Layer Type）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_SL_TYPE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SL_TYPE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_NRF_802154_TEMPERATURE_UPDATE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_TEMPERATURE_UPDATE)、[`CONFIG_TEMP_NRF5`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_NRF5)。

<a id="CONFIG_NRF_802154_SL_TYPE"></a>

## 228.70 `CONFIG_NRF_802154_SL_TYPE`

**提示（Prompt）**：nRF IEEE 802.15.4 服务层类型（Service Layer Type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_802154_RADIO_DRIVER && CONFIG_HAS_NORDIC_DRIVERS
```

**可选项（Choices）**

```text
CONFIG_NRF_802154_SL_OPENSOURCE
CONFIG_NRF_802154_SL_OPENSOURCE
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → NRF IEEE 802.15.4 无线电驱动（radio driver）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_NRF_802154_SL_OPENSOURCE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SL_OPENSOURCE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_SOURCE"></a>

## 228.71 `CONFIG_NRF_802154_SOURCE`

**提示（Prompt）**：IEEE 802.15.4 无线电驱动来源（Source）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NORDIC_DRIVERS
```

**可选项（Choices）**

```text
CONFIG_NRF_802154_SOURCE_HAL_NORDIC
CONFIG_NRF_802154_SOURCE_HAL_NORDIC
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_NRF_802154_SOURCE_HAL_NORDIC`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SOURCE_HAL_NORDIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_SOURCE_HAL_NORDIC"></a>

## 228.72 `CONFIG_NRF_802154_SOURCE_HAL_NORDIC`

**提示（Prompt）**：开源（Open source）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_802154_SOURCE>
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → IEEE 802.15.4 无线电驱动来源（Source）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_SOURCE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SOURCE)。

<a id="CONFIG_NRF_802154_TEMPERATURE_UPDATE"></a>

## 228.73 `CONFIG_NRF_802154_TEMPERATURE_UPDATE`

**提示（Prompt）**：nRF 802.15.4 温度更新（temperature update）

**说明（Help）**

启用 nRF 802.15.4 驱动的温度更新（temperature update）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_802154_RADIO_DRIVER && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_NRF54H20
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → NRF IEEE 802.15.4 无线电驱动（radio driver）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_SOC_NRF54H20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_TEMPERATURE_UPDATE_INIT_PRIO"></a>

## 228.74 `CONFIG_NRF_802154_TEMPERATURE_UPDATE_INIT_PRIO`

**提示（Prompt）**：nRF52 IEEE 802.15.4 温度更新初始化优先级（temperature update initialization priority）

**说明（Help）**

设置 nRF 802.15.4 驱动温度更新（temperature update）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_802154_TEMPERATURE_UPDATE && CONFIG_NRF_802154_RADIO_DRIVER && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
91
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → NRF IEEE 802.15.4 无线电驱动（radio driver） → nRF 802.15.4 温度更新（temperature update）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_TEMPERATURE_UPDATE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_TEMPERATURE_UPDATE)、[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_802154_TEMPERATURE_UPDATE_PERIOD"></a>

## 228.75 `CONFIG_NRF_802154_TEMPERATURE_UPDATE_PERIOD`

**提示（Prompt）**：nRF 802.15.4 温度更新周期（temperature update period），单位为毫秒

**说明（Help）**

nRF 802.15.4 驱动的温度更新周期（temperature update period），单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_802154_TEMPERATURE_UPDATE && CONFIG_NRF_802154_RADIO_DRIVER && CONFIG_HAS_NORDIC_DRIVERS
```

**默认值（Defaults）**

```text
60000
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → Nordic 驱动（drivers） → NRF IEEE 802.15.4 无线电驱动（radio driver） → nRF 802.15.4 温度更新（temperature update）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_TEMPERATURE_UPDATE`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_TEMPERATURE_UPDATE)、[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_DRIVERS`。

<a id="CONFIG_NRF_MPCCONF_API_IN_RAM"></a>

## 228.76 `CONFIG_NRF_MPCCONF_API_IN_RAM`

**提示（Prompt）**：将 MPCCONF API 放置在 RAM 中

**说明（Help）**

确保用于修改并锁定内存权限控制器配置（MPC configuration）的函数，即 `ironside_se_mpcconf_write()` 和 `ironside_se_mpcconf_finish_init()`，放置在 RAM 中。重新配置原地执行内存（XIP memory）的权限时可能需要这样做。Zephyr 默认的 IronSide 调用驱动不支持此方式，除非该驱动及全部依赖也重定位为从 RAM 执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IRONSIDE_SE_CALL && (!CONFIG_IRONSIDE_SE_CALL_ZEPHYR || !CONFIG_XIP) && CONFIG_HAS_IRONSIDE_SE
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE

**配置项引用（Symbol References）**：[`CONFIG_IRONSIDE_SE_CALL`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_IRONSIDE_SE_CALL)、[`CONFIG_IRONSIDE_SE_CALL_ZEPHYR`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_IRONSIDE_SE_CALL_ZEPHYR)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)、[`CONFIG_HAS_IRONSIDE_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IRONSIDE_SE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_IRONSIDE_SE`。

<a id="CONFIG_NRF_MPCCONF_SECTION"></a>

## 228.77 `CONFIG_NRF_MPCCONF_SECTION`

**提示（Prompt）**：全局内存权限控制器（Memory Privilege Controller，MPC）初始化段

**说明（Help）**

将构建中的静态全局内存权限控制器（MPC）外设初始化值放入专用段（dedicated section）。该段会从固件二进制文件中剥离。若启用了用户信息配置寄存器（UICR）生成器镜像，生成器会将剥离的段放入生成的 UICR MPCCONF 数据块（blob）中。目前 UICR 生成器最多支持一个镜像设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LINKER_DEVNULL_SUPPORT && CONFIG_HAS_IRONSIDE_SE
```

**弱选择（Implies）**

```text
CONFIG_LINKER_DEVNULL_MEMORY
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE

**配置项引用（Symbol References）**：[`CONFIG_LINKER_DEVNULL_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LINKER_DEVNULL_SUPPORT)、[`CONFIG_HAS_IRONSIDE_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IRONSIDE_SE)、[`CONFIG_LINKER_DEVNULL_MEMORY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_DEVNULL_MEMORY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LINKER_DEVNULL_SUPPORT`、`CONFIG_HAS_IRONSIDE_SE`。

<a id="CONFIG_NRF_PERIPHCONF_GENERATE_ENTRIES"></a>

## 228.78 `CONFIG_NRF_PERIPHCONF_GENERATE_ENTRIES`

**提示（Prompt）**：生成 PERIPHCONF 条目源文件（entries source file）

**说明（Help）**

根据设备树（devicetree）中的设备配置，生成包含 PERIPHCONF 条目的 C 文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_PERIPHCONF_SECTION && CONFIG_HAS_IRONSIDE_SE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE → 全局外设初始化段（Global peripheral initialization section）

**配置项引用（Symbol References）**：[`CONFIG_NRF_PERIPHCONF_SECTION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_PERIPHCONF_SECTION)、[`CONFIG_HAS_IRONSIDE_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IRONSIDE_SE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_IRONSIDE_SE`。

<a id="CONFIG_NRF_PERIPHCONF_GENERATE_ENTRIES_LOCK"></a>

## 228.79 `CONFIG_NRF_PERIPHCONF_GENERATE_ENTRIES_LOCK`

**提示（Prompt）**：锁定 PERIPHCONF 中的寄存器（registers）

**说明（Help）**

在支持锁定位（lock bit）的寄存器中设置该位。禁用后，可在启动后重新配置这些寄存器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_PERIPHCONF_GENERATE_ENTRIES && CONFIG_NRF_PERIPHCONF_SECTION && CONFIG_HAS_IRONSIDE_SE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE → 全局外设初始化段（Global peripheral initialization section） → 生成 PERIPHCONF 条目源文件（entries source file）

**配置项引用（Symbol References）**：[`CONFIG_NRF_PERIPHCONF_GENERATE_ENTRIES`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_PERIPHCONF_GENERATE_ENTRIES)、[`CONFIG_NRF_PERIPHCONF_SECTION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_PERIPHCONF_SECTION)、[`CONFIG_HAS_IRONSIDE_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IRONSIDE_SE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_IRONSIDE_SE`。

<a id="CONFIG_NRF_PERIPHCONF_SECTION"></a>

## 228.80 `CONFIG_NRF_PERIPHCONF_SECTION`

**提示（Prompt）**：全局外设初始化段（Global peripheral initialization section）

**说明（Help）**

将构建中的静态全局域外设初始化值（global domain peripheral initialization values）放入专用段。根据运行时加载方式，该段会从固件二进制文件中剥离，或保留为常量数据（constant data）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LINKER_DEVNULL_SUPPORT && CONFIG_HAS_IRONSIDE_SE
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE

**配置项引用（Symbol References）**：[`CONFIG_LINKER_DEVNULL_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LINKER_DEVNULL_SUPPORT)、[`CONFIG_HAS_IRONSIDE_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IRONSIDE_SE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LINKER_DEVNULL_SUPPORT`、`CONFIG_HAS_IRONSIDE_SE`。

<a id="CONFIG_NRF_PERIPHCONF_SECTION_KEEP_BY_DEFAULT"></a>

## 228.81 `CONFIG_NRF_PERIPHCONF_SECTION_KEEP_BY_DEFAULT`

**提示（Prompt）**：默认保留 PERIPHCONF 段，由构建系统设置

**说明（Help）**

由 Sysbuild 设置，用于更改镜像的默认行为，使其在没有其他显式配置时采用 `CONFIG_NRF_PERIPHCONF_SECTION_STRIP=n`。若要覆盖此行为，直接设置 `CONFIG_NRF_PERIPHCONF_SECTION_STRIP=y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_IRONSIDE_SE
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE

**配置项引用（Symbol References）**：[`CONFIG_HAS_IRONSIDE_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IRONSIDE_SE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_IRONSIDE_SE`。

<a id="CONFIG_NRF_PERIPHCONF_SECTION_STRIP"></a>

## 228.82 `CONFIG_NRF_PERIPHCONF_SECTION_STRIP`

**提示（Prompt）**：从二进制文件中剥离此段（Strip the section）

**说明（Help）**

从固件二进制文件中剥离 PERIPHCONF 段。启用 UICR 生成器镜像时，会将剥离的段放入生成的 UICR PERIPHCONF 数据块（blob）。禁用此项时，PERIPHCONF 段作为数据保留在二进制文件中，不再包含于 UICR PERIPHCONF 数据块；此时应通过 `ironside_se_periphconf_write()` API 加载。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_PERIPHCONF_SECTION && CONFIG_HAS_IRONSIDE_SE
```

**默认值（Defaults）**

```text
y if !CONFIG_NRF_PERIPHCONF_SECTION_KEEP_BY_DEFAULT
```

**弱选择（Implies）**

```text
CONFIG_LINKER_DEVNULL_MEMORY
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE → 全局外设初始化段（Global peripheral initialization section）

**配置项引用（Symbol References）**：[`CONFIG_NRF_PERIPHCONF_SECTION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_PERIPHCONF_SECTION)、[`CONFIG_HAS_IRONSIDE_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IRONSIDE_SE)、[`CONFIG_NRF_PERIPHCONF_SECTION_KEEP_BY_DEFAULT`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_PERIPHCONF_SECTION_KEEP_BY_DEFAULT)、[`CONFIG_LINKER_DEVNULL_MEMORY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_DEVNULL_MEMORY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_IRONSIDE_SE`。

<a id="CONFIG_NRF_REGTOOL_GENERATE_UICR"></a>

## 228.83 `CONFIG_NRF_REGTOOL_GENERATE_UICR`

**提示（Prompt）**：生成用户信息配置寄存器数据（UICR）

**说明（Help）**

使用 `nrf-regtool` 根据设备树（devicetree）内容生成 UICR hex 文件。需要分配 UICR 的 CPU 域（CPU domains），如果未随固件一起烧写 UICR，将无法启动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF92
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig.nrf_regtool:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig.nrf_regtool#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrf-regtool 选项（options）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF92`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF92)。

<a id="CONFIG_NRF_REGTOOL_VERBOSITY"></a>

## 228.84 `CONFIG_NRF_REGTOOL_VERBOSITY`

**提示（Prompt）**：控制台输出详细级别（Verbosity level）

**说明（Help）**

`nrf-regtool` 向控制台输出的详细级别（verbosity level）：

0. 仅输出关键信息和警告。
1. 输出格式美观、便于阅读的外设配置表示，推荐用于检查寄存器值。
2. 输出更多调试细节，例如外设配置的内存映射（memory maps），但格式较不易阅读。
3. 输出更多通常只有 `nrf-regtool` 开发者才有用的细节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF92
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 3]
```

**定义位置（Location）**：[`modules/hal_nordic/Kconfig.nrf_regtool:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/Kconfig.nrf_regtool#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrf-regtool 选项（options）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF92`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF92)。

<!-- kconfig-navigation -->

[上一章](P227_modules_hal_nordic_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P229_modules_hal_nxp_配置项参考.md)
