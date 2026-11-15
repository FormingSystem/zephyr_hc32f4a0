---
id: learning.zephyr-docs.kconfig-reference.page-161
title: "`drivers/sensor`配置项参考（13/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第161章\_`drivers/sensor`配置项参考（13/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SM351LT_TRIGGER_MODE"></a>

## 161.1 `CONFIG_SM351LT_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SM351LT && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_SM351LT_TRIGGER_NONE
CONFIG_SM351LT_TRIGGER_GLOBAL_THREAD
CONFIG_SM351LT_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/honeywell/sm351lt/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/sm351lt/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SM351LT 磁阻传感器（Magnetoresistive Sensor）

**配置项引用（Symbol References）**：[`CONFIG_SM351LT`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SM351LT)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SM351LT_TRIGGER_NONE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_SM351LT_TRIGGER_NONE)、[`CONFIG_SM351LT_TRIGGER_GLOBAL_THREAD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SM351LT_TRIGGER_GLOBAL_THREAD)、[`CONFIG_SM351LT_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_SM351LT_TRIGGER_OWN_THREAD)。

<a id="CONFIG_SM351LT_TRIGGER_NONE"></a>

## 161.2 `CONFIG_SM351LT_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SM351LT_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/sm351lt/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/sm351lt/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SM351LT 磁阻传感器（Magnetoresistive Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_SM351LT_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_SM351LT_TRIGGER_MODE)。

<a id="CONFIG_SM351LT_TRIGGER_OWN_THREAD"></a>

## 161.3 `CONFIG_SM351LT_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SM351LT_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_SM351LT_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/honeywell/sm351lt/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/sm351lt/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SM351LT 磁阻传感器（Magnetoresistive Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_SM351LT_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_SM351LT_TRIGGER_MODE)、[`CONFIG_SM351LT_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SM351LT_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SM351LT_TRIGGER`。

<a id="CONFIG_STCC4"></a>

## 161.4 `CONFIG_STCC4`

**提示（Prompt）**：STCC4 二氧化碳传感器（CO2 Sensor）

**说明（Help）**

启用基于热导率（Thermal Conductivity）原理的 Sensirion STCC4 二氧化碳传感器驱动，提供二氧化碳、温度和湿度数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSIRION_STCC4_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/sensor/sensirion/stcc4/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/stcc4/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_STM32_DIGI_TEMP"></a>

## 161.5 `CONFIG_STM32_DIGI_TEMP`

**提示（Prompt）**：STM32 数字温度传感器（Digital Temperature Sensor）

**说明（Help）**

启用 STM32 数字温度传感器（Digital Temperature Sensor）驱动。此传感器不同于由模数转换器（ADC）读取的 STM32 模拟温度传感器。虽然两个驱动的代码占用相近，模拟温度传感器驱动还要求启用 ADC 驱动。两类传感器在精密度（Precision）、准确度（Accuracy）和功耗方面有所不同。建议查阅数据手册，选择最适合实际需求的传感器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_DIGI_TEMP_ENABLED && CONFIG_SOC_FAMILY_STM32 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/stm32_digi_temp/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stm32_digi_temp/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_TEMP"></a>

## 161.6 `CONFIG_STM32_TEMP`

**提示（Prompt）**：STM32 温度传感器（Temperature Sensor）

**说明（Help）**

