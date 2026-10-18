---
id: learning.zephyr-docs.kconfig-reference.page-47
title: "`drivers/adc`配置项参考（1/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第47章\_`drivers/adc`配置项参考（1/3）

本章翻译官方 Kconfig 数据库中 `drivers/adc` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_AD405X_STREAM"></a>

## 47.1 `CONFIG_AD405X_STREAM`

**提示（Prompt）**：使用先进先出队列传输数据流（FIFO Streaming）

**说明（Help）**

启用通过实时 I/O（RTIO）流式传输模数转换器（ADC）数据的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_AD405X && CONFIG_SPI_RTIO && CONFIG_ADC
```

**主动选择（Selects）**

```text
CONFIG_AD405X_TRIGGER
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad405x:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad405x#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → AD405X 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_AD405X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD405X)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_AD405X_TRIGGER`](P047_drivers_adc_配置项参考_1.md#CONFIG_AD405X_TRIGGER)。

<a id="CONFIG_AD405X_TRIGGER"></a>

## 47.2 `CONFIG_AD405X_TRIGGER`

**提示（Prompt）**：AD405X 中断（Interrupts）

**说明（Help）**

启用 ADI AD405X 的中断（Interrupt）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_AD405X && CONFIG_ADC
```

**被选择（Selected by）**

```text
CONFIG_AD405X_STREAM
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad405x:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad405x#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → AD405X 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_AD405X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD405X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_AD405X_STREAM`](P047_drivers_adc_配置项参考_1.md#CONFIG_AD405X_STREAM)。

<a id="CONFIG_ADC"></a>

## 47.3 `CONFIG_ADC`

**提示（Prompt）**：模数转换器驱动（Analog-to-Digital Converter，ADC）

**说明（Help）**

启用模数转换器（Analog-to-Digital Converter，ADC）驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_INPUT_ANALOG_AXIS
CONFIG_BFLB_TSEN
CONFIG_EVERLIGHT_ALS_PT19
CONFIG_MCP970X
CONFIG_NRF_VBAT
CONFIG_TEMP_KINETIS
CONFIG_LPADC_TEMP40
CONFIG_D6F
CONFIG_GROVE_LIGHT_SENSOR
CONFIG_GROVE_TEMPERATURE_SENSOR
CONFIG_STM32_TEMP
CONFIG_STM32_VBAT
CONFIG_STM32_VREF
CONFIG_CURRENT_AMP
CONFIG_LM35
CONFIG_NTC_THERMISTOR
CONFIG_RPI_PICO_TEMP
CONFIG_VOLTAGE_DIVIDER
```

**定义位置（Location）**：[`drivers/adc/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_ANALOG_AXIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_ANALOG_AXIS)、[`CONFIG_BFLB_TSEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_TSEN)、[`CONFIG_EVERLIGHT_ALS_PT19`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EVERLIGHT_ALS_PT19)、[`CONFIG_MCP970X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCP970X)、[`CONFIG_NRF_VBAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_VBAT)、[`CONFIG_TEMP_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEMP_KINETIS)、[`CONFIG_LPADC_TEMP40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LPADC_TEMP40)、[`CONFIG_D6F`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_D6F)、[`CONFIG_GROVE_LIGHT_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GROVE_LIGHT_SENSOR)、[`CONFIG_GROVE_TEMPERATURE_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GROVE_TEMPERATURE_SENSOR)、[`CONFIG_STM32_TEMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_TEMP)、[`CONFIG_STM32_VBAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_VBAT)、[`CONFIG_STM32_VREF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_VREF)、[`CONFIG_CURRENT_AMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CURRENT_AMP)、[`CONFIG_LM35`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LM35)、[`CONFIG_NTC_THERMISTOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NTC_THERMISTOR)、[`CONFIG_RPI_PICO_TEMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RPI_PICO_TEMP)、[`CONFIG_VOLTAGE_DIVIDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VOLTAGE_DIVIDER)。

<a id="CONFIG_ADC_AD405X"></a>

## 47.4 `CONFIG_ADC_AD405X`

**提示（Prompt）**：AD405X 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 ADI AD405X 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ADI_AD4052_ADC_ENABLED || DT_HAS_ADI_AD4050_ADC_ENABLED) && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad405x:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad405x#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ADC_AD4114"></a>

## 47.5 `CONFIG_ADC_AD4114`

**提示（Prompt）**：AD4114 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 AD4114 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_AD4114_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad4114:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad4114#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ADC_AD4114_ACQUISITION_THREAD_PRIO"></a>

## 47.6 `CONFIG_ADC_AD4114_ACQUISITION_THREAD_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部模数转换器（ADC）数据采集线程（Data Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_AD4114 && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad4114:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad4114#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → AD4114 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_AD4114`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD4114)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_AD4114_ACQUISITION_THREAD_STACK_SIZE"></a>

## 47.7 `CONFIG_ADC_AD4114_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_AD4114 && CONFIG_ADC
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad4114:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad4114#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → AD4114 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_AD4114`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD4114)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_AD4130"></a>

## 47.8 `CONFIG_ADC_AD4130`

**提示（Prompt）**：ADI AD4130 模数转换器（Analog-to-Digital Converter）

**说明（Help）**

启用 AD4130 模数转换器（ADC）驱动。该器件是基于 SPI 的超低功耗（Ultra Low Power）24 位 Σ-Δ 模数转换器（Sigma-Delta ADC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_AD4130_ADC_ENABLED && CONFIG_ADC
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

