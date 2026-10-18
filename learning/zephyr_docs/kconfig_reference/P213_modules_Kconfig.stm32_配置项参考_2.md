---
id: learning.zephyr-docs.kconfig-reference.page-213
title: "`modules/Kconfig.stm32`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第213章\_`modules/Kconfig.stm32`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.stm32` 的 78 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_USE_STM32_HAL_RADIO_TIMER"></a>

## 213.1 `CONFIG_USE_STM32_HAL_RADIO_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 无线电定时器（Radio Timer）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_BT_STM32WB0
CONFIG_STM32WB0_RADIO_TIMER
```

**定义位置（Location）**：[`modules/Kconfig.stm32:546`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L546)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_BT_STM32WB0`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WB0)、[`CONFIG_STM32WB0_RADIO_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_STM32WB0_RADIO_TIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_RAMCFG"></a>

## 213.2 `CONFIG_USE_STM32_HAL_RAMCFG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube RAM 配置控制器（RAMs configuration controller (RAMCFG)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_STM32N6_AXISRAM
```

**定义位置（Location）**：[`modules/Kconfig.stm32:535`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L535)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_STM32N6_AXISRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32N6_AXISRAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`、`CONFIG_STM32N6_AXISRAM`。

<a id="CONFIG_USE_STM32_HAL_RAMECC"></a>

## 213.3 `CONFIG_USE_STM32_HAL_RAMECC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube RAM 纠错码监测（RAM ECC monitoring (RAMECC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:551`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L551)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_RCC"></a>

## 213.4 `CONFIG_USE_STM32_HAL_RCC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 复位与时钟控制（Reset and Clock Control (RCC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:556`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L556)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_RIF"></a>

## 213.5 `CONFIG_USE_STM32_HAL_RIF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 资源隔离框架（Resource Isolation Framework (RIF)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_STM32N6X
```

**定义位置（Location）**：[`modules/Kconfig.stm32:561`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L561)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`、`CONFIG_SOC_SERIES_STM32N6X`。

<a id="CONFIG_USE_STM32_HAL_RNG"></a>

## 213.6 `CONFIG_USE_STM32_HAL_RNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 真随机数生成器（True random number generator (RNG)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_RNG
```

**定义位置（Location）**：[`modules/Kconfig.stm32:566`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L566)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_RNG`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_RNG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_RNG_EX"></a>

## 213.7 `CONFIG_USE_STM32_HAL_RNG_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展真随机数生成器（Extended True random number generator (RNG)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_RNG
```

**定义位置（Location）**：[`modules/Kconfig.stm32:571`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L571)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_RNG`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_RNG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_RTC"></a>

## 213.8 `CONFIG_USE_STM32_HAL_RTC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 实时时钟（Real-time clock (RTC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:576`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L576)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_RTC_EX"></a>

## 213.9 `CONFIG_USE_STM32_HAL_RTC_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展实时时钟（Extended Real-time clock (RTC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:581`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L581)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SAI"></a>

## 213.10 `CONFIG_USE_STM32_HAL_SAI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 串行音频接口（Serial audio interface (SAI)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_I2S_STM32_SAI
```

**定义位置（Location）**：[`modules/Kconfig.stm32:586`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L586)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_I2S_STM32_SAI`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_STM32_SAI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SAI_EX"></a>

## 213.11 `CONFIG_USE_STM32_HAL_SAI_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展串行音频接口（Extended Serial audio interface (SAI)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_I2S_STM32_SAI
```

**定义位置（Location）**：[`modules/Kconfig.stm32:591`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L591)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_I2S_STM32_SAI`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_STM32_SAI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SBS"></a>

## 213.12 `CONFIG_USE_STM32_HAL_SBS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 系统配置、启动与安全（System configuration, boot, and security (SBS)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_ETH_STM32_HAL2_API
```

**定义位置（Location）**：[`modules/Kconfig.stm32:597`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L597)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_ETH_STM32_HAL2_API`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL2_API)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SD"></a>