启用 STM32 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32 && DT_HAS_ST_STM32_ADC_ENABLED && (DT_HAS_ST_STM32_TEMP_ENABLED || DT_HAS_ST_STM32_TEMP_CAL_ENABLED || DT_HAS_ST_STM32C0_TEMP_CAL_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**被选择（Selected by）**

```text
CONFIG_BT_STM32WBA_USE_TEMP_BASED_CALIB
```

**定义位置（Location）**：[`drivers/sensor/st/stm32_temp/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stm32_temp/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_BT_STM32WBA_USE_TEMP_BASED_CALIB`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA_USE_TEMP_BASED_CALIB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_TEMP_INJECTED"></a>

## 161.7 `CONFIG_STM32_TEMP_INJECTED`

**提示（Prompt）**：通过注入通道（Injected Channel）使用 STM32 温度传感器

**说明（Help）**

使用注入通道（Injected Channel）功能测量温度。这将持续启用 ADC 温度传感器，即将 `VSENSESEL` 位置为 1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_STM32_INJECTED_CHANNELS && CONFIG_STM32_TEMP && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/stm32_temp/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stm32_temp/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STM32 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ADC_STM32_INJECTED_CHANNELS`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STM32_INJECTED_CHANNELS)、[`CONFIG_STM32_TEMP`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STM32_TEMP)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_STM32_TEMP_READ_CALIB_VIA_NVMEM"></a>

## 161.8 `CONFIG_STM32_TEMP_READ_CALIB_VIA_NVMEM`

**提示（Prompt）**：使用 NVMEM 读取温度传感器校准数据（Calibration Data）

**说明（Help）**

通过非易失性存储器（NVMEM）子系统读取校准数据（Calibration Data），代替直接访问原始内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OTP && CONFIG_NVMEM && CONFIG_STM32_TEMP && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/stm32_temp/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stm32_temp/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STM32 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)、[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)、[`CONFIG_STM32_TEMP`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STM32_TEMP)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_STM32_VBAT"></a>

## 161.9 `CONFIG_STM32_VBAT`

**提示（Prompt）**：STM32 Vbat/Vddcore 传感器

**说明（Help）**

启用 STM32 Vbat/Vddcore 传感器驱动，并同时启用模数转换器（ADC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_VBAT_ENABLED || DT_HAS_ST_STM32_VDDCORE_ENABLED) && DT_HAS_ST_STM32_ADC_ENABLED && CONFIG_SOC_FAMILY_STM32 && !CONFIG_SOC_SERIES_STM32F1X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/st/stm32_vbat/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stm32_vbat/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`、`CONFIG_SOC_SERIES_STM32F1X`。

<a id="CONFIG_STM32_VBAT_INJECTED"></a>

## 161.10 `CONFIG_STM32_VBAT_INJECTED`

**提示（Prompt）**：通过注入通道（Injected Channel）使用 STM32 Vbat/Vddcore 传感器

**说明（Help）**

使用注入通道（Injected Channel）功能测量 Vbat/Vddcore。这将持续启用该传感器使用的 ADC 通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_STM32_INJECTED_CHANNELS && CONFIG_STM32_VBAT && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/stm32_vbat/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stm32_vbat/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STM32 Vbat/Vddcore 传感器

**配置项引用（Symbol References）**：[`CONFIG_ADC_STM32_INJECTED_CHANNELS`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STM32_INJECTED_CHANNELS)、[`CONFIG_STM32_VBAT`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STM32_VBAT)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_STM32_VREF"></a>

## 161.11 `CONFIG_STM32_VREF`

**提示（Prompt）**：STM32 VREF 传感器

**说明（Help）**

启用 STM32 Vref 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_ADC_ENABLED && DT_HAS_ST_STM32_VREF_ENABLED && CONFIG_SOC_FAMILY_STM32 && !CONFIG_SOC_SERIES_STM32F1X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/st/stm32_vref/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stm32_vref/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`、`CONFIG_SOC_SERIES_STM32F1X`。

<a id="CONFIG_STM32_VREF_INJECTED"></a>

## 161.12 `CONFIG_STM32_VREF_INJECTED`

**提示（Prompt）**：通过注入通道（Injected Channel）使用 STM32 Vref 传感器

**说明（Help）**

使用注入通道（Injected Channel）功能测量 Vref。这将持续启用 ADC Vref 传感器，即将 `VREFEN` 位置为 1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_STM32_INJECTED_CHANNELS && CONFIG_STM32_VREF && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/stm32_vref/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stm32_vref/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STM32 VREF 传感器

**配置项引用（Symbol References）**：[`CONFIG_ADC_STM32_INJECTED_CHANNELS`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STM32_INJECTED_CHANNELS)、[`CONFIG_STM32_VREF`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STM32_VREF)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_STM32_VREF_READ_CALIB_VIA_NVMEM"></a>

## 161.13 `CONFIG_STM32_VREF_READ_CALIB_VIA_NVMEM`

**提示（Prompt）**：使用 NVMEM 读取 VREF 校准数据（Calibration Data）

**说明（Help）**

通过非易失性存储器（NVMEM）子系统读取校准数据（Calibration Data），代替直接访问原始内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OTP && CONFIG_NVMEM && CONFIG_STM32_VREF && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/stm32_vref/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stm32_vref/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STM32 VREF 传感器

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)、[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)、[`CONFIG_STM32_VREF`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STM32_VREF)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_STMEMSC_I3C_I2C_WRITE_BUFFER_SIZE"></a>

## 161.14 `CONFIG_STMEMSC_I3C_I2C_WRITE_BUFFER_SIZE`

**提示（Prompt）**：ST memsc I2C 写入缓冲区大小

**说明（Help）**

栈上缓冲区的大小，该缓冲区用于复制待写入数据及寄存器地址。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_I2C || CONFIG_I3C) && CONFIG_HAS_STMEMSC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/sensor/st/stmemsc/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stmemsc/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STMEMSC`。

<a id="CONFIG_STS4X"></a>

## 161.15 `CONFIG_STS4X`

**提示（Prompt）**：STS4x 温度传感器（Temperature Sensor）

**说明（Help）**

启用 Sensirion STS4x 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSIRION_STS4X_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sts4x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sts4x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_STTS22H"></a>

## 161.16 `CONFIG_STTS22H`

**提示（Prompt）**：STTS22H 温度传感器（Temperature Sensor）

**说明（Help）**

启用基于 I2C 的 STTS22H 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STTS22H_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_STTS22H
```

**定义位置（Location）**：[`drivers/sensor/st/stts22h/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stts22h/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_STTS22H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_STTS22H)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_STTS22H`。

<a id="CONFIG_STTS22H_THREAD_PRIORITY"></a>

## 161.17 `CONFIG_STTS22H_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STTS22H_TRIGGER_OWN_THREAD && CONFIG_STTS22H_TRIGGER && CONFIG_STTS22H && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS22H 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_STTS22H_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS22H_TRIGGER_OWN_THREAD)、[`CONFIG_STTS22H_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STTS22H_TRIGGER)、[`CONFIG_STTS22H`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS22H)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_STTS22H_TRIGGER`。

<a id="CONFIG_STTS22H_THREAD_STACK_SIZE"></a>

## 161.18 `CONFIG_STTS22H_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STTS22H_TRIGGER_OWN_THREAD && CONFIG_STTS22H_TRIGGER && CONFIG_STTS22H && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS22H 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_STTS22H_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS22H_TRIGGER_OWN_THREAD)、[`CONFIG_STTS22H_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STTS22H_TRIGGER)、[`CONFIG_STTS22H`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS22H)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_STTS22H_TRIGGER`。

<a id="CONFIG_STTS22H_TRIGGER_GLOBAL_THREAD"></a>

## 161.19 `CONFIG_STTS22H_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_STTS22H_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_STTS22H_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS22H 温度传感器（Temperature Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_STTS22H_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS22H_TRIGGER_MODE)、[`CONFIG_STTS22H_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STTS22H_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_STTS22H_TRIGGER`。

<a id="CONFIG_STTS22H_TRIGGER_MODE"></a>

## 161.20 `CONFIG_STTS22H_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STTS22H && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_STTS22H_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_STTS22H_TRIGGER_NONE
CONFIG_STTS22H_TRIGGER_GLOBAL_THREAD
CONFIG_STTS22H_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS22H 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_STTS22H`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS22H)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_STTS22H_TRIGGER_NONE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS22H_TRIGGER_NONE)、[`CONFIG_STTS22H_TRIGGER_GLOBAL_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS22H_TRIGGER_GLOBAL_THREAD)、[`CONFIG_STTS22H_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS22H_TRIGGER_OWN_THREAD)。

<a id="CONFIG_STTS22H_TRIGGER_NONE"></a>

## 161.21 `CONFIG_STTS22H_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STTS22H_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS22H 温度传感器（Temperature Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_STTS22H_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS22H_TRIGGER_MODE)。

<a id="CONFIG_STTS22H_TRIGGER_OWN_THREAD"></a>

## 161.22 `CONFIG_STTS22H_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_STTS22H_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_STTS22H_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS22H 温度传感器（Temperature Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_STTS22H_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS22H_TRIGGER_MODE)、[`CONFIG_STTS22H_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STTS22H_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_STTS22H_TRIGGER`。

<a id="CONFIG_STTS751"></a>

## 161.23 `CONFIG_STTS751`

**提示（Prompt）**：STTS751 温度传感器（Temperature Sensor）

**说明（Help）**

启用基于 I2C 的 STTS751 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STTS751_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_STTS751
```

**定义位置（Location）**：[`drivers/sensor/st/stts751/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stts751/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_STTS751`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_STTS751)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_STTS751`。