**定义位置（Location）**：[`drivers/adc/Kconfig.ad4130:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad4130#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_AD4170"></a>

## 47.9 `CONFIG_ADC_AD4170`

**提示（Prompt）**：ADI AD4170 及同类模数转换器（Analog-to-Digital Converters）

**说明（Help）**

启用 AD4170 及同类模数转换器（ADC）驱动。这类器件是基于 SPI 的超低功耗（Ultra Low Power）24 位 Σ-Δ 模数转换器（Sigma-Delta ADC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ADI_AD4170_ADC_ENABLED || DT_HAS_ADI_AD4190_ADC_ENABLED || DT_HAS_ADI_AD4195_ADC_ENABLED || DT_HAS_ADI_AD4190_8_ADC_ENABLED || DT_HAS_ADI_AD4195_8_ADC_ENABLED) && CONFIG_ADC
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

**定义位置（Location）**：[`drivers/adc/Kconfig.ad4170:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad4170#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_AD559X"></a>

## 47.10 `CONFIG_ADC_AD559X`

**提示（Prompt）**：AD559x 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 AD559x 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_AD559X_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad559x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad559x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_ADC_AD559X_ACQUISITION_THREAD_PRIO"></a>

## 47.11 `CONFIG_ADC_AD559X_ACQUISITION_THREAD_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部模数转换器（ADC）数据采集线程（Data Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_AD559X && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad559x:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad559x#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → AD559x 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_AD559X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD559X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_AD559X_ACQUISITION_THREAD_STACK_SIZE"></a>

## 47.12 `CONFIG_ADC_AD559X_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_AD559X && CONFIG_ADC
```

**默认值（Defaults）**

```text
384
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad559x:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad559x#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → AD559x 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_AD559X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD559X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_AD7124"></a>

## 47.13 `CONFIG_ADC_AD7124`

**提示（Prompt）**：ADI AD7124 模数转换器（Analog-to-Digital Converter）

**说明（Help）**

启用 AD7124 模数转换器（ADC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_AD7124_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_CRC
CONFIG_ADC_CONFIGURABLE_INPUTS
CONFIG_ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ad7124:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ad7124#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)、[`CONFIG_ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`、`CONFIG_ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN`。

<a id="CONFIG_ADC_ADC124S021"></a>

## 47.14 `CONFIG_ADC_ADC124S021`

**提示（Prompt）**：TI ADC124S021 模数转换器驱动（ADC Driver）

**说明（Help）**

启用德州仪器（Texas Instruments）ADC124S021 支持；它是 4 通道、12 位 SPI 模数转换器（ADC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_ADC124S021_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/adc/Kconfig.adc124s021:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.adc124s021#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ADC_ADC124S021_ACQUISITION_THREAD_PRIO"></a>

## 47.15 `CONFIG_ADC_ADC124S021_ACQUISITION_THREAD_PRIO`

**提示（Prompt）**：ADC124S021 采集线程优先级（Acquisition Thread Priority）

**说明（Help）**

ADC124S021 采集线程（Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADC124S021 && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.adc124s021:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.adc124s021#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → TI ADC124S021 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADC124S021`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADC124S021)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADC124S021_ACQUISITION_THREAD_STACK_SIZE"></a>

## 47.16 `CONFIG_ADC_ADC124S021_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC124S021 采集线程栈大小（Acquisition Thread Stack Size）

**说明（Help）**

ADC124S021 采集线程（Acquisition Thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADC124S021 && CONFIG_ADC
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/adc/Kconfig.adc124s021:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.adc124s021#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → TI ADC124S021 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADC124S021`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADC124S021)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADCXX1C"></a>

## 47.17 `CONFIG_ADC_ADCXX1C`

**提示（Prompt）**：TI ADC081C / ADC101C / ADC121C（ADCxx1C）I2C 模数转换器系列（ADC Family）

**说明（Help）**

启用德州仪器（Texas Instruments）ADCxx1C 单通道 I2C 模数转换器（ADC）系列的驱动，包括 ADC081C021、ADC081C027、ADC101C021、ADC101C027、ADC121C021 和 ADC121C027。六款器件使用同一套寄存器映射（Register Map），仅分辨率（8、10 或 12 位）及一个封装引脚的功能不同，因此由同一个驱动处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_ADC081C021_ENABLED || DT_HAS_TI_ADC081C027_ENABLED || DT_HAS_TI_ADC101C021_ENABLED || DT_HAS_TI_ADC101C027_ENABLED || DT_HAS_TI_ADC121C021_ENABLED || DT_HAS_TI_ADC121C027_ENABLED) && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/adc/Kconfig.adcxx1c:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.adcxx1c#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_ADC_ADE7913"></a>

## 47.18 `CONFIG_ADC_ADE7913`

**提示（Prompt）**：亚德诺（Analog Devices）ADE7913 SPI 模数转换器（ADC）

**说明（Help）**

输出原始的有符号 24 位数值（Raw Signed 24-bit Values）。校准（Calibration）和换算（Conversion）由用户完成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADE7913_ENABLED && CONFIG_MULTITHREADING && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ade7913:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ade7913#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ADC_ADE7913_ACQUISITION_THREAD_PRIORITY"></a>

## 47.19 `CONFIG_ADC_ADE7913_ACQUISITION_THREAD_PRIORITY`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部模数转换器（ADC）数据采集线程（Data Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADE7913 && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ade7913:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ade7913#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 亚德诺（Analog Devices）ADE7913 SPI 模数转换器（ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADE7913`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADE7913)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADE7913_ACQUISITION_THREAD_STACK_SIZE"></a>

## 47.20 `CONFIG_ADC_ADE7913_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADE7913 && CONFIG_ADC
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ade7913:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ade7913#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 亚德诺（Analog Devices）ADE7913 SPI 模数转换器（ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADE7913`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADE7913)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADE7913_INIT_PRIORITY"></a>

## 47.21 `CONFIG_ADC_ADE7913_INIT_PRIORITY`

**提示（Prompt）**：ADE7913 初始化优先级（Init Priority）

**说明（Help）**

ADE7913 设备初始化（Device Initialization）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADE7913 && CONFIG_ADC
```

**默认值（Defaults）**

```text
CONFIG_SPI_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ade7913:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ade7913#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 亚德诺（Analog Devices）ADE7913 SPI 模数转换器（ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADE7913`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADE7913)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_INIT_PRIORITY)。

<a id="CONFIG_ADC_ADS1112"></a>

## 47.22 `CONFIG_ADC_ADS1112`

**提示（Prompt）**：德州仪器 ADS1112 模数转换器驱动（Texas Instruments ADC Driver）

**说明（Help）**

启用 ADS1112 的驱动实现（Driver Implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_ADS1112_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1112:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1112#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_ADS1118"></a>

## 47.23 `CONFIG_ADC_ADS1118`

**提示（Prompt）**：德州仪器 ADS1118（Texas Instruments ADS1118）

**说明（Help）**

启用 ADS1118 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_ADS1118_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
CONFIG_SPI
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1118:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1118#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_ADS1118_ACQUISITION_THREAD_STACK_SIZE"></a>

## 47.24 `CONFIG_ADC_ADS1118_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS1118 && CONFIG_ADC
```

**默认值（Defaults）**

```text
400
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1118:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1118#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 ADS1118（Texas Instruments ADS1118）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS1118`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1118)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS1118_ASYNC_THREAD_INIT_PRIO"></a>

## 47.25 `CONFIG_ADC_ADS1118_ASYNC_THREAD_INIT_PRIO`

**提示（Prompt）**：ADS1118 ADC 异步线程优先级（Async Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS1118 && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1118:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1118#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 ADS1118（Texas Instruments ADS1118）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS1118`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1118)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS1119"></a>

## 47.26 `CONFIG_ADC_ADS1119`

