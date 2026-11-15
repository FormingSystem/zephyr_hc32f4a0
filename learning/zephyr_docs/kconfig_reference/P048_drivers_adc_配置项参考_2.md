---
id: learning.zephyr-docs.kconfig-reference.page-48
title: "`drivers/adc`配置项参考（2/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第48章\_`drivers/adc`配置项参考（2/3）

本章翻译官方 Kconfig 数据库中 `drivers/adc` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ADC_MAX11102_17_ACQUISITION_THREAD_INIT_PRIO"></a>

## 48.1 `CONFIG_ADC_MAX11102_17_ACQUISITION_THREAD_INIT_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MAX11102_17 && CONFIG_ADC_ASYNC && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max11102_17:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max11102_17#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 美信 MAX11102–MAX11117（Maxim Integrated）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MAX11102_17`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_MAX11102_17)、[`CONFIG_ADC_ASYNC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ASYNC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MAX11102_17_ACQUISITION_THREAD_STACK_SIZE"></a>

## 48.2 `CONFIG_ADC_MAX11102_17_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MAX11102_17 && CONFIG_ADC_ASYNC && CONFIG_ADC
```

**默认值（Defaults）**

```text
400
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max11102_17:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max11102_17#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 美信 MAX11102–MAX11117（Maxim Integrated）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MAX11102_17`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_MAX11102_17)、[`CONFIG_ADC_ASYNC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ASYNC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MAX1125X"></a>

## 48.3 `CONFIG_ADC_MAX1125X`

**提示（Prompt）**：MAX1125X 驱动（Driver）

**说明（Help）**

启用 MAX1125X 的驱动实现（Driver Implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_MAXIM_MAX11254_ENABLED || DT_HAS_MAXIM_MAX11253_ENABLED) && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max1125x:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max1125x#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_MAX1125X_ACQUISITION_THREAD_PRIORITY"></a>

## 48.4 `CONFIG_ADC_MAX1125X_ACQUISITION_THREAD_PRIORITY`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部模数转换器（ADC）数据采集线程（Data Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MAX1125X && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max1125x:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max1125x#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MAX1125X 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MAX1125X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MAX1125X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MAX1125X_ACQUISITION_THREAD_STACK_SIZE"></a>

## 48.5 `CONFIG_ADC_MAX1125X_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MAX1125X && CONFIG_ADC
```

**默认值（Defaults）**

```text
400
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max1125x:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max1125x#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MAX1125X 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MAX1125X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MAX1125X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MAX1125X_ASYNC_THREAD_INIT_PRIORITY"></a>

## 48.6 `CONFIG_ADC_MAX1125X_ASYNC_THREAD_INIT_PRIORITY`

**提示（Prompt）**：MAX1125X ADC 异步线程优先级（Async Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MAX1125X && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max1125x:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max1125x#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MAX1125X 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MAX1125X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MAX1125X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MAX1125X_INIT_PRIORITY"></a>

## 48.7 `CONFIG_ADC_MAX1125X_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

ADS1X1X 模数转换器（ADC）设备驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MAX1125X && CONFIG_ADC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max1125x:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max1125x#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MAX1125X 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MAX1125X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MAX1125X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MAX2253X"></a>

## 48.8 `CONFIG_ADC_MAX2253X`

**提示（Prompt）**：MAX2253x 模数转换器驱动（ADC Driver）

**说明（Help）**

启用美信（Maxim）MAX2253X 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX2253X_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max2253x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max2253x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ADC_MAX2253X_ACQUISITION_THREAD_PRIORITY"></a>

## 48.9 `CONFIG_ADC_MAX2253X_ACQUISITION_THREAD_PRIORITY`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部模数转换器（ADC）数据采集线程（Data Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MAX2253X && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max2253x:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max2253x#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MAX2253x 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MAX2253X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MAX2253X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MAX2253X_ACQUISITION_THREAD_STACK_SIZE"></a>

## 48.10 `CONFIG_ADC_MAX2253X_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MAX2253X && CONFIG_ADC
```

**默认值（Defaults）**

```text
400
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max2253x:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max2253x#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MAX2253x 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MAX2253X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MAX2253X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MAX2253X_ASYNC_THREAD_INIT_PRIORITY"></a>

## 48.11 `CONFIG_ADC_MAX2253X_ASYNC_THREAD_INIT_PRIORITY`

**提示（Prompt）**：MAX2253X ADC 异步线程优先级（Async Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MAX2253X && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max2253x:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max2253x#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MAX2253x 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MAX2253X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MAX2253X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MAX2253X_INIT_PRIORITY"></a>

## 48.12 `CONFIG_ADC_MAX2253X_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

MAX2253X 设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MAX2253X && CONFIG_ADC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max2253x:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max2253x#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MAX2253x 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MAX2253X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MAX2253X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MAX2253X_STREAM"></a>

## 48.13 `CONFIG_ADC_MAX2253X_STREAM`

**提示（Prompt）**：MAX2253x 流式模式（Streaming Mode）

**说明（Help）**

启用美信（Maxim）MAX2253x 的流式模式（Streaming Mode）。这也意味着使用中断（Interrupt）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MAX2253X && CONFIG_SPI_RTIO && CONFIG_ADC
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max2253x:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max2253x#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MAX2253x 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MAX2253X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MAX2253X)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MAX32"></a>

## 48.14 `CONFIG_ADC_MAX32`

**提示（Prompt）**：MAX32 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 ADI MAX32xxx 微控制器（MCU）的模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_MAX32_STREAM"></a>

## 48.15 `CONFIG_ADC_MAX32_STREAM`

**提示（Prompt）**：使用先进先出队列传输数据流（FIFO Streaming）

**说明（Help）**