<a id="CONFIG_STTS751_SAMPLING_RATE"></a>

## 161.24 `CONFIG_STTS751_SAMPLING_RATE`

**提示（Prompt）**：输出数据速率（Output Data Rate，ODR）

**说明（Help）**

传感器输出数据速率（Output Data Rate），以每秒转换次数表示。芯片支持的速率对应关系为：

- 0：每 16 秒转换 1 次。
- 1：每 8 秒转换 1 次。
- 2：每 4 秒转换 1 次。
- 3：每 2 秒转换 1 次。
- 4：每秒转换 1 次。
- 5：每秒转换 2 次。
- 6：每秒转换 4 次。
- 7：每秒转换 8 次。
- 8：每秒转换 16 次。
- 9：每秒转换 32 次。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STTS751 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[0, 9]
```

**定义位置（Location）**：[`drivers/sensor/st/stts751/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stts751/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS751 温度传感器（Temperature Sensor） → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_STTS751`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS751)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_STTS751_TEMP_HI_THRESHOLD"></a>

## 161.25 `CONFIG_STTS751_TEMP_HI_THRESHOLD`

**提示（Prompt）**：高温阈值报警（High Temperature Threshold Alarm）

**说明（Help）**

触发报警的高温阈值（High Temperature Threshold）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STTS751_TRIGGER && CONFIG_STTS751 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/sensor/st/stts751/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stts751/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS751 温度传感器（Temperature Sensor） → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_STTS751_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STTS751_TRIGGER)、[`CONFIG_STTS751`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS751)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_STTS751_TRIGGER`。

<a id="CONFIG_STTS751_TEMP_LO_THRESHOLD"></a>

## 161.26 `CONFIG_STTS751_TEMP_LO_THRESHOLD`

**提示（Prompt）**：低温阈值报警（Low Temperature Threshold Alarm）

**说明（Help）**

触发报警的低温阈值（Low Temperature Threshold）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STTS751_TRIGGER && CONFIG_STTS751 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/stts751/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stts751/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS751 温度传感器（Temperature Sensor） → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_STTS751_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STTS751_TRIGGER)、[`CONFIG_STTS751`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS751)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_STTS751_TRIGGER`。

<a id="CONFIG_STTS751_THREAD_PRIORITY"></a>

## 161.27 `CONFIG_STTS751_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STTS751_TRIGGER_OWN_THREAD && CONFIG_STTS751 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/stts751/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stts751/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS751 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_STTS751_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS751_TRIGGER_OWN_THREAD)、[`CONFIG_STTS751`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS751)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_STTS751_THREAD_STACK_SIZE"></a>

## 161.28 `CONFIG_STTS751_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STTS751_TRIGGER_OWN_THREAD && CONFIG_STTS751 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/stts751/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stts751/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS751 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_STTS751_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS751_TRIGGER_OWN_THREAD)、[`CONFIG_STTS751`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS751)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_STTS751_TRIGGER_GLOBAL_THREAD"></a>

## 161.29 `CONFIG_STTS751_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_STTS751_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/stts751/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stts751/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS751 温度传感器（Temperature Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_STTS751_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STTS751_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_STTS751_TRIGGER`。

<a id="CONFIG_STTS751_TRIGGER_MODE"></a>

## 161.30 `CONFIG_STTS751_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STTS751 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_STTS751_TRIGGER_GLOBAL_THREAD
```

**可选项（Choices）**

```text
CONFIG_STTS751_TRIGGER_NONE
CONFIG_STTS751_TRIGGER_GLOBAL_THREAD
CONFIG_STTS751_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/stts751/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stts751/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS751 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_STTS751`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS751)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_STTS751_TRIGGER_GLOBAL_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS751_TRIGGER_GLOBAL_THREAD)、[`CONFIG_STTS751_TRIGGER_NONE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS751_TRIGGER_NONE)、[`CONFIG_STTS751_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS751_TRIGGER_OWN_THREAD)。

<a id="CONFIG_STTS751_TRIGGER_NONE"></a>

## 161.31 `CONFIG_STTS751_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STTS751_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/stts751/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stts751/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS751 温度传感器（Temperature Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_STTS751_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STTS751_TRIGGER_MODE)。

<a id="CONFIG_STTS751_TRIGGER_OWN_THREAD"></a>

## 161.32 `CONFIG_STTS751_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_STTS751_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/stts751/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stts751/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → STTS751 温度传感器（Temperature Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_STTS751_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STTS751_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_STTS751_TRIGGER`。

<a id="CONFIG_SX9500"></a>

## 161.33 `CONFIG_SX9500`

**提示（Prompt）**：SX9500 I2C SAR 接近检测芯片（Proximity Chip）

**说明（Help）**

启用基于 I2C 的 SX9500 SAR 接近传感器（Proximity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SEMTECH_SX9500_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/sx9500/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sx9500/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_SX9500_PROX_CHANNEL"></a>

## 161.34 `CONFIG_SX9500_PROX_CHANNEL`

**提示（Prompt）**：使用的接近检测通道（Proximity Channel）

**说明（Help）**

SX9500 提供 4 个独立的接近检测通道（Proximity Channel）。选择正在使用的通道，有效编号为 0 至 3。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SX9500 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/sensor/sx9500/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sx9500/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SX9500 I2C SAR 接近检测芯片（Proximity Chip）

