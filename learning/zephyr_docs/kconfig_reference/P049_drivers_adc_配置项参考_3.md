---
id: learning.zephyr-docs.kconfig-reference.page-49
title: "`drivers/adc`配置项参考（3/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第49章\_`drivers/adc`配置项参考（3/3）

本章翻译官方 Kconfig 数据库中 `drivers/adc` 的 7 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ADI_AD4130_ADC_ACQUISITION_THREAD_PRIO"></a>

## 49.1 `CONFIG_ADI_AD4130_ADC_ACQUISITION_THREAD_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_AD4130 && CONFIG_ADC_ASYNC && CONFIG_ADC
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad4130:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad4130#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ADI AD4130 模数转换器（Analog-to-Digital Converter）

**配置项引用（Symbol References）**：[`CONFIG_ADC_AD4130`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD4130)、[`CONFIG_ADC_ASYNC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ASYNC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADI_AD4130_ADC_ACQUISITION_THREAD_STACK_SIZE"></a>

## 49.2 `CONFIG_ADI_AD4130_ADC_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_AD4130 && CONFIG_ADC_ASYNC && CONFIG_ADC
```

**默认值（Defaults）**

```text
400
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad4130:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad4130#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ADI AD4130 模数转换器（Analog-to-Digital Converter）

**配置项引用（Symbol References）**：[`CONFIG_ADC_AD4130`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD4130)、[`CONFIG_ADC_ASYNC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ASYNC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADI_AD4170_ADC_ACQUISITION_THREAD_PRIO"></a>

## 49.3 `CONFIG_ADI_AD4170_ADC_ACQUISITION_THREAD_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_AD4170 && CONFIG_ADC_ASYNC && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad4170:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad4170#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ADI AD4170 及同类模数转换器（Analog-to-Digital Converters）

**配置项引用（Symbol References）**：[`CONFIG_ADC_AD4170`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD4170)、[`CONFIG_ADC_ASYNC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ASYNC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADI_AD4170_ADC_ACQUISITION_THREAD_STACK_SIZE"></a>

## 49.4 `CONFIG_ADI_AD4170_ADC_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_AD4170 && CONFIG_ADC_ASYNC && CONFIG_ADC
```

**默认值（Defaults）**

```text
400
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad4170:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad4170#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ADI AD4170 及同类模数转换器（Analog-to-Digital Converters）

**配置项引用（Symbol References）**：[`CONFIG_ADC_AD4170`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD4170)、[`CONFIG_ADC_ASYNC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ASYNC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADI_AD7124_ADC_ACQUISITION_THREAD_INIT_PRIO"></a>

## 49.5 `CONFIG_ADI_AD7124_ADC_ACQUISITION_THREAD_INIT_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_AD7124 && CONFIG_ADC_ASYNC && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad7124:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad7124#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ADI AD7124 模数转换器（Analog-to-Digital Converter）

**配置项引用（Symbol References）**：[`CONFIG_ADC_AD7124`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD7124)、[`CONFIG_ADC_ASYNC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ASYNC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADI_AD7124_ADC_ACQUISITION_THREAD_STACK_SIZE"></a>

## 49.6 `CONFIG_ADI_AD7124_ADC_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_AD7124 && CONFIG_ADC_ASYNC && CONFIG_ADC
```

**默认值（Defaults）**

```text
400
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad7124:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad7124#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ADI AD7124 模数转换器（Analog-to-Digital Converter）

**配置项引用（Symbol References）**：[`CONFIG_ADC_AD7124`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD7124)、[`CONFIG_ADC_ASYNC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ASYNC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_LPADC_DO_OFFSET_CALIBRATION"></a>

## 49.7 `CONFIG_LPADC_DO_OFFSET_CALIBRATION`

**提示（Prompt）**：执行偏移校准（Offset Calibration）

**说明（Help）**

执行偏移校准（Offset Calibration）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_MCUX_LPADC && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.mcux:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.mcux#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_MCUX_LPADC`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_LPADC)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<!-- kconfig-navigation -->

[上一章](P048_drivers_adc_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P050_drivers_audio_配置项参考.md)