启用通过实时 I/O（RTIO）流式传输模数转换器（ADC）数据的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MAX32 && DT_HAS_ADI_MAX32_ADC_B_ME18_ENABLED && CONFIG_ADC
```

**主动选择（Selects）**

```text
CONFIG_ADC_ASYNC
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MAX32 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MAX32`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MAX32)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_ASYNC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ASYNC)。

<a id="CONFIG_ADC_MCHP_G1"></a>

## 48.16 `CONFIG_ADC_MCHP_G1`

**提示（Prompt）**：Microchip G1 外设的 ADC 支持（ADC Support for G1 Peripherals）

**说明（Help）**

启用 Microchip G1 模数转换器（ADC）外设上的 ADC 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_ADC_G1_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_MCP320X"></a>

## 48.17 `CONFIG_ADC_MCP320X`

**提示（Prompt）**：MCP3204 / MCP3208 驱动（Driver）

**说明（Help）**

启用 MCP3204 / MCP3208 模数转换器（ADC）驱动。MCP3204 / MCP3208 是带有 SPI 接口的 4／8 通道、12 位模数转换器（A/D Converter）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_MICROCHIP_MCP3204_ENABLED || DT_HAS_MICROCHIP_MCP3208_ENABLED) && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcp320x:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcp320x#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ADC_MCP320X_ACQUISITION_THREAD_PRIO"></a>

## 48.18 `CONFIG_ADC_MCP320X_ACQUISITION_THREAD_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部模数转换器（ADC）数据采集线程（Data Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCP320X && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcp320x:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcp320x#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MCP3204 / MCP3208 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCP320X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP320X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MCP320X_ACQUISITION_THREAD_STACK_SIZE"></a>

## 48.19 `CONFIG_ADC_MCP320X_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCP320X && CONFIG_ADC
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcp320x:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcp320x#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MCP3204 / MCP3208 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCP320X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP320X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MCP3221"></a>

## 48.20 `CONFIG_ADC_MCP3221`

**提示（Prompt）**：MCP3221 驱动（Driver）

**说明（Help）**

启用 MCP3221 模数转换器（ADC）驱动。MCP3221 是带有 I2C 接口的单通道、12 位模数转换器（A/D Converter）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MCP3221_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcp3221:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcp3221#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_ADC_MCP3221_ACQUISITION_THREAD_PRIO"></a>

## 48.21 `CONFIG_ADC_MCP3221_ACQUISITION_THREAD_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部模数转换器（ADC）数据采集线程（Data Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCP3221 && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcp3221:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcp3221#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MCP3221 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCP3221`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP3221)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MCP3221_ACQUISITION_THREAD_STACK_SIZE"></a>

## 48.22 `CONFIG_ADC_MCP3221_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCP3221 && CONFIG_ADC
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcp3221:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcp3221#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MCP3221 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCP3221`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP3221)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MCP356XR"></a>

## 48.23 `CONFIG_ADC_MCP356XR`

**提示（Prompt）**：MCP3561R / 2R / 4R 驱动（Driver）

**说明（Help）**

启用 MCP3561R / 2R / 4R 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MCP356XR_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcp356xr:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcp356xr#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_MCP356XR_ADC_CHANNEL_COUNT"></a>

## 48.24 `CONFIG_ADC_MCP356XR_ADC_CHANNEL_COUNT`

**提示（Prompt）**：ADC 通道数量（Number of ADC Channels）

**说明（Help）**

驱动必须支持的模数转换器（ADC）通道数量。每个通道需要 3 字节 RAM，保存该通道使用的 ADC 设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCP356XR && CONFIG_ADC
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcp356xr:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcp356xr#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MCP3561R / 2R / 4R 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCP356XR`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP356XR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MCP356XR_POLL"></a>

## 48.25 `CONFIG_ADC_MCP356XR_POLL`

**提示（Prompt）**：轮询 ADC 而不使用 IRQ 引脚（Poll ADC）

**说明（Help）**

定期轮询（Poll）模数转换器（ADC）以获取状态标志（Status Flag），而不是等待 ADC 触发的中断请求（IRQ）。ADC 的 IRQ 引脚未接线时很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCP356XR && CONFIG_ADC
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcp356xr:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcp356xr#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MCP3561R / 2R / 4R 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCP356XR`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP356XR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MCP356XR_POLLING_PERIOD_MS"></a>

## 48.26 `CONFIG_ADC_MCP356XR_POLLING_PERIOD_MS`

**提示（Prompt）**：两次 ADC 轮询之间的等待时间，单位为毫秒（Polling Interval）

**说明（Help）**

驱动内部采集线程（Acquisition Thread）在两次 ADC 轮询之间的等待时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCP356XR_POLL && CONFIG_ADC_MCP356XR && CONFIG_ADC
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcp356xr:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcp356xr#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MCP3561R / 2R / 4R 驱动（Driver） → 轮询 ADC 而不使用 IRQ 引脚（Poll ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCP356XR_POLL`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP356XR_POLL)、[`CONFIG_ADC_MCP356XR`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP356XR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MCP356XR_THREAD_PRIORITY"></a>

## 48.27 `CONFIG_ADC_MCP356XR_THREAD_PRIORITY`

**提示（Prompt）**：ADC 线程优先级（Thread Priority）

**说明（Help）**

内部模数转换器（ADC）线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCP356XR && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcp356xr:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcp356xr#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MCP3561R / 2R / 4R 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCP356XR`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP356XR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MCP356XR_THREAD_STACK_SIZE"></a>

## 48.28 `CONFIG_ADC_MCP356XR_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 线程栈大小（Thread Stack Size）

**说明（Help）**

内部模数转换器（ADC）线程使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCP356XR && CONFIG_ADC
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcp356xr:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcp356xr#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MCP3561R / 2R / 4R 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCP356XR`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP356XR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MCP356XR_USE_READ_CRC"></a>