**配置项引用（Symbol References）**：[`CONFIG_SX9500`](P161_drivers_sensor_配置项参考_13.md#CONFIG_SX9500)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SX9500_THREAD_PRIORITY"></a>

## 161.35 `CONFIG_SX9500_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SX9500_TRIGGER_OWN_THREAD && CONFIG_SX9500 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/sx9500/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sx9500/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SX9500 I2C SAR 接近检测芯片（Proximity Chip）

**配置项引用（Symbol References）**：[`CONFIG_SX9500_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_SX9500_TRIGGER_OWN_THREAD)、[`CONFIG_SX9500`](P161_drivers_sensor_配置项参考_13.md#CONFIG_SX9500)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SX9500_THREAD_STACK_SIZE"></a>

## 161.36 `CONFIG_SX9500_THREAD_STACK_SIZE`

**提示（Prompt）**：传感器延迟工作（Delayed Work）线程栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SX9500_TRIGGER_OWN_THREAD && CONFIG_SX9500 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/sx9500/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sx9500/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SX9500 I2C SAR 接近检测芯片（Proximity Chip）

**配置项引用（Symbol References）**：[`CONFIG_SX9500_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_SX9500_TRIGGER_OWN_THREAD)、[`CONFIG_SX9500`](P161_drivers_sensor_配置项参考_13.md#CONFIG_SX9500)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SX9500_TRIGGER_GLOBAL_THREAD"></a>

## 161.37 `CONFIG_SX9500_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SX9500_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/sx9500/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sx9500/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SX9500 I2C SAR 接近检测芯片（Proximity Chip） → SX9500 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_SX9500_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SX9500_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SX9500_TRIGGER`。

<a id="CONFIG_SX9500_TRIGGER_NONE"></a>

## 161.38 `CONFIG_SX9500_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/sx9500/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sx9500/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SX9500 I2C SAR 接近检测芯片（Proximity Chip） → SX9500 触发模式（Trigger Mode）

<a id="CONFIG_SX9500_TRIGGER_OWN_THREAD"></a>

## 161.39 `CONFIG_SX9500_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SX9500_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/sx9500/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sx9500/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SX9500 I2C SAR 接近检测芯片（Proximity Chip） → SX9500 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_SX9500_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SX9500_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SX9500_TRIGGER`。

<a id="CONFIG_TACH_ENE_KB106X"></a>

## 161.40 `CONFIG_TACH_ENE_KB106X`

**提示（Prompt）**：ENE KB106X 转速传感器（Tachometer Sensor）

**说明（Help）**

启用 ENE KB106X 转速传感器（Tachometer Sensor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB106X_TACH_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/ene/kb106x/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ene/kb106x/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_TACH_ENE_KB1200"></a>

## 161.41 `CONFIG_TACH_ENE_KB1200`

**提示（Prompt）**：ENE KB1200 转速传感器（Tachometer Sensor）

**说明（Help）**

启用 ENE KB1200 转速传感器（Tachometer Sensor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB1200_TACH_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/ene_tach_kb1200/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ene_tach_kb1200/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_TACH_GPIO"></a>

## 161.42 `CONFIG_TACH_GPIO`

**提示（Prompt）**：GPIO 转速传感器（Tachometer GPIO Sensor）

**说明（Help）**

启用使用 GPIO 中断的转速传感器（Tachometer Sensor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_TACH_GPIO_ENABLED && CONFIG_GPIO && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/tach_gpio/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tach_gpio/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TACH_IT51XXX"></a>

## 161.43 `CONFIG_TACH_IT51XXX`

**提示（Prompt）**：ITE it51xxx 转速传感器（Tachometer Sensor）

**说明（Help）**

启用 ITE it51xxx 转速传感器（Tachometer Sensor）。it51xxx 支持三个 16 位转速传感器，每个传感器具有两个输入引脚，需要从中选择一个输入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_TACH_ENABLED && CONFIG_SOC_IT51XXX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/ite/ite_tach_it51xxx/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ite/ite_tach_it51xxx/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_IT51XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51XXX)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_IT51XXX`。

<a id="CONFIG_TACH_IT8XXX2"></a>

## 161.44 `CONFIG_TACH_IT8XXX2`

**提示（Prompt）**：ITE it8xxx2 转速传感器（Tachometer Sensor）

**说明（Help）**

启用 ITE it8xxx2 转速传感器（Tachometer Sensor）。it8xxx2 支持两个 16 位转速传感器，每个传感器具有两个输入通道，可从中选择一个输入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_TACH_ENABLED && CONFIG_SOC_IT8XXX2 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/ite/ite_tach_it8xxx2/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ite/ite_tach_it8xxx2/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_IT8XXX2`。

<a id="CONFIG_TACH_NPCX"></a>

## 161.45 `CONFIG_TACH_NPCX`

**提示（Prompt）**：Nuvoton NPCX 转速传感器（Tachometer Sensor）

**说明（Help）**

启用 Nuvoton NPCX 转速传感器（Tachometer Sensor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_TACH_ENABLED && CONFIG_SOC_FAMILY_NPCX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/nuvoton/nuvoton_tach_npcx/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nuvoton/nuvoton_tach_npcx/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCX)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCX`。

<a id="CONFIG_TACH_RTS5912"></a>

## 161.46 `CONFIG_TACH_RTS5912`

**提示（Prompt）**：RTS5912 转速传感器（Tachometer Sensor）

**说明（Help）**

启用 Realtek RTS5912 转速传感器（Tachometer Sensor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_TACH_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/realtek/rts5912/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/realtek/rts5912/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TACH_RTS5912_ASYNC_FETCH"></a>

## 161.47 `CONFIG_TACH_RTS5912_ASYNC_FETCH`

**提示（Prompt）**：异步采样获取（Asynchronous Sample Fetch）

**说明（Help）**

使 `sample_fetch()` 异步执行：立即返回，不等待转速读取完成。注意，这不是 Zephyr 传感器采样获取 API（Sensor Sample Fetch API）的常规行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TACH_RTS5912 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/realtek/rts5912/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/realtek/rts5912/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → RTS5912 转速传感器（Tachometer Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TACH_RTS5912`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TACH_RTS5912)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TACH_RTS5912_DISCARD_SAMPLES"></a>

## 161.48 `CONFIG_TACH_RTS5912_DISCARD_SAMPLES`

**提示（Prompt）**：获取时丢弃前两个采样

**说明（Help）**