**提示（Prompt）**：德州仪器 ADS1119 I2C（Texas Instruments ADS1119 I2C）

**说明（Help）**

启用 ADS1119 的驱动实现（Driver Implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_ADS1119_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1119:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1119#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_ADS1119_ACQUISITION_THREAD_STACK_SIZE"></a>

## 47.27 `CONFIG_ADC_ADS1119_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS1119 && CONFIG_ADC
```

**默认值（Defaults）**

```text
400
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1119:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1119#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 ADS1119 I2C（Texas Instruments ADS1119 I2C）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS1119`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1119)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS1119_ASYNC_THREAD_INIT_PRIO"></a>

## 47.28 `CONFIG_ADC_ADS1119_ASYNC_THREAD_INIT_PRIO`

**提示（Prompt）**：ADS1119 ADC 异步线程优先级（Async Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS1119 && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1119:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1119#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 ADS1119 I2C（Texas Instruments ADS1119 I2C）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS1119`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1119)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS1220"></a>

## 47.29 `CONFIG_ADC_ADS1220`

**提示（Prompt）**：德州仪器 ADS1220 模数转换器驱动（Texas Instruments ADC Driver）

**说明（Help）**

启用德州仪器（Texas Instruments）ADS1220 驱动。ADS1220 是 24 位、4 通道、低功耗的 Δ-Σ 模数转换器（Delta-Sigma ADC），集成可编程增益放大器（PGA）、电压基准（VREF）、SPI 接口和两个电流型数模转换器（IDAC）。它是精密 ADC，面向温度、压力和应变感测等传感器应用中的高分辨率测量。

此驱动支持以下特性：

- 24 位分辨率，每秒最多 2000 次采样。
- 4 个多路复用输入通道（Multiplexed Input Channels），支持单端（Single-Ended）和差分（Differential）输入。
- 可编程增益放大器（Programmable Gain Amplifier），增益 1–128。
- 内部 2.048V 基准或外部基准。
- 两个匹配的激励电流源（Excitation Current Sources，IDAC）。
- 电源监测能力（Supply Monitoring）。
- 50/60 Hz 抑制滤波器（Rejection Filters）。
- 低功耗工作模式（Low Power Operation Modes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_ADS1220_ENABLED && CONFIG_ADC
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

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1220:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1220#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_ADS1220_WAIT_FOR_COMPLETION_TIMEOUT_MS"></a>

## 47.30 `CONFIG_ADC_ADS1220_WAIT_FOR_COMPLETION_TIMEOUT_MS`

**提示（Prompt）**：等待读取完成的超时时间，单位为毫秒（Read Completion Timeout）

**说明（Help）**

等待读取完成的时间，单位为毫秒（ms）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS1220 && CONFIG_ADC
```

**默认值（Defaults）**

```text
250
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1220:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1220#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 ADS1220 模数转换器驱动（Texas Instruments ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS1220`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1220)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS126X"></a>

## 47.31 `CONFIG_ADC_ADS126X`

**提示（Prompt）**：德州仪器 ADS126x 模数转换器（Texas Instruments ADC）

**说明（Help）**

启用德州仪器（Texas Instruments）ADS126x SPI 模数转换器（ADC）支持。支持的器件包括 ADS1262 和 ADS1263。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_ADS1262_ENABLED || DT_HAS_TI_ADS1263_ENABLED) && CONFIG_SPI && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads126x:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads126x#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_ADS131M02"></a>

## 47.32 `CONFIG_ADC_ADS131M02`

**提示（Prompt）**：德州仪器 ADS131M02（Texas Instruments ADS131M02）

**说明（Help）**

启用 ADS131M02 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_ADS131M02_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
CONFIG_SPI
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads131m02:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads131m02#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_ADS1X1X"></a>

## 47.33 `CONFIG_ADC_ADS1X1X`

**提示（Prompt）**：ADS1X1X 驱动（Driver）

**说明（Help）**

启用 ADS1X1X 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_ADS1013_ENABLED || DT_HAS_TI_ADS1014_ENABLED || DT_HAS_TI_ADS1015_ENABLED || DT_HAS_TI_ADS1113_ENABLED || DT_HAS_TI_ADS1114_ENABLED || DT_HAS_TI_ADS1115_ENABLED) && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_ADC_CONFIGURABLE_INPUTS if DT_HAS_TI_ADS1015_ENABLED || DT_HAS_TI_ADS1115_ENABLED
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1x1x:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1x1x#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_ADS1X1X_ACQUISITION_THREAD_PRIO"></a>

## 47.34 `CONFIG_ADC_ADS1X1X_ACQUISITION_THREAD_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部模数转换器（ADC）数据采集线程（Data Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS1X1X && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1x1x:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1x1x#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ADS1X1X 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS1X1X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1X1X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS1X1X_ACQUISITION_THREAD_STACK_SIZE"></a>

## 47.35 `CONFIG_ADC_ADS1X1X_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS1X1X && CONFIG_ADC
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1x1x:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1x1x#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ADS1X1X 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS1X1X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1X1X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS1X1X_INIT_PRIORITY"></a>

## 47.36 `CONFIG_ADC_ADS1X1X_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

ADS1X1X 模数转换器（ADC）设备驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS1X1X && CONFIG_ADC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1x1x:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1x1x#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ADS1X1X 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS1X1X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1X1X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS1X4S0X"></a>

## 47.37 `CONFIG_ADC_ADS1X4S0X`

**提示（Prompt）**：德州仪器 ADS1X4S0X（Texas Instruments ADS1X4S0X）

**说明（Help）**

启用 ADS1X4S0X 系列的驱动实现（Driver Implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_ADS114S06_ENABLED || DT_HAS_TI_ADS114S08_ENABLED || DT_HAS_TI_ADS124S06_ENABLED || DT_HAS_TI_ADS124S08_ENABLED) && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_ADC_CONFIGURABLE_INPUTS
CONFIG_ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN
CONFIG_ADC_CONFIGURABLE_VBIAS_PIN
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1x4s0x:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1x4s0x#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)、[`CONFIG_ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN)、[`CONFIG_ADC_CONFIGURABLE_VBIAS_PIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_VBIAS_PIN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`、`CONFIG_ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN`、`CONFIG_ADC_CONFIGURABLE_VBIAS_PIN`。

<a id="CONFIG_ADC_ADS1X4S0X_ACQUISITION_THREAD_STACK_SIZE"></a>

## 47.38 `CONFIG_ADC_ADS1X4S0X_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS1X4S0X && CONFIG_ADC
```

**默认值（Defaults）**

```text
400
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1x4s0x:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1x4s0x#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 ADS1X4S0X（Texas Instruments ADS1X4S0X）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS1X4S0X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1X4S0X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS1X4S0X_ASYNC_THREAD_INIT_PRIO"></a>