## 48.29 `CONFIG_ADC_MCP356XR_USE_READ_CRC`

**提示（Prompt）**：使用 CRC 检查从 ADC 接收的数据（Received Data Check）

**说明（Help）**

在读取通信过程中使用循环冗余校验（CRC），检查从模数转换器（ADC）接收的数据的完整性（Integrity）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCP356XR && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcp356xr:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcp356xr#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → MCP3561R / 2R / 4R 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCP356XR`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP356XR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MCUX_12B1MSPS_SAR"></a>

## 48.30 `CONFIG_ADC_MCUX_12B1MSPS_SAR`

**提示（Prompt）**：MCUX 12B1MSPS SAR ADC 驱动（Driver）

**说明（Help）**

启用 MCUX 12B1MSPS 逐次逼近型模数转换器（SAR ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MCUX_12B1MSPS_SAR_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_MCUX_ADC12"></a>

## 48.31 `CONFIG_ADC_MCUX_ADC12`

**提示（Prompt）**：MCUX ADC12 驱动（Driver）

**说明（Help）**

启用 MCUX ADC12 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_ADC12_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_MCUX_ADC16"></a>

## 48.32 `CONFIG_ADC_MCUX_ADC16`

**提示（Prompt）**：MCUX ADC16 驱动（Driver）

**说明（Help）**

启用 MCUX ADC16 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_ADC16_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_MCUX_ADC16_CLK_DIV_RATIO_1"></a>

## 48.33 `CONFIG_ADC_MCUX_ADC16_CLK_DIV_RATIO_1`

**提示（Prompt）**：分频比为 1（Divide Ratio）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 时钟分频选择（Clock Divide Selection）

<a id="CONFIG_ADC_MCUX_ADC16_CLK_DIV_RATIO_2"></a>

## 48.34 `CONFIG_ADC_MCUX_ADC16_CLK_DIV_RATIO_2`

**提示（Prompt）**：分频比为 2（Divide Ratio）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 时钟分频选择（Clock Divide Selection）

<a id="CONFIG_ADC_MCUX_ADC16_CLK_DIV_RATIO_4"></a>

## 48.35 `CONFIG_ADC_MCUX_ADC16_CLK_DIV_RATIO_4`

**提示（Prompt）**：分频比为 4（Divide Ratio）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 时钟分频选择（Clock Divide Selection）

<a id="CONFIG_ADC_MCUX_ADC16_CLK_DIV_RATIO_8"></a>

## 48.36 `CONFIG_ADC_MCUX_ADC16_CLK_DIV_RATIO_8`

**提示（Prompt）**：分频比为 8（Divide Ratio）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 时钟分频选择（Clock Divide Selection）

<a id="CONFIG_ADC_MCUX_ADC16_ENABLE_EDMA"></a>

## 48.37 `CONFIG_ADC_MCUX_ADC16_ENABLE_EDMA`

**提示（Prompt）**：ADC 驱动的增强型直接内存访问（EDMA）

**说明（Help）**

启用 MCUX ADC16 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_MCUX_EDMA && CONFIG_ADC_MCUX_ADC16 && CONFIG_ADC
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_DMA_MCUX_EDMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA_MCUX_EDMA)、[`CONFIG_ADC_MCUX_ADC16`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_ADC16)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MCUX_ADC16_HW_TRIGGER"></a>

## 48.38 `CONFIG_ADC_MCUX_ADC16_HW_TRIGGER`

**提示（Prompt）**：ADC 硬件触发（HW Trigger）

**说明（Help）**

支持硬件触发（Hardware Trigger）的模数转换器（ADC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCUX_ADC16_ENABLE_EDMA && CONFIG_ADC_MCUX_ADC16 && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ADC 驱动的增强型直接内存访问（EDMA）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCUX_ADC16_ENABLE_EDMA`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_ADC16_ENABLE_EDMA)、[`CONFIG_ADC_MCUX_ADC16`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_ADC16)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MCUX_ADC16_VREF"></a>

## 48.39 `CONFIG_ADC_MCUX_ADC16_VREF`

**提示（Prompt）**：电压基准选择（Voltage Reference Selection）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCUX_ADC16 && CONFIG_ADC
```

**默认值（Defaults）**

```text
CONFIG_ADC_MCUX_ADC16_VREF_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ADC_MCUX_ADC16_VREF_DEFAULT
CONFIG_ADC_MCUX_ADC16_VREF_ALTERNATE
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCUX_ADC16`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_ADC16)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_MCUX_ADC16_VREF_DEFAULT`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_ADC16_VREF_DEFAULT)、[`CONFIG_ADC_MCUX_ADC16_VREF_ALTERNATE`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_ADC16_VREF_ALTERNATE)。

<a id="CONFIG_ADC_MCUX_ADC16_VREF_ALTERNATE"></a>

## 48.40 `CONFIG_ADC_MCUX_ADC16_VREF_ALTERNATE`

**提示（Prompt）**：备用参考电压对（Alternate Reference Pair）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADC_MCUX_ADC16_VREF>
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 电压基准选择（Voltage Reference Selection）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCUX_ADC16_VREF`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_ADC16_VREF)。

<a id="CONFIG_ADC_MCUX_ADC16_VREF_DEFAULT"></a>

## 48.41 `CONFIG_ADC_MCUX_ADC16_VREF_DEFAULT`