执行 `fetch()` 时丢弃前两个采样。在芯片处于低功耗状态时使用转速计（Tachometer），前两个采样可能不可靠，因此此选项很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TACH_RTS5912 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/realtek/rts5912/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/realtek/rts5912/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → RTS5912 转速传感器（Tachometer Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TACH_RTS5912`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TACH_RTS5912)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TACH_XEC"></a>

## 161.49 `CONFIG_TACH_XEC`

**提示（Prompt）**：XEC 转速传感器（Tachometer Sensor）

**说明（Help）**

启用 Microchip XEC 转速传感器（Tachometer Sensor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_TACH_ENABLED && CONFIG_SOC_FAMILY_MICROCHIP_MEC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/microchip/mchp_tach_xec/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mchp_tach_xec/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_TACH_XEC_2_TACH_EDGES"></a>

## 161.50 `CONFIG_TACH_XEC_2_TACH_EDGES`

**提示（Prompt）**：配置为 2 个转速信号边沿，即 1/2 个转速信号周期

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/microchip/mchp_tach_xec/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mchp_tach_xec/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → XEC 转速传感器（Tachometer Sensor） → 转速信号边沿数（Number of Tach Edges）

<a id="CONFIG_TACH_XEC_3_TACH_EDGES"></a>

## 161.51 `CONFIG_TACH_XEC_3_TACH_EDGES`

**提示（Prompt）**：配置为 3 个转速信号边沿，即 1 个转速信号周期

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/microchip/mchp_tach_xec/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mchp_tach_xec/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → XEC 转速传感器（Tachometer Sensor） → 转速信号边沿数（Number of Tach Edges）

<a id="CONFIG_TACH_XEC_5_TACH_EDGES"></a>

## 161.52 `CONFIG_TACH_XEC_5_TACH_EDGES`

**提示（Prompt）**：配置为 5 个转速信号边沿，即 2 个转速信号周期

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/microchip/mchp_tach_xec/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mchp_tach_xec/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → XEC 转速传感器（Tachometer Sensor） → 转速信号边沿数（Number of Tach Edges）

<a id="CONFIG_TACH_XEC_9_TACH_EDGES"></a>

## 161.53 `CONFIG_TACH_XEC_9_TACH_EDGES`

**提示（Prompt）**：配置为 9 个转速信号边沿，即 4 个转速信号周期

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/microchip/mchp_tach_xec/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mchp_tach_xec/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → XEC 转速传感器（Tachometer Sensor） → 转速信号边沿数（Number of Tach Edges）

<a id="CONFIG_TAD2144"></a>

## 161.54 `CONFIG_TAD2144`

**提示（Prompt）**：TAD2144 隧道磁阻角度传感器件（TMR Angle Sensor Device）

**说明（Help）**

启用基于 SPI 的 TAD2144 隧道磁阻（TMR）角度传感器件驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INVENSENSE_TAD2144_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI if n
CONFIG_I2C if n
CONFIG_USE_EMD_TAD2144
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/sensor/tdk/tad2144/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/tad2144/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USE_EMD_TAD2144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_TAD2144)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_TAD2144_THREAD_PRIORITY"></a>

## 161.55 `CONFIG_TAD2144_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TAD2144_TRIGGER_OWN_THREAD && CONFIG_TAD2144 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/tdk/tad2144/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/tad2144/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TAD2144 隧道磁阻角度传感器件（TMR Angle Sensor Device）

**配置项引用（Symbol References）**：[`CONFIG_TAD2144_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TAD2144_TRIGGER_OWN_THREAD)、[`CONFIG_TAD2144`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TAD2144)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TAD2144_THREAD_STACK_SIZE"></a>

## 161.56 `CONFIG_TAD2144_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TAD2144_TRIGGER_OWN_THREAD && CONFIG_TAD2144 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/tdk/tad2144/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/tad2144/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TAD2144 隧道磁阻角度传感器件（TMR Angle Sensor Device）

**配置项引用（Symbol References）**：[`CONFIG_TAD2144_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TAD2144_TRIGGER_OWN_THREAD)、[`CONFIG_TAD2144`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TAD2144)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TAD2144_TRIGGER_GLOBAL_THREAD"></a>

## 161.57 `CONFIG_TAD2144_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_TAD2144_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_TAD2144_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/tdk/tad2144/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/tad2144/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TAD2144 隧道磁阻角度传感器件（TMR Angle Sensor Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_TAD2144_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TAD2144_TRIGGER_MODE)、[`CONFIG_TAD2144_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TAD2144_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TAD2144_TRIGGER`。

<a id="CONFIG_TAD2144_TRIGGER_MODE"></a>

## 161.58 `CONFIG_TAD2144_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TAD2144 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_TAD2144_TRIGGER_GLOBAL_THREAD
```

**可选项（Choices）**

```text
CONFIG_TAD2144_TRIGGER_NONE
CONFIG_TAD2144_TRIGGER_GLOBAL_THREAD
CONFIG_TAD2144_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/tdk/tad2144/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/tad2144/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TAD2144 隧道磁阻角度传感器件（TMR Angle Sensor Device）

**配置项引用（Symbol References）**：[`CONFIG_TAD2144`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TAD2144)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_TAD2144_TRIGGER_GLOBAL_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TAD2144_TRIGGER_GLOBAL_THREAD)、[`CONFIG_TAD2144_TRIGGER_NONE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TAD2144_TRIGGER_NONE)、[`CONFIG_TAD2144_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TAD2144_TRIGGER_OWN_THREAD)。

<a id="CONFIG_TAD2144_TRIGGER_NONE"></a>

## 161.59 `CONFIG_TAD2144_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TAD2144_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/tdk/tad2144/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/tad2144/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TAD2144 隧道磁阻角度传感器件（TMR Angle Sensor Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TAD2144_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TAD2144_TRIGGER_MODE)。

<a id="CONFIG_TAD2144_TRIGGER_OWN_THREAD"></a>

## 161.60 `CONFIG_TAD2144_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_TAD2144_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_TAD2144_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/tdk/tad2144/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/tad2144/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TAD2144 隧道磁阻角度传感器件（TMR Angle Sensor Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_TAD2144_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TAD2144_TRIGGER_MODE)、[`CONFIG_TAD2144_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TAD2144_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TAD2144_TRIGGER`。

<a id="CONFIG_TCN75A"></a>

## 161.61 `CONFIG_TCN75A`

**提示（Prompt）**：TCN75A 环境温度传感器（Ambient Temperature Sensor）

**说明（Help）**

启用 TCN75A 环境温度数字转换器（Ambient Temperature to Digital Converter）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_TCN75A_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/microchip/tcn75a/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/tcn75a/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TCN75A_THREAD_PRIORITY"></a>

## 161.62 `CONFIG_TCN75A_THREAD_PRIORITY`

**提示（Prompt）**：专用线程优先级（Own Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TCN75A_TRIGGER_OWN_THREAD && CONFIG_TCN75A && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/microchip/tcn75a/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/tcn75a/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TCN75A 环境温度传感器（Ambient Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TCN75A_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TCN75A_TRIGGER_OWN_THREAD)、[`CONFIG_TCN75A`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TCN75A)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TCN75A_THREAD_STACK_SIZE"></a>

## 161.63 `CONFIG_TCN75A_THREAD_STACK_SIZE`

**提示（Prompt）**：专用线程栈大小（Own Thread Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TCN75A_TRIGGER_OWN_THREAD && CONFIG_TCN75A && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/microchip/tcn75a/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/tcn75a/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TCN75A 环境温度传感器（Ambient Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TCN75A_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TCN75A_TRIGGER_OWN_THREAD)、[`CONFIG_TCN75A`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TCN75A)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TCN75A_TRIGGER"></a>