## 47.39 `CONFIG_ADC_ADS1X4S0X_ASYNC_THREAD_INIT_PRIO`

**提示（Prompt）**：ADS1X4S0X ADC 异步线程优先级（Async Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS1X4S0X && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1x4s0x:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1x4s0x#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 ADS1X4S0X（Texas Instruments ADS1X4S0X）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS1X4S0X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1X4S0X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS1X4S0X_GPIO"></a>

## 47.40 `CONFIG_ADC_ADS1X4S0X_GPIO`

**提示（Prompt）**：通用输入输出支持（GPIO Support）

**说明（Help）**

在 ADS1X4S0X 模数转换器（ADC）驱动中启用 GPIO 子设备（Child Device）支持。通用输入输出（GPIO）功能由 ADS1X4S0X GPIO 驱动处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && CONFIG_ADC_ADS1X4S0X && CONFIG_ADC
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1x4s0x:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1x4s0x#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 ADS1X4S0X（Texas Instruments ADS1X4S0X）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_ADC_ADS1X4S0X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1X4S0X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS1X4S0X_WAIT_FOR_COMPLETION_TIMEOUT_MS"></a>

## 47.41 `CONFIG_ADC_ADS1X4S0X_WAIT_FOR_COMPLETION_TIMEOUT_MS`

**提示（Prompt）**：等待读取完成的超时时间，单位为毫秒（Read Completion Timeout）

**说明（Help）**

等待读取完成的时间，单位为毫秒（ms）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS1X4S0X && CONFIG_ADC
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads1x4s0x:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads1x4s0x#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 ADS1X4S0X（Texas Instruments ADS1X4S0X）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS1X4S0X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1X4S0X)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS7052"></a>

## 47.42 `CONFIG_ADC_ADS7052`

**提示（Prompt）**：德州仪器 ADS7052 SPI（Texas Instruments ADS7052 SPI）

**说明（Help）**

启用 ADS7052 的驱动实现（Driver Implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_ADS7052_ENABLED && CONFIG_ADC
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

**定义位置（Location）**：[`drivers/adc/Kconfig.ads7052:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads7052#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_ADS7052_ACQUISITION_THREAD_PRIO"></a>

## 47.43 `CONFIG_ADC_ADS7052_ACQUISITION_THREAD_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部模数转换器（ADC）数据采集线程（Data Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS7052 && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads7052:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads7052#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 ADS7052 SPI（Texas Instruments ADS7052 SPI）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS7052`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS7052)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS7052_ACQUISITION_THREAD_STACK_SIZE"></a>

## 47.44 `CONFIG_ADC_ADS7052_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS7052 && CONFIG_ADC
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads7052:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads7052#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 ADS7052 SPI（Texas Instruments ADS7052 SPI）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS7052`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS7052)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS7052_INIT_PRIORITY"></a>

## 47.45 `CONFIG_ADC_ADS7052_INIT_PRIORITY`

**提示（Prompt）**：ADS7052 初始化优先级（Init Priority）

**说明（Help）**

ADS7052 设备初始化优先级必须使其在 SPI 初始化之后执行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS7052 && CONFIG_ADC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads7052:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads7052#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 德州仪器 ADS7052 SPI（Texas Instruments ADS7052 SPI）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS7052`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS7052)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS7828"></a>

## 47.46 `CONFIG_ADC_ADS7828`

**提示（Prompt）**：TI ADS7828 / ADS7830 I2C 模数转换器（ADC）

**说明（Help）**

启用德州仪器（Texas Instruments）ADS7828 和 ADS7830 驱动；它们分别是 12 位和 8 位的 8 通道 I2C 逐次逼近型模数转换器（SAR ADC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_ADS7828_ENABLED || DT_HAS_TI_ADS7830_ENABLED) && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads7828:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads7828#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_ADC_ADS79XX"></a>

## 47.47 `CONFIG_ADC_ADS79XX`

**提示（Prompt）**：TI ADS79xx-Q1 SPI 模数转换器系列（ADC Family）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_ADS7950_ENABLED || DT_HAS_TI_ADS7951_ENABLED || DT_HAS_TI_ADS7952_ENABLED || DT_HAS_TI_ADS7953_ENABLED || DT_HAS_TI_ADS7954_ENABLED || DT_HAS_TI_ADS7955_ENABLED || DT_HAS_TI_ADS7956_ENABLED || DT_HAS_TI_ADS7957_ENABLED || DT_HAS_TI_ADS7958_ENABLED || DT_HAS_TI_ADS7959_ENABLED || DT_HAS_TI_ADS7960_ENABLED || DT_HAS_TI_ADS7961_ENABLED) && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads79xx:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads79xx#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ADC_ADS79XX_ACQUISITION_THREAD_PRIO"></a>

## 47.48 `CONFIG_ADC_ADS79XX_ACQUISITION_THREAD_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部模数转换器（ADC）数据采集线程（Data Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS79XX && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads79xx:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads79xx#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → TI ADS79xx-Q1 SPI 模数转换器系列（ADC Family）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS79XX`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS79XX)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS79XX_ACQUISITION_THREAD_STACK_SIZE"></a>

## 47.49 `CONFIG_ADC_ADS79XX_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS79XX && CONFIG_ADC
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads79xx:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads79xx#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → TI ADS79xx-Q1 SPI 模数转换器系列（ADC Family）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS79XX`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS79XX)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS79XX_DEBUG_SPI_TRANSFERS"></a>

## 47.50 `CONFIG_ADC_ADS79XX_DEBUG_SPI_TRANSFERS`

**提示（Prompt）**：底层 SPI 传输的额外调试（Low-Level SPI Transfer Debugging）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS79XX && CONFIG_ADC
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads79xx:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads79xx#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → TI ADS79xx-Q1 SPI 模数转换器系列（ADC Family）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS79XX`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS79XX)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ADS79XX_INIT_PRIORITY"></a>

## 47.51 `CONFIG_ADC_ADS79XX_INIT_PRIORITY`

**提示（Prompt）**：ADS79xxx 初始化优先级（Init Priority）

**说明（Help）**

ADS79xx 设备初始化优先级必须使其在 SPI 初始化之后执行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ADS79XX && CONFIG_ADC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ads79xx:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ads79xx#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → TI ADS79xx-Q1 SPI 模数转换器系列（ADC Family）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS79XX`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS79XX)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_AMBIQ"></a>

## 47.52 `CONFIG_ADC_AMBIQ`