**提示（Prompt）**：默认参考电压对（Default Voltage Reference Pair）：`V_REFH` 和 `V_REFL`。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADC_MCUX_ADC16_VREF>
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 电压基准选择（Voltage Reference Selection）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCUX_ADC16_VREF`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_ADC16_VREF)。

<a id="CONFIG_ADC_MCUX_GAU"></a>

## 48.42 `CONFIG_ADC_MCUX_GAU`

**提示（Prompt）**：MCUX GAU ADC 驱动（Driver）

**说明（Help）**

启用 GAU 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_GAU_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_MCUX_LPADC"></a>

## 48.43 `CONFIG_ADC_MCUX_LPADC`

**提示（Prompt）**：MCUX LPADC 驱动（Driver）

**说明（Help）**

启用 MCUX LPADC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_LPADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
CONFIG_REGULATOR
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)、[`CONFIG_REGULATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_MCUX_LPADC_ACQUISITION_TIMEOUT_MS"></a>

## 48.44 `CONFIG_ADC_MCUX_LPADC_ACQUISITION_TIMEOUT_MS`

**提示（Prompt）**：LPADC 采集超时，单位为毫秒（Acquisition Timeout）

**说明（Help）**

阻塞式 `adc_read()` 等待转换序列（Conversion Sequence）完成的时间上限。如果不设置上限，永远无法完成的序列，例如转换器禁用时发出的触发，会使调用线程永久阻塞。超时后，驱动停止序列并返回 `-EAGAIN`。如果在较慢的 ADCK 下，串联多个通道并使用较高的硬件平均次数（Hardware Average Count），应增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCUX_LPADC && CONFIG_ADC
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[1, 60000]
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCUX_LPADC`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_LPADC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MCUX_LPADC_DMA_DRIVEN"></a>

## 48.45 `CONFIG_ADC_MCUX_LPADC_DMA_DRIVEN`

**提示（Prompt）**：使用 DMA 传输数据（Data Transfer）

**说明（Help）**

在 LPADC 驱动中使用直接内存访问（DMA）传输数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n && n && CONFIG_ADC_MCUX_LPADC && CONFIG_ADC
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCUX_LPADC`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_LPADC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_ADC_MSPM0_ADC12"></a>

## 48.46 `CONFIG_ADC_MSPM0_ADC12`

**提示（Prompt）**：TI MSPM0 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 TI MSPM0 系列的 ADC12 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_ADC12_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_MSPM0_DL_ADC
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mspm0:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mspm0#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_USE_MSPM0_DL_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_MSPM0_DL_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_MSPM0_DL_ADC`。

<a id="CONFIG_ADC_NPCX"></a>

## 48.47 `CONFIG_ADC_NPCX`

**提示（Prompt）**：新唐 NPCX 嵌入式控制器 ADC 驱动（Nuvoton Embedded Controller，EC）

**说明（Help）**

启用 NPCX 处理器系列的模数转换器（ADC）驱动。如果需要使用 NPCX 微控制器（MCU）上的 ADC 通道，选择 `y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_NPCX_CMP_V1"></a>

## 48.48 `CONFIG_ADC_NPCX_CMP_V1`

**提示（Prompt）**：ADC 比较器版本 1 支持（Comparator V1 Support）

**说明（Help）**

启用模数转换器（ADC）比较器（Comparator）V1 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || n) && CONFIG_ADC_NPCX && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.npcx:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.npcx#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 新唐 NPCX 嵌入式控制器 ADC 驱动（Nuvoton Embedded Controller，EC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_NPCX`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NPCX)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_NPCX_CMP_V2"></a>

## 48.49 `CONFIG_ADC_NPCX_CMP_V2`

**提示（Prompt）**：ADC 比较器版本 2 支持（Comparator V2 Support）

**说明（Help）**

启用模数转换器（ADC）比较器（Comparator）V2 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.npcx:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.npcx#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 新唐 NPCX 嵌入式控制器 ADC 驱动（Nuvoton Embedded Controller，EC）

<a id="CONFIG_ADC_NRFX_ADC"></a>

## 48.50 `CONFIG_ADC_NRFX_ADC`

**提示（Prompt）**：nRF ADC nrfx 驱动（Driver）

**说明（Help）**

启用面向 nRF51 微控制器（MCU）系列的 nrfx 模数转换器（ADC）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_ADC
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.nrfx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.nrfx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_NRFX_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_NRFX_ADC_CHANNEL_COUNT"></a>

## 48.51 `CONFIG_ADC_NRFX_ADC_CHANNEL_COUNT`

**提示（Prompt）**：ADC 通道数量（Number of ADC Channels）

**说明（Help）**

驱动需要支持的模数转换器（ADC）通道数量。每个通道都需要在 RAM 中使用一个专用结构体，保存采样该通道时使用的 ADC 设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_NRFX_ADC && CONFIG_ADC
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`drivers/adc/Kconfig.nrfx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.nrfx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → nRF ADC nrfx 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_NRFX_ADC`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NRFX_ADC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_NRFX_SAADC"></a>

## 48.52 `CONFIG_ADC_NRFX_SAADC`

**提示（Prompt）**：nRF SAADC nrfx 驱动（Driver）

**说明（Help）**

启用 nrfx SAADC 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_SAADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
CONFIG_NRFX_SAADC
```

**定义位置（Location）**：[`drivers/adc/Kconfig.nrfx:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.nrfx#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)、[`CONFIG_NRFX_SAADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_SAADC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_NUMAKER"></a>

## 48.53 `CONFIG_ADC_NUMAKER`

**提示（Prompt）**：新唐 NuMaker MCU 模数转换器驱动（Nuvoton ADC Driver）

**说明（Help）**

