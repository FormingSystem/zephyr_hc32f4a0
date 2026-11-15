---
id: learning.zephyr-docs.kconfig-reference.page-163
title: "`drivers/sensor`配置项参考（15/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第163章\_`drivers/sensor`配置项参考（15/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 25 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_WSEN_ITDS_2533020201601_TRIGGER_MODE"></a>

## 163.1 `CONFIG_WSEN_ITDS_2533020201601_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ITDS_2533020201601 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_WSEN_ITDS_2533020201601_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_WSEN_ITDS_2533020201601_TRIGGER_NONE
CONFIG_WSEN_ITDS_2533020201601_TRIGGER_GLOBAL_THREAD
CONFIG_WSEN_ITDS_2533020201601_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ITDS-2533020201601 三轴加速度传感器（3-axis Acceleration Sensor）

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ITDS_2533020201601`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ITDS_2533020201601)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_WSEN_ITDS_2533020201601_TRIGGER_NONE`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_ITDS_2533020201601_TRIGGER_NONE)、[`CONFIG_WSEN_ITDS_2533020201601_TRIGGER_GLOBAL_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ITDS_2533020201601_TRIGGER_GLOBAL_THREAD)、[`CONFIG_WSEN_ITDS_2533020201601_TRIGGER_OWN_THREAD`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_ITDS_2533020201601_TRIGGER_OWN_THREAD)。

<a id="CONFIG_WSEN_ITDS_2533020201601_TRIGGER_NONE"></a>

## 163.2 `CONFIG_WSEN_ITDS_2533020201601_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WSEN_ITDS_2533020201601_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ITDS-2533020201601 三轴加速度传感器（3-axis Acceleration Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ITDS_2533020201601_TRIGGER_MODE`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_ITDS_2533020201601_TRIGGER_MODE)。

<a id="CONFIG_WSEN_ITDS_2533020201601_TRIGGER_OWN_THREAD"></a>

## 163.3 `CONFIG_WSEN_ITDS_2533020201601_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_WSEN_ITDS_2533020201601_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_WSEN_ITDS_2533020201601_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ITDS-2533020201601 三轴加速度传感器（3-axis Acceleration Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_WSEN_ITDS_2533020201601_TRIGGER_MODE`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_ITDS_2533020201601_TRIGGER_MODE)、[`CONFIG_WSEN_ITDS_2533020201601_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ITDS_2533020201601_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_ITDS_2533020201601_TRIGGER`。

<a id="CONFIG_WSEN_PADS_2511020213301"></a>

## 163.4 `CONFIG_WSEN_PADS_2511020213301`

**提示（Prompt）**：WSEN-PADS-2511020213301 绝对压力与温度传感器

**说明（Help）**

启用基于 I2C/SPI、集成温度传感器的 WSEN-PADS-2511020213301 绝对压力传感器（Absolute Pressure Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WE_WSEN_PADS_2511020213301_ENABLED && CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_HAS_WESENSORS
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_HAS_WESENSORS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_WESENSORS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`、`CONFIG_HAS_WESENSORS`。

<a id="CONFIG_WSEN_PADS_2511020213301_PRESSURE_THRESHOLD"></a>

## 163.5 `CONFIG_WSEN_PADS_2511020213301_PRESSURE_THRESHOLD`

**提示（Prompt）**：压力阈值触发器（Pressure Threshold Triggers）

**说明（Help）**

允许为高压阈值和／或低压阈值设置触发器。启用后，不能设置数据就绪触发器（Data Ready Trigger）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_PADS_2511020213301_TRIGGER && CONFIG_WSEN_PADS_2511020213301 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-PADS-2511020213301 绝对压力与温度传感器

**配置项引用（Symbol References）**：[`CONFIG_WSEN_PADS_2511020213301_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_PADS_2511020213301_TRIGGER)、[`CONFIG_WSEN_PADS_2511020213301`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_PADS_2511020213301)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_PADS_2511020213301_TRIGGER`。

<a id="CONFIG_WSEN_PADS_2511020213301_THREAD_PRIORITY"></a>

## 163.6 `CONFIG_WSEN_PADS_2511020213301_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_PADS_2511020213301_TRIGGER_OWN_THREAD && CONFIG_WSEN_PADS_2511020213301 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-PADS-2511020213301 绝对压力与温度传感器

**配置项引用（Symbol References）**：[`CONFIG_WSEN_PADS_2511020213301_TRIGGER_OWN_THREAD`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_PADS_2511020213301_TRIGGER_OWN_THREAD)、[`CONFIG_WSEN_PADS_2511020213301`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_PADS_2511020213301)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_WSEN_PADS_2511020213301_THREAD_STACK_SIZE"></a>

## 163.7 `CONFIG_WSEN_PADS_2511020213301_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_PADS_2511020213301_TRIGGER_OWN_THREAD && CONFIG_WSEN_PADS_2511020213301 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-PADS-2511020213301 绝对压力与温度传感器

**配置项引用（Symbol References）**：[`CONFIG_WSEN_PADS_2511020213301_TRIGGER_OWN_THREAD`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_PADS_2511020213301_TRIGGER_OWN_THREAD)、[`CONFIG_WSEN_PADS_2511020213301`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_PADS_2511020213301)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_WSEN_PADS_2511020213301_TRIGGER_GLOBAL_THREAD"></a>

## 163.8 `CONFIG_WSEN_PADS_2511020213301_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_WSEN_PADS_2511020213301_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_WSEN_PADS_2511020213301_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-PADS-2511020213301 绝对压力与温度传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_WSEN_PADS_2511020213301_TRIGGER_MODE`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_PADS_2511020213301_TRIGGER_MODE)、[`CONFIG_WSEN_PADS_2511020213301_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_PADS_2511020213301_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_PADS_2511020213301_TRIGGER`。

<a id="CONFIG_WSEN_PADS_2511020213301_TRIGGER_MODE"></a>

## 163.9 `CONFIG_WSEN_PADS_2511020213301_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_PADS_2511020213301 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_WSEN_PADS_2511020213301_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_WSEN_PADS_2511020213301_TRIGGER_NONE
CONFIG_WSEN_PADS_2511020213301_TRIGGER_GLOBAL_THREAD
CONFIG_WSEN_PADS_2511020213301_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-PADS-2511020213301 绝对压力与温度传感器

**配置项引用（Symbol References）**：[`CONFIG_WSEN_PADS_2511020213301`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_PADS_2511020213301)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_WSEN_PADS_2511020213301_TRIGGER_NONE`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_PADS_2511020213301_TRIGGER_NONE)、[`CONFIG_WSEN_PADS_2511020213301_TRIGGER_GLOBAL_THREAD`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_PADS_2511020213301_TRIGGER_GLOBAL_THREAD)、[`CONFIG_WSEN_PADS_2511020213301_TRIGGER_OWN_THREAD`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_PADS_2511020213301_TRIGGER_OWN_THREAD)。

<a id="CONFIG_WSEN_PADS_2511020213301_TRIGGER_NONE"></a>

## 163.10 `CONFIG_WSEN_PADS_2511020213301_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WSEN_PADS_2511020213301_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-PADS-2511020213301 绝对压力与温度传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_WSEN_PADS_2511020213301_TRIGGER_MODE`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_PADS_2511020213301_TRIGGER_MODE)。

<a id="CONFIG_WSEN_PADS_2511020213301_TRIGGER_OWN_THREAD"></a>

## 163.11 `CONFIG_WSEN_PADS_2511020213301_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_WSEN_PADS_2511020213301_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_WSEN_PADS_2511020213301_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_pads_2511020213301/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-PADS-2511020213301 绝对压力与温度传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_WSEN_PADS_2511020213301_TRIGGER_MODE`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_PADS_2511020213301_TRIGGER_MODE)、[`CONFIG_WSEN_PADS_2511020213301_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_PADS_2511020213301_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_PADS_2511020213301_TRIGGER`。

<a id="CONFIG_WSEN_PDMS_25131308XXX05"></a>

## 163.12 `CONFIG_WSEN_PDMS_25131308XXX05`

**提示（Prompt）**：WSEN-PDMS-25131308XXX05 差压传感器（Differential Pressure Sensor）

**说明（Help）**

启用基于 I2C/SPI 的 WSEN-PDMS-25131308XXX05 差压传感器（Differential Pressure Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WE_WSEN_PDMS_25131308XXX05_ENABLED && CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_HAS_WESENSORS
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_pdms_25131308XXX05/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_pdms_25131308XXX05/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_HAS_WESENSORS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_WESENSORS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`、`CONFIG_HAS_WESENSORS`。

<a id="CONFIG_WSEN_PDUS_25131308XXXXX"></a>

## 163.13 `CONFIG_WSEN_PDUS_25131308XXXXX`

**提示（Prompt）**：WSEN-PDUS-25131308XXXXX 差压传感器（Differential Pressure Sensor）

**说明（Help）**

启用基于 I2C 的 WSEN-PDUS-25131308XXXXX 差压传感器（Differential Pressure Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WE_WSEN_PDUS_25131308XXXXX_ENABLED && CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_HAS_WESENSORS
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_pdus_25131308XXXXX/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_pdus_25131308XXXXX/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_HAS_WESENSORS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_WESENSORS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`、`CONFIG_HAS_WESENSORS`。

<a id="CONFIG_WSEN_TIDS_2521020222501"></a>

## 163.14 `CONFIG_WSEN_TIDS_2521020222501`

**提示（Prompt）**：WSEN-TIDS-2521020222501 温度传感器（Temperature Sensor）

**说明（Help）**

启用基于 I2C 的 WSEN-TIDS-2521020222501 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WE_WSEN_TIDS_2521020222501_ENABLED && CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_HAS_WESENSORS
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_HAS_WESENSORS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_WESENSORS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`、`CONFIG_HAS_WESENSORS`。

<a id="CONFIG_WSEN_TIDS_2521020222501_THREAD_PRIORITY"></a>

## 163.15 `CONFIG_WSEN_TIDS_2521020222501_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_TIDS_2521020222501_TRIGGER_OWN_THREAD && CONFIG_WSEN_TIDS_2521020222501 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-TIDS-2521020222501 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_WSEN_TIDS_2521020222501_TRIGGER_OWN_THREAD`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_TIDS_2521020222501_TRIGGER_OWN_THREAD)、[`CONFIG_WSEN_TIDS_2521020222501`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_TIDS_2521020222501)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_WSEN_TIDS_2521020222501_THREAD_STACK_SIZE"></a>

## 163.16 `CONFIG_WSEN_TIDS_2521020222501_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_TIDS_2521020222501_TRIGGER_OWN_THREAD && CONFIG_WSEN_TIDS_2521020222501 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-TIDS-2521020222501 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_WSEN_TIDS_2521020222501_TRIGGER_OWN_THREAD`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_TIDS_2521020222501_TRIGGER_OWN_THREAD)、[`CONFIG_WSEN_TIDS_2521020222501`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_TIDS_2521020222501)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_WSEN_TIDS_2521020222501_TRIGGER_GLOBAL_THREAD"></a>

## 163.17 `CONFIG_WSEN_TIDS_2521020222501_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_WSEN_TIDS_2521020222501_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_WSEN_TIDS_2521020222501_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-TIDS-2521020222501 温度传感器（Temperature Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_WSEN_TIDS_2521020222501_TRIGGER_MODE`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_TIDS_2521020222501_TRIGGER_MODE)、[`CONFIG_WSEN_TIDS_2521020222501_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_TIDS_2521020222501_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_TIDS_2521020222501_TRIGGER`。

<a id="CONFIG_WSEN_TIDS_2521020222501_TRIGGER_MODE"></a>

## 163.18 `CONFIG_WSEN_TIDS_2521020222501_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_TIDS_2521020222501 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_WSEN_TIDS_2521020222501_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_WSEN_TIDS_2521020222501_TRIGGER_NONE
CONFIG_WSEN_TIDS_2521020222501_TRIGGER_GLOBAL_THREAD
CONFIG_WSEN_TIDS_2521020222501_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-TIDS-2521020222501 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_WSEN_TIDS_2521020222501`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_TIDS_2521020222501)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_WSEN_TIDS_2521020222501_TRIGGER_NONE`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_TIDS_2521020222501_TRIGGER_NONE)、[`CONFIG_WSEN_TIDS_2521020222501_TRIGGER_GLOBAL_THREAD`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_TIDS_2521020222501_TRIGGER_GLOBAL_THREAD)、[`CONFIG_WSEN_TIDS_2521020222501_TRIGGER_OWN_THREAD`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_TIDS_2521020222501_TRIGGER_OWN_THREAD)。

<a id="CONFIG_WSEN_TIDS_2521020222501_TRIGGER_NONE"></a>

## 163.19 `CONFIG_WSEN_TIDS_2521020222501_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WSEN_TIDS_2521020222501_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-TIDS-2521020222501 温度传感器（Temperature Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_WSEN_TIDS_2521020222501_TRIGGER_MODE`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_TIDS_2521020222501_TRIGGER_MODE)。

<a id="CONFIG_WSEN_TIDS_2521020222501_TRIGGER_OWN_THREAD"></a>

## 163.20 `CONFIG_WSEN_TIDS_2521020222501_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_WSEN_TIDS_2521020222501_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_WSEN_TIDS_2521020222501_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_tids_2521020222501/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-TIDS-2521020222501 温度传感器（Temperature Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_WSEN_TIDS_2521020222501_TRIGGER_MODE`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_TIDS_2521020222501_TRIGGER_MODE)、[`CONFIG_WSEN_TIDS_2521020222501_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_TIDS_2521020222501_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_TIDS_2521020222501_TRIGGER`。

<a id="CONFIG_XBR818"></a>

## 163.21 `CONFIG_XBR818`

**提示（Prompt）**：XBR818 雷达（Radar）

**说明（Help）**

启用 Phosense XBR818 雷达传感器（Radar Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PHOSENSE_XBR818_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/xbr818/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/xbr818/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_XGZP68XXD"></a>

## 163.22 `CONFIG_XGZP68XXD`

**提示（Prompt）**：CFSensor XGZP68XXD 压力传感器（Pressure Sensor）

**说明（Help）**

启用 CFSensor XGZP68XXD 压力传感器（Pressure Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CFSENSOR_XGZP68XXD_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/cfsensor/xgzp68xxd/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/cfsensor/xgzp68xxd/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_XMC4XXX_TEMP"></a>

## 163.23 `CONFIG_XMC4XXX_TEMP`

**提示（Prompt）**：XMC4XXX 温度传感器（Temperature Sensor）

**说明（Help）**

启用 Infineon XMC4XXX 目标平台上的温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_TEMP_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/infineon/xmc4xxx_temp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/xmc4xxx_temp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_XMC4XXX_TEMP_CALIBRATE_GAIN"></a>

## 163.24 `CONFIG_XMC4XXX_TEMP_CALIBRATE_GAIN`

**提示（Prompt）**：温度读数的增益调整（Gain Adjustment）

**说明（Help）**

温度读数的增益调整（Gain Adjustment），范围为 [0, 63]。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XMC4XXX_TEMP && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/sensor/infineon/xmc4xxx_temp/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/xmc4xxx_temp/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → XMC4XXX 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_XMC4XXX_TEMP`](P163_drivers_sensor_配置项参考_15.md#CONFIG_XMC4XXX_TEMP)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_XMC4XXX_TEMP_CALIBRATE_OFFSET"></a>

## 163.25 `CONFIG_XMC4XXX_TEMP_CALIBRATE_OFFSET`

**提示（Prompt）**：温度读数的偏移调整（Offset Adjustment）

**说明（Help）**

偏移调整（Offset Adjustment）定义为对转换结果的平移。该值为 7 位，范围为 [-64, 63]；原文给出的对应温度范围为 -/+12.5 °C。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XMC4XXX_TEMP && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/sensor/infineon/xmc4xxx_temp/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/xmc4xxx_temp/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → XMC4XXX 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_XMC4XXX_TEMP`](P163_drivers_sensor_配置项参考_15.md#CONFIG_XMC4XXX_TEMP)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<!-- kconfig-navigation -->

[上一章](P162_drivers_sensor_配置项参考_14.md) · [返回大纲](大纲.md) · [下一章](P164_drivers_sent_配置项参考.md)