**提示（Prompt）**：Ambiq 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 Ambiq 器件的模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_ADC
CONFIG_AMBIQ_HAL_USE_TIMER if CONFIG_SOC_SERIES_APOLLO3X
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ambiq:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ambiq#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_ADC)、[`CONFIG_AMBIQ_HAL_USE_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_TIMER)、[`CONFIG_SOC_SERIES_APOLLO3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO3X)。

<a id="CONFIG_ADC_AMBIQ_HANDLE_CACHE"></a>

## 47.53 `CONFIG_ADC_AMBIQ_HANDLE_CACHE`

**提示（Prompt）**：在 ADC 驱动中启用缓存处理（Cache Handling）

**说明（Help）**

如果上层已处理缓存（Cache），则禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE && CONFIG_ADC_AMBIQ && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ambiq:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ambiq#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → Ambiq 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_ADC_AMBIQ`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AMBIQ)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_AMEBA"></a>

## 47.54 `CONFIG_ADC_AMEBA`

**提示（Prompt）**：Ameba 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 Ameba 模数转换器（ADC）的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ameba:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ameba#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_ASYNC"></a>

## 47.55 `CONFIG_ADC_ASYNC`

**提示（Prompt）**：异步调用支持（Asynchronous Call Support）

**说明（Help）**

启用异步 API 调用（Asynchronous API Calls）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC
```

**主动选择（Selects）**

```text
CONFIG_POLL
```

**被选择（Selected by）**

```text
CONFIG_ADC_MAX32_STREAM
CONFIG_ADC_STM32
```

**定义位置（Location）**：[`drivers/adc/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_POLL`](P002_kernel_配置项参考_2.md#CONFIG_POLL)、[`CONFIG_ADC_MAX32_STREAM`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MAX32_STREAM)、[`CONFIG_ADC_STM32`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STM32)。

<a id="CONFIG_ADC_B91_ACQUISITION_THREAD_PRIO"></a>

## 47.56 `CONFIG_ADC_B91_ACQUISITION_THREAD_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部模数转换器（ADC）数据采集线程（Data Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_TELINK_B91 && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.b91:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.b91#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 泰凌微 B91 模数转换器驱动（Telink Semiconductor ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_TELINK_B91`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_TELINK_B91)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_B91_ACQUISITION_THREAD_STACK_SIZE"></a>

## 47.57 `CONFIG_ADC_B91_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_TELINK_B91 && CONFIG_ADC
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/adc/Kconfig.b91:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.b91#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 泰凌微 B91 模数转换器驱动（Telink Semiconductor ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_TELINK_B91`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_TELINK_B91)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_BEE"></a>

## 47.58 `CONFIG_ADC_BEE`

**提示（Prompt）**：瑞昱 Bee 系列模数转换器驱动（Realtek Bee ADC Driver）

**说明（Help）**

启用瑞昱（Realtek）Bee 片上系统（SoC）的模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_ADC
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.bee:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.bee#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_HAL_REALTEK_BEE_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_ADC`。

<a id="CONFIG_ADC_BFLB"></a>

## 47.59 `CONFIG_ADC_BFLB`

**提示（Prompt）**：博流模数转换器驱动（Bouffalolab ADC Driver）

**说明（Help）**

启用博流（Bouffalolab）模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_BFLB_FORCE_DYNAMIC_CALIBRATION"></a>

## 47.60 `CONFIG_ADC_BFLB_FORCE_DYNAMIC_CALIBRATION`

**提示（Prompt）**：使用动态校准代替 eFuse 校准值（Dynamic Calibration）

**说明（Help）**

使用对 `VBAT/2` 的差分测量（Differential Measurement）校准模数转换器（ADC）。这在很大程度上依赖芯片供电的精度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_BFLB && CONFIG_ADC
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_BL60X
```

**定义位置（Location）**：[`drivers/adc/Kconfig.bflb:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.bflb#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 博流模数转换器驱动（Bouffalolab ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_BFLB`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_BFLB)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)。

<a id="CONFIG_ADC_CC13XX_CC26XX"></a>

## 47.61 `CONFIG_ADC_CC13XX_CC26XX`

**提示（Prompt）**：CC13XX / CC26XX 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 TI CC13XX / CC26XX 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC13XX_CC26XX_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.cc13xx_cc26xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.cc13xx_cc26xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_CC23X0"></a>

## 47.62 `CONFIG_ADC_CC23X0`

**提示（Prompt）**：CC23X0 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 TI CC23X0 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC23X0_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.cc23x0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.cc23x0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_CC23X0_DMA_DRIVEN"></a>

## 47.63 `CONFIG_ADC_CC23X0_DMA_DRIVEN`

**提示（Prompt）**：TI CC23X0 ADC 器件的直接内存访问支持（DMA Support）

**说明（Help）**

直接内存访问（DMA）驱动模式将数据传输任务从 CPU 移交给 DMA，并减少处理模数转换器（ADC）序列模式所需的中断数量。使用 DMA 模式时，不会补偿 ADC 内部增益来调整测量结果。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_CC23X0 && CONFIG_ADC
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/adc/Kconfig.cc23x0:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.cc23x0#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → CC23X0 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_CC23X0`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_CC23X0)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_ADC_CC32XX"></a>

## 47.64 `CONFIG_ADC_CC32XX`

**提示（Prompt）**：CC32XX 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 CC32XX 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC32XX_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.cc32xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.cc32xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_CH32V00X"></a>

## 47.65 `CONFIG_ADC_CH32V00X`

**提示（Prompt）**：沁恒 CH32V00x 模数转换器驱动（WCH ADC Driver）

**说明（Help）**

启用沁恒（WCH）CH32V00x 系列模数转换器（Analog-to-Digital Converter，ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ch32v00x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ch32v00x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_DEFAULT_RTIO"></a>

## 47.66 `CONFIG_ADC_DEFAULT_RTIO`

**提示（Prompt）**：默认实时 I/O 支持（Default RTIO Support）

**说明（Help）**