## 213.13 `CONFIG_USE_STM32_HAL_SD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 安全数字输入／输出及多媒体卡接口（Secure digital input/output MultiMediaCard interface (SDMMC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_SDMMC_STM32
```

**定义位置（Location）**：[`modules/Kconfig.stm32:603`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L603)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_SDMMC_STM32`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SDADC"></a>

## 213.14 `CONFIG_USE_STM32_HAL_SDADC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube SDADC（SDADC）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:615`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L615)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SDIO"></a>

## 213.15 `CONFIG_USE_STM32_HAL_SDIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 安全数字输入／输出接口（Secure digital input/output interface (SDIO)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:620`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L620)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SDRAM"></a>

## 213.16 `CONFIG_USE_STM32_HAL_SDRAM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 同步动态随机存取存储器控制器（SDRAM controller (SDRAM)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_MEMC_STM32_SDRAM
```

**定义位置（Location）**：[`modules/Kconfig.stm32:626`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L626)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_MEMC_STM32_SDRAM`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_STM32_SDRAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SD_EX"></a>

## 213.17 `CONFIG_USE_STM32_HAL_SD_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展安全数字输入／输出及多媒体卡接口（Extended Secure digital input/output MultiMediaCard interface (SDMMC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_SDMMC_STM32
```

**定义位置（Location）**：[`modules/Kconfig.stm32:609`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L609)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_SDMMC_STM32`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SMARTCARD"></a>

## 213.18 `CONFIG_USE_STM32_HAL_SMARTCARD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 智能卡控制器（Smartcard controller (SMARTCARD)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:631`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L631)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SMARTCARD_EX"></a>

## 213.19 `CONFIG_USE_STM32_HAL_SMARTCARD_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展智能卡控制器（Extended Smartcard controller (SMARTCARD)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:636`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L636)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SMBUS"></a>

## 213.20 `CONFIG_USE_STM32_HAL_SMBUS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 系统管理总线（System Management Bus (SMBus)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:642`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L642)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SMBUS_EX"></a>

## 213.21 `CONFIG_USE_STM32_HAL_SMBUS_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展系统管理总线（Extended System Management Bus (SMBus)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:647`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L647)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SPDIFRX"></a>

## 213.22 `CONFIG_USE_STM32_HAL_SPDIFRX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube SPDIF 接收器接口（SPDIF receiver interface (SPDIFRX)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:652`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L652)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SPI"></a>

## 213.23 `CONFIG_USE_STM32_HAL_SPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 串行外设接口（Serial peripheral interface (SPI)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:657`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L657)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SPI_EX"></a>

## 213.24 `CONFIG_USE_STM32_HAL_SPI_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展串行外设接口（Extended Serial peripheral interface (SPI)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:662`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L662)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SRAM"></a>

## 213.25 `CONFIG_USE_STM32_HAL_SRAM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 静态随机存取存储器控制器（SRAM controller (SRAM)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_MEMC_STM32_NOR_PSRAM
```

**定义位置（Location）**：[`modules/Kconfig.stm32:668`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L668)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_MEMC_STM32_NOR_PSRAM`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_STM32_NOR_PSRAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_SWPMI"></a>

## 213.26 `CONFIG_USE_STM32_HAL_SWPMI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 单线协议主接口（Single Wire Protocol Master Interface，SWPMI）硬件抽象层（HAL）模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:673`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L673)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_TAMP"></a>

## 213.27 `CONFIG_USE_STM32_HAL_TAMP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 防篡改与备份寄存器（Tamper and backup registers (TAMP)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:679`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L679)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_TIM"></a>

## 213.28 `CONFIG_USE_STM32_HAL_TIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 定时器（Timer (TIM)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:684`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L684)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_TIM_EX"></a>

## 213.29 `CONFIG_USE_STM32_HAL_TIM_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展定时器（Extended Timer (TIM)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:689`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L689)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_TSC"></a>

## 213.30 `CONFIG_USE_STM32_HAL_TSC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 触摸感应控制器（Touch sensing controller (TSC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:694`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L694)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_UART"></a>

## 213.31 `CONFIG_USE_STM32_HAL_UART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 通用异步收发器（Universal asynchronous receiver transmitter (USART)）硬件抽象层（HAL）模块驱动。