启用新唐（Nuvoton）NuMaker 处理器系列的模数转换器（ADC）驱动。如果需要启用 NuMaker ADC，选择 `y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_NUMAKER_ADC
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_HAS_NUMAKER_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_NXP_AON_LPADC"></a>

## 48.54 `CONFIG_ADC_NXP_AON_LPADC`

**提示（Prompt）**：恩智浦 AON_LPADC 驱动（NXP Driver）

**说明（Help）**

启用恩智浦（NXP）常开低功耗模数转换器（Always-On LPADC，AON_LPADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_AON_LPADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.nxp_aon_lpadc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.nxp_aon_lpadc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_NXP_S32_ADC_SAR"></a>

## 48.55 `CONFIG_ADC_NXP_S32_ADC_SAR`

**提示（Prompt）**：恩智浦 S32 SAR ADC 驱动（NXP Driver）

**说明（Help）**

启用恩智浦（NXP）S32 逐次逼近型模数转换器（SAR ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_ADC_SAR_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.nxp_s32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.nxp_s32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_NXP_SAR_ADC"></a>

## 48.56 `CONFIG_ADC_NXP_SAR_ADC`

**提示（Prompt）**：恩智浦 SAR ADC 驱动（NXP Driver）

**说明（Help）**

启用恩智浦（NXP）逐次逼近型模数转换器（SAR ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SAR_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_NXP_SAR_ADC_INTERRUPT"></a>

## 48.57 `CONFIG_ADC_NXP_SAR_ADC_INTERRUPT`

**提示（Prompt）**：恩智浦 SAR ADC 中断驱动模式（Interrupt-Driven Mode）

**说明（Help）**

使用中断驱动的转换（Interrupt-Driven Conversion）。启用后，驱动针对每个样本等待硬件转换结束中断（End-of-Conversion Interrupt）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_NXP_SAR_ADC && CONFIG_ADC
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_NXP_SAR_ADC`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NXP_SAR_ADC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_NXP_SAR_ADC_INTERRUPT_TIMEOUT"></a>

## 48.58 `CONFIG_ADC_NXP_SAR_ADC_INTERRUPT_TIMEOUT`

**提示（Prompt）**：恩智浦 SAR ADC 中断超时，单位为微秒（Interrupt Timeout）

**说明（Help）**

等待 ECH 中断（Interrupt）的超时时间，单位为微秒。设为 0 表示无限等待。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_NXP_SAR_ADC_INTERRUPT && CONFIG_ADC_NXP_SAR_ADC && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 恩智浦 SAR ADC 中断驱动模式（Interrupt-Driven Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADC_NXP_SAR_ADC_INTERRUPT`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NXP_SAR_ADC_INTERRUPT)、[`CONFIG_ADC_NXP_SAR_ADC`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NXP_SAR_ADC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_NXP_SAR_ADC_POLL_TIMEOUT"></a>

## 48.59 `CONFIG_ADC_NXP_SAR_ADC_POLL_TIMEOUT`

**提示（Prompt）**：恩智浦 SAR ADC 轮询超时，单位为微秒（Poll Timeout）

**说明（Help）**

轮询模式转换（Polling Mode Conversion）的超时时间，单位为微秒。仅在未启用 `ADC_NXP_SAR_ADC_INTERRUPT` 时使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_ADC_NXP_SAR_ADC_INTERRUPT && CONFIG_ADC_NXP_SAR_ADC && CONFIG_ADC
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_NXP_SAR_ADC_INTERRUPT`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NXP_SAR_ADC_INTERRUPT)、[`CONFIG_ADC_NXP_SAR_ADC`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NXP_SAR_ADC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_REALTEK_RTS5912"></a>

## 48.60 `CONFIG_ADC_REALTEK_RTS5912`

**提示（Prompt）**：瑞昱 RTS5912 模数转换器驱动（Realtek ADC Drivers）

**说明（Help）**

启用瑞昱（Realtek）RTS5912 处理器的模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.rts5912:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.rts5912#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_RENESAS_RA"></a>

## 48.61 `CONFIG_ADC_RENESAS_RA`

**提示（Prompt）**：瑞萨 RA 模数转换器（Renesas ADC）

**说明（Help）**

启用瑞萨（Renesas）RA 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_RENESAS_RA_ADC12_ENABLED || DT_HAS_RENESAS_RA_ADC16_ENABLED) && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_ADC
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.renesas_ra:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.renesas_ra#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_USE_RA_FSP_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_RENESAS_RA_ADC_B"></a>

## 48.62 `CONFIG_ADC_RENESAS_RA_ADC_B`

**提示（Prompt）**：瑞萨 RA ADC-B 版本（Renesas ADC-B Version）

**说明（Help）**

启用瑞萨（Renesas）RA 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_ADC_B_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_ADC_B
CONFIG_PINCTRL
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.renesas_ra:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.renesas_ra#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_USE_RA_FSP_ADC_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_ADC_B)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_RENESAS_RX"></a>

## 48.63 `CONFIG_ADC_RENESAS_RX`

**提示（Prompt）**：瑞萨 RX 模数转换器（Renesas ADC）

**说明（Help）**

启用瑞萨（Renesas）RX 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RX_RDP_ADC
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.renesas_rx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.renesas_rx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_USE_RX_RDP_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RX_RDP_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_RENESAS_RZ"></a>

## 48.64 `CONFIG_ADC_RENESAS_RZ`

**提示（Prompt）**：瑞萨 RZ 模数转换器驱动（Renesas ADC Driver）

**说明（Help）**

启用 RZ 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_ADC
```

**定义位置（Location）**：[`drivers/adc/Kconfig.renesas_rz:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.renesas_rz#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_USE_RZ_FSP_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_ADC)。

<a id="CONFIG_ADC_RENESAS_RZA2M"></a>

## 48.65 `CONFIG_ADC_RENESAS_RZA2M`

**提示（Prompt）**：瑞萨 A2M 模数转换器驱动（Renesas ADC Driver）

**说明（Help）**

启用瑞萨（Renesas）模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZA2M_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.renesas_rz:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.renesas_rz#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_RENESAS_RZ_ADC_C"></a>

## 48.66 `CONFIG_ADC_RENESAS_RZ_ADC_C`