为未实现流式传输（Stream）功能的模数转换器（ADC）设备启用默认实时 I/O（RTIO）处理程序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC
```

**主动选择（Selects）**

```text
CONFIG_RTIO
CONFIG_RTIO_WORKQ
CONFIG_RTIO_SYS_MEM_BLOCKS
CONFIG_RTIO_CONSUME_SEM
```

**定义位置（Location）**：[`drivers/adc/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_RTIO_SYS_MEM_BLOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_SYS_MEM_BLOCKS)、[`CONFIG_RTIO_CONSUME_SEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_CONSUME_SEM)。

<a id="CONFIG_ADC_EMUL"></a>

## 47.67 `CONFIG_ADC_EMUL`

**提示（Prompt）**：模数转换器仿真器（ADC Emulator）

**说明（Help）**

启用模数转换器（ADC）仿真器驱动。这是一个不与真实硬件通信的模拟驱动，通过模拟实际 ADC，用于测试 ADC 设备的上层 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_ADC_EMUL_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.adc_emul:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.adc_emul#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_EMUL_ACQUISITION_THREAD_PRIO"></a>

## 47.68 `CONFIG_ADC_EMUL_ACQUISITION_THREAD_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部模数转换器（ADC）数据采集线程（Data Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_EMUL && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.adc_emul:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.adc_emul#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 模数转换器仿真器（ADC Emulator）

**配置项引用（Symbol References）**：[`CONFIG_ADC_EMUL`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_EMUL)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_EMUL_ACQUISITION_THREAD_STACK_SIZE"></a>

## 47.69 `CONFIG_ADC_EMUL_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。当仿真 ADC 的数值函数（Value Function）需要大量内存时，可能需要增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_EMUL && CONFIG_ADC
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/adc/Kconfig.adc_emul:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.adc_emul#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 模数转换器仿真器（ADC Emulator）

**配置项引用（Symbol References）**：[`CONFIG_ADC_EMUL`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_EMUL)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_EMUL_SHELL"></a>

## 47.70 `CONFIG_ADC_EMUL_SHELL`

**提示（Prompt）**：ADC 仿真器命令行（ADC Emulator Shell）

**说明（Help）**

启用模数转换器（ADC）仿真器 `zephyr,adc-emul` 的命令行（Shell）命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_ADC_EMUL && CONFIG_ADC
```

**定义位置（Location）**：[`drivers/adc/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_ADC_EMUL`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_EMUL)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ENE_KB106X"></a>

## 47.71 `CONFIG_ADC_ENE_KB106X`

**提示（Prompt）**：ENE KB106X 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 ENE KB106X 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB106X_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ene:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ene#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_ENE_KB1200"></a>

## 47.72 `CONFIG_ADC_ENE_KB1200`

**提示（Prompt）**：ENE KB1200 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 ENE KB1200 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB1200_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ene:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ene#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_ESP32"></a>

## 47.73 `CONFIG_ADC_ESP32`

**提示（Prompt）**：ESP32 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 ESP32 模数转换器（ADC）的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.esp32:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.esp32#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ESP32_CONVERSION_TIMEOUT_US"></a>

## 47.74 `CONFIG_ADC_ESP32_CONVERSION_TIMEOUT_US`

**提示（Prompt）**：单次转换完成超时，单位为微秒（Oneshot Conversion Completion Timeout）

**说明（Help）**

等待单次转换（Oneshot Conversion）完成的最长时间；超过此时间后，`adc_read` 返回 `-ETIMEDOUT`。共享模拟模块（Shared Analog Block）暂时断电时，例如处于 Wi-Fi 调制解调器休眠窗口（Modem Sleep Window）期间，转换无法完成；调用方应重试此类读取。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ESP32 && CONFIG_ADC
```

**默认值（Defaults）**

```text
2000
```

**取值范围（Ranges）**

```text
[100, 1000000]
```

**定义位置（Location）**：[`drivers/adc/Kconfig.esp32:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.esp32#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ESP32 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ESP32`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ESP32)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ESP32_DMA"></a>

## 47.75 `CONFIG_ADC_ESP32_DMA`

**提示（Prompt）**：ESP32 ADC 直接内存访问支持（DMA Support）

**说明（Help）**

启用模数转换器（ADC）的直接内存访问（DMA）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ESP32 && CONFIG_ADC
```

**主动选择（Selects）**

```text
CONFIG_DMA if DT_HAS_ESPRESSIF_ESP32_GDMA_ENABLED
```

**定义位置（Location）**：[`drivers/adc/Kconfig.esp32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.esp32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ESP32 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ESP32`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ESP32)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_ADC_GD32"></a>

## 47.76 `CONFIG_ADC_GD32`

**提示（Prompt）**：GD32 模数转换器驱动（ADC Driver）

**说明（Help）**

启用兆易创新（GigaDevice）GD32 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.gd32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.gd32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_GECKO_ADC"></a>

## 47.77 `CONFIG_ADC_GECKO_ADC`

**提示（Prompt）**：Gecko 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 Silicon Labs GeckoEFM32 模数转换器（ADC）的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GECKO_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_GECKO_ADC
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.silabs:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.silabs#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SILABS_GECKO_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_INFINEON_AUTANALOG_SAR"></a>

## 47.78 `CONFIG_ADC_INFINEON_AUTANALOG_SAR`

**提示（Prompt）**：英飞凌 AutAnalog 逐次逼近型模数转换器驱动（Infineon AutAnalog SAR ADC Driver）

**说明（Help）**

为采用 AutAnalog 逐次逼近型模数转换器（SAR ADC）的英飞凌（Infineon）微控制器（MCU）启用 ADC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_AUTANALOG_SAR_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.infineon_autanalog_sar:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.infineon_autanalog_sar#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_INFINEON_AUTANALOG_SAR_STREAM"></a>

## 47.79 `CONFIG_ADC_INFINEON_AUTANALOG_SAR_STREAM`

**提示（Prompt）**：英飞凌 AutAnalog SAR ADC 流式传输支持（Stream Support）

**说明（Help）**

启用英飞凌（Infineon）AutAnalog SAR ADC 的流式模式（Streaming Mode），利用硬件先进先出队列（FIFO），通过实时 I/O（RTIO）流式传输 ADC 样本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_INFINEON_AUTANALOG_SAR && CONFIG_ADC_STREAM && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.infineon_autanalog_sar:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.infineon_autanalog_sar#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 英飞凌 AutAnalog 逐次逼近型模数转换器驱动（Infineon AutAnalog SAR ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_INFINEON_AUTANALOG_SAR`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_INFINEON_AUTANALOG_SAR)、[`CONFIG_ADC_STREAM`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STREAM)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_INFINEON_CAT1"></a>

## 47.80 `CONFIG_ADC_INFINEON_CAT1`

**提示（Prompt）**：英飞凌 CAT1 模数转换器驱动（Infineon ADC Driver）

**说明（Help）**

启用英飞凌（Infineon）CAT1 系列的模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_ADC
CONFIG_USE_INFINEON_DMA
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.infineon:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.infineon#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_USE_INFINEON_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_ADC)、[`CONFIG_USE_INFINEON_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_DMA)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_INFINEON_HPPASS_SAR"></a>

## 47.81 `CONFIG_ADC_INFINEON_HPPASS_SAR`

**提示（Prompt）**：英飞凌 HPPASS SAR ADC 驱动（Infineon HPPASS SAR ADC Driver）

**说明（Help）**

