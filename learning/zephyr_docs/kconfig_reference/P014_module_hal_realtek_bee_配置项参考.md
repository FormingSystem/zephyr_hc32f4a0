---
id: learning.zephyr-docs.kconfig-reference.page-14
title: "`<module:hal_realtek>/bee`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第14章\_`<module:hal_realtek>/bee`配置项参考

本章翻译官方 Kconfig 数据库中 `<module:hal_realtek>/bee` 的 29 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_REALTEK_BEE_ADC"></a>

## 14.1 `CONFIG_REALTEK_BEE_ADC`

**提示（Prompt）**：Realtek Bee 模数转换器（ADC）驱动

**说明（Help）**

此选项启用 Realtek Bee 的模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_ADC
CONFIG_WRAP_REALTEK_BEE_ADC
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/adc/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_ADC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_ADC`。

<a id="CONFIG_REALTEK_BEE_AON_QDEC"></a>

## 14.2 `CONFIG_REALTEK_BEE_AON_QDEC`

**提示（Prompt）**：Realtek Bee 常开域正交解码器（AON QDEC）驱动

**说明（Help）**

此选项启用 Realtek Bee 的常开域正交解码器（AON QDEC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_AON_QDEC
CONFIG_WRAP_REALTEK_BEE_AON_QDEC
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/qdec/Kconfig:10`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_AON_QDEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_AON_QDEC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_AON_QDEC`。

<a id="CONFIG_REALTEK_BEE_AON_WDT"></a>

## 14.3 `CONFIG_REALTEK_BEE_AON_WDT`

**提示（Prompt）**：Realtek Bee MCU 常开域看门狗定时器（AON Watchdog Timer）

**说明（Help）**

此选项启用 Realtek Bee 系列处理器的常开域看门狗定时器（AON WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_AON_WDT
CONFIG_WRAP_REALTEK_BEE_AON_WDT
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/wdt/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_AON_WDT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_AON_WDT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_AON_WDT`。

<a id="CONFIG_REALTEK_BEE_BT"></a>

## 14.4 `CONFIG_REALTEK_BEE_BT`

**提示（Prompt）**：Realtek Bee MCU 蓝牙（Bluetooth）驱动

**说明（Help）**

此选项启用 Realtek Bee 系列处理器的蓝牙（Bluetooth）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAL_REALTEK_BEE_BT && (CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA)
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/bluetooth/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAL_REALTEK_BEE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_BT)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_BT`、`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_REALTEK_BEE_CAN"></a>

## 14.5 `CONFIG_REALTEK_BEE_CAN`

**提示（Prompt）**：Realtek Bee 控制器局域网（CAN）驱动

**说明（Help）**

此选项启用 Realtek Bee 的控制器局域网（CAN）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_CAN
CONFIG_WRAP_REALTEK_BEE_CAN
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/can/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_CAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_CAN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_CAN`。

<a id="CONFIG_REALTEK_BEE_CODEC"></a>

## 14.6 `CONFIG_REALTEK_BEE_CODEC`

**提示（Prompt）**：Realtek Bee 编解码器（CODEC）驱动

**说明（Help）**

此选项启用 Realtek Bee 的编解码器（Codec）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_CODEC
CONFIG_WRAP_REALTEK_BEE_CODEC
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/codec/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_CODEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_CODEC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_CODEC`。

<a id="CONFIG_REALTEK_BEE_CORE_WDT"></a>

## 14.7 `CONFIG_REALTEK_BEE_CORE_WDT`

**提示（Prompt）**：Realtek Bee MCU 内核看门狗定时器（Core Watchdog Timer）

**说明（Help）**

此选项启用 Realtek Bee 系列处理器的内核看门狗定时器（Core WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_CORE_WDT
CONFIG_WRAP_REALTEK_BEE_CORE_WDT
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/wdt/Kconfig:12`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_CORE_WDT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_CORE_WDT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_CORE_WDT`。

<a id="CONFIG_REALTEK_BEE_DMA"></a>

## 14.8 `CONFIG_REALTEK_BEE_DMA`

**提示（Prompt）**：Realtek Bee 直接存储器访问（DMA）驱动

**说明（Help）**