**提示（Prompt）**：瑞萨 RZ ADC-C 驱动（Renesas Driver）

**说明（Help）**

启用 RZ ADC-C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_ADC_C_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_ADC_C
```

**定义位置（Location）**：[`drivers/adc/Kconfig.renesas_rz:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.renesas_rz#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_USE_RZ_FSP_ADC_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_ADC_C)。

<a id="CONFIG_ADC_RENESAS_RZ_ADC_E"></a>

## 48.67 `CONFIG_ADC_RENESAS_RZ_ADC_E`

**提示（Prompt）**：瑞萨 RZ ADC-E 驱动（Renesas Driver）

**说明（Help）**

启用 RZ ADC-E 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_ADC_E_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_ADC_E
```

**定义位置（Location）**：[`drivers/adc/Kconfig.renesas_rz:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.renesas_rz#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_USE_RZ_FSP_ADC_E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_ADC_E)。

<a id="CONFIG_ADC_RPI_PICO"></a>

## 48.68 `CONFIG_ADC_RPI_PICO`

**提示（Prompt）**：树莓派 Pico 模数转换器驱动（Raspberry Pi Pico ADC Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_ADC_ENABLED && CONFIG_RESET && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PICOSDK_USE_ADC
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PICOSDK_USE_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_SAM"></a>

## 48.69 `CONFIG_ADC_SAM`

**提示（Prompt）**：Atmel SAM 系列模数转换器驱动（ADC Driver）

**说明（Help）**

启用 Atmel SAM 微控制器（MCU）系列的模数转换器（Analog-to-Digital Converter，ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.sam:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.sam#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_SAM0"></a>

## 48.70 `CONFIG_ADC_SAM0`

**提示（Prompt）**：Atmel SAM0 系列模数转换器驱动（ADC Driver）

**说明（Help）**

启用 Atmel SAM0 微控制器（MCU）系列的模数转换器（Analog-to-Digital Converter，ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.sam0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.sam0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_SAM_AFEC"></a>

## 48.71 `CONFIG_ADC_SAM_AFEC`

**提示（Prompt）**：SAM 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 Atmel SAM 微控制器（MCU）系列基于 AFEC 模块的模数转换器（Analog-to-Digital Converter，ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_AFEC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.sam_afec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.sam_afec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_SEQUENCE_PRIORITY"></a>

## 48.72 `CONFIG_ADC_SEQUENCE_PRIORITY`

**提示（Prompt）**：转换序列优先级支持（Sequence Priority Support）

**说明（Help）**

允许为模数转换器（ADC）的转换序列（Sequence）分配优先级。序列的优先级反映其相对于其他序列的时间敏感程度（Time Sensitivity）。支持的优先级数量，以及为序列指定某个优先级后得到的具体行为，都由硬件决定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_HAS_SEQUENCE_PRIORITY && CONFIG_ADC
```

**定义位置（Location）**：[`drivers/adc/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_HAS_SEQUENCE_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_HAS_SEQUENCE_PRIORITY)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_HAS_SEQUENCE_PRIORITY`。

<a id="CONFIG_ADC_SF32LB"></a>

## 48.73 `CONFIG_ADC_SF32LB`

**提示（Prompt）**：SF32LB 微控制器系列的 ADC 驱动（MCU ADC Driver）

**说明（Help）**

启用 SF32LB 微控制器（MCU）系列的模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_GPADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_SHELL"></a>

## 48.74 `CONFIG_ADC_SHELL`

**提示（Prompt）**：ADC 命令行（ADC Shell）

**说明（Help）**

启用用于测试的模数转换器命令行（ADC Shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_ADC
```

