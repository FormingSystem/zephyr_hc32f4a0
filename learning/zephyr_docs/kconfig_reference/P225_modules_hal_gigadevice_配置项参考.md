---
id: learning.zephyr-docs.kconfig-reference.page-225
title: "`modules/hal_gigadevice`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第225章\_`modules/hal_gigadevice`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/hal_gigadevice` 的 49 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_GD32_DBG_SUPPORT"></a>

## 225.1 `CONFIG_GD32_DBG_SUPPORT`

**提示（Prompt）**：使用 GD32 调试功能（Debug features）

**说明（Help）**

启用 GD32 调试功能（Debug features），允许使用访问 `DBG_CTL` 寄存器的函数，例如 `dbg_periph_enable()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_GD32_DBG
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)、[`CONFIG_USE_GD32_DBG`](P225_modules_hal_gigadevice_配置项参考.md#CONFIG_USE_GD32_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_GD32_HAS_AFIO_PINMUX"></a>

## 225.2 `CONFIG_GD32_HAS_AFIO_PINMUX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

该系列使用复用功能 I/O（AFIO）引脚复用模型（pinmux model）时，应选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_GD32E10X
CONFIG_SOC_SERIES_GD32E50X
CONFIG_SOC_SERIES_GD32F403
CONFIG_SOC_SERIES_GD32VF103
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_GD32E10X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E10X)、[`CONFIG_SOC_SERIES_GD32E50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E50X)、[`CONFIG_SOC_SERIES_GD32F403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F403)、[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)。

<a id="CONFIG_GD32_HAS_AF_PINMUX"></a>

## 225.3 `CONFIG_GD32_HAS_AF_PINMUX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

该系列使用复用功能（AF）引脚复用模型（pinmux model）时，应选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_GD32A50X
CONFIG_SOC_SERIES_GD32C2X1
CONFIG_SOC_SERIES_GD32F3X0
CONFIG_SOC_SERIES_GD32F4XX
CONFIG_SOC_SERIES_GD32L23X
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_GD32A50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32A50X)、[`CONFIG_SOC_SERIES_GD32C2X1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32C2X1)、[`CONFIG_SOC_SERIES_GD32F3X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F3X0)、[`CONFIG_SOC_SERIES_GD32F4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F4XX)、[`CONFIG_SOC_SERIES_GD32L23X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32L23X)。

<a id="CONFIG_GD32_HAS_IRC_32K"></a>

## 225.4 `CONFIG_GD32_HAS_IRC_32K`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