此选项启用 Realtek Bee 的直接存储器访问（DMA）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_DMA
CONFIG_WRAP_REALTEK_BEE_DMA
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/dma/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_DMA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_DMA`。

<a id="CONFIG_REALTEK_BEE_ENHTIMER"></a>

## 14.9 `CONFIG_REALTEK_BEE_ENHTIMER`

**提示（Prompt）**：Realtek Bee 增强定时器（ENHTIMER）驱动

**说明（Help）**

此选项启用 Realtek Bee 的增强定时器（ENHTIMER）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_ENHTIM
CONFIG_WRAP_REALTEK_BEE_ENHTIM
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/timer/Kconfig:10`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_ENHTIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_ENHTIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_ENHTIM`。

<a id="CONFIG_REALTEK_BEE_GPIO"></a>

## 14.10 `CONFIG_REALTEK_BEE_GPIO`

**提示（Prompt）**：Realtek Bee 通用输入／输出（GPIO）驱动

**说明（Help）**

此选项启用 Realtek Bee 的通用输入／输出（GPIO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_GPIO
CONFIG_WRAP_REALTEK_BEE_GPIO
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/gpio/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_GPIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_GPIO`。

<a id="CONFIG_REALTEK_BEE_GRTC"></a>

## 14.11 `CONFIG_REALTEK_BEE_GRTC`

**提示（Prompt）**：Realtek Bee GRTC 驱动

**说明（Help）**

此选项启用 Realtek Bee 的 GRTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/rtc/Kconfig:10`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_REALTEK_BEE_I2C"></a>

## 14.12 `CONFIG_REALTEK_BEE_I2C`

**提示（Prompt）**：Realtek Bee I2C 驱动

**说明（Help）**

此选项启用 Realtek Bee 的 I2C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_I2C
CONFIG_WRAP_REALTEK_BEE_I2C
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/i2c/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_I2C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_I2C`。

<a id="CONFIG_REALTEK_BEE_I2S"></a>

## 14.13 `CONFIG_REALTEK_BEE_I2S`

**提示（Prompt）**：Realtek Bee I2S 驱动

**说明（Help）**

此选项启用 Realtek Bee 的 I2S 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_I2S
CONFIG_WRAP_REALTEK_BEE_I2S
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/i2s/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_I2S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_I2S)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_I2S`。

<a id="CONFIG_REALTEK_BEE_IR"></a>

## 14.14 `CONFIG_REALTEK_BEE_IR`

**提示（Prompt）**：Realtek Bee 红外（IR）驱动

**说明（Help）**

此选项启用 Realtek Bee 的红外（IR）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_IR
CONFIG_WRAP_REALTEK_BEE_IR
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/ir/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_IR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_IR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_IR`。

<a id="CONFIG_REALTEK_BEE_KEYSCAN"></a>

## 14.15 `CONFIG_REALTEK_BEE_KEYSCAN`

**提示（Prompt）**：Realtek Bee 按键扫描（KEYSCAN）驱动

**说明（Help）**

此选项启用 Realtek Bee 的按键扫描（KEYSCAN）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_KEYSCAN
CONFIG_WRAP_REALTEK_BEE_KEYSCAN
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/keyscan/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_KEYSCAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_KEYSCAN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_KEYSCAN`。

<a id="CONFIG_REALTEK_BEE_LPQDEC"></a>

## 14.16 `CONFIG_REALTEK_BEE_LPQDEC`

**提示（Prompt）**：Realtek Bee 低功耗正交解码器（LP QDEC）驱动

**说明（Help）**

此选项启用 Realtek Bee 的低功耗正交解码器（LP QDEC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/qdec/Kconfig:16`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_REALTEK_BEE_MAC_802154"></a>

## 14.17 `CONFIG_REALTEK_BEE_MAC_802154`

**提示（Prompt）**：Realtek Bee MCU IEEE 802.15.4 媒体访问控制（MAC）驱动

**说明（Help）**

此选项启用 Realtek Bee MCU 的 IEEE 802.15.4 媒体访问控制（MAC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/mac_802154/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_REALTEK_BEE_NVIC"></a>

## 14.18 `CONFIG_REALTEK_BEE_NVIC`

**提示（Prompt）**：Realtek Bee 中断请求（IRQ）驱动

**说明（Help）**

此选项启用 Realtek Bee 的中断请求（IRQ）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_NVIC
CONFIG_WRAP_REALTEK_BEE_NVIC
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/irq/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_NVIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_NVIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_NVIC`。

<a id="CONFIG_REALTEK_BEE_PINMUX"></a>

## 14.19 `CONFIG_REALTEK_BEE_PINMUX`

**提示（Prompt）**：Realtek Bee 引脚复用（PINMUX）驱动

**说明（Help）**

此选项启用 Realtek Bee 的引脚复用（PINMUX）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_PINMUX
CONFIG_WRAP_REALTEK_BEE_PINMUX
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/pinmux/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_PINMUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_PINMUX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_PINMUX`。

<a id="CONFIG_REALTEK_BEE_PWM"></a>

## 14.20 `CONFIG_REALTEK_BEE_PWM`

**提示（Prompt）**：Realtek Bee 脉宽调制（PWM）驱动

**说明（Help）**