**定义位置（Location）**：[`drivers/adc/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_SHELL_PERIODIC_READ_STACK_SIZE"></a>

## 48.75 `CONFIG_ADC_SHELL_PERIODIC_READ_STACK_SIZE`

**提示（Prompt）**：ADC 命令行周期读取线程栈大小（Periodic Read Thread Stack Size）

**说明（Help）**

执行周期性 `adc <device> read <channel> <period_ms>` 命令并采集样本的线程栈大小（Thread Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_SHELL && CONFIG_ADC
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/adc/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ADC 命令行（ADC Shell）

**配置项引用（Symbol References）**：[`CONFIG_ADC_SHELL`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_SHELL)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_SILABS_ADC"></a>

## 48.76 `CONFIG_ADC_SILABS_ADC`

**提示（Prompt）**：Silicon Labs SAR ADC 驱动（Driver）

**说明（Help）**

启用 Silicon Labs 逐次逼近型模数转换器（SAR ADC）的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SERIES3_ADC_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_ADC
CONFIG_ADC_CONFIGURABLE_INPUTS
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.silabs:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.silabs#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SILABS_SISDK_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_SILABS_ADC_DMA"></a>

## 48.77 `CONFIG_ADC_SILABS_ADC_DMA`

**提示（Prompt）**：Silicon Labs SAR ADC 异步 DMA 支持（Async DMA Support）

**说明（Help）**

启用 Silicon Labs ADC 驱动的直接内存访问（DMA）支持，使模数转换（ADC Conversion）可以使用 DMA 执行，无论是否异步，从而提高性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/adc/Kconfig.silabs:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.silabs#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → Silicon Labs SAR ADC 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_ADC_SILABS_IADC"></a>

## 48.78 `CONFIG_ADC_SILABS_IADC`

**提示（Prompt）**：Silicon Labs 增量式模数转换器驱动（Incremental ADC Driver）

**说明（Help）**

启用 Silicon Labs 增量式模数转换器（Incremental ADC）的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_IADC_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_IADC
CONFIG_ADC_CONFIGURABLE_INPUTS
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.silabs:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.silabs#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SILABS_SISDK_IADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_IADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_SILABS_IADC_DMA"></a>

## 48.79 `CONFIG_ADC_SILABS_IADC_DMA`

**提示（Prompt）**：Silicon Labs IADC 异步 DMA 支持（Async DMA Support）

**说明（Help）**

启用 Silicon Labs IADC 驱动的直接内存访问（DMA）支持，使模数转换（ADC Conversion）可以使用 DMA 执行，无论是否异步，从而提高性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/adc/Kconfig.silabs:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.silabs#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → Silicon Labs 增量式模数转换器驱动（Incremental ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_ADC_SILABS_SIWX91X"></a>

## 48.80 `CONFIG_ADC_SILABS_SIWX91X`

**提示（Prompt）**：Silicon Labs Siwx91x MCU 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 Silicon Labs Siwx91x 模数转换器（ADC）的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_ADC_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.silabs:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.silabs#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_SMARTBOND_GPADC"></a>

## 48.81 `CONFIG_ADC_SMARTBOND_GPADC`

**提示（Prompt）**：瑞萨 SmartBond™ ADC 的模数转换器驱动（Renesas ADC Driver）

**说明（Help）**

启用瑞萨（Renesas）SmartBond™ 微控制器（MCU）系列的模数转换器（ADC）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.smartbond:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.smartbond#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_SMARTBOND_SDADC"></a>

## 48.82 `CONFIG_ADC_SMARTBOND_SDADC`

**提示（Prompt）**：瑞萨 SmartBond™ Σ-Δ 模数转换器驱动（Renesas Sigma-Delta ADC Driver）

**说明（Help）**

启用瑞萨（Renesas）SmartBond™ 微控制器（MCU）系列的模数转换器（ADC）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_SDADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.smartbond:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.smartbond#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_STM32"></a>

## 48.83 `CONFIG_ADC_STM32`

**提示（Prompt）**：STM32 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 STM32xx 模数转换器（ADC）的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_ADC_ASYNC if CONFIG_ADC_STREAM
CONFIG_ADC_HAS_SEQUENCE_PRIORITY if n
```

**定义位置（Location）**：[`drivers/adc/Kconfig.stm32:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.stm32#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_ADC_ASYNC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ASYNC)、[`CONFIG_ADC_STREAM`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STREAM)、[`CONFIG_ADC_HAS_SEQUENCE_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_HAS_SEQUENCE_PRIORITY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_HAS_SEQUENCE_PRIORITY`。

<a id="CONFIG_ADC_STM32WB0"></a>

## 48.84 `CONFIG_ADC_STM32WB0`

**提示（Prompt）**：STM32WB0 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 STM32WB0 系列模数转换器（ADC）的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32WB0_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.stm32:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.stm32#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_STM32_DMA"></a>

## 48.85 `CONFIG_ADC_STM32_DMA`

**提示（Prompt）**：STM32 MCU ADC 直接内存访问支持（DMA Support）

**说明（Help）**

为在设备树节点（Devicetree Node）中启用 DMA 通道的 ADC 实例，启用直接内存访问（DMA）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ADC_STM32 || CONFIG_ADC_STM32WB0) && CONFIG_ADC
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/adc/Kconfig.stm32:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.stm32#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_STM32`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STM32)、[`CONFIG_ADC_STM32WB0`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STM32WB0)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_ADC_STM32_INJECTED_CHANNELS"></a>

## 48.86 `CONFIG_ADC_STM32_INJECTED_CHANNELS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用注入通道（Injected Channel）支持。要将序列定义为注入序列，将 `struct adc_sequence` 的 `priority` 字段设为 1；规则序列（Regular Sequence）应设为 0，其他值都会返回错误。

使用注入通道时，建议在开始任何测量之前配置好将使用的所有通道，包括规则通道与注入通道。因为转换运行期间无法配置新通道；典型情况是规则转换（Regular Conversion）正在进行时，无法配置注入通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_SEQUENCE_PRIORITY && (CONFIG_ADC_STM32 || CONFIG_ADC_STM32WB0) && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.stm32:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.stm32#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_SEQUENCE_PRIORITY`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_SEQUENCE_PRIORITY)、[`CONFIG_ADC_STM32`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STM32)、[`CONFIG_ADC_STM32WB0`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STM32WB0)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_STM32_VREFINT_CALIBRATE"></a>

## 48.87 `CONFIG_ADC_STM32_VREFINT_CALIBRATE`

**提示（Prompt）**：初始化／校准时通过 VREFINT 测量 VREF+（Measure VREF+）

**说明（Help）**

使用 VREFINT 通道及 `st,stm32-vref` 节点描述的出厂校准（Factory Calibration），测量 ADC 参考电源轨（Reference Rail），即 `VREF+` / `VDDA`。这些节点的 `io-channels` 指定的每个 ADC 都可以执行测量，包括被禁用的节点所指定的 ADC。测量值在整个片上系统（SoC）范围内缓存；所有 STM32 ADC 实例在使用 `ADC_REF_INTERNAL` 时，都会通过 `adc_ref_internal()` / `adc_ref_get()` 返回此值。

在任何支持 VREFINT 的 ADC 上设置 `sequence.calibrate` 时，会重新测量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_STM32 && DT_HAS_ST_STM32_VREF_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.stm32:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.stm32#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → STM32 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_STM32`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STM32)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_STM32_VREFINT_CALIB_VIA_NVMEM"></a>

## 48.88 `CONFIG_ADC_STM32_VREFINT_CALIB_VIA_NVMEM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过非易失性存储器（NVMEM）API 读取 `VREFINT_CAL`，而不是使用原始的一次性可编程存储器（OTP）指针。此选项独立于传感器配置 `CONFIG_STM32_VREF`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_STM32_VREFINT_CALIBRATE && CONFIG_OTP && CONFIG_NVMEM && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.stm32:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.stm32#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → STM32 模数转换器驱动（ADC Driver） → 初始化／校准时通过 VREFINT 测量 VREF+（Measure VREF+）

**配置项引用（Symbol References）**：[`CONFIG_ADC_STM32_VREFINT_CALIBRATE`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STM32_VREFINT_CALIBRATE)、[`CONFIG_OTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OTP)、[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_STREAM"></a>

## 48.89 `CONFIG_ADC_STREAM`

**提示（Prompt）**：ADC 流式传输支持（Stream Support）

**说明（Help）**

启用流式 API 调用（Stream API Calls）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC
```

**主动选择（Selects）**

```text
CONFIG_RTIO
CONFIG_RTIO_SYS_MEM_BLOCKS
CONFIG_RTIO_CONSUME_SEM
```

**定义位置（Location）**：[`drivers/adc/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO)、[`CONFIG_RTIO_SYS_MEM_BLOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_SYS_MEM_BLOCKS)、[`CONFIG_RTIO_CONSUME_SEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_CONSUME_SEM)。

<a id="CONFIG_ADC_TELINK_B91"></a>

## 48.90 `CONFIG_ADC_TELINK_B91`

**提示（Prompt）**：泰凌微 B91 模数转换器驱动（Telink Semiconductor ADC Driver）

**说明（Help）**

启用泰凌微（Telink）B91 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TELINK_B91_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.b91:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.b91#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_TI_AM335X"></a>

## 48.91 `CONFIG_ADC_TI_AM335X`

**提示（Prompt）**：TI 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 TI AM335x 模数转换器（Analog-to-Digital Converter，ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_AM335X_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ti_am335x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ti_am335x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_TLA202X"></a>

## 48.92 `CONFIG_ADC_TLA202X`

**提示（Prompt）**：德州仪器 TLA202x 低功耗模数转换器（Texas Instruments Low-Power ADC）

**说明（Help）**

TLA202x 是经过成本优化、超小型、12 位的系统监测模数转换器（Cost-Optimized, Ultra-Small, System-Monitoring ADC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_TLA2021_ENABLED || DT_HAS_TI_TLA2022_ENABLED || DT_HAS_TI_TLA2024_ENABLED) && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_ADC_CONFIGURABLE_INPUTS if DT_HAS_TI_TLA2024_ENABLED
```

**定义位置（Location）**：[`drivers/adc/Kconfig.tla202x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.tla202x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_TLA202X_ACQUISITION_THREAD_PRIORITY"></a>

## 48.93 `CONFIG_ADC_TLA202X_ACQUISITION_THREAD_PRIORITY`

**提示（Prompt）**：数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）的执行优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ASYNC && CONFIG_ADC_TLA202X && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.tla202x:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.tla202x#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 TLA202x 低功耗模数转换器（Texas Instruments Low-Power ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ASYNC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ASYNC)、[`CONFIG_ADC_TLA202X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_TLA202X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_TLA202X_ACQUISITION_THREAD_STACK_SIZE"></a>

## 48.94 `CONFIG_ADC_TLA202X_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）的栈大小。需要为 I2C 操作留出空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ASYNC && CONFIG_ADC_TLA202X && CONFIG_ADC
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/adc/Kconfig.tla202x:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.tla202x#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 TLA202x 低功耗模数转换器（Texas Instruments Low-Power ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ASYNC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ASYNC)、[`CONFIG_ADC_TLA202X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_TLA202X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_TLA202X_INIT_PRIORITY"></a>

## 48.95 `CONFIG_ADC_TLA202X_INIT_PRIORITY`

**提示（Prompt）**：驱动初始化优先级（Driver Initialization Priority）

**说明（Help）**

微调驱动初始化优先级。确保其数值大于 `I2C_INIT_PRIORITY`，也就是实际优先级更低。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_TLA202X && CONFIG_ADC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/adc/Kconfig.tla202x:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.tla202x#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 TLA202x 低功耗模数转换器（Texas Instruments Low-Power ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_TLA202X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_TLA202X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_TLA2528"></a>

## 48.96 `CONFIG_ADC_TLA2528`

**提示（Prompt）**：德州仪器 TLA2528 I2C（Texas Instruments TLA2528 I2C）

**说明（Help）**

启用 TLA2528 模数转换器（ADC）的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TLA2528_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/adc/Kconfig.tla2528:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.tla2528#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_ADC_TLA2528_INIT_PRIO"></a>

## 48.97 `CONFIG_ADC_TLA2528_INIT_PRIO`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级。实际优先级必须低于 TLA2528 多功能设备（MFD）驱动，即数值必须更大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_TLA2528 && CONFIG_ADC
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`drivers/adc/Kconfig.tla2528:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.tla2528#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 TLA2528 I2C（Texas Instruments TLA2528 I2C）

**配置项引用（Symbol References）**：[`CONFIG_ADC_TLA2528`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_TLA2528)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_VF610"></a>

## 48.98 `CONFIG_ADC_VF610`

**提示（Prompt）**：VF610 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 VF610 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_VF610_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.vf610:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.vf610#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_XEC"></a>

## 48.99 `CONFIG_ADC_XEC`

**提示（Prompt）**：Microchip XEC 系列模数转换器驱动（ADC Driver）

**说明（Help）**

启用 Microchip XEC 微控制器（MCU）系列的模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.xec:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.xec#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_XMC4XXX"></a>

## 48.100 `CONFIG_ADC_XMC4XXX`

**提示（Prompt）**：XMC4XXX 模数转换器（ADC）

**说明（Help）**

启用 XMC4XXX 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.xmc4xxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.xmc4xxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<!-- kconfig-navigation -->

[上一章](P047_drivers_adc_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P049_drivers_adc_配置项参考_3.md)