译注：此项原文将“异步收发器”写为 USART；另有单独的同步／异步 USART 条目。名称按各条原文分别保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:699`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L699)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_UART_EX"></a>

## 213.32 `CONFIG_USE_STM32_HAL_UART_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展通用异步收发器（Extended Universal asynchronous receiver transmitter (USART)）硬件抽象层（HAL）模块驱动。

译注：此项原文将“异步收发器”写为 USART；另有单独的同步／异步 USART 条目。名称按各条原文分别保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:705`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L705)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_USART"></a>

## 213.33 `CONFIG_USE_STM32_HAL_USART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 通用同步／异步收发器（Universal synchronous asynchronous receiver transmitter (USART)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:711`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L711)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_USART_EX"></a>

## 213.34 `CONFIG_USE_STM32_HAL_USART_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展通用同步／异步收发器（Extended Universal synchronous asynchronous receiver transmitter (USART)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:717`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L717)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_WWDG"></a>

## 213.35 `CONFIG_USE_STM32_HAL_WWDG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 系统窗口看门狗（System window watchdog (WWDG)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:723`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L723)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_XSPI"></a>

## 213.36 `CONFIG_USE_STM32_HAL_XSPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 八线 SPI（OctoSPI (XSPI)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_STM32_XSPIM
CONFIG_FLASH_STM32_XSPI
CONFIG_MEMC_STM32_XSPI_PSRAM
CONFIG_MSPI_STM32_XSPI
```

**定义位置（Location）**：[`modules/Kconfig.stm32:728`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L728)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_STM32_XSPIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_XSPIM)、[`CONFIG_FLASH_STM32_XSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_XSPI)、[`CONFIG_MEMC_STM32_XSPI_PSRAM`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_STM32_XSPI_PSRAM)、[`CONFIG_MSPI_STM32_XSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_XSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_ADC"></a>

## 213.37 `CONFIG_USE_STM32_LL_ADC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 模数转换器（Analog-to-Digital Converter (ADC)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:733`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L733)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_BDMA"></a>

## 213.38 `CONFIG_USE_STM32_LL_BDMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 基本直接内存访问控制器（Basic direct memory access controller (BDMA)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_DMA_STM32_BDMA
```

**定义位置（Location）**：[`modules/Kconfig.stm32:738`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L738)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_DMA_STM32_BDMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_STM32_BDMA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_COMP"></a>

## 213.39 `CONFIG_USE_STM32_LL_COMP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 超低功耗比较器通道（Ultra Low Power Comparator channels (COMP)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:744`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L744)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_CORDIC"></a>

## 213.40 `CONFIG_USE_STM32_LL_CORDIC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube CORDIC 协处理器功能（CORDIC co-processor (CORDIC) functions）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:750`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L750)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_CRC"></a>

## 213.41 `CONFIG_USE_STM32_LL_CRC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 循环冗余校验计算单元（Cyclic redundancy check calculation unit (CRC)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:756`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L756)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_CRS"></a>

## 213.42 `CONFIG_USE_STM32_LL_CRS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 时钟恢复系统（Clock recovery system (CRS)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:762`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L762)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_DAC"></a>

## 213.43 `CONFIG_USE_STM32_LL_DAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 数模转换器（Digital-to-analog converter (DAC)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:767`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L767)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_DELAYBLOCK"></a>

## 213.44 `CONFIG_USE_STM32_LL_DELAYBLOCK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 延迟块（DelayBlock，DELAYBLOCK）底层（LL）模块驱动，用于 stm32H7 或 stm32MP1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:772`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L772)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_DLYB"></a>

## 213.45 `CONFIG_USE_STM32_LL_DLYB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 延迟块（DelayBlock，DELAYBLOCK）底层（LL）模块驱动，用于 stm32U5 或 STM32N6。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_FLASH_STM32_OSPI
CONFIG_FLASH_STM32_XSPI
CONFIG_MEMC_STM32_XSPI_PSRAM
CONFIG_MEMC_STM32_OSPI_PSRAM
CONFIG_MSPI_STM32_OSPI
CONFIG_MSPI_STM32_XSPI
```

**定义位置（Location）**：[`modules/Kconfig.stm32:777`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L777)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_FLASH_STM32_OSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_OSPI)、[`CONFIG_FLASH_STM32_XSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_XSPI)、[`CONFIG_MEMC_STM32_XSPI_PSRAM`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_STM32_XSPI_PSRAM)、[`CONFIG_MEMC_STM32_OSPI_PSRAM`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_STM32_OSPI_PSRAM)、[`CONFIG_MSPI_STM32_OSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_OSPI)、[`CONFIG_MSPI_STM32_XSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_XSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_DMA"></a>

## 213.46 `CONFIG_USE_STM32_LL_DMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 直接内存访问控制器（Direct Memory Access controller (DMA)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_DMA_STM32
CONFIG_DMA_STM32U5
```

**定义位置（Location）**：[`modules/Kconfig.stm32:782`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L782)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_DMA_STM32`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_STM32)、[`CONFIG_DMA_STM32U5`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_STM32U5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_DMA2D"></a>

## 213.47 `CONFIG_USE_STM32_LL_DMA2D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube Chrom-Art 加速器控制器（Chrom-Art Accelerator™ controller (DMA2D)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:788`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L788)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_EXTI"></a>

## 213.48 `CONFIG_USE_STM32_LL_EXTI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展中断与事件控制器（Extended interrupt and event controller (EXTI)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:794`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L794)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_FMAC"></a>

## 213.49 `CONFIG_USE_STM32_LL_FMAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 滤波数学加速器（Filter Math Accelerator (FMAC)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:800`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L800)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_FMC"></a>

## 213.50 `CONFIG_USE_STM32_LL_FMC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 灵活存储控制器（Flexible memory controller (FMC)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_MEMC_STM32_SDRAM
CONFIG_MEMC_STM32_NOR_PSRAM
```

**定义位置（Location）**：[`modules/Kconfig.stm32:805`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L805)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_MEMC_STM32_SDRAM`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_STM32_SDRAM)、[`CONFIG_MEMC_STM32_NOR_PSRAM`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_STM32_NOR_PSRAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_FSMC"></a>

## 213.51 `CONFIG_USE_STM32_LL_FSMC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 灵活静态存储控制器（Flexible static memory controller (FSMC)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:810`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L810)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_GPIO"></a>

## 213.52 `CONFIG_USE_STM32_LL_GPIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展通用输入／输出（Extended General-purpose I/Os (GPIO)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:816`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L816)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_HRTIM"></a>

## 213.53 `CONFIG_USE_STM32_LL_HRTIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 高分辨率定时器（High-Resolution Timer (HRTIM)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:821`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L821)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_I2C"></a>

## 213.54 `CONFIG_USE_STM32_LL_I2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube I2C 接口（Inter-integrated circuit (I2C) interface）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:826`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L826)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_I3C"></a>

## 213.55 `CONFIG_USE_STM32_LL_I3C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 改进型芯片间总线（Improved inter-integrated circuit (I3C)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:832`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L832)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_ICACHE"></a>

## 213.56 `CONFIG_USE_STM32_LL_ICACHE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 指令缓存（Instruction cache (ICACHE)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:838`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L838)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_IPCC"></a>

## 213.57 `CONFIG_USE_STM32_LL_IPCC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 处理器间通信控制器（Inter-Processor communication controller (IPCC)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:843`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L843)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_LCSC"></a>

## 213.58 `CONFIG_USE_STM32_LL_LCSC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube LC 传感器控制器（LC sensor controller (LCSC)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:849`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L849)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_LPGPIO"></a>

## 213.59 `CONFIG_USE_STM32_LL_LPGPIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 低功耗通用输入／输出（Low-power general-purpose I/Os (LPGPIO)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:854`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L854)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_LPTIM"></a>

## 213.60 `CONFIG_USE_STM32_LL_LPTIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 低功耗定时器（Low Power Timer (LPTIM)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:860`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L860)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_LPUART"></a>

## 213.61 `CONFIG_USE_STM32_LL_LPUART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 低功耗通用异步收发器（Low-power universal asynchronous receiver transmitter (LPUART)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:865`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L865)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_MDMA"></a>

## 213.62 `CONFIG_USE_STM32_LL_MDMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 主直接内存访问控制器（Master Direct Memory Access controller (MDMA)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:871`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L871)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_OPAMP"></a>

## 213.63 `CONFIG_USE_STM32_LL_OPAMP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 运算放大器（Operational amplifiers (OPAMP)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:877`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L877)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_PKA"></a>

## 213.64 `CONFIG_USE_STM32_LL_PKA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 公钥加速器（Public key accelerator (PKA)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:882`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L882)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_PWR"></a>

## 213.65 `CONFIG_USE_STM32_LL_PWR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 电源控制（Power control (PWR)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:887`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L887)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_RCC"></a>

## 213.66 `CONFIG_USE_STM32_LL_RCC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 复位与时钟控制（Reset and Clock Control (RCC)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_STM32_CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:892`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L892)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_CLOCK_CONTROL_STM32_CUBE`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_STM32_CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_RNG"></a>

## 213.67 `CONFIG_USE_STM32_LL_RNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 真随机数生成器（True random number generator (RNG)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:897`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L897)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_RTC"></a>

## 213.68 `CONFIG_USE_STM32_LL_RTC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 实时时钟（Real-time clock (RTC)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:902`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L902)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_SDMMC"></a>

## 213.69 `CONFIG_USE_STM32_LL_SDMMC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube SD／SDIO／MMC 卡主机接口（SD/SDIO/MMC card host interface (SDMMC)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_SDMMC_STM32
CONFIG_SDHC_STM32_SDMMC
```

**定义位置（Location）**：[`modules/Kconfig.stm32:907`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L907)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_SDMMC_STM32`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32)、[`CONFIG_SDHC_STM32_SDMMC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_STM32_SDMMC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_SPI"></a>

## 213.70 `CONFIG_USE_STM32_LL_SPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 串行外设接口（Serial peripheral interface (SPI)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:913`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L913)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_SWPMI"></a>

## 213.71 `CONFIG_USE_STM32_LL_SWPMI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 单线协议主接口（Single Wire Protocol Master Interface (SWPMI)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:918`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L918)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_TIM"></a>

## 213.72 `CONFIG_USE_STM32_LL_TIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 定时器（Timer (TIM)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:924`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L924)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_UCPD"></a>

## 213.73 `CONFIG_USE_STM32_LL_UCPD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube USB 供电设备接口（USB Power Delivery device interface (UCPD)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:929`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L929)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_USART"></a>

## 213.74 `CONFIG_USE_STM32_LL_USART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 通用同步／异步收发器（Universal synchronous asynchronous receiver transmitter (USART)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:935`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L935)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_USB"></a>

## 213.75 `CONFIG_USE_STM32_LL_USB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 通用串行总线全速设备接口（Universal serial bus full-speed device interface (USB)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_UDC_STM32
CONFIG_USB_DC_STM32
```

**定义位置（Location）**：[`modules/Kconfig.stm32:941`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L941)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_UDC_STM32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_STM32)、[`CONFIG_USB_DC_STM32`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_UTILS"></a>

## 213.76 `CONFIG_USE_STM32_LL_UTILS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 实用函数（Utility functions (UTILS)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_STM32_CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:947`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L947)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_CLOCK_CONTROL_STM32_CUBE`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_STM32_CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_LL_VENC"></a>

## 213.77 `CONFIG_USE_STM32_LL_VENC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 视频编码器（Video Encoder (VENC)）底层（LL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_VIDEO_STM32_VENC
```

**定义位置（Location）**：[`modules/Kconfig.stm32:952`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L952)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_VIDEO_STM32_VENC`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_VENC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_UTIL_I3C"></a>

## 213.78 `CONFIG_USE_STM32_UTIL_I3C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube I3C 时序实用函数（I3C Timing Utility functions，UTILS）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:957`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L957)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<!-- kconfig-navigation -->

[上一章](P212_modules_Kconfig.stm32_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P214_modules_Kconfig.syst_配置项参考.md)