## 161.64 `CONFIG_TCN75A_TRIGGER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TCN75A 基于中断的触发支持。要求将传感器设置为连续采样模式（Continuous Sample Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TCN75A && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/microchip/tcn75a/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/tcn75a/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TCN75A 环境温度传感器（Ambient Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TCN75A`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TCN75A)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TCN75A_TRIGGER_GLOBAL_THREAD"></a>

## 161.65 `CONFIG_TCN75A_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TCN75A_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/microchip/tcn75a/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/tcn75a/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TCN75A 环境温度传感器（Ambient Temperature Sensor） → TCN75A 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TCN75A_TRIGGER`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TCN75A_TRIGGER)。

<a id="CONFIG_TCN75A_TRIGGER_NONE"></a>

## 161.66 `CONFIG_TCN75A_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/microchip/tcn75a/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/tcn75a/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TCN75A 环境温度传感器（Ambient Temperature Sensor） → TCN75A 触发模式（Trigger Mode）

<a id="CONFIG_TCN75A_TRIGGER_OWN_THREAD"></a>

## 161.67 `CONFIG_TCN75A_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TCN75A_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/microchip/tcn75a/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/tcn75a/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TCN75A 环境温度传感器（Ambient Temperature Sensor） → TCN75A 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TCN75A_TRIGGER`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TCN75A_TRIGGER)。

<a id="CONFIG_TCS3400"></a>

## 161.68 `CONFIG_TCS3400`

**提示（Prompt）**：TCS3400 传感器（Sensor）

**说明（Help）**

启用 TCS3400 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMS_TCS3400_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ams/tcs3400/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tcs3400/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TCS34725"></a>

## 161.69 `CONFIG_TCS34725`

**提示（Prompt）**：TCS34725 颜色传感器（Color Sensor）

**说明（Help）**

启用 TCS34725 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMS_TCS34725_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ams/tcs34725/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tcs34725/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TEMP_KINETIS"></a>

## 161.70 `CONFIG_TEMP_KINETIS`

**提示（Prompt）**：NXP Kinetis 温度传感器（Temperature Sensor）

**说明（Help）**

启用 NXP Kinetis 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_TEMPERATURE_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/nxp/nxp_kinetis_temp/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/nxp_kinetis_temp/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_TEMP_KINETIS_FILTER"></a>

## 161.71 `CONFIG_TEMP_KINETIS_FILTER`

**提示（Prompt）**：对 ADC 读数进行数字滤波（Digital Filtering）

**说明（Help）**

按照 NXP AN3031，对 ADC 读数启用加权平均数字滤波（Weighted Average Digital Filtering）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TEMP_KINETIS && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nxp/nxp_kinetis_temp/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/nxp_kinetis_temp/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → NXP Kinetis 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TEMP_KINETIS`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_KINETIS)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TEMP_KINETIS_OVERSAMPLING"></a>

## 161.72 `CONFIG_TEMP_KINETIS_OVERSAMPLING`

**提示（Prompt）**：ADC 过采样（Oversampling）

**说明（Help）**

温度传感器和带隙电压（Bandgap Voltage）读数使用的 ADC 过采样（Oversampling）设置。过采样有助于获得更稳定的读数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TEMP_KINETIS && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 5]
```

**定义位置（Location）**：[`drivers/sensor/nxp/nxp_kinetis_temp/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/nxp_kinetis_temp/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → NXP Kinetis 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TEMP_KINETIS`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_KINETIS)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TEMP_KINETIS_RESOLUTION"></a>

## 161.73 `CONFIG_TEMP_KINETIS_RESOLUTION`

**提示（Prompt）**：ADC 分辨率（Resolution）

**说明（Help）**

温度传感器和带隙电压（Bandgap Voltage）读数使用的 ADC 分辨率（Resolution）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TEMP_KINETIS && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
16 if CONFIG_ADC_MCUX_ADC16
12 if CONFIG_ADC_MCUX_ADC12
```

**定义位置（Location）**：[`drivers/sensor/nxp/nxp_kinetis_temp/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/nxp_kinetis_temp/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → NXP Kinetis 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TEMP_KINETIS`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_KINETIS)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_ADC_MCUX_ADC16`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_ADC16)、[`CONFIG_ADC_MCUX_ADC12`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_ADC12)。

<a id="CONFIG_TEMP_MICROCRYSTAL_RV3032_INIT_PRIORITY"></a>

## 161.74 `CONFIG_TEMP_MICROCRYSTAL_RV3032_INIT_PRIORITY`

**提示（Prompt）**：rc3032c7 温度传感器初始化优先级（Init Priority）

**说明（Help）**

Microcrystal rv3032c7 传感器驱动的初始化优先级（Initialization Priority）。