启用英飞凌（Infineon）PSOC C3 高性能可编程模拟子系统（High Performance Programmable Analog Sub-System，HPPASS）的逐次逼近型模数转换器（SAR ADC）驱动。HPPASS SAR ADC 提供 12 位模数转换能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_HPPASS_SAR_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
CONFIG_USE_INFINEON_HPPASS_SAR_ADC
CONFIG_ADC_CONFIGURABLE_INPUTS
```

**定义位置（Location）**：[`drivers/adc/Kconfig.infineon_hppass_sar:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.infineon_hppass_sar#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)、[`CONFIG_USE_INFINEON_HPPASS_SAR_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_HPPASS_SAR_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_INFINEON_HPPASS_SAR_INIT_PRIORITY"></a>

## 47.82 `CONFIG_ADC_INFINEON_HPPASS_SAR_INIT_PRIORITY`

**提示（Prompt）**：英飞凌 HPPASS SAR ADC 驱动初始化优先级（Init Priority）

**说明（Help）**

英飞凌（Infineon）HPPASS SAR ADC 驱动的初始化优先级。其数值应大于 `HPPASS_ANALOG_INIT_PRIORITY`，以确保模拟子系统（Analog Subsystem）先完成初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_INFINEON_HPPASS_SAR && CONFIG_ADC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/adc/Kconfig.infineon_hppass_sar:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.infineon_hppass_sar#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 英飞凌 HPPASS SAR ADC 驱动（Infineon HPPASS SAR ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_INFINEON_HPPASS_SAR`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_INFINEON_HPPASS_SAR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_INFINEON_HPPASS_SAR_POLL_TIMEOUT_US"></a>

## 47.83 `CONFIG_ADC_INFINEON_HPPASS_SAR_POLL_TIMEOUT_US`

**提示（Prompt）**：英飞凌 HPPASS SAR ADC 同步轮询超时，单位为微秒（Synchronous Poll Timeout）

**说明（Help）**

同步、即阻塞式转换（Synchronous / Blocking Conversion）等待结果的时间上限，单位为微秒。只有 HPPASS 多功能设备（MFD）父设备的自主控制器（Autonomous Controller）已运行，且固件触发信号（Firmware Trigger）已路由到该组时，转换才会完成；这两个条件都不受此驱动控制。限制等待时间可使停滞或错误路由的触发以 `-ETIMEDOUT` 结束读取，而不会让调用线程一直挂起。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_INFINEON_HPPASS_SAR && CONFIG_ADC
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`drivers/adc/Kconfig.infineon_hppass_sar:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.infineon_hppass_sar#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 英飞凌 HPPASS SAR ADC 驱动（Infineon HPPASS SAR ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_INFINEON_HPPASS_SAR`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_INFINEON_HPPASS_SAR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_INFINEON_SAR"></a>

## 47.84 `CONFIG_ADC_INFINEON_SAR`

**提示（Prompt）**：英飞凌逐次逼近型模数转换器驱动（Infineon SAR ADC Driver）

**说明（Help）**

启用英飞凌（Infineon）器件的逐次逼近型模数转换器（SAR ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_SAR_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC_CONFIGURABLE_INPUTS
CONFIG_USE_INFINEON_ADC
```

**定义位置（Location）**：[`drivers/adc/Kconfig.infineon_sar:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.infineon_sar#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)、[`CONFIG_USE_INFINEON_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_ADC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_INFINEON_SAR_SARSEQ_SWITCHING"></a>

## 47.85 `CONFIG_ADC_INFINEON_SAR_SARSEQ_SWITCHING`

**提示（Prompt）**：使用 SARSEQ 硬件开关控制（Hardware Switch Control）

**说明（Help）**

启用 SARSEQ 硬件序列器（Hardware Sequencer）对 SAR ADC 输入开关（Input Switch）的控制。禁用后，驱动仅依赖由固件控制的开关。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_INFINEON_SAR && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.infineon_sar:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.infineon_sar#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 英飞凌逐次逼近型模数转换器驱动（Infineon SAR ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_INFINEON_SAR`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_INFINEON_SAR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_INIT_PRIORITY"></a>

## 47.86 `CONFIG_ADC_INIT_PRIORITY`

**提示（Prompt）**：ADC 初始化优先级（Init Priority）

**说明（Help）**

模数转换器（ADC）驱动设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/lmp90100_evb/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/lmp90100_evb/Kconfig.defconfig)。

```text
80
```

来源：[`boards/shields/mikroe_adc_click/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/mikroe_adc_click/Kconfig.defconfig)。

```text
80
```

**定义位置（Location）**：[`drivers/adc/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_ADC_IT51XXX_VOL_FULL_SCALE"></a>

## 47.87 `CONFIG_ADC_IT51XXX_VOL_FULL_SCALE`

**提示（Prompt）**：将 ADC 内部电压用作满量程（Internal Voltage as Full-Scale）

**说明（Help）**

启用 ADC 内部参考电压（Internal Reference Voltage），作为 3300mV 的满量程（Full-Scale）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ITE_IT51XXX && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.it51xxx:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.it51xxx#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ITE IT51XXX 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ITE_IT51XXX`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ITE_IT51XXX)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_IT8XXX2_READING_TIMEOUT_MS"></a>

## 47.88 `CONFIG_ADC_IT8XXX2_READING_TIMEOUT_MS`

**提示（Prompt）**：IT8XXX2 ADC 读取超时，单位为毫秒（Reading Timeout）

**说明（Help）**

等待模数转换器（ADC）数据有效中断（Data Valid Interrupt）的超时时间，单位为毫秒。设为 0 表示无限等待，即 `K_FOREVER`。超时后，若有有效数据，驱动会改为直接读取 ADC 值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ITE_IT8XXX2 && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.it8xxx2:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.it8xxx2#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ITE IT8XXX2 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ITE_IT8XXX2`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ITE_IT8XXX2)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_IT8XXX2_VOL_FULL_SCALE"></a>

## 47.89 `CONFIG_ADC_IT8XXX2_VOL_FULL_SCALE`

**提示（Prompt）**：将 ADC 内部电压用作满量程（Internal Voltage as Full-Scale）

**说明（Help）**

启用 ADC 内部参考电压（Internal Reference Voltage），作为 3300mV 的满量程（Full-Scale）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ITE_IT8XXX2 && CONFIG_ADC
```

**定义位置（Location）**：[`drivers/adc/Kconfig.it8xxx2:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.it8xxx2#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → ITE IT8XXX2 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ITE_IT8XXX2`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ITE_IT8XXX2)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_ITE_IT51XXX"></a>

## 47.90 `CONFIG_ADC_ITE_IT51XXX`

**提示（Prompt）**：ITE IT51XXX 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 IT51XXX 处理器系列的模数转换器（ADC）驱动。电压范围为 0–3300mV，支持 12 位分辨率（Resolution），支持 8 个通道，即 `ch0`–`ch7`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.it51xxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.it51xxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_ITE_IT8XXX2"></a>

## 47.91 `CONFIG_ADC_ITE_IT8XXX2`

**提示（Prompt）**：ITE IT8XXX2 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 IT8XXX2 处理器系列的模数转换器（ADC）驱动。电压范围为 0–3000mV，支持 10 位分辨率（Resolution），支持 8 个通道，即 `ch0`–`ch7`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/adc/Kconfig.it8xxx2:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.it8xxx2#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ADC_LMP90XXX"></a>

## 47.92 `CONFIG_ADC_LMP90XXX`

**提示（Prompt）**：LMP90xxx 驱动（Driver）

**说明（Help）**

启用 LMP90xxx 模数转换器（ADC）驱动。LMP90xxx 是多通道、低功耗的传感器模拟前端（Analog Frontend，AFE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_LMP90077_ENABLED || DT_HAS_TI_LMP90078_ENABLED || DT_HAS_TI_LMP90079_ENABLED || DT_HAS_TI_LMP90080_ENABLED || DT_HAS_TI_LMP90097_ENABLED || DT_HAS_TI_LMP90098_ENABLED || DT_HAS_TI_LMP90099_ENABLED || DT_HAS_TI_LMP90100_ENABLED) && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_ADC_CONFIGURABLE_INPUTS
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/adc/Kconfig.lmp90xxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.lmp90xxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_ADC_CONFIGURABLE_INPUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_CONFIGURABLE_INPUTS)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADC_CONFIGURABLE_INPUTS`。

<a id="CONFIG_ADC_LMP90XXX_ACQUISITION_THREAD_PRIO"></a>

## 47.93 `CONFIG_ADC_LMP90XXX_ACQUISITION_THREAD_PRIO`

**提示（Prompt）**：ADC 数据采集线程优先级（Data Acquisition Thread Priority）

**说明（Help）**

内部模数转换器（ADC）数据采集线程（Data Acquisition Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_LMP90XXX && CONFIG_ADC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/adc/Kconfig.lmp90xxx:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.lmp90xxx#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → LMP90xxx 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_LMP90XXX`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_LMP90XXX)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_LMP90XXX_ACQUISITION_THREAD_STACK_SIZE"></a>