此选项启用 Realtek Bee 的脉宽调制（PWM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/pwm/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_REALTEK_BEE_QDEC"></a>

## 14.21 `CONFIG_REALTEK_BEE_QDEC`

**提示（Prompt）**：Realtek Bee 正交解码器（QDEC）驱动

**说明（Help）**

此选项启用 Realtek Bee 的正交解码器（QDEC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_QDEC
CONFIG_WRAP_REALTEK_BEE_QDEC
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/qdec/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_QDEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_QDEC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_QDEC`。

<a id="CONFIG_REALTEK_BEE_RCC"></a>

## 14.22 `CONFIG_REALTEK_BEE_RCC`

**提示（Prompt）**：Realtek Bee 复位与时钟控制（RCC）驱动

**说明（Help）**

此选项启用 Realtek Bee 的复位与时钟控制（RCC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_RCC
CONFIG_WRAP_REALTEK_BEE_RCC
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/rcc/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_RCC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_RCC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_RCC`。

<a id="CONFIG_REALTEK_BEE_RTC"></a>

## 14.23 `CONFIG_REALTEK_BEE_RTC`

**提示（Prompt）**：Realtek Bee 实时时钟（RTC）驱动

**说明（Help）**

此选项启用 Realtek Bee 的实时时钟（RTC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_RTC
CONFIG_WRAP_REALTEK_BEE_RTC
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/rtc/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_RTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_RTC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_RTC`。

<a id="CONFIG_REALTEK_BEE_SDHC"></a>

## 14.24 `CONFIG_REALTEK_BEE_SDHC`

**提示（Prompt）**：Realtek Bee SD 主机控制器（SDHC）驱动

**说明（Help）**

此选项启用 Realtek Bee MCU 的 SD 主机控制器（SDHC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_SDHC
CONFIG_WRAP_REALTEK_BEE_SDHC
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/sdhc/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_SDHC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_SDHC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_SDHC`。

<a id="CONFIG_REALTEK_BEE_SPI"></a>

## 14.25 `CONFIG_REALTEK_BEE_SPI`

**提示（Prompt）**：Realtek Bee 串行外设接口（SPI）驱动

**说明（Help）**

此选项启用 Realtek Bee 的串行外设接口（SPI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_SPI
CONFIG_WRAP_REALTEK_BEE_SPI
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/spi/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_SPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_SPI`。

<a id="CONFIG_REALTEK_BEE_TIMER"></a>

## 14.26 `CONFIG_REALTEK_BEE_TIMER`

**提示（Prompt）**：Realtek Bee 定时器（TIMER）驱动

**说明（Help）**

此选项启用 Realtek Bee 的定时器（Timer）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_TIM
CONFIG_WRAP_REALTEK_BEE_TIM
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/timer/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_TIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_TIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_TIM`。

<a id="CONFIG_REALTEK_BEE_UART"></a>

## 14.27 `CONFIG_REALTEK_BEE_UART`

**提示（Prompt）**：Realtek Bee 通用异步收发器（UART）驱动

**说明（Help）**

此选项启用 Realtek Bee 的通用异步收发器（UART）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_UART
CONFIG_WRAP_REALTEK_BEE_UART
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/uart/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_UART)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_UART`。

<a id="CONFIG_REALTEK_BEE_USB"></a>

## 14.28 `CONFIG_REALTEK_BEE_USB`

**提示（Prompt）**：Realtek Bee MCU 通用串行总线（USB）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_WRAP_REALTEK_BEE_USB
CONFIG_WRAP_REALTEK_BEE_USB
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/usb/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_WRAP_REALTEK_BEE_USB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WRAP_REALTEK_BEE_USB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`、`CONFIG_WRAP_REALTEK_BEE_USB`。

<a id="CONFIG_REALTEK_BEE_USING_USB_HAL"></a>

## 14.29 `CONFIG_REALTEK_BEE_USING_USB_HAL`

**提示（Prompt）**：Realtek Bee USB 硬件抽象层库（HAL Library）

**说明（Help）**

此选项启用 Realtek Bee MCU 的 USB 硬件抽象层库（HAL Library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE || CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
y if CONFIG_REALTEK_BEE_USB
```

**定义位置（Location）**：`<module:hal_realtek>/bee/drivers/usb/Kconfig:8`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 硬件抽象层驱动（HAL Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_REALTEK_BEE_USB`](P014_module_hal_realtek_bee_配置项参考.md#CONFIG_REALTEK_BEE_USB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`、`CONFIG_HAS_REALTEK_AMEBA`。

<!-- kconfig-navigation -->

[上一章](P013_module_hal_realtek_ameba_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P015_module_lvgl_zephyr_配置项参考_1.md)