译注：对应标题原文写作 rc3032c7，帮助原文写作 rv3032c7；此处保留原文型号差异。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RV3032_TEMP && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/sensor/rv3032_temp/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/rv3032_temp/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → RV3032 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_RV3032_TEMP`](P160_drivers_sensor_配置项参考_12.md#CONFIG_RV3032_TEMP)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TEMP_NRF5"></a>

## 161.75 `CONFIG_TEMP_NRF5`

**提示（Prompt）**：nRF5 温度传感器（Temperature Sensor）

**说明（Help）**

启用 nRF5 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_TEMP_ENABLED && (CONFIG_MULTITHREADING || CONFIG_TEMP_NRF5_FORCE_ALT) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_NRF_802154_SL_OPENSOURCE
CONFIG_NRF_802154_SL_OPENSOURCE
CONFIG_CLOCK_CONTROL_NRF_USES_TEMP_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nordic/temp/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nordic/temp/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_TEMP_NRF5_FORCE_ALT`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_NRF5_FORCE_ALT)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_NRF_802154_SL_OPENSOURCE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_802154_SL_OPENSOURCE)、[`CONFIG_CLOCK_CONTROL_NRF_USES_TEMP_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_USES_TEMP_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_USES_TEMP_SENSOR`。

<a id="CONFIG_TEMP_NRF5_FORCE_ALT"></a>

## 161.76 `CONFIG_TEMP_NRF5_FORCE_ALT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用此选项可强制使用温度传感器驱动的另一种实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nordic/temp/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nordic/temp/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF`。

<a id="CONFIG_TEMP_NRFS"></a>

## 161.77 `CONFIG_TEMP_NRFS`

**提示（Prompt）**：通过 nrfs 访问的 nRF 温度传感器

**说明（Help）**

启用通过 nRF 服务层（nRF Services，nrfs）访问的 nRF 温度传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_TEMP_NRFS_ENABLED && CONFIG_NRFS && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/nordic/temp/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nordic/temp/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TEMP_NRFS_THREAD_PRIORITY"></a>

## 161.78 `CONFIG_TEMP_NRFS_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TEMP_NRFS_TRIGGER_OWN_THREAD && CONFIG_TEMP_NRFS_TRIGGER && CONFIG_TEMP_NRFS && CONFIG_NRFS_TEMP_SERVICE_SUBSCRIPTION_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 通过 nrfs 访问的 nRF 温度传感器

**配置项引用（Symbol References）**：[`CONFIG_TEMP_NRFS_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_NRFS_TRIGGER_OWN_THREAD)、[`CONFIG_TEMP_NRFS_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEMP_NRFS_TRIGGER)、[`CONFIG_TEMP_NRFS`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_NRFS)、[`CONFIG_NRFS_TEMP_SERVICE_SUBSCRIPTION_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_TEMP_SERVICE_SUBSCRIPTION_ENABLED)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TEMP_NRFS_TRIGGER`。

<a id="CONFIG_TEMP_NRFS_THREAD_STACK_SIZE"></a>

## 161.79 `CONFIG_TEMP_NRFS_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TEMP_NRFS_TRIGGER_OWN_THREAD && CONFIG_TEMP_NRFS_TRIGGER && CONFIG_TEMP_NRFS && CONFIG_NRFS_TEMP_SERVICE_SUBSCRIPTION_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 通过 nrfs 访问的 nRF 温度传感器

**配置项引用（Symbol References）**：[`CONFIG_TEMP_NRFS_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_NRFS_TRIGGER_OWN_THREAD)、[`CONFIG_TEMP_NRFS_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEMP_NRFS_TRIGGER)、[`CONFIG_TEMP_NRFS`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_NRFS)、[`CONFIG_NRFS_TEMP_SERVICE_SUBSCRIPTION_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_TEMP_SERVICE_SUBSCRIPTION_ENABLED)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TEMP_NRFS_TRIGGER`。

<a id="CONFIG_TEMP_NRFS_TRIGGER_GLOBAL_THREAD"></a>

## 161.80 `CONFIG_TEMP_NRFS_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_TEMP_NRFS_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_TEMP_NRFS_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 通过 nrfs 访问的 nRF 温度传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_TEMP_NRFS_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_NRFS_TRIGGER_MODE)、[`CONFIG_TEMP_NRFS_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEMP_NRFS_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TEMP_NRFS_TRIGGER`。

<a id="CONFIG_TEMP_NRFS_TRIGGER_MODE"></a>

## 161.81 `CONFIG_TEMP_NRFS_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TEMP_NRFS && CONFIG_NRFS_TEMP_SERVICE_SUBSCRIPTION_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_TEMP_NRFS_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_TEMP_NRFS_TRIGGER_NONE
CONFIG_TEMP_NRFS_TRIGGER_GLOBAL_THREAD
CONFIG_TEMP_NRFS_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 通过 nrfs 访问的 nRF 温度传感器

**配置项引用（Symbol References）**：[`CONFIG_TEMP_NRFS`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_NRFS)、[`CONFIG_NRFS_TEMP_SERVICE_SUBSCRIPTION_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_TEMP_SERVICE_SUBSCRIPTION_ENABLED)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_TEMP_NRFS_TRIGGER_NONE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_NRFS_TRIGGER_NONE)、[`CONFIG_TEMP_NRFS_TRIGGER_GLOBAL_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_NRFS_TRIGGER_GLOBAL_THREAD)、[`CONFIG_TEMP_NRFS_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_NRFS_TRIGGER_OWN_THREAD)。

<a id="CONFIG_TEMP_NRFS_TRIGGER_NONE"></a>

## 161.82 `CONFIG_TEMP_NRFS_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TEMP_NRFS_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 通过 nrfs 访问的 nRF 温度传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TEMP_NRFS_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_NRFS_TRIGGER_MODE)。

<a id="CONFIG_TEMP_NRFS_TRIGGER_OWN_THREAD"></a>

## 161.83 `CONFIG_TEMP_NRFS_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_TEMP_NRFS_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_TEMP_NRFS_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 通过 nrfs 访问的 nRF 温度传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_TEMP_NRFS_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TEMP_NRFS_TRIGGER_MODE)、[`CONFIG_TEMP_NRFS_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEMP_NRFS_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TEMP_NRFS_TRIGGER`。

<a id="CONFIG_TEMP_SILABS_EMU"></a>

## 161.84 `CONFIG_TEMP_SILABS_EMU`

**提示（Prompt）**：Silicon Labs Series 2 EMU 温度传感器

**说明（Help）**

启用 Silicon Labs Series 2（EFR32/EFM32）器件中 EMU 的内部裸片温度传感器（Die Temperature Sensor），通过 `sl_hal_emu_get_temperature()` 读取。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_EMU_TEMP_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_EMU
```

**定义位置（Location）**：[`drivers/sensor/silabs/emu_temp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/silabs/emu_temp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SILABS_SISDK_EMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_EMU)。

<a id="CONFIG_TH02"></a>

## 161.85 `CONFIG_TH02`

**提示（Prompt）**：TH02 温度传感器（Temperature Sensor）

**说明（Help）**

启用 TH02 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HOPERF_TH02_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/th02/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/th02/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TI_HDC"></a>

## 161.86 `CONFIG_TI_HDC`

**提示（Prompt）**：Texas Instruments 温湿度传感器（例如 HDC1008）

**说明（Help）**

启用 TI 温湿度传感器（Temperature and Humidity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_HDC_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/ti_hdc/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ti_hdc/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TI_HDC20XX"></a>

## 161.87 `CONFIG_TI_HDC20XX`

**提示（Prompt）**：Texas Instruments HDC20XX 温湿度传感器

**说明（Help）**

启用 TI HDC20XX 温湿度传感器（Temperature and Humidity Sensor）驱动，例如 HDC2010、HDC2021、HDC2022、HDC2080。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_HDC2010_ENABLED || DT_HAS_TI_HDC2021_ENABLED || DT_HAS_TI_HDC2022_ENABLED || DT_HAS_TI_HDC2080_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/ti_hdc20xx/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ti_hdc20xx/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TI_HDC302X"></a>

## 161.88 `CONFIG_TI_HDC302X`

**提示（Prompt）**：Texas Instruments HDC302X 温湿度传感器

**说明（Help）**

启用 TI HDC302X 温湿度传感器（Temperature and Humidity Sensor）驱动，例如 HDC3020、HDC3021、HDC3022。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_HDC302X_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/sensor/ti/ti_hdc302x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ti_hdc302x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_TLE9104_DIAGNOSTICS"></a>

## 161.89 `CONFIG_TLE9104_DIAGNOSTICS`

**提示（Prompt）**：TLE9104 输出诊断（Output Diagnostics）

**说明（Help）**

启用动力系统开关（Power Train Switch）TLE9104 的输出诊断（Output Diagnostics）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_TLE9104_DIAGNOSTICS_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/infineon/tle9104/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/tle9104/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TMAG5170"></a>

## 161.90 `CONFIG_TMAG5170`

**提示（Prompt）**：TMAG5170 SPI 霍尔效应传感器（Hall-effect Sensor）驱动

**说明（Help）**

启用 TMAG5170 霍尔效应传感器（Hall-effect Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TMAG5170_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/sensor/ti/tmag5170/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmag5170/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_TMAG5170_CRC"></a>

## 161.91 `CONFIG_TMAG5170_CRC`

**提示（Prompt）**：使用循环冗余校验（CRC）错误检测

**说明（Help）**

校验接收（RX）数据的 CRC，并为发送（TX）数据附加 CRC

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TMAG5170 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/sensor/ti/tmag5170/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmag5170/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMAG5170 SPI 霍尔效应传感器（Hall-effect Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_TMAG5170`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5170)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_TMAG5170_THREAD_PRIORITY"></a>

## 161.92 `CONFIG_TMAG5170_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TMAG5170_TRIGGER_OWN_THREAD && CONFIG_TMAG5170_TRIGGER && CONFIG_TMAG5170 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/ti/tmag5170/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmag5170/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMAG5170 SPI 霍尔效应传感器（Hall-effect Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_TMAG5170_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5170_TRIGGER_OWN_THREAD)、[`CONFIG_TMAG5170_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMAG5170_TRIGGER)、[`CONFIG_TMAG5170`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5170)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMAG5170_TRIGGER`。

<a id="CONFIG_TMAG5170_THREAD_STACK_SIZE"></a>

## 161.93 `CONFIG_TMAG5170_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TMAG5170_TRIGGER_OWN_THREAD && CONFIG_TMAG5170_TRIGGER && CONFIG_TMAG5170 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/ti/tmag5170/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmag5170/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMAG5170 SPI 霍尔效应传感器（Hall-effect Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_TMAG5170_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5170_TRIGGER_OWN_THREAD)、[`CONFIG_TMAG5170_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMAG5170_TRIGGER)、[`CONFIG_TMAG5170`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5170)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMAG5170_TRIGGER`。

<a id="CONFIG_TMAG5170_TRIGGER_DIRECT"></a>

## 161.94 `CONFIG_TMAG5170_TRIGGER_DIRECT`

**提示（Prompt）**：在中断上下文（Interrupt Context）中处理触发事件

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TMAG5170_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ti/tmag5170/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmag5170/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMAG5170 SPI 霍尔效应传感器（Hall-effect Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TMAG5170_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMAG5170_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMAG5170_TRIGGER`。

<a id="CONFIG_TMAG5170_TRIGGER_GLOBAL_THREAD"></a>

## 161.95 `CONFIG_TMAG5170_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TMAG5170_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ti/tmag5170/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmag5170/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMAG5170 SPI 霍尔效应传感器（Hall-effect Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TMAG5170_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMAG5170_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMAG5170_TRIGGER`。

<a id="CONFIG_TMAG5170_TRIGGER_MODE"></a>

## 161.96 `CONFIG_TMAG5170_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TMAG5170 && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_TMAG5170_TRIGGER_NONE
CONFIG_TMAG5170_TRIGGER_GLOBAL_THREAD
CONFIG_TMAG5170_TRIGGER_OWN_THREAD
CONFIG_TMAG5170_TRIGGER_DIRECT
```

**定义位置（Location）**：[`drivers/sensor/ti/tmag5170/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmag5170/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMAG5170 SPI 霍尔效应传感器（Hall-effect Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_TMAG5170`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5170)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_TMAG5170_TRIGGER_NONE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5170_TRIGGER_NONE)、[`CONFIG_TMAG5170_TRIGGER_GLOBAL_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5170_TRIGGER_GLOBAL_THREAD)、[`CONFIG_TMAG5170_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5170_TRIGGER_OWN_THREAD)、[`CONFIG_TMAG5170_TRIGGER_DIRECT`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5170_TRIGGER_DIRECT)。

<a id="CONFIG_TMAG5170_TRIGGER_NONE"></a>

## 161.97 `CONFIG_TMAG5170_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TMAG5170_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/ti/tmag5170/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmag5170/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMAG5170 SPI 霍尔效应传感器（Hall-effect Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TMAG5170_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5170_TRIGGER_MODE)。

<a id="CONFIG_TMAG5170_TRIGGER_OWN_THREAD"></a>

## 161.98 `CONFIG_TMAG5170_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TMAG5170_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ti/tmag5170/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmag5170/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMAG5170 SPI 霍尔效应传感器（Hall-effect Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TMAG5170_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMAG5170_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMAG5170_TRIGGER`。

<a id="CONFIG_TMAG5273"></a>

## 161.99 `CONFIG_TMAG5273`

**提示（Prompt）**：TMAG5273/TMAG3001 三维霍尔效应传感器（3D Hall-Effect Sensor）

**说明（Help）**

启用基于 I2C 的 TMAG5273 和 TMAG3001 三维霍尔效应传感器（3D Hall-Effect Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_TMAG5273_ENABLED || DT_HAS_TI_TMAG3001_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO
```

**弱选择（Implies）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/sensor/ti/tmag5273/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmag5273/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_TMD2620"></a>

## 161.100 `CONFIG_TMD2620`

**提示（Prompt）**：OSRAM-AMS TMD2620 接近传感器（Proximity Sensor）

**说明（Help）**

启用 TMD2620 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMS_TMD2620_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ams/tmd2620/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tmd2620/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<!-- kconfig-navigation -->

[上一章](P160_drivers_sensor_配置项参考_12.md) · [返回大纲](大纲.md) · [下一章](P162_drivers_sensor_配置项参考_14.md)