低速内部 RC 振荡器（low speed internal RC Oscillator）使用 32 kHz 振荡器

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_GD32C2X1
CONFIG_SOC_SERIES_GD32F4XX
CONFIG_SOC_SERIES_GD32L23X
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)、[`CONFIG_SOC_SERIES_GD32C2X1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32C2X1)、[`CONFIG_SOC_SERIES_GD32F4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F4XX)、[`CONFIG_SOC_SERIES_GD32L23X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32L23X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_GD32_HAS_IRC_40K"></a>

## 225.5 `CONFIG_GD32_HAS_IRC_40K`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

低速内部 RC 振荡器（low speed internal RC Oscillator）使用 40 kHz 振荡器

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_GD32A50X
CONFIG_SOC_SERIES_GD32E10X
CONFIG_SOC_SERIES_GD32E50X
CONFIG_SOC_SERIES_GD32F3X0
CONFIG_SOC_SERIES_GD32F403
CONFIG_SOC_SERIES_GD32VF103
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)、[`CONFIG_SOC_SERIES_GD32A50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32A50X)、[`CONFIG_SOC_SERIES_GD32E10X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E10X)、[`CONFIG_SOC_SERIES_GD32E50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E50X)、[`CONFIG_SOC_SERIES_GD32F3X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F3X0)、[`CONFIG_SOC_SERIES_GD32F403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F403)、[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_GD32_HXTAL_25MHZ"></a>

## 225.6 `CONFIG_GD32_HXTAL_25MHZ`

**提示（Prompt）**：25 MHz

**说明（Help）**

高速外部晶振（HXTAL）使用 25 MHz 振荡器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_GD32VF103 || CONFIG_SOC_SERIES_GD32E10X) && <choice CONFIG_GD32_HXTAL_FREQUENCY>
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录） → 高速外部振荡器时钟频率（High speed external oscillator clock frequency）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)、[`CONFIG_SOC_SERIES_GD32E10X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E10X)、[`CONFIG_GD32_HXTAL_FREQUENCY`](P225_modules_hal_gigadevice_配置项参考.md#CONFIG_GD32_HXTAL_FREQUENCY)。

<a id="CONFIG_GD32_HXTAL_8MHZ"></a>

## 225.7 `CONFIG_GD32_HXTAL_8MHZ`

**提示（Prompt）**：8 MHz

**说明（Help）**

高速外部晶振（HXTAL）使用 8 MHz 振荡器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_GD32VF103 || CONFIG_SOC_SERIES_GD32E10X || CONFIG_SOC_SERIES_GD32F4XX) && <choice CONFIG_GD32_HXTAL_FREQUENCY>
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录） → 高速外部振荡器时钟频率（High speed external oscillator clock frequency）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)、[`CONFIG_SOC_SERIES_GD32E10X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E10X)、[`CONFIG_SOC_SERIES_GD32F4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F4XX)、[`CONFIG_GD32_HXTAL_FREQUENCY`](P225_modules_hal_gigadevice_配置项参考.md#CONFIG_GD32_HXTAL_FREQUENCY)。

<a id="CONFIG_GD32_HXTAL_FIRMWARE_DEFINED"></a>

## 225.8 `CONFIG_GD32_HXTAL_FIRMWARE_DEFINED`

**提示（Prompt）**：由固件定义（Firmware defined）

**说明（Help）**

对高速外部晶振（HXTAL）使用固件中定义的默认频率。适用于固件中具有默认 HXTAL 定义的 SoC，例如 gd32f4xx、gd32f3x0 等。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_GD32VF103 && !CONFIG_SOC_SERIES_GD32E10X && <choice CONFIG_GD32_HXTAL_FREQUENCY>
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录） → 高速外部振荡器时钟频率（High speed external oscillator clock frequency）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)、[`CONFIG_SOC_SERIES_GD32E10X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E10X)、[`CONFIG_GD32_HXTAL_FREQUENCY`](P225_modules_hal_gigadevice_配置项参考.md#CONFIG_GD32_HXTAL_FREQUENCY)。

<a id="CONFIG_GD32_HXTAL_FREQUENCY"></a>

## 225.9 `CONFIG_GD32_HXTAL_FREQUENCY`

**提示（Prompt）**：高速外部振荡器时钟频率（High speed external oscillator clock frequency）

**说明（Help）**

以 Hz 为单位定义高速晶体振荡器（High-speed Crystal Oscillator，HXTAL）的值，用于设置振荡器频率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**默认值（Defaults）**

```text
CONFIG_GD32_HXTAL_FIRMWARE_DEFINED if CONFIG_SOC_SERIES_GD32F403 || CONFIG_SOC_SERIES_GD32F4XX || CONFIG_SOC_SERIES_GD32F3X0 || CONFIG_SOC_SERIES_GD32C2X1
CONFIG_GD32_HXTAL_25MHZ if CONFIG_SOC_SERIES_GD32VF103 || CONFIG_SOC_SERIES_GD32E50X
CONFIG_GD32_HXTAL_8MHZ if CONFIG_SOC_SERIES_GD32E10X
```

**可选项（Choices）**

```text
CONFIG_GD32_HXTAL_FIRMWARE_DEFINED
CONFIG_GD32_HXTAL_8MHZ
CONFIG_GD32_HXTAL_25MHZ
CONFIG_GD32_HXTAL_FIRMWARE_DEFINED
CONFIG_GD32_HXTAL_8MHZ
CONFIG_GD32_HXTAL_25MHZ
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)、[`CONFIG_GD32_HXTAL_FIRMWARE_DEFINED`](P225_modules_hal_gigadevice_配置项参考.md#CONFIG_GD32_HXTAL_FIRMWARE_DEFINED)、[`CONFIG_SOC_SERIES_GD32F403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F403)、[`CONFIG_SOC_SERIES_GD32F4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F4XX)、[`CONFIG_SOC_SERIES_GD32F3X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F3X0)、[`CONFIG_SOC_SERIES_GD32C2X1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32C2X1)、[`CONFIG_GD32_HXTAL_25MHZ`](P225_modules_hal_gigadevice_配置项参考.md#CONFIG_GD32_HXTAL_25MHZ)、[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)、[`CONFIG_SOC_SERIES_GD32E50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E50X)、[`CONFIG_GD32_HXTAL_8MHZ`](P225_modules_hal_gigadevice_配置项参考.md#CONFIG_GD32_HXTAL_8MHZ)、[`CONFIG_SOC_SERIES_GD32E10X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E10X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_GD32_LOW_SPEED_IRC_FREQUENCY"></a>

## 225.10 `CONFIG_GD32_LOW_SPEED_IRC_FREQUENCY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

以 Hz 为单位定义低速内部 RC 振荡器（Internal RC Oscillator，IRC）的值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**默认值（Defaults）**

```text
32000 if CONFIG_GD32_HAS_IRC_32K
40000 if CONFIG_GD32_HAS_IRC_40K
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)、[`CONFIG_GD32_HAS_IRC_32K`](P225_modules_hal_gigadevice_配置项参考.md#CONFIG_GD32_HAS_IRC_32K)、[`CONFIG_GD32_HAS_IRC_40K`](P225_modules_hal_gigadevice_配置项参考.md#CONFIG_GD32_HAS_IRC_40K)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_ADC"></a>

## 225.11 `CONFIG_USE_GD32_ADC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 模数转换器（Analog-to-Digital Converter，ADC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_BKP"></a>

## 225.12 `CONFIG_USE_GD32_BKP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 备份寄存器（Backup Registers，BKP）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_CAN"></a>

## 225.13 `CONFIG_USE_GD32_CAN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 控制器局域网（Controller Area Network，CAN）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_CEC"></a>

## 225.14 `CONFIG_USE_GD32_CEC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 消费电子控制（Consumer Electronics Control，CEC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_CMP"></a>

## 225.15 `CONFIG_USE_GD32_CMP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 比较器（Comparator，CMP）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_CRC"></a>

## 225.16 `CONFIG_USE_GD32_CRC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 循环冗余校验计算单元（Cyclic Redundancy Check calculation unit，CRC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_CTC"></a>

## 225.17 `CONFIG_USE_GD32_CTC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 时钟微调控制器（Clock Trim Controller，CTC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_DAC"></a>

## 225.18 `CONFIG_USE_GD32_DAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 数模转换器（Digital-to-Analog Converter，DAC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_DBG"></a>

## 225.19 `CONFIG_USE_GD32_DBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 调试（Debug，DBG）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**被选择（Selected by）**

```text
CONFIG_GD32_DBG_SUPPORT
CONFIG_GD32_DBG_SUPPORT
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)、[`CONFIG_GD32_DBG_SUPPORT`](P225_modules_hal_gigadevice_配置项参考.md#CONFIG_GD32_DBG_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_DCI"></a>

## 225.20 `CONFIG_USE_GD32_DCI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 数字摄像头接口（Digital Camera Interface，DCI）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_DMA"></a>

## 225.21 `CONFIG_USE_GD32_DMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 直接内存访问控制器（Direct Memory Access controller，DMA）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**被选择（Selected by）**

```text
CONFIG_DMA_GD32
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)、[`CONFIG_DMA_GD32`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_GD32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_ENET"></a>

## 225.22 `CONFIG_USE_GD32_ENET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 以太网（Ethernet，ENET）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_EXMC"></a>

## 225.23 `CONFIG_USE_GD32_EXMC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 外部存储控制器（External Memory Controller，EXMC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_EXTI"></a>

## 225.24 `CONFIG_USE_GD32_EXTI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 中断／事件控制器（Interrupt/Event controller，EXTI）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_FMC"></a>

## 225.25 `CONFIG_USE_GD32_FMC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 闪存控制器（Flash Memory Controller，FMC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_FWDGT"></a>

## 225.26 `CONFIG_USE_GD32_FWDGT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 自由看门狗定时器（Free Watchdog Timer，FWDGT）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**被选择（Selected by）**

```text
CONFIG_FWDGT_GD32
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L160)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)、[`CONFIG_FWDGT_GD32`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_FWDGT_GD32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_GPIO"></a>

## 225.27 `CONFIG_USE_GD32_GPIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 通用及复用功能输入／输出（General-purpose and Alternate-Function I/Os，GPIO 和 AFIO）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_I2C"></a>

## 225.28 `CONFIG_USE_GD32_I2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 芯片间总线接口（Inter-Integrated Circuit Interface，I2C）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_IPA"></a>

## 225.29 `CONFIG_USE_GD32_IPA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 图像处理加速器（Image Processing Accelerator，IPA）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_IREF"></a>

## 225.30 `CONFIG_USE_GD32_IREF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 可编程电流参考（Programmable Current Reference，IREF）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L182)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_MISC"></a>

## 225.31 `CONFIG_USE_GD32_MISC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 系统实用功能（System Utilities，MISC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_PMU"></a>

## 225.32 `CONFIG_USE_GD32_PMU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 电源管理单元（Power Management Unit，PMU）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_RCU"></a>

## 225.33 `CONFIG_USE_GD32_RCU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 复位与时钟单元（Reset and Clock Unit，RCU）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:197`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L197)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_RTC"></a>

## 225.34 `CONFIG_USE_GD32_RTC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 实时时钟（Real-Time Clock，RTC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L203)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_SDIO"></a>

## 225.35 `CONFIG_USE_GD32_SDIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 安全数字输入／输出接口（Secure Digital Input/Output interface，SDIO）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:208`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L208)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_SHRTIMER"></a>

## 225.36 `CONFIG_USE_GD32_SHRTIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 超高分辨率定时器（Super High-Resolution Timer，SHRTIMER）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:224`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L224)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_SPI"></a>

## 225.37 `CONFIG_USE_GD32_SPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 串行外设接口（Serial Peripheral Interface，SPI）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_SQPI"></a>

## 225.38 `CONFIG_USE_GD32_SQPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 串行／四线并行接口（Serial/Quad Parallel Interface，SQPI）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L219)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_SYSCFG"></a>

## 225.39 `CONFIG_USE_GD32_SYSCFG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 系统配置（System Configuration，SYSCFG）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_TIMER"></a>

## 225.40 `CONFIG_USE_GD32_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 定时器（Timer，TIMER）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_TIMER_GD32
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L234)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)、[`CONFIG_COUNTER_TIMER_GD32`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_TIMER_GD32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_TLI"></a>

## 225.41 `CONFIG_USE_GD32_TLI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 TFT-LCD 接口（TFT-LCD Interface，TLI）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_TMU"></a>

## 225.42 `CONFIG_USE_GD32_TMU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 三角函数数学单元（Trigonometric Math Unit，TMU）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:244`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L244)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_TRNG"></a>

## 225.43 `CONFIG_USE_GD32_TRNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 真随机数生成器（True Random Number Generator，TRNG）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**被选择（Selected by）**

```text
CONFIG_ENTROPY_GD32_TRNG
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:249`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L249)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)、[`CONFIG_ENTROPY_GD32_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GD32_TRNG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_TSI"></a>

## 225.44 `CONFIG_USE_GD32_TSI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 触摸感应接口（Touch Sensing Interface，TSI）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:254`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L254)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_USART"></a>

## 225.45 `CONFIG_USE_GD32_USART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 通用同步／异步收发器（Universal Synchronous/Asynchronous Receiver/Transmitter，USART）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**被选择（Selected by）**

```text
CONFIG_USART_GD32
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:259`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L259)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)、[`CONFIG_USART_GD32`](P169_drivers_serial_配置项参考_5.md#CONFIG_USART_GD32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_USBD"></a>

## 225.46 `CONFIG_USE_GD32_USBD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 通用串行总线全速设备接口（Universal Serial Bus full-speed Device interface，USBD）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_USBFS"></a>

## 225.47 `CONFIG_USE_GD32_USBFS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 通用串行总线全速 OTG（Universal Serial Bus on-the-go Full-Speed，USBFS）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:271`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L271)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_USBHS"></a>

## 225.48 `CONFIG_USE_GD32_USBHS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 通用串行总线高速接口（Universal Serial Bus High-Speed interface，USBHS）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:277`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L277)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<a id="CONFIG_USE_GD32_WWDGT"></a>

## 225.49 `CONFIG_USE_GD32_WWDGT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 窗口看门狗定时器（Window Watchdog Timer，WWDGT）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_GD32_HAL
```

**被选择（Selected by）**

```text
CONFIG_WWDGT_GD32
```

**定义位置（Location）**：[`modules/hal_gigadevice/Kconfig:283`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_gigadevice/Kconfig#L283)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_gigadevice（模块路径 `modules/hal/gigadevice`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_GD32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_GD32_HAL)、[`CONFIG_WWDGT_GD32`](P187_drivers_watchdog_配置项参考_2.md#CONFIG_WWDGT_GD32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_GD32_HAL`。

<!-- kconfig-navigation -->

[上一章](P224_modules_hal_ethos_u_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P226_modules_hal_infineon_配置项参考.md)