## 47.94 `CONFIG_ADC_LMP90XXX_ACQUISITION_THREAD_STACK_SIZE`

**提示（Prompt）**：ADC 数据采集线程栈大小（Data Acquisition Thread Stack Size）

**说明（Help）**

内部数据采集线程（Data Acquisition Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_LMP90XXX && CONFIG_ADC
```

**默认值（Defaults）**

```text
400
```

**定义位置（Location）**：[`drivers/adc/Kconfig.lmp90xxx:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.lmp90xxx#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → LMP90xxx 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_LMP90XXX`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_LMP90XXX)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_LMP90XXX_CRC"></a>

## 47.95 `CONFIG_ADC_LMP90XXX_CRC`

**提示（Prompt）**：使用循环冗余校验（Cyclic Redundancy Check，CRC）

**说明（Help）**

使用循环冗余校验（CRC）验证从 LMP90xxx 读取的数据的完整性（Integrity）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_LMP90XXX && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.lmp90xxx:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.lmp90xxx#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → LMP90xxx 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_LMP90XXX`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_LMP90XXX)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_LMP90XXX_GPIO"></a>

## 47.96 `CONFIG_ADC_LMP90XXX_GPIO`

**提示（Prompt）**：通用输入输出支持（GPIO Support）

**说明（Help）**

在 LMP90xxx 模数转换器（ADC）驱动中启用 GPIO 子设备（Child Device）支持。通用输入输出（GPIO）功能由 LMP90xxx GPIO 驱动处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && CONFIG_ADC_LMP90XXX && CONFIG_ADC
```

**主动选择（Selects）**

```text
CONFIG_GPIO_LMP90XXX
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/lmp90100_evb/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/lmp90100_evb/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/adc/Kconfig.lmp90xxx:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.lmp90xxx#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → LMP90xxx 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_ADC_LMP90XXX`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_LMP90XXX)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_GPIO_LMP90XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_LMP90XXX)。

<a id="CONFIG_ADC_LTC2451"></a>

## 47.97 `CONFIG_ADC_LTC2451`

**提示（Prompt）**：LTC2451 驱动（Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LLTC_LTC2451_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/adc/Kconfig.ltc2451:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.ltc2451#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_ADC_M5PM1"></a>

## 47.98 `CONFIG_ADC_M5PM1`

**提示（Prompt）**：M5Stack M5PM1 模数转换器驱动（ADC Driver）

**说明（Help）**

启用 M5Stack M5PM1 的模数转换器（ADC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_M5STACK_M5PM1_ADC_ENABLED && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/adc/Kconfig.m5pm1:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.m5pm1#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_ADC_M5PM1_INIT_PRIORITY"></a>

## 47.99 `CONFIG_ADC_M5PM1_INIT_PRIORITY`

**提示（Prompt）**：M5PM1 ADC 驱动初始化优先级（Initialization Priority）

**说明（Help）**

M5PM1 模数转换器（ADC）驱动的初始化优先级，其数值必须大于多功能设备（MFD）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_M5PM1 && CONFIG_ADC
```

**默认值（Defaults）**

```text
81
```

**定义位置（Location）**：[`drivers/adc/Kconfig.m5pm1:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.m5pm1#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → M5Stack M5PM1 模数转换器驱动（ADC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ADC_M5PM1`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_M5PM1)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_ADC_MAX11102_17"></a>

## 47.100 `CONFIG_ADC_MAX11102_17`

**提示（Prompt）**：美信 MAX11102–MAX11117（Maxim Integrated）

**说明（Help）**

启用 MAX11102–MAX11117 系列的驱动实现（Driver Implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_MAXIM_MAX11102_ENABLED || DT_HAS_MAXIM_MAX11103_ENABLED || DT_HAS_MAXIM_MAX11105_ENABLED || DT_HAS_MAXIM_MAX11106_ENABLED || DT_HAS_MAXIM_MAX11110_ENABLED || DT_HAS_MAXIM_MAX11111_ENABLED || DT_HAS_MAXIM_MAX11115_ENABLED || DT_HAS_MAXIM_MAX11116_ENABLED || DT_HAS_MAXIM_MAX11117_ENABLED) && CONFIG_ADC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/adc/Kconfig.max11102_17:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/Kconfig.max11102_17#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<!-- kconfig-navigation -->

[上一章](P046_boards_shields_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P048_drivers_adc_配置项参考_2.md)
